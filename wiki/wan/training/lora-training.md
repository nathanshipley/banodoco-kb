---
title: LoRA Training for Wan
aliases: [lora-training, training, finetune]
last_updated: 2025-03-09
---

# LoRA Training for Wan

LoRA (Low-Rank Adaptation) training allows fine-tuning Wan models on custom datasets without modifying the base model weights. This enables teaching new concepts, characters, styles, or motions while maintaining compatibility with the base model.

---

## Overview

LoRA training for Wan video models is significantly more resource-intensive than image model training due to the temporal dimension. Training times can range from hours to days (or even months for full-quality, high-resolution training).

> "at high res days lol" — Benjimon, March 9, 2025 (on training time for high-resolution LoRAs)

**Key considerations:**
- **Dataset quality matters more than quantity** for video LoRAs
- **Resolution and frame count** dramatically affect training time and VRAM requirements
- **Multi-GPU training** is often necessary for full-quality results
- **Captioning** is critical for motion/concept LoRAs

---

## Training Time Estimates

### Wan 1.3B

| Resolution | Frames | Duration | GPUs | Time |
|-----------|--------|----------|------|------|
| 244p | 60 | Short clips | 1 | Hours |
| 480p | 81 | Standard | 1 | Hours to 1 day |
| 720p | 81 | Standard | 1-2 | 1-2 days |

> "1.3B hours not days" — Juampab12, March 9, 2025

> "you dont need insane res for a character for example" — Juampab12, March 9, 2025

### Wan 14B I2V

| Resolution | Frames | Duration | GPUs | Time |
|-----------|--------|----------|------|------|
| 720x720 | 128 | 4 seconds | 4x 4090 | Days |
| 1280x720 | 81 | Full quality | 8x 4090 | Days to weeks |

> "she said good quality" — Benjimon, March 9, 2025 (responding to question about training time)

> "but I want the 14b i2v at full res/frames" — aikitoria, March 9, 2025

**Extreme example:**

Benjimon shared a training run that had been running for 3 months (though this was for SDXL, not Wan):

> "this ones been running for 3 months, this a restart" — Benjimon, March 9, 2025

> "steps: 2%|█ | 3396/167300 [12:19:15<594:39:50, 13.06s/it, avr_loss=0.0626]" — Benjimon, March 9, 2025

This demonstrates that full fine-tunes (not LoRAs) can take extremely long periods.

---

## Hardware Requirements

### Single GPU Training

**Minimum for 1.3B:**
- 12 GB VRAM (with low resolution)
- 16 GB VRAM (for 480p)
- 24 GB VRAM (for 720p)

**Minimum for 14B:**
- 24 GB VRAM (low resolution, heavy block swapping)
- 48 GB VRAM (comfortable training)

### Multi-GPU Training

**Tested configurations:**

**2x RTX 6000 Ada (48 GB each):**
- 720x720x128 frames: 101.853s/iter
- 960x960x128 frames: 266.814s/iter

**4x RTX 4090 (24 GB each):**
- 720x720x128 frames: 98.962s/iter
- 800x800: OOM

> "2x rtx 6000 ada 48gb: 720x720x128-steps: 1 loss: 0.0563 iter time (s): 101.853 samples/sec: 0.039" — Benjimon, March 9, 2025

> "4x 4090: 720x720x128- steps: 1 loss: 0.0457 iter time (s): 98.962 samples/sec: 0.027" — Benjimon, March 9, 2025

**8x RTX 4090:**
- Theoretically possible for full 1280x720x81 training
- Block swapping now enabled for multi-GPU setups
- May require pipeline parallelism configuration

> "8 might Im not sure. This is from my tests and 2 48gb gpus could do full 720p so 8 4090s could maybe. probably for sure now because they just enabled block swapping if needed" — Benjimon, March 9, 2025

### System RAM

- **32 GB minimum** for basic training
- **64 GB recommended** for high-resolution training
- **96+ GB ideal** for complex workflows

---

## Training Frameworks

### diffusion-pipe

Recommended by the community for distributed training:

> "I would recommend https://github.com/tdrussell/diffusion-pipe for distributed training. I was able to train at 720x720x4seconds with 4-4090s" — Benjimon, March 9, 2025

**Features:**
- Distributed training support
- Pipeline parallelism
- Block swapping for VRAM management
- Direct ComfyUI integration

**Configuration:**
- Supports pipeline parallel for multi-GPU
- "you divide the model" across GPUs — Benjimon, March 9, 2025

---

## Dataset Preparation

### Video Quality

> "the dataset is all 1080p videos yea with good bitrate" — aikitoria, March 9, 2025

High-quality source videos are critical for good LoRA results. Use:
- 1080p or higher source resolution
- High bitrate (avoid compressed/low-quality sources)
- Consistent lighting and quality across dataset

### Captioning

**For motion/concept LoRAs:**

> "if you're training a lora on movement, then yeah you want to caption the movement" — Cubey, March 9, 2025

Captioning is essential when training LoRAs to learn specific motions or concepts. Without captions, the model cannot associate the visual content with semantic meaning.

**For character LoRAs:**

Captioning may be less critical for pure character identity LoRAs, but still recommended for best results.

**Captioning tools:**
- Florence2 for auto-captioning
- ChatGPT for caption generation
- Manual captioning for best quality

> "I'm not sure how to go about captioning them or if that is even necessary" — aikitoria, March 9, 2025

> "I've never made a lora before" — aikitoria, March 9, 2025

### Dataset Size

> "assuming I have 100s of videos of different characters doing x to use as samples" — aikitoria, March 9, 2025

For motion/concept LoRAs, having diverse examples (100+ videos) is beneficial. For character LoRAs, fewer high-quality examples may suffice.

---

## Training Strategy

### Starting Simple

> "should prob start with something simpler to learn what I am doing here instead of running a process that takes days only to find out I did it wrong" — aikitoria, March 9, 2025

> "yes just use one even lol" — Benjimon, March 9, 2025 (suggesting starting with single GPU)

**Recommended progression:**
1. Start with 1.3B model on single GPU
2. Use low resolution (480p) and short clips
3. Train for a few hours to verify workflow
4. Scale up to higher resolution/longer clips
5. Move to 14B and multi-GPU when ready

### Epoch Monitoring

> "i trained a lora for a few hours for like 100 epochs, but noticed the 20 and 30 epoch ones are actually totally fine, i think 100 was even overbaked with no movement" — seitanism#0, March 9, 2025

> "so that only took like 30 minutes maybe idk" — seitanism#0, March 9, 2025

Save checkpoints at multiple epochs and test them. Early epochs (20-30) may be sufficient, and over-training can reduce quality.

### Image vs Video Training

> "but it was just pictures" — seitanism#0, March 9, 2025

> "its so much slower with video clips?" — seitanism#0, March 9, 2025

Video training is significantly slower than image training due to the temporal dimension. A LoRA that takes 30 minutes to train on images may take hours or days when training on video.

---

## T2V vs I2V Training

### Cross-Compatibility

> "you don't specifically need to use the i2v model" — Faust-SiN, March 9, 2025

> "t2v loras work with i2v" — Faust-SiN, March 9, 2025

> "and that still works in combination with i2v so it keeps the character from the image?" — aikitoria, March 9, 2025

> "yeah" — Faust-SiN, March 9, 2025

**Key insight:** T2V LoRAs are compatible with I2V models. This means you can train on the T2V model (which may be easier/faster) and use the resulting LoRA with I2V for character consistency.

---

## Quality Preservation

> "is it possible to teach wan i2v a new concept (any character does x) using lora without degrading visual quality overall?" — aikitoria, March 9, 2025

> "If your dataset is good quality and you train at high res the resulting videos will still be good quality." — Benjimon, March 9, 2025

**Best practices for quality preservation:**
- Use high-quality source videos (1080p+, high bitrate)
- Train at high resolution (720p+)
- Don't over-train (monitor epochs)
- Use sufficient VRAM to avoid excessive quantization

---

## Training Time Management

### Local vs Cloud

> "guess renting the gpus will be better then" — aikitoria, March 9, 2025

> "wouldn't want my local server blocked for days" — aikitoria, March 9, 2025

**Considerations:**
- **Local:** Free after hardware investment, but blocks your system
- **Cloud (Vast.ai, etc.):** Pay per hour, but doesn't block local resources
- **Hybrid:** Prototype locally, scale to cloud for final training

> "sometimes local sometime on vast" — Benjimon, March 9, 2025

> "vast is annoying asf tho" — Benjimon, March 9, 2025

### Patience Requirements

> "def wouldn't have the patience to wait 1 month to cook lora" — aikitoria, March 9, 2025

> "At that point I'd just learn to animate lol" — Kosinkadink, March 9, 2025

For extremely long training runs (weeks to months), consider whether the time investment is worth it compared to alternative approaches.

---

## Multi-GPU Setup

### Hardware Recommendations

**Motherboard:**
> "asus x99 e ws only like 150$ us" — Benjimon, March 9, 2025

X99 platform provides 40 PCIe lanes, sufficient for 4x GPUs at 8x/8x/8x/8x.

**PSU:**
> "1500w psu is good" — Benjimon, March 9, 2025

For 4x 4090s, 1500W is minimum. Each 4090 can draw up to 450W under load.

**Cooling:**
> "Water cooling or hybrid cards are alot better than air cooled in this scenario." — Benjimon, March 9, 2025

Multi-GPU training generates significant heat. Water cooling or hybrid cards are strongly recommended.

**Power consumption:**
> "I usually run 2 gui copies and they consume 495 watts each for the 4090s." — Benjimon, March 9, 2025

Expect ~500W per 4090 during training. For 4 cards, that's ~2000W total.

### PCIe Lanes

> "do you need many pcie lanes for training? like would training slow down alot if you only use 4 lanes or something?" — seitanism#0, March 9, 2025

For training, PCIe bandwidth is less critical than for inference. 8x lanes per GPU is generally sufficient. 4x lanes may cause slowdowns but is workable.

**Platform recommendations:**
- **X99:** 40 lanes, cheap, old platform (2014-2016)
- **X570/X670 (AM4/AM5):** 24-28 lanes, modern platform
- **Threadripper:** 64+ lanes, expensive but best for 4+ GPUs

> "For my initial miltigpu setup I used an AM4 X570 board from a previous setup that was my previous setup with a 5950x, the board supported two GPUs in dual 8x PCIe Gen 4 lanes." — Kosinkadink, March 9, 2025

---

## Troubleshooting

### OOM Errors

**Solutions:**
- Reduce resolution
- Reduce frame count
- Reduce batch size
- Enable block swapping
- Use more GPUs with pipeline parallelism

### Slow Training

**Check:**
- GPU utilization (should be near 100%)
- PCIe bandwidth (8x minimum recommended)
- System RAM (may be bottleneck)
- Dataset loading speed (SSD vs HDD)

### Quality Issues

**Common causes:**
- Low-quality source videos
- Over-training (too many epochs)
- Insufficient resolution
- Poor captioning

---

## See Also

- [[wan-2.1]] — Base model for LoRA training
- [[multi-gpu]] — Multi-GPU inference and training
- [[hardware]] — Hardware requirements and recommendations
- [[lora]] — Using LoRAs with Wan models

## External Resources

- [diffusion-pipe Repository](https://github.com/tdrussell/diffusion-pipe) — Recommended training framework
- [Vast.ai](https://vast.ai/) — GPU rental for cloud training

