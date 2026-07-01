---
name: linkedin-editing
description: Edit a LinkedIn draft before its copy lands in the Jira CSV. Two quick passes (hook/tightness, then a hard compliance gate) plus a scaled score. Enforces linkedin-writing-guide.md so voice/policy rules are checked by a fresh pass, not self-graded by the drafter. Use inside linkedin-process.md (Step 4.5) or standalone on any drafts/ file.
---

# LinkedIn Editing

A short two-pass edit for a single LinkedIn draft. The blog has [`seo-blog-editing`](../../../seo-blog/skills/seo-blog-editing/SKILL.md); this is its scaled-down sibling for social copy. It exists because the LinkedIn writing guide is only a guardrail if something **checks** the draft against it with fresh eyes — a drafter grading its own output is the anti-pattern that lets hashtags, first-comment links, em-dashes, and "actually" slip through.

## Input and output

- **Input:** a draft at `channels/linkedin/drafts/YYYY-MM-DD_[type]_[slug].md`
- **Output:** the **same draft file**, edited in place, with a `## Edit log` block appended.

LinkedIn has no draft→live split (unlike the blog). The draft is the source of truth, so this skill finalizes it in place. Do not create a second file.

Load [`../../linkedin-writing-guide.md`](../../linkedin-writing-guide.md) and [`../../CONTEXT.md`](../../CONTEXT.md) first. The banned words/structures are shared with the blog — cross-reference these verbatim, do not fork them:
- [`../../../seo-blog/skills/seo-blog-editing/references/phrases.md`](../../../seo-blog/skills/seo-blog-editing/references/phrases.md)
- [`../../../seo-blog/skills/seo-blog-editing/references/structures.md`](../../../seo-blog/skills/seo-blog-editing/references/structures.md)
- [`../../../seo-blog/skills/seo-blog-editing/references/examples.md`](../../../seo-blog/skills/seo-blog-editing/references/examples.md) (before/after anchors)

The blog-specific items in those references (CTA variant names, FAQ schema, body markers, internal-link rules) do **not** apply to LinkedIn — take only the voice-level phrase/structure bans.

---

## Pass 1 — Hook and tightness

Read the whole caption first. Fix structure before wording.

- **Hook:** does line 1 stop the scroll on its own? If it opens with setup or context, cut to the line that actually hooks.
- **Tightness:** every line earns its place. Cut anything that repeats a point or over-explains. A reader should get the whole point in one scroll.
- **Length band** (from the writing guide's per-type table):
  - `carousel` / `short-video` — very short (2–4 lines / 2–3 lines); the asset carries the content
  - `static-theme` — 3–5 short paragraphs
  - `static-blog` — 2–4 short paragraphs
  - `poll` — 3–4 short paragraphs
- **Scannability:** line breaks between beats, no wall of text.
- **Payoff + CTA:** the point lands, and the destination link (registration / blog) is present **in the caption**.

Do not rewrite word-by-word yet. Finish the pass, then rewrite.

## Rewrite pass — voice + banned list

Fix what Pass 1 flagged, then run the banned list (cross-referenced from the blog references above):

- **Adverbs — kill all:** actually, really, just, genuinely, simply (plus fundamentally, crucially, importantly).
- **Binary contrasts / negative listing:** "It's not X, it's Y" and "Not A. Not B. C." → state the positive directly.
- **Em-dashes:** none. Use a comma, period, or parentheses.
- **Filler openers:** "At its core," "when it comes to," "in a world where," "here's the thing."
- **Dramatic fragmentation** for manufactured emphasis, **false agency** (name the human actor), **elegant variation** (repeat the right word instead of reaching for a synonym).
- **Engagement-bait:** "comment YES if…", "tag someone who…", lowercase-thought-leader voice.

## Pass 2 — Compliance gate + score

### Compliance gate (hard pass/fail — all must pass)

This is deterministic; most of it is greppable. If any check fails, fix and re-run this gate — a draft cannot exit editing until every line is `pass`.

| # | Check | Fail signal |
|---|---|---|
| 1 | No hashtags | any `#` in the caption |
| 2 | Link in the caption, not the comments | a "first comment:" / "link in comments" line carrying the destination URL |
| 3 | No em-dashes | any `—` |
| 4 | No banned adverbs | actually / really / just / genuinely / simply |
| 5 | No binary-contrast / negative-listing structures | "not X, it's Y" / "Not A. Not B." |
| 6 | No engagement-bait | "comment YES", "tag someone" |
| 7 | Caption within the per-type length band | paragraph/line count outside the band above |
| 8 | Dates `YYYY-MM-DD` in any meta lines | other date formats |

**Exception handling:** a hashtag or comment-link is allowed only if the draft carries an explicit, one-line campaign-exception note the writer flagged (per the writing guide). Absent that note, it fails.

### Score (scaled for short copy)

| Dimension | Question | Score (1–10) |
|---|---|---|
| Hook | Does line 1 stop the scroll? | |
| Tightness | Every line earns its place? Within band? | |
| Voice | Cerkl-plain, no banned words/structures? | |
| Payoff | Clear takeaway + CTA/link in the caption? | |

**Exit condition: 28/40 or higher AND the compliance gate fully passed.** If below 28, rewrite only the failing dimension and re-score. The compliance gate is not negotiable regardless of score.

---

## Finalize

Append this block to the bottom of the draft (keep the caption + asset sections above it intact):

```
## Edit log
- Compliance: hashtags 0 · em-dashes 0 · banned adverbs 0 · link-in-caption yes · engagement-bait 0 · length <n> paras (band X–Y) · <PASS/exception note>
- Score: XX/40 (Hook X, Tightness X, Voice X, Payoff X)
- Fixes: <one line on what changed>
```

**Return:** the draft path + the score line + a one-word compliance verdict (`PASS` / `fixed`). If this runs as a subagent inside `linkedin-process.md`, return those values — the orchestrator inserts the edited caption into the CSV. Do not edit the CSV from here.

## Standalone use

`"Edit the LinkedIn draft for [slug]"` — run the two passes on one `drafts/` file and finalize in place. For a whole week, `linkedin-process.md` calls this per draft between drafting (Step 4) and CSV insert (Step 5).
