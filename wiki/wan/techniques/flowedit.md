---
title: FlowEdit for Video-to-Video
aliases: [flowedit, flow-edit, vid2vid, video-to-video]
last_updated: 2025-03-05
---

# FlowEdit for Video-to-Video

FlowEdit is a video-to-video (V2V) technique that allows using an input video to guide the generation of a new video while maintaining temporal consistency. It works by using the input video's motion and structure to guide the diffusion process.

## Overview

FlowEdit enables V2V workflows with Wan 2.1 by:
- Using an input video as guidance for motion and structure
- Maintaining temporal consistency across frames
- Supporting upscaling workflows (low-res pass → upscale → high-res pass)
- Working with context windows for long video generation
- **Compatible with TeaCache** (confirmed March 5, 2025)

> "context windowed flowedit test" — Kijai, March 4, 2025

> "should be able to go endlessly" — Kijai, March 4, 2025 (referring to 129-frame context windowed flowedit)

> "I think I did get it to work with flowedit at least" — Kijai on TeaCache compatibility, March 5, 2025

## Implementation

### Kijai Wrapper

FlowEdit is implemented in the Kijai wrapper with dedicated nodes for V2V workflows.

**Key features:**
- Works with both T2V and I2V models
- Supports context windowing for long videos
- Can be combined with upscaling workflows
- **Context window support added March 4, 2025**
- **TeaCache compatible** (March 5, 2025)

> "flowedit with context window support is in the wrapper now too, didn't make example workflow yet as, like always, flowedit is tough to figure out good settings for" — Kijai, March 4, 2025

**Note:** FlowEdit settings can be challenging to dial in. The wrapper provides the functionality but finding optimal settings requires experimentation.

### Native ComfyUI

FlowEdit workflows are also possible in native ComfyUI using Hunyuan FlowEdit nodes, though implementation details may differ from the wrapper.

> "Are these using the hunyuan FlowEdit nodes with Wan?" — Neex, March 4, 2025

> "These were tests on it for the wrapper. But can be done with those nodes too ofc, just not with context windows yet" — Kijai, March 4, 2025

## Use Cases

### Video-to-Video Generation

- Transform existing videos while maintaining motion
- Style transfer from one video to another
- Enhance or modify existing footage
- Creative transformations (e.g., ballerina to statue, dog to horse)

**Example transformations reported by community:**
- Ballerina to statue — citizenplain, March 4, 2025
- Dog to horse — citizenplain, March 4, 2025
- Destruction/transformation effects with high adherence

### Upscaling Workflows

FlowEdit is particularly useful for multi-pass upscaling:

1. **First pass:** Generate at low resolution (e.g., 480x272 or 640x352)
2. **Upscale:** Use pixel-space upscaler (2x or 4x)
3. **Second pass:** Use FlowEdit with upscaled video as guidance

> "1st pass 480x277, 2nd pass upscaler x2" — N0NSens, March 4, 2025

> "initial 640x352, upscaled to 1280x704 by flowedit" — N0NSens, March 4, 2025

**Challenges with upscaling workflows:**
- Can be "insanely slow" — N0NSens, March 4, 2025
- Implementation in wrapper vs native may differ
- Requires careful VRAM management

### Long Video Generation

FlowEdit works with context windows for generating very long videos:

- **129 frames** confirmed working with context windows (Kijai, March 4, 2025)
- Potential for "endless" generation by chaining context windows
- Maintains consistency across window boundaries

### Looping Videos

FlowEdit can be used to create seamless loops:

> "endless magic trick" — Benjaminimal, March 4, 2025 (demonstrating looping FlowEdit)

> "endless loops?! how?" — Fill, March 4, 2025

> "flow edit ?" — Lumifel, March 4, 2025

> "yea" — Kijai, March 4, 2025

See [[context-windows]] for more on looping techniques.

## Settings

**Note:** Specific settings for FlowEdit are still being explored by the community. General V2V principles apply:

- Lower denoise values preserve more of the input video
- Higher denoise values allow more creative freedom
- Context window settings follow standard recommendations (81 frames, 16 overlap)
- Settings are "tough to figure out" and require experimentation — Kijai, March 4, 2025

## Comparison to Other Techniques

| Method | Control Type | Consistency | Speed | Flexibility |
|--------|-------------|-------------|-------|-------------|
| **FlowEdit** | Video input | High | Medium | High |
| **Latent Guides** | Latent space | Medium | Fast | Very High |
| **VACE** | Preprocessors | High | Medium | High |
| **I2V** | Single image | Medium | Fast | Low |

## Known Issues

- **Speed:** FlowEdit workflows can be slow, especially with upscaling
- **VRAM:** Multi-pass workflows require careful VRAM management
- **Implementation differences:** Wrapper and native implementations may behave differently
- **Limited documentation:** FlowEdit is still being actively developed and documented
- **Settings difficulty:** Finding optimal settings is challenging and requires experimentation
- **Context windows:** Native ComfyUI does not yet support context windows with FlowEdit (as of March 4, 2025)

### Triton Errors

Some users encounter Triton-related errors when running FlowEdit:

> "could anyone fill me in on why I sometimes get a message saying I need triton installed when running FlowEdit?" — Neex, March 4, 2025

**Solutions:**
- Switch TorchCompile from inductor to cudagraph mode
- Reduce frame count to lower VRAM usage
- Triton is an optimization, not strictly required
- Behavior can change based on available VRAM

> "Some behaviour can change depending on how much free VRAM you have at the time, so possibly once you'd run it you had a bit less (due to caching) and that triggered a different thing to happen (requiring Triton)" — Screeb, March 4, 2025

## Workflow Examples

Kijai has posted example workflows demonstrating:
- Basic V2V with FlowEdit
- Context windowed FlowEdit for long videos
- Integration with upscaling pipelines

Check the Kijai wrapper repository for the latest examples.

**Community examples:**
- Ballerina to statue transformation — citizenplain, March 4, 2025
- Dog to horse transformation — citizenplain, March 4, 2025
- Upscaling from 640x352 to 1280x704 — N0NSens, March 4, 2025

## See Also

- [[wan-2.1]] — Base model that works with FlowEdit
- [[context-windows]] — For long video generation with FlowEdit
- [[latent-guides]] — Alternative V2V technique
- [[vace]] — Control method that can complement FlowEdit
- [[comfyui]] — Platform for building FlowEdit workflows
- [[teacache]] — Compatible optimization for FlowEdit

## External Resources

- [Kijai WanVideoWrapper Repository](https://github.com/kijai/ComfyUI-WanVideoWrapper) — Contains FlowEdit example workflows
- [FlowEdit Discussion Thread](https://discord.com/channels/1076117621407223829/1346134166311403692) — Community discussion and examples
