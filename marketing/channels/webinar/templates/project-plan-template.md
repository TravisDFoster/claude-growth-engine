# Webinar Project Plan

**Webinar Date:** [YYYY-MM-DD]
**Brief:** `<speaker-slug>.md`
**Collaboration Partner:** [Partner name]

> Dates below use offset notation (`T-Nw` = N weeks before event, `T+N` = N days after). When `webinar-project-init` scaffolds this file, it should replace offsets with absolute `YYYY-MM-DD` dates calculated from the event date.

## Status legend

- `[ ]` Not started
- `[~]` In progress
- `[x]` Completed

---

## Phase 1 — Planning (kickoff to T-6w)

| Status | Task | Owner | Due | Notes |
|---|---|---|---|---|
| [ ] | Review Mutual Action Plan | Cerkl | T-6w | Manual — Google Docs |
| [ ] | Agree on weekly meeting cadence | Joint | T-6w |  |
| [ ] | Finalize webinar topic and objectives | Joint | T-4w | Brief signed off |
| [ ] | Agree on giveaway | Partner | T-3w |  |

## Phase 2 — Content Development (T-4w to T-1w)

| Status | Task | Owner | Due | Notes |
|---|---|---|---|---|
| [ ] | Outline, script, and visuals | Joint | T-1w |  |
| [ ] | Speaker bio + headshot from partner | Partner | T-3w |  |
| [ ] | Create webinar in Zoom | Cerkl | T-3w | Manual; produces base reg URL |
| [ ] | Create tracking URLs in Zoom | Cerkl | T-3w | Use `<speaker-slug>-tracking-urls.md` |
| [ ] | Write registration page copy | Cerkl (Claude) | T-3w | `webinar-registration-page` skill |
| [ ] | Create Canva assets | Cerkl | T-3w | See `canva-asset-checklist.md` |
| [ ] | Build registration page | Cerkl | T-3w | Webflow |

## Phase 3 — Promotion (T-3w to T-1d)

| Status | Task | Owner | Due | Notes |
|---|---|---|---|---|
| [ ] | LinkedIn intro post — Cerkl | Cerkl | T-3w | `webinar-linkedin-posts` |
| [ ] | Pre-event blog post | Cerkl (Claude) | T-3w | `webinar-blog-intro` |
| [ ] | Email Blast #1 — Cerkl | Cerkl | T-10d | `webinar-promo-emails` |
| [ ] | Email Blast #1 — Partner | Partner | T-10d |  |
| [ ] | LinkedIn intro mirror — Partner | Partner | T-10d |  |
| [ ] | Thought-leadership post — Partner | Partner | T-10d |  |
| [ ] | Email #2 — Cerkl | Cerkl | T-3d |  |
| [ ] | Email #2 — Partner | Partner | T-3d |  |
| [ ] | LinkedIn boost — Cerkl | Cerkl | T-2d |  |
| [ ] | LinkedIn boost — Partner | Partner | T-2d |  |
| [ ] | Email #3 last reminder — Cerkl | Cerkl | T-1d |  |
| [ ] | Email #3 last reminder — Partner | Partner | T-1d |  |

## Phase 4 — Webinar (T-3d to T)

| Status | Task | Owner | Due | Notes |
|---|---|---|---|---|
| [ ] | Rehearsal | Joint | T-3d | Monday of event week (or Friday prior if event is Monday) |
| [ ] | Live event + recording | Cerkl | T |  |

## Phase 5 — Follow-up (T+1 to T+7)

| Status | Task | Owner | Due | Notes |
|---|---|---|---|---|
| [ ] | Ingest raw event artifacts into cleaned source-of-truth files | Cerkl (Claude) | T+1 | `webinar-ingest` (run first — every other follow-up skill consumes its output) |
| [ ] | Distribute recording to registrants | Cerkl (Claude) | T+1 | `webinar-followup-email` |
| [ ] | Import registrants to HubSpot | Cerkl | T+1 |  |
| [ ] | Share registrations with speaker | Cerkl | T+1 |  |
| [ ] | Select & notify giveaway winner | Partner | T+5 |  |
| [ ] | Recap clips for YouTube | Cerkl (Claude) | T+7 | `webinar-recap-clips` |
| [ ] | Standalone topic-led blog post for the SEO archive | Cerkl (Claude) | T+10 | `webinar-recap-blog` |
