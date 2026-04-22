#!/usr/bin/env python3
"""
Family OS — Weekly Task Digest
--------------------------------
Queries the Notion Family Tasks database and prints a grouped summary:
  🔴 OVERDUE     — due date is before today
  🟡 DUE THIS WEEK — due date is within the next 7 days
  ⚪ UPCOMING    — due date is beyond 7 days or not set
  ✅ COMPLETED   — status is Done (completed this week, optional)

Usage:
  python scripts/weekly-digest.py              # CLI output only
  python scripts/weekly-digest.py --notion     # CLI + write digest page to Notion
  python scripts/weekly-digest.py --week       # Show tasks due this week only (tighter view)

Requirements:
  pip install "notion-client==2.2.1" python-dotenv

Setup:
  Copy .env.example → .env and fill in NOTION_API_KEY
"""

import os
import sys
import argparse
from datetime import date, timedelta, datetime

try:
    from notion_client import Client
except ImportError:
    print("ERROR: notion-client not installed. Run: pip install notion-client python-dotenv")
    sys.exit(1)

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass  # dotenv optional — env vars can be set directly


# ── Config ────────────────────────────────────────────────────────────────────

NOTION_API_KEY       = os.environ.get("NOTION_API_KEY")
FAMILY_TASKS_DB_ID   = os.environ.get("NOTION_FAMILY_TASKS_DB", "395f395ac3de4ddaa8e86518e3c0377a")
HUB_PAGE_ID          = os.environ.get("NOTION_HUB_PAGE_ID",     "34a2cb98-3974-8170-9c3e-c3746f6e9b8f")

PRIORITY_ORDER = {"P1 (do today)": 1, "P2 (this week)": 2, "P3 (someday)": 3}
PRIORITY_EMOJI = {"P1 (do today)": "🔴", "P2 (this week)": "🟡", "P3 (someday)": "⚪"}

def normalize_priority(raw):
    """Match priority regardless of exact casing or label variation."""
    if not raw:
        return "P3 (someday)"
    r = raw.strip()
    if r.startswith("P1") or "today" in r.lower():
        return "P1 (do today)"
    if r.startswith("P2") or "week" in r.lower():
        return "P2 (this week)"
    return "P3 (someday)"


# ── Notion query ──────────────────────────────────────────────────────────────

def fetch_open_tasks(client):
    """Pull all non-Done tasks from the Family Tasks database."""
    results = []
    cursor = None

    while True:
        kwargs = {"database_id": FAMILY_TASKS_DB_ID}
        if cursor:
            kwargs["start_cursor"] = cursor

        response = client.databases.query(**kwargs)
        # Filter in Python — Notion's does_not_equal silently drops null-status tasks
        for page in response["results"]:
            status = (page["properties"].get("Status", {}).get("select") or {}).get("name", "")
            if status != "Done":
                results.append(page)

        if not response.get("has_more"):
            break
        cursor = response["next_cursor"]

    return results


def fetch_completed_this_week(client):
    """Pull tasks completed in the last 7 days."""
    one_week_ago = (date.today() - timedelta(days=7)).isoformat()
    results = []
    cursor = None

    while True:
        kwargs = {
            "database_id": FAMILY_TASKS_DB_ID,
            "filter": {
                "and": [
                    {"property": "Status", "select": {"equals": "Done"}},
                    {"property": "Due Date", "date": {"on_or_after": one_week_ago}},
                ]
            },
        }
        if cursor:
            kwargs["start_cursor"] = cursor

        response = client.databases.query(**kwargs)
        results.extend(response["results"])

        if not response.get("has_more"):
            break
        cursor = response["next_cursor"]

    return results


# ── Task parsing ──────────────────────────────────────────────────────────────

def parse_task(page):
    props = page["properties"]

    title_parts = props.get("Title", {}).get("title", [])
    title = "".join(t.get("plain_text", "") for t in title_parts) or "(untitled)"

    assignee = (props.get("Assignee", {}).get("select") or {}).get("name", "Unassigned")
    priority  = normalize_priority((props.get("Priority", {}).get("select") or {}).get("name"))
    status    = (props.get("Status", {}).get("select") or {}).get("name", "Not Started")
    notes     = "".join(t.get("plain_text", "") for t in props.get("Notes", {}).get("rich_text", []))

    # Project name via relation — title is on the related page, not inline
    project_relations = props.get("Project", {}).get("relation", [])
    project = f"{len(project_relations)} project(s)" if project_relations else "—"

    due_raw = (props.get("Due Date", {}).get("date") or {}).get("start")
    due_date = date.fromisoformat(due_raw) if due_raw else None

    return {
        "title":    title,
        "assignee": assignee,
        "priority": priority,
        "status":   status,
        "due_date": due_date,
        "project":  project,
        "notes":    notes,
    }


# ── Grouping ──────────────────────────────────────────────────────────────────

def bucket_tasks(tasks):
    today      = date.today()
    week_end   = today + timedelta(days=7)

    overdue    = []
    this_week  = []
    upcoming   = []
    no_due     = []

    for t in tasks:
        d = t["due_date"]
        if d is None:
            no_due.append(t)
        elif d < today:
            overdue.append(t)
        elif d <= week_end:
            this_week.append(t)
        else:
            upcoming.append(t)

    # Sort each bucket by priority then due date
    def sort_key(t):
        p = PRIORITY_ORDER.get(t["priority"], 99)
        d = t["due_date"] or date(9999, 12, 31)
        return (p, d)

    for bucket in [overdue, this_week, upcoming, no_due]:
        bucket.sort(key=sort_key)

    return overdue, this_week, upcoming, no_due


# ── Formatting ────────────────────────────────────────────────────────────────

BAR = "━" * 52

def fmt_task_line(t, show_due=True):
    emoji = PRIORITY_EMOJI.get(t["priority"], "⚪")
    due   = f" — due {t['due_date'].strftime('%b %-d')}" if (show_due and t["due_date"]) else ""
    overdue_tag = " ⚠️" if (t["due_date"] and t["due_date"] < date.today()) else ""
    return f"    {emoji} {t['title']}{overdue_tag}{due}  [{t['assignee']}]"


def group_by_assignee(tasks):
    groups = {}
    for t in tasks:
        groups.setdefault(t["assignee"], []).append(t)
    return groups


def print_digest(overdue, this_week, upcoming, no_due, completed):
    today = date.today()
    week_str = today.strftime("Week of %B %-d, %Y")

    print(f"\n{BAR}")
    print(f"  FAMILY OS — Weekly Digest")
    print(f"  {week_str}")
    print(f"{BAR}\n")

    # OVERDUE
    print(f"🔴  OVERDUE ({len(overdue)} tasks)")
    if overdue:
        for t in overdue:
            days_late = (today - t["due_date"]).days
            emoji = PRIORITY_EMOJI.get(t["priority"], "⚪")
            print(f"    {emoji} {t['title']}  [{t['assignee']}]  — was due {t['due_date'].strftime('%b %-d')} ({days_late}d late)")
    else:
        print("    ✓ Nothing overdue")
    print()

    # DUE THIS WEEK
    print(f"🟡  DUE THIS WEEK ({len(this_week)} tasks)")
    if this_week:
        for t in this_week:
            print(fmt_task_line(t, show_due=True))
    else:
        print("    ✓ Nothing due this week")
    print()

    # UPCOMING
    print(f"⚪  UPCOMING ({len(upcoming)} tasks)")
    if upcoming:
        for t in upcoming:
            print(fmt_task_line(t, show_due=True))
    else:
        print("    (none)")
    print()

    # NO DUE DATE
    print(f"📌  NO DUE DATE ({len(no_due)} tasks)")
    if no_due:
        for t in no_due:
            emoji = PRIORITY_EMOJI.get(t["priority"], "⚪")
            print(f"    {emoji} {t['title']}  [{t['assignee']}]")
    else:
        print("    (none)")
    print()

    # COMPLETED THIS WEEK
    print(f"✅  COMPLETED THIS WEEK ({len(completed)} tasks)")
    if completed:
        for t in completed:
            emoji = PRIORITY_EMOJI.get(t["priority"], "⚪")
            print(f"    {emoji} {t['title']}  [{t['assignee']}]")
    else:
        print("    (none)")

    # Summary
    total_open = len(overdue) + len(this_week) + len(upcoming) + len(no_due)
    print(f"\n{BAR}")
    print(f"  {total_open} open tasks  ·  {len(completed)} completed this week")
    print(f"  Generated {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print(f"{BAR}\n")


# ── Notion page writer ────────────────────────────────────────────────────────

def build_notion_content(overdue, this_week, upcoming, no_due, completed):
    today    = date.today()
    week_str = today.strftime("Week of %B %-d, %Y")
    lines    = []

    def section(emoji, label, tasks, show_due=True):
        lines.append(f"## {emoji} {label} ({len(tasks)})")
        if not tasks:
            lines.append("*None*")
        else:
            for t in tasks:
                due = f" — due {t['due_date'].strftime('%b %-d')}" if (show_due and t["due_date"]) else ""
                days_late = f" ({(today - t['due_date']).days}d late)" if (t["due_date"] and t["due_date"] < today) else ""
                pri = PRIORITY_EMOJI.get(t["priority"], "⚪")
                lines.append(f"- {pri} **{t['title']}** [{t['assignee']}]{due}{days_late}")
        lines.append("")

    lines.append(f"*Generated automatically by Family OS · {datetime.now().strftime('%Y-%m-%d %H:%M')}*")
    lines.append("")

    total_open = len(overdue) + len(this_week) + len(upcoming) + len(no_due)
    lines.append(f"> **{total_open} open tasks** · {len(overdue)} overdue · {len(completed)} completed this week")
    lines.append("")

    section("🔴", "OVERDUE", overdue, show_due=True)
    section("🟡", "DUE THIS WEEK", this_week, show_due=True)
    section("⚪", "UPCOMING", upcoming, show_due=True)
    section("📌", "NO DUE DATE", no_due, show_due=False)
    section("✅", "COMPLETED THIS WEEK", completed, show_due=False)

    return "\n".join(lines)


def write_to_notion(client, overdue, this_week, upcoming, no_due, completed):
    today    = date.today()
    week_str = today.strftime("Week of %B %-d")
    title    = f"📋 Weekly Digest — {week_str}"
    content  = build_notion_content(overdue, this_week, upcoming, no_due, completed)

    page = client.pages.create(
        parent={"page_id": HUB_PAGE_ID},
        icon={"type": "emoji", "emoji": "📋"},
        properties={"title": {"title": [{"type": "text", "text": {"content": title}}]}},
        children=[
            {
                "object": "block",
                "type": "paragraph",
                "paragraph": {
                    "rich_text": [{"type": "text", "text": {"content": content}}]
                },
            }
        ],
    )
    return page["url"]


# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Family OS — Weekly Task Digest")
    parser.add_argument("--notion", action="store_true", help="Write digest to a new Notion page")
    parser.add_argument("--week",   action="store_true", help="Show only this-week and overdue tasks")
    parser.add_argument("--debug",  action="store_true", help="Print raw task titles and statuses from Notion")
    args = parser.parse_args()

    if not NOTION_API_KEY:
        print("ERROR: NOTION_API_KEY is not set.")
        print("  1. Copy .env.example → .env")
        print("  2. Add your Notion integration token")
        print("  3. Re-run the script")
        sys.exit(1)

    client = Client(auth=NOTION_API_KEY)

    print("Fetching tasks from Notion...", end=" ", flush=True)

    if args.debug:
        # Fetch ALL tasks with no filter to see raw state
        print("\n[DEBUG] Fetching ALL tasks (no filter)...")
        all_pages = []
        cursor = None
        while True:
            kwargs = {"database_id": FAMILY_TASKS_DB_ID}
            if cursor:
                kwargs["start_cursor"] = cursor
            resp = client.databases.query(**kwargs)
            all_pages.extend(resp["results"])
            if not resp.get("has_more"):
                break
            cursor = resp["next_cursor"]
        print(f"[DEBUG] Total rows in database: {len(all_pages)}")
        for p in all_pages:
            props = p["properties"]
            title = "".join(t.get("plain_text","") for t in props.get("Title",{}).get("title",[]))
            status = (props.get("Status",{}).get("select") or {}).get("name","(no status)")
            assignee = (props.get("Assignee",{}).get("select") or {}).get("name","(no assignee)")
            print(f"  • {title!r:40s}  status={status!r:20s}  assignee={assignee!r}")
        print()

    raw_open      = fetch_open_tasks(client)
    raw_completed = fetch_completed_this_week(client)
    print(f"got {len(raw_open)} open, {len(raw_completed)} completed this week.")

    open_tasks  = [parse_task(p) for p in raw_open]
    completed   = [parse_task(p) for p in raw_completed]

    overdue, this_week, upcoming, no_due = bucket_tasks(open_tasks)

    if args.week:
        # Compact view: overdue + this week only
        print_digest(overdue, this_week, [], [], [])
    else:
        print_digest(overdue, this_week, upcoming, no_due, completed)

    if args.notion:
        print("Writing digest to Notion...", end=" ", flush=True)
        url = write_to_notion(client, overdue, this_week, upcoming, no_due, completed)
        print(f"done.\n  → {url}")


if __name__ == "__main__":
    main()
