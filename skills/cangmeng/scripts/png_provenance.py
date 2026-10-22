"""Lossless, limited PNG AI-provenance metadata inspector/cleaner. Stdlib only."""
from pathlib import Path
import argparse, hashlib, json, struct, zlib

SIGNATURE = b'\x89PNG\r\n\x1a\n'
COLOR = {b'iCCP',b'sRGB',b'gAMA',b'cHRM',b'cICP',b'PLTE',b'tRNS',b'sBIT'}
MARKERS = (b'aigc', b'c2pa', b'ai provenance', b'ai-generated', b'ai generated')

def chunks(data):
 if not data.startswith(SIGNATURE): raise ValueError('Only PNG input is supported.')
 pos=8; result=[]
 while pos < len(data):
  if pos+12>len(data): raise ValueError('Truncated PNG chunk.')
  length=struct.unpack('>I',data[pos:pos+4])[0]; end=pos+length+12
  if end>len(data): raise ValueError('Truncated PNG payload.')
  kind=data[pos+4:pos+8]; payload=data[pos+8:pos+8+length]
  crc=struct.unpack('>I',data[pos+8+length:end])[0]
  if zlib.crc32(kind+payload)&0xffffffff != crc: raise ValueError('PNG CRC mismatch.')
  result.append((kind,payload,data[pos:end])); pos=end
  if kind==b'IEND':
   if pos != len(data): raise ValueError('Trailing bytes after IEND; not modified.')
   return result
 raise ValueError('Missing PNG IEND.')

def is_provenance(kind,payload):
 if kind==b'caBX': return True
 if kind not in (b'tEXt',b'iTXt',b'zTXt'): return False
 # Never decompress arbitrary metadata or remove an unrelated copyright field.
 key=payload.split(b'\0',1)[0].lower()
 if any(m in key for m in MARKERS): return True
 if kind in (b'tEXt',b'iTXt') and key in (b'xml:com.adobe.xmp',b'description',b'software',b'comment'):
  return any(m in payload.lower() for m in MARKERS)
 return False

def fingerprint(items,kinds):
 return hashlib.sha256(b''.join(raw for kind,payload,raw in items if kind in kinds)).hexdigest()

def process(source,output=None):
 data=source.read_bytes(); original=chunks(data)
 selected=[(k,p,r) for k,p,r in original if is_provenance(k,p)]
 kept=[(k,p,r) for k,p,r in original if not is_provenance(k,p)]
 report={'format':'PNG','input_bytes':len(data),'detected':[{'chunk':k.decode('ascii'),'bytes':len(p)} for k,p,r in selected],
  'scope':'C2PA caBX and explicitly identifiable AI provenance text; no invisible watermark claim',
  'idat_sha256_before':fingerprint(original,{b'IDAT'}),'color_sha256_before':fingerprint(original,COLOR)}
 if output:
  if output.resolve()==source.resolve(): raise ValueError('Source must remain unchanged.')
  encoded=SIGNATURE+b''.join(r for k,p,r in kept)
  with output.open('xb') as f: f.write(encoded)
  after=chunks(output.read_bytes())
  report.update(output_bytes=len(encoded),removed=report['detected'],remaining_supported=len([1 for k,p,r in after if is_provenance(k,p)]),
   idat_sha256_after=fingerprint(after,{b'IDAT'}),color_sha256_after=fingerprint(after,COLOR))
  report['compressed_pixels_unchanged']=report['idat_sha256_before']==report['idat_sha256_after']
  report['color_configuration_unchanged']=report['color_sha256_before']==report['color_sha256_after']
 return report

def main():
 ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('command',choices=['identify','clean']);ap.add_argument('input',type=Path)
 ap.add_argument('--output',type=Path);ap.add_argument('--report',type=Path);a=ap.parse_args()
 if a.command=='clean' and not a.output: ap.error('clean requires --output')
 if a.command=='identify' and a.output: ap.error('identify never writes an image')
 if a.report and (a.report.exists() or a.report.resolve() in (a.input.resolve(),a.output.resolve() if a.output else None)):
  ap.error('report must be a new path separate from input/output')
 try: result=process(a.input,a.output if a.command=='clean' else None)
 except (ValueError,OSError) as e: ap.exit(1,str(e)+'\n')
 text=json.dumps(result,ensure_ascii=False,indent=2)
 if a.report:
  with a.report.open('x',encoding='utf-8') as f: f.write(text+'\n')
 print(text)

if __name__=='__main__': main()
