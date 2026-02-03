# Banodoco Discord Knowledge Base Project

## Project Goal
Transform the Banodoco Discord database into a useful web-based knowledge base about Open Source AI tools (video generation, image generation, training, ComfyUI, etc.).

**Live site:** https://nathanshipley.github.io/banodoco-kb/
**Knowledge Base:** https://nathanshipley.github.io/banodoco-kb/kb/
**Full Project Plan:** `docs/project-plan.md`

---

## Current Status (Feb 3, 2026)

**Phase: Wan Enrichment COMPLETE - Ready for Static KB**

### Completed
- LTX Video 2 extraction (44K messages → 4,345 items, $7.65)
- **Wan ecosystem extraction (316K messages, ~$65-70)** ✅
- **Wan external sources gathered** - 60+ URLs, technical content fetched ✅
- **#updates channel extracted** - @pom's curated highlights (1,987 msgs → 946 items, $1.44) ✅
- NotebookLM upload tested - **works well!**
- Static HTML KB built: https://nathanshipley.github.io/banodoco-kb/kb/ltx2/

### Wan Source Materials Ready
| Source | Content | Output |
|--------|---------|--------|
| wan_chatter | 244K msgs, 13 months | 13 files, ~4.3MB |
| wan_gens/training/comfyui/resources | 72K msgs | 4 files, ~1.3MB |
| #updates channel | 1,987 curated posts | 124KB |
| External sources | 60+ URLs fetched | ~500 lines technical specs |
| **Total** | **~318K msgs + external** | **~6MB extracted knowledge** |

### Next Step
**Build static Wan KB** - Synthesize all sources into HTML pages

### Pipeline Insight: Extraction → Enrichment → Synthesis → KB
Raw extraction produces fragmented knowledge items. For static KB, we need:
1. **Add external sources:** Official docs, blog posts, GitHub READMEs, #updates channel
2. **Synthesize:** Deduplicate, consolidate, add editorial structure
3. **Better attribution:** "— Discord #channel, Month Year" not just "— Username"

See `docs/project-plan.md` for full 6-step pipeline.

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
│   ├── wan_external_sources.md             # URLs for external sources
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
│   ├── ltx_*_knowledge.*                   # LTX extractions (8 files)
│   ├── wan_*_knowledge.*                   # Wan extractions (17 files)
│   ├── updates_*_knowledge.*               # #updates channel (curated highlights)
│   └── wan_external_sources_content.md     # Fetched content from external URLs
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
wan_gens:       1344057524935983125
wan_training:   1344309523187368046
wan_comfyui:    1420053619541283000
wan_resources:  1373291419434877078
updates:        1138790534987661363
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

### Wan Ecosystem (Feb 2025 - Feb 2026)

| Channel | Period | Messages | Cost |
|---------|--------|----------|------|
| wan_chatter | Feb 2025 | ~8K | $1.20 |
| wan_chatter | Mar 2025 | ~28K | $4.80 |
| wan_chatter | Apr 2025 | ~20K | $3.40 |
| wan_chatter | May 2025 | ~22K | $3.60 |
| wan_chatter | Jun 2025 | ~25K | $4.10 |
| wan_chatter | Jul 2025 | ~33K | $6.42 |
| wan_chatter | Aug 2025 | ~41K | $7.68 |
| wan_chatter | Sep 2025 | ~26K | $4.95 |
| wan_chatter | Oct 2025 | ~19K | $3.45 |
| wan_chatter | Nov 2025 | ~11K | $2.10 |
| wan_chatter | Dec 2025 | ~15K | $2.50 |
| wan_chatter | Jan-Feb 2026 | ~6K | $1.00 |
| wan_gens | Full | ~28K | $4.80 |
| wan_training | Full | ~26K | $4.50 |
| wan_comfyui | Full | ~12K | $2.30 |
| wan_resources | Full | ~6K | $2.00 |
| **Total** | | **~316K** | **~$65-70** |

**Deliverables:**
1. Raw extractions in `data/` (17 MD + 17 JSON files, ~843K words total)
2. NotebookLM: Upload each file as separate source (stays under 500K word limit)
3. Static KB: TBD - needs synthesis step

---

## Decisions Made

| Decision | Answer |
|----------|--------|
| Historical depth | **All-time** - extract from model release forward |
| Refresh frequency | **Weekly** (active) / **Monthly** (stable) |
| Media strategy | **Discord CDN + refresh API** first, R2 if needed |

---

## Cost Estimates

| Model | Messages | Cost |
|-------|----------|------|
| LTX Video 2 | 45K | $7.65 ✅ |
| Wan Ecosystem | 316K | ~$65-70 ✅ |
| FLUX | 80K | ~$14 |
| HunyuanVideo | 50K | ~$9 |
| All others | 400K | ~$70 |
| **Total** | **~900K** | **~$165** |

---

## Lessons Learned

1. **NotebookLM with raw chat works remarkably well** - Handles specific Q&A with nuance
2. **Static KB complements NotebookLM** - For browsing, media, decision trees
3. **Run extractions sequentially** - Parallel hits rate limits (30K tokens/min)
4. **Use Sonnet, not Opus** - Quality sufficient, 10x cheaper
5. **400-message chunks preserve context** - Good balance of cost vs coherence
6. **Wan is an ecosystem** - Not one model, but generations + branches + tools
7. **NotebookLM has 500K word/source limit** - Don't combine all files; upload as separate sources (50 max free, 300 Plus)
8. **Batch API calls** - Fetch author names in batches of 100, not individually
9. **Always save fetched content to files** - Context will be lost; save URLs to `for_notebooklm/` and content to `data/`
