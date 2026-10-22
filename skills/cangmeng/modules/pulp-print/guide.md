---
name: neil-quentin
description: "Turn a user-supplied photograph into a 1990s pulp-print movie-poster composition: one high-chroma flat colour flooding the background, the subject flattened into hard-edged high-contrast shapes, a heavy condensed uppercase golden-yellow title, a tiny credit block at the foot describing the scene, and aged paper grain and wear across the whole sheet. Total palette is three to four colours. Works on day or night photos. Subject treatment scales from straight photographic with graded colour, through two-to-three-tone posterisation, to flat vector redraw, chosen by whether a face has to stay recognisable. Use when the user supplies a photo and wants it rebuilt as a printed poster with flat saturated colour, brutal contrast, and retro typography, rather than a restyled photograph or a modern flat-design graphic."
---

# neil-quentin v0.3

Turn a supplied photograph into a printed poster. Preserve the signature **平面高饱和、主体压硬边、金黄粗字、旧纸颗粒**:

- flood the background with one high-chroma flat colour;
- flatten the subject into hard-edged high-contrast shapes;
- nail one heavy condensed golden-yellow title across one end of the sheet;
- keep the whole palette to three or four colours;
- lay aged paper grain and wear over everything.

Return the generated image plus one brief creative rationale. Include the final prompt only when the user asks.

## Decision Priority 决策优先级

Resolve conflicts in this order:

1. Keep the palette at four colours or fewer.
2. Keep every subject-to-background boundary hard. This style has no soft edges and no gradients.
3. Keep the title golden-yellow, heavy, condensed, uppercase.
4. Keep the print texture present. Without grain this becomes modern flat design.
5. Preserve face recognisability when the source has a face that matters.
6. Preserve the subject's silhouette and spatial layout.
7. Fill the background with flat colour rather than photographic sky or wall.
8. Keep the credit block small, quiet, and subordinate.

Flatten before you stylise. Remove tonal steps before you add colour.

## Consent and Privacy 授权与隐私

- Treat a supplied photo plus a poster request as consent to generate; do not ask again.
- Send only the final prompt and the required reference image to the generation service.
- Do not browse, search, save, upload elsewhere, or share the user's source material.
- Do not save source or generated images into project files unless asked.

## Identity Boundary 身份边界

The style is borrowed; the film is not.

- **Never place a real film title on the poster.** Use the wording the user supplies. If none is supplied, author a short original phrase.
- **Never place real actor, director, or studio names anywhere**, including the credit block.
- The credit block carries a scene description authored for this image. It may be read; it must never name a real person, film, or studio.
- Do not reproduce the specific layout of an existing poster. Take the printing language, not the design.

## Read the Photograph First 读图

Build an internal **Scene Card**:

- **Face check:** is there a face that must stay recognisable? This single answer selects the subject treatment.
- **Subject:** the one element the poster is about.
- **Silhouette quality:** how cleanly the subject separates from its background. Hard geometry posterises well; soft or cluttered edges do not.
- **Background regions:** which areas are flat enough to be replaced wholesale by one colour — sky, wall, water, road, ceiling.
- **Native contrast:** where the source already has strong light-dark separation to build on.
- **Detail to sacrifice:** texture,材质, foliage, small clutter that must disappear when the image flattens.
- **Title zone:** which region is empty enough to carry the title without covering the subject.
- **Existing colour:** the dominant hues, and whether any is close to a usable background choice.

Daylight and night sources are both valid.

## Prompt Compiler 编译字段

Resolve these fields in order. Compile only what becomes pixels.

1. **Canvas:** 2:3 vertical unless the user requests otherwise, plus the frame strategy.
2. **Background colour:** the exact flat hue and how much of the frame it floods.
3. **Subject treatment:** which of the three tiers, and the tone-step count.
4. **Palette:** the full list, three to four entries, named exactly.
5. **Edge policy:** where boundaries must be hard, and what softness is being removed.
6. **Title:** exact wording, position, size share, colour, letterform.
7. **Sub-line and credit block:** the sub-line's presence and position; the credit block's position and its exact scene-description wording, written out in full.
8. **Print texture:** grain, wear, misregistration, ink unevenness.
9. **Detail sacrifice:** what disappears in the flattening.
10. **Hard avoids.**

## Colour System 配色

**Three to four colours total. This is the hardest constraint in the document.**

- **One background hue floods the frame.** Choose from the Variation Engine, or promote a hue the source already has. It is flat: no gradient, no clouds, no texture, no vignette.
- **The title is golden yellow**, approximately `#F2B610`. Not lemon, not orange, not amber. It stays this hue regardless of the background choice.
- **The remaining one or two colours** are near-black and off-white. They carry the subject and the small type.
- Skin, when a face is preserved, counts as one colour and must be pushed to a single warm tone rather than a full range.
- Do not add a fifth hue for an accent, a highlight, or a mood. If something needs separating, use value, not a new colour.

Reference values from the same family: `#F2B610` gold, `#B80102` vermilion, `#F7F7F7` off-white, `#010100` black.

## Subject Treatment 主体处理

Three tiers. **Select by the face check, not by taste.**

### Tier 1 — Photographic with graded colour 实拍直出

Use when a face must stay recognisable.

- Keep the photograph's real features, proportions, and expression. **Do not redraw the face.**
- Push skin to one warm tone, clothing to flat light or dark, shadows to a deep version of the background hue.
- Contrast goes up hard: highlights clip, shadows block, midtones thin out.
- The background is still replaced by flat colour. Only the subject stays photographic.

### Tier 2 — Posterised 二值化 / 三阶压缩

Default for architecture, objects, vehicles, landscape, and any figure that does not need to be identified.

- Reduce the subject to two or three tone steps. No smooth ramps between them.
- Preserve the silhouette exactly; sacrifice all interior texture.
- Windows, signs, and small openings become clean geometric holes filled with the background colour. This is what makes buildings read.
- Halftone dots or coarse screen texture are permitted inside the tone steps.

### Tier 3 — Flat vector redraw 平涂矢量

Use only when the subject is simple and contains no face.

- Rebuild the subject as flat filled shapes with no shading.
- **Never use this tier on a face.** Redrawn faces collapse.

**Tiers may be mixed within one image:** the subject on Tier 1, the background architecture on Tier 2. This is the strongest configuration for photos of people in a place.

## Typography System 文字

- **Title:** heavy, condensed, uppercase, squared terminals, retro slab or grotesque. Occupies 8%-15% of frame height. Golden yellow. May carry a same-family offset shadow in the background hue.
- **Placement:** top band, bottom band, or overlapping the subject. It must sit in a region the Scene Card marked as empty.
- **Wording:** exactly what the user supplies. If none, author one short original phrase of one to three words. Never a real film title.
- **Sub-line:** optional single line beneath the title, smaller, off-white or yellow.
- **Credit block:** a dense block of very small type at the foot, **four to seven lines**, each running **eight to fourteen words**, spanning 60%-80% of the frame width. It carries **a full plain-English account of the scene in the source photograph, authored from the Scene Card** — the place, what is happening, the light and the hour, the weather, the surfaces and materials, what the subject is wearing and doing. Write continuous prose, not a list. Set the last line noticeably shorter and centred, the way a real billing block tapers.

  Set it in the off-white or the gold. Size it so the block fills its lines densely rather than to a fixed cap height — **density is the point**. At poster scale nobody reads it; the block exists as typographic texture.

  Print the credit text directly onto the already-existing flat background field. The background colour and paper texture must pass behind every line uninterrupted. **Never create a dedicated backing for the credit block:** no panel, box, band, ribbon, label, stroke, outline, text shadow, glow, or local darkening or lightening behind the letters.

  Real sentences are used, not invented ones, because real words give the model coherent shapes to set. Invented text collapses into a band of noise. No real names, film titles, or studio names.
- Keep all type on the same axis. No rotated, curved, or scattered lettering.

## Print Texture 印刷质感

Mandatory. Without it the result is modern flat design, not a printed poster.

- Aged paper grain across the entire sheet, including the flat colour field.
- Edge wear, a soft crease line, light staining or foxing.
- Slight misregistration: one colour plate offset by a hair.
- Uneven ink coverage in the flat field — subtle mottling, never a gradient.
- Optional inset border: an off-white rule inset 3%-5% from the trim, with paper tone outside it.

## Frame Strategy 画幅策略

- **Full bleed:** content fills the whole vertical canvas. Default.
- **Widescreen inset:** the composition is a wide horizontal band centred in the vertical canvas with flat dark bands above and below.
- **Angled inset:** the content block is rotated a few degrees, corners cropped, flat colour surrounding it.

**Practical note for widescreen and angled inset:** image models render precise geometric bands unreliably — they drift, gradient, or get ignored. When the user wants either, prefer generating at the wide aspect ratio and compositing the bands afterwards in an editor. State this rather than fighting the model.

## Variation Engine 变化引擎

Choose one option per axis before compiling.

| Axis | Options |
|---|---|
| background hue | vermilion red / cobalt blue / deep black / warm cream / traffic orange |
| subject tier | photographic graded / posterised 2-tone / posterised 3-tone / flat vector |
| title position | top band / bottom band / overlapping the subject |
| title weight | extra-bold slab / condensed grotesque / rounded retro slab |
| credit block | centred foot / right-aligned foot / none |
| border | inset off-white rule / none |
| print wear | light grain only / grain plus crease / heavy wear and staining |
| frame strategy | full bleed / widescreen inset / angled inset |

**Compatibility rules**

- `subject tier: flat vector` is forbidden when the Scene Card face check is positive.
- `background hue: deep black` requires `subject tier: posterised 2-tone` or `flat vector`; a photographic subject on black loses its edge.
- `title position: overlapping the subject` requires the subject to occupy less than 60% of the frame.
- `frame strategy` other than `full bleed` triggers the practical note above.

## Prompt Shape 提示词结构

Write the final prompt as four compact paragraphs:

1. **Canvas and colour:** aspect ratio, the exact background hue and how much it floods, the complete palette listed by name, and the statement that no fifth colour is allowed.
2. **Subject:** which tier, the tone-step count, what stays recognisable, what texture is sacrificed, and that every boundary is hard with no gradient.
3. **Type and print:** exact title wording, its position, size share, colour and letterform; the sub-line; the credit block's exact scene-description wording, its position and size; state that the credit prints directly on the uninterrupted flat field with no backing, outline, shadow, or local colour change; grain, wear, misregistration, and any border.
4. **Hard avoids.**

State what disappears as clearly as what remains.

## Generation Workflow 执行流程

1. Inspect the supplied photo. Build the Scene Card.
2. Run the face check and select the subject tier from it.
3. Select one complete variation recipe; check the compatibility rules.
4. Fix the background hue and write out the full palette, three to four entries.
5. Decide what detail is sacrificed in the flattening.
6. Resolve the title wording, position, and letterform. Use the user's words; never a real film title.
7. Resolve the sub-line, credit block, border, and print wear.
8. Compile the four-paragraph prompt.
9. Generate with the supplied photo as reference.
10. Inspect at full and thumbnail scale against the Quality Gate.
11. Regenerate at most once with a targeted correction.
12. Return the image and one brief rationale.

## Targeted Correction 定向修正

Regenerate at most once, correcting only the observed failure:

- **Too many colours:** name the offending hue and instruct it be merged into the nearest palette entry.
- **Soft edges:** restate that every subject-to-background boundary is a hard cut with no feathering, glow, or gradient.
- **Background not flat:** restate the sky or wall as one solid colour with no clouds, gradient, or vignette.
- **Title hue drifted:** name the exact gold and state it is neither lemon nor orange.
- **Title too light or too wide:** restate heavy, condensed, uppercase, squared terminals.
- **No print texture:** restate paper grain across the whole sheet, edge wear, and slight misregistration.
- **Face collapsed:** drop to Tier 1 and state the face must remain photographic and unredrawn.
- **Subject lost in the background:** raise contrast at the boundary or switch the background hue to a further value.
- **Credit block came out as noise or garbled letters:** restate the exact sentences verbatim, then step the density down one notch at a time — seven lines to five, five to four — until words form. Do not drop below four lines; a thin credit block loses the texture the block is there for.
- **Credit block gained a backing, outline, or shadow:** restate that the letters print directly on the uninterrupted flat background field; remove every panel, box, band, ribbon, label, stroke, outline, text shadow, glow, and any local darkening or lightening behind the text.
- **Real title or real names appeared:** replace with the user's wording and re-run; this is a hard failure, not a stylistic one.
- **Bands drifted or gradiented** (widescreen or angled inset): stop fighting it. Generate at the wide aspect ratio and composite the bands in an editor.

## Hard Avoids 负面约束

Avoid photographic realism, film-still look, cinematic lighting, modern flat design, gradient backgrounds, vignettes, soft or feathered subject edges, depth-of-field blur, glow, neon, bloom, 3D rendering, drop shadows on the subject, clean grain-free surfaces, five or more hues, accent colours added for mood, pastel or desaturated palettes, lemon or orange substituted for the gold, thin or light title weights, script or handwritten titles, rotated or curved lettering, invented or garbled lettering in the credit block, any backing panel, box, band, ribbon, label, stroke, outline, shadow, glow, or local colour change behind the credit block, real film titles, real actor or director names, real studio logos, direct reproduction of an existing poster layout, redrawn faces, extra or malformed fingers, and watermarks.

## Output Format 输出格式

```markdown
![neil-quentin v0.3](absolute-image-path-or-rendered-image)

**创作思路**

[One short Chinese paragraph: the background hue, which tier the subject took and why, what was sacrificed in the flattening, and where the title sits.]
```

Keep the rationale to one to three sentences. Include the full prompt only when the user asks.

When running in an environment without image generation, return the compiled four-paragraph prompt instead, plus the recipe line.

## Quality Gate 质量门

Before returning, verify:

- Can you count four colours or fewer in the whole sheet?
- Is the background one flat colour with no gradient, clouds, or vignette?
- Is the title the specified gold, and heavy, condensed, uppercase?
- Does the title occupy 8%-15% of frame height and sit clear of the subject's key features?
- Is every subject-to-background boundary a hard cut, with no feathering or glow anywhere?
- Is paper grain visible across the entire sheet, flat colour field included?
- Is there edge wear, and at least a hint of misregistration?
- If the face check was positive, is the face still photographic and recognisable?
- If posterised, does the silhouette survive while interior texture is gone?
- Do windows and openings read as clean holes filled with the background colour?
- Does the credit block read as set type rather than a noise band, and does it name no real person, film, or studio?
- Is the credit block printed directly on the uninterrupted flat background field, with no backing, outline, shadow, glow, or local colour change behind it?
- **Does the sheet carry no real film title, actor name, director name, or studio logo?**
- Is the layout distinct from any specific existing poster?
- At thumbnail scale, does the title still read and the subject still hold its shape?
- Would a viewer call this a printed poster rather than a filtered photograph?
