# Banodoco Discord Knowledge Base Project

## Project Goal
Transform the Banodoco Discord database into a useful web-based knowledge base about Open Source AI tools (video generation, image generation, training, ComfyUI, etc.).

## Database Access

### Supabase REST API
```bash
curl "https://ujlwuvkrxlvoswwkerdf.supabase.co/rest/v1/{TABLE_NAME}" \
  -H "apikey: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InVqbHd1dmtyeGx2b3N3d2tlcmRmIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NjczNzcyMzcsImV4cCI6MjA4MjczNzIzN30.XSTztghf_6a_bpR62wZdoA4S4oafJFDMoPQDRR4dT08"
```

### Useful Query Patterns
```bash
# Get row count
curl -s "URL?select=count" -H "apikey: KEY" -H "Prefer: count=exact" -I | grep content-range

# Filter by date
?created_at=gte.2025-01-01&created_at=lt.2025-02-01

# Select specific fields
?select=channel_name,channel_id

# Order results
?order=created_at.desc

# Limit results
?limit=10

# Filter by value
?channel_id=eq.1342763350815277067

# Filter by multiple values
?channel_id=in.(123,456,789)
```

## Database Schema

### Core Tables

| Table | Count | Description |
|-------|-------|-------------|
| `discord_messages` | 727,352 | All chat messages |
| `discord_members` | 4,477 | User profiles |
| `discord_channels` | 227 | Channel metadata |
| `daily_summaries` | 429 | AI-generated daily summaries |

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

## Data Coverage

### Message Timeline
| Period | Messages | Notes |
|--------|----------|-------|
| Aug - Dec 2023 | 124,595 | Early AnimateDiff era |
| Jan 2024 | 22,135 | Last month before gap |
| **Feb 2024 - Jan 2025** | **0** | **12-MONTH DATABASE GAP** |
| Feb - Jun 2025 | 236,407 | Post-gap recovery |
| Jul - Dec 2025 | 300,288 | High activity period |
| Jan 2026 | 43,927 | Current month |

### Summary Coverage
- **Date range:** Nov 4, 2025 - Jan 24, 2026 (~82 days)
- **Channels with summaries:** 21 of 227

### Channels With Daily Summaries
- wan_chatter, wan_comfyui, wan_training, wan_gens, wan_resources
- ltx_chatter, ltx_training, ltx_resources, ltx_gens
- hunyuanvideo, flux, comfyui, chroma, trellis
- kandinsky-5, qwen-image, sora, z-image, newbie

## Key Findings

### The 12-Month Gap
The database is missing all messages from **February 1, 2024** to **January 31, 2025**. This period includes:
- FLUX release and adoption
- Stable Diffusion 3
- CogVideoX
- Early HunyuanVideo discussions

**Action needed:** Check if this data can be recovered or re-scraped.

### Daily Summaries Are High Quality
The AI-generated summaries include:
- Specific technical details (VRAM, LoRA strengths, samplers)
- Attribution to community experts by name
- Links back to source messages
- Structured topics with subtopics

### Channel Categories (from exploration)
- **Video:** wan_*, ltx_*, hunyuanvideo, cogvideox, mochi, animatediff, sora, veo3
- **Image:** flux, sdxl, chroma, omnigen, qwen-image
- **Training:** *_training channels, training_control_loras
- **Technical:** comfyui, nodes, ml_engineering, ml_papers
- **3D/Motion:** trellis, hunyuan3d, liveportrait
- **Audio:** mmaudio, ace-step, music, yue, zonos

## Files Created

- `banodoco_db_exploration.html` - Visual summary of database exploration (for GitHub sharing)

## Next Steps

1. **Investigate the data gap** - Can Feb 2024 - Jan 2025 be recovered?
2. **Deep dive into daily_summaries** - Extract and display the structured content
3. **Build export pipeline** - Scripts to transform data for knowledge base
4. **Design navigation** - Browse by model, topic, contributor, or date
5. **Generate retrospective summaries** - For Aug 2023 - Jan 2024 content

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
```
