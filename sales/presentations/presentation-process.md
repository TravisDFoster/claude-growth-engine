# Presentation build process

> How to assemble a branded sales deck end-to-end: from brief or seed file → branded PPTX → exported deliverable. Encodes learnings from the [Prospect] "Day in the Life" deck (2026-06).

---

## When to use this process

- Restyling a seed/template deck for a specific prospect or use case
- Building a deck from a content brief (no seed file)
- Updating an existing deck to a new brand (Cerkl-branded → prospect-branded, or vice versa)

Skip this for: simple one-off slide edits in PowerPoint/Keynote, Canva-native design work (use the `canva-skills/template-fill/` skill instead).

---

## The pipeline

```
   1. Brief        2. Brand        3. Build         4. Assets        5. Export
─────────────  ─────────────  ─────────────  ─────────────  ─────────────
seed.pptx       Cerkl brand    python-pptx    Product Images  PPTX + PDF
content brief   prospect kit   HTML→PDF       _web/ derivs    QA in Keynote
ROADMAP.md      (build first)  Canva
```

---

## Step 1 — Brief / seed

Two starting points:

| Starting point | What to do |
|---|---|
| **You have a seed PPTX** | Extract text + layout via python-pptx (`Presentation(path).slides[i].shapes`). Capture the per-slide content into a JSON or dict so you can rebuild without parsing XML twice. |
| **You have a written brief** | Write a slide map (1 row per slide: time/section → headline → body → capability/CTA) before any styling. |

Either way: end this step with a **slide-by-slide content map** that's separated from styling. The map is what you rebuild from.

Also write a roadmap doc — see [`[prospect]-day-in-the-life-ROADMAP.md`]([prospect]-day-in-the-life-ROADMAP.md) as the template. North star, status table, slide map with Broadcast feature links, open questions, next actions. Update it as the project moves.

---

## Step 2 — Brand kit

- **Cerkl-branded deck** → load from [`marketing/design/branding-assets/Brand Guidelines/`](../../marketing/design/branding-assets/Brand%20Guidelines/) (colors.md, typography.md, logo-guide.md).
- **Prospect-branded deck** → run [`../prospect-brand-process.md`](../prospect-brand-process.md) first (it lives at `sales/` level because brand kits are reused across decks, outbound, ABM, etc.). Default output for deck work: `sales/presentations/<prospect>-brand-guidelines/`. Reuse on every deck for that prospect.

**Font licensing reality**: most enterprises use commercial typefaces (TWK Everett, Söhne, GT America, etc.). For one-off sales decks, use a free Google Fonts stand-in — Inter is the safest geometric-sans substitute. Document the substitution in the brand kit's typography.md.

---

## Step 3 — Build

Three viable engines, ranked by use case:

| Engine | When | Pros | Cons |
|---|---|---|---|
| **python-pptx** | Editable .pptx output (default) | Recipient can edit; survives PowerPoint/Keynote/Google Slides round-trips; deterministic | Lower visual fidelity than HTML; manual layout math |
| **HTML → PDF** (Chrome headless) | Pixel-perfect, send-only PDF | High fidelity, custom fonts, gradients, animations as static | Not editable by recipient; needs `marketing/skills/html-to-pdf/SKILL.md` |
| **Canva template fill** | High-volume / channel-templated | Brand-locked, fast | Constrained by template; less flexible for custom narrative |

**Default: python-pptx.** Recipients almost always need to edit or screenshot slides. Switch to HTML→PDF when visual fidelity matters more than editability (final send-ready PDF, leave-behind).

Layout conventions for python-pptx decks:
- Widescreen 13.33"×7.5" (matches PowerPoint default)
- Use `Blank` slide layout (`slide_layouts[6]`) — build every shape manually for predictability
- Set `tf.margin_left = tf.margin_right = Emu(0)` on textboxes — avoids unexpected padding
- Set `shp.line.fill.background()` on filled rectangles — removes default outline
- Use `MSO_SHAPE.ROUNDED_RECTANGLE` with `adjustments[0] = 0.5` for pill-shaped chips
- Footer band is the easiest "remembered brand" element — always include one

---

## Step 4 — Assets

### Product images (UI screenshots)

Route: `design/CLAUDE.md` → "Pick a specific Broadcast product image" → [`Product Images/INDEX.md`](../../marketing/design/branding-assets/Product%20Illustration/Product%20Images/INDEX.md) → feature subfolder INDEX → file.

**Always use the `_web/` derivative**, not the source. Sources are 5000×3334 (~5–10 MB each); `_web/` derivatives are 2000×1334 (~200–700 KB). Embedding sources in a deck balloons it from ~5 MB to ~50 MB.

```python
# In the build script:
src = Path("…/insights - custom dashboards.png")
web = src.parent / "_web" / src.name              # PNG with alpha
# or:                                              # JPG for photos
web = src.parent / "_web" / (src.stem + ".jpg")
slide.shapes.add_picture(str(web), Inches(x), Inches(y), width=Inches(w))
```

If `_web/` doesn't exist yet for a folder you need, run `python3 marketing/design/tools/compress-images.py --folder "<folder>"` once. Idempotent.

### Photos / lifestyle imagery

Route: [`Cerkl Photography/INDEX.md`](../../marketing/design/branding-assets/Cerkl%20Photography/INDEX.md) → subfolder → pick hero candidate.

### Logos

- Cerkl wordmark + symbol: [`Cerkl/`](../../marketing/design/branding-assets/Cerkl/) per [`logo-guide.md`](../../marketing/design/branding-assets/Brand%20Guidelines/logo-guide.md)
- Broadcast lockups: [`Broadcast/`](../../marketing/design/branding-assets/Broadcast/)
- Prospect logos: `<prospect>-brand-guidelines/logos/` from `prospect-brand-process.md`

**python-pptx accepts PNG/JPG only**, not SVG. If you only have an SVG, convert to PNG at 2x the embed size (e.g., embedding at 800px → render at 1600px PNG).

### Image embedding survives export

PNG and JPG embed as binary parts inside the .pptx zip. They travel with the file: PowerPoint, Keynote, Google Slides, PDF export all preserve them. No path-reference fragility. Confirmed in the [Prospect]-styled deck — see [`[prospect]-day-in-the-life-ROADMAP.md`]([prospect]-day-in-the-life-ROADMAP.md).

---

## Step 5 — Export and QA

1. **Save the editable .pptx** as `<Deck_Name>_<variant>.pptx`. Variant tag captures the styling pass: `seed`, `cerkl-styled`, `[prospect]-styled`, `final`.
2. **Open in Keynote** (Mac default — double-click). This is the most honest preview because Keynote renders fonts and shadows differently than PowerPoint. If Keynote looks fine, PowerPoint will look fine.
3. **Common rendering gotchas**:
   - **Font missing → falls back to system default.** If you used Inter/Roboto and the recipient doesn't have them installed, they'll see Helvetica. Embed fonts in the .pptx if licensing allows, or flatten headlines to outlines (right-click → Convert to Shape in PowerPoint).
   - **Image alignment drifts** between python-pptx coordinates and what's rendered. Always do a visual pass; numerical fidelity ≠ visual fidelity.
   - **Text overflow** isn't enforced by python-pptx. If body text is long, it'll spill past the textbox bounds silently. Spot-check long slides.
4. **PDF export** for send-ready: File → Export → PDF in PowerPoint/Keynote. Keep the .pptx as the working file.

---

## Tools available

| Tool | Use |
|---|---|
| python-pptx | Programmatic .pptx build/edit |
| [`design/tools/compress-images.py`](../../marketing/design/tools/compress-images.py) | Generate 2000px `_web/` derivatives for branding-assets |
| [`design/tools/build-image-index.py`](../../marketing/design/tools/build-image-index.py) | Generate INDEX.md skeletons for new asset folders |
| [`html-to-pdf` skill](../../marketing/skills/html-to-pdf/SKILL.md) | HTML → PDF via Chrome headless (for pixel-perfect non-editable decks) |
| [`html-overflow-detector` skill](../../skills/html-overflow-detector/SKILL.md) | Verify HTML layout before PDF export |
| [`md-to-drive` skill](../../skills/md-to-drive/SKILL.md) | Upload working docs (briefs, roadmaps) to Google Drive |

---

## Conventions

- **One ROADMAP.md per deck project.** Living overview, updated as the deck evolves. Use [`[prospect]-day-in-the-life-ROADMAP.md`]([prospect]-day-in-the-life-ROADMAP.md) as the template.
- **Variant naming.** `<Deck_Name>_seed.pptx` → `<Deck_Name>_<brand>-styled.pptx` → `<Deck_Name>_final.pptx`. Keep all variants in the folder; don't delete prior versions.
- **Brand kits live with the deck, not with marketing/design/.** A prospect's brand isn't a Cerkl brand asset. Keep `<prospect>-brand-guidelines/` here in `sales/presentations/`.

---

## Anti-patterns

- **Don't embed source-resolution images.** Always use `_web/` derivatives. A 50 MB deck looks unprofessional and bounces email attachments.
- **Don't write content into python-pptx code directly.** Separate content (JSON/dict) from build (Python). Iterating on copy via code-editing is painful.
- **Don't skip the brand-kit step for prospect-styled decks.** Eyeballing colors from screenshots leads to off-brand decks that the prospect will notice. Run [`../prospect-brand-process.md`](../prospect-brand-process.md).
- **Don't auto-translate "make it pretty" into "add features."** A clean 10-slide narrative beats a 25-slide feature tour. Defer to the content map from Step 1.
