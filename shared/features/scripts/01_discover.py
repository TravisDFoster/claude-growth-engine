# /// script
# requires-python = ">=3.10"
# dependencies = ["requests", "beautifulsoup4", "lxml"]
# ///
"""
Discover Cerkl helpdesk articles, grouped by Intercom collection.

Writes cache/collections.json with one entry per in-scope collection.
The taxonomy decision (collection -> feature doc) happens *later*,
after a planner subagent reviews the cached content. This script
intentionally takes no opinion on feature buckets.

Run:  uv run 01_discover.py
"""
import json
import sys
from pathlib import Path
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup

BASE = "https://help.cerkl.com"
FEATURES_DIR = Path(__file__).resolve().parent.parent
CACHE = FEATURES_DIR / "cache"
CACHE.mkdir(exist_ok=True)

# In-scope collections (product features only).
# Skipped per scope: Getting Started, Configuring Your Settings, Socialization & Change Management.
COLLECTIONS = [
    ("2479636", "content",                                 "Content"),
    ("7261302", "personalized-news-digests-welcome-email", "Personalized News Digests and Welcome Email"),
    ("2479651", "blasts",                                  "Blasts"),
    ("2479644", "audience",                                "Audience"),
    ("2479660", "insights",                                "Insights"),
    ("5822927", "images-image-gallery",                    "Images & Image Gallery"),
    ("2479682", "mobile",                                  "Utilizing Broadcast Mobile"),
    ("4597224", "slack",                                   "Utilizing Slack"),
    ("2994190", "teams",                                   "Utilizing Teams"),
    ("2479655", "intranet",                                "Personalizing Your Intranet"),
]

S = requests.Session()
S.headers["User-Agent"] = "cerkl-helpdesk-sync/1.0 (+internal)"


def fetch_sitemap_lastmods() -> dict[str, str]:
    r = S.get(f"{BASE}/sitemap.xml", timeout=30)
    r.raise_for_status()
    soup = BeautifulSoup(r.text, "xml")
    out: dict[str, str] = {}
    for url in soup.find_all("url"):
        loc = url.find("loc")
        if not loc:
            continue
        href = loc.get_text(strip=True).replace("http://", "https://")
        lm = url.find("lastmod")
        out[href] = lm.get_text(strip=True) if lm else ""
    return out


def fetch_collection_articles(collection_id: str) -> list[dict]:
    url = f"{BASE}/en/collections/{collection_id}"
    r = S.get(url, timeout=30)
    r.raise_for_status()
    soup = BeautifulSoup(r.text, "html.parser")
    seen, out = set(), []
    for a in soup.select("a[href*='/articles/']"):
        href = urljoin(BASE, a["href"])
        href = href.split("#", 1)[0].split("?", 1)[0].replace("http://", "https://")
        if href in seen:
            continue
        title = a.get_text(strip=True)
        if not title:
            continue
        seen.add(href)
        out.append({"url": href, "title": title})
    return out


def main() -> int:
    print("fetching sitemap…")
    lastmods = fetch_sitemap_lastmods()
    print(f"  {len(lastmods)} sitemap entries")

    result = {}
    total = 0
    for cid, slug, name in COLLECTIONS:
        print(f"fetching {slug}…")
        try:
            arts = fetch_collection_articles(cid)
        except requests.HTTPError as e:
            print(f"  WARN: {e}", file=sys.stderr)
            arts = []
        for a in arts:
            a["lastmod"] = lastmods.get(a["url"], "")
        arts.sort(key=lambda x: x["title"].lower())
        result[slug] = {
            "id": cid,
            "name": name,
            "url": f"{BASE}/en/collections/{cid}",
            "articles": arts,
        }
        total += len(arts)

    out_path = CACHE / "collections.json"
    out_path.write_text(json.dumps(result, indent=2, sort_keys=False))

    print()
    print(f"wrote {out_path.relative_to(FEATURES_DIR.parent.parent)}")
    print(f"unique articles across in-scope collections: {total}")
    for slug, c in result.items():
        print(f"  {slug:<40} {len(c['articles']):>3}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
