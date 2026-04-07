---
title: Video-to-Video Denoise Settings
aliases: [v2v-denoise, denoise-strength, v2v-steps]
last_updated: 2025-03-09
---

# Video-to-Video Denoise Settings

When using video-to-video (V2V) workflows with Wan, the denoise strength parameter controls how much the model modifies the input video. Understanding how denoise interacts with step count is critical for efficient V2V generation.

## How Denoise Affects Steps

**Important:** When using V2V with reduced denoise (e.g., 30% denoise), the model still processes the **full number of steps** specified, not a reduced number.

> "should that still be taking 50 steps with the wrapper?" — DevouredBeef, March 8, 2025

> "Actually no i think it does some stuff with the steps vs noise im not 100% sure the ratio but i think the closer you get back to 1. denoise the closer it goes to the 50 steps" — Colin, March 8, 2025

**Key insight:** The inference time remains the same regardless of denoise strength. A 30% denoise at 50 steps takes the same time as 100% denoise at 50 steps.

> "Well based on the inference time it's taking the same time as if the denoise strength was 100%" — DevouredBeef, March 8, 2025

## Optimizing V2V Workflows

### Manual Step Reduction

To speed up V2V with low denoise, **manually reduce the step count** rather than relying on denoise to skip steps:

> "let me try manually dropping the step count without teacache" — DevouredBeef, March 8, 2025

> "yep that's done the trick I think, not sure why I assumed the steps would be updated internally" — DevouredBeef, March 8, 2025

**Example:**
- Instead of: 50 steps at 30% denoise
- Try: 15-20 steps at 30% denoise
- Result: Same quality, much faster generation

### TeaCache Considerations

When using TeaCache with V2V:

1. **TeaCache needs recalibration for each denoise change**
   - Different denoise strengths require different TeaCache thresholds
   - "obviously with teacache that isn't much of a hit, except it needs completely recalibrated for each denoise change" — DevouredBeef, March 8, 2025

2. **Reduce threshold to compensate for perceived step count**
   - If using 50 steps at 30% denoise, TeaCache sees it as a full 50-step inference
   - Lower the threshold to maintain speed benefits
   - "Main point, if I reduce teacache's threshold to compensate, since it's a perceived 50 step inference I'll lose some speed" — DevouredBeef, March 8, 2025

## Recommended Workflow

For efficient V2V generation:

1. **Determine your target denoise strength** (e.g., 30%)
2. **Calculate appropriate step count** (e.g., 15-20 steps for 30% denoise)
3. **Set steps manually** rather than using full steps with low denoise
4. **Adjust TeaCache threshold** if using TeaCache
5. **Test and iterate** to find optimal balance

## Common Denoise Ranges

| Denoise Strength | Use Case | Recommended Steps |
|-----------------|----------|-------------------|
| **10-30%** | Minor modifications, style transfer | 10-15 steps |
| **30-50%** | Moderate changes, motion adjustment | 15-25 steps |
| **50-70%** | Significant changes, character replacement | 25-35 steps |
| **70-100%** | Major transformations, full regeneration | 30-50 steps |

## See Also

- [[flowedit]] — V2V technique using FlowEdit
- [[latent-guides]] — Alternative V2V approach
- [[teacache]] — Speed optimization for V2V workflows
- [[wan-2.1]] — Base model for V2V generation
