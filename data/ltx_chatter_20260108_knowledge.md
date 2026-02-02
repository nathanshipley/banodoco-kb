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
