---
title: Squish Effect LoRA
aliases: [squish-lora, squish-effect, sq41sh]
last_updated: 2025-03-10
---

# Squish Effect LoRA

The Squish Effect LoRA is a motion LoRA for Wan 2.1 I2V that teaches the model to generate "squish" effects — objects being compressed and deforming under pressure, similar to the viral effect popularized by Pika Labs.

> "can't believe how well that squish lora works. almost 1:1 with the pika-labs original" — orabazes, March 10, 2025

> "it's really damn good" — Juampab12, March 10, 2025

> "this is the first LORA that made me realize i really need to set up training in my pc" — Juampab12, March 10, 2025

---

## Overview

The Squish Effect LoRA demonstrates exceptional generalization capabilities, working across a wide variety of subjects and scenarios despite being trained on only 20 video clips. It represents a significant milestone in motion LoRA training for video models.

**Key features:**
- Trained on Wan 2.1 I2V 480p 14B
- Only 20 training clips used
- Generalizes extremely well to new subjects
- Works with both wrapper and native ComfyUI (with caveats)
- Trigger word: `sq41sh squish effect`
- Hands appear automatically during squishing (learned from training data)

> "only 20 clips in training data!" — Juampab12, March 10, 2025

> "that prove once again that we dont need so big dataset just good selection" — nebsh#0, March 10, 2025

> "quality is all you need!" — Juampab12, March 10, 2025

---

## Training Details

**Dataset:**
- 20 video clips total
- Likely trained on Pika Labs outputs (community speculation)
- High-quality source material
- Hands squishing objects are part of the learned motion

> "I think it's trained on Pika outputs?" — Kijai, March 10, 2025

**Model:**
- Base: Wan 2.1 I2V 480p 14B
- Training resolution: Not publicly disclosed

**Key insight:** This LoRA demonstrates that quality of training data matters far more than quantity. 20 well-selected clips produced a highly generalizable motion LoRA.

---

## Usage

### Basic Setup

**Model:** Wan 2.1 I2V 480p 14B (or 720p variant)

**Trigger word:** `sq41sh squish effect`

**Recommended prompt structure:**
```
In the video, a miniature is presented. The miniature is hold in person's hands. The person then presses the [object], causing a sq41sh squish effect. The person keeps pressing down on the miniature, further showing the sq41sh squish effect, colorful nails.
```

> "In the video, a miniature is presented. The miniature is hold in person's hands. The person then presses the tank, causing a sq41sh squid effect. The person keeps pressing down on the miniature, further showing the sq41sh squish effect, colorful nails." — Fred, March 10, 2025

### Wrapper Workflow

**Confirmed working** with Kijai wrapper.

**Settings:**
- Use I2V model (480p or 720p)
- Include trigger words in prompt
- Standard I2V settings apply

**Example workflow:** Available from Fred (March 10, 2025)

### Native ComfyUI

**Status:** Works, but with caveats.

**Issues reported:**
- TeaCache may cause problems with the LoRA
- Results may vary compared to wrapper

> "yeah, without teacache it works" — Fred, March 10, 2025

**Workaround:** Disable TeaCache when using the Squish LoRA in native workflows.

**Sampler:** Use `dpmpp_2m` for best results in native.

> "dpmpp_2m" — N0NSens, March 10, 2025

---

## Generalization and Motion

### Automatic Hand Appearance

The LoRA learned that hands appear during squishing from the training data:

> "same with the hands in the squish lora" — spacepxl, March 10, 2025

This means hands will automatically appear in generations even if not explicitly prompted, as they were part of the training videos.

### Motion Variation

Some users reported that their generations had no motion before the squishing, while others (like Kijai) observed wing flapping in a bird before squishing:

> "I love how it flapped the wings first" — Kijai, March 10, 2025

> "yeah mine have no motion at all before the squishing" — Juampab12, March 10, 2025

> "i guess a bird in mid air MUST flap its wings" — Juampab12, March 10, 2025

> "if you're using 1 strength" — Juampab12, March 10, 2025

This suggests the model adds contextually appropriate motion based on the subject and LoRA strength.

### Generalization Without Trigger Word

One user tested generalization by not using the trigger word:

> "wanted to see how well that squish lora would generalize to just 'squishing things'. Didn't use the trigger word though" — TK_999, March 10, 2025

Results were positive, suggesting the LoRA can work even without explicit triggering.

---

## Performance

**Generation times (community reports):**

**3080 Ti (12GB):**
- 448x448, 81 frames: ~8 minutes (with optimizations)

> "8 minutes for 448x448 / 81 frames on my 3080ti" — Fred, March 10, 2025

**3090 (24GB):**
- 624x624, 25 steps: ~11.5 minutes (wrapper, with TeaCache)

> "I'm using with wrapper, with teacache, 624x624, 25 steps 11.5min on my 3090" — burgstall, March 10, 2025

---

## Results Quality

**Generalization:**
- Works on wide variety of subjects (people, objects, animals)
- Maintains squish physics across different materials
- Handles different camera angles and lighting

> "it generalizes right?" — Kijai, March 10, 2025

**Examples from community:**
- Squishing miniatures
- Squishing food items
- Squishing toys
- Squishing faces (NSFW applications)
- Even works on cats (with humorous results)
- Birds (with wing flapping before squish)

> "my cat" — Juampab12, March 10, 2025 (with crying emoji reactions)

> "that bird needs a squishing" — Juampab12, March 10, 2025

**Quality comparison:**
- Nearly 1:1 with Pika Labs original effect
- Better than expected for a LoRA trained on only 20 clips
- Some users report it rivals commercial implementations

> "This feels at least as good as any similar stuff I've seen from Pika" — pom_x_moq#0, March 10, 2025

---

## Known Issues

### TeaCache Incompatibility

**Problem:** Using TeaCache with the Squish LoRA in native ComfyUI produces poor results.

**Solution:** Disable TeaCache when using this LoRA.

> "yeah preview is looking better now, seems like teacache was causing the weirdness" — Fred, March 10, 2025

### Image Orientation

**Problem:** Some users report the LoRA works better with landscape images than portrait.

**Solution:** Use landscape-oriented input images when possible.

> "Oh, wow...it just worked when I tried an image that was landscape!" — GalaxyTimeMachine (RTX4090), March 10, 2025

### Trigger Word Requirement

**Problem:** LoRA may not activate without proper trigger words.

**Solution:** Always include `sq41sh squish effect` in your prompt.

> "have you used the trigger words?" — Fred, March 10, 2025

---

## Training Implications

**Key lessons from this LoRA:**

1. **Quality over quantity:** 20 high-quality clips outperform hundreds of mediocre ones
2. **Motion LoRAs are viable:** Complex motion patterns can be learned effectively
3. **Generalization is possible:** Well-trained LoRAs generalize far beyond training data
4. **Wan is a strong base:** The model can learn and apply complex motion patterns
5. **Hands as learned elements:** Objects that appear consistently in training (like hands) become part of the learned motion

> "goes to show wan can learn anything, it's a very strong model" — Juampab12, March 10, 2025

> "it's crazy how well these LoRAs can work, Wan gonna have some future" — Kijai, March 10, 2025

**Community impact:**

This LoRA has inspired many users to begin training their own motion LoRAs:

> "this is the first LORA that made me realize i really need to set up training in my pc so many things I wanted to try" — Juampab12, March 10, 2025

---

## Upscaling and Post-Processing

**Upscaling workflow:**

Some users report good results upscaling Squish LoRA outputs:

> "I'm giving a try to upscale the result using lower res I didn't liked much, I'm using the normal upscaler so no flux or something else that probably could bring some better quality, but with 512x512 to 2048x2048 it looked interesting" — Fred, March 10, 2025

**Interpolation:**

Standard frame interpolation techniques work well with Squish LoRA outputs.

---

## Comparison to Commercial Solutions

**vs Pika Labs:**
- Quality: Nearly identical
- Speed: Depends on hardware (local may be slower)
- Cost: Free vs paid API
- Control: More control with local generation

**vs Other LoRAs:**
- Generalization: Exceptional compared to typical LoRAs
- Training efficiency: 20 clips is remarkably small dataset
- Motion complexity: Handles complex deformation physics

---

## Future Potential

**Possible extensions:**
- Other physics effects (stretch, bounce, melt)
- Material-specific deformations
- Multi-object interactions
- Combined with other control methods (VACE, depth)

> "You can see the brief look of terror in his eyes" — pom_x_moq#0, March 10, 2025 (commenting on a squish effect result)

---

## See Also

- [[lora-training]] — Training LoRAs for Wan
- [[wan-2.1]] — Base model for Squish LoRA
- [[i2v]] — Image-to-video workflows
- [[teacache]] — Optimization that conflicts with this LoRA
- [[cakify-lora]] — Related effect LoRA from same creator

## External Resources

- [Squish Effect LoRA on Civitai](https://civitai.com/models/1340141/squish-effect-wan21-i2v-lora)
- [Reddit Announcement](https://www.reddit.com/r/StableDiffusion/comments/1j7nk5g/i_just_opensourced_the_viral_squish_effect_see/)
