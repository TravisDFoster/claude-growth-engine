---
name: template-fill
description: "Generate one on-brand Canva asset from a Cerkl brand template by replacing text, inserting/swapping image fills by existing asset ID, and optionally deleting unused slots (e.g. drop speaker 2 on a solo speaker card) — the proven Path B loop (create-design-from-brand-template → start-editing-transaction → perform-editing-operations → commit-editing-transaction). Trigger phrases: 'render this Canva manifest', 'build the speaker card', 'generate the LinkedIn stat card from template X', 'fill this template with these values', 'run the template-fill skill'. Atomic and channel-agnostic — webinar / LinkedIn / blog / video processes all invoke it (typically dispatching one sub-agent per template for parallel rendering). Input: a manifest (template_id + page_index + text values + image asset IDs + optional delete-slots + commit mode). Output: {design_id, edit_url, view_url, warnings[], manual_drag_required[]} — the Canva URL is the deliverable handed to whoever finishes the asset (today: Furqan). Skill is fully driven from per-template JSONs in _element-maps/ (enriched 2026-06-02 with element_id, parent_element_id, container_type, position, dimension, page_id, occurrence) — no runtime element discovery needed. For templates with layered placeholder frames, images are inserted near the slot and the recipient drags them into the frame in Canva's UI (one drag per image; Canva auto-creates the SHAPE-container fill). No PNG export — the design lives in Canva."
metadata:
  version: 1.6.0
  status: live
  renamed_from: canva-asset-pack
---

# Template Fill (Canva)

Atomic, channel-agnostic skill that renders **one** Canva design from a Cerkl brand template using the Path B loop (create + programmatic edit, no autofill). Channel-level processes (webinar, LinkedIn, blog, video) call it once per asset shape with a manifest.

**Deliverable is the Canva design URL**, not a downloaded PNG. The URL is what gets handed to whoever finishes the asset (today: Furqan publishes from Canva directly). The skill stops at `commit-editing-transaction`; it does **not** export.

The Path B loop was proven end-to-end on 2026-05-29 (initial spike) and again on 2026-06-02 (this skill's acceptance check, design `DAHLa2AT45Q`) against the speaker card `EAGqLMN8_Po` with headshot asset `MAFZdaEt2Wc`.

---

## When to use this skill

Use when the caller has:
1. A specific brand-template ID (must be one of the 96 in [`../canva-template-index.md`](../canva-template-index.md)).
2. A specific page index (1-based — most webinar/LinkedIn templates are multi-page).
3. Text replacements keyed by the placeholder text that currently appears in that page.
4. Image swaps keyed by slot role (e.g. `headshot`, `full-bg`) → existing Canva asset ID(s) from [`../canva-asset-index.md`](../canva-asset-index.md). **Never upload new assets.**
5. A downstream owner who will pick up the design in Canva from the returned URL (today: Furqan).

If any of those is missing, the orchestrator should resolve them first — don't invoke this skill speculatively.

---

## Inputs — the manifest

The skill accepts a manifest passed in-message or written to a temp file. Shape (YAML for readability — JSON also accepted):

```yaml
template_id: EAGqLMN8_Po          # required — brand-template ID (EA…)
page_index: 1                     # required — 1-based; must be ≤ template page_count
design_title: rachel-folz-speaker-card-2up   # required — used as the Canva design title (prefixed with [AUTO] + date)
text_values:
  # Keys are the placeholder text currently in the template (the slot's "role" for text).
  # Values are either a string (replaces ALL occurrences of that placeholder) OR a list (positional — replaces the first N occurrences).
  "Webinar title": "Reset the Comms Strategy: Three Moves That Move the Numbers"
  "|   Mar 6, 2025 1:00 pm est": "|   Jun 25, 2026 1:00 pm EST"
  "Name": ["Rachel Folz"]
  "Title": ["Senior Director of Communications, ICP"]
image_assets:
  # Keys are the slot ROLE from the element map. Values are asset ID strings OR ordered lists.
  # The skill matches against the element map's `current_asset_id` first, then role+dimensions.
  headshot: ["MAFZdaEt2Wc"]                # 1 entry for a solo speaker; 2/3/4 entries for grid pages
  # full-bg: "MAGg-altBg"                  # optional override; omit to keep template default
delete_slots:                              # optional — trim unused template elements (Step 6b)
  - {role: headshot, occurrence: 2}        # delete speaker 2 frame group + decorative SHAPE in one op
  - {element_id: "PBCV6H4c0hBh21lc-LBzjddjR0DYNwzNR"}   # delete speaker 2 "Name" text
  - {element_id: "PBCV6H4c0hBh21lc-LBwpcbfPcXVQW3df"}   # delete speaker 2 "Title" text
commit_mode: checkpoint                    # checkpoint (default) | auto
```

**Conventions enforced by the skill:**

- `page_index` is **1-based** in the manifest. MCP `get-design-content` and `export-design` follow whatever indexing the tool uses (0-based or 1-based — the skill normalizes internally; the caller always speaks 1-based).
- `text_values` keys must match the placeholder verbatim (including punctuation and the leading pipe in date tags). The skill's matcher does a case-insensitive exact-match by default and falls back to substring match if no exact hit. Mismatches are reported as warnings.
- `image_assets` keys must match a role string from the element-map JSON (`full-bg`, `headshot`, `logo`, `icon`, `decorative-badge`, `decorative`, `photo-slot`). Unknown roles are reported as warnings and skipped.
- Multi-occurrence image slots (e.g. 2 headshots on a 2-speaker page) take a list — the Nth list entry maps to the Nth occurrence on that page in document order.

---

## Procedure — the Path B loop

### Step 1 — Load the element map for the template

Read `_element-maps/<template_id>.json` (relative to this skill folder).

If the file does not exist: stop with `{"status": "ERR_NO_ELEMENT_MAP", "template_id": ...}`. The catalog needs to be regenerated (see `scripts/build_element_maps.py`).

Validate that `page_index` ≤ `page_count`. If not: stop with `{"status": "ERR_PAGE_OUT_OF_RANGE"}`.

Pull the page's `text_slots` and `image_slots` arrays into local working state.

### Step 2 — Create the design from the brand template

Call `mcp__claude_ai_Canva__create-design-from-brand-template` with:

```
{
  "brand_template_id": "<template_id>",
  "title": "[AUTO] <asset_name> <YYYY-MM-DD>"
}
```

Capture the returned `design_id` and `canva_design_url`.

### Step 3 — Start the editing transaction

Call `mcp__claude_ai_Canva__start-editing-transaction` with `{"design_id": "<design_id>"}`. Capture from the response:
- `transaction_id` — needed for all subsequent ops
- `pages[]` — pass back verbatim to `perform-editing-operations` (it requires this exact array)
- `edit_design_url` — the in-flight edit URL (different from the create-design response's `edit_url`; surface this one at checkpoint)
- `thumbnails[]` — preview URL to show in chat

**You do not need to parse `richtexts[]` or `fills[]` from the response.** As of 2026-06-02 enrichment, every per-template JSON in `_element-maps/<template_id>.json` carries the runtime fields (element_id, parent_element_id, container_type, position, dimension, page_id, occurrence, editable) for every known slot. Read everything from disk; the transaction is opened only because subsequent ops require an open transaction context.

Sanity check the page from the element-map JSON: if any slot has `"editable": false`, skip ops that target it and add a `slot_pinned` warning (constraint #3).

### Step 5 — Resolve text replacements

For each `(placeholder, value)` in `text_values`:

1. Look up slots in the element-map JSON's `pages[<page_index>].text_slots[]` where `placeholder` matches (exact first; substring fallback). Each matching slot has a stored `element_id`.
2. If `value` is a string: emit one `replace_text` op per matched slot, all targeting `slot.element_id`.
3. If `value` is a list: emit one op per matched slot, in document order (sort by stored `position.top`, then `position.left`), up to `len(value)`. Extra matches beyond `len(value)` are left as-is.
4. If no slot matches: add `{"warning": "no_text_match", "placeholder": ..., "template_id": ..., "page": ...}` and continue.

Op shape: `{"type": "replace_text", "element_id": <slot.element_id>, "text": <value>}`. No runtime element discovery — `element_id` is read from the enriched JSON.

**Twitter "DELETE place image" placeholders** (constraint #4): if the placeholder text contains `DELETE` in caps, do NOT attempt to replace — emit a `delete_element` op instead (text + any bound SHAPE), and add a warning hinting the orchestrator that this slot was intended for an image insert which v1 does not support.

### Step 6 — Resolve image swaps

For each `(role, asset_ids)` in `image_assets`:

1. Look up the matching slots in the element-map JSON's `pages[<page_index>].image_slots[]` where `role` equals the manifest role. Sort by `occurrence` (already stored in the enriched JSON, 1-based).
2. If `asset_ids` is a string, apply to all matched slots with that asset. If `asset_ids` is a list, apply the Nth slot (by `occurrence`) with the Nth list entry. Extra occurrences past `len(asset_ids)` are left as-is.
3. **Decide the op type per slot, based on the slot's stored `container_type`:**
   - `container_type == "SHAPE"` → emit **`update_fill`** (5a). The slot is a real Canva framed-photo element; swapping the asset preserves the rounded clip path. Renders perfectly on-brand, no manual step.
   - `container_type == "RECT"` AND role is `headshot` or `photo-slot` AND `layered == true` → emit **`insert_fill`** (5b) AND add a `manual_drag_required` entry to the output. The new image lands on the page at the placeholder coords; the recipient drags it into the frame in Canva's UI, where Canva auto-creates a SHAPE-container fill inside the placeholder group.
   - `container_type == "RECT"` AND role is `full-bg`, `logo`, `icon`, or `decorative-badge` → emit **`update_fill`** (5a). No decorative foreground SHAPE above these; the swap is visible directly.
5a. **`update_fill` operation**: `{"type": "update_fill", "element_id": <slot.element_id>, "asset_type": "image", "asset_id": <new>, "alt_text": "<role> <subject if known>"}`.
5b. **`insert_fill` operation** (layered case requiring manual drag): `{"type": "insert_fill", "page_id": <slot.page_id, or the page's page_id from the page object>, "asset_type": "image", "asset_id": <new>, "alt_text": "<role> <subject if known>", "top": <slot.position.top>, "left": <slot.position.left>, "width": <slot.dimension.width>, "height": <slot.dimension.height>}`. All coordinates come from the enriched JSON — no runtime parsing required.

   Also append to the output's `manual_drag_required[]` array:
   ```json
   {"role": "<role>", "asset_id": "<new>", "subject": "<person/subject>", "instruction": "In Canva, drag the inserted image into the placeholder frame at this position. Canva will auto-fit it to the rounded frame."}
   ```
6. **SHAPE-only headshot circles** (constraint #2): if the slot's `raw` field contains `SHAPE` and has no `current_asset_id` (and therefore no enriched position/dimension), add `{"warning": "shape_only_slot_skipped", "role": ..., "advice": "insert fill manually via Canva UI or use a different template"}` and skip. v1 does **not** auto-insert into bare SHAPEs without a known anchor.
7. If no slot matches at all (role not present on this page): add `{"warning": "no_image_match", "role": ..., "asset_ids": ..., "template_id": ..., "page": ...}` and continue.

### Step 6b — Trim unused slots (`delete_slots` in the manifest)

When the manifest contains a `delete_slots[]` list, emit `delete_element` ops to remove unwanted template elements before the image inserts. Common cases:
- Solo speaker on a 2-up speaker card — delete the speaker 2 frame group + speaker 2 name/title text
- 2-speaker variant on a 3-up template — delete the unused third frame + text
- "Webinar" tag deletion when the asset is a non-webinar variant of a template

**Key capability (confirmed 2026-06-02):** `delete_element` accepts not just leaf element IDs (the ones returned in `fills[]` and `richtexts[]`) but **also their parent-ID prefix**. Live example from Rachel's solo launch run:

- Speaker 2 image fill exposed in `fills[]`: `element_id = "PBCV6H4c0hBh21lc-LBTwLFZGwqQPRfD9-LB4GhJFvL2fXW3Lh"`
- Calling `delete_element` on the parent prefix `"PBCV6H4c0hBh21lc-LBTwLFZGwqQPRfD9"` (no leaf child suffix) **succeeds** and removes the entire frame group — including the foreground decorative SHAPE which is NOT exposed in `fills[]` or `richtexts[]`.

This is the only documented MCP path to remove a foreground decorative SHAPE. Use it to cleanly excise unused placeholder frames; otherwise the SHAPE persists and renders its placeholder icon over the empty area.

**How to resolve `delete_slots` entries to ops:**

The manifest's `delete_slots[]` is a list of slot identifiers. Two shapes are accepted:

1. **By role + occurrence (preferred)** — `{"role": "headshot", "occurrence": 2}` deletes the 2nd headshot frame group in document order. The skill:
   - Looks up the matching slot in the element-map JSON's `image_slots[]` (role + occurrence — both stored)
   - Reads `slot.parent_element_id` (stored in the enriched JSON; derived as the element_id minus its last `-<segment>`)
   - Emits `{"type": "delete_element", "element_id": "<slot.parent_element_id>"}`
   - Also looks up associated text elements at adjacent positions (e.g. name/title to the right of a deleted headshot) and emits `delete_element` for each leaf
2. **By raw element_id** — `{"element_id": "PBCV6H4c0hBh21lc-LBzjddjR0DYNwzNR"}` is a passthrough for when the caller already knows the ID (e.g. a text element).

Add a warning if any delete op fails — typically means the ID was wrong, not that anything was destroyed (failed deletes are no-ops).

**Why this works** (confirmed 2026-06-02): When you drag a photo into a Canva placeholder frame via the UI, Canva creates a new sibling SHAPE-container image element inside the existing frame group — the new fill has rounded-corner clipping baked in (confirmed by inspecting `DAHLbAfO4xo`: speaker-2 frame received a new fill `containerElement.type: "SHAPE"` at 220.77×220.77, inset ~13px from the original 247.33×247.33 RECT, after a manual drop). The MCP's `insert_fill` only creates page-level RECT fills (no parent_element_id parameter) — it cannot replicate the UI drag-and-drop. So the workflow is:
- Skill inserts the image at the placeholder coords (page-level RECT, bare rectangle, full size)
- Recipient opens the Canva URL, drags the inserted image onto the placeholder once per slot (~5–10 seconds each)
- Canva auto-converts to a SHAPE-container fill inside the frame group; on-brand rounded styling preserved

**When this is NOT needed:** templates where the headshot is already a `SHAPE`-container fill (e.g. `DAHG3hqQ7oA` Tarek+Matt-style designs). In that case, `update_fill` swaps the photo cleanly with no manual step. The decision is automatic at runtime via Step 3's `containerElement.type` check.

### Step 7 — Apply the operations

Call `mcp__claude_ai_Canva__perform-editing-operations` with:

```
{
  "transaction_id": "<transaction_id>",
  "page_index": <manifest.page_index>,
  "pages": <pages array from Step 3>,
  "operations": [ ... built in steps 5+6 ... ]
}
```

Capture the response. Inspect `edit_operation_results[]` — each entry has its own `status`. Per-op `success` is mandatory; any per-op failure goes into `warnings[]`. Also surface the new `thumbnails[]` URL to the caller — the visual is the only honest validator (the spike showed `status: success` can mask layout issues).

### Step 8 — Commit checkpoint

If `commit_mode == "checkpoint"` (LinkedIn default):

Return to the caller with:

```
{
  "status": "AWAITING_REVIEW",
  "design_id": "<design_id>",
  "transaction_id": "<transaction_id>",
  "edit_url_in_transaction": "<edit_design_url from Step 3>",
  "thumbnail_url": "<from Step 7 response>",
  "warnings": [ ... ],
  "next_step": "Open the edit_url_in_transaction to verify the live edits, reply 'commit' to finalize, or 'cancel' to discard."
}
```

**Surface `edit_design_url` from Step 3, NOT the `edit_url` from Step 2.** The Step 2 URL points at the post-commit committed state; until commit, it still shows the empty template-copy. The Step 3 transaction URL reflects the in-flight edits. (Lesson from 2026-06-02 acceptance check — the wrong URL produced a "I don't see anything changed" moment.)

Halt here. The orchestrator (or Travis) will resume with `commit` or `cancel`. On `commit`, continue at Step 9. On `cancel`, call `mcp__claude_ai_Canva__cancel-editing-transaction` and return `{"status": "CANCELLED"}`.

If `commit_mode == "auto"`: continue directly to Step 9.

### Step 9 — Commit the transaction

Call `mcp__claude_ai_Canva__commit-editing-transaction` with `{"transaction_id": ...}`.

### Step 10 — Return

Return the final result:

```json
{
  "status": "OK",
  "design_id": "<design_id>",
  "edit_url": "<edit_url from Step 2 — now reflects committed state>",
  "view_url": "<view_url from Step 2>",
  "warnings": [ ... ],
  "manual_drag_required": [
    {"role": "headshot", "asset_id": "MAFZdaEt2Wc", "subject": "Rachel Folz",
     "instruction": "In Canva, drag the inserted image into the placeholder frame. Canva auto-fits it to the rounded frame."}
  ]
}
```

**The Canva URL is the deliverable.** No PNG export. The downstream owner (today: Furqan) picks up the design in Canva by URL, drags any `manual_drag_required` images into their placeholder frames (typically 5–10 seconds per drag), and publishes from Canva.

The orchestrator (e.g. `linkedin-asset-process.md`) MUST surface the `manual_drag_required` list to the recipient on the Jira card or in the chat-printed roll-up so they know there's a one-step finish.

---

## Per-template JSON schema (enriched)

Every per-template file in `_element-maps/<template_id>.json` carries both the markdown-derived slot definitions (placeholder text, role, dimensions string, layered flag, current_asset_id) AND the runtime fields needed to drive ops (element_id, parent_element_id, container_type, position, dimension, page_id, occurrence, editable). The skill reads this once at the start of a run and never re-discovers element IDs.

```json
{
  "template_id": "EAGqLMN8_Po",
  "name": "...",
  "use_case": "webinar-speaker-card",
  "page_count": 3,
  "inspection_design_id": "DAHLW7fJPJY",
  "enriched": true,
  "enriched_from_design_id": "DAHLW7fJPJY",
  "pages": [
    {
      "page": 1,
      "page_id": "PBCV6H4c0hBh21lc",
      "dimension": {"width": 1080, "height": 1080},
      "is_responsive": false,
      "text_slots": [
        {
          "placeholder": "Webinar title",
          "role_hint": "main headline",
          "element_id": "PBCV6H4c0hBh21lc-LBDPHJw1DqhJnKd8",
          "container_type": "TEXT",
          "position": {"top": 236.27, "left": 84.01},
          "dimension": {"width": 624.73, "height": 67}
        }
      ],
      "image_slots": [
        {
          "role": "headshot",
          "occurrence": 2,
          "layered": true,
          "current_asset_id": "MAGg-_VYc0Q",
          "element_id": "PBCV6H4c0hBh21lc-LBTwLFZGwqQPRfD9-LB4GhJFvL2fXW3Lh",
          "parent_element_id": "PBCV6H4c0hBh21lc-LBTwLFZGwqQPRfD9",
          "container_type": "RECT",
          "position": {"top": 669.25, "left": 362.48},
          "dimension": {"width": 247.33, "height": 247.33},
          "editable": true
        }
      ]
    }
  ]
}
```

**Field invariants the skill relies on:**
- `enriched: true` means runtime fields are populated. If `false`, fall back to live discovery via `start-editing-transaction`'s response (legacy path; still supported).
- `element_id` + `page_id` are deterministic per template — verified across multiple fresh designs from the same template. Cache freely.
- `occurrence` is 1-based within (role, page) and matches the document-order top-to-bottom, left-to-right ordering.
- `parent_element_id` is the element_id minus its last `-<segment>` — used by `delete_slots` to remove entire frame groups (including foreground decorative SHAPEs not exposed in the MCP's fills/richtexts arrays).
- `container_type` drives the SHAPE vs RECT op-routing decision (Step 6).

**Re-running enrichment:** `scripts/enrich_element_maps.py <template_id> <mcp_response_json>` merges fresh MCP transaction data into the per-template JSON in place. Run after re-crawling the markdown source, or to refresh runtime IDs if Canva ever rebuilds them (no evidence of that happening as of 2026-06-02).

---

## Slot-resolution rules — the six catalog-wide constraints

These come from the 2026-06-01 element-map crawl and the 2026-05-29 spike. The skill must respect them; the element-map JSON encodes the signal each rule keys on.

| # | Constraint | What the skill does |
|---|---|---|
| 1 | Layered headshot frames — back-layer `update_fill` is invisible behind a foreground decorative SHAPE that the MCP doesn't expose | Step 6 emits `insert_fill` at the back-layer's live coordinates AND adds a `manual_drag_required` entry. Recipient drags the image into the placeholder in Canva's UI (~5–10s per drag); Canva auto-creates a SHAPE-container fill inside the frame group and the rounded styling is preserved. Revised 2026-06-02 after exhaustive testing proved the MCP can't replicate the UI's drag-and-drop frame-fill behavior. |
| 2 | SHAPE-only headshot circles — no fill to update and no exposed coordinates to insert at | Step 6 skips with a `shape_only_slot_skipped` warning |
| 3 | `editable=false` pinned slots — non-editable headshot/icon frames | Step 4 filters non-editable elements; Step 5/6 emit a `slot_pinned` warning if a manifest entry tries to swap one |
| 4 | "DELETE place image or graphic here" text placeholders in Twitter family | Step 5 emits `delete_element` for placeholders containing `DELETE` (caps) + warning |
| 5 | 3 duplicate template-pair groups in the FB/LinkedIn share-card family | Out of scope for this skill — the **curated catalog** (`_cache/canonical-templates.json`) is responsible for marking only one ID per pair as canonical; orchestrators pick from canonical |
| 6 | Multi-page templates need explicit page selection | `page_index` is required in the manifest; the skill enforces `≤ page_count` |

---

## Commit modes

| Mode | When the skill commits | Reviewer sees |
|---|---|---|
| `checkpoint` (default for LinkedIn) | After human approval | Canva design URL — opens the editable design before commit |
| `auto` | Immediately after `perform-editing-operations` | Exported PNG only — design is already finalized |

`checkpoint` is the safer default. `auto` is for batch runs where the human will only review the final PNGs (faster, but a bad render means re-running the loop or hand-fixing in Canva). The Rachel Folz dry-run uses `checkpoint`.

---

## Output

JSON returned to the caller (see Step 10). The Canva design URL is the only deliverable — no PNG, no file on disk. Downstream owner (Furqan, today) opens the URL, finishes any manual cleanup (SHAPE-only fills, pinned slots, multi-page reorder), and publishes from Canva.

The skill does **not** clean up the Canva design after commit. Designs accumulate in Travis's Canva (`DAHLDiECHrE` from the 2026-05-29 spike, `DAHLa2AT45Q` from the 2026-06-02 acceptance check, etc.) — manual cleanup or a separate retention pass handles them. No API delete tool.

---

## Built-in test manifest — Rachel Folz speaker card

The acceptance-check manifest. Verified live on 2026-06-02 (design `DAHLa2AT45Q`); 6/6 ops succeeded, transaction committed.

```yaml
# Test manifest — Rachel Folz solo, 2026-06-25 IC Thought Leadership webinar
# Speaker-card 1-up variant (page 1 has 2 speaker slots; solo = fill speaker 1, delete speaker 2 entirely).

template_id: EAGqLMN8_Po
page_index: 1
design_title: TEST-rachel-folz-speaker-card-solo
text_values:
  "Webinar title": "Reset the Comms Strategy: Three Moves That Move the Numbers"
  "|   Mar 6, 2025 1:00 pm est": "|   Jun 25, 2026 1:00 pm EST"
  "Name": ["Rachel Folz"]
  "Title": ["Senior Director of Communications, ICP"]
image_assets:
  headshot: ["MAFZdaEt2Wc"]   # Rachel Folz canonical headshot — speaker 1 only
delete_slots:
  - {role: headshot, occurrence: 2}                       # remove speaker 2 frame + decorative SHAPE
  - {element_id: "PBCV6H4c0hBh21lc-LBzjddjR0DYNwzNR"}    # remove speaker 2 "Name" text
  - {element_id: "PBCV6H4c0hBh21lc-LBwpcbfPcXVQW3df"}    # remove speaker 2 "Title" text
commit_mode: checkpoint
```

Reference designs in Travis's Canva:
- 2026-05-29 spike: `DAHLDiECHrE` ("[TEST] Path B spike — safe to delete")
- 2026-06-02 acceptance check: `DAHLa2AT45Q` (early version — has the v1 bare-rectangle insert artifacts)
- 2026-06-02 launch run: `DAHLbDC9Nqo` ("Rachel Folz solo speaker card — 2026-06-25 IC Thought Leadership") — **the canonical reference for the current workflow**: speaker 2 fully removed, Rachel inserted at speaker 1 coords ready for manual drag-into-frame.

Expected visual: Rachel's headshot inserted at the speaker 1 position (flat rectangle, awaiting manual drag), her name + title to the right, updated headline + date, **no speaker 2 elements visible** (frame group + name + title all deleted), Cerkl logo + "PRESENTED BY:" intact at the bottom.

---

## Failure modes

| Symptom | Likely cause | Action |
|---|---|---|
| `ERR_NO_ELEMENT_MAP` | Catalog regenerated, JSON missing for this ID | Re-run `scripts/build_element_maps.py` |
| `ERR_PAGE_OUT_OF_RANGE` | `page_index` > `page_count` | Fix the manifest |
| `no_text_match` warning | Placeholder text in manifest doesn't appear in template | Re-inspect template via Canva; correct the placeholder string |
| `no_image_match` warning | No image slot with the requested role on this page | Check the element-map JSON for the page; pick a role that exists |
| `shape_only_slot_skipped` warning | Slot is a SHAPE without a fill | v1 limitation — insert fill manually or pick a different template |
| `slot_pinned` warning | `editable=false` element | Fall back to manual finish, or choose a template without pinned slots |
| "I don't see anything changed" when opening checkpoint URL | Surfaced the wrong URL — the create-design `edit_url` shows the empty pre-commit state | Surface `edit_design_url` from the `start-editing-transaction` response (the in-flight transaction URL), not the `edit_url` from `create-design-from-brand-template` |
| `update_fill` succeeds but the rendered headshot is invisible | Layered-frame back-layer swap is hidden behind a foreground decorative SHAPE (constraint #1) | Use `insert_fill` instead — see Step 6. The op should land at the back-layer's live coordinates, on top of the SHAPE. v1 fix landed 2026-06-02 after the first acceptance check exhibited this exact symptom on the Rachel Folz speaker card. |
| Visual regression that the per-op success masks | API success ≠ correct render | Always surface the post-op thumbnail to the human at checkpoint; the visual is the only honest validator |

---

## Files in this folder

```
template-fill/
├── SKILL.md                          ← this file
├── _element-maps/
│   ├── index.json                    ← id → name + use_case + path
│   ├── EAGqLMN8_Po.json              ← speaker card
│   └── … (96 files, one per template)
├── _cache/
│   ├── canonical-templates.json      ← built by refresh_canonical_cache.py
│   └── canonical-assets.json
└── scripts/
    ├── build_element_maps.py         ← markdown → per-template JSON (re-runnable)
    ├── refresh_canonical_cache.py    ← curation sheet → canonical-*.json
    └── rename_canva_assets.py        ← sheet → Connect REST PATCH /v1/assets/{id}
```

---

## Future work

- **Eliminate the manual-drag step.** Today, layered placeholder frames require the recipient to drag the inserted image into the frame in Canva's UI. If Canva ever adds (a) an MCP parameter to insert a fill *inside* an existing group, (b) a `convert_fill_to_shape` op type, or (c) drag-and-drop via API, we can drop the manual step. Worth periodic re-checks of the Canva MCP schema for new op types. The current workflow is the cleanest path the MCP supports today.
- **Auto-detect "unused" slots.** Today `delete_slots[]` is explicit in the manifest. A future version could infer: if the manifest's `image_assets.headshot` is a list of length 1 and the element-map shows 2 headshot slots, auto-delete slot 2. Reduces manifest verbosity; risk is silently deleting something the caller wanted to keep — defer until we have multiple webinar runs to ground the heuristic.
- **Source-design library.** Alternative pattern that avoids the manual-drag step entirely: build pristine "source designs" with SHAPE-container photo frames already wired (one per shape, ~20–30 min of design work). Skill uses `copy-design` to clone the source, then `update_fill` swaps photos cleanly. Best for high-volume shapes. Travis decided 2026-06-02 to defer this in favor of the manual-drag workflow.
- **Insert-fill support for SHAPE-only headshot circles** (constraint #2). Today: warn + skip. Future: if the element-map carries SHAPE bounds (currently it doesn't), emit `insert_fill` into those bounds — then the recipient drags-into-frame the same way.
- **Batch mode** — multiple manifests in one orchestrator call. Today: one design per skill invocation.
- **Render-verify automation** — current `eyeball the thumbnail` is human-only. Future: a vision pass that detects layered-frame regressions automatically.
- **PNG export wrapper** — if a downstream consumer ever needs a local PNG (e.g. a non-Furqan workflow), add a thin wrapper that calls `export-design` after commit. Out of scope for v1 since the Canva URL is the deliverable.
- **Wire to `/schedule`** once the LinkedIn process runs weekly.

---

## Learnings (append-only)

Notes from real runs go here. Each entry: what broke, what we changed, why.

### 2026-06-02 — first live acceptance check

- **`get-design-content` is text-only.** The MCP tool only returns `richtexts`, not image fills. The full element tree (text + image fills + page metadata) comes back from `start-editing-transaction`'s response. Step 4 of the procedure was wrong on the first draft of this skill (told the operator to call `get-design-content`); corrected after the live run.
- **Three distinct URLs in the loop.** `create-design-from-brand-template` returns `edit_url` and `view_url` (post-commit views). `start-editing-transaction` returns `edit_design_url` (the in-flight transaction view). For checkpoint review, surface the in-flight URL — the post-commit URL still shows the empty template-copy until commit. Travis caught this on the first run ("I don't see anything changed").
- **PNG export removed.** Downstream owner (Furqan today) finishes the asset in Canva and publishes from there. The Canva URL is the sole deliverable; the skill stops at `commit-editing-transaction`. Simpler interface, fewer moving parts, no temp files on disk.
- **Per-op `success` is not sufficient.** The MCP returns thumbnails in both the start-transaction response and the perform-ops response. Surface them at checkpoint — they're the visual confirmation that what the API thinks happened actually happened. (Constraint that pre-dated this skill, now codified in Step 7 + Step 8.)
- **Layered headshot frames need `insert_fill`, not `update_fill`.** The first commit looked successful at the API layer — speaker 1 fill went from `MAGg-_VYc0Q` to `MAFZdaEt2Wc`, all per-op statuses success. But the rendered design (verified via a second transaction) showed the same empty-frame placeholder icon. Diagnosis: the back-layer fill the MCP exposed sat behind a foreground decorative SHAPE that wasn't in `fills[]` or `richtexts[]` — the SHAPE was rendering its own placeholder icon over the swapped photo. Fix: emit `insert_fill` at the back-layer's live coordinates (read `containerElement.position` + `dimension` from the live transaction response). Confirmed: a single `insert_fill` op put Rachel's photo on top of the SHAPE as a bare rectangle.

- **The "purple frame" isn't a thin border — it's a full illustration.** Iterated `insert_fill` at multiple inset sizes (231×231, 200×200) trying to expose a clean decorative border around a smaller Rachel. Each smaller insert just revealed more of the placeholder *illustration* (cloud + grass scene) around her. The "rounded frame look" is produced by a SHAPE's clip path + the illustration filling the interior — there is no thin border with empty space to fit a smaller image into. The cleanest visual outcome via MCP-only ops is a full 247×247 bare-rectangle insert (covers everything).

- **The Canva UI's drag-and-drop creates an element type the MCP can't.** Travis dragged Rachel into the empty speaker-2 frame of a duplicate design (`DAHLbAfO4xo`). Inspection showed Canva had created a NEW sibling fill inside the existing frame group — `element_id: PBCV6H4c0hBh21lc-LBTwLFZGwqQPRfD9-LBZL5KFjzmmlBQpP`, `containerElement.type: "SHAPE"`, dimensions 220.77×220.77 (inset ~13px from the original 247.33 RECT). That SHAPE-container fill renders with rounded clipping perfectly. The MCP's `insert_fill` schema has no `parent_element_id` parameter — it can only insert page-level RECT fills, never child SHAPE fills inside a group. So the UI's drag-and-drop is currently unreplicable via MCP.

- **Final workflow (Travis's call 2026-06-02): MCP insert + manual drag.** For layered placeholder frames, the skill inserts the image at the placeholder's coords (page-level bare rect, full size) AND adds a `manual_drag_required` entry to the output. The recipient (Furqan today) opens the Canva URL, drags the inserted image onto the placeholder once (~5–10 sec), and Canva auto-creates the SHAPE-container fill inside the frame group. On-brand rounded styling preserved with one manual step per slot. Skill bumped to v1.3.0. The decision rule at runtime: branch on the live `containerElement.type` — `SHAPE` → `update_fill` (no manual step); `RECT` + layered headshot → `insert_fill` + manual-drag flag.

- **`delete_element` accepts parent-ID prefixes — the one MCP path to remove foreground decorative SHAPEs.** On the 2026-06-02 launch run (design `DAHLbDC9Nqo`), speaker 2 needed to be removed entirely for Rachel's solo card. The MCP exposed the speaker 2 image fill at `element_id: "PBCV6H4c0hBh21lc-LBTwLFZGwqQPRfD9-LB4GhJFvL2fXW3Lh"` (3-segment: page-parent-child), but the foreground decorative SHAPE wasn't exposed at all in `fills[]` or `richtexts[]`. Calling `delete_element` on just the **parent prefix** `"PBCV6H4c0hBh21lc-LBTwLFZGwqQPRfD9"` (no leaf segment) succeeded and removed both the back-layer image fill AND the foreground decorative SHAPE in one op — the entire frame group went away cleanly. This is the only documented MCP path to address foreground SHAPEs that aren't directly exposed; previously we believed they were completely unaddressable. Codified as Step 6b (`delete_slots` manifest field) and bumped skill to v1.4.0. Use cases: solo speakers on multi-up cards, 2-speaker variants of 3- or 4-up grids, removing decorative elements that don't apply to a given asset.

- **Element-map JSONs enriched — skill now disk-driven (v1.5.0).** 2 parallel sub-agents ran `enrich_element_maps.py` against all 96 templates' existing 2026-06-01 inspection designs. Each transaction was opened (read-only), the `pages[] / richtexts[] / fills[]` saved, the merge utility ran, and the transaction cancelled. Result: 259 text slots + 378 image slots enriched with runtime fields (element_id, parent_element_id, container_type, position, dimension, page_id, occurrence, editable). Verified element_id and parent_element_id are deterministic per template — the speaker-card's speaker-2 parent_element_id in the JSON (`PBCV6H4c0hBh21lc-LBTwLFZGwqQPRfD9`) matches exactly the ID that succeeded in the launch-run `delete_element` op. Steps 3, 5, 6, 6b rewritten to read from disk instead of parsing the live transaction response. The transaction is still opened (perform-editing-operations requires it), but the response data is no longer parsed for element IDs.

  130 text + 166 image slots were unmatched across the catalog. Most of those (12 templates) had empty markdown-source JSONs to begin with — those need a source-markdown re-crawl, not an enrichment fix. The rest reflect markdown crawl gaps on multi-page templates where the crawler summarized later pages as "same skeleton" instead of enumerating slots (e.g., EAGqLMN8_Po pages 2-3 are only partially enriched). For the speaker-card use case we care about, page 1 is fully enriched (5/5 text, 6/6 image).
