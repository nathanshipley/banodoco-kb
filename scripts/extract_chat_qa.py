#!/usr/bin/env python3
"""
Prototype: Extract knowledge from chat Q&A threads.
Finds high-value Q&A exchanges and uses Claude to extract structured knowledge.

Usage: python extract_chat_qa.py [channel_name] [limit]
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

# Channel IDs
CHANNELS = {
    "wan_chatter": 1342763350815277067,
    "comfyui": 1151448372549632142,
    "hunyuanvideo": 1310646809621864550,
}


def fetch_high_value_qa(channel_id, limit=50):
    """Fetch Q&A exchanges where answers have high reactions or come from experts."""

    # First, get messages that are replies (have reference_id) with good reactions
    url = f"{API_URL}/discord_messages?channel_id=eq.{channel_id}&reference_id=not.is.null&reaction_count=gte.2&select=message_id,author_id,content,created_at,reaction_count,reference_id&order=reaction_count.desc&limit={limit}"
    resp = requests.get(url, headers=headers)
    answers = resp.json()

    if not answers:
        print("No high-reaction answers found, trying expert answers...")
        # Fallback: get Kijai's replies
        kijai_id = 228118453062467585
        url = f"{API_URL}/discord_messages?channel_id=eq.{channel_id}&author_id=eq.{kijai_id}&reference_id=not.is.null&select=message_id,author_id,content,created_at,reaction_count,reference_id&order=created_at.desc&limit={limit}"
        resp = requests.get(url, headers=headers)
        answers = resp.json()

    # Fetch the original questions
    qa_pairs = []
    question_ids = [a['reference_id'] for a in answers if a.get('reference_id')]

    for ans in answers:
        ref_id = ans.get('reference_id')
        if not ref_id:
            continue

        # Fetch the question
        url = f"{API_URL}/discord_messages?message_id=eq.{ref_id}&select=message_id,author_id,content,created_at,reaction_count"
        resp = requests.get(url, headers=headers)
        questions = resp.json()

        if questions:
            qa_pairs.append({
                'question': questions[0],
                'answer': ans
            })

    return qa_pairs


def fetch_author_names(author_ids):
    """Fetch usernames for author IDs."""
    names = {}
    for aid in list(set(author_ids))[:100]:
        url = f"{API_URL}/discord_members?member_id=eq.{aid}&select=global_name,username"
        resp = requests.get(url, headers=headers)
        if resp.json():
            m = resp.json()[0]
            names[aid] = m.get('global_name') or m.get('username') or str(aid)
    return names


def format_qa_for_llm(qa_pairs, names):
    """Format Q&A pairs for LLM processing."""
    lines = []

    for i, pair in enumerate(qa_pairs, 1):
        q = pair['question']
        a = pair['answer']

        q_author = names.get(q['author_id'], str(q['author_id']))
        a_author = names.get(a['author_id'], str(a['author_id']))
        a_reactions = a.get('reaction_count', 0)

        lines.append(f"--- Q&A #{i} ---")
        lines.append(f"Q [{q_author}]: {q.get('content', '')}")
        lines.append(f"A [{a_author}] ({a_reactions} reactions): {a.get('content', '')}")
        lines.append("")

    return "\n".join(lines)


def extract_knowledge(qa_content, channel_name):
    """Use Claude to extract structured knowledge from Q&A pairs."""

    client = anthropic.Anthropic()

    prompt = f"""You are analyzing Q&A exchanges from the "{channel_name}" Discord channel of the Banodoco community, which focuses on open source AI video/image generation tools (Wan, ComfyUI, etc.).

These are real questions from users and answers from community members (often experts). The answers with more reactions are generally more valuable/accurate.

Your task: Extract the valuable knowledge from these exchanges. Focus on:
1. Technical solutions to specific problems
2. Best practices and tips
3. Common pitfalls and how to avoid them
4. Settings recommendations

Output a JSON object with this structure:
{{
  "troubleshooting": [
    {{
      "problem": "The specific issue or error",
      "solution": "How to fix it",
      "details": "Additional context if needed",
      "answered_by": "username"
    }}
  ],
  "tips": [
    {{
      "tip": "The advice or best practice",
      "context": "When this applies",
      "from": "username"
    }}
  ],
  "settings": [
    {{
      "setting": "What setting/parameter",
      "recommendation": "Recommended value or approach",
      "reason": "Why this helps",
      "from": "username"
    }}
  ],
  "concepts": [
    {{
      "term": "Technical term or concept",
      "explanation": "What it means in this context",
      "from": "username"
    }}
  ]
}}

Only include entries where there's clear, actionable information. Skip vague or incomplete exchanges.

Here are the Q&A exchanges:

{qa_content}

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
    channel_name = sys.argv[1] if len(sys.argv) > 1 else "wan_chatter"
    limit = int(sys.argv[2]) if len(sys.argv) > 2 else 30

    if channel_name not in CHANNELS:
        print(f"Unknown channel: {channel_name}")
        print(f"Available: {list(CHANNELS.keys())}")
        return

    channel_id = CHANNELS[channel_name]

    print(f"Fetching high-value Q&A from {channel_name}...")
    qa_pairs = fetch_high_value_qa(channel_id, limit)
    print(f"Found {len(qa_pairs)} Q&A pairs")

    if not qa_pairs:
        print("No Q&A pairs found!")
        return

    # Get author names
    author_ids = []
    for pair in qa_pairs:
        author_ids.append(pair['question']['author_id'])
        author_ids.append(pair['answer']['author_id'])

    print(f"Fetching author names...")
    names = fetch_author_names(author_ids)

    # Format for LLM
    qa_content = format_qa_for_llm(qa_pairs, names)
    token_estimate = len(qa_content) // 4
    print(f"Q&A content: ~{token_estimate} tokens")

    # Extract knowledge
    result, usage = extract_knowledge(qa_content, channel_name)

    print(f"\nAPI Usage: {usage.input_tokens} input, {usage.output_tokens} output tokens")

    # Parse and pretty print
    try:
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
        output_path = os.path.join(script_dir, '..', 'data', f'chat_qa_{channel_name}.json')
        with open(output_path, 'w') as f:
            json.dump({
                'channel': channel_name,
                'extracted_at': datetime.utcnow().isoformat() + 'Z',
                'qa_pairs_processed': len(qa_pairs),
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
