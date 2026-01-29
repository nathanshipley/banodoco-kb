# Banodoco Discord Knowledge Base Project

## Project Goal
Transform the Banodoco Discord database into a useful web-based knowledge base about Open Source AI tools (video generation, image generation, training, ComfyUI, etc.).

**Live site:** https://nathanshipley.github.io/banodoco-kb/

## Project Structure

```
banodoco-kb/
├── index.html              # Hub page linking to all sections
├── database.html           # Database overview and exploration
├── stats.html              # Community stats (top contributors)
├── scripts/
│   └── get_top_authors.py  # Fetches top contributors from API
├── data/
│   └── top_authors.json    # Cached stats data
├── docs/
│   └── stats-ideas.md      # Future stats/visualization ideas
├── CLAUDE.md               # This file
└── README.md               # GitHub readme
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
- `reference_id` - for reply threading

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

### Daily Summaries Are High Quality
The AI-generated summaries include:
- Specific technical details (VRAM, LoRA strengths, samplers)
- Attribution to community experts by name
- Links back to source messages
- Structured topics with subtopics

### Channel Categories
- **Video:** wan_*, ltx_*, hunyuanvideo, cogvideox, mochi, animatediff, sora, veo3
- **Image:** flux, sdxl, chroma, omnigen, qwen-image
- **Training:** *_training channels, training_control_loras
- **Technical:** comfyui, nodes, ml_engineering, ml_papers
- **3D/Motion:** trellis, hunyuan3d, liveportrait
- **Audio:** mmaudio, ace-step, music, yue, zonos

---

## Next Steps

### Stats & Visualization
See `docs/stats-ideas.md` for full list. Priority items:
1. Top channels by message count
2. Activity timeline (messages per month)
3. Most reacted messages
4. Activity heatmap (hour/day)

### Knowledge Base
1. Deep dive into daily_summaries structure
2. Design navigation (by model, topic, contributor, date)
3. Build search/browse interface
4. Generate retrospective summaries for Aug 2023 - Oct 2025

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
```
