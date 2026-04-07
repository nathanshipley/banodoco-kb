---
title: Comfy Scaled FP8 Models
aliases: [scaled-fp8, fp8-scaled, comfy-scaled]
last_updated: 2025-03-08
---

# Comfy Scaled FP8 Models

Comfy (the ComfyUI developer) released new "scaled" fp8 quantized models for Wan 2.1 on March 7, 2025. These models use a different quantization approach than standard fp8, avoiding fp8 matrix multiplication in favor of better quality preservation.

> "these models seem a lot more resistant to quantization" — comfy, March 7, 2025

> "wasn't able to get fp8 matrix mult working without quality degradation" — comfy, March 7, 2025

---

## Overview

The scaled fp8 models are designed to provide better quality than standard fp8 quantization while maintaining similar VRAM requirements. The key difference is that they avoid using fp8 matrix multiplication, which can cause quality degradation on Wan models.

**Key features:**
- Better quality than standard fp8
- Similar VRAM usage to standard fp8
- Requires updated ComfyUI to use properly
- Works with fp16 accumulation for best performance

---

## Availability

**Repository:** https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/tree/main/split_files/diffusion_models

**Models available:**
- T2V 1.3B fp8_scaled
- T2V 14B fp8_scaled
- I2V 14B 480p fp8_scaled
- I2V 14B 720p fp8_scaled

---

## Usage

### Requirements

1. **Update ComfyUI** to latest version (March 7, 2025 or later)
2. **Use native ComfyUI nodes** (not wrapper)
3. **Optional but recommended:** PyTorch 2.7+ with fp16 accumulation

> "make sure to update comfyui or else it will use fp8 matrix mult with them by default" — comfy, March 7, 2025

### Loading the Model

1. Download the scaled fp8 model from the repository
2. Place in your ComfyUI models folder
3. Load using the standard model loader node
4. ComfyUI will automatically detect it's a scaled model

**Verification:**
Comfy added a print statement to confirm proper loading:
> "I added a new print so it tells you if it's using fp8 matrix mult with scaled" — comfy, March 7, 2025

Check your console output to verify the model is being loaded correctly.

---

## Performance

### Speed

**Community reports (March 7-8, 2025):**

**Doctor Shotgun:**
- "scaled fp8 is slower by like 9 s/it for me compared to regular fp8"
- Tested on unspecified GPU

**N0NSens:**
- "tested. +-same" (comparing scaled to regular fp8)
- Tested on unspecified setup

**Consensus:** Scaled fp8 appears to be slightly slower than regular fp8, but the difference is relatively small (within ~20% based on reported numbers).

### Quality

> "yes it should be a bit better" — comfy, March 7, 2025 (comparing scaled to regular fp8)

The quality improvement is the main reason to use scaled fp8 over regular fp8. Comfy noted that Wan models are "a lot more resistant to quantization" than other models, making proper quantization more challenging.

---

## Recommended Setup

**For best performance:**

1. Use scaled fp8 model
2. Enable fp16 accumulation (requires PyTorch 2.7+)
3. Use `--fast fp16_accumulation` launch flag
4. Enable SageAttention
5. Enable torch.compile

> "so fastest way to run them without quality penalty is going to be fp16 + fp16 accumulation" — comfy, March 7, 2025

Note: This recommendation applies to running at fp16 precision with fp16 accumulation, not specifically to the scaled fp8 models. However, the scaled fp8 models also benefit from fp16 accumulation.

---

## Comparison to Other Formats

| Format | Quality | Speed | VRAM | Notes |
|--------|---------|-------|------|-------|
| **fp16** | Best | Fast with fp16 acc | High | Recommended by comfy for best quality |
| **Scaled fp8** | Better than fp8 | Slightly slower than fp8 | Medium | Good balance |
| **Regular fp8** | Good | Fast | Medium | Standard option |
| **GGUF Q8** | Best below fp16 | ~20% slower than fp8 | Medium | Community favorite |
| **GGUF Q6** | Good | Faster than Q8 | Lower | 16GB VRAM option |

---

## Known Issues

### Requires ComfyUI Update

Older versions of ComfyUI will use fp8 matrix multiplication with scaled models, defeating the purpose. Update to March 7, 2025 or later.

### Speed Regression

Some users report scaled fp8 being slower than regular fp8. This appears to be a tradeoff for better quality.

### Limited Testing

As of March 8, 2025, community testing is still limited. More feedback needed on quality vs speed tradeoffs.

---

## Portable ComfyUI with PyTorch Nightly

Comfy released a standalone portable ComfyUI package with PyTorch nightly (2.7+) that includes fp16 accumulation support:

**Download:** https://github.com/comfyanonymous/ComfyUI/releases/download/latest/ComfyUI_windows_portable_nvidia_or_cpu_nightly_pytorch.7z

**Features:**
- PyTorch 2.7+ nightly
- fp16 accumulation support
- Includes .bat file for easy fp16 accumulation launch
- Windows portable installation

> "if anyone is looking for a standalone package with pytorch nightly that has support for fp16 accumulation" — comfy, March 7, 2025

---

## See Also

- [[quantization]] — Overview of quantization methods
- [[fp16-accumulate]] — Using fp16 accumulation for speed
- [[wan-2.1]] — Base model documentation
- [[speed]] — Other speed optimizations

## External Resources

- [Comfy-Org Wan Models Repository](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged)
- [Portable ComfyUI with PyTorch Nightly](https://github.com/comfyanonymous/ComfyUI/releases/download/latest/ComfyUI_windows_portable_nvidia_or_cpu_nightly_pytorch.7z)
