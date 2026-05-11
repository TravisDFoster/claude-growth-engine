#!/usr/bin/env python3
"""YouTube Data API v3 fetcher for cc-trends daily recap.

Outputs JSON list of trending videos:
- Discovery via search.list (queries) + curated channel allowlist (channels.json)
- Filters to last N days, sorts by view count
- Deduped across queries/channels

Usage:
  python3 lib/yt_search.py [--days 7] [--per-query 10] [--top 20]
  python3 lib/yt_search.py --queries "claude code" "MCP server"

Requires YOUTUBE_API_KEY in personal/.env (or environment).
"""

import argparse
import json
import os
import re
import ssl
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path
from urllib.parse import urlencode
from urllib.request import urlopen, Request
from urllib.error import HTTPError, URLError

API_BASE = "https://www.googleapis.com/youtube/v3"


def _build_ssl_context() -> ssl.SSLContext:
    """macOS system Python often has no default cert bundle. Try common locations."""
    for cafile in ("/etc/ssl/cert.pem", "/opt/homebrew/etc/ca-certificates/cert.pem"):
        if Path(cafile).exists():
            return ssl.create_default_context(cafile=cafile)
    return ssl.create_default_context()


SSL_CONTEXT = _build_ssl_context()

_DUR_RE = re.compile(r"PT(?:(\d+)H)?(?:(\d+)M)?(?:(\d+)S)?")


def parse_iso8601_duration(s: str) -> int:
    if not s:
        return 0
    m = _DUR_RE.fullmatch(s)
    if not m:
        return 0
    h, mi, se = m.groups()
    return int(h or 0) * 3600 + int(mi or 0) * 60 + int(se or 0)
HERE = Path(__file__).resolve().parent
CCROOT = HERE.parent
PERSONAL_ROOT = CCROOT.parent.parent

# Narrowed 2026-05-10: original broad queries ("employee engagement", "intranet platform")
# matched Mel Robbins / generic self-help / electronics "IC measurement" content. The new
# list is competitor-product- and conference-anchored so search results stay IC-relevant.
# Dropped "IC measurement" (matched integrated-circuit videos) and "Ragan conference"
# (matched Ragan Disney social-media conference, not Ragan Communications).
DEFAULT_QUERIES = [
    "Staffbase demo",
    "Simpplr review",
    "Workvivo vs Staffbase",
    "ContactMonkey demo",
    "internal communications strategy",
    "IABC conference",
]


def load_env_file(path: Path) -> None:
    if not path.exists():
        return
    for line in path.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, _, v = line.partition("=")
        k, v = k.strip(), v.strip().strip('"').strip("'")
        if k and k not in os.environ:
            os.environ[k] = v


def yt_get(endpoint: str, params: dict, key: str) -> dict:
    params = {**params, "key": key}
    url = f"{API_BASE}/{endpoint}?{urlencode(params)}"
    req = Request(url, headers={"User-Agent": "cc-trends-yt-fetch/1.0"})
    with urlopen(req, timeout=20, context=SSL_CONTEXT) as r:
        return json.loads(r.read())


def search_query(q: str, published_after: str, key: str, max_results: int) -> list[str]:
    data = yt_get("search", {
        "part": "snippet",
        "q": q,
        "type": "video",
        "order": "viewCount",
        "publishedAfter": published_after,
        "maxResults": max_results,
    }, key)
    return [item["id"]["videoId"] for item in data.get("items", []) if item.get("id", {}).get("videoId")]


def resolve_handle_to_uploads(handle: str, key: str) -> str | None:
    h = handle.lstrip("@")
    data = yt_get("channels", {"part": "id,contentDetails", "forHandle": h}, key)
    items = data.get("items") or []
    if not items:
        return None
    return items[0]["contentDetails"]["relatedPlaylists"]["uploads"]


def channel_recent(uploads_playlist_id: str, published_after: str, key: str, max_results: int) -> list[str]:
    data = yt_get("playlistItems", {
        "part": "snippet,contentDetails",
        "playlistId": uploads_playlist_id,
        "maxResults": max_results,
    }, key)
    cutoff = datetime.fromisoformat(published_after.replace("Z", "+00:00"))
    out = []
    for item in data.get("items", []):
        published = item.get("contentDetails", {}).get("videoPublishedAt")
        vid = item.get("contentDetails", {}).get("videoId")
        if not published or not vid:
            continue
        if datetime.fromisoformat(published.replace("Z", "+00:00")) >= cutoff:
            out.append(vid)
    return out


def video_details(ids: list[str], key: str) -> list[dict]:
    out = []
    for i in range(0, len(ids), 50):
        batch = ids[i:i + 50]
        data = yt_get("videos", {
            "part": "snippet,statistics,contentDetails",
            "id": ",".join(batch),
        }, key)
        for item in data.get("items", []):
            stats = item.get("statistics", {})
            snip = item["snippet"]
            out.append({
                "id": item["id"],
                "title": snip["title"],
                "channel": snip["channelTitle"],
                "channel_id": snip["channelId"],
                "url": f"https://www.youtube.com/watch?v={item['id']}",
                "published_at": snip["publishedAt"],
                "view_count": int(stats.get("viewCount", 0)),
                "like_count": int(stats.get("likeCount", 0)),
                "comment_count": int(stats.get("commentCount", 0)),
                "duration": item.get("contentDetails", {}).get("duration"),
                "duration_seconds": parse_iso8601_duration(item.get("contentDetails", {}).get("duration", "")),
                "description_excerpt": (snip.get("description") or "")[:280],
            })
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--days", type=int, default=7)
    ap.add_argument("--per-query", type=int, default=10)
    ap.add_argument("--per-channel", type=int, default=10)
    ap.add_argument("--top", type=int, default=20)
    ap.add_argument("--min-duration-seconds", type=int, default=60,
                    help="filter out videos shorter than this (default 60 = exclude Shorts)")
    ap.add_argument("--queries", nargs="*", help="override default queries")
    ap.add_argument("--channels-file", default=str(CCROOT / "channels.json"))
    ap.add_argument("--env-file", default=str(PERSONAL_ROOT / ".env"))
    args = ap.parse_args()

    load_env_file(Path(args.env_file))
    key = os.environ.get("YOUTUBE_API_KEY")
    if not key:
        json.dump({"error": "YOUTUBE_API_KEY not set", "tried_env_file": args.env_file}, sys.stdout)
        return 1

    cutoff = (datetime.now(timezone.utc) - timedelta(days=args.days)).isoformat().replace("+00:00", "Z")
    queries = args.queries or DEFAULT_QUERIES

    found_ids: set[str] = set()
    via: dict[str, list[str]] = {}  # video_id -> [sources that surfaced it]
    errors: list[str] = []

    for q in queries:
        try:
            for vid in search_query(q, cutoff, key, args.per_query):
                found_ids.add(vid)
                via.setdefault(vid, []).append(f"query:{q}")
        except (HTTPError, URLError) as e:
            errors.append(f"search '{q}': {e}")

    channels_path = Path(args.channels_file)
    channels_used: list[dict] = []
    if channels_path.exists():
        try:
            cfg = json.loads(channels_path.read_text())
            for ch in cfg.get("channels", []):
                handle = ch.get("handle")
                if not handle:
                    continue
                try:
                    uploads = resolve_handle_to_uploads(handle, key)
                    if not uploads:
                        errors.append(f"channel {handle}: handle not found")
                        continue
                    vids = channel_recent(uploads, cutoff, key, args.per_channel)
                    for vid in vids:
                        found_ids.add(vid)
                        via.setdefault(vid, []).append(f"channel:{handle}")
                    channels_used.append({"handle": handle, "videos_in_window": len(vids)})
                except (HTTPError, URLError) as e:
                    errors.append(f"channel {handle}: {e}")
        except json.JSONDecodeError as e:
            errors.append(f"channels.json parse: {e}")

    videos: list[dict] = []
    if found_ids:
        try:
            videos = video_details(list(found_ids), key)
        except (HTTPError, URLError) as e:
            errors.append(f"video details: {e}")

    for v in videos:
        v["sources"] = via.get(v["id"], [])

    filtered_short_count = 0
    if args.min_duration_seconds > 0:
        kept = []
        for v in videos:
            if v.get("duration_seconds", 0) < args.min_duration_seconds:
                filtered_short_count += 1
                continue
            kept.append(v)
        videos = kept

    videos.sort(key=lambda v: v["view_count"], reverse=True)
    videos = videos[: args.top]

    json.dump({
        "items": videos,
        "errors": errors,
        "fetched_at": datetime.now(timezone.utc).isoformat(),
        "queries_used": queries,
        "channels_used": channels_used,
        "window_days": args.days,
        "filtered_short_count": filtered_short_count,
        "min_duration_seconds": args.min_duration_seconds,
    }, sys.stdout, indent=2, ensure_ascii=False)
    print()
    return 0


if __name__ == "__main__":
    sys.exit(main())
