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

## Three directions before one

When there is no existing brand to follow, write three distinct directions (five lines each, different worlds or concepts), compare them against the product sentence, then continue with one. Show them to the user when you stop for confirmation. Committing to the first idea is the most common source of sameness.

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

Not at "better than before". Stop when, side by side with the strongest reference, your result reads at least as well, and the template test passes.
