---
title: Enhance-a-Video
aliases: [enhance-a-video, enhance, wan-enhance]
last_updated: 2025-03-09
---

# Enhance-a-Video

Enhance-a-Video is an optimization technique for Wan video generation that provides speed improvements with minimal quality impact. It was implemented by Kijai for native ComfyUI on March 9, 2025.

> "made a proper WanVideo Enhance-a-video node for native" — Kijai, March 9, 2025

---

## Overview

Enhance-a-Video is based on research from NUS-HPC-AI-Lab that optimizes video generation by applying enhancements at specific points in the diffusion process. Kijai's implementation provides a proper patch that integrates cleanly with other optimizations.

**Key features:**
- Speed improvement of ~15-20% in tested workflows
- Compatible with TeaCache and torch.compile
- Minimal quality impact
- Works with both T2V and I2V models

---

## Performance Impact

**Reported benchmarks (March 9, 2025):**

JmySff tested with I2V 480p, 960x544, 25 steps, native ComfyUI:
- **Without Enhance-a-Video:** 6 minutes 35 seconds
- **With Enhance-a-Video:** 5 minutes 36 seconds
- **Speedup:** ~15% faster (59 seconds saved)

> "I don't really understand why i just gain 1 minute with Enhance a video but... i'm just happy" — JmySff, March 9, 2025

**Settings used:**
- Enhance-a-Video strength: 0.32
- Combined with TeaCache
- Native ComfyUI implementation

**Combined with TeaCache (March 9, 2025):**

JmySff reported combining TeaCache with the new Enhance-a-Video node:
- **324 frames, 960x544, I2V 480p, 25 steps:** 24 minutes 12 seconds
- Additional 1 minute speedup from Enhance-a-Video on top of TeaCache benefits

---

## Implementation

### Native ComfyUI

Kijai released the Enhance-a-Video node for native ComfyUI on March 9, 2025. It is included in the KJNodes custom node pack.

**Key implementation details:**
- Proper patch instead of replacing whole model code
- Applied AFTER rope, not before (critical for correct behavior)
- Compatible with TeaCache and torch.compile patches

> "my first implementation for native is completely wrong" — Kijai, March 9, 2025

> "it needs to be applied AFTER rope not before, it messed it up" — Kijai, March 9, 2025

> "and this node is a proper patch instead of replacing the whole model code like it does in the Loom -nodes" — Kijai, March 9, 2025

### Patch Order

When using multiple patches, order matters:

**Recommended order:**
1. Enhance-a-Video patch
2. TeaCache patch
3. Torch.compile patch (last)

> "seemed to work with TeaCache and torch.comiple patches too, to be safe I'd put the compile patch last" — Kijai, March 9, 2025

---

## Settings

| Parameter | Recommended Value | Notes |
|-----------|------------------|-------|
| **Strength** | 0.32 | JmySff's tested value; adjust based on workflow |
| **Placement** | After rope, before output layer | Handled automatically by node |

---

## Compatibility

**Works with:**
- Wan 2.1 T2V (all sizes)
- Wan 2.1 I2V (confirmed working)
- Native ComfyUI
- TeaCache (confirmed compatible)
- Torch.compile (confirmed compatible)

**May not work with:**
- I2V models (Kijai noted uncertainty about usefulness for I2V)
- Wrapper implementation (native only as of March 9, 2025)

> "I don't know if it's useful for I2V" — Kijai, March 9, 2025

**Testing results:**

N0NSens tested with I2V 480p and reported mixed results:
- Prompt: "woman smiles, steady camera"
- **Without Enhance-a-Video:** 1 minute 49 seconds
- **With Enhance-a-Video:** 2 minutes 38 seconds
- Result: Slower with Enhance-a-Video in this test

This suggests Enhance-a-Video may be more beneficial for T2V workflows than I2V, or that settings need adjustment for I2V use cases.

---

## Known Issues

### Initial Implementation Bug (RESOLVED)

Kijai's first implementation had a critical bug where the enhancement was applied before rope instead of after. This was fixed on March 9, 2025.

> "my first implementation for native is completely wrong" — Kijai, March 9, 2025

> "it needs to be applied AFTER rope not before, it messed it up" — Kijai, March 9, 2025

**Solution:** Update to latest version of KJNodes.

### Variable Performance

Performance impact varies by workflow:
- Some users report 15-20% speedup
- Others report no speedup or even slowdown
- May depend on model type (T2V vs I2V), resolution, and other settings

### I2V Uncertainty

Kijai expressed uncertainty about whether Enhance-a-Video is useful for I2V models. Community testing shows mixed results.

---

## Comparison to Other Optimizations

| Optimization | Speedup | Quality Impact | Compatibility |
|--------------|---------|----------------|---------------|
| **Enhance-a-Video** | ~15-20% | Minimal | Good |
| **TeaCache** | ~2x | Slight | Excellent |
| **SageAttention** | ~25% | Minimal | Excellent |
| **Torch.compile** | ~30% | None | Good |
| **fp16 accumulate** | ~20-30% | None | Excellent |

Enhance-a-Video provides modest speedup compared to other optimizations, but stacks well with them for cumulative benefits.

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| No speedup or slower | May not be beneficial for your specific workflow; try disabling |
| Errors with other patches | Check patch order; put torch.compile last |
| Quality degradation | Adjust strength parameter; try lower values |
| Not working with I2V | May not be useful for I2V; consider disabling for I2V workflows |

---

## Performance Stack

For maximum performance, combine Enhance-a-Video with:

- [[teacache]] — ~2x speedup, confirmed compatible
- [[sageattention]] — ~25% speedup, stacks well
- [[torch-compile]] — ~30% speedup, place last in patch order
- [[fp16-accumulate]] — ~20-30% speedup, stacks well

**Example combined performance (JmySff, March 9, 2025):**
- I2V 480p, 960x544, 324 frames, 25 steps
- TeaCache + Enhance-a-Video + other optimizations
- **Total time:** 24 minutes 12 seconds
- **Estimated baseline:** ~45-60 minutes without optimizations
- **Speedup:** ~2-2.5x faster

---

## See Also

- [[wan-2.1]] — Base model that benefits from Enhance-a-Video
- [[teacache]] — Compatible optimization
- [[torch-compile]] — Compatible optimization
- [[sageattention]] — Compatible optimization
- [[speed]] — Overview of all speed optimizations

## External Resources

- [Enhance-A-Video GitHub](https://github.com/NUS-HPC-AI-Lab/Enhance-A-Video) — Original research implementation
- [KJNodes Repository](https://github.com/kijai/ComfyUI-KJNodes) — Kijai's implementation
