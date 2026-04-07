---
title: Context Windows for Long Video
aliases: [context-windows, context-window, long-video]
last_updated: 2025-03-18
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

### Context Stride

**Controls how many frames to advance for each window.**

Rule of thumb: Smaller values create more windows with greater overlap but may be more redundant.

Typical settings:
- **4-8:** More windows, smoother potential results, slower generation
- **16-24:** Fewer windows, potentially faster generation
- **Match with your frame rate:** Setting to your natural frame rate (e.g., 8 for 24fps) can be intuitive

> "Context Stride (default: 4)" — fredbliss, March 17, 2025

### Context Overlap

**Controls how many frames at window edges are blended.**

Rule of thumb: More overlap means smoother transitions between windows but higher computation cost.

Typical settings:
- **8-12:** Minimal but functional blending
- **16-24:** Standard blending for good transitions
- **32-48:** Extra-smooth blending for videos with complex motion

> "Context Overlap (default: 16)" — fredbliss, March 17, 2025

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

**March 17, 2025 update:** Pipe separator `|` is the standard syntax for multi-prompt context windows:

```
Aerial view of a coastal village on a sunny day with calm sea and clear blue sky |
Clouds gradually forming and darkening, wind picking up as waves grow higher |
Heavy storm with rain pouring down, lightning in distance, dramatic seas |
Storm clearing gradually, rainbow appearing as sunlight breaks through clouds
```

> "Aerial view of a coastal village on a sunny day with calm sea and clear blue sky | Clouds gradually forming and darkening, wind picking up as waves grow higher | Heavy storm with rain pouring down, lightning in distance, dramatic seas | Storm clearing gradually, rainbow appearing as sunlight breaks through clouds" — fredbliss, March 17, 2025

### Multi-Window Prompts

For longer videos, separate prompts with `|` pipes:
```
scene 1 description | scene 2 description | scene 3 description
```

Keep prompts very similar between windows to avoid jarring transitions.

**Prompt blending experiments (March 17-18, 2025):**

fredbliss has been working on advanced prompt blending techniques for context windows:

> "A red sheep jumps over a fence at dusk | A red sheep jumps over a fence at night | A red sheep jumps over a fence at night, stars in sky | A red sheep jumps over a fence at dawn, sun rising" — fredbliss, March 17, 2025

However, combining loop and blend techniques proved challenging:

> "loop and blend dont seem to play well together" — fredbliss, March 17, 2025

> "or im doing something very wrong" — fredbliss, March 17, 2025

## Looping with Context Windows

**Kijai's recommendation (March 18, 2025):**

For looping videos, use the `uniform_looped` context schedule instead of the Mobius looping technique:

> "I don't feel like it's any good, somewhat works with 1.3B model but not the others.. I prefer using the context options for looping" — Kijai, March 18, 2025

**Setup for looping:**
- Use `uniform_looped` context schedule
- Minimum 169 frames (2 windows) for proper looping
- 81 frame context window size
- 16 frame overlap recommended

> "it's not good at that little frames, you want to use 81 as the context window size and do something like 169 frames" — Kijai, March 18, 2025

**I2V looping:**

Kijai had limited success with I2V looping using context windows:

> "yea, but i never had much luck with I2V" — Kijai, March 18, 2025

For I2V, use `uniform_looped` context schedule for best results.

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
- **1353 frames** at 832x480 with 30 steps in 25 minutes 37 seconds on unspecified hardware (Kijai, March 18, 2025)
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

**1353-frame generation (Kijai, March 18, 2025):**
- Resolution: 832x480
- Frames: 1353
- Steps: 30
- Time: 25 minutes 37 seconds (51.25s/it)
- Result: "weird goat hybrids"

> "Sampling 1353 frames at 832x480 with 30 steps 100%|██████████████████████████████████████████████████████████████████████████████████| 30/30 [25:37<00:00, 51.25s/it]" — Kijai, March 18, 2025 [👀x2 🔥]

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
| **Mobius Looping** | 81-161 frames | Good (1.3B), Fair (14B) | Fast | Low |

**Context Windows vs RifleX:**

In direct comparison at 161 frames:
- Context windows: Better temporal consistency, less looping
- RifleX: Constant looping artifacts, less stable, VRAM constrained

> "Kj did a sliding context with no riflex, that looked better than riflex lol. tbh, ive seen very little worth from riflex" — Draken, March 4, 2025

> "Context windows and TeaCache don't work together and leads to noise" — Kijai, March 3, 2025

**Context Windows vs Mobius Looping:**

Kijai's assessment (March 18, 2025):
- Mobius: Works somewhat with 1.3B, not reliable for 14B or I2V
- Context windows: Preferred for production looping, more reliable

> "I don't feel like it's any good, somewhat works with 1.3B model but not the others.. I prefer using the context options for looping" — Kijai, March 18, 2025

## Workflow Examples

Kijai posted example workflows in the repository. Key workflow from March 3, 2025 demonstrates:
- Multi-prompt support with `|` separator
- Proper overlap and stride settings
- Integration with I2V

## Advanced: Prompt Blending Research

**fredbliss's WanSAE project (March 18, 2025):**

fredbliss is developing an embedding transition autoencoder to improve context window transitions:

**Core problem:** Semantic transition understanding in video generation

**Key questions:**
1. How do semantic concepts transform between prompts?
2. Can we mathematically model the "distance" between conceptual spaces?
3. How can we create more intelligent bridges between disparate visual ideas?

**Proposed solution:**
- Learn latent representation of prompt transitions
- Develop metrics for transition "difficulty"
- Create predictive model for generating bridge prompts
- Enable more sophisticated context windowing

**Technical approach:**
- Focus on T5 embeddings (no CLIP dependency)
- Train on curated transition pairs
- Build analysis tools to quantify semantic shifts
- Develop recommendations for smooth blending

> "by modeling the mathematical relationship between prompt embeddings, we can: predict transition quality, recommend intelligent blending strategies, potentially extend video generation beyond current 81-frame limit" — fredbliss (via Claude summary), March 18, 2025

**Current status:** Early research phase, combining ideas from ColPali for multi-vector embeddings.

## See Also

- [[wan-2.1]] — Base model that uses context windows
- [[vace]] — VACE compatibility with context windows
- [[svi]] — Alternative for very long video
- [[teacache]] — Incompatible with context windows
- [[samplers]] — Sampler choices for context window workflows
- [[riflex]] — Alternative long-video technique (inferior to context windows)
- [[mobius-looping]] — Alternative looping technique (context windows preferred)

## External Resources

- [AnimateDiff Evolved Context Documentation](https://github.com/Kosinkadink/ComfyUI-AnimateDiff-Evolved/tree/main/documentation/nodes#context-optionsstandard-uniform) — Best documentation of how context windows work
