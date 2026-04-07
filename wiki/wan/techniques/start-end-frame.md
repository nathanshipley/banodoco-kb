---
title: Start and End Frame Interpolation
aliases: [start-end-frame, first-last-frame, flf2v, image-keyframing]
last_updated: 2025-03-23
---

# Start and End Frame Interpolation

Start and End Frame interpolation is a technique for guiding Wan I2V generation by providing both a starting image and an ending image, allowing the model to generate a video that transitions between the two frames.

**Released:** March 20, 2025 by Kijai in the wrapper

**Status:** Experimental — the model is not explicitly trained for this task, so results vary

---

## Overview

Unlike traditional I2V which only conditions on a single starting image, Start/End Frame provides two image inputs:
- **Start frame:** The first frame of the video
- **End frame:** The target final frame

The model attempts to generate a smooth transition between these two frames, though it **never reaches the end frame perfectly** since it wasn't trained for true interpolation.

> "sort of, it can do some thing but also isn't a proper interpolation as the model isn't trained for that, it never really reaches the end frame perfectly, but it can pull towards it pretty well with some image pairs" — Kijai, March 20, 2025

---

## Implementation

### Kijai Wrapper

**New nodes (March 20, 2025):**
- **ImageClipVisionEncode (Start)** — Encodes the starting image
- **ImageClipVisionEncode (End)** — Encodes the ending image
- Both nodes replace the previous single `ImageClipEncode` node

**Key parameters:**
- **strength_1** — Influence of the start frame CLIP embedding (0.0-1.0+)
- **strength_2** — Influence of the end frame CLIP embedding (0.0-1.0+)
- **combine_method** — How to combine the two embeddings:
  - `average` — Average the two CLIP embeddings (recommended)
  - `sum` — Sum the embeddings (can be too strong)
  - `concat` — Concatenate the embeddings (added March 22, 2025)
- **crop** — Whether to crop images to 224x224 for CLIP (disable for better results)
- **noise_aug_strength** — Noise augmentation applied to latents

**Workflow changes:**
1. Replace `ImageClipEncode` with two new nodes
2. Connect start image to first node, end image to second
3. Both nodes connect to the I2V sampler
4. Adjust strengths and combine method as needed

> "replace ImageClipEncode with these two new nodes and you can key frame start/end. Adjustments are similar in concept to how iPA works. Works well with Loras btw too." — The Shadow (NYC), March 20, 2025

**Tiled CLIP Vision Encoding (March 22, 2025):**

Kijai added tiled CLIP vision encoding to improve coverage of the full image:

- **tile_size** — Number of tiles to use (default: 4)
- **ratio** — How much of the full embed vs combined tiles (0.0-1.0)
- Tiles the image into multiple 224x224 crops and averages the CLIP embeddings
- Provides better coverage of the full image than center crop

> "you can send any size, it tiles it to the number of tiles you specific, and ratio is how much of the full embed is used vs the combined tiles" — Kijai, March 22, 2025

**Important:** Do NOT use the PrepImageForClipVision node if you want to use tiles — it defeats the whole purpose.

**Concat method (March 22, 2025):**

Kijai added concatenation as a combine method:

> "added concat because I just realised that it should work now that I modified the cross attn code" — Kijai, March 22, 2025

With concat, the combined clip embeds shape becomes:
```
Clip embeds shape: torch.Size([2, 257, 1280])
Combined clip embeds shape: torch.Size([1, 514, 1280])
```

**Tiled encoding results (March 22, 2025):**

Kijai tested tiled vs non-tiled encoding:
- **Non-tiled:** Standard center crop single embed
- **4 tiles:** Better detail preservation, less burning
- **Average combine method:** Produced better results than concat in testing

> "both worked better than the usual center crop single embed" — Kijai, March 22, 2025

### Native ComfyUI

**Status:** Not yet implemented as of March 22, 2025

The wrapper implementation uses CLIP vision encoding which could theoretically be ported to native, but no native nodes exist yet.

---

## Settings & Best Practices

### Recommended Settings

**For smooth transitions:**
- **strength_1:** 0.8
- **strength_2:** 0.8
- **combine_method:** average
- **crop:** disabled (allows CLIP to see full frame)
- **tile_size:** 4 (for tiled encoding)
- **ratio:** 1.0 (full tiles)

**For seamless looping (same start/end):**
- Use the same image for both start and end
- **strength_1:** 1.0
- **strength_2:** Can be disabled or set to 0.0
- Works well with rotation LoRAs for 360° spins

> "start/end frame example" — The Shadow (NYC), March 20, 2025 (demonstrating seamless loop)

### CLIP Vision Considerations

**Image preprocessing:**
- CLIP vision always processes at **224x224** internally
- The `crop` parameter controls whether to crop or stretch
- **Disabling crop** allows CLIP to see more of the image (recommended)
- Can use `PrepImageForClipVision` node from IPAdapter for manual control (but not with tiled encoding)

> "it's always 224" — Kijai, March 20, 2025

> "crop just means it's cropped instead of stretched" — Kijai, March 20, 2025

**Tiling for better coverage:**

Kijai implemented Matteo's tiling technique to allow CLIP vision to see more detail:
- Tile the image into multiple 224x224 crops
- Average the CLIP embeddings from all tiles
- Provides better coverage of the full image

> "May try that tiling method Matteo came up with too" — Kijai, March 20, 2025

### Combining Embeddings

**Average vs Sum vs Concat:**
- **Average** — Recommended default, balances both frames
- **Sum** — Can be too strong, may destroy results
- **Concat** — Concatenates embeddings for larger context (added March 22, 2025)

> "average 'works' as in doesn't destroy result, sum seems to" — Kijai, March 20, 2025

**Single image vs both:**

Kijai is testing whether using both images or just the start frame produces better results:
- Some image pairs work better with both
- Others work better with just the start frame
- "Situational" — depends on the specific images

> "I guess it's situational" — Kijai, March 20, 2025

### Achieving End Frame Accuracy (March 22, 2025)

deebo asked about getting closer to the end frame:

> "what might be the key properties to make the video hit the end frame close as possible?" — deebo, March 22, 2025

Kijai's response:

> "key would be to train a model or a LoRA at least with the method, the model as it is can't really fully do that otherwise (pretty sure)" — Kijai, March 22, 2025

> "using both start and end frame as clip embeds can help a bit" — Kijai, March 22, 2025

**Workarounds:**
- Use both start and end frame CLIP embeds
- Train a LoRA specifically for start/end frame interpolation
- Fake it by adding the last frame to the end of the video with cross-fade
- Use looping video datasets for training

> "You could fake it a bit and add the last frame init image to the end of the video, maybe with some cross-fade or something" — Kijai, March 22, 2025

---

## Use Cases

### Smooth Transitions

Generate videos that transition between two different images:
- Character transformations
- Scene changes
- Morphing effects
- Style transitions

**Example prompts:**
- "black mask dissolves to reveal skeleton underneath"
- "ballerina transforms into statue"
- "day transitions to night"

### Seamless Looping

Use the same image for both start and end to create perfect loops:
- Rotation animations (with rotation LoRA)
- Oscillating motions
- Cyclic transformations

> "also can combine with <@211685818622803970>'s Wallpaper lora (low strength) which is also yielding interesting results for seamless looping" — The Shadow (NYC), March 20, 2025

**Looping workflow:**
1. Use same image for start and end
2. Apply rotation or motion LoRA
3. Generate 81 frames
4. Result loops seamlessly (with minor cleanup)

**Known issue:** Extra frames at beginning (1) and end (4) need to be removed in post for perfect loops.

> "seems that for seamless using Start/End with both ImageClips connected it introduces 1 frame extra in begining and 4 frames extra in end... when I remove these in post we have something very close indeed." — The Shadow (NYC), March 20, 2025

**Frame removal in ComfyUI (March 22, 2025):**

const username = undefined; shared a solution:

> "you could use 'Select frames' node with an index '1:-4', just after the vae decode" — const username = undefined;, March 22, 2025

Cubey also developed a split index method to remove bad frames.

### LoRA Compatibility

Start/End Frame works well with LoRAs:
- Character LoRAs maintain identity through transition
- Motion LoRAs (rotation, camera movement) enhance the effect
- Style LoRAs can be applied to both frames

> "Works well with Loras btw too." — The Shadow (NYC), March 20, 2025

---

## Quality & Limitations

### Not True Interpolation

The model was **not trained for interpolation**, so it doesn't perfectly reach the end frame:
- The final frame will be **close** to the target but not identical
- Works better with similar start/end images
- Large differences between frames may produce wipe transitions

> "it never really reaches the end frame perfectly, but it can pull towards it pretty well with some image pairs" — Kijai, March 20, 2025

### Transition Quality

With very different start/end images, the model may:
- Perform a simple wipe transition (like a linear dissolve)
- Struggle to create meaningful intermediate frames
- Benefit from noise injection to create more dynamic transitions

**Potential improvement:**
The Shadow (NYC) suggested injecting noise similar to transitional LoRAs (like the Venom example for Hunyuan) to create more dynamic morphing instead of simple wipes.

> "think there is way to inject some noise similar to how a transitional lora might do (think Venom example for HYv) so when we Start/End with very different images it doesn't simply do a wipe transition" — The Shadow (NYC), March 20, 2025

### Image Pair Dependency

Results are highly dependent on the specific image pair:
- Some pairs produce excellent smooth transitions
- Others may show visible seams or abrupt changes
- Testing multiple seeds recommended

**Example results (March 22, 2025):**

VRGameDevGirl84 reported a "huge failure" when starting with a close-up and ending with a further away shot, suggesting that maintaining similar framing helps.

---

## Advanced Techniques

### Noise Augmentation

The `noise_aug_strength` parameter adds noise to the latents:
- Can help with transitions between very different images
- May reduce adherence to the exact input images
- Recommended values: 0.0-0.3

> "is noise_aug equally applied to start_latent and end_latent? I wonder if may just be better in a separate node to apply different values to each" — dawniii#0, March 20, 2025

**Recommended by community (March 22, 2025):**

const username = undefined; suggested:

> "perhaps increase the noise_aug_strenght in `WanVideo ImageToVideo Encode` node. Something like `0.095` and play around with the value" — const username = undefined;, March 22, 2025

### Latent Strength Control

Adjusting the latent strength can improve transitions:
- Lower strength (0.8) creates more natural transitions
- Higher strength (1.0) maintains closer adherence to input images

> "With the repo, it seems that lowering the latent strength help for more natural transition and better prompt understanding" — IllumiReptilien, March 20, 2025

### Combining with Depth Control

Start/End Frame can be combined with depth control LoRAs:
- Use depth maps to guide the transition structure
- Provides additional control over the interpolation path
- Requires careful balancing of strengths

### Shift Parameter (March 22, 2025)

dawniii#0 suggested:

> "try turning up the shift" — dawniii#0, March 22, 2025

Higher shift values may help with motion and transition quality.

---

## Comparison to Alternatives

### vs FLF2V (First-Last-Frame)

Wan 2.1 includes an official **FLF2V-14B-720P** model trained specifically for first-last-frame interpolation:
- FLF2V is explicitly trained for this task
- Start/End Frame is a hack using I2V + CLIP embeddings
- FLF2V likely produces better interpolation quality
- Start/End Frame is more flexible (works with any I2V model)

### vs RealFill

RealFill provides start frame conditioning:
- RealFill: Single start frame, T2V generation
- Start/End: Both start and end frames, I2V generation
- Start/End provides more control over the final result

> "but with RF you can supply a start frame, with this it's just t2v 😦" — HeadOfOliver, March 21, 2025

### vs Traditional I2V

Traditional I2V only conditions on the first frame:
- More freedom in motion and content
- Less control over the final result
- Start/End Frame constrains both beginning and end

---

## Known Issues

### Extra Frames in Output

When using both start and end frames, the output includes:
- **1 extra frame at the beginning**
- **4 extra frames at the end**

These need to be removed in post-processing for seamless loops.

**Workaround:** Remove frames manually after generation using "Select frames" node with index "1:-4".

> "when using the same start + end frames, i have hunch that removing that second image clip will help remove this issue" — The Shadow (NYC), March 20, 2025

### Wipe Transitions

With very different start/end images, the model may perform a simple wipe transition (like a linear dissolve) rather than a meaningful morph.

**Potential solutions:**
- Use more similar start/end images
- Add noise augmentation
- Use transitional LoRAs (future development)

### CLIP Vision Limitations

CLIP vision operates at 224x224, which may lose detail from high-resolution images:
- Disabling crop helps but still limited
- Tiling approach (implemented March 22, 2025) improves this
- CLIP embeddings are less influential than the actual image latents

> "the main thing is still the image encoded in latent space" — Kijai, March 20, 2025

### Prompt Requirement (March 22, 2025)

VRGameDevGirl84 asked:

> "so with start and end frame, is there no positive prompt?" — VRGameDevGirl84, March 22, 2025

The answer is unclear from the messages, but based on the workflow structure, prompts are still used alongside the start/end frame conditioning.

---

## Future Development

**Planned improvements:**
- Tiling support for better CLIP coverage (IMPLEMENTED March 22, 2025)
- Separate noise augmentation for start/end latents
- Better transition quality for dissimilar images
- Native ComfyUI implementation
- Transitional LoRAs for morphing effects
- Masking support for CLIP embeddings

**Community suggestions:**
- Noise injection for dynamic transitions (The Shadow NYC)
- Scheduled gradients to push latents (similar to AnimateDiff)
- Training transition-specific LoRAs
- Looping video dataset training

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| End frame not reached | Expected behavior; model not trained for true interpolation |
| Wipe transition instead of morph | Use more similar images; add noise augmentation; try different seeds |
| Extra frames in output | Remove 1 frame from start, 4 from end using "Select frames" node with index "1:-4" |
| Poor quality transitions | Adjust strength values; try average instead of sum; disable crop; use tiled encoding |
| LoRA not visible | Ensure LoRA is connected to sampler; increase strength |
| CLIP vision errors | Update ComfyUI to latest nightly; ensure wrapper is updated |
| Huge failure with different framing | Maintain similar framing between start and end images |
| Tiling not working | Do NOT use PrepImageForClipVision node with tiled encoding |

---

## Example Workflows

**Seamless loop with rotation:**
1. Load same image for start and end
2. Set strength_1 = 1.0, strength_2 = 0.0 (or use only start node)
3. Apply rotation LoRA (e.g., Remade-AI/Rotate)
4. Prompt: "ice falling into glass of soda, splashing in slow motion"
5. Generate 81 frames
6. Remove extra frames using "Select frames" node (index "1:-4")
7. Result: Perfect 360° rotation loop

**Character transformation:**
1. Load character image for start
2. Load transformed version for end
3. Set strength_1 = 0.8, strength_2 = 0.8, average
4. Prompt: "character transforms from human to skeleton"
5. Generate with appropriate steps/CFG
6. Result: Smooth transformation sequence

---

## See Also

- [[wan-2.1]] — Base I2V model used for Start/End Frame
- [[lora]] — LoRAs that work well with Start/End Frame
- [[context-windows]] — For extending Start/End Frame videos
- [[comfyui]] — Platform for building Start/End Frame workflows

## External Resources

- [ComfyUI-WanVideoWrapper](https://github.com/kijai/ComfyUI-WanVideoWrapper) — Kijai's wrapper with Start/End Frame support
- [Example Workflow](https://discord.com/channels/1076117621407223829/1342763350815277067/1352376700306194573) — The Shadow NYC's demonstration
