---
title: Phantom
aliases: [phantom, wan-phantom, phantom-14b, phantom-1.3b]
sources_ingested: 16
last_updated: 2026-04-06
verification: partial (GPT-5.4, checked against top 3 weeks of raw messages)
---

# Phantom

Phantom is a subject consistency / identity preservation model built on top of [[wan-2.1]]. It takes reference images and encodes them as latent frames appended to the generation's noise latent (in the temporal dimension), allowing it to preserve character likeness, clothing, and objects across video frames. Unlike standard I2V models that put image information in extra channels, Phantom keeps the T2V architecture intact, which means it remains compatible with [[vace|VACE]] and T2V-trained [[lora|LoRAs]].

Phantom was developed by the Phantom-video team. The 1.3B model was released first, followed by the 14B model in May 2025. The same team is believed to have also released [[humo|HuMo]] (audio-driven character generation) and OmniInsert (subject insertion for videos), though this is not confirmed in Discord discussions. There was unverified community speculation (late 2025) that the team may have been acquired by ByteDance.

> "Phantom references are on another level, true subject to video capability." -- Ablejones, Discord #wan_chatter, September 2025

---

## What It's For

- **Character consistency** -- Maintain a person's face, hair, clothing, and body across generated video
- **Multi-subject scenes** -- Supports multiple reference images (users reported up to 4), which can cover different subjects (people, objects, scenes)
- **Product replication** -- Excellent at accurately replicating products and objects from reference photos
- **Style adherence** -- Good at style mixing and maintaining artistic styles from references
- **Pseudo-I2V** -- Though technically T2V, produces some of the best I2V-like results by encoding reference latents
- **Inferring unseen views** -- Some users reported Phantom can infer views not present in the reference (e.g., the rear of a car from a front-facing image) -- David Snow, Discord #wan_chatter

---

## Setup & Requirements

### Model Files

Phantom is a fine-tuned Wan T2V model (not a separate module like VACE). It replaces the base T2V checkpoint entirely.

| Model | Size | Notes |
|-------|------|-------|
| Phantom 1.3B | -- | Tested with VACE at 1.3B scale (Kijai demo) |
| Phantom 14B fp16 | ~30 GB | Best quality, too large for on-the-fly quantization on 12 GB cards |
| Phantom 14B fp8_e4m3fn | ~15 GB | Good balance of quality and speed |
| Phantom 14B fp8_e5m2 | ~15 GB | Reported to work on RTX 3060 where e4m3fn did not |
| VACE+Phantom v2 merge (fp16) | ~30 GB | Piblarg's merged model combining both capabilities |
| VACE+Phantom v2 GGUF | varies | orabazes conversion for low-VRAM setups |
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

**System RAM:** 32 GB minimum. 64 GB recommended. Windows users may need to increase their paging file size to avoid OOM crashes with complex Phantom+VACE workflows.

### ComfyUI Setup

Phantom works with both **Kijai WanVideoWrapper** and **native ComfyUI nodes**.

**Key custom nodes:**
- `WanVacePhantomSimpleV2` (Ablejones) -- Simplified node for VACE+Phantom together
- `WanVacePhantomDualV2` (Ablejones) -- Dual control inputs for separate depth/pose/lineart
- `WanVaceAdvanced` (drozbay/Ablejones) -- Advanced VACE nodes with Phantom embed handling
- VACE+Phantom conditioning patcher (Ablejones) -- Properly injects phantom latents into VACE conditioning

**Important:** Phantom is architecturally a T2V model, which causes incompatibilities with some I2V-specific tooling. Kijai confirmed Uni3C does not work with Phantom because "uni3c is only for I2V models and Phantom is technically T2V model." Users also reported that non-GGUF VACE modules cannot be plugged into Phantom GGUF models. Some users did attempt I2V-style workflows with Phantom, but compatibility varies by setup.

---

## Key Settings

### Baseline Settings (No Speed LoRA)

| Parameter | Value | Notes |
|-----------|-------|-------|
| **Frames** | **121** | Phantom trained on 121 frames (confirmed by Ablejones). Some users reported degraded consistency at lower frame counts |
| **FPS** | **24** | Training framerate (confirmed by Ablejones, JohnDopamine) |
| **CFG** | **Varies** | CFG behavior is workflow- and LoRA-dependent. Some users reported good results at CFG 1 with CausVid setups; others preferred CFG 3-5 without speed LoRAs |
| **Steps** | **8-20** | Many users reported workable results at 8-12 steps with CausVid. Without speed LoRAs, more steps may improve quality |
| **Sampler** | **UniPC commonly used** | Scheduler choice significantly affects results. UniPC was frequently used successfully |
| **Shift** | **Low values reported better** | Several users reported lower shift improved likeness, but not universally tested |
| **Resolution** | **832x480** | Trained on 480p (confirmed by chrisd0073). Works at higher resolutions despite not being trained on them |
| **Reference images** | **1-4** | Users reported up to 4 images. Can cover different angles of same subject or different subjects |

### With Speed LoRAs (CausVid/LightX2V)

| Parameter | Value | Notes |
|-----------|-------|-------|
| **Steps** | **8-12** | Multiple users reported decent results at 8-12 steps with CausVid |
| **CFG schedule** | **Varies** | Some users scheduled CFG higher for first steps then dropped to 1.0; others used CFG 1 throughout |
| **CausVid strength** | **Varies widely** | Users reported different preferred strengths; some used 1.0, others lower. Higher strengths may cause flicker |
| **CausVid version** | **Mixed preferences** | CausVid V2 was widely tested, but some users preferred V1.5 for Phantom specifically |

### Phantom CFG (Internal)

Phantom has its own internal CFG mechanism that interacts with the main CFG setting. Users observed that Phantom CFG interactions were sometimes confusing -- some reported no noticeable changes between CFG values of 1, 5, and 9, while others found CFG affected likeness. The interaction between Phantom CFG and main CFG appears workflow-dependent and is not fully settled in community understanding.

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

Users observed that Phantom/VACE workflows may sample extra latent frames beyond what was requested. Kijai confirmed: "phantom reference adds a latent, so the frame count is not matching." This means control inputs may need padding to match. -- Kijai, Discord #wan_chatter

Several users reported that prompting can strongly affect which reference attributes Phantom preserves. Some found that Phantom often ignores reference details not mentioned in the prompt, while others got good results with minimal prompting. The exact mechanism is not fully understood, and results appear inconsistent across setups.

---

## Techniques

### Reference Image Preparation

- **Use diverse images** -- Don't use the same image for both first frame and Phantom reference. Different angles, lighting, and contexts produce much better results
- **White background preferred** -- Especially when removing backgrounds from subjects. Cut objects over white in ComfyUI
- **Real backgrounds also work** -- Phantom prefers simple but real backgrounds; VACE reference prefers white
- **Cover multiple angles** -- Four images of the same subject (face, profile, back of jacket, etc.) provide strong consistency
- **Collages for more subjects** -- Limited to 4 image slots, but each slot can be a collage of multiple characters
- **Multi-image handling varies by implementation** -- Wrapper and native node behavior may differ for batch inputs. Some users reported batch inputs only partially working (e.g., wrapper using only the first image). Test your specific setup

### Prompting for Phantom

Phantom prompting is different from standard T2V, though the community has not reached full consensus on best practices:

- **Simple vs. detailed prompts -- opinions vary** -- Many users prefer simpler prompts for better likeness ("A woman drinking coffee" rather than detailed paragraphs), finding that extensive descriptions take focus away from reference identity. However, some users reported success with more descriptive prompting that includes camera movements and scene details
- **Mention what you want to keep** -- Several users found that prompting can help steer which reference attributes are emphasized, though results are inconsistent
- **For multiple characters** -- Describe each person briefly ("man in black," "woman with red hair") to prevent Phantom from only rendering one
- **Unwanted talking is a common issue** -- Many users reported characters talking/moving their mouths regardless of the prompt. No widely confirmed fix exists in the checked messages, though some users experimented with closed-mouth references and negative prompts

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
- **FantasyTalking incompatible** -- Kijai confirmed: "FantasyTalking = I2V, Phantom = T2V" -- they cannot be directly combined

### Video Extension

- **Context windows** -- Limited evidence on context window behavior with Phantom. One user (tttADs) reported using context windows successfully: "with Phantom, I use the context window. After refining, the seams mostly disappear." Results may vary

---

## Phantom vs Alternatives

| Feature | Phantom | [[magref|MAGREF]] | [[vace|VACE]] ref | [[wananimate|WanAnimate]] | Stand-In | IP-Adapter | LoRA |
|---------|---------|--------|----------|-------------|----------|------------|------|
| **Architecture** | T2V + ref latents | I2V model | T2V + VACE module | ControlNet-like | LoRA (~300 MB) | Adapter | Fine-tuned weights |
| **Likeness** | Very good | Excellent (per some users) | Moderate | Good, not 1:1 | Decent | Moderate | Best (trained) |
| **Multi-ref** | Up to 4 images | Single image | Single image | Varies | Single | Single | N/A |
| **Prompt following** | Moderate | Weaker | Strong | Good | Moderate | Moderate | Strong |
| **Motion quality** | Good (24fps trained) | 15fps trained | Best | Good | Like base | Like base | Like base |
| **Speed** | Slow (3x CFG) | Normal | Normal | Normal | Normal | Normal | Normal |
| **Control compat** | VACE, some LoRAs | Limited | Full VACE | Its own | Full | Full | Full |
| **Flexibility** | Good (outfit/hair changes) | Rigid (exact match) | Moderate | Moderate | Limited | Limited | Fixed |

**Key comparisons:**
- **MAGREF** -- Some users (gokuvonlange) considered MAGREF better than Phantom for likeness; others (mdkb) found Phantom better in recent tests. MAGREF is an I2V model, which limits compatibility. Opinions varied by use case
- **VACE reference** is weaker for likeness but more compatible with controls and prompting. VACE has better motion than Phantom
- **Stand-In** is a LoRA-based approach, making it more compatible with other workflows. Not extensively compared in the checked messages
- **LoRA training** will almost always beat image references for consistency, but requires training time and data

---

## Quirks & Gotchas

- **Seed dependent** -- Some seeds work fantastically while others produce complete failures. Use live preview to detect failures after 5-10 steps and restart with new seed
- **Frame count critical** -- Trained on 121 frames. Some users reported degraded consistency at lower frame counts. Try 121 first
- **Fragile to additions** -- Adding anything (LoRAs, merges, other models) tends to make Phantom work worse. Use lower strengths when combining
- **LoRAs often reduce Phantom quality** -- Several users reported that many LoRAs work worse on pure Phantom than on base T2V, though some merged/FusionX workflows were reported to work well. Some stylized outputs (Simpsons, CGI-toon) were achieved successfully
- **Mixed results with stylized content** -- Some users speculated Phantom may be biased toward realistic imagery, but others reported good anime-style and CGI-toon results
- **Start-of-video glitches** -- Some users reported glitches or flashing at the beginning of generations, especially when combining VACE and Phantom
- **Characters constantly talking** -- Common issue reported by many users. No widely confirmed fix; some experimented with closed-mouth references and negative prompts
- **Multiple characters unreliable** -- Sometimes renders only one of two characters. More clearly describe both in the prompt
- **Reference positioning matters** -- Characters perform better when positioned optimally in reference images. Phantom considers colors, backgrounds, positions, and scale
- **Moviigen LoRA may cause issues** -- One user reported it was "a mistake in I2V Phantom" but this was an early, limited observation
- **Phantom alone + VACE can conflict** -- Coupling with VACE sometimes causes character consistency to break and produces artifacts. The merged model handles this better than separate loading
- **Precision format matters** -- Users reported that precision format choice (fp16, fp8, e4m3fn vs e5m2) significantly affects Phantom results and compatibility

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| CFG behavior inconsistent | CFG behavior is workflow-dependent. Some users reported good results at CFG 1 with CausVid; others preferred higher CFG without speed LoRAs. Experiment with your setup |
| Flashing/noise at start of video | Lower VACE embed strength for video input. Or add LoRA block edit with block 0 off. Lower CausVid to 0.4 |
| Tensor size mismatch with VACE | Phantom adds latent/frame-count complications. Use careful node ordering, put control frames through VACE and reference images through Phantom. May require patcher node |
| Only one character renders | Describe both characters explicitly in prompt. Use 14B (handles 3+ subjects better than 1.3B) |
| Mask showing as frame | Some users saw inpainting masks appear in outputs when combining VACE/Phantom/CausVid. Cause and fix not confirmed |
| ComfyUI crashes (OOM) | Check RAM usage. Consider increasing Windows paging file. Phantom + VACE workflows are very resource intensive |
| Scheduler sensitivity | Scheduler choice significantly affects Phantom results. UniPC was commonly used successfully. Experiment with different schedulers |
| CausVid artifacts | Some users reported noise/artifacts when combining CausVid with certain model formats. Experiment with different precision formats |
| Phantom ignoring references | Prompting may help steer which reference attributes are emphasized, but results are inconsistent. Try mentioning key details in the prompt |
| Slower than expected | Phantom's internal CFG mechanism may add overhead. Speed varies by workflow and settings |
| ControlNet tensor mismatch | Phantom adds latent(s) that can cause size mismatches. Kijai noted control frames may need padding |
| Precision format mismatch | Non-GGUF VACE modules cannot be used with Phantom GGUF models. Match precision formats between models |
| Poor results with same first-frame and ref | Use different images. Diverse references always outperform duplicate ones |
| Start-of-video flickering | Some users reported flicker at the beginning, especially when combining VACE and Phantom. Wrapper/native behavior may differ |
| Excessive mouth movement | Common issue. Some users experimented with closed-mouth references and prompt adjustments, but no reliable fix confirmed |
| VACE/Phantom input confusion | Phantom uses image refs; VACE can handle video/reference frames. Keep control frames in VACE and reference images in Phantom |
| Hair/clothing changes between batches | Frame count sensitivity. Use 121 frames. Add more reference images covering different angles |

---

## LoRA Compatibility

Phantom has a complicated relationship with LoRAs:

- **LoRA compatibility is mixed** -- Some users reported normal T2V LoRAs working with Phantom, while many reported reduced likeness or instability. Piblarg noted "any major change to phantom affects character consistency." Thom293 reported "Loras seem to just be weaker with phantom in general"
- **CausVid** is commonly used with Phantom at 8-12 steps. Strengths and version preferences varied substantially across users -- some preferred V2, while others found V1.5 worked better for Phantom specifically
- **Merging Phantom with base T2V** -- Some users (notably trianglecircle) reported that merging Phantom with T2V improved LoRA compatibility, as pure Phantom produced poor results with many LoRAs
- **Wan 2.2 LN LoRA extraction** was actively explored for Phantom (Ablejones), but Kijai reported not having luck applying it. Not confirmed to work
- **Experimental community merges** -- Users experimented with baking speed LoRAs into Phantom and various merge combinations, but results were unpredictable

---

## Hardware

| GPU | Capability | Notes |
|-----|-----------|-------|
| RTX 3060 (12 GB) | 832x480 with merge | Use e5m2 format (e4m3fn reported incompatible on 3060). Full VACE+Phantom workflows are resource-intensive at this VRAM level |
| RTX 4090 (24 GB) | Full Phantom 14B fp8 | One user initially got OOM on first attempt, succeeded on retry |

**Notes:** Phantom+VACE workflows are generally resource-intensive. Exact timings vary widely by workflow, resolution, frame count, and LoRA usage.

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
| July 2025 | Phantom+VACE workflows refined. MAGREF comparisons begin |

*Note: Later timeline entries (Aug-Dec 2025) were not verified against raw messages and have been removed pending verification.*

---

## See Also

- [[vace]] -- Control system that pairs with Phantom for the most popular advanced workflow
- [[magref]] -- I2V alternative with higher accuracy but less flexibility
- [[wananimate]] -- Alternative approach to motion/character control (not directly compared in verified messages)
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
