# Cerkl Blog Editing Guide

A two-pass editing process for removing AI writing patterns and tightening prose before a post is published.

## Input and Output

- **Input:** A draft file at `blog-posts-draft/YYYY-MM-DD_[slug]_draft.md`
- **Output:** A finalized file at `blog-posts-live/YYYY-MM-DD_[slug]_live.md`

Do not modify or delete the original draft. Read it, run the editing process below, then write the final version to `blog-posts-live/` with the `_live.md` suffix. Preserve the original date and slug from the draft filename.

---

## Pass 1 — Structural Edit

Read the full draft before touching any sentences. Flag issues at the structure level first.

- **Argument order:** Does the most important insight come first, or is it buried? Move it up.
- **Paragraph length:** No single-sentence paragraphs except for deliberate emphasis. No paragraphs longer than 5–6 sentences without a break.
- **List overuse:** If two or more consecutive sections are bulleted lists, rewrite at least one as prose. Lists should not be the default structure for open-ended points.
- **Section balance:** Are any H2 sections thin (one paragraph)? Either expand them or fold them into an adjacent section.
- **Tone consistency:** Flag any section that shifts register — formal to casual, direct to hedging, confident to over-qualified. Pick one and hold it.
- **Redundancy:** Mark any paragraph that repeats a point already made. Cut the weaker version.

Do not rewrite yet. Finish the structural pass, then rewrite.

---

## Rewrite Pass

Fix everything flagged in Pass 1. Then work through the sentence-level issues below.

### Banned phrases and words

Cross-reference against [`references/phrases.md`](references/phrases.md) for the full list. Key categories:

**Throat-clearing openers** — cut and state the point directly.
- "Here's the thing:", "The truth is,", "It turns out", "Let me be clear"

**Emphasis crutches** — delete entirely.
- "Full stop.", "Let that sink in.", "Make no mistake"

**Adverbs** — kill all of them.
- "really", "just", "genuinely", "simply", "actually", "fundamentally", "crucially", "importantly"

**Filler phrases** — cut.
- "At its core", "In today's [X]", "It's worth noting", "At the end of the day", "When it comes to", "In a world where"

**Cercl-specific word list** — these appear constantly in AI-generated B2B content. Replace with plain language.
- delve, explore, underscore, highlights, crucial, robust, pivotal, empower, revolutionize, transformative, seamless, leverage, navigate, unpack, landscape, game-changer, deep dive

**Transition word overuse** — use sparingly. "Furthermore," "moreover," "in addition," and "additionally" signal AI pacing. Cut or restructure the sentence so the connection is implied.

**Elegant variation** — do not substitute synonyms to avoid repeating a word. If "employee communication" is the right phrase, use it twice. Unnecessary variation reads as evasive and confuses readers.

**Vague attributions** — never write "studies show," "research suggests," or "modern experts say" without a specific source. Either name the study/source or cut the attribution entirely and state the claim directly.

### Banned structures

Cross-reference against [`references/structures.md`](references/structures.md) for the full list. Key patterns:

**Binary contrasts** — state the point directly. "It's not X, it's Y" → just say Y.

**Negative listing** — don't build up through negation. "Not A. Not B. C." → just say C.

**False agency** — name the human actor. "The data suggests" → "The survey found." "The culture shifts" → "Employees changed how they work."

**Passive voice** — find the actor and put them first. "Decisions were made" → name who decided.

**Dramatic fragmentation** — no staccato sentences for manufactured emphasis. "Speed. That's it. That's the point." → write it as one sentence.

**Rule of three** — two items beat three. If you have three, cut the weakest one.

**Colon overuse** — colons belong in headings only when the format genuinely requires it. Don't use them to introduce a list in running prose when a sentence works fine.

### Line-level checks

Use [`references/examples.md`](references/examples.md) as before/after anchors when unsure what a fix should look like.

- Any adverbs remaining? Kill them.
- Any passive voice? Find the actor, make them the subject.
- Inanimate thing doing a human verb ("the decision emerges")? Name the person.
- Sentence starts with a Wh- word? Restructure it.
- Any "not X, it's Y" contrasts? State Y directly.
- Three consecutive sentences match length? Break one.
- Em-dash anywhere? Remove it. Use a comma or period.
- Vague declarative ("The implications are significant")? Name the specific implication.
- Narrator-from-a-distance ("Nobody designed this")? Put the reader in the scene.
- Meta-joiners ("The rest of this post...")? Delete.
- Safe or opinion-free take? Add a clear point of view. Internal comms practitioners want a recommendation, not a survey of perspectives.

---

## Pass 2 — Line Edit and Score

Re-read the rewritten draft. Run the line-level checklist one more time, then score.

| Dimension | Question | Score (1–10) |
|-----------|----------|--------------|
| Directness | Statements or announcements? | |
| Rhythm | Varied or metronomic? | |
| Trust | Respects reader intelligence? | |
| Authenticity | Sounds human? Has a point of view? | |
| Density | Anything still cuttable? | |

**Exit condition: 35/50 or higher.** If below 35, identify which dimensions are failing and rewrite only those sections. Re-score. Do not run the full checklist again.

---

## Finalize

Once the post scores 35/50 or higher:

1. Save the final version to `blog-posts-live/YYYY-MM-DD_[slug]_live.md` (preserve the date and slug from the draft filename).
2. Leave the original `blog-posts-draft/YYYY-MM-DD_[slug]_draft.md` file unchanged.
3. Append a brief edit log to the bottom of the live file in this format:

```
---
**Edit log**
- Final score: XX/50 (Directness X, Rhythm X, Trust X, Authenticity X, Density X)
- Major structural changes: <one line>
- Notable phrase/structure fixes: <one line>
```
