---
title: Photo Restoration with Wan
aliases: [photo-restoration, old-photo, soviet-photo]
last_updated: 2025-03-13
---

# Photo Restoration with Wan

Wan's I2V capabilities can be used to bring old photographs to life, creating short animated videos from static images. This technique is particularly effective for historical photos, family archives, and damaged photographs.

> "the i2v i did yesterday on my wife's grandparents from old photos taken from the soviet union it was mindblowing" — fredbliss, March 13, 2025

---

## Overview

Wan I2V can:
- Animate faces in old photographs
- Add natural movement (blinking, slight head turns, breathing)
- Infer missing details from damaged photos
- Preserve the character and quality of the original image
- Work with low-quality source material

**Key advantage:** Unlike traditional photo restoration that only improves static quality, Wan can add lifelike motion while preserving the historical character of the image.

**Performance:** fredbliss reported being "shocked how fast it was" compared to Hunyuan Video, with VRAM usage around 11GB on a 4090 (suggesting block swap was not optimally configured).

---

## Basic Workflow

### 1. Prepare the Photo

**Minimal preparation:**
- No extensive restoration required
- Wan can work with damaged/low-quality photos
- Basic cleanup (dust removal, contrast adjustment) helps but isn't mandatory

**Optional preprocessing:**
- Upscale with traditional tools (Topaz, ESRGAN)
- Color correction
- Damage repair (tears, stains)
- Face enhancement

### 2. Generate with I2V

**Model:** Wan 2.1 I2V 14B (480p or 720p)

**Recommended settings:**
- Steps: 20-30
- CFG: 5-6
- Shift: 3.0 (for 480p) or 5.0 (for 720p)
- Frames: 81
- Prompt: Simple description of the person/scene
- **VAE:** fp32 for best quality (fredbliss used fp32 VAE)
- **Model precision:** fp16_fast (fredbliss's setup)

**Prompting tips:**
- Keep prompts simple and descriptive
- Mention the historical context if relevant
- Describe desired subtle motion ("slight smile," "gentle breathing")
- Avoid over-describing details already in the photo

### 3. Post-Processing

**Optional enhancements:**
- Frame interpolation to 24/30 FPS
- Color grading to match original photo tone
- Stabilization if needed
- Audio addition (period-appropriate music, ambient sound)

---

## Use Cases

### Family Archives

- Grandparents' wedding photos
- Childhood photos of parents
- Historical family portraits
- Immigration documents with photos

> "the i2v i did yesterday on my wife's grandparents from old photos taken from the soviet union" — fredbliss, March 13, 2025

### Historical Documentation

- Historical figures
- War photographs
- Cultural documentation
- Archival material

### Damaged Photos

- Torn or stained photographs
- Faded images
- Low-quality scans
- Partially obscured subjects

---

## Quality Expectations

### What Works Well

- **Facial animation:** Natural blinking, slight smiles, breathing
- **Subtle movement:** Gentle head turns, eye movement
- **Clothing:** Fabric movement, natural draping
- **Background:** Slight atmospheric movement

### Limitations

- **Large movements:** Avoid prompting for dramatic motion
- **Multiple subjects:** May struggle with group photos
- **Extreme damage:** Heavily damaged photos may need preprocessing
- **Anachronisms:** Model may add modern elements if not carefully prompted

---

## Emotional Impact

> "like i get this isnt even that good... but it just blew my mind" — fredbliss, March 13, 2025

Photo restoration with Wan has significant emotional impact:

- **Connection to ancestors:** Seeing grandparents "move" for the first time
- **Historical presence:** Making historical figures feel more real
- **Family storytelling:** Enhanced family history presentations
- **Memorial purposes:** Tribute videos for deceased relatives

**Note:** The emotional impact often exceeds the technical quality. Even imperfect results can be deeply meaningful.

---

## Advanced Techniques

### Photo Repair LoRA

Juampab12 suggested a potential application:

> "you could make a photo repairer with wan with this method" — Juampab12, March 13, 2025

**Concept:** Train a LoRA specifically for photo restoration:
- Dataset: Damaged photos → restored versions
- Learn to infer missing details
- Preserve historical character
- Add appropriate subtle motion

**Status:** Theoretical as of March 13, 2025. Not yet implemented.

### Multi-Pass Workflow

1. **First pass:** Basic I2V generation
2. **Second pass:** Upscale with [[control-lora#tile-control-v01--v02|tile control LoRA]]
3. **Third pass:** Color correction and stabilization
4. **Fourth pass:** Frame interpolation to higher FPS

### Combining with Other Tools

- **Magnific AI:** Upscale and enhance before I2V
- **Topaz Photo AI:** Repair damage before I2V
- **GFPGAN/CodeFormer:** Face restoration before I2V
- **Video denoisers:** Clean up I2V output (see [[wan-2.1#vae-compatibility|VAE noise cleanup]])

---

## Ethical Considerations

### Consent and Representation

- **Deceased subjects:** Consider family wishes
- **Historical figures:** Respect historical accuracy
- **Cultural sensitivity:** Be mindful of cultural context
- **Disclosure:** Clearly label AI-generated animations

### Accuracy vs. Interpretation

- **Movement inference:** Wan infers movement that never existed
- **Detail hallucination:** Model may add details not in original
- **Historical accuracy:** Balance emotional impact with factual representation
- **Labeling:** Make clear these are AI interpretations, not recovered footage

---

## Tips for Best Results

1. **Start with clear faces:** Photos with visible faces work best
2. **Simple prompts:** Don't over-describe what's already visible
3. **Subtle motion:** Request gentle, natural movement
4. **Multiple attempts:** Try different seeds for best result
5. **Preserve character:** Don't over-process; maintain historical feel
6. **Test settings:** Experiment with CFG and shift for your specific photo
7. **Use fp32 VAE:** For best quality encoding/decoding
8. **Optimize block swap:** fredbliss noted leaving 12GB VRAM unused, suggesting room for optimization

---

## Comparison to Other Methods

| Method | Pros | Cons |
|--------|------|------|
| **Wan I2V** | Natural motion, preserves character, works with damage, fast generation | Requires GPU, may add anachronisms |
| **MyHeritage Deep Nostalgia** | Easy to use, web-based | Limited control, subscription required |
| **D-ID** | Professional quality, API available | Expensive, less control |
| **Traditional restoration** | Accurate, no hallucination | Static only, no animation |
| **Hunyuan Video** | High quality | Much slower than Wan for this use case |

---

## See Also

- [[wan-2.1]] — Base model for photo restoration
- [[i2v]] — Image-to-video techniques
- [[control-lora]] — Tile control for upscaling restored photos
- [[comfyui]] — Platform for building restoration workflows

## External Resources

- [MyHeritage Deep Nostalgia](https://www.myheritage.com/deep-nostalgia) — Commercial alternative
- [GFPGAN](https://github.com/TencentARC/GFPGAN) — Face restoration preprocessing
- [Topaz Photo AI](https://www.topazlabs.com/topaz-photo-ai) — Photo enhancement preprocessing
