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
