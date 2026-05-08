---
name: seo-blog-editing
description: Use when finalizing a Cerkl SEO blog draft for publication — runs a two-pass editing process (structural edit, sentence-level rewrite, line edit, score) to remove AI writing patterns and tighten prose. Triggers on phrases like "edit the [slug] draft", "run editing on this blog post", "finalize this draft", "score this draft". Prerequisite: a draft at `blog-posts-draft/`. Output: `blog-posts-live/YYYY-MM-DD_[slug]_live.md` plus a Drive Doc URL.
metadata:
  version: 0.1.0
---

# SEO Blog Editing

A two-pass editing process for removing AI writing patterns and tightening prose before a post is published.

## Input and output

- **Input:** `/Users/travisfoster/claude-code/cerkl/marketing/channels/seo-blog/blog-posts-draft/YYYY-MM-DD_[slug]_draft.md`
- **Output:** `/Users/travisfoster/claude-code/cerkl/marketing/channels/seo-blog/blog-posts-live/YYYY-MM-DD_[slug]_live.md`

Do not modify or delete the original draft. Read it, run the process below, then write the final version to `blog-posts-live/` with the `_live.md` suffix. Preserve the original date and slug from the draft filename.

---

## Pass 1 — Structural edit

Read the full draft before touching any sentences. Flag issues at the structure level first.

- **Argument order:** Does the most important insight come first, or is it buried? Move it up.
- **Paragraph length:** No single-sentence paragraphs except for deliberate emphasis. No paragraphs longer than 5–6 sentences without a break.
- **List overuse:** If two or more consecutive sections are bulleted lists, rewrite at least one as prose. Lists should not be the default for open-ended points.
- **Section balance:** Are any H2 sections thin (one paragraph)? Either expand them or fold them into an adjacent section.
- **Tone consistency:** Flag any section that shifts register — formal to casual, direct to hedging, confident to over-qualified. Pick one and hold it.
- **Redundancy:** Mark any paragraph that repeats a point already made. Cut the weaker version.

Do not rewrite yet. Finish the structural pass, then rewrite.

---

## Rewrite pass

Fix everything flagged in Pass 1. Then work through the sentence-level issues below.

### Banned phrases and words

Cross-reference [`references/phrases.md`](references/phrases.md) for the full list. Key categories:

**Throat-clearing openers** — cut and state the point directly.
- "Here's the thing:", "The truth is,", "It turns out", "Let me be clear"

**Emphasis crutches** — delete entirely.
- "Full stop.", "Let that sink in.", "Make no mistake"

**Adverbs** — kill all of them.
- "really", "just", "genuinely", "simply", "actually", "fundamentally", "crucially", "importantly"

**Filler phrases** — cut.
- "At its core", "In today's [X]", "It's worth noting", "At the end of the day", "When it comes to", "In a world where"

**Cerkl-specific word list** — replace with plain language.
- delve, explore, underscore, highlights, crucial, robust, pivotal, empower, revolutionize, transformative, seamless, leverage, navigate, unpack, landscape, game-changer, deep dive

**Transition word overuse** — use sparingly. "Furthermore," "moreover," "in addition," and "additionally" signal AI pacing. Cut or restructure so the connection is implied.

**Elegant variation** — do not substitute synonyms to avoid repeating a word. If "employee communication" is the right phrase, use it twice.

**Vague attributions** — never write "studies show," "research suggests," or "modern experts say" without a specific source. Either name the source or cut the attribution.

### Banned structures

Cross-reference [`references/structures.md`](references/structures.md) for the full list. Key patterns:

**Binary contrasts** — "It's not X, it's Y" → just say Y.

**Negative listing** — "Not A. Not B. C." → just say C.

**False agency** — name the human actor. "The data suggests" → "The survey found." "The culture shifts" → "Employees changed how they work."

**Passive voice** — find the actor and put them first.

**Dramatic fragmentation** — no staccato sentences for manufactured emphasis. "Speed. That's it. That's the point." → write it as one sentence.

**Rule of three** — two items beat three. If you have three, cut the weakest.

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

## Pass 2 — Line edit and score

Re-read the rewritten draft. Run the line-level checklist one more time, then score.

| Dimension | Question | Score (1–10) |
|-----------|----------|--------------|
| Directness | Statements or announcements? | |
| Rhythm | Varied or metronomic? | |
| Trust | Respects reader intelligence? | |
| Authenticity | Sounds human? Has a point of view? | |
| Density | Anything still cuttable? | |

**Exit condition: 35/50 or higher.** If below, identify which dimensions are failing and rewrite only those sections. Re-score. Do not run the full checklist again.

---

## Finalize

Once the post scores 35/50 or higher:

1. Save the final version to `blog-posts-live/YYYY-MM-DD_[slug]_live.md` (preserve the date and slug from the draft filename).
2. Leave the original draft unchanged.
3. Append a brief edit log to the bottom of the live file:

```
---
**Edit log**
- Final score: XX/50 (Directness X, Rhythm X, Trust X, Authenticity X, Density X)
- Major structural changes: <one line>
- Notable phrase/structure fixes: <one line>
```

4. **Publish to Drive as a Google Doc.** Load and follow [`/Users/travisfoster/claude-code/cerkl/skills/md-to-drive/SKILL.md`](/Users/travisfoster/claude-code/cerkl/skills/md-to-drive/SKILL.md) with:
   - **Source file:** the `_live.md` file just written
   - **Cleanup:** apply the Edit-log strip recipe in that skill — the trailing `---\n**Edit log**...` block is QA metadata, not customer-facing content
   - **Destination:** default (Claude-Uploads folder)
   - **Naming:** default convention (`YYYY-MM-DD — <H1 title>` with em-dash)

   Report the resulting Doc URL in the handoff to the user, immediately after the final score line. For bulk-edit sessions where multiple subagents finish in parallel, each subagent invokes `md-to-drive` independently for its own file — single-file inline uploads, no central batching needed.

   **Skip the Drive upload** only when the user explicitly says "don't upload" / "skip Drive" / "local only," or when the post is being held back from publication for review. If uncertain, ask.
