---
type: concept
tags: [internal-email, ic-measurement-and-roi, intranet-and-digital-workplace]
---

# Cross-Channel Benchmark

## Definition

An IC measurement benchmark that aggregates engagement and delivery data across *all* internal-comms channels an organization uses — email + Teams/Slack + intranet + SMS + mobile push — rather than benchmarking each channel in isolation. As of 2026, **no published cross-channel IC benchmark exists.** Every named annual benchmark in the field ([[politemail]] / [[ragan-email-benchmarks-report-2026-05-12]], [[contactmonkey-internal-email-benchmark-2026]], [[workshop]] *Internal Comms Trends Report*, etc.) is single-channel, almost always email.

## Why It Matters

Two reasons. **First**, the buyer-side IC reality is multi-channel — the question "did the message get to the right people across the channels they actually use?" can't be answered by a single-channel benchmark, no matter how big its sample. **Second**, the structural absence of a cross-channel benchmark is a competitive vacuum that single-channel vendors **cannot fill** — PoliteMail (Outlook-only) and ContactMonkey (email-only) don't have the data — and Cerkl, as a cross-channel delivery + measurement layer (~6M employees/month spanning email + Teams + Slack + intranet + SMS), structurally can.

This is the asymmetric content position the [[ragan-email-benchmarks-report-2026-05-12]] deep-dive flagged: Cerkl can publish the first cross-channel IC benchmark, not by beating PoliteMail at email volume (Cerkl is ~half PoliteMail's email-only telemetry), but by changing the unit of measurement.

## How It Works

A cross-channel benchmark answers questions a single-channel benchmark can't:

- **Reach efficiency** — what percentage of the target audience saw the message in *any* channel, across the channels they use? (single-channel: open rate per channel, in isolation)
- **Channel mix by audience segment** — for frontline workers, what mix of SMS / mobile push / Teams delivered the message effectively? (single-channel: email open rate of frontline workers, which is already low; can't speak to why or what worked instead)
- **Cross-channel attribution** — when a message lands in Teams and email, which channel drove the read/action? (single-channel: each platform claims the open)
- **De-duplication** — when 5 employees see the same message in 3 channels each, how many *unique* employees engaged? (single-channel: doesn't compute)

A defensible benchmark methodology would publish:
- channel-mix distributions by industry and org size (what *typical* IC stacks look like)
- single-message reach efficiency across channels (the % uplift from adding each channel)
- de-duplicated audience-level engagement, not message-level pixel hits
- structural caveats (cf. [[open-rate-inflation]]) for each channel's measurement layer

## Seen In

- [[ragan-email-benchmarks-report-2026-05-12]] — flagged as Cerkl's defensible content slot in the deep-dive's recommendation
- [[gallagher]] — *State of the Sector* is the closest existing thing to a cross-channel IC benchmark, but it's strategy-focused (channel-mix self-report) not telemetry-anchored

## Related Concepts

- [[internal-email-benchmarks]] — the category cross-channel reframes
- [[open-rate-inflation]] — single-channel methodology critique that cross-channel sidesteps by changing the unit
- [[engagement-by-work-location]] — frontline / hybrid / on-site engagement gap is partially a channel-fit problem cross-channel measurement is positioned to expose

## Tensions / Criticisms

- **De-duplication is hard.** Linking the same employee's email open to their Teams notification to their intranet visit requires identity resolution across systems. Vendors with HRIS sync (Cerkl) can do this; vendors plugged into a single channel (PoliteMail, ContactMonkey, Workshop) structurally cannot — that's the moat, but it's also the technical lift.
- **Channel-mix heterogeneity makes baselining hard.** A cross-channel benchmark needs to publish "typical mix" baselines (e.g., "median IC team uses 2.3 channels"); the variance is large; the framing matters.
- **Cross-channel can still be inflated.** If Teams notifications and intranet impressions carry their own version of [[open-rate-inflation]] (e.g., notification-fired-but-never-viewed), a cross-channel benchmark inherits the problem in a different form. The credibility of the benchmark depends on which engagement signals it counts — read-through, dwell time, action, not just impression.

## Open Questions

- **Has any vendor floated a cross-channel benchmark publicly?** No public release surfaced as of 2026-05-12. Worth monitoring [[firstup]], Staffbase, and Simpplr — these are the cross-channel-capable vendors most likely to publish first if the category becomes contested.
- **Cerkl's marketing capacity to commission the benchmark by Q3 2026.** The deep-dive recommendation is a 2026 Q3 content target; whether that's a marketing-team capacity question or an executive-call is open.
- **Methodology partner.** Would an academic anchor ([[usc-annenberg]] / Communication Leadership Exchange / similar) co-publication strengthen credibility, or dilute the Cerkl branding? Trade-off worth thinking through if/when the benchmark is commissioned.
