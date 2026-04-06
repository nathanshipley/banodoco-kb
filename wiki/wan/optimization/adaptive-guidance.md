---
title: Adaptive Guidance
aliases: [adaptive-guidance, ag]
last_updated: 2025-03-03
---

# Adaptive Guidance

Adaptive Guidance is an automated CFG scheduling technique that provides speed improvements for Wan 2.1 by dynamically adjusting CFG values during generation, effectively setting CFG=1 for certain steps.

## Overview

Adaptive Guidance automatically determines which sampling steps benefit from classifier-free guidance and which don't, skipping CFG computation when it's not needed. This is similar to manual CFG scheduling but automated.

> "It's like automated cfg scheduling" — Kijai, March 3, 2025

## Installation

```bash
cd ComfyUI/custom_nodes
git clone https://github.com/asagi4/ComfyUI-Adaptive-Guidance
```

## Performance Impact

- **Speed improvement:** ~30% reported by some users
- **Quality impact:** Minimal to none — works "like a teacache but without losing quality"
- **Best for low-step workflows:** Particularly effective at 10 steps or fewer
- **Stacks with TeaCache:** Can be combined for additional speedup, though stability varies

> "for me, it works like a teacache but without losing quality, and i say for me cuz i like to use only 10 steps" — Miku, March 3, 2025

## How It Works

Adaptive Guidance skips CFG on steps where the guidance would have minimal impact, similar to how TeaCache skips steps with minimal latent changes. The key difference:

- **TeaCache:** Skips steps based on latent similarity
- **Adaptive Guidance:** Skips CFG computation based on guidance necessity
- **Combined:** Both skip different things, potentially stacking benefits

## Compatibility

**Works with:**
- Native ComfyUI workflows
- Wan 2.1 T2V and I2V
- Can be combined with TeaCache (with caveats)

**Does NOT work with:**
- Kijai wrapper (no built-in support as of March 2025)
- Some TeaCache configurations (see Known Issues)

**Note:** For wrapper users, Kijai mentioned looking into adding support but noted it may not make sense with TeaCache since they effectively do similar things.

## Known Issues

### TeaCache Compatibility

Adaptive Guidance can crash when combined with TeaCache:

- **Error:** `RuntimeError: output with shape [1, 12150, 1536] doesn't match the broadcast shape [2, 12150, 1536]`
- **Cause:** AG skips CFG on some steps, changing batch size, which TeaCache doesn't handle
- **When it crashes:** Typically at the step where AG kicks in (e.g., step 12/20)
- **Workaround:** Use one or the other, not both

Some users report it works fine together, others get consistent crashes. The issue appears related to how ComfyUI handles batched CFG with the 1.3B model.

### Model-Specific Behavior

- **1.3B model:** More prone to TeaCache+AG crashes due to batched CFG handling
- **14B model:** May work better, but not extensively tested

## Usage in Native ComfyUI

Adaptive Guidance is designed for native ComfyUI workflows. It requires using the `SamplerCustomAdvanced` node instead of the standard `KSampler`.

**Basic setup:**
1. Replace `KSampler` with `SamplerCustomAdvanced`
2. Add Adaptive Guidance node to the workflow
3. Connect to the sampler's guider input

**Note:** Some users reported that latent preview doesn't work with `SamplerCustomAdvanced` by default, but enabling preview in settings may fix this.

## Comparison to Alternatives

| Method | Speed Gain | Quality Impact | Compatibility | Complexity |
|--------|-----------|----------------|---------------|------------|
| **Adaptive Guidance** | ~30% | Minimal | Native only | Low |
| **TeaCache** | 1.5-2x | Slight | Both | Low |
| **Manual CFG scheduling** | Varies | Varies | Both | High |
| **Dynamic Thresholding** | Varies | Can improve | Both | Medium |

## Alternative: Dynamic Thresholding

For similar functionality with additional features, consider Dynamic Thresholding:

- Can mimic higher CFG values
- More control over CFG behavior
- Works with both native and wrapper
- Repository: https://github.com/mcmonkeyprojects/sd-dynamic-thresholding

> "took me a minute to remember the name, Dynamic Thresholding, it's similar to that Adaptive Guidance mode for native, but also lets you mimic higher CFG" — TK_999, March 3, 2025

## See Also

- [[teacache]] — Complementary optimization that can be combined (with caveats)
- [[samplers]] — Sampler and scheduler choices that affect performance
- [[speed]] — Other speed optimization techniques
- [[wan-2.1]] — Base model that benefits from Adaptive Guidance

## External Resources

- [ComfyUI-Adaptive-Guidance Repository](https://github.com/asagi4/ComfyUI-Adaptive-Guidance)
- [Reddit Discussion](https://www.reddit.com/r/StableDiffusion/comments/1j2an5p/get_a_30_speed_improvement_on_wan_with_the/)
- [Dynamic Thresholding](https://github.com/mcmonkeyprojects/sd-dynamic-thresholding)
