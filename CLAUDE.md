# Banodoco Discord Knowledge Base Project

## Project Goal
Transform the Banodoco Discord database into a useful web-based knowledge base about Open Source AI tools (video generation, image generation, training, ComfyUI, etc.).

**Live site:** https://nathanshipley.github.io/banodoco-kb/
**Knowledge Base:** https://nathanshipley.github.io/banodoco-kb/kb/
**Full Project Plan:** `docs/project-plan.md`

---

## Current Status (Feb 2, 2026)

**Phase: LTX2 Complete, Starting Wan Ecosystem**

### Completed
- LTX Video 2 extraction (44K messages → 4,345 items, $7.65)
- NotebookLM upload tested - **works well!**
- Static HTML KB built: https://nathanshipley.github.io/banodoco-kb/kb/ltx2/

### Next Up: Wan Ecosystem
The "Wan" KB covers an entire ecosystem, not just one model:
- **Core generations:** Wan 2.1 (Feb 2025), Wan 2.2 (July 2025)
- **Control branches:** VACE, Fun Control, Fun InP
- **Character/audio:** Phantom, MagRef, HuMo, S2V, MultiTalk
- **Optimization:** LightX2V, Lightning, Pusa, CausVid
- **ComfyUI:** WanVideoWrapper (Kijai) vs Native

See `docs/project-plan.md` for full Wan ecosystem breakdown.

---

## Key Insight: NotebookLM vs Static KB

**NotebookLM excels at specific Q&A:**
- "When should I use Wan 2.1 vs 2.2?" → Detailed comparison with trade-offs
- "My 1080p VACE has no motion, what's wrong?" → Diagnoses resolution issue, gives fix

**Static KB should complement, not compete:**
- Overview/comparison pages (decision trees, tables)
- Quick reference (VRAM requirements, settings)
- Rich media (videos, workflow files, screenshots)
- Navigation to help users know what questions to ask

---

## Project Structure

```
banodoco-kb/
├── index.html                              # Hub page
├── progress.html                           # Progress log
├── database.html                           # Database overview
├── stats.html                              # Community stats
│
├── kb/                                     # Static HTML Knowledge Base
│   ├── index.html                          # Model selector
│   └── ltx2/
│       └── index.html                      # LTX Video 2 guide
│
├── for_notebooklm/                         # NotebookLM upload files
│   ├── README.md
│   └── ltx2/
│       └── 2026-02-01/
│           ├── ltx2_january_combined.md    # 695KB
│           └── manifest.txt
│
├── scripts/
│   ├── extract_chat_chunks.py              # Main extraction (12 categories)
│   ├── extract_forum_thread.py             # Forum threads
│   └── ...
│
├── data/                                   # Extracted knowledge (JSON + MD)
│   └── ltx_*_knowledge.*                   # LTX extractions
│
├── docs/
│   ├── project-plan.md                     # Full project plan & scope
│   └── stats-ideas.md                      # Visualization ideas
│
├── CLAUDE.md                               # This file
└── README.md
```

---

## APIs & Tools

### Supabase REST API
```bash
curl "https://ujlwuvkrxlvoswwkerdf.supabase.co/rest/v1/{TABLE}" \
  -H "apikey: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InVqbHd1dmtyeGx2b3N3d2tlcmRmIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NjczNzcyMzcsImV4cCI6MjA4MjczNzIzN30.XSTztghf_6a_bpR62wZdoA4S4oafJFDMoPQDRR4dT08"
```

### Refresh Discord Media URLs (pom's API)
Discord CDN URLs expire. To get fresh URLs:
```bash
curl -X POST 'https://ujlwuvkrxlvoswwkerdf.supabase.co/functions/v1/refresh-media-urls' \
  -H "Authorization: Bearer $API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"message_id": "1465702490467995718"}'
```
Returns: `{ "success": true, "attachments": [...], "urls_updated": 1 }`

### Key Channel IDs
```
ltx_chatter:    1309520535012638740
ltx_training:   1457981700817817620
ltx_resources:  1457981813120176138
ltx_gens:       1458032975982755861
wan_chatter:    1342763350815277067
```

---

## Extraction Pipeline

### 1. Extract (`scripts/extract_chat_chunks.py`)
```bash
python extract_chat_chunks.py <channel> <start_date> <end_date> [chunk_size]
```
- Processes 400-message chunks with Claude Sonnet
- Extracts 12 categories (discoveries, troubleshooting, comparisons, tips, etc.)
- Cost: ~$0.17 per 1K messages

### 2. Combine for NotebookLM
Concatenate extractions → single markdown file → upload to NotebookLM

### 3. Build Static KB
Curate best content into HTML pages with:
- Sticky TOC, collapsible sections, tables
- Rich media (videos, images, workflow downloads)
- Links to NotebookLM for deeper Q&A

---

## Completed Work

### LTX Video 2 (Jan 2026)

| Channel | Messages | Items | Cost |
|---------|----------|-------|------|
| ltx_chatter | 34,751 | 3,053 | $5.52 |
| ltx_training | 2,850 | 358 | $0.59 |
| ltx_gens | 4,100 | 554 | $0.83 |
| ltx_resources | 2,891 | 380 | $0.71 |
| **Total** | **44,592** | **4,345** | **$7.65** |

**Deliverables:**
1. Raw extractions in `data/` (8 MD + 8 JSON files)
2. NotebookLM file: `for_notebooklm/ltx2/2026-02-01/ltx2_january_combined.md`
3. Static KB: `kb/ltx2/index.html`

---

## Decisions Made

| Decision | Answer |
|----------|--------|
| Historical depth | **All-time** - extract from model release forward |
| Refresh frequency | **Weekly** (active) / **Monthly** (stable) |
| Media strategy | **Discord CDN + refresh API** first, R2 if needed |

---

## Cost Estimates

| Model | Est. Messages | Est. Cost |
|-------|---------------|-----------|
| LTX Video 2 | 45K | $7.65 ✅ |
| Wan Ecosystem | 200K+ | ~$35 |
| FLUX | 80K | ~$14 |
| HunyuanVideo | 50K | ~$9 |
| All others | 400K | ~$70 |
| **Total** | **~800K** | **~$140** |

---

## Lessons Learned

1. **NotebookLM with raw chat works remarkably well** - Handles specific Q&A with nuance
2. **Static KB complements NotebookLM** - For browsing, media, decision trees
3. **Run extractions sequentially** - Parallel hits rate limits (30K tokens/min)
4. **Use Sonnet, not Opus** - Quality sufficient, 10x cheaper
5. **400-message chunks preserve context** - Good balance of cost vs coherence
6. **Wan is an ecosystem** - Not one model, but generations + branches + tools
