#!/usr/bin/env python3
"""
Compile raw Discord messages into wiki pages, one week at a time.

Processes messages chronologically. For each week:
1. Load raw messages from all channels
2. Load current wiki page state
3. Send to Claude Sonnet for compilation
4. Write updated wiki pages

Usage:
    python compile_weekly.py 2025-W08                  # Process one week
    python compile_weekly.py 2025-W08 2025-W12         # Process a range
    python compile_weekly.py --next 3                   # Process next 3 unprocessed weeks
    python compile_weekly.py --status                   # Show progress

Cost: ~$0.10-0.50 per week depending on message volume (Sonnet pricing).
"""

import requests
import json
import os
import sys
import re
from datetime import datetime
from pathlib import Path

# Load .env
env_path = Path(__file__).parent.parent / '.env'
if env_path.exists():
    with open(env_path) as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith('#') and '=' in line:
                key, value = line.split('=', 1)
                os.environ[key] = value

import anthropic

import functools
print = functools.partial(print, flush=True)

RAW_DIR = Path(__file__).parent.parent / "data" / "raw"
WIKI_DIR = Path(__file__).parent.parent / "wiki"
STATE_FILE = WIKI_DIR / "_meta" / "weekly-compile-state.json"

ALL_CHANNELS = ["wan_chatter", "wan_comfyui", "wan_training", "wan_gens", "wan_resources"]

# Use Sonnet for compilation (good quality, 10x cheaper than Opus)
COMPILE_MODEL = "claude-sonnet-4-5-20250929"
MAX_MESSAGES_PER_CHUNK = 500  # Split large weeks into chunks


def load_state():
    if STATE_FILE.exists():
        with open(STATE_FILE) as f:
            return json.load(f)
    return {"weeks_processed": [], "last_week": None}


def save_state(state):
    STATE_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(STATE_FILE, 'w') as f:
        json.dump(state, f, indent=2)


def get_all_weeks():
    """Get sorted list of all available weeks across all channels."""
    weeks = set()
    for ch_dir in RAW_DIR.iterdir():
        if ch_dir.is_dir():
            for f in ch_dir.glob("*.json"):
                weeks.add(f.stem)
    return sorted(weeks)


def load_week_messages(week_label):
    """Load all messages for a week across all channels."""
    messages = []
    for channel in ALL_CHANNELS:
        week_file = RAW_DIR / channel / f"{week_label}.json"
        if not week_file.exists():
            continue
        with open(week_file) as f:
            data = json.load(f)
        for msg in data["messages"]:
            msg["_channel"] = channel
        messages.extend(data["messages"])

    # Sort by timestamp
    messages.sort(key=lambda m: m.get("created_at", ""))
    return messages


def load_current_wiki():
    """Load all current wiki page contents."""
    pages = {}
    for md_file in WIKI_DIR.rglob("*.md"):
        # Skip meta files
        rel = md_file.relative_to(WIKI_DIR)
        if str(rel).startswith("_meta"):
            continue
        pages[str(rel)] = md_file.read_text()
    return pages


def format_messages_for_compilation(messages, max_messages=None):
    """Format raw messages into readable text for Claude."""
    lines = []
    msg_list = messages[:max_messages] if max_messages else messages

    for msg in msg_list:
        author = msg.get("author_name", "Unknown")
        content = msg.get("content", "")
        ts = msg.get("created_at", "")[:16]
        channel = msg.get("_channel", "unknown")
        reactions = msg.get("reactions", [])
        ref_id = msg.get("reference_id")
        is_pinned = msg.get("is_pinned", False)

        if not content.strip():
            continue

        # Build context markers
        markers = []
        if is_pinned:
            markers.append("📌PINNED")
        if ref_id:
            markers.append(f"↩reply-to:{ref_id}")

        reaction_str = ""
        if reactions:
            emoji_counts = {}
            for r in reactions:
                e = r.get("emoji", "?")
                emoji_counts[e] = emoji_counts.get(e, 0) + 1
            reaction_str = " [" + " ".join(
                f"{e}x{c}" if c > 1 else e for e, c in emoji_counts.items()
            ) + "]"

        marker_str = f" ({', '.join(markers)})" if markers else ""
        line = f"[{ts}] #{channel} {author}{marker_str}: {content}{reaction_str}"
        lines.append(line)

    return "\n".join(lines)


COMPILATION_SYSTEM_PROMPT = """You are building a wiki about the Wan video generation ecosystem by reading Discord community conversations.

You will receive:
1. Raw Discord messages from one week
2. The current state of all wiki pages (may be empty if this is the first week)

Your job: Read the conversations and update the wiki pages with any knowledge worth capturing.

## Wiki Structure

Pages go under wiki/wan/ in these categories:
- models/ — one page per model (wan-2.1.md, wan-2.2.md, vace.md, phantom.md, wananimate.md, humo.md, multitalk.md, infinitetalk.md, magref.md, echoshot.md, lynx.md, recammaster.md, svi.md, etc.)
- techniques/ — usage techniques (t2v.md, i2v.md, inpainting.md, video-extension.md, style-transfer.md, lora-usage.md)
- optimization/ — speed, memory, ComfyUI (speed.md, quantization.md, comfyui.md)
- training/ — LoRA training, embeddings (lora-training.md, embedding.md)
- Top-level: overview.md, choosing-a-model.md, hardware.md, troubleshooting.md, resources.md

Create pages on demand — only when there's enough content to justify one.

## Page Format

```markdown
---
title: Page Title
aliases: [alias1, alias2]
last_updated: YYYY-MM-DD
---

# Title

Overview paragraph.

## Sections...
```

Use wikilinks: [[wan-2.1]], [[vace]], etc.
Attribution: "— #channel, Author, Week YYYY-WNN" for notable claims.
Tables for settings, comparisons, hardware.

## CRITICAL RULES

1. **Attribute capabilities to the correct model.** Discord conversations discuss multi-model pipelines. "I used VACE canny with WanAnimate" means VACE handles canny, NOT WanAnimate. Read reply chains to understand context.

2. **Use reaction signals.** 🔥/❤️/👍 = community validates. 💀/😂 = joke/sarcasm. 💩/❌ = disagrees. High-reaction messages are higher-signal.

3. **Distinguish fact from opinion.** One person's preference is not consensus. Use "some users reported" or attribute by name for individual opinions.

4. **Preserve specific numbers** — step counts, CFG values, VRAM figures, resolution recommendations.

5. **Don't invent.** Only write what the messages actually say. If you're unsure which model something belongs to, note the ambiguity rather than guessing.

6. **Reply chains matter.** A message saying "use inverted canny" that's replying to a VACE question is about VACE, not whatever model was mentioned 5 messages earlier.

## Output Format

Return a JSON object:
```json
{
  "pages": {
    "wan/models/wan-2.1.md": "full page content here...",
    "wan/models/vace.md": "full page content here..."
  },
  "new_pages_created": ["wan/models/wan-2.1.md"],
  "pages_updated": ["wan/models/vace.md"],
  "summary": "Brief description of what was learned this week"
}
```

Include the FULL content of each page you create or update (not just the diff).
Only include pages that changed. If nothing noteworthy happened, return empty pages dict."""


def compile_week(week_label, messages, current_wiki, client):
    """Send messages + wiki state to Claude for compilation."""

    formatted = format_messages_for_compilation(messages)

    # Build wiki state summary
    wiki_state = ""
    if current_wiki:
        wiki_state = "## Current Wiki Pages\n\n"
        for path, content in sorted(current_wiki.items()):
            wiki_state += f"### {path}\n```markdown\n{content}\n```\n\n"
    else:
        wiki_state = "## Current Wiki Pages\n\n(No pages exist yet — this is the first week.)\n\n"

    user_content = f"""{wiki_state}## Discord Messages from {week_label}

{len(messages)} messages across Wan ecosystem channels.

```
{formatted}
```

Read through these conversations and update the wiki. Return your changes as JSON."""

    # Check approximate token count (rough: 1 token ≈ 4 chars)
    approx_tokens = len(user_content) // 4
    print(f"  Approximate input: ~{approx_tokens:,} tokens")

    response = client.messages.create(
        model=COMPILE_MODEL,
        max_tokens=16000,
        system=COMPILATION_SYSTEM_PROMPT,
        messages=[{"role": "user", "content": user_content}],
        temperature=0.2,
    )

    # Extract text content
    text = ""
    for block in response.content:
        if block.type == "text":
            text += block.text

    usage = response.usage
    print(f"  Tokens — input: {usage.input_tokens:,}, output: {usage.output_tokens:,}")

    # Calculate cost (Sonnet pricing: $3/M input, $15/M output)
    cost = (usage.input_tokens * 3 + usage.output_tokens * 15) / 1_000_000
    print(f"  Cost: ${cost:.3f}")

    # Parse JSON from response
    # Try to find JSON in the response
    json_match = re.search(r'\{[\s\S]*\}', text)
    if json_match:
        try:
            return json.loads(json_match.group()), cost
        except json.JSONDecodeError:
            pass

    print(f"  Warning: Could not parse JSON from response")
    print(f"  Response preview: {text[:500]}")
    return None, cost


def process_week(week_label, client, dry_run=False):
    """Process a single week: load messages, compile, write pages."""
    print(f"\n{'='*60}")
    print(f"Processing {week_label}")
    print(f"{'='*60}")

    messages = load_week_messages(week_label)
    if not messages:
        print(f"  No messages found, skipping")
        return 0

    print(f"  Messages: {len(messages)}")

    current_wiki = load_current_wiki()
    print(f"  Current wiki pages: {len(current_wiki)}")

    # For large weeks, we need to chunk
    if len(messages) > MAX_MESSAGES_PER_CHUNK:
        print(f"  Large week — processing in chunks of {MAX_MESSAGES_PER_CHUNK}")
        total_cost = 0
        for i in range(0, len(messages), MAX_MESSAGES_PER_CHUNK):
            chunk = messages[i:i + MAX_MESSAGES_PER_CHUNK]
            chunk_label = f"{week_label} (chunk {i // MAX_MESSAGES_PER_CHUNK + 1})"
            print(f"\n  --- {chunk_label}: {len(chunk)} messages ---")

            result, cost = compile_week(week_label, chunk, current_wiki, client)
            total_cost += cost

            if result and result.get("pages"):
                if not dry_run:
                    write_pages(result["pages"])
                    # Reload wiki for next chunk so it sees previous updates
                    current_wiki = load_current_wiki()

                summary = result.get("summary", "")
                print(f"  Summary: {summary}")

        return total_cost
    else:
        result, cost = compile_week(week_label, messages, current_wiki, client)

        if result and result.get("pages"):
            new_pages = result.get("new_pages_created", [])
            updated = result.get("pages_updated", [])
            summary = result.get("summary", "")

            print(f"  New pages: {new_pages}")
            print(f"  Updated: {updated}")
            print(f"  Summary: {summary}")

            if not dry_run:
                write_pages(result["pages"])

        return cost


def write_pages(pages):
    """Write compiled wiki pages to disk."""
    for rel_path, content in pages.items():
        # Ensure path is under wiki/
        if not rel_path.startswith("wan/"):
            rel_path = f"wan/{rel_path}"

        full_path = WIKI_DIR / rel_path
        full_path.parent.mkdir(parents=True, exist_ok=True)

        # Don't overwrite with empty content
        if not content.strip():
            continue

        full_path.write_text(content)
        print(f"    Wrote: {rel_path} ({len(content)} chars)")


def show_status():
    """Show compilation progress."""
    state = load_state()
    all_weeks = get_all_weeks()
    processed = set(state.get("weeks_processed", []))

    print(f"Total weeks available: {len(all_weeks)}")
    print(f"Weeks processed: {len(processed)}")
    print(f"Remaining: {len(all_weeks) - len(processed)}")

    if processed:
        print(f"Last processed: {state.get('last_week', '?')}")
        print(f"\nProcessed: {', '.join(sorted(processed))}")

    remaining = [w for w in all_weeks if w not in processed]
    if remaining:
        print(f"\nNext up: {', '.join(remaining[:10])}{'...' if len(remaining) > 10 else ''}")


def main():
    if len(sys.argv) > 1 and sys.argv[1] == "--status":
        show_status()
        return

    client = anthropic.Anthropic()

    # Parse arguments
    if "--next" in sys.argv:
        idx = sys.argv.index("--next")
        n = int(sys.argv[idx + 1]) if idx + 1 < len(sys.argv) else 1
        state = load_state()
        processed = set(state.get("weeks_processed", []))
        all_weeks = get_all_weeks()
        weeks_to_process = [w for w in all_weeks if w not in processed][:n]
    elif len(sys.argv) == 2:
        weeks_to_process = [sys.argv[1]]
    elif len(sys.argv) == 3:
        all_weeks = get_all_weeks()
        start, end = sys.argv[1], sys.argv[2]
        weeks_to_process = [w for w in all_weeks if start <= w <= end]
    else:
        print(__doc__)
        return

    if not weeks_to_process:
        print("No weeks to process.")
        return

    print(f"Will process {len(weeks_to_process)} weeks: {', '.join(weeks_to_process)}")

    state = load_state()
    total_cost = 0

    for week_label in weeks_to_process:
        cost = process_week(week_label, client)
        total_cost += cost

        # Update state
        if week_label not in state.get("weeks_processed", []):
            state.setdefault("weeks_processed", []).append(week_label)
        state["last_week"] = week_label
        save_state(state)

    print(f"\n{'='*60}")
    print(f"DONE: {len(weeks_to_process)} weeks processed")
    print(f"Total cost: ${total_cost:.3f}")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()
