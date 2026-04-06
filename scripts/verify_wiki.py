#!/usr/bin/env python3
"""
Verify wiki pages against raw Discord messages using GPT-5.4.

Cross-model verification: wiki pages are compiled by Claude, verified by GPT-5.4.
This catches capability conflation, model confusion, and other errors that the
same model tends to rubber-stamp.

Usage:
    python verify_wiki.py wiki/wan/models/wananimate.md          # Verify one page
    python verify_wiki.py wiki/wan/models/wananimate.md --fix    # Verify and apply fixes
    python verify_wiki.py wiki/wan/models/wananimate.md --weeks 2025-W38,2025-W39  # Specific weeks
    python verify_wiki.py wiki/wan/models/wananimate.md --top 5  # Use top N weeks by mention count

Pulls relevant raw messages based on the page topic, sends to GPT-5.4 for
fact-checking against the wiki content.
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

import functools
print = functools.partial(print, flush=True)

OPENAI_KEY = os.environ.get("OPENAI_KEY", "")
if not OPENAI_KEY:
    print("Error: OPENAI_KEY not set in .env or environment")
    sys.exit(1)

RAW_DIR = Path(__file__).parent.parent / "data" / "raw"
WIKI_DIR = Path(__file__).parent.parent / "wiki"

# Model for verification
VERIFY_MODEL = "gpt-5.4"

# Channels to search for relevant messages
ALL_CHANNELS = ["wan_chatter", "wan_comfyui", "wan_training", "wan_gens", "wan_resources"]


def extract_topic_terms(wiki_path):
    """Extract search terms from a wiki page's title and aliases."""
    content = wiki_path.read_text()

    terms = []

    # Get title from frontmatter
    title_match = re.search(r'^title:\s*(.+)$', content, re.MULTILINE)
    if title_match:
        terms.append(title_match.group(1).strip())

    # Get aliases from frontmatter
    alias_match = re.search(r'^aliases:\s*\[(.+)\]$', content, re.MULTILINE)
    if alias_match:
        aliases = [a.strip().strip('"').strip("'") for a in alias_match.group(1).split(',')]
        terms.extend(aliases)

    # Deduplicate and lowercase
    seen = set()
    unique = []
    for t in terms:
        low = t.lower()
        if low not in seen:
            seen.add(low)
            unique.append(low)

    return unique


def find_relevant_weeks(topic_terms, channels=None, top_n=10):
    """Find weeks with the most mentions of topic terms across channels."""
    channels = channels or ALL_CHANNELS
    week_counts = {}  # week_label -> {channel -> count}

    for channel in channels:
        channel_dir = RAW_DIR / channel
        if not channel_dir.exists():
            continue

        for week_file in sorted(channel_dir.glob("*.json")):
            with open(week_file) as f:
                data = json.load(f)

            count = 0
            for msg in data["messages"]:
                content = (msg.get("content") or "").lower()
                if any(term in content for term in topic_terms):
                    count += 1

            if count > 0:
                wk = week_file.stem
                if wk not in week_counts:
                    week_counts[wk] = {}
                week_counts[wk][channel] = count

    # Sort by total mentions across channels
    ranked = sorted(
        week_counts.items(),
        key=lambda x: sum(x[1].values()),
        reverse=True
    )

    return ranked[:top_n]


def load_relevant_messages(topic_terms, week_label, channels=None, include_context=True):
    """Load messages mentioning the topic from a specific week, with reply context."""
    channels = channels or ALL_CHANNELS
    messages = []
    all_messages_by_id = {}  # For reply chain lookup

    for channel in channels:
        week_file = RAW_DIR / channel / f"{week_label}.json"
        if not week_file.exists():
            continue

        with open(week_file) as f:
            data = json.load(f)

        # Index all messages for reply chain lookup
        for msg in data["messages"]:
            all_messages_by_id[msg["message_id"]] = msg

        # Find messages mentioning the topic
        for msg in data["messages"]:
            content = (msg.get("content") or "").lower()
            if any(term in content for term in topic_terms):
                messages.append(msg)

    # Add reply context: if a relevant message is a reply, include the parent
    if include_context:
        extra = []
        for msg in messages:
            ref_id = msg.get("reference_id")
            if ref_id and ref_id in all_messages_by_id:
                parent = all_messages_by_id[ref_id]
                parent["_is_reply_context"] = True
                extra.append(parent)
        messages.extend(extra)

    # Deduplicate and sort by time
    seen_ids = set()
    unique = []
    for msg in messages:
        mid = msg["message_id"]
        if mid not in seen_ids:
            seen_ids.add(mid)
            unique.append(msg)
    unique.sort(key=lambda m: m["created_at"])

    return unique


def format_messages_for_verification(messages, max_tokens_approx=80000):
    """Format raw messages into a readable block for the verifier."""
    lines = []
    approx_tokens = 0

    for msg in messages:
        author = msg.get("author_name", "Unknown")
        content = msg.get("content", "")
        ts = msg.get("created_at", "")[:16]  # Trim to minute
        reactions = msg.get("reactions", [])
        ref_id = msg.get("reference_id")
        is_context = msg.get("_is_reply_context", False)

        if not content.strip():
            continue

        prefix = "[REPLY-CONTEXT] " if is_context else ""
        reply_note = f" [replying to msg]" if ref_id and not is_context else ""

        reaction_str = ""
        if reactions:
            emoji_counts = {}
            for r in reactions:
                e = r.get("emoji", "?")
                emoji_counts[e] = emoji_counts.get(e, 0) + 1
            reaction_str = " | reactions: " + " ".join(
                f"{e}x{c}" if c > 1 else e for e, c in emoji_counts.items()
            )

        line = f"{prefix}[{ts}] {author}{reply_note}: {content}{reaction_str}"
        lines.append(line)

        approx_tokens += len(line) // 3
        if approx_tokens > max_tokens_approx:
            lines.append(f"\n... (truncated, {len(messages) - len(lines)} more messages)")
            break

    return "\n".join(lines)


VERIFICATION_PROMPT = """You are fact-checking a wiki page about {topic} against raw Discord messages.

The wiki page was compiled by a different AI (Claude) from summarized extraction files. Those summaries are lossy — they sometimes strip context about which model a capability belongs to, especially when Discord conversations discuss multi-model workflows.

Your job is to catch GENUINE ERRORS, not to rewrite or nitpick. The page is generally well-structured and mostly correct. Focus specifically on:

## Error Types to Check

1. **CAPABILITY CONFLATION** (most important): Is each capability attributed to the correct model?
   In Discord, people often discuss multi-model workflows. "I used VACE canny with WanAnimate" does NOT mean WanAnimate uses canny — it means VACE provides canny input to a WanAnimate pipeline.
   CHECK REPLY CHAINS: A message saying "use inverted canny" might be replying to a question about VACE, not about {topic}.

2. **MODEL CONFUSION**: Features from one Wan model (2.1, 2.2, VACE, Phantom, etc.) incorrectly attributed to {topic}.

3. **UNSUPPORTED CLAIMS**: Claims not present in the source messages, or claims that received pushback (look for negative emoji reactions like 💀 or disagreement in replies).

4. **MISINTERPRETATION**: Questions treated as statements, sarcasm missed, jokes taken as advice.

5. **INVENTED DETAILS**: Specific numbers, versions, or settings not found in the source messages.

6. **OPINION AS CONSENSUS**: One person's preference presented as community agreement. Look at reaction counts — a message with 🔥 reactions has more community validation than an unreacted comment.

## Important Context

The Wan ecosystem has many models that are often used together:
- **VACE**: Handles canny, depth, inpainting, outpainting, style transfer
- **WanAnimate**: Handles pose-driven character animation via VitPose/DWPose
- **Phantom**: Handles subject consistency via reference images
- **Wan 2.1 / 2.2**: Base generation models (T2V, I2V)
- **Fun Control**: Camera and structural control

When a Discord message discusses a pipeline involving multiple models, be very careful about which capability belongs to which model.

## Output Format

Return a JSON object with this structure:
```json
{{
  "issues": [
    {{
      "type": "capability_conflation|model_confusion|unsupported|misinterpretation|invented|opinion_as_consensus",
      "severity": "high|medium|low",
      "wiki_claim": "The exact text from the wiki that is wrong or suspect",
      "evidence": "What the raw messages actually say (quote relevant messages)",
      "correction": "What the wiki should say instead",
      "confidence": "high|medium|low"
    }}
  ],
  "verified_ok": ["List of specific claims/sections that ARE well-supported by the evidence"],
  "summary": "Brief overall assessment"
}}
```

Only report issues you are confident about. Do NOT flag things just because you can't find evidence — absence in this week's messages doesn't mean a claim is wrong (it may come from a different week). Only flag things where the evidence CONTRADICTS the wiki or where you can see the conflation happening in the conversation context."""


def call_gpt54(system_prompt, user_content, model=VERIFY_MODEL):
    """Call GPT-5.4 for verification."""
    resp = requests.post(
        "https://api.openai.com/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {OPENAI_KEY}",
            "Content-Type": "application/json",
        },
        json={
            "model": model,
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_content},
            ],
            "temperature": 0.2,
            "response_format": {"type": "json_object"},
        },
        timeout=120,
    )

    if resp.status_code != 200:
        print(f"GPT-5.4 error {resp.status_code}: {resp.text[:300]}")
        return None

    data = resp.json()
    usage = data.get("usage", {})
    print(f"  Tokens — input: {usage.get('prompt_tokens', '?')}, "
          f"output: {usage.get('completion_tokens', '?')}, "
          f"reasoning: {usage.get('completion_tokens_details', {}).get('reasoning_tokens', '?')}")

    content = data["choices"][0]["message"]["content"]
    try:
        return json.loads(content)
    except json.JSONDecodeError:
        print(f"  Warning: Could not parse JSON response")
        print(f"  Raw: {content[:500]}")
        return {"raw_response": content}


def verify_page(wiki_path, week_labels=None, top_n=5, apply_fixes=False):
    """Verify a wiki page against raw messages."""
    wiki_path = Path(wiki_path)
    if not wiki_path.exists():
        print(f"Error: {wiki_path} not found")
        return

    wiki_content = wiki_path.read_text()
    topic_terms = extract_topic_terms(wiki_path)

    print(f"Verifying: {wiki_path.name}")
    print(f"Topic terms: {topic_terms}")

    # Find relevant weeks
    if week_labels:
        weeks_to_check = [(wk, {"manual": 0}) for wk in week_labels]
    else:
        print(f"\nFinding top {top_n} weeks by mention count...")
        weeks_to_check = find_relevant_weeks(topic_terms, top_n=top_n)
        for wk, channels in weeks_to_check:
            total = sum(channels.values())
            ch_str = ", ".join(f"{c}:{n}" for c, n in sorted(channels.items(), key=lambda x: -x[1]))
            print(f"  {wk}: {total} mentions ({ch_str})")

    # Verify against each week
    all_issues = []
    all_verified = []

    for wk_label, _ in weeks_to_check:
        if isinstance(wk_label, tuple):
            wk_label = wk_label[0]

        print(f"\n{'='*60}")
        print(f"Verifying against {wk_label}...")

        messages = load_relevant_messages(topic_terms, wk_label)
        if not messages:
            print(f"  No relevant messages found, skipping")
            continue

        print(f"  {len(messages)} relevant messages (incl. reply context)")

        formatted = format_messages_for_verification(messages)

        system_prompt = VERIFICATION_PROMPT.format(topic=topic_terms[0] if topic_terms else "unknown")

        user_content = f"""## Wiki Page to Verify

```markdown
{wiki_content}
```

## Raw Discord Messages from {wk_label}

These are actual Discord messages from the community. Messages prefixed with [REPLY-CONTEXT] are parent messages that a relevant message was replying to — use them to understand what topic a reply is about.

```
{formatted}
```

Please fact-check the wiki page against these raw messages. Return your findings as JSON."""

        result = call_gpt54(system_prompt, user_content)

        if result and "issues" in result:
            issues = result["issues"]
            verified = result.get("verified_ok", [])
            summary = result.get("summary", "")

            print(f"\n  Summary: {summary}")
            print(f"  Issues found: {len(issues)}")
            print(f"  Claims verified OK: {len(verified)}")

            for i, issue in enumerate(issues):
                severity = issue.get("severity", "?")
                itype = issue.get("type", "?")
                conf = issue.get("confidence", "?")
                marker = "🔴" if severity == "high" else "🟡" if severity == "medium" else "⚪"
                print(f"\n  {marker} Issue {i+1} [{itype}] (severity: {severity}, confidence: {conf})")
                print(f"     Wiki says: {issue.get('wiki_claim', '?')[:200]}")
                print(f"     Evidence: {issue.get('evidence', '?')[:200]}")
                print(f"     Fix: {issue.get('correction', '?')[:200]}")

            all_issues.extend(issues)
            all_verified.extend(verified)
        elif result:
            print(f"  Unexpected response format: {str(result)[:300]}")

    # Summary
    print(f"\n{'='*60}")
    print(f"VERIFICATION COMPLETE: {wiki_path.name}")
    print(f"{'='*60}")
    print(f"Weeks checked: {len(weeks_to_check)}")
    print(f"Total issues: {len(all_issues)}")

    high = sum(1 for i in all_issues if i.get("severity") == "high")
    medium = sum(1 for i in all_issues if i.get("severity") == "medium")
    low = sum(1 for i in all_issues if i.get("severity") == "low")
    print(f"  High: {high}, Medium: {medium}, Low: {low}")
    print(f"Claims verified OK: {len(all_verified)}")

    # Save report
    report_dir = Path(__file__).parent.parent / "wiki" / "_meta" / "verification"
    report_dir.mkdir(parents=True, exist_ok=True)
    report_path = report_dir / f"{wiki_path.stem}_verification.json"

    report = {
        "page": str(wiki_path),
        "verified_at": datetime.now().isoformat(),
        "model": VERIFY_MODEL,
        "weeks_checked": [w[0] if isinstance(w[0], str) else w[0] for w, _ in weeks_to_check],
        "issues": all_issues,
        "verified_ok": all_verified,
        "summary": {
            "total_issues": len(all_issues),
            "high": high,
            "medium": medium,
            "low": low,
            "verified_claims": len(all_verified),
        },
    }

    with open(report_path, "w") as f:
        json.dump(report, f, indent=2, ensure_ascii=False)
    print(f"\nReport saved: {report_path}")

    return report


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    wiki_path = sys.argv[1]
    apply_fixes = "--fix" in sys.argv
    top_n = 5

    # Parse --top N
    if "--top" in sys.argv:
        idx = sys.argv.index("--top")
        if idx + 1 < len(sys.argv):
            top_n = int(sys.argv[idx + 1])

    # Parse --weeks W38,W39
    week_labels = None
    if "--weeks" in sys.argv:
        idx = sys.argv.index("--weeks")
        if idx + 1 < len(sys.argv):
            week_labels = sys.argv[idx + 1].split(",")

    verify_page(wiki_path, week_labels=week_labels, top_n=top_n, apply_fixes=apply_fixes)


if __name__ == "__main__":
    main()
