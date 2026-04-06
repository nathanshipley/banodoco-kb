---
title: FP16 Accumulation
aliases: [fp16-accumulate, fp16-accumulation, fp16_accumulation]
last_updated: 2025-03-04
---

# FP16 Accumulation

FP16 accumulation is a PyTorch optimization that performs matrix multiplication accumulation in FP16 precision instead of FP32, providing significant speed improvements for Wan 2.1 on NVIDIA consumer GPUs.

## Performance Impact

- **10-30% speed improvement** depending on GPU and model
- **Stacks with torch.compile and SageAttention** for cumulative speedup
- **~20-30% increase that stacks with compile and sageattn** — Kijai, March 1, 2025
- **On 3060:** ~2 minute reduction (23min → 21min) for 93 frames at 640x480 — Ashtar, March 4, 2025

## Requirements

- **PyTorch 2.7.0 or later** (nightly builds as of March 2025)
- NVIDIA GPU (Volta architecture or newer for best results)
- Works with GGUF via advanced GGUF node (some inconsistency reported)

## Installation

### Portable ComfyUI

```bash
python_embeded\python.exe -m pip install --pre -U torch torchvision --index-url https://download.pytorch.org/whl/nightly/cu126
```

**Note:** Use `-U` flag to ensure update to newest nightly. Without it, pip may not update properly.

### Standard Installation

```bash
pip install --pre -U torch torchvision --index-url https://download.pytorch.org/whl/nightly/cu128
```

**Critical:** Do not include `torchaudio` in the install command — it doesn't exist for latest nightly builds and will cause the installation to fail.

**Update (March 3, 2025):** Some users report torchaudio is available for certain nightly versions. On Windows, one user successfully installed:
```
torch==2.7.0.dev20250127+cu126
torchaudio==2.6.0.dev20250128+cu126
torchvision==0.22.0.dev20250128+cu126
```

However, installing torchaudio may downgrade PyTorch to an older nightly that doesn't support fp16 accumulation. If you need torchaudio, verify your PyTorch version after installation.

**Update (March 4, 2025):** Latest nightly as of March 4 is `torch-2.7.0.dev20250302+cu126`.

### Reverting to Stable

If you need to go back to stable PyTorch:

```bash
pip uninstall torch torchvision
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu126
```

## Enabling FP16 Accumulation

### Kijai Wrapper

FP16 accumulation is **automatic** in the wrapper when using PyTorch 2.7.0+. The wrapper sets:

```python
torch.backends.cuda.matmul.allow_fp16_accumulation = True
```

As of March 1, 2025, Kijai added an **optional toggle** in the wrapper nodes to enable/disable fp16 accumulation manually. Look for the `_fast` suffix on model loader nodes.

### Native ComfyUI

Two methods:

1. **Launch flag:** Add `--fast fp16_accumulation` to your ComfyUI launch command
   - Example: `python.exe main.py --use-sage-attention --fast fp16_accumulation`
   - **Note:** Requires ComfyUI update to v0.3.19 or later to recognize the flag
2. **Node setting:** Use Kijai's model loader node with compute_dtype set to `fp16`

**Important:** After updating to PyTorch 2.7.0 nightly, you must also update ComfyUI to the latest version for the `--fast fp16_accumulation` flag to be recognized. Update ComfyUI first, then restart (and refresh browser, not just restart ComfyUI).

## Precision Compatibility

| Weight Format | FP16 Accumulation | Notes |
|---------------|------------------|-------|
| **fp16** | ✅ Perfect | No conversion needed |
| **fp8** | ✅ Good | Weights upcast to fp16 for calculations; doesn't matter if using fp8 quant |
| **bf16** | ⚠️ Lossy | Avoid — bf16 to fp16 conversion loses precision |
| **GGUF** | ✅ Works | Via advanced GGUF node; some inconsistency reported |

> "if you used bf16 weights and did calculations in fp16 that would be lossy" — Kijai, March 1, 2025

> "if you use fp8 quant, it doesn't matter" — Kijai, Discord #wan_chatter, March 1, 2025

## Known Issues

### VAE Decode Error

Some users reported VAE decode errors when using fp16 accumulation with the `compute_dtype` node setting. Workarounds:

1. Add a VRAM unload node between sampler and VAE decode
2. Use `--fast fp16_accumulation` launch flag instead of the compute_dtype node

**Update (March 1, 2025):** User Miku reported this issue was resolved: "btw kijai, idk if you or comfy did something but im not having the sampler - vae issue anymore, i can use fp16 acum from ur node without issues 👍" — Discord #wan_chatter

### Offloading Issues

Some users reported slower generation with fp16 accumulation when offloading is enabled. Try the `--fast fp16_accumulation` flag instead of the node-based setting.

### Torch Version Detection

If you see the error:

```
torch.backends.cuda.matmul.allow_fp16_accumulation is not available in this version of torch, requires torch 2.7.0 nightly currently
```

Your PyTorch version is too old. Update to the latest nightly:

```bash
pip install --pre -U torch torchvision --index-url https://download.pytorch.org/whl/nightly/cu128
```

Note: The `-U` flag is critical — without it, pip may not update to the newest nightly.

### Torchaudio Version Conflicts

When installing nightly PyTorch with torchaudio, you may encounter version downgrades:

- Installing torchaudio can downgrade PyTorch from `2.7.0.dev20250301+cu126` to `2.7.0.dev20250127+cu126`
- The older version may not support fp16 accumulation
- If you don't need torchaudio, omit it from the installation
- If you need both, verify PyTorch version after installation and reinstall if necessary

### ComfyUI Version Requirement

The `--fast fp16_accumulation` flag requires ComfyUI v0.3.19 or later. If the flag is not recognized:

1. Update ComfyUI: `[ComfyUI-Manager] Updating ComfyUI: v0.3.18-11-gd6e5d487 -> v0.3.19`
2. Restart ComfyUI
3. **Refresh your browser** (not just restart ComfyUI) for nodes to update properly

## Performance Stack

For maximum performance, combine fp16 accumulation with:

- [[sageattention]] — ~25% speedup alone, nearly 2x with fp16 accumulate
- [[torch-compile]] — ~30% speedup, stacks with both
- [[teacache]] — ~2x speedup, stacks with fp16 accumulate

Achievable combined speedup: **~2x faster** than baseline (or more with TeaCache)

## See Also

- [[wan-2.1]] — Base model that benefits from fp16 accumulation
- [[quantization]] — Understanding fp16, fp8, and bf16 formats
- [[sageattention]] — Complementary optimization
- [[torch-compile]] — Another stackable optimization
- [[teacache]] — Latent caching optimization
