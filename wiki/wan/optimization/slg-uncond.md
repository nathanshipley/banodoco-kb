---
title: Skip Layer Guidance (Uncond)
aliases: [slg-uncond, uncond-skip, negative-skip, slg]
last_updated: 2025-03-13
---

# Skip Layer Guidance (Uncond)

Skip Layer Guidance for the unconditional (negative) pass is a technique that skips specific transformer blocks during the negative conditioning inference, potentially improving output quality without additional compute cost.

> "skipping layers on the uncond will make them a lot worse, but like you want the uncond to be bad lol" — Draken, March 13, 2025

---

## Overview

**Discovered:** March 13, 2025 via Reddit post

**Key insight:** By skipping certain transformer blocks (typically block 8, 9, or 10) during the unconditional/negative inference pass, the model produces improved results. This is counterintuitive but follows the principle that the negative conditioning should be "worse" to provide better guidance.

**Important distinction:** This is NOT the same as traditional Skip Layer Guidance (SLG) which runs three separate conditioning passes. This technique only skips block execution for the uncond pass, making it effectively free in terms of compute cost.

> "all he changed is to not execute 1 block" — aikitoria, March 13, 2025

> "it IS stg" — Kijai, March 13, 2025

> "think so, but only on neg" — Draken, March 13, 2025

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

**Key difference:** The unconditional pass skips execution of certain blocks (typically block 10), making the negative conditioning "worse" in a way that improves the final output.

---

## Performance Impact

**Compute cost:** Effectively zero
- No additional passes required
- Only skips block execution for uncond
- Same total inference time as standard CFG

**Quality impact:** Reported improvements in output quality
- Better detail preservation
- Improved prompt adherence
- More natural-looking results
- Better hands in some cases

> "wtf" — aikitoria, March 13, 2025 (reacting to quality improvement)

---

## Settings

### Recommended Blocks to Skip

| Block(s) | Notes |
|----------|-------|
| **10** | Most commonly recommended; "supposedly good" |
| **9** | Alternative option |
| **8** | Alternative option |
| **8, 9, 10** | Multiple blocks can be skipped |

**Starting recommendation:** Skip block 10 only for uncond pass.

### Implementation

The technique requires modifying the model's forward pass to skip specific blocks during unconditional inference. As of March 13, 2025:

- **Kijai wrapper:** Implementation available ("I'll add it" — Kijai)
- **Native ComfyUI:** Not yet implemented
- **Manual implementation:** Requires code modification

**Wrapper implementation (March 13, 2025):**

Kijai added SLG (uncond skip) support to the wrapper with the following parameters:

| Parameter | Recommended Value | Notes |
|-----------|------------------|-------|
| **slg_layers** | `[10]` | Block index to skip (0-indexed, so 10 = 11th block) |
| **end_percent** | 0.3 | Apply skipping for first 30% of steps |

**Important:** The block index is 0-indexed, so `slg_layers = [10]` skips the 11th block (block index 10).

---

## Model-Specific Behavior

### Wan 2.1 14B

**Block 10 (index 10, 11th block):** Most effective
- Consistently improved results across multiple tests
- Better prompt adherence
- Improved detail quality
- Better hand generation in some cases

> "no block 10 has improved/not degraded every test I tried so far" — aikitoria, March 13, 2025

**Other blocks (5-11):** Less effective or no improvement

**Multiple blocks (4, 8, 10, 16):** "much more coherent than i would expect" — TK_999, March 13, 2025

### Wan 2.1 1.3B

**Status:** Limited testing as of March 13, 2025

> "nothing in range 5-11 out of 30 worked on 1.3B for anything useful" — Kijai, March 13, 2025

**Key difference:** 1.3B has only 30 blocks (0-29) vs 14B's 40 blocks (0-39), so the equivalent block may not exist.

> "idk why try it on 1.3b, there is no reason to assume that block 10 working on 14b should imply it working on 1.3b" — aikitoria, March 13, 2025

---

## Visual Comparison

aikitoria shared a comparison on March 13, 2025:
- **Left:** Original (all blocks executed)
- **Right:** Skip block 10 on uncond
- **Same seed used for both**
- **Result:** Visible quality improvement

> "left original, right skip block 10 on uncond, same seed" — aikitoria, March 13, 2025

Community reactions: 🔥 👍x3

---

## Combining with Other Optimizations

### TeaCache

**Status:** Compatible

SLG (uncond skip) can be combined with TeaCache for additional speedup:

> "SLG 10 30% feta teacache" — IllumiReptilien, March 13, 2025

Reported as producing excellent results with good detail preservation.

### Feta (Enhance-a-Video)

**Status:** Compatible and recommended

Multiple users reported excellent results combining SLG with Feta:

> "SLG 10 30% feta teacache" — IllumiReptilien, March 13, 2025

> "the one with feta seems to have best hands?" — Kijai, March 13, 2025

> "seem so" — IllumiReptilien, March 13, 2025

### Flow Shift

**Status:** Compatible

IllumiReptilien tested SLG with different flow shift values:

> "SLG 10 30% feta teacache Flowshift 3 (flowshift 5 before)" — IllumiReptilien, March 13, 2025

Lower flow shift (3) reported to work well with SLG.

---

## End Percent Parameter

**Recommended value:** 0.3 (30% of steps)

The `end_percent` parameter controls what portion of the sampling steps use the block skipping:

- **0.3 (30%):** Apply skipping for first 30% of steps, then normal CFG for remaining 70%
- **1.0 (100%):** Apply skipping for all steps

> "end percent 0.3 at the SLG node?" — seitanism#0, March 13, 2025

> "yep" — IllumiReptilien, March 13, 2025

Community testing suggests 30% (0.3) provides good results without over-applying the effect.

---

## Theory

### Why Skipping Uncond Blocks Works

**Hypothesis:** The unconditional pass represents "what not to generate." By making this pass "worse" through block skipping, the guidance becomes more effective.

> "skipping layers on the uncond will make them a lot worse, but like you want the uncond to be bad lol" — Draken, March 13, 2025

**Analogy to SD negative prompts:**
> "some neg embeds in SD, if you threw them into the pos and checked them, they were like wild craziness strangeness haha" — Draken, March 13, 2025

The negative conditioning is supposed to be "bad" — that's what makes it effective guidance.

### CFG and Negative Prompts

**Important:** CFG is required for Wan, unlike some distilled models:

> "cfg is **required** with Wan" — Kijai, March 13, 2025

This makes the uncond skip technique particularly relevant for Wan workflows.

---

## Relationship to TeaCache

Draken raised an interesting question about combining this technique with TeaCache:

> "is it possible to do tea cache on uncond/neg inference? like only, excluding the pos i guess haha" — Draken, March 13, 2025

**Status:** Not yet explored as of March 13, 2025. Theoretically possible but would require implementation work.

---

## Implementation Status

### Kijai Wrapper

**Status:** Implemented (March 13, 2025)

Kijai confirmed the technique is legitimate and added support:

> "ohhh well it's very credible source" — Kijai, March 13, 2025

> "I mean that guy is legit" — Kijai, March 13, 2025

**Usage:**
1. Update wrapper to latest version
2. Use SLG node with `slg_layers = [10]`
3. Set `end_percent = 0.3`
4. Connect to sampler

### Native ComfyUI

**Status:** Not yet implemented

No native implementation announced as of March 13, 2025.

### Manual Implementation

The Reddit post included code showing the modification:
- Modify the model's forward pass
- Add conditional logic to skip specific blocks during uncond inference
- No additional passes required

---

## Known Issues

### Naming Confusion

The Reddit post titled this "Skip Layer Guidance," which caused initial confusion:

> "because the post is titled skip layer guidance" — Kijai, March 13, 2025

> "maybe he called it wrong but what matters is the code" — Juampab12, March 13, 2025

**Clarification:** This is NOT traditional SLG (which requires 3 passes). This is a simpler technique that only skips blocks for the uncond pass.

### Limited Testing

As of March 13, 2025, community testing is limited:
- aikitoria shared one comparison
- Visual improvement observed
- More testing needed to confirm effectiveness across different prompts/seeds

### Model-Specific Effectiveness

**14B:** Block 10 consistently effective
**1.3B:** No effective block found in range 5-11

This suggests the technique may not work equally well across all model sizes.

---

## Best Practices

1. **Start with block 10:** Most commonly recommended starting point for 14B
2. **Test with same seed:** Use identical seeds to compare results
3. **Experiment with different blocks:** Try blocks 8, 9, or 10
4. **Monitor quality:** Not all prompts may benefit equally
5. **Combine with other optimizations:** Works well with TeaCache and Feta
6. **Use 30% end percent:** 0.3 appears to be a good default

---

## Community Reception

**Positive reactions:**
- "wtf" — aikitoria (surprise at quality improvement)
- 🔥 👍x3 reactions to comparison
- Multiple users testing and reporting good results

**Kijai's grid testing (March 13, 2025):**

Kijai created extensive grids testing different blocks:

> "mostly you can see that it does not work on most blocks" — Kijai, March 13, 2025

> "this might end up same as STG where you just can't find one that always works for everything and end up wasting time searching for it" — Kijai, March 13, 2025

**Key insight:** Block 10 appears to be the most consistently effective, but results may vary by content.

---

## Comparison to Traditional SLG

| Aspect | Traditional SLG | Skip Layer Guidance (Uncond) |
|--------|----------------|------------------------------|
| **Passes required** | 3 (pos, neg, skip) | 2 (pos, neg with skip) |
| **Compute cost** | 1.5x baseline | Same as baseline |
| **Implementation** | Complex | Simple (skip block execution) |
| **Quality impact** | Varies | Reported improvements |
| **Speed** | 50% slower | No slowdown |

**Key advantage:** Skip Layer Guidance (Uncond) provides potential quality improvements without the 50% speed penalty of traditional SLG.

---

## Future Development

**Planned:**
- Kijai wrapper implementation (COMPLETED March 13, 2025)
- Community testing and validation
- Optimal block selection guidance
- Potential combination with TeaCache

**Questions to explore:**
- Does this work equally well across all model sizes (1.3B vs 14B)?
- Are certain blocks better for specific content types?
- Can multiple blocks be skipped effectively?
- Does this interact with other optimizations?

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| No quality improvement | Try different blocks (8, 9, or 10) |
| Quality degradation | Reduce end_percent or disable |
| Inconsistent results | Test multiple seeds to find what works |
| Not working on 1.3B | May not have effective block; use 14B instead |
| Unclear which block to use | Start with block 10 for 14B |

---

## See Also

- [[samplers]] — Sampler and scheduler choices
- [[teacache]] — Compatible optimization
- [[enhance-a-video]] — Compatible optimization (Feta)
- [[speed]] — Other speed optimizations
- [[wan-2.1]] — Base model documentation

## External Resources

- [Reddit Post: Skip Layer Guidance for Wan](https://www.reddit.com/r/StableDiffusion/comments/1jac3wm/dramatically_enhance_the_quality_of_wan_21_using/) — Original discovery and code
