# Design Folder Clean-up Plan

> **DO NOT TOUCH ANYTHING IN THIS LIST WITHOUT EXPLICIT APPROVAL FROM TRAVIS.**
> Every item below requires per-item sign-off before deletion, compression, or extraction. Do not bulk-execute. Do not mark "done" unless Travis confirms or has done it himself.

**Starting size:** 6.0 GB
**Target size after full clean-up:** ~1 GB
**Guiding principle:** preserve every modular component used for image construction (icons, lockups, photography hero shots, brand guidelines, design components). Cut Canva-native source files, oversized export artifacts, dated event photos, and duplicate copies.

---

## Status legend
- [ ] Pending approval
- [~] Approved, in progress
- [x] Done

---

## 1. Canva source files — strip from local (~2.5 GB)

Canva is the source of truth for these. The `.ai`/`.ait` files are exported masters that can be re-downloaded from Canva at any time and can't be opened well outside it. Replace with a `canva-assets.md` index listing each template name + Canva URL + thumbnail.

- [ ] `branding-assets/Canva Assets/Blog Posts/Ai File/2025 Blog Cover Overlays.ai` — 425 MB
- [ ] `branding-assets/Canva Assets/Blog Posts/Ai File/In text images_product graphics examples.ai` — 279 MB
- [ ] `branding-assets/Canva Assets/Blog Posts/Ai File/In text images_ data graphics examples.ai` — 230 MB
- [ ] `branding-assets/Canva Assets/Blog Posts/Ai File/Blog Post Cover Image Templates.ait` — 192 MB
- [ ] `branding-assets/Canva Assets/Blog Posts/Ai File/In text images_illustrated graphics examples.ai` — 49 MB
- [ ] `branding-assets/Canva Assets/Social Media/Ai File/Cerkl _ Broadcast Social Templates.ai` — 403 MB
- [ ] Build `branding-assets/Canva Assets/canva-assets.md` index (template name, Canva URL, purpose) before deletion

**Recoverable: ~1.6 GB**

---

## 2. Oversized LinkedIn PDF exports (~950 MB)

A LinkedIn PDF post should be < 5 MB. These are uncompressed Canva exports. Either re-export at LinkedIn spec or delete (LinkedIn doesn't keep the source after upload).

- [ ] `Canva Assets/Social Media/Assets/Mockup posts/Linkedin PDF/Cerkl _ Broadcast_ Linkedin PDF_list.pdf` — 323 MB
- [ ] `Canva Assets/Social Media/Assets/Mockup posts/Linkedin PDF/Cerkl _ Broadcast_ Linkedin PDF_product moudule feature.pdf` — 317 MB
- [ ] `Canva Assets/Social Media/Assets/Mockup posts/Linkedin PDF/Cerkl _ Broadcast_ Linkedin PDF_stats feature.pdf` — 315 MB
- [ ] `Canva Assets/Social Media/Assets/Mockup posts/Linkedin PDF/Employee Spotlight - Sam Huber_Linkedin.pdf` — 425 KB (keep or compress)

**Decision needed:** delete outright, or re-export compressed and keep as templates?

**Recoverable: ~950 MB**

---

## 3. Athos master illustration file (~1.1 GB)

- [ ] `branding-assets/Product Illustration/Athos Brand/ai file/athos_branding.ai` — 1.12 GB single .ai file

**Decision needed:** is this the canonical master for the Athos branding, or a working copy? If canonical, archive to Drive and replace with a stub `.md` pointing to the Drive location. If working copy, delete.

**Recoverable: ~1.1 GB**

---

## 4. Cerkl Photography — archive event photos to Drive (~1.7 GB)

Event photos aren't modular components — they're memory-keeping. Archive to Google Drive, keep ~10 hero shots locally per event, replace folder with `culture-photos.md` pointing to Drive.

- [x] `branding-assets/Cerkl Photography/Culture Photos/2021 Broadcast Bowl I/` — 1.4 GB (148 JPGs) — **deleted by Travis**
- [x] `branding-assets/Cerkl Photography/Culture Photos/2022 Broadcast Bowl II/` — 272 MB (83 JPGs) — **deleted by Travis**
- [ ] `branding-assets/Cerkl Photography/Culture Photos/Holiday/` — 12 MB (review, likely keep)
- [ ] `branding-assets/Cerkl Photography/Culture Photos/Other/` — 1.7 MB (review, likely keep)

**Keep as-is:**
- `Cerkl Photography/Office Photos/` — 155 MB (reusable backgrounds)
- `Cerkl Photography/Group Photos/` — 43 MB (reusable team shots)

**Recovered so far: ~1.7 GB ✓**

---

## 5. Brand Guidelines deck (~100 MB)

Content is already extracted into `Brand Guidelines/*.md` files. The PDF is a fine human-readable backup; the `.pptx` is redundant.

- [ ] `branding-assets/Brand Guidelines/Cerkl Brand Guidelines.pptx` — 102 MB **delete**
- [ ] `branding-assets/Brand Guidelines/Cerkl Brand Guidelines.pdf` — 3.5 MB **keep** (human-readable reference)

**Recoverable: ~100 MB**

---

## 6. Obvious duplicates and "(1)" copies

- [ ] `branding-assets/Typefaces/Google Doc Typeface Scale(1).docx` — duplicate of non-(1) version
- [ ] `branding-assets/Typefaces/Google Slide Typeface Scale(1).pptx` — duplicate of non-(1) version
- [ ] `branding-assets/Design Templates/Branded Collateral/Broadcast Branded Google Doc/Broadcast Branded Doc Template 2022.docx` — superseded by current version in same folder
- [ ] `branding-assets/Design Templates/Presentation Decks/TEMPLATE_ Cerkl Branded Deck 2022.pptx` — superseded by `2025 Cerkl Branded Deck/` folder
- [ ] `branding-assets/OLD TEMPLATE_ Cerkl Broadcast Branded Slide Deck 2020.pptx` — name says it all

**Recoverable: ~10 MB**

---

## 7. Already-flagged "old" folders (~30 MB)

Naming convention already marks these as deprecated.

- [ ] `branding-assets/Design Components/Old Assets/` — 14 MB
- [ ] `branding-assets/Product Illustration/Product Images/Mobile/Old/` — 9.8 MB
- [ ] `branding-assets/Social Assets/X_Old Assets/` — 4.2 MB
- [ ] `branding-assets/Product Illustration/Athos Brand/z_OLD_Athos Essentials/` — 1.3 MB
- [ ] `branding-assets/Social Assets/Video/Youtube/Old/` — 176 KB

**Recoverable: ~30 MB**

---

## 8. Slidedecks → markdown extraction

For an image-construction workflow, structured `.md` (sections, copy blocks, design notes) is more useful than the `.pptx`. Extract content, then archive original to Drive.

- [ ] `branding-assets/Cerkl/Decks/For Collaboration_ Cerkl Broadcast Overview.pptx` — 19 MB → `broadcast-overview.md`
- [ ] `branding-assets/Inner Cerkl/Templates/Cerkl Implementation & Launch Overview_ Cerkl for IC.pptx` — 17 MB → `ic-implementation-overview.md`
- [ ] `branding-assets/Inner Cerkl/Templates/MASTER_ Inner Cerkl Webinar Deck 2020.pptx` — 7 MB → `ic-webinar-template.md`
- [ ] `branding-assets/Inner Cerkl/Templates/Client Year In Review Template.pptx` — 8.8 MB → `client-yir-template.md`
- [ ] `branding-assets/Inner Cerkl/Templates/Template - Year In Review.pptx` — 6.7 MB → `yir-template.md`
- [ ] `branding-assets/Design Templates/Presentation Decks/CS Client Business Review/TEMPLATE_ Client Business Review.pptx` — 4.9 MB → `cbr-template.md`
- [ ] `branding-assets/Design Templates/Presentation Decks/InnerCerkl Webinar Deck Template.pptx` — 1.5 MB → consolidate with IC webinar template above

**Keep as-is** (active templates, current year):
- `Design Templates/Presentation Decks/2025 Cerkl Branded Deck/Cerkl Branded Deck 2025.pptx`
- `Design Templates/Presentation Decks/2025 Cerkl Branded Deck/2025 Team Meeting Deck Template.pptx`

**Recoverable: ~65 MB**

---

## Summary

| Section | Status | Size |
|---|---|---|
| 1. Canva sources | Pending | 1.6 GB |
| 2. LinkedIn PDFs | Pending | 950 MB |
| 3. Athos master | Pending | 1.1 GB |
| 4. Event photos | **Done (Bowl I & II)** | 1.7 GB ✓ |
| 5. Brand Guidelines .pptx | Pending | 100 MB |
| 6. Duplicates | Pending | 10 MB |
| 7. "Old" folders | Pending | 30 MB |
| 8. Deck → .md extraction | Pending | 65 MB |
| **Total recoverable** | | **~5.5 GB** |
| **Recovered to date** | | **~1.7 GB** |

---

## Workflow when ready to execute

1. Travis approves a specific section.
2. For deck-to-.md sections: extract content into the target `.md` first, Travis reviews the `.md`, then originals are archived/deleted.
3. For Drive-archive items: confirm Drive destination, upload, verify, then delete local.
4. Update this file: change `[ ]` → `[x]` with date.
5. Never bulk-process across sections without re-confirming.
