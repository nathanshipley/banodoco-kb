---
title: SVDQuant / Nunchaku
aliases: [svdquant, nunchaku, nvfp4]
last_updated: 2025-03-08
---

# SVDQuant / Nunchaku

SVDQuant is a 4-bit quantization method with an accompanying inference engine called Nunchaku, developed by MIT Han Lab. It claims 3× speedups over BF16 models while retaining 16-bit attention, with support for NVIDIA RTX 3090, 4090, 5090, and Ada 6000 GPUs.

> "On both RTX 4090 and 5090, SVDQuant achieves 3× speedups over the original BF16 model, even while retaining 16-bit attention." — MIT Han Lab

---

## Overview

SVDQuant uses a low-rank branch approach combined with 4-bit quantization. The key innovation is the Nunchaku inference engine, which fuses kernels to eliminate redundant memory access:

> "However, naively running the low-rank branch independently incurs significant overhead due to extra data movement of activations, negating the quantization speedup. To address this, we co-design an inference engine Nunchaku that fuses the kernels in the low-rank branch into those in the low-bit branch to cut off redundant memory access."

**Key features:**
- 3× speedup over BF16 baseline (on 4090/5090)
- 3.5× memory reduction
- Retains 16-bit attention for quality
- NVFP4 format support on 5090 (1.3× faster than INT4 on 4090)
- Supports 3090, 4090, 5090, Ada 6000

---

## Performance Claims

### Official Benchmarks

**Desktop RTX 4090:**
- 3.0× speedup over BF16
- 3.5× memory reduction

**Laptop RTX 4090:**
- 10.1× speedup total (includes eliminating CPU offloading)
- 3.0× speedup over NF4 W4A16 baseline

**RTX 5090:**
- NVFP4 model runs 1.3× faster than INT4 on 4090
- Aligns with theoretical 1.3× performance boost from 4090 to 5090

### Community Testing

**Ada (March 7, 2025):**
- Tested on RTX 3060
- "about 3x speedup on rtx 3060 compared to fp16 or q4 (no offloading)"
- "quality also in q4+ area with similar vram requirements"
- "I find it very fair but could not install into comfy"

**deleted_user_2ca1923442ba (March 7, 2025):**
- "its more like 30% boost rather than 3x boost"
- "compared to FP8 torch.compile sage attention"
- "but 30% boost is still decent"

**Clarification on 3× claim:**
> "to get the 3x speed up in their paper they compared to CPU offloading, without compilation, FP8 matmul or sage attention" — deleted_user_2ca1923442ba

> "the thing is they are comparing to uncompiled NF4 which cannot use accelerated Int4/FP4 matmul to their method which is using accelerated Int4/FP4 matmul along with compilation" — deleted_user_2ca1923442ba

**Realistic comparison:**
> "if you compare to a reasonable 4090 baseline like torch.compile, FP8 and sage attention then SVDquant is only about 30% faster" — deleted_user_2ca1923442ba

---

## Quality

### Official Claims

- Retains 16-bit attention
- Minimal quality loss compared to BF16
- INT4 examples look good in official demos

### Community Testing

**comfy (March 7, 2025):**
> "quantizing these models gives worse results than flux"

This suggests Wan may be more sensitive to quantization than image models like Flux.

**deleted_user_2ca1923442ba (March 7, 2025):**
> "it takes a hit in weird edge cases like Sana with high PAG levels"

Suggests quality degradation in specific scenarios.

**Ada's visual comparison (March 7, 2025):**
- Compared BF16 (left) vs INT4 (right) using official demo
- "Does not seem that much of a hit"
- Visual differences were subtle in the example shown

---

## Installation

### Requirements

- **Linux only** (as of March 2025)
- NVIDIA GPU: 3090, 4090, 5090, or Ada 6000
- CUDA toolkit
- PyTorch

### Installation Steps

```bash
git clone https://github.com/mit-han-lab/nunchaku
cd nunchaku
pip install -e .
```

**Note:** Installation into ComfyUI has been reported as problematic. Ada noted "could not install into comfy" on March 7, 2025.

---

## Compatibility

**Confirmed working:**
- Flux (mentioned in official materials)
- Likely works with Wan ("dont see a reason why it couldn't" — Ada)

**Limitations:**
- **Linux only** — no Windows support as of March 2025
- ComfyUI integration unclear/problematic
- May require custom integration work

---

## Comparison to Other Quantization Methods

| Method | Speedup (vs BF16) | Speedup (vs optimized baseline) | Quality | VRAM | Notes |
|--------|-------------------|----------------------------------|---------|------|-------|
| **SVDQuant INT4** | 3× (official) | ~30% (community) | Good | Low | Requires Nunchaku engine |
| **FP8 + compile + sage** | ~2× | Baseline | Good | Medium | Standard optimization stack |
| **GGUF Q8** | ~20% slower than fp8 | N/A | Best below fp16 | Medium | Widely used |
| **GGUF Q4** | Faster | N/A | Acceptable | Low | Low VRAM option |

**Key insight:** The 3× speedup claim compares to an unoptimized baseline. Against a properly optimized setup (fp8 + torch.compile + SageAttention), the speedup is closer to 30%.

---

## Known Issues

### Linux Only

As of March 2025, SVDQuant/Nunchaku only supports Linux. No Windows builds available.

> "linux only :/" — JmySff, March 7, 2025

### ComfyUI Integration

Multiple users reported difficulty integrating into ComfyUI:

> "could not install into comfy" — Ada, March 7, 2025

No confirmed working ComfyUI integration as of March 7, 2025.

### Quality Concerns

comfy noted that quantizing video models gives worse results than image models like Flux, suggesting Wan may be more sensitive to quantization artifacts.

### Edge Case Failures

deleted_user_2ca1923442ba noted quality hits "in weird edge cases like Sana with high PAG levels," suggesting the method may not be universally robust.

---

## When to Use

**Consider SVDQuant if:**
- You're on Linux
- You need maximum speed and can accept ~30% improvement over optimized baseline
- You're willing to do custom integration work
- VRAM is a constraint
- You can tolerate potential quality loss

**Stick with standard optimization if:**
- You're on Windows
- You need proven ComfyUI integration
- You want the best quality
- You already have fp8 + torch.compile + SageAttention working

---

## Future Development

**Potential improvements mentioned:**
- "initial benchmarks, and we are actively working on further kernel optimizations" — MIT Han Lab
- ComfyUI integration (community request)
- Windows support (community request)

---

## See Also

- [[quantization]] — Overview of quantization methods for Wan
- [[fp16-accumulate]] — Standard optimization that stacks with quantization
- [[sageattention]] — Standard optimization for comparison
- [[torch-compile]] — Standard optimization for comparison
- [[speed]] — Overview of all speed optimizations

## External Resources

- [Nunchaku GitHub Repository](https://github.com/mit-han-lab/nunchaku)
- [SVDQuant Blog Post](https://hanlab.mit.edu/blog/svdquant-nvfp4)
- [SVDQuant Demo](https://svdquant.mit.edu/)
- [Installation Guide](https://github.com/mit-han-lab/nunchaku?tab=readme-ov-file#installation)
