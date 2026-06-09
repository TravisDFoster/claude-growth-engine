# Skill: Growth Project Tracker (Leadership Review)

Triggered weekly (typically Thursday morning) to regenerate the **evergreen** growth-project-tracker artifact Travis takes into the leadership meeting with Tarek.

Output is **one file, updated in place**: `personal-assistant/growth-project-tracker.md` + sibling `.html`. No dated filenames — the doc's *content* carries the date in the meta header.

Goal: a portfolio-level read of active marketing & growth ops projects — what's shipping, what's at risk, what's on deck — derived from INDEX, git log, and project `## Log` tails. This is a view, not a source.

## Procedure

1. **Gather state** (cheap reads)
   - `INDEX.md` — Top of Mind + Calendar Anchors (already loaded).
   - `git log --since="14 days ago" --pretty=format:'%h %ad %s' --date=short --name-only` from the repo root — the shipped/moved signal.
   - For each file in `projects/` (skip `archive/` and team rollups): read the last ~10 lines for the latest `## Log` entry. The latest entry is that project's current state.

2. **Compute stats** (no fabrication — if a number isn't derivable, omit)
   - Active projects = files in `projects/` (excluding archive/ and rollups).
   - Hard deadlines in next 14 days = Calendar Anchors inside `[today, today+14]`.
   - Blocked / at-risk = projects whose latest log entry says blocked, waiting, or slipped.

3. **Render the markdown** at `personal-assistant/growth-project-tracker.md` (overwrite in place):
   ```
   # Marketing & Growth Ops — Portfolio Review

   > Personal Assistant · Growth Project Tracker
   > **Date:** YYYY-MM-DD (<Day>)
   > **Audience:** Tarek Kamil (CEO) + leadership team
   > **Author:** Travis Foster, Head of Marketing & Growth Ops

   ## TL;DR
   <2–3 sentences synthesizing portfolio state.>

   ## Stats
   - **N** active projects · **N** top of mind · **N** hard deadlines next 14 days · **N** blocked or at-risk (<short list>)

   ## Top of Mind
   <One subsection per INDEX Top-of-Mind item: next step / date / state / why it matters.>

   ## Upcoming Milestones (<today> → <today+30>)
   <Table from Calendar Anchors, next ~30 days.>

   ## Project Ledger
   <Table: Project | Current state (latest log entry, dated) — one row per active project.>

   ## Recently Shipped
   <Flat dated list from git log + log entries, ~last 2 weeks, most recent first.>

   ---

   *Sources: INDEX.md (refreshed YYYY-MM-DD) · git log · project logs*
   ```

4. **Render HTML via sub-agent** — dispatch `md-to-html` (never inline; protects parent context). Brief:
   ```
   Run the md-to-html skill on /Users/travisfoster/claude-code/cerkl/personal-assistant/growth-project-tracker.md.
   artifact_type: dashboard
   theme: dark
   ```

5. **Surface to Travis** — terse confirm: stats line, Top of Mind shifts since last refresh, anything flagged for his call before the meeting.

## Don't

- Don't author new content — this is a view. If a project's state looks wrong, the fix is a log line in the project file, not an edit here.
- Don't load full project files — tails only (latest `## Log` entry).
- Don't load `shared/` or domain context.
- Don't rename or date the output file. Evergreen filename is the point.
- Don't render HTML inline — always dispatch the `md-to-html` sub-agent.

## Edge cases

- **INDEX stale (>5 days):** run `refresh` first.
- **Project with no `## Log` yet (legacy file):** use its most recent git activity as the state line and note it; the log section gets created next time the project is touched.
- **Team rollups (`allison-projects.md`, `furqan-projects.md`):** skip — not projects.
