# Weekly LinkedIn Asset Production

> Sibling to [`linkedin-process.md`](linkedin-process.md). For every LinkedIn draft in the locked week that needs a Canva graphic, **either** scaffold a manifest and dispatch [`template-fill`](../../design/canva-skills/template-fill/SKILL.md) (non-webinar wraps) **or** look up the URL from the webinar's `canva-manifests/` (webinar wraps). Drop the resulting Canva edit URL into the matching Jira CSV Task Description on an `Asset:` line.
>
> **The Canva URL is the only deliverable.** Furqan picks up each design in Canva from that URL, finishes any manual cleanup, and publishes from Canva directly. No PNG export.

Runs **after** [`linkedin-process.md`](linkedin-process.md) (which produces the drafts + fills `Copy:` lines). This process adds the visual asset URL.

## Trigger

**Default (weekly):**
- "Render the LinkedIn assets for this week"
- "Build next week's LinkedIn assets"
- "Run weekly LinkedIn asset production"

**Overrides:**
- *Single post:* `"Render the asset for [slug]"` — operates on one draft, defaults to `commit_mode: checkpoint`
- *Multi-week:* `"Render LinkedIn assets for weeks 1–2"`
- *Re-render:* `"Re-render the asset for [slug]"` — uses the existing manifest, overwrites the `result:` block

## Inputs

| Input | Required | Default | Description |
|---|---|---|---|
| `target_window` | optional | the week of the most recent Jira CSV in `../../content-plan/jira/imports/` | Which week to render |
| `subset` | optional | All eligible drafts | List of draft slugs to render |
| `commit_mode` | optional | `auto` for batch (≥2 drafts), `checkpoint` for single-post | Sub-agent commit behavior |

I'll confirm the resolved draft list before dispatching.

## Context to load

- /Users/travisfoster/claude-code/cerkl/marketing/CONTEXT.md
- /Users/travisfoster/claude-code/cerkl/marketing/design/CONTEXT.md
- /Users/travisfoster/claude-code/cerkl/marketing/channels/linkedin/CONTEXT.md
- /Users/travisfoster/claude-code/cerkl/marketing/channels/linkedin/asset-packs.md

(Per [PRINCIPLES.md #4](/Users/travisfoster/claude-code/cerkl/PRINCIPLES.md), this list is authoritative for this scope. Sub-agents load `template-fill/SKILL.md` themselves at dispatch time.)

---

## Pre-flight checks

Stop and surface an error if any fail:

- **[`asset-packs.md`](asset-packs.md) exists and lists ≥1 template.** This is the authoritative cache gate.
- **Each chosen template has `enriched: true`** in `template-fill/_element-maps/<id>.json`. Warn if any chosen template's text_slots are <50% populated (substring-fallback risk).
- **The week's Jira CSV exists** at `../../content-plan/jira/imports/YYYY-Www.csv`.
- **For each eligible draft, the matching Jira Task row exists with a filled `Copy:` line** (Phase A ran). If still `[COPY_PLACEHOLDER]`, surface `phase_a_incomplete` and stop.
- **For each webinar-wrap draft, the webinar manifest's `result:` block exists.** If not, surface `webinar_pack_unrendered` and skip — don't fall back to LinkedIn-channel rendering.

---

## Steps

### Step 1 — Resolve eligible drafts for the target window

- **Owner:** Claude
- **Inputs:** `target_window`, `subset`, the week's CSV at [`../../content-plan/jira/imports/YYYY-Www.csv`](../../content-plan/jira/), `drafts/` folder
- **Produces:** in-memory list `[{slug, type, publish_date, draft_path, wraps_source, route}]`

For each LinkedIn Task in the week's CSV (parse `Post type:` + `Wraps:` from the Description; skip barebones short-video rows):

1. Locate the matching draft file at `drafts/YYYY-MM-DD_<type>_<slug>.md`. If missing, surface `draft_missing` and skip.
2. Classify by `route`:
   - **`skip-static-blog`** — type is `static-blog`. LinkedIn auto-renders the link card.
   - **`skip-poll`** — type is `poll`. Native widget.
   - **`skip-short-video`** — type is `short-video`. Video pipeline.
   - **`webinar-lookup`** — `Wraps:` field points at a webinar event folder (under `channels/webinar/`). Read URL from webinar manifest; no render.
   - **`render`** — everything else. Scaffold a manifest, dispatch a sub-agent.

Confirm the resolved list with Travis before proceeding to Step 2.

### Step 2 — Build per-draft work plan

Branch by `route`.

#### Step 2a — Webinar-lookup drafts

- **Inputs:** webinar event folder path (parsed from draft's `Wraps:` field)
- **Produces:** `(slug, edit_url)` pairs

For each `webinar-lookup` draft:
1. Resolve the webinar role from the draft's post type:
   - `static-theme` wrapping a webinar → role = `share-1200x628` (LinkedIn feed share)
   - `carousel` wrapping a webinar → role = `speaker-card` (LinkedIn intro post)
   - 2-days-to-go boost (caption mentions "2 days" or "Wednesday") → role = `countdown`
2. Read `<event-folder>/canva-manifests/<role>.yml`. Pull `result.edit_url` from the `result:` block.
3. If `result:` block is missing, add `webinar_pack_unrendered` warning and skip — the webinar process needs to run first.

No manifest scaffolded for these; no sub-agent dispatched. Go directly to Step 6 (Jira mirror).

#### Step 2b — Render drafts (scaffold manifest)

- **Inputs:** draft path, [`asset-packs.md`](asset-packs.md) selector table
- **Produces:** `canva-manifests/<slug>.yml` per render draft

For each `render` draft:
1. Read the draft's `## Asset` section. Extract:
   - Subtype signal (stat / quote / photo+text / text-only / problem-solution / N-part list / product / downloadable / blog-promo)
   - Visual concept text (stat numeral, statement, quote body, headline)
   - Optional `Asset ID:` line (only for photo-slot content templates)
2. Look up `(post_type, subtype) → template_id, page_index` in [`asset-packs.md`](asset-packs.md#post-type--template-selector).
3. If lookup is ambiguous, surface `template_unclear` warning with the draft slug + candidates, and ask Travis to pick. Do not guess.
4. Read the chosen `template-fill/_element-maps/<template_id>.json`. Extract the page's `text_slots[].placeholder` list — these become the `text_values` keys.
5. Map the draft's Asset content onto the placeholders:
   - Stat numeral → the `XX%`-shaped placeholder (template-specific)
   - Statement → the body-statement placeholder
   - Top tag (if specified) → the decorative tag placeholder
   - Leave any unmapped placeholders out (template defaults persist)
6. **Length-fit pre-check** — for each text replacement, compute `char_count(replacement) / char_count(placeholder)`. If ratio > 1.3 AND the slot has a foreground element below in the element-map (typical for the stat-card statement slot), add a `length_fit_risk` warning. Ask Travis whether to (a) shorten the draft, (b) pick a different template, or (c) proceed with risk acknowledged.
7. Write the manifest to `canva-manifests/<slug>.yml`. Include the wrapping source as a top comment for re-runs. Set `commit_mode` to the orchestrator-level value.

Manifest shape — see [`asset-packs.md` § Manifest generation rule](asset-packs.md#manifest-generation-rule).

### Step 3 — Pre-flight on scaffolded manifests

For each manifest written in Step 2b:
- Verify `template_id` is in [`asset-packs.md`](asset-packs.md) (cache gate). Reject with `template_out_of_pack` if not.
- Verify `text_values` keys appear in the element-map's `text_slots[].placeholder` (exact preferred; substring acceptable with warning).
- Verify `page_index ≤ template.page_count`.

Manifests failing pre-flight are pulled from the batch with explicit warnings — they don't dispatch, but the rest of the batch proceeds.

### Step 4 — Parallel sub-agent dispatch

- **Owner:** Claude (orchestrator)
- **Sequencing:** Send a single message with N `Agent` tool calls (one per manifest).
- **Inputs:** Each manifest's absolute path
- **Produces:** Per-manifest JSON result

Each sub-agent gets a self-contained brief — matches [`webinar-canva-render`](../webinar/skills/webinar-canva-render/SKILL.md) Step 4 verbatim except for the absolute manifest path:

```
You are running template-fill against a single Canva manifest.

1. Read the manifest at: <absolute manifest path>
2. Follow the procedure in template-fill's SKILL.md:
   /Users/travisfoster/claude-code/cerkl/marketing/design/canva-skills/template-fill/SKILL.md
   (Steps 1 → 10, including delete_slots handling in 6b)
3. **Smart text matching — override template-fill's blind substring fallback.**
   When you call start-editing-transaction (Step 3), capture the live richtexts[] response.
   For each manifest text_value whose key has no exact match in the element-map's text_slots[]:
   search richtexts[] for an element whose rendered text equals the manifest key exactly.
   If exactly one such element exists on the target page, use its element_id directly via replace_text.
   For multiple-match cases, disambiguate by position/size/font (largest = headline, smaller below
   a "Name" = "Title", etc.). Only fall back to substring matching when neither yields an exact match.
4. Use commit_mode from the manifest.
5. Return ONLY a JSON object — no narrative, ≤200 words:
   {
     "slug": "<filename stem>",
     "status": "OK" | "AWAITING_REVIEW" | "ERR_…",
     "design_id": "<DAH…>",
     "edit_url": "<https://www.canva.com/design/DAH…/edit>",
     "view_url": "<https://www.canva.com/design/DAH…/view>",
     "warnings": [...],
     "manual_drag_required": [...]
   }
```

Sub-agent type: `general-purpose`. No conversation context inherited. Each renders independently — no shared state, no order dependencies.

**Why `auto` for batch:** sub-agents can't all halt at `AWAITING_REVIEW` in parallel. Single-post override path uses `checkpoint` because there's no parallelism — Travis reviews before commit.

### Step 5 — Collect results + write `result:` blocks

- **Owner:** Claude
- **Produces:** Updated manifests + accumulated `slug → result` dict

**URL verification (required — do not trust the sub-agent's self-reported URL).** The trustworthy handle is `design_id` (11-char `DA…`), not any URL: a sub-agent can hallucinate a link, AND `get-design`'s own `urls.edit_url`/`view_url` are `/d/<token>` short links that **rotate on every call** (verified — three different tokens for one design), so they go stale in a saved CSV. The orchestrator is a separate trust boundary, so for each returned `design_id`:
  1. Call `mcp__claude_ai_Canva__get-design` to confirm the design exists/committed (validates the `design_id`).
  2. Write the **stable canonical URL** `https://www.canva.com/design/<design_id>/edit` into the `result:` block and the CSV — built from the `design_id`, never the rotating `/d/<token>` from the response and never the sub-agent's string.
  - If `get-design` errors or returns no design, the render did not produce a usable asset: surface `design_not_found`, do **not** write an `Asset:` line, and flag it for re-render.

For each sub-agent return with `status: OK`, append a `result:` block to its manifest YAML (using the **canonical** `design_id`-derived URL):

```yaml
# === Render result (written by linkedin-asset-process) ===
result:
  rendered_at: "2026-06-02T14:32:00Z"   # ISO timestamp, UTC
  design_id: "DAH…"
  edit_url: "https://www.canva.com/design/DAH…/edit"
  view_url: "https://www.canva.com/design/DAH…/view"
  template_id: "EAH…"
  warnings: [...]
  manual_drag_required: [...]
```

The manifest is now the audit trail: what was rendered, when, with what result.

For `webinar-lookup` drafts (Step 2a), the URL came from the webinar's manifest — no LinkedIn-side manifest exists. Track these in the result dict only.

### Step 6 — Mirror to Jira CSV

- **Owner:** Claude
- **Inputs:** result dict + target week's CSV path
- **Produces:** Updated CSV Task Descriptions

For each draft with a `get-design`-**verified** `edit_url` (from Step 5's verification, or the Step 2a webinar lookup):

1. Find the Task row in `../../content-plan/jira/imports/YYYY-Www.csv` matched by `Post type:` + `Wraps:` in the Description (same key as Step 1; not free-text Summary).
2. Add an `Asset:` line **at the end of the Description**, after the caption (separated by a blank line). Format:

```
Asset: <edit_url>
```

3. If the result has a non-empty `manual_drag_required[]`, add a `Manual finish:` line directly below `Asset:`:

```
Manual finish: drag <N> image(s) into placeholder frames in Canva — <role:subject pairs>
```

Use a real CSV library (Python `csv`) — Description fields contain newlines.

**Invocation modes:** when this runs as a Wave subagent inside the weekly content session, do **not** edit the CSV — return the values (the orchestrator fills all tokens in one pass). Only edit the CSV directly when running standalone (single writer either way).

**Placement:** put the `Asset:` line **at the bottom of the Description**, separated from the caption by a blank line — not directly below the `Copy:` label, which splits the Copy block visually. Furqan finds it after scanning past the caption.

If a Task row is missing or has no `Copy:` line filled in, surface a `csv_row_unfilled` warning and skip — Phase A (linkedin-process.md) hasn't run for that draft.

### Step 7 — Roll up and report

- **Owner:** Claude
- **Produces:** Chat-printed summary

```
Rendered N/N LinkedIn assets for Week WW (YYYY-MM-DD – YYYY-MM-DD):

| Type | Slug | Route | Status | URL | Warnings | Manual finish? |
|---|---|---|---|---|---|---|
| static-theme | financial-services-double-mandate | render | OK | <edit_url> | 0 | no |
| static-blog | microsoft-teams-internal-communications | skip-static-blog | n/a | n/a | n/a | n/a |
| poll | financial-services-ic-mandate | skip-poll | n/a | n/a | n/a | n/a |

Warnings to review:
- (slug): length_fit_risk — statement char count 63 vs. placeholder baseline 47 (ratio 1.34×)

Canonically stored in:
- canva-manifests/<slug>.yml (result: block per render)

Mirrored to:
- content-plan/jira/imports/YYYY-Www.csv (Asset: line per Task)
```

Surface any draft with:
- `template_unclear`, `length_fit_risk`, `photo_slot_unspecified`, `slot_pinned`, `no_text_match`, `no_image_match` warnings
- `template_out_of_pack` error (cache gate rejection)
- `webinar_pack_unrendered` (upstream dependency missing)
- `phase_a_incomplete` / `csv_row_unfilled` (linkedin-process.md hasn't run)

---

## Failure modes

| Symptom | Cause | Action |
|---|---|---|
| `template_out_of_pack` | Manifest's `template_id` isn't in `asset-packs.md` | Either add to the pack (with enriched element-map verified) or rebuild the manifest with a packed template |
| `template_unclear` | Scaffolder couldn't infer subtype from the draft's `## Asset` section | Travis picks; consider tightening the draft template's `## Asset` skeleton |
| `length_fit_risk` | Replacement text >1.3× placeholder baseline on a bounded slot | Shorten the draft, pick a different template, or proceed with eyes-open |
| `photo_slot_unspecified` | Template needs a content image; draft's `## Asset` has no `Asset ID:` line | Add `Asset ID: <id>` to the draft, or accept template default |
| `webinar_pack_unrendered` | LinkedIn draft wraps a webinar but webinar process hasn't rendered | Run `webinar-canva-render` first |
| `phase_a_incomplete` | Jira Task row still has `[COPY_PLACEHOLDER]` | Run `linkedin-process.md` first |
| Sub-agent returns `AWAITING_REVIEW` instead of `OK` | A manifest's `commit_mode` was `checkpoint` in a parallel batch | Orchestrator should override all manifests to `auto` for batch runs; this is a bug in Step 4 |
| Sub-agents return many `no_text_match` warnings | Manifest text_values keys don't match the chosen template | Likely a selector mismatch; revisit `asset-packs.md` mapping or the draft's `## Asset` section |

---

## Output

- One Canva design per `render` draft (lives in Travis's Canva)
- Per-draft manifest in `canva-manifests/<slug>.yml` with `result:` block (canonical audit trail)
- Updated Jira CSV with `Asset:` line on each LinkedIn Task Description
- Chat-printed roll-up

## What this does NOT do

- **Render webinar-wrap posts.** Webinar process owns those. This process looks up URLs.
- **Resolve photo-slot asset_ids automatically.** Caller declares via `Asset ID:` in the draft. V2 builds the fit index.
- **Reformat or shorten draft copy to fit slot baselines.** The length-fit check surfaces the risk; Travis decides what to change.
- **Push to Canva (publish).** Furqan opens each URL, finishes manual cleanup if any, and publishes from Canva.
- **Cleanup old Canva designs.** Renders accumulate in Travis's Canva account; manual cleanup handles them.

## Future work

- **V2 — Asset-fit index.** See [`asset-packs.md` § Future work](asset-packs.md#future-work-v2).
- **Render-verify automation.** Today the per-op success is checked but visual regression is human-only. A vision pass on each post-render thumbnail to detect element overlap would catch problems before commit. Pair with the length-fit pre-check.
- **Re-render UX.** Today re-rendering means editing the manifest and re-running with `subset: [<slug>]`. A cleaner shape would be `"Re-render <slug> with statement: <new text>"` — orchestrator updates the manifest in place, dispatches one sub-agent.
- **Auto-archive drafts after CSV row + manifest are both filled** — currently manual move from `drafts/` to `archive/`.
