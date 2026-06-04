# Feature-extraction rubric (notes → feature requests)

The classifier step of the weekly sales report dispatches a sub-agent with THIS file as its brief. It reads the deterministic notes pull and emits a structured list of product/positioning gaps. Inference is bounded to this one step — it produces JSON, never HTML.

## Inputs
- **Notes:** `tmp/notes-<label>.json` (from `pull_notes.py`) — each note has `body`, `owner`, `date`, `assoc_type`, `deal_names`, `company_names`, `deal_feature_gaps`.
- **Product truth (for `already_ships`):** `/Users/travisfoster/claude-code/cerkl/shared/broadcast.md` (+ `/Users/travisfoster/claude-code/cerkl/shared/features/` if present).

## Output
Write `tmp/feature-requests-<label>.json`:
```json
{
  "label": "<label>",
  "feature_requests": [
    {
      "quote": "<verbatim snippet from the note body>",
      "source": "<deal name if assoc_type=deal, else company name>",
      "source_type": "deal" | "company",
      "owner": "<owner>",
      "date": "<date>",
      "mapped_gap": "<taxonomy label> | novel: <short>",
      "already_ships": true | false | "unsure",
      "competitor": "<name or null>"
      // already_ships=true → a capability we HAVE that the prospect cares about
      //   (the AE is recording a priority, naming it because they know we have it).
      //   Recorded, but NOT a gap — excluded from the report's Feature-gaps section.
      // already_ships=false/"unsure" → a real gap (capability we lack) — the gap signal.
    }
  ],
  "summary": "<2-3 sentences: signals found vs notes scanned, themes, ambiguous calls>"
}
```

## What COUNTS as a feature signal (extract)
- A prospect/customer expressing a **need, want, or missing capability** ("needs X", "wants X", "wish it had X", "X is a dealbreaker", "as long as it can X").
- **Competitor dissatisfaction that implies a needed feature** ("they hate Politemail but want a plugin").
- **Integration / system requirements** ("needs HRIS/SAP connection", "Teams is their main tool").

## What to IGNORE (not a feature signal)
- **Positive feedback / praise** — e.g. "Loved retargeting", "the analytics are great". Praise is NOT a request. (Tightened 2026-05-29 — the first spike mis-tagged "Loved retargeting" as a gap.) Only extract if paired with an unmet need.
- Prospecting research: LinkedIn URLs, person names, "garbage site", "junk?", "site cannot be reached".
- Call/meeting logistics, internal reminders, generic next-steps, head-count/pricing-only notes (unless they state a capability need).

## Real gap vs. sought-after capability we ship (the `already_ships` call)
Check the asked-for capability against `broadcast.md`:
- **Cerkl does NOT ship it → `already_ships: false`** = a real *product gap* (roadmap signal). This is what the report's Feature-gaps section shows.
- **Cerkl already ships it → `already_ships: true`** = NOT a gap. The AE is recording a capability the prospect cares about that we *have* (they name it explicitly because they know we have it). **Still extract and record it** — it's valuable demand/marketing signal — but the report excludes it from the Feature-gaps section and reserves it for the planned "most-requested capabilities we ship" view (see the process Future work).
- Genuinely unclear → `already_ships: "unsure"` (treated as a possible gap).
Be deliberate about this call — it decides gap vs. sought-after.

## Mapping rules
- One row per **distinct** ask (a note listing several asks → several rows).
- Map each to the closest `feature_gaps` taxonomy label below; if nothing fits, `"novel: <short label>"`.
- Quotes must be **verbatim** from the note body — never invent.

## feature_gaps taxonomy (current — refresh from the `feature_gaps` deal property if it changes)
Journeys · Channel Content Translation · Workflows · Landing Pages · Integration with Analytics Platforms · Native Social Media Sharing · A/B Testing · Event Registration · AI Content Generation · Email Heatmaps · Native Forms · Digital Signage · SMS · Calendar View · Arrive in Recipients Time Zone · Dynamic Content Block in Blasts · Language Translation (Blasts) · Tasks · Template editing permissions · Anchor links within emails · Squads / Group permissions · Analytics in Slack · Calendar Invites · Leave Comments on Drafts · Canva integration · Translate Content Blocks Within Blast · Other · None

> The structured `feature_gaps` checkbox values are rolled up separately by `pull_pipeline.py` (the `feature_gaps_rollup`). This classifier covers the *unstructured note* signal that the property misses (the property is set on only ~10% of deals).
