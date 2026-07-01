# Webinar Project Plan

**Webinar Date:** [YYYY-MM-DD]
**Brief:** `<speaker-slug>.md`
**Collaboration Partner:** [Partner name, or "None — internal solo webinar (<Speaker>, Cerkl)"]
**Mutual Action Plan:** [Drive link — filled in by `webinar-project-init`, Step 4a]
**Google Doc Brief:** [Drive link — filled in by `webinar-project-init`, Step 4b]

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

Asset role mapping per [`asset-packs.md`](../asset-packs.md). Channels marked *(optional — confirm at scaffold)* are per-webinar discretionary; orchestrator decides yes/no during init.

| Status | Task | Owner | Due | Asset role | Notes |
|---|---|---|---|---|---|
| [ ] | LinkedIn intro post — Cerkl | Cerkl | T-3w | `speaker-card` | `webinar-linkedin-posts` |
| [ ] | Pre-event blog post (Cerkl SEO) | Cerkl (Claude) | T-3w | `blog-cover` | `webinar-blog-intro` |
| [ ] | ICPro blog promo *(optional — confirm at scaffold)* | Cerkl (Claude) | T-2w | `blog-cover` | `webinar-blog-intro` adapted for [`icpro-blog`](../../icpro-blog/CLAUDE.md) |
| [ ] | Email Blast #1 — Cerkl | Cerkl | T-10d | `email-banner` | `webinar-promo-emails` |
| [ ] | Cerklular newsletter inclusion *(optional)* | Cerkl | T-10d | `email-banner` | Add to next Cerklular send |
| [ ] | Inner Cerkl News announcement *(optional)* | Cerkl | T-10d | `share-1200x628` | Internal newsletter / employee channel |
| [ ] | Intercom in-app banner *(optional)* | Cerkl | T-10d | `share-1200x628` | To existing customers |
| [ ] | Customer-success outreach push *(optional)* | Cerkl | T-10d | `speaker-card` | CS team forwards to accounts |
| [ ] | Sales 1:1 outreach snippet — `<speaker-slug>-sales-outreach.md` *(optional)* | Cerkl (Claude) | T-10d | `speaker-card` | `webinar-promo-emails` → "Sales 1:1 outreach snippet" section. Paste-into-thread copy for reps + per-rep tracking links. NOT a HubSpot blast. |
| [ ] | Email Blast #1 — Partner | Partner | T-10d | `email-banner` | Partner-side; N/A for solo/internal |
| [ ] | LinkedIn intro mirror — Partner | Partner | T-10d | — | N/A for solo/internal |
| [ ] | Thought-leadership post — Partner | Partner | T-10d | — | N/A for solo/internal |
| [ ] | Email #2 — Cerkl | Cerkl | T-3d | `email-banner` |  |
| [ ] | Email #2 — Partner | Partner | T-3d | `email-banner` | N/A for solo/internal |
| [ ] | LinkedIn boost — Cerkl (countdown) | Cerkl | T-2d | `countdown` |  |
| [ ] | LinkedIn boost — Partner | Partner | T-2d | — | N/A for solo/internal |
| [ ] | Email #3 last reminder — Cerkl | Cerkl | T-1d | `email-banner` |  |
| [ ] | Email #3 last reminder — Partner | Partner | T-1d | `email-banner` | N/A for solo/internal |

## Phase 4 — Webinar (T-3d to T)

| Status | Task | Owner | Due | Asset role | Notes |
|---|---|---|---|---|---|
| [ ] | Rehearsal | Joint | T-3d | — | Monday of event week (or Friday prior if event is Monday) |
| [ ] | Set Zoom waiting-room banner | Cerkl | T-1d | `zoom-banner` | Upload via Zoom webinar settings |
| [ ] | Live event + recording | Cerkl | T | — |  |

## Phase 5 — Follow-up (T+1 to T+10)

| Status | Task | Owner | Due | Asset role | Notes |
|---|---|---|---|---|---|
| [ ] | Ingest raw event artifacts into cleaned source-of-truth files | Cerkl (Claude) | T+1 | — | `webinar-ingest` (run first — every other follow-up skill consumes its output) |
| [ ] | Distribute recording to registrants | Cerkl (Claude) | T+1 | `recording-thumbnail` | `webinar-followup-email`; thumbnail for on-demand page / YouTube |
| [ ] | Import registrants to HubSpot | Cerkl | T+1 | — |  |
| [ ] | Share registrations with speaker | Cerkl | T+1 | — |  |
| [ ] | Select & notify giveaway winner | Partner | T+5 | — | N/A for solo/internal (Cerkl-owned if giveaway used) |
| [ ] | Recap clips for YouTube | Cerkl (Claude) | T+7 | — | `webinar-recap-clips` |
| [ ] | Standalone topic-led blog post for the SEO archive | Cerkl (Claude) | T+10 | `recap-blog-cover` | `webinar-recap-blog` |
