---
name: unslop-anything
description: Use when something looks or reads AI-generated and the user wants it fixed or audited. Covers web pages, landing pages, dashboards, mobile app screens, visual design (posters, social graphics, slides, icons, generated images) and writing (posts, docs, emails, UI copy). Triggers on "unslop", "deslop", "looks vibecoded", "looks like AI", "make it less generic", "is this AI slop", purple gradients, glows, emoji icons, gradient text, uneven spacing, hype copy, em dashes, "not X, it's Y" sentences.
metadata:
  version: "0.2.1"
---

# Unslop Anything

AI slop is whatever nobody decided. The model reached for the most common answer, so the result looks like a thousand other results: the violet gradient, the emoji in every label, the greeting headline, the "not just X, it's Y" sentence. Even good patterns turn into slop once everyone ships them by default.

So unslopping has two halves, and you need both:

1. **Remove the defaults.** Find every named sign, fix it with a concrete value or a concrete sentence.
2. **Add a decision.** A clean result that could belong to any product is the next template. The finished work must carry at least one thing that only this product, brand or writer would have.

You do the work yourself: read the files, edit them, render, compare. Ask the user only for what the material cannot tell you.

## How to use this skill

Paths are relative to this skill's folder. Load references on demand, never all at once.

1. **Route.** Decide what you are unslopping and open only its references.

| Medium | Read |
|---|---|
| Web app, dashboard, landing page, any HTML/CSS/React/Vue/Svelte UI | `references/ui-signs.md`, `references/ui-passes.md`, `references/direction.md` |
| Mobile app screen (iOS, Android, React Native, Flutter, SwiftUI) | the UI files above plus `references/mobile.md` |
| Image, illustration, icon set, poster, social graphic, slide, logo | `references/visual-design.md`, `references/direction.md` |
| Writing: post, thread, article, email, docs, README, UI copy | `references/writing.md` |
| A UI whose copy is also slop | do the UI first, then the copy pass with `references/writing.md` |

Then name the surface's mode, because it sets how much expression fits:
   - **Persuade** (landing, marketing, pricing): the visitor decides. Full commitment to a direction, real imagery, a strong headline.
   - **Operate** (app, dashboard, editor, settings): the visitor finishes a task. Scanability, consistency and platform conventions beat expression; the brand lives in precise details.
   - **Read** (docs, articles, help, changelog): the visitor understands. Measure, hierarchy and rhythm first.
   - **Experience** (portfolio, gallery, showcase): the work leads from the first screen; the interface recedes.
   Pick it from the surface, not the company: a dev tool's landing page is Persuade, its docs are Read.

   When the user asks for a specific overlay or component and the name is vague ("make a popup"), check `references/component-vocabulary.md` before building.

2. **Pick the job.**
   - **Detect.** The user asks "is this slop?", wants an audit, or says not to change anything. Load only the signs file for the medium (`ui-signs.md`, `visual-design.md` or `writing.md`). Do not edit. Answer in this shape:
     ```text
     Slop level: N% (heavy | light | none)
     <Category>
     - <sign>: <where: file:line, screen region or "quoted sentence"> -> <fix in a few words>
     Claims to confirm: <unverifiable claims, or none>
     Not checked: <what you could not see, or none>
     Want me to fix it?
     ```
   - **Fix (default).** Run the workflow below.

3. **Get the material in front of you.**
   - Code: find the files that render the screen. If you can run it, render it and take a screenshot. Judge what people see, not only the code.
   - A URL with no code: open it in a browser tool, screenshot it, and save the HTML as a local copy to work on. The output is a redesigned file the user can hand to whoever owns the site. Say so.
   - Only a screenshot: rebuild it as one static HTML file that matches closely, treat that as the original, and say so.
   - No browser or render tool, or the app will not start: extract the screen into a static HTML file and render that if you can; otherwise work from the code and list every visual check under `Not checked:`.
   - Writing: ask for the draft if it is not pasted. If the audience is unclear, ask one question: who reads this and where.

## Workflow

1. **Scan.** For code or text files, run the scanner. It finds candidates, not verdicts:
   ```bash
   python3 <skill folder>/scripts/slop_scan.py <files or folders>
   python3 <skill folder>/scripts/slop_scan.py --text draft.md      # writing rules on any file
   ```
   On Windows use `py` instead of `python3`. It needs only Python 3. Exit 0 means no candidates, 1 candidates, 2 nothing scanned.
   Scan only the target: the screen's files and the shared components and styles it uses, not the whole repo, unless the user asked for a repo-wide audit. For a repo-wide audit, use `--json` and group hits by rule before reading them. Confirm each hit by reading it. Drop false positives and say why in the report.
2. **Audit.** Walk the signs file for the medium. One line per sign: what, where (`file:line`, screen region or quoted sentence), fix. Add signs the scanner cannot see: hierarchy, rhythm, composition, meaning.
3. **Rate it.** Count the categories of the signs file (not the scanner's categories) that have at least one sign. File each sign under one category only, the first one that lists it. That count times 10 is the slop level. In UI, the last category counts for builder fingerprints always, and for template-look signs only when the other nine are empty. Then pick the mode:
   - **Heavy** (50% or more): full process, direction first.
   - **Light** (10-40%): polish mode. Fix only what the audit found. Keep the palette, type, layout, voice and brand. Bigger ideas go in the report as suggestions.
   - **None** (0%): say so plainly. Offer two or three refinements with exact values and apply them only if the user agrees. Never change good work just to make it different.
4. **Direction (heavy UI and visual design only).** Follow `references/direction.md`: product sentence, character, world, moments, signature, and for new looks three candidate directions before committing to one. Show the audit and the direction, then stop and wait for the user's answer, because changing direction later means redoing everything. Skip the wait only when the user already said "just do it"; then still put the three candidates (one line each) and why you chose one in the report.
5. **Fix in passes.** UI: the pass order in `references/ui-passes.md`. Visual design: the order in `references/visual-design.md`. Writing: the workflow in `references/writing.md`. Finish one pass across the whole piece before starting the next.
6. **Verify.** Render again (at most three renders per run) and look at the render at full size, region by region: colliding columns, clipped or overlapping text and misaligned edges only show there. Check against the audit list and the checklist of the reference you used. Run the scanner again. Anything still on the list gets fixed or explicitly justified. Then put the original and the result side by side at the same size and ask which one a visitor would rather use; if it is the original, go back to the direction. The target in fix mode is a slop level of 10% or less, with no builder fingerprints left; if you stop above that, say what blocks it (usually a decision or an asset only the user has).
   For a public site, an independent scorer gives a second opinion before and after: the free Slop Score at antiwebslop.com checks design, copy and builder fingerprints on the rendered page. Lighthouse measures speed and accessibility, not whether a page looks generic.
7. **Report.** Slop level before and after, the direction, a few lines per pass about what changed, false positives you dropped, anything you could not check (`Not checked:`), and claims you need the user to confirm.

## Rules that do not bend

- **Keep the product, change the craft.** Features, content, data, section order and the product name stay. Do not add sections.
- **Mock data only replaces placeholders.** When the original shows placeholder values (`$123,456`, `Lorem`, `John Doe`, a fake chart), you may replace them with plausible mock values. List every mock value in the report under `Mock data to replace`. Real data is never changed.
- **Never invent.** No new features, stats, testimonials, sources, logos or quotes. Claims like "Trusted by 10,000+ teams" or "10x faster" get confirmed by the user or removed. List them in the report.
- **Removed decoration is not replaced with new decoration.** Swapping purple gradients for glassmorphism, grain, neon, bento grids or 3D glass icons is the same slop in a new trend.
- **Better, not just quieter.** Before the first pass, write down what the original does well: its energy, a color people remember, a product you can see, a density that fits. Keep those. Unslopping replaces defaults with decisions and keeps the personality. If someone shown both versions would pick the original, the result has failed, however few signs it has left.
- **Quiet is not faint.** Stripping all color until nothing reads is a failure too. Color stays where it carries meaning: the primary action, a selection, a status, a data series, the one moment.
- **Color and labels tell the truth.** A label matches its number ("64% recovery" is not "Excellent" unless the scale says so). Red means a problem. Green means good.
- **Work through the design system.** If the project has theme tokens or CSS variables, change their values or how they are used; never bypass them with hard-coded values.
- **Keep the writer's voice and the real brand.** A real logo, color or typeface stays. A violet-to-blue gradient, sparkle tile or glow in a logo is not brand unless the user says it is. Writing keeps the writer's vocabulary, bluntness and humor.
- **The brief wins.** A palette, font, era or material the user pinned stays, even when it matches a sign in this skill. Point out the risk once; do not redirect a clear brief toward your taste.
- **Keep the bans, drop the recipes.** Values in this skill's references are starting points to derive from. A fixed font, radius or shadow applied to every project becomes the next fingerprint. Every value you ship has a reason tied to this product.
- **Copying a famous app is not unslopping.** Study 3-5 references for structure and numbers, never paste one product's look onto another.
- **No detector guesses.** In detect mode you name patterns with evidence. You never claim something "was written by AI".

| Excuse | Reality |
|---|---|
| "It looks clean now" | Clean is the template. Run the template test: swap in a competitor's name. If it still fits, push the direction. |
| "The user just wants it prettier" | Prettier and different are not the same. Ten pretty AI apps side by side are one app. |
| "Fewer signs means better" | A page with zero signs that people like less than the original is a failed fix. Compare both side by side. |
| "Removing color fixes it" | Removing color without a ramp, an accent and meaning gives a grey template. |
| "The scanner found nothing" | Zero hits means zero greppable signs. Hierarchy, rhythm and meaning still need your eyes. |
| "I'll skip the render, the code is right" | Slop lives in what people see. Clipped text, uneven gaps and weak hierarchy only show when rendered. |

## Template test (run last, every time)

Replace the product name, or the writer's name, with a competitor's. If the screen, image or text still fits without edits, it is not done. Push the direction harder in the copy, the visual moment and the signature detail.
