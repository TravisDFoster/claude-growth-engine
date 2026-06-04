# Prospect brand reverse-engineering process

> How to stand up a working brand kit for a prospect we're selling to — colors, fonts, logo — by mining their public web presence. Encodes learnings from the first live build (2026-06).
>
> **Used by:** sales presentations, outbound visual collateral, partner co-marketing, ABM landing pages, account-styled one-pagers, and anywhere we need to render a prospect's brand back to them.
>
> **Output:** a folder named `<prospect>-brand-guidelines/` (same shape as Cerkl's brand kit). One kit per prospect — placed alongside the **first** process that needs it, then referenced by every downstream process. These folders live local-only (gitignored under `sales/presentations/`).

---

## Why this exists

Sending a prospect a deck styled in their own brand is a small but real sales signal — "we already understand you enough to mock up how this would feel." But: official brand kits are private. We have to mine public sources.

This process gets us to ~90% accurate in about 15 minutes. The remaining 10% (exact PMS swatches, official lockup geometry, photography style) we don't need for a pitch deck.

---

## The 6-step recipe

### 1. Pull the homepage CSS for fonts

The fastest way to identify a prospect's typography:

```bash
curl -sL "https://www.<prospect>.com" | grep -oE 'font-family[^;}]+' | sort -u
```

Look for the most-repeated `font-family` declaration that *isn't* `system-ui` or `inherit` — that's their display font. The secondary one is usually their body font.

Then check for `@font-face` declarations in their stylesheets:

```bash
# Find linked stylesheets first
curl -sL "https://www.<prospect>.com" | grep -oE 'href="[^"]+\.css[^"]*"'

# Then pull each and grep for @font-face
curl -sL "https://www.<prospect>.com/path/to/site.css" | grep -oE '@font-face[^}]+}'
```

The `@font-face src:` URLs tell you exact font files they self-host — confirming the family + which weights they use.

**Real example:** an enterprise prospect served `TWK Everett` (display) + `Roboto` (body), with self-hosted weights 200/300/400/500/700/800.

---

### 2. Find their design system on GitHub

Many enterprises publish their design tokens publicly even when the brand guidelines are private. Search:

- GitHub: `<prospect> design system`, `<prospect>-design-system`, `<prospect>-foundation`
- The repo's `tokens/` folder usually contains color JSON in W3C Design Token format

**Real example:** one enterprise prospect publishes a `*-foundation` design-system repo with the full color palette in `tokens/Color Palette/Color.json`, including an explicit `50-brand: #<hex>` annotation that confirms which color is THE brand color.

If they don't have a public design system, fall back to:

- Live CSS `:root` CSS-variable declarations
- Hand-eye-droppering hex codes from the homepage (Browser DevTools)
- Aggregator sites like brandfetch.com, brandcolors.org (lower trust, but a starting point)

---

### 3. Confirm the primary brand color

Even with a full palette, the prospect uses **one signature color**. It's almost always:

- The button color (call-to-action)
- The logo color
- The link color
- The most-recurring accent on hero illustrations

Cross-check 2–3 of those. They should agree.

---

### 4. Grab the logo

Find the official asset URL in the homepage HTML:

```bash
curl -sL "https://www.<prospect>.com" | grep -oE '(src|href)="[^"]*logo[^"]*"' | head
```

Enterprise sites usually serve logos from a CDN like Scene7, Cloudflare Images, or Akamai. Download the SVG if available — it's tiny, infinitely scalable, and easy to recolor. Wikimedia Commons is a backup source (`<Prospect>_logo.svg` etc.).

**For PPTX use, also save a PNG** at 800–1600px wide, transparent background. python-pptx doesn't accept SVG.

Generate color variants by sed-replacing the fill:

```bash
sed 's/#<original-hex>/#ffffff/g' logo.svg > logo-white.svg
sed 's/#<original-hex>/#000000/g' logo.svg > logo-black.svg
```

---

### 5. Make the font-licensing call

Most enterprises use commercial typefaces. You have three options:

| Option | When to use |
|---|---|
| **Use free Google Fonts substitute** | Default — for one-off or low-volume sales decks. **Inter** is the safe geometric-sans stand-in for almost any modern enterprise display font. **Roboto** stands in for body text. |
| **License the real font** | When the prospect becomes a real opportunity and you'll be making multiple touchpoints. Typical foundry pricing: $50–150 per weight for indie foundries. |
| **Use system fonts** | Last resort. Helvetica/Arial works but looks generic. |

Document the substitution decision in the brand kit's `typography.md` so the next agent doesn't have to re-litigate it.

---

### 6. Stand up the kit

Mirror the file shape from Cerkl's [`Brand Guidelines/`](../marketing/design/branding-assets/Brand%20Guidelines/) — that's the reference structure:

```
<consuming-process-folder>/<prospect>-brand-guidelines/
├── INDEX.md            ← router, sources, at-a-glance, known gaps
├── colors.md           ← primary palette + full scales + data viz + don'ts
├── typography.md       ← font names, type scale, fallback decision
├── logo-guide.md       ← logo files, color rules, clear space, co-branding with Cerkl
└── logos/
    ├── <prospect>-logo-color.svg
    ├── <prospect>-logo-color.png
    ├── <prospect>-logo-white.svg
    └── <prospect>-logo-black.svg
```

**Where to put it:** alongside the first process that needs it. Common locations:
- Sales deck → `sales/presentations/<prospect>-brand-guidelines/`
- Outbound landing page → `sales/outbound/<prospect>-brand-guidelines/`
- ABM one-pager → `sales/enablement/<prospect>-brand-guidelines/`

Other processes reference by relative path. If a prospect gets multiple touchpoints over time, leave the kit where it landed and link to it — **don't duplicate**.

**Template:** copy the structure of any existing `<prospect>-brand-guidelines/` folder under `sales/presentations/` (local-only). Keep the section headings and table shapes; replace prospect-specific content.

---

## INDEX.md — what to include

Every prospect brand kit's `INDEX.md` should have these sections:

1. **Sources** — where you pulled this from (homepage URL, design system repo, asset CDN). Future-you needs to know what to re-check when the prospect rebrands.
2. **At-a-glance** — primary color, primary type, logo style, tone, tagline. One-line each.
3. **Known gaps** — what you couldn't verify from public sources. Always honest. Examples: licensing details, exact clear-space spec, photography style, secondary palette tiers.

See the `INDEX.md` of any existing `<prospect>-brand-guidelines/` folder as the canonical example (local-only).

---

## Co-branding rules (Cerkl × prospect)

Most consuming processes will pair the prospect's brand with Cerkl's (decks, landing pages, partner collateral). Add a "Co-branding" section to `logo-guide.md` covering:

- **Divider style** between the two logos (usually a 1px hairline in a neutral gray)
- **Optical-height matching** — wordmark cap-heights vary; size logos to read at the same visual weight, not the same bounding box
- **Color pairing rule** — usually each brand's primary color on light backgrounds; reversed-white versions on dark
- **Minimum separation** — at least 2× the larger logo's clear-space rule

Document this in the kit's `logo-guide.md` under a "Co-branding with Cerkl" section.

---

## Common failure modes

- **Mistaking a marketing-page accent for the brand color.** Always cross-check 2–3 surfaces (button, logo, link). If they disagree, the *logo* color is canonical.
- **Pulling fonts from Google Fonts when the prospect uses a commercial face.** If you see `TWK Everett`, `Söhne`, `GT America`, `Founders Grotesk` — those are *commercial*. Don't pretend Inter is "what they use"; document Inter as the *stand-in*.
- **Downloading a JPEG logo from an aggregator.** Always prefer the SVG from the prospect's own CDN. JPEGs from third-party sites are often outdated, low-res, or wrong-color.
- **Skipping the "known gaps" section.** Future agents (and Travis) need to know what's confirmed vs. eyeballed.

---

## Time budget

| Step | Time |
|---|---|
| 1. CSS fonts | 2 min |
| 2. Design system / palette | 5 min |
| 3. Primary color confirmation | 1 min |
| 4. Logo grab + variants | 3 min |
| 5. Font licensing call | 2 min |
| 6. Stand up the kit | 5–10 min (copy template, fill content) |
| **Total** | **~20 min** |

Past 30 minutes = you've hit a wall on something. Most likely the prospect has no public design system. Note the gap in INDEX.md and ship.
