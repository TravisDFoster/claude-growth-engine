# Webinar Asset Packs

> Curated multi-template asset packs that `webinar-project-init` renders together for one webinar campaign. LinkedIn / other channels define their own picks inline — there is no shared `use_case → template` map at the skill layer.
>
> Each pack is a set of Canva brand-template IDs mapped to a **role** (the surface or use-case). Init iterates the chosen pack and creates one [`template-fill`](/Users/travisfoster/claude-code/cerkl/marketing/design/canva-skills/template-fill/SKILL.md) manifest per role in `<event-folder>/canva-manifests/`, pre-filling what's known (title, date, time, speaker) and leaving image-asset slots (headshot) marked TBD.

## Pack selection

| Pack | When to use |
|---|---|
| **IC Thought Leadership** (default) | All Cerkl webinars in the Thought Leadership series — the brand-styled visual lineage. |
| **Generic** | Non-series webinars where the IC Thought Leadership brand styling doesn't fit. |

`webinar-project-init` defaults to the IC Thought Leadership pack. Switch to Generic only if the orchestrator confirms non-series styling at scaffold time.

---

## IC Thought Leadership webinar pack (9 templates)

Template names all contain `_Thought Leadership_Webinar Series` in Canva — the screenshot identifier.

| Role | Template ID | Aspect | Promo step / channel(s) | Notes |
|---|---|---|---|---|
| `speaker-card` | `EAGqLMN8_Po` | 1:1 1080×1080 | LinkedIn intro post; sales / customer-success enablement | Layered placeholder frames — `manual_drag_required` for headshots |
| `countdown` | `EAGqLGh6dGQ` | 1:1 1080×1080 | LinkedIn 2-days-to-go boost | Single-page X-days-to-go |
| `share-1200x628` | `EAGqLHFNucs` | 1.91:1 | LinkedIn feed share; OG image for reg page; Inner Cerkl News; Intercom in-app | |
| `share-16x9` | `EAGqLLgAXU0` | 16:9 | Twitter/X share; embedded link previews | |
| `email-banner` | `EAGqLERK1oE` | 3:1 | Email Blasts #1, #2, #3; Cerklular newsletter | |
| `zoom-banner` | `EAGqLIWzZTY` | 3.2:1 | Zoom waiting-room banner (day-of) | |
| `blog-cover` | `EAGqLL_MWfw` | 3:2 | Pre-event blog post (Cerkl SEO blog + ICPro blog) | |
| `recap-blog-cover` | `EAGqLEylplk` | 3:2 | Post-event recap blog (SEO archive) | |
| `recording-thumbnail` | `EAGqLKbOQ-E` | 16:9 | On-demand recording page / YouTube thumbnail | |

## Generic webinar templates (5)

Available for non-IC-Thought-Leadership webinars (when the brand styling isn't series-specific).

| Role | Template ID | Aspect | Promo step / channel(s) | Notes |
|---|---|---|---|---|
| `square-webinar` | `EAGqLOHvqK8` | 1:1 | Generic LinkedIn intro post | No editable headshot fills — full-bg only |
| `fb-linkedin-share` | `EAGqLE12g5c` | 1.91:1 | Generic LinkedIn feed share; Facebook share | |
| `16x9-share` | `EAGqLJan-Ck` | 16:9 | Generic Twitter/X share; embedded link previews | |
| `blog-cover` | `EAGqLJvHcxg` | 3:2 | Generic pre-event blog post | |
| `video-thumbnail` | `EAGqLDCHyRM` | 16:9 | Generic recording thumbnail | |

---

## Manifest generation rule (used by `webinar-project-init` Step 5)

For each role in the chosen pack, init writes `<event-folder>/canva-manifests/<role>.yml`:

```yaml
template_id: <from pack table>
page_index: 1                          # override if pack notes otherwise
design_title: <speaker-slug>-<role>-<YYYY-MM-DD>
text_values:
  # Common keys — exact placeholders per template live in template-fill/_element-maps/<template_id>.json.
  # template-fill falls back to substring match if no exact hit, and reports warnings for misses.
  "Webinar title": "<working title>"
  "Name": ["<speaker name>"]
  "Title": ["<speaker role>"]
  "|   Mar 6, 2025 1:00 pm est": "|   <event date>, <YYYY> <h:mm AM/PM ZONE>"
image_assets:
  headshot: ["TBD — gather from speaker; resolve via canva-asset-index"]
commit_mode: checkpoint
```

After scaffold, the orchestrator (Claude or Travis) refines per template based on `template-fill` warnings when actually rendering — the manifests are starting skeletons, not guaranteed-clean inputs.

**Render trigger:** invoke `template-fill` per manifest once the speaker has provided the headshot. The returned Canva edit URL is the deliverable — paste it into the corresponding row of the Drive MAP and the markdown project-plan.

---

## Per-role manifest overrides (applied by `webinar-project-init` Step 5b)

After the common manifest skeleton is written, init applies these role-specific overrides — adding, replacing, or dropping `text_values` / `image_assets` entries so the manifest matches what each template actually has. Captures lessons from real renders.

### `countdown` (EAGqLGh6dGQ)

The countdown is **always** the LinkedIn 2-days-to-go boost. X is constant.

- **set** `text_values["X"]: "2"` — the countdown numeral
- **set** `text_values["Mar 6, 2025 1:00 pm est"]: "<event_date_formatted>"` — note: no leading pipe (`|`) on this template's date placeholder, unlike speaker-card/email-banner
- **drop** `text_values["|   Mar 6, 2025 1:00 pm est"]` — the piped version doesn't exist here
- **drop** `text_values["Name"]` — countdown has no speaker text slots
- **drop** `text_values["Title"]` — countdown has no speaker text slots
- **drop** `image_assets.headshot` — countdown has no headshot slot (`full-bg`, `icon`, `logo`, `decorative-badge` only)

### `recap-blog-cover` (EAGqLEylplk)

- **drop** `text_values["|   Mar 6, 2025 1:00 pm est"]` — no date element on page 1; date is implied by the "Webinar Recap" kicker

### `recording-thumbnail` (EAGqLKbOQ-E)

- **drop** `text_values["|   Mar 6, 2025 1:00 pm est"]` — no date element on page 1
- (Title slot is handled via the orchestrator's smart text-matching against live `richtexts[]`, not by a manifest key)

### `share-1200x628` (EAGqLHFNucs) and `share-16x9` (EAGqLLgAXU0)

No `text_values` overrides needed. The orchestrator's smart-headshot rule handles their DELETE-placeholder / SHAPE-only thumb slots — see [`webinar-canva-render`](skills/webinar-canva-render/SKILL.md) Step 4 brief.

### Other roles

No overrides — the common skeleton works as-is.

---

## Promo step → asset role lookup

Used during promotion to know which asset role feeds which channel/step. Pair with the tracking-URL slug from [`templates/tracking-urls-template.md`](templates/tracking-urls-template.md).

| Promo step | Tracking slug | Asset role(s) |
|---|---|---|
| LinkedIn intro post | `cerkl_linkedin` | `speaker-card` OR `share-1200x628` |
| LinkedIn 2-days-to-go boost | `cerkl_linkedin` | `countdown` |
| Email Blast #1 / #2 / #3 | `cerkl_email` | `email-banner` |
| Pre-event Cerkl SEO blog | `cerkl_linkedin` (distribution) | `blog-cover` |
| ICPro blog promo | `cerkl_icpro` | `blog-cover` |
| Cerklular newsletter | `cerkl_cerklular` | `email-banner` |
| Inner Cerkl News announcement | `cerkl_innercerkl-news` | `share-1200x628` |
| Intercom in-app banner | `cerkl_intercom` | `share-1200x628` |
| Customer-success outreach | `cerkl_customer-success` | `speaker-card` |
| Sales enablement | `cerkl_sales` | `speaker-card` |
| Zoom waiting room (day-of) | — (on-event) | `zoom-banner` |
| Recording / on-demand page | `cerkl_email` (follow-up) | `recording-thumbnail` |
| Recap blog (SEO archive) | `cerkl_email` (recap) | `recap-blog-cover` |
