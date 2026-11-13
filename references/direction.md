# Direction

Slop happens when the model commits to the first, most common answer. A direction is the decision that replaces the default. Write it before touching anything in heavy mode, for UI and for visual design.

## The five lines

Derive every line from what the product does and who it is for, never from what is trending.

- **Product.** What it does, for whom, in one plain sentence.
- **Character.** Two or three concrete words, like `calm, exact, a little warm` or `loud, competitive, fast`. Banned: clean, modern, sleek, minimal, premium, beautiful. They describe every template.
- **World.** The place, object or material the product naturally belongs to. A note app lives near paper and ink, a monitoring tool near instruments and night shifts, a train app near the actual route and its landscape, a glucose tracker near morning light and food. The world sets the tint of the neutrals, the accent and the visual.
- **Moments.** One or two places where the screen gets rich color, material and detail, chosen from what the product shows: the main chart, a rendered card, an illustration of the route, the big number the user opens the app for. Everything else stays quiet.
- **Signature.** One small detail only this product would have, used consistently: a live status dot, keycaps, a route line, a seat number set like a ticket stub. One, not five.

If the product already has a real brand (a logo, a color, a typeface that is not slop), keep it and build the direction around it.

## A concept instead of adjectives

For a new look, find a visual concept the product can be built around, then derive type, layout, color, illustration and motion from it. Examples of the shape of a concept, not answers to reuse:

- A running app built around an athletics track: lane lines as dividers, bib numbers for figures.
- A sleep app that feels like a village going to sleep: lights turning off as the evening goes on.
- A plant app made of paper cut-outs.
- A language app that borrows from regional playing cards.

The concept must make the product feel like its own world. "Attractive" and "different" are not the same thing: ten polished AI apps side by side are one app.

Put the concept in a single sentence you can hold each later choice against, and give it two tests:

- **Walk it forward.** Empty, busy, finished: if the idea vanishes after the opening frame, it was a poster.
- **Make it exclude something.** A concept invented to defend a choice already made rules nothing out. It has to forbid at least one move you would otherwise make.

## When the product is not named

Ask. If asking is not possible, or you were told to proceed: for a mock or demo, pick one concrete, believable product that matches the features shown and write the direction for it, labelled `Product (assumed):` so the user can correct it. Do not build the world from some incidental word in the copy, and do not fall back on generic SaaS: the palette, type and accent need a specific world to come from. For a real product you know nothing about, stay neutral, assert nothing, and list the facts you would need.

## The moment

Two shortcuts look designed in a screenshot and say nothing: a flat drawing of an object from the product's field, or an oversized word sitting above a standard form. Before settling, sketch one idea in each of these five families, a sentence apiece:

1. **Behavior:** an interaction no other product would have. At rest it can look ordinary.
2. **Real content:** the product's actual data or output, given the care usually spent on decoration.
3. **Proportion:** the one thing that matters gets most of the screen; the rest gets out of its way.
4. **Type:** a single dramatic size jump, one oversized figure, or one sentence filling the screen, as long as it means something (the figure answers the question, the sentence updates with the state). Huge "Log in" letters mean nothing.
5. **A surface or object,** under the rules below.

Keep the idea that survives two checks. Described aloud without its styling, it still sounds like an idea: "big serif headline" fails, "the invoice total fills the page and every settled line strikes itself out" passes. And its resting state is already a finished composition from this product's world, since most visitors never get past it. Build the second state as well; a concept that was only drawn has not been tried.

### Fields and objects

Whether a field or object may carry the moment depends on how long people look at the screen:

- **Long or daily use** (an app, a dashboard, settings, an active chat): keep surfaces neutral and let content be the moment.
- **A brief passage** (sign-in, an empty state, a confirmation, a hero): a field or object can stay when someone who never heard the concept could explain why it is there; when it uses no more than three hues, all from the world; when it has depth, light and a point of focus (a soft two-color wash does not count); when the controls on top remain calm and readable; and when, at the size people see it, it could not pass for clip art or a template-gallery background (layered flat hills, a gradient sunset, a dashed path). After two failed tries, switch to another family of moment.

A gradient can stay as a material when it is the brand's or the brief's, or a shift within one hue family, has a reason in the world, uses the chosen palette and keeps the controls on top quiet. As ornament it goes.

Texture is never required. Add one layer at most, and only to solve a problem you can name:

| Layer | Earns it | Wrong when |
|---|---|---|
| Fine grain or stipple | A gradient shows banding or looks too digital; tactile, warm worlds | Spread over a plain fill because it is fashionable |
| Halftone | Gives structure to soft, photographic color | It competes with the copy |
| Contour lines | Maps, routes, terrain, data | Strong enough to become wallpaper |
| Rings around a point | There is one object to emanate from | No object sits at the center |
| Ribbed glass | A crisp, contrasty subject sits behind it | Nothing behind it, so it is just stripes |
| Pixel or reaction-diffusion patterns | Publishing, heritage and bold brands | A plain product interface, where it looks like a filter |

- **A material must justify itself.** Frost only works over something worth seeing through; a refraction needs a subject to distort, and text passing through stays whole. Chrome, liquid metal and glossy 3D in the abstract are defaults; they qualify only when the object means something to this product. A mark that performs a job (a lighthouse beam that sweeps during a backup) is worth more than one that gleams.
- **An object you borrow keeps its physics.** Paper is never faded in, the pins of a lock move the way pins move, and nobody writes a reply on the letter they just received.
- **Illustrations and characters belong to the page:** its colors, its ink, a single stroke weight, no heavy black fills or cartoon glove hands. One that looks like a sticker or emoji gets redrawn or dropped.

## Three directions before one

When there is no existing brand to follow, write three distinct directions (five lines each, different worlds or concepts), compare them against the product sentence, then continue with one. Show them to the user when you stop for confirmation. Committing to the first idea is the most common source of sameness.

For a UI, render the three as hero variants on the real content and show the pictures, not five lines of text: people pick from images in seconds and cannot judge a palette from its hex values. None of the three may be the "tasteful" fallback (cream page, graphite text and button, one muted accent, lots of empty space): that is what a model reaches for once the loud defaults are banned, and it reads as a template too. At least one of the three keeps the original's energy and shows the product working.

## Decisions, not adjectives

"Make it modern", "cleaner", "more professional" turn into the most average thing the model knows. Before building, the direction must contain decisions someone can check: the typeface and why, the background, text and accent colors as values, the references and what to take from each, and a short list of don'ts. If the user cannot say what they want, ask for two or three sites they like and one they dislike; that answers more than any adjective. Without it you loop: ten iterations that end where the first one started.

## Variants of one part, not whole pages

Do not regenerate the whole page to explore. Pick the part that matters (the hero, one section, a background) and make two or three genuinely different variants of only that, on the same tokens. Choose one, or ask for a new round based on the closest. Then correct with small, concrete requests ("bigger, lower, filling the box right of the headline without touching the text"), one change at a time. Fonts, palette and measures stay fixed across variants; only layout, copy and motion vary.

## Study references for structure, not looks

When the product sits in a known category (chat, banking, fitness, booking), look at 3-5 strong apps or sites in that category, from screenshots the user gives you or from your own browsing:

- Ask a named question first ("how do the best chat lists handle unread and pinned?").
- Extract numbers and structure, not vibe: row heights, type sizes, where the primary action sits, what is icon vs text, how the active state looks.
- What every reference does is a convention: keep it unless you have a reason. What only the best do is the bar. What all of them do badly is your opening.
- Stop when new references stop changing your notes.
- Name what to take from each one: one site's heading scale, another's spacing between sections, a third's loader. For motion and details that are hard to put in words, a library of real interface styles (for example styles.refero.design) gives the model something concrete. Never ask for a clone: it comes back as a worse copy with nothing of this product in it.
- Build desktop first if the reference is desktop, then decide for each strong idea whether it transfers to mobile or needs a different answer there. Do not just shrink it.

Never paste one product's look onto another. Turning every chat app into iMessage is a new template, and people notice.

## Diagnose before you design

Before researching or redesigning, render the screen and name its three biggest deficits in plain words ("three rows with the same weight, nothing leads", "the primary action is below the fold", "the illustration is clip art"). The direction must answer those three.

## When to stop

Not at "fewer signs than before". Stop when the result beats the original side by side, and when, side by side with the strongest reference, your result reads at least as well, and the template test passes.
