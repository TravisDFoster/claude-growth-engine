---
name: audit-marketing-emails
description: "Scan HubSpot marketing emails for clone-and-edit mismatches between name, subject, body, and download links. Produces a findings report. Read-only — does not modify emails. For making changes, use draft-marketing-email."
license: MIT
metadata:
  version: "0.1.0"
  category: audit-planning
---

# Audit Marketing Emails

Scan a slice of HubSpot's marketing emails (typically `AUTOMATED_EMAIL` form follow-ups, but works for any type), surface mismatches between the email's name, subject line, body text, and download links, and produce a findings report.

**This skill is read-only.** It does not edit, draft, or publish anything. To act on the findings, hand them off to [`draft-marketing-email`](../draft-marketing-email/SKILL.md).

## When to use

- Periodic health check (quarterly or after a known cloning spree).
- After a campaign push that involved cloning existing emails as templates.
- When deliverability or click-through metrics dip on a specific email and the cause isn't obvious.

**Don't use** for routine copy updates on a single email — that's `draft-marketing-email`.

## Setup

Load env (required for python subprocesses to see the token):
```bash
set -a && source /Users/travisfoster/claude-code/cerkl/.env && set +a
```

Use `curl` for HTTP calls and `python3` for parsing the JSON files curl writes to disk. Per `hubspot/CLAUDE.md`, urllib hits SSL cert errors on this machine.

Required scope: `content` (read).

## Workflow

### Phase 1 — Pick the slice

Decide which emails to audit. The usual cuts:

| Slice | Filter |
|---|---|
| All form follow-ups | `?type=AUTOMATED_EMAIL` then filter `name.startswith('Form Follow-up:')` |
| All automated | `?type=AUTOMATED_EMAIL` |
| All campaign sends | `?type=BATCH_EMAIL` |
| Everything | no `type` filter |

Default to the narrowest slice that fits the user's question.

### Phase 2 — List

```bash
curl -s -H "Authorization: Bearer $HUBSPOT_ACCESS_TOKEN" \
  "https://api.hubapi.com/marketing/v3/emails?limit=100&type=AUTOMATED_EMAIL" \
  > /tmp/hs-audit-list.json
```

Note the `total` field. If it exceeds 100, paginate with `after=<cursor>` (returned in `paging.next.after`).

### Phase 3 — Read each email

For every email in the slice, fetch full JSON to disk so the body is parseable:

```bash
mkdir -p /tmp/hs-audit
for id in $IDS; do
  curl -s -H "Authorization: Bearer $HUBSPOT_ACCESS_TOKEN" \
    "https://api.hubapi.com/marketing/v3/emails/$id" > /tmp/hs-audit/$id.json
done
```

Body location: `content.widgets.<module-id>.body.html` (raw HTML, usually one main module per email). Extract clean text:

```python
import re
text = re.sub(r'<[^>]+>', ' ', html)
text = re.sub(r'\s+', ' ', text).strip()
```

Also pull from the JSON: `id`, `name`, `subject`, `state`, `clonedFrom`, and (optionally with `?includeStats=true`) the engagement counters.

### Phase 4 — Compare

For each email, lay out three values side-by-side:

| Field | Source |
|---|---|
| **Asset** | `name`, after stripping the prefix (e.g., `"Form Follow-up: "`) |
| **Subject** | `subject` |
| **Body** | text extracted from `content.widgets.<id>.body.html` (first 250 chars is usually enough) |

Look for **clone-and-edit mismatches**:

- **Subject mismatch** — subject talks about asset X, name and body are about asset Y. Pattern: someone cloned a working email and forgot to update the subject. Common when the asset name appears multiple places and one was missed.
- **Subject + body mismatch** — name says asset X but everything else (subject, body, download link) talks about asset Y. The clone was never edited at all. Almost always also has a wrong download link `href`.
- **Cascade clones** — when one already-broken email gets cloned and the new one inherits the same defect. Use the `clonedFrom` field in the API response to find the source. If you fix one, check siblings.

Don't try to programmatically classify. The right judge is a human reading the side-by-side. Surface the data; let the user (or you, with sufficient context) decide.

### Phase 5 — Report

Save findings to `reports/marketing-email-audit-{YYYY-MM-DD}.md`:

```markdown
# Marketing Email Audit — YYYY-MM-DD

## Summary
- Slice: <e.g., AUTOMATED_EMAIL, name starts with "Form Follow-up:">
- Total reviewed: NN
- Clean: NN
- Mismatches found: NN (broken down by type)

## Findings

### ❌ Wrong subject only — N emails
| ID | Name | Wrong subject | Should reference |
|---|---|---|---|
| `205165964609` | Form Follow-up: IC Content Calendar Template | "Access our Free Guide for Improving Email Click-Thru Rates" | IC Content Calendar Template |

### 🚨 Wrong subject AND body — N emails
| ID | Name | What it actually sends |
|---|---|---|
| `185541166622` | Form Follow-up: Onboarding Email Template | Subject + body both reference "Employee Experience Journey Mapping Template"; download link points to that asset too |

## Cascade clones detected
- `205165964609` cloned from `198052838150`; both inherited the same wrong subject.

## Suggested next steps
For each finding, run `/draft-marketing-email` to stage the correction.
For findings with bad download links, also flag those for manual UI fix
(asset attachment swap is best done in HubSpot's drag-and-drop editor).
```

End with a one-line handoff: "Run `/draft-marketing-email` on each ID to stage corrections; publish from the HubSpot UI."

## Anti-patterns

- **Auto-classifying mismatches without a human review.** False positives are easy (e.g., minor naming variants like "DE&I" vs "DEI Communications" describe the same asset). Show data, don't pre-judge.
- **Auditing the whole catalog when one slice is enough.** Each email is an extra GET. Pick the narrowest slice that fits the user's question.
- **Modifying anything from this skill.** This skill never PATCHes. If a fix is warranted, hand off to `draft-marketing-email`.
- **Treating engagement stats as the primary audit lens.** Stats reveal symptoms; the audit here is for content correctness. A broken email can have great stats if subscribers click anyway, and a correct one can have weak stats for unrelated reasons.

## Output

| Artifact | Path |
|---|---|
| Findings report | `reports/marketing-email-audit-{YYYY-MM-DD}.md` |
| Raw JSON snapshots (optional) | `data/audit-logs/marketing-emails-{YYYY-MM-DD}/` |

## Learnings (append-only)

### 2026-05-10 — first run, form follow-ups (22 emails)

- **Found 4 broken Form Follow-up emails.** Three with wrong subjects (cascade clone from "Email CTR Guide"); one with wrong subject AND body (cloned from "Journey Mapping Template", nothing edited; download link also wrong).
- **`clonedFrom` is the most useful field for diagnosis.** Surfaced the cascade-clone pattern: `IC Content Calendar` was cloned from `IC Policy Template`, and both inherited the same wrong subject from `Email CTR Guide`. Worth chasing whenever a finding looks like it might be systemic.
- **Naming variants aren't mismatches.** "DEI Communications Guide" → "DE&I Communications Checklist" reads as different but is the same asset. The audit produces side-by-side data; the human (or LLM with full context) judges. Don't string-match.
