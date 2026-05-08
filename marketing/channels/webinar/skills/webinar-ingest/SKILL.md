---
name: webinar-ingest
description: User-invoked skill to process raw post-event artifacts (Google Drive transcript .vtt, Zoom chat .txt, slide deck .pptx) into cleaned source-of-truth files that all downstream post-event skills (followup email, recap clips, blog recap, LinkedIn pulls) consume. NOT auto-triggered — Travis runs this explicitly after the live event, once raw files are saved into the event folder's `raw/` subfolder. Trigger phrases (only when explicitly invoked): "ingest the webinar", "process the raw files", "clean up the transcript", "run webinar ingest".
metadata:
  version: 0.1.0
---

# Webinar Ingest

Turn raw post-event artifacts into two cleaned source-of-truth files. Run this **once per webinar**, immediately after the live event, before any downstream content skill (`webinar-followup-email`, `webinar-recap-clips`, blog recap, LinkedIn pulls) is invoked.

This is the **Tier 2** step in the post-event content pipeline:

```
Tier 1 (raw)        Tier 2 (this skill)              Tier 3 (downstream skills)
raw/*.vtt   ──┐
raw/*.txt   ──┼──►  <slug>-transcript-clean.md  ──►  followup-email
raw/*.pptx  ──┘     <slug>-deck-extract.md      ──►  recap-clips
                                                ──►  key-quotes / frameworks / as-delivered
```

Every downstream skill reads from the **clean** files, never from `raw/`. That means name corrections, slide annotations, and chat folding happen **once**, not per-artifact.

## Prerequisites

- Event folder exists: `cerkl/marketing/channels/webinar/<speaker-slug>-<month>-<YYYY>/`
- Brief exists: `<speaker-slug>.md` (used to canonical-spell the partner's name and pull session metadata)
- `raw/` subfolder exists inside the event folder, containing one or more of:
  - **Transcript** (`*.vtt`) — Google Drive auto-caption preferred; Zoom often truncates. If both are present, prefer the longer/more-complete file. Flag broken/short transcripts with `-broken.vtt` or `-zoom-broken.vtt`.
  - **Chat log** (`*.txt`) — Zoom chat export with `HH:MM:SS\tName:\tMessage` rows.
  - **Slide deck** (`*.pptx`) — optional but high-value. Speaker notes and slide titles are reusable IP.
  - **Recording URL** — note in the clean transcript header if known; not required to run.

## Inputs to gather (only if missing)

Most of the time, this skill runs with no questions. Ask only when:
- The `raw/` folder has zero usable files → prompt user to confirm location.
- Multiple `*.vtt` files of similar length exist → ask which is canonical.
- Brief is missing or has placeholder names → ask for canonical Tarek-side and partner-side spellings before proceeding.

## What this skill produces

### 1. `<speaker-slug>-transcript-clean.md` — cleaned transcript

Single source of truth for the spoken content of the webinar. All downstream content skills consume this file.

**Structure:**
- Header block: webinar title, date, duration, speakers (canonical names), source-file references, cleanup conventions (5–7 bullets)
- ~10–13 numbered sections matching the webinar's narrative arc, each with a `[Slide N: <title>]` annotation
- Speaker labels on every turn: `**<Tarek/partner first name>:**`
- Timecodes every speaker switch and every ~1–2 minutes inside long monologues
- Chat folded inline as `> [Chat] Name (transcript ~MM:SS): ...` — chat timestamps converted to **transcript time** using the per-event chat offset (see Cleanup conventions below)
- "Cleanup notes — open questions for review" section at the bottom listing every `[unclear]`, every name correction made, every ambiguous slide reference, and any verbal-vs-deck data discrepancy

### 2. `<speaker-slug>-deck-extract.md` — cleaned deck content

Single source of truth for the visual/written content of the deck. Independent of the transcript — useful when downstream content needs to pull a manifesto bullet, an acronym, or a stat that's *on the slide* rather than what was *said*.

**Structure:**
- Header block: deck filename, slide count, image count, notes-slide count
- One section per slide:
  - `## Slide N — <title or one-line description>`
  - `**Text:**` — verbatim text content
  - `**Speaker notes:**` — verbatim notes (often contain written-down versions of analogies)
  - `**Images:**` — filenames only (pulled from slide rels), or "*(no images)*"
  - `**Transcript:**` — `~MM:SS–MM:SS` link to the matching section in `transcript-clean.md`
- "Skipped slides" callout — slides Matt/partner did not deliver live (very high-value to surface; often the most actionable content)
- "Appendix slides" callout — backup polls, registration-page content, etc., not used during the live event
- "Verbal-vs-deck deltas" section — every place the speaker said something different from what's on the slide (rounded numbers, swapped terminology, reordered bullets)

## Cleanup conventions (codified)

### Names
- Pull canonical Tarek-side spelling from `cerkl/CLAUDE.md` or any prior cleaned transcript: **Tarek Kamil** (often mis-captioned as "TK Camille / Terek / Tarik").
- Pull canonical partner-side spelling from the brief (`<speaker-slug>.md`).
- Pull canonical third-party names (mutual friends, sources cited mid-talk) from the brief or prior content if present. Common one for Cerkl webinars: **Steve Crescenzo** (often mis-captioned as "Presenzo").
- Correct partner email/URL via the brief or "By Attending You Will" appendix slide. For Matt Frost: `matt.frost@ic.partners` and `ic.partners`.

### Speaker labeling
- Always use first names in labels: `**Tarek:**`, `**Matt:**`. Not titles.
- When VTT captions overlap (both speakers tagged in adjacent blocks), assign captions to whoever held the floor for the longer turn. Move short interjections ("yeah, mhm, 100%") into the listening speaker's turn only if substantive.
- Strip pure-filler interjections that don't add meaning. Preserve any interjection that acknowledges or contradicts.

### Chat-time offset
- Zoom chat clock and recording clock are usually offset by 12–14 minutes (recording starts before broadcast). Compute the offset by aligning the first user-visible chat message (e.g., "Hello from <city>!") with the moment the live broadcast starts in the transcript.
- Apply the computed offset to every chat line. Quote chat reactions inline at their **transcript-equivalent timestamp**, not the chat clock.
- Filter Otter.ai / notetaker bot messages from inline quotes — preserve them in the bottom Cleanup notes if useful, otherwise drop.

### Slide annotation
- Every section gets a `[Slide N: <title-or-description>]` anchor, derived from the deck extract. If a section spans multiple slides, list them: `[Slides 6–7: From Compliance to Connection]`.
- For image-only slides where the title isn't in the .pptx text, infer a description from spoken cues *in the transcript* and mark with `⚠️` in the open-questions section.

### Verbal-vs-deck reconciliation
When the speaker rounds, paraphrases, or reorders content from the deck:
- **Use the deck's wording as canonical IP** in `deck-extract.md` (e.g., "VALUE: Visibility / Accessibility / Literacy / Usage / Experience").
- **Use the verbal version as delivered** in `transcript-clean.md` (e.g., "Understandable" if that's what the speaker actually said).
- Note the delta in `deck-extract.md`'s "Verbal-vs-deck deltas" section, *not* in `transcript-clean.md`.
- Stats: prefer the deck's source-cited number (e.g., $28,250 from BLS) for any external-facing content. Note the rounded verbal version (e.g., "close to $30,000") as a lower-precision delivery choice.

### Unclear captions
- Mark with `[unclear]` and provide best-guess in italics: `[unclear — likely "worry"]`.
- List every `[unclear]` in the bottom Cleanup notes section so the user can resolve in one pass against the recording.

## Reusable extractor

Run [`extract-pptx.py`](extract-pptx.py) on the deck file to dump slide text, speaker notes, and image manifests in one pass:

```bash
python3 cerkl/marketing/channels/webinar/skills/webinar-ingest/extract-pptx.py \
  "<event-folder>/raw/<deck-filename>.pptx"
```

The script outputs a structured markdown block ready to paste/adapt into `<speaker-slug>-deck-extract.md`.

## Output

Write both files to the **event folder** (not `raw/`):

```
<event-folder>/
├── raw/                              ← inputs (unchanged)
│   ├── *.vtt
│   ├── *.txt
│   └── *.pptx
├── <speaker-slug>-transcript-clean.md   ← Tier 2 output
└── <speaker-slug>-deck-extract.md       ← Tier 2 output
```

After writing both files, **list every open question for the user to review before downstream skills run.** Group by file:

- `transcript-clean.md`: every `[unclear]`, every inferred name correction, every ambiguous slide reference
- `deck-extract.md`: every image-only slide whose description was inferred, every verbal-vs-deck delta whose canonical version is debatable, every cited stat whose source is missing

Do not invoke any Tier 3 / downstream skill from inside this skill — wait for the user to confirm the cleaned files are good.

## Push update

After ingest, append an update block to the relevant project file in `personal-assistant/projects/` per the protocol in [../../CLAUDE.md](../../CLAUDE.md). Include in the update:
- Which raw files were processed
- Any open questions blocking downstream skills

## Worked example

The Matt Frost April 2026 webinar in [matt-frost-april-2026/](../../matt-frost-april-2026/) was the first ingest. Reference these files when uncertain about format:

- Inputs: [raw/](../../matt-frost-april-2026/raw/) — Google Drive .vtt, Zoom chat .txt, .pptx deck (43MB), broken Zoom .vtt for comparison
- Outputs: [matt-frost-transcript-clean.md](../../matt-frost-april-2026/matt-frost-transcript-clean.md), [matt-frost-deck-extract.md](../../matt-frost-april-2026/matt-frost-deck-extract.md)
