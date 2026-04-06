---
title: Wan 2.2
aliases: [wan-2.2, wan2.2, wan 2.2, moe, A14B, wan22, wan 2.2 14b, wan 2.2 5b]
sources_ingested: 14
last_updated: 2026-04-06
verification: partial (GPT-5.4, checked against top 3 weeks of raw messages)
---

# Wan 2.2

Wan 2.2 is Alibaba's mid-2025 successor to [[wan-2.1|Wan 2.1]], released late July 2025. Its defining innovation is a dual-model **Mixture-of-Experts (MoE)** architecture: a *High Noise* expert handles early diffusion steps (composition, layout, motion, prompt following) and a *Low Noise* expert handles later steps (detail, texture, resolution). The two models run sequentially on the same latent and together form a single video generation pipeline. Wan 2.2 shipped in two sizes simultaneously -- a **14B + 14B "A14B"** dual-expert flagship and a standalone **5B "TI2V"** model -- alongside a larger 1.3 GB VAE used only by the 5B variant.

The prevailing community view through early 2026: Wan 2.2 is widely praised as the motion and prompt-adherence winner for base T2V/I2V work, while many users still prefer 2.1 for VACE-heavy control workflows, long-form lip-sync, and mature speed-LoRA pipelines. Opinions on face consistency are mixed -- some find 2.1 still better, others report good results with base 2.2. The Wan 2.2 Low Noise model is widely understood to be "essentially a Wan 2.1 finetune" -- which is why most 2.1 LoRAs continue to work on the 2.2 low stage and why 2.1 LightX2V remains a top choice for the low-noise pass even in 2.2 workflows.

> "High noise model is the 'soul' of 2.2 -- all visual quality comes from the high noise part, low noise just does refinement." -- Discord #wan_chatter, July 2025

> "LN is basically 2.1, HN is where the 2.2 magic is at." -- Discord #wan_chatter, January 2026

> "2.2 LN Wan is just 2.1+++, so you can use 2.2 LN LoRAs pretty reliably in Wan 2.1 based models." -- Discord #wan_chatter, January 2026

---

## Overview

Wan 2.2 was teased through June-July 2025 (early-access users leaked the 1280x720x30fps teaser and confirmed it was still trained at 16fps native) and officially released in late July 2025 as a free, open-source model. At release it shipped in two structurally different families:

- **Wan 2.2 A14B** -- a two-model MoE for T2V and I2V, sometimes written as `14B+14B`, where **High Noise** and **Low Noise** are both ~14B parameter DiTs trained on shared data but specialized by timestep range.
- **Wan 2.2 TI2V-5B** -- a single-model 5B with a new VAE (16x spatial downsampling, z_dim=16, ~1.3 GB bf16) that handles both text-to-video and image-to-video in one network, runs at 24fps native, targets 720p+, and is positioned as a consumer-tier option.

The 14B A14B uses the **same Wan 2.1 VAE** for encoding and decoding. Only the 5B uses the new 2.2 VAE. This is a common source of confusion -- loading the wrong VAE produces garbage or errors. CLIP vision is dropped entirely in 2.2 (unlike 2.1 I2V), so no image encoder is used or needed.

Ecosystem position:

- **July 2025** -- Release. Immediate community pivot; Kijai and City96 ship fp8/bf16 and GGUF conversions within days. Early discovery: high/low boundary is at sigma ~0.875 (T2V) or ~0.900 (I2V), and you must use both experts to get the promised quality.
- **August 2025** -- Alibaba PAI releases Fun Control 2.2 and Fun Inpaint 2.2 (August 8); official native VACE 2.2 was not yet available -- users experimented with unofficial merges of Wan 2.1 VACE into Wan 2.2. First community Lightning LoRAs for 2.2 appear and are promptly criticized for style bias and motion degradation compared to the 2.1 LightX2V LoRA.
- **September 2025** -- WanAnimate released (structurally Wan 2.1 I2V despite the 2.2 branding). Fun VACE 2.2 workflows mature. InfiniteTalk / MultiTalk stay on 2.1.
- **October 2025** -- New LightX2V distill LoRAs specific to 2.2 ship (versions 1022 and 1030). Dyno model released. rCM distill from Nvidia as alternative.
- **November 2025** -- LightX2V v1030 declared very close to base motion quality. MAGREF, FFGO, and other ref/character systems ported. Kandinsky 5 2B enters as a rival.
- **December 2025** -- LightX2V 1217 released. New T2V distill LoRAs. rCM merged 2.2 I2V version.
- **January 2026** -- Community consensus stabilizes: 2.2 HN is the clear winner for motion and prompt following; 2.2 LN is a better 2.1; LightX2V 2.1 LoRAs still competitive on low noise; some say Wan 2.2 is the last open-source Wan.
- **February 2026** -- Reports that 2.5/2.6 (closed) may be quality *downgrades* from 2.2 due to speed shortcuts; 2.2 remains the community's "king of local generation."

---

## MoE Architecture

### The two experts

Wan 2.2 14B is not a single model with expert routing inside it. It is **two separate ~14B DiTs** that are loaded and run sequentially on the same latent:

| Stage | Model | Role | Timestep Range |
|-------|-------|------|----------------|
| **High Noise (HN)** | Trained from scratch | Composition, layout, motion, camera, prompt understanding | High sigma / early steps |
| **Low Noise (LN)** | Finetune of Wan 2.1 14B | Detail, texture, refinement, lip-sync cleanup | Low sigma / late steps |

The split is controlled by a **boundary** parameter:
- **T2V:** boundary = **0.875** (roughly the first ~30% of sampling is high noise)
- **I2V:** boundary = **0.900** (more steps are allocated to the high noise expert)

The models are not merged at inference -- naive attempts to average/merge the HN and LN weights generally degrade quality significantly, though some users reported partial success with experimental merges (especially when combined with VACE modules). Instead, one expert runs for its sigma range, hands its partially denoised latent to the second expert, and the second expert finishes. With offloading enabled (not running `--high-vram`), most implementations unload the first model before loading the second, so **only one ~14B model needs to be in VRAM at a time**.

### What each expert contributes

From extensive community testing (Kijai, slmonker, Ada, Benji, and others across July-December 2025):

- **High Noise does everything new.** Motion variety, camera motion, prompt following, complex scene understanding, broader compositions, light/shadow direction, brand recognition, world knowledge, improved hands, improved small faces -- all come from HN. Running the pipeline with *only* the low noise expert produces results "almost identical to Wan 2.1 T2V."
- **Low Noise is essentially a better Wan 2.1.** It refines detail and cleans up the noisy handoff from HN. Used standalone it works fine but looks washed-out and flat, with 2.1-style motion. It is the "refiner" to HN's "base."
- **Disabling HN with a distill LoRA kills 2.2's advantages.** Applying LightX2V or other distill LoRAs to the high noise stage makes outputs "feel like Wan 2.1" -- you lose the improved prompt adherence and motion variety. This is the single biggest gotcha in the 2.2 workflow space.

> "High noise model is the 'soul' of 2.2 -- handles colors, lights, shadows, cinematic graphics. All visual quality comes from high noise part, low noise just does refinement." -- Discord #wan_chatter, July 2025

> "Only high noise model got the improved prompt understanding training. Using only low noise model shows no difference from 2.1 in prompt following." -- Discord #wan_chatter, July 2025

### VAE and text encoder

- **14B models share the Wan 2.1 VAE** (causal 4-frame, 16 ch, 8x spatial, 250 MB bf16). Do not use the 2.2 VAE with 14B -- it will error or produce garbage.
- **5B uses a new, larger VAE** (~1.3 GB bf16, 16x spatial downsampling, 64x total compression, z_dim=16). This VAE is incompatible with 14B.
- Text encoder is **UMT5-XXL**, same as Wan 2.1. Shared text encoder means multilingual (Chinese, Japanese, etc.) prompts still work, and T5-fp16/fp32 choice still matters for complex prompts.
- **CLIP vision was removed entirely.** Wan 2.2 I2V does not use a CLIP image encoder (2.1 I2V did). Leaving a CLIP loader in your workflow is "just bloat on VRAM with no benefit."

---

## Variants

| Model | Size (fp16) | Resolution | Frames | fps | Purpose |
|-------|-------------|------------|--------|-----|---------|
| **Wan2.2-T2V-A14B** | 28 GB HN + 28 GB LN | 480p / 720p / higher | 81 (native) | 16 | Text-to-video flagship |
| **Wan2.2-I2V-A14B** | 28 GB HN + 28 GB LN | 480p / 720p / higher | 81 (native), 109 max | 16 | Image-to-video flagship |
| **Wan2.2-TI2V-5B** | ~10 GB | 720p minimum, prefers 1280x704+ | 121 (native) | 24 | Consumer T2V + I2V in one model |

Notes:
- The 5B is a "T or I" model: same weights do both modes. It has its own VAE.
- The 14B A14B I2V has ~27 GB weights per expert (same as 2.1 T2V), not the 32 GB of 2.1 I2V -- so some 2.1 I2V LoRAs key-mismatch.
- 14B A14B is sometimes called `wan2.2_a14b` in filenames; raw `14b` in the repo refers to the 2.1 14B.
- 14B natively generates 81 frames at 16 fps. Going to 121 frames at 24 fps causes looping unless you use context windows or SVI-Shot approaches.
- 5B natively generates 121 frames at 24 fps and is the only Wan model that is truly 24 fps native.

### Quantization

| Format | 14B Expert Size | Notes |
|--------|-----------------|-------|
| fp32 | ~66 GB | Research only |
| bf16 | ~28 GB | Original Alibaba precision; marginal edge over fp16 for 2.2 |
| fp16 | ~28 GB | Runs fine or faster than fp8_scaled on 3090/3090 Ti (Ampere fp16 path) |
| fp8_e4m3fn | ~16 GB | Default on 4090+; some workflows fail when specific layers are fp8 (e.g. Fun Control `ref_conv`) |
| fp8_e5m2 | ~16 GB | ~2 sec faster per step than e4m3fn; better on 30-series and older than 4090 |
| fp8_fast | ~16 GB | **Works with 2.2** (2.1 quality died with it); usable even on quality-sensitive work |
| GGUF Q8_0 | ~14 GB | Best quality below fp16; cleaner than fp8_scaled, especially with LoRAs |
| GGUF Q6_K | ~11 GB | Good 16 GB VRAM option |
| GGUF Q5_K_M | ~9 GB | "Works really well for 2.2" |
| GGUF Q4_K_M | ~8 GB | Lower VRAM |
| GGUF Q3 | ~6-7 GB | Surprisingly usable with 2.2 |
| NVFP4 | ~7.8 GB (14B I2V high) | Between Q4 and Q6 quality, ~8x faster, no ControlNet/LoRA support yet |

> "GGUF Q8 clearly better quality, no ugly pixels." -- Discord #wan_chatter, July 2025

> "2.2 even works with fp8_fast while 2.1 quality dies with it." -- Discord #wan_chatter, July 2025

5B quantization is problematic: some users reported artifacts with fp8, and fp16 is generally recommended. GGUF quantizations of 5B exist but quality reports are mixed.

---

## Key Settings & Parameters

### A14B T2V baseline (community converged)

| Parameter | Value | Notes |
|-----------|-------|-------|
| **Total Steps** | 20-30 (no distill), 4-8 (with distill LoRA) | Split across HN and LN per boundary |
| **HN steps** | ~30% of total (e.g. 6 of 20) | T2V boundary 0.875 |
| **LN steps** | ~70% of total | |
| **CFG (HN)** | 3.5-6 | Higher CFG on HN gives more motion and prompt adherence |
| **CFG (LN)** | 1.0-3.5 | Lower CFG on LN; too high washes out |
| **Shift** | 5-8 | Match between both samplers; some find shift 1 better than shift 8 |
| **Sampler** | dpmpp_sde (LN), LCM or Euler (HN) | LCM on HN eliminates snow particles |
| **Scheduler** | simple, beta, bong_tangent, linear_quadratic | linear_quadratic with new 2.2 LightX2V MoE |
| **Resolution** | 1280x720 or 1024x576 | A14B trained at 960x960 |
| **Frames** | 81 | Higher causes looping without SVI-Shot / context windows |

### A14B I2V baseline

| Parameter | Value | Notes |
|-----------|-------|-------|
| **Boundary** | **0.900** | Different from T2V's 0.875 |
| **CFG** | Full CFG (3.5-5) on HN, 1.0 on LN with distill | CFG 1 reduces motion and prompt adherence |
| **Shift** | 5-8 | |
| **Steps** | 20-30 (no distill), 6-10 (with distill) | 4-5 minimum on HN; lower = "epic fail" |
| **Resolution** | 1080x1920 works well; 1920x1080 works well | Handles vertical very well |
| **Max frames** | 109 at 16 fps | Loops at 121 unless extending techniques used |

### 5B TI2V baseline

| Parameter | Value | Notes |
|-----------|-------|-------|
| **Resolution** | **1280x720 minimum** | Produces "nightmare results" below 832x480 |
| **Frames** | 121 at 24 fps | Native |
| **Sampler (T2V)** | dpm++_sde | `flowmatch_distill` produces confetti/distortion |
| **Sampler (I2V)** | `flowmatch_pusa` | Only compatible sampler for 5B I2V in wrapper |
| **Precision** | fp16 recommended | Some users reported fp8 artifacts; GGUF options exist but quality is mixed |
| **Negative prompt** | Use the default Chinese negatives | Required for decent output |
| **VAE** | 2.2 VAE (the big one) | Must match |

### CFG behavior (A14B)

- **HN wants CFG.** CFG 3.5-6 on HN increases motion and prompt adherence. CFG 1 on HN is a common mistake that produces static, boring output.
- **LN is mostly tolerant.** With a distill LoRA on LN, CFG 1 is fine. Without distill, CFG 3-4 is typical.
- **Too much CFG on HN can be destructive** in the "HN with distill LoRA" regime -- push CFG gently.
- Per-step CFG schedules (list of values) are supported in Kijai's wrapper for fine control.

### Shift

- **Shift must match between HN and LN samplers.** Mismatches produce snow/particles in the handoff.
- Shift 1 can actually beat shift 8 for some content -- "shift 8 felt like 2.1."
- With LightX2V 1030, tuning shift to match the sigma boundary at 0.900 gives very clean results.

---

## Wan 2.1 vs Wan 2.2 -- Head-to-Head

| Dimension | Wan 2.1 | Wan 2.2 |
|-----------|---------|---------|
| **Architecture** | Single 14B DiT | Dual 14B DiTs (HN + LN) + 5B standalone |
| **Prompt adherence** | Good | Dramatically better (from HN) |
| **Motion** | Limited, sometimes "wanny motion" artifacts | More realistic, better micro-motion, 30fps-like feel downsampled to 16fps |
| **Hands** | Weak | Significantly better even at lower resolution |
| **Physics** | Okay | Much better |
| **Faces** | Many users found 2.1 better for close-ups and face consistency | Good; opinions mixed on whether 2.1 or 2.2 is better |
| **Anime / 2D** | Okay | Better, more inclined to 2D illustration style |
| **Brand / world knowledge** | Limited | Better (larger dataset, more logos, more time knowledge) |
| **Dynamic range / lighting** | Standard | Lightning 2.2 LoRA has reduced dynamic range; base 2.2 HN has better light/shadow |
| **VAE** | 2.1 VAE (250 MB) | 14B uses 2.1 VAE; 5B uses new 1.3 GB VAE |
| **CLIP vision** | I2V uses CLIP ViT-H | Removed |
| **fps native** | 16 | 14B = 16, 5B = 24 |
| **FLF** | Not native | Native FLF support |
| **VRAM** | Single model in VRAM | Two models sequential, about the same peak |
| **Speed** | Faster (single model) | Slower overall due to two passes |
| **LoRA ecosystem** | Massive, mature | Growing, most 2.1 LoRAs work on LN |
| **Inpainting / VACE** | Many users preferred 2.1 VACE for control-heavy work | Fun VACE 2.2 better at fast motion |
| **Face swap / likeness** | Phantom, MAGREF more mature on 2.1 | 2.2 works but 2.1 stack is more mature |
| **Long-form talking** | **InfiniteTalk / MultiTalk = king** | Poor MultiTalk compatibility |

### When to use which

- **Use 2.2** for: new T2V/I2V work, cinematic motion, prompt-heavy scenes, first-last frame morphing, vertical video, better physics, anime.
- **Use 2.1** for: VACE-heavy control workflows, speed-LoRA workflows (FusionX), InfiniteTalk/MultiTalk, WanAnimate (structurally 2.1), HuMo.
- **Use both** by mixing: Some users experimented with hybrid workflows using Wan 2.2 high noise and Wan 2.1-compatible low-noise components/LoRAs, since the low noise model "doesn't do anything new really."

---

## Optimization & Speed LoRAs

The speed-LoRA situation on 2.2 is the most complicated part of the ecosystem. Multiple generations of distill LoRAs exist, and the wrong choice will silently destroy motion quality or force 2.2 to behave like 2.1.

### LightX2V

| Version | Notes |
|---------|-------|
| **LightX2V 2.1 (original)** | Still "undefeated" for low noise as late as Feb 2026. Better lighting quality than any 2.2-specific LoRA. Needs strength **3.0 on HN, 1.0 on LN** to compensate for 2.2 architecture. Some say strength 2.5-3.0 on HN is required. |
| **Lightning 2.2 (first 2.2-specific)** | Criticized: style baked in, bright-lighting bias, reduced dynamic range, motion quality degradation, "Lightning 2.2 is not nearly as good as the previous distill LoRA." Strength 0.125 can reduce noise. |
| **Lightning v1.1** | Cartoon-style bias reported. |
| **LightX2V 2.2 1022** | New 2.2-specific rank-64 HN LoRA. "Much better than old MoE version, especially for 2D animation." Note: some 1022 LN LoRAs were accidentally trained on 2.1 weights, causing 170-key mismatches -- ignore the key errors or use the correct base. |
| **LightX2V 2.2 1030** | Current favorite as of late 2025. "Very close to base model motion quality, much better than other lightx2v variants or lightning." Best with shift tuned to sigma boundary 0.900. "LightX2V 1030 model significantly improved performance." |
| **LightX2V 1217** | December update; "decent for low noise model." |
| **LightX2V MoE full model** | The actual merged model (not LoRA) works better than the LoRA extraction. |
| **Phased DMD T2V Seko v2.0** | Newer distillation method replacing self-forcing. |

Common strengths (community consensus):
- HN: 2.5-3.0 (LightX2V 2.1 on 2.2) or 1.0 (LightX2V 1030)
- LN: 1.0 (all versions)
- Speed LoRAs on HN **will dampen 2.2's motion variety**. Many experts recommend running HN *without* a distill LoRA (just a few real steps at full CFG) and applying distill only to LN.

### CausVid, FusionX, Other Distills

- **CausVid** "is better than other distill LoRAs for high noise" per some users, worse per others. Mixed reviews.
- **FusionX** stays on 2.1 and is considered unmatched there; "FusionX + 2.2 + LightX2V" is worse than "FusionX + 2.1."
- **Dyno** is a fully trained HN replacement (not a LoRA) with LightX2V baked in. Achieves ~70% of the motion quality of full base 2.2 at fast-step budgets. Only LN needs a separate distill LoRA.
- **rCM (Nvidia)** -- Distillation alternative. rCM LoRAs trained on 2.1 don't transfer to 2.2. A 2.2-native rCM merged model (rcm-Wan / RCM6.0) was released for I2V in late 2025.
- **TaylorSeer-Lite** provides significant speedup for 2.2 inference.
- **Smoothmix** ships with LightX2V baked in; don't add it again.
- **Palingenesis** appears to be base 2.2 + Lightning merge.

### SageAttention

- **SageAttention** is widely used with Wan 2.2 for speed and memory benefits, though it is not strictly required.
- "Generation speed way faster after installing sage attn 2.2 with torch 2.10.0."
- Some users discussed first-frame flash artifacts, but this evidence set does not confirm SageAttention as the definitive fix.
- Prebuilt Windows wheels at `woct0rdho/SageAttention` releases.

### Torch compile

- Torch compile reduces VRAM peaks and increases speed on high-end cards.
- Some VAE VRAM bugs exist in **PyTorch 2.9.0+** (conv3d doubles VRAM use in half precision) -- use a nightly that fixes it or force fp32 conv3d.

### Three-sampler setup

An experimental community technique, reported by several users: use three ksamplers --
1. First: a few steps HN without any distill LoRA, at full CFG (3.5+).
2. Second: HN with distill LoRA at CFG 1 for remaining HN steps.
3. Third: LN with distill LoRA at CFG 1.

The idea is to preserve native 2.2 motion and brightness during early HN steps while still benefiting from distill speed. Some users reported this approach gave results closer to full-step quality.

---

## Quirks & Gotchas

### Things the community got wrong repeatedly

- **Using the wrong VAE.** 14B must use the 2.1 VAE; 5B must use the 2.2 VAE. Switched = garbage or errors.
- **Loading CLIP vision.** 2.2 doesn't use it. Leaving it in your workflow wastes VRAM.
- **Applying distill LoRA to HN.** Kills 2.2's defining feature (motion and prompt adherence) and makes outputs look like 2.1.
- **Using only LN.** "Not much different from Wan 2.1" -- you paid for two models, use both.
- **Merging HN and LN weights.** Naive averaging generally degrades quality significantly; some users reported partial success with experimental merges (especially combined with VACE modules), but straightforward weight averaging is not recommended.
- **Too few HN steps.** Below 4-5 is an "epic fail," especially with speed LoRAs.
- **CFG 1 on HN.** Reduces motion and prompt adherence. 2.2 HN wants proper CFG.
- **Mismatched shift between HN and LN samplers.** Produces snow/particles at the handoff.
- **Setting frame count above 81 on 14B.** Loops or ping-pongs around frame 109 unless you use SVI-Shot / context windows.
- **Using 5B at low resolution.** Requires 1280x720+ or "nightmare results."
- **fp8 on 5B.** Some users reported artifacts; fp16 is generally recommended.
- **Connecting context options to the second (LN) sampler.** Can break with negative dimensions; put context on HN, less overlap on LN (16 vs 48).
- **Stride > 10** crashes high noise context windows.

### Inpainting / VACE / control

- **VACE 2.1 module on 2.2:** Community reports suggest VACE 2.1 works most reliably on the 2.2 low-noise stage; high-noise support is weaker and inconsistent, and may require special settings or workarounds (e.g., injecting reference video as latents and starting denoising at step 2) rather than working out of the box. This topic was unsettled through mid-2025, with contradictory user reports.
- **Fun Control 2.2 and Fun Inpaint 2.2** were released August 8, 2025 by Alibaba PAI. Official native VACE 2.2 came later (users were using unofficial merges of Wan 2.1 VACE into Wan 2.2 through at least mid-August). Fun VACE 2.2 strengths: better at fast motion, better reference adherence, reduced color shifting. Weaknesses: many users found 2.1 VACE better for face consistency, multi-frame interpolation, wide shots.
- **WanAnimate** despite the 2.2 branding is structurally Wan 2.1 I2V. LoRAs trained on 2.2 are **not** compatible with WanAnimate; use 2.1 or 2.2 LN LoRAs instead.
- **Mask behavior in Wan 2.2 workflows** can be confusing and may differ between WanVideo Encode, VACE, and wrapper/native workflows; users reported mask slots sometimes behaving more like control/attention guidance than strict inpainting masks.
- **Control signals (Uni3C, Fun Control)** may need higher strength on HN than on LN; experiment to find working values for your workflow.

### Looping and frame count

- 14B naturally loops around frame 109. 81 is the safe native length.
- Skyreels LoRA can break the looping and push to 121+.
- 5B runs at 24fps natively and generates 121 frames without looping.
- First 5-16 frames can be corrupted on longer generations.

### Snow / confetti artifacts

- Caused by: mismatched shift, wrong HN-to-LN handoff, HN model forced into low-sigma territory, mixing incompatible samplers between stages.
- Fixes: match shift, use LCM on HN + dpmpp_sde on LN, check connection order (HN feeds into LN, not reversed).
- If HN and LN are **connected in the wrong order** ("High noise -> second sampler, Low noise -> first sampler" is wrong; HN goes first), you get mosaic/confetti artifacts.

---

## LoRA Compatibility

| From | To | Works? | Notes |
|------|-----|--------|-------|
| **Wan 2.1 T2V/I2V** | **Wan 2.2 LN** | **Yes, reliably** | LN is effectively a 2.1 finetune |
| Wan 2.1 | Wan 2.2 HN | Partial; often weak | HN is a new model; character LoRAs may not trigger |
| Wan 2.1 LightX2V I2V | Wan 2.2 LN | **Yes, still best for low noise** | Lighting quality unmatched |
| Wan 2.1 LightX2V I2V | Wan 2.2 HN | Works at **strength 2.5-3.0** | Compensates for architecture change |
| Wan 2.2 HN LoRA | Wan 2.1 | Usually no | HN is a different trunk |
| Wan 2.2 LN LoRA | Wan 2.1 | **Yes, reliably** ("2.1+++") | |
| Wan 2.2 LN LoRA | WanAnimate | **Yes** | WanAnimate is 2.1-based |
| Wan 2.2 LoRA | 5B | No | Different model |
| 5B LoRA | 14B | No | Size mismatch |
| Character LoRAs (2.1) | 2.2 | Best when applied to **LN only** at strength 1.0 | |
| rCM (Wan 2.1 trained) | Wan 2.2 | **Does not work** | Needs 2.2-native rCM |
| SVI-Shot (2.1) | Wan 2.2 | **Does not work** | Use SVI 2.2 Pro |
| FusionX LoRAs | Wan 2.2 | Worse than on 2.1 | FusionX belongs on 2.1 |
| Stand-In LoRA | Wan 2.2 | **Works directly** | No code changes required |
| PUSA 2.2 LoRA | Wan 2.1 | Sometimes better than PUSA 2.1 | For facial consistency |

### Training

- **2.2 LoRA training** works on both HN and LN, but most community LoRAs train **LN only** because it's where character identity lives, and training HN is expensive with mixed payoff.
- **Adaptive rank LoRA performs significantly better on 2.2** than fixed rank.
- **Rank 256** LightX2V extractions are needed to preserve the speed behavior across the architecture.
- Can train Wan 2.2 LoRAs with images only.
- **5B** destroys faces in LoRA training; avoid for character work.
- Hunyuan Video remains better than Wan for deepfake/celebrity likeness.

---

## Prompting

- **More prompt-responsive than 2.1.** "RL simplifies prompts" -- even short prompts like "a girl dancing" work well vs. strange results on 2.1.
- **HN is the prompt-following half.** Put prompt effort into what HN sees; LN mostly refines.
- **Multi-scene prompting** works natively without EchoShot: separate scenes with `|` pipes, e.g. `video of a red panda walking in the forest|video of a red panda jumping into a pond`. Works in context-window workflows with stride/overlap tuning.
- **EchoShot-style numbered brackets** `[1] [2] [3]` also work on 2.2 HN without trained weights, by splitting cross-attention.
- **Sequential VEO3-style** prompting can work but doesn't follow instructions closely.
- **Time-based prompting** is understood.
- **Text prompts significantly affect 2.2 output quality** -- the model is more prompt-sensitive than 2.1, both positively and negatively.
- **Default negative prompt is Chinese** (same string as 2.1). 5B specifically needs it.

---

## Hardware & VRAM

### VRAM guidance

| VRAM | Recommended 14B A14B config | 5B config |
|------|-----------------------------|-----------|
| 8 GB | Q4 GGUF + heavy block swap; single expert at a time | Fits at fp16 with offload |
| 12 GB | Q5/Q6 GGUF + block swap | Comfortable |
| 16 GB | fp8 with moderate block swap, or Q8 GGUF | Easy |
| 24 GB | fp8 comfortable, Q8 GGUF no block swap | -- |
| 32 GB | bf16/fp16 with minor swap, Q8 + LoRAs | -- |
| 48 GB+ | fp16 no compromise | -- |

- **Wan 2.2 FP16 can run on 16 GB VRAM** despite the 53 GB total model size because HN and LN are loaded sequentially, not simultaneously.
- **fp16 runs as fast or faster than fp8_scaled on 3090/3090 Ti** due to Ampere's fp16 path.
- **Block swap** handles 2.2 well; fp8 blocks swap better than GGUF for higher resolutions.
- **Wan 2.2 I2V is slightly more VRAM-efficient than 2.1 I2V** because image cross-attention was removed.

### Approximate speed (with SageAttention + distill LoRA)

| GPU | Model | Resolution | Frames | Steps | Time |
|-----|-------|------------|--------|-------|------|
| 5090 | A14B fp16 | 720p | 81 | 4+4 distill | ~160 sec |
| 5090 | A14B fp16 | 720x720 | 241 | 3+3 distill | ~one generation |
| 5090 | A14B | 1280x720 | 240 frames | LightX2V | 110 sec |
| 4090 | A14B fp8 | 720p | 81 | ~8 steps distill | several minutes |
| 3090 | 2.2 VACE 720p | dual model with controlnet | 81 | -- | ~16 minutes |
| Mac M4 128GB | 5B | -- | -- | -- | VAE OOMs on fp32 (5B VAE is 4x heavier than 2.1) |

- **Linux may use less VRAM than Windows** with torch compile (torch.compile on Windows was reported as inconsistent in some torch versions).
- **5090** handles fp8 with no block swap.
- "WAN 2.2 can generate 240 frames in 110 seconds" on top hardware with distill LoRAs.

---

## Derivatives & Ecosystem Built on Wan 2.2

| Model | Base | Purpose |
|-------|------|---------|
| **[[vace|Fun VACE 2.2]]** | 2.2 HN + LN modules | Unified control, better fast motion than 2.1 VACE |
| **Fun Control 2.2 / Camera / Trajectory** | 2.2 | Pose, camera, trajectory control |
| **Fun Inpaint 2.2** | 2.2 | Inpainting (some mask workflow quirks) |
| **Dyno** | 2.2 HN replacement | Fully trained HN alternative with LightX2V baked in |
| **Smoothmix / Smoothwan** | 2.2 merge | LightX2V built-in, merged 2.2 |
| **Palingenesis** | 2.2 | Base 2.2 + Lightning merge, style-specific |
| **Wan 2.2 S2V** | 2.2-ish | Speech/audio-to-video, closer to 2.1 than to HN |
| **Wan 2.2 Animate** | **Actually Wan 2.1 I2V** | Pose-driven animation, despite 2.2 branding |
| **MOVA** | Wan 2.2 A14B + audio branch | Audio+video, Apache licensed, basically Ovi scaled to 2.2 |
| **TurboWan 2.2** | 2.2 + activation quant + sparse attention + RCM | Claims 100x speedup |
| **HummingbirdXT** | AMD, 2.2 5B distill | Lightweight VAE decoder for 5B |
| **WorldCanvas** | 2.2, 53 input channels | VACE-like features on 2.2 |
| **SVI 2.0 Pro for Wan 2.2** | 2.2 | Long-video extension, needs only 1-frame mask (vs 5 on 2.1) |
| **HoloCine sparse model** | 2.2 | ~1 min video in 81-frame VRAM budget |
| **rcm-Wan / RCM6.0** | 2.2 I2V | Native 2.2 rCM merged model |

Models that **do not** build on 2.2 despite common assumptions:
- **WanAnimate** -- structurally 2.1 I2V.
- **InfiniteTalk, MultiTalk** -- 2.1 only, poor 2.2 compatibility.
- **HuMo** -- 2.1; can be used as LN in a 2.2 hybrid for lip-sync.
- **Phantom, MAGREF, Bindweave** -- 2.1 based; some work as LN refiners in 2.2 workflows.
- **SkyReels V3, FusionX** -- 2.1.

---

## Timeline

| Date | Event |
|------|-------|
| **Jun 2025** | Early-access users leak teaser specs (1280x720x30fps, still 16fps native) |
| **Jul 2025** | Wan 2.2 released. Three variants: A14B T2V, A14B I2V, TI2V-5B. MoE boundary discovered at sigma 0.875/0.900. Kijai fp8/bf16 conversions; City96 GGUF. Immediate community consensus: HN is the "soul," LN is "2.1 finetune." VACE 2.1 confirmed working on 2.2 LN only |
| **Aug 2025** | First Wan 2.2 Lightning LoRAs released and promptly criticized (style bias, bright-lighting bias, motion degradation). Fun Control 2.2 and Fun Inpaint 2.2 released by Alibaba PAI (Aug 8); users experiment with unofficial VACE 2.1-into-2.2 merges. fp8_fast confirmed usable with 2.2 (2.1 couldn't). Lightning 1.1 variants emerge |
| **Sep 2025** | Fun VACE 2.2 workflows mature. WanAnimate released (actually 2.1). MAGREF ported. Boundary parameter confirmed at 0.900 for I2V. LightVAE tested and found inferior to 2.1 VAE |
| **Oct 2025** | LightX2V 1022 and 1030 released; 1030 declared "very close to base motion quality." Dyno model. rCM I2V merged model. LongCat. 2.1 LightX2V on LN re-confirmed as best for lighting |
| **Nov 2025** | 2.2 LightX2V v1030 dominates; FFGO; Krea Realtime 2.2 extraction. Kandinsky 5 2B enters as quality rival. SVI 2.0 Pro released for 2.2 |
| **Dec 2025** | LightX2V 1217. New T2V distill LoRAs. rCM 6.0 merged for I2V. TurboWan 2.2 claims 100x speedup. Community consensus: Wan 2.2 may be the last open-source Wan |
| **Jan 2026** | "LN is basically 2.1, HN is where the 2.2 magic is at" declared. 2.2 LN LoRAs confirmed to work reliably in 2.1-based models ("2.1+++") |
| **Feb 2026** | Wan 2.5/2.6 rumored to be quality downgrades from 2.2 due to speed shortcuts. 2.2 remains "king of local generation" |

---

## See Also

- [[wan-2.1]] -- Predecessor; LN is a finetune of 2.1; many users still preferred 2.1 for VACE control workflows and long-form lip-sync
- [[vace]] -- Many users preferred VACE 2.1 for control-heavy inpainting; Fun VACE 2.2 for fast motion
- [[wananimate]] -- Branded as 2.2 but structurally 2.1 I2V
- [[humo]] -- 2.1-based; works as LN in 2.2 hybrid
- [[phantom]] -- 2.1-based character consistency; can be LN refiner for 2.2
- [[speed]] -- LightX2V, Lightning, Dyno, rCM distillation comparisons
- [[quantization]] -- fp8 vs GGUF vs bf16 tradeoffs for 2.2
- [[comfyui]] -- Wrapper and native node quirks for 2.2
- [[lora-training]] -- Training on HN, LN, or both
- [[svi]] -- Long-video extension; separate 2.1 and 2.2 versions
- [[infinitetalk]] -- 2.1 only; does not work on 2.2

## External Resources

- [Wan 2.2 GitHub Repository](https://github.com/Wan-Video/Wan2.2)
- [Wan 2.2 HuggingFace Collection](https://huggingface.co/Wan-AI)
- [Wan2.2-T2V-A14B](https://huggingface.co/Wan-AI/Wan2.2-T2V-A14B)
- [Wan2.2-I2V-A14B](https://huggingface.co/Wan-AI/Wan2.2-I2V-A14B)
- [Wan2.2-TI2V-5B](https://huggingface.co/Wan-AI/Wan2.2-TI2V-5B)
- [Kijai fp8/bf16 conversions](https://huggingface.co/Kijai/WanVideo_comfy)
- [Kijai LightX2V LoRAs](https://huggingface.co/Kijai/WanVideo_comfy/tree/main/LoRAs/Wan22_Lightx2v)
- [City96 GGUF quantizations](https://huggingface.co/city96)
- [lightx2v Wan2.2 Distill LoRAs](https://huggingface.co/lightx2v)
- [Fun VACE 2.2 (Alibaba PAI)](https://huggingface.co/alibaba-pai)
- [ComfyUI-WanVideoWrapper (Kijai)](https://github.com/kijai/ComfyUI-WanVideoWrapper)
- [SageAttention releases](https://github.com/woct0rdho/SageAttention/releases)
