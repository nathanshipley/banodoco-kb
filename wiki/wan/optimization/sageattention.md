---
title: SageAttention
aliases: [sageattention, sage-attention, sage]
last_updated: 2025-03-06
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
