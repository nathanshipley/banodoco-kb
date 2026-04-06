---
title: Torch Compile
aliases: [torch-compile, torch.compile, compile]
last_updated: 2025-03-04
---

# Torch Compile

Torch compile is a PyTorch optimization that compiles the model's computation graph for faster execution. It provides significant speed improvements for Wan 2.1 and stacks with other optimizations.

## Performance Impact

- **Speed gain:** ~30% on 4090 (2.94 s/it with compile vs 4.00 s/it without, at 640x480x33f)
- **Typical speedup:** 10-30% depending on configuration
- Stacks with SageAttention and fp16 accumulate
- First run takes several minutes to compile; subsequent runs reuse the compiled graph
- Reduces VRAM peaks in some cases

> "normally it's about 10% to 30% speed up, even 2%, so not always super useful" — for1096, March 4, 2025

## Compatibility

**Works with:**
- Wan 2.1 T2V (all sizes)
- Wan 2.1 I2V
- Native ComfyUI
- Kijai wrapper
- TeaCache (stacks for additional speedup)
- fp16 accumulation (stacks for additional speedup)
- SageAttention (stacks for additional speedup)

**May not work with:**
- Some models (compatibility varies)
- Certain PyTorch versions (requires updating)

## Implementation

### Kijai Wrapper

Kijai provides a custom compile node that compiles only the transformer blocks rather than the whole model:

- **Faster to compile/recompile** than standard torch.compile
- All transformer blocks are identical, so compilation is more efficient
- Use the `PatchModelAddDownscale (Kohya Deep Shrink)` or similar compile nodes from Kijai

### Native ComfyUI

Use the standard torch compile node in native workflows.

**Important for TeaCache compatibility:**
- When using TeaCache with torch.compile in native, use **Kijai's compile node** instead of the standard one
- The standard compile node wraps the whole model, which can cause errors with TeaCache
- Kijai's node only compiles transformer blocks, avoiding the `'OptimizedModule' object has no attribute 'forward_orig'` error

## Compile Modes

**Inductor mode:**
- Most commonly used
- Typically provides 10-30% speedup
- Works with most setups

**CUDAGraphs mode:**
- May have compatibility issues
- Some users report it doesn't work
- Requires specific PyTorch versions

> "typically we use the inductor mode, i think many have issues with cuagraphs node. It could be that pytorch needs updating" — TK_999, March 4, 2025

## Known Issues

### TeaCache Compatibility Error

When using native TeaCache with standard torch.compile:

```
KSampler
'OptimizedModule' object has no attribute 'forward_orig'
```

**Solution:** Use Kijai's compile node instead of the standard torch.compile node. It doesn't wrap the whole model and avoids this error.

### First Run Compilation Time

- First generation takes several minutes to compile
- Subsequent generations reuse the compiled graph and are much faster
- This is expected behavior

> "it compiles the model on the fly so that it generates much faster" — TK_999, March 4, 2025

### Platform Differences

- **Linux may use less VRAM than Windows** with torch compile
- torch.compile on Windows was reported as inconsistent in some torch versions

### Model Compatibility

- Not all models are compatible with torch.compile
- Some models may produce errors like `cannot assign 'comfy.ldm.wan.model.WanModel.forward' as child module 'diffusion_model'`
- This error is typically not related to compilation itself but to model loading

> "'comfy.ldm.wan.model.WanModel.forward' as child module 'diffusion_model' doesn't look like it is relevant to compilation" — for1096, March 4, 2025

### PyTorch Version Requirements

- Requires recent PyTorch version for best compatibility
- Some users report needing PyTorch 2.7.0+ for certain features
- Version `2.7.0.dev20250127+cu126` reported as working by some users

### GPU Compatibility

**3090 Issues:**
- fp8_e4m3fn compilation does not work on 3090 (Ada+ only)
- fp8_e5m2 compilation works on 3090
- Use fp16_fast on 3090 instead of fp8_fast

> "fp8_e4m3fn compilation in general doesn't work on 3090, fp8_e5m2 does" — Kijai, March 4, 2025

## Troubleshooting

| Problem | Solution |
|---------|----------|
| Compilation doesn't work | Update PyTorch to latest nightly; try inductor mode instead of CUDAGraphs |
| First run very slow | Expected — compilation happens on first run, subsequent runs are faster |
| Error with TeaCache | Use Kijai's compile node instead of standard torch.compile |
| Model loading error | May not be compilation-related; check model compatibility |
| Inductor not working | Update PyTorch; some models may not be compatible |
| 3090 compilation fails | Use fp8_e5m2 instead of fp8_e4m3fn; use fp16_fast instead of fp8_fast |
| "file already exists" error | Windows cache file bug; update to PyTorch 2.6.0+ |

## Performance Stack

For maximum performance, combine torch.compile with:

- [[fp16-accumulate]] — ~20-30% speedup, stacks with compile
- [[sageattention]] — ~25% speedup alone, nearly 2x with fp16 accumulate and compile
- [[teacache]] — ~2x speedup, stacks with compile (use Kijai's compile node)

Achievable combined speedup: **~2-3x faster** than baseline with all optimizations

## See Also

- [[wan-2.1]] — Base model that benefits from torch.compile
- [[fp16-accumulate]] — Stackable optimization
- [[sageattention]] — Stackable optimization
- [[teacache]] — Stackable optimization (requires Kijai's compile node)
- [[speed]] — Other speed optimization techniques
