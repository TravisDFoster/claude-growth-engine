---
name: webinar-recap-clips
description: When the user wants to identify short YouTube clips from a webinar recording — timestamps, captions, titles, descriptions for the video editor. Trigger phrases include "recap clips", "youtube clips", "webinar clips", "key insights clips", "highlight clips", "post-webinar clips", "clip the webinar". Run this AFTER the recording transcript is available.
metadata:
  version: 0.1.0
---

# Webinar Recap Clips

From a webinar recording transcript, identify **3–5 short clips** (60–180 seconds each) that can be edited into standalone YouTube videos. This skill produces the **clip plan** (timestamps + scripts + metadata) — the actual video editing happens outside Claude.

## Prerequisites

- Webinar recording exists (Zoom or YouTube unlisted)
- **Transcript is available** — ideally with timestamps. If not, ask the user to generate one (Zoom auto-transcript, Otter, etc.) before running this skill.

## Inputs to gather

- Transcript file (paste or path)
- Number of clips wanted (default: 3–5)
- Preferred clip length (default: 60–180 seconds)
- YouTube channel context — is this for the main Cerkl channel or a series?

## How to pick clips

Look for moments that are:
- **Self-contained** — work without needing the rest of the webinar to make sense
- **Punchy** — ideally a memorable line, a tension/release, or a clear "here's what most people get wrong" framing
- **Aligned to the brief's Core Message** — clips should reinforce the webinar's main thesis, not random tangents
- **Mix of voices** — at least one Cerkl-led clip and one partner-led clip if both speak

Avoid:
- Polls, intros, housekeeping
- Sales-pitchy CTA moments
- Anything that requires preceding context to land

## What to produce per clip

For each clip:

- **Clip title** — short YouTube-friendly title (50–70 chars)
- **Source timestamp range** — `mm:ss – mm:ss` from the recording
- **Verbatim transcript excerpt** — the actual words in the clip (so the editor can confirm boundaries)
- **Suggested cuts** — internal "ums", repetitions, or off-topic asides to trim
- **YouTube description** — 2–3 sentences for the video page; includes the webinar registration page link or the on-demand replay link
- **Suggested thumbnail text overlay** — 3–6 words
- **Hashtags** — 3–5, topic-relevant

## Cerkl context to apply

- **Foundations ICP**: titles and thumbnails should pattern-match what an HR generalist would click on YouTube — problem-led, specific, concrete
- **Don't sell** — clips are top-of-funnel awareness; the description can mention Foundations once but the clip itself shouldn't pitch
- **Brand consistency**: titles in sentence case, not Title Case. No emojis in titles.

## Output

Write to `<speaker-slug>-recap-clips.md` in the event folder. One section per clip, plus a top "Source recording" section with the recording URL and transcript reference.

## Push update

After producing the clip plan, append an update block to the relevant file in `personal-assistant/projects/`. See [../../CLAUDE.md](../../CLAUDE.md) for the protocol.
