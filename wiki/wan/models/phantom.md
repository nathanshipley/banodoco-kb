---
title: Phantom
aliases: [phantom, wan-phantom, phantom-14b, phantom-1.3b]
sources_ingested: 16
last_updated: 2026-04-06
---

# Phantom

Phantom is a subject consistency / identity preservation model built on top of [[wan-2.1]]. It takes reference images and encodes them as latent frames appended to the generation's noise latent (in the temporal dimension), allowing it to preserve character likeness, clothing, and objects across video frames. Unlike standard I2V models that put image information in extra channels, Phantom keeps the T2V architecture intact, which means it remains compatible with [[vace|VACE]] and T2V-trained [[lora|LoRAs]].

Phantom was developed by the Phantom-video team (possibly acquired by ByteDance based on developer GitHub profiles). The 1.3B model was released first, followed by the 14B model in May 2025. A "Phantom Pro" model trained on higher resolutions was announced but details remain limited. The team also released [[humo|HuMo]] (audio-driven character generation) and OmniInsert (subject insertion for videos).

> "Phantom references are on another level, true subject to video capability." -- Ablejones, Discord #wan_chatter, September 2025

---

## What It's For

- **Character consistency** -- Maintain a person's face, hair, clothing, and body across generated video
- **Multi-subject scenes** -- Up to 4 reference images, each can be a different subject (person, object, background)
- **Product replication** -- Excellent at accurately replicating products and objects from reference photos
- **Style adherence** -- Good at style mixing and maintaining artistic styles from references
- **Pseudo-I2V** -- Though technically T2V, produces some of the best I2V-like results by encoding reference latents
- **3D character perspectives** -- Can generate full rotation/pan views of a character from a single image, useful for extracting training data

---

## Setup & Requirements

### Model Files

Phantom is a fine-tuned Wan T2V model (not a separate module like VACE). It replaces the base T2V checkpoint entirely.

| Model | Size | Notes |
|-------|------|-------|
| Phantom 1.3B | ~2.6 GB (fp16) | Simpler, works well with VACE at this scale |
| Phantom 14B fp16 | ~30 GB | Best quality, too large for on-the-fly quantization on 12 GB cards |
| Phantom 14B fp8_e4m3fn | ~15 GB | Good balance of quality and speed |
| Phantom 14B fp8_e5m2 | ~15 GB | Better compatibility with older GPUs (e.g., RTX 3060) |
| VACE+Phantom v2 merge (fp16) | ~30 GB | Piblarg's merged model combining both capabilities |
| VACE+Phantom v2 GGUF Q8 | ~16 GB | orabazes conversion for low-VRAM setups |
| VACE+Phantom v2 GGUF Q5_K_M | ~10 GB | Smallest merged option |
| FusionX Phantom merge | varies | Phantom merged with FusionX LoRAs, compatible with VACE |

**Key repositories:**

- Kijai fp8 scaled: `Kijai/WanVideo_comfy_fp8_scaled` (includes `Wan2_1-T2V-14B-Phantom_fp8_e5m2_scaled_KJ.safetensors`)
- VACE+Phantom v2 GGUF: `orabazes/wan-14B_vace_phantom_v2_GGUF`
- VACE+Phantom v2 fp16: `Inner-Reflections/Wan2.1_VACE_Phantom` (`wan-14B_vace_phantom_v2_fp16.safetensors`)
- FusionX VACE Phantom: `QuantStack/Wan2.1_T2V_14B_FusionX_VACE`

### VRAM Requirements

| Configuration | Resolution | Frames | VRAM | Notes |
|--------------|-----------|--------|------|-------|
| Phantom 14B fp8 | 832x480 | 121 | ~16 GB | With block swap |
| Phantom 14B fp16 | 832x480 | 121 | ~32 GB | Without optimization |
| VACE+Phantom merge fp8 | 832x480 | 121 | ~12 GB | RTX 3060 confirmed |
| VACE+Phantom merge | 832x480 | 81 | ~12 GB | FFLF workflow, 15 min on 3060 |
| Phantom + VACE module | 720p | 81+ | ~24 GB+ | Resource intensive |

**System RAM:** 32 GB minimum. 64 GB recommended. Windows users should increase paging file to 80-96 GB to avoid OOM crashes.

### ComfyUI Setup

Phantom works with both **Kijai WanVideoWrapper** and **native ComfyUI nodes**.

**Key custom nodes:**
- `WanVacePhantomSimpleV2` (Ablejones) -- Simplified node for VACE+Phantom together
- `WanVacePhantomDualV2` (Ablejones) -- Dual control inputs for separate depth/pose/lineart
- `WanVaceAdvanced` (drozbay/Ablejones) -- Advanced VACE nodes with Phantom embed handling
- VACE+Phantom conditioning patcher (Ablejones) -- Properly injects phantom latents into VACE conditioning

**Critical:** Phantom only works with T2V models. It is incompatible with I2V models, Uni3C (which requires I2V), and GGUF VACE modules (cannot plug non-GGUF VACE into Phantom GGUF). The VACE+Phantom merged model works with fp8 scaled I2V models but not with GGUF loaders.

---

## Key Settings

### Baseline Settings (No Speed LoRA)

| Parameter | Value | Notes |
|-----------|-------|-------|
| **Frames** | **121** | Phantom trained on 121 frames. Consistency degrades at 81 or 49 frames (produces "midgets," wrong clothing). 97 frames is a viable middle ground for VACE merge |
| **FPS** | **24** | Training framerate. VACE trained at 16fps with 81 frames |
| **CFG** | **5** | Phantom needs CFG > 1. CFG 1.0 produces poor likeness and ignores references |
| **Steps** | **20** | Minimum for quality. Full model was much better than distilled at fewer steps |
| **Sampler** | **DPM++ SDE / UniPC** | DPM++ SDE Beta reportedly best. LCM generally does not work well |
| **Shift** | **Low (2.2 or lower)** | Phantom prefers low shift values. Higher shift hurts likeness/consistency |
| **Resolution** | **832x480** | Trained on 480p. Works well at higher resolutions despite not being trained on them |
| **Reference images** | **1-4** | Up to 4 images. Can cover different angles of same subject or different subjects |

### With Speed LoRAs (CausVid/LightX2V)

| Parameter | Value | Notes |
|-----------|-------|-------|
| **Steps** | **8-12** | 12 steps with CausVid produces decent results |
| **CFG schedule** | **CFG 3 for first 3 steps, CFG 1.0 for remaining** | Phantom is very sensitive to CFG scheduling with distill LoRAs |
| **CausVid strength** | **0.3-0.5** | Higher strengths cause flicker. Block 0 disabled is "the right way" |
| **LightX2V strength** | **0.5 with CFG 2.0** | CFG 1.0 worsens Phantom resemblance |
| **CausVid version** | **V2 preferred** | Can use full strength, less plasticy, has block 0 already removed |

### Phantom CFG (Internal)

The original Phantom model uses 3 CFG passes with its own internal formula:

```
noise_pred = noise_pred_uncond + phantom_cfg_scale * (noise_pred_phantom - noise_pred_uncond)
           + cfg_scale * (noise_pred_cond - noise_pred_phantom)
```

This makes Phantom 14B approximately 3x slower than base Wan 14B due to the triple noise predictions. Setting main CFG to 1.0 disables phantom CFG and restores normal speed, but at the cost of reference adherence. Use a dual CFG guider for proper handling of Phantom's 2 negative embeds. -- Kijai, Discord #wan_chatter, July 2025

### VACE+Phantom Merge Settings

| Parameter | Value | Notes |
|-----------|-------|-------|
| **VACE strength of Phantom frames** | **0.0** | Automatically set in background by merge nodes |
| **VACE strength (overall)** | **1.0** | Default works well for merge |
| **ControlVid strength** | **2.0** | Higher strength needed to make character follow control video instead of reference pose |
| **Frame count** | **97** | Compromise between Phantom's 121 and VACE's 81 |

---

## How It Works

Phantom encodes reference images into latent frames that are appended to the generation's noise tensor in the **temporal dimension**. This is architecturally identical to how [[vace|VACE]] stores its references -- both live in temporal space, while I2V models put image information in extra input channels. Because Phantom never modifies the base T2V architecture's channel count, it remains a T2V model and can work alongside VACE.

When you set 81 frames with Phantom, it actually samples more frames (e.g., 89) because the reference latents are included in the sampled tensor. The reference frames are trimmed at the **end** of sampling, not the beginning. -- Kijai, Discord #wan_chatter, July 2025

Phantom uses prompts internally to determine which aspects of reference images to focus on. This is why detailed prompting about reference contents is critical -- it will ignore anything in the reference not explicitly mentioned in the prompt.

---

## Techniques

### Reference Image Preparation

- **Use diverse images** -- Don't use the same image for both first frame and Phantom reference. Different angles, lighting, and contexts produce much better results
- **White background preferred** -- Especially when removing backgrounds from subjects. Cut objects over white in ComfyUI
- **Real backgrounds also work** -- Phantom prefers simple but real backgrounds; VACE reference prefers white
- **Cover multiple angles** -- Four images of the same subject (face, profile, back of jacket, etc.) provide strong consistency
- **Collages for more subjects** -- Limited to 4 image slots, but each slot can be a collage of multiple characters
- **Send as batch, not concatenated** -- Better results when feeding images separately rather than making one combined image
- **Duplicate for emphasis** -- Sending the same image multiple times can improve resemblance
- **Use real photos over AI images** -- Real face images produce much better results than AI-generated faces
- **Match resolution** -- Don't crop reference images smaller than the output resolution. Mirror edges and blur if needed

### Prompting for Phantom

Phantom prompting is fundamentally different from standard T2V:

- **Simple, minimal prompts work best** -- "A woman drinking coffee" works better than detailed paragraphs. Extensive descriptions take focus away from reference identity
- **Mention what you want to keep** -- Phantom ignores reference elements not mentioned in the prompt. Add details about hair color, clothing, etc. that you want preserved
- **Chinese prompts work better** -- Model was trained mostly with Chinese text, adheres better to Chinese prompts
- **For multiple characters** -- Describe each person briefly ("man in black," "woman with red hair") to prevent Phantom from only rendering one
- **Add actions to negative** -- "Talking" or "conversation" in negative prompt prevents unwanted mouth movement
- **Use closed-mouth reference** -- If characters keep talking, use reference images with closed mouths

### Combining with VACE

The VACE+Phantom combination is the most popular advanced workflow:

1. **Merge approach** -- Use a pre-merged VACE+Phantom model (Piblarg's v2 merge). Simplest setup, months of community refinement
2. **Module approach** -- Load Phantom as base model, add VACE module separately. Phantom gets references, VACE gets control preprocessors (depth, pose, canny)
3. **VACE input + Phantom ref** -- Use VACE for control (no ref image in VACE), put all reference images into Phantom. Identity preserved much better than VACE ref alone
4. **Don't pass ref image to both** -- Putting reference through both VACE and Phantom causes glitched output
5. **When chaining WanVacePhantom nodes** -- Phantom/reference images must go in the **last** node before the sampler to avoid latent size conflicts

**VACE strength control for Phantom embeds:** Ablejones created a node that controls the VACE strength values overlapping with Phantom embed latents, allowing fine-tuning of the interaction.

### Combining with Other Models

- **HuMo pipeline** -- Generate scene with VACE+Phantom for movement, then v2v pass with HuMo for lip sync
- **MultiTalk** -- Phantom has more dynamic movement, MultiTalk has better lip sync. Cannot easily combine their embeds (both feed into same image_embeds input)
- **Wan 2.2 hybrid** -- Use Wan 2.2 HN model for initial steps to get depth map, then use Phantom for LN sampling. Or use VACE 2.2 for high noise, switch to Phantom for final steps
- **WanAnimate** -- Can use VACE+Phantom for multi-subject videos, then WanAnimate for motion refinement with cropped inpainting
- **Face detailing** -- Standard FaceDetailer doesn't work with video. Use modified Impact Pack fork (Ablejones) that bypasses image batch warnings

### Video Extension

- **81 frames per section with 9-frame overlap** -- Using WanPhantomSubjectToVideo node for steerable motion continuation
- **FFLF (First-Frame-Last-Frame)** -- Morphing technique that avoids usual Phantom problems at less than 121 frames. Works better at 81 frames than standard Phantom at 81
- **Context windows** -- Phantom with context windows produces confusing results; use with caution. Phantom+VACE merge fixed for context windows as of August 2025

---

## Phantom vs Alternatives

| Feature | Phantom | [[magref|MAGREF]] | [[vace|VACE]] ref | [[wananimate|WanAnimate]] | Stand-In | IP-Adapter | LoRA |
|---------|---------|--------|----------|-------------|----------|------------|------|
| **Architecture** | T2V + ref latents | I2V model | T2V + VACE module | ControlNet-like | LoRA (~300 MB) | Adapter | Fine-tuned weights |
| **Likeness** | ~80% (excellent) | ~95% (best) | ~60% | Good, not 1:1 | Decent | Moderate | Best (trained) |
| **Multi-ref** | Up to 4 images | Single image | Single image | Varies | Single | Single | N/A |
| **Prompt following** | Moderate | Weaker | Strong | Good | Moderate | Moderate | Strong |
| **Motion quality** | Good (24fps trained) | 15fps trained | Best | Good | Like base | Like base | Like base |
| **Speed** | Slow (3x CFG) | Normal | Normal | Normal | Normal | Normal | Normal |
| **Control compat** | VACE, some LoRAs | Limited | Full VACE | Its own | Full | Full | Full |
| **Flexibility** | Good (outfit/hair changes) | Rigid (exact match) | Moderate | Moderate | Limited | Limited | Fixed |

**Key comparisons:**
- **MAGREF** gets higher accuracy (~95% vs ~80%) but is limited to single reference at full resolution and is an I2V model. Better for exact likeness, worse for creative flexibility. Works better for character swapping (5 people in video) than Phantom
- **VACE reference** is weaker for likeness but more compatible with controls and prompting. VACE has better motion than Phantom
- **WanAnimate** surpassed massive VACE+Phantom+PUSA workflows with far less tweaking (DawnII), though Phantom still edges it on pure likeness (Piblarg). Community split on which is better
- **Stand-In** is similar to Phantom but just a 300 MB LoRA, making it more compatible with other workflows. Phantom is better overall for likeness
- **LoRA training** will almost always beat image references for consistency, but requires training time and data

---

## Quirks & Gotchas

- **Seed dependent** -- Some seeds work fantastically while others produce complete failures. Use live preview to detect failures after 5-10 steps and restart with new seed
- **Frame count critical** -- Trained on 121 frames. At 49 frames produces "midgets," at 81 frames clothing/face degrades. Always try 121 first
- **Fragile to additions** -- Adding anything (LoRAs, merges, other models) tends to make Phantom work worse. Use lower strengths when combining
- **Style LoRAs destroy performance** -- Any style LoRA negatively impacts Phantom results. Character LoRAs trained on T2V only work ~30% with Phantom
- **Struggles with animated/2D content** -- Does realism well, struggles with anime/cartoon styles. Likely trained only on realistic images
- **First frames look bad** -- First few frames typically look poor, then quality clears up. This is normal behavior
- **Characters constantly talking** -- Common issue. Use closed-mouth reference images and add "talking" to negative prompt
- **Multiple characters unreliable** -- Sometimes renders only one of two characters. More clearly describe both in the prompt
- **Reference positioning matters** -- Characters perform better when positioned optimally in reference images. Phantom considers colors, backgrounds, positions, and scale
- **WebP format issues** -- Convert WebP images to PNG/JPG for better results
- **Moviigen LoRA causes issues** -- Even at 0.25 strength, not worth the weird motion artifacts or likeness loss
- **Phantom alone + VACE can conflict** -- Coupling with VACE sometimes causes character consistency to break and produces artifacts. The merged model handles this better than separate loading
- **fp16 vs bf16 matters** -- fp16 quality improvement over bf16 is massive on Phantom specifically. -- Dream Making, Discord #wan_chatter, June 2025

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| CFG 1.0 produces poor likeness | Phantom needs CFG > 1. Use at least CFG 3-5, or schedule: CFG 3 for first steps, then drop to 1.0 |
| Flashing/noise at start of video | Lower VACE embed strength for video input. Or add LoRA block edit with block 0 off. Lower CausVid to 0.4 |
| Tensor size mismatch with VACE | Use patcher node. Put Phantom images only in last node. Add 4 VACE images for every Phantom image to match sizes |
| Only one character renders | Describe both characters explicitly in prompt. Use 14B (handles 3+ subjects better than 1.3B) |
| Mask showing as frame | Try empty or very short prompts. Long prompts can cause flash issues |
| ComfyUI crashes (OOM) | Check RAM usage. Increase Windows paging file to 80-96 GB. Phantom + VACE is very resource intensive |
| LCM scheduler poor results | Use UniPC or DPM++ SDE instead. LCM doesn't work well with Phantom |
| CausVid causes noise/artifacts with GGUF | Use fp8 instead of GGUF Q8 for better CausVid compatibility |
| Phantom ignoring references | Add specific details about reference contents to the prompt. Phantom only preserves what's mentioned |
| 3x slower than expected | Phantom uses 3 CFG passes. Set main CFG to 1.0 to disable (at cost of quality), or accept the speed trade-off |
| ControlNet tensor mismatch | Need to pad control frames since Phantom adds latent(s) to the temporal dimension |
| bf16 VACE module issues | Don't mix bf16 VACE module with Phantom fp8_e5m2. Match precision between models |
| Poor results with same first-frame and ref | Use different images. Diverse references always outperform duplicate ones |
| Reference image flickering in wrapper | Latent isn't trimmed properly when combined with Phantom. Known wrapper issue |
| Self-forcing breaks at 6 steps | Use 4-5 steps maximum with Phantom when using self-forcing |
| Excessive mouth movement | Use reference with closed mouth. Add facial expression descriptions to prompt |
| WanVacePhantomSimpleV2 error | Need images in phantom image input. VACE references can be empty. Don't plug videos into phantom input (causes OOM) |
| Hair/clothing changes between batches | Frame count sensitivity. Use 121 frames. Add more reference images covering different angles |

---

## LoRA Compatibility

Phantom has a complicated relationship with LoRAs:

- **T2V LoRAs partially work** (~30% effectiveness). LoRAs need retraining with Phantom as base for best results
- **CausVid V2** is the most-used speed LoRA. Use at 0.3-0.5 strength with block 0 disabled. V2 preferred over V1
- **LightX2V** works at 0.5 strength with CFG 2.0. R16 version still better for VACE/Phantom at various strengths
- **FusionX** -- Merging FusionX with Phantom produces stellar results. UniPC sampler works well with FusionX Phantom
- **PUSA** -- Phantom FusionX + PUSA + LightX2V LoRA stack provides good I2V results
- **Merging Phantom with T2V at 0.15-0.25 strength** dramatically improves LoRA compatibility. Pure Phantom often produces poor results ("monstrosity") with LoRAs
- **Merging speed LoRAs into Phantom** (CausVid/AccVid baked in) works well for eliminating per-generation LoRA loading
- **Wan 2.2 LN LoRA** can be extracted and applied to Phantom to get 2.2 improvements
- **Disable TeaCache** when using Phantom + CausVid with 10 steps. Quality much better without

---

## Hardware

| GPU | Capability | Notes |
|-----|-----------|-------|
| RTX 3060 (12 GB) | 832x480x121 with merge | 15-18 min with VACE+Phantom FFLF. Use e5m2 format (e4m3fn incompatible). VACE module on top is too heavy |
| RTX 4090 (24 GB) | Full Phantom 14B fp8 | Comfortable. ~253 seconds for standard generation |
| RTX 5090 (32 GB) | Full Phantom + VACE + LoRAs | Handles complex multi-model workflows |
| RTX 6000 Pro (48 GB) | Everything | About 2x speed of 4090 |
| L4 (cloud) | Full workflow | ~100s with LightX2V + 3 LoRAs |

**Speed comparisons:**
- Phantom alone: 253 seconds vs VACE alone: 738 seconds (same generation) -- VRGameDevGirl84
- Phantom + VACE: 261 seconds -- VRGameDevGirl84
- FP8 Phantom: roughly half the generation time of FP16 with similar quality
- SageAttention approximately doubles Phantom speed

---

## Timeline

| Date | Event |
|------|-------|
| April 2025 | Phantom 1.3B released |
| May 2025 | Phantom 14B released on HuggingFace (trained on 480p, 121 frames, 24fps) |
| May 2025 | VACE+Phantom merge workflows developed (Piblarg, Ablejones) |
| May 2025 | Kijai provides fp8 scaled and e5m2 conversions |
| June 2025 | Community develops advanced combination nodes (WanVacePhantomSimpleV2, DualV2) |
| June 2025 | VACE+Phantom v2 merge released (Piblarg fp16, orabazes GGUF) |
| June 2025 | FusionX Phantom merged models appear |
| July 2025 | Phantom+VACE workflows refined. PerpNegGuider testing. MAGREF comparisons begin |
| August 2025 | Phantom + MultiTalk combination fixed for context windows |
| September 2025 | HuMo released by Phantom team. WanAnimate comparisons. VACE 2.2 + Phantom hybrid workflows |
| October 2025 | Phantom custom 14B model released by community (Thom293). Lynx released (ByteDance competitor) |
| November 2025 | OmniInsert announced by Phantom team. Phantom Pro (higher res training) announced |
| December 2025 | Community reports Phantom possibly acquired by ByteDance |

---

## See Also

- [[vace]] -- Control system that pairs with Phantom for the most popular advanced workflow
- [[magref]] -- I2V alternative with higher accuracy but less flexibility
- [[wananimate]] -- Newer alternative with simpler setup, debated vs Phantom for likeness
- [[humo]] -- Audio-driven model from same team, built on similar architecture
- [[lora|LoRA Training]] -- Training custom LoRAs on Phantom base for best character consistency
- [[wan-2.1]] -- Base model family Phantom is built on
- [[wan-2.2]] -- Partial compatibility; VACE 2.2 modules can work with Phantom in hybrid workflows

### External Resources

- VACE+Phantom combination node: https://github.com/drozbay/VaceWanAdvancedTests
- VACE+Phantom v2 GGUF: https://huggingface.co/orabazes/wan-14B_vace_phantom_v2_GGUF
- VACE+Phantom v2 fp16: https://huggingface.co/Inner-Reflections/Wan2.1_VACE_Phantom
- Kijai fp8 models: https://huggingface.co/Kijai/WanVideo_comfy_fp8_scaled
- OmniInsert: https://github.com/Phantom-video/OmniInsert
- HuMo: https://github.com/Phantom-video/HuMo
