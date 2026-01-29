# Wan Chatter Troubleshooting Guide

*Synthesized from Discord discussions - 2026-01-29*

## Troubleshooting

### mat1 and mat2 error for CLIP loader

**Problem:** CLIP loader only passing clip-l data, getting mat1 and mat2 shape mismatch errors

**Solution:** Reinstall specific versions of transformers and tokenizers

**Details:** Run these commands in your ComfyUI python environment:
```
.\python_embeded\python.exe -m pip uninstall -y transformers tokenizers
.\python_embeded\python.exe -m pip install transformers==4.48.0 tokenizers==0.21.0
```

Alternatively, using dual clip loader may also fix the issue.

*Contributors: Faust-SiN*

### WanSelfAttention normalized_attention_guidance error

**Problem:** Error: 'WanSelfAttention.normalized_attention_guidance() takes from 3 to 4 positional arguments but 8 were given'

**Solution:** Disable the WanVideo Apply NAG node in your workflow

**Details:** This error occurs when using NAG (Normalized Attention Guidance) with incompatible node versions. If the error is coming from the sampler itself, try replacing the node (in case a bad value is cached). Also ensure KJNodes and WanVideoWrapper are up to date.

*Contributors: Nao48, JohnDopamine*

### Sampler V2 preview not showing

**Problem:** Live preview not working on WanVideo Sampler V2 node, though it works on the old sampler

**Solution:** Change the Live Preview Method setting in ComfyUI's settings

**Details:** The preview setting was moved from ComfyUI Manager to ComfyUI's native settings. Click the gear icon on the bottom left, search for 'Preview' and change 'Live Preview Method' to latent2rgb (or your preferred method).

*Contributors: lostintranslation*

### Video colorspace/color shift issues

**Problem:** Color issues when loading videos, colors look different after save/load cycle

**Solution:** Use Load Video (FFmpeg) instead of VHS Load Video for correct colorspace handling

**Details:** Austin Mroz's analysis:
- Video Combine works correctly but may produce videos in colorspaces that loaders don't convert back from
- Load Video (FFmpeg) will convert colorspaces correctly but loads with high bit depth (may have rounding errors)
- VHS Load Video does not support colorspaces and probably can't be fixed
- Native Load Video loads as uint8 with default configuration

*Contributors: Austin Mroz, CaptHook*

### SkyReels V3 reference-to-video compatibility

**Problem:** How to run SkyReels V3 in native ComfyUI

**Solution:** Use the Phantom workflow nodes

**Details:** The reference-to-video model works with Phantom workflows. It should run with the phantom node in both wrapper and native modes.

*Contributors: Kijai*

### Block swap prefetch causing black output

**Problem:** Using WAN wrapper with block swap, setting prefetch higher than 1 causes black output with 'invalid value encountered in cast' warning

**Solution:** Keep prefetch count at 1 when using block swap

**Details:** With non_blocking enabled, prefetch count of 1 works reliably. Higher values (2-3) may give slight speed boost but risk black output. The error appears in videohelpersuite nodes.py:130.

*Contributors: patientx, Kijai*

### Shift values for distilled LoRAs

**Problem:** Unclear what shift value to use with Wan distilled LoRAs at different resolutions

**Solution:** Use shift=5 for Wan distilled LoRAs; increase shift for higher resolutions

**Details:** Distilled LoRAs are trained with shift=5, so that works best. In general, shift depends on resolution - higher resolution needs higher shift because more resolution increases signal at a given noise level. You increase shift to increase noise level which maintains equivalent SNR. FLUX uses resolution-dependent shift automatically, but for other models you need to adjust manually.

*Contributors: spacepxl*

### SAM3 masking VRAM leak

**Problem:** SAM3 masking has an awful VRAM leak when used in workflows

**Solution:** Run SAM3, then disable it, then load the video for the mask

**Details:** The workaround is to split the operation: run the SAM3 masking first, disable the node, then load the video with the mask applied. When it works, SAM3 can mask specific body parts like arms effectively.

*Contributors: mdkb*

### Long video generation approaches

**Problem:** Need to generate long videos with consistent identity/details

**Solution:** Use SVI Pro LoRA instead of context windows

**Details:** SVI Pro (released end of December) lets you chain generations using frames from the previous gen plus the original reference image. Benefits:
- Faster than context windows (no overhead)
- Each segment can be prompted individually
- Works well when camera angle doesn't change much

Caveats:
- Color drift is common (various correction attempts)
- Not as flexible as VACE for planned shots with controlnet

Alternatives: LongCat-avatar (best for single person talking), PainterI2V Long Gen

*Contributors: blake37, Juan Gea, Stef*

### SVI fragility and misalignment

**Problem:** SVI (Semantic Video Interpolation) produces misaligned results

**Solution:** Accept inherent limitations; use default overlap of 5 frames

**Details:** SVI is fragile due to the nature of its training - it was trained using noise generated from errors of a specific generation setup. Default 5-frame overlap works fine. For motion that doesn't translate well over few frames, try more frames but results may vary.

*Contributors: mallardgazellegoosewildcat2, lostintranslation*

### Frontend bug causing node display issues

**Problem:** Nodes not displaying correctly or workflow issues after frontend update

**Solution:** Update to the latest frontend version

**Details:** This was a bug in a recent frontend version that has been resolved. The frontend typically auto-updates on start, but if issues persist check for updates manually.

*Contributors: Kijai*

### SCAIL resolution for distant subjects

**Problem:** SCAIL output is hard to work with for far distance subjects

**Solution:** Use higher resolution or stick to closeups

**Details:** SCAIL works best for closeups and long gens with audio. For distant subjects, it needs more resolution. Also note: SCAIL uses pose image at half resolution, so expect about 50% more VRAM usage compared to similar workflows.

*Contributors: hicho, Kijai*

### Merged LoRA models causing errors

**Problem:** Models merged with LoRAs and their GGUFs giving errors that base models don't

**Solution:** Use base non-modified Wan models, or re-merge LoRAs using ComfyUI's model merge nodes

**Details:** If you're getting errors with merged models that worked before, try merging the LoRAs fresh using ComfyUI's nodes and saving the result. Base Wan models and their GGUFs typically work without these errors.

*Contributors: patientx*

### InfiniteTalk workflow step limit

**Problem:** InfiniteTalk workflow errors when using more than 4 steps without the lightx2v LoRA

**Solution:** Keep steps at 4 or below when using InfiniteTalk, or use with the lightx2v LoRA

**Details:** InfiniteTalk uses extensions looped (not long gen in one go). The workflow is designed for low step counts with the distilled LoRA.

*Contributors: Kijai, avillabon*

## Tips & Tricks

- **Diffusers version doesn't matter much for WanVideoWrapper**
  - Context: The wrapper doesn't really use diffusers beyond some schedulers, so version 0.36 or similar should work fine
  - *From: Kijai*

- **Use VitPose with thickness=20 for animal motion in SCAIL**
  - Context: For getting animals like dogs to run correctly, use SCAIL with just VitPose (not other pose options) and set thickness to 20
  - *From: Kijai, amli*

- **Refresh ComfyUI when nodes don't work on first add**
  - Context: Sometimes new nodes don't work until you refresh the page - this is a known quirk
  - *From: Kijai*

- **2x VAE upscaler available for Wan**
  - Context: spacepxl trained a decoder that acts as a free 2x upscaler, killing noise grid patterns: huggingface.co/spacepxl/Wan2.1-VAE-upscale2x
  - *From: spacepxl*

- **Self-refine feature is on a testing branch**
  - Context: The self-refine capability shown in examples is still in testing/development, not in main wrapper yet
  - *From: JohnDopamine*

- **Video-to-video infinite for extending VACE generations**
  - Context: To extend VACE videos, use two workflows: one for initial video gen, another for video-to-video infinite extension
  - *From: asd*

## FAQ

**Q: Can SkyReels V3 work with native ComfyUI?**

A: Yes, the reference-to-video model works with Phantom workflows in both wrapper and native modes

*Answered by: Kijai*

**Q: Is there a reference face solution for Wan I2V like IP-Adapter?**

A: WanAnimate-like facial injection methods may be added to SCAIL's official version, but nothing currently works like IP-Adapter on base Wan model

*Answered by: teal024 (SCAIL developer)*

**Q: How long can SVI Pro generate?**

A: About 5 seconds per segment, which you can chain together. The model lets you extend by using frames from previous gen plus original reference image

*Answered by: Elvaxorn, blake37*

**Q: What's the difference between wrapper and native nodes?**

A: Make sure you're using the correct sampler/loader - there are separate nodes for Wrapper vs Native workflows. Using the wrong one causes errors.

*Answered by: JohnDopamine*

**Q: Why are preview results grainy after ComfyUI update?**

A: This can be a ComfyUI frontend issue. Check that Live Preview Method is set correctly in ComfyUI settings (not Manager), and try latent2rgb

*Answered by: lostintranslation*
