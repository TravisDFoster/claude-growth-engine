# Identity

This folder holds **one subfolder per named prospect** — `prospects/<prospect>/`. Everything we produce *for a specific account* lives here: brand kits, sales decks, day-in-the-life scripts, account one-pagers, roadmaps, exported PDFs. Process folders (`presentations/`, `competitor-dissatisfaction/`, `pressure-prospecting/`, …) stay clean — they hold the *how*; this folder holds the *who*.

The processes that generate prospect work write their output into the matching `prospects/<prospect>/` folder and reference it by relative path. A prospect accumulates artifacts from several processes over time; keeping them together (not scattered inside each process folder) is the point.

## Convention

```
prospects/
├── CLAUDE.md                          ← you are here (the only tracked file)
└── <prospect>/                        ← e.g. kyndryl/ — all local-only
    ├── <prospect>-brand-guidelines/   ← from ../prospect-brand-process.md (colors, type, logo)
    ├── <Deck_Name>_<variant>.pptx     ← from ../presentations/presentation-process.md
    ├── <prospect>-<project>-ROADMAP.md ← living project memory
    └── … one-pagers, scripts, exports
```

- Prospect folder name is lowercase-kebab of the account (`kyndryl`, `acme-health`).
- One brand kit per prospect — `<prospect>/<prospect>-brand-guidelines/`. Stand it up once (via [`../prospect-brand-process.md`](../prospect-brand-process.md)); every downstream deliverable for that account references it, never duplicates it.

## Rules
- Everything under `prospects/<prospect>/` is **local-only** (gitignored — PII / competitive). Only this router is tracked.
- Process docs and skills never live here — they live in their process folder; this folder is account deliverables only.
