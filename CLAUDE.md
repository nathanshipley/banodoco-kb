# Banodoco Discord Knowledge Base Project

## Project Goal
Transform the Banodoco Discord database into a useful web-based knowledge base about Open Source AI tools (video generation, image generation, training, ComfyUI, etc.).

**Live site:** https://nathanshipley.github.io/banodoco-kb/
**Knowledge Base:** https://nathanshipley.github.io/banodoco-kb/kb/

---

## Current Status (Feb 2, 2026)

**Phase: LTX Video 2 KB Complete - Ready for Testing**

We've built a complete knowledge extraction and publishing pipeline:
1. Extract knowledge from Discord chat using Claude Sonnet (~$0.17 per 1K messages)
2. Output to markdown for NotebookLM upload
3. Curate into static HTML knowledge base pages

**LTX Video 2 is complete:**
- 44,500 messages processed → 4,345 knowledge items → $7.65 total cost
- NotebookLM-ready combined file: `for_notebooklm/ltx2/2026-02-01/ltx2_january_combined.md` (695KB)
- Static HTML KB: https://nathanshipley.github.io/banodoco-kb/kb/ltx2/

**Next model:** Wan 2.1 (using same approach)

---

## Project Structure

```
banodoco-kb/
├── index.html                              # Hub page with links to all sections
├── progress.html                           # Progress log documenting our thinking
├── database.html                           # Database overview and exploration
├── stats.html                              # Community stats (top contributors)
│
├── kb/                                     # Static HTML Knowledge Base
│   ├── index.html                          # Model selector (LTX2, Wan coming soon)
│   └── ltx2/
│       └── index.html                      # LTX Video 2 comprehensive guide
│
├── for_notebooklm/                         # Combined files for NotebookLM upload
│   ├── README.md                           # How to use these files
│   └── ltx2/
│       └── 2026-02-01/                     # Extraction date
│           ├── ltx2_january_combined.md    # 695KB - upload this to NotebookLM
│           └── manifest.txt                # What's included
│
├── scripts/
│   ├── extract_chat_chunks.py              # Main extraction script (12 categories)
│   ├── extract_forum_thread.py             # Process forum threads
│   ├── extract_chat_qa.py                  # Q&A pair extraction (superseded)
│   ├── get_top_authors.py                  # Fetches top contributors
│   └── synthesize_troubleshooting.py       # Synthesizes Q&A into guides
│
├── data/                                   # Extracted knowledge (JSON + MD)
│   ├── ltx_chatter_20260106_knowledge.*    # Jan 6
│   ├── ltx_chatter_20260107_knowledge.*    # Jan 7
│   ├── ltx_chatter_20260108_knowledge.*    # Jan 8-15
│   ├── ltx_chatter_20260116_knowledge.*    # Jan 16-23
│   ├── ltx_chatter_20260124_knowledge.*    # Jan 24-31
│   ├── ltx_training_20260101_knowledge.*   # Full month
│   ├── ltx_gens_20260101_knowledge.*       # Full month
│   ├── ltx_resources_20260101_knowledge.*  # Full month
│   └── top_authors.json                    # Cached stats
│
├── docs/
│   └── stats-ideas.md                      # Future visualization ideas
├── CLAUDE.md                               # This file
└── README.md                               # GitHub readme
```

---

## Design System

- Monochrome with accent color highlights (blue)
- Responds to system light/dark theme preference
- Manual theme toggle button in top-right corner
- Consistent styling across all pages with breadcrumb navigation

**KB Page Features:**
- Sticky table of contents (desktop)
- Collapsible sections for dense content
- Tables for structured data (hardware, settings)
- Callout boxes for tips/warnings (info, warning, success styles)
- Attribution to community members
- "Last updated" timestamps

**Design Reference:** [Wan 2.1 Knowledge Base on Notion](https://nathanshipley.notion.site/Wan-2-1-Knowledge-Base-1d691e115364814fa9d4e27694e9468f) by Adrien Toupet - good example of comprehensive single-page reference guide structure.

---

## Knowledge Extraction Pipeline

### 1. Extract from Discord (`scripts/extract_chat_chunks.py`)

Processes chat in 400-message time-ordered chunks using Claude Sonnet.

**12 extraction categories:**
1. Technical discoveries
2. Troubleshooting (problems + solutions)
3. Model comparisons
4. Tips and best practices
5. News and updates
6. Workflows
7. Settings/parameters
8. Concepts explained
9. Resources (links to models, repos, workflows)
10. Limitations (what doesn't work)
11. Hardware requirements (VRAM, RAM, GPU compatibility)
12. Community creations (LoRAs, nodes, tools)

**Usage:**
```bash
cd scripts
python extract_chat_chunks.py <channel_name> <start_date> <end_date> [chunk_size]
# Example:
python extract_chat_chunks.py ltx_chatter 2026-01-06 2026-01-07 400
```

**Cost:** ~$0.15-0.20 per 400-message chunk (~$0.60 per 3,500 messages)

**Output:** JSON + Markdown files in `data/` directory

### 2. Combine for NotebookLM

Concatenate extraction files into single document with section headers.

**Structure:**
```
for_notebooklm/
└── {model}/
    └── {extraction_date}/
        ├── {model}_combined.md    # Upload this
        └── manifest.txt           # What's included
```

### 3. Build Static HTML KB

Hand-curate best content into comprehensive HTML pages following the Notion KB pattern:
- Overview → Hardware → Settings → Discoveries → Limitations → Troubleshooting → Workflows → Comparisons → Training → Resources

---

## Database Access

### Supabase REST API
```bash
curl "https://ujlwuvkrxlvoswwkerdf.supabase.co/rest/v1/{TABLE_NAME}" \
  -H "apikey: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InVqbHd1dmtyeGx2b3N3d2tlcmRmIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NjczNzcyMzcsImV4cCI6MjA4MjczNzIzN30.XSTztghf_6a_bpR62wZdoA4S4oafJFDMoPQDRR4dT08"
```

### Key Channel IDs
```
ltx_chatter:    1309520535012638740
ltx_training:   1457981700817817620
ltx_resources:  1457981813120176138
ltx_gens:       1458032975982755861
wan_chatter:    1342763350815277067
```

### Useful Query Patterns
```bash
# Count messages in channel for date range
?channel_id=eq.{ID}&created_at=gte.2026-01-01&created_at=lt.2026-02-01&select=id
# Add header: Prefer: count=exact

# Get messages with content
?channel_id=eq.{ID}&select=message_id,author_id,content,created_at,reaction_count,attachments&order=created_at.asc

# Forum threads (use thread_id)
?thread_id=eq.{THREAD_ID}&order=created_at.asc
```

---

## Database Schema

### Core Tables

| Table | Count | Description |
|-------|-------|-------------|
| `discord_messages` | 1,046,692 | All chat messages |
| `discord_members` | 6,624 | User profiles |
| `discord_channels` | 227 | Channel metadata |
| `daily_summaries` | 463 | AI-generated daily summaries |
| `message_stats` | - | Aggregated stats per channel |

### Key Fields

**discord_messages:**
- `message_id`, `channel_id`, `author_id`
- `content` - message text
- `created_at`, `edited_at`
- `attachments` - array of media files
- `reaction_count`, `reactors`
- `reference_id` - for reply threading in regular channels
- `thread_id` - for forum-style channels (resources)

---

## Completed Work

### LTX Video 2 Extraction (Jan 2026)

| Channel | Messages | Items | Cost |
|---------|----------|-------|------|
| ltx_chatter (full month) | 34,751 | 3,053 | $5.52 |
| ltx_training | 2,850 | 358 | $0.59 |
| ltx_gens | 4,100 | 554 | $0.83 |
| ltx_resources | 2,891 | 380 | $0.71 |
| **Total** | **44,592** | **4,345** | **$7.65** |

### Deliverables

1. **Raw extractions:** 8 markdown + 8 JSON files in `data/`
2. **NotebookLM file:** `for_notebooklm/ltx2/2026-02-01/ltx2_january_combined.md` (695KB)
3. **Static HTML KB:** `kb/ltx2/index.html` - comprehensive guide with TOC, tables, collapsible sections

---

## Next Steps

### Immediate
- [ ] Test LTX2 NotebookLM file - compare to raw chat experience
- [ ] Get user feedback on static HTML KB format
- [ ] Process Wan 2.1 channels (similar volume, ~$8-10 estimated)

### Future
- [ ] Process older months (back to model release dates)
- [ ] Add more models: HunyuanVideo, FLUX, CogVideoX
- [ ] Build search/filter functionality for HTML KB
- [ ] Consider automated refresh pipeline

### Stats & Visualization (Lower Priority)
See `docs/stats-ideas.md`:
- Activity timeline (messages per month)
- Most reacted messages
- Activity heatmap (hour/day)
- Model mentions over time

---

## Key Findings

### Top Contributors
| Rank | Username | Messages | Top Channel |
|------|----------|----------|-------------|
| 1 | **Kijai** | 103,556 | wan_chatter |
| 2 | Draken | 62,016 | comfyui |
| 3 | Cubey | 21,935 | comfyui |

Kijai alone accounts for ~10% of all messages.

### Cost Economics
- **Naive approach:** 1M messages × $15/M tokens = $1,500+ (not practical)
- **Smart filtering:** Process high-value subsets with Sonnet = $7-10 per model/month
- **Actual LTX2 cost:** $7.65 for full January (44K messages)

### Quality Signals
- Messages with 2+ reactions marked with ★ in extraction
- Don't over-index on reactions - good info often has no reactions
- Expert authors (Kijai, etc.) worth prioritizing

---

## Lessons Learned

1. **Run extractions sequentially** - Parallel runs hit API rate limits (30K tokens/min)
2. **Use Sonnet, not Opus** - Quality is good enough, 10x cheaper
3. **400-message chunks work well** - Preserves conversation context
4. **Forum channels work with time-chunked approach** - Still captures value even without thread structure
5. **Single-page-per-model KB works best** - Users can Ctrl+F, read top-to-bottom, or jump to sections
