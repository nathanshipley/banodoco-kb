#!/usr/bin/env python3
"""
Synthesize troubleshooting guides from extracted Q&A pairs.
Uses Claude API to process raw Discord Q&A into structured knowledge.

Reads: ../data/reference_knowledge_{channel}.json
Writes: ../data/troubleshooting_{channel}.json and .md
"""

import json
import os
import anthropic
from datetime import datetime

def load_reference_data(channel_name):
    """Load the extracted reference knowledge."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(script_dir, '..', 'data', f'reference_knowledge_{channel_name}.json')

    with open(data_path) as f:
        return json.load(f)

def prepare_content_for_synthesis(data):
    """Prepare the raw Q&A data for LLM synthesis."""

    # Collect all the valuable content
    content_blocks = []

    # Q&A pairs
    content_blocks.append("## Q&A EXCHANGES FROM DISCORD\n")
    for pair in data.get('sample_qa_pairs', []):
        q = pair['question']
        a = pair['answer']
        content_blocks.append(f"Q ({q['author']}): {q['content']}")
        content_blocks.append(f"A ({a['author']}): {a['content']}")
        content_blocks.append("---")

    # Solutions
    content_blocks.append("\n## MESSAGES MENTIONING FIXES/SOLUTIONS\n")
    for msg in data.get('sample_solutions', []):
        content_blocks.append(f"[{msg['author']}]: {msg['content']}")
        content_blocks.append("---")

    # Error discussions
    content_blocks.append("\n## ERROR-RELATED DISCUSSIONS\n")
    for msg in data.get('sample_errors', []):
        content_blocks.append(f"[{msg['author']}]: {msg['content']}")
        content_blocks.append("---")

    return "\n".join(content_blocks)

def synthesize_with_claude(raw_content, channel_name):
    """Use Claude to synthesize the raw content into structured troubleshooting guides."""

    client = anthropic.Anthropic()

    prompt = f"""You are analyzing Discord chat messages from the "{channel_name}" channel of the Banodoco community, which focuses on AI video/image generation (particularly Wan, ComfyUI, etc.).

Below is raw data containing:
1. Q&A exchanges (questions and replies)
2. Messages where people mentioned fixing/solving problems
3. Error-related discussions

Your task: Extract and synthesize this into a structured troubleshooting guide. Focus on:
- Specific errors and their solutions
- Common problems and fixes
- Configuration tips and best practices
- Workflow advice

Output format - create a JSON object with this structure:
{{
  "troubleshooting_entries": [
    {{
      "title": "Brief title of the issue/topic",
      "problem": "Description of the problem or error",
      "solution": "The fix or solution",
      "details": "Additional context, commands, or notes",
      "contributors": ["usernames who provided this info"],
      "category": "one of: error_fix, configuration, workflow, performance, compatibility"
    }}
  ],
  "tips_and_tricks": [
    {{
      "tip": "The advice or best practice",
      "context": "When this applies",
      "contributor": "who shared this"
    }}
  ],
  "common_questions": [
    {{
      "question": "The question",
      "answer": "The answer",
      "contributor": "who answered"
    }}
  ]
}}

Important:
- Only include entries where there's a clear problem AND solution
- Skip vague or incomplete exchanges
- Preserve specific version numbers, commands, and technical details
- Attribute knowledge to the community members who shared it
- Be concise but complete

Here's the raw Discord content to analyze:

{raw_content}

Return ONLY the JSON object, no other text."""

    message = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=8000,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return message.content[0].text

def json_to_markdown(data, channel_name):
    """Convert the JSON troubleshooting data to readable Markdown."""

    lines = [
        f"# {channel_name.replace('_', ' ').title()} Troubleshooting Guide",
        f"\n*Synthesized from Discord discussions - {datetime.now().strftime('%Y-%m-%d')}*\n",
    ]

    # Troubleshooting entries
    if data.get('troubleshooting_entries'):
        lines.append("## Troubleshooting\n")
        for entry in data['troubleshooting_entries']:
            lines.append(f"### {entry.get('title', 'Untitled')}")
            lines.append(f"\n**Problem:** {entry.get('problem', 'N/A')}\n")
            lines.append(f"**Solution:** {entry.get('solution', 'N/A')}\n")
            if entry.get('details'):
                lines.append(f"**Details:** {entry['details']}\n")
            if entry.get('contributors'):
                lines.append(f"*Contributors: {', '.join(entry['contributors'])}*\n")
            lines.append("")

    # Tips and tricks
    if data.get('tips_and_tricks'):
        lines.append("## Tips & Tricks\n")
        for tip in data['tips_and_tricks']:
            lines.append(f"- **{tip.get('tip', '')}**")
            if tip.get('context'):
                lines.append(f"  - Context: {tip['context']}")
            if tip.get('contributor'):
                lines.append(f"  - *From: {tip['contributor']}*")
            lines.append("")

    # Common questions
    if data.get('common_questions'):
        lines.append("## FAQ\n")
        for qa in data['common_questions']:
            lines.append(f"**Q: {qa.get('question', '')}**\n")
            lines.append(f"A: {qa.get('answer', '')}\n")
            if qa.get('contributor'):
                lines.append(f"*Answered by: {qa['contributor']}*\n")
            lines.append("")

    return "\n".join(lines)

def main():
    channel_name = "wan_chatter"

    print(f"Loading reference data for {channel_name}...")
    data = load_reference_data(channel_name)

    print(f"Preparing content ({data['summary']['qa_pairs_found']} Q&A pairs, {data['summary']['solution_mentions']} solutions)...")
    raw_content = prepare_content_for_synthesis(data)

    print(f"Synthesizing with Claude (this may take a moment)...")
    result = synthesize_with_claude(raw_content, channel_name)

    # Parse the JSON response
    try:
        # Handle potential markdown code blocks in response
        if result.startswith("```"):
            result = result.split("```")[1]
            if result.startswith("json"):
                result = result[4:]
        synthesized = json.loads(result)
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON response: {e}")
        print("Raw response:")
        print(result[:500])
        return

    # Save JSON
    script_dir = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.join(script_dir, '..', 'data')

    json_path = os.path.join(data_dir, f'troubleshooting_{channel_name}.json')
    with open(json_path, 'w') as f:
        json.dump({
            'generated_at': datetime.utcnow().isoformat() + 'Z',
            'channel': channel_name,
            'source_messages': data['messages_analyzed'],
            **synthesized
        }, f, indent=2)
    print(f"Saved JSON to {json_path}")

    # Save Markdown
    md_content = json_to_markdown(synthesized, channel_name)
    md_path = os.path.join(data_dir, f'troubleshooting_{channel_name}.md')
    with open(md_path, 'w') as f:
        f.write(md_content)
    print(f"Saved Markdown to {md_path}")

    # Print summary
    print("\n" + "="*60)
    print("SYNTHESIS COMPLETE")
    print("="*60)
    print(f"Troubleshooting entries: {len(synthesized.get('troubleshooting_entries', []))}")
    print(f"Tips & tricks: {len(synthesized.get('tips_and_tricks', []))}")
    print(f"Common questions: {len(synthesized.get('common_questions', []))}")

    # Show a sample
    if synthesized.get('troubleshooting_entries'):
        print("\n--- Sample Entry ---")
        entry = synthesized['troubleshooting_entries'][0]
        print(f"Title: {entry.get('title')}")
        print(f"Problem: {entry.get('problem')}")
        print(f"Solution: {entry.get('solution')}")

if __name__ == "__main__":
    main()
