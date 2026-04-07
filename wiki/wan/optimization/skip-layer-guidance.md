---
title: Skip Layer Guidance (Uncond)
aliases: [slg-uncond, uncond-skip, negative-skip, slg, skip-layer-guidance]
last_updated: 2025-03-16
---

# Skip Layer Guidance (Uncond)

Skip Layer Guidance for the unconditional (negative) pass is a technique that skips specific transformer blocks during the negative conditioning inference, improving output quality without additional compute cost and actually providing a slight speed boost.

> "skipping layers on the uncond will make them a lot worse, but like you want the uncond to be bad lol" — Draken, March 13, 2025

> "it's purposely making the unconditional worse, as it should be, making the effect of cfg stronger" — Kijai, March 16, 2025

---

## Overview

**Discovered:** March 13, 2025 via Reddit post

**Key insight:** By skipping certain transformer blocks during the unconditional/negative inference pass, the model produces improved results. This is counterintuitive but follows the principle that the negative conditioning should be "worse" to provide better guidance.

**Important distinction:** This is NOT the same as traditional Skip Layer Guidance (SLG) which runs three separate conditioning passes. This technique only skips block execution for the uncond pass, making it effectively free in terms of compute cost.

**Major update (March 16, 2025):** Kijai released comprehensive testing grids for both 1.3B and 14B models, showing the effect of skipping different blocks. The technique is now available in native ComfyUI via KJNodes.

---

## How It Works

### Standard CFG Process

1. Run conditional (positive) pass through all blocks
2. Run unconditional (negative) pass through all blocks
3. Combine results using CFG scale

### Skip Layer Guidance (Uncond)

1. Run conditional (positive) pass through all blocks
2. Run unconditional (negative) pass, **skipping specific blocks**
3. Combine results using CFG scale

**Key difference:** The unconditional pass skips execution of certain blocks, making the negative conditioning "worse" in a way that improves the final output.

**Why it works:**
> "it's purposely making the unconditional worse, as it should be, making the effect of cfg stronger" — Kijai, March 16, 2025

> "too much of course breaks everything, so we have to choose a block where the effect works best" — Kijai, March 16, 2025

---

## Performance Impact

**Compute cost:** Slightly faster than baseline
- Skips block execution for uncond pass
- No additional passes required
- Actually provides a speed boost

**Quality impact:** Significant improvements reported
- Better detail preservation across many blocks
- Improved prompt adherence
- More natural-looking results
- Better hands in some cases
- Sharper details
- Improved acuity

> "in general details are improved on many" — Kijai, March 16, 2025

> "this method also increases the inference speed so it's kinda win-win" — Kijai, March 16, 2025

> "The SLG is quite stunning on the T2V 1.3B model, It brings whole new level of acuity" — zelgo_, March 16, 2025

---

## Settings

### Recommended Blocks to Skip

**For 14B models:**

| Block(s) | Notes |
|----------|-------|
| **9-10** | Most commonly recommended; tested defaults in KJNodes |
| **8** | Alternative option |
| **Multiple blocks** | Can skip multiple blocks for stronger effect |

**For 1.3B models:**

| Block(s) | Notes |
|----------|-------|
| **6-9** | Usable range for 1.3B |
| **8** | Kijai's favorite for 1.3B |
| **11** | Affects mouth movement (skipping 11 reduces talking) |

> "6-9 seems the usable range" — Kijai, March 16, 2025

> "still 8 is my favorite" — Cseti, March 16, 2025

**Block-specific effects (1.3B):**
- **Block 11:** When skipped, reduces mouth movement/talking
- **Start/end blocks:** More important than middle blocks
- **Different blocks have different effects** on detail, sharpness, and motion

### Start and End Percent

| Parameter | Recommended Value | Notes |
|-----------|------------------|-------|
| **start_percent** | 0.1-0.3 | When to begin applying SLG |
| **end_percent** | 0.9-1.0 | When to stop applying SLG |

**Kijai's tested settings (March 16, 2025):**
- 1.3B: start 0.3, end 0.9
- Effect: Less destructive than starting at 0.1

> "less destructive" — Kijai, March 16, 2025 (on using start 0.3 instead of 0.1)

---

## Implementation

### Native ComfyUI (KJNodes)

**Status:** Implemented (March 16, 2025)

Kijai released SLG support in KJNodes for native ComfyUI.

**Requirements:**
- KJNodes custom node pack (latest version)
- TeaCache node (required for model patching, can be set to no-op)

**Usage:**
1. Add TeaCache node (required for patching)
2. Add SLG node from KJNodes
3. Configure block numbers and start/end percent
4. Connect to sampler

**Default settings:**
- Optimized for 14B models
- Blocks 9-10 by default
- Tested and confirmed working

> "tested very little but enough that I saw it work" — Kijai, March 16, 2025

**Important:** The TeaCache node is required for SLG to work, as it patches the model to accept the modifications. You can set TeaCache to no-op settings if you don't want caching.

### Kijai Wrapper

**Status:** Implemented (March 13, 2025)

**Usage:**
1. Update wrapper to latest version
2. Use SLG node with `slg_layers = [8]` (1.3B) or `[9,10]` (14B)
3. Set `start_percent` and `end_percent`
4. Connect to sampler

---

## Visual Comparisons

### 1.3B Block Comparison Grid

Kijai shared comprehensive grids on March 16, 2025 showing the effect of skipping different blocks (0-29) on 1.3B model:

**Key findings:**
- Blocks 6-9 show usable improvements
- Block 8 is particularly effective
- Block 11 affects mouth movement (reduces talking when skipped)
- Start and end blocks (0-5, 25-29) have more dramatic effects
- Middle blocks show more subtle improvements

**Visual effects:**
- Improved detail and sharpness across many blocks
- Better acuity and clarity
- Some blocks improve specific features (hands, faces, etc.)

### CFG Interaction

Kijai tested SLG with different CFG values:

**Without SLG:**
- Standard output at CFG 6

**With SLG (block 10, start 0.3, end 0.9):**
- Improved detail at CFG 4
- Similar quality to CFG 6 without SLG

**Implication:** SLG allows reducing CFG while maintaining quality

> "yes, its seems you can reduce the CFG more with SLG, allowing for a more 'realistic' image" — zelgo_, March 16, 2025

---

## Combining with Other Optimizations

### TeaCache

**Status:** Compatible (required for native implementation)

**Setup:**
- TeaCache node is required for SLG in native ComfyUI
- Can set TeaCache to no-op if you don't want caching
- Both optimizations work together for cumulative speedup

> "it requires using my TeaCache node as well since it's what patches the model to accept some stuff that wouldn't work otherwise, for now" — Kijai, March 16, 2025

### Torch.compile

**Status:** Compatible with caveats

**Important:** Apply torch.compile LAST in the patch chain

**Patch order:**
1. SLG patch
2. Enhance-a-Video patch (if using)
3. TeaCache patch
4. Torch.compile patch (LAST)

> "you want compile to apply last after all that" — Kijai, March 16, 2025

**Known issue:** Introducing patches after compile has run once breaks compile until model reload

> "introducing enhance (and probably other patches) after you have ran it once with compile does break compile until you reload the model" — Kijai, March 16, 2025

### Enhance-a-Video

**Status:** Compatible

**Setup:** Apply before torch.compile in patch chain

### LoRA Block Editing

**Important finding:** When using SLG with LoRAs, disabling the same block in LoRA block edit as in SLG can cause slow-motion effects.

**Reported issue (March 16, 2025):**
- User (BondoMan) reported slow-motion effect when using SLG with LoRA
- Disabling the SLG block in LoRA block edit improved quality but introduced slow-motion
- Motion was more "real-time" without SLG block editing

**Recommendation:** Test both approaches for your specific use case

---

## Model-Specific Behavior

### Wan 2.1 14B

**Optimal blocks:** 9-10
- Consistently improved results
- Better prompt adherence
- Improved detail quality
- Default in KJNodes implementation

**Settings:**
- start_percent: 0.1-0.3
- end_percent: 0.9-1.0
- CFG: Can be reduced (4-5 instead of 6) while maintaining quality

### Wan 2.1 1.3B

**Optimal blocks:** 6-9 (8 is favorite)
- Block 8 provides best balance
- Blocks 6-9 all show improvements
- Block 11 affects mouth movement

**Settings:**
- start_percent: 0.3 (less destructive than 0.1)
- end_percent: 0.9
- CFG: Standard settings work well

**Key difference:** 1.3B has only 30 blocks (0-29) vs 14B's 40 blocks (0-39)

---

## Use Cases

### Detail Enhancement

**Primary benefit:** Improved detail and sharpness across the image

**Applications:**
- Close-up shots requiring fine detail
- Texture-heavy scenes
- Character faces and hands
- Any content where detail matters

### CFG Reduction

**Benefit:** Achieve similar quality at lower CFG values

**Applications:**
- More natural-looking outputs
- Reduced "AI look"
- Better motion at lower CFG
- Faster generation (lower CFG = faster)

### Speed Optimization

**Benefit:** Slight speed boost from skipping blocks

**Applications:**
- Production workflows
- Batch generation
- Combined with other optimizations for cumulative speedup

---

## Known Issues

### Slow-Motion Effect with LoRA Block Editing

**Problem:** When using SLG with LoRAs and disabling the same block in LoRA block edit, videos may show slow-motion effect.

**Reported by:** BondoMan, March 16, 2025

**Symptoms:**
- Videos play in slow-motion
- Motion is less "real-time"
- Particularly noticeable with fast movement (running, etc.)

**Possible solutions:**
- Adjust CFG (try lower values)
- Don't disable SLG block in LoRA block edit
- Test different block combinations
- Add "slow motion" to negative prompt

**Community investigation:**
> "its possibly too much total guidance strength" — deleted_user_2ca1923442ba, March 16, 2025

> "sometimes too much guidance can resemble too little" — deleted_user_2ca1923442ba, March 16, 2025

### Torch.compile Compatibility

**Problem:** Patches applied after compile break compilation

**Solution:** Always apply torch.compile LAST in patch chain

**Workaround:** Reload model if patches are added after compile

### Native ComfyUI Complexity

**Issue:** Native with multiple patches can be messy

> "native with all these patches and compile gets pretty messy and lots of things can go wrong" — Kijai, March 16, 2025

**Recommendation:** Test patches individually before combining

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| Slow-motion effect | Lower CFG; don't disable SLG block in LoRA block edit; add "slow motion" to negative |
| Compile breaks after adding SLG | Apply compile LAST; reload model if needed |
| TeaCache required error | Add TeaCache node (can set to no-op) |
| No quality improvement | Try different blocks (6-9 for 1.3B, 9-10 for 14B) |
| Too much effect | Increase start_percent (0.3 instead of 0.1) |
| Motion issues | Test without LoRA block editing; adjust CFG |
| Unclear which block to use | Start with block 8 for 1.3B, blocks 9-10 for 14B |

---

## Best Practices

1. **Use model-specific blocks:**
   - **14B:** Blocks 9-10
   - **1.3B:** Blocks 6-9 (8 recommended)

2. **Start conservatively:**
   - Use start_percent 0.3 for less destructive effect
   - Can lower to 0.1 if needed

3. **Apply patches in correct order:**
   - SLG → Enhance-a-Video → TeaCache → Torch.compile (LAST)

4. **Test with LoRAs carefully:**
   - Don't automatically disable SLG block in LoRA block edit
   - Test both approaches for your use case

5. **Reduce CFG when using SLG:**
   - Can achieve similar quality at lower CFG
   - Try CFG 4-5 instead of 6

6. **Reload model when changing patches:**
   - Especially important with torch.compile
   - Prevents compilation errors

---

## Performance Stack

For maximum performance with quality, combine SLG with:

- [[teacache]] — Required for native; provides additional speedup
- [[torch-compile]] — Apply LAST; ~30% speedup
- [[enhance-a-video]] — Compatible; apply before compile
- [[fp16-accumulate]] — Stackable; ~20-30% speedup
- [[sageattention]] — Stackable; ~25% speedup

**Combined benefits:**
- Improved quality from SLG
- Slight speed boost from SLG
- Cumulative speedup from other optimizations
- Ability to reduce CFG for more natural results

---

## Community Reception

**Highly positive (March 16, 2025):**

> "The SLG is quite stunning on the T2V 1.3B model, It brings whole new level of acuity" — zelgo_, March 16, 2025

> "Those blocks make a big difference" — Flipping Sigmas, March 16, 2025

> "in general details are improved on many" — Kijai, March 16, 2025

> "this method also increases the inference speed so it's kinda win-win" — Kijai, March 16, 2025

**Key advantages identified:**
- Free quality improvement
- Slight speed boost
- Allows CFG reduction
- Works with other optimizations
- Easy to implement in native ComfyUI

---

## Timeline

| Date | Event |
|------|-------|
| **Mar 13, 2025** | Technique discovered via Reddit post |
| **Mar 13, 2025** | Kijai implements in wrapper |
| **Mar 15, 2025** | Extensive community testing begins |
| **Mar 16, 2025** | **Kijai releases comprehensive testing grids for 1.3B and 14B** |
| **Mar 16, 2025** | **Native ComfyUI support released in KJNodes** |
| **Mar 16, 2025** | Community identifies slow-motion issue with LoRA block editing |
| **Mar 16, 2025** | Torch.compile compatibility guidelines established |

---

## See Also

- [[teacache]] — Required for native implementation; compatible optimization
- [[torch-compile]] — Compatible; apply LAST in patch chain
- [[enhance-a-video]] — Compatible optimization
- [[samplers]] — Sampler and scheduler choices
- [[speed]] — Other speed optimizations
- [[wan-2.1]] — Base model documentation

## External Resources

- [Reddit Post: Skip Layer Guidance for Wan](https://www.reddit.com/r/StableDiffusion/comments/1jac3wm/dramatically_enhance_the_quality_of_wan_21_using/) — Original discovery and code
- [KJNodes Repository](https://github.com/kijai/ComfyUI-KJNodes) — Native ComfyUI implementation
