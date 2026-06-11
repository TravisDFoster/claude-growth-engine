# Mission Control — Refresh Process

> Regenerate `data.json` so `index.html` (and `archive.html`) reflect: current pinned panels, recent activity across every report folder, per-category last-run + stale state. Output: `/Users/travisfoster/claude-code/cerkl/mission-control/data.json`.

Browse at: **http://127.0.0.1:3000/cerkl/mission-control/**

## Trigger

Routes here from `cerkl/CLAUDE.md`:

- "Refresh Mission Control" / "Refresh the dashboard"
- "Update Mission Control" / "Update the dashboard"
- "Let's review Mission Control"
- "Rebuild Mission Control"
- "Sync the dashboard"

## Inputs

None to ask. Reads `sources.md` and scans the folders it declares.

## Context to load

- [/Users/travisfoster/claude-code/cerkl/mission-control/sources.md](sources.md) — pinned-item declarations + category registry

## Steps

### Step 1 — Read the registry
- **Owner:** Claude
- **Needs:** [`sources.md`](sources.md)
- **Produces:** in-memory list of (a) Pinned items, (b) Categories (HTML, blog, MD-only)
- Parse four sections of `sources.md`: `## Pinned`, `## Categories`, `## Content Production`, `## MD-only categories`. Each `###` heading is one item.

**Pinned `kind`s:**
- `kind: artifact` → has `url` (the document) + `refresh_prompt`. UI buttons: `[↗ Open]` + `[⟳ Refresh]`. Optionally `extract_from` + `extract_section` for inline content.
- `kind: action` → has `plan_url` (context document) + `run_prompt`. UI buttons: `[↗ Plan]` + `[▶ Run]`. No inline content extraction.

The first pinned item with `layout: wide` spans the full left column. All other pinned items render compact in a 2×2 sub-grid on the right.

**Category `kind`s:**
- `kind: html` → primary categories. Render in Launch zone.
- `kind: blog` → blog channels with high-volume `.md` working copies. Render in Content Production zone (NOT dimmed). Title parsing strips `YYYY-MM-DD_` prefix and `_state` suffix; only include `*_live.md` files.
- `kind: md` → MD-only audits/briefs awaiting HTML rendering. Render dimmed in MD-only zone.

### Step 2 — Scan each category folder
- **Owner:** Claude
- **Needs:** Bash `find` (or equivalent)
- **What to do:** For each category, run `find <path> -name '<match>' -type f`. Apply local `exclude` list, then global excludes. Don't read file contents.

Example:
```bash
find /Users/travisfoster/claude-code/cerkl/research/ic-trends/daily/ -maxdepth 1 -name '*.html' -type f
```

### Step 3 — Parse metadata from each filename
- **Owner:** Claude
- For each file, derive:
  - **date**: filename prefix `YYYY-MM-DD-` OR suffix `-YYYY-MM-DD.ext` OR ISO week `YYYY-Www` (convert to Monday of that week) OR file mtime (`stat -f %Sm -t %Y-%m-%d <file>`) if no date in name.
  - **title**: strip date token, replace `-`/`_` with space, title-case. Category overrides:
    - `ic-trends-daily`: `"Daily Recap — {date}"`
    - `ic-trends-team-updates`: `"Team Update — {date}"`
    - `competitor-marketing-weekly`: `"Week {NN}"` from `YYYY-Www`
    - `competitor-marketing-profiles`: company name (strip trailing date)
    - `sales-reporting`: `"Week {NN}"` from a single `YYYY-Www`; `"Weeks {NN}–{MM}"` from a `YYYY-Www-Wmm` range. Date = Monday of the **last (ending)** ISO week in the label — a multi-week roll-up sorts by the week it covers *through*, not where it starts, so the newest roll-up surfaces on top.
    - `ic-trends-deepdives`: `"{Source} — {Topic}"` when filename starts with a known source token (`forrester`, `gartner`, `mckinsey`, `ragan`, `oracle`, `workshop`, `prdaily`, `hr-reporter`); otherwise default humanization
  - **url**: file path with `/Users/travisfoster/claude-code` stripped → server-relative path
  - **is_md**: ext is `.md`

### Step 4 — Sort each category newest-first

### Step 5 — Compute last-run + staleness per category
For each category with a `cadence` field:
- **last_run** = newest item's date (or `null` if empty)
- **days_since** = today − last_run
- **stale** = `true` if cadence is `daily` and days_since > 2, or `weekly` and > 8, or `monthly` and > 32. Cadence `adhoc` → `stale: false` always.

### Step 6 — Resolve pinned URLs
For each `## Pinned` item:
- If `url` looks dated (matches `*-YYYY-MM-DD.html`) and a newer dated sibling exists in the same folder, prefer the newer one. (Keeps `seo-leadership-status` pointed at the latest even before it goes evergreen.)
- Compute **last_updated** from the file's mtime (`stat -f %Sm -t %Y-%m-%d <file>`). This is what the stale badge keys off for pinned items.

### Step 7 — Extract pinned content (when `extract_from` is declared)
For each pinned item with `extract_from` + `extract_section`:
- Read the source `.md` file.
- Locate the named section heading (e.g., `## Top of Mind`).
- Capture lines until the next `## ` heading or `---`.
- For numbered-list sections like INDEX's Top of Mind, parse each row:
  - **title**: text inside `**[...](...)**`
  - **summary**: text after the first `—` (em-dash), trimmed to the first sentence (cap at ~140 chars; ellipsis if cut)
- Store as `pinned[].content.items[]` in `data.json`. If a section has no extractable rows, set `content: null`.

### Step 8 — Compute totals + global recent
- `total_html` = sum across `kind: html` categories
- `total_blog_posts` = sum across `kind: blog` categories
- `total_md_candidates` = sum across `kind: md` categories
- `generated_at` = today's date (`YYYY-MM-DD`)
- `recent[]` = top 5 items across ALL `kind: html` categories, sorted by date desc (for the compact Recent strip — blog posts have their own zone)

### Step 9 — Write `data.json`
- Path: [`/Users/travisfoster/claude-code/cerkl/mission-control/data.json`](data.json)
- Preserve the shape `index.html` expects. Schema reference at the bottom of this file.

### Step 10 — Summarize in chat
- New items per category since prior refresh
- Categories that newly went stale (or freshly recovered)
- Pinned items whose extracted content changed materially
- Folders that returned zero matches (smell — something moved)

One paragraph; no file dump.

## Output

- `cerkl/mission-control/data.json` — overwritten in place
- Chat summary of what changed

## How to add a new category

1. Add a `###` section under `## Categories` in [`sources.md`](sources.md) with `label`, `path`, `match`, `home_recent`, `kind`, and optional `cadence` + `new_run`.
2. Run a refresh.

## How to pin a new item

1. Add a `###` section under `## Pinned` with `label`, `url`, `subtitle`, `refresh_prompt`, and optional `extract_from` + `extract_section` + `cadence`.
2. Run a refresh.
3. Pinned cards render in registry order — reorder by moving the section.

## How to promote an MD-only category to HTML

When MD items get HTML siblings via [`md-to-html`](../skills/md-to-html/SKILL.md):

1. Move the category from `## MD-only categories` to `## Categories`.
2. Change `kind: md` → `html` and `match: *.md` → `*.html`.
3. Refresh.

## `data.json` schema

```jsonc
{
  "generated_at": "YYYY-MM-DD",
  "total_html": <int>,
  "total_md_candidates": <int>,
  "pinned": [
    {
      "slug": "growth-project-tracker",
      "label": "Growth Project Tracker",
      "subtitle": "PA — used in Thursday leadership meeting",
      "url": "/cerkl/personal-assistant/...html",
      "last_updated": "YYYY-MM-DD",
      "cadence": "weekly",
      "stale": false,
      "refresh_prompt": "...",
      "content": {                     // optional — only if extract_from declared
        "section": "Top of Mind",
        "items": [
          { "title": "SEM Landing Page Rebuild", "summary": "Launch Wed 2026-05-20 at 2:30..." }
        ]
      }
    }
  ],
  "categories": [
    {
      "slug": "ic-trends-daily",
      "label": "IC Trends — Daily",
      "kind": "html",
      "home_recent": 2,
      "cadence": "daily",
      "last_run": "YYYY-MM-DD",
      "stale": false,
      "new_run_prompt": "...",          // optional
      "items": [
        { "title": "...", "date": "YYYY-MM-DD", "url": "/cerkl/...", "is_md": false }
      ]
    }
  ],
  "recent": [
    { "title": "...", "date": "...", "url": "...", "cat_label": "...", "cat_slug": "...", "is_md": false }
  ]
}
```

## Future work

- **Diff against previous run** — persist `data.previous.json` for a real "what's new" Step 10 summary.
- **md-to-html sweep** — render the MD-only audits/briefs.
- **Per-pinned content type** — `extract_section` currently assumes numbered list. Could expand to "first table row" or "first H3 block".
- **Schedule** — wire to `/schedule` if a daily/weekly auto-refresh cadence stabilizes.

## Learnings

(Append as the process matures: what broke, what we changed, why.)
