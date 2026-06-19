# Skill: Process Meetings (Batch)

Triggered when Travis wants to process MANY meeting notes at once — "process all new meetings", "batch the drive-sync corpus", "backfill meeting insights into projects". For a single file, use `process-meeting.md` instead.

Goal: turn the unprocessed meeting corpus into project `## Log` entries + INDEX changes **without loading raw docs into the main context**. This is `process-meeting` scaled across a corpus, with a synthesis/prioritization layer and sub-agent fan-out for context protection. Never apply without showing the proposed diff (and resolving flags) first.

## Why sub-agents
Reading dozens of full docs in the main thread causes context rot and buries signal. Extraction runs in throwaway sub-agent contexts that return only structured rows; the main thread holds conclusions, never transcripts.

## Procedure

1. **Scope.** List source docs under `meetings/drive-sync/` with NO `## Processed` stamp (the idempotency key). Default = everything unprocessed; the first run is a backfill. Confirm the file list + count before fanning out.

2. **Build the context pack** (once, shared by every extractor):
   - Active project filenames + one-line descriptions (from `projects/`).
   - INDEX Top of Mind + Calendar Anchors.
   - Today's date (for relative → absolute conversion).
   - The importance rubric (below).

3. **Extract — fan-out sub-agents.** Group docs by series (recurring weeklies together; bundle singletons); one agent per group. Each reads its docs FULLY + the context pack and returns **structured rows only — no prose, no file dumps**:
   ```
   DOC: <relative path>
   ACTION  | owner | what | due:<YYYY-MM-DD|none|ASK> | route:<file.md|new|one-off> | imp:<H|M|L>
   DECISION| what | route:<file.md> | imp:<H|M|L>
   BLOCKER | waiting_on:<who/what> | what | route:<file.md> | imp:<H|M|L>
   INSIGHT | what | route:<file.md|none> | imp:<H|M|L>
   NEWPROJ | proposed-name | why | imp:<H|M|L>
   ```
   Agent rules: dedupe within the batch; recurring series → only net-new / status-changed items; **for backfills of old docs, surface only still-open items + durable insights — treat anything completed or superseded as skip-or-one-line-note**; never write files.

   Importance: **H** = Top-of-Mind project, or deadline ≤3 weeks, or owner=Travis near-due, or revenue/risk. **M** = clear owner/action, no imminent deadline. **L** = FYI / no clear owner.

4. **Synthesize (main thread).** Merge all rows; dedupe within and across docs; cross-check each candidate against the target project's existing `## Log` tail (don't re-log). Rank by importance. Collect **flags** — conflicts, date mismatches, items needing Travis's routing call.

5. **Confirm.** Present ONE grouped proposed diff (by destination: project `## Log` appends · INDEX changes · new projects · one-offs · a "not logged" digest). Lead with the flags. Get decisions + a single greenlight. Run `new-project.md` create-vs-fold for each NEWPROJ; route externally-owned items per Travis (drop or anchor-only).

6. **Apply.** Write entries into each file's `## Log` (match the format spec in `new-project.md`); update INDEX anchors / Top of Mind; create or fold projects. Group writes by target file and fan out writer sub-agents for distinct files (parallel-safe — never two agents on one file).

7. **Stamp.** Append to each source doc so this run and `refresh` skip it next time:
   ```
   ## Processed — YYYY-MM-DD
   - <count + projects touched, or "meeting-ingest batch">
   ```

8. **Refresh the ledger.** Run `growth-project-tracker.md` so the portfolio view reflects the new state.

## Don't
- Don't load raw docs into the main thread — that's what the extractors are for.
- Don't apply without the diff + flag resolution (per `process-meeting.md`).
- Don't write speculative tasks or invent owners — no clear owner → flag, don't guess.
- Don't re-log what's already in a project's `## Log` tail.
- Don't run two writer agents on the same file.
- Don't load `marketing/`, `sales/`, `hubspot/`, `strategy/`, or `shared/` context.

## Relationship
- Single file → `process-meeting.md`. Quick one-item capture → `capture.md`. New-project decision → `new-project.md`. Source docs come from `meeting-ingest/` (token-free Drive→markdown sync). Ledger view → `growth-project-tracker.md`.
