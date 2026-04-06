---
title: FPS Interpolation for Wan
aliases: [fps-interpolation, frame-interpolation, wan-fps]
last_updated: 2025-03-05
---

# FPS Interpolation for Wan

FPS interpolation is a technique for generating videos at lower frame rates (e.g., 2 FPS) and then interpolating to higher frame rates (e.g., 24 FPS) to achieve faster generation times while maintaining smooth playback. This is particularly useful for Wan 2.1, which is hardcoded to 16 FPS output.

## Overview

Wan 2.1 is hardcoded to generate at 16 FPS, which is a common limitation users want to work around. FPS interpolation allows:

- Generating fewer frames at lower FPS (faster generation)
- Interpolating to higher FPS for smoother playback
- Potential for 24 FPS or higher output from 16 FPS native generation

> "AFAIK the 16fps thing is hardcoded, I'd love to be wrong but it's my main 'issue' with wan after testing it more all day" — melmass#0, March 4, 2025

## Implementation

### fredbliss FPS Interpolation Nodes

fredbliss developed a set of custom nodes for FPS interpolation with Wan, available at:
https://github.com/fblissjr/ComfyUI-WanVideoWrapper-fps-interpolation

**Key nodes:**
- `WanVideoFPSConfig` — Sets up FPS parameters
- `WanVideoContextOptionsFPS` — Configures timing for context windows
- `WanVideoFPSSampler` — Generates frames at specified FPS
- `WanVideoLatentInterpolator` — Interpolates between generated frames

**Workflow:**
1. Set `generation_fps` (e.g., 2 FPS) — how fast the model generates
2. Set `output_fps` (e.g., 24 FPS) — desired final framerate
3. The system calculates `interpolation_factor` automatically (output_fps / generation_fps)
4. Latent interpolation fills in the missing frames

### Settings

| Parameter | Recommended Value | Notes |
|-----------|------------------|-------|
| **generation_fps** | 2-8 | Lower = faster generation, fewer frames to generate |
| **output_fps** | 16-24 | Final video framerate |
| **interpolation_factor** | Auto-calculated | output_fps / generation_fps (must be ≥1) |
| **motion_smoothness** | 0.5 | Controls interpolation smoothness |
| **interpolation_method** | adaptive / linear / slerp | Adaptive recommended |
| **frame_blending** | Enabled | Helps smooth transitions |

**Important:** If `generation_fps == output_fps`, interpolation factor will be 1 and no interpolation occurs. You must set `output_fps > generation_fps` to enable interpolation.

> "you need to set your output_fps higher than your generation_fps in the FPS Config node" — fredbliss, March 4, 2025

## How It Works

### Generation Phase

1. Model generates frames at `generation_fps` (e.g., 2 FPS = 13 latent frames for 49 pixel frames)
2. This is much faster than generating at full framerate
3. Latents are passed to the interpolator

### Interpolation Phase

1. Interpolator calculates missing frames between generated frames
2. Uses latent-space interpolation (adaptive/linear/slerp methods)
3. Fills in frames to reach `output_fps`
4. Example: 2 FPS → 24 FPS requires 12x interpolation (11 interpolated frames between each generated frame)

### Decoding Phase

1. All frames (generated + interpolated) are decoded by VAE
2. Final video is at `output_fps`

## Performance Impact

**Speed improvements:**
- Generating at 2 FPS with 8x interpolation to 16 FPS: ~2 seconds faster than generating 16 FPS directly
- Lower generation FPS = fewer frames to generate = faster overall time
- Interpolation overhead is minimal compared to generation time

**Example timings (from testing, March 4, 2025):**
- 2 FPS interpolated to 16 FPS: 1m 36s
- 2 FPS without interpolation: 1m 38s
- The interpolation itself adds negligible time

## Interpolation Methods

| Method | Description | Best For |
|--------|-------------|----------|
| **adaptive** | Adjusts interpolation based on motion | General use, recommended |
| **linear** | Simple linear interpolation | Fast motion, simple scenes |
| **slerp** | Spherical linear interpolation | Smooth camera motion, rotations |

## Alternative: LTX Keyframe Interpolation

**Major development (March 5, 2025):** LTX released "any keyframe" support, enabling it to be used as an advanced frame interpolator:

> "since LTX just released any keyframe, you can use it as a very advanced frame interpolator. generate 4fps wan video -> interpolate to 24fps with ltx" — Juampab12, March 5, 2025

**Workflow:**
1. Generate Wan video at low FPS (e.g., 4 FPS)
2. Use LTX keyframe interpolation to fill in frames to 24 FPS
3. LTX provides semantic understanding for better interpolation quality

**Limitations:**
- Still need a way to generate Wan at 4 FPS in the first place
- "we still cant generate 4fps video though" — Juampab12, March 5, 2025
- "that's the part I most wanted remember?" — Juampab12, March 5, 2025

This makes the FPS generation problem (not just interpolation) still relevant for the community.

## Known Issues

### Interpolation Factor = 1

If you see:
```
Using interpolation factor 1 from fps_config
```

This means no interpolation is happening. Check that `output_fps > generation_fps`.

> "🥺 sad face warning: Interpolation factor is 1 or less - no frames will be interpolated. Check that output_fps > generation_fps to enable interpolation" — fredbliss, March 4, 2025

### Jerky Slow Motion

If output video is jerky or slow-motion:
- Check that frame counts match expectations
- Verify interpolation is actually running (check console logs)
- Ensure FPS config is connected to all nodes
- Try different interpolation methods

### Same Video Output Regardless of Settings

If changing interpolation settings produces identical output:
- ComfyUI may be caching results
- Ensure FPS config is connected to FPS sampler
- Check that nodes are executing in correct order
- Restart ComfyUI and refresh browser

### Fast Motion Output

If video plays too fast:
- Check final output FPS in video player
- Verify VHS Combine node (or equivalent) is set to correct FPS
- The FPS set in VHS Combine is just metadata — it won't change generation, only playback speed

> "That's just the output, it won't change anything (Movie will look a bit sped up)" — melmass#0, March 4, 2025

### VAE Issues

fredbliss noted on March 5, 2025 that the VAE may not like temporal consistency modifications:

> "it was interpolating with the alien but it was bad. which would mean the vae just doesnt like us fucking with temporal consistency" — fredbliss, March 5, 2025

> "i'm in over my head once we get to this vae level stuff... i dont have enough experience messing with that side of things" — fredbliss, March 5, 2025

## Alternative Approaches

### Post-Processing Interpolation

Instead of latent interpolation, you can:

1. Generate at 16 FPS (Wan native)
2. Use post-processing interpolation:
   - **RIFE** (Realtime Intermediate Flow Estimation)
   - **FILM VFI** (Frame Interpolation for Large Motion)
   - **GIMM-VFI** (reported as better than FILM by some users)
   - **Topaz Video AI**
   - **Premiere Pro Optical Flow**

> "You might want to try one of comfy's own frame interpolation nodes. Film VFI works pretty good, taking 16 to 24fps" — zelgo_, March 4, 2025

> "for me GIMM-VFI is much better than film though" — melmass#0, March 4, 2025

### Editing Timeline Approach

Some users edit in a 16 FPS timeline and interpolate on export:

> "What I'm trying right now, is to edit some gens in premiere (in a 16fps timeline) and interpolate the whole thing to 25fps on export using OpticalFlow" — melmass#0, March 4, 2025

## Development Status

As of March 5, 2025, fredbliss is reconsidering the FPS interpolation approach:

> "i think im gonna revert back to when i had the alien popping out of the stomach, sync with kijai code, and if i cant get it working from there, starting back with context options fps and ditching the new stuff - then ill call it a failed experiment" — fredbliss, March 5, 2025

> "my goal was to see what from apollo paper worked and didnt. fps sampling alone is what im gonna go after" — fredbliss, March 5, 2025

The focus is shifting back to FPS sampling (generating at lower FPS) rather than interpolation, since LTX can now handle the interpolation part.

## Workflow Example

Basic setup (fredbliss nodes):

1. **FPS Config Node:**
   - generation_fps: 2.0
   - output_fps: 24.0
   - This gives interpolation_factor = 12

2. **Context Options FPS Node:**
   - Connect to FPS Config
   - Set context window parameters

3. **FPS Sampler Node:**
   - Connect FPS Config
   - Connect Context Options
   - Generate at 2 FPS

4. **Latent Interpolator Node:**
   - Connect samples from FPS Sampler
   - Connect FPS Config
   - interpolation_factor: 12 (auto from config)
   - motion_smoothness: 0.5
   - method: adaptive

5. **VAE Decode:**
   - Decode interpolated latents
   - Output: 24 FPS video

## Troubleshooting

| Problem | Solution |
|---------|----------|
| No interpolation happening | Set output_fps > generation_fps in FPS Config |
| Jerky output | Try different interpolation methods; check motion_smoothness |
| Same video regardless of settings | Ensure FPS Config connected to FPS Sampler; restart ComfyUI |
| Fast motion playback | Check VHS Combine FPS setting (metadata only) |
| Instant sampling / no generation | Update ComfyUI to latest version; git pull latest nodes |
| Ghosting artifacts | Lower motion_smoothness; try linear interpolation |
| Timing issues | Verify all FPS values are set correctly across all nodes |
| VAE artifacts | May be fundamental limitation; consider post-processing interpolation instead |

## See Also

- [[wan-2.1]] — Base model with 16 FPS limitation
- [[context-windows]] — For long video generation with FPS interpolation
- [[speed]] — Other speed optimization techniques
- [[comfyui]] — Platform for building FPS interpolation workflows
- [[fps-sampling]] — Related technique for FPS-based sampling

## External Resources

- [fredbliss FPS Interpolation Repository](https://github.com/fblissjr/ComfyUI-WanVideoWrapper-fps-interpolation)
- [FPS User Guide](https://github.com/fblissjr/ComfyUI-WanVideoWrapper/blob/main/wanvideo-fps-guide.md)
- [LTX Keyframe Announcement](https://discord.com/channels/1076117621407223829/1342763350815277067/1346862612496375860) — Any keyframe support for interpolation
