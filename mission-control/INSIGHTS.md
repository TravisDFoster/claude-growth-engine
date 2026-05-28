# Build a Claude Dashboard — Insights & One-Shot Guide

> Drop this file into a fresh Claude Code session along with your workspace and a one-line ask ("Build me a Claude Dashboard"). Claude should be able to ship a working dashboard end-to-end, asking only the questions it can't answer from the workspace itself.

---

## What this is

A **local-only, browser-based launcher and index** for the reports, audits, recaps, deep-dives, and other artifacts Claude produces inside a workspace. It serves two roles:

1. **Index** — see every artifact at a glance, browse archives by category
2. **Launcher** — one-click copy-to-clipboard prompts that spin up new artifacts or refresh existing ones

The dashboard is dark-themed by default, served via a local HTTP server (so JSON `fetch()` works), and built from three layers:

- A **routing entry** in the workspace's top CLAUDE.md
- A **registry** (`sources.md`) declaring what to surface
- A **regenerated data file** (`data.json`) that two **static HTML templates** read

Nothing dynamic — no backend, no database. The "refresh" is Claude re-scanning folders and rewriting `data.json`.

## The 5 insights that make it work

### 1. Active launcher > passive index

The instinct is to build a list of links. The real value shows up when each link is paired with **the prompt to refresh / regenerate it**. The dashboard becomes the front door to running processes, not just discovering past outputs. Every category card has a **`+ Run new`** button; every pinned doc has a **`⟳ Refresh`** button. Each copies a self-contained, paste-ready prompt with **absolute file paths** so it works from any directory.

### 2. Two artifact types need different UI

| Type | Examples | UI |
|---|---|---|
| **Evergreen** (one file, updated in place) | Active task ledger, current-week plan, live KPI snapshot | **Pin** at top — show last-updated, optionally extract inline content |
| **Dated** (new file each run) | Daily recaps, weekly summaries, point-in-time deep-dives | **Category cards + archive** — show recent N, link to "see all" |

This split is the structural unlock. A pinned panel showing "today's open tasks" inline is dramatically more useful than a link to a file you have to click into. A dated archive of 30 deep-dives is best as a per-category archive page, not a flat list.

### 3. Parse filenames; don't read contents

The refresh process **never reads source file contents** (except for declared `extract_from` files). It parses filenames and folder paths. Title comes from humanizing the filename; date comes from the prefix (`YYYY-MM-DD-…`), suffix (`…-YYYY-MM-DD.html`), ISO week (`YYYY-Www`), or file mtime. This keeps the refresh fast and token-cheap even with hundreds of artifacts.

Per-category title-parsing overrides go in `sources.md` (e.g., "deep-dives use a date suffix, not prefix"). New convention = new note, not new code.

### 4. The registry is the only thing humans edit

`sources.md` is the source of truth. The HTML and JSON are outputs. Process file is the recipe. Three roles:

- **Edit** when adding categories, pinning new docs, or changing conventions → `sources.md`
- **Run** to update what's shown → the refresh process (writes `data.json`)
- **Open** to view → the HTML files (read `data.json`)

This is the loose-coupling pattern: small, declarative registry; static views; deterministic regeneration.

### 5. Skip iframes — extract to data.json

The temptation is to embed the leadership review HTML in an iframe for inline preview. **Don't.** Instead, declare `extract_from: path/to/source.md` + `extract_section: "## Top of Mind"` in the registry, and have the refresh process pull the section into `data.json`. The HTML renders the extracted text natively. Faster, no cross-origin gymnastics, no needing to add anchors to source files.

---

## Architecture

```
{WORKSPACE_ROOT}/
├── CLAUDE.md                              ← gains 1 routing row
└── claude-dashboard/                      ← new folder
    ├── claude-dashboard-process.md        ← the refresh orchestrator
    ├── sources.md                         ← category registry (only file humans edit)
    ├── data.json                          ← regenerated each refresh
    ├── index.html                         ← home / launcher
    └── archive.html                       ← per-category archive (?category=<slug>)
```

The dashboard URL ends up at `http://<HOST>:<PORT>/<PATH_FROM_SERVER_ROOT>/claude-dashboard/`. The server root may not equal the workspace root — verify before generating URLs.

---

## Build sequence

### Phase 1 — Scope (ask the user)

Before scaffolding, ask:

1. **Workspace root** — `pwd` from inside it, or paste the absolute path.
2. **Local HTTP server** — Is one running? What URL is the server root mapped to? (`python3 -m http.server 3000`, `serve .`, etc.) If not, recommend one — the dashboard requires HTTP (not `file://`) for `fetch('data.json')` to work.
3. **Style reference** — Is there a brand guide, color tokens file, or an existing HTML report whose look you want to match? If yes, point to it. If no, the dashboard defaults to a dark Cosmic/Cobalt-style palette with Work Sans font.
4. **Initial pinned docs** — Which 2–4 files are "always-current and most-opened"? (Leadership review / live task ledger / current-week plan / KPI snapshot.) Default to 3 cards.
5. **Refresh cadence per source folder** — Is each folder updated daily, weekly, monthly, or ad-hoc? Drives the stale-indicator threshold.

If any answer is "not sure," propose defaults and move on. The registry is editable — wrong defaults are cheap to fix.

### Phase 2 — Inventory (deploy a subagent)

Spawn an `Explore`-style subagent to walk the workspace and find candidates. **Brief it with this prompt** (substituting the workspace root):

```
Inventory every "publishable output" under {WORKSPACE_ROOT}. Walk every
subdirectory — don't trust routing tables to be exhaustive. Search by
file pattern, not just folder convention.

Find:
1. Every .html file that's a publishable view (reports, audits, recaps,
   deep-dives, status docs, indexes, briefings, summaries).
2. Every .md file that looks like a report/audit/recap but has NO .html
   sibling — flag these separately as candidates for future rendering.

Exclude:
- SKILL.md, CLAUDE.md, CONTEXT.md, PRINCIPLES.md, README*
- Process orchestrators (*-process.md / *-process.html)
- Templates, scaffolds, partials, source/input docs
- Anything under skills/, wiki/, raw/, drafts/
- CSS files, HTML fragments, <head> partials

Heuristics for "publishable output":
- Lives in a reports/, audits/, recaps/, deep-dives/ folder
- Filename has a YYYY-MM-DD prefix or suffix
- Filename contains: report, audit, recap, status, deepdive, deep-dive,
  index, summary, briefing, digest

Do NOT read file contents — parse filename and path only.

Return format: two markdown sections grouped by parent folder.
  ## Existing HTML outputs (ready to dashboard)
  ### <domain>
  - `<absolute path>` | <inferred title> | <inferred date>
  ## MD-only candidates (no HTML sibling — flag for future rendering)
  ### <domain>
  - ...
End with: "Total: N HTML, M MD-only candidates."
```

When the inventory comes back, **review with the user**:
- Flag edge cases (templates that snuck in, draft folders, wiki entries)
- Identify the **categories** (groupings that share a folder + naming convention)
- Identify which categories have an **automated process file** that could be triggered with a "+ Run" button (search for `*-process.md` in each domain or check the routing CLAUDE.md)

### Phase 3 — Handle the "no HTML files" case

If the inventory turns up few or zero `.html` files, the workspace hasn't been HTML-rendering its outputs yet. Recommend:

1. **Identify the highest-value MD outputs** that get reread / reshared (typically: leadership reports, weekly recaps, deep-dives, audits).
2. **Look for an existing MD→HTML skill** in the workspace (search for `md-to-html`, `render-html`, or similar). If one exists, that's the route.
3. **If no such skill exists, recommend creating one** with a brand-aligned reference template, or point at a simple inline-CSS HTML wrapper. The `md-to-html` skill in this repo at `{WORKSPACE_ROOT}/skills/md-to-html/SKILL.md` (if present) is a strong reference.
4. **Pilot first**: render one high-value MD to HTML, confirm the look, then back-fill the rest. Don't bulk-render before the style is locked.
5. **Wire the existing process files** that produce those MDs to call the HTML-rendering skill at the end. Each process file gets a final step: "render the output to HTML at the sibling path."

The dashboard can still be built immediately — MD-only items just get a dimmed "Needs HTML rendering" zone until the gap closes.

### Phase 4 — Style setup

Two paths:

**(A) The workspace has a style reference** (brand guidelines, an existing report HTML, a CSS token file)
- Read the reference. Extract: font family, color palette (background, surface, ink, accent, semantic good/warn/bad), border radii, type scale, dark vs light default.
- Use those tokens directly in the dashboard's `:root { … }` CSS variables.
- Match the component vocabulary if the reference defines one (e.g., the Cerkl reference uses `.hero`, `.brief-chip`, `.strat-card`, `.gauge-status` — the dashboard reuses these mental models even though its components are different).

**(B) No reference exists** — ask the user three questions, then default:
1. Dark or light theme? **(default: dark)**
2. Any preferred accent color or palette name? **(default: cobalt / muted blue)**
3. Font preference — system stack, Inter, Work Sans, other? **(default: Work Sans via Google Fonts with system fallback)**

Brand-color shortcuts if the user only gives a vibe:
- "Calm / corporate" → Cobalt blue (`#3547c4`) on Cosmic dark (`#18181d`)
- "Energetic" → Warm orange (`#ff9457`) or amber on dark
- "Tech-forward / sleek" → Cyan-teal (`#5eead4`) on near-black
- "Trustworthy / data-y" → Forest green (`#1a9979`) on slate

### Phase 5 — Build the registry (`sources.md`)

Three sections — see [Schema reference](#sourcesmd-schema) for full field list.

### Phase 6 — Generate initial `data.json`

Walk the categories declared in `sources.md`. For each, scan files, parse filenames, sort by date, compute `last_run` and `stale`. For each pinned item, resolve URL and extract content if declared. Write `data.json`.

This is the same recipe documented in `claude-dashboard-process.md` Steps 1–9 — the initial build runs the refresh process once with empty inputs.

### Phase 7 — Build the HTML templates

Two files: `index.html` (launcher) and `archive.html` (per-category). Both self-contained — inline CSS + JS. Both `fetch('data.json')` and render. See [HTML component reference](#html-component-reference).

### Phase 8 — Wire routing

Add a row to the workspace top-level `CLAUDE.md`:

```markdown
| Refresh / update / review the claude dashboard | [`claude-dashboard/claude-dashboard-process.md`](claude-dashboard/claude-dashboard-process.md) |
```

And a folder-tree entry:

```markdown
└── claude-dashboard/   ← local browser index of reports/audits/recaps
```

### Phase 9 — Smoke test

```bash
# Server returns 200 for all three URLs
curl -s -o /dev/null -w "%{http_code}\n" http://{HOST}:{PORT}/{PATH}/claude-dashboard/index.html
curl -s -o /dev/null -w "%{http_code}\n" http://{HOST}:{PORT}/{PATH}/claude-dashboard/data.json
curl -s -o /dev/null -w "%{http_code}\n" "http://{HOST}:{PORT}/{PATH}/claude-dashboard/archive.html?category=<one-slug>"

# Every URL in data.json resolves to a real file
python3 -c "
import json, os
d = json.load(open('claude-dashboard/data.json'))
missing = [it['url'] for c in d['categories'] for it in c['items']
           if not os.path.exists('{WORKSPACE_ROOT}/..' + it['url'])]
print(f'{len(missing)} missing')
"

# Staleness math matches a per-category audit (eyeball with declared cadence)
```

Then **open in browser** and verify:
- All zones render
- Copy buttons fire toast on click and put text on clipboard
- Pinned content (if extracted) shows correctly
- Archive page loads with `?category=<slug>` for each category

---

## Subagent dispatch patterns

Use subagents when the work is **read-heavy** and the results return as a structured summary. Keeps tokens out of the parent context.

| Use case | Agent type | Brief includes |
|---|---|---|
| **Inventory scan** (Phase 2) | `Explore` / read-only | The full Phase-2 prompt above |
| **Style reference extraction** | `Explore` | "Read these N files. Return: color tokens, font stack, type scale, border radii, component class names." |
| **Process file enumeration** (find `*-process.md` per category) | `Explore` | "Walk each `category.path`. Look for a sibling `*-process.md`. Return: category slug → process file path (or 'none')." |
| **Routing audit** (verify CLAUDE.md row added correctly) | inline (no subagent) | — |

**Always**: give the subagent **absolute paths**, an **output schema**, and a **length cap**. Don't trust it to inherit context.

---

## `sources.md` schema

Three top-level sections.

### `## Pinned`

Always-visible cards at the top of the dashboard. Each `###` heading is one item.

```markdown
### <slug>
- **label**: Display title
- **url**: /server-relative/path/to/file.html
- **subtitle**: One-line context (optional)
- **extract_from**: /absolute/path/to/source.md      (optional; for inline content)
- **extract_section**: "## Heading to extract"        (optional)
- **refresh_prompt**: |
    Multi-line paste-ready prompt.
    Process: /absolute/path/to/process.md
- **cadence**: daily | weekly | monthly | adhoc
- **notes**: Free-form context (optional)
```

### `## Categories`

The browseable archive — each category becomes a card + archive page.

```markdown
### <slug>
- **label**: Display label
- **path**: /absolute/path/to/folder/
- **match**: *.html       (or **/ideas.html, etc.)
- **home_recent**: 2       (how many to show on home before "see all")
- **kind**: html | md
- **cadence**: daily | weekly | monthly | adhoc
- **exclude**: filename-or-glob.html   (optional, per-category)
- **new_run**: |                       (optional — drives the +Run button)
    Multi-line paste-ready prompt.
    Process: /absolute/path/to/process.md
- **notes**: any parsing edge cases (date suffix instead of prefix, etc.)
```

### `## MD-only categories`

Same shape as Categories but `kind: md`. Rendered at reduced opacity in a separate "Needs rendering" zone.

### `## Global excludes`

Filename patterns to skip across all scans (templates, README, CLAUDE.md, etc.).

---

## `data.json` schema

```jsonc
{
  "generated_at": "YYYY-MM-DD",
  "total_html": <int>,
  "total_md_candidates": <int>,
  "pinned": [
    {
      "slug": "...",
      "label": "...",
      "subtitle": "...",
      "url": "/server-relative/path",
      "last_updated": "YYYY-MM-DD",
      "cadence": "weekly",
      "stale": false,
      "refresh_prompt": "...",
      "content": {              // optional, only if extract_from declared
        "section": "Top of Mind",
        "items": [{ "title": "...", "summary": "..." }]
      }
    }
  ],
  "categories": [
    {
      "slug": "...",
      "label": "...",
      "kind": "html",
      "home_recent": 2,
      "cadence": "daily",
      "last_run": "YYYY-MM-DD",
      "stale": false,
      "new_run_prompt": "...",   // optional
      "items": [
        { "title": "...", "date": "YYYY-MM-DD", "url": "...", "is_md": false }
      ]
    }
  ],
  "recent": [                    // top N across all categories
    { "title": "...", "date": "...", "url": "...", "cat_label": "...", "cat_slug": "...", "is_md": false }
  ]
}
```

**Stale thresholds**: `daily` → >2 days; `weekly` → >8 days; `monthly` → >32 days; `adhoc` → never stale.

---

## HTML component reference

`index.html` zones, in order:

1. **Slim sticky topbar** — workspace name + breadcrumb + `Last refreshed` pill + [⟳ Refresh dashboard] button (copies the dashboard refresh prompt). No big hero — this is an app, not a report.
2. **Pinned grid** — 2:1:1 column ratio (one wide card for the high-value pinned item that has inline extracted content; two compact cards for the rest). Each card: eyebrow ("Pinned" + freshness pill) → title → subtitle → (optional inline content list) → footer with [↗ Open] [⟳ Refresh] buttons.
3. **Launch grid** — 4-column responsive (3 / 2 / 1 at breakpoints). Each card: title + freshness pill → meta row (count + latest date) → recent items list → footer with [+ Run new] (if `new_run_prompt` exists) and "See all →" link.
4. **Recent activity strip** — 5 dense chips in a horizontal grid, color-accented left border. Lower visual weight than Launch.
5. **Needs HTML rendering zone** — MD-only cards at ~60% opacity, separated from main grid so they're visible but not loud.
6. **Toast** — fixed bottom-right, fires on copy. 1.8s.
7. **Footer** — file references and an "Open archive" link.

Container: `max-width: 1320px`, padding 32px sides. Breakpoints at 1180 / 1100 / 980 / 880 / 560.

`archive.html` is much simpler: hero (breadcrumb + category label + meta), full list of items in the category (date | title), "Other categories" tag-cloud below.

**Print stylesheet on both pages** — ink-on-white, buttons hidden — so they export cleanly via headless Chrome if needed.

### Copy-button mechanic

Every button with a `data-copy-prompt="<key>"` attribute is wired through event delegation:

```javascript
const promptMap = {
  'refresh-dashboard': "Refresh my claude dashboard.\n\nProcess: /abs/path/process.md",
  'pinned:<slug>': "<that pinned item's refresh_prompt>",
  'category:<slug>': "<that category's new_run_prompt>"
};
document.body.addEventListener('click', async (ev) => {
  const btn = ev.target.closest('[data-copy-prompt]');
  if (!btn) return;
  ev.preventDefault();
  const text = promptMap[btn.getAttribute('data-copy-prompt')];
  await navigator.clipboard.writeText(text);
  showToast('Copied! Paste into Claude.');
});
```

Fallback to `document.execCommand('copy')` via a hidden textarea for non-secure contexts.

### Freshness pill logic

```javascript
function freshnessBadge(cadence, dateStr, isStale) {
  const days = daysSince(dateStr);
  if (cadence === 'adhoc' || !cadence) {
    return `<span class="freshness adhoc">ad-hoc · ${days}d ago</span>`;
  }
  const cls = isStale ? 'stale' : '';
  const label = days === 0 ? 'today' : (days === 1 ? '1d ago' : `${days}d ago`);
  return `<span class="freshness ${cls}">${cadence} · ${label}${isStale ? ' · stale' : ''}</span>`;
}
```

Stale = butter/amber pill. Fresh = forest/green pill. Ad-hoc = neutral grey pill.

---

## The refresh process — 10 steps

The orchestrator file (`claude-dashboard-process.md`) documents these. Claude runs them when the user types a trigger phrase routed via CLAUDE.md.

1. **Read the registry** — parse `## Pinned`, `## Categories`, `## MD-only categories` from `sources.md`
2. **Scan each category folder** — `find <path> -name <match> -type f`, minus local excludes, minus global excludes
3. **Parse metadata from each filename** — date from prefix/suffix/ISO-week/mtime; title from humanized filename + category overrides; URL from path-minus-workspace-root; `is_md` from extension
4. **Sort each category newest-first**
5. **Compute last-run + staleness per category** — `last_run` = newest item's date; `stale` per cadence threshold
6. **Resolve pinned URLs** — if dated, pick newest; compute `last_updated` from file mtime
7. **Extract pinned content** — for each `extract_from` + `extract_section`, read the source MD, slice the named section, parse list rows into `{title, summary}`
8. **Compute totals + global recent** — totals across categories; top-5 recent across all
9. **Write `data.json`** — overwrite in place
10. **Summarize in chat** — what's new, what went stale, what folders returned zero

---

## Routing CLAUDE.md row

Trigger phrases the dashboard should accept:

| Phrase | Routes to |
|---|---|
| "Refresh my claude dashboard" / "Refresh the claude dashboard" | the process file |
| "Update my claude dashboard" / "Update the claude dashboard" | same |
| "Sync the dashboard" / "Rebuild the claude dashboard" | same |
| "Review the claude dashboard project" | same |

The router row:

```markdown
| Refresh / update / review the claude dashboard, sync / rebuild the dashboard | [`claude-dashboard/claude-dashboard-process.md`](claude-dashboard/claude-dashboard-process.md) |
```

---

## Common pitfalls

- **Server root ≠ workspace root.** If the HTTP server serves `~/code/` and the workspace is `~/code/myproject/`, the dashboard URL is `127.0.0.1:3000/myproject/claude-dashboard/`. URLs in `data.json` must be server-relative — generate them by stripping the **server root**, not the workspace root.
- **`fetch()` fails on `file://`.** The dashboard requires HTTP. If the user opens `index.html` directly via filesystem, JSON loading errors. The error block in the HTML calls this out explicitly.
- **Adding a Run button for a category with no automated process.** Don't. Empty buttons hurt trust. Skip `new_run_prompt` if no process file exists.
- **Reading file contents during refresh.** Defeats the speed advantage. Only `extract_from` files (explicitly declared) get read.
- **Schema bloat in `sources.md`.** New fields should be optional and convention-first. If you need a non-default for one item, add a field. If you need it for half of items, you've drifted — reconsider the default.
- **One category per file convention.** If two folders have radically different naming, they're two categories, not one with overrides. Category overrides should be small adjustments (date prefix vs suffix), not branching logic.
- **Forgetting print stylesheet.** Even if no one prints, you'll want it the moment you try Chrome-headless → PDF.
- **Stale logic on `adhoc` cadence.** Adhoc never goes stale by definition — show a neutral pill, not a green one.
- **Iframe-embedding pinned content.** Costs more than it saves (cross-origin, scrollbars, height calc). Extract to JSON instead.

---

## First-shot prompt template

For someone with this file and a workspace, the kickoff message to Claude:

```
Build me a Claude Dashboard for this workspace using the build guide at
{ABSOLUTE_PATH_TO_THIS_INSIGHTS_FILE}.

Workspace root: {ABSOLUTE_PATH}
Local HTTP server: http://127.0.0.1:{PORT}/ (serves from {SERVER_ROOT})

[Optional context — fill in if you know:]
- Style reference: {path or "no preference, use defaults"}
- Pinned candidates: {list 2-4 evergreen docs or "ask me after the inventory"}
- Skip these folders: {list or "none"}
```

Claude should then:
1. Verify the server is reachable
2. Ask the Phase-1 questions it can't infer
3. Dispatch the inventory subagent (Phase 2)
4. Review findings with the user, propose categories
5. Lock the style (Phase 4)
6. Build registry → data.json → HTML templates → process file → routing row
7. Smoke-test
8. Hand off the URL

---

## Acceptance criteria — when is the dashboard "done"

- [ ] `index.html`, `archive.html`, `data.json`, `sources.md`, `claude-dashboard-process.md` all exist in `claude-dashboard/`
- [ ] Workspace top-level CLAUDE.md has the routing row
- [ ] All three URLs return 200 over HTTP
- [ ] Every URL listed in `data.json` resolves to a real file on disk
- [ ] At least one pinned card has inline extracted content (or all pinned cards are simple link cards by design)
- [ ] Every category card has either a `+ Run new` button (with a real process file behind it) or no button at all — never an empty/dead button
- [ ] Clicking any copy-prompt button writes text to the clipboard and shows the toast
- [ ] Freshness pills show on every category and pinned card (green / amber-stale / neutral-adhoc)
- [ ] MD-only categories appear in the dimmed "Needs rendering" zone, not mixed with HTML categories
- [ ] Print stylesheet works (test with browser print preview — ink on white, buttons hidden)
- [ ] Refresh process file documents the schema, the 10 steps, and a "how to add a new category / pinned item" section
- [ ] Future work section captures: any MD-only items that should be HTML-rendered, any pending naming-convention changes, any pinned items that may go evergreen

---

## What this is NOT

To stay disciplined and avoid scope creep:

- **Not a CMS.** The dashboard doesn't edit artifacts. It indexes and launches.
- **Not multi-user.** Local-only, single-machine. No auth, no cloud, no sync.
- **Not realtime.** "Refresh" is a manual step (or scheduled later). The dashboard reflects the last refresh, not the current filesystem state.
- **Not a designer tool.** Layout and components are fixed. Style tokens are configurable; the visual grammar is not.
- **Not a workflow engine.** The buttons copy prompts. They don't *execute* anything. The user pastes into Claude to actually run the work.

---

## Why this works

Three properties:

1. **Loose coupling.** Source folders don't know the dashboard exists. The registry is the only contract. Move folders, rename files, change conventions — update the registry and refresh.
2. **Transparent regeneration.** Every refresh fully rewrites `data.json`. No incremental state, no migrations, no drift. If something looks wrong, regenerate.
3. **Compounding usefulness.** Each new artifact category is a one-row addition. Each new automated process is a one-prompt addition. The dashboard's value scales with the workspace.

The trap to avoid: treating the dashboard as a destination. It's a junction. Everything useful happens because of what it routes you to.
