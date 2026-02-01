#!/usr/bin/env python3
"""
Prototype: Extract knowledge from a single forum thread.
Fetches a thread from wan_resources and uses Claude to extract structured knowledge.

Usage: python extract_forum_thread.py [thread_id]

Requires: ANTHROPIC_API_KEY in environment or .env file
"""

import requests
import json
import os
import sys
from datetime import datetime

# Load .env file if present
from pathlib import Path
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


def fetch_thread_messages(thread_id):
    """Fetch all messages in a forum thread."""
    url = f"{API_URL}/discord_messages?thread_id=eq.{thread_id}&select=message_id,author_id,content,created_at,reaction_count,attachments&order=created_at.asc"
    resp = requests.get(url, headers=headers)
    return resp.json()


def fetch_author_names(author_ids):
    """Fetch usernames for author IDs."""
    names = {}
    for aid in author_ids[:100]:  # Limit API calls
        url = f"{API_URL}/discord_members?member_id=eq.{aid}&select=global_name,username"
        resp = requests.get(url, headers=headers)
        if resp.json():
            m = resp.json()[0]
            names[aid] = m.get('global_name') or m.get('username') or str(aid)
    return names


def format_thread_for_llm(messages, names):
    """Format thread messages for LLM processing."""
    lines = []

    for i, msg in enumerate(messages):
        author = names.get(msg['author_id'], str(msg['author_id']))
        content = msg.get('content', '').strip()
        reactions = msg.get('reaction_count', 0)
        attachments = msg.get('attachments', [])

        # Skip empty messages with no attachments
        if not content and not attachments:
            continue

        # Format message
        msg_lines = [f"[{author}]" + (f" ({reactions} reactions)" if reactions > 0 else "")]

        if attachments:
            for att in attachments:
                filename = att.get('filename', 'unknown')
                msg_lines.append(f"  Attachment: {filename}")

        if content:
            msg_lines.append(f"  {content}")

        lines.append("\n".join(msg_lines))

    return "\n\n".join(lines)


def extract_knowledge(thread_content, thread_id):
    """Use Claude to extract structured knowledge from the thread."""

    client = anthropic.Anthropic()

    prompt = f"""You are analyzing a Discord forum thread from the Banodoco community, which focuses on open source AI video/image generation tools (Wan, ComfyUI, etc.).

This thread is from the "wan_resources" channel where community members share workflows, LoRAs, and techniques.

Your task: Extract the key knowledge from this thread into a structured format. Focus on:
1. What resource/tool is being shared (LoRA, workflow, technique, etc.)
2. How to use it (settings, requirements, tips)
3. Key technical details mentioned in discussion
4. Common issues or gotchas mentioned
5. Who created/contributed this

Output a JSON object with this structure:
{{
  "resource": {{
    "title": "Name of the resource/technique",
    "type": "lora | workflow | technique | node | script | other",
    "description": "What it does and why it's useful",
    "creator": "Username of the creator",
    "links": ["any URLs mentioned (civitai, github, huggingface, etc.)"]
  }},
  "usage": {{
    "requirements": ["what you need to use this"],
    "recommended_settings": ["specific settings mentioned"],
    "tips": ["tips and best practices from discussion"],
    "workflow_notes": "any workflow-specific guidance"
  }},
  "technical_details": [
    "key technical insights from the discussion"
  ],
  "issues_and_solutions": [
    {{
      "issue": "problem mentioned",
      "solution": "how to fix it"
    }}
  ],
  "related_resources": ["other tools/loras/techniques mentioned"],
  "key_contributors": ["usernames who provided valuable info in discussion"],
  "summary": "2-3 sentence summary of what this thread offers"
}}

Be thorough but concise. Only include information that is actually present in the thread.
Skip any fields that don't have relevant information.

Here's the thread content:

{thread_content}

Return ONLY the JSON object, no other text."""

    print("Sending to Claude for extraction...")

    message = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=4000,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return message.content[0].text, message.usage


def main():
    # Default to the high-value thread we found
    thread_id = int(sys.argv[1]) if len(sys.argv) > 1 else 1428831092181303437

    print(f"Fetching thread {thread_id}...")
    messages = fetch_thread_messages(thread_id)
    print(f"Found {len(messages)} messages")

    # Get author names
    author_ids = list(set(m['author_id'] for m in messages))
    print(f"Fetching names for {len(author_ids)} authors...")
    names = fetch_author_names(author_ids)

    # Format for LLM
    thread_content = format_thread_for_llm(messages, names)
    token_estimate = len(thread_content) // 4
    print(f"Thread content: ~{token_estimate} tokens")

    # Limit thread content to avoid huge API costs (take first ~50K chars)
    if len(thread_content) > 50000:
        print(f"Truncating from {len(thread_content)} to 50000 chars for cost control")
        thread_content = thread_content[:50000] + "\n\n[... thread truncated for processing ...]"

    # Extract knowledge
    result, usage = extract_knowledge(thread_content, thread_id)

    print(f"\nAPI Usage: {usage.input_tokens} input, {usage.output_tokens} output tokens")

    # Parse and pretty print
    try:
        # Handle potential markdown code blocks
        if result.startswith("```"):
            result = result.split("```")[1]
            if result.startswith("json"):
                result = result[4:]

        knowledge = json.loads(result)

        print("\n" + "="*60)
        print("EXTRACTED KNOWLEDGE")
        print("="*60)
        print(json.dumps(knowledge, indent=2))

        # Save to file
        script_dir = os.path.dirname(os.path.abspath(__file__))
        output_path = os.path.join(script_dir, '..', 'data', f'thread_{thread_id}_knowledge.json')
        with open(output_path, 'w') as f:
            json.dump({
                'thread_id': thread_id,
                'extracted_at': datetime.utcnow().isoformat() + 'Z',
                'messages_processed': len(messages),
                'api_usage': {'input_tokens': usage.input_tokens, 'output_tokens': usage.output_tokens},
                **knowledge
            }, f, indent=2)
        print(f"\nSaved to {output_path}")

    except json.JSONDecodeError as e:
        print(f"Error parsing JSON: {e}")
        print("Raw response:")
        print(result[:1000])


if __name__ == "__main__":
    main()
