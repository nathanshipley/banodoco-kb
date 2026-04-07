---
title: Troubleshooting Wan Video Generation
aliases: [troubleshooting, wan-troubleshooting, errors]
last_updated: 2025-03-23
---

# Troubleshooting Wan Video Generation

Common issues and solutions for Wan 2.1 video generation.

## Black Output / NaN Values

### Symptoms
- Output video is completely black
- Console shows `tensor(nan)` errors
- Error: `RuntimeWarning: invalid value encountered in cast`

### Causes and Solutions

**SageAttention issues:**
- Some SageAttention modes produce black output on certain GPUs
- Try switching to SDPA (standard attention) as fallback
- SpargeAttention will not work with Wan — use SageAttention or SDPA

**Driver issues:**
- Update NVIDIA drivers to latest version
- Some users reported issues with specific driver versions
- Studio drivers vs Game Ready drivers may behave differently

**PyTorch/CUDA version mismatch:**
- Ensure PyTorch CUDA version matches your system
- Try updating to PyTorch 2.7.0+ with cu126 or cu128
- Command: `pip install -U torch torchvision --index-url https://download.pytorch.org/whl/cu126`

**Model corruption:**
- Re-download the model file
- Verify file integrity (check file size matches expected)
- Try a different quantization format (fp16, fp8, GGUF)

**Workflow issues:**
- Check that all nodes are properly connected
- Verify model loader settings match your model format
- Ensure VAE is loaded correctly

> "that just means it has Nans and that's why it's black" — Kijai, March 2, 2025

**Reported case (March 2, 2025):**
- User (Fawks) experienced black output on RTX 4090
- Tried multiple models (1.3B, 14B, bf16, fp8)
- Tried SDPA, SageAttention, SpargeAttention — all produced black output
- Updated drivers, updated PyTorch to cu126 — issue persisted
- Workflow appeared correct
- **Resolution:** Not confirmed in this conversation; may require deeper investigation

## T2V Errors

### TypeError: expected Tensor as element 1 in argument 0, but got NoneType

**Error message:**
```
TypeError: expected Tensor as element 1 in argument 0, but got NoneType
  File "wanvideo/modules/model.py", line 618, in forward
    x = [torch.cat([u, v], dim=0) for u, v in zip(x, y)]
```

**Cause:** Broken commit in wrapper repository (commit 8e0a90f)

**Solution:**
- Update to latest wrapper version (fixed March 2, 2025)
- Or roll back to previous commit: `git checkout <previous_hash>`

> "ok I have broken something, was only doing I2V and didn't notice" — Kijai, March 2, 2025

> "this should be fixed now" — Kijai, March 2, 2025

## RAM Issues

### Cannot allocate memory / mmap error

**Error message:**
```
unable to mmap 32789894024 bytes from file: Cannot allocate memory (12)
```

**Cause:** Insufficient system RAM for model loading

**Solutions:**

1. **Increase system RAM:**
   - 32 GB is minimum for I2V 14B
   - 64 GB recommended for comfortable operation
   - 96 GB ideal for complex workflows

2. **Increase swap file (Linux):**
   - Default swap (512 MB) is too small
   - Increase to 16-32 GB or more
   - NVMe swap is much faster than HDD
   - "my nvme isnt that much slower than ram 6GBPS vs like 30" — Benjimon, March 2, 2025

3. **Use smaller model:**
   - Try 1.3B instead of 14B
   - Use GGUF quantization (Q4, Q6) for lower memory footprint

> "32 is really low, could you increase your swap file if on linux?" — Benjimon, March 2, 2025

> "64gb kits are relatively inexpensive now especially if you are running ddr4. That being said I would go with 96 if you can manager it. Comfy can get really ram hungry." — cyncratic#0, March 2, 2025

### Windows Virtual Memory Issues (March 23, 2025)

**Symptoms:**
- OOM errors on model loading despite sufficient physical RAM
- `RuntimeError: CUDA error: out of memory` (which actually means RAM, not VRAM)
- System freezes or crashes

**Cause:** Windows virtual memory (page file) disabled or misconfigured

**Solution:**
1. Press Win + R, type `sysdm.cpl`, press Enter
2. Navigate to Advanced tab → Settings under Performance
3. Go to Advanced tab → Change under Virtual memory
4. Enable "Automatically manage paging file size for all drives"
5. Restart system

> "I put Assigned by the system in all drives" — Juampab12, March 23, 2025

> "omg it works now" — Juampab12, March 23, 2025

**Important:** Having 0 virtual memory will cause OOM errors even with 64GB physical RAM. Windows needs virtual memory for proper operation.

**Recommended settings:**
- Let Windows manage page file size automatically
- If setting manually, use 1.5x-2x your physical RAM
- Place page file on fastest drive (NVMe SSD preferred)

## PyTorch Hash Mismatch

### ERROR: THESE PACKAGES DO NOT MATCH THE HASHES FROM THE REQUIREMENTS FILE

**Error message:**
```
ERROR: THESE PACKAGES DO NOT MATCH THE HASHES FROM THE REQUIREMENTS FILE.
Expected sha256 5ddca43b81c64df8ce0c59260566e648ee46b2622ab6a718e38dea3c0ca059a1
Got        58b88c67ef499b2b650b91e08bf71665b1f004e9cd7f8e6116e6462ebe9f8b05
```

**Cause:** PyTorch package hash verification failure during installation

**Solution:**
- This is unusual and may indicate a corrupted download or mirror issue
- Try installing without hash verification (not recommended for security)
- Try a different PyTorch mirror
- Clear pip cache: `pip cache purge`
- Reinstall from scratch in a fresh environment

## ComfyUI Crashes

### System crashes after latest pull

**Symptoms:**
- ComfyUI crashes on startup or during generation
- May be related to recent updates

**Solutions:**

1. **Update frontend package:**
   - "New front end package required for Comfy FYI" — Shawneau, March 2, 2025
   - Update ComfyUI to latest version
   - Refresh browser (not just restart ComfyUI)

2. **Create fresh environment:**
   - Use conda to create isolated environment
   - Link models folder via `extra_model_paths.yaml`
   - Keeps multiple ComfyUI versions for stability
   - "I have several conda environments with various comfy installs from python 310 to 312 cuda 124 etc all linked to the same models folder. When things break It is less of an issue that way." — cyncratic#0, March 2, 2025

3. **Roll back updates:**
   - If crash started after update, roll back to previous version
   - Check git history for breaking commits

## Performance Issues

### Slow generation times

See [[speed]] for comprehensive optimization guide.

**Quick checklist:**
- Enable [[fp16-accumulate]] (requires PyTorch 2.7+)
- Enable [[sageattention]]
- Enable [[torch-compile]]
- Consider [[teacache]] for 2x speedup
- Use appropriate [[quantization]] (GGUF Q8 recommended)
- Check [[samplers]] — UniPC is fastest for quality

### VRAM issues

See [[hardware]] for VRAM requirements.

**Quick solutions:**
- Increase block swap
- Use lower quantization (GGUF Q4, Q6)
- Reduce resolution
- Use 1.3B instead of 14B
- Enable model offloading

## Workflow Issues

### Nodes not loading / missing nodes

**Solutions:**
- Update custom nodes via ComfyUI Manager
- Check for conflicting node names
- Restart ComfyUI after installing nodes
- Clear browser cache

### Workflow produces different results than expected

**Check:**
- Seed value (change for variation)
- Model version (wrapper vs native)
- Sampler settings (UniPC vs DPM++)
- CFG and shift values
- LoRA strengths

## Model-Specific Issues

### I2V vs T2V confusion

- I2V models require conditioning image
- T2V models work with text only
- VACE only works with T2V models (16 channels)
- Check model filename to confirm variant

### VAE errors

**Critical:** Wrapper and native use different VAEs
- **Wrapper:** Use Kijai's VAE from `Kijai/WanVideo_comfy`
- **Native:** Use Comfy-Org's VAE from `Comfy-Org/Wan_2.1_ComfyUI_repackaged`
- Mixing these will cause errors or degraded output

See [[wan-2.1#vae-compatibility]] for details.

## CUDA Issues (March 23, 2025)

### Multiple CUDA versions installed

**Symptoms:**
- SageAttention errors
- Path conflicts
- Inconsistent behavior

**Diagnosis:**
- Check installed CUDA versions in Control Panel
- Run `nvcc --version` in PowerShell to see active version
- Note: `nvidia-smi` shows driver version, not CUDA toolkit version

**Solution:**
1. Uninstall all CUDA toolkits
2. Install single version (12.4, 12.5, or 12.8 recommended)
3. Verify installation: `nvcc --version`
4. Reinstall PyTorch matching CUDA version

**CUDA version recommendations:**
- **12.4** — Stable, widely compatible (Benjimon's preference)
- **12.5** — Good balance
- **12.8** — Latest, required for 5000-series GPUs

> "I like cuda 12.4" — Benjimon, March 23, 2025

> "Theoretically 12.8 would work with everything" — Benjimon, March 23, 2025

**Visual Studio Integration:**
- May be needed for compiler support
- Not always required for inference
- If needed, install matching version for your CUDA toolkit

### SageAttention not working after CUDA changes

**Solution:**
- Reinstall SageAttention after CUDA/PyTorch changes
- Reinstall Triton if using Windows
- Clear pip cache: `pip cache purge`
- Verify PyTorch CUDA version matches installed CUDA toolkit

## Getting Help

**Before asking for help:**
1. Check this troubleshooting guide
2. Search Discord history for similar issues
3. Verify your setup matches requirements
4. Try the simplest possible workflow first

**When asking for help, provide:**
- GPU model and VRAM
- System RAM
- Operating system
- PyTorch version (`pip list | grep torch`)
- CUDA version (`nvcc --version`)
- ComfyUI version
- Exact error message (full traceback)
- Workflow file (if possible)
- What you've already tried

**Where to ask:**
- Discord #wan_chatter for general questions
- Discord #wan_comfyui for ComfyUI-specific issues
- GitHub issues for wrapper/node bugs

## See Also

- [[hardware]] — Hardware requirements and recommendations
- [[speed]] — Performance optimization guide
- [[wan-2.1]] — Base model documentation
- [[comfyui]] — ComfyUI setup and usage
