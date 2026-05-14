---
type: concept
tags: [internal-email, ic-measurement-and-roi]
---

# Internal Email Benchmarks

## Definition

Aggregate performance metrics for internal-corporate-communications email — open rate, click rate, click-to-open rate, read time, skim share — used as comparison baselines by IC teams to evaluate their own program performance. As of 2026, **all named benchmarks in the category are single-vendor telemetry**; no independent academic or analyst IC email benchmark exists.

## Why It Matters

Internal email is the largest single comms channel in most enterprises, but the benchmark substrate is structurally compromised: every annual benchmark is published by a vendor whose customer base IS the dataset. Two competing 2026 benchmarks dropped within 24 hours (PoliteMail/Ragan on 2026-05-07, [[contactmonkey]] on 2026-05-08) — both vendor-funded, both single-channel, similar shape. Citing "the 2026 IC email benchmark" without naming the vendor and methodology overstates the typical IC team's reality, and the headline open-rate number on every benchmark carries acknowledged inflation issues (see [[open-rate-inflation]]).

The structural vacuum — no cross-vendor, no academic, no analyst benchmark — is itself the most important fact about this category as of 2026. It is the wedge for a [[cross-channel-benchmark]] from a vendor with cross-channel telemetry.

## How It Works

Vendors aggregate platform telemetry across their customer base and publish industry / company-size / interactive-feature splits. The 2026 cycle produced two parallel anchors:

### Paired vendor anchors — 2026

| Benchmark | Publisher / Author | Sample | Headline Open | Headline Click | Distribution |
|---|---|---|---|---|---|
| [[ragan-email-benchmarks-report-2026-05-12]] | [[politemail]] (authored), [[ragan-communications]] (distributed) | ~2B emails / ~11M employees / 10 S&P sectors | **66%** unique open | **7%** click any link (10% of openers) | Gated PDF via Ragan; ungated summary on [[pr-daily]] |
| [[contactmonkey-internal-email-benchmark-2026]] | [[contactmonkey]] | 255K campaigns across 20+ industries | **76%** open | **9%** click | Direct vendor publication (no co-brand) |

Both report similar additional metrics — average ~14 emails/employee/month, multi-minute read time, decline in open rate with org size, frontline-heavy industries clustered at the bottom of the range. The numerical difference between the two (10pp on open, 2pp on click) is best read as **methodology variance** (Outlook-only vs Outlook+Gmail; preview-pane handling; DL hygiene assumptions) rather than a real underlying gap.

## Methodology Caveats — Apply to Both 2026 Anchors

Per [[open-rate-inflation]], every vendor benchmark in this category inherits three structural inflation sources, all acknowledged in vendor content:

- **Outlook preview-pane "opens"** — pixel fires when reading-pane renders the message, regardless of whether the recipient gave it focused attention. Particularly material for [[politemail]] (Outlook-only telemetry).
- **Automated security scanners** — enterprise security tools fetch images and follow links to inspect them, generating false-positive open and click events. Material across the category; severity correlates with industry security maturity.
- **Stale distribution lists** — former-employee mailboxes, shared service-account mailboxes, and partner inboxes registering pixel hits without a human reader.

PoliteMail's own technical content acknowledges these. ContactMonkey's public summary does not. Either way, the **headline open-rate number is the most-cited and least-defensible metric** in the category — sharper alternatives (open-attention rate, read-rate, click-of-opener, skim split, time-in-email) are deeper in each vendor's methodology disclosures.

### Recommended citation discipline

- Always name the vendor and the methodology when citing a benchmark number.
- Prefer secondary metrics (CTOR, time-in-email, skim share) over headline open-rate where the vendor publishes them.
- For blog citation: per the *Blog Post Research Mode* rule in [`../../CLAUDE.md`](../../CLAUDE.md), competitor-sourced stats (ContactMonkey, PoliteMail) are excluded from external publication.

## Seen In

- [[ragan-email-benchmarks-report-2026-05-12]] — 2026 PoliteMail/Ragan paired anchor; 66% open / 7% click; ~2B emails / ~11M employees / 10 S&P sectors
- [[contactmonkey-internal-email-benchmark-2026]] — 2026 ContactMonkey paired anchor; 76% open / 9% click; 255K campaigns across 20+ industries
- [[politemail]] — vendor source for the PoliteMail/Ragan benchmark; self-acknowledges [[open-rate-inflation]]
- [[contactmonkey]] — vendor source for the parallel benchmark

## Related Concepts

- [[open-rate-inflation]] — methodology critique applying symmetrically to all single-channel vendor benchmarks
- [[cross-channel-benchmark]] — alternative measurement frame; Cerkl's defensible content slot, structurally inaccessible to single-channel vendors
- [[interactive-email-features]] — features vendors track within the benchmark; intent-confirmed engagement signals less subject to pixel inflation
- [[engagement-by-work-location]] — frontline-heavy industries cluster at the bottom of email open rates across vendors; consistent with the Gallup engagement gap

## Tensions / Criticisms

- **Single-vendor data: any benchmark from one platform reflects that vendor's customer base, not the IC market overall.** Compounded by ICP self-selection: PoliteMail's enterprise-Outlook customers and ContactMonkey's customers are likely both more measurement-mature than the median IC team.
- **Headline open-rate methodology is acknowledged-weak.** See [[open-rate-inflation]]. The vendor most credibly acknowledging this ([[politemail]]) is also the one publishing the lower of the two 2026 anchors (66% vs ContactMonkey's 76%), which may signal more conservative DL hygiene rather than worse performance.
- **No standardized cross-vendor benchmark exists.** Anyone citing a number should name the source. [[gallagher]]'s *State of the Sector* is the closest IC-wide industry survey, but it's strategy-focused, not telemetry-anchored.
- **Trade-pub editorial cover obscures vendor authorship.** The "Ragan 2026 Internal Email Benchmarks Report" is [[politemail]]'s data with [[ragan-communications]] distribution — not independent trade-publication research, despite the framing. Readers unfamiliar with the vendor-partnership pattern can miscite.

## Open Questions

- **Methodology depth in the gated PoliteMail/Ragan PDF** — does the full report disclose preview-pane handling, scan filtering, and DL hygiene assumptions in a way the ungated PR Daily summary doesn't?
- **Has [[contactmonkey]] published methodology disclosures comparable to PoliteMail's "5 Internal Email Metrics Better Than Open Rates"?** Not visible in current research.
- **2026 YoY direction on key metrics across vendors** — PoliteMail's report cites 2024 / 2023 comparisons; ContactMonkey's summary does not visibly. Cross-vendor longitudinal reading is not currently possible from public excerpts.
- **Would an academic or association-led benchmark ([[iabc]] / [[usc-annenberg]]) ever fill the vacuum?** None has emerged in this cycle; the *A Quiet Shift* 2026 report is PR/voice-focused, not IC channel telemetry.
