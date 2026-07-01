# One-Pager

> Produce a print-ready, visually rich PDF from a brief or a reference doc. Output: a `.{md,html,pdf}` trio under `output/<family>/` (e.g. `output/battlecards/<slug>-YYYY-MM-DD.*`). Letter-portrait by default; competitive battlecards are letter-landscape.
>
> **The bar:** designer-grade, magazine-dense, brand-true. Lead with real product screenshots and brand icons, not the reference's empty placeholder boxes. (Gradients as backgrounds, bands, and CTAs are encouraged — the rule is don't leave a blank stand-in gradient where a real asset belongs.) Default to a rich, multi-section page — see *Principles → Density*.

## Trigger

- "Let's make a one-pager"
- "Draft a one-pager for [event / meeting / topic]"
- "We need a Broadcast overview / IT pre-meeting / [topic] handout"
- "Write the one-pager for [partner / webinar / sales meeting]"

---

## How this process works (read first)

The running agent owns the outcome. This doc gives you the **resources** (tools, assets, components, recipes, budgets) and the **principles**; you make the calls and adjust on feedback. It is deliberately flexible — there are no rigid "tiers" or "types" to slot into. Load only what you need, when you need it, to protect context and tokens.

The flow:

```
0 Orient ──► 1 Strategy (self-served) ──► 2 Plan layout & assets ──► 3 Build (md → HTML)
   ──► 4 Self-review & edit (HTML only) ──► [SHARE — sign-off gate] ──► 5 Render PDF ──► 6 Harvest
```

Two real pauses: **share the HTML for sign-off** before rendering the PDF, and **escalate** only if remediation can't fit the page. Everything else the agent runs on its own judgment.

---

## 0 · Orient (cheap load)

Load the light stuff first. Do **not** pull the full reference HTML or every `shared/` file yet.

- This process doc (you're reading it).
- `marketing/design/CONTEXT.md` — brand palette, gradient rule (one per design), logo rules.
- The **Component index** (below) — one line per component so you can plan without loading the full reference.
- The **Tools & assets** inventory (below).
- The brief / any reference docs the user pointed you at.

Pull the heavier context (`shared/broadcast.md`, `shared/competitors.md`, `shared/icp.md`, `shared/company-info.md`, the matching `shared/features/*.md`, and the full `reference-one-pager.html`) **in Step 2–3, once you know what you're building** — and only the pieces that apply.

---

## Tools & assets you can use

Know these exist so you don't reinvent the wheel or ship a flat page. **The single biggest quality lever is filling the reference's placeholder stand-ins with real assets** (two early renders shipped the blank placeholder squares — don't repeat that). This is about swapping *empty placeholder blocks* for real screenshots/icons/photos/logos — not about avoiding gradients, which are great for backgrounds, bands, and CTAs.

### Skills that work (call by absolute path; most auto-trigger)

| Need | Skill |
|---|---|
| Render markdown → one-pager HTML | `cerkl/skills/md-to-html/SKILL.md` with `artifact-type=one-pager` |
| Render HTML → PDF (built-in overflow verify gate) | `cerkl/skills/html-to-pdf/SKILL.md` |
| Scan HTML for overflow/overlap/clipping before PDF | `cerkl/skills/html-overflow-detector/SKILL.md` |
| One-pager / deck / banner copy | `cerkl/marketing/skills/copywriting/SKILL.md` |
| Sales angle, objection handling, positioning | `cerkl/marketing/skills/sales-enablement/SKILL.md` |
| Generate a hero image / mockup when no real asset fits | `cerkl/marketing/skills/image/SKILL.md` |

### Asset libraries — browse the index, then evaluate fit

**Don't go hunting for a pre-named asset.** Browse the relevant INDEX to see what's *available*, pull anything that *might* serve the vision, look at it, and decide if it earns a place. The point is informed selection, not a checklist.

| Library | Index to browse | What it gives you |
|---|---|---|
| **Product screenshots** | `marketing/design/branding-assets/Product Illustration/Product Images/INDEX.md` (routes to 16 feature subfolders, each with its own per-file INDEX) | Real UI for hero mockups & feature shots — the thing that makes a page look designed, not generated |
| **Brand icons** | `marketing/design/branding-assets/Design Components/Brand Icons/` | Consistent line-icons for feature rows, stat bands, VS blocks — replaces placeholder circles |
| **Photography** | `marketing/design/branding-assets/Cerkl Photography/INDEX.md` | Office / Culture / Group photos for hero covers & image cards |
| **Customer logos** | `marketing/design/branding-assets/Customer Logos/` (inventory 2026-05-15: Church & Dwight, Novant Health, UC, Paycor, Roivant, St. Elizabeth) | Social-proof logo strips |
| **Broadcast lockups** | `marketing/design/branding-assets/Broadcast/Cerkl Broadcast Horizontal Lockup/` (Medium 160px, Small 80px) | The product wordmark for hero & footer |
| **Partner / co-brand logos** | `marketing/design/one-pagers/assets/` | Partner logos & competitor screenshots used in co-branded pieces & battlecards |

Asset routing lives in `marketing/design/CLAUDE.md` and `marketing/design/branding-assets/INDEX.md` if you need a wider map.

---

## Context to load (by step)

- **Step 0–1:** `marketing/design/CONTEXT.md` + the brief/reference docs (above).
- **Step 2–3, as relevant:** `shared/broadcast.md`, `shared/competitors.md`, `shared/icp.md`, `shared/company-info.md`, `marketing/design/branding-assets/Brand Guidelines/brand-guidelines.md`, and the matching `shared/features/*.md` for any feature you name (ai-personalization · analytics-insights · audience-segmentation · content-management · email-blasts · omni-channel-publishing · pulse-surveys-acknowledgments).
- **Step 3 (renderer):** `reference-one-pager.html` is read by md-to-html, not you — you work from the Component index.

(Per [PRINCIPLES.md #4](../../../PRINCIPLES.md), this list is authoritative for this scope.)

---

## Output path convention

```
cerkl/marketing/design/one-pagers/output/<family>/<slug>-YYYY-MM-DD.{md,html,pdf}
```

**Folder layout.** Artifacts live in `output/`, grouped by family: `output/battlecards/` (competitor comparisons; `…/research/` holds supporting notes), `output/recaps/` (webinar/event), `output/leave-behinds/` (sales handouts). Add a new family folder when a new artifact type recurs. Shared input assets — partner logos, screenshots — live in `one-pagers/assets/`. The `reference-one-pager.html`/`.pdf` template stays at the `one-pagers/` root.

The `.pdf` is the deliverable. The `.md` and `.html` are the audit trail — keep them. Revisions are 100× easier when the markdown source is on disk.

**Asset paths from an `output/<family>/` HTML:**
- Brand assets: `../../../branding-assets/<path>` (three `../`; URL-encode spaces, e.g. `Cerkl%20Broadcast`).
- Partner/co-brand logos & screenshots in `one-pagers/assets/`: `../../assets/<file>`.
- Paths assume HTML lives exactly at `output/<family>/`. Nesting deeper (e.g. `output/battlecards/research/`) changes the depth — count the `../` from the file's actual location.

---

## Principles

### Density — rich by default
The default is a **dense, multi-section, designer-grade page** — aim for the richness of a polished marketing one-pager (think 5–6 distinct sections on a portrait page: hero → feature/icon row → comparison or value block → stat band → CTA). Just below "everything crammed on one page." If the user wants it lighter, they'll say so. The component budgets below reflect this default — they were bumped up from the original print-conservative numbers; respect them but treat them as guides, not walls. The overflow verify gate is your safety net, so reach for richness and let the gate catch genuine overruns.

**Important distinction:** visual density and information density are not the same. A page can feel premium with many modules, icons, dividers, badges, screenshots, and CTA treatments, but the copy should stay lighter than the visual system. Prefer more visual modules with shorter text over fewer modules packed with paragraph copy.

### Visual quality
- **Real assets over placeholders.** Browse the asset indexes and use real product screenshots, brand icons, photos, and logos. A page that still shows the reference's *empty placeholder boxes* (blank stand-in gradients where an asset belongs) is a failed render — never ship one. **This is not a rule against gradients:** decorative gradients, gradient bands, and `gradient-cta` are encouraged (subject to the one-gradient-per-design rule below). The failure is leaving a hollow placeholder where a real asset would serve better.
- **Hero mockup first for product pages.** For product/package overviews, a large product screenshot/device mockup paired with a short tier badge (e.g. Foundations / Omni AI) is usually the strongest first impression. Treat this as the starting point unless the brief is event-, story-, or account-led.
- **Lead with a number *or* a tension.** Sales / recap / leave-behind pieces open with a `number-row` or `stat-panel`. Positioning / thought-leadership pieces may open with a problem frame instead (e.g. omni-ai-exo: *"Enterprises have signals. What they lack is delivery."*). Pick by intent.
- **≥3 distinct component types per body page.** Two of the same component back-to-back (two feature-grids, two bullet-grids) reads as a textbook. Mix it up.
- **Use modules to pace the scan.** A premium one-pager needs obvious stops: hero, icon row, comparison, included checklist, stat band, CTA. Avoid long same-weight blocks where every card has title + icon + 2-3 lines of body.
- **Whitespace & hierarchy.** Dense ≠ cramped. Let sections breathe with consistent gaps; establish clear visual hierarchy (one dominant element per section). Density comes from *more sections*, not from suffocating each one.
- **One gradient per design** (CONTEXT.md). Choose linear or freeform, not both.
- **Dark sections are on the table.** A dark cobalt band (e.g. an orchestration/engine diagram) adds depth — use `--onDark` text vars and `print-color-adjust: exact` (see omni-ai-exo-2026-06-15).

### Substance & positioning
- **Build prospect-agnostic first, personalize last.** Default to channel-/client-agnostic copy; layer account specifics (logo, name, "their goal") as a final optional pass. (We built TMNAS-specific and had to strip it back out.)
- **Pull objections & sentiment from Sales/CS, not just facts.** Framing-defining steers ("leadership dislikes 'social media'," "wary of algorithms," "why not use what's in our license") are political/emotional and live in reps' heads.
- **Verify every claim against the source of truth.** Reconcile against `shared/broadcast.md` (Cerkl) and verified research (competitors → official docs in `shared/competitors.md`). **Source of truth wins over any internal collateral** — a CS battlecard once listed SMS + digital signage as Cerkl channels; neither is real.
- **Scope claims to the tier being pitched.** Foundations vs. Foundations+ vs. Omni AI differ (mobile app / microsites / cross-channel publishing are Omni AI–only). Tier-inaccurate claims are an easy own-goal.
- **Position honestly and diplomatically.** Amber "limited" marks (not red ✗), concede the competitor's genuine strengths, never attack a dimension the buyer has already bought.

### Print fidelity (checklist)
1. `print-color-adjust: exact` on any colored/gradient/dark background, or Chrome drops it in the PDF.
2. Never pin content to the page edge — leave a bottom margin (an edge-pinned footer clipped in print even though the detector passed).
3. The overflow detector is necessary but not sufficient — **eyeball the actual PDF's bottom edge**.
4. A battlecard is a reusable system: the 6-criterion framework (Consistency · Prioritization · Insights · Reach · AI · Total Value) is competitor-agnostic. Verified competitor facts belong in `shared/competitors.md`.

---

## Steps

### Step 1 — Strategy (self-served) + intake
- **Owner:** Claude (ask only when genuinely blocked)
- **Produces:** a locked strategy held in conversation — the single belief-shift/action, the primary reader, the narrative arc, the proof points, the recipe.

You usually have enough to infer the strategy yourself. Derive it from the brief, any reference docs the user supplied, `shared/icp.md`, and the recipe patterns below. Settle these five — by inference where you can, by asking only what you truly can't resolve:

1. **Purpose** — sales meeting, webinar handout, event download, IT pre-call, long-form guide, competitive battlecard.
2. **Primary reader** — role, industry, company size, journey stage. Cross-check against ICP; flag misalignment.
3. **Single goal** — the one belief-shift or action. If the brief implies several, pick the primary and note it; flag a true conflict.
4. **Proof points** — required stats / case studies / quotes. If none supplied, pull candidates from `shared/broadcast.md` / `shared/competitors.md` / case studies and confirm.
5. **Slug** — short kebab-case (e.g. `broadcast-it-premeeting`).

Only pause to ask if the goal is genuinely ambiguous *and* you can't resolve it from context. A reference doc usually answers most of this — read it before asking.

### Step 2 — Plan layout, components & assets
- **Owner:** Claude
- **Needs:** the Recipe picker + Component index below. Load the full `reference-one-pager.html` only if you need component detail beyond the index.
- **Produces:** a section outline naming the component variants (e.g. "hero-compact → number-row (3) → callout-card → feature-grid.cols-2 → cta-strip") **and** the candidate assets you'll use.

Start at the **Recipe picker**, customize from there, drop to the **Variant pickers** for dense components. Then **browse the asset indexes** (Tools & assets, above): open the relevant INDEX, pull anything that might serve the vision, evaluate it, and note what you'll embed (which product screenshot, which icons, which photo). Present the outline + asset picks to the user for approval before drafting.

### Step 3 — Draft copy in markdown
- **Owner:** Claude
- **Needs:** `cerkl/marketing/skills/copywriting/SKILL.md` (auto-triggers); `sales-enablement/SKILL.md` for sales angles. Load `shared/broadcast.md` + relevant `shared/features/*.md` now.
- **Produces:** `output/<family>/<slug>-YYYY-MM-DD.md` — one section per component, in outline order, within each variant's budget.

Write Cerkl-voice copy. Mark each section with an HTML comment naming its component (e.g. `<!-- component: feature-grid.cols-3 -->`). **Put real `<img>` tags with real asset paths in the source** — the renderer only swaps placeholders when the markdown supplies an actual image (see asset substitution checklist below). If a section runs over budget, pick a roomier variant rather than forcing CSS to absorb it.

Skim the most recent file in the matching `output/<family>/` folder as the working precedent for the md→HTML convention (e.g. `output/recaps/matt-frost-recap-2026-05-19.md`; `output/leave-behinds/omni-ai-exo-overview-2026-06-15.md` for the richest/most-architectural shapes; `output/battlecards/cerkl-vs-viva-amplify-v2-2026-05-29.html` for the landscape battlecard).

**Asset substitution checklist — verify before returning the HTML** (two prior renders shipped placeholder squares):

| Slot | Reference placeholder | Required substitution |
|---|---|---|
| `.hero-cover .wordmark-ph` / `.hero-compact .wordmark-ph` | cobalt square + "Broadcast" | `<img src="../../../branding-assets/Broadcast/Cerkl Broadcast Horizontal Lockup/Medium (160px)/cerkl_broadcast_horizontal_lockup_full_color_medium.png">` (or 80px small) |
| `.hero-cover .photo-block` | "[ HERO PHOTO ]" gradient | real photo or product screenshot filling the block |
| `.footer .brand` | "Cerkl" text | 80px lockup |
| feature/icon cells | placeholder circle | real brand icon from the Brand Icons library |
| `.image-card .photo-ph` | "[ PHOTO ]" gradient | real `<img>` (or leave empty if decorative) |

### Step 4 — Render HTML + self-review (HTML only)
- **Owner:** Claude
- **Needs:** `cerkl/skills/md-to-html/SKILL.md` with `artifact-type=one-pager`.
- **Produces:** `output/<family>/<slug>-YYYY-MM-DD.html`, reviewed and edited — **before** the user sees it.

Render via md-to-html. Then **review your own HTML against the Principles** and fix it before sharing:
- Density: is it rich enough (5–6 sections)? Too sparse → add a section or upgrade a variant. Too cramped → spread it.
- Assets: any placeholder still showing? Re-render with the `<img>` explicit. **Do not share with placeholders.**
- ≥3 distinct component types; no two same components stacked.
- Lead element matches intent (number vs. tension).
- Run **html-overflow-detector**; remediate (Step 5 tiers) so the HTML you share already fits.

Iterate on the `.html` directly during this phase — apply copy/layout/logo/remediation here. **Defer reconciling the `.md`** until the draft is final (the `.md` is the audit trail; sync it at the end). Don't trigger a fresh md-to-html sub-agent for small tweaks.

**▸ SHARE — sign-off gate (PAUSE).** Show the reviewed HTML/PDF-preview. Get explicit approval before rendering the final PDF.

### Step 5 — Render PDF (with built-in verify gate)
- **Owner:** Claude
- **Needs:** `cerkl/skills/html-to-pdf/SKILL.md` (runs html-overflow-detector first).
- **Produces:** `output/<family>/<slug>-YYYY-MM-DD.pdf` (only on verify PASS).

On detector FAIL, remediate in order — stop at the first tier that resolves it:

**Tier A — type shrink (automatic).** Add `style="--body-size: 15px"` to the overflowing `.page` div; re-render. Still failing with overrun ≤ ~30px → `14px` (floor). (The reference scales dense components via `calc(var(--body-size) - Npx)`, so this shrinks grid/bullet/stat bodies too.)

**Tier B — variant swap (automatic).** `.feature-grid.cols-3 → cols-2 → cols-1`; `.bullet-grid.cols-4 → cols-3 → cols-2`. Usually means fewer items.

**Tier C — escalate (only after A + B).** Surface the overrun verbatim and wait — don't auto-pick:
```
The {component} is {overrun_px}px past page bottom after Tier-A + Tier-B.
Section: "{snippet}"
Options: 1. Trim to ≤ {budget} words  2. Split onto a new page  3. Drop {item N}
```

There is no "ship the broken PDF" path — the PDF doesn't exist until verify PASS. Eyeball the actual PDF bottom edge after PASS.

### Step 6 — Harvest + handoff
- **Owner:** Claude
- **What to do:**
  1. Reconcile the `.md` source to match what shipped; add a brief remediation-note comment near any section you remediated.
  2. **Harvest only reusable process improvements.** If this build introduced a net-new component, reusable fix, or durable decision rule, write it back into the standing guidance so the next build inherits it:
     - New component → add it to `reference-one-pager.html` + the Component index here.
     - Verified competitor fact → `shared/competitors.md`.
     - Process rule → revise the relevant principle, recipe, budget, or component note. Avoid dated logs unless the chronology itself matters.
  3. State in chat what shipped and the next step. PA derives activity from git log — no update blocks.

---

## Recipe picker — start here

Use these as starting points, not templates. Default to number-led (or tension-led), mixed-component, asset-rich layouts, then adjust to the brief.

| Recipe | When | Composition |
|---|---|---|
| **Recap** | post-webinar/event | hero-cover → number-row (3) → callout-card → editorial-2col → cta-strip |
| **Comparison** | versus-competitor, before/after | hero-compact → vs-compare → feature-grid.cols-2 → logo-strip → cta-strip |
| **Framework** | thought-leadership, methodology | hero-cover OR display-h1 → callout-card (thesis) → diagram-flow → framework-grid → cta-strip |
| **Sales leave-behind** | handouts, conference takeaways | hero-compact → number-row (3) → feature-grid.cols-3 (6) → pill-row → cta-strip |
| **Product / package overview** | Foundations / Omni AI tier sheets, flagship product pages | Usually starts with hero-mockup → icon-row (5-6 features/channels) → vs-compare and/or check-list → stat-band → gradient-cta. Keep hero copy and feature cells short; let the mockup, icons, and checklist do the work. |
| **Product / positioning overview** | partner pitch, category narrative, belief-shift piece | hero or hero-mockup → tension/callout → architectural diagram or value-row → feature-grid.cols-2 → use-case strip → footer/CTA. *May lead with a tension instead of a number.* Precedent: omni-ai-exo-2026-06-15 |
| **IT pre-meeting** | stakeholder pre-call | hero-compact → grid-2 (purpose) → pill-row → bullet-grid.cols-4 → footer |
| **Guide chapter** | long-form interior | running-header → display-h1 → callout-card (thesis) → icon-row-list → footer |
| **Competitive battlecard** (landscape) | head-to-head vs. a named competitor | hero → criterion-matrix (criterion rail \| Competitor \| Cerkl·plan) → CWR strip (Crawl/Walk/Run) → brand-gradient summary band. **Framework-led, letter LANDSCAPE.** Working reference: `output/battlecards/cerkl-vs-viva-amplify-v2-2026-05-29.html` (+ engage-v2). *A formal landscape reference is pending — see Future work.* |

**Co-branded hero (partner one-pagers).** Single-row inline: `Cerkl Broadcast lockup | divider | H1 | spacer | partner logo`. Keep hero-compact ~70px. **Anti-pattern: stacked-column hero** (logos row + H1 row + lead para) — adds ~80px and is a common cause of single-page overflow. H1 compresses to ≤4 words; partner logo ~28–32px; keep partner logos in `one-pagers/assets/` (`../../assets/<logo>.png`).

---

## Component index (plan from this; load the reference HTML only for detail)

**Heroes** — `hero-cover` (full-page cover) · `hero-compact` (wordmark + H1 band) · *hero-mockup* (hero + embedded product screenshot/device mockup — see Future work).
**Chrome** — `running-header` · `footer`.
**Headings** — `display-h1` (chapter opener).
**Content** — `feature-grid.cols-3/2/1` · `icon-row-list` · `bullet-grid.cols-4/3/2` · `editorial-2col` · `image-card` · *check-list* (green-check included-list, 2-col — see Future work).
**Number-led & diverse** — `stat-panel` (+ `.violet/.ruby/.forest`) · `number-row.cols-2/3/4` (+ icons) · `bar-compare` / *vs-compare* (VS-pill comparison — see Future work) · `diagram-flow` · `framework-grid.cols-2/3`.
**Utility** — `pill-row` · `logo-strip.logos/.names` · `cta-strip` / *gradient-cta* (full-bleed band + arrow button) · `callout-card` (quote) / `callout` (problem/tension).
**Landscape battlecard** — `criterion-matrix` · `cwr` (Crawl/Walk/Run strip) · `summary-band` (brand-gradient). *Self-contained in the v2 viva files until formalized.*
**Architectural (from omni-ai-exo)** — `engine` (dark orchestration diagram w/ chips + numbered steps) · `value-row` (4-col economics) · `facets` (3 problem articulations) · `uses` (use-case pill strip). *Proven; pending harvest into the reference.*

**Variant picker — feature grids**

| Items × words/item | Use |
|---|---|
| 6 × ≤55 | `.feature-grid.cols-3` |
| 4 × 60–95 | `.feature-grid.cols-2` |
| 3–6 × 90–160 | `.feature-grid.cols-1` |
| Bigger | split or trim |

**Variant picker — bullet grids**

| Cols × bullets × words/bullet | Use |
|---|---|
| 2 × 5–8 × 15–30 | `.bullet-grid.cols-2` |
| 3 × 4–6 × 12–24 | `.bullet-grid.cols-3` |
| 4 × 3–5 × 10–18 | `.bullet-grid.cols-4` |

---

## Component budgets — quick reference

These are planning budgets, not hard creative limits. Authoritative copy lives in the top comment of `reference-one-pager.html` — **keep the two in sync** (the HTML's `calc()` scaling must match these).

| Component | Budget |
|---|---|
| Cover hero title | ≤6 words |
| Cover hero subtitle | ≤18 words |
| Hero mockup title | ≤7 words |
| Hero mockup subtitle | ≤16 words |
| Hero mockup body | 35–60 words |
| Compact hero H1 | ≤4 words |
| Display H1 (chapter opener) | ≤14 words |
| Running header guide title | ≤8 words |
| Feature grid (cols-3) | 6 cells × 30–55 words |
| Feature grid (cols-2) | 4 cells × 60–95 words |
| Feature grid (cols-1) | 3–6 cells × 90–160 words |
| Icon row | 5–6 cells × title ≤4 words + body 8–16 words |
| Icon-row list | 3–6 rows × 35–70 words |
| Bullet grid (cols-4) | 4 cols × 3–5 bullets × 10–18 words |
| Bullet grid (cols-3) | 3 cols × 4–6 bullets × 12–24 words |
| Bullet grid (cols-2) | 2 cols × 5–8 bullets × 15–30 words |
| Editorial 2-col | H2 ≤6 words, body 70–120 words |
| Image card | H3 ≤5 words, body 30–90 words |
| Stat panel | stat ≤4 chars, label ≤14 words, body 25–50 words |
| Number row | 2–4 cells × stat ≤5 chars + label ≤9 words + sub ≤16 words |
| Bar / vs compare | header ≤6 words, 3–6 rows × row-label ≤4 words |
| Check-list | 2 cols × 7–11 items × item ≤5 words; optional one-line value note ≤10 words |
| Stat band | 3–4 stats × stat ≤6 chars + label ≤9 words |
| Diagram flow | 3–5 steps × label ≤4 words + desc ≤16 words |
| Callout card | quote ≤30 words + attribution ≤8 words |
| Framework grid | 2×2 or 3×3 × quad title ≤4 words + body ≤16 words; axis labels ≤4 words |
| Pill row | ≤8 pills × 1–3 words |
| CTA strip | pitch h3 ≤6 words, body 40–65 words + stat panel |

---

## Render-verify-remediate loop (the contract)

```
Step 3 ──► Step 4 (render+self-review) ──► SHARE ─approve─► Step 5 ─PASS─► Step 6 (done)
                                                              │
                                                              └─FAIL─► Tier A ──► re-render ─PASS─► Step 6
                                                                       Tier B ──► re-render ─PASS─► Step 6
                                                                       Tier C ── escalate ── ask user
```

The PDF does not exist until verify PASS. A FAIL stops the pipeline; only remediation advances it.

---

## Proven patterns

These are standing heuristics distilled from prior one-pagers and reference PDFs. Use them to make better calls; do not treat them as a chronology or rigid checklist.

- **Avoid "single template, infinite content."** Pick components and variants based on the job, then stay close to the budgets. If content does not fit, change the structure or trim the message; don't ask CSS to rescue a bad information design.
- **Use the right lead.** Recaps and sales leave-behinds usually benefit from a number-led opening. Positioning pieces often work better with a tension-led opening. Package overview sheets usually work best with a product mockup and tier badge.
- **Make package sheets modular.** The strongest package-overview shape is a compact value prop, product/device mockup, tier badge, 5-6 icon features, comparison or included checklist, stat band, and clear CTA band. Keep each cell short so the page feels rich without becoming exhausting.
- **Choose theme by legibility.** Dark cobalt works well for polished, contained package sheets and architectural sections. Light backgrounds usually serve product screenshots, analytics, and omnichannel proof better.
- **Use one badge with a job.** A circular or pill badge can carry a takeaway ("AI-powered", "built for internal communicators", "free forever"). One is useful; several become decoration.
- **Let the CTA carry reassurance.** The bottom band can include action, URL, and 2-3 micro-points such as free forever, no setup fees, no contract, enterprise-ready, or easy to use.
- **Use grid for print layout.** Chrome print handles CSS Grid page tracks more predictably than flex expansion. Avoid `grid-auto-rows: 1fr` when content can exceed the row; use `minmax(min-content, 1fr)`.
- **Use standard print margins.** Prefer `@page { margin: 0.5in 0.6in }` plus printable-area page sizing over `@page margin: 0` with all spacing on the page div.
- **Prefer landscape for true head-to-head battlecards.** A 6-criterion framework, Crawl/Walk/Run strip, and summary band need horizontal room.
- **Inspect local PDF references directly.** If the user points to local PDFs, render a high-res Quick Look thumbnail (`qlmanage -t -s 1600`) and inspect it before asking for screenshots.

---

## Future work

### Components to harvest into `reference-one-pager.html`
- **hero-mockup** — hero with an embedded real product screenshot/device mockup (the single biggest visual-appeal driver). Full laptop+phone composites are likely Canva/Figma territory; in HTML, embed a clean screenshot or simple framed mockup rather than faking complex 3D.
- **package-badge** — one circular or pill badge that carries the takeaway ("AI-powered", "built for internal communicators", "free forever"), not decoration.
- **icon-row** — 5-6-column feature/channel row using real Brand Icons (replaces placeholder circles).
- **vs-compare** — comparison block with circular "VS" pills + paired icons (a livelier `bar-compare`).
- **check-list** — 2-column green-check "everything included" block; keep item labels short.
- **gradient-cta** — full-bleed band with arrow button, URL, and 2-3 micro-badges/reassurance points.
- **stat-band** — `number-row` variant with brand icons per stat.
- **dark-theme variant** — formalize the dark cobalt section pattern (`--onDark` vars + texture) from omni-ai-exo.
- **engine / value-row / facets / uses** — fold the proven omni-ai-exo components in.

### System
- **Tune default `--body-size` for the richer density** (open, render-validated). Budgets in `reference-one-pager.html` are synced to the bumped numbers (2026-06-18); the font-size `calc()` scaling was left as-is since the Tier-A/verify loop handles fit. If rich-default renders routinely need Tier A out of the gate, consider dropping the default body size 16px → 15px.
- **Formalize the landscape battlecard reference** (`reference-battlecard-landscape.html`): letter-landscape `@page`, criterion-matrix / cwr / summary-band with budgets, brand-gradient + cobalt-column-cap + `print-color-adjust` baked in. Until then, the `cerkl-vs-viva-*-v2-2026-05-29` files are the working reference.
- **Persist verified competitor facts** to `shared/competitors.md` (Viva Engage + Amplify: paid-Viva licensing, 200-recipient publication cap, distribution-group-breaks-open-rate analytics, aggregate-only measurement) so each battlecard stops re-researching.
- **Wire `cerkl/marketing/skills/image/SKILL.md`** for hero image generation when no real asset fits.
- **Print-mode page-count check** — assert `.page` div count == PDF page count after render.
- **`--max-remediations=N`** on html-to-pdf so Tier A/B can run autonomously.
