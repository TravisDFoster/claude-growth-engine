---
name: webinar-project-init
description: When the user wants to set up a new webinar project, kick off a webinar, scaffold a new event folder, or start planning a new webinar with a partner. Trigger phrases include "new webinar", "set up a webinar", "kickoff webinar", "start webinar project", "scaffold webinar folder", "create webinar project". Run this AFTER the topic and date have been agreed with the partner.
metadata:
  version: 0.1.0
---

# Webinar Project Init

Scaffold a new webinar event folder with the brief, project plan, and tracking-URLs files. Run this **after** the webinar topic and date have been agreed with the partner — it's the first thing Claude does once those two are locked.

## Inputs to ask for

If any of these are missing, ask before proceeding. Don't guess.

1. **Partner / speaker name** — used to slug the folder (e.g., "Matt Frost" → `matt-frost`)
2. **Event month and year** — used in the folder name (`<speaker-slug>-<month>-<YYYY>`)
3. **Event date** — `YYYY-MM-DD` format
4. **Event time** — including timezone (e.g., "10:00 AM EST")
5. **Webinar topic / working title** (if known — placeholder OK)
6. **Cerkl presenter** (default to Tarek Kamil unless told otherwise)
7. **External partner?** Y/N — drives MAP customization in Step 4a. Y = standard partner co-marketing event; N = internal/solo (Cerkl-only speaker, no partner side). Infer from input #1 + #6 (e.g., speaker is Cerkl staff → N) but confirm if ambiguous.

## Conventions to enforce

- **Folder name**: `<speaker-slug>-<month-name-lowercase>-<YYYY>/` — e.g., `matt-frost-april-2026/`
- **All dates inside files**: `YYYY-MM-DD` (per `cerkl/CLAUDE.md` universal convention)
- **File naming inside the folder**: `<speaker-slug>-<artifact>.md` — matches the existing pattern in [matt-frost-april-2026/](../../matt-frost-april-2026/)

### Speaker slug normalization

- Lowercase
- Strip titles and suffixes (Dr., PhD, Jr., etc.)
- Replace spaces with hyphens
- Drop punctuation (apostrophes, commas, periods)
- ASCII-only — transliterate accented characters (é → e, ñ → n)

Examples:
- "Matt Frost" → `matt-frost`
- "John O'Brien" → `john-obrien`
- "Dr. Jane Smith, PhD" → `jane-smith`
- "Crescenzo Communications" → `crescenzo-communications`
- "François García" → `francois-garcia`

### Rehearsal date computation

Default rehearsal = **Monday of the event week**. Exception: if the event is on Monday, schedule rehearsal for **Friday of the prior week**. Override the `T-3d` offset in the project plan with this computed date.

### Tasks to mark `[x]` (already done) when scaffolding

If the user is running this skill, the following tasks are by definition complete and should be pre-marked done in the project plan:

- "Finalize webinar topic and objectives" (a working title is in the brief)
- Any other task implied by the inputs the user provided

Don't pre-mark tasks that *might* be done — only the ones unambiguously implied by running `webinar-project-init`.

## What to create

In `cerkl/marketing/channels/webinar/<speaker-slug>-<month>-<YYYY>/`:

### 1. `<speaker-slug>.md` — the brief
Copy from [`templates/brief-template.md`](../../templates/brief-template.md). Pre-fill the metadata header:
- **Title** (from input, or leave placeholder)
- **Date** (YYYY-MM-DD)
- **Time**
- **Featuring** ([Cerkl presenter] and [Partner name + role]; for solo/internal, just the speaker)

Then substitute the **"What we need from you" asks block** tokens — the block is pre-populated in the template but with `[BRACKET_TOKENS]` that init must resolve so the Doc is send-ready as soon as it lands in Drive. Substitutions:

| Token | Value |
|---|---|
| `[SPEAKER_FIRST_NAME]` | First name of input #1 (speaker) — used in the greeting |
| `[EVENT_DATE]` | Input #3, human-friendly format (e.g., `June 25` or `2026-06-25`) — used in both heading and Q1 |
| `[EVENT_TIME]` | Input #4 with timezone (e.g., `12:00 PM EDT`) — used in Q1 |
| `[CONTENT_DEV_DATE]` | Event date − 21 days (the T-3w content-dev lock date) — used in the working-deadline line |
| `[WORKING_TITLE]` | Input #5 (working title) or `TBD` if not yet set — used in Q3 |

Leave all other placeholders (in the structured brief sections below the asks block) intact for the `webinar-brief` skill to populate later from the speaker's answers.

### 2. `<speaker-slug>-project-plan.md` — the task list
Copy from [`templates/project-plan-template.md`](../../templates/project-plan-template.md). Then:
- Fill in **Webinar Date** (YYYY-MM-DD)
- Fill in **Brief** reference (`<speaker-slug>.md`)
- Fill in **Collaboration Partner** name
- **Convert all `T-Nw` / `T-Nd` / `T+N` offsets to absolute `YYYY-MM-DD` dates** based on the event date
- Update the `<speaker-slug>` placeholders in skill references and notes

### 3. `<speaker-slug>-tracking-urls.md` — Zoom URL inventory
Copy from [`templates/tracking-urls-template.md`](../../templates/tracking-urls-template.md). Then:
- Fill in **Webinar title** and **Webinar Date**
- Replace `<partner-slug>` with the actual partner slug throughout the partner-side table (internal/solo: drop the partner-side table or note N/A)

URL slots stay empty — the user fills them in after creating each one in the Zoom portal.

### 4. Drive artifacts — MAP + Google Doc brief

Stand up two Drive documents and write their URLs back into the local `.md` files. Every init must produce both.

#### 4a. Copy & customize the Mutual Action Plan

**Source template** (read-only — do not edit): `1cO4KvGdfcQIvnJxQ5orMLoh0GzQ0d78zl2C2nTzhY_c` ("Cerkl Webinar Mutual Action Plan - Template"). Has one `Project Plan` tab matching the markdown plan structure (Category, Task, Priority, Owner, Status, Due Date, Deliverable, Notes).

1. **Copy the template** via Drive API:
   ```bash
   gws drive files copy --params '{"fileId":"1cO4KvGdfcQIvnJxQ5orMLoh0GzQ0d78zl2C2nTzhY_c"}' --json '{"name":"<NAME>"}'
   ```
   Naming, by partner branch (input #7):
   - **Y (external partner):** `Cerkl Webinar Mutual Action Plan — <Speaker>, <Month> <YYYY>`
   - **N (internal/solo):** `Cerkl Webinar Internal MAP — <Speaker>, <Month> <YYYY>`

   Capture the returned `id`. URL: `https://docs.google.com/spreadsheets/d/<id>/edit`

2. **Clear** the Project Plan tab:
   ```bash
   gws sheets spreadsheets values clear --params "{\"spreadsheetId\":\"<id>\",\"range\":\"'Project Plan'!A1:H50\"}"
   ```

3. **Rewrite** the Project Plan tab with `gws sheets spreadsheets values update` (range `'Project Plan'!A1`, `valueInputOption: RAW`). Use the column structure above and the phase structure of [`templates/project-plan-template.md`](../../templates/project-plan-template.md). Apply:
   - **Header rows:** Webinar Date → event date (e.g., `Thu, June 25, 2026`); Collaboration Partner → partner name **(Y)** or `None — internal solo webinar (<Speaker>, Cerkl)` **(N)**.
   - **Due Date column:** convert all `T-Nw` / `T-Nd` / `T+N` offsets to absolute `YYYY-MM-DD` based on the event date (same conversion you applied to `<speaker-slug>-project-plan.md`).
   - **Status column:** pre-mark `Complete` for "Finalize webinar topic and objectives" and "Confirm date, time and platform" (both are by-definition done once init runs).
   - **Internal/solo branch (N):** remove all partner-owned rows (partner Email Blasts, partner LinkedIn posts, partner reminder rows, partner-side blog row); reassign mixed Cerkl/partner rows to Cerkl (bio + headshot, outline collaboration, downloadable asset); remove "Agree on speaker compensation".

   Worked example: the 2026-06-01 update on `personal-assistant/projects/webinars.md` (Rachel Folz webinar) — the JSON body written to `values update` is the structural reference for both branches; the solo branch is what was actually run.

#### 4b. Upload `<speaker-slug>.md` as a Google Doc

Follow [`md-to-drive`](/Users/travisfoster/claude-code/cerkl/skills/md-to-drive/SKILL.md). One file, so run inline (no subagent). Override the default naming because the brief's H1 is the generic "Webinar Brief":

- **Source:** `<event-folder>/<speaker-slug>.md`
- **Destination:** default (Claude-Uploads, folder ID `1L4GEISXbi9sbqOKDCwbFuD1F6MF-JI5g`)
- **Name override:** `Cerkl Webinar Brief — <Speaker>, <Month> <YYYY>`
- **Cleanup:** none

Capture the returned Doc URL: `https://docs.google.com/document/d/<id>/edit`.

#### 4c. Write URLs back into the local `.md` files

Both local files have placeholder lines populated from the templates. Replace:

- In `<speaker-slug>.md` header:
  - `**Mutual Action Plan:** [Drive link — filled in by ...]` → `[<Doc/Sheet display name>](<MAP URL>)`
  - `**Google Doc Brief:** [Drive link — filled in by ...]` → `[<Doc display name>](<Doc URL>)`
- In `<speaker-slug>-project-plan.md` header: same two lines.

### 5. Canva asset manifests — `<event-folder>/canva-manifests/`

Stand up one [`template-fill`](/Users/travisfoster/claude-code/cerkl/marketing/design/canva-skills/template-fill/SKILL.md) manifest per role in the chosen pack from [`../../asset-packs.md`](../../asset-packs.md). The manifests are render-ready skeletons — they pre-fill what's known at init (title, date, time, speaker name, speaker role) and leave the headshot slot as `TBD`. They are not invoked at init; render happens later (Phase 2/3) once the speaker has provided a headshot.

#### 5a. Pack selection

- **Default:** IC Thought Leadership pack (9 templates)
- **Override:** switch to Generic pack (5 templates) only if the user signals non-series styling. Confirm at scaffold if ambiguous.

#### 5b. Generate manifests

Create `<event-folder>/canva-manifests/` and write one YAML per role. Two-step process per role:

**Step 1 — common skeleton.** Start with this template:

```yaml
template_id: <from pack table>
page_index: 1                            # override if pack notes otherwise
design_title: <speaker-slug>-<role>-<event-date YYYY-MM-DD>
text_values:
  "Webinar title": "<input #5 — working title>"
  "Name": ["<input #1 — speaker name>"]
  "Title": ["<input #6 — speaker role; e.g. 'Head of Product, Cerkl'>"]
  "|   Mar 6, 2025 1:00 pm est": "|   <Mon DD>, <YYYY> <h:mm AM/PM ZONE>"
image_assets:
  headshot: ["TBD — gather from speaker; resolve via canva-asset-index"]
commit_mode: checkpoint
```

Use **lowercase** "am/pm" if matching the template's casing convention; **uppercase** zone (e.g., `EDT`, `EST`).

**Step 2 — apply per-role overrides** from [`../../asset-packs.md`](../../asset-packs.md) "Per-role manifest overrides" section. Each role's override block lists `set` / `drop` operations against `text_values` and `image_assets`. Apply them in order before writing the manifest to disk. Examples of why this matters:

- `countdown` → override locks `"X": "2"` (countdown is always the LinkedIn 2-days-to-go boost — no variability), drops vestigial Name/Title/headshot keys, and switches the date placeholder to the no-pipe variant the countdown template actually uses
- `recap-blog-cover` and `recording-thumbnail` → drop the date placeholder (those templates have no date element on page 1)
- Roles with no override block in asset-packs.md use the common skeleton as-is.

The exact placeholder per template lives in `template-fill/_element-maps/<template_id>.json`. Minor variance is handled by the orchestrator's smart matching at render time — see [`webinar-canva-render`](../webinar-canva-render/SKILL.md) Step 4 (live `richtexts[]` exact-match override of template-fill's blind substring fallback).

#### 5c. Write a `canva-manifests/README.md` index

List each role → manifest file → template ID → aspect ratio → promo step it serves (mirror the table in `asset-packs.md`). Include a one-line "to render" instruction.

#### 5d. Render trigger (not run at init)

The manifests are dormant until the speaker provides the headshot. When ready, invoke `template-fill` per manifest. Each returned Canva edit URL gets pasted into:
- The matching row of the Drive MAP (Phase 3 promo row)
- The matching row of `<speaker-slug>-project-plan.md` (Phase 3, asset-role column)

## After scaffolding — surface these reminders to the user

Print a checklist of next manual steps the user must take outside of Claude:

1. **Zoom webinar** — create in the Zoom portal. Then create one tracking registration URL per slug in `<speaker-slug>-tracking-urls.md` and paste them into the file. Reference: [tracking-urls-convention.md](../../tracking-urls-convention.md).
2. **Headshot upload** — get the speaker's headshot uploaded as a Canva asset; capture the asset ID. Until this is done, the `canva-manifests/` are dormant and `template-fill` won't render cleanly.
3. **Canva render** — once headshot is in hand, invoke [`template-fill`](/Users/travisfoster/claude-code/cerkl/marketing/design/canva-skills/template-fill/SKILL.md) per manifest in `canva-manifests/`. Paste returned URLs into the Drive MAP and project-plan rows.

Then list the **next Claude skills to invoke as the project progresses** (do not invoke them now):

- `webinar-brief` — fill out the brief content with the partner
- `webinar-registration-page` — once the brief is ready
- `webinar-promo-emails` — once the registration page is live
- `webinar-linkedin-posts` — paired with promo emails
- `webinar-blog-intro` — pre-event blog
- `webinar-runofshow` — before rehearsal
- `webinar-ingest` — **immediately after the live event**, once raw transcript / chat / deck are saved into `<event-folder>/raw/`. Produces the cleaned source-of-truth files every other post-event skill consumes.
- `webinar-followup-email` — day after the event (reads from the cleaned transcript)
- `webinar-recap-clips` — within a week of the event (reads from the cleaned transcript)
- `webinar-recap-blog` — within ~1–2 weeks; standalone topic-led blog post for the SEO archive (reads from the cleaned transcript + deck extract)

## Push update

After scaffolding, append an update block to the relevant file in `personal-assistant/projects/` per the protocol in [../../CLAUDE.md](../../CLAUDE.md).
