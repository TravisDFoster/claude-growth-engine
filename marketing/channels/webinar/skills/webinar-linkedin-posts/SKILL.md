---
name: webinar-linkedin-posts
description: When the user wants webinar LinkedIn promo posts — intro post, partner mirror, partner thought-leadership post, last-minute boost posts. Trigger phrases include "linkedin posts", "linkedin promo", "linkedin webinar posts", "thought leadership post", "boost posts", "webinar social posts". Run this AFTER the brief is filled out.
metadata:
  version: 0.1.0
---

# Webinar LinkedIn Posts

Produce the **5-post LinkedIn lineup** for one webinar. Two voices (Cerkl + partner), three cadence positions, one partner thought-leadership piece.

## Prerequisites

- Brief is filled out (especially: title, date, time, key learnings, partner perspective, social snippet)
- Tracking URLs exist: `cerkl_linkedin` and `<partner>_linkedin`

## The 5 posts

| # | Post | Voice | Send | Tracking URL |
|---|---|---|---|---|
| 1 | Intro post | Cerkl (company page or Tarek) | T-3w | `cerkl_linkedin` |
| 2 | Intro mirror | Partner | T-10d | `<partner>_linkedin` |
| 3 | Thought-leadership | Partner | T-10d | `<partner>_linkedin` |
| 4 | Boost (last-minute reg push) | Cerkl | T-2d | `cerkl_linkedin` |
| 5 | Boost (last-minute reg push) | Partner | T-2d | `<partner>_linkedin` |

For the boost posts (#4 and #5), provide **2–3 angle options** (urgency, conversational, short-and-direct) so the user can pick.

## Universal LinkedIn rules

> Reach is suppressed when the post body contains an outbound link. Put the registration link in the **first comment**, not the post body. Reference it at the end as "🔗 Registration link in comments". Hashtags: 2–3 max.

This applies to all 5 posts.

## Cerkl context to apply

- **Foundations ICP**: HR generalist scrolling LinkedIn — lead with the problem they're feeling, not the product category
- **Voice differentiation**: Cerkl posts are sharper and more declarative. Partner posts are personal and story-led. Don't make them sound the same.
- **No "demo" or "talk to sales" CTA** — registration is the only ask

## Reference

- [matt-frost-linkedin.md](../../matt-frost-april-2026/matt-frost-linkedin.md) — gold-standard structure (intro post + day-before with multiple angle options)
- [linkedin-writing-guide.md](../../../linkedin/linkedin-writing-guide.md) — Cerkl LinkedIn voice and format
- Generic skill (input only): `/Users/travisfoster/claude-code/cerkl/marketing/skills/social-content/SKILL.md`

## Output

Write to `<speaker-slug>-linkedin.md` in the event folder. Structure:

```
# LinkedIn Posts — <Webinar Title>

**Webinar:** ...
**Date:** YYYY-MM-DD
**Cerkl tracking URL:** ...
**Partner tracking URL:** ...

> LinkedIn note: registration link goes in the first comment, not post body.

---

## Post #1 — Intro (Cerkl, T-3w, post YYYY-MM-DD)
...

## Post #2 — Intro mirror (Partner, T-10d, post YYYY-MM-DD)
...

## Post #3 — Thought-leadership (Partner, T-10d, post YYYY-MM-DD)
...

## Post #4 — Boost (Cerkl, T-2d, post YYYY-MM-DD)
### Option A — Urgency
...
### Option B — Conversational
...
### Option C — Short and direct
...

## Post #5 — Boost (Partner, T-2d, post YYYY-MM-DD)
### Option A — ...
...
```

## Push update

After producing the posts, append an update block to the relevant file in `personal-assistant/projects/`. See [../../CLAUDE.md](../../CLAUDE.md) for the protocol.
