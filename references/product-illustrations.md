# Product illustrations: faux UI stills, demos and feature grids

Use this for any drawn or coded picture of a product's interface: the shot beside a landing-page headline, a feature card, a bento grid, a docs header, a slide or social graphic, or a short animated walkthrough with or without a pointer. It is neither a screenshot nor a working app. Like any visual job, it starts from a direction (`direction.md`). Live product screens are fixed with `ui-signs.md` and `ui-passes.md` instead.

A good one passes three tests: a stranger recognizes the product, the frame was chosen rather than defaulted, and nothing moves without a reason.

## Signs of slop

Ten categories; the slop level is the count with at least one sign, times 10%.

1. **Overloaded.** Every row carries real text, figures and a badge; every pane is full. The more detail, the more it looks generated.
2. **Wireframe.** A couple of grey blocks and a button, type shrunk to 7-10px, nothing left that says which product this is.
3. **Boxed or floating.** The entire window scaled down inside a card with equal air on all four sides, or set on a tinted plate on a white or dark page: a screenshot dropped in, not a product shot.
4. **Flat.** All objects share one weight and one bordered card. No focal point.
5. **Generic look.** Default grey chrome instead of the product's own tokens, or the style the brief asked for (blueprint, glass over color, a mascot, a poster palette) quietly dropped.
6. **Bad crop.** Words, buttons, chips or shadows sliced by the edge; an empty corner; a void below a list; a phone shown tiny and whole.
7. **Type and spacing.** Text touching edges, rows far taller than their content, rows spread out to fill height, edges that almost meet.
8. **Icons and logos.** Glyphs drawn by hand, mixed families, emoji standing in for icons, sparkles meaning "AI", a letter in a colored square posing as a logo, a real company name beside a made-up mark.
9. **Color.** Hue-to-hue gradients, glows, a ring and halo drawn round the hero to point at it, see-through layers overlapping, text too faint for its ground.
10. **Motion.** Content that blinks from one state to the next, a pointer wandering with no purpose, a reset nobody caused, numbers running backwards on screen, a payoff that opens empty.

What fixes most of these: a complete screen in calm neutrals, real wording only where the story happens, placeholder lines everywhere else, air around the subject, and a crop that leads the eye to the action. Cut words, keep context. Empty corners, a gap under a list, stretched rows or a window adrift on a plate look unfinished rather than minimal.

## Plan before drawing

Write five things down first: the slot on the page, the focal object, the single action, the payoff, and what stays out.

- **Medium.** A still or an animation, and if animated, whether it loops, plays once when scrolled into view, or runs on hover.
- **Size.** Draw at the size the viewer gets and display at 1:1. Rough starts: about 720 × 340 beside headline copy, 900-1100 wide across a full-width hero, 400 × 300 for a card, 500-560 wide for a lone card in a 680px article column so its text lands at 15-20px. Below about 320 wide a demo stops working; a grid tile or a small satellite card can go smaller.
- **Phone column.** If the picture can end up in a phone-width column, give it a second composition at that width (about 358): a tighter crop, the satellite dropped or stacked, action and payoff still whole. Recompose; do not shrink.
- **Fidelity.** Minimal (placeholder lines only), standard (words where they mean something, lines elsewhere) or realistic (believable content throughout). Standard is the default. Go realistic at hero scale, when the brief names a real product, or when the still is about a list or a whole page.
- **Story shape** (animations). Pick from what users value the product for: the feel of one gesture with its result under the hand; a short flow told as one continuous object; or the system acting on its own, with the effect landing somewhere else and a visible link between cause and effect, usually without a pointer. Three to five beats ending on a payoff; a hero loop runs 10-16 s. When a richer story fights a calmer frame, keep the frame.
- **A reference.** Choose the strongest comparable example you have (the product's own marketing, a product site you admire) and keep its still open beside yours. If yours looks emptier, flatter or smaller, start there.

## Look

- Take the look from the product. With its code available, read the tokens before drawing anything: CSS custom properties, a Tailwind config, a theme file, or failing that the computed styles of a real button, input, menu and card. Carry over the primary color, page and card backgrounds, text greys, border color, font stack, radius scale (inputs, menu rows, popovers and cards), input height and menu-row height.
- For another company's product, read the same values from its public site. Borrow values, not assets: no fonts or images without a licence.
- Compare a still with a screenshot of the real product at equal scale. Accent, grey temperature, corner radii and type should agree at a glance; when a control feels foreign, measure its real styles again rather than adjusting by eye.
- Tokens change; behavior does not. Keep the product's real interaction timing wherever it helps people recognize it.

## Framing

Choose the frame before building the screen. The crop decides what needs drawing and how large the type has to be.

1. **One lead object.** Supporting pieces are optional, never more than two, and each must earn its place: a receipt, a phone, a card with detail.
2. **Keep the identifying parts:** a title, the real chrome, the rows that explain why the action happens. Logo and navigation can go; crop around the story.
3. **Only filler may be cut.** The payoff, the action, anything the pointer touches and all real wording stay inside. A list, diff or terminal may lose one line off a bled edge. A placeholder button that the crop would cut gets deleted instead. The most common fault is a button, chip or shadow clipped by the stage edge.
4. **Let the hero bleed.** The window or phone covers at least two thirds of the stage width and runs 10-40% past an edge. Controls with labels stay complete. Shapes that still read when partly hidden, such as cards, slider tracks or avatar rows, should lose at least a third, so the cut looks intended.
5. **The stage clips everything,** with one rounded corner per edge. Use fades only on moving tracks, stacks and charts, plus one crop: a window dissolving at its foot over filler, done with a mask rather than a color wash, never on a side, never over the subject, never on two windows in one scene.
6. **Satellites sit across the hero's edge, roughly half outside,** over its chrome or margin (sidebar, header), never over its content. One placed entirely outside gets a 1px leader ending in a dot to tie it back.
7. **A second satellite is a different kind:** pair a card with something small from the system (a notification at true size, a chip, a receipt). Two same-width cards on one edge read as a pile. If the second object only points at something, an annotation does that job better.
8. **One gutter.** The hero's distance from the stage edge sets the gutter, and every other edge distance in the frame repeats it. Missing it by a few pixels, or crossing an edge by less than 24px, looks accidental: give a full gutter or go well past.
9. **Windows keep device proportions:** 1.25:1 or wider when whole, at least square in what shows when bled. Change the crop or layout; never squash.
10. **Whatever the story opens stays inside,** a gutter from every edge in every frame. Put the trigger where its menu or popover has room.
11. **No empty corners,** at rest or at any point in the loop. Fix crop or layout first; add a satellite only if it has a job.
12. **The page is the ground.** On a white or dark page there is no plate or tinted panel behind the device. On a colored stage, inset the hero 8-20% from both sides and let it run off the bottom, so color frames it on three sides.
13. **Straight and frontal by default.** A tilt has to beat the flat version at final size. Depth comes from shadow, stacking, scale and opacity; perspective only on request.
14. **Popovers, menus and toasts are not satellites.** They appear where the product would put them.
15. **The smaller the slot, the harder the crop.** A 400px card fits a third of a dashboard at true size, not the whole thing at a third of its size. A full screen shrunk until its text is illegible is the boxed failure.
16. **A wide tile with a narrow picture** leaves a blank strip beside the window: size the picture to its tile at every width, or crop it off the tile's edge.

A complete window with even gutters is acceptable only when the brief wants it and its contents stay readable. Never pick it by default.

### Starting compositions

| Composition | Hero placement | Good for |
|---|---|---|
| Bottom bleed | 8-12% in from left, right and top; 15-35% below the bottom edge; optional satellite on a side | Feature cards, grid tiles |
| Corner bleed | 10% in from top and left; 15-35% past right and bottom; satellite on the left or bottom edge | A hero next to headline copy |
| Colored stage | 8-20% in from each side over a colored ground, running off the bottom | Brand moments |
| Satellite leads | Hero cropped hard as context; a large satellite (30-40% of hero width) tells the story | A single small result, like an alert, a receipt or a code change |
| Wide hero | A 900-1100px window at 1:1, in from the top, off the bottom and often the sides; realistic content | Full-width homepage heroes |
| Window row | Three or four windows at one height, the outer ones cut by both sides; one brought forward by depth | Parallel sessions, tabs, agents |
| Desktop and phone | Desktop 75-80% wide, in from top and left, off the bottom; phone across the right edge, a third outside, there from the first frame | Stories that cross devices |
| Repetition | A grid of one small item running off every edge; one item lifted by depth and the only one with words | Showing scale |
| Close-up | The whole window enlarged 1.3-1.6x with its chrome, off the bottom; the row in question whole | A card about a single control |
| Setting and effect | Settings panel overlapping the product's empty margin, joined by a single leader to the element it alters | A toggle or theme and its result |
| Two views | A smaller chromeless card in front, its edge aligned to a structural line of the window, covering only filler | One event seen from two sides |
| Stacked components | Two components at one width, 12px apart, the lower one cut by the bottom | A control above the detail it drives |
| Opposite corners | Text anchored low on the left, product UI entering from the upper right | Grid tiles with a line of copy |
| Paper pile | Three equal cards at about -6°, 4° and -2°, offset 12-20px; only the top one has words | Receipts, tickets; the one place a tilt pays off |
| Corner chip | A small pill sitting on the window's corner, half outside, over chrome | One live fact about the whole product |
| Customer row | Three windows at one height, desaturated, fading at the foot | Customer or integration screens whose colors would clash |

### Phones

- Size a phone next to a window at 40% or more of the visible window width, 220px minimum; let it run off the bottom instead of shrinking it.
- Notifications keep their real proportions, spanning the screen less the system margins. If a banner would need enlarging to read, the phone is too small. The crop never cuts a banner.
- Cropping a phone at the top removes the status bar and the navigation bar together; the cut falls inside the content.
- In a narrow column the phone is cropped: one gutter on one side, cut by the other. Never small and whole.
- Status bar, home indicator and island come from an accurate device frame, never redrawn. Nothing sits under the island; sheets begin below the status bar. The screen is lit from the first frame.
- A notification story sits on the lock screen; never invent home-screen icons as a backdrop.
- A phone across a window never covers the figure or state it is there to explain.

## The screen

### Restraint

- **Budget the words:** the title, the object acted on, anything typed, the outcome. Three to seven strings is typical; placeholder lines carry the rest.
- **Budget words, not parts.** A calendar still needs a full week, a search a set of results, a filter enough rows to filter.
- **Words where the eye goes, lines at the edges.** Placeholder lines in the focal area look unfinished. Where the story touches a list, show two or three real rows and no more placeholder rows than that. A realistic list of six or more rows has at most as many placeholders as real ones.
- **Placeholder lines sit where text would,** keeping the real row's height and pitch, with widths that vary (60, 45, 70, 52%).
- **Small surfaces get one-line rows:** avatar, name, value. No grey line tucked under a real name.
- **Pairs agree:** label and value are both words or both lines. An empty pill next to a real control should go.
- **Keep what makes the domain recognizable:** album art in a music app, thumbnails in a file browser, faces in a team list. Replacing it with the feature's signal turns the screen into any list.
- **One big number;** the rest are lines.
- **State the feature once,** not in the header, the satellite and every row at the same time.
- **A fictional brand gets no masthead:** no monogram, logo, sidebar and navigation crammed into every crop. Show a product name only where the real product shows it and the brief needs it.
- **The payoff gets the space.** No empty band in the middle of the window while the result is squeezed against the crop.
- **Read the silhouette first:** at thumbnail size, subject, support and empty space should form one clear shape.
- **Keep proportions real.** The lead element is as large as it would be on an actual screen, not inflated.
- **Pick copy that fits:** names, emails and amounts whose length suits their slots, so nothing truncates, wraps or ends ragged.

### Type

- Size as the real UI would (11-15px at design size: about 13-14px for names, 11-12px for metadata), then let the stage scale it. Shrinking type to fit more rows is the wireframe failure; drop rows instead.
- A single typeface: whatever the product ships, else the system stack. Keep monospace for code, IDs and aligned figures.
- Small text needs a line height of at least 1.3 and proper insets.
- Sentence case unless the product uses capitals. Build hierarchy from space and a single weight step.
- The fake app's title is a styled element, not an `h1`-`h6`: the illustration lives inside someone else's document outline.
- Make text fit its control before touching the box. Never widen a container to hide an overflow.

### Spacing and alignment

- 12px between words and the edge of any window, card, panel or highlighted row; below 8px is a fault. Placeholder lines may run to an edge; words may not.
- Rows: 12px padding, 8px in dense lists. A single-line row three times the height of its text is padding, not calm.
- A title and its subtitle read as one unit with 4-6px between them. Space groups: a title sits nearer its own metadata than the next record. Do not distribute rows to fill a height.
- 8-12px between a button and the field or edge above it.
- A fixed 8-12px gap between text and any neighboring box.
- Nested shapes have equal padding on every side, and the outer radius is the inner radius plus that padding.
- Edges 1-3px apart look like a mistake: align them exactly or separate them by 8px or more.
- Columns share one grid with fixed tracks; a missing value leaves its track empty.
- Dots, badges and rings stay fully inside the content edge, 6px clear, in the gutter or on the avatar, never as a column of their own.
- Optical centering: center a label on its cap height and baseline rather than its line box (`text-box: trim-both cap alphabetic` where supported). A centered price centers its digits and hangs the currency sign outside.
- Hover and selection fills are inset with rounded corners unless the product's are square.

### Icons and logos

- Icons come from an existing set: the product's own first, otherwise one family chosen deliberately, at one size and stroke. Inside the illustration use the product's own icon size; when unknown, 14-16px at design size, which the stage scales like the type (live UIs follow `ui-signs.md`). A glyph drawn by hand never matches the weight of its neighbors.
- At 14px and under, and inside tinted tiles, prefer filled icons; fine outlines turn wiry.
- One opaque color per icon. For a quieter icon use a lighter opaque grey, or lower the opacity of the whole icon, never of its strokes: a translucent ink darkens wherever strokes overlap (`[scan]` translucent-icon).
- An icon cut by its own box gets a fitted viewBox, not a smaller box.
- Emoji belong in messages and reactions, not in place of icons.
- An AI feature is shown by what it produces. No sparkle, wand or star as decoration and no purple as the "AI color"; keep the product's own icon even if it happens to be a sparkle.
- No made-up logos: a letter on a colored square is not a brand. Use the real mark from its official source, in its own colors and proportions, contained without stretching and sized by eye so narrow and wide marks carry equal weight; or set the name as plain text. A real company with a fake mark never ships.
- Third-party marks keep their colors even inside a monochrome interface; only whole screenshots of other products may go grey, as in the customer row.
- Show only the integrations the story needs, in equal tracks, aligned by eye.
- A drawn physical object keeps its anatomy at any size: a payment card's chip is about an eighth of the card's width and a third of the way down, with name and number along the bottom and the network mark bottom right.
- A progress ring is one track and one arc with round caps; a number inside it centers on its digits.

### Color

- One neutral family for window, sidebar and cards. Start with about five inks and one accent; status colors only for status.
- Calm is not faint: check text and actions against the actual ground.
- Hue-to-hue gradients and colored glows stay slop here too (`ui-signs.md`). A gradient is kept only when it is the product's own or the brief's, with a deliberate direction; a shift within one hue family or a neutral is fine.
- Do not mark the hero with an accent ring and halo. Raise it the way the product would: its own surface, a stronger shadow, a label in the accent.
- Nothing translucent overlaps: stacked avatars, chips and cards are opaque.
- In dark themes depth comes from lighter surfaces, not shadows. A light document over a dark workspace remains a legible light document.
- Check every look the brief names. A light version passing proves nothing about dark.

### Chrome and devices

- System chrome is copied from a reference (the live app or a capture), not recalled.
- Use chrome that explains the task. Browser chrome only when the browser matters; a desktop app keeps its real chrome; a share dialog makes sense only with the file, who can access it, and the invite button.
- Sidebars and columns run the full height of their window; one that stops short leaves a seam.
- Platform conventions stay. Messages' blue bubbles with the plus and mic, a macOS window's traffic lights and an iOS banner at true size are the product's chrome. Invented accents get removed, conventions do not.
- With several windows, pick the active one and push the others back with lower contrast and lighter shadows.

## Feature grids

A bento grid by default is a costume (`ui-signs.md`); a grid that has been planned as one composition is not. Plan it as a table before building: tile, span, kind, the single thing it shows, its words.

1. **Mix the kinds.** Screens fill somewhere between 33% and 50% of the grid; the others are something else (see below).
2. **One lead tile,** larger (two columns or two rows), with the strongest picture.
3. **A UI tile shows one component,** at real size or larger, not a whole window. Window chrome appears once in the grid at most, on the lead tile.
4. **Alternate neighbors** across and down: picture beside number, dense beside calm. Never two window crops side by side.
5. **Large type counts as a tile:** one real figure at 48-72px with a short lead-in and a one-line label, figure and unit on one line; or a single short statement set large. Only true figures; never "10x" filler.
6. **Copy stays short and outside the picture:** one to four words or one sentence, 17-24px page type, in the same position on every tile.
7. **Shared frame, varied contents:** one radius, gap and padding for all tiles; the gap equals the inner padding or a clear fraction of it.
8. **Nothing repeats** from tile to tile: no string, avatar or chrome appears twice.
9. **Grounds work as a set:** one shared surface with a single photo, accent or inverted tile as punctuation, or several grounds whose lightness and temperature form a rhythm.
10. **One tile leads the motion.** Supporting tiles do one small thing once as the grid enters (staggered as `polish.md` sets for grid tiles) or on hover; only the lead tile may run a short story.
11. **Each tile at 1:1, recomposed when narrow.** Never scale the grid down as one picture. Important text stays at 10px or more in a 320px column.

Tile kinds: a single component; the lead UI; a stat; a statement; an object (payment card, chip, keycap) with one light source and a believable material; a diagram (grid, heatmap, nodes and lines) in one stroke weight; a collection (logos, file tiles) running off an edge; a real, licensed photo. A scene drawn in SVG or CSS never stands in for a photograph. For five tiles, a typical mix: the lead screen, a component or two, a figure or a sentence, and a non-UI piece (object, diagram or collection).

## Grounds

- Pick the ground for what it has to do: a quiet tint gives dense UI room to read; a color field or pattern gives a sparse picture character; on dark grounds choose text, borders and raised surfaces together.
- A strong ground does not also need strong controls, colored shadows and a glow.
- Materials (paper, glass, metal, plastic) keep consistent edges, highlights and shadows. Texture supports a material and never sits over text.

## Annotations

Each annotation clarifies a single link, such as the meaning of a data point or the destination of an event. If the layout already makes it obvious, leave it out.

- A leader is a thin line (1px, 1.5px at hero scale) in a muted ink with two clear ends. It starts at the note's edge and stops 4-6px before the object, ending in a small dot; straight or with one bend, never through another surface.
- Direction shows transfer: a request and its reply start from opposite ends, solid for the request and dashed for the acknowledgement.
- Dots travel along a route only while data is actually flowing, on a route that does not move.
- One relationship, one color. Attach lines to measured edges, never to coordinates read off a screenshot.

## Motion (animated demos)

### Story and loop

- The first frame is already a complete screen that would work as a still, with real content visible before anything happens.
- The payoff is readable at the displayed size and arrives with its content, never as an empty panel. It holds for about 2 s; nothing stays frozen for more than about 3 s.
- The poster frame is what most people see (thumbnail, reduced motion, screenshot). Choose the beat that tells the story alone, with the result visible and nothing caught halfway through a change.
- Every reset either has a visible cause (undo, clear, close), exits around an unchanged anchor, or happens while hidden. Values never count backwards in view, and a loop never replays a navigation in reverse.
- What the story added leaves as one reverse stagger, 40-80ms apart and done within half a second, while the product stays put. The next action starts within about a second.
- A second scene must add something new; repeating the beat only doubles the length.

### Pace and easing

- Calm, on two curves: travel `cubic-bezier(0.45, 0, 0.1, 1)`; entrances from nothing `cubic-bezier(0.25, 0.8, 0.25, 1)` over 0.8-1 s. On a phone, quicker and native: `cubic-bezier(0.3, 0.75, 0.1, 1)` over 0.5 s.
- Interface feedback stays as fast as in the real product; only the storytelling slows down.
- Related responses overlap, but a confirmation still comes after its cause. Groups stagger in reading order with the values in `polish.md`.
- Cards and text do not bounce; a small expressive icon may overshoot on its own. Arrivals slow down over their last third.
- A color change between distant hues takes about 200ms.

### Change, arrival and exit

- Everything that changes moves: text rolls, menus slide, surfaces morph. Nothing appears or vanishes between two frames; an exit finishes before the element is removed.
- Animate only what changed, and move what follows by its measured width. Numbers roll digit by digit from the last digit and settle once.
- A button whose label changes does it in place, on the same element.
- A new row pushes the rows below it; neighbors open space continuously as it arrives.
- A surface that resizes moves size, position and content together without stretching its text, and when interrupted it continues from where it is instead of restarting.
- Solid objects (windows, phones, cards) arrive by moving and stay opaque; they never fade through like ghosts. Cards, toasts and pills drop in whole from just above instead of being uncovered by a hard edge.
- An open menu or popover stays anchored to the edge it opened from and is sized before its first frame.
- One object makes one trip and ends in its final place; at the hand-off, size, position and look match exactly.
- Navigating within a window leaves its frame untouched; just the content area dissolves to the next view, about 200ms with a small 8px rise; never slide whole pages sideways.
- A chart line draws from its start, with the area following and the end point landing as the line reaches it.
- Nothing scrolls unless the pointer is over it; scrolling starts on whole rows, and edge fades appear only while content is hidden.
- A spinner is already turning before it fades in and keeps turning as it fades out.

### The pointer

- No pointer means no substitute: never move a focus ring or spotlight from control to control.
- The element under it sets its shape (arrow, hand, I-beam, resize), changing as it crosses the edge rather than after arriving.
- Its tip lands on the control's padding, not on the label being clicked. Between beats it rests on empty surface near the next action.
- Every move leads to the next action, carries something, or gets out of the way. A press shows feedback before the result.
- Keyboard stories show the keys being pressed.
- A drag is one continuous motion starting where the object is, keeping the grab offset. A carried card grows about 3%, casts a deeper shadow and tilts a degree or two with its text, then settles flat when dropped. A text selection stays under the I-beam in every frame.
- On a phone, use a touch indicator instead of the desktop arrow. Swipes are quick flicks covering roughly 33% of the screen width in some 250ms, with the finger leaving while the row still travels.
- Zoom only when the payoff would otherwise be unreadable, once per story, in and back out.

## Review

Judge rendered frames, never the code. Capture the still at its displayed width and at 390; for an animation, step through each press, morph, hand-off, exit and the loop seam at 40-80ms intervals. Fix the biggest visible fault first, in this order: framing, hierarchy and density, motion, polish.

Start with one question: could this composition belong to any product in the category, or does it answer this product and this page? A layout the brief did not shape counts as a finding even if every other check passes. Then set your still next to the reference and name the single biggest difference.

For a second opinion, a fresh reviewer gets the frames, the reference and this file, and nothing about your plan or intentions. Ask for a ranked list in which every finding names its frame and a one-line fix.

| What you see | What to do |
|---|---|
| Empty space under a list or in a pane | Fill it with more product that continues past the edge, or crop tighter; never pull rows apart |
| Single-line rows with far more height than text | 12px padding (8px dense), and more rows |
| Gaps between rows larger than the rows | Tighten the pitch to the row padding; add rows |
| A complete window floating with equal margins in a hero | Push it past two edges, keeping one gutter, or enlarge it to fill the stage |
| Placeholder lines in the focal area | Real words there; lines only beside it and at the crop |
| A real label next to a placeholder value | Both real, or remove the row |
| A figure's unit wrapping to its own line | Keep them together, resize the figure, or move the unit into the lead-in |
| A small or complete phone in a narrow column | Crop it with one gutter, cut by the other side |
| A sheet or handle under the island | Begin it below the status bar |
| A menu that shifts while it is open | Anchor it to its opening edge and reserve its height |
| An emoji used as an icon | A glyph from the chosen family |
| A tinted backdrop under the device on a plain page | Delete it and let the page itself be the background |
| A sparkle, wand or purple standing for AI | Show what the AI produces |
| A letter on a colored square as a logo | The real mark, or the name in plain text |
| A control or shadow clipped by the stage | Bring it fully inside, delete it if it is filler, or change the composition |
| Ten checks in a row with no visible change | Stop and ask for a fresh eye |

Before handing over, note the reference you compared against, the beats and loop length, the widths and looks you rendered, and what you did not check.
