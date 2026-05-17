# md-to-html — Convert a Markdown artifact into a styled, interactive HTML sibling file

> Renders a Markdown file as a self-contained HTML artifact applying the "Unreasonable Effectiveness of HTML" principles: rich layout, color-coded callouts, click-to-copy, collapsibles, and component-based visual structure. The HTML file is written as a sibling of the source (same basename, `.html` extension).

## Trigger

- "Render this competitor deep-dive as HTML"
- "Convert <markdown file> to HTML"
- Invoked automatically by `ic-trends-daily-process.md` and `ic-trends-tool-deepdive-process.md` after the markdown is written.
- Invoked automatically by `paid-youtube-hook-batch` after a batch's `ideas.md` is written, producing the interactive `ideas.html` selection sheet.

## Inputs

- **Source path** (required) — absolute path to the `.md` file to convert
- **Artifact type** (optional) — `deep-dive` (default, e.g., competitor profile) | `daily-recap` (IC trends recap) | `weekly-plan` (PA `current-week.md`) | `hook-batch` (paid-youtube hook ideas — interactive selection) | `dashboard` (number-driven status report with inline SVG/CSS charts; for leadership briefings, program health checks, KPI snapshots) | `one-pager` (print-format letter portrait; uses `cerkl/marketing/design/one-pagers/reference-one-pager.html` — different design system optimized for print, runs through `html-overflow-detector` + `html-to-pdf` after this skill) | `generic`
- **Theme** (optional) — `light` (default) | `dark`. Dark variant is opt-in and works with any artifact type. Use for short, high-impact, external-facing artifacts (leadership briefs, pitch one-pagers, prospect-shareable comp profiles). Don't use for long-read daily artifacts (recaps, deep-dives) — eye fatigue.

## Output

- A `.html` file at the same path with `.md` → `.html` (e.g., `staffbase-2026-05-10.md` → `staffbase-2026-05-10.html`)
- The HTML must be **self-contained**: inline CSS, inline JS, no CDN dependencies, no external assets.
- Footer references the source `.md` for traceability.

## When to use

Whenever a Markdown artifact is going to be **read by a human as a final document**, not consumed by another agent. Cerkl examples:

- Competitor deep-dives in `cerkl/research/ic-trends/deepdives/`
- Daily IC trends recaps (link-shareable to leadership)
- Vendor profile updates feeding `shared/competitors.md`
- Strategy briefings, comparison matrices, market scans

**Don't use** for:

- Files that are agent-consumed (CLAUDE.md, CONTEXT.md, sources.md, process docs, `shared/icp.md`, `shared/competitors.md`)
- Short conversational outputs
- HubSpot CSV exports or any data file

## How to invoke

The caller dispatches a sub-agent (to keep conversion tokens out of the main context window) with this brief:

```
Run the md-to-html skill on <source_path>.

1. Read /Users/travisfoster/claude-code/cerkl/skills/md-to-html/SKILL.md
2. Read /Users/travisfoster/claude-code/cerkl/skills/md-to-html/reference-deep-dive.html — visual language reference (theme, components, JS).
   For `daily-recap` artifact type, also read /Users/travisfoster/claude-code/cerkl/skills/md-to-html/reference-daily-recap.html.
   For `weekly-plan` artifact type, read /Users/travisfoster/claude-code/cerkl/skills/md-to-html/reference-weekly-plan.html instead — it carries the day-card collapsibles, deadline-pill strip, week-at-a-glance table, and auto-open-today JS.
   For `hook-batch` artifact type, read /Users/travisfoster/claude-code/cerkl/skills/md-to-html/reference-hook-batch.html instead — it carries the selection UI and copy-to-clipboard JS that the other references don't have.
   For `dashboard` artifact type, read /Users/travisfoster/claude-code/cerkl/skills/md-to-html/reference-dashboard.html instead — it carries the inline-SVG donut charts, CSS-only horizontal bar charts, CSS-Grid timeline strip, traffic-light gauges, paired-bar comparison, and number-led card patterns. Less prose; charts replace paragraphs.
   For `one-pager` artifact type, read /Users/travisfoster/claude-code/cerkl/marketing/design/one-pagers/reference-one-pager.html instead — it is a DIFFERENT design system (print-format letter portrait, .page divs, CSS Grid pagination, content-budget catalog in the header comment, layout variants per component, --body-size Tier-A remediation knob). Do not use reference-deep-dive.html's components for one-pagers. Compose by selecting variants from the catalog based on per-section word counts in the source markdown.
   When `theme=dark`, ALSO read /Users/travisfoster/claude-code/cerkl/skills/md-to-html/reference-dark.html — visual-language overlay (dark theme variables, gradient hero, dark-adapted semantic colors). Component class names match the light reference, so dark is a theme swap, not a layout change. The artifact-type-specific reference still governs section order and required components. **Dark theme is NOT supported for `one-pager` artifacts** — print uses light only.
3. Read the source markdown at <source_path>.
4. Write the HTML at the sibling path (same basename, .html extension), self-contained per the skill's quality bar.
5. Return only the output path + a one-line confirmation of components used. Do NOT echo the HTML body back to the parent.
```

## Design principles

The point of HTML output is to use what HTML can do that Markdown can't. Don't just style the Markdown — **rearrange for visual density**.

### Typography — Cerkl brand-aligned

Per Cerkl brand guidelines (`cerkl/marketing/design/branding-assets/Brand Guidelines/typography.md`), **Work Sans is the brand face for all web type** (headings, body, buttons). No serif body — that was the personal/ default; cerkl follows brand.

- **Font: Work Sans** (Google Fonts) — all web text. Body Regular 400; subtitles Medium 500; headings/buttons SemiBold 600 (Bold 700 for H1).
- **Stack:** `"Work Sans", Inter, ui-sans-serif, system-ui, -apple-system, sans-serif` — falls back gracefully if Google Fonts CDN is unreachable.
- **Mono (`ui-monospace, "JetBrains Mono", "SF Mono", Menlo, monospace`)** for code, install commands, copy-prompt boxes.
- **Sizes:** body 18px / 1.55 (close to brand Body 2 = 18px / 28px). H1 32–36px / 1.2; H2 22–24px / 1.3; H3 18px / 1.4. Letter-spacing -0.25 to -0.5 on headings per brand. Overlines (`.breadcrumb`, `.callout-label`) use SemiBold 600 with letter-spacing 0.05–0.08, all-caps.
- **Prose width:** `<p>` capped at 70ch. Outer wrap can extend ~1080px for grids/tables.

**Google Fonts exception to "self-contained" rule:** Brand-faced cerkl artifacts MUST use Work Sans. Embed via `<link>` to `https://fonts.googleapis.com/css2?family=Work+Sans:wght@400;500;600;700&display=swap`. This is the only allowed external dependency. The fallback stack ensures the artifact remains readable if the CDN is unreachable (cached / offline / blocked).

### Color scheme — Cerkl brand palette

Per `cerkl/marketing/design/branding-assets/Brand Guidelines/colors.md`. The primary palette is **cobalt + cosmic + butter** with accents in forest, ruby, and violet.

- **Light mode by default; dark is opt-in via `theme=dark`.** Brand defaults to white / Cosmic 10 backgrounds with Cosmic-base text. Dark variant (Cosmic-base body + Cobalt 100 gradient hero) is brand-approved — Cobalt 100 is explicitly tagged "dark backgrounds, depth" and every typography style approves white text. Use dark for short, high-impact, external-facing artifacts (leadership briefs, pitch one-pagers, prospect-shareable comp profiles). Keep light for long-read daily artifacts. See `reference-dark.html` for the dark theme variables.
- **Accent (primary brand):** Cobalt 60 `#3547c4` — used for hyperlinks, accent borders, TL;DR rule, primary buttons.
- **Surfaces:** white `#ffffff` (panel), Cosmic 10 `#f5f5fa` (panel-soft / body bg).
- **Text:** Cosmic base `#18181d` (ink), Cosmic 80 `#373740` (muted secondary).
- **Borders:** Cosmic 30 `#d5d5db` (line).
- **Semantic colors:**
  - Good (Yes verdict, success): Forest base `#1a9979` on Forest 10 `#e8fffa`
  - Warn (Maybe verdict, caution): Butter 100 `#80550f` text on Butter 10 `#fff9f2` bg
  - Bad (No verdict, danger): Ruby 80 `#b00045` on Ruby 10 `#fcf0f0`
  - Info (callouts, accent panels): Cobalt 60 `#3547c4` on Cobalt 10 `#f0f2fc`
  - Quote (community-signal accent): Violet base `#802ee6`
- **Code bg:** Cosmic 20 `#ebebf0`.
- One accent color (Cobalt 60) does the heavy lifting. Semantic colors only used where they carry meaning, never for vibe.

**Daily-recap category badges** — IC-specific, brand-aligned:
- Competitor: Cobalt 60 `#3547c4`
- Publication: Forest base `#1a9979`
- Analyst: Violet base `#802ee6`
- Community: Butter 100 `#80550f` text on Butter 10 bg (Butter base `#ffaa22` is too bright for badge text on light bg)
- Policy: Ruby 80 `#b00045` on Ruby 10 bg

### Required components

1. **Hero block at top** — title, breadcrumb (e.g., "ic-trends · Competitor Deep Dive"), date, category, and a color-coded verdict pill if there's a recommendation (Yes = green, Maybe = amber, No = red).
2. **TL;DR rendered prominently** — accent-bordered paragraph in the hero, ~2-3 sentences max.
3. **First-thing-to-try as a callout** — if the source has a "first thing to try" or "first action," surface it in the hero with a prominent style.
4. **Sectioned cards** — each major section gets a numbered card (`<section>` with a numbered `<h2>`). This breaks up wall-of-text.
5. **Click-to-copy on actionable strings** — any verbatim quote, vendor URL, install command, magic config line gets a copy button. JS is included in the reference.
6. **Color-coded callouts** for warnings/info/try-this. Three variants: `.try` (Cobalt 60), `.warn` (Butter 100/10), `.info` (Cobalt 60 / Cobalt 10).
7. **Quote cards** for community signal — speaker, date, link to source. Skeptic quotes get a different border color.
8. **Comparison tables** with hover states + a highlighted "decision-relevant axis" callout below.
9. **Collapsible `<details>` for open questions** — preserves data without wall-of-text.
10. **Print-friendly stylesheet** — include `@media print { ... }` so the artifact exports cleanly to PDF (light theme acceptable for print).
11. **Self-contained — with brand-font exception.** No CDN-loaded JS libraries, no analytics, no tracking. **Only allowed external resource:** Google Fonts `<link>` for Work Sans (see Typography). All other CSS and JS must be inline.

### Anti-patterns (avoid)

These are the "AI default look" — if your output drifts toward any of them, restart. Inherited from `dogum/html-artifacts`:

- **Cards everywhere** with rounded corners and shadows, on a gray background, doing no actual work.
- **Gradients used outside brand spec.** Cerkl's brand explicitly calls gradients "a key part of Broadcast's branding." The rule: **one approved gradient per design**, drawn from the brand combinations (`#4c60d9 → #3547c4`, `#0c1159 + #a7b3ed`, `#f5f5fa → #3547c4`, or the full cobalt sweep). Hero block is the natural home (especially in the dark variant). Multiple gradients, off-palette gradients, or animated gradient backgrounds are still off-brand.
- **Emoji as section headers** (📊 Analytics, ⚡ Performance). Use real iconography or none.
- **Four shades of indigo or violet** doing nothing in particular. One accent color, used semantically.
- **Shadcn-shaped components** when no shadcn library is in play.
- **Glass morphism, frosted blur, animated background gradients.**
- **Centered everything.** Left-aligned prose with deliberate structure beats centered cards.
- **Header with a logo placeholder.**
- **Wall of generic Tailwind cards with emoji headers.** This is the strongest tell of unconsidered generation.

If the output has any three of these, the rendering agent should restart from the reference template.

### Also avoid

- Centered layouts wider than ~1080px
- Fonts other than Work Sans for primary text (Work Sans IS the brand face; loading additional families is unnecessary)
- Animations beyond simple hover states
- Tracking scripts, analytics, or any network calls beyond the Google Fonts `<link>`
- Markdown-rendered-as-HTML look (i.e., just `<h1>`/`<p>` with no structure) — that defeats the purpose

## Layout patterns by artifact type

### `deep-dive` (default — competitor deep-dive, vendor profile, etc.)

Sections in this order (skip any that don't apply):
1. Hero (title, meta, verdict, TL;DR, first-thing-to-try)
2. What it is + What it does — two-column
3. Who it's for — three-card grid (primary user / strong fit / weak fit)
4. How it slots into Cerkl's competitive set / positioning — section with stack-card grid
5. Comparison to alternatives — table + axis callout
6. Gotchas — stacked callouts
7. Community signal — stats strip + quote cards
8. Recommendation — highlighted block with reco-grid (first thing to try / time-box / what would change my mind)
9. Open questions — collapsibles

### `daily-recap`

See `reference-daily-recap.html` in this folder for the canonical example.

Sections:
1. **Hero** — date, breadcrumb ("ic-trends · Daily Recap"), headline takeaway (2-sentence framing, accent-bordered). No verdict pill — recaps don't recommend; they survey.
2. **Top items** as numbered cards (5–10 items). Each card has:
   - Headline, source, URL, date, category badge (color-coded: Competitor / Publication / Analyst / Community / Vendor news / Policy)
   - 1–2 sentence summary
   - Optional "Why it matters for Cerkl" callout — only when it actually does
3. **Watchlist** as a 2-column compact list grouped by sub-heading (Competitors / Publications / Analysts / Community). Each row is one line: bold-title, source, date, URL. Denser than top items.
4. **Notes** as collapsible `<details>` blocks — covers gaps, source failures, paywalled reports.

Layout-specific patterns:
- Category badges in top-item cards should be visually distinct enough to scan by category at-a-glance
- Watchlist is *much* denser than top items — small font, one line each, multi-column where space allows
- Don't include a "recommendation" block — daily recaps don't recommend

### `weekly-plan`

See `reference-weekly-plan.html` for the canonical example. Used by the `personal-assistant` `plan-week` skill to render a sibling HTML of `current-week.md`. Scope is Mon–Fri work — not a personal life-plan (that artifact lives in `personal/` with a different theme).

Sections:
1. **Hero** — breadcrumb (`Personal Assistant · Weekly Plan`), title (`Week of <Mon> — W##`), meta-row (Range, Week A/B chip, Materialized date), TL;DR (2–3 sentences synthesizing the week's shape), and a **deadline-pill strip** for any hard EOD/by-date deadlines in the week. No verdict pill — weekly plans don't recommend; they allocate.
2. **Week at a glance** — a 4-column table (Day | Meetings | Free | Top priority). The "today" row gets a Cobalt-tinted background; the auto-open JS rewrites this on load using the visitor's local date, so don't hard-code which row is "today" unless you also want the script to overwrite it.
3. **Daily** — one collapsible `<details class="day-card">` per Mon–Fri. Each card has:
   - Summary row with day-of-week, date, optional `.day-tag` (e.g. `deadline`), and a one-line headline of the day's top priority
   - `.day-deadline` callout at the top of the body if the day has a hard EOD deadline
   - `.day-section` sub-blocks for Meetings, Free blocks, Priorities for the day, Ad-hocs / notes (preserve empty `(empty)` placeholders rather than dropping the section — Travis reads the absence as signal)
4. **Carryover candidates** — `.carryover-row` list with title · detail · priority pill (`.high` / `.med` / `.low`).
5. **Friday retro notes** — `.callout.info` placeholder section. Stays empty in the materialized plan; the `retro` skill populates it Friday end-of-day.

Layout-specific patterns:
- The `data-date="YYYY-MM-DD"` attribute on every day-card and glance row is **required** — the auto-open script keys off it
- Day-card auto-opens for today and gets `.today` styling (left-border accent)
- Free blocks render as inline `.free-block` code-style pills with a total at the end
- Priorities use an ordered list; bold the project name at the start of each item
- Don't include personal-life sections (goals, calendar snapshot with non-work events, weekend days) — this artifact is work-only. If a user wants a full life-plan, that's the personal/ template, not this one.

### `hook-batch`

See `reference-hook-batch.html` for the canonical example. **This is the only artifact type with interactive state.** Used exclusively by the `paid-youtube` channel's hook generation flow.

Sections:
1. **Hero** — title (`Hook Batch — <YYYY-MM-DD>`), breadcrumb (`paid-youtube · Hook Batch`), batch parameters in meta-row (ICP, mix ratio, total hook count, seed sources), TL;DR with usage instruction ("click a card to select, copy button produces paste-ready block").
2. **Sticky selection bar** — sits just below the hero with `position: sticky; top: 12px;`. Shows live "N selected" counter, primary "Copy Selections" button (disabled at 0), secondary "Clear" button.
3. **Hook grid** — single column of `.hook-card` rows. Each card has:
   - Custom-styled checkbox (orange when checked)
   - Hook ID (e.g., `H01`) in sans-serif uppercase
   - VO line — large serif, the dominant element
   - Visual concept — small italic muted-gray
   - Two badges: `.cat-badge.pain` or `.cat-badge.positioning` for angle, `.cat-badge.pattern` for the pattern type
   - Whole-card click toggles the checkbox (label-wrapping pattern); selected state changes background + adds accent inset shadow
4. **Footer** — references source `ideas.md`, batch date.

Required JS behavior:
- Checkbox change updates counter and selected-card visual state
- Clear button unchecks everything
- Copy button reads all checked cards' `data-id` and `data-vo` attributes, builds a paste-ready text block, writes to clipboard (`navigator.clipboard.writeText` with a `document.execCommand('copy')` fallback for non-secure contexts), shows a brief toast
- Format of the copied block (must match exactly so the chat parser downstream is predictable):
  ```
  Picks from <YYYY-MM-DD>-batch — paid-youtube hooks

  Selected (N):

  H## — "<VO line>"
  Reason: [add your reason]

  ... (one block per pick)

  Next: run paid-youtube-hook-select with these picks.
  ```

Required HTML pattern per card — the `data-` attributes are what the copy script reads, so they must be present and accurate:
```html
<label class="hook-card" data-id="H01" data-vo="The exact VO line, no smart quotes">
  <input type="checkbox" class="hook-cb" aria-label="Select H01">
  <div class="hook-body">
    <div class="hook-id">H01</div>
    <div class="hook-vo">&ldquo;The VO line with smart quotes for display&rdquo;</div>
    <div class="hook-visual">The visual concept sentence.</div>
    <div class="hook-tags">
      <span class="cat-badge pain">Pain · short angle label</span>
      <span class="cat-badge pattern">Pattern label</span>
    </div>
  </div>
</label>
```

Don't apply deep-dive components (verdict pills, comparison tables, reco grid, quote cards) — hook-batch is selection-driven, not analysis-driven.

### `dashboard`

See `reference-dashboard.html` for the canonical example (rendered from `cerkl/marketing/seo/reports/2026-05-15-blog-seo-leadership-status.md`). **Number-driven status report.** Use for leadership briefings, program health checks, KPI snapshots — anywhere the audience wants to scan the state of a system, not read a narrative. Pairs naturally with `theme=dark`.

The principle: **less prose, more visualization.** Each section leads with a chart or stats strip; explanatory text is at most 1–2 sentences. Cut paragraphs that just describe what a chart already shows.

Sections in this order (skip any that don't apply):
1. **Hero stat strip** — 5 headline numbers at-a-glance (the audience reads these first; everything else is depth). Dashboard title + date + breadcrumb + accent-bordered TL;DR. No verdict pill.
2. **Inventory / current state** — horizontal bar chart with per-row labels + health-status badges. Use one accent color (Cobalt 60) for bars; reserve the semantic palette (Forest / Butter / Ruby) for the badges only.
3. **Breakdown donuts** — inline-SVG ring charts (stroke-dasharray pattern). Pair a main donut (overall surface) with a focused donut (one slice expanded). Legends below each.
4. **Timeline / calendar** — CSS-Grid strip showing scheduled items across N weeks, color-coded by category. Each cell is a small "chip" with date + title.
5. **Comparison bars** — paired existing-vs-pipeline (or before-vs-after) bars to surface relative movement.
6. **Number-led cards (2–4)** — strategic-move or initiative cards each anchored by a single big number + one-line context + outcome metric.
7. **Status gauges** — traffic-light pills (Forest / Butter / Ruby) for tooling status, infrastructure readiness, or any binary-state inventory.
8. **Before / after compact comparison** — two-column table contrasting prior state with current. No headers above each row; let the contrast do the work.
9. **Actions table** — tight, scannable. Effort + owner + unlock columns. No prose row descriptions.

Chart implementation rules:
- **All charts inline SVG or CSS-only.** No D3, no Chart.js, no external libraries. Self-contained except Google Fonts.
- **SVG ring charts** use `stroke-dasharray="<slice> <remainder>"` with `stroke-dashoffset` to rotate slices into position; one `<circle>` per slice; total `viewBox="0 0 32 32"` and `r=16` is convenient. Wrap with a `<text>` element for the center number.
- **Horizontal bars** are flexbox rows: `<label><fill style="width:N%"/><value/></label>`. No SVG needed.
- **Timeline grid** uses CSS Grid (`grid-template-columns: repeat(7, 1fr)` for weekly) with brief chips placed by grid-column-start.
- **Status gauges** are styled pills using `.gauge.bad / .warn / .good` matching the semantic palette.
- **Cap chart count.** A dashboard with 8+ visualizations becomes a wall of charts; aim for 4–6 distinct chart types per page.

Layout-specific anti-patterns:
- **Don't recompute numbers.** The orchestrator (caller) should pre-compute percents and pass them in the brief. Sub-agents that recompute from source tables introduce rounding drift.
- **Don't pretend you have data you don't.** Dashboards lose credibility instantly when a chart implies measurement you can't substantiate. Mark missing data explicitly (e.g., a "Not currently tracked" status gauge) rather than fabricating a number.
- **Don't introduce a 5th accent color** to differentiate chart series. The palette has 6 semantic colors and that's already plenty.

### `generic`

Render sections in source order, applying components opportunistically. Use callouts where the source has bold caveats, comparison tables for any markdown table, quote cards for any blockquote.

## Component reference

This skill folder contains five reference templates:

- **`reference-deep-dive.html`** — canonical visual language for the **light** theme (Cerkl brand palette, component library, click-to-copy JS, print stylesheet). Use as the source-of-truth design system reference.
- **`reference-daily-recap.html`** — example application of the same design system to a daily-recap content shape. Use when artifact-type is `daily-recap`.
- **`reference-weekly-plan.html`** — PA weekly-plan variant. Day-card collapsibles (Mon–Fri), deadline-pill strip, week-at-a-glance table, auto-open-today JS. Use when artifact-type is `weekly-plan`.
- **`reference-hook-batch.html`** — selection-driven variant of the design system. Adds checkbox-state cards, sticky selection bar, and copy-to-clipboard JS that produces a paste-ready text block. Use when artifact-type is `hook-batch`.
- **`reference-dashboard.html`** — number-driven dashboard variant. Inline-SVG donut charts, CSS-only horizontal bar charts, CSS-Grid timeline, traffic-light gauges, paired-bar comparison, number-led cards. Use when artifact-type is `dashboard`. Pairs naturally with `theme=dark`.
- **`reference-dark.html`** — dark-theme overlay. Component class names match the light reference, so any artifact type swaps to dark by lifting these theme variables + the gradient-hero pattern. Body: Cosmic base (`#18181d`). Hero: Cobalt 100 + Cobalt 40 freeform gradient. Use when `theme=dark`. Pair with the artifact-type-specific reference for section order; this file only governs visual language.

Read whichever matches your artifact type once, then write fresh HTML — don't try to diff against it. Both share the same CSS theme, so cross-referencing the deep-dive reference for components and the recap reference for layout is fine.

Component classes available in the reference:

| Class | Purpose |
|---|---|
| `.hero` | Title block at top with verdict pill |
| `.verdict` (`.good` / `.warn` / `.bad`) | Color-coded recommendation pill |
| `.tldr` | Accent-bordered TL;DR paragraph |
| `.callout.try` / `.callout.warn` / `.callout.info` | Styled callouts |
| `.code-row` + `.copy-btn` | Inline code with click-to-copy |
| `.cols-2` | Two-column responsive layout |
| `.pillars` / `.pillar` | Numbered card grid (e.g., "five pillars") |
| `.personas` / `.persona` | Primary user / fit / not-fit cards |
| `.stack-cards` / `.stack-card` | "How it slots into the stack" cards |
| `.cmp` (table) | Comparison table |
| `.axis-note` | "Decision-relevant axis" highlight |
| `.quotes` / `.quote` (`.skeptic`) | Community quote cards |
| `.stats` / `.stat` | Numeric stats strip |
| `.reco` / `.reco-cell` | Recommendation block (deep-dive only) |
| `details.q` | Collapsible open questions / notes |
| `.top-item` / `.cat-badge.*` | Numbered top-item card with category badge (daily-recap) |
| `.watchlist` / `.watch-row` | Compact multi-column watchlist (daily-recap) |
| `.deadline-strip` / `.deadline-pill` | Hard-deadline pills in the hero (weekly-plan) |
| `table.glance` | Week-at-a-glance table with today-row highlight (weekly-plan) |
| `.day-card` / `.day-section` | Collapsible per-day card with Meetings / Free / Priorities sub-blocks (weekly-plan) |
| `.free-block` | Inline mono pill for a free time range (weekly-plan) |
| `.carryover-row` / `.c-priority.{high,med,low}` | Carryover candidates list with priority pill (weekly-plan) |
| `.week-chip` | Week A/B parity chip in the hero meta-row (weekly-plan) |
| `.sel-bar` | Sticky selection bar with counter + copy/clear buttons (hook-batch) |
| `.hook-card` (+ `.selected`) | Selectable hook card with custom checkbox (hook-batch) |
| `.cat-badge.pain` / `.positioning` / `.pattern` | Angle and pattern type badges (hook-batch) |
| `.toast` (`.show`) | Toast notification after copy-to-clipboard (hook-batch) |
| `.hero-stats` / `.h-stat` / `.h-num` / `.h-lbl` | Hero 5-number stat strip — headline KPIs at-a-glance (dashboard) |
| `.bar-chart` / `.bar-row` / `.bar-fill` / `.bar-label` / `.bar-meta` | CSS-only horizontal bar chart with per-row labels and value badges (dashboard) |
| `.donut-card` / `.donut-grid` / `.donut-svg` / `.donut-center` | Inline-SVG ring chart via stroke-dasharray (dashboard) |
| `.legend` / `.legend-item` / `.legend-swatch` / `.legend-label` / `.legend-value` | Donut legend rows with color swatches (dashboard) |
| `.brief-chip` | Category-color-coded chip placed on a CSS-Grid timeline row (dashboard) |
| `.pair-row` / `.pair-key` / `.pair-label` / `.pair-track-group` / `.pair-bar-track` | Paired existing-vs-pipeline (or before-vs-after) comparison bars (dashboard) |
| `.gauge-grid` / `.gauge-tool` / `.gauge-status` / `.gauge-unlocks` | Traffic-light tooling-status gauges (dashboard) |
| `.cost-callout` / `.cost-label` / `.cost-formula` / `.cost-result` | Cost-to-unlock prominent callout pairing with status gauges (dashboard) |
| `.ba-grid` | Two-column compact before/after comparison (dashboard) |
| `.actions` (table) / `.act-num` / `.effort` | Tight, scannable recommended-actions table (dashboard) |

## Quality bar

Before returning, verify:
- [ ] Self-contained (no `<link>` to external CSS aside from the Work Sans Google Fonts link, no `<script src=…>`)
- [ ] Theme matches the requested mode: light (default) renders on white / Cosmic 10; dark renders on Cosmic base with the Cobalt 100 + Cobalt 40 freeform gradient hero
- [ ] Body in Work Sans; UI chrome (breadcrumb, badges, buttons) uses Work Sans at SemiBold/Bold per brand typography
- [ ] Print stylesheet present (light theme always — paper needs ink-on-white regardless of screen theme)
- [ ] Footer references the source `.md` file
- [ ] All hyperlinks from the source markdown are preserved
- [ ] All quoted text from community signal includes attribution + source link
- [ ] No content is dropped — if the source has 8 sections, the HTML has 8 sections
- [ ] Verdict pill matches the source's recommendation (Yes/Maybe/No)
- [ ] No anti-patterns (gradient hero, emoji headers, glass morphism, etc.)

## Token cost honesty

HTML output runs **2–4× the tokens of a Markdown equivalent**. Smoke tests have come in at ~2.5× (13.8 KB MD → 34 KB HTML). The reading experience and shareability earn the cost for artifacts that get reread or shared. For one-shot summaries that get scanned once and discarded, stay in Markdown.

This is also the main reason every render is dispatched to a sub-agent: ~9K of tokens that would otherwise sit in the main context permanently end up isolated in the sub-agent and only a confirmation returns to the parent.

## Future work

- Add a `generic` reference template if a third artifact type is requested
- Auto-generate share links if/when a render-and-host pipeline exists (Google Drive `md-to-drive` skill is the likely host — see `cerkl/skills/md-to-drive/SKILL.md`)
