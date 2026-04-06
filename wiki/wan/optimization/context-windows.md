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

> "the whole point of long ctx and context sliding is to be able to break the vram limits. you are only ever working on the context_length of frames" — Draken, March 4, 2025

## Settings

| Parameter | Recommended Value | Notes |
|-----------|------------------|-------|
| **Window size** | 81 frames | Match native training length for best quality |
| **Overlap** | 5-16 frames (wrapper), 16-24 frames (native) | More overlap = smoother transitions but slower. 16 frames commonly used. 24 reported as good for keeping to original image |
| **Shift** | 8-15 | Higher shift works better with context windows |
| **Prompts** | Separate with `|` | One prompt per window; keep very similar |
| **Stride** | ≤10 (for HN), 4-8 (general) | Stride >10 crashes high noise context windows. Stride 8 can go "crazy" |

## Multi-Prompt Support

Context windows support multiple prompts separated by `|` pipes, with one prompt applied per window:

```
old man is laughing|old man is crying
```

**Important notes:**
- Each prompt is applied to one context window (20 latents = 80 frames)
- Prompts should be mostly the same with small variations
- The full prompt is used for each window, not just the changed portion
- The console log shows which prompt is used for which window via "Prompt index"
- Prompts that are too different will cause visible scene changes between windows

**Example workflow:**
- 6 context windows = 6 prompts possible
- Each window processes ~80 frames (20 latents × 4 frames per latent)
- Prompts should maintain consistency while varying specific details

> "you'd use mostly same prompt and change some bit of it" — Kijai, March 3, 2025

> "like here it was 'man walks to the ocean|a shark attacks the man' and it did keep the man but everything else changed" — Kijai, March 3, 2025

### Prompt Index Behavior

The console output shows which prompt is being applied to which frames:

```
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Prompt index: 0
[3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
Prompt index: 1
```

This indicates frames 0-10 use prompt 0, frames 3-13 use prompt 1, etc. The overlap means some frames see blended prompts.

**Common issues:**
- Prompt index 0 is sometimes skipped entirely
- Uneven distribution of prompt indices across windows
- Difficulty achieving even splits with certain frame counts and overlap settings

> "i can't seem to get an even number of stride/overlaps here, so there's never an even split of prompt indices" — TK_999, March 4, 2025

## Compatibility

**Works with:**
- Wan 2.1 T2V (all sizes)
- Wan 2.1 I2V (reuses same conditioning image per window)
- Native ComfyUI (after Kosinkadink's custom slicing merged)
- Kijai wrapper

**Does NOT work with:**
- TeaCache (produces noise artifacts) — confirmed incompatible by Kijai, March 2, 2025
- Stock VACE 2.1 (until custom slicing merged)

## I2V with Context Windows

Context windows work with I2V by reusing the same conditioning image across all windows. Kijai posted a workflow for this on March 2, 2025.

**Current limitations:**
- Cannot grab the last frame of each context window as new conditioning
- Cannot inject a new start frame for each window
- The model won't work with unfinished images
- Each window can have its own image (not yet implemented as of March 3, 2025)

> "giving each window it's own image should work though" — Kijai, March 3, 2025

> "Long Context with image to vid..." — Flipping Sigmas, March 3, 2025

Note that long I2V generations with context windows will take several hours.

**I2V-specific issues:**
- First window (frames 1-81) may feel like it has to "reset" after initial generation
- Subsequent windows (2→3, 3→4) blend more smoothly
- The image has to "reset" after the first window before other windows get along

> "with i2v, it feels like the image has to 'reset' after the first window [1-81]... maybe its my limited test and needs more, but it felt like after that one time, the other windows get along" — Cubey, March 4, 2025

## Known Issues

- **Visible quality drops** at window boundaries in long generations
- **Missing frames** not covered by windows get duplicated to closest window, causing jittering on interpolation
- **Slower than single-pass** due to overlap processing
- **Color drift** can occur over many windows
- **Stride limitations:** Setting stride >10 crashes high noise context windows
- **Context options connection:** Connecting context options to the second (LN) sampler in dual-sampler setups can break with negative dimensions; put context on HN, less overlap on LN (16 vs 48)
- **TeaCache incompatibility:** Cannot be combined with TeaCache — Kijai noted "can't figure out teacache for context windows though, maybe not even possible..." (March 2, 2025)
- **Precision sensitivity:** Some users reported better results with bf16 than fp16 for context window workflows
- **First window reset:** I2V workflows show visible reset between first and second window
- **Prompt index skipping:** Prompt index 0 is often skipped or not evenly distributed
- **Uneven prompt distribution:** Difficult to achieve even splits of prompts across windows with certain settings

## Benchmarks

- **257 frames** generated successfully with 1.3B model in 5 minutes using ~4.8 GB VRAM (Kijai, March 1, 2025)
- **325 frames** at 81 context, ~1600 seconds on 4090 (ajo6268, March 3, 2025)
- **513 frames** at 832x480 in 50 minutes on 5090 (Kijai, March 3, 2025)
- **1025+ frames** possible on modest VRAM with proper settings
- Context windows outperform RifleX for temporal consistency (tested at 161 frames)

### Notable Generations

**513-frame generation (Kijai, March 3, 2025):**
- Resolution: 832x480
- Window size: 81
- Overlap: 16
- Model: 14B
- Time: 50 minutes on 5090
- Prompt: "red panda playing with baby hippo on grass, chasing each other"
- Result: Smooth transitions with minimal visible context shifts

> "I think this might be a record for the longest single oss video gen in one go." — orabazes, March 3, 2025

## Window Blending

Kijai's implementation uses window blending code from Kosinkadink (AnimateDiff) to reduce noise between context windows:

- Standard uniform context windows are used as the base
- Additional blending is applied on top to reduce noise
- Does not implement attention fusing or other advanced techniques
- The blending happens after CFG math

> "the context windows themselves are the standard uniform, doing this to blend them in top of that as there was lots of noise otherwise" — Kijai, March 3, 2025

## Comparison to Alternatives

| Method | Max Length | Quality | Speed | VRAM |
|--------|-----------|---------|-------|------|
| **Context Windows** | 1000+ frames | Good with quality drops | Slow | Low |
| **RifleX** | ~161 frames | Inferior to context windows | Fast | High (VRAM constrained) |
| **Frame Extension** | Unlimited | Degrades after 3-5 iterations | Medium | Low |
| **SVI** | Unlimited | Best for pure continuation | Medium | Medium |

**Context Windows vs RifleX:**

In direct comparison at 161 frames:
- Context windows: Better temporal consistency, less looping
- RifleX: Constant looping artifacts, less stable, VRAM constrained

> "Kj did a sliding context with no riflex, that looked better than riflex lol. tbh, ive seen very little worth from riflex" — Draken, March 4, 2025

> "Context windows and TeaCache don't work together and leads to noise" — Kijai, March 3, 2025

## Workflow Examples

Kijai posted example workflows in the repository. Key workflow from March 3, 2025 demonstrates:
- Multi-prompt support with `|` separator
- Proper overlap and stride settings
- Integration with I2V

## See Also

- [[wan-2.1]] -- Base model that uses context windows
- [[vace]] -- VACE compatibility with context windows
- [[svi]] -- Alternative for very long video
- [[teacache]] -- Incompatible with context windows
- [[samplers]] -- Sampler choices for context window workflows
- [[riflex]] -- Alternative long-video technique (inferior to context windows)

## External Resources

- [AnimateDiff Evolved Context Documentation](https://github.com/Kosinkadink/ComfyUI-AnimateDiff-Evolved/tree/main/documentation/nodes#context-optionsstandard-uniform) — Best documentation of how context windows work
