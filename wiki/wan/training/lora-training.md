---
title: LoRA Training for Wan
aliases: [lora-training, training, finetune]
last_updated: 2025-03-14
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
- **Motion patterns can be learned at very low resolutions** and generalize to higher ones

---

## Breakthrough: Low-Resolution Training

**Major discovery (March 10, 2025):** The [[cakify-lora]] demonstrated that motion LoRAs can be trained at extremely low resolutions (168x350) and still produce excellent results at standard resolutions.

> "uh guys the cakify lora was trained on 168x350 only" — Juampab12, March 10, 2025

> "and its crazy good" — Juampab12, March 10, 2025

**Implications:**
- Motion patterns are resolution-independent
- Training at low resolution is much faster
- Results generalize to higher resolutions
- Dramatically reduces training time and VRAM requirements

---

## Training Time Estimates

### Wan 1.3B

| Resolution | Frames | Duration | GPUs | Time |
|-----------|--------|----------|------|------|
| 168x350 | Variable | Short clips | 1 | Minutes to hours |
| 244p | 60 | Short clips | 1 | Hours |
| 480p | 81 | Standard | 1 | Hours to 1 day |
| 720p | 81 | Standard | 1-2 | 1-2 days |

> "1.3B hours not days" — Juampab12, March 9, 2025

> "you dont need insane res for a character for example" — Juampab12, March 9, 2025

**Rapid training examples:**
- **Hydraulic press LoRA:** 2 videos, 1 epoch, 15-20 minutes, already "crazy good" — Juampab12, March 10, 2025
- **[[squish-lora]]:** 20 videos, minimal training time, exceptional results
- **[[cakify-lora]]:** 168x350 resolution, produces excellent results at standard resolutions

> "and he accidentally trained with only 2 videos! for 1 epoch" — Juampab12, March 10, 2025

> "for like 15m basically or 20" — Juampab12, March 10, 2025

> "and look at it its already crazy good" — Juampab12, March 10, 2025

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

**Note on diffusers:**

> "diffusion-pipe is fine" — comfy, March 10, 2025

> "but it is only a lora trainer" — comfy, March 10, 2025

> "I don't think it uses diffusers though" — comfy, March 10, 2025

> "it does" — Doctor Shotgun, March 10, 2025

> "it does" — Benjimon, March 10, 2025

While diffusion-pipe does use diffusers, comfy noted that diffusers is "a real pile of trash" and is working on an alternative training framework:

> "current libraries people use for training like diffusers for example is a real pile of trash and I think it's greatly limiting what can be done with training and I want to change that" — comfy, March 10, 2025

### spacepxl's WanTraining

**Released March 10, 2025:** spacepxl released training code for normal LoRA, CFG distillation, and control LoRA:

- **Repository:** https://github.com/spacepxl/WanTraining
- **Models:** https://huggingface.co/spacepxl/Wan2.1-control-loras/tree/main

> "eh fuckit, I don't have time to document anything right now so excuse the mess, but here's the wip tile loras: https://huggingface.co/spacepxl/Wan2.1-control-loras/tree/main and the training code for normal lora, cfg distillation, and control lora: https://github.com/spacepxl/WanTraining" — spacepxl, March 10, 2025

> "test script is in the training repo" — spacepxl, March 10, 2025

**Features:**
- Normal LoRA training
- CFG distillation
- Control LoRA training (tile deblur, depth, pose, etc.)
- Batch size 1 for mixed resolution/frames
- Rank 128 LoRA on 1.3B

> "I'm mostly doing rank 128 lora on 1.3b" — spacepxl, March 10, 2025

> "batch size 1, makes it easy to do mixed resolution/frames" — spacepxl, March 10, 2025

### Musubi (Kohya)

**Recent updates (March 13, 2025):**

Kohya merged a PR adding new features:
- fp8 optimization flag
- fp16 source file support

> "btw for anyone using musubi Kohya (merged a PR) that added a new flag for fp8 optimization yesterday. Worth a look (update maybe). fp16 source files are also supported now: https://github.com/kohya-ss/musubi-tuner/pull/141" — JohnDopamine, March 13, 2025

### Gradio Training Interfaces

**Community development (March 13-14, 2025):**

Multiple users are developing Gradio interfaces for easier LoRA training:

**VRGameDevGirl84:**
> "Wish me luck guys. i'm trying to build a gradio app that will let us train wan lora's all right inside the UI. Trying to get it to even do all the backend coding and downloads. everything. wish me luck!!!" — VRGameDevGirl84, March 14, 2025

**Alisson Pereira:**
> "I'm making an interface for the diffusion pipe." — Alisson Pereira, March 14, 2025

> "It's almost ready, I just need to test it more, because there are many combinations and the interface is dynamic for all models that have support in the diffusion pipe" — Alisson Pereira, March 14, 2025

Alisson's interface is built in Blazor (.NET) with extensive .NET experience, focusing on dynamic support for all diffusion-pipe models.

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

For motion/concept LoRAs, having diverse examples (100+ videos) is beneficial. However, recent breakthroughs show that as few as 2-20 high-quality videos can produce excellent results:

- **[[squish-lora]]:** 20 videos, exceptional generalization
- **[[cakify-lora]]:** Unknown count, trained at 168x350, excellent results
- **Hydraulic press LoRA:** 2 videos, 1 epoch, "crazy good" results

> "only 20 clips in training data!" — Juampab12, March 10, 2025

> "that prove once again that we dont need so big dataset just good selection" — nebsh#0, March 10, 2025

> "quality is all you need!" — Juampab12, March 10, 2025

### Frame 1 Considerations for I2V

**Critical insight:** Elements that appear after frame 1 are learned as part of the motion sequence, not from the reference image.

> "yeah the knife comes in after the first frame, so it learns it separate from the image" — spacepxl, March 10, 2025

> "same with the hands in the squish lora" — spacepxl, March 10, 2025

**Best practices:**
- Frame 1 should be the reference state (before transformation)
- Elements that appear during the motion (hands, knives, etc.) should not be in frame 1
- The model will learn to generate these elements as part of the sequence

> "your first referennce image should't innclude the knife" — mamad8, March 10, 2025

### Video Cropping and Preprocessing

**Tools:**

**Free online tool:**
> "I used this tool to crop my dataset, fast and free, no login, unlimited https://www.freeconvert.com/crop-video" — Juampab12, March 13, 2025

**Python script for batch processing:**
> "this is a great python script shared early on in the HYV training days that'll crop all videos in a folder to exact frames/resolutions: https://discord.com/channels/1076117621407223829/1316871013384065126/1325599601113174017" — JohnDopamine, March 13, 2025

**Note on manual cropping:**
> "the reason I needed to do it manually was to make sure it cropped where I wanted, not just the center" — Juampab12, March 13, 2025

---

## Training Strategy

### Starting Simple

> "should prob start with something simpler to learn what I am doing here instead of running a process that takes days only to find out I did it wrong" — aikitoria, March 9, 2025

> "yes just use one even lol" — Benjimon, March 9, 2025 (suggesting starting with single GPU)

**Recommended progression:**
1. Start with 1.3B model on single GPU
2. Use low resolution (168x350 or 480p) and short clips
3. Train for a few hours to verify workflow
4. Scale up to higher resolution/longer clips
5. Move to 14B and multi-GPU when ready

### Epoch Monitoring

> "i trained a lora for a few hours for like 100 epochs, but noticed the 20 and 30 epoch ones are actually totally fine, i think 100 was even overbaked with no movement" — seitanism#0, March 9, 2025

> "so that only took like 30 minutes maybe idk" — seitanism#0, March 9, 2025

Save checkpoints at multiple epochs and test them. Early epochs (20-30) may be sufficient, and over-training can reduce quality.

**Wan converges quickly:**

> "wan converges before 1 epoch lol" — Juampab12, March 10, 2025

> "it learns a lot very quickly, but you can still get better results with more training" — spacepxl, March 10, 2025

### Image vs Video Training

> "but it was just pictures" — seitanism#0, March 9, 2025

> "its so much slower with video clips?" — seitanism#0, March 9, 2025

Video training is significantly slower than image training due to the temporal dimension. A LoRA that takes 30 minutes to train on images may take hours or days when training on video.

**However:** spacepxl noted that training on 9 frames is not much slower than 1 frame:

> "I trained on 9 frames mostly, it's not that much slower than 1 frame since there's some constant cost per step" — spacepxl, March 10, 2025

### Regularization and Data Mixing

**Community discussion on 70/30 rule:**

> "train with a good mix of data, not just hydraulic press. usually like 70% of your target goal, 30% of diverse other stuff" — fredbliss, March 10, 2025

> "that way you dont overfit on the tiny model" — fredbliss, March 10, 2025

**spacepxl's perspective:**

> "that would be similar to regularization images in dreambooth training, I didn't find it helpful" — spacepxl, March 10, 2025

> "if you want to prevent overfitting just use more data" — spacepxl, March 10, 2025

> "clever tricks will never prevent overfitting, it's purely a data size vs training time problem" — spacepxl, March 10, 2025

> "In the limit, if you never go past 1 epoch it's not possible to overfit" — spacepxl, March 10, 2025

**Key insight:** More diverse data is better than mixing target and non-target data. Focus on quality and quantity of relevant data.

---

## Training Parameters

### Learning Rate

**spacepxl's tile model:**
- 5e-6 for 20k steps
- 1e-5 for 12k steps (when progress slowed)

> "for the tile model it was 5e-6 for 20k steps then 1e-5 for 12k steps since progress was slowing down" — spacepxl, March 10, 2025

**mamad8's experiments:**
- LR: 5e-2 (likely meant 5e-5 or 5e-4)
- Batch size: 1

> "I'm currently doing all my experiments using BS1 and LR 5e-2" — mamad8, March 10, 2025

> "Ooops inverse" — mamad8, March 10, 2025

**General guidance:**
> "lr = 1e-6 * sqrt(batch_size) is probably a good place to start" — spacepxl, March 13, 2025

### Rank and Alpha

**spacepxl's configuration:**
- Rank: 128
- Alpha: 128 (alpha = rank)

> "yes, rank=128 and alpha=rank" — spacepxl, March 10, 2025

**Alpha and LR relationship:**
> "multiply/divide by sqrt(alpha) when comparing different alphas, rank is unrelated to learning rate unless you set alpha based on rank" — spacepxl, March 13, 2025

> "if you set alpha=1 or some other constant value, you can change rank freely without affecting lr" — spacepxl, March 13, 2025

**Recommended for beginners:**
> "if you're a noob like me just do something like 16 rank, 5e-5 lr, 1 alpha" — Juampab12, March 13, 2025

**Alpha theory:**
> "in theory alpha=1 should help with numerical stability but with fp32 lora weights that really doesn't matter" — spacepxl, March 13, 2025

### Batch Size

**Recommendation:** Batch size 1

> "batch size 1, makes it easy to do mixed resolution/frames" — spacepxl, March 10, 2025

> "in image models there doesn't seem to be any quality benefit to higher batch sizes, only hardware efficiency benefit" — spacepxl, March 10, 2025

---

## T2V vs I2V Training

### Cross-Compatibility

> "you don't specifically need to use the i2v model" — Faust-SiN, March 9, 2025

> "t2v loras work with i2v" — Faust-SiN, March 9, 2025

> "and that still works in combination with i2v so it keeps the character from the image?" — aikitoria, March 9, 2025

> "yeah" — Faust-SiN, March 9, 2025

**Key insight:** T2V LoRAs are compatible with I2V models. This means you can train on the T2V model (which may be easier/faster) and use the resulting LoRA with I2V for character consistency.

### I2V-Specific Training

**Style transformation LoRAs:**

> "I've made a LoRA that changes the 'style' directly at frame 2" — mamad8, March 10, 2025

> "frame 1 is only used as a reference in photo realistic then frame 2 directly switches to another style and continues in the otherr style" — mamad8, March 10, 2025

**What I2V can learn:**
- Movement/action/camera movements
- Style transformations (frame 1 → frame 2+ style change)
- Object appearances (elements that appear after frame 1)

**What I2V cannot learn:**
- Pure style (frame 1 is always used as reference)
- Elements that should be in frame 1 (use T2V for this)

### Training Style Transformation LoRAs

**Workflow for "pixarify" or similar:**

1. Extract first frame of videos
2. Convert first frame to target style (using Magnific AI, etc.)
3. Use ffmpeg to replace first frame in videos
4. Train on modified videos

> "What you could do for your test is: 1. Extract the first frame of your videos 2. Covnert this first frame to a photorealistic style or any other style (using magnific ai for example) 3. Use ffmpeg to replace the first frame from your videos to the converted first frame in the other style 4. Train with this!" — mamad8, March 10, 2025

**Automation:**

> "yeah you could automate it in comfy, use a model with controlnets to convert the first frame to realistic, replace just the first frame in the otherwise pixar video, then save it out" — spacepxl, March 10, 2025

### Image-to-Image Style Transfer Training

**Technique discovered by mamad8:**

Train I2V LoRAs on 5-frame videos where:
- Frame 1: Original image (before transformation)
- Frames 2-5: Same image after transformation (all 4 frames identical)

**Applications:**
- Style transfer (realistic → cartoon, etc.)
- Object transformation (empty room → furnished room)
- Body transformation (normal weight → different weight)
- Any before/after transformation

**Training details (mamad8's furnishing LoRA):**
- 250 videos
- 6500 steps
- LR: 2e-5
- Rank: 64
- Alpha: 64
- Resolution: 384x256

> "Videos of 5 frames. Frame 1 : image before transformation. Frames 2-5 : same image after transformation" — mamad8, March 13, 2025

**Captioning for controllability:**
> "not currently, I have to caption dataset" — mamad8, March 13, 2025 (on controlling furnishing style)

Without captions, the transformation is random. With captions, you can control the type of transformation (e.g., "rustic furniture," "modern furniture," "white furniture").

**Community interest:**
> "basically you create a controlnet hehehe via prompt" — Alisson Pereira, March 13, 2025

> "slider lora" — Alisson Pereira, March 13, 2025

Multiple users expressed interest in this technique for various applications:
- Weight transformation
- Hair length/style changes
- Aging/de-aging
- Style transfer

---

## Control LoRAs

**New capability announced March 10, 2025:** spacepxl released training code and examples for control LoRAs (tile deblur, depth, pose, etc.).

**How they work:**
- Concatenate control signal along input channel dimension
- Train LoRA on the rest of the model
- Similar to InstructPix2Pix, SD depth models, Flux control LoRAs

> "this is just straight up concatenate the signal along the input channel dimension, and train lora on the rest of the model" — spacepxl, March 10, 2025

**Advantages:**
- Simpler than ControlNet architecture
- Lower inference cost
- Easier to train
- Can use any control signal (depth, pose, tile deblur, etc.)

> "IMO this method is stronger than controlnet, less inference cost, and easier to train, so I hope it catches on with more models" — spacepxl, March 10, 2025

See [[control-lora]] for detailed information.

---

## VAE Fine-tuning

**Experimental work by mamad8 (March 13, 2025):**

mamad8 is working on fine-tuning the Wan VAE to better handle videos with rapidly changing frames (e.g., timelapses).

**Problem:** The Wan VAE compresses 4 frames into each latent. When those 4 frames are very different (as in timelapses), quality degrades significantly.

**Proposed solution:** Fine-tune the VAE decoder on videos where each latent contains 4 identical frames, giving the VAE more capacity to preserve detail.

**Training parameters (from spacepxl):**
- LR: 1e-6 * sqrt(batch_size)
- Resolution: 256-512
- Frames: 33 (for ltxv reference)
- Loss: DINOv2-base
- dino_scale: 10
- Optimizer: 8bit AdamW
- Only train decoder, not encoder

> "don't finetune the encoder, you want the latent space to remain unchanged since the diffusion model already knows it" — spacepxl, March 13, 2025

**Status:** Training code being adapted from spacepxl's ltxv VAE training script. Results pending.

---

## Timelapse Training Technique

**Juampab12's approach (March 13-14, 2025):**

Training an aging timelapse LoRA using a novel frame duplication technique:

**Problem:** Timelapse videos have rapidly changing frames, causing VAE compression artifacts.

**Solution:** Duplicate frames to align with VAE's 4-frame latent structure:
- Frame 0: Uncompressed (first frame)
- Frames 1,1,1,1: First latent (4 identical frames)
- Frames 5,5,5,5: Second latent (4 identical frames)
- Frames 9,9,9,9: Third latent (4 identical frames)
- etc.

**Data augmentation:** Create 4 videos from the same source:
- Video 1: 0,1,1,1,1,5,5,5,5,9,9,9,9...
- Video 2: 1,2,2,2,2,6,6,6,6,10,10,10,10...
- Video 3: 2,3,3,3,3,7,7,7,7,11,11,11,11...
- Video 4: 3,4,4,4,4,8,8,8,8,12,12,12,12...

This provides 4x more training data from the same source video while avoiding VAE compression issues.

> "so Im getting more data out of the same starting data" — Juampab12, March 13, 2025

**Captioning:**
> "for example in my training im doing 'An aging timelapse in the style of 4g1ngl4ps3, one photo every day for 10 years.' where I only change this number in the captions" — Juampab12, March 13, 2025

**Training progress (March 13-14):**
- 32 epochs: Model learned stuttery motion, no transitions yet
- Training overnight to see further progress

---

## Quality Preservation

> "is it possible to teach wan i2v a new concept (any character does x) using lora without degrading visual quality overall?" — aikitoria, March 9, 2025

> "If your dataset is good quality and you train at high res the resulting videos will still be good quality." — Benjimon, March 9, 2025

**Best practices for quality preservation:**
- Use high-quality source videos (1080p+, high bitrate)
- Train at high resolution (720p+) OR low resolution for motion-only (168x350+)
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

**However:** Recent breakthroughs show that many useful LoRAs can be trained in minutes to hours, not days or weeks.

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

**PCIe bandwidth usage:**

> "you need pcie lanes to transfer data to your gpu. Like if you look at nvtop when ur using block swapping it is xfer at like 13GB/s" — Benjimon, March 10, 2025

Block swapping during training uses significant PCIe bandwidth. More lanes = faster transfers.

**Multi-GPU communication:**

> "multigpu talks to each other and block swapping while training is the same as during inf" — Benjimon, March 10, 2025

Multi-GPU training involves constant communication between GPUs, making PCIe bandwidth important.

---

## Troubleshooting

### OOM Errors

**Solutions:**
- Reduce resolution (try 168x350 for motion-only training)
- Reduce frame count
- Reduce batch size (use 1)
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
- Insufficient resolution (unless training motion-only)
- Poor captioning

### No Visible Changes

**Reported issue (March 10, 2025):**

JohnDopamine reported training an I2V LoRA with no visible changes when applied:

> "Lora off / Lora on / one of the 6 short vid clips I'm training on just as a test to try and get something to change when applied (pushing a pixarish style)" — JohnDopamine, March 10, 2025

> "So basically didn't seem to do anything......not sure what's up...." — JohnDopamine, March 10, 2025

**Possible causes:**
- Training style on I2V (frame 1 is always used as reference, so style changes may not be visible)
- Need to test with appropriate reference images
- Training parameters may need adjustment

> "I think something is wrong" — Juampab12, March 10, 2025

> "it will still copy the style/appearance from the image though, no?" — spacepxl, March 10, 2025

> "would need to test with an image in the style of the training data to see if there's a difference learned" — spacepxl, March 10, 2025

### HUD/UI Elements Not Learning

**JohnDopamine's experience (March 13, 2025):**

Tried training a LoRA to add a Super Mario Bros. score HUD overlay:
- Dataset: 33-frame videos with HUD overlay on frames 2-33
- Frame 1: Clean without HUD (reference image)
- Caption: "smbnes with score HUD"
- Result: LoRA did not learn the HUD at all

**Possible causes:**
> "hud learns poorly at low resolutions" — Mngbg, March 13, 2025

> "I cant think of a reason it wouldnt appear other than it wasn't in the training data" — Juampab12, March 13, 2025

Training tools may crop or pad videos, potentially removing the HUD area. Verify that the HUD is actually present in the processed training data.

---

## AI-Assisted Development

**Community perspective (March 14, 2025):**

Most developers in the community use AI assistance for coding:

> "I'd be surprised if anyone around here is not using AI to code at least to a small degree" — Juampab12, March 14, 2025

**Tools mentioned:**
- **GitHub Copilot:** Used by career programmers
- **DeepSeek:** Preferred by some for handling large scripts without leaving content out
- **ChatGPT:** Widely used but sometimes leaves out code
- **Claude:** Used for script generation and debugging
- **GPT o3 mini:** Larger context than other models

**Gradio interface development:**
> "I also use it when I need to make interfaces in gradio, it's faster, and then I adjust things that I think aren't so good" — Alisson Pereira, March 14, 2025

**Concerns:**
> "the problem that can happen in the long term is that people stop thinking hehehe and like not being able to do anything without an LLM in life" — Alisson Pereira, March 14, 2025

---

## See Also

- [[wan-2.1]] — Base model for LoRA training
- [[multi-gpu]] — Multi-GPU inference and training
- [[hardware]] — Hardware requirements and recommendations
- [[lora]] — Using LoRAs with Wan models
- [[squish-lora]] — Example of successful motion LoRA
- [[cakify-lora]] — Example of low-resolution training success
- [[control-lora]] — Control LoRA training for Wan

## External Resources

- [diffusion-pipe Repository](https://github.com/tdrussell/diffusion-pipe) — Recommended training framework
- [spacepxl WanTraining Repository](https://github.com/spacepxl/WanTraining) — Training code for LoRA, CFG distillation, and control LoRA
- [spacepxl Control LoRAs](https://huggingface.co/spacepxl/Wan2.1-control-loras/tree/main) — Example control LoRAs
- [spacepxl Demystifying SD Finetuning](https://github.com/spacepxl/demystifying-sd-finetuning/) — Dense but informative reference on alpha/LR relationships
- [Musubi Tuner](https://github.com/kohya-ss/musubi-tuner) — Kohya's training framework with recent fp8 optimizations
- [Vast.ai](https://vast.ai/) — GPU rental for cloud training
