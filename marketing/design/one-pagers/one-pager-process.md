# One-Pager

> Produce a print-ready PDF from a brief. Output: a `.{md,html,pdf}` trio under `output/<family>/` (e.g. `output/battlecards/<slug>-YYYY-MM-DD.*`). Letter-portrait by default; competitive battlecards are letter-landscape.

## Trigger

- "Let's make a one-pager"
- "Draft a one-pager for [event / meeting / topic]"
- "We need a Broadcast overview / IT pre-meeting / [topic] handout"
- "Write the one-pager for [partner / webinar / sales meeting]"

## Inputs (single intake block — ask all at once)

Before drafting anything, ask:

1. **Purpose** — what is this one-pager for? (sales meeting, webinar handout, event download, IT pre-call, long-form guide)
2. **Primary reader** — role, industry, company size, where in the buying journey
3. **Single goal** — the one belief shift or action you want the reader to take
4. **Proof points** — specific stats, case studies, customer quotes that must be included
5. **Deadline / in-hands date**
6. **Slug for filename** — short kebab-case (e.g., `broadcast-it-premeeting`, `newsletter-guide-foundations`)

If the user gives multiple goals (step 3), flag the conflict and ask them to pick a primary. If they can't supply proof points (step 4), pull candidates from `shared/competitors.md` / case studies after step 1 and confirm.

## Context to load

- `/Users/travisfoster/claude-code/cerkl/shared/company-info.md`
- `/Users/travisfoster/claude-code/cerkl/shared/icp.md`
- `/Users/travisfoster/claude-code/cerkl/shared/competitors.md`
- `/Users/travisfoster/claude-code/cerkl/shared/broadcast.md`
- `/Users/travisfoster/claude-code/cerkl/marketing/design/CONTEXT.md`
- `/Users/travisfoster/claude-code/cerkl/marketing/design/branding-assets/Brand Guidelines/brand-guidelines.md`

If the one-pager names specific Broadcast features (Audience Manager, Email Blasts, Insights, etc.), also load the matching deep-dive(s) from `/Users/travisfoster/claude-code/cerkl/shared/features/`:
- `ai-personalization.md` · `analytics-insights.md` · `audience-segmentation.md`
- `content-management.md` · `email-blasts.md` · `omni-channel-publishing.md`
- `pulse-surveys-acknowledgments.md`

(Per [PRINCIPLES.md #4](../../../PRINCIPLES.md), this list is authoritative for this scope — parent loads do not apply unless re-listed here.)

## Output path convention

```
cerkl/marketing/design/one-pagers/output/<family>/<slug>-YYYY-MM-DD.md
cerkl/marketing/design/one-pagers/output/<family>/<slug>-YYYY-MM-DD.html
cerkl/marketing/design/one-pagers/output/<family>/<slug>-YYYY-MM-DD.pdf
```

**Folder layout.** Artifacts live in `output/`, grouped by family: `output/battlecards/` (competitor comparisons; `…/research/` holds supporting notes), `output/recaps/` (webinar/event), `output/leave-behinds/` (sales handouts). Add a new family folder when a new artifact type recurs. Shared input assets — partner logos, CS source images, screenshots — live in `one-pagers/assets/`. The `reference-one-pager.html`/`.pdf` template stays at the `one-pagers/` root (the skills path to it there).

The `.pdf` is the deliverable. The `.md` and `.html` are the audit trail — keep them. Revisions are 100× easier when the markdown source is on disk.

---

## Workflow phases (pause at each gate)

Run the build in three phases with an explicit **pause at each gate**. The framing of a competitive/sales one-pager is contingent on context and facts that often arrive mid-build — pausing prevents the re-work we hit when we drafted before verifying.

**Phase 1 — Pull & intake.** Gather the brief (intake block above) *and* the soft context from Sales/CS: the specific objections raised in the room, stakeholder sentiment, and what the prospect already owns or values. Pull any competitor/product facts you'll need.

**▸ Gate 1 — Verify against research & source of truth (PAUSE).** Reconcile every factual claim against `shared/broadcast.md` (Cerkl) and verified research (competitors → Microsoft Learn / official docs, captured in `shared/competitors.md`). **The source of truth wins over any external or Sales/CS material** — even trusted internal collateral has shipped errors (a CS battlecard listed SMS + digital signage as Cerkl channels; neither is real). Scope every capability claim to the exact plan/tier being pitched. Do not start drafting until claims are verified.

**Phase 2 — Build & refine (HTML).** Draft → render HTML → iterate on the HTML with feedback and fine-tuning (see *Iteration workflow* below). Do **not** render the PDF during this phase, and don't re-sync the `.md` on every change.

**▸ Gate 2 — Sign-off (PAUSE).** Get explicit approval of the HTML before rendering.

**Phase 3 — Render & finalize.** Render the PDF through the verify gate, confirm it (incl. a human eyeball of the *actual PDF*, not just the detector), then reconcile the `.md` source to match what shipped.

## Principles (competitive battlecards & one-pagers)

- **Build prospect-agnostic first, personalize last.** Default to channel- and client-agnostic copy; layer account specifics (logo, name, "their goal") as a final optional pass. (We built TMNAS-specific and had to strip it back out — reverse that order.)
- **Pull objections & sentiment from Sales/CS, not just facts.** The framing-defining steers ("leadership dislikes 'social media'," "wary of algorithms," "why not use what's already in our license") were political/emotional and lived only in the reps' heads.
- **Verify every claim against the source of truth** — including Sales/CS materials (see Gate 1). Adopt their *voice and structure*; trust nothing factual until reconciled with `broadcast.md`.
- **Scope claims to the tier being pitched.** Foundations vs. Foundations+ vs. Omni AI differ (e.g., mobile app / microsites / cross-channel publishing are Omni AI–only). Tier-inaccurate claims are an easy own-goal.
- **Position honestly and diplomatically.** Use an amber "limited" mark (not a red ✗), concede the competitor's genuine strengths (e.g., "Engage is great for community"), and never attack a dimension the buyer has already bought (the cost angle backfires once they own the competitor).
- **Print-fidelity checklist.** (1) `print-color-adjust: exact` on any colored/gradient background, or Chrome drops it in the PDF. (2) Never pin content to the page edge — leave a bottom margin (an edge-pinned footer clipped in print even though the detector passed). (3) The overflow detector is necessary but not sufficient — eyeball the actual PDF's bottom edge.
- **A battlecard is a reusable system, not a one-off.** The 6-criterion framework (Consistency · Prioritization · Insights · Reach · AI · Total Value) is competitor-agnostic — it spins up Staffbase, Simpplr, Workvivo, etc. Verified competitor facts belong in `shared/competitors.md` so they're reused, not re-researched.

---

## Steps

### Step 1 — Intake + ICP cross-check
- **Owner:** Joint
- **Needs:** the intake block above; `shared/icp.md` already loaded
- **Inputs:** user's answers
- **Produces:** locked brief (goal, audience, proof points) — in conversation, not a file
- **What to do:** Ask the 6 intake questions in one turn. Cross-reference primary reader against ICP; flag misalignment if any. Don't proceed to drafting until the single goal is unambiguous.

### Step 2 — Pick layout & variants
- **Owner:** Claude
- **Needs:** reference catalog at `cerkl/marketing/design/one-pagers/reference-one-pager.html` (read the top comment block — it lists every component, its variants, and word budgets per variant)
- **Inputs:** locked brief from Step 1
- **Produces:** a section outline naming the component variants to use (e.g., "hero-compact → number-row (3 stats) → callout-card → editorial-2col → cta-strip")
- **What to do:** Start at the **recipe picker** below — name the recipe that fits the brief, then customize from there. Only drop to the **variant picker** for dense components within a recipe. Present the outline to the user for approval before drafting.

**Recipe picker — start here (default to number-led, mixed-component layouts)**

| Recipe | When to use | Composition |
|---|---|---|
| **Recap** | post-webinar, post-event recaps | hero-cover → number-row (3 stats) → callout-card → editorial-2col → cta-strip |
| **Comparison** | versus-competitor, before/after | hero-compact → bar-compare → feature-grid.cols-2 → logo-strip → cta-strip |
| **Framework** | thought-leadership, methodology | hero-cover OR display-h1 → callout-card (thesis) → diagram-flow (5 steps) → framework-grid (2×2) → cta-strip |
| **Sales leave-behind** | in-person handouts, conference takeaways | hero-compact → number-row (3 stats) → feature-grid.cols-3 (6 features) → pill-row → cta-strip |
| **IT pre-meeting** | stakeholder pre-call brief | hero-compact → grid-2 (purpose) → pill-row → bullet-grid.cols-4 → footer |
| **Guide chapter** | long-form interior page | running-header → display-h1 → callout-card (thesis) → icon-row-list → footer |
| **Competitive battlecard** (landscape) | head-to-head vs. a named competitor, scored on buyer criteria | hero (agnostic or co-branded) → criterion-matrix (criterion rail \| Competitor \| Cerkl·plan) → slim diagram-flow (Crawl/Walk/Run) → brand-gradient summary band. **Framework-led, not number-led; letter LANDSCAPE.** Working reference: `output/battlecards/cerkl-vs-viva-amplify-v2-2026-05-29.html` + `…-engage-v2-…` |

**Co-branded hero (partner one-pagers).** When the brief calls for a partner / co-marketing logo alongside the Cerkl Broadcast lockup (MSP partnerships, prospect pre-meetings, customer handouts):

- **Layout: single-row inline.** `Cerkl Broadcast lockup | divider | H1 | spacer | partner logo`. Hero-compact stays ~70px tall.
- **Anti-pattern: stacked-column hero** (logos row + H1 row + lead paragraph). Adds ~80px to the hero — the single biggest cause of single-page overflow in dense recipe shapes (learned the hard way on allcore-msp-premeeting-2026-05-22).
- **H1 budget compresses to ≤4 words.** Logos eat horizontal real estate. If the brief locks a longer title, drop H1 font-size from the default 28px to 20–22px and let it run on a single line.
- **Partner logo height:** ~28–32px to roughly match the 26px Cerkl medium lockup. Tune by eye.
- **Partner logo asset location:** keep partner/co-brand logos in `one-pagers/assets/` (alongside `tmnas-logo.png`, `allcore-logo.png`). From an `output/<family>/` HTML, reference them as `../../assets/<logo>.png`. (Anticipate `sales/prospects/<account>/` folders once that channel matures.)

**Anti-pattern: stacking two of the same component.** Two `feature-grid.cols-2` back-to-back, or two `bullet-grid` back-to-back, reads as a textbook page. Default to ≥3 distinct component types per body page. If a brief seems to call for stacking, propose a recipe with mixed components first; only stack with explicit user sign-off.

**Lead with a number.** Default opening component below the hero: `number-row` or `stat-panel`, not a prose block. Where there's a quantitative anchor in the brief, surface it visually.

**Variant picker — feature grids**

| Items × words/item | Use |
|---|---|
| 6 items × ≤45 words | `.feature-grid.cols-3` |
| 4 items × 50–85 words | `.feature-grid.cols-2` |
| 3–6 items × 90–150 words | `.feature-grid.cols-1` |
| Anything bigger | Tier C — split or trim |

**Variant picker — bullet grids**

| Cols × bullets × words/bullet | Use |
|---|---|
| 2 × 5–8 × 12–25 words | `.bullet-grid.cols-2` |
| 3 × 4–6 × 10–20 words | `.bullet-grid.cols-3` |
| 4 × 3–5 × 8–16 words | `.bullet-grid.cols-4` |

### Step 3 — Draft copy in markdown
- **Owner:** Claude
- **Needs:** `cerkl/marketing/skills/copywriting/SKILL.md` (auto-triggers on copy work). For sales-enablement angles, also `cerkl/marketing/skills/sales-enablement/SKILL.md`.
- **Inputs:** approved outline from Step 2; loaded brand context (incl. `shared/broadcast.md` and any relevant `shared/features/*.md`)
- **Produces:** `output/<family>/<slug>-YYYY-MM-DD.md` — markdown copy with one section per component, ordered to match the outline, written within each variant's word budget
- **What to do:** Write Cerkl-voice copy. Mark each section with an HTML comment naming its target component (e.g., `<!-- component: feature-grid.cols-3 -->`) so md-to-html knows what to render. Stay at or under each variant's word budget — if a section runs over, pick a roomier variant in Step 2 rather than forcing CSS to absorb it.

Before writing, skim the most recent file in the matching `output/<family>/` folder whose recipe matches yours — it's the working precedent for the markdown→HTML convention the renderer parses (e.g., `output/recaps/matt-frost-recap-2026-05-19.md` for hero + number-row + callout + cta shapes; `output/leave-behinds/allcore-msp-premeeting-2026-05-22.md` for co-branded hero + feature-grid.cols-2 shapes; `output/battlecards/cerkl-vs-viva-amplify-v2-2026-05-29.html` for the landscape competitive battlecard).

**Asset paths** — when the outline includes:
- `.logo-strip.logos` → reference files from `cerkl/marketing/design/branding-assets/Customer Logos/`. Current inventory (2026-05-15): Church & Dwight, Novant Health, UC, Paycor, Roivant, St. Elizabeth. **Output HTML now lives in `output/<family>/` (one level deeper than the old `pdfs/`), so `<img>` src is `../../../branding-assets/Customer Logos/<filename>.png`** (three `../`; URL-encode spaces). If the brief names a customer not in the folder, fall back to `.logo-strip.names` OR flag for asset acquisition.
- `.photo-ph` (hero / image cards) → `cerkl/marketing/design/branding-assets/Cerkl Photography/INDEX.md` — read the searchable per-photo index and pick from there (Office / Culture / Group Photos subfolders)
- `.wordmark-ph` (Broadcast logo) → `cerkl/marketing/design/branding-assets/Broadcast/Cerkl Broadcast Horizontal Lockup/`

### Step 4 — Render HTML
- **Owner:** Claude (sub-agent OK to keep parent context light)
- **Needs:** `cerkl/skills/md-to-html/SKILL.md` with `artifact-type=one-pager`
- **Inputs:** `output/<family>/<slug>-YYYY-MM-DD.md`
- **Produces:** `output/<family>/<slug>-YYYY-MM-DD.html`
- **What to do:** Invoke md-to-html with `artifact-type=one-pager`. The skill reads `cerkl/marketing/design/one-pagers/reference-one-pager.html` (not the daily-recap or deep-dive references) and composes HTML using the variant tags in the markdown source.

**Asset substitution checklist — verify before returning the HTML.** Two prior renders shipped the reference's CSS placeholder squares instead of the real brand assets (matt-frost-recap, foundations-post-webinar). The reference uses ::before pseudo-elements as visual stand-ins; they only swap out when the markdown source includes an actual `<img>` and the renderer keeps it.

| Slot | Reference placeholder | Required substitution |
|---|---|---|
| `.hero-cover .wordmark-ph` | cobalt square + "Broadcast" text | `<img src="../../../branding-assets/Broadcast/Cerkl Broadcast Horizontal Lockup/Medium (160px)/cerkl_broadcast_horizontal_lockup_full_color_medium.png">` |
| `.hero-cover .photo-block` | "[ HERO PHOTO ]" gradient | `<img src="../../../branding-assets/Cerkl Photography/<subfolder>/<file>.jpg">` filling the block |
| `.hero-compact .wordmark-ph` | cobalt square + "Broadcast" text | Same 160px lockup OR 80px small, depending on hero size |
| `.footer .brand` | "Cerkl" text | `<img src="../../../branding-assets/Broadcast/Cerkl Broadcast Horizontal Lockup/Small (80px)/cerkl_broadcast_horizontal_lockup_full_color_small.png">` |
| `.image-card .photo-ph` | "[ PHOTO ]" gradient | `<img>` per Step 3 asset paths (or leave empty if the card is decorative) |

If any required slot is still showing a placeholder in the rendered HTML, re-render with the substitution explicit in the markdown source (see matt-frost-recap-2026-05-19.md for an example of the wordmark/photo path comments). Do not advance to Step 5 with placeholders in the customer-facing artifact.

### Step 5 — Render PDF (with built-in verify gate)
- **Owner:** Claude
- **Needs:** `cerkl/skills/html-to-pdf/SKILL.md`
- **Inputs:** `output/<family>/<slug>-YYYY-MM-DD.html`
- **Produces:** `output/<family>/<slug>-YYYY-MM-DD.pdf` (only if verify gate PASS)
- **What to do:** Invoke html-to-pdf. The skill runs html-overflow-detector first. If detector FAIL → drop to Step 6 (remediate). If PASS → PDF is written; continue to Step 7.

### Step 6 — Remediate (only on verify FAIL)
- **Owner:** Claude (Tiers A, B); Joint (Tier C)
- **Needs:** detector output from Step 5 (selectors + overrun_px + text snippets)
- **Inputs:** failing HTML, detector JSON
- **Produces:** updated HTML; loop back to Step 5

Apply in order — stop at the first tier that resolves the overflow:

**Tier A — type shrink (automatic)**
Add `style="--body-size: 15px"` to the overflowing `.page` div. Re-render PDF. If detector still FAIL with overrun ≤ ~30px, shrink to `14px` (the floor). Re-render.

As of 2026-05-19, the reference (reference-one-pager.html) scales the dense component body sizes via `calc(var(--body-size) - Npx)` — so `--body-size:15px` actually shrinks feature-grid cells, bullet-grid items, stat-panel bodies, etc., not just the bare body text. If you're working from an older snapshot of the reference, Tier A is a no-op on the dense components and you should jump straight to Tier B.

**Tier B — variant swap (automatic)**
If detector still FAIL after Tier A, the section is genuinely too dense for its current variant. Swap:
- `.feature-grid.cols-3` → `.feature-grid.cols-2`
- `.feature-grid.cols-2` → `.feature-grid.cols-1`
- `.bullet-grid.cols-4` → `.bullet-grid.cols-3` → `.bullet-grid.cols-2`
This typically requires fewer items in the grid; if the brief insists on the count, escalate to Tier C.

**Tier C — escalate to user (only after A + B exhausted)**
Surface the overrun verbatim:
```
The {component} is {overrun_px}px past page bottom after Tier-A + Tier-B remediation.
Section: "{text snippet}"
Options:
  1. Trim the section to ≤ {budget} words
  2. Split this section onto a new page
  3. Drop {item N} from the grid
```
Wait for user direction; do NOT auto-pick.

Record what was tried in the .md source as an HTML comment near the affected section so a future reader knows what remediation was applied (and why).

### Step 7 — Push-update to PA if applicable
- **Owner:** Claude
- **Needs:** [marketing/CLAUDE.md Push-Update Protocol](../../CLAUDE.md)
- **Inputs:** the project this one-pager serves (webinar event folder, sales handoff, etc.)
- **Produces:** an update block appended to the relevant `personal-assistant/projects/<project>.md`
- **What to do:** If the one-pager was created for a tracked project (webinar, partnership, sales hand-off), append the standard update block. Skip if it's standalone.

---

## Render-verify-remediate loop (the contract)

```
Step 3 ──► Step 4 ──► Step 5 ─PASS─► Step 7 (done)
                       │
                       └─FAIL─► Step 6 (Tier A) ──► Step 5 ─PASS─► Step 7
                                Tier B ────────────► Step 5 ─PASS─► Step 7
                                Tier C ── escalate ── ask user
```

The PDF does not exist until verify PASS. A FAIL stops the pipeline; only the remediation loop can advance it. There is no "ship the broken PDF" path.

## Component budgets — quick reference

Read in detail at the top of `reference-one-pager.html`. Summary:

| Component | Budget |
|---|---|
| Cover hero title | ≤6 words |
| Cover hero subtitle | ≤14 words |
| Compact hero H1 | ≤4 words |
| Display H1 (chapter opener) | ≤14 words |
| Running header guide title | ≤8 words |
| Feature grid (cols-3) | 6 cells × 25–45 words each |
| Feature grid (cols-2) | 4 cells × 50–85 words each |
| Feature grid (cols-1) | 3–6 cells × 90–150 words each |
| Icon-row list | 3–6 rows × 35–60 words each |
| Bullet grid (cols-4) | 4 cols × 3–5 bullets × 8–16 words |
| Bullet grid (cols-3) | 3 cols × 4–6 bullets × 10–20 words |
| Bullet grid (cols-2) | 2 cols × 5–8 bullets × 12–25 words |
| Editorial 2-col | H2 ≤6 words, body 60–100 words |
| Image card | H3 ≤5 words, body 30–80 words |
| Stat panel | stat ≤4 chars, label ≤14 words, body 20–40 words |
| Number row | 2–4 cells × stat ≤5 chars + label ≤8 words + sub ≤14 words |
| Bar compare | header ≤6 words, 3–5 rows × row-label ≤4 words + 1–2 bars per row |
| Diagram flow | 3–5 steps × label ≤4 words + desc ≤14 words |
| Callout card | quote ≤25 words + attribution ≤8 words |
| Framework grid | 2×2 or 3×3 matrix × quad title ≤4 words + body ≤14 words; axis labels ≤4 words each |
| Pill row | ≤8 pills × 1–3 words |
| CTA strip | pitch h3 ≤6 words, body 35–55 words + stat panel |

## Future work

- Wire to `cerkl/marketing/skills/image/SKILL.md` for hero photo generation when no Cerkl photography fits the brief.
- Add evals/ folder with 2–3 gold-standard examples to anchor the variant picker's choices.
- Print-mode page-count check: assert `<.page> div count == PDF page count` after render (catches the rare class of overflows the screen detector misses).
- A `--max-remediations=N` flag on html-to-pdf so Tier A/B can run autonomously without going back through this orchestrator.
- **Formalize the landscape competitive-battlecard reference** (a sibling to `reference-one-pager.html`: letter-landscape `@page`, the battlecard/criterion-rail/summary-band/CWR-strip components with content budgets, the brand-gradient + solid-cobalt-column-cap + `print-color-adjust` rules baked in) and an agent skill — "spin up a battlecard for competitor X" → pull verified facts → fill the 6-criterion framework → render-verify. Until then, the `cerkl-vs-viva-*-v2-2026-05-29` files are the working reference.
- **Persist verified competitor facts** (Viva Engage + Amplify: paid-Viva licensing, 200-recipient publication cap, distribution-group-breaks-open-rate analytics, aggregate-only measurement) into `shared/competitors.md` — they aren't there yet, so each use re-researches them.

## Iteration workflow (drafting → final)

After the first full md → html → pdf pass, **iterate on the `.html` directly.** Travis reviews and gives feedback on the rendered HTML/PDF, so apply copy tweaks, layout changes, logo swaps, and remediation to the HTML and re-run the overflow/PDF gate each round. **Defer reconciling the `.md` source** (and writing remediation-note comments into it) until the draft is final/approved — the `.md` is the audit trail; it needs to match the shipped PDF at the end, not on every intermediate edit. Don't trigger a fresh md-to-html sub-agent render for small iterative changes.

## Learnings (append-only)

### 2026-05-15 — First build

- **The "single template, infinite content" pattern is a trap.** Fixed initially with content budgets + layout variants per component, plus a render-verify-remediate loop. Without verify, print-mode overflow is invisible until a human looks.
- **Chrome's print engine collapses flex `flex: 1` children silently.** CSS Grid row tracks (`auto 1fr`) survived pagination; flex did not. The reference uses grid for the page-level layout and flex only inside content containers.
- **`grid-auto-rows: 1fr` overlaps content** when rows are allocated less height than min-content. The fix is `minmax(min-content, 1fr)` — rows are at least content-tall, can stretch beyond if there's space.
- **`@page` margin: 0 + .page padding (the "all-margin-on-the-div" trick) fights Chrome's print engine.** Standard `@page { margin: 0.5in 0.6in }` + .page sized to printable area is the predictable path.
- **The detector is the contract.** Once it passed, the page genuinely fit — no more "looks OK to me" reviews that miss 25px of overflow. The Tier-A `--body-size: 15px` shrink was decisive on the page 2 overflow.
