---
title: Mobius Looping
aliases: [mobius, mobius-looping, seamless-loop]
last_updated: 2025-03-18
---

# Mobius Looping

Mobius is a technique for generating seamless looping videos by manipulating the noise schedule during diffusion. Originally developed for CogVideo and released on March 16, 2025, it was quickly adapted for Wan by Kijai on March 17, 2025.

> "we have looping at home" — Kijai, March 17, 2025

---

## Overview

Mobius works by applying noise manipulation before and after the noise prediction step during sampling. This creates videos where the last frame seamlessly transitions back to the first frame, enabling perfect loops.

**Key characteristics:**
- **Simple implementation:** Only 2 lines of code added to the sampling process
- **No model retraining required:** Works with existing Wan models
- **Works with 1.3B and 14B:** Tested on both model sizes
- **Some quality trade-offs:** Can introduce noise/artifacts, especially on 14B
- **Model-specific effectiveness:** Works better with T2V than I2V

> "it's not far from what I was already playing with" — Kijai, March 17, 2025

> "though bit funny how you can make paper from what's effectively 2 lines of code 😄" — Kijai, March 17, 2025

---

## Implementation

### Kijai Wrapper

**Released:** March 17, 2025

Kijai implemented Mobius looping as a node in the wrapper within hours of the paper release.

**Node:** `WanVideoMobiusLoop` or `WanVideoLoopArgs`

**Parameters:**
- **loop:** Enable/disable looping (boolean)
- **shift_skip:** Number of steps to skip (default: 6)
- **start_percent:** When to begin applying loop manipulation (default: 0.1)
- **end_percent:** When to stop applying loop manipulation (default: 1.0)

**Important:** The loop argument must be connected. If not connected, you'll get an error:
```
Traceback (most recent call last):
  ...
TypeError: 'NoneType' object is not iterable
```

> "if you dont connect the arg Loop you get this can you check it" — avataraim#0, March 17, 2025

> "Classic" — Kijai, March 17, 2025

---

## Performance & Quality

### 1.3B Model

**Status:** Works well with minimal artifacts

**Tested configurations:**
- 41 frames, 30 steps: Clean loops
- 49 frames, shift 4-6: Good results with minimal gaps
- 81 frames: Good results
- 121 frames: Tested successfully
- 161 frames: Works but quality varies
- Various resolutions tested successfully

> "quick test with loop arg 1.3B" — avataraim#0, March 17, 2025 [🔥x5]

> "41 frame count 30steps 1.3B" — avataraim#0, March 17, 2025 [❤️]

**Community feedback:**
> "lol this cool ..." — avataraim#0, March 17, 2025 [😮x4]

> "this node loop seamless" — avataraim#0, March 17, 2025 [❤️]

**Optimal settings for 1.3B (March 17-18, 2025):**
- **81 frames**
- **30 steps**
- **shift_skip: 4-6** (4 reported as working great, 6 is CogVideoX default for 49 frames)
- **start_percent: 0.1**
- **end_percent: 1.0**

> "81 lengh 30 steps shift 4 start_precent 0.1 end_precent 1.0" — avataraim#0, March 17, 2025

> "shift 4 lol drunk" — avataraim#0, March 17, 2025 [🤣x2]

**Frame count considerations:**
- **49 frames = 13 latents** — shift 6 recommended (CogVideoX default)
- **81 frames = 21 latents** — shift 4-6 works well
- **121 frames and 161 frames** — tested, quality varies

> "49 frames = 13 latents" — Kijai, March 17, 2025

> "I think it should be half?" — Kijai, March 17, 2025

### 14B Model

**Status:** Works but with more noise/artifacts

> "can't get rid of the noise, otherwise it's fun" — Kijai, March 17, 2025 [❤️x3]

> "maybe it needs more steps on 14B..." — Kijai, March 17, 2025

**Observations:**
- More prone to noise than 1.3B
- May require more sampling steps for clean results
- Still produces functional loops despite artifacts
- **start/end parameters help but worsen seam**

> "fiddling with start/end does clearup 14B too, but seam gets bad" — Kijai, March 17, 2025

### Sampler Compatibility

**UniPC:** Works significantly better than other samplers

> "oh much better on unipc" — Kijai, March 17, 2025 [🔥x2 ❗ lets_go:1126884737181552791]

Kijai shared before/after comparisons showing UniPC produces much cleaner loops than other samplers.

### I2V Compatibility

**Status:** Does not work well with I2V models

> "couldn't get it to work for I2V" — Kijai, March 17, 2025

**Reason:** The CLIP image encoder used in I2V models interferes with the looping mechanism. The image embeddings keep pulling the generation back to a single reference point, preventing smooth loops.

> "the image embeddings just keep swinging it back to a single point" — fredbliss, March 18, 2025

> "and if i2v did work, it would also work for start frame / end frame" — fredbliss, March 18, 2025

**Technical explanation:**
- I2V uses both T5 text encoder AND CLIP vision encoder
- CLIP features are heavily focused on the reference image
- This strong conditioning prevents the temporal looping from working properly
- T2V only uses T5, so it doesn't have this limitation

> "the clip is actually pretty weak, you can even disable it and it stays on the image, it's the encoded image conditioning latent that's super strong" — Kijai, March 18, 2025

---

## Settings

### Recommended Settings by Frame Count

| Frames | Latents | Shift Skip | Notes |
|--------|---------|------------|-------|
| 41 | ~11 | 4-6 | Tested working |
| 49 | 13 | 6 | CogVideoX default |
| 81 | 21 | 4-6 | Most tested, works great |
| 121 | 31 | 5-6 | Tested, quality varies |
| 161 | 41 | 5 | Tested |

### Start and End Percent

**Default values:**
- **start_percent: 0.1** — Begin applying loop manipulation at 10% through sampling
- **end_percent: 1.0** — Continue until end of sampling

**Effect of adjusting:**
- **Higher start_percent (0.2-0.3):** Reduces artifacts but may worsen seam quality
- **Lower end_percent (0.9):** Can help with noise but worsens seam
- **14B benefits from adjustment** but at cost of seam quality

> "added start/end, but not sure if it's a good idea" — Kijai, March 17, 2025

> "makes seam worse but clears some of the noise otherwise" — Kijai, March 17, 2025

### Shift Skip Parameter

**Purpose:** Controls how many latent frames to skip during the loop manipulation

**Calculation:** For 49 frames (13 latents), shift 6 works well. For 81 frames (21 latents), shift 4-6 is recommended.

**Rule of thumb:** Shift skip should be roughly half the number of latents, but this varies by content and desired effect.

> "the shift 6 was for 49 frames in the cogvideox example, which should be same here" — Kijai, March 17, 2025

**Effect of different shift values:**
- **shift 1:** Very small gap, drunk-looking results
- **shift 4:** Working great for 81 frames
- **shift 5:** Good results for 161 frames
- **shift 6:** CogVideoX default for 49 frames, also works for 81
- **shift 10:** Not good
- **shift 12:** Works for 49 frames

> "shift 1 lol drunk" — avataraim#0, March 17, 2025 [🤣x2]

> "well 10 was no good" — Kijai, March 17, 2025

---

## Known Issues

### VAE Flash Artifact

**Problem:** Persistent flash/noise artifact that Kijai couldn't eliminate

> "can't get rid of the noise" — Kijai, March 17, 2025

This appears to be related to the VAE encoding/decoding process and is more prominent on 14B than 1.3B.

### Small Gaps at Loop Point

**Observation:** Even with optimal settings, there may be a very small visible gap at the loop point

> "there is very small gap, <@228118453062467585> this normal?" — avataraim#0, March 17, 2025

**Mitigation:** Adjusting shift_skip can minimize but not completely eliminate the gap. Shift 4 for 81 frames produces minimal gaps.

### Required Connection

**Problem:** Loop argument must be connected or workflow errors

**Solution:** Always connect the loop parameter, even if just setting it to a boolean value.

### Content-Specific Issues

**Cars driving sideways:**
> "There is a car driving sideways but at least the loop happens." — Alisson Pereira, March 17, 2025

Some content (particularly vehicles) may exhibit strange behavior in loops. This is likely due to Wan's existing issues with vehicle motion direction.

### Frame Count Considerations

> "i think need more frame to close the looop" — avataraim#0, March 17, 2025

Shorter videos may not have enough frames for smooth loop transitions. 81 frames appears to be a good baseline.

### Start/End Percent Trade-offs

**14B specific:** Adjusting start/end percent can reduce noise but worsens the seam quality at the loop point. This is a fundamental trade-off with the current implementation.

---

## Optimization Compatibility

### TeaCache

**Status:** Incompatible

> "also with teacache not working" — avataraim#0, March 17, 2025

> "yea it doesn't like TeaCache" — Kijai, March 17, 2025

TeaCache produces artifacts when combined with Mobius looping.

**Update (March 18, 2025):** Kijai confirmed that Mobius "doesn't seem to like other models than 1.3B, and it hates TeaCache."

### SLG and Enhance-a-Video

**Status:** Compatible

> "SLG and enhance-a-video was fine" — Kijai, March 17, 2025

Both Skip Layer Guidance and Enhance-a-Video work with Mobius looping without issues.

---

## Use Cases

### Seamless Background Loops

**Ideal for:**
- Animated backgrounds
- Ambient scenes
- Nature footage (waterfalls, clouds, etc.)
- Abstract animations

### Product Showcases

**Rotating products:**
> "I2V 81f attempt with 14b 480 + Rotate Lora" — The Shadow (NYC), March 17, 2025 [🔥x3]

Combining Mobius with rotation LoRAs creates seamless 360° product views.

### Motion Graphics

**Continuous motion:**
- Particles
- Geometric patterns
- Flowing elements

### Endless Loops

> "endless magic trick" — Benjaminimal, March 17, 2025

> "endless loops?! how?" — Fill, March 17, 2025

> "flow edit ?" — Lumifel, March 17, 2025

> "yea" — Kijai, March 17, 2025

Mobius can be combined with FlowEdit for creating endless loop effects.

---

## Comparison to Other Looping Techniques

| Method | Quality | Speed | Complexity | Model Support |
|--------|---------|-------|------------|---------------|
| **Mobius** | Good (1.3B), Fair (14B) | Fast | Simple | Wan T2V (both sizes) |
| **Context Windows (uniform_looped)** | Better for long video | Slower | Medium | Wan T2V and I2V |
| **Manual Frame Blending** | Variable | Slow | Complex | All models |
| **Latent Looping** | Good | Medium | Medium | Models with latent access |

**Advantages of Mobius:**
- No post-processing required
- Works during generation (not after)
- Simple to implement
- No additional VRAM overhead
- Fast generation

**Disadvantages:**
- Quality varies by model size
- Some content types loop better than others
- Noise artifacts on 14B
- Does not work with I2V
- Small gaps may be visible at loop point

**Kijai's recommendation (March 18, 2025):**
> "I don't feel like it's any good, somewhat works with 1.3B model but not the others.. I prefer using the context options for looping" — Kijai, March 18, 2025

For production use, context windows with uniform_looped may be more reliable, especially for I2V or when working with 14B models.

---

## Best Practices

1. **Use 1.3B for cleaner loops** — Less prone to noise artifacts
2. **Use UniPC sampler** — Significantly better results than other samplers
3. **Avoid TeaCache** — Incompatible, produces artifacts
4. **Use 81+ frames** — Shorter videos may not loop smoothly
5. **Test with SLG/Enhance-a-Video** — Both compatible and may improve quality
6. **Prompt for continuous motion** — Avoid prompts with clear start/end actions
7. **Consider content type** — Some subjects (vehicles) may behave strangely
8. **Adjust shift_skip based on frame count** — ~half the number of latents is a good starting point
9. **T2V only** — Don't attempt with I2V models
10. **Consider context windows for production** — More reliable for final output

---

## Example Workflows

**Basic loop (1.3B):**
- Model: Wan 1.3B T2V
- Frames: 81
- Steps: 30
- Sampler: UniPC
- Loop: Enabled
- Shift Skip: 4
- Start Percent: 0.1
- End Percent: 1.0

**High-quality loop (1.3B, tested settings):**
- Model: Wan 1.3B T2V
- Frames: 81
- Steps: 30
- Sampler: UniPC
- Loop: Enabled
- Shift Skip: 4
- Start Percent: 0.1
- End Percent: 1.0
- SLG: Enabled (optional, block 8)
- Enhance-a-Video: Enabled (optional)

**14B experimental:**
- Model: Wan 14B T2V
- Frames: 81
- Steps: 40-50 (more steps help with noise)
- Sampler: UniPC
- Loop: Enabled
- Shift Skip: 6
- Start Percent: 0.2-0.3 (helps with noise)
- End Percent: 0.9-1.0
- Note: Expect some noise/artifacts and seam quality trade-offs

---

## Community Examples

**avataraim#0's successful tests (March 17, 2025):**
- 81 frames, shift 4: "very good only one fade out in end"
- 49 frames, shift 12: "very close... very smallll gap"
- Multiple tests with different shift values showing clear progression

**TK_999's tests (March 17, 2025):**
- 161 frames (looped twice): Works but with artifacts
- Shift 5-6 tested
- Noted that changing shift_skip dramatically changes the video output

**Alisson Pereira's I2V test (March 17, 2025):**
- I2V 81 frames with 14B 480p + Rotate LoRA
- Result: "I2V is perfect 🤣" (though Kijai later confirmed I2V doesn't work well)

---

## Future Development

**Potential improvements:**
- Noise reduction for 14B
- Better seam quality with start/end adjustments
- I2V compatibility (may require fundamental changes)
- Adaptive shift_skip based on content
- Integration with other loop-specific techniques
- Better handling of directional motion (vehicles, etc.)

**Community interest:**
> "be sick for this to work in WAN!" — The Shadow (NYC), March 17, 2025 (before implementation)

The technique was highly anticipated and quickly adopted after release, though Kijai's later assessment suggests context windows may be more reliable for production use.

---

## See Also

- [[wan-2.1]] — Base model that supports Mobius looping
- [[context-windows]] — Alternative looping technique, preferred by Kijai for production
- [[samplers]] — UniPC sampler recommended for best results
- [[teacache]] — Incompatible with Mobius
- [[slg-uncond]] — Compatible optimization
- [[enhance-a-video]] — Compatible optimization

## External Resources

- [Mobius GitHub Repository](https://github.com/YisuiTT/Mobius) — Original implementation for CogVideo
- [Mobius Paper](https://arxiv.org/abs/[paper-id]) — Technical details and theory
- [Kijai Wrapper Repository](https://github.com/kijai/ComfyUI-WanVideoWrapper) — Wan implementation
