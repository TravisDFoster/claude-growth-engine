#!/usr/bin/env python3
"""Refresh the content dashboard data.json.

Reads:
  - rolling-4week.md           (carryover, weeks, this_week)
  - marketing/seo/briefs/*.md   (frontmatter only)
  - marketing/channels/{seo-blog,icpro-blog}/blog-posts-{pre-writing,draft,live}/*.md
  - marketing/content-plan/jira/imports/*.csv

Writes:
  - content-dashboard/data.json
  - content-dashboard/data.previous.json   (copy of prior data.json)

Run:
    python3 /Users/travisfoster/claude-code/cerkl/content-dashboard/refresh.py
"""

import csv
import json
import re
import shutil
from datetime import date, timedelta
from pathlib import Path

ROOT = Path("/Users/travisfoster/claude-code/cerkl")
TODAY = date.today()
TODAY_STR = TODAY.isoformat()

DASH = ROOT / "content-dashboard"
ROLLING = ROOT / "marketing/content-plan/rolling-4week.md"
BRIEFS_DIR = ROOT / "marketing/seo/briefs"
SEO_BLOG = ROOT / "marketing/channels/seo-blog"
ICPRO_BLOG = ROOT / "marketing/channels/icpro-blog"
JIRA_DIR = ROOT / "marketing/content-plan/jira/imports"

CERKL_PREFIX = "Content - Blog (Cerkl.com)"
ICPRO_PREFIX = "Content - Blog (ICP)"
LINKEDIN_PREFIX = "Social Media - LinkedIn"


# --- Frontmatter ----------------------------------------------------------

def parse_frontmatter(path):
    text = path.read_text()
    if not text.startswith("---"):
        return {}
    end = text.find("\n---", 4)
    if end < 0:
        return {}
    out = {}
    for line in text[4:end].split("\n"):
        if not line or line.startswith(" ") or line.startswith("#") or ":" not in line:
            continue
        key, _, val = line.partition(":")
        val = val.strip().strip('"').strip("'")
        out[key.strip()] = val
    return out


# --- Briefs ---------------------------------------------------------------

EXCLUDE_BRIEFS = {"_template.md"}


def scan_briefs():
    queued, scheduled, in_progress, shipped = [], [], [], []
    for p in sorted(BRIEFS_DIR.glob("*.md")):
        if p.name in EXCLUDE_BRIEFS:
            continue
        fm = parse_frontmatter(p)
        item = {
            "title": fm.get("title", ""),
            "slug": fm.get("slug", p.stem),
            "url": f"/cerkl/marketing/seo/briefs/{p.name}",
            "target_channel": fm.get("target_channel", ""),
        }
        if fm.get("scheduled_for"):
            item["scheduled_for"] = fm["scheduled_for"]
        status = fm.get("status", "")
        {"queued": queued, "scheduled": scheduled,
         "in-progress": in_progress, "shipped": shipped}.get(status, []).append(item)
    scheduled.sort(key=lambda x: x.get("scheduled_for", "9999"))
    in_progress.sort(key=lambda x: x.get("scheduled_for", "9999"))
    queued.sort(key=lambda x: x["slug"])
    shipped.sort(key=lambda x: x["slug"])
    return {"queued": queued, "scheduled": scheduled,
            "in_progress": in_progress, "shipped": shipped}


# --- Blog folders ---------------------------------------------------------

FILENAME_RE = re.compile(r'^(\d{4}-\d{2}-\d{2}|TBD)_(.+)_(pre-writing|draft|live)\.md$')


def parse_blog_filename(name):
    m = FILENAME_RE.match(name)
    if not m:
        return None
    date_part, slug, state = m.group(1), m.group(2), m.group(3)
    return {
        "title": " ".join(w.capitalize() for w in slug.split("-")),
        "date": date_part,
        "slug": slug,
        "state": state,
    }


def sort_blog_items(items):
    dated = sorted([x for x in items if x["date"] != "TBD"],
                   key=lambda x: x["date"], reverse=True)
    tbd = [x for x in items if x["date"] == "TBD"]
    return dated + tbd


def scan_blog_channel(root, slug):
    folders = {
        "pre_writing": root / "blog-posts-pre-writing",
        "draft": root / "blog-posts-draft",
        "live": root / "blog-posts-live",
    }
    buckets = {}
    for bucket_name, folder in folders.items():
        items = []
        if folder.exists():
            for f in folder.iterdir():
                if not f.is_file() or not f.name.endswith(".md"):
                    continue
                parsed = parse_blog_filename(f.name)
                if not parsed:
                    continue
                items.append({
                    "title": parsed["title"],
                    "date": parsed["date"],
                    "slug": parsed["slug"],
                    "url": f"/cerkl/marketing/channels/{slug}/blog-posts-{parsed['state']}/{f.name}",
                })
        buckets[bucket_name] = sort_blog_items(items)
    return buckets


# --- Rolling 4-week -------------------------------------------------------

def _parse_table(lines, start):
    i = start
    while i < len(lines):
        if re.match(r'^\|\s*-', lines[i]):
            i += 1
            break
        if lines[i].startswith("## ") or lines[i].startswith("---"):
            return [], i
        i += 1
    rows = []
    while i < len(lines):
        line = lines[i]
        if line.startswith("## ") or line.startswith("---"):
            break
        if line.startswith("|"):
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if len(cells) >= 6:
                m = re.match(r'\[([^\]]+)\]\(([^)]+)\)', cells[5])
                if m:
                    slug = m.group(1)
                    source_brief = slug
                    source_brief_url = f"/cerkl/marketing/seo/briefs/{slug}.md"
                else:
                    source_brief = cells[5]
                    source_brief_url = None
                rows.append({
                    "deliverable": cells[0].strip("*").strip(),
                    "channel": cells[1],
                    "publish": cells[2],
                    "owner": cells[3],
                    "status": cells[4],
                    "source_brief": source_brief,
                    "source_brief_url": source_brief_url,
                })
        i += 1
    return rows, i


def parse_rolling_4week():
    text = ROLLING.read_text()
    lines = text.split("\n")
    last_reconciled = None
    for line in lines:
        m = re.match(r'\*\*Last reconciled:\*\*\s*(\d{4}-\d{2}-\d{2})', line)
        if m:
            last_reconciled = m.group(1)
            break

    carryover_rows = []
    weeks = []
    i = 0
    while i < len(lines):
        line = lines[i]
        if line.startswith("## Carryover"):
            rows, i = _parse_table(lines, i + 1)
            carryover_rows = rows
        elif re.match(r'^## Week \d', line):
            label = line[3:].strip()
            rows, i = _parse_table(lines, i + 1)
            weeks.append({
                "label": label,
                "rows": rows,
                "locked": "(locked" in label,
                "in_jira": "in Jira" in label,
            })
        else:
            i += 1

    for w in weeks:
        dates = [r["publish"] for r in w["rows"]
                 if re.match(r'\d{4}-\d{2}-\d{2}$', r["publish"])]
        if dates:
            min_d = date.fromisoformat(min(dates))
            monday = min_d - timedelta(days=min_d.weekday())
            friday = monday + timedelta(days=4)
            w["range"] = f"{monday.isoformat()} → {friday.isoformat()}"
            w["_monday"] = monday
        else:
            w["range"] = ""
            w["_monday"] = None
    return last_reconciled, carryover_rows, weeks


# --- Jira CSVs ------------------------------------------------------------

def drive_url_filled(description):
    for line in description.split("\n"):
        if line.strip().startswith("Draft (Google Doc):"):
            if "[DRIVE_URL_PLACEHOLDER]" in line:
                return False
            if "https://docs.google.com/" in line:
                return True
    return False


def linkedin_copy_filled(description):
    has_copy = re.search(r'^Copy:\s*$', description, re.MULTILINE) is not None
    return has_copy and "[COPY_PLACEHOLDER]" not in description


def is_out_of_band(summary):
    """Out-of-band rows are placeholders for Jira capacity tracking only —
    Furqan fills topic + copy at publish time, outside the content-plan system.
    They never carry [COPY_PLACEHOLDER] and shouldn't count toward copy fill."""
    return "(out-of-band)" in summary


def parse_csv_file(path):
    m = re.match(r'(\d{4})-W(\d{2})\.csv', path.name)
    if not m:
        return None
    year, week = int(m.group(1)), int(m.group(2))
    monday = date.fromisocalendar(year, week, 1)
    friday = monday + timedelta(days=4)

    tasks_total = cerkl = icpro = linkedin = subtasks = 0
    drive_f = drive_t = copy_f = copy_t = 0

    with path.open() as f:
        for row in csv.DictReader(f):
            t = row.get("Issue Type", "").strip()
            summary = row.get("Summary", "")
            desc = row.get("Description", "")
            if t == "Task":
                tasks_total += 1
                if summary.startswith(CERKL_PREFIX):
                    cerkl += 1
                    drive_t += 1
                    if drive_url_filled(desc):
                        drive_f += 1
                elif summary.startswith(ICPRO_PREFIX):
                    icpro += 1
                    drive_t += 1
                    if drive_url_filled(desc):
                        drive_f += 1
                elif summary.startswith(LINKEDIN_PREFIX):
                    linkedin += 1
                    if not is_out_of_band(summary):
                        copy_t += 1
                        if linkedin_copy_filled(desc):
                            copy_f += 1
            elif t == "Subtask":
                subtasks += 1

    import_ready = (drive_f == drive_t and copy_f == copy_t and drive_t + copy_t > 0)
    if TODAY >= monday:
        status = "imported"
    elif import_ready:
        status = "ready-to-import"
    else:
        status = "in-prep"

    return {
        "file": path.name,
        "path": f"/cerkl/marketing/content-plan/jira/imports/{path.name}",
        "week_iso": f"{year}-W{week:02d}",
        "week_monday": monday.isoformat(),
        "week_range": f"{monday.isoformat()} → {friday.isoformat()}",
        "status": status,
        "counts": {
            "tasks_total": tasks_total,
            "cerkl_blog_tasks": cerkl,
            "icpro_blog_tasks": icpro,
            "linkedin_tasks": linkedin,
            "subtasks_total": subtasks,
        },
        "readiness": {
            "drive_urls": {"filled": drive_f, "total": drive_t},
            "linkedin_copy": {"filled": copy_f, "total": copy_t},
        },
        "import_ready": drive_f == drive_t and copy_f == copy_t,
        "_monday": monday,
    }


def scan_csvs():
    csvs = []
    for p in sorted(JIRA_DIR.glob("*.csv")):
        c = parse_csv_file(p)
        if c:
            csvs.append(c)
    csvs.sort(key=lambda x: x["_monday"])
    return csvs


def find_current_csv(csvs):
    future = [c for c in csvs if c["_monday"] >= TODAY]
    if future:
        return min(future, key=lambda c: c["_monday"])
    return max(csvs, key=lambda c: c["_monday"])


# --- LinkedIn derivation --------------------------------------------------

def derive_linkedin(carryover, weeks):
    planned, in_progress, shipped = [], [], []
    blocked = pulled = 0

    def view(r):
        return {
            "deliverable": r["deliverable"],
            "channel": r["channel"],
            "publish": r["publish"],
            "owner": r["owner"],
            "source_brief": r["source_brief"],
        }

    for r in carryover:
        if r["channel"].startswith("LinkedIn"):
            in_progress.append(view(r))

    for w in weeks:
        for r in w["rows"]:
            if not r["channel"].startswith("LinkedIn"):
                continue
            s = r["status"]
            if s == "planned":
                planned.append(view(r))
            elif s == "in-progress":
                in_progress.append(view(r))
            elif s == "shipped":
                shipped.append(view(r))
            elif s == "blocked":
                blocked += 1
            elif s == "pulled":
                pulled += 1

    planned.sort(key=lambda x: x["publish"])
    in_progress.sort(key=lambda x: x["publish"])
    shipped.sort(key=lambda x: x["publish"])
    return {"planned": planned, "in_progress": in_progress, "shipped": shipped}, blocked, pulled


# --- Stats ----------------------------------------------------------------

def compute_stats(briefs, seo_b, icpro_b, li_view, li_blocked, weeks, csvs, current_csv):
    weeks_planned = sum(
        1 for w in weeks
        if any(not r["deliverable"].startswith("TBD") for r in w["rows"])
    )
    drive = current_csv["readiness"]["drive_urls"]
    copy = current_csv["readiness"]["linkedin_copy"]
    return {
        "briefs_total": sum(len(briefs[k]) for k in briefs),
        "briefs_queued": len(briefs["queued"]),
        "briefs_scheduled": len(briefs["scheduled"]),
        "briefs_in_progress": len(briefs["in_progress"]),
        "briefs_shipped": len(briefs["shipped"]),
        "seo_blog_in_flight": len(seo_b["pre_writing"]) + len(seo_b["draft"]),
        "seo_blog_live_count": len(seo_b["live"]),
        "icpro_blog_in_flight": len(icpro_b["pre_writing"]) + len(icpro_b["draft"]),
        "icpro_blog_live_count": len(icpro_b["live"]),
        "linkedin_planned": len(li_view["planned"]),
        "linkedin_in_progress": len(li_view["in_progress"]),
        "linkedin_shipped": len(li_view["shipped"]),
        "linkedin_blocked": li_blocked,
        "weeks_planned": weeks_planned,
        "csvs_in_prep": sum(1 for c in csvs if c["status"] == "in-prep"),
        "csvs_ready": sum(1 for c in csvs if c["status"] == "ready-to-import"),
        "csvs_imported": sum(1 for c in csvs if c["status"] == "imported"),
        "current_csv_drive_fill": f'{drive["filled"]}/{drive["total"]}',
        "current_csv_copy_fill": f'{copy["filled"]}/{copy["total"]}',
    }


# --- Actions --------------------------------------------------------------

def find_candidate_brief(deliverable, queued):
    """Look for a queued brief whose slug-tokens overlap the deliverable text.
    Returns the best-matching brief or None. Needs ≥2 distinctive token matches
    (length ≥ 4) to avoid false positives on generic words like 'internal'."""
    deliv = deliverable.lower()
    best, best_count = None, 0
    for b in queued:
        tokens = [t for t in b["slug"].split("-") if len(t) >= 4]
        matches = sum(1 for t in tokens if t in deliv)
        if matches >= 2 and matches > best_count:
            best, best_count = b, matches
    return best


def compute_actions(last_reconciled, carryover, weeks, csvs, current_csv, queued_briefs):
    locked = next((w for w in weeks if w["locked"]), weeks[0] if weeks else None)
    if locked and locked["_monday"]:
        next_monday = locked["_monday"] + timedelta(days=7)
        ny, nw, _ = next_monday.isocalendar()
        next_iso = f"{ny}-W{nw:02d}"
        next_range = f"{next_monday.isoformat()} → {(next_monday + timedelta(days=4)).isoformat()}"
    else:
        next_iso, next_range = "", ""

    scaffold_needed = f"{next_iso}.csv" not in {c["file"] for c in csvs}

    cerkl_unfilled = icpro_unfilled = li_placeholder = 0
    with (JIRA_DIR / current_csv["file"]).open() as f:
        for row in csv.DictReader(f):
            if row.get("Issue Type") != "Task":
                continue
            s = row.get("Summary", "")
            d = row.get("Description", "")
            if s.startswith(CERKL_PREFIX) and not drive_url_filled(d):
                cerkl_unfilled += 1
            elif s.startswith(ICPRO_PREFIX) and not drive_url_filled(d):
                icpro_unfilled += 1
            elif s.startswith(LINKEDIN_PREFIX) and "[COPY_PLACEHOLDER]" in d:
                li_placeholder += 1

    brief_gaps = []
    for r in carryover:
        if "needs brief from SEO" in r["source_brief"]:
            brief_gaps.append({**r, "_where": "Carryover"})
    for i, w in enumerate(weeks):
        for r in w["rows"]:
            if "needs brief from SEO" in r["source_brief"]:
                brief_gaps.append({**r, "_where": f"Week {i + 1}"})

    cur_week = current_csv["week_iso"]
    cur_path = f"/Users/travisfoster/claude-code/cerkl/marketing/content-plan/jira/imports/{current_csv['file']}"
    cur_counts = current_csv["counts"]

    actions = [
        {
            "id": "reconcile",
            "label": "Run Monday reconcile",
            "ready": True,
            "reason": f"Last reconciled {last_reconciled}; next publish week to lock is {next_iso} ({next_range})",
            "prompt": f"Run the Monday reconcile for the upcoming publish week ({next_iso}, {next_range}).\n\nProcess: /Users/travisfoster/claude-code/cerkl/marketing/content-plan/plan-reconcile-process.md",
        },
        {
            "id": "generate-csv-scaffold",
            "label": f"Generate Jira CSV scaffold for {next_iso}",
            "ready": scaffold_needed,
            "reason": (f"No CSV exists yet for {next_iso}" if scaffold_needed
                       else f"{next_iso}.csv already exists"),
            "prompt": f"Generate the Jira CSV scaffold for the next publish week ({next_iso}).\n\nOutput: /Users/travisfoster/claude-code/cerkl/marketing/content-plan/jira/imports/{next_iso}.csv\nProcess: /Users/travisfoster/claude-code/cerkl/marketing/content-plan/jira/jira-scaffold-process.md",
        },
        {
            "id": "bulk-write-cerkl-blog",
            "label": f"Bulk-write cerkl.com blog drafts for {cur_week}",
            "ready": cerkl_unfilled > 0,
            "reason": (f"{cerkl_unfilled} cerkl.com blog Task(s) in {current_csv['file']} still have [DRIVE_URL_PLACEHOLDER]"
                       if cerkl_unfilled > 0
                       else f"All {cur_counts['cerkl_blog_tasks']} cerkl.com blog Task(s) in {current_csv['file']} have Drive URLs filled"),
            "prompt": f"Bulk-write all cerkl.com blog drafts for rows with [DRIVE_URL_PLACEHOLDER] in this week's Jira CSV.\n\nJira CSV: {cur_path}\nProcess: /Users/travisfoster/claude-code/cerkl/marketing/channels/seo-blog/seo-blog-process.md\n\nFor each cerkl.com blog Task in the CSV with [DRIVE_URL_PLACEHOLDER], run the writing+publishing pipeline and replace the placeholder with the resulting Google Drive URL.",
        },
        {
            "id": "bulk-write-icpro-blog",
            "label": f"Bulk-write Internal Comms Pro blog drafts for {cur_week}",
            "ready": icpro_unfilled > 0,
            "reason": (f"{icpro_unfilled} ICPro blog Task(s) in {current_csv['file']} still have [DRIVE_URL_PLACEHOLDER]"
                       if icpro_unfilled > 0
                       else f"All {cur_counts['icpro_blog_tasks']} ICPro blog Task(s) in {current_csv['file']} have Drive URLs filled"),
            "prompt": f"Bulk-write all Internal Comms Pro blog drafts for rows with [DRIVE_URL_PLACEHOLDER] in this week's Jira CSV.\n\nJira CSV: {cur_path}\nProcess: /Users/travisfoster/claude-code/cerkl/marketing/channels/icpro-blog/icpro-blog-process.md\n\nFor each ICPro blog Task in the CSV with [DRIVE_URL_PLACEHOLDER], run the writing+publishing pipeline and replace the placeholder with the resulting Google Drive URL.",
        },
        {
            "id": "bulk-write-linkedin",
            "label": f"Bulk-write LinkedIn copy for {cur_week}",
            "ready": li_placeholder > 0,
            "reason": (f"{li_placeholder} LinkedIn Task(s) in {current_csv['file']} still have [COPY_PLACEHOLDER]"
                       if li_placeholder > 0
                       else f"All {cur_counts['linkedin_tasks']} LinkedIn Task(s) in {current_csv['file']} have drafted copy"),
            "prompt": f"Bulk-write LinkedIn copy in this week's Jira CSV.\n\nJira CSV: {cur_path}\nProcess: /Users/travisfoster/claude-code/cerkl/marketing/channels/linkedin/linkedin-process.md\n\nFor each LinkedIn Task whose Description still contains [COPY_PLACEHOLDER], draft the post and replace the placeholder with [CAPTION] / [POLL], [ASSET SPEC], and [HASHTAGS] in the Task Description.",
        },
    ]

    if brief_gaps:
        gap_lines = []
        deadlines = []
        candidate_notes = []
        for r in brief_gaps:
            dl = re.search(r'needs brief from SEO by (\d{4}-\d{2}-\d{2})', r["source_brief"])
            if dl:
                deadlines.append(dl.group(1))
            cand = find_candidate_brief(r["deliverable"], queued_briefs)
            cand_note = f"; queued brief `{cand['slug']}.md` may fit" if cand else ""
            gap_lines.append(
                f"- {r['_where']}: {r['deliverable']} ({r['channel']}, publish {r['publish']}, {r['source_brief']}){cand_note}"
            )
            if cand:
                candidate_notes.append(cand["slug"])
        deadline_part = f"; earliest deadline {min(deadlines)}" if deadlines else ""
        cand_part = (f"; queued brief(s) may fit: {', '.join(candidate_notes)}"
                     if candidate_notes else "")
        actions.append({
            "id": "fill-brief-gaps",
            "label": "Fill SEO brief gaps in rolling-4week",
            "ready": True,
            "reason": f"{len(brief_gaps)} row(s) in rolling-4week annotated `needs brief from SEO`{deadline_part}{cand_part}",
            "prompt": f"Write SEO briefs for the rolling-4week rows annotated `needs brief from SEO`.\n\nGaps right now (per /Users/travisfoster/claude-code/cerkl/marketing/content-plan/rolling-4week.md):\n" + "\n".join(gap_lines) + "\n\nIf a queued brief is flagged as a fit, confirm it covers the row's angle and (at next reconcile) move it to `status: scheduled` with the row's publish date. Otherwise write a new brief in /Users/travisfoster/claude-code/cerkl/marketing/seo/briefs/ following _template.md.",
        })
    else:
        actions.append({
            "id": "fill-brief-gaps",
            "label": "Fill SEO brief gaps in rolling-4week",
            "ready": False,
            "reason": "No rolling-4week rows currently annotated `needs brief from SEO`",
            "prompt": "Write SEO briefs for the rolling-4week rows annotated `needs brief from SEO`.\n\n(No gaps right now.)",
        })

    actions.append({
        "id": "refresh-dashboard",
        "label": "Refresh this dashboard",
        "ready": True,
        "reason": "Always available",
        "prompt": "Refresh my content dashboard.\n\nProcess: /Users/travisfoster/claude-code/cerkl/content-dashboard/content-dashboard-process.md",
    })

    ready = [a for a in actions if a["ready"]]
    unready = [a for a in actions if not a["ready"]]
    return ready + unready


# --- Main -----------------------------------------------------------------

def main():
    last_reconciled, carryover, weeks = parse_rolling_4week()
    briefs = scan_briefs()
    seo_blog = scan_blog_channel(SEO_BLOG, "seo-blog")
    icpro_blog = scan_blog_channel(ICPRO_BLOG, "icpro-blog")
    li_view, li_blocked, _ = derive_linkedin(carryover, weeks)
    csvs = scan_csvs()
    current_csv = find_current_csv(csvs)
    stats = compute_stats(briefs, seo_blog, icpro_blog, li_view, li_blocked, weeks, csvs, current_csv)
    actions = compute_actions(last_reconciled, carryover, weeks, csvs, current_csv, briefs["queued"])

    csvs_clean = [{k: v for k, v in c.items() if not k.startswith("_")} for c in csvs]
    weeks_clean = [
        {
            "n": i + 1,
            "label": w["label"],
            "range": w["range"],
            "locked": w["locked"],
            "in_jira": w["in_jira"],
            "rows": w["rows"],
        }
        for i, w in enumerate(weeks)
    ]
    this_week = None
    if weeks:
        w0 = weeks[0]
        this_week = {
            "label": w0["label"],
            "range": w0["range"],
            "locked": w0["locked"],
            "in_jira": w0["in_jira"],
            "rows": w0["rows"],
        }

    output = {
        "generated_at": TODAY_STR,
        "last_reconciled": last_reconciled,
        "current_csv_file": current_csv["file"],
        "stats": stats,
        "csvs": csvs_clean,
        "actions": actions,
        "carryover": carryover,
        "this_week": this_week,
        "weeks": weeks_clean,
        "briefs": {
            "queued": briefs["queued"],
            "scheduled": briefs["scheduled"],
            "in_progress": briefs["in_progress"],
        },
        "blog_swimlanes": [
            {
                "slug": "seo-blog",
                "label": "Cerkl Blog (cerkl.com)",
                "subtitle": "Webflow · primary growth channel",
                "new_run_prompt": "Draft this week's planned Cerkl blog post(s) for cerkl.com.\n\nCheck the rolling 4-week plan: /Users/travisfoster/claude-code/cerkl/marketing/content-plan/rolling-4week.md\nProcess: /Users/travisfoster/claude-code/cerkl/marketing/channels/seo-blog/seo-blog-process.md",
                "buckets": seo_blog,
            },
            {
                "slug": "icpro-blog",
                "label": "Internal Comms Pro (internalcommspro.com)",
                "subtitle": "Wix · ICP-aligned secondary",
                "new_run_prompt": "Draft this week's planned Internal Comms Pro blog post(s) for internalcommspro.com.\n\nCheck the rolling 4-week plan: /Users/travisfoster/claude-code/cerkl/marketing/content-plan/rolling-4week.md\nProcess: /Users/travisfoster/claude-code/cerkl/marketing/channels/icpro-blog/icpro-blog-process.md",
                "buckets": icpro_blog,
            },
        ],
        "linkedin": li_view,
    }

    out_path = DASH / "data.json"
    prev_path = DASH / "data.previous.json"
    if out_path.exists():
        shutil.copy2(out_path, prev_path)
    out_path.write_text(json.dumps(output, indent=2, ensure_ascii=False) + "\n")

    ready_count = sum(1 for a in actions if a["ready"])
    print(f"Wrote {out_path}")
    print(f"  briefs:  {stats['briefs_queued']}q / {stats['briefs_scheduled']}s / {stats['briefs_in_progress']}p / {stats['briefs_shipped']}shipped")
    print(f"  blogs:   seo {stats['seo_blog_in_flight']} in flight / {stats['seo_blog_live_count']} live | icpro {stats['icpro_blog_in_flight']} in flight / {stats['icpro_blog_live_count']} live")
    print(f"  csvs:    {stats['csvs_in_prep']} in-prep / {stats['csvs_ready']} ready / {stats['csvs_imported']} imported")
    print(f"  current: {current_csv['file']} (drive {stats['current_csv_drive_fill']}, copy {stats['current_csv_copy_fill']})")
    print(f"  actions: {ready_count} ready / {len(actions)} total")
    if (DASH / "data.previous.json").exists():
        print(f"  prior:   data.previous.json")


if __name__ == "__main__":
    main()
