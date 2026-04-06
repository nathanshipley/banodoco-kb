---
title: Context Windows for Long Video
aliases: [context-windows, context-window, long-video]
last_updated: 2025-03-02
---

# Context Windows for Long Video

Context windows are a technique for generating videos longer than the model's native training length (81 frames for Wan 2.1) by processing the video in overlapping chunks. This allows generating hundreds or even thousands of frames while keeping VRAM usage bounded to a single window's worth.

## How It Works

The model processes the video in sliding windows:
1. Generate frames 0-81
2. Generate frames 76-157 (reusing frames 76-81 from previous window)
3. Generate frames 152-233 (reusing frames 152-157)
4. Continue...

Memory stays bounded because only one window is processed at a time. The overlap provides continuity between windows.

## Settings

| Parameter | Recommended Value | Notes |
|-----------|------------------|-------|
| **Window size** | 81 frames | Match native training length for best quality |
| **Overlap** | 5-16 frames | More overlap = smoother transitions but slower. 24 frames reported working well by Kijai |
| **Shift** | 8-15 | Higher shift works better with context windows |
| **Prompts** | Separate with `|` or `->` | One prompt per window; keep very similar. `->` syntax works for scene transitions |
| **Stride** | ≤10 | Stride >10 crashes high noise context windows |

### Overlap Recommendations

Based on community testing (March 2, 2025):
- **16 frames:** Minimum for basic continuity; may show visible seams
- **24 frames:** Good balance reported by Kijai; reduces morphing artifacts
- **More overlap:** Smoother transitions but slower generation

## Compatibility

**Works with:**
- Wan 2.1 T2V (all sizes)
- Wan 2.1 I2V (reuses same conditioning image per window)
- Native ComfyUI (after Kosinkadink's custom slicing merged)
- Kijai wrapper

**Does NOT work with:**
- TeaCache (produces noise artifacts) — confirmed incompatible by Kijai, March 2, 2025
- Stock VACE 2.1 (until custom slicing merged)

## Prompting for Context Windows

### Scene Transitions

Kijai demonstrated effective scene transition syntax on March 2, 2025:

```
an old man gets up and walks away into the sea -> a shark attacks the old man -> huge explosion
```

```
red panda eats an ice cream -> red panda walks away
```

The `->` separator works well for indicating scene transitions. The model understands this syntax and creates smooth transitions between scenes.

### Multi-Window Prompts

For longer videos, separate prompts with `|` pipes:
```
scene 1 description | scene 2 description | scene 3 description
```

Keep prompts very similar between windows to avoid jarring transitions.

## Known Issues

- **Visible quality drops** at window boundaries in long generations
- **Missing frames** not covered by windows get duplicated to closest window, causing jittering on interpolation
- **Slower than single-pass** due to overlap processing
- **Color drift** can occur over many windows
- **Stride limitations:** Setting stride >10 crashes high noise context windows
- **Context options connection:** Connecting context options to the second (LN) sampler in dual-sampler setups can break with negative dimensions; put context on HN, less overlap on LN (16 vs 48)
- **TeaCache incompatibility:** Cannot be combined with TeaCache — Kijai noted "can't figure out teacache for context windows though, maybe not even possible..." (March 2, 2025)

## Benchmarks

- **257 frames** generated successfully with 1.3B model in 5 minutes using ~4.8 GB VRAM (Kijai, March 1, 2025)
- **1025+ frames** possible on modest VRAM with proper settings
- Context windows outperform RifleX for temporal consistency (tested at 161 frames)
- **253 frames with RifleX** tested by toyxyz (March 2, 2025) — though RifleX may only work up to 2x default (161 frames)

## Long Context I2V

> "Long Context with image to vid..." — Flipping Sigmas, March 3, 2025

Context windows work with I2V by reusing the same conditioning image across all windows. Kijai posted a workflow for this on March 2, 2025. Note that this will take several hours for very long generations.

## Comparison to Alternatives

| Method | Max Length | Quality | Speed | VRAM |
|--------|-----------|---------|-------|------|
| **Context Windows** | 1000+ frames | Good with quality drops | Slow | Low |
| **RifleX** | ~161 frames (2x default) | Inferior to context windows | Fast | Low |
| **Frame Extension** | Unlimited | Degrades after 3-5 iterations | Medium | Low |
| **SVI** | Unlimited | Best for pure continuation | Medium | Medium |

## See Also

- [[wan-2.1]] -- Base model that uses context windows
- [[vace]] -- VACE compatibility with context windows
- [[svi]] -- Alternative for very long video
- [[teacache]] -- Incompatible with context windows
