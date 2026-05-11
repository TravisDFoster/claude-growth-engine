#!/usr/bin/env python3
"""RSS/Atom feed fetcher for cc-trends daily recap.

Reads feeds.json (curated feed list), fetches each, parses RSS or Atom,
filters to the last N days, returns flat JSON list of items.

Usage:
  python3 lib/feed_fetch.py [--days 7] [--per-feed 8] [--top 30]
  python3 lib/feed_fetch.py --feeds https://simonwillison.net/atom/everything/

Stdlib only — no python-dotenv, no feedparser.
"""

import argparse
import json
import re
import ssl
import sys
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta, timezone
from email.utils import parsedate_to_datetime
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

HERE = Path(__file__).resolve().parent
CCROOT = HERE.parent
ATOM_NS = "{http://www.w3.org/2005/Atom}"


def _build_ssl_context() -> ssl.SSLContext:
    for cafile in ("/etc/ssl/cert.pem", "/opt/homebrew/etc/ca-certificates/cert.pem"):
        if Path(cafile).exists():
            return ssl.create_default_context(cafile=cafile)
    return ssl.create_default_context()


SSL_CONTEXT = _build_ssl_context()


def fetch(url: str, timeout: int = 20) -> bytes:
    req = Request(url, headers={
        "User-Agent": "cc-trends-feed-fetch/1.0 (+research)",
        "Accept": "application/rss+xml, application/atom+xml, application/xml, text/xml, */*",
    })
    with urlopen(req, timeout=timeout, context=SSL_CONTEXT) as r:
        return r.read()


def parse_date(s: str | None) -> datetime | None:
    if not s:
        return None
    s = s.strip()
    # Try RFC 822 (RSS pubDate)
    try:
        dt = parsedate_to_datetime(s)
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=timezone.utc)
        return dt
    except (TypeError, ValueError):
        pass
    # Try ISO 8601 (Atom published/updated)
    try:
        return datetime.fromisoformat(s.replace("Z", "+00:00"))
    except ValueError:
        return None


_TAG_RE = re.compile(r"<[^>]+>")


def strip_html(s: str | None, limit: int = 280) -> str:
    if not s:
        return ""
    text = _TAG_RE.sub("", s)
    text = re.sub(r"\s+", " ", text).strip()
    return text[:limit]


def parse_feed(xml_bytes: bytes, feed_url: str, feed_name: str) -> list[dict]:
    try:
        root = ET.fromstring(xml_bytes)
    except ET.ParseError as e:
        return [{"_parse_error": f"{feed_url}: {e}"}]

    items: list[dict] = []
    tag = root.tag.lower()

    if tag.endswith("rss") or tag == "rss":
        # RSS 2.0
        for item in root.iter("item"):
            title = (item.findtext("title") or "").strip()
            link = (item.findtext("link") or "").strip()
            pub = item.findtext("pubDate")
            desc = item.findtext("description") or ""
            items.append({
                "title": title,
                "url": link,
                "published_at_raw": pub,
                "summary": strip_html(desc),
                "feed": feed_name,
                "feed_url": feed_url,
            })
    else:
        # Atom (or namespaced root)
        for entry in root.iter(f"{ATOM_NS}entry"):
            title = (entry.findtext(f"{ATOM_NS}title") or "").strip()
            link_el = entry.find(f"{ATOM_NS}link")
            link = link_el.get("href") if link_el is not None else ""
            pub = entry.findtext(f"{ATOM_NS}published") or entry.findtext(f"{ATOM_NS}updated")
            summary = entry.findtext(f"{ATOM_NS}summary") or entry.findtext(f"{ATOM_NS}content") or ""
            items.append({
                "title": title,
                "url": link,
                "published_at_raw": pub,
                "summary": strip_html(summary),
                "feed": feed_name,
                "feed_url": feed_url,
            })
        # Also handle namespaceless RSS-in-Atom edge cases
        if not items:
            for item in root.iter("item"):
                title = (item.findtext("title") or "").strip()
                link = (item.findtext("link") or "").strip()
                pub = item.findtext("pubDate")
                desc = item.findtext("description") or ""
                items.append({
                    "title": title,
                    "url": link,
                    "published_at_raw": pub,
                    "summary": strip_html(desc),
                    "feed": feed_name,
                    "feed_url": feed_url,
                })

    # Resolve dates to ISO
    for it in items:
        dt = parse_date(it.get("published_at_raw"))
        it["published_at"] = dt.astimezone(timezone.utc).isoformat() if dt else None
    return items


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--days", type=int, default=7)
    ap.add_argument("--per-feed", type=int, default=8, help="max items kept per feed (after date filter)")
    ap.add_argument("--top", type=int, default=30, help="cap total items returned")
    ap.add_argument("--feeds", nargs="*", help="explicit feed URLs (overrides feeds.json)")
    ap.add_argument("--feeds-file", default=str(CCROOT / "feeds.json"))
    args = ap.parse_args()

    feeds_to_fetch: list[dict] = []
    if args.feeds:
        feeds_to_fetch = [{"url": u, "name": u} for u in args.feeds]
    else:
        path = Path(args.feeds_file)
        if not path.exists():
            json.dump({"error": f"feeds file not found: {args.feeds_file}"}, sys.stdout)
            return 1
        cfg = json.loads(path.read_text())
        feeds_to_fetch = cfg.get("feeds", [])

    cutoff = datetime.now(timezone.utc) - timedelta(days=args.days)
    all_items: list[dict] = []
    errors: list[str] = []
    feeds_fetched: list[dict] = []

    for f in feeds_to_fetch:
        url = f.get("url")
        name = f.get("name") or url
        if not url:
            continue
        try:
            xml = fetch(url)
        except (HTTPError, URLError) as e:
            errors.append(f"{name}: fetch failed: {e}")
            continue

        parsed = parse_feed(xml, url, name)
        parse_errors = [p["_parse_error"] for p in parsed if "_parse_error" in p]
        errors.extend(parse_errors)
        items = [p for p in parsed if "_parse_error" not in p]

        in_window = []
        for it in items:
            if not it.get("published_at"):
                continue
            try:
                dt = datetime.fromisoformat(it["published_at"])
            except ValueError:
                continue
            if dt >= cutoff:
                in_window.append(it)

        in_window.sort(
            key=lambda x: x.get("published_at") or "",
            reverse=True,
        )
        feeds_fetched.append({
            "name": name,
            "url": url,
            "total_items": len(items),
            "in_window": len(in_window),
        })
        all_items.extend(in_window[: args.per_feed])

    all_items.sort(key=lambda x: x.get("published_at") or "", reverse=True)
    all_items = all_items[: args.top]

    json.dump({
        "items": all_items,
        "errors": errors,
        "feeds_fetched": feeds_fetched,
        "fetched_at": datetime.now(timezone.utc).isoformat(),
        "window_days": args.days,
    }, sys.stdout, indent=2, ensure_ascii=False)
    print()
    return 0


if __name__ == "__main__":
    sys.exit(main())
