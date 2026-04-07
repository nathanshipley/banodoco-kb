---
title: Control LoRAs for Wan
aliases: [control-lora, control-loras, tile-deblur, tile-control]
last_updated: 2025-03-10
---

# Control LoRAs for Wan

Control LoRAs are a technique for adding control signals (depth, pose, tile deblur, etc.) to video generation models by training LoRAs on concatenated input channels. This approach is simpler and more efficient than traditional ControlNet architectures.

---

## Overview

Control LoRAs work by concatenating control signals (depth maps, pose skeletons, etc.) along the input channel dimension and training a LoRA on the model. This is the same approach used by:
- InstructPix2Pix
- SD depth models
- Marigold
- Most I2V models
- Flux control LoRAs

**Key advantages over ControlNet:**
- **Simpler architecture** — no separate control network needed
- **Lower inference cost** — just a LoRA, not a full model
- **Easier to train** — standard LoRA training with concatenated inputs
- **Stackable** — can combine multiple control signals
- **Model-agnostic loading** — works in native ComfyUI with proper implementation

> "IMO this method is stronger than controlnet, less inference cost, and easier to train, so I hope it catches on with more models" — spacepxl, March 10, 2025

---

## Available Control LoRAs

### Tile Control (v0.1 / v0.2)

**Released:** March 10, 2025 by spacepxl

**Model:** Wan 2.1 T2V 1.3B

**Purpose:** Tile deblur / upscaling

**Download:**
- v0.1: `wan2.1-1.3b-control-lora-tile-v0.1.safetensors` (wrapper only)
- v0.2: `wan2.1-1.3b-control-lora-tile-v0.1_comfy.safetensors` (native + wrapper)

**Repository:** https://huggingface.co/spacepxl/Wan2.1-control-loras/

**Training details:**
- Trained on blurred videos
- Input: downscaled to 0.25x, upscaled back (bilinear), blurred
- Learns to restore high-res details from degraded input
- Training resolutions: 624x624, 832x480, 480x832
- Rank: 128
- Alpha: 128 (alpha = rank)

**Use cases:**
- Video upscaling
- Detail restoration
- Deblurring
- Creative upscaling

> "They're all upscale examples technically, the input is downscaled to 0.25x then upscaled back up (bilinear) and blurred, to ensure all high res details are destroyed." — spacepxl, March 10, 2025

---

## Implementation

### Training Approach

**Basic method:**
1. Concatenate control signal along input channel dimension
2. Train LoRA on the rest of the model
3. Use standard LoRA training techniques

> "this is just straight up concatenate the signal along the input channel dimension, and train lora on the rest of the model" — spacepxl, March 10, 2025

**Similar to Flux control LoRAs:**

There's a diffusers example training script for Flux that uses the same approach:
https://github.com/huggingface/diffusers/tree/main/examples/flux-control

> "works the same way" — spacepxl, March 10, 2025

### Native ComfyUI Support

**Status:** Working as of March 10, 2025

**Requirements:**
- ComfyUI commit ca8efab or later (March 10, 2025)
- Control LoRA v0.2 with `reshape_weight` key

**How it works:**
- LoRA includes a `diffusion_model.patch_embedding.reshape_weight` key
- This key contains the new shape: `torch.tensor([1536, 32, 1, 2, 2])`
- Original shape: `[1536, 16, 1, 2, 2]`
- ComfyUI automatically reshapes the patch embedding to accept concatenated inputs

> "do sd["diffusion_model.patch_embedding.reshape_weight"] = torch.tensor([1536, 32, 1, 2, 2])" — comfy, March 10, 2025

**Loading:**
- Use standard LoRA loader node
- Use InstructPix2Pix conditioning node for control input
- Control latent must be **scaled** (not unscaled)

> "scaled is the correct thing to do always" — comfy, March 10, 2025

> "except on the original ip2p model" — comfy, March 10, 2025

### Kijai Wrapper Support

**Status:** Working with both v0.1 and v0.2

**Features:**
- Automatic handling of reshape weights
- Start/end percentage control for LoRA application
- Compatible with other LoRAs (with caveats)
- Example workflows provided

**Known limitation:** Cannot unload only the control LoRA when using end percentage with multiple LoRAs. The end percentage unloads all LoRAs currently.

> "doesn't work with another lora currently as I don't know how to unload only one LoRA..." — Kijai, March 10, 2025

---

## Usage

### Tile Control Workflow (Native)

**Basic setup:**
1. Load Wan 2.1 T2V 1.3B model
2. Load tile control LoRA v0.2
3. Prepare input video:
   - Resize to target resolution
   - Apply blur (gaussian blur recommended)
4. Encode to latents (scaled)
5. Use InstructPix2Pix conditioning node
6. Sample with appropriate settings

**Recommended settings:**
- Steps: 10-30 (more steps = more detail)
- Denoise: 0.5-0.9 (lower = more faithful to input)
- CFG: 1.0-3.0
- LoRA strength: 1.0 (adjust for creative control)
- Start/end percentage: 0.0-0.1 for early application

**Example workflow:** Provided by spacepxl (March 10, 2025)

### Tile Control Workflow (Wrapper)

**Basic setup:**
1. Load model and LoRA as usual
2. Use control LoRA loader node
3. Set start/end percentages
4. Connect to sampler

**Settings:**
- Start %: 0.0 (apply from beginning)
- End %: 0.1 (stop early for subtle effect)
- LoRA strength: 1.0

> "all my examples are ending it at 0.1" — Kijai, March 10, 2025

> "still so strong at 0.1" — Kijai, March 10, 2025

### Stacking Multiple Controls

**Status:** Experimental, not fully tested

**Potential approaches:**
- Add conditionings together
- Train multi-control LoRAs from the start
- Use separate LoRAs and test compatibility

> "this is a good point, I'm not sure how well they would stack. Might be possible to simply add the conditionings together, but maybe not." — spacepxl, March 10, 2025

**comfy's concern:**

> "those control loras are a good idea but you need to make sure they can be stacked" — comfy, March 10, 2025

**Community testing needed:**

> "has anyone tried stacking the flux depth and canny loras?" — spacepxl, March 10, 2025

No confirmed results on stacking as of March 10, 2025.

**spacepxl's perspective:**

> "IMO one good conditioning signal is better than 3 lousy ones though" — spacepxl, March 10, 2025

---

## Training Control LoRAs

### spacepxl's WanTraining

**Released:** March 10, 2025

**Repository:** https://github.com/spacepxl/WanTraining

**Features:**
- Normal LoRA training
- CFG distillation
- Control LoRA training (tile deblur, depth, pose, etc.)
- Batch size 1 for mixed resolution/frames
- Rank 128 LoRA on 1.3B

> "eh fuckit, I don't have time to document anything right now so excuse the mess, but here's the wip tile loras: https://huggingface.co/spacepxl/Wan2.1-control-loras/tree/main and the training code for normal lora, cfg distillation, and control lora: https://github.com/spacepxl/WanTraining" — spacepxl, March 10, 2025

**Training settings (tile model):**
- Learning rate: 5e-6 for 20k steps, then 1e-5 for 12k steps
- Rank: 128
- Alpha: 128 (alpha = rank)
- Batch size: 1 (enables mixed resolution/frames)
- Frames: 9 ("not that much slower than 1 frame")

> "for the tile model it was 5e-6 for 20k steps then 1e-5 for 12k steps since progress was slowing down" — spacepxl, March 10, 2025

> "I trained on 9 frames mostly, it's not that much slower than 1 frame since there's some constant cost per step" — spacepxl, March 10, 2025

### Tile Deblur Training Process

**Why tile deblur first:**

> "tile deblur was just the easiest to train from a data perspective, but it works just as well with any conditioning signal" — spacepxl, March 10, 2025

> "depth/pose/etc" — spacepxl, March 10, 2025

**Process:**
1. Downscale input to 0.25x
2. Upscale back to original size (bilinear)
3. Apply blur to destroy high-res details
4. Use as control signal for generation
5. Model learns to restore high-res details

**Data requirements:**

> "you can use any control signal you want, as long as it's represented as a image/video, and as long as you have enough data to train on" — spacepxl, March 10, 2025

### Future Control Signals

**Planned by spacepxl:**
- Depth control ("probably next")
- Pose control
- Canny edges
- Normal maps
- Any visual signal representable as image/video

**Community interest:**
- OpenPose
- Depth maps
- Style transfer
- Multi-control combinations

---

## Latent Upscaling Discussion

comfy suggested an alternative approach:

> "also you should try training something that can directly upscale the latent" — comfy, March 10, 2025

> "having it go to pixel space -> upscale and back is not efficient" — comfy, March 10, 2025

**spacepxl's response:**

> "true, but the wan vae is not that bad. All the latent upscale models I've seen aren't that good tbh, a good latent upscaler would probably be heavier than the vae" — spacepxl, March 10, 2025

**Trade-offs:**
- Latent upscaling is more efficient (no VAE encode/decode)
- But existing latent upscalers have quality issues
- A good latent upscaler would be computationally expensive
- Wan VAE is efficient enough that pixel-space upscaling is acceptable

---

## Performance

### Generation Speed

**1.3B tile control:**
- 10 seconds for standard generation (Kijai, March 10, 2025)
- Works with torch.compile
- Compatible with TeaCache and other optimizations

**Comparison to alternatives:**
- Faster than full ControlNet
- Similar speed to base model + LoRA
- Minimal overhead from control conditioning

### Quality

**Tile control results:**
- "crazy good" upscaling from low resolution
- Maintains temporal consistency
- Handles various input types
- Creative vs faithful balance adjustable via denoise

**Comparison to other upscaling methods:**
- More creative than traditional upscalers
- Better temporal consistency than frame-by-frame upscaling
- "closer to like a 'creative upscale'" — Draken, March 10, 2025

---

## Known Issues

### Torch.compile Compatibility

**Issue:** Some users reported issues with torch.compile

**Status:** Mixed reports
- TK_999 initially thought compile was the culprit
- Kijai reported using compile successfully
- May depend on specific setup

> "does this control lora not work with compile?" — TK_999, March 10, 2025

> "hmm I've been using compile now" — Kijai, March 10, 2025

### Control Strength

**Issue:** Control can be too strong, limiting creative freedom

> "the control is too strong yea" — Kijai, March 10, 2025

**Workarounds:**
- Adjust LoRA strength
- Use start/end percentages
- Modify denoise strength
- Adjust blur amount on input

> "would there be any methods to control it's strenght? multiplying the latent doesn't work" — Kijai, March 10, 2025

> "and reducing the LoRA strength breaks it after a point" — Kijai, March 10, 2025

### Multiple LoRA Unloading

**Issue:** Cannot unload only the control LoRA when using end percentage

**Impact:** When stacking control LoRA with other LoRAs, the end percentage unloads all LoRAs

**Status:** Known limitation in wrapper implementation

---

## Comparison to Other Control Methods

| Aspect | Control LoRA | ControlNet | VACE |
|--------|-------------|------------|------|
| **Architecture** | LoRA on base model | Separate control network | Module on base model |
| **Training complexity** | Simple (standard LoRA) | Complex (dual networks) | Complex (module training) |
| **Inference cost** | Low (just LoRA) | High (full control model) | Medium (module) |
| **VRAM usage** | Minimal | Significant | Medium |
| **Flexibility** | High (any control signal) | High (any control signal) | High (multiple controls) |
| **Stacking** | Unknown | Well-established | Native multi-control |
| **Quality** | Excellent (tile) | Proven | Excellent |
| **Native support** | Yes (with reshape_weight) | Yes | Yes |
| **Training time** | Fast | Slow | Slow |

---

## Use Cases

### Tile Deblur / Upscaling

- Restore high-res details from blurred/downscaled input
- Video upscaling workflows
- Detail enhancement
- Creative upscaling

**Workflow:**
1. Generate at low resolution (360p, 480p)
2. Upscale with tile control LoRA
3. Get high-resolution output with enhanced details

> "so you can use this to upscale like 360p to 720p by adding some blur?" — Juampab12, March 10, 2025

### Depth Control (Planned)

- Guide generation with depth maps
- 3D-aware video generation
- Scene structure control

### Pose Control (Planned)

- Character animation from pose sequences
- Motion transfer
- Dance/action videos

### Style Transfer (Future)

> "I think once we have a solid baseline of control models for video it will be easier to generate new paired data for creative training" — spacepxl, March 10, 2025

> "like using depth control to make style transfer examples" — spacepxl, March 10, 2025

---

## Future Development

### comfy's Training Framework

comfy is working on a new training framework that will support control LoRAs:

> "that's actually the direction I want to go in for the comfy trainer project" — comfy, March 10, 2025

> "right now it's just a lora trainer" — comfy, March 10, 2025

**Goals:**
- Model-agnostic control LoRA loading
- Better than current diffusers implementation
- Support for various control signals
- Easier to use than existing tools

**spacepxl's question:**

> "do you think it would be possible to implement the control lora loading in a way that's model agnostic, or does it have to be manually added for each new model? Obviously the conditionng preprocessing could be separate, custom nodes even" — spacepxl, March 10, 2025

comfy confirmed this is the plan for the comfy trainer project.

### Planned Control Signals

- Depth (next priority)
- Pose / OpenPose
- Canny edges
- Normal maps
- Segmentation masks
- Any visual signal representable as image/video

---

## Status and Availability

**Current status (March 10, 2025):**

> "Not ready to share yet, those examples were just from an extremely unoptimized inference script in my training repo" — spacepxl, March 10, 2025

> "I'll share it soon-ish, I want everyone to be able to train their own control models or finetune existing ones" — spacepxl, March 10, 2025

**Available now:**
- Tile control LoRA v0.1 and v0.2
- Training code (WanTraining repository)
- Example workflows

**Planned:**
- ComfyUI integration improvements
- Easy training workflow
- Model-agnostic implementation
- Support for various control signals
- Documentation and tutorials

---

## See Also

- [[lora-training]] — General LoRA training for Wan
- [[vace]] — Alternative control method
- [[wan-2.1]] — Base model for control LoRAs
- [[comfyui]] — Platform for using control LoRAs

## External Resources

- [spacepxl Control LoRAs](https://huggingface.co/spacepxl/Wan2.1-control-loras/) — Available models
- [WanTraining Repository](https://github.com/spacepxl/WanTraining) — Training code
- [Flux Control LoRA Training](https://github.com/huggingface/diffusers/tree/main/examples/flux-control) — Similar approach for Flux
- [InstructPix2Pix](https://github.com/timothybrooks/instruct-pix2pix) — Original concatenated control approach
- [ComfyUI Commit ca8efab](https://github.com/comfyanonymous/ComfyUI/commit/ca8efab79fa19bc9745b4f7346d38a49ba1b1b7c) — Native support for control LoRAs
