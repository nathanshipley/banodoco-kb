# Wan Chatter Knowledge Base
*Extracted from Discord discussions: 2025-03-01 to 2025-04-01*


## Technical Discoveries

- **Second pass through sampler significantly improves quality**
  - Running video through a second sampler produces much better results than single pass
  - *From: David Snow*

- **GGUF Q8 720p allows 1280x720x81 in 16 minutes**
  - Using GGUF Q8 quantized model at 720p resolution for 81 frames takes about 16 minutes
  - *From: seitanism*

- **FP16 accumulate provides 20-30% speed increase**
  - FP16 accumulate dtype gives significant speed boost that stacks with compile and sageattn
  - *From: Kijai*

- **Context window implementation working for endless video**
  - Window blending works well for long video generation, processed 257 frames with 1.3B model in 5 mins using under 5GB VRAM
  - *From: Kijai*

- **Adding 'realistic, cinematic' to prompts greatly improves output quality**
  - Simple prompt additions can dramatically improve generation quality
  - *From: seitanism*

- **UniPC sampler significantly outperforms DPM++ for WAN video generation**
  - UniPC produces better results with improved texture detail and fewer artifacts compared to DPM++
  - *From: Kijai*

- **PyTorch 2.7.0 nightly with fp16 accumulation provides ~20% speed improvement**
  - Latest nightly build enables fp16 optimization specifically for this model
  - *From: Kijai*

- **Double pass generation (2x20 steps) produces better results than single pass (40 steps)**
  - Running generation through second sampler with low denoise settings improves quality, especially visible in beard details
  - *From: David Snow*

- **Shift values between 8 and 15 work well with context options**
  - Testing shows higher shift values can be effective when using context windowing
  - *From: toyxyz*

- **Frame count significantly affects generation quality**
  - 81 frames is the model default, going over (like 121 or 129) causes artifacts and degradation
  - *From: Kijai*

- **fp16_accumulation parameter significantly improves quality**
  - New parameter that works well with WAN models, part of latest ComfyUI optimizations
  - *From: Juampab12*

- **Wrapper consistently produces better quality than native implementation for I2V**
  - Multiple users confirmed wrapper produces superior results, especially for complex prompts and activities
  - *From: T8star-Aix*

- **Native implementation has visible dither pattern issues**
  - Particularly noticeable on beards and textures, described as 'little box texture things' or VR screendoor effect
  - *From: Kijai*

- **Wrapper better handles non-standard sizes**
  - Native requires strict size adherence for best results, wrapper performs well at any size
  - *From: T8star-Aix*

- **SDE DPM sampler performs better than UniPC**
  - Though slower, produces better quality results in testing
  - *From: Juampab12*

- **fp8 matrix multiplication performs poorly on WAN**
  - fp16 accumulate works much better than fp8 for this model
  - *From: comfy*

- **Feta (enhance a video) node provides significant quality improvements**
  - Huge difference in background detail and overall quality when enabled
  - *From: David Snow*

- **Wan VAE uses magnitudes less memory than Hunyuan VAE**
  - Doesn't need tiled VAE like Hunyuan, far more memory efficient
  - *From: Kijai*

- **TeaCache optimization technique working**
  - Model input/output graphing with time step embeds to calculate polynomial fitting for skipping steps and using cache
  - *From: Kijai*

- **1025 frames possible with sliding context windows**
  - 512x512 resolution, decoding took only 16GB without spatial tiling
  - *From: Kijai*

- **Native implementation 10-15% faster than wrapper**
  - Wrapper takes longer but produces better quality results
  - *From: Kijai*

- **Loops appear naturally at certain frame counts and resolutions**
  - 129 frames at 640x480 creates natural loops, also happens at 125 frames
  - *From: TK_999*

- **Wan 14B bf16 GGUF fits in 32GB VRAM**
  - Successfully running on that VRAM amount
  - *From: Shawneau 🍁 [CA]*

- **Skyreels works best at specific resolution and framerate**
  - 960x544x97x24fps is optimal
  - *From: Benjimon*

- **TeaCache provides massive speed improvements for Wan video generation**
  - Speed improvements of approximately 50% - from 53 seconds to 28 seconds, 1 hour to 18 minutes for 1280x720x81fx50 steps, 730 seconds to 430 seconds for native vs wrapper with TeaCache
  - *From: Kijai*

- **Wan 2.1 14B model works well for image generation**
  - The t2v model is pretty good for images, lacks texture compared to flux but 1.3B WanX is more coherent than 2.5B SD3.5
  - *From: CDS*

- **TeaCache implementation without polynomial coefficients still works effectively**
  - Kijai skipped the polynomial fitting coefficients calculation and used direct thresholding based on time embed relative L1 distance, which works well with Wan model
  - *From: Kijai*

- **Video models may understand relations and context better than image models**
  - WanX trained on image sequences can understand relations, logic and context better than pure image models because video models learn more from sequences
  - *From: CDS*

- **TeaCache provides significant speed improvements**
  - 100% speed up for T2V reported, 30 step generation time reduced by half, from 41s/it to around 20s/it typical improvements
  - *From: slmonker*

- **TeaCache causes slight quality loss but acceptable**
  - Video quality degrades slightly with TeaCache but still very acceptable, especially for close-up shots where difference is minimal
  - *From: slmonker*

- **Wan has excellent prompt adherence compared to other models**
  - After hundreds of LTX generations, user reports Wan actually follows prompts much better
  - *From: N0NSens*

- **TeaCache VRAM overhead is about 12-13%**
  - Baseline 72% VRAM usage rose to 84% when TeaCache started
  - *From: DevouredBeef*

- **Camera movement prompts work well in Wan**
  - Prompts like 'camera gradually zooms out', 'camera slowly zooms in' produce good results with proper camera movements
  - *From: VRGameDevGirl84*

- **SDXL to Wan I2V workflow improves quality significantly**
  - Using SDXL generated image as input to Wan I2V sharpens the image and improves colors
  - *From: deleted_user_2ca1923442ba*

- **Wan adapts various art styles well unlike SDXL**
  - Wan seems to adapt various art style pretty well unlike original SDXL models that often stick with certain type of art style
  - *From: for1096*

- **TeaCache reduces generation time by ~2x**
  - 4-5min for 73 frames at 30-40 steps instead of 8min20 without teacache
  - *From: JmySff*

- **Wan follows prompts very precisely**
  - It follows prompts very exact - you could do like, Person claps, and then the person jumps and it will work
  - *From: Draken*

- **Area composition nodes now work on video models**
  - ComfyUI area composition nodes now work on video models
  - *From: comfy*

- **fp16 accumulation provides significant speed improvements**
  - torch.backends.cuda.matmul.allow_fp16_accumulation = True provides noticeable speed improvements
  - *From: Kijai*

- **fp16_fast is about 20% faster than regular fp8**
  - Performance improvement when using fp16_fast precision mode
  - *From: Kijai*

- **fp8 weight with fp16_fast works well**
  - Can combine fp8 weights with fp16_fast for better speed without major quality loss
  - *From: Juampab12*

- **Wan can support 1440×1440 resolution with good results**
  - Higher resolution produces clearer and better I2V results, similar to how Kling does it
  - *From: BNP4535353*

- **RifleX improves ground stability in videos**
  - Ground doesn't slide as much with RifleX enabled compared to without
  - *From: Draken*

- **Context windowing works with I2V but uses same image for each window**
  - I2V context processing limitation - each window starts with the same input image
  - *From: Kijai*

- **fps sampling could improve temporal consistency**
  - Apollo paper shows fps-based sampling maintains consistent temporal intervals vs uniform sampling which distorts temporal relationships
  - *From: fredbliss*

- **TeaCache works fine for I2V when properly configured**
  - Default TeaCache settings are for 30 steps, needs adjustment for different step counts
  - *From: Kijai*

- **FPS sampling from Apollo paper can be implemented in WanVideo**
  - Maintains consistent time intervals between frames rather than uniform distribution. Apollo paper found this superior for temporal understanding
  - *From: fredbliss*

- **Context windowing settings affect frame generation quality**
  - 81 context frames against 81 max frames just looks like normal i2v gen, but 41 context against 81 max frames makes latent noise
  - *From: TK_999*

- **TeaCache won't work with context windowing**
  - TeaCache is incompatible with context window settings
  - *From: Kijai*

- **Latent interpolation can be combined with FPS sampling**
  - Generate keyframes at low fps, interpolate between frames in latent space before decoding for smoother motion
  - *From: fredbliss*

- **FPS-based sampling can improve quality and consistency across all video lengths**
  - Meta Apollo paper shows videos from short 3-second clips to 30-second sequences showed improved visual quality and temporal consistency with FPS sampling. Even for 5-second clip at 24fps (120 frames), generating 30 frames (6fps) with interpolation is faster, more consistent, and often higher quality than generating all 120 frames directly
  - *From: fredbliss*

- **Multiple optimization combinations working together**
  - Using sageattention + torch.compile + fp16 accumulation + Teacache + Adaptive Guidance together for significant speed improvements
  - *From: Miku*

- **Adaptive Guidance acts like teacache with additional benefits**
  - Can be used together with teacache for combined speed improvements, provides automated CFG=1 setting during workflow
  - *From: Miku*

- **Start/end parameters fix teacache motion issues**
  - Teacache with start_percent 0.20 fixed motionless generation issues and reduced generation time to 3min34
  - *From: JmySff*

- **TeaCache and Adaptive Guidance don't work well together in native implementation**
  - TeaCache implementation can't handle splitting CFG when used with Adaptive Guidance
  - *From: Kijai*

- **GGUF models are slower than fp8 for Wan**
  - GGUFs need to be dequantized, while fp8 is natively supported on ada and above GPUs
  - *From: intervitens*

- **Pixel upscaling is better than latent upscaling**
  - Latent upscale is really bad, only useful when using higher denoise where it doesn't matter
  - *From: Kijai*

- **Frame count affects quality**
  - Anything other than 81 frames is suboptimal with this model
  - *From: Kijai*

- **Model sensitivity to attention implementations**
  - Got minor but visible visual differences on the same image, prompt and seed by switching attention implementations (flash/sage/pytorch sdpa) for the CLIP
  - *From: intervitens*

- **Vision part is same between models**
  - The vision part is the same model, should not be any difference between RoBERTa and clip_vision_h
  - *From: Kijai*

- **TeaCache quality is highest quality optimization that stacks with almost everything**
  - Additional optimization that provides best quality hit while being compatible with other optimizations
  - *From: Kijai*

- **WanVideoWrapper works significantly better on synthetic inputs**
  - Model works much better on HunyuanVideo outputs as inputs than on regular images, suggesting shared backbone/data
  - *From: fredbliss*

- **More than 512 tokens in input prompt causes instability**
  - Given T5 architecture, exceeding 512 tokens leads to unstable generation
  - *From: fredbliss*

- **Native wrapper shows different noise pattern compared to wrapper**
  - Native version produces larger noise patterns and beard noise issues that wrapper doesn't have
  - *From: David Snow*

- **TeaCache compares modulated time embed to model output after all blocks**
  - Implementation compares relative distances between modulated time embed and model output right after transformer blocks
  - *From: Kijai*

- **Wan can do timelapses**
  - Model can generate time-lapse videos of flowers blooming, trees growing, and other temporal progressions
  - *From: Kijai*

- **💩 works as negative prompt**
  - Using emoji poop symbol as negative prompt produces decent outputs
  - *From: fredbliss*

- **Model supports multilingual prompts with emojis**
  - Can use almost any language and/or emojis together in prompts to steer generation
  - *From: fredbliss*

- **Latent crossfade concept for context windows**
  - Proposed alpha blending method for overlapping frames between context windows
  - *From: fredbliss*

- **WAN inpainting implementation working**
  - Ported diffusers pipeline_stable_diffusion_inpaint_legacy code to wan for inpainting and i2v
  - *From: andreas*

- **Latent masking works with Wan**
  - Can use latent masking techniques for selective generation
  - *From: andreas*

- **TeaCache and context windowing are incompatible**
  - Using both together leads to noise artifacts. TeaCache works with both T2V and I2V, but cannot be used with context windowing for long videos
  - *From: Kijai*

- **Context windowing produces better results than RifleX for long videos**
  - 161 frame comparison showed context windowing maintained better temporal consistency while RifleX created constant looping artifacts
  - *From: Kijai*

- **GGUF Q8 can be faster than Q6_K even when partially loaded**
  - Q8 listed as partially loaded was still going slightly faster than Q6 which was fully loaded, though fp8 was still fastest overall
  - *From: Organoids*

- **Noise augmentation significantly improves I2V motion**
  - Adding 0.02 noise augment strength to I2V creates much more motion and allows action to happen in realistic content
  - *From: Juampab12*

- **RoPE frequency adjustment can be used for frame interpolation**
  - Modifying RoPE frequencies with temporal emphasis and motion smoothness parameters for spatiotemporal interpolation between keyframes
  - *From: fredbliss*

- **VHS update enables animated previews during generation**
  - Recent VHS update allows seeing animated previews while generation is running, saving time on bad generations
  - *From: Kijai*

- **bf16 produces better results than fp16 for Wan**
  - Switching everything back to bf16 instead of fp16 showed significant improvement in output quality
  - *From: AJO*

- **Multiple prompts can be used by separating with |**
  - You can give the model multiple prompts by separating them with | symbol, it tries to spread them over context windows
  - *From: Kijai*

- **Context windows use prompts per 20 latents = 80 frames**
  - Each latent has 4 pixel frames, so prompt for every 20 latents equals 80 frames total
  - *From: Kijai*

- **TeaCache at start_0 shows no quality degradation**
  - Using TeaCache from the beginning with no apparent quality loss while significantly reducing generation time
  - *From: Juampab12*

- **WAN loops after 81 frames**
  - The model starts to loop/repeat after 81 frames
  - *From: Kijai*

- **Overlap 24 is effective for maintaining original image consistency**
  - Using overlap 24 in sliding context keeps better consistency with the original image
  - *From: Cubey*

- **TeaCache coefficients from patches_II don't work properly on larger models**
  - The coefficients seem calculated for 1.3B model only and don't trigger on I2V or larger models
  - *From: Kijai*

- **TeaCache works only on 1.3B model starting around 0.2**
  - The new TeaCache implementation only functions on the 1.3B model and needs to start at around 0.2 threshold
  - *From: Kijai*

- **FBCache (First Block cache) works as alternative to TeaCache**
  - Originally introduced in Wavespeed nodes, doesn't need tuning per model, but seems slightly worse in general. Can't be used together with TeaCache
  - *From: Kijai*

- **PyTorch 2.6.0 nightly gives 20% speed increase**
  - With new full fp16 accumulation feature, works for both native and wrapper
  - *From: Kijai*

- **Native 1.3B model is faster than wrapper**
  - Native runs 1.3B model differently and is faster - it batches the cfg instead of doing it separately
  - *From: Kijai*

- **Context windows don't work with TeaCache**
  - TeaCache node fails when used with long video production and context windows
  - *From: sunnywang*

- **Cosmos empty latent creates half the frames**
  - Cosmos temporal factor is 8 (8 images in latent), while Hunyuan/Wan is 4, so using Cosmos node generates half the frames and appears faster
  - *From: Kijai*

- **FPS interpolation with context windowing works**
  - Fredbliss developed a system that can generate videos at low FPS (like 2fps) and interpolate frames to achieve higher output FPS (like 16fps), using latent interpolation logic with Wan's context windowing
  - *From: fredbliss*

- **Wan can fill interpolated frames in latent space**
  - The model has learned to take an input frame and up to 16 frames in advance, and fill in the 0's with interpolated values, possibly due to i2v training
  - *From: fredbliss*

- **TeaCache conflicts with context windowing**
  - TeaCache doesn't work with regular context windowing according to testing
  - *From: TK_999*

- **VRAM management node improves quality**
  - Using vram_management node generates at the same speed as original ComfyUI node but in much better quality
  - *From: for1096*

- **Wan FPS is hardcoded to 16fps**
  - 16fps output is hardcoded in the model, making it a main limitation after extensive testing
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Interpolation factor calculation issue**
  - When output_fps and generation_fps are the same, interpolation factor becomes 1 and no frames are interpolated
  - *From: fredbliss*

- **VAE caching causes color differences in first 2-3 latent frames**
  - When looping, VAE uses caching which creates color difference in beginning frames, requiring double decoding to fix
  - *From: Benjaminimal*

- **TeaCache acts as automated step reduction**
  - TeaCache tries to drop steps that matter least, higher threshold = more aggressive = less steps = less quality if too aggressive
  - *From: Kijai*

- **Context windows enable automatic looping**
  - Context windows can wrap around to beginning for automatic looping, no specific frame count requirement other than being at least one frame window size
  - *From: Benjaminimal*

- **VAE being temporally aware causes frame offset**
  - The VAE decoding process is temporally aware and causes a frame offset by 4, which compounds on each frame and gets worse over time, causing green noise and ghosting in interpolated videos
  - *From: fredbliss*

- **Context window frame coverage issue**
  - Missing frames not covered by context windows get duplicated to closest windows, causing jittering in generated videos when using interpolation
  - *From: fredbliss*

- **Linear interpolation creates ghosting**
  - Linear interpolation between keyframes produces ghosting artifacts in the final video output
  - *From: fredbliss*

- **TeaCache with coefficients is more accurate and allows starting from step 0**
  - New TeaCache implementation uses calculated coefficients and should be more accurate. Can potentially start from step 0 instead of requiring higher start steps
  - *From: Kijai*

- **81 frames is optimal for Wan video generation**
  - Anything other than 81 frames produces worse results. In original code it was hardcoded to 81 frames
  - *From: Kijai*

- **FPS sampling is superior to uniform frame sampling for video models**
  - FPS sampling maintains consistent video speed during training, allowing models to learn temporal dynamics more effectively than uniform sampling
  - *From: fredbliss*

- **TeaCache coefficients require different threshold values**
  - With coefficients enabled, threshold needs to be higher (around 0.3) to achieve same skip rate as without coefficients
  - *From: DevouredBeef*

- **LTX keyframe interpolation can work with Wan for frame rate conversion**
  - Generate 4fps Wan video then interpolate to 24fps with LTX as advanced frame interpolator
  - *From: Juampab12*

- **Higher drift shift is key for I2V to work properly**
  - For some reason it seemed like the key for I2V to work was higher drift shift
  - *From: Kijai*

- **TeaCache working for contexting with significant speed improvements**
  - Got some kind of TeaCache working for contexting, saved 30 secs out of 3 mins on this terrible test
  - *From: Kijai*

- **Translating prompts to Mandarin improves video quality**
  - Translating to mandarin makes every video better, have been doing so since day 1
  - *From: Juampab12*

- **BF16 model shows significantly better quality than fp8**
  - The rendering varies from the second scene onwards with BF16, prompt adherence also seems much more effective with the BF16 model compared to fp8
  - *From: JmySff*

- **1.3B model can generate directly at 1280x720 with no issues**
  - 1.3B seemingly no issues with directly generating at 1280x720
  - *From: Benjaminimal*

- **VAE reverse frame technique can mitigate starting flash**
  - Reverse the frames temporally, re-decode the first ~13 frames (which are now the last ~13 frames), then reverse it again to mitigate starting flash
  - *From: Benjaminimal*

- **Wan 1.3b t2v can generate 120 frame videos at 1152x512 resolution**
  - 120f, 30/10 latent frame/stride, 50 steps, native 1152x512, guidance end @ 0.8, unipc
  - *From: Benjaminimal*

- **TEA cache endstep setting can cause issues with context windows**
  - Setting TEA cache endstep at 18 when total steps is 20 can cause problems
  - *From: Cubey*

- **Sage attention --use-sage-attention command line flag is preferred over node**
  - For sage attention in native you just need the cmd line --use-sage-attention. no need for node
  - *From: pagan*

- **FP8 still saves VRAM even when accumulating in FP16**
  - Confirmed that FP8 helps save VRAM despite FP16 accumulation
  - *From: Kijai*

- **Multi-GPU Wan script exists for distributed inference**
  - Multi-GPU script available that can run full quality on 4x 3090ti GPUs
  - *From: intervitens*

- **Wan produces much sharper output compared to Hunyuan I2V**
  - No softening filter on results, significantly clearer image quality
  - *From: aikitoria*

- **Topaz Chronos interpolation makes Wan results look better than Hunyuan motion**
  - When Wan results are interpolated to 60fps with Topaz Chronos, motion quality surpasses Hunyuan
  - *From: aikitoria*

- **FP8 vs FP16 produces virtually identical quality**
  - Visual comparison shows no noticeable difference between precision levels
  - *From: aikitoria*

- **Topaz uses pre-built TensorRT engines**
  - Model files are stored in folders named TensorRT, which explains fast performance
  - *From: aikitoria*

- **Wan 2.1 has exceptional prompt following**
  - Better than closed source solutions at following prompts, though quality may be lower. Can reliably do complex actions like 'open door and walk through'
  - *From: Draken*

- **CFG distillation working on Wan 1.3B model**
  - Using LoRA to distill CFG away, allowing cfg=1 inference with minimal quality loss
  - *From: spacepxl*

- **Nunchaku SVDQuant claims 3x speedup**
  - MIT Han Lab tool claims 3x speedup on 4090/5090 with quantization, but actual boost is ~30% compared to FP8 torch.compile sage attention baseline
  - *From: Ada*

- **20 step vs 50 step shows significant difference in quality**
  - User reported seeing a lot of difference between 20 and 50 steps in their tests
  - *From: Juampab12*

- **SVDquant provides 10.1x speedup on laptop 4090 by eliminating CPU offloading**
  - 3x speedup without CPU offloading, 10x with CPU offloading elimination according to their paper
  - *From: Ada*

- **SVDquant is only 30% faster than reasonable baseline**
  - When compared to torch.compile, FP8 and sage attention baseline on 4090, SVDquant only provides about 30% speedup
  - *From: deleted_user_2ca1923442ba*

- **Spatial multidiffusion works alongside temporal multidiffusion**
  - Successfully generated 1664x960 video using 1.3B model with multidiffusion
  - *From: Benjaminimal*

- **VAE flash fix requires different frame counts for encoding vs decoding**
  - 15 frames for encoding, 13 frames for decoding when doing vid2vid loops
  - *From: Benjaminimal*

- **TeaCache value range changed, old workflows need updating**
  - New default should be 0.3 instead of previous values, can start from 0, 1, or 2 for safety
  - *From: Kijai*

- **CFG distillation works well on Wan 1.3B with minimal training effort**
  - After CFG distillation, gradient estimation sampler works great (doesn't work with base model)
  - *From: spacepxl*

- **CFG distillation is easier to train than step distillation**
  - Don't need synthetic data, works fine with real data, very few training steps needed (1200 steps for 1.3B LoRA)
  - *From: spacepxl*

- **Context stride 4 doesn't work with Wan models**
  - Kijai thinks it's because latent space has 4 frames in one latent
  - *From: Kijai*

- **14B and 480p models have same generation time at same resolution**
  - 720p run 39.9s/it and 480p run 38.9s/it using GGUF version
  - *From: shockgun*

- **720p model was trained from 480p model weights**
  - Weights of lower res model used to initialize training of higher res one
  - *From: deleted_user_2ca1923442ba*

- **FP16 1.3B model follows prompts better with less bad character faces**
  - Improved prompt following and character quality
  - *From: ArcherEmiya*

- **TeaCache values for 1.3B are different with coefficients**
  - Kijai updated documentation to reflect this difference
  - *From: Kijai*

- **LoRA trained on 480p doesn't work right on 720p**
  - Cross-resolution LoRA compatibility issue
  - *From: Cubey*

- **Block swapping can run full 1280x720x81f on 24GB VRAM**
  - Confirmed working with blockswapping enabled
  - *From: intervitens*

- **4090 performance with optimizations: 832x480x81 frames, 20 steps takes ~12 minutes using sage**
  - Using sageattention and torch optimizations
  - *From: Benjimon*

- **720p model requires more block swapping than 480p**
  - 720x1280@81 needed 34 blocks swapped out of 40 vs 26 blocks for 832x640
  - *From: Benjimon*

- **Multi-GPU setup allows fp16 inference without VRAM limits**
  - Using 4x 4090s with distributed processing and model weights split
  - *From: aikitoria*

- **1080p generation is technically possible but produces lower quality results**
  - Generated 1080x1920 video but with motion artifacts and quality issues
  - *From: aikitoria*

- **Wan generates looping-like behavior when generating over 81 frames**
  - It loops when generating over 81 frames, less noticeable for some content but noticeable for action sequences. It's not an exact loop though, movement is slightly varied
  - *From: TK_999*

- **Context windowing works with Wan for unlimited length videos**
  - Can use context windows to generate videos as long as you want, but context windows are difficult to work with for this model
  - *From: Kijai*

- **TeaCache can work without coefficients for better performance**
  - TeaCache works better without coefficients with very low threshold and starting slightly later (from step 2), gives faster rendering and slightly better quality
  - *From: JmySff*

- **Enhance-a-video node provides speed improvements**
  - Enhance-a-video node reduced generation time from 6min35 to 5min36 for 25 steps i2v 480p at 544x960
  - *From: JmySff*

- **Block swapping is faster than multi-GPU for Wan**
  - Block swapping provides roughly same inference time as 48gb GPU while using less VRAM, only slows down about 5%
  - *From: Benjimon*

- **TensorRT RIFE is lightning fast compared to normal RIFE**
  - TensorRT RIFE processes videos much faster than the normal RIFE interpolation, with amazingly low memory usage
  - *From: burgstall*

- **Square format should use 624x624 instead of 480x480**
  - 624x624 is the recommended default for square format based on official inference code, equivalent area to 832x480
  - *From: spacepxl*

- **T2V LoRAs work with I2V models**
  - T2V LoRAs are compatible with I2V and still maintain character consistency from the input image
  - *From: Faust-SiN*

- **Enhance a Video may not be useful for I2V**
  - Testing shows minimal visible difference when using Enhance a Video with I2V workflows
  - *From: Kijai*

- **Wan VAE is extremely memory efficient for long videos**
  - Uses latent-based architecture that encodes/decodes one frame at a time considering previous frame, so 100 frame video uses same VRAM as 200 frame video
  - *From: comfy*

- **Wan 14B model uses massive amounts of RAM**
  - Uses 96GB RAM with blockswapping, can require 128GB plus 37GB swap for full operation
  - *From: seitanism*

- **Control LoRAs can be trained using channel concatenation method**
  - Concatenate control signal along input channel dimension and train LoRA on rest of model, similar to instructpix2pix and flux control models
  - *From: spacepxl*

- **TeaCache can cause quality degradation but significant speed improvements**
  - User reports not noticing much quality loss with TeaCache at 0.4 setting
  - *From: seitanism*

- **sageattn_qk_int8_pv_fp8_cuda causes black screens for Wan I2V**
  - Using this attention optimization results in black video output
  - *From: Doctor Shotgun*

- **RAM timing issues can cause black video generation output**
  - Unstable RAM timings, FCLK, and SOC voltage can cause black output from generations
  - *From: seitanism*

- **Wan has better prompt adherence than Hunyuan generally**
  - Wan corrects typos like 'peach sign' to 'peace sign' while Hunyuan shows actual peach
  - *From: Doctor Shotgun*

- **e5m2 fp8 format works better with torch compile on 3090**
  - 3000 series GPUs can only handle e5m2 format with torch compile, not e4m3fn
  - *From: Kijai*

- **Latest pytorch nightly provides additional 20% speed boost**
  - Installing nightly pytorch gives another performance improvement on top of torch compile
  - *From: Kijai*

- **Squish LoRA trained on only 20 clips**
  - High-quality LoRA achieving near Pika-labs quality with minimal training data
  - *From: Juampab12*

- **WSL2 provides 20% speed boost over Windows**
  - User reported 20% additional performance boost when running ComfyUI on WSL2 compared to native Windows, with same performance as barebone Linux
  - *From: pagan*

- **SageAttention 2.1 upgrade may cause speed regression**
  - User lost 5 seconds of speed after upgrading from SageAttention 1.0.6 to 2.1.0
  - *From: Ashtar*

- **TeaCache node causes blurry results with old wrapper version**
  - TeaCache value of 0.1 with old wrapper version causes extremely blurry outputs, max should be 0.03 with old version
  - *From: Kijai*

- **Wan LoRAs can be trained very quickly on small datasets**
  - Hydraulic press LoRA trained with only 2 videos for 1 epoch (15-20 minutes) on 1.3B model already showed very good results
  - *From: Juampab12*

- **Omitting both t5_cpu and t5_fsdp parameters provides fastest performance if no OOM occurs**
  - Alternative to specific T5 configuration flags
  - *From: intervitens*

- **1.3B tile controlnet generates in 10 seconds**
  - Very fast generation times for tile control
  - *From: Kijai*

- **New tiled VAE should speed things up**
  - Default --tiled_vae_config not optimal for 4 GPUs and 1280x720, should split resolution into chunks divisible by number of GPUs
  - *From: intervitens*

- **Tile control LoRA trained at multiple resolutions: 624x624, 832x480, and 480x832**
  - Multi-resolution training approach
  - *From: spacepxl*

- **LoRA training on 50k videos took 31 hours on single 3090**
  - Using 9 or 13 frames works really well for training
  - *From: spacepxl*

- **Step times: 16 s/it without --dit_fsdp_offload, 17 s/it with it**
  - Performance comparison of offload settings
  - *From: aikitoria*

- **Conv3d operations should be commutative, allowing LoRA stacking**
  - Mathematical basis for stacking control LoRAs: conv3d + condition1 conv3d + condition2 conv3d
  - *From: comfy*

- **PyTorch conv3d might be cross-correlation instead of true convolution**
  - Cross-correlation isn't commutative, which could affect LoRA stacking
  - *From: deleted_user_2ca1923442ba*

- **torch.flip(kernel, dims=[-3, -2, -1]) converts cross-correlation to true convolution**
  - Simple function to convert between correlation types
  - *From: deleted_user_2ca1923442ba*

- **CogVideo-fun control model works with multiple condition types without switches**
  - Could send pose or depth and it just worked, no configuration needed
  - *From: Kijai*

- **Official Go with the Flow LoRAs use massive ranks**
  - Trained rank 2048 and 3072 LoRAs, basically same size as original model
  - *From: spacepxl*

- **Control LoRAs work with I2V and inpainting**
  - You can use control LoRAs for I2V as it already expands the input, also works with inpaint if you handle masks correctly
  - *From: spacepxl*

- **Teacache with rel_l1_thresh = 0.18 reduces time significantly with minimal quality loss**
  - Took time from 15 minutes to 10 minutes with near identical video quality
  - *From: intervitens*

- **NSFW LoRA helps with movement in SFW content**
  - Someone reported using NSFW LoRA for SFW stuff because it helped with movement
  - *From: Cubey*

- **Torch compile gives ~30% speed increase and reduced VRAM usage**
  - Basic inductor compilation provides significant performance boost
  - *From: Kijai*

- **Block compilation per transformer block is more efficient**
  - Regional compilation feature is fully utilized when limiting compile to transformer blocks only
  - *From: Kijai*

- **CFG distill LoRA provides 50-60% speedup for Wan**
  - spacepxl created a CFG distill LoRA for Wan 1.3B that works better with real CFG for first few steps, similar to skyreel approach
  - *From: spacepxl*

- **CFG distill LoRA works better with gradient estimation sampler**
  - Interestingly the CFG distilled version works better with gradient estimation sampler while base model hates that sampler
  - *From: spacepxl*

- **TeaCache fixes VRAM spikes**
  - Fixed vram spikes with teacache implementation
  - *From: intervitens*

- **Wan learns LoRAs extremely fast**
  - Model can learn LoRAs in just 20 minutes of training
  - *From: Juampab12*

- **Tiled VAE encode causes video warping**
  - Tiled encode works poorly causing strange video warping, only tiled decode needed for removing dit_fsdp_offload
  - *From: aikitoria*

- **CFG scheduling works better with I2V than T2V**
  - Scheduling CFG from 5.5 to 1.0 over timesteps provides 2x speedup on later steps without major quality loss for I2V
  - *From: Kijai*

- **WAN learns extremely quickly for LoRA training**
  - Can train a working LoRA in 20 minutes, even with 49 frame videos (takes a few hours for longer videos)
  - *From: Juampab12*

- **Small datasets work for WAN LoRA training**
  - Only need 10-20 videos for a concept + 10 images to retain quality
  - *From: Juampab12*

- **Moving torch compile node to end resolves OOM issues**
  - Torch compile node placement at end of workflow fixes memory errors
  - *From: CJ*

- **WAN I2V model handles low CFG well**
  - I2V model produces good results even at CFG 1.0 without distillation
  - *From: Juampab12*

- **Kijai optimized rope function and achieved 20% faster generation speed**
  - Adjustment to rope function in WanVideoWrapper provided 20% speed improvement, though noted as probably highly inefficient
  - *From: Kijai*

- **TeaCache works better when disabled for first steps**
  - TeaCache causes much less degradation if disabled for some first steps, now disabled for first 10 steps by default, configurable with --tc_start_step
  - *From: intervitens*

- **CFG can be disabled for later steps with minimal quality impact**
  - For I2V, disabling CFG starting from about 15-20 steps causes very little difference but speeds up remaining steps by 2x, configurable with --cfg_steps
  - *From: intervitens*

- **Under 40 steps causes artifacts**
  - With fast movement, 40 steps is not enough and keeps artifacting
  - *From: aikitoria*

- **TeaCache memory spike issue**
  - TeaCache causes a 2GB spike in memory usage even with offload_device enabled
  - *From: garbus*

- **VAE encode/decode with Flux VAE can improve SD 1.5 images**
  - Create SD 1.5 image, VAE decode to image file, then VAE encode with Flux VAE and decode again - pushes it closer to Flux photographic style
  - *From: deleted_user_2ca1923442ba*

- **Skip layer guidance technique works on Wan**
  - Skipping block 8, 9, or 10 (especially 10) on uncond inference improves quality - essentially STG but only on negative
  - *From: IllumiReptilien*

- **Wan I2V architecture supports multiple input frames theoretically**
  - Takes full extra latent and mask, but only trained on one frame at start - LoRA might improve this
  - *From: aikitoria*

- **Wan can generate 161 frame videos but quality degrades**
  - Embedding supports longer lengths but wasn't trained on them, causes weird looping
  - *From: aikitoria*

- **Skip block 10 on unconditional pass improves Wan 14B quality**
  - Skipping block index 10 (11th block) during unconditional denoising consistently improves generation quality across different tests
  - *From: aikitoria*

- **Skip block technique doesn't work universally across all Wan models**
  - Block 10 skip works well on 14B model but testing on 1.3B model (30 blocks total) showed no useful improvements in range 5-11
  - *From: Kijai*

- **HunyuanVideo outputs work better as I2V inputs for Wan**
  - Using HunyuanVideo generated frames as input images to Wan I2V performs significantly better than regular images
  - *From: fredbliss*

- **fp16 is faster and better quality than bf16 on consumer GPUs**
  - fp16 is about 20% faster on RTX 4090 and produces better results because Nvidia gimped bf16 accumulation on tensor cores for consumer cards
  - *From: aikitoria*

- **480p model has better motion coherence than 720p**
  - 480p model works fine at 720p resolution with less detail but more coherence, while 720p model does strange things at times
  - *From: David Snow*

- **SLG (Skip Layer Guidance) on layer 10 improves prompt adherence significantly**
  - Users report much better prompt adherence and coherence when using SLG with layer 10, particularly noted improvement in following complex prompts
  - *From: Cubey*

- **Torch compile provides significant speed improvements**
  - Reduces render times from 42 min to 17 min with teacache, then to 12 min with updated teacache repo. Comparison shows 745s with compile vs 859s without
  - *From: HeadOfOliver*

- **VAE frame duplication technique for timelapse training**
  - Training videos with shape (0,1,1,1,1,5,5,5,5,9,9,9,9) for frame index allows VAE to not compress images, enabling timelapse type videos
  - *From: Juampab12*

- **Control tile lora performs better with reduced shift values**
  - Using shift 1 instead of default 8 increases fine detail and texture definition like hair, though increases overall noise
  - *From: Payuyi*

- **T5 tokenizer contains exploitable leftover tokens**
  - UMT5 model has dataset-specific tokens like [wiki], [web], [c4], [book], [translate] that can target specific training datasets when used in prompts
  - *From: fredbliss*

- **T5 model can be used with special task tokens for text summarization**
  - Used [translate] and [wiki] tokens with T5 to summarize complex prompts into shorter embeddings, like '[translate] putin to trump' or '[wiki] Donald_Trump'
  - *From: fredbliss*

- **SkipLayerGuidanceDiT node dramatically improves prompt adherence**
  - User achieved flying motion and camera tilt that previously failed, working on first try with the skip layer node
  - *From: CapsAdmin*

- **TeaCache with high threshold works well for previews**
  - Using TeaCache with really high threshold provides good way to preview generations quickly
  - *From: CapsAdmin*

- **Euler sampler works better than uni_pc for low step previews**
  - TeaCache with 8-10 steps using Euler works well for previews, unlike uni_pc
  - *From: mamad8*

- **Two-stage workflow for quality enhancement**
  - T2V at 352x528, then use control lora workflow to upscale 3x resolution while changing prompt for outfit/color swap and detail enhancement
  - *From: ramonguthrie*

- **Native workflow faster than wrapper for some users**
  - Wrapper consistently slower than native implementation despite tweaking
  - *From: N0NSens*

- **Looping context already implemented in wrapper**
  - The wrapper already has looping context functionality, just missing seam fix
  - *From: Kijai*

- **Skip layer guidance improves quality for Wan 1.3B**
  - Starting SLG at 0.1 rather than 0 is key for 1.3B quality improvements
  - *From: Kijai*

- **Comfy RoPE implementation can be compiled for speed boost**
  - Switching to ComfyUI's RoPE calculation allows compilation and massive speed difference, though slightly slower without compilation
  - *From: Kijai*

- **Native SLG does 3 passes instead of 2 with CFG**
  - Proper skip layer guidance does extra pass on top of CFG using model without certain layers, making it 20-30% slower
  - *From: Kijai*

- **Torch compile reduces VRAM usage**
  - Compiling the model not only speeds up inference but also reduces VRAM consumption
  - *From: Kijai*

- **Cross attention doesn't benefit from SageAttention**
  - Using sage for cross attention gave zero speed benefit
  - *From: Kijai*

- **SLG amplifies LoRA strength significantly**
  - With SLG disabled, Jinx LoRA has almost no effect, but when SLG is enabled it becomes much more prominent
  - *From: Cseti*

- **SLG stabilizes hands in generations**
  - SLG helps stabilize hand movement and details in video generation
  - *From: Cseti*

- **Can disable most LoRA blocks and LoRA still works fine**
  - Mostly helpful with image trained LoRAs that tend to kill motion
  - *From: Kijai*

- **Tiny VAE preview shows clear results at half the steps**
  - TAEW VAE allows seeing clear preview quality much earlier in the generation process
  - *From: Kijai*

- **Non-blocking transfer uses less RAM but is slower**
  - Optional setting that trades speed for memory efficiency
  - *From: Kijai*

- **DPM++ SDE gives best contrast and sharpness for I2V**
  - Found to produce better visual quality compared to other samplers for I2V
  - *From: JmySff*

- **SLG (Skip Layer Guidance) significantly improves image quality and detail in Wan video generation**
  - Kijai tested different blocks and found skipping blocks 6-9 works well for 1.3B model, blocks 9-10 for 14B. It makes unconditional guidance worse purposely, strengthening CFG effect
  - *From: Kijai*

- **Connecting VAE to context window can improve results**
  - Kijai added VAE connection to context window node - it decodes and encodes the last frame of previous window for I2V conditioning
  - *From: Kijai*

- **Context window resets cause visible quality drops in long generations**
  - Cubey demonstrated 245 frames with visible resets every 5 seconds (though actual timing was 8-9 seconds on second window)
  - *From: Cubey*

- **Torch compile provides ~30% speed improvement and can reduce VRAM usage**
  - Situational performance gain, around 30% faster with these types of models
  - *From: Kijai*

- **Torch compile provides minimal speedup on some GPUs**
  - On 3090ti: 45s/it with compile vs 48s/it without - only 3 second improvement
  - *From: Benjimon*

- **SLG provides minor speedup due to skipped layer work**
  - Gets around 1 s/it speedup because it skips doing some work on a layer
  - *From: Doctor Shotgun*

- **Free noise turned off works better for vid2vid**
  - User found better results with free noise disabled on vid2vid workflows
  - *From: Flipping Sigmas*

- **Performance dramatically improved over time**
  - Generation that took 4 hours two weeks ago now takes 11 minutes (690 seconds) with optimizations
  - *From: Flipping Sigmas*

- **Multiple prompts can be used with | separator**
  - For context windowing, separate prompts with | - prompts should be VERY similar for it to be useful
  - *From: Kijai*

- **CUDA 12.6 with torch==2.7.0.dev20250227+cu128 works despite version mismatch**
  - Built with cu128 but 12.6 cuda can get along without real conflict
  - *From: Cubey*

- **SLG block 10 causes black areas on right side of image**
  - Block 10 tends to put black areas on side of image, block 9 fixes this issue
  - *From: Kijai*

- **SLG makes CFG behave differently**
  - Skip Layer Guidance changes how CFG values work, worth trying different CFG settings
  - *From: Kijai*

- **Multiple SLG blocks can be used with comma separation**
  - Can do comma separated list of blocks like 8,9 for multiple block guidance
  - *From: Kijai*

- **Context options don't work well with I2V**
  - Doesn't work well with I2V because it always goes back to init image, can't do continuity unless camera doesn't move
  - *From: Kijai*

- **fp8_e4m3fn_fast doesn't work with this model**
  - Creates weird noise artifacts, regular e4m3fn works fine
  - *From: Kijai*

- **Past 81 frames can cause glitches**
  - 88+ frames can cause glitches, should avoid going past 88 frames
  - *From: Kijai*

- **Context windowing in video generation processes frames in chunks with overlap, similar to LLM token processing**
  - With context_frames=81, WanVideo processes 81 frames at once (~20 latent frames due to 4:1 compression ratio). Context stride controls frame advancement between windows, context overlap controls blending at window edges
  - *From: fredbliss*

- **Whiteout effect caused by prompt incompatibility in blend zones**
  - When blending prompts with drastically different lighting conditions (night to day), model overcompensates with extreme brightness to satisfy both prompts. More common in short videos where blend zones occupy higher percentage of frames
  - *From: fredbliss*

- **Wan uses T5 text encoder and xlm roberta for clip vision in I2V**
  - T5 doesn't have vision component, but xlm roberta provides clip vision functionality for image-to-video tasks
  - *From: fredbliss*

- **Mobius looping technique works by shifting latents with overlap**
  - New looping node uses shift parameter to control latent overlap. For 49 frames (13 latents), shift of 6 works well. 1 latent = 4 frames
  - *From: Kijai*

- **UniPC scheduler performs better than other schedulers for Mobius looping**
  - Kijai found much better results using UniPC scheduler compared to other options for the looping technique
  - *From: Kijai*

- **Shift skip parameter significantly changes video output quality**
  - Testing values 5 and 6 showed notable differences in video generation
  - *From: TK_999*

- **LoRA can act as quality/speed boost without trigger word**
  - LoRA trained on people images improves sharpness and clarity at 10 steps, making it look like 20 steps without using trigger word
  - *From: VRGameDevGirl84(RTX 5090)*

- **Context windows only use VRAM for the window size, not total frame count**
  - Can generate 1000+ frames using same VRAM as context_frame amount
  - *From: Kijai*

- **Multiple prompts work with context windows using '|' separator**
  - Format: 'prompt1|prompt2' - one prompt per window, automatically distributed
  - *From: Kijai*

- **Loop functionality works with specific settings**
  - 81 length, 30 steps, shift 4, start_percent 0.1, end_percent 1.0
  - *From: avataraim*

- **SLG provides significant speed boost in I2V**
  - Twice speed boost in i2v using SLG option, but quality needs more testing
  - *From: N0NSens*

- **SLG can destroy picture quality**
  - SLG option destroys the picture, may need tweaks to make it less destructive
  - *From: N0NSens*

- **Multi-GPU setup achieves fast inference**
  - 4 GPUs can generate 1280x720p video with 81 frames in 5 minutes using 40 steps, tea cache threshold 0.2 after 10 steps, disabling cfg after 25 steps
  - *From: aikitoria*

- **Torch compile provides 30% speedup**
  - Torch compiled model gives additional 30% performance boost on top of multi-GPU speedup
  - *From: Juampab12*

- **Tilelang kernels provide performance improvements**
  - Rmsnorm implemented with tilelang kernel gives 10 second speedup compared to apex and 20 seconds compared to original
  - *From: intervitens*

- **Context windowing works with long frame counts**
  - Successfully generated 1353 frames at 832x480 with 30 steps, taking 25:37 total time
  - *From: Kijai*

- **Enhanced video workflow produces high quality results**
  - 316 frames at 960x544, 30 steps using SLG, teacache, enhance video features with native version
  - *From: JmySff*

- **spacepxl released WIP depth control LoRA for Wan 1.3b with good structure/motion control**
  - Prompt following not always great, needs recaption with dense VLM captions. Works with early step cutoff for creative results
  - *From: spacepxl*

- **1.3b LoRAs are not compatible with 14b models**
  - The weights are not compatible at all between model sizes
  - *From: spacepxl*

- **Depth LoRA works better on landscape than square format**
  - Trained at 624x624 and 832x480, more landscape data in dataset so square should theoretically be worst
  - *From: spacepxl*

- **Depth LoRA doesn't handle pure black well**
  - Model seems to have issues with solid black values in depth maps, lifting black to slightly higher values helps
  - *From: Kijai*

- **TeaCache causes blob distortions when using multiple LoRAs**
  - Lower TeaCache threshold helps resolve the issue
  - *From: Fawks*

- **Performance boost from rope function change**
  - Changing rope function gives free boost, more effective with compile
  - *From: Kijai*

- **Context windows work with depth control**
  - Control embeds work out of the box with context windows since it's not separate control signal
  - *From: Kijai*

- **Frame padding issue in context windows**
  - Code is padding latents so doing 81 frames actually does 85, causing artifacts similar to doing 85 frames normally
  - *From: Kijai*

- **WanVideoStartEndFrames adds extra frames**
  - ComfyUI-WanVideoStartEndFrames concats end frame resulting in num_frames + 1, may add up to 5 extra frames
  - *From: const username = undefined;*

- **Model can generate content for blank areas**
  - Model might be able to create what you prompt if you make area blank (pure white for backgrounds)
  - *From: Kijai*

- **Undervolting improves performance**
  - Gained 3 s/it undervolting 4090
  - *From: Doctor Shotgun*

- **Start/End frame introduces timing offsets**
  - Using Start/End with both ImageClips connected introduces 1 frame extra at beginning and 4 frames extra at end. Removing these in post creates near-seamless loops
  - *From: The Shadow (NYC)*

- **ClipVision is always 224x224 regardless of crop setting**
  - Crop setting only determines if image is cropped vs stretched, not the actual resolution processed
  - *From: Kijai*

- **Matteo's tiling method for ClipVision**
  - Technique to tile image and average the tiles for better vision processing, worked on some models but not others like SVD
  - *From: Kijai*

- **Average or sum options for dual image embeddings**
  - Average works without destroying results, sum seems to cause issues
  - *From: Kijai*

- **WAN requires nightly ComfyUI for Depth to work**
  - Depth workflows fail with standard ComfyUI version
  - *From: Kijai*

- **New image encode node doesn't have adjust_resolution**
  - Previous node automatically adjusted resolution, new one requires manual handling
  - *From: Kijai*

- **WAN resolution requirements divisible by 16**
  - vae_scale_factor_spatial being 8 and patch size[1] = 2 so 16
  - *From: Kijai*

- **Automatic resolution calculation formula**
  - max_area = 720 * 1280, calculates height/width based on aspect ratio and mod_value
  - *From: Kijai*

- **WAN primarily uses image encoded in latent space**
  - Cross attention is just added to prompt like ipadapter, main thing is still the image in latent space
  - *From: Kijai*

- **Tiled clip embed processing**
  - Can send any size, it tiles to specified number with ratio controlling full embed vs combined tiles
  - *From: Kijai*

- **WAN 2.1 tech report released**
  - Technical paper providing implementation details
  - *From: yi*

- **TeaCache patch required for SLG**
  - SLG patch needs TeaCache patch to pass certain parameters, even if TeaCache isn't actively used
  - *From: Kijai*

- **TeaCache with 0.25 threshold works well for faster generation**
  - Kijai using 25 steps with heavy TeaCache (skips 11 steps) for ~3 min generations, quality loss occurs above 0.2 threshold
  - *From: Kijai*

- **CLIP tiling may help reduce burning in videos**
  - Kijai testing clip tiling vs default, observing less burning on left (tiled) video
  - *From: Kijai*

- **Noise injection helps with motion**
  - The Shadow using 0.8 strength, notes noise injection helps with motion similar to iPA
  - *From: The Shadow (NYC)*

- **Model responds well to basic camera direction prompts**
  - Using prompts like 'camera orbit', 'static camera', 'camera tracks X' works surprisingly well
  - *From: The Shadow (NYC)*

- **Start and end frame as clip embeds can help with end frame accuracy**
  - Using both start and end frame as clip embeds helps model hit end frame closer
  - *From: Kijai*

- **DepthCrafter produces better results than DepthAnything for depth LoRA**
  - Depth map quality has fairly significant impact on output quality
  - *From: David Snow*

- **Higher step counts needed for differential diffusion**
  - Need high step counts (10, 20, 60 steps) to bring in enough of original video with diff diff
  - *From: David Snow*

- **Loop stitching improved for Wan video generation**
  - Implemented Mobius paper method for smoother looping, works with 1.3B model using loop_args
  - *From: Kijai*

- **Teacache makes outputs more creative**
  - Comparison shows teacache produces more creative results than no teacache
  - *From: VK (5080 128gb)*

- **Time lapse LoRA created for WanVideo**
  - Custom LoRA trained on three time-lapse painting process videos, works for 14B model with plans for i2v version
  - *From: 852話 (hakoniwa)*

- **CFG distillation can provide 50% speedup**
  - Using real CFG for a few steps then distilled CFG for the rest, only takes a few thousand training steps
  - *From: spacepxl*

- **Block pruning potential for 14B model**
  - Should be able to prune ~30% of blocks from 14B with little impact if flux is anything to go by
  - *From: spacepxl*

- **Blending source image with depth controlnet at 0.5 opacity produces more natural colors**
  - When using depth control, blending the original source image into the depth map at 0.5 creates better color results
  - *From: VK (5080 128gb)*

- **Anime lineart controlnet works without depth and defaults to anime style when it detects lines**
  - Pure anime lineart control input produces good results and the model automatically switches to anime style when it sees line art
  - *From: VK (5080 128gb)*

- **Face LoRA trained on 5-frame videos with identical last 4 frames enables controllable angle and emotion**
  - Training I2V LoRA on 5-frame sequences where frames 2-5 are identical creates controllable face generation for angles and emotions
  - *From: Juampab12*

- **SLG settings make a noticeable difference in output quality**
  - The SLG (extra CFG pass) settings posted earlier significantly improved generation results
  - *From: David Snow*

- **Loading workflow from yesterday's output fixed OOM errors when the exact same settings in autosave workflow failed**
  - Same workflow crashed from auto load but worked when loaded from output file
  - *From: Ghost*

- **Block swap memory showing 0MB on CUDA and 15410MB on host indicates RAM issues**
  - This pattern suggests insufficient available RAM causing problems
  - *From: arthuz*

- **Torch compile with RoPE function set to 'comfy' instead of 'default' enables full compilation and reduces VRAM usage significantly**
  - User went from needing 10-11 blocks swapped to fitting 81 frames in 28GB VRAM on 32GB card
  - *From: Shawneau/Kijai*

- **Prompt travel works by segmenting cross-attention and applying different prompts to different parts of video sequence**
  - Uses syntax like 'video of a person running|video of a person jumping' with no speed loss
  - *From: Kijai*

- **New batch join method for I2V splits images to different halves of video**
  - Allows different conditioning images for first and second half of generation
  - *From: Kijai*

- **Prompt strength can be adjusted with syntax modifications for full prompts**
  - Additional control over how strongly each prompt segment affects the output
  - *From: Kijai*

- **Using same start and end frame with character pose prompts creates very realistic 'photo comes to life' effect**
  - 50 steps, 720p, narrow use case but produces flawless results
  - *From: Shawneau*

- **CFG-Zero-star method implemented for Wan**
  - New node added that implements CFG-Zero-star technique with default settings from their demo. Provides subtle improvements to output quality, particularly noticeable in details like teeth and eyes
  - *From: Kijai*

- **Self attention split with multiple prompts works**
  - Using prompt syntax like 'video of person running|video of person sitting' with self attention split provides stronger separation between prompt conditions
  - *From: Kijai*

- **FP16 T5 encoder produces sharper results than BF16**
  - Using FP16 T5 text encoder instead of BF16 produces noticeably sharper output in native implementations
  - *From: The Shadow (NYC)*

- **14B LoRAs appear to work on 1.3B models**
  - Model accepts 14B LoRAs when used with 1.3B model but actually skips loading the incompatible weights
  - *From: Dream Making*

- **CFG Zero Star works with Wan and fixes many generation problems**
  - Fixes hands stabilization and various artifacts, can reduce steps needed (35 to 25 steps while looking better)
  - *From: Juampab12*

- **CFG Zero Star has zero init feature that multiplies early steps by zero**
  - Zero init literally makes the zero steps multiply by zero, completely different from skipping steps
  - *From: Kijai*

- **TeaCache default of 0.25 is too high for wrapper**
  - Causes artifacts, reducing to 0.2 improves quality
  - *From: Faust-SiN*

- **T5 should be used in bf16 or fp32, not fp16**
  - T5 produces NaNs in fp16 but works fine in fp32, bf16 is recommended according to documentation
  - *From: Kijai*

- **Short prompts work well for I2V**
  - Florence+manual prompt was same/worse than just manual prompt for I2V
  - *From: N0NSens*

- **SLG + lowering encoded video latents strength improves results**
  - Video latents strength to 0.85 allows denoise at 0.75 and still looks good
  - *From: A.I.Warper*

- **Wan 1.3B I2V model has 48 input channels instead of standard 36**
  - This is different from regular Wan models which use 16 for T2V + 20 for I2V
  - *From: Kijai*

- **Fun models work out of the box using existing VAE**
  - The InP model can be used without modification to the VAE setup
  - *From: H（4090）*

- **Fun models are temporal inpainting models that support both T2V and I2V**
  - They can handle start/end frame prediction and control signals
  - *From: Kijai*

- **Zero Star + enhance-a-video + SLG combination produces impressive temporal coherence**
  - Complex movement inference works very well with this setup
  - *From: Cseti*

- **TeaCache works with InP models but coefficients may not be optimal**
  - 0.010 is suggested as good starting point for InP 1.3B
  - *From: JmySff*

- **TeaCache coefficients need different settings for control models**
  - For 14B models with 'fun' or 'Fun' in name, TeaCache guesses between 480 or 720 coefficients
  - *From: Kijai*

- **Wan control models have built-in control without separate ControlNet**
  - The control models have built-in control capabilities and don't need external ControlNet
  - *From: Kijai*

- **Control model input structure is 16ch+16ch+16ch**
  - 16 channels for noise, 16 channels for reference image, 16 channels for condition
  - *From: mamad8*

- **Fun models use different masking method that fixes dark frame issue**
  - New masking method prevents darkening effect at end frames
  - *From: Kijai*

- **Training code available for reward LoRAs**
  - Repository includes training scripts for reward LoRA training
  - *From: Kijai*

- **Block swapping provides exact same results as VRAM**
  - Block swapping to fit models produces identical quality to running fully in VRAM, just takes longer
  - *From: aikitoria*

- **1.3B vs 14B InP models produce very similar quality**
  - Comparison shows both models generate comparable results for image2video
  - *From: Kijai*

- **Old 14B I2V model better than new InP models for regular I2V**
  - 14B old I2V is absolutely better than the 1.3B InP I2V, probably also better than the 14B InP one
  - *From: Kijai*

- **New Fun models struggle with complex concepts**
  - 1.3B fun model is devoid of some concepts that 14B implements, works better with generic content like 'girls in bikinis' but struggles with esoteric concepts
  - *From: miko*

- **Euler scheduler improved after bug fix**
  - After Kijai's latest changes fixing a mistake in euler code, euler is slightly better than unipc or at least comparable
  - *From: David Snow*

- **Control model is very strong and can be stopped after few steps**
  - The Fun Control model has very strong control influence and doesn't need to run for all steps
  - *From: Kijai*

- **Latent strength can be used as control strength**
  - The latent strength parameter in Fun Control model can control how much influence the control input has
  - *From: Kijai*

- **Trajectory control works and snaps after first frame**
  - The Fun Control model supports trajectory control input, but it only starts following the trajectory after the first frame
  - *From: Kijai*

- **Control model doesn't work well with end image**
  - When trying to use end frames with the control model, it either doesn't work or ruins the end by going white
  - *From: Kijai*

- **TeaCache uses different coefficients with e0 method**
  - Updated TeaCache implementation uses e0 instead of e with different coefficients for better performance
  - *From: Kijai*

- **Flow control works even when inverted**
  - Optical flow input works as control even when the flow direction is wrong/inverted
  - *From: Kijai*

- **Wan models work with extremely low step counts**
  - 1.3B control model can generate decent results with just 1 step, though quality improves with 2-4 steps
  - *From: Kijai*

- **14B model performs better than 1.3B at same step counts**
  - 4 step 14B model produces better results than 50 step 1.3B model
  - *From: VK (5080 128gb)*

- **Control strength differs significantly between models**
  - Control is very strong on 1.3B model, while image conditioning is stronger on 14B - needs completely different parameter ranges
  - *From: Kijai*

- **Exact resolution matching helps quality significantly**
  - Using exact resolution like 480x832 helped quality a ton
  - *From: A.I.Warper*

- **RGB input to control can be used effectively**
  - Feeding RGB images directly to control and reducing latent strength produces good results
  - *From: VK (5080 128gb)*

- **Flat color LoRA works on 14B model**
  - Flat anime LoRA is compatible with the 14B Fun control model
  - *From: DawnII*

- **Fun Control models integrate control into the model itself**
  - No separate LoRA needed - control functionality is built into the Fun Control models
  - *From: DawnII*

- **Tiled CLIP vision works well with Fun models in concat combine mode**
  - This is a working combination for the Fun models specifically
  - *From: Kijai*

- **Fun models were only released in bf16**
  - Should not use fp16 base precision if not using quantization
  - *From: Kijai*

- **Control latents need to be passed and split for tiled clip vision to work**
  - Had to pass and split the control latents too for it to work
  - *From: Kijai*

- **OptimalSteps technique claims 100 step quality at 20 steps**
  - From demo it seems much better than normal 20 steps
  - *From: YatharthSharma*

- **Stitching latents provides smoother decoding**
  - VAE can decode stitched latents smoother than combining individual clips
  - *From: Kijai*

- **DensePoste preprocessor works well with Wan Fun Control**
  - User was surprised to find densepose preprocessor worked really well
  - *From: Cubey*

- **Shuffle preprocessor works for experimentation**
  - Works for experimenting and getting crazy stuff
  - *From: IllumiReptilien*

- **Control embed end 0.25 works well**
  - Used with eye looking left and right prompt
  - *From: IllumiReptilien*

- **Resolution size causes flashing and color shifting**
  - Resolution size ended up being the culprit for flashing and color shifting
  - *From: Faux*

- **20 steps looks identical to 100 steps**
  - Comparison showing 20 vs 100 steps produces nearly identical results
  - *From: Juampab12*

- **Maximum 209 steps supported**
  - Kijai nodes supported maximum of 209 steps, anything above caused an error
  - *From: DiXiao*

- **Frame number must be multiple of 4+1**
  - Number of frames for Fun Control is a multiple of 4+1, so 5, 9, 13...
  - *From: Pedro (@LatentSpacer)*

- **8 tiles with concat improves control**
  - Try 8 tiles in clip encode node with combine set to 'concat'
  - *From: Kijai*

- **HiRes LoRA works well with 1.3B**
  - 1024x1024 generation works well with the HiRes LoRA on 1.3B model
  - *From: Kijai*

- **Aesthetics LoRA improves quality**
  - Aesthetics LoRA helps with 1.3B grain and quality
  - *From: DawnII*

- **Downscaling 14B model to 5B parameters can produce functional video models**
  - Modified diffusion-pipe repo to create 5B parameter model by dropping whole blocks and downscaling dimensions from 14B weights. At epoch 150, getting actual picture pieces instead of noise with persistent objects moving through space
  - *From: Kytra*

- **Sweet spot for 1.3B model performance is 41 frames**
  - Time increases disproportionately beyond 41 frames at 1280x768 resolution
  - *From: VK (5080 128gb)*

- **Loss plateauing at 0.36 indicates learning rate too high for from-scratch training**
  - When training from scratch, if lr is too high it will plateau early. Recommended to lower learning rate when loss plateaus, not raise it
  - *From: spacepxl*

- **Plot training loss with logarithmic x-axis for better trend analysis**
  - Makes it way easier to see real trends. Tensorboard can't do this which is annoying, but use spreadsheet if needed
  - *From: spacepxl*

- **Fun models have depth control embed built-in**
  - Control LoRAs are not compatible with Fun models and shouldn't be needed since depth control is already embedded
  - *From: Kytra*

- **Tiled encode causes strange/wrong motion in WAN despite looking seemingly correct**
  - Comparing tiled encode yes/no for sizes where both could run, tiled encode resulted in wrong motion more often, possibly due to incorrect math at tile edges
  - *From: aikitoria*

- **Fun InP model supports multiple start and end frames for video extension**
  - Can use 2-5 start/end frames, works better than single frame for extension. VAE encodes 4 images in one latent allowing 4 images as start
  - *From: Kijai*

- **Control signal is stronger on 1.3B than 14B model**
  - Control inputs look much better on 1.3B version compared to 14B with similar settings
  - *From: Kijai*

- **Wan is not autoregressive so Video-T1 tree of frame search doesn't apply**
  - Their approach for wan would be 'gen 8 videos and select best one' which is not the same benefit
  - *From: aikitoria*

- **Fun InP model now supports temporal masking with binary masks**
  - Can add temporal mask and full video as start_image, only binary masks work (no fade), mask is per 4 frames due to latent space
  - *From: Kijai*

- **Block swap reduces VRAM usage significantly**
  - 20 blocks needed for 16GB to be around 14.6GB VRAM usage
  - *From: VK (5080 128gb)*

- **Early DiT blocks affect composition and motion most in Wan**
  - Similar to Flux where early blocks affect composition and latter affect details, but motion is also affected early on in Wan
  - *From: Kijai*

- **Comfy RoPE function is lot cheaper with memory and faster**
  - Especially with torch.compile, now being considered as default
  - *From: Kijai*

- **TeaCache device fix**
  - TeaCache device didn't used to change from offload_device even if you selected main_device, now fixed
  - *From: Kijai*

- **VAE 2x2 identical frames trick works**
  - Using 2*2 identical frames per latent seems okay for similar frames
  - *From: mamad8*

- **Arcane LoRA works with InP model**
  - Added arcane lora to the InP model with strength 2.0 and it kept character and scene better
  - *From: Kijai*

- **Image resizing difference between native and wrapper**
  - Native uses bilinear resizing while wrapper uses lanczos when rescaling images
  - *From: Kijai*

- **Faded masks work with InP**
  - Successfully managed to make it work with faded masks
  - *From: PirateWolf*


## Troubleshooting & Solutions

- **Problem:** RMSNorm casting error with model management
  - **Solution:** Change compute type from fp16 back to default, or use T2V instead of I2V
  - *From: Doctor Shotgun*

- **Problem:** Torchaudio compatibility issues with latest PyTorch nightly
  - **Solution:** Don't include torchaudio in pip install command for latest nightly builds
  - *From: Kijai*

- **Problem:** VAE decode errors after sampling
  - **Solution:** Add VRAM unload node between sampler and VAE decode
  - *From: Miku*

- **Problem:** WanVideo Torch Compile Settings node causing errors
  - **Solution:** Disconnect/bypass the torch compile node if getting errors, workflow runs normally without it
  - *From: seitanism*

- **Problem:** Bad tiled VAE decode issues
  - **Solution:** Use tiled VAE decode and don't set tiling parameters too low
  - *From: Screeb*

- **Problem:** Text encoder not found
  - **Solution:** Put text encoder in clip folder and use Kijai's specific text encoder, not the Comfy one
  - *From: fearnworks*

- **Problem:** WanVideo Torch Compile Settings causing errors
  - **Solution:** Need Triton installed in environment, or use --fast 2 launcher flag with default compute_dtype
  - *From: VRGameDevGirl84/Miku*

- **Problem:** PyTorch nightly installation issues
  - **Solution:** Use command: pip install --pre -U torch torchvision --index-url https://download.pytorch.org/whl/nightly/cu128 (cannot include torchaudio)
  - *From: Kijai*

- **Problem:** Blocky artifacts appearing in generations
  - **Solution:** Usually caused by incompatible frame counts - stick to 81 frames or use context windowing
  - *From: Kijai*

- **Problem:** Flash-attn compatibility issues with nightly PyTorch
  - **Solution:** Uninstall flash-attn if causing import errors, it's barely used in ComfyUI
  - *From: Kijai*

- **Problem:** ComfyUI --fast optimization numbers causing crashes
  - **Solution:** Use --fast fp16_accumulation instead of --fast 2, command format changed
  - *From: Kijai*

- **Problem:** WanVideoBlockSwap missing required inputs
  - **Solution:** offload_txt_emb and offload_img_emb inputs required for blockswap node
  - *From: JohnDopamine*

- **Problem:** Torch compile cache error
  - **Solution:** Update PyTorch to 2.6.0, bug existed in older versions on Windows
  - *From: Kijai*

- **Problem:** Triton pointer error with CPU tensors
  - **Solution:** Restart ComfyUI or unload models, related to torch compile state
  - *From: Doctor Shotgun*

- **Problem:** V2V results looking worse than expected
  - **Solution:** Switch from dpm++ to unipc sampler, add enhance a video node
  - *From: David Snow*

- **Problem:** GGUF workflow not working with bf16 models
  - **Solution:** Use fp8 clip model instead of bf16, also avoid bf16 VAE
  - *From: Shawneau 🍁 [CA]*

- **Problem:** Florence 2 loading error with load_state_dict receiving none
  - **Solution:** Delete Florence models and let node download them fresh, or check transformers version compatibility
  - *From: JmySff*

- **Problem:** PyTorch nightly breaking custom nodes
  - **Solution:** Update bitsandbytes (bnb) to fix 'triton.ops' module error
  - *From: Cseti*

- **Problem:** Flash-attn conflicts after PyTorch upgrade
  - **Solution:** Uninstall flash-attn completely
  - *From: burgstall*

- **Problem:** Nouveau driver conflicts on Ubuntu
  - **Solution:** Use .run installer with proper blacklisting and DKMS
  - *From: fredbliss*

- **Problem:** numpy >= 2 breaks everything AI/ML
  - **Solution:** Downgrade numpy to version < 2
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Problem:** TeaCache causing noise and flickering artifacts
  - **Solution:** Use higher start_step value (like 12 instead of 6) and lower threshold (0.03 instead of 0.04) for 50 steps. Too aggressive threshold skips too many steps causing noise not to be removed fully
  - *From: Kijai*

- **Problem:** Color shifts occurring in generations
  - **Solution:** Use higher step counts - lower steps often give color shifts while higher step counts don't
  - *From: seitanism*

- **Problem:** Model file not updating properly
  - **Solution:** Use git pull in the folder instead of manager update, or manually check that \ComfyUI-WanVideoWrapper\wanvideo\modules\model.py file updated
  - *From: Kijai*

- **Problem:** Last frame instead of first frame doesn't work
  - **Solution:** Model isn't as flexible as cosmos img2vid for this use case - stick to first frame conditioning
  - *From: comfy*

- **Problem:** OOM errors when offloading to RAM
  - **Solution:** Try less blocks to offload and enable fp8 quantization on text encoder to free up ~4GB
  - *From: Kijai*

- **Problem:** 16GB RAM insufficient for block swapping
  - **Solution:** Increase block swap incrementally (from 22 to 28 blocks) to find balance
  - *From: Kijai*

- **Problem:** Computer freezes when switching to text encoder
  - **Solution:** Use bf16 text encoder model 'wan_t5_umt5-xxl-enc-bf16.pth' which uses 8GB VRAM instead of 40GB RAM
  - *From: Googol*

- **Problem:** fp8 text encoders not working with wrapper nodes
  - **Solution:** Use bf16 text encoder model instead, works reliably
  - *From: Googol*

- **Problem:** Latent upscale produces terrible results
  - **Solution:** Never use latent upscale, especially not with nearest sampling. Use image upscale instead
  - *From: Kijai*

- **Problem:** TeaCache error with high step counts
  - **Solution:** TeaCache works up to 209 steps, crashes with AssertionError above that
  - *From: DiXiao*

- **Problem:** fp8e4nv not supported on 3090
  - **Solution:** Use e5m2 quantization instead - torch.compile on 3000 series only works on e5m2
  - *From: Kijai*

- **Problem:** Token embedding weight error with wrong model
  - **Solution:** Use correct models from Kijai's repo: https://huggingface.co/Kijai/WanVideo_comfy/tree/main
  - *From: Kijai*

- **Problem:** TeaCache glitch at start of renderings
  - **Solution:** Try 81 frame count instead of 73
  - *From: Kijai*

- **Problem:** Extremely slow generation without optimizations
  - **Solution:** Enable sageattention and torch.compile - lots of inefficiency without them
  - *From: Kijai*

- **Problem:** 'list' object has no attribute 'to' error
  - **Solution:** Git pull latest wrapper changes - Kijai fixed this bug
  - *From: Kijai*

- **Problem:** Black outputs with Wrapper
  - **Solution:** Enable live preview to troubleshoot after 1 step, check torch version (recommend 2.6.0 minimum) and SageAttention compatibility
  - *From: Kijai*

- **Problem:** OOM error generating 81 frames at 720×1280
  - **Solution:** Enable block swap and set blocks to swap to 40 or higher, use fp8 on text encoder to reduce RAM use
  - *From: Kijai*

- **Problem:** RAM usage accumulates after several generations
  - **Solution:** Use Purge node in every decoder, though issue persists requiring ComfyUI restart
  - *From: N0NSens*

- **Problem:** Video combine node resets size when switching workflow tabs
  - **Solution:** Add --front-end-version Comfy-Org/ComfyUI_frontend@latest to .bat file to fix VHS-related ComfyUI bug
  - *From: N0NSens*

- **Problem:** torch.backends.cuda.matmul.allow_fp16_accumulation not available
  - **Solution:** Requires torch 2.7.0.dev20250226+cu128 or newer nightly build
  - *From: Kijai*

- **Problem:** TeaCache leaving noise behind
  - **Solution:** Adjust threshold - too aggressive threshold skips too many steps and doesn't fully remove noise. Start step affects threshold
  - *From: Kijai*

- **Problem:** T2V broken after latest wrapper commit
  - **Solution:** Use previous commit bd31044ef574b7872386fa6228461b15465079ae or wait for fix
  - *From: DiXiao*

- **Problem:** TypeError: expected Tensor as element 1 in argument 0, but got NoneType
  - **Solution:** Latest wrapper commit broke t2v functionality, use previous version
  - *From: TK_999*

- **Problem:** No preview images showing in wrapper
  - **Solution:** Previews only work with native ksamplers, not wrapper nodes
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Problem:** 1.3B FP32 model performing same as FP16
  - **Solution:** Use wavespeed model loader with weight_dtype Float32, but takes 4x longer for same results
  - *From: N0NSens*

- **Problem:** Black output with NaN values
  - **Solution:** Check for corrupted model files, redownload to different drive if needed
  - *From: Fawks*

- **Problem:** Teacache causing no motion in videos
  - **Solution:** Use start_percent parameter (0.20 works well) to prevent skipping critical early steps
  - *From: JmySff*

- **Problem:** T2V broken in native implementation
  - **Solution:** Commit 8e0a90f broke t2v, use earlier commit or wrapper version
  - *From: chancelor*

- **Problem:** CUDA 12.4 torch causing black outputs
  - **Solution:** Update to torch cu126: pip install -U torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu126
  - *From: Kijai*

- **Problem:** Teacache crashes with shape mismatch
  - **Solution:** Issue occurs with batches and sequential CFG, avoid CFG scheduling when using teacache
  - *From: Screeb*

- **Problem:** 32GB RAM insufficient for I2V 14B model
  - **Solution:** Need at least 64GB RAM, or increase swap file on Linux as temporary workaround
  - *From: Question*

- **Problem:** AttributeError: 'VAE' object has no attribute 'vae_dtype'
  - **Solution:** Use the native ComfyUI VAE loader with wan_2.1_vae.safetensors instead of wrapper VAE
  - *From: Miku*

- **Problem:** TeaCache node showing red/not working
  - **Solution:** Need to use TeaCache from Kijai's github repo, uninstall original TeaCache first
  - *From: Miku*

- **Problem:** PyTorch version not new enough for fp16 accumulation
  - **Solution:** Uninstall torchaudio and run nightly update command with only torch and torchvision
  - *From: Miku*

- **Problem:** Input image different dimensions to latent size
  - **Solution:** Ensure input image dimensions match the latent size requirements
  - *From: GalaxyTimeMachine*

- **Problem:** Workflow freezing at beginning of sampling
  - **Solution:** Increase blocks to swap or use new vram_management node, don't mix weights and choose matching dtype
  - *From: Kijai*

- **Problem:** TypeError: expected Tensor as element 1 in argument 0, but got NoneType
  - **Solution:** Fixed with recent git pull/updates to the repository
  - *From: burgstall*

- **Problem:** Can't find Wan in TeaCache node selection
  - **Solution:** Must refresh browser after installing TeaCache updates, even after restarting ComfyUI
  - *From: Kijai*

- **Problem:** KeyError: 'token_embedding.weight'
  - **Solution:** Use the correct T5 model from Kijai's repo: umt5-xxl-enc-bf16.safetensors
  - *From: Juampab12*

- **Problem:** TeaCache node naming conflict with wrapper node
  - **Solution:** Update KJNodes to fix class name change, need to re-add node if already using
  - *From: Kijai*

- **Problem:** Pointer argument cannot be accessed from Triton error
  - **Solution:** Change offload setting to 'main_device' instead of 'offload'
  - *From: GalaxyTimeMachine*

- **Problem:** Boolean value of Tensor error with dm++_sde sampler
  - **Solution:** Use non-SDE sampler like UniPC, TeaCache doesn't work with SDE anyway
  - *From: Kijai*

- **Problem:** Block swap causing OWM
  - **Solution:** Use vram_management instead of block_swap if it's more effective for your system
  - *From: Aube*

- **Problem:** Browser not showing updated nodes
  - **Solution:** Try different browser, refresh multiple times, or clear cache - usually browser caching issue
  - *From: Kijai*

- **Problem:** OOM with bf16 weights on i2v 4090
  - **Solution:** Use fp8 weights instead or increase block swap to 40+
  - *From: Juampab12*

- **Problem:** TeaCache node connection issues
  - **Solution:** Connect by double-clicking in empty space and typing node name
  - *From: Kijai*

- **Problem:** 'OptimizedModule' object has no attribute 'forward_orig' with native teacache
  - **Solution:** Use Kijai's torch compile node instead of normal torch compile
  - *From: Kijai*

- **Problem:** Face changes significantly with teacache in i2v
  - **Solution:** Reduce threshold value or adjust start percentage
  - *From: Kijai*

- **Problem:** Poor face quality in i2v results
  - **Solution:** Use more steps (15 may not be enough), try 20+ steps
  - *From: Draken*

- **Problem:** Tensor size mismatch error (58 vs 60) in I2V workflow
  - **Solution:** Disable adjust_resolution on the clip encode node to maintain exact dimensions for I2V embeds
  - *From: Kijai*

- **Problem:** TeaCache causing reduced motion and artifacts
  - **Solution:** Apply TeaCache to fewer steps (like 0.5-1.0 range) or start it later in the process
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Problem:** Consistent character appearing in every video during frame interpolation
  - **Solution:** Math error in VAE pixel:latent ratio calculation was set to 16:1 compression instead of correct ratio
  - *From: fredbliss*

- **Problem:** SageAttention node errors despite proper installation
  - **Solution:** Visual Studio and CUDA toolkit version conflicts can cause issues - needs specific compatible versions
  - *From: Kijai*

- **Problem:** SageAttention import error with 'sageattn_qk_int8_pv_fp16_cuda'
  - **Solution:** Issue appears to be with SageAttention installation or compatibility with the specific environment setup
  - *From: Teslanaut*

- **Problem:** Color shift/darkening towards end of generations
  - **Solution:** Multiple users reporting this issue, appears to be a model behavior rather than local setup problem
  - *From: Bleedy (Madham)*

- **Problem:** Triton not installing properly in virtual environment
  - **Solution:** Use 'uv pip install' commands instead of regular pip, check virtual environment activation with 'where pip'
  - *From: TK_999*

- **Problem:** Memory not clearing between runs causing extreme generation times
  - **Solution:** Need to add cache and model clearing nodes after compilation to prevent memory buildup
  - *From: AJO*

- **Problem:** Context windowing not splitting prompts evenly
  - **Solution:** Math for splitting prompts across context windows is complex, requires careful calculation of stride and overlap
  - *From: TK_999*

- **Problem:** TeaCache with default settings kills all motion
  - **Solution:** Need to start TeaCache later in the process, probably need different coefficients for I2V
  - *From: Kijai*

- **Problem:** LoRA keys not loading with SD1.5 LoRAs
  - **Solution:** 
  - *From: burgstall*

- **Problem:** RAM memory not clearing after runs
  - **Solution:** 
  - *From: AJO*

- **Problem:** Compile node error on Windows
  - **Solution:** 
  - *From: Kijai*

- **Problem:** Note node broken after ComfyUI update
  - **Solution:** 
  - *From: David Snow*

- **Problem:** Resolution mismatch in I2V with wrapper
  - **Solution:** 
  - *From: N0NSens*

- **Problem:** TeaCache causing artifacts and leftover noise
  - **Solution:** Check start_percent threshold - if too low it causes artifacts, if threshold is too high it can also cause issues. Certain steps when skipped will always result in noise being left behind
  - *From: JmySff*

- **Problem:** Native Wan slower than wrapper
  - **Solution:** Use Sage attention and Triton for best performance boost, also pytorch nightly fp16 boost available
  - *From: Kijai*

- **Problem:** Custom node not being recognized
  - **Solution:** Check startup log for import errors like 'module not found' to identify the actual error
  - *From: Kijai*

- **Problem:** Ultimate SD upscale slow and flickering
  - **Solution:** Modify processing.py defaults from 512 to 256 to reduce VRAM usage, though still has tile borders and quality issues
  - *From: David Snow*

- **Problem:** FPS interpolation not working despite settings
  - **Solution:** Set output_fps higher than generation_fps in FPS Config node. Example: generation_fps=2.0, output_fps=24.0 gives interpolation_factor=12
  - *From: fredbliss*

- **Problem:** TorchCompile error on 3090 with fp8_e4m3fn
  - **Solution:** fp8_e4m3fn compilation doesn't work on 3090, use fp8_e5m2 instead
  - *From: Kijai*

- **Problem:** Flash/jump at beginning of looped videos
  - **Solution:** Decode frames twice - first at beginning, then again after end, using second set of decoded frames. Also blend first 9 frames with repeated decode
  - *From: Benjaminimal*

- **Problem:** Context_frames slider limited to 80 in FPS config
  - **Solution:** Use constant int node to set context back to 81, slider step size prevents manual entry
  - *From: TK_999*

- **Problem:** Windows cache file bug with TorchCompile
  - **Solution:** Update to torch version 2.6.0 to fix the issue
  - *From: Kijai*

- **Problem:** Green noise and garbled video output
  - **Solution:** Issue is caused by VAE temporal awareness creating frame offset. Single frame generation works correctly
  - *From: fredbliss*

- **Problem:** Jittering in interpolated videos
  - **Solution:** Context window logic duplicates missing frames to closest windows - need to account for interpolated frames differently
  - *From: fredbliss*

- **Problem:** Triton error appearing intermittently
  - **Solution:** Switch TorchCompile from inductor to cudagraph, or reduce frame count to manage VRAM usage
  - *From: Neex*

- **Problem:** RuntimeError: Boolean value of Tensor with more than one value is ambiguous
  - **Solution:** Issue occurs when using context options on latest wrapper version
  - *From: Cubey*

- **Problem:** OOM errors on 720p with wrapper
  - **Solution:** Native workflow with GGUF8 model works while wrapper fails. RAM usage stays at 90-100% with wrapper vs 40% with native
  - *From: AJO*

- **Problem:** Slow motion output with low step counts
  - **Solution:** Add 'slow motion' to negative prompt in English and Mandarin, or use motion-related words like 'moves swiftly' or mention motion blur
  - *From: Juampab12*

- **Problem:** Yellow tinting in i2v after 15 frames
  - **Solution:** Increase noise_aug_strength to 0.01, 0.02, or 0.03 (higher values may lower quality)
  - *From: Juampab12*

- **Problem:** Load image node missing load image button after frontend update
  - **Solution:** Update frontend package: pip install --upgrade comfyui-frontend-package
  - *From: Juampab12*

- **Problem:** Note node still broken
  - **Solution:** Update frontend package with: pip install --upgrade comfyui-frontend-package or for portable: python.exe -m pip install --upgrade comfyui-frontend-package
  - *From: Kijai*

- **Problem:** CFG 1.0 doesn't work due to ComfyUI rounding
  - **Solution:** ComfyUI rounds CFG values, can't set exactly 1.0
  - *From: Kijai*

- **Problem:** RAM usage growing to 98% during multi-scene workflows
  - **Solution:** Use GGUF models to help reduce RAM usage, though complete solution still needed
  - *From: N0NSens*

- **Problem:** TeaCache not working after update
  - **Solution:** Set threshold to 0.3 (30%) instead of the old 0.03 value with new coefficients
  - *From: Juampab12*

- **Problem:** I2V color discoloration at 2.5 seconds
  - **Solution:** This is a known issue with how i2v works where the middle has a big shift, some videos recover original color
  - *From: Benjaminimal*

- **Problem:** Get Image Size & Count node broken
  - **Solution:** Node broke with update, couldn't see any errors anywhere so no idea why
  - *From: Kijai*

- **Problem:** Starting flash in videos when not looping
  - **Solution:** Doing the loop-fix VAE hack when not looping actually makes it significantly worse because VAE has memory of previous frames
  - *From: Benjaminimal*

- **Problem:** Black screen with sage attention
  - **Solution:** Change precision setting from auto to fp16 and try fp8_e5m2 instead of fp8_e4m3fn
  - *From: Cubey*

- **Problem:** mat1 and mat2 shapes cannot be multiplied error
  - **Solution:** Using wrong text encoder - wrapper and native use different text encoder files
  - *From: TK_999*

- **Problem:** Sage attention not working with Wan on all GPUs
  - **Solution:** Need to select specific sageattn 2.0 mode, doesn't work with Wan currently on all GPUs
  - *From: Kijai*

- **Problem:** Wrapper being 3x slower than native
  - **Solution:** Increase block swap to 25 or more, probably OOMing. Use fp16_fast in wrapper if set up for fp16_accumulation
  - *From: Juampab12*

- **Problem:** A6000 showing CUDA usage in 3d panel instead of compute
  - **Solution:** Check that python libs were installed with cuda support into comfyui's python venv
  - *From: jellybean5361*

- **Problem:** Sage attention fp8 cuda failing on I2V
  - **Solution:** Edit sageattention code to always use fp16_triton version or use --attn_impl sage_attn_fp16 flag
  - *From: intervitens*

- **Problem:** Parallel script execution fails with port conflict
  - **Solution:** Use --master_port=29501 to avoid port 29500 conflict
  - *From: aikitoria*

- **Problem:** WSL2 VAE decode failures
  - **Solution:** Configure WSL2 for 48GB RAM minimum - over 32GB is committed during processing
  - *From: jellybean5361*

- **Problem:** SageAttention 2.0 won't compile
  - **Solution:** Install ninja into the ComfyUI venv before attempting compilation
  - *From: jellybean5361*

- **Problem:** WSL extremely slow model loading from Windows drives
  - **Solution:** Copy models to Linux filesystem instead of accessing via /mnt
  - *From: CrypticWit*

- **Problem:** Black outputs suddenly appearing in generations
  - **Solution:** Restart ComfyUI - seems to be a temporary state issue
  - *From: seitanism*

- **Problem:** Sage attention and torch compile errors on Linux
  - **Solution:** Install sageattention 2.1.0 (not 1.0.6) and flash_attn, use fp16 and auto settings
  - *From: Cubey*

- **Problem:** TeaCache not working with new coefficients
  - **Solution:** New coefficients are more aggressive, can start from zero but too aggressive values hit early and destroy motion
  - *From: Kijai*

- **Problem:** RuntimeError: mat1 and mat2 shapes cannot be multiplied (154x768 and 4096x5120)
  - **Solution:** Use correct text encoder - the cloud service only had wrapper version, needed to load proper text encoder
  - *From: AJO*

- **Problem:** Text encoders not loading properly
  - **Solution:** Put text_encoders in clip folder rather than text_encoders folder for some setups
  - *From: Dream Making*

- **Problem:** Interpolating before upscaling causes OOM and wastes time
  - **Solution:** Upscale first, then interpolate - it's much faster, uses lower VRAM, and gives same result
  - *From: Juampab12*

- **Problem:** TeaCache stopped working
  - **Solution:** Update TeaCache threshold value to 0.3, old workflows have outdated values
  - *From: Kijai*

- **Problem:** LoRAs not working with native + compile
  - **Solution:** Use patch model patch order node before LoRA loading
  - *From: Kijai*

- **Problem:** VRAM management node causes CppCompilError with torch compile
  - **Solution:** Cannot use torch compile with VRAM management node together
  - *From: Kijai*

- **Problem:** Person keeps walking away in poses
  - **Solution:** Use higher CFG (8 vs 6), add 'the camera is static' to prompts, give specific pose guidance rather than vague 'poses'
  - *From: Shawneau 🍁 [CA]*

- **Problem:** TypeError: teacache_hunyuanvideo_forward() got unexpected keyword argument 'clip_fea'
  - **Solution:** Update torch, sage, flash and triton - torch 2.6.0, sage 2.11, flash 2.7.4, triton 3.20
  - *From: HeadOfOliver*

- **Problem:** Patch order + loras + torch compile = OOM
  - **Solution:** Remove patch order node or torch compile to use loras
  - *From: Doctor Shotgun*

- **Problem:** LoRAs don't work with torch compile in native
  - **Solution:** Use GGUF model with torch compile or disable compile
  - *From: zoz*

- **Problem:** Can't do 1280x720 on 4090 with Kijai wrapper
  - **Solution:** Native has better VRAM management, can do 1280x720 on native
  - *From: zoz*

- **Problem:** Getting weird stuff with lower test
  - **Solution:** Don't change context stride, leave at 4
  - *From: Organoids*

- **Problem:** RIFE causing OOM with multiple generations
  - **Solution:** Use RIFE outside ComfyUI or use Topaz for interpolation
  - *From: burgstall*

- **Problem:** VAE compression done wrong for keyframes in LTX
  - **Solution:** Change comfy code in comfy/comfy_extras_model_lt.pt, modify LTXVAddGuide class
  - *From: Juampab12*

- **Problem:** Triton error when approaching VRAM limit
  - **Solution:** Install Triton or use block swapping
  - *From: Neex*

- **Problem:** 2 hour render times with block swapping
  - **Solution:** Install sageattention, triton, and torch optimizations for better performance
  - *From: Colin*

- **Problem:** I2V persistently generates slow-mo videos
  - **Solution:** No solution provided, seeking help
  - *From: N0NSens*

- **Problem:** 720p model won't fit in VRAM on 4090
  - **Solution:** Enable block swapping or install optimization packages
  - *From: Neex*

- **Problem:** VAE tiling needed for 1920x1080 decoding on 24GB
  - **Solution:** Use VAE tiling with 512px spatial tiling and 128px overlap for higher resolution decoding
  - *From: aikitoria*

- **Problem:** OOM errors after first generation requiring ComfyUI restart
  - **Solution:** Issue occurs on text encoder node despite clean VRAM nodes being used
  - *From: VRGameDevGirl84(RTX 5090)*

- **Problem:** Wan not running on 5090 servers
  - **Solution:** Need nightly everything but newest sometimes breaks everything, may need CUDA 12.8 base image and torch nightly
  - *From: aikitoria*

- **Problem:** Block swapping running out of RAM
  - **Solution:** Need 256GB normal RAM (not VRAM) when using block swapping due to weight offloading
  - *From: Benjimon*

- **Problem:** LatentSync installation issues
  - **Solution:** Install dependencies manually including lighting, uses older numpy version, doesn't work with PyTorch 2.7, use 2.6 instead
  - *From: VRGameDevGirl84(RTX 5090)*

- **Problem:** Torch compile giving errors with wrapper
  - **Solution:** Clear triton cache (Snow\.triton\cache) and enable 'compile transformer block' option
  - *From: Kijai*

- **Problem:** Getting pure noise output
  - **Solution:** Check workflow connections and settings, particularly enhance a video node placement
  - *From: Cubey*

- **Problem:** 14B model stuck at 0%
  - **Solution:** Add block swap to get generation unstuck
  - *From: VRGameDevGirl84(RTX 5090)*

- **Problem:** Poor quality output with 14B model
  - **Solution:** Avoid 480x480 resolution, use proper aspect ratios and check if block swap is maxed out
  - *From: VRGameDevGirl84(RTX 5090)*

- **Problem:** GPU crashes at end of generation during VAE decode
  - **Solution:** Disable TeaCache and Enhance-a-Video
  - *From: TK_999*

- **Problem:** Wan gets stuck at first step for long time
  - **Solution:** Disable TeaCache, use proper block swapping configuration
  - *From: seitanism*

- **Problem:** High GPU memory temperatures (100°C)
  - **Solution:** Set power limits, configure case fans to GPU temperature instead of CPU
  - *From: seitanism*

- **Problem:** FP8 Sage causes NaN overflow in I2V resulting in black images
  - **Solution:** Use FP16 Sage for I2V, FP8 works fine for T2V
  - *From: Doctor Shotgun*

- **Problem:** Non-tiled VAE decode causes glitches and VRAM issues on AMD/Zluda
  - **Solution:** Use tiled VAE decode on AMD systems
  - *From: Screeb*

- **Problem:** Black video generation output
  - **Solution:** Don't use sageattn_qk_int8_pv_fp8_cuda for wan i2v, or adjust RAM timings/FCLK/SOC voltage
  - *From: Doctor Shotgun*

- **Problem:** CUDA out of memory error
  - **Solution:** It's actually a RAM error - use VRAM management node instead of block swap, close browsers/applications, set text encoder to fp8
  - *From: Kijai*

- **Problem:** Can't use block_swap_args and vram_management_args simultaneously
  - **Solution:** Remove block swap to use VRAM management node
  - *From: BestWind*

- **Problem:** numba package initialization failure
  - **Solution:** SystemError indicates JIT compilation issue with numba dependency
  - *From: Doctor Shotgun*

- **Problem:** Kijai nodes breaking after triton installer
  - **Solution:** Fresh ComfyUI install required after using one-click triton installer
  - *From: David Snow*

- **Problem:** torch.backends.cuda.matmul.allow_fp16_accumulation not available
  - **Solution:** Requires torch 2.7.0.dev2025 02 26 nightly minimum
  - *From: Ashtar*

- **Problem:** SageAttention DLL load failed error
  - **Solution:** Reinstall SageAttention to match current PyTorch version, use sageattention-2.0.0-cp312-cp312-win_amd64.whl for Windows
  - *From: Kijai*

- **Problem:** Triton compatibility issues on Windows
  - **Solution:** Use `pip install triton-windows` for Windows Triton support
  - *From: Kijai*

- **Problem:** Blurry/smeared T2V outputs
  - **Solution:** Update TeaCache node - old version with 0.1 value causes blur, newer version supports higher values
  - *From: Kijai*

- **Problem:** Python.h missing error
  - **Solution:** Reinstall Visual Studio and redo system variables
  - *From: David Snow*

- **Problem:** Context windows don't work well for I2V
  - **Solution:** Use black image on all but first window, or decode VAE mid-process to use intermediate results
  - *From: Kijai*

- **Problem:** OOM on finish after new changes
  - **Solution:** Issue was accidentally removing --dit_fsdp_offload flag
  - *From: aikitoria*

- **Problem:** RuntimeError: expected input to have 32 channels, but got 16 channels
  - **Solution:** Use torch.tensor([1536, 32, 1, 2, 2]) for reshape_weight
  - *From: comfy*

- **Problem:** Control LoRA not working with compile
  - **Solution:** Disable compile - compile was identified as the culprit
  - *From: TK_999*

- **Problem:** Native control LoRA loading but not sampling correctly
  - **Solution:** Need ComfyUI commit ca8efab79fa19bc9745b4f7346d38a49ba1b1b7c or later
  - *From: spacepxl*

- **Problem:** Keys not loaded warning when using wrong LoRA version
  - **Solution:** Use v0.2 LoRA file and ensure ComfyUI is updated
  - *From: spacepxl*

- **Problem:** Color flickering near end of video at low denoise (0.2-0.3)
  - **Solution:** Issue identified but no solution provided yet
  - *From: N0NSens*

- **Problem:** Speckles/unresolved noise in video output
  - **Solution:** Use 81 frames or less, or enable context options for longer videos
  - *From: VRGameDevGirl84(RTX 5090)*

- **Problem:** OOM when using torch compile + LoRA in native workflow
  - **Solution:** Use patch order node, but this prevents compile from working properly. Either use compile without LoRA or LoRA without compile
  - *From: zoz*

- **Problem:** Block swap inefficient for 32GB RAM systems
  - **Solution:** Consider adding option to disable non-blocking mode (would be slower but use less RAM)
  - *From: Kijai*

- **Problem:** 1280x720x81 not working with 32GB RAM
  - **Solution:** Use fp8 model, torch nightly, fp16fast, and block swap at 25
  - *From: zoz*

- **Problem:** GPU thermal throttling at 85°C
  - **Solution:** Use MSI Afterburner to set power limits and undervolt, dropped temps to 72°C
  - *From: B1naryV1k1ng*

- **Problem:** Shift parameter not working in I2V native workflow
  - **Solution:** Bug was fixed more than a month ago, check workflow connections
  - *From: HeadOfOliver*

- **Problem:** Power limit causing 1GHz clock reduction
  - **Solution:** That's literally what power limit does - prefer undervolting instead
  - *From: Kijai*

- **Problem:** Torch compile + LoRA + Patch Model Order causes OOM
  - **Solution:** Use --reserve-vram 3 or 4 flag when starting ComfyUI
  - *From: Kijai*

- **Problem:** Control Embeds bug after first generation
  - **Solution:** Turn off torch compile or use native instead of wrapper for better control
  - *From: TK_999*

- **Problem:** Triton Windows installation still requires Visual Basic compiler
  - **Solution:** Still need to install Visual Basic tools and dependencies despite new pip install triton-windows
  - *From: Neex*

- **Problem:** GPU not using 100% utilization hovering at 90%
  - **Solution:** Check with GPU-Z and HWInfo64 which report 100% while Task Manager shows 89-96%
  - *From: seitanism*

- **Problem:** ComfyUI clone failing with HTTP/2 stream error
  - **Solution:** Network connectivity issue, retry cloning
  - *From: CJ*

- **Problem:** OOM with torch compile + LoRA
  - **Solution:** Update KJNodes and set full_load to disabled in model weight patch
  - *From: Kijai*

- **Problem:** LoRA not loading on native implementation
  - **Solution:** Use proper model patcher node right after model loader
  - *From: TK_999*

- **Problem:** CFG distillation LoRA showing shape mismatch errors
  - **Solution:** 1.3B distillation LoRA only works with 1.3B models, not 14B models
  - *From: Kijai*

- **Problem:** RGBA image error with upscaler
  - **Solution:** Convert RGBA to RGB using Images to RGB node before upscaling
  - *From: Kijai*

- **Problem:** Context windows causing image drift in I2V
  - **Solution:** Using overlap of 24 frames can help reduce reset between windows for static content
  - *From: Cubey*

- **Problem:** I2V crash with rope function optimization
  - **Solution:** Kijai fixed the issue - it was related to tensor dimension mismatch in I2V processing
  - *From: Kijai*

- **Problem:** Batch CFG doesn't work for I2V
  - **Solution:** Error with tensor size mismatch - issue reported to Kijai for fixing
  - *From: Juampab12*

- **Problem:** LoRA loading causes VRAM issues
  - **Solution:** Kijai added low_mem_load option - slower to load (16 seconds vs 6 seconds) but uses less VRAM
  - *From: Kijai*

- **Problem:** ControlNet LoRA error with rank
  - **Solution:** Set the rank to 16 when loading, and ensure using the patch node with torch compile
  - *From: Benjaminimal*

- **Problem:** TeaCache not firing with very low threshold
  - **Solution:** Threshold of 0.035 is too low, should use around 0.2 for proper TeaCache function
  - *From: Kijai*

- **Problem:** LoRA key format compatibility
  - **Solution:** Fixed LoRA key format by adding 'diffusion_model.' prefix and removing '.default' suffix
  - *From: Benjaminimal*

- **Problem:** Windows memory allocation causing crashes
  - **Solution:** Issue appears to be Windows-specific memory management problem, works better on Linux with same hardware
  - *From: Kijai*

- **Problem:** Torch Compile issues with LoRA in native and patch order in wrapper
  - **Solution:** Update wrapper and use 'disabled' option for full_load if having memory issues
  - *From: Kijai*

- **Problem:** ComfyUI performance degradation from 14 min to 40 min on same workflow
  - **Solution:** Issue persisted even after reverting, nuking venv, and reverting custom nodes - unresolved
  - *From: HeadOfOliver*

- **Problem:** Loading two different LoRAs crashes due to simultaneous loading
  - **Solution:** Use native implementation or ensure enough RAM (128GB) to hold two models, or use block_swap=40
  - *From: burgstall*

- **Problem:** LoRA error 'shape is invalid for input'
  - **Solution:** Need LoRA with '-comfy' in filename, ensure ComfyUI is updated, check LoRA node has 1.0 version selected
  - *From: spacepxl*

- **Problem:** Dotted texture artifacts in native vs wrapper comparison
  - **Solution:** Appears to be sampler/scheduler differences, possibly UniPC implementation variations
  - *From: Kijai*

- **Problem:** Error when using spacepxl control workflow
  - **Solution:** Update ComfyUI to at least commit ca8efab79fa19bc9745b4f7346d38a49ba1b1b7c
  - *From: spacepxl*

- **Problem:** UniPC solver bug at steps < 50
  - **Solution:** Kijai fixed the bug in fm solvers
  - *From: Kijai*

- **Problem:** Triton error on specific GPU
  - **Solution:** Use fp8_e5m2 weight for compile on that GPU type
  - *From: Kijai*

- **Problem:** Control lora bugs out after 3rd generation when tweaking end% and denoise
  - **Solution:** May be related to wrapper not unloading lora correctly, especially on cancel operations
  - *From: N0NSens*

- **Problem:** Video combine node shows low quality preview despite large screen area
  - **Solution:** Issue acknowledged by developer, still investigating
  - *From: TK_999*

- **Problem:** Control lora not working in native ComfyUI
  - **Solution:** Need latest git version of ComfyUI, not stable release. Code change supporting wan control hasn't made it to stable yet
  - *From: spacepxl*

- **Problem:** Artifacts on power lines when using tile control for upscale
  - **Solution:** Add more blur to input (12px and 0.3 sigma starting point), avoid using no blur on original
  - *From: spacepxl*

- **Problem:** Extremely noisy outputs with TeaCache and SkipLayer
  - **Solution:** Update TeaCache node to work with SkipLayerGuidanceDiT - was code conflict issue
  - *From: Kijai*

- **Problem:** Spline editor not working, 'points to store' empty
  - **Solution:** Click on the 'new canvas' button first before using the spline editor
  - *From: Kijai*

- **Problem:** Model moving to CPU unexpectedly
  - **Solution:** This always happened, just added log entry to show it - not a malfunction
  - *From: Kijai*

- **Problem:** Sudden slowdown in workflows
  - **Solution:** Using monitor/RDP vs direct computer access affects performance due to VRAM threshold issues
  - *From: burgstall*

- **Problem:** H265 videos not playing on desktop app
  - **Solution:** Use H264 format instead - H265 support issues on Windows/desktop app
  - *From: ramonguthrie*

- **Problem:** OOM on RTX 3060
  - **Solution:** Use --lowvram flag to aggressively offload models after use
  - *From: CapsAdmin*

- **Problem:** TeaCache node error after ComfyUI updates
  - **Solution:** Update both ComfyUI and KJNodes through manager or manually with git pull
  - *From: Kijai*

- **Problem:** is_looped variable error
  - **Solution:** Add ', is_looped=False' to line 1255 in ComfyUI-WanVideoWrapper/nodes.py or revert to previous commit
  - *From: kendrick*

- **Problem:** VAE burning/artifacts at start of generation
  - **Solution:** Use VAE warmup trick to fix burning issue
  - *From: Kijai*

- **Problem:** Black screen when compiling VAE
  - **Solution:** Issue with torch compile on VAE, avoid compiling VAE
  - *From: yo9o*

- **Problem:** CUDA error with block swap
  - **Solution:** Use VRAM management node instead of block swap
  - *From: Colin*

- **Problem:** Rife-Tensorrt not working
  - **Solution:** Change line 49 logic to 'if (not hasattr(self, 'engine') or not hasattr(self, 'engine_label') or self.engine_label != engine):'
  - *From: burgstall*

- **Problem:** FloweEdit fails with single frame
  - **Solution:** Kijai fixed an AssertionError that occurred when trying to FloweEdit only one frame
  - *From: mamad8/Kijai*

- **Problem:** Color shift/darkening between I2V generations
  - **Solution:** No clear solution found, appears to be related to input image style. Color match node doesn't help
  - *From: seitanism*

- **Problem:** Inconsistent generation results with same seed
  - **Solution:** Some optimization nodes may have hidden randomness, particularly enhance-a-video
  - *From: seitanism*

- **Problem:** Can't use 14B fp16 models with wrapper due to VRAM
  - **Solution:** Even with 40 block swap it doesn't help, appears to be unresolved
  - *From: JmySff*

- **Problem:** RIFE-TensorRT not working
  - **Solution:** burgstall had to modify init.py with Claude's help to get it working again
  - *From: burgstall*

- **Problem:** TeaCache node causing 'Input type (torch.cuda.FloatTensor) and weight type (torch.FloatTensor) should be the same' error
  - **Solution:** Issue was with torch compile compatibility. Running workflow with TeaCache off but torch compile on, then re-enabling both fixed it. Torch compile is flaky and reloading model can help
  - *From: CJ*

- **Problem:** Triton installation failing on Windows with portable ComfyUI
  - **Solution:** Need to copy python libs to portable installation as per triton-windows readme section 8
  - *From: Kijai*

- **Problem:** SLG causing slow-motion effect in videos
  - **Solution:** Try different CFG values (grid search 0-10 in 0.5 increments). Too much total guidance strength can cause issues. Also try SLG start at 0.3 instead of 0.1 for less destructive effect
  - *From: deleted_user_2ca1923442ba*

- **Problem:** LoRA crashes with I2V GGUF models
  - **Solution:** Try fewer frames or lower resolution as LoRAs take slightly more memory
  - *From: Screeb*

- **Problem:** Dimension not divisible by 16 error
  - **Solution:** Ensure image dimensions are divisible by 16
  - *From: Kijai*

- **Problem:** Node order matters with patches and compile
  - **Solution:** Compile should be applied last after all patches to avoid conflicts
  - *From: Kijai*

- **Problem:** Using fp8 weights with fp16 compute wastes performance
  - **Solution:** Either get fp16 model weights or enable fp8 quantization - don't upcast fp8 to fp16
  - *From: Kijai*

- **Problem:** Adding enhance node after compile breaks compilation
  - **Solution:** Have the enhance node already in workflow when model loads, or reload model after adding patches
  - *From: Kijai*

- **Problem:** ComfyUI not detecting newly installed RAM
  - **Solution:** Check BIOS settings and for WSL users, create .wslconfig file to allocate more RAM to virtual environment
  - *From: Question*

- **Problem:** CUDA out of memory on 4090 with i2v
  - **Solution:** Use fp8 quantization on text encoder, use native clip vision loader instead of wrapper, disable non-blocking on block swap
  - *From: Kijai*

- **Problem:** Model hanging at 95% completion
  - **Solution:** Disable free noise and check if GPU is actually being utilized vs CPU fallback
  - *From: Flipping Sigmas*

- **Problem:** RuntimeError: CUDA error: out of memory is RAM issue not VRAM
  - **Solution:** For VRAM it would be allocation error instead - check RAM and swap access
  - *From: Kijai*

- **Problem:** Triton 3.2 causing issues
  - **Solution:** Downgrade to triton 3.1 version
  - *From: Cubey*

- **Problem:** Compile dropping with SLG node changes
  - **Solution:** Always run compile node to maintain compilation
  - *From: Kijai*

- **Problem:** TeaCache causing compile to drop
  - **Solution:** Fixed by always referencing original module and re-applying compile
  - *From: Kijai*

- **Problem:** Flash at beginning of vid2vid clips
  - **Solution:** Caused by frames past 81, keep under 88 frames or try riflex
  - *From: Kijai*

- **Problem:** Enhance a video node causing significant slowdown
  - **Solution:** Likely messing with VRAM management and auto blockswapping
  - *From: Doctor Shotgun*

- **Problem:** Generations taking much longer and using shared memory instead of GPU memory after updates
  - **Solution:** Check torch compile settings and memory allocation. May need to adjust offloading parameters
  - *From: Frojef*

- **Problem:** Loop argument node error when not connected
  - **Solution:** Fixed in updated version - node should work without loop args connected
  - *From: Kijai*

- **Problem:** VAE flash/noise issues with Mobius looping
  - **Solution:** Ensure VAE is properly connected and turn off freenoise. Still working on complete fix for VAE flash
  - *From: Kijai*

- **Problem:** TeaCache not working with looping
  - **Solution:** Disable TeaCache when using looping functionality. SLG and enhance-a-video work fine with looping
  - *From: Kijai*

- **Problem:** Sigma checking code fails with multiple conditioning elements
  - **Solution:** Use timestep[0] instead of full timestep array. Issue occurs with samplers like dpm_adaptive
  - *From: Ablejones*

- **Problem:** Spaces after pipe delimiters in prompts cause parsing issues
  - **Solution:** Remove spaces after | characters in multi-prompt strings for proper parsing
  - *From: fredbliss*

- **Problem:** LoRA loading became very slow (3 minutes)
  - **Solution:** Update to Torch 2.8 nightly - made loading instant again
  - *From: Fawks*

- **Problem:** Black screen and RuntimeWarning with i2v 480p bf16
  - **Solution:** Check model/setting mismatch - invalid value encountered in cast error
  - *From: Faust-SiN*

- **Problem:** Triton installation issues on RTX 5090
  - **Solution:** Use WSL Ubuntu setup instead of Windows
  - *From: Relven 96gb*

- **Problem:** Channels mismatch error with masking
  - **Solution:** Update wrapper nodes - fixed video mask handling was implemented
  - *From: Kijai*

- **Problem:** Mask input dimension mismatch
  - **Solution:** Input and output must have same spatial dimensions. Use Mask Resize node to same size as image input. Mask format must be B, H, W (ComfyUI standard)
  - *From: Kijai*

- **Problem:** MatAnyone outputs incompatible mask format
  - **Solution:** Use rembg instead of MatAnyone for mask generation to avoid size error messages
  - *From: burgstall*

- **Problem:** Video mask not working with flowedit
  - **Solution:** Mask input updated to allow video mask, but may need to bypass flowedit node for mask functionality
  - *From: Kijai*

- **Problem:** TeaCache destroying output
  - **Solution:** Go to 15 start value to avoid TeaCache destroying the output. TeaCache hates being used with certain settings
  - *From: Cubey*

- **Problem:** Torch compile triton version issue
  - **Solution:** Disable torch compile if getting triton-related errors
  - *From: Kijai*

- **Problem:** 14B model hanging on load
  - **Solution:** Try removing additional RAM sticks and use fp8 e4m3fn model instead of bf16
  - *From: Cubey*

- **Problem:** OOM with 4090 on 81 frames 1280x720 with 14b model
  - **Solution:** Use blockswap 40 setting
  - *From: Jas*

- **Problem:** rope_function and SLGARGS/LOOPARGS error
  - **Solution:** F5 to refresh and set rope_function to 'comfy' in node settings
  - *From: Kijai*

- **Problem:** Native Wan workflow error on latest ComfyUI
  - **Solution:** Update ComfyUI to commit ca8efab79fa19bc9745b4f7346d38a49ba1b1b7c or later, not just stable release
  - *From: spacepxl*

- **Problem:** Cannot copy out of meta tensor error with comfy-org 1.3B model
  - **Solution:** Use original model from Kijai repo instead of comfy-org version which has different keys
  - *From: Kijai*

- **Problem:** OOM during VAE decode with tiling enabled
  - **Solution:** Make sure VAE isn't in fp32, use bf16 instead
  - *From: Kijai*

- **Problem:** fp8_e4m3fn doesn't work for i2v models
  - **Solution:** Set weight_dtype to default instead
  - *From: BondoMan*

- **Problem:** Black output with i2v-720p models using fp8_e4m3fn weight_dtype
  - **Solution:** Disable sageattn auto mode and use manual sage attention settings
  - *From: Kijai*

- **Problem:** 'latent_mask' referenced before assignment error in WanVideo Encode
  - **Solution:** Update ComfyUI to nightly version, outdated ComfyUI lacks recent support
  - *From: Kijai*

- **Problem:** Generation time exploding from 80s/it to 180s/it after adding Patch Sage and Tea cache
  - **Solution:** Launch comfy with --reserve-vram option and set amount to what system is using
  - *From: Kijai*

- **Problem:** DepthAnythingV2 compatibility error
  - **Solution:** Update pytorch to cuda 12.4 in comfy and update xformers, or uninstall xformers as it works without it
  - *From: Juan Gea*

- **Problem:** Video load cap resetting to 49 frames
  - **Solution:** Disconnect any connections to the load cap parameter - connected nodes can override the value
  - *From: Kijai*

- **Problem:** Custom LoRAs don't shine with depth LoRA
  - **Solution:** Use depth + custom lora on early steps, then only custom lora on late steps
  - *From: spacepxl*

- **Problem:** Latent2RGB appearing too dark
  - **Solution:** Fixed scaling issue while implementing TAEW
  - *From: Kijai*

- **Problem:** Images not divisible by correct amount causing errors
  - **Solution:** Set divisible_by to 16 in resize node
  - *From: Kijai*

- **Problem:** OSError [WinError 193] %1 is not a valid Win32 application
  - **Solution:** Uninstall bitsandbytes - it gets imported through diffusers and causes triton compatibility issues
  - *From: Kijai*

- **Problem:** ComfyUI crashes with black screen flash
  - **Solution:** Check system logs for nvidia driver crash or virtual memory issues. Install armory crate can cause memory problems
  - *From: Kijai*

- **Problem:** LoRAs don't work with native workflow
  - **Solution:** Disable sage attention and torch compile nodes for LoRAs to function properly
  - *From: Cseti*

- **Problem:** Error with low_mem_load on lora load
  - **Solution:** Set low_mem_load to False on lora load node
  - *From: DawnII*

- **Problem:** Depth workflows failing
  - **Solution:** Use nightly version of ComfyUI
  - *From: Kijai*

- **Problem:** Tensor mismatch on resolutions with new image encode node
  - **Solution:** Use resize node since new node doesn't have automatic adjust_resolution
  - *From: DawnII/Kijai*

- **Problem:** ComfyUI Manager not updating to nightly properly
  - **Solution:** Manager works for repos but frontend updates to older version, update manually in venv
  - *From: LarpsAI*

- **Problem:** SLG causing distorted output
  - **Solution:** Try Euler sampler, limit SLG more (start later/end earlier), use appropriate resolution for model
  - *From: Kijai*

- **Problem:** 512x720 too low resolution for 720p model
  - **Solution:** Use 480p model for that resolution, or use 1280x720+ for 720p model
  - *From: Kijai*

- **Problem:** Error bypassing TeaCache with SLG
  - **Solution:** TeaCache patch is required, set threshold very low (like 0.05) to minimize effect
  - *From: Kijai*

- **Problem:** OOM with SLG Native but not with SLG in WanWrapper
  - **Solution:** Add buffer with --reserve-vram argument, patches can mess with native automatic VRAM calculations
  - *From: Kijai*

- **Problem:** Flow shift value 17 causes index out of bounds error
  - **Solution:** Use lower values like 8, don't go as high as 17
  - *From: David Snow*

- **Problem:** ComfyUI Manager losing git info and not checking for updates
  - **Solution:** Clean wrapper install, but manager updates can break it again
  - *From: Lumifel*

- **Problem:** Fal.ai LoRAs giving shape errors and key not loaded errors
  - **Solution:** LoRAs work for Image2Vid model not Text2Vid, check model compatibility
  - *From: TimHannan*

- **Problem:** SageAttention installation and compatibility issues
  - **Solution:** Linux installation much easier (5 seconds vs complex Windows issues), consider switching to Linux
  - *From: Benjimon*

- **Problem:** CUDA error about weight size mismatch
  - **Solution:** Caused by using ip2p conditioning without a control lora loaded, need control lora to change weight from [1536, 16, 1, 2, 2] to [1536, 32, 1, 2, 2]
  - *From: spacepxl*

- **Problem:** triton.ops module not found error
  - **Solution:** Uninstall or update bitsandbytes
  - *From: Kijai*

- **Problem:** PC freezing with CUDA out of memory
  - **Solution:** Lower video length or video resolution, blockswap can cause freezing behavior
  - *From: Benjimon/miko*

- **Problem:** WanVideo Sampler causing issues
  - **Solution:** Switch to KSampler instead
  - *From: arthuz*

- **Problem:** Loop args not working with 14B models
  - **Solution:** Context window uniform loop works with 14B but is very slow (30+ minutes for 5 seconds)
  - *From: Kijai*

- **Problem:** Image Resize to Closest outputting larger dimensions than limit
  - **Solution:** It maintains similar total pixel count - 832*832=677,376 vs 672*1008=692,224
  - *From: Kijai*

- **Problem:** CUDA out of memory errors on model loading
  - **Solution:** Check virtual memory/page file settings - having zero virtual memory can cause OOM issues even with sufficient RAM
  - *From: Juampab12*

- **Problem:** Weird artifacts in I2V at non-standard resolutions
  - **Solution:** Switch from native implementation to wrapper - resolved artifacts at 1056x896 and other non-standard sizes
  - *From: mamad8*

- **Problem:** VAE-related artifacts appearing as flashing or alignment issues
  - **Solution:** Check VAE model being used and consider switching to wrapper implementation
  - *From: Juampab12*

- **Problem:** Triton permission errors on Windows
  - **Solution:** Re-run requirements.txt and update wrapper nodes, or disable triton by unplugging compile node and switching attention to sdpa
  - *From: Cubey*

- **Problem:** OOM errors with exact same workflow that worked before
  - **Solution:** Load workflow from previous output file instead of autosave
  - *From: Ghost*

- **Problem:** Very slow renders and OOM with block swap
  - **Solution:** Don't use under 64GB RAM, adjust block swap settings carefully
  - *From: Obsolete*

- **Problem:** LoRA not changing when disabling blocks
  - **Solution:** Reload everything - might be cached without block settings. Also convert Musubi LoRAs to Diffusion-pipe format
  - *From: Juampab12/Benjimon*

- **Problem:** Can't connect blockswap node with KJnode workflows
  - **Solution:** Block swap isn't for native workflows, ComfyUI does it automatically
  - *From: Kijai*

- **Problem:** Torch compile not working fully with default RoPE
  - **Solution:** Set RoPE function to 'comfy' in sampler node instead of 'default'
  - *From: Kijai*

- **Problem:** First frame degradation and brightening with Start/End Frame
  - **Solution:** Trim some frames, never had first frame flash with proper end frame workflow
  - *From: Benjimon/Kijai*

- **Problem:** RuntimeError with mat1 and mat2 shapes
  - **Solution:** Related to prompt format compatibility issues
  - *From: Fawks*

- **Problem:** FlowEdit generations failing after first frame
  - **Solution:** No specific solution provided in discussion
  - *From: Dream Making*

- **Problem:** TAESD preview warning with taew2_1.safetensors
  - **Solution:** Change preview settings to something other than TAESD in ComfyUI manager, or download the file to vae_approx folder
  - *From: ingi // SYSTMS*

- **Problem:** VRAM retention issues at lower resolutions with native Wan
  - **Solution:** Click 'unload models' to release excess VRAM, or use higher resolutions (640x640+) to avoid the issue
  - *From: Screeb*

- **Problem:** Black output when rendering single frame with wrapper
  - **Solution:** Disable enhance-a-video when doing single frame generation
  - *From: Kijai*

- **Problem:** Florence2 error in segment-anything-2 node
  - **Solution:** Downgrade transformers to version 4.49.0 from 4.50.0
  - *From: Kijai*

- **Problem:** Meta tensor copy error with LoRAs
  - **Solution:** Disable low_vram_load setting on the LoRA loader
  - *From: Kijai*

- **Problem:** Triton error with 1.3B model
  - **Solution:** Set quantization to 'default' instead of other options
  - *From: Dream Making*

- **Problem:** Dimension not divisible error
  - **Solution:** Ensure input video dimensions are divisible by 16
  - *From: Kijai*

- **Problem:** FP16 T5 encoder breaks with I2V
  - **Solution:** Use BF16 T5 encoder for I2V workflows, FP16 works better for T2V
  - *From: IllumiReptilien*

- **Problem:** OOM errors with experiment_args node
  - **Solution:** Remove experiment_args node completely from workflow even if disabled
  - *From: The Shadow (NYC)*

- **Problem:** Black outputs with CFG Zero Star on native
  - **Solution:** Disable zero init, use euler/normal sampler, check denoise value is correct
  - *From: Kijai*

- **Problem:** CFG Zero Star ruins I2V with Wan when zero init enabled
  - **Solution:** Disable zero init for I2V workflows
  - *From: Kijai*

- **Problem:** Artifacts with CFG Zero Star
  - **Solution:** Don't set shift values too low, use default settings
  - *From: Faust-SiN*

- **Problem:** SLG artifacts in native with prismatic colors
  - **Solution:** Reduce CFG when using SLG to avoid strange prismatic-like colors
  - *From: Miku*

- **Problem:** AttrsDescriptor import error with triton
  - **Solution:** CUDA tools version compatibility issue, may need to use different CUDA version
  - *From: Question*

- **Problem:** Tiled clip vision causing issues with InP models
  - **Solution:** Disable tiling in the clipvision node for much better results
  - *From: David Snow*

- **Problem:** TorchCompile crashes when TeaCache activates with InP models
  - **Solution:** Issue is actually with SLG node, not TorchCompile - SLG doesn't work with InP models
  - *From: JmySff*

- **Problem:** Control LoRAs incompatible with Fun Control models
  - **Solution:** Cannot use control loras with the new Fun Control models
  - *From: Kijai*

- **Problem:** Size mismatch errors with Fun models
  - **Solution:** Resize all control images and reference images to same dimensions
  - *From: Kijai*

- **Problem:** Dark frame effect at end of videos
  - **Solution:** Enable the new masking method boolean in latest wrapper version
  - *From: Kijai*

- **Problem:** torch._dynamo cache size limit hit
  - **Solution:** Set higher cache limit in the compile node
  - *From: Kijai*

- **Problem:** LoRA loading bug in original Wan Fun nodes.py
  - **Solution:** Bug exists in load lora function, needs fixing for 14B model LoRA support
  - *From: ZeusZeus (RTX 4090)*

- **Problem:** 1.3B InP model producing poor quality outputs
  - **Solution:** Use SLG starting from block 8, enable new masking method, try CFG ZeroStar
  - *From: Kijai*

- **Problem:** Control model doesn't work well with old LoRAs
  - **Solution:** Model compatibility issue - LoRA strength needs to be increased to 2.0+ but still doesn't work well
  - *From: Kijai*

- **Problem:** OOM error with ImageToVideo Encode at high resolution
  - **Solution:** Set VAE to bf16 precision, was testing at 2304x1536
  - *From: mamad8*

- **Problem:** Tiling causes artifacts with new Fun models
  - **Solution:** Set tiles to 0 if using old version of example workflow, tiling seems to cause problems with this model
  - *From: Kijai*

- **Problem:** onnxruntime installing instead of runtime-gpu
  - **Solution:** Issue with DWPose taking forever due to wrong runtime package being installed
  - *From: ArtOfficial*

- **Problem:** Bad generation quality with Fun InP model
  - **Solution:** Check if SLG, CFG, or other settings are too strong - 'something too strong' causing poor results
  - *From: Kijai*

- **Problem:** Missing custom nodes in workflow
  - **Solution:** Need to install WanVideoWrapper from GitHub and run 'pip install -r requirements.txt' in the node folder
  - *From: Question*

- **Problem:** Sage attention causing issues with 1.5 models
  - **Solution:** Sage attention flag can break sampler when using 1.5 models, need to disable it
  - *From: Question*

- **Problem:** Error with euler sampler in wanvideo
  - **Solution:** Known issue, euler doesn't work with WanVideo sampler currently
  - *From: seitanism*

- **Problem:** Wrong text encoder error
  - **Solution:** Use the text encoder from comfy org wan huggingface instead
  - *From: comfy*

- **Problem:** Shape error with dimensions not divisible by 16
  - **Solution:** Ensure input dimensions are divisible by 16, try 768x560 or 832x480
  - *From: DawnII*

- **Problem:** Frame count errors
  - **Solution:** Frame count must follow 4n+1 formula (9, 13, 17, 21, 41, 81). Try different counts like 21 for testing
  - *From: DawnII*

- **Problem:** Load Video format causing issues
  - **Solution:** Change format from AnimateDiff to Wan in Load Video node
  - *From: Hot Hams, the God of Meats*

- **Problem:** Wrong model channels error (36 vs 48)
  - **Solution:** Only the control model can take 48 channels, make sure you're using the Fun-Control model not the InP model
  - *From: Kijai*

- **Problem:** Shape invalid for input size error
  - **Solution:** Check video length parameter, ensure it matches the actual frame count
  - *From: Kijai*

- **Problem:** ComfyUI Manager registry issues
  - **Solution:** Use git clone directly on repos instead of using manager after registry update
  - *From: deleted_user_2ca1923442ba*

- **Problem:** Tensor size mismatch when switching aspect ratios
  - **Solution:** Check for hardcoded size parameters in nodes - found hidden aspect ratio override causing the issue
  - *From: A.I.Warper*

- **Problem:** ComfyUI crashes when loading i2v 480p fp8 model
  - **Solution:** Use models_clip_open-clip-xlm-roberta-large-vit-huge-14.pth instead of other clip models
  - *From: 852話 (hakoniwa)*

- **Problem:** Control applying on first step regardless of start_percent
  - **Solution:** Bug with ensure first step - was applying control on first step no matter what start_percent was set
  - *From: Kijai*

- **Problem:** Memory issues with workflows
  - **Solution:** Check if ComfyUI-Miaoshouai-Tagger is in workflow - code never offloads the model which causes memory problems
  - *From: Kijai*

- **Problem:** WanVideoEmptyEmbeds control_embeds error
  - **Solution:** Update to ComfyUI nightly version and ensure WanVideoWrapper is version 1.1.1
  - *From: Kijai*

- **Problem:** torch._scaled_mm error on 3090
  - **Solution:** Can't use fp8_fast on 3090, and shouldn't use it with Wan models anyway
  - *From: Kijai*

- **Problem:** Color shifts when stitching clips together
  - **Solution:** Use last frame as exact start frame for next clip, stitch latents before VAE decode
  - *From: Kijai*

- **Problem:** Memory error after adding RAM (8GB VRAM)
  - **Solution:** Related to system RAM increase causing issues, strangely worked at 16GB but errors at 32GB
  - *From: Verevolf*

- **Problem:** TeaCache error with 'OptimizedModule' object
  - **Solution:** Set threshold to 0 to prevent crashes, or use different TeaCache node
  - *From: AJO*

- **Problem:** Shape error '[1, 33, 4, 96, 56]' is invalid
  - **Solution:** Related to frame load cap and frames per second settings not being set correctly
  - *From: ✧ฅโ๑ↀᆺↀ ๑ใฅ✧PookieNumnums*

- **Problem:** Glitches at stitch point when combining latents
  - **Solution:** Don't remove first latent of first batch, latents may not be separable like individual frames
  - *From: seitanism*

- **Problem:** OOM errors with new TeaCache version
  - **Solution:** Change rope_function to 'comfy' instead of default
  - *From: Kijai*

- **Problem:** Error with optional VAE input
  - **Solution:** Disconnect the optional VAE input
  - *From: Zuko*

- **Problem:** Gray degradation at end of video with Fun 1.3B inpaint
  - **Solution:** Toggle the fun node in image encode
  - *From: DawnII*

- **Problem:** Last frame deviates from input end frame
  - **Solution:** Use normal Wan instead of InP model for start+end frame
  - *From: ArtOfficial*

- **Problem:** Fun models not found in directory
  - **Solution:** No need to use their repo, models work in Kijai wrapper and ComfyUI natively
  - *From: Kijai*

- **Problem:** Image to video encode issue
  - **Solution:** Update messed up inputs, need to reconnect VAE, clip_embeds and images again
  - *From: Kijai*

- **Problem:** Sampling gets stuck with insufficient VRAM
  - **Solution:** Increase block swap amount up to 40
  - *From: Kijai*

- **Problem:** Bad resolution 512x256
  - **Solution:** Use better resolution ratios
  - *From: Benjimon*

- **Problem:** Control LoRA causing tensor mismatch with Fun models
  - **Solution:** Remove control LoRA - Fun models have control embeds built-in and don't need separate control LoRAs
  - *From: Kytra*

- **Problem:** FloweEdit producing rainbow noise
  - **Solution:** Issue caused by euler scheduler change - works better with normal inference but needs different settings for flow edit, or possibly TeaCache causing issues
  - *From: Kijai*

- **Problem:** Pose control not working properly with reference
  - **Solution:** When pose is too far from reference pose, reduce control latent strength and/or end percent of control embed
  - *From: Kijai*

- **Problem:** 1080p I2V glitching at outer borders beyond 1280x720
  - **Solution:** Might need RiFlex-type hack with RoPE. Tiled VAE encode/decode messes with quality, with tiled encode being much worse than decode
  - *From: aikitoria*

- **Problem:** Training only producing noise instead of meaningful images
  - **Solution:** Need much larger dataset (millions of samples, not 1200), proper learning rate scaling, and expect 10x-100x longer training time
  - *From: spacepxl*

- **Problem:** VAE tiled encode causing black outputs
  - **Solution:** Turn off VAE tile encode and decode - values weren't being converted to latent space properly
  - *From: VK (5080 128gb)*

- **Problem:** TeaCache causing garbled images
  - **Solution:** TeaCache values defaulted to 1/-1 which ruined initial frame
  - *From: JohnDopamine*

- **Problem:** Zero init causing messy inpainting results
  - **Solution:** Disable zero init for better inpainting results
  - *From: PirateWolf*

- **Problem:** SLG causing weird color distortion
  - **Solution:** Lower CFG until fixed, use CFG 3-5 and SLG strength 0.1-0.9
  - *From: DawnII*

- **Problem:** VRAM usage gradually increasing during sampling
  - **Solution:** Issue reported but couldn't be reproduced by developer
  - *From: DevouredBeef*

- **Problem:** Memory stepping up linearly with torch.compile + comfy RoPE
  - **Solution:** Use dynamic mode for torch.compile or clear triton cache
  - *From: Kijai*

- **Problem:** Black outputs when using SLG with zero star
  - **Solution:** Disable use_zero_init when using SLG with zero star from kijai node, or use native zero star node
  - *From: Miku*

- **Problem:** VAE tiling causing black outputs
  - **Solution:** Disable VAE tiling, it's not really needed anyway
  - *From: Kijai*

- **Problem:** Wrapper model connection issues after update
  - **Solution:** Reconnect VAE, start image, and clip embeds after recent commit changes
  - *From: DawnII*

- **Problem:** FlowEdit not working with unipc
  - **Solution:** May need to return old Euler scheduler specifically for flowedit
  - *From: Kijai*

- **Problem:** Native vs wrapper quality difference
  - **Solution:** Wrapper produces more stable outputs, especially for fast motion V2V inputs
  - *From: David Snow*


## Model Comparisons

- **Movement quality vs Kling**
  - This is like kling level - movement is insane, even knew to turn into drift like real cars
  - *From: deleted_user_2ca1923442ba*

- **GGUF vs regular model speed**
  - GGUF is faster when regular model gets offloaded but GGUF fits in VRAM, otherwise GGUF is bit slower
  - *From: seitanism*

- **Second pass vs more steps**
  - David Snow testing this comparison but results not yet reported
  - *From: David Snow*

- **UniPC vs DPM++ samplers**
  - UniPC significantly better - produces sharper details, better texture quality, fewer artifacts
  - *From: Kijai*

- **14B vs 1.3B model artifacts**
  - 14B model has far fewer dot/rope artifacts compared to 1.3B
  - *From: Kijai*

- **I2V vs T2V artifact levels**
  - I2V produces much cleaner results with fewer rope artifacts because image provides positional guidance
  - *From: deleted_user_2ca1923442ba*

- **WAN wrapper vs native implementation**
  - Wrapper consistently produces better quality, especially for I2V and complex prompts
  - *From: T8star-Aix*

- **fp16 accumulation vs fp8 matrix multiplication**
  - fp16 accumulation works much better than fp8 for WAN
  - *From: comfy*

- **SDE DPM vs UniPC samplers**
  - SDE DPM produces better quality but is slower
  - *From: Juampab12*

- **Video models vs image models for cleanup**
  - Video models don't perform as well as image models for v2v/i2i cleanup tasks
  - *From: Draken*

- **Wan native vs wrapper**
  - Native is 10-15% faster, wrapper produces better quality but takes longer
  - *From: Kijai*

- **Wan VAE vs Hunyuan VAE**
  - Wan VAE uses magnitudes less memory, doesn't need tiling
  - *From: Kijai*

- **Default PyTorch attention vs Sage render**
  - Sage render: 5 minutes, default PyTorch attention: 22 minutes
  - *From: TK_999*

- **UniPC vs DPM++ samplers for Wan**
  - UniPC works better, DPM_2_ancestral even better but twice as slow
  - *From: David Snow*

- **TeaCache speed improvement comparison**
  - 53 seconds vs 28 seconds, 1 hour to 18 minutes, 730 seconds to 430 seconds depending on setup
  - *From: Kijai*

- **Wan 1.3B vs SD3.5 2.5B for images**
  - 1.3B WanX is more coherent than 2.5B SD3.5
  - *From: CDS*

- **Wan 14B texture quality vs Flux**
  - Wan 14B t2v model is pretty good but lacks texture compared to flux
  - *From: zelgo_*

- **Wan vs LTX prompt adherence**
  - Wan significantly better at following prompts - 'After hundreds of LTX gens, Wan actually does what you ask'
  - *From: N0NSens*

- **TeaCache vs no TeaCache quality**
  - Slight quality loss with TeaCache but very acceptable trade-off for 50-100% speed improvement
  - *From: slmonker*

- **Wan original vs Hunyuan upscale**
  - Sometimes original Wan output looks better than Hunyuan upscaled version
  - *From: seitanism*

- **Wan vs Hunyuan prompt following**
  - Wan follows prompts much better than Hunyuan, but Hunyuan has better quality
  - *From: for1096*

- **Wan 1.3B vs other models**
  - Wan t2v 1.3B model is fantastic, very lightweight (2.8GB) and fast
  - *From: David Snow*

- **UniPC vs DPM++ samplers**
  - UniPC is just better than DPM++, though sometimes unipcs look like blurry mess
  - *From: Kijai*

- **fp32 vs bf16 precision**
  - fp32: 475s / bf16: 246s - not enough quality difference to be worth the extra time
  - *From: David Snow*

- **Stepfun vs Wan for movement**
  - Stepfun is stronger choice for movement, but doesn't have img to vid. For img to vid wan is great
  - *From: deleted_user_2ca1923442ba*

- **Native vs Kijai wrapper**
  - Kijai's wrapper is the superior option for tinkerers and advanced users, native is easier and uses less memory
  - *From: David Snow*

- **fp16_fast vs fp8 speed**
  - fp16_fast is about 20% faster: fp8 took 4m 55s, fp16_fast took 4m 39s but fp8 had better quality
  - *From: Juampab12*

- **Block swap vs VRAM management node**
  - Block swap is faster but can't save as much VRAM as VRAM management
  - *From: Kijai*

- **Native vs Wrapper results**
  - Wrapper shows different results from native, including different initial frame adherence and processing differences
  - *From: Simonj*

- **Uniform sampling vs fps sampling**
  - fps sampling significantly outperforms uniform sampling by maintaining consistent temporal relationships
  - *From: fredbliss*

- **FP32 vs BF16 quality**
  - Not worth the extra time, better to use more steps or second sampler pass
  - *From: David Snow*

- **1.3B vs 14B model**
  - Huge difference between the two models, 14B significantly better quality
  - *From: TK_999*

- **TeaCache performance**
  - 60 samples with teacache (227s) faster than 20 samples without teacache (240s)
  - *From: David Snow*

- **UniPC vs DPM++ samplers**
  - UniPC is remarkable and better than DPM++ on this model
  - *From: David Snow*

- **UniPC vs DPM++ samplers**
  - UniPC better for both T2V and I2V models, specifically UniPC BH2 variant in wrapper
  - *From: Kijai*

- **480p vs 720p I2V model**
  - 480p sometimes gives better videos with better motion and prompt adherence, especially at lower steps. 720p unbeatable at full 50 steps
  - *From: Juampab12*

- **1.3B model VRAM usage**
  - Only uses 5.2GB VRAM compared to 14B model, very efficient
  - *From: Benjimon*

- **GGUF vs fp8 models**
  - fp8 models are faster and equal quality
  - *From: burgstall*

- **unipc_bh2 wrapper vs native**
  - unipc_bh2 works great with wrapper but looks bad on native
  - *From: David Snow*

- **TeaCache vs Adaptive Guidance**
  - Adaptive Guidance works like TeaCache but without losing quality for fast movements
  - *From: Miku*

- **dpmpp_2m vs unipc on wrapper**
  - unipc reduces dotted mesh pattern compared to dpm++
  - *From: David Snow*

- **Wrapper vs Native VAE noise**
  - Wrapper has less VAE noise than native implementation
  - *From: Dream Making*

- **TeaCache quality vs speed tradeoff**
  - Reducing threshold or increasing start value makes image more stable but loses some speed
  - *From: JmySff*

- **FP8 vs higher precision**
  - FP8 model isn't always better for quality depending on use case
  - *From: JmySff*

- **Hunyuan vs Wan t2v**
  - For most t2v prefer hunyuan, but Wan i2v is in its own league open source wise
  - *From: Shawneau 🍁 [CA]*

- **fp8 vs fp8 fast quality**
  - fp8 quality is good, fp8 fast quality is not good
  - *From: Juampab12*

- **TeaCache vs no TeaCache**
  - Some quality loss but overall result is consistent, good for finding prompts/seeds
  - *From: intervitens*

- **res_2m vs euler sampler**
  - res_2m same speed as euler but should produce better quality outputs
  - *From: Ablejones*

- **Context windowing vs RifleX for long videos**
  - Context windowing maintains better temporal consistency, RifleX creates constant looping artifacts
  - *From: Kijai*

- **GGUF Q8 vs Q6_K vs fp8 performance**
  - fp8 fastest overall, Q8 can outperform Q6_K even when partially loaded, but lower quants take more compute
  - *From: Kijai*

- **14B vs 1.3B model for complex scenes**
  - 14B model handles context switching and complex interactions much better but takes significantly longer
  - *From: Kijai*

- **Wan vs Hunyuan quality**
  - Mixed opinions - some find Wan more consistent, others prefer Hunyuan quality. Wan has better prompt following but Hunyuan has better visual quality
  - *From: Draken*

- **Wan T2V vs I2V performance**
  - I2V performs much better than T2V, almost like different model families despite sharing computational cost
  - *From: Draken*

- **Sliding context vs RiFlex**
  - Sliding context looks better than RiFlex and doesn't have the VRAM constraints
  - *From: Draken*

- **Wan results vs Runway quality**
  - Wan results are almost as good as Runway but free
  - *From: VRGameDevGirl84(RTX 5090)*

- **Native vs Wrapper speed**
  - Native: 13.97 seconds, Wrapper: 49.519 seconds for same generation
  - *From: avataraim*

- **FBCache vs TeaCache**
  - FBCache doesn't need tuning per model but seems slightly worse in general
  - *From: Kijai*

- **1.3B vs 14B model batching**
  - 14B wouldn't be feasible for batched cfg due to VRAM requirements, so native generally doesn't do that
  - *From: Kijai*

- **Sage vs other optimizations**
  - Sage is by far the best boost for both quality and performance
  - *From: Kijai*

- **Wrapper vs Native speed**
  - Wrapper faster with Tea and Blocks, but native needed for some implementations like HunFlowEdit
  - *From: N0NSens*

- **Wan vs Hunyuan fine movements**
  - Wan does much better job at capturing fine movements than Hunyuan
  - *From: TK_999*

- **Wan frames vs other models**
  - Wan's frames are more valuable overall, allowing for subtle interpolation to 24fps
  - *From: Juampab12*

- **TeaCache vs FB cache**
  - Both FB cache and ComfyUI's TeaCache were slightly worse than Kijai's TeaCache implementation
  - *From: Kijai*

- **Step counts for quality**
  - 20 steps seems fine, anything over doesn't make huge difference. 10 works for toon style
  - *From: VRGameDevGirl84(RTX 5090)*

- **Wan I2V vs T2V quality**
  - I2V shows better quality and motion than T2V, feels like from different team. I2V maintains subject consistency across scene changes
  - *From: Draken*

- **Native vs Wrapper VRAM usage**
  - Native workflow uses ~40% RAM while wrapper uses 90-100% RAM, native can handle larger resolutions
  - *From: AJO*

- **Samplers for I2V**
  - DPM++ seems better than UniPC for I2V, though UniPC works better for T2V with wrapper
  - *From: David Snow*

- **UniPC sampler issues**
  - UniPC is glitchy for native T2V 1.3B - causes random bright flashing blobs and poor detail
  - *From: Screeb*

- **TeaCache with vs without coefficients**
  - With coefficients is better quality when adjusted for same speed - coefficients version is 'smarter' about which steps to skip
  - *From: DevouredBeef*

- **BF16 vs GGUF Q8 model quality**
  - BF16 full 32GB model is much better quality than GGUF Q8, even when run with fp16 accumulation
  - *From: JmySff*

- **10 steps vs 40-50 steps**
  - Higher step counts (40-50) produce better results than 10 steps which can cause slow motion issues
  - *From: Juampab12*

- **BF16 vs fp8 model quality**
  - BF16 shows much better prompt adherence and quality, rendering varies more from second scene onwards
  - *From: JmySff*

- **14B vs 1.3B model quality**
  - The difference is huge between 14B and 1.3B
  - *From: garbus*

- **480p vs 720p model stability**
  - 480p models seem to be much more stable, at least for resolutions up to 1120x632, prompt adherence is strangely better
  - *From: JmySff*

- **Model speed comparison**
  - 14b - 3:50 / Q6 - 3:25 / Q4 - 3:30 / 1.3b - 0:39
  - *From: N0NSens*

- **Hunyuan I2V vs Wan I2V**
  - Hunyuan I2V is fast but not all that impressive compared to wan
  - *From: Cubey*

- **Wan 1.3b vs 14b model**
  - One produces crappy results, the other doesn't (implying 14b is much better)
  - *From: N0NSens*

- **FP8 vs FP16 sage attention**
  - FP8 is faster but may have quality issues, FP16 is safer
  - *From: intervitens*

- **Wan vs Hunyuan I2V quality**
  - Wan is way better - much sharper with no softening filter, though Hunyuan has better motion
  - *From: aikitoria*

- **Hunyuan I2V vs T2V**
  - Hunyuan T2V was WAY better than I2V
  - *From: Colin*

- **Topaz Chronos vs RIFE/SVP**
  - Topaz Chronos is far better for frame interpolation
  - *From: aikitoria*

- **3090ti vs 4090 speed**
  - 4090 setup runs about twice as fast as 3090ti setup
  - *From: intervitens*

- **Wan vs Hunyuan I2V**
  - Wan is much higher quality with better prompt adherence, Hunyuan is faster but ignores prompts
  - *From: Faust-SiN*

- **Wan vs Hunyuan T2V**
  - Wan generally better for T2V, especially for non-realistic humans. Hunyuan good for LoRA training
  - *From: JohnDopamine*

- **FP16 vs FP32 quality**
  - FP16 almost identical to FP32, best quality option
  - *From: comfy*

- **Quantized models vs Flux**
  - Quantizing video models gives worse results than Flux quantization
  - *From: comfy*

- **Wan vs Hunyuan I2V quality**
  - Wan is by far the best I2V, user skipped Hunyuan I2V completely
  - *From: Janosch Simon*

- **30 bad LTX vs 1 good Wan generation**
  - Would rather have single good Wan generation despite 10 minute generation time on 4x4090s
  - *From: aikitoria*

- **Wan T2V vs Hunyuan T2V**
  - No clear winner - Wan gets physics and fine movements better, Hunyuan behaves differently. Both have strengths
  - *From: TK_999*

- **1.3B vs 14B Wan models**
  - 1.3B decent for speed, 14B fantastic but slow
  - *From: TK_999*

- **Wan sharpness vs Hunyuan**
  - Wan produces sharp results, Hunyuan is the non-sharp one
  - *From: aikitoria*

- **Wan vs Hunyuan I2V**
  - Wan is better quality, Hunyuan is faster. Wan isn't distilled so better by default
  - *From: comfy*

- **14B vs 1.3B models**
  - 14B is better quality but too slow for 3060 12GB, 1.3B decent with teacache making it fast
  - *From: ArcherEmiya*

- **Scaled FP8 vs regular FP8**
  - Scaled FP8 is slower by 9 s/it
  - *From: Doctor Shotgun*

- **Wan vs Luma**
  - Wan better at prompt understanding and specific actions like violin movement, Luma looks better visually
  - *From: NebSH*

- **Native vs Wrapper VRAM usage**
  - Native has better VRAM management, can do 1280x720 on 4090 vs OOM on wrapper
  - *From: zoz*

- **480p vs 720p model at same resolution**
  - 720 at 480 looks bad and 480 at 720 looks bad
  - *From: Juampab12*

- **Block swapping vs native VRAM**
  - Block swapping trades VRAM for time - same speed if optimizations used
  - *From: Benjimon*

- **Linux vs Windows for AI**
  - Linux saves ~1.5GB VRAM from Windows bloat and makes AI easier
  - *From: Colin*

- **480p model vs 720p model for 480p resolution**
  - 480p model is obviously better for 480p resolution, that's why it's called that
  - *From: aikitoria*

- **Wan I2V vs Hunyuan I2V**
  - Even 480p Wan I2V with interpolation and upscale is better than Hunyuan I2V results
  - *From: Shawneau 🍁 [CA]*

- **TeaCache with vs without coefficients**
  - Without coefficients: 5min32, with default coefficient values: 6min36 for same 20 step generation
  - *From: JmySff*

- **Block swapping vs full VRAM**
  - Block swapping roughly same inference time as 48GB GPU, enables full fp16/bf16 model usage without quality or speed hit
  - *From: Benjimon*

- **14B vs 1.3B speed**
  - 14B is significantly slower - 1.3B: 3.87s/it vs 14B: 19.59s/it for same settings
  - *From: burgstall*

- **fp32 vs fp16 for 1.3B model**
  - Minimal difference to fp16 and slower, not worthwhile
  - *From: Kijai*

- **TensorRT upscaler vs others**
  - Best upscaler seen so far in ComfyUI
  - *From: VRGameDevGirl84(RTX 5090)*

- **Wan vs Hunyuan for T2V/I2V**
  - Wan better for I2V with superior physics and likeness retention, Hunyuan faster and better NSFW. Community mixed on T2V quality
  - *From: JohnDopamine*

- **Wan VAE vs Hunyuan VAE**
  - Wan VAE most efficient, Hunyuan has worst/most inefficient VAE of all video models
  - *From: comfy*

- **5090 vs 4090 performance**
  - 5090 about 20-30% faster than 4090 in inference, but thermal issues with Founders Edition
  - *From: seitanism*

- **FP16 vs FP8 weights**
  - FP8 is 25% faster but causes quality degradation, though some users report no noticeable loss
  - *From: Doctor Shotgun*

- **Wan vs Hunyuan prompt adherence**
  - Wan generally has better prompt adherence, but Hunyuan handles typos more literally
  - *From: Doctor Shotgun*

- **Block swap vs VRAM management**
  - Block swap uses non-blocking transfers but less RAM efficient, VRAM management handles it better
  - *From: Kijai*

- **Squish LoRA quality vs Pika-labs**
  - Almost 1:1 quality match with Pika-labs original
  - *From: orabazes*

- **Wan I2V vs other models**
  - Wan is on different level for I2V than anything else open, follows prompts much better than HunyuanVideo
  - *From: Kijai*

- **E4M3FN vs E5M2 model types**
  - E5M2 necessary for 3000 series GPUs when using torch.compile, otherwise just different dtype
  - *From: Kijai*

- **SageAttention 1 vs 2**
  - SageAttention 2 is for 3090, version 1 better for 4090
  - *From: Juampab12*

- **LTX vs WAN for upscaling**
  - LTX much worse quality but much faster generation, better for faster creative iteration. WAN/HY change content more than expected compared to SDXL upscale
  - *From: Juampab12*

- **Block swap vs VRAM management**
  - Block swap is faster but very RAM inefficient
  - *From: Kijai*

- **Native vs Kijai wrapper**
  - Native not worth it even with new models, back to Kijai workflows and nodes
  - *From: Shawneau 🍁 [CA]*

- **Wan vs LeapFusion I2V**
  - LeapFusion has good likeness but suffers from lack of motion happening
  - *From: Draken*

- **VACE vs LTX+IC LoRA**
  - Wan+ACE requires 8 times computing power and more than 10 times time compared to LTX+IC LoRA
  - *From: DREX*

- **5090 vs 3090 for AI workloads**
  - 5090 has more than 3x the performance of 3090 with barely more power draw
  - *From: spacepxl*

- **AI vs gaming performance improvements**
  - 5090 improvement is much bigger in AI stuff than in gaming
  - *From: Juampab12*

- **TeaCache vs FB cache**
  - TeaCache better when tuned per model, FB cache more versatile as doesn't need tuning
  - *From: Kijai*

- **fp16 vs fp8 for Wan**
  - If fp16 fits in VRAM, zero reason to use fp8 versions as this model doesn't like fp8 matrix mult
  - *From: comfy*

- **Ampere vs Ada for diffusion**
  - Ampere feels like half the speed of Ada for diffusion models
  - *From: Doctor Shotgun*

- **TeaCache vs CFG scheduling**
  - Both provide similar speedup benefits, TeaCache skips whole steps while CFG scheduling reduces computation
  - *From: Kijai*

- **720p vs 480p inference speed**
  - 480p I2V is at very usable spot, 720p is painful for speed
  - *From: Kijai*

- **14B vs 1.3B model practicality**
  - Large models don't have much future due to speed limitations on consumer cards, small models like 1.3B could reach more people
  - *From: Cseti*

- **TeaCache quality impact**
  - Hit or miss - works well as preview, some seeds look identical, others show significant degradation with more warping
  - *From: aikitoria*

- **TeaCache speed vs quality trade-off**
  - With TeaCache: 3:33 generation time vs without: 5:35, but TeaCache breaks with big motion and may waste time with multiple generations needed
  - *From: Payuyi*

- **Training time 1.3B vs 14B**
  - 14B training about 20x slower than 1.3B, requiring gradient checkpointing and offloading on 32GB setup
  - *From: Kijai*

- **Different TeaCache thresholds**
  - Lower thresholds (0.18-0.2) provide better quality than 0.22, with 0.035 being too low to be effective
  - *From: intervitens*

- **Wan vs LTX for story generation**
  - LTX quality kills hybrid workflows, but LTX good for small movements only
  - *From: AJO*

- **Native vs Wrapper rendering quality**
  - Native shows dotted texture artifacts that wrapper doesn't have as prominently, despite same parameters
  - *From: Kijai*

- **Wan vs Hunyuan realism**
  - Hunyuan does realism better according to user experience
  - *From: Shawneau*

- **4090 48GB prices China vs Western sites**
  - $3k USD on Xianyu (China) vs $4k+ on Western sites, but Xianyu doesn't ship outside China
  - *From: Doctor Shotgun*

- **Wan vs HunyuanVideo**
  - Wan is better overall, especially for I2V. HunyuanVideo only has value for T2I and speed
  - *From: aikitoria*

- **fp16 vs bf16 precision**
  - fp16 is 20% faster and better quality on RTX 4090 due to Nvidia's consumer GPU limitations
  - *From: Kijai*

- **480p vs 720p Wan models**
  - 480p model has better motion coherence and works fine upscaled, 720p model can be problematic
  - *From: David Snow*

- **WAN Control Lora vs Topaz**
  - Control Lora now provides better options than Topaz, particularly impressive for upscaling. More comparable to Aura SR or Supir - bigger gains on lower quality inputs
  - *From: ramonguthrie*

- **LTX vs WAN for upscaling**
  - LTX upscaling works quite well for low-res upscaling, produces crisp results, though WAN control tile may be better overall
  - *From: N0NSens*

- **Flux upscaling vs other methods**
  - Flux schnell is popular and fast for LTV/Animatediff but tiled controlnet for flux not that good, results too NPR style
  - *From: ramonguthrie*

- **Wiki vs [wiki] token usage**
  - Both <wiki> and [wiki] produced same results on same seed
  - *From: TK_999*

- **SkipLayerGuidanceDiT vs normal sampling**
  - Skip layer dramatically improved results, better prompt adherence
  - *From: CapsAdmin*

- **Native vs Wrapper workflow speed**
  - Native consistently faster than wrapper for some users
  - *From: N0NSens*

- **AD vs new video models for consistency**
  - AD still better for low denoise vid2vid work, but new models handle 81 frames vs AD's 16 frame limit
  - *From: Draken*

- **480p LoRAs on 720p model**
  - Kind of didn't keep any of the details when using 480p loras on 720p model
  - *From: Benjimon*

- **Wan 1.3B vs Hunyuan speed**
  - 1.3B model runs faster than Hunyuan
  - *From: TimHannan*

- **Native SLG vs wrapper SLG**
  - Native is more advanced instead of just skipping layers, has more options
  - *From: Kijai*

- **Default RoPE vs ComfyUI RoPE**
  - ComfyUI RoPE changes results temporally, motion seems amplified in I2V, but quality differences unclear
  - *From: Kijai*

- **Native vs Wrapper RAM management**
  - Native RAM management is better than wrapper, but max model limits are the same
  - *From: Kijai*

- **UniPC vs other samplers for T2V**
  - For Wan T2V in wrapper, only UniPC is acceptable. I2V has smaller differences between samplers
  - *From: Kijai*

- **Native vs Wrapper frame limits**
  - Native: 101/105 frames max at 960x544. Wrapper: 97 frames max with same settings
  - *From: JmySff*

- **Wan 1.3B vs larger models for coherent generation**
  - CJ found 1.3B impressive despite most people dismissing it for lack of coherent generations
  - *From: CJ*

- **SLG quality vs speed trade-off**
  - SLG is better than free lunch - improves quality AND increases inference speed
  - *From: Kijai*

- **SAGE vs SDPA attention modes**
  - SAGE: better facial expression, no wall warping, but arm mutations. SDPA: worse background warping, less expressive face
  - *From: Benjimon*

- **fp8_fast vs regular fp8**
  - fp8_fast is faster but ruins quality completely on Wan model
  - *From: Kijai*

- **Wan 1.3B vs 14B LoRA sizes**
  - 1.3B LoRAs are much smaller (83MB at rank 64) vs 14B (500MB at rank 64)
  - *From: Flipping Sigmas*

- **Step-Video-TI2V specs**
  - 30B parameters, about same disk size as Wan, requires 4+ GPUs, includes anime in dataset
  - *From: Benjimon*

- **AdaptiveGuider vs CFGGuider**
  - AdaptiveGuider 3:07 vs CFGGuider 4:45, AdaptiveGuider faster but CFGGuider has less dots-effect
  - *From: N0NSens*

- **SLG with/without**
  - SLG makes generations more alive and lively
  - *From: JmySff*

- **Image-only LoRAs vs video+image datasets**
  - Image-only datasets cause glitchy look when character moves, need video+image mix
  - *From: Kytra*

- **Offloading impact on diffusion vs LLM performance**
  - Offloading doesn't hurt diffusion performance as badly as LLM performance because diffusion is more compute bound, allowing more time to shift data in background
  - *From: Doctor Shotgun*

- **Looping technique speed vs quality tradeoff**
  - Faster than context windows but not as good quality according to initial testing
  - *From: Kijai*

- **KSampler vs SamplerCustom**
  - KSampler has discard_penultimate_sigma option for specific samplers, making it less noisy than Custom variants
  - *From: Ablejones*

- **fp32 vs fp16 vs fp8**
  - fp16 is the best - fp32 not worth it
  - *From: Kijai*

- **uni_pc vs res multi vs gradient estimation samplers**
  - Personal preferences vary - uni_pc works well on Wan model
  - *From: TK_999*

- **Multi-GPU vs single GPU**
  - No benefit to adding more than 4 GPUs due to too much data transfer between them
  - *From: aikitoria*

- **Different flash-attention compilation methods**
  - pip install . takes 5 minutes instead of 2 hours compared to python setup.py
  - *From: Juampab12*

- **14b vs 1.3b model quality**
  - 14b outperforms HunyuanVideo with right parameters, but 1.3b is much faster
  - *From: Fawks*

- **1.3b model speed vs quality tradeoff**
  - 1.3b much better for spacepxl's use case, 1.3b gens take ~20 seconds vs minutes
  - *From: spacepxl*

- **5090 vs 4090 performance**
  - 5090 is 40% faster or more, with additional benefits from more memory allowing less offloading
  - *From: Kijai*

- **Wan depth control vs other models**
  - First time seeing logical transitions between almost identical frames on a local model
  - *From: Juampab12*

- **Start/End frame vs proper interpolation**
  - Not a proper interpolation as model isn't trained for that - never reaches end frame perfectly but can pull towards it well with some image pairs
  - *From: Kijai*

- **Using one image vs both images for dual embedding**
  - Situational - on some images it was worse with both, sometimes single image works better
  - *From: Kijai*

- **GGUF vs FP8 quality**
  - GGUF produces clearer, nicer output than FP8 models
  - *From: AJO*

- **WAN diffusion cache vs TeaCache**
  - WAN uses two-tier architecture and phase-aware caching vs TeaCache's uniform approach
  - *From: fredbliss*

- **umT5 vs other text encoders**
  - umT5 shows best performance with strongest multilingual capabilities and faster convergence
  - *From: fredbliss*

- **PCIe 8x vs 16x performance**
  - Almost no difference in block swapping performance between 8x and 16x PCIe
  - *From: Benjimon*

- **DDR5 vs DDR4 impact**
  - No effect on speed between DDR5 and DDR4 for WAN generation
  - *From: Benjimon*

- **FP32 vs FP16 quality and speed**
  - FP32 shows more realistic movement (cat example), minimal speed difference (72.89s vs 66.09s per iteration)
  - *From: Benjimon*

- **Sage vs default speed/quality**
  - Sage is twice as fast but not half quality, good balance especially for single GPU
  - *From: Kijai*

- **Linux vs Windows for AI workflows**
  - Linux much better for AI, easier package installation, better memory management, Windows has shared memory advantage
  - *From: Multiple users*

- **DepthCrafter vs DepthAnything**
  - DepthCrafter superior for depth LoRA input, significant quality impact
  - *From: David Snow*

- **1.3B vs 14B model performance**
  - 14B doesn't work with loop_args, context window uniform loop works but extremely slow
  - *From: Kijai*

- **DepthCrafter vs DepthAnythingV2**
  - DepthCrafter outputs consistently better results
  - *From: David Snow*

- **Sage vs Flash attention**
  - Sage is faster and better than flash
  - *From: Flipping Sigmas/Benjimon*

- **Depth + source blended vs pure depth controlnet**
  - Depth blended with source at 0.5 produces more natural colors
  - *From: David Snow*

- **Different controlnet combinations (depth, canny, lineart)**
  - Anime lineart works well standalone, depth+canny combination also effective
  - *From: VK (5080 128gb)*

- **14B vs 1.3B models**
  - 14B is about 30% better quality but 10x the computational cost, not a great deal
  - *From: spacepxl*

- **Native Hunyuan vs Hyvid wrapper**
  - Native Hunyuan is better, Hyvid I2V is way worse
  - *From: Kijai*

- **480p vs 720p model sizes**
  - Both models are same size despite resolution difference
  - *From: VK*

- **Wan vs Hunyuan for I2V**
  - Wan has no contest for I2V - quality on par or higher, prompt adherence much better. Wan twice as slow per step but more efficient overall
  - *From: Kijai*

- **Wrapper vs Native for stability**
  - Wrapper output is far more stable than native, but takes much longer to generate
  - *From: David Snow*

- **Native vs Wrapper for single GPU I2V capacity**
  - Native allows 61 frames on single GPU vs wrapper's 21 frames before OOM on 14B model
  - *From: VK (5080 128gb)*

- **16fps vs 24fps efficiency**
  - 16fps in 81 frames is more efficient than 24fps in 129 frames since you only sample 81 steps, can interpolate to 24fps after
  - *From: Kijai*

- **CFG Zero Star vs baseline**
  - Zero Star shows substantial differences, fixes movement and stabilizes hands
  - *From: Cseti*

- **GPT 4o native image generation quality**
  - Absolutely insane quality, 'we are done for'
  - *From: Juampab12*

- **Zero Star with/without zero init**
  - Zero init completely ruins I2V output but works for T2V
  - *From: Kijai*

- **Fun InP vs regular Wan**
  - Fun is about 200 seconds slower than regular Wan but seems to have better effects
  - *From: H（4090）*

- **1.3B vs 14B models for speed**
  - 1.3B is really fast compared to 14B, making 14B less appealing for many use cases
  - *From: David Snow*

- **Wan 1.3B vs CogVideoX 2B**
  - Wan 1.3B superior to CogVideoX 2B
  - *From: VK (5080 128gb)*

- **Wan control vs CogVideoX-Fun control**
  - Much better than CogVideoX-Fun, result is crazy good
  - *From: Excai*

- **1.3B InP vs 14B InP**
  - 1.3B InP is far worse than 14B
  - *From: Excai*

- **SLG effectiveness on 1.3B vs other models**
  - SLG may work better on original models than 1.3B InP
  - *From: Excai*

- **1.3B vs 14B Fun InP models**
  - Very close quality, main difference is 1.3B is much faster since it doesn't take all day
  - *From: Kijai*

- **New Fun InP vs old I2V models**
  - Old 14B I2V absolutely better than new InP models for regular I2V, but InP models better for start/end frame functionality
  - *From: Kijai*

- **Fun 14B vs Wan 2.1 720p i2v**
  - Official demo first try was pretty bad compared to wan 2.1
  - *From: Benjimon*

- **Euler vs UniPC after fix**
  - Euler is slightly better than UniPC or at least comparable after Kijai fixed euler code mistake
  - *From: David Snow*

- **Euler vs UniPC samplers**
  - Kijai's improved euler seems better than unipc for motion quality
  - *From: David Snow*

- **res_multistep vs uni_pc in native**
  - res_multistep is better than uni_pc, which has weird sigma handling hacks
  - *From: Ablejones*

- **1.3B vs 14B Fun Control models**
  - No major noticeable difference between 1.3B and 14B for Fun Control workflows
  - *From: DiXiao*

- **14B vs 1.3B LoRA compatibility**
  - 14B model works better with LoRAs from original Wan, not as good for 1.3B
  - *From: DawnII*

- **Fun 1.3B vs 480 i2v model**
  - 480 i2v model feels better at first glance for image-to-video tasks
  - *From: A.I.Warper*

- **Wan vs LTX-Video**
  - LTX-Video did a cleaner job in November than current Wan model for certain outputs
  - *From: VK (5080 128gb)*

- **Wan vs Hunyuan keyframe LoRA**
  - Wan's start/end frame control works better than Hunyuan's keyframe LoRA
  - *From: seitanism*

- **Fun InP vs standard I2V**
  - Fun InP only better at things base Wan can't do, control model is more interesting
  - *From: Kijai*

- **Multiple GPU performance**
  - Replicate achieves 40 seconds for 81 frames 480p 30 steps, probably using multiple GPUs
  - *From: Draken*

- **GPU performance hierarchy**
  - B200 > H100 > RTX Pro 6000 > 5090 > 4090. Multiple 3090s best flops/$ unless need fp8
  - *From: aikitoria*

- **RTX Pro 6000 vs multiple 5090s**
  - One Pro 6000 costs same as 2-3 5090s, collective 5090s have more flops if parallelizable
  - *From: aikitoria*

- **I2V model vs normal Wan for start+end frame**
  - Normal Wan is better for start+end frame usage
  - *From: ArtOfficial*

- **TeaCache vs TaylorSeer cache**
  - TeaCache better quality and uses less VRAM than TaylorSeer
  - *From: Kijai*

- **20 vs 100 steps**
  - 20 steps looks identical to 100 steps
  - *From: Juampab12*

- **4090 48GB vs normal 4090**
  - 48GB version only faster for training, not inference
  - *From: Benjimon*

- **Attention methods ranking**
  - sdpa > sage > flash > xformers for attention
  - *From: Benjimon*

- **Wan vs SD1.5 impact**
  - Wan is to Video, what SD1.5 was to image generation
  - *From: ramonguthrie (4080 16GB) 🇬🇧*

- **TeaCache vs TaylorSeer quality**
  - TaylorSeer quality drop is way higher than with TeaCache
  - *From: Kijai*

- **480p vs 720p model performance**
  - 480p model seems to have better motion than the 720p one
  - *From: Juampab12*

- **1.3B Fun Control vs 14B Fun Control**
  - 1.3B has much stronger control signal and better results
  - *From: Kijai*

- **RTX 6000 Pro vs H100**
  - RTX 6000 Pro is about 2/3 as fast as H100 or closer to half depending on H100 variant
  - *From: aikitoria*

- **5090 vs 4090 performance**
  - 30-40% improvement on 5090, not the minimal gains shown in some benchmarks
  - *From: Kijai*

- **Fun InP I2V vs regular Wan I2V**
  - Fun InP has been better for many users
  - *From: DawnII*

- **Native vs Wrapper quality**
  - Wrapper produces far more stable outputs, especially for videos with fast motion. Native sometimes has worse quality for unknown reasons
  - *From: David Snow*

- **1.3B model quality improvement**
  - 1.3B model is now very good for V2V with LoRAs, achieving great quality at 8 steps
  - *From: David Snow*

- **Comfy RoPE vs default RoPE**
  - Comfy RoPE is faster and uses less memory, no quality difference just slight variation
  - *From: Kijai*


## Tips & Best Practices

- **Use maximum context window (81 frames) for best results due to overlap**
  - Context: For window blending in long video generation
  - *From: Kijai*

- **Don't need block swap with 1.3B model on decent VRAM**
  - Context: Small model fits in VRAM without swapping blocks
  - *From: seitanism*

- **Monitor VRAM usage to optimize block swap settings**
  - Context: Use task manager to check actual VRAM usage during generation
  - *From: seitanism*

- **Translating prompts to Chinese doesn't seem to help**
  - Context: Google translate to Chinese didn't improve results
  - *From: Doctor Shotgun*

- **Aim for 81 frames or more and 30+ steps for good results**
  - Context: Wan is a slow model that needs sufficient frames and steps
  - *From: Shawneau 🍁 [CA]*

- **Use double-pass generation instead of just increasing steps**
  - Context: Better quality results with 2x20 steps vs single 40 step pass
  - *From: David Snow*

- **Stick to 81 frames or under for best quality**
  - Context: Model's default is 81 frames, going over causes artifacts
  - *From: Kijai*

- **Use fp8 weights with fp16 calculations for optimal performance**
  - Context: Avoid bf16 weights with fp16 calculations as it's lossy
  - *From: Kijai*

- **Use fp16_accumulation for best quality**
  - Context: When running WAN models with latest ComfyUI optimizations
  - *From: comfy*

- **Switch to UniPC sampler and add enhance a video node**
  - Context: For significant quality improvement in V2V workflows
  - *From: David Snow*

- **Use 0.2 denoise for cleanup passes**
  - Context: When doing v2v cleanup with low denoise
  - *From: Draken*

- **Run denoise pass to help with first frame artifacts**
  - Context: When first frame of I2V generation has artifacts
  - *From: Doctor Shotgun*

- **Use wrapper for better size flexibility**
  - Context: When working with non-standard resolutions
  - *From: T8star-Aix*

- **Use CFG exactly 1.0 to skip uncond and speed up generation**
  - Context: When using CFG scheduling
  - *From: Kijai*

- **Prompt for motion direction on looping content**
  - Context: When generating videos that might loop
  - *From: Kijai*

- **Use Wan 1.3B for both passes instead of Hunyuan second pass**
  - Context: Two-stage upscaling workflow
  - *From: David Snow*

- **Set batch count high with wildcards for continuous generation**
  - Context: When wanting to generate videos non-stop
  - *From: Cubey*

- **Use animated masks to control denoise per frame**
  - Context: Alternative to static masking for video control
  - *From: TK_999*

- **Use TeaCache for previewing, then disable for final high quality**
  - Context: TeaCache doesn't generally change motion and composition, so you can preview fast then run again without TeaCache for quality
  - *From: Kijai*

- **Kids can spot AI generated videos by looking at hair details**
  - Context: 11 year old could instantly identify Trump/Zelensky AI videos as fake by examining the hair
  - *From: fredbliss*

- **Balance TeaCache settings for quality vs speed**
  - Context: Find balance where it looks better than without TeaCache and is faster at the same time
  - *From: seitanism*

- **Use specific camera movement language in prompts**
  - Context: For cinematic effects, use phrases like 'camera gradually zooms out', 'camera slowly zooms in' to get proper camera movements
  - *From: VRGameDevGirl84*

- **TeaCache works best for portrait/halfbody shots**
  - Context: Quality difference minimal for close-up shots, more noticeable for complex scenes
  - *From: slmonker*

- **Use 0.2-0.3 denoise for upscaling with 1.3B model**
  - Context: When doing second pass upscaling from first generation
  - *From: N0NSens*

- **Don't use same seed for upscaling**
  - Context: Different noise needed for upscaling workflows, seed doesn't matter much
  - *From: TK_999*

- **Reference original image in I2V upscaling**
  - Context: When upscaling I2V, reference the original image again rather than just the generated video
  - *From: Cubey*

- **Use shorter positive prompts for better results**
  - Context: Wan generates better video when positive prompt is shorter
  - *From: for1096*

- **Keep negative prompt tags for quality**
  - Context: Removing the 28 negative prompt tags from workflow decreases quality
  - *From: for1096*

- **Use lanczos for upscaling in pixel space**
  - Context: If you don't use upscale model to do the upscaling, use lanczos to upscale in pixel space
  - *From: Kijai*

- **Both short and long prompts work well**
  - Context: Both very long and very short hints seem to work well with 1.3B model
  - *From: DiXiao*

- **Use aria2c for faster downloads**
  - Context: aria2c -j 1 -x 16 -s 16 -o makes downloads 1600% faster, requires good CPU
  - *From: deleted_user_2ca1923442ba*

- **Use structured prompts for better I2V results**
  - Context: When I2V workflows are hallucinating instead of following prompts
  - *From: fredbliss*

- **Use -> syntax for scene transitions**
  - Context: Prompting technique: 'old man gets up and walks away into the sea -> a shark attacks the old man -> huge explosion'
  - *From: Kijai*

- **Start TeaCache after initial noise removal**
  - Context: TeaCache can have false hits during early denoising steps
  - *From: Kijai*

- **Use 1440×1440 resolution for clearer I2V results**
  - Context: Higher resolution improves face consistency and overall quality, generation time about 50 minutes on 4090 24GB
  - *From: BNP4535353*

- **Can still use fp8 weights with fp16_fast**
  - Context: Combines speed benefits without major quality degradation
  - *From: Kijai*

- **Enable RifleX at setting 4 for better motion stability**
  - Context: Improves ground stability and reduces sliding artifacts
  - *From: Kijai*

- **Use 30 steps minimum for good quality**
  - Context: For WanVideo generation
  - *From: TK_999*

- **Use Chinese negative prompt for best results**
  - Context: Default Chinese negative works well, though English translations also work
  - *From: TK_999*

- **Don't go higher than 0.05 for TeaCache**
  - Context: 0.15 is too much, causes quality issues
  - *From: Kijai*

- **Use 848x480 resolution for good results**
  - Context: Can go lower if needed for VRAM
  - *From: TK_999*

- **Use percentage-based start/end parameters for teacache**
  - Context: More intuitive than step numbers, prevents users from not adjusting settings
  - *From: Kijai*

- **Higher steps (30) can give worse motion than lower steps (15) for I2V**
  - Context: Similar to Hunyuan behavior, may need to adjust shift parameter
  - *From: osfortuna*

- **DPM++ works better for anime, Euler works better for real people**
  - Context: Scheduler selection based on content type
  - *From: Miku*

- **Use resolutions divisible by 32**
  - Context: Model prefers 832x480 over other resolutions, some scripts error if outside this
  - *From: Benjimon*

- **Use 81 frames for optimal results**
  - Context: Any other frame count is suboptimal with this model
  - *From: Kijai*

- **Refresh browser after node updates**
  - Context: Even if you restart ComfyUI, nodes won't update without browser refresh
  - *From: Kijai*

- **Consider time vs quality tradeoffs**
  - Context: If optimizations finish in half time, adjust other settings like step count to offset quality loss
  - *From: Kijai*

- **Use pixel space upscaling with encode again**
  - Context: Don't try to pass video directly as latents, upscale in pixel space and encode again
  - *From: Kijai*

- **Use poop emoji in negative prompt**
  - Context: With umt5 model, adding poop emoji to negative prompt can improve results
  - *From: Juampab12*

- **Use matching dtypes**
  - Context: Don't mix weights, choose matching dtype for better compatibility
  - *From: Kijai*

- **Put base_precision to fp16 or bf16, make quantization match fp8 weight**
  - Context: When using fp8 weights, base_precision is what calculations are done at and can't be fp8
  - *From: Kijai*

- **Use euler + normal scheduler combination for low steps**
  - Context: Better than UniPC for low step counts, for higher steps euler + normal looks more natural on real people
  - *From: Miku*

- **Increase start value for TeaCache stability**
  - Context: When getting problematic results, increase start value to make image much more stable
  - *From: JmySff*

- **Use 1280x720 resolution for 720p model**
  - Context: 720p model needs very large resolution to work properly
  - *From: Kijai*

- **Use default Chinese negative prompt for best results**
  - Context: Better than empty negative
  - *From: Kijai*

- **TeaCache works better with more steps**
  - Context: With 10 steps use 0.5-0.6 start, with 20+ steps can use 0.2
  - *From: Miku*

- **Don't start teacache at 0**
  - Context: If it skips 2nd step generation is ruined
  - *From: Kijai*

- **Use descriptive time-lapse prompts**
  - Context: Detail the progression stages for better time-lapse results
  - *From: TK_999*

- **Search nodes with double-click in blank space**
  - Context: Alternative to right-click node menu
  - *From: Juampab12*

- **Use noise augmentation of 0.02 for I2V to increase motion**
  - Context: Realistic content that needs more action and movement
  - *From: Juampab12*

- **Disable adjust_resolution for exact dimension control**
  - Context: When using I2V workflows and need precise resolution matching
  - *From: Kijai*

- **Use adaptive guidance for cfg=1 speed boost**
  - Context: To optimize generation speed without quality loss
  - *From: TK_999*

- **Don't combine TeaCache with context windowing**
  - Context: Will cause noise artifacts and compatibility issues
  - *From: Kijai*

- **Keep I2V prompts simple and use camera directions**
  - Context: For img2vid workflows, simple prompts work better and the model listens to camera movement instructions
  - *From: The Shadow (NYC)*

- **Use mostly same prompt and change small bits for context windows**
  - Context: When using multiple prompts with |, keep the core prompt the same and only change specific elements like 'old man is laughing|old man is crying'
  - *From: Kijai*

- **Each context window needs full context, not just 'what happens next'**
  - Context: Don't think of multiple prompts as sequential story beats, each window needs complete scene description
  - *From: Kijai*

- **Start TeaCache later to avoid quality degradation**
  - Context: Starting TeaCache at the beginning can hurt quality, better to start it later in the process
  - *From: Cubey*

- **Remove unnecessary nodes from workflows**
  - Context: The threshold note for frames under 81 is no longer needed since the hardcoded limit was resolved
  - *From: Miku*

- **Avoid block swap if possible**
  - Context: As soon as you go from 0 block swap to any, it slows down a lot
  - *From: deleted_user_2ca1923442ba*

- **Use 'free model and node cache' button instead of restarting**
  - Context: Alternative to restarting ComfyUI to clear memory
  - *From: Screeb*

- **Take last frame as image instead of first**
  - Context: When making images, first frame might not be the best - consider using last frame
  - *From: deleted_user_2ca1923442ba*

- **Reduce fps by half then interpolate for faster upscaling**
  - Context: Select every 2nd frame to make it 2x faster, then use RIFE interpolation. Generate at 8fps then upscale rather than upscaling all frames
  - *From: Juampab12*

- **Use one less prompt than context window**
  - Context: Found better results having one less prompt than context window size
  - *From: Cubey*

- **Use percentage for teacache in native vs step numbers in wrapper**
  - Context: Native version uses percentage that gets rounded to int, wrapper uses direct step values which is less confusing for experienced users
  - *From: Kijai*

- **For FPS interpolation, ensure fps * interpolation factor = final fps**
  - Context: Mathematical rule for proper FPS interpolation setup
  - *From: fredbliss*

- **Lower teacache threshold and start earlier for better results**
  - Context: When encountering teacache artifacts
  - *From: Kijai*

- **Use GIMM-VFI instead of Film VFI for better interpolation**
  - Context: For frame interpolation workflows
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Try interpolating Wan output to 25fps using OpticalFlow in Premiere**
  - Context: Working with 16fps timeline and exporting with optical flow interpolation
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Disable 'enhance a video' for better results**
  - Context: Testing showed better output without video enhancement
  - *From: VRGameDevGirl84(RTX 5090)*

- **Use vram_management node to prevent freezing**
  - Context: For 4070 12GB VRAM, prevents 98% VRAM usage and freezing
  - *From: for1096*

- **For car/fast action videos use lower motion smoothness**
  - Context: motion_smoothness = 0.2 (lower) should work better for fast action
  - *From: fredbliss*

- **Use two-pass generation for speed**
  - Context: Generate first pass at half size, then upscale and feed into second sampler with 1.3B model. Reduces time from 1200s to 310s per gen
  - *From: David Snow*

- **Start with 1.3B model for learning**
  - Context: 1.3B model is much quicker than 14B and incredibly good for its size, though lacks image-to-video
  - *From: Screeb*

- **Use GGUF files for 14B I2V**
  - Context: 14B I2V may need GGUF files loaded with GGUF loader to manage memory
  - *From: Screeb*

- **Turn off block swap with high VRAM**
  - Context: Block swap is a VRAM saving feature that adds time - disable when you have sufficient VRAM
  - *From: Cubey*

- **Match model resolution to target**
  - Context: 480p models optimized for 480p generation, 720p for 720p. Use corresponding model for best results
  - *From: Screeb*

- **Use animated preview in VHS settings**
  - Context: Crucial with video models to cancel long generations if they're going wrong
  - *From: AJO*

- **Save intermediate steps during workflow development**
  - Context: Can save to /tmp/ folder to preserve workflow state without cluttering main output
  - *From: Juampab12*

- **For quick testing, VAE decode early to see blurry preview**
  - Context: Can tell how generation will go from early blurry results, useful since no taesd for video models yet
  - *From: deleted_user_2ca1923442ba*

- **Disable all offloading to maximize speed with high VRAM**
  - Context: For users with 48GB+ VRAM, turn off block swapping and keep models on main_device
  - *From: Juampab12*

- **Use Chinese negative prompt for I2V workflows**
  - Context: It seemed to improve things in I2V generation
  - *From: David Snow*

- **Translate positive prompts to Mandarin**
  - Context: For better video generation results
  - *From: Colin*

- **Use powers of 2 for interpolation**
  - Context: Factors of 2 will generally be best. Interp models are trained to generate halfway between images - 2x, 4x, 8x etc work best
  - *From: Benjaminimal*

- **Try translating camera motion prompts to Mandarin**
  - Context: When having trouble with camera movement prompts in English
  - *From: Benjaminimal*

- **Install VHS suite and enable animated previews**
  - Context: To see if generation is working during inference instead of finding out after
  - *From: Cubey*

- **Use CPU with integrated graphics for Linux builds**
  - Context: Save all VRAM for compute, Linux display drivers are problematic
  - *From: Shawneau 🍁 [CA]*

- **Use verbose option in context settings**
  - Context: Prompt travel info moved behind verbose option to not spam console
  - *From: Kijai*

- **Use overlap of 24 for 81 context for I2V runs**
  - Context: Best setting for context window overlap
  - *From: Cubey*

- **Use Topaz Chronos to interpolate Wan results to 60fps for better motion**
  - Context: When Wan's lower fps motion needs improvement
  - *From: aikitoria*

- **Manually select best frames for endless I2V chains**
  - Context: To avoid degradation when chaining multiple I2V generations
  - *From: Draken*

- **Use thermal cameras to verify cable safety**
  - Context: When running high-power GPU setups to prevent fire hazards
  - *From: aikitoria*

- **Experiment with --ring_size vs --ulysses_size parameters**
  - Context: For optimizing multi-GPU setups, especially 8xGPU configurations
  - *From: intervitens*

- **Use Chinese prompts with English commas for Hunyuan**
  - Context: Chinese generates better video but Chinese commas confuse the model
  - *From: for1096*

- **Use masks and LoRA hook system for multiple character consistency**
  - Context: To prevent character bleeding when using multiple LoRAs in same scene
  - *From: spacepxl*

- **Use Topaz interpolation for low FPS**
  - Context: 16fps output can be interpolated to 60fps nearly perfectly
  - *From: aikitoria*

- **Start TeaCache later with lower values**
  - Context: More conservative approach better than aggressive early start
  - *From: HeadOfOliver*

- **Add 'the camera is static' to end of prompts**
  - Context: Prevents unwanted camera movement in generations
  - *From: Faust-SiN*

- **Give specific pose guidance instead of vague prompts**
  - Context: Instead of just 'poses', specify breathing, leaning, fidgeting, modeling photoshoot, etc.
  - *From: Benjaminimal*

- **Use rgthree bookmarks to jump around quickly in workflows**
  - Context: For keeping workflows clean and navigable
  - *From: Gateway {Dreaming Computers}*

- **Set RIFE to clear cache every 10 frames**
  - Context: Prevents OOM when using RIFE interpolation
  - *From: AJO*

- **Generate video via VAE decode first, then interpolate separately**
  - Context: Better workflow: VAE decode → save video → interpolate → save interpolated video
  - *From: Juampab12*

- **Low steps (10-15, maybe 20) require high shift like 7-9**
  - Context: For getting good results with fewer sampling steps
  - *From: Miku*

- **Use real data instead of synthetic for CFG distillation**
  - Context: When training CFG distillation, works better and doesn't pick up bias if data samples > training steps
  - *From: spacepxl*

- **Don't change context stride, leave at 4**
  - Context: Context stride doesn't work well with Wan models
  - *From: Kijai*

- **Use coefficients with TeaCache**
  - Context: TeaCache values are different for 1.3B models when using coefficients
  - *From: Kijai*

- **V2V is just replacing empty latent with VAE encoded video**
  - Context: For video-to-video workflows
  - *From: Doctor Shotgun*

- **Use VHS node to output MP4 directly**
  - Context: Avoid heavy image format memory issues in ComfyUI
  - *From: Doctor Shotgun*

- **Check torch version after updating nodes**
  - Context: Some requirements.txt files aren't great and can cause issues
  - *From: ArtOfficial*

- **Use kubuntu if just starting with Linux**
  - Context: For users transitioning from Windows
  - *From: Benjimon*

- **Use resolutions divisible by 32 for better results**
  - Context: Some models require specific divisibility
  - *From: Benjimon*

- **Don't use models outside their trained resolution parameters**
  - Context: Quality degrades significantly
  - *From: Colin*

- **Be mean and direct with Claude for coding tasks**
  - Context: When using Claude AI for script generation
  - *From: Benjimon*

- **Use 480p I2V model for all renderings below 720p**
  - Context: Best model choice for sub-720p content
  - *From: JmySff*

- **Set block swap to use almost all VRAM, leave 1GB free**
  - Context: Monitor in nvtop or task manager when configuring
  - *From: Benjimon*

- **Can try various resolutions as long as divisible by 16**
  - Context: Model handles weird resolutions well
  - *From: Benjimon*

- **Use SageAttention for best speed with least negative effect**
  - Context: Performance optimization
  - *From: Benjimon*

- **Put torch.compile patch last when using multiple patches**
  - Context: When combining with TeaCache and other optimizations
  - *From: Kijai*

- **Generate at 480x480 then crop to 16:9 before interpolation**
  - Context: Speeds up generation when person is centered, works well for non-close-up shots
  - *From: VRGameDevGirl84(RTX 5090)*

- **Use enhance a video strength of 0.32 with teacache**
  - Context: Sweet spot setting found through testing
  - *From: JmySff*

- **Reboot ComfyUI if Wan starts to slow down**
  - Context: May help with memory leaks or similar issues
  - *From: N0NSens*

- **Consider upscaling first, then RIFE interpolation**
  - Context: May produce better results than RIFE then upscale
  - *From: burgstall*

- **Train I2V LoRAs at 480p first, then test on 720p model**
  - Context: First training attempt, can finetune at higher res if quality degrades
  - *From: mamad8*

- **Use TeaCache around 0.4 for seed hunting, then bypass for final generation**
  - Context: When doing multiple generations to find good seeds
  - *From: ArtOfficial*

- **Swap right amount of blocks to maximize VRAM usage**
  - Context: Optimal performance - don't overswap
  - *From: Benjimon*

- **Use Chinese prompting when English fails**
  - Context: Wan sometimes struggles with English nouns but responds better to Mandarin
  - *From: Screeb*

- **Set text encoder to fp8 to save RAM**
  - Context: When dealing with memory issues
  - *From: Kijai*

- **Use TeaCache threshold of 0.275-0.3 max, start from step 1**
  - Context: For optimal quality/speed balance
  - *From: Kijai*

- **Less blocks swapped is faster until VRAM gets full**
  - Context: Finding optimal block swap settings
  - *From: Kijai*

- **Quality dataset selection is more important than size**
  - Context: LoRA training - 20 clips can achieve excellent results
  - *From: NebSH*

- **Generate at lower resolution then upscale for better efficiency**
  - Context: Motion and coherence with big model, then details with small model
  - *From: Juampab12*

- **Use fp16-fast precision with fp8 models**
  - Context: Provides speed improvement as card has to upcast everything anyway
  - *From: Juampab12*

- **Train LoRAs with 70% target content, 30% diverse data**
  - Context: Prevents overfitting on small models, especially effective for 1.3B model
  - *From: fredbliss*

- **Refresh browser after git pull to see updated nodes**
  - Context: ComfyUI may cache old node versions
  - *From: Kijai*

- **Use more data for LoRA training - more data is more better**
  - Context: No reason not to use lots of data for LoRA training
  - *From: spacepxl*

- **Use 9 or 13 frames for video LoRA training**
  - Context: Works really well and doesn't need many frames
  - *From: spacepxl*

- **Video data is better than images for LoRA training**
  - Context: Can learn motion and consistency
  - *From: spacepxl*

- **Control LoRA strength by changing denoise strength and blur size**
  - Context: For making upscaling less creative
  - *From: spacepxl*

- **Use Target CFG 6.5-7 instead of 10, adjust CFG rather than denoise for control**
  - Context: Target CFG 4.5 barely noticeable, 7+ is lot of changes
  - *From: Kytra*

- **Transformer models seem to be more about composition on earlier blocks**
  - Context: For controlling LoRA strength with block configurations
  - *From: Kijai*

- **Higher steps use lower shift, lower steps use higher shift**
  - Context: Steps 50 try shift 3-5-6, steps 20 try shift 7-9-11
  - *From: HeadOfOliver*

- **Keep smallest edge at 480 or 720 depending on model**
  - Context: 16:9 may result in slightly better results but others still work
  - *From: DevouredBeef*

- **Use teacache 0.3 for faster prompt/seed finding**
  - Context: Takes 7.5 minutes but has noticeable artifacts, good for testing
  - *From: intervitens*

- **Manually raise fan speed to 80-90% for training**
  - Context: Helps with thermal management during intensive workloads
  - *From: spacepxl*

- **Disable adjust_resolution if you want exact dimensions**
  - Context: When you want precise control over output dimensions
  - *From: Kijai*

- **Few MLP layers between control image and model work well**
  - Context: Like LLaVA or ELLA approach for control architectures
  - *From: deleted_user_2ca1923442ba*

- **Use soft mask + differential diffusion with tile LoRA**
  - Context: For early steps at half strength, then switch tile off for end steps, works better than hyloom
  - *From: spacepxl*

- **Use CFG distill LoRA at 1.0 strength**
  - Context: Stacks fine with other LoRAs and provides significant speedup
  - *From: spacepxl*

- **Power limit GPU to 80% for stable performance**
  - Context: Reduces thermal throttling and provides more stable clocks
  - *From: HeadOfOliver*

- **Check perfcap reason in GPU-Z for throttling diagnosis**
  - Context: When GPU usage isn't at 100%, use GPU-Z to identify what's limiting performance
  - *From: Kijai*

- **Use Chinese prompts and negative prompts for better results**
  - Context: WAN model responds better to Chinese language prompts
  - *From: BestWind*

- **Use TeaCache as preview method**
  - Context: TeaCache doesn't change results too much so you can run again without it for final output
  - *From: Kijai*

- **Use Joy Caption for images and simple keywords for videos in LoRA training**
  - Context: For WAN LoRA training dataset preparation
  - *From: Juampab12*

- **Don't train multiple characters in same LoRA**
  - Context: Single character LoRAs work better than multi-character ones
  - *From: Juampab12*

- **Set spline editor interpolation to step-after for CFG scheduling**
  - Context: When using CFG distillation workflow
  - *From: Kijai*

- **Use 0.18-0.2 TeaCache threshold for better quality**
  - Context: Lower values provide better quality than the previous 0.22 recommendation
  - *From: intervitens*

- **Disable TeaCache for big motion content**
  - Context: TeaCache breaks with large motion and may waste time requiring multiple generations
  - *From: Payuyi*

- **Use 3-5 sentences for prompting**
  - Context: Can work with one-liners or long prompts, but 3-5 sentences is probably best
  - *From: TK_999*

- **Set CFG steps to 15-20 for speed boost**
  - Context: Disabling CFG after 15-20 steps provides 2x speedup with minimal quality loss
  - *From: intervitens*

- **Use patch node with torch compile + LoRA**
  - Context: Compile stops LoRA from loading without the patch node
  - *From: Kijai*

- **Use traditional video denoisers after upscaling**
  - Context: Cleans up VAE noise effectively - basic denoise in Nuke or similar software
  - *From: spacepxl*

- **Full 1.0 strength works better than reduced strength for upscaling**
  - Context: Tile LoRA works better at full strength than reduced
  - *From: spacepxl*

- **Blur input correctly for tile LoRA**
  - Context: 10-15px blur at sigma 0.3 using native blur node, same regardless of resolution
  - *From: spacepxl*

- **Try slow motion LoRA for longer videos**
  - Context: Train 50% speed LoRA and generate 8fps video for effectively 2x longer content
  - *From: Juampab12*

- **Use STG on layer 10 for quality improvement**
  - Context: Skip layer guidance on unconditioned inference, particularly effective on layer 10
  - *From: Juampab12*

- **Use fp32 VAE for slightly better encoding quality**
  - Context: When you have enough VRAM available
  - *From: Kijai*

- **Enable fp16 accumulation for better performance**
  - Context: Add torch.backends.cuda.matmul.allow_fp16_accumulation = True with nightly torch
  - *From: Kijai*

- **Test with 5 or 9 frames for faster iteration**
  - Context: Good for testing samplers, steps, denoise strength, prompts - doesn't show motion well but much faster
  - *From: spacepxl*

- **Avoid prompting for confetti**
  - Context: Causes 'wan dots explosion' artifacts due to high information content
  - *From: Draken*

- **Use structured prompts for better results**
  - Context: YAML-like format with character, action, location, style sections works well
  - *From: fredbliss*

- **Use SLG on negative conditioning to preserve good motion**
  - Context: Skip layer 10 in negative conditioning - if negative happens to make good motion, don't treat that as negative
  - *From: TK_999*

- **Run control lora to 1.0 to keep original image**
  - Context: For maintaining original image characteristics when using control loras
  - *From: Kijai*

- **Duplicate frames 4x in pixel space before encoding for VAE quality**
  - Context: When frames are highly different in a latent, improves VAE quality significantly
  - *From: Benjaminimal*

- **Use structured prompt format for better results**
  - Context: [Subject], [Setting], [Style], [Camera], [Mood] format works well with the model
  - *From: fredbliss*

- **Compare 2nd run when testing compile to avoid compilation time in timing**
  - Context: Always compare second run with compile enabled so compilation time doesn't skew performance measurements
  - *From: Kijai*

- **Use Console Debug node to output tokens from text encode**
  - Context: For debugging token processing in text embeddings
  - *From: fredbliss*

- **Put compile node always last**
  - Context: Enhance and TeaCache nodes modify model code, so compile after them
  - *From: Kijai*

- **Lower threshold for SkipLayerGuidanceDiT to reduce morphing effects**
  - Context: When getting Matrix Agent morphing on hands/faces at higher frame counts
  - *From: Kijai*

- **End SkipLayerGuidanceDiT very early to avoid slowdown**
  - Context: For Hunyuan usage - it's more like STG and slows down
  - *From: Kijai*

- **Add 'live action' to prompt for better superhero results**
  - Context: When generating characters like Supergirl that the model struggles with
  - *From: seitanism*

- **Use GGUF 8 Wan 480p for best quality/speed balance**
  - Context: For long video generation workflows
  - *From: AJO*

- **Use skip layer guidance value of 9**
  - Context: General SLG usage
  - *From: kendrick*

- **Start SLG at 0.1 for 1.3B model**
  - Context: Better quality results with 1.3B variant
  - *From: Kijai*

- **Use sharpest frame from last 10 frames for video extension**
  - Context: Video continuation workflow
  - *From: Benjimon*

- **Disable xformers to use flash attention**
  - Context: Need to use --disable-xformers flag
  - *From: Doctor Shotgun*

- **Use git pull instead of ComfyUI manager for updates**
  - Context: Manager doesn't always pull latest commits
  - *From: Kijai*

- **Cut LoRA strength in half if getting no motion**
  - Context: When LoRAs kill motion entirely
  - *From: Flipping Sigmas*

- **Disable LoRA blocks for image-trained LoRAs**
  - Context: When image LoRAs reduce motion too much
  - *From: Kijai*

- **Don't apply SLG to first steps for 1.3B model**
  - Context: Initially felt useless for 1.3B but works better when not applied to early steps
  - *From: Kijai*

- **Use blocks 9 or 10 for SLG with 14B models**
  - Context: Good starting points for Skip Layer Guidance
  - *From: Kijai*

- **Search Kijai's recent posts when in doubt**
  - Context: Quick way to find latest information and updates
  - *From: Flipping Sigmas*

- **Use enhancer LoRA with 20-30 steps on Wan 1.3B**
  - Context: For improving video quality
  - *From: VRGameDevGirl84(RTX 5090)*

- **For shots with lots of people, render them separately then composite in After Effects**
  - Context: Better results than trying to generate everything together
  - *From: happy.j*

- **Extract sharpest frame from last few frames for video extension**
  - Context: When extending videos to avoid quality issues
  - *From: Benjimon*

- **Disable corresponding LoRA blocks when using SLG on those same blocks**
  - Context: Significantly improves output quality, though may increase slow-motion effect
  - *From: BondoMan*

- **Use WSL2 instead of Windows native for 20-30% performance boost**
  - Context: For users having installation or performance issues on Windows
  - *From: pagan*

- **Don't use RiFlex patch**
  - Context: Too big quality impact for the performance benefit gained
  - *From: Kijai*

- **Set TeaCache threshold very low to disable**
  - Context: When you want to test without TeaCache, set threshold so low it never triggers
  - *From: Kijai*

- **Use first 20 blocks enabled, turn off singles for LoRAs**
  - Context: Helps with LoRA quality, technique that worked on Hunyuan as well
  - *From: Cubey*

- **Don't lower LoRA strength too much when combining**
  - Context: Found that lowering strength too far on LoRAs made for worse results even when combining multiple
  - *From: Cubey*

- **Use very similar prompts for context windowing**
  - Context: For multiple prompts with | separator to be useful, they should be very similar with small changes
  - *From: Kijai*

- **For I2V static images, describe movement and use more complex descriptions**
  - Context: When video feels static, try phrasing action differently without overdoing verbiage
  - *From: Cubey*

- **Use low res videos + high res images for LoRA training**
  - Context: Caption images as 'an image of...' to counteract motion degradation
  - *From: Juampab12*

- **Generate supporting videos with Kling/Viggle for character LoRAs**
  - Context: Helps preserve model's understanding of character + motion even with low quality videos
  - *From: Kytra*

- **Try different cfg values with SLG**
  - Context: SLG changes how CFG behaves, experiment with different values
  - *From: Kijai*

- **Connect ModelSamplingSD3 to scheduler node**
  - Context: Shift only works when properly connected to have effect
  - *From: Kijai*

- **Use staging prompts for extreme lighting transitions**
  - Context: Instead of direct night-to-day transitions, use intermediary prompts like 'dawn forest with early light' to avoid whiteout effects
  - *From: fredbliss*

- **Increase video length for better transitions**
  - Context: 120+ frames work better than shorter videos for smooth prompt transitions because blend zones occupy smaller percentage
  - *From: fredbliss*

- **Match semantic elements between prompts**
  - Context: Ensure prompts share common elements like 'same trees' to maintain consistency during transitions
  - *From: fredbliss*

- **Use optimize order for better embedding transitions**
  - Context: Nearest neighbor ordering of embeddings can create smoother semantic transitions between prompts
  - *From: fredbliss*

- **Start with max 40 for block swap and reduce if unused VRAM available**
  - Context: For I2V 480 workflow memory optimization
  - *From: Kijai*

- **Higher step counts better for looped videos**
  - Context: 35-45 steps produce better results than lower step counts for looping
  - *From: TK_999*

- **Use SLG with moderation for better results**
  - Context: Video generation quality improvement
  - *From: Kijai*

- **Context windows need minimum 2 windows and overlap should be 16**
  - Context: When using multiple prompts
  - *From: Kijai*

- **Extreme prompt changes don't work well with context windows**
  - Context: red panda|fox transition failed
  - *From: Kijai*

- **I2V context windows work better when not moving camera**
  - Context: Fine for faces, but limited movement
  - *From: Kijai*

- **Use SLG settings of 8 on 1.3B model**
  - Context: Starting bit later and ending bit early works well for 1.3B T2V
  - *From: Kijai*

- **SLG works better on 1.3B than 14B models**
  - Context: Looping doesn't work well with other models than 1.3B and hates TeaCache
  - *From: Kijai*

- **Use enhance video before SLG and torch compile**
  - Context: Before compile if using that, otherwise order doesn't matter
  - *From: Kijai*

- **Context windows work best with 33+ frames**
  - Context: Less than 33 frames gives bad results with context window
  - *From: xwsswww*

- **Remove context windows for longer videos**
  - Context: Don't use context windows and run all frames together for better consistency
  - *From: Cubey*

- **Use Superbadass upscaler for context changes**
  - Context: Works great for removing little colour shift that happens on context changes when extending
  - *From: StableVibrations*

- **Use early step cutoff with depth control LoRA for creative results**
  - Context: When using depth control LoRA
  - *From: spacepxl*

- **Remap depth values to realistic ranges and add gradients for perspective**
  - Context: When creating depth maps for aerial city views
  - *From: spacepxl*

- **Avoid pure black in depth maps, lift to slightly higher values**
  - Context: When using depth control LoRA
  - *From: Kijai*

- **Use cfg 4.0 for first pass and 6.0 for second pass with depth LoRA**
  - Context: Two-pass workflow with depth control
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Use depth + custom lora on early steps, then only custom lora on later steps**
  - Context: When combining multiple LoRAs for better results
  - *From: spacepxl*

- **Set overlap to 17 and turn off freenoise when using VAE with context windows**
  - Context: For better v2v results with context windows
  - *From: Flipping Sigmas*

- **Lower latent strength helps for more natural transitions and better prompt understanding**
  - Context: When using start/end frame workflow
  - *From: IllumiReptilien*

- **Think of SLG more like CFG setting - needs to be set correctly for given model/task**
  - Context: SLG configuration depends on your cfg and other settings
  - *From: Kijai*

- **Use point editor for video masking instead of Florence2**
  - Context: Florence2 is not most reliable for precise face selection in video
  - *From: Kijai*

- **Create video loops by using last frame as first frame and original first frame as last frame**
  - Context: Generate better video loops using start/end frame workflow
  - *From: const username = undefined;*

- **First inpaint object changes with Flux, then generate video**
  - Context: For changing specific objects in video generation workflow
  - *From: Kijai*

- **Use same start/end frame for rotation effects**
  - Context: When creating rotational animations, using identical start and end frames can improve results
  - *From: The Shadow (NYC)*

- **Remove second image clip when using same start+end frames**
  - Context: Helps remove timing offset issues demonstrated in seamless loop attempts
  - *From: The Shadow (NYC)*

- **Use long descriptive prompts for character LoRAs**
  - Context: Include specific trigger words like character name and distinctive features for better LoRA activation
  - *From: Cseti*

- **Clear Triton cache for dependency issues**
  - Context: When encountering import errors related to visual studio or path issues
  - *From: Kijai*

- **Don't use prep clip vision node with tiles**
  - Context: When using tiled clip embed processing, defeats the whole purpose
  - *From: Kijai*

- **Remove first few frames as warmup**
  - Context: WAN paper specifies first frames are for conditioning and should be discarded
  - *From: fredbliss*

- **Set CFG cutoff preference setting**
  - Context: For better CUDA memory management: set 'CUDA - Sysmem Fallback Policy' to 'Prefer No Sysmem Fallback'
  - *From: Benjaminimal*

- **Test optimizations yourself**
  - Context: Quality vs speed is subjective and varies by use case
  - *From: miko*

- **Don't use GGUF unless you need VRAM**
  - Context: GGUF is slower and only beneficial for VRAM savings
  - *From: Faust-SiN*

- **Turn off torch compile for quality**
  - Context: Can cause quality issues in generation
  - *From: Faust-SiN*

- **Use light prompts with camera direction at the end**
  - Context: For better camera control in video generation
  - *From: The Shadow (NYC)*

- **Don't use enhance a video node**
  - Context: May not do anything useful and can cause issues
  - *From: Kijai*

- **Composite result on original with traditional masking in pixel space**
  - Context: When using differential diffusion or latent masking to account for VAE losses
  - *From: Kijai*

- **Use LoadLoraModelOnly instead of running clip through lora**
  - Context: More efficient memory usage
  - *From: ArtOfficial*

- **Fake end frame accuracy by adding last frame to end with cross-fade**
  - Context: Workaround for models that can't reliably hit end frames
  - *From: Kijai*

- **Try different seeds first when troubleshooting generation issues**
  - Context: Before adjusting complex parameters
  - *From: LarpsAI*

- **Try noise_aug_strength value of 0.095 for better I2V results**
  - Context: When having motion quality issues with I2V
  - *From: const username = undefined;*

- **Use 768px768px204f shape over 544px992px204f for better quality**
  - Context: For standard video generation, though I2V version uses 544×992×102f for best fidelity
  - *From: deleted_user_2ca1923442ba*

- **Adjust latent strength in tiled encoder node to reduce camera movement**
  - Context: When trying to keep camera static in I2V workflow
  - *From: Flipping Sigmas*

- **Choose nightly version in ComfyUI manager, not stable version**
  - Context: To get the most recent nodes from Kijai
  - *From: Flipping Sigmas*

- **Can use any latent of right size/frames, doesn't have to be from ip2pcond node**
  - Context: For latent masking workflows
  - *From: spacepxl*

- **Set very low denoise (0.3) when using control LoRA, can do 2 passes**
  - Context: For better control with LoRA workflows
  - *From: Flipping Sigmas*

- **Use superior depthmaps for better controlnet results**
  - Context: When using depth controlnet
  - *From: David Snow*

- **Resize images before inputting to controlnet as it pulls width/height from image**
  - Context: When using controlnet inputs
  - *From: VK (5080 128gb)*

- **TeaCache should be used with limited step range as it slows down the process**
  - Context: When using SLG node with TeaCache
  - *From: Kijai*

- **Disable TeaCache when wanting 100% HQ generation as it skips steps**
  - Context: For final quality outputs vs seed hunting
  - *From: Benjimon*

- **Train face LoRAs using 5-frame videos where last 4 frames are identical due to VAE limitations with 2-frame sequences**
  - Context: LoRA training for face control
  - *From: Juampab12*

- **For looped context, use half the shift as max latents because they're always odd numbers**
  - Context: Default for 49 frames was shift of 6
  - *From: Kijai*

- **Under-shoot rather than over-shoot when setting context shift values**
  - Context: When calculating looped context parameters
  - *From: Kijai*

- **Should still get away with 20 block swap on 4090 with fp8**
  - Context: User had increased to 40 blocks due to slow 1280x720 outputs
  - *From: Kijai*

- **Use 40+ steps instead of 20 for better quality**
  - Context: 20 steps often looks grainy or has weird motion
  - *From: Faust-SiN*

- **Never set CFG to 0.0, use 1.0 to disable since it's a multiplier**
  - Context: When working with CFG settings
  - *From: Kijai*

- **Try different negative image options: same image with noise, just noise, black image, or concept to avoid**
  - Context: For new negative_image clip encode node
  - *From: Kijai*

- **Motion prompts work best with prompt travel, full subject changes bleed too much**
  - Context: When using the new prompt travel feature
  - *From: Kijai*

- **Always composite inpainting results back onto original video**
  - Context: When using masking/inpainting, use ImageComposite node to blend result with original to preserve unmasked areas at 100% quality
  - *From: Kijai*

- **Use detailed descriptive prompts for complex transformations**
  - Context: For difficult concepts like water textures, use very detailed prompts describing the exact visual properties desired
  - *From: DiXiao*

- **Don't use enhance-a-video for single frame generation**
  - Context: This setting breaks single frame output in the wrapper
  - *From: Kijai*

- **Use FP16 T5 encoder with wrapper through DualClipLoader node**
  - Context: Load FP16 T5 encoder using the same method as native rather than wrapper's text encoder loader
  - *From: Kijai*

- **Use 150 tokens for prompts**
  - Context: General prompting advice
  - *From: Benjimon*

- **Use qwen 2.5 vl for captioning with system prompt**
  - Context: For training data preparation
  - *From: TK_999*

- **Interpolate videos before using for FlowEdit**
  - Context: Original 40 frame videos need interpolation to 53 frames for FlowEdit to work
  - *From: Kijai*

- **Put torch compile last in node order**
  - Context: When using native + KJ nodes
  - *From: Kijai*

- **Use denoise 1.00 for I2V**
  - Context: Output gets damaged if not using full denoise for I2V
  - *From: Miku*

- **Use CFG 3 and turn off SLG for good results with InP models**
  - Context: When working with 1.3B InP model
  - *From: H（4090）*

- **Set TeaCache to 0.010 as starting point for InP 1.3B**
  - Context: Speed optimization for new InP models
  - *From: JmySff*

- **Use huggingface-cli or Aria2 for faster downloads**
  - Context: When downloading large model files
  - *From: Juampab12*

- **Use SLG starting from block 8 for 1.3B models**
  - Context: For better quality on shorter videos, set SLG weaker and start later
  - *From: Kijai*

- **Don't use context with loop arguments**
  - Context: Uniform loop already loops on its own
  - *From: Kijai*

- **Use depth map size matching for control**
  - Context: Check that depth anything output is same size as input
  - *From: Kijai*

- **Combine SLG + CFG ZeroStar for decent results**
  - Context: Use together for improved quality on Fun models
  - *From: Kijai*

- **Replace first pose frame with pose from ref image**
  - Context: To snap into alignment for better pose control
  - *From: spacepxl*

- **Use ControlNet to brute force concepts with 1.3B model**
  - Context: When 1.3B model struggles with complex concepts, controlnet can help force better results
  - *From: DawnII*

- **Check fun_model toggle for end frame workflows**
  - Context: Need to toggle fun_model switch in encode node when using start/end frame functionality
  - *From: Kijai*

- **Don't expect normal I2V to be better with Fun models**
  - Context: The interesting thing is the control model and start/end frame, not regular I2V quality
  - *From: Kijai*

- **Change base precision to bf16 for 1.3B model**
  - Context: Since there's no fp16 version of 1.3B model, need to use bf16 precision
  - *From: Kijai*

- **Use TeaCache with 0.1-2 coefficients and start step 3-6**
  - Context: For faster generation with acceptable quality loss
  - *From: HeadOfOliver*

- **Set coefficients bool to true when using TeaCache**
  - Context: When using the 0.1-2 coefficient range
  - *From: HeadOfOliver*

- **Try frame counts 21, 41, 81 for best compatibility**
  - Context: These specific frame counts seem to work reliably
  - *From: VK (5080 128gb)*

- **Use 832x480 resolution as standard**
  - Context: This resolution works well and is commonly used
  - *From: VK (5080 128gb)*

- **End control early and adjust latent strength**
  - Context: When control is far from reference image (not stylized first frame)
  - *From: Kijai*

- **Reduce denoise to 0.6-0.75 for better results**
  - Context: When getting unnatural motion, lower denoise can help
  - *From: chrisd0073*

- **Use black frames as input if no start image needed**
  - Context: For control model when you don't want a reference image
  - *From: Kijai*

- **Use aggressive TeaCache for better and safer results than ultra-low steps**
  - Context: When trying to speed up generation
  - *From: Kijai*

- **Drop encoded video latent strength to 0.85 and denoise at 0.75**
  - Context: For better i2v results with stylized first frames
  - *From: A.I.Warper*

- **Use face segmentation and masking for better face quality**
  - Context: When full body shots have awful faces, especially anime faces
  - *From: DawnII*

- **Keep TeaCache offload on CPU unless using --highvram or --gpuonly**
  - Context: For optimal performance and stability
  - *From: Kijai*

- **Set start latent strength to 0 when using only end frame**
  - Context: For end-frame-only generation with InP models
  - *From: seitanism*

- **Use reverse batch with end frame as start for better face detail**
  - Context: When creating clips, face detail is much higher
  - *From: DawnII*

- **Drop clip strength or use different image for camera motion**
  - Context: For achieving camera movements in I2V
  - *From: DevouredBeef*

- **Don't use fp16_fast with Fun models**
  - Context: Since Fun models were released in bf16, fp16_fast is lossy
  - *From: Kijai*

- **Use coefficient option in TeaCache and select your model**
  - Context: For both wrapper and native implementations
  - *From: mamad8*

- **Use 'rotate' or 'moves left to right' for panning**
  - Context: When trying to achieve panning motion in Wan
  - *From: ArtOfficial*

- **Include 'looks at the camera at the end' for extensions**
  - Context: When extending videos from last frame
  - *From: Benjimon*

- **Match character using depth frame or photoshop**
  - Context: For character consistency
  - *From: Blink*

- **Swap enough blocks to have 1GB free VRAM**
  - Context: On Windows systems
  - *From: Benjimon*

- **Use 30-40 block swaps for 4070**
  - Context: For efficient generation on RTX 4070
  - *From: DawnII*

- **Close and reopen log if it gets stuck**
  - Context: When progress updates stop showing
  - *From: ArtOfficial*

- **Use controlnet in image generation process and tie pose to first frame of planned video**
  - Context: For better pose control in video generation
  - *From: CJ*

- **Generate first frame with SDXL/Flux/SD3 using controlnet, then use as start-frame for video**
  - Context: For better video generation results with pose control
  - *From: BondoMan*

- **Keep tiling off unless decoding actually fails on lack of memory**
  - Context: For better quality in video generation
  - *From: Kijai*

- **Start with low res fast training then bump it up**
  - Context: When training video models from scratch
  - *From: Benjimon*

- **Use as large dataset as possible, ideally millions of samples**
  - Context: Training video models from scratch requires massive datasets, 1200 images not enough
  - *From: spacepxl*

- **Use anime character LoRAs at low strength (0.3) to reduce 3D/CGI look**
  - Context: When prompting for 2D/anime style
  - *From: VK (5080 128gb)*

- **For clip vision encode with temporal masking, choose 1-2 representative images from video rather than whole video**
  - Context: When using Fun InP temporal masking
  - *From: Kijai*

- **Use lanczos with anti-aliasing for best image resize quality**
  - Context: When resizing images in workflows
  - *From: Kijai*

- **Use CFG 3 (half of pre-SLG CFG 6) when using SLG**
  - Context: SLG workflow optimization
  - *From: Miku*

- **FETA strength can be tweaked to slow down movement in I2V**
  - Context: Controlling motion speed in Wan I2V
  - *From: IllumiReptilien*

- **Use basic and unambiguous language in prompts**
  - Context: For better prompt results
  - *From: David Snow*

- **For POV prompts, use 'turns to look at the viewer' instead of 'looking into camera'**
  - Context: To avoid literal cameras appearing in output
  - *From: Kytra*

- **Use Flux with first frame of depth map then use as start image**
  - Context: Best way to use the model for depth-controlled generation
  - *From: Kijai*

- **Use aesthetic LoRA at strength 0.2**
  - Context: To get benefits without altering CFG
  - *From: David Snow*


## News & Updates

- **FP16 accumulate support added**
  - New feature requires PyTorch 2.7.0 nightly, provides significant speed improvements
  - *From: Kijai*

- **Context window/sliding window implementation released**
  - Allows for much longer video generation with good blending between segments
  - *From: Kijai*

- **Support for ComfyUI diffusion models added**
  - Updated code to allow loading diffusion models saved from within ComfyUI
  - *From: Kijai*

- **PyTorch 2.7.0 nightly now supports fp16 accumulation for ~20% speed boost**
  - Specifically optimized for WAN model, works with block swap
  - *From: Kijai*

- **WAN wrapper latest update showing 80%+ success rate with I2V from Midjourney images**
  - Significant improvement in success rate, nearly 100% today
  - *From: Janosch Simon*

- **ComfyUI --fast parameter format changed**
  - Now uses named parameters like fp16_accumulation instead of numbers
  - *From: Kijai*

- **Second pass workflows working amazingly well**
  - Community discovering great results with multi-pass generation
  - *From: Juampab12*

- **Context windowing implementation working well**
  - Sliding context window with overlap blending functional
  - *From: Juampab12*

- **fp16_fast accumulate option added to wrapper**
  - New toggle available under advanced options
  - *From: Kijai*

- **TeaCache optimization implementation in progress**
  - Working on polynomial fitting for step skipping
  - *From: Kijai*

- **TeaCache implementation added to Wan Video Wrapper**
  - Kijai implemented TeaCache for Wan models without proper polynomial coefficients but it still works effectively
  - *From: Kijai*

- **CLIP tokenizer removed from wrapper**
  - Kijai removed CLIP tokenizer completely as it was never used anyway
  - *From: Kijai*

- **TeaCache now available in Kijai's wrapper nodes**
  - Can be enabled/disabled in sampler, provides significant speed improvements
  - *From: Kijai*

- **CPU caching option added for text encoder**
  - New option to cache text encoder on CPU instead of RAM to reduce memory issues
  - *From: Kijai*

- **fp8 text encoder available in Kijai's HuggingFace repo**
  - Can use fp8 version or quantize option in loader to reduce VRAM usage
  - *From: Kijai*

- **TeaCache integration added to Kijai's wrapper**
  - TeaCache functionality integrated providing 2x speed improvements
  - *From: Kijai*

- **fp16 accumulation support added**
  - torch nightly support with fp16 accumulation for significant speed improvements
  - *From: Kijai*

- **Diffsynth offloading option added**
  - Added Diffsynth offloading as option, though feels slower
  - *From: Kijai*

- **e5m2 quantization models uploaded**
  - e5m2 quantization for GPUs that don't support torch compile on e4m3fn
  - *From: Kijai*

- **Wrapper updated with bug fixes**
  - Fixed 'list' object has no attribute 'to' error
  - *From: Kijai*

- **Context windowing now works with I2V**
  - Implementation added but uses same image for each window
  - *From: Kijai*

- **New VRAM management option added**
  - Alternative to block swap for memory management
  - *From: Kijai*

- **Initial TeaCache implementation for native ComfyUI released**
  - Missing start step implementation, available at ComfyUI-TeaCache repo
  - *From: Kijai*

- **FPS sampling implementation created for WanVideo**
  - Fork available with experimental fps sampling based on Apollo paper recommendations
  - *From: fredbliss*

- **RifleX working with Wan since today**
  - Works but results aren't amazing, limit to 161 frames for okay results
  - *From: Kijai*

- **Kijai added start/end parameters to teacache**
  - Fixed motion issues and improved usability
  - *From: Kijai*

- **Fredbliss added latent interpolation code with slerp + lerp**
  - Implements Apollo paper FPS sampling approach
  - *From: fredbliss*

- **H1111 updated with basic WanX support**
  - Using kohya's musubi backend for training
  - *From: Benjimon*

- **Official TeaCache examples coming soon**
  - The official TeaCache team said we can expect official example soon with coefficiency values
  - *From: Kijai*

- **New ComfyUI area composition feature**
  - New area composition functionality for video released
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Phantom video project for Wan**
  - Could replace LoRAs for Wan, currently being implemented
  - *From: yo9o*

- **TeaCache implementation moved from fork to KJNodes**
  - Ended up rewriting TeaCache completely, now available as standalone in KJNodes instead of fork
  - *From: Kijai*

- **Updated Wan FlowEdit workflow available in resources**
  - Fixed errors in previous version and cleaned up workflow
  - *From: Zuko*

- **Fixed major bug in FPS sampling fork**
  - Time calculation was incorrect, whole system was broken due to math errors
  - *From: fredbliss*

- **TeaCache moved to KJNodes**
  - Kijai rewrote teacache and added it to KJNodes package instead of separate implementation
  - *From: Kijai*

- **Hunyuan i2v model release Wednesday**
  - Mentioned upcoming release of Hunyuan i2v model
  - *From: Draken*

- **Updated torch version slower**
  - Newer torch version showing slower performance
  - *From: ˗ˏˋ⚡ˎˊ-*

- **VHS update enables animated previews during generation**
  - Major time saver - can see animated previews while generation is running instead of waiting for completion
  - *From: Kijai*

- **Native ComfyUI Wan implementation with bridge compatibility**
  - Can use any text encoder now with bridge node in wanwrapper to make Kijai's wrapper work in native
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Hunyuan I2V model releasing March 5th**
  - Official announcement that Hunyuan I2V will drop on Wednesday March 5th, Beijing time
  - *From: huangkun1985*

- **patches_II added TeaCache support**
  - New TeaCache implementation available but coefficients seem designed for 1.3B model only
  - *From: Kijai*

- **Frame limit under 81 resolved**
  - Previous hardcoded 81 frame limit has been fixed, can now make videos under 5 seconds
  - *From: Miku*

- **ComfyUI frontend bugs with latest update**
  - Note node broken, lots of bugs reported in version, warnings now become errors
  - *From: David Snow*

- **PyTorch 2.7.0 dev available in nightly**
  - Nightly builds now include 2.7.0 development version
  - *From: Ashtar*

- **Context windowed FloweEdit test working**
  - Kijai successfully tested 129 frames with context windowing, enabling potentially endless vid2vid
  - *From: Kijai*

- **FPS interpolation experimental implementation released**
  - Fredbliss created experimental FPS sampling with latent interpolation for more cinematic video generation
  - *From: fredbliss*

- **Updated TeaCache node available**
  - Kijai updated TeaCache but still only works on 1.3B model with different values
  - *From: Kijai*

- **Wrapper getting end step support**
  - End step functionality coming to wrapper, part of big update with flowedit and context windows
  - *From: Kijai*

- **Hunyuan I2V release delayed**
  - Originally scheduled for today, now delayed to tomorrow (within 23 hours)
  - *From: Draken*

- **FlowEdit with context window support added**
  - FloweEdit with context window support now available in wrapper, no example workflow yet as settings are tough to configure
  - *From: Kijai*

- **Open-Sora 1.3 released**
  - 1.1B model, 5s 720×1280, Apache 2.0 license, can do T2V, I2V and video extension, based on Pixart architecture
  - *From: deleted_user_2ca1923442ba*

- **TeaCache updated with calculated coefficients**
  - New version should be more accurate with proper mathematical coefficients rather than estimates
  - *From: Kijai*

- **LTX released keyframe interpolation feature**
  - Can now use LTX for advanced frame interpolation from low fps to high fps video
  - *From: Juampab12*

- **New LTX version with keyframe capabilities released**
  - New ltx came out with any keyframe capabilities, can put in 16 fps video and turn it into 24 fps, or 8 into 24, or 4 into 24
  - *From: Juampab12*

- **fp16 weights added to Comfy-Org repository**
  - Added some fp16 weights to HuggingFace repo, they are much closer to fp32 and tested mainly on 720p i2v
  - *From: comfy*

- **Hunyuan I2V officially released**
  - https://huggingface.co/tencent/HunyuanVideo-I2V - appears to require high VRAM (5090 minimum mentioned)
  - *From: GalaxyTimeMachine (RTX4090)*

- **Prompt travel implemented for Wan**
  - Just for context windows, not very robust, somewhat works if prompts aren't too different
  - *From: Kijai*

- **LTX Video interpolation node created for frame interpolation**
  - Node to bring Wan generations from various fps to 24fps, can handle 1fps to 24fps
  - *From: Juampab12*

- **Topaz published Blackwell alpha version**
  - New version supports RTX 5090 and other Blackwell GPUs
  - *From: aikitoria*

- **Alibaba Wan prosumer offering launched**
  - Competing with Kling, Hailuo, Runway, Luma. Plus model allows duration choice, Turbo available, art style repaint feature
  - *From: happy.j*

- **ComfyUI examples updated to use FP16 weights**
  - Official examples now recommend FP16 weights for best quality
  - *From: comfy*

- **New TeaCache coefficients released**
  - Better performance with more aggressive settings, defaults to step 1 start
  - *From: Juampab12*

- **New fp8_scaled model files released**
  - Available on HuggingFace Comfy-Org/Wan_2.1_ComfyUI_repackaged, requires ComfyUI update to avoid fp8 matrix mult by default
  - *From: comfy*

- **ComfyUI switched default Wan compute dtype to fp16**
  - Change made to default settings
  - *From: comfy*

- **Ostris hints at potential Wan speedup development**
  - AI-Toolkit developer may add Wan support and speed improvements
  - *From: JohnDopamine*

- **ComfyUI portable package with pytorch nightly and fp16 accumulation support**
  - Standalone package available for Windows
  - *From: comfy*

- **TeaCache node updated with better documentation**
  - Updated to reflect different values for 1.3B models with coefficients
  - *From: Kijai*

- **FP16 accumulation support added**
  - Use --fast fp16_accumulation flag with pytorch nightly
  - *From: comfy*

- **ComfyUI added native Hunyuan I2V support with image prompting**
  - Uses same approach as existing image prompting methods
  - *From: fredbliss*

- **Google Whisk Animate and Veo2 now available**
  - Whisk converts images to text then generates video
  - *From: fredbliss*

- **Claude successfully generated VAE tiling script**
  - For use with multi-GPU inference
  - *From: aikitoria*

- **TensorRT upscaling updated with auto-building engines**
  - No longer requires manual engine building
  - *From: VRGameDevGirl84(RTX 5090)*

- **New proper WanVideo Enhance-a-video node for native ComfyUI**
  - Applied after RoPE not before, proper patch instead of replacing whole model code, works with TeaCache and torch.compile
  - *From: Kijai*

- **TeaCache documentation added with lots of new info**
  - Added extensive documentation to TeaCache nodes
  - *From: Kijai*

- **CFG Distill LoRA available for Wan 2.1 1.3B**
  - New LoRA that seems to add additional detail, available on Civitai
  - *From: David Snow*

- **Cakify LoRA released for Wan 14B I2V**
  - Effect similar to pika.ai, available on Civitai
  - *From: Miku*

- **Tile upscale/deblur control LoRA in training**
  - 31 training hours so far, not fully converged but close
  - *From: spacepxl*

- **Tiled upscale control LoRA in development**
  - New method for generating 480p or lower and upscaling later, works with 1.3B model
  - *From: Juampab12*

- **New squish effect LoRA released**
  - High-quality LoRA matching Pika-labs results, trained on minimal data
  - *From: Kijai*

- **Triton for Windows now available in PyPI**
  - Can install with pip install triton-windows
  - *From: Kijai*

- **Updated enhance-a-video node**
  - Node was updated yesterday, should be weaker not stronger than before
  - *From: Kijai*

- **Multi-GPU script optimizations**
  - Added tiled VAE implementation with --tiled_vae flag, optimized --t5_cpu option
  - *From: intervitens*

- **ComfyUI commit ca8efab79fa19bc9745b4f7346d38a49ba1b1b7c enables native control LoRA support**
  - Makes control LoRAs work in native ComfyUI
  - *From: comfy*

- **New CPU T5 implementation showing improved core usage**
  - Visual demonstration of CPU core utilization
  - *From: aikitoria*

- **Video effects collection and datasets available for training Pika-like effect LoRAs**
  - Resources for effect LoRA training
  - *From: Cseti*

- **VACE system released**
  - Video control system with style transfer, inpainting, subject-driven, outpainting capabilities
  - *From: DREX*

- **New I2V LoRAs released on Civitai**
  - Deflate Effect and Crush Effect Wan2.1 I2V LoRAs available for testing
  - *From: Juampab12*

- **Teacache integration added to multigpu script**
  - Set --tc_thresh 0.22 to activate teacache functionality
  - *From: intervitens*

- **VACE system announced by Alibaba**
  - New video control system for style transfer, inpainting, subject-driven, outpainting with 'code soon' status
  - *From: The Shadow (NYC)*

- **Tencent released inpainting training datasets**
  - VPData and VPBench datasets available on HuggingFace for training inpainting models
  - *From: Cseti*

- **New distillation method paper released**
  - Adapter guidance distillation method paper published on arxiv
  - *From: Cseti*

- **WaveSpeed service offers Wan inference**
  - Commercial service providing Wan inference with compile and FB cache optimizations
  - *From: various*

- **Kijai updated WAN TeaCache node to fix OOM issues**
  - New version includes full_load option to disable for memory management
  - *From: Multiple users*

- **spacepxl pushed ControlLoRA training code**
  - Training code for control LoRAs now available
  - *From: pom*

- **VACE control system announced**
  - New video control system from Alibaba for style transfer, inpainting, subject-driven, outpainting
  - *From: VRGameDevGirl84(RTX 5090)*

- **Rope function optimization provides 20% speed boost**
  - Kijai optimized the rope function in WanVideoWrapper for faster generation
  - *From: Kijai*

- **Native improvements for TeaCache and CFG scheduling**
  - Updates include configurable TeaCache start step and CFG step cutoff for speed improvements
  - *From: intervitens*

- **Low memory LoRA loading option added**
  - New option to load LoRAs with less VRAM usage, though slower loading time
  - *From: Kijai*

- **Sparse-VideoGen speed upgrade coming for Wan**
  - H100 kernels available, consumer GPU kernels less likely due to compute capacity ceiling
  - *From: Draken*

- **VACE system released**
  - Video control system for style transfer, inpainting, subject-driven, outpainting
  - *From: Tonon*

- **Skip layer guidance technique adapted for Wan**
  - Reddit post shows skipping blocks 8, 9, or 10 on uncond inference improves quality
  - *From: IllumiReptilien*

- **Sesame CSM-1B model open sourced**
  - 1B parameter model released on HuggingFace, but no Maya voice included and no training code released
  - *From: Juampab12*

- **FlashVideo cascaded model announced**
  - New cascaded approach like Stable Cascade for video generation
  - *From: deleted_user_2ca1923442ba*

- **ComfyUI made changes to node to make SkipLayerGuidanceDiT work**
  - Native implementation now supports the skip layer functionality
  - *From: ramonguthrie*

- **TeaCache node updated to work with SkipLayerGuidanceDiT**
  - Fixed compatibility issue between the two nodes
  - *From: Kijai*

- **Enhance node added to native workflow 5 days ago**
  - Video enhancement functionality now available in native implementation
  - *From: Kijai*

- **Discord video playback fixed**
  - H265 playback issue in desktop app resolved
  - *From: Austin Mroz*

- **VAE warmup trick implemented**
  - Added solution to fix VAE burning artifacts at start of generation
  - *From: Kijai*

- **ComfyUI RoPE implementation added as option**
  - Added alternative RoPE calculation that can be compiled for better performance
  - *From: Kijai*

- **Flash attention support added to native implementation**
  - Native ComfyUI implementation now supports flash attention
  - *From: Doctor Shotgun*

- **Tiny VAE for Wan available for testing**
  - Unfinished model/code but can be tested by updating wrapper and downloading taew2_1.safetensors
  - *From: Kijai*

- **New rope option available for better performance**
  - Much better performance when enabled in wrapper
  - *From: Kijai*

- **Kijai added native SLG (Skip Layer Guidance) method to WanVideoWrapper**
  - Currently only works with TeaCache node, works with both 1.3B and 14B models with different settings
  - *From: Kijai*

- **Context window now supports VAE connection for better I2V conditioning**
  - New feature allows decoding/encoding of last frame from previous window
  - *From: Kijai*

- **Step-Video-TI2V released**
  - 30B parameter text-driven image-to-video model, first open-weight video DiT that may do well with anime
  - *From: JohnDopamine*

- **New model variant mentioned**
  - Step-Video-TI2V available on HuggingFace with ComfyUI workflow, requires 4+ GPUs
  - *From: JohnDopamine*

- **New Mobius looping node released for seamless video loops**
  - Kijai created new node for generating seamless loops using latent shifting technique, works with both T2V and I2V
  - *From: Kijai*

- **WanVideoGranularTextEncode node added to fork**
  - New node for creating granular text embeddings with smooth transitions between main prompts, includes transition strength and count parameters
  - *From: fredbliss*

- **Sage Attention 2 available but requires CUDA 12.8 for Blackwell GPUs**
  - CUDA 12.8 not required for Sage Attention 2 in general, only needed for Blackwell GPU support
  - *From: Doctor Shotgun*

- **Added start/end parameters to loop functionality**
  - Makes seam worse but clears noise otherwise
  - *From: Kijai*

- **Fixed video mask handling in wrapper**
  - Previously only worked as non-animated mask
  - *From: Kijai*

- **Changed LoRA loading method**
  - Now loads model and applies LoRA weights simultaneously
  - *From: Kijai*

- **Torch 2.8 + TorchVision now compatible with TorchAudio 2.6**
  - No more compatibility issues, can use full install command
  - *From: Miku*

- **Video mask support added to wrapper**
  - Updated last night to allow video mask input instead of just first frame mask
  - *From: Kijai*

- **Manager update not yet available**
  - Manual update needed, not yet in ComfyUI Manager
  - *From: Juan Gea*

- **TensorRT-LLM exploration for WAN**
  - Found stdit implementation in trtllm, could be fastest possible execution option
  - *From: aikitoria*

- **spacepxl released WIP depth control LoRA for Wan 1.3b**
  - Available on HuggingFace with example workflow, needs more training for better prompt following
  - *From: spacepxl*

- **Kijai fixed torch.compile bug with end_percent LoRA reapplication**
  - LoRA wouldn't reapply properly with torch.compile, now fixed
  - *From: Kijai*

- **WanVideo wrapper updated with block dropping from control lora**
  - Allows dropping blocks from control lora which may help with results
  - *From: Kijai*

- **Start/End frame implementation pushed**
  - New workflow allows first frame to last frame morphing, works well with LoRAs
  - *From: Kijai*

- **Cosmos Transfer1 released by Nvidia**
  - Video-to-video transfer and upscaling tools now available
  - *From: ˗ˏˋ⚡ˎˊ-*

- **FLUXFLOW paper released**
  - Counter-intuitive training method that finetunes video models by shuffling 12-25% of frames to improve temporal coherence
  - *From: mamad8*

- **New Start/End frame interpolation capability**
  - Can now use start and end frame inputs with adjustable strengths, works like iPA concept
  - *From: The Shadow (NYC)*

- **FP16 model variant available**
  - taew2_1 - tiny VAE for faster previews
  - *From: Kijai*

- **Tiled clip embed stuff pushed**
  - New feature for processing clip embeddings in tiles
  - *From: Kijai*

- **WAN 2.1 technical report available**
  - Comprehensive paper with implementation details and benchmarking
  - *From: yi*

- **New CLIP vision encode options added**
  - Added concat option, tile support, crop/stretch options for better image handling
  - *From: Kijai*

- **More LoRAs available on HuggingFace**
  - Remade-AI collection has wan21-14b-t2v-loras
  - *From: Siraj*

- **Size adjustment node updates**
  - Added separate node for automatic size adjustment, calculates max area and keeps aspect ratio
  - *From: Kijai*

- **Time lapse LoRA will be distributed on Civitai**
  - After further adjustments, creator plans to release it publicly
  - *From: 852話 (hakoniwa)*

- **Loop stitching improvements implemented**
  - Based on Mobius paper methodology for smoother results
  - *From: Kijai*

- **Wan team planning to release official start/end model**
  - Trained single model for several frame conditioning options, then finetuned into separate i2v, start/end variants
  - *From: spacepxl*

- **woct0rdho now providing SageAttention wheels**
  - Available at GitHub releases
  - *From: TK_999*

- **New prompt travel feature pushed to WanVideoWrapper**
  - Allows segmenting cross-attention for different prompts in video sequence
  - *From: Kijai*

- **Added batch join method for I2V image splitting**
  - Can now split conditioning images to different video halves
  - *From: Kijai*

- **New negative_image clip encode node added**
  - Provides additional control over negative conditioning
  - *From: Kijai*

- **CFG-Zero-star implementation added to ComfyUI-WAN-WRAPPER**
  - New node implementing CFG-Zero-star technique with configurable parameters, provides subtle quality improvements
  - *From: Kijai*

- **Self attention split functionality added**
  - New capability to split self attention for multiple prompt conditioning using pipe syntax
  - *From: Kijai*

- **MultiGPU support working with native Wan**
  - Successfully loads 7GB on second GPU and 12GB on main GPU for distributed inference
  - *From: VK (5080 128gb)*

- **CFG Zero Star implemented in ComfyUI by comfy**
  - Official ComfyUI implementation that stacks with different cfg tricks
  - *From: comfy*

- **Wan2.1-Fun-14B-InP released by Alibaba**
  - New controlnet models from different Alibaba team
  - *From: yi*

- **Kijai renamed CFG Zero Star node**
  - Renamed to avoid conflicts with official ComfyUI implementation
  - *From: Kijai*

- **Qwen chat can do HD videos now**
  - Free service that looks similar to Wan, possibly using Wan backend
  - *From: Benjimon*

- **Wan2.1-Fun-1.3B released with I2V capabilities**
  - Includes both InP and Control variants, supporting start/end frame prediction
  - *From: Draken*

- **14B Fun models exist on ModelScope but not HuggingFace yet**
  - Available at modelscope.cn/models/PAI/Wan2.1-Fun-14B-Control/files
  - *From: yi*

- **Kijai uploaded fp8 converted versions of Fun models**
  - Available at huggingface.co/Kijai/WanVideo_comfy/ - reduces 14B from ~46GB to ~16GB
  - *From: Kijai*

- **VideoX-Fun repository renamed from original**
  - Repository was renamed and now contains training code
  - *From: Kijai*

- **14B Fun models available in bf16**
  - 35GB 14B model available on HuggingFace
  - *From: ReDiff*

- **T2V support added to InP model**
  - Just fixed T2V functionality with the InP model
  - *From: Kijai*

- **Reward LoRA example available**
  - HuggingFace page shows Wan2.1-T2V-1.3B-Reward results but no model file yet
  - *From: yi*

- **New Wan Fun models released**
  - Wan2.1-Fun-InP models (1.3B and 14B) for start/end frame prediction, and control models supporting multiple resolutions
  - *From: Kijai*

- **Beta sigmas added for Euler scheduler**
  - Added beta sigmas for euler as option, now available in diffusers, though not a huge difference
  - *From: Kijai*

- **Native ComfyUI support for 1.3B and 14B Fun Control models**
  - New commit adds native support, but not for inpaint models which still use regular i2v node
  - *From: comfy*

- **GPU prices normalizing**
  - 5090 prices dropped from 4.5k to 3k, 3090s still around $1400
  - *From: aikitoria*

- **ComfyUI native support added for Wan Fun models**
  - Official ComfyUI commit added native support
  - *From: comfy*

- **Fun Control and InP models now available**
  - New Wan 2.1 Fun models released with control and inpainting capabilities
  - *From: multiple users*

- **TeaCache improvements merged**
  - New TeaCache patch with e0 coefficients for better quality and speed
  - *From: yi*

- **Wan team released technical report**
  - Comprehensive technical report available at https://arxiv.org/abs/2503.20314 covering more than just base model
  - *From: Pedro (@LatentSpacer)*

- **ComfyUI-WanVideoWrapper updated to version 1.1.1**
  - Fixed control_embeds compatibility issues and made start_image optional for InP models
  - *From: Kijai*

- **New 3D generation models released**
  - TripoSF and TripoSG from VAST-AI-Research, may be 20-25% better than HY3D
  - *From: Draken*

- **Nunchaku plans to support Wan**
  - It's on their roadmap, currently supports Flux and is very fast
  - *From: Lumi*

- **Chinese modded 48GB RTX 4090 available**
  - 96GB versions also teased, can be upgraded in Shenzhen GPU shops
  - *From: Simonj*

- **New DiffSynth Studio LoRAs released**
  - Aesthetics, HiRes, and Extend LoRAs available for Wan 2.1
  - *From: TimHannan*

- **Comfy rope function made default**
  - Comfy function is now default in nodes and workflows, faster with compile
  - *From: Kijai*

- **Fun models work in native ComfyUI**
  - No need to use separate repo, Fun models work in both wrapper and ComfyUI natively
  - *From: Kijai*

- **TaylorSeer released support for all Wan models**
  - Will be especially useful for 1.3B variant, though acknowledges cannot perform single-GPU inference for 14B models on A100 80GB
  - *From: yi*

- **CFG distillation LoRAs available**
  - spacepxl/wan-cfgdistill-loras available on HuggingFace, plus diffsynth lora for 1.3B only
  - *From: yi*

- **fp16 weights of Wan available**
  - wavespeed/Wan2.1-T2V-14B-Diffusers-fp16 on HuggingFace, appears to just be fp16 conversion of original diffusers weights
  - *From: DawnII*

- **Added e5m2 versions of Fun models for users who can't use e4m3fn with torch.compile**
  - Available on HuggingFace, helps with <4xxx series GPU compatibility
  - *From: Kijai*

- **Fun InP model now supports temporal masking**
  - Binary masks only, works with full video input and matching length mask video
  - *From: Kijai*

- **Multi-frame start/end support added to Fun InP**
  - Can use 2-5 start and end frames for better video extension
  - *From: Kijai*

- **DiffSynth released 4 LoRAs for base 1.3B model**
  - Highres and aesthetics LoRAs making big difference in quality
  - *From: Kijai*

- **New reroute system merged in ComfyUI**
  - Breaking some workflows, uses regular Lt reroutes now
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Reward LoRAs still not released**
  - The reward LoRAs are separate from the DiffSynth LoRAs and not yet available
  - *From: Kijai*


## Workflows & Use Cases

- **Second pass sampling**
  - Use case: Improving video quality by running output through second sampler
  - *From: David Snow*

- **Context window for long videos**
  - Use case: Generating endless/very long videos using sliding window approach
  - *From: Kijai*

- **Double-pass generation with different seeds**
  - Use case: Better quality results than single high-step generation
  - *From: David Snow*

- **FlowEdit + Set Latent Noise Mask + WAN2.1 1.3b**
  - Use case: Interesting masking effects for video generation
  - *From: Nathan Shipley*

- **Infinite looping at 81 frames with RIFE interpolation**
  - Use case: 7 loops at 81f, 30 steps, 1232x720, output to 25fps
  - *From: AJO*

- **Two-pass generation with WAN + Hunyuan**
  - Use case: Significant quality improvement using WAN first pass, Hunyuan second pass at low denoise
  - *From: David Snow*

- **V2V cleanup with low denoise**
  - Use case: Cleaning up artifacts from I2V generation
  - *From: Doctor Shotgun*

- **Context sliding window for long videos**
  - Use case: Generating longer videos with temporal consistency
  - *From: Kijai*

- **Face swapping with ROPE**
  - Use case: Consistent face replacement in generated videos, takes 5 seconds per video
  - *From: VRGameDevGirl84(RTX 5090)*

- **Wan 960x544 -> HYV -> 2x upscale -> RIFE**
  - Use case: FullHD generation in under 12min on 3090
  - *From: burgstall*

- **T2V low res -> upscale first frame -> I2V with low denoise**
  - Use case: Faster than generating high res T2V directly
  - *From: mamad8*

- **Wan T2V -> denoise with Skyreels**
  - Use case: Video-to-video enhancement
  - *From: Benjimon*

- **Fast generation with TeaCache + CFG splitting + other optimizations**
  - Use case: wrapper with fp8, fp16 accumulate, cfg splitting, teacache, sage, torchcompile for maximum speed
  - *From: seitanism*

- **Using Hunyuan for video enhancement after Wan generation**
  - Use case: Generate with Wan, then use Hunyuan vid to vid for enhancement
  - *From: VRGameDevGirl84*

- **T2V then Hunyuan V2V enhancement**
  - Use case: Generate with Wan T2V at 720x480, then enhance with Hunyuan V2V for better quality in automated pipeline
  - *From: VRGameDevGirl84*

- **Multi-stage upscaling with different models**
  - Use case: Use 14B for initial gen, then 1.3B model for upscaling with 10 steps and low denoise
  - *From: N0NSens*

- **Three-stage processing pipeline**
  - Use case: Wan T2V → Hunyuan V2V → upscale to 1920x1080 with frame interpolation to 24fps and color correction
  - *From: VRGameDevGirl84*

- **SDXL to Wan I2V pipeline**
  - Use case: Generate SDXL image then use as input to Wan I2V for improved sharpness and colors
  - *From: deleted_user_2ca1923442ba*

- **Context generation workflow**
  - Use case: 1200 sec for 16sec video on 3090 at 832*480 using 3B model
  - *From: NebSH*

- **WAN I2V -> HunyuanVideo upscale pipeline**
  - Use case: Generate with WAN at low res then upscale with HunyuanVideo, but v2v with t2v model changes too much even at 0.1 denoise
  - *From: hablaba*

- **Context windowing for long videos**
  - Use case: Generate videos longer than 81 frames using context windows with overlap
  - *From: Kijai*

- **Multi-step upscaling and interpolation**
  - Use case: Original WAN 14B 368x368 -> upscale to 848x848 with HunyuanVideo -> interpolate, compared to WAN 14B upscale
  - *From: seitanism*

- **Context windowing for long videos**
  - Use case: Generate videos longer than 81 frames using overlapping windows
  - *From: Kijai*

- **FPS sampling with latent interpolation**
  - Use case: Generate keyframes at low fps then interpolate in latent space for smoother motion
  - *From: fredbliss*

- **Native scaled text encoder bridge**
  - Use case: Connect native text encoders to wrapper using bridge node
  - *From: Kijai*

- **FPS sampling with latent interpolation**
  - Use case: Generating longer, more consistent videos by generating fewer frames and interpolating between them
  - *From: fredbliss*

- **Multi-optimization stack for low VRAM**
  - Use case: Combining sageattention, torch.compile, fp16 accumulation, teacache, and adaptive guidance for 12GB cards
  - *From: Miku*

- **Multi-pass upscaling with vid2vid**
  - Use case: Generate low res first, then upscale and refine with same initial image
  - *From: mcmonkey*

- **3x RIFE with every 2nd frame skip**
  - Use case: Frame interpolation workflow for smoother video
  - *From: burgstall*

- **Looping video generation**
  - Use case: Infinite video loops that don't increase VRAM usage between loops
  - *From: AJO*

- **Decode-encode upscaling step between generation**
  - Use case: Takes longer and quality is lower but allows for upscaling mid-process
  - *From: burgstall*

- **RIFE 3x interpolation from 16fps to 48fps then back to 24fps**
  - Use case: Load every 2nd frame to get final 24fps output
  - *From: AJO*

- **8 iteration loop with increased RAM**
  - Use case: Used 98% of 76GB RAM with 64GB swap for extended generation
  - *From: AJO*

- **RES4LYF sampler with Wan2.1 1.3B**
  - Use case: Better quality sampling with res_2m at same speed as euler
  - *From: Ablejones*

- **Latent guides with t2v**
  - Use case: Influence generation direction with input images for character/color steering
  - *From: Ablejones*

- **Native Wan with masking support**
  - Use case: Selective area generation in video
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Context windowing for long videos**
  - Use case: Generating videos longer than 81 frames (up to 513+ frames tested)
  - *From: Kijai*

- **I2V with different images per context window**
  - Use case: Using different starting images for each context window to maintain consistency
  - *From: Kijai*

- **Simple latent guide workflow**
  - Use case: V2V-style control using latent guides for spatial and temporal control
  - *From: Ablejones*

- **I2V with TeaCache and upscaling**
  - Use case: Image to video generation with speed optimization and quality upscaling
  - *From: Bleedy (Madham)*

- **Context window automation with Florence and Groq**
  - Use case: Automated prompt generation for context windows using Florence for image analysis and Groq for LLM processing
  - *From: AJO*

- **Multi-prompt context window setup**
  - Use case: Using | separated prompts for different context windows in longer generations
  - *From: AJO*

- **WAN I2V upscaling and frame interpolation**
  - Use case: Complete pipeline from image to video with upscaling to 4K and frame interpolation
  - *From: The Shadow (NYC)*

- **V2V with context windows and freenoise**
  - Use case: 129 frames video-to-video with good quality, windows not easily noticeable
  - *From: Kijai*

- **Two-pass I2V upscaling**
  - Use case: Upscale first pass, then use for second pass I2V generation
  - *From: N0NSens*

- **FlowEdit for video-to-video**
  - Use case: Alternative v2v method similar to Wan 2.1 capabilities
  - *From: Ashtar*

- **Ultimate SD upscale for Wan videos**
  - Use case: Upscaling 832x480 to 3328x1920, fits in 16GB VRAM but slow with tile borders
  - *From: Cseti*

- **Context windowed video extension**
  - Use case: Generate 129+ frame videos with potential for endless generation
  - *From: Kijai*

- **FPS interpolation workflow**
  - Use case: Generate at low FPS (2fps) and interpolate to higher FPS (16fps) for more cinematic results
  - *From: fredbliss*

- **Multi-sequence rendering with interpolation**
  - Use case: 1 go rendering, 4 sequences (81+89+65+81 frames = 316 frames at 16fps), then interpolated to 25fps in Topaz
  - *From: JmySff*

- **Double VAE decoding for perfect loops**
  - Use case: Extend latents with first 4 frames, decode, then blend first 13 frames with repeated decode and trim
  - *From: Benjaminimal*

- **Context window looping**
  - Use case: Automatic looping through context windows wrapping around to beginning
  - *From: Benjaminimal*

- **Flux Storyboarding workflow**
  - Use case: Split Flux storyboard LoRA and use as first frame for each generation with PuLID and LLM prompting following original scenes
  - *From: AJO*

- **Batch text-to-video with Florence**
  - Use case: 848x480 last frame extensions using Florence, batch text prompts and Groq LLM enhanced directing
  - *From: Organoids*

- **Endless looping context windows**
  - Use case: Creating seamless video loops using looping context windows and VAE trickery
  - *From: Benjaminimal*

- **Multi-scene story generation pipeline**
  - Use case: Takes reference image, creates 4-scene storyboard, generates individual 81-frame videos for each scene, combines with 24fps correction for MMAudio integration
  - *From: AJO*

- **Wan + LTX interpolation pipeline**
  - Use case: Generate 4fps video with Wan, then interpolate to 24fps using LTX keyframes for smoother final output
  - *From: Juampab12*

- **Enhanced video upscaling chain**
  - Use case: Run video through SD Ultimate Upscale then Topaz Video AI for maximum quality enhancement
  - *From: Gateway {Dreaming Computers}*

- **Multi-scene generation from single image**
  - Use case: 4 scene auto storyboarding from one image with auto prompt and auto scene
  - *From: AJO*

- **Context windowing with TeaCache**
  - Use case: Generate longer videos with speed optimization using context windows
  - *From: Kijai*

- **Video extension using FILM VFI and RIFE VFI**
  - Use case: Extended 21 seconds, 513 frames, 24fps by adding FILM VFI and RIFE VFI
  - *From: Bleedy (Madham)*

- **Multi-GPU Wan inference script**
  - Use case: Running Wan at full quality across multiple GPUs with FSDP sharding/offloading
  - *From: intervitens*

- **Frame interpolation workflow using LTX VAE**
  - Use case: Converting low fps Wan videos (1-16fps) to 24fps using LTX Video interpolation
  - *From: Juampab12*

- **SillyTavern integration with Wan**
  - Use case: LLM chatbot generates prompts for SDXL images, then creates videos from those images using Wan
  - *From: aikitoria*

- **Multi-GPU automation system**
  - Use case: Automatically shut down TRTLLM, generate video with Wan, then restart TRTLLM - all controlled from SillyTavern
  - *From: aikitoria*

- **Two-stage generation with upscaling**
  - Use case: Generate at 368x368 then upscale to 720x720 using same LoRA for better quality
  - *From: seitanism*

- **Context windows for long video generation**
  - Use case: Using sliding window approach to generate longer videos, can do 1025 frames with 97-frame windows
  - *From: Uehreka*

- **Split CFG scheduling**
  - Use case: Real CFG for first few steps, then distilled CFG for remainder using LoRA
  - *From: spacepxl*

- **Automated movie generation with 4 scenes**
  - Use case: Enter reference image and story idea, generates 4-scene storyboard with PuLID, motion prompts, and RIFE interpolation to 24fps
  - *From: AJO*

- **VAE decode → save → interpolate → save**
  - Use case: Proper sequence to avoid OOM and optimize performance when using interpolation
  - *From: Juampab12*

- **V2V with context windows using wrapper**
  - Use case: Video-to-video generation with longer sequences
  - *From: Organoids*

- **CFG distilled 1.3B model workflow**
  - Use case: Faster inference with gradient estimation sampler
  - *From: spacepxl*

- **Native V2V without context windows**
  - Use case: Basic video-to-video when context windows not needed
  - *From: Kijai*

- **Google's image->text->video pipeline**
  - Use case: Create consistent videos from images using Whisk and VideoFX
  - *From: fredbliss*

- **Two-pass generation: lowres then upscale**
  - Use case: Faster workflow by generating 480p first then upscaling
  - *From: N0NSens*

- **Generate 720p then vid2vid at 1080p with low denoise**
  - Use case: Better quality than direct 1080p generation
  - *From: mamad8*

- **Complete video pipeline: Wan generation -> interpolation -> LatentSync -> upscale**
  - Use case: Creates initial 480x480 Wan video, interpolates, adds lip sync, upscales to FHD 16:9 in 175 seconds
  - *From: VRGameDevGirl84(RTX 5090)*

- **V2V using T2V model for better results**
  - Use case: Video-to-video generation, someone said I2V doesn't work for v2v but it works with flowedit mode
  - *From: Organoids*

- **Context windowing for long videos**
  - Use case: 129 frame renders with 4 context windows, 32 frame windows, 8 context stride, 4 overlap with TeaCache took ~211 secs on 3090
  - *From: Organoids*

- **480x480 generation + crop to 16:9 + TensorRT RIFE + TensorRT upscale**
  - Use case: Fast generation with interpolation and upscaling for talking head videos
  - *From: VRGameDevGirl84(RTX 5090)*

- **Face detection + crop to aspect ratio + face swap with Reactor**
  - Use case: Consistent character generation with face restoration
  - *From: VRGameDevGirl84(RTX 5090)*

- **Native ComfyUI with teacache + enhance a video**
  - Use case: I2V 480p, 324 frames, 960x544 in 24min12
  - *From: JmySff*

- **Seed hunting with TeaCache then full quality render**
  - Use case: Finding good seeds quickly before doing final high-quality generation
  - *From: ArtOfficial*

- **Multi-GPU setup for large model inference**
  - Use case: Running 14B model with dual 5090s at 70% power limit
  - *From: seitanism*

- **Multi-resolution generation pipeline**
  - Use case: Generate 360p with 14B model, then upscale to 720p quickly instead of native 720p
  - *From: Juampab12*

- **Memory-optimized setup**
  - Use case: Use VRAM management node instead of block swap for better RAM efficiency
  - *From: Kijai*

- **Video extension using context windows**
  - Use case: Generate longer videos by splitting steps into overlapping context windows
  - *From: Kijai*

- **LoRA training on 1.3B model**
  - Use case: Quick effect training with minimal data - hydraulic press effect trained with just 2 videos
  - *From: Juampab12*

- **Tile control LoRA for video upscaling**
  - Use case: Upscale videos using blurred input as conditioning
  - *From: spacepxl*

- **Native workflow with 2 LoRAs**
  - Use case: Running multiple LoRAs in native ComfyUI
  - *From: Kijai*

- **Image+video2video combination**
  - Use case: Style transfer applications
  - *From: Cubey*

- **Resize>blur>diffusion for high-res generation**
  - Use case: Basic high-resolution video generation
  - *From: TK_999*

- **T2V Hunyuan then 3 Wan end frame extensions**
  - Use case: Creating longer videos by chaining multiple extensions
  - *From: Organoids*

- **Single condition control training**
  - Use case: Train with different control types and let model figure out the image type
  - *From: comfy*

- **Blender camera movement training**
  - Use case: Create controlled camera movement datasets for training camera control LoRAs
  - *From: Juampab12*

- **CFG distill with spline curve**
  - Use case: Use CFG 5.5 to 1 at 25% point for faster inference with quality retention
  - *From: Juampab12*

- **GGUF with Virtual VRAM**
  - Use case: Use GGUF model with Virtual VRAM node to add RAM as VRAM and halve inference times
  - *From: GalaxyTimeMachine (RTX4090)*

- **Native vs wrapper for control**
  - Use case: Use native instead of wrapper for better control embed handling, can split to 2 different samplers
  - *From: Kijai*

- **CFG scheduling from 5.5 to 1.0 over timesteps**
  - Use case: Speed optimization while maintaining quality, works with CFG points like [{"x":0,"y":5.5}...{"x":19,"y":1}]
  - *From: Juampab12*

- **480p I2V with TeaCache for preview, then full quality**
  - Use case: Quick iteration and final quality output
  - *From: Kijai*

- **Model patcher -> LoRA -> Sage -> other nodes**
  - Use case: Proper node ordering for native WAN implementation
  - *From: TK_999*

- **I2V with TeaCache and CFG scheduling**
  - Use case: Faster I2V generation with 0.2 TeaCache threshold, start step 10, 35 total steps, CFG 30% at 5.5 strength
  - *From: Juampab12*

- **Resolution calculator for maintaining VRAM usage**
  - Use case: Tool to calculate closest resolutions/frame counts for target total pixels to maintain same VRAM usage
  - *From: Fred*

- **Wan/LTX hybrid story generation**
  - Use case: Combining Wan quality with LTX speed, but LTX quality issues limit effectiveness
  - *From: AJO*

- **Upscale then traditional denoise**
  - Use case: Clean up VAE noise after upscaling Wan outputs
  - *From: spacepxl*

- **T2V with 60 steps then upscale and VFI**
  - Use case: Single pass 832x480 T2V workflow, though user finds results fake-looking
  - *From: Shawneau*

- **Dual LoRA generation with block swap**
  - Use case: Generate two different 480x832x81 clips with different LoRAs, requires block_swap=40 and 1500sec total
  - *From: burgstall*

- **CFG scheduling with early termination**
  - Use case: Use high CFG (like 6) for first steps, then drop to 1 for remaining steps using end parameter at 0.5 for 40 steps
  - *From: Payuyi*

- **String to Float List for CFG control**
  - Use case: Put values like '6,6,6,6,6,1,1,1,1,1' for precise CFG scheduling per step
  - *From: Juampab12*

- **Torch compile + TeaCache optimization chain**
  - Use case: Reducing render times from 42min to 12min on A100 80GB for 1280x720x81 at 40 steps
  - *From: HeadOfOliver*

- **Timelapse LoRA training with frame duplication**
  - Use case: Training aging timelapse effects by manipulating frame indices to prevent VAE compression
  - *From: Juampab12*

- **Control tile upscaling with proper blur settings**
  - Use case: 2x upscaling with 12px blur and 0.3 sigma, lora strength 1.0, end percent 0.95
  - *From: spacepxl*

- **Two-stage video enhancement**
  - Use case: Small T2V render at 352x528, then control lora workflow for 3x upscale with detail enhancement and outfit swaps
  - *From: ramonguthrie*

- **Multi-scene story generation**
  - Use case: Automated 4-scene video generation using flux storyboarding, then 81-frame extensions with last frame chaining
  - *From: AJO*

- **Duo sampler approach**
  - Use case: 20 steps normal with CFG, then 10 steps with 1 CFG + detail daemon sampler for speed
  - *From: CapsAdmin*

- **Preview workflow with TeaCache**
  - Use case: Use TeaCache with high threshold and 8-10 steps with Euler for quick previews
  - *From: mamad8*

- **Use 81 frames minimum for best quality**
  - Use case: Wan needs at least 81 frames to work best, 33 can work to some extent
  - *From: Kijai*

- **Context windows naturally loop**
  - Use case: Can generate loopable videos using context window looping
  - *From: Kijai*

- **Frame extension using sharpest frames**
  - Use case: Take sharpest frame from last 10 frames for next video generation
  - *From: Benjimon*

- **Using SLG with LoRAs for enhanced effects**
  - Use case: Amplifying LoRA strength while maintaining stability
  - *From: Cseti*

- **FloweEdit with Wan video generation**
  - Use case: Video editing and style transfer, though requires significant render time
  - *From: yukass*

- **Combining multiple optimization nodes**
  - Use case: Using enhance-a-video, SLG, torch compile, sage attention, teacache together
  - *From: seitanism*

- **Long video generation with context windows and overlap**
  - Use case: Creating videos longer than base model limit (245 frames tested with 81 overlap)
  - *From: Cubey*

- **Using SLG with LoRA and disabled corresponding blocks**
  - Use case: Significantly improved quality output, especially for character consistency
  - *From: BondoMan*

- **LoRA training on 1.3B model**
  - Use case: Faster training and smaller file sizes - 83MB at rank 64 vs 500MB on 14B
  - *From: Flipping Sigmas*

- **Context windowing with image conditioning**
  - Use case: Using multiple similar prompts separated by | for better temporal consistency
  - *From: Kijai*

- **Last frame extraction for video extension**
  - Use case: Grabbing last frame of previous video to string them together for longer output
  - *From: AJO*

- **Using Context options with I2V for long generations**
  - Use case: 161 frame generations with | split method for prompt changes
  - *From: Lumi*

- **Seamless blending between multiple prompts**
  - Use case: Granular embedding blending across timesteps for smooth transitions
  - *From: fredbliss*

- **Multi-stage prompt blending with intermediate descriptions**
  - Use case: Generate video with A|B prompts, screenshot middle frames, describe with LLM, regenerate with A|A'|B'|B for smoother transitions
  - *From: fredbliss*

- **Context windowing for long videos**
  - Use case: Process long videos in chunks with frame overlap for memory efficiency while maintaining temporal consistency
  - *From: fredbliss*

- **Video inpainting with SAM2 + differential diffusion**
  - Use case: Object replacement in videos using mask input in encode node
  - *From: Kijai*

- **Context windows with multiple prompts**
  - Use case: Scene transitions like 'old man walking|shark attacks' within single generation
  - *From: Kijai*

- **Loop generation with mobius technique**
  - Use case: Creating seamless video loops
  - *From: Kijai*

- **Content-aware blending framework**
  - Use case: Frame analysis → blending → transition processing
  - *From: fredbliss*

- **Native WAN with SLG, teacache, enhance video**
  - Use case: High quality 316 frame generation at 960x544 with 30 steps
  - *From: JmySff*

- **Multi-GPU inference setup**
  - Use case: Fast 1280x720p 81 frame generation in 5 minutes
  - *From: aikitoria*

- **Depth control LoRA with two-pass sampling**
  - Use case: Structure and motion control with creative refinement
  - *From: spacepxl*

- **Start and end frame editing for Wan wrapper**
  - Use case: Creating looped or extended videos
  - *From: Eclipse*

- **Two-pass sampling with split LoRAs**
  - Use case: Using depth control + custom LoRA, then custom LoRA only for better face/character consistency
  - *From: spacepxl*

- **V2V with depth control using two passes**
  - Use case: Process footage through depth crafter first, then use two sampling passes with context windows
  - *From: Flipping Sigmas*

- **Video looping with start/end frames**
  - Use case: Generate video from first frame, use last frame as new first frame with original as end frame
  - *From: const username = undefined;*

- **Object replacement in video**
  - Use case: Either inpaint first then generate video, or generate normally then vid2vid with masking
  - *From: Kijai*

- **Start/End frame with dual ClipVision**
  - Use case: Creating controlled animations between two keyframes with adjustable embed strengths
  - *From: The Shadow (NYC)*

- **Depth control video-to-video**
  - Use case: Converting realistic video input to anime style using depth maps and control LoRAs
  - *From: 852話 (hakoniwa)*

- **Style transfer with RES4LYF guide nodes**
  - Use case: Rudimentary style transfer using guide nodes combined with depth LoRA
  - *From: Ablejones*

- **Native masked video-to-video**
  - Use case: Inpainting specific areas of video using masks, works with static and non-static backgrounds
  - *From: TK_999*

- **Start/End frame morphing**
  - Use case: Creating transitions between different images
  - *From: The Shadow (NYC)*

- **Automated storyboarding system**
  - Use case: 80% automated long-form video generation with looping
  - *From: AJO*

- **Remove warmup frames with split index**
  - Use case: Automatically removing first and last problematic frames
  - *From: Cubey*

- **I2V with TeaCache for fast generation**
  - Use case: Quick 3-minute generations with acceptable quality loss
  - *From: Kijai*

- **Using start and end frames with CLIP embeds**
  - Use case: Better end frame accuracy in video generation
  - *From: Kijai*

- **Differential diffusion with masking**
  - Use case: Selective video editing while preserving background
  - *From: David Snow*

- **Two-pass depth control workflow**
  - Use case: Better depth-controlled video generation, render DepthCrafter separately if OOM occurs
  - *From: Flipping Sigmas*

- **Start/end frame method for camera stability**
  - Use case: Keeping camera in place and creating loops in I2V
  - *From: Faux*

- **Differential diffusion with masking**
  - Use case: Diffusing at different strengths based on black and white mask input
  - *From: David Snow*

- **Face LoRA for controllable angles and emotions**
  - Use case: Creating controllable face generations for start/end frames with different viewing angles and emotional expressions
  - *From: Juampab12*

- **Controlnet blending technique**
  - Use case: Blending source images with controlnet inputs (depth, canny) for better style control
  - *From: VK (5080 128gb)*

- **I2V 480p then refine with T2V model using 1.25x upscale**
  - Use case: Quality improvement and upscaling of initial generations
  - *From: traxxas25*

- **Differential diffusion using mask option in encode node**
  - Use case: Diffuse different video parts at different strengths based on black/white mask
  - *From: David Snow*

- **Using Sam2 points editor for masking specific subjects**
  - Use case: Precise control over which parts of video get processed
  - *From: David Snow*

- **Start and end frame with same image and character pose prompts**
  - Use case: Creating realistic 'photo comes to life' effects
  - *From: Shawneau*

- **V2V with masking using native Wan**
  - Use case: Fast video-to-video generation with selective area modification using depth maps and masks
  - *From: David Snow*

- **Wrapper inpainting with compositing**
  - Use case: High-quality masked video generation with proper background preservation using differential diffusion and compositing
  - *From: Kijai*

- **Multiple prompt conditioning with self attention split**
  - Use case: Generate videos with different prompt conditions using pipe syntax and attention splitting
  - *From: Kijai*

- **Automated movie generation with LLM nodes**
  - Use case: Competition entry with 1-12 scenes, fully automated except image selection
  - *From: AJO*

- **Multiple samplers for depth LoRA control**
  - Use case: Cutting depth LoRA short by splitting the process
  - *From: Kijai*

- **WanRestyledFirstFrameWorkflow**
  - Use case: I2V generation with style control
  - *From: A.I.Warper*

- **Zero Star + enhance-a-video + SLG combo**
  - Use case: Complex movement inference with high temporal coherence
  - *From: Cseti*

- **Start/end frame control for Fun models**
  - Use case: Better control over video generation with different conditioning for start and end
  - *From: Kijai*

- **Flux ControlNet + Wan-Fun combined workflow**
  - Use case: Complete pipeline taking 2.5mins on RTX 5090
  - *From: ArtOfficial*

- **Start/end frame control with InP model**
  - Use case: Using different strength values (0.2 start, 2.0 end) for morphing effects
  - *From: TK_999*

- **I2V with control and TeaCache**
  - Use case: 44 seconds generation time with TeaCache enabled
  - *From: ArtOfficial*

- **SDXL controlnet combined workflow**
  - Use case: Full generation in under 2 minutes with grayscale lines and depth setup options
  - *From: ArtOfficial*

- **Start/end frame morphing**
  - Use case: Animating between 2 images using i2v with end frame/keyframes
  - *From: Kijai*

- **Last frame as next first frame approach**
  - Use case: Video extension technique for longer sequences
  - *From: DevouredBeef*

- **Depth control with stylized first frame**
  - Use case: Creating style transfer videos while maintaining geometric structure
  - *From: 852話 (hakoniwa)*

- **Trajectory control for object movement**
  - Use case: Controlling specific movement paths of objects in videos
  - *From: Kijai*

- **First frame restyling with control**
  - Use case: Similar to Runway video-to-video, changing style while preserving motion
  - *From: DawnII*

- **Flow edit for video modification**
  - Use case: Using native nodes for video editing workflows
  - *From: chrisd0073*

- **3D animation to stylized video**
  - Use case: Create 3D scene, stylize first frame with CN/SD, use as control for Wan generation
  - *From: 852話 (hakoniwa)*

- **Multi-scene single queue generation**
  - Use case: Generate multiple scenes from single reference image using Gemini for prompting
  - *From: AJO*

- **Colorization workflow using 1-step generation**
  - Use case: Consistently reproduce reference image on all control frames for colorization tasks
  - *From: Pedro (@LatentSpacer)*

- **Start/end frame morphing**
  - Use case: Create smooth transitions between two frames using InP models
  - *From: DawnII*

- **Split prompt with control**
  - Use case: Use different prompts for different parts of video (e.g., waterfall in second prompt)
  - *From: Kijai*

- **Start frame to end frame morphing with InP**
  - Use case: Creating consistent clip transitions using last frame as first frame for next clip
  - *From: Kijai*

- **Latent stitching before VAE decode**
  - Use case: Avoiding color shifts by combining latents before final video creation
  - *From: Kijai*

- **Style transfer with Wan control**
  - Use case: Transferring artistic styles like Van Gogh to video
  - *From: 3Dmindscaper2000*

- **First frame styling control**
  - Use case: Take video, change first frame, use as control with changed first frame as I2V input
  - *From: Draken*

- **Viggle gen first then depth map**
  - Use case: Generate with Viggle first, then create depth map for control
  - *From: LarpsAI*

- **Seed finding with 1.3B then v2v with 14B**
  - Use case: Efficient workflow using fast 1.3B for iteration then 14B for final quality
  - *From: yi*

- **Two-stage video generation for complex scenes**
  - Use case: Generate background video, then generate character on alpha layer and overlay for complex scenes with multiple keyframes
  - *From: DawnII*

- **T2V extension using Fun InP with multiple end frames**
  - Use case: Seamless video extension using 16 end frames forwarded as start
  - *From: Kijai*

- **Temporal masking for video inpainting**
  - Use case: Fix specific frames or areas in video using binary mask per 4 frames
  - *From: Kijai*

- **Multi-frame start for consistent animation**
  - Use case: Use 4 start frames for stop-motion like effects
  - *From: VK (5080 128gb)*

- **Model chain for SLG**
  - Use case: model > loras > patch model > teacache > slg > torch.compile > modelsamplingsd3 (shift) > cfg zero star > adaptive guider / ksampler
  - *From: Miku*

- **Multiple image guidance**
  - Use case: Send batch of 4 images to start image to help guide motion
  - *From: DawnII*

- **Two-stage interpolation**
  - Use case: Train 14B to generate intermediary frames, then use 1.3B to fill them
  - *From: mamad8*


## Recommended Settings

- **Block swap**: 40 for low VRAM, 0 for sufficient VRAM
  - Balance between VRAM usage and speed - more blocks = less VRAM but slower
  - *From: Kijai*

- **Frames**: 81 maximum
  - Wan doesn't support 121 frames, use 81 max for best stability
  - *From: yi*

- **Steps**: 30+
  - Slow model needs sufficient steps for good results
  - *From: Shawneau 🍁 [CA]*

- **FP16 base precision**: Enable for fp16 accumulate
  - Required for automatic fp16 accumulate with new PyTorch
  - *From: Kijai*

- **Frame rate**: 16 frames/second
  - Wan uses 16fps as standard
  - *From: yi*

- **Sampler**: UniPC (specifically uni_pc_bh2)
  - Significantly better results than DPM++, especially for texture detail
  - *From: Kijai*

- **Shift**: 5 (default) or 8-15 with context options
  - Default works best for most cases, higher values only with context windowing
  - *From: toyxyz/seitanism*

- **Frame count**: 81 frames
  - Model's default, going over causes artifacts
  - *From: Kijai*

- **PyTorch fp16 accumulation**: torch.backends.cuda.matmul.allow_fp16_accumulation = True
  - ~20% speed improvement
  - *From: Kijai*

- **ComfyUI fast mode**: --fast fp16_accumulation
  - Better quality than fp8, new parameter format
  - *From: Kijai*

- **V2V denoise**: 0.2
  - Good for cleanup passes without over-processing
  - *From: Draken*

- **Sampler choice**: UniPC over dpm++
  - Better quality results for WAN
  - *From: David Snow*

- **Model precision**: fp16 over fp8
  - fp8 matrix multiplication performs poorly on WAN
  - *From: comfy*

- **Power limit**: 495W (from 450W default)
  - Slight performance improvement
  - *From: Benjimon*

- **GPU memory clocks**: nvidia-smi -ac 7000,1725
  - Maximum performance state
  - *From: fredbliss*

- **CFG scheduling**: List of floats, exactly 1.0 to skip uncond
  - Speed optimization
  - *From: Kijai*

- **Transformers version**: 4.39.0 or 4.49.0
  - Compatibility with Florence nodes
  - *From: ˗ˏˋ⚡ˎˊ-*

- **TeaCache threshold**: 0.03-0.04
  - Good balance of speed and quality
  - *From: Kijai*

- **TeaCache start_step**: 6-12 depending on total steps
  - Higher start_step for more steps (12 for 50 steps, 6 for 30 steps) to avoid noise
  - *From: Kijai*

- **Recommended model settings**: fp8 weight, fp16 or fp16_fast base_precision, unipc sampler, feta 3-4
  - Optimal performance configuration
  - *From: Kijai*

- **Recommended resolution**: 832x480, 848x480, or 848x432
  - Good baseline resolutions, with 832x480 mentioned in official script
  - *From: seitanism*

- **Block swap for 16GB VRAM**: 28 blocks
  - Allows TeaCache to work without OOM on 16GB cards
  - *From: DevouredBeef*

- **Denoise for upscaling**: 0.2-0.3
  - Good balance for second pass upscaling without changing too much
  - *From: N0NSens*

- **Steps for 1.3B upscaling**: 10 steps
  - Sufficient for upscaling pass with 1.3B model
  - *From: N0NSens*

- **Text encoder quantization**: fp8
  - Frees up ~4GB VRAM
  - *From: Kijai*

- **TeaCache frame count**: 81 frames
  - Avoids glitch issues that occur with 73 frames
  - *From: Kijai*

- **Steps for quality**: 50-60 steps
  - No real benefits above 50-60 steps for most use cases
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Precision for 3090**: e5m2 quantization
  - torch.compile on 3000 series only works on e5m2
  - *From: Kijai*

- **fp16 accumulation**: torch.backends.cuda.matmul.allow_fp16_accumulation = True
  - Provides significant speed improvements
  - *From: Kijai*

- **Block swap**: 40
  - Required for 81 frames at 1280×720 on 4090 to avoid OOM
  - *From: burgstall*

- **TeaCache start step**: 7 for 30 steps
  - Start after initial noise, avoid false hits. Default settings are for 30 steps
  - *From: Kijai*

- **Context frames**: 81
  - What the model does best, though can work with other values in latent space
  - *From: Kijai*

- **Context overlap**: 24
  - 16 overlap not enough for morphing, 24 shows better results
  - *From: Kijai*

- **Enhance A Vid weight**: Under 2
  - Weights above 2 don't seem like a good idea
  - *From: toyxyz*

- **RifleX**: 4
  - Recommended setting for improved motion stability
  - *From: Kijai*

- **context_frames**: 81
  - Good balance for context window processing
  - *From: fredbliss*

- **context_overlap**: 16
  - Provides smooth transitions between windows
  - *From: fredbliss*

- **target_fps**: 2.0
  - Apollo paper recommendation for best temporal understanding
  - *From: fredbliss*

- **original_fps**: 30
  - Average baseline for training data expectations
  - *From: fredbliss*

- **TeaCache threshold**: 0.05 max
  - Higher values like 0.15 cause quality degradation
  - *From: Kijai*

- **reflex_freq_index**: 0
  - Default value of 1 causes bad results with UniPC
  - *From: Mngbg*

- **teacache start_percent**: 0.20
  - Prevents motion loss while maintaining speed benefits
  - *From: JmySff*

- **target_fps for interpolation**: target_fps * interpolation_factor = final_fps
  - Proper setup for FPS sampling workflow
  - *From: fredbliss*

- **context overlap**: 32 for long scenes
  - Doubling context overlap helps with complex car scenes
  - *From: fredbliss*

- **rel_l1_thresh for TeaCache**: 0.05
  - Low enough threshold for no noticeable quality impact but faster speed
  - *From: Screeb*

- **Scheduler for unipc_bh2**: not karras, exponential, or linear quadratic
  - These schedulers don't work well with unipc_bh2
  - *From: Kijai*

- **Sampler for native i2v**: dpmpp_2m with beta scheduler
  - Most reliable combination for i2v
  - *From: David Snow*

- **Steps with TeaCache**: 30 steps with TeaCache vs 15 without
  - Should compare equivalent generation times, not same step counts
  - *From: Kijai*

- **base_precision**: fp16 or bf16
  - Cannot be fp8, this is what calculations are done at
  - *From: Kijai*

- **quantization**: Match fp8 weight if using
  - What the weights will be loaded to, can be lower than weight precision
  - *From: Kijai*

- **offload**: main_device instead of offload
  - Fixes Triton pointer access errors
  - *From: GalaxyTimeMachine*

- **eta value in RES4LYF**: 0.0 for deterministic, >0.0 for SDE sampling
  - Controls noise exchange per step
  - *From: Ablejones*

- **TeaCache start percentage**: 0.2 minimum, 0.5-0.6 for low steps
  - Prevents quality degradation from early step skipping
  - *From: Miku*

- **Block swap for 12GB VRAM**: 40+
  - Prevents OOM on i2v workflows
  - *From: Kijai*

- **Steps for i2v face quality**: 20+ steps
  - 15 steps insufficient for good face consistency
  - *From: Draken*

- **noise_aug_strength**: 0.02
  - Significantly improves motion in I2V realistic content
  - *From: Juampab12*

- **context_length**: 81
  - Default chunk size for context windowing
  - *From: Kijai*

- **swap_block**: 20 (reduced from 40)
  - Saves 20 seconds generation time
  - *From: Ashtar*

- **TeaCache start range**: 0.5-1.0
  - Reduces quality degradation while maintaining speed benefits
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Data type**: bf16 instead of fp16
  - Significantly better quality output
  - *From: AJO*

- **TeaCache start**: start_0
  - No quality degradation while speeding up generation significantly
  - *From: Bleedy (Madham)*

- **Context overlap**: 24
  - Good balance for maintaining original image consistency
  - *From: Cubey*

- **TeaCache threshold**: 0.2-0.3 for 1.3B model
  - Only setting that triggers TeaCache on 1.3B model
  - *From: Kijai*

- **Sampling steps**: 10-30 steps work well
  - Official repo defaults of 40-50 steps are overkill, depending on shift/cfg settings
  - *From: chancelor*

- **Default shift/cfg**: shift 5, cfg 5
  - Standard settings from official repo
  - *From: Doctor Shotgun*

- **Block swap**: 0 (disabled)
  - Significant slowdown when enabled
  - *From: deleted_user_2ca1923442ba*

- **Latent upscale method**: bilinear or bicubic
  - Latent upscale is bad, if must use then at least these methods
  - *From: Kijai*

- **PyTorch nightly command**: pip install --pre -U torch torchvision --index-url https://download.pytorch.org/whl/nightly/cu126
  - 20% speed increase with fp16 accumulation
  - *From: Kijai*

- **Fast fp16 accumulation flag**: --fast fp16_accumulation
  - Global ComfyUI startup argument for speed boost
  - *From: Kijai*

- **Context window overlap**: 22 (doesn't need to be multiple of 4)
  - Flexibility in overlap settings
  - *From: Cubey*

- **motion_smoothness**: 0.5
  - Recommended for latent interpolation to avoid issues
  - *From: fredbliss*

- **teacache start_percent**: not too low
  - Prevents artifacts and noise, but native uses percentage while wrapper uses step numbers
  - *From: JmySff*

- **processing.py tile size**: 256 instead of 512
  - Reduces VRAM usage for upscaling workflows
  - *From: David Snow*

- **generation_fps**: 8
  - For fast action with interp=2 to get 16fps output
  - *From: fredbliss*

- **motion_smoothness**: 0.2
  - Lower values work better for fast action scenes
  - *From: fredbliss*

- **teacache_start_step**: 2
  - Allows 50 steps without turning to complete garbage, good for prototyping
  - *From: DevouredBeef*

- **steps**: 20
  - Sweet spot - anything over doesn't make huge difference, 10 works for toon style
  - *From: VRGameDevGirl84(RTX 5090)*

- **context_frames**: 81
  - Use constant int node since FPS config slider limits to 80
  - *From: TK_999*

- **Generation FPS**: 2.0
  - For cinema 24fps preset with 12x interpolation factor
  - *From: fredbliss*

- **TorchCompile mode**: cudagraph
  - Avoids Triton dependency and is much faster than inductor
  - *From: Neex*

- **Block swap**: disabled
  - When you have sufficient VRAM (48GB+), disabling saves time
  - *From: Draken*

- **TeaCache**: gpu
  - Provides tiny speed improvement when VRAM allows
  - *From: Draken*

- **TeaCache with coefficients**: threshold=0.3, start_step=2
  - Achieves similar speed to non-coefficients version while maintaining better quality
  - *From: DevouredBeef*

- **Frame count**: 81 frames
  - Optimal frame count, anything else produces worse results
  - *From: Kijai*

- **Steps for quality vs speed balance**: 25-50 steps
  - 25 steps minimum for decent results, 40-50 for high quality
  - *From: maitr3ya*

- **noise_aug_strength for i2v**: 0.01-0.03
  - Helps prevent yellow tinting issues in i2v, higher values may reduce quality
  - *From: Juampab12*

- **TeaCache start_step with coefficients**: 0 or 2
  - Coefficients version may not require start_step offset, can potentially start from 0
  - *From: Kijai*

- **TeaCache threshold**: 0.3 (30%)
  - New coefficients require about 10x higher value than old implementation
  - *From: Juampab12*

- **VRAM usage with context**: 169 frames in 2 mins with contexts, VRAM used 4.281 GB
  - Efficient memory usage with context windows
  - *From: Kijai*

- **I2V generation time**: 14 min to generate at 832x480x129
  - Gets 5 seconds out of it basically and an upscale of 2.5ish for resolution of 2218x1280, 24fps
  - *From: Bleedy (Madham)*

- **Block swap for 3080 12gb**: 40 blockswap for 20 steps/832x480/81 frames
  - Takes 9 min with TeaCache, uses more than 40 gigs of system ram
  - *From: garbus*

- **Context window size**: 81
  - Best context window size for quality
  - *From: Kijai*

- **Context overlap for I2V**: 24
  - Best overlap setting for 81 context I2V runs
  - *From: Cubey*

- **Block swap for 16GB VRAM**: 25-40
  - Prevent OOM, increase until VRAM not at 99%
  - *From: Juampab12*

- **Guidance end**: 0.8
  - Used in successful 120 frame generation
  - *From: Benjaminimal*

- **Default precision without arguments**: SAGE with FP8
  - Automatic fallback when no precision specified
  - *From: intervitens*

- **I2V resolution handling**: Downscales to 1280x720 area preserving aspect ratio
  - No cropping but doesn't generate exact set resolution unless manually cropped
  - *From: intervitens*

- **Vertical video resolution**: 720x960
  - Works better than other aspect ratios for vertical content
  - *From: Juampab12*

- **WanVideo BlockSwap**: Adjust until VRAM usage stays under 23GB
  - Prevents VRAM overflow based on generation resolution
  - *From: jellybean5361*

- **TeaCache old settings**: 6-8 start step with 20 steps, 0.04 thresh
  - Previous working configuration
  - *From: Cubey*

- **TeaCache new default**: 1 step start, 0.3 thresh
  - More aggressive new coefficients
  - *From: Cubey*

- **Long video context**: context_frames: 54, context_stride: 4, context_overlap: 16
  - For extended video generation
  - *From: Organoids*

- **Multi-GPU not beneficial**: ring_size 8 same speed as 4 GPUs
  - No performance gain with higher ring_size
  - *From: aikitoria*

- **TeaCache threshold**: 0.3
  - New default value range, old workflows need updating from previous values
  - *From: Kijai*

- **CFG for poses**: 8
  - Higher CFG (8 vs 6) helps prevent people from walking away when posing
  - *From: Shawneau 🍁 [CA]*

- **Steps for quality difference**: 50 vs 20
  - Significant quality improvement observed between 20 and 50 steps
  - *From: Juampab12*

- **DPM++ 2SA for quality**: 200 steps, eta 2.0, s_noise 1.07
  - Good quality results if willing to wait longer
  - *From: deleted_user_2ca1923442ba*

- **Context frames minimum**: 81
  - Lowest context frame count that works well
  - *From: Kijai*

- **Block swap for 24GB VRAM**: 20 blocks
  - For 832x832, 81 frames on 24GB VRAM system
  - *From: zoz*

- **TeaCache for 1.3B**: 0.25, 1, -1 with context stride 8
  - Works well and really fast at 12.89s/it
  - *From: Organoids*

- **CFG distillation training steps**: 1200 steps for 1.3B LoRA
  - Sufficient for good results, can go up to 20k steps max
  - *From: spacepxl*

- **TeaCache rel_l1**: 0.25 with coefficients
  - Works great on 480p I2V
  - *From: Kijai*

- **Context frames and overlap**: context_frames: 81, context_stride: 4, context_overlap: 16
  - Standard settings for longer generation
  - *From: Organoids*

- **Block swapping**: 26 blocks for 832x640, 34 blocks for 720x1280
  - To fit in 24GB VRAM
  - *From: Benjimon*

- **Steps**: 20 steps
  - Good balance of quality and speed
  - *From: Benjimon*

- **FPS**: 16 fps
  - Standard setting used in examples
  - *From: Benjimon*

- **Flow shift**: 5.0
  - Standard parameter used
  - *From: Benjimon*

- **TeaCache rel_l1_thresh**: 0.25 for larger models, 0.06 for 1.3B
  - Default recommended values for different model sizes
  - *From: Kijai*

- **TeaCache start step**: 0 or 1, can start much earlier after update
  - Can start TeaCache from beginning now
  - *From: Kijai*

- **Block swap size**: 40 maximum, using ~18GB VRAM vs 34GB without
  - Optimal memory usage
  - *From: Gateway {Dreaming Computers}*

- **Context windows configuration**: 32 frame windows, 8 context stride, 4 overlap
  - For 129 frame long video generation
  - *From: Organoids*

- **Enhance a Video strength**: 0.32
  - Sweet spot with teacache settings
  - *From: JmySff*

- **14B model steps**: 20+ steps
  - May need more steps than 1.3B model for quality
  - *From: burgstall*

- **Torch compile transformer block**: Enabled
  - Provides 20-30% speed boost
  - *From: Kijai*

- **Block swapping**: 20-22 blocks for 1280x720x81 on 5090
  - Maximizes VRAM usage without excessive slowdown
  - *From: seitanism*

- **CFG scheduling**: CFG 6 for 80% of steps, CFG 1 for last 20%
  - May reduce overfrying and improve quality
  - *From: seitanism*

- **Steps**: 30-50 steps
  - 30 steps adequate but 50 gives different/potentially better results
  - *From: seitanism*

- **TeaCache**: 0.4 for seed hunting
  - Good balance of speed vs quality for testing
  - *From: ArtOfficial*

- **TeaCache threshold**: 0.275-0.3 max
  - Balance between speed and quality
  - *From: Kijai*

- **TeaCache start step**: 1
  - Optimal performance
  - *From: Kijai*

- **Block swap amount**: 10-15 blocks
  - Good balance for 24GB VRAM
  - *From: Kijai*

- **Text encoder precision**: fp8
  - Saves RAM
  - *From: Kijai*

- **TeaCache**: 0.03 max with old wrapper, higher values with updated wrapper
  - Prevents blurry outputs
  - *From: Kijai*

- **torch nightly**: 2.7.0.dev20250309+cu128
  - Required for latest SageAttention compatibility
  - *From: BestWind*

- **fp16-fast precision**: recommended with fp8 models
  - Faster upcasting performance
  - *From: BestWind*

- **End percentage for control LoRA**: 0.05-0.1
  - Controls when LoRA gets unloaded during sampling
  - *From: Cubey*

- **Denoise for upscaling**: 0.9
  - Used with encoded video for strong transformation
  - *From: Kijai*

- **Target CFG**: 6.5-7
  - Better than 10, provides good control without over-processing
  - *From: Kytra*

- **teacache rel_l1_thresh**: 0.18
  - Good balance of speed vs quality - 15min to 10min with near identical results
  - *From: intervitens*

- **teacache rel_l1_thresh**: 0.3
  - Faster testing at 7.5min but with noticeable artifacts, good for prompt/seed finding
  - *From: intervitens*

- **Block swap**: 25
  - Works well for 1280x720x81 on 4090 with 32GB RAM using fp8 model
  - *From: zoz*

- **Recommended video resolution**: 1280x720
  - Optimal resolution for Wan model
  - *From: aikitoria*

- **torch compile mode**: reduce-overhead
  - Compiles faster than max-autotune-no-cudagraphs
  - *From: Kijai*

- **Power limit for GPU**: 80%
  - Reduces thermal throttling while maintaining performance
  - *From: B1naryV1k1ng*

- **CFG distill strength**: 1.0
  - Stacks properly with other LoRAs
  - *From: spacepxl*

- **Power limit**: 80%
  - More stable clocks and reduces throttling
  - *From: HeadOfOliver*

- **Reserve VRAM**: 3-4GB
  - Allows torch compile + LoRA to work without OOM
  - *From: Kijai*

- **Undervolt**: 2400mhz at 0.865mv
  - Stable performance for 5090 FE
  - *From: pagan*

- **CFG schedule**: 5.5 for first 30% of steps, then 1.0
  - Provides 2x speedup on later steps without major quality loss
  - *From: Juampab12*

- **Context overlap**: 24 frames
  - Helps reduce reset between context windows for static content
  - *From: Cubey*

- **full_load**: disabled
  - Prevents OOM when using torch compile with LoRAs
  - *From: Kijai*

- **TeaCache**: Works for preview
  - Provides speed boost with minimal quality change
  - *From: Kijai*

- **TeaCache threshold**: 0.18-0.2
  - Better quality than previous 0.22 recommendation
  - *From: intervitens*

- **TeaCache start step**: 10
  - Default setting to reduce degradation by disabling for first 10 steps
  - *From: intervitens*

- **CFG steps cutoff**: 15-20
  - Provides 2x speedup for remaining steps with minimal quality impact
  - *From: intervitens*

- **Minimum steps for quality**: 40+
  - Under 40 steps causes artifacts, especially with fast movement
  - *From: aikitoria*

- **LoRA rank**: 16
  - Required rank setting for ControlNet LoRA compatibility
  - *From: Benjaminimal*

- **block_swap**: 40
  - Needed for dual LoRA workflows on 24GB VRAM to prevent crashes
  - *From: burgstall*

- **blur for tile LoRA**: 10-15px at sigma 0.3
  - Prevents overcooked details and maintains quality
  - *From: spacepxl*

- **tile LoRA strength**: 1.0
  - Works better at full strength than reduced strength
  - *From: spacepxl*

- **T2V model choice**: 1.3B for T2V, 14B 480p for I2V
  - Recommended for RTX 4090
  - *From: Juampab12*

- **quantization**: fp8
  - Recommended over fp16/bf16 for efficiency
  - *From: Juampab12*

- **Skip block index**: 10
  - Consistently improves quality on 14B model
  - *From: aikitoria*

- **VAE precision**: fp32
  - Very slightly better for encoding quality
  - *From: Kijai*

- **Model precision**: fp16
  - 20% faster than bf16 on RTX 4090 with better results
  - *From: aikitoria*

- **CFG end percentage**: 0.5
  - Use high CFG for first half, CFG 1 for second half
  - *From: Payuyi*

- **Block swap for 16GB VRAM**: 25 blocks
  - Balance between speed and memory usage - 30 blocks too slow, 10 blocks too memory intensive
  - *From: N0NSens*

- **SLG layer**: 10
  - Carries motion information, best results for prompt adherence
  - *From: TK_999*

- **SLG end percent**: 0.3 or 1.0
  - Better results at 0.3 according to testing
  - *From: IllumiReptilien*

- **Control tile blur**: 12px radius, 0.3 sigma
  - Prevents oversharpening artifacts, starting point for good results
  - *From: spacepxl*

- **Control tile shift**: 1 instead of 8
  - Increases fine detail and texture definition
  - *From: Payuyi*

- **CFG for control lora**: 6.0
  - Makes control effect stronger
  - *From: spacepxl*

- **SkipLayerGuidanceDiT timing**: End very early (30/30 steps took 1.48s/it vs 1.32s/it)
  - Minimal slowdown when ended early
  - *From: Kijai*

- **TeaCache preview steps**: 8-10 steps with Euler sampler
  - Works well for previews unlike uni_pc
  - *From: mamad8*

- **Video format for Discord**: H264 instead of H265
  - Better compatibility across platforms
  - *From: ramonguthrie*

- **Duo sampler configuration**: 20 steps normal CFG + 10 steps 1 CFG
  - Speed improvement while maintaining quality
  - *From: CapsAdmin*

- **Skip layer guidance**: 9
  - Good general value
  - *From: kendrick*

- **SLG start time for 1.3B**: 0.1
  - Key for 1.3B quality improvement
  - *From: Kijai*

- **Frames per second**: 16
  - Model generates at 16 fps, not configurable as no fps conditioning in training
  - *From: Kijai*

- **SLG start/end range**: 0.1-0.9
  - Seems fine for general use
  - *From: Kijai*

- **SLG block for 1.3B model**: 8 or 9
  - 1.3B model only has 30 blocks vs 40 for larger models
  - *From: Kijai*

- **Block swap for 14B fp16**: 27/40 uses ~22GB VRAM, all blocks ~12GB
  - Memory management for different VRAM capacities
  - *From: Kijai*

- **Steps for testing**: 25 steps
  - Common setting used in examples
  - *From: Cseti*

- **TeaCache rel_1**: 0.07 for 1.3B model, 0.19+ for larger models
  - 1.3B requires much lower values than larger models
  - *From: IllumiReptilien*

- **SLG blocks**: 6-9 for 1.3B, 9-10 for 14B
  - Optimal range for quality improvement without breaking generation
  - *From: Kijai*

- **SLG start/end**: 0.3-0.9 instead of 0.1-0.9
  - Less destructive, reduces slow-motion effects
  - *From: Kijai*

- **CFG with SLG**: 3.0 when using SLG on multiple blocks
  - Lower CFG needed since SLG strengthens guidance effect
  - *From: Kijai*

- **Block swap**: 20 or lower for L40 48GB
  - Prevents CPU memory overflow on high VRAM but limited RAM systems
  - *From: Kijai*

- **Compile transformer blocks**: transformer blocks only vs full model
  - Full model compile wasn't faster and sometimes gave cryptic errors
  - *From: Doctor Shotgun*

- **TeaCache threshold**: Very low value
  - To effectively disable TeaCache when testing other optimizations
  - *From: Kijai*

- **LoRA blocks**: First 20 blocks enabled, singles off
  - Improves LoRA quality based on Hunyuan technique
  - *From: Cubey*

- **SLG blocks**: 9 instead of 10
  - Block 10 causes black areas, 9 fixes the issue
  - *From: Kijai*

- **fp8 quantization**: e4m3fn instead of e4m3fn_fast
  - Fast version creates noise artifacts
  - *From: Kijai*

- **Frame limit**: Under 88 frames
  - Past 88 frames can cause glitches
  - *From: Kijai*

- **SLG with LoRA**: 6 instead of 9
  - 9 gives weird VHS-like outputs with artifacts
  - *From: crinklypaper*

- **context_frames**: 64-81 for standard, 96-128 for complex motion, 32-48 for memory-constrained
  - Balance between quality, memory usage, and motion capture capability
  - *From: fredbliss*

- **context_stride**: 4-8 for smoother results, 16-24 for faster generation
  - Smaller values create more overlap but may be redundant, larger values are faster
  - *From: fredbliss*

- **context_overlap**: 8-12 minimal, 16-24 standard, 32-48 extra-smooth
  - More overlap means smoother transitions but higher computation cost
  - *From: fredbliss*

- **loop_shift**: 6 for 49 frames, generally half the latent count
  - Proper overlap for seamless looping, 1 latent = 4 frames
  - *From: Kijai*

- **shift_skip**: 4-6
  - Significantly affects video quality in loop generation
  - *From: TK_999*

- **context window overlap**: 16
  - Should always be approximately this value
  - *From: Kijai*

- **CFG**: 3.0
  - Works great with SLG
  - *From: avataraim*

- **steps for LoRA quality boost**: 10
  - Achieves 20-step quality with speed LoRA
  - *From: VRGameDevGirl84(RTX 5090)*

- **SLG Skip**: 9
  - Works well with 1.3B model starting at 0.3 end 0.9
  - *From: Kijai*

- **SLG for 14B**: 10 block with 0.0 start and 0.3 end
  - Good results without face distortion
  - *From: Cubey*

- **TeaCache start**: 15
  - Avoids TeaCache destroying the output
  - *From: Cubey*

- **Multi-GPU tea cache**: threshold 0.2 after 10 steps
  - Part of optimized multi-GPU workflow
  - *From: aikitoria*

- **CFG disable**: after 25 steps
  - Used in fast multi-GPU workflow
  - *From: aikitoria*

- **blockswap**: 40
  - Allows 81 frames at 1280x720 on 4090
  - *From: Jas*

- **rope_function**: comfy
  - Required setting to avoid validation errors
  - *From: Kijai*

- **TeaCache threshold**: lower than default
  - Prevents blob distortions when using multiple LoRAs
  - *From: Kijai*

- **VAE precision**: bf16
  - Prevents OOM during decode
  - *From: Kijai*

- **cfg values**: 4.0 first pass, 6.0 second pass
  - Works well with depth control LoRA
  - *From: ˗ˏˋ⚡ˎˊ-*

- **CFG**: 3.0
  - Dropping CFG made Pikachu more animated/active
  - *From: Kijai*

- **Steps for depth control**: 25-30
  - Good balance of quality and speed with UniPC sampler
  - *From: IllumiReptilien*

- **Context window overlap**: 17
  - Works better with VAE context windows when freenoise is off
  - *From: Flipping Sigmas*

- **Reserve VRAM**: Set to system usage amount
  - Prevents memory issues with patches like Sage and Tea cache
  - *From: Kijai*

- **Divisible by**: 16
  - Prevents errors with image processing in resize nodes
  - *From: Kijai*

- **3090 performance**: 5-8 s/it
  - With all speedups enabled for 480p 81 frames
  - *From: LarpsAI*

- **Sampling frames**: 81 frames at 480x832 with 20 steps
  - Example timing: 2:35 duration, 7.79s/it
  - *From: Kijai*

- **ClipVision strength for start/end**: 0.8 strengths for both clips with average
  - Balanced control between keyframes
  - *From: The Shadow (NYC)*

- **Control LoRA strength**: 1.3 strength
  - For anime style control LoRA application
  - *From: 852話 (hakoniwa)*

- **TeaCache for 1.3B model**: Lower settings than 14B
  - Model-specific optimization requirements
  - *From: DawnII*

- **SLG threshold**: 0.15-0.3 range
  - Proper activation range, 0.05 too low to trigger effectively
  - *From: Kijai*

- **Steps for quality**: 35-50 steps
  - No benefit seen from going over 50 steps
  - *From: Benjimon*

- **Noise aug strength**: 0 for wrapper when not using embeds
  - Disable when not providing embeddings
  - *From: Kijai*

- **TeaCache threshold for bypass**: Very low like 0.05
  - To minimize TeaCache effect when SLG patch is required
  - *From: Kijai*

- **TeaCache threshold**: 0.25
  - Good balance, quality loss above 0.2
  - *From: Kijai*

- **Noise injection strength**: 0.8
  - Helps with motion similar to iPA
  - *From: The Shadow (NYC)*

- **Block swap for 14B model**: 10 blocks for RTX 5090
  - Stable for 10-second videos, 5 blocks might be faster
  - *From: const username = undefined*

- **Steps for differential diffusion**: 10, 20, 60 steps
  - Higher counts needed to bring in original video details
  - *From: David Snow*

- **noise_aug_strength**: 0.095
  - For better I2V motion quality
  - *From: const username = undefined;*

- **denoise strength**: 0.3
  - When using control LoRA, allows for 2-pass generation
  - *From: Flipping Sigmas*

- **skip layer guidance**: 8, 9, 10
  - Recommended layers for SLG
  - *From: David Snow*

- **video resolution preference**: 768x768x204f or 544x992x102f for I2V
  - Better quality than 544x992x204f
  - *From: deleted_user_2ca1923442ba*

- **Block swap**: 32-34
  - Should allow running 720p on 4090
  - *From: Benjimon*

- **Full offloading with fp8 I2V model**: ~10 blocks
  - Uses ~12GB VRAM at 720p with 81 frames
  - *From: Kijai*

- **Depth controlnet blending**: 0.5 opacity
  - Produces more natural colors
  - *From: VK (5080 128gb)*

- **Original latents denoise**: 0.95
  - Used with controlnet for good results
  - *From: VK (5080 128gb)*

- **Block swap for 4090 fp8**: 20 blocks
  - Should be sufficient, 40 blocks makes RAM problems worse
  - *From: Kijai*

- **Context shift for 49 frames**: 6
  - Default recommended by Wan team
  - *From: Kijai*

- **RoPE function**: comfy
  - Enables full torch compile and reduces VRAM usage
  - *From: Kijai*

- **Steps for better quality**: 40+
  - 20 steps often looks grainy with weird motion
  - *From: Faust-SiN*

- **Standard i2v 480p settings**: uni_pc sampler, simple scheduler, 6 CFG, 20 steps
  - Community standard configuration
  - *From: Organoids*

- **Torch compile defaults**: inductor backend, full graph false, default mode, dynamic false, 64 cache size, compile transformer blocks only true
  - Standard configuration that works
  - *From: Kijai*

- **CFG-Zero-star use_zero_init**: true (default from demo)
  - Default setting from official demo, though purpose unclear
  - *From: Kijai*

- **Quantization for 1.3B model**: default
  - Prevents Triton errors, quantization not needed for 1.3B anyway
  - *From: Dream Making*

- **Self attention split step**: step 2, then every other step
  - Provides stronger prompt separation without overwhelming the generation
  - *From: Kijai*

- **TeaCache**: 0.2
  - Default 0.25 too high, causes artifacts
  - *From: Faust-SiN*

- **CFG Zero Star steps**: 0
  - 0 steps recommended, higher values like 2-3 may be too much
  - *From: Kijai*

- **SLG block for 1.3B**: 8
  - Best results for 1.3B model
  - *From: Cseti*

- **SLG block for 14B**: 9-10
  - Better results for 14B model
  - *From: Miku*

- **Steps with CFG Zero Star**: 25
  - Can reduce from 35 to 25 steps and get better results
  - *From: Juampab12*

- **CFG**: 3
  - Good results with InP models
  - *From: H（4090）*

- **TeaCache**: 0.010
  - Good starting point for InP 1.3B models
  - *From: JmySff*

- **Control end strength**: 0.2
  - Works well for end frame control
  - *From: Kijai*

- **SLG block start**: 8
  - Works better for 1.3B models when started later
  - *From: Kijai*

- **Zero star steps**: 0
  - Still does effect on first step with that setting
  - *From: Kijai*

- **LoRA strength for control model**: 2.0+
  - Old LoRAs need much higher strength but still don't work well
  - *From: Kijai*

- **Start strength**: 0.2
  - Lower start strength for morphing effects
  - *From: TK_999*

- **End strength**: 2.0
  - Higher end strength doesn't fry image and creates shape transformation
  - *From: TK_999*

- **Frame count for new Fun models**: 81 frames max
  - New InP models support up to 81 frames vs old method's 77+1 latent
  - *From: Kijai*

- **Base precision for 1.3B models**: bf16
  - No fp16 version available for 1.3B model
  - *From: Kijai*

- **CFG for example workflow**: 4
  - Default setting in example workflows
  - *From: seitanism*

- **Tile setting for Fun models**: 0
  - Tiling causes artifacts with new Fun models
  - *From: Kijai*

- **Frame count**: 4n+1 (9, 13, 17, 21, 41, 81)
  - Required mathematical formula for Wan models
  - *From: DawnII*

- **Resolution**: 832x480 or dimensions divisible by 16
  - Model architecture requirements
  - *From: VK (5080 128gb)*

- **TeaCache coefficients**: 0.1-2
  - Good balance of speed and quality
  - *From: HeadOfOliver*

- **TeaCache start step**: 3-6
  - Optimal starting point for cache activation
  - *From: HeadOfOliver*

- **Denoise strength**: 0.6-0.75
  - Prevents unnatural motion artifacts
  - *From: chrisd0073*

- **Control latent strength**: 0.6 start, 0.5 end
  - Good balance for control influence
  - *From: DawnII*

- **Video latent strength**: 0.85
  - Helps significantly with stylized first frame i2v
  - *From: A.I.Warper*

- **Denoise strength**: 0.75
  - Works well with reduced video latent strength
  - *From: A.I.Warper*

- **Steps for quality balance**: 4-20 steps
  - Good balance between speed and quality
  - *From: DawnII*

- **SLG value**: 9
  - Effective setting for wrapper usage
  - *From: DawnII*

- **Steps for Wan**: 30 steps
  - Only amount that always gives good results
  - *From: Draken*

- **TeaCache threshold**: 0
  - Prevents crashes with certain setups
  - *From: AJO*

- **Noise augmentation for control**: 0
  - Default value to preserve image detail
  - *From: Blink*

- **TeaCache start step**: 1
  - With coefficients, generally never skips those steps anyway
  - *From: Kijai*

- **Control embed end**: 0.25
  - Works well for eye movement
  - *From: IllumiReptilien*

- **Block swap amount**: Up to 40
  - For insufficient VRAM situations
  - *From: Kijai*

- **TeaCache threshold for Fun control**: 0.080
  - Lower values needed for 1.3B model
  - *From: Kijai*

- **TeaCache threshold for I2V endframe**: 0.220
  - Higher values for I2V operations
  - *From: workflow examples*

- **Clip encode tiles**: 8 tiles with concat
  - Improves control quality
  - *From: Kijai*

- **Block swap for 4070**: 30-40
  - For efficient 10 minute generations
  - *From: DawnII*

- **Resolution for 480p model**: 832x480
  - Required resolution for 480p model
  - *From: ArtOfficial*

- **Learning rate for 5B model training**: 3e-5
  - Successful training achieving actual video content instead of noise
  - *From: Kytra*

- **Optimal frame count for 1.3B model**: 41 frames
  - Sweet spot before time increases disproportionately
  - *From: VK (5080 128gb)*

- **Batch size calculation for training**: 8 GPUs x 4 grad accumulation x 2 batch = 64 total
  - Proper scaling for learning rate adjustment
  - *From: spacepxl*

- **Learning rate scaling formula**: 1e-4 / sqrt(1024 / 64) = 2.5e-5
  - Proper learning rate scaling based on batch size
  - *From: spacepxl*

- **Standard resolutions for 480p model**: 480x832, 480x856, 560x960, 720x1280
  - Working resolutions for different aspect ratios
  - *From: ChronoKnight*

- **Block swap**: 20 blocks
  - Reduces 16GB VRAM usage to ~14.6GB
  - *From: VK (5080 128gb)*

- **SLG strength**: 0.1 to 0.9
  - Optimal range for SLG workflows
  - *From: DawnII*

- **CFG with SLG**: 3-5
  - Works well with SLG, lower than non-SLG CFG
  - *From: DawnII*

- **Anime LoRA strength**: 0.3
  - Reduces 3D/CGI appearance while maintaining style
  - *From: VK (5080 128gb)*

- **SLG CFG adjustment**: Half of normal CFG (e.g., 6 becomes 3)
  - When using SLG, reduce CFG to half normal value
  - *From: Miku*

- **SLG block skip**: Block 8 or 9 only
  - Works better than other blocks, though difference isn't huge
  - *From: Benjimon*

- **Enhance a video value**: 4 for max frames
  - Needs to be set based on frame count
  - *From: Kijai*

- **Aesthetic LoRA strength**: 0.2
  - Gets benefits without having to alter CFG
  - *From: David Snow*


## Concepts Explained

- **Block swap**: Trade-off mechanism - more blocks swapped = less VRAM used but slower generation speed
  - *From: Kijai*

- **Context window**: Only the context frames are processed at once, allows longer videos by processing in segments with overlap
  - *From: Kijai*

- **FP16 accumulate**: Compute optimization that provides 20-30% speed increase, requires PyTorch 2.7.0 nightly
  - *From: Kijai*

- **Rope artifacts**: Structural issue causing dot patterns and pixel fog, especially in 1.3B model. Not texture issue but positional encoding problem
  - *From: deleted_user_2ca1923442ba*

- **fp16 accumulation**: FP16 GEMM accumulation available on Volta+ GPUs, trades numerical precision for performance gains
  - *From: Kijai*

- **--fast 2 flag**: Enables fp16 accumulation in ComfyUI launcher
  - *From: Miku*

- **fp16_accumulation**: New ComfyUI optimization parameter that improves quality over fp8 matrix multiplication for WAN
  - *From: comfy*

- **Context sliding window**: Technique that uses overlap and blending to generate longer videos by mixing separate runs together
  - *From: Draken*

- **Dither pattern**: Visual artifact appearing as small box textures, particularly noticeable in native WAN implementation
  - *From: Colin*

- **Second pass workflow**: Using one model for initial generation, then another model for refinement at low denoise
  - *From: David Snow*

- **Context windowing/sliding window**: Technique for generating very long videos by processing overlapping segments
  - *From: Kijai*

- **TeaCache**: Optimization that graphs model input/output to calculate when steps can be skipped and cached
  - *From: Kijai*

- **CLIP Vision in I2V**: Uses encoded image with CLIP image assistance for image-to-video generation
  - *From: Kijai*

- **TeaCache**: Caching technique that skips redundant computation steps by comparing time embedding vs model output, originally from Alibaba team. Kijai's implementation uses direct L1 distance thresholding instead of polynomial fitting
  - *From: Kijai*

- **naiveTeaCache**: Kijai's simplified TeaCache implementation that doesn't use polynomial fitting coefficients to scale accumulated relative distances, just uses direct thresholding
  - *From: Kijai*

- **Block swapping**: Offloading model blocks between VRAM and RAM to manage memory usage, but requires sufficient RAM
  - *From: Kijai*

- **TeaCache threshold**: Adjustable parameter that controls how much caching is applied, affects quality vs speed trade-off
  - *From: Draken*

- **cfg split**: Technique to optimize memory usage during generation
  - *From: seitanism*

- **TeaCache**: Caching system that recognizes input/output correspondence to speed up generation, doesn't work with stochastic samplers that add noise every step
  - *From: Kijai*

- **Scaled fp8**: fp8 weights are scaled to use full range - if weight values go from -1.0 to 1.0 but fp8 can represent -448 to 448, multiply by 448 and store 1/448 for unscaling to avoid wasted precision
  - *From: ˗ˏˋ⚡ˎˊ-*

- **SDE sampler**: Stochastic sampler that adds noise every step, works well but prevents TeaCache from triggering due to always changing inputs
  - *From: deleted_user_2ca1923442ba*

- **fps sampling**: Sampling frames at consistent time intervals (e.g., 2 fps) rather than uniformly distributing across video length, maintains temporal coherence
  - *From: fredbliss*

- **Context windowing**: Processing videos in overlapping chunks - context_frames (81) processed at once with context_overlap between windows
  - *From: Kijai*

- **Block swap**: Memory management technique that swaps transformer blocks between CPU and GPU to reduce VRAM usage
  - *From: Kijai*

- **TeaCache threshold**: Controls how aggressively TeaCache skips steps - too aggressive skips too many and leaves noise
  - *From: Kijai*

- **FPS sampling**: Frames sampled at consistent rate (e.g. 2fps) maintaining time intervals, vs uniform sampling which distributes frames evenly regardless of timing
  - *From: fredbliss*

- **Context windowing**: Processing video in overlapping windows of frames, then blending results in overlapping regions for seamless output
  - *From: fredbliss*

- **SLERP interpolation**: Spherical Linear Interpolation - like walking a straight line but on a sphere, faster but less precise than linear
  - *From: TK_999*

- **FPS-based sampling**: Generate fewer frames at lower FPS then interpolate to target framerate for better consistency and quality
  - *From: fredbliss*

- **Adaptive Guidance**: Automated way to set CFG=1 during workflow, provides speed improvements similar to teacache
  - *From: TK_999*

- **Context scheduling**: Managing how many frames and overlap are processed together, with settings like 21 frames, 1 stride, 4 overlap
  - *From: fredbliss*

- **Adaptive Guidance**: Automated CFG scheduling that skips CFG on some steps to make generation faster
  - *From: Kijai*

- **TeaCache**: Caching system that can achieve 1.5x to 3x speedup with acceptable visual quality loss
  - *From: Bleedy*

- **fp16 accumulation**: Optimization requiring PyTorch 2.7.0 nightly for improved performance
  - *From: Kijai*

- **Creativity parameter**: Same as denoising strength in auto, denoise in comfy's default sampler, start_step in other nodes
  - *From: mcmonkey*

- **base_precision vs quantization**: base_precision is what calculations are done at (can't be fp8), quantization is what weights are loaded to (can be lower)
  - *From: Kijai*

- **TeaCache implementation**: Compares modulated time embed to model output after transformer blocks using relative distances
  - *From: Kijai*

- **TeaCache percentage vs steps**: Native uses 0-1 percentage, wrapper shows actual step numbers - same thing expressed differently
  - *From: Kijai*

- **Latent guides**: Method to influence generation direction with input images without full i2v, can add character or colors
  - *From: Ablejones*

- **SDE vs ODE sampling**: eta=0 gives deterministic ODE sampling, eta>0 gives stochastic SDE sampling with noise exchange
  - *From: Ablejones*

- **Context windowing**: Method to generate long videos by processing in chunks of 81 frames with overlapping windows to maintain temporal consistency
  - *From: Kijai*

- **RifleX**: Alternative method for generating longer videos that adjusts RoPE to break looping but can introduce its own artifacts
  - *From: Kijai*

- **Latent guides**: V2V-style technique using latent space manipulation (colors, shapes, movement) to control T2V models without using actual video input
  - *From: Draken*

- **Context windows with multiple prompts**: Using | to separate prompts allows different prompts for different sections of the video, spreading across context windows
  - *From: Kijai*

- **Latents vs pixel frames**: Each latent represents 4 pixel frames, so 20 latents = 80 frames for prompt distribution
  - *From: Kijai*

- **Sliding context**: Method to generate longer videos by processing overlapping windows of frames, avoiding VRAM constraints of full-length processing
  - *From: Draken*

- **TeaCache coefficients**: Mathematical coefficients that determine when TeaCache optimization triggers, different values needed for different model sizes
  - *From: Kijai*

- **FBCache (First Block cache)**: Alternative caching method that doesn't need tuning per model but performs slightly worse than TeaCache
  - *From: Kijai*

- **Context windows**: Method for generating longer videos by processing in overlapping segments, similar to AnimateDiff implementation
  - *From: Kijai*

- **Temporal factor**: Number of images packed in one latent - Cosmos uses 8, Wan/Hunyuan uses 4
  - *From: Kijai*

- **Empty latent nodes**: Create empty tensors with desired shape for model, sampler creates noise based on that shape. Just torch zeroes used as shape guide
  - *From: Kijai*

- **FPS interpolation**: System that generates video at low FPS then fills in intermediate frames using latent interpolation, potentially allowing more diverse videos by letting model fill gaps instead of denoising frame by frame
  - *From: fredbliss*

- **Context windowing**: Method that allows processing longer videos by breaking them into overlapping windows, enables 129+ frame generation
  - *From: Kijai*

- **TeaCache**: Performance optimization that reuses attention calculations to save on redundant computation, but conflicts with some features like context windowing
  - *From: TK_999*

- **Context windows**: Sliding context window allows longer generations by avoiding noticeable switches when stitching i2v last frame to new video
  - *From: NeuralSamurAI*

- **Interpolation factor**: Calculated as max(1, round(output_fps / generation_fps)). When both fps values are same, factor is 1 and no interpolation occurs
  - *From: fredbliss*

- **VAE 4:1 compression ratio**: After VAE decoding, get 4x pixel frames per latent frame due to 1:4 compression
  - *From: fredbliss*

- **Frame density**: Target frames per latent frame - calculated as 0.27 in the example, meaning ~25% frames are generated, rest interpolated
  - *From: fredbliss*

- **Context window coverage**: System that ensures all frames in a sequence are covered by generation windows, can cause issues when missing frames get duplicated to nearest windows
  - *From: fredbliss*

- **FPS vs Uniform Sampling**: FPS sampling maintains consistent video speed during training vs uniform sampling which varies effective speed based on video length, leading to better temporal dynamics learning
  - *From: fredbliss*

- **TeaCache coefficients**: Mathematical coefficients that make TeaCache more precise about which denoising steps to skip, resulting in smarter skipping decisions
  - *From: Kijai*

- **Rectified flow testing limitations**: Can't test things quickly with rectified flow models because reducing steps changes the output significantly
  - *From: deleted_user_2ca1923442ba*

- **TeaCache coefficients**: Model-specific optimization values that allow much higher threshold settings (10x) compared to the old model-agnostic approach
  - *From: Kijai*

- **VAE temporal memory**: VAE has memory of previous frames, so jumping from end to beginning when not looping creates different frame sets that jack up the first few frames
  - *From: Benjaminimal*

- **Temporal compression**: The temporal compression is 4x and VAE is 8x pixels, first frame is special compared to others
  - *From: Benjaminimal*

- **Block swap**: Automatic offloading of model parts in native, manual setting in wrapper to prevent OOM
  - *From: Cubey*

- **FP16 accumulation**: Precision setting that affects which precision to use in wrapper (fp16_fast recommended)
  - *From: Cubey*

- **Adjust resolution**: Feature in clip encode node that automatically adjusts input resolution
  - *From: Kijai*

- **Area-based resolution for I2V**: I2V pipeline only uses total area (w*h) not individual width/height, unlike T2V which needs specific dimensions
  - *From: intervitens*

- **Metal emissivity in thermal imaging**: Metal GPU parts appear cooler than plastic cables in thermal cameras due to lower emissivity, even when actually hotter
  - *From: intervitens*

- **CFG distillation**: Training LoRA to match scaled difference between positive and negative predictions, allowing cfg=1 inference
  - *From: spacepxl*

- **LoRA hook system**: ComfyUI feature for masking and scheduling LoRA weights regionally, like regional prompting but for LoRA application
  - *From: spacepxl*

- **Ring_size and ulysses_size**: Multi-GPU parameters for distributed inference, but higher values don't necessarily improve speed
  - *From: aikitoria*

- **SVDquant Nunchaku inference engine**: Co-designed inference engine that fuses kernels in low-rank branch into low-bit branch to eliminate redundant memory access
  - *From: Ada*

- **VAE flash fix**: Technique to avoid VAE warmup flash by prepending frames - uses 15 frames for encoding, 13 for decoding in vid2vid loops
  - *From: Benjaminimal*

- **Spatial and temporal multidiffusion**: Techniques that can work together to generate higher resolution videos
  - *From: Benjaminimal*

- **Context stride**: How frames are spread in context windows, stride 4 disabled for Wan due to latent space having 4 frames in one latent
  - *From: Kijai*

- **CFG distillation**: Training technique to remove need for CFG guidance, easier than step distillation, works with real data
  - *From: spacepxl*

- **TeaCache coefficients**: Different coefficient values needed for 1.3B models, affects caching behavior
  - *From: Kijai*

- **Block swapping**: Offloads model blocks to system RAM to reduce VRAM usage
  - *From: intervitens*

- **P2P communications**: Peer-to-peer GPU communication for NCCL on consumer GPUs like 4090s
  - *From: aikitoria*

- **VAE tiling**: Technique to process high resolution videos in tiles to manage memory
  - *From: aikitoria*

- **fp16 accumulation**: Has no impact on memory use, you can still use any weights with it, it's just the compute that needs to be done in fp16
  - *From: Kijai*

- **Block swapping vs offloading**: Block swapping is different from offloading to RAM - it strategically swaps model parts between GPU and CPU to optimize memory
  - *From: Gateway {Dreaming Computers}*

- **TeaCache**: Saves some of the work the computer does while turning noise into video and reuses it later, like keeping a shortcut handy to speed up video generation
  - *From: Gateway {Dreaming Computers}*

- **Shift parameter**: Changes the shape of noise schedule - more shift = more steps at high noise (good for structure, bad for details), less shift = opposite
  - *From: spacepxl*

- **Block swap in training**: Similar to inference block swap, allows training larger models by swapping model parts in/out of memory
  - *From: Benjimon*

- **Block swapping**: Memory optimization technique that offloads model blocks to RAM/storage to fit larger models in VRAM
  - *From: Benjimon*

- **Control LoRAs**: LoRA training method using channel concatenation of control signals, similar to instructpix2pix approach
  - *From: spacepxl*

- **Apply Final Norm**: Makes model more literal with prompts, helps with normally censored content, leverages model imagination better than LoRAs in some cases
  - *From: Miku*

- **Block offloading**: Keeps set number of blocks on VRAM, processes with those, then moves to RAM and loads other blocks to VRAM, repeating each step
  - *From: Kijai*

- **JIT compile**: Just In Time compilation - code gets compiled when you run it, like with sageattention triton kernels or torch compile
  - *From: Doctor Shotgun*

- **Context windows for video**: Splits each step into overlapping context windows, runs through model, combines noise_pred results by averaging
  - *From: Kijai*

- **TeaCache**: Caching mechanism that can cause blur if set too high with older wrapper versions
  - *From: Kijai*

- **reshape_weight**: Special key needed for control LoRAs to load correctly in native ComfyUI - contains new shape of the weight
  - *From: comfy*

- **Patch embedding**: Part of the model architecture that needs special handling for control LoRAs with expanded input channels
  - *From: spacepxl*

- **Creative upscaling**: Upscaling that changes content during the process, as opposed to traditional upscaling that preserves original content
  - *From: Draken*

- **Control LoRA**: LoRA trained to accept additional conditioning inputs like blurred video, similar to ControlNet but as LoRA
  - *From: spacepxl*

- **Diffusion forcing**: Combination of autoregressive and diffusion approaches for video generation
  - *From: spacepxl*

- **Rectified flow**: Method to make model learn trajectory and map it to straight line, but nonlinear noise schedule still improves it
  - *From: spacepxl*

- **VACE**: ControlNet Union for DiT - video control system with multiple capabilities
  - *From: Fannovel16 🇻🇳*

- **Block swap**: Memory management technique that can be inefficient for systems with limited RAM
  - *From: Kijai*

- **CFG distillation**: Technique that removes negative prompt requirement and doubles inference speed with minimal quality loss, can be implemented as LoRA
  - *From: chancelor*

- **TeaCache**: Model-specific tuned caching system that reduces VRAM spikes and improves performance
  - *From: intervitens*

- **Differential diffusion**: Technique that prevents masks from being converted to binary internally, works with soft masks
  - *From: ˗ˏˋ⚡ˎˊ-*

- **CFG Distillation**: Technique that allows running at CFG 1.0 for 2x speed by training model to work with lower guidance
  - *From: spacepxl*

- **TeaCache**: Optimization that skips whole inference steps to speed up generation
  - *From: Kijai*

- **Context windows**: Method for generating longer videos by processing in overlapping segments
  - *From: Kijai*

- **Batch CFG**: CFG processing method that has compatibility issues with I2V mode due to tensor size mismatches
  - *From: Juampab12*

- **low_mem_load**: LoRA loading option that uses less VRAM by loading from RAM state_dict, applying weights, then moving to CPU
  - *From: Kijai*

- **TeaCache start step**: Setting to disable TeaCache for initial steps to reduce quality degradation
  - *From: intervitens*

- **matmul**: Matrix multiplication - core operation with set number of units that become bottleneck when fully utilized
  - *From: Cubey*

- **Skip Layer Guidance**: Technique that skips specific layers (8, 9, 10) during unconditioned inference to improve quality
  - *From: IllumiReptilien*

- **force_offload**: Moves models to RAM in Kijai nodes, automatically done in native implementation
  - *From: Kijai*

- **Skip Layer Guidance (SLG)**: Technique that skips unconditional denoising on specific transformer blocks to improve quality
  - *From: aikitoria*

- **Block index**: 14B model has 40 transformer blocks (0-39), 1.3B has 30 blocks (0-29). Index refers to which block to skip during unconditional pass
  - *From: Kijai*

- **Unconditional pass**: Pass through the model with the negative prompt during CFG guidance
  - *From: Kijai*

- **SLG (Skip Layer Guidance)**: Skip layer guidance on negative conditioning, particularly layer 10 - prevents treating good motion in negative conditioning as actually negative
  - *From: TK_999*

- **Frame index manipulation for VAE**: Using non-sequential frame indices like (0,1,1,1,1,5,5,5,5,9,9,9,9) prevents VAE from compressing images, enabling better timelapse training
  - *From: Juampab12*

- **Dataset-specific tokens**: Leftover tokens in T5 like [wiki], [web], [translate] that can target specific training datasets when used in prompts
  - *From: fredbliss*

- **SAE (Sparse Autoencoder)**: Tool trained on T5 for identifying important activations in embeddings, can be used to find meaningful concepts in text
  - *From: fredbliss*

- **Hierarchical embeddings**: Concept of organizing embeddings in parent-child relationships for better scene management
  - *From: fredbliss*

- **SkipLayerGuidanceDiT**: Similar to STG but for DiT models - can improve prompt adherence but may slow down generation
  - *From: Kijai*

- **TeaCache**: Caching mechanism that can be used with high threshold for quick preview generations
  - *From: CapsAdmin*

- **Skip Layer Guidance**: Does extra pass on top of CFG using model without certain layers, different from just skipping uncond on certain layers
  - *From: Kijai*

- **RoPE (Rotary Positional Embedding)**: Basic part of the model for positional encoding, ComfyUI uses different calculation method
  - *From: Kijai*

- **VAE warmup trick**: Method to fix VAE burning/artifacts at the start of generation
  - *From: Kijai*

- **SLG (Skip Layer Guidance)**: Simplified version that skips uncond on specific blocks, provides speed boost by skipping uncond calculation on selected block
  - *From: Kijai*

- **FETA**: From Enhance-A-Video, possibly stands for Frame Enhanced Temporal Attention, calculates diagonal score and multiplies attention
  - *From: Kijai*

- **Context parallel vs tensor parallel**: Context parallel splits input into parts and computes separately with attention trickery, while tensor parallel is for weight distribution
  - *From: intervitens*

- **FSDP weight sharing**: Each GPU sees full weights reconstructed from RAM with CPU offloading or by combining shards from multiple GPUs
  - *From: intervitens*

- **SLG (Skip Layer Guidance)**: Method that purposely makes unconditional guidance worse by skipping specific blocks, strengthening CFG effect and improving details
  - *From: Kijai*

- **Context window image_cond**: Uses last frame of previous window as conditioning for next window, with image_cond_start_step determining when to apply it
  - *From: Kijai*

- **TeaCache**: Optimization technique that patches the model to accept modifications that wouldn't work otherwise, required for SLG functionality
  - *From: Kijai*

- **fp8_fast**: Uses Ada/Hopper/Blackwell fp8 matrix multiplication by patching linear ops with custom functions
  - *From: Kijai*

- **Context windowing with I2V**: image_cond_window_count parameter attempts to do context windowing with image-to-video generation
  - *From: Kijai*

- **VAE frame encoding**: VAE encodes 1 frame plus 4x(1/4) frames at a time according to model documentation
  - *From: Flipping Sigmas*

- **SLG (Skip Layer Guidance)**: Makes generations more alive and changes CFG behavior, can use multiple blocks
  - *From: Kijai*

- **Context options**: Method for generating longer videos by processing in chunks with overlap
  - *From: Kijai*

- **Compile dropping**: When model compilation is lost due to node changes, causing slowdowns
  - *From: Kijai*

- **Context windowing in video generation**: Processing video frames in overlapping chunks rather than all at once, similar to sliding windows in LLMs but for temporal sequences
  - *From: fredbliss*

- **Blend zones**: Areas around section boundaries where prompts are interpolated together using various easing functions for smooth transitions
  - *From: fredbliss*

- **Embedding optimization order**: Reordering prompt embeddings based on semantic similarity using nearest neighbor search to create smoother transitions
  - *From: fredbliss*

- **Latent shifting for loops**: Technique where latent representations are shifted with controlled overlap to create seamless video loops
  - *From: Kijai*

- **Context windows**: Allows processing longer videos by dividing into overlapping segments, VRAM usage based on window size not total frames
  - *From: Kijai*

- **Differential diffusion**: Technique used with masking for video inpainting - controls diffusion strength per region
  - *From: Kijai*

- **discard_penultimate_sigma**: KSampler option that changes sigma schedule for specific samplers to reduce noise
  - *From: Ablejones*

- **Mobius looping**: Technique for creating seamless video loops, doesn't work well with I2V due to CLIP
  - *From: TK_999*

- **SLG**: Skip Layer Guidance - provides speed boost but can affect quality
  - *From: N0NSens*

- **TeaCache**: Cache mechanism that skips steps like '1,2, skip a few, 99,100' - reduces computation but can destroy output if not configured properly
  - *From: Cubey*

- **Context windowing**: Method to extend videos beyond 81 frame limit using frame shifts and overlaps
  - *From: Kijai*

- **Tilelang kernels**: Custom kernels for operations like rmsnorm that provide performance improvements
  - *From: intervitens*

- **Control LoRA**: LoRA trained to add control capabilities like depth, works by patching model during loading
  - *From: spacepxl*

- **Early step cutoff**: Disabling LoRA for later refinement steps to allow more creative freedom
  - *From: spacepxl*

- **Block dropping from control lora**: New feature that allows dropping specific blocks from control LoRA which may improve results
  - *From: Kijai*

- **VAE context windows**: Using VAE to pass different content than init image to other context windows, though results are limited
  - *From: Kijai*

- **FLUXFLOW training**: Training method that disrupts temporal order by shuffling frames to force model to learn disentangled motion dynamics
  - *From: mamad8*

- **Chunk-wise processing in Wan-VAE**: Videos processed in '1 + T/4' chunks with max 4 frames per chunk to prevent memory overflow
  - *From: Flipping Sigmas*

- **Start/End frame interpolation**: Method to create animations between two keyframes using dual image inputs with controllable embed strengths, similar to iPA concept
  - *From: The Shadow (NYC)*

- **ClipVision tiling**: Technique where image is tiled and tiles are averaged for better vision processing, originally developed by Matteo
  - *From: Kijai*

- **Diffusion Cache**: Similar to KV caching in LLMs, caches attention outputs across denoising steps
  - *From: fredbliss*

- **VAE Feature Cache**: Maintains frame-level feature caches between processing chunks for efficiency
  - *From: fredbliss*

- **Context Windowing**: Processing longer videos in overlapping windows with blending, similar to sliding window attention
  - *From: fredbliss*

- **Warmup phase**: First several frames used only for conditioning the model, not for output
  - *From: fredbliss*

- **Differential diffusion**: Method that uses masks but still processes background, requires compositing on original
  - *From: Kijai*

- **SLG (Skip Layer Guidance)**: Skip Layer Guidance technique for better generation control
  - *From: JmySff*

- **CLIP embed concatenation**: Combining start/end frame embeds: torch.Size([2, 257, 1280]) becomes torch.Size([1, 514, 1280])
  - *From: Kijai*

- **Differential Diffusion**: A technique for diffusing at different strengths based on black and white input mask
  - *From: David Snow*

- **Loop args vs context window uniform loop**: Two different methods for creating video loops, loop args works with 1.3B but not 14B, context window works with 14B but very slow
  - *From: Kijai*

- **CFG distillation**: Training technique using real CFG for few steps then distilled CFG for the rest, provides 50% speedup
  - *From: spacepxl*

- **SLG**: Runs an extra pass that's used as sort of extra CFG, slows down process and should be used with limited step range, requires TeaCache node
  - *From: Kijai*

- **Face LoRA training technique**: Training on 5-frame videos where last 4 frames are identical overcomes VAE limitations with 2-frame sequences
  - *From: Juampab12*

- **Block swap memory summary**: Shows how transformer blocks are distributed between CUDA and host memory - 0MB CUDA/high host indicates RAM issues
  - *From: arthuz*

- **Prompt travel**: Segmenting cross-attention to apply different prompts to different parts of video sequence using | separator
  - *From: Kijai*

- **SLG (Skip Layer Guidance)**: Skips unconditional pass on selected blocks, does 1 pass through 40 blocks + 1 pass through 39 blocks per step, increases details similar to higher CFG
  - *From: Kijai*

- **Differential diffusion**: Using mask to diffuse different parts of video at different strengths based on black and white mask
  - *From: David Snow*

- **Riflex**: Context parameter that can be set to values like 6 for longer generations up to 129 frames
  - *From: Kijai*

- **Differential diffusion**: Everything goes through the model but it tries to balance so only masked parts change, reduces quality of unmasked bits so compositing is recommended
  - *From: Kijai*

- **Self attention split**: Technique that makes prompt conditions separated by pipe syntax work stronger by splitting attention computation
  - *From: Kijai*

- **CFG-Zero-star**: Alternative CFG method that does extra calculations on results rather than additional model passes, provides subtle quality improvements
  - *From: Kijai*

- **CFG Zero Star**: Method that uses optimized scaling and optionally zeros out early steps completely
  - *From: Kijai*

- **Zero init**: Feature that literally multiplies early steps by zero, different from skipping steps entirely
  - *From: Kijai*

- **Alibaba prompt format**: Subject Description, Scene Description, Motion Description, Camera Language, Atmosphere, Styling
  - *From: Benjimon*

- **Fun models**: Different finetune supporting start/end frame and control signals, innately I2V/inpaint models for temporal inpainting
  - *From: Kijai*

- **48 input channels**: New channel count for 1.3B I2V model, different from standard 16+20 configuration
  - *From: Kijai*

- **SLG/Skip Layer Guidance**: Technique that makes significant quality difference, can be configured with different block start points
  - *From: Kijai*

- **CFG ZeroStar**: Works on all DiT flow models as a replacement to CFG
  - *From: yi*

- **TeaCache coefficients**: Different coefficient settings (480 or 720) used for different model variants
  - *From: Kijai*

- **i2v2i / image2video2image**: Animating between 2 images, generally called i2v with end frame/keyframes
  - *From: aikitoria*

- **Start/end frame latents**: For frames after start image when only specifying start image, latents should be zeros, not noise
  - *From: Kijai*

- **Fun_model toggle**: Switch in encode node that needs to be enabled when using Fun models with start/end frame functionality
  - *From: Kijai*

- **Fun Control model**: Wan 2.1 variant that accepts various control inputs like Canny, Depth, Pose, MLSD for guided video generation
  - *From: multiple users*

- **Fun InP model**: Wan 2.1 variant for temporal inpainting, can do start-to-end frame morphing
  - *From: Kijai*

- **4n+1 frame formula**: Mathematical requirement for frame counts in Wan models - must be 4 times any number plus 1
  - *From: DawnII*

- **Trajectory control**: Control method that guides object movement along specified paths in video generation
  - *From: Kijai*

- **Combine embeds modes**: average (averages both images), sum (adds together), concat (extends clip embed), batch (splits attention between first/second half of video)
  - *From: Kijai*

- **Split attention**: Experimental feature to separate video attention at specific steps, allowing different prompts/embeds for different parts of video
  - *From: Kijai*

- **Fun Control vs ControlNet LoRAs**: Fun Control has control built into model, doesn't use separate LoRAs like traditional ControlNet approach
  - *From: DawnII*

- **Fun InP**: I2V model that can do T2V, I2V with start and/or end frame prediction
  - *From: Kijai*

- **Fun InP masking**: Does masking differently than standard I2V, controlled by switch in encoder node
  - *From: Kijai*

- **I2V latent encoding**: Image + 3 empty frames are encoded in one go, not individually
  - *From: Kijai*

- **Fun models**: Newest models from Alibaba with dedicated control embed for depth/canny/normal/pose/trajectory control
  - *From: Kytra*

- **TeaCache coefficients toggle**: When using coefficients toggle for base wan, if not using toggle multiply recommended values by 0.1
  - *From: DawnII*

- **Model dimension scaling**: Can reduce model dimension by splitting weights while keeping head dimensions in mind to avoid random init weights
  - *From: spacepxl*

- **Latent attention masking**: What the mask is used for in control nodes to selectively apply control to parts of the generation
  - *From: Kytra*

- **Control latent strength and end percent**: Two parameters that can be adjusted to reduce control strength when pose is too far from reference
  - *From: Kijai*

- **Temporal masking**: Binary mask per 4 frames due to latent space, where white frames are kept and black ones are generated
  - *From: Kijai*

- **Binary mask**: 0 or 1 values only (no in-between), as opposed to gradient masks that can have partial opacity
  - *From: ˗ˏˋ⚡ˎˊ-*

- **DiT blocks**: Diffusion Transformer blocks - early blocks affect composition and motion most, later blocks affect details
  - *From: Kijai*

- **Fun models**: Control and InP variants - Fun Control for ControlNet inputs, Fun InP for inpainting/extension/I2V
  - *From: Doctor Shotgun*

- **Wan frame structure**: Steps of 4 because latent space has 4 images in one latent, always +1 frame (think of it as starting from 1)
  - *From: Kijai*

- **Fun Control reference image**: Partially like IPAdapter with clip embed similarity, but also used as latent input which is far stronger
  - *From: Kijai*

- **TeaCache patching**: TeaCache literally patches over most of the model itself, many things can go wrong with patch nodes
  - *From: Kijai*


## Resources & Links

- **David Snow's second pass workflow** (workflow)
  - https://discord.com/channels/1076117621407223829/1342763350815277067/1345141179616071782
  - *From: David Snow*

- **Wan2_1_VAE_bf16.safetensors** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/blob/main/Wan2_1_VAE_bf16.safetensors
  - *From: seitanism*

- **ComfyUI Wan examples** (workflow)
  - https://comfyanonymous.github.io/ComfyUI_examples/wan/
  - *From: VRGameDevGirl84(RTX 5090)*

- **ComfyUI repackaged models** (model)
  - https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/tree/main/split_files/diffusion_models
  - *From: VRGameDevGirl84(RTX 5090)*

- **WAN2.1 T2V 1.3B FP8 version** (model)
  - https://civitai.com/models/1307708/wan21t2v13bfp8
  - *From: yo9o*

- **ComfyUI-VEnhancer** (tool)
  - https://github.com/kijai/ComfyUI-VEnhancer
  - *From: VRGameDevGirl84*

- **ComfyUI Frame Interpolation** (tool)
  - https://github.com/Fannovel16/ComfyUI-Frame-Interpolation
  - *From: Draken*

- **SpargeAttn speed optimization** (tool)
  - https://github.com/thu-ml/SpargeAttn
  - *From: NebSH*

- **Triton Windows installation** (tool)
  - https://github.com/woct0rdho/triton-windows?tab=readme-ov-file
  - *From: Dream Making*

- **WanVideoBlockSwap node troubleshooting** (workflow)
  - *From: JohnDopamine*

- **David Snow's two-pass workflow** (workflow)
  - https://discord.com/channels/1076117621407223829/1342763350815277067/1345141179616071782
  - *From: David Snow*

- **ComfyUI-Unload-Model nodes** (tool)
  - https://github.com/SeanScripts/ComfyUI-Unload-Model
  - *From: chancelor*

- **ROPE face swapping tool** (tool)
  - https://github.com/Hillobar/Rope
  - *From: VRGameDevGirl84(RTX 5090)*

- **ComfyUI RopeWrapper** (node)
  - https://github.com/fssorc/ComfyUI_RopeWrapper
  - *From: David Snow*

- **FaceFusion (ROPE successor)** (tool)
  - https://github.com/facefusion/facefusion
  - *From: Janosch Simon*

- **ComfyUI-ReActor face swap nodes** (node)
  - https://github.com/Gourieff/ComfyUI-ReActor
  - *From: ˗ˏˋ⚡ˎˊ-*

- **SwarmUI with Wan integration** (workflow)
  - https://www.reddit.com/r/StableDiffusion/s/T5LEPjxzXM
  - *From: ramonguthrie (4080 16GB) 🇬🇧*

- **Genmo AI prompts** (prompts)
  - https://www.genmo.ai/play
  - *From: David Snow*

- **Movie Gen Video Bench prompts** (dataset)
  - https://huggingface.co/datasets/meta-ai-for-media-research/movie_gen_video_bench_no_generations
  - *From: Benjaminimal*

- **DiffSynth Studio** (tool)
  - https://github.com/modelscope/DiffSynth-Studio/
  - *From: Benjimon*

- **H1111 for Hunyuan/Skyreels** (tool)
  - https://github.com/maybleMyers/H1111
  - *From: Benjimon*

- **Wan 2.1 I2V 14B GGUF** (model)
  - https://huggingface.co/city96/Wan2.1-I2V-14B-720P-gguf/tree/main
  - *From: seitanism*

- **TemporalBench dataset** (dataset)
  - https://huggingface.co/datasets/microsoft/TemporalBench
  - *From: TK_999*

- **DatasetHelper node** (node)
  - https://github.com/fblissjr/ComfyUI-DatasetHelper
  - *From: fredbliss*

- **Original TeaCache paper/implementation** (repo)
  - https://github.com/ali-vilab/TeaCache
  - *From: Kijai*

- **Wan Cinematic Video Prompt Generator GPT** (tool)
  - https://chatgpt.com/g/g-67c3a6d6d19c81919b3247d2bfd01d0b-wan-cinematic-video-prompt-generator
  - *From: VRGameDevGirl84*

- **Wan as image generator discussion** (discussion)
  - https://www.reddit.com/r/StableDiffusion/comments/1j0s2j7/wan21_14b_video_models_also_have_impressive_image/
  - *From: Juampab12*

- **Wan prompt extension utility** (tool)
  - https://github.com/Wan-Video/Wan2.1/blob/main/wan/utils/prompt_extend.py
  - *From: Jetz*

- **TeaCache coefficients calculation** (repo)
  - https://github.com/ali-vilab/TeaCache/issues/20#issuecomment-2574564292
  - *From: Screeb*

- **bf16 text encoder model** (model)
  - wan_t5_umt5-xxl-enc-bf16.pth
  - *From: Googol*

- **City96 GGUF models** (model)
  - https://huggingface.co/city96
  - *From: TK_999*

- **High-res fix technique for Wan** (workflow)
  - https://www.reddit.com/r/StableDiffusion/comments/1j0znur/run_wan_faster_highres_fix_in_2025/
  - *From: N0NSens*

- **Kijai Wan Video models** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/tree/main
  - *From: Kijai*

- **e5m2 quantized I2V model** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/blob/main/Wan2_1-I2V-14B-480P_fp8_e5m2.safetensors
  - *From: Kijai*

- **T2V workflow example** (workflow)
  - https://discord.com/channels/1076117621407223829/1342763350815277067/1345141179616071782
  - *From: David Snow*

- **Area composition examples** (workflow)
  - https://comfyanonymous.github.io/ComfyUI_examples/area_composition/
  - *From: comfy*

- **SDE sampler implementation** (repo)
  - https://github.com/juliusberner/sde_sampler
  - *From: ˗ˏˋ⚡ˎˊ-*

- **ComfyUI security configuration guide** (guide)
  - https://comfyui-guides.runcomfy.com/ultimate-comfyui-how-tos-a-runcomfy-guide/how-to-fix-this-action-is-not-allowed-with-this-security-level-configuration
  - *From: David Snow*

- **SD-Latent-Interposer** (repo)
  - https://github.com/city96/SD-Latent-Interposer
  - *From: Kijai*

- **WAN Cinematic Video Prompt Generator** (tool)
  - https://chatgpt.com/g/g-67c3a6d6d19c81919b3247d2bfd01d0b-wan-cinematic-video-prompt-generator
  - *From: VRGameDevGirl84(RTX 5090)*

- **FPS sampling fork** (repo)
  - https://github.com/fblissjr/ComfyUI-WanVideoWrapper
  - *From: fredbliss*

- **TeaCache native implementation** (repo)
  - https://github.com/kijai/ComfyUI-TeaCache
  - *From: Kijai*

- **1.3B FP32 model** (model)
  - https://huggingface.co/Wan-AI/Wan2.1-T2V-1.3B/blob/main/diffusion_pytorch_model.safetensors
  - *From: David Snow*

- **RIFLEx** (repo)
  - https://github.com/thu-ml/RIFLEx
  - *From: BecauseReasons*

- **ComfyUI Frame Interpolation** (repo)
  - https://github.com/Fannovel16/ComfyUI-Frame-Interpolation
  - *From: Flipping Sigmas*

- **Rife TensorRT** (repo)
  - https://github.com/yuvraj108c/ComfyUI-Rife-Tensorrt
  - *From: Monster*

- **WanVideoWrapper FPS sampling workflow** (workflow)
  - https://github.com/fblissjr/ComfyUI-WanVideoWrapper/blob/main/example_workflows/wanvideo_fps_sampling_latent_interpolation.json
  - *From: fredbliss*

- **Kijai's teacache fork** (repo)
  - https://github.com/kijai/ComfyUI-TeaCache
  - *From: Miku*

- **Adaptive Guidance extension** (repo)
  - https://github.com/asagi4/ComfyUI-Adaptive-Guidance
  - *From: Miku*

- **H1111 with WanX support** (repo)
  - https://github.com/maybleMyers/H1111
  - *From: Benjimon*

- **Dynamic Thresholding** (repo)
  - https://github.com/mcmonkeyprojects/sd-dynamic-thresholding
  - *From: TK_999*

- **Kijai's TeaCache repo** (repo)
  - https://github.com/kijai/ComfyUI-TeaCache
  - *From: Miku*

- **Wan 2.1 VAE** (model)
  - https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/blob/main/split_files/vae/wan_2.1_vae.safetensors
  - *From: Miku*

- **T5 model for Wan** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/tree/main
  - *From: Juampab12*

- **Multi-GPU implementation** (repo)
  - https://github.com/intervitens/Wan-MultiGPU
  - *From: intervitens*

- **Pile T5 model** (model)
  - https://huggingface.co/EleutherAI/pile-t5-large/
  - *From: Juampab12*

- **ComfyUI area composition examples** (workflow)
  - https://comfyanonymous.github.io/ComfyUI_examples/area_composition/
  - *From: ˗ˏˋ⚡ˎˊ-*

- **MagicWan repo** (repo)
  - https://github.com/kijai/ComfyUI-MagicWan
  - *From: Kijai*

- **Phantom video project** (repo)
  - https://github.com/Phantom-video/Phantom
  - *From: yo9o*

- **Generation acceleration resources** (repo)
  - https://github.com/xuyang-liu16/Awesome-Generation-Acceleration/blob/main/TRAIN-FREE.md#training-free-diffusion-transformer-acceleration
  - *From: yi*

- **TeaCache paper** (paper)
  - https://arxiv.org/pdf/2411.19108
  - *From: fredbliss*

- **Adaptive Guidance repo** (repo)
  - https://github.com/asagi4/ComfyUI-Adaptive-Guidance
  - *From: zezo*

- **Updated Wan FlowEdit workflow** (workflow)
  - https://discord.com/channels/1076117621407223829/1346134166311403692
  - *From: Zuko*

- **RES4LYF sampler pack** (tool)
  - https://github.com/ClownsharkBatwing/RES4LYF
  - *From: Ablejones*

- **VideoGen-RewardBench dataset** (dataset)
  - https://huggingface.co/datasets/KwaiVGI/VideoGen-RewardBench
  - *From: TK_999*

- **llm CLI tool** (tool)
  - https://github.com/simonw/llm
  - *From: fredbliss*

- **Wan inpainting implementation** (model)
  - https://replicate.com/andreasjansson/wan-1.3b-inpaint
  - *From: andreas*

- **KJNodes package** (repo)
  - https://github.com/kijai/ComfyUI-KJNodes
  - *From: Kijai*

- **Simple latent guide workflow** (workflow)
  - *From: Ablejones*

- **RES4LYF nodes** (repo)
  - https://github.com/ClownsharkBatwing/RES4LYF
  - *From: Ablejones*

- **Comfy scaled text encoder** (model)
  - https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/tree/main/split_files/text_encoders
  - *From: The Shadow (NYC)*

- **Adaptive Guidance** (repo)
  - https://github.com/asagi4/ComfyUI-Adaptive-Guidance
  - *From: TK_999*

- **Triton installation guide** (tool)
  - https://www.youtube.com/watch?v=DigvHsn_Qrw
  - *From: David Snow*

- **Automatic Triton installation** (tool)
  - https://www.reddit.com/r/StableDiffusion/comments/1j0enkx/automatic_installation_of_triton_and/
  - *From: Miku*

- **TensorRT Upscaler for ComfyUI** (tool)
  - https://github.com/yuvraj108c/ComfyUI-Upscaler-Tensorrt
  - *From: Lumifel*

- **WAN Video I2V Upscaling and Frame Interpolation workflow** (workflow)
  - https://civitai.com/models/1297230/wan-video-i2v-upscaling-and-frame-interpolation
  - *From: The Shadow (NYC)*

- **Florence2 ComfyUI nodes** (tool)
  - https://github.com/kijai/ComfyUI-Florence2
  - *From: TK_999*

- **Ollama ComfyUI integration** (tool)
  - https://github.com/stavsap/comfyui-ollama
  - *From: B1naryV1k1ng*

- **WAN prompt enhancement system prompt** (resource)
  - https://github.com/Wan-Video/Wan2.1/blob/main/wan/utils/prompt_extend.py
  - *From: intervitens*

- **FlowEdit workflow** (workflow)
  - https://www.reddit.com/r/comfyui/comments/1j2u7og/wan_flowedit_i2v_and_t2v_updated_workflow/
  - *From: Ashtar*

- **AnimateDiff context documentation** (documentation)
  - https://github.com/Kosinkadink/ComfyUI-AnimateDiff-Evolved/tree/main/documentation/nodes#context-optionsstandard-uniform
  - *From: Kijai*

- **OpenModelDB upscalers** (models)
  - https://openmodeldb.info/
  - *From: Kijai*

- **TensorRT upscaler** (tool)
  - https://github.com/yuvraj108c/ComfyUI-Upscaler-Tensorrt
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Kijai Wan models on Civitai** (model)
  - https://civitai.com/models/1295569?modelVersionId=1463630
  - *From: Ashtar*

- **Kijai HuggingFace Wan models** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/tree/main
  - *From: Kijai*

- **Video repair tool** (tool)
  - https://repair.cleverfiles.com/es
  - *From: Juampab12*

- **Untrunc video repair** (tool)
  - https://github.com/anthwlock/untrunc
  - *From: Dream Making*

- **Hunyuan keyframe control LoRA** (model)
  - https://huggingface.co/dashtoon/hunyuan-video-keyframe-control-lora/discussions/1#67c04fe5dc9b46d98ec89e94
  - *From: Godhand*

- **Prompt travel implementation** (repo)
  - https://github.com/fblissjr/ComfyUI-WanVideoWrapper
  - *From: ˗ˏˋ⚡ˎˊ-*

- **WanVideo FPS Interpolation fork** (repo)
  - https://github.com/fblissjr/ComfyUI-WanVideoWrapper-fps-interpolation
  - *From: fredbliss*

- **Sage Attention 2 installation guide** (guide)
  - https://github.com/deepbeepmeep/Wan2GP
  - *From: Teslanaut*

- **Wrapper models** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/tree/main
  - *From: JmySff*

- **Native models** (model)
  - https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/tree/main/split_files/diffusion_models
  - *From: JmySff*

- **ComfyUI Wan tutorial** (tutorial)
  - https://comfyui-wiki.com/en/tutorial/advanced/wan21-video-model
  - *From: Bleedy (Madham)*

- **Wan2GP repository with optimizations** (repo)
  - https://github.com/deepbeepmeep/Wan2GP
  - *From: Teslanaut*

- **ComfyUI examples with Chinese prompts** (workflow)
  - https://github.com/comfyanonymous/ComfyUI_examples/blame/master/wan/image_to_video_wan_example.json#L179
  - *From: for1096*

- **Upstream default Chinese prompt** (repo)
  - https://github.com/Wan-Video/Wan2.1/blob/d18cc1b3977c53fe4cff825ee50dbec171d8dfae/wan/configs/shared_config.py#L19
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Updated TeaCache patch** (node)
  - *From: Kijai*

- **Wan2.1-I2V-14B GGUF models** (model)
  - https://huggingface.co/city96/Wan2.1-I2V-14B-480P-gguf
  - *From: Screeb*

- **Wan2.1-I2V-14B-720P GGUF** (model)
  - https://huggingface.co/city96/Wan2.1-I2V-14B-720P-gguf
  - *From: Screeb*

- **ComfyUI Wan examples** (workflow)
  - https://comfyanonymous.github.io/ComfyUI_examples/wan/
  - *From: Screeb*

- **RES4LYF samplers** (repo)
  - https://github.com/ClownsharkBatwing/RES4LYF
  - *From: David Snow*

- **SkyReels-A1 audio pipeline** (repo)
  - https://github.com/SkyworkAI/SkyReels-A1
  - *From: Draken*

- **TeaCache repository** (repo)
  - https://github.com/ali-vilab/TeaCache/commit/3cddb3689697ba949b689d81b3d508e68b68307d
  - *From: yi*

- **Open-Sora 1.3** (model)
  - Not provided
  - *From: deleted_user_2ca1923442ba*

- **Apollo paper on FPS sampling** (research)
  - Not provided
  - *From: fredbliss*

- **Goose collaborative coding tool** (tool)
  - https://block.github.io/goose/docs/quickstart/
  - *From: fredbliss*

- **fp16 Wan models** (model)
  - https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/tree/main/split_files/diffusion_models
  - *From: comfy*

- **Wan2GP** (repo)
  - https://github.com/deepbeepmeep/Wan2GP
  - *From: N0NSens*

- **Wan ComfyUI models** (model)
  - https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/tree/main/split_files/clip_vision
  - *From: N0NSens*

- **Wan Multi-GPU script** (repo)
  - https://github.com/intervitens/Wan-MultiGPU
  - *From: intervitens*

- **Hunyuan I2V models** (model)
  - https://huggingface.co/tencent/HunyuanVideo-I2V
  - *From: GalaxyTimeMachine (RTX4090)*

- **LTX Video interpolation node** (node)
  - *From: Juampab12*

- **Example I2V workflow** (workflow)
  - https://github.com/kijai/ComfyUI-WanVideoWrapper
  - *From: jellybean5361*

- **Topaz CLI documentation** (documentation)
  - https://docs.topazlabs.com/video-ai/advanced-functions-in-topaz-video-ai/command-line-interface
  - *From: aikitoria*

- **Comfy-Topaz node** (node)
  - https://github.com/choey/Comfy-Topaz
  - *From: Colin*

- **Inference-time scaling for LTX/WAN** (repo)
  - https://github.com/sayakpaul/tt-scale-flux/pull/18
  - *From: Benjaminimal*

- **CFG distillation LoRA and workflow** (model)
  - https://huggingface.co/spacepxl/wan-cfgdistill-loras/tree/main
  - *From: spacepxl*

- **Alibaba Wan prompting guide** (guide)
  - https://help.aliyun.com/zh/model-studio/use-cases/text-to-video-prompt
  - *From: for1096*

- **Taproot for looping context** (repo)
  - https://github.com/painebenjamin/taproot
  - *From: Benjaminimal*

- **ComfyUI LoRA masking blog** (tutorial)
  - https://blog.comfy.org/p/masking-and-scheduling-lora-and-model-weights
  - *From: spacepxl*

- **Nunchaku SVDQuant** (tool)
  - https://github.com/mit-han-lab/nunchaku
  - *From: Ada*

- **ComfyUI Wan examples updated** (examples)
  - https://comfyanonymous.github.io/ComfyUI_examples/wan/
  - *From: comfy*

- **HuggingFace fp8_scaled models** (model)
  - https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/tree/main/split_files/diffusion_models
  - *From: comfy*

- **Mimicpc cloud service** (service)
  - https://mimicpc.com?fpr=adam47
  - *From: AJO*

- **Taproot spatial/temporal multidiffusion implementation** (repo)
  - https://github.com/painebenjamin/taproot/blob/main/src/taproot/tasks/generation/video/wan/model/pipeline.py
  - *From: Benjaminimal*

- **Nvidia Cosmos prompt upsampler** (tool)
  - https://huggingface.co/spaces/benjamin-paine/nvidia-cosmos-prompt-upsampler
  - *From: Benjaminimal*

- **SAM segmentation tutorial** (tutorial)
  - https://www.youtube.com/watch?v=Zx9AQMA9zbI
  - *From: David Snow*

- **SVDquant demo** (demo)
  - https://svdquant.mit.edu/
  - *From: Ada*

- **Ostris Wan speedup hint** (news)
  - https://x.com/ostrisai/status/1898095715920101871
  - *From: JohnDopraine*

- **ComfyUI portable with pytorch nightly** (tool)
  - https://github.com/comfyanonymous/ComfyUI/releases/download/latest/ComfyUI_windows_portable_nvidia_or_cpu_nightly_pytorch.7z
  - *From: comfy*

- **VideoUFO dataset** (dataset)
  - https://huggingface.co/datasets/WenhaoWang/VideoUFO
  - *From: spacepxl*

- **MiraData dataset** (dataset)
  - https://github.com/mira-space/MiraData
  - *From: mamad8*

- **Wan V2V workflows** (workflow)
  - https://github.com/kijai/ComfyUI-WanVideoWrapper/tree/main/example_workflows
  - *From: Organoids*

- **GPT4V Image Captioner** (tool)
  - https://github.com/jiayev/GPT4V-Image-Captioner
  - *From: fredbliss*

- **FPS interpolation fork** (repo)
  - https://github.com/fblissjr/ComfyUI-WanVideoWrapper-fps-interpolation
  - *From: fredbliss*

- **P2P kernel modules for 4090s** (repo)
  - https://github.com/aikitoria/open-gpu-kernel-modules/tree/570.124.04-p2p
  - *From: aikitoria*

- **Multi-GPU Wan implementation** (repo)
  - https://github.com/intervitens/Wan-MultiGPU/tree/sage_fp16
  - *From: aikitoria*

- **Google Whisk** (tool)
  - https://labs.google/fx/tools/whisk
  - *From: fredbliss*

- **MSI 4090 fan replacement** (tool)
  - https://www.ebay.com/itm/176760659886
  - *From: Benjimon*

- **Wan-MultiGPU sage_fp16 branch** (repo)
  - https://github.com/intervitens/Wan-MultiGPU/tree/sage_fp16
  - *From: aikitoria*

- **ComfyUI-LatentSyncWrapper** (node)
  - https://github.com/ShmuelRonen/ComfyUI-LatentSyncWrapper
  - *From: JmySff*

- **ComfyUI-Adaptive-Guidance** (node)
  - https://github.com/asagi4/ComfyUI-Adaptive-Guidance
  - *From: Kijai*

- **Wan 2.1 1.3B CFG Distill LoRA** (lora)
  - https://civitai.com/models/1337418/wan21-13b-cfg-distill-lora?modelVersionId=1510288
  - *From: Juampab12*

- **Wan 2.1 1.3B CFG Distill LoRA** (lora)
  - https://civitai.com/models/1337418/wan21-13b-cfg-distill-lora?modelVersionId=1510288
  - *From: David Snow*

- **Cakify LoRA for Wan 14B** (lora)
  - https://civitai.com/models/1337473/cakify-cake-everything-wan-14b-i2v
  - *From: Miku*

- **ComfyUI-Rife-Tensorrt** (repo)
  - https://github.com/yuvraj108c/ComfyUI-Rife-Tensorrt
  - *From: burgstall*

- **ComfyUI-Depth-Anything-Tensorrt** (repo)
  - https://github.com/yuvraj108c/ComfyUI-Depth-Anything-Tensorrt
  - *From: burgstall*

- **ComfyUI-Facerestore-Tensorrt** (repo)
  - https://github.com/yuvraj108c/ComfyUI-Facerestore-Tensorrt
  - *From: burgstall*

- **ComfyUI_Fill-Nodes** (repo)
  - https://github.com/filliptm/ComfyUI_Fill-Nodes
  - *From: JohnDopamine*

- **Diffusion-pipe for distributed training** (repo)
  - https://github.com/tdrussell/diffusion-pipe
  - *From: Benjimon*

- **Squish Effect LoRA for Wan 2.1** (lora)
  - https://civitai.com/models/1340141/squish-effect-wan21-i2v-lora?modelVersionId=1513385
  - *From: Cubey*

- **Flux Control Training Script** (repo)
  - https://github.com/huggingface/diffusers/tree/main/examples/flux-control
  - *From: spacepxl*

- **Wan diving cat comparison video** (demo)
  - https://www.reddit.com/r/StableDiffusion/comments/1izjlvu/wan_21_14b_is_actually_crazy/
  - *From: seitanism*

- **Triton and SageAttention one-click installer** (tool)
  - https://civitai.com/articles/12248/triton-and-sageattention-one-click-installer-on-windows
  - *From: David Snow*

- **Wan2_1-I2V-14B-480P_fp8_e5m2.safetensors** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/blob/main/Wan2_1-I2V-14B-480P_fp8_e5m2.safetensors
  - *From: Kijai*

- **Squish Effect Wan2.1 I2V LoRA** (lora)
  - https://civitai.com/models/1340141/squish-effect-wan21-i2v-lora
  - *From: Kijai*

- **FLUX Depth and Canny LoRAs** (lora)
  - https://huggingface.co/black-forest-labs/FLUX.1-Depth-dev-lora
  - *From: GalaxyTimeMachine (RTX4090)*

- **ComfyUI FLUX examples** (workflow)
  - https://comfyanonymous.github.io/ComfyUI_examples/flux/#canny-and-depth
  - *From: Draken*

- **Squish Effect LoRA** (lora)
  - https://civitai.com/models/1340141/squish-effect-wan21-i2v-lora?modelVersionId=1513385
  - *From: Juampab12*

- **Cakify LoRA** (lora)
  - https://civitai.com/models/1337473/cakify-cake-everything-wan-14b-i2v
  - *From: Juampab12*

- **NovelAI T5** (repo)
  - https://github.com/NovelAI/t5
  - *From: Draken*

- **Triton Windows** (package)
  - https://pypi.org/project/triton-windows/
  - *From: Kijai*

- **Wan 2.1 1.3B tile control LoRA v0.1** (model)
  - https://huggingface.co/spacepxl/Wan2.1-control-loras/blob/main/wan2.1-1.3b-control-lora-tile-v0.1_comfy.safetensors
  - *From: spacepxl*

- **Video effects collection** (dataset)
  - https://huggingface.co/collections/finetrainers/video-effects-6798834eece6b7910c43870d
  - *From: Cseti*

- **Video effects training datasets** (dataset)
  - https://huggingface.co/finetrainers
  - *From: Cseti*

- **ComfyUI commit for control LoRA support** (repo)
  - https://github.com/comfyanonymous/ComfyUI/commit/ca8efab79fa19bc9745b4f7346d38a49ba1b1b7c
  - *From: comfy*

- **BlenderNeko TiledKSampler** (repo)
  - https://github.com/BlenderNeko/ComfyUI_TiledKSampler
  - *From: spacepxl*

- **SpotDiffusion** (research)
  - https://spotdiffusion.github.io
  - *From: Cubey*

- **Color-Canny-Controlnet-model** (model)
  - https://huggingface.co/ghoskno/Color-Canny-Controlnet-model
  - *From: deleted_user_2ca1923442ba*

- **History Guidance paper** (research)
  - https://boyuan.space/history-guidance/
  - *From: spacepxl*

- **Diffusion-pipe trainer** (tool)
  - https://github.com/tdrussell/diffusion-pipe/tree/main
  - *From: HeadOfOliver*

- **Musubi-tuner** (tool)
  - https://github.com/kohya-ss/musubi-tuner
  - *From: HeadOfOliver*

- **AI-toolkit by Ostris** (tool)
  - https://github.com/ostris/ai-toolkit
  - *From: HeadOfOliver*

- **VACE Page** (documentation)
  - https://ali-vilab.github.io/VACE-Page/
  - *From: DREX*

- **Deflate Effect LoRA** (model)
  - https://civitai.com/models/1344298/deflate-effect-wan21-i2v-lora?modelVersionId=1518196
  - *From: Juampab12*

- **Crush Effect LoRA** (model)
  - https://civitai.com/models/1344254/crush-effect-wan21-i2v-lora?modelVersionId=1518152
  - *From: Juampab12*

- **Color-matcher library** (tool)
  - https://github.com/hahnec/color-matcher
  - *From: Kijai*

- **3090 undervolting guide** (tutorial)
  - https://youtu.be/SIlXT32fOMk
  - *From: B1naryV1k1ng*

- **spacepxl CFG distill LoRA** (lora)
  - *From: spacepxl*

- **VPData dataset** (dataset)
  - https://huggingface.co/datasets/TencentARC/VPData
  - *From: Cseti*

- **VPBench dataset** (dataset)
  - https://huggingface.co/datasets/TencentARC/VPBench
  - *From: Cseti*

- **VACE project page** (project)
  - https://ali-vilab.github.io/VACE-Page/
  - *From: The Shadow (NYC)*

- **ComfyUI-WaveSpeed** (repo)
  - https://github.com/chengzeyi/Comfy-WaveSpeed
  - *From: aikitoria*

- **GIMM-VFI frame interpolation** (tool)
  - https://github.com/kijai/ComfyUI-GIMM-VFI
  - *From: Kijai*

- **Frame Interpolation ComfyUI nodes** (tool)
  - https://github.com/Fannovel16/ComfyUI-Frame-Interpolation
  - *From: spacepxl*

- **Flying Effect WAN LoRA** (model)
  - https://civitai.com/models/1348626/flying-effect-wan21-i2v-lora?modelVersionId=1523247
  - *From: Juampab12*

- **CFG Distill LoRA for 1.3B** (model)
  - https://civitai.com/models/1337418/wan21-13b-cfg-distill-lora?modelVersionId=1510288
  - *From: Juampab12*

- **VACE video control system** (repo)
  - https://github.com/ali-vilab/VACE
  - *From: VRGameDevGirl84(RTX 5090)*

- **ThunderCompute cloud service** (service)
  - https://www.thundercompute.com/
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Steamboat Willie LoRA** (lora)
  - https://huggingface.co/benjamin-paine/wan-lora/resolve/main/steamboat-willie.bf16.safetensors
  - *From: Benjaminimal*

- **Resolution Calculator Tool** (tool)
  - *From: Fred*

- **Wan ControlNet upscaler video** (tutorial)
  - https://youtu.be/1qIsPI7Uf6I?si=a_kQC3l4UhJFS0Ww
  - *From: ramonguthrie*

- **WanVideoWrapper GitHub** (repo)
  - https://github.com/kijai/ComfyUI-WanVideoWrapper
  - *From: Kijai*

- **Sparse-VideoGen** (repo)
  - https://github.com/svg-project/Sparse-VideoGen
  - *From: Draken*

- **VACE** (repo)
  - https://github.com/ali-vilab/VACE
  - *From: Tonon*

- **Updated tile LoRA with workflow** (model)
  - https://huggingface.co/spacepxl/Wan2.1-control-loras/tree/main/1.3b/tile
  - *From: spacepxl*

- **Wan2_1-I2V-14B-720P_fp8_e5m2.safetensors** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/blob/main/Wan2_1-I2V-14B-720P_fp8_e5m2.safetensors
  - *From: Kijai*

- **Skip layer guidance Reddit post** (guide)
  - https://www.reddit.com/r/StableDiffusion/comments/1jac3wm/dramatically_enhance_the_quality_of_wan_21_using/
  - *From: IllumiReptilien*

- **Chroma model** (model)
  - https://huggingface.co/lodestones/Chroma
  - *From: fredbliss*

- **Luma IMM research** (research)
  - https://lumalabs.ai/news/inductive-moment-matching
  - *From: fredbliss*

- **IMM code** (repo)
  - https://github.com/lumalabs/imm.git
  - *From: fredbliss*

- **Reddit post on Skip Layer Guidance** (technique)
  - https://www.reddit.com/r/ChatGPT/comments/1j99tfc/i_just_opensourced_8_more_viral_effects_request/
  - *From: Juampab12*

- **ComfyUI commit for control workflow fix** (repo)
  - https://github.com/comfyanonymous/ComfyUI/commit/ca8efab79fa19bc9745b4f7346d38a49ba1b1b7c
  - *From: spacepxl*

- **Wan2GP pull request** (repo)
  - https://github.com/deepbeepmeep/Wan2GP/pull/61#issuecomment-2721708607
  - *From: Kijai*

- **Diffusion-pipe training framework** (training tool)
  - https://github.com/tdrussell/diffusion-pipe
  - *From: Cseti*

- **Sesame CSM-1B model** (model)
  - https://huggingface.co/sesame/csm-1b/tree/main
  - *From: Juampab12*

- **CSM GitHub repository** (repo)
  - https://github.com/SesameAILabs/csm
  - *From: Juampab12*

- **FlashVideo project** (repo)
  - https://github.com/FoundationVision/FlashVideo
  - *From: deleted_user_2ca1923442ba*

- **Kijai WAN models** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/tree/main
  - *From: kendrick*

- **T5 SAE model by Linus Lee** (model)
  - https://huggingface.co/thesephist/contra-bottleneck-t5-small-wikipedia
  - *From: fredbliss*

- **ConceptAttention research** (repo)
  - https://github.com/helblazer811/ConceptAttention
  - *From: fredbliss*

- **ConceptAttention demo** (tool)
  - https://alechelbling.com/ConceptAttention/
  - *From: fredbliss*

- **Scientific AI blog post** (resource)
  - https://thomwolf.io/blog/scientific-ai.html#follow-up
  - *From: fredbliss*

- **Gitingest code analysis tool** (tool)
  - https://gitingest.com/
  - *From: fredbliss*

- **Kroki diagram service** (tool)
  - https://hub.docker.com/r/yuzutech/kroki/
  - *From: fredbliss*

- **4GB VRAM workflow** (workflow)
  - https://civitai.com/images/61717455
  - *From: kendrick*

- **4x upscaling models** (model)
  - https://openmodeldb.info/models/4x-FaceUpDAT
  - *From: yo9o*

- **Aging timelapse I2V LoRA** (lora)
  - https://civitai.com/models/1357480/wanvideo-i2v-480p-aging-timelapse
  - *From: Juampab12*

- **Collection of Wan 2.1 I2V LoRAs** (lora collection)
  - https://huggingface.co/collections/Remade-AI/wan21-14b-480p-i2v-loras-67d0e26f08092436b585919b
  - *From: Benjimon*

- **The Point LoRA** (lora)
  - https://civitai.com/models/1359644?modelVersionId=1535923
  - *From: Mint*

- **1x-DeJPG upscaler** (upscaler)
  - https://openmodeldb.info/models/1x-DeJPG-realplksr-otf
  - *From: Cseti*

- **RIFLEx for extended frame generation** (repo)
  - https://github.com/thu-ml/RIFLEx
  - *From: Kijai*

- **TAEW tiny VAE for Wan** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/blob/main/taew2_1.safetensors
  - *From: Kijai*

- **Enhance-A-Video repository** (repo)
  - https://github.com/NUS-HPC-AI-Lab/Enhance-A-Video
  - *From: Kijai*

- **TAEHV repository** (repo)
  - https://github.com/madebyollin/taehv
  - *From: Kijai*

- **FloweEdit workflow by Zack Abrams** (workflow)
  - https://discordapp.com/channels/1076117621407223829/1346134166311403692/1346134166311403692
  - *From: yukass*

- **Sharpest frame extraction script** (tool)
  - https://github.com/NSFW-API/TripleX/blob/master/utils/extract_sharpest_frame.py
  - *From: Benjimon*

- **RIFLEx (RoPE hack for video extension)** (repo)
  - https://github.com/thu-ml/RIFLEx
  - *From: aikitoria*

- **ComfyUI-WanSeamlessFlow** (repo)
  - https://github.com/fblissjr/ComfyUI-WanSeamlessFlow
  - *From: fredbliss*

- **Triton Windows installation guide** (repo)
  - https://github.com/woct0rdho/triton-windows?tab=readme-ov-file#8-special-notes-for-comfyui-with-embeded-python
  - *From: Kijai*

- **CJ's Wan workflow with split sigmas and torch compile** (workflow)
  - https://civitai.com/models/1301129?modelVersionId=1515505
  - *From: CJ*

- **Step-Video-TI2V model** (model)
  - https://huggingface.co/stepfun-ai/stepvideo-ti2v/tree/main
  - *From: JohnDopamine*

- **Step-Video-TI2V repository** (repo)
  - https://github.com/stepfun-ai/Step-Video-TI2V
  - *From: JohnDopamine*

- **Wan LoRA trainer on Replicate** (tool)
  - https://replicate.com/ostris/wan-lora-trainer
  - *From: Flipping Sigmas*

- **Army man LoRA for 1.3B model** (lora)
  - *From: Flipping Sigmas*

- **ReCamMaster** (research)
  - https://jianhongbai.github.io/ReCamMaster/
  - *From: Juampab12*

- **ComfyUI-WanSeamlessFlow fork** (repo)
  - https://github.com/fblissjr/fork-ComfyUI-WanVideoWrapper
  - *From: fredbliss*

- **ComfyUI-WanSeamlessFlow** (repo)
  - https://github.com/fblissjr/ComfyUI-WanSeamlessFlow/
  - *From: fredbliss*

- **Mobius for video loops** (repo)
  - https://github.com/YisuiTT/Mobius
  - *From: Alisson Pereira*

- **Rotate LoRA** (model)
  - https://huggingface.co/Remade-AI/Rotate
  - *From: The Shadow (NYC)*

- **ConceptAttention paper** (repo)
  - https://github.com/helblazer811/ConceptAttention
  - *From: fredbliss*

- **Mobius looping implementation** (repo)
  - https://github.com/YisuiTT/Mobius
  - *From: fredbliss*

- **ColPali document retrieval** (repo)
  - https://github.com/illuin-tech/colpali
  - *From: fredbliss*

- **Kijai PrecompiledWheels** (repo)
  - https://huggingface.co/Kijai/PrecompiledWheels/tree/main
  - *From: Alisson Pereira*

- **ColPali framework** (repo)
  - https://github.com/illuin-tech/colpali
  - *From: fredbliss*

- **Video Matting RMBG2 node** (tool)
  - https://github.com/tinhalo/ComfyUI-Video-Matting-RMBG2
  - *From: Impactframes.*

- **Torch 2.8 nightly install command** (tool)
  - pip install --pre -U torch torchvision torchaudio --index-url https://download.pytorch.org/whl/nightly/cu128
  - *From: Kijai*

- **Wan-MultiGPU** (repo)
  - https://github.com/intervitens/Wan-MultiGPU
  - *From: aikitoria*

- **PrecompiledWheels** (repo)
  - https://huggingface.co/Kijai/PrecompiledWheels/tree/main
  - *From: Impactframes.*

- **Flash-attention windows wheels** (repo)
  - https://huggingface.co/lldacing/flash-attention-windows-wheel/tree/main
  - *From: Benjimon*

- **Triton for Windows** (repo)
  - https://github.com/woct0rdho/triton-windows
  - *From: JmySff*

- **ComfyUI-GGUF** (repo)
  - https://github.com/city96/ComfyUI-GGUF
  - *From: Jetz*

- **VACE paper** (paper)
  - https://arxiv.org/pdf/2503.07598
  - *From: fredbliss*

- **Wan 2.1 depth control LoRA** (model)
  - https://huggingface.co/spacepxl/Wan2.1-control-loras/tree/main/1.3b/depth
  - *From: spacepxl*

- **WanTraining repository** (repo)
  - https://github.com/spacepxl/WanTraining
  - *From: spacepxl*

- **Start/End frame editing node** (tool)
  - https://github.com/raindrop313/ComfyUI-WanVideoStartEndFrames
  - *From: Eclipse*

- **Original Wan 1.3B fp32 model** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/blob/main/Wan2_1-T2V-1_3B_fp32.safetensors
  - *From: Kijai*

- **Taproot framework** (tool)
  - https://github.com/painebenjamin/taproot
  - *From: TK_999*

- **Restyledfirstframe LoRA** (lora)
  - https://civitai.com/models/1376578?modelVersionId=1555341
  - *From: 852話 (hakoniwa)*

- **Doom FPS Wan2.1 LoRA** (lora)
  - https://civitai.com/models/1376500/doom-fps-wan21-t2v-lora?modelVersionId=1555256
  - *From: Juampab12*

- **FLUXFLOW paper** (research)
  - https://haroldchen19.github.io/FluxFlow/
  - *From: mamad8*

- **ComfyUI-WanVideoStartEndFrames** (repo)
  - https://github.com/raindrop313/ComfyUI-WanVideoStartEndFrames
  - *From: Flipping Sigmas*

- **Cosmos Transfer1** (model)
  - https://huggingface.co/collections/nvidia/cosmos-transfer1-67c9d328196453be6e568d3e
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Wan2.1 depth control workflow** (workflow)
  - https://huggingface.co/spacepxl/Wan2.1-control-loras/blob/main/1.3b/depth/Wan2.1_1.3b_depth_control_lora.json
  - *From: irregularsizes*

- **Depth control LoRAs** (model)
  - https://huggingface.co/spacepxl/Wan2.1-control-loras/tree/main/1.3b/depth
  - *From: TK_999*

- **DepthAnythingV2 ComfyUI node** (repo)
  - https://github.com/kijai/ComfyUI-DepthAnythingV2
  - *From: David Snow*

- **Precompiled Wheels** (repo)
  - https://huggingface.co/Kijai/PrecompiledWheels/tree/main
  - *From: const username = undefined;*

- **Improved ClipVision implementation** (repo)
  - https://github.com/lllyasviel/Paints-UNDO/blob/main/diffusers_vdm/improved_clip_vision.py
  - *From: Kijai*

- **WanTraining** (repo)
  - https://github.com/spacepxl/WanTraining
  - *From: 852話 (hakoniwa)*

- **WAN 2.1 tech report** (paper)
  - https://x.com/StevenZhang66/status/1903035178890485888
  - *From: yi*

- **Rotate LoRA** (lora)
  - https://huggingface.co/Remade-AI/Rotate
  - *From: The Shadow (NYC)*

- **Live Wallpaper Style LoRA** (lora)
  - https://civitai.com/models/1264662/live-wallpaper-style?modelVersionId=1516994
  - *From: The Shadow (NYC)*

- **RES4LYF nodes** (repo)
  - https://github.com/ClownsharkBatwing/RES4LYF
  - *From: Ablejones*

- **ComfyUI-MultiGPU** (repo)
  - https://github.com/pollockjj/ComfyUI-MultiGPU
  - *From: Eclipse*

- **Dynamic Tanh paper** (paper)
  - https://arxiv.org/pdf/2503.10622
  - *From: fredbliss*

- **modular-diffusion** (repo)
  - https://github.com/fblissjr/modular-diffusion
  - *From: fredbliss*

- **WANVideWrapper workflow** (workflow)
  - Available from traxxas25's shared image
  - *From: traxxas25*

- **RES4LYF nodes** (repo)
  - https://github.com/ClownsharkBatwing/RES4LYF
  - *From: Ablejones*

- **Wan2.1 control LoRAs** (model)
  - https://huggingface.co/spacepxl/Wan2.1-control-loras/blob/main/1.3b/depth/Wan2.1_1.3b_depth_control_lora.json
  - *From: ˗ˏˋ⚡ˎˊ-*

- **SAMurai segmentation** (repo)
  - https://github.com/yangchris11/samurai
  - *From: Kijai*

- **DeepGEMM fp8 implementation** (repo)
  - https://github.com/deepseek-ai/DeepGEMM/issues/6
  - *From: fredbliss*

- **Wan2.1 14B T2V LoRAs collection** (model)
  - https://huggingface.co/collections/Remade-AI/wan21-14b-t2v-loras-67dc73d82f66cfac2b4eb253
  - *From: Siraj*

- **Wan2.1 Control LoRAs** (model)
  - https://huggingface.co/spacepxl/Wan2.1-control-loras
  - *From: spacepxl*

- **Time lapse LoRA demo** (model)
  - https://x.com/8co28/status/1903652929481126020
  - *From: 852話 (hakoniwa)*

- **Griptape nodes for RAG** (tool)
  - https://discord.gg/NF6fuAVD
  - *From: LarpsAI*

- **MMAudio for video sound generation** (tool)
  - https://github.com/hkchengrex/MMAudio
  - *From: Benjimon*

- **SimplePod AI for cloud computing** (tool)
  - https://simplepod.ai/
  - *From: LarpsAI*

- **StepVideo 24GB script** (repo)
  - https://github.com/modelscope/DiffSynth-Studio/tree/main/examples/stepvideo
  - *From: deleted_user_2ca1923442ba*

- **DJZ-Nodes audio merging** (repo)
  - https://github.com/MushroomFleet/DJZ-Nodes/tree/main
  - *From: VK (5080 128gb)*

- **Video background removal space** (tool)
  - https://huggingface.co/spaces/innova-ai/video-background-removal
  - *From: VK (5080 128gb)*

- **ComfyUI-Inspyrenet-Rembg** (repo)
  - https://github.com/john-mnz/ComfyUI-Inspyrenet-Rembg
  - *From: David Snow*

- **Wan 2.1 VAE** (model)
  - https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/vae/wan_2.1_vae.safetensors
  - *From: mamad8*

- **Wan prompt guide** (documentation)
  - https://alidocs.dingtalk.com/i/nodes/EpGBa2Lm8aZxe5myC99MelA2WgN7R35y
  - *From: Benjimon*

- **Sam2 points editor workflow** (repo)
  - https://github.com/kijai/ComfyUI-segment-anything-2
  - *From: David Snow*

- **Multi-GPU ComfyUI fork with WAN nodes** (repo)
  - https://github.com/pollockjj/ComfyUI-MultiGPU/tree/rc1_dev
  - *From: VK*

- **SageAttention wheels** (tool)
  - https://github.com/woct0rdho/SageAttention/releases
  - *From: TK_999*

- **LoRA conversion command** (script)
  - *From: Benjimon*

- **Celshaded style workflow** (workflow)
  - https://civitai.com/models/1376578/wanrestyledfirstframeworkflow
  - *From: A.I.Warper*

- **CFG-Zero-star repository** (repo)
  - https://github.com/WeichenFan/CFG-Zero-star
  - *From: yi*

- **Bottleneck-Sampling** (repo)
  - https://github.com/tyfeld/Bottleneck-Sampling
  - *From: mamad8*

- **Wan 2.1 ComfyUI FP16 T5 encoder** (model)
  - https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/tree/main/split_files/text_encoders
  - *From: David Snow*

- **WanRestyledFirstFrameWorkflow** (workflow)
  - https://civitai.com/models/1376578/wanrestyledfirstframeworkflow?modelVersionId=1555341
  - *From: A.I.Warper*

- **Depth LoRA workflow** (workflow)
  - https://huggingface.co/spacepxl/Wan2.1-control-loras/tree/main/1.3b/depth
  - *From: David Snow*

- **Wan2.1-Fun-14B-InP** (model)
  - https://huggingface.co/alibaba-pai/Wan2.1-Fun-14B-InP
  - *From: yi*

- **CFG Zero Star paper** (repo)
  - https://github.com/WeichenFan/CFG-Zero-star
  - *From: Screeb*

- **Qwen chat HD video** (tool)
  - https://chat.qwen.ai/
  - *From: Benjimon*

- **Wan2.1-Fun-1.3B-InP** (model)
  - https://huggingface.co/alibaba-pai/Wan2.1-Fun-1.3B-InP
  - *From: Draken*

- **Wan2.1-Fun-1.3B-Control** (model)
  - https://huggingface.co/alibaba-pai/Wan2.1-Fun-1.3B-Control
  - *From: ˗ˏˋ⚡ˎˊ-*

- **HuggingFace Space for testing** (tool)
  - https://huggingface.co/spaces/alibaba-pai/Wan2.1-Fun-1.3B-InP
  - *From: David Snow*

- **Kijai fp8 converted models** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/blob/main/Wan2.1-Fun-Control-14B_fp8_e4m3fn.safetensors
  - *From: Kijai*

- **VideoX-Fun ComfyUI code** (repo)
  - https://github.com/aigc-apps/VideoX-Fun/tree/main/comfyui
  - *From: yi*

- **VideoX-Fun training repository** (repo)
  - https://github.com/aigc-apps/VideoX-Fun
  - *From: Kijai*

- **Wan2.1-Fun-14B-InP model** (model)
  - https://huggingface.co/alibaba-pai/Wan2.1-Fun-14B-InP
  - *From: ReDiff*

- **Kijai WanVideo ComfyUI weights** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/tree/main
  - *From: Alisson Pereira*

- **Training scripts location** (repo)
  - https://github.com/aigc-apps/VideoX-Fun/tree/main/scripts
  - *From: Cseti*

- **Wan2.1-T2V-1.3B-Reward results** (model)
  - https://huggingface.co/xilanhua12138/Wan2.1-T2V-1.3B-Reward
  - *From: yi*

- **Wan2.1-Fun-1.3B-InP model** (model)
  - https://huggingface.co/alibaba-pai/Wan2.1-Fun-1.3B-InP/blob/main/diffusion_pytorch_model.safetensors
  - *From: Kijai*

- **Wan2.1-Fun-InP-14B_fp8_e4m3fn quantized** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/blob/main/Wan2.1-Fun-InP-14B_fp8_e4m3fn.safetensors
  - *From: Kijai*

- **WanVideoWrapper ComfyUI node** (node)
  - https://github.com/kijai/ComfyUI-WanVideoWrapper
  - *From: Cubey*

- **Alibaba-PAI models collection** (model)
  - https://huggingface.co/alibaba-pai
  - *From: David Snow*

- **VideoX-Fun official demo** (repo)
  - https://github.com/aigc-apps/VideoX-Fun/tree/main
  - *From: Benjimon*

- **ComfyUI native Fun Control support commit** (repo)
  - https://github.com/comfyanonymous/ComfyUI/commit/3661c833bcc41b788a7c9f0e7bc48524f8ee5f82
  - *From: comfy*

- **Sage attention bug report** (repo)
  - https://github.com/comfyanonymous/ComfyUI/issues/7352
  - *From: Question*

- **Wan2.1-Fun-1.3B-Control model** (model)
  - https://huggingface.co/alibaba-pai/Wan2.1-Fun-1.3B-Control/blob/main/diffusion_pytorch_model.safetensors
  - *From: Kijai*

- **Wan2.1-Fun-14B-Control model** (model)
  - https://huggingface.co/alibaba-pai/Wan2.1-Fun-14B-Control/blob/main/diffusion_pytorch_model.safetensors
  - *From: Kijai*

- **ComfyUI-HunyuanLoom** (repo)
  - https://github.com/logtd/ComfyUI-HunyuanLoom
  - *From: chrisd0073*

- **Flow edit tutorial video** (tutorial)
  - https://www.youtube.com/watch?v=0q402EJBZiw&t=30s
  - *From: chrisd0073*

- **TeaCache improved implementation** (repo)
  - https://github.com/welltop-cn/ComfyUI-TeaCache/commit/a6140dea8c139e628082c4fb6b56f53449296384
  - *From: yi*

- **ComfyUI native Wan support** (repo)
  - https://github.com/comfyanonymous/ComfyUI/commit/0a1f8869c9998bbfcfeb2e97aa96a6d3e0a2b5df
  - *From: comfy*

- **Wan technical report** (research paper)
  - https://arxiv.org/abs/2503.20314
  - *From: Pedro (@LatentSpacer)*

- **VideoX-Fun repository** (repo)
  - https://github.com/aigc-apps/VideoX-Fun
  - *From: DawnII*

- **Wan control LoRAs** (model)
  - https://huggingface.co/spacepxl/Wan2.1-control-loras/tree/main/1.3b/depth
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Wan 14B models and CLIP** (model)
  - https://huggingface.co/Wan-AI/Wan2.1-I2V-14B-720P/tree/main
  - *From: 852話 (hakoniwa)*

- **DistillT5 model** (model)
  - https://huggingface.co/LifuWang/DistillT5
  - *From: spacepxl*

- **TripoSF 3D generation** (repo)
  - https://github.com/VAST-AI-Research/TripoSF
  - *From: Kijai*

- **TripoSG 3D generation** (repo)
  - https://github.com/VAST-AI-Research/TripoSG
  - *From: Kijai*

- **Wan Restyled First Frame Workflow** (workflow)
  - https://civitai.com/models/1376578/wanrestyledfirstframeworkflow
  - *From: Hot Hams, the God of Meats*

- **Multi-scene Wan workflow** (workflow)
  - https://youtu.be/L7SYD_pbraA
  - *From: AJO*

- **OptimalSteps technique** (repo)
  - https://github.com/bebebe666/OptimalSteps
  - *From: YatharthSharma*

- **Hulk Transformation LoRA collection** (model)
  - https://huggingface.co/Remade-AI/Hulk-Transformation
  - *From: Draken*

- **Nunchaku optimization toolkit** (repo)
  - https://github.com/mit-han-lab/nunchaku
  - *From: BondoMan*

- **NVIDIA GPU architecture specs** (documentation)
  - Various NVIDIA PDFs for RTX 6000 Pro, 5090, B100
  - *From: aikitoria*

- **DiffSynth Studio LoRAs** (model)
  - https://huggingface.co/Evados/DiffSynth-Studio-Lora-Wan2.1-ComfyUI
  - *From: TimHannan*

- **Wan Video models** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/tree/main
  - *From: artemonary*

- **Fun 1.3B InP model** (model)
  - https://huggingface.co/alibaba-pai/Wan2.1-Fun-1.3B-InP
  - *From: VK (5080 128gb)*

- **Musubi tuner experimental branch** (repo)
  - https://github.com/kohya-ss/musubi-tuner/tree/wan21-fun-control
  - *From: Benjimon*

- **VideoX-Fun training script** (repo)
  - https://github.com/aigc-apps/VideoX-Fun/
  - *From: Benjimon*

- **OptimalSteps** (repo)
  - https://github.com/bebebe666/OptimalSteps
  - *From: const username = undefined;*

- **HART model** (repo)
  - https://github.com/mit-han-lab/hart
  - *From: The Shadow (NYC)*

- **ComfyUI-ppm** (repo)
  - https://github.com/pamparamm/ComfyUI-ppm
  - *From: Johnjohn7855*

- **VGGT point cloud generator** (tool)
  - https://huggingface.co/spaces/facebook/vggt
  - *From: mamad8*

- **TaylorSeer Wan support** (repo)
  - https://github.com/Shenyi-Z/TaylorSeer/blob/main/TaylorSeer-Wan2.1.md
  - *From: yi*

- **CFG distillation LoRAs** (model)
  - https://huggingface.co/spacepxl/wan-cfgdistill-loras
  - *From: yi*

- **Wan fp16 weights** (model)
  - https://huggingface.co/wavespeed/Wan2.1-T2V-14B-Diffusers-fp16
  - *From: DawnII*

- **4K upscaling research** (repo)
  - https://github.com/zhang0jhon/diffusion-4k
  - *From: spacepxl*

- **URAE 4K LoRA** (model)
  - https://huggingface.co/Huage001/URAE/tree/main
  - *From: Kijai*

- **Dataset size research paper** (paper)
  - https://arxiv.org/abs/2310.16825
  - *From: spacepxl*

- **Diffusers conversion script** (script)
  - https://github.com/huggingface/diffusers/blob/main/scripts/convert_wan_to_diffusers.py
  - *From: spacepxl*

- **Diffusion-pipe optimization** (repo)
  - https://github.com/tdrussell/diffusion-pipe
  - *From: ChronoKnight*

- **OptimalSteps optimization** (repo)
  - https://github.com/bebebe666/OptimalSteps
  - *From: yi*

- **Studio Ghibli style LoRA for Wan 2.1** (lora)
  - https://civitai.com/models/1404755/studio-ghibli-style-wan21-t2v-14b?modelVersionId=1587891
  - *From: ChronoKnight*

- **Flat Color Style LoRA** (lora)
  - https://civitai.com/models/1132089/flat-color-style?modelVersionId=1474944
  - *From: ChronoKnight*

- **Semi-Pixelated Style LoRA** (lora)
  - https://civitai.com/models/1384559/semi-pixelated-style-or-or-wan-21?modelVersionId=1564553
  - *From: ChronoKnight*

- **WAN 2.1 I2V Fast Workflow** (workflow)
  - https://civitai.com/models/1385056/wan-21-image-to-video-fast-workflow
  - *From: lostintranslation*

- **Flux block testing workflow and research** (workflow)
  - https://civitai.com/models/886270
  - *From: ChronoKnight*

- **TinyVAE for Wan** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/tree/main
  - *From: Juampab12*

- **Execution Inversion Demo for ComfyUI loops** (tool)
  - https://github.com/BadCafeCode/execution-inversion-demo-comfyui
  - *From: PirateWolf*

- **8 GPU Turin motherboard** (hardware)
  - https://www.asrockrack.com/general/productdetail.asp?Model=TURIN2D24G-2L%2b/500W#Specifications
  - *From: aikitoria*

- **DiffSynth Studio LoRAs for Wan 2.1** (model)
  - https://huggingface.co/Evados/DiffSynth-Studio-Lora-Wan2.1-ComfyUI/tree/main
  - *From: David Snow*

- **Wan 2.1 prompting guide** (guide)
  - https://www.instasd.com/post/mastering-prompt-writing-for-wan-2-1-in-comfyui-a-comprehensive-guide
  - *From: N0NSens*


## Known Limitations

- **Maximum 81 frames supported**
  - Wan doesn't support 121 frames, use 81 max for best stability
  - *From: yi*

- **No 1.3B I2V model available**
  - 1.3B model variant doesn't exist for Image-to-Video
  - *From: Kijai*

- **GGUF not compatible with wrapper**
  - GGUF models require native implementation, can't use with wrapper
  - *From: seitanism*

- **4K generation produces grey blurry mess**
  - 4K video generation with 1.3B model results in poor quality, 1920x1080 works better
  - *From: seitanism*

- **BF16 weights not ideal with FP16 accumulate**
  - Using bf16 weights with fp16 accumulate is not recommended
  - *From: Kijai*

- **Frame counts above 81 cause severe artifacts**
  - Model default is 81 frames, 121+ frames show blocky glitches and degradation
  - *From: Kijai*

- **1.3B model has significant rope/dot artifacts**
  - Especially rough with fur, hair textures - 14B model much cleaner
  - *From: Draken*

- **SpargeAttn requires 24+ hours of tuning per model/settings**
  - 5 passes recommended, single pass ruins image quality, not practical for general use
  - *From: Kijai*

- **16fps makes fast motion scenes difficult**
  - Low framerate hurts model's ability to learn motion in rapid scenes
  - *From: seitanism/deleted_user_2ca1923442ba*

- **fp8 matrix multiplication performs poorly**
  - Significant quality degradation compared to fp16 accumulation
  - *From: comfy*

- **Video models poor at v2v cleanup**
  - Don't perform as well as image models for cleanup tasks
  - *From: Draken*

- **Context sliding without control does whatever it wants**
  - Not very controllable without control nets or v2v
  - *From: Kijai*

- **GGUF support not available in wrapper**
  - Would require significant work to implement
  - *From: David Snow*

- **Native implementation requires strict size adherence**
  - Produces poor results with non-optimal sizes for the model
  - *From: T8star-Aix*

- **Wan 1.3B is T2V only**
  - Cannot set first image directly, only T2V capability
  - *From: hablaba*

- **Resolution constraints in wrapper**
  - 832x480 gets changed to 816x480 automatically
  - *From: seitanism*

- **Skyreels overtrained on portrait images**
  - Lost Hunyuan's native 720p capability, works best at 540p
  - *From: Doctor Shotgun*

- **Artifacts on first frame of I2V**
  - Encoded and decoded original image shows artifacts
  - *From: Doctor Shotgun*

- **TeaCache quality degradation with aggressive settings**
  - Using too low threshold or wrong start_step causes noise, flickering circles, and artifacts. Quality hit when skipping half the steps
  - *From: Kijai*

- **Model not flexible with frame conditioning**
  - Using last frame instead of first frame doesn't work at all, unlike cosmos img2vid
  - *From: comfy*

- **TeaCache may not work consistently across all setups**
  - Some users report no speed difference, possibly due to memory offloading or other factors
  - *From: TK_999*

- **I2V upscaling often changes original image too much**
  - Either distorts the original significantly or provides minimal improvement
  - *From: seitanism*

- **Can't use 480p resolution with 720p model**
  - Resolution mismatch causes issues, need to match model resolution
  - *From: N0NSens*

- **GGUF models don't work with Kijai's wrapper nodes**
  - Currently no support for GGUF format in the wrapper implementation
  - *From: Shawneau*

- **bf16 text encoder still uses 40GB RAM**
  - Even with bf16 model, RAM usage remains very high
  - *From: slmonker*

- **SparseAttention extremely slow**
  - Takes 5+ hours per pass, needs at least 5 passes, potentially 25+ hours total
  - *From: Juampab12*

- **TeaCache doesn't work with stochastic samplers**
  - Stochastic samplers like DPM++ 2SA add noise every step, preventing TeaCache from recognizing input/output correspondence
  - *From: Kijai*

- **TeaCache fails above 209 steps**
  - TeaCache crashes with AssertionError when using step counts above 209
  - *From: DiXiao*

- **fp8e4nv not supported on RTX 3000 series**
  - RTX 3090 and similar cards can't use e4nv quantization with torch.compile
  - *From: Kijai*

- **Context options don't work with TeaCache**
  - TeaCache produces blurred video when used with context options
  - *From: NebSH*

- **Video models don't work with text encoder/clip vision across implementations**
  - Video models work across implementations, but umt5 and clip vision do not
  - *From: comfy*

- **fp8 fast causes huge quality hit**
  - Using fp8_fast precision significantly degrades output quality
  - *From: Kijai*

- **RifleX maximum is 2x default frames (161)**
  - RifleX still only works up to 2x the default frame count
  - *From: Kijai*

- **torchao fp8 modes don't support offloading**
  - Memory management limitation with torchao fp8 implementations
  - *From: Kijai*

- **Context windowing for I2V uses same image each window**
  - Each context window starts with the same input image rather than evolving
  - *From: Kijai*

- **TeaCache can't work with context windows**
  - Maybe not even possible to implement TeaCache for context windowing
  - *From: Kijai*

- **Enhance A Vid adds senseless details**
  - Even at weight 1.5 with start 0.1 end 0.8, enhancement can add unwanted artifacts
  - *From: Juampab12*

- **RifleX results not amazing above 161 frames**
  - Works since today but quality degrades significantly beyond 161 frame limit
  - *From: Kijai*

- **WanVideo struggles with human-car interactions**
  - Model has difficulty with character-vehicle interaction scenes
  - *From: TK_999*

- **TeaCache incompatible with context windowing**
  - Cannot use TeaCache acceleration when using context window settings
  - *From: Kijai*

- **FP32 models show no quality improvement**
  - FP32 takes 4x longer but produces identical results to FP16
  - *From: N0NSens*

- **SpargeAttention tuning extremely slow**
  - Requires 5+ hours per run, with 24h total recommended. Results often terrible
  - *From: Kijai*

- **RTX 3090Ti doesn't support FP8 natively**
  - FP8 support introduced with Ada Lovelace/Hopper architecture, works but not faster
  - *From: Benjimon*

- **Interpolation can wreck small movements**
  - Facial expressions and fine details may suffer with interpolation approach
  - *From: TK_999*

- **Adaptive Guidance doesn't work with TeaCache in native**
  - TeaCache implementation can't handle CFG splitting
  - *From: Kijai*

- **Alternative T5 models don't work well**
  - Pile T5 and regular t5_xxl don't work properly with Wan
  - *From: Juampab12*

- **Hair often becomes pixelated mess**
  - Hair frequently distorts in generated videos
  - *From: GalaxyTimeMachine*

- **Non-81 frame counts are suboptimal**
  - Model works best with exactly 81 frames
  - *From: Kijai*

- **Looping workflows crash after several iterations**
  - 480p crashes around 7th loop, 720p around 3rd loop with no error messages
  - *From: AJO*

- **Native can't handle certain images properly**
  - Specific beard noise issues that multiple users have confirmed
  - *From: Kijai*

- **TeaCache doesn't work with SDE samplers**
  - Causes tensor boolean value errors
  - *From: Kijai*

- **Context + TeaCache causes fritzy outputs**
  - Using both context options and TeaCache together produces unstable results
  - *From: fearnworks*

- **Model heavily trained on photorealistic content**
  - Difficulty generating non-realistic outputs like anime style or abstract videos
  - *From: fredbliss*

- **Cannot cancel generation mid-step**
  - Still no ability to interrupt generation during step execution
  - *From: Juampab12*

- **TeaCache causes face changes in i2v**
  - Significant facial alterations when teacache enabled
  - *From: Aube*

- **GGUF support not available in Kijai loader**
  - GGUF loading requires additional code and is slower
  - *From: Kijai*

- **TeaCache incompatible with context windowing**
  - Cannot use both features together - causes noise artifacts
  - *From: Kijai*

- **RifleX causes constant looping artifacts**
  - Even with developer PR fixes, still produces looping behavior in long generations
  - *From: Kijai*

- **Context windowing doesn't work with unfinished images**
  - Cannot inject new start frames mid-generation, only works with complete images
  - *From: Kijai*

- **Prompt travel produces poor spatiotemporal consistency**
  - Naive prompt interpolation doesn't maintain spatial and temporal alignment across transitions
  - *From: fredbliss*

- **TeaCache doesn't work on larger WAN models**
  - The new TeaCache implementation only works on 1.3B model, coefficients don't work for 14B or I2V
  - *From: Kijai*

- **First context window doesn't blend well with subsequent windows**
  - There's a noticeable transition/reset effect between the first and second context windows
  - *From: Cubey*

- **Context window prompts are too different**
  - When prompts vary too much between windows, the model struggles to maintain coherence
  - *From: Kijai*

- **Color oversaturation tendency**
  - WAN tends to oversaturate colors compared to other models
  - *From: ybo678*

- **Multiple prompts don't inject new images**
  - Context windows with different prompts still try to force the original input image to control the scene
  - *From: AJO*

- **TeaCache incompatible with context windows**
  - Cannot use TeaCache when generating long videos with context windows
  - *From: Kijai*

- **LoRAs require specific setup in native**
  - In native you need to use either compile node in Wavespeed nodes or model patch order node
  - *From: Kijai*

- **Latent upscale produces poor quality**
  - Should avoid latent upscale, use pixel space upscalers instead
  - *From: Kijai*

- **14B model can't use batched cfg**
  - Too much VRAM required for batching positive/negative prompts in 14B model
  - *From: Kijai*

- **TensorRT engines are GPU-specific**
  - Compiled engines only work on same GPU model they were created on
  - *From: Dream Making*

- **TeaCache incompatible with context windowing**
  - Cannot use TeaCache acceleration with context windowed generation
  - *From: TK_999*

- **Ultimate SD upscale has tile borders and quality degradation**
  - While it fits in 16GB VRAM, upscaling is very slow with visible tile seams and image falling apart
  - *From: Cseti*

- **FPS interpolation still experimental**
  - Code is messy, has bugs, and results can be inconsistent or produce noise
  - *From: fredbliss*

- **16fps hardcoded output**
  - Main issue after extensive testing - output is locked to 16fps
  - *From: ˗ˏˋ⚡ˎˊ-*

- **TeaCache only works on 1.3B model**
  - Updated TeaCache still only compatible with 1.3B variant
  - *From: Kijai*

- **fp8_e4m3fn compilation doesn't work on RTX 3090**
  - Only works on 4000 series and up, RTX 3090 needs fp8_e5m2
  - *From: Kijai*

- **Context and TEA are exclusive**
  - Cannot combine context windows with TEA cache, also TEA and riflex are exclusive
  - *From: ˗ˏˋ⚡ˎˊ-*

- **102 frame count causes 98% VRAM and freezing**
  - On 4070 12GB at 720x480, 102 frames hits 98% VRAM and freezes system
  - *From: for1096*

- **1.3B model lacks image-to-video**
  - Only 14B model has I2V capability, 1.3B is T2V only
  - *From: Screeb*

- **Wan I2V models are very slow**
  - I2V models are 7-8 times slower than the 1.3B T2V model
  - *From: David Snow*

- **Wrapper has higher memory usage**
  - Wrapper uses 90-100% RAM vs 40% for native, causing OOM issues at higher resolutions
  - *From: AJO*

- **Wan Feta Enhance doesn't work with TeaCache**
  - Enhancement feature requires proper patching to work together with TeaCache
  - *From: Kijai*

- **Context windows don't work with TeaCache**
  - Unable to get TeaCache working with context sliding windows despite attempts
  - *From: Kijai*

- **No taesd equivalent for video models**
  - Unlike Flux/SD which have taesd for quick previews, video models only have latent2rgb which is linear mapping vs VAE's non-linear
  - *From: deleted_user_2ca1923442ba*

- **Wrapper custom model types incompatible with standard nodes**
  - Wrapper outputs custom model/VAE types that can't be used with normal ComfyUI nodes like VAE encode
  - *From: hablaba*

- **CFG 1.0 setting not achievable**
  - ComfyUI rounds CFG values so exactly 1.0 cannot be set
  - *From: Kijai*

- **Camera motion prompts don't work well**
  - WAN model doesn't seem to react to 'camera', both WAN and Hunyuan seem not trained well with camera motion prompts
  - *From: ByArlooo*

- **Latent interpolation not feasible with 3D VAE**
  - The vae, since its 3d, is never going to allow latent interpolation. These VAEs don't play nice with interpolation in latent space, they're more like downsample models than embedding models
  - *From: spacepxl*

- **8 fps alignment limitation**
  - LTX has 8 fps alignment for some reason, working on removing the assumption that time_scale_factor is always 8
  - *From: Juampab12*

- **720p resolution is very slow**
  - 720p model at 720p resolution significantly slower than lower resolutions
  - *From: Cubey*

- **Sage attention doesn't work with all GPUs for Wan**
  - Need specific sageattn 2.0 mode, not compatible with all GPU configurations
  - *From: Kijai*

- **LTX VAE is quite lossy**
  - Quality loss when using LTX VAE for frame interpolation
  - *From: Juampab12*

- **Context windows 20-23 have more random crazy moments**
  - Too much change in smaller context windows can cause latents that make no sense
  - *From: Cubey*

- **Wan has lower fps output**
  - Motion quality is inferior to Hunyuan I2V without interpolation
  - *From: aikitoria*

- **Sliding window not good quality solution**
  - More like a cool trick, not useful without control, degrades after multiple chained generations
  - *From: Juampab12*

- **Flash attention is slower and requires compilation**
  - Even slower than SAGE and needs time-consuming compilation process
  - *From: intervitens*

- **Multi-GPU Wan requires shutting down other VRAM-intensive processes**
  - Cannot run alongside TRTLLM due to VRAM requirements
  - *From: aikitoria*

- **Wan always does slow motion**
  - Tendency to generate slow motion content even when not requested
  - *From: seitanism*

- **Multi-GPU scaling issues**
  - Higher ring_size values don't improve performance, sometimes slower
  - *From: aikitoria*

- **Context windows don't work well very short**
  - Very short context windows have poor results
  - *From: Draken*

- **Vehicle direction consistency issues**
  - Long context generation can make vehicles drive backwards and forwards simultaneously
  - *From: Uehreka*

- **Quantization quality loss**
  - Quantizing video models gives worse results compared to Flux quantization
  - *From: comfy*

- **Cannot use torch compile with VRAM management node**
  - Causes CppCompilError when used together
  - *From: Kijai*

- **LoRAs don't work with native + compile without patch**
  - Requires patch model patch order node as workaround
  - *From: mamad8*

- **Wan struggles with 2D styles**
  - Not great for 2D art styles, tends to stay realistic
  - *From: TK_999*

- **Wan has camera movement issues**
  - Camera still moves more than desired even with prompting
  - *From: Shawneau 🍁 [CA]*

- **Cannot use setnode/getnode for teacache args**
  - Hit and miss when trying to use those nodes with teacache
  - *From: burgstall*

- **Long prompts may not work well with Wan**
  - Wan may not enjoy very long prompts unlike some other models
  - *From: burgstall*

- **Can't do low frame counts with context windows**
  - Context windows don't work well with short sequences
  - *From: Organoids*

- **Context stride doesn't work with Wan models**
  - Latent space structure prevents stride functionality
  - *From: Kijai*

- **TeaCache makes character motion unnatural and blurry**
  - Quality trade-off for speed, especially noticeable on 3060 12GB
  - *From: ArcherEmiya*

- **LoRAs don't work with torch compile in native**
  - Technical incompatibility requiring model patcher workaround
  - *From: zoz*

- **V2V with I2V model doesn't work with context windows**
  - Technical limitation preventing longer V2V generations
  - *From: AJO*

- **T5 cannot handle complex long-range dependencies**
  - Cannot do complex instructions like 'pour wine on eyeball and be totally still'
  - *From: fredbliss*

- **720p model produces awful results at 480x277**
  - Models shouldn't be used outside their trained resolution
  - *From: N0NSens*

- **1080p generation produces motion artifacts**
  - Quality degrades with shimmering at edges beyond 720x1280 center area
  - *From: aikitoria*

- **High resolution generation is impractical**
  - 40 minutes on 4x 4090s for 1080p
  - *From: aikitoria*

- **Going over 81 frames doesn't work right**
  - Becomes weird rather than proper looping, wish it had a 'continue video' option as using end frame to start new sequence gives unusable results
  - *From: aikitoria*

- **CFG 1.0 is very destructive on Wan**
  - Unlike distilled models, Wan quality is killed by CFG 1.0
  - *From: Kijai*

- **Context windows difficult to work with**
  - Context windows are too difficult to work with for Wan model
  - *From: TK_999*

- **A6000 cards slow for inference**
  - Good for training but will always be slow for inference
  - *From: Benjimon*

- **Upscaling Wan outputs often doesn't improve actual quality**
  - Models like Topaz fail to add useful detail, just increase resolution without real quality gain
  - *From: aikitoria*

- **Reactor face swap doesn't work well with head turning**
  - Works for static faces but struggles with more complex head movements
  - *From: N0NSens*

- **Enhance a Video limited usefulness**
  - May not provide meaningful improvement for I2V workflows
  - *From: Kijai*

- **16fps output limitation**
  - Wan outputs at 16fps which requires interpolation for smoother results
  - *From: JohnDopamine*

- **Poor English noun understanding**
  - Sometimes fails to recognize common English words, may be due to bilingual training or VLM captioning issues
  - *From: Screeb*

- **Context sensitivity issues**
  - Extremely context-sensitive which can limit creativity
  - *From: Screeb*

- **High memory requirements**
  - 14B model requires up to 128GB RAM plus swap space
  - *From: Benjimon*

- **Walking toward viewer prompts don't work well**
  - Old Hunyuan prompts for walking toward viewer result in static standing poses in Wan
  - *From: Doctor Shotgun*

- **Block swap is RAM inefficient**
  - Uses non-blocking transfers which consume more RAM
  - *From: Kijai*

- **3000 series GPU torch compile limitations**
  - Can only handle e5m2 fp8 format with torch compile, not e4m3fn
  - *From: Kijai*

- **I2V context windows don't work reliably**
  - Using same image for all windows doesn't progress well, needs better method to incorporate image guidance
  - *From: Kijai*

- **Video extension has motion breaks**
  - Clear breaks in motion when generating from last frame, 161 frames works somewhat but not reliably
  - *From: aikitoria*

- **Cakify LoRA resolution limited**
  - Trained only on 168x350 resolution
  - *From: Juampab12*

- **Python 3.13 compatibility issues**
  - Python 3.13.2 still has some issues with current setup
  - *From: Kijai*

- **1.3B model doesn't know certain characters**
  - Doesn't recognize Shrek or hippos
  - *From: Kijai*

- **No I2V support for 1.3B model**
  - T2V only, at least not yet
  - *From: spacepxl*

- **Control LoRA doesn't work with compile**
  - Compile causes issues with control LoRA functionality
  - *From: TK_999*

- **Can't unload only one LoRA currently**
  - End percent affects all LoRAs, not individual ones
  - *From: Kijai*

- **Control is too strong**
  - Reducing LoRA strength breaks it after a point, multiplying latent doesn't work
  - *From: Kijai*

- **Video extend approach doesn't work**
  - Model not smoothing out transitions when forcing earlier latent frames
  - *From: aikitoria*

- **Tiled diffusion has blending artifacts**
  - Not handling noise correctly - should generate noise once at full res then crop, not independently per tile
  - *From: spacepxl*

- **I2V training difficulty**
  - Hard to balance input likeness and motion - requires good data curation or model just generates very little motion
  - *From: spacepxl*

- **Longer video generation issues**
  - Generate new from last frame: bad motion kinks, quality loss. Multiple frame extensions produce artifacts and wrong transitions
  - *From: aikitoria*

- **Camera prompts don't work in I2V**
  - Tested for an hour with 12 attempts, camera prompts had no effect in I2V mode
  - *From: N0NSens*

- **Frame count limit without context**
  - Over 81 frames causes speckles/unresolved noise unless using context options
  - *From: VRGameDevGirl84(RTX 5090)*

- **Face quality at high resolution**
  - At 1280x720x81 with full body, faces have bad quality even at 50 steps
  - *From: seitanism*

- **Torch compile + LoRA incompatibility in native**
  - Can't use torch compile and LoRA together in native workflow due to memory issues
  - *From: zoz*

- **Wan cannot do longer videos beyond 81 frames**
  - Model never trained with frames outside 81 range, produces garbage even though rope can go further
  - *From: aikitoria*

- **Cannot extend with multiple start frames**
  - Model never trained with more than one start frame, produces garbage when extending mask
  - *From: aikitoria*

- **Poor celebrity and character recognition**
  - Doesn't know most celebs or iconic characters well, produces 'great value' versions
  - *From: spacepxl*

- **Torch compile and LoRA cannot work together**
  - Either compile works or LoRA works, but not both simultaneously without special workarounds
  - *From: Kijai*

- **TeaCache quality degradation**
  - Hit or miss results, more movement causes more degradation, increased fail rate
  - *From: aikitoria*

- **CFG distillation LoRA compatibility**
  - 1.3B CFG distill LoRA doesn't work with 14B models due to shape mismatch
  - *From: Kijai*

- **Context windows drift in I2V**
  - Image conditioning becomes weaker over time, causing drift away from original image
  - *From: Cubey*

- **720p inference speed**
  - 720p is painful for speed, even with optimizations
  - *From: Kijai*

- **Multi-character LoRA training**
  - Training multiple characters in same LoRA doesn't work well
  - *From: Juampab12*

- **TeaCache breaks with big motion**
  - TeaCache causes quality issues with large motion content and may require multiple generations
  - *From: Payuyi*

- **Batch CFG incompatible with I2V**
  - Tensor size mismatch errors when using batch CFG with I2V mode
  - *From: Juampab12*

- **LoRAs trained on one model size don't work on another**
  - LoRAs trained for 1.3B and 14B models are not intercompatible
  - *From: Kijai*

- **Windows memory allocation issues**
  - Windows has poor memory management causing crashes even with 64GB RAM, works better on Linux
  - *From: Kijai*

- **Can't unload models from RAM mid-run in ComfyUI**
  - General ComfyUI limitation, force_offload only moves from VRAM to RAM
  - *From: Kijai*

- **No 1.3B I2V model exists**
  - Only 14B variants available for I2V
  - *From: Juampab12*

- **No useful way to make longer videos**
  - All extension methods attempted have failed
  - *From: aikitoria*

- **Video quality degrades beyond 81 frames**
  - Model can generate 161 frames but wasn't trained on longer lengths, causes looping artifacts
  - *From: aikitoria*

- **Skip block technique doesn't work on all models**
  - Block 10 skip works on 14B but not on 1.3B model, no universal solution found
  - *From: Kijai*

- **Low resolutions like 640x352 always have artifacts**
  - Wan dots and quality issues persist at lower resolutions
  - *From: Kijai*

- **Confetti and high-detail elements cause artifacts**
  - Similar to video compression issues, confetti, snow, rain cause problems due to high information content
  - *From: spacepxl*

- **Preview not useful until late in generation**
  - Wan preview is still messy at step 20, only becomes sensible approaching step 40
  - *From: aikitoria*

- **WAN model can't extend videos**
  - Cannot do temporal expansion or extend beyond original length, splitting generation requires separate T2V pass
  - *From: Kijai*

- **Control tile lora not suitable for already high-quality videos**
  - Works best on lower quality, lower resolution inputs. Limited effectiveness on already detailed, high-quality sources
  - *From: Payuyi*

- **VAE quality degrades with highly different frames**
  - When 4 frames in a latent are very different, VAE quality decreases rapidly, making timelapse training difficult
  - *From: mamad8*

- **Video upscaling still not production ready**
  - Current video AI tools lack the specialist tooling needed, unlike image generation which can adapt tools from other areas
  - *From: deleted_user_2ca1923442ba*

- **WAN doesn't recognize Superman well**
  - Similar to HunyuanVideo with celebrities - hit or miss results
  - *From: The Shadow (NYC)*

- **Concept erasure for adult content**
  - Model appears to have concept-erased certain terms, causing 'phallus' to generate towers instead
  - *From: fredbliss*

- **SkipLayerGuidanceDiT won't work with native WAN**
  - WAN doesn't have single/double blocks and lacks the patching mechanism needed
  - *From: Kijai*

- **Matrix Agent morphing effects at higher frame counts**
  - TeaCache/EaV can induce morphing artifacts on hands and faces when pushing to 81 frames
  - *From: The Shadow (NYC)*

- **Wan doesn't work well with just 16 frames**
  - Needs at least 81 frames to work best, 33 can work to some extent
  - *From: Kijai*

- **No FPS conditioning in model**
  - Cannot change fps setting as model wasn't trained with fps conditioning
  - *From: Kijai*

- **Context windows not useful except for vid2vid**
  - AnimateDiff-style context windows aren't beneficial for most use cases
  - *From: Kijai*

- **RIFLEx ruins quality**
  - Method to extend beyond 81 frames degrades quality in testing
  - *From: Kijai*

- **480p LoRAs don't work well on 720p**
  - Cross-resolution LoRA usage loses detail fidelity
  - *From: Benjimon*

- **TeaCache incompatible with SDE sampler**
  - TeaCache won't work when using DPM++ SDE sampler
  - *From: Kijai*

- **Block swap not very RAM efficient**
  - Uses significantly more RAM compared to native implementation
  - *From: Kijai*

- **First frame color/brightness shifts in I2V**
  - Input images get slightly darker, especially noticeable with oil painting styles
  - *From: seitanism*

- **Can't do CFG=1.0 without model distillation**
  - Currently only a LoRA exists for 1.3B model to enable CFG-free generation
  - *From: Kijai*

- **Inconsistent generation with same seed**
  - Some optimization nodes introduce hidden randomness
  - *From: seitanism*

- **I2V weights don't propagate first frame information in context windows**
  - Cannot force change latents to maintain consistency across windows
  - *From: aikitoria*

- **Context window resets cause visible quality drops**
  - Resets happen every 5 seconds but timing can be inconsistent (8-9 seconds observed)
  - *From: Cubey*

- **SLG causes slow-motion effect with character LoRAs**
  - Especially noticeable with lots of movement like running, despite quality improvements
  - *From: BondoMan*

- **Torch compile is flaky and can break when changing settings**
  - Often requires model reloading to fix, can cause inconsistent errors
  - *From: Kijai*

- **Single frame extension causes motion kinks**
  - Using single frame for video extension creates discontinuities
  - *From: aikitoria*

- **fp8_fast ruins quality on Wan model**
  - While faster, fp8_fast completely destroys output quality despite speed gains
  - *From: Kijai*

- **TeaCache makes iteration speed hard to monitor**
  - Variable caching makes it difficult to measure true performance improvements
  - *From: Kijai*

- **Step-Video-TI2V requires 4+ GPUs**
  - Model is too heavy for single GPU setups, similar to other large video models
  - *From: JohnDopamine*

- **Context windowing requires very similar prompts**
  - For multiple prompts to work effectively, they must be very similar with only small changes
  - *From: Kijai*

- **1.3B and 14B LoRAs not compatible**
  - LoRAs trained on different model sizes don't work across versions
  - *From: Kijai*

- **14b and 14b 720p LoRAs incompatible**
  - Resolution mismatch causes pure chaos, likely due to training resolution differences
  - *From: Cubey*

- **Context options poor continuity with I2V**
  - Always returns to init image, only works if camera doesn't move
  - *From: Kijai*

- **Image-only LoRA datasets degrade motion**
  - Training only on images causes glitchy movement when character needs to move
  - *From: Kytra*

- **TeaCache doesn't work with Context options**
  - TeaCache interferes with Context options functionality
  - *From: Lumi*

- **WanVideo struggles with very short videos**
  - 21-frame videos produce artifacts and blowouts, likely because context is too small for effective processing
  - *From: TK_999*

- **Extreme lighting transitions cause whiteout effects**
  - Direct transitions between drastically different lighting conditions (night to day) cause model to overcompensate with extreme brightness
  - *From: fredbliss*

- **Looping technique doesn't work well on I2V**
  - While T2V looping works well, I2V results are not as good with the looping technique
  - *From: Kijai*

- **14B model has issues with T2V looping**
  - 14B variant showing problems with T2V looping that don't occur with 1.3B model
  - *From: Kijai*

- **I2V doesn't work well with context windows**
  - Every window just has same image, doesn't go far unless camera doesn't move
  - *From: Kijai*

- **Loop + blending techniques don't work well together**
  - Opposite goals - looping vs content-aware transitions
  - *From: fredbliss*

- **Extreme scene changes fail with context windows**
  - red panda to fox transition didn't work
  - *From: Kijai*

- **Mobius looping doesn't work with I2V**
  - CLIP embeddings keep swinging back to single point
  - *From: fredbliss*

- **SLG destroys picture quality**
  - SLG option provides speed but significantly degrades visual quality
  - *From: N0NSens*

- **Looping doesn't work well with 14B models**
  - Looping seems to only like 1.3B model and hates TeaCache
  - *From: Kijai*

- **Perfect loops are difficult**
  - Background always warps in loops, perfect loop would probably need static shot with mask on character
  - *From: Cubey*

- **Context windows break with I2V**
  - Context windows break hard with I2V, making seamless looping difficult
  - *From: Draken*

- **81 frame limit**
  - WanVideo maxes out at 81 frames, extension methods exist but smooth transitions not yet discovered
  - *From: fredbliss*

- **Multi-GPU diminishing returns**
  - No benefit to adding more than 4 GPUs due to excessive data transfer
  - *From: aikitoria*

- **1.3b LoRAs don't work with 14b models**
  - Weight incompatibility between different model sizes
  - *From: spacepxl*

- **Comfy-org 1.3B models incompatible with wrapper**
  - Different key format prevents use in WanVideoWrapper
  - *From: Kijai*

- **Depth LoRA struggles with pure black values**
  - Solid black in depth maps causes issues, need to lift to higher values
  - *From: Kijai*

- **WIP depth LoRA has inconsistent prompt following**
  - Needs recaption with dense VLM captions and continued training
  - *From: spacepxl*

- **SLG doesn't work well when cfg gets batched**
  - Happens when there's lots of memory free, automated in ComfyUI
  - *From: Kijai*

- **81 frame limit due to position encoding**
  - LoRA won't change frame limit, need PE rescaling or context windows
  - *From: spacepxl*

- **End frame never matches perfectly**
  - Model not good enough to reach perfect end frame matching
  - *From: Kijai*

- **Depth control only available for 1.3B model**
  - Not compatible with 14B models, so no i2v depth control
  - *From: spacepxl*

- **VAE context windows don't work well**
  - Have to be halfway through to have anything remotely usable as image condition
  - *From: Kijai*

- **Start/End frame not true interpolation**
  - Model isn't trained for interpolation - never reaches end frame perfectly, only pulls towards it
  - *From: Kijai*

- **ClipVision always 224x224 resolution**
  - Cannot process higher resolution vision inputs, always downscaled to 224x224
  - *From: Kijai*

- **TorchAO models cannot be offloaded**
  - Makes quantized models painful to use due to memory constraints
  - *From: Kijai*

- **Timing offsets with dual image inputs**
  - Extra frames added at beginning and end when using both start/end images
  - *From: The Shadow (NYC)*

- **720p model requires higher resolutions**
  - 512x720 too low for 720p model, needs 1280x720+ or use 480p model instead
  - *From: Kijai*

- **SLG doesn't work well with all samplers**
  - Some samplers behave weirdly with SLG, Euler recommended
  - *From: Kijai*

- **FP8 GEMM operations don't work properly**
  - Attempts to use fp8 scaled matmul just doesn't work
  - *From: Kijai*

- **Most paper optimizations not in released code**
  - Much of the advanced caching and optimization techniques from paper aren't implemented
  - *From: Kijai*

- **Start/End frame morphing does simple wipe**
  - Without additional techniques, creates basic wipe transition rather than smooth morph
  - *From: The Shadow (NYC)*

- **Model cannot reliably hit end frames without training**
  - Pretty sure the model can't fully do end frame accuracy without LoRA training
  - *From: Kijai*

- **TeaCache quality degradation above 0.2 threshold**
  - Will lose quality for sure above 0.2 especially
  - *From: Kijai*

- **Latent masking has inherent quality issues**
  - Rest of video still goes through VAE which is lossy, requires pixel space compositing
  - *From: Kijai*

- **Face morphing issues in generated videos**
  - Faces morph during generation, may need LoRA or FaceID node solution
  - *From: traxxas25*

- **Loop args doesn't work with 14B models**
  - Unknown reason why it fails with larger models
  - *From: Kijai*

- **Context window uniform loop extremely slow with 14B**
  - Takes 30+ minutes for 5 seconds of video
  - *From: const username = undefined;*

- **Wan produces unwanted camera movement**
  - Difficult to keep camera static even with prompts like 'static', 'fixed', 'no camera movement'
  - *From: Faux*

- **Grain texture artifacts at lower resolutions**
  - Noticeable grain and artifacts when going below 1024x576
  - *From: Ghost*

- **Motion going backwards in videos**
  - Frequent issue especially noticeable with cars racing in reverse
  - *From: Jas*

- **TeaCache degrades video quality by skipping steps**
  - Useful for seed hunting but not for final HQ generation
  - *From: Benjimon*

- **VAE has limitations with 2-frame sequences**
  - Need at least 5 frames with identical last 4 frames for proper LoRA training
  - *From: Juampab12*

- **Non-standard resolutions can cause VAE artifacts**
  - Even when divisible by 32, unusual aspect ratios like 1056x896 can produce artifacts
  - *From: mamad8*

- **Control LoRAs don't stack together**
  - Only one control input to model, multiple control loras try to use same input
  - *From: spacepxl*

- **Prompt travel has weak effect due to video attention blending**
  - Video attention is not segmented so it blends overall, next step is learning to mask that
  - *From: Kijai*

- **Full subject changes bleed too much with prompt travel**
  - Motion prompts work well but subject changes like 'red panda|dog' don't work cleanly
  - *From: Kijai*

- **Condition images too strong to override with prompt travel**
  - Only works for clip embed and prompt, not for conditioning images
  - *From: Kijai*

- **Can't do inference with 14B LoRAs on 1.3B model**
  - Models have different architectures preventing cross-compatibility
  - *From: Kijai*

- **Block swap performance issues with under 64GB RAM**
  - Very slow renders and OOM issues when insufficient system RAM
  - *From: Obsolete*

- **Depth LoRA only works with 1.3B model**
  - Training LoRA for 14B model would cost 10x more, so depth LoRA is limited to 1.3B variant
  - *From: David Snow*

- **Native VRAM management issues at low resolutions**
  - At 512x512 or lower, ComfyUI retains 4.5-5GB excess VRAM that's never released until manual unload
  - *From: Screeb*

- **FP16 T5 encoder breaks with I2V**
  - FP16 T5 encoder causes issues with I2V workflows, works fine for T2V
  - *From: IllumiReptilien*

- **Prompt conditioning weaker with start/end frame I2V**
  - Prompt travel and conditioning appears to have reduced effectiveness when using start/end frame I2V
  - *From: Kijai*

- **CFG Zero Star zero init ruins I2V completely**
  - Produces corrupted output when zero init enabled for image-to-video
  - *From: Kijai*

- **CFG Zero Star doesn't work with all samplers**
  - Compatibility issues with certain samplers, works best with euler/normal
  - *From: Kijai*

- **SLG in native doesn't work same with 1.3B**
  - CFG is done batched so need to limit the range
  - *From: Kijai*

- **Multiple unet wrappers get complicated**
  - Patching system makes it complex when different wrappers want to skip different things
  - *From: Kijai*

- **HuggingFace space limited to 512px resolution and 29 frames**
  - Testing environment has significant resolution and frame count restrictions
  - *From: David Snow*

- **Control LoRAs don't work with Fun Control models**
  - Incompatibility between old control loras and new Fun architecture
  - *From: Kijai*

- **SLG node incompatible with InP models**
  - Cannot use SLG enhancement with the new InP models
  - *From: JmySff*

- **Official demo limited to 29 frames**
  - Their demo interface restricts generation to 29 frames
  - *From: Kijai*

- **Old LoRAs don't work well with control models**
  - Model compatibility issues, even at high strength (2.0+) they don't work properly
  - *From: Kijai*

- **1.3B InP model has quality issues**
  - Generally produces worse results compared to 14B version
  - *From: Excai*

- **TeaCache may not work well with control models**
  - Suspect it might not work well with the same coefficients as other models
  - *From: Kijai*

- **Fun models have concept limitations**
  - 1.3B fun model is devoid of some concepts that 14B implements, struggles with complex or esoteric concepts compared to generic content
  - *From: miko*

- **Context windows don't work with control models yet**
  - Getting tensor mismatch error when trying to use context windows with control models
  - *From: Zuko*

- **Control + end frame incompatible**
  - Cannot use control and end frame together currently
  - *From: Eclipse*

- **29 frame limit on official demo**
  - Official HuggingFace demo limited to 29 frames, possibly not just due to compute constraints
  - *From: Kijai*

- **LoRAs work but are weak with Fun models**
  - LoRA trained on wan works but very weak and lazy for i2v
  - *From: Mngbg*

- **Euler sampler not working**
  - Euler sampler causes errors in WanVideo sampler
  - *From: seitanism*

- **Control model doesn't work with end frames**
  - End frame input either doesn't work or ruins the generation by going white
  - *From: Kijai*

- **1.3B Fun InP produces bad motion**
  - The 1.3B InP model generates unnatural looking motion
  - *From: David Snow*

- **LoRA compatibility reduced with control models**
  - Existing LoRAs don't perform as well with Fun Control models
  - *From: Payuyi*

- **TeaCache causes jittery generations**
  - Using TeaCache can introduce jitter artifacts in video output
  - *From: Ira*

- **Control only works with first frame**
  - Despite attempts, control cannot be applied to end frames effectively
  - *From: Kijai*

- **Start and end frames change during generation**
  - Both start and end frames undergo modifications during generation, making smooth clip transitions difficult
  - *From: seitanism*

- **Face quality issues in full body shots**
  - Faces become awful in full body shots, particularly prominent with anime faces
  - *From: PolygenNoa*

- **LoRAs not compatible with Fun Control**
  - Fun Control models don't work with traditional LoRAs, though 14B model does support some LoRA usage
  - *From: NebSH*

- **Batch start frames don't work**
  - Using more than 1 start frame in a batch doesn't seem to work
  - *From: Kijai*

- **Fun models lose quality with fp16_fast**
  - Since released in bf16, fp16_fast conversion is lossy
  - *From: Kijai*

- **Cannot use end latent directly for next clip**
  - I2V encodes image + empty frames together, can't extract individual latent frames
  - *From: Kijai*

- **Context windows don't work well with control model and second image conditioning**
  - Errors occur when adding second image conditioning with context windows
  - *From: Zuko*

- **1-step generation produces blurry, grainy results**
  - Even at 4-5 steps, quality is poor except for very slow moving content
  - *From: artemonary*

- **Wan doesn't understand panning well**
  - Big gap in training data, doesn't want to pan unless it's orbit motion around character
  - *From: ArtOfficial*

- **LoRAs for stock don't work for Fun**
  - Stock model LoRAs are incompatible with Fun models
  - *From: Benjimon*

- **81 frames max without riflex**
  - Won't see good results at 169 frames, 81 is max without riflex
  - *From: DawnII*

- **Extending from frame has motion kinks**
  - Will have kink in motion, doesn't work if character doesn't face forward perfectly
  - *From: aikitoria*

- **Control model 1.3B can't train on diffuse pipe**
  - Fun control model considered I2V so can't train with standard diffuse pipe
  - *From: TimHannan*

- **OptimalSteps method misleading**
  - Need to generate 50 step version first to optimize for 20 steps, making it worse than useless
  - *From: spacepxl*

- **Wan models cannot do video extension**
  - Only LTXV and Cosmos are open models with video extension capability
  - *From: Kijai*

- **Short video generation affects coherence**
  - Going away from default frame amount causes issues, especially for i2v. Coherence decreases when generating shorter videos
  - *From: Draken*

- **First and last frames ignored in short generations**
  - When generating videos with lower frame counts, start and end frames are practically ignored when trying img2vid
  - *From: PirateWolf*

- **1080p generation very slow with quality issues**
  - Tiled VAE encode/decode messes with quality, tiled encode being much worse than decode. Browser-based ComfyUI hates 1080p for VHS combine
  - *From: aikitoria*

- **Control models perform worse than promised**
  - Control functionality not as good as what was promised (and never delivered) for HunyuanVideo
  - *From: aikitoria*

- **Temporal masking only supports binary masks**
  - Cannot fade masks, only binary on/off per 4-frame groups
  - *From: Kijai*

- **14B model seems undercooked compared to 1.3B**
  - Speculation that 14B model is harder to train and may need more compute
  - *From: Piblarg*

- **Tiled encoding doesn't work well with Wan**
  - Results in strange/wrong motion despite looking correct, math at tile edges may be incorrect
  - *From: aikitoria*

- **Video-T1 test-time scaling doesn't apply to Wan**
  - Wan is not autoregressive so tree of frame search approach doesn't work
  - *From: aikitoria*

- **Camera prompts don't work**
  - Camera controls mentioned in prompting guide are not functional
  - *From: N0NSens*

- **VAE degradation with low FPS**
  - Lot of degradation from VAE if frames are slower than usual 16 fps, even with simple zoom operations
  - *From: mamad8*

- **1.3B interpolation poor without intermediary frames**
  - First frame + last frame with 1.3B-Inp model didn't get good results without intermediary frames
  - *From: mamad8*

- **FlowEdit compatibility issues**
  - FlowEdit doesn't work with unipc, and fixing Euler scheduler broke flowedit functionality
  - *From: Kijai*

- **LoRAs only for 1.3B model**
  - The new highres and aesthetics LoRAs only work with 1.3B, not 14B
  - *From: David Snow*


## Hardware Requirements

- **VRAM for 1.3B model context window**
  - 257 frames with 1.3B model used under 5GB VRAM (Max reserved: 4.844 GB)
  - *From: Kijai*

- **RTX cards heat issues**
  - RTX cards have heat-related stability problems during long renders
  - *From: deleted_user_2ca1923442ba*

- **3080ti with 40 block swap**
  - 3080ti needs significant block swapping for larger models
  - *From: VRGameDevGirl84(RTX 5090)*

- **PyTorch 2.7.0 nightly**
  - Required for FP16 accumulate feature
  - *From: Kijai*

- **VRAM for VEnhancer**
  - Takes up to 48GB VRAM on H200 for 832x480 video, very slow
  - *From: Janosch Simon*

- **RAM issues with infinite looping**
  - ComfyUI shuts down after 2 iterations due to running out of RAM
  - *From: AJO*

- **GPU compatibility for fp16 accumulation**
  - Available on Volta+ GPUs (compute capability 7.0+), works on RTX cards
  - *From: Kijai*

- **VRAM for 17GB models**
  - User with 16GB VRAM unable to run full models
  - *From: N0NSens*

- **PyTorch 2.6.0 minimum**
  - Required for Windows torch compile fix, 2.4.1 minimum for other features
  - *From: Kijai*

- **5090 performance**
  - Model runs pretty well on RTX 5090
  - *From: comfy*

- **Wan 1.3B minimum VRAM**
  - Can go as low as 8GB VRAM
  - *From: David Snow*

- **Wan 14B bf16 GGUF VRAM**
  - Fits in 32GB VRAM
  - *From: Shawneau 🍁 [CA]*

- **VAE decoding 1024 frames**
  - Uses much less VRAM than Hunyuan VAE, doesn't need tiling
  - *From: Kijai*

- **1025 frames at 512x512**
  - Decoding took 16GB without spatial tiling
  - *From: Kijai*

- **CUDA driver compatibility**
  - 570.124.04 driver with CUDA 12.8 works on Ubuntu 24.04
  - *From: fredbliss*

- **VRAM usage with TeaCache**
  - Using only 2.4 GB VRAM for 81 frames 480x256, 30 steps just 8 minutes on RTX 3060 with TeaCache
  - *From: VK*

- **Wrapper vs Native memory usage**
  - Wrapper causes OOM for some users while Native works fine, even with block swap enabled
  - *From: Miku*

- **RAM for block swapping**
  - 16GB RAM insufficient for offloading, causes OOM errors. 64GB suggested for T5 text encoder
  - *From: Kijai*

- **VRAM for TeaCache**
  - Adds 12-13% VRAM overhead when active
  - *From: DevouredBeef*

- **VRAM for text encoders**
  - bf16 text encoder uses 8GB VRAM, fp8 quantization saves ~4GB
  - *From: Googol*

- **Generation times**
  - I2V 21 frames in 6 minutes on 5080, 720p 81 frames in 17 minutes
  - *From: VK*

- **RTX 3090 performance**
  - 1200 sec for 16sec video at 832*480 using 3B model, works great overall
  - *From: NebSH*

- **RTX 4090 vs 3090 speed difference**
  - T2V example takes around 5 mins on 4090, should be about 10 mins on 3090
  - *From: Kijai*

- **VRAM usage optimization**
  - Native implementation uses less memory than wrapper, 14B models use same VRAM regardless of 480p vs 720p
  - *From: Kijai*

- **fp16 accumulation GPU support**
  - Works on compute level 7.0 minimum, should work fine on 4090 and 3090 (compute 8.6)
  - *From: Kijai*

- **VRAM for 81 frames 720×1280**
  - 31GB VRAM needed even with fp8, requires block swap on 24GB cards
  - *From: Shawneau 🍁 [CA]*

- **480p I2V model**
  - Fits in 8GB VRAM when tested, but takes a lot of RAM and is slow
  - *From: Kijai*

- **VAE decode 1000 frames**
  - Under 16GB VRAM - VAE is light compared to main model
  - *From: Kijai*

- **1440×1440 generation on 4090 24GB**
  - Won't OOM with proper settings, generation time about 50 minutes
  - *From: BNP4535353*

- **Torch version**
  - Minimum 2.6.0 recommended, fp16_fast requires 2.7.0.dev20250226+cu128 or newer
  - *From: Kijai*

- **VRAM for different context settings**
  - Low VRAM: 41 frames/8 overlap, Balanced: 81 frames/16 overlap, High quality: 121 frames/24 overlap
  - *From: fredbliss*

- **Frame interpolation performance**
  - Can double 97 frames at 1280x1962 in 3 seconds on 4080 16GB
  - *From: Monster*

- **TeaCache timing comparison**
  - 20 samples: 240s, 60 samples: 660s, 20 samples teacache: 167s, 60 samples teacache: 227s
  - *From: David Snow*

- **RAM for I2V 14B model**
  - Minimum 64GB RAM required, 32GB insufficient. 96GB recommended for comfortable use
  - *From: cyncratic*

- **VRAM for 14B training**
  - 24GB VRAM sufficient for LoRA training on 14B model with offloading, 28GB+ needed for full inference
  - *From: Shawneau 🍁 [CA]*

- **1.3B model efficiency**
  - Only uses 5.2GB VRAM, very efficient compared to 14B model
  - *From: Benjimon*

- **4090 48GB availability**
  - Available for $3.2k USD in China, $4.2k in US, same speed as regular 4090, limited to 450 watts
  - *From: Benjimon*

- **Multi-GPU setup**
  - 29 s/it using 4x3090ti when generating at 1280x720x81f with 14B model
  - *From: intervitens*

- **VRAM for 14B model**
  - Cannot run 14B T2V model with max offload on 16GB VRAM
  - *From: Cseti*

- **PyTorch version**
  - Requires PyTorch 2.7.0 nightly for fp16 accumulation
  - *From: Kijai*

- **Performance improvement**
  - Down from ~37s/it to ~14s/it with optimized workflow
  - *From: Organoids*

- **RAM usage for looping**
  - 8 iteration loop used 98% of 76GB RAM plus 64GB swap
  - *From: AJO*

- **Speed improvement with TeaCache**
  - Improved from 12s/it to 4.76s/it on RTX 3090
  - *From: ˗ˏˋ⚡ˎˊ-*

- **fp8 14B model block size**
  - Around 350MB per block in fp8
  - *From: Kijai*

- **fp8 480p default resolution**
  - Under 10GB VRAM requirement
  - *From: Kijai*

- **TeaCache performance on 3090**
  - 50s generation time with teacache
  - *From: ˗ˏˋ⚡ˎˊ-*

- **TeaCache speedup on 12GB setup**
  - Reduced from 950s to 744s (15min to 12min)
  - *From: Ashtar*

- **3080ti 12GB workflow performance**
  - 848x480, 269 frames (9 seconds) takes about 1+ hour with SageAttention issues
  - *From: Teslanaut*

- **5090 performance for long context**
  - 513 frames took 51 minutes (102.31s per step) on RTX 5090
  - *From: Kijai*

- **RTX 3060 12GB capability**
  - Can run 90 frame videos with fp8, sageAttention, TeaCache, BlockSwap optimizations
  - *From: Ashtar*

- **Context generation memory usage**
  - 8 loops (40 seconds) needs about 76GB RAM
  - *From: AJO*

- **VRAM for long context**
  - Sliding context helps manage VRAM by only processing context_length frames at a time, avoiding full-length VRAM requirements
  - *From: Draken*

- **4090 RTX performance**
  - I2V generation at 720x1024 for 81 frames takes about 20 minutes with TeaCache, 45 minutes without
  - *From: Bleedy (Madham)*

- **5090 RTX for higher resolutions**
  - Can't go past 720x480 without OOM on current setups, 5090 needed for higher resolution processing
  - *From: VRGameDevGirl84(RTX 5090)*

- **A4500 performance**
  - 24GB VRAM + 28GB RAM, approximately 11 minutes per generation
  - *From: The Shadow (NYC)*

- **3060 long generation**
  - 245 frames took 15 minutes on RTX 3060 using LoRA
  - *From: VK (5080 128gb)*

- **RTX 4090 performance**
  - 20% speed increase with PyTorch nightly fp16 accumulation
  - *From: Kijai*

- **RTX 3060 performance**
  - Some speed improvement with fast fp16 accumulation (21min vs 23min for 93 frames)
  - *From: Ashtar*

- **VRAM for 24GB cards**
  - Discussion of optimal settings for 24GB VRAM cards
  - *From: Relven 96gb*

- **ComfyUI memory usage**
  - Images cached in fp32 always, takes a lot of RAM when working with video
  - *From: Kijai*

- **FP8 i2v model VRAM usage**
  - 32GB VRAM needs about 10 blocks swapped for 720x1280 at 81 frames
  - *From: Shawneau 🍁 [CA]*

- **300+ frame generation on 4090**
  - Possible but slow, tested with experimental FPS interpolation
  - *From: fredbliss*

- **96GB RAM usage**
  - New 96GB kit at 6400 cl28 gets filled to brim when using both Wan and Hunyuan models
  - *From: seitanism*

- **VRAM usage with frame counts**
  - 4070 12GB VRAM: 33 frames uses 70% VRAM, 102 frames hits 98% and freezes at 720x480
  - *From: for1096*

- **fp8_e4m3fn compilation**
  - Requires RTX 4000 series and up, RTX 3090 not supported
  - *From: Kijai*

- **14B model OOM on RTX 4090**
  - fp16 14B model OOMs even with 40 block swap on RTX 4090, fp8 quantization required
  - *From: Juampab12*

- **RTX 4090 performance**
  - Generation of 201 frames at 832x480 took 982.90 seconds total (823.71s generation, 133.51s VAE decoding)
  - *From: fredbliss*

- **VRAM for 720p generation**
  - 720p generation at 720x720 causes OOM on 5090 with wrapper, but works with native using GGUF8 model
  - *From: AJO*

- **High VRAM optimization**
  - With 48GB+ VRAM, disable block swap and set TeaCache to GPU for better performance
  - *From: Draken*

- **VRAM for different resolutions**
  - 4080 can handle standard loads, 4090 with 48GB can run bf16 720p, regular 4090 cannot load bf16 720p
  - *From: maitr3ya*

- **RAM usage in multi-scene workflows**
  - RAM can reach 98% during complex workflows with multiple scene generations, GGUF helps reduce usage
  - *From: AJO*

- **Performance benchmarks**
  - 312 frames at 960x544 with TeaCache, 30 steps, GGUF Q8 on RTX4090: 28 minutes. 81 frames 720p native: 1000 seconds
  - *From: JmySff*

- **3090 cannot run BF16 model**
  - As a 3090 haver, not a chance on bf16
  - *From: Benjaminimal*

- **3080 12gb can run 14B model with block swapping**
  - Able to use Wan2_1-T2V-14B_fp8_e4m3fn.safetensors with block swapping enabled, uses more than 40 gigs of system ram
  - *From: garbus*

- **32GB VRAM needs 5 block swap for 720p**
  - To do 81 seconds at 720P resolution still need to swap five blocks even with 32GB VRAM
  - *From: Shawneau 🍁 [CA]*

- **fp8 speed limitations on older GPUs**
  - We cant take advantage of fp8 for speed gains, we dont have any fp8 cores, our gpu has to upcast
  - *From: Benjaminimal*

- **3090 timing for 120 frames**
  - 1½ hours on 3090 for 120f at 1152x512, 50 steps
  - *From: Benjaminimal*

- **3090 timing for 81 frames**
  - ~15 minutes for 81F@720p on 3090 using 14B model
  - *From: jellybean5361*

- **Multi-GPU memory usage**
  - 24GB VRAM recommended if offloading encoder and clip with FP8 versions
  - *From: jellybean5361*

- **Hunyuan I2V VRAM**
  - 20GB VRAM used for 848x480, OOM when using VAE tiled encoder
  - *From: slmonker(5090D 32GB)*

- **A6000 performance issue**
  - A6000 48GB taking 1.5-2 hours, significantly slower than expected
  - *From: Gateway {Dreaming Computers}*

- **WSL2 RAM for Wan**
  - Must configure for 48GB+ RAM or VAE decode will fail, commits over 32GB during processing
  - *From: jellybean5361*

- **Multi-GPU Wan VRAM optimization target**
  - Keep under 23GB VRAM usage by adjusting BlockSwap settings
  - *From: jellybean5361*

- **Mistral Large FP8 + context**
  - Fully utilizes 8x 4090 GPUs (24GB each)
  - *From: aikitoria*

- **High-end setup power consumption**
  - 9x 4090 setup draws 4kW (described as half the power of sauna stove), significant room heating
  - *From: aikitoria*

- **VRAM for higher resolution**
  - Significantly higher resolution will OOM on VAE decode, tiled VAE needed
  - *From: intervitens*

- **WSL file access speed**
  - Loading Windows files from WSL2 is very slow, 1/10 normal speed
  - *From: jellybean5361*

- **Long video generation time**
  - 1025 frames at 30 steps took 72 minutes
  - *From: Uehreka*

- **Training limitations for large models**
  - Need gradient checkpointing and quantization to train models larger than 1.3B
  - *From: spacepxl*

- **32GB VRAM still needs 5 block offload**
  - Even with 32GB VRAM, need to offload 5 blocks for 720P, 81 frames I2V using fp8
  - *From: Shawneau 🍁 [CA]*

- **24GB VRAM max resolution**
  - 832x832 for 81 frames achievable with 24GB VRAM, 32GB RAM, 20 block swap
  - *From: zoz*

- **4060 16GB performance**
  - 20 minutes generation time on 4060 16GB
  - *From: shockgun*

- **3060 12GB with GGUF**
  - RTX 3060 12GB can work with GGUF quantization, user wishes for 5090
  - *From: Ashtar*

- **RAM limitation with block swap**
  - 32GB RAM may not be enough for higher block swap values, limited by RAM not VRAM
  - *From: Kijai*

- **Multi-GPU performance**
  - 10 minutes on 4x4090s for single video generation
  - *From: aikitoria*

- **14B model on 3060 12GB**
  - Too slow, better to use 1.3B model
  - *From: ArcherEmiya*

- **1280x720 generation**
  - Possible on 4090 with native, OOMs with wrapper even with 40 block swap
  - *From: zoz*

- **325 frames 14B T2V**
  - Takes 4156.25 seconds vs 700 seconds for 1.3B
  - *From: Organoids*

- **24GB VRAM for 720p model**
  - Difficulty fitting 720p model workflows in 24GB VRAM
  - *From: Neex*

- **4090 performance**
  - 832x480x81f, 20 steps: ~12 mins with optimizations, 17 mins without
  - *From: Benjimon*

- **4080 performance**
  - 832x480x81f, 20 steps: ~5 minutes
  - *From: N0NSens*

- **Multi-GPU setup heat**
  - 4kW heat output from 4x 4090 setup
  - *From: aikitoria*

- **VRAM savings on Linux**
  - ~1.5GB VRAM saved vs Windows due to less system bloat
  - *From: Colin*

- **VRAM for different model sizes**
  - Full model is 60GB, bf16 is 30GB, fp16 is faster and higher quality than bf16
  - *From: seitanism*

- **Multi-GPU scaling**
  - 4 GPUs optimal, 8 GPUs same speed as 4, 2 GPUs doesn't fit, 3 GPUs much slower than 4 probably due to uneven NCCL
  - *From: aikitoria*

- **RAM for block swapping**
  - Need 256GB normal RAM when using block swapping due to weight offloading on every step
  - *From: Benjimon*

- **Generation times**
  - I2V 720p 5 seconds: ~10min on 4090, ~20min on 3090. A6000 much slower at ~1 hour
  - *From: Benjimon*

- **14B model VRAM usage**
  - Max allocated memory: 3.609 GB, Max reserved: 5.000 GB for 832x480, 81 frames on 3090
  - *From: burgstall*

- **Multi-GPU training setup**
  - X99 motherboard with 40 PCIe lanes, 1500W PSU recommended for dual 4090s
  - *From: Benjimon*

- **High-res training memory**
  - 720x720x128 frames possible on 2x RTX 6000 Ada 48GB, 4x 4090 can do 720x720 but 800x800 causes OOM
  - *From: Benjimon*

- **VRAM for 1280x720x81**
  - Requires blockswapping on 5090 (24GB), uses ~27GB peak allocation
  - *From: seitanism*

- **RAM usage**
  - 14B model uses 86-96GB RAM with blockswapping
  - *From: seitanism*

- **Performance**
  - 4090: 68s/it with blockswap, 5090: 44-50s/it, FP8 on 4090: 38s/it
  - *From: Benjimon*

- **Power consumption**
  - 5090 peaks at 575W, can cause thermal issues reaching 100°C VRAM temps
  - *From: seitanism*

- **3090 performance benchmark**
  - 65 frames at 496x512, 20 steps: 13.05s/it with optimizations (e5m2, TeaCache 0.4, 10 block swap)
  - *From: BestWind*

- **4090 performance benchmark**
  - 30 steps at 544x544x81 in 3 minutes, 69 frames around 4 minutes
  - *From: Kijai*

- **3090 I2V performance with optimizations**
  - 960x480x33 at 20 steps: 17s/it native, 14s/it with compile+sage, 9s/it with teacache
  - *From: ˗ˏˋ⚡ˎˊ-*

- **RAM requirements**
  - 64GB RAM allows block swap of 30, 32GB RAM limited to lower values
  - *From: BestWind*

- **VRAM usage**
  - 544x544x81 uses only 20GB VRAM with 10 blocks swapped on 4090
  - *From: Kijai*

- **VRAM capping causes extreme slowdowns**
  - 18 minutes vs 3 minutes when VRAM is capped with wrapper vs native
  - *From: N0NSens*

- **2x24GB GPU setup for tiled VAE**
  - Can run on 2x24GB GPUs with tiled VAE but no overall speed gain, 2x GPUs run almost 2x slower than 4x
  - *From: intervitens*

- **3090 compatibility**
  - SageAttention 2 designed for 3090, E5M2 model type necessary for 3000 series with torch.compile
  - *From: Juampab12*

- **1.3B model performance**
  - Described as runnable on 'smart toaster' with 8GB VRAM, very accessible
  - *From: Kijai*

- **LoRA training**
  - 31 hours on single 3090 for 50k videos
  - *From: spacepxl*

- **14B model training**
  - Requires serious compute, no one will be cooking LoRA on home GPU
  - *From: aikitoria*

- **12GB VRAM availability**
  - User has 12GB free while training
  - *From: Juampab12*

- **1280x720x81 on 4090**
  - Works with 24GB VRAM, needs fp8 model and 32GB+ RAM, block swap 25, ~10.5 min for 20 steps
  - *From: zoz*

- **1280x720x81 on 3090**
  - 800-1000 seconds for 81 frames, requires significant block swapping
  - *From: Organoids*

- **640x480 on RTX 3060**
  - 18 minutes for 85 frames with 12GB VRAM + 64GB RAM, BlockSwap=30, fp8 model
  - *From: Ashtar*

- **RAM usage for block swap**
  - Can use up to 81GB RAM on Windows, very inefficient for 32GB systems
  - *From: seitanism*

- **5090 performance**
  - More than 3x performance of 3090 with barely more power draw for AI workloads
  - *From: spacepxl*

- **960x960x81 with LoRA and compile**
  - Uses only 15GB VRAM but may offload too much
  - *From: Kijai*

- **1280x720x81 fp8 needs reserves**
  - 4090 needs --reserve-vram 3-4 to avoid OOM with torch compile + LoRA
  - *From: Kijai*

- **3090 optimization**
  - Can reach 1995MHz at 107% power limit, 80% limit gives 1790-1820MHz range
  - *From: HeadOfOliver*

- **WAN 480p I2V with optimizations**
  - 15GB VRAM for 960x960x81 frames, couple minutes with 4090
  - *From: Kijai*

- **WAN on 3090**
  - 409 seconds for 81 frames with FETA/TeaCache/upscale image
  - *From: NebSH*

- **24GB VRAM still gets OOM**
  - Even 24GB can OOM on 33 frames at 480x832 without proper settings
  - *From: CJ*

- **16GB + 128GB RAM**
  - Can run 480p I2V with wrapper VRAM management at 0.76
  - *From: Colin*

- **RAM for 14B training**
  - Requires significant RAM and gradient checkpointing, 20x slower than 1.3B on 32GB setup
  - *From: Kijai*

- **TeaCache memory overhead**
  - Causes 2GB memory spike even with offload_device enabled
  - *From: garbus*

- **Memory for generation**
  - 64GB RAM should be sufficient but Windows memory management can cause issues
  - *From: Kijai*

- **Training hardware comparison**
  - 8xH100 setup: 1.3B at 832x480x81 = 59s/100 steps, 14B at 1280x720x49 = 10:31/100 steps
  - *From: Benjaminimal*

- **832x480 I2V with LoRA 81 frames**
  - Needs block_swap on 24GB VRAM, right on the edge without it
  - *From: Kijai*

- **Dual LoRA workflow**
  - Needs 128GB RAM to hold two models, or block_swap=40 on 24GB VRAM
  - *From: burgstall*

- **Consumer GPU kernel optimization**
  - Less effective than datacenter due to compute capacity ceiling getting hit easier on 4090/5090
  - *From: deleted_user_2ca1923442ba*

- **RTX 4090 VRAM usage**
  - Can run at ~11GB with proper block swap settings, fp16 model precision recommended
  - *From: fredbliss*

- **16GB VRAM optimal settings**
  - 25 blocks for wrapper gives 4:05 generation time, 30 blocks too slow, 10 blocks causes memory issues
  - *From: N0NSens*

- **Generation times**
  - Native: 640x352/81 frames takes 2:30. Wrapper with 25 blocks: 3:50-4:05. Full quality tests: ~5 minutes
  - *From: N0NSens*

- **VRAM usage with block swap**
  - System showing 12.9+11.4 = 24.4GB usage when block swaps enabled, appears in shared memory
  - *From: mamad8*

- **A100 80GB performance**
  - 1280x720x81 at 40 steps: 42min without optimizations, 17min with torch+teacache, 12min with updated teacache
  - *From: HeadOfOliver*

- **4080 performance with control lora**
  - 7 minutes generation time for control lora upscaling workflow
  - *From: ramonguthrie*

- **8GB GPU needs special configuration**
  - Requires --lowvram flag, shorter frames, smaller video size, and possibly 1.3B model
  - *From: Kijai*

- **Monitor usage affects performance**
  - Using monitor vs RDP on Windows causes slowdown due to VRAM threshold when opening browser
  - *From: Kijai*

- **Triton installation for SageAttention**
  - SageAttention requires Triton, but now easier to install with pre-built Windows wheels
  - *From: kendrick*

- **4x 3090 not enough for fp16 without modifications**
  - Official Wan repo needed hacking to fit fp16 model on 4x 3090 setup
  - *From: Doctor Shotgun*

- **RTX 3060 as minimal GPU**
  - Used RTX 3060 considered baseline minimal GPU for current AI video work
  - *From: deleted_user_2ca1923442ba*

- **1280x768x81 possible on 24GB**
  - Can do 1280x768x81 resolution easy with fp8 on 24GB, fp16 uncertain
  - *From: Kijai*

- **~11GB VRAM for 720p fp16**
  - 720p fp16 uses around 11GB VRAM with full offloading on single 4090
  - *From: Kijai*

- **Turing architecture poor for video generation**
  - RTX 2080Ti/Turing struggles significantly with video generation workloads
  - *From: Benjimon*

- **RAM for 14B fp16 model**
  - ~30GB RAM needed for fp16 model plus text encoder overhead
  - *From: Kijai*

- **720p 81 frames VRAM usage**
  - All blocks swapped: ~12GB VRAM, 27/40 blocks: ~22GB VRAM
  - *From: Kijai*

- **Frame limits by hardware**
  - RTX 4090 + 64GB RAM: 101/105 frames native, 97 frames wrapper at 960x544
  - *From: JmySff*

- **FloweEdit render time**
  - RTX 4060: ~40 minutes for FloweEdit workflow
  - *From: yukass*

- **Long video generation performance**
  - 245 frames at 480P I2V took 5 hours on RTX 4090 with 81 overlap
  - *From: Cubey*

- **A100 96GB performance**
  - 140.59 seconds for text to video generation
  - *From: VRGameDevGirl84(RTX 5090)*

- **LoRA memory usage**
  - LoRAs require slightly more memory, reduce frames or resolution if crashing
  - *From: Screeb*

- **Torch compile VRAM impact**
  - Can reduce VRAM usage by ~30% in addition to speed improvements
  - *From: Kijai*

- **RAM detection in WSL**
  - WSL may not detect newly installed RAM without .wslconfig configuration file
  - *From: Question*

- **4090 i2v memory usage**
  - Can fill 64GB RAM during i2v generation, needs fp8 quantization and optimized loaders
  - *From: Kijai*

- **L40 48GB VRAM with block swap**
  - Needs block swap set to 20 or lower to prevent CPU memory overflow
  - *From: Kijai*

- **Step-Video-TI2V GPU requirements**
  - Requires more than 4 GPUs for practical use
  - *From: JohnDopamine*

- **fp16_acc support**
  - 3090 may not support fp16_acc optimization
  - *From: Cubey*

- **4090 T2V performance**
  - 720x1280x81f: 38 s/it regular fp8, 48 s/it scaled fp8, 82 s/it with enhance-a-video
  - *From: Doctor Shotgun*

- **VRAM for fp16 model**
  - fp16 weights alone exceed 4090 VRAM, requires offloading
  - *From: Doctor Shotgun*

- **VRAM management for I2V 480**
  - Use block swap starting at max 40, reduce if unused VRAM available. 4090 users experiencing OOM with torch compile on 33 frames at 1280x720
  - *From: Kijai*

- **CUDA version compatibility**
  - CUDA 12.8 needed for Blackwell GPUs but not required for Sage Attention 2 in general. Driver version must support target CUDA toolkit version
  - *From: Kijai*

- **14B model at 720p x 81f**
  - 22.43GB VRAM with 32 blocks swapped
  - *From: Benjimon*

- **RTX 5090 Triton compatibility**
  - Requires WSL Ubuntu setup for proper installation
  - *From: Relven 96gb*

- **3080ti performance with LoRA**
  - 130 seconds for video generation at 10 steps
  - *From: VRGameDevGirl84(RTX 5090)*

- **1024x720 with 1.3B model**
  - 449.42 seconds execution time on RTX 5090
  - *From: VRGameDevGirl84(RTX 5090)*

- **Multi-GPU setup**
  - 4x 4090s optimal for fast inference, more GPUs don't help due to data transfer overhead
  - *From: aikitoria*

- **1.3B model VRAM**
  - Can run on potato - very low VRAM requirements
  - *From: Kijai*

- **14B model VRAM/RAM**
  - Requires quite a bit of VRAM/RAM depending on frame count/resolution expectations
  - *From: Kijai*

- **4090 with fp8**
  - fp8 e4m3fn runs fine on 4090 with 128GB RAM
  - *From: Siraj*

- **Memory for 14B fp16**
  - 14B fp16 model fits in 48GB VRAM but runs at 114 s/it
  - *From: Doctor Shotgun*

- **VRAM for 1280x768x81 i2v**
  - 11GB VRAM possible with sufficient RAM (64GB recommended)
  - *From: Kijai*

- **1.3b model inference speed**
  - 20-30 seconds for 81 frames with 4090, compile, sage, TeaCache, fp16_fast
  - *From: Kijai*

- **Speed improvements**
  - fp16_fast gives ~20% boost, torch.compile gives ~30% boost
  - *From: Kijai*

- **Wan 1.3B VRAM**
  - Works on 8GB cards
  - *From: xwsswww*

- **3090 performance with speedups**
  - 5-8 s/it for 480p 81 frames
  - *From: LarpsAI*

- **5090 vs 4090**
  - 5090 is 40%+ faster, more memory allows less offloading
  - *From: Kijai*

- **ComfyUI version**
  - Need nightly version for latest depth control features
  - *From: Kijai*

- **5090 performance**
  - 7 minutes to generate video without teacache, 2:35 for 81 frames at 480x832 with 20 steps (7.79s/it)
  - *From: const username = undefined;*

- **Virtual memory issues**
  - Python.exe consuming 74GB virtual memory can cause system crashes
  - *From: TK_999*

- **704x1024 performance**
  - 5min 31.5s/it for 81 frames, 15 steps on high-end system
  - *From: Relven 96gb*

- **VRAM usage with RAM upgrade**
  - 32GB RAM used 100% VRAM, 64GB RAM reduced to 86% VRAM and slowed generation
  - *From: shockgun*

- **L40S performance**
  - 48GB VRAM, about 11 minutes for 49 frames I2V at 1280x720 with optimizations
  - *From: mamad8*

- **4090 performance full quality**
  - About 1 hour per generation at 720p with 50 steps, no optimizations except block swap
  - *From: Benjimon*

- **PCIe lane requirements**
  - 8x PCIe vs 16x PCIe shows almost no performance difference for block swapping
  - *From: Benjimon*

- **Memory type impact**
  - DDR5 vs DDR4 has no effect on generation speed
  - *From: Benjimon*

- **5090 performance**
  - 20 s/it on 856x480 16 Steps 81 Frames with GGUF 8
  - *From: AJO*

- **RTX 5090 performance**
  - 10-second 165 frames video takes ~10 minutes with 10 block swap, temps around 71°C, under 500 watts
  - *From: const username = undefined*

- **FP32 model memory usage**
  - At 960x768 with 38 block swap: 93GB RAM, 16GB VRAM, 63s/it
  - *From: Benjimon*

- **24GB VRAM recommendations**
  - Can use fp8 quantized models, full block swap fp32 might work with sufficient RAM
  - *From: Kijai*

- **Windows VRAM usage**
  - Windows uses ~0.2GB VRAM when properly configured, but average over time can be higher with monitors/apps
  - *From: Benjimon*

- **4090 VRAM usage at 720p**
  - Extremely slow at 720p - 500s/it, 35+ minutes generation time, uses significant VRAM
  - *From: Benjimon/Ghost*

- **1.3B vs 14B model speed**
  - 1.3B model takes about 20 minutes for two-sampler workflow on 4090
  - *From: Flipping Sigmas*

- **3060 with optimizations**
  - Can run with Block Swap, Sage, and Triton but takes 30 minutes to 1 hour
  - *From: Dream Making*

- **Memory management**
  - Need to close background applications like YouTube on Windows to avoid OOM
  - *From: Ghost*

- **VRAM usage with fp8 I2V model**
  - ~12GB VRAM at 720p with 81 frames using full offloading
  - *From: Kijai*

- **4090 720p capability**
  - Can run 720p with block swap set to 32-34
  - *From: Benjimon*

- **RAM usage on 12GB GPU**
  - Using 27 of 48 regular RAM, CLIP unloaded before sampling
  - *From: VK (5080 128gb)*

- **Virtual memory importance**
  - Zero virtual memory can cause OOM errors even with 64GB RAM
  - *From: Juampab12*

- **VRAM for 81 frames 720p i2v**
  - Should fit 32GB with compile, easily fits 48GB, uses ~28GB with proper settings
  - *From: Kijai/Shawneau*

- **4090 speed benchmark**
  - 1280x720x81 for 20 steps with 22 blocks swapped in 9:30 with teacache, torch compile, slg
  - *From: zoz*

- **RAM requirements for block swap**
  - Need 64GB+ RAM to avoid performance issues with block swapping
  - *From: Obsolete*

- **14B model VRAM**
  - Can do 21 frames on 3060, but T2V requires more than I2V
  - *From: VK/Dream Making*

- **VRAM usage with native implementation**
  - Native 14B T2V uses 17.5GB at 640x640, but can spike to 21-22GB at lower resolutions due to memory management bug
  - *From: Screeb*

- **MultiGPU distribution**
  - Native implementation can distribute load: 7GB on second GPU, 12GB on main GPU for 14B model
  - *From: VK (5080 128gb)*

- **RAM speed impact**
  - Higher RAM speed does not provide meaningful performance improvement for generation
  - *From: Kijai*

- **For I2V 720p on 4090**
  - Preference between fp8 e4m3fn, fp8 scaled, or bf16 with block swap
  - *From: Persoon*

- **VRAM optimization**
  - fp8 e4 with fp16 fast works well
  - *From: Juampab12*

- **14B Fun models**
  - ~46GB in bf16 format, ~16GB when converted to fp8
  - *From: Kijai*

- **1.3B models**
  - Much faster inference, suitable for 4080 and similar GPUs
  - *From: yi*

- **1.3B model VRAM usage**
  - ~8GB VRAM required
  - *From: yi*

- **Generation speed with 1.3B**
  - About 30 seconds sampling time, couple minutes on RTX 4090
  - *From: Kijai*

- **5090 performance**
  - 1 minute without TeaCache, 44 seconds with TeaCache, complete workflow 2.5 minutes
  - *From: ArtOfficial*

- **14B model size**
  - 35GB for bf16 version
  - *From: ReDiff*

- **VRAM for high resolution encoding**
  - 2304x1536 resolution causes OOM errors, need bf16 VAE precision or tiled encoding
  - *From: mamad8*

- **1.3B model performance advantage**
  - 1.3B model doesn't take all day compared to larger models, significant speed improvement
  - *From: Kijai*

- **Power circuit limitations**
  - Starting to have problems with not having enough power circuits in apartment to fit all the GPUs
  - *From: aikitoria*

- **5070 performance**
  - 6 minutes generation time for standard workflow
  - *From: VK (5080 128gb)*

- **4090 comparison**
  - No blockswap vs 32 block swapping shows similar 66-67s/iteration performance
  - *From: Benjimon*

- **H100 performance**
  - 45-35s/iteration on 81 frames 720x1280 25 steps with 25% VRAM still free
  - *From: Ira*

- **4090 VRAM usage**
  - Running out of VRAM halfway through steps on 960x640 81f i2v, even with optimizations
  - *From: Persoon*

- **Minimum VRAM**
  - 12-16GB to start testing Wan models
  - *From: yukass*

- **5090 performance**
  - Few minutes generation time for Fun Control workflows
  - *From: 852話 (hakoniwa)*

- **4090 VRAM capacity**
  - Max 81 frames at 832x480 without offloading on RTX 4090
  - *From: Kijai*

- **Generation speed**
  - 32 frames of 480p video took 32 minutes on RTX 4080
  - *From: lostintranslation*

- **1-step generation performance**
  - 61 frames at 640x832 with 1 step: 12.60 seconds total, max 5.446GB VRAM allocated
  - *From: Kijai*

- **CUDA compute capability**
  - torch._scaled_mm requires compute capability >= 9.0 or 8.9, RTX 3090 not supported for fp8_fast
  - *From: Faux*

- **Replicate performance benchmark**
  - 40 seconds for 81 frames 480p 30 steps on 14B model, likely multiple GPUs
  - *From: Draken*

- **B100 performance vs 5090**
  - 10x faster in fp16 with fp32 accumulate, 5x faster in fp8 with fp16 accumulate
  - *From: aikitoria*

- **Memory bandwidth comparison**
  - DGX Spark has 0.27TB/s for 128GB vs 25x faster memory in 4x 5090 setup
  - *From: aikitoria*

- **VRAM requirements increase**
  - Recent update caused 8GB VRAM to no longer handle 81 frames, needs lower frame count
  - *From: Verevolf*

- **VRAM for 1024x1024x81**
  - ~10GB VRAM needed for 1.3B model at this resolution
  - *From: Kijai*

- **RAM for 14B model**
  - Usually around 45-55GB RAM usage
  - *From: DawnII*

- **4070 generation time**
  - 85 minutes for basic clip with 20 block swaps, 10 minutes with 30-40 swaps
  - *From: lomerio/DawnII*

- **I2V generation time on 5090**
  - 6-8 minutes for I2V generation
  - *From: ArtOfficial*

- **Recommended RAM**
  - At least 64GB, ideally 96GB for optimal performance
  - *From: DawnII/Benjimon*

- **1.3B model VRAM**
  - Model maxed out around 7GB when tested
  - *From: StableVibrations*

- **HiRes LoRA generation time**
  - 1024x1024 took 40 minutes, 20 steps took 7.5 minutes
  - *From: VK (5080 128gb)*

- **5B model VRAM usage**
  - Only takes 11GB VRAM to render at 1280x720 for 65 frames, pretty fast without teacache
  - *From: Kytra*

- **Training hardware for base model**
  - Using 8x H100s for training 5B parameter model from scaled weights
  - *From: Kytra*

- **TaylorSeer 14B model limitation**
  - Current TaylorSeer model cannot perform single-GPU inference for 14B models on A100 with 80GB memory
  - *From: Kijai*

- **16GB VRAM optimization**
  - Use 20 block swap to reduce usage to ~14.6GB, avoid running at 98% VRAM
  - *From: VK (5080 128gb)*

- **5090 vs 4090 performance**
  - 5090 shows 30-40% improvement over 4090 for Wan
  - *From: Kijai*

- **RTX 6000 Pro performance**
  - About 2/3 speed of H100, good for running new unoptimized models that require 80GB VRAM
  - *From: aikitoria*

- **4090 performance benchmark**
  - 270 seconds for 81 frames at 1280x720 without optimizations on undervolted 4090
  - *From: David Snow*

- **VRAM for hires LoRA**
  - At 2048x1024 with hires LoRA, VAE tiling was required
  - *From: Kijai*


## Community Creations

- **Enhance a video (feta) node** (node)
  - Provides significant quality improvements to generated videos
  - *From: David Snow*

- **WanVideoBlockSwap optimization** (node)
  - Memory management node requiring offload_txt_emb and offload_img_emb inputs
  - *From: Kijai*

- **VRAM debug node** (node)
  - Actually functional memory clearing tool in KJ nodes
  - *From: Colin*

- **DatasetHelper** (node)
  - ComfyUI node for dataset loading
  - *From: fredbliss*

- **TeaCache implementation for Wan Video Wrapper** (node)
  - Kijai's TeaCache implementation that provides ~50% speed improvement without polynomial coefficients
  - *From: Kijai*

- **Wan Cinematic Video Prompt Generator** (tool)
  - GPT assistant for creating prompts for Wan video generation
  - *From: VRGameDevGirl84*

- **FPS sampling nodes** (node)
  - Implements Apollo paper FPS sampling with context windowing for consistent temporal dynamics
  - *From: fredbliss*

- **Native text encoder bridge** (node)
  - Connects native ComfyUI text encoders to wrapper functionality
  - *From: Kijai*

- **Wan Jinx LoRA** (lora)
  - First attempt character LoRA for Wan model
  - *From: Cseti*

- **FPS sampling implementation** (workflow)
  - Apollo paper-based FPS sampling with latent interpolation for improved video generation
  - *From: fredbliss*

- **Multi-optimization workflow** (workflow)
  - Combined sageattention, torch.compile, fp16 accumulation, teacache, and adaptive guidance for low VRAM
  - *From: Miku*

- **Multi-GPU Wan implementation** (tool)
  - Custom implementation for multi-GPU use, still not optimized and clunky
  - *From: intervitens*

- **T5 model conversion script** (tool)
  - AI-generated script to convert Pile T5 model structure to work with Wan
  - *From: Juampab12*

- **MagicWan** (node)
  - Kijai's implementation that somewhat works but doesn't feel fully right
  - *From: Kijai*

- **WanVideoFPSSampler** (node)
  - Experimental FPS sampling implementation that inherits from WanVideoSampler
  - *From: fredbliss*

- **TeaCache for Wan native** (node)
  - Rewritten TeaCache implementation now available in KJNodes
  - *From: Kijai*

- **WanVideo TeaCache native** (node)
  - Native teacache implementation moved to KJNodes
  - *From: Kijai*

- **WanVideoTemporalEmphasis node** (node)
  - Controls emphasis on temporal vs spatial features with ROPE frequency adjustments
  - *From: fredbliss*

- **VRAM management node** (node)
  - Better memory management for low VRAM setups
  - *From: Kijai*

- **RifleX node for Wan** (node)
  - Made hunyuan riflex node, uncertain if works for Wan
  - *From: Kijai*

- **Perfect looping modification** (workflow)
  - Working on modifications to both diffusion and VAE decoding steps for seamless video loops
  - *From: Benjaminimal*

- **Multi-prompt automation system** (workflow)
  - Automated system using Florence and Groq APIs for generating context window prompts
  - *From: AJO*

- **Storyboarding workflow adaptation** (workflow)
  - Adapting LTX storyboarding workflow to run panels via 2 context windows with prompt changes
  - *From: AJO*

- **WanVideoWrapper** (node)
  - Kijai's wrapper implementation for Wan video generation
  - *From: Kijai*

- **Easy-Use node** (node)
  - Shows generation timing information
  - *From: avataraim*

- **Model patch order node** (node)
  - Kijai's node for LoRA compatibility in native mode
  - *From: Kijai*

- **Compile node** (node)
  - Available in Wavespeed nodes for LoRA compatibility
  - *From: Kijai*

- **Wan 2.1 LoRAs** (lora)
  - LoRAs available on Civitai for Wan 2.1
  - *From: Ashtar*

- **WanVideo FPS Interpolation** (node)
  - Experimental system for generating videos at low FPS and interpolating to higher FPS using latent interpolation
  - *From: fredbliss*

- **Context windowed FloweEdit** (workflow)
  - Implementation of FloweEdit with context windowing for longer video processing
  - *From: Kijai*

- **WanVideoWrapper** (node)
  - Kijai's wrapper implementation with TeaCache and optimizations
  - *From: Kijai*

- **FPS Controller node** (node)
  - Planned unified node to handle all FPS math and configuration in one function
  - *From: fredbliss*

- **Loop VAE decoding fix** (workflow)
  - Double decoding method with blending to eliminate flash artifacts in looped videos
  - *From: Benjaminimal*

- **WanVideoUnifiedFPSConfig** (node)
  - Unified FPS configuration node for cleaner workflow setup
  - *From: fredbliss*

- **WanVideoInterpolationDebugger** (node)
  - Debug visualization tool for interpolation analysis
  - *From: fredbliss*

- **WanVideoEnhancedFPSSampler** (node)
  - Enhanced FPS sampler with improved debugging capabilities
  - *From: fredbliss*

- **WanVideoWorkflowPreset** (node)
  - Preset system for common workflow configurations like cinema_24fps
  - *From: fredbliss*

- **Updated TeaCache implementation** (node)
  - Made TeaCache optional with calculated coefficients for more accurate step skipping
  - *From: Kijai*

- **Multi-scene storyboard workflow** (workflow)
  - Automated pipeline that converts reference image to 4-scene storyboard with individual video generation for each scene
  - *From: AJO*

- **Custom LTX interpolation node** (node)
  - Input a video, calculates everything in backend to allow for interpolation with keyframe capabilities
  - *From: Juampab12*

- **TeaCache context windowing implementation** (optimization)
  - Caching every unique window for context generation, ends up being like 20+ cached windows
  - *From: Kijai*

- **LTX Video Interpolation Node** (node)
  - Converts low fps videos to 24fps using LTX VAE
  - *From: Juampab12*

- **Wan Multi-GPU Script** (tool)
  - FSDP-based multi-GPU inference script for Wan with various optimizations
  - *From: intervitens*

- **OpenRouter node for prompt generation** (node)
  - Custom node for using Mistral's free API for Pixtral prompt generation
  - *From: orabazes*

- **CFG distillation LoRA** (lora)
  - Allows cfg=1 inference on Wan 1.3B with minimal quality loss
  - *From: spacepxl*

- **Wan music video with Suno** (workflow)
  - T2V generation combined with Suno audio, no color grading
  - *From: SamLand*

- **Automated block swapping based on pixel count** (workflow)
  - Elaborate system to automatically adjust block swapping based on resolution and pixel count
  - *From: DevouredBeef*

- **Patch model patch order node** (node)
  - Temporary solution to make LoRAs work with torch compile + native
  - *From: Kijai*

- **CFG distilled 1.3B LoRA** (lora)
  - Removes need for CFG guidance, works with gradient estimation sampler
  - *From: spacepxl*

- **LTX keyframe fix** (code modification)
  - Fixes VAE compression for keyframes in LTX model
  - *From: Juampab12*

- **First and last frame guidance LoRA** (lora)
  - Training LoRA for conditioning on both first and last frames
  - *From: mamad8*

- **VAE tiling script by Claude** (tool)
  - Generated by Claude AI for high resolution video processing
  - *From: aikitoria*

- **Multi-GPU Wan script** (tool)
  - Distributed inference across multiple GPUs with model weight splitting
  - *From: intervitens*

- **VAE tiling script** (script)
  - Claude-generated script for VAE tiling with 512px spatial tiling and 128px overlap
  - *From: aikitoria*

- **WanVideo Enhance-a-video node** (node)
  - Proper patch for enhance-a-video functionality applied after RoPE, works with TeaCache
  - *From: Kijai*

- **Complete Wan pipeline workflow** (workflow)
  - Single workflow combining Wan generation, interpolation, LatentSync, and upscaling
  - *From: VRGameDevGirl84(RTX 5090)*

- **Crop to Aspect Ratio node** (node)
  - Custom node with list of different aspect ratios to choose from
  - *From: VRGameDevGirl84(RTX 5090)*

- **Face tracking crop node** (node)
  - Finds face and crops at 16:9 with adjustable padding distance
  - *From: VRGameDevGirl84(RTX 5090)*

- **Tile upscale/deblur control LoRA** (lora)
  - In training for 31 hours, designed to improve upscaling and deblurring
  - *From: spacepxl*

- **Control LoRAs using channel concatenation** (training method)
  - Method for training control models that's stronger than ControlNet with less inference cost
  - *From: spacepxl*

- **Tile deblur control model** (control model)
  - Upscale control model that takes 0.25x downscaled blurred input and restores details
  - *From: spacepxl*

- **Squish Effect LoRA** (lora)
  - Creates squishing/morphing effects matching Pika-labs quality, trained on only 20 clips
  - *From: Kijai*

- **Tiled upscale control LoRA** (lora)
  - In development - allows generating low resolution then upscaling with control
  - *From: Juampab12*

- **Squish Effect LoRA** (lora)
  - Creates squishing/melting effects on objects and characters
  - *From: Juampab12*

- **Cakify LoRA** (lora)
  - Transforms objects into cake that can be cut
  - *From: Juampab12*

- **Hydraulic Press LoRA** (lora)
  - In development, creates hydraulic press crushing effects, trained on minimal data
  - *From: Juampab12*

- **Multi-GPU tiled VAE** (tool)
  - Distributed tiled VAE implementation with --tiled_vae flag
  - *From: intervitens*

- **Wan 2.1 1.3B tile control LoRA** (lora)
  - Control LoRA trained on blurred videos for upscaling and deblurring
  - *From: spacepxl*

- **Native ComfyUI control LoRA support** (feature)
  - Implementation to make control LoRAs work in native ComfyUI
  - *From: comfy*

- **Control LoRA training workflow** (workflow)
  - 50k video training setup with 9-13 frame sequences
  - *From: spacepxl*

- **Custom Python UI for Wan** (tool)
  - Alternative to ComfyUI for creating Wan videos with custom interface
  - *From: VRGameDevGirl84(RTX 5090)*

- **Wan optimization summary document** (documentation)
  - Comprehensive guide covering settings, optimizations, and troubleshooting for Wan
  - *From: BestWind*

- **Teacache integration for multigpu** (feature)
  - Added teacache support to multigpu script with configurable threshold
  - *From: intervitens*

- **Wan CFG Distill LoRA** (lora)
  - 50-60% speedup LoRA for Wan 1.3B with CFG distillation
  - *From: spacepxl*

- **TeaCache native node** (node)
  - Native TeaCache implementation in KJNodes
  - *From: Kijai*

- **Virtual VRAM node** (node)
  - Adds RAM as virtual VRAM for GGUF models
  - *From: GalaxyTimeMachine (RTX4090)*

- **Flying Effect LoRA** (lora)
  - LoRA for creating flying motion effects in WAN
  - *From: Juampab12*

- **Updated WAN TeaCache node** (node)
  - Fixed version with full_load option to prevent OOM
  - *From: Kijai*

- **WAN LoRA training guide** (workflow)
  - Fast LoRA training method taking only 20 minutes
  - *From: Juampab12*

- **Steamboat Willie LoRA** (lora)
  - 1.3B LoRA for Steamboat Willie style, fixed for ComfyUI compatibility
  - *From: Benjaminimal*

- **Resolution Calculator** (tool)
  - Tool for calculating optimal resolutions and frame counts for target pixel counts
  - *From: Fred*

- **Rope function optimization** (optimization)
  - 20% speed improvement through rope function adjustments in WanVideoWrapper
  - *From: Kijai*

- **Custom Wan UI** (tool)
  - Custom UI that runs ComfyUI workflows in backend with prompt enhancement
  - *From: VRGameDevGirl84(RTX 5090)*

- **Updated tile LoRA** (lora)
  - Trained twice as long with randomized blur sizes and extra noise injection for robustness
  - *From: spacepxl*

- **Multi-GPU Wan script** (script)
  - Completely separate multi-GPU implementation for Wan
  - *From: intervitens*

- **Aging timelapse LoRA** (lora)
  - Experimental LoRA for aging timelapse effects, teaching model to generate at different FPS than 16
  - *From: Juampab12*

- **Monster Hunter creature LoRA** (lora)
  - Trained on all monsters from Monster Hunter games to generate new creatures incorporating concepts from originals
  - *From: 3Dmindscaper2000*

- **T5 tokenizer exploration script** (tool)
  - Code to scrape and analyze UMT5 tokenizer for odd tokens and dataset-specific markers
  - *From: fredbliss*

- **Flying effect LoRA** (lora)
  - Helps create flying/levitation effects in WAN generations
  - *From: Juampab12*

- **SkipLayerGuidanceDiT node** (node)
  - ComfyUI implementation of skip layer guidance for improved prompt adherence
  - *From: Kijai*

- **Enhanced TeaCache node** (node)
  - Updated TeaCache compatible with SkipLayerGuidanceDiT
  - *From: Kijai*

- **Multi-scene story generation workflow** (workflow)
  - Complex automated workflow for generating multi-scene videos with storyboarding
  - *From: AJO*

- **VAE warmup trick implementation** (feature)
  - Solution to fix VAE burning artifacts at generation start
  - *From: Kijai*

- **ComfyUI RoPE implementation** (feature)
  - Alternative RoPE calculation that supports compilation for better performance
  - *From: Kijai*

- **TeaCache node fix** (fix)
  - Updated TeaCache node to work with latest ComfyUI changes
  - *From: Kijai*

- **Vintage style LoRA** (lora)
  - Trained on vintage photos to make generations look less modern, tested at various epochs
  - *From: VRGameDevGirl84(RTX 5090)*

- **Jinx character LoRA** (lora)
  - Character LoRA that works well with SLG for enhanced effect
  - *From: Cseti*

- **Saving Private Ryan style LoRA** (lora)
  - Style transfer LoRA that automatically adapts settings to Normandy
  - *From: Flipping Sigmas*

- **Enhancer LoRA** (lora)
  - Trained on diverse headshot dataset, enhances overall generation quality
  - *From: VRGameDevGirl84(RTX 5090)*

- **Enhancer LoRA** (lora)
  - Improves video quality for Wan 1.3B model
  - *From: VRGameDevGirl84(RTX 5090)*

- **Vintage style and Victorian goth LoRAs** (lora)
  - Custom style LoRAs for Wan, planning Civitai release
  - *From: VRGameDevGirl84(RTX 5090)*

- **ComfyUI-WanSeamlessFlow** (node)
  - Experimental node for smarter transitions between context windows using embedding interpolation and nearest neighbor optimization
  - *From: fredbliss*

- **Native SLG implementation** (node)
  - Skip Layer Guidance integrated into KJnodes WanVideoWrapper
  - *From: Kijai*

- **Army man LoRA** (lora)
  - 83MB LoRA at rank 64 for 1.3B model, trigger word 'GGG', trained on A6000
  - *From: Flipping Sigmas*

- **LoRA block selection helper** (workflow)
  - Node setup for enabling first 20 blocks and disabling singles for better LoRA quality
  - *From: Cubey*

- **WanSeamlessFlow** (tool)
  - Custom node for seamless prompt blending across video frames with embedding interpolation
  - *From: fredbliss*

- **WanVideoGranularTextEncode** (node)
  - Node for creating granular text embeddings with configurable transition strength and count between main prompts
  - *From: fredbliss*

- **Mobius looping node** (node)
  - Node for generating seamless video loops using latent shifting technique with configurable shift parameter
  - *From: Kijai*

- **Smart blend visualization** (tool)
  - ASCII visualization system showing context windows, blend zones, and section boundaries for debugging prompt transitions
  - *From: fredbliss*

- **Speed/Quality LoRA** (lora)
  - Achieves 20-step quality at 10 steps, works without trigger word
  - *From: VRGameDevGirl84(RTX 5090)*

- **WanVideoLoopArgs node** (node)
  - Handles loop settings with start/end percentages
  - *From: Kijai*

- **Content-aware blending framework** (workflow)
  - Frame analysis system for intelligent transition blending
  - *From: fredbliss*

- **Forked blending nodes** (node)
  - Multiple blending technique implementations
  - *From: fredbliss*

- **Tilelang branch** (optimization)
  - Branch with rmsnorm implemented with tilelang kernel for 10-20 second speedup
  - *From: intervitens*

- **WanVideoWrapper updates** (node)
  - Updated to support video mask input and various enhancements
  - *From: Kijai*

- **Depth control LoRA for Wan 1.3b** (lora)
  - Controls structure and motion based on depth maps, WIP version
  - *From: spacepxl*

- **ComfyUI-WanVideoStartEndFrames** (node)
  - Allows start and end frame editing in Wan wrapper
  - *From: Eclipse*

- **Restyledfirstframe** (lora)
  - V2V restyling LoRA for first frame processing
  - *From: 852話 (hakoniwa)*

- **Side scrolling LoRA** (lora)
  - LoRA for creating side-scrolling video effects
  - *From: Kytra*

- **Doom FPS LoRA** (lora)
  - First-person shooter perspective LoRA
  - *From: Juampab12*

- **WanVideo wrapper block dropping** (node)
  - Updated wrapper allowing dropping blocks from control LoRA
  - *From: Kijai*

- **Start/End frame implementation** (workflow)
  - First frame to last frame morphing workflow
  - *From: Kijai*

- **Anime style control LoRA** (lora)
  - Converts realistic video input to anime style using v2v in 1.3B model
  - *From: 852話 (hakoniwa)*

- **Start/End frame nodes** (node)
  - Replaces ImageClipEncode with dual image inputs for keyframe control
  - *From: The Shadow (NYC)*

- **Script for combining sharded diffusers** (tool)
  - Converts weights to fp16 and combines shards, can be modified to skip fp16 conversion
  - *From: Kijai*

- **WanVideoWrapper improvements** (node)
  - Updated with new CLIP vision encode options, tiling support, crop/stretch options
  - *From: Kijai*

- **Time lapse LoRA** (lora)
  - Creates time-lapse style videos, trained on painting process videos for 14B model
  - *From: 852話 (hakoniwa)*

- **Wan Control LoRAs** (lora)
  - Depth and tile control LoRAs for video generation
  - *From: spacepxl*

- **Sam2 points editor setup** (tool)
  - Point editing system for video segmentation, supports shift+click for positive points, shift+right click for negative
  - *From: Kijai*

- **Face LoRA with controllable angles and emotions** (lora)
  - Trained on I2V for 65 hours using 5-frame videos, enables controllable face angles and emotions
  - *From: Juampab12*

- **LoRA conversion script** (tool)
  - Convert Musubi LoRAs to Diffusion-pipe format: python convert_lora.py --input musubi_lora.safetensors --output converted.safetensors --target other
  - *From: Benjimon*

- **QoL blockswap setting node** (node)
  - Added quality of life improvement for setting blockswap without reloading model each time
  - *From: Kijai*

- **Prompt travel implementation** (feature)
  - Segments cross-attention for different prompts using | separator syntax
  - *From: Kijai*

- **I2V batch join method** (feature)
  - Splits conditioning images to different halves of video generation
  - *From: Kijai*

- **CFG-Zero-star node** (node)
  - Implementation of CFG-Zero-star technique for improved generation quality without additional model passes
  - *From: Kijai*

- **Self attention split functionality** (node)
  - Enables multiple prompt conditioning with stronger separation using pipe syntax
  - *From: Kijai*

- **CFG Zero Star KJ implementation** (node)
  - ComfyUI node for CFG Zero Star with zero init capability
  - *From: Kijai*

- **Official CFG Zero Star node** (node)
  - ComfyUI official implementation that stacks with different cfg tricks
  - *From: comfy*

- **WanVideoWrapper** (workflow)
  - Wrapper implementation with CFG Zero Star support
  - *From: Kijai*

- **WanVideo wrapper update for Fun models** (node)
  - Updated wrapper to support new Fun model variants with proper channel handling
  - *From: Kijai*

- **WanVideoWrapper** (node)
  - ComfyUI wrapper for Wan models by Kijai
  - *From: Kijai*

- **LoRA loader fix PR** (tool)
  - Pull request to fix LoadWanFunLora for control models
  - *From: caster*

- **WanVideoWrapper fp8 quantized models** (model)
  - Kijai quantized the 14B InP model to fp8_e4m3fn format for better performance
  - *From: Kijai*

- **Updated SDXL controlnet workflow** (workflow)
  - Combined workflow with grayscale lines, depth, and multiple blending options for sub-2min generation
  - *From: ArtOfficial*

- **Start/end frame experimental support** (node)
  - Added experimental end frame support to WanVideoWrapper
  - *From: Kijai*

- **WanVideoWrapper** (node)
  - Kijai's ComfyUI wrapper for Wan models with optimizations and control support
  - *From: Kijai*

- **ComfyUI-wanBlockswap** (tool)
  - Tool to control block swapping in native Wan implementation
  - *From: Persoon*

- **Wan video exp args node** (node)
  - Node for experimental Wan video arguments, available in nightlies
  - *From: burgstall*

- **WanVideoWrapper** (node)
  - ComfyUI wrapper for Wan models with control support
  - *From: Kijai*

- **Wan control LoRAs** (lora)
  - Control LoRAs for depth and other conditions on 1.3B model
  - *From: spacepxl*

- **Multi-scene workflow with Gemini** (workflow)
  - Cloud-runnable workflow for multi-scene generation from single reference using Gemini
  - *From: AJO*

- **Latent insert/combine node** (node)
  - Allows combining video latents for stitching clips
  - *From: Kijai*

- **Camera movement LoRAs** (lora)
  - Being developed for camera movements, training control LoRA on 1.3B fun control model
  - *From: mamad8*

- **WanVideoWrapper updated workflow** (workflow)
  - Updated workflow to accommodate new Wrapper updates
  - *From: ArtOfficial*

- **5B parameter Wan model** (model)
  - Downscaled 14B model to 4.14B parameters by dropping blocks and scaling dimensions, achieving functional video generation
  - *From: Kytra*

- **Modified diffusion-pipe for Wan training** (tool)
  - Modified diffusion-pipe repo to do full finetunes on WAN models
  - *From: Kytra*

- **5B Wan model experiment** (model)
  - 14B model trimmed to 5B parameters and retrained on limited dataset for educational purposes
  - *From: Kytra*

- **WanVideoWrapper** (node)
  - ComfyUI wrapper for Wan models with various optimizations
  - *From: Kijai*

- **Temporal masking workflow** (workflow)
  - Binary mask per frame workflow for video inpainting
  - *From: ˗ˏˋ⚡ˎˊ-*

- **WanVideoWrapper** (node)
  - Kijai's ComfyUI wrapper implementation for Wan models
  - *From: Kijai*

- **DiffSynth LoRAs** (lora)
  - Highres and aesthetics LoRAs for 1.3B model improving quality significantly
  - *From: David Snow*
