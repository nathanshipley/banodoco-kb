---
title: Wan 2.1
aliases: [wan-2.1, wan2.1, wan 2.1, wan2_1]
sources_ingested: 17
last_updated: 2026-04-05
---

# Wan 2.1

Wan 2.1 is Alibaba's open-source video diffusion model family, released on February 26, 2025. It was the release that fundamentally changed the open-source video generation landscape: the first open model to deliver quality competitive with closed-source commercial systems, released under permissive licensing, in sizes ranging from 1.3B (runnable on 8 GB consumer GPUs) to 14B (competitive with Kling and Sora). Wan 2.1 is the foundation on which virtually every open-source video workflow of 2025 was built -- including [[vace|VACE]], [[phantom|Phantom]], [[humo|HuMo]], [[wananimate|WanAnimate]], InfiniteTalk, MultiTalk, SkyReels V3, Krea Realtime, and dozens of other derivative models. Even the [[wan-2.2|Wan 2.2]] Low Noise expert is, in effect, a Wan 2.1 finetune.

> "Wan 2.1 is miles better than Hunyuan Video despite only 1B parameter difference. Massive quality differences between the models." -- Discord #wan_chatter, February 2025

> "Old 2.1 LightX2V still undefeated as baseline." -- Discord #wan_chatter, October 2025

> "2.2 LN Wan is just 2.1+++, so you can use 2.2 LN LoRAs pretty reliably in Wan 2.1 based models." -- Discord #wan_chatter, January 2026

---

## Overview

Wan 2.1 was announced by Alibaba Wan Team in late February 2025 and released with a broadcast event on February 25-26, 2025. It shipped simultaneously in multiple variants to cover the full consumer-to-pro VRAM range, with a 1.3B T2V intended as "the SD1.5 of video" and a 14B flagship competing with closed-source systems.

The model family includes Text-to-Video (T2V) in 1.3B and 14B sizes, Image-to-Video (I2V) in 14B at 480p and 720p, and a First-Last-Frame (FLF2V) variant at 720p. All models share the same underlying architecture, VAE, and text encoder stack -- they differ only in DiT width/depth and training data mix.

Its position in the ecosystem:

- **February 2025** -- Released. Immediately considered best open-source video model, ahead of Hunyuan Video and LTX.
- **March-June 2025** -- Rapid community development: quantization (City96 GGUF, Kijai fp8), optimization (SageAttention, TeaCache, fp16 accumulate), speed LoRAs (CausVid, FusionX), VACE release.
- **July 2025** -- Wan 2.2 released with dual high/low noise MoE architecture. The Low Noise expert is effectively a Wan 2.1 finetune, which is why 2.1 LoRAs and techniques continue to work on the 2.2 low stage.
- **August 2025-present** -- Wan 2.1 remains the base of choice for many purpose-built derivatives (HuMo, WanAnimate, InfiniteTalk, Phantom, MAGREF, Bindweave, SteadyDancer, SCAIL, etc.) because its T2V and I2V structures are simpler, more stable, and train faster than 2.2's MoE split.

The community consensus through early 2026 is that Wan 2.1 is not obsolete: for inpainting, face consistency, VACE work, reference adherence, and most distilled/speed workflows, 2.1 is still either competitive with or superior to 2.2.

---

## Model Variants

| Model | Size (fp16) | Resolution | Purpose | HuggingFace ID |
|-------|-------------|------------|---------|----------------|
| **Wan2.1-T2V-1.3B** | ~2.6 GB | 480p primary, 720p capable | Text-to-video, consumer GPUs, "SD1.5 of video" | `Wan-AI/Wan2.1-T2V-1.3B` |
| **Wan2.1-T2V-14B** | ~28 GB (66 GB fp32) | 480p and 720p | Text-to-video, flagship quality | `Wan-AI/Wan2.1-T2V-14B` |
| **Wan2.1-I2V-14B-480P** | ~28 GB | 480p native | Image-to-video at 480p | `Wan-AI/Wan2.1-I2V-14B-480P` |
| **Wan2.1-I2V-14B-720P** | ~28 GB | 720p native | Image-to-video at 720p | `Wan-AI/Wan2.1-I2V-14B-720P` |
| **Wan2.1-FLF2V-14B-720P** | ~28 GB | 720p | First-last-frame interpolation | `Wan-AI/Wan2.1-FLF2V-14B-720P` |
| **Wan2.1 VAE** | 250 MB (bf16) | -- | Video VAE, causal, 4-frame chunks, 16 channels | Shipped with all models |
| **UMT5-XXL encoder** | ~10-11 GB | -- | Text encoder, 100+ language support | Shared with all variants |

Quantization formats available from Kijai and City96:

| Format | 14B Size | Notes |
|--------|----------|-------|
| fp32 | ~66 GB | Research only |
| fp16 | ~28 GB | Recommended for quality on consumer GPUs with fp16 accumulate |
| bf16 | ~28 GB | Preferred for training; fp16 preferred for inference |
| fp8_e4m3fn | ~16.5 GB | Good quality, widely compatible |
| fp8_e5m2 | ~16.5 GB | Alternative fp8 format |
| GGUF Q8_0 | ~14 GB | Best quality below fp16; widely considered superior to fp8 |
| GGUF Q6_K | ~11 GB | Good 16 GB VRAM option |
| GGUF Q4_K_M | ~8 GB | Low VRAM option |

> "Q8 GGUF clearly better quality, no ugly pixels." -- Discord #wan_chatter, March 2025

The 1.3B T2V model requires only ~8.2 GB VRAM in bf16, making it the smallest credible video model of its era. The 14B I2V 720p model is 66 GB in fp32 and 16.5 GB in fp8.

---

## Architecture

Wan 2.1 is a DiT (Diffusion Transformer) trained with flow matching, similar in high-level structure to Hunyuan Video but with a distinct VAE and a multilingual text encoder.

**Transformer depth:**
- **1.3B T2V** -- 30 transformer blocks
- **14B (T2V, I2V)** -- 40 transformer blocks

**Text encoder:**
- **UMT5-XXL** (Google's multilingual T5 variant, ~10-11 GB). Supports 100+ languages with zero-shot cross-lingual transfer. This is what lets Chinese, Japanese, Korean, and even emoji prompts work natively. The fp32 version of UMT5 produces noticeably better quality than bf16 -- the difference is visible on text-heavy or multi-subject prompts.
- I2V models additionally use a **CLIP ViT-H** image encoder (RoBERTa variant) to encode the conditioning image.

**VAE:**
- **Wan VAE** is causal (decodes forward in time), operates in **4-frame chunks** (1 latent frame = 4 video frames), and outputs **16-channel latents** at 8x spatial downsampling. It is only ~250 MB in bf16, tiny compared to most video VAEs, and achieves strong reconstruction quality.
- The Wan 2.1 VAE is shared across the entire Wan 2.1 family AND the Wan 2.2 14B family. (Only the Wan 2.2 5B uses a different VAE.) It remains widely preferred over the Wan 2.2 LightVAE, which the community tested and found to introduce noticeable quality loss.
- Can encode and decode long videos at 16fps or 24fps with minimal quality loss -- a property LongCat, SVI, and other long-video systems exploit by using the 2.1 VAE on top of different DiTs.

**Frame rate:**
- **16 fps is hardcoded** in `wan/configs/shared_config.py` and cannot be changed at inference without retraining. All output is 16 fps regardless of which variant (1.3B, 14B, T2V, I2V) you run. Interpolation to 24/30/60 fps happens in post.

**Dimension constraints:**
- **Width and height must be divisible by 16** (because of 8x VAE downsample * 2x patch size). ComfyUI and Kijai wrapper will error or produce noise at off-grid resolutions.
- **Frame count follows the 4n+1 rule** (5, 9, 13, ..., 77, **81**, 85, ..., 121, ...) because of the causal 4-frame VAE.
- Sequence length formula for 14B: `width/16 * height/16 * (length+3)/4`, result must be divisible by 128.
- **81 frames is the native training length** and the sweet spot for quality. The native nodes historically required minimum 81 frames; anything significantly over 81 will start to loop or degrade without context windowing.

---

## Settings & Parameters

Wan 2.1 has more parameter latitude than most video models, but community-converged values exist for each variant.

### T2V 14B default settings (community consensus)

| Parameter | Value | Notes |
|-----------|-------|-------|
| **Steps** | 20-30 | 20 is the "don't think" default; 30 for critical work |
| **CFG** | 5-7 | 6 is a common default; higher CFG improves prompt adherence but risks burning |
| **Shift** | 5.0 | Official default for everything except I2V 480p |
| **Sampler** | uni_pc / dpmpp_2m | uni_pc is the Wan Team default; dpmpp_2m_sde slightly better for detail |
| **Scheduler** | simple / beta | |
| **Resolution** | 1280x720 or 832x480 | Native training resolutions |
| **Frames** | 81 | Native training length; use 4n+1 otherwise |

### I2V 14B 480p default settings

| Parameter | Value | Notes |
|-----------|-------|-------|
| **Shift** | **3.0** | Lower than 480p T2V; per official repo config |
| **CFG** | 5-6 | |
| **Steps** | 20-30 | |
| **Resolution** | 832x480 or 640x480 | |

### I2V 14B 720p settings

| Parameter | Value | Notes |
|-----------|-------|-------|
| **Shift** | 5.0 | |
| **CFG** | 5-6 | |
| **Steps** | 30 | 720p is the less-stable training resolution, more steps help |
| **Resolution** | 1280x720 | |

### T2V 1.3B settings

| Parameter | Value | Notes |
|-----------|-------|-------|
| **Shift** | 8-9 | "Less steps, more shift" pattern like Hunyuan |
| **Steps** | 20-30 | 20 steps with shift 9 works well |
| **CFG** | 5-7 | |
| **Resolution** | 832x480 is official native; 1.3B handles higher too | |

### Shift tuning rules of thumb

- **Lower shift (2-4):** More detail, more texture, closer to training distribution. Use for 480p output or detail-critical work. Shift 3 is recommended for 480p. Shift 1 with control tile LoRAs increases fine detail but adds noise.
- **Mid shift (5-9):** Most scenes. Shift 5 is the official "everything except I2V 480p" default.
- **High shift (8-15):** Better with context windows, more motion, better coherence on 1.3B. Shift 8-15 pairs well with context options for long video.
- **Very high shift (>15):** Used in VACE extensions (shift 120) and some ref-heavy workflows.
- Official pattern: fewer steps + higher shift = similar quality at lower cost.

### Negative prompts

The official Wan 2.1 negative prompt is a long Chinese string starting with "色调艳丽，过曝，静态..." (gaudy colors, overexposed, static, etc.). Key considerations:

- **CFG 1 makes negative prompts useless** -- they are only active above CFG 1.
- The default Chinese negative contains words like "artwork, style, painting" (画风) that block anime/cartoon outputs. Remove those tokens for stylized work.
- English negative prompts work but are less effective than the native Chinese negative.
- The emoji `💩` reportedly works as a minimalist negative prompt.

---

## 1.3B vs 14B

| Aspect | T2V-1.3B | T2V-14B |
|--------|----------|---------|
| **Parameters** | 1.3 billion | 14 billion |
| **Transformer blocks** | 30 | 40 |
| **VRAM (fp16)** | ~8 GB | ~28 GB; fp8 ~16 GB; Q4 ~8 GB |
| **Best resolution** | 480p, usable to 720p+ | 720p and 480p |
| **Speed on 4090 (832x480x81, 20 steps)** | ~2 min | ~12 min with SageAttention |
| **Quality at 720p** | "~10% of 14B" (community consensus) | Flagship |
| **Quality at 480p** | Surprisingly close to 14B | Sharper but sometimes oversharpened |
| **Stippling artifacts** | Yes, needs second-pass cleanup | No |
| **Prompt adherence** | Good for its size | Excellent |
| **Realism** | More realistic looking | Sharper, sometimes "fake" |
| **Context windows** | Fast enough to make sense | Slower, less used |
| **LoRA ecosystem** | Large, but shrinking post-2.2 | Huge; dominant |
| **LoRA transferability** | Partial load on 14B (won't work well) | T2V 14B LoRAs partially apply to I2V 14B |
| **Training cost** | Very cheap; 50 videos at 244p in hours | ~5% more expensive than 1.3B per step, but needs more time overall |
| **Max frames** | Up to 225 in testing | 81 native, loops after |

**When to use 1.3B:**
- 8-12 GB VRAM setups
- Rapid iteration and prototyping
- Multi-pass workflows (1.3B generate → 14B or 2.2 Low refine)
- V2V and differential diffusion work (works well with 1.3B)
- Character LoRA training (cheap, fast)
- Image generation at 1.3B is surprisingly coherent, better than SD3.5 Medium in some tests

**When to use 14B:**
- Final quality
- 720p output
- Complex scenes, multi-subject
- Long prompts and fine-grained prompt following
- Anything where the ~6x speed penalty is affordable

> "14B markedly better than 1.3B, but 1.3B not as bad as expected." -- Discord #wan_chatter, February 2025

> "Multi-pass 1.3B is much faster than using 14B model." -- Discord #wan_chatter, February 2025

---

## T2V vs I2V

Wan 2.1 ships T2V and I2V as separate checkpoints rather than conditioning a single model. They differ in input channels (T2V is 16-channel, I2V has additional channels for the conditioning image and mask), and are trained on different data mixes.

**Key differences:**

- **T2V** takes text only. Controllable via VACE (which is T2V-only). Works with Phantom, HuMo, all text-conditioned control methods.
- **I2V** takes a start frame and optionally an end frame (FLF2V variant). Uses CLIP ViT-H to encode the input image in addition to UMT5 text.
- **LoRA transfer:** T2V LoRAs partially load into I2V with good results (sometimes requiring strength 1.5-2.0 for undertrained LoRAs). The reverse -- I2V LoRAs on T2V -- generally does not work.
- **I2V 480p vs 720p are different models.** The 480p model is better at generating 480p content than the 720p model is, even at 480p. Don't assume 720p strictly dominates.
- **SageAttention quirk:** I2V with SageAttention `fp8_cuda` kernel produces black outputs due to precision overflow. Use `fp16_cuda` or the `sageattn_qk_int8_pv_fp16_triton` variant.
- **VACE is T2V only.** It requires 16 input channels and cannot work with I2V models.
- **First-frame likeness preservation** is significantly better on I2V (the CLIP encoder helps). If likeness preservation is the goal, I2V often beats T2V+VACE.
- **Minimum frames:** Native ComfyUI I2V historically required at least 81 frames; going below throws `max_seq_len` errors.

---

## Precision & Quantization

Wan 2.1 is unusual in that **fp16 is recommended over bf16** for inference on consumer NVIDIA GPUs. This is the opposite of most modern models.

### fp16 vs bf16

- **fp16 + fp16 accumulate is ~10-20% faster** on 4090/5090 than bf16, because NVIDIA consumer GPUs have faster fp16 matmul throughput than bf16 matmul throughput with fp32 accumulate. "18 s/it with bf16 vs 14 s/it with fp16" is typical for fp8 weights.
- **fp16 is significantly better for anatomy during fast motion.** In galloping horses, action scenes, and any high-motion content, bf16 weights misplace limbs while fp16 gets gait cycles correct.
- **bf16 is still preferred for training and for the VAE.** The original Wan VAE is fp32; bf16 VAE is close but the fp32 VAE gives noticeably better results.
- Use the `fp16_accumulation` node / parameter in ComfyUI. On older PyTorch, requires 2.7.0 nightly. After PyTorch 2.7 stable, it works natively.
- Monkey-patching model.py lines 114-115 to force fp16 is sometimes needed for GGUF models that don't use fp16 accumulation automatically.

> "FP16 weights significantly outperform BF16 for anatomy accuracy during fast motion." -- Discord #wan_chatter, March 2025

### fp8 variants

- **fp8_e4m3fn** -- Standard. Works on 4090/5090/L40, not on 3090 (Ada+ only for fp8 matmul).
- **fp8_e5m2** -- Alternative format. Don't load e4m3fn weights and cast to e5m2 -- it is extra lossy. Use the e5m2 weights directly if you need e5m2, or go bf16 → e5m2.
- **fp8_fast** is 4090+ only; does not work on 3090 (use fp16_fast there instead).
- **fp8 matmul on MLP layers** has a crazy quality hit on Wan 2.1 but the largest speed increase. Wan 2.2 handles fp8 MLP better.

### GGUF

- **Q8 GGUF is clearly superior to fp8** in community testing. No pixelation artifacts, cleaner faces, better overall fidelity.
- **GGUF compatibility:** Use standard UMT5 text encoder, no GGUF text encoder required. GGUF models work with native ComfyUI and with Kijai wrapper (some shape/detection issues in wrapper).
- **GGUF speed:** ~20% slower than fp8 when fp8 fits in VRAM. Q8 uses more memory than fp8.
- **GGUF + LoRAs:** Higher VRAM use and slower generation than fp8 + LoRAs. Known issue.
- **"Unexpected architecture type" error** -- update ComfyUI-GGUF nodes (not just base ComfyUI).

> "Q8 GGUF is superior to FP8 quantization." -- Discord #wan_chatter, March 2025

---

## Optimization

### SageAttention

The biggest free speedup on Wan 2.1. Nearly doubles generation speed with minimal quality loss.

- **Speed gain:** ~25% alone, nearly 2x when combined with fp16 accumulate and torch.compile.
- **I2V black image fix:** Use the fp16 kernel, not fp8_cuda. Specifically `sageattn_qk_int8_pv_fp16_triton` on Ada GPUs when the 8+8 kernel produces black output.
- **Auto mode issues:** Select a specific SageAttention mode instead of auto if things break.
- Use the **PatchSageAttention** node rather than the `--use-sage-attention` CLI flag; the node form is more reliable with ComfyUI's model patching.

### fp16 accumulate

- 10-30% speed improvement depending on GPU and model.
- Requires PyTorch 2.7+ (previously 2.7.0 nightly).
- Works with GGUF via the advanced GGUF node that exposes precision controls (though some users report inconsistency).
- Stacks with torch.compile and SageAttention.

### TeaCache

Latent-caching optimization that skips redundant diffusion steps.

- **Speed improvement:** ~2x typical, sometimes more. 1 hour to 18 minutes for 1280x720x81 at 50 steps. 730s → 430s comparing native-no-teacache to wrapper-with-teacache.
- **Quality tradeoff:** Slight degradation, acceptable for most work. Close-ups are where the difference is least visible.
- **VRAM overhead:** +12-13% over baseline.
- **Incompatible with context windowing** -- produces noise artifacts. Do not combine for long video.
- **With VACE:** Use threshold 0.1, not the default 0.015.
- **TeaCache causes VRAM spikes** between samplers if not cleared; turn off between sampler stages or clear VRAM.

### Torch.compile

- **Speed gain:** ~30% on 4090 (2.94 s/it with compile vs 4.00 s/it without, at 640x480x33f).
- Stacks with SageAttention and fp16 accumulate.
- First run takes several minutes to compile; subsequent runs reuse the compiled graph.

### SLG (Skip Layer Guidance)

Guides specific blocks during specific sampling phases for better composition and coherence.

- **Typical settings for 14B:** Block 8, start 0.1, end 0.3-0.5.
- Useful for image arrangement, subject placement, and multi-subject scenes.
- Different blocks work for different models -- VACE has its own recommendations.

### Block swap

Wan 2.1 14B has 40 blocks, 1.3B has 30. Block swap moves blocks between GPU and CPU between inference steps, trading speed for VRAM.

| VRAM | Block swap (14B, 81f, 480p) |
|------|------------------------------|
| 8 GB | 25-40 blocks |
| 12 GB | 20-25 |
| 16 GB | 10-20 |
| 24 GB | 0-10 |
| 32 GB+ | 0 |

- **Native ComfyUI** has automatic offloading; the wrapper requires manual block swap config.
- Start with 0 and increase by 5 each time you OOM.
- 5090 users should lower block swap more aggressively than 4090 users.

### FP16 accumulate + SageAttention + torch.compile stack

The standard performance stack for Wan 2.1. Achievable numbers:

| GPU | Resolution | Frames | Steps | Time (optimized) |
|-----|------------|--------|-------|------------------|
| 4090 | 832x480 | 81 | 20 | ~12 min (T2V 14B) |
| 4090 | 1280x720 | 81 | 20 | ~16 min (Q8 GGUF) |
| 4090 | 832x480 | 81 | 20 | ~2 min (T2V 1.3B) |
| 3090 | 832x480 | 81 | 30 | ~2 hr (14B, no fp8_fast) |
| 5090 | 832x480 | 81 | 20 | ~6 min (T2V 14B, fp16 fast) |

---

## Prompting

### UMT5 multilingual

Wan 2.1 uses UMT5-XXL which supports **100+ languages** via zero-shot cross-lingual transfer. This makes it unusually flexible for prompting.

- **Chinese prompts often produce better results** than English for the same concept, particularly for FLF2V. The official repo recommends Chinese for FLF2V.
- **English works well** for most prompts. The original training included English via translation.
- **Mixed language prompts** work.
- **Emojis work** in prompts -- `🚗💨` and similar are parsed meaningfully.
- Chinese prompt generation produces higher quality results than their English translations for equivalent scenes.

### Prompt structure

- **Long descriptive prompts are rewarded.** Wan 2.1 handles multi-sentence prompts well -- describe subject, action, environment, lighting, camera, style.
- **Separate prompts with `|`** for context-windowed long video -- each prompt is applied to one context window (20 latents = 80 frames per prompt). Prompts should be very similar; big jumps cause visible shifts.
- **Negative prompts** are only active at CFG > 1. Use the official Chinese negative, editing out style words if you want stylized output.
- Token limit is ~512 UMT5 tokens; long prompts are truncated rather than erroring.

### Prompt length

- Short prompts (1-2 sentences): works but under-utilizes the model.
- Medium prompts (3-6 sentences): sweet spot.
- Long prompts (paragraph+): fine; 14B handles them better than 1.3B.

---

## Quirks & Limitations

- **81-frame cap.** The model loops or degrades past 81 frames without context windowing, RifleX, or extension techniques. 81 is baked into the encode_image function and was hardcoded in the original code.
- **16 fps hardcoded.** All generation is 16 fps. Interpolate in post to 24/30/60.
- **Width and height must be divisible by 16.**
- **Minimum 81 frames for native I2V nodes** (older versions). Going under 81 throws max_seq_len errors.
- **Asian default.** Training data skews Asian; unprompted faces trend Asian. Specify ethnicity explicitly.
- **Celebrity censorship.** 14B is more censored than 1.3B for celebrity likeness. 1.3B is more permissive (less training data = less filtering). Hunyuan Video is notably better at celebrity likeness. 1.4B models (Phantom, VACE 1.3B) lack the capacity to capture true celebrity fidelity regardless.
- **Car motion bugs.** Wan consistently has issues with car motion direction -- cars often drive backward or drift sideways even when prompted otherwise.
- **Physics priorities.** Wan prioritizes cinematic composition over strict physical accuracy. Objects can float, gravity can be wrong, but framing is usually excellent.
- **Stippling artifacts on 1.3B.** Small dotted noise pattern, particularly on skin. Requires a low-denoise second pass or an upscaling step to clean up.
- **Looping behavior past 81 frames.** Not an exact loop -- movement varies slightly, but action sequences show clear repetition.
- **RifleX tiling artifacts** -- set to 0 if you see strange tiling. `riflex_freq_index=0` disables it. It doesn't mix with VACE.
- **Memory leaks** when canceling workflows mid-sample. Restart ComfyUI.
- **Native 1.3B text encoder was slow** until ComfyUI added batch text encoding.
- **Differential diffusion** works well with 1.3B (unusual for small video models).

---

## Long Video Techniques

81 frames is only 5 seconds at 16 fps. Every long-video technique for Wan 2.1 exists to push past this.

### Context windowing

Processes the video in overlapping chunks of 81 frames (~20 latents), advancing the window and reusing overlap frames for continuity. Memory stays bounded to one window's worth -- you can generate 1025+ frames on modest VRAM.

- **Works with both T2V and I2V** (I2V reuses the same conditioning image per window).
- **Shift 8-15** pairs well with context options.
- **Multiple prompts** via `|` separator, one per window. Keep prompts very similar.
- **VAE connection** to context window node enables decoding/encoding the last frame of the previous window for I2V conditioning continuity.
- **Incompatible with TeaCache** (noise artifacts).
- **Incompatible with stock VACE 2.1** until Kosinkadink's custom slicing merged into ComfyUI.
- **Known issue:** Missing frames not covered by windows get duplicated to the closest window, causing jittering on interpolation.
- **Visible quality drops** at window resets in long generations.
- Context windows outperform RifleX for long video temporal consistency (tested at 161 frames).

### RifleX

Position-embedding trick that extends the effective context window without retraining.

- **Helps ground stability** in longer videos (less sliding).
- **Prevents looping** in videos longer than 81 frames for some content.
- **Set to 0 (disable) if you see tiling artifacts** -- it doesn't always work cleanly.
- **Does not mix with VACE.**
- Inferior to context windowing for most use cases by late 2025.

### Frame extension / autoregressive

Take the last N frames of one generation, feed as first frames of the next. Simple but prone to color drift and character degradation after 3-5 iterations. See [[vace|VACE]] extension techniques for the standard approach.

### Mobius / latent looping

Shift latents with overlap to create seamless loops. For 49 frames (13 latents), shift of 6 works well. 1 latent = 4 frames.

### SVI, InfiniteTalk, and purpose-built long video

For truly long video (30s+), purpose-built systems based on Wan 2.1 are often better than context windows:

- **[[svi|SVI]] 2.0** on Wan 2.1 I2V 480p uses special LoRAs and code modifications for infinite generation with minimal degradation. The 2.0 for Wan 2.1 uses 5 frames as motion context, the 2.2 version uses 1.
- **InfiniteTalk** -- audio-driven long-form talking video, the reigning king of minimal degradation/colorshift extension.
- **SkyReels V3** -- Wan 2.1-based, designed for extended sequences.
- **FreeLong++** -- 640 frames in one batch on VACE.
- **LongVie2 controlnet** -- works with just Wan 2.1 I2V.

---

## LoRA Compatibility

### Cross-variant compatibility

| From | To | Works? |
|------|-----|--------|
| 1.3B T2V | 1.3B T2V | Yes |
| 14B T2V | 14B T2V | Yes |
| 14B T2V | 14B I2V | **Yes**, often with strength 1.25-1.75 for undertrained LoRAs |
| 14B I2V | 14B T2V | Generally no |
| 1.3B | 14B | Partial load, poor results |
| 14B | 1.3B | Partial load, poor results |
| Wan 2.1 T2V/I2V | Wan 2.2 Low Noise | **Yes, reliably** -- 2.2 LN is effectively a 2.1 finetune |
| Wan 2.1 | Wan 2.2 High Noise | Mixed -- sometimes, often not |
| Wan 2.1 I2V LightX2V | Wan 2.2 Low Noise | Yes, undefeated for low noise |
| rCM (Wan 2.1 trained) | Wan 2.2 | Does not work properly |
| Character LoRAs (2.1) | Wan 2.2 | Works better when connected to low noise only |

> "Wan 2.2 LN Wan is just 2.1+++, so you can use 2.2 LN LoRAs pretty reliably in Wan 2.1 based models." -- Discord #wan_chatter, January 2026

### Training tips

- **1.3B is the budget training platform.** 50 videos at 244p, 60 frames, 0.0001 lr trains fast.
- **14B needs more VRAM but only ~5% more cost per step** than 1.3B.
- **diffusion-pipe** supports Wan LoRA training and drops into ComfyUI directly.
- **Hunyuan Video is better than Wan for celebrity/deepfake likeness training.** Wan trials did not produce good likeness.
- **Rank 256 LoRAs** introduce noticeably more animation than lower ranks -- better movement, more dynamic clothing.
- LightX2V extraction requires very high rank to preserve the speed behavior.

---

## Why Still Use Wan 2.1 (After 2.2 Release)

Wan 2.2 launched in July 2025 with a dual high/low noise MoE architecture. Despite being newer and officially recommended, Wan 2.1 remains in heavy use for several specific reasons:

### 1. The Wan 2.2 Low Noise model IS essentially Wan 2.1

The 2.2 MoE splits at sigma ~0.875. The High Noise expert is a new model trained for motion, composition, and prompt following. The Low Noise expert is, functionally, a Wan 2.1 finetune that handles detail and resolution. This means:

- Wan 2.1 LoRAs work on the 2.2 Low stage.
- The 2.1 LightX2V LoRA is still the best low-noise speed LoRA even for 2.2 workflows.
- Character LoRAs from 2.1 work better when applied only to the low-noise stage of 2.2.

### 2. LightX2V 2.1 LoRAs are still undefeated

The original Wan 2.1 LightX2V LoRA for I2V remains the best speed LoRA for low noise work as of early 2026. New 2.2 Lightning and Lightx2v variants have better prompt adherence in some cases but the 2.1 version still wins for lighting quality, motion coherence, and low-noise stability.

### 3. FusionX

FusionX is a distilled 14B T2V merge (CausVid + LightX2V + other accelerations baked in). As of late 2025, "FusionX quality is still unmatched for Wan 2.1 -- considered the perfect finale to Wan 2.1." FusionX on 2.1 produces better results than FusionX-equivalent stacks on 2.2.

### 4. Face consistency and inpainting

- VACE 2.1 beats Fun VACE 2.2 for inpainting, reference preservation, face consistency, and wide shots.
- Character LoRA workflows are more stable on 2.1.
- Multi-frame interpolation is better on VACE 2.1 than 2.2.

### 5. Long-form lip-sync / talking video

- **InfiniteTalk** is based on Wan 2.1 and remains the king of long-form consistency.
- **MultiTalk** is based on 2.1.
- **HuMo** is trained on Wan 2.1. Workflows that try to use it with Wan 2.2 HN stage "never completely perfect but work well enough."

### 6. Speed and VRAM

- 2.1 is simpler and faster than 2.2's dual-model split.
- No need to load two models and split samplers.
- Less VRAM pressure.

### 7. Stable ecosystem

Every major derivative (Phantom, MAGREF, Bindweave, HuMo, WanAnimate, SteadyDancer, Krea, SkyReels V3, SCAIL, ATI, WanMove, FlashPortrait, EgoX, LongCat, SVI) was built on Wan 2.1. The tooling is mature.

> "Wan 2.1 vs 2.2 for low noise: 2.1 LightX2V LoRA works fine with 2.2 low noise, no need for new 2.2 low noise LoRA." -- Discord #wan_chatter, October 2025

> "Lightning preferred for I2V generally, but 2.1 LightX2V still undefeated for low noise due to better lighting." -- Discord #wan_chatter, October 2025

---

## Models Built on Wan 2.1

Wan 2.1 is the base of an enormous ecosystem. Models that are finetunes, derivatives, or architectural children of Wan 2.1 include:

| Model | Type | Base |
|-------|------|------|
| **[[vace|VACE 2.1]]** | Unified control (depth, pose, inpaint, ref, outpaint) | Wan 2.1 T2V 1.3B and 14B |
| **[[phantom|Phantom]]** | Character consistency from reference | Wan 2.1 T2V |
| **MAGREF** | Multi-reference character/object control | Wan 2.1 I2V |
| **Bindweave** | Subject-consistent video | Wan 2.1 I2V 720p |
| **[[humo|HuMo]]** | Audio-driven video, 17B = 14B + audio layers | Wan 2.1 14B |
| **[[wananimate|WanAnimate]]** | Pose-driven character animation with controlnet | Wan 2.1 |
| **SteadyDancer-14B** | Dance/pose animation with facial expression | Wan 2.1 I2V + VideoLLaMA3-7B |
| **SVI / SVI-Film** | Infinite video via special LoRAs | Wan 2.1 I2V 480p |
| **InfiniteTalk** | Long-form talking head | Wan 2.1 |
| **MultiTalk** | Multi-speaker audio-driven | Wan 2.1 |
| **FantasyTalking / FantasyPortrait** | Portrait animation | Wan 2.1 |
| **Krea Realtime** | Realtime distilled video (like CausVid) | Wan 2.1, distilled via Self-Forcing |
| **SkyReels V3** | Long-form video | Wan 2.1 720p |
| **SkyReels Extend** | Video extension | Wan 2.1 720p |
| **SCAIL** | 3D pose control | Wan 2.1 14B |
| **ATI** | Reference-to-video | Wan 2.1 I2V 1.3B |
| **WanMove** | Motion-focused finetune | Wan 2.1 I2V (identical structure, finetuned) |
| **FlashPortrait** | Portrait acceleration (rebranded LightX2V) | Wan 2.1 |
| **EgoX** | Egocentric video | Wan 2.1 |
| **LongCat** | Long video | Uses Wan 2.1 VAE, different DiT |
| **Rolling Forcing** | Causal video | Wan 2.1 14B |
| **Bindweave** | MLLM-integrated I2V | Wan 2.1 I2V |
| **OmniTransfer** | Transfer learning variant | Wan 2.1 |
| **PainterI2V** | Inpainting specialist | Wan 2.1 I2V |
| **Ovi-style** | Audio+video | Wan 2.1 1.3B |
| **Fun T2V / Fun InP / Fun Control** | Alibaba PAI's control variants | Wan 2.1 |
| **Wan 2.2 Low Noise** | Low noise expert | Effectively Wan 2.1 finetune |

---

## Hardware Benchmarks

Speed numbers assume SageAttention + fp16 accumulate unless noted.

| GPU | Model | Resolution | Frames | Steps | Time |
|-----|-------|------------|--------|-------|------|
| 4090 | T2V-1.3B bf16 | 832x480 | 81 | 20 | ~2 min |
| 4090 | T2V-1.3B fp16 | 512x512 | 53 | 20 | 36 sec |
| 4090 | T2V-14B fp8 | 832x480 | 81 | 20 | ~12 min (SageAttention) |
| 4090 | T2V-14B Q8 GGUF | 1280x720 | 81 | 20 | ~16 min |
| 4090 | T2V-14B | 1280x720 | 81 | 30 | ~1 hr (no optimization) |
| 4090 | I2V-14B 480p fp8 | 832x480 | 81 | 30 | ~10 min |
| 4090 | I2V-14B 720p fp8 | 1280x720 | 81 | 30 | ~1 hr |
| 3090 | T2V-14B fp16 | 832x480 | 81 | 30 | ~2 hr |
| 3090 | T2V-14B Q4 GGUF | 832x480 | 81 | 30 | ~45 min |
| 5090 | T2V-14B fp16 | 832x480 | 81 | 20 | ~6 min |
| 5090 | T2V-14B fp8 | 1280x720 | 81 | 20 | ~10 min |
| RTX 8000 | T2V-14B | 832x480 | 81 | 30 | ~2.5-3 hr |
| 4070 Ti | T2V-14B | 832x480 | 81 | 20 | ~25 min (bandwidth-limited) |

VRAM guidance:

| VRAM | Recommended config |
|------|-------------------|
| 8 GB | 1.3B T2V fp16, or 14B Q4 GGUF + heavy block swap |
| 12 GB | 1.3B full quality, 14B Q4-Q6 GGUF with block swap |
| 16 GB | 14B fp8 with moderate block swap, or Q8 GGUF |
| 24 GB | 14B fp8 comfortable, Q8 GGUF no block swap |
| 32 GB | 14B bf16/fp16 with minor swap, Q8 + LoRAs |
| 48 GB+ | 14B fp16 no compromise |

Power consumption is lower than image generation: a 5080 uses ~200W for Wan video vs ~350W for Flux image generation. A 5090 uses ~226W at 720p.

---

## Timeline

| Date | Event |
|------|-------|
| **Feb 25, 2025** | Wan 2.1 open source broadcast. Code and weights released. T2V-1.3B, T2V-14B, I2V-14B-480P, I2V-14B-720P all released simultaneously |
| **Feb 26, 2025** | 14B I2V 720p fp8 and 14B T2V fp8 available via Kijai. City96 begins GGUF work |
| **Mar 2025** | SageAttention support, diffusion-pipe LoRA training, TeaCache first attempts, first LoRAs. Wan 2.1 declared "miles better than Hunyuan Video" |
| **Apr 2025** | VACE 1.3B preview released, Kijai wrapper support, fp16 accumulate optimization, Q8 GGUF declared superior to fp8 |
| **May 2025** | Official VACE 1.3B and 14B released. CausVid released (extractable as LoRA for 2.1). Native ComfyUI VACE. FLF2V-14B-720P released |
| **Jun 2025** | FusionX distilled merge released. Phantom, MAGREF early versions |
| **Jul 2025** | **Wan 2.2 released** with dual MoE architecture. Low Noise model identified as 2.1 finetune |
| **Aug 2025** | LightX2V becomes dominant speed LoRA. HuMo released (Wan 2.1 + audio layers). Krea Realtime distillation |
| **Sep 2025** | WanAnimate released. Fun VACE 2.2. InfiniteTalk established as long-form king. SkyReels V3 |
| **Oct 2025** | Bindweave, SteadyDancer, Rolling Forcing. LightX2V 1022 and 1030 versions. 2.1 LightX2V LoRA confirmed still best for low noise |
| **Nov 2025** | LongCat (uses 2.1 VAE). SCAIL, WanMove, ATI, SVI 2.0 released for both 2.1 and 2.2 |
| **Dec 2025** | FusionX declared "unmatched for Wan 2.1, perfect finale." LightX2V 1217. rCM alternative distillation |
| **Jan 2026** | Community consensus: 2.1 still preferred for inpainting, face consistency, VACE, speed LoRAs. 2.2 LN officially acknowledged as "2.1+++" |
| **Feb 2026** | Wan 2.1 ecosystem still actively extended (FlashPortrait, OmniTransfer, PainterI2V, EgoX) |

---

## See Also

- [[wan-2.2]] -- Dual MoE successor; Low Noise expert is a 2.1 finetune
- [[vace]] -- Unified control system, VACE 2.1 still preferred for most tasks
- [[phantom]] -- Character consistency, built on Wan 2.1 T2V
- [[humo]] -- Audio-driven video, Wan 2.1 14B + audio layers
- [[wananimate]] -- Pose-driven character animation on Wan 2.1
- [[comfyui]] -- Node-based UI for running Wan 2.1 workflows
- [[speed]] -- LightX2V, CausVid, FusionX, TeaCache, SageAttention
- [[quantization]] -- GGUF, fp8, fp16 accumulate tradeoffs
- [[lora-training]] -- Training LoRAs on 1.3B and 14B
- [[fun-control]] -- Fun team's Wan 2.1-based control variants
- [[infinitetalk]] -- Long-form talking video on Wan 2.1
- [[svi]] -- Infinite video system on Wan 2.1 I2V 480p

## External Resources

- [Wan 2.1 GitHub Repository](https://github.com/Wan-Video/Wan2.1)
- [Wan 2.1 Technical Report / Paper](https://arxiv.org/abs/2503.20314)
- [Wan 2.1 HuggingFace Collection](https://huggingface.co/Wan-AI)
- [Wan 2.1 T2V-1.3B](https://huggingface.co/Wan-AI/Wan2.1-T2V-1.3B)
- [Wan 2.1 T2V-14B](https://huggingface.co/Wan-AI/Wan2.1-T2V-14B)
- [Wan 2.1 I2V-14B-480P](https://huggingface.co/Wan-AI/Wan2.1-I2V-14B-480P)
- [Wan 2.1 I2V-14B-720P](https://huggingface.co/Wan-AI/Wan2.1-I2V-14B-720P)
- [Kijai fp8/bf16 conversions](https://huggingface.co/Kijai/WanVideo_comfy)
- [City96 GGUF quantizations](https://huggingface.co/city96)
- [ComfyUI-WanVideoWrapper (Kijai)](https://github.com/kijai/ComfyUI-WanVideoWrapper)
- [diffusion-pipe LoRA training](https://github.com/tdrussell/diffusion-pipe)
