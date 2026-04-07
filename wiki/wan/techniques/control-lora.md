---
title: Control LoRAs for Wan
aliases: [control-lora, control-loras, tile-deblur, tile-control, depth-control]
last_updated: 2025-03-19
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

### Depth Control (WIP)

**Released:** March 19, 2025 by spacepxl (WIP version)

**Model:** Wan 2.1 T2V 1.3B

**Purpose:** Depth-based structure and motion control

**Download:** https://huggingface.co/spacepxl/Wan2.1-control-loras/tree/main/1.3b/depth

**Status:** Work in progress — prompt following not always great, needs recaptioning with dense VLM captions

**Training details:**
- Uses Depth Anything V2 Small for depth generation
- Purposely avoided consistent video depth models to learn to ignore flickering
- Training resolutions: 624x624, 832x480 (portrait and landscape)
- Rank: 128

> "Just uploaded a WIP version of depth control lora for 1.3b (+workflow) https://huggingface.co/spacepxl/Wan2.1-control-loras/tree/main/1.3b/depth WIP because the prompt following is not always great. I need to recaption some data with dense VLM captions probably, and continue training. It controls structure and motion quite well though, and with an early step cutoff you can get creative results." — spacepxl, March 19, 2025 [🔥x32 🚀x5 😮x3 🤯 🩵x2]

**Community reception:**
> "bro you're fucking crushing it" — Faust-SiN, March 19, 2025

> "Those examples look really nice!" — pom_x_moq#0, March 19, 2025

> "awesome!" — Kijai, March 19, 2025

**Known quirks:**
- Doesn't like pure black in depth maps — use slightly lifted values
- Works well on square images (624x624) and landscape (832x480)
- Can be used with character LoRAs for combined control
- Prompt following improves with proper captioning

**Depth map preprocessing:**
- Use Depth Anything V2 for generation
- Avoid pure black values (lift to slightly higher values)
- Solid colors can trip it up — use gradients for better results

> "can you try lifting the black to a slightly higher value just to see what happens? I'm curious if it's ok with solid non-black there or if any solid color will trip it up" — spacepxl, March 19, 2025

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

**Native workflow:** Available at https://huggingface.co/spacepxl/Wan2.1-control-loras/blob/main/1.3b/depth/Wan2.1_1.3b_depth_control_lora.json

### Kijai Wrapper Support

**Status:** Working with both v0.1 and v0.2

**Features:**
- Automatic handling of reshape weights
- Start/end percentage control for LoRA application
- Compatible with other LoRAs (with caveats)
- Example workflows provided
- Block dropping support (added March 19, 2025)

**Known limitation:** Cannot unload only the control LoRA when using end percentage with multiple LoRAs. The end percentage unloads all LoRAs currently.

> "doesn't work with another lora currently as I don't know how to unload only one LoRA..." — Kijai, March 10, 2025

**Update (March 19, 2025):** Kijai added the ability to drop blocks from control LoRAs, which may help with compatibility when stacking with other LoRAs.

> "I updated the wrapper to allow dropping blocks from the control lora, that may help" — Kijai, March 19, 2025

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

### Depth Control Workflow

**Basic setup (Wrapper):**
1. Load Wan 2.1 T2V 1.3B model
2. Load depth control LoRA
3. Generate depth maps using Depth Anything V2
4. Use control LoRA loader node
5. Set start/end percentages
6. Connect to sampler

**Recommended settings:**
- **LoRA strength:** 1.0 (default)
- **Start %:** 0.0 (apply from beginning)
- **End %:** 0.1-0.3 (stop early for creative freedom)
- **Steps:** 25-35 (split sigmas: 10 depth + 15-25 refinement)
- **CFG:** 4.0 (first pass), 6.0 (second pass)
- **Sampler:** UniPC recommended

> "all my examples are ending it at 0.1" — Kijai, March 10, 2025

> "still so strong at 0.1" — Kijai, March 10, 2025

**Split sigma workflow:**
- First sampler: Depth control LoRA + character LoRA (10 steps)
- Second sampler: Character LoRA only (15-25 steps)
- This allows structure from depth, then refinement for details

> "depth + custom lora on early steps, then only custom lora on late steps, that's the way" — spacepxl, March 19, 2025

**Combining with character LoRAs:**
- Use depth control + character LoRA on first pass
- Character LoRA only on second pass
- Adjust steps to balance structure vs likeness
- More steps on second pass = better character likeness

> "you should probably use more steps" — melmass#0, March 19, 2025

> "I would also use depth + your lora on the first pass and your lora only on the second" — melmass#0, March 19, 2025

### Depth Control Workflow (Native)

**Requirements:**
- ComfyUI commit ca8efab or later
- All nodes updated
- Depth control LoRA v0.2

**Common error if outdated:**
> "Given groups=1, weight of size [1536, 32, 1, 2, 2], expected input[2, 16, 11, 78, 78] to have 32 channels, but got 16 channels instead"

**Solution:** Update ComfyUI to latest commit (March 10, 2025 or later)

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

**Training settings (depth model):**
- Depth Anything V2 Small for depth generation
- Generated during training (not pre-processed)
- Purposely used flickering depth to teach robustness

> "depth anything v2 small, I purposely avoided any of the more consistent video depth models so it would learn to ignore flickering" — spacepxl, March 19, 2025

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
- Depth control (released WIP March 19, 2025)
- Pose control
- Canny edges
- Normal maps
- Any visual signal representable as image/video

**Community interest:**
- OpenPose
- Depth maps
- Style transfer
- Multi-control combinations
- Camera control for I2V

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

**1.3B depth control:**
- ~20 seconds for 81 frames at 832x480 with all optimizations (Kijai, March 19, 2025)
- 30 steps: 29 seconds (Kijai, March 19, 2025)
- Works with SageAttention, fp16_fast, TeaCache, torch.compile

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

**Depth control results:**
- Controls structure and motion quite well
- Prompt following needs improvement (WIP)
- Works well with early step cutoff for creative results
- Scales up to 640p from training resolution

> "pretty good, pretty good" — Kijai, March 19, 2025

> "especially when these 1.3B gens take like 20 seconds 😄" — Kijai, March 19, 2025

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

**Workaround (March 19, 2025):** Use block dropping feature to reduce control LoRA influence while keeping it loaded

### Depth Map Quirks

**Pure black issue:**
- Depth control doesn't like pure black in depth maps
- Lift black values slightly (e.g., to 10-20 instead of 0)
- Solid colors can trip it up — use gradients

> "it doesn't seem to like pure black much" — Kijai, March 19, 2025

> "yeah I noticed this too, maybe I should do some random clamping in the training since DAv2 will almost never return a solid black" — spacepxl, March 19, 2025

**Inverted depth values:**
- Some users reported needing to invert depth values (black front, white back)
- Check your depth map polarity if results are unexpected

### Character LoRA Compatibility

**Issue:** Character LoRAs may not show through strongly when combined with depth control

**Solutions:**
- Use split sigma workflow (depth + character on first pass, character only on second)
- Increase steps on second pass for better likeness
- Adjust relative LoRA strengths
- Use more steps overall (35+ recommended)

> "I am finding that my lora's don't really shine in combination with depth lora. the clothing is kind of there, but not the face at all" — jasblack#0, March 19, 2025

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
| **Quality** | Excellent (tile, depth WIP) | Proven | Excellent |
| **Native support** | Yes (with reshape_weight) | Yes | Yes |
| **Training time** | Fast | Slow | Slow |
| **Model sizes** | 1.3B only (currently) | Various | 1.3B and 14B |

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

### Depth Control

- Guide generation with depth maps
- 3D-aware video generation
- Scene structure control
- Camera movement control
- Character animation with depth

**Workflow:**
1. Generate or extract depth maps
2. Use depth control LoRA for structure
3. Combine with character LoRAs for identity
4. Refine with second pass

### Pose Control (Planned)

- Character animation from pose sequences
- Motion transfer
- Dance/action videos

### Style Transfer (Future)

> "I think once we have a solid baseline of control models for video it will be easier to generate new paired data for creative training" — spacepxl, March 10, 2025

> "like using depth control to make style transfer examples" — spacepxl, March 10, 2025

### Camera Control for I2V

**Community interest:**
> "Well, you might want to think about controlling the camera in i2v..." — N0NSens, March 19, 2025

**spacepxl's perspective:**
> "fair, although conditioning on camera movement alone without scene structure is a tricky one" — spacepxl, March 19, 2025

> "I think image + pose might be more useful to more people" — spacepxl, March 19, 2025

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

- Depth (released WIP March 19, 2025)
- Pose / OpenPose
- Canny edges
- Normal maps
- Segmentation masks
- Any visual signal representable as image/video

### 14B Support

**Community interest:**
> "Are you thinking about training a 14b depth at all?" — Cubey, March 19, 2025

**spacepxl's response:**
> "t2v maybe, i2v would probably need different considerations because it already has the image and mask inputs" — spacepxl, March 19, 2025

**Considerations for I2V:**
> "tbh, I don't see depth control being that useful for i2v, since you would need a video source for the control, and in that case you can already get great results with flow edit. Maybe I'm wrong though" — spacepxl, March 19, 2025

---

## Status and Availability

**Current status (March 19, 2025):**

**Available now:**
- Tile control LoRA v0.1 and v0.2 (1.3B)
- Depth control LoRA WIP (1.3B)
- Training code (WanTraining repository)
- Example workflows (native and wrapper)

**Planned:**
- Improved depth control with better captioning
- Pose control LoRA
- Canny/lineart control
- 14B versions (T2V)
- ComfyUI training framework integration
- Model-agnostic implementation
- Documentation and tutorials

---

## Community Examples

**Depth control examples (March 19, 2025):**

**Kijai's tests:**
- Flying fish with depth control
- Pikachu with depth control (restless at CFG 3.0)
- Color mask experiments (RGB colors as depth)
- 640p upscaling from training resolution

**melmass#0's tests:**
- Bearded man crying and making grimaces
- Two robots fighting with sparkles and fire
- PlayStation one graphics style
- Red flower growing
- Camera rotating around subjects

**Community feedback:**
> "this is game changing" — Neex, March 19, 2025

> "You think this(training control LoRAs) could also work on hyv" — happy.j, March 19, 2025

> "yes, it could be done if someone wants to train it" — spacepxl, March 19, 2025

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
