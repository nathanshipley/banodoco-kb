---
title: Regional Conditioning for Wan
aliases: [regional-conditioning, regional-prompting, area-conditioning]
last_updated: 2025-03-25
---

# Regional Conditioning for Wan

Regional conditioning allows applying different prompts to different spatial regions of a video, enabling multi-subject scenes with independent control over each region.

---

## Overview

**Implemented by:** Clownshark Batwing (RES4LYF)

**Released:** March 24-25, 2025 (proof of concept)

**How it works:** Uses attention masks to split both cross-attention and self-attention, allowing different prompts to control different spatial regions of the video.

> "i've got attention masks that split up cross and self attention both" — Clownshark Batwing, March 25, 2025

**Key features:**
- Multiple regions per video
- Temporal dimension support (different prompts at different times)
- Works with native ComfyUI area conditioning
- Custom tricks requiring model tweaking

---

## Implementation

### RES4LYF Nodes

Clownshark Batwing's RES4LYF custom node pack includes regional conditioning:

- **Repository:** https://github.com/ClownsharkBatwing/RES4LYF
- **Status:** Proof of concept demonstrated, full Wan support coming soon
- **Current support:** Flux, SD3.5M/L, Auraflow, Wan (partial)
- **Planned:** Hunyuan, Stable Cascade

> "i don't have this up in the repo yet with wan but i think i can prolly get it cleaned up neough tomorrow sometime" — Clownshark Batwing, March 25, 2025

### Native ComfyUI Area Conditioning

Native ComfyUI's area conditioning also works with Wan:

> "well masked conditioning doesn't work with native, but area conditioning does" — spacepxl, March 25, 2025

**Difference:**
- **Masked conditioning:** Does not work with native Wan
- **Area conditioning:** Works with native Wan

---

## Examples

### Three-Region Example

Clownshark Batwing demonstrated 3-region conditioning:

> "3 regions with regional conditioning" — Clownshark Batwing, March 25, 2025

**Setup:**
- Three distinct spatial regions
- Different prompt for each region
- Unmasked area as third zone

### Temporal Dimension

> "crude POC but can do it along the temporal dim too" — Clownshark Batwing, March 25, 2025

Regional conditioning can vary across time, not just space.

---

## Comparison to Other Methods

### vs Native Area Conditioning

| Aspect | RES4LYF | Native Area Conditioning |
|--------|---------|-------------------------|
| **Attention masking** | Cross + Self | Area-based |
| **Temporal support** | Yes | Limited |
| **Custom tricks** | Yes | No |
| **Setup complexity** | Higher | Lower |
| **Model support** | Multiple models | ComfyUI native |

### vs Prompt Travel

| Aspect | Regional Conditioning | Prompt Travel |
|--------|---------------------|---------------|
| **Dimension** | Spatial regions | Temporal segments |
| **Use case** | Multi-subject scenes | Scene transitions |
| **Bleeding** | Controlled by masks | Significant |
| **Implementation** | Attention masks | Cross-attention segmentation |

---

## Technical Details

### Attention Masking

RES4LYF uses attention masks for both:
- **Cross-attention:** Text-to-image conditioning
- **Self-attention:** Spatial relationships within the video

This provides more control than cross-attention segmentation alone.

### Custom Model Tricks

> "got some custom tricks that require tweaking the model too" — Clownshark Batwing, March 25, 2025

Specific tricks not yet documented.

### Multi-Model Support

RES4LYF implements regional conditioning for multiple models:

> "got some nice attention masking stuff working with flux, sd35M/L, auraflow, wan, guess hunyuan, stable cascade are up next" — Clownshark Batwing, March 25, 2025

---

## Status and Availability

**Current status (March 25, 2025):**

- Proof of concept demonstrated for Wan
- Code exists but not yet cleaned up for release
- Expected release: "tomorrow sometime" (March 26, 2025)

**What's working:**
- Multiple spatial regions
- Temporal dimension support
- Attention masking (cross + self)

**What's coming:**
- Cleaned up Wan implementation
- Documentation
- Example workflows

---

## Use Cases

### Multi-Subject Scenes

Different prompts for different subjects in the same frame:
- Left side: "red panda"
- Right side: "cat"
- Background: "forest"

### Spatial Composition Control

Precise control over scene layout:
- Foreground: detailed subject
- Midground: secondary elements
- Background: environment

### Temporal Variations

Different prompts for the same region at different times:
- First half: "person standing"
- Second half: "person sitting"

---

## See Also

- [[prompt-travel]] — Temporal segmentation (different technique)
- [[latent-guides]] — Alternative control method
- [[vace]] — Unified control system
- [[comfyui]] — Platform for regional conditioning

## External Resources

- [RES4LYF GitHub Repository](https://github.com/ClownsharkBatwing/RES4LYF)
