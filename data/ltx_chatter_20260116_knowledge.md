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
