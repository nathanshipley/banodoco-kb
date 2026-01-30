# Banodoco Discord Knowledge Base Project

## Project Goal
Transform the Banodoco Discord database into a useful web-based knowledge base about Open Source AI tools (video generation, image generation, training, ComfyUI, etc.).

**Live site:** https://nathanshipley.github.io/banodoco-kb/

## Project Structure

```
banodoco-kb/
├── index.html                              # Hub page linking to all sections
├── progress.html                           # Progress log documenting our thinking
├── database.html                           # Database overview and exploration
├── stats.html                              # Community stats (top contributors)
├── scripts/
│   ├── get_top_authors.py                  # Fetches top contributors from API
│   ├── extract_reference_knowledge.py      # Extracts Q&A pairs from raw chat
│   └── synthesize_troubleshooting.py       # Synthesizes Q&A into guides (API-based)
├── data/
│   ├── top_authors.json                    # Cached stats data
│   ├── reference_knowledge_wan_chatter.json # Extracted Q&A from wan_chatter
│   ├── troubleshooting_wan_chatter.json    # Synthesized troubleshooting guide
│   └── troubleshooting_wan_chatter.md      # Human-readable version
├── docs/
│   └── stats-ideas.md                      # Future stats/visualization ideas
├── CLAUDE.md                               # This file
└── README.md                               # GitHub readme
```

## Design
- Monochrome with accent color highlights
- Responds to system light/dark theme preference
- Manual theme toggle button in top-right corner
- Consistent styling across all pages with breadcrumb navigation

---

## Database Access

### Supabase REST API
```bash
curl "https://ujlwuvkrxlvoswwkerdf.supabase.co/rest/v1/{TABLE_NAME}" \
  -H "apikey: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InVqbHd1dmtyeGx2b3N3d2tlcmRmIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NjczNzcyMzcsImV4cCI6MjA4MjczNzIzN30.XSTztghf_6a_bpR62wZdoA4S4oafJFDMoPQDRR4dT08"
```

### Useful Query Patterns
```bash
# Get row count
curl -sI "URL?select=id" -H "apikey: KEY" -H "Prefer: count=exact" | grep content-range

# Filter by date
?created_at=gte.2025-01-01&created_at=lt.2025-02-01

# Select specific fields
?select=channel_name,channel_id

# Order and limit
?order=created_at.desc&limit=10

# Filter by value
?channel_id=eq.1342763350815277067

# Filter by multiple values
?channel_id=in.(123,456,789)
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
- `embeds` - embedded content
- `reaction_count`, `reactors`
- `reference_id` - for reply threading in regular channels
- `thread_id` - for forum-style channels (resources), identifies which post/thread a message belongs to

**discord_channels:**
- `channel_id`, `channel_name`
- `category_id`, `description`

**discord_members:**
- `member_id`, `username`, `global_name`
- `avatar_url`, `twitter_handle`

**daily_summaries:**
- `daily_summary_id`, `date`, `channel_id`
- `full_summary` - structured JSON with topics
- `short_summary` - bullet point highlights

**message_stats:**
- `channel_id`, `channel_name`
- `message_count`, `unique_authors`
- `first_message_at`, `last_message_at`

### Daily Summary JSON Structure
```json
{
  "title": "Topic headline",
  "mainText": "Overview with **user attribution**",
  "message_id": "link to source message",
  "channel_id": "channel ID",
  "subTopics": [
    {
      "text": "Sub-discussion point",
      "subTopicMediaMessageIds": ["msg_id1", "msg_id2"],
      "message_id": "source message"
    }
  ]
}
```

---

## Data Coverage

### Message Timeline
| Period | Messages | Notes |
|--------|----------|-------|
| Aug - Dec 2023 | 124,595 | Early AnimateDiff era |
| Jan - Dec 2024 | 262,808 | FLUX, SD3, CogVideoX era |
| Jan - Jun 2025 | 273,282 | Wan, LTX, HunyuanVideo emerge |
| Jul - Dec 2025 | 319,886 | High activity period |
| Jan 2026 | 66,053 | Current month |

### Summary Coverage
- **Date range:** Nov 4, 2025 - Jan 29, 2026 (~87 days)
- **Channels with summaries:** 21 of 227

### Channels With Daily Summaries
- wan_chatter, wan_comfyui, wan_training, wan_gens, wan_resources
- ltx_chatter, ltx_training, ltx_resources, ltx_gens
- hunyuanvideo, flux, comfyui, chroma, trellis
- kandinsky-5, qwen-image, sora, z-image, newbie

---

## Key Findings

### Complete Message Coverage
The database has **continuous coverage** from August 2023 to present:
- **1M+ messages** spanning 2.5 years of open source AI development
- 2024 data (262K messages) includes FLUX, SD3, CogVideoX, and early HunyuanVideo discussions
- Gap was filled by @pom in January 2026

### Top Contributors
| Rank | Username | Messages | Top Channel |
|------|----------|----------|-------------|
| 1 | **Kijai** | 103,556 | wan_chatter |
| 2 | Draken | 62,016 | comfyui |
| 3 | Cubey | 21,935 | comfyui |
| 4 | ˗ˏˋ⚡ˎˊ- | 18,268 | wan_chatter |
| 5 | Juampab12 | 17,780 | wan_chatter |

- **Kijai alone accounts for ~10% of all messages**
- 8,145 unique authors across 1M+ messages
- **wan_chatter** is the most common top channel

### Daily Summaries: How They're Generated
Found the source code: [brain-of-bdnc/news_summary.py](https://github.com/banodoco/brain-of-bdnc/blob/main/src/features/summarising/subfeatures/news_summary.py)

**Generation process:**
- **Model:** Claude Sonnet 4.5 for generation, GPT-5.2 with "high reasoning effort" for verification
- **Chunking:** 1000 messages at a time, combined to top 3-5 items
- **Verification:** Checks for attribution errors, unsupported claims, logical leaps, invented details

**Prompt priorities (in order):**
1. Original creations by community members (nodes, workflows, tools, LoRAs)
2. Notable achievements and demonstrations
3. High-engagement content (reactions/comments)
4. New features people are excited about
5. Shared workflows with examples

**Key insight:** Reference knowledge IS captured but framed as "news". When someone discovers "FP32 compute improves quality", it's captured as a news item even though it's durable reference knowledge.

**Important caveat:** Peter (@pom) noted the GPT-5.2 verification step was only added this week (late Jan 2026). Earlier summaries may contain inaccuracies - attribution errors, unsupported claims, etc. This adds more reason to re-process everything rather than using summaries as-is.

### Daily Summaries Contain Reference Knowledge
Looking at actual summaries, they include:
- **Technical settings:** FP32 vs BF16 flags, sampler recommendations, resolution tables
- **Workflow techniques:** Dual-model approaches, step counts for effects
- **Training knowledge:** LoRA strength conversions, captioning best practices
- **Troubleshooting:** SageAttention issues, facial changes during relighting
- Plus: attribution, media links, structured format

### Raw Chat Contains Buried Q&A
Extraction from wan_chatter (50K messages) found:
- 11,544 potential questions (23% of messages)
- 5,605 Q&A reply pairs (via `reference_id`)
- 662 solution mentions, 793 error discussions
- Synthesized into 14 troubleshooting entries, 6 tips, 5 FAQs

### Channel Categories
- **Video:** wan_*, ltx_*, hunyuanvideo, cogvideox, mochi, animatediff, sora, veo3
- **Image:** flux, sdxl, chroma, omnigen, qwen-image
- **Training:** *_training channels, training_control_loras
- **Technical:** comfyui, nodes, ml_engineering, ml_papers
- **3D/Motion:** trellis, hunyuan3d, liveportrait
- **Audio:** mmaudio, ace-step, music, yue, zonos

### Resources Channels (Forum-Style, High Value)
These are Discord forum channels where each "post" is a thread. Use `thread_id` to group messages.

| Channel | Forum Posts | Total Messages | Avg Msgs/Post |
|---------|-------------|----------------|---------------|
| wan_resources | 50 | 10,224 | 204 |
| ltx_resources | 45 | 2,808 | 62 |
| resources | 114 | 4,374 | 38 |
| **Total** | **~209** | **17,406** | - |

**Content:** Curated workflows, LoRAs, techniques shared by community members with discussion threads.

### High-Value Message Subsets
For filtering the 1M+ messages to high-value content:

| Filter | Count | Notes |
|--------|-------|-------|
| Messages with 3+ reactions | 42,058 | Community-validated value |
| Messages with attachments | 154,642 | Workflows, examples, media |
| Long messages (>300 chars) | ~21,000 | Substantive content |
| Messages with thread_id | 32,430 | Forum-style discussions |
| Kijai's messages | 103,609 | Expert knowledge |

---

## LLM Processing Cost Estimates

### Decision: Don't Trust Existing Daily Summaries
- Summaries only cover ~87 days (Nov 2025 - Jan 2026)
- GPT verification step added only late Jan 2026; earlier summaries may have errors
- Want to cover full 2.5 year archive
- Will regenerate from raw messages

### Processing All 1M Messages = Too Expensive
- 1M+ messages × ~50 tokens avg = 50M+ input tokens
- With Opus 4.5 ($15/M input, $75/M output): **~$1,500+**
- Not practical

### Smart Filtering Approach = ~$60-110
By filtering to high-value content first:

| Tier | Content | Volume | Opus Cost |
|------|---------|--------|-----------|
| 1 | Resources (209 forum threads) | ~17K msgs in 209 units | ~$5-10 |
| 2 | High-signal chatter (3+ reactions, >300 chars, attachments) | ~50-60K msgs | ~$50-75 |
| 3 | Q&A threads (questions + expert replies) | ~30-40K msgs | ~$30-45 |
| **Total** | | ~100-150K msgs | **~$60-110** |

With Sonnet instead of Opus: **~$15-25**

---

## Next Steps

### Knowledge Base (Current Focus)

**Revised approach - Process raw messages, not summaries:**

**Tier 1: Resources Channels (Highest Priority)**
- 209 forum posts across wan_resources, ltx_resources, resources
- Each post = curated workflow/LoRA/technique + discussion thread
- Process each thread as a unit (opening post + key replies)
- Estimated cost: ~$5-10 with Opus

**Tier 2: High-Signal Chatter Messages**
- Filter by: 3+ reactions, >300 chars, has attachments, expert authors
- Use `reference_id` to reconstruct Q&A threads
- Estimated cost: ~$50-75 with Opus

**Tier 3: Expert Knowledge Mining**
- Kijai's 104K messages (filter for substantive ones)
- Other top contributors
- Focus on technical explanations, not casual chat

**Open questions:**
- Best format? Static pages vs RAG vs chat interface?
- How to keep content fresh as field evolves rapidly?
- Start with Sonnet to validate approach, then upgrade to Opus if needed?

**To build:**
- Script to fetch and process forum threads (using `thread_id`)
- Script to filter high-value chatter messages
- Prototype extraction on one forum thread to validate approach

### Stats & Visualization
See `docs/stats-ideas.md` for full list. Priority items:
1. Activity timeline (messages per month)
2. Most reacted messages
3. Activity heatmap (hour/day)
4. Model mentions over time

---

## Useful Example Queries

```bash
# Get all channel names
curl -s "...discord_channels?select=channel_name&order=channel_name" -H "apikey: ..."

# Get recent messages from a channel
curl -s "...discord_messages?channel_id=eq.1342763350815277067&order=created_at.desc&limit=10" -H "apikey: ..."

# Get daily summaries for a specific channel
curl -s "...daily_summaries?channel_id=eq.1342763350815277067&order=date.desc" -H "apikey: ..."

# Get messages with attachments
curl -s "...discord_messages?attachments=not.eq.[]&limit=10" -H "apikey: ..."

# Get channel stats ordered by message count
curl -s "...message_stats?order=message_count.desc&limit=20" -H "apikey: ..."

# Get all messages in a forum thread (by thread_id)
curl -s "...discord_messages?thread_id=eq.{THREAD_ID}&order=created_at.asc" -H "apikey: ..."

# Get unique thread_ids in a channel (forum posts)
curl -s "...discord_messages?channel_id=eq.{CHANNEL_ID}&select=thread_id" -H "apikey: ..."

# Get high-value messages (3+ reactions)
curl -s "...discord_messages?reaction_count=gte.3&order=reaction_count.desc" -H "apikey: ..."
```
