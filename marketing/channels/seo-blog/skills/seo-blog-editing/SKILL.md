# SEO Blog Editing

A two-pass editing process for removing AI writing patterns and tightening prose before a post is published.

## Input and output

- **Inputs:**
  - `/Users/travisfoster/claude-code/cerkl/marketing/channels/seo-blog/blog-posts-draft/YYYY-MM-DD_[slug]_draft.md` (the prose to edit)
  - `/Users/travisfoster/claude-code/cerkl/marketing/channels/seo-blog/blog-posts-pre-writing/YYYY-MM-DD_[slug]_pre-writing.md` (the source of the Properties block — same slug, may have a different date)
- **Output:** `/Users/travisfoster/claude-code/cerkl/marketing/channels/seo-blog/blog-posts-live/YYYY-MM-DD_[slug]_live.md`

Do not modify or delete the original draft. Read it, run the process below, then write the final version to `blog-posts-live/` with the `_live.md` suffix. Preserve the slug from the draft filename. Date the live file with the same date as the draft *unless* this is a re-edit of a previously-published post — in that case advance the date (and confirm with the user before overwriting an existing live file with the same date).

If the pre-writing file is missing or its Properties section is incomplete: **stop and surface the gap.** Do not invent or guess properties; the pre-writing file is the source of truth for the Webflow CMS fields.

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
- Any internal link doing a "See [URL]" / "Click here" / "→ [URL]" callout, or using the URL path as anchor text? Rewrite so the link wraps a meaningful noun phrase inside the existing sentence. See the Internal linking rules in [`../seo-blog-drafting/SKILL.md`](../seo-blog-drafting/SKILL.md#internal-linking).
- Any internal link in root-relative form (`/blog/...`, `/broadcast/...`) instead of absolute (`https://cerkl.com/...`)? Convert. Markdown artifacts have to be clickable during review.
- **Voice and byline.** Unless the post was explicitly commissioned as a first-person editorial / POV piece, hold standard Cerkl voice (practical, direct, second/third person). Flag and convert any first-person founder/marketer narration ("I run marketing at Cerkl," "the horse I am riding") and remove any `Author` / `Publish date` byline fields from the Properties block — standard posts carry no personal byline.
- **CTA variant names.** Every CTA variant in the Properties block and the body markers must be a real name from the canonical catalog in [`../seo-blog-pre-writing/SKILL.md`](../seo-blog-pre-writing/SKILL.md#cta-variant-selection). Reject invented names (e.g., `Foundations Free Middle`, `Foundations Free Bottom`). Top CTA is blank/`Nothing` only when Primary Solution is Educational or Omni AI; a Foundations or email-focused post carries a real Top variant (`Email/Gmail/Outlook General Top`).

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

### Step 1 — Insert the five visible body markers

The drafting skill does not emit body markers — it can't know where the natural pivot lands until the post is written. Editing owns marker placement, post-scoring.

The markers serve two purposes at once:
1. They tell Furqan where to insert Top / Middle / Bottom CTA components in Webflow.
2. They label the **Content 1** and **Content 2** Rich Text field boundaries, since Webflow's blog template renders as: Top CTA → Content 1 → Middle CTA → Content 2 → Bottom CTA → FAQ.

Use **bold-bracket markers**, not HTML comments. Google Drive's markdown→Doc converter silently strips HTML comments, so any `<!-- ... -->` syntax becomes invisible in the Doc that Furqan actually works from. Bold-bracket markers render as visible bold text in the Doc.

Walk the edited body and insert these five markers in order. Pull the CTA variant names from the pre-writing file's Properties block — never invent them.

- `**[Top CTA — <variant name>]**` — immediately after the H1, before the intro paragraph. If the variant is `Nothing` (Omni AI / Educational posts), still emit the marker with `Nothing` as the variant so Furqan knows to skip the insertion point. No judgment needed on placement.

- `**[Content 1]**` — on its own line, immediately after the Top CTA marker. Marks where the Content 1 Rich Text field begins.

- `**[Middle CTA — <variant name>]**` — **past the structural midpoint, not at it.** The first half of the body is the problem / pain / diagnosis arc; the second half picks up the operational fixes. Place the marker after the H2 section that *completes* the diagnosis arc — typically the section after the one a naive midpoint pass would pick. Aim for roughly 55–65% of the way through the body by H2 count, biased later, not earlier. If the Middle CTA variant is thematically tied (e.g., `Email Analytics Middle` pairs with a measurement section), prefer placing the marker so that themed section is the *first* one of the second half.

  This marker is also the **Content 1 → Content 2 split**: everything between `**[Content 1]**` and `**[Middle CTA — ...]**` is Furqan's Content 1 Rich Text paste; everything between `**[Content 2]**` and `**[Bottom CTA — ...]**` is the Content 2 paste.

  **Sanity check:** count H2s in the body (excluding the FAQ and FAQ Schema H2s). For `n` body H2s, the Middle CTA should sit after H2 #⌈n × 0.55⌉ through #⌈n × 0.65⌉ — not earlier. If the natural pivot really is earlier, write a one-line note in the edit log explaining why (and aim to revisit on the next post in the same shape).

  **Content 1 / Content 2 balance check:** the two halves should be within roughly 30/70 to 70/30 of each other by word count. Lopsided splits (90/10) mean the Middle CTA marker is in the wrong place or the draft itself is unbalanced — fix before scoring.

- `**[Content 2]**` — on its own line, immediately after the Middle CTA marker. Marks where the Content 2 Rich Text field begins.

- `**[Bottom CTA — <variant name>]**` — after the closing paragraph of the body, followed immediately by a `---` separator before the `## Frequently Asked Questions` heading.

### Step 2 — Assemble the live file in this exact order

1. **Properties block at the top.** Copy the `## Properties` section verbatim from the pre-writing file. The block carries the Webflow CMS fields downstream owners (Furqan, Webflow) need: Title, Slug, Top 3 Organic Search Keywords, Primary Solution, Top/Middle/Bottom CTA names, Primary Category, All Categories, Meta Title, Meta Description. Do not re-derive or re-word — pre-writing is canonical. (Legacy pre-writing files may use `Secondary Category` instead of `All Categories` — that's a historical single-value field; rename to `All Categories` when copying forward, since Webflow's actual CMS field is the multi-tag `All Categories`.)
2. **A `---` separator** after the properties block.
3. **The edited post body, with the five body markers inserted per Step 1.** The full body shape, top to bottom: `# H1` → `**[Top CTA — <variant>]**` → `**[Content 1]**` → first-half H2 sections (problem/diagnosis arc) → `**[Middle CTA — <variant>]**` → `**[Content 2]**` → second-half H2 sections (operational fixes, ending with forward-moving takeaway) → `**[Bottom CTA — <variant>]**` → `---` → `## Frequently Asked Questions` (or `## How To`) → `## FAQ Schema` (or `## How-to Schema`) with the JSON-LD fenced code block. Recording-URL placeholders (e.g., `<RECORDING_URL>`) must be resolved to a real URL before saving; if you don't have one, stop and ask the user — do not ship a placeholder.

   **Validation gate before saving:** if any of the five body markers are missing, if any CTA marker is missing its variant name (e.g., `**[Top CTA]**` without the `— <variant>` suffix), if any CTA variant name is not in the canonical catalog in [`../seo-blog-pre-writing/SKILL.md`](../seo-blog-pre-writing/SKILL.md#cta-variant-selection) (no invented names like `Foundations Free Bottom`), if a standard (non-editorial) post still carries first-person narration or an `Author` / `Publish date` byline, if the Content 1 / Content 2 word-count split is outside the 30/70–70/30 band, or if the schema block is missing / doesn't parse / has a Q&A count that doesn't match the FAQ section's H3 count — **stop and fix.** The shape above is required, not optional.

4. **A `---` separator** before the edit log.
5. **The edit log block:**

```
**Edit log**
- Final score: XX/50 (Directness X, Rhythm X, Trust X, Authenticity X, Density X)
- Major structural changes: <one line>
- Notable phrase/structure fixes: <one line>
- Middle CTA placement: after H2 "<section title>" (position N of M body H2s, ~XX%). <If outside the 55–65% band, one-line reason.>
- Content 1 / Content 2 balance: <Content 1 word count> / <Content 2 word count> (<ratio, e.g., 48/52>). <If outside 30/70–70/30, one-line reason.>
- Verification: <one line on em-dash count, banned-phrase count, recording URL filled, properties block verbatim from pre-writing, all 5 body markers present and correctly named (Top CTA, Content 1, Middle CTA, Content 2, Bottom CTA — each CTA marker carrying its variant name), FAQ-schema JSON-LD present and Q&A count matches FAQ count>
```

6. **The image candidates block** — appended right after the edit log (no new `---` separator; the publishing skill's strip recipe catches everything from `\n---\n**Edit log**...` to end of file, so this block stays QA-side and never reaches the Drive doc).

   Read [`/Users/travisfoster/claude-code/cerkl/marketing/design/blog-assets/PRINCIPLES.md`](/Users/travisfoster/claude-code/cerkl/marketing/design/blog-assets/PRINCIPLES.md) once. The "Picking a template" guide there is the source of truth. The three templates available today:

   - **`numbered-stack`** — vertical ordered list of 3-5 named concepts (maturity ladders, named steps, priority hierarchies)
   - **`letter-strip`** — horizontal 3-6 acronym letters or named pillars
   - **`stat-hero`** — one dominant stat + framing (best for OG / social preview)

   Scan the post for content that fits. For each genuine fit (max 3), append a numbered entry naming the template and pre-filling the content slots verbatim from the post. Block format:

   ```
   **Image candidates**

   1. **stat-hero** — `$28,250` per US employee on benefits (the lede stat). Best for OG / social preview.
      - Stat: `$28,250`
      - Tag: "Spent per US employee, per year, on benefits."
      - Takeaway: "Most never use what they have."
      - Source: U.S. Bureau of Labor Statistics

   2. **numbered-stack** — Four-rung maturity ladder (Compliance → Connection). Best for in-body, "Why it happens" section.
      - Rungs: 01 Compliance · 02 Clarity · 03 Relevance · 04 Connection
      - Marker: "Most teams sit here" between 02 and 03
   ```

   **Rules:**
   - **Mandatory step, can output "none."** If no concept pattern in the post maps to any of the three templates, write `**Image candidates:** none — no concept pattern fits the available templates.` Skipping the step entirely is a bug.
   - **No force-fit.** A 4-bullet list that isn't really a sequence shouldn't become a `numbered-stack`. A stat that isn't a scroll-stopper shouldn't become a `stat-hero`. If you have to argue for the fit, drop the candidate.
   - **Pre-fill content slots verbatim** from the post so a downstream rendering agent doesn't have to re-derive
   - **Order by leverage** — OG/social card (`stat-hero`) first when applicable; in-body diagrams after, in the order they appear in the post
   - **Do not render** HTML or PNG here. Rendering is a separate manual step via `cerkl/marketing/design/blog-assets/render.sh`.

Save to `blog-posts-live/YYYY-MM-DD_[slug]_live.md`. Leave the original draft unchanged.

**Return:** the `_live.md` path + the final score line. The downstream `seo-blog-publishing` skill handles Drive upload (Edit log stripped; Properties block + CTA markers + FAQ schema kept so Furqan has everything he needs in one Doc) and Jira CSV row update — editing's job ends at a publication-ready file on disk.
