# Visual design: images, illustrations, icons, graphics, slides

For anything that is a picture rather than an interface: generated images, illustrations, icon sets, posters, social graphics, thumbnails, slides, brand boards, logos. Set the direction first (`direction.md`).

## Signs of slop

Ten categories; the slop level is the count with at least one sign, times 10%.

1. **Default subject matter.** Glossy blobs, orbs, liquid chrome, floating cubes, crystals, nebulas, rockets, lightbulbs for ideas, robots and glowing brains for AI, handshake for partnership, smiling diverse team at a laptop.
2. **Default palette.** Violet-to-blue or pink-to-orange gradients, neon on black, everything saturated, colored glow around the subject.
3. **Render tells.** Plastic skin, waxy airbrushing, HDR halos, every surface glossy, random bokeh, light from several directions at once, an over-perfect symmetry.
4. **Broken details.** Garbled or invented text, melting logos, wrong finger counts, objects that merge, patterns that do not repeat correctly, reflections that do not match, a fine checker pattern from "add film grain".
5. **No idea.** Several subjects, a busy collage, or a pretty picture that says nothing about the product. If you cannot describe it in one sentence, there is no idea.
6. **Composition by default.** Subject dead center, no room for text, text placed wherever is left, a hard rectangular image dropped on a page of a different color.
7. **Typography in graphics.** A default sans in bold everywhere, gradient or glowing text, centered paragraphs, more than two families, tracked caps, tiny unreadable lines, emoji as bullets.
8. **Icon sets.** Mixed styles and strokes, each icon a different color, pastel bubbles behind every icon, 3D glossy icons next to flat ones, a hand-drawn glyph among library icons.
9. **Slides and social graphics.** Title + three bullets + stock photo on every slide, a headline that could fit any company, a decorative shape in every corner, "✨ 5 tips to..." covers, logo soup.
10. **Style as a filter.** A print style (engraving, risograph, woodcut) or a trend (glass, clay 3D, grain) slapped on one image while the rest of the brand is plain, so it reads as a filter instead of a language.

## Product stills and demos

A faux UI shot or an animated product demo has its own rules: `product-illustrations.md`.

## Fix in passes

1. **Idea.** Write the subject as one concrete sentence from the product's world ("a single container ship seen from straight above on a calm grey sea" for a logistics API). Cut every subject that is not in the sentence.
2. **Style.** Choose one style that fits the character and keep it for the whole set. Styles that tend to work:
   - Painted background art: a calm sky or landscape with one subject, crisp clouds, soft light, open space for text. Warm, hopeful, human products.
   - Cinematic photo of one object: a real thing in simple dramatic light on a plain field. Calm, serious, trustworthy products.
   - Soft stylized 3D: one small scene with matte materials and gentle light. Playful, friendly products.
   - Product object render: a payment card, a phone, a package with true materials. Anything that touches the physical world.
   - Light and optics: one physical phenomenon on a dark field. Technical and data products.
   - Engraving or print: monochrome in one ink on a tinted page, only when the whole brand lives in that world with matching type.
3. **Palette.** 3-5 colors taken from the world and the page, named as hex values. One leads. The background color of the destination is one of them, so edges blend.
4. **Composition.** Decide where the subject sits and where text goes before generating ("subject on the right third, calm empty space on the left"). Leave the lower fifth calm if UI or a caption will sit over it.
5. **Type (for graphics and slides).** One family, two at most; size and color for hierarchy; one message per slide or graphic; left-aligned text blocks; real text in the layout, never baked into the image.
6. **Details.** Inspect at 100% and 200%: text, hands, edges, logos, repeated patterns, reflections. Regenerate or retouch anything broken. Add texture in code or in an editor, never by prompting for grain.
7. **Consistency.** Same light direction, same palette, same rendering style across the whole set. Icons: one family, one stroke, one size, one color role.

## Prompt recipe for image generation

Build the prompt in this order:

1. **Subject:** the one sentence, concrete and physical.
2. **Setting:** where it is, kept simple.
3. **Light and palette:** direction of the light, the hex values, and the destination background color so edges blend.
4. **Style:** one clear direction from the list above.
5. **Composition:** where the subject sits and where the empty space is; the aspect ratio of the slot.
6. **Exclusions:** no text, no letters, no logos, no UI, no watermark, no glow, no gradient background.
7. **Format:** twice the display size; never upscale a small image.

Rules:

- Show the user the prompt, the model and the size before any paid generation, and ask.
- Generate once, judge against the sentence and the palette, then change the prompt instead of rerolling the same one. Generate 3-4 candidates when the tool allows it and pick one.
- Single objects for a UI: one object, studio lit, on a plain background in the exact page color, soft contact shadow, the angle the layout needs. Remove the background if the tool can, otherwise mask it into the page color.
- To show real UI on a generated device, generate the device straight-on, lay real HTML over the screen and rotate both together, so the text stays sharp and true.
- Everything inside one visual tells the same story: the invoice number in the list is the one on the phone.

## Placing images

- Export WebP or AVIF at twice the display size, with an `alt` that says what is shown.
- Match the edges to the background, or fade them with a mask (`mask-image: radial-gradient(closest-side, #000 70%, transparent)`).
- Static, or one slow motion that fits the subject. No parallax.
- Give the image fixed dimensions so the layout does not jump.

## Hero images that carry a headline

For a landing hero or poster where a generated picture and the headline share the frame. The weak ones usually fail the same way: an entire product hovering in the middle under flat, shadowless light looks like a product catalogue, no matter how well it is rendered.

- **A single dominant subject** that the frame crops or that sweeps across it. Tiny figures inside a broad landscape fail twice: models garble small faces, hands and crowds, and the composition looks like stock.
- **Lighting with a name,** stated in the prompt together with where it lands. Leave it unstated and the model returns soft, uniform light.

| Setup | Where it fits | Result |
|---|---|---|
| A pair of colored gels from opposite sides | portraits, shiny products, tech | shape modelled by color; the brighter gel becomes the accent |
| Sun shafts cutting through haze | wellness, hotels, handmade goods | the subject inside the beams, which carry the accent |
| Direct flash from the camera | fashion, food, drinks, splashes | motion frozen, a hard shadow, believable skin |
| Only the product's own light | devices that glow or make sound | a dark scene lit by the subject, its glow shaped into something that crosses the frame rather than a halo around a centered object |
| A single spotlight on a black stage | dance, theatre, concerts | the performer lit and everything else falling away |
| Light passing through the accent material | glass, liquid, fabric, petals | the accent lit from within |
| Midday sun with crisp shadows | outdoors, sport, travel | saturated sky, sharp shadows, sparkle on snow or water |

- **A real surface behind the subject,** taken from the brand's world rather than a flat digital fill: limewash, handmade paper or linen for wellness and handmade goods; brushed metal, frosted glass or matte ceramic for hardware; enamel, glazed tiles or waxed paper for food; a paper backdrop sweeping into the floor with a shadow, or velvet, for fashion; sandstone, rubber or snow for sport; plaster or halftone print for culture.
- **Accent by measurement** (OKLCH). Two base colors, a dark one and a light one, separated by at least 0.4 in lightness, typically one clearly colored and one close to neutral. The accent is the most saturated color present: medium lightness, at or above 80% of the maximum chroma its hue allows at that lightness (around 0.2 for most hues, around 0.15 for greens and teals), and 120-180° of hue away from both base colors (never under 75°; anything below 0.04 chroma is treated as neutral). Warm accents on cool fields stand out most. It should fill 15-30% of the frame and live on the subject itself (its light, its paint, its material) before reaching the headline; a hairline or a small patch of accent leaves the image dull. The one exception: when a single strong light floods the scene and that light is the accent, it can share the field's hue family provided it is at least 1.8 times as saturated and 0.3 lighter.
- **The subject and the headline interact.** A luminous subject throws its light on the letters; a sweeping one (fabric, a cable) crosses in front of some letters and behind others; a remarkable material bleeds into a word; a static subject keeps clear of a large headline. Letters placed behind the subject keep the even spacing they would have without it, and the subject covers one letter at most, never its defining stroke (an L missing its base becomes an I). If the model splits the word around the subject, delete the headline from the image, mask out the subject, typeset the words in a real font underneath and layer the subject back over them.
- **The typeface follows the category:** a light, high-contrast serif for calm and luxury; a broad, heavy sans in two colors for devices; a bold grotesk in sentence case with its final word in the accent for software and studios; one giant condensed word for food, drinks and festivals; a tall condensed italic serif divided by the subject for fashion and culture; an accent-colored script word above a serif for audio, scent and beauty.
- **People** get one of the lighting setups, visible skin texture (pores, fine hair), grain and slight blooming on the hottest highlights. Poreless skin under flat light gives a render away first.
- **Products that usually look like catalogue shots** (watches, coffee, sneakers, fragrance): either crop very tight and let the accent form a shape that crosses the frame, or move the product into an unexpected setting. Fragrance surrounded by petals is what every fragrance ad already does.
- **Supporting type carries facts:** a wordmark, three to five navigation links, a single button and no more than three short captions stating a date, a spec, a price or a location. No slogans tucked into corners.
- **In a set of images,** no single layout covers more than half of them, and six or more images use at least four layouts; "copy on the left, subject on the right" and "giant word with the subject in front" are the model's defaults. Vary the button too (a round badge, a text link, an outline pill), and give one page only a wordmark and a single link.
- **Variants of one image** change one thing each (the crop, the moment, the camera height, how far the subject sweeps), so the user chooses between close neighbors instead of unrelated ideas.

Reject a render when it has: a tiny figure in a broad scene; a complete product hovering with even margins under flat light; a product glowing alone in empty darkness; poreless skin; a flat digital background; fire, lava or lightning used as ornament; distorted proportions; smudged dials, screens or fine print; an accent that is small, pale or too close in hue to stand out as the brightest element; a letter hidden or overlapped in the wrong place; slogans in the captions; a clever metaphor that obscures what is actually being sold.

## Code treatments for an image

To make a generated image belong to the page, on the main visual only and only when it fits the character:

- **Glyphs:** redraw the image as a grid of characters picked by brightness, taken from the product's material (`. : 1 7 4 0 $ %` for finance, `{ } < > = #` for code, letters of a word for reading). Cells of 6-10px in the interface's monospace, colored from the image or the ramp.
- **Halftone dots** sized by brightness, in one ink on the page color, for editorial and print characters.
- **Dithering** into two or three ramp colors, computed once on load, for retro, technical or playful characters.
- **Duotone:** brightness mapped onto the darkest surface and the accent; the simplest way to pull any image into the palette (`feColorMatrix`, or a greyscale image under a `mix-blend-mode: color` layer).
- Performance: read the pixels once on load, never inside the animation loop; prepare glyph atlases ahead of time; animate at 8-12 steps per second, changing a few cells per step; pause off screen; cap the canvas at 2x device pixel ratio.

## Logos and app icons

- A logo that is an emoji, a sparkle in a gradient tile, a glossy orb or a gradient wordmark is slop. Redraw it flat: the wordmark in the chosen type, or one simple glyph from the product's idea, in one solid color.
- App icons: 1024x1024, no transparency, one idea readable at 29pt, no text unless it is a single letterform.
- Keep a real existing logo as it is.

## Checklist

- [ ] The idea fits in one sentence and belongs to this product
- [ ] One style across the whole set; no trend used as a filter
- [ ] Palette of 3-5 named colors including the destination background
- [ ] Composition leaves room for text where text will go
- [ ] No garbled text, broken hands, melted logos or baked-in UI
- [ ] Icons: one family, stroke, size and color role
- [ ] Graphics and slides: one message each, one or two families, real text
- [ ] Template test: with a competitor's name on it, would it still fit? If yes, push the idea
