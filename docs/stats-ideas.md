# Stats Ideas

Potential statistics and visualizations to build for the Banodoco Knowledge Base.

## Time-Based Analysis
- **Activity heatmap** - Messages by hour of day / day of week (when is the community most active?)
- **Growth timeline** - Messages per month trend over 29 months
- **Busiest days ever** - What events caused activity spikes?
- **Response time patterns** - How quickly do questions get answered?

## Channel Analysis
- **Top channels by message count** - Already available in message_stats table
- **Channel growth/decline** - Which channels are rising vs fading over time?
- **Channel overlap** - Users who are active across multiple channels
- **Channel comparison** - Side-by-side activity metrics

## Engagement Metrics
- **Most reacted messages** - Using reaction_count field
- **Most replied-to threads** - Using reference_id to find popular threads
- **Users who get the most reactions** - Who's dropping knowledge that resonates?
- **Average reactions per message by channel** - Which channels have highest engagement?

## Content Analysis
- **Attachment stats** - How many images/videos shared? Breakdown by channel
- **Link sharing patterns** - Most shared domains (GitHub, HuggingFace, Civitai, etc.)
- **Message length distribution** - Quick questions vs detailed explanations
- **Code/workflow sharing** - Messages containing code blocks or JSON

## Community Health
- **User retention** - Of people who joined in 2023, how many are still active?
- **New member onboarding** - Time from join to first message
- **Power law distribution** - What % of messages come from top 1%, 10%, 50%?
- **Lurker ratio** - Members who never posted vs active contributors

## Technical/Topic-Specific
- **Model mentions over time** - Track when "Wan" overtook "AnimateDiff", FLUX adoption, etc.
- **Training vs inference discussions** - Ratio of training-focused vs usage-focused content
- **The "Kijai effect"** - What topics/channels does Kijai engage with most?
- **Hardware discussions** - VRAM requirements, GPU mentions over time

## From Daily Summaries
- **Most mentioned contributors** - Who appears in AI-generated summaries most frequently?
- **Discovery timeline** - Major technical breakthroughs extracted from summaries by date
- **Topic clustering** - What themes and categories emerge from summary content?
- **Summary coverage gaps** - Which active channels don't have summaries yet?

## Network Analysis (Advanced)
- **Who replies to whom** - Build a reply graph
- **Community clusters** - Groups of users who interact frequently
- **Key connectors** - People who bridge different channels/topics
- **Influence flow** - How do ideas spread through the community?

---

## Implementation Priority

### Quick wins (data readily available)
1. Top channels by message count
2. Most reacted messages
3. Activity by month timeline
4. Power law distribution of contributors

### Medium effort
5. Activity heatmap (hour/day)
6. Channel growth over time
7. Most mentioned contributors in summaries
8. Link domain analysis

### Requires more processing
9. Model mentions over time (text search)
10. Topic clustering from summaries
11. Reply network analysis
12. User retention cohorts
