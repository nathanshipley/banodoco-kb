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
