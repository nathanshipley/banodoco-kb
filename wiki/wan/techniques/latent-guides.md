---
title: Latent Guides
aliases: [latent-guides, latent-guide, v2v, video-to-video]
last_updated: 2025-03-03
---

# Latent Guides

Latent guides (also called "latent guidance" or "semi-I2V") is a technique for controlling video generation by feeding pre-processed latent information into the diffusion process. This allows for video-to-video style workflows without using a traditional video input, enabling control through shapes, colors, movements, and image transformations.

## Overview

Latent guides work by encoding control information directly into the latent space that the model operates in. Unlike traditional V2V which uses a video as input, latent guides can use:

- Solid colors
- Shapes and patterns
- Image sequences (zooming, panning, color shifts)
- Hand-drawn sketches
- Any visual information that can be encoded as latents

> "in essence its v2v, but you not using a video" — Draken, March 3, 2025

> "use an image and like zoom it, zoom out, shift it, change colors etc" — Draken, March 3, 2025

## How It Works

The fundamental principle:

1. Create a sequence of images/frames with the desired control information
2. Encode these frames into latent space
3. Feed the latents into the diffusion model
4. The model uses these latents as guidance for generation

**Basic example:**
> "Feed all blue latents into HY or WAN, with 1.0 denoise, you get a 100 blue output" — Draken, March 3, 2025

This demonstrates that the latent information directly influences the output. By varying the latent input (colors, shapes, positions), you can control the generation.

## Implementation

### RES4LYF Nodes

The primary implementation for latent guides is through the RES4LYF custom node pack:

- **Repository:** https://github.com/ClownsharkBatwing/RES4LYF
- **Maintained by:** ClownsharkBatwing
- **Contributors:** Ablejones and others
- **Compatibility:** Works with most image models (SD, SDXL) and video models (Wan, Hunyuan, etc.)
- **Note:** Does not work with Mochi or CogVideo

> "No, I contribute to them but they are <@1208924372299939890> nodes." — Ablejones, March 3, 2025

### Basic Workflow

Ablejones shared a simple latent guide workflow on March 3, 2025:

**Key components:**
1. Image sequence generation (zoom, pan, color shifts, etc.)
2. Latent encoding of the sequence
3. Connection to the diffusion model
4. Standard sampling process

**Note:** The workflow may contain "group node essence" that causes red outlines when loaded. This is harmless - drop the workflow over ComfyUI to fix it, or ignore the visual artifacts.

## Use Cases

### Camera Movement Control

- Zoom in/out by scaling images in sequence
- Pan by shifting images horizontally/vertically
- Rotation by rotating the source image
- Complex camera paths by combining transformations

### Color and Lighting Control

- Gradual color shifts (day to night, seasonal changes)
- Lighting changes (brightness, contrast adjustments)
- Color grading effects

### Shape and Pattern Control

- Geometric shapes to guide composition
- Patterns to influence texture
- Abstract forms for artistic effects

### Motion Control

- Moving shapes to guide object motion
- Position changes to control subject movement
- Transformation sequences for complex animations

## Advantages

1. **No video input required** — Generate control sequences programmatically
2. **Precise control** — Direct manipulation of latent space
3. **Flexible** — Can combine multiple control types
4. **Compatible** — Works with T2V models without special training
5. **Efficient** — No need to process full video inputs

## Limitations

- Requires understanding of latent space behavior
- May need experimentation to achieve desired effects
- Results can be unpredictable with complex control sequences
- Not as intuitive as direct video input for some use cases

## Comparison to Other Techniques

| Method | Control Type | Complexity | Flexibility |
|--------|-------------|------------|-------------|
| **Latent Guides** | Latent space | Medium | High |
| **V2V** | Video input | Low | Medium |
| **VACE** | Preprocessors | Medium | High |
| **ControlNet** | Preprocessors | Low | Medium |
| **I2V** | Single image | Low | Low |

## Tips and Best Practices

1. **Start simple** — Test with basic color or shape sequences before complex animations
2. **Use high denoise** — 1.0 denoise gives the model maximum freedom to interpret the latent guides
3. **Experiment with strength** — The influence of latent guides can be adjusted
4. **Combine with prompts** — Latent guides work alongside text prompts for additional control
5. **Preview latents** — Use latent preview nodes to understand what you're feeding the model

## Related Techniques

### RoPE Frequency Adjustment

Some developers are experimenting with modifying RoPE (Rotary Position Embedding) frequencies to adjust temporal vs. spatial emphasis in latent-guided generation. This is an advanced technique still under development.

### Perceiver Resampling

Another experimental approach involves using perceiver integration to process latent guides, allowing for more sophisticated control over how the guidance information is interpreted.

## See Also

- [[wan-2.1]] — Base model that works with latent guides
- [[vace]] — Alternative control method using preprocessors
- [[i2v]] — Single-image conditioning approach
- [[comfyui]] — Platform for building latent guide workflows

## External Resources

- [RES4LYF GitHub Repository](https://github.com/ClownsharkBatwing/RES4LYF)
- [Ablejones' Simple Latent Guide Workflow](https://discord.com/channels/1076117621407223829/1342763350815277067/1346236034513371166) (Discord link)