# Competitor Dissatisfaction Mining — Process

> Mine public reviews + forums for dissatisfied competitor users, enrich, hand off to AEs. Output: Google Sheet of enriched rows + Slack exec summary to Marc + Josh.

## Trigger

User types one of:
- "Run a competitor dissatisfaction mining pass"
- "Mine [competitor name] for dissatisfaction signals"
- "Refresh the competitor dissatisfaction list"

## Inputs

Ask at start of each run (skip if obvious from context):

1. **Scope** — full pass across all competitors, or focused on N specific competitors?
2. **Surfaces** — all source surfaces in [methodology §1](methodology.md#1-source-surfaces), or a subset?
3. **Tool** — Apify / BrightData / ScrapingBee / custom Python / manual? Lock for this run.
4. **Volume cap** — max rows to ship to sales? (Default 50 to avoid swamping AEs on early runs.)

## Context to load

- /Users/travisfoster/claude-code/cerkl/shared/company-info.md
- /Users/travisfoster/claude-code/cerkl/shared/icp.md
- /Users/travisfoster/claude-code/cerkl/shared/competitors.md
- /Users/travisfoster/claude-code/cerkl/shared/broadcast.md
- /Users/travisfoster/claude-code/cerkl/sales/CONTEXT.md
- /Users/travisfoster/claude-code/cerkl/sales/competitor-dissatisfaction/methodology.md

(Per [PRINCIPLES.md #4](../../PRINCIPLES.md), this list is authoritative for this scope.)

**Parallelization fallback:** if the runtime has `Agent`/`Task`, dispatch sub-agents in one message for Steps 2a–2b (per-competitor parallelism). If not, parallelize via multiple `WebSearch`/`WebFetch` calls in a single message — same effect.

## Steps

### Step 1 — Confirm scope + tool choice

- **Owner:** Joint (Travis decides; Claude documents in run notes)
- **Parallelizable with:** —
- **Needs:** [methodology.md](methodology.md) §1 (source surfaces), [`shared/competitors.md`](../../shared/competitors.md)
- **Inputs:** User answers to the 4 input questions
- **Produces:** Run plan (in-memory): `{competitors[], surfaces[], tool, volume_cap}`
- **What to do:** Confirm the four inputs. Lock the tool for this run — don't switch mid-run. If `volume_cap` unset, default to 50.

### Step 2a — Pull source URLs per competitor

- **Owner:** Claude (sub-agent OR parallel tool calls)
- **Parallelizable with:** 2b
- **Needs:** [`marketing/skills/customer-research/SKILL.md`](../../marketing/skills/customer-research/SKILL.md) Mode 2
- **Inputs:** Competitor list from Step 1
- **Produces:** In-memory map `{<competitor-slug>: [{surface, url}]}`
- **What to do:** For each competitor × each in-scope surface, identify the canonical landing URL (G2 review page, Reddit subreddit search URL with vendor name, LinkedIn vendor company page, etc.). Don't scrape yet — collect URLs first so Step 3 batch is clean.

### Step 2b — Pull positioning context from competitor deep-dives

- **Owner:** Claude (sub-agent OR parallel reads)
- **Parallelizable with:** 2a
- **Needs:** [`research/competitor-marketing/Competitors/`](../../research/competitor-marketing/Competitors/)
- **Inputs:** Competitor list from Step 1
- **Produces:** In-memory map `{<competitor-slug>: <2–3 sentence current positioning summary + 2026 narrative>}`
- **What to do:** Read each competitor's most recent dated deep-dive (e.g., LumApps' "AI Employee Hub" pivot, Simpplr's Comms AI). Feeds the `recommended_angle` field in Step 7.

### Step 3 — Mine reviews and forum posts

- **Owner:** Claude (using locked tool from Step 1)
- **Parallelizable with:** —
- **Needs:** [`customer-research`](../../marketing/skills/customer-research/SKILL.md) Mode 2 extraction template
- **Inputs:** URLs from Step 2a
- **Produces:** `raw/<competitor-slug>/<YYYY-MM-DD>/<surface>/...` per [methodology §8](methodology.md#8-evidence-storage)
- **What to do:** Mine each URL. Capture: post/review text, star rating where present, reviewer name + role + company where present, date, source URL. **Persist raw before any filtering.** Note any blocked/404'd sources in `raw/<slug>/<YYYY-MM-DD>/notes.md`.

### Step 4 — Apply dissatisfaction filter

- **Owner:** Claude
- **Parallelizable with:** —
- **Needs:** [methodology §3](methodology.md#3-dissatisfaction-filter)
- **Inputs:** Raw scrape files from Step 3
- **Produces:** In-memory `candidates[]` — rows that pass hard filter, with soft-filter rank score
- **What to do:** Apply hard filter (star threshold OR keyword OR switch-intent; recency ≤12 mo). Score against soft-filter signals. Trim to top `volume_cap × 1.5` (buffer for enrichment drop-off in Step 5).

### Step 5 — Enrichment pass

- **Owner:** Joint (External: Apollo/Clay/ZoomInfo + LinkedIn lookup; Claude: stitch + verify)
- **Parallelizable with:** —
- **Needs:** External enrichment tooling
- **Inputs:** `candidates[]` from Step 4
- **Produces:** `enriched[]` — candidates with all [methodology §4](methodology.md#4-enrichment-schema) fields populated
- **What to do:** For each candidate, pull company size, industry, role, contact info. Drop candidates where (a) company is outside ICP per [`shared/icp.md`](../../shared/icp.md), (b) reviewer identity can't be verified for Tier-S rows, (c) duplicate within run. Externally-owned sub-steps go to Travis as a checklist.

### Step 6 — HubSpot dedupe + bucket assignment

- **Owner:** Joint (External: HubSpot lookup; Claude: bucket logic)
- **Parallelizable with:** —
- **Needs:** HubSpot access, [methodology §5](methodology.md#5-bucket-model-outbound-posture)
- **Inputs:** `enriched[]` from Step 5
- **Produces:** `ready[]` — final rows with `hubspot_status` and `bucket` set
- **What to do:** For each row, check HubSpot for existing contact and account. Set `hubspot_status` ∈ {new, existing-contact, existing-account-new-contact}. Assign bucket per §5 signal-pattern table. If a row's tier and bucket feel mismatched, re-check §2 vs. §5 — that's the trap.

### Step 7 — Format handoff + notify AEs + push PA update

- **Owner:** Claude
- **Parallelizable with:** —
- **Needs:** [methodology §6](methodology.md#6-handoff-format), [methodology §7](methodology.md#7-voice-rules)
- **Inputs:** `ready[]` from Step 6, positioning context from Step 2b
- **Produces:**
  - `handoffs/<YYYY-MM-DD>.md` (master + Google Sheet link)
  - Slack-ready 4–6 bullet exec summary (in-chat, for Travis to send to AEs)
  - Update block appended to [`personal-assistant/projects/competitor-dissatisfaction-mining.md`](../../personal-assistant/projects/competitor-dissatisfaction-mining.md)
- **What to do:** Generate `complaint_summary` per row per §7 voice rules. Pull `recommended_angle` from §5 + Step 2b positioning context. Format as Sheet-ready table. Draft Slack summary (theme leaders + bucket distribution + dedupe stats + flagged-but-skipped). Append PA push-update with completion + status change + next step.

## Output

- **File:** `sales/competitor-dissatisfaction/handoffs/<YYYY-MM-DD>.md` (master) + Google Sheet (link in master)
- **Format:** Per [methodology §4](methodology.md#4-enrichment-schema) — one row per contact, sortable by bucket
- **Destination:** Marc Fregoe + Josh Mandelman (AEs) via Slack
- **Consumer:** AEs work the list per bucket playbook in [methodology §5](methodology.md#5-bucket-model-outbound-posture)

## Future work

- Cadence (weekly? biweekly?) — decide after first 2 runs
- `/schedule` wiring for automatic recurrence
- Direct HubSpot import path (skip the Sheet intermediate)
- Watchlist mode: flag accounts whose dissatisfaction *intensifies* across runs
- Cross-feed with [Pressure Prospecting](../pressure-prospecting/CLAUDE.md): when an account shows both vendor dissatisfaction **and** corporate pressure, it's a top-tier sales target — handoff format should call this out

## Learnings (append-only)

Append "what broke / what we changed" notes here as the process matures.
