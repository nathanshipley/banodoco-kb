---
title: Samplers and Schedulers
aliases: [samplers, sampler, scheduler, schedulers]
last_updated: 2025-03-03
---

# Samplers and Schedulers

Sampler and scheduler choice significantly affects Wan 2.1 output quality, with some combinations producing noticeably better results than others.

## Recommended Samplers

### UniPC (uni_pc)

**The community-discovered winner for Wan 2.1.**

- **Default in official Wan code** — the Wan team uses UniPC
- **Significantly better texture quality** than dpm++ variants
- **Less stippling/dotting artifacts** on fur, hair, and fine textures
- **Sharper detail** especially visible in close-ups
- **Clearest hair rendering** compared to other samplers

> "uuuff... why haven't I been using uni_pc?" — Kijai, March 1, 2025

> "I've had better luck with unipc as well." — toyxyz, March 1, 2025

> "try unipc_bh2 as sampler, at least with the wrapper it's far better" — Kijai, March 3, 2025

**Settings:**
- Works well at 20-30 steps
- Pairs with simple or beta scheduler
- Default is `uni_pc_bh2` (recommended for >10 steps)
- `uni_pc_bh1` is recommended for <10 steps

### DPM++ Variants

**Previously common but now considered inferior to UniPC for Wan.**

- `dpmpp_2m` — Slightly better for detail than base dpm++
- `dpmpp_2m_sde` — Can be good but slower
- `dpmpp_sde` — More camera movement than dpm++

All dpm++ variants show more stippling artifacts and "pixel fog" compared to UniPC, especially on 1.3B model.

### Euler

**Reliable fallback, especially for troubleshooting.**

- Works well at 20 steps
- Some users reported better results with Euler than UniPC at 20-30 steps
- Less prone to weird artifacts than some other samplers
- Works well for realistic people
- Pairs well with `normal` scheduler for some use cases

> "Even at 30 it's weird. Hm. Possibly something else messed up with my settings" — Screeb testing UniPC issues, March 1, 2025

### DEIS

**Alternative sampler with specific strengths.**

- `deis_2m` was "surprisingly good" in some tests — TK_999, March 3, 2025
- For I2V native workflows, some users reported `deis / sgm_uniform` as best combination

## Sampler Comparison

Visual quality comparison (Kijai, March 1, 2025):

**UniPC vs DPM++:**
- UniPC: Cleaner fur texture, less stippling, sharper beard detail
- DPM++: More "pixel fog" and dotting artifacts, especially on moving parts

**Effect on motion:**
- `dpmpp_sde` produces more camera movement than `dpmpp_2m`
- UniPC maintains good motion while improving texture quality

**Scheduler comparison (Wan 1.3B):**
- UniPC has the clearest hair rendering
- Differences between schedulers are subtle unless examined closely

## Schedulers

| Scheduler | Notes |
|-----------|-------|
| **simple** | Default, works well with most samplers. Recommended for UniPC |
| **beta** | Alternative default, similar to simple. Likely works well with UniPC |
| **normal** | Works with UniPC. Pairs well with Euler for some use cases |
| **beta57** | Used in some workflows |
| **flowmatch_distill** | For Lightning LoRA workflows |
| **linear_quadratic** | For new 2.2 LightX2V MoE. **Not recommended for UniPC** |
| **karras** | **Not recommended for UniPC** |
| **exponential** | **Not recommended for UniPC** |
| **sgm_uniform** | Works well for T2V in some cases. Recommended for I2V native with DEIS |

## Wrapper vs Native Differences

**Important:** The same sampler name may behave differently between Kijai wrapper and native ComfyUI.

- **UniPC in wrapper** uses `uni_pc_bh2` by default (recommended for >10 steps)
- **UniPC in native KSampler** defaults to `uni_pc_bh1` (recommended for <10 steps)
- Native has separate `uni_pc` and `uni_pc_bh2` options

For consistency with wrapper behavior, use `uni_pc_bh2` in native ComfyUI when running 20+ steps.

### Native vs Wrapper Quality Differences

Some users have reported consistent quality differences between wrapper and native implementations:

> "Native still can't do this picture proper, I don't get it" — Kijai, March 3, 2025

Specific issues observed in native:
- **Beard/texture artifacts:** Blocky patterns, "dotbeard" effect that doesn't appear in wrapper
- **Noise patterns:** Larger noise patterns that don't appear in wrapper
- **Perlin-like overlay:** Almost like a perlin noise overlay on certain textures

These differences persist across different samplers and settings, suggesting deeper implementation differences between wrapper and native.

## Model-Specific Notes

### Wan 2.1 T2V

- **UniPC is clearly superior** for texture quality
- Stippling artifacts more prevalent on 1.3B than 14B
- 14B T2V shows less "pixel fog" overall

### Wan 2.1 I2V

- **UniPC recommended** for I2V as well
- Some users reported wrapper produces better I2V quality than native regardless of sampler
- Texture artifacts (blocky patterns on beards, etc.) appear in native I2V with various samplers
- **Recommended for I2V native:** `deis / sgm_uniform` reported as best by some users

### Hunyuan Video

- UniPC and dpm++ are "very similar" for Hunyuan
- Wan-specific texture improvements with UniPC may not apply to other models

## TeaCache Compatibility

**Important:** TeaCache does not work with SDE samplers.

- **Compatible:** dpmpp_2m, uni_pc, euler, deis, etc.
- **Incompatible:** dpmpp_sde, dpmpp_2m_sde
- Error with SDE: `RuntimeError: Boolean value of Tensor with more than one value is ambiguous`

See [[teacache]] for more details.

## Troubleshooting

| Problem | Solution |
|---------|----------|
| Stippling/dotting on fur/hair | Switch to UniPC from dpm++ |
| Weird artifacts at 20-30 steps with UniPC | Try Euler as fallback; check other settings |
| Different results wrapper vs native | Check sampler variant (bh1 vs bh2 for UniPC) |
| Blocky texture on beards/skin (I2V native) | Use wrapper instead, or try different sampler |
| Pixelated hair | Try UniPC sampler |
| TeaCache error with sampler | Switch from SDE sampler to non-SDE (dpmpp_2m, uni_pc, euler) |
| "Dotbeard" effect in native | Try wrapper instead; native implementation has known texture issues |
| Poor I2V quality in native | Try deis/sgm_uniform combination, or use wrapper |

## See Also

- [[wan-2.1]] — Base model these samplers are tested with
- [[speed]] — Speed LoRAs that affect sampler choice
- [[quantization]] — Precision formats that interact with samplers
- [[teacache]] — Sampler compatibility with TeaCache
