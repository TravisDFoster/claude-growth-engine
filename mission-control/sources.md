# Mission Control — Source Registry

Authoritative list of what the dashboard surfaces. The refresh process reads this file, scans declared folders, extracts any pinned-content snippets, and regenerates `data.json`.

**Convention**: parse filename and folder only — never read source-file contents *except* for declared `extract_from` files (see Pinned section). Date comes from filename prefix (`YYYY-MM-DD-...`), suffix (`...-YYYY-MM-DD.html`), or ISO-week (`YYYY-Www`). Title is the humanized filename.

---

## Pinned

These items are the **always-visible top-of-dashboard panels** — the few documents Travis opens most often, plus the few actions Travis launches most often. Two kinds:

- `kind: artifact` (default) — points at a tangible document. Buttons: `[↗ Open]` (link) + `[⟳ Refresh]` (copy-prompt to update in place).
- `kind: action` — points at no specific artifact. Buttons: `[↗ Plan]` (opens the planning doc context) + `[▶ Run]` (copy-prompt to kick off the work).

Layout: the first pinned item (`growth-project-tracker`) renders **wide** and spans both rows on the left (it carries inline extracted content). The remaining 4 render as a **compact 2×2 grid** on the right.

### growth-project-tracker
- **kind**: artifact
- **layout**: wide
- **label**: Growth Project Tracker
- **url**: `/cerkl/personal-assistant/growth-project-tracker.html`
- **subtitle**: PA — used in Thursday leadership meeting
- **extract_from**: `/Users/travisfoster/claude-code/cerkl/personal-assistant/INDEX.md`
- **extract_section**: `## Top of Mind` (numbered list — extract each `**[Title](link)** — status` row)
- **refresh_prompt**:
  ```
  Regenerate the Growth Project Tracker (leadership review).

  Process: /Users/travisfoster/claude-code/cerkl/personal-assistant/skills/growth-project-tracker.md
  ```
- **cadence**: weekly
- **notes**: Evergreen — one file (`growth-project-tracker.{md,html}`) updated in place each week. The doc's content carries the date in its meta header; the filename never changes.

### weekly-content-session
- **kind**: action
- **label**: Weekly Content Session
- **plan_url**: `/cerkl/marketing/content-plan/weekly-content-process.md`
- **subtitle**: Review → decide → scaffold → produce → import
- **run_prompt**:
  ```
  Run the weekly content session.

  Process: /Users/travisfoster/claude-code/cerkl/marketing/content-plan/weekly-content-process.md
  ```
- **cadence**: weekly

### seo-leadership-status
- **kind**: artifact
- **label**: Cerkl Blog SEO — Leadership Status
- **url**: `/cerkl/marketing/seo/reports/2026-05-15-blog-seo-leadership-status.html` *(latest — auto-pick newest in `reports/` once Travis decides whether this stays dated or goes evergreen)*
- **subtitle**: Blog SEO program health
- **refresh_prompt**:
  ```
  Generate a fresh SEO leadership status report.

  Process: /Users/travisfoster/claude-code/cerkl/marketing/seo/seo-leadership-report-process.md
  ```
- **cadence**: monthly

### blog-writing
- **kind**: action
- **label**: This Week's Blog Posts
- **plan_url**: `/cerkl/marketing/content-plan/weekly-content-process.md`
- **subtitle**: Draft scheduled posts (cerkl.com + ICPro)
- **run_prompt**:
  ```
  Start this week's blog post writing.

  Scheduled briefs are canonical (grep scheduled_for /Users/travisfoster/claude-code/cerkl/marketing/seo/briefs/*.md); the week's Jira CSV in content-plan/jira/imports/ holds the ICPro row.

  Process — cerkl.com (Webflow): /Users/travisfoster/claude-code/cerkl/marketing/channels/seo-blog/seo-blog-process.md
  Process — internalcommspro.com (Wix): /Users/travisfoster/claude-code/cerkl/marketing/channels/icpro-blog/icpro-blog-process.md
  ```
- **cadence**: weekly

---

## Categories

Each category has: `slug`, `label`, `path`, `match`, `home_recent`, `kind` (html/md), optional `new_run` (the prompt for spawning a fresh artifact), and optional `cadence` (daily / weekly / monthly / adhoc — drives the stale indicator).

**Stale thresholds**: daily → >2 days = stale; weekly → >8 days = stale; monthly → >32 days = stale; adhoc → no indicator.

### personal-assistant
- **label**: Personal Assistant
- **path**: `/Users/travisfoster/claude-code/cerkl/personal-assistant/`
- **match**: `*.html`
- **home_recent**: 2
- **cadence**: weekly
- **notes**: Items in this category already drive the Pinned section above; the category-level card stays for archive access.

### marketing-seo
- **label**: Marketing — SEO Reports
- **path**: `/Users/travisfoster/claude-code/cerkl/marketing/seo/reports/`
- **match**: `*.html`
- **home_recent**: 2
- **cadence**: monthly
- **new_run**:
  ```
  Generate a fresh SEO leadership status report.

  Process: /Users/travisfoster/claude-code/cerkl/marketing/seo/seo-leadership-report-process.md
  ```

### marketing-design-one-pagers
- **label**: Marketing — One-Pagers
- **path**: `/Users/travisfoster/claude-code/cerkl/marketing/design/one-pagers/output/`
- **match**: `*.html`
- **home_recent**: 2
- **exclude**: `reference-one-pager.html`
- **cadence**: adhoc
- **new_run**:
  ```
  Build a new one-pager. I'll provide the topic/source when you ask.

  Process: /Users/travisfoster/claude-code/cerkl/marketing/design/one-pagers/one-pager-process.md
  ```

### marketing-paid-youtube
- **label**: Marketing — Paid YouTube Hooks
- **path**: `/Users/travisfoster/claude-code/cerkl/marketing/channels/paid-youtube/`
- **match**: `**/ideas.html`
- **home_recent**: 2
- **cadence**: adhoc
- **new_run**:
  ```
  Generate a new batch of paid YouTube hook ideas.

  Skill: /Users/travisfoster/claude-code/cerkl/marketing/channels/paid-youtube/skills/paid-youtube-hook-batch/SKILL.md
  ```

### ic-trends-daily
- **label**: IC Trends — Daily
- **path**: `/Users/travisfoster/claude-code/cerkl/research/ic-trends/daily/`
- **match**: `*.html`
- **home_recent**: 2
- **cadence**: daily
- **new_run**:
  ```
  Run today's IC Trends daily recap.

  Process: /Users/travisfoster/claude-code/cerkl/research/ic-trends/ic-trends-daily-process.md
  ```

### ic-trends-team-updates
- **label**: IC Trends — Team Updates
- **path**: `/Users/travisfoster/claude-code/cerkl/research/ic-trends/team-update/`
- **match**: `*.html`
- **home_recent**: 2
- **cadence**: weekly
- **new_run**:
  ```
  Run this week's IC Trends team update.

  Process: /Users/travisfoster/claude-code/cerkl/research/ic-trends/team-update-process.md
  ```

### ic-trends-deepdives
- **label**: IC Trends — Deep Dives
- **path**: `/Users/travisfoster/claude-code/cerkl/research/ic-trends/deepdives/`
- **match**: `*.html`
- **home_recent**: 2
- **cadence**: adhoc
- **new_run**:
  ```
  Start a new IC Trends deep dive. I'll provide the source / topic when you ask.

  Process: /Users/travisfoster/claude-code/cerkl/research/ic-trends/ic-trends-deepdive-process.md
  ```

### competitor-marketing-weekly
- **label**: Competitor Marketing — Weekly
- **path**: `/Users/travisfoster/claude-code/cerkl/research/competitor-marketing/weekly/`
- **match**: `*.html`
- **home_recent**: 2
- **cadence**: weekly
- **new_run**:
  ```
  Run this week's competitor marketing weekly recap.

  Process: /Users/travisfoster/claude-code/cerkl/research/competitor-marketing/competitor-marketing-weekly-process.md
  ```

### competitor-marketing-profiles
- **label**: Competitor Marketing — Profiles
- **path**: `/Users/travisfoster/claude-code/cerkl/research/competitor-marketing/Competitors/`
- **match**: `*.html`
- **home_recent**: 2
- **cadence**: adhoc
- **notes**: One-time batch — no `new_run` button.

### sales-reporting
- **label**: Sales — Weekly Pipeline
- **path**: `/Users/travisfoster/claude-code/cerkl/sales/sales-reporting/reports/`
- **match**: `*.html`
- **home_recent**: 2
- **cadence**: weekly
- **new_run**:
  ```
  Run the weekly sales report.

  Process: /Users/travisfoster/claude-code/cerkl/sales/sales-reporting/weekly-sales-report-process.md
  ```
- **notes**: Title override (see process Step 3): `2026-W21` → "Week 21"; range labels like `2026-W19-W22` → "Weeks 19–22". Date is the Monday of the **last (ending)** ISO week in the label, so a 4-week roll-up sorts by the week it covers through (e.g. `2026-W21-W24` dates to W24's Monday, surfacing above single-week reports). `reports/` holds only dated outputs; the locked `reference-weekly-sales-report.html` lives in the parent folder and is never scanned. Family color: `ops` (shared with HubSpot — revenue/ops grouping).

### deal-report
- **label**: Sales — Deal Health
- **path**: `/Users/travisfoster/claude-code/cerkl/sales/deal-report/reports/`
- **match**: `*.html`
- **home_recent**: 1
- **cadence**: adhoc
- **new_run**:
  ```
  Run the deal report.

  Process: /Users/travisfoster/claude-code/cerkl/sales/deal-report/deal-report-process.md
  ```
- **notes**: On-demand companion to the weekly pipeline report — per-deal health drilldown (trajectory/velocity/health bands). Single overwritten `deal-report.html` (no date in filename), so the scan dates it by file mtime; `adhoc` cadence means no stale badge — the tile is primarily a "Run new" launcher + link to the latest run. `reports/` is gitignored (deal-level PII) — Mission Control stores only the file path, never contents, and renders locally, so PII stays local. A `deal-report.pdf` sibling lives in the same folder but `match: *.html` skips it. Family color: `ops`.

> **Note (2026-05-25):** Blog channels (Content Production) and SEO Briefs are now surfaced on the dedicated **[content-dashboard](../content-dashboard/)** — they were removed from this registry to avoid duplication. This dashboard focuses on non-content artifacts (research, audits, IC trends, competitor profiles, leadership reports). The Content Reconcile and This Week's Blog Posts pinned actions remain as quick launchers.

---

## MD-only categories (dimmed until rendered to HTML)

These categories have `.md` outputs but no HTML siblings. They appear on the dashboard at reduced opacity so the gap stays visible without dominating the view. Link to the `.md` file directly.

### hubspot-audits
- **label**: Ops — HubSpot Audits
- **path**: `/Users/travisfoster/claude-code/cerkl/hubspot/reports/`
- **match**: `*.md`
- **home_recent**: 2
- **cadence**: adhoc

### marketing-seo-audits
- **label**: Marketing — SEO Audits
- **path**: `/Users/travisfoster/claude-code/cerkl/marketing/seo/audits/`
- **match**: `*.md`
- **home_recent**: 2
- **cadence**: adhoc

---

## Global excludes

Never include — apply to every category scan:

- `*template*`, `*scaffold*`
- `*-process.md`, `*-process.html`
- `CLAUDE.md`, `CONTEXT.md`, `SKILL.md`, `PRINCIPLES.md`, `README*`
- Anything under `**/skills/**`, `**/wiki/**`, `**/raw/**`

---

## Future work

- HubSpot / SEO audits/briefs → run through [`md-to-html`](../skills/md-to-html/SKILL.md), then move from MD-only to main category list.
- When `growth-project-tracker.html` becomes evergreen (one file), update `pinned.growth-project-tracker.url` and remove the date from `personal-assistant` category items.
- Per-pinned-item *stale* indicator could use `extract_from` file mtime as ground truth rather than referenced HTML mtime.
- `cadence` could be extended to per-day (e.g., "Mon/Wed/Fri") if a 3x-week IC trends rhythm gets adopted.
