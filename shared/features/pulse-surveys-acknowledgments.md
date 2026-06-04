# Feature: Pulse Surveys & Employee Acknowledgments

> Part of Cerkl Broadcast. For product overview, see [broadcast.md](../broadcast.md).

**Available on:** All plans (Foundations, Foundations+, Omni AI)

---

## Close the Loop

Open-rate tracking via pixels has gotten noisier every year — Microsoft Defender, Mimecast, Proofpoint, AI assistants, and Apple Mail Privacy Protection all open emails on the subscriber's behalf, inflating opens and obscuring real engagement. Pulse Surveys and Employee Acknowledgments are the two Blast elements that close that loop. Both require an explicit action from the subscriber on a Cerkl-hosted landing page, so the response is real — and both feed reporting that can be retargeted against. They're the recommended way to get a 100% accurate read on whether a subscriber actually saw and engaged with a specific message.

Both elements live inside the [Blast editor](email-blasts.md) as drag-and-drop blocks. No separate survey tool, no external links, no manual follow-up.

---

## Pulse Surveys

A Pulse Survey is a single-question block dropped into a Blast. Communicators choose between two reaction styles:

- **Range** — numerical scale, useful for sentiment scoring and satisfaction check-ins
- **Positive / Negative** — binary reaction, useful for fast yes/no read-outs

Use cases include check-ins, sentiment captures, policy feedback, event RSVPs, and quick polls — anywhere a separate survey platform would be overkill for a single question.

### Reporting

Pulse Survey results appear on the **Survey** tab of a Blast's full Insights page (**Insights > Blasts > Metrics**, then click into the Blast). The display includes:

- **Question** — the survey question as sent
- **Reaction Style** — range or positive/negative
- **Total Responses** — count of subscribers who answered
- **Response Rate** — total responses divided by Blast audience
- **Average Response** — numerical mean for range surveys, Percent Positive for positive/negative
- **Most Common Response** — flagged with a star when one response clearly leads

Pulse Survey results are intentionally aggregated. Individual subscriber-level responses are **not** available — responses are grouped by reaction style only. Privacy-restricted subscribers ("Do not personalize my experience") are still counted in Survey reporting because the response is submitted explicitly on a landing page.

When a Blast is retargeted, Survey data from the original send and the retarget are combined into a single view, so the response picture stays complete.

---

## Employee Acknowledgments

Acknowledgments are a timestamped read receipt embedded directly in a Blast. The subscriber clicks the acknowledgment element, lands on a Cerkl-hosted page, confirms, and the timestamp is recorded against their audience record. This is the primary tool for compliance communications, policy updates, safety notices, handbook rollouts, and anywhere HR or legal needs proof of receipt.

### Reporting

The **Acknowledgment** tab on a Blast's full Insights page shows row-level subscriber data:

- **Audience Member** — name and email
- **Open** — green checkmark if the Blast was opened, "x" if not
- **Date Acknowledged** — exact timestamp of the acknowledgment, blank if the subscriber has not yet confirmed

Because acknowledgments require an explicit click-through to a landing page, they're collected even for subscribers with the strictest privacy setting — making this the most reliable confirmation surface in Broadcast.

For full reporting context, see [analytics-insights.md](analytics-insights.md).

---

## Retargeting Non-Responders

Both elements integrate directly with [Blast Retargeting](email-blasts.md). When retargeting a Blast (**Blasts > Sent > Retarget Blast**), the Projected Audience step exposes two response-based options on top of the standard open/click filters:

- **An Acknowledgment** — recipients who have not confirmed the Acknowledgment in the original Blast
- **Responded to Survey** — recipients who have not submitted a response to the Pulse Survey

If the original Blast didn't contain an Acknowledgment or Survey, the corresponding option is disabled. Retargets can be scheduled up to 180 days after the original send. This is the workflow that turns a one-shot compliance message into a managed close-the-loop campaign: send, watch the response data fill in, then automatically re-send only to the holdouts.
