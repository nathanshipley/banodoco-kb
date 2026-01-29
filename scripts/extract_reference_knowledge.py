#!/usr/bin/env python3
"""
Extract potential "reference knowledge" from a Discord channel.
Looks for Q&A patterns, error discussions, and how-to content.

Saves results to ../data/reference_knowledge_{channel}.json
"""

import requests
import json
import os
import re
from datetime import datetime
from collections import defaultdict

API_URL = "https://ujlwuvkrxlvoswwkerdf.supabase.co/rest/v1"
API_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InVqbHd1dmtyeGx2b3N3d2tlcmRmIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NjczNzcyMzcsImV4cCI6MjA4MjczNzIzN30.XSTztghf_6a_bpR62wZdoA4S4oafJFDMoPQDRR4dT08"

headers = {"apikey": API_KEY}

# wan_chatter channel ID
CHANNEL_ID = 1342763350815277067
CHANNEL_NAME = "wan_chatter"

# Patterns that suggest questions or problems
QUESTION_PATTERNS = [
    r'\?',  # Questions
    r'\bhow (do|can|to|does)\b',
    r'\bwhat (is|are|does)\b',
    r'\bwhy (is|does|do)\b',
    r'\berror\b',
    r'\bfail(ed|ing|s)?\b',
    r'\bcrash(ed|ing|es)?\b',
    r'\bhelp\b',
    r'\bissue\b',
    r'\bproblem\b',
    r'\bdoesn\'t work\b',
    r'\bnot working\b',
    r'\bfixed\b',
    r'\bsolved\b',
    r'\bsolution\b',
    r'\btip\b',
    r'\btrick\b',
    r'\bvram\b',
    r'\bout of memory\b',
    r'\boom\b',
]

def matches_patterns(text, patterns):
    """Check if text matches any of the patterns."""
    text_lower = text.lower()
    for pattern in patterns:
        if re.search(pattern, text_lower):
            return True
    return False

def fetch_messages(channel_id, limit=10000):
    """Fetch messages from a channel."""
    print(f"Fetching messages from channel {channel_id}...")

    messages = []
    offset = 0
    batch_size = 1000

    while len(messages) < limit:
        url = f"{API_URL}/discord_messages?channel_id=eq.{channel_id}&select=message_id,author_id,content,created_at,reference_id,reaction_count&order=created_at.desc&offset={offset}&limit={batch_size}"
        resp = requests.get(url, headers=headers)

        if resp.status_code != 200:
            print(f"Error: {resp.status_code}")
            break

        data = resp.json()
        if not data:
            break

        messages.extend(data)
        offset += batch_size
        print(f"  Fetched {len(messages)} messages...")

        if len(data) < batch_size:
            break

    return messages

def fetch_member_names(author_ids):
    """Fetch usernames for a list of author IDs."""
    print(f"Fetching names for {len(author_ids)} authors...")
    names = {}

    for aid in author_ids:
        url = f"{API_URL}/discord_members?member_id=eq.{aid}&select=global_name,username"
        resp = requests.get(url, headers=headers)
        if resp.status_code == 200 and resp.json():
            m = resp.json()[0]
            names[aid] = m.get('global_name') or m.get('username') or str(aid)
        else:
            names[aid] = str(aid)

    return names

def analyze_messages(messages):
    """Analyze messages for reference knowledge patterns."""

    # Index messages by ID for reply lookup
    msg_by_id = {m['message_id']: m for m in messages}

    # Find potential questions/problems
    questions = []
    for msg in messages:
        content = msg.get('content', '')
        if not content:
            continue
        if matches_patterns(content, QUESTION_PATTERNS):
            questions.append(msg)

    print(f"Found {len(questions)} potential questions/problems")

    # Find replies to questions
    qa_pairs = []
    for msg in messages:
        ref_id = msg.get('reference_id')
        if ref_id and ref_id in msg_by_id:
            original = msg_by_id[ref_id]
            # Check if original was a question
            orig_content = original.get('content', '')
            if matches_patterns(orig_content, QUESTION_PATTERNS):
                qa_pairs.append({
                    'question': original,
                    'answer': msg
                })

    print(f"Found {len(qa_pairs)} Q&A reply pairs")

    # Find messages with "fixed", "solved", "solution"
    solutions = []
    for msg in messages:
        content = msg.get('content', '').lower()
        if any(word in content for word in ['fixed', 'solved', 'solution', 'figured it out', 'got it working']):
            solutions.append(msg)

    print(f"Found {len(solutions)} messages mentioning fixes/solutions")

    # Find error-related discussions
    errors = []
    for msg in messages:
        content = msg.get('content', '').lower()
        if any(word in content for word in ['error', 'traceback', 'exception', 'crash', 'failed']):
            errors.append(msg)

    print(f"Found {len(errors)} error-related messages")

    # Find highly-reacted messages (might be good info)
    reacted = [m for m in messages if m.get('reaction_count', 0) >= 3]
    reacted.sort(key=lambda x: x.get('reaction_count', 0), reverse=True)

    print(f"Found {len(reacted)} messages with 3+ reactions")

    return {
        'questions': questions[:100],  # Limit for analysis
        'qa_pairs': qa_pairs[:100],
        'solutions': solutions[:100],
        'errors': errors[:100],
        'highly_reacted': reacted[:50]
    }

def main():
    # Fetch recent messages from wan_chatter
    messages = fetch_messages(CHANNEL_ID, limit=50000)
    print(f"\nTotal messages fetched: {len(messages)}")

    # Analyze for reference knowledge
    analysis = analyze_messages(messages)

    # Get unique author IDs for name lookup
    all_author_ids = set()
    for key in ['questions', 'solutions', 'errors', 'highly_reacted']:
        for msg in analysis[key]:
            all_author_ids.add(msg['author_id'])
    for pair in analysis['qa_pairs']:
        all_author_ids.add(pair['question']['author_id'])
        all_author_ids.add(pair['answer']['author_id'])

    names = fetch_member_names(list(all_author_ids)[:100])  # Limit API calls

    # Build output with readable names
    def format_msg(msg):
        return {
            'message_id': msg['message_id'],
            'author': names.get(msg['author_id'], str(msg['author_id'])),
            'content': msg['content'],
            'created_at': msg['created_at'],
            'reactions': msg.get('reaction_count', 0)
        }

    output = {
        'generated_at': datetime.utcnow().isoformat() + 'Z',
        'channel': CHANNEL_NAME,
        'channel_id': CHANNEL_ID,
        'messages_analyzed': len(messages),
        'summary': {
            'potential_questions': len(analysis['questions']),
            'qa_pairs_found': len(analysis['qa_pairs']),
            'solution_mentions': len(analysis['solutions']),
            'error_discussions': len(analysis['errors']),
            'highly_reacted': len(analysis['highly_reacted'])
        },
        'sample_qa_pairs': [
            {
                'question': format_msg(pair['question']),
                'answer': format_msg(pair['answer'])
            }
            for pair in analysis['qa_pairs'][:30]
        ],
        'sample_solutions': [format_msg(m) for m in analysis['solutions'][:30]],
        'sample_errors': [format_msg(m) for m in analysis['errors'][:30]],
        'top_reacted': [format_msg(m) for m in analysis['highly_reacted'][:20]]
    }

    # Save to data folder
    script_dir = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.join(script_dir, '..', 'data')
    os.makedirs(data_dir, exist_ok=True)

    output_path = os.path.join(data_dir, f'reference_knowledge_{CHANNEL_NAME}.json')
    with open(output_path, 'w') as f:
        json.dump(output, f, indent=2)

    print(f"\nResults saved to {output_path}")

    # Print summary
    print("\n" + "="*60)
    print("SUMMARY")
    print("="*60)
    print(f"Messages analyzed: {len(messages)}")
    print(f"Potential questions: {len(analysis['questions'])}")
    print(f"Q&A pairs (reply to question): {len(analysis['qa_pairs'])}")
    print(f"Solution mentions: {len(analysis['solutions'])}")
    print(f"Error discussions: {len(analysis['errors'])}")
    print(f"Highly reacted (3+): {len(analysis['highly_reacted'])}")

    # Show a few example Q&A pairs
    print("\n" + "="*60)
    print("SAMPLE Q&A PAIRS")
    print("="*60)
    for i, pair in enumerate(analysis['qa_pairs'][:5], 1):
        q = pair['question']
        a = pair['answer']
        q_author = names.get(q['author_id'], str(q['author_id']))
        a_author = names.get(a['author_id'], str(a['author_id']))
        print(f"\n--- Pair {i} ---")
        print(f"Q ({q_author}): {q['content'][:200]}...")
        print(f"A ({a_author}): {a['content'][:200]}...")

if __name__ == "__main__":
    main()
