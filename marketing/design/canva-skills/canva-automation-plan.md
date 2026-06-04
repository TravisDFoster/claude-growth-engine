# Canva Full-Automation — Implementation Plan

> **Goal:** programmatically generate on-brand Canva assets (webinar graphics, LinkedIn cards, blog covers) from existing brand templates by replacing text and swapping images **by existing asset ID**, then exporting — with **no autofill dependency** and **no re-uploaded / duplicated assets**.

## Decision: Path B — create + programmatic edit

We use the design-editing tools, not autofill. Rationale: the 2026-05-29 spike proved Path B works end to end today, on the existing template library, with no Canva-side configuration. Autofill is the cleaner API but requires Canva Enterprise *and* per-template data-field setup, and **0 of 97 templates currently expose an autofill dataset**. Keep autofill as a future simplification only if we confirm Enterprise and decide to invest in field setup (see [`make-template-autofill-ready.md`](make-template-autofill-ready.md)).

## Execution approach

Use **sub-agents + Python/Node scripts** for the heavy lifting — saves tokens and runs in parallel. Reserve interactive MCP calls for discovery and one-off spikes.

- **Cataloging / re-cataloging** (templates + assets): sub-agent walks the MCP and writes the index files (already done this way).
- **Bulk asset rename + retag** (sheet → Canva): a script hitting the Connect REST API `PATCH /v1/assets/{id}` (`name`, `tags`). The MCP has **no** rename tool — this is REST-only.
- **Element mapping + batch generation**: scripts call the Connect endpoints directly (create-from-template → editing transaction → export), so the running process never loads the full MCP toolset.

## What the spike proved (2026-05-29)

Full loop confirmed on template `EAGqLMN8_Po` (webinar speaker card):
`create-design-from-brand-template` → `start-editing-transaction` → `perform-editing-operations` → `commit-editing-transaction` → `export-design` (PNG).

- `replace_text` / `update_title` — reliable; rendered exactly in the exported PNG.
- `update_fill` with an **existing Uploads asset_id** (`Rachel-folz.jpg` = `MAFZdaEt2Wc`) — accepted, no upload step. ✓ satisfies the no-duplicate rule.
- Export to 1080×1080 PNG — works; download URL returned.
- Test artifact left in Canva: design `DAHLDiECHrE`, titled "[TEST] Path B spike — safe to delete" (no API delete tool — delete manually).

## Gaps the spike surfaced (these drive the build)

1. **Element IDs are per-design.** Each created design gets fresh element IDs, so they can't be hardcoded — slots must be resolved at runtime (match by placeholder text and/or position).
2. **Image frames are grouped/layered.** Swapping the obvious image fill put the headshot *behind* a decorative placeholder card. The automation must target the *correct visible* slot, which differs per template.
3. **Visual verification is mandatory.** API `status: success` did **not** guarantee a correct render. Every asset needs an export + visual check before it's "done."
4. **Headshot crop/fit** inside frames needs a finishing check (aspect mismatch between source photo and frame).
5. **Multi-page templates.** The speaker card has 3 layouts (2/3/4 speakers); the skill must pick/export the right page for the speaker count.
6. **Commit is a guarded write.** `commit-editing-transaction` expects approval. Automation needs an explicit checkpoint or pre-authorization.
7. **Asset library is messy.** 91 of 162 images are screenshot clutter; duplicates exist (two `Rachel-folz`, two `Maddy-rieman`). Must be curated before the picker can choose confidently.

## Confirmed across the catalog (2026-06-01 element-map crawl)

96 templates inspected via 2 parallel sub-agents (output: [`template-element-map.md`](template-element-map.md)). The spike's "layered frame" gap broadens into a clearer set of build constraints:

1. **Layered headshot frames are the norm in personality templates.** Confirmed across webinar speaker cards (EAGqLMN8_Po), employee-spotlight LinkedIn PDFs (EAGqLAfjcls, EAGqLOWcIHY), and multi-photo product carousels. Image swap targets the **background** fill, not the foreground decorative card.
2. **SHAPE-only headshot circles exist too.** Some templates (16:9 promotional + Webinar Recap covers) expose the headshot only as a SHAPE with no image fill — automation must **insert** a fill, not swap.
3. **`editable=false` pinned slots block swaps.** Non-editable headshot frames in EAGqLEqOaM4, EAGqLOWcIHY, EAGqLLf6OBk; non-editable lower-third icons in the video-thumbnail family (EAGqLKCh5Is, EAGqLCGg9JI). The skill needs a fallback (warn + skip, or manual finish).
4. **"DELETE place image or graphic here" text placeholders** in the Twitter post family mark intended image spots that aren't real image slots. The skill must recognize and either delete-text + insert-fill, or flag for manual.
5. **3 explicit duplicate template-pair groups** in the FB/LinkedIn 1.91:1 share-card family (e.g., EAGqLPtHbaY ↔ EAGqLBhKYtg). Pick a canonical per pair in the curation pass.
6. **Multi-page templates need explicit page-selection in the manifest.** LinkedIn Carousel_Problem Solution_1 (8 pages, 30+ slots) and Blog image_in text_illustrated (14 pages, 40+ fills) are the heaviest; the speaker card's 3-page 2/3/4-speaker variants are the canonical "pick a page by data shape" pattern.

## Phases

### Phase 1 — Curation spreadsheet (Google Sheet in Claude-Uploads) — NEXT

Create a Google Sheet via the gws Sheets capability in the **Claude-Uploads** Drive folder (same destination the `md-to-drive` skill uses). Seed it from [`canva-template-index.md`](canva-template-index.md) and [`canva-asset-index.md`](canva-asset-index.md). Furqan/Travis tag, recategorize, approve, and dedupe in the sheet; we then re-import the approved rows to drive the automation (or hand Furqan a Canva to-do list). **Re-import is literal:** a script reads canonical Name + Tags from the Assets tab and `PATCH`es each asset live in Canva via the Connect API — curating in the sheet sets asset metadata in Canva itself. (MCP can't rename; REST-only.)

**Tab 1 — Templates**

| Column | Purpose |
|---|---|
| Template Name | from index |
| Template ID | the `EA…` brand-template ID (the automation key) |
| Canva Link | `create_url` (open in browser) |
| Aspect / Dimensions | e.g. 1:1 1080×1080 |
| Shape Category | square / portrait / landscape / blog / video |
| Use Case | dropdown: webinar-speaker, webinar-countdown, linkedin-stat, linkedin-carousel, blog-cover, … |
| Pages | page count |
| Autofill-ready | No (today) |
| Element-map status | not-started / mapped / verified (Phase 2) |
| Approved for automation | Y/N |
| Priority | 1–3 |
| Notes | layering quirks, etc. |

**Tab 2 — Assets**

| Column | Purpose |
|---|---|
| Asset Name | from index |
| Asset ID | the `M…` id (the automation key — assets have **no shareable link**, only an ID) |
| Category | People / Stock / Event / Logo / Screenshot |
| Subject / Person | e.g. Rachel Folz |
| Tags | comma list: headshot, office, background, working, … |
| Aspect | from index |
| Canonical? | Y/N — pick ONE id per duplicated asset |
| Approved for use | Y/N |
| Notes | |

Note: Canva **assets** (uploads) are referenced by ID, not by a public link — only **templates** have a browser link. The sheet reflects that.

### Phase 2 — Per-template element map

For each approved/priority template: `create-design-from-brand-template` → `start-editing-transaction` → record each fillable slot's role (title, date, speaker_name, headshot, …) keyed by its **placeholder text and position**, and flag layered/grouped image slots (per Gap 2). Save as `template-element-map.md` (one block per template) or a third sheet tab. **Verify each by exporting** a filled sample. This is the real engineering work the spike exposed; it cannot be skipped.

### Phase 3 — Manifest + skill

- **Manifest** (per channel): asset name, template ID, page number, text field values, image asset IDs (canonical, from the curated sheet).
- **Build** the `template-fill` skill (per [`../../../skills/build-process`](/Users/travisfoster/claude-code/cerkl/skills/build-process/SKILL.md)) executing the proven loop, with: runtime slot resolution (Phase 2 map), a mandatory **render-verify gate**, and a **commit checkpoint**.

### Phase 4 — Channel wiring + dry-run

Webinar first — dry-run on Rachel Folz solo, 2026-06-25 (headshot `MAFZdaEt2Wc` already in Canva). Then LinkedIn (stat cards, link cards), reusing the same skill with a different manifest.

## Open items / decisions

- **Confirm Canva Enterprise** — not a blocker for Path B, but would unlock autofill as a simpler path for high-volume templates.
- **Grant `search-folders` scope** — closes the small asset-coverage gap (shared-with-you folders outside root).
- **Delete the test design** `DAHLDiECHrE` ("[TEST] …safe to delete") manually.

---

*Generated 2026-05-29. Companion files: [`canva-template-index.md`](canva-template-index.md), [`canva-asset-index.md`](canva-asset-index.md), [`make-template-autofill-ready.md`](make-template-autofill-ready.md).*
