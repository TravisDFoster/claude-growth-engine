# /// script
# requires-python = ">=3.10"
# dependencies = ["requests", "beautifulsoup4", "markdownify", "lxml"]
# ///
"""
Scrape Cerkl helpdesk articles listed in cache/collections.json.

Writes each article as markdown to cache/helpdesk/<collection-slug>/<article-id>.md
with YAML-ish frontmatter (title, url, lastmod). Idempotent: skips files whose
lastmod matches the recorded value. Pass --refresh to force re-fetch.

Run:  uv run 02_scrape.py [--refresh]
"""
import json
import re
import sys
import time
from pathlib import Path

import requests
from bs4 import BeautifulSoup
from markdownify import markdownify

FEATURES_DIR = Path(__file__).resolve().parent.parent
CACHE = FEATURES_DIR / "cache"
HELPDESK = CACHE / "helpdesk"
HELPDESK.mkdir(parents=True, exist_ok=True)

# Intercom article body selectors, tried in order.
BODY_SELECTORS = [
    ".article__content",
    ".jsx-article-body",
    "article",
    "main",
]

S = requests.Session()
S.headers["User-Agent"] = "cerkl-helpdesk-sync/1.0 (+internal)"


def article_id_from_url(url: str) -> str:
    # https://help.cerkl.com/en/articles/5189371-how-classic-news-digest-... → 5189371-how-classic-news-digest-...
    m = re.search(r"/articles/([^/?#]+)", url)
    if not m:
        raise ValueError(f"can't extract article id from {url}")
    return m.group(1)


def read_existing_lastmod(path: Path) -> str:
    if not path.exists():
        return ""
    head = path.read_text(errors="ignore").splitlines()[:10]
    for line in head:
        if line.startswith("lastmod:"):
            return line.split(":", 1)[1].strip()
    return ""


def fetch_article_body(url: str) -> tuple[str, str]:
    """Return (title, markdown_body)."""
    r = S.get(url, timeout=30)
    r.raise_for_status()
    soup = BeautifulSoup(r.text, "html.parser")
    title = ""
    h1 = soup.find("h1")
    if h1:
        title = h1.get_text(strip=True)
    if not title and soup.title:
        title = soup.title.get_text(strip=True)

    body_html = None
    for sel in BODY_SELECTORS:
        node = soup.select_one(sel)
        if node:
            body_html = str(node)
            break
    if body_html is None:
        body_html = str(soup.body or soup)

    md = markdownify(body_html, heading_style="ATX", strip=["script", "style"])
    # collapse 3+ blank lines
    md = re.sub(r"\n{3,}", "\n\n", md).strip()
    return title, md


def main(argv: list[str]) -> int:
    refresh = "--refresh" in argv
    cmap = json.loads((CACHE / "collections.json").read_text())

    fetched = skipped = errored = 0
    for slug, info in cmap.items():
        coll_dir = HELPDESK / slug
        coll_dir.mkdir(exist_ok=True)
        for art in info["articles"]:
            aid = article_id_from_url(art["url"])
            out = coll_dir / f"{aid}.md"
            recorded = read_existing_lastmod(out)
            if not refresh and out.exists() and recorded == art.get("lastmod", ""):
                skipped += 1
                continue
            try:
                title, body = fetch_article_body(art["url"])
            except Exception as e:
                print(f"  ERROR {art['url']}: {e}", file=sys.stderr)
                errored += 1
                continue
            frontmatter = (
                "---\n"
                f"title: {title or art['title']}\n"
                f"url: {art['url']}\n"
                f"collection: {slug}\n"
                f"lastmod: {art.get('lastmod','')}\n"
                "---\n\n"
            )
            out.write_text(frontmatter + body)
            fetched += 1
            print(f"  {slug}/{aid}")
            time.sleep(0.25)  # gentle pacing

    print()
    print(f"fetched: {fetched}   skipped (cached): {skipped}   errored: {errored}")
    return 0 if errored == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
