"""Discover named optional local skills. No download, execution, or copying."""
from pathlib import Path
import argparse,json
NAMES=('scene-distillation-zine-v1-3','scene-to-art-lab','tait-crt-interface-skill','culture-fragment-poster-engine','create-photo-flipbook-ui','xxd-panel-224','xxd-panel-100','xxd-panel-028','remove-ai-watermarks')
def main():
 ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--root',type=Path,action='append');ap.add_argument('--json',action='store_true');a=ap.parse_args()
 roots=a.root or [Path.home()/'.codex/skills',Path.home()/'.agents/skills']
 result=[]
 for name in NAMES:
  paths=[r/name/'SKILL.md' for r in roots]
  found=next((p for p in paths if p.is_file()),None)
  result.append({'skill':name,'available':found is not None,'guide':str(found.resolve()) if found else None,'license':'governed by the separately obtained upstream skill; not this repository MIT license'})
 print(json.dumps(result,ensure_ascii=False,indent=2) if a.json else '\n'.join(f"{x['skill']}: "+('available' if x['available'] else 'not installed') for x in result))
if __name__=='__main__':main()
