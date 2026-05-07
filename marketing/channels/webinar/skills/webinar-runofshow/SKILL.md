---
name: webinar-runofshow
description: When the user wants a rehearsal checklist or day-of run-of-show / timing script for a webinar. Trigger phrases include "run of show", "runofshow", "rehearsal checklist", "rehearsal prep", "day-of script", "webinar timing", "live event prep", "webinar checklist". Run this AFTER the brief outline is settled, ideally a few days before the rehearsal.
metadata:
  version: 0.1.0
---

# Webinar Run-of-Show

Produce two things: a **rehearsal checklist** to run a few days before the event, and a **day-of run-of-show / timing script** to follow live.

## Prerequisites

- Brief outline (the 60-minute structure section) is filled out
- Polling questions are settled
- Speakers know their segments

## Rehearsal checklist

A checklist the team runs 3 days before the event (or the Friday prior if the event is Monday — see project plan):

- Tech check — Zoom audio, video, screen share, recording on, polls loaded
- Walk through each outline segment with timing — flag any segment running over
- Confirm slidedeck is finalized and shared
- Confirm transitions between speakers (who hands off to whom, on what cue)
- Confirm Q&A handling — moderated by whom, where questions are routed
- Confirm giveaway mechanics — how winner is selected and notified post-event
- Confirm CTA at close — exact words, link visible
- Backup plan — what to do if internet drops, screen share fails, audio is bad

## Day-of run-of-show

A minute-by-minute script for the live event. Pull timing from the brief outline. For each segment include:

- **Start time** (e.g., "10:00 — Intro")
- **Duration**
- **Who's speaking** (lead, support)
- **Key points to hit** (3–5 bullets, condensed from the brief)
- **Transitions in/out** ("Tarek hands to Matt with: 'Matt, you've seen this exact thing happen — talk us through it.'")
- **Polls or interactive moments** — when to launch, when to display results

Include a **pre-show checklist** for the 15 minutes before going live:
- Both presenters in the room, mics tested
- Recording started
- First slide up
- Polls queued
- Backup notes within reach

Include a **post-show checklist** for the 5 minutes after:
- Confirm recording saved
- Note attendance number
- Note any questions that didn't get answered (for follow-up email)
- Quick debrief — what went well, what to flag for next time

## Cerkl context to apply

- **Tarek's role** is typically the Cerkl host — opens, frames, closes with CTA. Partner leads on subject-matter content.
- **Always record** — recording is needed for follow-up email + recap clips.
- **Foundations sign-up CTA** at close is non-negotiable. Write the exact line.

## Output

Write to `<speaker-slug>-runofshow.md` in the event folder. Two main sections: `## Rehearsal Checklist` and `## Day-of Run-of-Show`.

## Push update

After producing the run-of-show, append an update block to the relevant file in `personal-assistant/projects/`. See [../../CLAUDE.md](../../CLAUDE.md) for the protocol.
