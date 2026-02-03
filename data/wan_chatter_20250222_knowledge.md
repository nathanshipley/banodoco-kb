# Wan Chatter Knowledge Base
*Extracted from Discord discussions: 2025-02-22 to 2025-03-01*


## Technical Discoveries

- **Wan 2.1 has multiple model variants available**
  - WanX2.1-T2V-1.3B, WanX2.1-T2V-14B, WanX2.1-I2V-14B-480P, WanX2.1-I2V-14B-720P according to HuggingFace page listings
  - *From: wottso*

- **Model file sizes confirmed**
  - I2V 14B 720P model is 66GB in fp32, 16.5GB in fp8
  - *From: seitanism, Fannovel16 🇻🇳*

- **Model uses 16fps as base frame rate**
  - All samples posted are at 16fps
  - *From: JohnDopamine*

- **Model has strong prompt adherence**
  - First try success without needing to finesse prompts, follows complex scene descriptions well
  - *From: TK_999, DiXiao*

- **Model defaults to Asian people for human generation**
  - Anything involving humans without specification defaults to Asian person
  - *From: Pedro (@LatentSpacer)*

- **Wan2.1 T2V-1.3B model requires only 8.19 GB VRAM**
  - Compatible with almost all consumer-grade GPUs, can generate 5-second 480P video on RTX 4090 in about 4 minutes without optimization
  - *From: thaakeno*

- **VAE is very efficient**
  - VAE is only 250MB in bf16, much smaller than other models
  - *From: Kijai*

- **Model uses 40 transformer blocks**
  - Architecture appears familiar to other models
  - *From: Kijai*

- **Model supports CFG (Classifier-Free Guidance)**
  - Has CFG support which makes it more controllable
  - *From: Fannovel16*

- **Text encoder is heavier than the 1.3B model itself**
  - Uses umt5-xxl text encoder which is around 10-11GB
  - *From: Fannovel16*

- **Models released in fp32 format**
  - Original weights are in fp32, making them very large but convertible
  - *From: Kijai*

- **VAE is really fast and requires no config file**
  - Kijai discovered the VAE runs fast and surprisingly doesn't need any configuration file, unlike most models
  - *From: Kijai*

- **Model can generate images like Hunyuan Video**
  - Similar to HyV, it can also generate images, which helps the model and could potentially be finetuned on images
  - *From: Cseti*

- **Wan 2.1 is 35% smaller than LTX**
  - The 1.3B model is significantly smaller than LTX while still providing great quality
  - *From: Juampab12*

- **Model follows 'less steps more shift' pattern like Hunyuan**
  - Similar optimization approach to Hunyuan Video where you can reduce steps and increase shift for better results
  - *From: Fannovel16*

- **Sage-attention 2 can replace flash-attention**
  - Hacky implementation allows running on 4060 Ti 16GB with torch.compile support
  - *From: Pol*

- **DiffSynth Studio can run Wan 14B under 24GB VRAM**
  - With their settings, it uses about 20GB VRAM
  - *From: ArtOfficial*

- **Wan has minimum frame count requirement**
  - 81 frames minimum for I2V, 49 frames errors to max_seq_len error
  - *From: Kijai*

- **FP8_fast quantization causes artifacts**
  - img_embed weights at fp8 caused color/noise issues, keeping them at fp32 fixes this
  - *From: Kijai*

- **Model supports camera movement prompts**
  - Camera movement effect is very good with appropriate prompts
  - *From: Masanlong*

- **1.3B model can do higher resolutions**
  - Can be used in 2 passes: 1) generation at 480p, 2) upscaling vid2vid at 720p with low denoise and fewer steps
  - *From: CDS*

- **Hard-coded 81 frame minimum in encode_image function**
  - The model has 81 hardcoded in the encode_image function with msk = torch.ones(1, 81, height//8, width//8, device=self.device)
  - *From: ArtOfficial*

- **Generated videos have 16 fps output**
  - Regardless of model used (1.3B, 14B, i2v, t2v), the generated videos have a frame rate of 16 fps as set in wan/configs/shared_config.py
  - *From: Juampab12*

- **Flow shift significantly affects quality**
  - Lower flow shift values (3-5) produce better details than higher values (6-10), but too low causes coherence issues
  - *From: Juampab12*

- **T2V is much faster than I2V**
  - T2V generation took 130 seconds vs much longer I2V times for similar settings
  - *From: TK_999*

- **50 steps significantly improves quality over 30 steps**
  - Quality improvement is noticeable when increasing from 30 to 50 steps, but 70 steps doesn't improve much over 50
  - *From: slmonker(5090D 32GB)*

- **Camera movement prompting works well**
  - Camera movement prompting is working great on Wan, unlike HunyuanVideo where good camera movements were difficult to achieve
  - *From: mamad8*

- **1.3B model can generate 225 frames**
  - Successfully generated 225 frame t2v videos with the 1.3B model
  - *From: TK_999*

- **Video models perform better at specific resolutions**
  - From experience, video models perform way better at specific resolutions/ratio, better to target native res and upscale
  - *From: ˗ˏˋ⚡ˎˊ-*

- **VAE tiling has no quality impact**
  - VAE tiling at default settings vs no VAE tiling showed zero difference in quality
  - *From: TK_999*

- **CFG scheduling can speed up generation**
  - Using cfg 1.0 skips uncond and can potentially make it faster - half the steps at cfg 1.0, ~20 secs to gen with small model
  - *From: Kijai*

- **Model performs well with Chinese text generation**
  - Chinese text rendering works great in the model
  - *From: slmonker(5090D 32GB)*

- **CFG scheduling significantly improves I2V results**
  - Using variable CFG through generation (e.g., 6 CFG for 18 steps, then 1 CFG for 18 steps) produces better motion and quality
  - *From: JmySff*

- **FP32 text encoder produces sharper results**
  - FP32 UMT5-XXL encoder shows noticeable quality improvement over BF16, similar improvements seen across T5 family models
  - *From: Pedro (@LatentSpacer)*

- **Tiled VAE decode fixes washed out frames**
  - Regular VAE decode causes extremely washed out frames (except first), tiled VAE decode works fine
  - *From: Screeb*

- **Flow shift affects motion speed**
  - Flow shift value changes motion characteristics - shift 5 vs shift 2 produces different motion qualities
  - *From: ezMan*

- **Wan I2V can be chained for extensions**
  - Taking last frame and feeding to I2V creates nearly seamless video extensions
  - *From: ezMan*

- **Differential diffusion works well with Wan 1.3B**
  - Training-free technique that just works with the model
  - *From: spacepxl*

- **Wan I2V model behaves like an inpaint model**
  - Can feed start and end frames into it
  - *From: comfy*

- **Native implementation has color degradation with fp8**
  - Yellowish hue appears with fp8 quantization, stronger in some implementations
  - *From: Kijai*

- **PyTorch nightly with --fast flag provides speedup**
  - Uses fp16 + fp16 accumulation instead of fp16/bf16 + fp32 accumulation, 2x faster on NVIDIA GPUs
  - *From: comfy*

- **LoRAs work with Wan video models using both wrapper and native nodes**
  - Multiple users successfully tested LoRAs, including character and style LoRAs
  - *From: Kijai*

- **Wan can do video-to-video (v2v) generation**
  - Both 1.3B and 14B models support v2v functionality
  - *From: Kijai*

- **Training on 256 resolution doesn't translate as well to higher resolutions compared to Hunyuan**
  - Lower resolution training results don't scale up as effectively
  - *From: samurzl*

- **Wan training is easier than Hunyuan**
  - Better LoRA results in 2 epochs compared to hundreds with Hunyuan
  - *From: samurzl*

- **Text encoder can be quantized to fp8 without issues**
  - The text encoder works fine on fp8 quantization
  - *From: Kijai*

- **CLIP vision embeds have weak effect in video models**
  - Only difference from reference implementation is slightly different scaling to 224x224
  - *From: comfy*

- **WanImageToVideo is native in ComfyUI**
  - Need to update to use it properly
  - *From: Kijai*

- **VAE caches data that wastes VRAM**
  - 1-2GB completely wasted VRAM even for inference time, fixed in wrapper update
  - *From: Kijai*

- **Wan 1.3B and 14B models have very different performance characteristics**
  - 1.3B produces more realistic looking results while 14B looks sharper but potentially oversharpened
  - *From: Draken*

- **Model can generate beyond 81 frames**
  - Successfully generated 97 and 121 frames without looping
  - *From: GalaxyTimeMachine (RTX4090)*

- **LoRA trained on 14B partially loads on 1.3B**
  - Some keys load but outputs change minimally due to dimension differences (1536 vs 5120)
  - *From: mamad8*

- **Chinese prompts work better than English**
  - Translating prompts to Chinese gives better output 99% of the time
  - *From: Juampab12*

- **Wan LoRAs trained on T2V 14B have impact on I2V 14B**
  - LoRA trained on T2V 14B works on I2V 14B model, with better likeness preservation. User had to set weight at 1.75 for undertrained LoRA
  - *From: mamad8*

- **Dynamic CFG can boost inference speed**
  - User testing if dynamic cfg works well for speed improvements, previously used pre_cfg_comfy_nodes
  - *From: Raphaël*

- **Sage attention works with one of the sage 2.0 modes for Wan**
  - Sage works with specific sage 2.0 modes on Wan models
  - *From: Kijai*

- **Training on 244p with high frame count works well for video/motion**
  - For videos/motion with high frame count, 244p training resolution is very good. For images, 768p would be used instead
  - *From: chancelor*

- **Wan training runs oddly fast compared to Hunyuan**
  - Training Wan2.1-T2V-1.3B with ~50 videos at 244p, 60 frames, 0.0001 lr runs much faster than expected
  - *From: chancelor*

- **Motion/composition is largely determined by low frequency information in noise**
  - Motion/composition stays consistent when changing steps but not seed, more so than other video models
  - *From: spacepxl*

- **Noise augmentation prevents blurriness and adds detail**
  - Generally adds detail and can prevent blurry outputs
  - *From: Kijai*

- **Earlier LoRA blocks capture features/composition, later blocks handle details/style**
  - First 20 blocks vs last 20 blocks of LoRA show different effects - earlier blocks more for features/composition, latter for details/style
  - *From: Kijai*

- **Context windows might be worth adding for 1.3B model**
  - 1.3B model is fast enough that context windows could be beneficial
  - *From: Kijai*

- **Wan I2V with SageAttention fp8 kernel causes black images**
  - fp8_cuda kernel leads to black outputs due to precision overflow, while fp16_cuda kernel works correctly
  - *From: Doctor Shotgun*

- **ComfyUI native nodes now batch text encoder processing for 1.3B model**
  - Text encoder fix makes native implementation faster for 1.3B model
  - *From: comfy*

- **Auto offloading detection in console**
  - Console prints 'loaded partially' when auto offloading is active, 'loaded completely' when not
  - *From: comfy*

- **Wan can extend videos by using last frame as input**
  - Model maintains consistency well enough to chain generations using the final frame
  - *From: burgstall*

- **Wan 2.1 has 40 transformer blocks, block swapping moves defined blocks between GPU and CPU during inference**
  - Each inference step runs through all blocks, block swapping enables offloading for memory management
  - *From: Kijai*

- **SageAttention provides almost 25% speed improvement**
  - RTX 3090 comparison: with both sage-attention and torchcompile 476.59 seconds (14.78s/it), without both 641.94 seconds (20.31s/it)
  - *From: zezo*

- **SageAttention is the real speedup, almost twice as fast**
  - Provides significantly more speed benefit than other optimizations
  - *From: Kijai*

- **CFG drop to 0.5 technique can be used with Wan via spline editor**
  - Can send list of floats to cfg parameter in wrapper, points should match inference steps not frames
  - *From: Kijai*

- **RifleX helps prevent looping in videos longer than 81 frames**
  - Value of 4 works for Hunyuan, results in more coherent actions
  - *From: Kijai*

- **Q8 GGUF produces better quality than fp8**
  - No more ugly pixels, clearer results
  - *From: JmySff*

- **GGUF models work with standard text encoder, not gguf text encoder required**
  - Normal text encoder is compatible with GGUF model files
  - *From: JmySff*

- **Wan model uses CLIP vision model vit-h for image-to-video**
  - Same old clip vision model, the vit h
  - *From: Kijai*

- **Chinese prompts may provide better results than English**
  - Better prompt adherence observed when using Chinese language prompts
  - *From: JmySff*

- **fp16 + fp16 accumulate is 10% faster on 5090 for 1.3B model**
  - Performance improvement observed with specific precision settings
  - *From: Kijai*

- **Wan VAE is best performing VAE so far**
  - Quality assessment compared to other available VAEs
  - *From: Kijai*

- **UmT5 multilingual T5 model exhibits zero-shot cross-lingual transfer**
  - If trained on English tasks, can perform reasonably in Chinese without explicit fine-tuning due to shared embedding space
  - *From: fredbliss*

- **Wan 2.1 uses RoBERTa CLIP ViT-H for multilingual support**
  - Performs slightly worse in English compared to vanilla CLIP ViT-H but provides multilingual capability
  - *From: Pedro (@LatentSpacer)*

- **Different languages produce visual bias in generated content**
  - Each language seems to bias toward visual characteristics of that country/culture
  - *From: TK_999*

- **UmT5 allows multi-language prompting across 100+ languages**
  - All languages share embedding space, enabling mixed-language prompts and potential for undertrained language data
  - *From: fredbliss*

- **Wan author now works at company behind TeaCache**
  - Suggests potential TeaCache integration for Wan models in future
  - *From: guahunyo*

- **Wan wrapper had critical bug mixing frame count with height dimensions**
  - Frame count was being taken from height value, causing OOM errors on portraits and generating hundreds of frames instead of intended count
  - *From: Kijai*

- **FP16 accumulation significantly improves speed**
  - 18s/it with bf16 vs 14s/it with fp16 using fp8 weights
  - *From: Kijai*

- **Context schedule working for extended videos**
  - Successfully generated 165 frames and 329 frames using context scheduling, though transition quality needs work
  - *From: Kijai*

- **Emojis work in prompts with UMT5**
  - Can use emojis like '🍆' in prompts for classification and generation
  - *From: fredbliss*

- **FP16 weights significantly outperform BF16 for anatomy accuracy during fast motion**
  - During fast moving scenes like galloping horses, bf16 weights get leg positioning wrong while fp16 maintains correct gait cycles
  - *From: Kytra*

- **FloweEdit works out of the box with Wan models**
  - No modifications needed, can use existing HunyuanLoom implementation directly with Wan T2V
  - *From: Kijai*

- **Q8 GGUF is superior to FP8 quantization**
  - FP8 is a 'dumb downcast' while Q8 is more like image compression that preserves the best features
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Emoji prompts work through embedding space**
  - Emojis are tokenized and work as prompts, can be combined with multiple languages for steering
  - *From: fredbliss*

- **Chinese prompts may produce better motion**
  - Training data mix of Chinese and English, Chinese prompts sometimes help with motion generation
  - *From: Kytra*

- **1.25x latent upscale with 45% denoise on second pass cleans up 1.3B artifacts**
  - Works as fast as first pass, eliminates need for different model on second pass
  - *From: Kytra*

- **Wan has fewer failed generations compared to HunyuanVideo**
  - More consistent results, less likely to produce 'bad' outputs
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Wan 1.3B model requires very little VRAM**
  - Uses only 49% VRAM for 81 frames
  - *From: David Snow*

- **Width must divide by 16 for Wan models**
  - Getting tensor dimension errors at 1920x1080, doesn't divide with 16
  - *From: Kijai*

- **Official default steps are higher than commonly used**
  - Official repo defaults: 50 steps for i2v, 40 steps for t2v
  - *From: Doctor Shotgun*

- **Default shift values from official repo**
  - 3.0 shift for i2v 480p, 5.0 shift for everything else
  - *From: Doctor Shotgun*

- **H265 encoding reduces noise jitter**
  - Using h265 has less of that noise jitter
  - *From: Kijai*

- **Longer descriptive prompts improve prompt following**
  - I usually get better prompt following with longer and more descriptive prompts
  - *From: intervitens*


## Troubleshooting & Solutions

- **Problem:** HuggingFace space gets stuck at 95-100% generation
  - **Solution:** Wait for same amount of time with no progress, then reload page if completely frozen. Timer works separately from percentage
  - *From: DiXiao*

- **Problem:** HuggingFace space shows 'too many running tasks' error
  - **Solution:** Queue is limited to 10 people, need to wait or try later
  - *From: yo*

- **Problem:** Generation times inconsistent
  - **Solution:** 
  - *From: DiXiao*

- **Problem:** Git repository is empty
  - **Solution:** Weights are available but code not yet released, expected within hours
  - *From: Fannovel16*

- **Problem:** Models too large for most GPUs
  - **Solution:** Need quantization to fp16/fp8 or GGUF format for consumer hardware
  - *From: multiple users*

- **Problem:** PyTorch 2.6 weights_only error when loading models
  - **Solution:** Need to set weights_only=False in torch.load due to PyTorch 2.6 default change
  - *From: AJO*

- **Problem:** 14B model needs excessive VRAM
  - **Solution:** Use offload_model=True parameter, but still requires around 120GB VRAM
  - *From: DiXiao*

- **Problem:** Flash attention compilation issues on WSL
  - **Solution:** Use precompiled wheels from Kijai's HuggingFace repo
  - *From: Alisson Pereira*

- **Problem:** PyTorch 2.6 weights_only load failure
  - **Solution:** Modify vae.py line 614 to add weights_only=False parameter to torch.load
  - *From: AJO*

- **Problem:** T5 in VRAM causing OOM on 720p with 1.3B
  - **Solution:** Use T5 CPU offload with --t5_cpu flag, though it slows generation
  - *From: Parker*

- **Problem:** Zsh shell expanding * in size parameter
  - **Solution:** Put size parameter in quotes or use 'noglob' before command
  - *From: Zopiac*

- **Problem:** Flash attention import error
  - **Solution:** Reinstall CUDA/flash attention dependencies
  - *From: Kirara*

- **Problem:** 100 torch compile messages during generation
  - **Solution:** Remove debug print statements from code
  - *From: Kijai*

- **Problem:** VAE error: 'VAE' object has no attribute 'to'
  - **Solution:** Must use the Wan VAE loader node, not the standard ComfyUI VAE loader
  - *From: ArtOfficial*

- **Problem:** Nodes failing to import due to triton dependency
  - **Solution:** Install triton or use sdpa instead of sage attention (slower but works)
  - *From: Kijai*

- **Problem:** Target shape error with sampler
  - **Solution:** Fixed in latest update, pull latest version
  - *From: Kijai*

- **Problem:** Output resolution doesn't match input settings
  - **Solution:** Model uses aspect ratio of input image and adjusts dimensions, this is expected behavior
  - *From: Kijai*

- **Problem:** RifleX causing weird tiling artifacts
  - **Solution:** Set RifleX to 0 to disable it - it doesn't work with this model
  - *From: Kijai*

- **Problem:** UnboundLocalError with target_shape
  - **Solution:** Update Kijai's wrapper nodes
  - *From: Kijai*

- **Problem:** Can't swap width/height on WanVideo Empty Embeds node
  - **Solution:** Fixed - was tied to widget name
  - *From: Kijai*

- **Problem:** MPS compatibility issue
  - **Solution:** Change torch.float64 to float32 in model.py file to run on MPS
  - *From: jwool*

- **Problem:** Standalone ComfyUI missing diffusers
  - **Solution:** Run 'python.exe -m pip install -r custom_nodes\ComfyUI-WanVideoWrapper\requirements.txt' in comfy terminal
  - *From: Mecha*

- **Problem:** Getting wrong subjects (woman and cat instead of dogs)
  - **Solution:** Check workflow settings, remove unnecessary nodes like deeptranslator
  - *From: TK_999*

- **Problem:** VAE decode OOM after long generation
  - **Solution:** Save latent before VAE decode to preserve the generation
  - *From: Juampab12*

- **Problem:** AttributeError: module 'comfy.latent_formats' has no attribute 'Wan21'
  - **Solution:** ComfyUI desktop app needed update from Austin Mroz to add format information
  - *From: Austin Mroz*

- **Problem:** RuntimeError: Input type (float) and bias type (c10::BFloat16) should be the same
  - **Solution:** Related to ComfyUI startup settings, resolved with updates
  - *From: moss*

- **Problem:** VAE decode OOM during batch generation
  - **Solution:** Save latents instead of decoded videos to prevent losing entire night of generation
  - *From: Juampab12*

- **Problem:** 16GB VRAM OOM on 14B model
  - **Solution:** Use smaller resolution (480x480), increase block swap to 16, set load_device to offload_device
  - *From: zelgo_*

- **Problem:** Triton compatibility on Windows
  - **Solution:** Use woct0rdho/triton-windows repo, install matching Python version and copy libs
  - *From: slmonker(5090D 32GB)*

- **Problem:** 720p model won't generate, stuck at 0its
  - **Solution:** 480p model works, issue might be workflow-specific
  - *From: BecauseReasons*

- **Problem:** Pixelated artifacts in generated videos
  - **Solution:** Issue with corrupted text encoder download, re-download text encoder
  - *From: ingi // SYSTMS*

- **Problem:** Moiré pattern in outputs
  - **Solution:** Try different resolutions like 832x480 or 640x480, higher steps help
  - *From: ezMan*

- **Problem:** Model loops after 81 frames
  - **Solution:** 81 frames gives best results, longer durations degrade quality and cause weird behavior
  - *From: seitanism*

- **Problem:** Sage attention giving NaNs in native
  - **Solution:** First two modes work, avoid certain sage attention options
  - *From: Kijai*

- **Problem:** patch_embedding.weights error with Kijai's wrapper
  - **Solution:** Remove torch compile args node connection
  - *From: PookieNumnums*

- **Problem:** OOM issues with bf16 weights
  - **Solution:** Restart ComfyUI without --use-sage-attention flag
  - *From: Pedro (@LatentSpacer)*

- **Problem:** Input type mismatch error after node update
  - **Solution:** Update to latest version of Kijai's nodes
  - *From: Kijai*

- **Problem:** Wrong T5 model causing errors in native nodes
  - **Solution:** Use the T5 model that ComfyOrg shared
  - *From: Kijai*

- **Problem:** Native nodes don't work under 81 frames
  - **Solution:** Use minimum 81 frames for native implementation
  - *From: Kijai*

- **Problem:** Memory estimation issues with 14B models
  - **Solution:** Update to latest git for native ComfyUI - there's a fix for memory estimation code
  - *From: comfy*

- **Problem:** VAE wasting 1-2GB VRAM
  - **Solution:** Update wrapper - VAE caches stuff that wasn't being cleared
  - *From: Kijai*

- **Problem:** fp8 e4m3fn quantization crashes on 3090/below 4000 series with torch.compile
  - **Solution:** Disconnect torch.compile when using fp8 quantization on 3090s
  - *From: Kendo*

- **Problem:** I2V workflow freezing at 67%
  - **Solution:** Check model type compatibility - don't mix T2V model with I2V workflow
  - *From: Kijai*

- **Problem:** Can't generate single frame
  - **Solution:** Minimum is 5 frames, but Kijai changed min to 1 in update
  - *From: Kijai*

- **Problem:** VAE encode error: 'VAE' object has no attribute 'vae_dtype'
  - **Solution:** Use VAE from ComfyUI or use wrapper node to encode
  - *From: Kijai*

- **Problem:** Resolution compatibility issues with VAE
  - **Solution:** Width must be compatible with VAE requirements. 856 width doesn't work, try 840 or 848 (divisible by 8). 106 x 8 = 848, 105 x 8 = 840
  - *From: Kijai*

- **Problem:** Missing WanImageToVideo node after updates
  - **Solution:** Update ComfyUI. It's a core node so won't be found in custom nodes manager
  - *From: TK_999*

- **Problem:** Tensor dimension error: 'Trying to create tensor with negative dimension'
  - **Solution:** Use correct text encoder - need the one from Comfy-Org, not other versions
  - *From: GalaxyTimeMachine*

- **Problem:** Matrix multiplication shape error in native
  - **Solution:** Use fp8 text encoder instead of fp32. Download from Comfy-Org/Wan_2.1_ComfyUI_repackaged
  - *From: seitanism*

- **Problem:** Black output with torch+sage on native
  - **Solution:** Use fp16 sage instead, though may get overexposed flashing yellow output
  - *From: seitanism*

- **Problem:** Sage attention + compile gives burned output
  - **Solution:** Don't use sage attention with compile together on native WAN
  - *From: Ro*

- **Problem:** Torch compile doesn't work with GPUs under 40xx series
  - **Solution:** Remove torch compile argument for older GPUs
  - *From: ✧ฅโ๑ↀᆺↀ ๑ใฅ✧PookieNumnums*

- **Problem:** FP8 causing black output in native nodes
  - **Solution:** ComfyUI commit 0270a0b41cef69726694b189f37942a04d762c8a fixes the fp8 issue by upcasting specific operations
  - *From: comfy*

- **Problem:** Sage FP8 not working properly in native
  - **Solution:** Use 'sageattn_qk_int8_pv_fp16_triton' option, native work broken after update for FP8 weight
  - *From: Mngbg*

- **Problem:** FP8 burns output yellow for I2V
  - **Solution:** FP8 causes quality issues, wrapper works better as it excludes smaller operations from FP8 for quality
  - *From: Kijai*

- **Problem:** Strange outputs after ComfyUI update
  - **Solution:** Turn off Torch Compile and set attention to spda to verify if those are causing issues
  - *From: chancelor*

- **Problem:** TorchAO fp8dqrow compatibility issues
  - **Solution:** Use main device for load device - torchao doesn't like offloading
  - *From: Kijai*

- **Problem:** Long prompts causing issues
  - **Solution:** Fixed in recent ComfyUI update
  - *From: comfy*

- **Problem:** VRAM bug in wrapper
  - **Solution:** Kijai fixed a bug that was using 1-2GB VRAM unnecessarily
  - *From: Kijai*

- **Problem:** I2V generates black images with SageAttention
  - **Solution:** Use fp16_cuda kernel instead of fp8_cuda, or switch to xformers attention
  - *From: Doctor Shotgun*

- **Problem:** CUDA out of memory on 4090 with tiny resolution
  - **Solution:** Switch from wrapper to native nodes which have automatic offloading
  - *From: comfy*

- **Problem:** Torch compile fails on 3090 with fp8
  - **Solution:** Use fp8_e5m2 format instead of fp8_e4m3fn for torch compile on 3090
  - *From: Kijai*

- **Problem:** Native workflow extremely slow compared to wrapper
  - **Solution:** Use fp8_e4m3fn models with native nodes instead of full precision models
  - *From: Organoids*

- **Problem:** Non-blocking transfer not working on some systems
  - **Solution:** Try reducing block count until finding compatible value, or use native workflow which has automatic offloading
  - *From: Kijai*

- **Problem:** Sage Attention 'auto' mode causing issues in native
  - **Solution:** Select specific sageattention mode instead of auto
  - *From: JmySff*

- **Problem:** I2V producing completely different results in native
  - **Solution:** Make sure using I2V model, not T2V model - common mistake that surprisingly doesn't error
  - *From: seitanism*

- **Problem:** Torch compile failing on 3000 series GPUs with fp8_e4m3fn
  - **Solution:** Use e5m2 instead, it's a Triton issue not node-specific
  - *From: Kijai*

- **Problem:** Native I2V going very slow
  - **Solution:** Check for 'model partially loaded' in log indicating low VRAM mode activated, custom nodes can interfere
  - *From: Kijai*

- **Problem:** Resolution changing from input (480x480 to 512x512)
  - **Solution:** This is due to complicated divisions/multiplications with area calculations using integer divisions
  - *From: seitanism*

- **Problem:** TypeError: must be real number, not list when using spline editor
  - **Solution:** Use SamplerCustomAdvanced instead of KSampler, feed spline editor float into Scheduled CFG Guidance
  - *From: seitanism*

- **Problem:** Unexpected architecture type in GGUF file error
  - **Solution:** Update ComfyUI-GGUF nodes, not just base ComfyUI
  - *From: mamad8*

- **Problem:** I2V with sage+fp8 producing black or saturated images
  - **Solution:** Monkeypatch to force fp16 in model.py lines 114-115, though still has saturation issues
  - *From: Doctor Shotgun*

- **Problem:** Invalid size error when using enhance video node with I2V
  - **Solution:** Error in attention based on shape, shouldn't be able to change shape - investigation needed
  - *From: Kijai*

- **Problem:** headdim should be in [64, 96, 128] error on 3080ti
  - **Solution:** Update ComfyUI and refresh page
  - *From: Teslanaut*

- **Problem:** SageAttention 8+8 kernel causes black image output in I2V on Ada GPUs
  - **Solution:** Use SageAttention 8+16 triton kernel instead (sageattn_qk_int8_pv_fp16_triton)
  - *From: Doctor Shotgun*

- **Problem:** Missing sparge_wan_30_steps_1_iter.pt file
  - **Solution:** File is experimental and requires 5+ hours tuning per model variant - not ready for production use
  - *From: Kijai*

- **Problem:** ComfyUI loading MMAudio models interferes with workflow processing
  - **Solution:** Use separate workflows - generate I2V first, then queue extensions, then combine and add MMAudio
  - *From: Organoids*

- **Problem:** OOM errors with 16GB VRAM using wrapper
  - **Solution:** Increase block swapping to 25, 35, or 40. Bug was also causing frame count to be read from height dimension
  - *From: Kijai*

- **Problem:** SageAttention 2.0 causing import errors
  - **Solution:** Missing Triton compile environment. Run test script from triton windows repo to verify installation
  - *From: Kijai*

- **Problem:** GGUF models not using fp16 accumulation
  - **Solution:** Use advanced GGUF node to set precision, though some users report it doesn't work consistently
  - *From: Kijai*

- **Problem:** Exponentially longer generation times with more frames on GGUF
  - **Solution:** Caused by running out of VRAM - 6min for 33 frames vs 2hrs for 81 frames when VRAM exceeded
  - *From: Kijai*

- **Problem:** mat1 and mat2 shapes cannot be multiplied (512x768 and 4096x1536)
  - **Solution:** Use correct text encoder from Comfy-Org repo, not wrapper models
  - *From: MilesCorban*

- **Problem:** V2V workflow not working with regular VAE encode
  - **Solution:** Need specific VAE encode node from Kijai's workflow, use bf16 VAE
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Problem:** FP16 accumulation node errors without nightly torch even when disabled
  - **Solution:** Code needs fix to only check torch version when enabling, not when disabling
  - *From: Doctor Shotgun*

- **Problem:** Stippling artifacts in 1.3B model output
  - **Solution:** Use second pass with low denoise or switch to 14B model which doesn't have these issues
  - *From: David Snow*

- **Problem:** RMSNorm has no attribute comfy_cast_weights error with i2v
  - **Solution:** Use default compute instead of fp16 compute, or use sage 8+8 (but may cause black image)
  - *From: Doctor Shotgun*

- **Problem:** Black image with sage attention on i2v
  - **Solution:** sageattn_qk_int8_pv_fp8_cuda produces black image on Ada GPUs for Wan i2v
  - *From: Doctor Shotgun*

- **Problem:** Tensor size mismatch at 1920x1080
  - **Solution:** Width must divide by 16, try different resolution
  - *From: Kijai*

- **Problem:** Duplicates in preview at high resolution
  - **Solution:** Use multipass approach instead of single pass for 1920x1080
  - *From: David Snow*

- **Problem:** Grid/tile artifacts in output
  - **Solution:** Try disable VAE tiling, use higher steps (50 instead of 20), use better quants (Q8 > fp8)
  - *From: Kijai*

- **Problem:** Memory management issues with fp16 compute + sage 8+16
  - **Solution:** CPU offloading triggers differently based on VRAM usage variations
  - *From: Doctor Shotgun*


## Model Comparisons

- **Wan 2.1 vs Hunyuan Video**
  - Wan 2.1 is miles better than Hunyuan Video despite only 1B parameter difference. Massive quality differences between the models
  - *From: yi, mamad8*

- **Wan 2.1 vs current top closed-source models**
  - About one generation behind current top closed-sources, likely due to only 14B parameters while they use 30B+
  - *From: Fannovel16 🇻🇳*

- **Wan 2.1 I2V vs other I2V models**
  - I2V looks Kling levels of quality according to previews
  - *From: yi*

- **1.3B model potential vs CogVideo 5B**
  - Heard to be comparable to CogVideo 5B, might be better
  - *From: guahunyo*

- **Wan2.1 1.3B vs other models**
  - At least Kling 1.0 levels of quality despite much smaller size
  - *From: yi*

- **Wan2.1 VAE vs other VAEs**
  - Half the size of other VAEs, much more efficient
  - *From: Fannovel16*

- **Wan 2.1 vs LTX size**
  - Wan 2.1 is 35% smaller than LTX
  - *From: Juampab12*

- **Wan 2.1 quality vs model size**
  - Very impressive quality for just 1.3B parameters, comparable to SD1.5 size but for video
  - *From: Cseti*

- **Chinese vs US AI labs**
  - Chinese labs are 'lightyears ahead' while US labs fight over autocomplete
  - *From: seitanism*

- **Wan 1.3B vs Hunyuan**
  - Better than Hunyuan according to some users, much better than CogX and other non-Hunyuan models
  - *From: seitanism*

- **Wan 14B vs Hunyuan visual quality**
  - Looks worse than Hunyuan in visual fidelity but motion is better
  - *From: samurzl*

- **Wan 1.3B censorship vs SDXL**
  - Similar to SDXL censorship, way less censored than base SDXL
  - *From: yi*

- **Wan vs Kling 1.0**
  - Better than Kling 1.0, on par with it, better prompt adherence than Skyreel
  - *From: Juampab12*

- **Wan vs Hunyuan**
  - Better than Hunyuan for sure, which was a decently high bar
  - *From: Ro*

- **Wan 14B vs 3090 performance**
  - 720x480x81 is slower than Hunyuan on 3090
  - *From: burgstall*

- **Wan vs Veo2 for text creation**
  - Wan is preferred because it showed the creation of text from start to finish, while Veo2 starts mid-way
  - *From: orabazes*

- **Wan vs HunyuanVideo camera movement**
  - Wan has much better camera movement prompting than HunyuanVideo
  - *From: mamad8*

- **Wan quality vs competitors**
  - There's a huge gap between Wan and other models, they completely outclass the competition
  - *From: deleted_user_2ca1923442ba*

- **Wan I2V vs Kling quality**
  - I2V quality is close to Kling 1.5 even 1.6
  - *From: slmonker(5090D 32GB)*

- **fp8 vs bf16 quality on 1.3B**
  - Weird noise issues are exacerbated a bit but otherwise pretty minimal quality loss with fp8
  - *From: Benjaminimal*

- **bf16 VAE vs fp32 VAE**
  - Significant visual differences - fp32 produces sharper results, changes can be dramatic (different bird species)
  - *From: Kijai*

- **Wan I2V vs other open source models**
  - So much ahead of anything else in open source with Apache 2.0 license, makes everything before redundant
  - *From: Kijai*

- **Speed comparison between models**
  - 1.3B model: 2 minutes, 14B model: 20m 43s for same generation
  - *From: B1naryV1k1ng*

- **Wan vs Skyreels**
  - Compared to Wan, Skyreels feels like a toy
  - *From: slmonker(5090D 32GB)*

- **420p vs 720p model motion**
  - 420p model motion feels slower than 720p model at same resolution
  - *From: ezMan*

- **1.3B vs larger models**
  - 1.3B is more impressive and efficient, Hunyuan-level quality at same speed with less memory
  - *From: Draken*

- **480p vs 720p model**
  - 480p takes 10 minutes, 720p takes 1 hour for 81 frames on 4090. Not much quality difference, 480p + upscaler recommended
  - *From: Juampab12*

- **Open source vs API costs**
  - 1 hour 4090 generation costs ~6 cents in electricity, likely cheaper than API
  - *From: burgstall*

- **fp8 vs bf16 performance**
  - Both take roughly 30 mins for 30 steps, similar performance
  - *From: Pedro (@LatentSpacer)*

- **1.3B vs 14B model capabilities**
  - Anything that works on 1.3B (except LoRAs) works on 14B
  - *From: comfy*

- **Wan vs other closed platforms cost**
  - Fal costs 40 cents per video, Veo2 costs 50 cents per second
  - *From: intervitens*

- **Wan 1.3B vs 14B**
  - 1.3B: 36 seconds for 512x512x53, more realistic. 14B: 3min 33sec, sharper but potentially fake looking
  - *From: Kijai*

- **bf16 vs fp32 precision**
  - Only text encoder, img encoder and VAE worth running in fp32, not worth quality gains otherwise
  - *From: Pedro (@LatentSpacer)*

- **uni-pc vs euler sampler**
  - uni-pc seems to lower video quality compared to euler+simple
  - *From: slmonker(5090D 32GB)*

- **480p model vs 720p model**
  - 480p model is better than 720p model at generating 480p content on 14B
  - *From: Juampab12*

- **Wan vs Skyreels**
  - Wan works much better than skyreels out of the box but needs motion LoRAs to do specific things
  - *From: hablaba*

- **Wan vs Hunyuan visual quality**
  - Wan has 'ai vid' feel like CogVideo, Hunyuan doesn't give that feel. Hunyuan makes things lower res to avoid AI-ish look
  - *From: Draken*

- **Native vs Wrapper advantages**
  - Native exists in ComfyUI ecosystem with better compatibility, wrapper lives in its own ecosystem
  - *From: TK_999*

- **1.3B vs 14B for training costs**
  - 14B takes more VRAM, leaving less space for frames, but only about 5% more cost according to one user
  - *From: yi*

- **480p model vs all other models**
  - 480p model is better than all models together on 4090
  - *From: Janosch Simon*

- **14B vs 1.3B model quality at 720p**
  - 14B model significantly better - 1.3B is like 10% quality of 14B at 720p, not 90%. 14B is a whole other beast
  - *From: seitanism*

- **1.3B vs 14B at 480p**
  - Not too different when both generating at 480p resolution they were trained on
  - *From: Juampab12*

- **FP8_fast vs fp8dqrow speed on 5090**
  - fp8dqrow: 20/20 [00:11<00:00, 1.68it/s] - quite fast without terrible quality loss
  - *From: Kijai*

- **3B vs 14B model quality and speed**
  - 14B is sooo much better quality but 2:12 vs 12:15 generation time
  - *From: ingi // SYSTMS*

- **Wan physics vs other models**
  - Physics seem lacking compared to expectations, prioritizes image fidelity over authentic motion representation
  - *From: Zuko*

- **Native vs wrapper VRAM usage**
  - About the same VRAM usage, native might be slightly lower with automatic offloading
  - *From: Kijai*

- **480p vs 720p model memory usage**
  - Both models are 17GB so no difference in memory usage, difference only comes from resolution used
  - *From: Juampab12*

- **Wan vs Cosmos quality**
  - Wan is much cleaner, Cosmos does janky morphing while Wan maintains consistency
  - *From: Organoids*

- **1.3B vs 14B model quality**
  - 14B markedly better than 1.3B, but 1.3B not as bad as expected
  - *From: Parker*

- **I2V vs T2V models**
  - Don't even seem like same model, like from two different groups
  - *From: Draken*

- **GGUF vs fp8 quality**
  - Q8 GGUF clearly better quality, no ugly pixels
  - *From: JmySff*

- **Native vs wrapper speed**
  - Native is amazingly faster when it works
  - *From: JmySff*

- **bf16 vs fp16 for video**
  - bf16 preferred for video generation and training
  - *From: Kijai*

- **e4m3fn vs e5m2 casting**
  - Loading e4 and casting to e5 is extra lossy, should use e5 weight or bf16->e5
  - *From: Kijai*

- **fp8 vs fp8 fast**
  - fp8 fast is faster but substantially worse quality, not worth it
  - *From: David Snow*

- **Q8 GGUF vs fp8**
  - Q8 is superior to fp8 as it's a smarter way to downsample to same datatype
  - *From: ˗ˏˋ⚡ˎˊ-*

- **res4lyfe samplers - rk vs deis 2m sde**
  - Both have same generation time, visual comparison shows differences in detail
  - *From: TK_999*

- **bf16 vs fp16 precision**
  - Clear difference in eyes and background detail, though mouth quality bad on both
  - *From: Kijai*

- **Wan vs HunyuanVideo quality**
  - Wan blows away HunyuanVideo according to users
  - *From: Ada*

- **Wan compute vs other models**
  - Takes 2x compute and slightly bigger than comparable models
  - *From: Draken*

- **Wan 1.3B vs 14B quality**
  - 14B much better quality but significantly slower. 1.3B surprisingly good for size but has artifacts
  - *From: David Snow*

- **Wan 14B vs Hunyuan I2V speed on 3090**
  - Almost on par speed-wise between the two models
  - *From: ˗ˏˋ⚡ˎˊ-*

- **FP32 vs quantized quality vs speed**
  - FP32 much better quality (690s vs 352s generation time) but very slow. Question whether time difference worth it
  - *From: David Snow*

- **720p vs 480p models**
  - 720p can do 480p but 480p model is better at 480p specifically. 720p adds more detail
  - *From: David Snow*

- **FP16 vs BF16 weights**
  - FP16 significantly better quality, especially for anatomy in fast motion scenes
  - *From: Kytra*

- **Q8 GGUF vs FP8**
  - Q8 always better quality, FP8 is dumb downcast while Q8 preserves important features
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Wan vs HunyuanVideo reliability**
  - Wan produces fewer failed generations, more consistent results
  - *From: ˗ˏˋ⚡ˎˊ-*

- **1.3B vs 14B model**
  - 14B doesn't have stippling issues but extremely slow, 1.3B fast but needs artifact cleanup
  - *From: David Snow*

- **HunyuanVideo vs Wan for second pass refinement**
  - HunyuanVideo better for cleaning up Wan 1.3B artifacts and adding detail
  - *From: David Snow*

- **Wan vs Hunyuan second pass**
  - Hunyuan wins for refinement, looks more alive
  - *From: David Snow*

- **Q8 vs fp8 quality**
  - Q8 is better than fp8 in quality
  - *From: zezo*

- **Native ComfyUI vs Wrapper speed**
  - Native is ~10% faster
  - *From: Kijai*

- **fp8 vs fp16 quality**
  - fp8 quality is still lower
  - *From: Kijai*

- **Multi-pass Wan 1.3B vs 14B model**
  - Multi-pass 1.3B is much faster than using 14B model
  - *From: David Snow*

- **Wan vs Hunyuan quality**
  - Wan's quality is a bit better
  - *From: Doctor Shotgun*


## Tips & Best Practices

- **Use '3D anime' style for better results**
  - Context: When doing 3D anime style, model performs better than proper 2D
  - *From: TK_999*

- **Model works better with Asian datasets**
  - Context: Heavy bias toward Asian sources in training data
  - *From: Pedro (@LatentSpacer)*

- **Good for finetuing and LoRA training potential**
  - Context: Solid base model that should work well for specific tasks with additional training
  - *From: Pedro (@LatentSpacer), DiXiao*

- **Wait for quantized versions**
  - Context: Unless you have 80GB+ VRAM, better to wait for fp16/fp8 conversions
  - *From: seitanism*

- **Use offloading for larger models**
  - Context: Can run on 12-14GB VRAM with auto CPU offload
  - *From: slmonker*

- **1.3B model could be finetuned to I2V**
  - Context: Similar to how skyreels did with Hunyuan, possible on single A100
  - *From: Fannovel16*

- **Use shift 9 and steps 20 for better results**
  - Context: When running the 1.3B model for optimal quality/speed balance
  - *From: Fannovel16*

- **Try shift 3 for 480p video generation**
  - Context: Recommended shift parameter specifically for 480p resolution
  - *From: 片ヨ亡亡丹片*

- **Can get 4x faster with bf16 and fp8 quantization**
  - Context: Instead of using fp32 for much faster generation
  - *From: Juampab12*

- **Use torch.autocast for fp16 to reduce VRAM**
  - Context: When running into memory issues
  - *From: Fannovel16*

- **Use camera movement prompts for better effects**
  - Context: Camera movement effect is very good
  - *From: Masanlong*

- **Use supported resolutions for T2V-1.3B**
  - Context: Use --size 480*832 or --size 832*480
  - *From: AJO*

- **Start with custom nodes rather than ComfyUI core code**
  - Context: For learning ComfyUI development
  - *From: Kijai*

- **Use Chinese negative prompt for better results**
  - Context: Real negative prompt in Chinese works better than English
  - *From: Juampab12*

- **Use flow shift 4-5 for optimal quality at 30 steps**
  - Context: Lower values give better details but too low causes coherence loss
  - *From: Juampab12*

- **50 steps significantly better than 30 steps**
  - Context: Quality improvement visible, worth the extra time
  - *From: Juampab12*

- **Lower block swap for 5090 users**
  - Context: Can afford like 5 blocks with 5090 and sage attention
  - *From: Juampab12*

- **Use 10 steps for seed testing, then high steps for quality**
  - Context: Workflow optimization to find right seed quickly then render final quality
  - *From: seitanism*

- **Specify model variant when posting generations**
  - Context: Community requested labeling gens as 1.3B or 14B for clarity
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Use fp32 VAE for best quality**
  - Context: Original VAE is fp32, produces significantly better results than bf16
  - *From: Pedro (@LatentSpacer)*

- **Target native resolution and upscale later**
  - Context: Better results than generating at non-native resolutions
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Use --fp32-vae launch flag with original VAE file**
  - Context: For using original fp32 VAE quality
  - *From: comfy*

- **Use negative prompts to control camera movement**
  - Context: For static shots, try negatives like 'zoom-in, dolly, push-in' to prevent unwanted camera motion
  - *From: mamad8*

- **Test with smaller steps and FP8 first**
  - Context: Use lower step count and FP8 fast to find good seeds before running overnight with 50 steps
  - *From: seitanism*

- **Choose good stitching points for extensions**
  - Context: When chaining I2V generations, ending frames that work well for extension can create nearly seamless results
  - *From: ezMan*

- **Use FP32 for text encoder when possible**
  - Context: FP32 text encoders produce sharper results across T5 family models, worth the extra VRAM
  - *From: Pedro (@LatentSpacer)*

- **Hunt seeds with 10 steps, then use 50 steps for final quality**
  - Context: Faster workflow for quality results
  - *From: seitanism*

- **Use specific resolutions for each model**
  - Context: 720p model for 720x1280, 480p for lower resolutions to avoid artifacts
  - *From: wooden tank*

- **Stick to 81 frames for best results**
  - Context: Higher frame counts cause quality degradation and looping
  - *From: seitanism*

- **Use flux gens + Kling/Skyreels for dataset creation**
  - Context: Create training datasets for T2V LoRAs
  - *From: Kytra*

- **Start with 0 block swap and increase by 5 each time you get OOM**
  - Context: When configuring memory usage
  - *From: Juampab12*

- **Use English negative prompts**
  - Context: When getting color issues or artifacts
  - *From: codexq*

- **50+ steps looks best for animations**
  - Context: When doing anime content
  - *From: Kytra*

- **Use Subject+Scene+Action prompt structure**
  - Context: Official prompt guidance from Wan team
  - *From: slmonker(5090D 32GB)*

- **Translate prompts to Chinese for better results**
  - Context: Works 99% of the time for better output
  - *From: Juampab12*

- **Use denoise setting for video2video**
  - Context: Same as img2img in ComfyUI native nodes
  - *From: Kijai*

- **Use 0.5 denoise for v2v by cutting sigmas in half**
  - Context: For video2video workflows
  - *From: Kijai*

- **1.3B is the best part of Wan release**
  - Context: Good balance of speed vs quality
  - *From: Draken*

- **Use Chinese translation for prompts**
  - Context: Both positive and negative prompts should be translated into Chinese before feeding into prompt
  - *From: B1naryV1k1ng*

- **Avoid using 'video' in negative prompts**
  - Context: Using the word 'video' in negative prompts might have adverse effects
  - *From: TK_999*

- **Set Points To Sample = Sampler Steps when using spline editor**
  - Context: When using KJ nodes spline editor for CFG scheduling
  - *From: TK_999*

- **Use CFG scheduling for speed boost**
  - Context: At certain point in generation when image/motion is formed, less need for negative prompt, so set cfg=1 for speed
  - *From: TK_999*

- **Always keep backups**
  - Context: Important for protecting models and data from git accidents
  - *From: yi*

- **Don't lower CFG too much**
  - Context: Kept getting bad results when lowering CFG
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Prompting well helps significantly**
  - Context: Good prompting makes a notable difference in output quality
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Use detailed, descriptive prompts**
  - Context: Claude-generated detailed prompts work well for consistent results
  - *From: ingi // SYSTMS*

- **Exclude feedforward layers from fp8_fast**
  - Context: Doesn't ruin quality but also barely gives speed increase
  - *From: Kijai*

- **Use DPM++2M Beta scheduler**
  - Context: Avoid UniPC + DDIM uniform combination as it produces messed up results
  - *From: seitanism*

- **Use CRF or noise augment for static results**
  - Context: When getting low motion in I2V generations, try these parameters on same seed
  - *From: ▲*

- **Use fp32 text encoder for better prompt adherence**
  - Context: May improve prompt following but uses more VRAM
  - *From: seitanism*

- **Force fp16 kernel for I2V with SageAttention**
  - Context: When using SageAttention with I2V to avoid black images
  - *From: Miku*

- **Use cfg_end at 0.8 for better I2V results**
  - Context: When using GGUF Q8 model
  - *From: JmySff*

- **Stick with 81 frames for best results**
  - Context: Model works best at this length
  - *From: Kijai*

- **Use 480p resolution for optimal performance**
  - Context: 720p less stable due to limited training, 1.3B model capable but not recommended
  - *From: Bleedy*

- **More realistic images need more denoising steps**
  - Context: Art style affects required steps, realistic content needs more steps
  - *From: Draken*

- **Try different seeds when I2V prompt doesn't match image**
  - Context: Model sometimes ignores image when prompt doesn't match
  - *From: seitanism*

- **Never go under 1.0 CFG**
  - Context: When using CFG scheduling
  - *From: Kijai*

- **No more than 200 tokens is good compromise for prompts**
  - Context: English prompts, less after Chinese translation
  - *From: JmySff*

- **Use video frame interpolation to get to 30fps for much better realism**
  - Context: Post-processing Wan video outputs
  - *From: Shawneau 🍁 [CA]*

- **Try swap as least blocks as you can**
  - Context: When working with limited VRAM
  - *From: Draken*

- **If using 480p resolution, use the 480p model as it's tuned for that and much faster**
  - Context: Resolution and model selection
  - *From: seitanism*

- **Use Qwen models for prompt expansion**
  - Context: Wan was designed to work with Qwen2.5-VL-7B-Instruct for prompt extension, being from Alibaba
  - *From: orabazes*

- **Try close-up shots for better subject focus**
  - Context: When trying to make subject the main focus of video
  - *From: Cubey*

- **Generate at 480p then upscale with VFI nodes**
  - Context: Fast workflow that produces better end results than generating at higher resolution
  - *From: Shawneau 🍁 [CA]*

- **Portrait/close-up shots need fewer steps (10-15), half-body/full-body need more (20-30)**
  - Context: I2V generation step recommendations
  - *From: slmonker*

- **Don't go above 40-50 steps**
  - Context: Maximum recommended steps for Wan
  - *From: Kijai*

- **More steps usually best answer for motion blur, can try stronger schedulers or increasing shift**
  - Context: Removing motion blur from generations
  - *From: Kijai*

- **Keep Hunyuan denoise at 0.3 or below for V2V refining**
  - Context: Using Hunyuan as refiner for Wan outputs
  - *From: David Snow*

- **Use fp16 base_precision for better consistency, updated weights give better results without moiré noise**
  - Context: Native ComfyUI implementation improvements
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Use FP16 weights instead of BF16 for better quality**
  - Context: Especially important for fast motion scenes and anatomy accuracy
  - *From: Kytra*

- **Try Chinese prompts for better motion generation**
  - Context: Training data includes Chinese prompts, may produce more dynamic results
  - *From: Kytra*

- **Use dpmpp_2m sampler to avoid soft/denoised look**
  - Context: UniPC sampler was causing overly soft appearance
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Combine emojis with multiple languages for creative prompting**
  - Context: Embedding space allows mixing languages and emojis for unique steering
  - *From: fredbliss*

- **Use 1.25x latent upscale between KSamplers for artifact cleanup**
  - Context: Fast alternative to using different model for second pass on 1.3B
  - *From: Kytra*

- **Use multipass rendering for better results**
  - Context: Helps significantly with quality
  - *From: David Snow*

- **Use PatchSageAttention node over --use-sage-attention**
  - Context: Gives you more control
  - *From: Doctor Shotgun*

- **Use 'clean' inputs for Wan**
  - Context: Contrary to LTX, Wan likes clean inputs
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Higher steps improve quality**
  - Context: Steps should help with grid artifacts and overall quality
  - *From: Kijai*

- **Q6-K is good balance for 3090 users**
  - Context: Q6-K is go-to quant for most things, Q8 may OOM on 3090
  - *From: Benjaminimal*


## News & Updates

- **Model name changed from WanX to Wan**
  - Likely due to international feedback on the original name
  - *From: NebSH*

- **Wan 2.1 I2V 14B 720P model released**
  - Available on HuggingFace, 66GB fp32 / 16.5GB fp8
  - *From: seitanism*

- **Release confirmed for Beijing time night**
  - Direct communication from Wan team confirmed release timing
  - *From: guahunyo*

- **1.3B model intended as 'SD1.5 of video field'**
  - Internal model used for various experiments, meant to be widely adoptable base model
  - *From: guahunyo*

- **Wan2.1 models officially released**
  - Both 1.3B T2V and 14B I2V models available on HuggingFace
  - *From: multiple users*

- **Model name changed from WanX to Wan**
  - Alibaba changed the model name, likely for branding reasons
  - *From: yi*

- **Code expected to be released at 23:00 UTC+8**
  - Official announcement indicates code release timing
  - *From: Fannovel16*

- **Wan 2.1 code officially released**
  - GitHub repository is now public with full implementation
  - *From: Fannovel16*

- **Official training script available**
  - LoRA training is supported with official training scripts already provided
  - *From: Fannovel16*

- **14B T2V example script has wrong slice count**
  - Shows 7 slices but repo only has 6, will be corrected
  - *From: Masanlong*

- **Kijai released ComfyUI wrapper for Wan**
  - ComfyUI-WanVideoWrapper available on GitHub
  - *From: Kijai*

- **Wan 2.1 open source broadcast available**
  - Available on Alibaba_Wan Twitter/X
  - *From: ramonguthrie*

- **1.3B T2V model released**
  - Kijai released 1.3B T2V model on HuggingFace
  - *From: Kijai*

- **DMP++ SDE scheduler added**
  - Added dmp++_sde scheduler option
  - *From: Kijai*

- **I2V bug fixed**
  - I2V was broken with T2V update but now fixed
  - *From: Kijai*

- **720P I2V model released**
  - 14B 720P I2V model available in fp8 format
  - *From: Kijai*

- **fp32 VAE uploaded**
  - Original fp32 VAE now available for better quality
  - *From: Kijai*

- **14B T2V model released**
  - 14B T2V model in fp8 format now available
  - *From: Kijai*

- **Native ComfyUI implementation available**
  - Official ComfyUI support with repackaged models and workflows
  - *From: comfy*

- **CFG schedule support added**
  - Added CFG scheduling functionality to potentially speed up generation
  - *From: Kijai*

- **ComfyUI added native SaveWEBM node**
  - Frontend not implemented yet but functional for saving webm files without custom nodes
  - *From: comfy*

- **ComfyUI Desktop compatibility fixed**
  - Austin Mroz pushed update to fix Wan format information for desktop version
  - *From: Austin Mroz*

- **LoRA training available for Wan**
  - diffusion-pipe repo supports Wan LoRA training, works with both 1.3B T2V and drops into ComfyUI
  - *From: pro.evolution*

- **Native ComfyUI implementation released**
  - Comfy released native WanImageToVideo node, uses different text encoder format
  - *From: comfy*

- **City96 working on GGUF quantization**
  - GGUF versions in development for better memory efficiency
  - *From: Kijai*

- **Native ComfyUI nodes added for Wan**
  - Official ComfyUI support implemented alongside Kijai's wrapper
  - *From: B1naryV1k1ng*

- **City added GGUF models for Wan**
  - Quantized versions now available
  - *From: B1naryV1k1ng*

- **First Wan LoRAs created and shared**
  - Community members successfully trained and shared character and style LoRAs
  - *From: Kytra*

- **HunyuanVideo showing official I2V examples**
  - Posted on Twitter, looks really good
  - *From: samurzl*

- **HunyuanVideo keyframe control LoRA released**
  - I2V with end frame support available on HuggingFace
  - *From: yi*

- **TeaCache support commented out in wrapper**
  - Would need model-specific coefficient values to work
  - *From: Kijai*

- **GGUF torch.compile support added**
  - Bit faster but not full 30% speedup
  - *From: Kijai*

- **Native ComfyUI support added for Wan**
  - ComfyUI now has native support for Wan models
  - *From: QANICS🕐*

- **Performance improvements for fp8 models**
  - Great news for GGUF users - can go back to GGUFs since Wave and TeaCache provide speed boost with fp8 models
  - *From: ramonguthrie*

- **1.3B I2V not on roadmap**
  - Wan2.1 Image-to-Video roadmap shows 14B model integration but 1.3B I2V is not listed
  - *From: Mngbg*

- **ComfyUI fixed FP8 native implementation**
  - Commit 0270a0b41cef69726694b189f37942a04d762c8a fixes fp8 issues by upcasting specific operations
  - *From: comfy*

- **Kijai added noise augment and other features**
  - Added noise augmentation and other functionality to the wrapper
  - *From: Kijai*

- **Kijai added LoRA block selection support**
  - Added block selection functionality to WAN LoRA node
  - *From: Kijai*

- **Long prompt support fixed**
  - Issues with long prompts have been resolved in recent update
  - *From: comfy*

- **Kijai working on SpargeAttn tuning for speed improvements**
  - 6 minutes per step on 4090 for tuning, will create shareable model files for faster inference
  - *From: Kijai*

- **ComfyUI switched to Flux RoPE implementation**
  - Changed from original to flux implementation for better compatibility
  - *From: comfy*

- **RifleX node added for native Wan**
  - New patcher to help with videos longer than 81 frames, prevents looping
  - *From: Kijai*

- **New GGUF models available for I2V**
  - Q8 and other quantizations now available for I2V 480p model
  - *From: yi*

- **Bitsandbytes 12.8 CUDA released**
  - Version 0.45.3 with CUDA 12.8 builds available via pip install -U bitsandbytes
  - *From: AJO*

- **720p Q8 I2V GGUF model coming tomorrow from city96**
  - GGUF quantized version of 720p I2V model expected
  - *From: seitanism*

- **Comfy released fp16 weights converted from full fp32**
  - Available at Comfy-Org/Wan_2.1_ComfyUI_repackaged, gives very close results to full fp32
  - *From: comfy*

- **Enhance video node added to wrapper**
  - New feature for improving video quality, runs every block on every step
  - *From: Kijai*

- **City96 released Wan2.1-I2V-14B-720P-gguf model**
  - GGUF quantized version now available for lower VRAM usage
  - *From: AJO*

- **ComfyUI --fast 2 now supports fp16 accumulation with fp8 weights**
  - Requires latest PyTorch nightly for fp16 accumulation with fp8 weights
  - *From: comfy*

- **City96 uploaded 720p GGUF models**
  - Available at huggingface.co/city96/Wan2.1-I2V-14B-720P-gguf
  - *From: seitanism*

- **ComfyUI examples updated with shift node**
  - Updated examples available at comfyanonymous.github.io/ComfyUI_examples/wan/ including proper shift configuration
  - *From: comfy*

- **FP32 weights available for 1.3B model**
  - Single file fp32 weights at huggingface.co/Wan-AI/Wan2.1-T2V-1.3B/blob/main/diffusion_pytorch_model.safetensors
  - *From: Kijai*

- **Updated FP16 models available**
  - New FP16 1.3B models released that eliminate noise issues
  - *From: ˗ˏˋ⚡ˎˊ-*

- **FloweEdit compatibility confirmed**
  - Existing HunyuanLoom FloweEdit implementation works out of the box with Wan
  - *From: Kijai*

- **Zuko creating new FlowEdit fork**
  - Making I2V-specific implementation since logtd is stepping back from ComfyUI development
  - *From: Zuko*

- **PyTorch nightly dropping CUDA 124 support**
  - According to official repo code
  - *From: Doctor Shotgun*

- **ModelSamplingSD3 node added recently to ComfyUI workflow**
  - Should always be used for I2V
  - *From: Miku*


## Workflows & Use Cases

- **Basic T2V generation with custom parameters**
  - Use case: python generate.py --task t2v-1.3B --size 832*480 --ckpt_dir ./Wan2.1-T2V-1.3B --sample_shift 8 --sample_guide_scale 6 --prompt 'your prompt'
  - *From: Parker*

- **High resolution generation with offloading**
  - Use case: Use --size 1280*720 --offload_model True --t5_cpu --sample_shift 9 --sample_guide_scale 6 --sample_steps 20 for 720p
  - *From: Alisson Pereira*

- **Download models using huggingface-cli**
  - Use case: huggingface-cli download <model_name> --local-dir <output_folder>
  - *From: Alisson Pereira*

- **Two-pass upscaling with Wan 1.3B**
  - Use case: Generate at 480p then upscale to 720p using vid2vid with low denoise
  - *From: CDS*

- **RIFE interpolation for 24fps output**
  - Use case: Converting native 16fps output to smoother 24fps
  - *From: JohnDopamine*

- **T2V workflow available**
  - Use case: Text to video generation
  - *From: slmonker(5090D 32GB)*

- **10 steps for testing, 50 steps for final**
  - Use case: Efficient workflow to find good seeds quickly then render high quality
  - *From: seitanism*

- **I2V for animation work**
  - Use case: Best I2V model for animation according to users
  - *From: DevouredBeef*

- **Video2Video processing**
  - Use case: 1.3B model works well for vid2vid applications
  - *From: Kijai*

- **I2V extension chaining**
  - Use case: Creating longer videos by taking last frame and feeding to I2V repeatedly
  - *From: ezMan*

- **Overnight batch generation**
  - Use case: Save latents instead of videos to prevent OOM during VAE decode ruining entire batch
  - *From: Juampab12*

- **Seed hunting with step progression**
  - Use case: Generate multiple seeds at 10 steps, then refine best ones at 50 steps
  - *From: seitanism*

- **480p generation + upscaling**
  - Use case: Faster generation with quality upscaling instead of native 720p
  - *From: Juampab12*

- **LoRA training with diffusion-pipe repo**
  - Use case: Training character and style LoRAs for Wan models
  - *From: Kytra*

- **Native ComfyUI workflow with LoraLoaderModelOnly**
  - Use case: Testing LoRAs with native nodes
  - *From: Kytra*

- **Latent upscaling from 480x320 with 1.5x scaling**
  - Use case: Improving resolution of generated videos
  - *From: ▲*

- **Video2video using denoise**
  - Use case: Converting existing videos with Wan models
  - *From: Kijai*

- **Multi-resolution training**
  - Use case: LoRA training with 384/512/768/1024 square resolutions
  - *From: mamad8*

- **Multi-step upscaling using 1.3B**
  - Use case: Generate 480p on 1.3B, then upscale to 1080p in 2 upscale steps
  - *From: B1naryV1k1ng*

- **I2V2V pipeline**
  - Use case: Use Wan I2V then Hunyuan V2V as refiner
  - *From: Colin*

- **T2V with 1.3B model for fast iteration**
  - Use case: Quick testing and experimentation - very fast generation times
  - *From: B1naryV1k1ng*

- **Generate at low steps then refine good ones**
  - Use case: Efficient workflow since motion stays consistent when changing steps
  - *From: ˗ˏˋ⚡ˎˊ-*

- **16GB VRAM I2V workflow**
  - Use case: Kijai's wrapper with block swaps 12-16, 480x480 resolution, ~10 steps, torch compile + sage
  - *From: zelgo_*

- **Video extension using last frame**
  - Use case: Creating longer videos by chaining generations with final frame as input
  - *From: burgstall*

- **Native nodes with automatic offloading**
  - Use case: Running large resolutions on limited VRAM without manual block swapping
  - *From: comfy*

- **Using spline editor for CFG scheduling**
  - Use case: Implementing CFG drop technique in wrapper
  - *From: Kijai*

- **Block swapping for memory management**
  - Use case: Running larger models on limited VRAM by moving blocks between GPU/CPU
  - *From: Kijai*

- **Vid2vid using VAE encode with denoise <1**
  - Use case: Generate at 480p with low steps, then improve with 720p high steps for temporal consistency
  - *From: hablaba*

- **Chinese translation in VLM workflow**
  - Use case: Translate English prompts to Chinese for better results
  - *From: JmySff*

- **CFG scheduling from high to low values**
  - Use case: Start with CFG 6 for first 15 steps, then CFG 1 for last 15 steps - twice as fast but may degrade quality
  - *From: seitanism*

- **Multi-stage video extension with MMAudio**
  - Use case: Generate first I2V, then queue extensions, combine segments, add audio
  - *From: Organoids*

- **Discord bot integration with 1.3B model**
  - Use case: Automated video generation through Discord interface
  - *From: AJO*

- **Wan 1.3B + Hunyuan refiner**
  - Use case: Cleaning up artifacts from 1.3B model while maintaining speed advantage over 14B
  - *From: David Snow*

- **Vid2vid using any model including Wan**
  - Use case: Video-to-video generation, works nicely with Wan models
  - *From: Kijai*

- **Context schedule for extended videos**
  - Use case: Generating very long videos (165-329 frames) though transitions need work
  - *From: Kijai*

- **Wan + HunyuanVideo two-pass refinement**
  - Use case: Generate with Wan 1.3B then refine with HunyuanVideo V2V at low denoise to clean artifacts
  - *From: David Snow*

- **1.25x latent upscale two-pass with same model**
  - Use case: Clean up 1.3B artifacts using latent upscale and 45% denoise second pass
  - *From: Kytra*

- **FloweEdit video editing with Wan**
  - Use case: Use existing HunyuanLoom nodes for video-to-video editing with flow guidance
  - *From: Kijai*

- **Multi-language emoji prompting**
  - Use case: Combine Chinese, English, Hebrew, and emojis for creative prompt steering
  - *From: fredbliss*

- **Two-pass Wan 1.3B + Hunyuan refinement**
  - Use case: Fast generation with quality refinement
  - *From: David Snow*

- **Linear blended windowing for long videos**
  - Use case: 161 frames with 24 frame windows and 12 frame stride
  - *From: Benjaminimal*


## Recommended Settings

- **Frame rate**: 16fps
  - Base frame rate for all model outputs
  - *From: JohnDopamine*

- **VRAM requirement**: 8.19 GB for 1.3B model
  - Official specification for consumer GPU compatibility
  - *From: thaakeno*

- **Generation time**: 4 minutes for 5-second 480P video
  - On RTX 4090 without optimization
  - *From: thaakeno*

- **shift parameter for 480p**: 3.0
  - Recommended in documentation for 480p video generation
  - *From: 片ヨ亡亡丹片*

- **optimal 1.3B settings**: shift 9, steps 20
  - Good quality/speed balance
  - *From: Fannovel16*

- **sample_guide_scale**: 6
  - Standard guidance scale used in examples
  - *From: Parker*

- **default fps**: 16
  - Standard frame rate for generated videos
  - *From: Parker*

- **sample_shift**: 8
  - Default recommended setting
  - *From: AJO*

- **sample_guide_scale**: 6
  - Default recommended setting
  - *From: AJO*

- **sample_steps**: 50
  - Default, though 10 steps can work for some cases
  - *From: AJO*

- **torch_dtype**: torch.float8_e4m3fn
  - For FP8 quantization in DiffSynth
  - *From: Raphaël*

- **minimum frames**: 81
  - Model requirement for I2V
  - *From: Kijai*

- **Steps**: 50 steps
  - Significantly better quality than 30 steps, worth the extra time
  - *From: Juampab12*

- **Flow shift**: 4-5
  - Better details than 6-10, but 3 causes coherence issues
  - *From: Juampab12*

- **Resolution for speed**: 480x480
  - Faster than 512x512 default
  - *From: Juampab12*

- **Block swap for 5090**: 5 blocks
  - Can afford lower block swap with more VRAM
  - *From: Juampab12*

- **Negative prompt**: 色调艳丽，过曝，静态，细节模糊不清，字幕，风格，作品，画作，画面，静止，整体发灰，最差质量，低质量，JPEG压缩残留，丑陋的，残缺的，多余的手指，画得不好的手部，画得不好的脸部，畸形的，毁容的，形态畸形的肢体，手指融合，静止不动的画面，杂乱的背景，三条腿，背景人很多，倒着走
  - Chinese negative prompt works better
  - *From: Juampab12*

- **Steps**: 50 steps recommended
  - Significant quality improvement over 30 steps, 70 steps doesn't improve much over 50
  - *From: seitanism*

- **Steps for testing**: 10 steps
  - Good for finding the right seed quickly
  - *From: seitanism*

- **RifleX**: 0
  - Doesn't work with Wan models, causes tiling artifacts
  - *From: Kijai*

- **Resolution for 1.3B T2V**: 720x480
  - Working well at this resolution
  - *From: slmonker(5090D 32GB)*

- **FPS**: 16fps over 24fps
  - 24fps seems a bit too fast
  - *From: slmonker(5090D 32GB)*

- **CFG 1.0**: 1.0 for speed
  - Skips uncond computation, can halve generation time
  - *From: Kijai*

- **CFG and Flow shift for 14B I2V**: CFG 6, Flow 5 for 50 steps
  - Good balance found through testing
  - *From: Juampab12*

- **Block swap for 16GB VRAM**: Block swap 16
  - Allows 480x480 generation on 16GB VRAM
  - *From: zelgo_*

- **Steps and model for quality**: 50 steps better than 30 steps
  - Improved quality worth the extra time
  - *From: Juampab12*

- **Supported resolutions for 720p model**: 832*480, 1280*720, 1024*1024, 720*1280, 480*832
  - Official supported resolutions
  - *From: Benjimon*

- **Steps**: 40 steps recommended for I2V
  - Official recommendation from Wan repository
  - *From: yi*

- **Frames**: 81 frames maximum
  - Best quality, hardcoded limit in original code
  - *From: Kijai*

- **Scheduler**: dpm++_sde
  - Best quality but slowest
  - *From: Juampab12*

- **Resolution**: 480x848 with 73 frames
  - Optimal performance at 3 seconds per frame
  - *From: huangkun1985*

- **Block swap for fp8**: 39 blocks instead of 35
  - Needed for proper memory management with fp8 quantization
  - *From: Pedro (@LatentSpacer)*

- **Learning rate for LoRA training**: bfloat16 precision
  - Successful training results
  - *From: Kytra*

- **Training resolution**: 512 max resolution
  - Nearly caps 24GB VRAM, could do 1024 with bigger GPU
  - *From: Kytra*

- **Video training frames**: 16 frames for 420 bucket
  - Fits in 23GB VRAM
  - *From: Cubey*

- **Steps for 1.3B model**: 15 steps
  - Good balance of speed vs quality
  - *From: Pedro (@LatentSpacer)*

- **Precision settings**: fp32 for text encoder, img encoder, VAE; bf16 for transformer
  - Best quality without excessive compute
  - *From: Pedro (@LatentSpacer)*

- **Sampler choice**: uni-pc
  - Used in official code
  - *From: comfy*

- **Video2video denoise**: 0.5
  - Half the sigmas for proper v2v
  - *From: Kijai*

- **Minimum frames**: 5 frames minimum, but updated to allow 1
  - Technical limitation, but now adjustable
  - *From: Kijai*

- **CFG scheduling**: Start 0.0 end 0.6, max 6
  - Good balance for quality and speed
  - *From: B1naryV1k1ng*

- **Steps**: 30
  - Standard setting used in testing
  - *From: B1naryV1k1ng*

- **Resolution**: 856x480 for 16:9
  - Good 16:9 aspect ratio
  - *From: Janosch Simon*

- **Resolution**: 848x480
  - Works well for most generations
  - *From: ingi // SYSTMS*

- **Block swap**: 20 with compile for 1280x544
  - Enables higher resolution on limited VRAM
  - *From: David Snow*

- **Block swap**: 40 for 1280x720x81f
  - Required for high resolution I2V
  - *From: Juampab12*

- **Noise augmentation**: 0.05
  - Produces clean results with good texture detail
  - *From: Zuko*

- **Steps for quality/speed balance**: 20-30 steps
  - 30 steps recommended, not much difference between 30-40 steps
  - *From: seitanism*

- **CFG**: Don't go too low
  - Lower CFG produces bad results
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Block swaps for 16GB**: 12-16 blocks
  - Works reliably on 16GB VRAM for I2V
  - *From: zelgo_*

- **Resolution for 3090 optimal**: 848x480x81 frames
  - Good balance of quality and speed on 24GB VRAM
  - *From: Organoids*

- **4090 high resolution**: 1280x720x81f with offloading
  - Maximum practical resolution with automatic memory management
  - *From: Doctor Shotgun*

- **SageAttention kernel for I2V**: fp16_cuda
  - Avoids black images from fp8 precision overflow
  - *From: Miku*

- **Block swap value for wrapper**: Lower than 20
  - Earlier offloading to prevent VRAM issues
  - *From: PookieNumnums*

- **Optimal 16:9 resolution**: 480x848x73 frames
  - Optimal size and performance according to testing
  - *From: Organoids*

- **RifleX freq index**: 4
  - Works for Hunyuan, results in more coherent actions
  - *From: Kijai*

- **CFG schedule**: Linear ramp down or drop to 0.8
  - Better quality results, used in stable video diffusion
  - *From: Kijai*

- **Inference steps vs frames**: Points to sample should be number of steps, not frames
  - Proper spline editor configuration
  - *From: seitanism*

- **Resolution recommendation**: 480p
  - Optimal performance, 720p less stable due to limited training
  - *From: Bleedy*

- **CFG scheduling**: 6.0 to 1.0 over 30 steps
  - Last 15 steps twice as fast, though may degrade quality
  - *From: seitanism*

- **Frame count default**: 1 for T2I, 81 for other tasks
  - Default values from Wan codebase
  - *From: Captain of the Dishwasher*

- **Prompt length for Chinese**: 80-100 characters
  - Suggested in Wan's prompt upscaling code
  - *From: TK_999*

- **Performance mode**: --fast flag with latest pytorch nightly
  - Enables fp16 compute for better performance
  - *From: comfy*

- **SageAttention kernel selection**: sageattn_qk_int8_pv_fp16_triton for I2V, sageattn_qk_int8_pv_fp8_cuda for T2V on Ada GPUs
  - Prevents black image output in I2V
  - *From: Doctor Shotgun*

- **Quantization for speed**: fp8_e4m3fn with SageAttention
  - Fastest option when VRAM limited
  - *From: Kijai*

- **Best quality/speed balance**: fp16 + fp16 accumulate if VRAM allows, or fp8 weights with fp16 compute
  - Optimal quality without significant speed loss
  - *From: comfy*

- **BF16 for 4090**: bf16 reduces step time to 18s/step on 720x480 73 frames
  - Further speed optimization
  - *From: slmonker(5090D 32GB)*

- **Steps for I2V**: 10-15 for portraits, 20-30 for full body
  - Depends on image complexity and shot type
  - *From: slmonker*

- **Hunyuan denoise for refining**: 0.3 or below
  - Higher levels don't work well for V2V
  - *From: David Snow*

- **Block swapping**: 25, 35, or 40
  - For 16GB VRAM to avoid OOM
  - *From: Kijai*

- **Maximum steps**: 40-50
  - Diminishing returns beyond this range
  - *From: Kijai*

- **FP16 compute dtype**: enabled
  - Significantly faster inference on supported GPUs
  - *From: Kijai*

- **FP16 accumulation**: enabled with pytorch 2.7.0 nightly
  - Best performance with FP16 weights
  - *From: Kijai*

- **Second pass denoise**: 45% for latent upscale method
  - Cleans artifacts without over-processing
  - *From: Kytra*

- **V2V denoise for HunyuanVideo refinement**: low denoise
  - Removes Wan artifacts while preserving motion
  - *From: David Snow*

- **Frame count**: 832x480x65 frames for 4060 8GB
  - Fits in VRAM with 6-8 min generation times
  - *From: Googol*

- **Resolution scaling**: 1920x1080 to 656x368
  - Reduces VRAM usage for longer sequences
  - *From: 3Dmindscaper2000*

- **Shift value**: 3.0 for i2v 480p, 5.0 for everything else
  - Official repo defaults
  - *From: Doctor Shotgun*

- **Steps**: 50 for i2v, 40 for t2v
  - Official repo defaults
  - *From: Doctor Shotgun*

- **Sage attention**: 8+8 for compatibility, 8+16 for speed
  - 8+16 may cause issues with some setups
  - *From: Doctor Shotgun*

- **Base precision**: fp16 over bf16
  - fp16 seems superior though difference is small
  - *From: Benjaminimal*


## Concepts Explained

- **3D VAE benefits**: 3D VAE helps solve issues like hands, long necks, weird buttons that are common in image models
  - *From: Draken, Pedro (@LatentSpacer)*

- **Wanxiang**: Chinese term meaning 'all phenomena' or 'the universe', can also mean everything is renewed or complex diversity
  - *From: wange1002*

- **shift parameter**: Noise schedule shift parameter that affects temporal dynamics, needs adjustment based on resolution
  - *From: 片ヨ亡亡丹片*

- **NSFW Score**: Training data classification system, not necessarily a filter - used to separate training data types
  - *From: DawnII*

- **MoE architecture**: Wan 2.2 will use Mixture of Experts with High/Low noise expert split in 5B hybrid model
  - *From: context*

- **Flow shift**: Parameter that affects detail quality and coherence - lower values give better details but can cause coherence issues if too low
  - *From: Juampab12*

- **Block swap**: More block swap = less VRAM usage but slower speed
  - *From: Juampab12*

- **Flow shift**: Parameter affecting motion characteristics - different values (2 vs 5 vs 8) produce different motion qualities
  - *From: ezMan*

- **CFG scheduling**: Using variable CFG values during generation (e.g., high CFG early, low CFG later) for better results
  - *From: JmySff*

- **Differential diffusion**: Training-free technique that works with many models for better control
  - *From: spacepxl*

- **I2V dataset creation**: Same as T2V dataset, only difference is how you condition the model (freeze frame 0)
  - *From: spacepxl*

- **Block swapping**: Uses system RAM to manage VRAM limitations during inference
  - *From: Kijai*

- **MoE architecture**: Wan 2.2 uses Mixture of Experts with High/Low noise expert split
  - *From: context*

- **First-Frame-Last-Frame morphing**: Fun InP feature for video extension and morphing
  - *From: context*

- **Subject+Scene+Action prompt structure**: Official guidance - Subject (humans/animals/characters), Scene (environment/setting), Action (movement/camera motion)
  - *From: slmonker(5090D 32GB)*

- **VAE caching**: VAE stores data that isn't cleared properly, wasting VRAM during inference
  - *From: Kijai*

- **TeaCache**: Acceleration method that needs model-specific coefficient values to work
  - *From: Kijai*

- **Spline editor CFG scheduling**: Create a line from top to bottom in middle, connects float output to CFG input for dynamic CFG control
  - *From: seitanism*

- **Points To Sample**: Parameter in spline editor that should equal the number of sampler steps
  - *From: TK_999*

- **Low frequency noise information**: Determines motion and composition in diffusion models - why motion stays consistent when changing steps but not seed
  - *From: spacepxl*

- **Ancestral vs deterministic samplers**: Ancestral samplers (like euler_a) change composition with step changes, deterministic samplers (like euler, DPM) don't
  - *From: spacepxl*

- **clip_vision_h**: Refers to XLM-Roberta-Large-Vit-L-14 model from HuggingFace
  - *From: ˗ˏˋ⚡ˎˊ-*

- **SpargeAttn tuning**: Training-free attention optimization that calculates parameters for speedup, saves tiny files with tuned params
  - *From: Kijai*

- **Auto offloading**: Automatic memory management that moves model parts between VRAM and RAM based on usage
  - *From: comfy*

- **fp8 precision overflow**: Mathematical overflow in fp8 format causing NaN values and black image outputs
  - *From: Doctor Shotgun*

- **Block swapping**: Moving transformer blocks between GPU and CPU memory during inference to manage VRAM usage
  - *From: Kijai*

- **fp8 casting precision loss**: Loading e4 weight and casting to e5 loses both exponent and mantissa, should use matching precision
  - *From: Kijai*

- **RifleX**: Technique to reduce attention to high frequency movements, allowing more attention to low frequency movements via softmax
  - *From: deleted_user_2ca1923442ba*

- **Enhance video**: Uses fancy math to enhance attention results, runs every block on every step
  - *From: Kijai*

- **Force offload**: Setting that controls memory management for the sampler
  - *From: Shawneau 🍁 [CA]*

- **Feta args**: Parameters for the enhance video functionality, optimal values still being determined
  - *From: Kijai*

- **UmT5 (Unified multilingual T5)**: Multilingual text encoder that shares embedding space across 100+ languages, enabling cross-lingual transfer
  - *From: fredbliss*

- **SpargeAttention**: Attention optimization requiring model-specific tuning, taking ~5 hours per iteration with minimal speed gains
  - *From: Kijai*

- **fp16 accumulation**: Higher precision accumulation for matrix operations while using lower precision weights
  - *From: comfy*

- **Shift**: Adjusts the sigma schedule - higher values affect the denoising curve, can't be negative with video models
  - *From: Kijai*

- **Context schedule**: Method for generating extended video sequences beyond normal frame limits
  - *From: Kijai*

- **Block swapping**: Memory management technique in wrapper to handle larger models on limited VRAM
  - *From: Kijai*

- **FP16 accumulation**: PyTorch feature for doing all FP16 GEMM accumulation in FP16 for increased performance on Volta+ GPUs, at cost of numerical precision
  - *From: Kijai*

- **FETA in FlowEdit**: Flow editing strength parameter, typically set to 0.2 for Wan vs 2.0 for HunyuanVideo
  - *From: Zuko*

- **Embedding space steering**: Using different languages and emojis to steer generation through shared embedding space of UMT5
  - *From: fredbliss*

- **fp16 accumulation**: When doing matmul on fp16 tensors, the sum variable (accumulation) is computed in fp32 for stability, then recast to fp16
  - *From: Benjaminimal*

- **Grid/tile artifacts**: Pattern artifacts that appear as stipple-like patterns, often related to quantization quality
  - *From: N0NSens*


## Resources & Links

- **Wan 2.1 I2V 14B 720P** (model)
  - https://huggingface.co/Wan-AI/Wan2.1-I2V-14B-720P
  - *From: seitanism*

- **Wan 2.1 HuggingFace Space** (demo)
  - https://huggingface.co/spaces/Wan-AI/Wan2.1
  - *From: various*

- **Alibaba Wan Twitter** (social)
  - https://x.com/Alibaba_Wan
  - *From: yi*

- **Wan API documentation** (documentation)
  - https://help-aliyun-com.translate.goog/zh/model-studio/developer-reference/image-to-video-api-reference
  - *From: Pedro (@LatentSpacer)*

- **Timestamp converter tool** (tool)
  - https://sesh.fyi/timestamp/
  - *From: Fannovel16 🇻🇳*

- **Wan2.1-T2V-1.3B** (model)
  - https://huggingface.co/Wan-AI/Wan2.1-T2V-1.3B/
  - *From: Fannovel16*

- **Wan2.1-I2V-14B-720P** (model)
  - https://huggingface.co/Wan-AI/Wan2.1-I2V-14B-720P/tree/main
  - *From: seitanism*

- **DiffSynth-Studio pipeline code** (repo)
  - https://github.com/modelscope/DiffSynth-Studio/blob/af7d305f00c67e3fa16d9f902f77980170e1ef38/diffsynth/pipelines/wan_video.py#L22
  - *From: Fannovel16*

- **Wan2.1 official space** (tool)
  - https://huggingface.co/spaces/Wan-AI/Wan2.1
  - *From: wange1002*

- **Official Wan 2.1 Repository** (repo)
  - https://github.com/Wan-Video/Wan2.1
  - *From: Fannovel16*

- **DiffSynth-Studio implementation** (repo)
  - https://github.com/modelscope/DiffSynth-Studio/tree/main/examples/wanvideo
  - *From: Juampab12*

- **Precompiled Flash Attention wheels** (tool)
  - https://huggingface.co/Kijai/PrecompiledWheels/tree/main
  - *From: Alisson Pereira*

- **Live stream on X** (tool)
  - https://x.com/i/broadcasts/1lPJqMaokNeJb
  - *From: ResTrading*

- **ComfyUI-WanVideoWrapper** (repo)
  - https://github.com/kijai/ComfyUI-WanVideoWrapper
  - *From: Kijai*

- **DiffSynth-Studio Wan examples** (repo)
  - https://github.com/modelscope/DiffSynth-Studio/tree/main/examples/wanvideo
  - *From: ArtOfficial*

- **Wan2_1-I2V-14B-480P_fp8_e4m3fn.safetensors** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/blob/main/Wan2_1-I2V-14B-480P_fp8_e4m3fn.safetensors
  - *From: Kijai*

- **WSL disk expansion guide** (tool)
  - https://learn.microsoft.com/en-us/windows/wsl/disk-space#how-to-expand-the-size-of-your-wsl-2-virtual-hard-disk
  - *From: TK_999*

- **uv package manager** (tool)
  - https://docs.astral.sh/uv/
  - *From: ˗ˏˋ⚡ˎˊ-*

- **1.3B T2V model** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/blob/main/Wan2_1-T2V-1_3B_fp8_e4m3fn.safetensors
  - *From: Kijai*

- **Training scripts** (repo)
  - DiffSynth repo examples
  - *From: Kytra*

- **Prompt extend system prompts** (repo)
  - https://github.com/Wan-Video/Wan2.1/blob/main/wan/utils/prompt_extend.py
  - *From: TK_999*

- **Wan 720P I2V model** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/blob/main/Wan2_1-I2V-14B-720P_fp8_e4m3fn.safetensors
  - *From: Kijai*

- **Wan fp32 VAE** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/blob/main/Wan2_1_VAE_fp32.safetensors
  - *From: Kijai*

- **Wan 14B T2V model** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/blob/main/Wan2_1-T2V-14B_fp8_e4m3fn.safetensors
  - *From: Kijai*

- **ComfyUI native implementation** (repo)
  - https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/tree/main/split_files
  - *From: comfy*

- **ComfyUI WanVideo wrapper** (repo)
  - https://github.com/kijai/ComfyUI-WanVideoWrapper
  - *From: NebSH*

- **ComfyUI commit for native support** (repo)
  - https://github.com/comfyanonymous/ComfyUI/commit/63023011b97b85087896683b73eab5d1a6d95a05
  - *From: comfy*

- **FP32 UMT5-XXL encoder** (model)
  - https://huggingface.co/Nap/umt5-xxl-encoder-only-fp32-safetensors/tree/main
  - *From: Pedro (@LatentSpacer)*

- **FP32 visual encoder** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/blob/main/open-clip-xlm-roberta-large-vit-huge-14_visual_fp32.safetensors
  - *From: Kijai*

- **Triton for Windows** (tool)
  - https://github.com/woct0rdho/triton-windows
  - *From: JohnDopamine*

- **Wrapper workflows** (workflow)
  - https://github.com/kijai/ComfyUI-WanVideoWrapper/tree/main/example_workflows
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Kijai's WanVideoWrapper** (repo)
  - https://github.com/kijai/ComfyUI-WanVideoWrapper
  - *From: garbus*

- **diffusion-pipe LoRA training** (repo)
  - https://github.com/tdrussell/diffusion-pipe
  - *From: pro.evolution*

- **Test LoRA** (model)
  - https://huggingface.co/tdrussell/wan-1.3b-grayscale-lora-test
  - *From: pro.evolution*

- **Comfy repackaged models** (model)
  - https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/tree/main/split_files
  - *From: comfy*

- **City96 GGUF models** (model)
  - https://huggingface.co/city96/Wan2.1-T2V-14B-gguf
  - *From: 🦙rishappi*

- **ComfyOrg Wan repackaged models** (model)
  - https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/tree/main/split_files
  - *From: Kytra*

- **Grayscale LoRA test** (lora)
  - https://huggingface.co/tdrussell/wan-1.3b-grayscale-lora-test
  - *From: Screeb*

- **Character LoRA (Kylie Jenner)** (lora)
  - https://www.mediafire.com/file/0d46wdbmxklarp8/adapter_model.safetensors/file
  - *From: Kirara*

- **Diffusion-pipe repo** (training tool)
  - *From: Kytra*

- **ComfyUI Wan examples** (workflow)
  - https://comfyanonymous.github.io/ComfyUI_examples/wan/
  - *From: comfy*

- **HunyuanVideo keyframe control LoRA** (model)
  - https://huggingface.co/dashtoon/hunyuan-video-keyframe-control-lora
  - *From: yi*

- **TeaCache GitHub issue** (repo)
  - https://github.com/ali-vilab/TeaCache/issues/1
  - *From: Kijai*

- **ComfyUI Wan examples** (workflow)
  - https://comfyanonymous.github.io/ComfyUI_examples/wan/
  - *From: Mngbg*

- **Pre-CFG ComfyUI nodes** (repo)
  - https://github.com/Extraltodeus/pre_cfg_comfy_nodes_for_ComfyUI
  - *From: Raphaël*

- **Comfy-Org Wan text encoders** (model)
  - https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/tree/main/split_files/text_encoders
  - *From: ingi // SYSTMS*

- **Video comparison tool** (tool)
  - *From: mamad8*

- **GGUF T2V 14B model** (model)
  - https://huggingface.co/city96/Wan2.1-T2V-14B-gguf/tree/main
  - *From: seitanism*

- **ComfyUI Wan examples** (workflow)
  - https://comfyanonymous.github.io/ComfyUI_examples/wan/
  - *From: Miku*

- **XLM-Roberta-Large-Vit-L-14** (model)
  - https://huggingface.co/M-CLIP/XLM-Roberta-Large-Vit-L-14
  - *From: ˗ˏˋ⚡ˎˊ-*

- **AlekPet Custom Nodes** (repo)
  - https://github.com/AlekPet/ComfyUI_Custom_Nodes_AlekPet
  - *From: B1naryV1k1ng*

- **FP32 T5 text encoder** (model)
  - https://huggingface.co/Nap/umt5-xxl-encoder-only-fp32-safetensors/tree/main
  - *From: seitanism*

- **NF4 quantized 14B models** (model)
  - https://civitai.com/models/1299436/wan21-nf4-quantizations
  - *From: seitanism*

- **SpargeAttn repository** (repo)
  - https://github.com/thu-ml/SpargeAttn
  - *From: Kijai*

- **Wan 2.1 I2V GGUF models** (model)
  - https://huggingface.co/city96/Wan2.1-I2V-14B-480P-gguf
  - *From: yi*

- **Wan 2.1 T2V GGUF models** (model)
  - https://huggingface.co/city96/Wan2.1-T2V-14B-gguf
  - *From: yi*

- **ComfyUI Wan examples** (workflow)
  - https://comfyanonymous.github.io/ComfyUI_examples/wan/
  - *From: Draken*

- **Wan GGUF models** (model)
  - https://huggingface.co/calcuis/wan-gguf/tree/main
  - *From: ˗ˏˋ⚡ˎˊ-*

- **ComfyUI-WanVideoWrapper** (repo)
  - https://github.com/kijai/ComfyUI-WanVideoWrapper
  - *From: Draken*

- **Comfy-Org repackaged models** (model)
  - https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/tree/main/split_files
  - *From: B1naryV1k1ng*

- **city96 GGUF models** (model)
  - https://huggingface.co/city96/Wan2.1-I2V-14B-480P-gguf/tree/main
  - *From: burgstall*

- **Comfy fp16 repackaged models** (model)
  - https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged
  - *From: comfy*

- **Wan prompt extension code** (repo)
  - https://github.com/Wan-Video/Wan2.1/blob/main/wan/utils/prompt_extend.py
  - *From: TK_999*

- **720p bf16 I2V model** (model)
  - https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/blob/main/split_files/diffusion_models/wan2.1_i2v_720p_14B_bf16.safetensors
  - *From: Cubey*

- **Wan2.1-I2V-14B-720P-gguf** (model)
  - https://huggingface.co/city96/Wan2.1-I2V-14B-720P-gguf
  - *From: AJO*

- **xDiT project** (repo)
  - https://github.com/xdit-project/xDiT
  - *From: fredbliss*

- **Goku MovieGen benchmark viewer** (tool)
  - https://huggingface.co/spaces/benjamin-paine/goku-moviegen-bench-viewer
  - *From: Benjaminimal*

- **HunyuanVideo Penguin benchmark prompts** (dataset)
  - https://github.com/Tencent/HunyuanVideo/blob/main/assets/PenguinVideoBenchmark.csv
  - *From: fredbliss*

- **SpargeAttn research paper** (paper)
  - https://arxiv.org/abs/2502.20126
  - *From: yi*

- **720p GGUF models** (model)
  - https://huggingface.co/city96/Wan2.1-I2V-14B-720P-gguf/tree/main
  - *From: seitanism*

- **ComfyUI Wan examples** (workflow)
  - https://comfyanonymous.github.io/ComfyUI_examples/wan/
  - *From: comfy*

- **FP32 1.3B weights** (model)
  - https://huggingface.co/Wan-AI/Wan2.1-T2V-1.3B/blob/main/diffusion_pytorch_model.safetensors
  - *From: Kijai*

- **ComfyUI-GGUF node** (node)
  - https://github.com/city96/ComfyUI-GGUF
  - *From: Kijai*

- **Genmo prompts for inspiration** (resource)
  - https://www.genmo.ai/play
  - *From: David Snow*

- **Official ComfyUI Wan examples** (workflow)
  - https://comfyanonymous.github.io/ComfyUI_examples/wan/
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Comfy-Org Wan 2.1 repackaged models** (model)
  - https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/tree/main
  - *From: MilesCorban*

- **HunyuanLoom FlowEdit nodes** (repo)
  - https://github.com/logtd/ComfyUI-HunyuanLoom
  - *From: Kijai*

- **FP16 model weights** (model)
  - https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/tree/main/split_files/diffusion_models
  - *From: Juampab12*

- **Kagi emoji translator** (tool)
  - https://translate.kagi.com/?from=auto&to=emoji&text=
  - *From: fredbliss*

- **Extended windowing code for long videos** (repo)
  - https://github.com/painebenjamin/taproot/blob/main/src/taproot/tasks/generation/video/wan/model/pipeline.py
  - *From: Benjaminimal*

- **PyTorch nightly CUDA 128 builds** (tool)
  - https://download.pytorch.org/whl/nightly/cu128
  - *From: Benjaminimal*

- **Two-pass workflow with Hunyuan refinement** (workflow)
  - *From: David Snow*


## Known Limitations

- **I2V model not good for anime**
  - Lots of morphing issues with anime-style input images
  - *From: Miku*

- **Only 5 second generation length**
  - All samples and API limited to 5 seconds despite claims of longer videos
  - *From: wottso*

- **Heavy Asian bias in human generation**
  - Defaults to Asian people for any human generation without specific ethnicity prompts
  - *From: Pedro (@LatentSpacer)*

- **1.3B model is T2V only**
  - No I2V capability in the smaller model
  - *From: B1naryV1k1ng*

- **Large model sizes in fp32**
  - 14B model is around 66GB, needs quantization for most users
  - *From: seitanism*

- **No inference code initially**
  - Only weights released initially, code came later
  - *From: Kijai*

- **1.3B model is T2V only currently**
  - No I2V capability in the 1.3B variant, only text-to-video
  - *From: slmonker(5090D 32GB)*

- **14B model requires excessive VRAM**
  - Takes around 120GB VRAM and estimates 30 minutes for 50 steps
  - *From: samurzl*

- **Hunyuan image generation quality issues**
  - 1 frame videos are always pony style and bad quality compared to proper image models
  - *From: Juampab12*

- **Camera movement accuracy**
  - Sometimes pans in instead of out as prompted, but not bad overall
  - *From: DawnII*

- **Minimum 81 frames required for I2V**
  - Anything less than 81 frames with I2V errors out
  - *From: ArtOfficial*

- **No 1.3B I2V model available**
  - Only T2V model released for 1.3B variant
  - *From: seitanism*

- **Grid/speckle artifacts from VAE**
  - Strided convolutions and VGG LPIPS loss cause artifacts
  - *From: spacepxl*

- **FP8_fast quantization causes noise artifacts**
  - Especially with img_embed weights
  - *From: Kijai*

- **Hardcoded 81 frame minimum**
  - Cannot generate less than 81 frames due to hardcoded values in encode_image function
  - *From: ArtOfficial*

- **Poor quality above 81 frames**
  - 121 frames consistently produces nightmare fuel/static content
  - *From: Ro*

- **Celebrity censorship**
  - Model doesn't know celebrities, appears censored
  - *From: yi*

- **T2V not implemented in 1.3B initially**
  - Only I2V 14B available at first, T2V 1.3B came later
  - *From: Juampab12*

- **Poor prompt following**
  - Complex prompts not followed well, model interprets differently than intended
  - *From: Juampab12*

- **14B model is very slow**
  - 14B takes over 20 minutes compared to 1.3B taking 2 minutes
  - *From: B1naryV1k1ng*

- **720P I2V extremely slow on lower-end GPUs**
  - 1280x720x81 I2V took almost 1 hour to generate
  - *From: Juampab12*

- **4060Ti 16GB struggles with 14B**
  - 14B i2v model causes GPU overload, 260 seconds per inference step
  - *From: wange1002*

- **img2vid2vid not working well**
  - Video to video conversion not quite there yet
  - *From: Kijai*

- **1.3B model produces glitchy results at 30 steps**
  - 30 step generations on 1.3B T2V are very glitchy
  - *From: TK_999*

- **No 1.3B I2V model available**
  - Only T2V available for 1.3B variant
  - *From: mamad8*

- **Speed is very slow**
  - CFG is particularly slow, 1h per video for 720p I2V on some setups
  - *From: Kijai*

- **Can't achieve static camera easily**
  - I2V tends to add camera movement/zoom even when trying for static shots
  - *From: Juampab12*

- **Can't generate fisheye lens perspective**
  - T2V unable to produce fisheye lens footage
  - *From: Ghost*

- **Video extensions won't be fully seamless**
  - Without velocity/acceleration info from input frames, perfect seamless joining is mathematically impossible
  - *From: Screeb*

- **FP8 fast causes quality issues**
  - FP8 fast produces blocky artifacts, only good for composition testing
  - *From: Juampab12*

- **Frame count hardcoded to 81**
  - Model starts looping or degrading after 81 frames
  - *From: Kijai*

- **High VRAM usage for 720p**
  - 16GB GPU can only handle 49 frames at 512x768 with 14B I2V
  - *From: wange1002*

- **Cannot interchange model resolutions**
  - 720p model doesn't work well for 480p resolution and vice versa
  - *From: AJO*

- **LoRAs not compatible between model sizes**
  - 1.3B and 14B have different architectures, LoRAs won't transfer
  - *From: Fannovel16*

- **Native nodes require minimum 81 frames**
  - Won't work with frame counts below 81
  - *From: Kijai*

- **LoRAs don't transfer between 1.3B and 14B models**
  - Models have different architectures (30 vs 40 blocks, different inner dimensions)
  - *From: comfy*

- **14B model is very slow**
  - Takes 1200 seconds for 1280x720 15 steps
  - *From: Kirara*

- **No 1.3B I2V model available**
  - Only T2V model exists for 1.3B variant
  - *From: Kijai*

- **English text generation breaks down**
  - Good at single words but sentences become garbled, affects both 1.3B and 14B
  - *From: DawnII*

- **LoRA compatibility between model sizes**
  - 14B LoRAs won't work on 1.3B due to dimension differences (5120 vs 1536)
  - *From: Kijai*

- **Quality suffers outside 81 frames**
  - While longer sequences possible, quality degrades
  - *From: Kijai*

- **480p model doesn't generalize to 720p well**
  - 720p model performs worse at 480p than dedicated 480p model
  - *From: Juampab12*

- **Sage attention doesn't work with I2V in native**
  - Cannot use --use-sage-attention startup flag with I2V models in native mode
  - *From: seitanism*

- **Text generation produces gibberish in I2V**
  - Text generation ends up being gibberish in image-to-video, may work better on text-to-video
  - *From: Ro*

- **Compile artifacts with fp8_e5m2**
  - Using compile with fp8_e5m2 quantization creates artifacts in video output on 3090
  - *From: B1naryV1k1ng*

- **High resolution generates poor quality**
  - 4K output (3840x2160) doesn't produce good results despite working
  - *From: seitanism*

- **FP8_fast doesn't provide significant speed benefits**
  - When feedforward layers excluded to maintain quality, speed increase is minimal
  - *From: Kijai*

- **14B model tough on 12GB VRAM**
  - Challenging to run 14B model effectively with only 12GB VRAM
  - *From: Kijai*

- **720x720 resolution causes device errors**
  - RuntimeError about tensors on different devices (cuda:0 and cpu) when trying 720x720, 640x640 works
  - *From: seitanism*

- **Physics accuracy issues**
  - Foot going through skateboard, lacks authentic motion representation, prioritizes image fidelity
  - *From: Zuko*

- **Very slow generation times for 14B model**
  - 65 frames at 720p takes 2190 seconds (36+ minutes)
  - *From: seitanism*

- **SageAttention fp8 kernel fails with I2V**
  - Causes black images due to precision overflow, only affects I2V not T2V
  - *From: Doctor Shotgun*

- **14B LoRA training requires 50GB+ VRAM**
  - 480p videos cause RAM swap on 24GB cards making training extremely slow
  - *From: chancelor*

- **Issues going past 81 frames**
  - While frame limit is uncapped, problems occur beyond 81 frames
  - *From: Kijai*

- **fp8_fast has lower quality**
  - Works but produces lower quality results than standard fp8
  - *From: comfy*

- **720p resolution instability**
  - Less stable than 480p due to limited training at higher resolution
  - *From: Bleedy*

- **I2V sometimes ignores input image**
  - When prompt doesn't match image, model may only use text prompt like IPAdapter
  - *From: Draken*

- **Long videos start looping**
  - Model begins looping after certain point, around 81 frames
  - *From: Kijai*

- **1.3B model quality issues**
  - Described as 'janky' compared to 14B model
  - *From: Parker*

- **GGUF not supported in wrapper**
  - Would require significant work to implement, not currently planned
  - *From: Kijai*

- **CFG scheduling not compatible with most input nodes**
  - Most inputs don't expect lists, need specific nodes like Scheduled CFG Guidance
  - *From: Kijai*

- **32GB model won't fit fully in 32GB VRAM**
  - Will get offloaded partly making it slower unless quantized
  - *From: seitanism*

- **Aggressive CFG scheduling degrades quality**
  - Going from 8/9 to 6 to 1, or 8->7->6->1 messes up a lot
  - *From: seitanism*

- **96 frames causes extreme slowdown**
  - Over 1000 seconds per iteration reported, though may have been a glitch
  - *From: ✧ฅโ๑ↀᆺↀ ๑ใฅ✧PookieNumnums*

- **Object permanence issues**
  - Objects remain visible after explosions or destruction events
  - *From: seitanism*

- **SpargeAttention minimal performance gains**
  - Only 0.3s/it improvement (3s to 2.7s) with 5+ hour tuning requirement
  - *From: Kijai*

- **Language translation loses meaning**
  - Translating between Chinese and English loses nuance, especially with very different language structures
  - *From: seitanism*

- **14B T2V LoRAs load onto I2V but compatibility unclear**
  - Loading works but effectiveness not confirmed
  - *From: Cubey*

- **1.3B model has artifacts and fuzzy distant objects**
  - Pixel-to-pixel consistency issues at distance, likely VAE related. Affects bigger model too but less noticeable
  - *From: Draken*

- **Context schedule transitions aren't great**
  - Motion carries over well but transition quality needs improvement for extended videos
  - *From: Kijai*

- **SpargeAttn not viable yet**
  - Requires training, nothing changes currently
  - *From: Kijai*

- **GGUF generation becomes exponentially slower with more frames when VRAM exceeded**
  - 6min for 33 frames vs 2hrs for 81 frames when running out of VRAM
  - *From: Seb*

- **1.3B model produces stippling artifacts**
  - Requires second pass or upscaling to clean up, 14B doesn't have this issue
  - *From: David Snow*

- **FP8_fast ruins quality**
  - Despite 30% speed improvement, quality degradation makes it unusable
  - *From: Kijai*

- **GGUF may not work with multi-GPU setups**
  - Only native nodes support GGUF, wrapper may have issues
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Wan dataset appears compressed/washed**
  - Latent space highly compressed compared to other models
  - *From: TK_999*

- **High resolution single-pass creates duplicates**
  - 1920x1080 single pass shows duplicates in preview
  - *From: David Snow*

- **Width must be divisible by 16**
  - Gets tensor errors otherwise
  - *From: Kijai*

- **Sage attention compatibility issues with i2v**
  - sageattn_qk_int8_pv_fp8_cuda produces black images on Ada GPUs
  - *From: Doctor Shotgun*

- **Poor prompt adherence**
  - Still at level of trying to get reasonable output each seed, let alone following prompts
  - *From: deleted_user_2ca1923442ba*


## Hardware Requirements

- **Model size**
  - I2V 14B model: 66GB in fp32, 16.5GB in fp8
  - *From: Fannovel16 🇻🇳, seitanism*

- **1.3B model VRAM**
  - 8.19 GB VRAM required, compatible with consumer GPUs
  - *From: thaakeno*

- **14B model size**
  - Around 66GB in fp32, 40GB+ in bf16, needs high-end hardware
  - *From: multiple users*

- **RTX 4090 performance**
  - 4 minutes for 5-second 480P video generation
  - *From: thaakeno*

- **1.3B model generation time**
  - About 4 minutes on RTX 4090 for 50 steps, 3 minutes for basic generation
  - *From: Parker*

- **14B model VRAM**
  - Around 120GB VRAM required, doesn't work on single H100 without offloading
  - *From: samurzl*

- **4060 Ti 16GB compatibility**
  - Can run 1.3B model with sage-attention 2 and torch.compile modifications
  - *From: Pol*

- **720p generation time**
  - Says 6:19 remaining for 720p on 4090
  - *From: Parker*

- **14B model VRAM**
  - Runs under 24GB VRAM with DiffSynth settings, uses about 20GB
  - *From: ArtOfficial*

- **1.3B model performance**
  - 3.6-4.1s/it generation speed reported
  - *From: seitanism*

- **I2V generation time**
  - 15 minutes for 50 steps on unspecified hardware
  - *From: seitanism*

- **VRAM for I2V 14B**
  - Fits under 20GB VRAM, max allocated 16.763 GB
  - *From: burgstall*

- **4090 performance**
  - 50 steps takes 10m, 30 steps 6m at 480x480x81 frames
  - *From: Juampab12*

- **5090 performance**
  - 544x704x129 frames at 10 steps takes 4 minutes
  - *From: seitanism*

- **3090 performance**
  - 720x480x81 at 22s/it, slower than Hunyuan
  - *From: slmonker(5090D 32GB)*

- **4060ti 16GB compatibility**
  - Can run 544*960 resolution 10 steps 49 frames
  - *From: wange1002*

- **3060 12GB limitation**
  - Cannot run 14B model, gets stuck on sampler
  - *From: ArcherEmiya*

- **1.3B T2V VRAM usage**
  - 11GB VRAM for 200+ frames, 7GB for 480x840 30 steps 81 frames
  - *From: TK_999*

- **720P I2V VRAM usage**
  - Less than 7GB VRAM for 1280x720x81 frames on 1.3B
  - *From: burgstall*

- **4060Ti 16GB performance**
  - 480x848 resolution: 65s per step, 544x960 resolution: 260s per step
  - *From: wange1002*

- **4090 performance**
  - 30 steps: 11 min, 50 steps: 19:30 min, 10 steps: 4 min at 480x800
  - *From: Parker*

- **3090 performance**
  - 720P generation takes 20+ minutes, only utilizing 33% VRAM
  - *From: burgstall*

- **Max memory usage example**
  - Max allocated: 5.309GB, Max reserved: 6.875GB for 1280x720x81
  - *From: burgstall*

- **1.3B model on RTX 3060**
  - 9.5 s/it with ComfyUI native
  - *From: CDS*

- **14B model timing**
  - 4090: 6-9 minutes for I2V (61-73 frames), 4x3090ti: supports 480x832
  - *From: ezMan*

- **VRAM for 720p**
  - 24GB VRAM needs block swapping, 35 blocks works for 1280x720
  - *From: Pedro (@LatentSpacer)*

- **16GB VRAM support**
  - Can run 480x480 with block swap 16 and offloading
  - *From: zelgo_*

- **4090 performance benchmarks**
  - 25 frames 720x1280: 177s, 49 frames 544x960: 174s, optimal 73 frames 480x848: 225s
  - *From: huangkun1985*

- **VRAM usage**
  - 1.3B T2V uses 5-6GB inference, I2V 14B 720p 97 frames max 10.2GB
  - *From: Draken*

- **5090 speed**
  - 480x720x81 frames in 5 minutes with 30 steps
  - *From: Kijai*

- **3090 limitations**
  - 1 hour estimated for 81 frames on 3090 vs 30 minutes on 4090
  - *From: wooden tank*

- **LoRA training VRAM**
  - Nearly caps 24GB VRAM at 512 resolution, 26GB for 256 video training up to 65 frames
  - *From: Kytra*

- **14B model inference**
  - Uses 23GB VRAM on 4090, takes 524 seconds for 30 steps
  - *From: GalaxyTimeMachine (RTX4090)*

- **1.3B model performance**
  - 19% VRAM usage with 20 block swap, 158 seconds execution time
  - *From: GalaxyTimeMachine (RTX4090)*

- **Video training memory**
  - 512x videos with up to 65 frames uses 45GB on A40
  - *From: samurzl*

- **14B I2V on 3090**
  - 512x512x65 frames: 25min, 45s/it at 20 steps
  - *From: ˗ˏˋ⚡ˎˊ-*

- **14B I2V on 4090**
  - 1280x720 81 frames: 34-58min depending on steps
  - *From: Pedro (@LatentSpacer)*

- **1.3B vs 14B speed on 4090**
  - 1.3B: 36sec vs 14B: 3min 33sec for 512x512x53
  - *From: Kijai*

- **14B training on A40**
  - 42.5GB VRAM usage, LoRA rank 64, multi-resolution
  - *From: mamad8*

- **1.3B training memory**
  - 13GB memory for 1280x704 images only
  - *From: Cseti*

- **Ada 6000 performance**
  - 11 minutes for I2V generation
  - *From: comfy*

- **VRAM for 1.3B T2V**
  - 3090 can do 480x720x81 in 3 minutes, works well on 12GB cards
  - *From: B1naryV1k1ng*

- **VRAM for 14B I2V**
  - Takes 15-20 minutes on 3090, 1 hour on 4090 at 1280x720x81f with blockswap 40
  - *From: Juampab12*

- **5090 performance**
  - 30% speed increase over 4090, 1280x720x81 takes 3 minutes on 1.3B T2V with sage+compile
  - *From: seitanism*

- **4K generation**
  - 3840x2160x33 takes 2128 seconds (35+ minutes) on high-end hardware
  - *From: seitanism*

- **40GB VRAM for full bf16 model**
  - Native ComfyUI implementation needs ~40GB for full precision model
  - *From: Kijai*

- **5090 performance**
  - *From: Kijai*

- **4090 performance with 1.3B**
  - 31 seconds for 33 frames at 20 steps
  - *From: ingi // SYSTMS*

- **4060 Ti performance**
  - 832x480x81 frames getting 80s/it with 31 blocks swapped on I2V 14B fp8
  - *From: Colin*

- **12GB VRAM minimum**
  - Can run 512x512 I2V with SageAttention and torch optimizations
  - *From: Miku*

- **4090 capabilities**
  - Can handle 768x768x81 with auto offloading, 1280x720x81f with manual offloading
  - *From: comfy*

- **3090 performance**
  - 848x480x81 frames at ~22s/it with fp8 models and torch compile
  - *From: Organoids*

- **Torch compile speed boost**
  - 20-30% speed improvement on compatible GPUs
  - *From: Kijai*

- **14B 720p generation**
  - Takes 36 minutes for 3 seconds on 4090, 30+ minutes for 5 seconds on 4080
  - *From: seitanism*

- **14B 480p generation**
  - 10-20 minutes on RTX 3090, 9 minutes for 81 frames at 848x480 with GGUF Q8
  - *From: B1naryV1k1ng*

- **VRAM for bf16 vs fp8**
  - 24GB VRAM would OOM with load_device main_device on bf16, fp8 weights much more manageable
  - *From: seitanism*

- **5090 performance estimates**
  - Expected 25-30% faster than 4090, not 50% as initially hoped
  - *From: seitanism*

- **Memory management**
  - GGUF can be faster than non-gguf when regular model spills over/gets offloaded
  - *From: seitanism*

- **VRAM for 720p bf16 I2V**
  - 32.8GB model size, needs >32GB VRAM to fit fully or will offload
  - *From: Shawneau 🍁 [CA]*

- **Performance on RTX 5000 Ada**
  - 90 seconds per iteration for 81 frames at 1280x720 with fp8 I2V
  - *From: Shawneau 🍁 [CA]*

- **Performance on 5090**
  - 832x480x81 on 1.3B model: 20/20 steps in 37 seconds (1.86s/it)
  - *From: Kijai*

- **RAM recommendations**
  - 32GB not enough, 64GB insufficient, 96GB recommended for comfortable usage
  - *From: seitanism*

- **3080Ti I2V capability**
  - Can run I2V at default settings, 363 seconds for standard generation
  - *From: Teslanaut*

- **4x3090Ti multi-GPU setup**
  - 30 s/it for 14B 720x1280 I2V with tweaks
  - *From: intervitens*

- **4090 performance with different kernels**
  - 43 s/it with SageAttention 8+8, 51 s/it with 8+16, 75 s/it with xformers
  - *From: Doctor Shotgun*

- **5090D 32GB performance**
  - 30s/step to 13s/step improvement with optimizations, 18s/step with bf16
  - *From: slmonker(5090D 32GB)*

- **12GB VRAM options**
  - GGUF Q4 or native fp8, with GGUF needed for LoRA support
  - *From: ZEALOT*

- **14B T2V VRAM usage**
  - 832x480x81 frames on 4090 with optimizations: 4min 41sec total
  - *From: Kijai*

- **1280x720x81 frames memory**
  - Only 24GB VRAM usage, better scaling than Hunyuan at high resolution
  - *From: pagan*

- **3090 performance**
  - 1.3B FP16: 8sec/it for 30 steps 65 frames. 832x480x65 takes 300 seconds total
  - *From: ˗ˏˋ⚡ˎˊ-*

- **1.3B model size**
  - 5GB in fp32, only 1.5GB in fp8. With text encoders totals ~11GB disk space
  - *From: Kijai*

- **8GB cards support**
  - Only 1.3B model could fit with reasonable inference times
  - *From: Kijai*

- **4060 8GB can run 832x480x65 frames**
  - 6-8 minute generation times on RTX 4060 with 8GB VRAM
  - *From: Googol*

- **4090 recommended for FP16 accumulation**
  - Best performance with FP16 compute and accumulation enabled
  - *From: Kytra*

- **PyTorch 2.7.0 nightly needed for FP16 accumulation**
  - Required for torch.backends.cuda.matmul.allow_fp16_accumulation feature
  - *From: Kijai*

- **5090 performance**
  - 832x480x49 frames: 6.90s/it, 1280x720: 19.61s/it, uses 26GB VRAM with fp8
  - *From: Kijai*

- **4090 performance**
  - 1280x720x81f: 38 s/it with fp8 weights, fp16 compute, torch compile, sage 8+8
  - *From: Doctor Shotgun*

- **3090 VRAM limits**
  - BARELY able to fit T2V 14B at Q8, I2V might OOM. Q6-K recommended
  - *From: Benjaminimal*

- **3090 optimization limitations**
  - No native fp8 support, Q8 and fp8 execute at same speed due to casting overhead
  - *From: Benjaminimal*

- **Generation time comparison**
  - 640x352x49f takes 3-4min, considered very slow
  - *From: N0NSens*


## Community Creations

- **Sage-attention 2 implementation** (tool)
  - Hacky implementation to replace flash-attention for running on lower VRAM GPUs like 4060 Ti 16GB
  - *From: Pol*

- **Dynamic height/width patch** (tool)
  - Code modification for DiffSynth to make height/width dynamic based on input image
  - *From: ArtOfficial*

- **ComfyUI-WanVideoWrapper** (node)
  - ComfyUI wrapper for Wan video models
  - *From: Kijai*

- **Quantized FP8 model weights** (model)
  - FP8 quantized version of Wan I2V 14B model
  - *From: Kijai*

- **WanVideoWrapper** (node)
  - ComfyUI wrapper for Wan video models with I2V and T2V support
  - *From: Kijai*

- **WanVideo ComfyUI wrapper** (node)
  - ComfyUI integration for Wan video models
  - *From: Kijai*

- **Native ComfyUI implementation** (node)
  - Official ComfyUI support with repackaged models
  - *From: comfy*

- **UMT5-XXL encoder extraction scripts** (tool)
  - Scripts to merge model shards and extract encoder-only version
  - *From: Pedro (@LatentSpacer)*

- **Wan LoRA training setup** (workflow)
  - Easy setup using diffusion-pipe, works with 1.3B model
  - *From: Kytra*

- **Native ComfyUI nodes** (node)
  - WanImageToVideo node for native implementation
  - *From: comfy*

- **Copic marker style LoRA** (lora)
  - 88MB style LoRA trained on 75 images, epoch 7 = 1400 steps
  - *From: Kytra*

- **Retro anthro style LoRA** (lora)
  - Style LoRA trained on 528 images for 3 epochs
  - *From: Kytra*

- **WanVideoWrapper** (node)
  - Kijai's wrapper implementation for ComfyUI
  - *From: Kijai*

- **Wan training info channel request** (community request)
  - Channel specifically for LoRA training info and feedback
  - *From: mamad8*

- **Wan2.1 I2V Motion Video Prompt Generator** (prompt system)
  - Structured prompt generator using Subject+Scene+Action framework
  - *From: AJO*

- **Video comparison interface** (tool)
  - Simple interface where you drop 2 videos and it plays them in loop and in sync
  - *From: mamad8*

- **14B LoRA training** (lora)
  - Successfully trained character LoRA on 14B model with 16 frames at 420p
  - *From: Cubey*

- **SageAttention selector node** (node)
  - Custom node for selecting specific SageAttention kernels in ComfyUI
  - *From: Miku*

- **RifleX patch for Wan** (tool)
  - Adaptation of RifleX temporal consistency for Wan models
  - *From: Kijai*

- **RifleX patcher node** (node)
  - Helps prevent looping in longer videos by reducing high frequency attention
  - *From: Kijai*

- **Scheduled CFG Guidance node** (node)
  - Allows CFG scheduling in native sampler
  - *From: Kijai*

- **CFG Schedule node** (node)
  - Allows CFG scheduling with native workflows
  - *From: Kijai*

- **Enhance video node** (node)
  - Enhances attention results every block on every step
  - *From: Kijai*

- **Dictionary translation node** (node)
  - Translates prompts to Chinese for better adherence
  - *From: AJO*

- **WanVideoWrapper** (node)
  - Kijai's ComfyUI wrapper for Wan models with SageAttention support
  - *From: Kijai*

- **Discord bot with 1.3B model** (tool)
  - Automated video generation through Discord interface
  - *From: AJO*

- **Multi-GPU implementation** (repo)
  - 4x3090Ti setup with optimizations, repo coming soon
  - *From: intervitens*

- **WanVideoWrapper** (node)
  - Kijai's ComfyUI wrapper for Wan models with experimental features
  - *From: Kijai*

- **Power consumption comparison tool** (tool)
  - Compares GPU power usage between different models/configurations
  - *From: Benjaminimal*

- **Sage attention control node** (node)
  - Allows enabling/disabling sage attention per workflow without global flags
  - *From: Kijai*

- **Modified FlowEdit for I2V** (workflow)
  - Adapted FlowEdit implementation specifically for Wan I2V model
  - *From: Zuko*

- **Wan+HunyuanVideo refinement workflow** (workflow)
  - Two-pass system using Wan for generation and HunyuanVideo for artifact cleanup
  - *From: David Snow*

- **FL_Image_Notes node** (node)
  - Adds black banner with text overlay for comparison videos
  - *From: Kytra*
