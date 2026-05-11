---
name: paid-youtube-hook-batch
description: When the user wants to brainstorm, generate, or draft new YouTube ad hook ideas — the 5–10 second openers that swap into the polished paid YouTube ad. Trigger phrases include "generate hooks", "new hook batch", "20 youtube hooks", "brainstorm video hooks", "new paid youtube hooks", "draft hooks for the youtube ad". Always produces 20 ideas in a dated batch folder, seeded by ICP pain points, Broadcast positioning, and the proven-hooks library.
metadata:
  version: 0.1.0
---

# Paid YouTube — Hook Batch Generator

Generate 20 hook ideas (5–10s YouTube ad openers) in one batch. Each hook gets a VO line, a one-sentence visual concept, and an angle tag (pain or positioning). Output is a single `ideas.md` file in a new dated batch folder, ready for selection.

## Prerequisites

- `proven-hooks.md` exists at `../../proven-hooks.md` (it does — empty seed is fine for the first batch)
- ICP and Broadcast context loaded via the channel `CLAUDE.md`

## Inputs to ask for

If any are missing, ask before generating. Don't guess.

1. **ICP focus** — Foundations, Paid (Omni AI), or mixed? (Default: Foundations.)
2. **Angle mix** — pain-led, positioning-led, or skewed pain? (Default: **skewed pain — 15 pain, 5 positioning**. IC buyers self-identify by lived pain before they're brand-aware. Positioning hooks are warm-audience material; we lean cold.)
3. **Theme / experiment hypothesis** *(optional)* — anything specific driving this batch? (e.g., "test hooks for the new measurement feature", "challenge competitor X's positioning", "lean into operations leaders, not formal IC managers"). Skip if generic.
4. **Batch date** *(usually today)* — `YYYY-MM-DD`.

## Conventions to enforce

- **Batch folder name:** `<YYYY-MM-DD>-batch/` — created at the channel root, e.g., `2026-05-08-batch/`
- **File created:** `<batch-folder>/ideas.md` — copied from [`../../templates/hook-batch-template.md`](../../templates/hook-batch-template.md)
- **Hook IDs:** `H01` through `H20` — zero-padded, sequential
- **VO line length:** 12–25 words (5–10s spoken pace)
- **Visual concept:** one sentence — keep it tight, Flow handles the heavy lifting

## What to read before generating

In this order:

1. **`../../proven-hooks.md`** — what's worked, what hasn't, emerging pattern observations. Bias toward proven patterns. Avoid repeating flops.
2. **`/Users/travisfoster/claude-code/cerkl/shared/icp.md`** — pain points and qualification signals per ICP segment.
3. **`/Users/travisfoster/claude-code/cerkl/shared/broadcast.md`** — positioning lines and product framing. Use the actual phrasing, don't paraphrase into something weaker.
4. **`../../CONTEXT.md`** — channel hook anatomy, what good looks like, what to avoid.

## The core criterion: land on the lived experience, not the feature

This is the single rule that separates good hooks from generic ad copy:

> A hook should evoke a **specific psychological moment** an IC / comms-owner actually lives through — not name a product capability that solves it.

**Test:** if you removed Cerkl from the picture entirely, would the VO line still describe a real moment in this person's week? If yes, the hook is experience-led. If no, it's feature-led — rewrite it.

### Experience-led (do this)

- "You sent the all-staff email three days ago. You still have no idea if anyone read it." — the experience of post-send uncertainty
- "It took you four hours to write the leadership update. It's already eight emails deep in their inbox." — the experience of high effort vs. low signal
- "Why does the same email look fine on your screen and broken on every other Outlook in the building?" — the experience of bewildered frustration
- "It's been eight weeks since you asked IT for an updated employee list. You're still pulling it from the intranet org chart." — the experience of being blocked, then routing around it

### Feature-led (don't do this)

- "Get instant read receipts on every email you send." — names a feature
- "Build audiences by department in 90 seconds without IT." — names a feature
- "Send to 25,000 employees per minute." — names a metric
- "Free forever, no contract." — pitch language, not a moment

Feature-led copy belongs in the **polished body** of the ad — never in the hook. The hook's only job is to make the IC say "that's me" in two seconds.

## How to generate the 20

Distribute across pain and positioning per the requested mix. Within each, **vary the pattern**:

- **Pattern types to mix in** (don't make all 20 the same shape):
  - POV ("You spent your whole morning…")
  - Direct address ("Internal comms team — read this.")
  - Stat-led ("83% of your employees never opened the last email.")
  - Visual-first (a striking image/scene with minimal VO)
  - Question-led ("Why do your most important emails get the least attention?")
  - Pattern-break (unexpected setting, unusual subject, dry humor)
  - Specific role call-out ("If you're the office manager who somehow inherited all-hands emails…")
  - Negative space (admit a problem your product *doesn't* solve, then pivot)

- **Across the 20, hit at least 6 distinct lived moments** (don't 20-variant a single moment). Pull from `icp.md` "Key Qualification Signals" and use cases — but translate each into a specific moment (e.g., "no segmentation" → "the moment you realize you sent the warehouse memo to corporate again").

- **Across the 20, hit at least 3 distinct positioning lines** for positioning-led hooks. Pull from `broadcast.md`.

- **For every hook, the moment must be readable in ≤2 seconds.** If you can't picture the specific instant the IC lives through by reading just the VO line, rewrite it.

## Visual rules — keep Flow-friendly

Flow renders short clips best when each shot has one subject, one setting, one action. Hard rules:

- **One subject** per visual (not "a wall of phones", not "43 sticky notes")
- **One setting** (a desk, a meeting room, a black title card — not a multi-room montage)
- **One action** (refreshing a folder, hovering a cursor, looking at a screen — not three things at once)
- **Specific not generic** — "phone face-down on a wood desk, screen dark" beats "phone on a desk"
- **Title-card minimalism is fine** — black screen + line of text reads as confident, not lazy
- **Avoid:** conveyor belts, multi-screen montages, anything with text or UI you need rendered legibly (Flow struggles with on-screen text — add text in post)

If the visual concept needs more than one sentence to describe, simplify it.

## What to avoid (per `CONTEXT.md` + this skill's core criterion)

- **Feature-pointing in the hook** — "get read receipts", "build audiences in 90 seconds", "free forever no contract". Move these to the body.
- **Generic "are you tired of X?" openers** — pattern-recognized as ad in 1 second
- **Visual complexity Flow can't render** — multiple subjects, on-screen text it has to read, montages, conveyor belts, anything with >1 setting
- **Stat-led hooks that drift toward feature-marketing** — a stat about *the IC's life* is fine ("you've opened the draft seven times this morning"); a stat about *the product* ("25,000 emails per minute") is not
- **Hooks needing setup to land** — viewer has 3 seconds
- **Foundations-targeted hooks naming enterprise pain** (5,000+ HQ, IT involvement, deskless workforce) — those belong in Paid-segment batches
- **Hooks that promise something the polished body doesn't deliver**

## Output

Write directly to `<batch-folder>/ideas.md`, copied from the template with placeholders filled. **Create the batch folder if it doesn't exist.** Do not modify `proven-hooks.md` — that's append-only and only after performance signal exists.

## Render the interactive HTML selection sheet

After `ideas.md` is written, **dispatch a sub-agent** to render the markdown as an interactive HTML file at the sibling path `<batch-folder>/ideas.html`. The HTML provides a checkbox-driven selection UI with a "Copy Selections" button that produces a paste-ready text block — Travis opens the HTML in a browser, picks winners, clicks copy, pastes back into chat.

Sub-agent brief (paste verbatim, adjust the path):

```
Run the md-to-html skill on <batch-folder>/ideas.md with artifact type `hook-batch`.

1. Read /Users/travisfoster/claude-code/cerkl/skills/md-to-html/SKILL.md
2. Read /Users/travisfoster/claude-code/cerkl/skills/md-to-html/reference-hook-batch.html — the canonical visual language and required JS for selection + copy-to-clipboard behavior.
3. Read the source markdown at <batch-folder>/ideas.md.
4. Write the HTML at <batch-folder>/ideas.html, self-contained per the skill's quality bar. Each hook card must include `data-id` and `data-vo` attributes (the copy script reads them) — escape any inner quotes in the `data-vo` value.
5. Return only the output path + a one-line confirmation. Do NOT echo the HTML body back to the parent.
```

Dispatching to a sub-agent keeps ~30KB of HTML out of the main context window. Don't render inline in the orchestrator's context.

## Next-step prompt to print to the user

After writing `ideas.md` AND the rendered `ideas.html`, print:

```
Done. 20 hooks in <batch-folder>/ideas.md (+ ideas.html for interactive selection).

Open <batch-folder>/ideas.html in a browser. Click cards to select your winners
(typically 3–5 of 20), then click "Copy Selections" and paste back into this chat.
Add a one-line reason per pick where indicated, and I'll run paid-youtube-hook-select.

Then for each winner:
  paid-youtube-hook-storyboard  → shot list
  paid-youtube-hook-prompts     → Google Flow prompts

Render in Google Flow → ship → append performance signal to proven-hooks.md.
```

## Push update

After generating a batch, append an update block to the relevant project file in `personal-assistant/projects/` (likely `youtube.md` or `advertising.md` — check before writing). See [../../CLAUDE.md](../../CLAUDE.md) for the protocol.
