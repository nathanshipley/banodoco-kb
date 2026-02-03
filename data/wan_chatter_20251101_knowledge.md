# Wan Chatter Knowledge Base
*Extracted from Discord discussions: 2025-11-01 to 2025-12-01*


## Technical Discoveries

- **ATI (Animate Trajectory Inference) model has been largely forgotten despite being powerful**
  - ATI is described as a 'sick model' that just needed better UI implementation
  - *From: Fill/Kijai*

- **RIFE can run in real-time when coded properly**
  - Fill's implementation is 10x faster than other developers' versions by coding it properly
  - *From: Fill*

- **Wan 2.2 was not trained with CLIP vision at all**
  - Using CLIP vision with Wan 2.2 is just bloat on workflow and VRAM with no benefit
  - *From: DawnII*

- **FlashVSR can upscale single images when used with multiple steps**
  - 1 step, then 4 steps, then 8 steps produces sharper upscaled images. Takes 2 seconds per step after initial loading
  - *From: patientx*

- **Wan models can do basic latent noise mask based inpainting without VACE**
  - Any Wan model does basic inpainting quite well, questioning the need for WanAnimate and VACE for some tasks
  - *From: Ablejones*

- **Grid noise pattern was present in initial Wan models**
  - Bad grid noise pattern existed in early model versions but was fixed in later releases
  - *From: Kijai*

- **Noise masking works well for Wan models like image models**
  - Basic noise masking techniques from image generation are effective with Wan video models
  - *From: Ablejones*

- **VACE inpainting is more consistent than basic approaches**
  - VACE provides better consistency for inpainting tasks compared to standard methods
  - *From: Ablejones*

- **SVI-film reduces artifacting for extensions with 5 input frames**
  - SVI-film LoRA specifically designed to reduce artifacts when extending videos using exactly 5 input frames
  - *From: Ablejones*

- **Latent noise mask works for both i2v and t2v models**
  - Because it's not based on the i2v channels, latent noise masking is effective for both image-to-video and text-to-video models
  - *From: Ablejones*

- **Clearing Triton cache can dramatically reduce VRAM usage**
  - User saw VRAM usage drop from 14.3GB to 8.7GB after clearing Triton cache and updating dependencies
  - *From: flo1331*

- **Most video models are trained at 16fps which struggles with fast motion**
  - Training at 16fps or similar framerates creates inherent limitations for capturing fast motion accurately
  - *From: Kiwv*

- **Wan Animate control input is very flexible**
  - Can accept various types of input beyond just standard ControlNet inputs like depth/pose - more of a 'guide' than a 'pin' like ATI
  - *From: Mads Hagbarth Damsbo*

- **ATI gives trajectory control for character animation**
  - Better for subtle animations like breathing and swaying compared to standard Wan 2.2 I2V
  - *From: Fill*

- **UniC3 works with Wan 2.2 at higher strength**
  - Need to use strength of at least 3, tested up to 4-5 for effect with 2.2 models
  - *From: Kijai*

- **Dynamic/resized LoRAs cause OOM with torch compile**
  - LoRAs with different ranks within cause massive recompiles and memory issues when torch compile is enabled
  - *From: Kijai*

- **Wan Animate can follow point trajectories for animation control**
  - Works well for guiding objects along paths, not just for dances as commonly assumed. Better quality than ATI but doesn't 'pin' items like ATI
  - *From: Gleb Tretyak*

- **Wan Animate can work with first-to-last frame control**
  - Can use character on first and last frame, but ref input with background without character. When character moved, got correct text from ref image
  - *From: Gleb Tretyak*

- **BindWeave model released**
  - Wan 2.1 I2V based subject-consistent video generation with cross-modal integration using MLLM. Only 2 new layers, text projection to use Qwen VL 7B outputs
  - *From: ZeusZeus (RTX 4090)*

- **Video-as-prompt feature working**
  - Finally fixed logic error where self attention output layers weren't applied on corresponding output. Works with cfg now, tested with Wan 2.1 I2V
  - *From: Kijai*

- **SageAttention 2.2 significantly faster**
  - Generation speed way faster for t2v Wan after installing sage attn 2.2 with torch 2.10.0
  - *From: Léon*

- **VAP (Video Alignment Protocol) doesn't work properly**
  - Testing shows VAP outputs are just from the prompt, with placebo effect. Even their own code doesn't work in any useful manner. Any difference from reference video doesn't actually matter what video you use
  - *From: Kijai*

- **BindWeaver model uses unusual input structure**
  - Uses 4 references encoded separately in latents, concatenated to front of I2V channel. Empty references are still used as zeros: [ref_0, ref_1, ref_2, ref_3] [start_image + padding]. Start image becomes 5th latent
  - *From: Kijai*

- **Holocine maximum frame count is 375 frames**
  - Exceeding 375 frames causes system crash. 403 frames also tested and works
  - *From: BNP4535353*

- **WanFirstLastFrameToVideo node exists for native start/end frame I2V**
  - Built-in node for Wan 2.2 first-last frame workflow instead of using custom inputs
  - *From: Ablejones*

- **Cinematic Hard Cut v2 LoRA can create transitions between scenes**
  - Works by creating hard cuts between different scenes when combined with Qwen edit for second scene generation
  - *From: Ablejones*

- **BindWeave model uses image alpha channel as I2V channel mask**
  - The model expects alpha channel for masking but dataset images don't have alpha channel
  - *From: Kijai*

- **BindWeave background should be BLACK for best results**
  - Model appears to want black background for proper generation
  - *From: Kijai*

- **QwenVL input image needs specific resizing logic**
  - If width*height > 720*1280 resize to 0.3 scale, else 0.75 scale. Arbitrary but improves results
  - *From: Kijai*

- **Clip vision resolution is only 224x224**
  - Very small resolution means if using full reference image with small face, it can be detrimental
  - *From: Kijai*

- **Q8_0 vs bf16 casted to fp16 shows 0 difference in quality**
  - Testing showed no visible quality difference between these formats
  - *From: Gleb Tretyak*

- **Lightx2v v1030 appears cleaner than v1022**
  - User reports better results with newer version after testing
  - *From: JohnDopamine*

- **Wan 2.2 I2V has better identity preservation than LTX2 Pro**
  - LTX2 Pro has some of the worst identity preservation in an I2V model despite high video quality output, while Wan 2.5 is phenomenal at identity preservation
  - *From: blake37*

- **Position matters when using multiple references in Bindweave**
  - The positioning and arrangement of multiple reference images affects the output quality in multi-reference Bindweave generations
  - *From: Kijai*

- **Wan 2.2 first-last frame performs better than Veo 3**
  - Veo 3 first-last frame just fades out the first image instead of proper interpolation, while Wan does proper first-last frame morphing
  - *From: Draken*

- **Bindweave supports objects as subjects, not just people**
  - The model can handle object-based subject consistency in addition to human subjects
  - *From: Kijai*

- **Bindweave works without clip or qwenVL conditioning**
  - Generated smooth 121 frames at 480p without any text or vision conditioning, producing interesting morphing effects
  - *From: Kijai*

- **Bindweave model is trained from Wan 2.1 I2V 720p**
  - Confirmed by Kijai that Bindweave is 720p and trained from 2.1 I2V, not 2.2
  - *From: Kijai*

- **QwenVL in Bindweave has minimal effect**
  - Kijai reports the QwenVL part has minimal to no effect, works without it, unsure how to use it properly
  - *From: Kijai*

- **Bindweave uses specific negative prompt**
  - Uses comprehensive negative prompt: 'Bright tones, overexposed, static, blurred details, subtitles, style, works, paintings, images, static, overall gray, worst quality, low quality, JPEG compression residue, ugly, incomplete, extra fingers, poorly drawn hands, poorly drawn faces, deformed, disfigured, misshapen limbs, fused fingers, still picture, messy background, three legs, many people in the background, walking backwards, split screen, divided frame, frame split, multiple parts, separated,motionless, frozen, still image, no movement, stationary, unmoving'
  - *From: Kijai*

- **Bindweave ref_masks should be white on image, black on padding**
  - Box mask for subject is important as full frame mask makes it all washed out
  - *From: Kijai*

- **New T2V Seko v2.0 LightX2V uses 'Phased DMD' distillation method**
  - The newer LightX2V version uses 'Phased DMD' technique instead of self-forcing
  - *From: yi*

- **SeC-4B provides tighter masking than Sam2**
  - SeC-4B masking is alot tighter than Sam2 with blockify expand
  - *From: LookingGlass*

- **EdgeTAM is much faster than Sam2**
  - EdgeTAM is 7 months old, light version of Sam2, faster but slightly less accurate. 15fps on phone reportedly
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Wan 2.2 low-noise model works as excellent refiner**
  - Can be used to refine any T2I model output with denoise value 0.2, works even with SD1.5
  - *From: slmonker(5090D 32GB)*

- **Wan 2.2 can handle in-between frames**
  - Model can process sequences with frames between start and end, not just first-to-last frame
  - *From: Kijai*

- **PainterI2V node enhances LightX2V LoRA dynamics**
  - Manipulates motion by pre-scaling input latents and balancing brightness increase
  - *From: slmonker(5090D 32GB)*

- **Flash VSR 1.1 is significantly better than v1**
  - Smoother and more natural looking results, less VRAM hungry
  - *From: Elvaxorn*

- **Multitalk works with silent audio for idle animations**
  - Using silence audio makes body and head move like speaking videos but mouth won't move
  - *From: manu_le_surikhate_gamer*

- **Wan 2.2 masks are inverted from VACE**
  - blank image = black mask, opposite of VACE behavior
  - *From: lemuet*

- **Single frames inserted in middle of sequences are ignored**
  - Only sequences of 2+ frames have effect, single frames get blended with prev/next frames
  - *From: lemuet*

- **svi-film lora only works with hn model at high strength**
  - Need strength set to 3, doesn't fix distorted frames but prevents color shifting
  - *From: lemuet*

- **Frames within 4+1 block appear blended together**
  - Each frame appears to be a bit blended with the prev/next frame, causing light flashes and dark compensation
  - *From: lemuet*

- **Painter node adds input image to gray frames in I2V**
  - Uses coded formula: diff = gray_latent - start_latent, then scales with motion_amplitude
  - *From: Kijai*

- **Wan 2.2 I2V handles noisy input images well**
  - Can handle 0.2 augment noise in input image effectively
  - *From: Kijai*

- **Wan 2.2 can do multi-keyframe natively**
  - Set frames you want to the last frame of a latent (latent indices are 4x+1)
  - *From: Juampab12*

- **CUDA 130 is faster than 128 without compile**
  - CUDA 130 roughly as fast as torch compile was on 128, but torch compile on 130 produces black/static images
  - *From: devnullblackcat*

- **injecting some noise helps a lot with video generation**
  - Using noise injection in the generation process improves results
  - *From: A.I.Warper*

- **Wan Animate can use ATI trajectories with first frame and ref**
  - Model can handle trajectories from ATI along with first frame and reference image inputs
  - *From: Gleb Tretyak*

- **Setting VACE white level from gray (0.5) to black (0) fixes awful end frames**
  - Changing the VACE white level from gray (mid 0.5) to 0 (black) eliminates noise at the end of generations
  - *From: Gleb Tretyak*

- **Wan Animate supports multiple control inputs simultaneously**
  - Can use first frame, last frame, one ref slot, controlnet, and trajectories all together
  - *From: Gleb Tretyak*

- **Audio CFG of 8.0 fixes gibberish output in Ovi model**
  - Bumping audio_cfg to 8.0 resolved mostly gibberish output and made Ovi work properly
  - *From: Kijai*

- **For wrapper implementations the 'null' image is black, for native it's gray**
  - Different implementations use different null image colors - wrapper uses black frames, native uses gray frames
  - *From: Ablejones*

- **Audio negative prompt connection bug discovered and fixed**
  - Node was storing negative as positive and expecting it to be negative when it was positive, so audio negative was never actually used
  - *From: Kijai*

- **Default video negative is 253 tokens, short video negative is 11 tokens**
  - Log shows torch.Size([253, 4096]) vs torch.Size([11, 4096])
  - *From: Kijai*

- **EasyCache can skip significant steps while maintaining quality**
  - Skipped 16 out of 50 steps in one test, 9 out of 40 in another
  - *From: Kijai*

- **Motion augmentation scheduling creates interesting effects**
  - Can schedule which latent frames motion is applied to, creating scene transition effects
  - *From: Ablejones*

- **Bindweave model on HuggingFace is missing the scaled_fp8 key for ComfyUI native**
  - This prevents it from loading properly in native ComfyUI
  - *From: Ablejones*

- **OVI 1.1 works better with specific resolutions**
  - Works well with horizontal formats like 1280x704, 960x512, 1120x448. Vertical formats like 512x960 don't work as well
  - *From: avataraim*

- **OVI 1.1 needs more swap blocks to avoid OOM**
  - Requires 25-30 swap blocks for 1280x704 resolution on 24GB VRAM
  - *From: avataraim*

- **Context windows don't work well with I2V models**
  - Each context window is its own model call needing input image, but you only have single clean input for whole process
  - *From: Kijai*

- **Kandinsky 5 Pro 20B model parameters confirmed**
  - It's around 20B parameters and considering how the 2B performs, it could be about 2x-4x better than Wan2.2
  - *From: yi*

- **Generated latent artifacts explained**
  - It's triggered by the mismatch between real (encoded) and generated latents. Generated latents are usually blurry, decoder doesn't know how to handle blurry latents as they're out of distribution, so it generates speckle/grid artifacts as its failure mode
  - *From: spacepxl*

- **VRAM cleanup nodes don't work with node-cached models**
  - If the node references to the model, it's cached in the node itself and it can not be freed. VRAM clean nodes generally do not do anything
  - *From: Kijai*

- **LightX2V LoRA effectiveness patterns**
  - Earlier LightX loras were still better than new ones in light testing. Both are better than the initial lightning ones
  - *From: ingi // SYSTMS*

- **Ovi 1.1 resolution preferences confirmed**
  - 1280x704 and 704x1280 working best, low you go get bad quality shake and wrong motion
  - *From: avataraim*

- **Kandinsky 5.0 2B model significantly outperforms Wan 2.2 5B and 2.1 14B**
  - Ada reports that Kandinsky 2B blows away 2.2 5B and 2.1 14B in quality
  - *From: Ada*

- **Kandinsky 20B T2V works with FP8 and blockswapping**
  - Ada successfully got 20B T2V working with FP8 quantization and block swapping on 24GB VRAM
  - *From: Ada*

- **Kandinsky 20B has uncensored NSFW capability**
  - 20B fully knows nudity with no barbie doll censoring on top or bottom
  - *From: Ada*

- **Face detailer workflow can improve small faces in generated videos**
  - Running a face detailer workflow afterwards makes a big difference for videos with small faces
  - *From: ingi // SYSTMS*

- **Closer framing helps with face likeness in Wan Animate**
  - Using closer framing in reference images improves results
  - *From: hudson223*

- **spacepxl is making progress on training a better VAE to fix speckle/dithering**
  - Working on Wan VAE training to fix the speckle/dithering problem, though GAN component is holding back quality
  - *From: spacepxl*

- **TTM (Time to Move) technique is masked latent inpainting with timestep scheduling**
  - The method is fundamentally masked latent inpainting with timestep scheduling, possibly implementable with native ComfyUI nodes
  - *From: Kijai*

- **TTM works with any model, not just Wan**
  - The technique should work with any video generation model, tested with Wan 1.3B T2V
  - *From: Kijai*

- **LightX2V causes ghosting issues on low noise side**
  - Using LightX2V LoRA on the low noise part of split samplers creates ghost artifacts and ruins video quality
  - *From: slmonker*

- **TTM provides camera control capabilities for I2V models**
  - TTM enables camera control effects like zoom and movement for Wan 2.2 I2V that can't be achieved with prompts alone
  - *From: hicho*

- **Wan 2.2 high/low noise split makes motion techniques work better**
  - The MoE architecture's high/low noise expert split allows for better motion control and resolution
  - *From: Kijai*

- **TimeToMove (TTM) is essentially just v2v + differential diffusion with the right masks**
  - TTM isn't really a new technique, just works well with Wan 2.2. The original code applies it only for a few steps (3-7 out of 50 total steps)
  - *From: spacepxl*

- **TTM works by understanding direction and path from reference video automatically**
  - The model can follow paths and directions from reference footage without needing specific prompts for movement direction
  - *From: avataraim*

- **LightX2V LoRA v1030 performs very close to base model motion quality**
  - New lightx2v lora is very impressive for i2v, much better than other lightx2v variants or lightning. Works well when adjusting shift value to match sigma boundary at 0.900
  - *From: FL13*

- **MoGe2 works well for generating 3D models for camera animation with TTM**
  - Can generate 3D model and set up in Blender in under 2 minutes. Just import model, plug texture into emission shader, place camera at 0,0,0 and adjust focal length
  - *From: lemuet*

- **TTM can be used as vid2vid where you define different noise to the masked area**
  - TTM is essentially vid2vid with noise applied to masked regions
  - *From: Kijai*

- **Mask can be one frame and acts like v2v**
  - Setting mask to one black frame makes TTM behave like vid2vid
  - *From: hicho*

- **LightX2V is problematic for low noise part in TTM**
  - LightX2V works fine for high noise but causes issues in low noise sampling, huge quality gap when removed
  - *From: slmonker(5090D 32GB)*

- **LightX2V 1030 is I2V model**
  - 1030 version is specifically for I2V, not T2V distill
  - *From: Koba*

- **SAM3 uses prompt-based segmentation**
  - More precise prompts give more accurate segmentation, can limit to 1 simultaneous segmentation, automatically retrieves highest confidence mask
  - *From: slmonker(5090D 32GB)*

- **TTM fixes lighting and object interactions**
  - TTM fixes lighting of animated objects to match scene and animates hair/clothes interactions
  - *From: xwsswww*

- **WAN is 16fps native, requires prompting adjustments for 24fps**
  - When converting 16fps WAN output to 24fps, need to prompt for slow motion to achieve normal speed playback
  - *From: Ruairi Robinson*

- **FFGO LoRA enables multiple subject generation with Wan 2.2 I2V**
  - Uses specific trigger prompt 'ad23r2 the camera view suddenly changes.' and requires white background for reference subjects
  - *From: Kijai*

- **res_2s and multistep samplers effectively do twice the steps**
  - For fair comparison, should compare res_2s at X steps vs other samplers at 2X steps
  - *From: Kijai*

- **FFGO works with multiple characters (3-4 subjects tested)**
  - Even number of references may work better, very sensitive to prompting
  - *From: Dever*

- **FFGO can work as IP adapter with single image**
  - FFGO transfers style and colors well even with just one image, working like an IP adapter
  - *From: Lodis*

- **Holocine + FFGO makes I2V work**
  - Combining Holocine and FFGO enables image-to-video functionality
  - *From: Elvaxorn*

- **TTM and FFGO can be combined**
  - TTM (Time-To-Move) can be combined with FFGO for enhanced control
  - *From: Guey.KhalaMari*

- **Wan 2.2 shows significant visual improvement over 2.1**
  - Comparison described as 'like rtx on and off', with 2.2 having realism and global illumination-like lighting
  - *From: hicho*

- **FFGO trigger prompt requirement**
  - Need to add trigger prompt 'ad23r2 the camera view suddenly changes.' to the start when using FFGO
  - *From: Kijai*

- **Wan 2.2 has MoE architecture with High/Low noise expert split**
  - First the High noise model handles noise over a certain threshold, then the Low model finishes the generation
  - *From: JohnDopamine*

- **v2v with base wan i2v 2.2 models can use reference without FFGO or TTM**
  - Reference frames can be inserted and work exactly like VACE. Characters can come from out of frame and maintain likeness. Used 0.8 denoise with 8 steps.
  - *From: lemuet*

- **First frame in TTM doesn't need to be actual first frame of video**
  - Can use any frame as reference to help preserve environment and character consistency, even if it doesn't match the motion sequence chronologically
  - *From: Guey.KhalaMari*

- **Native TTM node values are different from wrapper version**
  - Set start step in sampler, TTM node steps are on top of that. Example: 4 steps sampler + 2 steps TTM
  - *From: Kijai*

- **FL13 created working tiled upscaler for wan i2v**
  - Doesn't limit to VRAM if you set few number of tiles. Can upscale to 2K/4K but very slow (10+ minutes for 2K on 4090)
  - *From: FL13*

- **Can do v2v without TTM by encoding motion video and plugging into latent input**
  - Set denoise to 0.7-0.8, enable 'add_noise_to_samples' on first sampler only
  - *From: lemuet*

- **Reference frames work by inserting reference 4 times then starting image**
  - Must fit the 4-frame block rule, reference becomes part of the video like a hard cut edit
  - *From: lemuet*

- **Wan 2.2 uses two models split by timestep range**
  - High noise trained on sigma >= 0.875, low noise on low timesteps. Like MoE but experts are entire models selected by timestep
  - *From: spacepxl*

- **Wan 2.2 low noise is probably a 2.1 finetune**
  - High noise is more different from 2.1. Splitting allows each to perform better on their part of the schedule
  - *From: spacepxl*

- **Modern models use flow matching and predict velocity (noise - data)**
  - ComfyUI converts to x0 prediction. Flow matching outperforms diffusion across the board
  - *From: spacepxl*

- **RF schedule focuses lots on high noise then tails off**
  - 'Shift' parameter controls the curvature of the inference schedule
  - *From: spacepxl*

- **Wan masks are inverted between wrapper and native implementations**
  - Masks work differently between wrapper/native versions - they are inverted
  - *From: Gleb Tretyak*

- **Frame windows are fixed in Wan Animate causing hallucination after input ends**
  - X(frame window) - (x-1)(motion frames) = total frames - this causes Wan to continue generating after input clip finishes
  - *From: DawnII*

- **Native Wan Animate V2 is better than V1**
  - V1 underperforms for native, V2 version is a fix for native implementation
  - *From: Gleb Tretyak*

- **You can feed RGB video directly as control input without preprocessor**
  - You technically don't need to use a controlnet preprocessor, you can input a video directly as a control - it should follow the structure and motion
  - *From: Lodis*

- **HY1.5 empty latent speeds up Wan T2V generation**
  - Using HY1.5 empty latent on Wan makes T2V very fast and is very good for upscaling
  - *From: hicho*

- **Triton caches cause memory increases after updates**
  - Any model code change can end up having to recompile during inference, adding on top of current VRAM use, mostly on Windows
  - *From: Kijai*

- **fp16 models can be faster than fp8_scaled on Ampere cards**
  - Full fp16 versions of Wan 2.2 run as fast or faster than fp8_scaled on RTX 3090/3090 Ti due to how Ampere handles fp16
  - *From: GWX-Reloaded*

- **ComfyUI can load models larger than GPU VRAM**
  - Can load full fp16 models that exceed VRAM capacity by swapping, performance depends on RAM speed and motherboard
  - *From: GWX-Reloaded*

- **Depth maps work better than masks for selective upscaling**
  - Using clipped depthmap stops upscaler adding unnecessary detail in background, more accurate than regular masking
  - *From: David Snow*

- **Wan 2.2 high and low noise models run sequentially**
  - Since they don't run simultaneously, you could potentially use larger models for each stage
  - *From: metaphysician*

- **LoRA stacking prevents fading issues**
  - Can stack MOE high noise, Lightx2v 480p rank 256, and Wan 2.1 LoRAs without fading, unlike using MOE alone
  - *From: GWX-Reloaded*

- **SteadyDancer preprocessing might work with other models**
  - All preprocessing (pose detector, pose alignment) is applied before blocks, so might be compatible with other models beyond the base 2.1 I2V
  - *From: Kijai*

- **SVDQuant uses nunchaku implementation with custom kernels for speed**
  - Has int8 and fp8 matmuls plus torch compile, but no actual int4 matmuls despite claims
  - *From: Kijai*

- **SteadyDancer uses positive and negative pose inputs**
  - Negative pose appears to be mis-aligned version used as negative conditioning, with scale differences between positive and negative
  - *From: Kijai*

- **SteadyDancer uses triple model passes by default**
  - 50 steps x 3 passes = 150 total model calls, vs 4 steps shown in testing
  - *From: Kijai*

- **JSON prompting works for video models without specific training**
  - Structured JSON format provides more precise directions than loose text prompts, works with Wan models
  - *From: Scruffy*

- **Denoise parameter works differently in wrapper vs native**
  - WanVideoWrapper denoise is just step adjustment shortcut, while native KSampler does actual denoise calculations
  - *From: Scruffy*

- **SteadyDancer requires base model weights**
  - Pose embeddings are only 6MB, but LoRA extraction failed because patch embed was trained too
  - *From: Kijai*

- **Wan 2.2 5B model is significantly undertrained**
  - The diffusion model can't handle the VAE properly, despite the VAE itself not being that bad. Shows worse structure/motion than 1.3B
  - *From: spacepxl*

- **1.3B model performs better when trained on high res with control inputs**
  - Unless you train it on high resolution with control inputs, then it's actually really strong
  - *From: spacepxl*

- **CFG distillation is the primary driver of step distillation**
  - Theory from Z-Image research that cfg distillation actually drives step distillation performance
  - *From: spacepxl*

- **Latent upscaling requires diffusion models for proper results**
  - Best way to latent upscale is with a diffusion model trained as control lora to take low res latent and output high res latent. Interpolating latents is a fool's game without generative models
  - *From: spacepxl*

- **Kandinsky 5.0 Pro shows near Veo3 quality**
  - Near Veo3 quality for motion and semantics, about wan2.1 level for prompt following. Even 2B outperforms Wan2.1 in motion and semantics
  - *From: yi*

- **SeedVR can be better than other options sometimes**
  - Although one step really isn't enough, can show grainy artifacts
  - *From: spacepxl*

- **Phantom works amazingly well for replicating subjects like product photos**
  - Demonstrated excellent subject replication capabilities in product photo scenarios
  - *From: Ablejones*

- **Using separate student loras for high/low noise in distillation**
  - Concept for DMD distillation: 14B teacher, 1.3B student, 1.3B fake, with separate student loras for high/low noise
  - *From: spacepxl*

- **Custom ops can prevent graph breaks in torch.compile while keeping parts uncompiled**
  - Using @torch.library.custom_op allows uncompiled operations like sageattention and unmerged lora application to be part of the graph without breaking it, preventing memory issues
  - *From: Kijai*

- **Graph breaks cause 4-5GB higher peak VRAM usage**
  - Intermediate tensors like q, k, v do not get released and stay in VRAM until whole block is done when graph breaks occur
  - *From: Kijai*

- **SageAttention holds unnecessary fp16 q and k tensors**
  - Latest version holds input fp16 q and k for no reason above the int8 that it actually uses, could drop at least 1GB of peak VRAM by fixing this
  - *From: Kijai*

- **Context windows work with concat latent controls**
  - Native context windows PR now works with concat latent controls, context window blends are almost invisible especially with freenoise enabled
  - *From: spacepxl*

- **New optimizations dramatically reduced memory usage**
  - RAM usage dropped from 110GB to 80GB, GPU shared memory from 63GB to 34GB, VRAM to 10GB on test case
  - *From: Gleb Tretyak*


## Troubleshooting & Solutions

- **Problem:** FlashVSR dtype error with Float and Half mismatch
  - **Solution:** Roll back to version checkpoint commit 9e0b3afe4eef5188ac441e83e06edd7ed2b26150
  - *From: Dita*

- **Problem:** OOM issues with Wan Animate on 5090 that previously worked
  - **Solution:** Enable LoRA merging in LoRA load node to fix memory issues
  - *From: Quality_Control*

- **Problem:** Silent crash with native torch compile
  - **Solution:** Remove --pinned-memory and --async-offload flags, especially if at RAM limit
  - *From: Gleb Tretyak*

- **Problem:** VAP model doesn't work with CFG
  - **Solution:** Implementation still has issues, not fully working yet
  - *From: Kijai*

- **Problem:** Higher VRAM usage with low resolution I2V than high resolution
  - **Solution:** Issue acknowledged but no solution provided
  - *From: WorldX*

- **Problem:** Newer wrapper version causes OOM errors
  - **Solution:** Roll back to earlier version or increase blockswap settings. Also try clearing Triton cache
  - *From: flo1331*

- **Problem:** SVI-Shot gives frozen frame video with Wan 2.2
  - **Solution:** SVI-Shot doesn't work with 2.2 at all, need to use alternative approaches
  - *From: Dita*

- **Problem:** Input frames get glitchy with ghosting in clip extension
  - **Solution:** Replace glitched frames with original frames if ghosting doesn't affect rest of clip
  - *From: lemuet*

- **Problem:** VRAM usage increased after wrapper update
  - **Solution:** Update all dependencies, clear Triton cache, update wrapper, clear Triton cache again
  - *From: flo1331*

- **Problem:** Custom sigma and step mismatch with Euler scheduler
  - **Solution:** Other schedulers work fine, issue specific to Euler with 2.2 HN sampler
  - *From: DawnII*

- **Problem:** Massive VRAM increase with torch compile
  - **Solution:** Consider dropping torch compile attempts or use --cache-none argument
  - *From: Gleb Tretyak*

- **Problem:** Second sampler uses much more VRAM/RAM than first
  - **Solution:** Use --cache-none argument or save latent to disk between samplers
  - *From: lemuet*

- **Problem:** First compile run uses significantly more VRAM on Windows
  - **Solution:** Clear Triton caches, sometimes just running workflow again works
  - *From: Kijai*

- **Problem:** OOM issues with dynamic LoRAs and torch compile
  - **Solution:** Add @torch.compiler.disable() to apply_lora function in custom_linear.py and clear triton cache
  - *From: Kijai*

- **Problem:** Old VACE workflows suddenly not working
  - **Solution:** Remove custom nodes that hook into sampler, search .py files for wrapper conflicts
  - *From: JohnDopamine*

- **Problem:** Wan Animate causing image shake without masking
  - **Solution:** Use masking and expand mask in y-axis using transform node to reduce overall shot wiggles
  - *From: enigmatic_e*

- **Problem:** Memory issues after ComfyUI update
  - **Solution:** Roll back to commit from Oct 12-13th to resolve memory problems introduced around Oct 15th
  - *From: Miku*

- **Problem:** Triton cache causing issues
  - **Solution:** Clear triton cache folder, can be found at C:\Users\username\AppData\Local\Temp\torchinductor_username or ~/.triton on Linux
  - *From: Kijai*

- **Problem:** RuntimeError: stack expects a non-empty TensorList in Diffusion Forcing
  - **Solution:** No specific solution provided yet
  - *From: Dream Making*

- **Problem:** Longcat dropping reference image
  - **Solution:** Set attention_mode to sdpa in model loader
  - *From: Hashu*

- **Problem:** Float and BFloat16 dtype mismatch in Longcat
  - **Solution:** Revert wrapper version to 1.3.6 or turn off compile
  - *From: Ablejones*

- **Problem:** OOM issues after git pull
  - **Solution:** Add --cache-none to launch script, or disable --fast command line argument
  - *From: Stef*

- **Problem:** Torch compile bug causing VRAM spikes
  - **Solution:** Cancel and rerun to get normal memory use, or disable dynamic LoRAs for full graph compilation
  - *From: Kijai*

- **Problem:** Sage 1 compatibility issues
  - **Solution:** Upgrade to SageAttention 2.2: pip install --upgrade sageattention --force-reinstall
  - *From: Ablejones*

- **Problem:** vae.encode None type error
  - **Solution:** VAE is somehow NoneType - check VAE loading
  - *From: samhodge*

- **Problem:** Sage attention broke after ComfyUI update due to rope commit
  - **Solution:** Update KJNodes - Kijai fixed it using core attention override system instead of monkey patching
  - *From: Kijai*

- **Problem:** Input type FloatTensor and weight type CUDABFloat16Type mismatch with bf16 wan animate
  - **Solution:** Cannot merge loras with low mem load enabled for wan animate
  - *From: Gleb Tretyak*

- **Problem:** Context options with reference latent causes device mismatch error
  - **Solution:** Remove reference latent to avoid 'tensors on cuda:0 vs cpu' error
  - *From: Gleb Tretyak*

- **Problem:** Qwen not compatible with ComfyUI core controlnet node
  - **Solution:** Bypass controlnet node - error disappears when removed
  - *From: xwsswww*

- **Problem:** Wan animate doesn't work without lightx loras - overexposed at higher CFG
  - **Solution:** Ask in wan comfyui channel for specific settings
  - *From: Kiwv*

- **Problem:** Holocine BindWeaver model requires enabling merge loras
  - **Solution:** Enable merge loras and set image dimensions to multiple of 16
  - *From: Daviejg*

- **Problem:** RuntimeError: The size of tensor a (29124) must match the size of tensor b (24)
  - **Solution:** Remove KJnodes folder and git clone again, works with Sage Attention and latest comfyui
  - *From: Ashtar*

- **Problem:** CUDA out of memory after ComfyUI update
  - **Solution:** Use --disabled-pinned-memory flag or rollback ComfyUI commit
  - *From: Ashtar*

- **Problem:** System freeze on Image Concatenate Multi
  - **Solution:** Add 'unload all models' toggle at end of workflow
  - *From: Gleb Tretyak*

- **Problem:** End frame becomes discolored/purple with jpg artifacts
  - **Solution:** Enable fun_or_fl2v_model setting for anything but basic 2.1 I2V
  - *From: Kijai*

- **Problem:** Interpolation fails with torch.cuda.HalfTensor vs torch.cuda.FloatTensor mismatch
  - **Solution:** Issue occurs after resize image node, still being investigated
  - *From: lostintranslation*

- **Problem:** High VRAM usage with lower resolutions using specific LoRAs
  - **Solution:** Use --reserve-vram 2 flag when starting ComfyUI
  - *From: Kijai*

- **Problem:** FlashVSR node output causing errors with other nodes
  - **Solution:** Add .cpu().float() to the final node output: return(output.cpu().float() ,)
  - *From: Kijai*

- **Problem:** Multiple WanWrapper installs causing image_embeds error
  - **Solution:** Remove duplicate WanWrapper installations, ensure only one is active
  - *From: Kijai*

- **Problem:** FlashVSR memory leak with tile sizes above 256
  - **Solution:** Use tile size 256 or below - 288 and higher cause memory leaks
  - *From: lostintranslation*

- **Problem:** CUDA error appearing randomly in ComfyUI
  - **Solution:** Try the flag --disable-pinned-memory if using latest ComfyUI
  - *From: Lumifel*

- **Problem:** Wan Animate has visible shift/transition in video
  - **Solution:** Adjust mask to be tighter around subject, leave thin edge on top so model sees what's there, try 50% coverage on problematic areas
  - *From: TimHannan*

- **Problem:** ComfyUI memory leak with color match node
  - **Solution:** Disable pinned memory with --disable-pinned-memory flag, remove --fast and --async-offload
  - *From: Gleb Tretyak*

- **Problem:** Bindweave QwenVL input errors
  - **Solution:** Recreate the node to fix old input name from workflow
  - *From: Kijai*

- **Problem:** LongCat loading extremely slow on CPU
  - **Solution:** Use GPU instead of CPU for text encoding nodes, CPU loading is much slower
  - *From: Ablejones*

- **Problem:** NAG (Negative Conditioning) no longer works with updated Bindweave
  - **Solution:** Known issue after update, but results are much better without it
  - *From: JmySff*

- **Problem:** Contrast shifting at exact same point in every video
  - **Solution:** Switch from Tiled VAE Decoding to regular VAE Decoding
  - *From: devnullblackcat*

- **Problem:** Custom 2.1 style LoRAs won't work with LongCat
  - **Solution:** LongCat is not a Wan model, just similar structure - nothing trained for Wan will work
  - *From: Kijai*

- **Problem:** Memory leak issues with ComfyUI
  - **Solution:** Try --disable-pinned-memory flag or --cache-none, disable multi-gpu node pack
  - *From: Gleb Tretyak*

- **Problem:** Green color appearing on buildings in Wa20 Motion Control
  - **Solution:** No definitive solution provided, issue persists across different samplers/schedulers
  - *From: XWAVE*

- **Problem:** SeC Model loader errors
  - **Solution:** No solution provided in discussion
  - *From: van*

- **Problem:** WanAnimate goes black screen with clip embeds and sageattn on some GPUs
  - **Solution:** Disconnect clip output or use PatchSageAttentionKJ node with sageattn_qk_int8_pv_fp16_cuda mode
  - *From: Kijai*

- **Problem:** Torch compile + scaled models + pinned memory causes instant OOM
  - **Solution:** Use GGUF models instead of fp8_scaled for torch compile compatibility
  - *From: Gleb Tretyak*

- **Problem:** VAE decode OOM on 24GB VRAM
  - **Solution:** Use unload all models and vramdebug before decode
  - *From: asd*

- **Problem:** Memory leak in FlashVSR node with non-256 tile sizes
  - **Solution:** Use alternative node from https://github.com/1038lab/ComfyUI-FlashVSR which doesn't have memory leak
  - *From: lostintranslation*

- **Problem:** Torch compile issues with VRAM
  - **Solution:** Clear Triton cache at C:\Users\<username>\AppData\Local\Temp\torchinductor_<username>
  - *From: Kijai*

- **Problem:** Green artifacts when using higher resolution (720p)
  - **Solution:** The noise becomes too fine at higher resolutions, causing green artifacts. Model seems to generate noise based on color distribution proportion of background video
  - *From: slmonker*

- **Problem:** CUDA out of memory after ComfyUI and Python dependencies update
  - **Solution:** Use --disable-pinned-memory command line argument or update ComfyUI-GGUF custom node and switch to UnetLoaderGGUFDisTorch2MultiGPU
  - *From: xwsswww*

- **Problem:** Triton compilation error with ATI workflow
  - **Solution:** Disable torch compile or sageattention - it's a Triton installation issue not related to the workflow
  - *From: Kijai*

- **Problem:** Bidirectional sampling causes instant OOM
  - **Solution:** Can do 1000 frames but not 512 with bidirectional due to enormous VRAM increase
  - *From: Gleb Tretyak*

- **Problem:** Ovi model producing mushy/blurry results
  - **Solution:** Remove the extra audio model node and only use the video model, or increase audio_cfg to 8.0
  - *From: avataraim*

- **Problem:** Audio issues with multi-channel video files
  - **Solution:** Video had separate speech channels - extract as mono/stereo or save as stereo 44.1kHz
  - *From: burgstall*

- **Problem:** WanVideoUniAnimateDWPoseDetector error 'cannot convert float NaN to integer'
  - **Solution:** Occurs when hand detection fails, likely didn't detect the hand properly
  - *From: Ablejones*

- **Problem:** Audio quality issues in Ovi model
  - **Solution:** Connect text_embeds instead of negative_text_embeds, or use proper negative prompt configuration after bug fix
  - *From: avataraim*

- **Problem:** Bindweave produces noise/scribbling output on native ComfyUI
  - **Solution:** Cannot work properly on native - needs wrapper implementation with proper QwenVL integration and noise padding
  - *From: Kijai*

- **Problem:** Updated wan wrapper causing OOM with Ditto
  - **Solution:** No specific solution provided yet
  - *From: Stad*

- **Problem:** Device mismatch error with ref latent on context options
  - **Solution:** Issue is with having RMBG or SAM models on CPU - not fixed yet
  - *From: Gleb Tretyak*

- **Problem:** OVI 1.1 OOMing on 24GB VRAM
  - **Solution:** Use 40 swap blocks instead of 30-36
  - *From: avataraim*

- **Problem:** SAM2 segmentation causing OOM after processing
  - **Solution:** Use first frame only for LLM/VLM, let SAM handle rest based on it
  - *From: burgstall*

- **Problem:** OVI audio text spilling outside <S> <E> tags
  - **Solution:** Make sure text inside tags is long enough (around 10 seconds worth)
  - *From: Kijai*

- **Problem:** Poor Wan Animate LoRA results
  - **Solution:** Use trigger word in captions, train on 720p images with videos, use lower rank (32 instead of 64)
  - *From: ingi // SYSTMS*

- **Problem:** OOM on loops with Sa2VA segmentation
  - **Solution:** Edit the node's code to force unload the Qwen model after each run with a bool setting
  - *From: boorayjenkins*

- **Problem:** Garbled and discolored first/last frames with new lightx2v lora
  - **Solution:** Reduce the shift to 5, as dpm_sde highlights these details more
  - *From: 🦙rishappi*

- **Problem:** Kandinsky 5 VAE OOM issues
  - **Solution:** Use tiled VAE or it will OOM. Also torch version related - works on 2.7.1 but not 2.9
  - *From: yi and Kagi*

- **Problem:** Comfy UI slowdown in browser
  - **Solution:** Opening comfy in chrome on mac doesn't have this problem. On same machine where it's slow in chrome, works fine in firefox
  - *From: scf*

- **Problem:** High VRAM usage setting
  - **Solution:** Set to normal VRAM instead of high VRAM to reduce memory issues
  - *From: hicho*

- **Problem:** Plastic waxy look in renders
  - **Solution:** 20 steps is way too much when using lightx LoRA, try 4-6 steps. Also CFG should be 1 on both samplers
  - *From: garbus*

- **Problem:** Tiled VAE causes temporal blending artifacts at frame 45 with Wan 2.2
  - **Solution:** Better to run lower resolution with default VAE than higher resolution with Tiled VAE
  - *From: brbbbq*

- **Problem:** Fixed seed doesn't prevent animation changes when adjusting other settings
  - **Solution:** Any change to size, shift, or other parameters will change the output regardless of fixed seed - this is normal behavior
  - *From: ingi // SYSTMS*

- **Problem:** Wan Animate keeps too many facial features from input video instead of reference image
  - **Solution:** Disconnect the face_images input from WanVideo Animate Embeds node
  - *From: Charlie*

- **Problem:** OOM issues that have been popping up more frequently
  - **Solution:** Add --disable-pinned-memory to launch .bat and remove --fast parameter
  - *From: JohnDopamine*

- **Problem:** Ovi 1.1 unclear speech quality
  - **Solution:** Update to latest nightly nodes and try using higher audio cfg (up to 10)
  - *From: Kijai*

- **Problem:** Ghost artifacts appearing in TTM videos
  - **Solution:** Remove LightX2V LoRA from low noise sampler - only use it on high noise side
  - *From: slmonker*

- **Problem:** TTM doesn't work with split samplers initially
  - **Solution:** Apply TTM only on high noise side, not low noise side, as it shouldn't be applied to low noise anyway
  - *From: Kijai*

- **Problem:** Latent burn and mask seams with VACE Fun
  - **Solution:** Still being investigated, no clear solution provided yet
  - *From: Fawks*

- **Problem:** IndexError with 5B model
  - **Solution:** Increase sample count - error occurs when samples are too low
  - *From: Guey.KhalaMari*

- **Problem:** TTM mask quality issues
  - **Solution:** Need perfect alpha channel without background cuts - use separate background and person/item rather than inpainting
  - *From: avataraim*

- **Problem:** DMP++_SDE sampler causing issues with second sampler in dual sampling
  - **Solution:** Stop the reference one step before the last step of high noise to fix the issue
  - *From: lemuet*

- **Problem:** TTM fails if empty space has no noise or content
  - **Solution:** Make sure background areas have some content, TTM doesn't work well with fully black/empty backgrounds
  - *From: Kijai*

- **Problem:** Double character issue appearing in generations
  - **Solution:** Remove subject from reference image, or check if using distill LoRA at too high strength (someone was accidentally using 2.2 lora at 3.0 strength)
  - *From: hicho*

- **Problem:** Resolution mismatch errors when changing default settings
  - **Solution:** Make sure resolution settings match between nodes when modifying from defaults
  - *From: hicho*

- **Problem:** WanVideoEncode error: GET was unable to find an engine to execute this computation
  - **Solution:** Change WanVideo VAE Loader from bf16 to fp16
  - *From: xwsswww*

- **Problem:** Module errors when using VACE with wrong model combinations
  - **Solution:** Use T2V models with VACE node, I2V models give errors saying VACE only works with T2V
  - *From: psylent_gamer*

- **Problem:** TTM dimension mismatch with 5B model
  - **Solution:** Ensure dimensions are divisible by 32 as 5B requires, check for 720 vs 704 pixel issues
  - *From: Kijai*

- **Problem:** TTM mask code assumes 2.1 latent space with 5B model
  - **Solution:** Kijai fixed the mask creation for 5B VAE compatibility
  - *From: Kijai*

- **Problem:** Attention_mode=sageattn causes corrupted output on H100
  - **Solution:** Switch back to SDPA attention mode
  - *From: killermonkeys*

- **Problem:** LoRA key not loaded messages
  - **Solution:** Clear the caches, often caused by using wrong model/lora combinations like 2.1 I2V lora on non-2.1 model
  - *From: Kijai*

- **Problem:** Transformers 4.57.1 causing errors with Wan I2V
  - **Solution:** Error was actually from too long prompt, not transformers version
  - *From: patientx*

- **Problem:** TTM animation leaving white spaces when moving objects
  - **Solution:** Use outpainting or clone tool to fill the cutout space with background content
  - *From: xwsswww*

- **Problem:** OOM issues after triton update
  - **Solution:** Add --disable-pinned-memory to launch script and remove --fast launch argument
  - *From: JohnDopamine*

- **Problem:** Low VRAM usage with 8GB
  - **Solution:** Use --cache-none argument with fast drive and enable Windows virtual memory
  - *From: garbus*

- **Problem:** Character cheeks interpreted as sad lips in Wan Animate
  - **Solution:** User seeking solution for correcting facial expression interpretation
  - *From: Guus*

- **Problem:** FFGO scene switching at inconsistent frames
  - **Solution:** Potentially add mask to last reference frame to guide the model
  - *From: eraxor_*

- **Problem:** TTM ghosting issues
  - **Solution:** Shift start and end values on TTM node, mix with playing with shift value on sampler. Sometimes obvious in high noise preview showing double characters.
  - *From: Guey.KhalaMari*

- **Problem:** TypeError: WanTimeTextImageEmbedding.forward() got an unexpected keyword argument 'timestep_seq_len'
  - **Solution:** Need to update to compatible workflow/model versions
  - *From: David Snow*

- **Problem:** Silent fatal crashes in ComfyUI
  - **Solution:** Usually RAM related. Try disabling pinned memory and/or increasing OS swap size
  - *From: Kijai*

- **Problem:** OOM issues with Wan 2.2 Mocha
  - **Solution:** Can swap up to 40 blocks. Text encoder memory is separate from sampling. Try lower resolution like 448x256 instead of 480p
  - *From: Suomsoh*

- **Problem:** Loop nodes causing memory leaks
  - **Solution:** Suspected memory leak in easy-use looping nodes, doesn't clear RAM properly
  - *From: Cseti*

- **Problem:** ValueError when using T2V model with encoded images
  - **Solution:** T2V models only work with text prompts, I2V models needed for encoded images
  - *From: lemuet*

- **Problem:** Reference frames being denoised even with masks
  - **Solution:** Masks seem to be ignored in this setup, may need different approach
  - *From: lemuet*

- **Problem:** FFGO reference image takes part of output video
  - **Solution:** Use node to ignore first 4 frames, or cut with video editor. Trim latent node may work
  - *From: patientx*

- **Problem:** RuntimeError about channel mismatch (36 vs 68 channels)
  - **Solution:** Switch from 2.2 VAE to 2.1 VAE - 2.2 models use 2.1 VAE
  - *From: Shubhooooo*

- **Problem:** InfiniteTalk hanging at 720p/1280 width
  - **Solution:** Stick to lower resolutions like 640p square, 720p may be too demanding
  - *From: metaphysician*

- **Problem:** Dithering dots in Wan 2.2 output
  - **Solution:** Use more steps instead of recommended LightX2V steps
  - *From: harryB*

- **Problem:** Green/pink color tint with T2V-A14B controlnet
  - **Solution:** Switch to different LightX LoRA, may be incompatibility between old LoRAs and new models
  - *From: David Snow*

- **Problem:** Wan video preview not showing in sampler node after update
  - **Solution:** Check if preview is enabled in settings - updates can turn it off
  - *From: StableVibrations*

- **Problem:** Pink hue/color shifts in Wan output
  - **Solution:** Enable add_noise_to_samples on the first sampler
  - *From: David Snow*

- **Problem:** Wan going OOM after a few generations
  - **Solution:** Known recurring issue, no definitive fix mentioned
  - *From: lostintranslation*

- **Problem:** Pose detection failing on 2D drawings/sketches
  - **Solution:** Try using SAM3D to convert drawings to more recognizable 3D figures first, then extract poses
  - *From: Scruffy*

- **Problem:** Unable to subgraph nodes with Get/Set connections
  - **Solution:** Copy/paste the group of nodes to a new canvas, subgraph there, then copy back
  - *From: JohnDopamine*

- **Problem:** High memory consumption after Wan wrapper updates
  - **Solution:** Clear triton caches and run model few times to get rid of recompilation overhead
  - *From: Kijai*

- **Problem:** Asian eyes appearing squinted/closed in Wan Animate
  - **Solution:** Disconnect background and mask so only pose and face inputs are used, background comes from reference image
  - *From: 42hub*

- **Problem:** Wan 2.2 Animate converting anime style to realistic
  - **Solution:** Disable lightx2v wan 2.1 lora and add 'anime, animation, 3d' to prompt to reduce realistic results
  - *From: Suomsoh*

- **Problem:** Context window size mismatch in native i2v
  - **Solution:** Don't leave context length at 81 when increasing latent count for frames above that - causes size mismatch
  - *From: Baku*

- **Problem:** Slow VAE encoding on pytorch 2.9 vs 2.7
  - **Solution:** PyTorch version-dependent issue, rolling back to 2.7.1 cu128 showed significant speed improvements
  - *From: shaggss*

- **Problem:** Expected tensors on same device error with fp16
  - **Solution:** Don't place FreeMemory nodes right after loader and before sage attention - causes CPU/CUDA device mismatch
  - *From: metaphysician*

- **Problem:** Flashing artifacts in Wan 2.2 i2v generations
  - **Solution:** Issue was caused by overly long auto-generated prompts from Grok - making prompts more concise fixed the problem
  - *From: David Snow*

- **Problem:** KJ WanVideoSampler showing different results than KSampler
  - **Solution:** Use SamplerCustom with same sigmas list, or KSamplerAdvanced with matching start_at step, due to different denoise implementations
  - *From: Ablejones*

- **Problem:** WanVideoSampler showing 7 steps and 85 frames for 81 frame video
  - **Solution:** 0.75 denoise_strength starts at later step than 0, and 85 frames includes reference frame processing
  - *From: Ablejones*

- **Problem:** TTM high pass looks good in preview but low pass ignores it
  - **Solution:** Low pass gets more influenced by driving video, resulting in stiff choppy generation
  - *From: Desto Geima*

- **Problem:** Torch.compile causing massive VRAM usage and slow performance after updates
  - **Solution:** Clear Triton caches by deleting contents of C:\Users\<username>\.triton and C:\Users\<username>\AppData\Local\Temp\torchinductor_<username>, update triton-windows, restart ComfyUI
  - *From: Kijai*

- **Problem:** WanVideoWrapper showing recompile warnings and slow generation
  - **Solution:** Delete and reinstall WanVideoWrapper folder, check torch version compatibility, clear Triton caches
  - *From: Kierkegaard*

- **Problem:** Context windows causing weird blending issues in long videos
  - **Solution:** Use cache none for long videos, though this isn't a complete fix
  - *From: Gleb Tretyak*

- **Problem:** OOM errors with torch.compile on 720p 81 frames
  - **Solution:** Use chunked rope and pytorch RMS norm instead of compile, increase block swap to 40, set prefetch_blocks to 1 for better VRAM efficiency
  - *From: Kijai*

- **Problem:** Canny control making images look flat/2D
  - **Solution:** Need good prompting, use Fun Vace 2.2 which has improved control training, don't rely on reference input for style transfer
  - *From: Ablejones*

- **Problem:** Skeleton+depth mix producing actual skeleton in output
  - **Solution:** Don't use skeleton+depth mix, send depth and skeleton into separate Vace control inputs using separate WanVaceToVideo nodes or WanVacePhantomDualV2 node
  - *From: Ablejones*

- **Problem:** Graph breaks preventing tensor release in torch.compile
  - **Solution:** Use torch custom ops instead of @torch.compiler.disable() to avoid graph breaks while keeping parts uncompiled
  - *From: Kijai*

- **Problem:** ComfyUI memory management estimation errors
  - **Solution:** Use Manager's 'Unload Models' function or Purge VRAM node before suspected problem steps
  - *From: Ablejones*

- **Problem:** Memory issues with Wan 2.2
  - **Solution:** Run with --reserve-vram flag, new wrapper optimizations should fix most issues
  - *From: Kijai*


## Model Comparisons

- **Chrono Edit vs Qwen Edit**
  - Chrono Edit is worse than Qwen Edit
  - *From: Ada*

- **dasiwaWAN22 vs SmoothMix**
  - dasiwaWAN22 has better realism than SmoothMix
  - *From: asd*

- **VACE vs ATI for trajectories**
  - VACE isn't nearly as accurate with trajectories as ATI
  - *From: Kijai*

- **FlashVSR quality issues**
  - FlashVSR looks oversharpened with halos compared to other upscalers
  - *From: WorldX*

- **Quantized vs FP16 models for consecutive frames**
  - Quantized models have certain chance of producing errors in consecutive frames, FP16 more reliable
  - *From: BNP4535353*

- **832x480 vs 1280x720 generation time**
  - Higher resolution produces better results but generation time increases threefold
  - *From: BNP4535353*

- **SVI-film vs VACE for extensions**
  - VACE doesn't have glitchy input frame issues that SVI-film has, but SVI-film still helps reduce color shifting
  - *From: lemuet*

- **Wan 2.2 fp8 high vs low model generation time**
  - High model takes twice as long as low model for same user, unusual behavior
  - *From: patientx*

- **ATI vs Wan 2.2 I2V**
  - ATI gives trajectory control for specific animations, Wan 2.2 is general text/image to video - different use cases
  - *From: Fill*

- **SeedVR vs FlashVSR for upscaling**
  - FlashVSR better quality, SeedVR2 better but takes more time
  - *From: ulvord*

- **Sora pricing vs open source**
  - Sora costs $0.1 per second, open models need to be cheaper or better to compete
  - *From: Draken*

- **Wan Animate vs ATI**
  - Wan Animate better quality but ATI still wins for specific controls like face tracking and precise spinning motions
  - *From: Juampab12*

- **VACE vs Wan Animate**
  - VACE has stronger native control, but Wan Animate saves time by keeping everything in same model
  - *From: Mads Hagbarth Damsbo*

- **SmoothMix vs BindWeave**
  - SmoothMix model still better than BindWeave for I2V
  - *From: Juampab12*

- **LightX2V full models vs LoRAs**
  - Full models are slightly stronger but you can't control strength, so LoRAs are preferred
  - *From: Kijai*

- **Prompting with '|' vs Cinematic Hard Cut LoRA**
  - LoRA actually works better than simple prompting methods like 'description before | description after'
  - *From: Ablejones*

- **LTX 2 Pro vs other models in benchmarks**
  - LTX 2 Pro ranks 3rd in I2V (Wan2.5 at 13th), 7th in T2V (Wan2.5 at 14th). LTX 2 pro above Sora 2 pro overall
  - *From: yi*

- **Holocine general consensus vs demo quality**
  - General consensus is it isn't great compared to demo results
  - *From: Kiwv*

- **InfinityStar vs Wan 2.1**
  - Same quality as Wan2.1 but new autoregressive architecture, 8B model from ByteDance
  - *From: yi*

- **Lightx2v v1022 vs v1030**
  - v1030 appears cleaner and better overall, v1022 adds less motion
  - *From: JohnDopamine*

- **Q5_K_M vs Q8_0 vs bf16**
  - Q5_K_M shows some differences (like extra eyebrows) but doesn't completely garbage output
  - *From: Gleb Tretyak*

- **Lower GGUF quants vs Q8**
  - Q8 is fast, but lower quants are slower to dequantize, avoid low quants
  - *From: Kijai*

- **Wan 2.2 I2V vs LTX2 Pro I2V**
  - Wan 2.2 has much better identity preservation, LTX2 Pro has poor identity preservation despite high video quality
  - *From: blake37*

- **Wan 2.2 vs Veo 3 first-last frame**
  - Wan 2.2 does proper first-last interpolation while Veo 3 just fades images
  - *From: Draken*

- **MagRef vs Phantom vs Bindweave**
  - MagRef only does single reference at full res, Phantom doesn't work well with distill LoRAs and breaks identity, Bindweave supports multiple references
  - *From: Kijai*

- **FlashVSR tiny vs full model**
  - Tiny seems 30% faster than full with near zero loss of quality
  - *From: lostintranslation*

- **Area vs Lanczos downscaling**
  - Area performs comparably to Lanczos but runs on GPU making it 10-20x faster
  - *From: lostintranslation*

- **LongCat vs other Wan models**
  - LongCat has limitations: requires multiple samplers instead of one, different architecture means LoRAs don't work and unlikely community will retrain, making it limited use case
  - *From: Lodis*

- **Lucy Edit 1.1 vs previous version**
  - Still very bad with anime content
  - *From: DiXiao*

- **New T2V Seko v2.0 quality vs 250928**
  - Quality seems utter ass compared to the 250928 version
  - *From: ucren*

- **EdgeTAM vs Sam2**
  - EdgeTAM is faster but slightly less accurate than Sam2
  - *From: Kijai*

- **Bindweave results before and after update**
  - Much better results after update, even though NAG no longer works
  - *From: JmySff*

- **I2V Wan vs VACE for start/end image handling**
  - I2V Wan treats start/end images as separate videos instead of blending, VACE blends them
  - *From: ingi // SYSTMS*

- **2.1 VACE vs Fun VACE 2.2**
  - 2.1 VACE performs better than Fun 2.2 for most tasks, though Fun VACE better for some specific tasks
  - *From: Mecha*

- **FlashVSR processing methods**
  - Built-in tiled processing better than cutting into separate chunks for longer videos
  - *From: lostintranslation*

- **WanAnimate quality with vs without svi-shot**
  - Quality degraded significantly when using svi-shot on wan animate
  - *From: Gleb Tretyak*

- **Bindweave vs VACE for ID preservation**
  - Bindweave seems to get more similarity from what I've seen
  - *From: Juampab12*

- **1.3B model quality limitations**
  - It's just the fact that it's only 1.3B model that limits the quality so much, and low res too
  - *From: Kijai*

- **FastWan vs Turbo LoRA for speed**
  - FastWan is much better than Turbo LoRA for audio models
  - *From: Kijai*

- **HuMO vs InfiniteTalk for lip sync**
  - HuMO better for lip sync and expressiveness but same expression throughout, InfiniteTalk better all-rounder for longer videos and multiple characters
  - *From: Tachyon*

- **5B vs 14B model quality with Ovi**
  - 5B with Ovi is quite good, for 14B it would be close to Wan 2.5 quality
  - *From: ZeusZeus*

- **LongCat vs Wan 2.2**
  - LongCat prompt adherence is closer to Wan 2.1, not as good as 2.2. Only better at video extension. No substitute for 2.2 A14B high noise for motion and prompting
  - *From: Kijai*

- **Training on T2V vs I2V models**
  - T2V designed to generate all visuals vs I2V focused on using image as starting point, so T2V has more image data to build on
  - *From: ingi // SYSTMS*

- **Wan 2.1 vs 2.2 for character training**
  - 2.2 is better in terms of fine details than 2.1
  - *From: ingi // SYSTMS*

- **Kandinsky 5 2B vs Wan 2.2**
  - Really close to wan2.2. Just that prompt adherence is iffy. Else semantics, quality are really good
  - *From: yi*

- **New vs old LightX LoRAs**
  - Earlier LightX loras were still better, both are better than initial lightning ones
  - *From: ingi // SYSTMS*

- **3 ksampler merging vs loop**
  - 3 ksampler merging is better than loop
  - *From: hicho*

- **Kandinsky 5.0 2B vs Wan models**
  - 2B blows away Wan 2.2 5B and 2.1 14B in quality
  - *From: Ada*

- **Depth Anything 3 vs Depth Anything 2**
  - DA3 has worse image quality for monocular depth, more geometrically accurate but not good for Wan use
  - *From: Kijai*

- **Tiled VAE vs Default VAE for Wan 2.2**
  - Lower resolution with default VAE is better than higher resolution with Tiled VAE due to temporal artifacts
  - *From: brbbbq*

- **TTM vs old fashioned inpainting**
  - Question raised but not answered in this discussion
  - *From: Ablejones*

- **TTM vs Uni3C for camera control**
  - TTM is described as 'the new uni3c for camera control in wan 2.2 i2v'
  - *From: hicho*

- **I2V vs T2V with TTM**
  - I2V works better for keeping background/subject consistent, T2V acts more like vid2vid
  - *From: Kijai*

- **Wan 1.3B vs basic requirements**
  - 1.3B can't do real-time generation due to frame batching requirements, but causal models with 9 frames can be real-time
  - *From: Kijai*

- **LightX2V v1030 vs base model vs other speed LoRAs**
  - New lightx2v v1030 performs very close to base model motion, much better than other lightx2v variants or lightning LoRAs
  - *From: FL13*

- **Hunyuan 3D vs VGGT for 3D generation**
  - Hunyuan creates actual 3D meshes (not point clouds) and looks better for objects, but VGGT still better for camera guidance in some cases
  - *From: Juampab12*

- **UniPC vs DMP++_SDE samplers**
  - UniPC mostly just reduces small jitter while maintaining motion, while DMP++_SDE can cause issues with second sampler
  - *From: lemuet*

- **SAM3 vs SAM2 semantic segmentation**
  - SAM3 semantic segmentation not as good as SAM2 points-to-mask accuracy
  - *From: slmonker(5090D 32GB)*

- **3 sampler vs 2 sampler setup**
  - 3 sampler setup still worth it for motion testing
  - *From: FL13*

- **With vs without LightX2V on low noise**
  - Huge quality gap, much better without LightX2V for low noise part
  - *From: slmonker(5090D 32GB)*

- **FFGO vs Bindweave**
  - FFGO with Wan 2.2 beats Bindweave, Kijai feels sorry for Bindweave since 2.2 + LoRA basically replaces it
  - *From: Kijai*

- **Bindweave vs Wan 2.2 + FFGO**
  - Bindweave allows full resolution per subject but can't match 2.2's motion capability
  - *From: Kijai*

- **Sec4B vs SAM2/3 for video segmentation**
  - Sec4B still preferred for video segmentation, though SAM2/3 have interactive features
  - *From: slmonker*

- **Wan 2.2 vs 2.1**
  - 2.2 has better realism and lighting, described as 'rtx on vs off'
  - *From: hicho*

- **HunyuanVideo 1.5 vs Wan**
  - Wan still appears better, though HunyuanVideo is 24fps and faster. Community consensus favors Wan quality
  - *From: MarkDalias*

- **Wan 2.2 Fun Vace + pose vs Wan Animate**
  - Wan 2.2 Fun Vace with pose might outperform Wan Animate for character animation
  - *From: Guus*

- **Wan 2.1 vs 2.2 lightx2v LoRAs**
  - 2.1 gives more intense motion for superhero action but animates background more. 2.2 gets movement but less intensity.
  - *From: metaphysician*

- **3 sampler method vs full 20 steps**
  - 3 sampler method is best you can get compared to full 20 steps
  - *From: FL13*

- **T2V upscaler vs I2V upscaler**
  - T2V version more detailed but suffers on original details. I2V retains start image details even with high denoise
  - *From: FL13*

- **TTM vs direct v2v approach**
  - TTM more convenient and works well with anything thrown at it, but direct v2v approach also works
  - *From: lemuet*

- **I2V vs T2V for reference keeping**
  - I2V models keep reference while T2V models don't - makes sense
  - *From: hicho*

- **Flow matching vs diffusion**
  - Flow matching outperforms diffusion pretty much across the board
  - *From: spacepxl*

- **SDXL base/refiner vs Wan 2.2 high/low**
  - Same idea but Wan 2.2 executed much better - nobody used SDXL refiner
  - *From: spacepxl*

- **WanAnimate vs VACE for depth**
  - WanAnimate doesn't understand depth at all, VACE 2.2 does
  - *From: 42hub*

- **FlashVSR vs normal upscaling**
  - Should be as good as normal version but faster, though some find results look artificial
  - *From: FL13*

- **Wrapper vs Native Wan quality**
  - Quality is 1:1 or really close between wrapper and native implementations
  - *From: Gleb Tretyak*

- **Wan 2.2 vs 2.1 quality**
  - Wan 2.2 is way better quality wise than 2.1
  - *From: Lodis*

- **Stable Audio vs ACE for video sound**
  - Both are not that good for generating sound for videos
  - *From: Valle*

- **Anisora vs base Wan 2.2 for i2v**
  - Anisora works well for anime style movement with less artifacts and motion blur, but dramatically changes character appearances and colors - not suitable for animation tool use cases
  - *From: GWX-Reloaded*

- **fp16 vs fp8_scaled on Ampere cards**
  - fp16 is as fast or faster than fp8_scaled on RTX 3090/3090 Ti, while fp8 models on non-fp8 cards just cast to fp16 anyway with extra compute overhead
  - *From: Kijai*

- **PainterLongVideo vs simple extension**
  - PainterLongVideo is 'vibecoded nothing' - simple extension from last frame gives same results, while Painter I2V actually prepares latents in interesting way
  - *From: 42hub*

- **Different lightx2v LoRA ranks**
  - 480p rank 256 holds likeness and prompt adherence with less degradation than MOE alone, rank 256 gives more freedom but costs more parameters and possible artifacts vs rank 64
  - *From: GWX-Reloaded*

- **SteadyDancer vs WanAnimate**
  - Unfair comparison since SteadyDancer doesn't do face at all, WanAnimate comparison is silly
  - *From: Kijai*

- **SteadyDancer vs UniAnimate**
  - UniAnimate works with other models and isn't much worse, if at all
  - *From: Kijai*

- **VACE vs I2V models for reference keeping**
  - I2V models have VACE beat for keeping reference identity
  - *From: Kijai*

- **Structured JSON vs natural language prompting**
  - JSON may help but natural language sometimes works just as well, no convincing evidence of major difference
  - *From: Ablejones*

- **FlashVSR quality vs other upscalers**
  - Poor quality due to tiny attention windows preventing proper motion tracking, details swim around
  - *From: spacepxl*

- **Wan 2.2 5B vs 1.3B**
  - 1.3B shows better structure/motion despite being smaller, 5B is way undertrained
  - *From: spacepxl*

- **Kandinsky 5.0 Pro vs Wan2.1**
  - Kandinsky near Veo3 quality for motion/semantics, Wan2.1 level prompt following. Even 2B Kandinsky outperforms Wan2.1 motion
  - *From: yi*

- **Z-Image vs other models**
  - Z-Image turning out to be the most interesting recent model development
  - *From: Ablejones*

- **Fun Vace 2.2 vs Vace 2.1**
  - Fun Vace 2.2 has improved training for working with controls, especially openpose
  - *From: Ablejones*

- **Torch.compile vs non-compile performance**
  - Compile uses much more VRAM (18GB vs 11GB) on Windows with marginal speed benefits, not worth it
  - *From: Kijai*

- **del vs detach for memory management**
  - del is enough for inference mode, detach is about computation graph not memory
  - *From: spacepxl*

- **Graph break vs recompile performance**
  - Graph break is worse than recompile, recompiles are fine if they aren't too many
  - *From: Kijai*

- **Video upscaling methods**
  - Most use SeedVR2 or FlashVSR these days for video upscaling
  - *From: Kijai*

- **Context window vs Topaz Starlight**
  - Context window blends almost invisible, Starlight actually has horrible context seam in test clip
  - *From: spacepxl*


## Tips & Best Practices

- **Describe foreground characters in HuMo prompts to avoid unwanted additions**
  - Context: When doing lip-sync or character consistency work
  - *From: Ablejones*

- **Use static camera descriptions in prompts to prevent camera movement**
  - Context: When generating with HuMo for lip-sync work
  - *From: Ablejones*

- **Try SVI-shot using first frame as reference to lock character in place**
  - Context: For better character consistency in HuMo generations
  - *From: Ablejones*

- **Put trigger words in Chinese, rest of prompt in English for Qwen LoRAs**
  - Context: When using Qwen Edit LoRAs with Chinese triggers
  - *From: uff*

- **Use pressure cache to help with RAM usage for large models**
  - Context: When running at RAM limits with native implementations
  - *From: Kijai*

- **Prompting is incredibly important for all Wan models**
  - Context: You often can't get away from iterating on prompting, no LLM one-shot solution known
  - *From: Ablejones*

- **Use noise masking for spatial inpainting to refine and detail**
  - Context: Works great for refining and detailing in spatial inpainting tasks
  - *From: Ablejones*

- **Clear Triton cache after bigger updates**
  - Context: Can be helpful for resolving VRAM and performance issues
  - *From: Kijai*

- **Generate smaller and upscale rather than generating large**
  - Context: Often gives better results than generating directly at high resolution
  - *From: metaphysician*

- **Don't use many LoRAs unmerged in general**
  - Context: Better to merge LoRAs for better performance
  - *From: Kijai*

- **Use high VRAM for better Wan Animate quality**
  - Context: 96GB VRAM produces good results without post-processing
  - *From: Fill*

- **Set TRITON_CACHE_DIR to ComfyUI path**
  - Context: Prevents cache interference between multiple ComfyUI installations
  - *From: patientx*

- **Remove Patch Model Patcher Order node**
  - Context: Unnecessary with v2 compile nodes and can cause OOM
  - *From: Kijai*

- **Use preview nodes on all outputs**
  - Context: To understand exactly which frames you're getting from complex workflows
  - *From: ArtOfficial*

- **Lines work better than dots for Wan Animate control**
  - Context: When creating control inputs for animation
  - *From: Mads Hagbarth Damsbo*

- **Solid shapes work quite well for Wan Animate**
  - Context: Alternative to lines for control inputs
  - *From: Mads Hagbarth Damsbo*

- **Better character positioning helps reduce shake**
  - Context: Position character close to first frame pose to reduce random shake in reference
  - *From: HeadOfOliver*

- **Generate at higher resolution like 1920x1080**
  - Context: May help with face problems in Wan Animate
  - *From: Juampab12*

- **Use MPS LoRA at 1.0 strength in high model**
  - Context: Improves prompt adherence, marginally better than HPS
  - *From: Juampab12*

- **Use SmoothMix model with MPS LoRA**
  - Context: Best way to use Wan I2V found so far
  - *From: Juampab12*

- **For models that don't like odd shots/angles, cut step count way down and use higher order sampler**
  - Context: When trying to get unusual outputs like hybrid creatures or odd camera angles
  - *From: Clownshark Batwing*

- **Turn noise down or off (eta = 0.0) for better prompt adherence**
  - Context: Higher noise levels help convergence toward more likely model outputs
  - *From: Clownshark Batwing*

- **Use 17 motion frames instead of 16 for smoother continuation**
  - Context: 17 frames continue without hitching compared to 16 frames
  - *From: DawnII*

- **Storyboard prompts for Holocine must be written concisely and clearly**
  - Context: For better results with Holocine T2V generation
  - *From: BNP4535353*

- **Set n frames higher than input n frames for first-to-last frame workflows**
  - Context: When using first and last frame generation methods
  - *From: Dream Making*

- **Use face crop for clip vision instead of full image**
  - Context: When face is small in reference image, full image can be detrimental
  - *From: Kijai*

- **Disconnect clip vision from Wan Animate encode node for better likeness**
  - Context: Especially helps as video progresses and after first window
  - *From: HeadOfOliver*

- **Treat Wan Animate input image like VACE v2v start frame**
  - Context: Make mask large enough to incorporate new character
  - *From: HeadOfOliver*

- **Use Q8 quants with offloading instead of lower quants**
  - Context: Only use lower quants if RAM limited, offloading is very fast now
  - *From: Kijai*

- **Iterate prompts manually for better results**
  - Context: Model may be capable but needs right prompt, don't assume it can't do something after few tries
  - *From: Ablejones*

- **Use Simple or Beta schedulers with lightx loras and low step counts**
  - Context: These schedulers work better for prompt adherence with this setup
  - *From: Ablejones*

- **Use lower size images for Qwen and add box masks to padded reference images**
  - Context: When using Bindweave with multiple references
  - *From: Kijai*

- **Remove background for better subject freedom in Bindweave**
  - Context: To avoid zoom out effects and get better character consistency
  - *From: Kijai*

- **Use x4 upscale then downscale instead of direct x2 upscale**
  - Context: For better quality with FlashVSR - x2 direct produces artifacts
  - *From: lostintranslation*

- **Clear triton cache on Linux for better VRAM management**
  - Context: Can reduce max allocated memory from 15.8GB to 9.9GB
  - *From: Kijai*

- **Use box mask for subject in Bindweave**
  - Context: Full frame mask makes results washed out
  - *From: Kijai*

- **Pad references properly for Shot/Dance/Talk LoRAs**
  - Context: Use custom mask to mask them out, this is how the LoRAs handle degradation
  - *From: Kijai*

- **Use standard prompts for QwenVL in Bindweave**
  - Context: Same prompt for both T5 and Qwen, not instructional system prompts
  - *From: Kijai*

- **Always use CPU for text encoding**
  - Context: General recommendation for resource management
  - *From: Lodis*

- **Use Grounded SAM for text-to-mask tasks**
  - Context: Most reliable for text to mask conversion
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Use Florence2 to mask out characters for Multitalk**
  - Context: For multi-character talking videos
  - *From: manu_le_surikhate_gamer*

- **Use audio without vocals for non-speaking character movement**
  - Context: When you want character to move but not speak
  - *From: Charlie*

- **Use median blur before Flash VSR to reduce sharpness**
  - Context: Flash VSR can be too sharp for video
  - *From: Elvaxorn*

- **Use high strength for svi-film lora**
  - Context: When using with hn model, set strength to 3 for visible effect
  - *From: lemuet*

- **Different gray values in Painter node create different motion**
  - Context: Values above 0.5 make result brighter, can adjust motion amplitude
  - *From: Kijai*

- **For I2V prompts should avoid specific subject names/gender**
  - Context: Makes prompt work better across different input images
  - *From: hicho*

- **Use VACE 2.1 with 2.2 models**
  - Context: Can rename 2.1 to 2.2 and use VACE, or use VACE 2.1 model + 2.2 low
  - *From: hicho*

- **LightX2V significantly speeds up WanAnimate**
  - Context: Without LightX, WanAnimate takes 40+ minutes; with LightX, 11 minutes for 8 steps
  - *From: Gleb Tretyak*

- **Use 4x latent + 1 rule for multi-keyframe approach**
  - Context: When placing intermediate keyframes in video generation
  - *From: mccoxmaul*

- **Use black frames for wrapper, gray for native implementations**
  - Context: When using null images in different Wan implementations
  - *From: Ablejones*

- **Masks are inverted between wrapper and native implementations**
  - Context: When converting workflows between implementations
  - *From: Ablejones*

- **Remove negative prompt from audio model for cleaner audio**
  - Context: When using Ovi model - connect text_embed instead of negative_text_embeds for better audio quality
  - *From: avataraim*

- **Use short video negative prompt for better audio quality**
  - Context: When using Ovi model with audio generation
  - *From: Kijai*

- **CFG scheduling still helps with new LightX2V LoRA**
  - Context: Use scheduled CFG on first step, sometimes second step for high motion cases
  - *From: lostintranslation*

- **Do lipsync separately for best results**
  - Context: Better to vid2vid with InfiniteTalk rather than trying to do everything in one pass
  - *From: Kijai*

- **Use GIMP or Photoshop for facial feature scaling**
  - Context: Better than trying to use DWPose for subtle facial adjustments
  - *From: metaphysician*

- **Use same rank for LightX2V LoRA on high and low samplers**
  - Context: Don't waste storage on different ranks
  - *From: hicho*

- **More detailed prompts can help maintain likeness in character replacement**
  - Context: Instead of just 'the man is speaking'
  - *From: burgstall*

- **For OVI audio, use 20 steps instead of 10 for better audio quality**
  - Context: 10 steps is risky for audio
  - *From: Hevi*

- **Use bindweave with actual box mask instead of full frame**
  - Context: Full mask gets washed out and motion suffers
  - *From: Kijai*

- **Include trigger word in training captions for character LoRAs**
  - Context: Needed for Wan Animate to recognize the person
  - *From: ingi // SYSTMS*

- **Don't mention clothing in captions if you want person wearing training data clothes**
  - Context: For character LoRA training
  - *From: ingi // SYSTMS*

- **Use larger generation sizes for better realism**
  - Context: Generation size is the single biggest factor for output quality, even makes motion better. Try 576x1024 or 720x1024 for 33 frames
  - *From: ingi // SYSTMS*

- **Add second sampler with low denoise for realism**
  - Context: Use low denoise around 0.2 with Wan 2.2 Low noise to help with plastic look
  - *From: ingi // SYSTMS*

- **Use higher shift for I2V**
  - Context: Guidelines for Wan i2v is shift 9. Lower shift tends to make things sharper, which can make things look less real
  - *From: ingi // SYSTMS*

- **Include person description in prompts**
  - Context: Using a super simple prompt rarely generates great outcome. Copy captions from training data and update what you want different
  - *From: ingi // SYSTMS*

- **Avoid extremely detailed reference images**
  - Context: Providing reference images with too much detail can contribute to artifacts. Qwen-generated reference images avoid this because they're soft and lack detail
  - *From: 42hub*

- **Crop reference faces to be larger with less wasted space**
  - Context: When using Wan Animate with small faces in reference images
  - *From: Kijai*

- **Run face detailer workflow separately rather than in the node chain**
  - Context: For improving small faces in generated videos
  - *From: ingi // SYSTMS*

- **Try different reference images as some work better than others**
  - Context: When struggling with likeness in Wan Animate
  - *From: hudson223*

- **Use AI Toolkit for training Wan LoRAs with good likeness results**
  - Context: For character training with Wan models
  - *From: Drommer-Kille*

- **Fixed seed is useful for seeing what changing values actually does**
  - Context: Using same starting point with different settings to understand parameter effects
  - *From: ingi // SYSTMS*

- **Use separate background and person/item instead of inpainting for TTM**
  - Context: Prevents double objects and artifacts when using cut and drag techniques
  - *From: avataraim*

- **Be careful with steps when using distill LoRAs and low steps**
  - Context: Not much room for error with these combinations in TTM
  - *From: Kijai*

- **Change seeds to solve VACE workflow inconsistencies**
  - Context: Random seed changes can solve inconsistencies with same prompt/image/parameters
  - *From: Stef*

- **Use 127 grey for inpainting masks with VACE**
  - Context: Still the default mask value even with new VACE implementation
  - *From: Kijai*

- **Reduce end step on TTM node to get more motion and follow prompts better**
  - Context: When you want the model to have more freedom to generate motion and follow movement prompts like wing flapping
  - *From: lemuet*

- **Use convert image to mask node with reference video for simple TTM usage**
  - Context: For basic camera movement replication, just pass reference video through convert image to mask node and connect to TTM mask input
  - *From: lemuet*

- **Mentioning specific car model in prompts helps with vehicle generation**
  - Context: When generating car scenes, being specific about the car model improves results
  - *From: FL13*

- **Prompting really helps with camera movements in TTM**
  - Context: Adding camera movement descriptions in prompts (like 'camera zoom') can help avoid unwanted effects like earth shaking
  - *From: hicho*

- **Always preview high noise render first**
  - Context: If high noise doesn't look reasonable, adjust prompt and settings before rerun
  - *From: Guey.KhalaMari*

- **No magical settings work for all scenarios**
  - Context: It's a game of tinkering, need to adjust for each use case
  - *From: Guey.KhalaMari*

- **Base animation should match prompt intentions**
  - Context: If prompting camera movement, base reference animation should support that
  - *From: Guey.KhalaMari*

- **Use LightX2V 1030 for high noise with I2V**
  - Context: Might be better than old version for high noise part
  - *From: FL13*

- **Graphics and color in motion signal video should match prompt**
  - Context: Visual consistency between input animation and desired output
  - *From: hicho*

- **Use detailed prompting with FFGO for better results**
  - Context: More descriptive prompts help prevent drift and improve object consistency
  - *From: Guey.KhalaMari*

- **Start FFGO prompts with specific trigger phrase**
  - Context: Begin with 'ad23r2 the camera view suddenly changes.' followed by detailed description
  - *From: Dever*

- **Use white background for FFGO reference subjects**
  - Context: Helps isolate references for better multi-subject generation
  - *From: Dever*

- **Use detailed burpee prompt for exercise animations**
  - Context: For fitness/exercise video generation with FFGO
  - *From: Guey.KhalaMari*

- **Close all other apps except ComfyUI for low VRAM setups**
  - Context: When running on limited 32GB RAM systems
  - *From: Tony(5090)*

- **Start with low settings and gradually increase to find limits**
  - Context: For users with limited hardware resources
  - *From: garbus*

- **Use last frame for video extension**
  - Context: Take the last frame of a video and do img2vid for extension
  - *From: buttercup5108*

- **Use overscan composition technique with TTM**
  - Context: Animate everything in overscan frame then crop in post so characters can enter from off-screen
  - *From: chrisd0073*

- **Reference frames help preserve character consistency**
  - Context: Even if reference doesn't match motion sequence, wan 'remembers' character appearance from that frame
  - *From: lemuet*

- **TTM works best with I2V models**
  - Context: Using with T2V changes background too much
  - *From: Kijai*

- **Prompting becomes more important with soft-looking subjects**
  - Context: When subject is soft, there's too much room for interpretation on low noise
  - *From: Guey.KhalaMari*

- **For testing TTM workflow without TTM, plug encoded latent into first sampler instead of TTM node**
  - Context: When wanting to quickly test v2v approach
  - *From: lemuet*

- **Describing characters in prompt is important for reference consistency**
  - Context: When using character references in video generation
  - *From: xwsswww*

- **Create first frame with character already placed in scene**
  - Context: For better expression transfer and character consistency
  - *From: Valle*

- **Use Qwen Image Edit for placing characters in scenes**
  - Context: Good for consistency and lighting adjustment
  - *From: Valle*

- **Second pass with T2V LOW model at low denoise (0.2) can fix shading issues**
  - Context: When output has incorrect shading compared to source
  - *From: Juan Gea*

- **Work backwards for shots where subject enters/exits frame**
  - Context: Only works on simple shots, not multiple entries/exits
  - *From: David Snow*

- **LightX2V usually goes last in LoRA chain**
  - Context: Has more dramatic overall effect
  - *From: metaphysician*

- **Use 2.1 VACE then last few steps with 2.2 low noise if you have depth**
  - Context: When you have depth control available
  - *From: spacepxl*

- **Use Qwen Edit workflow to create correct first frame with character placed in scene**
  - Context: When animating characters to avoid disappointment with Wan's character interpretation
  - *From: Valle*

- **Turn up CLIP vision embed strength and lower pose control settings for better character consistency**
  - Context: When trying to maintain character likeness in animations
  - *From: Flipping Sigmas*

- **Use character reference images for better stability in complex scenes**
  - Context: When generating videos with multiple characters or complex movements
  - *From: Scruffy*

- **Set frame_window_size to frame_count or multiple to avoid hallucination**
  - Context: When input video finishes but Wan continues generating
  - *From: Guus*

- **Use masks when upscaling to only sharpen desired areas**
  - Context: To avoid tile upscalers injecting unnecessary detail in backgrounds
  - *From: dj47*

- **Use MOE as a restrainer with 480p LoRA**
  - Context: Keeps motion aligned with prompt while staying more expressive than MOE alone, prevents quality loss and fading
  - *From: GWX-Reloaded*

- **Use depthmap as mask for selective processing**
  - Context: More accurate than regular masks, can select focal point from depth map then create mask based on it
  - *From: David Snow*

- **Stack multiple LoRAs for better control**
  - Context: Can use MOE high noise at 1, Lightx2v 480p rank 256 at 3, and Wan 2.1 at 0.30 for controlled motion without fading
  - *From: GWX-Reloaded*

- **Test block swap settings systematically**
  - Context: Set to 30, try target resolution, then reduce by 5 until OOM - previous value is your sweet spot
  - *From: Scruffy*

- **Read model documentation for memory fixes**
  - Context: Solutions like triton cache clearing are documented in readmes but people don't read them
  - *From: Kijai*

- **Use JSON structured prompting for more precise results**
  - Context: Format prompts with clear subject, camera, composition sections for better control
  - *From: Scruffy*

- **Avoid denoise parameter, use direct step control instead**
  - Context: Both native and wrapper - use KSamplerAdvanced or set steps/start_step/end_step directly
  - *From: 42hub*

- **For VRAM optimization, keep as many blocks in VRAM as possible without exceeding limit**
  - Context: More blocks in VRAM = faster inference, but don't go over your card's VRAM
  - *From: Kagi*

- **Prompt VACE 2.2 like instructing a literal person who only watched YouTube/Netflix**
  - Context: When using Fun Vace 2.2 model, be very explicit and descriptive
  - *From: Ablejones*

- **For object replacement without masking everything, use canny/depth controlnet with strength experimentation**
  - Context: When you need many pixels to change but want to preserve motion physics
  - *From: Ablejones*

- **Use high/low noise split for better results**
  - Context: For most camera movements, only need lora for high noise as low will pick up existing movement from high pass generation
  - *From: NebSH*

- **Don't use Vace reference for style transfer**
  - Context: Vace reference is for background, setting, or subjects - not a style-transfer model even if occasionally works
  - *From: Ablejones*

- **Use Phantom+Vace combination for character work**
  - Context: When character reference doesn't exactly match first frame position, combine Phantom with Vace for better results
  - *From: Ablejones*

- **Skip HN stage when using Phantom**
  - Context: Phantom only works with LN part, can skip HN stage completely or make HN output look close enough to target references
  - *From: Ablejones*

- **Use chunked rope and pytorch RMS norm instead of compile**
  - Context: Reduces VRAM usage without the compilation overhead and instability
  - *From: Kijai*

- **Train control lora for proper latent upscaling**
  - Context: Instead of interpolating latents, train diffusion model to synthesize missing information
  - *From: spacepxl*

- **Include as much as possible in one compile graph**
  - Context: Better than having multiple separate compiled sections
  - *From: Kijai*

- **Use del, gc.collect(), and torch.cuda.empty_cache() together**
  - Context: To actually flush tensors completely, though this slows things down if done every block
  - *From: spacepxl*

- **Use disable smart memory for heavy workloads**
  - Context: Always offloads but slows down lightweight tasks
  - *From: spacepxl*


## News & Updates

- **EMU 3.5 released - 34B truly native multimodal autoregressive model**
  - Beats all SOTA Image Gen and Image Edit models on benchmarks, has both T2I and X2I versions
  - *From: shaggss*

- **VAP (Video-as-Prompt) implementation pushed to test branch**
  - Early implementation, probably buggy, requires 8GB extra at bf16, doubles sequence length for self attention
  - *From: Kijai*

- **LongCat is now available in main branch**
  - Available for few days in the main wrapper branch
  - *From: Kijai*

- **Fill's node pack stream planned for November 11th**
  - Will showcase hidden gems and tools in the expanded node pack
  - *From: Fill*

- **Kijai uploaded VAP weights**
  - Still in testing phase, not yet in main branch
  - *From: Lodis*

- **New LightX LoRAs released but causing random zooms**
  - Newer versions better in some ways but cause unexpected zoom behavior vs pre-1022 and 1030 versions
  - *From: blake37*

- **Video-As-Prompt branch available from Kijai**
  - Text prompt still needed to make it work well, mixed results reported
  - *From: JohnDopamine*

- **Meta upgraded image and video generation, partnered with Midjourney**
  - Available at meta.ai, has rate limits and safeguards
  - *From: 🦙rishappi*

- **CamCloneMaster released**
  - New V2V camera motion transfer model from KwaiVGI, supports video to video motion transfer
  - *From: Kijai*

- **Fill created path editor for ATI**
  - New node with timing control for trajectory paths in ATI model
  - *From: Fill*

- **Flash VSR v1.1 was made private**
  - Was a beta version that got pulled by the creator
  - *From: yi*

- **BindWeave weights released**
  - ByteDance released Wan 2.1 based subject-consistent video generation model on HuggingFace
  - *From: ZeusZeus (RTX 4090)*

- **Video-as-prompt feature fixed**
  - Logic error resolved, works with cfg now but still needs good prompts to be useful
  - *From: Kijai*

- **New LightX2V 2.2 LoRAs released**
  - Only high noise version updated, low noise unchanged. Available through HuggingFace
  - *From: Doctor Shotgun*

- **Wan official retweeted community content**
  - Alibaba Wan account retweeted community generated content
  - *From: JohnDopamine*

- **Phantom team possibly acquired by ByteDance**
  - Phantom developer's GitHub profile showing ByteDance affiliation
  - *From: JohnDopamine*

- **FlashVSR 1.1 released**
  - Enhanced stability + fidelity improvements over previous version
  - *From: DawnII*

- **LTX mentioned end of November release in their Discord**
  - Official timeframe mentioned in LTX Discord for model release
  - *From: Stad*

- **LTX 2 specifications confirmed: 20 seconds, 4K, 50 fps**
  - Official specs confirmed in their Discord/social accounts
  - *From: ZeusZeus*

- **UniAVGen released built on Wan 5B and 1.3B models**
  - New model architecture using Wan as base
  - *From: DawnII*

- **Holocine available in WanVideoWrapper via PR**
  - Need to install specific PR #1615 to use Holocine
  - *From: BNP4535353*

- **Lumos-Custom relight model released**
  - Uses Wan and Qwen VL for relighting
  - *From: hicho*

- **InfinityStar 8B video model from ByteDance lab**
  - Autoregressive architecture, supports T2I, T2V, I2V, and long-duration video synthesis
  - *From: yi*

- **BindWeave by ByteDance for subject-consistent video**
  - New model for character consistency in video generation
  - *From: Dream Making*

- **Sage fix available in KJNodes nightly**
  - Fix is in main branch but not in versioned release yet
  - *From: Kijai*

- **InfinityStar 8B video model released**
  - New autoregressive video model from FoundationVision team, same team that made Waver from Bytedance
  - *From: Ada*

- **FlashVSR updated to version 1.1**
  - Fixed bug about dropping last few frames, but added new memory leak issues and frame misalignment bugs
  - *From: lostintranslation*

- **LTX2 open source release scheduled for end of month**
  - LTX2 models will be open sourced by end of January
  - *From: Kiwv*

- **SeedVR2 ComfyUI integration updated after 4 months**
  - New version with updated CLI tool for batch processing, available in ComfyUI Manager
  - *From: Adrien Toupet*

- **Self-forcing Wan2.2 14B model available**
  - Unofficial release from FastVideo team, might be better than LightX2V for Wan2.1
  - *From: yi*

- **ComfyUI Vue UI now default**
  - New UI is deployed by default on latest version, has opt-out option
  - *From: ˗ˏˋ⚡ˎˊ-*

- **LightX2V T2V Seko v2.0 released**
  - New 4-step distillation using Phased DMD technique
  - *From: JohnDopamine*

- **Lucy Edit 1.1 Dev released**
  - Based on 5B model, has fp16 version available
  - *From: DawnII*

- **New cinematic quick cuts LoRA released**
  - Scene cut LoRA for enhancing cut scenes in Wan
  - *From: DawnII*

- **Lumos-Custom released for background swapping**
  - Background swapping with accurate lighting
  - *From: Shubhooooo*

- **Ovi 1.1 released with 10-second generation**
  - Simplified audio tags, new 5-second base model at 960x960p, 10-second uses bidirectional dense attention
  - *From: Juampab12*

- **New Lumos-Custom model from Alibaba**
  - 1.3B model with 48 input channels for noise + foreground + background video, similar to IC light
  - *From: slmonker(5090D 32GB)*

- **Ovi 1.1 released with 960x960x10 seconds capability**
  - New version can handle 960x960 resolution for 10 second videos, dataset is twice as large
  - *From: Thom293*

- **Kijai updated code to use Ovi models directly without extra model**
  - Can now use the models directly without needing the additional audio model component
  - *From: Kijai*

- **ChronoEdit-14B-Diffusers-Upscaler-Lora released**
  - NVIDIA released an upscaler LoRA that might be usable to upscale normal Wan images
  - *From: yi*

- **Audio negative prompt bug fixed in WanVideoWrapper**
  - Node updated to properly handle negative prompts, made input optional, added logging to show which negative is used
  - *From: Kijai*

- **New audio description format**
  - Old format was <AUDCAP>...<ENDAUDCAP>, new format is Audio:...
  - *From: Hashu*

- **Kijai added 10s workflow in last commit**
  - For OVI 1.1 10-second model
  - *From: Kijai*

- **New Infinitystar model released**
  - No ComfyUI integration exists yet
  - *From: ZeusZeus (RTX 4090)*

- **xDiT finally released ComfyUI node**
  - For distributed inference
  - *From: Juampab12*

- **Kandinsky 5.0 I2V Pro model released**
  - 20B parameter model with I2V version out on HuggingFace, uses Qwen2.5 as text encoder, VAE reused from Hyv, supports 24fps
  - *From: multiple users*

- **New LightX2V 4-step distill (1030) for high noise**
  - Recent release of new LightX2V LoRA specifically for high noise expert
  - *From: patientx*

- **Kijai to replace bindweave scaled with version that has scale key**
  - Will replace scaled version but won't scale layers it doesn't expect for now, will ask comfy if mixed precision can work
  - *From: Kijai*

- **Kijai merged the wrapper Bindweave branch to main**
  - Still needs example workflow to be created
  - *From: Kijai*

- **Kandinsky 5.0 T2V Pro models released with both I2V and T2V 5sec versions**
  - Open source models available on HuggingFace
  - *From: 42hub*

- **Depth Anything 3 released**
  - New version available but seems focused on 3D accuracy rather than 2D depth map quality
  - *From: A.I.Warper*

- **LightX2V team adding new features**
  - New commits showing additional functionality being developed
  - *From: hicho*

- **TTM (Time to Move) technique implemented in ComfyUI**
  - Kijai has implemented TTM as a ComfyUI node for cut and drag animation control
  - *From: Kijai*

- **DepthAnything V3 released**
  - V3 requires inversion for ControlNets, unlike V2
  - *From: Drommer-Kille*

- **UniVid model released**
  - New model for unifying vision tasks with pre-trained video generation, appears to be LoRA-based
  - *From: JohnDopamine*

- **TimeToMove (TTM) workflow added to WanVideo wrapper**
  - New example workflow available in wrapper's example folder demonstrating how to use TTM for camera motion and object movement
  - *From: lemuet*

- **ComfyUI update makes LatentCompositeMasked work with basic video latents**
  - Recent ComfyUI update by comfyanonymous improves video latent handling
  - *From: xwsswww*

- **SAM3 released**
  - New segmentation model from Facebook, supports video segmentation and 3D object detection
  - *From: Lodis*

- **CausalWan 2.2 I2V A14B Preview released**
  - 50gb+ model containing both experts, autoregressive architecture for potentially long generation
  - *From: JohnDopamine*

- **Hunyuan 8B video model coming tomorrow**
  - New video model similar to Wan2.1-2.2 but only 8B parameters
  - *From: slmonker(5090D 32GB)*

- **Music video created with WAN for Dimitri Vegas/David Guetta/Loreen**
  - Professional music video production using WAN extensively, EP'd by Neill Blomkamp
  - *From: Ruairi Robinson*

- **HunyuanVideo 1.5 release imminent**
  - Tencent announced upcoming release, model reportedly between Wan 2.1 and 2.2 quality, around 8B parameters
  - *From: yi*

- **FFGO LoRA released for Wan 2.2**
  - Enables multiple subject video generation with camera view changes
  - *From: Kijai*

- **HunyuanVideo 1.5 released**
  - 8B model, 24fps, faster than Wan, not censored, doesn't know celebrities
  - *From: JohnDopamine*

- **Kijai completed native ComfyUI implementation**
  - Native ComfyUI implementation for Wan models completed by Kijai
  - *From: Kijai*

- **David Snow returns after 4 month absence**
  - Community member returns, missed Wan 2.2 release entirely
  - *From: David Snow*

- **Native TTM for testing released**
  - Kijai released native TTM implementation that wraps functionality to allow ending noise injection
  - *From: Kijai*

- **ComfyUI team warns about harmful Block Swap node**
  - Someone made native version that screws up memory management and causes crashes after latest ComfyUI updates. Wrapper version is fine.
  - *From: Kijai*

- **FL13 improved tiled upscaler scripts**
  - Fixed bugs when using more than 2 tiles
  - *From: FL13*

- **SteadyDancer-14B released for Wan 2.1**
  - New tool for Wan 2.1, went public recently
  - *From: DawnII*

- **Playmate2 released**
  - Uses Wan 2.1 I2V with VideoLLaMA3-7B, similar to InfiniteTalk with advantages in facial expression diversity
  - *From: Kijai*

- **LTX 2 release confirmed delayed**
  - No later than December according to confirmation
  - *From: ZeusZeus (RTX 4090)*

- **Flux.2-dev released**
  - T2I and edit model with multi ref editing, up to 4MP resolution, but uses non-commercial license
  - *From: shaggss*

- **SteadyDancer paper and project page released**
  - Uses Wan2.1 as base model for dance generation
  - *From: slmonker*

- **Alibaba stock jumps after strong cloud growth**
  - Good news for future Wan models as cloud performance correlates with model releases
  - *From: pom*

- **SteadyDancer-14B implementation in progress**
  - Kijai working on implementation with pose detector, pose alignment - complex with many new inputs but might be compatible with other models
  - *From: Kijai*

- **Tile LoRA v1.1 released**
  - Trained on wider variety of sizes/frames, fixes artifacts v1.0 had with few frames or high res
  - *From: spacepxl*

- **Z-image-turbo claims to beat SDXL and Flux**
  - Supposedly generates in 10 seconds on smaller GPUs, 2-3 seconds on larger ones
  - *From: GWX-Reloaded*

- **SteadyDancer implementation added to test branch**
  - Available at ComfyUI-WanVideoWrapper steadydancer branch, pose detector and aligner still need implementation
  - *From: Kijai*

- **Hard cut Wan LoRA v3 released**
  - Available on HuggingFace at neph1/hard_cut_wan_lora
  - *From: DawnII*

- **Cinematic Fast Cutting LoRA available**
  - Previously Quick Cuts, multiple interesting LoRAs by neph1 on Civitai
  - *From: NebSH*

- **New latent upscale model released**
  - Basic latent upscale model using VAE training components, 2x spatial upscale for images and video, huge improvement over bilinear/bislerp
  - *From: spacepxl*

- **AE Animation node fork with English UI**
  - Full English UI + new Flip H/V & Scale X/Y features, useful for TTM
  - *From: Vérole*

- **Torch.compile memory issues identified**
  - Windows-specific issue where compilation uses excessive VRAM due to tensor stacking from graph breaks
  - *From: Kijai*

- **Memory optimizations found in wrapper model code**
  - Found numerous intermediate tensors that could be freed, got overall memory usage down significantly
  - *From: Kijai*

- **WanVideoWrapper memory optimizations released**
  - Fixed torch.compile graph break issues, reduced VRAM usage, integrated SteadyDancer
  - *From: Kijai*

- **Native ComfyUI optimizations enabled by default**
  - Pinned memory and async offloading optimizations now enabled, aimed at speeding up offloading
  - *From: Kijai*

- **Context windows PR working with concat latent controls**
  - Native context windows implementation now supports concat latent controls with nearly invisible blends
  - *From: spacepxl*


## Workflows & Use Cases

- **ATI UI integration with trajectory tracking and motion transfer**
  - Use case: Creating controlled camera movements and object trajectories with preset animations like spins and waves
  - *From: Fill*

- **HuMo I2V with custom embeds for lip-sync**
  - Use case: Audio-reactive video generation with character consistency using reference images and audio
  - *From: Ablejones*

- **FFLF extension using VACE with blank grey frames**
  - Use case: Extended T2V generation by feeding blank frames to VACE for longer sequences
  - *From: The Shadow (NYC)*

- **FlashVSR multi-step upscaling for single images**
  - Use case: Upscaling images through multiple FlashVSR passes (1 step, 4 steps, 8 steps)
  - *From: patientx*

- **Using end frames as start frames with masks for extensions**
  - *From: mdkb*

- **VACE for clip extension by injecting frames**
  - *From: mdkb*

- **Save latent to disk between samplers for memory management**
  - *From: lemuet*

- **Basic Wan Animate at 1920x1080**
  - Use case: High quality character animation without masking
  - *From: Fill*

- **Wan Animate with masking and transform**
  - Use case: Character pose editing with expanded mask to reduce image shake
  - *From: enigmatic_e*

- **ATI with trajectory control**
  - Use case: Subtle character animations like breathing and swaying
  - *From: Fill*

- **Wan Animate with point trajectory control**
  - Use case: Animating objects along specific paths, not just dance movements
  - *From: Gleb Tretyak*

- **First-to-last frame control with background preservation**
  - Use case: Character animation while preserving background text/elements
  - *From: Gleb Tretyak*

- **Blender mesh to grease pencil for control**
  - Use case: Creating animation control inputs using Blender's grease pencil system
  - *From: Blink*

- **Separate character generation for multi-character scenes**
  - Use case: Create characters separately on clean background, composite later for Street Fighter style animations
  - *From: Valle*

- **Storyboard to video using Qwen edit + Wan 2.2**
  - Use case: Creating longer videos by generating keyframes with Qwen edit, then using Wan 2.2 I2V for frame-to-frame animation
  - *From: avataraim*

- **Hard cut transitions using Cinematic Hard Cut v2 LoRA**
  - Use case: Creating scene transitions by using Qwen edit for second scene, then applying as final image for I2V with hard cut LoRA
  - *From: Ablejones*

- **Multi-reference BindWeaver setup**
  - Use case: Using up to 4 reference images concatenated to front of I2V channel for enhanced control
  - *From: Kijai*

- **720p 370 frames generation**
  - Use case: Long video generation took 1 hour
  - *From: BNP4535353*

- **Infinite duration loop with frame overlap**
  - Use case: Smooth long video generation with frame concatenation
  - *From: Gleb Tretyak*

- **Audio reactive coordinates for ATI/VACE/WanAnimate**
  - Use case: Modified class to get red dots in mask areas that react to audio
  - *From: yukass*

- **InfiniteTalk group dialog workflow**
  - Use case: Creating multi-speaker conversations up to 4 people using pyannote for speaker diarization, works up to 2 minute dialogs
  - *From: manu_le_surikhate_gamer*

- **Bindweave multi-reference workflow**
  - Use case: Using multiple reference images for consistent character generation with proper masking and positioning
  - *From: Kijai*

- **Bindweave with character separation for MultiTalk/InfiniteTalk**
  - Use case: Preparing characters that don't overlap for lip-sync processing
  - *From: manu_le_surikhate_gamer*

- **Using SeC-4B masking with Wan Animate**
  - Use case: Getting tighter masks for better facial expressions and hand movements
  - *From: LookingGlass*

- **Using Wan 2.2 low-noise as refiner**
  - Use case: Refine any T2I model output, works with SD1.5 to remove flicker
  - *From: slmonker(5090D 32GB)*

- **Multi-character Multitalk setup**
  - Use case: 2+ characters talking/listening with individual audio tracks and masks
  - *From: avataraim*

- **Video chunk processing for VRAM limitations**
  - Use case: Split videos over 81 frames into chunks, process, then recombine
  - *From: lostintranslation*

- **Using WanAnimate with start/end frame and trajectory input**
  - Use case: Creating transitions between reference images with trajectory guidance
  - *From: Gleb Tretyak*

- **Painter I2V for motion enhancement**
  - Use case: Adding motion to I2V by manipulating gray frame values with motion amplitude
  - *From: Kijai*

- **FlashVSR with tiled processing**
  - Use case: Upscaling longer videos using built-in tiled processing instead of chunking
  - *From: lostintranslation*

- **Wan Animate with first frame, last frame, trajectory and reference**
  - Use case: Advanced video generation with multiple control inputs
  - *From: Gleb Tretyak*

- **Using SAM2 to mask person + bindweave v2v with character masking**
  - Use case: Character-focused video-to-video generation with identity preservation
  - *From: Juampab12*

- **Multi-scene WanAnimate with scene detection**
  - Use case: Automatically processing videos with multiple scenes using scenedetect node
  - *From: burgstall*

- **Phantom + VACE + WanAnimate + Inpainting pipeline**
  - Use case: Use VACE+phantom for multi-subject videos, WanAnimate for motion refinement with cropped inpainting, then inpaint faces and voice match with HuMO/InfiniteTalk
  - *From: Ablejones*

- **Automated multi-scene WanAnimate character replacement**
  - Use case: Character replacement in videos
  - *From: burgstall*

- **Using SAM2 segmentation with Wan Animate**
  - Use case: Automatic character segmentation for animation
  - *From: boorayjenkins*

- **Bindweave working on native ComfyUI**
  - Use case: I2V generation with reference consistency
  - *From: Ablejones*

- **Repeat batch with mask for background preservation**
  - Use case: Let Wan Animate model know to use BG from input ref image
  - *From: hicho*

- **Multiple ksampler approach over looping**
  - Use case: Better results than single ksampler loop for long video generation
  - *From: hicho*

- **Two-stage sampling for realism**
  - Use case: Add second sampler with low denoise (0.2) using Wan 2.2 Low noise to improve plastic look
  - *From: ingi // SYSTMS*

- **Face detailer workflow for improving video faces**
  - Use case: Enhancing small or poor quality faces in generated videos
  - *From: ingi // SYSTMS*

- **T2V followed by long video generation from last frame**
  - Use case: Creating extended 10+ second videos by chaining generation
  - *From: hicho*

- **Using WanAnimate with disconnected face input for non-human characters**
  - Use case: Animating characters without forcing human facial features
  - *From: Charlie*

- **TTM cut and drag animation**
  - Use case: Creating controlled object movement and camera effects in videos using masks and motion vectors
  - *From: Kijai*

- **Using TTM with I2V for background consistency**
  - Use case: Maintaining consistent backgrounds and subjects while applying motion control
  - *From: Kijai*

- **Camera control effects with TTM**
  - Use case: Creating zoom, rotation and camera movement effects that can't be achieved with prompts alone
  - *From: hicho*

- **TTM with 3D animation pipeline using MoGe2 and Blender**
  - Use case: Creating controlled camera movements by generating 3D scene from single image, animating camera in Blender, then using TTM to transfer motion
  - *From: lemuet*

- **MS Paint recording for TTM mask creation**
  - Use case: Recording drawing/painting in MS Paint to create animated masks for TTM motion control
  - *From: hicho*

- **Dual sampling setup with 3 samplers for speed optimization**
  - Use case: 1 step at cfg 3.5, then remaining steps with cfg 1 for faster inference while maintaining quality
  - *From: FL13*

- **3 sampler setup for TTM**
  - Use case: Better motion quality - first sampler 1 step high noise cfg 3.5 no lora, second sampler high noise cfg 1 with lightx2v, third sampler low noise with lora
  - *From: PeroBueno*

- **TTM with 3D animations from Blender**
  - Use case: Using TTM with Blender rough animations for lighting fixes and object interactions
  - *From: xwsswww*

- **Sequential character animation**
  - Use case: Animate one character then reprocess video for second character
  - *From: 42hub*

- **FFGO multi-subject I2V with Wan 2.2**
  - Use case: Generate videos with multiple subjects/objects using reference images on white background
  - *From: Dever*

- **TTM + Uni3C combination**
  - Use case: Camera control with motion transfer for enhanced results
  - *From: Kijai*

- **Krita + SAM2 + TTM for object animation**
  - Use case: Create animated sequences by masking and moving objects in Krita, then processing with TTM
  - *From: hicho*

- **FFGO character consistency loop**
  - Use case: Maintaining character consistency and battling degradation in I2V workflow by using last frame and adding to reference
  - *From: eraxor_*

- **TTM with keyframes for animated characters**
  - Use case: Adding keyframes for more control in character animation
  - *From: Guey.KhalaMari*

- **Animation interpolation system**
  - Use case: Animate at 1fps and interpolate with TTM/FFGO for keyframe-based animation
  - *From: Juampab12*

- **3 sampler method for Wan 2.2**
  - Use case: Better motion quality. Use lightx2v 1030 on high, old 2.1 lightx2v rank64 on low. Switch at sigma 0.9
  - *From: FL13*

- **TTM with overscan composition**
  - Use case: Preserving environment and allowing characters to enter from off-frame
  - *From: Guey.KhalaMari*

- **Tiled upscaling for wan i2v**
  - Use case: Upscaling to 2K/4K resolution without VRAM limits, reduces seams significantly
  - *From: FL13*

- **V2V with reference frames**
  - Use case: Character consistency without TTM or FFGO, edit out reference at start after output
  - *From: lemuet*

- **V2V without TTM using direct latent input**
  - Use case: Alternative to TTM for video-to-video generation
  - *From: lemuet*

- **Reference frame insertion for character consistency**
  - Use case: Maintaining character appearance across video using 4-frame block rule
  - *From: lemuet*

- **WanAnimate without background/mask for style transfer**
  - Use case: Better results when not using background from driving video
  - *From: 42hub*

- **T2V + VACE for video extension**
  - Use case: First generate with T2V then extend with I2V using different prompts
  - *From: 42hub*

- **Two-pass character animation with Qwen Edit**
  - Use case: First create character-in-scene frame with Qwen Edit, then animate to ensure character looks correct
  - *From: Valle*

- **JSON-driven video generation with detailed prompts**
  - Use case: Using LLMs to generate second-by-second detailed prompts for complex action sequences
  - *From: Scruffy*

- **RGB video as Fun Control input**
  - Use case: Feed storyboards or drawings directly as RGB control without preprocessors for motion guidance
  - *From: Hashu*

- **Depth-based selective upscaling**
  - Use case: Upscaling videos while preventing unwanted background detail addition
  - *From: David Snow*

- **Multi-LoRA stacking for motion control**
  - Use case: Using MOE + 480p LoRA + Wan 2.1 LoRA on different noise levels for controlled animation
  - *From: GWX-Reloaded*

- **Sequential model loading for larger capacity**
  - Use case: Since Wan 2.2 runs high/low noise sequentially, can potentially use larger models for each stage
  - *From: metaphysician*

- **Multiple reference images with Wan MoCha**
  - Use case: Using 1 full body + 1 closeup reference, 30+ shots rendered with 1-2 takes max per shot
  - *From: Guey.KhalaMari*

- **Tiled upscaling with VACE controls using Impact Pack Detailer**
  - Use case: High resolution video upscaling while maintaining subject identity with Phantom references
  - *From: Ablejones*

- **Face detailing during generation using HuMo**
  - Use case: Crop and expand faces to specified pixel size during video generation for better facial detail
  - *From: Ablejones*

- **1.3B tile + 2.2 low noise with split ksamplers**
  - Use case: Clean upscaling results by combining different model strengths
  - *From: spacepxl*

- **Using depth mask with canny for selective control**
  - Use case: Create binary mask to mask out object details while keeping outlines, allows volume changes while preserving silhouettes
  - *From: Ablejones*

- **Multi-reference Phantom setup**
  - Use case: Use up to 3 Phantom references for character consistency, likely 1 reference per subject
  - *From: Ablejones*

- **Separate control inputs for skeleton and depth**
  - Use case: Chain WanVaceToVideo nodes or use WanVacePhantomDualV2 for multiple control types without blending artifacts
  - *From: Ablejones*

- **Z-image with SD upscaler for 8K images**
  - Use case: Achieved 8K upscaling with subtle detail addition that was missing from 2K original
  - *From: Scruffy*

- **Using context windows with concat latent controls**
  - Use case: Video generation with tile control lora, 1 step of 2.2 low variant
  - *From: spacepxl*


## Recommended Settings

- **Wan 2.2 Lightx2v steps**: 4 steps on HN, total 7 steps
  - Working configuration for I2V
  - *From: Atlas*

- **dasiwaWAN22 steps**: 4 steps total
  - Good movement with faster inference
  - *From: asd*

- **HuMo resolution**: 720p
  - HuMo works better at higher resolution
  - *From: Ablejones*

- **VAP frame count**: 49 frames
  - Original code limitation, hardcoded frame count
  - *From: Kijai*

- **SVI-film LoRA strength**: hn:3, ln:1
  - Helps reduce color shifting in video extensions
  - *From: lemuet*

- **Blockswap**: 40
  - For memory management, can be increased further if needed
  - *From: Quality_Control*

- **Resolution for fighting/fast motion**: 1280x720
  - User generates at this resolution for physical fighting moves
  - *From: metaphysician*

- **UniC3 strength with Wan 2.2**: 3-5
  - Need higher strength for UniC3 to work with 2.2 models vs 2.1
  - *From: Kijai*

- **Block swap usage**: 20-25
  - Balance between memory usage and performance for 4090
  - *From: Kijai*

- **torch_dynamo_resume_in_forward**: false
  - Setting to true can cause bugs, keep false for stability
  - *From: Kijai*

- **attention_mode**: sdpa
  - Fixes Longcat reference dropping issues
  - *From: Hashu*

- **MPS LoRA strength**: 1.0 in high model
  - Improves prompt adherence, better than HPS
  - *From: Juampab12*

- **torch.compile dynamic**: True if works
  - Prevents unnecessary recompiles
  - *From: Ablejones*

- **video generation steps**: 30 steps with fp8_scaled
  - Better results than 50 steps bf16
  - *From: Kijai*

- **CFG for Wan without lightx LoRAs**: 4
  - Compensates for removal of lightx LoRAs
  - *From: Kiwv*

- **Motion frames for Wan animate**: 17 instead of 16
  - 17 frames continue without hitching compared to 16
  - *From: DawnII*

- **Best motion frames for SVI workflow**: 5
  - Gives best results according to testing
  - *From: DawnII*

- **LightX2V LoRA strength with 1030 model**: 1.0 with CFG
  - 1030 model works better with CFG enabled
  - *From: Kijai*

- **fun_or_fl2v_model**: enabled
  - Keep enabled for anything but basic 2.1 I2V when using end frame
  - *From: Kijai*

- **Lighting lora + 30 steps**: 30 steps
  - Gets a lot of details despite odd setup
  - *From: Dream Making*

- **Full precision fp16**: fp16
  - Used on both model and text encoder for testing
  - *From: Dream Making*

- **QwenVL image resize**: 0.3 or 0.75 scale
  - Based on resolution threshold for better results
  - *From: Kijai*

- **FlashVSR tile size**: 256 or below
  - 288 and higher cause memory leaks
  - *From: lostintranslation*

- **ComfyUI reserve VRAM**: 2GB
  - Helps with VRAM issues on lower resolutions
  - *From: Kijai*

- **Bindweave steps with LightX2V**: 6 steps
  - Achieves good results with lightning LoRA
  - *From: Kijai*

- **QwenVL image resolution**: Lowest resolution
  - As per original Bindweave implementation
  - *From: Kijai*

- **System prompt for QwenVL**: You are a helpful assistant
  - Original Bindweave uses basic system prompt, not Qwen edit template
  - *From: Kijai*

- **ComfyUI launch args for memory issues**: --disable-pinned-memory --reserve-vram 2
  - Fixes memory leaks and OOM issues in recent ComfyUI versions
  - *From: Gleb Tretyak*

- **Denoise value for Wan 2.2 low-noise refiner**: 0.2
  - Optimal for refining images
  - *From: slmonker(5090D 32GB)*

- **Sampler/scheduler for Wan 2.2 refiner**: euler+simple
  - Works well with ComfyUI native workflow
  - *From: slmonker(5090D 32GB)*

- **Flash VSR 1.1 settings**: Tiny mode with ultra fast nodes
  - Less VRAM hungry option
  - *From: Elvaxorn*

- **svi-film lora strength**: 3
  - Required for visible effect with hn model
  - *From: lemuet*

- **Painter node gray value**: 0.6
  - Good balance for motion without excessive brightness
  - *From: Kijai*

- **FlashVSR tile processing**: 4x288x288 tiles
  - Avoids memory leak compared to 9 tiles at 256 size
  - *From: lostintranslation*

- **WanAnimate continue_motion_max_frames**: 1 or 5
  - Only available choices in original code, wrapper always uses 1
  - *From: Kijai*

- **Audio CFG**: 8.0
  - Fixes gibberish output in Ovi model
  - *From: Kijai*

- **SLG**: 7, 8, 9
  - Required for prompt to work with specific images, though ruins image quality
  - *From: Kijai*

- **VACE white level**: 0 (black)
  - Eliminates awful noise at end of generations compared to gray (0.5)
  - *From: Gleb Tretyak*

- **Ovi 10s model frames**: 241 video frames, 314 audio frames
  - Required frame counts for 10 second Ovi model
  - *From: Hashu*

- **Command line args for memory issues**: --reserve-vram 2 --max-upload-size 500 --async-offload --use-sage-attention --fast fp16_accumulation
  - Helps resolve CUDA OOM issues
  - *From: Gleb Tretyak*

- **CFG for FastWan LoRA**: 1.5-2.0 with 10-20 steps
  - CFG 1.0 gives poor results, higher values work better
  - *From: Hashu*

- **Steps for distill LoRAs with audio**: 20 steps minimum
  - Audio goes crazy with too few steps on distill LoRAs, no distill available for audio model
  - *From: Kijai*

- **Lynx reference image size**: Avoid full resolution
  - Works with any size technically but doesn't perform well with very large images
  - *From: Kijai*

- **FastWan I2V**: 0.5 strength, 10 steps, CFG 2.0
  - Sweet spot for speed+quality
  - *From: Hevi*

- **OVI I2V**: FastWan 0.5, 10 steps, CFG 4, OVI audio CFG 3, shift 5, euler
  - User configuration
  - *From: PeroBueno*

- **OVI I2V CFG**: 1.5
  - Recommended over 4.0
  - *From: avataraim*

- **FastWan I2V optimal**: cfg 1.5, 10 steps, 720p
  - Optimal results found
  - *From: ZeusZeus (RTX 4090)*

- **Wan Animate LoRA training**: Rank 32, 4k+ steps, 720p images
  - Better than rank 64, prevents affecting entire image+motion too much
  - *From: ingi // SYSTMS*

- **LoRA strengths**: 1.0 for relight and lightx, 0.7-0.75 for likeness loras
  - Recommended values
  - *From: ingi // SYSTMS*

- **LightX2V strength**: 1030 at 1 strength vs old at 3 strength
  - New 1030 model more effective at lower strength
  - *From: patientx*

- **CFG for LightX workflows**: 1 on both samplers
  - Prevents overcooking with LightX LoRA
  - *From: garbus*

- **Steps with LightX**: 4-6 steps
  - 20 steps is way too much when using lightx LoRA
  - *From: garbus*

- **Block swap**: 40
  - Standard setting in wrapper to prevent model from taking up VRAM
  - *From: hicho*

- **Shift for I2V**: 9
  - Guidelines for Wan i2v, lower shift makes things sharper which can look less real
  - *From: ingi // SYSTMS*

- **Training video resolution**: 288x512
  - Don't need videos that big for training, larger resolutions slow down training significantly without much benefit
  - *From: ingi // SYSTMS*

- **Audio CFG**: Up to 10
  - Helps with speech clarity in Ovi 1.1 and makes negative prompts work better
  - *From: Kijai*

- **Launch parameters**: --disable-pinned-memory and remove --fast
  - Eliminates OOM issues that have been occurring more frequently
  - *From: JohnDopamine*

- **Steps for TTM with distill LoRAs**: 3+3 (6 total, 3 split)
  - Works better than higher step counts, avoids artifacts
  - *From: hicho*

- **CFG for low noise part with TTM**: 3.5
  - Works well with 10 steps on low noise part
  - *From: slmonker*

- **LightX2V usage**: High noise only
  - Causes ghosting artifacts when used on low noise side
  - *From: slmonker*

- **VACE inpainting mask**: 127 grey
  - Default value that works with new VACE implementation
  - *From: Kijai*

- **TTM reference steps**: Start 1, End 2-3
  - Gives more freedom for motion generation while still providing guidance
  - *From: Atlas*

- **LightX2V shift values for different schedulers**: Beta57: I2V=15.87, T2V=12.34; Beta: I2V=8.96, T2V=6.98; Simple: I2V=9, T2V=7
  - Makes split step sigma equal to i2v sigma boundary (0.900) for optimal performance
  - *From: FL13*

- **Original TTM paper settings**: Steps 3-7 out of 50 total (tweak_index=3, tsstrong_index=7)
  - Default configuration from original TTM implementation for cut and drag operations
  - *From: Kijai*

- **TTM steps**: 50 steps (25/25 split)
  - Good balance for high/low noise processing
  - *From: TheSwoosh*

- **TTM CFG**: 3.5
  - Standard configuration for TTM workflows
  - *From: TheSwoosh*

- **TTM shift**: 8
  - Part of working TTM configuration
  - *From: TheSwoosh*

- **TTM start/end steps**: 3 start step, 7 end step
  - Effective range for TTM processing
  - *From: TheSwoosh*

- **High noise sampling**: 10 steps + cfg 3.5
  - Preferred configuration for high noise part
  - *From: slmonker(5090D 32GB)*

- **FFGO prompt format**: ad23r2 the camera view suddenly changes. [detailed description]
  - Required trigger for LoRA to work properly
  - *From: Kijai*

- **Sampler comparison methodology**: Compare res_2s at X steps vs other samplers at 2X steps
  - res_2s effectively does twice the work so fair comparison requires double steps
  - *From: Kijai*

- **Euler sampler preference**: Use Euler sampler for better visual results
  - Produces better looks than other samplers according to testing
  - *From: FL13*

- **LightX2V I2V settings**: 1 step high cfg 3.5 no LoRA, then 2 steps high cfg 1 with lightx2v_4step_lora, then 2 steps low cfg 1 with lightx2v_I2V_14B
  - Produces results most similar to default 20 steps
  - *From: Danial*

- **Euler/Beta scheduler**: shift 8.96
  - Works well for image to video
  - *From: FL13*

- **Motion amplitude for I2V painter**: 1.15 to 1.5, usually 1.3
  - Higher values can produce artifacts depending on image
  - *From: Elvaxorn*

- **Latest lightx2v LoRA**: Euler and simple with shift 5
  - Recommended by lightx2v team for latest LoRA
  - *From: FL13*

- **lightx2v 1030 LoRA strength**: 1.0 for both high and low
  - Recommended values for 3 sampler method
  - *From: FL13*

- **TTM native steps**: 4 steps sampler + 2 steps TTM
  - Example configuration, values are on top of sampler start step
  - *From: hicho*

- **V2V denoise for reference**: 0.8 denoise with 8 steps
  - Working configuration for character consistency
  - *From: lemuet*

- **Upscaler denoise values**: 0.3 vs 0.4 denoise
  - Comparison showed different detail levels
  - *From: FL13*

- **Denoise for v2v without TTM**: 0.7-0.8
  - Works well for direct latent input approach
  - *From: lemuet*

- **Denoise for second pass T2V LOW**: 0.2
  - Fixes shading issues without over-processing
  - *From: Juan Gea*

- **WanAnimate depth LoRA strength**: 1.2
  - Works well with HIGH noise model
  - *From: Valle*

- **High noise timestep threshold**: sigma >= 0.875
  - Threshold for switching between high/low noise models
  - *From: spacepxl*

- **frame_window_size**: Set to frame_count or multiple
  - Prevents hallucination after input video ends
  - *From: DawnII*

- **add_noise_to_samples**: Enable on first sampler
  - Removes weird color shifts/pink hue
  - *From: David Snow*

- **lightx LoRA**: 1022 low
  - Solves noisy image issues in cartoon character generation
  - *From: Gleb Tretyak*

- **MOE LoRA strength**: 1.0
  - Works as restrainer when paired with other LoRAs
  - *From: GWX-Reloaded*

- **Lightx2v 480p rank 256 LoRA strength**: 3.0
  - Maintains likeness and prompt adherence with less degradation
  - *From: GWX-Reloaded*

- **Wan 2.1 LoRA strength**: 0.30
  - Adds extra dynamic motion when needed without overwhelming
  - *From: GWX-Reloaded*

- **Block swap starting value**: 30
  - Good starting point for finding optimal VRAM usage
  - *From: Scruffy*

- **InfiniteTalk height limit**: 700 pixels
  - Above this causes GPU thrashing and VRAM swapping issues
  - *From: metaphysician*

- **SteadyDancer with LightX2V**: 4 steps, no CFG, no negative pose
  - Works well for basic pose transfer without complex conditioning
  - *From: Kijai*

- **SteadyDancer resolution**: 480x832
  - Good balance for testing pose control quality
  - *From: Kijai*

- **VACE control strength**: Reduce strength for more reference influence
  - When original footage takes too much from reference
  - *From: CHUCK*

- **Block swap optimization**: More blocks in VRAM = faster
  - VRAM is fastest place for bits to live, but don't exceed card limit
  - *From: Kagi*

- **TTM steps**: 2 steps for 6 total steps
  - Fewer steps help TTM follow original video movements without adding unwanted elements
  - *From: Vérole*

- **TTM denoise**: 0.7-0.8
  - Balance between following background movement and maintaining character accuracy
  - *From: Vérole*

- **Vace strength with depth**: 0.7
  - Better character reference matching while losing some accuracy
  - *From: dj47*

- **Block swap**: 40
  - Better VRAM efficiency for long videos, prevents OOM errors
  - *From: Kijai*

- **Prefetch blocks**: 1
  - Optimal VRAM usage, setting to 0 can be slower
  - *From: Kijai*

- **--reserve-vram**: enabled
  - Helps avoid memory issues with Wan models
  - *From: Kijai*

- **CFG**: 3.5
  - Note that CFG >1.0 increases resource consumption significantly
  - *From: Gleb Tretyak*

- **Resolution test**: 1024x576x161 frames
  - High resource consumption test case that previously caused OOM
  - *From: Gleb Tretyak*


## Concepts Explained

- **VAP (Video-as-Prompt)**: System that uses video as reference but still requires massive text prompts explaining exact actions
  - *From: Kijai*

- **MoE architecture**: Mixture of Experts architecture with High/Low noise expert split in Wan 2.2
  - *From: context*

- **Block swap**: Memory management technique that depends on system configuration, affected by unmerged LoRA changes
  - *From: Kijai*

- **Pressure cache**: Command line argument feature that prevents large models from being cached in RAM to help with memory usage
  - *From: Kijai*

- **SVI-film**: LoRA that reduces artifacting for extensions, specifically designed for 5 input frames, effects are subtle but game-changing
  - *From: Ablejones*

- **VACE inpainting**: Video control system for inpainting that provides more consistent results than basic noise masking
  - *From: Ablejones*

- **Block swap**: Memory management technique where model parts are offloaded, LoRAs now obey block swap instead of being fully offloaded
  - *From: Kijai*

- **ATI trajectory control**: Allows precise control over character movement paths, similar to spine bone animations
  - *From: Fill*

- **Dynamic/resized LoRAs**: LoRAs with different ranks that cause recompilation issues with torch compile
  - *From: Kijai*

- **Vue frontend update**: ComfyUI's new JavaScript framework frontend overhaul, similar to React
  - *From: Draken*

- **Video-as-prompt (VAP)**: Feature that uses reference video as control input similar to VACE but without controlnet preprocessing
  - *From: Kijai*

- **MPS vs HPS LoRAs**: Different LoRA variants for Wan 2.2, MPS marginally better for prompt adherence
  - *From: Juampab12*

- **Dynamic LoRAs**: LoRA system that can change without recompilation, but causes issues with full graph compilation
  - *From: Kijai*

- **Sage attention with compile**: Previously always disabled compile as it wouldn't work with sage, but now possible to compile sage with latest version, though other graph breaks exist in native sampling
  - *From: Kijai*

- **Reference hack with Lynx**: Lynx is a module for enhanced identity preservation that can be added to other workflows
  - *From: Kijai*

- **Hard cut vs scene transition**: Hard cut creates abrupt scene changes while scene transitions create smooth morphing between scenes
  - *From: Lodis*

- **fl2v**: First-Last-Frame mode, affects how end frame is encoded in video generation
  - *From: Kijai*

- **Autoregressive video generation**: Architecture that supports temporal autoregression for long-duration video synthesis
  - *From: Zabo*

- **fp16 fast accumulation**: Performance benefit when using fp16 precision for calculations
  - *From: Kijai*

- **Mantissa vs Exponent loss**: bf16 loses mantissa, fp16 loses exponent - casting between them loses data permanently
  - *From: Kijai*

- **Phased DMD**: New distillation method used in LightX2V T2V Seko v2.0, different from self-forcing technique
  - *From: yi*

- **Self-forcing vs DMD**: Terms used somewhat interchangeably, but are different techniques. FastVideo model uses 'self forcing' in config name but 'dmd' in pipeline class
  - *From: Kijai*

- **Bindweave reference padding**: Clip vision embed padding done after encoding with zeros, not encoding empty images. Input references to image_1 and it's handled automatically
  - *From: Kijai*

- **Wan frame count requirement**: Must be 8x+1 format (like 81 frames)
  - *From: lostintranslation*

- **PainterI2V motion amplification**: Pre-scales input latents and balances brightness increase, no actual 'motion data' at that processing stage
  - *From: Kijai*

- **SEC model**: Segment Concept - new segmentation model for better results
  - *From: Dever*

- **4+1 latent block rule**: Frames must align with latent block structure for certain effects to work properly
  - *From: Kijai*

- **Painter I2V math**: G_scaled = I + (G - I - D) * M + D where M is motion_amplitude, I is initial image, G is gray latents, D is mean difference
  - *From: Ablejones*

- **4x latent + 1 rule**: Rule for placing intermediate keyframes - if first frame is at 1 and last at 81, mid frame should be at 17 (4 x 4 + 1)
  - *From: mccoxmaul*

- **Pinned memory**: New memory feature merged into ComfyUI core that some people have trouble with, can be disabled with --disable-pinned-memory
  - *From: Gleb Tretyak*

- **Context windows**: Facilitate generating longer videos in one execution but don't help with extending existing videos. Sometimes loosely used for WanAnimate and InfiniteTalk batch generation beyond 81 frames
  - *From: 42hub*

- **Motion augmentation scheduling**: Technique to modify 'looseness' of latents and control where scene transitions occur by scheduling which latent frames have motion applied
  - *From: Ablejones*

- **Noise padding**: For Bindweave, need to pad noise channel with zeros to match concatenated reference latents, done per step and trimmed before scheduler
  - *From: Kijai*

- **Bindweave box mask**: Marks original area white and padded area black when reference aspect doesn't match video aspect
  - *From: Kijai*

- **Context windows limitation with I2V**: Each window needs input image but you only have one clean input for whole process, leading to either never getting away from input or doing text2vid
  - *From: Kijai*

- **Generated latent artifacts**: Artifacts caused by mismatch between real encoded and generated latents. Generated latents are blurry and out of distribution for the decoder, causing speckle/grid artifacts
  - *From: spacepxl*

- **Node cache**: If a node references a model, it's cached in the node itself and cannot be freed by VRAM cleanup nodes
  - *From: Kijai*

- **Adversarial distillation**: Technique like LightX (dmd2) that helps sharpen generated latents, similar to how GAN loss sharpens VAE or image upscaler outputs
  - *From: spacepxl*

- **Block swapping**: Memory optimization technique that allows running larger models by swapping blocks between GPU and system memory
  - *From: Ada*

- **FP8 quantization**: 8-bit floating point quantization that reduces VRAM usage while maintaining quality
  - *From: Ada*

- **Face input disconnection in Wan Animate**: Removing the face_images connection prevents the model from trying to force facial features onto non-human subjects
  - *From: Charlie*

- **TTM (Time to Move)**: A technique for controlling object movement in videos using masked latent inpainting with timestep scheduling
  - *From: Kijai*

- **High/Low noise split benefits**: Wan 2.2's MoE architecture allows motion control on high noise side while resolution happens on low noise side
  - *From: Kijai*

- **Perfect alpha channel requirement**: TTM requires clean alpha channels without background remnants to avoid artifacts and ghosting
  - *From: avataraim*

- **TimeToMove (TTM)**: A technique that's essentially v2v + differential diffusion with proper masks, applied only for a few steps during sampling. Works particularly well with Wan 2.2
  - *From: spacepxl*

- **Sigma boundary matching**: Adjusting shift values so the split step sigma equals i2v sigma boundary (0.900) for optimal scheduler performance
  - *From: FL13*

- **TTM (Time To Move)**: A technique for guided video-to-video generation using masks to define different noise levels to different areas
  - *From: Kijai*

- **SDE eta value**: Coefficient for noise added/removed per step in SDE/ancestral samplers. 0.5 makes Euler = Euler_ancestral, 0.0 = baseline Euler. Max practically 1.0
  - *From: Ablejones*

- **3 sampler setup**: Multi-stage sampling: first sampler (1 step high noise, cfg 3.5, no lora), second sampler (high noise, cfg 1, with lightx2v), third sampler (low noise with lora)
  - *From: PeroBueno*

- **Causal model**: Autoregressive model architecture that can potentially do long generation, different training approach than standard models
  - *From: FL13*

- **FFGO (First-Frame-Go)**: LoRA technique for Wan 2.2 that enables multiple subject generation with camera view transitions
  - *From: Kijai*

- **res_2s sampler**: Sampler that effectively performs twice the computational steps, should be compared against other samplers at 2x step count
  - *From: Kijai*

- **FFGO**: LoRA that makes I2V easier, requires trigger prompt 'ad23r2 the camera view suddenly changes.'
  - *From: Kijai*

- **TTM (Time-To-Move)**: Uses mask video to know what object to animate, very flexible for 2.5D and 3D camera movement
  - *From: xwsswww*

- **Wan Animate**: Uses controlnet to animate reference image from input video, built on Wan 2.1
  - *From: hicho*

- **gc_collect**: Garbage collection - automatic process that frees up memory by deleting unused objects
  - *From: Dever*

- **TTM (Time To Move)**: Motion guidance system for Wan models, like v2v but with masking. Injects motion signals to control character movement
  - *From: Dever*

- **I2V Painter node**: Injects different values for empty frames instead of all black, like varying intensities of gray. One line of code that calculates difference from init image
  - *From: Kijai*

- **3 sampler method**: Uses separate samplers for high and low noise with different LoRAs, switching at sigma 0.9
  - *From: 42hub*

- **Flow matching**: Generalization that transports between arbitrary distributions, predicts velocity (noise - data). Outperforms diffusion
  - *From: spacepxl*

- **Wan 2.2 MoE architecture**: Two models split by timestep - high noise for motion, low noise for visuals. Like MoE but experts are entire models
  - *From: spacepxl*

- **4-frame block rule**: Reference frames must fit this rule - insert reference 4 times then starting image
  - *From: lemuet*

- **A14B model designation**: 14B active parameters in MoE setup, total 27B parameters but only 14B active at inference time
  - *From: JohnDopamine*

- **Subgraphs in ComfyUI**: Node groups similar to Blender that keep workflows clean, can be unpacked and modified
  - *From: Valle*

- **Frame window calculation**: X(frame window) - (x-1)(motion frames) = total frames - explains why Wan continues past input length
  - *From: DawnII*

- **VACE two-pass process**: First removes character from scene, second places character with pose in scene
  - *From: Valle*

- **Triton caches**: Caches that accumulate during model updates and recompilation, causing memory increases especially on Windows
  - *From: Kijai*

- **LoRA rank**: Low-rank matrices dimensions - higher rank gives more capacity/freedom but costs more parameters and possible artifacts, lower rank is more constrained but faster/safer
  - *From: GWX-Reloaded*

- **Block swap**: Puts model parts into normal RAM and brings to VRAM only when needed - slower but allows more free VRAM for larger operations
  - *From: Scruffy*

- **fp8 fast mode**: When not using fp8 fast mode, fp8 models on non-fp8 cards store weights in fp8 but cast to fp16 for calculations, adding compute overhead
  - *From: Kijai*

- **SVDQuant**: Nunchaku implementation with custom kernels for fast inference, despite name similarity to SVD
  - *From: Kijai*

- **Triple model passes**: SteadyDancer's default method using 3 separate model calls per generation for better quality
  - *From: Kijai*

- **Denoise as step proxy**: Denoise parameter adjusts steps/start_step/end_step but in counterintuitive way, better to set steps directly
  - *From: 42hub*

- **Hyperdimensional latent space**: LLMs use thousands of axes to map concepts, structured prompts like JSON provide more precise navigation than loose text
  - *From: Scruffy*

- **Decoupled DMD**: New distillation method from Z-Image where CFG distillation is the primary driver of step distillation, not just a side effect
  - *From: spacepxl*

- **High/Low noise expert split**: MoE architecture approach where separate models handle different noise levels during denoising, brings capability of larger models to consumer GPUs
  - *From: Ablejones*

- **Chunked rope and FFN**: Optimization that splits RoPE (rotary positional embeds) and FFN (feed forward) calculations into chunks, reducing peak VRAM usage below attention level
  - *From: Kijai*

- **Stage B upscaling**: Cascade approach of taking small high-channel latents and upscaling to high resolution using diffusion model, like a diffusion model upscaler
  - *From: Ablejones*

- **Graph break**: Breaks in torch.compile graph that prevent intermediate tensors from being released, causing higher VRAM usage
  - *From: Kijai*

- **Custom ops**: PyTorch feature that allows uncompiled operations to be part of the compile graph without breaking it
  - *From: Kijai*

- **Concat latent controls**: Elements that get concatenated to the noise input, staying separate until patch embedding
  - *From: spacepxl*


## Resources & Links

- **Wan 2.2 Lightx2v 4-step LoRA v1030** (lora)
  - https://huggingface.co/Kijai/WanVideo_comfy/blob/main/LoRAs/Wan22_Lightx2v/Wan_2_2_I2V_A14B_HIGH_lightx2v_4step_lora_v1030_rank_64_bf16.safetensors
  - *From: avataraim*

- **Qwen Edit Multiple Angles LoRA** (lora)
  - https://huggingface.co/dx8152/Qwen-Edit-2509-Multiple-angles
  - *From: uff*

- **dasiwaWAN22 I2V GGUF** (model)
  - https://huggingface.co/Bedovyy/dasiwaWAN22I2V14B-GGUF/tree/main/HighNoise
  - *From: asd*

- **dasiwaWAN22 full model** (model)
  - https://huggingface.co/JCPser/dasiwaWAN22I2V14B_radiantcrush
  - *From: asd*

- **EMU 3.5 collection** (model)
  - https://huggingface.co/collections/BAAI/emu35
  - *From: shaggss*

- **VAP module weights** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/blob/main/Video-as-prompt/Wan2_1-I2V-14B-VAP_module_bf16.safetensors
  - *From: Kijai*

- **Multiple angles LoRA workflow** (workflow)
  - https://discord.com/channels/1076117621407223829/1402003225061625888/1420881345068142592
  - *From: xwsswww*

- **Simple workflow** (workflow)
  - https://discord.com/channels/1076117621407223829/1342763350815277067/1410772541735174306
  - *From: xwsswww*

- **Wan2.2 frames-to-video model** (model)
  - https://huggingface.co/morphic/Wan2.2-frames-to-video
  - *From: lemuet*

- **Image batcher custom node** (node)
  - https://huggingface.co/Stkzzzz222/remixXL/blob/main/image_batcher_by_indexz.py
  - *From: JohnDopamine*

- **Custom frame indexing node** (node)
  - https://gist.github.com/thelemuet/9318d0e9b19d3c8473ca14722d104aa8
  - *From: lemuet*

- **AI toolkit for training** (tool)
  - https://github.com/ostris/ai-toolkit
  - *From: aikitoria*

- **Stable Video Infinity** (research)
  - https://stable-video-infinity.github.io/homepage/
  - *From: BecauseReasons*

- **Triton Windows wheels** (tool)
  - https://github.com/woct0rdho/triton-windows
  - *From: Kijai*

- **SageAttention Windows wheels** (tool)
  - https://github.com/woct0rdho/SageAttention
  - *From: Kijai*

- **CamCloneMaster** (repo)
  - https://github.com/KwaiVGI/CamCloneMaster
  - *From: Kijai*

- **ATI tutorial video** (tutorial)
  - https://www.youtube.com/watch?v=AI9-1G7niXY
  - *From: Fill*

- **SeedVR2 VideoUpscaler** (tool)
  - https://github.com/numz/ComfyUI-SeedVR2_VideoUpscaler
  - *From: Dream Making*

- **LongCat-Flash-Omni** (model)
  - https://huggingface.co/meituan-longcat/LongCat-Flash-Omni
  - *From: slmonker(5090D 32GB)*

- **ComfyUI-SocksLatentPatcher** (tool)
  - https://github.com/synystersocks/ComfyUI-SocksLatentPatcher
  - *From: scf*

- **BindWeave model** (model)
  - https://huggingface.co/ByteDance/BindWeave
  - *From: ZeusZeus (RTX 4090)*

- **SmoothMix Wan 2.2 model** (model)
  - https://civitai.com/models/1995784/smooth-mix-wan-22-i2vt2v-14b
  - *From: Juampab12*

- **Blender grease pencil tutorial** (tutorial)
  - https://www.youtube.com/watch?v=aIWdBq7-ias
  - *From: Blink*

- **LightX2V 2.2 LoRAs** (lora)
  - https://huggingface.co/Kijai/WanVideo_comfy/tree/main/LoRAs/Wan22_Lightx2v
  - *From: Ablejones*

- **MPS LoRA** (lora)
  - https://huggingface.co/Kijai/WanVideo_comfy/blob/main/LoRAs/Wan22_FunReward/Wan2.2-Fun-A14B-InP-HIGH-MPS_resized_dynamic_avg_rank_21_bf16.safetensors
  - *From: Juampab12*

- **ComfyUI Qwen3-VL-Instruct** (node)
  - https://github.com/IuvenisSapiens/ComfyUI_Qwen3-VL-Instruct
  - *From: devnullblackcat*

- **FlashVSR v1.1** (model)
  - https://huggingface.co/JunhaoZhuang/FlashVSR-v1.1
  - *From: DawnII*

- **Cinematic Hard Cut v2 LoRA** (lora)
  - https://civitai.com/models/2088559?modelVersionId=2376295
  - *From: Ablejones*

- **SmoothMix Wan 2.2** (model)
  - https://civitai.com/models/1995784/smooth-mix-wan-22-i2v-14b
  - *From: Juampab12*

- **Next Scene LoRAs** (lora)
  - https://huggingface.co/lovis93/next-scene-qwen-image-lora-2509 and https://huggingface.co/peteromallet
  - *From: Juampab12*

- **Wan2.2 animate relight LoRA** (lora)
  - https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/blob/main/split_files/loras/wan2.2_animate_14B_relight_lora_bf16.safetensors
  - *From: ulvord*

- **BindWeave** (repo)
  - https://github.com/bytedance/BindWeave
  - *From: BecauseReasons*

- **ChronoEdit** (repo)
  - https://github.com/nv-tlabs/ChronoEdit
  - *From: JohnDopamine*

- **C2C Cache bridging** (repo)
  - https://github.com/thu-nics/C2C
  - *From: fredbliss*

- **UniAVGen** (model)
  - https://mcg-nju.github.io/UniAVGen/
  - *From: DawnII*

- **Holocine PR for wrapper** (workflow)
  - https://github.com/kijai/ComfyUI-WanVideoWrapper/pull/1615
  - *From: BNP4535353*

- **Wan 2.2 Lightx2v v1030** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/blob/main/LoRAs/Wan22_Lightx2v/Wan_2_2_I2V_A14B_HIGH_lightx2v_4step_lora_v1030_rank_64_bf16.safetensors
  - *From: Kijai*

- **Wan 2.2 Lightx2v v1022** (model)
  - https://huggingface.co/lightx2v/Wan2.2-Distill-Loras/blob/main/wan2.2_i2v_A14b_high_noise_lora_rank64_lightx2v_4step_1022.safetensors
  - *From: Kijai*

- **InfinityStar model** (model)
  - https://huggingface.co/FoundationVision/InfinityStar
  - *From: yi*

- **BindWeave repository** (repo)
  - https://github.com/alibaba-damo-academy/Lumos-Custom
  - *From: hicho*

- **Wan Prompt Generator** (tool)
  - https://chatgpt.com/g/g-6887849e21b8819183e20c1dc6bcf353-wan-2-2-prompt-generator
  - *From: Dream Making*

- **MediaSyncer for frame comparison** (tool)
  - https://whatdreamscost.github.io/MediaSyncer/
  - *From: JohnDopamine*

- **Kijai's Wan models** (repo)
  - https://huggingface.co/Kijai/WanVideo_comfy/tree/main
  - *From: ingi // SYSTMS*

- **Optimized GGUF branch** (repo)
  - git clone -b feat_optimized_dequant https://github.com/blepping/ComfyUI-GGUF
  - *From: Dita*

- **BindWeave main code** (repo)
  - https://github.com/bytedance/BindWeave/tree/main
  - *From: Kijai*

- **InfinityStar 8B video model** (repo)
  - https://github.com/FoundationVision/InfinityStar
  - *From: Ada*

- **InfinityStar HuggingFace** (model)
  - https://huggingface.co/FoundationVision/InfinityStar/tree/main
  - *From: Ada*

- **InfinityStar paper** (paper)
  - https://arxiv.org/pdf/2511.04675
  - *From: Ada*

- **ComfyUI-ultimate-openpose-editor** (node)
  - https://github.com/westNeighbor/ComfyUI-ultimate-openpose-editor
  - *From: metaphysician*

- **ComfyUI-FlashVSR_Ultra_Fast** (node)
  - https://github.com/lihaoyun6/ComfyUI-FlashVSR_Ultra_Fast
  - *From: lostintranslation*

- **FlashVSR memory leak fix fork** (repo)
  - https://github.com/Burgstall-labs/ComfyUI-FlashVSR_Ultra_Fast
  - *From: burgstall*

- **Bindweave model** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy_fp8_scaled/tree/main/Bindweave
  - *From: Lodis*

- **Self-forcing Wan2.2 14B** (model)
  - https://huggingface.co/rand0nmr/SFWan2.2-T2V-A14B-Diffusers/tree/main
  - *From: yi*

- **Lucy Edit 1.1 Dev** (model)
  - https://huggingface.co/decart-ai/Lucy-Edit-1.1-Dev
  - *From: DawnII*

- **EdgeTAM transformers version** (model)
  - https://huggingface.co/yonigozlan/EdgeTAM-hf
  - *From: ˗ˏˋ⚡ˎˊ-*

- **SeC-4B ComfyUI nodes** (repo)
  - https://github.com/9nate-drake/Comfyui-SecNodes
  - *From: Gleb Tretyak*

- **SeedVR2 ComfyUI integration** (tool)
  - https://registry.comfy.org/nodes/seedvr2_videoupscaler
  - *From: Adrien Toupet*

- **Sam2 variants comparison** (resource)
  - https://www.sievedata.com/resources/exploring-sam2-variants
  - *From: Kijai*

- **IPAdapter for Wan** (repo)
  - https://github.com/kaaskoek232/IPAdapterWAN
  - *From: Persoon*

- **ComfyUI LightVAE** (repo)
  - https://github.com/ModelTC/ComfyUI-LightVAE
  - *From: Kevin "Literally Who?" Abanto*

- **WAN21 Gouache Style LoRA** (lora)
  - https://hub.oxen.ai/api/repos/shadowworks/public/file/main/WAN21/Gouache_Style_WAN21_14b_2400_r32-v4.safetensors
  - *From: The Shadow (NYC)*

- **ComfyUI-Speaker-Isolation** (repo)
  - https://github.com/pmarmotte2/ComfyUI-Speaker-Isolation
  - *From: manu_le_surikhate_gamer*

- **ComfyUI-Wan22FMLF** (repo)
  - https://github.com/wallen0322/ComfyUI-Wan22FMLF
  - *From: slmonker(5090D 32GB)*

- **ComfyUI-PainterI2V** (repo)
  - https://github.com/princepainter/ComfyUI-PainterI2V
  - *From: slmonker(5090D 32GB)*

- **FastVideo ComfyUI node** (repo)
  - https://github.com/hao-ai-lab/FastVideo
  - *From: hicho*

- **Lumos-Custom** (repo)
  - https://github.com/alibaba-damo-academy/Lumos-Custom
  - *From: Shubhooooo*

- **Cinematic quick cuts LoRA** (lora)
  - https://huggingface.co/neph1/cinematic_quick_cuts_wan
  - *From: DawnII*

- **WanVideo ComfyUI fp8 scaled** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy_fp8_scaled/tree/main
  - *From: 🦙rishappi*

- **FlashVSR alternative node** (node)
  - https://github.com/1038lab/ComfyUI-FlashVSR
  - *From: lostintranslation*

- **Hard cut Wan LoRA** (lora)
  - https://huggingface.co/neph1/hard_cut_wan_lora
  - *From: DawnII*

- **Lumos-Custom model** (model)
  - https://github.com/alibaba-damo-academy/Lumos-Custom
  - *From: slmonker(5090D 32GB)*

- **CoTracker node for point tracking** (node)
  - https://github.com/s9roll7/comfyui_cotracker_node
  - *From: hablaba*

- **SageAttention documentation** (repo)
  - https://github.com/woct0rdho/SageAttention
  - *From: Gleb Tretyak*

- **Ovi 1.1 models** (model)
  - https://huggingface.co/chetwinlow1/Ovi/tree/main
  - *From: MarkDalias*

- **ChronoEdit Upscaler LoRA** (model)
  - https://huggingface.co/nvidia/ChronoEdit-14B-Diffusers-Upscaler-Lora
  - *From: yi*

- **Ovi 10s fp8_scaled model** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy_fp8_scaled/blob/main/TI2V/Ovi/Wan2_2-5B-Ovi_960x960_10s_fp8_e4m3fn_scaled_KJ.safetensors
  - *From: Kijai*

- **Wan 2.2 Turbo LoRAs** (lora)
  - https://huggingface.co/Kijai/WanVideo_comfy/tree/main/LoRAs/Wan22-Turbo
  - *From: avataraim*

- **Wan models/modules/loras spreadsheet** (resource)
  - https://docs.google.com/spreadsheets/d/1HvJ5_ZAzx0Dmw_mifdj1sx2nyIIXoUmqUYj30sMlJpI/edit?usp=sharing
  - *From: Koba*

- **ComfyUI-PainterI2V** (repo)
  - https://github.com/princepainter/ComfyUI-PainterI2V
  - *From: Ablejones*

- **Model comparison spreadsheet** (reference)
  - https://docs.google.com/spreadsheets/d/1HvJ5_ZAzx0Dmw_mifdj1sx2nyIIXoUmqUYj30sMlJpI
  - *From: 42hub*

- **Context options knowledge** (documentation)
  - wanx-troopers.github.io/what-plugs-where/context-options.html
  - *From: 42hub*

- **Phantom with Wan 2.2 tricks** (workflow)
  - https://discord.com/channels/1076117621407223829/1403263501421776977/1432575780919185439
  - *From: Ablejones*

- **WAN2.2-14B-Rapid-AllInOne merge** (model)
  - https://huggingface.co/Phr00t/WAN2.2-14B-Rapid-AllInOne
  - *From: Kiwv*

- **DualParal Project** (repo)
  - https://github.com/DualParal-Project/DualParal
  - *From: Ada*

- **ComfyUI-FlashVSR** (repo)
  - https://github.com/1038lab/ComfyUI-FlashVSR/tree/main
  - *From: lostintranslation*

- **ComfyUI-Wan22FMLF** (node)
  - https://github.com/wallen0322/ComfyUI-Wan22FMLF
  - *From: JohnDopamine*

- **Wan2.2-Lightning LoRA** (model)
  - https://huggingface.co/lightx2v/Wan2.2-Lightning/tree/main/Wan2.2-T2V-A14B-4steps-lora-rank64-Seko-V2.0
  - *From: Dannhauer80*

- **xDiT ComfyUI node** (node)
  - https://github.com/jpgallegoar/xdit-comfyui-private
  - *From: Juampab12*

- **Time-to-Move** (repo)
  - https://github.com/time-to-move/TTM
  - *From: JohnDopamine*

- **Kandinsky 5 ComfyUI implementation** (repo)
  - https://github.com/kandinskylab/kandinsky-5/tree/comfyui/comfyui
  - *From: Ada*

- **Kandinsky 5.0 I2V Pro model** (model)
  - https://huggingface.co/kandinskylab/Kandinsky-5.0-I2V-Pro-sft-5s-Diffusers
  - *From: Juampab12*

- **PyTorch installation for RTX 5090** (tool)
  - https://download.pytorch.org/whl/cu130
  - *From: Juampab12*

- **Sa2VA segmentation issue solution** (repo)
  - https://github.com/adambarbato/ComfyUI-Sa2VA/issues/3
  - *From: boorayjenkins*

- **Carl Wan 2.2 Animate workflow** (workflow)
  - https://www.reddit.com/r/comfyui/comments/1nzrf0j/carl_wan_22_animate/
  - *From: boorayjenkins*

- **Wan2_1-I2V-14B-Bindweave_fp16.safetensors** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/blob/main/Bindweave/Wan2_1-I2V-14B-Bindweave_fp16.safetensors
  - *From: Kijai*

- **Kandinsky 5.0 ComfyUI implementation** (repo)
  - https://github.com/Ada123-a/ComfyUI-Kandinsky
  - *From: Ada*

- **Wan2.2-frames-to-video LoRA** (lora)
  - https://huggingface.co/morphic/Wan2.2-frames-to-video
  - *From: Kijai*

- **ComfyUI-PainterLongVideo** (repo)
  - https://github.com/princepainter/ComfyUI-PainterLongVideo
  - *From: hicho*

- **ComfyUI-Wan22FMLF** (repo)
  - https://github.com/wallen0322/ComfyUI-Wan22FMLF
  - *From: Gateway {Dreaming Computers}*

- **Depth Anything 3** (repo)
  - https://github.com/ByteDance-Seed/Depth-Anything-3
  - *From: A.I.Warper*

- **ComfyUI-PainterI2V** (repo)
  - https://github.com/princepainter/ComfyUI-PainterI2V
  - *From: Dream Making*

- **TTM GitHub repository** (repo)
  - https://github.com/time-to-move/TTM
  - *From: Kijai*

- **TTM Gradio GUI** (tool)
  - https://github.com/time-to-move/TTM/tree/main/GUIs
  - *From: avataraim*

- **ComfyUI-MultiCutAndDrag** (node)
  - https://github.com/Pablerdo/ComfyUI-MultiCutAndDrag
  - *From: hudson223*

- **ComfyUI-PainterI2V wrapper** (node)
  - https://github.com/princepainter/ComfyUI-PainterI2VforKJ
  - *From: hicho*

- **UniVid model** (model)
  - https://github.com/CUC-MIPG/UniVid
  - *From: JohnDopamine*

- **Kijai's TTM implementation commit** (repo)
  - https://github.com/kijai/ComfyUI-WanVideoWrapper/commit/b826642a83cb0e752f18949c3e858eabb8f49646
  - *From: Kijai*

- **TTM GitHub repository** (repo)
  - https://github.com/time-to-move/TTM
  - *From: Kijai*

- **PainterSampler all-in-one sampler** (repo)
  - https://github.com/princepainter/Comfyui-PainterSampler
  - *From: hicho*

- **WanMoeKSampler alternative sampler** (repo)
  - https://github.com/stduhpf/ComfyUI-WanMoeKSampler
  - *From: CJ*

- **ComfyUI-AE-Animation for mask animation** (tool)
  - https://github.com/wallen0322/ComfyUI-AE-Animation
  - *From: slmonker*

- **DFloat11 Wan 2.2 T2V model** (model)
  - https://huggingface.co/DFloat11/Wan2.2-T2V-A14B-2-DF11
  - *From: brbbbq*

- **ComfyUI-DFloat11 plugin** (repo)
  - https://github.com/LeanModels/ComfyUI-DFloat11
  - *From: brbbbq*

- **VGGT 3D generation space** (tool)
  - https://huggingface.co/spaces/facebook/vggt
  - *From: Juampab12*

- **Wan tricks documentation** (documentation)
  - https://wanx-troopers.github.io/wan-i2v-tricks.html#timetomove
  - *From: 42hub*

- **TTM GUI** (tool)
  - https://github.com/time-to-move/TTM/blob/main/GUIs/README.md
  - *From: xwsswww*

- **CausalWan2.2-I2V-A14B-Preview** (model)
  - https://huggingface.co/FastVideo/CausalWan2.2-I2V-A14B-Preview-Diffusers
  - *From: JohnDopamine*

- **SAM3 model** (model)
  - https://huggingface.co/facebook/sam3
  - *From: Lodis*

- **ComfyUI SAM3 node** (node)
  - https://github.com/PozzettiAndrea/ComfyUI-SAM3
  - *From: slmonker(5090D 32GB)*

- **Alternative SAM3 node** (node)
  - https://github.com/Ltamann/ComfyUI-TBG-SAM3
  - *From: asd*

- **FastVideo CausalWan blog** (documentation)
  - https://hao-ai-lab.github.io/blogs/fastvideo_causalwan_preview/
  - *From: JohnDopamine*

- **Music video using WAN** (example)
  - https://youtu.be/XGTF4yOfOjA?list=RDXGTF4yOfOjA
  - *From: Ruairi Robinson*

- **ComfyUI MagickWand for motion blur** (node)
  - https://github.com/Fannovel16/ComfyUI-MagickWand
  - *From: JohnDopamine*

- **FFGO LoRA for Wan 2.2** (lora)
  - https://huggingface.co/Kijai/WanVideo_comfy/tree/main/LoRAs/Wan22_FFGO
  - *From: Kijai*

- **FFGO research paper** (paper)
  - https://arxiv.org/abs/2511.15700
  - *From: Alisson Pereira*

- **FFGO Video Customization repo** (repo)
  - https://github.com/zli12321/FFGO-Video-Customization
  - *From: Dever*

- **ComfyUI-TBG-SAM3 node** (node)
  - https://github.com/Ltamann/ComfyUI-TBG-SAM3
  - *From: Kijai*

- **Wan ecosystem timeline** (documentation)
  - https://wanx-troopers.github.io/timeline.html
  - *From: 42hub*

- **TTM GUI tools** (tool)
  - https://github.com/time-to-move/TTM/tree/main/GUIs
  - *From: Dever*

- **ComfyUI-UniRig** (repo)
  - https://github.com/PozzettiAndrea/ComfyUI-UniRig
  - *From: xwsswww*

- **ComfyUI-PainterFLF2V** (repo)
  - https://github.com/princepainter/Comfyui-PainterFLF2V
  - *From: xwsswww*

- **FFGO-Video-Customization** (repo)
  - https://github.com/zli12321/FFGO-Video-Customization/
  - *From: Piblarg*

- **TTM examples** (repo)
  - https://github.com/time-to-move/TTM/tree/main/examples/cutdrag_wan_Monkey
  - *From: xwsswww*

- **ComfyUI-PainterLongVideo** (repo)
  - https://github.com/princepainter/ComfyUI-PainterLongVideo
  - *From: JohnDopamine*

- **Qwen3-VL-8B-NSFW-Caption** (model)
  - https://huggingface.co/mradermacher/Qwen3-VL-8B-NSFW-Caption-V4.5-GGUF
  - *From: patientx*

- **WanX Troopers Timeline** (website)
  - https://wanx-troopers.github.io/timeline.html
  - *From: 42hub*

- **Wan 2.2 ComfyUI Repackaged** (model)
  - https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/blob/main/split_files/diffusion_models/wan2.2_ti2v_5B_fp16.safetensors
  - *From: Boop*

- **Kijai WanVideo fp8 scaled models** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy_fp8_scaled/tree/main/T2V
  - *From: 🦙rishappi*

- **TTM GitHub repo** (repo)
  - https://github.com/time-to-move/TTM/
  - *From: Dever*

- **ComfyUI-AE-Animation** (tool)
  - https://github.com/wallen0322/ComfyUI-AE-Animation
  - *From: Vérole*

- **42hub's Wan I2V tricks guide** (guide)
  - https://wanx-troopers.github.io/wan-i2v-tricks.html#timetomove
  - *From: 42hub*

- **ComfyUI-MotionCapture** (tool)
  - https://github.com/PozzettiAndrea/ComfyUI-MotionCapture
  - *From: xwsswww*

- **Depth ControlNet for Wan 2.2** (model)
  - https://huggingface.co/TheDenk/wan2.2-t2v-a14b-controlnet-depth-v1/tree/main
  - *From: David Snow*

- **WanAnimate relight LoRA** (model)
  - Kijai/WanVideo_comfy WanAnimate_relight_lora_fp16.safetensors
  - *From: 42hub*

- **Wan research paper** (paper)
  - https://www.arxiv.org/pdf/2510.21890
  - *From: samhodge*

- **Panorama LoRA for FLUX** (model)
  - https://huggingface.co/jbilcke-hf/flux-dev-panorama-lora-2
  - *From: Scruffy*

- **Ditto LoRA** (lora)
  - https://huggingface.co/Kijai/WanVideo_comfy/tree/main/LoRAs/Ditto
  - *From: Yan*

- **ComfyUI QwenVL nodes** (node)
  - https://github.com/1038lab/ComfyUI-QwenVL
  - *From: Gateway {Dreaming Computers}*

- **Playmate2 repository** (repo)
  - https://github.com/Playmate111/Playmate2
  - *From: Kijai*

- **Wan 2.2 Lightning LoRAs** (model)
  - https://huggingface.co/lightx2v/Wan2.2-Distill-Loras/tree/main
  - *From: Critorio*

- **ComfyUI-FlashVSR_Ultra_Fast** (repo)
  - https://github.com/lihaoyun6/ComfyUI-FlashVSR_Ultra_Fast
  - *From: FL13*

- **Qwen-Edit-2509-Upscale-LoRA** (model)
  - https://huggingface.co/vafipas663/Qwen-Edit-2509-Upscale-LoRA
  - *From: David Snow*

- **FLUX.2-dev** (model)
  - https://huggingface.co/black-forest-labs/FLUX.2-dev
  - *From: shaggss*

- **SteadyDancer** (repo)
  - https://github.com/MCG-NJU/SteadyDancer
  - *From: slmonker*

- **ComfyUI-SAM3DBody** (repo)
  - https://github.com/PozzettiAndrea/ComfyUI-SAM3DBody
  - *From: Scruffy*

- **Wan speed LoRA list** (resource)
  - https://wanx-troopers.github.io/loras/part-01.html#22-t2v
  - *From: 42hub*

- **FFGO Video Customization** (repo)
  - https://github.com/zli12321/FFGO-Video-Customization/
  - *From: spacemathapocalypse*

- **ComfyUI-VAE-Utils for Wan upscale** (repo)
  - https://github.com/spacepxl/ComfyUI-VAE-Utils
  - *From: David Snow*

- **David Snow's depth-based upscaler workflow** (workflow)
  - *From: David Snow*

- **WanExperiments repo** (repo)
  - https://github.com/drozbay/WanExperiments
  - *From: 42hub*

- **Wan LoRA collection page** (resource)
  - https://wanx-troopers.github.io/loras/part-01.html
  - *From: 42hub*

- **SteadyDancer-14B** (model)
  - https://github.com/MCG-NJU/SteadyDancer
  - *From: Gateway {Dreaming Computers}*

- **Tile LoRA v1.1** (lora)
  - *From: spacepxl*

- **ComfyUI SDNQ quantization** (node)
  - https://github.com/EnragedAntelope/comfyui-sdnq
  - *From: cocktailprawn1212*

- **Wan 2.2 1030 LoRA** (lora)
  - https://huggingface.co/Kijai/WanVideo_comfy/resolve/main/LoRAs/Wan22_Lightx2v/Wan_2_2_I2V_A14B_HIGH_lightx2v_4step_lora_v1030_rank_64_bf16.safetensors
  - *From: 🦙rishappi*

- **SteadyDancer-14B model** (model)
  - https://huggingface.co/MCG-NJU/SteadyDancer-14B/tree/main
  - *From: DawnII*

- **ComfyUI-WanVideoWrapper steadydancer branch** (repo)
  - https://github.com/kijai/ComfyUI-WanVideoWrapper/tree/steadydancer
  - *From: Kijai*

- **Hard Cut Wan LoRA v3** (lora)
  - https://huggingface.co/neph1/hard_cut_wan_lora/tree/main
  - *From: DawnII*

- **ComfyUI-PainterI2V** (repo)
  - https://github.com/princepainter/ComfyUI-PainterI2V
  - *From: Valle*

- **Civitai Cinematic Fast Cutting LoRA** (lora)
  - https://civitai.com/models/2113025/cinematic-fast-cutting-previously-quick-cuts
  - *From: NebSH*

- **Samplers and Schedulers guide** (guide)
  - https://civitai.com/articles/9191/samplers-schedulers-and-sigmas-oh-my-cutting-through-denoise
  - *From: Scruffy*

- **ComfyUI-SuperUltimateVaceTools** (tool)
  - https://github.com/bbaudio-2025/ComfyUI-SuperUltimateVaceTools
  - *From: FL13*

- **ComfyUI-AE-Animation-English-Mod** (tool)
  - https://github.com/Verolelb/ComfyUI-AE-Animation-English-Mod
  - *From: Vérole*

- **Z-Image Decoupled DMD research** (research)
  - https://github.com/Tongyi-MAI/Z-Image?tab=readme-ov-file#-decoupled-dmd-the-acceleration-magic-behind-z-image
  - *From: spacepxl*

- **UltraCascade ComfyUI implementation** (repo)
  - https://github.com/ClownsharkBatwing/UltraCascade
  - *From: Ablejones*

- **ComfyUI-VAE-Utils latent upscale model** (tool)
  - https://github.com/spacepxl/ComfyUI-VAE-Utils
  - *From: spacepxl*

- **SFWan2.2-T2V-A14B-Diffusers** (model)
  - https://huggingface.co/rand0nmr/SFWan2.2-T2V-A14B-Diffusers/tree/main/transformer
  - *From: yi*

- **Self-Forcing model** (model)
  - https://huggingface.co/gdhe17/Self-Forcing
  - *From: yi*

- **Triton Windows** (tool)
  - https://github.com/woct0rdho/triton-windows
  - *From: Kijai*

- **PyTorch Custom Ops Tutorial** (documentation)
  - https://docs.pytorch.org/tutorials/advanced/python_custom_ops.html#python-custom-ops-tutorial
  - *From: Kijai*

- **WanVideoWrapper update** (tool)
  - *From: Kijai*


## Known Limitations

- **ATI appears to be limited to 81 frames**
  - Frame count is hardcoded in original code, changing it doesn't work without other adjustments
  - *From: Fill/Kijai*

- **VAP doesn't work with CFG**
  - Current implementation has issues preventing proper CFG functionality
  - *From: Kijai*

- **VAP requires exact 49 frame reference videos**
  - Original code limitation, reference video must match exactly
  - *From: Kijai*

- **MTV Crafter only does 49 frames at once**
  - Has extension method but limited context window
  - *From: Kijai*

- **FlashVSR produces oversharpened results with halos**
  - Quality issues compared to other upscaling methods
  - *From: WorldX*

- **SVI-Shot doesn't work with Wan 2.2**
  - Only gives frozen frame video output
  - *From: Dita*

- **Complex or fast motions not completely solved**
  - Video models still struggle to make complex/fast motion look nice or understand how it should be
  - *From: Lodis*

- **SVI-film effects are subtle**
  - While game-changing, effects are ultimately quite subtle in how they are applied
  - *From: Ablejones*

- **SVI-film would need retraining for Wan 2.2**
  - Minimal testing shows it would likely need to be retrained for 2.2
  - *From: Ablejones*

- **Video-As-Prompt needs text prompt to work well**
  - Cannot rely on video input alone, text prompt still required for good results
  - *From: JohnDopamine*

- **UniC3 limited effectiveness with Wan 2.2**
  - Works better with 2.1, needs higher strength (3+) to work with 2.2
  - *From: Juan Gea*

- **ATI model limited to Wan 2.1 I2V 1.3B**
  - Uses smaller 1.3B model instead of larger 14B due to training cost limitations
  - *From: Draken*

- **Wan models can't accurately represent unseen angles**
  - Single reference image can't provide enough information for accurate 360-degree character representation
  - *From: Persoon*

- **BindWeave not extractable as LoRA**
  - Cannot be extracted like other models due to architecture differences
  - *From: Gleb Tretyak*

- **Video-as-prompt requires good text prompts**
  - Doesn't work without detailed text descriptions, limiting usefulness
  - *From: Kijai*

- **Wan Animate can only control one character**
  - Multi-character scenes require separate generation and compositing
  - *From: Valle*

- **Longcat is downgrade from Wan 2.2**
  - Worse motion and prompt following compared to Wan 2.2
  - *From: Kijai*

- **T2V LightX2V LoRAs still lacking**
  - New LoRAs focus on I2V, T2V still needs improvement
  - *From: Doctor Shotgun*

- **Wan 2.2 limited to 5 seconds for anime-style 10 second videos**
  - For 10 second anime videos, LongCat recommended instead
  - *From: Kiwv*

- **VAP completely non-functional**
  - VAP outputs are just from prompts with placebo effect, doesn't actually use reference video meaningfully
  - *From: Kijai*

- **Wan Animate cannot use SD 1.5/SDXL LoRAs**
  - Unlike AnimateDiff, Wan Animate can't use SD model LoRAs - different model architecture
  - *From: hicho*

- **Cannot merge LoRAs with low mem load in Wan Animate**
  - Causes dtype mismatch errors with bf16 models
  - *From: Gleb Tretyak*

- **Switching between Qwen edit and Wan 2.2 very slow on 64GB RAM**
  - Memory management issues requiring potential upgrade to 128GB
  - *From: Ablejones*

- **BindWeave cannot be used as LoRA with Wan Animate**
  - Same channels but completely different input structure
  - *From: Kijai*

- **Wan 2.2 T2I struggles with close-up shots**
  - Difficulty getting headlight close-ups even with prompt iteration
  - *From: Dream Making*

- **QwenVL part of BindWeave doesn't seem to do much**
  - Unclear if implementation is correct or if it needs different settings
  - *From: Kijai*

- **Hard cut lora difficult to activate for fight scenes**
  - Much harder to trigger for certain scene types
  - *From: Ablejones*

- **Clip vision uses center crop for square input**
  - Face might not be included in the 224x224 crop
  - *From: Kijai*

- **InfinityStar quality issues**
  - Fast but quality is poor according to initial testing
  - *From: Benjimon*

- **Bindweave zoom out effect**
  - Too much background in reference images can cause unwanted zoom out effect
  - *From: Kijai*

- **FlashVSR memory leak**
  - Tile sizes above 256 cause severe memory leaks, second run can consume 64GB+ of memory
  - *From: lostintranslation*

- **Phantom doesn't work with distill LoRAs**
  - Phantom breaks identity when running with distillation LoRAs
  - *From: ZeusZeus*

- **Bindweave can't extract as LoRA for Wan Animate**
  - Input is structured differently, combining weights would break functionality of both models
  - *From: Kijai*

- **LightX2V screws up Bindweave positioning**
  - Tends to obey reference position too much when using LightX2V
  - *From: Kijai*

- **Lucy Edit still poor with anime**
  - Despite 1.1 update, still performs badly on anime content
  - *From: DiXiao*

- **I2V models lose likeness when face obstructed**
  - I2V VACE and similar have problems maintaining likeness/consistency when person's face gets obstructed or moves out of frame
  - *From: ucren*

- **Wan Animate ignores character legs frequently**
  - Very often ignores character's legs during transformation, happens more when character is sitting
  - *From: Zabo*

- **In-between frame sequences are glitchy**
  - Frames can't be used to crossfade with previous clip, introduces color shifting
  - *From: lemuet*

- **High noise LoRAs don't work with some I2V workflows**
  - Important pose/move information in high LoRAs may not be compatible with certain AIO workflows
  - *From: Phr00t*

- **Multitalk/Infinitetalk limited to 8 seconds**
  - Maximum duration constraint for talking video generation
  - *From: avataraim*

- **Single frame insertion in middle of sequences**
  - Single frames are ignored, only 2+ frame sequences have effect due to blending with adjacent frames
  - *From: lemuet*

- **svi-film lora doesn't fix distorted frames**
  - Only prevents color shifting on remaining frames, doesn't resolve initial frame distortion
  - *From: lemuet*

- **Painter node changes subject appearance**
  - Changes subject way too much at higher values, visible even in examples
  - *From: Kijai*

- **FlashVSR wrapper basic implementation**
  - Can't do super large resolutions, need specialized FlashVSR wrappers for that
  - *From: Kijai*

- **VACE compatibility limited to matching models**
  - VACE needs to match the model it was trained with, only works with T2V based models
  - *From: Kijai*

- **Ovi 10s model not suitable for lower resolutions**
  - Really not meant to be used at tiny resolutions, audio becomes poor quality
  - *From: Kijai*

- **High resolution causes green artifacts**
  - At 720p resolution, noise becomes too fine causing people to turn green
  - *From: slmonker*

- **Wan Animate has trouble with shooting actions**
  - Model sometimes has difficulty generating shooting motions
  - *From: Juampab12*

- **960x960 for 241 frames is very slow**
  - Takes about 27.85 seconds per step, not fast for high resolution long videos
  - *From: Kijai*

- **Context windows work poorly with SVI dance**
  - Context window approach doesn't work well for extending SVI dance beyond 49 frames
  - *From: Kijai*

- **Prompt scheduling not implemented for Wan**
  - Old animate diff/deforum prompt travel/scheduling isn't available for Wan models
  - *From: fearnworks*

- **Lynx doesn't work well with non-realistic faces**
  - Poor performance on stylized or animated characters
  - *From: Kijai*

- **Bindweave cannot work properly on native ComfyUI**
  - Requires wrapper implementation with proper reference encoding, noise padding, and QwenVL integration
  - *From: Kijai*

- **HuMO maintains same expression throughout video**
  - Character looks dead/static compared to InfiniteTalk which makes character look more alive
  - *From: Charlie*

- **100% character consistency impossible without multiple reference images**
  - Even with 4 reference slots in Bindweave, cannot achieve perfect consistency
  - *From: Gleb Tretyak*

- **Wan Animate doesn't transfer eyes, jaw line, lips from reference image**
  - Has bias towards original video, looks similar but not exactly the person
  - *From: Albert*

- **Bindweave struggles with backside of character from single frontal image**
  - Understandable limitation when working with single reference
  - *From: burgstall*

- **LongCat doesn't work with Wan 2.2 LoRAs**
  - None of the Wan stuff like loras work on it
  - *From: Kijai*

- **OVI vertical formats don't work well**
  - i2v 512x960 or 704x1280 don't work as well as horizontal
  - *From: avataraim*

- **Small video sizes cause shaking and poor quality**
  - Very bad results with small resolutions
  - *From: avataraim*

- **Multiple people talking confusion**
  - Model gets confused who is talking and who not when multiple people are in scene
  - *From: Gill Bastar*

- **Wan Animate plastic look**
  - Wan Animate tends to make people look pretty plastic
  - *From: ingi // SYSTMS*

- **Kandinsky 5 prompt adherence**
  - Prompt adherence is iffy compared to other aspects which are good
  - *From: yi*

- **Resolution limits for Wan**
  - If you go up to 1080p it starts stretching stuff, highest recommended is 1440x816
  - *From: ingi // SYSTMS*

- **Interpolation methods can't handle detail artifacts**
  - Most interpolation methods (rife, film, etc.) can't deal with speckle artifacts because motion of details don't match the object they're attached to
  - *From: lemuet*

- **Kandinsky 5.0 20B doesn't fit on 24GB VRAM without block swapping**
  - Even with FP8 quantization, full model requires memory management techniques
  - *From: Ada*

- **Depth Anything 3 has worse image quality for monocular depth compared to v2**
  - More geometrically accurate but poor visual quality, not suitable for Wan use
  - *From: Kijai*

- **Wan 2.2 with custom frames not perfect since not exactly trained for it**
  - Still has some flashing and other artifacts when using FMLF workflows
  - *From: Kijai*

- **Painter long video has bugs with prompt adherence**
  - Bug kills prompt adherence, prompts don't change properly on each sampler
  - *From: hicho*

- **TTM requires perfect mask quality**
  - Poor alpha channels or background remnants cause ghosting and double objects
  - *From: avataraim*

- **Low success rate with TTM**
  - Around 5% success rate reported, highly dependent on proper settings and mask quality
  - *From: slmonker*

- **Character consistency issues with TTM**
  - Doesn't maintain same character likeness as original image, may create different characters
  - *From: avataraim*

- **Wan 1.3B not suitable for real-time generation**
  - Requires processing large frame batches before decoding, unlike causal models
  - *From: Kijai*

- **TTM fails with empty backgrounds**
  - If empty space has no noise or content, TTM doesn't work properly. Needs some background content to function
  - *From: Kijai*

- **TTM may not work well for subtle movements like mouth animation**
  - Works well for camera movement and object trajectory, but might be too subtle for close-up facial movements unless it's a close-up shot
  - *From: lemuet*

- **Character consistency issues with TTM for artist-driven characters**
  - TTM may not work well for maintaining consistent artistic character styles
  - *From: amli*

- **SAM3 doesn't work for cartoon characters**
  - Body detection fails on non-realistic character types
  - *From: Guey.KhalaMari*

- **WAN 2.1 quality is bad**
  - Lower quality compared to 2.2, novelty is realtime use
  - *From: Kijai*

- **LightX2V causes issues in low noise sampling**
  - Works fine for high noise but creates problems in low noise part of generation
  - *From: slmonker(5090D 32GB)*

- **Causal self forcing useless as distill LoRA**
  - Trained too differently to work in normal workflows
  - *From: Kijai*

- **TTM with 2.1 models has tensor mismatch issues**
  - Compatibility problems when using TTM with WAN 2.1 and InfiniteTalk
  - *From: amli*

- **FFGO requires specific image layout**
  - Needs white background references and specific prompt trigger to work properly
  - *From: Dever*

- **TTM workflow limitations**
  - Can't work with any video - input and output need to match, unlike Uni3C
  - *From: hicho*

- **Sec4B segmentation quality**
  - Not as good for real person segmentation compared to other subjects
  - *From: slmonker*

- **Prompt length restrictions still exist**
  - Too long prompts cause errors in Wan I2V generation
  - *From: patientx*

- **FFGO tricky with character introductions**
  - Works well for objects already in scene, but trickier introducing new characters that are off screen coming into frame
  - *From: Guey.KhalaMari*

- **I2V painter doesn't work with T2V or VACE**
  - The new motion control node only works with I2V, not T2V or VACE
  - *From: Elvaxorn*

- **TeaCache not effective with LightX2V**
  - TeaCache doesn't help much with LightX2V since it works best with many steps, and 4-6 steps doesn't make it worthwhile
  - *From: Elvaxorn*

- **TTM character consistency issues**
  - When unique characters enter/exit frame at different times and come back, they lose consistency and identity bleeds
  - *From: Guey.KhalaMari*

- **Tiled upscaler memory issues**
  - 4K upscaling crashes due to RAM leak in loop nodes. ComfyUI shuts down during 4th tile process with 3x3 tiles
  - *From: FL13*

- **Wan 2.2 loses context off-screen**
  - Camera panning 360 degrees will drift as model loses context of things offscreen
  - *From: Guey.KhalaMari*

- **I2V Painter compatibility**
  - Doesn't work well with TTM as it messes up noise latents pre-generation
  - *From: 42hub*

- **T2V models can't use encoded images**
  - Only work with text prompts, need I2V models for image inputs
  - *From: lemuet*

- **WanAnimate character can't exit shot or start with empty shot**
  - Character entering frame is a big limitation
  - *From: Juan Gea*

- **WanAnimate doesn't understand depth**
  - Only works with pose, depth input is ignored
  - *From: 42hub*

- **DWPose struggles with non-front-facing videos and multiple people**
  - Fails on martial arts, spinning kicks, loose drawings
  - *From: dj47*

- **Wan 2.2 dithering issues**
  - Generates dithering dots at 720p with I2V or T2V
  - *From: harryB*

- **InfiniteTalk struggles with 720p at 1280 width**
  - Hangs and thrashes GPU, works better at lower resolutions
  - *From: metaphysician*

- **Fun Control lacks strength/weight controls**
  - Preprocessors are either on or off with no fine control over influence
  - *From: dj47*

- **Pose detection fails on 2D drawings**
  - Pose tracking works best for realistic 3D shaded characters and is poor at 2D art styles
  - *From: metaphysician*

- **Depth controlnet doesn't capture facial expressions**
  - Depth controlnet failed to capture any facial expressions from source video
  - *From: David Snow*

- **Fighting animations challenging for pose detection**
  - Fighting animations often end up with body poses that don't look recognizably human to pose estimators
  - *From: metaphysician*

- **FlashVSR results look artificial**
  - FlashVSR upscaling examples look very artificial according to user testing
  - *From: David Snow*

- **Anisora changes character appearances too dramatically**
  - While motion is good, it significantly alters colors and character looks, making it unsuitable for consistent animation work
  - *From: GWX-Reloaded*

- **PainterLongVideo doesn't actually work**
  - Has harsh changes in camera and object movement despite 30-frame overlap, essentially same as simple extension
  - *From: 42hub*

- **fp8 models don't actually run in fp8 on non-fp8 cards**
  - Unless fp8 fast mode is used, they cast to fp16 for calculations anyway with extra compute overhead
  - *From: Kijai*

- **Dynamic compilation needs CPU compiler setup on Windows**
  - Requires specific compiler setup that causes issues for many users
  - *From: Kijai*

- **SteadyDancer only works with base model**
  - Cannot extract as LoRA, requires full model weights, pose embeddings are only 6MB but patch embed was trained
  - *From: Kijai*

- **SteadyDancer doesn't do facial control**
  - No face processing capability, making WanAnimate comparisons unfair
  - *From: Kijai*

- **Wan MoCha character placement unpredictable**
  - Even with good mask, sometimes puts character wherever it pleases, prompt becomes useless
  - *From: Guey.KhalaMari*

- **VACE takes too much from original footage**
  - When used as reference without masking, over-influences the generation
  - *From: CHUCK*

- **No long generation method in SteadyDancer**
  - Examples are only 3 seconds long, though driving videos can be 10s
  - *From: Kijai*

- **Tiled ksamplers don't support control inputs**
  - Cannot use controlnet or other control inputs with video model tiling
  - *From: spacepxl*

- **FlashVSR has tiny attention windows**
  - Prevents proper motion tracking, causes details to swim around
  - *From: spacepxl*

- **Wan 2.2 5B spatial latent density too low**
  - Almost too bad to work with honestly, with so much spatial compression no room to train details that don't take up entire video
  - *From: Ablejones*

- **1.3B can't resolve details well**
  - Unless trained on high resolution with control inputs
  - *From: spacepxl*

- **Wan2.1 latent size falls apart with small objects**
  - Falls apart really fast when things are too small
  - *From: Ablejones*

- **Context windows cause background drift**
  - Less drift when not using ref latent slot, but drift still occurs
  - *From: Gleb Tretyak*

- **Wan animate poor for 2D anime characters**
  - Makes 2D anime characters look bad, better fit for 3D characters
  - *From: conjark*

- **Poor pose detection for 2D video input**
  - Best results are front-facing dance videos, anything deviating causes pose detection to drop or fail
  - *From: metaphysician*

- **Kandinsky 5.0 Pro lacks tooling ecosystem**
  - Not even comparable to Wan's tooling ecosystem despite better base model performance
  - *From: yi*

- **Kandinsky 5.0 Pro needs speed breakthrough**
  - Even with optimizations, still needs significant speed improvements
  - *From: JohnDopamine*

- **Riflex doesn't work with Wan**
  - Doesn't really work at all with Wan models, even if it worked would only be few more seconds vs infinite context windows
  - *From: Kijai*

- **Graph breaks still exist in some models**
  - InfiniteTalk still has graph breaks, though shouldn't cause as big issues with new fixes
  - *From: Kijai*

- **RMS norm fusion benefits smaller now**
  - Compile performance gains reduced as RMS norm is now available as native pytorch function
  - *From: Kijai*

- **Reserve VRAM sometimes ignored**
  - Reserve VRAM setting can be overridden by minimum memory fraction settings
  - *From: spacepxl*


## Hardware Requirements

- **VAP memory usage**
  - 8GB extra at bf16, doubles sequence length for self attention making it heavy to use
  - *From: Kijai*

- **FlashVSR performance**
  - Takes 2 seconds per step after initial loading, decoding 1440p at 17 frames takes considerable time
  - *From: patientx*

- **RAM limits with pinned memory**
  - Pinned memory flag will crash if you run out of RAM, especially at 99-100% usage
  - *From: Kijai/Gleb Tretyak*

- **VRAM usage with block swap 40**
  - Model uses under 1GB VRAM with block swap 40
  - *From: Kijai*

- **720p generation with 20 blocks swapped**
  - Max memory: 11.059GB, Max reserved: 12.281GB for 81 frames
  - *From: Kijai*

- **RAM usage for Wan 2.2 workflow**
  - Around 38GB RAM used at end with 20 blocks swapped and cached text encoder
  - *From: Kijai*

- **Generation time scaling**
  - 832x480 to 1280x720 increases generation time threefold
  - *From: BNP4535353*

- **1280x720 25min generation time example**
  - High resolution generation taking 25 minutes
  - *From: BNP4535353*

- **VRAM usage for torch compile**
  - First run uses more VRAM due to compilation, subsequent runs use less
  - *From: Kijai*

- **4090 memory limits**
  - Around 18-19GB max allocation for 81 frames at 720x1280, block swap 20-25 works
  - *From: aipmaster*

- **LongCat-Flash-Omni requirements**
  - 560B parameters, needs at least 8×H20-141G for FP8 or 16×H800-80G for BF16
  - *From: scf*

- **GPU temperature**
  - Wan Animate raises GPU temp to 77°C max on water-cooled 4070 Ti Super, which is normal
  - *From: Gleb Tretyak*

- **VRAM usage**
  - Torch compile recompiles can spike VRAM usage by 2GB+ on Windows
  - *From: Kijai*

- **Memory optimization**
  - --cache-none launch argument reduces both VRAM and RAM consumption
  - *From: Stef*

- **RAM for model switching**
  - 64GB RAM insufficient for smooth switching between Qwen edit and Wan 2.2, may need 128GB
  - *From: Ablejones*

- **VRAM for Wan animate 14B bf16**
  - Questioned if 16GB VRAM + 64GB RAM sufficient for wan2.2_animate_14B_bf16.safetensors
  - *From: Gleb Tretyak*

- **Sage attention performance benefits**
  - For single image only 5-10% benefit depending on resolution, much bigger increase for batch of 4. Helps AMD users with both speed and memory
  - *From: Kijai*

- **VRAM for full A14B model**
  - Huge amount needed, most users stick to high/low variants. 5090 can handle BF16 version
  - *From: ingi // SYSTMS*

- **Offloading performance**
  - For video models where single block processing takes longer than moving the block, near zero loss in inference speed
  - *From: Kijai*

- **fp8_fast mode GPU support**
  - Only works on 4000 series and up, no calculation done in fp8 unless using this mode
  - *From: Kijai*

- **RAM limitations affect quant choice**
  - 32GB RAM user needs Q5_K_M, but offloading makes Q8 viable for most
  - *From: Gleb Tretyak*

- **FlashVSR VRAM needs**
  - 32GB VRAM needed for 145 frames with tiled dit, 81 frames works without tiling
  - *From: lostintranslation*

- **Bindweave VRAM usage**
  - RTX 5090 with 32GB hitting VRAM limits at lower resolutions with certain LoRAs
  - *From: WorldX*

- **Bindweave QwenVL CLIP**
  - RTX 2060 struggles to load, needs to be put to CPU, works if unloaded before ksampler
  - *From: hicho*

- **LongCat CPU loading**
  - Loading four nodes for >30 minutes with CPU from cold start on good machine
  - *From: The Shadow (NYC)*

- **Gleb's setup**
  - 4070 Ti Super, 16GB VRAM, 64GB RAM - experiences lag but not breaking with heavy workflows
  - *From: Gleb Tretyak*

- **64GB RAM recommended for some workflows**
  - RAM can bottleneck certain Wan processing workflows
  - *From: Fawks*

- **Flash VSR 1.1 less VRAM hungry**
  - Improved memory efficiency compared to v1
  - *From: Elvaxorn*

- **SageAttention performance on different GPUs**
  - On 4090 and 5090 sage is roughly 2x faster than other attention methods at 720p
  - *From: Kijai*

- **4070 Ti Super performance**
  - 16GB VRAM, 64GB RAM, gets around 124s/it with res_2s sampler
  - *From: Gleb Tretyak*

- **RTX 4070 Ti SUPER specs**
  - Total VRAM 16376 MB, total RAM 32577 MB, works well with offloading
  - *From: Léon*

- **720p 81 frames performance**
  - Around 20s/it on high-end GPUs with proper settings
  - *From: Kijai*

- **VRAM for higher resolutions**
  - Unable to do higher than 1024x576 on 24GB VRAM even with full blockswap
  - *From: burgstall*

- **Bidirectional sampling VRAM usage**
  - Causes enormous VRAM increase and instant OOM - can do 1000 frames but not 512 with it
  - *From: Gleb Tretyak*

- **5090 fp8_fast mode performance**
  - 241 frames at 960x960 with 40 steps took 5:46 with 9 steps skipped by EasyCache, max memory 16.893 GB
  - *From: Kijai*

- **Slow performance issue**
  - wan2.2 I2V at 720x512 taking 8min for transformer loading and 16min+ for first step with py313+cu130+pytorch290
  - *From: psylent_gamer*

- **OVI 1.1 VRAM usage**
  - 25-30 swap blocks needed for 1280x704 on 24GB VRAM, hits 16GB with 40 blocks
  - *From: avataraim*

- **Wan 2.2 I2V performance**
  - <200sec 720p gens on cu128+pt280 with ComfyUI 3.66
  - *From: psylent_gamer*

- **Color match node VRAM**
  - Very touchy on VRAM, doesn't fit into 32GB even after cleaning VRAM
  - *From: lostintranslation*

- **Kandinsky 5 Pro VRAM**
  - Needs >40gb to get past VAE-Decode, OOMs on 4090 even at 24frames 512x512
  - *From: JohnDopamine*

- **Wan training on A100-80GB OOM**
  - 13 videos 720x1280x81frames and 20 images with 720x1280 and 3 repeats causes OOM
  - *From: Albert*

- **PyTorch version compatibility**
  - Python 3.10 and latest torch works, cuda 12.8 or 13 is fine for RTX 5090
  - *From: Juampab12*

- **Torch version for Kandinsky**
  - Works on pytorch 2.7.1 but not 2.9 due to OOM issues
  - *From: Kagi*

- **VRAM usage**
  - 128GB RAM useful with single GPU, ingi constantly hits 75%+ usage in ComfyUI with RTX6000
  - *From: ingi // SYSTMS*

- **Kandinsky 20B VRAM**
  - Requires 24GB+ VRAM even with FP8 and block swapping for full functionality
  - *From: Ada*

- **PainterLongVideo VRAM**
  - Cannot run 720x1280 3x81 frames on 5090, needs memory optimization
  - *From: Dkamacho*

- **VRAM optimization improvements**
  - Torch 2.7->2.9 + CUDA 13 with sageattn_qk_int8_pv_fp8_cuda++ reduced time from 270s to 150s on RTX 4090
  - *From: berserk4501*

- **TTM is VRAM hungry**
  - The technique requires significant VRAM and may need image downsizing on lower-end GPUs
  - *From: Guey.KhalaMari*

- **Python 3.12+ for SAM3**
  - SAM3 requires Python 3.12 or higher, upgrade needed from 3.10
  - *From: JohnDopamine*

- **H100 with CUDA 9.0 compatibility**
  - Attention mode sageattn causes issues, need to use SDPA instead
  - *From: killermonkeys*

- **Minimum RAM for Wan 2.2**
  - 64GB RAM minimum for Wan 2.2 with 12GB VRAM
  - *From: Tony(5090)*

- **8GB VRAM limitations**
  - 8GB VRAM (4070) will be tough, 32GB RAM not sufficient for video generation, stick to images
  - *From: Tony(5090)*

- **High-speed storage for low VRAM**
  - Fast drive needed when using --cache-none argument for model loading/unloading
  - *From: garbus*

- **Tiled upscaler performance**
  - 10+ minutes for 2K upscaling on RTX 4090, 15+ minutes on RTX 4060 16GB
  - *From: FL13*

- **Wan 2.2 Mocha memory**
  - Doubles memory usage compared to other models. 16GB VRAM + 32GB RAM still OOMs at 480p, needs 448x256 resolution
  - *From: Suomsoh*

- **Sam 3D Objects**
  - Requires 32GB+ VRAM recommended, 24GB VRAM minimum on RTX 30xx series
  - *From: Guey.KhalaMari*

- **Memory pressure issues with 'Attempting to release mmap'**
  - 60 sec pause indicates RAM (not VRAM) struggles. Try --disable-pinned-memory, add RAM, large swap file
  - *From: 42hub*

- **Tiny VAE performance**
  - Almost instant vs 1.5-2 minutes for normal VAE on low resolution generations
  - *From: patientx*

- **16GB VRAM insufficient for Wan 2.2 VACE**
  - User with 16GB VRAM and 32GB RAM running out of VRAM with Wan 2.2 VACE
  - *From: Suomsoh*

- **Performance issues with wrapper**
  - User machine struggles with wrapper, OOMs at 17 frames
  - *From: Gleb Tretyak*

- **12GB VRAM tight for Wan likeness LoRA training**
  - 12GB VRAM is too tight for training, suggested to use 24GB VRAM on runpod
  - *From: Juan Gea*

- **RTX 3090 Ti VRAM usage for 720x720 81 frames**
  - VAE encoding uses 6GB VRAM, takes 5 seconds without tiling on 4090
  - *From: Kijai*

- **Memory requirements vary by system configuration**
  - Performance depends on RAM speed, PCI bus speed, motherboard - no universal answer for model swapping
  - *From: Scruffy*

- **Ampere cards handle fp16 differently**
  - RTX 3090/3090 Ti can run fp16 as fast or faster than fp8_scaled, while 4000/5000 series have improved quant support
  - *From: GWX-Reloaded*

- **VRAM optimization**
  - 6GB VRAM not enough to decide optimal block swap settings, more blocks in VRAM = faster but don't exceed limit
  - *From: hicho/Kagi*

- **SteadyDancer inference time**
  - 121 frames at 480x832 with 4 steps took reasonable time vs original 150 model passes
  - *From: Kijai*

- **VRAM for 720p 81 frames**
  - Around 15GB VRAM with fp8 14B model and full block swap, up to 18GB+ with torch.compile
  - *From: Kijai*

- **Long video RAM usage**
  - 260GB swap RAM nearly filled SSD for very long video generation
  - *From: Gleb Tretyak*

- **Kandinsky 720p performance**
  - 720p video in 20sec/it with Taylorseer lite, without CFG/step distill, adaptive guidance adds 30% speed improvement
  - *From: yi*

- **5090 upscaling performance**
  - About 10 minutes on RTX 5090 for upscaling workflow
  - *From: spacepxl*

- **Torch.compile Windows issues**
  - Windows-specific excessive VRAM usage during compilation, Linux doesn't have this issue
  - *From: Kijai*

- **Memory usage optimization**
  - 720p 81 frames uses 10.9GB/31.8GB with full block swap on Linux, 1024x576x161 frames uses 12GB
  - *From: Kijai*

- **High CFG memory impact**
  - CFG 3.5 significantly increases resource consumption compared to CFG 1.0
  - *From: Gleb Tretyak*

- **Test system specs**
  - 16GB VRAM, 128GB RAM for high-resolution long video generation
  - *From: Gleb Tretyak*


## Community Creations

- **ATI UI integration** (node)
  - UI system for ATI with trajectory tracking, motion transfer, and preset animations
  - *From: Fill*

- **Optimized RIFE implementation** (node)
  - 10x faster RIFE implementation with proper coding, includes FILM interpolation
  - *From: Fill*

- **WanI2VCustomEmbeds node** (node)
  - Custom node for adding start/overlap images and masks to I2V workflows
  - *From: Ablejones*

- **dasiwaWAN22 merge** (model)
  - Wan 2.2 merge with NSFW LoRAs and speed optimizations for 4-step generation
  - *From: asd*

- **Custom frame indexing node** (node)
  - Allows frame indexing and blank frame insertion with syntax like 0:10,(10),-1:-3,5,6,(10)
  - *From: lemuet*

- **Image batcher by indexz** (node)
  - Custom node for batching images by index for VACE workflows
  - *From: JohnDopamine*

- **ATI Path Editor with timing control** (node)
  - Allows easy creation of trajectory paths with timing control for ATI model
  - *From: Fill*

- **Custom triton cache setup** (workflow)
  - Batch file setup to isolate triton cache per ComfyUI installation
  - *From: patientx*

- **WanVideo lora select multi** (node)
  - Multi-LoRA loader with compact layout for wrapper
  - *From: Mattis*

- **Blender file for grease pencil control** (workflow)
  - Mesh rendered as grease pencil for animation control
  - *From: Blink*

- **Next Scene LoRAs** (lora)
  - Multiple LoRAs for creating different camera angles and scene changes - optimized for navigating around scenes vs cinematic shots
  - *From: pom*

- **Hard Cut testing workflow** (workflow)
  - Workflow for testing Cinematic Hard Cut v2 LoRA with frame-to-frame transitions
  - *From: Ablejones*

- **SVI Shot workflow for Wan 2.2** (workflow)
  - Modified workflow using SVI shot techniques adapted for Wan 2.2 to counter degradation in long videos
  - *From: DawnII*

- **Audio reactive mask coordinates** (tool)
  - Modified class to get red dots in mask areas that react to audio, outputs coordinates for ATI
  - *From: yukass*

- **Optimized GGUF dequantization** (tool)
  - Fork with optimized dequant within 5% of fp8 performance, needs triton/Linux
  - *From: Dita*

- **Infinite duration workflow** (workflow)
  - Loop workflow with frame concatenation and overlap for smooth long videos
  - *From: Gleb Tretyak*

- **Dialog Diarizer Node** (node)
  - Custom node using pyannote to split dialog audio into up to 4 speakers with silences
  - *From: manu_le_surikhate_gamer*

- **FlashVSR memory leak fix** (node)
  - Fork attempting to fix memory leak issues in FlashVSR node
  - *From: burgstall*

- **Bindweave branch** (model)
  - Test version of Bindweave model with QwenVL integration
  - *From: Kijai*

- **SeedVR2 ComfyUI integration update** (tool)
  - Updated version with CLI tool for batch processing
  - *From: Adrien Toupet*

- **Real Multitalk Workflow** (workflow)
  - Uses Florence2 to mask characters and custom diarizer node for multi-character talking
  - *From: manu_le_surikhate_gamer*

- **Modified Humo embeds node** (node)
  - Integrated PainterI2V motion logic into Humo embeds for enhanced motion
  - *From: VRGameDevGirl84(RTX 5090)*

- **File path switching node** (node)
  - Switches between even/odd file paths with MyCustomPath/0 or 1/ structure
  - *From: Gleb Tretyak*

- **Modified Painter node with last frame** (node)
  - Enhanced version of Painter I2V that includes last frame functionality
  - *From: Vérole*

- **Wan models/modules/loras spreadsheet** (resource)
  - Comprehensive list of all models/modules/loras for Wan 2.1/2.2 with best practice suggestions
  - *From: Koba*

- **Modified PainterI2V noise code** (tool)
  - Experimenting with noise math modifications for I2V generation
  - *From: Ablejones*

- **Scene detection node** (node)
  - Added to nodepack for multi-scene WanAnimate workflows
  - *From: burgstall*

- **Custom I2V mask node** (node)
  - Allows custom masks and optional input of i2v latents directly for strength modulation
  - *From: Ablejones*

- **Automated multi-scene WanAnimate character replacement workflow** (workflow)
  - WIP workflow for replacing characters across multiple scenes
  - *From: burgstall*

- **HuMo I2V patch** (node)
  - Lets HuMo add start images, end frames like standard I2V model, makes it compatible with SVI
  - *From: Ablejones*

- **Bindweave native ComfyUI implementation** (node)
  - Working bindweave implementation for native ComfyUI with clip vision embeds
  - *From: Ablejones*

- **Face detailer workflow** (workflow)
  - Workflow pulled from Cseti's upscaling workflow for improving faces in generated videos
  - *From: ingi // SYSTMS*

- **Kandinsky 5.0 ComfyUI support with GGUF** (node)
  - Implementation supporting FP8 quantization, block swapping, and GGUF format
  - *From: Ada*

- **WanVideoWrapper Bindweave support** (node)
  - Merged branch adding Bindweave model support to the wrapper
  - *From: Kijai*

- **TTM ComfyUI implementation** (node)
  - ComfyUI wrapper for Time to Move cut and drag animation technique
  - *From: Kijai*

- **MultiCutAndDrag** (node)
  - Alternative ComfyUI implementation of cut and drag functionality
  - *From: hudson223*

- **PainterI2V wrapper for KJ** (node)
  - ComfyUI wrapper for PainterI2V functionality working with Kijai's implementation
  - *From: princepainter*

- **TimeToMove example workflow** (workflow)
  - Demonstrates how to use TTM for camera motion and object movement, available in WanVideo wrapper examples
  - *From: Kijai*

- **3D animation pipeline combining MoGe2, Blender and TTM** (workflow)
  - Complete pipeline for controlled camera animation using 3D scene generation and motion transfer
  - *From: lemuet*

- **Host node for podcast generation** (node)
  - Creates prompts for Qwen to generate podcast content with multiple voices and styles
  - *From: manu_le_surikhate_gamer*

- **Modified Chatterbox node** (node)
  - Creates audio files with required silences for turn-taking in generated podcasts
  - *From: manu_le_surikhate_gamer*

- **FFGO workflow implementation** (workflow)
  - Basic I2V workflow setup for FFGO LoRA with proper image concatenation and padding
  - *From: ingi // SYSTMS*

- **Koboldcpp integration for Qwen3-VL** (node)
  - Custom node for loading/unloading Qwen3-VL models via koboldcpp with VRAM management
  - *From: patientx*

- **WanVideoWrapper** (wrapper)
  - Kijai's wrapper with example workflows for various Wan 2.2 features
  - *From: Tony(5090)*

- **SmoothMix LoRA** (lora)
  - LoRA for motion control, mentioned as recent release
  - *From: garbus*

- **LightX2V 1030 HIGH sampler LoRA** (lora)
  - Big improvement for I2V, significant upgrade from previous versions
  - *From: garbus*

- **Tiled upscaler for wan i2v** (workflow)
  - Upscales videos to 2K/4K without VRAM limits, retains start image details, reduces seams
  - *From: FL13*

- **Native TTM implementation** (node)
  - Wraps TTM functionality for native ComfyUI use, allows ending noise injection
  - *From: Kijai*

- **Timeline documentation** (tool)
  - Community effort to track Wan ecosystem development
  - *From: 42hub*

- **Wan tricks documentation** (resource)
  - Community-maintained documentation of Wan techniques and workflows
  - *From: 42hub*

- **Wanx-troopers website** (resource)
  - Comprehensive documentation site for Wan ecosystem compiled from community conversations
  - *From: 42hub*

- **Video upscaler workflow by mumpitz** (workflow)
  - New video upscaler workflow posted on YouTube
  - *From: David Snow*

- **Depth-based upscaler** (workflow)
  - 1.3B upscaler using clipped depthmap to prevent background detail addition
  - *From: David Snow*

- **WanExperiments** (node)
  - Node to replicate Painter I2V functionality in more principled fashion
  - *From: Ablejones*

- **Tile LoRA v1.1** (lora)
  - Updated tile LoRA trained on wider variety of sizes/frames with fewer artifacts
  - *From: spacepxl*

- **WanVideoWrapper SteadyDancer implementation** (node)
  - ComfyUI integration for SteadyDancer pose-controlled video generation
  - *From: Kijai*

- **Impact Pack Detailer Hook for VACE** (workflow)
  - Enables tiled upscaling with VACE controls using detailer segmentation
  - *From: Ablejones*

- **Hard Cut Wan LoRA v3** (lora)
  - Cinematic fast cutting effects for Wan models
  - *From: DawnII*

- **ComfyUI-AE-Animation-English-Mod** (tool)
  - Fork of AE Animation node with full English UI and new Flip H/V & Scale X/Y features
  - *From: Vérole*

- **Basic latent upscale model** (model)
  - 2x spatial upscale model using VAE training components, works on images and video
  - *From: spacepxl*

- **WanVacePhantomDualV2 node** (node)
  - Node for handling multiple control inputs separately, compatible with Phantom
  - *From: Ablejones*

- **SteadyDancer integration** (feature)
  - Merged into WanVideoWrapper
  - *From: Kijai*

- **Native context windows PR** (feature)
  - Context windows implementation that works with concat latent controls
  - *From: spacepxl*
