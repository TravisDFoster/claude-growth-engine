---
name: webinar-recap-clips
description: When the user wants to identify short vertical clips (YouTube Shorts) from a webinar recording, plus LinkedIn cross-post copy — timestamps, captions, YouTube descriptions, and LinkedIn post copy for the video editor and social poster. Trigger phrases include "recap clips", "webinar shorts", "youtube shorts", "linkedin clips", "webinar clips", "key insights clips", "highlight clips", "post-webinar clips", "clip the webinar". Run this AFTER the cleaned transcript is available (i.e., after `webinar-ingest`).
metadata:
  version: 0.3.0
---

# Webinar Recap Clips

From a cleaned webinar transcript, identify **3–5 vertical Shorts** (≤60 seconds each). Each clip is a **YouTube Short that is also cross-posted to LinkedIn**. This skill produces the **clip plan** (timestamps + verbatim excerpts + YouTube metadata + LinkedIn post copy) — the actual video editing happens outside Claude.

**Primary destination:** YouTube Shorts (Cerkl channel).
**Default cross-post:** LinkedIn (Cerkl page + speaker repost if applicable). Every Short gets a LinkedIn cross-post by default — don't skip the LinkedIn copy unless the user explicitly says LinkedIn-only or YouTube-only.

The YouTube description and the LinkedIn post copy are **different deliverables with different voices** — don't reuse one for the other.

## Prerequisites

- `webinar-ingest` has been run — `<speaker-slug>-transcript-clean.md` and `<speaker-slug>-deck-extract.md` exist in the event folder
- Source recording URL is known (Zoom cloud or YouTube unlisted) so the editor can pull the source

## Inputs to gather

- Path to the cleaned transcript file
- Number of clips wanted (default: 3–5)
- Source recording URL (Zoom cloud or YouTube unlisted) and on-demand replay link
- Whether the partner/speaker (e.g., Matt Frost) will repost on LinkedIn — affects voicing of one variant of LinkedIn copy

## Format constraints (every clip)

- **Length**: ≤60 seconds — aim 30–55s. Hard cap at 60.
- **Aspect ratio**: 9:16 vertical
- **Captions**: burned-in, since LinkedIn autoplays muted
- **Hook**: first 2 seconds must land a tension or claim — no "hi everyone, today we're talking about…"

## How to pick clips

Look for moments that are:
- **Self-contained** — land in <60s without needing the rest of the webinar
- **Punchy** — a memorable line, a contrarian framing, or a clear "here's what most people get wrong"
- **Aligned to the brief's Core Message** — reinforce the webinar's main thesis, not tangents
- **Mix of voices** — at least one Cerkl-led clip and one partner-led clip if both speak

Avoid:
- Polls, intros, housekeeping, transitions
- Sales-pitchy CTA moments — clips are top-of-funnel
- Anything that requires preceding context to land

## What to produce per clip

For each clip, write a section with:

**Editor-facing (source material):**
- **Clip title** — internal label for the editor (e.g., "Compliance proof gap")
- **Source timestamp range** — `mm:ss – mm:ss` from the recording, length in seconds
- **Speaker** — who is on camera
- **Verbatim transcript excerpt** — the actual words, so the editor can confirm boundaries
- **Suggested trims** — "ums", repetitions, off-topic asides to cut to fit ≤60s
- **On-screen text / caption emphasis** — 1–2 short phrases to bold/highlight in burned-in captions (the punch line)

**YouTube Shorts metadata (primary post):**
- **Shorts title** — ≤60 chars, sentence case, ends with `#Shorts`
- **Shorts description** — 2–4 sentences for the YouTube video page. Repository of the idea, slightly more context than the LinkedIn post; pointer to on-demand replay link; one Foundations mention max
- **YouTube hashtags** — 3–5, topic-relevant; include `#Shorts`

**LinkedIn cross-post copy (different voice, different format):**
- **LinkedIn post copy — Cerkl voice**: 80–150 words, hook on line 1, line breaks for scannability, ends with a soft pointer to the on-demand replay. List 3–5 hashtags at the bottom. Follow [`/Users/travisfoster/claude-code/cerkl/marketing/channels/linkedin/linkedin-writing-guide.md`](/Users/travisfoster/claude-code/cerkl/marketing/channels/linkedin/linkedin-writing-guide.md). **Do not reuse the YouTube description verbatim** — LinkedIn rewards a stronger conversational hook and native framing.
- **LinkedIn post copy — speaker voice** (only if the speaker will repost): same length, first person from the speaker's POV, lighter on Cerkl-product framing
- **LinkedIn hashtags** — 3–5, topic-relevant (HR, Total Rewards, Benefits Communication, etc.); typically different/fewer than the YouTube set

## Cerkl context to apply

- **Foundations ICP**: hooks should pattern-match what an HR/Total Rewards leader would stop scrolling for — problem-led, specific, concrete
- **Don't sell** — clips and post copy are awareness; the post can point to the replay once but the clip itself shouldn't pitch
- **Brand voice**: plain language, sentence case, no emojis unless the speaker's own LinkedIn voice uses them

## Output

Write to `<speaker-slug>-recap-clips.md` in the event folder. Structure:

1. **Source recording** — recording URL, transcript file reference, on-demand replay link
2. **Clip plan summary** — one-line table of all clips (title, timestamp, length, speaker)
3. **Per-clip sections** — full details per the list above (editor block + YouTube block + LinkedIn block)
4. **Posting cadence suggestion** — proposed dates to space out the clips (default: 1/week starting the week after the recording goes on-demand). YouTube Short publishes first; LinkedIn cross-post goes the same day or next morning.

## Push update

After producing the clip plan, append an update block to the relevant file in `personal-assistant/projects/`. See [../../CLAUDE.md](../../CLAUDE.md) for the protocol.
