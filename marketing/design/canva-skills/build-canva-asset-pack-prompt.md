# Build prompt — `canva-asset-pack` skill + `linkedin-asset-process.md`

> Paste this into a fresh Claude Code session to fire up the build.

---

Build the `canva-asset-pack` skill and `linkedin-asset-process.md` that uses it, end-to-end. The proven Path B loop, catalog, element map, and curation spreadsheet are all in place — this sprint wires them into a working automation.

**Load first (required, in this order):**
- [`cerkl/PRINCIPLES.md`](/Users/travisfoster/claude-code/cerkl/PRINCIPLES.md) — workspace conventions for routers / skills / processes
- [`cerkl/skills/build-process/SKILL.md`](/Users/travisfoster/claude-code/cerkl/skills/build-process/SKILL.md) — meta-skill for spinning up new processes

**Then load the context for this build:**
- [`cerkl/marketing/design/canva-skills/canva-automation-plan.md`](/Users/travisfoster/claude-code/cerkl/marketing/design/canva-skills/canva-automation-plan.md) — design decisions, gaps, and confirmed catalog-wide constraints. Read this first after the required loads above; everything else descends from it.
- [`cerkl/marketing/design/canva-skills/canva-template-index.md`](/Users/travisfoster/claude-code/cerkl/marketing/design/canva-skills/canva-template-index.md) — 96 brand templates with IDs, aspect, autofill status
- [`cerkl/marketing/design/canva-skills/canva-asset-index.md`](/Users/travisfoster/claude-code/cerkl/marketing/design/canva-skills/canva-asset-index.md) — 162 image assets with stable IDs
- [`cerkl/marketing/design/canva-skills/template-element-map.md`](/Users/travisfoster/claude-code/cerkl/marketing/design/canva-skills/template-element-map.md) — per-template slot shape (text placeholders + image-fill dimensions + layered-frame notes); ~1.7k lines
- [`cerkl/marketing/design/canva-skills/make-template-autofill-ready.md`](/Users/travisfoster/claude-code/cerkl/marketing/design/canva-skills/make-template-autofill-ready.md) — autofill is the *alternative* path; we are **not** using it
- [`cerkl/marketing/design/canva-skills/canva-asset-pack/SKILL.md`](/Users/travisfoster/claude-code/cerkl/marketing/design/canva-skills/canva-asset-pack/SKILL.md) — placeholder stub for the skill you're building
- [`cerkl/marketing/channels/linkedin/linkedin-process.md`](/Users/travisfoster/claude-code/cerkl/marketing/channels/linkedin/linkedin-process.md) — existing LinkedIn copy/drafting process; your sibling
- Curation spreadsheet **"Canva Catalog — Templates & Assets"** in Drive's `Claude-Uploads` folder (Use Case pre-filled column F; `Canonical?` / `Approved for use` columns will be populated by a Furqan/Travis curation pass — may be partial when you start)

**What's already decided (don't re-debate):**
- **Path B (create + programmatic edit)** — the editing-transaction API works on all 96 templates as-is. Autofill requires Canva-side data-field config and 0 templates have it. The 2026-05-29 spike proved the loop end-to-end on the speaker card.
- **Brand assets referenced by existing Canva asset ID** (no uploads — confirmed safe by spike).
- **Sub-agents + Python/Node scripts** for heavy lifting (JSON gen, bulk rename); interactive MCP reserved for one-off spikes.

**The proven loop (Path B):**
`create-design-from-brand-template` → `start-editing-transaction` → resolve slots via element map → `perform-editing-operations` (`replace_text` + `update_fill`) → `commit-editing-transaction` → `export-design`.

**6 catalog-wide constraints to handle** (full detail in `canva-automation-plan.md` → "Confirmed across the catalog"):
1. Layered headshot frames — image swap targets the BG fill, not the foreground decorative card.
2. SHAPE-only headshot circles — must INSERT a fill, not swap.
3. `editable=false` pinned slots — warn + skip fallback.
4. "DELETE place image" text placeholders in the Twitter family.
5. 3 duplicate template-pair groups in FB/LinkedIn share-card family — use canonical only.
6. Multi-page templates need explicit page selection in the manifest.

**Build order:**
1. **Element-map JSON sidecar** — one-time Python script parsing `template-element-map.md` → structured JSON (per-template slot tree). The skill reads JSON, not markdown.
2. **`canva-asset-pack/SKILL.md`** — atomic, channel-agnostic. Manifest input: `template_id`, `page_index`, `text_values` keyed by slot role, `image_assets` keyed by slot role (Canva asset IDs), `export` spec, `commit_mode` (`auto` | `checkpoint`). Output: `{png_path, canva_design_url, design_id, warnings[]}`. Includes a render-verify gate (export + return for review before declaring done). Hardcoded test manifest first → end-to-end on Rachel Folz speaker card (template `EAGqLMN8_Po`, headshot asset `MAFZdaEt2Wc`); success is checkable against the spike export from 2026-05-29 (design `DAHLDiECHrE` in Travis's Canva, titled "[TEST] Path B spike").
3. **Curated-catalog JSON cache** — Python script reading the curation spreadsheet via `gws sheets` → `canonical-templates.json` + `canonical-assets.json`, filtered to `Approved=Y` / `Canonical=Y`. Re-runnable. The LinkedIn process selects from this cache, never the raw 96/162 catalog.
4. **`linkedin-asset-process.md`** — sibling to `linkedin-process.md`. Reads each draft's `## Asset` section, maps post type → template `use_case`, picks a canonical template ID + image asset IDs from the curated cache, builds the manifest, invokes `canva-asset-pack`, drops the Canva design URL into the matching Jira CSV Task description (same shape as `linkedin-process.md` Step 5).
5. **(Parallel — independent of 1–4) Connect-API REST rename/retag script** — sheet → `PATCH /v1/assets/{id}` (name + tags). Separate auth from the MCP. Can run anytime once curation has progress.

**Three open decisions — surface to Travis at the start, do not assume:**
1. Where does the element-map JSON live — single `template-element-map.json` file, or per-template files in `_element-maps/`?
2. Strict curation gate — should `linkedin-asset-process.md` refuse to run on templates not marked `Approved=Y` in the sheet?
3. Commit mode default for LinkedIn — `checkpoint` (Travis reviews each design URL before commit) or `auto` (skill commits, Travis reviews the exported PNG only)?

**Anti-patterns:**
- Do NOT load the full Canva MCP tool descriptions into the running skill — call only the specific tools needed (deferred schemas load via ToolSearch on demand).
- Do NOT upload images — every photo we use already exists in Canva with a stable asset ID.
- Do NOT re-debate autofill vs Path B — Path B is decided.

**Acceptance check:** the skill produces all 9 IC Thought Leadership Series asset shapes for the Rachel Folz solo webinar (2026-06-25) end-to-end.

**Project file:** `cerkl/personal-assistant/projects/canva-asset-pack-build.md` — append a dated log line when each milestone lands (append-only; no update-block ceremony).
