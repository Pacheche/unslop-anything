# Modern Web Guidance

Use this when auditing or changing a web platform pattern in the requested scope. Examples include layout, motion, accessibility, forms, browser APIs, performance, privacy, and security. For copy-only or color-only work, continue the relevant Unslop Anything pass.

## Targeted search and implementation

Before editing, search a single capability using two to five action-oriented English words. Translate the intent into the web primitive and omit framework and project names. Search separately for separate capabilities.

```sh
npx -y modern-web-guidance@1.0.1 search "light dismiss dialog" --skill-version 2026_11_10-47b4c80e
npx -y modern-web-guidance@1.0.1 retrieve "light-dismiss-a-dialog,dialog"
```

Use `npx.cmd` on Windows or `pnpx` without `-y` when available. Read the returned guide in full, including any output written to a temporary file. Retry weak results once with the concrete component name, then use `list` to locate a relevant guide. The [original guide](upstream/modern-web-guidance/guide.md) documents the complete search, retrieval, framework and verification workflow.

When the CLI is unavailable, search the [local catalog](upstream/modern-web-guidance/guides/) by filename and content. Read the relevant implementation guide and any discipline overview it references. The local catalog includes the full upstream snapshot, from CSS, HTML and accessibility to JavaScript, security, PWA, built-in AI, WebMCP and WebAssembly.

Check the project's browser support policy. Treat Baseline Widely available as the default when no policy exists and apply the guide's fallback for features outside the target. Verify current compatibility when it affects the choice. Adapt the examples to the existing framework, SSR and component lifecycle. Test the changed behavior, including keyboard and focus where relevant, reduced motion where applicable, and the fallback when one is required. In the report, name each applied guide ID and the implementation decision or fallback it informed. If you searched and applied none, say why.

## Explicit broad modernization

For a broad legacy scan or modernization request, run `npx -y modern-web-guidance@1.0.1 legacy-scan <path> --json`. Check each match against its `keepWhen` and `dropWhen` rubric and the actual runtime and support needs. Report verified findings. If editing was requested, retrieve the corresponding guides, apply replacements and rescan. Keep legitimate fallbacks even if the scanner still flags them. The scan covers a subset of the guide catalog. Use targeted search for a specific component or feature.

## Chrome extensions

For an extension surface, read the relevant parts of the [Chrome extensions guide](upstream/modern-web-guidance/chrome-extensions/guide.md), including its linked Manifest V3 API references and output checklist. Use its store listing, privacy, permissions and release preparation guidance when the request affects the extension's store presence. Publishing requires user authorization.
