# Canva Brand Template Element Map (batch A)
> Generated 2026-06-01 by parallel crawl. Captures the slot shape of each template for use by the create-then-edit Canva automation. Inspection design_ids are throwaway artifacts requiring manual cleanup in Canva.

## Quotes and testimonials — `EAHK4xxpksA`
- use_case: social-quotes-testimonials
- canvas: 1080x1080 (pages 1-3); 1080x1350 (page 4)
- pages: 4
- inspection design_id: `DAHLW7G5Img`
- text slots (page 1):
  - "Firstname Lastname / Title, Company" — name/title block (in pill shape)
  - "Lorem ipsum dolor sit amet, ..." — quote body
- image slots (page 1):
  - full-page fill (1080x1080), role: full-bg, current asset_id: `MAHK4W0nNeI`
  - 192x67, role: logo (Cerkl wordmark), current asset_id: `MAHHJ8ab-yI`
  - 230x188, role: decorative (quote-mark graphic), current asset_id: `MAHK4uDIWU8`
- text slots (page 2):
  - "Optional Frame for headshot photo / DELETE IF UNUSED" — headshot frame label (shape)
  - "Firstname Lastname / Title, Company" — name/title block
  - "Lorem ipsum dolor sit amet, ..." — quote body
- image slots (page 2):
  - full-page fill (1080x1080), role: full-bg, current asset_id: `MAHK4l-S0UA`
  - 224x181, role: decorative (quote-mark), current asset_id: `MAHK4m7Ag_M`
  - 192x67, role: logo, current asset_id: `MAHHJ8ab-yI`
- text slots (page 3):
  - "Optional Frame for headshot photo / DELETE IF UNUSED" — headshot frame label
  - "Firstname Lastname" — name
  - "Title, Company" — title
  - "Lorem ipsum dolor sit amet, ..." — quote body
- image slots (page 3):
  - full-page fill (1080x1080), role: full-bg, current asset_id: `MAHK4drp8mg`
  - 192x67, role: logo, current asset_id: `MAHHJ8ab-yI`
  - 162x132, role: decorative (quote-mark), current asset_id: `MAHK4yRWFzA`
- text slots (page 4):
  - "Optional Frame for headshot photo / DELETE IF UNUSED" — headshot frame label
  - "OPTIONAL SPACE FOR LOGO" — logo placeholder shape
  - "Firstname Lastname" — name
  - "Title, Company" — title
  - "Lorem ipsum dolor sit amet, ..." — quote body
- image slots (page 4):
  - full-page fill (1080x1350), role: full-bg, current asset_id: `MAHK4UJw0oU`
  - 192x67, role: logo, current asset_id: `MAHHJ8ab-yI`
  - 191x155, role: decorative (quote-mark), current asset_id: `MAHK4m7Ag_M`
- notes: 4 distinct quote-card variants (page 4 is portrait 1080x1350 not square). Each page has its own full-bg image fill (different backgrounds). Cerkl wordmark logo asset MAHHJ8ab-yI repeats on every page. Headshot frames are optional decorative SHAPE placeholders with "DELETE IF UNUSED" instructions — no separate image fill bound to them, so a runtime headshot insert would need to add a fill or use the SHAPE's container. No layered image-on-image frames detected; quote-mark graphics are non-editable decorative fills.
---

## Downloadable Asset Promotion Template — `EAHJ5Aa1cUw`
- use_case: downloadable-asset-promo-square
- canvas: 1080x1080
- pages: 5
- inspection design_id: `DAHLW6bco3c`
- text slots (page 1):
  - "AI-Powered Internal Communications Strategy Template" — headline (800x216)
  - "Define communication objectives" — bullet 1
  - "Map audiences and channels" — bullet 2
  - "Improve message consistency" — bullet 3
  - "Access Now" — CTA button label (inside pill SHAPE)
  - "Example Image" — top label SHAPE (decorative banner)
- image slots (page 1):
  - full-page fill (1080x1080), role: full-bg, current asset_id: `MAHJ40A0LrI`
  - 930x516, role: photo-slot (lower half asset preview), current asset_id: `MAHJ41v7nMA` — layered frame: yes — image swap targets this lower-half fill, sits over the full-bg
  - 240x83, role: logo (Cerkl wordmark), current asset_id: `MAHHJ8ab-yI`
  - 60x60, role: icon (CTA arrow), current asset_id: `MAHG2X6g4mw`
  - three 45x45 icons (check marks at bullets), role: icon, current asset_id: `MAHHTkSOnB8`
- text slots (page 2): same skeleton with "Excepteur sint occaecat..." headline + 3 Lorem bullets + "Access Now" CTA
- image slots (page 2): full-bg `MAHJ40A0LrI`; logo `MAHHJ8ab-yI` (240x83); CTA arrow `MAHG2X6g4mw` (60x60); 3 check icons `MAHHTkSOnB8` (45x45) — NOTE: no editable photo-slot on page 2 (text-only variant)
- text slots (page 3):
  - "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod" — large headline (733x323)
  - "Access Now" — CTA text (602x58, full-width style)
- image slots (page 3):
  - full-page fill (1080x1080), role: full-bg, current asset_id: `MAHJ40Y4_Kg`
  - 60x60, role: icon (CTA arrow), current asset_id: `MAHG2X6g4mw`
  - 204x71, role: logo (Cerkl wordmark, smaller variant), current asset_id: `MAHHJ8ab-yI`
- text slots (page 4): same skeleton as page 2 (3-bullet variant)
- image slots (page 4): full-bg `MAHJ4_OUDcM`; logo `MAHHJ8ab-yI` (240x83); CTA arrow `MAHG2X6g4mw` (60x60); 3 check icons `MAHHTkSOnB8` (45x45)
- text slots (page 5): "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod" headline + "Access Now" CTA
- image slots (page 5): full-bg `MAHJ46i86FI`; logo `MAHHJ8ab-yI` (204x71); CTA arrow `MAHG2X6g4mw` (60x60)
- notes: 5 variants for downloadable-asset promo carousel. Pages 1+2+4 share the "headline + 3 bullets + CTA" skeleton with full-bg + decorative check icons. Page 1 alone has the editable photo-slot (covers lower half — clearly layered atop full-bg, so image swap must target element_id `PBJKm2VzwCYry0cH-LB2n9TTS4PgkvYKG`). Pages 3+5 are headline-only variants. Cerkl wordmark `MAHHJ8ab-yI` repeats on every page. CTA arrow icon `MAHG2X6g4mw` and check icon `MAHHTkSOnB8` are NON-editable.
---

## Square post_ Webinar — `EAGqLOHvqK8`
- use_case: webinar-square-generic
- canvas: 1080x1080
- pages: 3
- inspection design_id: `DAHLWw_aD4Q`
- text slots (page 1):
  - "live webinar" — pill badge (SHAPE)
  - "Date and time" — date/time line
  - "Webinar title" — main headline
  - "Hosted by:" — section label
  - "Name" / "Title" x2 — speaker 1 + 2 name/title pairs
  - "INsert logo(s)" — bottom logo placeholder text
- image slots (page 1):
  - full-page fill (1080x1080), role: full-bg, current asset_id: `MAGRO9QE3rg`
- text slots (page 2): same skeleton with 3 speakers (Name/Title triple)
- image slots (page 2): full-bg `MAGRO9QE3rg` (1080x1080)
- text slots (page 3): same headline skeleton; 4 speaker Name/Title pairs arranged in 2x2 grid below
- image slots (page 3): full-bg `MAGRO9QE3rg` (1080x1080)
- notes: NO editable image fills for speaker headshots — the visible speaker thumbnails are within the single full-bg fill (rendered as part of background). Headshot insertion requires adding new image elements at speaker position. This contradicts speaker-card layered-frame pattern seen in EAGqLMN8_Po. Only full-bg image is editable. Logo placeholder is text-only ("INsert logo(s)") not a fill.
---

## Square Social_speakers_Thought Leadership_Webinar Series — `EAGqLMN8_Po`
- use_case: webinar-speaker-card
- canvas: 1080x1080
- pages: 3
- inspection design_id: `DAHLW7fJPJY`
- text slots (page 1):
  - "Webinar" — top tag label
  - "|   Mar 6, 2025 1:00 pm est" — date/time tag
  - "Webinar title" — main headline
  - "Name" / "Title" x2 — 2 speakers (right column)
  - "Presented by:" — bottom-left label (preceded by Cerkl logo image fill)
- image slots (page 1):
  - full-page fill (1080x1080), role: full-bg, current asset_id: `MAGg-8Ldy8k`
  - 32x32, role: icon (play icon next to "Webinar"), current asset_id: `MAGg-1Nbpjs`
  - 296x296, role: decorative-badge (IC Thought Leadership Series round badge), current asset_id: `MAGg-9y8TiY`
  - 247x247, role: headshot (speaker 1 frame, layered over bg), current asset_id: `MAGg-_VYc0Q` — layered frame: yes — image swap targets this fill
  - 247x247, role: headshot (speaker 2 frame), current asset_id: `MAGg-_VYc0Q` — layered frame: yes
  - 111x40, role: logo (Cerkl wordmark), current asset_id: `MAFYswpMFus`
- text slots (page 2): same skeleton with 3 speakers (Name/Title triple — across bottom row)
- image slots (page 2): full-bg `MAGg-8Ldy8k`; play icon `MAGg-1Nbpjs` (32x32); IC badge `MAGg-9y8TiY` (296x296); 3 headshot frames `MAGg-_VYc0Q` (247x247 each, layered); logo `MAFYswpMFus` (111x40)
- text slots (page 3): same headline; 4 speaker Name/Title pairs in right column
- image slots (page 3): full-bg `MAGg-8Ldy8k`; play icon `MAGg-1Nbpjs` (32x32); IC badge `MAGg-9y8TiY` (296x296); 4 headshot frames `MAGg-_VYc0Q` (183x183 each, 2x2 grid, layered); logo `MAFYswpMFus` (111x40)
- notes: CRITICAL layered-frame pattern — all headshot fills (`MAGg-_VYc0Q`) are independent editable image elements layered atop the full-bg fill. Image swap for a speaker MUST target the specific headshot element_id (NOT the bg). This is the canonical layered-frame template the 2026-05-29 spike identified. Cerkl logo is bottom-right wordmark image fill (not text). IC Thought Leadership badge is decorative circle 296x296 — large round = decorative-badge per inference rule. 2/3/4 speaker variants align with EAGqLOHvqK8 page-count.
---

## TEMPLATE: Downloadable resource/Email template promo_square — `EAGqLDRlwkI`
- use_case: downloadable-resource-email-promo-square
- canvas: 1080x1080
- pages: 8
- inspection design_id: `DAHLW_wSA80`
- text slots (page 1):
  - "Heading" — headline (864x76)
  - "Benefit 1 / Benefit 2 / Benefit 3" — bullet list (555x212)
  - "Access Now" — CTA pill (SHAPE)
- image slots (page 1):
  - full-page fill (1080x1080), role: full-bg, current asset_id: `MAGi11H7iek`
  - 579x132, role: logo (Cerkl x Broadcast lockup at top), current asset_id: `MAFvNSHHFmY`
  - 703x703, role: photo-slot (resource preview, right side), current asset_id: `MAGi16981As` — layered frame: yes — image swap targets this large fill atop the full-bg
- text slots (pages 2-4): same skeleton (Heading + 3 benefits + Access Now). Page 4 has bullets right-aligned instead of left.
- image slots (page 2): full-bg `MAGi17MbIqI`; logo lockup `MAFvNRVZhsQ` (579x132); resource preview `MAGi16981As` (703x703, layered)
- image slots (page 3): full-bg `MAGi16BlaWM`; logo lockup `MAFvNSHHFmY`; resource preview `MAGi16981As` (703x703, layered)
- image slots (page 4): full-bg `MAGi1wZ2Lkc`; logo lockup `MAFvNSHHFmY`; resource preview `MAGi16981As` (703x703, layered, positioned left)
- text slots (pages 5-8):
  - "Heading" — headline
  - "Body" — body line (864x44)
  - "Access Now" — bottom-strip SHAPE
- image slots (page 5): full-bg `MAGi11H7iek`; logo lockup `MAFvNSHHFmY`; oversized preview `MAGi1xwRXTw` (579x1865, extends beyond canvas, layered)
- image slots (page 6): full-bg `MAGi17MbIqI`; logo lockup `MAFvNRVZhsQ`; oversized preview `MAGi1xwRXTw` (layered)
- image slots (page 7): full-bg `MAGi16BlaWM`; logo lockup `MAFvNSHHFmY`; oversized preview `MAGi1xwRXTw` (layered)
- image slots (page 8): full-bg `MAGi1wZ2Lkc`; logo lockup `MAFvNSHHFmY`; oversized preview `MAGi1wOQsw4` (578x1865, layered)
- notes: Largest template so far — 8 pages = 4 color variants × 2 layouts (3-bullet vs body-only). Logo lockup `MAFvNSHHFmY` (or `MAFvNRVZhsQ` for darker variant) anchors every page. Resource preview fill is heavily layered (703x703 square or 579x1865 vertical) — all swaps must target the specific preview element_id, NOT the bg. Pages 5-8 use bottom CTA strip SHAPE rather than top-left pill button. The pre-existing oversized preview height (1865px) suggests intentional crop — content extends below the canvas.
---

## Title + CTA + Product image_Square post — `EAHJPZD93P8`
- use_case: social-square-cta-product
- canvas: 1080x1080
- pages: 4
- inspection design_id: `DAHLW0RWNYw`
- text slots (page 1):
  - "Build and manage audiences so every message is relevant" — headline (864x134)
  - "Start free with Foundations" — CTA pill text (SHAPE container)
- image slots (page 1):
  - full-page fill (1080x1080), role: full-bg, current asset_id: `MAHJO5gD7-4`
  - 841x562, role: photo-slot (product screenshot), current asset_id: `MAHJPOAGAzQ` — layered frame: yes
  - 56x56, role: icon (CTA arrow), current asset_id: `MAHG2X6g4mw`
  - 352x72, role: logo (Broadcast lockup), current asset_id: `MAHG2o30xY0`
- text slots (page 2): "Create better emails faster with built-in consistency & control" + "Start free with Foundations" CTA
- image slots (page 2): full-bg `MAHJO7ebNuI`; product screenshot `MAG_crWuMmo` (964x644, layered); CTA arrow `MAHG2X6g4mw` (56x56); Broadcast lockup `MAHG2o30xY0`
- text slots (page 3): "Build emails that actually get read" + "Learn More" CTA pill
- image slots (page 3): full-bg `MAHJO8JUOFE`; CTA arrow `MAHG2X6g4mw` (45x45); product screenshot `MAG_crWuMmo` (936x625, layered); Broadcast lockup `MAHG2o30xY0`
- text slots (page 4): "Turn insights into better communication" + "Learn More" CTA
- image slots (page 4): full-bg `MAHJOxiYjSM`; CTA arrow `MAHG2X6g4mw` (45x45); product screenshot `MAHAD9i1oWI` (936x625, layered); Broadcast lockup `MAHG2o30xY0`
- notes: Foundations product promo carousel — pages 1+2 use bottom-strip Foundations CTA; pages 3+4 use top-left "Learn More" pill. Product screenshots are always layered atop full-bg (swap target is the screenshot fill, not bg). Broadcast wordmark `MAHG2o30xY0` and CTA arrow `MAHG2X6g4mw` are non-editable.
---

## Square_Data / IC Fact post — `EAHG3Tpp4CI`
- use_case: linkedin-stat-card
- canvas: 1080x1080
- pages: 4
- inspection design_id: `DAHLW9wA8NA`
- text slots (page 1):
  - "60%" — large stat number (664x224)
  - "of employees say they miss important updates" — stat body (760x155)
  - "Learn more at cerkl.com" — CTA pill text (over CTA capsule SHAPE)
  - "Example post" — top tag SHAPE (decorative)
- image slots (page 1):
  - full-page fill (1080x1080), role: full-bg, current asset_id: `MAHG1QAn6v0`
  - 65x65, role: icon (Broadcast/compass mark, bottom-right), current asset_id: `MAGq6IEEnQQ`
  - 104x104, role: icon (page-number "1" badge top-right), current asset_id: `MAHG22i2Esw`
  - 716x103, role: photo-slot (browser-window/CTA capsule frame), current asset_id: `MAHG1nvS6R0` — layered frame: yes (decorative panel)
  - 56x56, role: icon (CTA arrow inside capsule), current asset_id: `MAHG2X6g4mw`
- text slots (page 2): "XX%" placeholder + "Lorem ipsum dolor sit amet, consectetur elit" + CTA
- image slots (page 2): full-bg `MAHG1QAn6v0`; compass `MAGq6IEEnQQ`; page-number badge `MAHG22i2Esw`; CTA capsule `MAHG1nvS6R0`; CTA arrow `MAHG2X6g4mw`
- text slots (page 3):
  - "Stop Sending Emails No One Reads" — headline (760x174)
  - "If your internal messages are competing with 100+ daily emails, your strategy needs more than better subject lines." — body (760x222)
  - "Learn more at cerkl.com" — CTA
  - "Example post" — top tag SHAPE
- image slots (page 3): full-bg `MAHG1VWzUTw` (different bg); compass `MAGq6IEEnQQ`; page-number badge `MAHG22i2Esw`; CTA capsule `MAHG1nvS6R0`; CTA arrow `MAHG2X6g4mw`
- text slots (page 4): same skeleton as page 3, Lorem placeholders
- image slots (page 4): full-bg `MAHG1VWzUTw`; compass `MAGq6IEEnQQ`; page-number badge `MAHG22i2Esw`; CTA capsule `MAHG1nvS6R0`; CTA arrow `MAHG2X6g4mw`
- notes: Stat-card carousel — pages 1+2 are XX% + statement; pages 3+4 are headline + body variant. Browser-window "CTA capsule" (`MAHG1nvS6R0`) sits inside the bg as decorative panel — non-editable, contains text + arrow icon overlaid. Page-number badge `MAHG22i2Esw` is the same "1" icon on every page (likely needs swap per slide for carousel pagination). Cerkl/Broadcast compass mark bottom-right is editable but tiny. No headshot/photo slot — stat-driven only.
---

## Linkedin pdf post_style 2 — `EAGqLAeuCc0`
- use_case: linkedin-pdf-carousel
- canvas: 1080x1080
- pages: 4
- inspection design_id: `DAHLW49F_BE`
- text slots (page 1):
  - "Lorem ipsum dolor sit amet, consecteur" — title headline (864x155)
- image slots (page 1):
  - full-page fill (1080x1080), role: full-bg, current asset_id: `MAFaAed19WI`
  - 380x146, role: logo (Broadcast powered by Cerkl lockup, top-left), current asset_id: `MAFYs9rAVro`
- text slots (page 2):
  - "1" — page-number numeral (over circle SHAPE)
  - "Lorem ipsum dolor sit amet, consectetuer" — section headline
  - "Lorem ipsum dolor sit amet... tincunt." — body (864x157)
- image slots (page 2):
  - full-page fill (1080x1080), role: full-bg, current asset_id: `MAFaAaDm0gc`
- text slots (page 3): "2" numeral, section headline + body (same skeleton)
- image slots (page 3): full-bg `MAFaAZHrmAY`
- text slots (page 4): "3" numeral + section headline + body
- image slots (page 4): full-bg `MAFaAed19WI`
- notes: Lightweight 4-page text-only carousel — only page 1 (cover) has the Broadcast logo lockup image. Pages 2-4 are numbered content slides (1/2/3 numeral inside circle SHAPE). No editable photo slots besides full-bg per page. Body image visible in cover thumbnail is actually part of the bg fill (single full-bg asset).
---

## Square post_style 6 — `EAGqLKYVlQs`
- use_case: social-square-style
- canvas: 1080x1080
- pages: 1
- inspection design_id: `DAHLW5Uxsdg`
- text slots (page 1):
  - "XX%" — large stat (346x200)
  - "Lorem ipsum dolor sit amet, consectetuer" — statement (864x176)
  - "Learn more at Cerkl.com" — CTA text
- image slots (page 1):
  - full-page fill (1080x1080), role: full-bg, current asset_id: `MAFZifQs_is`
  - 380x146, role: logo (Broadcast powered by Cerkl), current asset_id: `MAFYs9rAVro`
- notes: Minimal 1-page stat card. No CTA arrow image (arrow is part of bg or absent). Just full-bg + Broadcast logo image. Cleanest skeleton in this set.
---

## Square Social_countdown_Thought Leadership_Webinar Series — `EAGqLGh6dGQ`
- use_case: webinar-countdown
- canvas: 1080x1080
- pages: 1
- inspection design_id: `DAHLW5y1nMw`
- text slots (page 1):
  - "Mar 6, 2025 1:00 pm est" — date/time label
  - "Webinar" — tag label
  - "Webinar title" — headline
  - "X" — large countdown numeral (212x331)
  - "DAYS TO GO" — countdown label
  - "Register Now" — CTA pill (SHAPE)
- image slots (page 1):
  - full-bg (1080x1080), role: full-bg, current asset_id: `MAGg-3xM4lg`
  - 103x36, role: logo (Cerkl wordmark, top-right), current asset_id: `MAFYswpMFus`
  - 32x32, role: icon (play icon next to "Webinar"), current asset_id: `MAGg-1Nbpjs`
  - 390x390, role: decorative-badge (IC Thought Leadership round badge), current asset_id: `MAGg-9y8TiY`
- notes: 1-page countdown variant of the webinar speaker card series. Reuses Cerkl wordmark + play icon + Thought Leadership badge. Days-to-go numeral is text only (X placeholder). No headshot fills.
---

## Square post_style 5 — `EAGqLAaxqWw`
- use_case: social-square-style
- canvas: 1080x1080
- pages: 1
- inspection design_id: `DAHLWwGZvs8`
- text slots (page 1):
  - "Feb 14th, 2023 @ 2:00 pm Est" — date/time
  - "Venue  |  Location" — venue line
  - "Conference Title" — main headline
  - "Firstname Lastname" — speaker name
  - "Company  |  Position" — speaker title
- image slots (page 1):
  - 1080x200 strip at top of speaker block, role: photo-slot (gradient strip behind speaker), current asset_id: `MAFZjeQawlc`
  - 276x106, role: logo (Broadcast lockup bottom-left), current asset_id: `MAFYs2RusE8`
- notes: Conference promo card — bg is a SHAPE (1080x1080) not an image fill. Round photo decorative (582x582 SHAPE bottom-right) is also a SHAPE not editable image. Only two image fills: gradient strip (behind speaker block) and Broadcast logo lockup. NO speaker headshot fill — name/title is text only. This is a low-image template.
---

## Square post_style 3 — `EAGqLD4Janc`
- use_case: social-square-style
- canvas: 1080x1080
- pages: 1
- inspection design_id: `DAHLWxxNPHw`
- text slots (page 1):
  - "Add a heading" — main headline (864x108)
  - "Your paragraph text" — body
  - "Position title" — pill button SHAPE (open-position label)
  - "View our other open positions" — CTA text
- image slots (page 1):
  - full-bg (1080x1080), role: full-bg, current asset_id: `MAFZiTukXmQ`
  - 287x160, role: logo (Cerkl wordmark top-left), current asset_id: `MAFZjCbguOo`
- notes: Hiring/job-post card. Two image fills (bg + logo). CTA arrow visible in render appears to be part of bg.
---

## Square post_style 4 — `EAGqLEHWJkk`
- use_case: social-square-style
- canvas: 1080x1080
- pages: 1
- inspection design_id: `DAHLW-fc51M`
- text slots (page 1):
  - "Firstname Lastname" — speaker name
  - "Company / Position" — speaker title
  - "Lorem ipsum dolor sit amet..." — testimonial quote (724x286)
- image slots (page 1):
  - full-page fill (1080x1080), role: full-bg, current asset_id: `MAFZibaLuGo`
  - 449x295, role: decorative (curved corner shape top-right), current asset_id: `MAFZjd4R99g` — layered
  - 381x146, role: logo (Broadcast lockup top-left), current asset_id: `MAFYs2RusE8`
  - 566x288, role: decorative (curved shape bottom-right), current asset_id: `MAFZjU488WI` — layered
- notes: Testimonial card with curved orange decorative shapes flanking. Quote card SHAPE (864x590) and round headshot frame (324x324 SHAPE) are NOT image fills — they are SHAPE-only placeholders. Headshot insertion would require adding a fill into the round SHAPE. No editable headshot photo-slot fill currently. Decorative corner shapes are images.
---

## Square post_style 2 — `EAGqLJyJqD0`
- use_case: social-square-style
- canvas: 1080x1080
- pages: 1
- inspection design_id: `DAHLWwDoKCg`
- text slots (page 1):
  - "Lorem ipsum dolor sit amet, consectetuer" — body (864x135)
  - "Read the report" — CTA pill SHAPE
- image slots (page 1):
  - full-bg (1080x1080), role: full-bg, current asset_id: `MAFZiSmozos`
  - 352x135, role: logo (Broadcast lockup top-center), current asset_id: `MAFYs2RusE8`
- notes: Minimal 1-page. Center image visible in render is part of full-bg fill (not a separate editable slot). Just 2 image fills total.
---

## Square post_style 1 — `EAGqLD9C1Rk`
- use_case: social-square-style
- canvas: 1080x1080
- pages: 1
- inspection design_id: `DAHLW0_vRp0`
- text slots (page 1):
  - "Lorem ipsum dolor sit amet, consectetuer" — body (864x155)
- image slots (page 1):
  - full-bg (1080x1080), role: full-bg, current asset_id: `MAFZiXCGoq8`
  - 380x146, role: logo (Broadcast lockup top-left), current asset_id: `MAFYs9rAVro`
- notes: Bare minimum 1-page text post. The illustration shown in render is baked into full-bg fill. No CTA or button — just headline + logo.
---

## Linkedin pdf post_style 1 — `EAGqLFziaCE`
- use_case: linkedin-pdf-carousel
- canvas: 1080x1080
- pages: 4
- inspection design_id: `DAHLW2lQGII`
- text slots (page 1):
  - "Lorem ipsum dolor" — large headline (864x300)
  - "Lorem ipsum dolor sit amet... aliqua." — body (711x227)
  - feature-tag SHAPE (583x85, no text) — Broadcast feature tag container
  - CTA round SHAPE (110x110) bottom-right — arrow button
  - bottom bar SHAPE (1080x30) — slim accent strip
- image slots (page 1):
  - 497x44, role: icon (feature-tag label image inside top pill — e.g. "Broadcast Email Blasts"), current asset_id: `MAFZ10vmjv8`
- text slots (page 2): "Lorem ipsum dolor sit amet, consectetuer" headline (829x174)
- image slots (page 2):
  - 840x560, role: photo-slot (large content image, top half), current asset_id: `MAFZ18uJOMw`
- text slots (page 3):
  - "Customer name" — name
  - "Company / Position" — title
  - "Lorem ipsum dolor sit amet... consequat." — testimonial quote (864x404)
- image slots (page 3): no editable fills — headshot frame is missing (would need add)
- text slots (page 4):
  - "Lorem ipsum dolor sit amet, consectetuer" — outro headline (829x298)
  - "Learn more at Cerkl.com" — CTA pill SHAPE
- image slots (page 4):
  - 352x135, role: logo (Broadcast lockup), current asset_id: `MAFYs2RusE8`
- notes: 4-page carousel: cover (feature tag + body), photo slide, testimonial slide, outro CTA. Bottom bar SHAPE appears on every page (decorative accent). Almost everything is SHAPE-based — only 3 editable image fills total across all 4 pages: feature-tag label (p1), content photo (p2), Broadcast logo (p4). p3 testimonial has NO image — just text on bg.
---

## Linkedin pdf post_style 3 — `EAGqLLyZJpc`
- use_case: linkedin-pdf-carousel
- canvas: 1080x1080
- pages: 2
- inspection design_id: `DAHLW5FdQ2U`
- text slots (page 1):
  - "Lorem ipsum dolor sit amet, consectetuer" — headline (829x298)
  - "Learn more" — CTA pill SHAPE
  - CTA round arrow SHAPE (110x110) bottom-right (decorative)
- image slots (page 1):
  - full-bg (1080x1080), role: full-bg, current asset_id: `MAFaAUH0Qnw`
  - 352x135, role: logo (Broadcast lockup top-right), current asset_id: `MAFYs2RusE8`
- text slots (page 2):
  - 3x "XX%" stat numerals (210x115 each) inside circular SHAPE
  - 3x "Sed do eiusmod tempor incididunt ut labore et dolore." captions
- image slots (page 2): no image fills — page 2 is text-only stat grid
- notes: 2-page mini carousel: cover + stat-grid. Page 2 has 3 stat tiles (each = circle SHAPE + XX% text + caption text). Round headshot in page 1 thumbnail is baked into bg fill. Only 2 editable images (bg + logo) on p1; zero editable images on p2.
---

## Linkedin pdf post_Employee Spotlight 2 — `EAGqLAfjcls`
- use_case: linkedin-pdf-carousel-employee-spotlight
- canvas: 1080x1080
- pages: 3
- inspection design_id: `DAHLWzRhSH8`
- text slots (page 1):
  - "Employee Spotlight" — large cover headline (864x351)
  - CTA round SHAPE (110x110) bottom-right — arrow button
- image slots (page 1):
  - full-bg (1080x1080), role: full-bg, current asset_id: `MAFZ1kbYhG8`
- text slots (page 2):
  - "Firstname lastname" — name (330x41)
  - "Position" — title
  - "Lorem ipsum dolor sit amet... tempor nisi." — quote body (391x626)
- image slots (page 2):
  - 528x1080, role: photo-slot (full-height headshot, left half), current asset_id: `MAFZ1gSOjCY` — layered frame: yes — image swap targets this half-canvas headshot fill
- text slots (page 3):
  - "Join our Team!" — outro headline (864x136)
  - "Cerkl supports employees' whole selves as our business begins and ends with you." — body (829x210)
  - "View open opportunities" — CTA pill SHAPE
- image slots (page 3):
  - full-bg (1080x1080), role: full-bg, current asset_id: `MAFZ1kfCvR0`
- notes: 3-page employee spotlight: cover, half-photo-half-quote, outro CTA. The half-page headshot fill (528x1080) is the key swap target for personalization — clearly layered atop p2 bg. No CTA arrow image (it's all SHAPE).
---

## Copy of Linkedin pdf post_Employee Spotlight — `EAGqLEqOaM4`
- use_case: linkedin-pdf-carousel-employee-spotlight
- canvas: 1080x1080
- pages: 3
- inspection design_id: `DAHLW4eAQh8`
- text slots (page 1):
  - "Employee Spotlight" — cover headline (864x351)
  - CTA arrow SHAPE (110x110) — round button
- image slots (page 1):
  - full-bg (1080x1080), role: full-bg (dark), current asset_id: `MAFZ0-rZy4Y`
- text slots (page 2):
  - "Firstname Lastname" — name
  - "Position" — title
  - "Cerkl always prioritizes... How Work Should Be." — quote (864x263)
- image slots (page 2):
  - full-bg (1080x1080), role: full-bg, current asset_id: `MAFZ0yn26Cs`
  - 335x335, role: headshot (round, centered), current asset_id: `MABw6X6WEUY` — layered frame: yes (NON-editable in this template — note: editable=false, so swap may not be straightforward)
- text slots (page 3): "Join our Team!" headline + supporting body + "View open opportunities" CTA pill
- image slots (page 3): bg is a SHAPE (1080x1080), no editable image
- notes: Dark-mode variant of employee spotlight. Centered round headshot (vs half-page in EAGqLAfjcls). Headshot fill is marked editable:false here — may need to add new fill or workaround for personalization swap. p3 uses SHAPE background only.
---

## Linkedin pdf post_Employee Spotlight — `EAGqLOWcIHY`
- use_case: linkedin-pdf-carousel-employee-spotlight
- canvas: 1080x1080
- pages: 3
- inspection design_id: `DAHLW7P8r8s`
- text slots (page 1): "Employee Spotlight" headline + CTA arrow SHAPE
- image slots (page 1): full-bg `MAFZ0-rZy4Y` (dark)
- text slots (page 2): "Firstname Lastname" + "Position" + "Cerkl always prioritizes..." quote
- image slots (page 2): full-bg `MAFZ0yn26Cs`; 335x335 round headshot frame `MABw6X6WEUY` (editable:false, layered)
- text slots (page 3): "Join our Team!" + body + "View open opportunities" CTA pill
- image slots (page 3): SHAPE bg only, no editable image
- notes: IDENTICAL structure to EAGqLEqOaM4 (`Copy of...` variant). Same dark cover + centered headshot + outro CTA. Headshot fill non-editable here too. Treat as duplicate-of-record alongside EAGqLEqOaM4.
---

## LinkedIn Carousel_Problem Solution_2 — `EAHIEGj_L3s`
- use_case: linkedin-carousel-problem-solution
- canvas: 1080x1350
- pages: 7
- inspection design_id: `DAHLW4rQ0kM`
- text slots (page 1):
  - "Example COVER DELETE BEFORE EXPORT" — top tag SHAPE
  - "Why Yor Messages Aren't Driving Action" — headline (934x168)
  - "Lets break it down" — CTA pill text
- image slots (page 1):
  - full-bg (1080x1350), role: full-bg, current asset_id: `MAHIE1JZw6Q`
  - 936x111, role: photo-slot (CTA capsule bar bottom), current asset_id: `MAHH_YEVO1o`
  - 320x65, role: logo (Broadcast lockup), current asset_id: `MAHG2o30xY0`
  - 188x65, role: logo (Cerkl wordmark), current asset_id: `MAHHJ8ab-yI`
  - 981x664, role: photo-slot (product screenshot), current asset_id: `MAHAD9i1oWI` — layered frame: yes
  - 659x390, role: photo-slot (secondary product UI tile), current asset_id: `MAHADyPRVgc` — layered frame: yes
- text slots (page 2): "Lets break it down" CTA + "Lorem ipsum dolor sit amet, consectetur" body
- image slots (page 2): full-bg `MAHIE1JZw6Q`; CTA bar `MAHH_YEVO1o`; Broadcast lockup `MAHG2o30xY0`; Cerkl wordmark `MAHHJ8ab-yI`
- text slots (page 3):
  - "The Problem" — section label
  - "You're sending messages without a clear view of what's working" — headline body (864x222)
  - "Because they:" — sub-label
  - 3 bulleted points: "Surface-level metrics" / "Incomplete data" / "Assumptions about your audience"
  - "And improvement becomes guesswork" — closing line
  - "See how Broadcast can help" — CTA pill
- image slots (page 3): full-bg `MAHIEktU28A`; CTA bar `MAHH_YEVO1o`; 3x 39x39 bullet-point icons `MAHH_szrDxo`
- text slots (page 4): "See performance clearly" headline + body
- image slots (page 4): full-bg `MAHIErCTDqA`; 2x 959x650 product UI screenshots `MAHADx8yh_A` (layered atop each other — duplicate fills, possibly accordion-style stack)
- text slots (page 5): "Understand your audience" headline + body (829x201)
- image slots (page 5): full-bg `MAHIEnIkNJc`; 959x650 product UI screenshot `MAHAD2LWlZ4` (layered)
- text slots (page 6): "Optimize with real data" headline + body
- image slots (page 6): full-bg `MAHIEigA8o8`; 959x650 product UI screenshot `MAHAD_BUsO8` (layered)
- text slots (page 7):
  - "Get started today with Broadcast" — closing headline (864x200)
  - 3 feature bullets: "Track performance across every send" / "Understand engagement by audience" / "Optimize with real insights"
  - "Start free" — CTA pill SHAPE
- image slots (page 7): full-bg `MAHIErQuQlg`; 60x60 CTA arrow `MAHIAo1en1s`; 3x 60x60 check-circle icons `MAHHTkSOnB8`; 352x72 Broadcast lockup `MAHG2o30xY0`; 207x72 Cerkl wordmark `MAHHJ8ab-yI`
- notes: Most complex template in this set (7 pages, ~25 image fills total). Problem/solution carousel: cover → setup → problem → 3 solution slides → CTA recap. Pages 4-6 each carry a large 959x650 product UI screenshot (layered atop bg) — these are the key swap targets for product-specific carousels. Page 1 cover has TWO layered product screenshots stacked. CTA bar (`MAHH_YEVO1o`) repeats on every page as bottom strip. Bullet check-circle icons `MAHHTkSOnB8` re-used from EAHJ5Aa1cUw — shared icon library.
---

## Foundations and Product Images Templates — `EAHI2RC4_s8`
- use_case: foundations-product-images
- canvas: 1080x1350
- pages: 4
- inspection design_id: `DAHLW6zuDFc`
- text slots (page 1):
  - "Lorem ipsum dolor sit amet, consectetur adipiscing elit" — headline (864x250)
  - "Lorem ipsum dolor sit amet... aliqua." — body (864x157)
  - "Start free with Foundations" — CTA pill text + SHAPE
- image slots (page 1):
  - full-bg (1080x1350), role: full-bg, current asset_id: `MAHI2beEOSg`
  - 843x571, role: photo-slot (product UI montage), current asset_id: `MAG-KiuqDp8` — layered frame: yes
  - 65x65, role: icon (Cerkl compass mark), current asset_id: `MAGq6IEEnQQ`
  - 56x56, role: icon (CTA arrow), current asset_id: `MAHG2X6g4mw`
- text slots (page 2): "Duis aute irure dolor..." headline + "Start free with Foundations" CTA
- image slots (page 2): full-bg `MAHI1oJpYaM`; 320x65 Broadcast lockup `MAHG2o30xY0`; 188x65 Cerkl wordmark `MAHHJ8ab-yI`; 843x571 product UI `MAG-Kmnn3Kg` (layered); 56x56 CTA arrow `MAHG2X6g4mw`
- text slots (page 3):
  - "Excepteur sint occaecat..." — headline (864x250)
  - "Lorem ipsum dolor sit amet, adipiscing elit, sed do tempor." — subhead (864x129)
  - 3 bullet rows: "Duis aute irure dolor" / "Reprehenderit in voluptate" / "Excepteur sint occaecat"
- image slots (page 3): full-bg `MAHI2XnyHD4`; 65x65 compass `MAGq6IEEnQQ`; 3x 45x45 check icons `MAHHTkSOnB8`; 928x627 product UI `MAHA2RshL_k` (layered)
- text slots (page 4): "Duis aute irure dolor..." headline + body
- image slots (page 4): full-bg `MAHI1ntFOa4`; 320x65 Broadcast lockup; 188x65 Cerkl wordmark; 928x627 product UI `MAHAD9i1oWI` (layered)
- notes: 4-page 4:5 portrait product carousel. Each page has a layered product UI screenshot (843x571 or 928x627) — these are the primary swap targets. Pages 1+3 use compass `MAGq6IEEnQQ` + check-icons; pages 2+4 use Broadcast lockup + Cerkl wordmark at top. Bottom-right Broadcast watermark visible in render is part of bg.
---

## LinkedIn Carousel_3 Part List — `EAHHKqwQjWM`
- use_case: linkedin-carousel-3-part-list
- canvas: 1080x1350
- pages: 7
- inspection design_id: `DAHLWxYAwKM`
- text slots (page 1):
  - "Lorem ipsum dolor sit amet elit, sed do et dolore magna" — headline (810x280)
  - "Example COVER DELETE BEFOR EXPORT" — vertical side tag SHAPE
- image slots (page 1):
  - full-bg (1080x1350), role: full-bg, current asset_id: `MAHHJI7O-kk`
  - 926x768, role: photo-slot (top hero photo), current asset_id: `MAG8ANMAVHI` — layered frame: yes
  - 320x65, role: logo (Broadcast lockup), current asset_id: `MAHG2o30xY0`
  - 188x65, role: logo (Cerkl wordmark), current asset_id: `MAHHJ8ab-yI`
  - 157x112, role: icon (CTA arrow-in-circle), current asset_id: `MAHHI0qJPoA`
- text slots (page 2): same as page 1
- image slots (page 2): full-bg `MAHHJI7O-kk`; top hero photo `MAG_crWuMmo` (926x768, layered); CTA arrow + Broadcast lockup + Cerkl wordmark (same set)
- text slots (page 3): headline only (no photo)
- image slots (page 3): full-bg `MAHHJI7O-kk`; CTA arrow + Broadcast lockup + Cerkl wordmark
- text slots (pages 4-6):
  - "Lorem ipsum dolor sit amet, consectetur" — list-item headline (864x204)
  - "Lorem ipsum dolor sit amet... aliqua." — list-item body (864x186)
  - tiny SHAPE cluster (page-indicator dots, bottom)
- image slots (pages 4-6): full-bg only (`MAHHJLpF-_A`, `MAHHJA27HDw`, `MAHHJHp8So0` respectively)
- text slots (page 7):
  - "Duis aute dolor in reprehenderit" — closing headline (878x233)
  - "Lorem ipsum dolor sit amet, consectetur adipiscing elit" — feature 1
  - "Ut enim ad minim veniam, quis nostrud exercitation" — feature 2
  - "Start using a tool built for communicators" — CTA pill text (over SHAPE)
- image slots (page 7): full-bg `MAHHJHi2YzU`; 92x92 CTA arrow `MAHG2X6g4mw`; 352x72 Broadcast lockup; 207x72 Cerkl wordmark; 2x 52x52 check icons `MAHHTkSOnB8`
- notes: 7-page 4:5 carousel: 3 intro/cover slides + 3 list-item slides + outro CTA. Pages 1-3 reuse the same intro-slide skeleton (one hero photo each) with different bgs. Pages 4-6 are text-only list items with page-indicator dot cluster at bottom. Page 7 is the standard "Cerkl + Broadcast" outro CTA. Hero photo fills (`MAG8ANMAVHI`, `MAG_crWuMmo`) are the swap targets for cover photos.
---

## LinkedIn Carousel_Problem Solution_1 — `EAHIAt1o9d4`
- use_case: linkedin-carousel-problem-solution
- canvas: 1080x1350
- pages: 8
- inspection design_id: `DAHLWxVooZw`
- text slots (page 1): "Why Yor Messages Aren't Driving Action" headline + "Lets break it down" CTA + "Example COVER DELETE BEFOR EXPORT" tag
- image slots (page 1):
  - full-bg `MAHH_KXbtUA`
  - 1080x1080 hero photo `MAG8AFv60Gg` (top, layered)
  - 1080x929 gradient overlay `MAHH_YnT_7Q` (over photo, layered)
  - CTA bar `MAHH_YEVO1o` (936x111); Broadcast lockup `MAHG2o30xY0`; Cerkl wordmark `MAHHJ8ab-yI`
- text slots (page 2): headline + CTA (same pattern)
- image slots (page 2): full-bg + gradient `MAHH_YnT_7Q` + CTA bar + Broadcast + Cerkl lockups (NO hero photo on p2)
- text slots (page 3):
  - "The Problem" label
  - "Your messages are being seen—but not acted on" headline (864x168)
  - "Because they:" sub-label
  - 3 bullet items: "Try to reach everyone" / "Lack a clear next step" / "Arrive at the wrong time"
  - "Even strong content gets ignored" closing line
  - "How do you fix it" CTA pill
- image slots (page 3): full-bg `MAHH_MIHqOQ`; CTA bar; 3x 40x40 bullet icons `MAHH_szrDxo`
- text slots (page 4): "Solution:" + "Start with the Audience" + body
- image slots (page 4): full-bg `MAHH_GAjL4g` only
- text slots (page 5): "Solution:" + "Make the Message Actionable" + body
- image slots (page 5): full-bg `MAHH_MMzQA0` only
- text slots (page 6): "Solution:" + "Improve Timing" + body (864x402)
- image slots (page 6): full-bg `MAHH_DfUAJw` only
- text slots (page 7):
  - "How can Broadcast Help?" headline (864x226)
  - 3 feature rows: "Reach the right audience with targeted messaging" / "Deliver at the right time for higher engagement" / "Improve performance with real-time insights"
- image slots (page 7): full-bg `MAHH_Ia1UR8`; 3x 67x67 CTA arrow icons `MAHIAo1en1s`
- text slots (page 8):
  - "Reach the right audience with the right message at the right time" — final headline (878x461)
  - "Get started today with Broadcast" — closing CTA headline (864x168)
  - "Schedule a Chat" — CTA pill
- image slots (page 8): full-bg `MAHH_DB06Y0`; 60x60 arrow `MAHIAo1en1s`; 352x72 Broadcast lockup; 207x72 Cerkl wordmark
- notes: 8-page problem-solution carousel — sister template to EAHIEGj_L3s. Pages 1-3 share "intro/setup/problem" pattern with consistent CTA bar; pages 4-6 are 3 solution slides (text-only, full-bg); page 7 is feature recap; page 8 outro CTA. Hero photo on cover (`MAG8AFv60Gg`) has overlaid gradient mask `MAHH_YnT_7Q` — layered swap means: replace photo, keep gradient. No layered product UI screenshots on solution pages 4-6 (text-only). Bullet icon and CTA arrow ID library matches EAHIEGj_L3s.
---

## 1350x1080_Text only post — `EAHHbiYvZCE`
- use_case: social-landscape-text-only
- canvas: 1080x1350 (despite name "1350x1080", aspect is portrait 4:5)
- pages: 4
- inspection design_id: `DAHLWxPtVOk`
- text slots (page 1):
  - "Clarity is the Real Goal of Internal Comms" — headline (864x196)
  - "It's not about how many messages you send. It's about how well they're understood." — subhead (864x104)
  - 3 bullets: "Send targeted messages" / "Prioritize clarity over volume" / "Measure engagement beyond open rates"
  - "Start free with Foundations" — CTA pill SHAPE + text
  - "Example post" — top tag SHAPE
- image slots (page 1): full-bg `MAHHaO6osJ4`; 320x65 Broadcast lockup `MAHG2o30xY0`; 188x65 Cerkl wordmark `MAHHJ8ab-yI`; 3x 36x36 bullet icons `MAHHaQSgp6I`; 56x56 CTA arrow `MAHG2X6g4mw`
- text slots (page 2): "Lorem ipsum dolor sit amet, consectetur" headline + subhead + 3 Lorem bullets + same CTA
- image slots (page 2): same image set as page 1
- text slots (page 3):
  - "If Your Message Isn't Clear It Won't Drive Action" — headline (864x326)
  - 2 bullets: "Too many competing updates reduce understanding" / "Clear intent leads to better engagement"
  - "See Broadcast in Action" — CTA pill (different SHAPE)
  - "Example post" tag SHAPE
- image slots (page 3): full-bg `MAHHaCQJL64`; Broadcast lockup + Cerkl wordmark; 2x 36x36 bullet icons; 56x56 CTA arrow
- text slots (page 4): "Lorem ipsum dolor sit amet adipiscing elit sed do" headline + 2 Lorem bullets + "See Broadcast in Action" CTA
- image slots (page 4): same image set as page 3
- notes: 4-page text-only portrait carousel: pages 1-2 share "Foundations" CTA skeleton (3 bullets); pages 3-4 share "See Broadcast in Action" CTA skeleton (2 bullets). New radio-bullet icon `MAHHaQSgp6I` (vs the check `MAHHTkSOnB8` seen elsewhere). No photo slots — entirely text + bg + repeated icons.
---

## 1080x1350_Photo + text 1 — `EAHG3Ty0I9Y`
- use_case: social-portrait-photo-text
- canvas: 1080x1350
- pages: 4
- inspection design_id: `DAHLW-cGLeM`
- text slots (page 1):
  - "Why Employees Ignore Internal Emails (And How to Fix It)" — headline (864x259)
  - "It's not about attention spans..." body (864x235)
  - "Learn More" — CTA text
  - "Example post" — top tag SHAPE
- image slots (page 1):
  - full-bg `MAHG2dLGpEc`
  - 957x529, role: photo-slot (top half hero photo), current asset_id: `MAG8AJy7khI` — layered
  - 1080x987, role: photo-slot (large mid-bottom content panel), current asset_id: `MAHG2UepKQk` — layered
  - 346x71, role: logo (Broadcast lockup, bottom-left), current asset_id: `MAHG2o30xY0`
  - 56x56, role: icon (CTA arrow), current asset_id: `MAHG2X6g4mw`
- text slots (page 2): "Lorem ipsum..." headline + body + "Learn More" CTA (no top tag)
- image slots (page 2): full-bg `MAHG2dLGpEc`; 1080x987 content panel `MAHG2UepKQk` (layered); Broadcast lockup; CTA arrow (NO hero photo on p2)
- text slots (pages 3+4): same skeletons as 1+2 with different bg
- image slots (page 3): full-bg `MAHG2YeVAII`; hero photo `MAG8AOi6pmo` (layered); content panel `MAHG2ec8tYU` (layered); Broadcast lockup; CTA arrow
- image slots (page 4): full-bg `MAHG2YeVAII`; content panel `MAHG2ec8tYU` (layered); Broadcast lockup; CTA arrow
- notes: 4-page portrait carousel: 2 cover variants (with hero photo) + 2 secondary variants (text-only). Hero photo (957x529, top) is layered atop full-bg. Content panel fill `MAHG2UepKQk` / `MAHG2ec8tYU` is a large 1080x987 overlay covering bottom 73% — likely the white text panel.
---

## LinkedIn Carousel_5 Part List — `EAHHb4dbs1Y`
- use_case: linkedin-carousel-5-part-list
- canvas: 1080x1350
- pages: 9
- inspection design_id: `DAHLW6Q52TE`
- text slots (page 1): "Lorem ipsum dolor sit amet elit, sed do et dolore magna" headline + "Example COVER DELETE BEFOR EXPORT" tag
- image slots (page 1): full-bg `MAHHTYoxE18`; 926x768 hero photo `MAG8ANMAVHI` (layered); CTA arrow-circle icon `MAHHI0qJPoA` (157x112); Broadcast lockup; Cerkl wordmark
- text slots (page 2): same headline + tag
- image slots (page 2): full-bg + 926x768 hero photo `MAHA2RshL_k` (layered) + same icons/lockups
- text slots (page 3): headline only
- image slots (page 3): full-bg + icons/lockups (no hero photo)
- text slots (pages 4-8): each has:
  - "xxx #N" — list-item number tag SHAPE
  - "Lorem ipsum dolor sit amet, consectetur" — item headline (864x204)
  - "Lorem ipsum dolor sit amet... aliqua." — item body (864x186)
  - page-indicator dot cluster SHAPE row
- image slots (pages 4-8): full-bg only — `MAHHTQhjHIk` (p4,5,7) and `MAHHTdcPZ54` (p6,8) alternating
- text slots (page 9): "Duis aute dolor in reprehenderit" closing headline + 2 feature lines + "Start using a tool built for communicators" CTA
- image slots (page 9): full-bg `MAHHTfiq3_4`; 92x92 CTA arrow `MAHG2X6g4mw`; Broadcast lockup + Cerkl wordmark; 2x 52x52 check icons `MAHHTkSOnB8`
- notes: 9-page extension of the 3-Part List template (EAHHKqwQjWM) — same skeleton but with 5 item slides instead of 3. Page-indicator dot SHAPE cluster (5 dots) tracks current item. Hero photos on cover (p1+p2) are the only photo swap targets — p4-p8 are pure list items with bg color alternation. Outro is identical to EAHHKqwQjWM.
---

## Product_carousel — `EAG3Gmxux4Q`
- use_case: product-carousel-portrait
- canvas: 1080x1350
- pages: 6
- inspection design_id: `DAHLW7jqcT8`
- text slots (page 1):
  - "Introducing Calendar Invites" — headline (864x225)
  - "Send meetings directly..." subhead (864x166)
- image slots (page 1):
  - full-bg (1080x1350) `MAGq6DpUVaU`
  - 627x143, role: logo (Cerkl x Broadcast lockup), current asset_id: `MAFvNRVZhsQ`
  - 1036x657, role: photo-slot (large product UI hero), current asset_id: `MAGq6YLVt50` — layered
  - 230x220, role: decorative (sparkle icon), current asset_id: `MAGq0aWoUGM`
  - 87x87, role: icon (small badge), current asset_id: `MAGq6BXXtU0`
- text slots (page 2):
  - "No more missed invites. Deliver meetings right to employee calendars." — headline (807x266)
  - CTA pill SHAPE
- image slots (page 2):
  - full-bg `MAGq6O9Uo3Y`
  - 928x618, role: photo-slot (product UI screenshot), current asset_id: `MAGq6ODLqHc` — layered
  - 200x200, role: decorative (Athos brand circle), current asset_id: `MAGAiOQqcE0`
  - 164x164, role: decorative (sparkle badge), current asset_id: `MAF8ni2huLk`
  - 158x158, role: decorative (sparkle badge), current asset_id: `MAGq5hpDvvI`
  - 293x100, role: photo-slot (CTA pill image, "Send Invite" button), current asset_id: `MAGq58HuBhA`
- text slots (page 3):
  - "Send invites from key leaders to give the your events visibility and importance." — body (887x356)
  - CTA pill SHAPE
- image slots (page 3): full-bg `MAGq6Dg5iXg`; 913x608 product UI `MAGq6FfWs7E` (layered); 293x100 Send Invite pill `MAGq58HuBhA`
- text slots (page 4): "Include all relevant info—who, what, when, where—directly in the calendar item." (807x356)
- image slots (page 4): full-bg `MAGq6MfxffA`; 972x648 product UI `MAGq6BW1-DQ` (layered); Send Invite pill
- text slots (page 5): "Update or cancel events, swap attendees, and keep calendars accurate—without starting over." (887x356)
- image slots (page 5): full-bg `MAGq6HWmP5E`; 913x608 product UI `MAGq7N0NuQY` (layered); Send Invite pill
- text slots (page 6):
  - "Boost event turnout and cut the noise. \n\n Get critical meetings on the calendars of employees who need them—automatically." — closing headline (878x699)
  - "Learn more at Cerkl.com" — CTA pill SHAPE
- image slots (page 6): full-bg `MAGq6DpUVaU`; 615x615 decorative compass badge `MAGq6IEEnQQ`
- notes: 6-page Broadcast feature product carousel ("Calendar Invites"). Each content page has a large layered product UI screenshot (913-1036px wide) — these are the primary feature swap targets. Pages 2 reuses Athos brand badge + 2 sparkle decoratives. "Send Invite" button image (`MAGq58HuBhA`, 293x100) appears on pages 2-5 as a stylized CTA element layered over the UI. Outro is large gradient bg + compass mark.
---

## Shorts interview question template — `EAGqLE7tM_8`
- use_case: shorts-interview-question
- canvas: 1080x1920
- pages: 3 (page 1 is_empty=true)
- inspection design_id: `DAHLW5KMqnE`
- text slots (page 1): none (empty placeholder slide)
- image slots (page 1): none
- text slots (page 2):
  - "Question" — question text (943x75) inside top banner SHAPE
  - "Name" — speaker name (353x77, bottom-left card)
  - "Title" — speaker title (469x46, bottom-left card)
- image slots (page 2):
  - 251x140, role: logo (Cerkl wordmark top-right), current asset_id: `MAFYswpMFus`
- text slots (page 3): none
- image slots (page 3):
  - full-bg (1080x1920) `MAFn5Wxw57k`
  - 622x313, role: photo-slot (decorative bar/lockup), current asset_id: `MAFn5OsB4OY` — layered
- notes: 9:16 vertical Shorts template — VERY minimal. Page 1 is intentionally empty (for video footage overlay). Page 2 is the question card overlay (title bar + speaker name/title). Page 3 is an end-card with bg + a decorative content card. Designed to overlay short-form video; most "image" content comes from video footage layered behind. Layered-frame: yes for p3 (the 622x313 card sits atop bg).
---

## Shorts endcard template - Broadcast — `EAGqLEInYAk`
- use_case: shorts-endcard-broadcast
- canvas: 1080x1920
- pages: 1
- inspection design_id: `DAHLW4FVR_s`
- text slots (page 1): none
- image slots (page 1):
  - full-bg (1080x1920) `MAFn5Wxw57k` (Broadcast blue)
  - 864x319, role: logo (Broadcast lockup centered), current asset_id: `MAFYs2RusE8`
- notes: Brand-only end-card. No text — just centered Broadcast logo on blue bg. Both fills editable (rare). For shorts video end frame.
---

## Shorts thumbnail template — `EAGqLGG2TYI`
- use_case: shorts-thumbnail
- canvas: 1080x1920
- pages: 1
- inspection design_id: `DAHLW382yhk`
- text slots (page 1):
  - "Lorem ipsum dolor sit amet consectetur adipiscing elit" — large title (655x474, stacked in 4 white text bars)
  - Plus 4 white-strip SHAPEs + a vertical accent bar SHAPE — these are the highlighter banners behind the title text
- image slots (page 1):
  - full-bg (1139x1962, slightly oversized) `MAD4Qd-CYbs` (non-editable — the illustrated landscape)
  - 251x140, role: logo (Cerkl wordmark top-right), current asset_id: `MAFYswpMFus`
- notes: Shorts thumbnail — designed for vertical video preview. Background image is non-editable (locked landscape). Title fills 4 striped white text-banners. Only the logo and title text are user-customizable per slide.
---

## Shorts endcard template - HWSB — `EAGqLHnssQU`
- use_case: shorts-endcard-hwsb
- canvas: 1080x1920
- pages: 1
- inspection design_id: `DAHLW7LJ4ec`
- text slots (page 1): none
- image slots (page 1):
  - full-bg (1080x1920) `MAFn5Wxw57k`
  - 622x313, role: logo (Cerkl How Work Should Be lockup), current asset_id: `MAFn5OsB4OY`
- notes: HWSB-branded variant of EAGqLEInYAk. Same structure (bg + centered lockup), but uses Cerkl HWSB lockup instead of Broadcast.
---

## Facebook_Linkedin post_Webinar — `EAGqLE12g5c`
- use_case: webinar-linkedin-share-generic
- canvas: 1200x628
- pages: 3
- inspection design_id: `DAHLW26qXO0`
- text slots (page 1):
  - "live webinar" pill SHAPE
  - "Date and Time" / "Webinar title" / "Register now" CTA
  - "Hosted by:" + "INsert logo(s)" labels
  - 2x "Name" + "Title" speaker name/title pairs
  - Right-side speaker block SHAPE (430x628)
- image slots (page 1): full-bg `MAGRO9eVcvc` (1200x628)
- text slots (page 2): same with 3 speakers
- image slots (page 2): full-bg `MAGRO9eVcvc`
- text slots (page 3): same with 4 speakers
- image slots (page 3): full-bg `MAGRO9eVcvc`
- notes: Landscape 1200x628 webinar share card. 2/3/4 speaker variants. NO editable headshot fills — speaker headshots visible in render are baked into bg or rendered via SHAPE placeholders. Only 1 image fill per page (the bg). Logo placeholder is text "INsert logo(s)" not an image fill.
---

## 1200x628 post_Thought Leadership_Webinar Series — `EAGqLHFNucs`
- use_case: webinar-share-card-1200x628
- canvas: 1200x628
- pages: 3
- inspection design_id: `DAHLW1yESRI`
- text slots (page 1):
  - "Webinar" | "Mar 6, 2025 1:00 pm est" — date/time header
  - "Webinar title" — main headline (575x62)
  - "Register now" — CTA pill SHAPE + text
  - "Presented by:" label + Cerkl logo bg SHAPE
  - 2x "Name" / "Title" speaker pairs
- image slots (page 1):
  - full-bg (1200x628) `MAGg-3XLg1s`
  - 64x23, role: logo (Cerkl wordmark), current asset_id: `MAFYswpMFus`
  - 164x164, role: decorative-badge (IC Thought Leadership), current asset_id: `MAGg-9y8TiY`
  - 22x22, role: icon (play icon next to "Webinar"), current asset_id: `MAGg--nIQbc`
- text slots (page 2): same with 3 Name/Title pairs
- image slots (page 2): same as page 1 (full-bg + Cerkl + IC badge + play icon)
- text slots (page 3): same with 4 Name/Title pairs
- image slots (page 3): same image set
- notes: 1200x628 landscape variant of the IC Thought Leadership webinar series. Like EAGqLMN8_Po (square version) but headshots are NOT separate image fills here — they're rendered through bg or SHAPE placeholders. The only editable images per page are: full-bg, small Cerkl wordmark, big IC badge, small play icon. 2/3/4 speaker variants.
---

## Copy of Facebook_Linkedin post_style 1 — `EAGqLBc3p_w`
- use_case: linkedin-share-card-1200x628
- canvas: 1200x628
- pages: 1
- inspection design_id: `DAHLW3y0tD0`
- text slots (page 1):
  - "Lorem ipsum dolor sit amet" — headline (580x155)
  - "Sed diam nonummy nigh euismod tincunt ut laoreet dolore magna" — body (580x82)
  - "DELETE place image or graphic here" — image-placeholder instruction text
- image slots (page 1):
  - full-bg `MAFZLn9aDBo`
  - 450x296, role: photo-slot (round image placeholder, right side), current asset_id: `MAFZLpnoBN4` — layered
  - 336x129, role: logo (Broadcast lockup top-left), current asset_id: `MAFYs9rAVro`
- notes: Light style-1 share card with right-side circular image well. Image slot is editable + placeholder text instructs "DELETE place image or graphic here".
---

## Copy of Facebook_Linkedin post_style 2 — `EAGqLM0FChA`
- use_case: linkedin-share-card-1200x628
- canvas: 1200x628
- pages: 1
- inspection design_id: `DAHLW0CfKBw`
- text slots: "Euismod tincidunt ut laoreet dolore magna aliqua ut enim ad" headline (640x216) + "Read the report" CTA pill SHAPE + "DELETE place image or graphic here" placeholder
- image slots: full-bg `MAFZLuV3fY4`; 299x115 Broadcast lockup `MAFYs2RusE8`; 414x414 round image well `MAFZLycTv8I` (layered)
- notes: Dark-mode style-2 variant. Same skeleton as EAGqLBc3p_w but darker bg and right-side circular icon-image well. Image slot is editable.
---

## 1200 x 628px_Employee spotlight 2 — `EAGqLJg1OSY`
- use_case: linkedin-employee-spotlight-1200x628
- canvas: 1200x628
- pages: 1
- inspection design_id: `DAHLW371Pkg`
- text slots: "Employee Spotlight" headline (752x90) + quote (623x133) + "Firstname Lastname, Position Title" attribution
- image slots: full-bg `MAE_8ueKZRw` only
- notes: Headshot visible in render (round image left of quote) is baked into bg fill — NOT a separate image element. Cerkl HWSB logo also part of bg. Only 1 editable image fill (the full-bg). Lightweight share card.
---

## Facebook_Linkedin post_style 4 — `EAGqLFFIvPs`
- use_case: linkedin-share-card-1200x628
- canvas: 1200x628
- pages: 1
- inspection design_id: `DAHLW8y77-U`
- text slots: testimonial quote (1074x216) + "Firstname Lastname" + "Company / Position" + "DELETE place image or graphic here" placeholder
- image slots: full-bg `MAFZLhIFSzQ`; 299x115 Broadcast lockup `MAFYs2RusE8` (bottom-right); 450x296 decorative gradient corner `MAFZLjrDtjk` (top-right, layered)
- notes: Dark testimonial card. Round headshot well (small, bottom-left) is SHAPE placeholder with image-placeholder text — no editable headshot fill. Only 3 image elements (bg + Broadcast lockup + decorative gradient).
---

## Copy of Facebook_Linkedin post_style 4 — `EAGqLCaRTeM`
- use_case: linkedin-share-card-1200x628
- canvas: 1200x628
- pages: 1
- inspection design_id: `DAHLW8GZUkY`
- text slots: same as EAGqLFFIvPs (testimonial quote + name + position + placeholder)
- image slots: full-bg `MAFZLhIFSzQ`; Broadcast lockup `MAFYs2RusE8`; decorative gradient `MAFZLjrDtjk`
- notes: IDENTICAL skeleton to EAGqLFFIvPs ("Facebook_Linkedin post_style 4") — same fills, same text slots. Treat as duplicate-of-record alongside EAGqLFFIvPs.
---

## Facebook_Linkedin post_style 5 — `EAGqLBhKYtg`
- use_case: linkedin-share-card-1200x628
- canvas: 1200x628
- pages: 1
- inspection design_id: `DAHLW8tfChk`
- text slots: "Euismod tincidunt ut laoreet dolore" headline (600x155) + "Lorem ipsum dolor..." body (600x143) + "DELETE place image or graphic here" placeholder
- image slots: full-bg `MAFZLtGE-Mo`; 50x50 Broadcast compass mark bottom-right `MAFZLu2JowY`
- notes: Right-side circular image well visible in render is a SHAPE (not editable image fill). Image slot needs to be added/swapped manually. Only 2 editable images.
---

## Facebook_Linkedin post_style 3 — `EAGqLFOg67s`
- use_case: linkedin-share-card-1200x628
- canvas: 1200x628
- pages: 1
- inspection design_id: `DAHLW3VFy5Y`
- text slots: "XX%" stat (280x153) + "Sed diam nonummy nigh euismod tincunt..." statement (580x132) + "DELETE place image or graphic here" placeholder
- image slots: full-bg `MAFZLu4Qj98`; 50x50 Broadcast compass `MAFZLu2JowY`
- notes: Stat-card variant for 1200x628. Left-side circular image well is SHAPE only (no editable fill).
---

## Facebook_Linkedin post_style 5 (dup ID) — `EAGqLPtHbaY`
- use_case: linkedin-share-card-1200x628
- canvas: 1200x628
- pages: 1
- inspection design_id: `DAHLWz8yJUc`
- text slots: same as EAGqLBhKYtg (headline + body + placeholder)
- image slots: full-bg `MAFZLtGE-Mo`; 50x50 compass mark `MAFZLu2JowY`
- notes: IDENTICAL skeleton to EAGqLBhKYtg. Duplicate-of-record.
---

## Facebook_Linkedin post_style 4 (dup ID) — `EAGqLPtZFC0`
- use_case: linkedin-share-card-1200x628
- canvas: 1200x628
- pages: 1
- inspection design_id: `DAHLWwuimXc`
- text slots: same as EAGqLFFIvPs
- image slots: full-bg `MAFZLhIFSzQ`; Broadcast lockup `MAFYs2RusE8`; decorative gradient `MAFZLjrDtjk`
- notes: IDENTICAL skeleton to EAGqLFFIvPs / EAGqLCaRTeM. Third duplicate of the style-4 testimonial card.
---

## Facebook_Linkedin post_style 2 — `EAGqLHXIMi0`
- use_case: linkedin-share-card-1200x628
- canvas: 1200x628
- pages: 1
- inspection design_id: `DAHLWzwomTk`
- text slots: "Euismod tincidunt..." headline + "Read the report" CTA + placeholder
- image slots: full-bg `MAFZLuV3fY4`; Broadcast lockup `MAFYs2RusE8`; 414x414 round image well `MAFZLycTv8I` (layered, editable)
- notes: IDENTICAL to EAGqLM0FChA ("Copy of style 2"). The image well IS editable here (vs the placeholder-text-only wells in styles 3/5). Authoritative version of style 2.
---

## 1200 x 628px_Employee spotlight — `EAGqLLf6OBk`
- use_case: linkedin-employee-spotlight-1200x628
- canvas: 1200x628
- pages: 1
- inspection design_id: `DAHLW49ol6Y`
- text slots: "Employee Spotlight" headline (468x207) + quote (480x199) + "Firstname lastname" + "Position Title"
- image slots: full-bg `MAE_8rsI_C4`; 100x100 round headshot frame `MABw6X6WEUY` (NON-editable, layered)
- notes: Dark-mode variant of EAGqLJg1OSY. Headshot frame is a separate image fill (vs baked into bg in v2) but is editable=false, matching the headshot-frame pattern in EAGqLEqOaM4 / EAGqLOWcIHY. Swap likely requires workaround.
---

## Facebook_Linkedin post_style 3 (dup ID) — `EAGqLE_tvTw`
- use_case: linkedin-share-card-1200x628
- canvas: 1200x628
- pages: 1
- inspection design_id: `DAHLWxihqJc`
- text slots: "XX%" stat + statement + placeholder (same as EAGqLFOg67s)
- image slots: full-bg `MAFZLu4Qj98`; 50x50 compass `MAFZLu2JowY`
- notes: IDENTICAL to EAGqLFOg67s. Duplicate-of-record style-3 stat card.
---

## Facebook_Linkedin post_style 6 — `EAGqLPO8k5c`
- use_case: linkedin-share-card-1200x628
- canvas: 1200x628
- pages: 1
- inspection design_id: `DAHLW3ejVrk`
- text slots: "Euismod tincidunt ut laoreet dolore" headline + "Lorem ipsum..." body + "DELETE place image or graphic here" placeholder
- image slots: full-bg `MAFZL5pLExM`; 336x129 Broadcast lockup bottom-left `MAFYs9rAVro`
- notes: Light-mode share card with right-side large image placeholder (no editable fill — SHAPE only). Only 2 editable images. Sister to EAGqLBhKYtg but with light bg + Broadcast lockup.
---

## Facebook_Linkedin post_style 1 — `EAGqLAh0VTQ`
- use_case: linkedin-share-card-1200x628
- canvas: 1200x628
- pages: 1
- inspection design_id: `DAHLW2ZwJ4A`
- text slots: "Lorem ipsum dolor sit amet" headline + body + placeholder
- image slots: full-bg `MAFZLn9aDBo`; 450x296 round image well `MAFZLpnoBN4` (editable, layered); 336x129 Broadcast lockup `MAFYs9rAVro`
- notes: IDENTICAL to EAGqLBc3p_w ("Copy of style 1"). Authoritative style-1 share card with editable right-side circular image well. The series of `EAGqL...` 1200x628 templates includes 4 styles (1,2,3,5/6) with light + dark variants and 3 explicit duplicates.
---

