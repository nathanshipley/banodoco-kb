#!/usr/bin/env python3
"""
Extract knowledge from chat messages using chunked summarization.
Processes messages in time-ordered chunks to capture all types of knowledge.

Usage: python extract_chat_chunks.py <channel_name> <start_date> <end_date> [chunk_size]
Example: python extract_chat_chunks.py ltx_chatter 2026-01-06 2026-01-07 300
"""

import requests
import json
import os
import sys
from datetime import datetime
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

import anthropic

API_URL = "https://ujlwuvkrxlvoswwkerdf.supabase.co/rest/v1"
API_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InVqbHd1dmtyeGx2b3N3d2tlcmRmIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NjczNzcyMzcsImV4cCI6MjA4MjczNzIzN30.XSTztghf_6a_bpR62wZdoA4S4oafJFDMoPQDRR4dT08"
headers = {"apikey": API_KEY}

CHANNELS = {
    "ltx_chatter": 1309520535012638740,
    "ltx_training": 1457981700817817620,
    "ltx_resources": 1457981813120176138,
    "ltx_gens": 1458032975982755861,
    "wan_chatter": 1342763350815277067,
}


def fetch_messages(channel_id, start_date, end_date, limit=10000):
    """Fetch messages from a channel within a date range."""
    messages = []
    offset = 0
    batch_size = 1000

    while len(messages) < limit:
        url = f"{API_URL}/discord_messages?channel_id=eq.{channel_id}&created_at=gte.{start_date}&created_at=lt.{end_date}&select=message_id,author_id,content,created_at,reaction_count,attachments&order=created_at.asc&offset={offset}&limit={batch_size}"
        resp = requests.get(url, headers=headers)
        data = resp.json()

        if not data:
            break

        messages.extend(data)
        offset += batch_size

        if len(data) < batch_size:
            break

    return messages


def fetch_author_names(author_ids):
    """Fetch usernames for author IDs."""
    names = {}
    unique_ids = list(set(author_ids))[:200]  # Limit API calls

    for aid in unique_ids:
        url = f"{API_URL}/discord_members?member_id=eq.{aid}&select=global_name,username"
        resp = requests.get(url, headers=headers)
        if resp.json():
            m = resp.json()[0]
            names[aid] = m.get('global_name') or m.get('username') or str(aid)

    return names


def format_chunk_for_llm(messages, names):
    """Format a chunk of messages for LLM processing."""
    lines = []

    for msg in messages:
        author = names.get(msg['author_id'], str(msg['author_id']))
        content = msg.get('content', '').strip()
        reactions = msg.get('reaction_count', 0)
        attachments = msg.get('attachments', [])

        if not content and not attachments:
            continue

        # Format: [Author] (reactions if any): content
        reaction_str = f" ({reactions}★)" if reactions >= 2 else ""
        attachment_str = f" [+{len(attachments)} files]" if attachments else ""

        lines.append(f"[{author}]{reaction_str}{attachment_str}: {content}")

    return "\n".join(lines)


def extract_knowledge_from_chunk(chunk_content, channel_name, chunk_num, model_context=""):
    """Use Claude to extract all valuable knowledge from a chunk."""

    client = anthropic.Anthropic()

    prompt = f"""You are analyzing a chunk of Discord chat from the "{channel_name}" channel of the Banodoco community. This community focuses on open source AI video/image generation.

{model_context}

Your task: Extract ALL valuable knowledge from this discussion into these categories:

1. **Technical discoveries** - Settings, parameters, techniques that work well
2. **Troubleshooting** - Problems encountered and solutions found
3. **Model comparisons** - How this compares to other models (quality, speed, features)
4. **Tips and best practices** - Advice shared by experienced users
5. **News and updates** - New releases, updates, announcements
6. **Workflows** - How people are using the model, pipelines that work
7. **Settings** - Specific parameter values and configurations
8. **Concepts explained** - Technical terms or concepts clarified
9. **Resources** - Links to models, repos, Civitai, HuggingFace, workflows shared
10. **Limitations** - What the model can't do well, known issues, failure cases
11. **Hardware** - VRAM requirements, RAM needs, GPU compatibility, performance benchmarks
12. **Community creations** - LoRAs, custom nodes, tools, scripts people have made

QUALITY SIGNALS:
- Messages marked with (★) have community reactions - these often indicate valuable/accurate info
- However, don't exclude good information just because it lacks reactions
- Prioritize concrete, specific information over vague statements

IMPORTANT - Accuracy guidelines:
- Do NOT jump to conclusions unsupported by the actual messages
- Only include information that is explicitly stated or clearly demonstrated
- Distinguish between confirmed facts and speculation/opinions
- If someone speculates, note it as speculation
- Skip unsubstantiated claims, jokes, casual chat, off-topic discussion

Output a JSON object:
{{
  "discoveries": [
    {{"finding": "what was discovered", "details": "specifics", "from": "username"}}
  ],
  "troubleshooting": [
    {{"problem": "issue", "solution": "fix", "from": "username"}}
  ],
  "comparisons": [
    {{"comparison": "X vs Y", "verdict": "conclusion", "from": "username"}}
  ],
  "tips": [
    {{"tip": "the advice", "context": "when it applies", "from": "username"}}
  ],
  "news": [
    {{"update": "what happened", "details": "specifics", "from": "username"}}
  ],
  "workflows": [
    {{"workflow": "description", "use_case": "what it's for", "from": "username"}}
  ],
  "settings": [
    {{"setting": "parameter", "value": "recommended value", "reason": "why", "from": "username"}}
  ],
  "concepts": [
    {{"term": "concept", "explanation": "what it means", "from": "username"}}
  ],
  "resources": [
    {{"resource": "name/description", "url": "link if provided", "type": "model/repo/workflow/tool", "from": "username"}}
  ],
  "limitations": [
    {{"limitation": "what doesn't work", "details": "specifics", "from": "username"}}
  ],
  "hardware": [
    {{"requirement": "hardware aspect", "details": "specifics (VRAM, RAM, GPU, speed)", "from": "username"}}
  ],
  "community_creations": [
    {{"creation": "name", "type": "lora/node/tool/workflow", "description": "what it does", "from": "username"}}
  ]
}}

If a category has no relevant entries, use an empty array.

Here's the chat chunk:

{chunk_content}

Return ONLY the JSON object."""

    message = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=4000,
        messages=[{"role": "user", "content": prompt}]
    )

    return message.content[0].text, message.usage


def merge_knowledge(all_knowledge):
    """Merge knowledge from multiple chunks, deduplicating."""
    merged = {
        "discoveries": [],
        "troubleshooting": [],
        "comparisons": [],
        "tips": [],
        "news": [],
        "workflows": [],
        "settings": [],
        "concepts": [],
        "resources": [],
        "limitations": [],
        "hardware": [],
        "community_creations": []
    }

    for chunk_knowledge in all_knowledge:
        for key in merged.keys():
            if key in chunk_knowledge:
                merged[key].extend(chunk_knowledge[key])

    return merged


def knowledge_to_markdown(knowledge, channel_name, date_range):
    """Convert extracted knowledge to clean markdown for NotebookLM."""
    lines = [
        f"# {channel_name.replace('_', ' ').title()} Knowledge Base",
        f"*Extracted from Discord discussions: {date_range}*\n",
    ]

    section_titles = {
        "discoveries": "Technical Discoveries",
        "troubleshooting": "Troubleshooting & Solutions",
        "comparisons": "Model Comparisons",
        "tips": "Tips & Best Practices",
        "news": "News & Updates",
        "workflows": "Workflows & Use Cases",
        "settings": "Recommended Settings",
        "concepts": "Concepts Explained",
        "resources": "Resources & Links",
        "limitations": "Known Limitations",
        "hardware": "Hardware Requirements",
        "community_creations": "Community Creations"
    }

    for key, title in section_titles.items():
        items = knowledge.get(key, [])
        if not items:
            continue

        lines.append(f"\n## {title}\n")

        for item in items:
            if key == "discoveries":
                lines.append(f"- **{item.get('finding', '')}**")
                if item.get('details'):
                    lines.append(f"  - {item['details']}")
                if item.get('from'):
                    lines.append(f"  - *From: {item['from']}*")
            elif key == "troubleshooting":
                lines.append(f"- **Problem:** {item.get('problem', '')}")
                lines.append(f"  - **Solution:** {item.get('solution', '')}")
                if item.get('from'):
                    lines.append(f"  - *From: {item['from']}*")
            elif key == "comparisons":
                lines.append(f"- **{item.get('comparison', '')}**")
                lines.append(f"  - {item.get('verdict', '')}")
                if item.get('from'):
                    lines.append(f"  - *From: {item['from']}*")
            elif key == "tips":
                lines.append(f"- **{item.get('tip', '')}**")
                if item.get('context'):
                    lines.append(f"  - Context: {item['context']}")
                if item.get('from'):
                    lines.append(f"  - *From: {item['from']}*")
            elif key == "news":
                lines.append(f"- **{item.get('update', '')}**")
                if item.get('details'):
                    lines.append(f"  - {item['details']}")
                if item.get('from'):
                    lines.append(f"  - *From: {item['from']}*")
            elif key == "workflows":
                lines.append(f"- **{item.get('workflow', '')}**")
                if item.get('use_case'):
                    lines.append(f"  - Use case: {item['use_case']}")
                if item.get('from'):
                    lines.append(f"  - *From: {item['from']}*")
            elif key == "settings":
                lines.append(f"- **{item.get('setting', '')}**: {item.get('value', '')}")
                if item.get('reason'):
                    lines.append(f"  - {item['reason']}")
                if item.get('from'):
                    lines.append(f"  - *From: {item['from']}*")
            elif key == "concepts":
                lines.append(f"- **{item.get('term', '')}**: {item.get('explanation', '')}")
                if item.get('from'):
                    lines.append(f"  - *From: {item['from']}*")
            elif key == "resources":
                lines.append(f"- **{item.get('resource', '')}** ({item.get('type', 'resource')})")
                if item.get('url'):
                    lines.append(f"  - {item['url']}")
                if item.get('from'):
                    lines.append(f"  - *From: {item['from']}*")
            elif key == "limitations":
                lines.append(f"- **{item.get('limitation', '')}**")
                if item.get('details'):
                    lines.append(f"  - {item['details']}")
                if item.get('from'):
                    lines.append(f"  - *From: {item['from']}*")
            elif key == "hardware":
                lines.append(f"- **{item.get('requirement', '')}**")
                if item.get('details'):
                    lines.append(f"  - {item['details']}")
                if item.get('from'):
                    lines.append(f"  - *From: {item['from']}*")
            elif key == "community_creations":
                lines.append(f"- **{item.get('creation', '')}** ({item.get('type', '')})")
                if item.get('description'):
                    lines.append(f"  - {item['description']}")
                if item.get('from'):
                    lines.append(f"  - *From: {item['from']}*")

            lines.append("")

    return "\n".join(lines)


def main():
    if len(sys.argv) < 4:
        print("Usage: python extract_chat_chunks.py <channel_name> <start_date> <end_date> [chunk_size]")
        print("Example: python extract_chat_chunks.py ltx_chatter 2026-01-06 2026-01-07 300")
        return

    channel_name = sys.argv[1]
    start_date = sys.argv[2]
    end_date = sys.argv[3]
    chunk_size = int(sys.argv[4]) if len(sys.argv) > 4 else 300

    if channel_name not in CHANNELS:
        print(f"Unknown channel: {channel_name}")
        print(f"Available: {list(CHANNELS.keys())}")
        return

    channel_id = CHANNELS[channel_name]

    # Model context for LTX
    model_context = ""
    if "ltx" in channel_name.lower():
        model_context = "This discussion is about LTX Video 2, a video generation model released January 5, 2026. It supports text-to-video and image-to-video generation with audio."

    print(f"Fetching messages from {channel_name} ({start_date} to {end_date})...")
    messages = fetch_messages(channel_id, start_date, end_date)
    print(f"Found {len(messages)} messages")

    if not messages:
        print("No messages found!")
        return

    # Get author names
    author_ids = [m['author_id'] for m in messages]
    print("Fetching author names...")
    names = fetch_author_names(author_ids)

    # Process in chunks
    all_knowledge = []
    total_input_tokens = 0
    total_output_tokens = 0

    num_chunks = (len(messages) + chunk_size - 1) // chunk_size
    print(f"\nProcessing {num_chunks} chunks of ~{chunk_size} messages each...")

    for i in range(0, len(messages), chunk_size):
        chunk = messages[i:i + chunk_size]
        chunk_num = i // chunk_size + 1

        print(f"\nChunk {chunk_num}/{num_chunks} ({len(chunk)} messages)...")

        chunk_content = format_chunk_for_llm(chunk, names)
        token_estimate = len(chunk_content) // 4
        print(f"  ~{token_estimate} tokens")

        result, usage = extract_knowledge_from_chunk(chunk_content, channel_name, chunk_num, model_context)
        total_input_tokens += usage.input_tokens
        total_output_tokens += usage.output_tokens

        print(f"  API: {usage.input_tokens} in, {usage.output_tokens} out")

        # Parse result
        try:
            if result.startswith("```"):
                result = result.split("```")[1]
                if result.startswith("json"):
                    result = result[4:]

            chunk_knowledge = json.loads(result)
            all_knowledge.append(chunk_knowledge)

            # Quick summary
            total_items = sum(len(chunk_knowledge.get(k, [])) for k in chunk_knowledge)
            print(f"  Extracted {total_items} items")

        except json.JSONDecodeError as e:
            print(f"  Error parsing JSON: {e}")
            continue

    # Merge all knowledge
    print("\n" + "="*60)
    print("MERGING KNOWLEDGE")
    print("="*60)

    merged = merge_knowledge(all_knowledge)

    # Summary
    print("\nExtracted:")
    for key, items in merged.items():
        if items:
            print(f"  {key}: {len(items)}")

    print(f"\nTotal API usage: {total_input_tokens:,} input, {total_output_tokens:,} output tokens")
    cost_estimate = (total_input_tokens * 3 + total_output_tokens * 15) / 1_000_000
    print(f"Estimated cost: ${cost_estimate:.2f}")

    # Save JSON
    script_dir = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.join(script_dir, '..', 'data')

    date_str = start_date.replace('-', '')
    json_path = os.path.join(data_dir, f'{channel_name}_{date_str}_knowledge.json')
    with open(json_path, 'w') as f:
        json.dump({
            'channel': channel_name,
            'date_range': f"{start_date} to {end_date}",
            'messages_processed': len(messages),
            'chunks_processed': num_chunks,
            'api_usage': {
                'input_tokens': total_input_tokens,
                'output_tokens': total_output_tokens,
                'estimated_cost': cost_estimate
            },
            'extracted_at': datetime.utcnow().isoformat() + 'Z',
            **merged
        }, f, indent=2)
    print(f"\nSaved JSON: {json_path}")

    # Save Markdown (for NotebookLM)
    md_content = knowledge_to_markdown(merged, channel_name, f"{start_date} to {end_date}")
    md_path = os.path.join(data_dir, f'{channel_name}_{date_str}_knowledge.md')
    with open(md_path, 'w') as f:
        f.write(md_content)
    print(f"Saved Markdown: {md_path}")


if __name__ == "__main__":
    main()
