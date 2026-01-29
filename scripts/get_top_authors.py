#!/usr/bin/env python3
"""
Fetch top authors by message count from the Banodoco Discord database.
Saves results to ../data/top_authors.json
"""

import requests
import json
import os
from collections import defaultdict
from datetime import datetime

API_URL = "https://ujlwuvkrxlvoswwkerdf.supabase.co/rest/v1"
API_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InVqbHd1dmtyeGx2b3N3d2tlcmRmIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NjczNzcyMzcsImV4cCI6MjA4MjczNzIzN30.XSTztghf_6a_bpR62wZdoA4S4oafJFDMoPQDRR4dT08"

headers = {"apikey": API_KEY}

def main():
    print("Fetching all messages (this will take several minutes)...")

    author_counts = defaultdict(int)
    author_channels = defaultdict(lambda: defaultdict(int))

    offset = 0
    batch_size = 1000
    total = 0

    while True:
        url = f"{API_URL}/discord_messages?select=author_id,channel_id&order=message_id&offset={offset}&limit={batch_size}"
        resp = requests.get(url, headers=headers)

        if resp.status_code != 200:
            print(f"Error at offset {offset}: {resp.status_code}")
            break

        data = resp.json()
        if not data:
            break

        for msg in data:
            aid = msg['author_id']
            cid = msg['channel_id']
            author_counts[aid] += 1
            author_channels[aid][cid] += 1

        total += len(data)
        offset += batch_size

        if total % 100000 == 0:
            print(f"  Processed {total:,} messages...")

        if len(data) < batch_size:
            break

    print(f"\nTotal messages processed: {total:,}")
    print(f"Unique authors: {len(author_counts):,}")

    # Get top 50 author IDs (fetch more for flexibility)
    top_author_ids = [aid for aid, _ in sorted(author_counts.items(), key=lambda x: x[1], reverse=True)[:50]]

    # Fetch their names
    print("\nFetching author names...")
    author_names = {}
    for aid in top_author_ids:
        url = f"{API_URL}/discord_members?member_id=eq.{aid}&select=global_name,username"
        resp = requests.get(url, headers=headers)
        if resp.status_code == 200 and resp.json():
            m = resp.json()[0]
            author_names[aid] = m.get('global_name') or m.get('username') or str(aid)
        else:
            author_names[aid] = str(aid)

    # Fetch channel names
    print("Fetching channel names...")
    channel_names = {}
    url = f"{API_URL}/discord_channels?select=channel_id,channel_name"
    resp = requests.get(url, headers=headers)
    if resp.status_code == 200:
        for c in resp.json():
            channel_names[c['channel_id']] = c['channel_name']

    # Build results
    results = {
        "generated_at": datetime.utcnow().isoformat() + "Z",
        "total_messages": total,
        "unique_authors": len(author_counts),
        "top_authors": []
    }

    for rank, (aid, count) in enumerate(sorted(author_counts.items(), key=lambda x: x[1], reverse=True)[:50], 1):
        top_channel_id = max(author_channels[aid].items(), key=lambda x: x[1])[0]
        results["top_authors"].append({
            "rank": rank,
            "author_id": aid,
            "username": author_names.get(aid, str(aid)),
            "message_count": count,
            "top_channel_id": top_channel_id,
            "top_channel_name": channel_names.get(top_channel_id, str(top_channel_id))
        })

    # Save to data folder
    script_dir = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.join(script_dir, "..", "data")
    os.makedirs(data_dir, exist_ok=True)

    output_path = os.path.join(data_dir, "top_authors.json")
    with open(output_path, "w") as f:
        json.dump(results, f, indent=2)

    print(f"\nResults saved to {output_path}")

    # Print table
    print("\n" + "="*75)
    print(f"{'Rank':<5} {'Username':<25} {'Messages':>12} {'Top Channel':<28}")
    print("="*75)

    for author in results["top_authors"][:20]:
        name = author["username"][:24]
        channel = author["top_channel_name"][:27]
        print(f"{author['rank']:<5} {name:<25} {author['message_count']:>12,} {channel:<28}")

if __name__ == "__main__":
    main()
