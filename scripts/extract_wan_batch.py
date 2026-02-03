#!/usr/bin/env python3
"""
Batch extraction for all Wan channels.
Runs wan_chatter in monthly chunks, other channels in full.
"""

import subprocess
import sys
from datetime import datetime

# Monthly chunks for wan_chatter (244K messages - too big for one run)
WAN_CHATTER_CHUNKS = [
    ("2025-02-22", "2025-03-01"),  # Late Feb 2025
    ("2025-03-01", "2025-04-01"),  # Mar 2025
    ("2025-04-01", "2025-05-01"),  # Apr 2025
    ("2025-05-01", "2025-06-01"),  # May 2025
    ("2025-06-01", "2025-07-01"),  # Jun 2025
    ("2025-07-01", "2025-08-01"),  # Jul 2025
    ("2025-08-01", "2025-09-01"),  # Aug 2025
    ("2025-09-01", "2025-10-01"),  # Sep 2025
    ("2025-10-01", "2025-11-01"),  # Oct 2025
    ("2025-11-01", "2025-12-01"),  # Nov 2025
    ("2025-12-01", "2026-01-01"),  # Dec 2025
    ("2026-01-01", "2026-02-01"),  # Jan 2026
    ("2026-02-01", "2026-02-03"),  # Feb 2026 (partial)
]

# Other channels - small enough for single runs
OTHER_CHANNELS = [
    ("wan_gens", "2025-02-25", "2026-02-03"),      # 26K messages
    ("wan_training", "2025-02-26", "2026-02-03"),  # 23K messages
    ("wan_comfyui", "2025-09-23", "2026-02-03"),   # 12K messages
    ("wan_resources", "2025-05-17", "2026-02-03"), # 10K messages
]


def run_extraction(channel, start, end):
    """Run the extraction script for a channel/date range."""
    cmd = ["python3", "scripts/extract_chat_chunks.py", channel, start, end, "400"]
    print(f"\n{'='*60}")
    print(f"Extracting: {channel} ({start} to {end})")
    print(f"{'='*60}")

    result = subprocess.run(cmd, cwd="/Volumes/OWC 8TB HHD/Dropbox (Personal)/Work/Projects/Banodoco/BDCO_002_OmniKB/banodoco-kb")
    return result.returncode == 0


def main():
    start_time = datetime.now()
    successful = 0
    failed = 0

    # Check if we should skip to a specific point
    skip_until = None
    if len(sys.argv) > 1:
        skip_until = sys.argv[1]
        print(f"Skipping until: {skip_until}")

    skipping = skip_until is not None

    # Run wan_chatter in monthly chunks
    print("\n" + "="*60)
    print("PHASE 1: wan_chatter (monthly chunks)")
    print("="*60)

    for i, (start, end) in enumerate(WAN_CHATTER_CHUNKS):
        chunk_id = f"wan_chatter_{start}"

        if skipping:
            if skip_until in chunk_id:
                skipping = False
            else:
                print(f"Skipping {chunk_id}...")
                continue

        print(f"\n[{i+1}/{len(WAN_CHATTER_CHUNKS)}] wan_chatter: {start} to {end}")
        if run_extraction("wan_chatter", start, end):
            successful += 1
        else:
            failed += 1
            print(f"WARNING: Failed extraction for wan_chatter {start}")

    # Run other channels
    print("\n" + "="*60)
    print("PHASE 2: Other Wan channels")
    print("="*60)

    for channel, start, end in OTHER_CHANNELS:
        if skipping:
            if skip_until in channel:
                skipping = False
            else:
                print(f"Skipping {channel}...")
                continue

        if run_extraction(channel, start, end):
            successful += 1
        else:
            failed += 1
            print(f"WARNING: Failed extraction for {channel}")

    # Summary
    elapsed = datetime.now() - start_time
    print("\n" + "="*60)
    print("EXTRACTION COMPLETE")
    print("="*60)
    print(f"Successful: {successful}")
    print(f"Failed: {failed}")
    print(f"Total time: {elapsed}")


if __name__ == "__main__":
    main()
