---
title: Wan 2.1
aliases: [wan-2.1, wan2.1, wan 2.1, wan2_1, wanx, wanx-2.1]
last_updated: 2025-03-01
---

# Wan 2.1

Wan 2.1 (marketed as "WanX 2.1") is Alibaba's open-source video diffusion model family, released on February 26, 2025. It represents a significant quality leap in open-source video generation, with the 14B variant showing quality competitive with closed-source systems like Kling and Hunyuan Video.

> "I'm still surprised that this is 'just' a 14b model" — TK_999, Discord #wan_chatter, February 23, 2025

> "Wan 2.1 is miles better than Hunyuan Video despite only 1B parameter difference. Massive quality differences between the models." — Discord #wan_chatter, February 2025

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
|--------|----------|---------||
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
- **For 1.3B model:** Block swap is generally not needed -- the model is small enough to fit in VRAM on 12GB+ cards.

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
- **257 frames tested successfully** with 1.3B model using context windows (5 minutes, ~4.8 GB VRAM) — Kijai, March 1, 2025

### Frame extension / autoregressive

Take the last N frames of one generation, feed as first frames of the next. Simple but prone to color drift and character degradation after 3-5 iterations. See [[vace|VACE]] extension techniques for the standard approach.

---

## VAE Compatibility

**Critical:** The Wan 2.1 VAE from Kijai's repository is required for the wrapper workflow. The VAE from Comfy-Org's repackaged models is custom for native ComfyUI and will not work with the wrapper.

- **Wrapper:** Use `Wan2_1_VAE_bf16.safetensors` from https://huggingface.co/Kijai/WanVideo_comfy/blob/main/Wan2_1_VAE_bf16.safetensors
- **Native:** Use the VAE from https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged

Mixing these will cause errors or degraded output quality.

---

## Troubleshooting

### Setup Errors

| Problem | Solution |
|---------|----------|
| `AttributeError: 'RMSNorm' object has no attribute 'comfy_cast_weights'` | Update ComfyUI to latest version. This error appeared after certain ComfyUI updates in early March 2025 |
| Wrong VAE loaded | Wrapper requires Kijai's VAE; native requires Comfy-Org VAE. They are not interchangeable |
| Text encoder not found | Wrapper requires Kijai's text encoder; native uses Comfy-Org's. Download from correct repository |
| Torch compile error | Update PyTorch to 2.7+ nightly. Some users needed to uninstall torchaudio |
| fp16 accumulate not working | Requires PyTorch 2.7.0+. Use `--fast 2` flag or set compute_dtype to fp16 |

### Generation Issues

| Problem | Solution |
|---------|----------|
| Weird artifacts/low quality | Check that block swap is appropriate for your VRAM. 1.3B shouldn't need block swap on 12GB+ cards |
| Frame count changes output | Frame counts above 81 degrade quality. Stick to 81 for best results |
| Resolution changes unexpectedly | The encoder node adjusts resolution based on aspect ratio and total pixels. This is intentional behavior |
| Slow generation with fp16 accumulate | May be related to offloading issues. Try `--fast 2` flag instead of compute_dtype node |
| VAE decode error with fp16 accumulate | Known issue. Workaround: add VRAM unload node between sampler and VAE decode, or use `--fast 2` instead of compute_dtype setting |

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
| 3090 | T2V-14B fp16 | 832x480 | 81 | 30 | ~2 hr |
| 3090 | T2V-14B Q4 GGUF | 832x480 | 81 | 30 | ~45 min |
| 5090 | T2V-14B fp16 | 832x480 | 81 | 20 | ~6 min |
| 5090 | T2V-14B fp8 | 1280x720 | 81 | 20 | ~10 min |
| RTX 8000 | T2V-14B | 832x480 | 81 | 30 | ~2.5-3 hr |
| 4070 Ti | T2V-14B | 832x480 | 81 | 20 | ~25 min (bandwidth-limited) |
| 3080 Ti (12GB) | T2V-1.3B | 832x480 | 81 | 30 | ~2.5 min (with block swap 40, fp8) |

VRAM guidance:

| VRAM | Recommended config |
|------|-------------------|
| 8 GB | 1.3B T2V fp16, or 14B Q4 GGUF + heavy block swap |
| 12 GB | 1.3B full quality (no block swap needed), 14B Q4-Q6 GGUF with block swap |
| 16 GB | 14B fp8 with moderate block swap, or Q8 GGUF |
| 24 GB | 14B fp8 comfortable, Q8 GGUF no block swap |
| 32 GB | 14B bf16/fp16 with minor swap, Q8 + LoRAs |
| 48 GB+ | 14B fp16 no compromise |

Power consumption is lower than image generation: a 5080 uses ~200W for Wan video vs ~350W for Flux image generation. A 5090 uses ~226W at 720p.

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
- [Wan 2.1 HuggingFace Collection](https://huggingface.co/Wan-AI)
- [Wan 2.1 T2V-1.3B](https://huggingface.co/Wan-AI/Wan2.1-T2V-1.3B)
- [Wan 2.1 T2V-14B](https://huggingface.co/Wan-AI/Wan2.1-T2V-14B)
- [Wan 2.1 I2V-14B-480P](https://huggingface.co/Wan-AI/Wan2.1-I2V-14B-480P)
- [Wan 2.1 I2V-14B-720P](https://huggingface.co/Wan-AI/Wan2.1-I2V-14B-720P)
- [Kijai fp8/bf16 conversions](https://huggingface.co/Kijai/WanVideo_comfy)
- [City96 GGUF quantizations](https://huggingface.co/city96)
- [ComfyUI-WanVideoWrapper (Kijai)](https://github.com/kijai/ComfyUI-WanVideoWrapper)
- [diffusion-pipe LoRA training](https://github.com/tdrussell/diffusion-pipe)
