# Landing Page CRO Process

> One-line purpose: Audit a Cerkl landing page, generate hypotheses, design and run A/B tests in PostHog, ship winners.
> Output: per-page workspace at `landing-pages/<slug>/`, cross-page assets in `backlog.md` + `playbook.md`.

## Trigger
The parent `website/CLAUDE.md` routes here on phrases like:
- "Let's do a landing page audit"
- "Let's work on our landing pages"
- "A/B test [page URL]"
- "CRO [page URL]"
- Anything about a landing page on `cerkl.com/broadcast/*`

## Inputs (ask before starting, unless already provided)
- Page URL (must live under `cerkl.com/broadcast/`)
- New workspace or follow-up test on an existing one?
- If new: any prior data, customer feedback, or hypotheses Travis already has?

## Context to load
- /Users/travisfoster/claude-code/cerkl/shared/icp.md
- /Users/travisfoster/claude-code/cerkl/shared/broadcast.md
- /Users/travisfoster/claude-code/cerkl/shared/competitors.md
- /Users/travisfoster/claude-code/cerkl/shared/company-info.md
- /Users/travisfoster/claude-code/cerkl/marketing/CONTEXT.md
- /Users/travisfoster/claude-code/cerkl/marketing/website/CONTEXT.md
- /Users/travisfoster/claude-code/cerkl/marketing/website/landing-pages/tooling.md
- /Users/travisfoster/claude-code/cerkl/marketing/website/landing-pages/backlog.md
- /Users/travisfoster/claude-code/cerkl/marketing/website/landing-pages/playbook.md

(Per [PRINCIPLES.md #4](../../../PRINCIPLES.md), this list is authoritative for this scope — parent loads do not apply unless re-listed here.)

**Parallelization fallback:** if the runtime has the `Agent`/`Task` tool, dispatch parallel steps (3a–3c) as sub-agents in one message. If not, parallelize via multiple `WebFetch`/`WebSearch`/`Read` calls in a single message.

---

## Steps

### Step 1 — Scope + baseline
- **Owner:** Joint (Claude prompts, Travis provides numbers)
- **Parallelizable with:** —
- **Needs:** —
- **Inputs:** page URL; Travis pulls weekly traffic from GA4/PostHog
- **Produces:** `landing-pages/<slug>/baseline.md` — URL, weekly uniques, sessions, current CTA click rate, current Foundations signup rate, primary CTA description, top traffic sources, screenshot or text snapshot of current page
- **What to do:** Confirm `<slug>` (kebab-case of last URL segment). Create the page workspace folder if new. Capture baseline metrics. **If baseline tracking data is missing, halt and route to Step 2 first.**

### Step 2 — Tracking precheck
- **Owner:** Claude
- **Parallelizable with:** —
- **Needs:** /Users/travisfoster/claude-code/cerkl/marketing/skills/analytics-tracking/SKILL.md
- **Inputs:** `baseline.md`, `tooling.md` event naming convention
- **Produces:** `landing-pages/<slug>/tracking.md` — list of required PostHog events for this page (`lp_view`, `lp_cta_click`, `signup_started`, `signup_completed`), how each maps to the page's specific CTAs, gaps Travis must fix before any test launches
- **What to do:** Read `tooling.md` conventions. Enumerate the events this page needs. Surface any gaps as a checklist for Travis. **No test design proceeds until tracking is confirmed live.**

### Step 3a — Page-CRO audit (parallel)
- **Owner:** Claude (sub-agent if available)
- **Parallelizable with:** 3b, 3c
- **Needs:** /Users/travisfoster/claude-code/cerkl/marketing/skills/page-cro/SKILL.md
- **Inputs:** page URL (WebFetch), `baseline.md`
- **Produces:** `landing-pages/<slug>/audit.md` — friction inventory, observations ranked against CRO principles (clarity, distraction, friction, motivation, anxiety), initial hypothesis seeds
- **Sub-agent brief must state:**
  - **Inputs:** the page URL (WebFetch it directly), full text of `shared/broadcast.md` and `shared/icp.md` (paste verbatim into the brief)
  - **Output format:** friction inventory table + ranked observations + ≥3 hypothesis seeds tied to specific page elements
  - **Length cap:** ≤600 words
  - **Conventions:** cite specific page elements (hero headline, sub-hero, proof block, primary CTA copy, anchor link list); don't recycle generic CRO advice; absolute YYYY-MM-DD dates only

### Step 3b — Voice-of-customer pull (parallel)
- **Owner:** Claude (sub-agent if available)
- **Parallelizable with:** 3a, 3c
- **Needs:** /Users/travisfoster/claude-code/cerkl/marketing/skills/customer-research/SKILL.md
- **Inputs:** Cerkl ICP context, search for SMB pain about paying for internal email tools
- **Produces:** `landing-pages/<slug>/voc.md` — 5–10 verbatim quotes from SMBs about internal-email-tool pricing and value, source URLs, pain-language summary
- **Sub-agent brief must state:**
  - **Inputs:** `shared/icp.md` (full), `shared/broadcast.md` (full)
  - **Search targets:** Reddit r/sysadmin, r/InternalComms, r/internalcomms, G2 reviews of ContactMonkey/Mailchimp/Staffbase, TrustRadius reviews, LinkedIn posts about internal comms tooling
  - **Output format:** 5–10 quote excerpts with source URL + 1-paragraph pain-language summary
  - **Length cap:** ≤500 words
  - **Conventions:** verbatim quotes only, no paraphrasing; include source URL for every quote; absolute YYYY-MM-DD dates

### Step 3c — Competitive framing (parallel)
- **Owner:** Claude (sub-agent if available)
- **Parallelizable with:** 3a, 3b
- **Needs:** /Users/travisfoster/claude-code/cerkl/marketing/skills/competitor-alternatives/SKILL.md
- **Inputs:** `shared/competitors.md`, current page positioning (WebFetch)
- **Produces:** `landing-pages/<slug>/competitive.md` — positioning gap table (Cerkl vs each competitor on price, audience fit, calendar invites, omni-channel, etc.), what the current page is MISSING vs the gaps
- **Sub-agent brief must state:**
  - **Inputs:** `shared/competitors.md` (full), `shared/broadcast.md` (full), current page URL (WebFetch)
  - **Output format:** positioning gap table + a bulleted list of what the page does NOT currently say that the gap analysis suggests it should
  - **Length cap:** ≤500 words
  - **Conventions:** don't repeat `broadcast.md`'s "Sharpest summary" verbatim; surface what's MISSING from the current page; absolute YYYY-MM-DD dates

### Step 4 — Hypothesis synthesis + ICE scoring
- **Owner:** Claude
- **Parallelizable with:** —
- **Needs:** outputs from 3a, 3b, 3c
- **Inputs:** `audit.md`, `voc.md`, `competitive.md`
- **Produces:** `landing-pages/<slug>/hypotheses.md` — 5–10 hypotheses scored on Impact/Confidence/Ease, ranked by ICE. Append top 3 to `landing-pages/backlog.md` with the page's slug and `LP-NNN` IDs (next sequential).
- **What to do:** Each hypothesis follows the `ab-test-setup` framework: *"Because [observation], we believe [change] will cause [outcome] for [audience]. We'll know when [metric]."* Score 1–10 on each dimension, ICE = average. Sort highest-first. Surface the top hypothesis to Travis with a recommendation: "Test this one next?"

### Step 5 — Variant design (top hypothesis only)
- **Owner:** Claude
- **Parallelizable with:** —
- **Needs:** /Users/travisfoster/claude-code/cerkl/marketing/skills/copywriting/SKILL.md, /Users/travisfoster/claude-code/cerkl/marketing/skills/marketing-psychology/SKILL.md
- **Inputs:** top-ranked hypothesis from `hypotheses.md`, brand voice from `marketing/CONTEXT.md`
- **Produces:** `landing-pages/<slug>/tests/YYYY-MM-DD-<test-slug>/variants.md` — control text + 1–2 challenger variants, each annotated with the persuasion lever it tests (anchoring, specificity, social proof, loss aversion, etc.)
- **What to do:** Create the dated test folder. Write the variant copy. Each challenger names ONE psychology lever — don't compound levers in a single variant (violates "test one thing").

### Step 6 — Test design
- **Owner:** Claude
- **Parallelizable with:** —
- **Needs:** /Users/travisfoster/claude-code/cerkl/marketing/skills/ab-test-setup/SKILL.md
- **Inputs:** `variants.md`, `baseline.md` (for sample math), `tooling.md` (for metric + MDE conventions)
- **Produces:** `landing-pages/<slug>/tests/YYYY-MM-DD-<test-slug>/test-design.md` — full hypothesis statement, primary metric, guardrail metric, sample size + duration math, success threshold, stop conditions, PostHog setup notes (feature flag name, target audience, split %)
- **What to do:** Apply `ab-test-setup` §Sample Size and §Metrics Selection. Use `tooling.md` defaults: primary = CTA click-through, guardrail = `signup_completed` direction, MDE = 50% relative lift, 50/50 split, 3-week minimum. Compute duration honestly — if it exceeds 6 weeks, flag and suggest a bolder change or proxy metric.

### Step 7 — Build & launch
- **Owner:** External (Travis)
- **Parallelizable with:** —
- **Needs:** `test-design.md`, `variants.md`
- **Inputs:** the dated test folder
- **Produces:** Webflow variant build (per `tooling.md` implementation patterns) + PostHog experiment configured + tracking verified live on staging
- **What to do:** Surface this as a numbered checklist for Travis. Claude cannot publish Webflow changes or flip PostHog experiments. The checklist should restate the feature flag name, primary/guardrail metrics, and target sample size so Travis can configure PostHog correctly.

### Step 8 — Read out + decide
- **Owner:** Joint (Travis pulls PostHog results; Claude synthesizes)
- **Parallelizable with:** —
- **Needs:** /Users/travisfoster/claude-code/cerkl/marketing/skills/ab-test-setup/SKILL.md (§Analyzing Results)
- **Inputs:** PostHog experiment results (Bayesian view or exports Travis shares), `test-design.md`
- **Produces:** `landing-pages/<slug>/tests/YYYY-MM-DD-<test-slug>/results.md` — sample reached, primary metric outcome (with significance), guardrail outcome (direction only), segment splits if relevant, decision (ship / kill / extend / inconclusive)
- **What to do:** Apply the `ab-test-setup` analysis checklist. Decide winner/loser/inconclusive. Per `tooling.md`, do NOT call signup-conversion on per-test significance — track direction and roll up quarterly. If inconclusive after target sample, document and move to the next hypothesis.

### Step 9 — Update playbook + backlog
- **Owner:** Claude
- **Parallelizable with:** —
- **Needs:** —
- **Inputs:** `results.md`
- **Produces:** appended entry in `landing-pages/playbook.md` (every concluded test, winner OR loser); updated row in `landing-pages/backlog.md` (status → `shipped` / `killed` / `parked`)
- **What to do:** Use the playbook entry template. Capture the **reusable pattern**, not just the result. If the pattern could apply to another landing page, add a new hypothesis to `backlog.md` referencing this test as evidence (which raises its Confidence score).

### Step 10 — Session handoff
- **Owner:** Claude
- **Parallelizable with:** —
- **Needs:** —
- **Inputs:** `results.md`
- **Produces:** chat output
- **What to do:** End by stating in chat what shipped and the proposed next step. PA derives activity from git log — no update blocks.

---

## Output

Per-page workspace structure (created as the process runs — files don't all need to exist day one):

```
landing-pages/<slug>/
├── baseline.md
├── tracking.md
├── audit.md
├── voc.md
├── competitive.md
├── hypotheses.md
└── tests/
    └── YYYY-MM-DD-<test-slug>/
        ├── variants.md
        ├── test-design.md
        └── results.md
```

Plus cross-page assets touched every run: `backlog.md` (new hypotheses appended, statuses updated) and `playbook.md` (concluded tests appended).

## Future work

- Wire monthly backlog re-score to `/schedule` when scheduling lands
- Auto-fetch per-page PostHog dashboard data (baseline + active test status) on Step 1
- Decide whether signup-flow CRO tests get their own process or chain off this one via `signup-flow-cro` skill
- Sunset decision on GA4 once PostHog Web Analytics is validated as a replacement
- Build a "test idea" intake form so non-Travis sources (sales, customer support) can drop hypotheses into the backlog

## Learnings

Append "what broke / what we changed" notes here as the process matures. Format: `### YYYY-MM-DD — short title` then bullets.
