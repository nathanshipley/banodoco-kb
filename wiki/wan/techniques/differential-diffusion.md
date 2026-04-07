---
title: Differential Diffusion and Video Masking
aliases: [differential-diffusion, diff-diff, video-masking, latent-masking]
last_updated: 2025-03-25
---

# Differential Diffusion and Video Masking

Differential diffusion (often called "diff diff") is a technique for selectively applying different diffusion strengths to different parts of a video using masks. This enables precise control over which regions change during generation.

---

## Overview

Differential diffusion allows masking specific regions of a video to control how much they change during generation. This is essential for:

- Video inpainting (replacing specific objects/regions)
- Background replacement
- Subject isolation
- Selective style transfer

**Key principle:** The entire video goes through the VAE and model, but masked regions receive different diffusion strengths, allowing selective modification.

---

## Implementation Methods

### Wrapper Method (Kijai)

**Recommended approach** for most use cases.

**How it works:**
1. Encode video with mask in WanVideoEncode node
2. Use differential diffusion during sampling
3. Composite result back onto original video

**Advantages:**
- More stable output
- Better quality preservation
- Fewer artifacts

**Disadvantages:**
- Slower (more steps required)
- Wrapper-specific

### Native Method

**Faster but less stable.**

**How it works:**
1. Use latent masking in native ComfyUI
2. Apply mask during sampling
3. Composite result back onto original

**Advantages:**
- Faster generation
- Native ComfyUI support

**Disadvantages:**
- Less stable
- More artifacts (flashing, color shifts)
- Background degradation

---

## Critical: Always Composite

**The most important rule of differential diffusion:**

> "it's using differential diffusion, so everything does go through the model, but it tries to balance so only the masked part changes... it's not perfect and it reduces the quality of the unmasked bits, so afterwards it's best to composite your result on top of the original video, so you get the 100% original background/unmasked bits" — Kijai, March 25, 2025

> "it should pretty much always be done with any kind of inpainting" — Kijai, March 25, 2025

**Why compositing is essential:**
- VAE encoding/decoding degrades unmasked regions
- Differential diffusion is not perfect
- Compositing restores 100% original quality to unmasked areas

**How to composite:**
1. Generate video with differential diffusion
2. Use ImageComposite node (or similar)
3. Composite generated video onto original using the same mask
4. Adjust mask (grow, blur edges) as needed

---

## Mask Preparation

### Mask Format

- **White (255):** Areas to modify
- **Black (0):** Areas to preserve
- **Gray (127):** Partial modification (for VACE-style workflows)

### Mask Quality

For differential diffusion:
- Clean edges work best
- Slight blur on edges helps blending
- Grow mask slightly beyond subject to prevent leaking

### Mask Tools

**SAM2 (Segment Anything 2):**

Kijai's SAM2 implementation includes a points editor:

> "I've been using Kijai's fantastic Sam2 points editor to mask specific subjects or parts of the video" — David Snow, March 24, 2025

**Repository:** https://github.com/kijai/ComfyUI-segment-anything-2

**Features:**
- Point-based segmentation
- Video tracking
- Automatic mask generation

**Box drawing:**

> "you can also draw box on it btw" — Kijai, March 25, 2025

> "sometimes better" — Kijai, March 25, 2025

SAM2 supports both point and box selection for mask creation.

---

## Common Issues

### Background Changes Despite Masking

**Problem:** Background changes even when masked as "preserve."

**Cause:** VAE encoding/decoding affects the entire video.

**Solution:** Always composite the result back onto the original video.

### Flashing and Color Shifts

**Problem:** Flashing or color shifts in output, especially with native method.

**Example issues:**
- First frame flash
- Color shifts between frames
- Brightness changes

**Solutions:**
1. Use wrapper method instead of native
2. Increase steps (30-50 instead of 20)
3. Adjust denoise strength
4. Composite result onto original
5. Check depth map quality (if using depth control)

### Mask Leaking

**Problem:** Effects leak outside the masked region.

**Solutions:**
- Grow mask slightly beyond subject
- Blur mask edges
- Adjust composite mask separately from generation mask

---

## Combining with Control LoRAs

### Depth + Masking

A powerful combination for precise control:

**Workflow:**
1. Generate depth map of original video
2. Create mask for region to modify
3. Use depth control LoRA for structure
4. Apply differential diffusion with mask
5. Composite result

**Example use case:** Replace background while preserving subject position and depth.

### Flat Color + Masking

For background replacement:

**Workflow:**
1. Mask subject
2. Use flat color LoRA for background
3. Composite result

---

## Settings

### Wrapper Settings

| Parameter | Recommended Value | Notes |
|-----------|------------------|-------|
| **Denoise** | 0.5-0.9 | Lower = more faithful to input |
| **Steps** | 30-50 | More steps = more stable |
| **CFG** | 3.0-6.0 | Standard range |
| **Mask in encode** | Yes | Pass mask to WanVideoEncode |
| **Composite** | Always | Use ImageComposite after generation |

### Native Settings

| Parameter | Recommended Value | Notes |
|-----------|------------------|-------|
| **Denoise** | 0.5-0.9 | Lower = more faithful to input |
| **Steps** | 20-30 | Faster than wrapper |
| **CFG** | 3.0-6.0 | Standard range |
| **Latent mask** | Yes | Use SetLatentNoiseMask or similar |
| **Composite** | Always | Essential for quality |

---

## Example Workflows

### Basic Wrapper Workflow

1. Load original video
2. Create mask (SAM2 or manual)
3. Load depth control LoRA (optional)
4. WanVideoEncode with mask
5. Sample with differential diffusion
6. Decode
7. ImageComposite onto original video
8. Save

### Basic Native Workflow

1. Load original video
2. Create mask
3. Encode to latents
4. SetLatentNoiseMask
5. Sample
6. Decode
7. ImageComposite onto original video
8. Save

---

## Comparison to Other Techniques

| Method | Speed | Stability | Quality | Use Case |
|--------|-------|-----------|---------|----------|
| **Wrapper diff diff** | Slower | High | High | Final quality work |
| **Native diff diff** | Faster | Medium | Medium | Quick iterations |
| **VACE inpainting** | Medium | High | High | Complex inpainting |
| **Latent guides** | Fast | Medium | Medium | V2V style work |

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| Background changes | Always composite result onto original |
| Flashing artifacts | Use wrapper method; increase steps; composite |
| Color shifts | Check depth map normalization; composite |
| Mask leaking | Grow mask; blur edges; adjust composite mask |
| Poor quality unmasked areas | Composite result onto original (essential) |
| Artifacts at mask edges | Blur mask edges; grow mask slightly |

---

## See Also

- [[vace]] — Alternative inpainting method
- [[control-lora]] — Depth and other control signals
- [[latent-guides]] — Alternative V2V technique
- [[comfyui]] — Platform for differential diffusion workflows

## External Resources

- [ComfyUI-segment-anything-2](https://github.com/kijai/ComfyUI-segment-anything-2) — SAM2 masking tools
- [ComfyUI-WanVideoWrapper](https://github.com/kijai/ComfyUI-WanVideoWrapper) — Wrapper with diff diff support
