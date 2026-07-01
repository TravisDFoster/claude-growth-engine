---
name: html-to-pdf
description: When the user wants to convert a rendered HTML file to a PDF, when a process is generating a print-format deliverable (one-pager, slide handout, designed report), when the final step of a render pipeline needs to produce a .pdf sibling. Triggers on phrases like "render to PDF," "save as PDF," "convert to PDF," "print this." Built-in verify gate: runs html-overflow-detector first; if the HTML has layout overflow, the PDF is NOT written and the caller is told to apply remediation. Invoked automatically by one-pager-process.md as the final step after md-to-html.
metadata:
  version: 0.1.0
---

# html-to-pdf

> Renders an HTML file to PDF via Chrome headless, with a built-in verify gate that catches layout overflow before the PDF is written.

The verify gate is the point of this skill — it's the difference between "render and discover failure" and "verify, then render." If the HTML doesn't pass the overflow detector, this skill refuses to render, returning a failure that the caller can react to (apply remediation, then re-run).

## Trigger

- "Render this HTML to PDF"
- "Convert <file> to PDF"
- "Generate the PDF"
- Invoked automatically by `cerkl/marketing/design/one-pagers/one-pager-process.md` after `md-to-html` produces the HTML.

## Inputs

- **Source path** (required) — absolute path to the `.html` file to render.
- **Output path** (optional) — absolute path for the `.pdf`. Defaults to a sibling of the source with the same basename (`foo.html` → `foo.pdf`).
- **`--skip-verify`** (optional) — bypass the overflow detector. Use ONLY for HTML that doesn't follow the `.page` div convention (e.g., generic single-flow documents the detector can't reason about).
- **`--single-page`** (optional) — render the whole document as **one content-sized page** instead of paper pages. For digital, zoomable, scrolling deliverables (dashboards/reports), where paper pagination would slice content across page breaks. Measures the rendered content height and prints a single page sized exactly to it — zero internal breaks. Implies `--skip-verify` (there's no `.page` convention to check). Requires Node ≥22 (uses built-in WebSocket/fetch to drive Chrome over the DevTools Protocol — no npm install).

## Two modes

| | Default (paper) | `--single-page` |
|---|---|---|
| Use for | Print-format one-pagers, handouts (the `.page` convention) | Digital, zoomable dashboards/reports read on screen |
| Pagination | US Letter pages | One page sized to content height |
| Verify gate | Runs (unless `--skip-verify`) | Skipped (no `.page` concept) |
| Renderer | Chrome `--print-to-pdf` | `single_page.mjs` (Chrome via DevTools Protocol) |

For scrolling dashboards, `--single-page` is the right call — paper pagination has no notion of where a table row or card *should* break, so rows get sliced. Default paper mode also hardens against this where it can (`tr { break-inside: avoid }` in callers' print CSS keeps rows whole), but single-page sidesteps the problem entirely.

## Output

- A `.pdf` file at the resolved output path.
- `stdout`: status messages including page count and file size.
- `exit code`: `0` = PDF written, `1` = verify gate failed (no PDF), `2` = bad args, `3` = render failed, `4` = empty/missing output, `5` = (`--single-page`) content taller than the 200in single-page cap — use paper mode.

## How to invoke

```
bash /Users/travisfoster/claude-code/cerkl/skills/html-to-pdf/run.sh <html-path> [output-path] [--skip-verify] [--single-page]
```

Pipeline pattern (typical):
```bash
if bash cerkl/skills/html-to-pdf/run.sh "$HTML" "$PDF"; then
  echo "Done. PDF saved."
else
  # Detector flagged overflow — apply remediation (--body-size step, variant
  # swap, or escalate to user), edit HTML, and re-run.
  echo "Verify gate stopped the render. Remediating..."
fi
```

## How it works

1. **Verify gate** — calls `cerkl/skills/html-overflow-detector/run.sh` on the source HTML. If exit code is non-zero, this skill exits with the detector's exit code (1) and the PDF is NOT written. Skipped only with `--skip-verify`.
2. **Render** — `chrome --headless --no-pdf-header-footer --print-to-pdf=<out> file://<src>`.
3. **Sanity check** — confirms the output file is non-empty.
4. **Report** — prints page count and file size for the caller's audit log.

## Page-count contract

The output PDF page count should match the number of `.page` divs in the source HTML. If they don't match, content overflowed in print mode that wasn't visible in screen layout (rare, but it happens with `page-break-inside` interactions). The caller should compare:

```bash
SRC_PAGES=$(grep -c 'class="page"' "$HTML")
PDF_PAGES=$(mdls -name kMDItemNumberOfPages "$PDF" | grep -oE '[0-9]+' | head -1)
if [ "$SRC_PAGES" != "$PDF_PAGES" ]; then
  echo "Page-count mismatch: HTML has $SRC_PAGES .page divs, PDF has $PDF_PAGES pages"
fi
```

This catches the residual class of failures the overflow detector misses.

## Requirements

- macOS (uses `/Applications/Google Chrome.app/Contents/MacOS/Google Chrome`).
- The companion skill `cerkl/skills/html-overflow-detector/` must exist at that path (only needed if `--skip-verify` is NOT used).
- Source HTML uses the `.page` div convention from `reference-one-pager.html` (otherwise pass `--skip-verify`).

## When NOT to use

- HTML that's meant to be read on screen, not printed. Use `md-to-html` alone.
- Quick-and-dirty PDFs from arbitrary single-flow HTML — pass `--skip-verify` or use Chrome directly.

## Future work

- Optional `--theme=dark` pass-through (currently only light is wired into the one-pager reference).
- Post-render: extract text positions from the generated PDF to confirm visible content matches the source (catches `color: white` invisibility, font-substitution disasters).
- A `--max-remediations=N` flag for callers that want this skill to autonomously try Tier-A type-shrink + Tier-B variant-swap before giving up (right now remediation is the caller's job).
