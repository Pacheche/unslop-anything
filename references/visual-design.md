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
