# Competitor Dissatisfaction Mining — Methodology

> Always loaded with `competitor-dissatisfaction/CLAUDE.md`. This file is the source of truth for signal taxonomy, source surfaces, dissatisfaction filter, enrichment schema, bucket model, and handoff format. CLAUDE.md carries decisions; detail lives here.

**Last reviewed:** 2026-05-14 (v1 draft — pending Travis sign-off on §3 filter, §4 schema, §5 bucket names)

---

## 1. Source surfaces

Public surfaces where competitor users speak unfiltered. Each surface has a default confidence level — the bouncer for signal tier (see §2).

| Surface | Why | Default confidence | Notes |
|---|---|---|---|
| **G2** | Star-rated reviews; reviewer role/company often visible | **High** when reviewer profile shows company; **Medium** when masked | Use the "4 stars and below" filter; 12-month recency |
| **Capterra** | Similar to G2; different audience overlap | **High** w/ profile, **Medium** masked | Often surfaces SMB voices G2 misses |
| **TrustRadius** | Verbose reviews; reviewer-validated | **High** | Smaller volume; scan the verified-buyer feed |
| **Software Advice** | Similar to Capterra | **Medium** | Lower volume; supplementary |
| **Trustpilot** | General review site | **Low–Medium** | Often non-buyer noise; only use when ≤3-star detail names the vendor |
| **Reddit** | r/internalcomms, r/humanresources, r/communications | **Medium** | Reviewer identity rarely available — treat as theme signal, not contact source |
| **LinkedIn comment threads** | Comments on competitor posts / ex-employee posts | **Medium** | Reviewer identity visible; verifiable role |
| **Vendor-specific feedback & bug channels** | Vendor-hosted feedback forums, idea/roadmap boards (Canny, ProductBoard public), bug-report threads, `community.<vendor>.com`, `feedback.<vendor>.com`, status-page incident comments | **Medium–High** when reviewer profile shows company; **Medium** otherwise | **Requires per-vendor discovery** — not every vendor has these. Search patterns: `site:canny.io <vendor>`, `<vendor> community`, `<vendor> feedback`, `<vendor> roadmap`, `<vendor> known issues`. When found, signal-to-noise is high because content is product-specific. Worth a parallel sub-agent search per competitor in Step 2a of the process. |
| **Glassdoor** | Employee side — comments on internal-comms tooling | **Low** | Out-of-band; useful for "Vendor Burnout" theme only |
| **X / Twitter** | Public mentions of vendor names | **Low** | High noise; only mine when paired with another signal |

### Known limitations

- **Reddit is fully blocked** by Claude Code's `WebFetch` for both HTML and RSS endpoints (validated 2026-05-15 — the `.rss` workaround does **not** work). Reddit mining requires Firecrawl MCP, browser MCP, or an external scraper (Apify / BrightData / ScrapingBee).
- **G2 / Capterra / TrustRadius return HTTP 403 (Cloudflare bot protection)** on direct `WebFetch`. Workaround: `WebSearch` with `site:<source>.com <vendor>` returns indexed content with theme-level complaints + ratings (validated on G2 for Poppulo, 2026-05-15). Lower fidelity than direct scrape — no per-reviewer identity extraction — but viable as a Plan-B mining path for theme signal.
- Trustpilot and X return high false-positive rates — leave them out of v1 source set unless Travis explicitly opts in.

---

## 2. Signal taxonomy

A "dissatisfaction signal" has two parts: a **type** (what kind of complaint) and a **tier** (how hot).

### Signal types

| Type | Example | Best surface |
|---|---|---|
| **Switch intent** | "Looking for alternatives to X" / "Migrating off X" | Reddit, G2 reviews, LinkedIn |
| **Named complaint** | "X's segmentation is broken" / "Support is terrible" | G2, Capterra, TrustRadius |
| **Feature gap** | "X doesn't support Y" / "Wish X had…" | G2, competitor forums, Canny boards |
| **Pricing/value** | "Not worth $X/mo" / "Hidden fees" | G2 1–3 star, Trustpilot |
| **Renewal friction** | "Stuck in contract until…" / "Procurement nightmare" | LinkedIn comments, Reddit |
| **Implementation pain** | "Took 6 months to roll out" / "IT team hated it" | G2, case-study counter-narratives |

### Signal tiers

| Tier | Definition | Confidence required |
|---|---|---|
| **S** | Explicit switch intent OR named complaint with verifiable user + company | High |
| **A** | Named complaint OR feature gap with verifiable user, recent (<6 mo) | High or Medium |
| **B** | Theme signal (e.g., 3+ reviewers same complaint) without individual contact ID | Medium |

Tier-S signals require **High source confidence** — verifiable reviewer identity (real name + company OR named role at named company). Padding the list with Medium-confidence Tier-S rows ruins the list's reputation with sales fast (same rule pressure-prospecting uses).

---

## 3. Dissatisfaction filter

Applied after source mining, before enrichment. Two layers.

### Hard filter (must pass)
- ≤3-star review (G2/Capterra/Software Advice/TrustRadius), **OR**
- Explicit complaint keyword in body (see §3.1), **OR**
- Explicit switch-intent keyword (see §3.1)
- **AND** posted within the **last 12 months**

### Soft filter (rank, don't exclude)
- Reviewer identity verifiable → +1 rank
- Specific feature/complaint named (not just "bad") → +1 rank
- Quantified impact ("took 6 weeks", "lost X hours/wk") → +1 rank
- ICP-matched company (size + vertical per [`shared/icp.md`](../../shared/icp.md)) → +1 rank

### 3.1 Keyword categories

**Switch-intent keywords:** "switching from", "moving off", "alternative to", "replace [vendor]", "migrating from", "looking for something better", "evaluating alternatives"

**Named-complaint keywords:** "frustrated with", "support is terrible", "useless", "broken", "doesn't work", "buggy", "slow", "missing", "wish it had", "would not recommend"

**Pricing/value:** "overpriced", "not worth", "hidden fees", "renewal price hike", "vendor lock-in"

(Keep this list living — append discovered phrases in §10 Learnings as runs surface them.)

---

## 4. Enrichment schema

Not every field is populated on every row. The schema is layered: **Required** must be present; **Identity** must satisfy a minimum viable combination; **Nice-to-have** is helpful but a row ships without it.

### Required (always present)

| Field | Source |
|---|---|
| `competitor` | Mined surface |
| `signal_type` | From §2 types |
| `signal_tier` | From §2 tiers |
| `bucket` | From §5 bucket model |
| `complaint_summary` | 1–2 sentence Claude synthesis from raw quote (§7 voice rules) |
| `source_url` | Direct link to review/post |
| `source_date` | YYYY-MM-DD |
| `confidence` | High / Medium / Low |
| `evidence_path` | `raw/<slug>/YYYY-MM-DD/...` |
| `recommended_angle` | From §5 bucket → angle map + competitor-specific 2026 narrative (always derivable from bucket + competitor) |

### Identity (must satisfy ≥1 valid combination)

A row is handoffable to AEs only if it identifies a target persona well enough to act on. Acceptable combinations:

- `reviewer_name` + `company`
- `reviewer_role` + `company`
- `reviewer_role` + `industry` + `company_size`

If none hold, the row routes to a separate **Theme signals** tab in the handoff (see §6) — informs positioning/angle work but isn't a contact lead.

| Field | Source |
|---|---|
| `reviewer_name` | Mined surface OR Apollo/Clay/ZoomInfo lookup |
| `reviewer_role` | Mined surface OR LinkedIn |
| `company` | Mined surface OR enrichment |
| `company_size` | Apollo/Clay (employee count band) |
| `industry` | Apollo/Clay |

### Nice-to-have (ship without if not found; flag in row)

| Field | Source |
|---|---|
| `hubspot_status` | `new` / `existing-contact` / `existing-account-new-contact` (skip if HubSpot lookup blocked) |

Any row missing nice-to-have fields ships with a `flags` column populated (e.g., `flags: hubspot-status-unknown`) so Marc/Josh see at-a-glance what's incomplete.

---

## 5. Bucket model (outbound posture)

Bucket = how Marc/Josh should *talk* to this person, not what they're complaining about. Parallel to pressure-prospecting's bucket model — the bucket maps to a playbook.

| Bucket | Signal pattern | Recommended angle | When to send |
|---|---|---|---|
| **Active Switcher** | Explicit switch intent in last 90 days | Lead with Cerkl's free Foundations + speed-to-launch; offer a side-by-side | Now |
| **Vocal Critic** | Named complaint, feature gap, or pricing dissatisfaction | Lead with the specific feature/measurement angle that addresses the complaint | Within 14 days of complaint posting |
| **Frustrated User** | General dissatisfaction, no clear angle | Warm sequence — start with relevant case study, then ask about renewal timing | Drip over 4–6 weeks |
| **Vendor Burnout** | Long-tenured user (≥3 yr) complaining about platform overall | Strategic — multi-touch over 60+ days; lead with "delivery + measurement layer, not platform replacement" reframe | Slow burn |

If a row's `signal_tier` and `bucket` feel mismatched, that's usually the trap pressure-prospecting calls out — re-check §2 vs. §5 before shipping.

---

## 6. Handoff format

Default output: Google Sheet with **two tabs**, one row per row. One sheet per run, named `competitor-dissatisfaction-handoff-YYYY-MM-DD`. Pivoted view by bucket gives Marc/Josh a sequence-ready cut.

- **Leads tab** — rows that satisfy §4 Identity. Contact-actionable.
- **Theme signals tab** — rows with strong dissatisfaction signal but no actionable identity. Informs positioning/angle work; not a contact lead.

Stretch goal (Phase 4): direct HubSpot import with a custom property `competitor_dissatisfaction_signal` carrying the source URL + bucket. Decide after first run.

**What Marc + Josh get at handoff:**
1. The Sheet (link, both tabs)
2. A 4–6 bullet Slack exec summary — top theme per competitor, bucket distribution, dedupe stats, Leads/Theme-signals split
3. A note flagging any rows the run *almost* shipped but caught at filter — sanity check for tuning

Rows missing nice-to-have fields ship with a `flags` column populated (e.g., `flags: hubspot-status-unknown`) so Marc/Josh see at-a-glance what's incomplete.

---

## 7. Voice rules

When summarizing a complaint in the `complaint_summary` field or in any outbound angle:

- Quote the reviewer's words when the words are good ("drowning in spreadsheets" > "manual workflow inefficiency")
- Don't manufacture emotion the reviewer didn't express
- Don't restate the vendor's marketing claims as if true — we're mining what users actually said
- One sentence per `complaint_summary` field. Two only if the complaint has two distinct parts.

---

## 8. Evidence storage

Every mined source gets persisted to disk before synthesis — same pattern as `competitor-profiling` SKILL and pressure-prospecting:

```
sales/competitor-dissatisfaction/raw/
└── <competitor-slug>/
    └── YYYY-MM-DD/
        ├── g2/              ← one .md per scraped page
        ├── capterra/
        ├── reddit/          ← thread URLs + extracted posts
        ├── linkedin/
        └── notes.md         ← run-level notes (filters applied, anomalies, sources that 404'd)
```

Rules:
- `<competitor-slug>` is lowercase, hyphenated (e.g., `workshop`, `contact-monkey`, `axios-hq`)
- `<YYYY-MM-DD>` is the run date — never overwrite a prior date
- Raw is the receipt; the synthesized handoff Sheet is the deliverable

---

## 9. References

- [PRINCIPLES.md](../../PRINCIPLES.md) — workspace conventions
- [pressure-prospecting/methodology.md](../pressure-prospecting/methodology.md) — sibling signal-mining methodology; confidence framework + bucket conventions parallel
- [`marketing/skills/customer-research/SKILL.md`](../../marketing/skills/customer-research/SKILL.md) — Mode 2 (Digital Watering Hole Research) is the primary engine; extraction template + High/Medium/Low confidence model
- [`marketing/skills/competitor-profiling/SKILL.md`](../../marketing/skills/competitor-profiling/SKILL.md) — Firecrawl-based scraping pattern + dated raw-data storage convention
- [`shared/competitors.md`](../../shared/competitors.md) — anchor competitor list
- [`shared/icp.md`](../../shared/icp.md) — ICP fit for the soft-filter rank
- [`research/competitor-marketing/Competitors/`](../../research/competitor-marketing/Competitors/) — 2026 positioning context per competitor (10 dated deep-dives at 2026-05-10); feeds the `recommended_angle` field. **Note:** `shared/competitors.md` references this folder at the wrong path (`research/ic-trends/deepdives/Competitors/`) — pre-existing broken links, flagged for cleanup.

---

## 10. Learnings (append-only)

Append "what broke / what we changed" notes here as the methodology evolves.

### 2026-05-15 — Pre-sample access test (Poppulo target)

- `WebFetch` returned **HTTP 403 Cloudflare** on G2 (`/products/poppulo/reviews`) and TrustRadius (`/products/poppulo/reviews`) — bot protection, not vendor-specific.
- `WebFetch` is **fully blocked at the tool level** for `www.reddit.com` on both HTML search and the `.rss` endpoint. The earlier methodology hypothesis that `.rss` was a workaround was wrong — both fail with "Claude Code is unable to fetch from www.reddit.com".
- `WebSearch` with `site:g2.com poppulo reviews complaint` DID return indexed G2 content: 4.4/5 stars across 87 reviews, plus theme-level complaints (mobile experience, complexity, API integration, template limitations, PDF display). Fidelity is theme-level, not per-reviewer.
- **Methodology change applied:** §1 Known Limitations rewritten to reflect actual access pattern + named `WebSearch` fallback.

### 2026-05-15 — Poppulo vendor-specific surface audit (sub-agent)

- Most standard vendor-specific patterns are **absent** for Poppulo: no `community.poppulo.com`, no `forum.poppulo.com`, no public Canny/Productboard roadmap, no `r/poppulo` subreddit, no Discord/Slack community.
- Working surfaces (public, accessible): `poppulo1.statuspage.io` (Statuspage incident history), `knowledgebase.poppulo.com` (KB, no comments), `developer.poppulo.com` (API docs, no feedback), `github.com/poppulo` (19 repos, mostly archived; 0 open issues).
- Marketing roadmap landers exist (`poppulo.com/lp/employee-comms-roadmap-2025` and `/lp/digital-signage-roadmap-2025`) but are upstream positioning content with no feedback widget. Not a dissatisfaction signal source.
- Legacy FWI Community (`community.fourwindsinteractive.com`) is decommissioned post-merger (TLS cert invalid).
- **Implication for Poppulo runs specifically:** the §1 "Vendor-specific feedback & bug channels" row yields no usable surface — Poppulo runs lean on G2 + Capterra + TrustRadius + Reddit + LinkedIn instead.
- **Methodology change applied:** none — §1 row already says "Requires per-vendor discovery — not every vendor has these." Per-vendor finding documented here as run notes.
