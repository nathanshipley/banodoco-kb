---
title: FPS Sampling for Long Video
aliases: [fps-sampling, fps-based-sampling, apollo-sampling]
last_updated: 2025-03-02
---

# FPS Sampling for Long Video

FPS (frames per second) sampling is an experimental technique for long video generation based on the Apollo paper's findings. Instead of uniformly distributing frames across the entire video (which distorts temporal relationships), FPS sampling maintains consistent time intervals between frames by sampling at a target framerate.

**Status:** Experimental implementation by fredbliss (March 2, 2025). Not yet widely tested or confirmed to provide benefits over standard context windowing.

> "uniform_standard_fps maintains consistent time intervals between frames, while uniform_standard distributes frames evenly regardless of timing" — fredbliss, March 2, 2025

---

## How It Works

### Uniform Sampling (Standard)

Frames are distributed evenly across the entire video, regardless of duration. This means the temporal distance between frames changes depending on video length.

**Problem:** When videos exceed frame capacity, uniform sampling distorts temporal relationships.

### FPS Sampling (Apollo Paper)

Frames are sampled at a consistent rate (e.g., 2 frames per second). This maintains consistent time intervals between consecutive frames.

**Benefit:** Temporal relationships remain consistent regardless of video length.

---

## Implementation

fredbliss created an experimental fork of the Kijai wrapper implementing FPS sampling:

- **Repository:** https://github.com/fblissjr/ComfyUI-WanVideoWrapper
- **Example workflow:** `wanvideo_long_T2V_fps_sampling_experimental.json`
- **Release date:** March 2, 2025

### How It Combines with Context Windows

FPS sampling works alongside context windowing:

1. **Initial Sampling:** Sample frames at a consistent frame rate (e.g., 2 fps) instead of uniformly distributing across the entire video
2. **Window Application:** For very long videos, maintain this consistent fps within each context window, but distribute the windows themselves uniformly throughout the video
3. **Processing:** Process each context window independently (as standard context windows do)
4. **Blending:** Blend the results in the overlapping regions (as standard context windows do)

**Key difference:** Within each window, the temporal relationship between frames is consistent.

---

## Settings

| Parameter | Recommended Value | Notes |
|-----------|------------------|-------|
| **target_fps** | **2.0** | Apollo paper recommendation for best temporal understanding |
| **original_fps** | **30** | Reference baseline (average training data fps) |
| **context_schedule** | `uniform_standard_fps` | Maintains consistent time intervals |
| **context_frames** | 81 | Standard context window size |
| **context_overlap** | 16 | Standard overlap |
| **context_stride** | 4 | Standard stride |
| **freenoise** | true | Prevents repetitive patterns |

### Target FPS Variations

| target_fps | Effect | Use Case |
|------------|--------|----------|
| **1.0** | Slower perceived motion | Very long videos (>5 minutes) |
| **2.0** | Apollo recommended | Standard (best temporal understanding) |
| **3-4** | Faster perceived motion | Short videos (<5 seconds) |

### Rules of Thumb

```
Effective new frames per window = context_frames - context_overlap
Video playback duration ≈ num_frames ÷ playback_fps
Optimal overlap ratio: context_overlap ≈ 20% of context_frames
Generation duration = num_frames ÷ target_fps
```

---

## Parameter Details

### context_schedule

- **Effect:** Determines how the video is split into chunks for processing
- **`uniform_standard_fps`:** Maintains consistent time intervals between frames
- **`uniform_standard`:** Distributes frames evenly regardless of timing
- **When to adjust:** Change to `uniform_standard` if you notice temporal inconsistencies

### context_frames

- **Effect:** The number of frames processed together in each window
- **Default:** 81
- **Higher values:** Capture longer-term dependencies but use more VRAM
- **Lower values:** Use less memory but might have more abrupt transitions

### context_stride

- **Effect:** How far the window advances between steps
- **Default:** 4
- **Lower values:** More overlap, more computation
- **Example:** If context_frames=81 and context_stride=4, each step processes 77 new frames

### context_overlap

- **Effect:** Number of frames that overlap between consecutive windows
- **Default:** 16
- **Higher values:** Smoother transitions between windows
- **Lower values:** More visible seams between sections

### freenoise

- **Effect:** Shuffles noise to prevent repetitive patterns
- **Default:** true
- **With freenoise=true:** Longer videos have more variation
- **With freenoise=false:** Patterns might repeat

### target_fps

- **Effect:** The conceptual frames per second for temporal consistency
- **Default:** 2.0 (Apollo recommendation)
- **This is what Apollo found crucial for motion understanding**
- **1.0:** Slower perceived motion
- **4.0:** Faster perceived motion

### original_fps

- **Effect:** Reference value used in temporal calculations
- **Default:** 30
- **Rarely needs changing** — it's a baseline for calculations
- **Mainly affects how the model internally calculates time relations**

---

## Experimental Variations

### Motion Speed Variations

- **Slow motion:** target_fps=1.0, original_fps=30
- **Apollo recommended:** target_fps=2.0, original_fps=30
- **Faster motion:** target_fps=4.0, original_fps=30

### Window Size Variations

- **Low VRAM:** context_frames=41, context_overlap=8
- **Balanced:** context_frames=81, context_overlap=16
- **High quality:** context_frames=121, context_overlap=24

---

## Latent Interpolation

fredbliss experimented with combining FPS sampling with latent-space interpolation:

**Concept:**
1. Generate keyframes at low FPS (e.g., 2 fps)
2. Interpolate between keyframes in latent space
3. Decode the combined set of frames

**Potential benefits:**
- More interesting outputs
- Semantic consistency with prompt/image
- Theoretically more natural movement

**Implementation:**
```python
# After generating key frames at low fps
for i in range(len(latents)-1):
    # Insert interpolated frames between key frames
    alpha = torch.linspace(0, 1, steps=interpolation_factor)
    for j in range(1, interpolation_factor):
        interp_latent = (1-alpha[j])*latents[i] + alpha[j]*latents[i+1]
        interpolated_latents.append(interp_latent)
```

**Interpolation methods tested:**
- **Linear interpolation:** Straight averaging between latents
- **SLERP (Spherical Linear Interpolation):** "Walking a straight line, but on a sphere" — potentially more accurate but slower

**Status:** Experimental. fredbliss tested various interpolation factors (6, 12) with mixed results. Unclear if this provides benefits over standard frame interpolation in pixel space.

> "FPS Sampling + Latent Interpolation: Perfect Companions. FPS sampling ensures consistent time intervals between frames during generation, giving better temporal dynamics. Latent interpolation then fills in missing frames while maintaining those temporal dynamics." — fredbliss (via Claude), March 2, 2025

---

## Test Results

fredbliss conducted initial testing on March 2, 2025:

**Test setup:**
- Model: Wan 2.1 T2V 1.3B fp32
- Precision: fp16_fast
- Optimizations: SageAttention, torch.compile
- Resolution: 832x480
- Steps: 30
- Sampler: UniPC

**Test cases:**
1. **257 frames, target_fps=2.0:** ~5 minutes generation time, ~4.8 GB VRAM
2. **241 frames, target_fps=4.0:** ~5 minutes generation time
3. **Various prompts with emoji negatives** (🤡🚀🔥 prompt, 👎 negative)

**Observations:**
- "i cant tell a difference" between FPS sampling and uniform sampling (fredbliss)
- "you get more transitions with fps sampling i think" (fredbliss)
- Performance is "nuts" — 241 frames in ~5 minutes on 1.3B model
- Latent interpolation results were "weird" and required experimentation

**Community response:**
- Limited testing by others as of March 2, 2025
- TK_999 attempted context windowing with FPS sampling but got results that "looked like three different seeds of the same prompt"
- No clear consensus on whether FPS sampling provides benefits over standard context windowing

---

## Known Issues

- **Unclear benefits:** As of March 2, 2025, it's not clear whether FPS sampling provides noticeable improvements over standard context windowing
- **Limited testing:** Only tested by fredbliss and a few community members
- **Interpolation challenges:** Latent-space interpolation produced "weird" results that required extensive tuning
- **Frame rate mismatch:** Output needs to be interpolated to match target playback fps (e.g., 16 fps native → 24 fps playback)
- **Experimental status:** Not integrated into main wrapper; requires using fredbliss's fork

---

## Comparison to Standard Context Windows

| Aspect | Standard Context Windows | FPS Sampling |
|--------|-------------------------|-------------|
| **Frame distribution** | Uniform across video | Consistent time intervals |
| **Temporal consistency** | Can distort at long lengths | Maintains temporal relationships |
| **Complexity** | Simple | More complex |
| **Testing** | Widely tested | Experimental |
| **Benefits** | Proven to work | Unclear |
| **Speed** | Standard | Similar |

---

## When to Use

**Potential use cases (theoretical):**
- Very long videos where temporal consistency is critical
- Time-lapse style videos
- Videos requiring precise timing relationships

**When NOT to use:**
- Standard video generation (use regular context windows)
- When you need proven, stable results
- When you don't want to experiment with settings

---

## See Also

- [[context-windows]] — Standard approach to long video generation
- [[wan-2.1]] — Base model used for FPS sampling
- [[latent-guides]] — Related technique for latent-space control

## External Resources

- [fredbliss's FPS Sampling Fork](https://github.com/fblissjr/ComfyUI-WanVideoWrapper)
- [Apollo Paper Discussion](https://discord.com/channels/1076117621407223829/1345796910035898438) — fredbliss's overview in Discord
