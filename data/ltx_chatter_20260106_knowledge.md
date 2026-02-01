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
