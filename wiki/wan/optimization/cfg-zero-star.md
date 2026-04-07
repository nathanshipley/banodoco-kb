---
title: CFG Zero Star
aliases: [cfg-zero-star, zero-star, cfg-zero, zero-init]
last_updated: 2025-03-26
---

# CFG Zero Star

CFG Zero Star is a novel CFG (Classifier-Free Guidance) optimization technique that improves output quality by modifying how conditional and unconditional predictions are combined. Released as a research paper and implemented for Wan on March 25, 2025.

> "So crazy that zero init even works...would never have guessed" — Kijai, March 26, 2025

---

## Overview

CFG Zero Star modifies the standard CFG calculation to improve quality without additional compute cost. It consists of two components:

1. **Alpha scaling** — Dynamically scales the unconditional prediction based on its alignment with the conditional prediction
2. **Zero initialization** (optional) — Sets the first N steps to zero output

**Key advantage:** Improves quality with minimal speed impact, and can actually be slightly faster than standard CFG.

---

## How It Works

### Standard CFG

```
noise_pred = uncond + cfg_scale * (cond - uncond)
```

### CFG Zero Star

```
alpha = dot_product(cond, uncond) / (squared_norm(uncond) + epsilon)
noise_pred = uncond * alpha + cfg_scale * (cond - uncond * alpha)
```

**Alpha calculation:**
- Computes alignment between conditional and unconditional predictions
- Scales unconditional prediction to better match conditional
- Reduces artifacts and improves coherence

### Zero Initialization

Optionally, the first N steps can be set to zero output:

```python
if (current_step <= zero_steps) and use_zero_init:
    return cond * 0
```

> "nothing on those steps, literally multiply by zero" — Kijai, March 26, 2025

**Why this works:** Unknown, but empirically effective for T2V.

---

## Implementation

### Kijai Wrapper

**Status:** Implemented March 25, 2025

**Node:** `CFG Zero Star (KJ)`

**Parameters:**

| Parameter | Default | Notes |
|-----------|---------|-------|
| **zero_star_steps** | 0 | Number of steps to zero (if zero_init enabled) |
| **use_zero_init** | false | Enable zero initialization |

**Important:** Renamed from `CFG Zero Star` to `CFG Zero Star (KJ)` on March 26 to avoid conflict with comfy's implementation.

### Native ComfyUI (comfy)

**Status:** Implemented March 26, 2025

**Node:** `CFG Zero Star`

**Key difference:** comfy's implementation is a post-CFG patch, making it more compatible with other CFG modifications (like SLG). It does NOT include zero initialization.

> "this node is cfg sampling function patch so it probably conflicts with other cfg patches, while his node is post cfg patch and more compatible with those, but it (currently) doesn't have the zero init" — Kijai, March 26, 2025

**Commit:** https://github.com/comfyanonymous/ComfyUI/commit/84fdaf7b0ef4d030723bc3b350282dc6c92743f6

---

## Settings

### Recommended Values

**For T2V:**
- zero_star_steps: 0-1 (if using zero_init)
- use_zero_init: false (default)

**For I2V:**
- zero_star_steps: N/A
- use_zero_init: **false** (critical — breaks I2V if enabled)

> "the zero init does ruin Wan I2V completely though, that's for sure" — Kijai, March 26, 2025

### Zero Steps Behavior

**Important:** Zero steps are 0-indexed.

- `zero_star_steps = 0` → Steps 0 is zeroed (1 step)
- `zero_star_steps = 1` → Steps 0-1 are zeroed (2 steps)
- `zero_star_steps = 2` → Steps 0-2 are zeroed (3 steps)

> "It's actually 3 steps zeroed since it starts from 0" — Kijai, March 26, 2025

**Recommendation:** Use 0-1 for most cases. Higher values may be too aggressive.

---

## Quality Impact

### Improvements Reported

**General:**
- Fixes hand stability
- Reduces artifacts
- Improves fine details
- Better coherence
- More natural results

> "new cfg zero is insane" — Juampab12, March 25, 2025

> "fixes so much problems from previous gens" — Juampab12, March 25, 2025

> "it stabilizes the hands tho" — Cseti, March 26, 2025

**With LoRAs:**

> "made one lora of mine so much better instantly" — Juampab12, March 25, 2025

**Comparison testing (Cseti, March 26):**

Three versions tested:
1. Baseline (no optimizations)
2. Zero Star + Enhance-a-Video
3. Zero Star + Enhance-a-Video + SLG

Result: "movement fixed" with substantial quality differences between all three.

### Step Reduction

> "i had 35 because its the lowest that looked good, now lowered to 25 and it looks even better than before" — Juampab12, March 25, 2025

Zero Star allows reducing step count while maintaining or improving quality.

### CFG Reduction

> "i disabled stg and half cfg and feta. could even lower steps" — Juampab12, March 25, 2025

Zero Star enables lower CFG values while maintaining quality, similar to [[slg-uncond]].

---

## Compatibility

### Works With

- **Wan 2.1 T2V** (all sizes) ✓
- **Wan 2.1 I2V** (with zero_init disabled) ✓
- **Wan Fun models** ✓
- **SD 3.5** ✓
- **TeaCache** ✓
- **Enhance-a-Video** ✓
- **SLG** ✓ (with comfy's implementation)
- **Torch.compile** ✓

### Does NOT Work With

- **Flux** (no CFG) ✗
- **Wan I2V with zero_init enabled** ✗

### Sampler Compatibility

**Confirmed working:**
- euler / normal
- dpmpp_2m / beta
- uni_pc
- res_2m (Clownshark's sampler)

**May not work:**
- Some samplers may be incompatible
- Test with your specific sampler

> "It's very possible and likely the zero star doesn't work with all samplers yea" — Kijai, March 25, 2025

---

## Performance Impact

### Speed

**Slightly faster than baseline:**

> "this method also increases the inference speed so it's kinda win-win" — Kijai, March 16, 2025 (referring to SLG uncond, similar principle)

Zero Star adds minimal computation (dot product and scaling), and zero_init actually skips steps entirely.

**With zero_init enabled:**
- Skips model prediction for zeroed steps
- Measurable speedup (few seconds per generation)

**Without zero_init:**
- Minimal overhead from alpha calculation
- Effectively same speed as baseline

### VRAM

**No additional VRAM required.**

Zero Star operates on existing tensors without allocating new memory.

---

## Shift Behavior

**Important:** Shift values behave differently with Zero Star.

> "only thing i've found is that shift values kind of behave the opposite of how they normally do" — Faust-SiN, March 25, 2025

Lower shift values may work better with Zero Star than they do with standard CFG. Experimentation recommended.

---

## Known Issues

### I2V with Zero Init

**Problem:** Enabling zero_init completely breaks I2V output.

**Symptoms:**
- Ghosting
- Severe artifacts
- Unusable output

**Solution:** Always disable zero_init for I2V.

> "the zero init does ruin Wan I2V completely though, that's for sure" — Kijai, March 26, 2025

### Black Outputs

**Problem:** Some users report black outputs when using Zero Star.

**Possible causes:**
- Incorrect sampler
- Incompatible settings
- Model variant issues

**Solutions:**
- Try euler/normal sampler
- Disable zero_init
- Check other settings (denoise, CFG, etc.)

### Pale/Faded Outputs

**Problem:** Some users report pale green-faded outputs.

**Possible causes:**
- Sampler incompatibility
- Scheduler incompatibility

**Solution:** Try different sampler/scheduler combinations.

> "sampler and scheduler seems to matter too" — Miku, March 25, 2025

### Prompt Following

**Observation:** Some users feel Zero Star "loses the prompt a bit."

> "i feel zero star kinda loses the prompt a bit" — TK_999, March 26, 2025

This may be seed-dependent or related to specific settings. More testing needed.

---

## Combining with Other Optimizations

### Zero Star + SLG

**Status:** Compatible (with comfy's implementation)

> "zerostar + slg" — Cseti, March 26, 2025 [🔥x2]

Comfy's post-CFG implementation stacks cleanly with SLG.

**Kijai's implementation:** May conflict with SLG since both patch CFG sampling function.

### Zero Star + Enhance-a-Video

**Status:** Compatible

> "zero-star + enhance-a-video in the middle, and zero-star + enhance-a-video + SLG at the bottom" — Cseti, March 26, 2025

Excellent results reported with this combination.

### Zero Star + TeaCache

**Status:** Compatible

> "still Inp 1.3B, same settings but with Zero Star" — JmySff, March 26, 2025

Works well together for cumulative speedup.

### Zero Star + Torch.compile

**Status:** Compatible

**Patch order:** Zero Star → other patches → Torch.compile (last)

---

## Use Cases

### Quality Improvement

Primary use case: Improve output quality without speed penalty.

**Best for:**
- Hand stability
- Artifact reduction
- Fine detail preservation
- Overall coherence

### Step Reduction

Secondary benefit: Reduce step count while maintaining quality.

**Example:**
- Previous: 35 steps for acceptable quality
- With Zero Star: 25 steps for better quality

### CFG Reduction

Tertiary benefit: Lower CFG values while maintaining quality.

**Example:**
- Previous: CFG 6 required
- With Zero Star: CFG 4-5 sufficient

### LoRA Enhancement

> "made one lora of mine so much better instantly" — Juampab12, March 25, 2025

Zero Star appears particularly effective with LoRAs, improving their output quality.

---

## Comparison to Other Techniques

| Technique | Quality | Speed | Compatibility | Complexity |
|-----------|---------|-------|---------------|------------|
| **Zero Star** | High | Neutral/Faster | Good | Low |
| **SLG Uncond** | Medium | Neutral/Faster | Good | Low |
| **Enhance-a-Video** | Medium | Slower | Good | Low |
| **TeaCache** | Slight loss | 2x faster | Good | Medium |
| **Standard CFG** | Baseline | Baseline | Perfect | None |

---

## Research Paper

**Title:** CFG-Zero*

**Authors:** Weichen Fan et al.

**Repository:** https://github.com/WeichenFan/CFG-Zero-star

**Key contributions:**
- Alpha scaling for better CFG
- Zero initialization for improved quality
- Minimal computational overhead

**Note:** Authors plan to release ComfyUI implementation.

> "Seems the authors are also going to do a ComfyUI implementation... Hopefully more optimally than their demo code" — Screeb, March 26, 2025

---

## Implementation Details

### Original Implementation Issues

The original research code had inefficiencies:

> "Looking at their code, it really looks like they are just for whatever reason not doing this optimally at all (maybe for demonstrative purposes, or minimal change?)" — Screeb, March 26, 2025

Kijai's wrapper implementation is optimized:

> "updated the wrapper implementation to just skip the step, identical result and faster obviously" — Kijai, March 26, 2025

### Optimization

Kijai's optimization for zero_init:

```python
if (current_step_index <= zero_star_steps) and use_zero_init:
    return  # Skip step entirely
```

This avoids running the model prediction for zeroed steps, providing actual speedup.

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| Black output | Try euler/normal sampler; disable zero_init |
| Pale/faded output | Try different sampler/scheduler |
| I2V broken | Disable zero_init |
| Conflicts with SLG | Use comfy's implementation instead of Kijai's |
| No quality improvement | Try different zero_star_steps value; ensure zero_init is appropriate for your use case |
| Prompt following issues | Adjust CFG; try different seeds |

---

## See Also

- [[slg-uncond]] — Similar quality improvement technique
- [[enhance-a-video]] — Compatible optimization
- [[teacache]] — Compatible speedup
- [[samplers]] — Sampler compatibility
- [[wan-2.1]] — Base model

## External Resources

- [CFG-Zero* GitHub](https://github.com/WeichenFan/CFG-Zero-star)
- [CFG-Zero* Paper](https://arxiv.org/abs/[paper-id]) — (if available)
- [ComfyUI Commit](https://github.com/comfyanonymous/ComfyUI/commit/84fdaf7b0ef4d030723bc3b350282dc6c92743f6)
- [Reddit Discussion](https://www.reddit.com/r/StableDiffusion/comments/1jac3wm/dramatically_enhance_the_quality_of_wan_21_using/)
