---
title: VACE (Video Anything ControlNet Enhancement)
aliases: [vace, vace-2.1, vace-2.2, fun-vace, vace-1.3b, vace-14b]
sources_ingested: 15
last_updated: 2026-04-06
verification: partial (GPT-5.4, checked against top 3 weeks of raw messages)
---

# VACE (Video Anything ControlNet Enhancement)

VACE is a unified video control system from Alibaba (ali-vilab) that adds style transfer, inpainting, outpainting, subject-driven generation, and pose/depth control to the [[wan-2.1]] and [[wan-2.2]] model families. Unlike traditional ControlNets, VACE bundles reference images, control signals, and masks into a single conditioning system. It is architecturally a set of extra blocks (the "Context Embedder" and "Context Blocks") added alongside a frozen T2V DiT model -- the base model weights are never modified, which means existing [[lora|LoRAs]] trained on the base model continue to work.

A 1.3B preview was available by early April 2025, with official 1.3B and 14B versions released on May 14, 2025. A Wan 2.2 "Fun VACE" variant followed later.

> "VACE is basically just a controlnet on top of an unmodified T2V model, so T2V LoRAs work incredibly well. A trained LoRA will almost always beat image references." -- spacepxl, Discord #wan_chatter, December 2025

---

## Setup & Requirements

### Model Files

VACE comes in two forms:

1. **Standalone VACE module** -- Only the VACE blocks, loaded alongside a separate Wan T2V base model. This approach allows swapping base models freely. Kijai initially extracted a standalone 1.3B preview module; 14B modules became available after the May 2025 release.
2. **Merged VACE model** -- The VACE blocks baked into a full Wan T2V checkpoint. Simpler to use but less flexible.

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
- Official VACE: `ali-vilab/VACE`
- Kijai fp8 modules: `Kijai/WanVideo_comfy_fp8_scaled/tree/main/VACE`
- Kijai bf16 modules: `Kijai/WanVideo_comfy/tree/main/Fun/VACE` (2.2) and `Kijai/WanVideo_comfy` (2.1)
- Kijai GGUF modules: `Kijai/WanVideo_comfy_GGUF/tree/main/VACE`
- Fun VACE 2.2 original: `alibaba-pai/Wan2.2-VACE-Fun-A14B`
- Fun VACE 2.2 GGUF: `QuantStack/Wan2.2-VACE-Fun-A14B-GGUF`
- FusionX VACE (distilled merge): `QuantStack/Wan2.1_T2V_14B_FusionX_VACE`
- Phantom-VACE merge: `orabazes/wan-14B_vace_phantom_v2_GGUF`

### VRAM Requirements

| Configuration | Resolution | Frames | VRAM | Notes |
|--------------|-----------|--------|------|-------|
| 1.3B fp32 + VACE | 832x480 | 81 | ~12 GB | After Kijai memory optimizations |
| 1.3B fp32 + VACE | 1024x1024 | 81 | ~13 GB | With offloading |
| 14B fp8 + VACE module | 832x480 | 81 | ~16 GB | With block swap |
| 14B fp8 + VACE module | 720p | 81 | ~20-24 GB | Block swap 40 base + 5 VACE |
| 14B bf16 + VACE bf16 | Any | Any | ~40 GB | Without optimization |
| Wan 2.2 dual model + VACE | 720p | 81 | 12-16 GB | fp8 modules, 32 GB system RAM |
| VACE + Phantom merge | 832x480 | 121 | ~12 GB | fp8, on RTX 3060 |

**Block swap settings for VRAM management:**

| VRAM | Base blocks to swap | VACE blocks to swap |
|------|--------------------|--------------------|
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

---

## Key Settings

| Parameter | Recommended Value | Notes |
|-----------|------------------|-------|
| **VACE encode strength** | 0.4-0.8 | Lower values (e.g. 0.4) preserve more creative freedom, higher values increase fidelity to control. Users reported various values working well |
| **VACE strength** (overall) | 0.7-1.0 | Above 1.0 causes contrast/darkening issues. Can go to 1.5 for pose following with DWPose |
| **CFG** | 2.0-6.0 | Start at 3.0. VACE 2.2 benefits from CFG > 1.0 (unlike many distilled models). High CFG causes artifacts |
| **Steps** | 20-50 | 20 minimum for quality. 50 for VACE 2.2. 6-8 with speed LoRAs (CausVid/FusionX) |
| **Frames** | 81 (2.1) / 97-121 (Phantom merge) | Must follow 4n+1 formula. 81 is VACE training default. Phantom trained on 121 |
| **Resolution** | 832x480 to 1280x720 | 14B needs higher resolution. 1.3B better at lower res |
| **Shift** | Varies by workflow | Users reported various shift values; no confirmed VACE-specific default. Higher shift may increase reference adherence |
| **Sampler** | dpmpp_sde_gpu / uni_pc | Both reported to work. Experiment with your workflow |
| **Scheduler** | beta / beta57 | flowmatch_distill when using Lightning LoRA with Fun VACE |
| **Gray value for masks** | 0.5 (RGB 127,127,127) | The neutral/"empty" value for VACE. Gray = areas to generate. Black = preserve. White = full effect |
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

## 1.3B vs 14B

| Aspect | 1.3B | 14B |
|--------|------|-----|
| **Best resolution** | 480p-576p | 720p+ (needs higher res to work well) |
| **VACE block frequency** | Every other block | Every 5th block |
| **Relative speed** | ~2x slower than base 1.3B T2V | Slower still, but relatively faster VACE overhead |
| **LoRA compatibility** | Many 1.3B T2V LoRAs work (compatibility varies) | Works with 14B T2V LoRAs |
| **Reference consistency** | Good at lower res | Vastly superior for reference image consistency |
| **Control understanding** | Basic | Better understands control video nuances |
| **VRAM** | 12 GB with offloading | 16-24 GB with block swap |
| **Quality floor** | Decent at all sizes | Poor below 720p, excellent above |
| **Speed with CausVid** | Fast at 6-8 steps | Fast, CausVid at 0.2-0.4 strength optimal |

**When to use 1.3B:** Quick iterations, low VRAM setups, lower resolutions, character LoRA workflows. Results can rival 14B I2V quality with proper settings.

**When to use 14B:** Final quality renders, 720p+ output, reference consistency critical, complex multi-subject scenes.

---

## Techniques

### Reference / Style Transfer

VACE uses a reference image to maintain subject appearance and style across generated video. The reference image is encoded as the first latent frame and the model is trained to pick up likeness from it.

**Reference image preparation:**
- **White background is commonly recommended.** Remove the background from your subject and pad with white for cleaner results. Kijai advised removing background or padding with white. Some users noted the official VACE examples include gray backgrounds, so white may not be strictly mandatory. -- Kijai, Discord #wan_chatter, April-May 2025
- Dimensions must match the control video dimensions exactly.
- Use a closeup crop that matches the pose you want. If you have a closeup shot, use a closeup reference.
- Multiple subjects can be placed on the same white canvas by cutting and pasting them together.
- VACE workflows may accept a batch of reference images, but they are concatenated into a single composite reference (side by side) rather than treated as separate refs. -- melmass, Discord #wan_chatter, April 2025
- White padding around the subject may improve results.

**Strength and control:**
- VACE strength > 1.0 is possible and boosts likeness (1.5 helps DWPose following), but causes contrast/darkening issues. -- buttercup5108, Discord #wan_chatter, September 2025
- The prompt matters: VACE uses prompt-to-reference matching. Describe what is in the reference.
- **Control signals often improve results with references**, helping with motion and structure. However, ref-only workflows (without control signals) are also possible and some users report workable results. -- Discord #wan_chatter, May 2025
- VACE reference respects positioning too strongly -- subjects tend to stay where they appear in the reference frame. This can be an advantage or disadvantage depending on use case. -- Kijai, 42hub

**Split sampler technique for better motion:** When using both a start frame and a reference, motion is severely reduced. The workaround is to run the first 1-2 sampling steps without the reference frame to get motion going, then add VACE conditioning with the reference for the remaining steps. -- Ablejones, Discord #wan_resources, 2025

**Style transfer:** Users do use VACE for style/reference transfer with mixed results. Some users reported good style transfer from stylized first frames, while others found it works better for subject/background matching than pure style transfer. Results vary by workflow. -- Discord #wan_chatter, May 2025

### Inpainting

VACE excels at video inpainting -- both spatial (replacing regions within frames) and temporal (generating frames between keyframes).

**How VACE inpainting works:**
1. Prepare the input video with the masked areas filled with **gray (RGB 127,127,127 / value 0.5)**. You must bake the mask into the video itself, not just supply a separate mask.
2. Supply a matching mask where **white = areas to regenerate**, **black = areas to preserve**.
3. VACE provides more consistent inpainting than basic latent noise masking or differential diffusion, though it can be combined with both for even better results. -- Kijai, Discord #wan_chatter, October 2025

**Key tips:**
- Extend the inpainting mask slightly larger (e.g., 5 pixels) than the gray area on the video to prevent edge leaking. -- scf, Discord #wan_chatter, September 2025
- Some users reported that full denoise (1.0) works best for inpainting, though this has not been widely confirmed.
- Don't use masks with holes -- VACE has issues with discontinuous mask regions.
- Some users reported blurred masks work poorly with VACE 2.1. -- chrisd0073
- Grow mask with negative expansion to shrink slightly inside the depth map prevents mask leaking. -- HeadOfOliver
- Composite the result back onto the original footage using the alpha mask if background degradation is a concern.
- Some users reported VACE 2.1 handles spatial inpainting better than Fun VACE 2.2 (not widely confirmed).

### Outpainting

VACE handles outpainting well -- extending the visible area of a video beyond its original bounds.

- Use white for the areas to be outpainted (full effect).
- VACE remembers object details intelligently when outpainting (e.g., a partially visible scooter will be completed correctly).
- The prompt is respected during outpainting -- VACE chooses "union type" from inputs and prompt.
- Works with the Layer Forge node for HDRI dome creation in Unreal Engine. -- yukass

### Video Extension

VACE can extend videos by using the last N frames of a previous generation as the first frames of the next.

**Standard approach:**
1. Take the last 10-16 frames from the previous generation.
2. Feed them as the first frames of a new VACE generation with gray frames filling the rest.
3. Use matching masks (black for preserved frames, white for new ones).
4. Users experimented with various overlap amounts (e.g. 13-frame overlap reported by Ablejones). More overlap generally helps smooth transitions.

**Extension settings:**
- VACE strength 0.7-0.9 for subsequent segments (lower than first segment to allow motion).
- Shift value of 120 helps with motion continuity in extensions despite being much higher than the typical 4-6. -- Daviejg
- n/4+1 overlap formula may be more correct than flat 10 frames. -- JohnDopamine

**Known limitations of extensions:**
- **Color drift** has been reported by multiple users in VACE extensions. Colors may "drift over time, becoming crispier" in long continuations. Higher resolution and color-match nodes between samplers may help. -- Discord #wan_chatter, May 2025
- **Character degradation** over multiple autoregressive generations has been reported. Faces may become progressively less defined. The practical limit depends on the specific workflow and content.
- **Autoregressive burn-in** causes coherence loss over time. -- Benjaminimal
- Fun VACE 2.2 handles extensions better than 2.1, with less color degradation and better fast motion. -- Daflon, Kijai

**Alternatives for extensions:** [[svi|SVI]] has less quality loss for pure continuations. [[fun-control|Fun Control 2.2]] is better for scenes with large color changes. PUSA LoRA at strength 1.0 can extend without VACE (81 frames, 17 frame overlap, extended 7x for 30 seconds). -- Hashu, Ablejones

### Multi-Control

Users can layer controls by chaining multiple VACE encode/embed nodes. Depth and pose are the best-supported combination. Direct blended/combined controls in a single image are often unreliable; separate VACE encodes are preferred. Some users reported issues with canny and lineart controls, and support for normals is experimental.

**Chaining VACE encode nodes:**
Each VACE encode node has a `prev_vace_embeds` input. Connect the output of one encode to the input of the next to layer controls with different strengths.

**Important rules for multi-control:**
- Users often tune relative strengths across chained encodes (e.g. stronger pose, weaker depth). Examples include pose at 1.0 and depth at 0.5. There is no confirmed rule that combined strengths must stay under 1.0.
- Send each control type as its own VACE input rather than blending them into a single image (e.g., no image blend screen at 0.5). -- Ablejones
- When chaining VACE nodes at the same timesteps, it may help to include a neutral image in the "empty" encode. When applying at different timesteps, leaving the reference empty on subsequent encodes may work fine. -- Kijai, Discord #wan_chatter, May 2025
- When chaining multiple WanVacePhantom nodes, phantom and reference images must go in the **last** node before the sampler to avoid latent size conflicts. -- Ablejones
- VACE 2.2 Fun supports proper multi-controlnet blends (depth + normal + lineart), especially useful with style transfer. -- yo9o

**Control types and their quirks:**

| Control Type | Notes |
|-------------|-------|
| **Depth** | Use Depth Anything V2 (not V3, not Video Depth Anything which has banding). Blur slightly for VACE -- high-quality depth maps are treated as RGB grayscale and trigger colorize mode |
| **DWPose** | VACE was trained with DWPose. Use inverted openpose to prevent stick artifacts. DWPose better than depth for facial features |
| **Lineart/Canny** | Canny should be inverted for VACE. -- Kijai, May 2025. Early users reported mixed results with canny/lineart as VACE control inputs; some found canny just colored the input rather than controlling motion |
| **Normal maps** | Not officially trained for VACE but users experimented with them. Isolating the subject/knocking out the background before processing helps. Results are hit-or-miss |
| **OpenPose** | Pose/openpose can bleed through into output. Inverted openpose helped reduce visible stick artifacts. Pose control may have facial/hand tracking quirks |
| **Optical flow** | VACE paper shows this as input -- no signal until something moves |

### Keyframe Interpolation

VACE can generate video between arbitrary keyframes, not just start and end frames.

- Place keyframes at specific positions in the frame batch, fill gaps with gray frames, and provide matching masks.
- VACE can do true interpolation by placing input frames on every other frame and having VACE fill the missing ones.
- Works for frame rate doubling: space out frames so every other one is from the video, the rest are gray with matching masks. -- ingi // SYSTMS
- Some users reported VACE 2.1 works better than Fun VACE 2.2 for multi-frame interpolation (not widely confirmed).
- For hand-drawn animation, VACE tries to morph frames too literally. [[timetomove|TimeToMove]] may work better for that use case. -- lemuet

---

## Working with LoRAs

### CausVid LoRA

CausVid can be extracted as a LoRA and works well with VACE for faster inference:

- **Optimal strength: 0.2-0.4.** Above 0.4 reduces VACE control strength (e.g., prevents mouth movement). -- Discord #wan_chatter, May 2025
- Apply the Block Edit node to skip VACE blocks when using CausVid to prevent interference.
- Every 5th block disabling improves VACE pose following with CausVid on 14B.
- CausVid works with VACE for T2V but **not** for I2V.

### 1.3B LoRA Compatibility

Many T2V LoRAs appear compatible with VACE because the base model weights are unmodified (VACE is added alongside them). However, compatibility and quality vary by LoRA. This is an advantage over [[fun-control|Fun models]], where LoRAs trained on standard weights may not work well.

- Character LoRAs work exceptionally well. A trained character LoRA will almost always produce better likeness than image references alone. -- spacepxl, December 2025
- Hi-Res LoRA is compatible.
- Reward LoRAs (HPS 2.1, MPS) can cause issues: HPS 2.1 was found to cause anime-style artifacts in VACE outputs. Leave them out when troubleshooting. -- Gleb Tretyak
- Detail LoRAs can add too much detail to faces in VACE/I2V workflows. -- VRGameDevGirl84
- **Control LoRAs** may be incompatible with VACE since VACE is T2V-only (16 channels). Not widely tested or confirmed.
- VACE 2.1 14B only supports T2V LoRAs. I2V LoRAs will load partially but perform poorly.
- Some users reported Wan 2.2 Fun VACE may not support standard Wan 2.2 LoRAs (it is built on the 2.2 Fun architecture). Not widely confirmed.

### Speed LoRAs

| LoRA | Recommended Strength | Steps | Notes |
|------|---------------------|-------|-------|
| CausVid (extracted) | 0.2-0.4 | 6-8 | Best tested. Use flowmatch_distill if using Lightning variant |
| FusionX | ~1.0 | ~8 | Distilled merge, reported to work with VACE (exact settings not widely confirmed) |
| LightX2V | ~0.5 | 4-8 | Some users reported issues with VACE (not widely confirmed) |
| DiffSynth | ~1.0 | ~8 | Reported for watermark removal workflows (not widely confirmed) |

When using speed LoRAs with VACE + Phantom: try strength=0.5 and CFG=2.0 if CFG=1.0 worsens Phantom resemblance. -- Ablejones

---

## Common Issues & Troubleshooting

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

### Mask & Inpainting Issues

| Problem | Solution |
|---------|----------|
| Mask being ignored | Bake the mask into the video as gray areas. Also check wrapper vs native mask polarity (may need to invert) |
| Mask leaking into output | Extend inpainting mask 5px beyond the gray area. Use grow mask with negative expansion |
| Grey alpha edges on expanded masks | Known issue with mask expansion. Use precise masks instead |
| Inpainting not replacing anything | Need BOTH gray fill on the video AND a separate mask. Gray alone oversaturates, mask alone does nothing |
| Seams with tight crop inpainting | Add more padding of unmasked area. Use bigger sampling area. Composite back with grow mask and border blending |
| Masks with holes cause issues | VACE does not handle discontinuous masks well |

---

## VACE 2.2 (Fun VACE)

Fun VACE is the Wan 2.2 version of VACE, created by the Fun team at Alibaba PAI. It reportedly supports both high-noise and low-noise sampling, expanding on VACE 2.1. Note: the Fun VACE 2.2 details in this section are from later extraction sources and were not verified against the raw Discord messages checked during verification.

### Key Differences from VACE 2.1

| Aspect | VACE 2.1 | VACE 2.2 (Fun VACE) |
|--------|----------|---------------------|
| **Noise support** | Low noise only | High noise AND low noise |
| **Fast motion** | Struggles | Significantly better -- main advantage |
| **Reference adherence** | Better for face/subject | Worse reference handling, multiple refs contaminate |
| **Inpainting** | Significantly better | Worse -- "forgot some things like inpainting" (Ablejones) |
| **Color shifting** | More color drift in extensions | Reduced color shifting |
| **Blurred masks** | Always broke | Handles them better |
| **OpenPose following** | Weak | Much better at following OpenPose |
| **Environment lighting** | Better integration | Doesn't integrate lighting as well |
| **Depth control** | Good | Better understanding of depth |
| **Detail quality** | Standard | Better quality and detail preservation |
| **Video extensions** | More color degradation | Better for continuation/extension |
| **Multi-controlnet** | Separate encodes needed | Proper multi-controlnet blends supported |
| **Canny/lineart** | Inverted canny recommended | Polarity may differ (not confirmed) |
| **Speed LoRA** | CausVid well-supported | Lacks proper distill LoRA for high noise |
| **Relight feature** | None | Hidden relight: relights foreground to match background when BG replaced with gray |

### High/Low Noise Split

VACE 2.2 uses two modules -- **High Noise** and **Low Noise** -- corresponding to the [[wan-2.2]] dual-model architecture.

- **Do not swap the High and Low modules** -- plugging them into the wrong slots produces garbage.
- Typical setup uses 3 samplers or schedules CFG/LoRA strengths across the noise levels.
- Can mix: VACE 2.2 for high noise + VACE 2.1 module for low noise (2.1 performs better on low-noise side for natural, integrated results). -- Ablejones
- Can also use VACE 2.2 for high noise + Phantom for low noise for superior output. -- Ablejones
- Fun VACE works without needing both samplers -- using only the low model works fine for many tasks. -- lemuet

### Community Opinions (as of early 2026)

Opinions on VACE 2.1 vs Fun VACE 2.2 are mixed and depend heavily on workflow. Some users report preferring VACE 2.1 for most tasks:

- **Use VACE 2.1 for:** Inpainting, reference preservation, face consistency, wide shots, multi-frame interpolation, spatial masking, character LoRA workflows
- **Use Fun VACE 2.2 for:** Fast motion, OpenPose following, video continuation/extension, high noise work, dual-model 2.2 workflows, depth control

> "VACE 2.1 generally better regarded, Fun VACE 2.2 better for fast motion and maintaining likeness." -- Kijai, Discord #wan_chatter, September 2025

> "Fun VACE 2.2 is better than VACE 2.1 -- better in every way from testing, even ignoring the extra High Noise part." -- Ablejones, Discord #wan_comfyui, October 2025

These contradictory assessments likely reflect different workflows and use cases.

---

## Combining VACE with Other Models

### VACE + Phantom

The most powerful combination for character consistency with structural control.

- Phantom handles character identity (better at likeness than VACE reference).
- VACE provides structural control (depth, pose, inpainting).
- Setup: Phantom reference images go in the Phantom input, control signals go in the VACE encode. Do not add VACE reference unless you have a specific reason. -- Ablejones
- Phantom embed nodes have a VACE embed input for integration. Specific strength settings may vary by workflow.
- Use diverse reference images for Phantom merge for better character consistency across angles.
- Phantom prefers simple but real background. VACE reference likes white background. -- Ablejones

### VACE + HuMo

- Some users reported that VACE and HuMo cannot be used simultaneously in the same sampling pass, and suggested splitting them across noise levels. Not verified against raw messages.

### VACE + Lynx

- Some users reported Lynx lite works with VACE for face ID control. Not verified against raw messages.

### VACE + PUSA

- Some users reported PUSA works with VACE for maintaining reference likeness. Not verified against raw messages.

### Incompatible Combinations

| Model | Why |
|-------|-----|
| I2V models | VACE is T2V only (16 channels) |
| HuMo (same pass) | Different conditioning systems |
| MagRef | MagRef is I2V, VACE is T2V |
| Control LoRAs | May be incompatible since VACE is T2V-only (16 channels); not widely tested |
| WanMove | Incompatible control systems |
| LongCat | Too different architecture and dimensions |
| SVI 2.0 Pro | Reported as I2V-only (not verified against raw messages) |
| PainterI2V | Reported as I2V-only (not verified against raw messages) |

---

## Advanced Workflows

### Upscaling with VACE

Users experimented with latent upscaling passes alongside VACE, reporting some success:
- Use the original video as control input at the target resolution.
- Specific strength/denoise settings vary by workflow (not widely confirmed).
- Use CPU cache for VAE instead of tiled VAE to avoid quality degradation.

### Two-Pass Workflows

1. **VACE + Vanilla refinement:** First pass with VACE (60 steps with pose + ref), second pass with vanilla 1.3B + enhancement LoRAs (8 steps) for quality improvement.
2. **VACE + 2.2 Low refinement:** Generate with VACE 2.1, then 1-2 steps of 2.2 Low model to clean up output. -- spacepxl, December 2025
3. **Any first pass + HuMo second pass:** Use T2V+VACE, WanAnimate, or MagRef as first pass, then HuMo for lip sync and refinement. -- VRGameDevGirl84

### VFX Compositing Pipeline

For integrating 3D assets or CG elements into live footage:
1. Track the shot, add 3D asset in Blender/AE.
2. Create infill mask for the CG insertion area.
3. Generate DepthAnything map of the scene.
4. Use reference image + VACE + Wan 2.1 to harmonize the composite.
5. Feather depth on corners for camera matching. -- Nathan Shipley, Neex

### Long Video Generation

- **VACE** can create very long videos using frame overlap with gray padding for continuation. Users discussed feeding prior frames plus N gray frames at the same resolution into VACE embed. -- Discord #wan_chatter, May 2025
- **Context windows** work with VACE 2.2 but slow things down exponentially. Custom slicing of context windows now merged into ComfyUI for use with VACE and Phantom inputs.
- **Segment and extend:** Split control video into chunks with overlap for unlimited length.
- **Seam repair:** Use VACE to fix jumps at connection points between clips by masking the seam area with gray and white masks.

---

## VACE vs Other Control Methods

| Method | Strengths vs VACE | Weaknesses vs VACE |
|--------|-------------------|---------------------|
| **[[phantom]]** | Better character identity / likeness | No structural control (depth, pose) |
| **[[fun-control]]** | Faster (1/3 VRAM and time), handles cuts better | No reference subject feature, inconsistent quality |
| **[[wananimate]]** | Less tweaking needed, includes motion | Poor character consistency, rigid masking, too controlling |
| **SkyReels DF** | No color shift in extensions | Based on I2V, different ecosystem |
| **SVI/SVI-Film** | Less quality loss in extensions | No controlnet or prompt control, I2V only |
| **I2V models** | Better first-frame likeness preservation | Less versatile, no inpainting/outpainting |
| **FaceFusion** | Simpler setup | VACE "incomparably better" -- handles lighting, partial occlusion, no flickering |
| **SCAIL** | Superior 3D pose data | Narrower use case |

Community opinions on VACE vary. Some users strongly prefer VACE for VFX work, while others find I2V or other control methods better suited to their workflows. The choice depends heavily on the specific use case.

---

## Known Limitations

- **T2V only.** Cannot work with I2V models, period.
- **Single reference image.** Only one reference is supported natively. Multiple images get concatenated but model limitation remains.
- **Color drift in extensions** has been reported by multiple users and can be difficult to eliminate.
- **Character degradation** over multiple autoregressive generations.
- **~2x slower** than base model due to 15 additional blocks running every step (1.3B) or 8 blocks every 5th step (14B).
- **Lipsync interaction.** Some users speculated VACE may affect existing lip sync in content (not widely confirmed).
- **Style consistency** with new surfaces -- struggles to maintain specific art styles (e.g., flat color/cartoon).
- **Normal maps** are not a trained modality; results are hit-or-miss.
- **No VACE for 5B model.** Currently only exists for 1.3B and 14B.
- **Morphing vs animation.** VACE tends to morph images between keyframes rather than creating true animated movement. Better for smooth transitions than discrete motion.
- **Tiled VACE encoding** is very slow and lower quality than standard encoding.

---

## Timeline

| Date | Event |
|------|-------|
| March 2025 | VACE paper published by Alibaba |
| April 2025 | 1.3B Preview available on HuggingFace (by April 1). Kijai adds wrapper support, extracts standalone module, memory optimizations |
| May 2025 | Official 1.3B and **14B** versions released. CausVid compatibility confirmed. Native ComfyUI support begins |
| June-Aug 2025 | Community develops workflows: Phantom+VACE, multi-control, extension pipelines |
| September 2025 | **Fun VACE 2.2** released by Alibaba PAI team with high/low noise support. Kijai releases bf16/fp8/GGUF conversions |
| October 2025 | Ditto VACE variant released for style transfer. WanVaceAdvanced custom nodes mature |
| November 2025 | WanVacePhantomDualV2 node. Context window support merged into ComfyUI |
| December 2025 | FreeLong++ for VACE (640 frames in one batch). Motion scale control node. WorldCanvas identified as 2.2+VACE-like |
| January 2026 | OmniVCus identified as VACE module. SCAIL emerges as alternative for 3D pose |

---

## See Also

- [[wan-2.1]] -- Base model family for VACE 2.1
- [[wan-2.2]] -- Base model family for Fun VACE
- [[phantom]] -- Character consistency model, best paired with VACE
- [[comfyui]] -- Node-based UI for running VACE workflows
- [[quantization]] -- GGUF and fp8 formats for VACE modules
- [[speed]] -- CausVid, FusionX, LightX2V acceleration LoRAs
- [[wananimate]] -- Alternative control method
- [[fun-control]] -- Fun team's lighter control model
- [[lora]] -- Training and using LoRAs with VACE
- [[ditto]] -- Style transfer VACE variant

## External Resources

- [VACE Project Page](https://ali-vilab.github.io/VACE-Page/)
- [VACE GitHub Repository](https://github.com/ali-vilab/VACE)
- [VACE Paper (arXiv)](https://arxiv.org/pdf/2503.07598)
- [VACE User Guide (Official)](https://github.com/ali-vilab/VACE/blob/main/UserGuide.md)
- [ComfyUI-WanVaceAdvanced](https://github.com/drozbay/ComfyUI-WanVaceAdvanced)
- [Wan 2.2 VACE User Guide (Nathan Shipley)](https://nathanshipley.notion.site/Guide-VACE-with-Wan-2-2-in-ComfyUI-27191e115364802186aacc04c00d71f3)
- [Wan 2.1 Knowledge Base - VACE Section](https://nathanshipley.notion.site/Wan-2-1-Knowledge-Base-1d691e115364814fa9d4e27694e9468f#1d691e11536481f380e4cbf7fa105c05)
