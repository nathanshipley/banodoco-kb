---
title: Cakify LoRA
aliases: [cakify, cake-lora, cakify-lora]
last_updated: 2025-03-10
---

# Cakify LoRA

The Cakify LoRA is a motion LoRA for Wan 2.1 I2V that transforms objects into cake and cuts them with a knife, similar to the viral "everything is cake" effect popularized by Pika Labs.

> "wtf" — aikitoria, March 10, 2025 (reacting to Cakify results)

> "hahahah" — Juampab12, March 10, 2025

> "wan is amazing" — Juampab12, March 10, 2025

---

## Overview

The Cakify LoRA demonstrates exceptional training efficiency, having been trained on an extremely low resolution (168x350) yet producing high-quality results at standard resolutions. Like the [[squish-lora]], it represents a breakthrough in understanding how little data is needed for effective motion LoRA training.

**Key features:**
- Trained on Wan 2.1 I2V 14B 480p
- Training resolution: **168x350** (extremely low)
- Generalizes to much higher resolutions
- Knife appears automatically (learned from training data)
- Part of the Pika Labs effect replication series
- **Trained on 16GB VRAM** — demonstrates accessibility of motion LoRA training

> "uh guys the cakify lora was trained on 168x350 only" — Juampab12, March 10, 2025

> "and its crazy good" — Juampab12, March 10, 2025

> "this model..." — Juampab12, March 10, 2025

> "the cakify model is i2v 14b 480p... trained on 16gb" — Juampab12, March 10, 2025

---

## Training Details

**Dataset:**
- Likely trained on Pika Labs outputs
- Training resolution: 168x350 (portrait orientation)
- High-quality source material despite low resolution
- Knife cutting motion is part of the learned sequence

**Model:**
- Base: Wan 2.1 I2V 14B 480p
- Extremely low training resolution demonstrates Wan's ability to learn motion patterns independent of resolution
- **Hardware:** Single 16GB GPU (likely RTX 4090 or similar)

**Key insight:** The LoRA was trained at 168x350 resolution but works excellently at standard resolutions, proving that motion patterns can be learned at very low resolutions and generalize to higher ones.

---

## How It Works

### Learned Elements

The LoRA learns several key elements from the training data:

1. **Cake transformation:** Object interior becomes cake-like texture
2. **Knife appearance:** Knife enters frame automatically (learned from training)
3. **Cutting motion:** Smooth cutting animation
4. **Reveal sequence:** Interior is revealed as the knife cuts through

> "if the knife was in all the reference images, I have a hard time believing it learned it" — mamad8, March 10, 2025

> "if it appears right at frame 2 then yes" — mamad8, March 10, 2025

> "yes exactly" — mamad8, March 10, 2025

> "it appears" — mamad8, March 10, 2025

> "yeah the knife comes in after the first frame, so it learns it separate from the image" — spacepxl, March 10, 2025

### Frame Sequence

**Frame 1:** Reference image (object before cutting)
**Frame 2+:** Knife appears and cutting motion begins

The knife is learned as part of the motion sequence, not from the reference image. This is why it appears consistently across different subjects.

---

## Usage

### Basic Setup

**Model:** Wan 2.1 I2V 14B 480p

**Input:** Reference image of object to "cakify"

**Recommended workflow:**
1. Provide reference image without knife
2. Apply Cakify LoRA
3. Generate video
4. Knife will appear automatically and cut through object

> "your first referennce image should't innclude the knife" — mamad8, March 10, 2025

---

## Results Quality

**Generalization:**
- Works on wide variety of subjects
- Maintains cake texture consistency
- Smooth knife motion across different objects
- Handles different camera angles

**Resolution scaling:**
- Trained at 168x350
- Works excellently at standard resolutions (480p, 720p)
- Demonstrates motion learning is resolution-independent

**Examples from community:**
- Various objects transformed to cake
- Consistent knife appearance and cutting motion
- High-quality results despite low training resolution

---

## Training Implications

**Key lessons from Cakify:**

1. **Resolution independence:** Motion patterns can be learned at very low resolutions (168x350) and generalize to higher ones
2. **Sequential learning:** Elements that appear after frame 1 (like the knife) are learned as part of the motion sequence
3. **Efficient training:** Low resolution training is much faster while maintaining quality
4. **Wan's capabilities:** The model can learn complex motion patterns independent of resolution
5. **Accessibility:** 14B I2V LoRA training is possible on consumer 16GB GPUs with proper settings

> "this model is a machine i tell ya" — Juampab12, March 10, 2025

### Training Recommendations

Based on Cakify's success:

**For motion LoRAs:**
- Consider training at lower resolutions for faster iteration
- Focus on motion quality over resolution
- Ensure consistent motion patterns in training data
- Elements that appear after frame 1 will be learned as part of the sequence

**Data preparation:**
- Reference image (frame 1) should not include elements that appear later
- Subsequent frames should show the motion/transformation
- Quality of motion matters more than resolution

**Hardware requirements:**
- 16GB VRAM sufficient for I2V 14B 480p training at low resolution
- Low resolution training dramatically reduces VRAM requirements
- Makes advanced motion LoRA training accessible to consumer hardware

---

## Comparison to Other Effect LoRAs

**vs [[squish-lora]]:**
- Squish: 20 training clips, hands appear automatically
- Cakify: Unknown clip count, knife appears automatically, trained at 168x350
- Both demonstrate exceptional generalization
- Both learn elements that appear after frame 1
- Cakify trained on 14B I2V, Squish on 14B I2V

**vs Pika Labs:**
- Quality: Comparable to original Pika effect
- Cost: Free vs paid API
- Control: More control with local generation

---

## Community Reception

> "wtf" — aikitoria, March 10, 2025

> "WWTTTFFFFFF" — Juampab12, March 10, 2025

> "that was trained in 168x350 resolution" — Juampab12, March 10, 2025

> "this model..." — Juampab12, March 10, 2025

The community was particularly impressed by the low training resolution producing high-quality results, demonstrating Wan's ability to learn motion patterns independent of resolution.

---

## Related Effects

The Cakify LoRA is part of a series of Pika Labs effect replications:

- [[squish-lora]] — Squishing/compression effect
- Cakify — Cake cutting effect
- Hydraulic press (in development)
- Melt (potential future development)
- Crush (potential future development)

> "the melt one would be really cool also, or the crush one..." — orabazes, March 10, 2025

---

## See Also

- [[squish-lora]] — Related effect LoRA
- [[lora-training]] — Training LoRAs for Wan
- [[wan-2.1]] — Base model for Cakify LoRA
- [[i2v]] — Image-to-video workflows

## External Resources

- [Cakify LoRA on Civitai](https://civitai.com/models/1337473/cakify-cake-everything-wan-14b-i2v)
- [Pika Labs Effects](https://twitter.com/pika_labs/status/1846295401491845213) — Original inspiration
