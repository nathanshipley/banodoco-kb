---
title: Quality vs Speed Trade-offs
aliases: [quality-vs-speed, optimization-tradeoffs]
last_updated: 2025-03-09
---

# Quality vs Speed Trade-offs

When optimizing Wan video generation, there's an inherent tension between generation speed and output quality. Understanding these trade-offs helps you make informed decisions about which optimizations to use for your specific use case.

---

## The Quality-First Perspective

Community member spacepxl advocates strongly for prioritizing quality over speed:

> "teacache in particular is really bad for quality, sage attn is probably ok" — spacepxl, March 9, 2025

> "but high shift and low steps are deadly for quality" — spacepxl, March 9, 2025

> "eh, 1.3b at 50 steps easily beats the quality of most people's 'efficient' 14b workflows" — spacepxl, March 9, 2025

> "most of the optimizations people use hurt quality a lot" — spacepxl, March 9, 2025

> "I would much rather wait twice as long for better quality" — spacepxl, March 9, 2025

> "these video generation times are not bad at all compared to cg rendering" — spacepxl, March 9, 2025

**Key arguments:**
- Many popular optimizations significantly degrade quality
- Generation times are already fast compared to traditional CG rendering
- 1.3B at 50 steps can beat "efficient" 14B workflows in quality
- Patience pays off in final output quality

---

## The Speed-First Perspective

Most of the community actively seeks speed optimizations:

- **TeaCache:** ~2x speedup, widely used despite quality concerns
- **Speed LoRAs:** 4-8 steps instead of 20-50
- **Low step counts:** 8-12 steps common in production workflows
- **High shift values:** Compensate for fewer steps

**Key arguments:**
- Faster iteration enables more experimentation
- "Good enough" quality at 2x speed is often acceptable
- Time is valuable, especially for commercial work
- Quality loss is minimal with proper settings

---

## Optimization Impact on Quality

### High Impact (Significant Quality Loss)

| Optimization | Quality Impact | Speed Gain | Notes |
|--------------|----------------|------------|-------|
| **TeaCache (aggressive)** | High | ~2-3x | "really bad for quality" per spacepxl |
| **Very low steps (4-8)** | High | ~4-6x | Especially with high shift |
| **High shift + low steps** | Very High | Varies | "deadly for quality" per spacepxl |
| **Speed LoRAs on HN (Wan 2.2)** | High | ~2-4x | Kills 2.2's motion advantages |

### Medium Impact (Noticeable Quality Loss)

| Optimization | Quality Impact | Speed Gain | Notes |
|--------------|----------------|------------|-------|
| **TeaCache (moderate)** | Medium | ~1.5-2x | Threshold 0.04-0.08 |
| **Low steps (12-15)** | Medium | ~2-3x | With proper shift tuning |
| **fp8 quantization** | Low-Medium | ~1.2-1.5x | Varies by model |
| **GGUF Q4-Q6** | Medium | ~1.3-1.8x | Lower quants = more loss |

### Low Impact (Minimal Quality Loss)

| Optimization | Quality Impact | Speed Gain | Notes |
|--------------|----------------|------------|-------|
| **SageAttention** | Minimal | ~1.25x | "probably ok" per spacepxl |
| **fp16 accumulate** | None | ~1.2-1.3x | Pure speed, no quality loss |
| **Torch.compile** | None | ~1.3x | Pure speed, no quality loss |
| **GGUF Q8** | Minimal | ~1.2x | Better than fp8 |
| **Enhance-a-Video** | Minimal | ~1.15-1.2x | Newer optimization |

---

## Quality-Preserving Speed Stack

For users who want speed without sacrificing quality:

**Recommended stack:**
1. **fp16 accumulate** — 20-30% speedup, no quality loss
2. **SageAttention** — 25% speedup, minimal quality loss
3. **Torch.compile** — 30% speedup, no quality loss
4. **GGUF Q8** (if VRAM limited) — minimal quality loss vs fp16

**Combined speedup:** ~2x faster with negligible quality impact

**Avoid:**
- TeaCache (if quality is critical)
- Very low step counts (<20)
- High shift with low steps
- Aggressive quantization (Q4 and below)

---

## Speed-Optimized Stack

For users who prioritize speed and accept quality trade-offs:

**Recommended stack:**
1. **Speed LoRA** (CausVid/LightX2V) — 4-8 steps instead of 20-50
2. **TeaCache** — 2x speedup on top of speed LoRA
3. **fp16 accumulate** — Additional 20-30%
4. **SageAttention** — Additional 25%
5. **Torch.compile** — Additional 30%

**Combined speedup:** ~4-6x faster than baseline

**Quality impact:** Noticeable but acceptable for many use cases

---

## Use Case Recommendations

### Final Quality Renders

**Settings:**
- 30-50 steps
- No TeaCache
- Moderate shift (5-8)
- fp16 or GGUF Q8
- SageAttention + fp16 accumulate + torch.compile only

**Expected time (14B, 720p, 81 frames):**
- ~15-20 minutes on 4090 with optimizations
- ~30-40 minutes without optimizations

### Rapid Prototyping

**Settings:**
- 8-12 steps with speed LoRA
- TeaCache enabled
- Higher shift (8-12)
- fp8 or GGUF Q6
- All optimizations enabled

**Expected time (14B, 720p, 81 frames):**
- ~3-5 minutes on 4090

### Commercial Production

**Balance approach:**
- 20 steps (no speed LoRA)
- TeaCache with conservative threshold (0.06-0.08)
- Moderate shift (5-8)
- GGUF Q8 or fp16
- SageAttention + fp16 accumulate + torch.compile

**Expected time (14B, 720p, 81 frames):**
- ~8-12 minutes on 4090

---

## Model Size Considerations

### 1.3B vs 14B for Quality

> "eh, 1.3b at 50 steps easily beats the quality of most people's 'efficient' 14b workflows" — spacepxl, March 9, 2025

**Key insight:** A properly configured 1.3B model at 50 steps can produce better quality than an over-optimized 14B model at 8 steps.

**When to use 1.3B:**
- Quality-focused workflows with time to spare
- 50 steps is ~2 minutes on 4090 (very fast)
- Better than rushing 14B with aggressive optimizations

**When to use 14B:**
- Final quality at moderate step counts (20-30)
- Complex scenes requiring more model capacity
- When you can afford the time investment

---

## Measuring Quality Loss

Quality degradation from optimizations can be subtle. Look for:

**Visual artifacts:**
- Flickering or noise
- Loss of fine detail (hair, texture)
- Reduced sharpness
- Color shifts
- Motion artifacts

**Temporal issues:**
- Jittering or stuttering
- Inconsistent motion
- Frame-to-frame instability

**Composition problems:**
- Poor structure
- Incorrect anatomy
- Prompt adherence issues

---

## Community Consensus

The community is split on quality vs speed:

**Quality-first minority:**
- Willing to wait for best results
- Avoid aggressive optimizations
- Compare to CG rendering times (hours/days)
- "I would much rather wait twice as long for better quality"

**Speed-first majority:**
- Actively seek all optimizations
- Accept quality trade-offs
- Value iteration speed
- "Good enough" is often sufficient

**Balanced middle:**
- Use conservative optimizations
- Test quality at each step
- Adjust based on use case
- Different settings for preview vs final

---

## Recommendations

### For Quality-Critical Work

1. **Start with baseline settings** (30-50 steps, shift 5-8)
2. **Add only quality-preserving optimizations** (fp16 accumulate, SageAttention, torch.compile)
3. **Test each optimization** before adding the next
4. **Compare outputs** at each step
5. **Accept longer generation times** as necessary

### For Rapid Iteration

1. **Use speed LoRAs** (CausVid/LightX2V)
2. **Enable TeaCache** with moderate threshold
3. **Use all optimizations** (fp16 accumulate, SageAttention, torch.compile)
4. **Accept quality trade-offs** for speed
5. **Re-render finals** without aggressive optimizations if needed

### For Balanced Workflows

1. **20-30 steps** (no speed LoRA)
2. **Conservative TeaCache** (threshold 0.06-0.08)
3. **Quality-preserving optimizations** (fp16 accumulate, SageAttention, torch.compile)
4. **Test and adjust** based on results
5. **Different settings** for preview vs final

---

## See Also

- [[teacache]] — Speed optimization with quality trade-offs
- [[sageattention]] — Quality-preserving optimization
- [[fp16-accumulate]] — Quality-preserving optimization
- [[speed]] — Overview of all speed optimizations
- [[shift]] — Shift parameter and its quality impact
- [[samplers]] — Sampler choices and quality

