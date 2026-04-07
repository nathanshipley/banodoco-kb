---
title: SkyReels A2
aliases: [skyreels-a2, skyreels-animate-anything, skyreels-a2-wan]
last_updated: 2025-04-06
---

# SkyReels A2 (Animate Anything)

SkyReels A2 is a video generation model from Skywork AI, released on April 3, 2025. It is based on Wan 2.1 14B and focuses on character animation and multi-subject composition. Kijai converted it to work with VACE-style reference conditioning on April 5, 2025.

**Release:** April 3, 2025 (original), April 5, 2025 (Kijai conversion)

**Model:** `Skywork/SkyReels-A2` (original), `Kijai/WanVideo_comfy/blob/main/Wan2_1_SkyreelsA2_fp8_e4m3fn.safetensors` (converted)

**Code:** https://github.com/SkyworkAI/SkyReels-A2

---

## Overview

SkyReels A2 is built on top of Wan 2.1 14B architecture and appears to be trained for character animation and multi-subject composition tasks.

> "https://huggingface.co/Skywork/SkyReels-A2" — Juampab12, April 3, 2025

**Architecture identification:**

> "it's Wan based. it's Wan 14B. same structure, same number of blocks, same clipvision and T5 etc." — Kijai, April 3, 2025

> "these are just diffusers weights" — Kijai, April 3, 2025

**LoRA compatibility:**

Since it's based on Wan 2.1 14B with the same structure, it should be LoRA-compatible:

> "so... LORA'able?" — Juampab12, April 3, 2025

(Implied yes based on Kijai's confirmation of identical structure)

**However (April 5, 2025):** Kijai noted that LoRA compatibility may be imperfect:

> "the base model weights are changed so not gonna be perfect" — Kijai, April 5, 2025

---

## Kijai Conversion (April 5, 2025)

Kijai converted SkyReels A2 to work with VACE-style reference conditioning:

**Model:** `Kijai/WanVideo_comfy/blob/main/Wan2_1_SkyreelsA2_fp8_e4m3fn.safetensors`

### Key Features

- **14B I2V model** with reference support
- Works like VACE with reference and start frame
- Can also do normal I2V without reference
- **No extra VRAM cost** compared to standard 14B I2V
- **No control inputs** -- reference and start frame only

> "same as VACE with reference and start frame, but it's 14B model" — Kijai, April 5, 2025

> "it's far better for I2V as it uses the 14B I2V" — Kijai, April 5, 2025

> "in fact it can do normal I2V just as it is too" — Kijai, April 5, 2025

### Reference Handling

**Multiple references supported:**

Unlike VACE which uses a single reference image, SkyReels A2 appears to support 2-3 reference images:

> "seems it can support more than one, didn't look into that, 2-3" — Kijai, April 5, 2025

**Reference placement:**

Kijai initially placed the reference as the last latent but corrected this:

> "I think I made mistake actually.. the latent ends up last 😄" — Kijai, April 5, 2025

> "it still works tho" — Kijai, April 5, 2025

The reference should be the first latent (like VACE):

> "when adding to front instead, like it should.. (fist latent not removed here hence the start noise)" — Kijai, April 5, 2025

**CLIP embed handling:**

SkyReels A2 uses CLIP embeds for all reference images:

> "looks like they use all the images as clip embeds btw" — Kijai, April 5, 2025

> "concat all 3 clip embeds" — Kijai, April 5, 2025

**Image padding:**

The model pads the first frame image:

> "and looks like they pad the first frame image always too" — Kijai, April 5, 2025

> "gotta pad that to get their results I think" — Kijai, April 5, 2025

**CLIP image encoding:**

CLIP images can only be squares. When offsetting subjects significantly, ensure the image-to-clip encode fits properly:

> "When you offset the bear that much, make sure the image to clip encode fits it because by default it does center crop" — Kijai, April 5, 2025

> "Clip images can only be squares" — Kijai, April 5, 2025

### Advantages Over VACE

**VRAM efficiency:**

> "VACE for 14B is gonna be tough to run" — Kijai, April 5, 2025

> "in that sense this is better" — Kijai, April 5, 2025

SkyReels A2 provides 14B quality with reference support at the same VRAM cost as standard 14B I2V, whereas VACE 14B (when released) will require significantly more VRAM due to the additional VACE blocks.

**I2V quality:**

> "curiously at least my initial test just doing normal I2V with this gave different results than the base I2V" — Kijai, April 5, 2025

> "so it might be better I2V model too" — Kijai, April 5, 2025

### Limitations

**No control inputs:**

Unlike VACE, SkyReels A2 does not support depth, pose, or other control signals:

> "skyreels has no controls hey, its just ref ?" — Draken, April 5, 2025

(Confirmed by Kijai's description -- reference and start frame only)

**No video-to-video:**

As of April 6, 2025, SkyReels A2 does not support v2v workflows:

> "seems you can't do v2v with skyreel :/" — JmySff, April 6, 2025

**LoRA compatibility:**

> "the base model weights are changed so not gonna be perfect" — Kijai, April 5, 2025

Since SkyReels A2 is a finetune rather than an add-on module, LoRAs trained on base Wan 2.1 may not work as well as they do with VACE.

---

## Technical Details

**Frame rate:** 15 fps (unusual for Wan-based models)

> "I wonder why it is 15 fps" — Benjimon, April 3, 2025

**Format:** Diffusers format only (as of April 3, 2025)

> "diffusers format, would take some effort to convert" — Kijai, April 3, 2025

Conversion to ComfyUI format would require work, though Kijai noted it "could be simple" -- not yet attempted as of April 3, 2025.

**Update (April 5, 2025):** Kijai completed the conversion and released an fp8 version.

---

## Usage

### Reference Image Composition

The composition and size of subjects in reference images is critical:

> "the composition and size of subjects is quite import for the final output" — slmonker, April 5, 2025

**Best practices:**
- Plan the layout and size of subjects when uploading images
- Position subjects where you want them to appear in output
- Resize subjects appropriately for the scene
- Use solid backgrounds (white or gray) for cleaner results

> "if ur bear on left ,ur person on right, and the last thing u should do is resize the people and subject u wanna show" — slmonker, April 5, 2025

**Preview image planning:**

> "Once you master the rules of setting preview images, everything becomes very smooth" — slmonker, April 5, 2025

### Native ComfyUI Support

Kijai noted that SkyReels A2 should work in native ComfyUI with minimal changes:

> "skyreels should work in native too with minimal changes, unsure how multiple clip embeds are handled though" — Kijai, April 5, 2025

However, as of April 6, 2025, there is no way to use more than 1 clip embed in native ComfyUI:

> "skyreelsA2 on native almost works, but there's no way to use more than 1 clip embed currently in native so it fails to keep the other images besides the first" — Kijai, April 6, 2025

---

## Quality Assessment

**Community reactions (April 3, 2025):**

> "idk it looks better than VACE to me" — Juampab12, April 3, 2025

> "but it's likely based on HYV so unfair comparison since VACE is 1.3b" — Juampab12, April 3, 2025

(Note: Later confirmed to be Wan 14B, not Hunyuan)

**Comparison to SkyReels I2V:**

> "I liked the skyreels i2v model alot" — Benjimon, April 3, 2025

> "skyreels was bigger and slower than hunyuan but a good bit better" — Benjimon, April 3, 2025

**Community examples (April 5-6, 2025):**

Multiple users reported excellent results with character consistency and multi-subject composition:

> "Now we have evidence to prove that China invented the AK rifle 1000 years ago" — slmonker, April 5, 2025 [🤣]

(Referring to a successful historical character generation)

---

## Known Issues

### Lighting Integration

Some examples show subjects that don't integrate well with background lighting:

> "Some of them just don't fit into the background" — Screeb, April 3, 2025

> "yeah lighting is not adjusted" — Juampab12, April 3, 2025

> "but 'chroma'/composition is good" — Juampab12, April 3, 2025

**Example issues:**
- Subjects appear composited rather than naturally integrated
- Lighting doesn't match between foreground and background
- Suggests training on automated dataset that composited videos together

> "I'm guessing they trained on an automated dataset that just composited videos on one another" — Screeb, April 3, 2025

**Proposed workaround:**

> "a 1.3b pass will fix that haha" — Juampab12, April 3, 2025

Using a Wan 1.3B refinement pass may help integrate lighting and composition.

### Character Deviation

Some users reported large character deviation from reference:

> "I don't know why the character deviation is very large" — slmonker, April 5, 2025

This may be related to reference image composition, CLIP embed handling, or prompt-to-reference matching.

---

## Availability

**HuggingFace download issues (April 3, 2025):**

> "huggingface is slow rn" — Benjimon, April 3, 2025

Users reported slow download speeds from HuggingFace at the time of release.

**ComfyUI support:**

As of April 3, 2025, no ComfyUI conversion was available. Kijai noted it would require conversion work from diffusers format.

**Update (April 5, 2025):** Kijai released a converted fp8 version for ComfyUI.

---

## Community Interest

**Mixed reception:**

The community showed interest but noted significant limitations:
- Lack of control support reduces utility compared to VACE
- Lighting integration issues in examples
- Diffusers-only format limits accessibility (resolved April 5)
- Preview status suggests incomplete release

Kijai expressed limited interest in converting the model due to lack of control features:

> "all those examples are of no interest" — Kijai, April 3, 2025

**However (April 5, 2025):** Kijai reconsidered and converted the model, noting its advantages for I2V with reference support at lower VRAM cost than VACE 14B.

**Positive reception (April 5-6, 2025):**

After the conversion, community interest increased significantly with users reporting excellent results for character consistency and multi-subject composition.

---

## Use Cases

**Best for:**
- 14B I2V with reference image support
- Character animation with reference consistency
- Multi-subject composition
- Users who need VACE-like reference features but can't run VACE 14B due to VRAM
- Normal I2V tasks (may be better than base 14B I2V)

**Not suitable for:**
- Control-based workflows (depth, pose, etc.) -- use VACE instead
- Users who need both reference AND control signals
- Video-to-video workflows (not supported as of April 6, 2025)

---

## See Also

- [[wan-2.1]] — Base model architecture
- [[vace]] — Alternative with control support but higher VRAM requirements
- [[lora]] — LoRA compatibility and usage

## External Resources

- [SkyReels A2 on HuggingFace](https://huggingface.co/Skywork/SkyReels-A2)
- [SkyReels A2 GitHub](https://github.com/SkyworkAI/SkyReels-A2)
- [SkyReels A2 Project Page](https://skyworkai.github.io/skyreels-a2.github.io/)
- [Kijai Converted Model](https://huggingface.co/Kijai/WanVideo_comfy/blob/main/Wan2_1_SkyreelsA2_fp8_e4m3fn.safetensors)
