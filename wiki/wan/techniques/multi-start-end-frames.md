---
title: Multi-Start and Multi-End Frame Generation
aliases: [multi-start-frames, multi-end-frames, multiple-start-frames, multiple-end-frames]
last_updated: 2025-03-30
---

# Multi-Start and Multi-End Frame Generation

Multi-start and multi-end frame generation is a technique that uses multiple frames (instead of just one) as conditioning for video generation, enabling better video extension, inpainting, and motion continuity.

---

## Overview

**Discovered:** March 30, 2025 by Kijai

**Key insight:** The Wan VAE encodes 4 frames into each latent. By providing multiple start or end frames (2-5 frames), the model can better understand motion and context, leading to smoother extensions and more coherent inpainting.

> "right, yeah I was going about it all wrong.. the VAE encodes 4 images in one latent so of course we can have 4 images as start......" — Kijai, March 30, 2025

**Supported models:**
- Wan 2.1 Fun InP (Inpainting) model
- Works with both T2V and I2V variants

---

## How It Works

### Standard Single-Frame Conditioning

**Traditional I2V:**
1. Provide 1 start frame
2. Model generates remaining frames
3. Limited motion context

**Traditional video extension:**
1. Take last frame of previous video
2. Use as start frame for next generation
3. Often results in stuttering or motion discontinuity

### Multi-Frame Conditioning

**With multiple start frames:**
1. Provide 2-5 start frames (batched images)
2. Model understands motion trajectory
3. Generates continuation with better motion coherence

**With multiple end frames:**
1. Provide 2-5 end frames (batched images)
2. Model knows where video should end up
3. Generates interpolation between start and end

**With both start and end frames:**
1. Provide multiple start frames AND multiple end frames
2. Model interpolates between known beginning and end
3. Best for inpainting and controlled generation

---

## Implementation

### Requirements

- Kijai wrapper (latest version as of March 30, 2025)
- Wan 2.1 Fun InP model
- ComfyUI with batch image support

### Basic Setup

**For multi-start frames:**
1. Load 2-5 images as a batch
2. Connect to start_image input
3. Generate as normal

**For multi-end frames:**
1. Load 2-5 images as a batch
2. Connect to end_image input (if using inpainting)
3. Generate as normal

**Node configuration:**
> "Just batch in the images" — Kijai, March 30, 2025

> "Only tried 2-5 which all seemed to work" — Kijai, March 30, 2025

---

## Use Cases

### Video Extension

**Problem:** Traditional video extension using only the last frame often results in stuttering or motion discontinuity.

**Solution:** Use the last 4 frames of the previous video as start frames for the next generation.

> "so it does definitely help with extension to use more" — Kijai, March 30, 2025

**Comparison (March 30, 2025):**
- **1 start frame:** Motion continues but may stutter
- **4 start frames:** Smoother motion continuation, better trajectory understanding

**Example workflow:**
1. Generate initial video (81 frames)
2. Extract last 4 frames
3. Use as start frames for next generation
4. Result: Smoother transition between segments

### Video Inpainting

**Use case:** Fill in missing frames in the middle of a video

**Setup:**
1. Provide first 4 frames as start_image
2. Provide last 4 frames as end_image
3. Provide temporal mask indicating which frames to inpaint
4. Model fills in the gap with motion-coherent frames

> "guess it's an actual inpainting model" — Kijai, March 30, 2025

> "you can now simply add your own temporal mask, and full video with matching length as 'start_image'" — Kijai, March 30, 2025

**Temporal masking:**
- Binary masks only (no fading)
- White = inpaint this frame
- Black = keep original frame

> "only binary works though, can't fade" — Kijai, March 30, 2025

### Motion Interpolation

**Use case:** Create smooth transitions between two known states

**Setup:**
1. Provide starting frames (2-5 frames)
2. Provide ending frames (2-5 frames)
3. Model generates smooth interpolation

**Applications:**
- Character pose transitions
- Camera movement interpolation
- Object motion paths

### Stop-Motion Effect

**Experimental use case:** Create stop-motion-style animation

**Setup:**
1. Use 4 start frames that are far apart (jarring transitions)
2. Model may generate stop-motion-like interpolation

> "Wonder what will happen if first 4 are more jarring. Like father apart." — VK, March 30, 2025

> "definitely interesting to test" — dawniii#0, March 30, 2025

> "I wonder if you could maybe even get like a consistent stop motion with that" — dawniii#0, March 30, 2025

**Community testing (March 30, 2025):**
- VK tested with jarring frame transitions
- Result: "Neat" animation effect
- "Odd" but interesting visual style
- Successfully creates animation-like motion

> "yea it really is giving that animation effect!!" — dawniii#0, March 30, 2025

---

## Technical Details

### VAE Encoding

**Key understanding:** The Wan VAE encodes 4 frames into each latent.

**Implications:**
- Providing 4 start frames = 1 latent of motion context
- Providing 8 start frames = 2 latents of motion context
- More frames = better motion understanding (up to a point)

**Tested range:**
> "Only tried 2-5 which all seemed to work" — Kijai, March 30, 2025

### I2V Model Behavior

**Standard I2V encoding (spacepxl's explanation):**

> "The i2v model encodes the first frame by itself, then the last frame by itself, then joins them together for the model input. So it starts with a first frame latent, and ends with another first frame latent in the place of the last 4 frames." — spacepxl, March 30, 2025

**Better approach for multi-frame:**

> "The right way to do it IMO, is to join the first and last frames with padding in between, then VAE encode, like you would for an inpaint model. Then you could handle any arbitrary frames as condition" — spacepxl, March 30, 2025

**Implication:** Future improvements could allow conditioning on arbitrary frame positions, not just start and end.

### Temporal Masking

**Current implementation:**
- Binary masks only (0 or 1)
- No gradient/fading support
- Mask must match video length

**Workflow:**
1. Create temporal mask (white = inpaint, black = keep)
2. Provide full video as start_image
3. Masked frames are regenerated
4. Unmasked frames are preserved

**Example (Kijai, March 30, 2025):**
- Original video with person walking
- Temporal mask on middle frames
- Inpainted result: Person continues walking with coherent motion

---

## Performance Considerations

### VRAM Usage

**Impact:** Minimal increase
- 4 start frames vs 1 start frame: Negligible VRAM difference
- VAE encodes them into same latent structure

### Generation Time

**Impact:** No significant change
- Same number of diffusion steps
- Slightly more VAE encoding time (negligible)

### Quality vs Quantity

**Optimal frame count:**
- **2-5 frames:** Tested and working
- **4 frames:** Aligns with VAE latent structure (recommended)
- **More than 5:** Untested, may not provide additional benefit

---

## Comparison to Other Techniques

| Technique | Start Frames | End Frames | Use Case |
|-----------|--------------|------------|----------|
| **Standard I2V** | 1 | 0 | Basic image-to-video |
| **Multi-start I2V** | 2-5 | 0 | Video extension, motion continuation |
| **Multi-end I2V** | 0 | 2-5 | Reverse generation (untested) |
| **Multi-start + Multi-end** | 2-5 | 2-5 | Inpainting, interpolation |
| **Context windows** | 1 | 0 | Long video generation |
| **Temporal masking** | Full video | 0 | Frame-level inpainting |

---

## Known Limitations

### Binary Masking Only

**Issue:** Temporal masks must be binary (0 or 1)

**Impact:** Cannot create smooth fade-in/fade-out effects

**Workaround:** Use multiple generations with different masks and blend in post-processing

### Model-Specific

**Requirement:** Currently only works with Wan 2.1 Fun InP model

**Status:** May be extended to other models in future

### Frame Count Limits

**Tested range:** 2-5 frames

**Unknown:** Whether more frames provide additional benefit

**Recommendation:** Use 4 frames to align with VAE latent structure

---

## Best Practices

1. **Use 4 frames when possible:**
   - Aligns with VAE's 4-frame latent structure
   - Provides good motion context
   - Tested and reliable

2. **For video extension:**
   - Extract last 4 frames of previous video
   - Use as start frames for next generation
   - Results in smoother transitions

3. **For inpainting:**
   - Provide both start and end frames
   - Use binary temporal mask
   - Test mask coverage before full generation

4. **For stop-motion effects:**
   - Use frames that are far apart
   - Experiment with different frame spacing
   - May require multiple attempts to get desired effect

5. **Batch images correctly:**
   - Ensure frames are in correct temporal order
   - Use ComfyUI batch image nodes
   - Verify frame count before generation

---

## Future Development

**Potential improvements:**

1. **Arbitrary frame conditioning:**
   - Condition on any frame positions, not just start/end
   - Would enable more flexible inpainting

2. **Gradient masking:**
   - Support for smooth fade-in/fade-out
   - Better blending between inpainted and original frames

3. **Model finetuning:**
   - Train models specifically for multi-frame conditioning
   - Could improve motion coherence further

4. **Extended frame counts:**
   - Test with more than 5 frames
   - Determine optimal frame count for different use cases

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| Black output | Ensure using Fun InP model; check frame batching |
| Stuttering motion | Use 4 frames instead of 1; verify frame order |
| Inpainting not working | Check temporal mask is binary; verify mask length matches video |
| Frames out of order | Verify batch order in ComfyUI |
| No improvement over single frame | Try 4 frames; ensure frames show motion progression |
| Stop-motion effect too subtle | Use frames that are farther apart |

---

## Community Examples

### Video Extension (Kijai, March 30, 2025)

**Setup:**
- 1 start frame vs 4 start frames
- Same prompt and settings

**Result:**
- 4 start frames: "it continues for a little bit with the motion only"
- Smoother motion continuation
- Better trajectory understanding

### Inpainting (Kijai, March 30, 2025)

**Setup:**
- 16 start frames + 16 end frames
- Temporal mask on middle frames
- Person walking in video

**Result:**
- Inpainted frames show coherent walking motion
- Smooth transition between original and inpainted frames
- "proof that it is indeed new frames"

### Stop-Motion Effect (VK, March 30, 2025)

**Setup:**
- 4 start frames with jarring transitions
- Standard generation settings

**Result:**
- "Neat" animation effect
- "yea it really is giving that animation effect!!"
- Successfully creates stop-motion-like motion

---

## See Also

- [[wan-2.1]] — Base model family
- [[context-windows]] — Alternative approach for long video
- [[video-extension]] — Traditional extension techniques
- [[inpainting]] — Frame-level inpainting
- [[i2v]] — Image-to-video generation

## External Resources

- [Kijai Wrapper Repository](https://github.com/kijai/ComfyUI-WanWrapper) — Implementation of multi-frame support
