---
title: VACE (Video Anything ControlNet Enhancement)
aliases: [vace, vace-2.1, vace-2.2, fun-vace, vace-1.3b, vace-14b]
last_updated: 2025-04-06
---

# VACE (Video Anything ControlNet Enhancement)

VACE is a unified video control system from Alibaba (ali-vilab) that adds style transfer, inpainting, outpainting, subject-driven generation, and pose/depth control to the [[wan-2.1]] and [[wan-2.2]] model families. Unlike traditional ControlNets, VACE bundles reference images, control signals, and masks into a single conditioning system. It is architecturally a set of extra blocks (the "Context Embedder" and "Context Blocks") added alongside a frozen T2V DiT model -- the base model weights are never modified, which means existing [[lora|LoRAs]] trained on the base model continue to work.

A 1.3B preview was available by early April 2025, with official 1.3B and 14B versions released on May 14, 2025. A Wan 2.2 "Fun VACE" variant followed later.

> "VACE is basically just a controlnet on top of an unmodified T2V model, so T2V LoRAs work incredibly well. A trained LoRA will almost always beat image references." -- spacepxl, Discord #wan_chatter, December 2025

**Major Update (April 3, 2025):** Kijai released a standalone VACE module that can be loaded separately from the base model, saving 6GB disk space. The original VACE release bundled the full 1.3B model with VACE blocks, but the base model was never actually trained -- it was just the standard 1.3B fp32 model.

**Major Memory Optimization (April 6, 2025):** Kijai significantly reduced VACE memory usage by removing redundant tensor conversions. 832x480x81 now fits in ~12GB VRAM without any offloading, down from previous ~15GB+ requirements.

---

## Setup & Requirements

### Model Files

VACE comes in two forms:

1. **Standalone VACE module** -- Only the VACE blocks, loaded alongside a separate Wan T2V base model. This approach allows swapping base models freely and saves disk space.
2. **Merged VACE model** -- The VACE blocks baked into a full Wan T2V checkpoint. Simpler to use but less flexible and larger file size.

**Standalone VACE module (recommended as of April 3, 2025):**
- **HuggingFace:** `Kijai/WanVideo_comfy/blob/main/Wan2_1_VACE_1_3B_preview_bf16.safetensors`
- **Size:** ~1.5 GB (VACE blocks only)
- **Usage:** Load with WanVideo VACE Model Select node alongside any 1.3B T2V model
- **Advantage:** Works with any 1.3B model including DG (DiffSynth) distilled variants

Kijai provides converted modules in multiple formats:

| Format | 14B Size | Notes |
|--------|----------|-------|
| bf16 | ~6 GB | Best quality, needs ~40 GB VRAM without offloading |
| fp8_e4m3fn | ~3 GB | Good balance, recommended for most setups |
| fp8_e5m2 | ~3 GB | Alternative fp8 format |
| GGUF Q8_0 | ~3.5 GB | For GGUF-compatible loaders |
| GGUF Q4_K_M | ~2 GB | Lowest VRAM option |

**Key model repositories:**

- Original 1.3B preview: `ali-vilab/VACE-Wan2.1-1.3B-Preview`
- Standalone VACE module: `Kijai/WanVideo_comfy/blob/main/Wan2_1_VACE_1_3B_preview_bf16.safetensors`
- Official VACE: `ali-vilab/VACE`
- Kijai fp8 modules: `Kijai/WanVideo_comfy_fp8_scaled/tree/main/VACE`
- Kijai bf16 modules: `Kijai/WanVideo_comfy/tree/main/Fun/VACE` (2.2) and `Kijai/WanVideo_comfy` (2.1)
- Kijai GGUF modules: `Kijai/WanVideo_comfy_GGUF/tree/main/VACE`
- Fun VACE 2.2 original: `alibaba-pai/Wan2.2-VACE-Fun-A14B`
- Fun VACE 2.2 GGUF: `QuantStack/Wan2.2-VACE-Fun-A14B-GGUF`
- FusionX VACE (distilled merge): `QuantStack/Wan2.1_T2V_14B_FusionX_VACE`
- Phantom-VACE merge: `orabazes/wan-14B_vace_phantom_v2_GGUF`

### VRAM Requirements

**Updated April 6, 2025:** Kijai's memory optimizations significantly reduced VRAM usage.

| Configuration | Resolution | Frames | VRAM | Notes |
|--------------|-----------|--------|------|-------|
| 1.3B fp32 + VACE | 832x480 | 81 | **~12 GB** | After April 6 optimizations, no offloading |
| 1.3B fp32 + VACE | 512x512 | 57 | **~7.7 GB** | After April 6 optimizations |
| 1.3B fp32 + VACE | 640x480 | 53 | **~6.2 GB** | After April 6 optimizations, with block swap |
| 1.3B fp32 + VACE | 1024x1024 | 81 | ~13 GB | With offloading |
| 1.3B + VACE | 960x960 | 60 | ~10 GB | With VACE block swap 15, normal block swap 27 |
| 14B fp8 + VACE module | 832x480 | 81 | ~16 GB | With block swap |
| 14B fp8 + VACE module | 720p | 81 | ~20-24 GB | Block swap 40 base + 5 VACE |
| 14B bf16 + VACE bf16 | Any | Any | ~40 GB | Without optimization |
| Wan 2.2 dual model + VACE | 720p | 81 | 12-16 GB | fp8 modules, 32 GB system RAM |
| VACE + Phantom merge | 832x480 | 121 | ~12 GB | fp8, on RTX 3060 |

**Memory optimization details (April 6, 2025):**

Kijai discovered that the original VACE code performed redundant tensor conversions:

> "this VACE code has made no sense to me since the beginning... it just seems to do lots of redundant stuff" — Kijai, April 6, 2025

> "now I'm getting identical results, faster, with far less memory used by removing some pointless conversions to tensors and back" — Kijai, April 6, 2025

Before optimization:
- 832x480x57: Max reserved memory: 8.688 GB
- 832x480x57: Max reserved memory: 9.906 GB

After optimization:
- 832x480x57: Max reserved memory: 5.938 GB
- 832x480x57: Max reserved memory: 5.875 GB
- 832x480x81: Max reserved memory: 6.219 GB

> "832x480x81 fits around 12GB now without any offloading" — Kijai, April 6, 2025

> "this gives hope with running the 14B VACE locally when that comes out" — Kijai, April 6, 2025

The optimization keeps results in a list rather than stacking to tensor and unbinding, eliminating unnecessary memory allocations.

**Block swap settings for VRAM management:**

| VRAM | Base blocks to swap | VACE blocks to swap |
|------|--------------------|--------------------||
| 8-12 GB | 27-40 | 5-15 |
| 16 GB | 20-30 | 3-5 |
| 24 GB | 8-15 | 1-3 |
| 48+ GB | 0 | 0-1 |

Setting at least 1 VACE block to swap enables RAM offloading of VACE intermediate results, which saves a lot of VRAM with only slight speed loss. -- Kijai, Discord #wan_chatter, May 2025

**System RAM:** 32 GB minimum. 64 GB recommended for long videos. 128 GB ideal if running multiple models simultaneously.

### ComfyUI Setup

VACE was initially used through the **Kijai WanVideoWrapper**, with **native ComfyUI node** support added later. Native support was still evolving and users reported mixed memory/offloading behavior; the wrapper remained important for modular workflows.

**Critical:** VACE only works with **T2V models** (16 input channels). It will not work with I2V models. -- Discord #wan_chatter, confirmed by multiple users (Kijai, dawniii, MilesCorban)

**Important:** Some users reported issues when mixing precision between VACE modules and the base model (e.g., bf16 VACE with fp8 base). Matching formats may help avoid degraded results (not widely confirmed).

**Custom node packs:**
- `ComfyUI-WanVaceAdvanced` (drozbay/Ablejones) -- Advanced VACE nodes with detailer integration, per-frame strength control, tiling support
- `ComfyUI-SuperUltimateVaceTools` -- Utility nodes for VACE workflows
- `ComfyUI-WanVideoWrapper` (Kijai) -- The original wrapper with VACE support

**Standalone VACE Loading (April 3, 2025):**

Kijai added a "WanVideo VACE Model Select" node that allows loading the standalone VACE module separately from the base model:

1. Load your base 1.3B T2V model (standard, DG distilled, or any variant)
2. Load the standalone VACE module with the VACE Model Select node
3. Connect both to the VACE encode node

This approach:
- Saves 6GB disk space (no redundant base model)
- Works with any 1.3B T2V model
- Allows testing VACE with distilled models like DG variants
- Quantization/precision options on the model loader apply to VACE

---

## Key Settings

| Parameter | Recommended Value | Notes |
|-----------|------------------|-------|
| **VACE encode strength** | 0.4-0.8 (general), 1.5 (for pose following) | Lower values preserve creative freedom, higher values increase control fidelity. Strength >1.0 boosts likeness but causes contrast/darkening |
| **VACE start_percent** | 0.0 | When to begin applying VACE |
| **VACE end_percent** | 0.5-1.0 | When to stop applying VACE. Can end at 0.5 for faster generation |
| **Steps** | 10-30 | 10 steps works well, 30 for higher quality. 60-75+ for very dynamic scenes |
| **CFG** | 2.0-6.0 | Standard Wan settings. CFG 1.0 works with distilled models |
| **Sampler** | uni_pc / euler | uni_pc is the Wan Team default; dpmpp_2m_sde slightly better for detail |
| **Scheduler** | simple / beta | flowmatch_distill when using Lightning LoRA with Fun VACE |
| **Resolution** | 832x480 recommended | Official recommendation from repo. 1024x576 also works well |
| **Frames** | 77 max (with ref) | Reference adds 4 frames, resulting in 81 latents. 81 without ref |
| **Gray value for masks** | 0.5 (RGB 127,127,127) | The neutral/"empty" value for VACE. Gray = areas to generate |
| **Gray value for padding** | 0.8 | For reference image padding (April 2, 2025) |
| **pad_frame_value** | 0.5 | For empty frame padding in VACE workflows |
| **riflex_freq_index** | 0 | Non-zero values add strange effects with VACE |
| **Sigma boundary** | 0.875 | VACE is T2V, not I2V (which uses 0.9) |
| **NAG strength** | 3-5 | For VACE 2.2 Fun workflows |
| **TeaCache threshold** | 0.1 | Standard 0.015 does not work well with VACE |
| **SLG** | Block 8, start 0.1, end 0.3-0.5 | Helps with image arrangement |

### Frame Count Formula

VACE requires frame counts following the **4n+1** rule: 5, 9, 13, 17, 21, 25, 29, 33, 37, 41, 45, 49, 53, 57, 61, 65, 69, 73, 77, **81**, 85, 89, 93, **97**, 101, 105, 109, 113, 117, **121**...

When a reference image is used, VACE adds 4 frames to the beginning of the batch (users reported sampling 85 frames from a nominal 81-frame setup). These may need to be trimmed before decode depending on the workflow.

---

## Multi-Control with prev_vace_embeds

**Major Feature (April 4, 2025):** Kijai added support for chaining multiple VACE encode nodes via the `prev_vace_embeds` input, allowing users to layer different controls with independent strengths.

### How It Works

Each VACE encode node has a `prev_vace_embeds` input. Connect the output of one encode to the input of the next to layer controls with different strengths.

**Key principles:**
- Each VACE encode can have its own strength, start_percent, and end_percent
- Controls can be applied at different timesteps (e.g., pose 0.0-0.2, then depth 0.2-1.0)
- **All nodes must have a reference image if ANY node has one** -- use a gray image as placeholder for nodes without a real reference
- The reference image adds a latent frame, so all inputs must match in size

> "you can set strength, start and end for each of them tho" -- Kijai, April 4, 2025

> "also using reference on one and not on another is not possible, because using reference adds the latent" -- Kijai, April 4, 2025

### Timestep-Based Control

Controls can be applied at different phases of generation:

- **Early steps (0.0-0.2):** Very strong influence on composition and structure
- **Mid steps (0.2-0.8):** Balanced control
- **Late steps (0.8-1.0):** Refinement and detail

> "like just tested, first embeds 0.0 - 0.2 and then flipped version of the video for 0.2-1.0" -- Kijai, April 4, 2025

**Important:** Early steps have WAY stronger influence than late steps. A 50/50 split won't give equal weight -- the first 20% of steps dominates the output.

> "stepwise, yes it works, but note that early steps are WAY stronger" -- Kijai, April 4, 2025

> "doing 50/50 split won't do much" -- Kijai, April 4, 2025

### Example Workflows

**Depth + Reference with different strengths:**
1. First VACE encode: depth control at 0.5 strength, gray reference image
2. Second VACE encode: no control, actual reference at 1.0 strength
3. Connect first output to second's prev_vace_embeds

> "sort of worked, gray image as the reference for the one with control, and strength 1.0, then the actual reference as 2nd VACE, with strenght 0.5" -- Kijai, April 4, 2025

**Pose for early steps, reference for rest:**
1. First VACE encode: pose control, start 0.0, end 0.2
2. Second VACE encode: reference only, start 0.2, end 1.0

**Depth + Pose combination:**
- Overlay pose skeleton on depth map, OR
- Use separate VACE encode nodes for each
- Depth provides scene structure, pose provides character motion
- Works particularly well with Sapiens pose for facial detail

### Depth + Pose Blending Technique (April 6, 2025)

**Community discovery:** Blending depth and pose into a single control image works well with proper preprocessing.

**Key requirements:**
- Blur the depth map significantly
- Increase contrast on the depth map
- Darken the depth map (pose expects black background)
- Layer pose on top of processed depth

> "this worked! With the prev embeds it affects the image results quality quite a lot but still testing" — yo9o, April 6, 2025

> "u can even punch the brightness and contrast higher as long as there is enough blur" — yo9o, April 6, 2025

**Why this works:**

Kijai explained that VACE was trained with grayscale inputs for colorization, and too-clean depth maps get confused as RGB grayscale:

> "I think it may have something to do with the model being conditioned with grayscale inputs too, for colorization, and it confuses a too good depthmap as such" — Kijai, April 6, 2025

Blurring the depth map prevents this confusion while preserving structural information.

**Alternative approach:**

Use separate VACE encode nodes with prev_vace_embeds:

> "you can also use two VACE encode nodes, one with the pure depth and one with the pure pose, and either set the strenthg to 0.5 on both (or less) or do some steps with one and some with another" — Kijai, April 6, 2025

> "the step range works pretty well, need to look at the preview to get an idea when to switch" — Kijai, April 6, 2025

### Limitations

**Latest input dominance (reported April 4, 2025):**

Some users reported that the latest VACE input in the chain seems to dominate:

> "from my early tests it doesnt feel like a blend. the latest input takes over all others" -- Hashu, April 4, 2025

This may be related to timestep distribution -- ensure early controls use low start_percent values to have meaningful influence.

**Reference image requirement:**

If ANY VACE encode in the chain has a reference image, ALL must have one (even if just a gray placeholder):

> "you need a reference in the second as well" -- dawniii, April 4, 2025

> "can just be a blank grey image but if you have one reference hooked up they all need to be" -- dawniii, April 4, 2025

---

## Control Signals

### Supported Preprocessors

**Confirmed working:**
- **Depth:** Depth Anything V2, Midas (official), Lotus
- **DWPose:** Excellent results for pose control
- **Sapiens:** Face pose, body pose, normals -- SOTA quality, temporally stable
- **Canny:** Works (should be inverted - black lines on white background)
- **Lineart:** Works (black lines on white background)
- **DensePreprocessor:** Works with good results
- **OpenPose:** Works
- **Mediapipe Face:** Works but may miss faces on some frames
- **SemSeg Preprocessor:** Surprisingly good results
- **OneCoco Sem:** Even better than standard SemSeg
- **Bounding Box:** Works for object tracking and positioning (April 3, 2025)
- **Optical Flow:** Works for motion control

> "btw for lineart/canny the model seems to want it as black lines on white bg" -- Kijai, April 2, 2025

**Sapiens Preprocessors (April 3, 2025):**

Kijai added support for Sapiens (Facebook's SOTA human understanding model):
- **Sapiens Pose:** Superior to DWPose for body and face
- **Sapiens Normals:** Excellent temporal stability
- **Sapiens Depth:** High quality depth maps

Sapiens is particularly effective for:
- Face pose control (better than DWPose/Mediapipe)
- Lip sync applications
- Full body pose with facial detail
- Normal maps for relighting

> "sapiens normals" -- Kijai, April 3, 2025 [🔥x7]

Sapiens nodes available at: `ComfyUI-WanVideoWrapper` (Kijai's follow-your-emoji wrapper)

**Bounding Box Control (April 3, 2025):**

Kijai added bounding box control for object tracking:
- Draw boxes around objects to guide their position
- Works with T2V (random if object appears) and I2V (more reliable)
- Can use spline editor to animate box positions
- No mask required -- just the box overlay on input frames

> "anyone tried the bounding box control yet?" -- Kijai, April 3, 2025

Results:
- Works well for tracking objects through scenes
- T2V may not always generate content in the box
- I2V more reliable for maintaining objects in boxes
- Can apply VACE to only some blocks for partial box visibility

**From official annotators:**
- Flow raft (new)
- Grounding DINO (new)
- Layout (new)
- RAM (Recognize Anything Model) (new)
- Salient (background removal mask) (new)
- InsightFace (face detection)
- FlowVisAnnotator (optical flow visualization)

### Control Types and Their Quirks

| Control Type | Notes |
|-------------|-------|
| **Depth** | Use Depth Anything V2 (not V3, not Video Depth Anything which has banding). Blur significantly for VACE -- high-quality depth maps are treated as RGB grayscale and trigger colorize mode. Lotus provides excellent quality. **Blender depth requires blur** to work properly |
| **DWPose** | VACE was trained with DWPose. Use inverted openpose to prevent stick artifacts. DWPose better than depth for facial features. Can leave visible dots on output if overlaid on depth |
| **Sapiens** | SOTA for human pose, face, and normals. Superior temporal stability. Recommended over DWPose for face work |
| **Lineart/Canny** | Should be inverted for VACE (black lines on white background). Early users reported mixed results. Realistic lineart > anyline |
| **Normal maps** | Not officially trained for VACE but users experimented with them. Lotus normals work well. Isolating the subject helps. VACE doesn't understand normals directly -- desaturate or treat as depth |
| **OpenPose** | Pose/openpose can bleed through into output. Inverted openpose helped reduce visible stick artifacts. Dots may appear on final output |
| **Optical flow** | VACE paper shows this as input -- no signal until something moves |
| **Bounding Box** | New as of April 3, 2025. Works for object tracking and positioning |

**Depth map preprocessing for VACE (April 6, 2025):**

VACE has specific requirements for depth maps that differ from other models:

> "oddly enough it doesn't understand my Blender depth, but depth anything pred is fine?" — Kijai, April 6, 2025

**The issue:** VACE was trained with grayscale inputs for colorization. Too-clean depth maps (like Blender renders) get confused as RGB images.

**Solution:** Add blur to depth maps:

> "3 pixel blur and completely different" — Kijai, April 6, 2025

> "even just this is enough..." — Kijai, April 6, 2025 (referring to minimal blur)

**Why this works:**

> "I think it may have something to do with the model being conditioned with grayscale inputs too, for colorization, and it confuses a too good depthmap as such" — Kijai, April 6, 2025

Every other model works with Blender depth maps, but VACE specifically needs the blur to distinguish depth from grayscale images.

**Pose dot bleeding issue (April 5, 2025):**

Multiple users reported visible pose skeleton dots appearing in final output when using DWPose:

> "I can't get rid of the pose dots on the output without losing likeness" -- burgstall, April 5, 2025

Attempted solutions:
- Adjusting dots toward gray and background toward gray to reduce contrast
- Using separate VACE encodes instead of overlaying controls
- Reducing VACE strength

The issue appears related to overlaying pose on depth maps. Using separate prev_vace_embeds for each control may help.

---

## Reference Images

### Basic Usage

VACE uses reference images to maintain subject appearance and style across generated video. The reference image is encoded as the first latent frame.

**Critical requirements:**
1. **White or gray background is essential** -- Remove background or pad with white/gray (0.8 gray recommended)
2. **Must have some white/gray in the image** -- Model won't work without it
3. **Dimensions must match video resolution** (or will be auto-padded)
4. **Positioning matters** -- Subject position in reference affects output position
5. **Scale matters** -- Reference image scale affects output (smaller ref may decrease quality)

> "if this is VACE, you should remove the background of your reference, or pad it with white" -- Kijai, April 2, 2025

> "I noticed it doesn't work at all if there aren't any white in the reference" -- Kijai, April 2, 2025

**Why white/gray background:**
The model is trained to look for multiple references in the same image separated by white background. Without white/gray, the model cannot properly identify the reference subject.

**Gray vs White Background (April 3, 2025):**

Community discussion revealed some nuance:
- **White background:** Recommended by Kijai and most documentation
- **Gray background:** Some VACE examples show gray backgrounds
- **Use gray for white subjects:** If the subject is predominantly white, gray background may work better to provide contrast

> "I've noticed that if the subject or reference object is predominantly white, it's better to use a gray background" -- JmySff, April 3, 2025

**Auto-padding (April 2, 2025):**

Kijai's wrapper automatically pads reference images with white/gray if aspect ratio doesn't match:

> "it does because it's square so it gets padded by white in the node. I have that setup to do it automatically in cases like this" -- Kijai, April 2, 2025

However, manual padding is recommended for better control over positioning.

### Reference Strength

**VACE strength parameter:**
- 0.4-0.8: Standard range
- 1.0: Default
- 1.5: Boosts reference likeness significantly, helps with pose following
- >1.0: Causes contrast/darkening issues

> "the strength value really boosts the reference too. using 1.5 now actually" -- Kijai, April 2, 2025

**Separate reference strength control:**

As of April 3, 2025, there is no way to control reference image strength separately from control signal strength in a single VACE encode node. However, with prev_vace_embeds, you can use separate nodes with different strengths.

### Multiple References

**Method:** Composite multiple subjects into a single image with white background.

> "in terms of multiple images, you put the images into a single image" -- Draken, April 2, 2025

**Training context:**
> "i believe it puts that image as the 'first frame' and is trained to pick up the likeness from it, very similar to ACE++ for flux, but not splitting the image" -- Draken, April 2, 2025

**Positioning:**
The model takes position from the reference image. Place subjects where you want them to appear in the output.

**Reference image locked to position:**

Multiple users reported that VACE strongly preserves the position and angle of the reference image:

> "Seems really wedded to keeping everything in the ref image intact" -- ajo6268#0, April 2, 2025

**Workaround for character consistency:**

For character face consistency across different angles/positions, users found success by:
1. Segmenting just the face from the reference
2. Zooming in on the face
3. Passing only the face as reference

### Reference Tips for Better Likeness

**From community testing (April 4, 2025):**

> "the bigger your ref is on screen the better the likeness, so if you just use a closeup of your characters face on a white bg you will get a better likeness" -- Hashu, April 4, 2025

**Best practices:**
- Use closeup crops that match the desired shot composition
- Reference resolution doesn't have to match output resolution (can be higher)
- Aspect ratio should match output for best results
- Describe the character in the prompt along with outfit colors
- Reference strength can go above 1.0 for better likeness (with contrast tradeoffs)
- Crop and composite multiple elements (face + clothes) side-by-side on white background

---

## Inpainting & Masking

### Video Inpainting

VACE supports video inpainting by masking regions to regenerate.

**Method:**
1. Prepare input video with masked areas filled with **gray (0.5 value / RGB 127,127,127)**
2. Supply matching mask where **white = regenerate**, **black = preserve**
3. VACE will regenerate the masked regions

> "send empty frames as gray frames (0.5 seems to work best) and your video frames, and mask where your video frames are white and rest black" -- Kijai, April 1, 2025

**Regional Inpainting (April 3, 2025):**

Users successfully demonstrated regional inpainting -- replacing specific objects or areas within frames:

**Outfit swapping example (Zuko):**
1. Take input video
2. Create mask for clothing area
3. Composite gray (0.5) over masked area in input_frames
4. Provide reference image with desired outfit
5. VACE regenerates clothing while preserving rest of video

> "I took the input frames, got the mask, then used an ImageMaskComposite node to composite gray over the parts of the mask in the input_frames" -- Zuko, April 3, 2025

**Object removal example (traxxas25, April 5, 2025):**

Successfully removed a person from a tracking shot using VACE inpainting:

> "I actually don't mean for the girl to be in this shot, trying to make it an empty lobby, but vaces inpaint feature is amazing... this would have been hours of comping work." -- traxxas25, April 5, 2025

**Subject removal tips (April 6, 2025):**

> "I think gray works best for the masking. Make sure the bounding box completely covers the subject, if even a few pixels of the person arent masked Vace tries to make sense of it by inserting a person." — traxxas25, April 6, 2025

> "I also found if theres a shadow or reflection that isnt masked vace will try to add a person too. The model seems too smart for its own good" — traxxas25, April 6, 2025

**Tinting masks to background color:**

> "tinting the mask color to the background you're trying to generate seems to help" — ArtOfficial, April 6, 2025

This helps VACE understand what should be generated in the masked area.

**Key tips:**
- Extend the inpainting mask slightly larger (e.g., 5 pixels) than the gray area to prevent edge leaking
- Don't use masks with holes -- VACE has issues with discontinuous mask regions
- Grow mask with negative expansion to shrink slightly inside the depth map prevents mask leaking
- Composite the result back onto the original footage using the alpha mask if background degradation is a concern
- Some users reported VACE 2.1 works better than Fun VACE 2.2 for spatial inpainting (not widely confirmed)
- **Avoid blurred/tapered mask edges** -- VACE doesn't handle them well and leaves artifacts

> "VACE not like blurred masks like that? Feels like every time I see someone using a faded mask it leaves artifacts on the edges" — A.I.Warper, April 6, 2025

> "sure it wouldn't be better without blurring the mask?" — Kijai, April 6, 2025

> "yeah I don't think it deals with that proper" — Kijai, April 6, 2025

**Mask polarity (April 5, 2025):**

Users reported confusion about whether to composite the mask into the video or provide it separately:

> "the mask is not for the reference image, but for the video in entry. i would to keep the decor of a real video, and change the man with a reference picture" -- Vérole, April 5, 2025

**Clarification:** You need BOTH:
1. Gray-filled areas in the input video itself
2. A separate mask input (white = regenerate, black = preserve)

Some workflows composite the result back onto the original video at the end to preserve unmasked areas perfectly.

### Outpainting

VACE handles outpainting well -- extending the visible area of a video beyond its original bounds.

- Use white for the areas to be outpainted (full effect).
- VACE remembers object details intelligently when outpainting (e.g., a partially visible scooter will be completed correctly).
- The prompt is respected during outpainting -- VACE chooses "union type" from inputs and prompt.
- Works with the Layer Forge node for HDRI dome creation in Unreal Engine. -- yukass

---

## Combining VACE with DG Models

**Major Discovery (April 4, 2025):** The standalone VACE module works with DG (DiffSynth) distilled models, enabling very fast VACE-controlled generation.

### DG Model Compatibility

Kijai's standalone VACE module can be loaded alongside any 1.3B T2V model, including the DG distilled variants:

- DG_Wan_v1_lite
- DG_Wan_v2_lite  
- DG_Wan_v3_lite
- DG_Wan_v4_lite
- DG_Wan_v4_plus_new (multiple variants)

Repository: `Evados/DiffSynth-Studio-Lora-Wan2.1-ComfyUI`

### Performance

**Speed with DG models:**
- **4 steps, CFG 1.0:** 7 seconds to generate (Kijai test, April 3, 2025)
- **8 steps, CFG 2.0:** Maintains quality while still very fast
- **10 steps, CFG 2.0:** 38 seconds for 832x480 (burgstall, April 5, 2025)

> "4 steps with the DG model, cfg 1.0, 7 seconds to generate" -- Kijai, April 3, 2025

**Quality considerations:**

Community testing revealed tradeoffs:

> "DG seems more creative and from my test it follows the reference image much less" -- IllumiReptilien, April 4, 2025

> "DG V4 High 10 steps cfg 2, with depth, the likeness is actually not much worse" -- burgstall, April 5, 2025

**Recommendations:**
- DG High variants (v4 High) provide better quality than Light/Medium
- Use CFG 1.0-2.0 with DG models (they are distilled)
- 4-10 steps is the sweet spot
- Reference adherence is weaker than base VACE but still usable
- Excellent for rapid iteration and previewing

### Settings for DG + VACE

| Parameter | Recommended Value | Notes |
|-----------|------------------|-------|
| **Steps** | 4-10 | 4 for speed, 10 for quality |
| **CFG** | 1.0-2.0 | DG models are distilled |
| **VACE strength** | 0.5-1.0 | Standard range |
| **Sampler** | uni_pc / euler | Standard samplers |
| **Scheduler** | simple / beta | Standard schedulers |

---

## SkyReels A2 Integration

**Released:** April 5, 2025 by Kijai

Kijai converted the SkyReels A2 model (a Wan 2.1 14B derivative) to work with VACE-style reference conditioning.

**Model:** `Kijai/WanVideo_comfy/blob/main/Wan2_1_SkyreelsA2_fp8_e4m3fn.safetensors`

### Key Features

- **14B I2V model** with reference support
- Works like VACE with reference and start frame
- Can also do normal I2V without reference
- **No extra VRAM cost** compared to standard 14B I2V
- **No control inputs** -- reference and start frame only

> "same as VACE with reference and start frame, but it's 14B model" -- Kijai, April 5, 2025

> "it's far better for I2V as it uses the 14B I2V" -- Kijai, April 5, 2025

### Advantages Over VACE

**VRAM efficiency:**
> "VACE for 14B is gonna be tough to run" -- Kijai, April 5, 2025

> "in that sense this is better" -- Kijai, April 5, 2025

SkyReels A2 provides 14B quality with reference support at the same VRAM cost as standard 14B I2V, whereas VACE 14B (when released) will require significantly more VRAM.

**I2V quality:**
> "curiously at least my initial test just doing normal I2V with this gave different results than the base I2V" -- Kijai, April 5, 2025

> "so it might be better I2V model too" -- Kijai, April 5, 2025

### Limitations

**No control inputs:**
Unlike VACE, SkyReels A2 does not support depth, pose, or other control signals -- only reference images and start frames.

**LoRA compatibility:**
> "the base model weights are changed so not gonna be perfect" -- Kijai, April 5, 2025

Since SkyReels A2 is a finetune rather than an add-on module, LoRAs trained on base Wan 2.1 may not work as well.

**Reference handling:**
The model supports 2-3 reference images (not just one), but the exact usage is still being explored.

---

## Known Issues

### Setup Errors

| Problem | Solution |
|---------|----------|
| `vace_scale` KeyError | VACE model not loaded properly. Ensure VACE module is connected |
| `WanModel has no attribute 'vace_blocks'` | Using I2V model instead of T2V. VACE only works with T2V models |
| `vace_blocks.0._orig_mod.self_attn.q.weight` KeyError | Update wrapper to latest commit |
| `vace_blocks.8.modulation` error with fp8 | May indicate model/format mismatch. Users reported this with incorrect settings/model combinations |
| Model mismatch error with VACE 2.2 | Check VAE version and model compatibility (not widely confirmed) |
| `Wan22` import error | May indicate outdated ComfyUI version (not widely confirmed) |
| VACE module won't load after update | Check PyTorch version compatibility (not widely confirmed) |
| `ValueError: loading VACE module as WanVideo model` | VACE module goes in `vace_model` input, not the main model loader |
| GGUF with VACE module in native | Native support was evolving; some users had success, while modular/chained workflows were often easier in wrapper |
| Block swap error with VACE | Ensure VACE blocks to swap is not 0. Set to at least 1 for proper offloading |
| Scaled model text encoding error | Use ComfyUI text encoding (CLIPTextEncode) with the bridge node, not wrapper text encoding |
| Tensor size mismatch with prev_vace_embeds | All reference images must be present if ANY node has one. Use gray placeholder images |
| Dimension mismatch errors | Width and height must be divisible by 16 |

### Generation Issues

| Problem | Solution |
|---------|----------|
| Flashy/bad results | Some users reported disabling batched CFG or adjusting block swap helped (not widely confirmed) |
| Orange tinted outputs | Some users reported adjusting vace_blocks_to_swap and block_swap values or reducing frame count helped (not widely confirmed) |
| Black generations | May be caused by mismatched quantization types. Try matching formats (not widely confirmed) |
| Darkened output | Reduce VACE strength to 0.7-1.0. Strength above 1.0 causes contrast issues |
| Garbage output | Don't swap High and Low modules -- plugging High in Low slot produces garbage. -- Gleb Tretyak |
| First frame flash in VACE 2.2 | Some users reported lowering CFG scale start helped (not widely confirmed) |
| Double ghost effect | VACE adds ghosts to compensate when controlnets are out of position with ref image |
| Misty effect / white dots on faces | Disable face aspect of pose controlnet |
| Pose rig bleeding through | Try random seed, adjust VACE strength up or down. Don't overlay controlnets -- use separate VACE encodes |
| Color shift in results | Prompting matters a lot per batch. Higher resolution reduces color degradation. VACE encode node may contribute |
| Over-saturated outputs | Use separate VACE encodes instead of combining preprocessors. Reduce strength |
| Warm colorization tendency | VACE trained for grayscale-to-color conversion. Blur high-quality depth/normal maps |
| Tensor size mismatch | Ensure all images, masks, and videos have same resolution and frame count. Reference adds 4 frames |
| VACE module seems ignored | Check that sampler recognizes the model as VACE (should show 'WAN21_vace', not 'WAN21') |
| Losing 2 frames (32 in, 30 out) | Use 4n+1 frame count formula |
| Tiled VAE degrades quality | Use CPU cache for VAE instead of tiled VAE |
| TeaCache not working with VACE | Some users reported needing to disable TeaCache when using VACE with CausVid. Specific threshold guidance not widely confirmed |
| OOM at high resolutions | Users reported OOM at higher resolutions even with block swap. Reducing resolution or frame count may help |
| torch.compile artifacts in Fun VACE | May be PyTorch version-related; try upgrading (not widely confirmed) |
| Context options tensor mismatch | Some users reported errors when using context options with multi-VACE setups. Workarounds may depend on workflow |
| Memory leak with VACE | Occurs when workflow errors during encode/sample. Restart ComfyUI |
| Bounding box not working | T2V may randomly place objects. Use I2V for more reliable box tracking |
| Control signal treated as video | Ensure first frame is colored image, rest are control. Use proper masks |
| Gray halo around inpainted areas | Reduce mask growth or composite result back onto original footage |
| Pose dots visible in output | Use separate VACE encodes instead of overlaying pose on depth. Adjust contrast between dots and background |
| Poor likeness with inpainting | Use larger reference crops. Increase VACE strength. Ensure reference background is white/gray |
| Latest control dominates in chain | Apply early controls at low start_percent (0.0-0.2) for meaningful influence |
| Blender depth not working | Add blur to depth map (3+ pixels). VACE confuses clean depth as grayscale image |
| Depth + pose blend shows rig | Blur depth significantly, increase contrast, darken depth map before layering pose |

### Mask & Inpainting Issues

| Problem | Solution |
|---------|----------|
| Mask being ignored | Bake the mask into the video as gray areas. Also check wrapper vs native mask polarity (may need to invert) |
| Mask leaking into output | Extend inpainting mask 5px beyond the gray area. Use grow mask with negative expansion |
| Grey alpha edges on expanded masks | Known issue with mask expansion. Use precise masks instead |
| Inpainting not replacing anything | Need BOTH gray fill on the video AND a separate mask. Gray alone oversaturates, mask alone does nothing |
| Seams with tight crop inpainting | Add more padding of unmasked area. Use bigger sampling area. Composite back with grow mask and border blending |
| Masks with holes cause issues | VACE does not handle discontinuous masks well |
| Blurred mask edges leave artifacts | Use sharp masks without blur or taper. VACE doesn't handle soft edges well |
| Person keeps appearing in mask | Ensure bounding box completely covers subject including shadows/reflections |

---

## See Also

- [[wan-2.1]] — Base model family for VACE 2.1
- [[wan-2.2]] — Base model family for Fun VACE
- [[phantom]] — Character consistency model, best paired with VACE
- [[comfyui]] — Node-based UI for running VACE workflows
- [[quantization]] — GGUF and fp8 formats for VACE modules
- [[speed]] — CausVid, FusionX, LightX2V acceleration LoRAs
- [[lora]] — Training and using LoRAs with VACE
- [[context-windows]] — Long video generation with VACE
- [[sapiens]] — SOTA human understanding preprocessors
- [[skyreels-a2]] — Alternative 14B reference model

## External Resources

- [VACE Project Page](https://ali-vilab.github.io/VACE-Page/)
- [VACE GitHub Repository](https://github.com/ali-vilab/VACE)
- [VACE Paper (arXiv)](https://arxiv.org/pdf/2503.07598)
- [VACE User Guide (Official)](https://github.com/ali-vilab/VACE/blob/main/UserGuide.md)
- [Standalone VACE Module](https://huggingface.co/Kijai/WanVideo_comfy/blob/main/Wan2_1_VACE_1_3B_preview_bf16.safetensors)
- [ComfyUI-WanVaceAdvanced](https://github.com/drozbay/ComfyUI-WanVaceAdvanced)
- [Wan 2.2 VACE User Guide (Nathan Shipley)](https://nathanshipley.notion.site/Guide-VACE-with-Wan-2-2-in-ComfyUI-27191e115364802186aacc04c00d71f3)
- [Wan 2.1 Knowledge Base - VACE Section](https://nathanshipley.notion.site/Wan-2-1-Knowledge-Base-1d691e115364814fa9d4e27694e9468f#1d691e11536481f380e4cbf7fa105c05)
- [DG Distilled Models](https://huggingface.co/Evados/DiffSynth-Studio-Lora-Wan2.1-ComfyUI)
- [Sapiens (Facebook)](https://github.com/facebookresearch/sapiens)
- [SkyReels A2](https://huggingface.co/Kijai/WanVideo_comfy/blob/main/Wan2_1_SkyreelsA2_fp8_e4m3fn.safetensors)
