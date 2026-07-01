# Webinar Project Plan

**Webinar Date:** 2026-07-09 (Thursday)
**Brief:** `rachel-maddy.md`
**Collaboration Partner:** None external — two internal Cerkl presenters: Rachel Folz (Head of Product) & Maddy Rieman (Head of Customer Success)
**Mutual Action Plan:** [Cerkl Webinar Internal MAP — Rachel Folz, June 2026](https://docs.google.com/spreadsheets/d/12-d4oC27mMfr384G01u8PVn8b3n3Fo7Kj2B18aZIDJ0/edit)
**Google Doc Brief:** [Cerkl Webinar Brief — Rachel Folz, June 2026](https://docs.google.com/document/d/1oav1DePRF4jaffRvCB9t8lCRHrc5Y5fAJ4hD5lo_U08/edit)

> Offsets converted to absolute dates from the event date (2026-07-09). **Updated 2026-06-10:** date moved from 2026-06-25 → 2026-07-09 (all rows shifted +14 days) and a second internal presenter (Maddy Rieman) was added. Partner-coordination/amplification rows remain omitted — this is a two-person *internal* webinar with no external partner.

## Status legend

- `[ ]` Not started
- `[~]` In progress
- `[x]` Completed

---

## Phase 1 — Planning (kickoff to 2026-05-28)

| Status | Task | Owner | Due | Notes |
|---|---|---|---|---|
| [ ] | Align with Rachel & Maddy on prep cadence | Joint | 2026-05-28 | Internal sync schedule; both presenters |
| [x] | Finalize webinar topic and objectives | Joint | 2026-06-11 | Title set: "Stop Guessing About Your Analytics: 5 Questions Every Internal Communicator Should Answer" |
| [ ] | Decide on giveaway (optional) | Cerkl | 2026-06-18 | Optional for an internal webinar |

## Phase 2 — Content Development (2026-06-11 to 2026-07-02)

| Status | Task | Owner | Due | Notes |
|---|---|---|---|---|
| [ ] | Outline, script, and visuals | Joint (Rachel + Maddy + Cerkl) | 2026-07-02 | Split speaking roles between Rachel & Maddy |
| [ ] | Speaker bios + headshots — Rachel & Maddy | Cerkl | 2026-06-18 | Headshots already in Canva (`MAFZdaEt2Wc`, `MAFZdS-3JCo`); gather bios |
| [ ] | Create webinar in Zoom | Cerkl | 2026-06-18 | Manual; produces base reg URL |
| [ ] | Create tracking URLs in Zoom | Cerkl | 2026-06-18 | Use `rachel-maddy-tracking-urls.md` |
| [ ] | Write registration page copy | Cerkl (Claude) | 2026-06-18 | `webinar-registration-page` skill |
| [ ] | Create Canva assets | Cerkl | 2026-06-18 | `webinar-canva-render` — 2-speaker pack (re-rendered 2026-06-10) |
| [ ] | Build registration page | Cerkl | 2026-06-18 | Webflow |

## Phase 3 — Promotion (2026-06-18 to 2026-07-08)

Asset role mapping per [`../asset-packs.md`](../asset-packs.md). Channels marked *(optional)* are per-webinar discretionary.

| Status | Task | Owner | Due | Asset role | Notes |
|---|---|---|---|---|---|
| [ ] | LinkedIn intro post — Cerkl | Cerkl | 2026-06-18 | `speaker-card` | `webinar-linkedin-posts` |
| [ ] | Pre-event blog post (Cerkl SEO) | Cerkl (Claude) | 2026-06-18 | `blog-cover` | `webinar-blog-intro` |
| [ ] | ICPro blog promo *(optional)* | Cerkl (Claude) | 2026-06-25 | `blog-cover` | `webinar-blog-intro` adapted for [`icpro-blog`](../../icpro-blog/CLAUDE.md) |
| [ ] | Email Blast #1 — Cerkl | Cerkl | 2026-06-29 | `email-banner` | `webinar-promo-emails` |
| [ ] | Cerklular newsletter inclusion *(optional)* | Cerkl | 2026-06-29 | `email-banner` | Add to next Cerklular send |
| [ ] | Inner Cerkl News announcement *(optional)* | Cerkl | 2026-06-29 | `share-1200x628` | Internal employee channel |
| [ ] | Intercom in-app banner *(optional)* | Cerkl | 2026-06-29 | `share-1200x628` | To existing customers |
| [ ] | Customer-success outreach push *(optional)* | Cerkl | 2026-06-29 | `speaker-card` | CS team forwards to accounts (Maddy's network) |
| [~] | Sales enablement — talk track + asset *(optional)* | Cerkl | 2026-06-29 | `speaker-card` | Hand off to sales for outbound. Copy done: `rachel-maddy-sales-outreach.md` (1:1 email snippet + Marc/Josh links). `speaker-card` Canva asset still pending. |
| [ ] | Email #2 — Cerkl | Cerkl | 2026-07-06 | `email-banner` |  |
| [ ] | LinkedIn boost — Cerkl (countdown) | Cerkl | 2026-07-07 | `countdown` |  |
| [ ] | Email #3 last reminder — Cerkl | Cerkl | 2026-07-08 | `email-banner` |  |

## Phase 4 — Webinar (2026-07-06 to 2026-07-09)

| Status | Task | Owner | Due | Asset role | Notes |
|---|---|---|---|---|---|
| [ ] | Rehearsal | Joint (Rachel + Maddy + Cerkl) | 2026-07-06 | — | Monday of event week |
| [ ] | Set Zoom waiting-room banner | Cerkl | 2026-07-08 | `zoom-banner` | Upload via Zoom webinar settings |
| [ ] | Live event + recording | Cerkl | 2026-07-09 | — |  |

## Phase 5 — Follow-up (2026-07-10 to 2026-07-19)

| Status | Task | Owner | Due | Asset role | Notes |
|---|---|---|---|---|---|
| [ ] | Ingest raw event artifacts into cleaned source-of-truth files | Cerkl (Claude) | 2026-07-10 | — | `webinar-ingest` (run first — every other follow-up skill consumes its output) |
| [ ] | Distribute recording to registrants | Cerkl (Claude) | 2026-07-10 | `recording-thumbnail` | `webinar-followup-email`; thumbnail for on-demand page / YouTube |
| [ ] | Import registrants to HubSpot | Cerkl | 2026-07-10 | — |  |
| [ ] | Share registrations with speakers (Rachel & Maddy) | Cerkl | 2026-07-10 | — |  |
| [ ] | Select & notify giveaway winner (if giveaway used) | Cerkl | 2026-07-14 | — |  |
| [ ] | Recap clips for YouTube | Cerkl (Claude) | 2026-07-16 | — | `webinar-recap-clips` |
| [ ] | Standalone topic-led blog post for the SEO archive | Cerkl (Claude) | 2026-07-19 | `recap-blog-cover` | `webinar-recap-blog` |
