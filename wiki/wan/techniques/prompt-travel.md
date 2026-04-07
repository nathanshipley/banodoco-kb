---
title: Prompt Travel and Multi-Prompt Generation
aliases: [prompt-travel, multi-prompt, prompt-segmentation]
last_updated: 2025-03-25
---

# Prompt Travel and Multi-Prompt Generation

Prompt travel is a technique for changing prompts during video generation, allowing smooth transitions between different concepts or scenes within a single generation. Kijai implemented this for Wan 2.1 in late March 2025 by segmenting the cross-attention layers.

---

## Overview

**Released:** March 24, 2025 by Kijai (experimental)

**How it works:** The technique segments the cross-attention layers and applies different prompts to different parts of the temporal sequence. This allows the model to transition between concepts without requiring multiple separate generations.

> "I segmented the cross attn and applying different prompts to different parts of the sequence" — Kijai, March 24, 2025

> "I think a lot more can be done with that, only now learning how it all works" — Kijai, March 24, 2025

**Key advantages:**
- No speed loss
- Works with all existing optimizations (TeaCache, torch.compile, etc.)
- Simple syntax using `|` separator
- Can be combined with RifleX for longer videos

**Current limitations:**
- Bleeding between prompts due to unsegmented video attention
- Weak effect for full subject changes
- Still experimental (broke other functions during initial implementation)

---

## Syntax

### Basic Multi-Prompt

Separate prompts with the `|` pipe character:

```
video of a man laughing|video of a man crying
```

The first prompt applies to the first half of the video, the second to the second half.

### Motion Prompts

Motion-based prompts work particularly well:

```
video of a red panda walking to the right|video of a red panda walking to the left
```

```
video of a person running|video of a person jumping
```

### Subject Changes

Subject changes are possible but show significant bleeding:

```
video of a red panda eating bamboo|video of a cat
```

```
red panda|dog
```

> "it bleeds too much for full subject change" — Kijai, March 24, 2025

### Prompt Strength Adjustment

Kijai added syntax to adjust prompt strength (only for full prompts):

```
(prompt1:strength)|(prompt2:strength)
```

Specific syntax details not yet documented.

---

## Settings

### Frame Count

Works with standard frame counts (81) and extended counts with RifleX:

- **81 frames:** Standard, first 40 frames use first prompt, last 41 frames use second prompt
- **129 frames with RifleX:** Demonstrated working (riflex_freq_index=6)

### Sampler Settings

No special sampler settings required. Use standard Wan settings:

- **Steps:** 20-30 (standard)
- **CFG:** 5-7 (standard)
- **Sampler:** uni_pc, dpmpp_2m (standard)
- **Scheduler:** simple, beta (standard)

### RifleX Integration

Combining with RifleX allows longer multi-prompt videos:

```
Prompt: laughing|crying
Frames: 129
riflex_freq_index: 6
```

---

## Implementation Status

**Current status (March 24-25, 2025):**

- Code exists but not yet pushed to repository
- Broke multiple other functions during refactoring
- Kijai testing and fixing before release

> "didn't push the code yet, broke too many things" — Kijai, March 24, 2025

> "just broke a lot of other functions with my refactoring" — Kijai, March 24, 2025

**What's implemented:**
- Cross-attention segmentation for T2V prompts
- CLIP embed segmentation for I2V (batch mode)
- Prompt strength adjustment syntax

**What's not implemented:**
- Video attention masking (causes bleeding)
- Native ComfyUI support (wrapper only)
- Three or more prompts (currently limited to two)

---

## I2V Batch Mode

For I2V, Kijai implemented CLIP embed segmentation:

> "I did do same for the clip embeds for the I2V, which was the initial idea" — Kijai, March 24, 2025

> "so now if you choose 'batch' as the join method, it should split the images to different halves of the video" — Kijai, March 24, 2025

**How it works:**
- Load multiple images
- Set join method to "batch"
- First image conditions first half of video
- Second image conditions second half

**Limitations:**
- Only works for CLIP embeds and prompts
- Does not work for conditioning images (too strong to override)
- Mostly useful for motion prompts

---

## Examples

### Successful Examples

**Emotion transitions:**
```
video of a man laughing|video of a man crying
```
Result: Clean transition between emotions

**Direction changes:**
```
video of a red panda walking to the right|video of a red panda walking to the left
```
Result: Smooth direction reversal

**Simple prompts:**
```
laughing|crying
```
Result: Works well with minimal prompting

### Problematic Examples

**Subject changes:**
```
red panda|dog
```
Result: Significant bleeding, confused model

**Action changes:**
```
video of a person running|video of a person jumping
```
Result: Model confused, mixed actions

---

## Technical Details

### Cross-Attention Segmentation

The technique works by segmenting the cross-attention layers:

1. Divide the temporal sequence into segments (currently 2)
2. Apply different text conditioning to each segment
3. Cross-attention uses the appropriate prompt for each frame

**Why it works:**
> "most interesting take away is that just segmenting the crossattn works that well" — Kijai, March 24, 2025

### Video Attention Bleeding

The video attention (self-attention across frames) is not segmented, causing bleeding:

> "it's pretty weak effect in general, there's still the video attention that is not segmented so it blends it overall" — Kijai, March 24, 2025

> "next step would be to learn how to mask that" — Kijai, March 24, 2025

### Future Improvements

Kijai identified video attention masking as the next step:

- Mask video attention to prevent bleeding
- Allow cleaner subject transitions
- Enable more dramatic prompt changes

---

## Comparison to Context Windows

Prompt travel is different from context window multi-prompting:

| Aspect | Prompt Travel | Context Windows |
|--------|--------------|----------------|
| **Implementation** | Cross-attention segmentation | Separate sampling windows |
| **Speed** | No speed loss | Slower (overlapping windows) |
| **Bleeding** | Significant | Minimal (separate windows) |
| **Max prompts** | 2 (currently) | Unlimited (one per window) |
| **Frame limit** | 81-129 with RifleX | 1000+ frames |
| **Transitions** | Smooth blend | Hard cuts at boundaries |
| **Use case** | Smooth transitions | Scene changes, long video |

---

## Use Cases

### Emotion Transitions

Smooth transitions between emotional states:
- Laughing to crying
- Happy to sad
- Calm to excited

### Direction Changes

Reversing or changing movement direction:
- Walking left to walking right
- Moving forward to moving backward
- Rotating clockwise to counterclockwise

### Motion Variations

Changing the type of motion:
- Walking to running (with bleeding)
- Standing to sitting
- Slow to fast movement

### NOT Recommended For

- Full subject changes (use context windows instead)
- Complex scene transitions (too much bleeding)
- More than 2 distinct concepts

---

## Known Issues

### Bleeding Between Prompts

**Problem:** Video attention is not segmented, causing prompts to blend.

**Impact:** Subject changes show mixed features from both prompts.

**Workaround:** Use motion-based prompts rather than subject changes.

### Limited to Two Prompts

**Current limitation:** Only two prompts supported (first half / second half).

**Future:** May be expanded to 3+ prompts with additional segmentation.

### Experimental Status

**Problem:** Code broke other functions during refactoring.

**Status:** Not yet released to repository (as of March 25, 2025).

**Workaround:** Wait for official release.

---

## Compatibility

**Works with:**
- TeaCache (confirmed)
- Torch.compile (confirmed)
- SageAttention (confirmed)
- RifleX (confirmed, demonstrated at 129 frames)
- All standard optimizations

**Does NOT work with:**
- Native ComfyUI (wrapper only)
- Context windows (different technique)

---

## Community Reception

**Highly anticipated:**

> "prompt travel would be amazing" — fearnworks, March 24, 2025

**Positive reactions to examples:**
- 🔥 reactions to emotion transition examples
- Interest in using for storytelling
- Excitement about smooth transitions

**Concerns:**
- Bleeding between prompts
- Limited to two prompts
- Subject changes not clean enough

---

## See Also

- [[context-windows]] — Alternative for multi-prompt long video
- [[wan-2.1]] — Base model for prompt travel
- [[riflex]] — Can be combined for longer multi-prompt videos
- [[comfyui]] — Platform for running prompt travel workflows

## External Resources

- [ComfyUI-WanVideoWrapper](https://github.com/kijai/ComfyUI-WanVideoWrapper) — Will include prompt travel when released
