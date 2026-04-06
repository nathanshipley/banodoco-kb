---
title: WanAnimate
aliases: [wan-animate, wananimate, wan animate, wan-2.2-animate, wan animate 2.2]
sources_ingested: 6
last_updated: 2026-04-05
---

# WanAnimate

WanAnimate is Alibaba's character animation / motion transfer model in the Wan family, released mid-September 2025. It takes a driving video (providing pose + facial performance) and a reference character image, and produces a video of the reference character performing the driving video's motion. It can also replace a character inside existing footage (character swap) when run with masks and background frames.

Despite being branded "Wan 2.2 Animate," WanAnimate is architecturally closer to [[wan-2.1]] I2V: "Wan Animate is closer to 2.1 architecture. LoRA 2.2 are not compatible with wan animate." -- Kijai, Discord #wan_chatter, September 2025. In practice this means 2.1 LoRAs and 2.2 *low-noise* LoRAs both work; 2.2 MoE LoRAs do not.

> "WanAnimate is clearly best for vid2vid." -- Kijai, Discord #wan_chatter, September 2025

> "WanAnimate takes things to a whole new level compared to AnimateDiff." -- T2 (RTX6000Pro)

---

## What It Does

WanAnimate operates in two main modes:

1. **Animation mode** (character animation from pose/face) -- reference character image + driving video -> the reference character performing the driving motion. Disconnect `bg_images` and `mask` inputs to run in this mode; the background comes from the reference image.
2. **Replacement mode** (character swap inside existing video) -- driving video + reference character + mask + background frames -> the same video with the character swapped. Includes a relight LoRA to help blend the new character into the scene lighting.

It also supports:

- **Face control** -- facial expression/performance is transferred via a face adapter, not just skeleton pose. It tracks lip sync and gaze direction, which is unusual for pose models.
- **Animal poses** -- VitPose in the WanAnimatePreprocess nodes can detect animal skeletons, enabling quadruped animation. -- Nathan Shipley, Hashu
- **Trajectory/ATI-style control** -- can follow point trajectories for object movement, not just dance poses. Accepts first-frame, last-frame, one ref slot, controlnet, and trajectories simultaneously. -- Gleb Tretyak, Discord #wan_chatter, November 2025
- **RGB driving input** -- you can feed RGB video directly as control without a preprocessor; it will follow structure and motion, losing a bit of likeness but handling foreground-occluded scenes better than pose.

---

## Setup & Requirements

### Model Files

- **Original release:** `Wan2.2-Animate-14B` (14B parameter model, ~64 GB full precision, released with included relighting LoRA).
- **Kijai conversions:** fp8_scaled, bf16, and a v2 fp8_scaled (fixes grid noise pattern in native ComfyUI).
- **GGUF quantizations** by patientx and The Punisher: Q2, Q3, Q4_0, Q4_K_M, Q6, fp8_e5m2. Kijai recommends Q8 with offloading instead of lower quants if RAM is available.
- **Relight LoRA** -- shipped alongside the model, for character-replacement lighting blend.

### VAE & Base

WanAnimate uses the **Wan 2.1 VAE** (it is based on the 2.1 I2V architecture, not 2.2). Wan 2.1 T2V will also load because base layers are the same. -- xiver2114

### ComfyUI Nodes

Two implementations exist and the wrapper is generally considered superior:

| Implementation | Notes |
|---|---|
| **Kijai WanVideoWrapper** | "Animate quality in wrapper is 5x better than native" -- asd. Better prompt adherence, looping, handles empty face images automatically. |
| **Native ComfyUI** | Better backplate cleanup in character replace; slightly better gaze control. Requires manually feeding black face images when not using face input. |

The `ComfyUI-WanAnimatePreprocess` custom node package (Kijai) replaces manual pose/face detection with automatic VitPose-based detection, SAM2 masking from keypoints or bbox, and optional Flux Kontext reference retargeting. V2 of this workflow gives substantially cleaner face transfer and better eye quality than V1.

### VRAM & RAM

| Setup | Resolution | Frames | VRAM | Notes |
|---|---|---|---|---|
| fp8_scaled + LightX2V | 480p | 77 | 12 GB | With blockswap, lighter text encoder |
| fp8_scaled | 720p | 77-81 | 16-24 GB | Blockswap 20-40 |
| bf16 | 720p | 77 | ~32 GB | Slightly better quality than fp8 |
| GGUF Q4 | 720x400 | 101 | 10-12 GB | ~200s on RTX 3090 (lightweight workflow) |
| bf16 | 1920x1080 | 77 | 96 GB | "Basic Wan Animate at 1920x1080" -- Fill |

**System RAM is the real bottleneck for long generations:** 64 GB is a minimum; 128 GB is recommended for 200+ frame runs without context windows, since the model holds all decoded frames in system memory before returning them. "WanAnimate crashes when returning 1000+ frames -- it's a RAM issue, not VRAM. The model had VRAM to spare but crashed when returning the frames to system memory." -- Kijai

On 5090s, Wan Animate has "larger blocks so heavier compute load" -- power supply instability has been reported; disable `--async-offload` and `--pinned-memory` if hitting silent crashes.

---

## Key Settings

These are the defaults in the wrapper / native templates, plus community-validated tweaks:

| Parameter | Default | Notes |
|---|---|---|
| **Steps** | 20 (CFG) / 6-8 (LightX2V) | 25-step Euler CFG 1.2 has better init adherence than 8-step LightX2V, though LightX2V is usable |
| **CFG** | 1.0 | Original code never uses CFG; CFG > 1 often degrades results |
| **Shift** | 5.0 | Model default |
| **Scheduler** | Euler | Preferred: "less jiggly and better contrast" -- CaptHook. LCM works. DPM++ SDE reported as worst. UniPC slightly sharper in eyes. |
| **Prompt** | `视频中的人在做动作` | Chinese text meaning "the person in the video is performing actions". This is the hardcoded default prompt in the original code. |
| **Frame window size** | 77 (short) / 81 (long) | Short clips: set `frame_window_size == num_frames` to disable built-in looping |
| **Num frames** | multiples of 77 | Reference adds an extra latent, so 77 becomes 81 at inference time. Also valid: `4n+1` (49, 53, ...) in latent space. |
| **fps** | 12-16 | 12 fps is better for pose consistency than 24; 24 fps causes "awkward cuts and pose failures" per Kijai. 16 fps is the standard. Some users report 24 fps works better with specific workflows. |
| **Face strength** | 1.0 | Set to 0 to disable face performance transfer. Needed ≥1.0 when masking. |
| **Pose strength** | 1.0 | Increase to 1.3 if lip sync is delayed. Reduce if losing face likeness. |
| **Relight LoRA strength** | 0-1 | "Hit or miss. Leave it in and turn to 0 or 1 depending on need. Works better when sources have similar brightness." -- U̷r̷a̷b̷e̷w̷e̷ |

> Contradiction flag: 12 fps vs 24 fps. Kijai's position is clearly 12 fps for pose consistency; NC17z reports 24 fps works better than 16 fps for his pipeline. The safest default is 16 fps, matching the driving video source fps.

### Inference Specifics

- WanAnimate runs two rounds of 20-step sampling internally (the architecture does inference twice). -- ˗ˏˋ⚡ˎˊ-
- It is "trained for 78-frame chunks" -- can go longer but in 78-frame chunks. -- DawnII
- Extends automatically via sliding window with 1-frame overlap: 0-77, 76-153, 152-229. -- Kijai
- Output frames must be divisible by 4 after the first frame, which is why output sometimes has 2-3 fewer frames than input. -- Kijai
- Maintains 1:1 frame count with input (121 frames in = 121 frames out at 77-frame windows). -- A.I.Warper
- Supports temporal reference for automatic extensions (similar to InfiniteTalk), trained for up to 2 extensions. -- Kijai

---

## Blocks & Strength Scaling

WanAnimate exposes block-range scheduling (wrapper-only) for fine-grained control vs prompt following:

| Block range | Effect |
|---|---|
| 0-5, 0-9 | Light likeness nudge, preserves prompt freedom |
| **0-15** | Recommended default: "nice results but hair can be overexposed" -- Kijai |
| 10-39 | Heavier likeness, less prompt following |
| 15-39 | Very strong character lock |

- Strength **2.0 is too much** on Wan 2.2 -- ruins prompt following and motion. Keep strength at or below 1.0.
- WanAnimate is "generally too strong and ruins prompt following and motion" -- Kijai. Blocks 0-15 is the standard trade-off.
- **`start_percent=0.5`** is a useful trick: "Using start percentage 0.5 with WanAnimate allows better prompt following and motion while still getting likeness. Only needs a few steps to get likeness." -- Hashu
- Face adapter blocks are part of the main blocks (every 5th, total 8) and are included in block swap for VRAM reduction.

---

## Prompting

- **No CFG by default.** `cfg=1.0` effectively disables negative prompts. Use a NAG node (Normalized Attention Guidance) if you need negatives; dial in alpha and tau until it affects output without killing quality.
- **Hardcoded Chinese prompt.** The original code uses `视频中的人在做动作` ("the person in the video is performing actions") regardless of what you pass. Chinese negative prompts tokenize differently (126 tokens vs 99 English) and produce dramatically different results even when semantically translated.
- **Keep prompts simple** -- the model is sensitive and can break references if prompts are misaligned. "Empty prompting works fine for Wan Animate. Prompting can break the references pretty badly if not aligned." -- Piblarg
- Use Florence2 or ChatGPT for auto-captioning reference images, then strip to the bare minimum.
- Prompt for motion in the scene ("driving a car", "dancing") when the background should move -- otherwise backgrounds stay static.
- First step with CFG gives better likeness; some users apply CFG only on step 0 then drop it.
- Put `geisha` in the negative prompt to prevent characters incorrectly turning Asian. -- mdkb
- "Snow"/"dust" artifacts -- add them to the negative prompt.

---

## Inputs

### Pose / Canny / Driving Video

- Uses **VitPose-H** internally (not DWPose), with a hardcoded 256x192 input resolution.
- VitPose can extract human joints from hand-drawn sketches and stick figures -- usable as driving source without real video. -- dj47
- VitPose only handles **one person at a time**; use DWPose for multi-person scenes.
- **Inverted canny required** -- unlike regular canny, WanAnimate expects white background with black edges. Using non-inverted canny causes static backgrounds and bad results. -- Ablejones
- Pose input accepts **depth maps mixed in**, useful for backward-facing scenes where pose estimation fails. -- Clément
- Lines work better than dots for control inputs; solid shapes also work well. -- Mads Hagbarth Damsbo
- You can feed raw RGB video as control without a preprocessor; it follows motion and structure at a small cost to likeness.

### Reference Image

- **Single reference only** -- multiple references cause extra arms / errors. -- Kijai
- **Closer framing helps likeness.** "You want to smell their digital breath." Crop tighter and prompt for the face being prominent.
- **Back-shot references** help with character turn-arounds.
- **T-pose characters work best** because Flux Kontext preprocessing is biased toward T-pose. -- Kijai
- Higher-resolution reference = better face texture, since more pixels go to the face.
- Reference image in the same pose/position as first frame of the guiding video gives much better consistency.
- **Flux Kontext step** in the preprocessor aligns the reference with the first video frame automatically.

### Face Images

- If you use masking but no face images, masking breaks -- pass **empty (black) images for every frame** as a workaround. The wrapper handles this automatically; native requires manual input. -- Kijai
- Face model input is hardcoded to 512x512, which can cause warped crops on extreme profiles.
- Disconnect `face_images` if you don't want facial performance transferred -- works fine without the blocky black mask.
- Disconnect `clip_vision` from the encode node for better likeness as the video progresses and after the first context window.
- "With clip embeds: better identity but worse lighting. Without: better lighting but worse identity." -- Kijai

### Masking

- The model is trained to handle **blocky masks only** -- also works with square masks but not smooth masks. A custom node converts normal masks into the blocky style. -- Kijai
- Masking is **rigid** -- use grow/blur, or switch to VACE for precise masks.
- **Mask everything you want to replace** including hair, face, and body. The model prefers larger masks over too-small ones.
- SAM 2.1 is better than earlier SAM versions for this task. SEC masking is solid and works better than SAM2 alone. Qwen2.5VL tagging outperforms Florence2 for mask generation (155 frames in 30s).
- For chibi / non-standard body proportions, greatly expand the mask (200+ pixel expansion makes a massive difference). -- David Snow
- **Disconnect bg_images and mask entirely** to run WanAnimate as a character animation model (reference provides background) instead of character replacement.
- Removing bg_images and mask also turns WanAnimate into a "stronger VACE/Fun controlnet". -- slmonker

---

## Resolution & Dimensions

- **All image inputs must be divisible by 16** for long videos. If dimensions aren't divisible by 16, you can only generate exactly 77 frames. -- BestWind
- **Generate at 720p or higher** for better pose following and likeness; WanAnimate, like VACE and Phantom, benefits strongly from higher resolution.
- 832x480 works; 480x832 has issues in some segmentation workflows.
- 1920x1080 produces excellent quality on 96 GB VRAM systems, no post-processing needed.
- For vertical phone video, if mask nodes flip vertical -> horizontal, pre-rotate with `ffmpeg -vf "scale=1080:1920"`.

---

## Techniques

### Character Replacement Pipeline

1. Extract first frame of driving video, edit with Seedream or Qwen Image Edit to replace the character cleanly.
2. Use SAM masking workflow (Kijai's example) for the character region.
3. Load into WanAnimate with background images and mask connected.
4. Apply relight LoRA at 0.5-1.0 for lighting blend.

Alternative: "Adding character in second pass works better -- smaller mask, cleaner results, faster processing." -- boorayjenkins. Generate the scene first, then add the character on top with a minimal mask.

### Long Video Generation

Two mechanisms are available (vs SCAIL's single mechanism):

1. **Built-in sliding window** -- automatic, 1-frame overlap, processes 77-frame chunks. Frame windows are fixed, which causes hallucination after the input clip ends.
2. **Context windows** (`WanVideo Encode Latent Batch` with context options) -- works after bug fix in Oct 2025. Minimizes color drift but causes background morphing. Less "frying" than built-in windows.

For maximum stability over long sequences:
- Set blockswap to 40 for 389 frames at 720x1280 on 64 GB RAM. -- Kijai
- Use `tiled_vae` option in WanVideo Animate Embeds for higher frame limits.
- Set `num_frames == frame_window_size` when using context options (disables built-in looping).
- Concat latent image trick reduces flash during long generations. -- Gleb Tretyak

### Speed (LightX2V & Lightning)

- LightX2V turns 40+ minute generations into 11-minute 8-step generations.
- Use **2.1 LightX2V** (not 2.2) because WanAnimate is 2.1-based.
- Delay caching for a few steps on both models when using LightX2V to avoid quality degradation.
- FastWan + LightX enables 2-step generation at acceptable quality.
- RCM distill LoRA (Nvidia) is an alternative to LightX2V with good character consistency and prompt adherence.
- Use `cfg` and avoid the "first step 0 lora trick" if speed LoRAs are breaking prompt adherence.

### Extension / Continuation

- Supports 2 automatic extensions via temporal reference (similar to InfiniteTalk).
- `continue_motion_max_frames` parameter controls extension behavior.
- For very long runs, use Uni3C instead of trying to match cameras with WanAnimate directly.
- Two-pass pipeline: 1) WanAnimate + Uni3C, 2) Extract depth via VDA, 3) Re-run with VACE and context windows for long consistent generations. -- NebSH

### Multi-Model Pipelines

- **WanAnimate + V2V InfiniteTalk at 50% denoise** is claimed as a current SOTA stack. -- ArtOfficial
- **SCAIL -> WanAnimate** -- use SCAIL for pose retargeting to different body proportions, then WanAnimate for facial performance stability. -- Juan Gea
- **Alternate single steps** between WanAnimate and SCAIL samplers for combined benefits. -- mallardgazellegoosewildcat2
- **Flux Krea w/ PuLID -> Wan S2V -> Qwen 2509 -> WanAnimate 2.2** is a full production pipeline example. -- Zlikwid

---

## Quirks & Gotchas

- **No CFG by default** -- CFG 1.0, 20 steps, shift 5.0. CFG is present in the code but not used. Using CFG > 1 often makes things worse.
- **Pupil / gaze tracking doesn't always fire locally** -- the website version tracks pupils perfectly while local versions often don't. Setting face strength to 0 fixes eye gaze problems, suggesting a face-processing bug. -- A.I.Warper
- **Chinese default prompt** -- the original code hardcodes `视频中的人在做动作`.
- **Face pixels set to -1** for unconditional generation in the original code.
- **Reference frames included and later cut** (similar to VACE), which explains why input frames become +4 during sampling.
- **Masking breaks without face images** -- pass empty black images as workaround.
- **Runs sampling twice** (2x20 steps internally).
- **Overexposes characters** slightly by default.
- **Tends to degrade over time** for very long generations -- OneToAll Animation and SCAIL are reportedly more stable over very long sequences.
- **The model is very sensitive to prompts** -- keep them simple.
- **Relight LoRA causes identity drift** in some cases -- disable for 2D/anime characters.
- **Bottom of objects go wonky** with the relight LoRA enabled.
- **2.2 LoRAs (MoE) are NOT compatible**; only 2.1 LoRAs and 2.2 **low-noise** LoRAs work. Use the 2.2 Low Noise LoRA at weight 1.0 alone.
- **LoKr format not supported** for WanAnimate LoRAs. -- boorayjenkins
- **Animate "adds lips to every character"** regardless of reference image -- generate multiple seeds for close matches. -- Sal TK FX
- **Anime characters have mouth-scale issues** -- the model forces human anatomy onto smaller anime mouths.

---

## Troubleshooting

| Problem | Solution |
|---|---|
| OOM with 77 frames on A100 42GB / RTX 5090 | Enable LoRA merging in LoRA load node; check power supply on 5090 |
| OOM on 12 GB VRAM | Blockswap, lighter text encoder (6 GB instead of 11 GB), lower resolution first |
| RAM saturating with high block swap | Start with 16 blocks on 32 GB RAM, don't go too high |
| Crashes returning 1000+ frames | RAM issue, not VRAM -- need 128 GB for long runs without context |
| Tensor size mismatch | Happens with < 77 input frames; match to 4n+1 pattern |
| 36 channel error | Update nodes to main branch, check for conflicting custom node class names |
| Resolution / frame count error | Dimensions must be divisible by 16 |
| OOM after ComfyUI update | Roll back to Oct 12-13 commit; or add `--disable-pinned-memory`, remove `--fast` and `--async-offload` |
| Torch compile breaks after update | Mixed-precision update broke compile in general |
| `FloatTensor vs CUDABFloat16Type` with bf16 | Cannot merge LoRAs with low-mem load enabled for bf16 WanAnimate |
| Snow/dust artifacts | Add to negative prompt (requires NAG since CFG 1.0) |
| Grid noise pattern | Use the v2 fp8_scaled model |
| Black mask box around V2 output | Add black face images instead of disconnecting; ensure face strength ≥ 1.0 |
| Flickering black blocks | Enable `fl2v` switch on the node for 2.2 models |
| Face shaking / jitter | Use old preprocessor workflow, or disconnect face_images if not needed |
| Losing face likeness without LightX | Reduce pose strength, increase face strength; or keep LightX LoRA for its face-preserving side effect |
| Overexposure on long runs | Use LCM, fewer steps, weaker settings, or context windows instead of frame windowing |
| Character cheeks read as sad lips | Prompt/seed issue; animate-adds-lips behavior |
| Asian eyes squinted/closed | Disconnect bg_images and mask; background from reference |
| Anime converted to realistic | Disable LightX2V 2.1 LoRA, add "anime, animation, 3D" to prompt |
| Clothes changed instead of face | Use face detector node instead of SAM2, or make mask cover whole person |
| Character LoRAs not working | Only 2.1 LoRAs or 2.2 Low-Noise LoRA (weight 1.0 alone) work |
| Poor LoRA results | Trigger word in captions, train on 720p images+videos, rank 32 instead of 64 |
| Shift/transition visible in video | Tighter mask around subject, leave thin edge on top, 50% coverage on problematic areas |
| Color drift between windows | Known issue; context windows vs built-in is a tradeoff |
| Depth input turns green | Blend method similar to VACE needed; depth training isn't reliable |
| Black screen with clip embeds + sageattn | Disconnect clip output, or use `PatchSageAttentionKJ` with `sageattn_qk_int8_pv_fp16_cuda` |
| Black result when torch compiling | Related to SageAttention auto mode with clip vision |
| Native black image while wrapper works | Check all settings match; wrapper handles empty face inputs, native doesn't |
| Blocks visible in subject replacement | Native doesn't send empty pixels when face isn't used -- use wrapper, or ensure face adapter executes |
| `WanAnimatePreprocess` nodes not loading | Browser cache -- restart browser or clear cache |
| Onnxruntime JIT error on RTX 50-series | Set ONNX device to CPU |
| OpenCV error in preprocess | Face not in full view (side profile) -- use crop-by-mask |
| Pose/bone bigger than mask | Set padding to 0, don't use reference image with masking |
| `load_video` path format error | Set path format to "wan" |
| OOM with Uni3C + WanAnimate | Disconnect both bg_images and mask |
| Output 2-3 frames short | Normal -- output must be divisible by 4 after first frame |
| Hair cut off in reference | Change KJ workflow resize from "stretch" to another mode |
| Flickering background in static scenes | Use inverted canny, prompt for motion |

---

## LoRA Compatibility

| LoRA type | Works? |
|---|---|
| Wan 2.1 T2V LoRAs | Yes (base layers are identical) |
| Wan 2.1 I2V LoRAs | Yes (WanAnimate is 2.1 I2V architecture) |
| Wan 2.2 Low-Noise LoRAs | Yes, at weight 1.0 alone |
| Wan 2.2 High-Noise LoRAs | No |
| Wan 2.2 MoE (dual) LoRAs | No -- use only the Low-Noise half |
| LightX2V 2.1 | Yes, strongly recommended |
| LightX2V 2.2 | No |
| Character LoRAs | Yes, often still needed for strong likeness -- "Wan Animate still needs character LoRA in testing" -- Dream Making |
| LoKr format | No |
| Relight LoRA (bundled) | Yes, 0-1 strength |

For training custom WanAnimate character LoRAs: use trigger words in captions, train on 720p images with videos, rank 32 instead of 64, skip mentioning clothing if you want the training-data outfits to appear.

---

## Comparison to Other Models

| Model | vs WanAnimate |
|---|---|
| **[[vace]]** | VACE has stronger native control and is "10x more useful for real VFX work" (spacepxl). WanAnimate saves time by keeping everything in one model. VACE is far better at depth; WanAnimate doesn't understand depth at all. |
| **[[phantom]]** | Phantom has better 1:1 likeness for fine details. Phantom+VACE combined is still considered best overall likeness. Disagreement: Quality_Control says WanAnimate is more accurate. |
| **Fun VACE 2.2 + pose** | May outperform WanAnimate for some character animation cases. -- Guus |
| **SCAIL** | Better for plain pose control, complex movements (spinning, multi-character), body retargeting to non-human proportions, and ID retention. WanAnimate better for facial performance / dialogue and long-gen stability. Use both in sequence: SCAIL -> WanAnimate. |
| **OneToAll Animation** | Better at pose retargeting and reference keeping; better for long clips. WanAnimate still wins on init adherence and likeness. |
| **SteadyDancer** | Doesn't do face at all -- unfair comparison. |
| **UniAnimate** | UniAnimate still wins at pose handling specifically. |
| **MoCha** | Better eye movement and lighting, better scene integration, no pose detection needed. But worse ID preservation, worse image quality, 2x compute. |
| **Runway Act 2** | "Basically Runway's Act 2 but better." -- VRGameDevGirl84 |
| **Kling O1** | O1 matches input head more closely; WanAnimate has better lighting and feels more natural. |
| **FlashPortrait** | Uses the same face encoder as WanAnimate; its "6x acceleration" is just LightX2V. |
| **LivePortrait** | WanAnimate's face detection is more stable; LivePortrait jitters on head rotation/scale. WanAnimate also handles glasses correctly. |
| **InfiniteTalk** | Ranking: InfiniteTalk > WanAnimate > HuMo for pure audio-driven lip sync. WanAnimate wins for full-body motion + face. |
| **AnimateDiff** | "Takes things to a whole new level." |
| **Wan 2.5 lip sync** | "Much more natural looking than InfiniteTalk or WanAnimate" for dialogue. |

---

## When to Use WanAnimate

- Character swap in existing footage where you have a clean reference
- Motion transfer from a performance video to a new character
- Dialogue / facial performance (best-in-class for face + lips + gaze)
- Full-body dance and action with good pose fidelity
- Animal / quadruped animation (VitPose supports animal skeletons)

## When NOT to Use WanAnimate

- Precision VFX work (use [[vace]])
- Fine-detail character likeness (use [[phantom]] or Phantom+VACE)
- Depth-aware composites (use [[vace]])
- Very long (>200 frame) clips where ID drift matters (use SCAIL or OneToAll)
- Complex spinning or non-standard body proportions (use SCAIL)
- Multi-person scenes with face tracking (VitPose is single-person)

---

## Timeline

| Date | Event |
|---|---|
| Sep 2025 | **Wan 2.2 Animate 14B** released on HuggingFace with bundled relight LoRA. "Wan Animate, formerly VACE" announcement uses VitPose + LIA + face/body adapters. ComfyUI native and Kijai wrapper implementations pushed within days. |
| Sep 2025 | GGUF quantizations (Q2/Q3/Q4/Q6/fp8) by patientx and The Punisher. piscesbody releases modified Qwen2.5VL-based masking. |
| Sep 2025 | `ComfyUI-WanAnimatePreprocess` released by Kijai with automatic VitPose face/pose detection. V2 example workflow with fp8_scaled fix. |
| Sep 2025 | Replicate API hosts WanAnimate at ~333 seconds for $1. |
| Oct 2025 | Context windows work with WanAnimate after bug fix. Face adapter blocks moved into main blocks for block-swap VRAM reduction. V2 fp8_scaled released (fixes grid noise). |
| Oct 2025 | Native torch RMSNorm support (9x faster RMSNorm) in ComfyUI nightly. Confirmed architecture is 2.1 I2V-based. |
| Nov 2025 | ATI-style trajectory support confirmed, multiple simultaneous control inputs (first frame + last frame + ref + controlnet + trajectories). OneToAll Animation emerges as pose-retargeting competitor. |
| Dec 2025 | SCAIL emerges as strong alternative; community settles on "SCAIL for body retargeting, WanAnimate for facial performance." FlashPortrait identified as same face encoder. |
| Jan-Feb 2026 | David Snow's chibi workflow (200+ pixel mask expansion). HY-Motion 1.0 pairs well as driving video generator. |

---

## See Also

- [[wan-2.1]] -- Base architecture WanAnimate is built on
- [[wan-2.2]] -- Despite branding, WanAnimate is not true 2.2; LoRA compatibility differs
- [[vace]] -- Primary alternative for control + VFX
- [[phantom]] -- Character likeness alternative (often stacked with VACE)
- [[fun-control]] -- Lighter pose control option
- [[humo]], [[infinitetalk]], [[multitalk]] -- Audio-driven lip sync alternatives
- [[lightx2v]] -- Speed LoRA (use 2.1 version)
- [[lora]] -- Training character LoRAs for WanAnimate
- [[comfyui]] -- Wrapper vs native nodes
- [[quantization]] -- GGUF and fp8 formats

## External Resources

- [Wan 2.2 Animate on HuggingFace](https://huggingface.co/Wan-AI/Wan2.2-Animate-14B)
- [ComfyUI-WanAnimatePreprocess (Kijai)](https://github.com/kijai/ComfyUI-WanAnimatePreprocess)
- [Kijai WanVideoWrapper](https://github.com/kijai/ComfyUI-WanVideoWrapper)
- [Wan 2.2 Animate GGUF (patientx)](https://huggingface.co/patientx)
- [Replicate WanAnimate API](https://replicate.com/)
