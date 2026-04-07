---
title: Wan 2.1
aliases: [wan-2.1, wan2.1, wan 2.1, wan2_1, wanx, wanx-2.1]
last_updated: 2025-03-23
---

# Wan 2.1

Wan 2.1 (marketed as "WanX 2.1") is Alibaba's open-source video diffusion model family, released on February 26, 2025. It represents a significant quality leap in open-source video generation, with the 14B variant showing quality competitive with closed-source systems like Kling and Hunyuan Video.

On March 21, 2025, Alibaba released the official technical report detailing the architecture, training methodology, and optimization techniques used in Wan 2.1.

> "I'm still surprised that this is 'just' a 14b model" — TK_999, Discord #wan_chatter, February 23, 2025

> "Wan 2.1 is miles better than Hunyuan Video despite only 1B parameter difference. Massive quality differences between the models." — Discord #wan_chatter, February 2025

---

## Technical Report (March 2025)

The official Wan 2.1 technical report was released on March 21, 2025, providing comprehensive details about the model architecture, training pipeline, and optimization strategies.

**Key revelations from the technical report:**

### Shared AdaLN Architecture

Wan uses **shared adaptive normalization layers** across transformer blocks, substantially reducing parameters without sacrificing performance. This architectural choice is one reason the 14B model achieves competitive quality despite its relatively modest size.

### umT5 Text Encoder Selection

The report confirms that **umT5 was chosen** after extensive testing of multiple text encoders:
- Strongest multilingual capabilities
- Better composition abilities
- Faster convergence during training

This validates the community's observations about Wan's excellent multilingual support and prompt following.

### Diffusion Cache (Not Yet Implemented)

The report describes a **diffusion cache system** similar to KV caching in LLMs:
- Caches attention outputs across denoising steps
- Reuses conditional/unconditional passes to reduce computation
- Achieves **1.62× speedup** according to the paper

**Important:** This diffusion cache is NOT implemented in the open-source code release as of March 2025. The community-developed [[teacache]] is a separate implementation with similar goals.

> "it's not in the code we have" — Kijai, March 21, 2025

> "so much of this paper is not in the code" — Kijai, March 21, 2025

**Diffusion Cache vs TeaCache differences (March 21, 2025):**

fredbliss analyzed the differences between WanVideo's described diffusion cache and the community's TeaCache implementation:

1. **Two-Tier Architecture vs. Single-Level Caching**
   - **WanVideo**: Uses a two-tier system separating attention caching from CFG caching
   - **TeaCache**: Implements a single caching mechanism that focuses only on model prediction outputs

2. **Targeted Component Caching vs. End-to-End Caching**
   - **WanVideo**: Specifically targets attention computations (the most expensive operation) and conditional/unconditional branches separately
   - **TeaCache**: Caches final outputs of denoising steps without distinguishing between internal components

3. **Phase-Aware Caching Strategies**
   - **WanVideo**: Employs different caching frequencies for different phases of the diffusion process:
     * Early steps (high noise): Minimal caching for higher precision
     * Middle steps: Moderate caching
     * Late steps (low noise): Aggressive caching where similarities are highest
   - **TeaCache**: Uses a uniform caching approach throughout the entire process

4. **Residual Compensation Technique**
   - **WanVideo**: Implements error compensation when using cached outputs, particularly for CFG, which helps preserve fine details
   - **TeaCache**: No error compensation mechanism, which can lead to detail loss with aggressive caching

5. **Sophisticated Interpolation**
   - **WanVideo**: Uses more advanced interpolation between cached points, potentially with temporal-aware weighting
   - **TeaCache**: Primarily relies on direct reuse without sophisticated interpolation

6. **Dynamic Validation**
   - **WanVideo**: Appears to use validation-based thresholds to determine optimal caching points
   - **TeaCache**: Relies on fixed thresholds and heuristics

> "The most significant innovation in WanVideo's approach is breaking down the caching problem into more granular components. By recognizing that attention operations and conditional/unconditional branches have different similarity patterns across timesteps, they can apply much more targeted and aggressive optimizations." — fredbliss, March 21, 2025

### Feature Cache for VAE

The VAE maintains **frame-level feature caches** between processing chunks for efficient long video processing. This explains why the Wan VAE handles long videos so well.

> "the VAE is good" — Kijai, March 21, 2025

### Context Windows

The report discusses context windowing in detail, processing longer videos in overlapping windows with blending — conceptually similar to sliding window attention in LLMs. This validates the community's [[context-windows]] implementations.

**WanVideo Streamer technique (March 21, 2025):**

fredbliss identified key differences between WanVideo's streaming approach and community implementations:

- **Warmup phase**: The first w tokens are used solely for 'warming up' the model and do not contribute to the loss computation. At inference time, the first w tokens are discarded, and the generated video begins from the (w + 1)-th token.
- **Token queue**: Tokens "flow through" the denoising process. Only the leftmost token (fully denoised) is removed and a new noisy token is added at the right. They maintain a consistent window length throughout the process.
- **Sliding mechanism**: After a fixed number of denoising steps, the leftmost token (with the lowest noise level) is dequeued and cached, while a new token with Gaussian noise is appended to the rightmost position.

> "it's like the same exact thing as LLMs context windows but not as smart" — fredbliss, March 21, 2025

### Training Pipeline

The report reveals a multi-stage training approach:
1. Initial low-resolution image pre-training (256px)
2. Joint image-video training at progressive resolutions (256px → 480px → 720px)
3. Post-training with higher quality data

**Data principles:**
- High quality
- High diversity
- Substantial scale (billions of videos and images)

**Data preprocessing includes:**
- Fundamental filtering: text detection, aesthetic evaluation, NSFW filtering, watermark detection
- Visual quality assessment: clustering and expert scoring models
- Motion quality assessment: classification into six tiers from optimal to unusable
- Visual text data: special processing for text generation capabilities

### Acceleration & Optimization

**Training optimizations:**
- Combined Fully Sharded Data Parallel (FSDP) with 2D Context Parallelism
- Activation offloading and gradient checkpointing

**Inference optimizations:**
- FP8 GEMM operations with per-tensor weight quantization
- 8-bit FlashAttention with mixed precision
- Diffusion caching (described but not released)

**FP8 Implementation Details (March 21-22, 2025):**

fredbliss analyzed the FP8 implementation described in the paper:

- Uses mixed 8-bit optimization: INT8 for S = QK^T (attention scores) and FP8 for O = PV (output computation)
- Uses FP32 accumulation for cross-block reduction to prevent overflow with long sequences
- Fuses Float32 accumulation with intra-warpgroup pipelining
- Performs block size tuning to reduce register spilling

**Critical insight:** The paper lacks specific details about which layers use which precision, specific calibration methodology, and whether they use E4M3 or E5M2 format for different components.

> "theyre almost certainly doing mixed bpw and you can quant the kv cache too but it needs to be dynamic and based on activations, not based on calibration data + weight updates" — fredbliss, March 21, 2025

**DeepGEMM for FP8 (March 22, 2025):**

fredbliss shared that DeepSeek's DeepGEMM is being adapted for FP8 operations: https://github.com/deepseek-ai/DeepGEMM/issues/6

### Wan-Bench Evaluation

The report introduces **Wan-Bench**, a comprehensive evaluation metric covering:
- Dynamic quality (motion, artifacts, stability)
- Image quality (fidelity, scene generation)
- Instruction following capabilities

Both 14B and 1.3B models outperformed existing models in most metrics.

**External resources:**
- [Technical Report Announcement](https://x.com/StevenZhang66/status/1903035178890485888) — March 21, 2025

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

> "Q8 GGUF clearly better quality, no ugly pixels." — Discord #wan_chatter, March 2025

The 1.3B T2V model requires only ~8.2 GB VRAM in bf16, making it the smallest credible video model of its era. The 14B I2V 720p model is 66 GB in fp32 and 16.5 GB in fp8.

**FP32 Testing (March 22, 2025):**

Benjimon tested fp32 vs fp16 on the 14B model:
- **FP32:** 100%|██████████| 30/30 [36:26<00:00, 72.89s/it]
- **FP16:** 100%|██████████| 30/30 [33:02<00:00, 66.09s/it]
- **Quality:** "I think the cat has more realistic movement in fp32"
- **VRAM:** 93GB RAM, 16GB VRAM with 38 blocks swapped at 960x768
- **Speed:** 63s/it with fp32 + block swap

> "not much difference" — Benjimon, March 22, 2025

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
- The Wan 2.1 VAE is shared across the entire Wan 2.1 family AND the Wan 2.2 14B family. (Only the Wan 2.2 5B uses a different VAE.)
- Can encode and decode long videos at 16fps or 24fps with minimal quality loss.
- Uses **RMSNorm instead of GroupNorm** to preserve temporal causality (per technical report).
- Implements a **feature cache mechanism** for efficient processing of long videos (per technical report).

**Frame rate:**
- **16 fps is hardcoded** in `wan/configs/shared_config.py` and cannot be changed at inference without retraining. All output is 16 fps regardless of which variant (1.3B, 14B, T2V, I2V) you run. Interpolation to 24/30/60 fps happens in post.

**Dimension constraints:**
- **Width and height must be divisible by 16** (because of 8x VAE downsample * 2x patch size). ComfyUI and Kijai wrapper will error or produce noise at off-grid resolutions.
- **Frame count follows the 4n+1 rule** (5, 9, 13, ..., 77, **81**, 85, ..., 121, ...) because of the causal 4-frame VAE.
- Sequence length formula for 14B: `width/16 * height/16 * (length+3)/4`, result must be divisible by 128.
- **81 frames is the native training length** and the sweet spot for quality. The native nodes historically required minimum 81 frames; anything significantly over 81 will start to loop or degrade without context windowing.

---

## Key Settings & Parameters

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

---

## 1.3B vs 14B

| Aspect | T2V-1.3B | T2V-14B |
|--------|----------|----------|
| **Parameters** | 1.3 billion | 14 billion |
| **Transformer blocks** | 30 | 40 |
| **VRAM (fp16)** | ~8 GB | ~28 GB; fp8 ~16 GB; Q4 ~8 GB |
| **Best resolution** | 480p, usable to 720p+ | 720p and 480p |
| **Speed on 4090 (832x480x81, 20 steps)** | ~2 min | ~12 min with SageAttention |
| **Quality at 720p** | Much weaker than 14B, though still usable for prototyping | Flagship |
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

---

## Precision & Quantization

Wan 2.1 is unusual in that **fp16 is recommended over bf16** for inference on consumer NVIDIA GPUs. This is the opposite of most modern models.

### fp16 vs bf16

- **fp16 + fp16 accumulate is ~10-20% faster** on 4090/5090 than bf16, because NVIDIA consumer GPUs have faster fp16 matmul throughput than bf16 matmul throughput with fp32 accumulate. "18 s/it with bf16 vs 14 s/it with fp16" is typical for fp8 weights.
- **fp16 is significantly better for anatomy during fast motion.** In galloping horses, action scenes, and any high-motion content, bf16 weights misplace limbs while fp16 gets gait cycles correct.
- **bf16 is still preferred for training and for the VAE.** The original Wan VAE is fp32; bf16 VAE is close but the fp32 VAE gives noticeably better results.
- Use the `fp16_accumulation` node / parameter in ComfyUI. Requires PyTorch 2.7.0 or later.
- Monkey-patching model.py lines 114-115 to force fp16 is sometimes needed for GGUF models that don't use fp16 accumulation automatically.

> "FP16 weights significantly outperform BF16 for anatomy accuracy during fast motion." — Discord #wan_chatter, March 2025

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

> "Q8 GGUF is superior to FP8 quantization." — Discord #wan_chatter, March 2025

---

## Optimization

### fp16 accumulate

- **10-30% speed improvement** depending on GPU and model.
- Requires **PyTorch 2.7+** (nightly builds recommended as of March 2025).
- Works with GGUF via the advanced GGUF node that exposes precision controls (though some users report inconsistency).
- Stacks with torch.compile and SageAttention.
- **Installation:** `pip install --pre torch torchvision --index-url https://download.pytorch.org/whl/nightly/cu126` (or cu128)
- **Note:** torchaudio doesn't exist for latest nightly, so can't install it at all. Leave it installed but don't include in pip install command.
- **Enabling:** Set `compute_dtype` to `fp16` in the diffusion model loader, or use `--fast 2` launch flag (enables fp16 accumulate automatically).
- **It's like 20-30% increase that stacks with compile and sageattn** — Kijai, March 1, 2025

### SageAttention

The biggest free speedup on Wan 2.1. Nearly doubles generation speed with minimal quality loss.

- **Speed gain:** ~25% alone, nearly 2x when combined with fp16 accumulate and torch.compile.
- **I2V black image fix:** Use the fp16 kernel, not fp8_cuda. Specifically `sageattn_qk_int8_pv_fp16_triton` on Ada GPUs when the 8+8 kernel produces black output.
- **Auto mode issues:** Select a specific SageAttention mode instead of auto if things break.
- Use the **PatchSageAttention** node rather than the `--use-sage-attention` CLI flag; the node form is more reliable with ComfyUI's model patching.

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

### Block swap

Wan 2.1 14B has 40 blocks, 1.3B has 30. Block swap moves blocks between GPU and CPU between inference steps, trading speed for VRAM.

| VRAM | Block swap (14B, 81f, 480p) |
|------|-----------------------------|  
| 8 GB | 25-40 blocks |
| 12 GB | 20-25 |
| 16 GB | 10-20 |
| 24 GB | 0-10 |
| 32 GB+ | 0 |

- **Native ComfyUI** has automatic offloading; the wrapper requires manual block swap config.
- Start with 0 and increase by 5 each time you OOM.
- 5090 users should lower block swap more aggressively than 4090 users.

### fp16 accumulate + SageAttention + torch.compile stack

The standard performance stack for Wan 2.1. Achievable numbers:

| GPU | Resolution | Frames | Steps | Time (optimized) |
|-----|------------|--------|-------|------------------|
| 4090 | 832x480 | 81 | 20 | ~12 min (T2V 14B) |
| 4090 | 1280x720 | 81 | 20 | ~16 min (Q8 GGUF) |
| 4090 | 832x480 | 81 | 20 | ~2 min (T2V 1.3B) |
| 3090 | 832x480 | 81 | 30 | ~2 hr (14B, no fp8_fast) |
| 5090 | 832x480 | 81 | 20 | ~6 min (T2V 14B, fp16 fast) |

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

**Mobius RoPE Modifications (March 22, 2025):**

Kijai noted that the Mobius paper includes RoPE modifications for longer generations:

> "the Mobius paper and code actually had some RoPE stuff, for longer gens... not sure how well that works for Wan tho" — Kijai, March 22, 2025

### Frame extension / autoregressive

Take the last N frames of one generation, feed as first frames of the next. Simple but prone to color drift and character degradation after 3-5 iterations. See [[vace|VACE]] extension techniques for the standard approach.

### Mobius / latent looping

Shift latents with overlap to create seamless loops. For 49 frames (13 latents), shift of 6 works well. 1 latent = 4 frames.

**Improved loop stitching (March 22, 2025):**

Kijai improved the Mobius loop implementation:

> "I think I improved the loop stitching, didn't notice that the Mobius paper was doing it bit differently, smoother now" — Kijai, March 22, 2025

The updated implementation produces smoother loops with the 1.3B model, though it still doesn't work well with 14B models.

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
| Wan 2.1 T2V/I2V | Wan 2.2 Low Noise | Often works (2.2 LN is effectively a 2.1 finetune), but reliability varies by LoRA; native 2.2 LoRAs usually perform better |
| Wan 2.1 | Wan 2.2 High Noise | Mixed -- sometimes, often not |
| Wan 2.1 I2V LightX2V | Wan 2.2 Low Noise | Commonly used; some users preferred it over 2.2 Lightning for low noise |
| rCM (Wan 2.1 trained) | Wan 2.2 | Does not work properly |
| Character LoRAs (2.1) | Wan 2.2 | Works better when connected to low noise only |

> "Wan 2.2 LN Wan is just 2.1+++, so you can use 2.2 LN LoRAs pretty reliably in Wan 2.1 based models." — Discord #wan_chatter, January 2026

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

- Many Wan 2.1 LoRAs can be used on the 2.2 low-noise stage, often with higher strength, but results are mixed and native 2.2 training generally works better.
- The 2.1 LightX2V LoRA remained commonly used on the low-noise stage of 2.2 workflows.
- Character LoRAs from 2.1 work better when applied only to the low-noise stage of 2.2.

### 2. LightX2V 2.1 LoRAs remained popular

The original Wan 2.1 LightX2V LoRA for I2V remained commonly used for low-noise speed workflows into 2026. Some users preferred it over newer 2.2 Lightning variants for lighting quality, though others argued that distill/speed LoRAs on 2.2 high-noise reduced what made 2.2 special. New 2.2 variants offered better prompt adherence in some cases.

### 3. FusionX

FusionX is a distilled 14B T2V merge (CausVid + LightX2V + other accelerations baked in). It was a popular Wan 2.1 variant known for speed/quality balance, though some users noted that distillation can "invent" details and trade off character/LoRA fidelity for speed. FusionX represented a mature, well-tested workflow for users who prioritized generation speed on Wan 2.1.

### 4. VACE-based control workflows

- Users reported strong results from Wan 2.1 + VACE workflows, particularly for V2V/control; some continued to prefer 2.1-based control setups because 2.2 VACE workflows were experimental or less mature.
- Character LoRA workflows were generally more stable on 2.1.
- Direct comparative evidence across all categories (inpainting, face consistency, wide shots, multi-frame interpolation) was limited; the preference was strongest for V2V control specifically.

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

> "Wan 2.1 vs 2.2 for low noise: 2.1 LightX2V LoRA works fine with 2.2 low noise, no need for new 2.2 low noise LoRA." — Discord #wan_chatter, October 2025

> Some users reported preferring 2.1 LightX2V over Lightning for low-noise work due to lighting quality, though this was not universally agreed. — Discord #wan_chatter, October 2025

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
| **[[wananimate|WanAnimate]]** | Pose-driven character animation derivative | Wan 2.1 |
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
| 4090 | I2V-14B Q8 GGUF | 1280x720 | 81 | -- | ~16 min |
| 4090 | T2V-14B fp32 | 960x768 | -- | 30 | 72.89s/it (with 38 block swap) |
| 3090 | T2V-14B fp16 | 832x480 | 81 | 30 | ~2 hr |
| 3090 | T2V-14B Q4 GGUF | 832x480 | 81 | 30 | ~45 min |
| 5090 | T2V-14B fp16 | 832x480 | 81 | 20 | ~6 min |
| 5090 | T2V-14B fp8 | 1280x720 | 81 | 20 | ~10 min |
| 5090 | I2V-14B | -- | 165 | 35 | 10 min (10 blocks swapped) |
| RTX 8000 | T2V-14B | 832x480 | 81 | 30 | ~2.5-3 hr |
| 4070 Ti | T2V-14B | 832x480 | 81 | 20 | ~25 min (bandwidth-limited) |
| 3080 Ti (12GB) | T2V-1.3B | 832x480 | 81 | 30 | ~2.5 min (with block swap 40, fp8) |

VRAM guidance:

| VRAM | Recommended config |
|------|-----------------|
| 8 GB | 1.3B T2V fp16, or 14B Q4 GGUF + heavy block swap |
| 12 GB | 1.3B full quality (no block swap needed), 14B Q4-Q6 GGUF with block swap |
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
| **Mar 21, 2025** | **Official technical report released** detailing architecture, training pipeline, and optimization strategies |
| **Mar 22, 2025** | Kijai improves Mobius loop stitching based on paper details |

---

## See Also

- [[wan-2.2]] -- Dual MoE successor; Low Noise expert is a 2.1 finetune
- [[vace]] -- Unified control system
- [[phantom]] -- Character consistency model, built on Wan 2.1 T2V
- [[comfyui]] -- Node-based UI for running Wan 2.1 workflows
- [[quantization]] -- GGUF and fp8 formats for Wan 2.1
- [[speed]] -- LightX2V, CausVid, FusionX, TeaCache, SageAttention
- [[lora-training]] -- Training LoRAs on 1.3B and 14B

## External Resources

- [Wan 2.1 GitHub Repository](https://github.com/Wan-Video/Wan2.1)
- [Wan 2.1 Technical Report / Paper](https://arxiv.org/abs/2503.20314)
- [Technical Report Announcement](https://x.com/StevenZhang66/status/1903035178890485888)
- [Wan 2.1 HuggingFace Collection](https://huggingface.co/Wan-AI)
- [Wan 2.1 T2V-1.3B](https://huggingface.co/Wan-AI/Wan2.1-T2V-1.3B)
- [Wan 2.1 T2V-14B](https://huggingface.co/Wan-AI/Wan2.1-T2V-14B)
- [Wan 2.1 I2V-14B-480P](https://huggingface.co/Wan-AI/Wan2.1-I2V-14B-480P)
- [Wan 2.1 I2V-14B-720P](https://huggingface.co/Wan-AI/Wan2.1-I2V-14B-720P)
- [Kijai fp8/bf16 conversions](https://huggingface.co/Kijai/WanVideo_comfy)
- [City96 GGUF quantizations](https://huggingface.co/city96)
- [ComfyUI-WanVideoWrapper (Kijai)](https://github.com/kijai/ComfyUI-WanVideoWrapper)
- [diffusion-pipe LoRA training](https://github.com/tdrussell/diffusion-pipe)
- [DeepGEMM (DeepSeek FP8)](https://github.com/deepseek-ai/DeepGEMM)
