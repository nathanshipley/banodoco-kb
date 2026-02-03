# Banodoco Knowledge Base - Project Plan

*Created: February 2, 2026*
*Last Updated: February 3, 2026*

---

## Vision

Build the definitive knowledge base for open source AI video/image generation tools, sourced from the Banodoco Discord community (and eventually other sources).

**Two output formats:**
1. **NotebookLM uploads** - For interactive Q&A ("How do I fix X?", "What settings for Y?")
2. **Static HTML KB** - For browsing/reference with rich media (videos, images, workflows)

---

## Scope

### Phase 1: Banodoco Discord (Current Focus)

**Video Generation Models:**
| Model | Priority | Approx Messages | Status |
|-------|----------|-----------------|--------|
| LTX Video 2 | P1 | 45K (Jan 2026) | ✅ Complete |
| **Wan Ecosystem** | P1 | 316K | 🔄 Extraction 90% complete |
| HunyuanVideo | P2 | 50K+ | Not started |
| CogVideoX | P2 | 30K+ | Not started |
| AnimateDiff | P3 | 100K+ (historical) | Not started |
| Mochi | P3 | 10K+ | Not started |

### Wan Ecosystem Detail

The "Wan" KB is actually an entire ecosystem, not a single model:

**Core Generations:**
- Wan 2.1 (Feb 2025) - Standard DiT, 1.3B and 14B variants, T2V and I2V
- Wan 2.2 (July 2025) - MoE architecture, High/Low noise split, 5B hybrid

**Control & Editing Branches:**
- VACE 2.1 - ControlNet for video (style transfer, inpainting, motion control)
- VACE 2.2 (Fun VACE) - For Wan 2.2, separate High/Low modules
- Fun Control - Canny, Depth, Pose, MLSD inputs
- Fun InP - First-Frame-Last-Frame morphing, video extension

**Character & Audio Models:**
- Phantom - T2V with high character consistency
- MagRef - I2V with likeness preservation
- HuMo - Audio-reactive character performance
- Wan 2.2 S2V - Speech-to-video
- MultiTalk / InfiniteTalk - Long-form lip-sync

**Optimization LoRAs:**
- LightX2V - 4-8 step distillation
- Lightning - Alternative speed LoRAs
- Pusa - T2V→I2V capability (~20GB)
- CausVid - Temporal consistency

**ComfyUI Implementations:**
- WanVideoWrapper (Kijai) - Bleeding edge, VACE, complex workflows
- ComfyUI Native - Stable, GGUF support, simpler workflows

**Wan KB Structure (proposed):**
```
kb/wan/
├── index.html          # Overview + navigation
├── 2.1/                # Wan 2.1 specifics
├── 2.2/                # Wan 2.2 specifics
├── vace/               # VACE control system
├── character/          # Phantom, MagRef, HuMo, lip-sync
├── optimization/       # LoRAs, speed tips
└── comfyui/            # Implementation guides
```

**Image Generation Models:**
| Model | Priority | Approx Messages | Status |
|-------|----------|-----------------|--------|
| FLUX | P1 | 80K+ | Not started |
| SDXL | P2 | 150K+ (historical) | Not started |
| Chroma | P3 | 10K+ | Not started |
| Qwen Image | P3 | 5K+ | Not started |

**Tools & Infrastructure:**
| Topic | Priority | Notes |
|-------|----------|-------|
| ComfyUI | P1 | Core workflow engine |
| Training/LoRAs | P2 | Across all models |
| Custom Nodes | P2 | Kijai's nodes, etc. |

**Other:**
| Topic | Priority | Notes |
|-------|----------|-------|
| 3D (Trellis, Hunyuan3D) | P3 | Emerging |
| Audio (MMAudio) | P3 | Emerging |
| LivePortrait | P3 | Face animation |

### Phase 2: External Sources (Future)

- GitHub repos (READMEs, issues, discussions)
- Blog posts / tutorials
- Reddit threads (r/StableDiffusion, r/comfyui, etc.)
- YouTube video transcripts
- Official documentation

---

## Pipeline

### Step 1: Extract Knowledge from Discord

**Tool:** `scripts/extract_chat_chunks.py`

**Process:**
1. Query messages from Supabase for channel + date range
2. Process in 400-message time-ordered chunks
3. Claude Sonnet extracts 12 categories of knowledge
4. Output: JSON + Markdown files

**12 Categories:**
1. Technical discoveries
2. Troubleshooting (problems + solutions)
3. Model comparisons
4. Tips and best practices
5. News and updates
6. Workflows
7. Settings/parameters
8. Concepts explained
9. Resources (links)
10. Limitations
11. Hardware requirements
12. Community creations

**Cost:** ~$0.17 per 1K messages (~$8 per 50K messages)

**Validation:**
- [ ] Spot-check 20 random items for accuracy
- [ ] Compare extraction output to raw chat - are we missing important info?
- [ ] Check attribution accuracy

### Step 2: Combine for NotebookLM

**Process:**
1. Concatenate extraction files with section headers
2. Add metadata header (coverage, date, source)
3. Save to `for_notebooklm/{model}/{date}/`

**Output Structure:**
```
for_notebooklm/
├── ltx2/
│   └── 2026-02-01/
│       ├── ltx2_january_combined.md (695KB) ✅
│       └── manifest.txt
├── wan/
│   └── YYYY-MM-DD/
│       └── wan_combined.md
└── ...
```

**Validation:**
- [ ] Upload to NotebookLM
- [ ] Test 10 questions per model, compare answers to raw chat NotebookLM
- [ ] Check for hallucinations / incorrect info
- [ ] Get user feedback on usefulness

### Step 3: Enrich with External Sources

**Goal:** Discord extractions capture community knowledge, but official docs and curated content provide authoritative context.

**High-value Discord sources (curated, not raw chat):**
- **#updates channel** (~2K messages) - @pom's curated announcements and discoveries
- **#dev_updates** - Developer announcements

**External sources to add:**
- Official model documentation (GitHub READMEs)
- ComfyUI blog posts and guides
- Model release announcements
- Tutorial posts from known experts

**Process:**
1. Identify high-value external sources for each model
2. Fetch/scrape content (WebFetch or manual)
3. Extract relevant knowledge using same categories
4. Merge with Discord extractions, noting source

### Step 4: Synthesize for Static KB

**Goal:** Transform fragmented extraction items into cohesive, authoritative content.

**Key improvements over raw extraction:**
1. **Deduplicate** - Consolidate repeated discoveries
2. **Prioritize** - Highlight authoritative info (Kijai, official docs) over speculation
3. **Structure** - Create decision trees, comparison tables, step-by-step guides
4. **Better attribution** - "Discord, Jan 2026" or "ComfyUI Blog, Dec 2025" with links where possible

**Attribution format:**
- Discord: "— Discord #channel, Month Year"
- External: "— [Source Name](url), Month Year"
- Avoid raw usernames without context

**Process:**
1. Group extraction items by topic
2. LLM pass to consolidate and synthesize
3. Add editorial structure (when to use X vs Y, etc.)
4. Manual review of key sections

### Step 5: Build Static HTML KB

**Process:**
1. Take synthesized content from Step 4
2. Organize into sections (Overview → Hardware → Settings → etc.)
3. Add rich media (videos, images, workflow files)
4. Build HTML page with TOC, collapsible sections, tables

**Media Handling:**
1. Identify high-value media from `attachments` field in database
2. Refresh Discord CDN URLs using pom's API endpoint
3. Embed videos/images inline
4. Offer workflow JSON files as downloads

**Refresh Media URL API:**
```bash
curl -X POST 'https://ujlwuvkrxlvoswwkerdf.supabase.co/functions/v1/refresh-media-urls' \
  -H "Authorization: Bearer $API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"message_id": "1465702490467995718"}'
```

**Output Structure:**
```
kb/
├── index.html (model selector)
├── ltx2/
│   └── index.html ✅
├── wan/
│   └── index.html
├── flux/
│   └── index.html
└── ...
```

**Validation:**
- [ ] Can users find answers to common questions?
- [ ] Do embedded videos/images display correctly?
- [ ] Is navigation intuitive?
- [ ] Mobile responsive?
- [ ] Get user feedback

### Step 6: Media Asset Pipeline (To Build)

**Goal:** Download and host media reliably (Discord URLs expire)

**Options:**
1. **Discord CDN + refresh API** - Use pom's API to refresh URLs on-demand
2. **Cloudflare R2** - Download once, host permanently (~$0.50/mo for 10GB)
3. **GitHub LFS** - Free 1GB, then $5/mo per 50GB pack

**Recommended approach:**
- Start with Discord CDN + refresh API (simplest)
- If reliability issues, migrate to R2

**Process (if R2):**
1. Identify media to include (high-reaction messages, referenced in KB)
2. Download from Discord
3. Upload to R2 bucket
4. Update URLs in KB pages

---

## Execution Plan

### Week 1: Wan Ecosystem Extraction ✅ COMPLETE

**LTX2 Validation:** ✅ Tested in NotebookLM - works well!

**Wan Extraction Status (Feb 3, 2026): COMPLETE**
- [x] wan_chatter Feb-Jun 2025: Complete
- [x] wan_chatter Jul-Nov 2025: Complete (5 months re-extracted)
- [x] wan_chatter Dec 2025 - Feb 2026: Complete
- [x] wan_gens: Complete (487KB)
- [x] wan_training: Complete (457KB)
- [x] wan_comfyui: Complete (233KB)
- [x] wan_resources: Complete (206KB)

**Total extracted:** ~316K messages, ~$65-70 cost
**Output:** 24 extraction files (JSON + MD for each time period/channel)

**Remaining for Wan:**
- [ ] Combine all Wan extractions into NotebookLM file
- [ ] Add external sources (docs, blog posts, #updates channel)
- [ ] Build static Wan KB with synthesis step

### Week 2: Expand Coverage

- [ ] Extract FLUX
- [ ] Extract HunyuanVideo
- [ ] Build static KB pages for both
- [ ] Test NotebookLM uploads

### Week 3: Complete P1, Start P2

- [ ] Complete ComfyUI extraction
- [ ] Start P2 models (CogVideoX, SDXL, Training)
- [ ] Refine HTML KB based on feedback

### Week 4+: P2/P3 Models, Polish

- [ ] Complete remaining models
- [ ] Add search/filter to KB
- [ ] Consider media hosting migration if needed
- [ ] Document process for future updates

---

## Cost Estimates

### Extraction Costs (One-time)

| Model/Topic | Est. Messages | Est. Cost |
|-------------|---------------|-----------|
| LTX Video 2 | 45K | $7.65 ✅ |
| Wan 2.1 | 200K | ~$35 |
| FLUX | 80K | ~$14 |
| HunyuanVideo | 50K | ~$9 |
| CogVideoX | 30K | ~$5 |
| AnimateDiff | 100K | ~$17 |
| SDXL | 150K | ~$26 |
| ComfyUI | 100K | ~$17 |
| Other (Mochi, Chroma, etc.) | 50K | ~$9 |
| **Total** | **~800K** | **~$140** |

### Ongoing Costs

| Item | Cost |
|------|------|
| GitHub Pages hosting | Free |
| Media hosting (if R2) | ~$0.50/mo |
| Refresh extractions monthly | ~$20/mo (for active models) |

---

## Success Metrics

### NotebookLM
- Users can get accurate answers to technical questions
- Answers include attribution to community members
- No hallucinations or incorrect info
- Faster than searching raw Discord

### Static HTML KB
- Users can find information within 30 seconds
- Media (videos, workflows) displays correctly
- Mobile-friendly
- Useful enough that people bookmark/share it

### Overall
- Positive feedback from Banodoco community
- Reduces repeated questions in Discord
- Becomes go-to resource for model-specific knowledge

---

## Decisions Made

1. **Historical depth:** ✅ All-time coverage
   - Valuable historical knowledge (AnimateDiff, SDXL) should be included
   - Extract from model release date forward

2. **Refresh frequency:** ✅ Tiered approach
   - Active models (LTX2, Wan): Weekly
   - Stable models (AnimateDiff, SDXL): Monthly

3. **Media strategy:** ✅ Discord CDN + refresh API first
   - Use pom's refresh API to get fresh URLs
   - Migrate to Cloudflare R2 if reliability issues arise

4. **LTX2 validation:** ✅ NotebookLM tested, works well
   - Proceeding to Wan extraction

## Open Questions

1. **Quality control:** How do we catch and fix errors in extracted knowledge?
   - Community flagging system?
   - Manual review of high-stakes info (settings, troubleshooting)?

2. **Attribution:** Should we link back to original Discord messages?
   - Useful for verification
   - But Discord links require login

3. **Contribution:** Should community members be able to suggest edits?
   - GitHub PRs?
   - Simple feedback form?

4. **Wan KB structure:** Single page vs multi-page?
   - Ecosystem is complex (2.1, 2.2, VACE, Fun, character models, etc.)
   - Adrien's Notion KB is single page - works but very long
   - Multi-page with index might be more navigable

---

## Reference

- **LTX2 KB (live):** https://nathanshipley.github.io/banodoco-kb/kb/ltx2/
- **Wan Notion KB (inspiration):** https://nathanshipley.notion.site/Wan-2-1-Knowledge-Base-1d691e115364814fa9d4e27694e9468f
- **Extraction script:** `scripts/extract_chat_chunks.py`
- **Media refresh API:** See "Refresh Media URL API" above
