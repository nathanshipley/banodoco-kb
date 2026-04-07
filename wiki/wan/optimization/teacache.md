---
title: TeaCache
aliases: [teacache, tea-cache, naive-teacache]
last_updated: 2025-03-09
---

# TeaCache

TeaCache is a latent-caching optimization that skips redundant diffusion steps by detecting when model outputs are similar enough to cached values. Originally developed by Alibaba's ali-vilab team (the same company behind Wan), it provides dramatic speed improvements with minimal quality loss.

Kijai implemented a "naive" version of TeaCache for Wan 2.1 on March 1, 2025, achieving nearly 2x speedup without the full polynomial fitting approach used in the original paper. A native ComfyUI implementation was also released on March 2, 2025.

**Major Update (March 5, 2025):** Kijai integrated the official coefficient calculations from the TeaCache team, making the implementation more accurate and allowing for higher threshold values with better quality preservation.

**Major Update (March 8, 2025):** Kijai updated the TeaCache node documentation to reflect significantly different optimal values for 1.3B vs 14B models when using coefficients.

> "3 mins 32 secs vs 1min 49 secs" — Kijai demonstrating TeaCache speedup, Discord #wan_chatter, March 1, 2025

> "I have exceeded my own expectations" — Kijai, March 1, 2025

---

## Performance Impact

**Wrapper implementation (Kijai):**
- **~2x speedup typical** — 212 seconds → 109 seconds, 53 seconds → 28 seconds
- **Up to 3.3x speedup** — 1 hour → 18 minutes for 1280x720x81 at 50 steps (reported by Juampab12)
- **100% speedup reported** for T2V workflows (slmonker, March 2, 2025)
- **Minimal quality degradation** — differences are subtle in most cases
- **VRAM overhead:** +12-13% over baseline

**With coefficients enabled (March 5, 2025):**
- **Better quality at same speed** — coefficients allow higher threshold values while maintaining quality
- **Can start from step 0** — no longer requires skipping early steps
- **More precise skipping** — skips the "right" steps in a smarter manner
- **28 minutes for 312 frames** at 960x544, 30 steps, GGUF Q8 on RTX 4090 (JmySff)
- **169 frames in 2 minutes** with context windows, 4.281 GB VRAM used (Kijai, March 5, 2025)
- **24 minutes for 324 frames** at 960x544 I2V 480p (JmySff, March 9, 2025)

**Native implementation:**
- Initial testing shows promise but requires proper threshold tuning
- Default threshold (0.15) is too high; 0.05 or lower recommended
- Quality can be "meh" at aggressive settings

**Benchmark examples:**
- 832x480x81, 30 steps: 212s → 109s (threshold 0.04)
- 832x480x81, 30 steps: 53s → 28s (threshold 0.04)
- 1280x720x81, 50 steps: ~1 hour → 18 minutes (threshold 0.04)
- 720p, 50 steps: 276s → 114s (threshold 0.0, start_step 0)
- 81 frame I2V on 3080: 5 minutes with TeaCache (garbus, March 2, 2025)
- 480p, 61 frames, 20 steps: 2 min → 1.5 min (N0NSens, March 2, 2025)
- 720p, 10 steps: 1296s → ~90s (N0NSens, March 2, 2025)
- 20 samples: 240s → 167s with TeaCache (David Snow, March 2, 2025)
- 60 samples: 660s → 227s with TeaCache (David Snow, March 2, 2025)
- 312 frames, 960x544, 30 steps: 28 minutes (JmySff, March 5, 2025)
- 169 frames with context windows: 2 minutes, 4.281 GB VRAM (Kijai, March 5, 2025)
- 324 frames, 960x544, I2V 480p, 25 steps: 24 minutes 12 seconds (JmySff, March 9, 2025)

> "more steps u run, more benefit u get" — slmonker, March 2, 2025

> "Basically, you can generate a video with 60 samples (using teacache defaults) faster than you can generate one with 20 samples without teacache." — David Snow, March 2, 2025

---

## How It Works

### The Naive Implementation

Kijai's implementation calculates the L1 distance between:
- **Time embeddings** (input to the model)
- **Model output** (after all transformer blocks)

When the relative distance falls below a threshold, the step is skipped and the cached output is reused.

**Key difference from the paper:** The original TeaCache uses polynomial fitting to calculate scaling coefficients that align the time embed and model output curves. Kijai's "naive" implementation skips this step because the curves for Wan 2.1 are already very close:

> "I plotted the difference like in the paper... then you're supposed to calculate scaling values to make them match better which I could NOT figure out, so I didn't do that. However as they are so close already, unlike the other models apparently, I thought to just directly use the difference without scaling." — Kijai, March 1, 2025

This suggests Wan 2.1 may be inherently easier to cache than other video models.

### Coefficient Update (March 5, 2025)

On March 5, 2025, the TeaCache team released official coefficient calculations. Kijai integrated these into the wrapper, making the implementation more accurate:

> "made it optional so can test and compare" — Kijai, March 5, 2025

> "can't compare with same values of course, this is less aggressive" — Kijai, March 5, 2025

The coefficients make TeaCache:
- **More precise** — skips steps more intelligently
- **Less aggressive at same threshold** — requires higher threshold values to match previous skip rates
- **Better quality** — "the quality is brilliant with the coefficients" (DevouredBeef)
- **Safer at step 0** — can potentially start from step 0 without artifacts

### Model-Specific Values (March 8, 2025)

Kijai updated the TeaCache node documentation to reflect that **1.3B and 14B models require very different threshold values** when using coefficients:

> "I did not actually realise the TeaCache values for 1.3B are so different with coefficients... updated my node to have better docs to reflect all that" — Kijai, March 8, 2025

**Reported working values:**
- **1.3B with coefficients:** threshold 0.250, start_step 1, end_step -1 (Organoids, March 8, 2025)
- **14B with coefficients:** threshold 0.25-0.35 (community consensus, March 5, 2025)

### Conditional vs Unconditional

The implementation caches conditional and unconditional passes separately. Kijai noted they seem to trigger at the same steps, so batching them might not have been necessary, but separate caching was chosen to avoid higher memory usage.

**Note on skip reporting (March 5, 2025):** With coefficients enabled, the skip count reporting may be inaccurate. The reported number only shows one of the cond/uncond passes, and they may now skip independently. Use generation time as the primary metric for comparison.

---

## Settings

### Wrapper (Kijai)

| Parameter | Recommended Value | Notes |
|-----------|------------------|-------|
| **threshold** | **0.04** (without coefficients), **0.25-0.35** (with coefficients, 14B), **0.250** (with coefficients, 1.3B) | Lower = more aggressive caching, higher speedup, more quality loss. With coefficients, much higher values are safe. **Model-specific values critical.** |
| **start_step** | **8** (without coefficients), **0-2** (with coefficients) | Skip early noisy steps. With coefficients, may not be needed at all |
| **use_coefficients** | **true** | Enable official coefficient calculations (recommended as of March 5, 2025) |
| **Steps (total)** | 20-50 | TeaCache works across all step counts; more steps = more benefit |

**Threshold guidance (without coefficients):**
- **0.04** — Balanced default (Kijai's recommendation)
- **0.03** — More aggressive, good quality with 50% time savings (Juampab12, March 2, 2025)
- **0.0** — Maximum speedup (276s → 114s reported), noticeable quality changes
- **Higher values** — More conservative, less speedup, better quality

**Threshold guidance (with coefficients enabled):**
- **0.2** — Starting point for testing
- **0.25-0.35** — Recommended range for 14B models (DevouredBeef, March 5, 2025)
- **0.250** — Reported working well for 1.3B (Organoids, March 8, 2025)
- **0.3** — Good balance of speed and quality at 50 steps for 14B (community consensus, March 5, 2025)
- **Higher values possible** — Coefficients allow much higher thresholds while maintaining quality

**Start step guidance (without coefficients):**
- **0** — Cache from the beginning (fastest but can introduce artifacts)
- **5-6** — Early start for maximum speedup (N0NSens, March 2, 2025)
- **8** — Skip the noisy early steps (recommended default)
- **10-12** — More conservative for 50-step workflows (seitanism#0, March 2, 2025)
- **Higher values** — More conservative, slower but stabler

**Start step guidance (with coefficients enabled):**
- **0** — May work without artifacts now (Kijai noted it "seems to never activate at start like it shouldn't")
- **1** — Reported working well for 1.3B (Organoids, March 8, 2025)
- **2** — Conservative choice for testing (DevouredBeef used this)
- **Higher values** — Potentially unnecessary with coefficients

The node reports at the end how many steps were skipped:
```
TeaCache skipped 15 cond steps, 15 uncond steps
```

**Note:** For 50-step workflows, starting later (step 10-12) may be necessary to avoid artifacts. The optimal start_step value scales with total step count.

**Step count dependency:** The default settings (start_step 8, threshold 0.04) are optimized for 30 steps. For 20-step workflows, you may need to adjust start_step lower (e.g., 5-6). For 50-step workflows, you may need to increase start_step (e.g., 10-12).

**Important update (March 5, 2025):** After the coefficient update, the default threshold in example workflows was changed from 0.04 to 0.03, but this may be a decimal error. With coefficients enabled, the recommended threshold is **0.3** (not 0.03). Users reported TeaCache not triggering with 0.03 threshold after the update.

**Critical: Model-specific values (March 8, 2025):** The 1.3B and 14B models require **significantly different threshold values** when using coefficients. Using 14B values on 1.3B (or vice versa) will result in poor performance.

### Native ComfyUI

Kijai released an initial native TeaCache implementation on March 2, 2025:
- Repository: https://github.com/kijai/ComfyUI-TeaCache
- Missing start_step parameter in initial release
- Requires threshold tuning for good results

**Threshold guidance for native:**
- **0.15** — Default, too high (Kijai confirmed)
- **0.05** — Maximum recommended (Kijai)
- **Lower than 0.05** — More aggressive, test carefully

> "Oh the 0.15 is definitely too much" — Kijai, March 2, 2025

> "Wouldn't go higher than 0.05" — Kijai, March 2, 2025

**Quality comparison (JmySff, March 2, 2025):**
- Default (0.15): Faster but quality is "meh"
- Low (0.05): Better quality, still good speedup

---

## Quality Impact

**General observations:**
- **Close-ups:** Differences least visible
- **Motion:** Slight stability reduction possible at aggressive settings
- **Details:** Minor loss of fine texture at lower thresholds
- **Hands/faces:** User seitanism#0 reported "his lower hand actually looks better with teacache" in one comparison
- **Composition and motion preserved:** TeaCache doesn't generally change motion and composition, making it useful for previewing
- **Sometimes better results:** Kijai noted one I2V generation "looks better with tea" — suggesting TeaCache can occasionally improve results, possibly by reducing overfitting to noise

**With coefficients enabled (March 5, 2025):**
- **"Quality is brilliant"** — DevouredBeef after testing
- **Less aggressive at same threshold** — requires higher threshold to match previous skip rates
- **Better quality preservation** — can use higher thresholds without quality loss
- **Smarter skipping** — "just skipping the right steps, in a smarter manner" (DevouredBeef)

**Comparison (same seed, 30 steps, threshold 0.04, start_step 8):**
- Minimal visible differences in most cases
- Slight eye movement artifact noted in one test
- Overall quality "doesn't look noticeably bad" — seitanism#0

**Aggressive settings (threshold 0.0, start_step 0):**
- "that actually changes the vid" — seitanism#0
- More noticeable differences
- Still usable for many workflows

**Quality degradation with too many skipped steps:**
- If threshold is too aggressive for the step count, noise may not be fully removed
- Flickering circles or noise artifacts indicate too many steps were skipped
- Increase threshold or start_step to resolve

> "just too many steps skipped so the noise isn't removed fully" — Kijai, March 2, 2025

**Quality vs Speed Trade-offs (March 9, 2025):**

Community member spacepxl noted that TeaCache and other optimizations can significantly hurt quality:

> "teacache in particular is really bad for quality, sage attn is probably ok" — spacepxl, March 9, 2025

> "but high shift and low steps are deadly for quality" — spacepxl, March 9, 2025

> "eh, 1.3b at 50 steps easily beats the quality of most people's 'efficient' 14b workflows" — spacepxl, March 9, 2025

> "most of the optimizations people use hurt quality a lot" — spacepxl, March 9, 2025

spacepxl advocates for prioritizing quality over speed:

> "I would much rather wait twice as long for better quality" — spacepxl, March 9, 2025

> "these video generation times are not bad at all compared to cg rendering" — spacepxl, March 9, 2025

This represents a minority view in the community, as most users actively seek speed optimizations, but it's worth noting for quality-critical work.

---

## Compatibility

**Works with:**
- Wan 2.1 T2V (1.3B and 14B)
- Wan 2.1 I2V (14B) — confirmed working well by Kijai, March 2, 2025
- Kijai wrapper (as of March 1, 2025)
- Native ComfyUI (as of March 2, 2025)
- Stacks with [[fp16-accumulate]] and [[sageattention]]
- Stacks with [[torch-compile]]
- Works with CFG splitting (seitanism#0 confirmed, March 2, 2025)
- **FlowEdit** — Kijai confirmed TeaCache works with FlowEdit (March 5, 2025), though lower threshold values may be needed
- **Context windows** — Kijai implemented TeaCache support for context windows on March 5, 2025. Uses a complex caching system that caches every unique window (20+ caches). Requires lower threshold values than standard workflows.
- **Enhance-a-Video** — Compatible as of March 9, 2025. JmySff reported using TeaCache + Enhance-a-Video together successfully.

**Does NOT work with:**
- **Wan Feta Enhance** — JmySff reported no difference with/without when TeaCache is enabled (March 5, 2025). Kijai confirmed it needs to be a proper patch to work together.
- GGUF models (as of March 2, 2025)

**Previously incompatible but now working:**
- **Context windowing** — Was incompatible (produced noise artifacts) until March 5, 2025. Kijai implemented a solution that caches each unique context window separately. Requires lower threshold values.

**Unclear/untested:**
- LoRA workflows
- Long video generation without context windows
- Interaction with different samplers

---

## Known Issues

### Context Window Compatibility (RESOLVED March 5, 2025)

**Previous status:** TeaCache was **incompatible with context windowing** and produced noise artifacts when combined.

Kijai noted on March 2, 2025: "can't figure out teacache for context windows though, maybe not even possible..."

**Update (March 5, 2025):** Kijai successfully implemented TeaCache support for context windows. The implementation caches every unique window separately (20+ caches in some cases). Example output:

```
TeaCache skipped: 0 conditional steps
TeaCache skipped: 0 unconditional steps
TeaCache skipped: 11 prediction_2 steps
TeaCache skipped: 11 prediction_3 steps
[...continues for 40+ prediction windows...]
```

**Important notes for context window usage:**
- Requires **much lower threshold values** than standard workflows
- Each context window is cached separately to avoid mixing them up
- Successfully tested: 169 frames in 2 minutes with 4.281 GB VRAM
- Kijai confirmed: "it does work" and "main thing is to not mix them up like it was doing, leading to only noise"

### Threshold Changes After Update (March 5, 2025)

**Critical issue:** After the March 5, 2025 update that added coefficient support, many users reported TeaCache no longer triggering with previous settings.

**Cause:** The default threshold in example workflows was changed to 0.03, but with coefficients enabled, this value is too low. The recommended threshold with coefficients is **0.3** (10x higher).

**Solution:** Update threshold to 0.25-0.35 when using coefficients. The example workflow may have a decimal error (0.03 instead of 0.3).

> "It got changed with the update, when using the coefficients the value should be about 10x from when not using them" — Kijai, March 5, 2025

### Model-Specific Values (March 8, 2025)

**Critical:** The 1.3B and 14B models require **very different threshold values** when using coefficients. Using 14B values on 1.3B (or vice versa) will result in poor performance.

**Solution:** Always check the TeaCache node documentation for your specific model size. Kijai updated the node to include model-specific guidance.

### Early Step Noise

The input/output alignment is poor at the very start of sampling, which can throw off the cache calculation. This is why `start_step` exists — to skip the noisy early steps.

> "you can see the noise at start though where it doesn't match right? so added option to start it later to avoid having that distort the calculation" — Kijai, March 1, 2025

**With coefficients:** This may no longer be an issue. Kijai noted the cache "seems to never activate at start like it shouldn't" even with start_step=0.

### VRAM Spikes

TeaCache can cause VRAM spikes between samplers if not cleared. Turn off TeaCache between sampler stages or clear VRAM manually.

### VRAM Overhead with Block Swap

TeaCache adds approximately **12-13% VRAM overhead**. Users with limited VRAM who rely on block swap may need to increase the number of blocks swapped when enabling TeaCache.

> "aye that 12~13% increase seems to track, swapped enough blocks to set the baseline at 72% usage, rose to about 84%" — DevouredBeef, March 2, 2025

**Workaround:** If you experience OOM after enabling TeaCache, increase block swap by 5-10 blocks to compensate for the overhead.

### Step Count Dependency

The relative L1 distance plot shown by Kijai was for 30 steps. The optimal `start_step` value may need adjustment for different step counts (e.g., 20 steps vs 50 steps). More testing needed.

**Guidance from community testing (March 2, 2025):**
- **20 steps:** start_step 5-6 works well
- **30 steps:** start_step 8 (default)
- **50 steps:** start_step 10-12 may be needed to avoid artifacts

**With coefficients (March 5, 2025):** Start step may no longer be necessary at all.

### Aggressive Threshold Artifacts

If too many steps are skipped (threshold too low, start_step too early), artifacts may appear:
- Flickering circles
- Noise not fully removed
- Quality degradation

**Solution:** Increase threshold (try 0.05-0.08) or increase start_step.

### Native Implementation Limitations

The initial native TeaCache release (March 2, 2025) is missing the start_step parameter, which may limit its effectiveness. Kijai noted this in the release announcement.

### Skip Count Reporting Issues (March 5, 2025)

With coefficients enabled, the skip count reporting may be inaccurate:
- Reports only one of cond/uncond passes
- Actual skips may be higher than reported
- Cond and uncond may skip independently now
- **Use generation time as primary metric** for comparison

> "seems the teacache skipped log is a bit off, 0.04 was 8, and yet 0.2 is 2 (obviously in reality it's skipped a lot more)" — DevouredBeef, March 5, 2025

### Wan Feta Enhance Incompatibility

JmySff reported on March 5, 2025 that Wan Feta Enhance shows no difference when TeaCache is enabled, suggesting they may be incompatible. Kijai confirmed that "the enhance a video needs to be a proper patch to work together with it."

### FlowEdit Lower Threshold Requirement

Kijai noted on March 5, 2025 that "for FlowEdit I had to use lower values to not break it." When using TeaCache with FlowEdit, you may need to reduce the threshold below standard recommendations.

### Set/Get Node Incompatibility

User burgstall reported on March 6, 2025 that TeaCache arguments cannot be passed through "setnode/getnode" nodes. This appears to be a workflow limitation rather than a TeaCache bug.

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| No speedup | TeaCache didn't trigger; try lower threshold or lower start_step |
| "0 steps skipped" in log | TeaCache didn't trigger; try lower threshold or lower start_step |
| TeaCache not triggering after March 5 update | Increase threshold to 0.25-0.35 if using coefficients (default may be 0.03 instead of 0.3) |
| TeaCache not working on 1.3B after March 8 | Check model-specific threshold values; 1.3B requires different values than 14B |
| Noise artifacts / flickering circles | Increase start_step to 8 or higher; avoid threshold 0.0; may need start_step 10-12 for 50-step workflows |
| Quality degradation | Increase threshold (try 0.06-0.08); increase start_step |
| VRAM spikes between samplers | Turn off TeaCache between stages or add VRAM clear node |
| Artifacts with context windows (pre-March 5) | Context windows were incompatible until March 5, 2025 |
| Context windows producing noise (post-March 5) | Use much lower threshold values than standard workflows |
| Slower than expected | Check that node reports skipped steps; ensure PyTorch 2.7+ for fp16 accumulate |
| OOM after enabling TeaCache | Increase block swap by 5-10 blocks to compensate for 12-13% VRAM overhead |
| Too many steps skipped, noise remains | Increase threshold or start_step; threshold too aggressive for step count |
| Works poorly with I2V | Default settings are for 30 steps; adjust start_step for your step count (e.g., start_step 5-6 for 20 steps) |
| Native TeaCache not working well | Try wrapper implementation; native is missing start_step parameter in initial release |
| Much slower with coefficients | Increase threshold to 0.25-0.35 to match previous skip rates |
| Skip count seems wrong | With coefficients, reporting may be inaccurate; use generation time instead |
| Feta Enhance not working | May be incompatible with TeaCache; disable one or the other |
| FlowEdit breaking with TeaCache | Use lower threshold values than standard workflows |
| Set/Get nodes not working | Cannot pass TeaCache args through set/get nodes; connect directly |

---

## Performance Stack

For maximum performance, combine TeaCache with:

- [[fp16-accumulate]] — 10-30% speedup, stacks with TeaCache
- [[sageattention]] — ~25% speedup alone, stacks with TeaCache
- [[torch-compile]] — ~30% speedup, stacks with TeaCache
- **CFG splitting** — Works with TeaCache (seitanism#0 confirmed)
- **Enhance-a-Video** — Compatible with TeaCache (JmySff confirmed March 9, 2025)

**Achievable combined speedup:** ~3-4x faster than baseline in some cases

**Example (1280x720x81, 50 steps):**
- Baseline: ~1 hour
- With TeaCache + fp16 accumulate + SageAttention: ~18 minutes
- **3.3x speedup**

> "wrapper with fp8, fp16 accumulate, cfg splitting, teacache, sage, torchcompile...its ridiculous fast" — seitanism#0, March 2, 2025

**Example with Enhance-a-Video (March 9, 2025):**

JmySff reported combining TeaCache with the new Enhance-a-Video node:
- **Without Enhance-a-Video:** 6 minutes 35 seconds (25 steps, native, TeaCache)
- **With Enhance-a-Video:** 5 minutes 36 seconds (25 steps, native, TeaCache)
- Additional 1 minute speedup from Enhance-a-Video on top of TeaCache benefits

> "I don't really understand why i just gain 1 minute with Enhance a video but... i'm just happy" — JmySff, March 9, 2025

---

## Technical Details

### Relative L1 Distance Calculation

TeaCache calculates:
```
relative_distance = L1(time_embed, model_output) / norm_factor
```

When `relative_distance < threshold`, the step is skipped.

### Coefficient Calculations (March 5, 2025)

The official TeaCache team released coefficient calculations that make the distance comparison more accurate. These coefficients:
- Scale the time embed and model output curves to align them better
- Allow for higher threshold values while maintaining quality
- Make skipping more precise and intelligent
- Can be toggled on/off in the wrapper for comparison

### Caching Strategy

- **Separate cond/uncond caching** — avoids batching to save memory
- **Mid-sampling trigger** — typically activates in the middle of sampling, not at the start
- **Step reporting** — logs "TeaCache skipped X cond steps, Y uncond steps" at completion
- **Unequal skipping:** Conditional and unconditional passes may skip different numbers of steps (e.g., 16 cond, 29 uncond reported by seitanism#0)
- **With coefficients:** May skip cond/uncond independently, making reported counts less reliable
- **Context window caching (March 5, 2025):** Each unique context window is cached separately to avoid mixing, resulting in 20+ separate caches

### Why Wan 2.1 Works Well

The time embed and model output curves are naturally very close for Wan 2.1, unlike other models. This means the "naive" approach (no polynomial fitting) works surprisingly well.

### Polynomial Fitting (Future Improvement)

The original TeaCache paper uses polynomial fitting to calculate scaling coefficients. Community member Screeb suggested:

> "you just need to use `coefficients = np.polyfit(x, y, 4)` (or a higher order than 4 if that helps), where x and y are the raw input difference and output difference" — Screeb, March 2, 2025

Kijai attempted this but encountered SVD errors. This remains a potential future optimization for even better efficiency.

**Update (March 5, 2025):** The TeaCache team provided official coefficient calculations, which Kijai has now integrated.

---

## Preview Workflow

TeaCache is particularly useful for previewing:

> "another thing I like is that it doesn't generally change the motion and composition, so you can sort of preview. And just disable it and run again for high quality version" — Kijai, March 2, 2025

**Workflow:**
1. Enable TeaCache with aggressive settings (threshold 0.03-0.04 without coefficients, or 0.25-0.35 with coefficients, start_step 5-8)
2. Generate preview quickly to check composition and motion
3. Disable TeaCache and regenerate with same seed for final quality

---

## Timeline

| Date | Event |
|------|-------|
| **March 1, 2025** | Kijai implements "naive TeaCache" for Wan 2.1 wrapper |
| **March 1, 2025** | Initial benchmarks: 212s → 109s, 53s → 28s |
| **March 1, 2025** | Community testing begins; threshold 0.04 emerges as default |
| **March 2, 2025** | User reports 1 hour → 18 minutes speedup at 720p/50 steps |
| **March 2, 2025** | 12-13% VRAM overhead confirmed; block swap adjustment needed |
| **March 2, 2025** | CFG splitting confirmed compatible with TeaCache |
| **March 2, 2025** | Kijai releases initial native TeaCache implementation (missing start_step) |
| **March 2, 2025** | I2V compatibility confirmed; works well with proper settings |
| **March 2, 2025** | Context window incompatibility confirmed; Kijai notes it may not be possible to combine |
| **March 2, 2025** | Native implementation testing shows promise but requires threshold tuning |
| **March 5, 2025** | **TeaCache team releases official coefficient calculations** |
| **March 5, 2025** | Kijai integrates coefficients into wrapper; makes them optional for testing |
| **March 5, 2025** | Community testing shows coefficients allow higher thresholds (0.25-0.35) with better quality |
| **March 5, 2025** | FlowEdit compatibility confirmed (requires lower threshold values) |
| **March 5, 2025** | Wan Feta Enhance incompatibility discovered |
| **March 5, 2025** | Skip count reporting issues identified with coefficients enabled |
| **March 5, 2025** | **Context window support implemented** — caches each unique window separately |
| **March 5, 2025** | 169 frames in 2 minutes with context windows + TeaCache demonstrated |
| **March 6, 2025** | Set/Get node incompatibility reported |
| **March 8, 2025** | Kijai updates node documentation to reflect model-specific threshold values (1.3B vs 14B) |
| **March 9, 2025** | Enhance-a-Video compatibility confirmed; JmySff reports successful combination with TeaCache |
| **March 9, 2025** | 324 frames in 24 minutes with TeaCache + Enhance-a-Video (JmySff) |
| **March 9, 2025** | spacepxl advocates for quality-first approach, noting TeaCache "really bad for quality" |

---

## See Also

- [[wan-2.1]] — Base model that benefits from TeaCache
- [[fp16-accumulate]] — Stackable optimization
- [[sageattention]] — Stackable optimization
- [[torch-compile]] — Stackable optimization
- [[context-windows]] — Now compatible with TeaCache (as of March 5, 2025)
- [[speed]] — Overview of all speed optimizations
- [[adaptive-guidance]] — Alternative optimization (native only)
- [[flowedit]] — Compatible with TeaCache (requires lower threshold)
- [[enhance-a-video]] — Compatible with TeaCache (confirmed March 9, 2025)

## External Resources

- [TeaCache Original Paper/Repository](https://github.com/ali-vilab/TeaCache) — Alibaba's original implementation
- [TeaCache Official Coefficient Update](https://github.com/ali-vilab/TeaCache/commit/3cddb3689697ba949b689d81b3d508e68b68307d) — March 5, 2025 update
- [ComfyUI-WanVideoWrapper](https://github.com/kijai/ComfyUI-WanVideoWrapper) — Kijai's wrapper with TeaCache support
- [ComfyUI-TeaCache](https://github.com/kijai/ComfyUI-TeaCache) — Kijai's native TeaCache implementation
- [TeaCache GitHub Issue on Polynomial Fitting](https://github.com/ali-vilab/TeaCache/issues/20#issuecomment-2574564292) — Community discussion on coefficient calculation
