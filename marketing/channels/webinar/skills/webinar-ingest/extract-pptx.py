#!/usr/bin/env python3
"""
Extract slide text, speaker notes, and image manifest from a .pptx file.

Output: structured Markdown block ready to seed `<speaker-slug>-deck-extract.md`.

Usage:
    python3 extract-pptx.py <path-to-pptx>

Used by the `webinar-ingest` skill. See SKILL.md for context.
"""

import os
import re
import sys
import shutil
import tempfile
import zipfile
import xml.etree.ElementTree as ET

NS_A = "{http://schemas.openxmlformats.org/drawingml/2006/main}"


def slide_num(filename: str) -> int:
    m = re.search(r"(\d+)", filename)
    return int(m.group(1)) if m else 999


def extract_text(xml_path: str) -> list[str]:
    """Pull every <a:t> text run from a slide or notes XML file."""
    try:
        tree = ET.parse(xml_path)
    except (ET.ParseError, FileNotFoundError):
        return []
    return [t.text for t in tree.getroot().iter(f"{NS_A}t") if t.text]


def extract_image_refs(rels_path: str) -> list[str]:
    """Pull image filenames referenced from a slide's _rels file."""
    if not os.path.exists(rels_path):
        return []
    with open(rels_path) as f:
        content = f.read()
    return re.findall(r'Target="\.\./media/(image\d+\.[a-z]+)"', content)


def main(pptx_path: str) -> None:
    if not os.path.exists(pptx_path):
        sys.exit(f"File not found: {pptx_path}")

    workdir = tempfile.mkdtemp(prefix="pptx-extract-")
    try:
        with zipfile.ZipFile(pptx_path) as zf:
            zf.extractall(workdir)

        slides_dir = os.path.join(workdir, "ppt", "slides")
        notes_dir = os.path.join(workdir, "ppt", "notesSlides")
        media_dir = os.path.join(workdir, "ppt", "media")

        slide_files = sorted(
            (f for f in os.listdir(slides_dir) if re.match(r"slide\d+\.xml$", f)),
            key=slide_num,
        )
        total_slides = len(slide_files)
        total_images = (
            len([f for f in os.listdir(media_dir) if not f.startswith(".")])
            if os.path.isdir(media_dir)
            else 0
        )

        deck_name = os.path.basename(pptx_path)
        print(f"# Deck Extract — {deck_name}")
        print()
        print(f"- **Slides:** {total_slides}")
        print(f"- **Total images embedded:** {total_images}")
        print(f"- **Source file:** `{pptx_path}`")
        print()
        print("---")
        print()

        for slide_file in slide_files:
            n = slide_num(slide_file)

            slide_path = os.path.join(slides_dir, slide_file)
            notes_path = os.path.join(notes_dir, f"notesSlide{n}.xml")
            rels_path = os.path.join(slides_dir, "_rels", f"{slide_file}.rels")

            slide_texts = extract_text(slide_path)
            note_texts = [
                t
                for t in extract_text(notes_path)
                if t.strip() and not t.strip().isdigit() and len(t.strip()) > 3
            ]
            images = extract_image_refs(rels_path)

            print(f"## Slide {n}")
            print()
            if slide_texts:
                print("**Text:**")
                print()
                for t in slide_texts:
                    cleaned = t.strip()
                    if cleaned:
                        print(f"- {cleaned}")
                print()
            else:
                print("**Text:** *(no extractable text — likely image-only)*")
                print()

            if note_texts:
                print("**Speaker notes:**")
                print()
                for t in note_texts:
                    print(f"> {t.strip()}")
                print()

            if images:
                print(f"**Images:** {', '.join(images)}")
            else:
                print("**Images:** *(none)*")
            print()
            print("**Transcript:** _<fill in `~MM:SS–MM:SS` after reconciliation>_")
            print()
            print("---")
            print()

    finally:
        shutil.rmtree(workdir, ignore_errors=True)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("Usage: extract-pptx.py <path-to-pptx>")
    main(sys.argv[1])
