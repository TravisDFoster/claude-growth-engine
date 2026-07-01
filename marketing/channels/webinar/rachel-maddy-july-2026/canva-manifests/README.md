# Rachel Folz + Maddy Rieman — Canva Manifests (July 2026 webinar)

> 9 manifests from the **IC Thought Leadership** pack ([`../../asset-packs.md`](../../asset-packs.md)), each a render-ready input for [`template-fill`](/Users/travisfoster/claude-code/cerkl/marketing/design/canva-skills/template-fill/SKILL.md).
>
> **Updated 2026-06-10:** event moved to **2026-07-09**, retitled, and a **second speaker (Maddy Rieman, Head of Customer Success)** added. Every page-1 template carries the 2-speaker layout, so both speakers are now filled (the prior solo render left a placeholder speaker-2 on those templates). `countdown` has no speaker slots; `recording-thumbnail` / `recap-blog-cover` have no page-1 date element.

## Manifests in this folder

| Role | File | Template ID | Aspect | Promo step / channel |
|---|---|---|---|---|
| `speaker-card` | [speaker-card.yml](speaker-card.yml) | `EAGqLMN8_Po` | 1:1 | LinkedIn intro post; sales / CS enablement |
| `countdown` | [countdown.yml](countdown.yml) | `EAGqLGh6dGQ` | 1:1 | LinkedIn 2-days-to-go boost |
| `share-1200x628` | [share-1200x628.yml](share-1200x628.yml) | `EAGqLHFNucs` | 1.91:1 | LinkedIn feed share; OG image; Inner Cerkl News; Intercom in-app |
| `share-16x9` | [share-16x9.yml](share-16x9.yml) | `EAGqLLgAXU0` | 16:9 | Twitter/X share; link previews |
| `email-banner` | [email-banner.yml](email-banner.yml) | `EAGqLERK1oE` | 3:1 | Email Blasts #1, #2, #3; Cerklular newsletter |
| `zoom-banner` | [zoom-banner.yml](zoom-banner.yml) | `EAGqLIWzZTY` | 3.2:1 | Zoom waiting-room banner (day-of) |
| `blog-cover` | [blog-cover.yml](blog-cover.yml) | `EAGqLL_MWfw` | 3:2 | Pre-event blog (Cerkl SEO + ICPro) |
| `recap-blog-cover` | [recap-blog-cover.yml](recap-blog-cover.yml) | `EAGqLEylplk` | 3:2 | Post-event recap blog |
| `recording-thumbnail` | [recording-thumbnail.yml](recording-thumbnail.yml) | `EAGqLKbOQ-E` | 16:9 | On-demand recording / YouTube |

## What's pre-filled

- Webinar title: `Stop Guessing About Your Analytics: 5 Questions Every Internal Communicator Should Answer`
- Speaker 1: `Rachel Folz` — `Head of Product, Cerkl` — headshot `MAFZdaEt2Wc`
- Speaker 2: `Maddy Rieman` — `Head of Customer Success, Cerkl` — headshot `MAFZdS-3JCo`
- Date placeholder: `|   Jul 9, 2026 12:00 PM EDT` (no pipe on `countdown`; dropped on `recording-thumbnail` / `recap-blog-cover`)

> **Render note:** the new title is long (~78 chars). Verify it doesn't overflow on the tighter banners (`email-banner` 3:1, `zoom-banner` 3.2:1, `share-16x9`) when reviewing renders.

## To render

Once Rachel's headshot is uploaded to Canva and the asset ID is captured:

1. Replace `headshot: ["TBD …"]` in each manifest with the actual asset ID.
2. Invoke `template-fill` per manifest (one invocation per role).
3. Paste each returned Canva edit URL into:
   - The matching row of the Drive MAP (Phase 3 / 4 / 5 promo row)
   - The matching row of [`../rachel-maddy-project-plan.md`](../rachel-maddy-project-plan.md)

If `template-fill` returns warnings about unmatched placeholders (likely on the date/time field — template placeholders vary), refine that manifest's `text_values` to match the actual element-map for that template (`canva-skills/template-fill/_element-maps/<template_id>.json`) and re-invoke.
