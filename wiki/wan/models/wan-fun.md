---
title: Wan 2.1 Fun Models
aliases: [wan-fun, fun-wan, wan2.1-fun, funwanx]
last_updated: 2025-03-30
---

# Wan 2.1 Fun Models

Wan 2.1 Fun is a family of models released by Alibaba PAI (a different branch from the main Wan team) on March 26, 2025. These models are finetunes of Wan 2.1 that add inpainting, start/end frame interpolation, and control capabilities.

> "Unfun WanX is history" — Kijai, March 26, 2025

> "time for FunWanX" — Kijai, March 26, 2025

---

## Overview

The Fun models are based on the CogVideoX-Fun architecture and methodology, adapted for Wan 2.1. They support:

- **Temporal inpainting** (InP models)
- **Start and end frame interpolation** (InP models)
- **Control signals** (depth, pose, canny, mlsd, scribble, trajectory)
- **Image-to-video on 1.3B** (previously only available on 14B)
- **Multiple resolutions** (trained at various resolutions)

**Key difference from base Wan 2.1:** Fun models are inherently I2V models (inpaint architecture), even when doing T2V.

---

## Model Variants

| Model | Size (bf16) | Size (fp8) | Purpose | Channels | HuggingFace ID |
|-------|-------------|------------|---------|----------|----------------|
| **Wan2.1-Fun-1.3B-InP** | ~3.13 GB | ~1.6 GB | Text-to-video, image-to-video, start/end frame | 36 | `alibaba-pai/Wan2.1-Fun-1.3B-InP` |
| **Wan2.1-Fun-14B-InP** | ~46 GB | ~16 GB | Text-to-video, image-to-video, start/end frame | 48 | `alibaba-pai/Wan2.1-Fun-14B-InP` |
| **Wan2.1-Fun-1.3B-Control** | ~3.13 GB | ~1.6 GB | I2V with control (depth, pose, canny, etc.) | 36 | `alibaba-pai/Wan2.1-Fun-1.3B-Control` |
| **Wan2.1-Fun-14B-Control** | ~46 GB | ~16 GB | I2V with control (depth, pose, canny, etc.) | 48 | `alibaba-pai/Wan2.1-Fun-14B-Control` (ModelScope only) |

**Note:** Original releases are in bf16 (not fp32 as initially thought). Kijai provides fp8_e4m3fn conversions.

---

## Architecture Differences

### Channel Count

**Base Wan 2.1:**
- T2V: 16 channels
- I2V: 16 + 20 = 36 channels (image + mask)

**Fun models:**
- 1.3B: 36 channels (inpaint architecture)
- 14B: 48 channels (inpaint architecture)

> "it's 36 channels too so it's I2V" — Kijai, March 26, 2025

### Inpaint Architecture

Fun models use temporal inpainting architecture, meaning they can:
- Generate video from text (T2V mode)
- Generate video from image (I2V mode)
- Interpolate between start and end frames
- Inpaint temporal regions

> "it's a different finetune with their method, supports start/end frame and control signals" — Kijai, March 26, 2025

> "it innately is image 2 video" — Kijai, March 26, 2025

---

## Control Capabilities

### Available Control Types

The Control models support multiple control signals:

- **Depth** — Depth maps for structure control
- **Pose** — Human pose skeletons
- **Canny** — Edge detection
- **MLSD** — Line segment detection
- **Scribble** — Hand-drawn sketches
- **Trajectory** — Motion paths
- **Unprocessed video** — The model is generalized enough to work with raw video as control
- **DensePose** — Works well (Cubey, March 28, 2025)
- **Shuffle** — For experimental/creative effects (IllumiReptilien, March 28, 2025)

> "do we have a list of the possible conditions for the 1.3b? Ive seen: pose, mlsd, depth, canny, trajectory" — mamad8, March 26, 2025

> "it's so generalized you can give it unprocessed videos and it works" — Kijai, March 27, 2025

> "I dunno if anyone explored other preprocessors, but I was surprised to see densepose also worked really well" — Cubey, March 28, 2025

### Built-in Control

Unlike spacepxl's control LoRAs, Fun Control models have built-in control:

> "you can't use the control lora with it" — Kijai, March 26, 2025

> "it doesn't need it anyway" — Kijai, March 26, 2025

> "it has built in control" — Kijai, March 26, 2025

### Control Strength

**Critical:** Control is VERY strong and can be stopped after just a few steps.

> "control is -very- strong and can be stopped after few steps" — Kijai, March 27, 2025

> "just one step with the control and it's still that strong..." — Kijai, March 27, 2025

**Control strength adjustment:**
- Use the `latent_strength` parameter to adjust control strength
- Stop control application early (e.g., after 1-5 steps) for more creative freedom
- The model can handle significant differences between control and desired output

**Trajectory control (March 27, 2025):**

Kijai tested trajectory control:
- Works but snaps to trajectory only after first frame
- Wants to move the camera rather than just the subject
- Can be used for motion paths but requires careful tuning

> "trajectory is doing something" — Kijai, March 27, 2025

> "it wants to move the camera..." — Kijai, March 27, 2025

---

## Implementation

### Kijai Wrapper

**Status:** Implemented March 26, 2025

**Key features:**
- Automatic model variant detection
- Start/end frame support
- Control signal support
- CLIP vision conditioning
- Cross-attention splitting for start/end frames
- Context window support (confirmed working March 27, 2025)
- Block dropping support (added March 19, 2025)

**Usage:**

```
WanVideoModelLoader (Fun variant)
  ↓
WanFunStartEndFrameEncode (for InP models)
  ↓
WanFunControlEncode (for Control models)
  ↓
KSampler
```

**Important:** Control images and reference images must be the same size. The model will error if dimensions don't match.

> "check that the depth anything output is same size" — Kijai, March 26, 2025

**Critical setting for InP models:**

When using the InP models, enable the `fun_model` toggle in the encode node:

> "toggle this too in the encode node that takes the images" — Kijai, March 26, 2025

This affects end frame handling and prevents darkening artifacts.

**Update (March 28, 2025):** Kijai made start_image optional for InP models, which breaks old workflows:

> "I'm making the start_image optional as the InP model works with end image only... this has VERY annoying side effect of screwing up the inputs, so expect old workflows to need adjustment" — Kijai, March 28, 2025

Old workflows will need to reconnect the vae, clip_embeds, and images after this update.

### Native ComfyUI

**Status:** Implemented March 27, 2025

comfy released native support for the Fun Control models:

> "https://github.com/comfyanonymous/ComfyUI/commit/3661c833bcc41b788a7c9f0e7bc48524f8ee5f82" — comfy, March 27, 2025

**Important distinctions:**
- **Control models:** Use the new native node
- **InP models:** Work with regular I2V Wan node (just add end frame support)

> "for the 1.3B and 14B fun control models" — comfy, March 27, 2025

> "not the inpaint ones" — comfy, March 27, 2025

> "inpaint one works with the regular i2v wan node" — comfy, March 27, 2025

---

## CLIP Vision Conditioning

### How It Works

Fun models use CLIP vision embeddings as additional conditioning:

> "it's extra conditioning added to the text cond" — Kijai, March 26, 2025

> "for the whole thing" — Kijai, March 26, 2025

> "so if you use only first frame, it's that for whole video" — Kijai, March 26, 2025

### Start/End Frame Handling

Kijai implemented multiple approaches for handling start/end frames:

1. **Average embeddings** — Average CLIP embeds from start and end frames
2. **Concatenate embeddings** — Concat the embeds
3. **Split cross-attention** — Apply start embed to early frames, end embed to late frames
4. **Split video attention** — Also split self-attention (experimental, very strong)

> "the latest where the cross attn is split into two parts and the start/end clip embeds are only used for their corresponding frames" — Kijai, March 26, 2025

> "now that is not very strong because it's just cross attn, and the video attention smooths it over" — Kijai, March 26, 2025

> "so there's experimental option to also split the video attention... but that is TOO strong and splits the whole thing into 2 diff videos" — Kijai, March 26, 2025

> "so I have option to only do it on certain steps" — Kijai, March 26, 2025

### Tiled CLIP Vision Issues

**Critical:** Tiled CLIP vision can cause severe quality degradation.

> "my tiled clip vision was causing problems" — Kijai, March 26, 2025

Before/after disabling tile in CLIP vision node shows dramatic improvement. Disable tiling or use higher tile ratio.

**Update (March 28, 2025):** Tiled CLIP vision works well with Fun models in concat combine mode:

> "the tiled clip vision actually works good with the Fun models in the concat combine mode" — Kijai, March 28, 2025

**Recommended settings (March 28, 2025):**
- Use 8 tiles in the clip encode node
- Set combine to 'concat'

> "try doing 8 tiles in the clip encode node, with the combine set to 'concat'" — Kijai, March 28, 2025

---

## Performance

### Speed Comparison

**1.3B InP vs base 1.3B:**
- Similar speed for T2V
- I2V now available on 1.3B (previously 14B only)

**14B InP vs base 14B:**
- ~200 seconds slower than base Wan 14B (H（4090）, March 26, 2025)
- Still usable but noticeably slower

> "It's 200 seconds slower than WAN" — H（4090）, March 26, 2025

**1.3B Control:**
- 1 minute without TeaCache (832x480x49f)
- 44 seconds with TeaCache
- ~30 seconds with all optimizations (March 27, 2025)
- 10 steps: Very fast (VK, March 29, 2025)

— ArtOfficial, March 26, 2025

**14B Control:**
- ~30 minutes for 81 frames at 832x480 (VK, March 27, 2025)
- "a few minutes on a 5090" (852話, March 27, 2025)
- **4 steps:** Surprisingly good results with low motion (Kijai, March 27, 2025)
- **1 step:** Works but quality varies (Kijai, March 27, 2025)

**Low-step generation (March 27-28, 2025):**

Kijai discovered that the Fun Control models can generate usable output with very few steps:

- **1 step:** Works, especially with low motion
- **2 steps:** Better quality
- **4 steps:** "surprisingly good" for low motion content
- **6 steps:** High quality

> "huh, with only 4 steps gets this much" — Kijai, March 27, 2025

> "1 step...." — Kijai, March 27, 2025

> "still very curious it just can do 1 step at all" — Kijai, March 27, 2025

**Important caveat:** Low-step generation only works well with low motion. High motion content requires more steps.

> "yeah but only really works with low motion" — Kijai, March 27, 2025

**Alternative to low steps:** Aggressive TeaCache can be "even better and safer" than 1-4 step generation.

> "honestly can also just use aggressive TeaCache and that's even better and safer" — Kijai, March 27, 2025

### VRAM Requirements

| Model | bf16 | fp8 | Minimum VRAM |
|-------|------|-----|-------------|
| 1.3B InP | ~3.13 GB | ~1.6 GB | 8 GB |
| 1.3B Control | ~3.13 GB | ~1.6 GB | 8 GB |
| 14B InP | ~46 GB | ~16 GB | 24 GB (with block swap) |
| 14B Control | ~46 GB | ~16 GB | 24 GB (with block swap) |

**4090 limits (March 28, 2025):**

> "max for 4090 without offloading is about 81 frames at 832x480" — Kijai, March 28, 2025

**1.3B Model Tests (March 30, 2025):**

VK tested various frame counts at 1280x768:
- **41 frames:** Sweet spot for speed/quality balance
- **Beyond 41 frames:** Time increases disproportionately

> "Sweet spot seems to be 41 frames. Then time increases disproportionately." — VK, March 30, 2025

---

## Quality Impact vs Speed Trade-offs

### InP Model Quality Concerns

Multiple users reported that the InP models (especially 1.3B) produce lower quality than the original Wan 2.1 I2V:

> "I don't know about the 1.3B InP quality, just feels off?" — Kijai, March 27, 2025

> "1.3b inp is far worse than 14b" — Excai, March 27, 2025

> "the 14B old I2V is absolutely better than the 1.3B InP I2V... probably also better than the 14B one" — Kijai, March 27, 2025

> "I was not convinced by the 14B Inp" — IllumiReptilien, March 27, 2025

**However:** The demo on HuggingFace shows better quality than local generations, suggesting settings/scheduler issues:

> "demo seemed pretty decent to me, much better than native, which suggests something is off" — David Snow, March 27, 2025

**Kijai's investigation:**

> "something has to be off with the scheduler in the wrapper" — Kijai, March 27, 2025

> "can't possibly get same quality using euler" — Kijai, March 27, 2025

Kijai fixed issues with the Euler scheduler on March 27, 2025:

> "something was definitely off with my euler, at least that's much better now" — Kijai, March 27, 2025

> "and by my I mean the original code 😅" — Kijai, March 27, 2025

### Control Model Quality

The Control models received much more positive reception:

> "the fun 14B control is, indeed, really fun 😂" — IllumiReptilien, March 27, 2025 [🔥x7 😆x6]

> "I tried your workflow with 1.3B and didn't see any major differences from what you did on the 14B model 👀" — DiXiao, March 27, 2025

**Key insight from Kijai (March 27, 2025):**

> "the interestring thing is the control model" — Kijai, March 27, 2025

> "and start/end frame" — Kijai, March 27, 2025

> "we are spoiled by the amazing I2V the initial model can do" — Kijai, March 27, 2025

**Community concerns (March 30, 2025):**

Some users found the control models less impressive than expected:

> "yeah the control thing seems not that good" — aikitoria, March 30, 2025

> "it's way worse than what was promised (and never delivered) for hunyuan" — aikitoria, March 30, 2025

---

## Optimization Compatibility

### TeaCache

**Status:** Works, but coefficients may not be optimal

> "we don't know if the TeaCache coefficients will work as these are new models" — Kijai, March 26, 2025

> "teacache works with them" — JmySff, March 26, 2025

**Recommended settings:**
- **1.3B InP:** threshold 0.010 (JmySff, March 26, 2025)
- **1.3B Control:** threshold 0.080 (Kijai example workflow, March 28, 2025)
- **14B InP:** threshold 0.220 (Kijai example workflow, March 28, 2025)
- **14B Control:** Unknown, needs testing

**Note:** Control models can handle more aggressive TeaCache due to their ability to work with very few steps.

### Torch.compile

**Status:** Partially working

> "torchcompile is a bit complicated with native and these models" — JmySff, March 26, 2025

Some users report torch.compile works, others encounter errors. May depend on specific setup.

### SLG (Skip Layer Guidance)

**Status:** Mixed results

SLG behavior differs between InP and Control models:

> "it seems that, in wan2.1fun 1.3binp, w/o SLG maybe better" — Excai, March 26, 2025

**Recommendations:**
- For 1.3B InP: SLG may not help or may hurt quality
- For 14B Control: SLG works well (block 8-10, end 0.3)
- Start SLG later (block 8) for Fun models
- Can be higher on longer videos

> "it works fine, just start it bit later, block 8" — Kijai, March 26, 2025

### CFG Zero Star

**Status:** Works

> "still Inp 1.3B, same settings but with Zero Star" — JmySff, March 26, 2025

CFG Zero Star is compatible with Fun models and provides quality improvements.

### Enhance-a-Video

**Status:** Unknown, needs testing

### fp8_fast

**Status:** No improvement over standard fp8

> "fp8 fast isn't any better on this" — Kijai, March 26, 2025

### Base Precision

**Critical:** Fun models were released in bf16, not fp16.

> "one major thing to note is that the Fun models were only released in bf16" — Kijai, March 28, 2025

> "so if not using quantization, should not use fp16 base precision" — Kijai, March 28, 2025

Using fp16_fast with bf16 models is lossy:

> "haven't really compared, but it's lossy at least" — Kijai, March 28, 2025

---

## Known Issues

### Size Mismatch Errors

**Problem:** Control images and reference images must be exactly the same size.

**Error message:**
```
RuntimeError: Sizes of tensors must match except in dimension 1
```

**Solution:** Ensure all images (reference, depth, control) are resized to identical dimensions before encoding.

> "did you resize everything to same size?" — Kijai, March 26, 2025

> "control images and reference image" — Kijai, March 26, 2025

### Channel Count Errors

**Problem:** Using control LoRAs with Fun models causes channel mismatch.

**Error message:**
```
expected 32 channels, got 36 channels
```

**Solution:** Don't use spacepxl's control LoRAs with Fun models. Fun has built-in control.

> "you can't use the control lora with it" — Kijai, March 26, 2025

### T2V Mode Not Yet Implemented

**Problem:** T2V mode for Control models not yet implemented in wrapper.

> "or are you trying to do T2V? I didn't add logic for that yet" — Kijai, March 26, 2025

**Status:** I2V works, T2V pending implementation.

**Update (March 27, 2025):** T2V with InP model now works:

> "oh and just now fixed the T2V with the inp model" — Kijai, March 27, 2025

### Ghosting/Artifacts

**Problem:** Some users report ghosting or strange artifacts.

**Possible causes:**
- Tiled CLIP vision enabled (disable it)
- Incorrect control image preprocessing
- Model still being tested

> "out of the box with the old code with the 1.3B inp, kinda weird" — Kijai, March 26, 2025

### bf16 Format

**Issue:** Models released in bf16, not fp16.

> "also very annoying this is bf16" — Kijai, March 26, 2025

This is unusual for Wan models. Use fp8 conversions for better performance, or set base precision to bf16 when using the 1.3B models.

### Darkening Effect on End Frame

**Problem:** End frame appears darkened in some workflows.

**Cause:** Old masking method in the encode node.

**Solution:** Enable the `fun_model` toggle in the encode node that takes images:

> "toggle this too in the encode node that takes the images" — Kijai, March 26, 2025

> "I fixed the code" — Kijai, March 26, 2025

> "the dark frame is from the old method" — Kijai, March 26, 2025

### LoRA Compatibility Issues

**Problem:** LoRAs don't work well with Fun models.

**Status (March 27, 2025):**
- 14B LoRAs: Some users report they work when strength is increased to 2.0
- 1.3B LoRAs: Generally don't work or are very weak
- Character LoRAs: May destroy image composition instead of helping

> "I made a 14B lora, and it seems to make a difference on the result when bumped two strenght." — Impactframes, March 27, 2025

> "loras aren't working on that so I'm guessing 14b" — dawniii#0, March 27, 2025

**Kytra's experience:**

> "works well enough but my loras are destroying the image composition instead of helping it now" — Kytra, March 26, 2025

> "same gen but with my loras turned off" — Kytra, March 26, 2025

**Update (March 30, 2025):** Benjimon created a conversion script for LoRAs:

> "https://github.com/maybleMyers/H1111/blob/main/funconvert_lora.py I think it worked testing it now" — Benjimon, March 30, 2025

> "It did work 😄 that script only works for lora in musubi format btw" — Benjimon, March 30, 2025

The script removes incompatible patch_embedding weights to allow LoRAs trained on base Wan to work with Fun models.

### End Frame Not Working with Control Model

**Problem:** Control model does not work with end frame.

**Status (March 27-28, 2025):**

> "the control model does not like end image... it just doesn't work" — Kijai, March 27, 2025

> "control only seems to work with first frame no matter what I tried" — Kijai, March 28, 2025

The InP model works with start, end, or both frames, but the Control model only works with the start frame.

### Start Image Optional (March 28, 2025)

**Breaking change:** Kijai made start_image optional for InP models, which breaks old workflows.

> "I'm making the start_image optional as the InP model works with end image only... this has VERY annoying side effect of screwing up the inputs, so expect old workflows to need adjustment" — Kijai, March 28, 2025

Old workflows will need to be updated to work with the new node structure.

### End Frame Interpolation Issues

**Problem:** End frame is not properly interpolated, just appended at the end.

**Status (March 30, 2025):**

Multiple users reported issues with end frame interpolation:

> "Why is Wan totally ignoring my end frame? It just appends it at the end but doesn't interpolate" — PirateWolf, March 30, 2025

> "the last frame in the generated clips deviates alot from the actual end frame input. its blurred, sometimes the colors are very different, washed out and just overall kinda weird" — seitanism#0, March 29, 2025

**Workaround:** Use base Wan 2.1 I2V 480p instead of Fun InP for better start/end frame interpolation:

> "when you use start + end frame, the normal wan is better?" — seitanism#0, March 29, 2025

> "Yeah, it's the best for sure" — ArtOfficial, March 29, 2025

### Control Strength Too High

**Problem:** Control is too strong and limits creative freedom.

**Status (March 30, 2025):**

Users reported difficulty controlling the strength of control embeds:

> "is there any way i can control the strenght of the control embeds?" — 3Dmindscaper2000, March 30, 2025

**Solutions:**
- Adjust `latent_strength` in the video encode node
- Adjust `end_percent` of the control embed

> "that's what latent strength does in the encode node" — dawniii#0, March 30, 2025

> "That and the end percent indeed" — Kijai, March 30, 2025

### Reference Image Mismatch

**Problem:** Generated video feels unrelated to reference image when using control.

**Cause:** Control pose is too far from the reference pose.

**Solution:**

> "The pose is too far from the reference pose to work properly like that, you can try reducing the control latent strength and/or the end percent of the control embed" — Kijai, March 30, 2025

**Alternative approach (March 30, 2025):**

BondoMan and CJ suggested using the first frame of the control video to generate a matching reference image:

> "You should use the 1st frame of the video to generate a image with SDXL/Flux/SD3 or w/e using the 1st frame for controlnet (OpenPose, DepthMap, Canny, or w/e you think gives best results). You can then use the frame you generated as the start-frame to animate the whole video" — BondoMan, March 30, 2025

---

## Use Cases

### Start/End Frame Interpolation

Generate smooth transitions between two keyframes:

1. Provide start frame
2. Provide end frame
3. Model interpolates between them

Useful for:
- Animation workflows
- Keyframe-based generation
- Controlled motion sequences

**Quality note:** Some users report the end frame is only "barely hit for a frame, but not completely" (TK_999, March 26, 2025).

**Update (March 30, 2025):** spacepxl discovered that using multiple start frames (5 frames instead of 1) significantly improves video extension:

> "wan2.1-fun-1.3B-InP works really well with multiple frames instead of just 1 as start condition. These are the exact same seed and everything, just 1 start frame vs 5 start frames, extending the video from the same point" — spacepxl, March 30, 2025

This allows the model to carry motion forward more naturally.

### Temporal Inpainting

Inpaint regions of video over time:

1. Provide reference video
2. Provide mask
3. Model inpaints masked regions

Useful for:
- Object removal
- Background replacement
- Creative editing

### Control-Guided Generation

Generate video following control signals:

1. Provide control map (depth, pose, etc.)
2. Optionally provide reference image
3. Model follows control structure

Useful for:
- 3D-to-video workflows
- Pose-driven animation
- Depth-guided generation
- **Stylized animation from real footage** (major use case)

**Example workflow (March 27, 2025):**

852話 demonstrated using depth control + stylized first frame to create anime-style video from real footage:

> "I created a sample video by using a gray low-poly image in Midjourney and running it on Vidu. I edited the first floor using Midjourney." — 852話, March 27, 2025

The workflow: Real video → Depth map → Stylized first frame → Fun Control → Stylized video

> "this is image to video with depth control???????" — Juan Gea, March 27, 2025

> "not only depth.. can be about anything as control" — Kijai, March 27, 2025

**Community reaction:**

> "As an animator I have been waiting for this for sooo long... what a time to be alive." — penguinbox#0, March 27, 2025

> "Those examples look really nice!" — pom_x_moq#0, March 27, 2025

> "awesome!" — Kijai, March 27, 2025

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

### 1.3B I2V

Fast image-to-video on consumer GPUs:

> "1.3b i2v model" — slmonker(5090D 32GB), March 26, 2025 [💯x7 ❤️x3]

Previously, I2V required 14B model. Now available on 1.3B for much faster generation.

### Split Prompts with Control (March 28, 2025)

Kijai demonstrated split prompt functionality with control:

> "split prompt with control" — Kijai, March 28, 2025

Example: "waterfall in the 2nd prompt"

This allows different prompts for different parts of the video while maintaining control structure.

---

## Comparison to Base Wan 2.1

| Aspect | Base Wan 2.1 | Fun Models |
|--------|-------------|------------|
| **Architecture** | T2V or I2V | Inpaint (I2V-based) |
| **1.3B I2V** | No | Yes |
| **Start/End frames** | No (workarounds only) | Native support |
| **Control** | LoRAs only | Built-in |
| **Speed (14B)** | Faster | ~200s slower |
| **Image following** | Good | Better (less color shift) |
| **Temporal coherence** | Excellent | Excellent |
| **I2V quality (1.3B)** | N/A | Lower than 14B base I2V |
| **I2V quality (14B)** | Excellent | Lower than base (community consensus) |
| **Control quality (14B)** | N/A | Mixed (excellent for some, disappointing for others) |
| **LoRA compatibility** | Excellent | Poor to mixed (conversion script available) |
| **Low-step generation** | Not viable | Works (1-4 steps with control) |
| **Multi-frame start conditioning** | No | Yes (5+ frames for better extension) |

**Key insight:** The Control models are the standout feature, while the InP models are considered inferior to base Wan 2.1 I2V for pure image-to-video work.

> "the interestring thing is the control model" — Kijai, March 27, 2025

> "and start/end frame" — Kijai, March 27, 2025

> "we are spoiled by the amazing I2V the initial model can do" — Kijai, March 27, 2025

---

## Training

### Character LoRAs

**Community reports:**

> "I had good results when training characters with the 14B but damn I can't get it to work on the 1.3B" — mamad8, March 26, 2025

1.3B Fun may be more difficult to train character LoRAs on compared to 14B Fun or base Wan 2.1.

### Compatibility with Base Wan LoRAs

**Status:** Conversion script available (March 30, 2025)

Benjimon created a script to convert base Wan LoRAs to Fun format:
- **Repository:** https://github.com/maybleMyers/H1111/blob/main/funconvert_lora.py
- **Format:** Works with Musubi-format LoRAs
- **Method:** Removes incompatible patch_embedding weights

> "It did work 😄 that script only works for lora in musubi format btw" — Benjimon, March 30, 2025

**Layer differences:**
```
Layers with shape mismatches (1):
  - patch_embedding.weight:
      i2v_14B: (5120, 36, 1, 2, 2) (737,280 params)
      i2v_14B_FC: (5120, 48, 1, 2, 2) (983,040 params)
      Param diff: +245,760

Total common layers with identical shapes: 1094
```

### Training on Fun Models

**Status (March 27, 2025):** Kytra successfully started training on the Fun Control 1.3B model:

> "I got diffusion-pipe to start training on the control_fun 1.3B model with the correct amount of channels, just now have to see what happens and determine how to fix the loss being so high" — Kytra, March 26, 2025

> "loss trending down significantly but still not sub 1.0" — Kytra, March 26, 2025

**Kohya Musubi support (March 28, 2025):**

> "General heads up: Kohya added a PR and has branch for training the 14b Fun control model: https://github.com/kohya-ss/musubi-tuner/tree/wan21-fun-control" — JohnDopamine, March 28, 2025

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

**1.3B Fun I2V (March 29-30, 2025):**
- 10 steps: Very fast (VK, March 29, 2025)
- 20 steps at 1280x768: 7.5 minutes (VK, March 30, 2025)
- 41 frames: Sweet spot for speed/quality balance
- Beyond 41 frames: Time increases disproportionately

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

## Community Reception

**Highly positive:**

> "It's both a blessing and a curse to wake up to 300 messages in this channel" — Faust-SiN, March 26, 2025

> "you literally can't get 8 hours of sleep without falling drastically behind on Wan" — Eclipse, March 26, 2025

**Key excitement:**
- 1.3B I2V finally available
- Built-in control (no LoRAs needed)
- Start/end frame interpolation
- Temporal coherence improvements
- **Stylized animation from real footage** (major breakthrough)
- **Low-step generation** (1-4 steps with control)
- **Multi-frame start conditioning** for better video extension

**Concerns:**
- Slower than base Wan (14B)
- bf16 format instead of fp16
- Optimization compatibility unclear
- Documentation sparse (CogVideoX-based)
- InP models inferior to base Wan 2.1 I2V
- LoRA compatibility issues (conversion script now available)
- Control quality mixed (excellent for some, disappointing for others)

**Animation community reaction:**

> "As an animator I have been waiting for this for sooo long... what a time to be alive. Thank you Kijai for making all this possible. You truly are outstanding and such an inspiration for me and this community! ❤️" — penguinbox#0, March 27, 2025

> "I don't deserve the credit for that, we should be thankful for alibaba for open sourcing so much" — Kijai, March 27, 2025

---

## HuggingFace Spaces

Official demo spaces:

- **1.3B InP:** https://huggingface.co/spaces/alibaba-pai/Wan2.1-Fun-1.3B-InP
- **14B InP:** Not yet available

**Limitations:**
- 512px max resolution
- 29 frame limit
- Queue during high usage

> "the 29 frame limitation is even more savage" — David Snow, March 26, 2025

Despite limitations, early testing shows strong results:

> "even with all these limitations, I can already tell this model is going to be 🔥" — David Snow, March 26, 2025

**Demo quality vs local:**

Multiple users noted the HuggingFace demo produces better quality than local generations:

> "demo seemed pretty decent to me, much better than native, which suggests something is off" — David Snow, March 27, 2025

This led to Kijai investigating and fixing scheduler issues.

---

## Code and Documentation

### Official Repository

**CogVideoX-Fun repo:** https://github.com/aigc-apps/VideoX-Fun/tree/main/comfyui

> "the code is in their cogvideox-fun repo" — Kijai, March 26, 2025

> "spent an hour figuring out how to use the control model through all that" — Kijai, March 26, 2025

**Note:** Code is described as "one huge mess" by Kijai. ComfyUI implementation is cleaner.

**Installation issues:**

The official repo requires downloading the entire model folder (19GB) even if you already have the models:

> "You'll have to download the whole repo (unfortunately 19gb, even if you have the other models) to ComfyUI/models/Fun_models." — penguinbox#0, March 27, 2025

**Recommendation:** Use Kijai wrapper or native ComfyUI instead:

> "yeah.... or just use my wrapper 😛" — Kijai, March 27, 2025

> "or comfy native" — Kijai, March 27, 2025

> "no reason to use that repo really" — Kijai, March 27, 2025

### Model Naming

> "didn't even bother renaming anything?" — Kijai, March 26, 2025

Fun models retain CogVideoX naming conventions in code, which can be confusing.

---

## Context Windows

**Status:** Working (confirmed March 27, 2025)

> "context windows do work, so there's no length limit" — Kijai, March 27, 2025

> "well at least with T2V..." — Kijai, March 27, 2025

> "actually not sure if they work when using reference image" — Kijai, March 27, 2025

**Interesting behavior:**

> "however this model doesn't seem to break when it gets black image as cond.... in fact that's how the T2V works with the InP model" — Kijai, March 27, 2025

This suggests the InP model is more flexible with conditioning than expected.

**Long generation example (March 28, 2025):**

Kijai generated 228 frames with context windows:

> "'hands' (228 frames with context windows)" — Kijai, March 28, 2025

---

## Timeline

| Date | Event |
|------|-------|
| **March 26, 2025** | Wan 2.1 Fun models released by Alibaba PAI |
| **March 26, 2025** | Kijai implements wrapper support |
| **March 26, 2025** | Community testing begins |
| **March 26, 2025** | Kijai releases fp8 conversions |
| **March 26, 2025** | SLG incompatibility discovered |
| **March 26, 2025** | TeaCache compatibility confirmed |
| **March 26, 2025** | LoRA compatibility issues identified |
| **March 27, 2025** | Kijai fixes Euler scheduler issues |
| **March 27, 2025** | comfy releases native support for Control models |
| **March 27, 2025** | Context window support confirmed |
| **March 27, 2025** | Animation community embraces stylized control workflow |
| **March 27, 2025** | Low-step generation discovered (1-4 steps with control) |
| **March 27, 2025** | Trajectory control tested |
| **March 28, 2025** | Start image made optional for InP models (breaking change) |
| **March 28, 2025** | Tiled CLIP vision confirmed working with concat mode |
| **March 28, 2025** | Split prompts with control demonstrated |
| **March 28, 2025** | Kohya Musubi adds Fun Control training support |
| **March 28, 2025** | DensePose and Shuffle preprocessors confirmed working |
| **March 29, 2025** | End frame interpolation issues widely reported |
| **March 30, 2025** | Benjimon releases LoRA conversion script |
| **March 30, 2025** | spacepxl discovers multi-frame start conditioning for better extension |
| **March 30, 2025** | VK identifies 41 frames as sweet spot for 1.3B at 1280x768 |

---

## See Also

- [[wan-2.1]] — Base model that Fun is built on
- [[control-lora]] — Alternative control method (not compatible with Fun)
- [[comfyui]] — Platform for running Fun workflows
- [[quantization]] — fp8 conversions for Fun models
- [[vace]] — Alternative control system for Wan 2.1

## External Resources

- [Wan2.1-Fun-1.3B-InP](https://huggingface.co/alibaba-pai/Wan2.1-Fun-1.3B-InP)
- [Wan2.1-Fun-14B-InP](https://huggingface.co/alibaba-pai/Wan2.1-Fun-14B-InP)
- [Wan2.1-Fun-1.3B-Control](https://huggingface.co/alibaba-pai/Wan2.1-Fun-1.3B-Control)
- [Wan2.1-Fun-14B-Control (ModelScope)](https://modelscope.cn/models/PAI/Wan2.1-Fun-14B-Control/files)
- [Kijai fp8 Conversions](https://huggingface.co/Kijai/WanVideo_comfy)
- [CogVideoX-Fun Repository](https://github.com/aigc-apps/VideoX-Fun)
- [HuggingFace Space Demo](https://huggingface.co/spaces/alibaba-pai/Wan2.1-Fun-1.3B-InP)
- [Kohya Musubi Fun Control Branch](https://github.com/kohya-ss/musubi-tuner/tree/wan21-fun-control)
- [LoRA Conversion Script](https://github.com/maybleMyers/H1111/blob/main/funconvert_lora.py)
