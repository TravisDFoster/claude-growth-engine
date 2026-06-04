# How-To: Make a Canva Brand Template Autofill-Ready

> **Why this exists.** The 2026-05-29 spike found that **zero** of Cerkl's current brand templates support API autofill (`get-brand-template-dataset` returned `{}` for the IC Fact post, and `search-brand-templates dataset=non_empty` returned an empty list). A template only becomes autofillable once someone adds **data fields** to it inside Canva. This is the one-time manual step that unlocks full Canva automation. Do it once per template; the automation then fills and exports it forever.

## Prerequisite (verify first — possible blocker)

Autofill via the Connect API **requires the Canva account to be part of a Canva Enterprise organization.** Our read-only tools worked, but autofill specifically is gated to Enterprise. **Confirm Cerkl's Canva plan is Enterprise before investing in field setup.** If it isn't, autofill is off the table and we fall back to create-design + manual finish (or the HTML→PNG pipeline for stat cards).

## Part A — Add data fields in the Canva editor (one-time per template)

1. Open the brand template in Canva (Brand Templates → the template → **Edit**).
2. Open **Apps** in the left sidebar and search for **"Data autofill"** (a.k.a. the Bulk Create / Data autofill app). Open it.
3. Click an element on the canvas you want the automation to fill, then in the Data autofill panel choose **Add as data field** (the `+` / "Add" action).
4. **Name the field** with our convention below. The name you type here becomes the exact key the API returns and expects — it's the contract between this manual step and the automation, so be precise and consistent.
5. Repeat for every element that should be dynamic. Three element types can become fields:
   - **Text** → text fields (headline, stat, body, CTA, date).
   - **Image / frame** → image fields (headshot, background photo, logo). The frame must be a real image placeholder/frame.
   - **Chart** → chart/data fields (rarely needed for us).
6. **Publish / save the brand template** so the dataset is registered.

### Field naming convention (use this exactly)

Lowercase `snake_case`, semantic, no spaces. Keep names stable across templates so one manifest format works everywhere:

| Element | Field name |
|---|---|
| Main headline / title | `headline` |
| Secondary / subhead | `subhead` |
| Big number or stat | `stat_value` |
| Stat label / caption | `stat_label` |
| Body paragraph | `body` |
| Call-to-action text | `cta_text` |
| Date / time | `event_datetime` |
| Person photo | `headshot` |
| Background photo | `background_image` |
| Logo (if swappable) | `logo` |

For the webinar speaker card add the webinar-specific set: `webinar_title`, `event_datetime`, `speaker_name`, `speaker_headshot`.

## Part B — Verify the template is now autofill-ready

After publishing, re-run the dataset check. It should now return the fields instead of `{}`:
- `get-brand-template-dataset` (MCP) on that template ID → expect a JSON object whose keys are the field names you set, each with a `type` of `text` or `image`.
- The template should now also appear in `search-brand-templates` with `dataset="non_empty"`.

If it still returns `{}`, the fields weren't saved/published, or the account isn't Enterprise.

## Part C — How the automation fills it (the API flow, for reference)

Confirmed against Canva's Autofill guide. The eventual skill runs:

1. **Get dataset** — read the field names + types for the template ID.
2. **Build the `data` object** — one entry per field:
   - text → `{"type": "text", "text": "<value>"}`
   - image → `{"type": "image", "asset_id": "<canva-asset-id>"}`
3. **Create autofill job** — `POST /autofills` (MCP equivalent) with `brand_template_id` + `data`. Asynchronous — returns a job ID.
4. **Poll the job** until `status: success`; the result carries the new design.
5. **Export** the design to PNG/JPG/PDF at target dimensions; save the link/file back.

**Image assets — no re-upload (matches our "don't duplicate in Canva" rule).** Image fields take a Canva `asset_id`. Our existing images already live in Canva with stable IDs (see `canva-asset-index.md`, e.g. a headshot like `Rachel-folz.jpg` → `MAFZdaEt2Wc`). The automation passes those IDs directly — no upload step, no duplicates. ⚠️ The one thing to confirm in the build spike: that an **existing folder-image ID is accepted as an autofill `asset_id`** (Canva's guide documents the upload-then-use path; we're betting the already-stored asset ID works the same — verify before relying on it).

## Recommended pilot

Convert **one** template first and prove the whole loop end to end. Best candidate: the webinar **`Square Social_speakers_Thought Leadership`** (1080×1080) — obvious fixed fields (`webinar_title`, `event_datetime`, `speaker_name`, `speaker_headshot`), and webinars are the first consumer. Dry-run target: Rachel Folz solo webinar, 2026-06-25 (headshot already in Canva).

---

*Sources: [Canva Autofill guide](https://www.canva.dev/docs/connect/autofill-guide/), [Connect API — Autofill reference](https://www.canva.dev/docs/connect/api-reference/autofills/), [Canva Help — Data autofill](https://www.canva.com/help/data-autofill/).*
