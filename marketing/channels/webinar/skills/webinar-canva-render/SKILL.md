---
name: webinar-canva-render
description: "Render the full Canva asset pack for one webinar by dispatching one parallel sub-agent per manifest in the event's canva-manifests/ folder. Each sub-agent invokes template-fill against its assigned manifest and returns the Canva edit URL. The orchestrator appends each URL to its manifest YAML (primary source-of-truth) and mirrors the URL into the Drive MAP's Deliverable column (bonus for the internal team). Trigger phrases: 'render the canva assets for [webinar]', 'kick off canva render for rachel', 'run the asset pack render', 'fill all the webinar templates'. Inputs: event-folder path + headshot Canva asset ID. Output: chat-printed roll-up of role → URL + warnings + manual_drag_required list."
metadata:
  version: 0.2.0
  status: live
  changelog:
    - "0.2.0 (2026-06-10): URLs are now Canva-verified. Sub-agents must call get-design after commit and return the canonical /design/<id>/edit form; orchestrator Step 6 validates every edit_url against its design_id before write. Fixes the short-link 404 incident."
---

# Webinar Canva Render

Channel-level orchestrator that renders a webinar's full Canva asset pack — one design per manifest in `<event-folder>/canva-manifests/` — by dispatching parallel sub-agents that each invoke [`template-fill`](/Users/travisfoster/claude-code/cerkl/marketing/design/canva-skills/template-fill/SKILL.md). Atomic per-design rendering stays in `template-fill`; this skill handles the fan-out, the headshot injection, the result collection, and the URL write-back.

**Output destination (canonical):** each manifest YAML in the event folder gets a `result_url:` field appended after render. The event-folder manifests are the source of truth — downstream skills (`webinar-promo-emails`, `webinar-linkedin-posts`, `webinar-blog-intro`, `webinar-followup-email`, `webinar-recap-blog`) read URLs from there.

**Output destination (mirror, bonus):** the Drive MAP's "Deliverable" column gets the URL written into every Phase 3 / 4 / 5 row whose Deliverable string matches a rendered role. This is a courtesy for the internal team using the Drive MAP as a working doc — it is **not** a source of truth.

---

## When to use this skill

Use when:
1. `webinar-project-init` has scaffolded the event folder with `canva-manifests/<role>.yml` files (one per pack role).
2. The speaker's headshot is uploaded to Canva and the asset ID is captured (Travis or a separate helper resolves this — out of scope for this skill).
3. Each manifest is render-ready (template_id, page_index, text_values populated, `headshot: ["TBD …"]` or already-filled).

Do NOT use if the manifests aren't cleaned up — see "Pre-flight" below for the checks.

---

## Inputs

| Input | Required | Description |
|---|---|---|
| `event_folder` | ✓ | Absolute path to the event folder, e.g. `/Users/travisfoster/claude-code/cerkl/marketing/channels/webinar/rachel-folz-june-2026/` |
| `headshot_asset_id` | ✓ | Canva asset ID for the speaker's headshot (e.g. `MAFZdaEt2Wc`). v1 takes this as a literal input; v2 may resolve from a Drive file or URL. |
| `commit_mode` | optional | `auto` (default — batch run) or `checkpoint` (per-design human review). Auto is the only practical mode for ≥3 parallel sub-agents. |
| `roles_subset` | optional | List of role names to render. Defaults to **all manifests in the folder**. Use to re-render a single asset or skip a known-bad one. |

---

## Pre-flight checks

Stop and surface an error if any fail:

- **Event folder exists** and contains `canva-manifests/` with ≥1 `.yml` file.
- **Headshot asset ID is non-empty** and looks like a Canva asset ID (`MA…` prefix). v1 does NOT verify the ID exists in Canva — a bad ID surfaces as a render failure per-subagent.
- **Each manifest has the required keys**: `template_id`, `page_index`, `design_title`, `text_values`. Manifests missing any of these are skipped with a `manifest_invalid` warning.
- **For templates known to need `delete_slots`** (e.g. speaker-card with 2-up layout on page 1 for a solo render), the manifest must include the `delete_slots` block. If missing, the design will keep placeholder speakers. Surface a `delete_slots_missing` warning and let the orchestrator decide whether to proceed.

---

## Procedure

### Step 1 — Enumerate manifests

Read `<event_folder>/canva-manifests/*.yml`. Skip `README.md`. Build a list of `(role, path, content)` tuples — `role` is the filename stem (e.g. `speaker-card.yml` → `speaker-card`).

If `roles_subset` is provided, filter to those roles only.

### Step 2 — Inject headshot asset ID

For each manifest content dict where `image_assets.headshot` contains a `TBD` string, replace with `[<headshot_asset_id>]`. Multi-occurrence headshot slots (where `headshot:` is a list of N entries) get the same asset ID broadcast across all N entries by default (override per-manifest if needed). Write the updated manifest back to disk so it's a permanent record.

### Step 3 — Apply `commit_mode` override

If the orchestrator-level `commit_mode` is `auto`, override every manifest's `commit_mode` field to `auto`. (Per-manifest checkpoint mode is incompatible with parallel batch dispatch — sub-agents would all halt at AWAITING_REVIEW.)

### Step 4 — Dispatch parallel sub-agents

**Send a single message with N `Agent` tool calls** (one per manifest). Each sub-agent gets a self-contained brief:

```
You are running template-fill against a single Canva manifest.

1. Read the manifest at: <absolute manifest path>
2. Follow the procedure in template-fill's SKILL.md:
   /Users/travisfoster/claude-code/cerkl/marketing/design/canva-skills/template-fill/SKILL.md
   (Steps 1 → 10, including delete_slots handling in 6b)
3. **Smart text matching — override template-fill's blind substring fallback.** Short manifest keys (e.g. "Title") can substring-collide with longer placeholders (e.g. "Webinar title"). Don't blindly substring — you have better data:
   - When you call `start-editing-transaction` (template-fill Step 3), capture the live `richtexts[]` response. It carries every text element on the page with its exact rendered text, element_id, position (top/left), dimension (width/height), and font size — including elements the element-map JSON may have merged or omitted.
   - For each manifest text_value whose key has no **exact** match in the element-map's `text_slots[]`: search `richtexts[]` for an element whose rendered text equals the manifest key exactly. If exactly one such element exists on the target page, use its element_id directly via `replace_text`. No warning needed — this is the right answer.
   - If multiple elements have matching text (e.g. three speaker "Title" slots in a 3-up variant), disambiguate by context: smaller text directly below a "Name" element is that speaker's "Title"; the largest text near the top is the headline; positional order (top-to-bottom, left-to-right) maps to the manifest's positional list ordering.
   - Only fall back to template-fill's substring matcher when neither the element-map nor `richtexts[]` yields an exact match. The substring path is the last resort, not the default.
4. **Smart headshot insertion — override template-fill's "DELETE placeholder unsupported" punt.** Some templates (Twitter/X share-card family, including `share-1200x628` and `share-16x9`) wire speaker thumbs as text placeholders containing "DELETE place image…" or as bare SHAPEs/empty rectangles instead of pre-wired headshot `image_slots`. Template-fill v1's spec says delete the DELETE-text and warn that v1 doesn't insert into those slots — **do not follow that punt:**
   - When a manifest's `image_assets.headshot` would produce a `no_image_match` warning AND the live `richtexts[]` / `fills[]` carries a recognizable target position for the speaker-1 thumb (a DELETE-text element, an empty SHAPE, or a placeholder rectangle near the speaker-1 Name), emit `insert_fill` at those coordinates with the headshot `asset_id`.
   - Match the existing thumb's width/height when known; default to a square sized to the visible placeholder otherwise.
   - Also `delete_element` the DELETE-text placeholder if it was the position anchor.
   - Add a `manual_drag_required` entry — recipient drops the rectangle into the visible frame in Canva's UI (same pattern as the speaker-card layered case).
   - **Do not treat DELETE-placeholder templates as a different category from layered frames.** Same workflow.
5. Use commit_mode from the manifest (already normalized by the orchestrator).
6. **Verify the URLs against Canva — do NOT self-report them.** After a successful commit you know the `design_id`. The edit/view URLs returned inline by the editing-transaction tools are unreliable short-link tokens that frequently 404 (real incident 2026-06-10: every sub-agent reported a `/d/<token>/edit` link that did not resolve, even though the designs were fine). So:
   - Call `mcp__claude_ai_Canva__get-design` with the committed `design_id`.
   - Take `view_url` **verbatim** from that response.
   - Construct `edit_url` as the stable canonical form `https://www.canva.com/design/<design_id>/edit` (do not paste a `/d/<token>` short link — even the one get-design returns; the `/design/<id>/edit` form is the durable one).
   - If get-design fails, return `status: "ERR_URL_UNVERIFIED"` with the `design_id` so the orchestrator can re-pull — never emit a guessed/self-constructed URL.
7. Return ONLY a JSON object — no narrative, ≤200 words:
   {
     "role": "<filename stem>",
     "status": "OK" | "AWAITING_REVIEW" | "ERR_…",
     "design_id": "<DAH…>",
     "edit_url": "https://www.canva.com/design/<design_id>/edit",   // canonical form, built from the verified design_id
     "view_url": "<verbatim from get-design>",
     "warnings": [...],
     "manual_drag_required": [...]
   }
```

Sub-agent type: `general-purpose`. No conversation context inherited. Each renders independently — no shared state, no order dependencies.

### Step 5 — Collect results

Accumulate the N JSON returns into a `role → result` dict.

### Step 6 — Write URLs into manifests (canonical store)

**URL guard (orchestrator-side safety net).** Before writing, validate every result's `edit_url`. It MUST match `https://www.canva.com/design/<design_id>/edit` where `<design_id>` equals that result's `design_id`. If a sub-agent returned anything else — a `/d/<token>` short link, a mismatched ID, or status `ERR_URL_UNVERIFIED` — do NOT store it. Call `mcp__claude_ai_Canva__get-design` yourself with the `design_id`, then store the canonical `https://www.canva.com/design/<design_id>/edit` (and `view_url` verbatim from get-design). This is the backstop for the 2026-06-10 short-link 404 incident; never let an unverified URL reach the manifest.

For each result with `status: OK`, append a `result:` block to the matching manifest YAML:

```yaml
# Append to the bottom of the manifest:
result:
  rendered_at: "2026-06-02T14:32:00Z"   # ISO timestamp, UTC
  design_id: "DAH…"
  edit_url: "https://www.canva.com/design/DAH…/edit"   # canonical /design/<id>/edit form ONLY — never a /d/<token> short link
  view_url: "https://www.canva.com/d/…"                # verbatim from get-design
  warnings_count: 0
  manual_drag_required_count: 1
```

The manifest YAML becomes the per-asset audit trail: what was rendered, when, with what result.

### Step 7 — Mirror URLs into the Drive MAP (bonus)

Read the brief at `<event_folder>/<speaker-slug>.md`. Extract the MAP sheet ID from the `Mutual Action Plan:` header link.

For each result with `status: OK`, find rows in the MAP's `Project Plan` tab where the **Deliverable** column matches the role string (e.g. `speaker-card`, `email-banner`) and replace the cell with the `edit_url`.

Use `gws sheets spreadsheets values batchUpdate` — only the matching cells, not the whole sheet. If multiple rows share the same Deliverable role (e.g. `email-banner` appears on 3 promo rows for Email Blast #1/#2/#3), each gets the same URL.

If the brief doesn't have a parseable MAP link, skip this step with a `map_mirror_skipped` warning and continue — the canonical store (manifest YAMLs) is already done.

### Step 8 — Roll-up chat output

Print a single roll-up message:

```
Rendered N/N Canva assets for <webinar slug>:

| Role | Status | URL | Warnings | Manual drag? |
|---|---|---|---|---|
| speaker-card | OK | <edit_url> | 0 | yes (1 headshot) |
| email-banner | OK | <edit_url> | 1 (date placeholder) | yes (2 headshots) |
| …

Manual-drag list (paste to Furqan with the URLs):
- speaker-card: drag headshot into speaker 1 frame
- email-banner: drag headshots into both speaker frames

Warnings to review:
- email-banner: date placeholder "Mar 6, 2025…" matched via substring — verify the date text on the design is correct

URLs canonically stored in:
- <event_folder>/canva-manifests/*.yml (result_url field per manifest)

URLs mirrored into:
- Drive MAP "Deliverable" column (rows matching each role)
```

---

## Failure modes

| Symptom | Cause | Action |
|---|---|---|
| Some sub-agents return `ERR_NO_ELEMENT_MAP` | The template's element-map JSON is missing | Investigate `template-fill/_element-maps/<template_id>.json`; re-run `scripts/build_element_maps.py` if needed; re-render the affected role with `roles_subset: [<role>]` |
| Sub-agents return many `no_text_match` warnings | Manifest text_values keys don't exist in the element-map | Likely a manifest-cleanup issue (e.g. writing `"Title"` against a template whose element-map merged it into `"Name"`). Refine the manifest, re-render |
| Sub-agents return `AWAITING_REVIEW` instead of `OK` | A manifest's `commit_mode` was `checkpoint` AND Step 3 override didn't apply | Bug in this skill — Step 3 must normalize ALL manifests to `auto` for parallel dispatch |
| MAP mirror step skipped with `map_mirror_skipped` | Brief is missing or has an unparseable MAP link | Non-fatal; canonical store is intact |
| Manifest YAML write-back fails (Step 6) | Permission or path issue | This is the canonical store — fail loudly. Surface error to user and DO NOT continue to Step 7 (mirror) — keeps consistency. |
| Stored `edit_url` 404s when opened | Sub-agent self-reported a `/d/<token>` short link instead of querying Canva (the inline transaction URLs are unreliable) | Re-pull via `mcp__claude_ai_Canva__get-design` on the `design_id` and store the canonical `https://www.canva.com/design/<design_id>/edit`. Step 6's URL guard should now catch this before write — if one still slips through, the guard regex (`/design/<design_id>/edit`) wasn't applied. (Root cause of the 2026-06-10 incident.) |

---

## What this skill does NOT do

- **Upload the headshot to Canva.** v1 takes the asset ID as input. Caller resolves it manually (drag-and-drop in Canva UI, or `mcp__claude_ai_Canva__upload-asset-from-url` if the headshot has a public URL).
- **Clean up bad manifests.** If a manifest has substring-fallback risk (e.g. `"Title"` against a template that doesn't have it), this skill renders it as-is and surfaces warnings. Manifest cleanup is upstream.
- **Update markdown project-plan rows.** Considered for v2 — the project-plan markdown already has an Asset role column, so appending URLs there is a natural mirror, but v1 keeps the loop small: manifests (canonical) + Drive MAP (bonus). Downstream skills should read from manifests directly.
- **Push LinkedIn posts to content-plan.** Separate concern — when the LinkedIn posts are drafted (by `webinar-linkedin-posts`) and the asset URLs are available, a follow-up skill needs to surface them at the weekly content session for slot reservation. Out of scope for this render skill.
- **Verify renders visually.** Per-op success ≠ correct render. Travis (or Furqan) opens each URL to confirm before publishing.

---

## Output

Roll-up to chat (Step 8). Side effects: manifest YAMLs updated with `result:` blocks; Drive MAP cells updated.

---

## Future work

- **v2: headshot upload helper.** Accept either an asset ID OR a public URL — if URL, invoke `mcp__claude_ai_Canva__upload-asset-from-url` first, then proceed.
- **v2: markdown project-plan mirror** (low priority; manifests are canonical).
- **v2: pre-flight manifest validator.** Cross-check each manifest's text_values keys against its template's element-map at runtime; warn on substring-fallback risk before dispatching.
- **Wire to `/schedule`** if webinar cadence becomes regular and we want auto-rendering N weeks before each event.
