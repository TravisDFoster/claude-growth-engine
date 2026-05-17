---
name: html-overflow-detector
description: When the user wants to verify an HTML page renders without layout problems before generating a PDF, when a rendered PDF has visible overlap or cut-off content, when a render-verify-remediate loop needs a deterministic "does the layout fit?" check. Triggers on phrases like "check for overflow," "verify the layout," "did anything get cut off," "find the overlap." Invoked automatically by one-pager-process.md and any process that renders fixed-format artifacts (letter PDFs, slides, ad creatives) from variable-length content. Returns a JSON report listing overflow type, page, selector, pixel overrun, and a text snippet — plus an exit code (0 = PASS, 1 = FAIL).
metadata:
  version: 0.1.0
---

# html-overflow-detector

> Scans an HTML page and reports where content escapes its containers or overlaps siblings — before a PDF is generated. Output: JSON report + exit code.

The detector exists because Chrome's print engine fails silently. Content past the page boundary clips. Sibling boxes that should stack can overlap. There's no visual indicator at render time. This skill makes those failures visible as data the rendering process can react to.

## Trigger

- "Check this HTML for overflow"
- "Verify the layout before rendering the PDF"
- "Why is the content cut off / overlapping"
- Invoked automatically by `cerkl/marketing/design/one-pagers/one-pager-process.md` as the verify step in its render-verify-remediate loop.
- Invoked by any process that renders a fixed-format artifact (letter-portrait PDF, slide deck) from variable-length copy.

## Inputs

- **Source path** (required) — absolute path to the `.html` file to scan.

## Output

- `stdout`: Status line + JSON report.
- `exit code`: `0` = PASS (no issues), `1` = FAIL (issues found), `2` = bad arguments, `3` = detector failed to run.

### Report shape

```json
{
  "status": "FAIL",
  "count": 2,
  "issues": [
    {
      "page": 2,
      "type": "overflow-page-bottom",
      "selector": "body > div.page > div.page-body.stretch > div.cta-strip",
      "overrun_px": 25,
      "text": "Broadcast Platform Powered by Cerkl Deliverability…"
    },
    {
      "page": 2,
      "type": "sibling-overlap",
      "container": "div.feature-grid.grow",
      "upper": "div.feat",
      "lower": "div.feat",
      "overlap_px": 14,
      "text_upper": "Insights — Cross-channel, channel…",
      "text_lower": "Intelligent Content — Instead of jumping…"
    }
  ]
}
```

## Issue types

| Type | Means | Common cause |
|---|---|---|
| `overflow-page-bottom` | Element's bottom edge is past its `.page` container's bottom | Content too tall for the page; CTA strip / footer pushed off |
| `sibling-overlap` | Two children of a stacking container have overlapping rectangles | `grid-auto-rows: 1fr` allocating less height than content needs; flex `min-height: 0` letting items collapse |
| `content-clipped` | Element with `overflow: hidden` has `scrollHeight > clientHeight` | Cell with fixed `max-height` whose content is too long |

## How to invoke

```
bash /Users/travisfoster/claude-code/cerkl/skills/html-overflow-detector/run.sh <absolute-path-to-html>
```

In a render-verify loop, the caller checks the exit code:

```bash
if /Users/travisfoster/claude-code/cerkl/skills/html-overflow-detector/run.sh "$HTML"; then
  # PASS — proceed to PDF
else
  # FAIL — apply remediation (shrink type, swap variant, escalate)
fi
```

## How it works

1. **Inject** `detector.js` as a `<script>` tag into a temp copy of the source HTML (alongside the source so relative paths resolve).
2. **Render** with `chrome --headless --dump-dom --virtual-time-budget=4000` — runs JS, waits for layout, dumps the post-execution DOM.
3. **Extract** the `<pre id="__overflow_report__">` element the detector inserts into the DOM. Parses its `data-status`, `data-count`, and JSON text content.
4. **Return** the status line, the JSON, and an appropriate exit code.

The detector itself (`detector.js`) walks each `.page` div and applies the three checks above. It deliberately ignores `position: absolute / fixed` children when checking sibling overlap (decorative blobs and overlay cards are meant to layer).

## Requirements

- macOS (uses `/Applications/Google Chrome.app/Contents/MacOS/Google Chrome`).
- Source HTML must use `.page` divs to demarcate page containers (matches the convention in `cerkl/marketing/design/one-pagers/reference-one-pager.html` and the other `cerkl/skills/md-to-html/reference-*.html` files).

## When NOT to use

- One-shot HTML you'll never print — overflow doesn't matter for screen.
- HTML that doesn't follow the `.page` div convention — the detector returns "no pages found" (effectively a no-op).
- Pre-render content-budget checks — those go on the markdown side (word counts vs. component budgets), not the rendered HTML.

## Limitations

- **Detects, doesn't fix.** This is a verify step, not a remediator. The calling process owns remediation (shrink type, swap variant, escalate).
- **Print pagination is approximated by screen layout.** The detector runs in screen rendering, so it catches issues that manifest in screen *and* print. Issues that *only* show up after Chrome's print pagination (rare; usually involves `page-break-inside` interactions) won't be caught — a final PDF-page-count check is still worth running.
- **Threshold is 1.5px.** Sub-pixel overlap (e.g., 0.5px from anti-aliasing) is ignored. Tunable in `detector.js` if false positives appear.

## Future work

- Print-mode validation: run the detector against the rendered PDF too (extract text positions via a PDF parser).
- Per-component overlap budgets: some components legitimately allow 1–2px overlap (e.g., a decorative underline) — let those be allow-listed.
- HTML diff: when the detector flags an issue, show a side-by-side of the offending region as a screenshot.
