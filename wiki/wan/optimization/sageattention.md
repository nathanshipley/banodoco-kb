---
title: SageAttention
aliases: [sageattention, sage-attention, sage]
last_updated: 2025-03-10
---

# SageAttention

SageAttention is an attention optimization that provides significant speed improvements for Wan 2.1 with minimal quality loss. It's one of the most impactful free optimizations available.

## Performance Impact

- **Speed gain:** ~25% alone, nearly 2x when combined with fp16 accumulate and torch.compile
- **Quality impact:** Minimal to none in most cases
- **VRAM impact:** Neutral to slightly positive
- Stacks with [[fp16-accumulate]] and [[torch-compile]]

## Installation

### Standard Installation

```bash
pip install sageattention
```

### From Source (for latest features)

```bash
git clone https://github.com/thu-ml/SageAttention
cd SageAttention
pip install -e . --no-build-isolation
```

**Note:** The `--no-build-isolation` flag is required if torch is not found during installation. You must also have **ninja** installed in your ComfyUI venv for SageAttention 2.0 to compile properly.

> "the only key piece of info missing in all the guides is you have to have ninja installed into the comfyui venv or sageattention 2.0 won't actually compile" — jellybean5361, March 6, 2025

### Prebuilt Wheels (Windows)

Prebuilt Windows wheels available at: https://github.com/woct0rdho/SageAttention/releases

**Latest version (March 2025):** SageAttention 2.1.1

**Installation from wheel:**
```bash
python -m pip install sageattention-2.1.1-cp312-cp312-win_amd64.whl
```

> "i downloaded the file kijai shared and did this: python.exe -m pip install sageattention-2.0.0-cp312-cp312-win_amd64.whl" — BestWind, March 10, 2025

## Usage

### Native ComfyUI

Add the launch flag:
```bash
--use-sage-attention
```

No node required — the flag enables it globally.

### Kijai Wrapper

Use the **PatchSageAttention** node rather than the CLI flag. The node form is more reliable with ComfyUI's model patching.

**Available modes:**
- `auto` — Automatically selects best mode (may cause issues)
- `fp16_cuda` — FP16 CUDA kernel
- `fp8_cuda` — FP8 CUDA kernel (fastest on Ada+)
- `sageattn_qk_int8_pv_fp16_triton` — FP16 Triton kernel
- `sageattn_qk_int8_pv_fp16_cuda` — FP16 CUDA kernel (alternative)
- `sage_attn_fp16` — FP16 mode for multi-GPU setups

**Recommendation:** Select a specific mode instead of `auto` if you encounter issues.

## Kernel Selection by GPU Architecture

SageAttention auto-selects kernels based on hardware:

| GPU Architecture | Auto-Selected Kernel | Notes |
|-----------------|---------------------|-------|
| **A100** | `sageattn_qk_int8_pv_fp16_cuda` | Ampere flagship |
| **Other Ampere (3090, etc.)** | `sageattn_qk_int8_pv_fp16_triton` | 3090, 3090 Ti, A6000 |
| **Ada (4090, 5090, L40)** | `sageattn_qk_int8_pv_fp8_cuda` | Fastest on Ada+ |
| **Hopper (H100)** | `sageattn_qk_int8_pv_fp8_cuda_sm90` | Hopper-specific |
| **Blackwell (B100)** | `sageattn_qk_int8_pv_fp8_cuda` | Latest architecture |

> "A100 = `sageattn_qk_int8_pv_fp16_cuda`" — Doctor Shotgun, March 10, 2025

> "other Ampere = `sageattn_qk_int8_pv_fp16_triton`" — Doctor Shotgun, March 10, 2025

> "Ada = `sageattn_qk_int8_pv_fp8_cuda`" — Doctor Shotgun, March 10, 2025

> "Hopper = `sageattn_qk_int8_pv_fp8_cuda_sm90`" — Doctor Shotgun, March 10, 2025

> "Blackwell = `sageattn_qk_int8_pv_fp8_cuda`" — Doctor Shotgun, March 10, 2025

## Performance Benchmarks

**4090 with fp8 weights + torch.compile + SageAttention:**
- **int8+fp8 kernel:** 38 s/it
- **int8+fp16 kernel:** 47 s/it
- **xformers (baseline):** ~75 s/it

> "i get 38 s/it with int8fp8 and 47 s/it with int8fp16" — Doctor Shotgun, March 10, 2025

> "xformers like 75 s/it or sth lmao" — Doctor Shotgun, March 10, 2025

**Speedup analysis:**
- fp8 kernel is ~25% faster than fp16 kernel
- fp8 kernel is ~2x faster than xformers baseline
- fp16 kernel is ~1.6x faster than xformers baseline

## Multi-GPU Usage

SageAttention works with multi-GPU setups and gets monkeypatched automatically when using xfuser or FSDP.

**For multi-GPU scripts:**
- SageAttention integrates automatically
- No special configuration needed
- Works with FSDP (Fully Sharded Data Parallel)

**Forcing FP16 mode in multi-GPU:**

For scripts that need to force FP16 Triton mode, edit SageAttention source:

```python
# In sageattention/core.py, line ~130
# Change the if statement to always use fp16_triton
return sageattn_qk_int8_pv_fp16_triton(...)
```

Or use the `sage_fp16` branch with `--attn_impl sage_attn_fp16` flag.

**I2V with multi-GPU:**

Some users experience issues with fp8 SageAttention on I2V in multi-GPU setups. Use `--attn_impl sage_attn_fp16` instead of the default fp8 mode.

> "the 8+8 kernel produces black output" — referring to fp8_cuda on I2V — Discord #wan_chatter, March 2025

## Known Issues

### I2V Black Output

**Problem:** I2V generations produce completely black output when using certain SageAttention modes.

**Cause:** The `fp8_cuda` kernel (specifically `sageattn_qk_int8_pv_fp8_cuda`) causes precision overflow on I2V models.

> "i2v doesnt work for me with fp8 sage" — Doctor Shotgun, March 10, 2025

> "something overflows to NaN and you get a black image" — Doctor Shotgun, March 10, 2025

**Solution:** Use the FP16 kernel instead:
- In wrapper: Select `sageattn_qk_int8_pv_fp16_triton` or `sageattn_qk_int8_pv_fp16_cuda`
- In native: Use the PatchSageAttention node with fp16 mode
- In multi-GPU: Use `--attn_impl sage_attn_fp16` flag

### GPU Compatibility

**Ada+ GPUs (4090, 5090, L40):**
- `fp8_cuda` works and is fastest
- All modes supported

**Ampere GPUs (3090, 3090 Ti, A6000):**
- `fp8_cuda` may not work properly
- Use `fp16_cuda` or `fp16_triton` modes
- Still provides significant speedup

**Older GPUs:**
- May not support SageAttention at all
- Fall back to SDPA (standard attention)

### Auto Mode Issues

**Problem:** `auto` mode may select incompatible kernels or cause crashes.

**Solution:** Manually select a specific SageAttention mode:
- For T2V: Try `fp8_cuda` first (Ada+) or `fp16_cuda` (Ampere)
- For I2V: Use `fp16_triton` or `fp16_cuda`
- If issues persist, try different modes until one works

### Wan 2.1 Compatibility

**Current status (March 2025):**
- SageAttention does not work with Wan 2.1 on all GPUs
- Requires selecting specific SageAttention 2.0 modes
- Some users report it working, others get black screens

> "Doesn't work with Wan currently, at least not on all GPUs, need to select specific sageattn 2.0 mode" — Kijai, Discord #wan_chatter, March 6, 2025

**Workaround:** Use the PatchSageAttention node and manually select modes:
1. Try `fp16_cuda` first
2. If that fails, try `fp16_triton`
3. If all modes fail, disable SageAttention and use SDPA

### Black Screen with Native

**Problem:** Black screen output when using SageAttention in native ComfyUI.

**Solutions:**
1. Change SageAttention mode from `auto` to `fp16` in the patch node
2. Try `fp8_e5m2` precision instead of `fp8_e4m3fn`
3. Disable SageAttention and use SDPA as fallback

> "change this from auto to fp16" — Cubey, Discord #wan_chatter, March 6, 2025

### Triton Errors

Some users encounter Triton-related errors when running with SageAttention:

**Possible causes:**
- VRAM pressure triggering different code paths
- Missing Triton installation
- Incompatible Triton version

**Solutions:**
- Triton is an optimization, not strictly required
- Behavior can change based on available VRAM
- Try reducing frame count or resolution
- Switch to non-Triton modes (`fp16_cuda` instead of `fp16_triton`)

> "Some behaviour can change depending on how much free VRAM you have at the time, so possibly once you'd run it you had a bit less (due to caching) and that triggered a different thing to happen (requiring Triton)" — Screeb, Discord #wan_chatter, March 4, 2025

### PyTorch Nightly Compatibility

**Issue:** After upgrading to PyTorch nightly (2.7.0+), SageAttention may need to be reinstalled.

**Error message:**
```
ValueError: Can't import SageAttention: DLL load failed while importing _qattn: The specified procedure could not be found.
```

**Solution:** Reinstall SageAttention after PyTorch upgrade:
```bash
pip install sageattention-2.1.1-cp312-cp312-win_amd64.whl
```

> "sageattention need to be reinstalled to match the new latest torch or something like that?" — BestWind, March 10, 2025

> "possibly" — Kijai, March 10, 2025

**Note:** Some users report SageAttention 1.0.6 continuing to work with PyTorch 2.7.0 without reinstallation, but upgrading to SageAttention 2.1+ is recommended.

### Triton Version Requirements

**Windows users:** Triton 3.0+ is required for SageAttention 2.0+.

**Installation:**
```bash
pip install triton-windows
```

> "windows triton should be in pypi now" — Kijai, March 10, 2025

> "pip install triton-windows" — Kijai, March 10, 2025

**Reported working configurations:**
- SageAttention 1.0.6 + Triton 3.2.0 + PyTorch 2.7.0
- SageAttention 2.0.0 + Triton 3.0.0 + PyTorch 2.7.0
- SageAttention 2.1.1 + Triton 3.0.0 + PyTorch 2.7.0

### First-Time Compilation

**Issue:** First time running SageAttention shows compilation logs (ptxas).

**Behavior:**
- Compilation logs only appear on first run
- Subsequent runs use cached compiled kernels
- Logs may reappear if cache is cleared or settings change

> "ptxas only shows up in the console first time it does something, then it's cached" — Kijai, March 10, 2025

> "it won't show when it uses the cached" — Kijai, March 10, 2025

## Quality Impact

### Quantization Concerns

**Community perspective on 8-bit attention:**

> "taking the precision hit to 8bit to me sounds like meh when im used to ppl around me trying to run LLMs in friggin 2.5bit weight quantization" — Doctor Shotgun, March 10, 2025

SageAttention uses 8-bit quantization for attention calculations, which is inherently lossy. However:
- The quality loss is minimal in practice
- Much less aggressive than extreme LLM quantization (2.5-bit)
- According to SageAttention's paper, quality impact is negligible

**fp8 vs fp16 quality:**

Community reports suggest minimal quality difference:
- fp8 kernel is faster but theoretically lower quality
- In practice, differences are hard to detect
- Speed gain (25%) often worth the minimal quality tradeoff

> "according to sageattention's paper claims, it doesnt [degrade quality]" — Doctor Shotgun, March 10, 2025

> "but it is quantized attention" — Doctor Shotgun, March 10, 2025

## Performance Comparison

| Mode | Speed | Quality | GPU Support |
|------|-------|---------|-------------|
| **fp8_cuda** | Fastest | Good | Ada+ only |
| **fp16_cuda** | Fast | Best | All modern GPUs |
| **fp16_triton** | Fast | Best | All modern GPUs |
| **SDPA (no SageAttention)** | Baseline | Best | All GPUs |

**Typical speedup over SDPA:**
- fp8_cuda: ~30-40% faster
- fp16_cuda/triton: ~20-30% faster

## Troubleshooting

| Problem | Solution |
|---------|----------|
| Black output on I2V | Use fp16 mode instead of fp8 |
| Black output on T2V | Try different SageAttention modes; check GPU compatibility |
| "auto" mode crashes | Select specific mode (fp16_cuda or fp16_triton) |
| Triton errors | Switch to non-Triton mode or reduce VRAM usage |
| No speedup | Verify SageAttention is actually enabled (check console logs) |
| Slower than SDPA | Check for VRAM pressure causing offloading; increase block swap |
| Installation fails | Use `--no-build-isolation` flag; ensure torch and ninja are installed first |
| Compilation fails | Install ninja in ComfyUI venv: `pip install ninja` |
| DLL load failed after PyTorch upgrade | Reinstall SageAttention to match new PyTorch version |
| ptxas logs appearing | Normal on first run; subsequent runs use cached kernels |

## Performance Stack

For maximum performance, combine SageAttention with:

- [[fp16-accumulate]] — ~20-30% speedup, stacks with SageAttention
- [[torch-compile]] — ~30% speedup, stacks with SageAttention
- [[teacache]] — ~2x speedup, stacks with SageAttention

Achievable combined speedup: **~3-4x faster** than baseline with all optimizations

## See Also

- [[wan-2.1]] — Base model that benefits from SageAttention
- [[fp16-accumulate]] — Stackable optimization
- [[torch-compile]] — Stackable optimization
- [[teacache]] — Stackable optimization
- [[speed]] — Overview of all speed optimizations
- [[multi-gpu]] — Multi-GPU generation with SageAttention

## External Resources

- [SageAttention GitHub](https://github.com/thu-ml/SageAttention)
- [SageAttention Windows Builds](https://github.com/woct0rdho/SageAttention/releases)
- [SageAttention Paper](https://arxiv.org/abs/2410.02367)
- [Triton Windows PyPI](https://pypi.org/project/triton-windows/)
