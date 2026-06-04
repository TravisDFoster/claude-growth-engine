#!/usr/bin/env python3
"""Parse template-element-map.md into per-template JSON files.

Source of truth stays in the markdown. Re-run this anytime the markdown changes;
the skill reads only the JSON.

Input:  ../template-element-map.md (relative to this script's parent)
Output: ../_element-maps/<TEMPLATE_ID>.json
        ../_element-maps/index.json (id -> name + path + use_case)
"""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

SCRIPT_DIR = Path(__file__).resolve().parent
SKILL_DIR = SCRIPT_DIR.parent
CANVA_SKILLS_DIR = SKILL_DIR.parent
MARKDOWN = CANVA_SKILLS_DIR / "template-element-map.md"
OUT_DIR = SKILL_DIR / "_element-maps"

HEADER_RE = re.compile(r"^##\s+(?P<name>.+?)\s+—\s+`(?P<id>[A-Za-z0-9_-]+)`\s*$")
KV_RE = re.compile(r"^-\s+(?P<key>use_case|canvas|pages|inspection design_id|notes):\s*(?P<value>.*)$")
SECTION_RE = re.compile(r"^-\s+(?P<kind>text|image)\s+slots\s*\(page\s+(?P<page>\d+)\)\s*:\s*(?P<rest>.*)$")
ASSET_ID_RE = re.compile(r"`(M[A-Za-z0-9_-]{6,})`")
DIM_RE = re.compile(r"\b(\d{2,5})\s*[xX×]\s*(\d{2,5})\b")
ROLE_RE = re.compile(r"role:\s*([a-zA-Z-]+)")
LAYERED_RE = re.compile(r"layered\s+frame:\s*yes|layered\b", re.IGNORECASE)
EDITABLE_FALSE_RE = re.compile(r"editable\s*[:=]?\s*false|non-?editable|NON-?editable", re.IGNORECASE)
TEXT_QUOTE_RE = re.compile(r"^\s*[-•]?\s*\"([^\"]+)\"")
DELETE_HINT_RE = re.compile(r"DELETE\s+(?:place\s+image|if\s+unused|before\s+export)", re.IGNORECASE)


def split_compact_slots(rest: str) -> list[str]:
    """Compact image-slot lines look like:
       full-bg `MAGg-8Ldy8k`; play icon `MAGg-1Nbpjs` (32x32); IC badge `MAGg-9y8TiY` (296x296)
       Split on ';' but tolerate semicolons inside parentheses (rare).
    """
    pieces: list[str] = []
    depth = 0
    buf: list[str] = []
    for ch in rest:
        if ch == "(":
            depth += 1
        elif ch == ")":
            depth = max(0, depth - 1)
        if ch == ";" and depth == 0:
            piece = "".join(buf).strip()
            if piece:
                pieces.append(piece)
            buf = []
        else:
            buf.append(ch)
    tail = "".join(buf).strip()
    if tail:
        pieces.append(tail)
    return pieces


def parse_image_slot(raw: str) -> dict[str, Any]:
    """Best-effort structured extraction. Keep raw so the skill can fall back."""
    slot: dict[str, Any] = {"raw": raw.strip()}
    asset_match = ASSET_ID_RE.search(raw)
    if asset_match:
        slot["current_asset_id"] = asset_match.group(1)
    dim_match = DIM_RE.search(raw)
    if dim_match:
        slot["dimensions"] = f"{dim_match.group(1)}x{dim_match.group(2)}"
    role_match = ROLE_RE.search(raw)
    if role_match:
        slot["role"] = role_match.group(1)
    else:
        # Inference for compact lines that drop "role:" prefix.
        lowered = raw.lower()
        if "full-bg" in lowered or "full-page fill" in lowered or "full bg" in lowered:
            slot["role"] = "full-bg"
        elif "logo" in lowered or "wordmark" in lowered or "lockup" in lowered:
            slot["role"] = "logo"
        elif "headshot" in lowered:
            slot["role"] = "headshot"
        elif "icon" in lowered:
            slot["role"] = "icon"
        elif "badge" in lowered:
            slot["role"] = "decorative-badge"
        elif "decorative" in lowered:
            slot["role"] = "decorative"
        elif "photo-slot" in lowered or "photo slot" in lowered:
            slot["role"] = "photo-slot"
    if LAYERED_RE.search(raw):
        slot["layered"] = True
    if EDITABLE_FALSE_RE.search(raw):
        slot["editable"] = False
    return slot


def parse_text_slot(raw: str) -> dict[str, Any]:
    slot: dict[str, Any] = {"raw": raw.strip()}
    quote_match = TEXT_QUOTE_RE.search(raw)
    if quote_match:
        slot["placeholder"] = quote_match.group(1)
    if DELETE_HINT_RE.search(raw):
        slot["delete_hint"] = True
    # Anything after the em-dash is usually a role hint.
    if "—" in raw:
        slot["role_hint"] = raw.split("—", 1)[1].strip()
    elif "-" in raw and quote_match:
        tail = raw.split(quote_match.group(0), 1)[1].lstrip(" -—")
        if tail:
            slot["role_hint"] = tail.strip()
    return slot


def ensure_page(pages: dict[int, dict], n: int) -> dict:
    if n not in pages:
        pages[n] = {"page": n, "text_slots": [], "image_slots": []}
    return pages[n]


def parse_template_block(lines: list[str]) -> dict[str, Any] | None:
    if not lines:
        return None
    header = HEADER_RE.match(lines[0])
    if not header:
        return None
    out: dict[str, Any] = {
        "template_id": header.group("id"),
        "name": header.group("name").strip(),
        "pages": [],
    }
    pages: dict[int, dict] = {}
    notes_buf: list[str] = []
    in_notes = False
    current_section: tuple[str, int] | None = None  # ("text"|"image", page)

    for raw_line in lines[1:]:
        line = raw_line.rstrip()
        if not line.strip():
            in_notes = False
            current_section = None
            continue

        # Metadata bullets at indent 0 (single dash).
        kv = KV_RE.match(line)
        if kv:
            key = kv.group("key")
            value = kv.group("value").strip()
            if key == "notes":
                notes_buf = [value]
                in_notes = True
            else:
                in_notes = False
                if key == "pages":
                    try:
                        out["page_count"] = int(value.split()[0])
                    except ValueError:
                        out["page_count_raw"] = value
                elif key == "inspection design_id":
                    out["inspection_design_id"] = value.strip("`")
                else:
                    out[key] = value
                current_section = None
            continue

        sec = SECTION_RE.match(line)
        if sec:
            in_notes = False
            kind = sec.group("kind")
            page_n = int(sec.group("page"))
            ensure_page(pages, page_n)
            current_section = (kind, page_n)
            rest = sec.group("rest").strip()
            if rest:
                # Compact form — split inline.
                slots_list = (
                    pages[page_n]["image_slots"]
                    if kind == "image"
                    else pages[page_n]["text_slots"]
                )
                for piece in split_compact_slots(rest):
                    if kind == "image":
                        slots_list.append(parse_image_slot(piece))
                    else:
                        slots_list.append(parse_text_slot(piece))
            continue

        # Indented child bullet — belongs to the active section.
        if current_section and re.match(r"^\s{2,}-\s+", line):
            kind, page_n = current_section
            entry = line.strip().lstrip("- ").strip()
            target = (
                pages[page_n]["image_slots"]
                if kind == "image"
                else pages[page_n]["text_slots"]
            )
            if kind == "image":
                target.append(parse_image_slot(entry))
            else:
                target.append(parse_text_slot(entry))
            continue

        # Notes continuation.
        if in_notes:
            notes_buf.append(line.strip())
            continue

        # Fallthrough: ignore unrecognized line.

    if notes_buf:
        out["notes"] = " ".join(s.strip() for s in notes_buf if s.strip())

    out["pages"] = [pages[k] for k in sorted(pages)]
    return out


def main() -> None:
    text = MARKDOWN.read_text()
    # Split on '## ' at line start (after the first header line).
    chunks: list[list[str]] = []
    current: list[str] = []
    for line in text.splitlines():
        if line.startswith("## "):
            if current:
                chunks.append(current)
            current = [line]
        elif line.strip() == "---":
            if current:
                chunks.append(current)
                current = []
        else:
            if current:
                current.append(line)
    if current:
        chunks.append(current)

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    index: list[dict[str, str]] = []
    written = 0
    for chunk in chunks:
        parsed = parse_template_block(chunk)
        if not parsed:
            continue
        tid = parsed["template_id"]
        out_path = OUT_DIR / f"{tid}.json"
        out_path.write_text(json.dumps(parsed, indent=2) + "\n")
        index.append(
            {
                "template_id": tid,
                "name": parsed.get("name", ""),
                "use_case": parsed.get("use_case", ""),
                "page_count": parsed.get("page_count", 0),
                "path": f"_element-maps/{tid}.json",
            }
        )
        written += 1

    (OUT_DIR / "index.json").write_text(json.dumps(index, indent=2) + "\n")
    print(f"Wrote {written} template JSON files + index.json to {OUT_DIR}")


if __name__ == "__main__":
    main()
