#!/usr/bin/env python3
"""
Pull raw Discord messages from Supabase and store locally by channel/week.

Uses the message_feed view which pre-joins author names, channel names,
and structured reactions (emoji + reactor name).

Usage:
    python pull_raw_messages.py                    # Pull all Wan channels, all time
    python pull_raw_messages.py wan_chatter         # Pull one channel
    python pull_raw_messages.py wan_chatter 2025-07 # Pull one channel, one month
    python pull_raw_messages.py --status            # Show what's been pulled

Stores as: data/raw/{channel_name}/{YYYY}-W{WW}.json (ISO week)
"""

import requests
import json
import os
import sys
from datetime import datetime, timedelta
from pathlib import Path

# Load .env file if present
env_path = Path(__file__).parent.parent / '.env'
if env_path.exists():
    with open(env_path) as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith('#') and '=' in line:
                key, value = line.split('=', 1)
                os.environ[key] = value

import functools
print = functools.partial(print, flush=True)

API_URL = "https://ujlwuvkrxlvoswwkerdf.supabase.co/rest/v1"
API_KEY = os.environ.get("SUPABASE_API_KEY", "")

if not API_KEY:
    print("Error: SUPABASE_API_KEY not set in .env or environment")
    sys.exit(1)

HEADERS = {"apikey": API_KEY}

# Wan ecosystem channels (channel_id → name)
WAN_CHANNELS = {
    1342763350815277067: "wan_chatter",
    1344057524935983125: "wan_gens",
    1344309523187368046: "wan_training",
    1420053619541283000: "wan_comfyui",
    1373291419434877078: "wan_resources",
}

# Reverse lookup
CHANNEL_NAME_TO_ID = {v: k for k, v in WAN_CHANNELS.items()}

# Data directory
DATA_DIR = Path(__file__).parent.parent / "data" / "raw"


def iso_week_start(year, week):
    """Get the Monday that starts ISO week."""
    jan4 = datetime(year, 1, 4)
    start_of_week1 = jan4 - timedelta(days=jan4.isoweekday() - 1)
    return start_of_week1 + timedelta(weeks=week - 1)


def get_week_boundaries(dt):
    """Get (monday, next_monday) for the ISO week containing dt."""
    iso_year, iso_week, _ = dt.isocalendar()
    monday = iso_week_start(iso_year, iso_week)
    next_monday = monday + timedelta(weeks=1)
    return monday, next_monday, iso_year, iso_week


def week_label(iso_year, iso_week):
    """Format as YYYY-WNN."""
    return f"{iso_year}-W{iso_week:02d}"


def fetch_messages_for_range(channel_id, start_date, end_date):
    """Fetch all messages from message_feed for a channel and date range.

    Uses message_feed view which includes author_name, channel_name, and
    structured reactions (emoji + reactor name).

    Also fetches reference_id, edited_at, is_pinned from discord_messages
    for fields not in the view.
    """
    # Fetch from message_feed (has author names, reactions inline)
    feed_messages = []
    offset = 0
    batch_size = 1000

    while True:
        url = (
            f"{API_URL}/message_feed"
            f"?channel_id=eq.{channel_id}"
            f"&created_at=gte.{start_date}"
            f"&created_at=lt.{end_date}"
            f"&select=message_id,content,created_at,author_name,channel_name,reactions"
            f"&order=created_at.asc"
            f"&offset={offset}&limit={batch_size}"
        )
        resp = requests.get(url, headers=HEADERS, timeout=60)
        if resp.status_code != 200:
            print(f"  Error {resp.status_code}: {resp.text[:200]}")
            break

        data = resp.json()
        if not data:
            break

        feed_messages.extend(data)
        offset += batch_size
        print(f"    message_feed: {len(feed_messages)} messages...", end='\r')

        if len(data) < batch_size:
            break

    if not feed_messages:
        return []

    print(f"    message_feed: {len(feed_messages)} messages       ")

    # Fetch additional fields from discord_messages (reference_id, edited_at, etc.)
    # We need these for reply chain reconstruction and edit tracking
    extra_fields = {}
    offset = 0

    while True:
        url = (
            f"{API_URL}/discord_messages"
            f"?channel_id=eq.{channel_id}"
            f"&created_at=gte.{start_date}"
            f"&created_at=lt.{end_date}"
            f"&select=message_id,reference_id,edited_at,is_pinned,attachments,embeds,thread_id,is_deleted"
            f"&order=created_at.asc"
            f"&offset={offset}&limit={batch_size}"
        )
        resp = requests.get(url, headers=HEADERS, timeout=60)
        if resp.status_code != 200:
            print(f"  Error fetching extras {resp.status_code}: {resp.text[:200]}")
            break

        data = resp.json()
        if not data:
            break

        for msg in data:
            extra_fields[msg["message_id"]] = msg
        offset += batch_size
        print(f"    discord_messages extras: {len(extra_fields)} messages...", end='\r')

        if len(data) < batch_size:
            break

    print(f"    discord_messages extras: {len(extra_fields)} messages       ")

    # Merge: message_feed fields + discord_messages extras
    merged = []
    for msg in feed_messages:
        mid = msg["message_id"]
        extras = extra_fields.get(mid, {})

        # Skip deleted messages
        if extras.get("is_deleted", False):
            continue

        merged.append({
            "message_id": mid,
            "content": msg["content"],
            "created_at": msg["created_at"],
            "author_name": msg["author_name"],
            "channel_name": msg["channel_name"],
            "reactions": msg.get("reactions"),
            "reference_id": extras.get("reference_id"),
            "edited_at": extras.get("edited_at"),
            "is_pinned": extras.get("is_pinned", False),
            "attachments": extras.get("attachments", []),
            "embeds": extras.get("embeds", []),
            "thread_id": extras.get("thread_id"),
        })

    return merged


def parse_timestamp(ts):
    """Parse Supabase timestamps which may have variable fractional seconds."""
    # Strip timezone suffix
    ts = ts.replace("+00:00", "").replace("Z", "")
    # Normalize fractional seconds to 6 digits (microseconds)
    if "." in ts:
        base, frac = ts.split(".")
        frac = frac[:6].ljust(6, '0')
        ts = f"{base}.{frac}"
    return datetime.fromisoformat(ts)


def organize_by_week(messages):
    """Split messages into ISO week buckets. Returns {week_label: [messages]}."""
    weeks = {}
    for msg in messages:
        dt = parse_timestamp(msg["created_at"])
        _, _, iso_year, iso_week = get_week_boundaries(dt)
        label = week_label(iso_year, iso_week)
        weeks.setdefault(label, []).append(msg)
    return weeks


def save_week(channel_name, wk_label, messages):
    """Save a week of messages to JSON."""
    out_dir = DATA_DIR / channel_name
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / f"{wk_label}.json"

    data = {
        "channel": channel_name,
        "week": wk_label,
        "message_count": len(messages),
        "first_message": messages[0]["created_at"] if messages else None,
        "last_message": messages[-1]["created_at"] if messages else None,
        "messages": messages,
    }

    with open(out_path, 'w') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    return out_path


def get_existing_weeks(channel_name):
    """Return set of week labels already pulled for a channel."""
    channel_dir = DATA_DIR / channel_name
    if not channel_dir.exists():
        return set()
    return {p.stem for p in channel_dir.glob("*.json")}


def pull_channel(channel_name, channel_id, month_filter=None):
    """Pull all messages for a channel, organized by week.

    If month_filter is set (e.g. '2025-07'), only pulls that month.
    Skips weeks that already exist on disk.
    """
    existing = get_existing_weeks(channel_name)

    if month_filter:
        year, month = int(month_filter[:4]), int(month_filter[5:7])
        start = datetime(year, month, 1)
        if month == 12:
            end = datetime(year + 1, 1, 1)
        else:
            end = datetime(year, month + 1, 1)
        start_str = start.strftime("%Y-%m-%d")
        end_str = end.strftime("%Y-%m-%d")
    else:
        # Wan channels started Feb 2025
        start_str = "2025-02-01"
        end_str = datetime.now().strftime("%Y-%m-%d")

    print(f"\n{'='*60}")
    print(f"Channel: {channel_name} (ID: {channel_id})")
    print(f"Range: {start_str} to {end_str}")
    print(f"Already have: {len(existing)} weeks")
    print(f"{'='*60}")

    # Pull in monthly batches to avoid huge single requests
    current = datetime.strptime(start_str, "%Y-%m-%d")
    end_dt = datetime.strptime(end_str, "%Y-%m-%d")

    total_messages = 0
    total_weeks_saved = 0
    total_weeks_skipped = 0

    while current < end_dt:
        # Month boundary
        if current.month == 12:
            month_end = datetime(current.year + 1, 1, 1)
        else:
            month_end = datetime(current.year, current.month + 1, 1)
        month_end = min(month_end, end_dt)

        month_label = current.strftime("%Y-%m")
        print(f"\n  {month_label}...")

        messages = fetch_messages_for_range(
            channel_id,
            current.strftime("%Y-%m-%d"),
            month_end.strftime("%Y-%m-%d"),
        )

        if messages:
            weeks = organize_by_week(messages)
            for wk_label in sorted(weeks.keys()):
                if wk_label in existing:
                    total_weeks_skipped += 1
                    print(f"    {wk_label}: {len(weeks[wk_label]):,} msgs (skip - exists)")
                    continue

                path = save_week(channel_name, wk_label, weeks[wk_label])
                total_messages += len(weeks[wk_label])
                total_weeks_saved += 1
                print(f"    {wk_label}: {len(weeks[wk_label]):,} msgs → {path.name}")
        else:
            print(f"    (no messages)")

        current = month_end

    print(f"\n  Done: {total_messages:,} messages in {total_weeks_saved} new weeks"
          f" ({total_weeks_skipped} skipped)")
    return total_messages, total_weeks_saved


def show_status():
    """Show what's been pulled."""
    if not DATA_DIR.exists():
        print("No raw data pulled yet.")
        return

    print(f"\nRaw message storage: {DATA_DIR}\n")

    total_msgs = 0
    total_weeks = 0

    for channel_dir in sorted(DATA_DIR.iterdir()):
        if not channel_dir.is_dir():
            continue

        weeks = sorted(channel_dir.glob("*.json"))
        channel_msgs = 0
        first_week = None
        last_week = None

        for wk_file in weeks:
            with open(wk_file) as f:
                data = json.load(f)
                channel_msgs += data["message_count"]
            if first_week is None:
                first_week = wk_file.stem
            last_week = wk_file.stem

        print(f"  {channel_dir.name}:")
        print(f"    Weeks: {len(weeks)} ({first_week} → {last_week})")
        print(f"    Messages: {channel_msgs:,}")
        total_msgs += channel_msgs
        total_weeks += len(weeks)

    print(f"\n  Total: {total_msgs:,} messages in {total_weeks} week-files")


def main():
    if len(sys.argv) > 1 and sys.argv[1] == "--status":
        show_status()
        return

    # Determine which channels to pull
    if len(sys.argv) > 1 and sys.argv[1] in CHANNEL_NAME_TO_ID:
        channel_name = sys.argv[1]
        channels = {CHANNEL_NAME_TO_ID[channel_name]: channel_name}
    else:
        channels = WAN_CHANNELS

    # Optional month filter
    month_filter = None
    if len(sys.argv) > 2 and len(sys.argv[2]) == 7:  # YYYY-MM
        month_filter = sys.argv[2]

    grand_total_msgs = 0
    grand_total_weeks = 0

    for channel_id, channel_name in channels.items():
        msgs, weeks = pull_channel(channel_name, channel_id, month_filter)
        grand_total_msgs += msgs
        grand_total_weeks += weeks

    print(f"\n{'='*60}")
    print(f"GRAND TOTAL: {grand_total_msgs:,} messages in {grand_total_weeks} week-files")
    print(f"Storage: {DATA_DIR}")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()
