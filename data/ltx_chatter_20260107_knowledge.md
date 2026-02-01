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
