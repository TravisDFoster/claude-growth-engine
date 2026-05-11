# Paid YouTube Channel Context

## What this channel does
Production of YouTube video ads for paid distribution. The video itself follows a stable, polished pattern; the **hook** (first 5–10 seconds) is the test variable. New hooks are swapped in to experiment with which openings drive the highest watch-through and click rate.

## Current state
- Active YouTube channel
- 2 ads live
- Standard ad anatomy: 5–10s **hook** (variable, AI-generated via Google Flow) → 40–50s polished body (HeyGen voice-over + product showcase). Total length ~50–60s.
- Hook generation is the experimentation surface: many hooks tried, winners promoted into the polished pattern.

## Why we test hooks aggressively
- Watch-through on YouTube ads collapses after 3 seconds without a strong hook
- The body is high-cost to produce (HeyGen + showcase footage); the hook is low-cost (one Flow scene)
- Pattern-breaking, ICP-specific hooks outperform generic stock-style openers — they earn the next 50 seconds

## Hook anatomy (5–10s clip target)
- **VO line / on-screen text**: one tight idea, ICP-specific, pattern-break encouraged
- **Visual concept**: 2–3 shots max, generated in Google Flow video studio
- **Pain or positioning angle**: every hook should map to one ICP pain point or one Cerkl positioning line — never both, never neither

## What good looks like
- Hook is recognizable as Cerkl-relevant within 2 seconds (pain or positioning lands fast)
- Visual choice is unexpected — avoids stock office b-roll, generic "frustrated worker" tropes
- Last frame leads naturally into the polished body (visual or narrative continuity)
- Reproducible: a winning hook can be variant-tested (same VO, new visual, etc.) without rebuilding the body

## What to avoid
- Hooks that require lots of context to "land" — viewer has 3 seconds
- Hooks that target paid (Omni AI / 5,000+) buyers when running on Foundations campaigns — see [`shared/icp.md`](../../../shared/icp.md) for the split
- Generic "are you tired of X?" openers — pattern-recognized as ad in 1 second
- Hooks that promise something the polished body doesn't deliver (creates a watch-time spike but kills CTR)

## The learning loop
- Each batch is 20 hooks → Travis selects winners (production-ready) → winners are storyboarded → Flow prompts generated → rendered → tested in market
- Performance-validated winners are promoted into [`proven-hooks.md`](proven-hooks.md), which feeds every future batch as positive-pattern reference
- Failures (hooks that tested poorly) can also be noted in `proven-hooks.md` under a "what didn't work" section so the pattern isn't repeated
