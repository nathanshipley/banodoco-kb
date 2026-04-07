---
title: Multi-GPU Generation
aliases: [multi-gpu, multigpu, distributed]
last_updated: 2025-03-11
---

# Multi-GPU Generation

Multi-GPU generation allows running Wan models across multiple GPUs to achieve faster generation times and handle larger models that don't fit on a single GPU.

## Overview

Multi-GPU support for Wan uses FSDP (Fully Sharded Data Parallel) to shard and offload the model across multiple GPUs. This enables:

- Running full-quality models on multiple consumer GPUs
- Faster generation through parallel processing
- Handling models that exceed single-GPU VRAM
- **TeaCache support** for additional speedup (confirmed March 11, 2025)
- **Torch.compile support** for further optimization (in development March 11, 2025)

## Implementation

### Wan Multi-GPU Script

**Repository:** https://github.com/intervitens/Wan-MultiGPU

**Maintained by:** intervitens

**Features:**
- FSDP-based model sharding
- Automatic SageAttention integration
- Support for both T2V and I2V
- Weight offloading for VRAM management
- Ring attention for sequence parallelism
- Ulysses attention for additional parallelism
- **TeaCache support** (March 11, 2025)
- **Torch.compile support** (in development March 11, 2025)

### Hardware Requirements

**Tested configurations:**
- 4x 3090 Ti (24 GB each) — Full quality I2V 720p
- 4x 4090 (24 GB each) — Full quality I2V 720p
- 8x 4090 (24 GB each) — Tested but requires optimization
- 9x 4090 + 1x 5090 — Tested in production

**Minimum recommended:**
- 4 GPUs with 12+ GB VRAM each
- NVLink or high-bandwidth interconnect (recommended)
- 64+ GB system RAM

## Setup

### Installation

```bash
git clone https://github.com/intervitens/Wan-MultiGPU
cd Wan-MultiGPU
pip install -r requirements.txt
```

### SageAttention Configuration

**For I2V models:**

Some users experience issues with fp8 SageAttention on I2V. Two solutions:

1. **Use the sage_fp16 branch:**
```bash
git checkout sage_fp16
pip install -e . --no-build-isolation
```

Then use `--attn_impl sage_attn_fp16` flag.

2. **Patch SageAttention manually:**

Edit `sageattention/core.py` line ~130 to always use fp16_triton:

```python
# Change from:
if sm >= 89:
    return sageattn_qk_int8_pv_fp8_cuda(...)
else:
    return sageattn_qk_int8_pv_fp16_triton(...)

# To:
return sageattn_qk_int8_pv_fp16_triton(...)
```

**For T2V models:**

fp8 SageAttention should work without modification.

### Text Encoder Options

The script supports three modes for the T5 text encoder:

| Mode | Flag | Description | Speed | VRAM |
|------|------|-------------|-------|------|
| **CPU** | `--t5_cpu` | Runs T5 on CPU | Slowest | Lowest GPU VRAM |
| **FSDP** | `--t5_fsdp` | Runs T5 on GPU with offloading | Fastest | Higher GPU VRAM |
| **Default** | (none) | Standard GPU execution | Medium | Medium |

**CPU mode bottleneck:**

When using `--t5_cpu`, the text encoder becomes a significant bottleneck:
- Uses only 4 CPU cores by default
- Can take several minutes for encoding
- Alternates between CPU bursts and idle periods

**Optimization:**

Set `OMP_NUM_THREADS` to use more CPU cores:

```bash
export OMP_NUM_THREADS=X
```

Where X = (total CPU cores) / (number of GPUs)

Example for 96 cores and 4 GPUs: `export OMP_NUM_THREADS=24`

**Recommendation:** Use `--t5_fsdp` for best performance if you have sufficient VRAM.

## Usage

### Basic I2V Generation

```bash
OMP_NUM_THREADS=24 CUDA_VISIBLE_DEVICES=0,1,2,3 NCCL_P2P_LEVEL=SYS \
torchrun --nproc_per_node=4 generate.py \
  --task i2v-14B \
  --size 1280*720 \
  --ckpt_dir ./Wan2.1-I2V-14B-720P-FP16 \
  --image examples/input.jpg \
  --fp16_acc \
  --dit_fsdp \
  --dit_fsdp_offload \
  --t5_fsdp \
  --ring_size 4 \
  --offload_model True \
  --attn_impl sage_attn_fp16 \
  --prompt "Your prompt here"
```

### Key Parameters

| Parameter | Description | Recommended Value |
|-----------|-------------|-------------------|
| `--nproc_per_node` | Number of GPUs to use | 4 |
| `--fp16_acc` | Enable FP16 accumulation | Always use |
| `--dit_fsdp` | Enable FSDP for DiT | Always use |
| `--dit_fsdp_offload` | Offload DiT weights | Use for VRAM management |
| `--t5_fsdp` | Run T5 on GPU with FSDP | Recommended |
| `--t5_cpu` | Run T5 on CPU | Use if VRAM limited |
| `--ring_size` | Sequence parallelism size | Match GPU count for best results |
| `--ulysses_size` | Additional parallelism | Experimental; test carefully |
| `--offload_model` | Enable model offloading | True |
| `--attn_impl` | Attention implementation | `sage_attn_fp16` for I2V |
| `--base_seed` | Random seed | Set for reproducibility |
| `--master_port` | Port for distributed training | Change if running multiple instances |
| `--tc_thresh` | TeaCache threshold | 0.18-0.3 for speedup (March 11, 2025) |

### Environment Variables

| Variable | Purpose | Example |
|----------|---------|----------|
| `OMP_NUM_THREADS` | CPU threads for T5 | 24 |
| `CUDA_VISIBLE_DEVICES` | Select GPUs | 0,1,2,3 |
| `NCCL_P2P_LEVEL` | GPU communication | SYS |

## Performance

### Benchmarks

**4x 3090 Ti:**
- Resolution: 1280x720
- Frames: 81
- Time: ~29.5 s/it
- Quality: Full quality, no compromises

**4x 4090:**
- Resolution: 1280x720
- Frames: 81
- Time: ~3 minutes total (estimated)
- Quality: Full quality

**4x 4090 with TeaCache (March 11, 2025):**
- **Without TeaCache:** 15 minutes
- **With TeaCache (threshold 0.18):** 10 minutes (near-identical quality)
- **With TeaCache (threshold 0.3):** 7.5 minutes (some artifacts, useful for prompt finding)
- **Speedup:** 33-50% faster with TeaCache

**8x 4090:**
- Tested but requires optimization
- `ring_size 8` shows minimal improvement over 4 GPUs
- `ring_size 4` + `ulysses_size 2` is 4x slower than 4 GPUs
- Optimal configuration still being determined

> "running ring_size 8 is definitely not useful it's basically the same speed it was with 4 gpus" — aikitoria, March 6, 2025

> "ring_size 4 and ulysses_size 2 makes it 4 times slower than 4 gpus" — aikitoria, March 6, 2025

**Note:** 4090 performance may be lower than expected due to optimization opportunities. The script is still being optimized. For 8+ GPU setups, experimenting with `--ring_size` vs `--ulysses_size` may yield better results.

### Performance Factors

**GPU utilization:**
- Check that all GPUs reach maximum TDP during generation
- Uneven load may indicate configuration issues
- Use `nvidia-smi` to monitor utilization

**Power consumption:**
- 4x 4090 setup can draw ~4kW total power
- Thermal camera shows significant heat generation
- Ensure adequate cooling and power supply capacity

> "this sure heats up the room to have 4kw of gpus running" — aikitoria, March 6, 2025

**Bottlenecks:**
- T5 encoding on CPU (use `--t5_fsdp` instead)
- Insufficient CPU cores for T5 (increase `OMP_NUM_THREADS`)
- Slow interconnect between GPUs (NVLink recommended)
- VRAM pressure causing excessive offloading

## TeaCache Integration (March 11, 2025)

intervitens successfully integrated TeaCache with the multi-GPU script:

> "btw I think I got teacache working with the multigpu script" — intervitens, March 11, 2025

### TeaCache Performance

**Threshold 0.18:**
- Time: 15 minutes → 10 minutes
- Quality: "videos look near identical to me" — intervitens
- **Recommended for production use**

**Threshold 0.3:**
- Time: 15 minutes → 7.5 minutes
- Quality: "some noticeable artifacts" but "movement and overall composition are almost the same"
- **Useful for prompt/seed finding**

### Visual Comparison

intervitens shared side-by-side comparisons:
- Left: No TeaCache
- Right: TeaCache with 0.18 threshold
- Result: Near-identical quality with 33% speedup

### Use Cases

**Production rendering:**
- Use threshold 0.18 for near-identical quality
- 33% speedup with minimal quality loss
- Suitable for final outputs

**Rapid iteration:**
- Use threshold 0.3 for 50% speedup
- Some artifacts but composition/motion preserved
- Excellent for finding good prompts/seeds
- Re-render finals at lower threshold

### Activation

Set `--tc_thresh 0.22` (or other value) to activate TeaCache:

```bash
torchrun --nproc_per_node=4 generate.py \
  --task i2v-14B \
  --tc_thresh 0.18 \
  # ... other parameters
```

## Torch.compile Integration (March 11, 2025)

aikitoria is actively working on torch.compile integration for the multi-GPU script:

> "I'm still trying to get the compile to do anything" — aikitoria, March 11, 2025

**Current status:**
- Compiling individual blocks doesn't provide speedup
- Compiling entire model is slow and may not be beneficial
- torch_tensorrt attempted but has compatibility issues (f64 types, missing trtllm)
- Work in progress

**Implementation note:**

For torch.compile to work with FSDP, add `use_orig_params=True` to the FSDP function call in `wan/distributed/fsdp.py`:

```python
# In wan/distributed/fsdp.py
FSDP(..., use_orig_params=True)
```

## Precision and Quality

### fp16 vs fp8

Community testing shows minimal quality difference between fp16 and fp8 on multi-GPU setups:

> "either I'm blind or there is no difference" — aikitoria, March 6, 2025 (comparing fp8 vs fp16)

> "if anything the fp8 looks a bit cleaner lol" — Draken, March 6, 2025

**Recommendation:** Use fp8 for faster generation with negligible quality loss.

## Known Issues

### Initial Loading Time

**Problem:** Long delay after "generating video" message appears.

**Cause:** Model loading and T5 encoding happen before generation starts.

**Timeline:**
1. VRAM allocation (visible in nvidia-smi)
2. "generating video" message
3. T5 encoding (CPU or GPU, depending on flags)
4. Model sharding and distribution
5. Generation begins

**Workaround:** Be patient. First generation takes longest; subsequent generations with same model are faster.

**Future improvement:** Server mode to keep model loaded between generations (planned).

### Hunyuan I2V Multi-GPU

**Status:** Experimental, not fully working as of March 2025.

**Issue:** OOM during VAE encode stage when using FSDP.

**Workaround:** None currently. Single-GPU Hunyuan I2V works fine.

### Unbalanced GPU Load

**Problem:** One GPU shows higher VRAM usage than others.

**Cause:** Another process pre-loaded on that GPU.

**Solution:** 
- Use `CUDA_VISIBLE_DEVICES` to select different GPUs
- Clear GPU memory before running
- Ensure no other processes are using the GPUs

### Seed Randomness

**Problem:** Results vary between runs even with same settings.

**Cause:** No seed specified, random seed used.

**Solution:** Add `--base_seed 12345` to command for reproducibility.

### Multiple Instances

**Problem:** `The server socket has failed to listen on any local network address. port: 29500`

**Cause:** Trying to run multiple instances on the same port.

**Solution:** Use `--master_port=29501` (or other port) for additional instances.

> "looks like we can fix with `--master_port=29501`" — aikitoria, March 6, 2025

### Resolution and Frame Limits

**Current limitations:**
- Default resolution is 1280x720
- Higher resolutions may OOM during VAE decode
- Tiled VAE implementation planned to solve this
- Frame count follows standard Wan limits (81 frames native)

> "you can make it higher, but it will oom in the end on the vae decode if you significantly increase it" — intervitens, March 6, 2025

> "tiled VAE solves this, I'll implement it some time" — intervitens, March 6, 2025

### Video Extension

**Current status:** No sliding window implementation yet.

**Workaround:** Generate video → I2V from last frame → concatenate videos.

> "I think it breaks without tricks, like sliding window, that I haven't implemented yet. But you can gen a video -> i2v from the last frame -> concat the videos" — intervitens, March 6, 2025

## Comparison to Single-GPU

| Aspect | Single GPU | Multi-GPU (4x) |
|--------|------------|----------------|
| **VRAM per GPU** | 24+ GB required | 12+ GB sufficient |
| **Speed (720p I2V)** | ~15 min (3090) | ~3 min (4x 3090 Ti) |
| **Speed with TeaCache** | ~10 min (estimated) | ~10 min (threshold 0.18), ~7.5 min (threshold 0.3) |
| **Setup complexity** | Simple | Moderate |
| **Cost** | 1 high-end GPU | 4 mid-range GPUs |
| **Flexibility** | Limited by single GPU | Can scale to larger models |
| **Power consumption** | ~300-450W | ~1600W (4x 400W) |
| **Cooling requirements** | Standard | Significant |

## Future Development

**Planned features:**
- Server mode to avoid reloading model
- Better Hunyuan I2V support
- Automatic optimization tuning
- Support for more GPUs (8+)
- Tiled VAE for higher resolutions
- Sliding window for video extension
- Optimized ring_size and ulysses_size configurations
- **TeaCache integration** (COMPLETED March 11, 2025)
- **Torch.compile integration** (IN PROGRESS March 11, 2025)

## Troubleshooting

| Problem | Solution |
|---------|----------|
| OOM during generation | Increase `--dit_fsdp_offload`, reduce resolution |
| Slow T5 encoding | Use `--t5_fsdp` instead of `--t5_cpu` |
| Uneven GPU load | Check `CUDA_VISIBLE_DEVICES`, clear GPU memory |
| Black output on I2V | Use `--attn_impl sage_attn_fp16` |
| Long initial delay | Normal; T5 encoding and model loading take time |
| Different results each run | Set `--base_seed` for reproducibility |
| GPUs not at max TDP | Check for bottlenecks (CPU, interconnect, VRAM) |
| Port conflict | Use `--master_port` to specify different port |
| 8 GPU setup slow | Experiment with `--ring_size` and `--ulysses_size` values |
| Higher resolution OOM | Wait for tiled VAE implementation |
| TeaCache not working | Ensure latest version of multi-GPU script; use threshold 0.18-0.3 |
| TeaCache artifacts | Lower threshold to 0.18 for better quality |
| Torch.compile not working | Work in progress; add `use_orig_params=True` to FSDP call |

## See Also

- [[wan-2.1]] — Base model for multi-GPU generation
- [[sageattention]] — Attention optimization used in multi-GPU
- [[fp16-accumulate]] — Required optimization for multi-GPU
- [[teacache]] — Speed optimization now compatible with multi-GPU
- [[torch-compile]] — Speed optimization being integrated with multi-GPU
- [[hardware]] — Hardware requirements and recommendations

## External Resources

- [Wan Multi-GPU Repository](https://github.com/intervitens/Wan-MultiGPU)
- [FSDP Documentation](https://pytorch.org/docs/stable/fsdp.html)
- [SageAttention GitHub](https://github.com/thu-ml/SageAttention)
