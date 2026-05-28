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
Copy from [`templates/brief-template.md`](../../templates/brief-template.md). Pre-fill:
- **Title** (from input, or leave placeholder)
- **Date** (YYYY-MM-DD)
- **Time**
- **Featuring** ([Cerkl presenter] and [Partner name + role])

Leave all other placeholders intact for the `webinar-brief` skill to populate later.

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
- Replace `<partner-slug>` with the actual partner slug throughout the partner-side table

URL slots stay empty — the user fills them in after creating each one in the Zoom portal.

## After scaffolding — surface these reminders to the user

Print a checklist of next manual steps the user must take outside of Claude:

1. **Mutual Action Plan** — create in Google Docs (manual; not a Claude skill).
2. **Zoom webinar** — create in the Zoom portal. Then create one tracking registration URL per slug in `<speaker-slug>-tracking-urls.md` and paste them into the file. Reference: [tracking-urls-convention.md](../../tracking-urls-convention.md).
3. **Canva assets** — generate via the [`canva-asset-pack`](/Users/travisfoster/claude-code/cerkl/marketing/design/canva-skills/canva-asset-pack/SKILL.md) skill (placeholder until built; until then build manually per [canva-asset-checklist.md](../../canva-asset-checklist.md)). Gather inputs first (logo, headshots).

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
