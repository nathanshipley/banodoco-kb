---
title: VAE Fine-tuning for Wan
aliases: [vae-finetuning, vae-training, decoder-finetuning]
last_updated: 2025-03-14
---

# VAE Fine-tuning for Wan

Fine-tuning the Wan VAE decoder can improve quality for specific use cases, particularly videos with rapidly changing frames (timelapses, image-to-image transformations) where the standard VAE's 4-frame compression causes quality degradation.

---

## Overview

**Experimental work by:** mamad8 (March 13-14, 2025)

**Problem:** The Wan VAE compresses 4 video frames into each latent. When those 4 frames are very different (as in timelapses or image-to-image transformations), quality degrades significantly.

**Proposed solution:** Fine-tune the VAE decoder on videos where each latent contains 4 identical frames, giving the VAE more capacity to preserve detail when frames don't change.

> "13K steps currently, I \"\"\"think\"\"\" there's improvement but I think I'd also need to finetune the encoder for best results. Then train again my loras with the new VAE" — mamad8, March 14, 2025

---

## Why Fine-tune the VAE?

### Standard VAE Behavior

The Wan VAE:
- Compresses 4 frames into 1 latent
- Optimized for smooth motion (frames are similar)
- Struggles when consecutive frames are very different

### Problem Cases

**Timelapses:**
- Each frame is significantly different from the previous
- VAE compression artifacts become visible
- Quality degrades over the sequence

**Image-to-Image LoRAs:**
- Frame 1: Original image
- Frames 2-5: Transformed image (all identical)
- VAE must handle both smooth and static sequences

**Rapid scene changes:**
- Hard cuts between scenes
- Fast transformations
- Any content where 4 consecutive frames are not similar

---

## Training Approach

### Decoder-Only Fine-tuning

**Critical:** Only train the decoder, not the encoder.

> "don't finetune the encoder, you want the latent space to remain unchanged since the diffusion model already knows it" — spacepxl, March 13, 2025

**Reasoning:**
- The diffusion model is trained on the existing latent space
- Changing the encoder would change the latent space
- This would break compatibility with the diffusion model
- Decoder-only training preserves latent space while improving reconstruction

### Training Data

Videos where each latent contains 4 identical frames:
- Frame structure: 0,1,1,1,1,5,5,5,5,9,9,9,9...
- Each group of 4 identical frames becomes one latent
- VAE learns to reconstruct static frames better

**Why this works:**
- Standard VAE is optimized for motion (changing frames)
- Fine-tuning on static frames teaches it to handle both cases
- Improves reconstruction when frames don't change

---

## Training Parameters

**From spacepxl (March 13, 2025):**

| Parameter | Value | Notes |
|-----------|-------|-------|
| **Learning rate** | 1e-6 * sqrt(batch_size) | Scale with batch size |
| **Resolution** | 256-512 | Lower resolution for faster training |
| **Frames** | 33 | Reference from ltxv VAE training |
| **Loss function** | DINOv2-base | Perceptual loss |
| **dino_scale** | 10 | Weight for DINO loss |
| **Optimizer** | 8bit AdamW | Memory-efficient optimizer |
| **Train decoder only** | Yes | Critical: do not train encoder |

### Loss Function

**DINOv2-base perceptual loss:**
- Measures perceptual similarity
- Better than pixel-wise MSE for visual quality
- dino_scale=10 balances perceptual and reconstruction loss

---

## Implementation

### Training Code

mamad8 is adapting spacepxl's ltxv VAE training script for Wan.

**Key modifications needed:**
- Load Wan VAE instead of LTX VAE
- Freeze encoder weights
- Prepare dataset with 4-frame repetition structure
- Configure loss function (DINOv2)

### Dataset Preparation

For timelapse/image-to-image training:

1. Extract frames from source videos
2. Create training videos with structure: 0,1,1,1,1,5,5,5,5,9,9,9,9...
3. Each group of 4 identical frames will be compressed to 1 latent
4. VAE learns to reconstruct static frames accurately

**Example (Juampab12's aging timelapse approach):**
- Frame 0: Uncompressed (first frame)
- Frames 1,1,1,1: First latent (4 identical frames)
- Frames 5,5,5,5: Second latent (4 identical frames)
- Frames 9,9,9,9: Third latent (4 identical frames)

---

## Expected Results

### Improvements

**For timelapses:**
- Better preservation of detail in each frame
- Less compression artifacts
- Cleaner transitions between frames

**For image-to-image LoRAs:**
- Better reconstruction of static transformed frames
- Less blur/artifacts in transformation results
- Improved quality for style transfer LoRAs

### Limitations

**Encoder fine-tuning may be needed:**
> "I think I'd also need to finetune the encoder for best results" — mamad8, March 14, 2025

However, encoder fine-tuning would require retraining all LoRAs on the new latent space.

**LoRA compatibility:**
- LoRAs trained on standard VAE may need retraining
- Fine-tuned VAE changes reconstruction characteristics
- Existing LoRAs may not work optimally

---

## Training Progress

**mamad8's run (March 13-14, 2025):**

- **13,000 steps:** "I think there's improvement"
- **Planned:** 12 more hours of training
- **Observation:** Noise radius getting smaller

> "I think it's better too! the noise is getting smaller in radius at least" — Juampab12, March 14, 2025

---

## Use Cases

### Timelapse LoRAs

Juampab12 is training an aging timelapse LoRA that would benefit from fine-tuned VAE:
- Videos show aging over time (one photo per day for 10 years)
- Each frame is significantly different
- Standard VAE compression causes artifacts
- Fine-tuned VAE should preserve detail better

### Image-to-Image Transformation LoRAs

mamad8's image-to-image LoRAs:
- Frame 1: Original image
- Frames 2-5: Transformed image (all identical)
- Fine-tuned VAE should handle this structure better

### Style Transfer

Any LoRA that transforms images:
- Realistic → cartoon
- Empty room → furnished room
- Normal weight → different weight
- Any before/after transformation

---

## Comparison to Standard VAE

| Aspect | Standard VAE | Fine-tuned VAE |
|--------|-------------|----------------|
| **Optimized for** | Smooth motion | Both motion and static |
| **Timelapse quality** | Poor (artifacts) | Improved (less artifacts) |
| **I2I LoRA quality** | Moderate | Better |
| **Training time** | N/A (pretrained) | Hours to days |
| **LoRA compatibility** | All existing LoRAs | May require retraining |
| **Latent space** | Standard | Unchanged (decoder-only) |

---

## Future Work

### Encoder Fine-tuning

**Potential benefits:**
- Even better quality for timelapses
- Improved latent space for rapid changes

**Challenges:**
- Would change latent space
- All LoRAs would need retraining
- Diffusion model may need adaptation
- Much more complex undertaking

### Community Testing

Once mamad8's fine-tuned VAE is released:
- Test with existing LoRAs
- Compare quality on timelapses
- Evaluate I2I transformation quality
- Determine if LoRA retraining is necessary

---

## Status

**As of March 14, 2025:**
- Training in progress (13K+ steps)
- Results pending
- Code being adapted from spacepxl's ltxv VAE training
- Community awaiting results

---

## See Also

- [[lora-training]] — Training LoRAs that may benefit from fine-tuned VAE
- [[wan-2.1]] — Base model using the standard VAE
- [[timelapse-training]] — Juampab12's timelapse LoRA technique

## External Resources

- [DINOv2 Paper](https://arxiv.org/abs/2304.07193) — Perceptual loss function
- [spacepxl's ltxv VAE training](https://github.com/spacepxl/) — Reference implementation
