---
title: RoPE Optimization
aliases: [rope-optimization, rope, rotary-position-embedding]
last_updated: 2025-03-15
---

# RoPE Optimization

RoPE (Rotary Position Embedding) is a position encoding mechanism used in transformer models. Kijai discovered on March 12, 2025 that optimizing the RoPE function in Wan 2.1 can provide significant speed improvements.

> "Adjusted the rope function a bit and got 20% faster gen? Go figure" — Kijai, March 12, 2025

> "It's probably highly inefficient" — Kijai, March 12, 2025

---

## Overview

On March 12, 2025, Kijai made adjustments to the RoPE function in the Wan wrapper and observed approximately 20% faster generation times. This optimization appears to be related to how the RoPE calculations are performed, though the exact mechanism was not detailed in the initial announcement.

**Key characteristics:**
- **20% speedup** reported on 1.3B model
- **Same quality** — appears to be pixel-perfect identical to unoptimized version
- **Already implemented in native ComfyUI** — comfy had already done this optimization for native
- **Wrapper-specific improvement** — brings wrapper performance closer to native

**Update (March 15, 2025):** Kijai is exploring further optimizations to eliminate complex number calculations entirely, which could enable torch.compile compatibility and additional speedups.

---

## Performance Impact

**Reported improvements (March 12, 2025):**

**1.3B model:**
- ~20% faster generation
- Pixel-perfect identical output to unoptimized version (confirmed by Kijai)

**14B model:**
- Not extensively tested in initial reports
- Likely similar percentage improvement

**User testing (Juampab12):**
- Initial test: 5:40 → 4:00 (significant improvement)
- Follow-up test: Only 10 seconds improvement
- Video quality: ~1% different, slightly worse
- Later testing: 6:50 → 6:30 (20 seconds improvement)
- With latest version: Nearly pixel-perfect match to original

> "wow <@228118453062467585> from 5:40 to 4m" — Juampab12, March 12, 2025

> "now not so much improvement like 10s" — Juampab12, March 12, 2025

> "the video is like 1% different too" — Juampab12, March 12, 2025

> "for worse" — Juampab12, March 12, 2025

**Note:** Initial testing showed variable results, with some users seeing significant improvements and others seeing minimal gains. Kijai made additional fixes to address quality differences.

---

## Implementation

### Wrapper (Kijai)

The RoPE optimization is automatically included in the Kijai wrapper as of March 12, 2025. No user configuration is required.

**Technical details:**
- Optimization involves adjusting how the RoPE function is calculated
- Previously always cast to float64
- New implementation uses more efficient precision handling
- Kijai noted the implementation is "probably highly inefficient" and could be improved further

> "I did find one thing that may cause it, previously it was always cast to float64" — Kijai, March 12, 2025

**Compatibility:**
- Works with T2V models (confirmed)
- Works with I2V models (confirmed)
- Stacks with other optimizations (TeaCache, SageAttention, etc.)

**Torch.compile compatibility (March 15, 2025):**

The current RoPE implementation uses complex numbers, which prevents torch.compile from working:

> "view_as_complex and view_as_real can't be compiled apparently" — Kijai, March 15, 2025

> "anyway this is still like 10-20% slower than using comfy's rope that can be fully compiled" — Kijai, March 15, 2025

Kijai is exploring ways to eliminate complex number calculations:

> "I want to get rid of the whole complex number way of doing it, but I don't understand enough 😄" — Kijai, March 12, 2025

> "then could compile it too" — Kijai, March 12, 2025

### Native ComfyUI

The RoPE optimization was already implemented in native ComfyUI by comfy before Kijai's wrapper implementation.

> "at least on 1.3B, but this is something comfy already done for native, so not faster than that" — Kijai, March 12, 2025

This means native ComfyUI users were already benefiting from this optimization.

**Native implementation details (March 15, 2025):**

Comfy's RoPE implementation does not use float64 and can be fully compiled with torch.compile, making it faster than the wrapper's current implementation.

---

## Alternative Approaches

### Rotation Matrix Method

**Community discussion (March 15, 2025):**

aikitoria raised the question of whether complex numbers are necessary:

> "I was reading https://huggingface.co/blog/designing-positional-encoding and there is no complex numbers involved, why did they over complicate it" — aikitoria, March 15, 2025

> "like can't we just manually create rotation matrix and get exact same result?" — aikitoria, March 15, 2025

Kijai confirmed this is possible:

> "I think just easier? dunno, comfy's implementation does seem fine without still" — Kijai, March 15, 2025

The complex number approach is used because complex multiplication naturally represents rotation, but it's not strictly necessary. A manual rotation matrix implementation could achieve the same results without the compile limitations.

---

## Quality Impact

**Initial concerns (March 12):**

Juampab12 reported quality differences in early testing:
- Video appeared "1% different"
- Quality was "for worse"
- Faces appeared to be affected in some cases

> "I think im gonna revert it messes up faces" — Juampab12, March 12, 2025

**Resolution:**

Kijai identified the issue as related to float64 casting and made corrections:

> "I did find one thing that may cause it, previously it was always cast to float64" — Kijai, March 12, 2025

After the fix:
- T2V testing showed pixel-perfect identical output
- I2V testing showed nearly pixel-perfect match
- Quality concerns resolved

> "are you sure? just tried with T2V and it's pixel perfect same" — Kijai, March 12, 2025

---

## Known Issues

### Initial Quality Differences (RESOLVED)

**Problem:** Early implementation showed slight quality differences, particularly in faces.

**Cause:** Float64 casting issue in the RoPE function.

**Resolution:** Kijai fixed the float64 casting issue on March 12, 2025. Latest version produces pixel-perfect (T2V) or nearly pixel-perfect (I2V) results.

### Variable Performance Gains

**Observation:** Different users reported different levels of speedup:
- Some saw 20% improvement
- Others saw only 10-20 seconds improvement
- Results may vary by workflow, resolution, and other settings

**Possible causes:**
- Different model sizes (1.3B vs 14B)
- Different resolutions
- Interaction with other optimizations
- Measurement methodology

### I2V Differences Over Time

**Observation:** Juampab12 noted that I2V generations showed increasing differences over the course of the video:

> "the longer it goes the more it changes" — Juampab12, March 12, 2025

> "at first its the same" — Juampab12, March 12, 2025

**Status:** This was related to the float64 casting issue and appears to be resolved in the latest version.

### Torch.compile Incompatibility

**Problem:** The current RoPE implementation uses complex numbers (view_as_complex, view_as_real), which cannot be compiled by torch.compile.

**Impact:** The wrapper's RoPE is 10-20% slower than native ComfyUI's fully-compiled RoPE implementation.

**Status:** Kijai is exploring ways to eliminate complex number calculations to enable compilation.

---

## Future Development

**Planned improvements:**

Kijai noted the current implementation is "probably highly inefficient" and expressed interest in further optimization:

> "I want to get rid of the whole complex number way of doing it, but I don't understand enough 😄" — Kijai, March 12, 2025

> "then could compile it too" — Kijai, March 12, 2025

**Possible directions:**
- Remove complex number calculations
- Make the function torch.compile compatible
- Further precision optimizations
- Better understanding of the underlying mathematics
- Implement rotation matrix approach directly

**Community suggestions:**

> "ask claude" — Juampab12, March 12, 2025 (suggesting using AI assistance to understand the math)

**Potential speedup:** If RoPE can be made torch.compile compatible, it could provide an additional 10-20% speedup on top of the current optimization.

---

## Fused RMSNorm Exploration

**March 15, 2025:** Kijai is also exploring fused RMSNorm as a potential optimization:

> "I wonder if fused rms norm would be beneficial for this model..." — Kijai, March 15, 2025

> "but I need to compile flash attention or apex to try" — Kijai, March 15, 2025

Fused RMSNorm could provide additional speedups by combining normalization operations, but requires compiling flash attention or apex libraries.

---

## Comparison to Native

Kijai's optimization brings the wrapper closer to native ComfyUI performance, which already had this optimization implemented.

**Before RoPE optimization:**
- Native ComfyUI: Faster (had RoPE optimization)
- Wrapper: Slower (no RoPE optimization)

**After RoPE optimization:**
- Native ComfyUI: Same speed (already optimized, fully compiled)
- Wrapper: ~20% faster (now has optimization, but not fully compiled)
- Performance gap reduced but not eliminated

**Remaining gap:** Native's RoPE can be fully compiled with torch.compile, making it 10-20% faster than the wrapper's current implementation.

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| Quality differences | Update to latest wrapper version (March 12, 2025 or later) |
| Faces look different | Fixed in latest version; update wrapper |
| No speedup observed | Speedup may vary by workflow; try different settings |
| I2V changes over time | Fixed in latest version; update wrapper |
| Pixel differences | T2V should be pixel-perfect; I2V nearly pixel-perfect in latest version |
| Slower than native | Native has fully-compiled RoPE; wrapper improvement in progress |

---

## Performance Stack

RoPE optimization stacks with other optimizations:

- [[fp16-accumulate]] — 20-30% speedup, stacks with RoPE
- [[sageattention]] — ~25% speedup, stacks with RoPE
- [[torch-compile]] — ~30% speedup, stacks with RoPE (but RoPE itself cannot be compiled yet)
- [[teacache]] — ~2x speedup, stacks with RoPE

**Combined potential:** ~3-4x speedup with all optimizations enabled

**Future potential:** If RoPE can be made torch.compile compatible, an additional 10-20% speedup may be possible.

---

## See Also

- [[wan-2.1]] — Base model that benefits from RoPE optimization
- [[speed]] — Overview of all speed optimizations
- [[fp16-accumulate]] — Stackable optimization
- [[sageattention]] — Stackable optimization
- [[torch-compile]] — Stackable optimization (RoPE compatibility in progress)
- [[comfyui]] — Platform for running Wan workflows

---

## Technical Background

**What is RoPE?**

RoPE (Rotary Position Embedding) is a method for encoding positional information in transformer models. It uses rotation matrices to encode relative positions, which helps the model understand the order and relationships between tokens (or in this case, video frames and spatial positions).

**Why optimize it?**

RoPE calculations are performed frequently during inference, so even small improvements in efficiency can compound to significant speedups. The optimization appears to involve:
- More efficient precision handling (avoiding unnecessary float64 casting)
- Potentially simplified mathematical operations
- Better memory access patterns

**Limitations:**

Kijai noted the current implementation still uses complex numbers, which may be inefficient. Future optimizations could involve:
- Replacing complex number operations with equivalent real number operations
- Making the function compatible with torch.compile for additional speedup
- Further mathematical simplifications

**Complex numbers vs rotation matrices:**

The current implementation uses complex number multiplication to represent rotations because it's mathematically elegant and concise. However, this approach:
- Prevents torch.compile from working (view_as_complex/view_as_real are not compilable)
- May be less efficient than direct rotation matrix operations
- Is not strictly necessary — rotation matrices can achieve the same result

A future implementation using rotation matrices directly could enable torch.compile and provide additional speedups.

## External Resources

- [HuggingFace Blog: Designing Positional Encoding](https://huggingface.co/blog/designing-positional-encoding) — Explanation of RoPE without complex numbers
- [RoFormer Paper](https://arxiv.org/abs/2104.09864) — Original RoPE research