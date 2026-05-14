# Content Plan — Rolling 4-Week

> **Source of truth for what gets made and when.** Continuously refreshed; the Monday reconcile is where new inputs land. Week 1 is locked + in Jira. Weeks 2–4 are planned but mutable. After a row ships, mark **Status: shipped** — at month close, ship rows get archived into `monthly-content-plans/YYYY-MM-posted.md`.
>
> **Who writes here:** Travis (Monday reconciles). Channels never edit this file. New ideas reach the plan three ways: (a) Travis pulls a queued brief from [`../seo/briefs/`](../seo/briefs/) (the canonical path for SEO content), (b) Travis adds non-SEO items during reconcile (e.g., customer story, product announcement — fast path), or (c) they appear in [`inputs.md`](inputs.md) via the Wednesday team-update (evidence-backed path).
>
> **What channels do:** read their rows here, read the linked SEO brief (if any), execute, report completion back via the PA Push-Update Protocol.

---

## Week 1 — locked (in Jira)

| Deliverable | Channel | Publish | Owner | Status | Source brief |
|---|---|---|---|---|---|

## Week 2 — planned

| Deliverable | Channel | Publish | Owner | Status | Source brief |
|---|---|---|---|---|---|

## Week 3 — planned

| Deliverable | Channel | Publish | Owner | Status | Source brief |
|---|---|---|---|---|---|

## Week 4 — planned

| Deliverable | Channel | Publish | Owner | Status | Source brief |
|---|---|---|---|---|---|

---

## How a row reads (convention, not enforced)

- **Deliverable** — short, scannable. Working title.
- **Channel** — `seo-blog`, `icpro-blog`, `linkedin`, `newsletter`, `comparison-seo`, `case-studies`, `webinar`, `youtube`, `newsroom-pr`, `paid-reddit`, `paid-youtube`, `partnerships`, `design`, `website`.
- **Publish** — `YYYY-MM-DD`.
- **Owner** — name. Channel reads this row; PA's project file tracks status updates.
- **Status** — `planned`, `in-progress`, `shipped`, `pulled`, `blocked`.
- **Source brief** — link to the source:
  - For SEO content (blog post, landing page, versus, refresh): a [`../seo/briefs/<slug>.md`](../seo/briefs/) file. This carries the full schema, keywords, internal linking, and pre-flight checks. The channel reads it verbatim.
  - For non-SEO content (customer story, product launch, partnership, etc.): a one-line pointer to a deep-dive, an `inputs.md` entry, a vault `[[slug]]`, or a customer interview note. This is what the channel reads to understand the *why*.

---

## Monday reconcile — brief lifecycle

Run through these brief-related steps each Monday reconcile:

1. **Pull from the SEO brief queue.** Open [`../seo/briefs/`](../seo/briefs/), find briefs with `status: queued`, decide which ones to schedule.
2. **Schedule.** For each chosen brief, add a row to the appropriate week table in this file. Link the brief in the `Source brief` column. In the brief file's frontmatter: set `status: scheduled` and fill `scheduled_for: YYYY-MM-DD`.
3. **Advance in-flight briefs.** When a channel begins execution, flip the brief's `status: in-progress`. When the channel reports completion (post live in Webflow), flip the brief's `status: shipped` and fill `shipped_date: YYYY-MM-DD`.
4. **Archive.** Move all `status: shipped` briefs from `seo/briefs/` into `seo/briefs/archive/`. Active folder stays a clean queue + scheduled + in-progress view.

Non-SEO rows don't have a brief file to manage — the Source brief link points at the upstream source instead.
