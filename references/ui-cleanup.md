# Subtractive UI and chart cleanup

Use this pass for interface copy, decorative chrome, charts, and dashboards. Keep the target to the files or components the user named. If none are named, use the relevant files changed in the conversation. Ask for a target when neither identifies a surface.

Read the existing brand or `DESIGN.md` rules if present. When the project already has `.unslop-ui/taste.md`, apply its **Bans** and **Keep** lists as UI-specific settings within those rules and the user's scope. Preserve named exceptions and report why. The counter's three supported bans are exclamation marks, uppercase text and middle dots between items. Other bans and Keep exceptions require review. Run from the project root or pass `--taste <file>`. Use the [example format](upstream/unslop-ui/references/taste-example.md) when asked to persist UI-specific choices. Keep project-wide decisions in the canonical brand or design file.

Read the [U1–U20 rules and review checklist](upstream/unslop-ui/guide.md). The original invocation instructions are for the upstream package. Within Unslop Anything, use our writing pass for full sentences and the [bundled numbered writing rules](upstream/unslop-ui/references/unslop-fallback.md) for the UI-specific exceptions. Labels, tabs, table headers and KPI captions can be fragments. A dash that stands for an empty value or marks a range can stay. The optional [upstream loader](upstream/unslop-ui/scripts/load_unslop.py) can read a separately installed pstack ruleset when the user wants to apply that version.

1. Count candidates before editing with the bundled counter:

   ```sh
   python3 <skill-dir>/references/upstream/unslop-ui/scripts/count_tells.py <target>
   python3 <skill-dir>/references/upstream/unslop-ui/scripts/count_tells.py --surface <target>
   ```

   Use `py` on Windows. If Python is unavailable, use the [equivalent candidate searches](upstream/unslop-ui/references/finding-tells.md) and count consistently by element. Read every visible string and check real state and source bindings. The counter misses context and several U rules. Use the supplied [examples](upstream/unslop-ui/references/examples.md) and [before/after fixtures](upstream/unslop-ui/examples/) to calibrate.
2. Give a verdict from the evidence. A few confirmed issues get narrow edits. Repeated issues get a full pass within the requested scope. Leave clean work alone. In detect mode, report the evidence without editing.
3. Cut before rewriting. Apply U1–U8 to copy, U9–U11 to decoration and U12–U16 to charts. Keep real sequence, factual distinctions, action guidance, labeled controls, accessible names and text tied to real state. Preserve data, the chart type, series colors and interactions. Keep instructions essential to operation and legends needed to distinguish series. Flag unverified claims for the owner during a scoped copy pass. Edit translated or data-backed copy at its source. Remove wrappers, spacing and imports used only by deleted decoration.
4. Apply U17–U20 only when the request includes surface polish or broader visual work. For narrow polish use project tokens and keep the established palette, typography, radii and layout. The upstream [token values](upstream/unslop-ui/references/tokens.md) are starting points. Keep meaningful motion, emphasis and gradients.
5. Run the same counter again, inspect the diff and render when available. Check form labels, icon-button names, live state, chart labels, empty wrappers and preserved layout. Report counts by rule before and after, valid candidates kept and why, each rewritten string with its rule, and remaining tasks with locations. Count manual findings for rules outside the counter. An upstream counter hit is a candidate and does not increase the overall slop score until confirmed.
