# LinkedIn Asset Pack

> Curated set of brand templates the LinkedIn asset process renders into. Sibling to [`webinar/asset-packs.md`](../webinar/asset-packs.md) but scoped to LinkedIn-native shapes (stat cards, quote cards, carousels, link/blog promos, text-only).
>
> **This file is the authoritative gate.** [`linkedin-asset-process.md`](linkedin-asset-process.md) rejects any manifest whose `template_id` isn't in the table below. Expand by appending rows.

## The pack — 12 templates (2026-06-02)

| Template ID | Use case | Aspect | Pages | Photo-slot? | Notes |
|---|---|---|---|---|---|
| `EAHK4xxpksA` | social-quotes-testimonials | 1:1 | 4 | No | Page 1 = quote layout |
| `EAHJ5Aa1cUw` | downloadable-asset-promo-square | 1:1 | 5 | Yes (cover) | Asset cover needs explicit `asset_id` |
| `EAHJPZD93P8` | social-square-cta-product | 1:1 | 4 | Yes (product) | Product image needs explicit `asset_id` |
| `EAHHKqwQjWM` | linkedin-carousel-3-part-list | 4:5 | 7 | Yes (per-page) | Multi-page; per-page photos optional |
| `EAHI2RC4_s8` | foundations-product-images | 1:1 | 4 | Yes (product) | Product screenshots needed |
| `EAHJUVpBsz4` | blog-post-promo | 1:1 | 2 | No | Blog promo card |
| `EAHIAt1o9d4` | linkedin-carousel-problem-solution-1 | 1:1 | 8 | No (text-led) | Text-led carousel |
| `EAHG3Ty0I9Y` | social-portrait-photo-text | 4:5 | 4 | Yes | Page 1 photo+text — `asset_id` required |
| `EAHG3Tpp4CI` | linkedin-stat-card | 1:1 | 4 | Yes (decorative) | XX% + statement variant; photo-slot is CTA capsule (default kept) |
| `EAHHb4dbs1Y` | linkedin-carousel-5-part-list | 4:5 | 9 | No (text-led) | Text-led carousel |
| `EAHHbiYvZCE` | social-landscape-text-only | 5:4 | 4 | No | Text-only |
| `EAHIEGj_L3s` | linkedin-carousel-problem-solution-2 | 1:1 | 7 | Yes (per-page) | Per-page photos optional |

All 12 are **enriched** in [`template-fill/_element-maps/`](../../design/canva-skills/template-fill/_element-maps/) (verified 2026-06-02 — runtime fields populated, ready for `template-fill`).

**Out of scope for v1:**
- `EAGqLAh0VTQ` (FB/LinkedIn share-card style 1) — element-map is empty, needs markdown re-crawl.
- All webinar-pack templates (`EAGqLMN8_Po`, etc.) — owned by [`webinar/asset-packs.md`](../webinar/asset-packs.md); the LinkedIn process **reads** webinar manifests for webinar-wrap posts but doesn't render through them.

---

## Post type → template selector

The asset process scaffolder infers subtype from the draft's `## Asset` section and maps to a template via this table.

| Post type | Subtype signal in `## Asset` | Template ID | Page | Photo-slot fill |
|---|---|---|---|---|
| `static-theme` | "Stat:" + single numeric line | `EAHG3Tpp4CI` | 1 | Default (decorative) |
| `static-theme` | quoted "..." in Visual concept | `EAHK4xxpksA` | 1 | n/a |
| `static-theme` | "Photo + text" / explicit `Asset ID:` | `EAHG3Ty0I9Y` | 1 | **`Asset ID:` required** |
| `static-theme` | text-only narrative, no stat or quote | `EAHHbiYvZCE` | 1 | n/a |
| `static-blog` | (always) | — | — | **Skip** — LinkedIn auto-renders the link card from blog OG image |
| `carousel` | "problem/solution" framing | `EAHIAt1o9d4` or `EAHIEGj_L3s` | 1 + per-page | Optional per-page |
| `carousel` | N-part list (3 items) | `EAHHKqwQjWM` | 1 + per-page | Optional per-page |
| `carousel` | N-part list (5 items) | `EAHHb4dbs1Y` | 1 + per-page | Optional per-page |
| `carousel` | downloadable-resource promo | `EAHJ5Aa1cUw` | 1 | **`Asset ID:` required** |
| `carousel` | product showcase | `EAHJPZD93P8` or `EAHI2RC4_s8` | 1 | **`Asset ID:` required** |
| `carousel` | blog post promo | `EAHJUVpBsz4` | 1 | n/a |
| `poll` | (always) | — | — | **Skip** — native LinkedIn poll widget |
| `short-video` | (always) | — | — | **Skip** — video pipeline, not Canva |

If the subtype doesn't match cleanly, the scaffolder surfaces a `template_unclear` warning with the draft slug and asks Travis to pick before scaffolding. Don't guess.

**Decision boundary — stat-comparison case:** the 2-stat comparison shape (e.g., "60% reported / 12% actual") does **not** fit `EAHG3Tpp4CI` page 1 cleanly. Until a stat-comparison template lands, route those to `carousel` and split across two cover pages, or surface `template_unclear` and let Travis decide.

---

## Webinar-wrap path (cross-channel)

When a LinkedIn draft's `Wraps:` field points at a webinar event folder, the LinkedIn asset process **does not render**. It reads the matching role's `result.edit_url` from the webinar's `canva-manifests/` and mirrors that URL into the Jira CSV `Asset:` line.

LinkedIn-shaped roles available in the webinar pack ([`webinar/asset-packs.md`](../webinar/asset-packs.md)):

| Role | When the LinkedIn process reuses it |
|---|---|
| `speaker-card` (1:1) | LinkedIn intro post for the webinar |
| `share-1200x628` (1.91:1) | LinkedIn feed share / link-card fallback |
| `share-16x9` (16:9) | Twitter/X cross-post |
| `countdown` (1:1) | 2-days-to-go boost |

If the matching webinar manifest's `result:` block is missing (webinar hasn't been rendered yet), surface a `webinar_pack_unrendered` warning and skip — don't fall back to LinkedIn-channel rendering for webinar-wrap posts.

---

## Manifest generation rule

For each eligible LinkedIn draft, the asset process writes `linkedin/canva-manifests/<draft-slug>.yml`:

```yaml
template_id: <from pack table>
page_index: 1
design_title: <draft-slug>-<YYYY-MM-DD>
text_values:
  # Keys match the placeholder text in the chosen template's _element-maps JSON.
  # Substring fallback exists with warnings (per template-fill SKILL.md).
  "60%": "<stat from draft>"
  "of employees say they miss important updates": "<statement from draft>"
image_assets: {}        # default — keeps template defaults
commit_mode: auto       # overridden to checkpoint for single-post override path
```

For templates with a content-bearing photo-slot, the manifest must include:

```yaml
image_assets:
  photo-slot: ["<asset_id from canva-asset-index.md>"]
```

If absent, the scaffolder warns `photo_slot_unspecified` and renders with the template default — Furqan replaces in Canva.

---

## V1 image-role behavior

| Role | Behavior | Why |
|---|---|---|
| `full-bg` | Keep template default | Brand backgrounds — never swap at render time |
| `logo` | Keep template default | Branding lockup |
| `icon` | Keep template default | Branded icons |
| `decorative` / `decorative-badge` | Keep template default | UI elements |
| `photo-slot` | **Caller declares explicitly via `Asset ID:` in draft** (or default) | Content image — see selector table; missing = warning + default |

This is the minimal v1 path. No auto-resolution of best-fit assets. V2 builds the fit index.

---

## Length-fit pre-check (v1 honesty rule)

Before scaffolding a manifest, the process checks each text replacement's character count against the slot's design baseline (the placeholder's original character count). If a replacement is **>1.3×** the baseline AND the slot is **bounded** (text element with a foreground element below — typical for the stat-card statement slot), surface a `length_fit_risk` warning and ask Travis whether to (a) shorten the draft, (b) pick a different template, or (c) proceed and accept potential overlap.

Added 2026-06-02 after the W24 stat-card render produced a "send." overlap with the CTA capsule.

---

## Future work (v2)

- **Asset-fit index** at `linkedin/asset-fit-index.json` — joins `canva-asset-index.md` (aspect, category) with each template's photo-slot dimensions to rank candidate `asset_id`s per `(template_id, page, role)`.
- **Asset intent metadata** — extend `canva-asset-index.md` with `intent` and `subject` columns; populate `canonical-assets.json` via a curation pass.
- **Expand the pack** — add LinkedIn-native templates as they're created in Canva. Each new template must have an enriched `_element-maps/<id>.json` before going in the table.
- **`stat-comparison` subtype** — the 2-stat case (`frontline-reach-problem`) needs either a custom template or a multi-page carousel pattern. Defer until the pattern recurs.
- **Catalog re-crawl** — `EAGqLAh0VTQ` (FB/LinkedIn share-card style 1) needs its markdown re-crawled before it's addable.
