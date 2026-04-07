---
title: Shift Parameter
aliases: [shift, sample-shift, noise-schedule]
last_updated: 2025-03-09
---

# Shift Parameter

The shift parameter controls the shape of the noise schedule in flow matching models like Wan and Hunyuan. It determines how sampling steps are distributed between high-noise and low-noise regions, affecting both structure and detail in generated videos.

## What Shift Does

> "shift changes the shape of the noise schedule, more shift means it spends more steps at high noise, and less at low noise" — spacepxl, March 9, 2025

**High shift values:**
- More steps spent at high noise levels
- Better for structure and composition
- Worse for fine details
- More dynamic motion

**Low shift values:**
- More steps spent at low noise levels
- Better for details and texture
- Worse for overall structure
- Less dynamic motion

> "more shift is good for structure, but bad for details, and less shift is bad for structure, but good for details" — spacepxl, March 9, 2025

---

## Noise Schedule Visualization

spacepxl shared noise schedule plots showing the effect of different shift values (March 9, 2025):

- **Shift 3:** More time at low noise (detail-focused)
- **Shift 8:** Balanced distribution
- **Shift 17:** More time at high noise (structure-focused)

The noise schedule determines what percentage of sampling steps occur at each noise level, directly affecting what the model prioritizes during generation.

---

## Recommended Values

### Wan 2.1

| Model | Default Shift | Notes |
|-------|--------------|-------|
| **T2V 14B** | 5.0 | Official default for most variants |
| **I2V 480p** | 3.0 | Lower than other variants |
| **I2V 720p** | 5.0 | Same as T2V |
| **T2V 1.3B** | 8-9 | "Less steps, more shift" pattern |

### Hunyuan I2V

| Model | Default Shift | Notes |
|-------|--------------|-------|
| **Hunyuan I2V** | 17 | Much higher than Wan defaults |

> "on hunyuan i2v it defaults to 17" — aikitoria, March 9, 2025

> "so that's why they recommended raising it for 'more dynamic video'" — aikitoria, March 9, 2025

---

## Effect on Motion

> "shift makes it move more" — Benjimon, March 9, 2025

Higher shift values generally produce more dynamic motion and camera movement. This is why Hunyuan I2V defaults to shift 17 — it prioritizes dynamic video generation.

**For Wan:**
- Shift 3-5: Subtle motion, detail-focused
- Shift 5-8: Balanced motion and detail
- Shift 8-15: More dynamic motion, better for action
- Shift 15+: Very dynamic, may sacrifice detail

---

## Advanced: Custom Sigma Schedules

Some users bypass the shift parameter entirely and use custom sigma schedules:

> "personally I turn shift off and do custom sigmas" — deleted_user_2ca1923442ba, March 9, 2025

> "it doesn't take that long rly" — deleted_user_2ca1923442ba, March 9, 2025

Custom sigma schedules allow precise control over the noise distribution at each step, but require more expertise to configure properly.

---

## Interaction with Other Parameters

### Shift and Steps

The "less steps, more shift" pattern (used in Wan 1.3B and Hunyuan) suggests that higher shift can compensate for fewer sampling steps by spending more time on structure.

### Shift and Context Windows

Higher shift values (8-15) work better with context windows for long video generation. See [[context-windows]] for details.

### Shift and Quality

spacepxl noted that shift is one of the parameters that significantly affects quality:

> "high shift and low steps are deadly for quality" — spacepxl, March 9, 2025

For quality-critical work, use moderate shift values (5-8) with sufficient steps (30-50).

---

## Model-Specific Behavior

### Wan 2.1

- Official defaults are well-tuned for most use cases
- I2V 480p uses lower shift (3.0) than other variants
- 1.3B benefits from higher shift (8-9) to compensate for smaller model size

### Wan 2.2

Shift behavior in Wan 2.2 may differ due to the dual high/low noise architecture. The high noise expert handles composition and structure, while the low noise expert handles detail — this architectural split may reduce the impact of shift tuning.

### Hunyuan

Hunyuan I2V defaults to much higher shift (17) than Wan, reflecting different training and design priorities.

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| Too much motion, chaotic output | Lower shift to 3-5 |
| Static, boring output | Increase shift to 8-12 |
| Poor structure, composition issues | Increase shift |
| Lack of fine detail | Decrease shift |
| Quality issues with low steps | Increase steps rather than relying on high shift |

---

## See Also

- [[wan-2.1]] — Base model with shift parameter
- [[samplers]] — Sampler and scheduler choices that interact with shift
- [[context-windows]] — Long video technique that benefits from higher shift
- [[speed]] — Speed optimizations and their interaction with shift

## External Resources

- [Flow Matching Paper](https://arxiv.org/abs/2210.02747) — Theoretical background on flow matching and noise schedules
