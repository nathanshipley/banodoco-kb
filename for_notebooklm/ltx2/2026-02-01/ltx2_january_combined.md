# LTX Video 2 Knowledge Base - January 2026

This document contains extracted knowledge from Banodoco Discord discussions about LTX Video 2 (released January 5, 2026).

**Coverage:** January 6-31, 2026
**Channels:** ltx_chatter, ltx_training, ltx_gens, ltx_resources
**Total messages processed:** ~44,500
**Extraction date:** February 1, 2026

---


# LTX Chatter - January 6, 2026

# Ltx Chatter Knowledge Base
*Extracted from Discord discussions: 2026-01-06 to 2026-01-07*


## Technical Discoveries

- **LTX Video 2 has built-in VAE and audio processing merged into single model**
  - 27GB fp8 model includes video (19B params), audio processing, and VAE all in one file
  - *From: Ada*

- **Model supports multiple input modes**
  - Text-to-video, image-to-video, video-to-video, and audio-to-video generation capabilities
  - *From: l҈u҈c҈i҈f҈e҈r҈*

- **Distilled version available as LoRA**
  - ltx-2-19b-distilled-lora-384.safetensors allows using base model with distilled speeds
  - *From: Ada*

- **Built-in upscaling capabilities**
  - Upscales latents from 512 to 1024 / 720 to 1440, includes spatial and temporal upscalers
  - *From: Ada*

- **Audio continuation maintains voice consistency**
  - Can take audio from video input and continue generating with same voice characteristics
  - *From: harelcain*

- **LTX Video 2 supports resolutions up to 4K**
  - Official info mentions 4K support, though some users experienced issues at 1920x1088
  - *From: sometimesTwitchy*

- **Model requires resolutions divisible by 32**
  - Minimum resolution can go as low as 352x256 or 320x320
  - *From: harelcain*

- **Audio is spatially aware**
  - Audio changes based on position - footsteps get louder as character approaches camera
  - *From: Lodis*

- **Generation times are very fast**
  - 18 seconds for short clips, 117 seconds for 10 second video on 5090
  - *From: Shubhooooo*

- **Live preview causes sampling errors**
  - Disabling live preview in ComfyUI fixes sampler errors that prevent generation
  - *From: Cubey*

- **5090 can run LTX Video 2 at high resolutions**
  - 832x480, 241 frames using fp8 model + distill lora at 0.6 weight works on 5090
  - *From: CrypticWit*

- **LTX2 generates audio and video separately then combines in latent space**
  - This architecture suggests possibility of feeding in custom audio instead of generated audio
  - *From: dj47*

- **Model supports up to 4K native generation**
  - Can do 4K 30fps for 20 seconds, though still has some blurriness issues
  - *From: Clint Hardwood*

- **Portrait orientation doesn't work well**
  - Portrait aspect ratios appear to cause issues with generation quality and motion
  - *From: Cubey*

- **832x480 resolution produces poor results with no motion**
  - Most results had no motion, and all outputs didn't look very good at this resolution
  - *From: Cubey*

- **Model wasn't trained on many anime**
  - The dataset is mainly cinematic landscape videos
  - *From: dj47*

- **Model can generate accents based on visual context**
  - Generated Indian accent when Indian doctors appeared in video without being prompted for accent
  - *From: Tachyon*

- **LTX-2 has much better dynamic motion than other models**
  - The amount of dynamic motion in the same 5 seconds LTX can handle compared to Wan is mind blowing
  - *From: dj47*

- **Model breaks down at longer durations**
  - Out of distribution breakdown at 30 seconds, probably best to keep it to 20 seconds
  - *From: sometimesTwitchy*

- **Model has some NSFW training content**
  - Can confirm its been trained on some anime nsfw
  - *From: Tachyon*

- **Generating text is not LTX-2's forte**
  - Model struggles with proper looking text generation
  - *From: harelcain*

- **LTX Video 2 supports multiple languages including Hindi, Russian, and Chinese**
  - Users successfully tested audio generation in Hindi, Russian, and Chinese languages
  - *From: Govind Singh*

- **Model has significant temporal consistency issues**
  - Model struggles with complex motion like gymnastics where anatomy breaks down during flips
  - *From: dj47*

- **Euler_A scheduler performs better for anime/art content than default Euler**
  - Better animation quality observed when using Euler_A for anime/art style content
  - *From: Clint Hardwood*

- **Model has built-in temporal upscaler capability**
  - Can achieve effective double frame rate using temporal latent upscaler to reduce deformations
  - *From: harelcain*

- **Prompt is stronger than LoRA influence**
  - Camera movement prompts override static camera LoRA settings
  - *From: burgstall*

- **LTX Video 2 includes depth information in decoded latents**
  - The depth is included in the decoded latent output
  - *From: Kijai*

- **Model has very fast generation speed**
  - Can achieve realtime generation speed due to high compression VAE
  - *From: yi*

- **Higher quality and faster than Wan 2.2**
  - LTX2 using full pagefile is still faster than wan2.2, has higher fidelity and better audio
  - *From: boop*

- **Model can run on as low as 5GB VRAM with sufficient RAM**
  - Successfully tested with --reserve-vram 20, requires enough system RAM for offloading
  - *From: Kijai*

- **LTX Video 2 can run on 8GB VRAM**
  - Works with 64GB RAM using offloading, confirmed by multiple users
  - *From: Kijai*

- **Generation is extremely fast with distilled model**
  - 121 frames at 720p generates in ~6 seconds on RTX 4090, almost realtime
  - *From: Kijai*

- **VAE compresses 8 frames to 1 latent frame**
  - 16 latents decode to 121 pixel frames, first frame is single latent
  - *From: Dragonyte*

- **Model supports up to 10s official duration**
  - Some users report 20s works, 361 frames tested successfully
  - *From: mamad8*

- **I2V works better at higher resolutions**
  - 1280x720 works well, below that tends to perform poorly
  - *From: Tachyon*

- **LTX Video 2 supports 24 fps output with audio**
  - Model outputs 24 fps video with integrated audio generation
  - *From: Tachyon*

- **LTX-1 LoRAs work with LTX-2**
  - Existing LTX-1 LoRAs are compatible and functional with the new model
  - *From: Fill*

- **Model has excellent physics understanding**
  - Drifting physics work well - historically difficult for video models
  - *From: Fill*

- **FP4 version available in Lightricks repo**
  - Ultra-compressed FP4 model variant exists for extreme memory efficiency
  - *From: D'Squarius Green, Jr.*

- **Two-stage generation process**
  - First stage generates at quarter resolution, second stage upscales with partial denoise
  - *From: harelcain*

- **Model can continue videos with audio continuation**
  - By encoding video and audio as latent and using as input, can extend videos and clone voices
  - *From: protector131090*

- **LTX-1 LoRAs are compatible with LTX-2**
  - Previous LTX-1 LoRAs work on the new model, providing backwards compatibility
  - *From: Fill/NebSH*

- **FP8 and distilled models have minimal quality difference**
  - No significant difference observed between full model and FP8 version for most use cases
  - *From: seitanism*

- **Model supports multilingual audio generation**
  - Successfully generates speech in Hindi, Dutch, French and other languages beyond English
  - *From: Tachyon/wouter/mamad8*

- **Latent tensor size calculation affects quality**
  - Formula: (w/32)*(h/32)*((f-1)/8+1) should be <20k, preferably <15k. Values like 144k cause artifacts
  - *From: harelcain*

- **Custom audio input is possible**
  - Can use conditioning masks to input custom audio files for lip sync generation
  - *From: LTX Lux*

- **Temporal inpainting capabilities**
  - Model can do audio-guided video continuation/inpainting as demonstrated with Mariah Carey example
  - *From: harelcain*

- **Mask value of 0.4 and above allows image movement in I2V**
  - Setting mask value to 0.34 or higher enables motion in image-to-video generation
  - *From: Kijai*

- **LTX-2 can generate up to 50 seconds of coherent video**
  - Successfully generated 50 second videos, much longer than the official 20 second limit
  - *From: avataraim*

- **LTX-2 supports multi-character voice assignment**
  - The model can assign different voices to different characters in the same scene based on prompts
  - *From: Mazrael.Shib*

- **Adding noise to latent helps with I2V motion**
  - Using added noise with 0.8 mask produces better movement than without
  - *From: Kijai*

- **FP4 model is 33% faster than FP8 on RTX 50xx series**
  - Performance improvement specifically on Blackwell architecture GPUs
  - *From: pagan*

- **480p uses more RAM than 720p**
  - User hit OOM error at 480p but 720p worked fine
  - *From: Kiwv*

- **Model adds microphones and headphones automatically for singing audio**
  - Even without prompting, the AI instinctively adds mic/headphones when audio sounds like singing
  - *From: Kijai*

- **Noise amount is most important factor for audio+image to video**
  - After testing audio+image to video workflow, noise amount has the biggest impact on results
  - *From: Kijai*

- **Can extend videos using I2V with more start frames**
  - Temporal extension works by using I2V but with more start frames, same as classic extension technique
  - *From: Kijai*


## Troubleshooting & Solutions

- **Problem:** ModuleNotFoundError for audio_vae
  - **Solution:** Update ComfyUI to nightly version and restart
  - *From: Tachyon*

- **Problem:** Missing tokenizer.model file
  - **Solution:** Download text encoder from Comfy-Org/ltx-2 split_files/text_encoders
  - *From: JohnDopamine*

- **Problem:** Custom nodes not working
  - **Solution:** Git pull in ComfyUI-LTXVideo folder and restart ComfyUI
  - *From: crinklypaper*

- **Problem:** ComfyUI requires Python 3.10+
  - **Solution:** Upgrade from Python 3.9 to 3.10 minimum
  - *From: Vardogr*

- **Problem:** ModuleNotFoundError: No module named 'comfy.ldm.lightricks.vae.audio_vae'
  - **Solution:** Update ComfyUI to latest version using git pull, use nightly build
  - *From: Ada*

- **Problem:** mat1 and mat2 shapes cannot be multiplied error
  - **Solution:** Disable live preview in ComfyUI settings - change 'Live preview method' to None
  - *From: KevenG*

- **Problem:** Custom LTX nodes won't install due to fairscale
  - **Solution:** Update to ComfyUI nightly build and force git pull
  - *From: l҈u҈c҈i҈f҈e҈r҈*

- **Problem:** fp8 and fp4 support unavailable error
  - **Solution:** pip install comfy-kitchen in your environment
  - *From: CrypticWit*

- **Problem:** AttributeError: 'NoneType' object has no attribute 'Params'
  - **Solution:** Uninstall xformers - it's deprecated and causes conflicts
  - *From: Clint Hardwood*

- **Problem:** Text encoder file structure issues
  - **Solution:** Put encoder in its own folder and rename file to model.safetensors
  - *From: crinklypaper*

- **Problem:** Workflow stalling with 'NoneType' object has no attribute 'Params'
  - **Solution:** Install comfy-kitchen in the python environment
  - *From: CrypticWit*

- **Problem:** OOM during audio decoding
  - **Solution:** Add clear VRAM call before final audio decode step
  - *From: CrypticWit*

- **Problem:** Enhanced prompt node causing errors
  - **Solution:** Disable the enhanced prompt node to avoid crashes
  - *From: CrypticWit*

- **Problem:** Sampler error with resolution dimensions
  - **Solution:** Ensure dimensions are multiples of 32
  - *From: Vardogr*

- **Problem:** GGUF models not loading with 'Unexpected text model architecture type: gemma3'
  - **Solution:** ComfyUI-gguf needs update to support Gemma3 architecture
  - *From: Vardogr*

- **Problem:** Need to use single Gemma file instead of splits
  - **Solution:** Use the 24GB single file and rename to model.safetensors, place in text_encoders folder
  - *From: crinklypaper*

- **Problem:** Workflow gets stuck on Gemma node without error
  - **Solution:** Use Shubhoo's workflow from ComfyUI templates instead of official example workflows
  - *From: JohnDopamine*

- **Problem:** ComfyUI crashes with high resolution/frame count
  - **Solution:** Reduce resolution or frame count - 1280x720x242 frames works, higher resolutions cause crashes
  - *From: Tachyon*

- **Problem:** Need to disable enhance node to get workflows working
  - **Solution:** Disable the 'Enhance' node in the workflow
  - *From: CrypticWit*

- **Problem:** ComfyUI crashes when trying higher resolutions
  - **Solution:** Disable video preview to prevent crashes
  - *From: Tachyon*

- **Problem:** Getting wall of text errors about Gemma
  - **Solution:** Wall of text is fine and can be ignored - model still works
  - *From: Tachyon*

- **Problem:** Bundled example workflows are outdated
  - **Solution:** Update ComfyUI workflow templates with: pip install --upgrade comfyui-workflow-templates
  - *From: JohnDopamine*

- **Problem:** mat1 and mat2 shapes cannot be multiplied error
  - **Solution:** Disable live previews in ComfyUI settings (Execution > Live preview method: none)
  - *From: Zabo*

- **Problem:** LTXVGemmaCLIPModelLoader node missing
  - **Solution:** Install ComfyUI-LTXVideo custom nodes using ComfyUI Manager
  - *From: 1248225653124239392*

- **Problem:** Header too large error with Gemma model
  - **Solution:** Use git lfs install before cloning or use hf download command
  - *From: CrypticWit*

- **Problem:** 'NoneType' object has no attribute 'Params' error
  - **Solution:** Install comfy-kitchen package with 'pip install comfy-kitchen' in ComfyUI venv
  - *From: patientx*

- **Problem:** Prompt enhancer chat template error
  - **Solution:** Disable the prompt enhancer node
  - *From: seitanism*

- **Problem:** Memory leak with repeated generations
  - **Solution:** Restart ComfyUI between generations or manually unload models
  - *From: Zabo*

- **Problem:** RuntimeError: input tensor must fit into 32-bit index math
  - **Solution:** Use frame counts divisible by specific intervals (241, 361 frames instead of 242, 363)
  - *From: seitanism*

- **Problem:** Expected all tensors to be on the same device error
  - **Solution:** Use --reserve-vram flag for memory management with fp8 models
  - *From: Kijai*

- **Problem:** Expected all tensors to be on the same device error
  - **Solution:** Disable live preview in ComfyUI settings
  - *From: Kijai*

- **Problem:** Audio embeddings connector device assignment issue
  - **Solution:** Apply Kijai's code fix for device assignment
  - *From: Kijai*

- **Problem:** OOM errors on generation
  - **Solution:** Use --reserve-vram parameter with higher values (2-20 depending on setup)
  - *From: Kijai*

- **Problem:** System freezing at 99% VRAM
  - **Solution:** Increase --reserve-vram value and use --cache-none parameter
  - *From: Kijai*

- **Problem:** Prompt enhancer chat template error
  - **Solution:** Git clone gemma model to models/text_encoder directory
  - *From: burgstall*

- **Problem:** ComfyUI crashing without errors
  - **Solution:** Try --cache-none parameter and increase reserve-vram
  - *From: Kijai*

- **Problem:** OOM errors on lower VRAM systems
  - **Solution:** Add --reserve-vram 5 launch flag and modify embeddings_connector line in code
  - *From: crinklypaper*

- **Problem:** CLIPTextEncode device mismatch error
  - **Solution:** Make sure code modification was done correctly and restart ComfyUI
  - *From: Kijai*

- **Problem:** Tensor size mismatch in KSampler
  - **Solution:** Use LTXVCropGuides node to remove context latent after sampling
  - *From: mkupchik_lightricks*

- **Problem:** VAE decode crashes on high resolution
  - **Solution:** Use tiled VAE decode instead of regular decode
  - *From: orabazes*

- **Problem:** Prompt enhancer tokenizer errors
  - **Solution:** Check Gemma setup and transformers version
  - *From: LTX Lux*

- **Problem:** ComfyUI crashes without error
  - **Solution:** Enable system-managed swap file, usually RAM exhaustion issue
  - *From: seitanism*

- **Problem:** I2V produces static images or wrong scenery
  - **Solution:** Use prompt enhancer and ensure proper resolution (1280x720+)
  - *From: burgstall*

- **Problem:** Out of memory errors on high VRAM systems
  - **Solution:** Use --reserve-vram flag (values 4-10 depending on resolution)
  - *From: Kijai*

- **Problem:** Page file/swap causing disk writes
  - **Solution:** Use --cache-none flag to avoid excessive disk writes
  - *From: Mngbg*

- **Problem:** Size tensor mismatch at sampling
  - **Solution:** Delete model-0001 safetensors files, keep only the downloaded model from Comfy-Org repo
  - *From: Tachyon*

- **Problem:** ValueError: Cannot use chat template functions
  - **Solution:** Disable enhancer or use workflows from blog.comfy.org instead of examples folder
  - *From: seitanism*

- **Problem:** Random static output from workflows
  - **Solution:** Use official workflows from blog.comfy.org rather than included examples folder
  - *From: Tachyon*

- **Problem:** WSL2 memory management issues
  - **Solution:** Run on native Linux for better RAM/VRAM management - WSL2 has bugged memory cleaning
  - *From: seitanism*

- **Problem:** FP4 weights extremely slow performance
  - **Solution:** Use FP8 instead - FP4 takes 12.24s/it vs FP8 at 1.13s/it
  - *From: D'Squarius Green, Jr.*

- **Problem:** OOM errors during upscale sampler
  - **Solution:** Increase --reserve-vram value incrementally (try 4, 6, etc.)
  - *From: fearnworks/Vardogr*

- **Problem:** Gemma text encoder device mismatch errors
  - **Solution:** Run text encoder on CPU or use separate ComfyUI portable install
  - *From: Lodis/Tachyon*

- **Problem:** Save video node failing with NaN/Inf audio errors
  - **Solution:** Use 'get video components' node with VHS video combine node instead
  - *From: seitanism*

- **Problem:** res_2s sampler not found error
  - **Solution:** Install clownshark res4lyf nodes or switch to euler_ancestral sampler
  - *From: seitanism*

- **Problem:** CUDA invalid argument error
  - **Solution:** Usually indicates OOM - increase reserve VRAM
  - *From: TK_999*

- **Problem:** Preview-related crashes
  - **Solution:** Turn off all video previews in settings and use --preview-method none flag
  - *From: MOV/JohnDopamine*

- **Problem:** Live previews cause crashes with LTX-2
  - **Solution:** Turn off live previews in ComfyUI menu
  - *From: seitanism*

- **Problem:** I2V ignores input image when masking video
  - **Solution:** Fully mask audio, then mask first video frames using latent noise mask
  - *From: Kijai*

- **Problem:** Audio workflow causes BSOD when loading Gemma
  - **Solution:** Switch to native T2V workflow instead of audio workflow
  - *From: boop*

- **Problem:** Gemma text encoder missing files error
  - **Solution:** Place tokenizer and json files next to safetensors model in text_encoder folder root
  - *From: naomikenkorem*

- **Problem:** Preprocess noise node accumulates between queues
  - **Solution:** Clear memory and restart ComfyUI between runs
  - *From: Kijai*

- **Problem:** FP4 model runs slower than FP8 on RTX 5090
  - **Solution:** Use FP8 model instead, FP4 optimization may need fixes
  - *From: Kijai*

- **Problem:** ComfyUI crashes when loading CLIP
  - **Solution:** Use single file from Comfy-Org repository or update ComfyUI
  - *From: Moonbow*

- **Problem:** FileNotFoundError: No files matching pattern 'tokenizer.model' found
  - **Solution:** Download the other non-model files from the original gemma repo or restart ComfyUI and reload browser
  - *From: Lodis*

- **Problem:** Single file model not working
  - **Solution:** You're missing another file from the original repo
  - *From: Lodis*

- **Problem:** VAE decode bottleneck using 99% VRAM on RTX 3090
  - **Solution:** Use tiled decode node
  - *From: Piblarg*

- **Problem:** FP8 dev model produces blurry blotchy results
  - **Solution:** Ask someone to share working workflow, may be setup issue
  - *From: Lodis*


## Model Comparisons

- **LTX 2 vs WAN 2.2 training**
  - LTX 2 easier to train - single model system vs WAN's problematic dual model approach
  - *From: Ada*

- **LTX 2 vs WAN 2.2 size**
  - LTX 2 roughly half the size of WAN 2.2, includes audio processing
  - *From: Ada*

- **Distilled vs non-distilled models**
  - Non-distilled required for LoRA training, distilled better for inference speed
  - *From: Kiwv*

- **LTX Video 2 vs Wan 2.2**
  - LTX Video 2 has Wan 2.2 quality but with audio support
  - *From: Kiwv*

- **Distilled vs Full model quality**
  - Full model was 'a lot worse even at 50 steps' compared to distilled
  - *From: Clint Hardwood*

- **fp8 vs fp4 quality**
  - Audio quality drops with fp8, visual quality drops with fp4
  - *From: CrypticWit*

- **LTX2 vs WAN 2.2**
  - LTX2 makes WAN content look primitive, much more advanced quality
  - *From: dj47*

- **Distilled vs Dev model**
  - Distilled is better by like 10 times performance
  - *From: Clint Hardwood*

- **LTX2 vs Sora2**
  - Similar artifact patterns, approaching Sora2 quality with potential to match via training
  - *From: yi*

- **LTX-2 vs Wan/Kadinsky**
  - LTX looks way better than wan or kadinsky
  - *From: dj47*

- **LTX vs Veo3**
  - LTX looks more natural than Veo3
  - *From: dj47*

- **I2V vs T2V performance**
  - I2V produces better results than T2V for same prompts, T2V is faster
  - *From: burgstall*

- **LTX 2 vs LTX 0.98**
  - Big upgrade from 0.98 but still feels somewhat janky
  - *From: Zabo*

- **LTX2 vs Wan 2.2**
  - LTX2 is faster, higher quality, and has better audio that beats some cloud models
  - *From: Ada*

- **GGUF vs pagefile for large models**
  - GGUF is faster than pagefile, pagefile on NVME is very slow
  - *From: Kijai*

- **Distilled vs Base model**
  - Base model gives higher quality output and better prompt adherence, distilled is faster
  - *From: Salama*

- **LTX-2 vs previous versions**
  - Much better motion quality, improved lip sync capabilities
  - *From: harelcain*

- **LTX-2 vs WAN speed**
  - LTX-2 is much faster than WAN
  - *From: yi*

- **LTX-2 vs Sora features**
  - First open source audio-video model like Sora
  - *From: Lodis*

- **Native Linux vs WSL2 performance**
  - Native Linux uses less RAM (64GB sufficient vs 96GB+ needed in WSL2)
  - *From: Kijai*

- **LTX-2 vs Wan speed**
  - LTX-2 significantly faster - 'blows Wan out the water in terms of speed'
  - *From: David Snow*

- **FP8 vs distilled models**
  - Both work well, distilled may be slightly faster for same quality
  - *From: seitanism*

- **Full weights vs FP8**
  - No significant quality difference observed in most cases
  - *From: seitanism*

- **FP8 dev vs distilled model quality**
  - Distilled model produces much better output than FP8 dev model
  - *From: ucren*

- **With vs without upscaling for I2V**
  - Generating without upscaling can be faster due to VRAM offloading
  - *From: MOV*

- **LTX nodes vs ComfyUI native workflow**
  - If one doesn't work, try the other - compatibility varies
  - *From: JohnDopamine*

- **LTX vs other models for 50s coherency**
  - Much better than other model stitching, not amazing but still better
  - *From: Moonbow*

- **Quality assessment**
  - Feels like Sora at home, pretty amazing quality
  - *From: Parker*


## Tips & Best Practices

- **Use fp8 instead of GGUFs**
  - Context: GGUFs are slower than offloading for modern video models
  - *From: Ada*

- **Use base model for LoRA training**
  - Context: Distilled models make LoRA training very difficult
  - *From: Kiwv*

- **Download distilled LoRA for speed**
  - Context: Can train on base then apply distilled LoRA for faster inference
  - *From: Ada*

- **Prepare 25fps datasets**
  - Context: LTX 2 requires 25fps format, need to rebuild existing datasets
  - *From: Ada*

- **Turn off node previews if you have VHS installed**
  - Context: VHS node previews don't work correctly with LTX Video 2
  - *From: CrypticWit*

- **Use euler simple or ddpm 2 karras samplers**
  - Context: These are safe sampler combinations for LTX Video 2
  - *From: Kiwv*

- **Skip upsampling stage to get 960x540 resolution**
  - Context: For users with lower VRAM who want to avoid memory issues
  - *From: naomikenkorem*

- **Use official prompting guide for best results**
  - Context: Model trained mainly on HD content, following guide improves output quality
  - *From: Lodis*

- **Use free RAM/VRAM nodes between steps**
  - Context: Helps manage memory usage in ComfyUI workflows
  - *From: Lodis*

- **Text encoder can run on CPU**
  - Context: Helps reduce VRAM requirements during generation
  - *From: Lodis*

- **Switch to tiled VAE for memory issues**
  - Context: Helps with VRAM limitations on lower-end cards
  - *From: Cubey*

- **Use long, detailed prompts similar to Chroma**
  - Context: Model likes long prompts and responds well to detailed descriptions of what the camera sees
  - *From: Tachyon*

- **Use Gemini to enhance prompts**
  - Context: Create a Gemini gem with LTX prompting instructions to improve short prompts into longer, better ones
  - *From: burgstall*

- **Lower image adherence for better compliance**
  - Context: When using image-to-video, lower the image adherence to make it more compliant
  - *From: Clint Hardwood*

- **Use res_2s sampler with cfg > 1 and 20+ step LTXV schedule for better quality**
  - Context: When using higher step counts for improved results
  - *From: harelcain*

- **Generate at higher base resolution to help with anatomy issues**
  - Context: When dealing with complex motion and anatomy problems
  - *From: Benjimon*

- **Push LoRA weight above 1.0 to overcome prompt dominance**
  - Context: When LoRA effects are being overridden by prompt instructions
  - *From: harelcain*

- **Everything must be divisible by 64**
  - Context: For proper model functioning
  - *From: Benjimon*

- **Use temporal latent upscaler to reduce motion deformations**
  - Context: When experiencing motion artifacts in complex scenes
  - *From: harelcain*

- **Prompt every motion explicitly for best results**
  - Context: Model requires detailed motion prompting or generates minimal movement
  - *From: seitanism*

- **Use VRAM cleaner node before ksampler**
  - Context: When experiencing VRAM issues
  - *From: hicho*

- **Set pagefile on separate NVME drive from system**
  - Context: To avoid system freezing during generation
  - *From: hicho*

- **Use fp8 gemma for memory savings**
  - Context: When running on lower VRAM setups
  - *From: yi*

- **Use --cache-none launch flag for RAM management**
  - Context: When running low on RAM or want to unload models
  - *From: Kijai*

- **Use ComfyUI template workflows instead of repo examples**
  - Context: Repo examples may have issues, templates are more reliable
  - *From: JohnDopamine*

- **Start conservative with 832x480 resolution**
  - Context: For initial testing and stability
  - *From: LTX Lux*

- **Write out numbers as words in prompts**
  - Context: Write 'fifty pounds' instead of '£50' for better results
  - *From: harelcain*

- **Use split sampling for controlnet-like behavior**
  - Context: Stop conditioning after first X steps to control IC-LoRA strength
  - *From: harelcain*

- **Enable system-managed swap file**
  - Context: Prevents crashes from RAM exhaustion
  - *From: seitanism*

- **Use long detailed prompts for better results**
  - Context: Better prompting leads to better output quality
  - *From: harelcain*

- **Prompt the whole movement sequence**
  - Context: Include complete motion description rather than partial movements
  - *From: Kijai*

- **Set FPS to 40 for fast motion prompts**
  - Context: When prompting for fast motion scenes
  - *From: hicho*

- **Use LLM to enhance prompts**
  - Context: Feed prompts to ChatGPT or other LLMs for improvement
  - *From: Tachyon*

- **Different LoRA strengths control distillation level**
  - Context: Gives degrees of freedom and saves disk space
  - *From: harelcain*

- **Use multi-scale approach for higher resolutions**
  - Context: Start with smaller base tile (720x720) then upscale in stages to avoid artifacts
  - *From: harelcain*

- **Detailed prompting essential for good results**
  - Context: Model has excellent prompt adherence but requires detailed descriptions
  - *From: seitanism*

- **Reserve VRAM incrementally**
  - Context: Start with small values like 2, increase by 2 until stable
  - *From: Lodis*

- **Disable smart memory for stability**
  - Context: Can cause unexpected behavior during generation
  - *From: Lodis*

- **Low sigma values safe for second stage**
  - Context: Second stage just adds detail, hard to go wrong with low sigma levels
  - *From: harelcain*

- **Use simple prompts and layer instructions gradually**
  - Context: Complex prompts with many actions/characters may not render properly
  - *From: seitanism*

- **Use temporal upscaler for fast motion situations**
  - Context: When generating scenes with rapid movement
  - *From: dj47*

- **Separate and refine audio in post-processing**
  - Context: For better audio quality after generation
  - *From: Gleb Tretyak*

- **Use res_2s sampler instead of euler_ancestral**
  - Context: LTX workflow uses different sampler than ComfyUI default
  - *From: seitanism*

- **Use compression/blur to induce more motion**
  - Context: LTX-2 still benefits from these techniques for better movement
  - *From: Dragonyte*

- **Use vocals-only audio for cleaner lipsync**
  - *From: Kijai*

- **Use JSON prompting format**
  - Context: Since the model is based on Gemma
  - *From: Moonbow*

- **Create prompt template with location, character, motion, action, lighting**
  - Context: For consistent prompting results, copy paste and modify as needed
  - *From: Lodis*

- **Put unwanted elements in negative prompt**
  - Context: When model keeps adding unwanted elements like microphones
  - *From: Lodis*

- **Use GPT to create automatic scene prompts**
  - Context: For generating multiple scenes efficiently
  - *From: avataraim*

- **Balance between keeping reference and audio sync**
  - Context: When using audio to video generation
  - *From: Kijai*


## News & Updates

- **LTX Video 2 released with NVIDIA partnership**
  - 19B parameter model with audio support, synchronized with NVIDIA CES announcement
  - *From: LTX Lux*

- **ComfyUI native support added**
  - LTX 2 templates now available in ComfyUI nightly builds
  - *From: yi*

- **Control LoRAs coming soon**
  - Canny, Depth, Detailer, Pose Control, and camera control LoRAs listed in readme
  - *From: Vardogr*

- **LTX Video 2 released with LoRA support**
  - Model comes with camera control LoRAs like Dolly Left, supports up to 20s at 25fps via API
  - *From: NebSH*

- **ComfyUI native workflow available**
  - Native ComfyUI workflow doesn't require custom nodes, available in workflow templates
  - *From: yi*

- **Workflows being fixed in real-time**
  - Some workflows have wrong model links embedded and are being updated as issues are discovered
  - *From: Dragonyte*

- **LTX2 trainer released**
  - Standalone Python package available supporting LoRA and full fine-tuning
  - *From: naomikenkorem*

- **Distilled fp8 model available**
  - More efficient version released at https://huggingface.co/Lightricks/LTX-2/blob/main/ltx-2-19b-distilled-fp8.safetensors
  - *From: mkupchik_lightricks*

- **Low VRAM solutions in development**
  - Team already has solution path but couldn't make it for initial release
  - *From: Dragonyte*

- **Audio fix is forthcoming**
  - LTX team is working on fixing audio quality issues
  - *From: Lodis*

- **Audio controlnet feature planned**
  - They will have audio controlnet functionality coming later
  - *From: dj47*

- **Separate Discord channel created for better organization**
  - Created dedicated channel to make it easier for people to read discussions
  - *From: NebSH*

- **LTX Video 2 released with audio support**
  - Supports text-to-video and image-to-video generation with audio, released January 5, 2026
  - *From: harelcain*

- **Retake feature available on API**
  - Video editing/extension feature available on LTX playground and fal.ai
  - *From: harelcain*

- **Multiple training options available**
  - Standard LoRA Training, Audio-Video LoRA Training, Full Model Fine-tuning, In-Context LoRA Training
  - *From: NebSH*

- **Spatio-temporal tiles support coming soon**
  - Will enable progressive scaling to 60/120fps and 4K generation
  - *From: Zeev Farbman*

- **Memory/offloading optimizations being worked on for ComfyUI**
  - Will solve many current memory issues when implemented
  - *From: Kijai*

- **Video Helper Suite animated previews don't work with LTX2 yet**
  - No latent RGB factors available for the model
  - *From: Kijai*

- **Tech report for LTX Video 2 coming within 48 hours**
  - Will provide detailed technical information about the model
  - *From: LTX Lux*

- **FP8 quantized Gemma available**
  - 13GB version available on HuggingFace by GitMylo
  - *From: yi*

- **No plans for 9B and 2B versions**
  - LTX team confirmed no smaller model variants planned
  - *From: harelcain*

- **LTX Video 2 released January 5, 2026**
  - Open source audio-video generation model with text-to-video and image-to-video capabilities
  - *From: community*

- **No plans to change license to OSI**
  - License similar to Llama, commercial use allowed under $10M revenue
  - *From: LTX Lux*

- **Delay from 2025 to January 2026 was worth it**
  - Extra development time made significant difference in quality
  - *From: LTX Lux*

- **LTX-2 training descendant of earlier models**
  - Explains why LTX-1 LoRAs work with new model
  - *From: harelcain*

- **ComfyUI needs patches for proper offloading**
  - Current version doesn't properly offload LTX-2, --reserve-vram is workaround
  - *From: seitanism*

- **ComfyUI fixed learnable_registers bug**
  - No longer need to manually edit files, revert edits if update fails
  - *From: Kijai*

- **Training support being worked on in Musubi tuner**
  - LoRA training implementation in development
  - *From: Lodis*

- **Team is in night time, slow response expected**
  - Official team response time will be slow during night hours
  - *From: LTX Lux*

- **Things were fixed overnight**
  - Issues from previous night were resolved
  - *From: Kagi*


## Workflows & Use Cases

- **Vid2vid with partial latent masking**
  - Use case: Modifying existing video content while maintaining consistency
  - *From: harelcain*

- **Two-stage generation pipeline**
  - Use case: Text-to-video with spatial and temporal upscaling
  - *From: Benjimon*

- **Two-stage production pipeline**
  - Use case: High quality video generation with upscaling, used for 1536x2304x481 frames
  - *From: sometimesTwitchy*

- **Native ComfyUI workflow without custom nodes**
  - Use case: Standard workflow using built-in ComfyUI nodes, all functionality in subgraphs
  - *From: yi*

- **Use ltxv low VRAM nodes for memory-constrained setups**
  - Use case: Running on GPUs with limited VRAM
  - *From: Ada*

- **Multiscale generation for high resolution**
  - Use case: Proper way to achieve very high resolutions by upscaling progressively
  - *From: harelcain*

- **Shubhoo's T2V workflow with upscaling**
  - Use case: 20 steps for initial generation, then 3 steps for upscale
  - *From: Shubhoo*

- **Full fp8 T2V workflow from LTX repo**
  - Use case: Using LTX-2_T2V_Full_wLora.json for text-to-video generation
  - *From: burgstall*

- **Using native ComfyUI workflows instead of custom nodes**
  - Use case: Better compatibility and fewer dependency issues
  - *From: Clint Hardwood*

- **Custom GUI with proper offloading for 16GB GPUs**
  - Use case: Running full model on limited VRAM with system RAM offloading
  - *From: Benjimon*

- **Progressive upscaling with temporal and spatial passes**
  - Use case: Moving from base generation to 4K 60/120fps
  - *From: Zeev Farbman*

- **Using Flux 2 for I2V first frame generation**
  - Use case: Creating consistent starting frames for image-to-video
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Text-to-video with audio generation**
  - Use case: Creating videos from text prompts with synchronized audio
  - *From: multiple users*

- **Image-to-video with controlnet guidance**
  - Use case: Animating static images with depth/canny control
  - *From: harelcain*

- **Video extension using masking**
  - Use case: Extending videos by masking portions with LTXVMaskByTime node
  - *From: harelcain*

- **Two-stage generation with upscaling**
  - Use case: Generate video at low res first, then upscale with partial denoise for final resolution
  - *From: harelcain*

- **Video extension using MaskByTime**
  - Use case: Set latent masks correctly with MaskByTime node to continue existing videos
  - *From: harelcain*

- **I2V setup for controlled generation**
  - Use case: Use LTXVPreprocess node to process conditioning image for image-to-video
  - *From: harelcain*

- **Multi-stage upscaling approach**
  - Use case: High resolution generation without artifacts - 720x720 base, then 1440x1440, then 2880x2880
  - *From: seitanism/harelcain*

- **Audio conditioning with masks**
  - Use case: Custom audio input using LTXV Set Audio Video Mask By Time node
  - *From: LTX Lux*

- **Temporal inpainting setup**
  - Use case: Audio-guided video continuation and lip sync replacement
  - *From: harelcain*

- **Audio-synchronized lip sync with I2V**
  - Use case: Creating talking character videos with audio input
  - *From: Kijai*

- **Video continuation with audio**
  - Use case: Extending video sequences while maintaining audio sync
  - *From: Ro*

- **Single-shot 720p generation without upscaling**
  - Use case: Faster generation by skipping multiscale approach
  - *From: MOV*

- **Use native workflow from templates**
  - Use case: Recommended over custom nodes, more reliable
  - *From: Cubey*

- **Audio + image to video generation**
  - Use case: Creating videos that react to music/audio input
  - *From: Kijai*

- **Multi-prompt generation for scenes**
  - Use case: Generate all scenes in one video using multiple prompts
  - *From: avataraim*


## Recommended Settings

- **VRAM requirements**: 24GB for fp8, 32GB+ for full model
  - Model size and audio processing requirements
  - *From: Vardogr*

- **Distilled inference steps**: 8 steps
  - Optimized for speed vs quality trade-off
  - *From: Kiwv*

- **Generation length**: 10 seconds
  - Standard output duration for the model
  - *From: Kiwv*

- **Steps for distilled model**: 8 sigmas
  - Prescribed steps for distilled version
  - *From: harelcain*

- **Steps for full model**: 20 steps
  - Recommended steps for full model
  - *From: harelcain*

- **Live preview method**: None
  - Prevents mat1 and mat2 multiplication errors
  - *From: KevenG*

- **Minimum resolution**: 352x256
  - Lowest resolution that should work, must be multiples of 32
  - *From: harelcain*

- **--fp8_e4m3fn-unet flag**: Enable when running ComfyUI
  - Reduces VRAM usage by about 3GB for low VRAM users
  - *From: mkupchik_lightricks*

- **Distill LoRA weight**: 0.6
  - Works well with fp8 model on 5090
  - *From: CrypticWit*

- **Resolution**: 832x480 for 24GB VRAM
  - Seems to be the working resolution for 4090/24GB setups
  - *From: Cubey*

- **Memory blocks**: 2 blocks in memory
  - Uses only 5.3GB during main inference
  - *From: Benjimon*

- **Resolution**: 1280x720
  - Sweet spot for 5090 - higher resolutions cause OOM errors
  - *From: burgstall*

- **Frames**: 81-242 frames
  - VRAM goes up to 98% on 5090 with 1280x720x81, 242 frames possible with good workflow
  - *From: burgstall*

- **Generation time**: 218 seconds for 1280x720
  - Typical generation time on RTX 5090
  - *From: burgstall*

- **VRAM requirement**: 24GB minimum
  - Lowest seen working is 24GB VRAM, unclear if 16GB works
  - *From: Lodis*

- **2K resolution**: 2560x1440
  - Standard 2K resolution specification
  - *From: l҈u҈c҈i҈f҈e҈r҈*

- **Steps and CFG**: 20 steps, 4 CFG default
  - Default recommended settings, can experiment with higher values
  - *From: harelcain*

- **Maximum resolution on RTX 5090**: 1920x864 at 121 frames, 1920x1088 at 481 frames
  - Hardware limitations for different frame counts
  - *From: Ruairi Robinson*

- **Frame counts**: 241, 361 frames work well
  - Avoids 32-bit index math errors
  - *From: seitanism*

- **Memory requirements**: RTX 6000 Pro can handle 1920x1280 at 242 frames
  - Full model performance on high-end hardware
  - *From: dg1860*

- **--reserve-vram**: 2-20 depending on setup
  - Prevents OOM errors and system freezing
  - *From: Kijai*

- **--cache-none**: enabled
  - Helps with memory issues on lower VRAM systems
  - *From: Kijai*

- **cfg**: 1.0
  - Optimal for speed without quality loss
  - *From: Kijai*

- **fps range**: 24-60
  - Supported framerate range for generation
  - *From: seitanism*

- **live preview**: disabled/none
  - Required - model doesn't support live preview yet
  - *From: Kijai*

- **--reserve-vram**: 5
  - Prevents OOM by reserving VRAM buffer
  - *From: crinklypaper*

- **steps**: 8
  - Recommended for distilled model
  - *From: Tachyon*

- **CFG**: 1.0
  - Works well with distilled model for fast generation
  - *From: Kijai*

- **--cache-none**: enabled
  - Helps with RAM management
  - *From: Kijai*

- **resolution**: 1280x720
  - Minimum for good I2V results
  - *From: Tachyon*

- **--reserve-vram**: 4-10
  - Prevents OOM by forcing more aggressive offloading, scale up for higher resolutions
  - *From: Kijai*

- **--cache-none**: enabled
  - Reduces disk writes and prevents excessive paging file usage
  - *From: Mngbg*

- **CFG for dev model**: 3-6
  - Dev version works with CFG 3-6, use CFG 1 only with distill LoRA
  - *From: seitanism*

- **CFG for distilled**: 1
  - Distilled model/LoRA designed for CFG 1
  - *From: seitanism*

- **Steps**: 8
  - Standard step count, distilled can use fewer steps
  - *From: Kijai*

- **Recommended resolution**: 1280x720
  - Good balance of quality and performance
  - *From: Tachyon*

- **--reserve-vram**: 4-6
  - Prevents OOM during upscale, compensates for poor offloading
  - *From: seitanism/Vardogr*

- **--preview-method**: none
  - Prevents crashes during generation
  - *From: David Snow*

- **--disable-pinned-memory --disable-async-offload**: enabled
  - Improves stability on some systems
  - *From: David Snow*

- **Base resolution limit**: <15k latent tensor size
  - Prevents artifacts from exceeding training data distribution
  - *From: harelcain*

- **Steps for second stage**: derived from sigma list
  - Number of steps = number of sigmas - 1
  - *From: harelcain*

- **--reserve-vram**: 4-5
  - Prevents OOM errors on RTX 4090/5090
  - *From: TK_999*

- **--cache-ram**: 40
  - Prevents random OOM errors
  - *From: TK_999*

- **CFG**: 1 for distilled model
  - Distilled model works better with lower CFG
  - *From: ucren*

- **Denoise**: 1.0 with basic scheduler
  - Generates whole video from scratch
  - *From: seitanism*

- **Length calculation**: 25fps (125 frames = 5 seconds)
  - Proper frame rate calculation for desired duration
  - *From: NC17z*

- **--reserve-vram**: 5
  - For multi-prompt generation and scene creation
  - *From: avataraim*

- **--reserve-vram**: 1.0
  - For 12GB VRAM with --cache-none and CPU clip device
  - *From: garbus*

- **--reserve-vram**: 4
  - For RTX 3090 usage
  - *From: Roman_S*

- **Resolution**: 1280x720
  - Good balance for quality and performance
  - *From: avataraim*

- **Duration**: 20s
  - Good balance, opens up possibilities for temporal inpainting and extending
  - *From: mamad8*


## Concepts Explained

- **Distilled model**: Model trained to generate in fewer steps (8 vs 20) with slight quality trade-off, makes LoRA training difficult
  - *From: Kiwv*

- **Spatial vs temporal upscaler**: Spatial upscales resolution, temporal upscales frame rate (frame interpolation)
  - *From: naomikenkorem*

- **NVFP4/NVFP8**: NVIDIA's new precision formats for RTX 5000+ series, more efficient than standard fp4/fp8
  - *From: Vardogr*

- **Distilled vs Full model**: Distilled model uses 8 sigma steps and is faster, full model uses ~20 steps for higher quality
  - *From: harelcain*

- **Block swapping**: Technique by Kijai that will help models run on lower VRAM by swapping model blocks in and out of memory
  - *From: Clint Hardwood*

- **Multiscale generation**: Generating at lower resolution then upscaling progressively rather than trying native high-res
  - *From: harelcain*

- **Block swapping**: Memory management technique to reduce VRAM requirements by swapping model parts
  - *From: CJ*

- **fp8 model**: 27GB model file that works with distilled lora for memory efficiency
  - *From: Tachyon*

- **Distilled lora**: Used alongside fp8 model for better performance and memory usage
  - *From: Tachyon*

- **System RAM requirements**: 64GB system RAM recommended alongside high VRAM GPU for stable operation
  - *From: Tachyon*

- **Retake feature**: Video editing/extension capability that maintains identity and allows continuation of existing videos
  - *From: harelcain*

- **Temporal latent upscaler**: Latent to latent fast model that upscales spatial/temporal dimension by factor of 2 for multiscale generations
  - *From: harelcain*

- **Sharded model files**: Gemma model is split across multiple .safetensors files (model-00001-of-00005.safetensors etc.) - all parts required for loading
  - *From: ltx_daphnaL*

- **Temporal upscaler vs Spatial upscaler**: Temporal is interpolation for more frames, spatial is for higher resolution
  - *From: Kijai*

- **High compression VAE**: Enables fast generation speed but may cause quality artifacts
  - *From: yi*

- **Block swapping**: Memory optimization technique not properly implemented in ComfyUI yet
  - *From: Ada*

- **LTXVCropGuides**: Node that removes context latent from output before VAE decode
  - *From: Dragonyte*

- **IC-LoRA**: Image conditioning LoRA for controlnet-like behavior in LTX Video 2
  - *From: harelcain*

- **Block offloading**: Technique to run model on lower VRAM by offloading blocks to RAM
  - *From: yi*

- **Context latent**: Additional latent frame added during generation that needs to be cropped out
  - *From: Dragonyte*

- **Reserve VRAM**: Forces ComfyUI to use more system RAM by reserving VRAM for OS, helps prevent OOM when automatic estimation fails
  - *From: Vardogr*

- **Distilled model**: Optimized version that can run with CFG 1 and fewer steps for faster generation
  - *From: seitanism*

- **MaskByTime node**: Controls when to start/stop editing input AV latents - mask_start_time and mask_end_time define editing period
  - *From: harelcain*

- **Two-stage approach**: Generate at quarter resolution first, then upscale with another partial denoise at final resolution
  - *From: harelcain*

- **Latent tensor size calculation**: Formula (w/32)*(h/32)*((f-1)/8+1) determines if resolution is within model's training bounds
  - *From: harelcain*

- **Multi-scale generation**: Generate at low resolution first, then upscale in stages to maintain quality and avoid artifacts
  - *From: harelcain*

- **Sigma scheduling**: Each sigma represents a denoising step, can use distilled model schedule values for custom step counts
  - *From: harelcain*

- **Reserve VRAM**: ComfyUI flag that reserves system RAM for OS/other software, compensates for poor model offloading
  - *From: harelcain*

- **Multiscale generation**: First stage at lower resolution, second stage adds details for better/faster results
  - *From: Dragonyte*

- **Deep compressed latent**: Makes training super fast, can get LoRAs in an hour
  - *From: Dragonyte*

- **NVFP4/NVFP8**: FP4 is nvfp4, FP8 has input scales for fp8 matmuls on newer hardware
  - *From: Kijai*

- **Temporal extension**: Video extension in time (duration) rather than spatial outpainting
  - *From: Roman_S*

- **Async offloading**: Technique used to run models on low VRAM by offloading to system RAM
  - *From: Kijai*

- **Tiled decode**: VAE decoding technique to reduce VRAM usage by processing in tiles
  - *From: Piblarg*


---

# LTX Chatter - January 7, 2026

# Ltx Chatter Knowledge Base
*Extracted from Discord discussions: 2026-01-07 to 2026-01-08*


## Technical Discoveries

- **Gemma text encoder works with quantized versions**
  - FP8 single version works with minimal quality difference
  - *From: Lodis*

- **Sage attention provides speed improvements**
  - Combined with 16 accumulation on default template speeds up generations significantly
  - *From: ucren*

- **Model can generate unexpected content**
  - Model adds Peppa Pig content without prompting, revealing training data
  - *From: Kijai*

- **Audio latent multiplication creates interesting effects**
  - Multiplying audio latent produces unexpected visual results
  - *From: Kijai*

- **Model has pronunciation quality**
  - Consistently pronounces words well in generated audio
  - *From: TK_999*

- **Seed variation significantly affects quality**
  - Top 0.1% of seeds produce amazing results, seed hunting is valuable
  - *From: mallardgazellegoosewildcat2*

- **16 steps works better than 8 for non-distilled workflows**
  - User switched from 8 steps (inherited from distilled workflow) to 16 steps and got better results, noting default is 25 and comfy uses 20
  - *From: Dever*

- **LTX-2 generates 10 seconds of 1080p footage in under 3 minutes**
  - Speed benchmark for local generation
  - *From: KakerMix*

- **Model generates at half resolution then upscales**
  - Most of the speed improvement comes from generating at lower resolution and upscaling, plus distillation
  - *From: TK_999/Moonbow*

- **VAE decode is the biggest time sink**
  - For the generation process, VAE decoding takes longer than the actual video generation
  - *From: Clint Hardwood/TK_999*

- **Full fp8 model works with distilled workflow but crashes with full workflow during VAE decode**
  - Specific compatibility issue between model versions and workflows
  - *From: Tachyon*

- **Original LTXV LoRAs still somewhat work with LTX-2**
  - Backwards compatibility with previous version LoRAs
  - *From: tarn59*

- **Distilled and non-distilled fp8 models are the same size**
  - Both fp8 versions have identical file sizes
  - *From: Tachyon*

- **LTX Video 2 works down to 4GB VRAM**
  - Kijai tested and confirmed 4GB VRAM compatibility
  - *From: Lodis*

- **Text encoder loading behavior affects VRAM usage**
  - When encoding text, it loads the whole Gemma into VRAM, then offloads Gemma to pagefile/RAM and loads the main model for sampling
  - *From: yi*

- **Native ComfyUI nodes only need 1 file for text encoder**
  - Native implementation uses single file instead of whole folder for text encoder
  - *From: yi*

- **FP4 should work well now, especially with 50 series GPUs**
  - Performance improvements for FP4, optimized for newer hardware
  - *From: comfy*

- **Model needs detailed, verbose prompts**
  - LTX Video 2 requires LLM-style language with lots of fluff and details, which also increases video quality
  - *From: Zabo*

- **Sage attention provides speed improvements**
  - Patch Sageattention node works and provides small speed bump
  - *From: Tachyon*

- **LTX2 provides massive quality improvement over v0.9**
  - User described upgrade as 'night and day, HUGE upgrade'
  - *From: Lodis*

- **FP8 distilled model works at 720p in approximately 1 minute**
  - Good prompt adherence, audio working and fitting well
  - *From: Lodis*

- **LTX2 has significantly better volumetrics than other models**
  - Non-fucky volumetrics, no dithered artifacts on water/smoke unlike HunYuan and Wan
  - *From: ZombieMatrix*

- **Camera effects LoRAs from LTX 0.97 work well with LTX2**
  - No need to retrain camera effect LoRAs, but effect LoRAs may deteriorate quality slightly
  - *From: NebSH*

- **Detail LoRA helps with 2D/anime generation quality**
  - Improved details for animated content generation
  - *From: Choowkee*

- **Full model + distill LoRA gives better results than distilled model**
  - Better quality using full model with distill LoRA at 8 steps CFG 4 vs distilled model at 8 steps CFG 1
  - *From: gopnik*

- **LTX2 can generate audio from existing video with minimal prompts**
  - Testing with just 'man is speaking' prompt generates coherent audio, even works with no prompt at all when video is masked
  - *From: Kijai*

- **LTX2 supports keyframe-based generation through CLI**
  - Can use 5 photos as evenly spaced keyframes and model transitions through all input photos
  - *From: wouter*

- **Smudginess during movement is caused by latent misalignment**
  - Original workflows only use spatial upscaler, but you need both temporal and spatial upscalers to prevent smudginess during movement
  - *From: Ada*

- **VAE issues with fast moving objects**
  - Better to use temporal upscaler to double effective latent fps before VAE decode stage
  - *From: harelcain*

- **Model has Indian/Bollywood bias in outputs**
  - Dataset contains a lot of old Bollywood movies, causing bias toward Indian people in generations
  - *From: 企鵝（50% CASH 50%GOLD）*

- **LTX 0.97 LoRAs are compatible with LTX-2**
  - Old LoRAs from version 0.97 work with the new LTX-2 model
  - *From: NebSH*

- **Sage attention makes LTX-2 significantly faster**
  - Using sage attention provides approximately 3x speed improvement
  - *From: Hevi*

- **French language prompts work well with LTX-2**
  - French text-to-video generation produces good results, described as 'almost sota for French text to speech'
  - *From: mamad8*

- **German language prompts also work**
  - German prompts produce functional results
  - *From: gopnik*

- **Audio latent strength can be controlled with LatentMultiply node**
  - You can tone down the audio latent effect on animation by using LatentMultiply on the audio latent
  - *From: ucren*

- **Video-to-audio generation works by masking video latent**
  - Adding a zero latent noise mask to video latent before sampler generates synced audio
  - *From: Kijai*

- **Temporal upscaler converts 24fps to 48fps**
  - When using temporal upscaler, you must change the save video node to 48fps while keeping sampler at 24fps
  - *From: yi*

- **LTX Video 2 technical paper released**
  - Technical paper dropped on January 5th
  - *From: fearnworks*

- **LTX-2 4K generation works on 4090**
  - 4K sampling working fine with 1464.33 MB usable, 1088.48 MB loaded, 19452.79 MB offloaded
  - *From: Kijai*

- **Audio reactive pose control working with LTX-2**
  - Successfully implemented audio reactive pose control using SCAIL nodes
  - *From: burgstall*

- **Landscape orientation produces better motion than portrait**
  - Motion is much better in landscape format compared to portrait
  - *From: Ashtar*

- **Distilled LoRA with dev model provides 2x speed improvement**
  - Normal takes 80sec, with distilled LoRA takes 40sec for same generation
  - *From: avataraim*

- **Temporal upscaling changes FPS by x2**
  - Using 2x spatial would make resolution x4
  - *From: Gleb Tretyak*

- **LTXVPreProcess node adds compression noise to input image**
  - It helps to generate more motion in the video
  - *From: Kijai*

- **Side padding trick not working for anime characters**
  - But it's really fast, only takes 110 sec to gen a 720P 30FPS on RTX pro 6K with no spatial upscale
  - *From: KingGore2023*

- **Model has biases toward bollywood and microphones**
  - These keep appearing in generations
  - *From: ucren*

- **Frame count needs to be 8n+1 format**
  - Must be divisible by 8, plus 1 frame
  - *From: Scruffy*

- **Temporal latent upscale node added 15 latent frames**
  - Used for frame interpolation
  - *From: 企鵝（50% CASH 50%GOLD）*

- **LTXVAddGuide node is for keyframing, not looping video**
  - Wraps lots of logic on how to denoise parts of latents, tile, extend, etc. Good for complex conditioning masks
  - *From: Dragonyte*

- **Higher frame rates eliminate artifacts**
  - 24 fps vs 50 fps shows most artifacts disappear at higher frame rates
  - *From: Tonon*

- **Frame interpolation works with keyframes**
  - 12 frames inbetween keyframes creates smooth interpolation, needs minimum 10 frame gaps to work properly
  - *From: Kijai*

- **FP4 model only runs native on Blackwell cards**
  - On other cards FP4 is just upcasted, not true FP4 performance
  - *From: Kijai*

- **Model is very efficient**
  - So efficient that user joked about needing to turn on room heating
  - *From: Kijai*

- **Empty frames needed between keyframes**
  - Need lot more empty frames for keyframe interpolation to work properly, minimum 10 frames recommended
  - *From: Kijai*


## Troubleshooting & Solutions

- **Problem:** I2V crashes with 3GB VRAM load
  - **Solution:** Load text encoder with T2I prompt first, then switch to I2V workflow
  - *From: FUNZO*

- **Problem:** Comfy update needed for functionality
  - **Solution:** Update ComfyUI to resolve loading issues
  - *From: dj47*

- **Problem:** OOM errors frequently occurring
  - **Solution:** Use --reserve-vram flag and ComfyUI_ExtraModels node
  - *From: garbus*

- **Problem:** Clip loader forced to CPU despite spare VRAM
  - **Solution:** Use Force/Set Clip Device node to override
  - *From: FancyJustice*

- **Problem:** I2V producing static slideshow effect
  - **Solution:** Add noise to image or ensure prompt has action, use noise injection node
  - *From: Kijai*

- **Problem:** Models loading in wrong order causing exit
  - **Solution:** Try alternative workflows, may be environment specific
  - *From: Mngbg*

- **Problem:** LTX consuming all pagefile on Windows
  - **Solution:** Turn off pagefile if you have 64GB+ system RAM
  - *From: Moonbow*

- **Problem:** Loading fails with Gemma module errors
  - **Solution:** Manually git pull ComfyUI from master branch to get latest updates
  - *From: Tachyon*

- **Problem:** Audio VAE encode error with short audio
  - **Solution:** Set trim audio duration node start_index to 0 instead of default 25
  - *From: 304770846873092097*

- **Problem:** Memory errors when switching between different prompts
  - **Solution:** Need to restart ComfyUI occasionally due to memory bugs
  - *From: Moonbow/VK*

- **Problem:** Crashes during VAE decode at higher resolutions
  - **Solution:** Lower the spatial tiles setting to 6 or use tiled VAE decode
  - *From: TK_999/buggz*

- **Problem:** Model/TE reloads after every run on 16GB VRAM
  - **Solution:** Issue with current implementation - awaiting optimization
  - *From: yi*

- **Problem:** Frozen frame videos
  - **Solution:** Try euler_a with 20 steps and 5 CFG
  - *From: Cubey*

- **Problem:** CheckpointLoaderSimple 'NoneType' object has no attribute 'Params'
  - **Solution:** Update ComfyUI to latest nightly version
  - *From: yi*

- **Problem:** 'LTXAVTEModel_' object has no attribute 'processor'
  - **Solution:** Use native ComfyUI workflow instead of custom nodes, or update to latest ComfyUI nightly
  - *From: yi*

- **Problem:** Import failed error with custom nodes
  - **Solution:** Git pull ComfyUI manually, make sure you're on master branch
  - *From: Tachyon*

- **Problem:** ImportError: cannot import name 'precompute_freqs_cis'
  - **Solution:** Remove corrupted old version of custom node and reinstall
  - *From: Lodis*

- **Problem:** Audio cutting off at halfway point
  - **Solution:** Check for mismatch between real video fps and video fps used for audio latent initialization
  - *From: harelcain*

- **Problem:** Invalid tokenizer in audio to video workflow
  - **Solution:** Use the ComfyUI org text encoder instead of sharded model, or change the text encoder node
  - *From: Kijai*

- **Problem:** Workflow nodes not connecting properly
  - **Solution:** ComfyUI loads some workflows incorrectly - manually rewire nodes in subgraph
  - *From: Q-*

- **Problem:** Audio trim node error when audio is shorter than trim start time
  - **Solution:** Audio trim node set to start at 25 seconds but user audio was shorter - adjust trim start time
  - *From: Kijai*

- **Problem:** SageAttention fallback error with FP8 model
  - **Solution:** Remove --use-sage-attention startup flag when using SageAttention patch node
  - *From: japar*

- **Problem:** T2V full workflow crashes during VAE decode
  - **Solution:** Use ComfyUI template workflow instead, issue seems specific to certain workflow configurations
  - *From: Tachyon*

- **Problem:** Gemma model loading causes 30-second delays on 16GB VRAM
  - **Solution:** Use --reserve-vram startup argument to prevent VRAM swapping issues
  - *From: Kijai*

- **Problem:** Random OOM errors on 3090
  - **Solution:** Add --reserve-vram 4 to ComfyUI startup arguments
  - *From: Hevi*

- **Problem:** Randomize seed not working in subgraphs
  - **Solution:** Unpack the subgraph or check if seed is connected to input vs promoted
  - *From: Zabo*

- **Problem:** Smudging on fast movement in videos
  - **Solution:** Must use both temporal and spatial upscalers together, not just spatial
  - *From: Ada*

- **Problem:** ComfyUI crashes when loading LTXV Audio Text Encoder
  - **Solution:** Try using --reserve-vram with higher values, crashes often due to RAM issues
  - *From: Kijai*

- **Problem:** OOM errors on first run but works on second run
  - **Solution:** Use --reserve-vram parameter and clear models/cache between generations
  - *From: BobbyD4AI*

- **Problem:** Smudginess during movement in generated videos
  - **Solution:** Use both temporal and spatial upscalers instead of just spatial
  - *From: Ada*

- **Problem:** ComfyUI crashes with non-fp8 models
  - **Solution:** Only use fp8dev model, other models cause ComfyUI to terminate
  - *From: avataraim*

- **Problem:** COMBO values appearing in nodes
  - **Solution:** Remove combo node and put checkpoint name directly, or disconnect/reconnect
  - *From: Ada*

- **Problem:** Error with res_2s sampler not found
  - **Solution:** Switch to euler_ancestral sampler or install RES4LYF node pack
  - *From: seitanism*

- **Problem:** Long loading times in sample node
  - **Solution:** This indicates VRAM leaking, clear models or restart ComfyUI
  - *From: hicho*

- **Problem:** Machine freezing when VRAM gets used up
  - **Solution:** Use --reserve-vram parameter, disable 'system fallback' in NVIDIA control panel
  - *From: Kijai*

- **Problem:** OOM errors on various GPUs including RTX 4090 and RTX 5090
  - **Solution:** Use --reserve-vram flag with values like 4, 6, or 10 depending on your setup
  - *From: seitanism*

- **Problem:** Prompt changes causing double generation time
  - **Solution:** Set text encoder device to CPU to prevent model reloading
  - *From: yi*

- **Problem:** --fp16-vae causing I2V workflow problems
  - **Solution:** Remove --fp16-vae from startup command
  - *From: boorayjenkins*

- **Problem:** Xformers errors with bf16 on non-A100 GPUs
  - **Solution:** bf16 is only supported on A100+ GPUs, use different precision
  - *From: protector131090*

- **Problem:** VAE decode OOM on large resolutions
  - **Solution:** Use tiled VAE node and lower tile size (e.g., 384 for 832x480)
  - *From: patientx*

- **Problem:** Portrait video generation not working properly
  - **Solution:** Use height smaller than 1080 for better results
  - *From: mkupchik_lightricks*

- **Problem:** Audio out of sync with temporal upscaler
  - **Solution:** Keep sampler at 24fps but set save video node to 48fps, remove frame rate node connection
  - *From: Owlie*

- **Problem:** Tensor mismatch when concatenating empty latent audio with i2v latent
  - **Solution:** Need to ensure tensor dimensions match between audio and video latents
  - *From: DawnII*

- **Problem:** Motionless first 5 seconds then motion in next 5 seconds
  - **Solution:** Change the seed, change the videoInPlace strength
  - *From: ucren*

- **Problem:** Start image fully lost in pose control
  - **Solution:** Strength too low, increase I2V node strength
  - *From: ucren*

- **Problem:** OOM issues on high-end systems
  - **Solution:** Add --reserve-vram 4 or --reserve-vram 6 to ComfyUI args
  - *From: Tyronesluck*

- **Problem:** DLL load failed error with audio workflow
  - **Solution:** Download latest portable ComfyUI version
  - *From: yi*

- **Problem:** RAM issues with less than 48GB
  - **Solution:** Use --no-cache argument to help tremendously
  - *From: Vardogr*

- **Problem:** Second sampler step taking too long
  - **Solution:** Increase --reserve-vram to 5, reduced time from 30 secs per iteration to 5
  - *From: 企鵝（50% CASH 50%GOLD）*

- **Problem:** Audio sync is 2x speed off with temporal upscaling
  - **Solution:** Need to temporal scale the audio latent too, and fps x2
  - *From: ucren*

- **Problem:** SamplerCustomAdvanced error: too many values to unpack (expected 4)
  - **Solution:** Issue with temporal upscale not working properly with audio latents
  - *From: ucren*

- **Problem:** Face consistency on i2v is bad
  - **Solution:** Use first last frame to solve consistency issue, or mess with strength settings
  - *From: ボグダンおじさん*

- **Problem:** OOM issues with Gemma 3
  - **Solution:** Use startup argument --reserve-vram 4 (more or less, in gigabytes)
  - *From: Kijai*

- **Problem:** Tiled VAE generating visible tiles
  - **Solution:** No specific solution provided, acknowledged as a problem
  - *From: Juan Gea*

- **Problem:** Audio cuts out at exactly halfway point
  - **Solution:** Use shorter audio text or check if frame amount is correct (not too many)
  - *From: Gleb Tretyak*

- **Problem:** Loading/reloading/offloading models killing PC
  - **Solution:** Use fp8 gemma with projections_only model to fix reloading issue
  - *From: avataraim*

- **Problem:** --fp16-vae startup arg causing issues
  - **Solution:** Remove --fp16-vae from startup arguments
  - *From: sawlike*

- **Problem:** Matplotlib error with sigma visualize node
  - **Solution:** Remove the sigma visualize node
  - *From: Kijai*

- **Problem:** Latent upscaler node not finding models
  - **Solution:** Place models in models/latent_upscale_models/ folder, may need local directory instead of extra model paths
  - *From: Lumori*

- **Problem:** Getting slideshows instead of motion
  - **Solution:** Prompt must describe what happens between keyframes, otherwise you get slideshow
  - *From: Benjimon*

- **Problem:** OOM errors
  - **Solution:** Use --cache-none flag and disable pinned memory for 32GB systems
  - *From: Kijai*

- **Problem:** Audio sync issues with temporal upscaler
  - **Solution:** Manually align audio by doubling audio latents to match visual samples
  - *From: ucren*


## Model Comparisons

- **Full Gemma vs FP8 Gemma**
  - No significant quality difference, FP8 preferred for smaller file size
  - *From: Lodis*

- **Distilled vs non-distilled models**
  - Distilled improves quality 10-fold vs dev, slight quality improvement over regular
  - *From: Clint Hardwood*

- **Spatial vs temporal upscaler**
  - Spatial works better, temporal may have issues with distill lora
  - *From: TK_999*

- **LTX vs Sora capabilities**
  - Comparable for realistic videos, can do 20 seconds with audio and multi-cut scenes
  - *From: dj47*

- **ComfyUI native vs LTX custom workflows**
  - LTX official workflows give better results than ComfyUI versions
  - *From: Ada*

- **LTX-2 vs Sora**
  - Feels very close to Sora quality, described as 'Sora 1.5 - between Sora 1 and 2'
  - *From: KakerMix/VK*

- **LTX-2 vs Veo 3**
  - LTX-2 feels real close to Veo 3 quality but local and faster
  - *From: KakerMix*

- **LTX-2 vs Wan**
  - Way faster than Wan, speed not considered an issue
  - *From: Moonbow*

- **Distilled vs non-distilled**
  - Non-distilled has better music generation
  - *From: Benjimon*

- **Full fp8 vs fp8 distilled**
  - fp8 distilled gives poor quality results for some users
  - *From: aipmaster*

- **LTX Video 2 vs WAN for setup difficulty**
  - Less initial troubleshooting with LTX Video 2 than WAN 2.2
  - *From: Choowkee*

- **LTX Video 2 vs WAN performance**
  - WAN: 5 sec videos 640x360 per minute, LTX: 1280x720 + audio in same time
  - *From: Miku*

- **T2V vs paid API services**
  - 1 minute for 5 second video with audio is faster than paid APIs due to no API calls
  - *From: dj47*

- **Custom nodes vs native workflows**
  - Both are functionally identical for normal t2v/i2v, same speed
  - *From: Tachyon*

- **LTX2 vs LTX 0.9**
  - LTX2 is a massive upgrade, described as 'night and day' difference
  - *From: Lodis*

- **Full model + distill LoRA vs distilled model**
  - Full model with distill LoRA at 8 steps CFG 4 gives better results than distilled model at 8 steps CFG 1
  - *From: gopnik*

- **LTX2 volumetrics vs HunYuan/Wan**
  - LTX2 has superior volumetrics without dithered artifacts on water/smoke
  - *From: ZombieMatrix*

- **Full fp8 model vs distilled with LoRA**
  - Full fp8 model with LoRA at 0.6 strength has better quality and almost same generation time
  - *From: gopnik*

- **Native Windows vs WSL2**
  - Native Linux loads models instantly, WSL2 has very long loading times for text encoder and models
  - *From: seitanism*

- **LTX-2 vs Sora and Veo**
  - Better than Veo, comparable to Sora but LTX-2 wins by being open source
  - *From: protector131090*

- **LTX-2 vs previous models for emotion**
  - Emotion in voice and faces is amazing, better than Sora and Veo
  - *From: protector131090*

- **LTX2 vs SVi humo**
  - LTX2 has long duration, high res, native lipsync and sounds with ability to replace audio. Flickers like svi humo but more advantages
  - *From: Gleb Tretyak*

- **Distilled vs dev model**
  - Dev model preferred over distilled - distilled is too burned out
  - *From: Grimm1111*

- **2D/anime vs realistic content**
  - Model mostly good with realistic content, 2d comic and anime does not perform so well
  - *From: Tonon*

- **LTX Video 2 vs Veo 3.1**
  - Better than Veo 3.1 for user's specific use cases
  - *From: Tonon*

- **LTX Video 2 vs previous LTX models**
  - Much more interesting than previous LTX models beyond just speed
  - *From: Kijai*

- **LTX Video 2 vs Sora 2**
  - Close to Sora 2 quality, just needs prompt to LLM for creativity
  - *From: Rainsmellsnice*


## Tips & Best Practices

- **Use sage attention with accumulation for speed**
  - Context: Default template with sage + 16 accum speeds up significantly
  - *From: ucren*

- **Reserve VRAM to avoid reloading models**
  - Context: Use --reserve-vram 5 so you don't select same model 3 times
  - *From: Kijai*

- **Add noise for I2V motion**
  - Context: When image lacks noise or prompt lacks action, use noise injection
  - *From: Kijai*

- **Use tiled VAE decode for Apple Silicon**
  - Context: Change to tiled VAE decode using T2V settings for better performance
  - *From: buggz*

- **Seed hunting improves results dramatically**
  - Context: Top 0.1% seeds are significantly better, worth exploring different seeds
  - *From: mallardgazellegoosewildcat2*

- **SDE sampling with S_noise above 1 helps**
  - Context: Can improve generation quality as usual with diffusion models
  - *From: mallardgazellegoosewildcat2*

- **Use tiled VAE decode instead of regular VAE decode**
  - Context: Better performance and stability, prevents machine lockups
  - *From: buggz*

- **Disable prompt enhancer node for better compatibility**
  - Context: When having issues with workflows
  - *From: Tachyon/Miku*

- **Use --no-cache and --fast flags for performance boost**
  - Context: ComfyUI startup parameters
  - *From: Vardogr*

- **Skip upscaling step for faster seed fishing**
  - Context: When testing prompts quickly, can upscale later
  - *From: Moonbow*

- **Use non-distilled for first pass, then refine upscale with distilled**
  - Context: Following source code approach for best quality
  - *From: Benjimon*

- **Start with 1280x704 121 frames for testing**
  - Context: Recommended starting resolution/length for stability
  - *From: Tachyon*

- **Use detailed, verbose prompts with lots of fluff**
  - Context: LTX Video 2 responds better to LLM-style language and increases video quality
  - *From: Zabo*

- **Don't use custom node Gemma node**
  - Context: Stick with native workflows to avoid issues
  - *From: Tachyon*

- **Use res_2s to reduce steps**
  - Context: With res_2s you can drop steps to 10 because it doubles to 40 overall
  - *From: Tachyon*

- **Never use upscaler output as-is**
  - Context: Always denoise upscaler results further with low sigmas to add detail and fix audio-video sync
  - *From: harelcain*

- **Use spatial LoRA for better quality**
  - Context: Spatial gives more quality, temporal is for higher fps
  - *From: Miku*

- **Add detailer LoRA only to stage 2**
  - Context: Unless it's specifically a detailer LoRA, only add to second stage
  - *From: tavi.halperin*

- **Use dense, elaborate prompts for best T2V results**
  - Context: Feed lyrics into AI to generate 1000-word dense prompt descriptions
  - *From: ZombieMatrix*

- **Use both temporal and spatial upscalers together**
  - Context: Videos look far worse without both upscalers, prevents smudging on movement
  - *From: Ada*

- **Consider image compression settings for quality vs memory tradeoff**
  - Context: Higher than 10 can have negative impact, similar to older models
  - *From: ZombieMatrix*

- **FP8 distilled model is safe bet for 4090 users**
  - Context: Very fast performance on 4090 GPUs
  - *From: Kijai*

- **Use both temporal and spatial upscalers**
  - Context: To prevent smudginess during movement in generated videos
  - *From: Ada*

- **Clear models/cache between each generation**
  - Context: When experiencing OOM issues on 4090
  - *From: BobbyD4AI*

- **Don't use monitor on same GPU**
  - Context: To avoid VRAM conflicts and improve stability
  - *From: Kijai*

- **Install bitsandbytes dependency**
  - Context: Required for running 4-bit quantized Gemma models
  - *From: Hevi*

- **Disable swap file can cause instability**
  - Context: Disabling Windows swap file makes system unstable and can cause crashes
  - *From: seitanism*

- **Use simplified prompts for better movement**
  - Context: When getting zero movement in generations, try simple prompts like 'a woman talking'
  - *From: Dever*

- **Use country-specific ethnicity descriptors**
  - Context: Instead of generic terms like 'white' or 'caucasian', use specific country references like 'irish man'
  - *From: ZombieMatrix*

- **Always use input images for better results**
  - Context: I2V performs better than T2V according to LTX tutorial
  - *From: Tonon*

- **Be very clear and verbose in prompts to avoid Bollywood bias**
  - Context: Model has strong Bollywood training bias, requires 16k+ token prompts to override
  - *From: ZombieMatrix*

- **Enhance prompts using Grok with enhancer node instructions**
  - Context: For better prompt enhancement workflow
  - *From: gopnik*

- **Get GPT to fully describe the start image and include it in prompt**
  - Context: To prevent LTX-2 from dropping the input image and doing text-to-image instead
  - *From: AJO*

- **Apply pose control only to first few steps**
  - Context: For best results with pose control workflows
  - *From: Kijai*

- **Use 0.6 strength instead of 1.0 for better i2v motion**
  - Context: In LTX workflow for improved motion quality
  - *From: fearnworks*

- **Add temporal upscaler after spatial upscaler**
  - Context: Increases quality for fast motion scenes, though doubles duration
  - *From: Gleb Tretyak*

- **Use fixed seed and prompt (changing only text) for consistent voices**
  - Context: Achieves very consistent voice generation across clips
  - *From: protector131090*

- **Use first last frame inference for consistency**
  - Context: When dealing with face consistency issues
  - *From: Benjimon*

- **On latent upscale pass set imgtovideoinplace strength to 1**
  - Context: For upscaling workflow
  - *From: ucren*

- **Lower the strength on the low res pass**
  - Context: When dealing with upscaling issues
  - *From: ucren*

- **Use more compression and/or less strength on the image**
  - Context: When getting static images instead of motion
  - *From: Kijai*

- **If it doesn't move with image strength under 0.3 something else is borked**
  - Context: Troubleshooting static image issues
  - *From: Kijai*

- **Prompt for fast movement instead of slow**
  - Context: Getting static or barely moving images when prompting for slow movement
  - *From: Gleb Tretyak*

- **Use samplers that add noise like euler_a, lcm**
  - Context: For better generation results
  - *From: Kijai*

- **Use horizontal or square resolutions**
  - Context: Vertical images work less predictably and give worse results, especially for audio workflow
  - *From: Owlie*

- **Reduce frame rate and use interpolation for speed**
  - Context: Cuts generation times in half while allowing much longer video times
  - *From: Phr00t*

- **Use lower strength for more motion**
  - Context: Lower strength gives more motion but less adherence to original image
  - *From: gordo*

- **Use 81 empty frames between 4 keyframe images**
  - Context: For keyframe interpolation with multiple images
  - *From: avataraim*


## News & Updates

- **LTX team working on separating audio model from video model**
  - 5B audio model separation from 14B video model to save VRAM for users who don't need audio
  - *From: Lodis*

- **Day one training code available from Lightricks**
  - Training repository supports image-only training, processes as 1-frame video
  - *From: fearnworks*

- **Overnight updates to ComfyUI and Kijai nodes**
  - Bug fixes and improvements released
  - *From: Tachyon*

- **LTX Video 2 released January 5, 2026**
  - Supports text-to-video and image-to-video generation with audio
  - *From: context*

- **ComfyUI kitchen extension causing warnings**
  - Shows extension file not found for CUDA, but triton works fine anyway
  - *From: Lodis*

- **Custom node workflows updated an hour ago**
  - Lightricks pushed updates including workflow fixes
  - *From: Tachyon*

- **Example workflows with enhancer prompt node published**
  - Includes editable system prompt functionality, published 4 hours ago
  - *From: 1376860387873390672*

- **Audio-only and video-only derivative models exist but not released**
  - Both are smaller and faster than full model, release uncertain
  - *From: harelcain*

- **Native LTX-2 templates available in ComfyUI**
  - Official templates are now in ComfyUI workflow templates, accessible via browse templates
  - *From: seitanism*

- **Work being done to solve VRAM management issues**
  - Development in progress to fix VRAM estimation and management problems
  - *From: Kijai*

- **comfyui-workflow-templates pip package contains LTX-2 workflows**
  - Templates are available through the pip package installation
  - *From: Kijai*

- **LTX Video 2 technical paper released**
  - Available at https://arxiv.org/pdf/2601.03233
  - *From: fearnworks*

- **First LTX-2 LoRA released**
  - First community-trained LoRA for LTX-2 posted on Reddit
  - *From: Ada*

- **Depth and canny control models released for LTX-2**
  - Official depth and canny control models work pretty well
  - *From: Kijai*

- **Changes made to ComfyUI for LTX support**
  - Recent commit addressing LTX integration issues
  - *From: Vardogr*

- **CEO will be holding a Reddit AMA tomorrow**
  - Announced on Discord events
  - *From: ltx-2*

- **WAN2GP v10.10 now supports LTX-2**
  - Low VRAM version, can run with 10GB VRAM, 2 minutes for 20s at 720p with 24GB+ VRAM
  - *From: Benjimon*


## Workflows & Use Cases

- **Image-to-video with audio driving**
  - Use case: Creating videos with subjects moving/dancing to music
  - *From: NC17z*

- **Video-to-audio extraction**
  - Use case: Using model as expensive video->audio converter for old content
  - *From: Kiwv*

- **Upscaling pipeline with FlashVSR**
  - Use case: Combine LTX with FlashVSR and audio upscaler for quality video
  - *From: Kiwv*

- **ComfyUI template workflows using LTXV Audio Text Encoder Loader**
  - Use case: Faster text encoder loading compared to Gemma 3 Model loader
  - *From: Tachyon*

- **Two-pass generation: non-distilled first pass, distilled upscale second**
  - Use case: Following source code approach for optimal quality
  - *From: Benjimon*

- **Kijai's audio + image to video workflow**
  - Use case: Incorporating custom audio with image input
  - *From: 834759695939928064*

- **Native ComfyUI templates**
  - Use case: Standard t2v/i2v generation without custom nodes
  - *From: yi*

- **Custom node workflows from Lightricks**
  - Use case: Advanced features like LoopingSampler and detailer flows
  - *From: tavi.halperin*

- **Two-stage generation**
  - Use case: Stage 1 for base generation in lower res, stage 2 for upscaling to larger res
  - *From: tavi.halperin*

- **Video extension using padding**
  - Use case: Pad video with black frames and silent audio, use LTXVSetAudioVideoMaskByTime to regenerate specific sections
  - *From: harelcain*

- **Audio insert workflow by Kijai**
  - Use case: Generating videos with custom audio input, used for music video creation
  - *From: ZombieMatrix*

- **Dense prompt workflow for music videos**
  - Use case: Using AI to expand lyrics into detailed prompts, generating 28-second music videos
  - *From: ZombieMatrix*

- **Audio generation from existing video**
  - Use case: Adding speech or audio to silent video clips using masking
  - *From: Kijai*

- **Keyframe-based video generation via CLI**
  - Use case: Creating transitions between 5 input photos using CLI tools
  - *From: wouter*

- **Dual upscaler approach**
  - Use case: Using both temporal and spatial upscalers to prevent motion artifacts
  - *From: Ada*

- **Audio-driven animation using video latent masking**
  - Use case: Generate synced audio by adding zero latent noise mask to video latent
  - *From: Kijai*

- **Using LatentMultiply to control audio influence**
  - Use case: Tone down exaggerated mouth movements in audio-driven animation
  - *From: ucren*

- **Audio reactive pose control with LTX-2**
  - Use case: Creating videos with pose control synchronized to audio beats
  - *From: burgstall*

- **2x upscaling workflow for LTX-2**
  - Use case: Generate at 544x976 then upscale to 1080x1920 in 80 seconds
  - *From: AJO*

- **Audio-driven video generation**
  - Use case: Using audio input to drive video generation with pose sequences
  - *From: Kijai*

- **Temporal upscaling for frame interpolation**
  - Use case: Converting 16fps to 64fps and increasing resolution to 1000x1600
  - *From: 企鵝（50% CASH 50%GOLD）*

- **First to last frame workflow using LTXVAddGuide**
  - Use case: Setting keyframes at different indices, img2video for first frame, addguide for last frame
  - *From: TK_999*

- **Audio and image to video workflow**
  - Use case: Generating video with both audio and image input
  - *From: KangTaeMoo*

- **Keyframe interpolation with guide frames**
  - Use case: Creating smooth motion between sparse keyframes, good for video interpolation
  - *From: Kijai*

- **Audio-visual generation workflow**
  - Use case: Generating videos with synchronized audio, works better with horizontal/square images
  - *From: Owlie*


## Recommended Settings

- **--reserve-vram**: 5
  - Prevents reloading models multiple times
  - *From: Kijai*

- **Noise injection**: 40 (higher for audio driving)
  - Prevents slideshow effect in I2V
  - *From: Kijai*

- **Resolution**: 720p most common
  - Balance of quality and performance
  - *From: Lodis*

- **Accumulation**: 16
  - Speed improvement with sage attention
  - *From: ucren*

- **Steps**: 20 steps default, 16-25 range
  - 20 works well for most cases, 16 better than 8, default is 25
  - *From: Dever/buggz*

- **Scheduler**: res_2m for 20 steps
  - Works better than res_2s, good for 20 step generation
  - *From: garbus*

- **CFG**: 5
  - Used with euler_a scheduler for frozen frame issues
  - *From: Cubey*

- **LoRA strength**: 0.6 for i2v, 1.0 for t2v
  - Default values that work well
  - *From: garbus/KakerMix*

- **Spatial tiles**: 6
  - Prevents crashes during VAE decode
  - *From: TK_999*

- **Reserve VRAM**: --reserve-vram 4
  - For low VRAM setups to use system RAM
  - *From: Tachyon*

- **CFG**: 1
  - Recommended for fp8 model
  - *From: drbaph*

- **Steps**: 8
  - Recommended for fp8 model
  - *From: drbaph*

- **FPS**: 24-25
  - Default workflows use 24-25 fps, model supports up to 60
  - *From: Lodis*

- **Frames**: 121
  - 121 frames at 24fps = exactly 5 seconds (120 frames divided by 24)
  - *From: Lodis*

- **Resolution**: 1280x720
  - Good balance of quality and performance
  - *From: Tachyon*

- **Image strength**: 0.6
  - Level of adherence to first frame, 0=ignore, 1=fully reconstruct
  - *From: tavi.halperin*

- **Sampler**: Euler
  - Subjectively best results reported
  - *From: Choowkee*

- **Steps and CFG for full model + distill LoRA**: 8 steps, CFG 4
  - Better quality than distilled model at 8 steps CFG 1
  - *From: gopnik*

- **Steps and CFG for distilled model**: 8 steps, CFG 1
  - Optimized for speed with 2x speedup from CFG=1
  - *From: harelcain*

- **Distill LoRA strength**: 0.6 in original workflow, 1.0 also works
  - No big quality difference but 1.0 seems faster
  - *From: gopnik*

- **Image compression**: 33 default, avoid higher than 10
  - Higher values can negatively impact quality
  - *From: ZombieMatrix*

- **Reserve VRAM**: --reserve-vram 4
  - Prevents OOM errors, allows sampling with minimal VRAM
  - *From: Hevi*

- **--reserve-vram**: 4-6 GB
  - Prevents OOM errors on RTX 4090
  - *From: BobbyD4AI*

- **LoRA strength**: 0.6
  - Good balance of quality with full fp8 model
  - *From: gopnik*

- **Frame count limit**: 130 frames
  - Maximum stable frame count for RTX 4090
  - *From: Govind Singh*

- **Frame rate doubling**: 48fps instead of 24fps
  - To get correct 5 second duration instead of 10 seconds
  - *From: MOV*

- **--reserve-vram**: 4-10 depending on GPU
  - Prevents OOM by giving ComfyUI's memory system a buffer
  - *From: seitanism*

- **Text encoder device**: CPU
  - Prevents model reloading when changing prompts, avoiding double generation time
  - *From: yi*

- **Temporal upscaler frame rates**: Sampler: 24fps, Save video: 48fps
  - Proper frame rate handling for temporal upscaling
  - *From: yi*

- **Tile size for VAE decode**: 384
  - Prevents OOM on large resolutions like 832x480
  - *From: patientx*

- **Video height**: Less than 1080
  - Better results for portrait generation
  - *From: mkupchik_lightricks*

- **videoInPlace strength**: 0.8-0.9
  - Better control over motion and image retention
  - *From: ucren*

- **I2V strength**: 0.6 instead of 1.0
  - Improves motion quality in image-to-video
  - *From: fearnworks*

- **CFG**: 1.0
  - Used with distilled LoRA for faster generation
  - *From: avataraim*

- **Steps**: 6-8 steps with distilled LoRA
  - Reduces generation time significantly
  - *From: avataraim*

- **--reserve-vram**: 4-6 GB
  - Prevents OOM errors on high VRAM systems
  - *From: Tyronesluck*

- **Image strength**: Under 0.3
  - If it doesn't move above this value, something else is wrong
  - *From: Kijai*

- **FPS**: 25
  - Standard setting, 23fps might cause issues
  - *From: Owlie*

- **VAE tile size**: 512
  - Using comfy native settings
  - *From: ucren*

- **VRAM reservation**: 4GB
  - Use --reserve-vram 4 startup argument for better memory management
  - *From: Kijai*

- **Frame rate**: 50 fps
  - Eliminates most artifacts compared to 24 fps
  - *From: Tonon*

- **Frames for temporal upscaling**: 301 frames
  - Proper frame count for temporal upscaling workflow
  - *From: AiAuteur*

- **Keyframe spacing**: 12 frames minimum
  - Needs at least 10-12 frame gaps between keyframes for smooth interpolation
  - *From: Kijai*

- **Steps for quality**: 15 steps with res2_s
  - Good balance of quality and speed
  - *From: PATATAJEC*

- **Sampler combination**: res2_s sampler with beta scheduler
  - Preferred combination for quality results
  - *From: mallardgazellegoosewildcat2*


## Concepts Explained

- **Sage attention**: Speed optimization that uses slightly more memory than SDPA but provides faster generation
  - *From: Kijai*

- **Audio latent multiplication**: Technique to modify audio components that affects video generation
  - *From: Kijai*

- **Noise injection**: Adding noise to input image to encourage motion in I2V generation
  - *From: Kijai*

- **Two-pass generation**: Generate at lower resolution first, then upscale - main source of speed improvement
  - *From: Moonbow*

- **Distilled vs Full model**: Distilled is optimized for speed, full model for quality. Can be combined in two-pass approach
  - *From: Benjimon*

- **Image strength**: Level of adherence to the first frame, 0 is ignore, 1 is reconstruct fully. Internally blends back with this coefficient after every step
  - *From: tavi.halperin*

- **Two-stage generation**: Stage 1 is base generation in lower res, stage 2 is shorter upscaling to larger res
  - *From: tavi.halperin*

- **LTXVSetAudioVideoMaskByTime**: Node for video extension, audio-to-video, video-to-audio, temporal inpainting. When it says 'mask' think 'edit'
  - *From: harelcain*

- **Distillation LoRA**: Creates spectrum of more/less distilled models - more distilled needs fewer steps, works with CFG=1 for 2x speedup, but has smaller variety and struggles with hard prompts
  - *From: harelcain*

- **Audio latents per second**: Fixed at 25 latents per second for audio, while video latents per second varies based on pixel frame rate
  - *From: harelcain*

- **Reserve VRAM**: How much memory in GB added to estimation for model activation temporary tensors, causes ComfyUI to offload enough weights to allow room
  - *From: Kijai*

- **Lowvram patches**: Indicates number of low VRAM optimizations applied, 0 means none applied
  - *From: BobbyD4AI*

- **Temporal vs Spatial upscaling**: Temporal upscaler works on time dimension, spatial on resolution - both needed to prevent latent misalignment
  - *From: Ada*

- **Temporal upscaler**: Converts 24fps video to 48fps, requires specific frame rate settings in workflow
  - *From: yi*

- **--reserve-vram**: ComfyUI startup flag that reserves VRAM buffer to prevent OOM when OS uses VRAM
  - *From: Kijai*

- **Bollywood bias**: LTX-2 model has strong training bias toward Bollywood content, often generating Indian people and dance scenes even with unrelated prompts
  - *From: ZombieMatrix*

- **videoInPlace strength**: Parameter controlling how much the video deviates from the input image
  - *From: ucren*

- **Solid mask value**: Increasing this value increases the noise in the generation
  - *From: theUnlikely*

- **Distilled LoRA**: LoRA that works with dev model to achieve faster generation with fewer steps
  - *From: avataraim*

- **LTXVAddGuide**: Node for keyframing that wraps logic for denoising parts of latents, tiling, extending. Not for looping video but for complex conditioning masks
  - *From: Dragonyte*

- **projections_only model**: Something needed to make the dualcliploader work, helps with model reloading issues
  - *From: Phr00t*

- **8n+1 frame format**: Frame count must be divisible by 8, plus 1 frame
  - *From: Scruffy*

- **Keyframe interpolation**: Adding new frames between input keyframes to create smooth motion
  - *From: Kijai*

- **Guide frames**: Non-black images that are added as keyframes for video latent control
  - *From: Kijai*

- **FP4 upcasting**: On non-Blackwell cards, FP4 models are automatically converted to higher precision
  - *From: Kijai*


## Resources & Links

- **Gemma 3 12B Q4 quantized** (model)
  - https://huggingface.co/google/gemma-3-12b-it-qat-q4_0-unquantized/tree/main
  - *From: Clint Hardwood*

- **SageAttention installation** (repo)
  - https://github.com/woct0rdho/SageAttention
  - *From: Lodis*

- **ComfyUI_ExtraModels for OOM fixes** (repo)
  - https://github.com/city96/ComfyUI_ExtraModels
  - *From: garbus*

- **LTX official workflows** (workflow)
  - https://github.com/Lightricks/ComfyUI-LTXVideo/tree/master/example_workflows
  - *From: Ada*

- **ComfyUI blog LTX tutorial** (tutorial)
  - https://blog.comfy.org/p/ltx-2-open-source-audio-video-ai
  - *From: garbus*

- **fp8 Gemma model** (model)
  - https://huggingface.co/GitMylo/LTX-2-comfy_gemma_fp8_e4m3fn/blob/main/gemma_3_12B_it_fp8_e4m3fn.safetensors
  - *From: Miku*

- **LTX training documentation** (repo)
  - https://github.com/Lightricks/LTX-2/blob/main/packages/ltx-trainer/README.md
  - *From: Doctor Diffusion*

- **ComfyUI LTX workflows** (workflow)
  - https://github.com/Lightricks/ComfyUI-LTXVideo/tree/master/example_workflows
  - *From: Miku*

- **ComfyUI blog workflow** (workflow)
  - https://blog.comfy.org/p/ltx-2-open-source-audio-video-ai
  - *From: el marzocco*

- **Arcane Jinx LoRA** (model)
  - https://civitai.com/models/1575738/ltxv-13b-lora-arcanejinx
  - *From: tarn59*

- **Kijai's audio workflow** (workflow)
  - https://www.reddit.com/r/StableDiffusion/comments/1q627xi/kijai_made_a_ltxv2_audio_image_to_video_workflow/
  - *From: 834759695939928064*

- **ComfyUI workflow templates** (workflow)
  - https://github.com/Comfy-Org/workflow_templates/blob/main/templates/video_ltx2_t2v.json
  - *From: yi*

- **Lightricks custom nodes** (repo)
  - https://github.com/Lightricks/ComfyUI-LTXVideo
  - *From: Lodis*

- **LTX-2 fp8 text encoder** (model)
  - https://huggingface.co/GitMylo/LTX-2-comfy_gemma_fp8_e4m3fn/discussions/1
  - *From: Lodis*

- **Detailer workflow** (workflow)
  - https://github.com/Lightricks/ComfyUI-LTXVideo/blob/master/example_workflows/LTX-2_V2V_Detailer.json
  - *From: tavi.halperin*

- **Correct Gemma weights** (model)
  - https://huggingface.co/google/gemma-3-12b-it-qat-q4_0-unquantized/tree/main
  - *From: pintz*

- **Spatial upscaler LoRA** (model)
  - https://huggingface.co/Lightricks/LTX-2-19b-IC-LoRA-Detailer
  - *From: Lodis*

- **ComfyUI GGUF support issue** (repo)
  - https://github.com/city96/ComfyUI-GGUF/issues/398
  - *From: Lodis*

- **SageAttention 2.2.0 for Windows** (tool)
  - https://github.com/woct0rdho/SageAttention
  - *From: Kijai*

- **Gemma 3 12B model files** (model)
  - https://huggingface.co/google/gemma-3-12b-it-qat-q4_0-unquantized
  - *From: pintz*

- **ComfyUI-LTXVideo example workflows** (workflow)
  - https://github.com/Lightricks/ComfyUI-LTXVideo
  - *From: 1376860387873390672*

- **Kijai's audio insert workflow** (workflow)
  - https://discord.com/channels/1076117621407223829/1309520535012638740/1458221075442958499
  - *From: ZombieMatrix*

- **Gemma 3 12B 4-bit quantized** (model)
  - https://huggingface.co/unsloth/gemma-3-12b-it-bnb-4bit/tree/main
  - *From: Hevi*

- **RES4LYF sampler pack** (node_pack)
  - https://github.com/ClownsharkBatwing/RES4LYF
  - *From: Shubhooooo*

- **LTX-2 CLI tools** (repo)
  - https://github.com/Lightricks/LTX-2
  - *From: wouter*

- **ComfyUI-LTXVideo workflows** (workflow)
  - https://github.com/Lightricks/ComfyUI-LTXVideo/tree/master/example_workflows
  - *From: Hevi*

- **Gemma fp8 for ComfyUI** (model)
  - https://huggingface.co/GitMylo/LTX-2-comfy_gemma_fp8_e4m3fn/tree/main
  - *From: Owlie*

- **LTX-2 separated components** (model)
  - https://huggingface.co/GitMylo/LTX-2-comfy_gemma_fp8_e4m3fn
  - *From: yi*

- **LTX 0.97 LoRA collection** (model)
  - https://civitai.com/collections/9825789
  - *From: NebSH*

- **LTX-2 prompting guide** (guide)
  - https://ltx.io/model/model-blog/prompting-guide-for-ltx-2
  - *From: BobbyD4AI*

- **VRAM fix tutorial** (guide)
  - https://www.reddit.com/r/StableDiffusion/comments/1q5k6al/fix_to_make_ltxv2_work_with_24gb_or_less_of_vram/
  - *From: 企鵝（50% CASH 50%GOLD）*

- **LTX Video 2 technical paper** (paper)
  - https://arxiv.org/pdf/2601.03233
  - *From: fearnworks*

- **ComfyUI-SCAIL-AudioReactive** (repo)
  - https://github.com/ckinpdx/ComfyUI-SCAIL-AudioReactive
  - *From: AJO*

- **LTX-2 Shinkai anime style LoRA** (lora)
  - https://civitai.com/models/1575844/ltxv-13b-lora-shinkai-anime-style?modelVersionId=1783229
  - *From: Vardogr*

- **LTX-2 GGUF test version** (model)
  - https://huggingface.co/smthem/LTX-2-Test-gguf/tree/main
  - *From: patientx*

- **Gemma FP8 model** (model)
  - https://huggingface.co/GitMylo/LTX-2-comfy_gemma_fp8_e4m3fn
  - *From: theUnlikely*

- **LTX-2 prompting guide** (guide)
  - https://ltx.io/model/model-blog/prompting-guide-for-ltx-2
  - *From: Benjimon*

- **Gemma FP8 model with projections** (model)
  - https://huggingface.co/GitMylo/LTX-2-comfy_gemma_fp8_e4m3fn
  - *From: Phr00t*

- **Qwen Image Edit 2511 Multiple Angles LoRA** (lora)
  - https://huggingface.co/fal/Qwen-Image-Edit-2511-Multiple-Angles-LoRA
  - *From: KingGore2023*

- **WAN2GP with LTX2 support** (tool)
  - https://github.com/deepbeepmeep/Wan2GP
  - *From: Tachyon*

- **LTX Video ComfyUI nodes** (repo)
  - https://github.com/Lightricks/ComfyUI-LTXVideo
  - *From: TK_999*

- **LTX-2 Spatial Upscaler** (model)
  - *From: Lumori*

- **Gemma FP8 text encoder** (model)
  - *From: maitr3ya*

- **Updated keyframe workflow** (workflow)
  - *From: Kijai*


## Known Limitations

- **I2V becomes horrors easily**
  - Image-to-video tests frequently produce disturbing results
  - *From: Cubey*

- **Bad with basic anatomy**
  - Model struggles with human anatomy, especially when not trained on nudity
  - *From: dj47*

- **Can't do people turning around**
  - Gets back-to-front mutation horrors, heads don't spin with body
  - *From: ucren*

- **Stiff on non-realistic content**
  - Tends to be very stiff on anything that's not realistic
  - *From: Moonbow*

- **Vertical generations are very repetitive**
  - Portrait orientation produces repetitive content
  - *From: TK_999*

- **Slideshow effect in I2V**
  - Still image zooming effect when insufficient noise or action
  - *From: Lumi*

- **Dialog prompt limits**
  - Definite limit to how much dialog you can stuff into prompts
  - *From: TK_999*

- **Memory leaks requiring restarts**
  - Occasional memory errors requiring manual ComfyUI restart
  - *From: Moonbow*

- **High RAM usage during VAE decode**
  - Can cause BSOD at higher resolutions, 1920x960 242 frames uses extreme RAM
  - *From: Tachyon*

- **Inconsistent subtitle generation**
  - Can generate subtitles but not consistently
  - *From: Moonbow*

- **Camera movement artifacts**
  - Issues with camera pulling back while background remains static
  - *From: Clint Hardwood*

- **Warping/garbling in fast motion**
  - Quality issues with fast movement and thin lines
  - *From: Ruairi Robinson*

- **Poor understanding of military equipment**
  - Model doesn't know what B-17 bombers or flak guns look like
  - *From: Tachyon*

- **Face distortion in low resolution**
  - Faces always seem to distort a bit, especially at lower resolutions
  - *From: Q-*

- **Native workflow missing some nodes**
  - LoopingSampler and some detailer nodes not available in native ComfyUI
  - *From: tavi.halperin*

- **Temporal upscaler sync issues**
  - Temporal upscaler causes lip sync desynchronization
  - *From: Xor*

- **Audio cutting off**
  - Audio cuts off at halfway point in longer generations due to fps mismatch
  - *From: Grimm1111*

- **Unprompted NSFW outputs**
  - Model generates random nudity even when prompting for clothes, particularly in I2V when zooming out from portraits
  - *From: Kijai*

- **Face distortion in wider shots**
  - Faces get distorted in wider video shots, quality degrades with movement
  - *From: Choowkee*

- **Motion smudginess**
  - Clear when still but gets smudgy during movement, more than normal motion blur
  - *From: Owlie*

- **SageAttention 3 quality degradation**
  - Serious quality degradation, not recommended even for Blackwell cards
  - *From: Kijai*

- **Text generation reliability**
  - Cannot reliably write text on screen
  - *From: Dever*

- **Heavy compression artifacts**
  - Any model with heavy compression like LTX2 and Sora2 shows smudginess during motion
  - *From: yi*

- **Latent RGB preview not working**
  - Latent space is too packed - super low res and only every 8th frame, not useful for monitoring progress
  - *From: Kijai*

- **Indian/Bollywood bias**
  - Model outputs Indian people frequently due to training dataset containing old Bollywood movies
  - *From: yi*

- **Memory management issues**
  - Model reloads every time even with same prompt, unlike other models
  - *From: yi*

- **Portrait video generation issues**
  - Many users report zero movement in portrait aspect ratio generations
  - *From: xdestroyer*

- **Strong Bollywood training bias**
  - Model frequently generates Indian people and Bollywood-style content regardless of prompt
  - *From: ZombieMatrix*

- **I2V often results in zero movement**
  - 90% of image-to-video results show no movement regardless of aspect ratio
  - *From: boop*

- **Character drift in audio-driven animation**
  - Mouth movements can be exaggerated and drift from initial character likeness
  - *From: ucren*

- **Ethnicity specification challenges**
  - Model struggles with generic ethnicity terms, requires specific country-based descriptors
  - *From: ZombieMatrix*

- **Poor 2D animation performance**
  - Model struggles with 2D animation compared to 3D CGI, may need LoRA training
  - *From: TK_999*

- **Start image retention issues**
  - Model tends to ignore input images and do text-to-image instead
  - *From: AJO*

- **I2V significantly slower than T2V**
  - Image-to-video generation 4x slower or worse than text-to-video
  - *From: Phr00t*

- **4K generation doesn't scale well with default settings**
  - Default scheduler settings don't work well for 4K resolution
  - *From: Kijai*

- **Desaturation issues in 4K first second**
  - 4K generations tend to desaturate in the first second, not matching reference image
  - *From: Nemlet17*

- **Audio sync issues with temporal upscaling**
  - Temporal upscale latent model/node doesn't know how to upscale audio latents properly
  - *From: ucren*

- **Character consistency problems**
  - No consistency past the first image, doesn't remember faces if they turn away and back, extending is impossible
  - *From: AJO*

- **Poor performance with anime/2D content**
  - Side padding trick not working for anime characters, 2d comic and anime does not perform well
  - *From: KingGore2023*

- **Model overtrained on static images**
  - Too much data with static, slowly moving images worked like poison for movement
  - *From: Mngbg*

- **Audio cuts out at halfway point**
  - In T2V generations, audio stops at exactly 10 seconds even with longer prompts
  - *From: Grimm1111*

- **Vertical images give unpredictable results**
  - Audio workflow especially affected, horizontal/square images work better
  - *From: Owlie*

- **Keyframe interpolation needs minimum spacing**
  - Won't create motion if frames are too close together, needs at least 10 frame gaps
  - *From: Kijai*

- **High RAM usage**
  - Hits pagefiles hard, making it difficult to use frequently
  - *From: boop*

- **Audio sync issues with temporal upscaler**
  - Temporal upscaler works for visual but not audio samples, requires manual alignment
  - *From: ucren*

- **Getting slideshows frequently**
  - 50% of generations result in slideshows instead of smooth motion
  - *From: Zueuk*


## Hardware Requirements

- **3090 generation length**
  - Can generate up to 4.5 seconds, sometimes 121 frames but OOMs, safe at 81 frames
  - *From: dj47*

- **5090 performance benchmark**
  - 361 frames I2V at 1280x720 in 35 seconds (4.46s/it)
  - *From: Kijai*

- **Sub-4GB VRAM for 5 seconds**
  - If 5 seconds works with <4GB, 10 seconds easily fits 12GB
  - *From: Kijai*

- **12GB VRAM capability**
  - Someone with 12GB managed 10 seconds at 720p
  - *From: Lodis*

- **64GB+ system RAM recommended**
  - Less than 64GB will use pagefile heavily on Windows
  - *From: Moonbow*

- **Apple Silicon compatibility**
  - Works perfectly with tiled VAE decode, faster than T2V, half the runtime
  - *From: buggz*

- **12GB VRAM minimum**
  - Can run on 12GB VRAM cards with proper setup
  - *From: Miku*

- **4GB VRAM possible with high RAM**
  - Works with 4GB VRAM if sufficient system RAM available
  - *From: Tachyon*

- **48GB RAM recommended**
  - For 4090 16GB VRAM laptop setup
  - *From: randomanum*

- **16GB VRAM comfortable**
  - No problem running full bf16 model and text encoder
  - *From: Benjimon*

- **High RAM for higher resolutions**
  - More system RAM needed for VAE decoding at higher res/longer videos
  - *From: Tachyon*

- **Minimum VRAM**
  - Works down to 4GB VRAM as tested by Kijai
  - *From: Lodis*

- **Recommended setup example**
  - RTX 3090 with 128GB RAM works well
  - *From: NC17z*

- **Speed benchmark**
  - 363 seconds generation time at 1280x720 with some artifacting
  - *From: Tachyon*

- **Model sizes**
  - FP8 model is 25GB, spatial/temporal LoRAs are 2GB, other LoRAs ~300MB
  - *From: Hevi*

- **50 series optimization**
  - FP4 works especially well on RTX 50 series GPUs
  - *From: comfy*

- **VRAM for 720p generation**
  - FP8 distilled model generates 720p in ~1 minute
  - *From: Lodis*

- **3090 I2V performance**
  - 1280x704 with fp8+distill LoRA: 383 seconds for 121 frames, ~40GB RAM usage for 241 frames
  - *From: Hevi*

- **3090 music video generation**
  - 640x352 resolution, 155 seconds for 28-second video (~700 frames)
  - *From: ZombieMatrix*

- **5060 TI performance**
  - 240 seconds generated in 11 minutes with 16GB VRAM
  - *From: Jumper*

- **Frame scaling performance impact**
  - 121 frames: 120 seconds, 242 frames: 1200 seconds - 10x slower for double frames
  - *From: gopnik*

- **RAM requirements**
  - 32GB+ RAM recommended, 16GB can cause swapping issues with Gemma model loading
  - *From: yi*

- **RTX 4090 VRAM management**
  - Needs --reserve-vram 4-6 GB, can run distilled fp8 model with proper settings
  - *From: BobbyD4AI*

- **Windows memory handling**
  - Windows automatically uses shared memory to prevent crashes, disabling swap file causes instability
  - *From: Kijai*

- **fp8dev model compatibility**
  - Only fp8dev model works reliably on RTX 4090, other models cause ComfyUI crashes
  - *From: avataraim*

- **RAM vs VRAM performance**
  - RAM speed doesn't matter for video models, even slow JEDEC standard RAM performs well
  - *From: seitanism*

- **RTX 4090 24GB VRAM with 64GB RAM**
  - Still experiences OOM issues, requires --reserve-vram flag
  - *From: avataraim*

- **RTX 5090 with 192GB system RAM**
  - Experiences random OOM on default workflow, needs --reserve-vram 6 or higher
  - *From: D'Squarius Green, Jr.*

- **RTX 4070 Ti S 16GB VRAM / 64GB RAM**
  - Confirmed working by multiple community members
  - *From: ZombieMatrix*

- **RTX 3090**
  - Works better than RTX 4090 in some cases according to user experience
  - *From: Hevi*

- **RX 6800 with ROCM on Windows**
  - Works with fp8 model and fp8 gemma, generation fast but VAE decoding takes time
  - *From: patientx*

- **4K generation**
  - Works on 4090 with proper VRAM management and offloading
  - *From: Kijai*

- **Long video generation**
  - 5090 with 363 frames at 720p works, 273 frames at 1280x720 confirmed
  - *From: VK (5080 128gb)*

- **OOM prevention**
  - Need --reserve-vram 4-6 even on high-end systems like 5090
  - *From: Tyronesluck*

- **RAM optimization**
  - Systems with less than 48GB RAM should use --no-cache argument
  - *From: Vardogr*

- **Second pass optimization**
  - --reserve-vram 5 reduced second step from 30 secs per iteration to 5
  - *From: 企鵝（50% CASH 50%GOLD）*

- **VRAM usage**
  - RTX Pro 6000: 110 sec for 720P 30FPS generation, can generate 1080p 241 frames without OOM
  - *From: KingGore2023*

- **Memory performance**
  - With 4090 + 128GB RAM: super fast with offload enabled
  - *From: Juan Gea*

- **High-end performance**
  - RTX 5090: 10 second videos generated in about 200 seconds
  - *From: particle9*

- **Mid-range performance**
  - 16GB VRAM, 64GB RAM: 2 minutes for 720p generation with distilled version
  - *From: RegularRacoon*

- **RTX 6000 for 1080p 50fps**
  - High-end GPU needed for best quality 1080p generation at 50fps
  - *From: Tonon*

- **24GB VRAM**
  - Multiple users working with 24GB VRAM, need high system page file
  - *From: Owlie*

- **48GB VRAM still uses shared RAM**
  - Even with 48GB VRAM, shared RAM usage goes to huge levels
  - *From: maitr3ya*

- **32GB RAM challenges**
  - Difficult to run on 32GB system RAM, needs --cache-none and disabled pinned memory
  - *From: JUSTSWEATERS*


## Community Creations

- **Noise injection node** (node)
  - Adds noise to input images to prevent slideshow effect
  - *From: Kijai*

- **Sage patch node** (node)
  - Alternative to command flag for enabling sage attention
  - *From: Kijai*

- **Force/Set Clip Device node** (node)
  - Override clip device assignment when forced to CPU
  - *From: Xor*

- **fp8 Gemma text encoder** (model)
  - Optimized fp8 version of Gemma text encoder for faster loading
  - *From: Miku*

- **Sigma visualization node** (node)
  - Ported from wrapper to KJNodes, demystifies what LTX scheduler does
  - *From: Kijai*

- **Audio VAE loader with dtype selection** (node)
  - Custom VAE loader supporting audio VAE with dtype options
  - *From: Kijai*

- **LTX-2 separated model components** (model)
  - Extracted VAEs, projections, vocoder to work with native ComfyUI nodes
  - *From: GitMylo*

- **Audio reactive pose control workflow** (workflow)
  - Combines SCAIL audio reactive nodes with LTX-2 pose control
  - *From: burgstall*

- **First LTX-2 LoRA** (lora)
  - Community member trained first LoRA for LTX-2
  - *From: Ada*

- **Shinkai anime style LoRA** (lora)
  - Anime style LoRA for LTX-2 available on Civitai
  - *From: Vardogr*

- **Alternative keyframe node** (node)
  - Images that are not black are added as keyframes, cleaner way to add multiple keyframes
  - *From: Kijai*

- **Batch keyframe processing** (workflow)
  - Method for processing multiple keyframes with proper empty frame spacing
  - *From: Kijai*


---

# LTX Chatter - January 8-15, 2026

# Ltx Chatter Knowledge Base
*Extracted from Discord discussions: 2026-01-08 to 2026-01-16*


## Technical Discoveries

- **SDE samplers require 1000+ steps for proper convergence**
  - Over 1,000 steps with SDE sampler is how diffusion/flow models are meant to be used. Around 1000 steps is what it takes to converge a noisy SDE with flow models, tested on Flux
  - *From: mallardgazellegoosewildcat2*

- **Temporal upscale lora doubles frames through interpolation**
  - The temporal upscale lora actually doubles the frames (interpolates), so frame count in video combine node needs to be 2x when using it
  - *From: Grimm1111*

- **Frame count rule is 8n+1 for total frames**
  - Frames need to be divisible by 8, plus 1 frame. This applies to frame_count (total number of frames), not FPS
  - *From: buggz*

- **Seed hunting can be more effective than high step counts**
  - Getting more seeds in can help more than doing many steps
  - *From: mallardgazellegoosewildcat2*

- **Native 1080p uses 4x more RAM than upscaled 1080p**
  - Raw 1080 generation uses about 4x the RAM compared to generating at lower resolution and upscaling
  - *From: Kiwv*

- **VRAM debug nodes can solve slowdown issues**
  - Placing VRAM debug nodes between text encoder and ksampler, and after video generation clears memory and maintains consistent 2s/it speeds
  - *From: Phr00t*

- **Abliterated Gemma model works with LTX**
  - User successfully created and tested an abliterated version that adheres better to certain prompts
  - *From: Kiwv*

- **FP4 projections model can work in CLIP encoder**
  - Using ltx-2-19b-dev-fp4_projections_only.safetensors in DualClipLoader can help with VRAM issues
  - *From: JUSTSWEATERS*

- **Spatial upscaler may not need distilled LoRA**
  - Testing showed disabling distilled lora in upscaler route with 20 steps/cfg 4 produced results
  - *From: TK_999*

- **Separating VAE from model provides better control and avoids duplication**
  - VAE separated from checkpoint gives more control and doesn't need duplication for every model, plus can be used for VAE pre-caching for trainers
  - *From: yi*

- **CRF/LTXVPreprocess adds compression artifacts to bridge train-test gap**
  - Adds h.264-like compression artifacts to pristine images to prevent static/frozen I2V results by bridging gap between training on real video frames vs pristine T2I images
  - *From: 976496720370348032*

- **Sigmas are animation curves**
  - Realization that sigmas function as animation curves for video generation
  - *From: JUSTSWEATERS*

- **Variable latent compression rates being developed**
  - Future versions will have variable latent compression rates or variable latent spaces, still WIP. Latent temporal upscaler works against temporal compression by spreading over double the latents in time axis
  - *From: 976496720370348032*

- **Full prompting of audio content improves audio generation quality**
  - When using audio continuation, prompt for the complete text that will be spoken in the final video, including what was said in the audio prefix that's being kept
  - *From: 976496720370348032*

- **Non-distilled models perform significantly better than distilled versions**
  - 30 steps cfg 4.0 on undistilled fp8 shows much bigger quality difference than expected compared to distilled versions
  - *From: Kijai*

- **LTX Video 2 can be used effectively for upscaling other model outputs**
  - Using LTX to upscale Wananimate generations to 1080p creates a 'killer combo'
  - *From: David Snow*

- **Audio continuation works by model attending to masked audio and video latents**
  - The model attends to the audio latents that are left masked and to the video latents too for voice matching
  - *From: 976496720370348032*

- **48 FPS significantly improves I2V quality by fixing temporal compression issues**
  - Fixes smudginess and glitchy artifacts in fast moving frames for I2V. Better than temporal upscaler.
  - *From: Ada*

- **LTX-2 has impressive prompt adherence for complex sequences**
  - Can handle complex prompts with dialogue and multiple actions: 'character x does that, then says:"blablabla", then turns around and goes somewhere and picks up a book, then says:"etcetc" then the character jumps out a window' and executes everything correctly in a 20s video
  - *From: seitanism*

- **Spatial inpainting is possible with LTX-2**
  - Can use spatial_mask input to generate parts of frames/all frames. Different from temporal inpainting which regenerates sections of video/audio.
  - *From: 976496720370348032*

- **Model supports frame counts of 8k+1 format**
  - Frame count must be multiple of 8, plus 1: 1, 9, 17, 25... (8k+1 for k in N)
  - *From: 976496720370348032*

- **Full attention across all video latents enables true 20-second context**
  - Unlike AnimDiff's 16 frame context, LTX-2 provides full attention between all video latents up to ~484 frames (20 seconds)
  - *From: 976496720370348032*

- **LTX-2 struggles with non-upright character poses**
  - Model is completely overwhelmed with characters doing handstands or similar non-standard poses
  - *From: seitanism*

- **Disabling sage attention patch and torch compile can help with OOM issues**
  - Juan Gea found that after disabling these features, sampling worked better and reduced memory pressure
  - *From: Juan Gea*

- **Text encoding can use up to 50GB RAM with fp8 model**
  - This seems excessive for a 12B model but is currently happening
  - *From: CDS*

- **Canceling and restarting workflow during ksampler step makes inference 12x faster**
  - 100% repeatable and reliable method - faster to cancel then restart than let it complete
  - *From: Phr00t*

- **LTX2 has automatic padding capability for video continuation**
  - Kijai added option to pad input frames automatically - if you input 81 frames and set end time to 10s, it will create new frames to reach that duration and mask them out for extension
  - *From: Kijai*

- **Same seed produces extremely similar results even at different resolutions**
  - When using same seed and settings but just increasing resolution, the model generates the same video content just sharper
  - *From: seitanism*

- **CFG causes significant VRAM increase**
  - CFG mode causes batched processing which increases VRAM usage by 4GB compared to CFG 1.0
  - *From: Kijai*

- **Model can handle negative frame positioning for reference**
  - Negative values in frame positioning place reference latents 'in the past' using positional encodings, not Python-style indexing
  - *From: 976496720370348032*

- **fp8 distilled model has better audio quality**
  - fp8 distilled doesn't have the tinny sound that the regular fp8 model has
  - *From: David Snow*

- **Sigma values can be used as animation curves**
  - Sigmas could be used as like an animation curve for controlling animation timing
  - *From: JUSTSWEATERS*

- **Custom text encoders can significantly change output**
  - Using different text encoders like antislop models produces notably different results for the same prompt
  - *From: Kiwv*

- **LTX Video 2 inpainting works well**
  - Inpainting functionality produces good results that are hard to distinguish from original content
  - *From: Hashu*

- **Samplers/Schedulers affect lipsync in I2V**
  - Using DDIM sampler in first KSampler improves lipsync, default settings were producing no lipsync
  - *From: Elvaxorn*

- **LTX-2 performs better with manual sigmas than basic schedulers**
  - Manual sigmas provide better results compared to BasicScheduler or LTXVScheduler
  - *From: yi*

- **Distill LoRA works with 20 steps, full model needs 40 steps**
  - 20 steps only works if you include the distill lora for stage 2, otherwise 40 steps is needed for full model
  - *From: psylent_gamer*

- **VAE encoding uses significant VRAM**
  - Encoding 121 frames at 1024x1024 uses like 15GB VRAM
  - *From: Kijai*

- **FP8 distill vs full model quality difference**
  - Full model provides significantly better quality than distilled version, especially for consistency
  - *From: psylent_gamer*

- **Image compression factor can fix motionless video issues**
  - Increasing image compression factor helps add motion to videos while maintaining quality, works even without camera LoRA
  - *From: 1100803024298975263*

- **48 fps generation reduces artifacts**
  - Generating at 48fps instead of 24fps can help with sharpness and reduce blurry artifacts
  - *From: Ada*

- **Perfect input images cause motionless videos**
  - When input image is too perfect with no blur, the generated video becomes motionless, especially in portraiture
  - *From: 1100803024298975263*

- **Two-pass procedure with distill LoRA**
  - Advantage of distill LoRA is doing 20 steps undistilled, then 3 steps with latent upscalers + LoRA
  - *From: ZeusZeus (RTX 4090)*

- **Q8 GGUF is better than fp8**
  - Q8 provides better quality than fp8, though it's slower on 40xx series cards and above
  - *From: Kijai*

- **Distilled model produces blurry faces**
  - LTX2 distilled model tends to generate blurry or out-of-focus faces, feels like focus issues rather than motion blur
  - *From: Kijai*

- **FP8 scaled is closest to BF16 quality**
  - General motion and structure wise, FP8 scaled performs most similarly to BF16
  - *From: Kijai*

- **NAG (Negative Attention Guidance) works with LTX Video 2**
  - Without NAG prompt, jeep was green, with NAG it changed color as expected
  - *From: Kijai*

- **Distill lora acts as lightx2v equivalent**
  - Consider the distill lora as the lightx2v for LTX
  - *From: Kijai*

- **Audio upscaler AudioSR shows no notable difference**
  - Testing showed no improvements when using AudioSR for audio enhancement
  - *From: toxicvenom117*

- **Higher FPS reduces blurriness**
  - You can avoid blurriness to some extent by increasing the FPS value
  - *From: KingGore2023*

- **NAG (Negative Audio/visual Guidance) now works with LTX Video 2**
  - Can add negative prompts like 'cartoon' to avoid unwanted styles, or 'music' to remove background music. Works similarly to how it did with Wan
  - *From: Kijai*

- **Can adjust distill strength even when using the distilled model**
  - Previously thought this wasn't possible, but distill strength can be modified for quality tuning
  - *From: Kijai*

- **FP8 scaled Gemma 3 text encoder available**
  - New fp8_scaled version is closer to bf16 quality than normal fp8, requires latest ComfyUI commit
  - *From: Kijai*

- **Enhance-A-Video works with LTX Video 2**
  - Universal method originally for CogVideoX, applied only to video attention layers, weaker effect than other models
  - *From: Kijai*

- **Using dev model with distilled LoRA at negative weight (-0.3 to -0.6) fixes plastic skin issue**
  - Loading distill fp8 model with distill LoRA at -0.60 weight removes shiny plastic skin appearance from humans while maintaining speed benefits
  - *From: David Snow*

- **Embedding connectors are different between dev and distill models**
  - The embeddings_connector weights are completely different between dev and distill models, giving almost completely different results when swapped
  - *From: Kijai*

- **SLG works with LTX-Video 2**
  - SLG guidance works but has huge effect on block 1, block 2 seems good with subtle effects, stronger near start of blocks
  - *From: Kijai*

- **Removing negative prompts can improve results**
  - Removing all negative conditioning completely fixed a t2v generation that wasn't working properly
  - *From: BobbyD4AI*

- **Distil LoRA at negative weight fixes shiny skin and AI contrast issues**
  - Using distil LoRA on upscale pass only at -0.5 weight reduces shiny plastic look and overly contrasted AI appearance. Don't use on first pass as it can affect motion.
  - *From: David Snow*

- **LTXVAddGuideMulti node ignores frame_idx parameter**
  - When adding guide for image at index 16, it adds at the end and ignores the frame_idx number
  - *From: Phr00t*

- **Audio-only LoRA training works extremely well and fast**
  - Training runs at 2 steps per second on RTX5090
  - *From: mamad8*

- **New Comfy-Org Gemma models have better accuracy than fp8_scaled**
  - fpmixed and fp4_mixed versions target 95% and 90% fp4 layers respectively with minimal loss
  - *From: comfy*

- **Distilled model produces much better results than non-distilled**
  - User reported getting much better results switching from non-distilled to distilled model
  - *From: Gleb Tretyak*

- **Audio quality improves after upscaler pass**
  - Sound becomes cleaner after upscaling, especially music clarity
  - *From: N0NSens*

- **Dev model produces better audio than distilled model**
  - Dev model after upscaler produces much better sound quality than distilled model after upscaler
  - *From: N0NSens*

- **VAE tiled decoding causes flashing/flickering**
  - Flash/flickering always at same point in videos caused by VAE decode (Tile), doesn't happen with regular VAE decode
  - *From: mamad8*

- **I2V mask level affects movement**
  - If it doesn't move under 0.3 mask level then something else is broken
  - *From: Kijai*

- **CFG works fine with distilled model for few steps**
  - CFG for few steps while using distill seems to work fine, especially with SLG
  - *From: Kijai*

- **LTX2 uses modality-aware classifier-free guidance with separate control parameters**
  - st controls text guidance strength, sm controls cross-modal (audio↔video) guidance strength. Default values: Video st=3, sm=3; Audio st=7, sm=3
  - *From: Chandler ✨ 🎈*

- **Keyframe conditioning uses reference latent technique with positional embeddings**
  - Model attends to dedicated new latent frame matching the set index, then frame is discarded using LTXCropGuides. Doesn't put keyframe directly into tensor due to latent space architecture
  - *From: 976496720370348032*

- **Audio latents are fixed at 25 per second, video latents are 8 pixel frames per latent frame**
  - Video pixel frames per second is variable, so audio latent initialization needs to know pixel frame count and fps to match properly
  - *From: 976496720370348032*

- **Detail daemon produces floating orbs and particles as byproduct**
  - Particles are intentional motion-generating effect but can be excessive
  - *From: David Snow*

- **Using -1 frame index creates looping videos**
  - When last frame is similar/identical to first frame, -1 index produces looping generations
  - *From: Gleb Tretyak*

- **GGUF models work with multiple loaders**
  - Unsloth GGUF models work but require their specific loader
  - *From: cocktailprawn1212*

- **Distilled LoRA can be used with full model at positive values**
  - Examples show dev model + distilled lora at positive values working well
  - *From: Hashu*

- **Distilled model can use negative LoRA values**
  - Distilled model + distill lora at negative values produces good results
  - *From: Hashu*

- **res_2s with 8 steps performs better than 4 steps**
  - res_2s with 8 steps is 100% better than 4 steps but twice slower
  - *From: N0NSens*

- **cfg > 1 with 'music' in negative prompt removes unwanted music**
  - Using cfg higher than 1 with 'music' in negative prompt successfully prevents unwanted music generation
  - *From: foxydits*

- **LTX2 has VRAM limits even with offloading**
  - VRAM offload can only offload model weights, but if activations don't fit in 24GB then generation size is still too large (1080p 480 frames failed)
  - *From: Kijai*

- **Close-up portrait prompts trigger image zoom behavior**
  - Using 'A close-up portrait' in T2V prompts causes the model to generate static images with zoom effects instead of proper video
  - *From: hicho*

- **LTX2 can generate high-quality still images**
  - The close-up portrait 'bug' actually generates very high quality images, can be used as an image generator workflow
  - *From: hicho*

- **Quotation marks in prompts improve lip sync**
  - Using quotation marks around spoken dialogue in prompts helps generate better lip movement
  - *From: hicho*

- **Video extension works like inpainting**
  - Video extension is analogous to image inpainting - describing the whole video including unchanged parts helps the model find better fitting solutions
  - *From: Kijai*

- **Film grain helps with I2V motion - the more grain, the more likely the image will move**
  - Adding film grain to images before I2V processing significantly improves motion generation
  - *From: Elvaxorn*

- **Audio start time affects video motion in I2V**
  - Having audio start time at 0.0 screws up motion. Audio start time should be equal to or higher than video start time (e.g., 0.2) to prevent static video at beginning
  - *From: Elvaxorn*

- **JPEG compression adds macroblock noise similar to MPEG video compression**
  - Model likely learned during training that this macroblock noise is associated with cinematic sequences
  - *From: 138332118890708992*

- **Spatial audio masking works**
  - Can mask out specific characters in audio while keeping others
  - *From: Kijai*

- **PyTorch 2.9.0+cu130 vs 2.8.0+cu129 performance difference**
  - Full HD 81 frames render time: 201 sec vs 89 sec on 2.9.0+cu130
  - *From: protector131090*

- **LTX2 has severe I2V VRAM issues due to per-token timestep handling**
  - I2V uses gigabytes more VRAM than T2V, similar to WAN 5B issue with huge intermediate timestep tensors
  - *From: Kijai*

- **Different embedding connectors exist for dev vs distilled models**
  - Dev and distilled models have different embedding_connector files, mixing them produces different outputs
  - *From: Kijai*

- **Q8 distilled model performs better than Q8 dev + distilled LoRA**
  - Initial testing shows Q8 distilled gives better results than using Q8 dev with distilled LoRA for I2V use cases
  - *From: Choowkee*

- **LTX2 can accept video input for video-to-video generation**
  - Can feed video directly into LTXVImgToVideoInplace node, works with 721 frames for continuous video generation
  - *From: ZombieMatrix*

- **NSFW content generation varies with text encoders**
  - Stock gemma prevents touching underwear, while abliterated gemma allows touching underwear and certain provocative motions
  - *From: Choowkee*

- **Video compression helps with motion**
  - LTX uses video compression artifacts to derive motion, so adding compression to a scene can drive up the amount of motion it interprets
  - *From: ZombieMatrix*

- **Memory optimization breakthrough for I2V**
  - Can now run 1920x1088x193 I2V with no extra reserve VRAM on 4090, previously needed 7GB reserve
  - *From: Kijai*

- **Upscale sampler improves audio quality**
  - Both upscale sampler and step count can definitely clean up the audio
  - *From: garbus*

- **Distilled LoRA provides massive speedup**
  - Can be used with both Q4 GGUF and regular models, provides significant quality improvement especially at 8 steps
  - *From: Kiwv*

- **Audio quality is linked to resolution**
  - Higher resolutions like 1920x1088 give better audio quality than lower resolutions like 960x544
  - *From: 568465354158768129*

- **Frame rate affects video quality significantly**
  - 50fps produces noticeably better quality than 24fps, smoother animations at higher resolutions
  - *From: Choowkee*

- **Resolution affects motion quality**
  - 960x544 produces almost static motion, while higher resolutions have smoother animations
  - *From: 568465354158768129*

- **1440x800 is minimum resolution for lip sync**
  - Below this resolution, lip sync quality degrades significantly
  - *From: 568465354158768129*

- **50fps produces much faster action execution and more fluid motion with micro expressions not present in 24fps versions**
  - 50fps shows lots of little micro expressions that aren't there on the 24fps version, definitely more fluid
  - *From: Choowkee*

- **Resolution affects I2V results significantly - higher resolution doesn't always mean better quality**
  - 1920x1080 resolution minimum recommended, but changing resolutions is like changing the seed. Higher resolution does not mean the scene is actually better
  - *From: 568465354158768129*

- **Frame count changes can dramatically affect output quality**
  - Changing total frames from 151 to 153 made video much worse - miscalculating frames (151 instead of 153) produced better results
  - *From: 568465354158768129*

- **Random noise seed value has barely any noticeable effect in I2V**
  - Changing random noise_seed values had minimal impact, might have more effect on T2V but not tested yet
  - *From: 568465354158768129*

- **Distilled LoRA strength of 0.8 instead of 1.0 makes skin look less plastic**
  - Reducing distill lora value from 1.0 to 0.8 makes skin less plastic looking
  - *From: 568465354158768129*

- **Training dataset bias affects generation based on fps and resolution**
  - Different fps and resolution settings trigger different training data - 50fps suggests model was probably trained on 50-60 fps content
  - *From: 568465354158768129*

- **VRAM usage memory optimization for I2V**
  - Kijai's av_model.py modification drops I2V VRAM usage to near T2V levels, cuts VRAM use by ~1GB at higher resolutions
  - *From: Kijai*

- **Higher FPS can reduce motion artifacts**
  - 48-50 FPS generation shows less texture smearing and breaking, helps with motion jank
  - *From: David Snow*

- **First pass vs second pass quality differences**
  - First pass maintains better character consistency and skin quality, second pass often introduces latex-like skin appearance
  - *From: ラD.*

- **Audio loudness affects motion generation**
  - Louder audio files produce more movement in lip sync generations, quiet speech can produce static results
  - *From: protector131090*

- **av_model.py update provides significant speed improvements**
  - Latest av_model.py shows 38.6s vs 36.9s performance improvement, also faster generation at 299.80s vs 313.99s from 15 hours prior
  - *From: Choowkee*

- **Sage attention patch node works better than command line flag**
  - Using Kijai's patch node instead of --use-sage-attention flag resolves dtype errors and works properly
  - *From: Kijai*

- **Mixed precision text encoder gives better results**
  - Using the mixed precision TE from Comfy-Org/ltx-2 split_files/text_encoders should give better results than regular fp8
  - *From: TK_999*

- **Higher FPS improves quality for fast action**
  - Model gives higher quality at >40fps, especially need 40-50fps for fast action scenes to avoid morphing degradation
  - *From: nikolatesla20*


## Troubleshooting & Solutions

- **Problem:** Audio stopping halfway through video
  - **Solution:** When using temporal upscale lora, set frame count in video combine node to 2x because the lora interpolates and doubles frames
  - *From: Grimm1111*

- **Problem:** Image to video looks like slideshow
  - **Solution:** Adjust strength parameter - lower strength gives more motion but less adherence to original image
  - *From: gordo*

- **Problem:** Getting 'baked' look with too much CFG at 20 steps
  - **Solution:** Try disabling sage attention and fp16 accumulation
  - *From: NC17z*

- **Problem:** Kernel error on 2060
  - **Solution:** Fixed with latest kitchen version
  - *From: hicho*

- **Problem:** OOM issues with high resolution
  - **Solution:** Use reserve RAM setting (--reserve-vram) and ensure sufficient system RAM for offloading
  - *From: avataraim*

- **Problem:** OOM errors during generation
  - **Solution:** Use --reserve-vram 5 or higher, and try FP4 projections model in clip encoder
  - *From: TK_999*

- **Problem:** Model slowdown after first generation
  - **Solution:** Place VRAM debug nodes after text encoder and after video generation to clear memory
  - *From: Phr00t*

- **Problem:** Missing tokenizer in abliterated model
  - **Solution:** Include the model tokenizer in the file during conversion
  - *From: Kiwv*

- **Problem:** ComfyUI crashes during VAE decode
  - **Solution:** Try regular VAE decode instead of tiled, or reduce overlap from 4096
  - *From: Tachyon*

- **Problem:** Unpin errors in ComfyUI
  - **Solution:** Usually caused by custom nodes messing with model weights
  - *From: comfy*

- **Problem:** RuntimeError: Padding size should be less than corresponding input dimension
  - **Solution:** Set trim audio duration to not 0 - you're starting after the index start in the second node
  - *From: Q-*

- **Problem:** OOM errors on 4090 with 64GB RAM
  - **Solution:** Use --reserve-vram 2 (or higher) to offload more, or create 32GB swapfile, or use --lowvram --cache-none --reserve-vram 8
  - *From: NebSH, taoofai, tamilboy*

- **Problem:** CUDA locks every 4th run on 4090
  - **Solution:** Restart ComfyUI - no easy way to remove models yet, open PRs exist to fix issues
  - *From: Q-*

- **Problem:** Static image in I2V with no movement
  - **Solution:** Lower I2V strength to under 0.4, increase LTXVPreprocess strength value from 33 to higher, use more detailed prompts
  - *From: Kijai, 976496720370348032*

- **Problem:** Garbled faces in fast motion
  - **Solution:** Turn fps up, but user wanted 24fps specifically
  - *From: Benjimon, Ruairi Robinson*

- **Problem:** Audio VAE encode needs stereo audio
  - **Solution:** Use Audio Change Channels node or AudioBatch custom node to convert mono to stereo
  - *From: 976496720370348032, 421114995925843968*

- **Problem:** Portrait videos (832/1216) causing severe artifacts
  - **Solution:** Try smaller final resolution, use full model instead of distilled, or make shorter video. Portrait breaks more easily with high token count
  - *From: 976496720370348032*

- **Problem:** Videos freeze when using character mutations or out-of-distribution content
  - **Solution:** Use preprocessing (CRF), lower strength, and detailed prompting to help with frozen videos
  - *From: 976496720370348032*

- **Problem:** Character won't animate in I2V, tends toward realism
  - **Solution:** Try using pose control or other control signals, as the model may not identify animated characters well
  - *From: Juan Gea*

- **Problem:** Volume jumps significantly in audio continuation
  - **Solution:** Adjust audio levels, original audio becomes quiet compared to generated portion
  - *From: FUNZO*

- **Problem:** RuntimeError about tensors on different devices with prompt enhancer
  - **Solution:** Update ComfyUI to latest version, issue was fixed in recent update
  - *From: yi*

- **Problem:** OOM errors with Gemma3 in LTX custom node workflows
  - **Solution:** Use the native ComfyUI workflow instead, or enable VRAM reserve settings
  - *From: Juan Gea*

- **Problem:** FigureCanvasAgg tostring_rgb error in VisualizeSigmasKJ node
  - **Solution:** Just mute/disable this node as it's only for visualization
  - *From: NebSH*

- **Problem:** OOM errors on RTX 4090 with 24GB VRAM
  - **Solution:** Use --reserve-vram 4 to 6. Higher values significantly slow performance (10x slower at reserve-vram 10)
  - *From: protector131090*

- **Problem:** I2V crashes on 30xx series
  - **Solution:** Use FP8 models with specific combinations - shared working combo available
  - *From: The Shadow (NYC)*

- **Problem:** Motion freezing in V2V
  - **Solution:** Issue occurs because V2V compresses 4 frames to 1 latent, causing problems with fast moving scenes where 4 frames are very different
  - *From: 企鵝（50% CASH 50%GOLD）*

- **Problem:** Prompt enhancer causing errors in I2V
  - **Solution:** Disable/bypass the prompt enhancer in official workflows
  - *From: Juan Gea*

- **Problem:** Quality degradation with higher frame counts
  - **Solution:** Combined resolution+frames shouldn't exceed certain values. Either use many frames at low resolution or few frames at high resolution
  - *From: seitanism*

- **Problem:** Different checkpoints selected causing errors
  - **Solution:** Ensure same checkpoint is used across all model loaders - distilled vs dev fp8 mismatch causes issues
  - *From: Kagi*

- **Problem:** 4090 getting stuck on first custom ksampler with green bar
  - **Solution:** Use --reserve-vram 4 or higher, Juan Gea suggests at least 4-5, up to 10 with controlnet
  - *From: 391020191338987522, Juan Gea*

- **Problem:** OOM errors on second sampler
  - **Solution:** Use higher --reserve-vram values incrementally, disable sage attention patch and torch compile
  - *From: Juan Gea, seitanism*

- **Problem:** Sage attention error about tensor dtypes
  - **Solution:** Try without the startup argument - startup argument now overrides the patch node
  - *From: Kijai*

- **Problem:** Frozen/static results in I2V
  - **Solution:** Use LTXVPreprocess with high strength (33+), weaker conditioning in InPlace node, long detailed prompts, pose control if needed
  - *From: 976496720370348032*

- **Problem:** Mat1/mat2 error with text encoder
  - **Solution:** Update KJ nodes to nightly using 'switch ver', ensure correct connector type loaded (gemma must be first)
  - *From: Juan Gea, Kijai*

- **Problem:** Prompt enhancer causing censorship and no movement
  - **Solution:** Use llama.cpp server with prefill support, or disable prompt enhancer entirely
  - *From: Ada, Juan Gea*

- **Problem:** High VRAM usage with distilled LoRA
  - **Solution:** Issue was CFG causing batched mode, not the LoRA itself. Use CFG 1.0 to reduce VRAM by 4GB
  - *From: Kijai*

- **Problem:** Device mismatch error (cuda:0 and cpu)
  - **Solution:** Common when objects aren't on same device - need to move tensors to same location, often by encoding images to latents
  - *From: Scruffy*

- **Problem:** res_2s sampler error on Mac
  - **Solution:** Download RES4LYF pack or change sampler to euler_ancestral in both stages
  - *From: seitanism*

- **Problem:** Upscaling destroys lip sync
  - **Solution:** Use lower denoise (0.2) and lower shift (0.2-0.4), though results may still vary depending on face size
  - *From: dj47*

- **Problem:** LTXVGemmaEnhancePrompt node error: 'LTXAVTEModel_' object has no attribute 'processor'
  - **Solution:** Bypass the enhancer node
  - *From: Q-*

- **Problem:** Black fade appearing in generations
  - **Solution:** Try different prompts first, shouldn't be happening in the first place
  - *From: Kiwv*

- **Problem:** ComfyUI disconnecting with no errors during generation
  - **Solution:** Issue identified but no specific solution provided yet
  - *From: 140897652324827137*

- **Problem:** VAE encode/decode causing ghosting and duplicate images in V2V
  - **Solution:** VAE from LTX is confirmed buggy, issue persists even with tiled VAE decode
  - *From: 企鵝（50% CASH 50%GOLD）*

- **Problem:** Crash during clip loading
  - **Solution:** Use KJ's workflow version or load gemma with dual clip loader
  - *From: Michael Carychao*

- **Problem:** Static image outputs instead of video
  - **Solution:** Try lower resolution - gradually decrease so longest edge is 1024
  - *From: Gleb Tretyak*

- **Problem:** AttributeError: 'FigureCanvasAgg' object has no attribute 'tostring_rgb'
  - **Solution:** Matplotlib version issue, Kijai will add fallback for different versions
  - *From: psylent_gamer*

- **Problem:** RAM usage issues with LTX-2
  - **Solution:** Use --cache-ram with threshold or --cache-none for nuclear option, also try --disable-pinned-memory
  - *From: Kijai*

- **Problem:** Model crashes during tiled decode
  - **Solution:** Increase page size to 65GB made workflows bearable, doesn't crash during tiled decode anymore
  - *From: Tachyon*

- **Problem:** I2V results super saturated and plastic style
  - **Solution:** Add more noise to the image - if image is too perfect or synthetic, model behaves differently than with noisy or movie-like images
  - *From: Lodis*

- **Problem:** Slow I2V performance
  - **Solution:** Use --reserve-vram with values starting from 1 or 2
  - *From: Kijai*

- **Problem:** --reserve-vram parameter is in gigabytes
  - **Solution:** Use --reserve-vram 2 instead of 2048 - the parameter is in GB, not MB
  - *From: Kijai*

- **Problem:** ComfyUI crashes with 24GB VRAM
  - **Solution:** Use --cache-none flag, gemma 4-bit on CPU, and fp8 checkpoint. Try --reserve-vram flag
  - *From: onama*

- **Problem:** Audio artifacts in continue workflow
  - **Solution:** Set CFG to 4 with full fp8 model and 20-30 steps, or use distilled model with proper CFG settings
  - *From: ZeusZeus (RTX 4090)*

- **Problem:** Same video output with time node
  - **Solution:** Time node starts at 5 seconds but input is shorter - use padding node instead
  - *From: Kijai*

- **Problem:** GGUF models generate noise
  - **Solution:** Need ComfyUI-GGUF PR #399 to load metadata properly, or use vantage fork
  - *From: Kijai*

- **Problem:** VAE tiling artifacts visible as squares
  - **Solution:** Tiled VAE generates visible square artifacts with LTX, especially at higher resolutions like 2K
  - *From: David Snow*

- **Problem:** Slow second stage inference
  - **Solution:** Second stage at twice resolution should be slower but 160s/it at 99% VRAM suggests memory issues
  - *From: 411637464806195202*

- **Problem:** Line artifacts at high resolution
  - **Solution:** Width & height must be divisible by 32+1, frame count by 8+1. Stay below 1537x1537, use 1280x720 or 1080x1080
  - *From: Gill Bastar*

- **Problem:** AttributeError: 'VAE' object has no attribute 'latent_frequency_bins'
  - **Solution:** Update KJnodes or change version to 'nightly'
  - *From: Juan Gea*

- **Problem:** GGUF models need tokenizer support
  - **Solution:** Currently needs a PR https://github.com/city96/ComfyUI-GGUF/pull/399
  - *From: Kijai*

- **Problem:** VAE ghosting artifacts during encode/decode
  - **Solution:** Use temporal tiles during VAE encode and decode with overlap - don't use temporal_overlap=0
  - *From: 976496720370348032*

- **Problem:** Sage attention flag doesn't work with model
  - **Solution:** Don't use --use-sage-attention flag, use Kijai's sage patch node instead
  - *From: Kijai*

- **Problem:** OOM issues on RTX 5090
  - **Solution:** Use --reserve-vram flag, don't use --lowvram or --highvram
  - *From: Kijai*

- **Problem:** Memory management issues in ComfyUI
  - **Solution:** Use --reserve-vram instead of other memory flags
  - *From: Kijai*

- **Problem:** MelBandRoFormerSampler error on Mac
  - **Solution:** Use Mac-compatible fork: https://github.com/Brainkeys/ComfyUI-MelBandRoFormer-Mac/tree/main
  - *From: buggz*

- **Problem:** OOM errors with limited VRAM
  - **Solution:** Turn up VRAM reserve settings to prevent out of memory issues
  - *From: Gill Bastar*

- **Problem:** GGUFLoaderKJ 'dict' object has no attribute 'startswith'
  - **Solution:** Try updating KJNodes
  - *From: 162053387582439425*

- **Problem:** VAE loading crashes ComfyUI
  - **Solution:** Launch ComfyUI with --cache-none argument to confirm if it's RAM related issue
  - *From: Kijai*

- **Problem:** Text encoder connector missing error
  - **Solution:** Error occurs when connector is missing in text encoder setup
  - *From: Kijai*

- **Problem:** Mat1 and mat2 shapes multiplication error
  - **Solution:** Try --preview-method none in ComfyUI startup arguments
  - *From: yi*

- **Problem:** Audio becomes desynced when using temporal upscaling
  - **Solution:** Set source fps correctly - if source was 20fps, set upscale to 40fps, not 48fps
  - *From: Xor*

- **Problem:** Portrait/vertical video has jittery motion issues
  - **Solution:** General known issue with vertical video generation, developers mentioned portrait improvements planned for version 2.1
  - *From: TK_999*

- **Problem:** Plastic shiny skin on humans with distill model
  - **Solution:** Add distill LoRA to distill model at negative weight (-0.3 to -0.6) to reduce plastic appearance
  - *From: David Snow*

- **Problem:** FP4 not working
  - **Solution:** Update PyTorch to CUDA 13 version
  - *From: D'Squarius Green, Jr.*

- **Problem:** Model unloading when only changing prompts
  - **Solution:** Text encoder needs to run when prompts change, this is normal behavior
  - *From: Kijai*

- **Problem:** Tensor size mismatch error in LTX
  - **Solution:** Remove smZnodes extension
  - *From: Aergo*

- **Problem:** OOM issues on audio-image-to-video workflow
  - **Solution:** Reduce resolution and duration, avoid upscale nodes if VRAM limited
  - *From: Vérole*

- **Problem:** Audio not working in workflow with detailers
  - **Solution:** Detailers may be causing audio issues in workflow
  - *From: NC17z*

- **Problem:** ComfyUI failing to load after system crash
  - **Solution:** Delete all CUDA related software and Python installations, then reinstall fresh
  - *From: Charlie*

- **Problem:** Power Puter node 'IsNot not supported' error
  - **Solution:** Change 'is not' to '!=' or update rgthree version
  - *From: 411637464806195202*

- **Problem:** Static output in I2V
  - **Solution:** Lower I2V mask level - if it doesn't move under 0.3 then something else is broken
  - *From: Kijai*

- **Problem:** Enhance-a-Video not working properly with LTX2
  - **Solution:** Changes output too much, doesn't seem to burn like with other models, maybe because of audio attention - try video only
  - *From: Kijai*

- **Problem:** Black outputs when changing frame count
  - **Solution:** Too many frames can cause black outputs
  - *From: seitanism*

- **Problem:** input tensor must fit into 32-bit index math when decoding
  - **Solution:** Something becomes too large (like 1024x1024x297), exact cause unknown yet
  - *From: mamad8*

- **Problem:** Weight error with new nodes
  - **Solution:** Needs ComfyUI updated to specific commit bd0e6825e84606e0706bbb5645e9ea1f4ad8154d
  - *From: Kijai*

- **Problem:** Stylistic drift in I2V second pass
  - **Solution:** Happening in upscaler pass, related to distill lora usage
  - *From: David Snow*

- **Problem:** Expected mat1 and mat2 to have the same dtype, but got: c10::Half != c10::BFloat16
  - **Solution:** Text encoder should run at bf16, use fixed node to convert fp16 to bf16
  - *From: KingGore2023*

- **Problem:** FileNotFoundError: Gemma3 tokenizer not found for GGUF
  - **Solution:** Put tokenizer files from huggingface.co/smhf72/gemma-3-12b-it-extras-comfy into text encoders folder
  - *From: yi*

- **Problem:** Enhanced Prompt node error with GGUF: 'LTXAVTEModel_' object has no attribute 'processor'
  - **Solution:** Disable Enhanced Prompt node when using GGUF models
  - *From: Tachyon*

- **Problem:** RuntimeError: The size of tensor a (1920) must match the size of tensor b (261248)
  - **Solution:** Remove ComfyUI_smZNodes - it overwrites comfy samplers and breaks LTX2 due to nested video + audio tensors
  - *From: Kijai*

- **Problem:** Garbled mess output with GGUF distilled model
  - **Solution:** If using full fp8 model without distill LoRA, bump first pass steps to 40. Otherwise use distill LoRA at 20 steps
  - *From: Tachyon*

- **Problem:** Blurry GGUF output
  - **Solution:** Use distill LoRA in upscale phase, or increase steps if not using LoRA
  - *From: Tachyon*

- **Problem:** ComfyUI GGUF nodes don't support LTX2
  - **Solution:** Use Vantage-GGUF fork: https://github.com/vantagewithai/Vantage-GGUF
  - *From: Kijai*

- **Problem:** I2V gives slideshow-like results unless using exact image as prompt
  - **Solution:** Try compression value of 90 for stylized images, or lower conditioning strength below 1.0
  - *From: N0NSens*

- **Problem:** Second frame cuts in I2V
  - **Solution:** Lower mask level (conditioning strength) to let model modify the latent and bring it into distribution
  - *From: 976496720370348032*

- **Problem:** GGUF Gemma models not working with LTX-2
  - **Solution:** Use correct GGUF source - unsloth GGUF requires their specific loader
  - *From: cocktailprawn1212*

- **Problem:** OOM errors on image2video with 2x 3090
  - **Solution:** Use Reddit fix for 24GB or less VRAM systems
  - *From: noodlz*

- **Problem:** Model merges producing garbage output
  - **Solution:** Need to save metadata from original model including license and model configs
  - *From: Kijai*

- **Problem:** GGUF models 4x slower than FP8
  - **Solution:** Something appears wrong with current GGUF implementation - shouldn't be 4x slower
  - *From: garbus*

- **Problem:** OOM at high resolutions with reserve-vram
  - **Solution:** Increase --reserve-vram value (try 6-7 for high res), estimation has issues at huge resolutions
  - *From: Kijai*

- **Problem:** 1080p 480 frame generation fails with OOM
  - **Solution:** Split latents and merge using overlap nodes for smooth 20 second footage from two 10-second segments
  - *From: dj47*

- **Problem:** Lip sync not working consistently
  - **Solution:** Adjust compression noise applied to image or lower image_cond_strength
  - *From: TK_999*

- **Problem:** Getting slideshow/zoom instead of animation in I2V
  - **Solution:** Increase img compression from default 30-33 to 40-ish range, or lower image_strength to 0.8
  - *From: foxydits*

- **Problem:** Static/frozen videos in I2V
  - **Solution:** Use LTXVPreprocess node on input image and set proper image preprocessing
  - *From: 976496720370348032*

- **Problem:** ComfyUI memory leaks after multiple generations
  - **Solution:** Use --disable-cuda-malloc flag and restart ComfyUI regularly, or use vacuum button
  - *From: pagan*

- **Problem:** System freezing during high resolution generation
  - **Solution:** Use --reserve-vram flag (tested with values 4-8GB)
  - *From: 217076219072479232*

- **Problem:** Metadata is required for audio VAE error
  - **Solution:** Use VAELoader KJ and the LTX2 audio vae bf16
  - *From: zelgo_*

- **Problem:** ComfyUI crashes with LTX2
  - **Solution:** Disable video previews in ComfyUI and use --cache-none flag
  - *From: Tachyon*

- **Problem:** OOM errors
  - **Solution:** Use --reserve-vram 4 or higher, increase page file to 65GB on Windows
  - *From: Tachyon*

- **Problem:** Static images in I2V
  - **Solution:** Add film grain to images and ensure audio start time is at least 0.2
  - *From: Elvaxorn*

- **Problem:** Converting mono audio to stereo
  - **Solution:** Use Join Audio Channels node and plug same audio into both left and right channels
  - *From: Elvaxorn*

- **Problem:** Python/ComfyUI dying during generation
  - **Solution:** Usually due to running out of RAM + pagefile. Use --cache-none or increase pagefile
  - *From: Kijai*

- **Problem:** I2V VRAM issues and freezing at higher resolutions
  - **Solution:** Change memory_usage_factor in supported_models.py from 0.061 to 0.2 for safer operation, or 0.16 for 5090
  - *From: Elvaxorn*

- **Problem:** Video snapping back to original image at end in I2V
  - **Solution:** Use LTXVRemoveGuides node to remove guides before decode when using guided generation
  - *From: Kijai*

- **Problem:** OOM errors despite large RAM/VRAM
  - **Solution:** Use --reserve-vram flag or modify memory_usage_factor, both achieve more offloading
  - *From: Kijai*

- **Problem:** ComfyUI updates reset memory_usage_factor changes
  - **Solution:** Re-edit the value back to custom setting after updates
  - *From: Elvaxorn*

- **Problem:** Metadata loading issues causing audio problems
  - **Solution:** Ensure using GGUF node with metadata code applied, city96 merged PR for ComfyUI-GGUF metadata support
  - *From: Kijai*

- **Problem:** GGUF models running slow despite memory optimizations
  - **Solution:** Update memory_usage_factor setting - was seeing 15.53s/it on dev-Q8 vs 5.52s/it on dev-fp8
  - *From: garbus*

- **Problem:** T2V workflows breaking with memory optimization
  - **Solution:** Updated av_model file fixes T2V case while maintaining I2V improvements
  - *From: Kijai*

- **Problem:** Massive RAM usage and crashes on lower VRAM systems
  - **Solution:** Memory optimization in av_model.py reduces VRAM usage by ~5GB at higher resolutions
  - *From: Kijai*

- **Problem:** Dark scene artifacts with certain samplers
  - **Solution:** er_sde on first sampler stage was causing artifacts in dark scenes, switching samplers helped
  - *From: garbus*

- **Problem:** VAE decode causing PC crashes
  - **Solution:** Try normal VAE decode instead of LTX VAE decode, check frame count limits
  - *From: David Snow*

- **Problem:** 'post_quant_conv.weight' error with VAE
  - **Solution:** Use Kijai's VAE loader node instead of standard ones when using GGUF quantized models
  - *From: Tachyon*

- **Problem:** Metadata required for audio VAE error
  - **Solution:** Use audio VAE from Kijai's repo: LTX2_audio_vae_bf16.safetensors
  - *From: Tachyon*

- **Problem:** Tensor size mismatch error
  - **Solution:** Disable video sampling previews in ComfyUI settings
  - *From: Tachyon*

- **Problem:** Custom node causing tensor errors
  - **Solution:** Disable problematic custom nodes that interfere with LTX2
  - *From: 201830562200027137*

- **Problem:** AttributeError with GGUF loader
  - **Solution:** Use separate GGUF UNet loader node instead of regular loader
  - *From: JUSTSWEATERS*

- **Problem:** KeyError: 'num_crops' error with Enhance Prompt Node
  - **Solution:** Most users have disabled or completely removed the Enhance Prompt Node from workflows
  - *From: NC17z*

- **Problem:** 'VAE' object has no attribute 'latent_frequency_bins' error
  - **Solution:** KJ nodes update solved the issue
  - *From: xwsswww*

- **Problem:** CLIPLoaderGGUF error: 'Unexpected text model architecture type in GGUF file: 'gemma3''
  - **Solution:** Update City96 GGUF nodes to latest version, or use merged pull requests for comfy gguf node. Also need tokenizer.model in clip folder
  - *From: 568465354158768129*

- **Problem:** Long pause before sampler starts first step
  - **Solution:** Normal behavior - first step should take the longest, but 10+ minutes indicates hardware issues or offloading problems
  - *From: 568465354158768129*

- **Problem:** I2V not following reference image when same size as latent
  - **Solution:** ComfyUI I2V workflow resizes image so longest side is 1536, then feeds to LTXVImgToVideoInplace - image isn't supposed to be same size as latent
  - *From: 411637464806195202*

- **Problem:** GGUF model producing noise output
  - **Solution:** Update ComfyUI-GGUF nodes to nightly version, LTX2 support was only merged recently
  - *From: Kijai*

- **Problem:** ComfyUI disconnecting with VAE tiled at low settings
  - **Solution:** Use --cache-none flag, issue is RAM limitation not VRAM (16GB RAM is tough)
  - *From: Kijai*

- **Problem:** Second stage upscaling very slow (5 minutes per iteration)
  - **Solution:** Check if using --normal-vram or --reserve-vram flags, may be causing slowdowns
  - *From: NC17z*

- **Problem:** Vertical video artifacts at 1080p+
  - **Solution:** Consensus is vertical video doesn't work well with current model
  - *From: ucren*

- **Problem:** Error running sage attention: Input tensors must be in dtype of torch.float16 or torch.bfloat16
  - **Solution:** Use Kijai's patch node instead of --use-sage-attention flag
  - *From: Kijai*

- **Problem:** Blurry/artifacted I2V results with grid patterns
  - **Solution:** Switch to euler_ancestral sampler, increase distill lora strength to 1.0, don't connect distill lora to first stage if using 40 steps
  - *From: seitanism*

- **Problem:** Frame limit crash on VAE: input tensor must fit into 32-bit index math
  - **Solution:** Known limitation at high frame counts (above 281 frames), VAE decode bottleneck
  - *From: NebSH*

- **Problem:** Gemma won't load after latent2rgb PR
  - **Solution:** Need to rebase PR to be up to date with main
  - *From: Kijai*


## Model Comparisons

- **SDE vs ODE samplers**
  - SDE adds noise every step providing quality, exploration and error-correction but requires more steps. ODE samplers (euler, dpm, unipc, deis) are faster. Most people prefer speed so should use ODE and distilled models
  - *From: mallardgazellegoosewildcat2*

- **Temporal upscaler steps**
  - 4 steps res_2s sounds much better than 20 steps for temporal upscaling, reduces visual artifacts
  - *From: TK_999*

- **LTX2 vs WAN 2.2**
  - LTX2 does way more than WAN 2.2 - has audio/dialog built in, variable frame rate, much faster in 1 model
  - *From: Phr00t*

- **FP8 vs FP4 models**
  - FP4 didn't provide much speed improvement, sometimes slower than FP8
  - *From: D'Squarius Green, Jr.*

- **Abliterated vs non-abliterated Gemma**
  - Abliterated version adheres better to prompts, especially for soft core content
  - *From: Kiwv*

- **RTX Pro 5000 48GB vs RTX 5090**
  - Pro 5000 probably better for this model right now due to VRAM, but worse in future. 4090 mod with 48GB is best deal
  - *From: Benjimon*

- **FP4 models vs others**
  - FP4 models are fast but really suck in quality
  - *From: Grimm1111*

- **High res only vs two stage pipeline**
  - High res only really hurts motion compared to two stage pipeline
  - *From: Benjimon*

- **HuMo vs LTX character consistency**
  - HuMo's character consistency is way better so far
  - *From: AJO*

- **Distilled vs non-distilled models**
  - Non-distilled models produce significantly better quality, distilled models change too much at cfg=1
  - *From: Kijai*

- **fp8 vs bf16 models**
  - Full bf16 model recommended over fp8 for best quality, any speedup shortcut can be disastrous
  - *From: 421114995925843968*

- **T2V vs I2V speed**
  - T2V and I2V are basically the same speed with very minor differences
  - *From: 976496720370348032*

- **LTX temporal tiling vs other methods**
  - LTX temporal tiling is better, use larger overlap especially spatial
  - *From: 976496720370348032*

- **Distilled vs Full model quality**
  - No big difference noticed between full model and fp8 model. Distilled model may do better upscaling but has apparent differences
  - *From: seitanism*

- **res_2s vs euler_ancestral scheduler**
  - res_2s 40 steps gave overbaked outputs. euler_ancestral 40 steps looked similar to res_2s 20 steps. Stick with euler_ancestral
  - *From: seitanism*

- **Custom node workflow vs ComfyUI template**
  - ComfyUI-LTXVideo example workflows way better than ComfyUI template - template i2v basically has no motion
  - *From: protector131090*

- **LTX-2 vs Sora**
  - Having local sora 1.5 moment - most exciting release since wan2.2
  - *From: VK (5080 128gb), seitanism*

- **Separated components vs default workflow**
  - Separated components take more VRAM sadly, OOM in situations where default works
  - *From: Gleb Tretyak*

- **FP8 vs BF16 quality**
  - BF16 has significantly better quality than FP8, especially for character LoRAs
  - *From: NebSH*

- **Distilled vs Full model**
  - Distilled model has 'crushed' AI look, full model preferred for natural motion. FP8 gives better motion than FP4 despite FP4 being sharper
  - *From: Grimm1111*

- **Different NVIDIA drivers**
  - No speed difference found between driver versions 570.86.16, 580.119.02, and 590.48.01 - exact same inference times
  - *From: Kijai*

- **Manual sigmas vs BasicScheduler vs LTXVScheduler**
  - Manual sigmas work better, though basic scheduler differences were minimal
  - *From: psylent_gamer*

- **FP8 distill vs FP8 full model**
  - Full model significantly better quality and consistency, distill version has issues with consistency
  - *From: psylent_gamer*

- **LTX-2 vs WAN 2.5**
  - This is what WAN 2.5 was supposed to be
  - *From: VK (5080 128gb)*

- **LTX2 vs WAN image quality**
  - WAN has better raw output quality, LTX2 requires higher resolution (1080p) to match WAN 720p sharpness
  - *From: seitanism*

- **Q8 vs fp8 quality**
  - Q8 is better quality than fp8, closer to full bf16 model
  - *From: Kijai*

- **Q6 vs fp8**
  - fp8 is usually worse than Q6
  - *From: Ada*

- **Distilled vs full model**
  - At 20-30 steps distilled was better, but full model might be better at 50+ steps
  - *From: Ada*

- **fp8 scaled vs Q8**
  - With WanVideo 2.1, fp8 scaled was nearly as close as Q8
  - *From: Kijai*

- **Quantization quality ranking**
  - fp16 > Q8 > fp8scaled >> Q6
  - *From: Kijai*

- **First stage vs second stage audio quality**
  - First stage voice is better and less robotic than second stage
  - *From: Gleb Tretyak*

- **Distill vs full model**
  - Distill is fast but dumb - get desired result on 10th try with fast iterations, or 3rd try with long iterations using full model
  - *From: N0NSens*

- **LTX distilled fp8 vs q8 gguf**
  - Hard to tell which is better in quality, but fp8 should be 30-40% faster on ada+ GPUs
  - *From: David Snow*

- **FP8 scaled Gemma vs normal FP8**
  - FP8 scaled is closer to bf16 quality than normal fp8
  - *From: Kijai*

- **40 steps no distill vs distilled versions**
  - 40 steps without distill has very real, subtle movement quality
  - *From: ZeusZeus (RTX 4090)*

- **Dev model vs Distill model audio quality**
  - Dev model has awful audio with high pitched drone, distill model has better audio
  - *From: David Snow*

- **Full dev model with distill LoRA vs pure distill model**
  - Dev + distill LoRA at 0.6 makes skin far more natural than just distill model, but uses more RAM
  - *From: David Snow*

- **Q8 vs FP8 quality**
  - Small quality improvement with Q8 over FP8
  - *From: D'Squarius Green, Jr.*

- **With vs without spatial upscaler**
  - Huge difference in quality, upscaler significantly improves results
  - *From: TK_999*

- **LTX vs WAN for debris/action scenes**
  - LTX handles debris fields with better clarity than WAN in FP8, WAN gets extreme dithering
  - *From: ZombieMatrix*

- **WAN vs LTX prompt following**
  - WAN is more responsive to prompting, LTX fights prompts more but is good for basic trained scenarios
  - *From: Grimm1111*

- **Comfy Gemma fpmixed vs fp8_scaled**
  - fpmixed should be better than fp8_scaled with extra weight_scale_2 on every layer
  - *From: comfy*

- **fp8 vs mixed Gemma models**
  - Mixed is slightly bigger (12.7gb vs 12.3gb) but offers better accuracy
  - *From: TK_999*

- **Distilled vs non-distilled model**
  - Distilled gives much much better results
  - *From: Gleb Tretyak*

- **Dev model vs distilled model audio quality**
  - Dev model produces much better sound after upscaler
  - *From: N0NSens*

- **LTX2 vs Wan/Kandinsky for 2D animation**
  - LTX2 is noticeably worse than Wan or Kandinsky for 2D animation
  - *From: Ada*

- **FP8_scaled vs other quantizations**
  - FP8_scaled looks closest to bf16, especially for main subjects
  - *From: Kijai*

- **Native LTX workflows vs ComfyUI defaults**
  - ComfyUI native defaults aren't the best
  - *From: Kijai*

- **Distilled vs full model audio quality**
  - Distilled model has somewhat worse audio quality as it's a compromise model trained for few steps
  - *From: 976496720370348032*

- **Quality order for model types**
  - Full model > Q8 > fp8 in terms of quality
  - *From: Tachyon*

- **fp16 vs Q8 speed and quality**
  - fp16 is faster than Q8 despite higher VRAM usage, similar quality between fp16 and Q8
  - *From: Underdog*

- **GGUF speed on Apple Silicon**
  - GGUF cuts generation time by more than half compared to full models on M4 Mac
  - *From: buggz*

- **GGUF Q6 vs Q8**
  - No difference between Q6 and Q8 - no reason to use Q8 over Q6
  - *From: Kijai*

- **Full model vs Distilled model quality**
  - Many users report distilled model produces better results than full model
  - *From: Gleb Tretyak*

- **GGUF vs FP8 speed**
  - GGUF always slower but uses less VRAM - price of lower VRAM usage
  - *From: Xor*

- **Different GGUF repositories**
  - Q4 can be slightly better in some repos (unsloth, others) due to mixed layers with some Q5
  - *From: Kijai*

- **LTX2 vs LatentSync 1.6/InfiniteTalk v2v**
  - LTX2 lip-sync works far better than both alternatives
  - *From: KingGore2023*

- **V2V vs Audio I2V for lip sync**
  - V2V lip-sync works better than Audio I2V, never produces still images
  - *From: KingGore2023*

- **Dev model vs Distill model audio quality**
  - Dev model is slow but produces great sound, especially during upscaling. Distill model is 4x faster but final sound is really bad
  - *From: N0NSens*

- **I2V vs T2V memory usage**
  - I2V uses significantly more VRAM - instantly 5GB+ higher memory usage when I2V node is added
  - *From: Kijai*

- **Direct high-res vs upscale approach**
  - Generating 30 steps 1280x1024@161 frames direct takes 8 minutes vs same with upscale pass completes under 3 minutes
  - *From: 138332118890708992*

- **Q8 distilled vs Q8 dev + distilled LoRA**
  - Q8 distilled performs better for I2V use cases
  - *From: Choowkee*

- **LTX2 vs LTX1 quality**
  - LTX2 has similar hard quality ceiling as LTX1, fast and versatile but limited quality
  - *From: Christian Sandor*

- **LTX2 realistic vs anime**
  - I2V works much better for realistic images than anime, realistic images animate way easier
  - *From: Kijai*

- **GGUF vs FP8 speed**
  - GGUF should be only couple percent slower than FP8 on 3090, not massively different
  - *From: Kijai*

- **Stock vs abliterated text encoders**
  - Abliterated allows more provocative motions but doesn't uncensor the underlying model, which wasn't trained on NSFW
  - *From: Kiwv*

- **FP8 vs full precision text encoders**
  - FP8 version shows no degrading effects that the eye can see for I2V
  - *From: Choowkee*

- **Distilled vs non-distilled with LoRA**
  - Non-distilled with lora in 2nd sampler looked better in limited testing
  - *From: MechanimaL*

- **Q8 GGUF vs FP8 performance**
  - Q8-DEV GGUF: 15.53s/it vs dev-fp8: 5.52s/it on same workflow
  - *From: garbus*

- **Q4 GGUF vs FP8**
  - GGUF takes about 3 minutes for 33 frames vs FP8 taking 1 minute, but uses less VRAM
  - *From: JUSTSWEATERS*

- **With vs without distilled LoRA**
  - Without distilled LoRA looks much worse, especially noticeable difference in quality
  - *From: 568465354158768129*

- **Different resolutions**
  - 1920x1080 gives best overall results, 1280x720 is good compromise
  - *From: multiple users*

- **FP8 vs GGUF performance**
  - FP8 is faster than GGUF as long as you're not offloading, but GGUF gives 10GB free VRAM where FP8 gives only 3GB
  - *From: JUSTSWEATERS*

- **LTX-2 vs Wan2.2 for video generation**
  - LTX2 is relatively weak in stage 1, can use Wan2.2 to generate videos in stage 1 then LTX2 for stage 2, but reaches limits in stage 2 most of the time
  - *From: KingGore2023*

- **I2V vs T2V strength**
  - I2V seems a lot stronger than T2V, though T2V can sometimes produce really nice results. I2V is mixed - can give good results but also bad ones
  - *From: particle9*

- **Q4 vs Q8 GGUF quality**
  - No noticeable difference in quality between Q4 and Q8, prompting has bigger impact than quantization level
  - *From: Hevi*

- **Distilled vs Dev model skin quality**
  - Even Dev model struggles with realistic skin, no clear benefit over distilled for skin realism
  - *From: ラD.*

- **LTX2 vs Infinite for lip sync**
  - LTX2 is far better than Infinite for video-to-video lip sync applications
  - *From: Stef*

- **LTX2 vs WAN I2V**
  - LTX2 main features are automatic voiceover and speed, but video quality and prompt understanding are worse than WAN
  - *From: N0NSens*

- **Official WF vs KJ WF**
  - KJ WF using Dynamic Lora at 0.8 and CFG schedule shows more animation than Official WF using Dev+Distilled at 1.0
  - *From: The Shadow (NYC)*

- **LTX2 vs Sora2/VEO3**
  - Biggest influence on quality is prompt and using Gemma fpmixed for prompt adherence
  - *From: nacho.money*


## Tips & Best Practices

- **Use lower frame rates for longer videos**
  - Context: Lower frame rates mean fewer frames to generate, making longer videos easier to create, though lip syncing isn't as good
  - *From: Phr00t*

- **Use 24 fps as standard**
  - Context: 24p is used in the states, 25p elsewhere. Official LTX workflow uses 24 fps
  - *From: Daflon*

- **Generate at 20fps and upscale to 40fps via temporal upscaler**
  - Context: For better efficiency while maintaining quality
  - *From: Xor*

- **Use audio-to-audio models to improve LTX-2 audio quality**
  - Context: Audio quality from LTX-2 is poor but can be enhanced with voice cloning tools like Elevenlabs or audio upscaling models
  - *From: Kiwv*

- **Disable previews for LTX-2**
  - Context: To avoid certain errors
  - *From: TK_999*

- **Use larger resolution to fix overblown/plastic looking results**
  - Context: When videos look blown out
  - *From: Kiwv*

- **20 seconds appears to be the sweet spot before distortion starts**
  - Context: For maintaining coherence in longer videos
  - *From: Tachyon*

- **Use CoPilot on Windows for troubleshooting errors**
  - Context: Right-click errors in Edge browser for instant help
  - *From: NC17z*

- **Update ComfyUI for latest nodes and fixes**
  - Context: When experiencing issues with workflows
  - *From: Tachyon*

- **Be very verbose with LTX2 prompts**
  - Context: For getting proper lip movement and speech
  - *From: Q-*

- **Specify person with country of origin to avoid Bollywood influence**
  - Context: When prompt doesn't specify nationality
  - *From: yi*

- **Use strong clear prompts from Gemini with interleaved ethnicities**
  - Context: To avoid Bollywood influence in generations
  - *From: ZombieMatrix*

- **Resolution should be divisible by 32+1 and frames 8+1**
  - Context: Following model requirements, though it picks closest anyway
  - *From: Q-*

- **Use images where face is larger for better identity adherence**
  - Context: Small faces are harder for model to maintain identity throughout longer videos
  - *From: 976496720370348032*

- **Horizontal images work better than portrait for I2V**
  - Context: Portrait images tend to just move frame up and down
  - *From: JUSTSWEATERS*

- **Reduce LTXVPreprocess strength from 33 to lower for better results**
  - Context: When having identity preservation issues
  - *From: 976496720370348032*

- **Use temporal upscaler for very dynamic videos with texture smear**
  - Context: Good remedy for VAE struggles with dynamic content, denoise more after applying
  - *From: 976496720370348032*

- **Use LTXVSetAudioVideoMaskByTime node for audio/video editing**
  - Context: For continuation and editing workflows, this node defines noise mask on av_latents from start to end editing time
  - *From: 976496720370348032*

- **Wipe negative prompts when using non-distilled models**
  - Context: Negative prompts do nothing with distilled models at cfg=1, but should be removed for proper non-distilled usage
  - *From: 976496720370348032*

- **Use non-quantized Gemma3 model for better voice quality**
  - Context: Quantized models can affect audio quality, full precision works like a charm
  - *From: 976496720370348032*

- **Prompt for animation details when character won't move**
  - Context: Increase preprocessing and lower weight, add detailed prompts for movement when characters appear frozen
  - *From: Juan Gea*

- **Use higher resolution to improve generation quality**
  - Context: Higher resolution can help with various quality issues including character animation
  - *From: 976496720370348032*

- **Use 48 FPS for I2V generations**
  - Context: Significantly improves quality by counteracting temporal compression artifacts
  - *From: Ada*

- **Add IC detailer LoRA to second stage**
  - Context: Will be night and day difference in upscaling quality
  - *From: scf*

- **Lower resolution allows longer videos**
  - Context: At 540p can do 1000 frames easily. At 960x960, 1000 frames outputs garbage. 16fps with 640x640 could do 1 minute videos
  - *From: seitanism*

- **Use separate start/end times for audio and video**
  - Context: Can control audio and video regeneration independently in continuation workflows
  - *From: 976496720370348032*

- **Test long context with specific prompts**
  - Context: Ask for something that shows consistency like 'person going out a door and coming back at the end'
  - *From: 976496720370348032*

- **Tone down CFG for full model**
  - Context: High CFG can cause skin quality issues
  - *From: 976496720370348032*

- **For 2D animation, add '2d Japanese traditional anime sequence' to start of prompt**
  - Context: When trying to generate 2D style content
  - *From: VK (5080 128gb)*

- **Don't describe the image in I2V prompts, focus on actions**
  - Context: Model already sees the image, describing it leads to static results
  - *From: seitanism*

- **Voices are better and less robotic if you describe voice details**
  - Context: Include accent, tone etc in audio prompts
  - *From: seitanism*

- **Use 'soft spoken' keyword to control audio volume/intensity**
  - Context: When audio is too loud or intense
  - *From: VK (5080 128gb)*

- **Set dual clip loader device to CPU to help with memory**
  - Context: Reduces VRAM usage during text encoding
  - *From: yi*

- **Use ffmpeg to extend videos with padding**
  - Context: For video continuation - simpler command: ffmpeg -i input.mp4 -vf 'tpad=stop_duration=5:color=gray' -af 'apad=pad_dur=5' output.mp4
  - *From: 976496720370348032*

- **Remove audio latent inputs to save VRAM**
  - Context: When you don't need audio generation
  - *From: Kijai*

- **Use VAE tiled decode for VRAM safety**
  - Context: Safer option when concerned about VRAM usage
  - *From: JUSTSWEATERS*

- **Less tiling gives better results**
  - Context: Reduces tiling artifacts and helps with lip syncing, but increases OOM risk
  - *From: Grimm1111*

- **Use detailed negative prompts for better results**
  - Context: LTX likes wordy prompts, use comprehensive negative prompts
  - *From: Q-*

- **Do side by side tests when comparing models**
  - Context: Keep same everything except clip model, same seed etc.
  - *From: Scruffy*

- **Use 2D animation prompts for consistent frame timing**
  - Context: Use prompts like '2d animation, The animation plays on twos with stepped/limited timing and held poses every two frames, slight frame-to-frame registration wiggle, minimal motion blur'
  - *From: JUSTSWEATERS*

- **Make video longer than needed for interpolation**
  - Context: When using interpolation, last frame usually gets corrupted, so make video a few frames longer and cut it
  - *From: Ruairi Robinson*

- **Use higher FPS for better results**
  - Context: You will get better results with higher FPS like 48
  - *From: Benjimon*

- **Use res2s with 15 steps for better results**
  - Context: General usage
  - *From: yi*

- **Write long prompts once as templates then modify**
  - Context: Long prompts seem to help with results
  - *From: Lodis*

- **Use visualize node for sigmas to understand them better**
  - Context: Res4lyf has one and KJNodes has another option
  - *From: Kijai*

- **For vid2vid, model works better with continuous shots rather than fast changing scenes**
  - Context: Video-to-video generation
  - *From: VK (5080 128gb)*

- **Inject noise into initial picture to add motion**
  - Context: When input image is too perfect and causes motionless video
  - *From: Lodis*

- **Use camera LoRA to fix motionless issues**
  - Context: When generating videos with static input images
  - *From: 1100803024298975263*

- **Generate at double frame rate**
  - Context: Use 48fps instead of 24fps to solve smeared faces and fast movement issues
  - *From: Juan Gea*

- **Use VAE tile size of 1536 on 4090**
  - Context: Default is 512, can increase to 1536 for better performance on 4090
  - *From: David Snow*

- **Run text encoding separately for memory**
  - Context: Save text encoding to file and load it to work around memory limitations
  - *From: Kijai*

- **Set Gemma to CPU device**
  - Context: Massive speed improvement when changing prompts, avoids swapping
  - *From: onama*

- **Don't use negative prompts with distilled model**
  - Context: CFG 1 doesn't support negative prompts effectively
  - *From: KingGore2023*

- **Use detailer lora with strength 0.5-0.75 on both stages**
  - Context: For better quality results
  - *From: David Snow*

- **Skip audio in 2nd stage while keeping it for video**
  - Context: For efficiency when first stage audio is better
  - *From: hicho*

- **Add 'with tears' to prompts for crying emotion**
  - Context: Model tends to generate laughing instead of crying without explicit direction
  - *From: KingGore2023*

- **Keep NAG negative prompts short and specific**
  - Context: Don't use huge negative prompt word lists, just define things you don't want to see
  - *From: Kijai*

- **Use Res_2s first stage, euler_a second stage for high quality**
  - Context: Combination produces very clean outputs with crisp motion
  - *From: David Snow*

- **Lower distill LoRA strength to 0.9 for second stage**
  - Context: Appears to improve quality in multi-stage workflows
  - *From: IceAero*

- **Reduce video resolution for audio-only generation**
  - Context: Can make audio generation much faster since video part is still needed but can be low res
  - *From: Kijai*

- **Use split models to avoid loading video VAE for audio-only**
  - Context: When using Kijai's split models, don't need to load video VAE at all for audio generation
  - *From: Kijai*

- **Use proper sentence negatives instead of tag-style negatives**
  - Context: When writing negative prompts, use sentence fragments like 'A person is standing perfectly still, staring at the camera'
  - *From: TK_999*

- **SLG, PAG, SEG are better than negative prompts**
  - Context: These guidance methods are more effective than traditional negative prompting
  - *From: mallardgazellegoosewildcat2*

- **Use keyframing for complex effects**
  - Context: For effects like characters jumping out of screens, generate before and after frames and fill in the blanks
  - *From: 421114995925843968*

- **Set last keyframe 10 frames before actual end**
  - Context: When using guidance, allows trimming last 10 frames for cleaner transitions
  - *From: JUSTSWEATERS*

- **Describe smooth transitions between frames**
  - Context: For first-to-last frame workflows, describe first frame, transition, then last frame to avoid slideshow effect
  - *From: Benjimon*

- **Use dev model to reduce plastic look**
  - Context: dev model helps with plastic appearance compared to other variants
  - *From: Benjimon*

- **Pick best stage 1 video before stage 2**
  - Context: Not efficient but fast - select best output from stage 1 before continuing to stage 2
  - *From: KingGore2023*

- **Add small value to mask for better results**
  - Context: When using masking workflows, adding small value works better
  - *From: 224611423869730818*

- **Start with weight 2.0 for Enhance-a-Video**
  - Context: Initial recommendation for Enhance-a-Video weight
  - *From: Kijai*

- **Prompt for specific explicit movements for better results**
  - Context: When prompting for character actions
  - *From: Kijai*

- **The prompt matters a lot for quality**
  - Context: Getting good results from the model
  - *From: KingGore2023*

- **Find the right seed - annoying but necessary**
  - Context: Since model won't follow prompt perfectly
  - *From: KingGore2023*

- **Use subgraphs for repeated functions, not to obfuscate major workflow parts**
  - Context: Proper subgraph usage
  - *From: Kijai*

- **Lower I2V mask level will always move but you lose character at too low levels**
  - Context: Balancing movement vs character preservation
  - *From: Kijai*

- **Try other seeds when troubleshooting**
  - Context: When getting static or poor results
  - *From: Kijai*

- **Use LTXVImg2VideoInPlace node for frame 0 instead of AddGuide**
  - Context: For classic i2v conditioning which is stronger and better than keyframe method
  - *From: 976496720370348032*

- **Set keyframe index to k-1 for k pixel frames (zero-based)**
  - Context: When using keyframe workflows, but adherence won't be perfect
  - *From: 976496720370348032*

- **Try longer videos with keyframes further apart or fewer keyframes**
  - Context: For challenging interpolation styles
  - *From: 976496720370348032*

- **LTX2 really relies on prompt quality**
  - Context: Prompt variations and descriptive motion change results significantly even with same seed
  - *From: KingGore2023*

- **Can introduce partial CFG even with distill model**
  - Context: For additional control over generation
  - *From: Kijai*

- **Try compression value of 40 first, 90 is very high**
  - Context: When dealing with stylized images that produce still frames
  - *From: 976496720370348032*

- **Don't use more than 3 LoRAs with LTX2**
  - Context: Performance consideration, prefer distilled original model
  - *From: KingGore2023*

- **Can use euler_A on upscale to tone down res_2 effects**
  - Context: When using resolution upscaling
  - *From: David Snow*

- **Seed hunting is key for video generation**
  - Context: LTX has always been unpredictable, need to try different seeds
  - *From: N0NSens*

- **Tweak settings with fixed seed first**
  - Context: Before seed hunting, optimize settings on one seed
  - *From: mallardgazellegoosewildcat2*

- **Split workflow into lowres and upscale parts**
  - Context: Deal with lowres until you find needed seed, then upscale - faster with distilled
  - *From: N0NSens*

- **Use regen fixed seed for multi-sampler workflows**
  - Context: Regen sampler 1 with fixed seed for baseline, then sampler 2 - cuts gen time in half
  - *From: foxydits*

- **Add 'no backing music' to prompts**
  - Context: Helps prevent unwanted audio generation even with small audio prompts
  - *From: TK_999*

- **Lower second frame strength in 3-keyframe guider**
  - Context: Can force movement when using guider for 3 keyframes
  - *From: JUSTSWEATERS*

- **Make second keyframe noisier**
  - Context: Alternative method to force movement in keyframe guidance
  - *From: KingGore2023*

- **Prompt the entire video including masked parts**
  - Context: When doing video extension, describe the whole video including unchanged parts for better results
  - *From: 976496720370348032*

- **Use LTXVPreprocess on input images**
  - Context: Helps avoid frozen, semi-frozen and cut-on-2nd-frame videos in I2V
  - *From: 976496720370348032*

- **Set video start time to at least 0.1**
  - Context: In video extension workflows to avoid generating T2V instead of I2V
  - *From: Elvaxorn*

- **Use detailed prompts with LTX2**
  - Context: Model responds much better to detailed prompting vs simple prompts
  - *From: nacho.money*

- **Use elaborate prompting for multiple speakers**
  - Context: Format as 'Person A says: XXXXX, Person B says: YYYYYYY' etc.
  - *From: 976496720370348032*

- **Use grainy realistic pics over smooth AI pics for I2V**
  - Context: Smoother AI-generated images don't work as well as grainy, realistic photos
  - *From: Elvaxorn*

- **Use Detail Daemon for free quality improvement**
  - Context: Particularly useful for image models, less so on video models
  - *From: David Snow*

- **Use --cache-none over pagefile when possible**
  - Context: Both are slower but cache-none just does more reads, not writes to disk
  - *From: Kijai*

- **Use image compression value of 0 if still getting motion**
  - Context: If motion is achieved with 0 compression, there are no other downsides
  - *From: Kijai*

- **Higher image compression = more motion, less adherence to init image**
  - Context: Default is around 32-33, can go lower to maintain character better
  - *From: Kijai*

- **Underclock GPU by 30-40% to dramatically lower temps and extend lifespan**
  - Context: Only lose 10-15% speed but GPU runs at 58C vs much higher, extends life significantly
  - *From: Underdog*

- **Use detailer LoRA at low value (0.2) during second pass**
  - Context: Helps with details but can add artifacts if used too aggressively
  - *From: David Snow*

- **Realistic images animate much easier than anime/stylized content**
  - Context: Model works better with photorealistic input images for I2V
  - *From: Kijai*

- **Use I2V for NSFW content generation**
  - Context: I2V is really the current ticket for NSFW, using video input frames for motion samples is very effective
  - *From: foxydits*

- **Disable compression for specific use cases**
  - Context: You can disable compression entirely if you start with a few frames of video, but that's a pretty specific use-case
  - *From: foxydits*

- **Use 25 frames for crossover in infinite workflows**
  - Context: For SVI style infinite workflow, it seems to work best with a full 25 frames for a crossover
  - *From: ZombieMatrix*

- **Lower LoRA strength from default**
  - Context: Found lora strength 0.6 to be better than the default 1.0 in ComfyUI workflow
  - *From: MechanimaL*

- **Use quantized version of Gemma 12b**
  - Context: When working with limited VRAM, helps reduce memory usage
  - *From: Kiwv*

- **Try Q4 quantization for better VRAM efficiency**
  - Context: Especially useful when generating at high resolutions like 1088x1920
  - *From: Kiwv*

- **1280x720 is a good resolution spot**
  - Context: Balance between quality and generation time
  - *From: Tachyon*

- **Disable Florence2 and other LoRAs when testing**
  - Context: Florence2 is 'sdpa attention seeker' and can cause memory issues
  - *From: 568465354158768129*

- **Use tiled VAE decode for large resolutions**
  - Context: Helps prevent OOM when working with high resolution outputs
  - *From: 568465354158768129*

- **Use Pro tip: Stick a VAE decode and video combine on first stage to see if generation is jank**
  - Context: Will save hours in the long run by catching bad generations early
  - *From: David Snow*

- **Find the seed, tweak prompt and settings, then use upscaling stage for final iteration**
  - Context: Better workflow approach than always running full pipeline
  - *From: NC17z*

- **Use tiled VAE decoding to avoid OOM errors**
  - Context: Especially important with limited VRAM - helps manage memory usage during upscaling
  - *From: 568465354158768129*

- **Film grain helps everything with video models**
  - Context: Noise seems to really help video models think there is motion
  - *From: mallardgazellegoosewildcat2*

- **Use euler_A for first pass and dpmpp_sde for second pass**
  - Context: Good sampler combination - euler_A is fast, dpmpp_sde adds detail
  - *From: David Snow*

- **Generate at 48fps then reduce to 24fps**
  - Context: Theory to reduce motion artifacts then get normal playback speed
  - *From: David Snow*

- **Do seed hunting before the sampler**
  - Context: For better results with IC detailer and maintaining likeness
  - *From: dg1860*

- **Lower or disable IC detailer strength**
  - Context: High IC detailer values can kill likeness to source image
  - *From: dg1860*

- **Use LoRAs for better likeness retention**
  - Context: Trained LoRAs help maintain character consistency during lip sync
  - *From: NebSH*

- **Use distilled lora on both first and second stage for significantly better results**
  - Context: When using distilled model workflow
  - *From: Choowkee*

- **Use default image rescale vs matching to frame size for better I2V results**
  - Context: When doing image-to-video generation
  - *From: The Shadow (NYC)*

- **Connect explode lora to both stages for better results**
  - Context: When using loras in multi-stage workflows
  - *From: seitanism*

- **Use denoised output when passing from first to second pass**
  - Context: Multi-pass upscaling workflows
  - *From: TK_999*


## News & Updates

- **Universal Music Group partnered with NVIDIA**
  - Partnership announced for AI music generation
  - *From: NC17z*

- **Wan2gp released support**
  - Support was released for LTX-2
  - *From: Benjimon*

- **New Nvidia Studio Driver includes LTX optimizations**
  - January NVIDIA Studio Driver provides RTX optimizations for LTX-2, along with PyTorch NVFP4 and NVFP8 support in ComfyUI
  - *From: zelgo_*

- **Abliterated Gemma model released**
  - Gemma-3-12b-Abliterated-LTX2 available as drop-in replacement, removes censoring bias but doesn't unlock much extra coherent content
  - *From: Kiwv*

- **Official NVIDIA collaboration on quantizations**
  - LTX worked with NVIDIA to release high quality fp8 and nvfp4 quantizations
  - *From: ltx-2*

- **GGUF version of LTX-2 transformer released**
  - 16GB transformer-only q6 GGUF uploaded, though ComfyUI compatibility uncertain
  - *From: zelgo_*

- **Reddit AMA with Lightricks CEO is live**
  - CEO answering questions about LTX-2 on r/StableDiffusion
  - *From: ltx-2*

- **ComfyUI optimizations released recently**
  - Recent commits in past 1-2 days with optimizations, more coming
  - *From: Lodis*

- **Company pronunciation clarified**
  - Lightricks is pronounced 'Light-tricks' meaning 'Tricks of light'
  - *From: 976496720370348032*

- **Previews are coming back to LTX-2**
  - Resolution is tiny for LTX latent space so preview isn't great, but better than no preview
  - *From: Kijai, yi*

- **Prompt enhancer will be fixed to work with LTXV Audio Text Encoder Loader**
  - Lightricks team working on compatibility fix
  - *From: mkupchik_lightricks*

- **Work being done on advanced memory management**
  - ComfyUI team working on memory improvements so --reserve-vram won't be needed
  - *From: Kijai*

- **Memory management worked on in ComfyUI past months**
  - ComfyUI v0.8.2 optimized memory for LTX-2, still being worked on
  - *From: Kijai*

- **New audio-video model research**
  - 26B size model that's closed source but runnable on consumer hardware
  - *From: yi*

- **Hunyuan Video 1.5 rumored to be 40B with MoE architecture**
  - Someone with inside knowledge mentioned 40B size
  - *From: yi*

- **LTX 2.1 releasing in February**
  - Will fix various issues mentioned in current version
  - *From: Lodis*

- **LTX team working on quality improvements**
  - Team said they would try to improve quality issues in version 2.5
  - *From: Ada*

- **Memory management improvements in ComfyUI**
  - PR https://github.com/Comfy-Org/ComfyUI/pull/11748 apparently improved memory management significantly
  - *From: yi*

- **GGUF quantized models available**
  - Kijai has released GGUF quantized versions of LTX Video 2
  - *From: D'Squarius Green, Jr.*

- **Portrait, sound, and I2V improvements planned for LTX 2.1**
  - Developers mentioned these as goals for the next version
  - *From: Gleb Tretyak*

- **Gemma 3 GGUF support available via PR**
  - Pull request #402 adds Gemma 3 GGUF support to ComfyUI-GGUF
  - *From: Kijai*

- **New Comfy-Org Gemma models released**
  - fpmixed and fp4_mixed versions available, targeting different fp4 layer percentages
  - *From: comfy*

- **City96 GGUF support for Gemma added**
  - Pull requests 399 and 402 add LTX 2.0 GGUF + Gemma3 GGUF support
  - *From: japar*

- **bitsandbytes required for Gemma quant**
  - Need to install bitsandbytes through Comfy Manager for fp4 Gemma quantization
  - *From: zelgo_*

- **Dynamic rank reduced distill lora released**
  - First working dynamic rank reduced distill lora available in bf16 and fp8 (fp8 not recommended)
  - *From: Kijai*

- **Developers mentioned I2V, vertical, sound are goals for version 2.1**
  - These are areas targeted for improvement in next version
  - *From: Gleb Tretyak*

- **LTX distilled LoRA released by Kijai**
  - Community-created distilled LoRA available
  - *From: David Snow*

- **Version 2.1 expected in February**
  - Should solve current workflow and compatibility problems
  - *From: Lodis*

- **LTX 2.1 announced for February**
  - Fixed version 2.1 coming in February with better I2V and variable latent space compression
  - *From: Lodis*

- **ComfyUI uploaded FP4 quant of Gemma**
  - New FP4 quantized Gemma model available, around 9GB
  - *From: zelgo_*

- **VACE-LTX-Video-0.9 available for 2B model**
  - Available on HuggingFace but only for 2B model, not 13B
  - *From: NebSH*

- **New embeddings connector for Distill model**
  - New embeddings connector specifically for distilled model available in Kijai's repo
  - *From: Elvaxorn*

- **Lower rank LoRAs for distill model released**
  - Kijai released lower rank versions of distill LoRAs (original was 7GB)
  - *From: Tachyon*

- **Join Audio Channels node added to ComfyUI core**
  - Added 2 days ago in nightly build for converting mono to stereo audio
  - *From: Kijai*

- **Improved cache management PR in development**
  - PR #10779 for better RAM management, hopefully default behavior in future
  - *From: Kijai*

- **ComfyUI-GGUF metadata support merged**
  - city96 merged PR for LTX model support in official ComfyUI-GGUF nodes
  - *From: Kijai*

- **LTX 2.1 version coming with better I2V**
  - Upcoming 2.1 version mentioned to have improved I2V capabilities
  - *From: Kijai*

- **ComfyUI previews PR available but pending**
  - Preview functionality PR exists but ComfyUI dev unsure about final implementation affecting everything
  - *From: Kijai*

- **Memory optimization breakthrough**
  - Major VRAM reduction for I2V workflows - saves ~5GB at higher resolutions by optimizing timestep embeddings
  - *From: Kijai*

- **GGUF compatibility improvements**
  - GGUF models now working with memory optimizations and various text encoders
  - *From: various*

- **Kijai updated av_model.py file**
  - New file provides improvements for image to video generation, dramatically reduces VRAM usage
  - *From: Gleb Tretyak*

- **City96 updated GGUF nodes**
  - Now supports Gemma3 GGUF and other improvements
  - *From: Tachyon*

- **ComfyUI memory management improvements being worked on**
  - Someone is working on fixing ComfyUI's memory management issues
  - *From: Ada*

- **Torch 2.9.0+cu130 delivers 2.2x speedup**
  - Full HD 81 frame renders dropped from 201 seconds to 89 seconds compared to torch 2.8.0 (unconfirmed)
  - *From: NebSH*

- **Kijai's optimizations reduce VRAM usage**
  - No more OOMs when generating at 1536x1536 for T2V, maximum was previously 1089x1089
  - *From: Gill Bastar*

- **ComfyUI GGUF officially supports LTX2**
  - LTX2 GGUF support merged to main branch
  - *From: yi*

- **Memory optimization fix completed**
  - Kijai's updated av_model.py maintains identical output to original while reducing VRAM usage and improving speed
  - *From: Kijai*

- **Kijai released latent2rgb preview support for LTX2**
  - PR allows preview during generation, works with upscale model but is slow
  - *From: Kijai*

- **Someone reuploading old loras from community to Civitai**
  - Earth zoom out LTX 2 lora being redistributed
  - *From: boop*


## Workflows & Use Cases

- **Voice to video with audio replacement**
  - Use case: Created video using Kijai's voice to video workflow, generated audio in SUNO, then replaced voice using RePlay with RVC model
  - *From: NC17z*

- **First Frame to Last Frame**
  - Use case: For controlled video generation
  - *From: Tachyon*

- **Using WAS LM Studio nodes for prompt generation from image analysis**
  - Use case: Getting prompts from image analysis
  - *From: buggz*

- **Using VRAM debug nodes for memory management**
  - Use case: Preventing OOM and maintaining consistent generation speeds
  - *From: Phr00t*

- **Video-to-video restyling without controlnet**
  - Use case: Restyling existing videos
  - *From: hicho*

- **Audio injection workflow for long generations**
  - Use case: Creating videos with synchronized audio up to 4 minutes
  - *From: ZombieMatrix*

- **Audio to video with empty latent instead of image**
  - Use case: Creating video from audio alone, similar to KJ's i+a2v workflow
  - *From: TK_999*

- **Split audio into segments for long generation**
  - Use case: Take 4-minute song, split up, generate each with different related prompts, stitch back together
  - *From: 976496720370348032*

- **Three stage workflow with temporal and spatial upscaling**
  - Use case: Better quality results using both upscalers chained together
  - *From: various users*

- **Video temporal inpainting using masking**
  - Use case: Edit part of existing video by masking audio and video latents for specific time segments
  - *From: 976496720370348032*

- **Audio/video continuation using masking**
  - Use case: Replace parts of existing video/audio while maintaining continuity
  - *From: 976496720370348032*

- **I2V with audio continuation**
  - Use case: Generate video from single frame while continuing existing audio track
  - *From: Kijai*

- **V2V latent upscaling**
  - Use case: Upscale existing videos using latent space processing
  - *From: hicho*

- **LTX for upscaling other model outputs**
  - Use case: Use LTX Video 2 to upscale Wananimate generations to higher resolution
  - *From: David Snow*

- **Split lowres/upscale workflow for slower hardware**
  - Use case: When upscale pass is 5x slower than lowres generation (1min gen -> 5min upsc). Run fast lowres, enable upscaler only if result is good
  - *From: N0NSens*

- **Spatial tiling for high resolution**
  - Use case: Split latent from low res run, process individually with highres, stitch together with overlap blending using LTXVLoopingSampler
  - *From: 976496720370348032*

- **Audio-only generation workaround**
  - Use case: Generate 'redundant' video and throw out video stream, keeping audio stream when audio-only model not available
  - *From: 976496720370348032*

- **LTX + WAN upscale pipeline**
  - Use case: Less mushy detail, use low denoising just enough to fix lost details from LTX, stick to 720p or 1600x960 then upscale to 1080p
  - *From: dj47*

- **Video upscale using WAN + SeedVR2 + grading**
  - Use case: Cleaning up LTX output while maintaining lip sync, keeps color shifts manageable
  - *From: dj47*

- **Video continuation with audio masking**
  - Use case: Extending videos while preserving original segments and adding new content
  - *From: Kijai*

- **Two-stage generation with distilled LoRA for upscaling**
  - Use case: First stage generates base video, second stage with distilled LoRA adds texture/detail
  - *From: 976496720370348032*

- **Auto-regressive video generation**
  - Use case: Creating arbitrarily long videos using temporal tiles with LoopingSampler
  - *From: 976496720370348032*

- **Distilled fp8 model with 2K upscaling workflow**
  - Use case: Generating and upscaling videos to 2K resolution, takes 100sec total
  - *From: avataraim*

- **Audio + image to video workflow**
  - Use case: Combining custom audio with image input for video generation
  - *From: multiple users discussing*

- **2-stage generation with distill LoRA**
  - Use case: 20 steps first pass with bf16, then 8 steps distill second stage
  - *From: NebSH*

- **Spatial vs temporal model upscaling**
  - Use case: Spatial is for resolution, temporal is only for FPS
  - *From: Lodis*

- **Audio continuation workflow**
  - Use case: Can copy original audio and continue it or feed custom audio, works like MaskGCT but for video
  - *From: 421114995925843968*

- **Two-stage generation with upscaler**
  - Use case: Getting sharp results - first stage low res, second stage with spatial upscaler and detailer LoRA
  - *From: David Snow*

- **Keyframe test workflow**
  - Use case: Combining different images to make a video with movement
  - *From: Owlie*

- **Audio continuation workflow**
  - Use case: Extending video with consistent audio, requires proper CFG settings
  - *From: Kijai*

- **Two-stage generation with detailer lora**
  - Use case: High quality video generation using detailer lora on both first and second stages
  - *From: avataraim*

- **Audio voice refinement via TTS iterations**
  - Use case: Improving generated audio quality through multiple TTS passes
  - *From: Gleb Tretyak*

- **TTS Audio Suite workflow**
  - Use case: Fixing voices in generated videos, alternative to training voice LoRAs
  - *From: 722193816089788427*

- **Multi-stage sampling with different CFG**
  - Use case: First step with CFG4 and no distill lora, last 7 steps with CFG1 and distill lora
  - *From: N0NSens*

- **Spatial inpaint + first frame + depth control**
  - Use case: Basically have face control similar to VACE but without reference
  - *From: Hashu*

- **Two-stage generation with different models**
  - Use case: Use dev model for first pass, dev + distill LoRA for second pass upscaling to get better quality
  - *From: BobbyD4AI*

- **Video extension with keyframes**
  - Use case: Generate separate 121-frame sections and join them, splitting audio cleanly
  - *From: A.I.Warper*

- **Multiple keyframe workflow with custom audio**
  - Use case: Creating videos with multiple guided keyframes and custom audio, works without upscale
  - *From: FUNZO*

- **Video extension/temporal outpainting**
  - Use case: Take 5s clip and generate next 5s using LTXV Set Audio Video Mask By Time node
  - *From: 74637656272666624*

- **Audio + image generation workflow**
  - Use case: Adding sound to existing videos, available in specified channel from Kijai
  - *From: Moonbow*

- **Dev model + distill lora for upscaler**
  - Use case: Better audio quality - use dev model at basic sampler and dev model + distill lora at upscaler
  - *From: N0NSens*

- **Hybrid workflow using LTX with Kijai ComfyUI nodes**
  - Use case: Allows using GGUF and 4bit gemma
  - *From: zelgo_*

- **Combined audio + image with keyframes**
  - Use case: Prerecorded audio with images reacting to audio and singing
  - *From: Owlie*

- **Using compression settings to drive motion**
  - Use case: When not getting motion in generations, increase compression to help drive more motion
  - *From: Tachyon*

- **Multi-keyframe setup with AddGuide**
  - Use case: Creating videos with multiple keyframe conditioning points
  - *From: The Shadow (NYC)*

- **Split model workflow**
  - Use case: Loading model components separately to manage VRAM usage
  - *From: Kijai*

- **Keyframe workflow with LTXCropGuides**
  - Use case: Setting keyframes at specific indices then removing reference latents after generation
  - *From: 976496720370348032*

- **Multi-keyframe workflow with STG node**
  - Use case: Creating videos with multiple keyframes at specific positions
  - *From: The Shadow (NYC)*

- **Audio + first frame to video**
  - Use case: Start frame + audio input for video generation
  - *From: TK_999*

- **GGUF workflow with model switches**
  - Use case: Switching between different GGUF models in single workflow
  - *From: buggz*

- **Video and audio extension using masking**
  - Use case: Extending existing videos with new content while maintaining continuity
  - *From: 976496720370348032*

- **Multi-stage upscaling 256->512->1024->2048**
  - Use case: Progressive upscaling for higher resolution outputs, though color shifts occur at 2K
  - *From: KingGore2023*

- **Audio-video lip sync using V2V**
  - Use case: Creating lip-synced videos with better results than I2V approach
  - *From: KingGore2023*

- **I2V with audio masking and film grain preprocessing**
  - Use case: Creating lip-sync videos from images with proper motion
  - *From: Elvaxorn*

- **Video extension with turn-by-turn dialog**
  - Use case: Creating longer stories by extending video segments with different speakers
  - *From: 138332118890708992*

- **Continuous video generation using SVI method**
  - Use case: Generate longer videos by feeding last 9 frames from one generation into next for continuation
  - *From: ZombieMatrix*

- **Two-stage generation with spatial upscale**
  - Use case: Official workflow renders in 2 stages to achieve 1080p quality
  - *From: Christian Sandor*

- **Video-to-video using LTXVImgToVideoInplace**
  - Use case: Feed video directly into I2V node for video-to-video processing, can handle 721+ frames
  - *From: ZombieMatrix*

- **Three-pass generation with upscaler**
  - Use case: Using upscaler as third pass increases quality even more than two-pass
  - *From: David Snow*

- **SVI style infinite generation**
  - Use case: Can extend videos indefinitely using 3x5s segments with 1s crossover, though audio blending needs work
  - *From: ZombieMatrix*

- **Direct long generation without context windows**
  - Use case: 60s direct generation with single KSampler, maintains subject fidelity
  - *From: ZombieMatrix*

- **Q4 GGUF with distilled LoRA setup**
  - Use case: Memory-efficient generation with good quality using 8 steps
  - *From: 568465354158768129*

- **Two-stage generation with distilled LoRA**
  - Use case: T2V workflow using distilled LoRA in stage 2 for speed improvement
  - *From: 568465354158768129*

- **Using Wan2.2 for stage 1, then LTX2 for stage 2**
  - Use case: Compensating for LTX2's weakness in stage 1 generation
  - *From: KingGore2023*

- **Infinite length video generation workflow**
  - Use case: Creating extended video sequences beyond normal limits
  - *From: ZombieMatrix*

- **Adding audio to existing videos with very low denoise**
  - Use case: Audio generation for input video while keeping original video untouched
  - *From: 627140525916422145*

- **Infinite length video generation**
  - Use case: Creating long-form videos using anchor image method with cross points
  - *From: ZombieMatrix*

- **Two-stage I2V with different samplers**
  - Use case: First pass with euler_A, second pass with dpmpp_sde for speed/quality balance
  - *From: David Snow*

- **Audio-driven lip sync I2V**
  - Use case: Using audio input to drive facial animation with LoRAs for consistency
  - *From: dg1860*

- **Multi-keyframe I2V with audio**
  - Use case: 361 frames using first and 341st frame as keyframes with distilled lora and ic detailer lora
  - *From: Daflon*

- **Two-stage upscaling with distilled lora**
  - Use case: First stage sampling followed by upscaling pass using distilled lora
  - *From: multiple users*

- **Image-guided I2V with masked video**
  - Use case: First frame > middle guide frame > masked video for controlled generation
  - *From: TK_999*


## Recommended Settings

- **Steps for high quality**: 1201 steps
  - For maximum quality with SDE sampler, though very slow
  - *From: Benjimon*

- **Reserve VRAM**: --reserve-vram 8 or 5
  - For handling VRAM limitations and enabling system RAM offloading
  - *From: avataraim*

- **Temporal upscaler steps**: 4 steps
  - Using res_2s scheduler, better than 20 steps which causes artifacts
  - *From: TK_999*

- **Frame rate**: 24 fps
  - Standard used in official workflows, 24p in US, 25p elsewhere
  - *From: Daflon*

- **--reserve-vram**: 5
  - Helps with OOM issues by offloading to system RAM
  - *From: TK_999*

- **VAE decode overlap**: 4096
  - Set to avoid temporal tiling artifacts, but may cause high RAM usage
  - *From: Kiwv*

- **Steps for res2s sampler**: 25
  - Default used, but may test if less is sufficient
  - *From: Mandark*

- **Upscaler steps**: 20 steps, CFG 4
  - Testing configuration for spatial upscaler
  - *From: TK_999*

- **reserve-vram**: 4GB for 4090
  - Prevents OOM errors, can drop to 2-3GB for lower res/length
  - *From: Gill Bastar, Tachyon*

- **I2V strength**: Under 0.4 for movement
  - Higher values can cause frozen/static results
  - *From: Kijai*

- **I2V strength**: 0.8 for character preservation
  - Maintains character but loses identity faster
  - *From: Kijai*

- **I2V strength**: 1.0 for best character retention
  - Keeps character better but still loses it over time
  - *From: Kijai*

- **LTXVPreprocess strength**: 33 standard, increase for frozen videos
  - Higher values help unfreeze static results
  - *From: 976496720370348032*

- **Final resolution height**: Not over ~1000 pixels for base tile
  - Prevents artifacts and duplications
  - *From: 976496720370348032*

- **FPS encoding after temporal upscaler**: Double the original fps
  - Temporal upscaler doubles fps, need to encode at double rate or video looks slowmo
  - *From: 976496720370348032*

- **CFG scale for non-distilled**: 4.0
  - Default recommended setting for non-distilled models
  - *From: Kijai*

- **Steps for non-distilled**: 30 steps first sampler, 3 steps second sampler
  - Proper step count needed for full model quality
  - *From: Tachyon*

- **Steps for distilled**: 8 steps
  - Sufficient for distilled fp8 model
  - *From: Kijai*

- **Mask parameters**: mask_audio=True, mask_video=True
  - Will regenerate audio/video between mask_start_time and mask_end_time
  - *From: 976496720370348032*

- **--reserve-vram**: 4-6 for RTX 4090
  - Prevents OOM errors, higher values significantly slow performance
  - *From: protector131090*

- **Frame count for quality balance**: 960x960x571 at 30fps
  - Close to limit but works fine for quality/length balance
  - *From: seitanism*

- **Custom sigmas usage**: Use custom sigmas from distilled model
  - These are the ones used in distilling the distilled model
  - *From: 976496720370348032*

- **Spatial inpainting setup**: start_time=0, end_time=big number, mask_video=True, mask_audio=False
  - Generates just video latents and keeps audio
  - *From: 976496720370348032*

- **--reserve-vram**: 4-12 depending on use case
  - 4090 needs 4-5 minimum, up to 10+ with controlnet. 3090 users suggest 11-12. Value depends on resolution, frame count, models used
  - *From: Juan Gea, Q!, seitanism*

- **LTXVPreprocess strength**: 33+
  - High values help prevent frozen/static results in I2V
  - *From: 976496720370348032*

- **Temporal overlap in tiled decoder**: Minimum 0 (modify code)
  - Can improve results, default minimum is 16 but reducing helps
  - *From: 企鵝（50% CASH 50%GOLD）, tavi.halperin*

- **Page file size**: 60-100GB
  - Fixes random crashes, 100GB works well but 60GB may be enough
  - *From: Owlie*

- **CFG**: 1.0
  - Reduces VRAM usage by 4GB compared to higher CFG values
  - *From: Kijai*

- **Steps with distilled LoRA**: 8 or lower
  - Default workflow has 20 steps but distilled LoRA should use fewer steps
  - *From: MechanimaL*

- **Upscaling denoise**: 0.2
  - Lower denoise with shift 0.2-0.4 helps preserve details when upscaling
  - *From: dj47*

- **NVFP4 inference time**: 7.35s/it for 8 steps
  - 1920x1088x193 frames on 5090 with sage attention
  - *From: Kijai*

- **FPS**: 25
  - Official model training framerate, shown on website
  - *From: Kiwv*

- **Reserve VRAM**: 4-9 depending on setup
  - Prevents OOM during generation, 9 seems optimal for 5090 8-second I2V
  - *From: toxicvenom117*

- **Resolution for working setup**: 1280x704
  - Works for all setups, can multiply by 2 for higher res
  - *From: avataraim*

- **Frame count**: 121 frames standard, up to 334+ possible
  - Model can handle longer sequences, 20 seconds official, 30+ seconds seen working
  - *From: multiple users*

- **Steps for full model**: 40 steps
  - Reference code default, 20 steps only works with distill LoRA
  - *From: Kijai*

- **CFG for full model**: 3
  - Original code uses CFG 3, not 4 like some examples
  - *From: Kijai*

- **Page file size**: 64-65GB
  - Needed if under 100GB RAM to prevent crashes
  - *From: Tachyon*

- **Reserve VRAM**: Start with 1 or 2
  - For slow I2V performance issues
  - *From: Kijai*

- **CFG**: 4
  - For full model with 20-30 steps to avoid audio degradation
  - *From: ZeusZeus (RTX 4090)*

- **CFG**: 1
  - For distilled model, disable distilled LoRA when using this
  - *From: ZeusZeus (RTX 4090)*

- **Steps**: 20-30
  - Minimum steps for undistilled model, low steps produce bad results
  - *From: ZeusZeus (RTX 4090)*

- **--reserve-vram**: 2
  - Reserves 2GB VRAM, improved speed from 06:12<21:04 to 01:01<01:19
  - *From: NebSH*

- **VAE tile size**: 1536
  - Better performance on 4090, default is 512
  - *From: David Snow*

- **Audio fps**: 48
  - Must be changed along with video fps when generating at double rate
  - *From: Juan Gea*

- **--reserve-vram**: 6GB for 4K on RTX 4090
  - Enables 4K generation without OOM
  - *From: Kijai*

- **Detailer lora strength**: 0.5-0.75
  - Optimal quality improvement without artifacts
  - *From: David Snow*

- **Full model CFG and steps**: CFG 3.5, 40 steps
  - Default settings for full model
  - *From: NebSH*

- **Distilled model settings**: CFG 1 with distill lora
  - Standard configuration for distilled workflow
  - *From: gopnik*

- **1920x1088 generation**: CFG 3.5, 40 steps, FPS 24, euler_ancestral, distilled lora str 1, detailer lora 0.75 str on both stages, --reserve-vram 6GB
  - Successfully tested on RTX 4090 without OOM
  - *From: gopnik*

- **NAG impact on generation time**: ~10% slower
  - Performance impact is relatively minimal for the quality improvement
  - *From: Kijai*

- **Distill LoRA strength for second stage**: 0.9
  - Appears to improve quality compared to full strength
  - *From: IceAero*

- **Resolution for testing**: 1280x704 for normal, 2560x1408 possible on RTX 3090
  - Workflow was originally set for 2K, normal resolution is lower
  - *From: avataraim*

- **Enhance-A-Video strength**: 8.0 tested without breaking
  - Surprisingly high values can work without issues
  - *From: David Snow*

- **Dev model recommended settings**: 40 steps, CFG 4, Euler sampler
  - Standard workflow parameters mentioned by experienced users
  - *From: Hashu*

- **I2V without distill LoRA**: 1st stage: Euler 40 steps CFG 3, 2nd stage: Euler 8 steps CFG 3
  - Recommended for experiencing I2V at its fullest
  - *From: toxicvenom117*

- **Distill LoRA negative weight**: -0.3 to -0.6
  - Fixes plastic skin while maintaining speed benefits
  - *From: David Snow*

- **SLG block selection**: Block 2
  - Good balance, not too strong like block 1
  - *From: Kijai*

- **Distil LoRA weight on upscale**: -0.5
  - Reduces shiny skin and AI contrast issues
  - *From: David Snow*

- **VRAM reserve**: 12GB
  - For heavy LoRA usage, though 6GB might be sufficient
  - *From: David Snow*

- **CFG for distil model**: 1.0
  - Recommended CFG setting for distilled model
  - *From: David Snow*

- **Frame intervals**: 8
  - LTX model uses 8-frame intervals (not 4n+1)
  - *From: TK_999*

- **Enhance-a-Video weight**: 2.0
  - Starting recommendation
  - *From: Kijai*

- **I2V mask level threshold**: under 0.3
  - If no movement below this, something is broken
  - *From: Kijai*

- **I2V mask level**: 0.5 on first and last
  - User example for troubleshooting static output
  - *From: Gleb Tretyak*

- **Compression level**: 40ish max tested
  - Maximum compression tested by developer
  - *From: Kijai*

- **Native LTX sampler**: res_2s
  - Default sampler used in native workflows
  - *From: Tachyon*

- **ComfyUI sampler**: Euler
  - Default sampler in ComfyUI
  - *From: Tachyon*

- **Preferred samplers**: lcm and er_sde
  - Developer preferences - lcm for standard, er_sde for stronger option
  - *From: Kijai*

- **CFG value for distilled model**: 1.0
  - Distilled model designed to work at CFG=1
  - *From: 976496720370348032*

- **Steps for full model without distill LoRA**: 40
  - Need higher steps for quality without distillation
  - *From: Tachyon*

- **Steps for distilled model**: 8 + 3
  - Default working configuration
  - *From: zelgo_*

- **Upscale steps**: 2-3 steps
  - Second stage upscaling requires fewer steps, specified by sigmas to control creativity level
  - *From: 976496720370348032*

- **Image compression for stylized images**: 40-90
  - Higher compression helps with motion in stylized content
  - *From: N0NSens*

- **Conditioning strength for I2V**: Less than 1.0
  - Helps avoid second frame cuts by allowing model to modify latent
  - *From: 976496720370348032*

- **Detail daemon settings from David Snow**: Referenced workflow settings
  - Proven settings for good results
  - *From: Gleb Tretyak*

- **--reserve-vram**: 6-7 for high resolution
  - Prevents OOM at huge resolutions due to estimation issues
  - *From: Kijai*

- **Distilled model steps**: 8 steps with 1 CFG
  - Standard configuration for distilled model
  - *From: buggz*

- **Dev model steps**: 20 steps with CFG 4
  - Standard configuration for dev model
  - *From: buggz*

- **VRAM usage target**: 90-95% max
  - Prevents Windows shared memory slowdown
  - *From: Kijai*

- **temporal_tile_length**: 16-24
  - Default 16 is safe, 24 almost causes OOM, 50 causes cooking/performance issues
  - *From: garbus*

- **image_compression**: 40
  - Increases from default 30-33 to fix slideshow behavior
  - *From: foxydits*

- **image_strength**: 0.8
  - Lower values help avoid slideshow/zoom behavior
  - *From: garbus*

- **CFG**: 4
  - Default setting for fp8 full model with proper step counts
  - *From: Tachyon*

- **--reserve-vram**: 8
  - Improved second sampler speed to 11s/it on 1088p 193 frames
  - *From: 217076219072479232*

- **Audio start time**: 0.2 or higher
  - Prevents static video at beginning when audio start time equals video start time
  - *From: Elvaxorn*

- **Reserve VRAM**: 7
  - Needed for I2V with 384 LoRA on high VRAM cards
  - *From: Kijai*

- **Detail Daemon strength**: 0.4 for normal, up to 5.0 for overkill
  - Higher values provide more detail enhancement
  - *From: David Snow*

- **Page file size**: 65GB
  - Prevents ComfyUI crashes when system runs out of RAM
  - *From: Tachyon*

- **Distill LoRA strength**: 0.8 to 1.0
  - For use with fp8-dev model in I2V
  - *From: Tachyon*

- **memory_usage_factor**: 0.2 for safety, 0.16 for 5090
  - Prevents I2V VRAM issues and freezing at higher resolutions
  - *From: Elvaxorn*

- **reserve-vram**: 4-20 depending on card
  - Alternative solution for VRAM issues, achieves same offloading as memory_usage_factor
  - *From: Kijai*

- **image compression**: 0 for character consistency, 32-33 default
  - Lower values maintain character better, higher values allow more motion
  - *From: Kijai*

- **detailer LoRA strength**: 0.2
  - Low value prevents artifacts while improving details
  - *From: David Snow*

- **Compression strength**: 0.50
  - Helps with motion generation by providing compression artifacts for LTX to interpret
  - *From: hicho*

- **LoRA strength**: 0.6
  - Better results than default 1.0 setting in ComfyUI workflow
  - *From: MechanimaL*

- **Steps for audio quality**: 40 steps
  - 40 steps compared to 20 gives much cleaner and consistent audio
  - *From: IceAero*

- **Max shift**: 1.88
  - Lower than default steep settings for better results
  - *From: TK_999*

- **Frame calculation**: Always divisible by 8, then add 1 (e.g., 152/8 + 1 = 153 for 25fps 6-second video)
  - Required for proper model function
  - *From: Choowkee*

- **Reserve VRAM**: 4GB for high resolution i2v
  - Prevents OOM on higher resolutions
  - *From: Tachyon*

- **Spatial upscaler tiles**: Use more tiles for memory management
  - Prevents OOM during spatial upscaling
  - *From: 568465354158768129*

- **ComfyUI launch flags**: --normalvram --preview-method none
  - Works well for RTX 4060 TI 16GB setup
  - *From: 568465354158768129*

- **FPS**: 25 fps instead of 24 fps
  - Much better results, more like Pixar/Disney movie quality
  - *From: 568465354158768129*

- **Resolution**: 1440x800 or 1920x1080 minimum
  - Better results than lower resolutions
  - *From: 568465354158768129*

- **Distilled LoRA strength**: 0.8 instead of 1.0
  - Makes skin look less plastic/waxy
  - *From: 568465354158768129*

- **Sampler**: euler_sde instead of euler
  - Better results in certain cases, made things better
  - *From: 568465354158768129*

- **Steps for res2 sampler**: Half the steps compared to euler
  - res2 sampler requires half the steps of standard samplers
  - *From: 568465354158768129*

- **VAE decode tiling**: 4 4 4 instead of 512
  - Doesn't matter much for video quality but more efficient
  - *From: KingGore2023*

- **Image strength**: 0.6 default
  - Controls how much generation can change the first frame, 1.0 keeps it as-is, 0.0 almost ignores input
  - *From: zelgo_*

- **Detail daemon**: 0.25 on second pass
  - Adds detail without being too aggressive
  - *From: David Snow*

- **Enhance a video**: 4 on both passes
  - Consistent enhancement across pipeline
  - *From: David Snow*

- **FPS**: 48-50 fps
  - Reduces motion artifacts and texture smearing
  - *From: David Snow*

- **Distilled lora strength**: 1.0
  - Better results than lower values like 0.2
  - *From: seitanism*

- **CFG schedule**: Start at 3, end at 0.2
  - Works well with dynamic lora at 0.8 strength
  - *From: The Shadow (NYC)*

- **Chunking**: 4 chunks
  - Ensures VRAM usage below other functions, 2 chunks cuts peak but 4 is safer
  - *From: Kijai*

- **Steps for distilled model**: 40 steps first stage, 3 steps second stage
  - Standard configuration for two-stage workflow
  - *From: nacho.money*


## Concepts Explained

- **SDE vs ODE samplers**: SDE samplers add noise every step for quality/exploration/error-correction but need more steps. ODE samplers (euler, dpm, unipc, deis) just solve equations to sample, faster but potentially lower quality
  - *From: mallardgazellegoosewildcat2*

- **Abliteration**: Removes internal censoring biases in models, makes them uncensored but potentially less intelligent
  - *From: Kiwv*

- **NVFP4**: FP4 quantization format proprietary to NVIDIA 5000 series (Blackwell) cards
  - *From: Kiwv*

- **Abliteration**: Process to uncensor models, new method causes less IQ loss compared to old style
  - *From: Mandark*

- **Projections only model**: Separated projection components from main checkpoint to reduce disk usage and fix low VRAM issues
  - *From: yi*

- **Temporal tiling artifacts**: Nasty artifacts that occur with many video models during VAE decode
  - *From: TK_999*

- **Abliterated model**: Model finetuned to remove censoring bias, won't say 'sorry I can't do that', gives more accurate prompts in iffy territory
  - *From: Kiwv*

- **LTXVPreprocess/CRF**: Adds h.264-like compression artifacts to images to bridge train-test gap between real video frames and pristine T2I images
  - *From: 976496720370348032*

- **Latent guides**: Used for controlling generation with reference frames, strength <1.0 gives more freedom, 1.0 for most important keyframes
  - *From: 976496720370348032*

- **Audio/Video masking**: mask_audio=True means regenerate audio between mask times, mask_video=True means regenerate video - think of mask as the verb to edit
  - *From: 976496720370348032*

- **Slope_len parameter**: Method for building phase-in-phase-out with original video pixels, a kind of crossfade that determines blend coefficients
  - *From: 976496720370348032*

- **V2V latent processing**: Video-to-video processing in latent space allows for better quality upscaling and modifications
  - *From: hicho*

- **res_2s scheduler**: Does 2 steps within 1 step, so 20 steps = effectively 80 steps
  - *From: yi*

- **Latent volume constraint**: WxHxF (width x height x frames) of video sections affects quality. Not about original video length but the latent volume used
  - *From: 976496720370348032*

- **Spatial vs temporal inpainting**: Spatial = generating parts of frames/all frames with masks. Temporal = regenerating certain sections of video/audio timeline
  - *From: 976496720370348032*

- **projections_only**: Component used with gemma text encoder to reduce size, part of FP8 optimization
  - *From: BobbyD4AI*

- **Execution Order Controller**: Ensures gemma text encoder loads and runs first, then unloads to free memory for next model - reduces VRAM consumption
  - *From: mkupchik_lightricks*

- **LTXVPreprocess img_compression parameter**: Using larger values can help with memory issues and model performance
  - *From: mkupchik_lightricks*

- **Comfy-kitchen**: PyTorch extension layer that adds NVIDIA-specific low-bit (FP8/FP4) tensor layouts and kernels for LTX 2's NVFP4 checkpoints to run fast and fit in VRAM
  - *From: Grimm1111*

- **Latent masking for continuation**: Model can attend to masked latents whether they're before or after the regenerated region, enabling flexible video editing
  - *From: 976496720370348032*

- **Reference latent mechanism**: LoopingSampler conditions on last part of previous video using reference latents rather than direct masking
  - *From: 976496720370348032*

- **Reserve VRAM**: Blocks a certain amount of VRAM from being used by ComfyUI for inference, helps prevent OOM
  - *From: 224611423869730818*

- **Abliterated models**: Models with safety blocks removed, but don't suddenly unlock much - real changes are in retrained models that alter token usage
  - *From: Scruffy*

- **Batch size in training**: Amount of videos evaluated per step in training - more videos gives more accurate evaluation but doesn't speed up training
  - *From: Kiwv*

- **Manual sigmas**: Steps/denoise rate values that don't have names unlike scheduler-generated sigmas
  - *From: yi*

- **Pinned memory**: Feature that makes offloading faster by a lot sometimes, enabled by default
  - *From: Kijai*

- **Cache strategies**: cache-none executes every node each run with reduced RAM/VRAM usage, cache-ram uses RAM pressure caching with threshold
  - *From: Kijai*

- **Noise injection in latent space**: Adding noise to latent representation rather than image level to create motion in static inputs
  - *From: Lodis*

- **Distilled LoRA vs distilled model**: Distilled LoRA is for two-pass procedure, distilled model is direct replacement - don't use both together
  - *From: Lodis*

- **fp8 scaled**: A specific type of fp8 quantization that's closer to full precision than regular fp8
  - *From: Kijai*

- **Temporal overlap in VAE**: LTX's VAE has temporal convolutions that create boundary effects on temporal tiles - overlap prevents artifacts
  - *From: 976496720370348032*

- **LL and LN notation**: L=lora, N=none. So LN means lora on first pass, none on second pass
  - *From: David Snow*

- **NAG for LTX**: Negative Attention Guidance works with LTX - just one extra crossattn call without significant slowdown
  - *From: Kijai*

- **NAG (Negative Audio/visual Guidance)**: System for adding negative prompts to avoid unwanted elements in both video and audio generation
  - *From: Kijai*

- **Joint model architecture**: LTX Video 2 requires video part even for audio-only generation since it's a unified model
  - *From: Kijai*

- **Distill strength adjustment**: Can modify the strength of distillation even when using pre-distilled models
  - *From: Kijai*

- **Embedding connectors**: Additional layers for the text encoder stored in checkpoints, separate files available when not using full checkpoint
  - *From: Kijai*

- **CFG batching**: When ComfyUI has enough memory, it batches positive and negative inputs into single model run instead of separate runs - uses more memory but can be faster
  - *From: Kijai*

- **Distil LoRA negative weight**: Using LoRA at negative weight to counteract effects - works because LoRA represents difference between distill and dev models
  - *From: Kijai*

- **Embedding connector weights difference**: Dev and distill models have different embedding connector weights, and LoRA doesn't include this difference
  - *From: Kijai*

- **Embedding connector weights**: Normally in checkpoint file, separate files needed when using GGUF or separate diffusion models instead of checkpoints
  - *From: Kijai*

- **Dynamic rank reduction**: Method to reduce LoRA size while retaining specified percentage of fro value per layer
  - *From: Kijai*

- **SLG**: Works well with CFG for few steps with distilled model
  - *From: Kijai*

- **Embedder_connector weights**: Section that connects between Gemma text encoder and the main model, has different weights between dev and distill models
  - *From: Kijai*

- **Reference latent technique**: Method used for keyframe conditioning where model attends to dedicated latent frame rather than direct tensor insertion
  - *From: 976496720370348032*

- **Mask level conditioning**: Value (1 - strength) determines noise level applied to latent, with 1.0 keeping unmodified and lower values allowing model modification
  - *From: 976496720370348032*

- **Cross-modal guidance (sm)**: Parameter controlling how tightly video generation follows audio conditioning, critical for lip sync and timing
  - *From: Chandler ✨ 🎈*

- **Strength parameter in keyframes**: Controls influence towards reference image - high strength pushes towards ref image
  - *From: The Shadow (NYC)*

- **STG sigmas**: Sigmas in STG node are not used directly, closest one from real sigmas is chosen instead
  - *From: Gleb Tretyak*

- **Model activations vs weights**: Model size is static, VRAM usage varies on input size due to temporary tensors and activations
  - *From: Kijai*

- **Activations vs model weights**: VRAM offload only affects model weights, activations still need to fit in VRAM for generation
  - *From: Kijai*

- **Peak VRAM consumption**: Usually occurs at feed forward activation stage, most critical for memory management
  - *From: Kijai*

- **slope_len parameter**: Creates fading intensity latent mask affecting masked frames to different degrees, works in 8-frame increments, values below 8 have no effect
  - *From: 138332118890708992*

- **Dev connector**: Additional layers between the text encoder and the model, different in distill vs dev model
  - *From: Kijai*

- **Macroblock noise**: Type of noise from JPEG compression similar to MPEG video compression that model associates with cinematic sequences
  - *From: 138332118890708992*

- **embedding_connector**: Component that changes based on model type (dev vs distilled), affects output when mixed between model types
  - *From: Kijai*

- **per-token timestep handling**: Memory inefficient process causing I2V to use gigabytes more VRAM than T2V, similar to WAN 5B issue
  - *From: Kijai*

- **IC LoRA**: Image Conditioning LoRA that requires guides/reference images, used for detailing and upscaling
  - *From: Kijai*

- **Timestep embedding optimization**: Creating timestep embed per token when using masks creates huge tensors with mostly identical values. Optimization only does embeddings for unique timesteps then expands later
  - *From: Kijai*

- **Abliterated text encoders**: Modified text encoders that remove safety restrictions, but don't uncensor the underlying diffusion model which wasn't trained on NSFW content
  - *From: Kiwv*

- **Distilled LoRA**: A compressed version that provides speedup for inference, works with both GGUF and regular models
  - *From: multiple users*

- **Mixed layer approach**: Quantization method used in Q4 and below, Q5 and above use different approach
  - *From: Kijai*

- **Manual sigmas**: Setting used in stage 2 when reducing acceleration weight - typically increase steps manually when using manual sigmas
  - *From: ラD.*

- **Noise compression**: Process to introduce H.264-like compression artifacts to simulate video frames and encourage motion in the model
  - *From: 976496720370348032*

- **Reference image resizing in I2V**: ComfyUI I2V workflow resizes image so longest side is 1536 for proper noise compression, image isn't supposed to be same size as latent
  - *From: Kijai*

- **Image strength in I2V**: Controls how much the generation can deviate from the input image - higher values keep closer to original, lower values allow more change
  - *From: 138332118890708992*

- **Character drift**: Issue where character appearance changes during video generation, especially noticeable in second pass upscaling
  - *From: David Snow*

- **8+1 frame rule**: Frame count must be 1 modulus 8 (leave remainder of 1 when divided by 8) due to how LTXV video latents work - 8 latent frames per pixel frame plus one for initial image
  - *From: 976496720370348032*

- **FPS vs frame count confusion**: FPS for conditioning the model's motion speed is different from encoding FPS and different from total frame count requirements
  - *From: 976496720370348032*

- **Audio latent granularity**: Audio latents are 25 latents per second and have different time granularity than video, making cutting/splicing complex
  - *From: 976496720370348032*


## Resources & Links

- **LTX-2 FP4 model** (model)
  - https://huggingface.co/Lightricks/LTX-2/blob/main/ltx-2-19b-dev-fp4.safetensors
  - *From: Mandark*

- **Gemma abliterated model** (model)
  - https://huggingface.co/mlabonne/gemma-3-12b-it-abliterated-v2
  - *From: Kiwv*

- **Audio super resolution** (tool)
  - https://github.com/haoheliu/versatile_audio_super_resolution
  - *From: Kiwv*

- **First Frame to Last Frame workflow** (workflow)
  - https://gist.github.com/kabachuha/dafd6952bdc00050b4d6b594d11bec6c
  - *From: Tachyon*

- **Lightweight Gemma FP4** (model)
  - https://huggingface.co/GitMylo/LTX-2-comfy_gemma_fp8_e4m3fn/resolve/main/ltx-2-19b-dev-fp4_projections_only.safetensors
  - *From: avataraim*

- **ComfyUI BF16 support PR** (repo)
  - https://github.com/Comfy-Org/ComfyUI/pull/11713
  - *From: patientx*

- **Example workflows** (workflow)
  - https://github.com/Lightricks/ComfyUI-LTXVideo/tree/master/example_workflows
  - *From: Xor*

- **Better abliteration technique** (repo)
  - https://huggingface.co/blog/grimjim/norm-preserving-biprojected-abliteration
  - *From: Mandark*

- **LTX-2-comfy_gemma_fp8_e4m3fn** (model)
  - https://huggingface.co/GitMylo/LTX-2-comfy_gemma_fp8_e4m3fn
  - *From: Phr00t*

- **LTX Detailer LoRA** (lora)
  - https://huggingface.co/Lightricks/LTX-2-19b-IC-LoRA-Detailer
  - *From: N0NSens*

- **ComfyUI LTX2 workflows** (workflow)
  - https://blog.comfy.org/p/ltx-2-open-source-audio-video-ai
  - *From: Tachyon*

- **SageAttention for Windows** (repo)
  - https://github.com/sdbds/SageAttention-for-windows
  - *From: Tachyon*

- **Triton for Windows** (repo)
  - https://github.com/woct0rdho/triton-windows
  - *From: Tachyon*

- **PainterLTXV2** (repo)
  - https://github.com/princepainter/ComfyUI-PainterLTXV2
  - *From: avataraim*

- **Gemma-3-12b-Abliterated-LTX2** (model)
  - https://huggingface.co/FusionCow/Gemma-3-12b-Abliterated-LTX2/tree/main
  - *From: Kiwv*

- **ComfyUI_MusicTools for voice naturalization** (tool)
  - https://github.com/jeankassio/ComfyUI_MusicTools
  - *From: Xor*

- **AudioBatch for audio channel conversion** (tool)
  - https://github.com/set-soft/ComfyUI-AudioBatch
  - *From: 421114995925843968*

- **Video upscale using WAN FusionX** (workflow)
  - https://civitai.com/models/1714513/video-upscale-or-enhancer-using-wan-fusionx-ingredients
  - *From: Samuca*

- **ComfyUI-AudioSR wrapper** (tool)
  - https://github.com/Saganaki22/ComfyUI-AudioSR
  - *From: drbaph*

- **AudioSR model** (model)
  - https://huggingface.co/drbaph/AudioSR
  - *From: drbaph*

- **LTX-2 ICLoRA workflow** (workflow)
  - https://github.com/Lightricks/ComfyUI-LTXVideo/blob/master/example_workflows/LTX-2_ICLoRA_All_Distilled.json
  - *From: 976496720370348032*

- **Transformer-only model variants** (model)
  - https://huggingface.co/Kijai/LTXV2_comfy/blob/main/diffusion_models/ltx-2-19b-distilled-fp8_transformer_only.safetensors
  - *From: Kijai*

- **LTX Video official workflows** (workflow)
  - https://github.com/Lightricks/ComfyUI-LTXVideo/tree/master/example_workflows
  - *From: MechanimaL*

- **Smaller Gemma3 quantized model** (model)
  - https://huggingface.co/unsloth/gemma-3-12b-it-bnb-4bit/tree/main
  - *From: MechanimaL*

- **LTX-2 GGUF transformer** (model)
  - https://huggingface.co/smthem/LTX-2-Test-gguf/tree/main
  - *From: zelgo_*

- **Alternative Gemma3 models for testing** (model)
  - https://huggingface.co/reedmayhew/Suno-Song-Generator-gemma3-12B-HF
  - *From: Scruffy*

- **Anti-slop Gemma3 model** (model)
  - https://huggingface.co/sam-paech/gemma-3-12b-it-antislop
  - *From: Scruffy*

- **ComfyUI LTXVideo custom nodes** (repo)
  - https://github.com/Lightricks/ComfyUI-LTXVideo
  - *From: NebSH*

- **IC Detailer LoRA** (lora)
  - https://huggingface.co/Lightricks/LTX-2-19b-IC-LoRA-Detailer/blob/main/ltx-2-19b-ic-lora-detailer.safetensors
  - *From: scf*

- **AudioSR for audio upscaling** (tool)
  - https://github.com/Saganaki22/ComfyUI-AudioSR
  - *From: 976496720370348032*

- **FP8 Gemma text encoder** (model)
  - https://huggingface.co/GitMylo/LTX-2-comfy_gemma_fp8_e4m3fn
  - *From: GalaxyTimeMachine (RTX4090)*

- **FlashSR for audio processing** (tool)
  - https://github.com/ysharma3501/FlashSR
  - *From: 224611423869730818*

- **Versatile Audio Super Resolution** (tool)
  - https://github.com/haoheliu/versatile_audio_super_resolution
  - *From: MOV*

- **LTX-2 example workflows** (workflow)
  - https://github.com/Lightricks/ComfyUI-LTXVideo/tree/master/example_workflows
  - *From: The Shadow (NYC)*

- **Gemma 3 12B model for LTXV Audio Text Encoder** (model)
  - https://huggingface.co/Comfy-Org/ltx-2/blob/main/split_files/text_encoders/gemma_3_12B_it.safetensors
  - *From: yi*

- **FP8 Gemma model** (model)
  - https://huggingface.co/GitMylo/LTX-2-comfy_gemma_fp8_e4m3fn/blob/main/gemma_3_12B_it_fp8_e4m3fn.safetensors
  - *From: yi*

- **ComfyUI memory management PR** (repo)
  - https://github.com/Comfy-Org/ComfyUI/pull/11741
  - *From: Kijai*

- **Video upscale workflow using WAN** (workflow)
  - https://civitai.com/models/1714513/video-upscale-or-enhancer-using-wan-fusionx-ingredients
  - *From: dj47*

- **ComfyUI AudioMass node** (node)
  - https://github.com/jtydhr88/ComfyUI-AudioMass
  - *From: Kagi*

- **ComfyUI nodes registry for audio** (tool)
  - https://registry.comfy.org/?nodes_index%5Bquery%5D=audio
  - *From: Kagi*

- **LTX-2 prompting guide** (guide)
  - https://ltx.io/model/model-blog/prompting-guide-for-ltx-2
  - *From: avataraim*

- **NVFP4 model** (model)
  - https://huggingface.co/Lightricks/LTX-2/blob/main/ltx-2-19b-dev-fp4.safetensors
  - *From: seitanism*

- **TEAR LoRA** (lora)
  - https://huggingface.co/oumoumad/LTX-2-19b-LoRA-TEAR/tree/main
  - *From: hicho*

- **Gemma 3 12b model** (model)
  - https://huggingface.co/google/gemma-3-12b-it-qat-q4_0-unquantized
  - *From: theUnlikely*

- **Gemma-3-12b-Abliterated-LTX2** (model)
  - https://huggingface.co/FusionCow/Gemma-3-12b-Abliterated-LTX2/tree/main
  - *From: TK_999*

- **Featherless AI model search** (resource)
  - https://featherless.ai/model-families/gemma3/12b
  - *From: Scruffy*

- **HuggingFace search tool** (tool)
  - https://hf.tst.eu
  - *From: Scruffy*

- **CrystalDiskInfo** (tool)
  - https://sourceforge.net/projects/crystaldiskinfo/
  - *From: garbus*

- **LTXV2_comfy weights** (model)
  - https://huggingface.co/Kijai/LTXV2_comfy/tree/main
  - *From: yi*

- **LTX-2-SDNQ-4bit-dynamic** (model)
  - https://huggingface.co/Disty0/LTX-2-SDNQ-4bit-dynamic
  - *From: cocktailprawn1212*

- **Audio-video model research paper** (research)
  - https://arxiv.org/abs/2601.04151
  - *From: yi*

- **ComfyUI Noise nodes** (repo)
  - https://github.com/BlenderNeko/ComfyUI_Noise
  - *From: Lodis*

- **LTX ComfyUI official** (repo)
  - https://github.com/Lightricks/ComfyUI-LTXVideo
  - *From: NebSH*

- **Kijai GGUF models** (model)
  - https://huggingface.co/Kijai/LTXV2_comfy/tree/main/diffusion_models
  - *From: Kijai*

- **Vantage GGUF fork** (repo)
  - https://github.com/vantagewithai/Vantage-GGUF
  - *From: Kijai*

- **ComfyUI-GGUF PR #399** (repo)
  - https://github.com/city96/ComfyUI-GGUF/pull/399
  - *From: Kijai*

- **LTX Detailer LoRA** (model)
  - https://huggingface.co/Lightricks/LTX-2-19b-IC-LoRA-Detailer/tree/main
  - *From: zelgo_*

- **Gemma 4bit GGUF** (model)
  - https://huggingface.co/unsloth/gemma-3-12b-it-bnb-4bit/tree/main
  - *From: zelgo_*

- **Vantage LTX GGUF variants** (model)
  - https://huggingface.co/vantagewithai/LTX-2-GGUF/tree/main
  - *From: yi*

- **Calcuis GGUF nodes** (repo)
  - https://github.com/calcuis/gguf
  - *From: yi*

- **City96 GGUF loader PR** (repo)
  - https://github.com/city96/ComfyUI-GGUF/pull/399
  - *From: Kijai*

- **ComfyUI memory management improvement** (repo)
  - https://github.com/Comfy-Org/ComfyUI/pull/11748
  - *From: yi*

- **ComfyUI preview latent support** (repo)
  - https://github.com/Comfy-Org/ComfyUI/pull/11741
  - *From: Kijai*

- **Adaptive Guidance for ComfyUI** (repo)
  - https://github.com/asagi4/ComfyUI-Adaptive-Guidance
  - *From: Kijai*

- **Mac-compatible MelBandRoFormer** (repo)
  - https://github.com/Brainkeys/ComfyUI-MelBandRoFormer-Mac/tree/main
  - *From: buggz*

- **LTX training example** (model)
  - https://huggingface.co/kabachuha/ltx2-hydraulic-press
  - *From: 224611423869730818*

- **LTX VAE location** (model)
  - Kijai's HuggingFace
  - *From: Juan Gea*

- **FP8 scaled Gemma 3 text encoder** (model)
  - https://huggingface.co/Comfy-Org/ltx-2/blob/main/split_files/text_encoders/gemma_3_12B_it_fp8_scaled.safetensors
  - *From: Kijai*

- **Enhance-A-Video** (tool)
  - https://github.com/NUS-HPC-AI-Lab/Enhance-A-Video
  - *From: Kijai*

- **GGUF loader options** (tool)
  - https://github.com/city96/ComfyUI-GGUF/pull/399
  - *From: Kijai*

- **Gemma-3-12b-Abliterated single file** (model)
  - https://huggingface.co/FusionCow/Gemma-3-12b-Abliterated-LTX2/tree/main
  - *From: yi*

- **LTX-2 dev embeddings connector** (model)
  - https://huggingface.co/Kijai/LTXV2_comfy/blob/main/text_encoders/ltx-2-19b-embeddings_connector_dev_bf16.safetensors
  - *From: Kijai*

- **LTX-2 distill embeddings connector** (model)
  - https://huggingface.co/Kijai/LTXV2_comfy/blob/main/text_encoders/ltx-2-19b-embeddings_connector_distill_bf16.safetensors
  - *From: Kijai*

- **Gemma 3 GGUF support PR** (repo)
  - https://github.com/city96/ComfyUI-GGUF/pull/402
  - *From: Kijai*

- **QuantStack LTX-2 GGUF models** (model)
  - https://huggingface.co/QuantStack/LTX-2-GGUF/tree/main/LTX-2-dev
  - *From: zelgo_*

- **Alternative LTX-2 GGUF models** (model)
  - https://huggingface.co/vantagewithai/LTX-2-GGUF/tree/main/dev
  - *From: Miku*

- **Comfy-Org LTX-2 Gemma fpmixed** (model)
  - https://huggingface.co/Comfy-Org/ltx-2/blob/main/split_files/text_encoders/gemma_3_12B_it_fpmixed.safetensors
  - *From: comfy*

- **Comfy-Org LTX-2 Gemma fp4_mixed** (model)
  - https://huggingface.co/Comfy-Org/ltx-2/blob/main/split_files/text_encoders/gemma_3_12B_it_fp4_mixed.safetensors
  - *From: comfy*

- **Abliterated Gemma model** (model)
  - https://huggingface.co/FusionCow/Gemma-3-12b-Abliterated-LTX2/tree/main
  - *From: David Snow*

- **LTX Video example workflows** (workflow)
  - https://github.com/Lightricks/ComfyUI-LTXVideo/tree/master/example_workflows
  - *From: David Snow*

- **City96 GGUF LTX support pull requests** (repo)
  - https://github.com/city96/ComfyUI-GGUF/pull/399 and https://github.com/city96/ComfyUI-GGUF/pull/402
  - *From: japar*

- **Kijai LTXV2 ComfyUI repo** (repo)
  - https://huggingface.co/Kijai/LTXV2_comfy
  - *From: Gleb Tretyak*

- **Dynamic rank reduced distill lora** (model)
  - https://huggingface.co/Kijai/LTXV2_comfy/tree/main/loras
  - *From: Kijai*

- **Required ComfyUI commit** (repo)
  - https://github.com/Comfy-Org/ComfyUI/commit/bd0e6825e84606e0706bbb5645e9ea1f4ad8154d
  - *From: Kijai*

- **Shutter Encoder** (tool)
  - https://www.shutterencoder.com/
  - *From: Kijai*

- **Owlie's prompt example** (workflow)
  - https://pastebin.com/7WhL0HWj
  - *From: Owlie*

- **ComfyUI image examples** (workflow)
  - https://files.catbox.moe/5uy9w5.png and https://files.catbox.moe/ara1ck.png
  - *From: Owlie*

- **Gemma 3 12b Abliterated** (model)
  - https://huggingface.co/FusionCow/Gemma-3-12b-Abliterated-LTX2/tree/main
  - *From: David Snow*

- **Vantage-GGUF fork** (repo)
  - https://github.com/vantagewithai/Vantage-GGUF
  - *From: Kijai*

- **Gemma tokenizer files** (model)
  - https://huggingface.co/smhf72/gemma-3-12b-it-extras-comfy
  - *From: yi*

- **FP4 text encoders** (model)
  - https://huggingface.co/Comfy-Org/ltx-2/tree/main/split_files/text_encoders
  - *From: zelgo_*

- **GGUF text encoders** (model)
  - https://huggingface.co/Kijai/LTXV2_comfy/tree/main/text_encoders
  - *From: buggz*

- **Official LTX workflows** (workflow)
  - https://github.com/Lightricks/ComfyUI-LTXVideo/tree/master/example_workflows
  - *From: 976496720370348032*

- **LTX-2 paper** (research)
  - https://arxiv.org/abs/2601.03233
  - *From: Chandler ✨ 🎈*

- **24GB VRAM fix** (guide)
  - https://www.reddit.com/r/StableDiffusion/comments/1q5k6al/fix_to_make_ltxv2_work_with_24gb_or_less_of_vram/
  - *From: Underdog*

- **GGUF workflow example** (workflow)
  - https://www.reddit.com/r/StableDiffusion/comments/1q8gffc/using_gguf_models_for_ltx2_in_t2v/
  - *From: buggz*

- **Reddit OOM fix for 24GB VRAM** (guide)
  - https://www.reddit.com/r/StableDiffusion/comments/1q5k6al/fix_to_make_ltxv2_work_with_24gb_or_less_of_vram/
  - *From: noodlz*

- **GGUF models from QuantStack** (model)
  - https://huggingface.co/QuantStack/LTX-2-GGUF/tree/main/LTX-2-dev
  - *From: zelgo_*

- **Kijai LTXV2 ComfyUI models** (model)
  - https://huggingface.co/Kijai/LTXV2_comfy/tree/main
  - *From: various*

- **Audio separation tools** (tool)
  - https://github.com/jeankassio/ComfyUI_MusicTools
  - *From: 267974636690472960*

- **Bartowski Gemma GGUF** (model)
  - https://huggingface.co/bartowski/google_gemma-3-12b-it-GGUF
  - *From: cocktailprawn1212*

- **Kijai's LTXV2 models** (model)
  - https://huggingface.co/Kijai/LTXV2_comfy/tree/main
  - *From: Elvaxorn*

- **VACE-LTX-Video-0.9** (model)
  - https://huggingface.co/ali-vilab/VACE-LTX-Video-0.9
  - *From: NebSH*

- **LTX-2 video extend workflow** (workflow)
  - https://github.com/Rolandjg/LTX-2-video-extend-ComfyUI/blob/main/ltx-video-and-audio-extend.json
  - *From: Miku*

- **Earth Zoom Out LoRA** (lora)
  - https://discord.com/channels/1076117621407223829/1459859512025546792
  - *From: 627140525916422145*

- **SageAttention 2 precompiled for cu130 torch 2.9.0** (tool)
  - https://github.com/woct0rdho/SageAttention/releases/download/v2.2.0-windows.post3/sageattention-2.2.0+cu130torch2.9.0.post3-cp39-abi3-win_amd64.whl
  - *From: Tachyon*

- **ComfyUI cache management PR** (repo)
  - https://github.com/Comfy-Org/ComfyUI/pull/10779
  - *From: Kijai*

- **Join Audio Channels commit** (repo)
  - https://github.com/Comfy-Org/ComfyUI/commit/027042db6811c875562296f0a6b797c89d59e426
  - *From: Kijai*

- **Kijai's LoRA versions** (model)
  - https://huggingface.co/Kijai/LTXV2_comfy/tree/main/loras
  - *From: The Shadow (NYC)*

- **LTX2 LoRAs by NebSH** (lora)
  - https://huggingface.co/Nebsh/RollTransition https://huggingface.co/Nebsh/POVObject/ https://huggingface.co/Nebsh/LTX2_Pushtoglass https://huggingface.co/Nebsh/LTX2_Herocam_Lora/tree/main https://huggingface.co/Nebsh/LTX2_Animatediff_style/
  - *From: NebSH*

- **VRAM fix Reddit post** (guide)
  - https://www.reddit.com/r/StableDiffusion/comments/1qa1or3/ltx2_1080p_lipsync_if_you_liked_the_previous_one/
  - *From: Elvaxorn*

- **Vantage GGUF loader** (node)
  - https://github.com/vantagewithai/Vantage-GGUF
  - *From: David Snow*

- **Dev embedding connector** (model)
  - https://huggingface.co/Kijai/LTXV2_comfy/blob/main/text_encoders/ltx-2-19b-embeddings_connector_dev_bf16.safetensors
  - *From: Kijai*

- **LTX2 Rapid Merges** (model)
  - https://huggingface.co/Phr00t/LTX2-Rapid-Merges
  - *From: Phr00t*

- **Memory optimized ComfyUI branch** (repo)
  - https://github.com/kijai/ComfyUI/tree/ltx2_memory
  - *From: Kijai*

- **Heretic Gemma FP8 text encoder** (model)
  - https://huggingface.co/DreamFast/gemma-3-12b-it-heretic/blob/main/comfyui/gemma_3_12B_it_heretic_fp8_e4m3fn.safetensors
  - *From: Choowkee*

- **AudioSR for audio enhancement** (tool)
  - https://audioldm.github.io/audiosr/
  - *From: David Snow*

- **ComfyUI AudioSR nodes** (nodes)
  - https://github.com/Saganaki22/ComfyUI-AudioSR
  - *From: David Snow*

- **Unsloth LTX-2 GGUF models** (model)
  - https://huggingface.co/unsloth/LTX-2-GGUF/tree/main
  - *From: 568465354158768129*

- **QuantStack LTX-2 GGUF models** (model)
  - https://huggingface.co/QuantStack/LTX-2-GGUF/tree/main/LTX-2-dev
  - *From: 568465354158768129*

- **LTX-2 Distilled LoRA** (model)
  - https://huggingface.co/Lightricks/LTX-2/blob/main/ltx-2-19b-distilled-lora-384.safetensors
  - *From: 568465354158768129*

- **Kijai's Audio VAE** (model)
  - https://huggingface.co/Kijai/LTXV2_comfy/blob/main/VAE/LTX2_audio_vae_bf16.safetensors
  - *From: 568465354158768129*

- **Official LTX example workflows** (workflow)
  - https://github.com/Lightricks/ComfyUI-LTXVideo/tree/master/example_workflows
  - *From: David Snow*

- **Vantage GGUF Nodes** (repo)
  - https://github.com/vantagewithai/Vantage-Nodes
  - *From: 568465354158768129*

- **Kijai's updated av_model.py** (repo)
  - https://github.com/kijai/ComfyUI/blob/ac4daffd80cecbc56ee0e31f2b521114fa0f8e08/comfy/ldm/lightricks/av_model.py
  - *From: 568465354158768129*

- **Lightricks workflows customized for GGUF** (workflow)
  - *From: 568465354158768129*

- **Gemma 3 FP8 scaled model** (model)
  - https://huggingface.co/Comfy-Org/ltx-2/blob/main/split_files/text_encoders/gemma_3_12B_it_fp8_scaled.safetensors
  - *From: Xor*

- **LTXV2 ComfyUI models** (model)
  - https://huggingface.co/Kijai/LTXV2_comfy
  - *From: Xor*

- **ComfyUI-GGUF (City96)** (repo)
  - https://github.com/city96/ComfyUI-GGUF
  - *From: 568465354158768129*

- **ComfyUI-GGUF (CRCODE22 fork)** (repo)
  - https://github.com/CRCODE22/ComfyUI-GGUF
  - *From: 568465354158768129*

- **LTX2-Infinity workflow** (workflow)
  - https://github.com/Z-L-D/LTX2-Infinity
  - *From: ZombieMatrix*

- **Unsloth Gemma 3 GGUF** (model)
  - https://huggingface.co/unsloth/gemma-3-12b-it-GGUF
  - *From: *Dan*

- **Gemma tokenizer.model** (model)
  - https://huggingface.co/google/gemma-3-12b-it/resolve/main/tokenizer.model
  - *From: *Dan*

- **Kijai's memory-optimized av_model.py** (code)
  - https://github.com/kijai/ComfyUI/blob/ltx2_memory/comfy/ldm/lightricks/av_model.py
  - *From: Kijai*

- **Gemma 3 12B IT GGUF** (model)
  - https://huggingface.co/unsloth/gemma-3-12b-it-GGUF/tree/main
  - *From: cocktailprawn1212*

- **ComfyUI-GGUF commit for LTX2** (repo)
  - https://github.com/city96/ComfyUI-GGUF/commit/58625e1cb63a8b8dd1bf4e0221de032b5135d0d2
  - *From: Kijai*

- **Volume control browser extension** (tool)
  - mentioned but not linked
  - *From: David Snow*

- **LTX2 lip sync workflow** (workflow)
  - https://www.reddit.com/r/StableDiffusion/comments/1qa1or3/ltx2_1080p_lipsync_if_you_liked_the_previous_one/
  - *From: dg1860*

- **Kijai Dynamic Lora bf16 r175** (lora)
  - https://huggingface.co/Kijai/LTXV2_comfy/tree/main/loras
  - *From: The Shadow (NYC)*

- **Mixed precision text encoder** (model)
  - https://huggingface.co/Comfy-Org/ltx-2/tree/main/split_files/text_encoders
  - *From: TK_999*

- **Latent2rgb PR** (repo)
  - https://github.com/Comfy-Org/ComfyUI/pull/11741
  - *From: Kijai*

- **LTX-2 IC-LoRA-Detailer** (lora)
  - https://huggingface.co/Lightricks/LTX-2-19b-IC-LoRA-Detailer/tree/main
  - *From: The Shadow (NYC)*


## Known Limitations

- **Model cannot do violence**
  - LTX-2 seems unable to generate violent content, ignores prompts asking for violence like stabbing
  - *From: Kiwv*

- **Audio quality is poor**
  - Audio sounds like 64kbps mp3 from p2p sharing era, needs post-processing with audio-to-audio models
  - *From: Mandark*

- **High VRAM usage for native high resolution**
  - Native 1080p uses 4x more VRAM than upscaled approach, causes OOM issues
  - *From: Kiwv*

- **Gemma model censorship**
  - Q4 version outputs 'this prompt contains unsafe content' for boxing prompts, returning original prompt
  - *From: leodev*

- **Model degrades after 20 seconds**
  - Quality falls apart over 20s, coherence issues in longer videos
  - *From: Tachyon*

- **Violence prompts don't work well**
  - Model doesn't seem to have knowledge of violence, failed on violent prompts
  - *From: Kiwv*

- **No VACE equivalent**
  - Unlike WAN, LTX2 doesn't have VACE functionality and never will
  - *From: Grimm1111*

- **Distilled model with distill setup**
  - Makes LTX turn into dumb first version - generates anything but what's in prompt
  - *From: N0NSens*

- **Cannot reliably prevent subtitles in output**
  - No reliable way to stop model from putting subtitles on screen
  - *From: Q-*

- **Compressed latent space causes quality loss**
  - LTX is fast because of very compressed latent space, but this causes garbled faces and details in wide shots
  - *From: 976496720370348032*

- **Portrait videos more prone to artifacts**
  - Portrait can break more easily than landscape with high token count or long duration
  - *From: 976496720370348032*

- **Character identity loss over time**
  - Model loses character identity as video progresses, especially with higher I2V strength
  - *From: Kijai, Nokai*

- **No support for pure audio-only continuation**
  - Cannot continue from audio only - need to mask both audio and video segments
  - *From: 976496720370348032*

- **Model struggles with animated character identity**
  - LTX tends toward realism and may not identify animated characters well, often results in frozen animation
  - *From: Juan Gea*

- **Distilled models lose more character identity**
  - While faster, distilled versions sacrifice identity preservation compared to full models
  - *From: Kijai*

- **Some images refuse to animate**
  - Certain images only generate slide shows instead of proper animation, even with prompt enhancer
  - *From: Zueuk*

- **NVFP4 doesn't work with control LoRAs**
  - FP4 quantization is incompatible with control LoRA functionality
  - *From: cyncratic*

- **Memory management issues with custom node workflows**
  - LTX custom node workflows can cause OOM errors that don't occur with native workflows
  - *From: Juan Gea*

- **I2V has temporal compression issues**
  - Smudginess and glitchy artifacts in fast moving frames, though 48 FPS helps counteract this
  - *From: Ada*

- **Cannot generate audio-only without redundant video**
  - No audio-only derived model available yet, need to generate video and discard it
  - *From: 976496720370348032*

- **Static camera LoRA affects 2D anime style**
  - Turns 2D retro anime into 3D style
  - *From: Gleb Tretyak*

- **Quality degrades with high frame count at high resolution**
  - 960x960 at 1000 frames outputs garbage due to tensor size limits
  - *From: seitanism*

- **Struggles with non-standard character poses**
  - Completely overwhelmed with characters doing handstands or similar poses
  - *From: seitanism*

- **1024 token limit on text encoder**
  - ComfyUI reports prompt length exceeding limit
  - *From: PeroBueno*

- **I2V struggles with frozen/static results without control signals**
  - Especially with 2D/3D animation, often needs pose control to get movement
  - *From: Juan Gea*

- **Character likeness not fully preserved in I2V**
  - Characters tend to morph toward realistic look and lose original appearance
  - *From: Juan Gea*

- **WAN upscale destroys lip sync**
  - If you have videos with people talking, upscaling breaks synchronization
  - *From: seitanism*

- **Memory management issues cause model reloading**
  - Before decoding latents, ComfyUI empties VRAM causing models to reload repeatedly
  - *From: yi*

- **Preview quality is poor**
  - Resolution is tiny for LTX latent space so preview isn't great
  - *From: Kijai*

- **Model doesn't understand tabs or musical notation**
  - Never saw captions with tabs during training, would need LoRA training for musical chord notation
  - *From: 976496720370348032*

- **Upscaling destroys lip sync**
  - Even at low denoise strength (0.09), upscaling significantly degrades lip synchronization
  - *From: seitanism*

- **Non-linear memory usage**
  - Memory usage isn't linear and can spike unexpectedly during generation
  - *From: Kijai*

- **Full autoregressive audio+video is tricky**
  - Time granularities of audio and video latent spaces don't match, making full autoregressive generation challenging
  - *From: 976496720370348032*

- **fp4 quantization performance**
  - fp4 is twice as slow and quality is too low, even on Blackwell cards where it's supposed to be accelerated
  - *From: Shawneau 🍁 [CA]*

- **Long video generation quality degradation**
  - 200+ frame generations work but quality falls apart over very long sequences
  - *From: Shawneau 🍁 [CA]*

- **Custom audio integration**
  - Still can't get custom audio to work properly
  - *From: VRGameDevGirl84(RTX 5090)*

- **Focus issues with camera movement**
  - LTX loves moving cameras and focal shifts but subject is never in focus
  - *From: dj47*

- **Looping sampler cannot handle audio**
  - Audio functionality not available with looping sampler
  - *From: Chandler ✨ 🎈*

- **Advanced noise node incompatibility**
  - Advanced noise node from res4lyf doesn't work with LTX
  - *From: l҈u҈c҈i҈f҈e҈r҈*

- **FP4 quantization quality degradation**
  - FP4 quants will degrade video quality even with Blackwell series
  - *From: yi*

- **Audio quality issues**
  - Audio has robotic noise, needs improvement for next LTX version
  - *From: Lodis*

- **Fast changing scenes problems**
  - Model doesn't like to switch scenes, works better with continuous shots
  - *From: VK (5080 128gb)*

- **Model size estimation issues**
  - ComfyUI thinks model is 35GB during inference, memory estimation for offloading not quite accurate
  - *From: yi*

- **Blurry output at same resolution**
  - LTX2 outputs less sharp videos than WAN at same resolution, need 1080p to match WAN 720p quality
  - *From: seitanism*

- **Tiled VAE artifacts**
  - Visible square artifacts when using tiled VAE, especially at high resolutions like 2K
  - *From: David Snow*

- **Distilled model face blur**
  - Distilled model produces blurry/out-of-focus faces, not just motion blur
  - *From: Juan Gea*

- **Perfect images cause no motion**
  - Too perfect input images with no blur result in motionless video output
  - *From: 1100803024298975263*

- **LoRAs degrade audio quality**
  - LoRAs can considerably degrade audio depending on training method
  - *From: ZeusZeus (RTX 4090)*

- **Q4 quality is poor**
  - Q4 quantization produces poor quality, not recommended unless absolutely necessary
  - *From: Kijai*

- **--cache-none breaks advanced workflows**
  - Using --cache-none for memory makes video extension and advanced workflows impossible
  - *From: Zueuk*

- **Model doesn't follow complex prompts well**
  - Neither dev nor distilled models follow detailed prompts for complex actions like character switching positions
  - *From: N0NSens*

- **Negative prompts don't work with distilled model**
  - CFG 1 prevents negative prompt functionality
  - *From: KingGore2023*

- **Lower quantization reduces speed**
  - Lower the quant, slower it becomes
  - *From: Kijai*

- **VAE produces ghosting artifacts**
  - Encoding and decoding video produces ghosting artifacts that affect v2v pipelines
  - *From: 企鵝（50% CASH 50%GOLD）*

- **NAG doesn't go through MLPs**
  - Major limitation as MLPs are a significant part of the model architecture
  - *From: mallardgazellegoosewildcat2*

- **Audio prompt doesn't seem to do much**
  - Based on limited testing, audio prompting may have minimal effect
  - *From: Kijai*

- **Torch compile doesn't work well with offloading**
  - Too many graph breaks, device copies and recompiles make it very slow (30s/it to 200s/it)
  - *From: Kijai*

- **Characters sometimes don't talk in I2V**
  - Audio is present but no mouth movement, different seed can solve it
  - *From: PeroBueno*

- **Low resolution generations are blurry**
  - 720p results in blurred output, need higher resolution but causes OOM issues
  - *From: N0NSens*

- **Portrait/vertical video has motion issues**
  - Jittery motion in vertical videos, likely due to limited portrait video training data from platforms like TikTok, Instagram, Snapchat that don't release data
  - *From: mallardgazellegoosewildcat2*

- **Audio quality issues with dev model**
  - High pitched drone present in dev model audio that isn't in distill model
  - *From: David Snow*

- **Plastic skin appearance with distill model**
  - Humans rendered with distill model have shiny plastic skin texture
  - *From: David Snow*

- **Low quality output without distill LoRA on dev model**
  - Dev model at 40 steps CFG 4 produces much worse quality than with distill LoRA, feels like needs extra 40 steps
  - *From: Wildminder*

- **Video extension uses significantly more VRAM**
  - VRAM usage at least double compared to basic txt2video or img2video, 24GB sufficient for 10s ~1080p txt2video but 480p barely works for extension
  - *From: 74637656272666624*

- **Poor text/logo generation**
  - Model struggles with text generation, example showed 'Retro Synthwave' rendered as unreadable text
  - *From: David Snow*

- **Character consistency issues**
  - Model changes character face after 3 seconds, requires tedious manual correction
  - *From: KingGore2023*

- **Poor prompt following compared to alternatives**
  - Model doesn't listen to prompting well, generates what it wants rather than following prompts closely
  - *From: Grimm1111*

- **2D animation quality**
  - Model is great at realism and 3D animation but bad at 2D - noticeably worse than Wan or Kandinsky for 2D
  - *From: Ada*

- **Enhance-a-Video compatibility**
  - Not working properly with LTX2, changes output too much and doesn't seem to burn like other models
  - *From: Kijai*

- **Ethnic bias in outputs**
  - Model tends to skew characters towards being African American or Indian, even when not prompted
  - *From: David Snow*

- **VAE compression issues**
  - VAE has more compression and is somewhat bugged - door frames warp and motion becomes transparent, not good for v2v
  - *From: 企鵝（50% CASH 50%GOLD）*

- **Rank reduction limits**
  - Even rank32/64 loses too much quality - to keep 90% fro the average rank is still 175
  - *From: Kijai*

- **Keyframe adherence not perfect**
  - Due to reference latent technique, adherence to keyframes can sometimes be relatively low
  - *From: 976496720370348032*

- **Model resists drawn/stylized content**
  - Tries to render photoreal instead of maintaining artistic styles
  - *From: N0NSens*

- **Challenging interpolation with certain styles**
  - Some artistic styles are difficult for the model to interpolate smoothly
  - *From: 976496720370348032*

- **Enhanced Prompt node incompatible with GGUF**
  - Node doesn't work with GGUF models, must be disabled
  - *From: Tachyon*

- **ComfyUI sampler modifications break LTX2**
  - Any sampler overrides break due to nested video + audio tensor structure
  - *From: Kijai*

- **Distilled model audio quality compromise**
  - Audio quality somewhat worse due to being optimized for fewer steps
  - *From: 976496720370348032*

- **Full model produces poor results for many users**
  - Many report distilled model works better than full model
  - *From: Gleb Tretyak*

- **Context windows don't work with audio**
  - Nested video/audio latents not supported in context windows currently
  - *From: Kijai*

- **Poor text rendering**
  - LTX struggles with text generation due to compressive VAEs
  - *From: hicho*

- **Model mistakes skin for clothing**
  - Known issue where model confuses skin and clothing
  - *From: Zabo*

- **Face consistency issues in I2V**
  - No luck with face consistency in image-to-video despite trying various settings
  - *From: tamilboy*

- **High resolution generation causes system freezing**
  - Even 720p generation can freeze the entire PC during processing
  - *From: Elvaxorn*

- **Color shifts at 2K upscaling**
  - Progressive upscaling works well up to 1024, but 2048 causes bad color shifting
  - *From: KingGore2023*

- **Audio I2V lip sync inconsistency**
  - Lip sync strength cannot be adjusted and doesn't work reliably for talking, works better for music
  - *From: AJO*

- **Model doesn't like some input images**
  - Certain images consistently fail to animate properly regardless of settings
  - *From: TK_999*

- **First-to-last frame guidance unreliable**
  - Too inconsistent in using guides, requires experimentation with every image/prompt pair
  - *From: Phr00t*

- **Prompt not masked in video extension**
  - The prompt applies to the whole video, not just the new part being generated
  - *From: Kijai*

- **Distill LoRA destroys audio quality**
  - Using distill LoRA with dev model results in poor audio quality during upscaling
  - *From: Wildminder*

- **Multiple person dialog issues**
  - Describing multiple people in same prompt usually makes main character carry out dialog of both
  - *From: 138332118890708992*

- **Subtitle data contamination**
  - Model has subtitle contamination, future versions will caption subtitles better for neg-prompting
  - *From: 976496720370348032*

- **Some images don't work with specific names**
  - Certain image/name combinations cause static results due to apparent content filtering
  - *From: Elvaxorn*

- **I2V extremely random, some seeds work others don't**
  - No matter how much noise added, some seeds simply won't animate properly
  - *From: Kijai*

- **Fast motion causes blurred/shredded anatomy**
  - During camera movement or subject motion, faces and limbs become blurry smudges even at 48fps
  - *From: foxydits*

- **Hard quality ceiling similar to LTX1**
  - Model is fast and versatile but has fundamental quality limitations
  - *From: Christian Sandor*

- **3090 with 64GB RAM limited to ~321 frames at 1920x1088**
  - Maximum resolution/length capacity even with all optimizations applied
  - *From: Underdog*

- **VRAM is hard cap even with full model offloading**
  - Cannot exceed VRAM limits even when offloading entire model to RAM
  - *From: Kijai*

- **Model inconsistency**
  - This model is pretty random with everything
  - *From: Kijai*

- **Audio quality issues**
  - Audio in general is a weakness with this model, produces sibilant/droning sounds
  - *From: David Snow*

- **I2V subject consistency**
  - I2V after 1-2 seconds will lose most of the original subject and change it to someone else (though others report good consistency)
  - *From: 568465354158768129*

- **4K generation issues**
  - LTX does not like 3840x2160 direct generation, took 53 minutes and had problems
  - *From: ZombieMatrix*

- **NSFW generation limited**
  - Underlying diffusion model wasn't trained on NSFW content, need LoRAs to achieve that
  - *From: Kiwv*

- **Complex prompts become dumpster fire**
  - Model struggles with very complex, multi-part prompts with many scene changes
  - *From: Tachyon*

- **Cannot handle cuts or complex interactions well**
  - Model doesn't follow complex prompt instructions that involve multiple scene transitions
  - *From: Ablejones*

- **Prompts only ~75% accurate**
  - Even official example prompts don't execute perfectly, model typically follows first 40% of complex prompts
  - *From: Ablejones*

- **Lower resolutions produce static motion**
  - Resolutions like 960x544 result in very static, low-quality movement
  - *From: 568465354158768129*

- **50fps requires more than 16GB VRAM**
  - Unless you want only 3 second videos
  - *From: 568465354158768129*

- **I2V is hit or miss depending on the image**
  - Sometimes doesn't animate at all, very dependent on input image quality
  - *From: Tachyon*

- **Hard to keep character consistency in stage 2**
  - Character consistency is difficult to maintain during the upscaling stage
  - *From: KingGore2023*

- **Wan2.2 has obvious limitations**
  - Limited to 81 frames, 16fps constraints
  - *From: KingGore2023*

- **LTX2 is relatively weak in stage 1**
  - First stage generation is not as strong as other models
  - *From: KingGore2023*

- **Fast camera movements cause major problems**
  - Model struggles with rapid camera motion, though higher FPS helps reduce artifacts
  - *From: 1099257978277867542*

- **Multiple person scenes degrade quickly**
  - Quality drops significantly when adding more people, works best with single person scenes
  - *From: Hevi*

- **Character consistency in second pass**
  - Upscaling pass often changes character appearance and introduces unrealistic skin textures
  - *From: ラD.*

- **Vertical video quality issues**
  - Crazy artifacts when doing 1080p or higher vertical video generation
  - *From: ucren*

- **T2I performance**
  - LTX2 as text-to-image is very bad, not optimized for still image generation
  - *From: protector131090*

- **Cannot handle complex actions**
  - Model refuses to generate woman kicking car to slide it across street, can't do pants pulling down actions
  - *From: nikolatesla20*

- **Poor understanding of audio noise sources**
  - Anything with noise sounds like sampling window isn't long enough and just repeats
  - *From: 381513363517341698*

- **8-frame boundary thinking**
  - Hard to describe short transient actions like 1-frame flash due to model thinking in 8-frame boundaries
  - *From: 138332118890708992*

- **Frame count limits**
  - Cannot generate more than 281 frames due to VAE limitations and 32-bit index math constraints
  - *From: NebSH*

- **Audio/video latent synchronization**
  - Cannot cut video and audio latents along same timeline due to different time granularities
  - *From: 976496720370348032*


## Hardware Requirements

- **VRAM for different approaches**
  - Can work with 4GB VRAM minimum using system RAM offloading. Native high-res needs much more VRAM than upscaled approach
  - *From: Moonbow*

- **System RAM importance**
  - System RAM more important than VRAM for offloading. Works on 2060 with proper settings
  - *From: hicho*

- **NVFP4 requirements**
  - Needs Blackwell GPU (RTX 5090) and Torch 13 for NVFP4 model format
  - *From: Kiwv*

- **Performance benchmark**
  - 40 iterations took 08:58 (13.46s per iteration) for 1201 steps
  - *From: Benjimon*

- **RTX 5090 performance**
  - Can handle 720p 20 second videos without VRAM offload, but system RAM maxes during VAE decode
  - *From: Tachyon*

- **16GB VRAM + 32GB RAM**
  - Can work with FP8 model and reserve VRAM settings, struggles without optimizations
  - *From: JUSTSWEATERS*

- **Long video generation**
  - 5000+ frames requires significant time, 1080 frames took 200s to generate
  - *From: ZombieMatrix*

- **System RAM usage**
  - 64GB RAM can max out during tiled decode for 1920x960, 242 frames
  - *From: Tachyon*

- **4090 with 64GB RAM needs swapfile**
  - OOMs during upscaler stage, system RAM spikes to 60GB+, 32GB swapfile fixes it
  - *From: taoofai*

- **24GB VRAM needs reserve-vram setting**
  - Use --reserve-vram 4 for 4090, can drop to 2-3GB for lower res/length
  - *From: Gill Bastar*

- **Modified 4090 with 48GB best value**
  - 4090 mod is best deal for 48GB, D variant available for ~3k and only 10% slower but super loud
  - *From: Benjimon*

- **VRAM usage difference between T2V and I2V**
  - I2V uses more VRAM than T2V due to conditioning image encoding, affects maximum frame counts
  - *From: protector131090*

- **Performance timing for 1080p I2V**
  - 1080p 121 frames I2V on RTX 4090 takes 1939 seconds, 720p takes 180 seconds
  - *From: protector131090*

- **T2V performance on RTX 4090**
  - 15 second T2V video takes 190 seconds to generate on RTX 4090
  - *From: GalaxyTimeMachine*

- **CUDA version for NVFP4**
  - NVFP4 requires CUDA 13, users on CUDA 12.9 see no performance difference
  - *From: protector131090*

- **FP8 compatibility**
  - FP8 works on RTX 4000 series, NVFP4 requires RTX 5000 series and up
  - *From: Scruffy*

- **Memory requirements for full model**
  - Full bf16 model requires significant VRAM, may need RAM offload on cards below RTX 6000 Pro
  - *From: 421114995925843968*

- **VRAM management for RTX 4090**
  - 24GB VRAM + 128GB RAM needs --reserve-vram 4-6 to prevent OOM. Higher values (10+) cause 10x slowdown
  - *From: Juan Gea*

- **RTX 3090 optimization**
  - 24GB VRAM + 64GB RAM, recommended startup: --lowvram --cache-none --reserve-vram 4
  - *From: 1100803024298975263*

- **Performance comparison**
  - 720p 21 frames i2v takes 5 seconds on fp8 non-distilled. 3 minutes for full generation
  - *From: GalaxyTimeMachine (RTX4090)*

- **Upscale performance hit**
  - Upscale pass 5x slower than lowres generation (1min gen -> 5min upsc) on lower-end hardware
  - *From: N0NSens*

- **PyTorch CUDA requirement**
  - Need pytorch with cu130 or higher for optimized CUDA operations
  - *From: NebSH*

- **RTX 4090 VRAM usage**
  - Needs --reserve-vram 4+ minimum, up to 10+ with controlnet. Uses 96-98% VRAM regularly
  - *From: 391020191338987522, Juan Gea*

- **RTX 3090 recommended settings**
  - --reserve-vram 11-12, works but less VRAM than newer cards
  - *From: Juan Gea, Q!*

- **Page file requirements**
  - 60-100GB system page file needed to prevent random crashes
  - *From: Owlie*

- **Speed comparison after memory fix**
  - 16.47s/it on first sampler, flash attention gives ~15 second improvement (3m24 to 3m09)
  - *From: Juan Gea, 1100803024298975263*

- **VRAM for 1920x1088x193 frames**
  - Requires reserve-vram 6-7 GB on Linux, more with CFG enabled
  - *From: Kijai*

- **5090 performance**
  - 1920x1088 193 frames (8 seconds) takes 97s total, 60s inference time with 8+3 steps
  - *From: toxicvenom117*

- **Reserve VRAM scaling**
  - Higher reserved VRAM leads to longer inference times due to unnecessary offloading
  - *From: Kijai*

- **RAM usage with full model**
  - 128GB RAM works fine with full model, 64GB may cause crashes
  - *From: David Snow*

- **VRAM reserve settings**
  - RTX 5090: reserve VRAM 9 optimal for 8-second I2V. Users with 12GB+64GB RAM need reserve VRAM 2-4. 128GB RAM users still need reserve VRAM 4-5
  - *From: multiple users*

- **RAM usage and paging**
  - Model uses 50-60GB pagefile even with 64GB RAM and only 35GB RAM usage. Major disk writing issue affecting SSD health
  - *From: Fred*

- **Performance benchmarks**
  - 5090: 1920x1088p 8-second I2V takes varying times based on reserve VRAM settings. 1280x704 takes 40sec, 2K upscale total 100sec
  - *From: toxicvenom117*

- **Training hardware needs**
  - RTX Pro 6000 sufficient for training with batch size 4, would take about a week straight. H100s more expensive with no speed benefit for this use case
  - *From: Kiwv*

- **RAM for high resolution**
  - Need around 64GB pagefile if under 100GB RAM, 128GB RAM recommended
  - *From: Lodis*

- **VRAM for VAE**
  - 15GB VRAM for encoding 121 frames at 1024x1024
  - *From: Kijai*

- **Memory management**
  - RAM usage reports wildly varying, 64GB Windows has issues, 64GB Linux works better
  - *From: Kijai*

- **GGUF for quantization**
  - GGUF will be better for quants, especially gemma quant will save massive RAM
  - *From: yi*

- **32GB RAM with --cache-none**
  - Can run LTX2 on 32GB RAM using --cache-none but breaks advanced workflows
  - *From: Zueuk*

- **24GB VRAM struggles**
  - 24GB VRAM has issues, needs gemma 4-bit on CPU and careful memory management
  - *From: Zueuk*

- **GGUF slower on 40xx series**
  - GGUF doesn't have fp8 speedups for 40 series cards, but good for 30 series
  - *From: FUNZO*

- **128GB RAM for full model**
  - Probably need 96GB+ for larger models, user uses 128GB
  - *From: David Snow*

- **Q8 GGUF is 20.4GB**
  - Q8 distilled model size is 20.4GB
  - *From: Tachyon*

- **2060 6GB with 64GB RAM works**
  - Generated 121 frames at 384x672 in 380 seconds using gemma bnb
  - *From: hicho*

- **RTX 4090 4K generation**
  - Can generate 4K video with --reserve-vram 6GB and 128GB RAM
  - *From: Kijai*

- **RTX 5090 high resolution**
  - Used around 70GB VRAM for 4K generation, 10 minutes per 5s video
  - *From: D'Squarius Green, Jr.*

- **RTX 3090 high resolution**
  - Successfully generated 2560x1408 resolution
  - *From: NC17z*

- **Q6 quantization memory usage**
  - Still causes OOM issues even on high-end systems
  - *From: boop*

- **VRAM for 1080p 10 seconds**
  - 24GB VRAM/32GB system RAM can handle 1080p 10 second generation in 455 seconds
  - *From: boop*

- **VRAM for 2560x1408**
  - RTX 3090 can handle 2560x1408 resolution
  - *From: NC17z*

- **Performance difference**
  - FP8 should be 30-40% faster than Q8 GGUF on ada+ GPUs
  - *From: mallardgazellegoosewildcat2*

- **VRAM usage for different configurations**
  - 4090 can handle distill model workflows but dev + distill LoRA OOMs on second upscale pass. FP4 can load on RTX 2060.
  - *From: theUnlikely*

- **Generation speed benchmarks**
  - 4090: 90 seconds for 10s 720p video. RTX 3090: 15 minutes for 1080p 10 seconds (was actually 20 seconds). 720p renders in 2 minutes on unspecified GPU.
  - *From: BobbyD4AI*

- **Distill LoRA memory usage**
  - Distill LoRA is 7GB, very heavy for a LoRA and uses significant RAM
  - *From: Kijai*

- **VRAM and RAM for longer videos**
  - Need sufficient VRAM + RAM for longer than 4 second videos, works 'for the most part' if you have enough
  - *From: Moonbow*

- **fp4 model requirements**
  - Need 50xx series GPU, new driver, and torch+cu130 for fp4 quantization
  - *From: TK_999*

- **RTX 3090 limitations**
  - RTX 3090/64GB RAM struggles with 1080p 20 second upscale, requires VRAM offloading
  - *From: dj47*

- **4060 Ti performance**
  - I2V 1280x704 361 dev gguf takes 10:15min on 3060 12GB
  - *From: Daflon*

- **VRAM for rank reduction**
  - SVD requests 136GB VRAM for large weights, script needs adjustment to skip problematic weights
  - *From: Kijai*

- **VAE tiled decoding VRAM**
  - Takes max 4GB for decoding 5s 720p videos, but ComfyUI removes whole model instead of offloading blocks
  - *From: yi*

- **4090 limitations**
  - Hard to experiment with only 4090 - user wishes for more powerful GPU
  - *From: happy.j*

- **Memory optimization**
  - Can lower peak VRAM usage by 1GB at larger inputs by chunking ffn
  - *From: Kijai*

- **4090 + 64GB RAM setup**
  - Can run fp8 text encoder and choose between distilled or full model
  - *From: berserk4501*

- **3090 + 64GB RAM with modifications**
  - Can run full fp16 model with cache clearing and page file usage (10-15GB)
  - *From: Underdog*

- **M4 Mac Mini with 64GB**
  - GGUF provides 2x+ speed improvement, full dev takes ~28 minutes for 640x352x73
  - *From: buggz*

- **ComfyUI launch parameters for 24GB VRAM**
  - --cache-none --disable-auto-launch --fast fp16_accumulation --reserve-vram 4
  - *From: Underdog*

- **VRAM management**
  - 4090 can do up to 4K resolution for 121 frames with --reserve-vram and fp8
  - *From: Kijai*

- **Memory for GGUF**
  - GGUF Q4 LTX2 + Q4 Gemma still won't fit in 24GB VRAM together
  - *From: 138332118890708992*

- **Performance impact**
  - GGUF models always slower but use less VRAM - trade-off for memory usage
  - *From: Xor*

- **Sage attention benefit**
  - 5-10% speed improvement with sage attention for LTX2
  - *From: belair3*

- **Memory usage with large models**
  - User with 128GB RAM hits 80-85GB usage, 96GB RAM + 120GB swap still crashes after multiple generations
  - *From: ZombieMatrix*

- **24GB VRAM limitations**
  - Cannot handle 1080p 480 frames even with VRAM offloading due to activation memory limits
  - *From: Kijai*

- **5090 performance**
  - Even 5090 users experience OOMs and hiccups with high resolution generation
  - *From: Elvaxorn*

- **RTX 4060 TI 16GB compatibility**
  - Can run Q4 LTX-2 + fp8 Gemma3 but may hit VRAM limits and crash
  - *From: 568465354158768129*

- **I2V memory usage**
  - I2V uses significantly more VRAM than T2V - instantly 5GB+ higher when I2V node is added
  - *From: Kijai*

- **High resolution I2V**
  - 1280x1024@161 frames requires careful memory management, often causes OOM during upscale
  - *From: 138332118890708992*

- **5090 with reserve-vram 4**
  - Can OOM with 384 LoRA in I2V, need reserve-vram 7 for stable operation
  - *From: Tachyon*

- **System RAM for cache-none**
  - Using --cache-none helps with VRAM but requires sufficient system RAM to avoid constant model reloading
  - *From: Kijai*

- **I2V VRAM usage**
  - I2V uses gigabytes more VRAM than T2V due to per-token timestep handling inefficiency
  - *From: Kijai*

- **1024x1024x121 I2V**
  - Runs on 4090 without reserve-vram or tweaks after optimizations
  - *From: Kijai*

- **Q4 1080p 10sec I2V**
  - Possible on 3090 with Q4 quantization
  - *From: Hevi*

- **3090 limits**
  - Can handle up to 321 frames at 1920x1088 with distilled models and 64GB RAM
  - *From: Underdog*

- **VRAM for high resolution I2V**
  - Can now do 1920x1088x193 I2V with no reserve VRAM on 4090, saves ~5GB with optimization
  - *From: Kijai*

- **High resolution generation capabilities**
  - 1440x1440x361 possible on 16GB VRAM, 128GB RAM with optimizations
  - *From: Gleb Tretyak*

- **2560x1440 I2V requirements**
  - 2560x1440x241 I2V uses 60% VRAM on 4090 with 128GB RAM
  - *From: David Snow*

- **4K generation performance**
  - 3840x2160x49 frames takes 38+ minutes on single 3090
  - *From: ZombieMatrix*

- **Q4 GGUF on 16GB**
  - Q4 GGUF works well on 16GB VRAM, smaller than FP8 so should work with quantized text encoder
  - *From: Kiwv*

- **VRAM usage scales with resolution**
  - 1088x1920 @145 frames uses almost all 16GB VRAM, leaves little room for LoRAs
  - *From: 568465354158768129*

- **System memory important for offloading**
  - Uses 128GB system memory for offloading when VRAM is insufficient, paging file setup crucial
  - *From: 568465354158768129*

- **4GB VRAM likely insufficient**
  - Would require extensive offloading making generation extremely slow
  - *From: 568465354158768129*

- **1440x1440x481 works on 16GB VRAM**
  - Takes 26 minutes on 16GB VRAM + 128GB RAM setup
  - *From: Gleb Tretyak*

- **VRAM for 50fps**
  - Requires more than 16GB VRAM for reasonable video lengths
  - *From: 568465354158768129*

- **RTX 3090 performance**
  - Takes about 5 minutes to generate 5 seconds of 720p with upscaling stage
  - *From: NC17z*

- **RTX 3080 12GB performance**
  - Can generate 5 seconds of 720p in under a minute with distilled model
  - *From: garbus*

- **RTX 3090 with GGUF**
  - GGUF model Q4 + gguf gemma Q4 can go up to 35 seconds with I2V 720p
  - *From: Hevi*

- **Generation speeds**
  - 121 frames at 1920x1088 in about 315 seconds, 1m49s video took 16m21s to generate
  - *From: particle9*

- **16GB RAM limitation**
  - 16GB RAM is tough for LTX2, may cause disconnections even with VAE tiling
  - *From: Kijai*

- **Q4 GGUF performance**
  - Model Q4 GGUF + Gemma Q4 GGUF = ~35 seconds for 720p on RTX 3090
  - *From: Hevi*

- **4090 laptop capability**
  - RTX 4090 laptop with 16GB VRAM and 46GB RAM is capable for LTX2 generation
  - *From: 870722151316082689*

- **Memory usage with new optimization**
  - New av_model.py drops I2V VRAM usage to near T2V levels, tested faster on both RTX 5080 and PRO 6000
  - *From: BitPoet (Chris)*

- **VRAM reduction with chunking**
  - Chunking can reduce VRAM by up to 5GB at 1080p, 2GB at 1216x1216 with 121 frames
  - *From: Kijai*

- **RTX 4060 TI 16GB performance**
  - Can handle 1920x1088 @ 25 FPS, 201 frames with 6GB VRAM unused using sage attention
  - *From: 568465354158768129*

- **RTX 3060 12GB limitations**
  - OOM on tiled decode with 481 frames at 1024x544, needed to switch to spatial decode
  - *From: Daflon*

- **Speed improvements**
  - 8 steps in 14 seconds (1.81s/step) for I2V 281 frames 1280x720 with KJ py + torch/cu upgrade
  - *From: NebSH*


## Community Creations

- **Custom LTX fork with GUI** (tool)
  - Fork of LTX with graphical interface for running outside ComfyUI
  - *From: Benjimon*

- **Low VRAM workflow** (workflow)
  - Optimized workflow for very low VRAM usage with model recommendations
  - *From: avataraim*

- **Abliterated Gemma model** (model)
  - BF16 version created, FP8 version planned for upload
  - *From: Kiwv*

- **VRAM Debug workflow optimization** (workflow)
  - Method using VRAM debug nodes to maintain consistent generation speeds
  - *From: Phr00t*

- **Audio channel conversion code snippet** (utility)
  - Custom node code for converting mono to stereo audio
  - *From: 976496720370348032*

- **Transformer-only model extraction script** (tool)
  - Removes VAEs and connector from checkpoint, saves ~5GB per model
  - *From: Kijai*

- **Join channels node** (node)
  - ComfyUI PR for joining audio channels to complement split channels node
  - *From: Kijai*

- **LTXVSetAudioVideoMaskByTime node** (node)
  - Custom node for defining audio/video masks for continuation and editing workflows
  - *From: 976496720370348032*

- **V2V detailer workflow** (workflow)
  - Video-to-video detailing workflow from LTX nodes for upscaling and enhancement
  - *From: David Snow*

- **FP8 quantized Gemma3 text encoder** (model)
  - Community member quantized Gemma3 to FP8 at ~11GB, smaller than existing versions
  - *From: cyncratic*

- **Split workflow for slower hardware** (workflow)
  - Separates lowres generation and upscaling to save time on slower systems
  - *From: N0NSens*

- **LTXVLoopingSampler** (node)
  - Allows spatial tiling on video latents with overlap blending
  - *From: 976496720370348032*

- **LTX2 prompt enhancer fix** (tool)
  - Uses llama.cpp server with prefill support to bypass censorship issues
  - *From: Ada*

- **LTXVAudioVideoMask node** (node)
  - Node for masking audio and video portions during generation
  - *From: Kijai*

- **LTXVAddLatents node** (node)
  - Node to add empty latents of same spatial dimension for extending videos
  - *From: 976496720370348032*

- **Video padding automation** (node enhancement)
  - Added automatic padding option to extend input videos when end time exceeds input length
  - *From: Kijai*

- **Distilled fp8 + 2K upscale workflow** (workflow)
  - Complete workflow for generating with distilled fp8 model and upscaling to 2K resolution
  - *From: avataraim*

- **30k video training dataset** (dataset)
  - Dataset of ~30k videos prepared for LTX 2 uncensoring, includes realism, 3D, anime content
  - *From: Kiwv*

- **LTX-2 LoRA training** (lora)
  - Successfully trained person LoRA using video interview dataset on fal
  - *From: NebSH*

- **Sigma visualization nodes** (node)
  - Visualize nodes for sigmas in Res4lyf and KJNodes
  - *From: Kijai*

- **Dynamic rank reduced distill lora** (lora)
  - Reduced size version of distill lora from rank 384 to ~242 while retaining 95% fro value
  - *From: Kijai*

- **Video extend workflow** (workflow)
  - Workflow for extending video length using padding
  - *From: Kijai*

- **I2V looping workflow** (workflow)
  - Image to video workflow with looping capability
  - *From: Gleb Tretyak*

- **First community LoRA** (lora)
  - Community member's first LoRA creation for LTX2
  - *From: 627140525916422145*

- **Kijai's distilled LoRA** (lora)
  - Community-created distilled LoRA as alternative to original
  - *From: David Snow*

- **fp16 to bf16 conversion node** (node)
  - Fixed node to handle dtype conversion issues
  - *From: KingGore2023*

- **Modified multi-keyframe workflow** (workflow)
  - Modified version of KJ's original test workflow for multi-keyframe generation
  - *From: The Shadow (NYC)*

- **GGUF workflow with switches** (workflow)
  - Workflow that switches between different GGUF models
  - *From: buggz*

- **Low VRAM adjusted workflow** (workflow)
  - Workflow adjusted to run on 16GB VRAM systems
  - *From: 611243496753594371*

- **KJNodes memory monitoring** (tool)
  - Nodes for recording and visualizing VRAM usage with HTML reports, requires --disable-cuda-malloc flag
  - *From: Kijai*

- **Earth Zoom Out LoRA** (lora)
  - LoRA for creating earth zoom out effects, trained and shared by community member
  - *From: 627140525916422145*

- **Video extension workflow** (workflow)
  - Complete workflow for extending videos with audio using masking techniques
  - *From: Elvaxorn*

- **Fast Film Grain node** (node)
  - Adds film grain to images to improve I2V motion generation
  - *From: VRGameDevGirl84(RTX 5090)*

- **Detail Daemon** (node)
  - Provides free quality improvement, particularly useful for image models
  - *From: David Snow*

- **LTXVSetAudioVideoMaskByTime** (node)
  - Node for masking audio and video by time ranges, available in KJ nodes
  - *From: Elvaxorn*

- **Multiple LTX2 LoRAs** (lora)
  - RollTransition, POVObject, PushToGlass, HeroCam, AnimateDiff style LoRAs
  - *From: NebSH*

- **LTX2 Rapid Merges** (model)
  - Model merges including less distilled + detail versions
  - *From: Phr00t*

- **Beavis and Butthead LoRA** (lora)
  - LoRA training at step 8000, should reach 20000 steps, audio sounds pretty good and can associate correct voices by name
  - *From: 627140525916422145*

- **LTX2-Infinity workflow** (workflow)
  - Infinite length video workflow for creating extended video sequences
  - *From: ZombieMatrix*

- **Hero Shot LoRA** (lora)
  - LoRA for cinematic hero shot style generations
  - *From: NebSH*

- **LTX2 memory optimization code** (code)
  - Modified av_model.py that reduces I2V VRAM usage while maintaining identical output
  - *From: Kijai*

- **Infinite length workflow for LTX2** (workflow)
  - Work-in-progress workflow for generating very long videos with anchor image method
  - *From: ZombieMatrix*

- **Sage attention patch node** (node)
  - Patches forward function in FeedForward class as model patch, active only when node is active
  - *From: Kijai*

- **VRAM chunking node** (node)
  - Reduces VRAM usage up to 1GB at higher resolutions but may change output with fp8 fast
  - *From: Kijai*


---

# LTX Chatter - January 16-23, 2026

# Ltx Chatter Knowledge Base
*Extracted from Discord discussions: 2026-01-16 to 2026-01-24*


## Technical Discoveries

- **LTXVNormalizingSampler improves audio quality in distilled model**
  - New node specifically designed to fix audio issues with the distilled LTX2 model, should only be used for first pass 8-step generation
  - *From: harelcain*

- **Loading camera LoRA fixes static image/lip sync issues**
  - Applying LTX-2-19b-LoRA-Camera-Control-Static LoRA enables lip sync when using external audio
  - *From: nikolatesla20*

- **Audio latents use fixed 25 latents per second**
  - Audio latents are essentially fixed at 25 per second regardless of video frame rate, must be calculated accordingly
  - *From: Scruffy*

- **Preview override node conflicts with LTXVNormalizingSampler**
  - Kijai's preview override node causes pixelation and output damage with normalizing sampler after first 3 steps
  - *From: Miku*

- **Image strength affects static image issue**
  - Lower image strength around 0.5 can help get movement when experiencing still image problems
  - *From: triquichoque*

- **Normalization sampler affects both audio and video quality**
  - LTX Video 2 is a joint model where audio and video affect each other. Normalizing audio latents impacts video generation as well
  - *From: Kijai*

- **LTX2 Audio Latent Normalizing Sampling can improve audio quality**
  - Provides clearer sound with no ghost echo, less tinny sound, and fewer vocoder artifacts for distilled model configurations
  - *From: nacho.money*

- **CFG can improve audio quality in distilled model**
  - Scheduled CFG (start 0, end 0.3) produces better sound quality than CFG 1 with distilled model
  - *From: N0NSens*

- **Image compression at 0 may not keep initial image**
  - Initial image blinks away and forces text-to-video behavior instead of image-to-video
  - *From: phazei*

- **Normalization node gives identical results to sampler**
  - The LTX2 Audio Latent Normalizing Sampling node produces identical results to the normalizing sampler
  - *From: Kijai*

- **Static camera LoRA fixes unwanted zoom**
  - Using static camera LoRA eliminates sudden zoom at the start of videos
  - *From: PsiClone*

- **Japanese phonetic spelling for TTS**
  - Using キジャイ (ki-jai) works for text-to-speech pronunciation of 'Kijai'
  - *From: GalaxyTimeMachine*

- **NAG node combines negative prompt with positive conditioning for CFG 1**
  - When using CFG 1 (distilled model), NAG node basically combines the negative prompt with the positive conditioning to make negative prompts work
  - *From: DawnII*

- **Camera LoRA consistently enables movement in I2V**
  - Adding camera LoRA to image-to-video generations consistently produces movement, while without it generations often remain static with minimal camera movement
  - *From: Mazrael.Shib*

- **Structured prompts with scene descriptions improve movement**
  - Using timestamps and scene structure in prompts (e.g., 'scene 1: dragon breathes fire', 'transition: whip cut') helps the model follow movement instructions better
  - *From: ErosDiffusion*

- **LTX-2 can run on 4GB VRAM with Q4_K_M GGUF**
  - Generating 10s of 1280x720 24fps video on RTX 3050 with 4GB VRAM, takes about 15-20 minutes
  - *From: Xor*

- **LTX Video 2 TAE has been uploaded to GitHub**
  - Native ComfyUI support requested for the new TAE encoder
  - *From: yi*

- **NAG increases peak VRAM when chunked FFN is used**
  - VRAM usage goes as high as unchunked would when using NAG with chunked FFN
  - *From: Kijai*

- **LTX uses 2x more spatial compression than Wan**
  - This is the tradeoff of their fast training methods and faster inference
  - *From: Ablejones*

- **Context windows work with frame counts over 81 on Wan**
  - Can exceed 81 frames with good control inputs or light denoising, especially with context windows
  - *From: Ablejones*

- **Tiled VAE decode creates visible seams in dark backgrounds**
  - Seams appear as faint tick-tack-toe board pattern, more visible in high motion and dark scenes
  - *From: ucren*

- **Single frame inpainting works with LTX Video 2**
  - Always worked with single frame, contrary to some user experiences
  - *From: Kijai*

- **LTX Video 2 latent index is 8 (compared to Wan's 4)**
  - More tightly packed latent space, not due to audio addition
  - *From: Kijai*

- **Audio latents are treated as proper latents that need denoising**
  - Unlike other models where audio might just be conditioning, LTX requires simultaneous denoising of audio latents
  - *From: Kijai*

- **Guide vs inplace placement affects stability**
  - Guides are more like suggestions allowing room for working video, while inplace is exact keyframe replacement but more limiting
  - *From: Kijai*

- **Inplace keyframing only works well for first-to-last frame**
  - Short distances between inplace images don't work well, needs more room like 177 frames vs 121
  - *From: Kijai*

- **New dynamic input node system eliminates JavaScript requirements**
  - Native support for dynamic inputs in ComfyUI, though inputs grow from under cursor which can be inconvenient
  - *From: Kijai*

- **LTX2 is very sensitive to specific words in prompts**
  - The word 'stepped' in a prompt caused unwanted steps/bricks to appear in the video. Removing the word fixed the issue completely with same seed
  - *From: Ablejones*

- **Image enhancement between passes works for video**
  - VAE decode video output of first sampler, run through image enhancement nodes, then encode again for second sampler adds great detail
  - *From: David Snow*

- **Not using LTX upscalers helped motion quality**
  - Using RIFE on final output instead of LTX upscalers, combined with LCM and fixed distilled sigma values plus normalizing sampler improved motion
  - *From: Phr00t*

- **Specific sigma values improve quality for distilled model**
  - Manual sigma values: 1., 0.99375, 0.9875, 0.98125, 0.975, 0.909375, 0.725, 0.421875, 0.0
  - *From: David Snow*

- **Temporal upscaler on empty latents just doubles frame count**
  - Using temporal upscaler on empty latents doesn't provide any special benefits - it just increases frame count same as setting empty latent node to more frames
  - *From: Kijai*

- **LTX Video 2 works well with Aussie accents and lipsync**
  - Initial testing shows good accent handling and accurate lip synchronization
  - *From: mdkb*

- **Motion timing is much better in LTX than WAN**
  - LTX provides superior motion timing compared to WAN, though WAN may still be better for some 2D content
  - *From: dj47*

- **Camera LoRAs dramatically reduce artifacts in LTX2**
  - Using camera movement LoRAs at 1.0 strength significantly reduces artifacts when camera moves in any direction
  - *From: protector131090*

- **Anime LoRA trained on images produces more anime-like motion in I2V**
  - LoRA trained only on anime images when used in image-to-video produces more anime-style motion characteristics
  - *From: protector131090*

- **Higher FPS (48-60) helps with motion quality**
  - Increasing base fps to 60 fixed blur/artifacts on motion, though may cause OOM issues
  - *From: veldrin*

- **Res_2s samplers are 2x slower than normal samplers**
  - Res_2s subsampling samplers double the steps, so should be compared against double steps on normal samplers for fair comparison
  - *From: Nekodificador*

- **LTX2 motion blur artifacts caused by latent space compression**
  - Motion blur happens because the latent space is tightly packed - 8 frames in one latent vs Wan's 4 frames
  - *From: Kijai*

- **Higher FPS reduces motion blur artifacts**
  - Using higher FPS conditioning reduces motion blur problems in LTX2
  - *From: Kijai*

- **Temporal upscaler on empty latent is mathematically identical to doubling frame count**
  - Using temporal upscaler before sampling on empty latent does nothing - it's the same as just increasing frame count
  - *From: Ablejones*

- **Audio latents are fixed at 25 FPS regardless of video FPS**
  - Audio processing always uses 25 latents per second in LTX2, formula: ceil((video_frames / video_fps) * 25)
  - *From: phazei*

- **Max shift parameter can be lowered for high resolution/frame count issues**
  - When getting scheduler errors with high res/frames, lowering max shift helps
  - *From: Kijai*

- **Frame interpolation works best with 12 frame gaps**
  - For frame interpolation, 12 frame gaps work smoothly, 9 frames can be stuttery
  - *From: Kijai*

- **VAE smearing issue on last pixel frames**
  - Smearing is a well-known VAE issue that affects the last frames of videos, not yet fixed
  - *From: harelcain*

- **Latent temporal upscaler improves smearing**
  - Using latent temporal upscaler with extra denoising at low sigmas before VAE decode reduces smearing
  - *From: harelcain*

- **Audio sync padding solution**
  - Padding the end of each video chunk with 7 frames fixes audio sync issues when stitching clips
  - *From: VRGameDevGirl84(RTX 5090)*

- **Resolution affects lip sync functionality**
  - 848x480 resolution causes freezing/no movement in lip sync workflows, while 480x256 works
  - *From: mdkb*

- **Guide nodes may be incorrect for i2v workflows**
  - Using a guide node to set frame 0 is incorrect - should use LTXVImgToVideoInplace like regular i2v workflows
  - *From: TK_999*

- **Prompting 'shouting' instead of 'speaking' improves lip movement**
  - Switching from 'he says' to 'he shouts' helped boost mouth movement significantly
  - *From: David Snow*

- **Increasing audio volume helps lipsync**
  - Sometimes audio doesn't drive lipsync until volume is increased, audio normalization helps
  - *From: Nekodificador*

- **Film grain causes still image problem in i2v**
  - Adding more than 0.05 film/image grain results in still image output - LTX2 assumes grainy images are stills from documentaries
  - *From: Vardogr*

- **Experimental attention patch improves lipsync**
  - New experimental node makes lipsync work when without it only produces still images, tried 5 seeds and worked each time
  - *From: Kijai*

- **Higher framerate helps with action scenes**
  - Must increase frame rate to 28+ frames for action, tested up to 120 frames which helped. Larger resolution + more frames = less motion artifacts
  - *From: dj47*

- **Guide keyframes need to be removed before decode in LTXV**
  - The index doesn't matter, LTXV works with guides being after all real frames, but guides need to be removed before decode
  - *From: Gleb Tretyak*

- **Audio to video attention can be boosted for existing audio**
  - New node allows boosting audio to video attention, useful when not generating new audio and want stronger effect on visuals
  - *From: Kijai*

- **Memory optimizations significantly reduce VRAM usage**
  - Two nodes together save 6GB VRAM at 1024x1024x500 frames, peaked at 14GB instead of expected higher usage
  - *From: Kijai*

- **Model repeats content to fit frame count**
  - Repeat happens when model tries to fit prompt into the frame count, similarly as it tries to speed or slow it down
  - *From: Kijai*

- **Higher conditioning FPS improves motion detail**
  - Bumping conditioning fps from 24 to 30+ gives better motion detail, helps reduce motion blur on mouth/teeth
  - *From: ucren*

- **Distilled model with negative distill LoRA removes overcooked look**
  - Using distilled model with distill LoRA at negative values (-0.4 to -0.6) removes the baked/cartoonish appearance
  - *From: David Snow*

- **Single pass at final resolution can be faster than 2-pass approach**
  - Speed is better with 1 pass at final resolution vs 2 passes due to offloading/loading time for second part
  - *From: Abyss*

- **VRAM usage reduced to 61% for FHD 169 frames with new patches**
  - Added patches and VRAM only goes up to 61% when sampling an FHD 169 frames clip
  - *From: burgstall*

- **6GB peak VRAM reduction tested with specific resolution**
  - 6GB peak VRAM reduction was tested with 1024x1024x497
  - *From: Kijai*

- **Attention tuning node refactors main forward function**
  - To make attention tuning possible, had to patch over the whole main forward function of the model, refactored it and tested stuff which ended up reducing VRAM use even more
  - *From: Kijai*

- **LTX2 model caps performance on RTX 5090**
  - Model pretty much caps on 5090 already, the length and resolution it can do is limited
  - *From: Kijai*

- **Spatial inpainting works for single frames**
  - With latent masking disabled, only masking the model timesteps, spatial certainly works for single frames at least
  - *From: Kijai*

- **Negative prompting with distilled LoRA at -0.3 fixes frozen frame issues**
  - Using distilled LoRA set to -0.3 resolves the 'frozen frame, slow zoom in, nothing moving' situation that was causing problems
  - *From: mdkb*

- **Audio attention tuner significantly improves lip sync performance**
  - Boosting audio_to_video attention has major effect on lip sync, consistently prevents failures when used
  - *From: Kijai*

- **LTXV Spatio Temporal Tiled VAE Decode recommended for 2nd pass upscaling**
  - Multiple users confirm this is the best VAE decode method for upscaling passes
  - *From: Abyss*

- **Higher FPS helps with fast motion but costs more resources**
  - 50fps definitely helps with fast motion compared to 25fps, but significantly increases computational cost
  - *From: N0NSens*

- **SageAttn memory optimization reduces VRAM usage significantly**
  - 704x704x121 activations only cost ~300MB with new SageAttn implementation, major VRAM savings achieved
  - *From: Kijai*

- **LTX2 can generate very long videos at low resolution**
  - 2000+ frames possible at 320x320 resolution
  - *From: Kijai*

- **Model quality degrades with length and resolution**
  - Memory isn't the issue with length, quality goes down and there's a limit to what the model can do
  - *From: Kijai*

- **Model reacts oddly to silence**
  - If audio clip ends in silence, it sometimes fades video to black which ruins extensions
  - *From: Kijai*

- **Audio mask values have huge effect**
  - Difference between 0.8 mask vs 0.9 mask is huge for audio
  - *From: Kijai*

- **Model has shallow focus behavior**
  - When faces move forward toward camera, they often go out of focus, like there's a set focal point
  - *From: Kijai*

- **50fps version generation possible**
  - Demonstrated 50fps frog singing video
  - *From: Kijai*

- **Three memory optimization patches provide significant VRAM savings**
  - Sage Attention patch, Chunk Feedforward, and LTX2 Mem Eff Sage Attention Patch can enable 1280x1280 for 1000 frames on 20GB VRAM
  - *From: Kijai*

- **Temporal overlap fixes brightness adjustment issues**
  - Cranking temporal overlap up fixed brightness shifts that occur around 5 second mark in videos
  - *From: Arts Bro*

- **Memory usage factor can be adjusted for extreme VRAM optimization**
  - Default is 0.077 for LTX2, can go down to 0.04 with all patches, but values may vary and should be adjusted carefully
  - *From: Kijai*

- **Higher init resolution provides better likeness from input image**
  - Using higher initial resolution in I2V gives more accurate character preservation
  - *From: N0NSens*

- **FP32 precision fixes certain I2V issues with bf16**
  - When bf16 causes errors in I2V, switching to fp32 resolves the issue
  - *From: Kijai*

- **Weight missing spam should be gone when using fp8/fp4 Gemma3**
  - Specific fix for weight missing error messages
  - *From: Kijai*

- **Active PR cuts normal VAE memory use by more than half**
  - Major memory optimization for VAE processing
  - *From: Kijai*

- **Can do 2000 frames at 320x320 resolution**
  - Model supports very long sequences at low resolution
  - *From: Kijai*

- **Tiny VAE made inference faster due to smaller size**
  - Performance improvement from using smaller VAE
  - *From: hicho*

- **Memory optimization nodes come into play especially in ic Lora workflows**
  - Specific use case where memory optimization is most beneficial
  - *From: Kijai*

- **Can use offload multiplier 0.04 with all optimizations**
  - Very low offload multiplier possible with memory optimizations
  - *From: Kijai*

- **PyTorch 2.10 has native varlen attention**
  - PyTorch 2.10 includes native variable length attention support, reducing need for flash_attn
  - *From: Kijai*

- **LTX2 runs in bf16 by default**
  - Model runs in bf16 format, certain nodes like TinyVAE have no effect
  - *From: Kijai*

- **Patch torch causes significant slowdown**
  - Using patch torch increased generation time from 158 sec to 436 sec on first run
  - *From: psylent_gamer*

- **Using distilled model vs full LTX2 model affects output quality**
  - User found that ditching the distilled model helped significantly with generation quality
  - *From: makeitrad*

- **Studio drivers improve performance over game-ready drivers**
  - Switching from gameready to studio drivers made image generation noticeably faster, studio drivers are older version of same driver
  - *From: David Snow*

- **Keyframes act as literal guides in LTX2**
  - Keyframes were found to be literal guides, with Phr00t's workflow being best for FFLF (first frame last frame)
  - *From: mdkb*

- **sa_solver sampler produces good quality at nearly half the rendering time**
  - sa_solver: 182s for 2x10s segments vs res_2s: 343s for same generation, with comparable or better quality
  - *From: ZombieMatrix*

- **Higher resolution reduces artifacts significantly**
  - The only way to reduce artifacts is higher resolution - preferably 4K, also using camera loras helps
  - *From: protector131090*

- **FP4 model can work effectively as FP16 replacement**
  - Using KJ loaders made everything faster including VAE, FP4 benefits from small model yet loads same as FP16
  - *From: hicho*

- **fp32 takes significantly more VRAM and is slower on RTX 2060**
  - Performance comparison between precision formats
  - *From: hicho*

- **fp8 is faster than fp4 on RTX 3060**
  - 16s vs 20s generation time
  - *From: Xor*

- **System RAM usage can spike to 75GB during tiled VAE processing**
  - During 1500 frame generation at 704x704
  - *From: FryingMan*

- **ComfyUI automatically switches to tiled VAE when regular VAE hits OOM**
  - Automatic fallback mechanism
  - *From: FryingMan*

- **Default distill scheduler is linear_quadratic with shift 8.0**
  - 2nd stage uses the last 4 of that schedule
  - *From: Kijai*

- **Dev model produces black output at 1920x1088 but works at 1792x1088**
  - Resolution limitations of the dev model
  - *From: Ablejones*

- **Using LTXV scheduler with full distill is wrong and shouldn't be used**
  - Scheduler compatibility issue
  - *From: Kijai*

- **LTX reference code doesn't use token scaling**
  - The official reference implementation simply doesn't use token scaling in the scheduler
  - *From: Kijai*

- **Diffusers implementation uses separate CFG for audio and video**
  - In the diffusers implementation, CFG is handled separately for audio and video components
  - *From: Kijai*

- **Official distill LoRA matches extracted LoRA**
  - Testing showed that the official distill LoRA produces the same results as manually extracted LoRA, confirming they are the same model
  - *From: Kijai*

- **LTX scheduler doesn't go below 0.1**
  - The LTX2 pipeline scheduler doesn't actually go below 0.1 in the denoising process
  - *From: Ablejones*

- **Preview functionality merged into ComfyUI**
  - The preview feature has been merged into ComfyUI master and will preview on the sampler
  - *From: ˗ˏˋ⚡ˎˊ-*


## Troubleshooting & Solutions

- **Problem:** NestedTensor error in append_keyframe
  - **Solution:** No specific solution provided, user seeking help
  - *From: hicho*

- **Problem:** Audio noise with LTXVNormalizingSampler and masking
  - **Solution:** Issue occurs because normalization scales masked portions of audio latents, breaking VAE decoding
  - *From: Xor*

- **Problem:** Static noise with normalizing sampler on I2V
  - **Solution:** Turn off preview node, issue seems related to sageattn or LTXV Chunk FeedForward
  - *From: FUNZO*

- **Problem:** I2V produces static images instead of animation
  - **Solution:** Try loading camera control LoRA or lower image strength to around 0.5
  - *From: nikolatesla20*

- **Problem:** Gray videos with sound output
  - **Solution:** No solution provided, user seeking help
  - *From: Nokai*

- **Problem:** Face drifting in I2V generations
  - **Solution:** Try lowering preprocess steps to 22-27 or turning off completely, ensure videoInPlace strength at 1.0
  - *From: ucren*

- **Problem:** Preview node not working with normalized sampler
  - **Solution:** Use the old sampler instead - preview works on first pass but becomes noise on subsequent passes due to normalizing sampler looping
  - *From: zelgo_*

- **Problem:** Audio becoming gibberish with preview override
  - **Solution:** Preview override node only touches callback function - issue is with sampler compatibility
  - *From: Kijai*

- **Problem:** Distortion in humans at bottom of 1:1 aspect ratio
  - **Solution:** Avoid very tall aspect ratios, squash down the dimensions to clear the problem
  - *From: GalaxyTimeMachine*

- **Problem:** LTXAVTEModel processor attribute error
  - **Solution:** Remove the Gemma Prompt Enhance node as it doesn't work properly
  - *From: GalaxyTimeMachine*

- **Problem:** Wrong pronunciation in TTS
  - **Solution:** Type names phonetically (e.g., 'Keej-eye' for Kijai) or use Japanese characters キジャイ
  - *From: GalaxyTimeMachine*

- **Problem:** I2V producing corrupted output after first frame
  - **Solution:** Check text encoder configuration or use provided working workflow
  - *From: Wicked069*

- **Problem:** Normalization sampler not working with audio masks
  - **Solution:** Use Kijai's normalization node instead which attempts to handle masks properly
  - *From: Kijai*

- **Problem:** VAE loading error with old code
  - **Solution:** Update ComfyUI and KJNodes if using VAE loader from it
  - *From: Kijai*

- **Problem:** Sample upscale error on second run
  - **Solution:** Restart ComfyUI - appears to be a bug that happens on second execution
  - *From: avataraim/zelgo_*

- **Problem:** Audio too short causing padding error
  - **Solution:** Use longer audio files to avoid 'Padding size should be less than the corresponding input dimension' error
  - *From: randomanum*

- **Problem:** No previews in new ComfyUI installation
  - **Solution:** Install LTXVLatentPreview node for previews to work
  - *From: Miku*

- **Problem:** mat1/mat2 error with Qwen CLIP
  - **Solution:** Issue reported but no clear solution provided
  - *From: sftawil*

- **Problem:** I2V generates static images without movement
  - **Solution:** Add camera LoRA or use structured scene-based prompts with timestamps
  - *From: Mazrael.Shib*

- **Problem:** Inpainting broken after ComfyUI update
  - **Solution:** Revert to commit just before av_model.py changes that were pushed to comfy
  - *From: Hashu*

- **Problem:** White glow around objects in videos
  - **Solution:** Likely caused by high contrast on low resolution
  - *From: LarpsAI*

- **Problem:** VAE decode seams in tiled decoding
  - **Solution:** Use 1 tile 0 overlap for best results, or adjust tile size/overlap settings
  - *From: ucren*

- **Problem:** Memory issues with LTXV Set Audio Video Mask By Time
  - **Solution:** Some users report memory issues but may be resolved with updates
  - *From: ZombieMatrix*

- **Problem:** Portrait aspect ratio causing weirdness
  - **Solution:** Heavily prompt 'selfie style' for portrait videos
  - *From: jiffyam*

- **Problem:** Inpainting broken currently
  - **Solution:** Kijai provided fix at https://github.com/kijai/ComfyUI/commit/9c76f1076c5e80051af8544d330e9bf8a937e577 - overwrite file and reboot ComfyUI
  - *From: Kijai*

- **Problem:** Getting turtle in inpainted area regardless of prompt
  - **Solution:** Inpainting uses different masking that affects timestep embeds, not traditional latent masking
  - *From: Kijai*

- **Problem:** Audio mismatch error at 1920x1080
  - **Solution:** Use more frames - worked when going to higher frame counts
  - *From: herpderpleton*

- **Problem:** fp8_e4m3fn_fast not working with NAG node on 3090
  - **Solution:** fp8 fast only works on 40xx series and up due to hardware matrix multiplication support
  - *From: Kijai*

- **Problem:** VAE decode error with taeltx_2
  - **Solution:** Need to use preview override node properly and ensure taeltx_2.safetensors model is used as VAE
  - *From: Kijai*

- **Problem:** Audio desync when using trim latent
  - **Solution:** Trim latent cuts from original audio source, causing desync - proper video/audio tensor handling under consideration
  - *From: Elvaxorn*

- **Problem:** Getting stuck at upscale step with 0% progress
  - **Solution:** Try refreshing browser UI, update ComfyUI, or disable sage attention
  - *From: Mazrael.Shib*

- **Problem:** OOM errors on 1920x1080
  - **Solution:** Edit supported_models.py, change value from 0.061 to 0.16, use LTXV Spatio Temporal Tiled VAE Decode instead of regular VAE Decode
  - *From: Alpha-Neo*

- **Problem:** Sage attention causing issues
  - **Solution:** Use --disable-xformers flag to fix sage attention problems
  - *From: Xor*

- **Problem:** Black video outputs
  - **Solution:** Turn off sage attention as it can cause black outputs
  - *From: hudson223*

- **Problem:** Lip sync gets lost during upscaling
  - **Solution:** Lower the denoise significantly where upscale effect becomes less meaningful
  - *From: dj47*

- **Problem:** First/last frames are blurry in LTX2
  - **Solution:** Take first frame, multiply into 5 frames, add to beginning of video. After refining, trim off those 5 frames - errors remain in those first frames
  - *From: N0NSens*

- **Problem:** LTX2 I2V has consistency issues
  - **Solution:** Use camera LoRAs at 1.0 strength to reduce artifacts during camera movements
  - *From: protector131090*

- **Problem:** OOM issues with long videos
  - **Solution:** Use chunking node from KJNodes before second stage sampler, or reduce initial resolution to 0.2x instead of 0.5x
  - *From: ErosDiffusion*

- **Problem:** Long prompts cause ComfyUI to OOM with LTX
  - **Solution:** Keep prompts shorter, too long prompts cause the model to ignore input image
  - *From: Kijai*

- **Problem:** Black output when generating long videos
  - **Solution:** Seems to be a cap around 1000-1400 frames, going past this results in NaNs and black output
  - *From: Kijai*

- **Problem:** Motion artifacts in high movement scenes
  - **Solution:** Generate immediately in high resolution with large number of steps, or use res_2s samplers (though this may restrict motion)
  - *From: N0NSens*

- **Problem:** Memory issues with NAG and FFN nodes together
  - **Solution:** Update both nodes - NAG node was killing memory gains from FFN node, fixed in recent update
  - *From: Kijai*

- **Problem:** Tensor error with feedforward node at high frame counts
  - **Solution:** Restart ComfyUI - it's a random issue not specific to the feedforward node
  - *From: Kijai*

- **Problem:** LTX scheduler goes bonkers with high inputs
  - **Solution:** Lower the max shift parameter when using high resolution and/or lots of frames
  - *From: Kijai*

- **Problem:** VAE decode showing tiles/artifacts
  - **Solution:** Update KJNodes - old VAE loader nodes didn't load metadata properly from new VAE
  - *From: Kijai*

- **Problem:** Audio drift in multi-segment generations
  - **Solution:** Audio starts to drift after first run, need to manually adjust timing by ~7 frames when combining
  - *From: VRGameDevGirl84(RTX 5090)*

- **Problem:** 48kHz audio causing issues
  - **Solution:** Resample audio to 44.1kHz before processing in ComfyUI
  - *From: burgstall*

- **Problem:** Split sampling incompatible with LTX-2
  - **Solution:** Noise scale function doesn't handle combined latent properly - needs fix in multiple places
  - *From: Ablejones*

- **Problem:** Audio sync drift when stitching video chunks
  - **Solution:** Add 7 frames of padding at the end of each video chunk before stitching
  - *From: VRGameDevGirl84(RTX 5090)*

- **Problem:** VAE smearing on last frames
  - **Solution:** Use latent temporal upscaler with extra denoising at low sigmas before VAE decode
  - *From: harelcain*

- **Problem:** SaveVideo NaN/Inf error with audio
  - **Solution:** Use LTX Audio VAE Loader instead of KJ VAE loader, ensure workflow is up to date
  - *From: garbus*

- **Problem:** Spatial mask tensor size error
  - **Solution:** Ensure horizontal_tiles and vertical_tiles are not set to zero, try Spatio Temporal node
  - *From: garbus*

- **Problem:** No lip sync movement with audio input
  - **Solution:** Issue related to resolution settings - 848x480 causes problems, try 896x512 (divisible by 64)
  - *From: TK_999*

- **Problem:** OOM with certain resolutions in audio-driven lipsync
  - **Solution:** Only 480x256 works, other resolutions like 848x480, 832x480 cause frozen image. Issue appears workflow-specific and audio-file driven only
  - *From: mdkb*

- **Problem:** Workflow missing downscale causing 4K output
  - **Solution:** Second pass upscales by 2x, so need to downscale first pass by 0.5. Official LTX workflows have downscale on first sampler
  - *From: David Snow*

- **Problem:** Black or grid output after updating VAE
  - **Solution:** Update KJNodes if using KJ VAE loader, or update ComfyUI itself if using core VAE loader
  - *From: Kijai*

- **Problem:** AddGuideMulti node missing index/strength values
  - **Solution:** Uses newer ComfyUI node features, may need frontend to be newer version
  - *From: Kijai*

- **Problem:** System RAM OOM with 32GB
  - **Solution:** Use --cache-none flag and possibly --disable-pinned-memory. Switch to nightly GGUF nodes if getting corrupted output
  - *From: Kijai*

- **Problem:** ComfyUI freezes using all resources without progress
  - **Solution:** Kill ComfyUI when it uses too much VRAM and starts using shared PC VRAM, making generation extremely slow. Use --reserve-vram command args
  - *From: Gleb Tretyak*

- **Problem:** Tuple index out of range error when generating 2K video
  - **Solution:** Error occurs in audio latent processing during one-pass generation
  - *From: Jonathan Scott Schneberg*

- **Problem:** NAG node not working with first pass after ComfyUI update
  - **Solution:** Second pass still works, but first pass compatibility broken after update
  - *From: JmySff*

- **Problem:** Audio input causing frozen image zoom without lipsync
  - **Solution:** Boost audio using normalization to -14LUFS, adjust LTXImgToVideoInPlace setting to around 0.4, use static camera LoRA
  - *From: mdkb*

- **Problem:** No music lipsync with Q8 GGUF model
  - **Solution:** Normalize audio with higher peaks for better lip sync, use NovaSR for normalization
  - *From: David Snow*

- **Problem:** Overcooked look with distilled model
  - **Solution:** Use distilled model with distill LoRA at negative values (-0.4 to -0.6) to debake
  - *From: David Snow*

- **Problem:** Distilled model giving static image instead of motion
  - **Solution:** Try different seeds, might have been seed-specific issue
  - *From: Danial*

- **Problem:** OOM issues with higher resolution
  - **Solution:** Reduce number of frames in context windows node to 97 or 81
  - *From: Ablejones*

- **Problem:** Audio frying pan noise on 2nd pass upscaler
  - **Solution:** Don't use LTXVNormalizingSampler at all on the 2nd pass
  - *From: Kijai*

- **Problem:** Memory leak causing OOM on second generation
  - **Solution:** Identified as potential RAM leak issue with long video lengths
  - *From: cocktailprawn1212*

- **Problem:** Model loading taking minutes from expensive PCIE5.0 NVMe disk
  - **Solution:** Suspected to be related to transferring Windows drive from old machine without clean reinstall
  - *From: burgstall*

- **Problem:** RTX 2080 can't use bf16 VAE for i2v workflows
  - **Solution:** Hardware limitation - RTX 2080 doesn't support bf16, users must use distilled safetensors with baked VAE instead
  - *From: xwsswww*

- **Problem:** Sync issues between video segments in automated workflows
  - **Solution:** Add logic to send correct frame count based on duration plus extra frames, then trim back to correct duration. Also add pre-roll frames to prevent mouth closed on first frame
  - *From: VRGameDevGirl84*

- **Problem:** VAE Decode hanging indefinitely on 2nd pass
  - **Solution:** Caused by VRAM usage hitting dead spot where it doesn't OOM but uses Windows shared memory. Use --reserve-vram 2 --disable-pinned-memory
  - *From: Kijai*

- **Problem:** Random Indians appearing in 21:9 aspect ratio generations
  - **Solution:** Zoom into subject area to avoid random artifacts appearing in wide aspect ratios
  - *From: David Snow*

- **Problem:** LTXVAddGuide error 'NestedTensor' object has no attribute 'clone'
  - **Solution:** Add it to video latent only
  - *From: Kijai*

- **Problem:** Temporal latent mask not respecting 0 for first frames when last frames also set to 0
  - **Solution:** Use proper guides instead of temporal latent mask for spatial work
  - *From: hablaba*

- **Problem:** Detailer LoRA causing artifacts without guides
  - **Solution:** Feed images or latent as guide using LTXVAddguide node, looping sampler, or in context sampler
  - *From: Hashu*

- **Problem:** Memory optimization patches causing unnecessary offloading
  - **Solution:** Kijai is working on patching memory estimation to prevent unnecessary offloading
  - *From: Kijai*

- **Problem:** Sage attention error 'qk_int8_sv_f8_accum_f16_fuse_v_scale_attn_inst_buf' not found
  - **Solution:** Update sageattention to version 2.2.0 with latest builds, or reinstall torch and sage
  - *From: Kijai*

- **Problem:** Brightness shifts every 5 seconds in videos
  - **Solution:** Increase temporal overlap settings in the VAE
  - *From: Arts Bro*

- **Problem:** RTX 3060 compatibility issues with memory efficient sage
  - **Solution:** Update KJNodes, may need fallback for older sage versions on sm80 cards
  - *From: Kijai*

- **Problem:** Video latent noise mask showing as None
  - **Solution:** Added check for None mask in nodes, but Audio Video Mask node already handles padding
  - *From: Kijai*

- **Problem:** Numpy/numba dependency version mismatch causing import errors
  - **Solution:** pip install numpy == 1.26.4 and numba == 0.63.1
  - *From: Kijai*

- **Problem:** Memory efficiency nodes error with outdated KJNodes
  - **Solution:** Update KJNodes to latest version
  - *From: Kijai*

- **Problem:** Grid artifacts in VAE output
  - **Solution:** Update ComfyUI to latest - new VAE has metadata that needs to be loaded
  - *From: Kijai*

- **Problem:** Tiny VAE loading errors with size mismatch
  - **Solution:** Update ComfyUI with git pull
  - *From: Kijai*

- **Problem:** AttributeError with LTX2 Mem Eff Sage Attention Patch on 3090
  - **Solution:** Update sageattention to version after torch compile support
  - *From: Kijai*

- **Problem:** Audio artifacts on 1st pass
  - **Solution:** Check sageattention version and update if needed
  - *From: Zueuk/Kijai*

- **Problem:** Can't use both LTXVAudioVideoMask and LTXVAddGuide
  - **Solution:** Update KJNodes to latest version, try reverse order
  - *From: Nathan Shipley/Kijai*

- **Problem:** Flash attention and xformers compatibility issues with new PyTorch versions
  - **Solution:** Uninstall flash_attn and xformers - they're not needed for LTX2 and cause errors with newer torch versions
  - *From: Kijai*

- **Problem:** Tried to unpin tensor not pinned by ComfyUI error
  - **Solution:** Related to pinned memory issues, shouldn't affect NAG node functionality
  - *From: Kijai*

- **Problem:** LTXVAddGuidesFromBatch error with combined AV latent
  - **Solution:** Only feed video latent to the node, not combined audio-video latent
  - *From: Kijai*

- **Problem:** Keyframe interpolation showing flashing between images
  - **Solution:** Use more frames (81 frames too few), spread keyframes further apart, and prompt the sequence properly
  - *From: Kijai*

- **Problem:** Out of focus issues in generated video
  - **Solution:** Try removing background and making it flat, or add 'Camera Static Focus Eyes' to positive prompt
  - *From: NC17z*

- **Problem:** ComfyUI terminal crashes with 'install latest nvidia drivers' message
  - **Solution:** Switch from gameready to studio drivers (older version of same driver)
  - *From: David Snow*

- **Problem:** Weak lipsync or character likeness issues
  - **Solution:** Adjust compression noise amount, image strength, audio_to_video attention scale, audio volume, and prompt
  - *From: Kijai*

- **Problem:** ComfyUI crash on TE (Text Encoder)
  - **Solution:** Don't use fp4 TE with ltx2 fp16, try different text encoder
  - *From: hicho*

- **Problem:** Artifacts in video generation
  - **Solution:** Use higher resolution (preferably 4K) and camera loras to reduce artifacts
  - *From: protector131090*

- **Problem:** Different results with same settings on reruns
  - **Solution:** FFN chunk and NAG node changes can affect output; optimizations change results
  - *From: Kijai*

- **Problem:** Dev model produces very noisy, incoherent outputs at high resolution
  - **Solution:** Use distilled lora at low strength (0.2+) with dev model on first pass
  - *From: psilo*

- **Problem:** LTX2 scheduler breaks at high resolution
  - **Solution:** Use reasonable custom schedule instead of LTX2 scheduler at high res
  - *From: TK_999*

- **Problem:** Memory cleanup nodes requiring elevated privileges
  - **Solution:** Remove them - they're not required and only fix issues they cause
  - *From: Kijai*

- **Problem:** WSL crashes during high resolution generation
  - **Solution:** Increase swap size from 16GB to 40GB, use fp8 instead of GGUF
  - *From: gordo*

- **Problem:** Distilled lora breaks when set lower than 0.20
  - **Solution:** Keep distilled lora strength at minimum 0.20
  - *From: Abyss*

- **Problem:** Node missing class_type property error
  - **Solution:** Switch to legacy UI to see what's missing, often the Searge LLM node
  - *From: David Snow*

- **Problem:** TAEHV model size mismatch error
  - **Solution:** Need to install RES4LYF: https://github.com/ClownsharkBatwing/RES4LYF
  - *From: David Snow*

- **Problem:** Character shifting in video-to-video
  - **Solution:** Character LoRAs do make a difference and help maintain consistency, though still challenging
  - *From: NC17z*

- **Problem:** Model inconsistent prompt following
  - **Solution:** Model behavior seems random - sometimes distilled works better, sometimes dev model with distilled LoRA works better
  - *From: N0NSens*


## Model Comparisons

- **Default sampler vs LTXVNormalizingSampler**
  - Default sampler produces 100x better video output, normalizing sampler better for audio but worse video quality
  - *From: Gleb Tretyak*

- **LTX2 vs Wan2GP for lip sync**
  - Wan2GP fails to animate/lip sync properly, just zooms or pans, 2x slower than ComfyUI
  - *From: nikolatesla20*

- **LTX2 vs Wan 2.2 for likeness**
  - Wan 2.2 has better likeness preservation than LTX2, LTX2 tends to drift more
  - *From: ucren*

- **Normalized vs non-normalized audio**
  - Normalized produces steadier volume but may add noise in some cases
  - *From: Kijai*

- **New vs old distilled model audio**
  - New distilled model audio is slightly less annoying than previous version
  - *From: Drommer-Kille*

- **CFG 1 vs scheduled CFG for audio**
  - Scheduled CFG produces better sound quality than CFG 1 with distilled model
  - *From: N0NSens*

- **FP8 vs normal precision**
  - FP8 fast mode produces slightly different output due to floating point accuracy, not necessarily worse but different
  - *From: Kijai*

- **With vs without camera LoRA for I2V**
  - Camera LoRA consistently produces movement in I2V, without it generations often remain static
  - *From: Mazrael.Shib*

- **LTX vs Wan spatial compression**
  - LTX uses 2x more spatial compression than Wan, requiring spatial and temporal upscaling for production-ready results
  - *From: Ablejones*

- **Base model vs distilled model quality**
  - Base model should work fine if setup is correct, distilled not required for good results
  - *From: Ablejones*

- **RIFE49 vs LTX temporal upscale**
  - RIFE49 may look better with less smearing, but LTX upscalers are more efficient as they avoid decode/encode steps
  - *From: Phr00t*

- **Guide vs inplace for last frame**
  - Both work, but inplace is more accurate as it's literal last image rather than guide
  - *From: Kijai*

- **Distilled vs dev model for 9:16**
  - Different outputs even with same prompt/seed, distilled tends to add text overlays, dev model avoids text captions
  - *From: Tyronesluck*

- **LTX2 distilled full vs fp8**
  - People should save 16GB storage and just use fp8 version, quality difference minimal
  - *From: David Snow*

- **Dev model vs distilled**
  - Dev is better if using full potential with more steps and time, but most are happy with distilled
  - *From: David Snow*

- **WAN vs LTX2**
  - WAN still better for outright quality, but LTX2 is faster. For realistic content LTX2 is mindblowing, for 2D animation WAN destroys LTX2
  - *From: xwsswww, protector131090*

- **LTX2 vs WAN motion quality**
  - LTX2 better for overall details, WAN wins for motion quality and temporal consistency
  - *From: David Snow, dj47*

- **FP8 distilled vs GGUF models**
  - FP8 distilled model is faster than GGUFs except for Gemma on 12GB VRAM + 64GB RAM
  - *From: Miku*

- **LTX2 vs WAN for 2D content**
  - WAN still better for 2D/anime content with fewer artifacts, but LTX2 incredible for realistic content
  - *From: protector131090*

- **Hunyuan vs other models for 2D**
  - Hunyuan T2V (older version) was best for anime with almost super clean results, less artifacts than others
  - *From: protector131090*

- **LTX2 full vs fp8 versions**
  - Differences are so minor they might as well not exist, fp8 version performs nearly identically
  - *From: David Snow*

- **LTX2 vs Ovi for joint video/audio**
  - LTX2 is miles better than Ovi, which is the 2nd best option for joint video/audio models
  - *From: Kijai*

- **Euler vs res_2s on first sampler**
  - res_2s may restrict motion - Sonic would not stop T-posing with res_2s, started moving again with euler
  - *From: David Snow*

- **Dev model with distill LoRA vs distilled model**
  - Dev + distill LoRA may be better quality than pure distilled model
  - *From: LarpsAI*

- **FP16 vs FP8 distilled model quality**
  - Couldn't see much difference between fp8 and fp16 distilled models
  - *From: David Snow*

- **15 steps vs 30 steps with distilled**
  - 30 steps with euler simple reduces overcooked/glossy look
  - *From: LarpsAI*

- **LTX-2 vs Wananimate for emotion**
  - LTX-2 is much better at getting emotion from audio in faces, Wananimate has straight faces with emotional vocals
  - *From: VRGameDevGirl84(RTX 5090)*

- **FP4 model performance**
  - Really fast 1080p generation but image is very blurry/soft with 40 steps, audio quality is okay
  - *From: Drommer-Kille*

- **I2V vs T2V for smearing**
  - I2V seems much less prone to smearing, it's still there but reduced
  - *From: metaphysician*

- **AudioSR vs NovaSR vs FlashSR**
  - AudioSR best quality but very slow (359 seconds). NovaSR extremely fast (0 seconds) but lower quality. FlashSR balanced speed/quality
  - *From: David Snow*

- **WAN vs LTX2 for action scenes**
  - WAN does better job with action speed during fight scenes, but LTX2 has better upscaling
  - *From: tarn59*

- **WAN spatial upscaling with LTX**
  - Terrible idea - WAN 832x480 to LTX spatial upscaler x2 produces awful results
  - *From: N0NSens*

- **Distilled LoRA sizes**
  - Original 8GB version vs smaller versions - middle size recommended, fp8 version changes output significantly and not recommended unless absolutely necessary
  - *From: Kijai*

- **Distilled model vs original + LoRA**
  - Slower but perhaps better prompt following
  - *From: N0NSens*

- **Dev fp8 model vs distilled model**
  - Dev fp8 model with distill LoRA at 0.3 works well, distilled model gives cartoonish expressions/deep wrinkle lines
  - *From: Abyss*

- **High res first pass vs low res + upscale**
  - Low res then upscaling gives better motion and faster speeds than high res first pass
  - *From: Elvaxorn*

- **1 pass vs 2 pass workflow**
  - 1 pass can be faster due to less offloading, but 2 pass may give better quality
  - *From: Abyss*

- **Full checkpoint vs KJ's separated stuff with dynamic lora**
  - KJ's approach uses less than 2GB vs 6GB distill LoRA and saves VRAM
  - *From: Elvaxorn*

- **LTX2 vs Wan for coherent long videos**
  - LTX2 can do coherent 600+ frames which is quite the shift from Wan
  - *From: Kijai*

- **Distilled model vs normal model with different settings**
  - Left is distilled only, right has distilled lora at -0.2 showing visual differences
  - *From: TK_999*

- **LTX2 vs WAN for anime content**
  - LTX is much worse with 2D content, too many artifacts compared to WAN which can make almost perfectly clean outputs at 1080p
  - *From: protector131090*

- **Different quantization formats for text encoder**
  - fp8_scaled is closest to bf16 original, Q8 is also pretty good. Differences are subtle but fp8_scaled shows most consistent details across frames
  - *From: Kijai*

- **Euler vs Euler_a samplers**
  - Better results with euler (not _a) for first pass, 30-40 steps recommended over 20 steps
  - *From: IceAero*

- **LTX2 vs Wan 2.1**
  - Not leagues ahead in terms of animation, but technologically superior with sound and movement to sound
  - *From: Abyss*

- **960x544 upscaled vs 1344x736 with latent upscale**
  - Higher res approach is 2x slower but not worth it quality-wise
  - *From: N0NSens*

- **LTX2 vs WAN Animate for pose control**
  - WAN Animate is better for pose control use cases
  - *From: Kijai*

- **Sage++ vs regular sage performance**
  - Speed difference is only 2-5% max, not critical upgrade
  - *From: Kijai*

- **LTX2 vs Veo3.1 and Kling quality**
  - LTX lacks detail resolution and temporal smoothness compared to closed source models
  - *From: dj47*

- **FP16 40GB model vs FP4**
  - FP16 is faster - 10 sec vs 28 sec per step, but requires 100GB page file
  - *From: hicho*

- **With NAG vs without NAG vs baseline with sage**
  - Without NAG: 10 seconds, with NAG: 12 seconds, baseline with sage: 13 seconds for 121x704x704
  - *From: Kijai*

- **LTX2 vs Veo3.1**
  - LTX2 preferred for local use, performance, audio-driven generation and keyframing, while Veo is closed source with limitations
  - *From: Godhand*

- **LTX2 vs Wan 2.2**
  - LTX2 has artifact issues that were solved in Wan 2.2, making it not ready for production until fixed
  - *From: Juan Gea*

- **sa_solver vs res_2s samplers**
  - sa_solver produces comparable quality in nearly half the time (182s vs 343s)
  - *From: ZombieMatrix*

- **LTX2 vs LongCat Avatar**
  - LTX2 is state of the art - LongCat avatar is insanely slow in comparison
  - *From: Kijai*

- **FP8_scaled vs mixed gemma**
  - FP8_scaled is closer to bf16 original based on quantization measurement
  - *From: Kijai*

- **fp8 vs fp4 on RTX 3060**
  - fp8 is faster: 16s vs 20s
  - *From: Xor*

- **Dev model vs distilled model for first pass**
  - Distilled model with negative lora (-0.4 to -0.7) produces more coherent results than dev model alone
  - *From: garbus*

- **LCM vs Res_2s sampler**
  - LCM can produce better results than Res_2s in some cases, particularly for first pass
  - *From: David Snow*

- **Official distill LoRA vs manually extracted LoRA**
  - They produce the same results, confirming they are the same model
  - *From: Kijai*

- **Base vs distilled model image sizes**
  - Different sized images are provided for base vs distilled models for unspecified reasons
  - *From: The Shadow (NYC)*

- **Dev model vs distilled model prompt following**
  - Dev model with distilled LoRA sometimes responds better to prompts than distilled model alone
  - *From: N0NSens*


## Tips & Best Practices

- **Use detailed prompts to prevent identity drift**
  - Context: When generating longer videos or with complex subjects, detailed descriptions help maintain character consistency
  - *From: Mazrael.Shib*

- **Use radau_iia_5s sampler to remove tin voice**
  - Context: Better than NAG for fixing audio quality issues
  - *From: Gleb Tretyak*

- **Stack character LoRA in I2V workflow**
  - Context: Helps maintain character consistency in image-to-video generation
  - *From: ucren*

- **Include words to be spoken in prompt**
  - Context: Typing out dialogue can improve lip sync timing
  - *From: Benjimon*

- **Use 'music video of performer singing passionately' prompt structure**
  - Context: Works well for audio+video generation with good lip sync results
  - *From: Mazrael.Shib*

- **Use guides workflow correctly for 2-sampler setup**
  - Context: Add guides > low res sampler > crop guides > upsample > add guides > full res sampler > crop guides > VAE decode
  - *From: Simonj*

- **Create looping videos using first/last frame conditioning**
  - Context: Use identical frames for first and last positions (ff2lf) to create loops
  - *From: Gleb Tretyak*

- **Use AudioSR for audio upscaling**
  - Context: Post-process audio to improve quality beyond model output
  - *From: Kijai*

- **Try different seeds instead of slow samplers**
  - Context: Rolling different seed values is more sensible than using very slow samplers
  - *From: mallardgazellegoosewildcat2*

- **Use Heun or DPM samplers for speed/quality compromise**
  - Context: Papers suggest these as good balance between speed and quality
  - *From: mallardgazellegoosewildcat2*

- **Upscale separately with SeedVR2**
  - Context: Instead of high resolution generation, use lower res and upscale afterward
  - *From: Tachyon*

- **Use extensive negative prompts only when needed**
  - Context: Best way to use NAG is see what generation is like without negative, then add what you don't like into the NAG prompt
  - *From: DawnII*

- **Add anime-related keywords for anime style**
  - Context: LTX defaults to realism, so add '2d anime, 2d animation, hand drawn cel animation' for anime content
  - *From: dj47*

- **Use consistent prompts with image inputs**
  - Context: Model is prone to break if you ask something weird or contradictory to the input image
  - *From: ErosDiffusion*

- **Use 24-25 fps as good standards**
  - Context: LTX supports range from 15 to 60 fps, 24 or 25 are good standard frame rates
  - *From: ErosDiffusion*

- **Use light denoising with Wan to improve LTX results**
  - Context: For polishing up LTX output with denoising around 0.25
  - *From: Ablejones*

- **Use spatial and temporal upscaling for production-ready results**
  - Context: Due to LTX's higher compression ratio
  - *From: Ablejones*

- **Choose the right anchor image for second sampler**
  - Context: In multiframe workflows, choose image where subject is clear rather than always using first frame
  - *From: Elvaxorn*

- **Crop guides after first pass when using multiframe workflows**
  - Context: Prevents duplication and improves quality in 2-stage workflows
  - *From: neofuturo*

- **Run 720p first stage for better quality**
  - Context: Instead of lower resolutions for first pass
  - *From: neofuturo*

- **Use NAG (negative prompt) to avoid text/subtitles**
  - Context: Especially helpful for 9:16 aspect ratio
  - *From: Kijai*

- **Higher resolution helps with fast motion**
  - Context: Anything under 1080p has issues with fast movement, both higher res and fps help
  - *From: Arts Bro*

- **Add negative prompt even if empty**
  - Context: Empty negative is different than zeroed out negative, affects non-distilled model significantly
  - *From: Ablejones*

- **Use 8n+1 frame counts for proper generation**
  - Context: Frame count should follow this pattern, e.g., 49 frames for 24fps (48+1)
  - *From: dj47*

- **Describe image style in prompt to maintain consistency**
  - Context: Add description like 'The image is an anime style semi-realistic 2.5D' at start of prompt
  - *From: veldrin*

- **Use --novram flag for higher resolutions on limited VRAM**
  - Context: Enables 1080p generation on cards like 3090
  - *From: dj47*

- **Be very careful with word choice in prompts**
  - Context: LTX2 is extremely sensitive to specific words which can trigger unintended visual elements
  - *From: Ablejones*

- **Use 'prefer no system fallback' option**
  - Context: Turn on NVIDIA option to avoid horribly slow generation, will OOM instead so you can adjust settings
  - *From: Ablejones*

- **1536x864 is sweet spot resolution**
  - Context: This resolution works best for the model according to testing
  - *From: Arts Bro*

- **720p minimum for cleaner results**
  - Context: Several people suggest 720p minimum resolution for better quality outputs
  - *From: mdkb*

- **Low denoise with WAN for polishing LTX output**
  - Context: Use WAN model with denoise under 0.3 as detailer/polisher, up to 0.78 as fixer, above that creates new video
  - *From: mdkb*

- **Use WAN pass for better quality**
  - Context: After LTX2 generation, run through WAN for improved quality and reduced artifacts
  - *From: protector131090*

- **Resize images before feeding to LTX2**
  - Context: Better to resize beforehand so you can control how resizing is done (lanczos vs bilinear)
  - *From: Kijai*

- **Use camera LoRAs for specific movements**
  - Context: For panning up, use jib up lora to avoid horrible artifacts
  - *From: protector131090*

- **Generate in high resolution with more steps for quality**
  - Context: Only reliable way to improve motion quality is immediate high-res generation or use WAN
  - *From: N0NSens*

- **Pad first frames to fix artifacts**
  - Context: Multiply first frame into 5 frames, add to beginning, then trim after processing
  - *From: N0NSens*

- **Compare res samplers fairly**
  - Context: Always compare res_2s against double steps on normal samplers, not equal steps
  - *From: Kijai*

- **Use negative distill LoRA to reduce overcooked look**
  - Context: Add distill LoRA with -0.2 to -0.4 strength to make distilled model less overcooked
  - *From: Elvaxorn*

- **Lower mask value allows more motion but sacrifices likeness**
  - Context: For I2V, mask values lower than 1.0 allow more motion but reduce adherence to input image
  - *From: Kijai*

- **Think of mask value like denoise strength**
  - Context: Mask value controls how much T2V vs I2V influence you get
  - *From: Elvaxorn*

- **Use keyframe conditioning at 0.8 strength instead of 1.0**
  - Context: Sometimes strength at 1.0 for all keyframes doesn't work as well as 0.8
  - *From: phazei*

- **Place keyframes far enough apart with smart prompting**
  - Context: Keyframes too close or at full strength make model struggle to interpolate
  - *From: harelcain*

- **Use quieter audio for less intense acting**
  - Context: Since audio and video latents are coupled, loud sounds trigger bigger responses
  - *From: TK_999*

- **Keyframe conditioning on earlier frames**
  - Context: Try conditioning on frame num_frames-3 or num_frames-4 instead of last frame, throw out a few frames after
  - *From: harelcain*

- **Use AddGuides then crop guides for both samplers**
  - Context: For better sampling workflow
  - *From: Elvaxorn*

- **Reduce compression if going over 8 steps**
  - Context: Going more than 8 steps requires bringing down compression or video quality degrades and likeness changes
  - *From: hicho*

- **Normalize audio volume before sampling**
  - Context: Improves lipsync performance, can use FL Studio or volume normalization nodes
  - *From: David Snow*

- **Add more compression noise or reduce i2v strength for movement**
  - Context: When getting still images, prompt for stronger movement, use NAG, try different seeds
  - *From: Kijai*

- **Remove last few frames as they look bad**
  - Context: Use simple math expression to subtract frames from end of video
  - *From: David Snow*

- **Divide intended resolution by 2 when setting up**
  - Context: When using two-pass upscaling workflow to avoid massive output files
  - *From: David Snow*

- **Use camera static LoRA for audio-driven issues**
  - Context: Official workflows use this LoRA, can help with switching between prompt and image
  - *From: David Snow*

- **Use static camera LoRA for better stability**
  - Context: When experiencing camera movement issues or frozen image problems
  - *From: mdkb*

- **Remove ICDetailer for most cases**
  - Context: Unnecessary 99% of the time especially for i2v, can cause conflicts with other LoRAs
  - *From: ucren*

- **Test base settings before adding multiple LoRAs**
  - Context: Don't stack multiple LoRAs when troubleshooting, start with base and tune one thing at a time
  - *From: ucren*

- **Increase resolution and crop video for better face quality**
  - Context: When faces are getting messed up in low resolution generations
  - *From: David Snow*

- **Use redundant prompting for better adherence**
  - Context: Model requires very specific prompting, 'hair burst into flames burning on head' works better than 'hair burst into flames'
  - *From: MysteryShack*

- **Prompt action followed by dialogue**
  - Context: Use format like 'action followed by then she says...' for better prompt adherence
  - *From: Elvaxorn*

- **Use starting input image with teeth slightly visible**
  - Context: May help with teeth detail generation
  - *From: Abyss*

- **Try higher fps for better fine details**
  - Context: When struggling with details like teeth
  - *From: Abyss*

- **Use tiled upscale instead of full-frame generation above 720p**
  - Context: You mostly don't need full-frame gen if going above 720p, tiled upscale negative effects tend to be really low
  - *From: mallardgazellegoosewildcat2*

- **Context windows work fine for upscaling since guidance is strong from original video**
  - Context: Don't need tiling for upscaling workflows
  - *From: Ablejones*

- **Leave attention tuner and chunk feed forward settings at default**
  - Context: For VRAM optimization nodes
  - *From: veldrin*

- **Connect new VRAM nodes after LoRAs, before NAG node, before CFGGuider**
  - Context: Proper workflow connection for memory optimization
  - *From: veldrin*

- **Normalize audio to -14 LUFS for better lip sync**
  - Context: Forces mouth movement when audio is present, can be reduced once lip sync is working properly
  - *From: mdkb*

- **For realism, lower detailer LoRA strength and use more steps**
  - Context: Use 30-40 steps first pass with euler sampler, detailer at 0.15-0.25 for first pass, ~0.4 for second pass
  - *From: IceAero*

- **Don't use normalizing sampler on upscale pass**
  - Context: Only use normalizing sampler on first pass, not for upscaling
  - *From: veldrin*

- **Higher audio attention makes characters more expressive**
  - Context: Increasing audio values makes character articulate more and adds hand/body movement, but don't set too high
  - *From: Abyss*

- **For T2V workflows, set image strength to 0 on i2v workflows**
  - Context: Easy way to convert i2v workflows to t2v, may have brief flash of original image at start
  - *From: David Snow*

- **Use 2-stage workflow for long videos**
  - Context: For handling longer generations effectively
  - *From: Kijai*

- **Handle audio crossfading before generation**
  - Context: Better to use audio tools to crossfade between audios before video generation
  - *From: Nekodificador*

- **32fps might be sweet spot for lip sync**
  - Context: 48fps too hectic and runs out of usable frames too soon, 24fps lacking motion detail
  - *From: David Snow*

- **Remove sound to prevent random talking**
  - Context: If you remove sound altogether in generation, characters won't randomly talk
  - *From: JUSTSWEATERS*

- **Use first pass at full resolution for best quality**
  - Context: Better than using 2-pass upscaler approach
  - *From: Abyss*

- **Use both normal sage patch and memory efficient sage together**
  - Context: Memory efficient sage doesn't affect cross attention, benefits from regular sage too
  - *From: Kijai*

- **Put optimization patches before LoRAs when branching to multiple model stages**
  - Context: Ensures patches affect both models when workflow branches
  - *From: Kijai*

- **Use lower resolution for very long generations**
  - Context: 352x640 upscaled to higher resolution works well for 700+ frame videos
  - *From: N0NSens*

- **NAG node works better with fewer words**
  - Context: Instead of long negative prompts, use simple phrases like 'hand movement'
  - *From: Miku*

- **Remove --reserve-vram flag when using new optimization patches**
  - Context: New memory patches make manual VRAM reservation unnecessary
  - *From: NC17z*

- **Use single venv for everything instead of multiple ComfyUI installs**
  - Context: Managing multiple models and custom nodes
  - *From: Kijai*

- **Learn manually installing custom nodes and dependencies**
  - Context: Makes everything easier than using automated scripts
  - *From: Kijai*

- **Use git pull instead of automated scripts to avoid 90% of update issues**
  - Context: Updating ComfyUI
  - *From: Kijai*

- **If VRAM use isn't maxed out when offloading, decrease the memory usage factor**
  - Context: Optimizing memory usage with memory optimization nodes
  - *From: Kijai*

- **Think of IC Detailer lora like tile controlnet - use whole video as guide**
  - Context: Using IC Detailer lora properly
  - *From: Kijai*

- **Can do final pass with Wan for HD quality**
  - Context: Getting high quality video output
  - *From: Kijai*

- **Higher value offloads more in memory usage factor**
  - Context: Tuning memory optimization
  - *From: Kijai*

- **Tiny VAE should be used in preview node only**
  - Context: Proper usage of tiny VAE
  - *From: hicho*

- **Start with 2 images for keyframe interpolation to understand how it works**
  - Context: When learning keyframe interpolation workflow
  - *From: Kijai*

- **Use higher audio_to_video scale if getting frozen video issues**
  - Context: When video shows slow pan/frozen motion despite audio
  - *From: Kijai*

- **Add camera static at 0.5 and distill lora at -0.3 for better lipsync**
  - Context: When getting frozen video with motion only at the end
  - *From: mdkb*

- **Flash attention and sage attention can run together without issues**
  - Context: Contrary to some beliefs about compatibility
  - *From: veldrin*

- **Remove prompt 4 when editing for 3 frames**
  - Context: The model is built to prompt 4 keyframes, so duplicate last frame or edit out prompt 4
  - *From: The Shadow (NYC)*

- **Use empty positive prompt for simple camera movements**
  - Context: When trying to get simple camera movements from frame to frame
  - *From: xwsswww*

- **Seed luck is crucial for quality results**
  - Context: Biggest factors for quality are framerate, resolution, and seed luck
  - *From: David Snow*

- **Launch ComfyUI with --high-vram or --gpu-only for high VRAM cards**
  - Context: Keeps all models in VRAM to avoid loading times on cards like RTX 6000
  - *From: Kijai*

- **Use 2-stage workflow for very long generations**
  - Context: First do low res long generation, then upscale - quality suffers with length so reduce resolution to balance
  - *From: Kijai*

- **Reduce resolution to balance quality when increasing length**
  - Context: Quality starts to suffer with very long generations
  - *From: Kijai*

- **Use distilled lora at 0.6 strength with dev model for better results**
  - Context: Even with 20 steps euler cfg1
  - *From: gordo*

- **Split model files for better results**
  - Context: Results became way better when using split files
  - *From: gordo*

- **Cap prompts at 200 words for better results with quants**
  - Context: Especially when not using distilled model
  - *From: The Shadow (NYC)*

- **Over-describe prompts for better results**
  - Context: Everything with LTX T2V seems to work better when you really over-describe things
  - *From: garbus*

- **Use I2V for testing**
  - Context: I2V provides a clear starting point for comparing model performance
  - *From: N0NSens*

- **Changing one word in prompt has greater impact than seed changes**
  - Context: Prompt modifications often have more significant effects than seed variations
  - *From: gordo*


## News & Updates

- **LTX-2.5 in active development**
  - Building new latent space with better properties for preserving spatial and temporal details, mentioned in CEO AMA
  - *From: ZeusZeus (RTX 4090)*

- **1 million HuggingFace downloads reached**
  - LTX2 model has achieved 1M downloads milestone
  - *From: ZeusZeus (RTX 4090)*

- **ComfyUI main branch updated**
  - VRAM optimization changes merged to main ComfyUI, no need to edit av_model.py file anymore
  - *From: Kijai*

- **Orbital LoRA available for LTX2**
  - Nebsh has created orbital camera movement LoRA for LTX2
  - *From: Charlie*

- **Preview support added for LTX Video 2**
  - LTX2 Sampling Preview Override node enables previews during generation
  - *From: Kijai*

- **KJNodes updated to fix preview compatibility**
  - Updated to work with normalization sampler
  - *From: Kijai*

- **LTX2 Audio Latent Normalizing Sampling node added**
  - New node that gives identical results to sampler and supports masks
  - *From: Kijai*

- **LTX-2 team considering free Gemma embeddings API**
  - To solve Gemma bottleneck in workflows by providing API that returns Gemma embeddings for prompts, reducing switching between models
  - *From: StatusReport*

- **Tiny VAE being worked on for better preview quality**
  - Current preview quality can only be improved with tiny VAE which is being developed
  - *From: Kijai*

- **LTX 2 TAE uploaded to GitHub**
  - Available at https://github.com/madebyollin/taehv/tree/main/safetensors
  - *From: yi*

- **ComfyUI pull request for tiny VAE support**
  - PR #11929 for native ComfyUI support
  - *From: Kijai*

- **LTX 2.5 already in development**
  - Team working on updates including 9:16 aspect ratio improvements
  - *From: ˗ˏˋ⚡ˎˊ-*

- **LTX team knows about i2v issues and will release update soon**
  - They are aware of i2v problems and planning to improve it
  - *From: Ruairi Robinson*

- **LTXVNormalizingSampler appeared in nightly build**
  - New normalizing sampler node was added to nightly version within last 24 hours
  - *From: mdkb*

- **LTX Video 2 released January 5, 2026**
  - Supports text-to-video and image-to-video generation with audio
  - *From: community*

- **Memory optimizations for LTX2 in ComfyUI**
  - Recent updates improved VRAM usage and offloading, may no longer need --reserve-vram flags
  - *From: Kijai*

- **NAG and FFN node memory issue fixed**
  - Updated yesterday - NAG node was killing memory gains from FFN node when used together
  - *From: Kijai*

- **Normalizing sampler causes detail degradation**
  - Swapping to new Normalizing sampler causes some degrading of details, may be due to tweaked sigmas and cfg scheduled
  - *From: The Shadow (NYC)*

- **NAG node significantly improves LTX performance**
  - NAG node fixes many issues with LTX mixing things up and improves results dramatically
  - *From: nikolatesla20*

- **LTX-2 Chattable KB updated with fresh Discord scrape**
  - Knowledge base updated with past week's discussions, can ask about ai-toolkit or recent developments
  - *From: Nathan Shipley*

- **LoRA support temporarily broken**
  - Broken in current code due to incompatibility with memory optimizations, have working branch for testing, will make PR soon
  - *From: Kijai*

- **WHATUSEE LoRA released**
  - Spent most of last weekend working on it
  - *From: burgstall*

- **KJNodes updated 12 hours ago**
  - Latest version needed for new VRAM optimizations
  - *From: Kijai*

- **Tiny VAE PR submitted to main ComfyUI**
  - Super light VAE for better preview quality, not yet supported in main comfy
  - *From: Kijai*

- **A2V announcement is about LTX Studio app partnership with ElevenLabs**
  - Today's A2V announcement is tooling built into LTX Studio app, work on standalone A2V continues
  - *From: LTX Lux*

- **ComfyUI commit removes amplitude normalization from audio encoding**
  - New commit affects audio to video workflows and audio extension by removing amplitude normalization bit from audio encode
  - *From: Kijai*

- **Kijai updated audio masking nodes**
  - Fixed 'truncate' behavior to actually cut video to max length, added 'partial' mode for old behavior, nodes can be chained
  - *From: Kijai*

- **GGUF CLIP support working**
  - GGUF clip models have been working for a week now, including unsloth gemma3 12b with ComfyUI-GGUF
  - *From: Kijai*

- **Major memory optimization improvements**
  - Most memory optimization ever done including Chunked FFN, refactored LTX2 model forward function, custom Sage attention forward
  - *From: Kijai*

- **NAG (Negative Augmented Generation) node released**
  - Kijai released NAG node for better negative prompting with LTX2
  - *From: Kijai*

- **Tiny VAE PR merged**
  - Can now use Tiny VAE with attention override node
  - *From: Kijai*

- **LTX 2.1 expected in February**
  - Community anticipating improvements in version 2.1
  - *From: Lodis*

- **ComfyUI PR 12028 for memory optimization**
  - Significant improvement to memory handling
  - *From: Kijai*

- **Qwen3-TTS released**
  - New text-to-speech model available
  - *From: Gill Bastar*

- **ComfyUI 3.6.0 available but no reason to update**
  - Latest version available
  - *From: Kijai*

- **VAE memory reduction PR merged into ComfyUI**
  - Many workflows can now ditch tiled VAE decode
  - *From: Kijai*

- **Custom allocator PR in development**
  - Rattus building custom allocator to allow offloading on the fly, currently Nvidia only
  - *From: Kijai*

- **New Nvidia blog post about RTX AI Garage ComfyUI tutorial**
  - https://blogs.nvidia.com/blog/rtx-ai-garage-comfyui-tutorial/
  - *From: LTX Lux*

- **Kijai made NAG node inplace application optional**
  - Disabled = same output as before, enabled = less memory but different output
  - *From: Kijai*

- **Core ComfyUI updates allow dropping tiled LTX VAE**
  - Recent commit allows this optimization
  - *From: Gleb Tretyak*

- **Tiny VAE now on main ComfyUI branch**
  - Core integration completed
  - *From: Gleb Tretyak*

- **Kijai submitted PR for memory savings to ComfyUI core**
  - Memory optimizations being integrated into main codebase
  - *From: Kijai*

- **Kijai working on fully native prompt enhancer**
  - Can understand images, doesn't use transformers, very custom code
  - *From: Kijai*

- **Daily summaries updated with GPT-5-2-High fact-checking**
  - Line-by-line fact/sense-check to decrease errors
  - *From: pom*

- **Preview functionality merged into ComfyUI**
  - Preview feature now works on the sampler in master branch, with daily releases available
  - *From: ˗ˏˋ⚡ˎˊ-*


## Workflows & Use Cases

- **First Frame Last Frame (FFLF) with LTX2**
  - Use case: Controlling start and end frames of generation
  - *From: Gleb Tretyak*

- **AddGuide with index -1 and inplace**
  - Use case: Guide first frame for better control
  - *From: Gleb Tretyak*

- **TTM (Text-to-Motion) method**
  - Use case: Artist-focused approach for longer duration content with audio sync
  - *From: Guey.KhalaMari*

- **First/Middle/Last frame conditioning**
  - Use case: Creating videos with specific keyframes at beginning, middle, and end
  - *From: Simonj*

- **Two-stage upscaling with guides**
  - Use case: Generate low resolution first, then upscale with proper guide cropping
  - *From: Simonj*

- **I2V with lip sync**
  - Use case: Image-to-video generation synchronized with audio input
  - *From: ErosDiffusion*

- **Voice cloning workflow for LTX videos**
  - Use case: Clone voice from LTX generated videos using RVC Engine or F5-TTS
  - *From: Nokai/PsiClone/Gleb Tretyak*

- **ImageAudioVideo to Video with pose LoRA**
  - Use case: 30-second video generation using pose control
  - *From: PsiClone*

- **Comprehensive LTX-2 workflow collection**
  - Use case: Handles I2V, first to last frame, T2V with memory management nodes and distilled settings
  - *From: Phr00t*

- **LTX-2 infinite video generation**
  - Use case: Creating arbitrarily long videos with audio bridging
  - *From: ZombieMatrix*

- **Two-stage upscaling with guides**
  - Use case: First pass at 720p, then upscale with cropped guides for better quality
  - *From: neofuturo*

- **Temporal inpainting for video extension**
  - Use case: Extending videos by inpainting specific time segments
  - *From: ▲*

- **Face preservation for I2V**
  - Use case: Takes image after LTXVPreprocess, masks faces, applies original face over to prevent noise corruption while allowing motion in rest of image
  - *From: phazei*

- **Two-stage upscaling with guides**
  - Use case: First pass at lower resolution, second pass uses high-res guides instead of video inplace node for better results
  - *From: Elvaxorn*

- **Audio + spatial masking combination**
  - Use case: Creates audio for silent video while inpainting specific image areas throughout video duration
  - *From: MOV*

- **First frame to last frame (FFLF) setup**
  - Use case: Control start and end points of video generation for more directed movement
  - *From: Phr00t*

- **Image enhancement between passes**
  - Use case: VAE decode first pass, enhance image, encode for second pass to add detail
  - *From: David Snow*

- **Batch manager for upscaling**
  - Use case: Drop batch to 41 frames or lower to avoid OOM during upscaling
  - *From: VRGameDevGirl84(RTX 5090)*

- **David Snow's upscaling workflow with chunking**
  - Use case: High quality upscaling with memory management using chunking nodes
  - *From: ErosDiffusion*

- **First frame padding technique**
  - Use case: Fixing first/last frame artifacts by padding with duplicate frames then trimming
  - *From: N0NSens*

- **WAN refinement pass after LTX2**
  - Use case: Using WAN as a refinement step after LTX2 generation for better quality
  - *From: protector131090*

- **Multi-segment video generation with custom audio**
  - Use case: Creating longer videos by running multiple 10-second passes with different start times and images
  - *From: VRGameDevGirl84(RTX 5090)*

- **Frame interpolation using I2V with guide frames**
  - Use case: Improving motion quality by using guide frames spaced 12 frames apart
  - *From: Kijai*

- **Two-pass generation for quality improvement**
  - Use case: First pass at lower settings, second pass with temporal upscaler to improve motion and audio quality
  - *From: Kijai*

- **Automated music video generation**
  - Use case: Full music video creation using whisper for vocal extraction, ChatGPT for story/prompts, LLM nodes for enhancement
  - *From: VRGameDevGirl84(RTX 5090)*

- **Audio-reactive chunk generation**
  - Use case: Create different durations for each video chunk based on audio analysis automatically
  - *From: VRGameDevGirl84(RTX 5090)*

- **Context window extensions**
  - Use case: Extending video length using overlapping frames, 17 frames overlap for seamless continuation
  - *From: Kijai*

- **Two-pass upscaling with audio extraction**
  - Use case: Remove voice from music track then boost for LTX use
  - *From: David Snow*

- **First frame/last frame setup**
  - Use case: Guide video generation with specific start and end frames
  - *From: veldrin*

- **Audio-driven lipsync with TTS**
  - Use case: Generate lip sync by piping TTS audio into audio latent with mask set to 0
  - *From: hablaba*

- **Automated pipeline with Gemini, Qwen3VL-8B, Z-Image and LTX-2**
  - Use case: Fully automated video generation with some lipsync and consistency issues
  - *From: burgstall*

- **WAN2.1 detailer pass for fixing garbled details**
  - Use case: Light pass to fix details without changing likeness or audio sync, works on 95% complete videos
  - *From: Ablejones*

- **Two-stage sampling with resolution scaling**
  - Use case: First stage downscales latent to half, second stage upscales 2x back to full resolution for better motion
  - *From: Elvaxorn*

- **Automated music video workflow**
  - Use case: Gemini+QwenVL+Z-image+LTX-2 for fully automated music video generation
  - *From: burgstall*

- **LTX to Wan upscaling workflow**
  - Use case: Upscaling LTX video to Wan to clean up artifacts, does really nice job
  - *From: dj47*

- **Two-stage sampler for spatial/temporal upscale**
  - Use case: Second sampler stage usually for spatial or temporal upscale, can reach 2560 x 1408 on 5090
  - *From: drbaph*

- **Automated music video generation with LLM-driven prompts**
  - Use case: Creates 16 clips of 10 seconds each automatically using whisper for lyrics extraction and LLM for scene generation based on lyrics and themes
  - *From: VRGameDevGirl84*

- **Timeline editor for video project management**
  - Use case: GUI-based timeline editor that allows adjusting scenes, loading files, handling cuts, and outputting timestamps and prompts for batch rendering
  - *From: ErosDiffusion*

- **Multi-keyframe video stitching**
  - Use case: New template in Browse Templates for stitching multiple video segments together seamlessly
  - *From: el marzocco*

- **Image2reverb for spatial audio processing**
  - Use case: Feed image to generate reverb impulse response for the space, batch process film audio overnight to match reverb space per shot
  - *From: mdkb*

- **3-stage upscaling**
  - Use case: 320x320 -> 640x640 -> 1280x1280 for very long videos
  - *From: Kijai*

- **Video extension with audio masking**
  - Use case: Extending videos while maintaining lip sync and character likeness
  - *From: Nekodificador*

- **Audio-to-video with sound effects**
  - Use case: Adding sound effects to existing video by masking video latent
  - *From: Kijai*

- **Two-stage generation with different LoRAs per stage**
  - Use case: First stage with one LoRA set, second stage upscale with different LoRA
  - *From: Mazrael.Shib*

- **Audio-reactive video generation**
  - Use case: Using audio stems (drums, bass) to drive video reactions, though results vary
  - *From: David Snow*

- **Long-form video generation up to 1000 frames**
  - Use case: Using optimized memory patches for extended video lengths
  - *From: Kijai*

- **IC Detailer lora workflow using whole video as guide**
  - Use case: Video detailing similar to tile controlnet
  - *From: Kijai*

- **Trimming last frames from animation using native nodes**
  - Use case: Post-processing video output
  - *From: Kijai*

- **Audio-reactive particle emission with LTX-2**
  - Use case: Creating particle effects that respond to audio using taichi-based nodes
  - *From: burgstall*

- **Two-pass upscaling with LoRA**
  - Use case: Upscale first pass output and run through second step with LoRA for better results
  - *From: scf*

- **Audio + image to video with custom audio input**
  - Use case: Creating lip synced speech videos from custom image with custom audio track
  - *From: Kijai*

- **LTX 720p/1080p video upscaled with Wan**
  - Use case: Processing LTX videos with Wan upscaling for better quality
  - *From: Juan Gea*

- **High quality video generation workflow**
  - Use case: Creates very high quality i2v videos, to be shared later
  - *From: David Snow*

- **2-stage workflow for long videos**
  - Use case: Very long generations - first low res long gen, then upscale
  - *From: Kijai*

- **Image+audio to video workflow**
  - Use case: Creating lip-sync videos up to 30 seconds, works with spoken English
  - *From: FryingMan*

- **LTX2 detailing workflow using detail IC lora**
  - Use case: Improving detail in generated videos
  - *From: Kijai*

- **Using distilled model with negative lora for first pass**
  - Use case: More coherent first pass results than dev model alone
  - *From: garbus*

- **Clean I2V workflow**
  - Use case: Up-to-date image-to-video generation workflow
  - *From: David Snow*

- **Extend sampler + looping sampler chain**
  - Use case: For video generation without audio, can chain 5 with no problem
  - *From: ErosDiffusion*


## Recommended Settings

- **CFG**: 1
  - Should be 1 for distilled model, user had CFG 6 causing issues
  - *From: Jonathan Scott Schneberg*

- **LTX preprocess steps**: 33
  - Standard value that works for most users
  - *From: Mazrael.Shib*

- **Image strength for static image fix**: 0.5
  - Lower values help achieve movement when getting still images
  - *From: triquichoque*

- **VideoInPlace strength**: 1.0
  - Helps maintain character consistency in I2V
  - *From: ucren*

- **Preprocess steps for face preservation**: 22-27 or off
  - Lower values or disabling can help prevent face drift
  - *From: ucren*

- **CFG**: 4
  - Best prompt adherence and quality for distilled fp8 model
  - *From: nacho.money*

- **Steps**: 40
  - Optimal for distilled fp8 I2V workflow
  - *From: nacho.money*

- **FPS**: 24
  - Best results for distilled fp8 model
  - *From: nacho.money*

- **Frames**: 241
  - Optimal frame count for distilled fp8 workflow
  - *From: nacho.money*

- **Normalization ratios**: 1,1,0.4,1,1,0.4,1,1
  - Better normalized audio output
  - *From: Kijai*

- **Scheduled CFG**: start 0, end 0.3
  - Improves sound quality with distilled model
  - *From: N0NSens*

- **Frame rate calculation**: For 5 sec video at 24fps = 120 frames (+1) so use 121 in length box
  - Proper frame count calculation
  - *From: ErosDiffusion*

- **Steps for distilled model**: 22 steps instead of default 20
  - Better quality results
  - *From: Mazrael.Shib*

- **CFG for distilled model**: 1.0
  - Distilled model uses CFG 1.0
  - *From: avataraim*

- **NAG node connection**: Up connection preferred
  - Better in case you decide to use some CFG later
  - *From: DawnII*

- **Denoising strength**: 0.25
  - For light denoising to refine LTX output with Wan
  - *From: Ablejones*

- **CFG**: 1
  - For distilled model usage
  - *From: Vardogr*

- **Tiled VAE decode**: 1 tile, 0 overlap
  - Best results for eliminating seams in dark backgrounds
  - *From: ucren*

- **First stage resolution**: 720p
  - Better quality than lower resolutions
  - *From: neofuturo*

- **CFG and steps for non-distilled**: CFG 4, 35 steps
  - Helps smooth animations compared to distilled model
  - *From: herpderpleton*

- **Inpainting mask strength**: 0.5
  - Solid masks cause artifacts, lower strength works better
  - *From: MOV*

- **Clamp values for inpainting**: 0.94 min & max
  - Best results for existing video inpainting
  - *From: Grimm1111*

- **FPS for mouth animation**: 48fps then downsample to 24fps
  - Helps with smearing issues and cleaner mouth movements
  - *From: Arts Bro*

- **Distilled LoRA strength**: 50%
  - Allows cutting steps to 7 while maintaining quality
  - *From: Arts Bro*

- **Resolution for fast motion**: 1080p minimum
  - Lower resolutions have issues with fast movements
  - *From: Arts Bro*

- **Steps for distilled model**: 8 steps
  - Distilled model works well with 8 steps instead of original 7
  - *From: Arts Bro*

- **Film grain strength**: 0.05
  - Default 0.5 is too high for image enhancement workflow
  - *From: David Snow*

- **Image blend node strength**: 0.5 by default
  - Controls strength of image enhancement effect between passes
  - *From: David Snow*

- **MultiGuide node images**: 1 for I2V
  - Set to 1 for simple image-to-video, bypass last frame processing
  - *From: Phr00t*

- **Camera LoRA strength**: 1.0
  - Dramatically reduces artifacts during camera movements
  - *From: protector131090*

- **Base FPS**: 48-60
  - Helps with motion quality and reduces blur/artifacts
  - *From: veldrin*

- **Initial resolution scaling**: 0.2x instead of 0.5x
  - Reduces VRAM usage for longer videos, though lower quality
  - *From: ErosDiffusion*

- **Training resolution for LoRAs**: 512
  - Used for anime LoRA training on 4090
  - *From: protector131090*

- **LoRA training learning rate**: 0.00001
  - Low learning rate used for style/person training
  - *From: protector131090*

- **Steps with distilled model**: 15 steps maximum
  - 15 steps is already too much for distill models
  - *From: Kijai*

- **Euler Simple steps for quality**: 30 steps
  - Reduces overcooked/glossy look compared to 15 steps
  - *From: LarpsAI*

- **Distill LoRA negative strength**: -0.2 to -0.4
  - Makes distilled model less overcooked/debakes it
  - *From: Elvaxorn*

- **Frame gap for interpolation**: 12 frames
  - Provides smooth motion, 9 frames can be stuttery
  - *From: Kijai*

- **Audio sample rate**: 44.1kHz
  - 48kHz causes issues in ComfyUI processing
  - *From: burgstall*

- **FPS preference**: 24 fps or 25 fps
  - 25 seemed better than 24 in tests, 30 and 44 were generally much better. Audio is effectively at 25fps
  - *From: TK_999*

- **Resolution for compatibility**: 896x512
  - Divisible by 64 instead of 32, avoids freezing issues seen with 848x480
  - *From: TK_999*

- **Mask compression for speech**: mask=0.7 compression=40
  - Helps when model struggles with lip sync, use detailed prompt about emotions and mouth movement
  - *From: N0NSens*

- **CFG scale with video normalization**: 1.0
  - At 1.0 CFG, video normalization does nothing as scales per step with 1 does nothing
  - *From: Kijai*

- **Audio compression for preprocessing**: Add more img_compression
  - May help fix still image issues by smoothing out grain
  - *From: veldrin*

- **Audio sample rate for input**: 44kHz
  - Model requires input to be 44kHz for proper audio processing
  - *From: Kijai*

- **Audio to video attention scale**: Leave at 1.0 for normal use
  - Values other than 1.0 are experimental and can break things, useful only for existing audio
  - *From: Kijai*

- **Distill LoRA strength**: -0.4 to -0.6
  - Removes overcooked/cartoonish look from distilled model
  - *From: David Snow*

- **CFG with distill LoRA**: 1
  - Required when using distill LoRA
  - *From: Abyss*

- **ICDetailer LoRA strength**: 0.2-0.4
  - Very low values to avoid conflicts, often unnecessary
  - *From: ucren*

- **LTXImgToVideoInPlace**: 0.4
  - Helps with audio-in frozen image issues
  - *From: mdkb*

- **Audio normalization**: -14LUFS
  - Improves lipsync quality
  - *From: mdkb*

- **FPS for better motion**: 28 instead of 25
  - Fixes motion issues with anime style
  - *From: crinklypaper*

- **Steps with distilled model**: 10-20 steps
  - Balance between quality and speed
  - *From: veldrin*

- **Normalizing sampler scale value**: Changed from 0.25
  - 0.25 seemed too aggressive
  - *From: Kijai*

- **Chunk feed forward chunks**: 2 chunks
  - With new attention tuner node, 2 chunks is enough
  - *From: Kijai*

- **Distilled LoRA strength**: -0.2
  - For negative LoRA setup comparison
  - *From: TK_999*

- **Context windows frames**: 97 or 81
  - To combat OOM issues with higher resolution
  - *From: Ablejones*

- **Detailer LoRA strength**: 0.15-0.25 first pass, ~0.4 second pass
  - Better realism compared to higher values like 0.55
  - *From: IceAero*

- **Distilled LoRA strength for fixing frozen frames**: -0.3
  - Negative value fixes frozen frame issues while maintaining quality
  - *From: mdkb*

- **First pass sampler settings**: euler (not _a), 30-40 steps, cfg 3.5-4
  - Better results than euler_a with fewer steps
  - *From: IceAero*

- **Second pass distilled LoRA**: 0.8-0.9 strength
  - Reduced strength works better for upscaling pass
  - *From: IceAero*

- **Audio attention tuner**: 2 for audio_scale and audio_to_video_scale
  - Improves music reactivity and expression
  - *From: Erhan*

- **ComfyUI launch parameters for stability**: --reserve-vram 2 --disable-pinned-memory
  - Prevents OOM issues and memory conflicts
  - *From: sawlike*

- **Resolution for long videos**: 320x320
  - Can go past 2k frames without breaking
  - *From: Kijai*

- **Frame limit before quality issues**: ~1000 frames
  - Things get sketchy when approaching 1000 frame mark
  - *From: David Snow*

- **Audio mask fade range**: 0.8 to 0.9
  - Very small range between not changing at all and keeping some original tune
  - *From: Kijai*

- **Memory usage factor**: 0.04 minimum with all patches
  - Default 0.077, can reduce for extreme VRAM optimization but adjust carefully
  - *From: Kijai*

- **Temporal overlap**: Higher values
  - Fixes brightness adjustment issues that occur every 5 seconds
  - *From: Arts Bro*

- **Audio scale in attention tuner**: Up to 20
  - For audio-reactive effects, though results may vary
  - *From: David Snow*

- **Chunk feedforward and memory patches**: 0 for audio generation
  - Should be set to zero when generating audio to avoid interference
  - *From: Kijai*

- **numpy version**: 1.26.4
  - Compatibility with numba and other dependencies
  - *From: Kijai*

- **numba version**: 0.63.1
  - Compatible with numpy 1.26.4
  - *From: Kijai*

- **torch version**: 2.11.0.dev20260111+cu130
  - Latest development version
  - *From: Kijai*

- **CFG**: 1
  - Recommended for dev model
  - *From: gordo*

- **normalization steps**: 8
  - Better quality than higher values that become too sharp and bright
  - *From: gordo*

- **memory usage factor**: 0.04-0.05
  - With all optimizations can use very low values
  - *From: Kijai*

- **Frame count for keyframe interpolation**: Use more than 81 frames, model can do 500+
  - Too few frames result in slideshow effect rather than smooth motion
  - *From: Kijai*

- **Keyframe spacing**: Spread keyframes further apart
  - Closer keyframes are less likely to work properly
  - *From: Kijai*

- **Image compression values**: Important to add motion
  - Depends on your images but usually important for proper motion
  - *From: Kijai*

- **Model Memory Usage Factor**: 0.077 (default), can be decreased with patches
  - Controls VRAM offloading, patches reduce memory use so factor can be lowered
  - *From: Kijai*

- **Sampler choice**: sa_solver
  - Produces good quality at nearly half the rendering time compared to res_2s
  - *From: ZombieMatrix*

- **Resolution**: 4K preferred
  - Only way to significantly reduce artifacts
  - *From: protector131090*

- **Denoise for Wan upscale**: 0.1 or 0.2
  - Works well with UltimateSD Upscaler for LTX videos
  - *From: Juan Gea*

- **Distilled lora strength**: 0.6
  - Works well with dev model even at 20 steps euler cfg1
  - *From: gordo*

- **Memory usage factor**: 0.077 (default for LTX2)
  - Default value, adjust from this baseline
  - *From: Kijai*

- **Linear quadratic scheduler shift**: 8.0
  - Replicates default distill scheduler
  - *From: Kijai*

- **Maximum frames at 1920x1088**: 89 frames (20k rule), 150 frames (35k limit)
  - Based on latent size calculations
  - *From: IceAero*

- **Minimum distilled lora strength**: 0.20
  - Below this value causes breaking
  - *From: Abyss*

- **Resolution for 16GB VRAM**: 1280x720
  - Should be manageable with 16GB VRAM and 128GB system RAM
  - *From: David Snow*


## Concepts Explained

- **Audio latent frame calculation**: Audio latents are fixed at 25 per second, so for 10 seconds of video you need 250 audio latents regardless of video frame rate
  - *From: Scruffy*

- **LTXVNormalizingSampler usage**: Only for first pass 8-step generation with distilled model, not for second stage upscaling
  - *From: harelcain*

- **Debaking distilled model**: Using distilled lora at -0.4 strength to reverse some distillation effects
  - *From: ucren*

- **Latent normalization**: Process that fixes overbaking and audio clipping issues by adjusting latent values during sampling
  - *From: Elvaxorn*

- **Joint model**: LTX Video 2 processes audio and video together, so changes to one affect the other
  - *From: Kijai*

- **Guide workflow**: Method using guide frames to control video generation with proper cropping between stages
  - *From: Simonj*

- **NAG (Negative Augmented Generation)**: Node that combines negative prompt with positive conditioning when CFG is 1, making negative prompts work with distilled models
  - *From: DawnII*

- **Chunking/Feed Forward Chunking**: Memory management technique that reduces VRAM spikes during generation
  - *From: Kijai*

- **Normalizing Sampler**: Sampler that handles packed latents and audio scaling in LTX-2
  - *From: Kijai*

- **NAG (Negative Augmented Generation)**: More targeted to content than negative prompts with CFG, works differently from traditional negative prompting
  - *From: Kijai*

- **Crop Guides**: Removes guide frames from latent after first pass to prevent duplication in second stage
  - *From: Kijai*

- **Context windows**: Allow extending video generation beyond trained frame limits like 81 frames
  - *From: Ablejones*

- **AddGuide node functionality**: Resizes image to get higher res guide for upscale pass, requires cropping and adding back
  - *From: Kijai*

- **Crop guides node purpose**: Removes guides from latents for upscale pass, making it normal v2v without controls
  - *From: Kijai*

- **LTX chunk feed forward**: Memory saving model patch that's about 10% slower but reduces VRAM usage
  - *From: Kijai*

- **Temporal masking**: Mask affects timestep embeds in addition to latent masking, different from traditional approaches
  - *From: Kijai*

- **Second image in workflow**: The second image slot is for the last frame, allowing 'first to last frame' generation
  - *From: Phr00t*

- **Blancmange effect**: A visual artifact described as making things look soft/wobbly, common in lower resolution outputs
  - *From: mdkb*

- **Normalizing sampler**: New sampler that helps improve quality when combined with LCM and fixed distilled sigma values
  - *From: Phr00t*

- **Temporal upscaling on empty latents**: Misconception - this just doubles input frame count, same as setting empty latent node to more frames
  - *From: Kijai*

- **res_2s samplers**: Subsampling samplers that do inbetween steps between sigmas, effectively doubling the step count
  - *From: Kijai*

- **Debake**: Refers to vid2vid detailer pass in workflows
  - *From: Kijai*

- **First/last frame issues**: Common problem where first and last frames are blurry or have consistency problems
  - *From: metaphysician*

- **Motion blur in LTX2**: Caused by latent space being tightly packed with 8 frames per latent vs 4 in other models
  - *From: Kijai*

- **Temporal upscaler proper usage**: Should be used after first pass to double frame rate, then sample with higher fps conditioning
  - *From: Kijai*

- **Audio FPS in LTX2**: Audio always processed at 25 latents per second regardless of video FPS
  - *From: harelcain*

- **Keyframe conditioning**: Uses positional encoding to tell model where keyframes should take effect, requires AddGuide and CropGuides nodes
  - *From: Kijai*

- **Latent frame representation confusion**: A latent can represent a single or 8 pixel frames, causing philosophical confusion. You can cut latents from frame 5 onwards then VAE decode to reinterpret 8-frame latent as 1 pixel frame
  - *From: harelcain*

- **Pixel index in keyframe conditioning**: AddGuide devotes additional latents whose pixel index is correctly set for the keyframe index, unlike masking approach
  - *From: harelcain*

- **First vs last frame conditioning strength**: Last frame conditioning will never be as strong or exact as first frame conditioning due to latent structure design
  - *From: harelcain*

- **Video normalization with CFG 1.0**: Scales are applied per step, so scaling with 1 does nothing. Could be useful with patterns like 2,2,1,1,1,1,1,1
  - *From: Kijai*

- **Documentary still image assumption**: LTX2 assumes grainy images are stills from documentaries (common in dataset) and treats them as static
  - *From: Vardogr*

- **Audio latent masking**: Set audio mask to 0 for audio-driven generation, 1 for continuation after initial silence
  - *From: hablaba*

- **Guide keyframes**: Frames used to guide generation that need to be removed before decoding, work after all real frames
  - *From: Gleb Tretyak*

- **Audio to video attention**: How strongly audio influences video generation, can be boosted for existing audio but hurts generated audio quality
  - *From: Kijai*

- **Debaking**: Process of removing the overcooked/cartoonish look from distilled models using negative LoRA values
  - *From: David Snow*

- **Conditioning FPS**: Frame rate parameter that affects motion detail quality, separate from overall workflow FPS
  - *From: ucren*

- **NAG (Normalized Attention Guidance)**: Nothing to do with audio, means normalized attention guidance
  - *From: Kijai*

- **IMG2VideoInPlace**: Behaves like img2img, replaces the first latent
  - *From: Nekodificador*

- **AddGuides**: More like a tile controlnet where you add pose, depth, etc.
  - *From: Juan Gea*

- **LTXVPreprocess img_compression**: Adds noise, prepping the image for latent space
  - *From: Kijai*

- **Latent masking vs pixel masking**: ComfyUI processes mask from normal frames to latent frames with trilinear interpolation, causing smudging between frames
  - *From: Ablejones*

- **Audio attention scaling**: Since LTX2 is a joint model, video and audio affect each other through attention. Adjusting attention values controls how much they influence each other
  - *From: Kijai*

- **Denoising strength as reference control**: For LTX2 model, denoising strength 0.5-1.0 determines if starting frame is actual starting frame (1.0) or just reference frame (0.5)
  - *From: ZombieMatrix*

- **Virtual links in workflows**: Using get/set nodes to connect workflow elements without visible noodle connections, makes workflows cleaner and more organized
  - *From: David Snow*

- **Detailer LoRA usage**: IC-lora meant to be used like other ic-loras with guides, not just plugged in. Need to give low quality video as guides
  - *From: Kijai*

- **Audio masking nodes**: Work in seconds instead of frames because audio and video latents are different, helps keep them in sync
  - *From: Kijai*

- **Frobenius norm**: Tells you what percentage of original matrix's information is retained after keeping top k singular values, useful for LoRA rank reduction
  - *From: Kijai*

- **Sage++**: Updated version of SageAttention with slightly better performance (2-5% faster) but requires newer versions
  - *From: Kijai*

- **Memory usage factor**: Controls VRAM allocation efficiency, lower values save more VRAM but may affect performance
  - *From: Kijai*

- **Temporal overlap**: VAE setting that controls how video segments blend together, affects temporal consistency
  - *From: Arts Bro*

- **IC Detailer lora**: Should be used like tile controlnet with whole video as guide, not in normal generations
  - *From: Kijai*

- **Memory usage factor**: Controls how much is offloaded, scales with different input sizes
  - *From: Kijai*

- **Normalization functions**: Only part of original VAE used in tiny VAE, no actual decoding
  - *From: Kijai*

- **Keyframe indexes**: Frame_idx values represent the new frames where you want those images to appear in the sequence
  - *From: Kijai*

- **Timestep masking**: I2V (image to video) increases memory usage factor because of timestep masking or any mask use
  - *From: Kijai*

- **Keyframes in LTX2**: Act as literal guides for the model, not strict requirements
  - *From: mdkb*

- **FFN chunking**: Has nothing to do with anything but memory use, doesn't affect generation capability for longer videos
  - *From: Kijai*

- **Split sampling vs two passes**: Split sampling doesn't work with LTX2 due to joint video/audio tensor handling, so all workflows use two passes
  - *From: Kijai*

- **20k rule**: Latent size matters - if you increase resolution, you must decrease frames. 20k is safe limit, can go up to ~35k
  - *From: IceAero*

- **FFN chunk**: Can change output depending on model/GPU, affects memory usage
  - *From: Kijai*

- **NAG node inplace application**: Optional feature - disabled gives same output as before, enabled uses less memory but changes output
  - *From: Kijai*


## Resources & Links

- **LTX-2-19b-LoRA-Camera-Control-Static** (lora)
  - https://huggingface.co/Lightricks/LTX-2-19b-LoRA-Camera-Control-Static
  - *From: nikolatesla20*

- **42 Camera Movements AI Prompts** (resource)
  - https://aishotstudio.com/42-camera-movements-ai-prompts
  - *From: mdkb*

- **Reddit workflow** (workflow)
  - https://drive.google.com/file/d/1VYrKf7jq52BIi43mZpsP8QCypr9oHtCO/view
  - *From: dj47*

- **TinySR audio upscaling** (model)
  - https://huggingface.co/MihaiPopa-1/TinySR
  - *From: yi*

- **FlashSR audio upscaling** (model)
  - https://huggingface.co/YatharthS/FlashSR
  - *From: yi*

- **NovaSR audio upscaling** (model)
  - https://huggingface.co/YatharthS/NovaSR
  - *From: yi*

- **4-bit Gemma text encoder** (model)
  - https://huggingface.co/Comfy-Org/ltx-2/tree/main/split_files/text_encoders
  - *From: zelgo_*

- **First/Last frame I2V workflow** (workflow)
  - https://discord.com/channels/1076117621407223829/1309520535012638740/1461527849944092805
  - *From: Gleb Tretyak*

- **LTX-2 Documentation Bot** (tool)
  - https://notebooklm.google.com/notebook/4f07f98c-75b6-4278-bde1-906f9899b60c
  - *From: The Shadow (NYC)*

- **ComfyUI LTX-2 VRAM Memory Management** (repo)
  - https://github.com/RandomInternetPreson/ComfyUI_LTX-2_VRAM_Memory_Management
  - *From: zelgo_*

- **AudioSR for LTX-2 audio improvement** (workflow)
  - https://www.reddit.com/r/StableDiffusion/comments/1qeh156/psa_you_can_use_audiosr_to_improve_the_quality_of/
  - *From: veldrin*

- **Training Custom LoRAs with LTX-2 Tutorial** (tutorial)
  - https://www.youtube.com/watch?v=sL-T6dsO0v4
  - *From: LTX Lux*

- **LTX-2 Rapid Merges Workflow Collection** (workflow)
  - https://huggingface.co/Phr00t/LTX2-Rapid-Merges/tree/main
  - *From: Phr00t*

- **Kijai's LTX-2 Split Models** (model)
  - https://huggingface.co/Kijai/LTXV2_comfy/tree/main
  - *From: Kijai*

- **ComfyOrg FP8 Text Encoders** (model)
  - https://huggingface.co/Comfy-Org/ltx-2/tree/main/split_files/text_encoders
  - *From: Kijai*

- **DAC-SE1 for speech cleanup** (model)
  - https://huggingface.co/disco-eth/DAC-SE1
  - *From: DawnII*

- **LTX 2 TAE** (model)
  - https://github.com/madebyollin/taehv/tree/main/safetensors
  - *From: yi*

- **LTX2-Infinity workflow** (workflow)
  - https://github.com/Z-L-D/LTX2-Infinity
  - *From: ZombieMatrix*

- **Antrobots ComfyUI nodepack** (repo)
  - https://github.com/antrobot1234/antrobots-comfyUI-nodepack
  - *From: ZombieMatrix*

- **ComfyUI Music Tools** (tool)
  - https://github.com/jeankassio/ComfyUI_MusicTools/blob/main/images/example.png
  - *From: Wicked069*

- **ComfyUI pull request for tiny VAE** (repo)
  - https://github.com/Comfy-Org/ComfyUI/pull/11929
  - *From: Kijai*

- **Kijai's inpainting fix** (repo)
  - https://github.com/kijai/ComfyUI/commit/9c76f1076c5e80051af8544d330e9bf8a937e577
  - *From: Kijai*

- **taeltx_2.safetensors VAE model** (model)
  - https://github.com/madebyollin/taehv/tree/main/safetensors
  - *From: Kijai*

- **LTX 2.5 development discussion** (news)
  - https://www.reddit.com/r/StableDiffusion/comments/1qdug07/ltx2_updates/
  - *From: ˗ˏˋ⚡ˎˊ-*

- **1920x960 i2v workflow** (workflow)
  - https://www.reddit.com/r/StableDiffusion/comments/1qae922/ltx2_i2v_isnt_perfect_but_its_still_awesome_my/
  - *From: dj47*

- **Phr00t's LTX2 all-in-one workflow v2** (workflow)
  - https://huggingface.co/Phr00t/LTX2-Rapid-Merges/blob/main/LTXV-DoEverything-v2.json
  - *From: Phr00t*

- **Official LTX team workflows** (workflow)
  - https://github.com/Lightricks/ComfyUI-LTXVideo/tree/master/example_workflows
  - *From: Xor*

- **Neat Video** (tool)
  - https://www.neatvideo.com/examples#car
  - *From: hudson223*

- **Temporal Time Dilation technique** (technique)
  - https://www.reddit.com/r/StableDiffusion/comments/1qg0tnw/i_used_temporal_time_dilation_to_generate_this/
  - *From: cocktailprawn1212*

- **Scooby Doo style LoRA for LTX2** (model)
  - https://civitai.com/models/2308294/scooby-doo-style-lora-ltx2?modelVersionId=2597100
  - *From: dj47*

- **AI-toolkit training tutorial** (tutorial)
  - https://youtu.be/po2SpJtPdLs?t=2435
  - *From: David Snow*

- **RES4LYF node pack** (nodes)
  - not provided
  - *From: Nekodificador*

- **ComfyUI_essentials for math nodes** (nodes)
  - https://github.com/cubiq/ComfyUI_essentials
  - *From: David Snow*

- **Yunokusnir workflow** (workflow)
  - https://drive.google.com/file/d/1VYrKf7jq52BIi43mZpsP8QCypr9oHtCO/view?usp=sharing
  - *From: Danial*

- **LTX prompting guide** (guide)
  - https://ltx.io/model/model-blog/prompting-guide-for-ltx-2
  - *From: garbus*

- **VRAM Memory Management nodes** (repo)
  - https://github.com/RandomInternetPreson/ComfyUI_LTX-2_VRAM_Memory_Management
  - *From: LarpsAI*

- **ComfyUI PR for TAE LTX2 previews** (repo)
  - https://github.com/Comfy-Org/ComfyUI/pull/11929
  - *From: Kijai*

- **LTXV-DoEverythingV2 workflow** (workflow)
  - *From: metaphysician*

- **Yoshiaki Kawajiri LTX2 Retro anime lora** (lora)
  - https://civitai.com/models/2320379?modelVersionId=2610425
  - *From: tarn59*

- **Hugging Face mirror of Yoshiaki Kawajiri lora** (lora)
  - https://huggingface.co/tarn59/Yoshiaki_Kawajiri_Retro_Anime_LTX2
  - *From: tarn59*

- **LTX-2 Camera Control Static LoRA** (lora)
  - https://huggingface.co/Lightricks/LTX-2-19b-LoRA-Camera-Control-Static/tree/main
  - *From: Wicked069*

- **Fal AI LTX2 Video Trainer** (training service)
  - https://fal.ai/models/fal-ai/ltx2-video-trainer
  - *From: LarpsAI*

- **VoxCP audio processing workflow** (workflow)
  - https://www.youtube.com/watch?v=AqyyLY_ajTQ
  - *From: David Snow*

- **LTX-2 Chattable KB** (tool)
  - https://notebooklm.google.com/notebook/4f07f98c-75b6-4278-bde1-906f9899b60c
  - *From: Nathan Shipley*

- **Phr00t's first/last frame workflows** (workflow)
  - https://huggingface.co/Phr00t/LTX2-Rapid-Merges/tree/main
  - *From: veldrin*

- **Benji's LTX2 workflow** (workflow)
  - https://youtu.be/k52Hilha11s
  - *From: David Snow*

- **Ultimate Vocal Remover GUI** (tool)
  - https://github.com/Anjok07/ultimatevocalremovergui
  - *From: Gonzo*

- **Audio separation quality checker** (tool)
  - https://mvsep.com/quality_checker/synth_leaderboard
  - *From: Gonzo*

- **MiMo Audio for voice conversion** (tool)
  - https://github.com/XiaomiMiMo/MiMo-Audio
  - *From: Gleb Tretyak*

- **Smaller distill LoRA versions** (model)
  - https://huggingface.co/Kijai/LTXV2_comfy/tree/main/loras
  - *From: Kijai*

- **Original large distill LoRA** (model)
  - https://huggingface.co/Lightricks/LTX-2/blob/main/ltx-2-19b-distilled-lora-384.safetensors
  - *From: Danial*

- **Smaller Gemma model** (model)
  - https://huggingface.co/unsloth/gemma-3-12b-it-qat-bnb-4bit
  - *From: Zueuk*

- **Benji's lipsync workflow** (workflow)
  - https://www.youtube.com/watch?v=AqyyLY_ajTQ&t=2s
  - *From: Mazrael.Shib*

- **WHATUSEE LoRA** (lora)
  - https://discord.com/channels/1076117621407223829/1463103343055605964
  - *From: burgstall*

- **Automated music video output** (workflow)
  - https://www.youtube.com/watch?v=gJ7QkkmozJ0
  - *From: burgstall*

- **WanVaceAdvanced mask processing code** (repo)
  - https://github.com/drozbay/ComfyUI-WanVaceAdvanced/blob/b6f5b2263f04f41ba84183b1735cc738d34ca95c/nodes/vace_custom_nodes.py#L982
  - *From: Ablejones*

- **HQ example video** (workflow)
  - https://app.filen.io/#/f/bcb3369c-8062-4dff-a891-c2cfdf110ff8%23kSKhRtRmieVpbL4930dF1yIXRfbfldnd
  - *From: Arts Bro*

- **Reduced size distilled LoRA** (model)
  - https://huggingface.co/Kijai/LTXV2_comfy/tree/main/loras
  - *From: Kijai*

- **Yoshiaki Kawajiri Retro Anime LoRA for LTX2** (lora)
  - https://huggingface.co/tarn59/Yoshiaki_Kawajiri_Retro_Anime_LTX2/tree/main
  - *From: David Snow*

- **Image2reverb for spatial audio** (tool)
  - https://github.com/mdkberry/image2reverb
  - *From: mdkb*

- **Whisper timestamped for word-level timestamps** (tool)
  - https://github.com/linto-ai/whisper-timestamped
  - *From: ZombieMatrix*

- **Timeline editor node (pre-alpha)** (node)
  - https://github.com/erosDiffusion/ComfyUI-Erosdiffusion-LTX2/tree/master
  - *From: ErosDiffusion*

- **LTX2 prompting guide** (guide)
  - https://ltx.io/model/model-blog/prompting-guide-for-ltx-2
  - *From: Alpha-Neo*

- **Unsloth gemma3 12b GGUF** (model)
  - https://huggingface.co/unsloth/gemma-3-12b-it-GGUF/tree/main
  - *From: Kijai*

- **ComfyUI StarNodes converter** (tool)
  - https://github.com/Starnodes2024/ComfyUI_StarNodes
  - *From: cocktailprawn1212*

- **LTX2 memory management fork** (repo)
  - https://github.com/RandomInternetPreson/ComfyUI_LTX-2_VRAM_Memory_Management
  - *From: protector131090*

- **LTX inpainting fixes branch** (repo)
  - https://github.com/kijai/ComfyUI/tree/ltx2_memory
  - *From: ucren*

- **Split VAE files by Kijai** (model)
  - https://huggingface.co/Kijai/LTXV2_comfy/tree/main/diffusion_models
  - *From: TK_999*

- **Official LTX-2 models** (model)
  - https://huggingface.co/Lightricks/LTX-2/tree/main
  - *From: TK_999*

- **Problematic lip sync workflow** (workflow)
  - https://discord.com/channels/1076117621407223829/1309520535012638740/1462695447335534602
  - *From: David Snow*

- **VRGameDevGirl84 automation workflow** (workflow)
  - https://discord.com/channels/1076117621407223829/1463747305802043423
  - *From: VRGameDevGirl84*

- **taeltx_2.safetensors** (model)
  - https://github.com/madebyollin/taehv/blob/main/safetensors/taeltx_2.safetensors
  - *From: Kijai*

- **SageAttention releases** (tool)
  - https://github.com/woct0rdho/SageAttention/releases
  - *From: Kijai*

- **Triton Windows** (tool)
  - https://github.com/woct0rdho/triton-windows
  - *From: Kijai*

- **ComfyUI PR 12028** (repo)
  - https://github.com/Comfy-Org/ComfyUI/pull/12028
  - *From: Kijai*

- **Qwen3-TTS** (model)
  - https://github.com/QwenLM/Qwen3-TTS
  - *From: Gill Bastar*

- **MelBandRoFormer commit fix** (repo)
  - https://github.com/kijai/ComfyUI-MelBandRoFormer/commit/260cb03c4da37aaf20ef3ab5ad5805e1e0eafd38
  - *From: Kijai*

- **Custom allocator PR** (repo)
  - https://github.com/Comfy-Org/ComfyUI/pull/11845
  - *From: Kijai*

- **Ryan's audio-reactive nodes** (repo)
  - https://github.com/ryanontheinside/ComfyUI_RyanOnTheInside
  - *From: Cseti*

- **LTX2-Infinity extension workflow** (repo)
  - https://github.com/Z-L-D/LTX2-Infinity
  - *From: Xor*

- **UltraShape1 3D mesh refiner** (repo)
  - https://github.com/jtydhr88/ComfyUI-UltraShape1
  - *From: Nekodificador*

- **Improved UltraShape1 with comfy_env** (repo)
  - https://github.com/PozzettiAndrea/ComfyUI-UltraShape1/tree/dev
  - *From: Vardogr*

- **Flash attention prebuilt wheel** (tool)
  - https://github.com/mjun0812/flash-attention-prebuild-wheels/releases/download/v0.7.12/flash_attn-2.8.3+cu130torch2.10-cp312-cp312-win_amd64.whl
  - *From: veldrin*

- **Vid2vid workflow from Benji's AI Playground** (workflow)
  - *From: AIGambino*

- **Prompt examples and techniques** (workflow)
  - https://discord.com/channels/1076117621407223829/1459223128139104436
  - *From: The Shadow (NYC)*

- **Phr00t's FFLF workflow** (workflow)
  - https://discord.com/channels/1076117621407223829/1309520535012638740/1463393616708898949
  - *From: mdkb*

- **4D Gaussian Splats for AI videos** (tool)
  - https://www.youtube.com/watch?v=v-U8QnyknY8
  - *From: dj47*

- **VRAM Memory Management extension** (tool)
  - https://github.com/RandomInternetPreson/ComfyUI_LTX-2_VRAM_Memory_Management
  - *From: cocktailprawn1212*

- **Sam Shark sampler explanation** (tutorial)
  - https://youtu.be/A6CXfW4XaKs
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Video upscaling tool** (tool)
  - https://www.youtube.com/watch?v=IyLNMu6mjvc
  - *From: David Snow*

- **Gemma 3 12B 4-bit quantized model** (model)
  - https://huggingface.co/unsloth/gemma-3-12b-it-qat-bnb-4bit
  - *From: Zueuk*

- **ComfyUI memory optimization PR** (repo)
  - https://github.com/Comfy-Org/ComfyUI/pull/12046
  - *From: Kijai*

- **Dynamic memory management PR** (repo)
  - https://github.com/Comfy-Org/ComfyUI/pull/11845
  - *From: Kijai*

- **GGUF 12GB workflows for LTX2** (workflow)
  - https://civitai.com/models/2304098?modelVersionId=2623604
  - *From: U̷r̷a̷b̷e̷w̷e̷*

- **Abliterated Gemma model** (model)
  - https://huggingface.co/FusionCow/Gemma-3-12b-Abliterated-LTX2/blob/main/gemma_ablit_fixed_bf16.safetensors
  - *From: David Snow*

- **LTX-2 I2V workflow** (workflow)
  - https://github.com/Lightricks/ComfyUI-LTXVideo/blob/master/example_workflows/LTX-2_I2V_Full_wLora.json
  - *From: The Shadow (NYC)*

- **RES4LYF** (repo)
  - https://github.com/ClownsharkBatwing/RES4LYF
  - *From: David Snow*


## Known Limitations

- **LTXVNormalizingSampler breaks with audio masking**
  - Causes severe audio noise/artifacts when used with masking nodes due to normalization affecting preserved audio segments
  - *From: Xor*

- **I2V without audio produces static images**
  - Many users experience still image output when doing image-to-video without audio input
  - *From: Mazrael.Shib*

- **Face drift in I2V generations**
  - Model tends to change facial features from input image during video generation
  - *From: NebSH*

- **LTX2 struggles with faces at distance**
  - Quality degrades significantly when faces are not in close-up
  - *From: nikolatesla20*

- **Context window issues around 8 seconds**
  - Background shifts and quality degradation occurring around 8 second mark in longer generations
  - *From: Drommer-Kille*

- **Preview quality is low resolution**
  - LTX Video 2 latents are highly compressed, resulting in rough preview quality
  - *From: Kijai*

- **Normalization breaks audio in some cases**
  - Can add lots of noise to audio that was already good quality
  - *From: Kijai*

- **Masks not fully supported**
  - Sampler doesn't account for masks properly, only works for audio but affects video
  - *From: Kijai*

- **Music added to most generations**
  - Normalization tends to make background music more audible in generations
  - *From: Kijai*

- **I2V character consistency issues**
  - Characters change appearance despite reinforcement prompts
  - *From: buggz*

- **Preview quality is low**
  - Current latent previews are very low quality, can only be improved with tiny VAE which is being worked on
  - *From: Kijai*

- **Audio normalization produces British accents**
  - With normalization on for audio, gets a lot of British accents for T2V, possibly due to Bollywood training data
  - *From: ucren*

- **I2V often produces static results without LoRAs**
  - Image-to-video generations frequently remain static with minimal movement unless camera LoRA is used
  - *From: Mazrael.Shib*

- **Model prone to breaking with contradictory prompts**
  - Very sensitive to inconsistencies between input image and prompt descriptions
  - *From: ErosDiffusion*

- **Voice in prompts affects visual generation**
  - When VO text has word 'moustache', LTX draws moustache on women
  - *From: Drommer-Kille*

- **FP4 model quality issues**
  - FP4 variants produce psychedelic artifacts and poor image quality
  - *From: jacinda*

- **Audio quality inconsistency**
  - Audio generation is hit or miss, often muddy even with normalization
  - *From: N0NSens*

- **Portrait aspect ratio issues**
  - Much more weirdness happens in portrait orientation
  - *From: scf*

- **Compression artifacts learned from training**
  - Model may have learned compression artifacts as important parts of video rather than artifacts
  - *From: Screeb*

- **Inplace keyframing doesn't work well with short distances**
  - Needs longer frame counts like 177 vs 121 frames between keyframes
  - *From: Kijai*

- **9:16 aspect ratio shows overlay text frequently**
  - Distilled model particularly prone to adding text overlays in vertical format
  - *From: Tyronesluck*

- **9:16 tends to be static**
  - Vertical format has tendency toward static content
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Lower resolutions struggle with fast motion**
  - Anything under 1080p has issues with fast movements, causes smearing
  - *From: Arts Bro*

- **Temporal upscaling may hurt lip sync**
  - Frame interpolation can mess up mouth animation accuracy
  - *From: herpderpleton*

- **Inpainting not at VACE level quality**
  - Even with clamp of 1, still alters original video significantly
  - *From: Grimm1111*

- **Camera movement causes artifacts**
  - Any camera movement in LTX2 will result in motion artifacts that can't be easily fixed
  - *From: protector131090*

- **Juddery motion on certain seeds**
  - Some seeds produce very stuttery motion while others are fine, seems random
  - *From: David Snow*

- **First/last frame setup issues**
  - Video doesn't end with last frame, flickers between first and last frames at end
  - *From: metaphysician*

- **WAN better for 2D animation**
  - WAN destroys LTX for 2D animation content, LTX better for realistic content
  - *From: protector131090*

- **LTX2 struggles with 2D/anime content**
  - Artifacts are more prominent in 2D content compared to realistic content
  - *From: protector131090*

- **Style LoRA training ineffective**
  - After 20k steps over 4 days, style LoRA still not matching training data
  - *From: protector131090*

- **Frame count cap around 1000-1400**
  - Going past ~1400 frames results in NaNs and black output
  - *From: Kijai*

- **Long prompts cause issues**
  - Too long prompts cause model to ignore input image and go off-prompt
  - *From: Kijai*

- **First/last frame consistency problems**
  - Consistent issue with blurry first/last frames and clothing consistency
  - *From: metaphysician*

- **Spatial masks don't work well with movement**
  - Inpainting masks perform worse when there's head turns or motion, faces get glitchy
  - *From: Grimm1111*

- **Temporal upscaler misuse creates no effect**
  - Using temporal upscaler on empty latent before sampling does nothing - it's mathematically identical to doubling frame count
  - *From: Ablejones*

- **Motion blur artifacts from architecture**
  - Motion blur is likely unfixable due to model's tightly packed latent space design
  - *From: nikolatesla20*

- **Split sampling not working with LTX-2**
  - Current implementation incompatible with split sampling due to noise scale function issues
  - *From: Ablejones*

- **Identity loss in extension workflows**
  - Multi-generation extension loses character identity, needs injection method
  - *From: Kijai*

- **Audio drift in multi-segment generation**
  - Audio timing drifts by ~7 frames when combining multiple generation runs
  - *From: VRGameDevGirl84(RTX 5090)*

- **VAE smearing on last frames**
  - Well-known issue where VAE can smear the last pixel frames, not yet fixed
  - *From: harelcain*

- **Upper limit on video size**
  - Model has upper limit for AV tokens, 1024x832 497 frames caused noise output
  - *From: TK_999*

- **Audio/video sync issues**
  - When stitching video chunks, audio ends up 7 frames out of sync requiring manual adjustment
  - *From: VRGameDevGirl84(RTX 5090)*

- **Context windows don't work with audio**
  - Context window extensions currently don't work with audio latents
  - *From: Kijai*

- **Resolution-dependent lip sync failure**
  - Certain resolutions like 848x480 cause lip sync to freeze/not work properly
  - *From: mdkb*

- **Audio-driven lipsync resolution issues**
  - Many resolutions fail with audio file input - only 480x256 works reliably, higher resolutions cause frozen frames or ignore image input
  - *From: mdkb*

- **Lipsync harder with mixed humans and animals**
  - Model has difficulty with lip sync when people are mixed with animals in frame, can do each separately without problems
  - *From: N0NSens*

- **Person continues talking after audio ends**
  - Model doesn't handle blank audio at end well, person keeps lip movement even when audio stops
  - *From: hablaba*

- **Poor morphing between different objects**
  - Very bad at redrawing objects between frames when images are completely different, random results even with detailed prompts
  - *From: N0NSens*

- **Model struggles with piano playing accuracy**
  - Difficult to get accurate key presses and timing, may require LoRA training for proper piano playing
  - *From: veldrin*

- **Poor prompt adherence compared to other models**
  - Requires very specific and redundant prompting, less forgiving than Qwen edit or Flux
  - *From: MysteryShack*

- **Guide inputs are not predictable**
  - Guide inputs suggest to model at attention level but don't use trained mechanism, so results are unpredictable
  - *From: Ablejones*

- **Anime/cartoon quality issues**
  - Model lacks training on anime corpus, photorealistic works better, hands become blobs in animated content
  - *From: MysteryShack*

- **Face degradation in high motion**
  - Significant quality loss in faces and hands during walking or high motion scenes
  - *From: Ryzen*

- **Frame count affects content repetition**
  - Model repeats or stretches content to fit specified frame count
  - *From: Kijai*

- **Teeth details remain imperfect**
  - Teeth are slightly better but probably will never be 100% perfect
  - *From: Abyss*

- **Video inpainting less effective than image inpainting**
  - Harder to do changes on video though, seems more frameless it changes
  - *From: Kijai*

- **Masking timestep embeds spatially doesn't help**
  - Doesn't look like masking the timestep embeds spatially helps at all
  - *From: Kijai*

- **Latent inpainting with limited mask frames**
  - Latent inpainting when one mask can only be for 8 frames is gonna never be great
  - *From: Kijai*

- **Model performance caps at RTX 5090**
  - Length and resolution it can do is limited, not worth RTX PRO 6000 for LTX2 inference
  - *From: Kijai*

- **FPS above 30 causes issues with longer videos**
  - After 30fps things get corrupted, may be due to total frame count getting too high with 12+ second videos
  - *From: veldrin*

- **bf16 VAE incompatible with RTX 2080**
  - RTX 2080 doesn't support bf16, can't convert bf16 to fp16 without being lossy
  - *From: Kijai*

- **LTX2 poor performance with 2D/anime content**
  - Much worse with 2D content compared to WAN, produces too many artifacts
  - *From: protector131090*

- **Audio generation not as good with music vs speech**
  - LTX's audio is surprisingly decent at speech but not so good with music
  - *From: MysteryShack*

- **Normalizing sampler has minimum length requirements**
  - Normalizing sampler produces NaN errors for 1-2 second videos, may have minimum length requirement
  - *From: ErosDiffusion*

- **Model breaks at high resolution/length combinations**
  - 1280x1280 x 1001 frames produces artifacts, model has limits
  - *From: Kijai*

- **Spatial inpainting doesn't work**
  - Spatial inpainting functionality not working properly
  - *From: hablaba*

- **Hard cuts in masked video affect likeness**
  - Final frame of cut dictates likeness for rest of generation, hard cuts are problematic
  - *From: Nekodificador*

- **LoRA rank reduction quality loss**
  - Reducing LoRA rank loses quite a lot of quality, some LoRAs break even with half rank
  - *From: Kijai*

- **LTX2 dev model is very finicky**
  - Super finicky about steps, sampler, scheduler, resolution, and fps settings
  - *From: veldrin*

- **High portrait resolutions cause hallucinations**
  - Even at 720x1280 you'll start getting hallucinations, need to lower to 640x1088
  - *From: ucren*

- **Spatial inpainting doesn't work well**
  - Works on single image and short clips, but normal length videos never get proper changes
  - *From: Kijai*

- **LTX2 struggles with multiple people**
  - Has difficulty handling 3+ people in scenes, often ignores some subjects
  - *From: N0NSens*

- **Audio reactivity is inconsistent**
  - Despite high audio scale values, getting proper audio-reactive effects is unreliable
  - *From: David Snow*

- **Model can't do anything good at very high resolutions like 1000 frames**
  - Only works technically but quality is poor
  - *From: Kijai*

- **Can't convert VAE to fp8 meaningfully**
  - Would lose half precision to save only 1GB VRAM
  - *From: Kijai*

- **Hands seem overtrained - gloves randomly turn into bare hands**
  - Model bias issue with hand rendering
  - *From: Zueuk*

- **Tiny VAE always has bad quality**
  - Trade-off for smaller size and faster inference
  - *From: Kijai*

- **Model not great at morphing between very different images**
  - Works better with similar images for keyframe interpolation
  - *From: Kijai*

- **VAEs often fail on fp16**
  - Common issue causing artifacts when VAE is cast to fp16
  - *From: Kijai*

- **Tiled VAE decode adds seam noise**
  - Creates visible seams and is slower than non-tiled decode
  - *From: Kijai*

- **Custom allocator currently Nvidia only**
  - Hardware-specific implementation limits cross-platform support
  - *From: mallardgazellegoosewildcat2*

- **80 second videos mostly don't work regardless of memory**
  - Need very small resolution to go that far, combined input size of resolution and frame count is limiting factor
  - *From: Kijai*

- **Artifact issues similar to Wan 2.1**
  - Watery/flowing effects on detailed backgrounds during camera movement, not ready for production until fixed
  - *From: Juan Gea*

- **T2V produces poor results compared to I2V**
  - User found T2V results 'near disastrous' compared to I2V
  - *From: b̶̈́͠o̶̗̅n̶̽̒k̵̽̿*

- **Split sampling doesn't work with LTX2**
  - Code can't handle the joint video/audio tensor for split sampling
  - *From: Kijai*

- **FFN chunking can change output in some circumstances**
  - Reason FFN isn't chunked by default
  - *From: Kijai*

- **LTX2 doesn't understand sequence of events**
  - Sometimes does things out of order
  - *From: Zueuk*

- **Dev model produces very noisy, incoherent outputs alone**
  - Needs distilled lora for proper function, can't work well at high resolution without assistance
  - *From: Ablejones*

- **Quality suffers significantly with very long generations**
  - Need to reduce resolution to balance quality vs length
  - *From: Kijai*

- **LTX2 scheduler breaks very early at high resolutions**
  - Sends all sigmas to ceiling at higher resolutions
  - *From: Kijai*

- **Can't do time-based regional prompting**
  - Would need splitting the attention itself, no current code for this
  - *From: Kijai*

- **Abliterated Gemma models don't actually work**
  - Still shows 'this isn't safe and I'm not supposed to talk about this topic' messages
  - *From: nikolatesla20*

- **Character consistency issues in V2V**
  - Character shifts occur in video-to-video, even with LoRAs helping maintain consistency
  - *From: ErosDiffusion*

- **Inconsistent prompt following**
  - Often doesn't follow prompts, then suddenly follows perfectly, behavior seems random and not seed-based
  - *From: gordo*


## Hardware Requirements

- **RTX 3090 performance**
  - 1920x960 20 seconds takes 30 minutes to generate
  - *From: dj47*

- **RTX 2080 compatibility**
  - Only supports fp16, does not support bf16 weight dtype
  - *From: xwsswww*

- **VRAM optimization with chunked feedforward**
  - KJNodes chunked feedforward reduces peak VRAM significantly
  - *From: Kijai*

- **16GB VRAM for longer videos**
  - 5060 Ti with 16GB VRAM can handle 10-second videos, takes about 11 minutes with Sage
  - *From: Wicked069*

- **High RAM needed for VAE decode**
  - Long duration clips at high resolution will freeze PC during VAE decode without sufficient RAM
  - *From: Tachyon*

- **Consumer GPU compatibility**
  - Can run 10s of 1280x720 24fps video on RTX 3050 4GB VRAM using Q4_K_M GGUF, takes 15-20 minutes
  - *From: Xor*

- **RTX 3090 24GB VRAM requirements**
  - User reported OOM issues with 24GB VRAM + 32GB system RAM, needs optimization
  - *From: Ben Czegeny*

- **Compute capability for optimized operations**
  - Need GPUs with compute capability 8.9 for SM89 kernel, RTX 4090 reported this error
  - *From: sftawil*

- **VRAM for NAG**
  - NAG increases peak VRAM usage significantly when using chunked FFN
  - *From: Kijai*

- **RTX 3090 FP8/FP4 performance**
  - RTX 3090 cannot natively run FP8 or FP4 models, does conversion making generation slower
  - *From: dj47*

- **VAE decode memory**
  - 24GB VRAM still requires tiled decode at higher resolutions/lengths, auto-switches to tiled when needed
  - *From: ucren*

- **10 seconds 1280x720 i2v generation**
  - 16GB VRAM, 64GB RAM for first pass + 2x upscale without OOM
  - *From: Vérole*

- **fp8_e4m3fn_fast support**
  - Requires 40xx series GPU or higher for hardware fp8 matrix multiplication
  - *From: Kijai*

- **3090 1080p generation**
  - 64GB system RAM, can do 1920x960 i2v for 20 seconds with proper settings and --novram flag
  - *From: dj47*

- **4090 performance**
  - i2v 1920x1080 400 frames takes about 5 minutes
  - *From: David Snow*

- **5090 performance note**
  - User claimed 11 minutes for 5 seconds at 1024x576 which indicates configuration issues
  - *From: VRGameDevGirl84*

- **Sage attention benefits**
  - Only provides significant speed boost (2x+ faster) with large input dimensions like video models
  - *From: Kijai*

- **3060 RTX performance**
  - Can generate 10 seconds at 1408x768 24fps in 16 minutes, 241 frames at 704p 24fps in 15 minutes with GGUFs
  - *From: mdkb*

- **5090 performance**
  - 1024x576 5 second video in under 219 seconds with upscaling, 4 second 1920x1088 upscale in under 5 minutes
  - *From: VRGameDevGirl84(RTX 5090)*

- **4090 performance**
  - 1920x1056 upscale in 91 seconds using LTX video-to-video detailer
  - *From: David Snow*

- **VRAM usage comparison**
  - Full fat model 42GB vs fp8 version 26GB, GGUF models can push limits with lower VRAM
  - *From: David Snow*

- **LoRA training VRAM**
  - 24GB minimum for LTX2 LoRA training, 4 days training time on 4090 for 20k steps
  - *From: protector131090*

- **Long video generation**
  - 640x640x1400 frames possible on 4090 without breaking sweat using offloading
  - *From: Kijai*

- **Memory for 20 second videos**
  - 32GB RAM + 10GB VRAM sufficient for 20 seconds at 50fps with optimizations
  - *From: ErosDiffusion*

- **--reserve-vram flag**
  - May no longer be needed with recent ComfyUI updates and chunked FFN
  - *From: Kijai*

- **VRAM savings with feedforward node**
  - 1-2GB drop in peak VRAM at higher input sizes
  - *From: Kijai*

- **RTX 5090 generation speed**
  - 1024x576 10 seconds takes about 321 seconds, though user expected faster
  - *From: VRGameDevGirl84(RTX 5090)*

- **RTX 3090 performance comparison**
  - 720x1280 10 seconds in about 160s using LCM, 4s/it for 8 steps
  - *From: phazei*

- **High resolution/frame count limits**
  - Very high res and frame counts cause scheduler errors, need to lower max shift
  - *From: Kijai*

- **VRAM usage with NAG and chunk nodes**
  - Adding NAG increases overall VRAM use when using chunk ffn node, but updated KJNodes reduces this
  - *From: Kijai*

- **FP4 model performance**
  - FP4 model works on Apple Silicon, faster than v1 by several minutes
  - *From: buggz*

- **VRAM usage with audio processing**
  - Audio processing significantly increases VRAM usage, can cause OOM with resolutions that normally work fine
  - *From: David Snow*

- **System RAM requirements**
  - 32GB system RAM can OOM, use --cache-none and --disable-pinned-memory flags to help
  - *From: Ben Czegeny*

- **Peak VRAM reduction**
  - New attention patch lowered peak VRAM again by refactoring forward function
  - *From: Kijai*

- **CUDA version requirement**
  - Need pytorch with cu130 or higher for optimized CUDA operations, cu130 confirmed safe with 5090
  - *From: Kijai*

- ****
  - Even with high-end setup, 800 frames at upscaled resolution causes memory issues
  - *From: Gleb Tretyak*

- **Memory usage scales with resolution and frame count**
  - 1024x1024x121 frames with optimizations, 1024x1024x500 frames peaked at 14GB VRAM
  - *From: Kijai*

- **8GB VRAM can handle 720x1280 resolution**
  - Using Q4 GGUF distill model, 20 seconds takes 28 minutes
  - *From: army*

- **3060 with 32GB system RAM works with quantized models**
  - Using distilled Q4 KM model, had to disable pinned memory
  - *From: mdkb*

- **RTX 5090 performance**
  - Model pretty much caps on 5090 already, 365sec for FHD 169 frames, 13min if model loading issues
  - *From: burgstall*

- **VRAM optimization**
  - VRAM only goes up to 61% sampling an FHD 169 frames clip with new patches
  - *From: burgstall*

- **6GB VRAM reduction**
  - 6GB peak VRAM reduction tested with 1024x1024x497
  - *From: Kijai*

- **GPU compatibility for quantization**
  - FP8/FP4 support depends on GPU, wouldn't touch low quants unless absolutely necessary on unsupported GPUs
  - *From: Kijai*

- **VRAM for 50fps high resolution**
  - 16GB VRAM, 64GB system RAM needed to handle 350 frames at 50fps for 7 second videos
  - *From: N0NSens*

- **RTX 3060 12GB setup for complex workflows**
  - 3060 RTX 12GB VRAM, 32GB system RAM, static page file to SSD enables running 7.5GB LoRAs with GGUF models
  - *From: mdkb*

- **SageAttn memory optimization**
  - New SageAttn implementation reduces memory usage significantly, 704x704x121 activations only cost ~300MB
  - *From: Kijai*

- **Memory optimization benefits**
  - New memory optimizations include chunked FFN, refactored model forward function, custom Sage attention - must use ALL for benefit
  - *From: Kijai*

- **Generation speed by resolution**
  - 14 sec video takes 6min on 4090. Speed changes exponentially with resolution
  - *From: Janosch Simon*

- **VRAM usage for different resolutions**
  - 1280x1280 x 1001 frames fits in memory with optimizations
  - *From: Kijai*

- **4090 VRAM usage with optimizations**
  - Can do 1280x1280 for 1000 frames on 20GB VRAM with memory patches
  - *From: Kijai*

- **4090 needs 6-10GB reserved VRAM without optimizations**
  - Need to reserve at least 6GB to make it work, 10GB to run smoothly
  - *From: gordo*

- **5090 VRAM improvements**
  - VRAM usage dropped from 98% to 75% with optimization patches
  - *From: neofuturo*

- **Performance comparison**
  - 4080: 4.22s/it with sage, 5.51s/it with new memory efficient node
  - *From: N0NSens*

- **RTX 3090 limitations**
  - Cannot generate 4k with 121 frames even with chunk forwarding optimization
  - *From: dj47*

- **fp8 matmuls support**
  - Only 40xx series and newer GPUs have native fp8 support
  - *From: Kijai*

- **WSL performance issues**
  - WSL adds layer of problems and performance issues, not recommended
  - *From: Kijai*

- **512x512 3sec video should take couple seconds on 4090**
  - Expected performance benchmark
  - *From: Kijai*

- **Memory for FP16 40GB model**
  - Requires 100GB page file, 70GB page file causes ComfyUI disconnect
  - *From: hicho*

- **Windows 10 Pro RAM limitation**
  - Max 128GB on Windows 10 Pro vs 250GB possible on Linux
  - *From: NC17z*

- **RTX 4090 performance**
  - 121x704x704 takes 10-13 seconds depending on optimization settings
  - *From: Kijai*

- **Dependencies for optimal performance**
  - Need updated ComfyUI, KJNodes, sageattention, triton, pytorch, comfy-kitchen for 10-second performance
  - *From: Kijai*

- **RTX 6000 Pro 96GB pricing**
  - Cheapest seen around $7600, runs very hot (near/above 90°C)
  - *From: orabazes*

- **Long video memory needs**
  - With all patches, 1080p 2000 frames can be done with ~18GB VRAM
  - *From: Kijai*

- **8GB VRAM capability**
  - Can generate 14,341 frames at 1000x1000 with 32GB RAM using chunking
  - *From: cocktailprawn1212*

- **FP4 support**
  - RTX 2060 and RTX 3070 support FP4, seems only RTX 5xxx have native FP4 support
  - *From: army*

- **System RAM for long videos**
  - 75GB RAM spike during tiled VAE at 1500 frames 704x704
  - *From: FryingMan*

- **VRAM for long videos**
  - 1500 frames at 704x704 runs within 16GB VRAM without fatal OOM
  - *From: FryingMan*

- **Generation speed on RTX 5070ti**
  - 100s/it for 1500 frames at 704x704 with distilled fp8
  - *From: FryingMan*

- **Linux vs Windows VRAM usage**
  - Linux reserves less VRAM (maybe 2GB savings) if using monitor with same GPU
  - *From: Abyss*

- **WSL swap size**
  - Increase from default 16GB to 40GB to avoid crashes
  - *From: gordo*

- **VRAM for different resolutions**
  - 24GB VRAM can handle higher resolutions, 16GB VRAM should manage 1280x720
  - *From: David Snow*

- **CPU RAM usage**
  - Model can run anything on CPU RAM if you have enough system memory
  - *From: Abyss*


## Community Creations

- **Orbital LoRA for LTX2** (lora)
  - Camera movement LoRA for orbital camera motion
  - *From: Charlie*

- **Kijai's preview override node** (node)
  - Custom preview node that conflicts with normalizing sampler
  - *From: Miku*

- **LTXV Chunk FeedForward node** (node)
  - Reduces peak VRAM usage for larger generations
  - *From: Kijai*

- **LTX2 Sampling Preview Override** (node)
  - Enables preview functionality during LTX Video 2 generation with optional upscaling
  - *From: Kijai*

- **LTX2 Audio Latent Normalizing Sampling** (node)
  - Normalization node that works with masks and gives identical results to the sampler
  - *From: Kijai*

- **LTXVLatentPreview** (node)
  - Enables latent previews for LTX-2, currently low quality but functional
  - *From: Miku*

- **NAG (Negative Augmented Generation) node** (node)
  - Makes negative prompts work with CFG 1 by combining with positive conditioning
  - *From: DawnII*

- **RES4LYF nodes** (node)
  - Custom nodes for LTX-2 workflows, requires separate requirements installation
  - *From: randomanum*

- **Voice cloning workflow** (workflow)
  - Extract and replace audio from LTX videos using RVC Engine
  - *From: Nokai/PsiClone*

- **LTX2-Infinity** (workflow)
  - Infinite video generation workflow with audio bridging capabilities
  - *From: ZombieMatrix*

- **Inpainting workflow fix** (workflow)
  - Fixed inpainting workflow that addresses recent breaking changes
  - *From: Nekodificador*

- **New ImgToVideoInplaceMulti node** (node)
  - Allows multiple images with index selection, uses new dynamic input system
  - *From: Kijai*

- **LTXV chunk feed forward patch** (tool)
  - Memory saving model patch with ~10% speed penalty
  - *From: Kijai*

- **Inpainting fix patch** (tool)
  - Fixes broken inpainting functionality while retaining memory savings
  - *From: Kijai*

- **Random camera LoRA** (lora)
  - LoRA needed for camera movement, without it you only get slow camera movement unless prompting very specifically
  - *From: Mazrael.Shib*

- **Detailer LoRAs** (lora)
  - LoRAs that make huge difference to quality along with framerate, samplers, and resolution
  - *From: David Snow*

- **Image enhancement node setup** (workflow)
  - Nodes that enhance images between first and second pass, includes film grain and blend controls
  - *From: David Snow*

- **Scooby Doo style LoRA** (lora)
  - Style LoRA for LTX2 with good quality output
  - *From: dj47*

- **WHATUSEE LoRA** (lora)
  - Custom LoRA tested in I2V and FFLF by burgstall
  - *From: burgstall*

- **Chunked FFN node** (node)
  - Memory optimization node that reduces VRAM usage during generation
  - *From: Kijai*

- **Feedforward node** (node)
  - Reduces VRAM usage by 1-2GB at higher input sizes
  - *From: Kijai*

- **LTXImageToVideo in-place node** (node)
  - Allows image conditioning at any frame location, though it's a hack putting single frame info in 8-frame latent
  - *From: Kijai*

- **Voice cloning models** (model)
  - Trained GLaDOS and Bender voice models for synthetic audio generation
  - *From: Fill*

- **KJNodes LTX2 NAG node** (node)
  - Allows negative audio conditioning to improve audio quality
  - *From: veldrin*

- **Automated music video workflow** (workflow)
  - Complex workflow combining whisper vocal extraction, ChatGPT story generation, LLM prompt enhancement, and automated video generation
  - *From: VRGameDevGirl84(RTX 5090)*

- **Frame padding node** (node)
  - Custom node that duplicates the last frame 7 times to fix audio sync issues
  - *From: VRGameDevGirl84(RTX 5090)*

- **Audio chunk splitter nodes** (node)
  - Custom nodes that split audio with indexing, allow re-doing chunks, move to backup folders
  - *From: VRGameDevGirl84(RTX 5090)*

- **LTX2 Audio Latent Normalizing Sampling** (node)
  - Experimental node that helps with lipsync by adjusting video influence, may ruin audio gen but useful with input audio
  - *From: Kijai*

- **LTX2 Sampling Preview Override** (node)
  - Node for animated previews during sampling, currently not working
  - *From: Kijai*

- **Audio downsampling node** (node)
  - Node to downsample audio to 16kHz before SR processing
  - *From: ▲*

- **Audio to video attention booster node** (node)
  - Allows boosting audio to video attention for existing audio inputs
  - *From: Kijai*

- **Memory optimization nodes** (node)
  - Two nodes that together save 6GB VRAM during generation
  - *From: Kijai*

- **WAN2.1 detailer workflow** (workflow)
  - Light pass detailer for fixing garbled details without affecting likeness or audio sync
  - *From: Ablejones*

- **Two-stage resolution workflow** (workflow)
  - Downscales to half resolution then upscales 2x for better motion and speed
  - *From: Elvaxorn*

- **WHATUSEE LoRA** (lora)
  - LoRA that took most of last weekend to create
  - *From: burgstall*

- **LTX2 Attention Tuner Patch** (node)
  - Can help increase audio influence on video, still experimental as it degrades output slightly
  - *From: Kijai*

- **Chunk FeedForward node** (node)
  - VRAM optimization node for memory reduction
  - *From: Kijai*

- **Custom mask processing node** (node)
  - Takes maximum value of masks in pixels for entire latent frame to fix temporal mask blurring
  - *From: Ablejones*

- **Timeline editor GUI node** (node)
  - Interactive timeline interface for managing video projects with scene adjustment, file loading, and batch rendering capabilities
  - *From: ErosDiffusion*

- **Beat analyzer node for music videos** (node)
  - Analyzes music beats and sends list of durations to make video cuts align with song beats
  - *From: VRGameDevGirl84*

- **LTX-infinity workflow with segmented video extension** (workflow)
  - Automated workflow for creating long-form videos by stitching multiple segments with seamless transitions
  - *From: ZombieMatrix*

- **Image2reverb spatial audio tool** (tool)
  - Forked and modified tool that generates reverb impulse responses from images for matching audio ambience to visual spaces
  - *From: mdkb*

- **Resized distilled LoRA** (lora)
  - ltx-2-19b-distilled-lora_resized_dynamic_fro09_avg_rank_175_fp8 - smaller version of distilled LoRA
  - *From: community*

- **Custom video chaining nodes** (node)
  - Custom nodes that chain videos together for unlimited length
  - *From: VRGameDevGirl84*

- **LTX2 Mem Eff Sage Attention Patch** (node)
  - Memory efficient version of sage attention specifically for LTX2
  - *From: Kijai*

- **Chunk Feedforward optimization** (node)
  - Reduces memory usage for feedforward operations
  - *From: Kijai*

- **NAG (Negative Augmented Generation) node** (node)
  - Improved negative prompting for LTX2 distilled model
  - *From: Kijai*

- **Memory Usage Factor controller** (node)
  - Allows fine-tuning of VRAM usage with automatic restoration
  - *From: Kijai*

- **LTX automation workflow** (workflow)
  - Nearly fully automated workflow using Gemini LLM nodes for prompt generation
  - *From: VRGameDevGirl84*

- **Taichi-based particle emitting nodes** (node)
  - Audio reactive particles compatible with ROTI features, uses GPU instead of single CPU thread
  - *From: burgstall*

- **Taichi particle emitter nodes** (node)
  - Audio-reactive particle emission system for LTX-2, uses ROTI's feature format
  - *From: burgstall*

- **LTX2 Memory optimization patches** (node)
  - Multiple memory efficiency improvements including forward function changes and chunking
  - *From: Kijai*

- **LTXVAllInOneVRAMPatchesNode concept** (node)
  - Suggested unified node for all VRAM optimization patches
  - *From: ucren*

- **LTXV Enhance A Video** (node)
  - Video enhancement node by Kijai, provides improvements over regular pipeline
  - *From: Xor*

- **LTX2 inpainting workflow** (workflow)
  - Working inpainting based on ltx2_memory branch with some artifacting
  - *From: ucren*

- **High quality video workflow** (workflow)
  - Obsessively optimized settings for best quality, includes latest mem efficient sage and tiny vae
  - *From: David Snow*

- **Memory optimization nodes** (node)
  - Attention tuning and memory usage factor nodes for optimization
  - *From: Kijai*

- **Native prompt enhancer** (node)
  - Fully native version that can understand images without using transformers
  - *From: Kijai*


---

# LTX Chatter - January 24-31, 2026

# Ltx Chatter Knowledge Base
*Extracted from Discord discussions: 2026-01-24 to 2026-02-01*


## Technical Discoveries

- **LTX2 has high VRAM spikes during generation**
  - It doesn't use that much VRAM continuously but has very high spikes
  - *From: Ablejones*

- **Distill LoRA improves dev model quality significantly**
  - Even 0.1-0.2 of distill LoRA on dev model produces cleaner results than without it
  - *From: Kijai*

- **Single block LoRA application still effective**
  - Distill LoRA on first block only at 0.5 strength makes huge difference despite there being 48 blocks total
  - *From: Kijai*

- **FFN chunks can be reduced to 2**
  - Now enough to use only 2 ffn chunks instead of higher values
  - *From: Kijai*

- **Model recognizes voices and generates corresponding visuals**
  - When given speech of African American woman, model outputs video of African American woman even without specifying in prompt. Training data accuracy is reflected in this behavior.
  - *From: hicho*

- **Model produces specific accents based on visual appearance**
  - You get specific accents depending on how people look, sometimes regardless of prompts trying to override it
  - *From: ucren*

- **KJ loaders significantly improve inference speed**
  - Made inference steps go from 30 to 10 seconds per step compared to native which was casting to fp32
  - *From: hicho*

- **modelcomputeDtype setting dramatically improves performance**
  - Inference went down from 30 seconds to 20 seconds on 3090 with GGUF Q8
  - *From: ▲*

- **FFN chunking may not affect output quality on some setups**
  - Chunking on/off showed pixel perfect same results with slight speed difference on 4070 Ti Super
  - *From: Gleb Tretyak*

- **LTX preprocessing uses h.264 codec compression**
  - The preprocess node actually encodes using h.264 codec which has limitations when encoding frames
  - *From: The Shadow (NYC)*

- **VAE decode expects single latent to be single image**
  - No matter how many latents it gets, it always assumes the first is a single image
  - *From: theUnlikely*

- **LTX2 recognizes voices from real quotes**
  - Using actual quotes in prompts generates the corresponding voice - example: Trump quote generates Trump voice
  - *From: hicho*

- **IC-lora brings everything into focus**
  - The IC-lora removes depth of field and makes background come into focus, useful for certain scenarios
  - *From: Kijai*

- **IC-lora useful at low resolutions**
  - IC-lora provides noticeable improvement at 480-620 resolution bucket, especially for T2V
  - *From: ▲*

- **Significantly increasing resolution and FPS improves quality**
  - Using at least 48 FPS with high resolution greatly improves image clarity, visual appeal, and reduces ghosting
  - *From: BNP4535353*

- **Using VAE KJ loader at fp16 speeds up add guide node**
  - Switching to KJ VAE loader at fp16 makes the controlnet add guide node faster
  - *From: hicho*

- **Warming up VAE with 1 frame then rendering full frames improves speed**
  - Loading models and warming up VAE with 1 frame first, then rendering 121 frames shows speed improvement compared to running all frames while models load
  - *From: hicho*

- **Memory management for LTX was fixed**
  - The --reserve-vram flag is no longer needed according to user testing
  - *From: N0NSens*

- **4 steps is better for keeping init image in 320p first pass**
  - Using fewer steps actually preserves the initial image better during first pass generation
  - *From: Kijai*

- **Compression artifacts may not be necessary for motion**
  - User trained a 256 rank LoRA on 30,000 videos that produces motion without needing compression noise on start image
  - *From: Fill*

- **Motion blur can reduce LTX artifacts**
  - Applying Pixel motion blur in After Effects before V2V processing at 60+ FPS reduces motion artifacts
  - *From: protector131090*

- **2nd stage upscaling provides significant quality improvement**
  - Users report that 2nd stage processing is worth the time investment for quality gains
  - *From: hicho*

- **LTX can handle very long videos**
  - Successfully tested at 1280x720x1000f and 1920x1080x481f, potentially up to 500f before audio crashes
  - *From: BNP4535353*

- **RTX 5090 can handle 4K video generation but with significant frame limitations**
  - 5090 can do 33 frames in 4K without tiled VAE, defaults to tiles after that. With 96GB RAM, could potentially do 4K 121 frames if memory leaks were fixed
  - *From: protector131090*

- **Color washing and black/white artifacting occurs at higher resolutions**
  - QHD and 4K generations sometimes lose color, hands get black and white, colors start to wash out
  - *From: protector131090*

- **Memory leaks prevent consistent rendering**
  - Yesterday rendered 150 frames in QHD 60fps, after that couldn't even render 90 frames whatever settings used
  - *From: protector131090*

- **Portrait orientation doesn't work well with LTX**
  - LTX doesn't respond well to portrait aspect ratios, 21:9 landscape works better
  - *From: David Snow*

- **LTX2 Image2Video Adapter LoRA significantly improves i2v quality**
  - Trained to stick to reference images harder than original LTX, no compression tricks needed, direct image embedding pipeline
  - *From: Fill*

- **LTX2 LoRAs have separate audio and video attention blocks**
  - Found audio_attn1.to_v.lora_B.weight and cross-modal keys like audio_to_video and video_to_audio in LoRA structure
  - *From: Phr00t*

- **Different systems produce wildly different outputs with identical settings**
  - Same models, ComfyUI version, PyTorch, drivers produce visibly different results across different setups
  - *From: Kijai*

- **CPU vs GPU device selection changes output significantly**
  - Switching device from GPU to CPU produces completely different images
  - *From: Abyss*

- **60fps reduces motion artifacts compared to 24fps**
  - User found artifacts almost gone when switching from 24fps to 60fps generation
  - *From: protector131090*

- **Audio normalization at specific steps improves audio quality**
  - Steps 3 and 6 should be set to 0.25 for audio normalization, prevents clipping during audio sampling
  - *From: Phr00t*

- **Memory use factor optimization**
  - Default value for LTX is 0.077, lowering it provides speed optimization when using memory optimizations that push VRAM use down
  - *From: Kijai*

- **Chunked feed forward node saves significant VRAM**
  - Around ~1GB save at 720p for Wan model, much bigger save for LTX
  - *From: Kijai*

- **Different outputs between Linux and Windows setups**
  - Same workflow/models/torch version etc. produce different outputs on different operating systems
  - *From: Kijai*

- **Using Wan22 LN 0.4 denoise run with tiling helps keep overhead down**
  - Successfully running UHD with tiled setup while HuMo couldn't do FHD even with low context_window
  - *From: N0NSens*

- **Mixing HuMo first then Tiled produces even better results**
  - If you have enough hardware, combining models this way improves output
  - *From: N0NSens*

- **AddGuide working fine only with VAE fp32**
  - AddGuide and ImageToVideo not working with fp16, requires fp32 VAE
  - *From: hicho*

- **New Multimodal Guider significantly improves I2V quality**
  - Motion, dynamics, consistency seems crazy good with new nodes
  - *From: Volkin*

- **LTX2 normalizing sampler fixes overbaking issues**
  - Using normalizing sampler makes overbaking go away compared to default workflow
  - *From: Phr00t*

- **New LTX 2 guider nodes provide significantly better video and motion quality**
  - When using 1080p 15+ seconds with full dev model, new nodes sacrifice motion speed for quality and character consistency, prevent drifting
  - *From: Volkin*

- **Resolution requirements updated from div by 32 to div by 64**
  - Notes were updated to recommend divisible by 64 instead of 32
  - *From: TK_999*

- **Speed varies by video length, not just resolution**
  - Same speed for 10 seconds 720p and 1080p, but massive jump when bumped to 15 seconds 1080p
  - *From: Volkin*

- **API vs Local Gemma produces different outputs**
  - Local Gemma biases towards more realistic look, API has better prompt adherence and follows prompts better
  - *From: protector131090*

- **LTX2 API uses full precision Gemma vs local quantized versions**
  - API uses high precision version which can cause differences compared to quantized local versions
  - *From: Barak*

- **Hardware differences affect Gemma output consistency**
  - Different results on 4090 vs 5090 with same workflow, even CPU vs GPU on same PC gives different results
  - *From: protector131090*

- **New LTX2 API node provides better generation time and quality**
  - Using new LTX2 API node seems to be better in generation time and bit of quality
  - *From: 🦙rishappi*

- **FP4 + FP4 configuration uses 25GB RAM**
  - FP4 video model + FP4 text encoder uses sweet spot at 25GB RAM
  - *From: Volkin*

- **FP16 video model + FP4 text encoder uses 50GB max RAM**
  - On Linux, can run FP16 video model + FP4 text encoder with no swapfile at 50GB max RAM used
  - *From: Volkin*

- **Modality and skip steps relationship for new guider nodes**
  - Higher modality + 0 skip step = more constrained tight control (ideal for lipsync, character consistency, details). Skip steps = faster speeds, but should never be higher than modality value. Sweet spot for speed + better consistency = modality 1 + skip step 1
  - *From: Volkin*

- **Vertical format issues with LTX2**
  - Vertical/portrait videos work poorly compared to landscape - causes static results, face color shifts (orange faces), and motion issues
  - *From: David Snow, AJO, Charlie*

- **Resolution affects motion quality**
  - Higher resolutions can reduce motion in LTX2, similar to first LTX versions
  - *From: N0NSens*

- **API text encoder nodes provide significant speed improvement**
  - Using API text encoder nodes is 20% faster than standard text encoding
  - *From: AJO*

- **Euler sampler faster and more realistic than res_2s**
  - Euler sampler on first pass produces more realistic output and is much faster than res_2s
  - *From: AJO, David Snow*

- **WSL memory allocation issue**
  - Allocating too much RAM to WSL (86GB out of 96GB) caused memory thrashing and slow model loading, reducing to 76GB fixed it
  - *From: burgstall*

- **LTX2 uses mel spectrogram for audio processing, not wav2vec or whisper like previous models**
  - This allows it to use the full audio spectrum for conditioning while applying speech formants to mouth areas only
  - *From: Chandler ✨ 🎈*

- **Full audio mix works better than vocal splitting for music videos**
  - Model can use upcoming audio events to prepare visual scene and use visual context to inform audio. Character can actually move in time with music beat
  - *From: Chandler ✨ 🎈*

- **Audio can condition more than just mouth movements**
  - More audio mix given to model provides more audio conditioning beyond lip sync
  - *From: Chandler ✨ 🎈*

- **Mel-Bond can be safely disabled**
  - Everything works fine without separation
  - *From: N0NSens*

- **LCM + linear_quadratic scheduler combination works well**
  - User reports this as their favorite sampler setup with beta scheduler
  - *From: N0NSens*


## Troubleshooting & Solutions

- **Problem:** Tiny VAE error on startup
  - **Solution:** Strip out tiny VAE components and connect model directly to set model node
  - *From: David Snow*

- **Problem:** CUDA error '_cuda_archs' is not defined
  - **Solution:** Bypass sage attention and chunk feedforward nodes to test one at a time
  - *From: David Snow*

- **Problem:** OOM during VAE decode
  - **Solution:** Add --reserve-vram command line argument and increase spatial tiles to 6
  - *From: David Snow*

- **Problem:** GGUF nodes producing bad output
  - **Solution:** Update GGUF nodes and ComfyUI - GGUF nodes not being up to date causes bad output
  - *From: Kijai*

- **Problem:** VAE VRAM issues on AMD
  - **Solution:** VAE has to run in fp32 on AMD, update to nightly ComfyUI for halved VAE VRAM usage
  - *From: Kijai*

- **Problem:** No lip sync on talking videos
  - **Solution:** Simplify prompt, add NAG node, increase audio_to_video_scale value, try negatives like 'still image with no motion'
  - *From: Kijai*

- **Problem:** High res videos losing color/becoming black and white
  - **Solution:** Increase image compression to even 65
  - *From: ErosDiffusion*

- **Problem:** Flash attention errors on startup
  - **Solution:** Remove flash-attn with 'python_embeded\python.exe -m pip uninstall -y flash-attn' and nodes should fall back to sdpa properly
  - *From: Kijai*

- **Problem:** Tensor errors at 720p with lip sync
  - **Solution:** Remove flash-attn to resolve compatibility issues
  - *From: AJO*

- **Problem:** ComfyUI not supporting tiny VAE
  - **Solution:** Update ComfyUI to nightly version
  - *From: Kijai*

- **Problem:** Going directly to high resolution doesn't work well
  - **Solution:** Better to do upscaling in 2 stages rather than direct high res generation
  - *From: Kijai*

- **Problem:** Black and white or weird output at high resolution
  - **Solution:** Use 2-stage approach instead of direct high resolution generation
  - *From: protector131090*

- **Problem:** VHS audio trim node crashes with no audio input
  - **Solution:** Use VHS nodes which already check if there's audio, or add audio resample node
  - *From: Kijai*

- **Problem:** Workflow crashes when input video has no audio track
  - **Solution:** Add silent audio track or use audio video combine node
  - *From: hudson223*

- **Problem:** Error with sageattention version
  - **Solution:** Update to latest sageattention version (post 4) and use cu128 or higher
  - *From: Kijai*

- **Problem:** VRAM out of memory during VAE decoding
  - **Solution:** Use tiled VAE decoding, or decrease tiling parameters if already using
  - *From: jab*

- **Problem:** Set/Get nodes not working in subgraphs
  - **Solution:** Set/Get nodes won't work through subgraphs, ensure proper execution order
  - *From: Kijai*

- **Problem:** PromptModels WJSetGetPlus nodes corrupting workflows
  - **Solution:** Remove the PromptModels custom node pack and reload workflows from scratch using KJ's original set/get nodes
  - *From: AJO*

- **Problem:** NaN error during video save at high resolution
  - **Solution:** Lower resolution while keeping frame count constant, or use first pass audio instead of upscaled audio
  - *From: BNP4535353*

- **Problem:** Maximum recursion depth exceeded error
  - **Solution:** Check for looping workflow connections (1->2->3->1) or update nodes
  - *From: Gleb Tretyak*

- **Problem:** First frame effect when not encoding extensions
  - **Solution:** Use overlap to cover the bad first latent
  - *From: Kijai*

- **Problem:** Audio muxing errors
  - **Solution:** Create node that checks video for audio and muxes it in if missing, creating copy in temp directory
  - *From: hudson223*

- **Problem:** Audio VAE decode running out of VRAM for 2 minute videos
  - **Solution:** Use tiled audio decoding in 3 parts
  - *From: Xor*

- **Problem:** Tensor mismatch errors
  - **Solution:** Ensure audio and video masks match and are multiples of 8+1
  - *From: David Snow*

- **Problem:** CUDA 13.1 not working with torchaudio built for CUDA 13.0
  - **Solution:** Downgrade CUDA or ensure proper library versions
  - *From: Gleb Tretyak*

- **Problem:** VAE casting issues on older GPUs
  - **Solution:** Use fp32 for VAE when GPU doesn't support bf16, as many VAEs are sensitive to lower precision
  - *From: Kijai*

- **Problem:** Pause artifacts every 64 frames with temporal tiled VAE
  - **Solution:** Use normal VAE encode instead of tiled when possible, as tiled VAE is locked to multiples of 2
  - *From: ucren*

- **Problem:** Size mismatch between video and reference image
  - **Solution:** Ensure video and reference image dimensions match for controlnet workflows
  - *From: hicho*

- **Problem:** VAE not showing in Load VAE node list
  - **Solution:** Set ComfyUI manager to update to nightly instead of latest stable
  - *From: IceAero*

- **Problem:** Spatial inpainting not working - masked regions remain unchanged
  - **Solution:** Hit and miss, most of the time doesn't change anything. May depend on temporal mask placement
  - *From: Kijai*

- **Problem:** Split sampling bug with audio
  - **Solution:** Currently can't do split sampling with SamplerCustom if using audio - bug exists
  - *From: Kijai*

- **Problem:** Black frames remain black with 1.0 latent mask
  - **Solution:** Black frames still influence sampling even with mask 1.0, may need latent noise injection
  - *From: Simonj*

- **Problem:** VRAM OOM on RTX 4090 with SamplerCustomAdvanced
  - **Solution:** Don't use GGUF on 4090, use fp8 instead. Also suggested startup args: --preview-method none --reserve-vram 4
  - *From: Kijai*

- **Problem:** Audio desync issues with motion LoRA
  - **Solution:** Disable audio layers in LoRA using KJ's advanced LoRA node
  - *From: Kijai*

- **Problem:** Static frame issues in 9:16 aspect ratio
  - **Solution:** Use NAG (Negative Activation Guidance) or avoid overly simple prompts
  - *From: burgstall*

- **Problem:** Blur in generations
  - **Solution:** Use distill LoRA to fix blur issues
  - *From: protector131090*

- **Problem:** Different outputs between ComfyUI versions
  - **Solution:** Revert to ComfyUI 0.10.0 if experiencing quality degradation in 0.11
  - *From: Volkin*

- **Problem:** Unintended output changes with T2V after ComfyUI v0.11 update
  - **Solution:** Update KJNodes to fix addcmul_ operation differences that caused output changes
  - *From: Kijai*

- **Problem:** OOM errors on 24GB GPUs
  - **Solution:** Set memory use override to 1, or use --reserve-vram 1 or 1.5, ensure at least 64GB RAM
  - *From: Volkin*

- **Problem:** Model mismatch errors
  - **Solution:** Turn ON the bypass option in the workflow
  - *From: NC17z*

- **Problem:** Can't run legacy manager in new ComfyUI UI
  - **Solution:** Pass in --enable-manager --enable-manager-legacy-ui flags
  - *From: jab*

- **Problem:** VAE Encoder freezes with 250+ frames
  - **Solution:** Try LTX tiled VAE node which is faster and more efficient than default tiled VAE
  - *From: Volkin*

- **Problem:** Model Memory Usage Factor Override estimation wrong for offloading
  - **Solution:** Use kjnodes Model Memory Usage Factor Override node, set to 3.0 instead of default 2.3 for Wan2.1 i2v
  - *From: Ablejones*

- **Problem:** Sampler infinite looping due to subgraphing
  - **Solution:** Explode the subgraph to identify the loop
  - *From: The Shadow (NYC)*

- **Problem:** bf16 throws error, fp16 is ignored
  - **Solution:** Use fp32 for older video cards, bf16 is suitable for 30xx+
  - *From: Xor*

- **Problem:** FLF don't work when using split model way
  - **Solution:** This way only works as t2v
  - *From: hicho*

- **Problem:** Fade to black common with model
  - **Solution:** Often happens with i2v without external audio, may be related to generation length vs number of actions
  - *From: N0NSens*

- **Problem:** Error: Input tensors must be in dtype of torch.float16 or torch.bfloat16
  - **Solution:** Can't use Auto Feature, have to choose one of the presets
  - *From: NC17z*

- **Problem:** Black output at 1080p
  - **Solution:** Possible wrong resolution, try restarting or check if resolution is divisible by 64
  - *From: TK_999*

- **Problem:** Sigmas hitting high ceiling with ltxvscheduler
  - **Solution:** Adjust max_shift or disconnect latent to use default values making it not dependent on resolution
  - *From: Hashu*

- **Problem:** T2V errors with skip_blocks value 29
  - **Solution:** Delete/remove the skip_blocks value to stop the error
  - *From: Jonathan Scott Schneberg*

- **Problem:** New nodes don't work properly with T2V
  - **Solution:** Only I2V seems to work correctly with new nodes, T2V may need ComfyUI update
  - *From: Volkin*

- **Problem:** Error with model memory usage factor override kjnode
  - **Solution:** Remove skip_blocks to get rid of errors
  - *From: Elvaxorn*

- **Problem:** Distilled model with CFG produces bad/burned out outputs
  - **Solution:** Use normalizing sampler, even low values like 2,1,1,1,1,1,1,1 can look burned out
  - *From: David Snow*

- **Problem:** No lipsync with custom audio using new nodes
  - **Solution:** Change modality to Audio in the settings
  - *From: Elvaxorn*

- **Problem:** ComfyUI crashes on LTXV Audio VAE Loader node
  - **Solution:** Use --cache-none --novram and fp4 models for both
  - *From: Volkin*

- **Problem:** Out of memory on GPU when upscaling
  - **Solution:** Lower resolution and use upscaling instead of generating at high resolution directly
  - *From: protector131090*

- **Problem:** I2V taking much more VRAM than T2V
  - **Solution:** Update ComfyUI to v0.11 for better VRAM handling. Make sure ComfyUI itself is up to date to include memory optimizations
  - *From: Kijai*

- **Problem:** Memory issues with KJ nodes after runs
  - **Solution:** Use attention tuner patch node to force output results that was before ComfyUI 0.11 due to inplace operations changes
  - *From: Volkin*

- **Problem:** New nodes not showing up in search
  - **Solution:** Delete custom node and git clone it manually, or check for conflicting node packs like WanVideoWrapper overwriting
  - *From: Kijai*

- **Problem:** Color loss/semi black and white effect at high resolutions
  - **Solution:** Lower resolution and use upscaling - this happens when resolution is too high
  - *From: protector131090*

- **Problem:** Crashes with 32GB RAM
  - **Solution:** Use --cache-none (not --novram), fp8 or smaller models, native workflow with no prompt enhancer. May need --disable-pinned-memory and ensure page file is enabled
  - *From: Kijai*

- **Problem:** Portrait resolutions breaking image
  - **Solution:** LTX2 is limited in portrait resolutions. Use landscape format like 1920x1088 instead of 1088x1920
  - *From: scf*

- **Problem:** Pixelated results with Q8_0.gguf model
  - **Solution:** Use fp8 dev safetensor file instead of gguf versions. Match dev connector to dev model, distill connector to distill model
  - *From: David Snow*

- **Problem:** Orange face and tiny hands in generated videos
  - **Solution:** Use correct resolution - issue occurs when workflow generates at higher resolution than specified (e.g., 3840x2560 instead of 1920x1080)
  - *From: David Snow*

- **Problem:** Plastic/fake looking faces
  - **Solution:** Use distill LoRA at negative values (like -0.2) to counteract plastic skin issue, or switch from distilled model to dev model
  - *From: David Snow, protector131090*

- **Problem:** No motion in vertical videos
  - **Solution:** Try different workflows specifically designed for vertical, or render at lower resolution first then upscale
  - *From: protector131090*

- **Problem:** ComfyUI Manager missing nodes lists
  - **Solution:** Need to manually pull nodes - Manager no longer showing missing or updates sections for some users
  - *From: AJO*

- **Problem:** Models taking minutes to load from PCIe5 drive
  - **Solution:** Reduce WSL RAM allocation from 86GB to 76GB to prevent memory thrashing
  - *From: burgstall*

- **Problem:** Lost connection to ComfyUI with no indication why
  - **Solution:** Reboot ComfyUI
  - *From: AJO*

- **Problem:** Grid pattern appears on higher resolution clips (1920x1920)
  - **Solution:** Try using standard VAE Decode node (not tiled) or LTXV Spatio node
  - *From: garbus*

- **Problem:** Memory efficient sageattn crashes with multimodal guider
  - **Solution:** Disable memory efficient attention or check for user error in applying distill twice
  - *From: Gleb Tretyak*

- **Problem:** Perturbed attention (layer skip) broken for T2V
  - **Solution:** Turn off layer skip for T2V workflows
  - *From: Jonathan Scott Schneberg*

- **Problem:** Tiled VAE decoder works harder and uses more memory on non-16:9 resolutions
  - **Solution:** Use 16:9 aspect ratios for better performance
  - *From: nikolatesla20*


## Model Comparisons

- **Distill LoRA vs no LoRA on dev model**
  - Distill LoRA acts like a 'make it better' button, produces much cleaner results
  - *From: Ablejones*

- **SA solver vs res_2s**
  - SA solver is not the same quality as res_2s - uses Adams Bashforth method from 1883, multi-step methods are worse with SDE noise, less stable, worse error correction
  - *From: mallardgazellegoosewildcat2*

- **Distill vs Dev model with LoRA**
  - Dev model with distill lora (0.6) and scheduled CFG gives same speed at 8 steps but listens to prompt better
  - *From: N0NSens*

- **LTX2 vs SCAIL motion capacity**
  - SCAIL has superior motion capacity, though LTX2 preview version limited by lack of proper extension method and face control
  - *From: Kijai*

- **IC workflows vs normal workflows speed**
  - IC workflows are half the speed of normal workflows because they do twice the work
  - *From: Kijai*

- **LTX 4K vs WAN 1080p quality**
  - LTX 4K is about as good as WAN 1080p
  - *From: protector131090*

- **Depth LoRA vs Pose LoRA**
  - Depth LoRA keeps structure of original video while pose LoRA keeps plastic bag appearance
  - *From: hicho*

- **Euler vs Euler Ancestral vs Res2s**
  - Euler has cleaner vibrant colors compared to res2s at larger resolutions. Euler ancestral had faster generation but worse color shift from color to BW
  - *From: dj47*

- **LTX1 vs LTX2 for portrait animation**
  - LTX1 refused to animate portraits, LTX2 is hit and miss
  - *From: protector131090*

- **Natural language vs other conditioning**
  - Natural language is super bad conditioning mechanism but easy for the public. Scene graphs and segmentation maps are lot better
  - *From: mallardgazellegoosewildcat2*

- **LTX2 vs Wan for VFX**
  - LTX2 better suited as Sora replacement, Wan still king in terms of VFX
  - *From: Nekodificador*

- **Motion LoRA with vs without audio layers**
  - Disabling audio layers prevents desync while maintaining motion benefits
  - *From: protector131090*

- **I2V adapter at different strengths**
  - 0.5 strength better for consistency to initial image than 1.0 strength
  - *From: protector131090*

- **T2V vs T2V with I2V adapter**
  - Adapter makes things more cartoonish, especially at stage 2
  - *From: protector131090*

- **GGUF Q2 vs fp8 on RTX 4090**
  - fp8 is faster and uses less VRAM than GGUF quantization
  - *From: Kijai*

- **LTX 2 IC Pose LoRA vs SCAIL**
  - LTX 2 more consistent in facial expressions, SCAIL better at copying poses
  - *From: Kevin "Literally Who?" Abanto*

- **Full resolution vs upscale mode**
  - Running I2V at full res 720p/1080p gives very good crisp, dynamic and motion fluid animations compared to default low res + upscale mode, but much slower
  - *From: Volkin*

- **3 vs 4 vs 8 steps**
  - Can't see big differences, 3 steps can make similar results compared to 8 steps
  - *From: Kevin "Literally Who?" Abanto*

- **LTX2 vs InfiniteTalk for V2V motion**
  - LTX2 V2V motion capability seems a lot better than InfiniteTalk
  - *From: KingGore2023*

- **Wan 1.3b vs 14b for upscaling**
  - 14b much better (and slower as well)
  - *From: N0NSens*

- **Kandinsky5 2b vs Wan2.1 14b**
  - 2b model isn't magically on par with 14B model, whole Kandinsky5 thing was waste of time
  - *From: Kijai*

- **MOVA vs LTX2**
  - Don't see a competition, MOVA is weak with 8 second generations that take multiple times as long
  - *From: KingGore2023*

- **Kling vs LTX2 motion performance**
  - Kling got best motion performance so far, even at 1080p, but too expensive and heavily censored
  - *From: KingGore2023*

- **New guider nodes vs regular pipeline**
  - 2-3x slower but significantly better output quality, premium quality level
  - *From: Volkin*

- **API Gemma vs Local Gemma**
  - API has better prompt adherence and is faster with less VRAM/RAM usage, Local biases toward realistic look
  - *From: protector131090*

- **Distilled vs Dev model with new nodes**
  - New guider nodes don't work with distilled since they modify CFG logic and distilled has no CFG
  - *From: Benjimon*

- **LTX2 I2V quality assessment**
  - I2V is amazingly good now with new nodes
  - *From: Volkin*

- **Euler vs res_2s sampler**
  - Euler is faster and produces more realistic output for first pass, res_2s better for detail in upscale pass
  - *From: David Snow, AJO*

- **Dev model vs distilled model**
  - Dev model with distill LoRA avoids plastic face issues better than distilled model alone
  - *From: protector131090, N0NSens*

- **LTX2 vs Humo for music videos**
  - Humo takes 32 minutes for 3 min generation but is more static, LTX2 has better motion but character consistency issues when leaving frame
  - *From: AJO*

- **Dev model vs distill model**
  - Dev alone with more steps is obviously the best, but distill model is way better for sound and avoids jank outputs
  - *From: Jonathan Scott Schneberg, Benjimon*

- **Guide nodes vs default sampler**
  - Guide nodes have much better output even at 9:16 unsupported aspects with difficult images
  - *From: Volkin*

- **LTX-2 vs other models (Kling 2.6, Wan 2.6, Seedance Pro)**
  - LTX-2 and Wan2.2 + Lightx2v win on animated video game character consistency where others fail
  - *From: Volkin*


## Tips & Best Practices

- **Use 10-20% of VRAM for --reserve-vram setting**
  - Context: When setting --reserve-vram parameter
  - *From: CelestialDesign*

- **Don't use --reserve-vram with current ComfyUI on NVIDIA**
  - Context: Lots of people using it for no reason now with current ComfyUI version
  - *From: Kijai*

- **Higher resolutions work better than lower ones**
  - Context: 1920x1088 works well, going down to 1280x768 causes blurry rapid movement like possessed person
  - *From: boorayjenkins*

- **Flow models benefit from many very tiny steps**
  - Context: When using different schedulers and step counts
  - *From: Ablejones*

- **Give room in prompts for audio generation**
  - Context: Too much description that doesn't match throws off audio sync
  - *From: Kijai*

- **Use --cache-ram option for massive workflows with lots of models**
  - Context: Allows offloading from RAM to prevent VRAM issues
  - *From: Kijai*

- **Apply preprocessing to larger image for better quality**
  - Context: Video artifacting gets scaled down more when resized from larger source
  - *From: Ablejones*

- **Resize input image to working resolution first**
  - Context: Better than letting guide nodes resize with bilinear
  - *From: N0NSens*

- **Use multiple virtual environments for different node types**
  - Context: Dependencies are too complex to fit everything in one venv
  - *From: Nekodificador*

- **Keep pinned memory enabled unless having RAM issues**
  - Context: Much faster offloading with it enabled, only disable if RAM problems
  - *From: Kijai*

- **Disconnect LLM and write own prompts, switch first sampler to euler**
  - Context: When experiencing Ken Burns effect instead of actual motion
  - *From: David Snow*

- **Increase image compression to help with motion**
  - Context: When getting panning/scanning instead of movement
  - *From: David Snow*

- **Use 1080p resolution and 2 stage for crisp quality**
  - Context: For both T2V and I2V generation
  - *From: hicho*

- **Turn down image strength to let motion LoRA come through**
  - Context: When using motion LoRAs with I2V
  - *From: Flipping Sigmas*

- **Use first pass audio when upscaled audio has issues**
  - Context: When encountering audio problems at high resolutions
  - *From: David Snow*

- **Avoid using IC-lora in I2V because it changes input too much**
  - Context: IC-lora adds details that don't exist in input image
  - *From: Kijai*

- **Use simple prompts instead of complex ones**
  - Context: LTX works better with simple prompts rather than super long detailed prompts
  - *From: hicho*

- **Restyle first frame with same view and pose for better controlnet results**
  - Context: When using controlnet workflows
  - *From: hicho*

- **Skip frames to speed up processing while maintaining motion**
  - Context: Using 57 frames instead of 121 with same motion is faster and acceptable quality
  - *From: hicho*

- **Use depth LoRA when reference frame is similar to original video**
  - Context: Pose LoRA should only be used when restyle frame is very different from original video frame
  - *From: hicho*

- **Don't skip 2nd stage upscaling**
  - Context: 2nd stage is worth the time investment for quality improvement
  - *From: hicho*

- **Use LLM for detailed prompts**
  - Context: Use roughly 100 words per second of video for i2v
  - *From: ZombieMatrix*

- **Humans rarely prompt as well as LLMs**
  - Context: Too lazy to not use prompt enhancer, LLMs generally better at prompting
  - *From: mallardgazellegoosewildcat2*

- **Lower resolution allows longer video generation**
  - Context: At some point lower the res, longer it can go - model breaks with more frames at high resolution
  - *From: Kijai*

- **Use first to last frame for reliable results**
  - Context: Reliable method for complex animations
  - *From: Phr00t*

- **Apply LoRA strengths differently to audio and video components**
  - Context: When merging LoRAs to prevent dialog stomping
  - *From: Phr00t*

- **Use less contrasted initial images for better AI model performance**
  - Context: Subtle but makes significant difference
  - *From: Tonon*

- **I2V adapter particularly useful for animating vertical images**
  - Context: Vertical images often refuse to move without adapter
  - *From: protector131090*

- **Use linear_quadratic scheduler instead of manual sigmas**
  - Context: Native implementation available, shift 8 equivalent to manual sigmas
  - *From: Kijai*

- **Refresh browser if previews don't work after creating new nodes**
  - Context: Known bug workaround
  - *From: Kijai*

- **Use --novram for best VRAM efficiency**
  - Context: Especially for full 1920x1080p 15+ second videos on 16GB VRAM + 64GB RAM
  - *From: Volkin*

- **Use longer detailed prompts with audio cues**
  - Context: LTX-2 responds much better to detailed descriptions and explanations rather than short prompts
  - *From: Volkin*

- **Higher resolution and FPS improves quality**
  - Context: For LTX, higher res and higher fps reduces hand damage and other artifacts, but will be much slower
  - *From: N0NSens*

- **Use torch compile with Wan for refinement**
  - Context: Should free a couple VRAM gigs when passing through Wan for refinement
  - *From: Volkin*

- **Connect two switches to the same toggle for hybrid i2v/t2v workflow**
  - Context: When making workflows that can switch between modes
  - *From: David Snow*

- **Just connect bypass switch on imagetovideoinplace to subgraph input**
  - Context: For making hybrid i2v/t2v workflow, make sure both passes connected to same socket
  - *From: David Snow*

- **Set AddGuideMulti frame_idx to -1 and strength to 0 with cropguides**
  - Context: For t2v when VidInPlace node doesn't work well
  - *From: CelestialDesign*

- **Use First to Last frame workflow for better results**
  - Context: Results are some of the best ever had with LTX or WAN
  - *From: garbus*

- **Don't use default template, use normalizing sampler**
  - Context: Default workflow sucks, avoiding overbaking issues
  - *From: Phr00t*

- **Use negative distill LoRA values to debake distilled models**
  - Context: When using distilled model, use negative 0.4-0.6 values
  - *From: hudson223*

- **For 2nd pass with distilled model, use higher distill LoRA strength**
  - Context: 0.6 at 1st pass, 0.8 at 2nd pass to avoid overcooked results
  - *From: N0NSens*

- **LTX2 loves big detailed prompts**
  - Context: Model was trained with detailed prompts since early versions, unlike other models
  - *From: Elvaxorn*

- **Use separate guider parameter nodes for audio and video**
  - Context: Need two guider parameter nodes chained - one for audio, one for video
  - *From: Volkin*

- **Clear model after generation when using LM Studio**
  - Context: Make sure to check this option when using LM Studio integration
  - *From: Elvaxorn*

- **Use official fp8 model for 4070**
  - Context: Gets speed boost from 40xx fp8 matmul support and is properly scaled
  - *From: Kijai*

- **Guide nodes are better than in-place for First-Last-Frame**
  - Context: Always gives much better consistency for FLF workflows
  - *From: Volkin*

- **Put 'Pink Panther' and 'Big Nose' in negative prompt for vampire/Dracula content**
  - Context: Helps with generating vampire/Dracula characters properly
  - *From: garbus*

- **Never use --novram with low RAM**
  - Context: --novram with low ram is kill switch
  - *From: Kijai*

- **Use --cache-none for memory issues**
  - Context: For low VRAM situations, use --cache-none instead of --novram
  - *From: Kijai*

- **Enable page file on Windows**
  - Context: Will crash trying to run LTX-2 workflows even with 64GB RAM if no page file
  - *From: Ablejones*

- **Simple prompts work best for audio-driven generation**
  - Context: Basic prompt like 'a girl in a blue dress talks' is sufficient - model does heavy lifting, complex audio transcription setups not needed
  - *From: David Snow*

- **Use two-pass rendering for quality**
  - Context: Render first pass at 720p, second pass upscaling for better results at 1080p
  - *From: protector131090*

- **Hide video length limitations with cuts**
  - Context: Do 20 seconds at a time from different angles instead of trying longer generations
  - *From: David Snow*

- **Use sa_solver sampler for upscale pass**
  - Context: sa_solver is faster than res_2s for second pass, but don't use on first pass as it drifts from init image
  - *From: David Snow*

- **Use consistent microphone LoRA**
  - Context: When trying to keep microphone appearance consistent across generations
  - *From: BitPoet (Chris)*

- **Switch to different window to regain speed after checking previews**
  - Context: Previews slow down generation, switching windows accelerates them back
  - *From: Volkin*

- **Minimum 40 steps for dev model or res2s with 20**
  - Context: For better quality results
  - *From: Volkin*

- **Offload model to RAM and use VRAM free to host latent video frames**
  - Context: For running FP16 on 16GB VRAM
  - *From: Volkin*


## News & Updates

- **Tiny VAE support merged into ComfyUI**
  - Can update ComfyUI and KJNodes to get proper previews with tiny vae now
  - *From: Kijai*

- **VAE VRAM usage halved in nightly ComfyUI**
  - Update to nightly version to get commit that halves VAE VRAM use
  - *From: Kijai*

- **New motion LoRA released with trigger word 'ltxable motion'**
  - 3GB high rank LoRA focused on steerable motion outputs, replaces previous version with corrected training parameter
  - *From: Flipping Sigmas*

- **No official date for LTX 2.5 release**
  - No confirmed timeline available for next version
  - *From: Charlie*

- **LTX2 Image2Video Adapter LoRA released**
  - Fill dropped the adapter on HuggingFace, substantially improves i2v generation quality
  - *From: Fill*

- **Split sampling fix coming to ComfyUI**
  - PR submitted to fix split sampling issue with LTX2
  - *From: Kijai*

- **LTX 2.1 and 2.5 announced**
  - CEO announced during Reddit AMA
  - *From: Lodis*

- **ComfyUI-LTXVideo added API text encode feature**
  - GitHub commit d153ca3f7839759baa7c58c331277451ba760bbb
  - *From: ramonguthrie*

- **Fill considering V2 release of motion LoRA with audio blocks disabled**
  - Response to audio desync discovery
  - *From: Fill*

- **Kijai released new KJNodes version with LTX LoRA Advanced node**
  - Allows disabling audio layers and adjusting individual layer/block strengths
  - *From: Kijai*

- **ComfyUI v0.11 includes LTX2 VRAM optimizations**
  - Refactor forward function for better VRAM efficiency and fix spatial inpainting by kijai in #12046
  - *From: Danial*

- **KJNodes updated to fix output changes**
  - Fixed unintended output change caused by addcmul_ operations that affected T2V more visibly
  - *From: Kijai*

- **End-of-January LTX-2 drop released**
  - More control in real-world workflows, includes API text encoder, Multimodal Guider, IC LoRA improvements
  - *From: Lodis*

- **LTX team working on improving prompt understanding**
  - Planning to improve visual quality and reduce watery effect
  - *From: LTX Lux*

- **MOVA model released**
  - 18B parameter model based on Wan2.2, generates video and audio simultaneously, Apache2 license
  - *From: Ada*

- **New model hopefully at end of quarter**
  - Future LTX2 model expected
  - *From: KingGore2023*

- **LTX Video 2 released with new control nodes**
  - Released January 5, 2026 with better control for real workflows, supports text-to-video and image-to-video with audio
  - *From: community*

- **Free API for prompt enhancer now available**
  - LTX offers free API to offload the LLM completely, removing local processing burden
  - *From: Purz*

- **LTX commented on multimodel guidance**
  - Official response to community questions about multimodel guidance features
  - *From: Chandler ✨ 🎈*

- **New LTX2 multimodal guidance nodes released**
  - Better control for real workflows, includes modality and skip step parameters
  - *From: LTX team*

- **MOVA audio video model released**
  - 32b parameters, open sourced with code
  - *From: dj47*

- **LTX-2-19b-IC-LoRA-Union-Control released**
  - Union control like ControlNet
  - *From: Draken*

- **LTX team acknowledged 9:16 mode issues**
  - Team admitted vertical/portrait mode doesn't work well and will fix in next update
  - *From: Charlie*

- **VRAM usage inconsistency resolved**
  - After ComfyUI update, VRAM usage returned to normal from previous 98% spikes
  - *From: Charlie*

- **Story Writer workflow released**
  - Takes story info input, uses QWEN VL node to generate story and QWEN TTS friendly character descriptions up to 4 characters
  - *From: manu_le_surikhate_gamer*

- **PR submitted to LTXVideo repository**
  - Pull request #401 submitted
  - *From: theUnlikely*


## Workflows & Use Cases

- **Audio extension via multiple generations**
  - Use case: Extending audio beyond single generation limits using 5 separate generations
  - *From: Kijai*

- **Two-stage generation with guides**
  - Use case: Using add guides method with 6 frames over 601 frames at 1920x1088
  - *From: boorayjenkins*

- **2-pass generation with different step counts**
  - Use case: 3 sigmas from tail end of linear quad for quality improvement
  - *From: ucren*

- **First and last frame workflow**
  - Use case: Generating videos with specific start/end frame constraints
  - *From: protector131090*

- **Clown sampler setup for single pass**
  - Use case: Using dev model with distill lora weights ramping up at the end
  - *From: TK_999*

- **Extension workflow with overlap handling**
  - Use case: Re-encoding last 25 frames for video extensions
  - *From: theUnlikely*

- **Auto audio muxing node**
  - Use case: Automatically checks video for audio and muxes it in if missing
  - *From: hudson223*

- **Two-stage upscaling with first pass audio retention**
  - Use case: Allows switching between upscaled and original audio when needed
  - *From: David Snow*

- **Lip sync for existing video with new audio**
  - Use case: Replacing speech in movie scenes with cloned voices
  - *From: David Snow*

- **Motion blur preprocessing before V2V**
  - Use case: Apply pixel motion blur in After Effects, then V2V at 60+ FPS to reduce artifacts
  - *From: protector131090*

- **Automated flux 4B restyle to LTX2 pipeline**
  - Use case: Restyle first frame with Flux 4B then send to LTX2 for consistent character transformation
  - *From: hicho*

- **SRT file timestamp input for scene switching**
  - Use case: Using subtitle file timestamps to target specific sections for processing
  - *From: VRGameDevGirl84(RTX 5090)*

- **Audio-driven i2v generation**
  - Use case: Generate video from image with audio synchronization
  - *From: protector131090*

- **Two-pass generation with distill LoRA**
  - Use case: Higher quality output using distilled model with LoRA
  - *From: various*

- **Spatial inpainting workflow**
  - Use case: Modify specific regions of video while keeping rest original
  - *From: Nekodificador*

- **Two-pass generation with and without distill**
  - Use case: First pass without cfg, second with cfg for better quality
  - *From: ˗ˏˋ⚡ˎˊ-*

- **LoRA merging with separate audio/video strengths**
  - Use case: Combining multiple LoRAs while preventing audio dialog issues
  - *From: Phr00t*

- **I2V with motion adapter for lip sync**
  - Use case: Improving lip sync quality, works better than without adapter
  - *From: protector131090*

- **Two-pass refinement with Wan/Humo**
  - Use case: Cleaning motion artifacts and improving quality, requires loading Wan/Humo
  - *From: pom*

- **Tiled upscaler/refiner setup**
  - Use case: Alternative to Wan refinement for users with limited VRAM/RAM
  - *From: N0NSens*

- **Hybrid i2v/t2v workflow with toggle switch**
  - Use case: Switching between image-to-video and text-to-video in same workflow
  - *From: David Snow*

- **Loop test over different lora versions**
  - Use case: Training validation, generates 10 videos for comparison
  - *From: Gleb Tretyak*

- **LTX2 V2V with audio for lip-sync**
  - Use case: Replace empty noise latent with video latent, don't need upscaling stage for 720p
  - *From: KingGore2023*

- **Two-stage LTX2 with distilled LoRA**
  - Use case: Using distilled LoRA at 2nd stage for upscaling with ic-detailer to help stabilize latent noise
  - *From: Volkin*

- **Music video production workflow**
  - Use case: Running 17 chunks of 10-second videos for music video creation, testing different model versions for plasticy output and lipsync issues
  - *From: AJO*

- **Using new API nodes with local rendering**
  - Use case: Better generation time and quality while offloading text encoder
  - *From: 🦙rishappi*

- **FP4 + FP4 setup for low RAM**
  - Use case: Running LTX2 with 32GB system RAM using fp4 video model and text encoder
  - *From: Volkin*

- **Guide nodes for I2V**
  - Use case: Better consistency for image-to-video generation, especially for character consistency and details
  - *From: Volkin*

- **Lower resolution with upscaling**
  - Use case: Avoid color loss and memory issues at high resolutions
  - *From: protector131090*

- **Two-pass rendering with different samplers**
  - Use case: First pass with Euler for speed and realism, second pass with res_2s or sa_solver for detail upscaling
  - *From: David Snow*

- **Audio-driven I2V workflow**
  - Use case: Image-to-video with audio synchronization, works better in landscape format
  - *From: protector131090*

- **Dev model workflow with manual sigmas**
  - Use case: Using dev fp8 model with CFG 4, 20 steps first pass, 4 steps second pass with CFG 1
  - *From: David Snow*

- **Automated music video generation with 17 chunks**
  - Use case: Full song production at 250 seconds per 10 second chunk, 70 minutes total processing time
  - *From: AJO*

- **Audio to video without prompts**
  - Use case: Let audio guide the model completely, grab best video scenes and use audio to see model output
  - *From: hicho*


## Recommended Settings

- **--reserve-vram**: 1-2 GB recommended
  - Better to use lower values like 1-2GB instead of high values like 8GB
  - *From: Abyss*

- **Spatial tiles**: 6
  - Increase to 6 to help with VRAM management
  - *From: David Snow*

- **FFN chunks**: 2
  - Now sufficient to use only 2 chunks instead of higher values
  - *From: Kijai*

- **Distill LoRA strength**: 0.1-0.6
  - Works effectively in this range, even 0.1-0.2 shows significant improvement
  - *From: neofuturo*

- **Memory usage factor**: 0.04
  - Can lower from base 0.077 to around 0.04 for better memory management
  - *From: neofuturo*

- **FFN chunking**: 2 chunks
  - Memory savings with minimal speed impact
  - *From: Kijai*

- **Steps for distill model**: 8 steps first stage + 4 steps second stage
  - Good balance of quality and speed
  - *From: Gleb Tretyak*

- **Preprocessing resize**: 1536
  - Optimal size for h.264 compression artifacts placement
  - *From: Zueuk*

- **ComfyUI launch parameters**: --reserve-vram 1 --disable-api-nodes
  - Memory optimization for Linux setup
  - *From: Gleb Tretyak*

- **IC-lora strength**: 0.5-0.7
  - Good balance for detail enhancement without excessive changes
  - *From: ▲*

- **Portrait resolution limit**: 640x1088 or below
  - Prevents artifacts at higher resolutions
  - *From: ucren*

- **FP16 accumulation**: Don't use on RTX 4090
  - Better performance without fp16 on high-end cards
  - *From: Kijai*

- **Minimum FPS for quality**: At least 48 FPS
  - Greatly improves image clarity and reduces ghosting
  - *From: BNP4535353*

- **Steps for 320p first pass**: 4 steps
  - Better preserves init image
  - *From: Kijai*

- **CFG for distilled model**: 1
  - Appropriate for distilled models
  - *From: protector131090*

- **Sampler**: res_2s
  - Recommended sampler choice
  - *From: Xor*

- **Resolution for quality**: 2560x1440
  - Needed for decent quality output, even though still not perfect
  - *From: protector131090*

- **Frame rate for motion blur workflow**: 60+ FPS
  - Higher FPS helps with motion blur processing
  - *From: protector131090*

- **Strength for controlnet**: Try 1.0 instead of 0.8
  - May help with skeletal/pose issues
  - *From: hicho*

- **QHD i2v 121 frames**: CFG 4, 20 steps, Res2s
  - Takes 200 seconds on 5090
  - *From: protector131090*

- **Optimized 5090 settings**: 121 frames, 40 steps, Euler ancestral, CFG 1, dev fp8
  - Took 186 seconds with undervolted 5090 at 60% power limit
  - *From: protector131090*

- **Chunk FFN optimization**: Only use 2 chunks
  - Using more than 2 chunks slows down sampling
  - *From: Kijai*

- **4K frame limit on 5090**: 33 frames maximum
  - Without tiled VAE, defaults to tiles after 33 frames
  - *From: protector131090*

- **I2V adapter strength**: 0.5
  - Better consistency to initial image than 1.0
  - *From: protector131090*

- **ComfyUI startup args for RTX 4090**: --preview-method none --reserve-vram 4
  - Prevents VRAM issues
  - *From: protector131090*

- **Scheduler**: linear_quadratic with shift 8
  - Equivalent to manual sigmas but native implementation
  - *From: Kijai*

- **Frame rate**: 60fps
  - Reduces motion artifacts compared to 24fps
  - *From: protector131090*

- **Audio normalization**: 0.25 at steps 3 and 6
  - Prevents clipping and improves audio quality
  - *From: Phr00t*

- **Memory use override**: 0.077
  - Default for LTX, provides optimal memory usage
  - *From: Kijai*

- **Steps for optimal quality**: 40 with Euler or 20 (double sampled) Res2s
  - Good recommended optimal number, too many steps will limit motion
  - *From: Volkin*

- **Audio normalization alternative values**: 0.4-0.5
  - Kijai found 0.25 too much dampening, these values work better
  - *From: Kijai*

- **Model Memory Usage Factor Override**: 3.0
  - Default 2.3 causes memory estimation errors
  - *From: Ablejones*

- **Denoise**: 0.4
  - Used in successful Wan22 LN run
  - *From: The Shadow (NYC)*

- **Context frames**: Adjustable based on hardware
  - Can adjust for better hardware
  - *From: The Shadow (NYC)*

- **Resolution divisibility**: Divisible by 64
  - Updated requirement from div by 32 to div by 64
  - *From: TK_999*

- **Distilled model CFG**: Use normalizing sampler
  - Regular CFG produces bad/burned outputs with distilled model
  - *From: David Snow*

- **Distill LoRA strength for 2-pass**: 0.6 first pass, 0.8 second pass
  - Prevents overcooked results in distilled model workflow
  - *From: N0NSens*

- **Attention multiply structural values**: 1.15 or 1.3
  - Can reduce artifacts and contrast, especially with hands
  - *From: Elvaxorn*

- **modality + skip step**: modality 1 + skip step 1
  - Sweet spot for speed + better consistency
  - *From: Volkin*

- **modality for tight control**: higher modality + 0 skip step
  - More constrained tight control, ideal for lipsync, character consistency, details
  - *From: Volkin*

- **ComfyUI startup arguments**: --cache-none
  - For memory issues, better than --novram
  - *From: Kijai*

- **VRAM usage for 10 seconds 720p**: 3-6 GB VRAM with --novram
  - 241 frames, can fit 900 frames at 1280x720p in 16GB VRAM
  - *From: Volkin*

- **Audio to video scale in attention tuner**: 1.2
  - Better audio synchronization, up from default 0.8
  - *From: David Snow*

- **Distill LoRA strength for dev fp8**: 0.6
  - Optimal balance when using dev model
  - *From: 🦙rishappi*

- **Dev model CFG settings**: CFG 4 for first pass, CFG 1 for second pass
  - Standard configuration for dev fp8 model
  - *From: protector131090*

- **WSL RAM allocation**: 76GB out of 96GB total
  - Prevents memory thrashing, was causing issues at 86GB
  - *From: burgstall*

- **CFG**: cfg 1 at 2nd stage vs cfg 4 at 2nd stage
  - Testing influence on second stage only
  - *From: protector131090*

- **Steps**: Minimum 40 steps for dev model or res2s with 20
  - Better quality results
  - *From: Volkin*

- **Scheduler**: LCM + linear_quadratic with beta scheduler
  - Best sampler combination results
  - *From: N0NSens*


## Concepts Explained

- **NAG**: Normalized Attention Guidance - helps with still images by adding 'still image with no motion' in prompt
  - *From: Abyss*

- **LTX2 metadata config**: LTX2 models rely on metadata config so every loader loading them needs to be up to date
  - *From: Kijai*

- **FFN chunking**: Feed-forward network chunking for memory optimization during sampling
  - *From: Kijai*

- **Tiny VAE**: Approximate VAE for preview generation during sampling
  - *From: nikolatesla20*

- **LTX preprocessing**: Applies h.264 codec compression at 1536 resolution to create motion artifacts for the model
  - *From: The Shadow (NYC)*

- **Audio_scale vs audio_to_video_scale**: Audio_scale affects the audio itself, audio_to_video affects the audio's effect on the video
  - *From: Kijai*

- **Frame_idx in guide nodes**: Position ID for guide image that tells the model what frame it should affect
  - *From: Kijai*

- **IC-lora workflow**: Uses guides and adds latents to the end, requiring twice the computational work
  - *From: Kijai*

- **8n+1 rule for temporal size**: LTX Video requires temporal dimensions to follow 8n+1 pattern, unlike standard multiples of 2
  - *From: ucren*

- **Pixel motion blur**: Blurs only the pixels that are in motion, not the entire image like standard blur
  - *From: protector131090*

- **256 rank LoRA**: High rank LoRA that might as well be a fine tune - this one was 5GB in size
  - *From: Fill*

- **IC LoRA**: Image conditioning LoRAs that are clumsy to use and highly inefficient for inference but fast to train
  - *From: Kijai*

- **Max projection method**: Method for mask pooling that should be used for video models in general
  - *From: Ablejones*

- **Scene graphs**: Better conditioning mechanism than natural language for AI models
  - *From: mallardgazellegoosewildcat2*

- **Audio-to-video and video-to-audio attention**: Cross-modal attention mechanisms in LTX2 that can be separately controlled in LoRAs
  - *From: Phr00t*

- **Distill connector vs distill LoRA**: Different methods with different results - distill model has layers that LoRA doesn't have
  - *From: Kijai*

- **Audio normalization in LTX**: Scales the audio part of the latent at specific steps to prevent audio becoming too strong which disturbs the video
  - *From: Kijai*

- **Inplace operations**: Memory optimization technique that modifies tensors in place, but different methods like addcmul_ can produce different outputs due to broadcasting differences
  - *From: Kijai*

- **Frame-Stride Diffusion**: Process only keyframes (e.g., 1 out of 4), interpolate the rest
  - *From: mallardgazellegoosewildcat2*

- **Noise-level experts**: Different models used at different noise levels, like Wan2.2 architecture
  - *From: mallardgazellegoosewildcat2*

- **IC LoRA**: Identity Consistency LoRA for maintaining character consistency across frames
  - *From: Alisson Pereira*

- **Skip layer/skip_blocks**: Parameter that affects model processing, value of 29 causes errors in T2V
  - *From: Volkin*

- **Modality scale**: Setting that affects audio/video processing, default appears to be 0
  - *From: Phr00t*

- **Guider parameters**: New nodes that modify CFG logic to provide better control, need separate nodes for audio and video
  - *From: Volkin*

- **Debaking**: Using negative LoRA values to reduce overcooked/burned appearance in distilled models
  - *From: hudson223*

- **Skip steps in new nodes**: Should never be higher than modality value or you get default LTX2 behavior prior to new nodes
  - *From: Volkin*

- **Page file**: Virtual file which serves as substitute for RAM memory, but slower. Essential for running LTX-2 workflows
  - *From: Volkin*

- **Pinned memory**: CUDA page-locked host memory for transfers and model caching
  - *From: buggz*

- **Manual sigmas vs scheduler**: Can use LTXV scheduler instead of manual sigmas for easier setup
  - *From: David Snow*

- **Distill LoRA usage**: Even with 100+ steps on dev model, distill LoRA is needed for usable results
  - *From: protector131090*

- **Mel spectrogram**: Audio processing method used by LTX2 internally instead of wav2vec or whisper bands, allows full spectrum conditioning
  - *From: Chandler ✨ 🎈*

- **Cond dict**: Can include model specific parameters, but encoded embeds should be normal text encoder output
  - *From: Kijai*


## Resources & Links

- **Tiny VAE for LTX** (model)
  - https://github.com/madebyollin/taehv/blob/main/safetensors/taeltx_2.safetensors
  - *From: TK_999*

- **LTX-2 GGUF Workflows** (workflow)
  - https://huggingface.co/RuneXX/LTX-2-Workflows/blob/main/LTX-2%20-%20I2V%20Basic%20(GGUF).json
  - *From: Jemmo*

- **Flippin Rad Motion Morph LoRA** (lora)
  - https://drive.google.com/file/d/1w3I8r7l_qtikYMRhcQq9T8j3QTrKH07C/view?usp=drive_link
  - *From: Flipping Sigmas*

- **Gemma text encoder GGUF** (model)
  - https://huggingface.co/unsloth/gemma-3-12b-it-GGUF/tree/main
  - *From: Lodis*

- **Gemma QAT GGUF (compatible)** (model)
  - https://huggingface.co/unsloth/gemma-3-12b-it-qat-GGUF/tree/main
  - *From: boop*

- **SageAttention Windows wheels** (tool)
  - https://github.com/woct0rdho/SageAttention/releases
  - *From: Kijai*

- **Official LTX-2 I2V workflow** (workflow)
  - https://github.com/Lightricks/ComfyUI-LTXVideo/blob/master/example_workflows/LTX-2_I2V_Full_wLora.json
  - *From: The Shadow (NYC)*

- **VRGameDevGirl workflows** (workflow)
  - https://github.com/vrgamegirl19/comfyui-vrgamedevgirl
  - *From: VRGameDevGirl84(RTX 5090)*

- **PyTorch CUDA memory documentation** (documentation)
  - https://docs.pytorch.org/docs/stable/torch_cuda_memory.html
  - *From: Kijai*

- **ComfyUI-LTX2-MultiGPU nodes** (tool)
  - https://github.com/dreamfast/ComfyUI-LTX2-MultiGPU
  - *From: LarpsAI*

- **SageAttention 1.0.6** (package)
  - https://pypi.org/project/sageattention/
  - *From: scf*

- **ComfyUI-AudioTools** (tool)
  - https://github.com/Urabewe/ComfyUI-AudioTools
  - *From: U̷r̷a̷b̷e̷w̷e̷*

- **Retro 90s Anime Golden Boy Style LoRA** (model)
  - https://civitai.com/models/2334302/retro-90s-anime-golden-boy-style-lora-ltx2?modelVersionId=2627789
  - *From: ucren*

- **Studio Ghibli LTX2 Style LoRA** (model)
  - https://civitai.com/models/2335739/studio-ghibli-ltx2-style-lora?modelVersionId=2627385
  - *From: ucren*

- **KYNode audio automation** (repo)
  - https://github.com/yorkane/ComfyUI-KYNode/tree/main
  - *From: hudson223*

- **Motion LoRA for LTX2** (model)
  - https://drive.google.com/file/d/1nOYVkQMcRcvv-XMZbWOGugX0YNJqlGUw/view?usp=sharing
  - *From: Flipping Sigmas*

- **ComfyUI-AudioTools** (repo)
  - https://github.com/Urabewe/ComfyUI-AudioTools
  - *From: U̷r̷a̷b̷e̷w̷e̷*

- **LTX2 distilled vs dev comparison** (comparison)
  - https://www.reddit.com/r/StableDiffusion/comments/1qatuni/ltx219bdistilled_vs_ltx219bdev_distilledlora/
  - *From: Kevin "Literally Who?" Abanto*

- **Comedy video made with LTX** (example)
  - https://youtu.be/jKHX8YBBFg0
  - *From: protector131090*

- **Audio to video extension workflow** (workflow)
  - https://github.com/purzbeats/purz-comfyui-workflows/blob/main/ltx2/ltx2-audio_to_video_extension_5x.json
  - *From: jab*

- **FlashVSR for video upscaling** (tool)
  - *From: Kiwv*

- **LTX-2 Image2Video Adapter LoRA** (model)
  - https://huggingface.co/MachineDelusions/LTX-2_Image2Video_Adapter_LoRa/tree/main
  - *From: Fill*

- **IC Pose workflow** (workflow)
  - https://huggingface.co/RuneXX/LTX-2-Workflows/blob/main/LTX-2%20-%20I2V%20IC-Control%20(pose).json
  - *From: Kevin*

- **ComfyUI split sampling fix** (repo)
  - https://github.com/Comfy-Org/ComfyUI/pull/12089
  - *From: Kijai*

- **LTXV-DoEverything-v2.json merging script** (script)
  - https://huggingface.co/Phr00t/LTX2-Rapid-Merges/blob/main/LTXV-DoEverything-v2.json
  - *From: Phr00t*

- **WAN upscaling example comparison** (example)
  - https://cdn.discordapp.com/attachments/1461011216578248907/1465359027780194470/LTX-2-Wan-SharkSampling_Compare_00016-audio.mp4
  - *From: pom*

- **KJNodes repository with LTX fixes** (repo)
  - https://github.com/kijai/ComfyUI-KJNodes/blob/fec6f48795e5870d695ebf13d949965e3a7c10ed/nodes/ltxv_nodes.py#L1094
  - *From: Kijai*

- **Commit with addcmul_ fix** (repo)
  - https://github.com/kijai/ComfyUI-KJNodes/commit/fec6f48795e5870d695ebf13d949965e3a7c10ed
  - *From: Kijai*

- **LTX-2 Workflows collection** (workflow)
  - https://huggingface.co/RuneXX/LTX-2-Workflows/discussions/9#697837f57e15e20d6046e8eb
  - *From: Kevin "Literally Who?" Abanto*

- **LTX2 Rapid Merges** (model)
  - https://huggingface.co/Phr00t/LTX2-Rapid-Merges
  - *From: David Snow*

- **ComfyUI LTX2 Efficient** (repo)
  - https://github.com/kakachiex2/comfyui-ltx2-efficient
  - *From: hicho*

- **MOVA model** (model)
  - https://huggingface.co/OpenMOSS-Team/MOVA-720p
  - *From: Ada*

- **LTX2 quality issues writeup** (guide)
  - https://www.reddit.com/r/StableDiffusion/comments/1qqewis/bad_ltx2_results_youre_probably_using_it_wrong/
  - *From: Phr00t*

- **LTX blog post** (documentation)
  - https://ltx.io/model/model-blog/ltx-2-better-control-for-real-workflows
  - *From: The Shadow (NYC)*

- **Execution Inversion Demo** (repo)
  - https://github.com/BadCafeCode/execution-inversion-demo-comfyui
  - *From: BitPoet (Chris)*

- **LTX 2 model blog** (documentation)
  - https://ltx.io/model/model-blog/ltx-2-better-control-for-real-workflows
  - *From: Volkin*

- **LTXV2 ComfyUI VAE** (model)
  - https://huggingface.co/Kijai/LTXV2_comfy/tree/main/VAE
  - *From: Volkin*

- **TaeLTX VAE for previews** (model)
  - https://github.com/madebyollin/taehv/blob/main/safetensors/taeltx_2.safetensors
  - *From: TK_999*

- **MOVA model repository** (repo)
  - https://github.com/OpenMOSS/MOVA
  - *From: TK_999*

- **LTX2 API access** (model)
  - https://ltx.io/model/model-blog/ltx-2-better-control-for-real-workflows
  - *From: The Shadow (NYC)*

- **MelBandRoFormer nodes** (repo)
  - https://github.com/kijai/ComfyUI-MelBandRoFormer
  - *From: Kijai*

- **MOVA audio video model** (model)
  - https://mosi.cn/models/mova
  - *From: dj47*

- **LTX-2-19b-IC-LoRA-Union-Control** (model)
  - https://huggingface.co/Lightricks/LTX-2-19b-IC-LoRA-Union-Control
  - *From: Draken*

- **Low memory tutorial** (tutorial)
  - https://www.youtube.com/watch?v=ub-1pBrAd9U
  - *From: garbus*

- **Tiny VAE for previews** (model)
  - https://huggingface.co/Kijai/LTXV2_comfy/blob/main/VAE/taeltx_2.safetensors
  - *From: David Snow*

- **ComfyUI Ollama nodes for vision** (node)
  - https://github.com/stavsap/comfyui-ollama
  - *From: AJO*

- **RunComfy Ollama vision node** (node)
  - https://www.runcomfy.com/comfyui-nodes/comfyui-ollama/OllamaVision
  - *From: AJO*

- **YouTube setup tutorial** (tutorial)
  - https://www.youtube.com/watch?v=ub-1pBrAd9U
  - *From: David Snow*

- **Updated workflow link** (workflow)
  - https://discord.com/channels/1076117621407223829/1459223128139104436/1467226444940841173
  - *From: The Shadow (NYC)*

- **Audio splitting analysis** (discussion)
  - https://discordapp.com/channels/1076117621407223829/1309520535012638740/1467057081155719189
  - *From: Chandler ✨ 🎈*

- **Working workflow from ucren** (workflow)
  - not provided
  - *From: nikolatesla20*


## Known Limitations

- **Audio latents cannot be split like video latents**
  - No way yet to split audio latents in same way as video, reason for audio extension limitations
  - *From: Zueuk*

- **FP4 model not compatible with LoRAs**
  - FP4 transformer only, just get 'lora key not loaded' with fp4 model
  - *From: boop*

- **Inconsistent prompt adherence**
  - LTX not consistently functional - default prompts work but custom prompts often fail to produce motion
  - *From: psylent_gamer*

- **Poor performance on abstract content**
  - Abstraction always came hard to LTX models
  - *From: N0NSens*

- **Direct high resolution generation produces poor results**
  - Going directly to 720p+ often results in tensor errors or degraded quality
  - *From: AJO*

- **Workflow automation fails with videos lacking audio**
  - Audio processing nodes crash when input video has no audio track, breaking batch processing
  - *From: ▲*

- **Set/Get nodes don't work through subgraphs**
  - Variable passing fails when nodes are in different subgraph contexts
  - *From: Kijai*

- **Model can't be forced to ignore voice-appearance correlations**
  - Sometimes produces specific accents based on visual appearance regardless of prompt instructions
  - *From: ucren*

- **Hard cap on input size**
  - Model breaks down after certain resolution/frame combinations
  - *From: Kijai*

- **Vertical format works worse**
  - LTX2 struggles more with vertical aspect ratios, especially T2V
  - *From: N0NSens*

- **IC-lora changes input image significantly**
  - Adds details that don't exist in original image, making it problematic for I2V
  - *From: Kijai*

- **Audio issues at very high resolutions**
  - 1920x1088x961f causes NaN audio errors, limited to ~10 seconds at 48fps instead of target 20 seconds
  - *From: BNP4535353*

- **Controlnet add guide node is very slow**
  - Much slower than normal inference due to VAE encoding requirements
  - *From: hicho*

- **Audio crashes with very long videos**
  - If increased beyond ~500 frames at 1920x1080, audio processing will crash
  - *From: BNP4535353*

- **Fast motion causes quality issues**
  - Hands moving at high speed and fast motion in general can cause problems for LTX
  - *From: David Snow*

- **Base model poor at I2V without tricks**
  - Standard LTX model with basic workflow produces little to no motion from still images
  - *From: Fill*

- **Quality issues with faces and hands**
  - Hands and faces remain problematic areas for the model
  - *From: Hevi*

- **Blurriness issues near fast-moving elements**
  - Fast moving hands and similar elements show weird blurriness artifacts
  - *From: AIGambino*

- **Portrait orientation poor performance**
  - LTX doesn't respond well to portrait, works better with 21:9 landscape
  - *From: David Snow*

- **High resolution memory constraints**
  - Model breaks with more frames at high resolution due to combined input size
  - *From: Kijai*

- **Color degradation at higher resolutions**
  - QHD and 4K sometimes lose color, hands become black and white
  - *From: protector131090*

- **Spatial inpainting unreliable**
  - Hit and miss, most of the time doesn't change anything in masked regions
  - *From: Kijai*

- **Audio desync with motion LoRAs**
  - LoRAs trained without audio cause lip sync issues
  - *From: Miku*

- **I2V adapter changes input image too dramatically at 1.0 strength**
  - Significantly alters face and appearance of original image
  - *From: protector131090*

- **Last frame issues unavoidable**
  - Final frames often have quality degradation
  - *From: David Snow*

- **Plastic skin appearance with Qwen image edit upscaling**
  - Upscaling gives unnatural plastic feel to skin
  - *From: David Snow*

- **System-dependent output variation**
  - Identical setups produce different results across different hardware/OS
  - *From: Kijai*

- **Robotic audio quality**
  - Generated audio sounds extremely robotic, far from production-ready
  - *From: Nekodificador*

- **Resolution and VRAM bottlenecks**
  - Lipsync appears blurry at low resolutions, need 1920x1080 for decent results which increases VRAM consumption
  - *From: Nekodificador*

- **Character consistency issues with motion**
  - Too much motion makes character inconsistent, needs last frame for better results
  - *From: Gleb Tretyak*

- **Poor pose copying fidelity**
  - LTX 2 IC Pose LoRA doesn't copy movement as well as SCAIL
  - *From: Kevin "Literally Who?" Abanto*

- **Model sensitivity to small changes**
  - Very sensitive to smallest changes, even tiny code differences can change outputs significantly
  - *From: Kijai*

- **HuMo can't do FHD even with low context_window**
  - Memory limitations prevent full HD generation
  - *From: N0NSens*

- **Fade to black common with model**
  - Usually accompanied by audio fading, happens often when using audio input that goes silent towards end
  - *From: Kijai*

- **Model struggles to pronounce certain words like 'zone'**
  - Audio generation has pronunciation issues
  - *From: David Snow*

- **Fast motion creates artifacts and watery effect**
  - Fast things are full of artifacts, smudged faces when they move around
  - *From: Alisson Pereira*

- **New Multimodal Guider causes 3x slowdown**
  - Even with CFG 1 with distilled models, nearly 2-3x slower
  - *From: Phr00t*

- **Black video output when going above 720p on certain hardware**
  - RTX 6000 produces black videos above 720p
  - *From: Purz*

- **New guider nodes don't work with distilled models**
  - Guider modifies CFG logic but distilled models don't use CFG
  - *From: Benjimon*

- **T2V doesn't work properly with new nodes**
  - Only I2V works correctly, T2V has errors and may need ComfyUI update
  - *From: Volkin*

- **Temporal attention multiply has no effect on LTX2**
  - LTX2 doesn't have time_stack layers so temporal settings don't affect anything
  - *From: Kijai*

- **Voice training requires significant dataset**
  - 15 videos/81 frames too few for voice training, need at least 30 videos or 10+ minutes of audio
  - *From: crinklypaper*

- **FP4 model has decreased motion and crumbly output**
  - FP4 version produces lower quality with motion issues
  - *From: VK*

- **No Image Reference to Video capability**
  - Reference to Video is one of the main things LTX currently can't do
  - *From: Elvaxorn*

- **Complex dialogue prompts not handled well**
  - LTX2 struggles with back-and-forth dialogue and character interactions, even simple character swapping scenarios
  - *From: N0NSens*

- **Portrait resolution limitations**
  - LTX2 is limited in portrait resolutions, breaks after some threshold. Use landscape format instead
  - *From: scf*

- **Color loss at high resolutions**
  - Semi black and white effect happens when resolution is too high
  - *From: protector131090*

- **Q3 model quality issues**
  - Q3 models produce heavily garbled noisy output
  - *From: David Snow*

- **Vertical/portrait format poor performance**
  - 9:16 aspect ratio causes static results, color shifts, motion issues - team working on fix
  - *From: Charlie, David Snow, AJO*

- **Character LoRAs cause unwanted character summoning**
  - Training anime LoRA on character clips for motion causes character to appear instead of just motion style
  - *From: protector131090*

- **Dev model requires distill LoRA**
  - Dev model produces unusable results without distill LoRA even at 100+ steps
  - *From: protector131090*

- **Character face consistency issues**
  - Unless using character LTX2 lora, model won't hold face from input images on each scene
  - *From: AJO*

- **Memory efficient sageattn incompatible with multimodal guider**
  - Causes crashes when used together
  - *From: Gleb Tretyak*

- **Layer skip (perturbed attention) broken for T2V**
  - Doesn't work even with skip layer turned off for text-to-video
  - *From: Jonathan Scott Schneberg*


## Hardware Requirements

- **CUDA 130**
  - cu130 torch is important, nvfp4 won't work without cu130
  - *From: Kijai*

- **24GB VRAM fits full model**
  - Full model fits in 24GB VRAM completely loaded
  - *From: dj47*

- **System RAM usage**
  - Uses up to 70GB system RAM when offloading, 80GB during generation
  - *From: jab*

- **VRAM usage with chunking**
  - First stage: 12.721GB allocated, 12.969GB reserved. Second stage: 10.355GB allocated, 11.156GB reserved (with chunking)
  - *From: Gleb Tretyak*

- **VRAM usage without chunking**
  - First stage: 12.860GB allocated, 13.188GB reserved. Second stage: 10.877GB allocated, 12.062GB reserved (without chunking)
  - *From: Gleb Tretyak*

- **GPU compatibility for fp8**
  - fp8 works better on 40xx cards, older GPUs should use fp16 with model compute dtype node
  - *From: Kijai*

- **Performance on 3090**
  - GGUF Q8 model reduces inference from 30s to 20s per step with proper settings
  - *From: ▲*

- **VRAM for IC workflows**
  - IC workflows double latent count, requiring more VRAM
  - *From: Kijai*

- **FP16 accumulation compatibility**
  - Requires PyTorch 2.7.1 or higher for fp16 accumulation
  - *From: randomanum*

- **RTX 5090 performance**
  - 90 seconds per 9-second V2V generation
  - *From: Kevin "Literally Who?" Abanto*

- **RTX 2060 limitations**
  - Slower performance due to VAE casting to fp32, fp16 not working
  - *From: hicho*

- **15 seconds for 40s first pass**
  - Fast generation time for initial 320p pass
  - *From: Kijai*

- **Training hardware**
  - A6000 Pro used for about a week to train 30,000 videos
  - *From: Fill*

- **High resolution requirements**
  - 2560x1440 needed for decent quality, requires RTX 5090 level VRAM
  - *From: protector131090*

- **4K generation on RTX 5090**
  - Can handle 33 frames in 4K without tiled VAE, needs 96GB RAM for optimal performance
  - *From: protector131090*

- **QHD performance on RTX 5090**
  - 121 frames takes 186-200 seconds with undervolted card at 60% power limit
  - *From: protector131090*

- **Memory for longer 4K**
  - Could potentially do 4K 121 frames on 5090 if memory leaks were fixed
  - *From: protector131090*

- **RTX 4090 VRAM capacity**
  - Can handle 1280x1280 for 1000 frames, 1920x1080 for 121 frames with fp8
  - *From: Kijai*

- **VRAM usage recommendations**
  - Use fp8 instead of GGUF on RTX 4090, reserve 4GB VRAM with startup args
  - *From: Kijai*

- **PyTorch CUDA version**
  - Need cu130 or higher for optimized CUDA operations
  - *From: triquichoque*

- **ComfyUI version compatibility**
  - Version 0.11 may cause quality issues, 0.10.0 more stable
  - *From: Volkin*

- **Minimum RAM for LTX-2**
  - 16GB RAM not sufficient, minimum-optimal recommended is 64GB+, can substitute with 64GB+ swap/pagefile but will be very slow
  - *From: Volkin*

- **5080 16GB performance**
  - Will perform amazingly well with enough RAM (64GB+)
  - *From: Volkin*

- **Full resolution requirements**
  - For 1920x1080p 15+ seconds: need 16GB VRAM + 64GB RAM with --novram flag
  - *From: Volkin*

- **SSD wear considerations**
  - Modern drives like 990 Pro have ~2400 TBW warranty, swapping for AI workloads causes gradual wear but typically manageable
  - *From: Kijai*

- **16GB VRAM / 64GB RAM**
  - System specs for running tiled UHD setup
  - *From: N0NSens*

- **A4500 with 20g VRAM and 28g SysRam**
  - Successfully runs context frames and block swap settings
  - *From: The Shadow (NYC)*

- **bf16 suitable for 30xx+ GPUs**
  - fp32 needed for older video cards, bf16 works on newer GPUs
  - *From: Xor*

- **VRAM for 1080p 15sec generation**
  - 6GB VRAM for rendering 1080p 15-second video
  - *From: Volkin*

- **High-end GPU performance**
  - 2560x1440 generation works on RTX 4090
  - *From: David Snow*

- **Hardware consistency issues**
  - Different results between RTX 4090 and RTX 5090 with same workflow
  - *From: protector131090*

- **VRAM usage**
  - Can do 1000 frames at 1280x1280 I2V. 720p 10 seconds (241 frames) uses 3-6GB VRAM with --novram. Can fit 900 frames at 1280x720p and 400 frames at 1080p in 16GB VRAM
  - *From: Volkin*

- **RAM requirements**
  - FP16 video model + FP4 text encoder: 50GB max RAM. FP4 + FP4: 25GB RAM. 32GB RAM can work with proper settings and fp4 models
  - *From: Volkin*

- **12GB VRAM compatibility**
  - Can run with fp4 models, --cache-none, and proper configuration. May need upscaling workflow
  - *From: multiple users*

- **Page file necessity**
  - Essential even with 64GB RAM on Windows for LTX-2 workflows
  - *From: Ablejones*

- **Minimum GPU capability**
  - People running LTX2 successfully on 8GB GPUs, 24GB RTX 3090 easily sufficient
  - *From: David Snow*

- **VRAM usage variability**
  - Same generation sometimes uses 98% VRAM, sometimes 81%, inconsistent behavior
  - *From: Charlie, David Snow*

- **Memory allocation for WSL**
  - 86GB RAM allocation to WSL caused thrashing, 76GB optimal for 96GB total system RAM
  - *From: burgstall*

- **16GB VRAM can run FP16**
  - Can do 1920x1080 15-20 seconds on 16GB VRAM by offloading model to RAM
  - *From: Volkin*

- **Full model loading**
  - 36GB loaded completely to GPU (35997.23 MB loaded, full load: True)
  - *From: buggz*

- **5090 with 128GB RAM**
  - User configuration for 1920x1920 generation with ltx-2-19b-dev
  - *From: Hell G.*


## Community Creations

- **Flippin Rad Motion Morph LoRA** (lora)
  - LoRA trained on motion morph dataset producing interesting morphing effects
  - *From: Flipping Sigmas*

- **Custom LoRA by neofuturo** (lora)
  - Custom trained LoRA working at 0.4-0.6 strength, available soon
  - *From: neofuturo*

- **ComfyUI-AudioTools** (nodes)
  - Audio enhancement and normalization nodes for LTX2, includes enhance and normalize functions
  - *From: U̷r̷a̷b̷e̷w̷e̷*

- **ComfyUI-LTX2-MultiGPU** (nodes)
  - Multi-GPU support nodes for LTX2 with CPU offloading capabilities
  - *From: LarpsAI*

- **Motion LoRA with 'ltxable motion' trigger** (lora)
  - 3GB high rank LoRA for steerable motion outputs in image-to-video generation
  - *From: Flipping Sigmas*

- **Auto audio muxing node** (node)
  - Checks video for audio and automatically muxes if missing
  - *From: hudson223*

- **Custom I2V trained LoRA** (lora)
  - 256 rank LoRA trained on 30,000 videos to improve I2V motion generation, 5GB size
  - *From: Fill*

- **SRT timestamp workflow feature** (workflow)
  - Allows using SRT subtitle files with timestamps to target specific video sections
  - *From: VRGameDevGirl84(RTX 5090)*

- **Tiled audio VAE decode in parts** (node)
  - Decodes audio in 3 parts to avoid VRAM issues
  - *From: Xor*

- **LTX frames cheat sheet calculator** (workflow)
  - Automated frame calculation to avoid manual reference checking
  - *From: garbus*

- **LTX-2 Image2Video Adapter LoRA** (lora)
  - Substantially improves i2v generation quality with direct image embedding pipeline
  - *From: Fill*

- **Motion LoRA for LTX** (lora)
  - Helps with animatediff motion, better than before for ltxable motion
  - *From: Flipping Sigmas*

- **Taichi particle fork with mask emission** (tool)
  - Added mask emission feature for particle effects
  - *From: burgstall*

- **Audio-video separated LoRA merging script** (script)
  - Allows applying different strengths to audio and video components during LoRA merging
  - *From: Phr00t*

- **LTX LoRA Advanced node** (node)
  - Allows disabling audio layers and adjusting individual layer/block strengths in LoRAs
  - *From: Kijai*

- **Chunked Feed Forward Node** (node)
  - Saves significant VRAM (~1GB at 720p for Wan, more for LTX)
  - *From: Kijai*

- **Memory Use Override Node** (node)
  - Allows fine control of VRAM allocation, helps prevent OOM errors
  - *From: Kijai*

- **Multi LoRA Loader Node** (node)
  - Advanced LoRA loading with multiple controls, works with all LTX 2 LoRAs
  - *From: Kijai*

- **IC LoRA for head swap** (lora)
  - Copies movements from reference video, requires first frame with new head
  - *From: Alisson Pereira*

- **Updated workflow with TorchCompile toggle** (workflow)
  - Context frames and block swap settings adjustable, TorchCompile can be toggled
  - *From: The Shadow (NYC)*

- **phr00tmerge-sfw-v5** (model)
  - Includes i2v lora adapter and detailer
  - *From: Phr00t*

- **Attention tuner patch node** (node)
  - Forces output results from before ComfyUI 0.11 due to inplace operations changes
  - *From: Kijai*

- **Frieren LoRA** (lora)
  - Anime LoRA trained on Frieren clips, but causes character summoning instead of motion style
  - *From: protector131090*

- **Fill's character LoRA** (lora)
  - Character LoRA retrained on Z-Image base instead of turbo, makes huge difference and cheaper to train
  - *From: AJO*

- **Story Writer** (workflow)
  - Uses QWEN VL node to generate stories and QWEN TTS friendly character descriptions up to 4 characters
  - *From: manu_le_surikhate_gamer*


---

# LTX Training - January 2026

# Ltx Training Knowledge Base
*Extracted from Discord discussions: 2026-01-01 to 2026-02-01*


## Technical Discoveries

- **LTX v1 LoRAs work with LTX-2**
  - Existing LTX v0.96/v1 LoRAs are compatible with LTX-2, visually anyway but audio doesn't get affected
  - *From: Fill*

- **LTX-2 training is significantly faster than other models**
  - What used to take over 20 hours on Wan2.2 now takes 1 hour on LTX-2. Training is lightning fast compared to previous video models
  - *From: oumoumad*

- **Training stalls after 1.5k steps with minor changes**
  - Character training progresses quickly up to 1.5k steps then progress becomes very minor, may need higher learning rate
  - *From: boorayjenkins*

- **5x-10x training speedup possible**
  - Reference to hydraulic press LoRA trained at home in 15 hours with significant speedup methods
  - *From: yi*

- **FP8 vs BF16 makes huge difference in quality**
  - Training on FP8 produces worse results, using BF16 for inference shows huge quality improvement
  - *From: NebSH*

- **Less character bleeding compared to Wan**
  - LTX-2 doesn't seem to overfit other characters like Wan does
  - *From: NebSH*

- **LTX-2 converges faster than LTX-1**
  - Model seems to converge in 1500 steps vs 2000 steps for LTX-1
  - *From: NebSH*

- **Multi-character training in single LoRA works**
  - Successfully trained 2 characters in one LoRA, though using them separately in generation causes mixing
  - *From: NebSH*

- **Sequential training approach works well**
  - 5000 steps on video data -> 2000 steps on image data -> 1400 steps on NSFW image data produces good results
  - *From: crinklypaper*

- **Audio-only training modifications improve LoRA**
  - Excluding cross attention keys between audio and video from trained LoRA improved results while keeping visual and audio concepts intact
  - *From: mamad8*

- **Model learns background music quickly**
  - After adding clips with same background music captioned as 'background music: ...', model learned the songs after just 2k steps
  - *From: dischordo*

- **Training order can be video first then images or images first then video - both work**
  - Images kick start style pickup much faster, but videos are better for voice training plus style
  - *From: crinklypaper*

- **Image-only training for animated styles is insufficient**
  - Gets the look somewhat but movement creates issues, probably because base model is missing that context
  - *From: crinklypaper*

- **Mixed video+image training produces best results**
  - Video + image training had best results compared to video only, image only, or image + video
  - *From: crinklypaper*

- **AI Toolkit supports mixed image+video training for LTX2**
  - Can have separate datasets - mark image datasets as 1f and it works fine. Bug that treated 1f datasets as i2v was fixed
  - *From: MOV*

- **LTX2 can learn character voices from small amounts of data**
  - At 1000 steps was already getting correct voice, even accidental 2-3 clips with audio taught Japanese accent
  - *From: Choowkee*

- **Scene splitter script in LTX trainer works better than pyscene**
  - Built-in scene splitter is quite nice for preparing datasets
  - *From: crinklypaper*

- **LTX2 is exceptionally good at learning audio/voices**
  - Multiple users report impressive voice cloning results, with one user saying their 1500 sample LoRA sounds exactly like their wife
  - *From: NC17z*

- **Increasing FPS can improve video generation quality**
  - User found that simply increasing fps made their generation work better
  - *From: crinklypaper*

- **LTX2 captures physical motion well**
  - User reports that LTX captures jiggling motion that WAN needed specific training for
  - *From: crinklypaper*

- **Simple 'Anime style' caption separates character from style effectively**
  - Just like with WAN, adding 'Anime style' to captions helps separate character learning from style learning
  - *From: Choowkee*

- **Training can be done on 4090 with good performance**
  - Successfully trained on RTX 4090 at 5.23 sec/iter with no layer offloading, cache text embeddings, low vram setting
  - *From: chancelor*

- **Large datasets require significant cache space**
  - When caching text embeddings, each dataset item creates 376mb files, leading to 300GB+ storage needs for large datasets
  - *From: avataraim*

- **768x768 training resolution shows better results than 512x512**
  - Training at 768 resolution produces clearer, more detailed motion learning compared to lower resolutions, though requires more VRAM
  - *From: dischordo*

- **Higher FPS training reduces motion artifacts**
  - Training at 32fps shows fewer hand distortions and motion artifacts compared to lower fps training, even when generating at 24fps
  - *From: MOV*

- **Custom cropping centered on motion area improves training**
  - Cropping training data to squares centered on the area of motion works better than letting the model resize whole clips
  - *From: dischordo*

- **Float8 with 4-bit text encoder uses 24-28GB VRAM**
  - Training configuration allowing LTX2 training on consumer cards with reasonable VRAM usage
  - *From: crinklypaper*

- **Audio normalize feature fixes pitch distortion**
  - Using audio normalize in AI Toolkit fixed high-pitched voice distortion that occurred from FPS mismatches
  - *From: crinklypaper*

- **IC LoRA can perform head swapping in videos**
  - Identity Consistent LoRA trained with 200+ paired video samples can swap heads across video sequences
  - *From: Alisson Pereira*

- **Musubi-Tuner has much smaller cache files than AI-Toolkit**
  - AI-Toolkit creates 360MB cache files per text encoder while Musubi-Tuner creates only 30MB cache files
  - *From: avataraim*

- **Recent Musubi-Tuner commits broke training**
  - Multiple users confirmed that newer commits fail to train properly, with bad loss curves and poor results
  - *From: Choowkee*

- **Older Musubi-Tuner commit works properly**
  - Commit 90e1559a7c73ff41ade497605e1f5b1850270711 produces proper loss curves and good results
  - *From: Choowkee*

- **Block swapping affects VRAM usage significantly**
  - 30 blockswap uses 18.6GB max VRAM, 26 blockswap uses 21.6GB, 24 blockswap uses 22.9GB for 512res 121f videos
  - *From: MOV*

- **High pitch voice issue can be fixed with audio preserve pitch setting**
  - Setting fps to match dataset and enabling audio preserve pitch fixed high pitch voices within 500 steps
  - *From: crinklypaper*

- **SDPA attention works better than Sage attention for training**
  - User switched from Sage attention to SDPA and got better training performance
  - *From: Choowkee*

- **LTX2 base resolution is 1280x720**
  - Model metadata shows modelspec.resolution: 1280x720 as base resolution
  - *From: Choowkee*

- **Musubi fork provides faster training than AI-toolkit**
  - User reported 2 it/s on 256x256x169 with Musubi vs 3 it/s with AI-toolkit, but Musubi is actually faster overall
  - *From: JonkoXL*

- **Audio-only training works with proper setup**
  - Successfully trained voice cloning using only audio files with 5 sec duration
  - *From: Gleb Tretyak*

- **Spatial outpainting possible with IC LoRA**
  - User trained IC LoRA by removing parts of videos (making them black) as reference and original videos as target
  - *From: oumoumad*

- **Audio LoRA training successful with very small dataset**
  - Successfully trained with only 20 audio files, each 5 seconds long with simple phrases
  - *From: Gleb Tretyak*

- **YouTube shorts effective for training data**
  - YouTube shorts are great for cropping out everything but the person, creates better focus for training
  - *From: Jonathan Scott Schneberg*


## Troubleshooting & Solutions

- **Problem:** Fal trainer showing internal server error but training actually succeeds
  - **Solution:** Check logs for lora_file: url= line to download the trained LoRA, training didn't actually fail
  - *From: ZeusZeus (RTX 4090)*

- **Problem:** Audio causes OOM during preprocessing
  - **Solution:** Need to cleanup text encoder in preprocess script before moving to latent caching
  - *From: fearnworks*

- **Problem:** Triton dependency prevents Windows training
  - **Solution:** Can use triton-windows manually installed, though official trainer requires Linux
  - *From: AshmoTV*

- **Problem:** Slow motion effect when generating longer videos than training dataset
  - **Solution:** Include variation in dataset with same effect at different speeds and durations, use prompts mentioning timing like 'quick burst'
  - *From: oumoumad*

- **Problem:** OOM on dataset preprocessing with 24GB VRAM
  - **Solution:** Need higher VRAM cards or use CPU preprocessing (very slow - 6 minutes for 3 second clip)
  - *From: crinklypaper*

- **Problem:** Quantization error with fp8 model
  - **Solution:** Set quantization to 'null' if using fp8 model since it's already fp8
  - *From: crinklypaper*

- **Problem:** Empty conditions folder during preprocessing
  - **Solution:** Change output_file = output_path / output_rel_path to output_file = output_path /'dataset'/ output_rel_path.name - issue with pathlib handling relative paths when folder named 'dataset'
  - *From: iGoon*

- **Problem:** Out of memory on longer frame training
  - **Solution:** Train on 5-6 seconds instead of 20 seconds, even on H100. 500 frames causes OOM
  - *From: NebSH*

- **Problem:** T2V produces floating heads and weird anatomy while I2V works fine
  - **Solution:** Consider adding high quality images to training data to improve T2V performance
  - *From: daring_ls*

- **Problem:** Audio captioning for engine sounds mixed with speech
  - **Solution:** Avoid putting descriptive text like 'There is a reving engine' as character will often say it literally
  - *From: vanhex*

- **Problem:** Black screen LoRA from training without samples
  - **Solution:** Take at least one sample at 250 steps to make sure it's not broken
  - *From: dischordo*

- **Problem:** Audio error 'Invalid argument: avcodec_send_frame() NaN/+-Inf' after ~6000 steps
  - **Solution:** Error goes away when removing audio but video becomes black. Doesn't happen at 5600 steps checkpoint
  - *From: Lumori*

- **Problem:** Multiple character voices combining into one
  - **Solution:** Need to tag each character specifically in SPEECH prompts and separate them properly in dataset
  - *From: Lumori*

- **Problem:** Slow training speed with full offloading
  - **Solution:** Reduce transformer offloading - went from 9s/it to 5s/it by offloading only 20% instead of 100%
  - *From: Critorio*

- **Problem:** AI Toolkit convergence issues with newer versions
  - **Solution:** Roll back to first release that supported LTX2 (Jan 13) for normal convergence
  - *From: Choowkee*

- **Problem:** Training on videos longer than expected frames
  - **Solution:** AI toolkit takes first 121f (or specified amount) and doesn't require exact length
  - *From: MOV*

- **Problem:** CUDA 13.0 compatibility issues with libnvrtc-builtins
  - **Solution:** Update cuda-toolkit from 12.8 to match the requirements
  - *From: burgstall*

- **Problem:** Poor training results even after 2000+ steps
  - **Solution:** Ensure source videos are proper aspect ratios (divisible by 32) to avoid cropping important content
  - *From: BrainNXDomain*

- **Problem:** Cache latent or additional resolution checkboxes causing issues
  - **Solution:** Disabling these checkboxes resolved training problems
  - *From: Mazrael.Shib*

- **Problem:** High loss starting above 1.0 and not dropping quickly
  - **Solution:** This indicates potential dataset or settings issues - healthy runs should start lower and drop gradually
  - *From: Choowkee*

- **Problem:** Running out of disk space with text embedding cache
  - **Solution:** Either get larger drive, split training into multiple sessions, or use unload text encoder method
  - *From: chancelor*

- **Problem:** High-pitched audio in generated videos
  - **Solution:** Set correct FPS in dataset settings and enable audio normalize feature, or use Audio Preserve Pitch option
  - *From: MOV*

- **Problem:** Poor I2V results when only training T2V
  - **Solution:** Add the same dataset twice, with I2V enabled on one copy to train both modes simultaneously
  - *From: MOV*

- **Problem:** Cache not updating after changing I2V settings
  - **Solution:** Delete _latent_cache and _t_e_cache folders in dataset directory to force recaching
  - *From: MOV*

- **Problem:** OOM errors on 5090 with 64GB RAM
  - **Solution:** Quantize transformers to float8 and set offload to 100%
  - *From: Jonathan Scott Schneberg*

- **Problem:** WSL2 Docker memory limitations on Win11 Home
  - **Solution:** Update WSL2 to break 100GB vxhd limitation, avoid Docker if possible and use direct WSL2 installation
  - *From: metaphysician*

- **Problem:** High pitch voices in generated audio
  - **Solution:** Set fps to same as dataset and enable audio preserve pitch
  - *From: crinklypaper*

- **Problem:** Training freezes when VRAM exceeds capacity
  - **Solution:** Some samples go up to 24GB and freeze, adjust block swap settings
  - *From: avataraim*

- **Problem:** Bad training results with newer Musubi-Tuner versions
  - **Solution:** Roll back to commit 90e1559a7c73ff41ade497605e1f5b1850270711
  - *From: Choowkee*

- **Problem:** OOM errors during training
  - **Solution:** Set blocks_to_swap to 5 and test what works for your setup
  - *From: avataraim*

- **Problem:** Sage attention causing training issues
  - **Solution:** Do not use sage attention during training, use SDPA instead
  - *From: Benjimon*

- **Problem:** Training results very poor with unstable repository versions
  - **Solution:** Use specific stable commit: 2b77b23defc40bea39ee21680fa3ab73765ab3bf
  - *From: avataraim*

- **Problem:** High VRAM usage when training with audio+video
  - **Solution:** Train video-only first to test, audio training requires more VRAM management
  - *From: avataraim*

- **Problem:** Poor voice cloning results
  - **Solution:** Need 20-30+ videos minimum for good voice cloning, not just 10 videos
  - *From: JonkoXL*

- **Problem:** Chrome occupying VRAM during training
  - **Solution:** Disable GPU acceleration in Chrome to free up VRAM
  - *From: scf*

- **Problem:** AdamW optimizer causing issues
  - **Solution:** User fixed training by not using AdamW optimizer
  - *From: Jimi*

- **Problem:** Musubi-tuner crashes with OOM on validation sampling
  - **Solution:** User gave up and switched to Simpletuner on Linux
  - *From: Gleb Tretyak*

- **Problem:** Simpletuner config path errors
  - **Solution:** Fix paths in config JSON - replace system-specific paths like '/home/gleb/.simpletuner/config/lycoris_config.json' with your own system paths
  - *From: Gleb Tretyak*

- **Problem:** LoRA trained for 4000 steps has basically 0 effect at 256 resolution
  - **Solution:** No solution provided - user asking if LTX2 can't be trained on 256 res, previously worked at 512 res
  - *From: protector131090*


## Model Comparisons

- **LTX-2 vs Wan2.2 training speed**
  - LTX-2 is dramatically faster - 1 hour vs 20+ hours for similar datasets
  - *From: oumoumad*

- **Character likeness LTX-2 vs Wan2.2**
  - Character likeness is less good than Wan 2.2, may need more steps or different precision
  - *From: NebSH*

- **128 rank vs 32 rank LoRAs**
  - 128 rank (ltx-trainer) yields nicer results without AI-ish chrome/metal particles, 32 rank less biased to texture changes
  - *From: oumoumad*

- **LTX-2 vs LTX-1 training speed**
  - LTX-2 is approximately 10x faster to train than WAN, but more sensitive
  - *From: crinklypaper*

- **FP16 vs FP8 generation quality**
  - FP16 always produces better results - smoother movement, higher quality, more details. Difference is like Veo3.1 vs Veo3.1 fast
  - *From: Tonon*

- **Dataset size impact**
  - Smaller datasets (108 videos) seem to converge faster than larger ones (830+ videos). Larger datasets may be too restrictive and slow down learning
  - *From: NebSH*

- **Official LTX trainer vs AI Toolkit**
  - Official trainer is better but annoying to use, AI Toolkit easier but came out recently so may have bugs
  - *From: Kiwv*

- **Musubi tuner vs AI Toolkit for LTX2**
  - Musubi faster (2it/s vs slower), 1.3it/s for pure video training
  - *From: Choowkee*

- **WAN 2.2 vs LTX2 training**
  - WAN seemed simpler (crop, keyword, train, ship), LTX2 more complex but can learn and generalize intelligently
  - *From: Kiwv*

- **Distilled vs base LTX2 model**
  - Distilled is fried with amalgamation and prompt deviation, base model has no issues
  - *From: Kiwv*

- **LTX2 vs WAN for audio learning**
  - LTX2 is significantly better at learning voices and audio
  - *From: Choowkee*

- **Different FPS settings for 2D content**
  - 24fps performed better than 48fps-60fps for 2D content in testing
  - *From: protector131090*

- **AI-toolkit vs Musubi tuner fork**
  - Musubi tuner provides more control over parameters and is faster for LTX2 training
  - *From: Choowkee*

- **Video+image datasets vs image-only**
  - Video datasets produce much more realistic results than image-only, especially for realism
  - *From: ZeusZeus (RTX 4090)*

- **Musubi tuner vs AI Toolkit speed**
  - Musubi tuner achieves 2.9s/iter with 10% offload vs slower performance in AI Toolkit
  - *From: scf*

- **Cache sizes: Musubi vs AI Toolkit**
  - Musubi produces cache files ~30MB vs AI Toolkit's 300+MB, 10x smaller
  - *From: avataraim*

- **Musubi-Tuner vs AI-Toolkit cache size**
  - Musubi-Tuner cache is 12x smaller (30MB vs 360MB per file)
  - *From: avataraim*

- **Musubi-Tuner vs AI-Toolkit speed**
  - Musubi-Tuner is faster: 11s/it vs 15s/it on same dataset
  - *From: MOV*

- **Musubi-Tuner vs AI-Toolkit for specific dataset**
  - Musubi-Tuner at 800 steps wins in both quality and audio for this test dataset
  - *From: avataraim*

- **Training samples vs ComfyUI results**
  - Samples during training are MUCH worse than actual LoRA performance in ComfyUI
  - *From: NebSH*

- **Musubi vs AI-toolkit for voice training**
  - Musubi produces better voice cloning results - good results in 800 steps vs poor results in AI-toolkit at 2K steps
  - *From: avataraim*

- **LTX2 vs WAN for eye generalization**
  - WAN 2.1 handles anime eye styles better than LTX2 on same dataset
  - *From: Choowkee*


## Tips & Best Practices

- **Use varied dataset for motion effects to avoid slow-mo bias**
  - Context: When training effect LoRAs, include same effect at different speeds and durations
  - *From: oumoumad*

- **Avoid mixing closeups and wide shots in single dataset**
  - Context: Models can get confused seeing closeups and wide views as separate subjects
  - *From: oumoumad*

- **Use first_frame_conditioning_p: 1.0 for product training**
  - Context: Key parameter for training LoRAs on objects like cars, specify only one frame for bucket preprocessing
  - *From: oumoumad*

- **2000 steps can cause overfitting with small datasets**
  - Context: Better results between 1000-1500 steps unless dataset has 24+ varied examples
  - *From: oumoumad*

- **Negative prompts are very important in LTX-2**
  - Context: Every word has impact, good for fixing issues and minimizing bias, unlike previous LTXV where negative prompts felt ineffective
  - *From: oumoumad*

- **Use BF16 instead of FP8 for better quality**
  - Context: FP8 training produces worse character likeness, BF16 inference shows huge quality difference
  - *From: NebSH*

- **Use detailed captions with shot-by-shot breakdown for longer videos**
  - Context: For videos 8-13 seconds with multiple actions or cuts, include overall description, then shot-by-shot breakdowns with audio description
  - *From: fearnworks*

- **Test captioning concept without LoRA first**
  - Context: Find prompts that get in vague ballpark to help identify right captioning approach
  - *From: fearnworks*

- **Use custom sigmas and specific sampler settings for I2V**
  - Context: Use undistilled model with distill LoRA at 0.5-0.6 strength, DPM SDE sampler, custom sigmas, 1.0 denoise strength, sometimes reduce precompression
  - *From: dischordo*

- **Checkpoint often and test locally instead of sampling during training**
  - Context: Sampling during training never looks right
  - *From: crinklypaper*

- **Tag music uniquely with actual song names rather than generic 'background music'**
  - Context: Generic tags cause different songs to mix together, especially bad if in different keys
  - *From: dischordo*

- **Normalize audio levels to around -7db**
  - Context: Model picks up full audio range, good level for training
  - *From: dischordo*

- **Include dialogue in Japanese as romaji in captions**
  - Context: Don't translate to English, write as 'sou desu ne' etc. and specify language
  - *From: crinklypaper*

- **Use diverse clips for concept training**
  - Context: Too few or similar clips cause model to learn unintended specifics like faces, expressions, colors
  - *From: SmaX*

- **Start with 512 res and 65 frames or 256 res and 121 frames for video**
  - Context: Good starting points for LTX2 video training
  - *From: MOV*

- **Don't overtrain - less steps can be better**
  - Context: User found 1500 step LoRA performed better than 6000 step version, suggesting overtraining can hurt results
  - *From: NC17z*

- **Use detailed captions for LTX2**
  - Context: LTX2 may need more detailed captions compared to other models due to DiT-based architecture
  - *From: Mazrael.Shib*

- **Mix images and videos for best results**
  - Context: 500 images + 100 videos combination works well for learning both style and character
  - *From: avataraim*

- **Consider rank size relative to dataset size**
  - Context: For 20 videos, rank 32 might be too much and could cause overfitting instead of generalization
  - *From: Kiwv*

- **Use keyframes for smoother motion**
  - Context: Multiple close keyframes with sufficient frames between them produces smoother results
  - *From: JUSTSWEATERS*

- **Train both T2V and I2V modes for best results**
  - Context: When planning to use LoRA for both text-to-video and image-to-video generation
  - *From: MOV*

- **Match training FPS to your dataset FPS**
  - Context: Prevents audio pitch distortion and timing issues during generation
  - *From: MOV*

- **Use rank 32 for most character LoRAs**
  - Context: Balance between learning capacity and overfitting for identity/character training
  - *From: MOV*

- **Pad frames minimally to fit bucket sizes**
  - Context: When preparing video datasets, pad maximum 2-3 frames to fit bucket requirements
  - *From: crinklypaper*

- **Generate lipsynced I2V for character training instead of interpolating stills**
  - Context: Preserves natural lipsync when training with audio clips
  - *From: MOV*

- **Use lower rank for character training with images**
  - Context: To avoid diminished movement and talking ability, try rank 4-8 instead of higher values
  - *From: Guey.KhalaMari*

- **Train character with multiple people in final stage**
  - Context: To counter the issue where LoRA makes everyone look like the trained character
  - *From: Guey.KhalaMari*

- **Don't rely on training samples for quality assessment**
  - Context: Samples are much worse than actual LoRA performance in ComfyUI
  - *From: NebSH*

- **Use 3 second clips around 73 frames for good results**
  - Context: For training with audio, this duration works well
  - *From: crinklypaper*

- **Use natural language captions, not keyword-based ones**
  - Context: For LTX2 training with LLM-based text encoders
  - *From: Kiwv*

- **Caption as if describing for the original LTX2 dataset**
  - Context: Better results than artificial keyword-style captions
  - *From: Kiwv*

- **Use consistent keywords throughout dataset**
  - Context: Don't mix 'car', 'automobile', 'racer' - pick one term and stick with it
  - *From: LTX Lux*

- **Audio clips should be 24fps to avoid audio issues**
  - Context: When preparing video datasets with audio
  - *From: crinklypaper*

- **Caption audio naturally at end of video captions**
  - Context: Use format like 'character says "dialogue"' and describe background sounds
  - *From: crinklypaper*

- **Aim for overtraining rather than undertraining**
  - Context: Model learns extremely slowly, need 150+ repeats per data point on average
  - *From: dischordo*

- **Use GUI for Simpletuner on Linux**
  - Context: When using Simpletuner
  - *From: Kiwv*

- **Sometimes editing config file directly is easier than using complex UI**
  - Context: When dealing with complex training interfaces
  - *From: scf*

- **Use YouTube shorts for training datasets**
  - Context: For character training - allows cropping out everything but the person for better focus
  - *From: Jonathan Scott Schneberg*


## News & Updates

- **LTX-2 trainer supports multiple training modes**
  - Standard LoRA Training (Video-Only), Audio-Video LoRA Training, Full Model Fine-tuning, In-Context LoRA (IC-LoRA) Training
  - *From: NebSH*

- **Fal.ai LTX-2 trainer available but image-only**
  - Fal trainer currently only supports images, not video training
  - *From: NebSH*

- **Audio training toggle available but needs tweaking**
  - Audio training option exists but default settings need adjustment, being worked on
  - *From: Dragonyte*

- **AI Toolkit now officially supports LTX-2 LoRA training**
  - Ostris announced official support and trained Carl Sagan LoRA on RTX 5090
  - *From: Arts Bro*

- **AI Toolkit added I2V training support**
  - Ostris pushed I2V training capabilities to AI Toolkit
  - *From: fearnworks*

- **VRAM usage reduction in AI Toolkit**
  - Recent commit allows proper caching of latents, drastically reducing VRAM usage during training
  - *From: MOV*

- **LTX2 training tutorial coming soon**
  - Finishing touches on tutorial, hope to have live in a day or so
  - *From: LTX Lux*

- **Official LTX2 training tutorial released**
  - Training Custom LoRAs with LTX-2 (Full Workflow) on YouTube
  - *From: LTX Lux*

- **Planned AI Toolkit improvements**
  - PRs coming for audio-only training, video+image training together, prodigyscheduler_free optimizer, multiple dataset folders with balancing, tensorboard logging
  - *From: mamad8*

- **Musubi tuner fork fixed audio-only datasets**
  - Audio-only training with dummy video was broken but has been fixed
  - *From: Gleb Tretyak*

- **LTX model had git commit pulled back causing re-downloads**
  - Recent git commit in LTX repo was reverted, causing users to see updates and re-download all files
  - *From: BrainNXDomain*

- **Musubi-Tuner LTX-2 fork available**
  - Fork by AkaneTendo25 supports LTX Video 2 training
  - *From: avataraim*

- **Recent Musubi-Tuner updates broke training**
  - Updates from last few days caused training failures, author working on fixes
  - *From: Choowkee*

- **Koyha working on official LTX training support**
  - Official support for LTX training coming to Musubi-Tuner soon
  - *From: JonkoXL*


## Workflows & Use Cases

- **Music video generation using camera control LoRAs**
  - Use case: Generate start images then run with LTXV 0.97 distilled 13B using randomly assigned camera control LoRAs
  - *From: burgstall*

- **Character dataset creation from interviews**
  - Use case: Use pyscene to extract clips from interviews - 10 min video becomes ~177 training clips
  - *From: NebSH*

- **Video-first then image training**
  - Use case: Train 5000 steps on videos first to get motion/sound, then continue with images to improve style accuracy
  - *From: crinklypaper*

- **Sequential dataset training**
  - Use case: 5000 steps video -> 2000 steps images -> 1400 steps specific content images for comprehensive character/style learning
  - *From: crinklypaper*

- **AMV-style video-to-video training**
  - Use case: Extract keyframes from AMV, repeat first frame until scene changes to create reference video for transition training
  - *From: Alisson Pereira*

- **Multi-stage training approach**
  - Use case: Train on videos first then switch to images, or vice versa, by stopping and resuming from checkpoint
  - *From: crinklypaper*

- **Character + environment training**
  - Use case: Train room separately with token, then person in room with both tokens, crop different shots for variety
  - *From: MOV*

- **Gemini captioning workflow**
  - Use case: Use Gemini with custom tool to caption video datasets including Japanese dialogue
  - *From: crinklypaper*

- **Image + Video dataset combination**
  - Use case: Training both style and character simultaneously using 500 images + 100 videos with audio
  - *From: avataraim*

- **Head swap IC LoRA training**
  - Use case: Training for face swapping by using head-swapped first frames with Humo processing at 0.7 denoise
  - *From: Alisson Pereira*

- **Multi-keyframe generation**
  - Use case: Using 4 keyframes with 25fps processing and 121 frames for smooth character motion
  - *From: JUSTSWEATERS*

- **Whisper + Qwen-VL captioning workflow**
  - Use case: Automated video captioning for training with speech transcription and visual description
  - *From: MOV*

- **IC LoRA head swap training**
  - Use case: Train identity-consistent LoRA for video head swapping using paired video samples
  - *From: Alisson Pereira*

- **Mixed dataset training**
  - Use case: Training with both videos (512x512, 73 frames) and images (768x768) for character LoRAs
  - *From: avataraim*

- **Character training with diverse dataset**
  - Use case: Using 94 images and 59 videos with audio for character LoRA, achieved good results at 3.5k-5k steps
  - *From: crinklypaper*

- **Audio-only training with Simpletuner**
  - Use case: Voice cloning using only audio files
  - *From: Gleb Tretyak*

- **Spatial outpainting with IC LoRA**
  - Use case: Remove parts of videos (make black) as reference, use originals as target for outpainting training
  - *From: oumoumad*

- **Audio 2 Audio with voice LoRA**
  - Use case: Provide audio source of intended performance and apply voice LoRA on top, using Kijai's node with audio trained on black frames and Video/Audio LoRA
  - *From: Guey.KhalaMari*

- **Repurposing character LoRAs for voice only**
  - Use case: Using existing character LoRAs but only extracting their voice component with Kijai's node
  - *From: Guey.KhalaMari*


## Recommended Settings

- **Learning rate**: 0.0002
  - Used successfully for tear effect LoRA training
  - *From: oumoumad*

- **Steps**: 1000-1500
  - Better results than 2000 steps unless dataset is very varied (24+ examples)
  - *From: oumoumad*

- **Resolution**: 512x different buckets
  - Used successfully for 121 frame video training in ~1 hour
  - *From: KevenG*

- **Frames**: 121 frames
  - Good balance of quality and training speed for video LoRAs
  - *From: KevenG*

- **Quantization**: null
  - Set to null if using fp8 model since it's already fp8, otherwise will error
  - *From: crinklypaper*

- **Rank**: 64-128
  - 128 rank produces better quality than 32 rank, but 32 rank less texture biased
  - *From: oumoumad*

- **learning_rate**: 1e-4 (default), 2e-5 for stability
  - 4e-4 is too high, 2e-5 recommended by Kiwv
  - *From: Kiwv*

- **rank and alpha**: 32
  - Standard setting used by multiple successful trainers
  - *From: NebSH*

- **first_frame_conditioning_p**: 0.5 for both T2V/I2V, 1.0 for I2V only, 0.0 for T2V only
  - 0.5 works for both modes, adjust based on desired capabilities
  - *From: mamad8*

- **training steps**: 1500 steps typical, sweet spot 7k-9k for style
  - LTX-2 converges faster than LTX-1, style accuracy peaks around 7k-9k steps
  - *From: NebSH*

- **resolution buckets**: 960x544x41 through 960x544x137
  - Standard resolution buckets used by successful trainers
  - *From: Cseti*

- **Frame count**: 121 frames at 25fps
  - Standard for LTX2, avoids slow motion/sped up issues
  - *From: SmaX*

- **Audio normalization**: -7db
  - Good level that model picks up well
  - *From: dischordo*

- **Transformer offloading**: 20% instead of 100%
  - Better speed (9s/it to 5s/it) without full VRAM usage
  - *From: Critorio*

- **Training resolution**: 5 second clips at 25fps for video
  - Recommended by AI-toolkit author, should match intended generation length
  - *From: SmaX*

- **Clip length variety**: 2-8 seconds acceptable
  - Won't completely mess up training, just affects learning
  - *From: amli*

- **Video resolution**: 768x512 (preferred), 512x512, 768x768, 1024x768
  - Must be divisible by 32 due to VAE spatial compression factor
  - *From: BrainNXDomain*

- **Training steps for small datasets**: 5000 steps
  - General recommendation, but stop when results look good
  - *From: Kiwv*

- **Frame count and resolution**: 512 resolution with 49 frames, or 256 resolution with 79 frames
  - Works well on 4090 with 18GB VRAM usage
  - *From: avataraim*

- **Rank for IC LoRA**: 128
  - Higher rank helped significantly for IC LoRA training compared to typical 64
  - *From: Alisson Pereira*

- **Video duration**: 2 seconds
  - Works well for cartoon/animated content training
  - *From: avataraim*

- **Resolution for consumer cards**: 512x512 at 121 frames
  - Fits in 24GB VRAM with slight headroom
  - *From: MOV*

- **768 bucket at 121 frames**: Works on A6000 without offloading
  - Provides better motion learning for unique concepts
  - *From: dischordo*

- **Audio scale**: Tested values: 0.75, 0.8, 0.85, 1.0, 1.5
  - Different values for lipsync intensity testing
  - *From: Mazrael.Shib*

- **Offload percentage**: 75% works, 100% recommended for 24GB cards
  - VRAM management for consumer hardware
  - *From: avataraim*

- **Rank**: 16-32 for identity LoRAs, 64+ for complex concepts
  - Balance learning capacity with overfitting prevention
  - *From: MOV*

- **rank**: 4-8 for character training
  - Higher ranks can cause diminished movement and talking ability
  - *From: Guey.KhalaMari*

- **learning_rate**: 1e-4 default
  - Standard rate, but may need adjustment for small datasets
  - *From: CJ*

- **blocks_to_swap**: 5-10 for 4090
  - Balance between VRAM usage and speed
  - *From: avataraim*

- **training steps**: 3k-8k steps
  - Sufficient for good results without overtraining
  - *From: Guey.KhalaMari*

- **blocks_to_swap**: 0 for RTX 5090, 5 for RTX 4090, 20+ for lower VRAM
  - VRAM optimization
  - *From: avataraim*

- **network_dim/network_alpha**: 32/32 recommended over 32/16
  - 32/16 gives horrible results in LTX2 unlike other models
  - *From: Choowkee*

- **learning_rate**: 1.5e-4
  - Used in working training configuration
  - *From: Jimi*

- **max_train_steps**: 400-800 steps for good results
  - Sufficient for character training with proper dataset
  - *From: avataraim*

- **audio duration**: 5 seconds for audio clips
  - Works well for voice cloning
  - *From: Gleb Tretyak*

- **video count for voice training**: 20-30+ videos minimum
  - 10 videos insufficient for good voice cloning
  - *From: crinklypaper*

- **Audio training dataset**: 20 audio files, 5 seconds each
  - Sufficient for basic audio LoRA training
  - *From: Gleb Tretyak*

- **Character LoRA training dataset**: 25 photos of a person with captions in txt
  - Standard dataset size for character training
  - *From: protector131090*


## Concepts Explained

- **In-Context LoRA (IC-LoRA)**: Training mode supported by LTX-2 for vid2vid pairs
  - *From: Persoon*

- **Bucket preprocessing**: Maximum bucket size limited by shortest video in dataset - if shortest video has 41 frames, that's the max bucket size even if other videos are longer
  - *From: oumoumad*

- **Multi frame conditioning**: LTX-2 feature that can help bias generation to desired outcomes
  - *From: oumoumad*

- **first_frame_conditioning_p**: Probability of using first frame as conditioning (0.0-1.0). Controls I2V vs T2V capability retention during training
  - *From: mamad8*

- **Frame bucket number**: Number after resolution (e.g. 89, 113) refers to frame count the model was trained on, not resolution bucket
  - *From: NebSH*

- **Cross attention keys exclusion**: Technique to exclude cross attention keys between audio and video modalities from trained LoRA, potentially improving results
  - *From: mamad8*

- **Frame count buckets**: System for organizing training data by frame counts, one of the training pitfalls to manage
  - *From: dischordo*

- **Audio normalization**: Process to standardize audio levels across training clips to avoid volume inconsistencies
  - *From: dischordo*

- **Resolution buckets**: 1920x1080 goes into 1536 bucket (1920+1080=3000, so ~1536x1536 square format)
  - *From: MOV*

- **Layer offloading**: Moving model layers between GPU and CPU RAM to save VRAM, affects training speed
  - *From: MOV*

- **DiT-based architecture**: LTX2 uses DiT (Diffusion Transformer) which may require different captioning approaches compared to non-DiT models like WAN
  - *From: Mazrael.Shib*

- **VAE spatial compression factor**: LTX2 uses compression factor of 32, requiring input dimensions to be divisible by 32
  - *From: BrainNXDomain*

- **IC LoRA**: Image Conditioning LoRA - trains with control and target video datasets to transform one type of video into another
  - *From: Alisson Pereira*

- **Text embedding cache**: Creates large cache files (376MB per dataset item) to avoid recomputing text encodings, but requires significant storage
  - *From: chancelor*

- **IC LoRA**: Identity Consistent LoRA - specialized training approach for maintaining character identity across video generations
  - *From: Alisson Pereira*

- **Bucket size**: Training resolution dimensions, not the same as final output resolution
  - *From: dischordo*

- **Rank**: Controls how many model weights the LoRA affects - higher rank = more layers affected = more VRAM but potentially more learning
  - *From: MOV*

- **LTX2 i2v mode**: Forces first frame to be input image but still generates based on text prompt, not trained as dedicated i2v
  - *From: Kiwv*

- **Mixed datasets in LTX2**: May prioritize videos over images during training
  - *From: Choowkee*


## Resources & Links

- **LTX-2 Trainer GitHub** (repo)
  - https://github.com/Lightricks/LTX-2/tree/main/packages/ltx-trainer
  - *From: NebSH*

- **Training modes documentation** (documentation)
  - https://github.com/Lightricks/LTX-2/blob/main/packages/ltx-trainer/docs/training-modes.md
  - *From: NebSH*

- **Fal.ai LTX-2 trainer** (platform)
  - https://fal.ai/models/fal-ai/ltx2-video-trainer
  - *From: NebSH*

- **Tear effect LoRA** (model)
  - https://huggingface.co/oumoumad/LTX-2-19b-LoRA-TEAR
  - *From: oumoumad*

- **Gemma-3-12b Abliterated for LTX2** (model)
  - https://huggingface.co/FusionCow/Gemma-3-12b-Abliterated-LTX2/tree/main
  - *From: crinklypaper*

- **LTX-2 training paper** (paper)
  - https://arxiv.org/pdf/2601.03233
  - *From: fearnworks*

- **Hydraulic press LoRA with speedup tips** (model)
  - https://huggingface.co/kabachuha/ltx2-hydraulic-press#ltx-2-hydraulic-press-trained-at-home-in-just-15-hours
  - *From: yi*

- **Sprout LoRA for LTX-2** (model)
  - https://huggingface.co/oumoumad/LTX-2-19b-LoRA-SPROUT
  - *From: oumoumad*

- **IceKiub's LTX-2 Docker template** (tool)
  - docker pull icekiub/icyltx2:latest
  - *From: Alisson Pereira*

- **IceKiub template tutorial** (tutorial)
  - https://youtu.be/JlfQIyjxx2k?t=178
  - *From: Alisson Pereira*

- **Scooby Doo style LoRA** (model)
  - https://civitai.com/models/2308294?modelVersionId=2597100
  - *From: crinklypaper*

- **LTX-2 official trainer repository** (repo)
  - https://github.com/Lightricks/LTX-2/tree/main/packages/ltx-trainer
  - *From: NebSH*

- **TartanAir dataset for IC LoRA** (dataset)
  - https://tartanair.org/
  - *From: Cseti*

- **LoRA Captioner Tool** (tool)
  - https://huggingface.co/spaces/comfyuiman/loracaptionertaz
  - *From: crinklypaper*

- **Deep Zoom LoRA** (lora)
  - https://discord.com/channels/1076117621407223829/1461346143161028702/1461346143161028702
  - *From: oumoumad*

- **Ostris LTX2 settings** (settings)
  - https://x.com/ostrisai/status/2011070979066450171
  - *From: Choowkee*

- **Cakeify Dataset** (dataset)
  - https://huggingface.co/datasets/Lightricks/Cakeify-Dataset
  - *From: matanby*

- **AI Toolkit Easy Install** (tool)
  - https://github.com/Tavris1/AI-Toolkit-Easy-Install
  - *From: MOV*

- **Archive.org music videos** (dataset)
  - https://archive.org/details/artsandmusicvideos
  - *From: NebSH*

- **Archive.org cartoons** (dataset)
  - https://archive.org/details/vintage_cartoons
  - *From: NebSH*

- **LTX trainer quickstart** (documentation)
  - https://github.com/Lightricks/LTX-2/blob/main/packages/ltx-trainer/docs/quick-start.md
  - *From: ColinUrbs*

- **Scooby Doo Style LoRA** (lora)
  - https://civitai.com/models/2308294/scooby-doo-style-lora-ltx2?modelVersionId=2597100
  - *From: crinklypaper*

- **Official LTX2 captioning prompts** (prompt)
  - provided in message
  - *From: BrainNXDomain*

- **Musubi tuner fork** (repo)
  - https://github.com/AkaneTendo25/musubi-tuner
  - *From: Gleb Tretyak*

- **LTX-2 dataset preparation docs** (documentation)
  - https://github.com/Lightricks/LTX-2/blob/main/packages/ltx-trainer/docs/dataset-preparation.md
  - *From: Choowkee*

- **Head swap LoRA for Flux** (model)
  - https://civitai.com/models/2027766
  - *From: Alisson Pereira*

- **Qwen2.5-Omni-7B** (model)
  - mentioned
  - *From: BrainNXDomain*

- **Musubi Tuner LTX-2 fork** (repo)
  - https://github.com/AkaneTendo25/musubi-tuner/tree/ltx-2
  - *From: avataraim*

- **LTX2 Training Docker image** (tool)
  - https://www.reddit.com/r/StableDiffusion/comments/1q8nknf/ltx2_lora_training_docker_imagerunpod/
  - *From: metaphysician*

- **Video captioning tool** (tool)
  - https://huggingface.co/spaces/comfyuiman/loracaptionertaz_v2
  - *From: crinklypaper*

- **Captioning guide** (workflow)
  - https://civitai.com/articles/24082/tazs-ultimate-imagevideo-easy-captioning-tool-gemini-qwen-vl
  - *From: crinklypaper*

- **Golden Boy LoRA** (model)
  - https://civitai.com/models/2334302?modelVersionId=2625818
  - *From: crinklypaper*

- **BFS Head Swap LoRA** (model)
  - https://huggingface.co/Alissonerdx/BFS-Best-Face-Swap-Video
  - *From: Alisson Pereira*

- **Oxen.ai training livestream** (resource)
  - https://www.youtube.com/watch?v=QMRuOZ_JVXg
  - *From: LTX Lux*

- **SD Finetuning guide** (resource)
  - https://github.com/spacepxl/demystifying-sd-finetuning/
  - *From: JUSTSWEATERS*

- **Musubi-Tuner LTX-2 fork** (repo)
  - https://github.com/AkaneTendo25/musubi-tuner.git
  - *From: avataraim*

- **Working Musubi-Tuner commit** (repo)
  - https://github.com/kohya-ss/musubi-tuner/tree/90e1559a7c73ff41ade497605e1f5b1850270711
  - *From: Choowkee*

- **ComfyUI API helper** (tool)
  - https://github.com/deimos-deimos/comfy_api_simplified
  - *From: Guey.KhalaMari*

- **Gemma model for training** (model)
  - https://huggingface.co/google/gemma-3-12b-it-qat-q4_0-unquantized
  - *From: avataraim*

- **Musubi LTX2 fork - stable version** (repo)
  - https://github.com/AkaneTendo25/musubi-tuner/tree/2b77b23defc40bea39ee21680fa3ab73765ab3bf
  - *From: avataraim*

- **Flash Attention prebuilt wheels** (tool)
  - https://github.com/mjun0812/flash-attention-prebuild-wheels/releases/download/v0.7.11/flash_attn-2.8.3+cu128torch2.8-cp312-cp312-win_amd64.whl
  - *From: crinklypaper*

- **Flash Attention packages documentation** (repo)
  - https://github.com/mjun0812/flash-attention-prebuild-wheels/blob/main/doc/packages.md
  - *From: crinklypaper*

- **Older branch of Musubi Tuner for audio** (tool)
  - not provided
  - *From: Guey.KhalaMari*

- **Simpletuner installation** (tool)
  - git clone repo, then pip install '.[cuda13-stable]'
  - *From: Gleb Tretyak*

- **Simpletuner UI command** (tool)
  - simpletuner server --ssl --port 8080
  - *From: avataraim*


## Known Limitations

- **Dataset must be homogeneous**
  - Either all videos or all images, mixing is not supported in training
  - *From: crinklypaper*

- **Fal trainer reliability issues**
  - Multiple users reporting failures and inconsistent results with fal trainer
  - *From: multiple users*

- **Windows compatibility requires manual setup**
  - Official trainer requires Linux, Windows needs manual triton installation
  - *From: boorayjenkins*

- **Effect duration tied to training data length**
  - Training on 3sec clips tends to produce slow motion when generating longer videos
  - *From: oumoumad*

- **I2V is fussy and does its own thing**
  - I2V mode often ignores input and generates unexpected content, sometimes just shows initial frame then goes off on its own
  - *From: fearnworks*

- **Multiple characters in one generation bleed together**
  - When trying to use 2-character LoRA for generating different characters separately, they get mixed like in WAN
  - *From: NebSH*

- **Long music training doesn't work well**
  - Training on 40-90 second music samples performed poorly, likely because base model only trained on 5-10s max
  - *From: mamad8*

- **Pronunciation issues in non-English languages**
  - French words often mispronounced with silent letters spoken or wrong sounds, text encoder doesn't reliably encode pronunciation
  - *From: NebSH*

- **Real movement causes distortion**
  - Even at 9k steps on image + 12k steps on video, any real movement gets distortion
  - *From: crinklypaper*

- **Videos without audio tracks cause issues**
  - Having videos with no audio in dataset may cause inference errors
  - *From: Lumori*

- **Character voice separation difficulty**
  - Multiple characters in dataset tend to combine voices into one unless properly separated
  - *From: Lumori*

- **WAN training parameters don't translate to LTX2**
  - Training approaches that worked for WAN don't work as well for LTX2
  - *From: Choowkee*

- **Audio quality cannot be improved through LoRA**
  - Audio limitations are inherent to LTX2 model itself and cannot be fixed with LoRAs
  - *From: Kiwv*

- **Logos are difficult to train**
  - Multiple attempts to train logos failed even after 9000+ steps, suggesting logos may be a pain point for the model
  - *From: Mazrael.Shib*

- **Small datasets don't work well**
  - 5 videos won't learn anything meaningful, need at least 40 videos for proper training
  - *From: Kiwv*

- **Character bleed between subjects**
  - Some character attributes can bleed between different characters in the dataset
  - *From: crinklypaper*

- **IC LoRA doesn't support audio conditioning during training**
  - Audio must be added as adaptation to IC LoRA workflow, not trained directly
  - *From: Alisson Pereira*

- **Image-only training produces poor motion results**
  - Training with only images gives poor results for video generation compared to video training
  - *From: Mazrael.Shib*

- **Low FPS training causes motion artifacts**
  - Training at low FPS creates hand distortions and artifacts during fast movements
  - *From: MOV*

- **Dataset limited to landscape causes poor vertical video results**
  - Training primarily on landscape videos results in poor performance on vertical videos with full body visible
  - *From: Alisson Pereira*

- **Overtraining character LoRAs with images**
  - Can cause diminished movement and inability for character to talk, even at 250 steps
  - *From: CJ*

- **Training samples are poor quality indicators**
  - Samples during training look much worse than actual LoRA performance
  - *From: NebSH*

- **Recent Musubi-Tuner versions broken**
  - Latest commits fail to train properly with bad loss curves
  - *From: Choowkee*

- **Eyes generalization issues**
  - Model fails to generalize anime eye styles correctly even at 6k steps
  - *From: Choowkee*

- **Audio generation inconsistency**
  - Works only 30% of the time and is prompt-dependent
  - *From: Jonathan Scott Schneberg*

- **8GB VRAM insufficient for training**
  - Barely possible on 24GB, definitely not feasible on 8GB cards
  - *From: Kiwv*

- **Outpainting seam issues**
  - IC LoRA outpainting works but slightly alters original content creating visible seams
  - *From: oumoumad*

- **LTX2 isn't like a one-shot voice cloner**
  - Mileage that audio LoRA can give seems limited
  - *From: Guey.KhalaMari*

- **Simpletuner validation during training doesn't work yet**
  - Plus need to convert LoRAs to ComfyUI format
  - *From: Gleb Tretyak*

- **Possible resolution limitation for training**
  - LoRA trained at 256 resolution had no effect, while 512 resolution previously worked
  - *From: protector131090*


## Hardware Requirements

- **VRAM for training**
  - RTX 6000 Pro uses ~48GB VRAM for training at 992x544x185 without audio, 37-44GB with fp8 model
  - *From: fearnworks*

- **Full model fine-tuning**
  - Requires significant resources, likely multiple H100s
  - *From: burgstall*

- **Minimum VRAM estimate**
  - Looking like 44GB VRAM minimum for training, though AI Studio might enable 24GB
  - *From: Kiwv*

- **System RAM usage**
  - Uses tons of RAM, 64GB recommended for smooth operation
  - *From: crinklypaper*

- **Text encoder size**
  - Gemma text encoder is 23.5GB
  - *From: crinklypaper*

- **H100 training stats**
  - Peak GPU memory: 45.45 GB, 0.30 steps/second, 111.9 minutes total time
  - *From: NebSH*

- **H100 VRAM usage with specific buckets**
  - 60-70GB VRAM usage with resolution buckets 960x544x41 through 960x544x137
  - *From: Cseti*

- **RTX 3090/4090 training possible**
  - Sub-24GB training possible but slow, image-only training works on 24GB
  - *From: ZeusZeus*

- **RTX 3090 training requirements**
  - Need 128GB+ RAM, float8 model, 4-bit text encoder, 256 resolution, 72 frames (3 seconds) might work
  - *From: Kiwv*

- **24GB VRAM training setup**
  - Possible with 128GB RAM, float8 model and text encoder, 100% offload, 512 resolution 5s videos, 30s/it speed
  - *From: MOV*

- **Minimum GPU for training**
  - Tested on 5090+, 4090 might work for images with heavy quantization and offloading but will be slow with poor quality
  - *From: LTX Lux*

- **5090 VRAM usage**
  - 14GB VRAM utilization during training with offloading enabled
  - *From: Choowkee*

- **3090 capability**
  - Can train locally with 100% offload, good for 512res videos and 1024res images
  - *From: MOV*

- **24GB VRAM limitation**
  - Too little for proper LTX training, can only do images with heavy quantization and offloading
  - *From: Kiwv*

- **H100 speed**
  - <1s/it on H100 with LTX trainer, ~7.9s/it on H100 with AI Toolkit
  - *From: scf*

- **VRAM for video training**
  - 100 videos at 512 resolution with 49 frames uses 18GB VRAM on 4090, with 7.30 sec/iter speed
  - *From: avataraim*

- **Storage for text embedding cache**
  - Large datasets require 300GB+ storage space for cached embeddings
  - *From: avataraim*

- **RTX 4090 performance**
  - 5.23 sec/iter for image training, 6-7 sec/iter for video training with audio
  - *From: chancelor*

- **Memory usage during training**
  - Training shows 74.8% memory usage (17.9GB/24GB) on RTX 4090
  - *From: avataraim*

- **24GB VRAM minimum for video training**
  - 512x512x121 frames with rank 32 and audio training uses 22.5-23GB VRAM in AI Toolkit
  - *From: MOV*

- **768x768 training needs A6000 class**
  - 768 resolution at 121 frames requires high-end professional cards without offloading
  - *From: dischordo*

- **Consumer 24GB cards work with optimization**
  - RTX 4090/3090 can train with float8, 4-bit text encoder, and full offloading
  - *From: avataraim*

- **Cache storage needs**
  - 400 videos + 400 images = ~300GB cache files in AI Toolkit, 30MB in Musubi
  - *From: avataraim*

- **VRAM usage with block swapping**
  - 512res 121f videos: 30 swap=18.6GB, 26 swap=21.6GB, 24 swap=22.9GB max VRAM
  - *From: MOV*

- **Training speed on 4090**
  - 5-6 it/sec for 512 video + 768 images, 10 it/sec for video only
  - *From: avataraim*

- **Training speed on 5090**
  - Around 3.30s/it for 512x512 video with images
  - *From: JonkoXL*

- **Cache storage requirements**
  - TE cache for 720 image dataset is 265GB, can quickly fill SSD
  - *From: izashin*

- **RTX 4090 VRAM usage**
  - Can run with blocks_to_swap=5, but may freeze with audio+video training
  - *From: avataraim*

- **RTX 5090 VRAM usage**
  - Can run with blocks_to_swap=0, training speed 3.62 iter/sec
  - *From: avataraim*

- **A6000 performance**
  - Works well for training, used when 4090 had issues
  - *From: avataraim*

- **Minimum VRAM for training**
  - 24GB barely sufficient, 8GB not feasible for quality training
  - *From: Kiwv*

- **VRAM for musubi-tuner**
  - 16 VRAM, still got OOM on validation sampling at 512x512x49
  - *From: Gleb Tretyak*


## Community Creations

- **Tear effect LoRA** (lora)
  - Trained tear/ripping effect, available in 32 and 128 rank versions
  - *From: oumoumad*

- **Sprout LoRA** (lora)
  - Plant sprouting effect retrained for LTX-2 with fine detail improvements
  - *From: oumoumad*

- **Character LoRAs** (lora)
  - Various character LoRAs trained on interview footage using pyscene extraction
  - *From: NebSH*

- **Camera control LoRAs** (lora)
  - 20 camera control LoRAs trained for LTXV 0.97 distilled
  - *From: NebSH*

- **NSFW LoRAs** (lora)
  - Handjob and other adult content LoRAs trained successfully
  - *From: KevenG*

- **IceKiub's LTX-2 Docker template** (tool)
  - Free template with interface for LTX-2 training, available on Runpod or local Docker
  - *From: Alisson Pereira*

- **Audio-only training modifications** (tool)
  - Modified LTX-2 trainer for audio-only training, significantly reduces memory usage
  - *From: mamad8*

- **Scooby Doo style LoRA** (lora)
  - Character and style LoRA trained on Scooby Doo content with voice capabilities
  - *From: crinklypaper*

- **South Park LoRA** (lora)
  - Style LoRA trained on 4 episodes, 889 videos, produces authentic South Park style
  - *From: NebSH*

- **Video segmentation script** (tool)
  - Bash script for bulk segmenting videos into 5s 24fps files
  - *From: ZeusZeus*

- **IC Light LoRA for LTX-2** (lora)
  - Useful for audio react workflows, reference input can be basic white on black audio react map to drive luminance
  - *From: oumoumad*

- **Lum Particles LoRA** (lora)
  - Use any basic white on black video to drive luminance, handy for audio react workflows
  - *From: oumoumad*

- **Musubi tuner fork for LTX2** (tool)
  - Community fork adding LTX2 support to Kohya's training tools, faster than AI Toolkit
  - *From: Choowkee*

- **Custom checkpoint selector node** (node)
  - ComfyUI node to easily select training checkpoints by index from a directory path
  - *From: avataraim*

- **Dataset loader node** (node)
  - ComfyUI node that loads videos and captions from dataset path, supports JSON or separate files
  - *From: avataraim*

- **Multi-run generation node** (node)
  - Allows running 50+ video generations with single click for easy checkpoint comparison
  - *From: avataraim*

- **Whisper ComfyUI node** (node)
  - Custom node for running Whisper speech recognition in ComfyUI workflows
  - *From: MOV*

- **Gradio interface for LTX Musubi** (tool)
  - Easy interface to create datasets, generate toml files, cache, and train with live terminal view
  - *From: avataraim*

- **Firefox extension for Twitch clips** (tool)
  - Scrape and download multiple clips from Twitch as mp4 for dataset creation
  - *From: crinklypaper*

- **Batch setup files for Musubi-Tuner** (workflow)
  - Easy .bat setup for Windows users with install, cache, and train scripts
  - *From: avataraim*

- **Kijai's node for voice LoRA** (node)
  - Works for repurposing character LoRAs for voice only and audio-trained LoRAs
  - *From: Guey.KhalaMari*


---

# LTX Gens - January 2026

# Ltx Gens Knowledge Base
*Extracted from Discord discussions: 2026-01-01 to 2026-02-01*


## Technical Discoveries

- **LTX Video 2 supports text-to-video generation with audio**
  - Model generates both video and audio simultaneously in T2V mode
  - *From: Multiple users*

- **Old LoRAs from LTX 0.97 are compatible with LTX Video 2**
  - NebSH confirmed compatibility and demonstrated multiple LoRAs working without conversion
  - *From: NebSH*

- **Model has strong cartoon/animation memorization**
  - Generates perfect Peppa Pig voices and characters, Amazing World of Gumball style, SpongeBob recognition
  - *From: Phr00t*

- **LTX 2 supports multiple languages for audio generation**
  - French audio generation confirmed working with proper accents
  - *From: Vérole*

- **NebSH's 0.97 camera LoRAs work with LTX-2 out of the box**
  - Old 0.9x LoRAs applied to LTX-2 work without processing - tested 62 different camera motion LoRAs including dolly out, 360 orbit, whip pan, crash zoom, dutch angle, etc.
  - *From: NebSH*

- **Vertical motion works better with specific prompting techniques**
  - Describing mouth movement and other specific movements creates better results than just prompting 'she says...' which didn't move image at all
  - *From: gopnik*

- **LTX-2 can generate music and sound effects**
  - Model acts as music generator - can create realistic sound effects and music matching video content
  - *From: Fictiverse*

- **Scene transitions need 2-3 seconds between cuts to avoid confusion**
  - Model leans towards one long shot rather than cutting scenes, needs adequate time between transitions
  - *From: cyncratic*

- **BF16 has considerable quality difference over FP8**
  - Noticeable quality improvement when using BF16 full model versus FP8 quantized version
  - *From: NebSH*

- **Short prompts work better when given audio input**
  - Simple prompts like 'A punk rock music video in a public bathroom. A Man wearing sunglasses and a leather jacket' work well with audio latents
  - *From: 305792526629994496*

- **Distill LoRA affects skin rendering**
  - The model likes to make shiny skin, and the distill lora might have an impact on this
  - *From: Owlie*

- **Using different LoRA configurations affects output**
  - Comparison shows detailer lora on stage 1 vs stage 2 vs both stages produces different results
  - *From: gopnik*

- **LTX2 can handle multi-language audio**
  - Model performs well with German and French language generation, with some spelling complexities in French
  - *From: gopnik*

- **Big negative prompts can cause stuttery outputs**
  - Large default negative prompts may be causing stuttery video outputs
  - *From: TK_999*

- **Model supports audio conditioning and masking**
  - Can use audio masking to preserve original audio in specific time ranges
  - *From: Dragonyte*

- **CFG1 distilled models ignore encoding, so can reuse single encoding to save time**
  - When using distilled models with CFG1, the encoding is ignored anyway, so you can reuse a single encoding to save processing time
  - *From: TK_999*

- **LTX2 might work as world model base**
  - LTX2 could potentially be used as a foundation for world models in the future
  - *From: TK_999*

- **Music has big effect on motion speed**
  - The audio/music input significantly affects the speed and intensity of generated motion in videos
  - *From: Benjimon*

- **No background gives better results**
  - Cropping out backgrounds or using no background naturally seems to produce better generation results
  - *From: JUSTSWEATERS*

- **Model can sync dancing to audio beat**
  - LTX2 can generate dancing that is timed to the beat of input audio
  - *From: Marco_vdm*

- **Distilled model needs adjustment for better quality**
  - To avoid plastic look with distilled model, add detail LoRA on both samplers, reduce distilled LoRA to 0.6, and use detail daemon with enhance image node
  - *From: dj47*

- **Grid patterns appear in dark scenes**
  - Strong grid patterns visible in dark scenes, can be adjusted with LTXV Spatio Temporal Tiled VAE Decode settings
  - *From: garbus*

- **Natural looking breathing makes videos appear more alive**
  - Breathing animation improves realism in character videos
  - *From: Rainsmellsnice*

- **Changed fps from 24 to 25 fixed temporal jerkyness**
  - Temporal upscaler expects 25 fps, works even at high frame counts like 461 frames
  - *From: HeadOfOliver*

- **Empty audio latent for upscale stage improves audio quality**
  - Instead of running first stage audio latent output into upscale, use new empty audio latent for better i2v audio
  - *From: dischordo*

- **Negative distill lora at -0.50 removes film grain**
  - Using negative distill lora strength helps remove excessive film grain and damage artifacts
  - *From: Nathan Shipley*

- **FlowMatchEuler scheduler maintains sharpness in long videos**
  - FlowMatch scheduler doesn't degrade video quality over time, keeps sharp last frames even on 15 steps
  - *From: neofuturo*

- **Increasing FPS helps reduce blur and improve detail quality**
  - Higher FPS makes videos less blurry and increases detail, but reduces effective video length you can render
  - *From: GalaxyTimeMachine (RTX4090)*

- **LTX2 can generate stereo audio with spatial positioning**
  - Model supports stereo audio generation and has some sense of spatial audio positioning
  - *From: ezMan*

- **Detail LoRA is primarily for v2v upscaling**
  - Detail LoRA is more used with video-to-video upscaling rather than initial generation
  - *From: The Shadow (NYC)*

- **Motion blur may be from overtrained dataset or latent space compression**
  - The mushiness/motion blur issues could be from being overtrained on motion blur or a side effect of latent space compression
  - *From: nikolatesla20*

- **LTX2 doesn't need large datasets for camera/effect LoRAs**
  - Can train effective camera movement and effect LoRAs with as few as 6 generated AI videos
  - *From: NebSH*

- **Audio generation may be random when not explicitly prompted**
  - Background music generation appears random when audio description isn't included in prompt
  - *From: ezMan*

- **Distilled 8-step with custom sigmas works well**
  - Using er_sde sampler with distilled model and 8-step custom sigmas produces high quality results
  - *From: GalaxyTimeMachine (RTX4090)*

- **48fps conditioning gives less blurry speech generation**
  - Using 48fps as conditioning frame rate reduces blur during speech, then can export back to 24fps for cinematic feel
  - *From: ucren*

- **Distilled LoRA with negative strength improves likeness**
  - Using distilled LoRA at negative strength (like -0.4) helps fix overbaked distilled model and improves face consistency
  - *From: ucren*

- **Multiple frame extension workflow (FFLF) works well**
  - First, middle, last frame workflow with multiplier node allows adding more frames for extensions
  - *From: neofuturo*

- **LTX2 knows character voices well**
  - Model can generate Rick and Morty voices without pre-generated audio clips, just from prompting
  - *From: herpderpleton*

- **Inpainting maintains better likeness**
  - Using inpainting/extending with many latent samples helps maintain face consistency better than straight generation
  - *From: ucren*

- **Audio latent strength can be reduced**
  - Using latent multiply at 0.75 strength on audio latent reduces exaggerated expressions
  - *From: ucren*

- **Second masked upscale pass improves audio sync**
  - Adding a second masked upscale pass significantly helps with audio extend/clone quality
  - *From: ucren*

- **Distilled model can be 'debaked' using distill LoRA at negative values**
  - Using distill LoRA at -0.4 makes a huge difference on plastic skin issues
  - *From: ucren*

- **GGUF lipsync solution found**
  - Use one stage Kijai-based workflow with GGUF distilled model, distilled lora at -0.3, and normal connector on clip (not distilled)
  - *From: Alpha-Neo*

- **Frame count formula discovered**
  - Frame count must be 8n+1 (e.g., 241 frames for 10 seconds at 24fps)
  - *From: N0NSens*

- **Tiled VAE decoding causes visible grid patterns in dark scenes**
  - Grid patterns appear as double lines where tiles overlap, visible in dark scenes but masked in bright areas
  - *From: ucren*

- **Audio normalization issues in v2v extend**
  - Huge volume changes and distortion occur when using v2v extend functionality
  - *From: U̷r̷a̷b̷e̷w̷e̷*

- **Two-stage vs one-stage workflow differences**
  - One stage workflow has better camera adherence and prompt following, two-stage is hit and miss
  - *From: Alpha-Neo*

- **LTX2 can handle very long videos with RTX 5090**
  - 5090 can generate 1000 frames at 1280x720 resolution
  - *From: NebSH*

- **Frame injection technique for controlled transitions**
  - Can inject 3-5 frames at specific frame indexes for precise control over video transitions
  - *From: neofuturo*

- **Camera static LoRA combined with negative distill LoRA improves stability**
  - Camera static LoRA at 0.5 and distill LoRA at -0.3 resolved camera static issues
  - *From: mdkb*

- **Audio-to-video works well with musical content**
  - Model shows good audio reactivity and can generate music videos from audio input
  - *From: multiple users*

- **Dev model with distill LoRA at lower strength reduces oversaturation**
  - Using dev model with distill LoRA at 0.6 helps control oversaturation compared to pure distilled model
  - *From: U̷r̷a̷b̷e̷w̷e̷*

- **Charlie generated 1500 frames in one go with LTX2**
  - Successfully generated 1500 frames in a single generation
  - *From: Charlie*

- **Direct resolution at 1504/832 gives better motion than 1280/720 then upscale**
  - First pass at higher resolution produces better motion quality than upscaling from lower resolution
  - *From: Vérole*

- **Charlie can do 2000 frames in 1 go**
  - Extended frame generation capability demonstrated
  - *From: Charlie*

- **LTX2 supports text-to-image generation**
  - Model can generate static images as well as video, described as realistic
  - *From: hicho*

- **Prompt structure affects i2v vs t2v behavior**
  - Simple prompts like 'woman is walking and sings' maintain i2v mode, complex prompts not matching reference image switch to t2v mode
  - *From: hicho*

- **Audio prompting order matters for speech generation**
  - Structure like 'person speaks in harsh low voice and says' works better than 'person speaks saying [text] in harsh low voice'
  - *From: U̷r̷a̷b̷e̷w̷e̷*

- **T2AV (text-to-audio-video) prompting works well**
  - Single pass t2v audio prompting produces good results
  - *From: 152993277631528960*

- **Heavy noise helps LTX output quality**
  - Adding noise to input improves generation results
  - *From: 152993277631528960*

- **Keeping everything in silhouette avoids artifacts**
  - Silhouette approach reduces visual artifacts in generations
  - *From: 152993277631528960*

- **Motion LoRA on first pass produces better results**
  - Using motion LoRA at 1920/1088 first pass then upscale preferred over preprocessor on first stage
  - *From: Vérole*

- **LTX2 knows Super Mario Bros Super Show content**
  - Key phrase 'A cartoon from the Super Mario Bros Super Show' enables character generation from that series
  - *From: U̷r̷a̷b̷e̷w̷e̷*

- **Using dev+lora at 0.6 strength helps maintain face quality during camera rotation**
  - User reports improved face consistency when using this configuration
  - *From: U̷r̷a̷b̷e̷w̷e̷*

- **IC detailer lora at 0.5 strength works for T2V but breaks I2V/V2V**
  - Using IC detailer lora on I2V or V2V messes up matching and changes faces significantly
  - *From: U̷r̷a̷b̷e̷w̷e̷*

- **Static camera control lora helps prevent camera wandering**
  - Testing shows it definitely helps keep the camera from moving unexpectedly
  - *From: Benjimon*

- **New LTX Multimodal Guider shows significant improvement over old guider**
  - Comparison shows dramatically better results with the new guider
  - *From: garbus*


## Troubleshooting & Solutions

- **Problem:** I2V outputs static for 3 seconds then deforms
  - **Solution:** Lower noise mask to 0.6 (strength parameter on native workflow)
  - *From: Dragonyte*

- **Problem:** Out of memory errors on first run
  - **Solution:** Run batch of 2 - first will fail, second will work
  - *From: VK (5080 128gb)*

- **Problem:** CLIP encoder causing OOM errors
  - **Solution:** Use fp8 gemma 3 model
  - *From: Phr00t*

- **Problem:** Audio quality is tinny/wonky
  - **Solution:** Listed as known issue, no solution provided yet
  - *From: burgstall*

- **Problem:** OOM/crashes during VAE decode on longer videos
  - **Solution:** Use tiled VAE decode, increase RAM, or reduce resolution/frame count
  - *From: Tachyon*

- **Problem:** Tensor mismatch in native workflow
  - **Solution:** Use shared working workflows from community members
  - *From: HeadOfOliver*

- **Problem:** Model occasionally produces slideshow-like images with no motion
  - **Solution:** Unknown trigger, appears random in automatic scene generation
  - *From: Simonj*

- **Problem:** Green squares appear on screen during high-resolution long renders
  - **Solution:** Reboot system - likely unstable overclock/downvolt issue
  - *From: 305792526629994496*

- **Problem:** Custom audio not working
  - **Solution:** Issue with custom audio functionality, still unresolved
  - *From: VRGameDevGirl84(RTX 5090)*

- **Problem:** Static video with short prompts
  - **Solution:** Use longer, more detailed prompts. Short prompts result in static videos that barely move
  - *From: VRGameDevGirl84(RTX 5090)*

- **Problem:** Enhancer node causing errors
  - **Solution:** Remove the prompt enhancer node from workflow to fix mat1/mat2 errors
  - *From: GalaxyTimeMachine(RTX4090)*

- **Problem:** OOM errors on second sampler
  - **Solution:** Set aggressive tiling settings, use reserve VRAM setting at 6, ensure using FP8 models
  - *From: D'Squarius Green, Jr.*

- **Problem:** Face warping and eye issues in T2V
  - **Solution:** 
  - *From: gopnik*

- **Problem:** Preview mode causing mat1/mat2 errors
  - **Solution:** Disable preview mode to fix matrix multiplication errors
  - *From: gopnik*

- **Problem:** Cursed fingers with distilled model
  - **Solution:** Full model needs 40 steps to avoid cursed fingers, distilled gets it mostly right but changes the face
  - *From: 421114995925843968*

- **Problem:** Plastic look with distilled model
  - **Solution:** Add detail LoRA on both samplers, reduce distilled LoRA to 0.6, add detail daemon and enhance image node
  - *From: dj47*

- **Problem:** Grid patterns in dark scenes
  - **Solution:** Adjust LTXV Spatio Temporal Tiled VAE Decode settings - 2/8/16/8 appears best but doubles VRAM use
  - *From: garbus*

- **Problem:** Image degradation when using last frame for continuation
  - **Solution:** Still looking for solution to maintain continuation while avoiding degradation
  - *From: NebSH*

- **Problem:** Blotchy face in wider shots during character motion in I2V
  - **Solution:** No specific solution provided, user asking for advice
  - *From: Choowkee*

- **Problem:** I2V produces garbage with short prompts
  - **Solution:** LTX2 requires long prompts same as LTX 0.9.8 did - short prompts produce garbage
  - *From: cyncratic*

- **Problem:** Audio has hissing and distortion
  - **Solution:** Need more steps or different sampler during upscale, multistep/complex schedulers seem better
  - *From: garbus*

- **Problem:** Temporal jerkyness in upscaler above 241 frames
  - **Solution:** Change fps to 25 instead of 24, upscaler expects 25 fps
  - *From: HeadOfOliver*

- **Problem:** i2v was broken, generations taking longer
  - **Solution:** Use negative node in workflow, switch to ksampler approach
  - *From: hicho*

- **Problem:** Extend workflow spitting out input video
  - **Solution:** Install 2 prerequisites for gemma to work with gemma 3 model loader node
  - *From: Mazrael.Shib*

- **Problem:** Jerkyness every few frames
  - **Solution:** Decrease detail-lora strength or change fps to 25
  - *From: N0NSens*

- **Problem:** Background elements appearing jittery/boiling even with minimal movement
  - **Solution:** Use dpmpp_sde + normal (50% slower) or res_2s (4x slower) samplers
  - *From: Arts Bro*

- **Problem:** NoneType object has no attribute 'Params' on checkpoint node
  - **Solution:** Delete the 'ckpt_name' thing and select everything manually
  - *From: Zueuk*

- **Problem:** GEMMA model load destroys hardware on 3090
  - **Solution:** Try using quantized GEMMA or GGUF GEMMA
  - *From: Tachyon*

- **Problem:** Upscaling uses all 24GB VRAM regardless of GGUF model size
  - **Solution:** Model size doesn't affect latent frame buffer - VRAM usage depends on latent video frames at resolution, not model size
  - *From: Volkin*

- **Problem:** Image-to-video often produces still images
  - **Solution:** Use audio+image to video instead of just image to video for better motion
  - *From: Mazrael.Shib*

- **Problem:** Loss of lip sync with faster workflows
  - **Solution:** Speed improvements may come at cost of lip sync quality - trade-off between speed and sync
  - *From: Simonj*

- **Problem:** Face changes too much in I2V with audio
  - **Solution:** Use distilled LoRA at negative strength (-0.4 to -0.6), reduce audio latent strength to 0.75, and consider using non-famous faces
  - *From: ucren*

- **Problem:** Sage attention errors with FP32
  - **Solution:** Use KJ checkpoint loader to force FP16 loading to avoid sage switching to pytorch attention
  - *From: nikolatesla20*

- **Problem:** OOM errors on high resolution long videos
  - **Solution:** Use --reserve-vram 2.0 startup parameter and Kijai's Chunk Feed Forward node
  - *From: garbus*

- **Problem:** Motion artifacts in longer extensions
  - **Solution:** Higher conditioning fps (48fps) creates more motion artifacts in long extensions, 24fps conditioning works better for longer clips
  - *From: ucren*

- **Problem:** LTXVPREPROCESS node causing issues
  - **Solution:** Set LTXVPREPROCESS node to 0
  - *From: Jonathan Scott Schneberg*

- **Problem:** Tiled VAE decode grid artifacts in dark scenes
  - **Solution:** Increase tiled overlap to 256 or use non-tiled decoding with 1 tile and 0 overlap
  - *From: ucren*

- **Problem:** No lipsync with GGUF Q8 dev model
  - **Solution:** Use distilled model with distilled LoRA at -0.3 and normal clip connector
  - *From: Alpha-Neo*

- **Problem:** Frozen frame issues with GGUF at higher resolutions
  - **Solution:** Balance LTXImgToVideoInPlace (start at 0.4) and LTXVPreprocess (10-33, usually 25) settings
  - *From: mdkb*

- **Problem:** Audio volume inconsistency in v2v extend
  - **Solution:** Create audio normalization node that analyzes video before segment and auto-normalizes
  - *From: U̷r̷a̷b̷e̷w̷e̷*

- **Problem:** Prompt control varies between resolutions
  - **Solution:** Need to rebalance LTXImgToVideoInPlace and LTXVPreprocess when changing resolution
  - *From: mdkb*

- **Problem:** Character loses likeness in audio-driven video
  - **Solution:** Adjust mask timing - too early preserves likeness but loses mouth movement, too late gets movement but loses likeness
  - *From: Nekodificador*

- **Problem:** Video extension consistency issues and RAM problems
  - **Solution:** Use Kijai's new memory efficiency nodes and NAG for better control
  - *From: mdkb*

- **Problem:** Frame count error for video extension
  - **Solution:** Need 1 + 8 * x frames (e.g., 1, 9, 17, ...). Sometimes need to add +1 to frame count manually
  - *From: mdkb*

- **Problem:** Audio volume jumps when switching to LTX generation
  - **Solution:** Use audio enhancement and normalization nodes with auto mode that analyzes first 3 seconds of source audio
  - *From: U̷r̷a̷b̷e̷w̷e̷*

- **Problem:** High CFG causing artifacts
  - **Solution:** User had CFG set too high, switching back to CFG 1.0 for distilled model fixed artifacts
  - *From: Nekodificador*

- **Problem:** Color bug with vertical upscale outputs over 1536 pixels
  - **Solution:** Top and bottom get blue hue and hallucinations at high vertical resolutions
  - *From: dischordo*

- **Problem:** Frame count issues in video processing
  - **Solution:** Change inbound video to 146 frames or reduce cutoff frames in increments of 1 until finding working number
  - *From: mdkb*

- **Problem:** FPS related generation issues
  - **Solution:** Set FPS to 25 to fix the problem
  - *From: boop*

- **Problem:** Memory issues on 5080 16GB with controlnet
  - **Solution:** Use GGUF models in fp4, or try KJ loader and force fp16
  - *From: hicho*

- **Problem:** Grid deforming faces in generations
  - **Solution:** Issue acknowledged but no specific fix provided yet
  - *From: hicho*

- **Problem:** Video codec playback issues
  - **Solution:** Use standard h.264 MP4 format with VHS node for better compatibility
  - *From: 152993277631528960*

- **Problem:** Wrong aspect ratio in prompt causes split screen effect
  - **Solution:** Ensure correct aspect ratio is specified in the prompt
  - *From: 152993277631528960*

- **Problem:** Face drift and identity loss during generation
  - **Solution:** Attempted using identity lora but results were similar - issue persists
  - *From: NebSH*

- **Problem:** Face gets messed up during camera rotation prompts
  - **Solution:** Switch to dev+lora at 0.6, use manual sigma settings with euler, and use IC detailer lora at 0.5 for T2V only
  - *From: U̷r̷a̷b̷e̷w̷e̷*


## Model Comparisons

- **LTX 2 vs WAN 2.2**
  - LTX has better everything except per-pixel resolution and physics. WAN better for texture fidelity
  - *From: dj47*

- **LTX 2 vs Sora 2**
  - Both have character dialogue assignment issues, but LTX has less problems
  - *From: dj47*

- **Dev model vs Distilled model for movement**
  - Dev model helps with movement quality, recommend 40 steps with dev then 3 with distill for upscale
  - *From: Benjimon*

- **Portrait vs landscape orientation**
  - Portrait works fine, Sora portrait often better than landscape
  - *From: VK*

- **Full model vs FP8 for LoRA quality**
  - Considerable quality difference with BF16 full model being superior
  - *From: NebSH*

- **Distill workflow vs full model workflow**
  - Full model workflow has better prompt adherence and detail due to higher CFG and more steps
  - *From: gopnik*

- **T2V vs I2V stability**
  - Getting more stable results overall with T2V than I2V
  - *From: 305792526629994496*

- **Motion quality at different resolutions**
  - Motion is not as good at higher resolution
  - *From: Benjimon*

- **Stage 2 vs both stages for LoRA**
  - Stage 2 alone produces more natural car movement, both stages makes it look floating
  - *From: Tonon*

- **Different upscalers**
  - res_2s takes extra 100s to generate compared to euler_a
  - *From: chancelor*

- **T2V vs original video idea**
  - LTX2 T2V got surprisingly close to replicating video concepts, though not exact
  - *From: garbus*

- **Distilled vs full model quality**
  - Full model produces better quality but distilled is faster - distilled has plastic look
  - *From: NebSH*

- **8 steps distill vs 40 steps full model**
  - Full model at 40 steps produces more natural look than distilled at 8 steps
  - *From: NebSH*

- **Distilled vs Dev model for audio/video masking**
  - Distilled has more motion and grain, more overcooked and angry; Dev matches original footage better, less angry
  - *From: Nathan Shipley*

- **LTX-2 vs WAN 2.2 for car lifting prompt**
  - WAN 2.2 did it in one shot, LTX-2 took over 20 workflow runs
  - *From: nikolatesla20*

- **15 steps distilled vs dev model for i2v**
  - 15 steps on distilled works like a charm, dev model produces crap with i2v
  - *From: neofuturo*

- **LTX western cartoon vs anime capability**
  - LTX2 knows how to do western cartoon somewhat, but struggles with anime
  - *From: Choowkee*

- **LTX2 vs Wan2**
  - Wan has better character retention and physics, but LTX2 has sound, higher FPS, dynamic motion and realistic speed. Currently a tie with LTX2 having better potential as base
  - *From: dj47*

- **Non-distilled vs distilled for audio**
  - Non-distilled often produces better sound quality than distilled version
  - *From: ezMan*

- **Phroot merge fp8 vs distilled gguf q4km**
  - Phroot merge in fp8 format is about 1.5x larger but actually faster in all parts
  - *From: patientx*

- **LTX2 vs WAN for visual quality**
  - LTX2 has watery effects and detail loss similar to WAN 2.1, behind WAN 2.2 in visual quality but faster
  - *From: Juan Gea*

- **LTX2 vs InfiniteTalk for face consistency**
  - InfiniteTalk better for face consistency, LTX2 changes faces too much but much faster (82 seconds vs 8 minutes)
  - *From: nikolatesla20*

- **LTX2 vs WAN speed**
  - LTX2 much faster - can generate 8 seconds in 30 seconds vs WAN taking much longer
  - *From: 152993277631528960*

- **Dev vs Distilled model quality**
  - Dev + distill lora @0.6 seems same quality as distilled for most cases
  - *From: ucren*

- **Flux Klein vs Flux Kontext for image editing**
  - Klein is smaller, faster (4-5 seconds on RTX 3090), and produces better results than the older Kontext model
  - *From: nikolatesla20*

- **LTX vs InfiniteTalk with Magref for lipsync**
  - InfiniteTalk produces better 'communique' results, LTX attempts were disappointing and more challenging than expected
  - *From: mdkb*

- **One-stage vs two-stage workflow**
  - One-stage superior with better camera adherence like 'kling 2.6', two-stage makes more blancmange artifacts
  - *From: Alpha-Neo*

- **Dev model vs distilled model**
  - Dev with distill LoRA at 0.6 gives less washed out results but takes twice as long as pure distilled
  - *From: U̷r̷a̷b̷e̷w̷e̷*

- **LTX2 vs WAN model**
  - LTX2 system prompt is essential unlike WAN which works with simple sentences
  - *From: hicho*

- **GGUF Q5 models vs full models**
  - GGUF Q5 can generate high resolution (3072x2048) on lower VRAM but takes 20-30 minutes
  - *From: The Shadow (NYC)*

- **LTX2 vs WAN for video-to-video**
  - LTX2 v2v with latent low denoise is very bad unlike WAN, but LTX2 IC LoRA with controlnet works better
  - *From: hicho*

- **Motion LoRA vs preprocessor on first stage**
  - Motion LoRA on first pass preferred over preprocessor
  - *From: Vérole*

- **Single resolution vs upscale workflow**
  - Direct high resolution (1504/832) better motion than lower resolution (1280/720) then upscale
  - *From: Vérole*

- **Old guider vs new LTX Multimodal Guider**
  - New guider produces significantly better results
  - *From: garbus*


## Tips & Best Practices

- **Videos have time to breathe and linger, allowing realistic pacing**
  - Context: Unlike cramming everything into 5 seconds
  - *From: KakerMix*

- **Try other languages for different voice effects**
  - Context: Model supports multiple languages with proper accents
  - *From: garbus*

- **Use WAN upscaling on LTX 2 output for quality improvement**
  - Context: Hybrid workflow for better final results
  - *From: VK (5080 128gb)*

- **Use dolly out camera LoRA for better vertical motion**
  - Context: When trying to achieve vertical movement in videos
  - *From: gopnik*

- **Describe specific movements in prompts rather than generic actions**
  - Context: For better animation results - describe mouth moving rather than just 'she says'
  - *From: gopnik*

- **Close Civitai tabs during generation for better performance**
  - Context: Having Civitai tabs open affects performance especially in final VAE decode step
  - *From: Hell G.*

- **Use timestamp prompting for scene control**
  - Context: [0-3s] format works well with LTX-2 and can handle cuts/transitions
  - *From: brent*

- **Sequential prompting works without markup**
  - Context: Can prompt sequentially without timestamp notation
  - *From: TK_999*

- **Use detailed prompting for better results**
  - Context: Prompting rewrites improve the quality of the result quite a bit
  - *From: chancelor*

- **Use LLM nodes for prompt enhancement**
  - Context: Create workflow that uses LLM nodes to help with prompting, taking image and text prompts to create video prompts
  - *From: VRGameDevGirl84(RTX 5090)*

- **Sound helps video stability**
  - Context: Including sound in generations helps with overall video stability
  - *From: Benjimon*

- **Different samplers may help with skin issues**
  - Context: To address shiny skin problems, try different samplers like sa_solver or lcm
  - *From: Phr00t*

- **Image preprocessing recommended**
  - Context: Use image compression preprocessing node for better I2V results
  - *From: Phr00t*

- **Use frame slice node to get proper frame count**
  - Context: GIF needs to be 8n+1 frames - had to slice off 1 frame to get 17 frames
  - *From: Scruffy*

- **Add your own smearish frame in middle**
  - Context: Adding custom intermediate frames can improve motion
  - *From: JUSTSWEATERS*

- **Use LLM to enhance prompts**
  - Context: Copy instructions from enhancer node and put through LLM for better I2V prompts
  - *From: Choowkee*

- **Long prompts work better**
  - Context: LTX2 requires long detailed prompts like LTX 0.9.8, short prompts produce poor results
  - *From: cyncratic*

- **Sometimes big prompt changes do nothing, single words change everything**
  - Context: After 200 prompt tweaks, learned that prompting behavior is unpredictable
  - *From: jiffyam*

- **For i2v, less intricate prompts work much better**
  - Context: Complex prompts cause loss of input image quickly
  - *From: Arts Bro*

- **Use dev fp8 + 0.5 distilled lora with half the steps**
  - Context: Get quality results with fewer steps by combining models
  - *From: Arts Bro*

- **40-50fps better for fast motion**
  - Context: Higher fps helps with fast motion sequences
  - *From: nikolatesla20*

- **Videos need couple seconds at least, should be long enough for intended action/dialogue**
  - Context: Many people don't give enough time for the action they want
  - *From: garbus*

- **Simple prompts sometimes work better than detailed ones**
  - Context: LTX prompting can be unpredictable
  - *From: HeadOfOliver*

- **Using Sora2 system prompt works with LTX**
  - Context: Cross-model prompting techniques
  - *From: hicho*

- **Use ChatGPT with specific formatting for better prompts**
  - Context: Give ChatGPT a structured format template, then describe what you want and it will format prompts for LTX-2 that work better than manual typing
  - *From: nikolatesla20*

- **Lower LoRA strength when combining multiple effects**
  - Context: When using snorricam LoRA with outfit change, had to lower snorricam to 0.4 for better results
  - *From: NebSH*

- **Use 'interrupted' instead of 'disturbed' for character interactions**
  - Context: Better word choice for prompting character dialogue interruptions
  - *From: Mazrael.Shib*

- **Create x2 interpolation after generation for smoother results**
  - Context: Generate at 32 fps then apply 2x interpolation for better detail and smoothness
  - *From: GalaxyTimeMachine (RTX4090)*

- **Use separate passes for upscaling quality control**
  - Context: Output first low-res pass, check if it's OK, then send to upscaler pass
  - *From: N0NSens*

- **Be very specific in prompts for crowd scenes**
  - Context: For busy sidewalk scenes, specify exact movements like 'he pushes past the people' rather than vague descriptions
  - *From: U̷r̷a̷b̷e̷w̷e̷*

- **Use LLMs for prompt enhancement**
  - Context: ChatGPT 4o mini, Gemma3, Qwen3 via OpenRouter work well for enhancing prompts
  - *From: U̷r̷a̷b̷e̷w̷e̷*

- **Include spoken text in prompts for better results**
  - Context: When doing audio-driven generation, typing out what the character says in the prompt can help, especially for inpainting continuations
  - *From: ucren*

- **Lower diffused lora strength for longer generations**
  - Context: Reduce to about 0.6 to help with focus issues on longer generations
  - *From: Mazrael.Shib*

- **Keep models loaded for faster generation**
  - Context: When doing series of similar generations, keeping models loaded speeds up process significantly
  - *From: 152993277631528960*

- **Use minimal prompting for i2v**
  - Context: More descriptive prompts cause model to ignore image and add unwanted elements
  - *From: mdkb*

- **Include non-masked audio in prompt for v2v**
  - Context: Helps with audio continuity when extending videos
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Normalize audio to loud levels like -14LUFS**
  - Context: Helps with lipsync quality
  - *From: mdkb*

- **Use negative prompts for accent control**
  - Context: Can control unwanted accents by putting them in negative prompt
  - *From: mdkb*

- **Do 5-10 seconds setup then extend with fresh prompt**
  - Context: Works well for lazy prompting approach instead of highly structured prompts
  - *From: garbus*

- **Use system prompt for better results**
  - Context: LTX2 system prompt is essential for good results unlike other models
  - *From: hicho*

- **Static shots can go very long without degradation**
  - Context: For mostly static shots with little motion, can generate very long videos
  - *From: garbus*

- **Mask input image for video extension**
  - Context: When getting errors in video extension, try masking the input image
  - *From: mdkb*

- **Use smaller first stage then upscale**
  - Context: Start with small resolution like 480x420 then upscale for better results
  - *From: JUSTSWEATERS*

- **First and last frame workflow works better with specific weights**
  - Context: Use 1.0 for first frame, 0.75 for subsequent frames, and change second frame to 1.00 for better results
  - *From: VRGameDevGirl84*

- **Use simple prompts for image-to-video to avoid switching to text-to-video mode**
  - Context: When you want to maintain reference image fidelity
  - *From: hicho*

- **Structure speech prompts as 'person speaks in [voice] and says [text]'**
  - Context: For better audio generation results
  - *From: U̷r̷a̷b̷e̷w̷e̷*

- **Generate at 1920x1080 resolution for better quality**
  - Context: Low resolution always looks poor, higher resolution helps significantly
  - *From: nikolatesla20*

- **Usually generate with at least 960x960 for good results**
  - Context: General generation guidelines, though higher resolution is always better
  - *From: U̷r̷a̷b̷e̷w̷e̷*

- **Add 'GLITCH' in various prompt places to create artifacts**
  - Context: For intentional glitch effects
  - *From: 305792526629994496*

- **Use phrase 'A cartoon from the Super Mario Bros Super Show' to generate Mario content**
  - Context: For generating content from that specific animated series
  - *From: U̷r̷a̷b̷e̷w̷e̷*

- **Create T2V with complex prompt, take first frame, convert to desired style, then use same prompt in I2V**
  - Context: Workflow for style transfer and consistency
  - *From: VK (5080 128gb)*

- **Only use IC detailer lora on T2V, not I2V or V2V**
  - Context: Using it on I2V/V2V will mess up matching and change faces
  - *From: U̷r̷a̷b̷e̷w̷e̷*

- **Bad audio can be replaced with groove music to change the video's tone**
  - Context: Can transform epic war scenes into fashion show-style content
  - *From: U̷r̷a̷b̷e̷w̷e̷*

- **Create perfect loops by copying and pasting end to end**
  - Context: 4-second loops can be extended to any length needed
  - *From: U̷r̷a̷b̷e̷w̷e̷*


## News & Updates

- **ComfyUI templates added for LTX Video 2**
  - Official templates available in ComfyUI pull request
  - *From: LukeG89*

- **Training scripts released for LTX Video 2**
  - Model is trainable with open source training scripts
  - *From: AshmoTV*

- **LoRA training documentation released including audio training**
  - Official documentation available for training LoRAs with audio capabilities
  - *From: 305792526629994496*

- **Wallace and Gromit LoRA available on HuggingFace**
  - Community LoRA working with LTX-2
  - *From: ˗ˏˋ⚡ˎˊ-*

- **LTX team is impressed with community creations**
  - Team spoke about being super impressed with community work
  - *From: 210245371002093570*

- **Community showcase video created featuring recent work**
  - Showcase video made featuring cool community creations from recent days
  - *From: 210245371002093570*

- **LTX devs have fix for audio stability coming soon**
  - Developers said they had a good idea for fixing audio stability issues but it didn't make it in time for current release, will be in next release
  - *From: TK_999*

- **New workflow and nodes released**
  - Updated nodes and new workflow released that helped stop still images and no talking issues
  - *From: 130694557913317377*

- **VHS LoRA trained on old tapes**
  - LoRA trained on VHS tapes from late 80s/early 90s with commercials and desert footage
  - *From: 305792526629994496*

- **AnimateDiff LoRA available**
  - AnimateDiff style LoRA for LTX2 available on HuggingFace
  - *From: neofuturo*


## Workflows & Use Cases

- **ChainneR app for reusing I2V workflows**
  - Use case: Streamlining I2V generation process
  - *From: magix*

- **LTX 2 to WAN upscaling pipeline**
  - Use case: Improving final video quality
  - *From: VK (5080 128gb)*

- **Two-stage rendering: 20 steps half-res then distill at full-res**
  - Use case: High quality renders - splits first 20 steps at half resolution then 4 distill steps at full resolution
  - *From: 305792526629994496*

- **Automatic scene generation from Reddit stories**
  - Use case: One-click conversion from text stories to video scenes using multiple LLM calls
  - *From: Simonj*

- **Audio input workflow for custom sound**
  - Use case: Adding custom audio with selectable start point and duration
  - *From: Helikaon23s*

- **LLM-enhanced prompting with random image generation**
  - Use case: Uses LLM nodes with zimage to create random images, then LLM takes image and text prompt to create new image-to-video prompt
  - *From: VRGameDevGirl84(RTX 5090)*

- **Kijai's Audio Continuity workflow**
  - Use case: For maintaining audio continuity across video generation
  - *From: Tachyon*

- **Video extension using latent concatenation**
  - Use case: Continue videos by giving multiple frames instead of single image, similar to Google Flow extend
  - *From: 421114995925843968*

- **Multi-scene automated generation**
  - Use case: Automated workflow for creating multiple scenes with scheduler applet
  - *From: magix*

- **Extension from audio using image and audio driving to video**
  - Use case: Creating videos that sync motion to audio beat
  - *From: Vérole*

- **Flux2 keyframes with character reference then LTX**
  - Use case: Character consistency across video sequences
  - *From: magix*

- **Single frame from each segment as input**
  - Use case: Creating longer sequences by using keyframes
  - *From: magix*

- **Extend with last frame of each sequence or add picture at start**
  - Use case: Video extension using z-image and qwen edit 2511
  - *From: Vérole*

- **Half res generation then upscaled 4 step distill**
  - Use case: Managing VRAM constraints while maintaining quality
  - *From: 305792526629994496*

- **Keyframes made in Flux 2 then LTX**
  - Use case: Creating longer narrative content with consistent characters
  - *From: ˗ˏˋ⚡ˎˊ-*

- **I2V 640x640 1st sampler + 1280x1280 upscaler**
  - Use case: Two-stage upscaling process for better quality
  - *From: Elvaxorn*

- **Audio re-take workflow for perfect video with new sound**
  - Use case: When video is perfect but audio needs retrying
  - *From: garbus*

- **Video continue/extend using gemma 3 model loader**
  - Use case: Extending existing video clips
  - *From: Mazrael.Shib*

- **T2V/I2V GGUF workflows with updated video VAE**
  - Use case: Efficient generation on 12GB/48GB systems
  - *From: U̷r̷a̷b̷e̷w̷e̷*

- **T2I2V pipeline with auto-prompting LLMs**
  - Use case: Text to image to video with automated prompt generation using LLMs and z-image creation
  - *From: GalaxyTimeMachine (RTX4090)*

- **First/Last/Middle keyframe workflow**
  - Use case: Creating videos with multiple keyframes but struggles with lip sync
  - *From: Simonj*

- **Frame-to-frame implementation**
  - Use case: Processing with 3 random frames for faster generation but loses lip sync
  - *From: neofuturo*

- **FFLF (First, Middle, Last Frame) extension**
  - Use case: Extending videos by using key frames with multiplier nodes
  - *From: neofuturo*

- **48fps conditioning with frame interpolation**
  - Use case: Interpolate source to 48fps, use for conditioning, then export back to 24fps for better speech quality
  - *From: ucren*

- **Multi-stage upscaling with masking**
  - Use case: Two-pass rendering with masked upscale for better audio sync quality
  - *From: ucren*

- **Audio-driven I2V with automatic calculations**
  - Use case: Modified workflow that auto-calculates frames from audio duration and separates vocals
  - *From: nikolatesla20*

- **Klein image edit for character consistency**
  - Use case: Create multiple poses and scenes from single starting image without LoRAs
  - *From: nikolatesla20*

- **Partial automation workflow for music videos**
  - Use case: Full video generation in 40 minutes including transitions
  - *From: VRGameDevGirl84(RTX 5090)*

- **IC Control workaround for GGUF lipsync**
  - Use case: Generate i2v first for camera control, then use IC Control for lipsync - slower but works
  - *From: Alpha-Neo*

- **Three-stage upscaling pipeline**
  - Use case: LTX2 Undistilled with CFG > distilled + detailed LoRAs with CFG=1 > FlashVSR for high resolution outputs
  - *From: The Shadow (NYC)*

- **Audio-to-video workflow for 16GB VRAM**
  - Use case: Can generate 1000 frames of 1280x720px videos from audio + text prompt on RTX 5080
  - *From: meakwa23*

- **Frame injection with 2 nodes**
  - Use case: Guide nodes for general guidance, inplace nodes for precise frame positioning like 'on frame 54'
  - *From: neofuturo*

- **LTX automation with re-do feature**
  - Use case: Full automation workflow with ability to re-do specific scenes by index number
  - *From: VRGameDevGirl84*

- **2-chunk 20-second video generation for 40-second output**
  - Use case: Creating longer videos by combining multiple chunks
  - *From: Vérole*

- **T2AV, TA2V, I2V, or IA2V all-in-one workflow**
  - Use case: Universal workflow supporting multiple input types
  - *From: Vérole*

- **Using SRT files for automated scene timing in music videos**
  - Use case: Creating music videos with precise scene cuts based on timing data
  - *From: VRGameDevGirl84(RTX 5090)*

- **Auto beat node for music video generation**
  - Use case: Automatically adding cuts based on beats in songs, with inputs for drums and bass
  - *From: VRGameDevGirl84(RTX 5090)*

- **Hybrid CGI-AI production setup**
  - Use case: Commercial automotive work where product is CGI but enhanced with AI
  - *From: 520191580007563264*

- **Using Flux Klein 9B for keyframe generation with LoRA and reference image**
  - Use case: Enhanced keyframe generation for video production
  - *From: 520191580007563264*

- **Film grain and color filtering in CapCut for AI look reduction**
  - Use case: Post-processing to make AI-generated content appear more natural
  - *From: VRGameDevGirl84(RTX 5090)*

- **2-stage workflow with audio and image inputs**
  - Use case: Creating videos with synchronized audio
  - *From: Janosch Simon*

- **T2AV 1-pass generation**
  - Use case: Single-pass text-to-audio-video generation
  - *From: 152993277631528960*

- **I2V with new nodes**
  - Use case: Image-to-video generation using updated workflow components
  - *From: NebSH*

- **Using Midjourney for images, CosyVoice 3 for TTS, then LTX2 for video**
  - Use case: Multi-tool pipeline for complete video creation
  - *From: Janosch Simon*


## Recommended Settings

- **Noise mask/strength for I2V**: 0.6
  - Prevents static output and deformation
  - *From: Dragonyte*

- **Steps for basic generation**: 8 steps
  - Sufficient for decent quality at 5 second clips
  - *From: Owlie*

- **WAN upscale denoise**: 0.3
  - Good balance for v2v upscaling
  - *From: VK (5080 128gb)*

- **Sampler**: res_2s
  - LTX team recommended over euler, improves quality but increases generation time
  - *From: 498275793852432384*

- **Steps for dev + distill combo**: 40 steps dev + 3 steps distill
  - Good balance for upscaling workflow
  - *From: Benjimon*

- **FPS options**: 16, 24, 48 fps
  - Various frame rates supported and tested
  - *From: TK_999*

- **LoRA strength testing**: 0.6, 0.8, 0.9
  - Different strengths tested, can disable on upscaler stage
  - *From: NebSH*

- **CFG**: 3.5
  - Used in high-quality 1920x1088 generation
  - *From: gopnik*

- **Steps**: 40
  - Used for detailed high-resolution outputs
  - *From: gopnik*

- **FPS**: 24
  - Standard frame rate for cinematic results
  - *From: gopnik*

- **Sampler**: euler_ancestral
  - Produces good results in high-resolution generations
  - *From: gopnik*

- **Distilled LoRA strength**: 1
  - Full strength when using distilled model
  - *From: gopnik*

- **Detailer LoRA strength**: 0.75
  - Applied to both stage 1 and 2 for enhanced detail
  - *From: gopnik*

- **Reserve VRAM**: 6
  - Prevents OOM errors on RTX 4090
  - *From: gopnik*

- **CFG**: 4
  - Used with Euler sampler for audio continuity workflow
  - *From: Tachyon*

- **Compression**: 33
  - Used for first and last frame processing
  - *From: Vérole*

- **Force**: 1
  - Used with compression setting for frame processing
  - *From: Vérole*

- **Denoise**: 0.3
  - Used with LoRA generation
  - *From: VK (5080 128gb)*

- **Distilled LoRA strength**: 0.5
  - Used with 20 steps cfg 3 for distill
  - *From: NebSH*

- **CFG**: 3
  - Used with distill 0.5 20 steps
  - *From: NebSH*

- **CFG**: 4
  - Used with no distill 40 steps
  - *From: NebSH*

- **VAE Decode tiling**: 2/8/16/8
  - Best setting for reducing grid patterns but doubles VRAM use
  - *From: garbus*

- **Detail daemon start**: 0.8
  - Set start point for detail daemon sampler
  - *From: jiffyam*

- **FPS**: 25
  - Temporal upscaler expects 25 fps, fixes jerkyness
  - *From: HeadOfOliver*

- **Distilled lora strength**: -0.50
  - Removes excessive film grain and artifacts
  - *From: Nathan Shipley*

- **Steps for distilled model**: 15
  - Works well for 720p single stage, good quality
  - *From: neofuturo*

- **CFG for dev model**: 5
  - Avoids mess that occurs at CFG 4
  - *From: Nathan Shipley*

- **Animatediff lora strength**: 2.0
  - Higher strength helps with effect, works well with deforum loras
  - *From: NebSH*

- **Audio normalization**: -23 default
  - Helps improve audio quality
  - *From: U̷r̷a̷b̷e̷w̷e̷*

- **Custom sigmas for distilled upscale**: 0.975, 0.909375, 0.725, 0.421875, 0.0
  - 4 steps instead of 3 for better upscaling results
  - *From: dischordo*

- **Sampler configuration**: er_sde with 8 steps using distilled model
  - Produces high quality results
  - *From: GalaxyTimeMachine (RTX4090)*

- **Resolution for detail**: 1792x1088 at 32 fps
  - Good balance of detail without being full HD
  - *From: GalaxyTimeMachine (RTX4090)*

- **Maximum frames for 16GB VRAM**: 480 frames MAX at 1920x1080 (20 seconds)
  - Hardware limitation regardless of model precision
  - *From: Volkin*

- **Distilled LoRA strength**: -0.4 to -0.6
  - Fixes overbaked distilled model and improves face consistency
  - *From: ucren*

- **Audio latent multiply**: 0.75
  - Reduces exaggerated expressions in audio-driven generation
  - *From: ucren*

- **Steps for quality boost**: 8->15 steps on first pass
  - Gives noticeable quality improvement
  - *From: ucren*

- **Fast generation settings**: 7 steps, 1 CFG, LCM sampler
  - For quick generation when models stay loaded
  - *From: 152993277631528960*

- **LTXVPREPROCESS**: 0
  - Prevents issues in workflow
  - *From: Jonathan Scott Schneberg*

- **Conditioning fps**: 30-48 fps
  - Higher fps helps reduce motion artifacts
  - *From: Elvaxorn*

- **Distill LoRA strength**: -0.4
  - Debakes plastic skin issues in distilled model
  - *From: ucren*

- **Tiled spatial overlap**: 256
  - Helps reduce but doesn't eliminate VAE tiling artifacts
  - *From: Ablejones*

- **LTXImgToVideoInPlace**: 0.4 starting point
  - Controls image likeness and character consistency, needs adjustment per resolution
  - *From: mdkb*

- **LTXVPreprocess**: 10-33, usually 25
  - Prevents blancmange on face, lower if issues return
  - *From: mdkb*

- **Camera static LoRA strength**: 0.1
  - Lower strength helps with GGUF lipsync issues
  - *From: mdkb*

- **Frame count for 10 seconds**: 247 frames
  - Compensates for LTX cutting 7 frames, following 8n+1 rule gives 241
  - *From: VRGameDevGirl84(RTX 5090)*

- **CFG for undistilled model**: 4.0
  - When not using distill LoRA, should use CFG 4.0 instead of 1.0
  - *From: NebSH*

- **Distill LoRA strength for dev model**: 0.6
  - Helps control oversaturation while maintaining quality
  - *From: U̷r̷a̷b̷e̷w̷e̷*

- **Camera static LoRA**: 0.5
  - Combined with distill LoRA at -0.3 to fix camera static issues
  - *From: mdkb*

- **VHS LoRA strength**: 2.0 for maximum crispy, 1.3 for better balance
  - Control intensity of VHS effect
  - *From: 305792526629994496*

- **Steps for dev + distill workflow**: 8 steps first sampler, 3 steps second sampler
  - Efficient workflow with spatial upscale between samplers
  - *From: U̷r̷a̷b̷e̷w̷e̷*

- **Distilled LoRA strength on first sampler**: 0.2
  - For 10-second FFLF generation with motion enhancement
  - *From: Simonj*

- **Upscale distill strength**: 0.6
  - For 3-step upscaling process
  - *From: Simonj*

- **Upscale sampler steps**: 20 steps at 1/2 res, 3 steps upscale
  - Memory optimization for 16GB GPU
  - *From: Simonj*

- **Denoise for upscaling**: 0.2
  - For 2+2 steps using upscale to ksampler
  - *From: hicho*

- **Guide resolution for 1920x1024 video**: 1920x1024
  - Should match generated video resolution
  - *From: Simonj*

- **Manual sigma values Stage 1**: 1., 0.99375, 0.9875, 0.98125, 0.975, 0.909375, 0.725, 0.421875, 0.0
  - 8 steps for better quality
  - *From: U̷r̷a̷b̷e̷w̷e̷*

- **Manual sigma values Stage 2**: 0.8025, 0.6332, 0.3425, 0.0
  - 4 steps for refinement
  - *From: U̷r̷a̷b̷e̷w̷e̷*

- **Dev+lora strength**: 0.6
  - Helps maintain face quality during camera rotation
  - *From: U̷r̷a̷b̷e̷w̷e̷*

- **IC detailer lora strength**: 0.5
  - For T2V only - improves detail without breaking consistency
  - *From: U̷r̷a̷b̷e̷w̷e̷*


## Concepts Explained

- **Pickletensors**: Dangerous .pt models that can contain arbitrary Python code - avoid using them
  - *From: cyncratic*

- **Snorricam shot**: Camera technique where camera is mounted to subject's chest, keeping them centered while background moves
  - *From: NebSH*

- **Stop-motion on twos**: Animation technique with stepped/limited timing, held poses every two frames, frame registration wiggle, minimal motion blur
  - *From: The Shadow (NYC)*

- **Audio latents**: Audio spectrograms used as input for video generation, resolution tied to video resolution
  - *From: TK_999*

- **Tiled VAE decode**: Method to handle memory limitations during video decoding by processing in tiles
  - *From: Tachyon*

- **Stage 1 vs Stage 2 LoRA application**: LoRAs can be applied to either stage 1, stage 2, or both stages of the two-stage generation process, with different visual effects
  - *From: gopnik*

- **Audio masking**: Technique to preserve original audio in specific time ranges while allowing model to generate audio in other parts
  - *From: Dragonyte*

- **Object POV**: Point of view from an object's perspective, used in LoRA training
  - *From: NebSH*

- **Transition roll**: Camera transition technique that rolls/sweeps between scenes
  - *From: NebSH*

- **Hero shot**: Cinematic camera technique for dramatic angles, available as LoRA
  - *From: NebSH*

- **IC-LoRA training**: Powerful training method mentioned in official documentation
  - *From: 305792526629994496*

- **FFLF**: First Frame Last Frame workflow technique
  - *From: chancelor*

- **De-baking distill model**: Using negative lora strength to reverse distillation effects
  - *From: ucren*

- **Temporal stutter artifacts**: Jerkyness that appears every few frames in temporal upscaling
  - *From: HeadOfOliver*

- **Object permanence in LTX**: LTX has trouble maintaining consistent objects like dents throughout a video sequence
  - *From: nikolatesla20*

- **Latent frame buffer**: The memory space that holds latent video frames during processing - more important for VRAM usage than model size
  - *From: Volkin*

- **NAG node**: Allows negative conditioning even when using distilled models
  - *From: nikolatesla20*

- **Inpainting/extending**: Technique where model continues from existing video frames rather than generating from scratch, helps maintain consistency
  - *From: ucren*

- **Watery effects**: Visual quality issue where details become soft/blurred, common problem in LTX2
  - *From: Juan Gea*

- **8n+1 rule**: Video frames must follow pattern of 8n+1 (e.g., 121, 241 frames)
  - *From: N0NSens*

- **Debaking distilled model**: Using distill LoRA at negative values to reduce plastic skin artifacts in distilled models
  - *From: ucren*

- **Blancmange**: Facial artifact that appears as smooth, featureless texture, controlled by LTXVPreprocess settings
  - *From: mdkb*

- **Token limit sweet spot**: Every model has a maximum resolution/frame length sweet spot, LTX2 is more forgiving than others
  - *From: TK_999*

- **Frame injection**: Technique to inject specific frames at precise positions for controlled video transitions
  - *From: neofuturo*

- **First Last Frame workflow**: Method using specific frame indexes (0 for first, -1 for last) to control video start and end points
  - *From: VRGameDevGirl84*

- **FFLF (First Frame Last Frame)**: Video generation technique using first and last frame guidance
  - *From: Simonj*

- **I2V vs T2V mode switching**: LTX2 can switch from image-to-video mode to text-to-video mode when prompts don't match reference image
  - *From: hicho*

- **T2AV**: Text-to-Audio-Video generation capability
  - *From: 152993277631528960*


## Resources & Links

- **ComfyUI-LTXVideo workflows** (workflow)
  - https://github.com/Lightricks/ComfyUI-LTXVideo/tree/master/example_workflows
  - *From: xdestroyer*

- **ComfyUI templates PR** (repo)
  - https://github.com/comfyanonymous/ComfyUI/pull/11652
  - *From: LukeG89*

- **Merge safetensors tool** (tool)
  - https://github.com/dkotel/merge-safetensors
  - *From: Scruffy*

- **NebSH's LoRA collection** (model)
  - https://civitai.com/collections/9825789
  - *From: NebSH*

- **ComfyChainer** (tool)
  - https://github.com/XmYx/ComfyChainer
  - *From: magix*

- **Wallace and Gromit LoRA** (lora)
  - https://huggingface.co/Cseti/LTXV-13B-LoRA-Wallace_and_Gromit-v1
  - *From: ˗ˏˋ⚡ˎˊ-*

- **LTX-2 ComfyUI workflow** (workflow)
  - https://civitai.com/models/2287923/ltx-2-workflow-text-to-video-and-image-to-video
  - *From: Hell G.*

- **LTX-2 prompting guide** (guide)
  - https://ltx.io/model/model-blog/prompting-guide-for-ltx-2
  - *From: GalaxyTimeMachine (RTX4090)*

- **GalaxyAce LoRA** (lora)
  - *From: gopnik*

- **Audio input workflow template** (workflow)
  - *From: Helikaon23s*

- **Official LTX2 prompting guide** (guide)
  - https://ltx.io/model/model-blog/prompting-guide-for-ltx-2
  - *From: GalaxyTimeMachine(RTX4090)*

- **LTX2 API documentation prompting guide** (documentation)
  - https://docs.ltx.video/api-documentation/prompting-guide
  - *From: Anchorite*

- **Official prompt template** (template)
  - https://github.com/Lightricks/LTX-2/blob/main/packages/ltx-core/src/ltx_core/text_encoders/gemma/encoders/prompts/gemma_t2v_system_prompt.txt
  - *From: chancelor*

- **ComfyUI-OpenAI-API** (tool)
  - https://github.com/hekmon/comfyui-openai-api
  - *From: chancelor*

- **Vast.ai GPU rental** (service)
  - https://cloud.vast.ai/?ref_id=343946
  - *From: Xor*

- **Official LTX-2 trainer script** (repo)
  - https://github.com/Lightricks/LTX-2/blob/main/packages/ltx-trainer/README.md
  - *From: NebSH*

- **Inflate LoRA** (model)
  - https://huggingface.co/kabachuha/ltx2-inflate-it
  - *From: VK (5080 128gb)*

- **Audio workflow** (workflow)
  - https://discord.com/channels/1076117621407223829/1309520535012638740/1458505971801395424
  - *From: Vérole*

- **Hero shot LoRA shared in resources channel** (model)
  - *From: NebSH*

- **Fable show runner** (tool)
  - *From: dj47*

- **T2V/I2V GGUF workflows V1.1** (workflow)
  - https://civitai.com/models/2304098?modelVersionId=2593987
  - *From: U̷r̷a̷b̷e̷w̷e̷*

- **Deforum loras** (model)
  - https://huggingface.co/mixy89/LTXV_Deforum/tree/main
  - *From: GalaxyTimeMachine*

- **Animatediff lora** (model)
  - https://huggingface.co/Nebsh/LTX2_Animatediff_Lora/blob/main/AnimateDiff_step2000.safetensors
  - *From: 210245371002093570*

- **Community showcase video** (video)
  - https://www.youtube.com/watch?v=7uaU4Rm7fEo#t=13m27s
  - *From: 210245371002093570*

- **Camera techniques video** (educational)
  - https://www.youtube.com/watch?v=j2bUsYemG-M
  - *From: Arts Bro*

- **ComfyUI_Yvann-Nodes** (repo)
  - https://github.com/yvann-ba/ComfyUI_Yvann-Nodes
  - *From: Golden*

- **Kijai's LTXV chunk feedforward** (workflow)
  - https://github.com/kijai/ComfyUI/blob/ltx2_memory/comfy/ldm/lightricks/av_model.py
  - *From: Peera*

- **Twin Peaks Episode 8 reference footage** (reference)
  - https://www.youtube.com/watch?v=Xrnm1dxUIEQ
  - *From: Arts Bro*

- **ComfyUI-AudioSR** (tool)
  - https://github.com/Saganaki22/ComfyUI-AudioSR
  - *From: ucren*

- **ComfyUI-NovaSR** (tool)
  - https://github.com/Saganaki22/ComfyUI-NovaSR
  - *From: justinj*

- **NovaSR** (repo)
  - https://github.com/ysharma3501/NovaSR
  - *From: justinj*

- **LTX LLM for questions** (tool)
  - https://discord.com/channels/1076117621407223829/1460390123547000935
  - *From: jiffyam*

- **FirstFrameGo paper** (research)
  - https://firstframego.github.io/
  - *From: NebSH*

- **Flux Klein Image Edit** (model)
  - *From: nikolatesla20*

- **ComfyUI-Egregora-Audio-Super-Resolution** (tool)
  - https://github.com/lucasgattas/ComfyUI-Egregora-Audio-Super-Resolution
  - *From: HeadOfOliver*

- **Test-time training for video** (repo)
  - https://github.com/test-time-training/ttt-video-dit
  - *From: dj47*

- **AnimateDiff LoRA for LTX2** (lora)
  - https://huggingface.co/Nebsh/LTX2_Animatediff_style/
  - *From: neofuturo*

- **South Park LoRA** (lora)
  - https://discord.com/channels/1076117621407223829/1464203426496778386
  - *From: NebSH*

- **Snorricam LoRA** (lora)
  - https://civitai.com/models/1557338/snorricam
  - *From: NebSH*

- **12GB GGUF Workflows Collection** (workflow)
  - https://civitai.com/models/2304098?modelVersionId=2623604
  - *From: U̷r̷a̷b̷e̷w̷e̷*

- **ComfyUI AudioTools** (tool)
  - https://github.com/Urabewe/ComfyUI-AudioTools
  - *From: U̷r̷a̷b̷e̷w̷e̷*

- **VCR LoRA for LTX2** (lora)
  - *From: 305792526629994496*

- **AnimateDiff LoRA** (lora)
  - *From: hell2heights2*

- **Fill's LTX LoRA Image2Video Adapter** (lora)
  - https://huggingface.co/MachineDelusions/LTX-2_Image2Video_Adapter_LoRa
  - *From: 520191580007563264*

- **HeartMula local music generation** (tool)
  - https://heartmula.github.io/
  - *From: Janosch Simon*

- **LEVO local music generation** (tool)
  - https://levo-demo.github.io/
  - *From: Janosch Simon*

- **Suno song example** (resource)
  - https://suno.com/s/EsvTKVKnDv7Tow88
  - *From: Vérole*

- **YouTube video test example** (resource)
  - https://www.youtube.com/shorts/yn5UOBFls2o?feature=share
  - *From: hicho*

- **Sample video output** (resource)
  - https://www.huge.com/denrakeiw/160922-ghost-of-the-grid
  - *From: 520191580007563264*

- **Klipy video hosting** (resource)
  - https://klipy.com/gifs/misty-dance-2
  - *From: hicho*

- **OIIA Spinning Cat weights** (model)
  - https://civitai.com/models/2018677/oiia-spinning-cat
  - *From: 710895360981205003*

- **V2V matching example video** (example)
  - https://www.youtube.com/watch?v=GUXBpjHIuw0
  - *From: U̷r̷a̷b̷e̷w̷e̷*


## Known Limitations

- **Character dialogue assignment issues**
  - Actions and dialogue can bleed between characters, making narrative difficult
  - *From: dj47*

- **Body horror without NSFW training**
  - Model deliberately not trained on NSFW content leading to anatomy issues
  - *From: dj47*

- **Audio context not maintained**
  - Cannot keep same voice/character consistency across generations
  - *From: KakerMix*

- **Model doesn't recognize some military hardware**
  - No knowledge of B-17 bombers or flak guns
  - *From: Tachyon*

- **Model substitutes most celebrities when prompted**
  - Will replace celebrities with generic faces - only handful of exceptions work
  - *From: brent*

- **Inconsistent vertical motion**
  - Not yet sure when vertical motion works and when it doesn't
  - *From: gopnik*

- **Scene changes difficult to control**
  - Model prefers continuous shots over cuts, needs specific prompting techniques
  - *From: cyncratic*

- **Dead air in longer generations with short prompts**
  - Found a lot of 'dead air' waiting periods when prompt isn't long enough for frame count
  - *From: 305792526629994496*

- **Text generation inconsistency**
  - LTX prompting guide says you really can't expect consistent text in generated videos
  - *From: garbus*

- **Model defaults to human-like features**
  - The model likes to snap to humans a lot of the time, even when generating other subjects
  - *From: Benjimon*

- **Face quality degradation**
  - Loss of detail pretty quickly into the video, face warping and eye issues common
  - *From: Phr00t*

- **Violence and adult content restrictions**
  - Model has limitations with violence and nudity generation, likely due to training data restrictions
  - *From: dj47*

- **Audio quality needs improvement**
  - Audio quality needs a bump, sounds generic like tutorial narrator voice
  - *From: HeadOfOliver*

- **Japanese language understanding**
  - LTX2 doesn't understand Japanese very well
  - *From: DreamWeebs*

- **Prompt comprehension**
  - Prompt comprehension is poor, takes many generations to get something correct
  - *From: nikolatesla20*

- **Text generation**
  - Text is generally an issue for LTX
  - *From: dj47*

- **Character consistency in longer sequences**
  - Characters change too much in longer sequences
  - *From: NebSH*

- **Beatboxing concept**
  - LTX doesn't know what beatboxing is but can work with some prompting
  - *From: N0NSens*

- **Speed advantage negated by higher steps/detailed samplers**
  - Using res_2s or higher steps defeats the speed benefits LTX team promotes
  - *From: nikolatesla20*

- **Temporal upscaler artifacts above 241 frames**
  - Strange temporal stutter artifacts when going above 241 frames
  - *From: HeadOfOliver*

- **Characters forgotten when moving out of frame**
  - Model forgets non-human character details when they move out of frame
  - *From: Mazrael.Shib*

- **Scene cuts break image guidance**
  - Image guidance doesn't survive when LTX decides to do scene cuts
  - *From: BitPoet*

- **Prompt comprehension issues**
  - Complex actions like car lifting require many attempts vs other models
  - *From: nikolatesla20*

- **Detail lora causes problems with flat 2D anime generations**
  - Using detail lora with anime style causes issues
  - *From: Choowkee*

- **Can't handle upside down objects well**
  - Asking for flipped cars or upside down things creates monstrosities
  - *From: nikolatesla20*

- **Fast movement creates mouth and teeth issues**
  - Any fast movement, even at 2048x800 raw resolution, creates problems with facial features
  - *From: Arts Bro*

- **Audio quality lacks layers**
  - Audio needs more layers for background noises like wind, rain, waves, destruction - not just voice
  - *From: GalaxyTimeMachine (RTX4090)*

- **Struggles with smaller faces**
  - Generally has trouble with smaller faces in frame, gets better when camera is closer
  - *From: Simonj*

- **Difficulty following complex prompts accurately**
  - Hard to get accurate scene following with complex multi-step prompts, may need 10+ generations
  - *From: Fictiverse*

- **Face consistency in I2V with audio**
  - LTX2 changes faces significantly when using custom audio, especially with non-famous faces
  - *From: nikolatesla20*

- **Motion artifacts at higher fps for long clips**
  - 48fps conditioning creates more motion artifacts in longer extensions
  - *From: ucren*

- **Cartoon over-training**
  - Model seems overtrained on cartoons, defaults to cartoon style easily and has more distortion with animation
  - *From: nikolatesla20*

- **Watery visual effects**
  - Detail loss and soft/blurred effects that aren't production-ready quality
  - *From: Juan Gea*

- **People turning/spinning issues**
  - LTX2 does not handle people turning around or spinning well
  - *From: ucren*

- **GGUF models have lipsync issues without LoRAs**
  - Q8 dev model requires distilled LoRA or camera LoRA to achieve lipsync
  - *From: Alpha-Neo*

- **Prompt control varies between resolutions**
  - Settings that work at 256p don't work at 480p, requiring rebalancing
  - *From: mdkb*

- **Tiled VAE decoding artifacts in dark scenes**
  - Visible grid patterns appear in dark areas, can't be fully eliminated with current implementations
  - *From: ucren*

- **Audio-video mask timing trade-off**
  - Early masking preserves likeness but loses mouth movement, late masking gets movement but loses likeness
  - *From: Nekodificador*

- **Character consistency issues**
  - LTX does not maintain consistent character appearance across longer generations
  - *From: dj47*

- **Face consistency issues in video extension**
  - Consistency degrades over time, eyes don't hold together well, becomes chaotic
  - *From: mdkb*

- **Color artifacts at high vertical resolutions**
  - Vertical outputs around or over 1536 pixels get blue color hue and hallucinations at top/bottom
  - *From: dischordo*

- **Model doesn't recognize specific objects well**
  - Still doesn't know what drill presses look like
  - *From: nikolatesla20*

- **Prompt following issues**
  - LTX doesn't listen to prompts well in either dev or distilled mode
  - *From: N0NSens*

- **LTX2 struggles with mouth and eyes detail**
  - Poor quality even on closeups, needs second stage and high resolution
  - *From: hicho*

- **Low resolution always looks poor**
  - At low resolution quality is consistently bad
  - *From: nikolatesla20*

- **32GB RAM insufficient for long video generation**
  - 32GB RAM won't get you far for extended video generation
  - *From: Charlie*

- **Random switching from I2V to T2V mode**
  - Sometimes randomly switches to text-to-video instead of maintaining image-to-video, can't force it to happen consistently
  - *From: U̷r̷a̷b̷e̷w̷e̷*

- **V2V with latent low denoise performs poorly**
  - Video-to-video with low denoise latent approach is very bad compared to WAN
  - *From: hicho*

- **Grid artifacts deform faces**
  - Grid processing causes face deformation issues
  - *From: hicho*

- **Full AI production still time-consuming in post**
  - For commercial clients, especially automotive, full AI workflows require extensive post-production work
  - *From: 520191580007563264*

- **Face drift during long generations**
  - Faces lose consistency and drift significantly during video generation
  - *From: NebSH*

- **Camera rotation prompts can mess up faces**
  - 360-degree camera rotation prompts often result in face distortion
  - *From: VRGameDevGirl84(RTX 5090)*

- **IC detailer lora breaks I2V and V2V**
  - Using IC detailer lora on image-to-video or video-to-video workflows causes mismatching and face changes
  - *From: U̷r̷a̷b̷e̷w̷e̷*


## Hardware Requirements

- **Minimum VRAM**
  - Works with 4GB VRAM (reported by someone) and 3060 confirmed, but needs >64GB RAM
  - *From: Tachyon*

- **3090 performance**
  - 1:45 generation time for 5 second video at 8 steps using system swap
  - *From: Owlie*

- **4090 capability**
  - Can handle 1280x1024 resolution without dying
  - *From: TK_999*

- **High frame counts**
  - 351 frames at 720p possible on 5090, I2V OOMs over 121 frames
  - *From: NebSH*

- **RTX 6000**
  - Can handle 1920x1088 at 513 frames in ~10 minutes with full model
  - *From: 305792526629994496*

- **RTX 5090 + 64GB RAM**
  - Can do 2048x1152, needs 25GB VRAM, maxes out RAM during VAE decode
  - *From: el marzocco*

- **RTX 4090 + 24GB GPU**
  - Can handle 609 frames with specific settings
  - *From: Benjimon*

- **128GB RAM recommended**
  - Helps significantly with tiled VAE decode and longer generations
  - *From: Hell G.*

- **Full fine-tune needs 8 H100s**
  - Full model fine-tuning not feasible for most users
  - *From: dj47*

- **VRAM for different resolutions**
  - 1920x1088 takes 645 seconds on RTX 4090, 1280x1280 121 frames requires aggressive tiling settings even on RTX 5090
  - *From: gopnik*

- **RAM usage**
  - Goes up to 96GB RAM usage out of 192GB available, 64GB RAM can be limiting factor
  - *From: PATATAJEC*

- **Generation times by resolution**
  - 1920x1088: 645 seconds, 480p: 150 seconds on RTX 4090
  - *From: gopnik*

- **Upscaling performance**
  - Generation takes 2 minutes, upscaling takes 20 minutes
  - *From: N0NSens*

- **3060 12GB with 48GB RAM**
  - Successfully running LTX2
  - *From: U̷r̷a̷b̷e̷w̷e̷*

- **3090 24GB with 64GB RAM**
  - Successfully running LTX2
  - *From: clockstopper*

- **RTX 5090**
  - Running LTX2 with ComfyUI locally
  - *From: Dkamacho*

- **1280 x 732 resolution**
  - 792 frames was too many for 1920 resolution, had to use lower res
  - *From: 305792526629994496*

- **VRAM usage doubles**
  - Using 2/8/16/8 VAE decode settings doubles VRAM usage
  - *From: garbus*

- **Full HD 20 seconds possible**
  - Able to generate 1920x1080 20 second videos
  - *From: magix*

- **VRAM for 1536x1536 video**
  - Generated in 457.63 seconds on 12GB/48GB system
  - *From: U̷r̷a̷b̷e̷w̷e̷*

- **VRAM for i2v 1000x1000**
  - Works on 8GB VRAM, 32GB RAM system, takes about 550 seconds
  - *From: cocktailprawn1212*

- **RTX 6000 Ada performance**
  - 15 steps render in 5-6 minutes with 48GB VRAM
  - *From: Nathan Shipley*

- **RAM usage for WAN upscaling**
  - Uses up to 220GB RAM for 2560x1440x241 upscale, takes 20 minutes
  - *From: seitanism*

- **VRAM for 10-second 1080p generation**
  - Can generate 10-second 1080p videos with chunk feedforward modification, up from 6-second limit
  - *From: Peera*

- **VRAM frame limits**
  - 16GB VRAM can fit 480 frames MAX at 1920x1080 (20 seconds) regardless of FP16/FP8/FP4
  - *From: Volkin*

- **3060ti performance**
  - Can generate 2k images in 30 seconds on 3060ti
  - *From: neofuturo*

- **RTX 5080 16GB VRAM**
  - Can generate 10 seconds at 1280x704 resolution
  - *From: meakwa23*

- **System RAM for long videos**
  - Need adequate system RAM for 20+ second generations, 8-9GB VRAM usage typical
  - *From: garbus*

- **RTX 5090**
  - Enables very fast generation - 8 seconds of video in 30 seconds with proper settings
  - *From: 152993277631528960*

- **VRAM for distilled LoRA**
  - 7.5GB LoRA may not fit on 12GB VRAM systems
  - *From: mdkb*

- **RAM for long frame counts**
  - Less than 64GB RAM causes pagefile/swapfile usage and delayed generation speed for >241 frames
  - *From: Volkin*

- **GGUF Q8 model requirements**
  - RTX 5090 with 64GB RAM generates 10s video, RTX 4080 with 64GB RAM also works
  - *From: Alpha-Neo*

- **Generation time for 50 seconds**
  - 50 seconds at 480p took 30 minutes on RTX 3060
  - *From: mdkb*

- **40 seconds generation time**
  - Took 307 seconds on RTX 5090
  - *From: ezMan*

- **RTX 5090 for long high-res videos**
  - 32GB VRAM, can handle 1000 frames at 1280x720
  - *From: NebSH*

- **A4500 for high resolution**
  - 20GB VRAM + 28GB system RAM can generate 3072x2048 videos in 20-30 minutes using GGUF Q5
  - *From: The Shadow (NYC)*

- **RTX 5080 for audio workflows**
  - 16GB VRAM can generate 1000 frames of 1280x720px videos from audio
  - *From: meakwa23*

- **RTX 3060 12GB still viable**
  - Can run workflows with proper memory management, good value option
  - *From: U̷r̷a̷b̷e̷w̷e̷*

- **16GB VRAM performance**
  - Can handle 10-second FFLF at 1080p with memory optimizations
  - *From: Simonj*

- **32GB RAM limitation**
  - 32GB RAM insufficient for long video generation workflows
  - *From: Charlie*

- **2060 card capability**
  - Successfully generated up to 450 frames on RTX 2060
  - *From: hicho*

- **5080 16GB memory issues**
  - Struggles with controlnet, hitting memory issues where renders vary from 1-6 minutes
  - *From: VK (5080 128gb)*

- **GGUF model performance**
  - GGUF models are slower, FP4 is better alternative, but can help with memory constraints
  - *From: hicho*

- **RTX 3090 performance benchmark**
  - 589 seconds (around 10 minutes) to render 1280x720 i2v 15 second video with lipsync external audio
  - *From: nikolatesla20*

- **Generation time for 2-pass workflow**
  - ~3 minutes for generation, ~10-15 minutes for refinement
  - *From: N0NSens*

- **Higher resolution needs more GPU power**
  - User wishes for more computer power to make content at 1080p
  - *From: U̷r̷a̷b̷e̷w̷e̷*


## Community Creations

- **Snorricam LoRA** (lora)
  - Creates snorricam camera movement effect
  - *From: NebSH*

- **Switch Focus LoRA** (lora)
  - Changes focus between subjects in scene
  - *From: NebSH*

- **Bullet Time LoRA** (lora)
  - Creates Matrix-style bullet time effects
  - *From: NebSH*

- **Car Chasing LoRA** (lora)
  - Generates car chase sequences
  - *From: NebSH*

- **Through Object LoRA** (lora)
  - Camera moves through objects in scene
  - *From: NebSH*

- **62 camera motion LoRAs** (lora)
  - Collection including dolly out, 360 orbit, whip pan, crash zoom, dutch angle, flying, incline, crane shots, etc.
  - *From: NebSH*

- **Wallace and Gromit LoRA** (lora)
  - Character style LoRA working with LTX-2
  - *From: Cseti*

- **GalaxyAce LoRA** (lora)
  - Replicates early 2010s Samsung Galaxy Ace smartphone video style
  - *From: gopnik*

- **Amgery LoRA** (lora)
  - Custom trained LoRA by community member
  - *From: NebSH*

- **Audio input workflow** (workflow)
  - ComfyUI workflow for adding custom audio with timing controls
  - *From: Helikaon23s*

- **Deforum style LoRA** (lora)
  - LoRA trained by Safety Marc that adds deforum-style transformations and effects
  - *From: NebSH*

- **Character LoRA** (lora)
  - Double dolly + character LoRA for consistent character generation
  - *From: NebSH*

- **Detailer LoRA** (lora)
  - LoRA for enhancing detail in generated videos, costs $9 to train
  - *From: NebSH*

- **Hero shot LoRA** (lora)
  - 89 bucket training for cinematic hero shots
  - *From: NebSH*

- **Object POV LoRA** (lora)
  - Point of view from objects like microwave perspective
  - *From: NebSH*

- **Transition roll LoRA** (lora)
  - Fast rolling camera transitions sweeping between scenes, T2V tested
  - *From: NebSH*

- **Push to glass LoRA** (lora)
  - Camera effect LoRA
  - *From: NebSH*

- **Group photo LoRA** (lora)
  - Step 500 and 750 versions available
  - *From: burgstall*

- **Earth zoom out LoRA** (lora)
  - Step 500 and 1000 versions, shows zoom out from Earth
  - *From: burgstall*

- **Guitar playing LoRA** (lora)
  - For guitar playing scenes
  - *From: burgstall*

- **Timelapse Human LoRA** (lora)
  - Creates timelapse effects with humans
  - *From: NebSH*

- **Outfit check LoRA** (lora)
  - For outfit checking scenes
  - *From: NebSH*

- **Animatediff lora** (lora)
  - Creates animatediff-style effects, works well at strength 2.0, combines well with deforum loras
  - *From: NebSH*

- **Scooby Doo lora** (lora)
  - Character lora for Scooby Doo, creator planning to retrain from scratch
  - *From: 138234075931475968*

- **Anime character lora** (lora)
  - 700 steps out of 3000 training, showing typical anime motion
  - *From: Choowkee*

- **South Park lora** (lora)
  - Works with non-South Park prompts for style transfer
  - *From: NebSH*

- **TouchDesigner lora** (lora)
  - In training, intended for audioreactive output effects
  - *From: NebSH*

- **Beauty and the Beast lora** (lora)
  - Character lora showing good results
  - *From: JUSTSWEATERS*

- **Outfit switch LoRA** (lora)
  - Allows characters to change outfits during video, works well with other LoRAs
  - *From: NebSH*

- **Nuclear explosion LoRA** (lora)
  - Creates nuclear explosion effects
  - *From: NebSH*

- **Hand transition LoRA** (lora)
  - Creates smooth hand-based scene transitions, trained on only 6 videos
  - *From: NebSH*

- **Handheld run LoRA** (lora)
  - Creates handheld camera running motion effects
  - *From: NebSH*

- **Deep Zoom LoRA** (lora)
  - Creates deep zoom camera effects
  - *From: oumoumad*

- **Herocam LoRA** (lora)
  - Smooths out images, recommended for camera effects
  - *From: NebSH*

- **TouchDesigner + AnimateDiff LoRA combination** (lora)
  - Style and motion effects for psychedelic visuals
  - *From: NebSH*

- **Anime character LoRA training method** (lora)
  - Training with videos first, then continuing with images helps establish character likeness
  - *From: Choowkee*

- **Saturday morning cartoons LoRA** (lora)
  - 80s cartoon style LoRA for use with LTX
  - *From: U̷r̷a̷b̷e̷w̷e̷*

- **Static Camera LoRA** (lora)
  - LoRA for maintaining static camera shots
  - *From: nikolatesla20*

- **Negative training technique LoRA** (lora)
  - LoRA trained with negative strength (-1) for improved results
  - *From: 305792526629994496*

- **Audio normalization node** (node)
  - Analyzes video before segment and auto-normalizes audio to prevent volume spikes
  - *From: U̷r̷a̷b̷e̷w̷e̷*

- **Frame count calculator** (workflow)
  - Formula that calculates correct frame count following 8n+1 rule for given duration
  - *From: N0NSens*

- **AnimateDiff Lora for creepy effects** (lora)
  - LoRA for creating creepy/horror-style animations
  - *From: hell2heights2*

- **ComfyUI AudioTools** (tool)
  - Audio enhancement and normalization nodes with auto modes for V2V, requires resampy and soundfiles
  - *From: U̷r̷a̷b̷e̷w̷e̷*

- **VHS LoRA** (lora)
  - Trained on old VHS tapes from late 80s/early 90s with commercials and personal footage
  - *From: 305792526629994496*

- **LTX automation workflow with re-do feature** (workflow)
  - Full automation with ability to re-do specific scenes by index number
  - *From: VRGameDevGirl84*

- **12GB GGUF workflow collection** (workflow)
  - Complete set of GGUF-based workflows for t2v, i2v, v2v, ia2v, ta2v on 12GB cards
  - *From: U̷r̷a̷b̷e̷w̷e̷*

- **VCR LoRA** (lora)
  - Video generation LoRA trained on captioned dataset, latest version in testing
  - *From: 305792526629994496*

- **OIIA Spinning Cat LoRA** (lora)
  - First LoRA trained for LTX-2, includes sound effects
  - *From: 710895360981205003*

- **Music video automation workflow with SRT support** (workflow)
  - Automated music video generation using SRT files for scene timing
  - *From: VRGameDevGirl84(RTX 5090)*

- **Python app for SRT file creation** (tool)
  - App that plays song and lets you tap down arrow for cuts, creates SRT with start/end times
  - *From: VRGameDevGirl84(RTX 5090)*

- **Auto beat detection node** (node)
  - Node that adds cuts based on beats in songs, supports separate inputs for drums and bass
  - *From: VRGameDevGirl84(RTX 5090)*

- **Static camera control lora** (lora)
  - Helps prevent camera from wandering during generation
  - *From: Benjimon*


---

# LTX Resources - January 2026

# Ltx Resources Knowledge Base
*Extracted from Discord discussions: 2026-01-01 to 2026-02-01*


## Technical Discoveries

- **LTX Video 2 can be fine-tuned on a subject or concept in 1-2 hours**
  - Much faster than previous models like Wan 2.2 which took significant resources and time
  - *From: oumoumad*

- **Lower steps and lower LoRA strength brings back normal audio functionality**
  - Audio was a challenge in initial tests but this fixed sound working normally
  - *From: oumoumad*

- **CFG scheduling can be done with clownsampler using 15/5 split**
  - User testing 15/5 CFG split, though time between samplers almost negates the benefit
  - *From: TK_999*

- **I2V workflow fixed with noise masks issue resolved**
  - Problem was with noise masks and how they are carried on the latent state info
  - *From: Ablejones*

- **Preview issues fixed by Kijai, unrelated to PR**
  - Previews breaking when steps and steps to run == 1, disabling previews node fixed everything
  - *From: Gleb Tretyak*

- **ComfyUI now has native LoRA training capability**
  - Comfy mentioned you can train a lora in ComfyUI, works on any supported model
  - *From: TK_999*

- **Spatial upscaler doesn't need CFG, causes memory spikes**
  - Not much benefit to using CFG on upscaler pass, memory use spikes significantly
  - *From: TK_999*

- **Using LTXV Spatio Temporal Tiled VAE Decode instead of standard tile prevents freezing and improves speed by 2.5x**
  - Also helps with stability on RTX 4090
  - *From: avataraim*

- **Disabling distilled LoRA, upscale temporary, and using 25fps instead of 50fps improves performance**
  - Multiple optimizations for better speed
  - *From: avataraim*

- **Dev model requires distilled model or distilled LoRA for proper artifact removal and upscaling**
  - Dev model alone produces noise artifacts, distilled component is required even when using dev model
  - *From: Ablejones*

- **Latent normalization works better when implemented inside the sampler rather than at outer sampler level**
  - Functions with complex chained sampling and unsampling, using values like 1,1,0.5,1 per step
  - *From: Ablejones*

- **Running a step or two with CFG helps improve results**
  - Similar approach as used with WAN testing
  - *From: Ablejones*

- **LTX-2 has intentionally sparse latent space so advanced sampling may not be as useful**
  - Model limitations mean best sampling can only get most accurate output from what model can produce
  - *From: Ablejones*

- **Context length should ideally be around less than 15k, but 20k is probably fine for LTX-2**
  - This is the context limit of audio and video dimension and length. Going bigger/longer may result in more artifacts
  - *From: TK_999*

- **New ComfyUI commit drastically reduces LTX-2 VAE VRAM use**
  - Recent update to ComfyUI that significantly improves VRAM efficiency for LTX-2 VAE
  - *From: TK_999*

- **Dev model at full CFG for first stage may help quality**
  - Using pure dev model with full CFG for first stage potentially improves results
  - *From: Ablejones*

- **LTX-2 preprocess node applies h264 video compression at level 33**
  - The LTXVpreprocess node compresses images using h264 at CRF 33 to better match training data and fight static video issues
  - *From: TK_999*

- **GGUF quantized models require shorter prompts for good adherence**
  - When using quantized GGUF models, prompts should be under 200 words for good adherence
  - *From: The Shadow (NYC)*

- **Negative prompts are powerful for excluding specific styles in LTX**
  - Using negative prompts to exclude unwanted visual styles and aesthetics works effectively
  - *From: Ablejones*

- **LTX model tends to randomly add nudity unprompted**
  - Model sometimes generates nude content even when not requested, requires adding nudity to negative prompts
  - *From: hudson223*

- **Four finger generations are common issue**
  - Model frequently generates characters with four fingers instead of five
  - *From: hudson223*

- **LTX works well for Western style/Fox animation aesthetic**
  - Model performs particularly well for this specific animation style
  - *From: hudson223*

- **LTX-2 i2v LoRA adapter significantly improves image-to-video generation**
  - High-rank LoRA trained on 30,000 generated videos that eliminates need for complex workflows, image preprocessing, or ControlNet stacking for i2v
  - *From: Fill*

- **HuMo can be used as detailer for LTX-2 outputs with context windows**
  - HuMo maintains reference for higher denoising while preserving scene and lip sync, allowing stronger correction of motion artifacts
  - *From: Ablejones*

- **Using 32fps for LTX-2 then downsampling to 16fps helps with edge artifacts**
  - Generate at 32fps, select every 2nd frame to get 16fps, then RIFE back to 32fps reduces artifacting on edges
  - *From: The Shadow (NYC)*

- **First frame of LTX-2 i2v is often blurry with compression artifacts**
  - Using 2nd or 3rd frame as HuMo reference instead of first frame may improve results
  - *From: Ablejones*

- **Diagimplicit samplers work well with motion blur effects**
  - Particularly effective for achieving squash stretch feel in animations
  - *From: hudson223*

- **Memory override node with 0.01 value fixes OOM issues on 4090 with 121 frames at 1024x1024**
  - Resolved out of memory errors on second stage using v3 workflow
  - *From: scf*

- **Shift value in ModelSamplingSD3 can be cranked up to 40-50 for more denoise changes**
  - Equates to about 0.5 denoise value and is safe to use
  - *From: Ablejones*

- **LoRA + reference images gives best character consistency**
  - Combination works better than either method alone
  - *From: Eiw / Dennis*

- **60 steps makes huge difference compared to lower steps in LTX2**
  - First pass workflow with higher steps significantly improves results
  - *From: NC17z*

- **Using dev model with distilled lora at 0.4-0.6 strength gives better results than full distilled**
  - Works better for I2V than using distilled model alone
  - *From: N0NSens*

- **30 FPS gives much better results than 24/25 FPS with less artifacts**
  - Works even with 8 steps, not much slower than lower framerates
  - *From: Elvaxorn*

- **LTX2 beats WAN 2.2 on video leaderboard**
  - Can do variable frame rates, 10-20+ seconds, I2V/V2V/T2V, audio to video in one model
  - *From: Phr00t*

- **LTX-2 multiwhatever guide node works with sharksamplers**
  - Works out of the box without modification
  - *From: Ablejones*

- **LTX reacts to all audio types**
  - Speech to lips, music to bodies - reacts differently to different audio elements
  - *From: Chandler ✨ 🎈*

- **Model prompts well with animation LoRAs**
  - BTNB animation LoRA works at various weights
  - *From: hudson223*


## Troubleshooting & Solutions

- **Problem:** Expected all tensors to be on same device error
  - **Solution:** Issue occurred on 2nd stage 1st sampler, related to OOM and CFG hitting VRAM hard
  - *From: Gleb Tretyak*

- **Problem:** Preview breaking on 1 step samplers
  - **Solution:** Disable previews node when steps and steps to run == 1
  - *From: Gleb Tretyak*

- **Problem:** I2V workflow not working
  - **Solution:** Use the RES4LYF PR branch, problem was with noise masks on latent state
  - *From: Ablejones*

- **Problem:** Temporal upscaler audio mismatch
  - **Solution:** Temporal doubles fps (25->50), need to account for this in audio latent processing
  - *From: Gleb Tretyak*

- **Problem:** OOM issues on second pass
  - **Solution:** Apply 16 VRAM measurements, disable temporal upscaling, lower CFG, or use fewer steps
  - *From: Gleb Tretyak*

- **Problem:** Random no movement or lipsync
  - **Solution:** Avoid words implying stillness: static, still, frozen, locked, hold, pause. Use 'music video' in prompt or describe specific singing actions
  - *From: EnragedAntelope*

- **Problem:** Tensor size mismatch in I2V with guides
  - **Solution:** Don't upscale latent when using spatial resize, crop images instead of resizing, reapply guide conditioning on both stages
  - *From: Gleb Tretyak*

- **Problem:** Nested tensor clone error when using RES4LYF
  - **Solution:** Update to latest RES4LYF main version, remove old RES4LYF folders to avoid conflicts
  - *From: Ablejones*

- **Problem:** VAE decoding crashes at high resolutions
  - **Solution:** Lower tile size, increase system RAM or swap space - 64GB RAM still needs swap for these large models
  - *From: Ablejones*

- **Problem:** Audio and video length mismatch causing errors
  - **Solution:** Ensure audio duration matches frame count exactly - e.g., 121 frames = 4.85 sec for 25fps
  - *From: avataraim*

- **Problem:** Clownshark sampler errors with custom audio in first pass
  - **Solution:** Compare workflow to working examples, often caused by mismatch between audio and video parameters
  - *From: Arts Bro*

- **Problem:** Quick shift from start image in first few frames
  - **Solution:** Issue acknowledged but no specific solution provided yet
  - *From: Ablejones*

- **Problem:** Ghosting effects in output
  - **Solution:** Appears to be timeline/temporal coherence issue, no specific fix mentioned
  - *From: The Shadow (NYC)*

- **Problem:** Second VAE decode sometimes hangs
  - **Solution:** Customize vae decode tiled inputs to match system capabilities for particular video
  - *From: Ablejones*

- **Problem:** VAE decoding tiled artifacts visible in sky
  - **Solution:** Use more overlap and larger tiles, or try better decoder nodes
  - *From: Ablejones*

- **Problem:** Out of sync audio issues
  - **Solution:** Check if input audio is getting into sampler, ensure audio input toggle is enabled
  - *From: neofuturo*

- **Problem:** Poor mouth movement/lip sync
  - **Solution:** Prompt correctly for audio synchronization - model doesn't do it automatically, requires specific prompting
  - *From: Ablejones*

- **Problem:** ClownsharKSampler error with LTXV Set Audio Video Mask By Time
  - **Solution:** Use SamplerCustomAdvanced instead, or use Ablejones' dev fork which has a fix
  - *From: Ablejones*

- **Problem:** Page file/swap disk space size issues in containers
  - **Solution:** Increase page file size for container - not specific to workflow, occurs when decoding video at large sizes with VAE
  - *From: Ablejones*

- **Problem:** EasyFilePaths breaks core nodes due to PyTorch version conflict
  - **Solution:** Don't use EasyFilePaths as it has ultralytics dependency incompatible with PyTorch 2.10.0
  - *From: Gleb Tretyak*

- **Problem:** ClownShark workflow randomly adding 16 frames when generating
  - **Solution:** Issue may be related to addguidemulti node, chainsampler might also need it
  - *From: JUSTSWEATERS*

- **Problem:** Cannot encode larger latent with image to video node
  - **Solution:** Use WanEx I2VCustomEmbeds node and encode latents before passing in using tiled VAE encoding node
  - *From: Ablejones*

- **Problem:** Spatial upscale in chainsampler causing tensor unpacking error
  - **Solution:** Most functions don't preserve state info for continuation - need to grab and re-apply state info using separate nodes
  - *From: Ablejones*

- **Problem:** Chunk override mode incrementing filenames instead of overwriting
  - **Solution:** Use backup mode instead, as it works as expected
  - *From: mightynice*

- **Problem:** RESplain debug line causing NameError in RES4LYF
  - **Solution:** Remove debug line from latents.py line 953
  - *From: Xor*

- **Problem:** Mask size tensor mismatch in RES4LYF
  - **Solution:** Fixed in dev fork with major changes for LTX-2 compatibility
  - *From: Ablejones*

- **Problem:** FL_ImageNotes node causing Mac compatibility issues
  - **Solution:** Bypass the FL_ImageNotes nodes, likely font-related issue
  - *From: Fill*

- **Problem:** GGUF Gemma model architecture errors
  - **Solution:** Use alternative model as provided GGUF has unsupported 'gemma3' architecture
  - *From: army*

- **Problem:** Second chunk video generation becomes very slow
  - **Solution:** Speed degradation from 4min to 13min likely due to VRAM management, use clean VRAM nodes
  - *From: army*

- **Problem:** OOM on second stage with 121 frames at 1024x1024 on 4090
  - **Solution:** Use memory override node with 0.01 value
  - *From: scf*

- **Problem:** Audio normalizing node crashes with shark sampler nodes
  - **Solution:** Disconnect audio normalizing node from nodes using multiple samplers
  - *From: Ablejones*

- **Problem:** No sample_sigmas matched current timestep error
  - **Solution:** Use v1 workflow instead of v2, or switch to Ablejones fork of res4lyf
  - *From: N0NSens*

- **Problem:** Wrong T5 clip causing errors
  - **Solution:** Make sure T5 clip doesn't have 'enc' in the name
  - *From: Ablejones*

- **Problem:** Multistep samplers failing with low step counts
  - **Solution:** Steps too far apart, use fallback sampler or increase step count
  - *From: Ablejones*

- **Problem:** Bug in workflow with text encoder connector
  - **Solution:** Change text encoder connector from dev to distill
  - *From: Phr00t*

- **Problem:** Cycles resampler error
  - **Solution:** Can do cycles manually by chaining unsample/resample nodes instead of using cycles rebounds
  - *From: Ablejones*

- **Problem:** Error from LTX2 Attention Tuner
  - **Solution:** Try bypassing the LTX2 Attention Tuner node
  - *From: Ablejones*

- **Problem:** Memory efficient sageattn error
  - **Solution:** Restart ComfyUI after updating everything
  - *From: Gleb Tretyak*


## Model Comparisons

- **LQ vs HQ output quality**
  - LQ version had more vivid and natural facial expressions and gestures, though less accurate lip sync
  - *From: Rusch Meyer*

- **Dev model vs Distilled model for first pass**
  - Dev model alone cannot generate coherent video by itself, needs distilled component
  - *From: TK_999*

- **First pass only vs second pass with distill LoRA**
  - Second pass with dev+distill LoRA for 3 steps shows significant improvement over first pass alone
  - *From: TK_999*

- **res_2 vs other samplers for LTX**
  - No clear visual benefits from res_2, almost double the time for minimal gains
  - *From: The Shadow (NYC)*

- **Linear-euler vs res_2 family**
  - Linear-euler preferred for LTX2 until proper dialed workflow allows grid tests
  - *From: The Shadow (NYC)*

- **LTX-2 vs WAN 2.2**
  - LTX-2 seems better than WAN 2.2 once kinks are sorted out, at least for certain styles
  - *From: crinklypaper*

- **Dev model quality vs distilled model**
  - If dev model can't do good details at high resolution, it's much more similar to WAN 2.2 High Noise model in functionality
  - *From: Ablejones*

- **LTX-2 I2V vs WAN I2V**
  - WAN had dedicated I2V model, LTX-2 is half-way between T2V and I2V so might not be as good as dedicated model
  - *From: Ablejones*

- **LTX vs WAN for 2D animation**
  - LTX too mushy for 2D styles compared to WAN, but good for 3D animation and dialogue scenes
  - *From: dj47*

- **Dev model vs Distill model quality**
  - Haven't seen any dev model generation as good as distill model output
  - *From: Ablejones*

- **LTX vs WAN for different use cases**
  - Use WAN with hand drawn keyframes for action, LTX or infinite talk for dialogue scenes
  - *From: dj47*

- **VACE 2.1 vs other models for hand drawn animation**
  - VACE 2.1 still best for purely hand drawn animation
  - *From: dj47*

- **HuMo 14b vs 1.7b**
  - 14b much better quality but 1.7b is 3x faster. 540p vid: 4:25 with 14b vs 1:26 with 1.7b
  - *From: Ablejones*

- **Flux Klein vs ZImage**
  - ZImage more realistic, Klein has better adherence. 9b Klein on par with ZImage
  - *From: dj47*

- **HeartMula vs Suno**
  - HeartMula quality like Suno v2, limited to schlager/pop, Suno still better
  - *From: burgstall*

- **LTX i2v LoRA vs without**
  - LoRA improves image quality and motion details in T2V, better hands and natural colors
  - *From: Kevin 'Literally Who?' Abanto*

- **LTX2 vs WAN 2.2**
  - LTX2 beats WAN 2.2 on video leaderboard and offers more features like audio, longer videos, variable framerates
  - *From: Phr00t*

- **Dev model + distilled lora vs full distilled model**
  - Dev model with distilled lora at 0.4-0.6 strength gives better results, especially for I2V
  - *From: N0NSens*

- **30 FPS vs 24/25 FPS**
  - 30 FPS gives much better results with less artifacts, not significantly slower
  - *From: Elvaxorn*

- **60 steps vs lower steps**
  - 60 steps makes huge difference in quality
  - *From: NC17z*


## Tips & Best Practices

- **Use specific singing descriptions for better lip sync**
  - Context: Instead of just 'singing', use 'rapping with fierce intensity', 'lip-syncing with swagger', or 'music video performer'
  - *From: Arts Bro*

- **Add grain to input image for I2V**
  - Context: Signals to model that image is already in transition, recommended by devs along with preprocessing node
  - *From: EnragedAntelope*

- **Use image strength 0.6-0.9 for I2V**
  - Context: 1.0 is too high, 0.6-0.9 is good range to try
  - *From: Gleb Tretyak*

- **Set compression to 35 instead of 33**
  - Context: 35 is default for preprocessor node
  - *From: Gleb Tretyak*

- **Apply FPS conditioning twice with different values**
  - Context: 1 node for 1st stage with base fps, 1 node for 2nd stage with base/doubled fps
  - *From: Gleb Tretyak*

- **For faster generations skip temporal upscaling**
  - Context: Or lower resolution, use fewer steps with CFG > 1.0, or change samplers to CFG 1.0
  - *From: Ablejones*

- **Slightly open mouths help with non-human singing**
  - Context: Especially for non-human characters to avoid human mouth bleeding
  - *From: Arts Bro*

- **Add consistent grain before upscaling**
  - Context: Normalize sharpness and textures, then do detail upscaling for best results
  - *From: hudson223*

- **Use large overlap of 256 to avoid tiling artifacts in VAE decode**
  - Context: When using tiled VAE decoding
  - *From: Ablejones*

- **Resize extreme resolution output to 720p to save disk space and make Wan detailer more reasonable**
  - Context: After LTX 2x upscale stage
  - *From: Ablejones*

- **Use as large tile_size and temporal_size as hardware can handle, with smallest overlap possible without artifacts**
  - Context: For optimal tiled VAE performance
  - *From: Ablejones*

- **Use melband roformer if audio has background noise or isn't lip syncing properly**
  - Context: When working with audio that has unwanted background sounds
  - *From: Arts Bro*

- **Keep denoising low on Wan detailer stage to avoid interfering with movement or lip sync**
  - Context: When using Wan as detailer pass after LTX
  - *From: Ablejones*

- **Basic audio processing and frequency filters can help remove weird rumbling tones from LTX-2 output**
  - Context: Post-processing LTX-2 generated audio
  - *From: Ablejones*

- **Use dev model for first stage, then distill model/lora for upscale**
  - Context: This is the intended pipeline for best quality video according to devs
  - *From: Ablejones*

- **Don't add detailer in first pass**
  - Context: Adding detailer in first pass makes output much worse than without it
  - *From: scf*

- **Only run detailer when happy with LTX-2 result**
  - Context: Detailer stage takes significant time, so optimize main generation first
  - *From: Ablejones*

- **Use memory_usage_factor of 0.1 with KJ's memory usage factor override node**
  - Context: Helps prevent VRAM overflow and improves performance
  - *From: Ablejones*

- **Lower I2V strength to 0.8 instead of 1.0**
  - Context: Strength of 1 can be too much for I2V, varies based on frame count
  - *From: The Shadow (NYC)*

- **Start with 97 frames for testing mouth movements**
  - Context: Judge mouth movements and camera on LQ first, if mouths aren't moving properly, prompt is likely the issue
  - *From: Arts Bro*

- **Use detailed character descriptions for ZiT character consistency**
  - Context: When working with character-based content
  - *From: burgstall*

- **Train a LoRA for single character used across multiple videos**
  - Context: When you have one main character appearing in multiple videos
  - *From: burgstall*

- **Don't try to cut too many corners with animation**
  - Context: Quality animation still requires mindful iteration even with AI tools
  - *From: hudson223*

- **Animation LoRAs help get better looking inbetweens**
  - Context: When working on animation projects
  - *From: JUSTSWEATERS*

- **Use lower denoise for better facial expression preservation**
  - Context: When concerned about maintaining expressions, try 2 steps instead of 3 (set start step to 6/8)
  - *From: Ablejones*

- **Higher FPS helps motion quality significantly**
  - Context: More fps helps a lot with LTX-2 output quality
  - *From: dj47*

- **Use Klein for different characters instead of training LoRAs**
  - Context: For music videos with different characters, Klein works like omni model - generate consistent character images then animate with LTX
  - *From: dj47*

- **Keep resolution reasonable for Wan models**
  - Context: 720p was high resolution one month ago, LTX's compressed latent space means higher res isn't always better
  - *From: Ablejones*

- **Prompt complexity affects generation duration significantly**
  - Context: Prompt length and complexity have big impact on processing time
  - *From: hudson223*

- **Use additional face close-up images as batch inputs into HuMo reference**
  - Context: For character consistency, especially with loras
  - *From: Ablejones*

- **Try changing unsampler steps_to_run from 2 to 3 for face vibration issues**
  - Context: Will take longer (6 steps total instead of 4) but may fix face stability
  - *From: Ablejones*

- **Generate at 32fps and convert to 25fps for HuMo workflow**
  - Context: This formula works well for LTX2 to WAN21 HuMo pipeline
  - *From: The Shadow (NYC)*

- **Don't use crazy long LLM-generated prompts with LTX2**
  - Context: Simple prompts work better, model doesn't follow complex prompts well anyway
  - *From: Phr00t*

- **Use increments of 8 when increasing VAE temporal overlap**
  - Context: Should be 24 or 32, not arbitrary numbers
  - *From: Phr00t*

- **For likeness LoRA only need 30-50 clips, style LoRA needs a little more since it's more conceptual**
  - Context: LoRA training data requirements
  - *From: Golden*

- **Try bypassing mel separator node and send full audio instead of just vocals**
  - Context: When you want LTX to react to all audio elements, not just optimize for lip sync
  - *From: Chandler ✨ 🎈*

- **Second prompt box is for short extra instructions for both T2I and I2V**
  - Context: Like making sure main character wears exact same outfit all the time
  - *From: BitPoet (Chris)*


## News & Updates

- **LTX added latent normalization sampler**
  - New sampler type available in official repo
  - *From: TK_999*

- **ComfyUI now supports native LoRA training**
  - Training node available that works on any supported model
  - *From: TK_999*

- **Resource page will be updated Monday with fresh Discord scrape**
  - Will include new information from early days of LTX-2 usage
  - *From: Nathan Shipley*

- **LTX team plans to fix audio rumbling issues in version 1.5**
  - Acknowledged issue with early rumbling tones in audio generation
  - *From: TK_999*

- **RES4LYF merged to main branch**
  - Latest updates now available in main branch
  - *From: TK_999*

- **New VRAM reduction node released by KJ**
  - Memory usage factor node that allows pushing system limits properly
  - *From: BNP4535353*

- **New ComfyUI commit reduces LTX-2 VAE VRAM usage**
  - Recent update that drastically reduces VRAM requirements for LTX-2 VAE
  - *From: TK_999*

- **New version of RES4LYF workflow coming**
  - Ablejones working on fixes and improvements, should be available today or tomorrow
  - *From: Ablejones*

- **VEO now supports 4K output**
  - VEO model has been updated with 4K resolution capability
  - *From: dj47*

- **Z-image base model release coming soon**
  - Expected to be even better than current models, has been teased for months
  - *From: LarpsAI*

- **LTX-2 Image2Video Adapter LoRA released**
  - High-rank LoRA trained on 30k videos to improve i2v generation without complex workflows
  - *From: Fill*

- **Multiple datasets in processing**
  - General anime version on 50k clips, native 4k upscale model, and IC control LoRA (pose-based)
  - *From: Fill*

- **RES4LYF dev fork updated with LTX-2 fixes**
  - Major changes made for proper LTX-2 compatibility, available in dev branch
  - *From: Ablejones*

- **New version 2 of WanHuMo Detailer workflow released**
  - Uses unsampling and resampling with noise instead of denoising, maintains color better
  - *From: Ablejones*

- **KJ released new lora node to bypass audio blocks**
  - Fixes sync issues with audio input
  - *From: N0NSens*

- **New multimodal guider nodes available**
  - Seem to improve many things, may help with audio
  - *From: TK_999*

- **01.29.26 LTX2 Updates released**
  - Better control for real workflows
  - *From: The Shadow (NYC)*


## Workflows & Use Cases

- **I2V workflow with RES4LYF PR**
  - Use case: Image to video generation with proper noise mask handling
  - *From: Ablejones*

- **Audio replacement workflow based on Kijai's video-audio-continue**
  - Use case: Replace existing video's audio, prompt can be blank or used for guidance
  - *From: garbus*

- **Simplified audio-to-voice converter**
  - Use case: Streamlined audio conversion process
  - *From: Nokai*

- **I2V + audio + v2v workflow optimized for fp4/fp8/dev**
  - Use case: Low quality preview for blocking/movements, then fine control and quality maximization
  - *From: Arts Bro*

- **LTX2-Rapid-Merges LTXV-DoEverything-v2 workflow handles I2V, First to Last Frame and T2V with speed and quality optimizations**
  - Use case: Complete LTX workflow with chunk feed forward, distilled sigmas/lcm/tiled vae
  - *From: Phr00t*

- **Audio + first image to video (A2V) workflow**
  - Use case: Creating videos from audio input and starting image
  - *From: avataraim*

- **Two-pass workflow using dev model with positive distill LoRAs and Wan detailer**
  - Use case: High quality video generation with detailing pass
  - *From: Ablejones*

- **Audio reactive workflow using canny input video and IC LoRA**
  - Use case: Creating music-reactive videos for shorts content
  - *From: Trap City*

- **Z-Image / LTX-2 Unlimited-Length Image-to-Video Automation**
  - Use case: One-run automated pipeline for full-length music videos from lyrics/audio
  - *From: VRGameDevGirl84(RTX 5090)*

- **Split samplers with different loras**
  - Use case: Apply different loras to each sampler stage without model reload
  - *From: Ablejones*

- **Pure dev model with full CFG first stage**
  - Use case: Current experimental setup for potentially better quality
  - *From: Ablejones*

- **LTX to HuMo detailing pipeline**
  - Use case: Using LTX for initial generation then HuMo for upscaling with better lip sync and ID preservation
  - *From: Ablejones*

- **Single pass dev+distill chainsampling**
  - Use case: 16 steps cfg 4 with lora 0.0, then rest are cfg 1 lora 0.75
  - *From: TK_999*

- **3D projection with AI backgrounds**
  - Use case: Live action actors with out of focus AI generated backgrounds
  - *From: hudson223*

- **Motion model for inbetween frames**
  - Use case: Using motion models to generate inbetween frames that can be edited or cut
  - *From: JUSTSWEATERS*

- **LTX-2 + HuMo detailing with context windows**
  - Use case: Infinite length video detailing on any system that can run Wan, stronger artifact correction
  - *From: Ablejones*

- **Custom length scenes with SRT timestamps**
  - Use case: Music videos with variable scene lengths based on beat markers and lyric segments
  - *From: VRGameDevGirl84*

- **32fps generation with frame rate conversion**
  - Use case: Generate at 32fps, downsample to 16fps, then RIFE back to 32fps for cleaner edges
  - *From: The Shadow (NYC)*

- **Flux Klein keyframe generation adapted from VRGameDevGirl workflow**
  - Use case: Alternative to Chinese models for keyframe generation
  - *From: Eiw / Dennis*

- **WanHuMo Detailer v2 using unsampling/resampling**
  - Use case: Video enhancement with better color maintenance
  - *From: Ablejones*

- **LTX2 first pass + WAN21 HuMo second pass**
  - Use case: Two-stage video generation for higher quality output
  - *From: The Shadow (NYC)*

- **Context windows with HuMo reference control for long videos**
  - Use case: Generate videos of any length as long as you can do 41+ frames at desired resolution
  - *From: Ablejones*

- **Audio to video with voice cloning pipeline**
  - Use case: Create YouTube shorts using TTS and video generation
  - *From: NC17z*

- **Fixed LTXV-DoAlmostEverything workflow**
  - Use case: Comprehensive LTX video generation
  - *From: Phr00t*

- **Custom node for generating prompts and style from theme**
  - Use case: Automated prompt generation based on theme
  - *From: randomanum*


## Recommended Settings

- **ModelComputeDtype**: bf16 or fp16
  - Left over from bf16 model testing, may not make difference for fp8 being cast
  - *From: Ablejones*

- **Image strength for I2V**: 0.6-0.9
  - 1.0 is too high, this range works better
  - *From: Gleb Tretyak*

- **Compression setting**: 35
  - Default for preprocessor node instead of 33
  - *From: Gleb Tretyak*

- **CFG for upscaler pass**: 1.0
  - Not much benefit to higher CFG, causes memory spikes
  - *From: TK_999*

- **AnimateDiff LoRA strength**: 2.0
  - Recommended starting strength for AnimateDiff combinations
  - *From: NebSH*

- **Latent normalization**: 1,1,0.5,1 per step
  - Applies 0.5 on step 3 out of 8, leaves rest unchanged
  - *From: Ablejones*

- **Distill LoRA strength for Deforum Morphing**: 1.5
  - Higher strength for more intense morphing effect
  - *From: S4f3ty_Marc*

- **Second pass distill LoRA**: 0.75
  - Good balance for second pass refinement
  - *From: TK_999*

- **Jinx LoRA strength**: 0.9
  - Recommended to avoid overcooking from 29000 training steps
  - *From: Cseti*

- **VAE tiled decode overlap**: 256
  - Large overlap to avoid tiling artifacts
  - *From: Ablejones*

- **Resolution buckets for training**: 960x544x41;960x544x49;960x544x57;960x544x65;960x544x73;960x544x81;960x544x97;960x544x105;960x544x121;960x544x137;960x544x169;960x544x217
  - Various frame lengths for comprehensive training
  - *From: Cseti*

- **FPS**: 12 for generation, upscale to 24
  - Manages computational load while achieving target framerate
  - *From: crinklypaper*

- **Resolution for high detail runs**: 1280x720, 30fps, 361-391 frames
  - Achievable settings for detailed generation
  - *From: veldrin*

- **Distilled lora strength**: 0.42
  - Working value, though bypassing distilled sometimes gives better results
  - *From: veldrin*

- **Static camera and detailer values**: 0.10 static camera, 0.55 detailer
  - Settings used in successful 720p generation
  - *From: veldrin*

- **Memory usage factor**: 0.1
  - Prevents VRAM overflow and improves performance
  - *From: Ablejones*

- **H264 compression level**: 33 (CRF)
  - Default compression level used by LTXVpreprocess node
  - *From: TK_999*

- **Context window context_length**: Decrease to get model to run
  - Prevents situations where model can't run
  - *From: Ablejones*

- **HuMo render framerate**: 25 fps
  - Must be 25 fps for proper lip syncing, works well with LTX-2
  - *From: Ablejones*

- **HuMo sampling fps**: 25 fps
  - HuMo trained on 25fps, strict requirement for audio sync
  - *From: Ablejones*

- **HuMo context length**: 97 frames
  - Model trained at 97 frames, though 81 or lower also works
  - *From: Ablejones*

- **CFG for CausVid 1.3b**: 2.0
  - Recommended setting when using with HuMo 1.7b
  - *From: Ablejones*

- **Memory usage factor for 1024x1024**: 3.0
  - Required patch to run higher resolutions without OOM
  - *From: Ablejones*

- **HuMo denoise steps**: 2-3 steps minimum
  - Start step 6 gives 2 steps, minimum recommended for quality
  - *From: Ablejones*

- **Memory override node**: 0.01
  - Fixes OOM issues on 4090
  - *From: scf*

- **Shift value in ModelSamplingSD3**: 40-50
  - Increases denoise amount safely (equals ~0.5 denoise)
  - *From: Ablejones*

- **Distilled lora strength with dev model**: 0.4-0.6
  - Better results than full distilled model
  - *From: N0NSens*

- **Frame rate**: 30 FPS
  - Much better results than 24/25 FPS with less artifacts
  - *From: Elvaxorn*

- **Steps for first pass**: 60
  - Makes huge difference compared to lower steps
  - *From: NC17z*

- **VAE temporal overlap**: 16+ frames
  - Minimum recommended, use increments of 8 (24, 32)
  - *From: Phr00t*

- **Context size for 720x480**: 97 frames
  - Should work easily on 4090 for any length video
  - *From: Ablejones*

- **BTNB animation LoRA weight**: various weights
  - Works well for animation prompting
  - *From: hudson223*


## Concepts Explained

- **Temporal upscaling**: Uses upscale model for temporal dimension instead of spatial, doubles fps (25->50) and frame count
  - *From: Ablejones*

- **Latent normalization sampling**: New sampling method to prevent audio latents from blowing out early to distorted sounds
  - *From: TK_999*

- **ReModel series nodes**: Patches for doing style guides, the ltxv one won't work with ltx2
  - *From: Ablejones*

- **Latent normalization**: Technique that modifies latents on the fly during sampling to improve audio-video coherence, works better inside sampler than at outer level
  - *From: Ablejones*

- **Distilled model requirement**: Dev model alone produces noise artifacts and requires distilled model or LoRA component for proper artifact removal and upscaling
  - *From: Ablejones*

- **Sparse latent space**: LTX has intentionally sparse latent space for faster training and inference, which may limit effectiveness of advanced sampling techniques
  - *From: Ablejones*

- **IC LoRA**: Input Control LoRA that can be trained on specific reference inputs like luminance maps to drive aspects of video generation
  - *From: oumoumad*

- **Context length limit**: The context limit of audio and video dimension and length that affects artifact levels - ideally under 15k, max 20k
  - *From: TK_999*

- **LTXVpreprocess node**: Node that applies h264 video compression to images to better match training data and fight against static video issues
  - *From: TK_999*

- **VAE decoding tiled artifacts**: Visual artifacts that appear during VAE decoding, especially visible in areas like sky, caused by tiling process
  - *From: Ablejones*

- **Attention tuning on audio**: Method for improving audio quality in multimodal generation
  - *From: Ablejones*

- **ClownGuides for audio**: Potential concept for controlling audio generation similar to visual guides
  - *From: Ablejones*

- **Context windows with HuMo**: Allows processing infinite length videos by splitting into manageable chunks while maintaining reference
  - *From: Ablejones*

- **Per-key merging for LoRAs**: Intelligent mixing method that performs separate audio and visual strength merging rather than simple loading
  - *From: Phr00t*

- **Audio stripped i2v LoRA**: Applying only visual weights from i2v LoRA while preserving original audio quality
  - *From: Phr00t*

- **Unsampling and resampling with noise**: Alternative to denoising that maintains color better in video enhancement
  - *From: Ablejones*

- **Bongmath with eta = 0.0**: Just repeats same model call unmodified, wastes time and compute without SDE noise
  - *From: Ablejones*

- **8n + 1 frame issue**: LTX generates frames in 8n+1 format which causes timing issues when trying to cut exactly on beats
  - *From: VRGameDevGirl84(RTX 5090)*

- **Chopping up movie for training data**: A 1.5 hour movie would yield 540 ten-second clips for training
  - *From: Fill*


## Resources & Links

- **Ltxv-Deforum-Morphing-Style_v1-2025** (model)
  - https://huggingface.co/s4f3tymarc/Ltxv-Deforum-Morphing-Style_v1-2025
  - *From: S4f3ty_Marc*

- **Ltxv-Deforum-Circle-Effect_v1-2025** (model)
  - https://huggingface.co/s4f3tymarc/Ltxv-Deforum-Circle-Effect_v1-2025
  - *From: S4f3ty_Marc*

- **Clay stop motion LoRA** (model)
  - https://huggingface.co/oumoumad/clay-stop-motion-lora-ngtvspc
  - *From: oumoumad*

- **Paper stop motion LoRA** (model)
  - https://huggingface.co/oumoumad/paper-stop-motion-lora-ptprnc
  - *From: oumoumad*

- **Deep zoom LoRA** (model)
  - https://huggingface.co/oumoumad/deepzoom-lora
  - *From: oumoumad*

- **Hand Transition LoRA** (model)
  - https://huggingface.co/Nebsh/HandTransition
  - *From: NebSH*

- **LTX2_Handheld_run LoRA** (model)
  - https://huggingface.co/Nebsh/LTX2_Handheld_run
  - *From: NebSH*

- **LTX2_AtomicExplosion LoRA** (model)
  - https://huggingface.co/Nebsh/LTX2_AtomicExplosion
  - *From: NebSH*

- **LTX2_Outfitswitch LoRA** (model)
  - https://huggingface.co/Nebsh/LTX2_Outfitswitch
  - *From: NebSH*

- **Arcane Jinx LoRA** (model)
  - https://civitai.com/models/2314428/ltx-2-19b-arcane-jinx-lora
  - *From: Cseti*

- **LTX2 updates Reddit post** (resource)
  - https://www.reddit.com/r/StableDiffusion/comments/1qdug07/ltx2_updates/
  - *From: TK_999*

- **RES4LYF PR for I2V fix** (repo)
  - https://github.com/ClownsharkBatwing/RES4LYF/pull/231
  - *From: TK_999*

- **DiscordChatExporter** (tool)
  - https://github.com/Tyrrrz/DiscordChatExporter
  - *From: Nathan Shipley*

- **Discord text cleaner web tool** (tool)
  - https://nathanshipley.github.io/discord-text-cleaner/
  - *From: Nathan Shipley*

- **LTX2-Rapid-Merges workflow** (workflow)
  - https://huggingface.co/Phr00t/LTX2-Rapid-Merges/blob/main/LTXV-DoEverything-v2.json
  - *From: Phr00t*

- **LTXV Spatio Temporal Tiled VAE Decode node** (node)
  - *From: avataraim*

- **Gemma 3 text encoder models** (model)
  - https://huggingface.co/Comfy-Org/ltx-2/tree/main/split_files/text_encoders
  - *From: Ablejones*

- **RES4LYF fork with latent normalization** (repo)
  - https://github.com/drozbay/res4lyf
  - *From: Ablejones*

- **AI Bongmath tutorial videos** (tutorial)
  - https://www.youtube.com/@ai_bongmath
  - *From: Ablejones*

- **ComfyUI RIFE TensorRT Auto** (tool)
  - https://github.com/silveroxides/ComfyUI_RIFE_TensorRT_Auto
  - *From: EnragedAntelope*

- **KJNodes** (repo)
  - https://github.com/kijai/ComfyUI-KJNodes
  - *From: The Shadow (NYC)*

- **MilkDrop3** (tool)
  - https://github.com/milkdrop2077/MilkDrop3
  - *From: Arts Bro*

- **Gemma 3 12B quantized model** (model)
  - https://huggingface.co/google/gemma-3-12b-it-qat-q4_0-unquantized/tree/main
  - *From: Arts Bro*

- **LTX-2 resources compilation** (resource)
  - https://github.com/wildminder/awesome-ltx2
  - *From: Abyss*

- **Updated prompting resource** (resource)
  - https://discord.com/channels/1076117621407223829/1459223128139104436/1463353304422809653
  - *From: The Shadow (NYC)*

- **Z-Image / LTX-2 Unlimited-Length Music Video Workflow** (workflow)
  - https://github.com/vrgamegirl19/comfyui-vrgamedevgirl/tree/main/Workflows
  - *From: VRGameDevGirl84(RTX 5090)*

- **ComfyUI VRGameDevGirl Custom Nodes** (custom nodes)
  - https://github.com/vrgamegirl19/comfyui-vrgamedevgirl/tree/main
  - *From: VRGameDevGirl84(RTX 5090)*

- **WAN Humo LTX-2 Music Video Prompt Creator GPT** (tool)
  - https://chatgpt.com/g/g-68d0a5a9f7b4819189bdb15c826c789c-wanhumo-ltx-2-music-video-prompt-creator
  - *From: VRGameDevGirl84(RTX 5090)*

- **Ablejones RES4LYF fork** (repo)
  - https://github.com/drozbay/res4lyf
  - *From: Ablejones*

- **LTX-2 VRAM Memory Management** (tool)
  - https://github.com/RandomInternetPreson/ComfyUI_LTX-2_VRAM_Memory_Management
  - *From: BNP4535353*

- **LTX-2 Deforum Evolution LoRA** (lora)
  - https://huggingface.co/s4f3tymarc/LTX-2_Deforum_Evolution_v1
  - *From: S4f3ty_Marc*

- **Cutout Satire LoRA** (lora)
  - https://huggingface.co/Nebsh/cutout-satire-lora/
  - *From: NebSH*

- **WAN 2.1 I2V LoRA** (lora)
  - https://huggingface.co/lightx2v/Wan2.1-Distill-Loras/blob/main/wan2.1_i2v_lora_rank64_lightx2v_4step.safetensors
  - *From: Ablejones*

- **LTX-2 19B GGUF 12GB ComfyUI workflows** (workflow)
  - https://civitai.com/models/2304098/ltx-2-19b-gguf-12gb-comfyui-workflows-5-total-t2vi2vv2via2vta2v
  - *From: U̷r̷a̷b̷e̷w̷e̷*

- **Urabewe audio nodes** (node)
  - *From: U̷r̷a̷b̷e̷w̷e̷*

- **VRGameDevGirl ComfyUI workflows** (repo)
  - https://github.com/vrgamegirl19/comfyui-vrgamedevgirl
  - *From: VRGameDevGirl84(RTX 5090)*

- **Honda Dream Generator project** (project)
  - https://www.rpa.com/work/project/honda-the-dream-generator
  - *From: hudson223*

- **LTX-2 Image2Video Adapter LoRA** (lora)
  - https://huggingface.co/MachineDelusions/LTX-2_Image2Video_Adapter_LoRa
  - *From: Fill*

- **ComfyUI Nano Banana** (node)
  - https://github.com/ru4ls/ComfyUI_Nano_Banana
  - *From: LarpsAI*

- **ComfyUI AudioTools** (node)
  - https://github.com/Urabewe/ComfyUI-AudioTools
  - *From: U̷r̷a̷b̷e̷w̷e̷*

- **RES4LYF dev fork** (repo)
  - https://github.com/drozbay/RES4LYF
  - *From: Ablejones*

- **HeartMula open source song generator** (tool)
  - https://github.com/HeartMuLa/heartlib
  - *From: dj47*

- **LTX2 Rapid Merges script** (script)
  - https://huggingface.co/Phr00t/LTX2-Rapid-Merges/blob/main/MergingScript/fancy-apply.py
  - *From: Phr00t*

- **WanExperiments** (repo)
  - https://github.com/drozbay/WanExperiments
  - *From: N0NSens*

- **ComfyUI-WanVaceAdvanced** (repo)
  - https://github.com/drozbay/ComfyUI-WanVaceAdvanced
  - *From: The Shadow (NYC)*

- **Ablejones res4lyf fork** (repo)
  - https://github.com/drozbay/res4lyf
  - *From: Ablejones*

- **Phr00t LTX2 merged models** (model)
  - https://huggingface.co/Phr00t/LTX2-Rapid-Merges
  - *From: Phr00t*

- **Next Scene LoRA** (lora)
  - https://huggingface.co/lovis93/next-scene-qwen-image-lora-2509
  - *From: Eiw / Dennis*

- **LTXV-DoEverything-v2 workflow** (workflow)
  - https://huggingface.co/Phr00t/LTX2-Rapid-Merges/blob/main/LTXV-DoEverything-v2.json
  - *From: Phr00t*

- **Video Generation Arena Leaderboard** (tool)
  - https://huggingface.co/spaces/ArtificialAnalysis/Video-Generation-Arena-Leaderboard
  - *From: Phr00t*

- **LTXV-DoAlmostEverything-v3.json** (workflow)
  - https://huggingface.co/Phr00t/LTX2-Rapid-Merges/blob/main/LTXV-DoAlmostEverything-v3.json
  - *From: Phr00t*

- **Beauty and Beast LoRA for general 2D animation** (model)
  - Available on Civitai
  - *From: JUSTSWEATERS*

- **WanExperiments nodes** (repo)
  - https://github.com/drozbay/WanExperiments
  - *From: Ablejones*

- **Kimi 2.5 LLM** (tool)
  - https://www.kimi.com/ai-models/kimi-k2-5
  - *From: pom*

- **LTX implementation with GUI and memory management** (tool)
  - https://github.com/maybleMyers/ltx
  - *From: Benjimon*

- **LTX2 prompt reference library** (resource)
  - https://ltx.io/model/model-blog/ltx-2-better-control-for-real-workflows
  - *From: The Shadow (NYC)*


## Known Limitations

- **LTXVImgToVideoInplace node is broken**
  - Breaks on 'resample', needs investigation
  - *From: Gleb Tretyak*

- **CFG hits VRAM very hard**
  - Causes OOM issues especially on second pass
  - *From: Gleb Tretyak*

- **Character bleeding in multi-character scenes**
  - Jinx LoRA mostly bleeds out when prompting for other characters but sometimes works well
  - *From: Cseti*

- **Random loss of movement or lipsync**
  - Can turn into Ken Burns effect when changing single words
  - *From: MiggyCabrera*

- **Slowest part is stopping and starting sampling**
  - Same model but doesn't start up again quickly
  - *From: Ablejones*

- **LTX-2 breaks basic ComfyUI functions**
  - Can't split sampling with audio+video in regular ComfyUI, only works in RES4LYF
  - *From: Ablejones*

- **Dev model cannot generate coherent video alone**
  - Always needs distilled component for proper results
  - *From: TK_999*

- **Spatial upscaler is fixed at 2x scale**
  - No flexibility to choose other scaling factors like 1.3x or 1.5x
  - *From: Arts Bro*

- **Character LoRAs sometimes bleed out with multiple people**
  - Jinx LoRA works sometimes with multiple people but often bleeds characteristics
  - *From: Cseti*

- **Audio generation has weird rumbling tones**
  - Basic frequency filters needed to remove unwanted low-frequency artifacts
  - *From: Ablejones*

- **Requires large amounts of system RAM**
  - Even 64GB RAM needs swap space for these large models, commonly crashes without proper swap
  - *From: Ablejones*

- **Dev model incomplete sampling effect**
  - Dev model shows incomplete sampling artifacts that are concerning for quality
  - *From: Ablejones*

- **I2V doesn't stick well to original image**
  - Model doesn't adhere rigidly to input image, tends toward creative interpretation rather than faithful reproduction
  - *From: Ablejones*

- **Audio conditioning convergence**
  - Audio conditioning shows interesting behaviors but often converges toward similar soundscapes rather than following unique inputs
  - *From: S4f3ty_Marc*

- **Prompt sensitivity**
  - Single word can totally misdirect video output, model is very sensitive to prompting
  - *From: Ablejones*

- **H.264 pixel size limits**
  - H.264 compression has hard limits on frame size, can't handle very large stadium-sized displays
  - *From: The Shadow (NYC)*

- **LTX model heavily biased toward white subjects**
  - Generates mostly white people, lots of hockey haircuts
  - *From: hudson223*

- **High speed artifacts and motion artifacts**
  - Serious issues with fast motion and general motion artifacts
  - *From: TK_999*

- **Copyright content generation**
  - Will generate copyrighted content, music, voices without awareness
  - *From: TK_999*

- **Anatomy issues**
  - Loads of anatomical problems in generated content
  - *From: TK_999*

- **Baked-in camera focus pulls**
  - Model seems to have certain camera movements built in
  - *From: TK_999*

- **Raw dev model quality issues**
  - Dev checkpoint is unwieldy and produces worse results than distill
  - *From: hudson223*

- **Latent upscale doesn't support nested tensors**
  - Cannot use standard latent upscale nodes with LTX's nested tensor format
  - *From: TK_999*

- **HuMo changes everyone into girls at high denoise**
  - Especially noticeable with male characters, may need reference from last frame instead of first
  - *From: dj47*

- **HuMo not great at wide shots**
  - Best used as detailer for medium-close up character content
  - *From: hudson223*

- **First frame of LTX-2 i2v usually poor quality**
  - Blurry with compression artifacts, better to use 2nd or 3rd frame as reference
  - *From: Ablejones*

- **Detail injection difficult with distilled models**
  - Only 2-3 enormous steps makes it hard to inject fine details like facial pores
  - *From: Ablejones*

- **LTX-2 8n + 1 frame constraint affects scene timing**
  - Custom length scenes don't align perfectly with beat markers due to frame constraints
  - *From: VRGameDevGirl84*

- **Owl mouth not detected by HuMo**
  - Reference matching fails when mouth location unclear, try lower denoise or different seed
  - *From: Ablejones*

- **LTX upscaling models introduce motion artifacts**
  - Designed more for speed, better to do 1 stage and use RIFE later
  - *From: Phr00t*

- **Quality degrades over time in long video generation**
  - Not recommended for extending videos without enhancement
  - *From: VRGameDevGirl84(RTX 5090)*

- **LTX2 doesn't follow prompts well, especially with distilled model and CFG 1**
  - Simply doesn't care what you prompt with those settings
  - *From: N0NSens*

- **Normalizing sampler doesn't fix broken audio**
  - Just an equalizer - if sound was broken, it stays broken. Doesn't work on dev models
  - *From: N0NSens*

- **Chunk feed forward node significantly slows generation**
  - Makes generation about half speed
  - *From: Ivoxx*

- **Only one audio output in certain workflows**
  - Refined audio out not connected by default, connecting it disconnects pre-fine tuned output
  - *From: buggz*

- **Cycles rebounds can be finicky**
  - May cause errors with certain guiders
  - *From: Ablejones*

- **Custom nodes run each time new chunk is generated**
  - When you only want them to run once at beginning for prompt/style creation
  - *From: randomanum*


## Hardware Requirements

- **16GB VRAM minimum for default workflows**
  - Need to apply 16 VRAM measurements for complex workflows
  - *From: Gleb Tretyak*

- **OOM issues on 5090 with 128GB RAM**
  - At 24fps/721 frames/1280x720 at HQ stage with sage attn + chunking
  - *From: drbaph*

- **24GB RTX4090 can handle workflows but freezes with high tile settings**
  - User needs to use lower tile sizes to avoid system freeze
  - *From: avataraim*

- **400 seconds generation time for 15 second video**
  - Using full workflow with temporal upscaling on RTX4090
  - *From: avataraim*

- **130 seconds after optimizations**
  - Skipping distilled LoRA, temporal upscaling, and frame rate doubling
  - *From: avataraim*

- **VRAM usage**
  - RTX 5090 mentioned as being spoiled by resources, RTX 4090 working well with optimizations
  - *From: Ablejones*

- **Training VRAM**
  - H100 peaked around 60GB VRAM for LoRA training, could use cheaper GPUs next time
  - *From: Cseti*

- **System RAM**
  - 64GB RAM still insufficient without proper swap space, crashes are common with small swap
  - *From: Ablejones*

- **Training time**
  - Around 1 day training time on H100 for LoRA with multiple resume sessions
  - *From: Cseti*

- **RIFE acceleration**
  - TensorRT version is blazing fast compared to standard ComfyUI Frame Interpolation
  - *From: EnragedAntelope*

- **VRAM for HQ long generations**
  - 48GB VRAM or more needed for HQ versions of longer generations
  - *From: Arts Bro*

- **4090 performance**
  - Takes around 4 minutes for first stage with GGUF, 20 minutes without optimizations
  - *From: AI_Fan*

- **System with 20GB VRAM and 28GB system RAM**
  - Can run GGUF Q5 LTX-2/Gemma models at high resolutions like 3072x2048
  - *From: The Shadow (NYC)*

- **GGUF model for lower VRAM**
  - GGUF workflow works well for users with VRAM limitations while maintaining quality
  - *From: VRGameDevGirl84(RTX 5090)*

- **HuMo detailing context windows**
  - Works on any system that can run Wan, enables infinite length processing
  - *From: Ablejones*

- **1024x1024 resolution**
  - Requires memory_usage_factor patch to 3.0 to avoid OOM
  - *From: Ablejones*

- **Low-end system performance**
  - A4500 with 20GB VRAM and 28GB system RAM can run workflows with heavy paging
  - *From: The Shadow (NYC)*

- **Mac M4 compatibility**
  - 64GB M4 Mac Mini Pro can load LTX-2 completely (35997.23 MB)
  - *From: buggz*

- **8GB VRAM limitations**
  - Causes slowdown in second chunk generation, first chunk 4min vs second 13min
  - *From: army*

- **4090 VRAM for 720x480 at 97 frames context**
  - Should work easily for any length video, more limited by RAM
  - *From: Ablejones*

- **128GB CPU RAM helpful for long videos**
  - Memory becomes limiting factor more than VRAM for extended generation
  - *From: NC17z*

- **RTX 6000 Pro Blackwell (96GB VRAM) for training**
  - Used for 5000 steps training, took at least 10 hours total
  - *From: oumoumad*

- **24GB VRAM (RTX 3090) for 20-30 second videos**
  - Possible at 720x480 resolution range
  - *From: NC17z*

- **Works on laptop 4090**
  - 46GB RAM used successfully
  - *From: randomanum*

- **Not great option for low VRAM/RAM**
  - Regarding the GUI implementation with memory management
  - *From: Benjimon*


## Community Creations

- **Deforum Morphing Style LoRA** (lora)
  - Originally trained for LTXv-13b.0.97, works with LTX-2, will retrain for v2
  - *From: S4f3ty_Marc*

- **Deforum Circle Effect LoRA** (lora)
  - Circle effect style for video generation
  - *From: S4f3ty_Marc*

- **Clay stop motion LoRA** (lora)
  - Creates clay stop motion style with trigger word NGTVSPC
  - *From: oumoumad*

- **Paper stop motion LoRA** (lora)
  - Creates paper stop motion style with trigger word PTPRNC
  - *From: oumoumad*

- **Deep zoom LoRA** (lora)
  - Extreme zoom effect, intended to be reversed for reveal effect, trained on hand-held objects
  - *From: oumoumad*

- **Hand Transition LoRA** (lora)
  - Creates hand transition effects
  - *From: NebSH*

- **Handheld run LoRA** (lora)
  - Creates handheld camera movement effects
  - *From: NebSH*

- **Atomic Explosion LoRA** (lora)
  - Generates atomic explosion effects
  - *From: NebSH*

- **Outfit Switch LoRA** (lora)
  - Creates outfit switching transitions
  - *From: NebSH*

- **Arcane Jinx LoRA** (lora)
  - Character LoRA for Jinx from Arcane
  - *From: Cseti*

- **Audio replacement workflow** (workflow)
  - Easily replace existing video's audio based on Kijai's video-audio-continue workflow
  - *From: garbus*

- **Simplified audio-to-voice converter** (workflow)
  - Streamlined version of audio to voice conversion
  - *From: Nokai*

- **I2V + audio + v2v workflow** (workflow)
  - Multi-stage workflow for preview and quality control
  - *From: Arts Bro*

- **LTXV Spatio Temporal Tiled VAE Decode** (node)
  - Improved VAE decode that prevents freezing and improves speed
  - *From: avataraim*

- **Luminance Map IC LoRA** (lora)
  - IC LoRA trained on luminance map references for driving video brightness/particle effects
  - *From: oumoumad*

- **WHATUSEE transition effect LoRA** (lora)
  - Creates eye zoom transition effect from person's view to first-person perspective
  - *From: burgstall*

- **Updated Deforum Morphing LoRA** (lora)
  - Morphing effects LoRA being retrained for LTX-2
  - *From: S4f3ty_Marc*

- **Jinx character LoRA** (lora)
  - 29000 step trained character LoRA, recommended strength 0.9
  - *From: Cseti*

- **LTX2 prompting resource with GPT integration** (workflow)
  - Comprehensive prompting system with reference files for GPT 5.2 Thinking model
  - *From: The Shadow (NYC)*

- **LTX-2 Deforum Evolution LoRA** (lora)
  - Fine-tuned on Deforum animations with Flux, creates hypnotic morphing animations with trigger [deforumorph]
  - *From: S4f3ty_Marc*

- **Cutout Satire LoRA** (lora)
  - LoRA for cutout/satire style video generation
  - *From: NebSH*

- **Z-Image/LTX-2 Unlimited Music Video Automation** (workflow)
  - Fully automated pipeline for creating full-length music videos from audio and lyrics
  - *From: VRGameDevGirl84(RTX 5090)*

- **LTX-2 VRAM Memory Management custom node** (tool)
  - Custom node for reducing VRAM usage with LTX-2
  - *From: BNP4535353*

- **Urabewe audio nodes** (node)
  - Audio processing nodes now available in Comfy Manager, search for 'Urabewe'
  - *From: U̷r̷a̷b̷e̷w̷e̷*

- **VRGameDevGirl automation workflow** (workflow)
  - LTX automation workflow with prompt creator
  - *From: VRGameDevGirl84(RTX 5090)*

- **DeterministicFPSResample node** (node)
  - Frame rate conversion without interpolation, works for both upsample and downsample
  - *From: The Shadow (NYC)*

- **ComfyUI AudioTools** (node)
  - Enhance and normalize audio for LTX-2, prevents dramatic audio changes in extended videos
  - *From: U̷r̷a̷b̷e̷w̷e̷*

- **LTX2 Rapid Merges** (script)
  - Per-key LoRA merging with separate audio/visual strengths and FP8 conversion
  - *From: Phr00t*

- **Custom length scenes with SRT import** (workflow)
  - App to create scene markers by playing song and hitting keyboard, generates SRT file for variable length scenes
  - *From: VRGameDevGirl84*

- **WanHuMo Detailer v2** (workflow)
  - Enhanced video detailing using unsampling/resampling technique
  - *From: Ablejones*

- **Motion enhancement LoRA** (lora)
  - LoRA for adding more motion to LTX2 generations
  - *From: Fill*

- **Deterministic FPS converter node** (node)
  - Converts image batches between different frame rates
  - *From: The Shadow (NYC)*

- **Beat-driven scene segmentation system** (workflow)
  - Analyzes audio beats and creates scene cuts with SRT timeline
  - *From: VRGameDevGirl84(RTX 5090)*

- **Character LoRA training on 33 videos** (lora)
  - Trained on 24fps 5-second clips at 1024x576 for 6000 steps
  - *From: NC17z*

- **BTNB animation LoRA** (lora)
  - Good for general 2D animation, Beauty and the Beast style
  - *From: Cseti*

- **LTX GUI implementation** (tool)
  - Built upon source repo with more features, GUI and memory management
  - *From: Benjimon*

- **Custom prompt generation node** (node)
  - Makes rules from prompt theme automatically
  - *From: randomanum*
