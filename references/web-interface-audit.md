# Web interface audit

Use for a web UI audit or for the components and routes affected by a redesign. Read the [local Vercel Web Interface Guidelines](upstream/web-interface-guidelines/command.md) and apply the rules relevant to the target. Keep the project's browser support policy and user-approved behavior. Follow [Modern Web Guidance](web-guidance.md) when an implementation recommendation depends on browser compatibility.

- Review source for semantic controls, keyboard access, focus, forms, navigation and recoverable states. In the browser, check the behavior those rules describe. A native control can supply keyboard behavior without custom handlers. Choose autocomplete values from the field's purpose.
- Check touch alternatives, safe areas, long and translated text, empty values, reduced motion and themes where the project supports them. Inspect actual layout before adding clipping or truncation.
- Report each confirmed issue as `file:line` or a reproducible route and state, along with impact and a scoped fix. Identify which checks were source-only. Audit mode leaves the code intact.

The local snapshot follows [Vercel's skill](https://github.com/vercel-labs/agent-skills/tree/5a37a6329fbad3666c3207392a6a7c0110e92efb/skills/web-design-guidelines) and preserves the [source license](upstream/web-interface-guidelines/LICENSE).
