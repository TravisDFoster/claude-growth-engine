# One-Pager

> Produce a print-ready letter-portrait PDF from a brief. Output: `pdfs/<slug>-YYYY-MM-DD.{md,html,pdf}` trio in this folder.

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
cerkl/marketing/design/one-pagers/pdfs/<slug>-YYYY-MM-DD.md
cerkl/marketing/design/one-pagers/pdfs/<slug>-YYYY-MM-DD.html
cerkl/marketing/design/one-pagers/pdfs/<slug>-YYYY-MM-DD.pdf
```

The `.pdf` is the deliverable. The `.md` and `.html` are the audit trail — keep them. Revisions are 100× easier when the markdown source is on disk.

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
- **Produces:** a section outline naming the component variants to use (e.g., "compact hero → feature-grid.cols-3 → cta-strip with ruby stat-panel → footer")
- **What to do:** Map the brief to components. Use the picker below for the dense components. Present the outline to the user for approval before drafting.

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
- **Produces:** `pdfs/<slug>-YYYY-MM-DD.md` — markdown copy with one section per component, ordered to match the outline, written within each variant's word budget
- **What to do:** Write Cerkl-voice copy. Mark each section with an HTML comment naming its target component (e.g., `<!-- component: feature-grid.cols-3 -->`) so md-to-html knows what to render. Stay at or under each variant's word budget — if a section runs over, pick a roomier variant in Step 2 rather than forcing CSS to absorb it.

**Asset paths** — when the outline includes:
- `.logo-strip.logos` → reference files from `cerkl/marketing/design/branding-assets/Customer Logos/`. Current inventory (2026-05-15): Church & Dwight, Novant Health, UC, Paycor, Roivant, St. Elizabeth. Output HTML lives in `pdfs/`, so `<img>` src is `../../branding-assets/Customer Logos/<filename>.png` (URL-encode spaces). If the brief names a customer not in the folder, fall back to `.logo-strip.names` OR flag for asset acquisition.
- `.photo-ph` (hero / image cards) → `cerkl/marketing/design/branding-assets/Cerkl Photography/` (Office / Culture / Group Photos subfolders)
- `.wordmark-ph` (Broadcast logo) → `cerkl/marketing/design/branding-assets/Broadcast/Cerkl Broadcast Horizontal Lockup/`

### Step 4 — Render HTML
- **Owner:** Claude (sub-agent OK to keep parent context light)
- **Needs:** `cerkl/skills/md-to-html/SKILL.md` with `artifact-type=one-pager`
- **Inputs:** `pdfs/<slug>-YYYY-MM-DD.md`
- **Produces:** `pdfs/<slug>-YYYY-MM-DD.html`
- **What to do:** Invoke md-to-html with `artifact-type=one-pager`. The skill reads `cerkl/marketing/design/one-pagers/reference-one-pager.html` (not the daily-recap or deep-dive references) and composes HTML using the variant tags in the markdown source.

### Step 5 — Render PDF (with built-in verify gate)
- **Owner:** Claude
- **Needs:** `cerkl/skills/html-to-pdf/SKILL.md`
- **Inputs:** `pdfs/<slug>-YYYY-MM-DD.html`
- **Produces:** `pdfs/<slug>-YYYY-MM-DD.pdf` (only if verify gate PASS)
- **What to do:** Invoke html-to-pdf. The skill runs html-overflow-detector first. If detector FAIL → drop to Step 6 (remediate). If PASS → PDF is written; continue to Step 7.

### Step 6 — Remediate (only on verify FAIL)
- **Owner:** Claude (Tiers A, B); Joint (Tier C)
- **Needs:** detector output from Step 5 (selectors + overrun_px + text snippets)
- **Inputs:** failing HTML, detector JSON
- **Produces:** updated HTML; loop back to Step 5

Apply in order — stop at the first tier that resolves the overflow:

**Tier A — type shrink (automatic)**
Add `style="--body-size: 15px"` to the overflowing `.page` div. Re-render PDF. If detector still FAIL with overrun ≤ ~30px, shrink to `14px` (the floor). Re-render.

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
| Pill row | ≤8 pills × 1–3 words |
| CTA strip | pitch h3 ≤6 words, body 35–55 words + stat panel |

## Future work

- Wire to `cerkl/marketing/skills/image/SKILL.md` for hero photo generation when no Cerkl photography fits the brief.
- Add evals/ folder with 2–3 gold-standard examples to anchor the variant picker's choices.
- Print-mode page-count check: assert `<.page> div count == PDF page count` after render (catches the rare class of overflows the screen detector misses).
- A `--max-remediations=N` flag on html-to-pdf so Tier A/B can run autonomously without going back through this orchestrator.

## Learnings (append-only)

### 2026-05-15 — First build

- **The "single template, infinite content" pattern is a trap.** Fixed initially with content budgets + layout variants per component, plus a render-verify-remediate loop. Without verify, print-mode overflow is invisible until a human looks.
- **Chrome's print engine collapses flex `flex: 1` children silently.** CSS Grid row tracks (`auto 1fr`) survived pagination; flex did not. The reference uses grid for the page-level layout and flex only inside content containers.
- **`grid-auto-rows: 1fr` overlaps content** when rows are allocated less height than min-content. The fix is `minmax(min-content, 1fr)` — rows are at least content-tall, can stretch beyond if there's space.
- **`@page` margin: 0 + .page padding (the "all-margin-on-the-div" trick) fights Chrome's print engine.** Standard `@page { margin: 0.5in 0.6in }` + .page sized to printable area is the predictable path.
- **The detector is the contract.** Once it passed, the page genuinely fit — no more "looks OK to me" reviews that miss 25px of overflow. The Tier-A `--body-size: 15px` shrink was decisive on the page 2 overflow.
