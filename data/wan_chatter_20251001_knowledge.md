# Wan Chatter Knowledge Base
*Extracted from Discord discussions: 2025-10-01 to 2025-11-01*


## Technical Discoveries

- **VACE inpainting can be combined with normal latent inpaint and differential diffusion**
  - VACE inpainting is a model feature that can be layered with other inpainting techniques for better results
  - *From: Kijai*

- **High Noise model fails with large inpaint masks**
  - The 2.2 High Noise model has issues with large inpaint areas, dependent on mask size
  - *From: Ablejones*

- **Unmerged LoRAs provide better quality than merged**
  - Unmerged LoRAs use more VRAM but maintain base precision and allow runtime strength adjustment with better quality
  - *From: Kijai*

- **Some T2V LoRAs don't work well with fp8/fp16 but work fine with GGUF**
  - Certain T2V-trained LoRAs have compatibility issues with fp8 and fp16 formats but function properly with GGUF models
  - *From: Samy*

- **LoRA can fall off when hitting VRAM limits**
  - If you hit VRAM limit, the LoRA stops being used entirely
  - *From: mallardgazellegoosewildcat*

- **Palingenesis model appears to be base 2.2 + lightning merge**
  - It's a rebirth/regeneration concept by merging distill loras into the base model
  - *From: hicho*

- **SA-ODE sampler is just Adams-Bashforth method from 1883**
  - The sampler gets 'released' by someone every 3 months or so, it's an old mathematical method
  - *From: mallardgazellegoosewildcat*

- **DYNO model achieves 70% dynamic performance of Wan2.2 14b standard model**
  - Original LightX2V LoRA only reached 50%, DYNO is a fully new high-noise model trained based on 2.2, not a LoRA
  - *From: slmonker(5090D 32GB)*

- **LightX2V LoRA extraction requires very high rank**
  - Extraction took rank 512 before it came close to the full model, some methods end up to rank 1000
  - *From: Kijai*

- **Pose and face detection should take 1-2 seconds for 81 frames**
  - If taking longer, it's likely running on CPU instead of GPU due to missing onnxruntime-gpu
  - *From: Kijai*

- **Wan 2.2 low noise style LoRAs work with WanAnimate**
  - User tested and confirmed that LoRAs trained on Wan 2.2 low noise model are compatible with WanAnimate
  - *From: TheSwoosh*

- **Improved pose processing for WanAnimate**
  - New preprocessor uses vitpose (the one WanAnimate was trained with), better face crop and masking through pose keypoints or bbox instead of manual point editor
  - *From: Kijai*

- **WanAnimate model architecture relationship**
  - Wan 2.2 low is a sort of finetune of Wan 2.1 and WanAnimate despite being called for 2.2 is also based on 2.1, which explains LoRA compatibility
  - *From: Lodis*

- **GPU optimization for ComfyUI mask operations**
  - Kijai rewrote blockify code in pytorch with device option, achieving massive speedup from CPU to GPU processing
  - *From: Kijai*

- **Most 2.1 LoRAs work on 2.2 low noise**
  - 2.2 low noise is essentially a modified 2.1 model
  - *From: mdkb*

- **AI Toolkit supports blockswapping by default**
  - Sends 40 blocks to CPU during training, allowing 256 res video training on 5090
  - *From: Ryzen*

- **HuMO hugely benefits from higher resolution**
  - Ideally 720p (1280x720) for best results
  - *From: Ablejones*

- **Dyno model has built-in LightX2V LoRA**
  - High noise model comes with LightX2V attached, only low noise model needs separate LoRA
  - *From: Rainsmellsnice*

- **New Lightning LoRAs solve motion speed issues**
  - 250928 LoRAs extremely good for preserving motion on high noise
  - *From: pom*

- **ByteDance VAE works with VibeVoice without finetuning**
  - Can take output audio tensor and feed it into ByteDance VAE for reconstruction without needing to finetune VibeVoice, though finetuning might improve speed by avoiding extra VAE refiner stage
  - *From: MysteryShack*

- **Wan 2.2 MOE LoRAs work with Wan Animate using only Low Noise sampler**
  - Use only the Low Noise LoRA at weight 1.0 instead of both High and Low, since Wan Animate is based on 2.1 architecture
  - *From: Screeb*

- **OVI uses symmetric twin backbone design**
  - Parallel audio and video branches built on identical DiT architecture, video branch initialized from Wan 2.2 5B, audio branch trained from scratch, totaling 11B parameters
  - *From: mallardgazellegoosewildcat*

- **Training High and Low Noise LoRAs separately may reduce body deformations**
  - Training both LoRAs together in AI Toolkit may cause body deformities, separate training of each model appears to resolve this issue
  - *From: Kytra*

- **Smooth mix model retains 99% movement/prompt following of regular wan while being faster**
  - Merged light loras in a way that retained movement and prompt adherence, works at 1cfg 8 steps
  - *From: Ada*

- **Standard Wan2.2 can achieve similar results to smooth mix using 3 sampler setup**
  - Though it takes more steps, can get similar motion quality
  - *From: garbus*

- **2.2 loras work fine on 2.1, especially if loaded on low noise only**
  - For character loras and details, can load on low model only. Big changes or motion need high noise too
  - *From: Juampab12*

- **WanAnimate V2 preprocessing nodes workflow available**
  - Kijai released example workflow V2 that uses preprocessing nodes, with fixed scaled fp8 model
  - *From: Charlie*

- **Smooth Mix model trades motion characteristics for frame interpolation compatibility**
  - Exaggerates motion at 16fps which looks better after frame interpolation to 32fps, designed for 30fps playback
  - *From: Rainsmellsnice*

- **HuMo can generate 277 frames (~11s) in one shot with big GPU**
  - More frames causes original image reference to degrade over time
  - *From: Dever*

- **Dual model setups fail when exceeding frame limits**
  - High Noise model limited to 81 frames, Low Noise can handle 121+ frames. Using Phantom/MagRef in LN slot with >81 frames causes camera blending compensation
  - *From: mdkb*

- **Radial Attention causes black video output but reduces generation time significantly**
  - Issue resolved by updating sage
  - *From: GalaxyTimeMachine (RTX4090)*

- **T2V requires only 1+1 steps with certain configurations**
  - For T2V generation, can use just 1+1 steps
  - *From: hicho*

- **5B + 2.2 low model bypass technique**
  - Can combine 5B content with Wan 2.2 graphics by using 5B + 2.2 low to bypass its VAE
  - *From: hicho*

- **Black output caused by incorrect resolution**
  - Resolution must follow specific rules - multiples of 64 work, with video token number divisible by 128
  - *From: GalaxyTimeMachine (RTX4090)*

- **Video token calculation formula**
  - For Wan 2.1 and 2.2 14B: width/16 * height/16 * (length+3)/4. For Wan 2.2 5B: width/32 * height/32 * (length+3)/4. Result must be divisible by 128
  - *From: GalaxyTimeMachine (RTX4090)*

- **Only one dimension needs to be 128 multiple**
  - Height X Width must be divisible by 128, but easiest way is having at least one dimension as multiple of 128
  - *From: Instability01*

- **Speed LoRAs work best on low model only**
  - Character LoRAs from Wan 2.1 work better when connected to low noise model only
  - *From: Dream Making*

- **I2V generates slower motions**
  - I2V models seem to overall generate slower motions compared to T2V
  - *From: Lodis*

- **T2V generally superior to I2V**
  - T2V is generally far better with video models because it resembles optimal transport far better
  - *From: mallardgazellegoosewildcat*

- **FP8 scaled model causing pixelated/blurry outputs**
  - User experiencing pixelated outputs with FP8 scaled model, switching to FP16 resolved the issue completely
  - *From: Ryzen*

- **Pytorch native RMS norm function provides significant speedup**
  - New native rms_norm function is ~9x faster than custom Wan rms norm when not using torch compile, though whole generation speedup is smaller since it's only small part of inference
  - *From: Kijai*

- **Lightning LoRA settings for high quality fast generation**
  - Using Lightning LoRA v0.7 strength with CFG 1.4 on low-noise phase, achieving 720p in 160 seconds on RTX 5090
  - *From: Lan8mark*

- **Dynamic shift parameter tuning required**
  - Shift parameter needs to be tuned depending on other settings and is set incorrectly in default ComfyUI workflow
  - *From: Lan8mark*

- **Converting latent to regular images, upscaling, then converting back to latent works better than direct latent upscaling**
  - User found that direct latent upscaling is poorly implemented and doesn't achieve good quality, so they decode to images first, upscale x2, then encode back to latent
  - *From: Lan8mark*

- **Manual denoise strength calibration between 0.2-0.4 produces better results than automatic calculation**
  - Comparing automatic denoise strength calculated by KSampler Advanced vs manually calibrated strength shows significant improvement in facial expression and details
  - *From: Lan8mark*

- **High-noise phase at native 720p isn't necessary - can halve resolution for high-noise then upscale for low-noise**
  - User cuts resolution in half on both sides for high-noise steps, then upscales x2 and feeds into low-noise phase without quality loss. Achieves 81 frames at 720p in 160 seconds on 5090
  - *From: Lan8mark*

- **CLIP vision model not necessary for Wan 2.2**
  - Even there it's not necessary, not that it ever was fully necessary with 2.1 either
  - *From: Kijai*

- **OVI is 11B parameters total**
  - It's Wan 2.2 5B twice and then some extra param
  - *From: mallardgazellegoosewildcat*

- **AniSora 3.2 is already distilled**
  - The 3.2 is already distilled, so no need for that, the older versions do work with the loras, and it's better than lightx2v or lightning too for high noise, 8 steps
  - *From: Kijai*

- **Wan 2.2 5B is better base than 1.3B**
  - The 1.3B was described as 'too squishy' while 5B offers something better that's still cheaper than 14B
  - *From: mallardgazellegoosewildcat*

- **OVI is 11B audio-video model**
  - Based on Wan2.2 5B and MM Audio, works like Veo 3/Sora 2 for audio-video generation
  - *From: yi*

- **rCM LoRA available as SOTA distillation for Wan**
  - Nvidia's 'SOTA distillation' method, works like LightX2V but supposedly better
  - *From: yi*

- **Consistency models must be distillations**
  - Consistency models map points on trajectory of parent model directly to finished output, they find shortcuts but need existing trajectories from parent model
  - *From: mallardgazellegoosewildcat*

- **Wan 2.2 performs better on consumer but Step benchmarks higher in research**
  - Step consistently benches higher on arxiv papers and is considered stronger in research community, but Wan is more popular with consumers
  - *From: mallardgazellegoosewildcat*

- **Wan animate temporal mask works for keeping/generating frames**
  - The wan-fun inpaint model can do white/black mask for keeping/generating frames and has temporal mask functionality
  - *From: Kijai*

- **e4m3fn vs e5m2 FP8 model performance comparison**
  - e5m2 is about 2 seconds faster than e4m3fn (34s vs 36s), with similar VRAM usage. e4s work better on 4090+, e5s work better on cards lower than 4090, especially 30 series
  - *From: happy.j*

- **Torch Compile node only works with e5 models on fresh install**
  - Previously worked with e4 models but now only functions with e5 models after fresh ComfyUI install
  - *From: ▲*

- **OVI lip-sync quality varies with steps**
  - 50 steps works better than lower step counts for lip-sync quality in OVI model
  - *From: tarn59*

- **MAGREF working with WAN 2.2 for character consistency**
  - Successfully integrated MAGREF with WAN 2.2 for good multi-character consistency in I2V generation
  - *From: Elvaxorn*

- **SecNodes segmentation accuracy**
  - SEC segmentation model works very well for object tracking and masking, with high accuracy even through cuts and when objects are out of frame
  - *From: Vérole*

- **SAM 3 waitlist is available**
  - SAM 3 has been announced by Meta with a waitlist signup
  - *From: Kijai*

- **SEC masking is solid for Wan animate**
  - SEC works better than SAM2 alone and is still SAM2.1 with extra guidance for segmentation
  - *From: ArtOfficial*

- **New RCM LoRA works well for character consistency**
  - RCM distill LoRA by Nvidia devs works as alternative to lightx2v, provides good character consistency with prompt adherence
  - *From: Elvaxorn*

- **MagRef provides excellent character consistency**
  - MagRef works with both T2V and I2V, outperforms other consistency models in testing
  - *From: Elvaxorn*

- **Linear quadratic scheduler works better than simple scheduler for new Lightx2v MoE**
  - Simple scheduler causes ghosting issues with the new model, linear quadratic fixes this
  - *From: FL13*

- **New Lightx2v 2.2 I2V full model works better than LoRA version**
  - LoRA version has ghosting and glitchy output, full model produces cleaner results
  - *From: JohnDopamine*

- **Kijai extracted LoRA works better than official repo LoRA**
  - Official LoRA from lightx2v repo doesn't work properly, Kijai's extraction fixes the issues
  - *From: FL13*

- **New Lightx2v I2V only needs high noise LoRA, can use 2.1 LoRA for low noise**
  - Low noise component can reuse existing 2.1 lightx2v LoRA
  - *From: Kijai*

- **New Light MoE High LoRA provides significantly more motion**
  - Using Kijai's extracted 64 rank LoRA at strength 3.00 gives lots more motion compared to previous setups
  - *From: phazei*

- **FlashVSR uses only 11GB VRAM**
  - Peak VRAM usage is 11GB, much less than any other diffusion based upscaler
  - *From: yi*

- **Linear quadratic scheduler is most reliable with new LoRA**
  - After experimenting with few schedulers, linear quadratic is the most reliable when using new LoRA
  - *From: FL13*

- **Triton 3.5.0 fixes fp8 compile issues**
  - New triton release specifically mentions fp8 patch that's been merged to fix compilation issues with fp8 models
  - *From: phazei*

- **FlashVSR can do 384->1024 upscale for 81 frames in ~6 seconds using only 1 step with 1.3B model**
  - Whole process took approximately 6 seconds, with VAE decode being 3 seconds vs 20 seconds for normal VAE
  - *From: Kijai*

- **Running only FlashVSR low q projection on image input and adding to first block result works with single step without using their VAE**
  - Achieved upscaling results without the full FlashVSR pipeline
  - *From: Kijai*

- **TaylorSeer Lite version provides significant speed improvement over TeaCache**
  - Getting around 5s/it compared to 15s/it, works well but quality takes a hit with lots of movement
  - *From: Zabo*

- **CFG scheduling can be done with list of values for each step in Kijai's wrapper**
  - Can provide different CFG values for each sampling step
  - *From: Kijai*

- **PyTorch 2.9.0 stable breaks Wan VAE, causing double VRAM usage**
  - PyTorch 2.9.0 stable causes VAE to use twice the VRAM in both native and wrapper nodes, but specific nightly builds work fine
  - *From: Kijai*

- **fp32 conv3d workaround reduces VRAM usage on PyTorch 2.9.0+**
  - Running conv3d operations in fp32 bypasses the PyTorch bug while using less VRAM than full fp32 VAE
  - *From: Kijai*

- **Wan 2.2 high noise model offers significantly more motion than 2.1**
  - When properly used with both high and low noise models, 2.2 generates way more motion than 2.1 ever could
  - *From: Kijai*

- **FlashVSR combined with Cinescale LoRA works well with 0.75 denoise**
  - Provides 20% speed increase with no noticeable quality loss, helps reduce over-sharpness
  - *From: Elvaxorn*

- **New Wan2.2 4-step distill models are significantly better**
  - Characters now have expressions and movements, prompt adherence is much improved
  - *From: Zabo*

- **New distill models work at higher resolutions**
  - Can now generate at 960x960
  - *From: Zabo*

- **CineScale uses specific RoPE scaling values**
  - Original used 1, 20, 20 then 1, 25, 25 for spatial rope scaling
  - *From: DawnII*

- **CineScale LoRA possibly trained with scale of 20**
  - RoPE scaling attempts to make larger resolutions work without repeat effect
  - *From: Kijai*

- **VACE can be used for full frame inpainting to stitch videos**
  - Using 10 frames input and output with masks for smoother video connections
  - *From: Koba*

- **Torch 2.9.0 and 2.10 have VAE VRAM bug**
  - Makes conv3d operations use 3x more VRAM when using half precision, affects Wan VAE
  - *From: Kijai*

- **Accidentally combining new distill 4 step base model with 256 rank lightx2v lora massively amplifies motion**
  - When forgetting to turn off the lora while using the distill model, the combination achieves much more motion than either component alone
  - *From: Ruairi Robinson*

- **FlashVSR needs at least 2x upscale for good results**
  - Using less than 2x upscale produces poor quality, especially for faces. 4x upscale works well but uses 20GB VRAM
  - *From: Kijai*

- **RoPE frequency scaling prevents repetition artifacts at high resolutions**
  - Especially important for 1080p and up, particularly high vertical resolutions to avoid repeat patterns
  - *From: Kijai*

- **WAN models can learn detailed object features from small training sets**
  - Training a WAN LoRA on just 10 images of the same green car produced impressive detail learning, though color flexibility was limited
  - *From: Dever*

- **Wan 2.2 first frame corruption on longer generations**
  - Wan 2.2 corrupts first 5-16 frames on longer generations (121 frames). Only the 5B model is truly 24fps
  - *From: garbus*

- **FP8 vs FP16 quality difference in video extension**
  - FP/BF16 models retain much more quality than FP8 when extending videos using last frame, difference becomes huge at 25 seconds
  - *From: Zabo*

- **CFG on high noise steps improves results**
  - Adding CFG on first step or all high steps makes huge difference in test results
  - *From: Dever*

- **FlashVSR effective for fixing bad renders**
  - FlashVSR at 0.8 strength can fix up bad looking renders very nicely, only needs 1 step
  - *From: mdkb*

- **InfiniteTalk can do vid2vid for adding lipsync**
  - InfiniteTalk supports vid2vid workflow for just adding lipsync, but requires figuring out masking or it changes rest of video
  - *From: Kijai*

- **Wan VAE excellent compression for long videos**
  - Wan 2.1 VAE can encode and decode long high quality videos (16fps and 24fps tested) with minimal quality loss
  - *From: Ablejones*

- **New sageattn version that allows torch.compile reduces VRAM usage**
  - Max allocated memory reduced from 15.749 GB to 14.667 GB, with tiny speed difference
  - *From: Kijai*

- **Ditto LoRAs work with simple style transfer prompts**
  - Uses prompts like 'Make it a Japanese anime style', 'Make it Pixel Art video', etc. for video style transfer
  - *From: Kijai*

- **LoRA rank can be significantly reduced while maintaining quality**
  - Original rank 128 vs average rank 29 showed minimal quality difference
  - *From: Kijai*

- **Wan 2.1 Lightx I2V 480p still performs better than newer variants for certain tasks**
  - Better lighting and look than 2.2 lightning for low noise, though lacks motion unless at very high strength
  - *From: FL13*

- **Ditto LoRAs can turn VACE into RGB video in, stylized video out**
  - These loras are designed for style transfer from input video to stylized output
  - *From: Draken*

- **WanAnimate can do face control in addition to pose**
  - More interesting than basic pose stuff since it includes facial animation
  - *From: Kijai*

- **Vitpose pose detector can detect animals as well as humans**
  - There are also specific animal pose detectors available for use with WanAnimate
  - *From: Kijai*

- **Ditto global lora recognizes some characters**
  - Can prompt with 'make it Elsa from Frozen' and it understands the character
  - *From: DawnII*

- **Ditto full module vs LoRA comparison shows full module has less artifacting**
  - Full module seems to have less artifacting and ghosting and is more reliable than using the LoRA
  - *From: Hashu*

- **Krea model is based on Wan 2.1 and works like CausVid**
  - Supposed to be used 3 latents at a time, like causvid, but surprisingly works with 21 latents
  - *From: Kijai*

- **Krea realtime LoRA extracted from Wan 2.1 can be used on Wan 2.2**
  - Using 4 steps similar to lighting, strength 4 on HN and 1.1 on LN with HPS at 0.75 to reduce noise
  - *From: aipmaster*

- **MoCha only segments first frame, not the video**
  - It's the simplest thing ever - ref is inserted last like Phantom
  - *From: Kijai*

- **Krea realtime achieves 11fps inference speed using 4 steps on NVIDIA B200 GPU**
  - Distilled from Wan 2.1 14B using Self-Forcing technique
  - *From: Dever*

- **WoW world model can generate extremely close to real life physics**
  - Can take a photo from robot vision, say 'pick up the cup' and it makes the video for training
  - *From: Draken*

- **MoCha (from Orange-3DV-Team) is a video generation model that allows character/subject replacement using reference images and masks**
  - Model concatenates control video with mask and reference in frame dimension, requires prompting for best results
  - *From: Kijai*

- **MoCha works with context windows for longer videos**
  - Each window contains noise + mask + ref, but longer sequences can cause issues with multiple characters
  - *From: Kijai*

- **MoCha uses double frame dimension which increases VRAM usage significantly**
  - Uses about double VRAM because whole control video is concatenated in frame dimension
  - *From: Kijai*

- **Krea LoRA produces more realistic results compared to other 4-step models**
  - aipmaster reports it looks less artificial than other fast models, generates 140 seconds 720p in ~140 seconds on 4090
  - *From: aipmaster*

- **New Wan 2.2 distill LoRAs were updated**
  - lightx2v updated their Wan 2.2 distill LoRAs, marked as version 1022 (Oct 22)
  - *From: Gateway {Dreaming Computers}*

- **Rolling Forcing model released using WAN 2.1-14B**
  - New reference-to-video model, shows better temporal consistency in comparisons
  - *From: Kytra*

- **New LightX2V LoRAs dated 1022 released**
  - New LoRAs with date 1022 released but unclear if they're just renames or actual new versions
  - *From: Draken*

- **New LightX2V LoRA shows improved performance**
  - The new 1022 LoRA performs better than previous versions, especially for complex prompts that failed on older versions
  - *From: Ada*

- **QwenImage VAE converted to ComfyUI format**
  - Kijai successfully converted e2e-qwenimage-vae to ComfyUI format using Claude-generated reverse script
  - *From: Kijai*

- **QwenImage VAE shows more detail**
  - QwenImage VAE produces more detailed results compared to Wan VAE
  - *From: Kijai*

- **Rolling Force model is 1.3B with 17GB due to multiple weight copies**
  - Model contains generator, critic, and generator_ema weights, causing large file size despite being 1.3B parameters
  - *From: Kijai*

- **Stable Video Infinity (SVI) works with base 2.1 I2V model using LoRAs**
  - SVI uses base Wan 2.1 I2V 480p model with special LoRAs and code modifications for infinite video generation
  - *From: Kijai*

- **New lightx2v LoRA version released**
  - The wan2.2_i2v_A14b_high_noise_lora_rank64_lightx2v_4step_1022.safetensors is confirmed to be different from the old MoE version and performs better for 2D animation
  - *From: Kijai*

- **SVI LoRA padding mechanism**
  - In shot workflow, padding is set to -1 which pads all frames with the reference image instead of black pixels
  - *From: Kijai*

- **SVI uses different frame configurations**
  - Shot-lora uses single start image with random_ref padded for whole video length, while film lora uses 5 start images with no padding
  - *From: Kijai*

- **Multiple frames can be fed to I2V node**
  - The WanVideo ImageToVideo Encode node can accept multiple images in start_image input, same as Fun InP
  - *From: Kijai*

- **SVI reference frame structure**
  - The ref is the original init image, the first frame is the previous last frame from the generation
  - *From: Kijai*

- **SVI film LoRA works with Wan 2.2**
  - Users successfully tested SVI film LoRA with Wan 2.2 workflows, showing coherent results
  - *From: voxJT*

- **SVI uses 5 frames from end of previous generation for continuity**
  - The film LoRA uses 5 frames from the end of the previous generation to maintain motion continuity
  - *From: Kijai*

- **LightX2V released new lightweight VAE**
  - 31MB VAE that's much faster but with significant quality drop compared to standard VAE
  - *From: JohnDopamine*

- **Ditto can generate longer videos beyond 3 seconds**
  - Despite documentation suggesting 3s limit, users successfully generated 20s+ videos (600 frames)
  - *From: JohnDopamine*

- **SVI film LoRA prevents I2V model flash/saturation issues**
  - The LoRA helps maintain consistency and reduces oversaturation in I2V chaining
  - *From: voxJT*

- **SVI supports T2V by using black input image**
  - You can bypass color match nodes and use SVI with T2V by providing a black input image
  - *From: garbus*

- **SVI LoRAs work with native ComfyUI nodes**
  - Film, shot, and other SVI LoRAs converted to fp16 and native compatible format work well with native ComfyUI Wan video nodes
  - *From: Ablejones*

- **Native ComfyUI handles masking automatically for video extensions**
  - The native ComfyUI nodes create default masks and pad starting images properly without manual mask input
  - *From: Ablejones*

- **SVI-shot uses reference frame padding while SVI-film uses zero padding**
  - SVI-shot repeats the original input image for padding frames, while SVI-film uses zero padding (black frames in diffusers, 0.5 in ComfyUI)
  - *From: Kijai*

- **ComfyUI uses 0-1 scale while diffusers uses -1 to 1 scale**
  - In ComfyUI middle value is 0.5, in diffusers/original codes middle is 0. Zero padding in their code equals 0.5 padding in ComfyUI
  - *From: Kijai*

- **SVI-shot works with reference frames, SVI-film fails completely**
  - When using reference frame repetition technique, SVI-shot maintains scene continuity but SVI-film produces static output
  - *From: Ablejones*

- **MTV Crafter works better when input pose is close to target**
  - Model performs better when continuing from last frame rather than starting from very different poses, spends fewer frames transitioning
  - *From: Kijai*

- **HoloCine can generate 121 frames straight out with just weights only**
  - Kijai tested HoloCine weights without full implementation and got 121 frame generations, though it still loops and needs proper attention code
  - *From: Kijai*

- **HoloCine uses structured prompting with [character1], [character2] tags and shot descriptions**
  - Uses format like '[global caption] description [character1] details [character2] details This scene contains X shots. [per shot caption] shot descriptions [shot cut]'
  - *From: Tachyon*

- **Method to improve SVI consistency by using reference image as first frame**
  - VK found that using original reference image as first frame followed by last four frames from prior render helps maintain character consistency better than using just 5 frames from prior render
  - *From: VK (5080 128gb)*

- **InfiniteTalk provides best consistency with minimal degradation/colorshift**
  - Reported as having crazy good consistency compared to other extension methods
  - *From: seitanism*

- **Context windows are 2x+ slower per frame due to overlap mechanics**
  - 161 frames takes 4 minutes instead of 2 minutes for twice the length due to doing 3-4 runs to join just 2 segments
  - *From: blake37*

- **SVI "random ref" naming refers to training, not inference**
  - In inference code it's actually the input image that's used, called 'random ref' because for training it's random
  - *From: Kijai*

- **Different SVI LoRAs use different padding strategies**
  - Tom LoRA doesn't use padding (0), only single input for normal I2V. Dance, talk, shot use reference padding which makes sense as they mostly stay in frame
  - *From: Kijai*

- **Shot LoRA can help with degradation**
  - Shot LoRA always has the original input there as reference, unlike film which is more creative and doesn't use that
  - *From: Kijai*

- **Wan I2V can already do reference generation without MagRef**
  - Wan 2.2 I2V can take an image of a face with white around and do t2v with reference, but MagRef makes it insanely good at this task
  - *From: Draken*

- **More frames forwarded with film keeps motion better**
  - With 2.2 i2v, 16 frames forwarded with film was working pretty well for motion continuation
  - *From: DawnII*

- **5 frames has less degradation but worse motion continuation**
  - Trying with 5 frames shows less image degradation but motion continuation not as good compared to 16 frames
  - *From: DawnII*

- **Different content shows flash artifacts more**
  - Flash is most noticeable in dark scenes/areas, less noticeable in white backgrounds or sky
  - *From: Draken*

- **i2v model supports multiple frame inputs natively**
  - The i2v model actually does support multiple frame inputs natively, not just single frame
  - *From: Ablejones*

- **svi-film lora enables multi-frame input for base i2v**
  - Normal I2V doesn't do well with more than one input image, but the film loras make that work
  - *From: Kijai*

- **Position of character in reference frame dictates ViT pose starting position**
  - The position of the character in the reference frame (in screen space) dictates the starting position of the ViT pose (in screen space)
  - *From: Neex*

- **Film lora may be better to skip on first sampler**
  - When using film lora that it's better to not use it for the first sampler - it seems weird motion-wise if it starts from single image
  - *From: Kijai*

- **Two different film lora versions available**
  - There are two film loras - regular and film-opt version, with film-opt being a newer version
  - *From: Ablejones*

- **HoloCine enables long 241-frame generation in one pass without context windows**
  - User generated 720x720x241 frames (15 seconds) in one go using 3 high 3 low steps with lightx2v lora
  - *From: seitanism*

- **HoloCine sparse model enables ~1 minute video generation with similar VRAM to 81 frames**
  - Sparse model maintains almost same visual quality while enabling long coherent cinematic video generation
  - *From: mamad8*

- **SVI Shot LoRA doesn't work with Wan 2.2**
  - People have tried using SVI Shot LoRA with 2.2 but it doesn't work even when used normally
  - *From: Kijai*

- **Film LoRA can somewhat work with 2.2**
  - Unlike Shot LoRA, Film LoRA doesn't do anything special and can work with 2.2
  - *From: Kijai*

- **VAE decode/encode causes degradation that can't be avoided in latent space**
  - Multiple users confirmed that latent manipulation always causes artifacts like flashing, color shifting, or ghosting when first frame is modified
  - *From: lemuet*

- **FusionX LoRA with WAN 2.1 produces better results than with WAN 2.2 and LightX2V LoRA**
  - Based on tests comparing the combinations
  - *From: Govind Singh*

- **LongCat-Video can be run in WanVideoWrapper but doesn't work properly**
  - Result doesn't have much to do with the prompt
  - *From: Kijai*

- **Holocine high model + WAN 2.2 low model produces better quality**
  - Combines better detail from original low model with Holocine capabilities
  - *From: avataraim*

- **LongCat generates 6 second pieces in T2V, I2V, or multi-frame I2V mode**
  - Has same repeating issue as WAN when trying 12+ seconds in one go
  - *From: aikitoria*

- **WAN 2.2 works better with Qwen image inputs**
  - Qwen images are soft enough that they don't cross into detail level where VAE fails into noise grids
  - *From: aikitoria*

- **SVI film with WAN 2.2 doesn't meaningfully differ from WAN 2.2 alone**
  - WAN 2.2 already does motion continuation by itself using previous frames
  - *From: lemuet*

- **Wan 2.2 has sparse attention and distill LoRA as separate features**
  - Both are available separately for optimization
  - *From: Ada*

- **Video extension with 13 start frames works with LongCat**
  - Only works if character keeps looking at camera at end of segment
  - *From: aikitoria*

- **HoloCine generates 241 frames (15-16 seconds) in one pass**
  - Uses windowed attention where frames attend only to global caption and shot-specific captions
  - *From: shaggss*

- **SVI-Film method works with Wan 2.2 using 5-frame batches**
  - Put 5-frame batch in ImageToVideo encode node start_image input, wrapper handles automatically
  - *From: lemuet*

- **Kijai successfully merged LongCat distill LoRA by renaming layers and splitting fused components**
  - Renamed layers, split fused qkv for self attention and kv for cross attention
  - *From: Kijai*

- **LongCat handles T2V and I2V in single model**
  - Model combines t2v and i2v capabilities, released main model and 2 loras that run as separate modules
  - *From: Kijai*

- **LongCat crossattention split improvement**
  - Fixed small mistake in LongCat crossattention split so it doesn't fade
  - *From: Kijai*

- **LongCat attention split for input images**
  - Has to do attention separately for the input image(s) in LongCat, which is why it diverges from input so much
  - *From: Kijai*

- **Holocine shot control with frame cuts**
  - Can control every shot duration with frame cuts like '50,100,150,200,250' for 5 shots, giving 50 frames per shot linearly
  - *From: avataraim*

- **Resolution bucket importance for LongCat**
  - LongCat is picky about input resolution and should test with bucket resolutions. 640x608 vs 640x640 shows significant quality difference
  - *From: Kijai*

- **LongCat is 15fps by default and interpolates well to 30fps**
  - The model generates at 15fps natively, and their refine pipeline trilinear interpolates from 15fps 480p to 30fps 720p
  - *From: Kijai*

- **LongCat uses step and cfg distill LoRA**
  - With distill LoRA can use 16 steps, without it requires at least 30 steps with cfg 4.0
  - *From: Kijai*

- **LongCat I2V works like 5B or Pusa I2V**
  - Uses any number of start_frames as extra latents, code replaces that part of noise with image and sets corresponding timestep to 0
  - *From: Kijai*

- **SageAttention 1.0.6 causes first frame flash issue with LongCat**
  - Updating to SageAttention 2.2.0 or switching to SDPA fixes the I2V first frame flash problem
  - *From: Hashu*

- **fp16 precision causes black/NaN outputs with Wan models**
  - fp16 consistently produces NaN results leading to black output, bf16 works fine
  - *From: Kijai*

- **Changing to SPDA fixed black frames issue**
  - User had black frame issues that were resolved by switching attention mechanism to SPDA
  - *From: scf*

- **LongCat requires 17 frames minimum for proper extension, not 16**
  - Original code uses 13 frames, should follow the 4+1 rule. 16 frames wouldn't work proper for extension
  - *From: Kijai*

- **LongCat refinement lora runs at low sigmas without CFG**
  - Refinement lora is meant to run at low sigmas without cfg, can adjust effect with lora strength
  - *From: Kijai*

- **LongCat generates at 720p natively, not just 480p**
  - It can generate 720p on its own, though their pipeline uses 2 passes with refiner lora
  - *From: scf*

- **Holocine 241 must be at end of list or it crashes**
  - Always use 241 in end of list, otherwise crashes
  - *From: avataraim*

- **FP32 norm operations with fp8_scaled affects Wan 2.2 quality**
  - Doing all norm operations with fp32 (using fp32 weight even) with fp8_scaled has an effect in Wan 2.2
  - *From: Kijai*

- **Wan VAE noise patterns can be reduced with spacepxl's 2x upscaler VAE**
  - Custom trained VAE decoder that acts as free 2x upscaler and kills noise grid patterns for images
  - *From: spacepxl*

- **NeatVideo can filter out Wan VAE noise patterns in video**
  - Enable temporal and set spatial to low weight or disabled to preserve detail while removing noise
  - *From: spacepxl*

- **Magref can be used as low noise model in Wan 2.2 workflows**
  - Using Magref with right loras for Wan 2.2 low noise reduces context window artifacts and improves image quality
  - *From: blake37*

- **Uni3C controlnet needs higher strength at larger resolutions**
  - Works well at 512x512 but needs increased strength for higher resolutions, should not increase strength on low noise side
  - *From: Kijai*

- **LongCat refinement lora scaling issue fixed**
  - Modulation layers were merged with alpha 0.5 but forgot to scale properly, causing it to not work well at 1.0 strength
  - *From: Kijai*

- **WAN 2x VAE provides significant quality improvements with sharper images and better detail**
  - Works with existing WAN models using same encoder/latent space, decoders are cross compatible
  - *From: spacepxl*

- **Holocine implementation now includes proper attention code rather than just weights**
  - Shot attention requires structured prompt metadata and text_cut_positions for multi-shot generation
  - *From: NebSH*

- **LongCat refinement LoRA works at strength 1.0 with specific sampling parameters**
  - Use 50 steps with Euler or UniPC, start from step 45, CFG 1.0
  - *From: Kijai*

- **Video extension workflows use vid2vid process starting at later steps like really low denoise**
  - Original code decodes, upscales in pixel space, encodes and runs as vid2vid
  - *From: Kijai*

- **Smooth window parameter in Holocine creates interesting transition effects between different scenes**
  - Values tested include 0, 6, and 12 smooth window settings
  - *From: NebSH*

- **VRAM usage difference between operating systems**
  - 4GB less VRAM used on Linux compared to Windows with torch compile
  - *From: Kijai*

- **Memory cleanup node significantly reduces RAM usage**
  - Using Comfyui-Memory_Cleanup node reduced RAM usage from 99% to 45%, and generation time from 400s to 100s on 3060
  - *From: avataraim*

- **VACE WAN 2.2 dual model workflow can run on 3060**
  - Can run VACE WAN 2.2 dual model workflow with controlnet to 720p in 16 minutes on a 3060
  - *From: mdkb*

- **PyTorch RAM reservation behavior**
  - PyTorch can't literally move something from RAM to VRAM, it reserves the same amount from RAM
  - *From: Kijai*

- **Qwen VL by AI lab OOMs on high resolution images**
  - OOMs on 2K resolution images, works fine when using resize node at 512x512
  - *From: hicho*

- **LongCat uses Wan 2.1 VAE but has significant architectural differences**
  - Uses Wan architecture but trained from scratch with adjustments to model size and structure
  - *From: JohnDopamine*

- **Wan 2.2 I2V can do multi-frame interpolation without any LoRA**
  - Base Wan 2.2 I2V model naturally supports interpolation between multiple frames
  - *From: Kijai*

- **Morph LoRA appears to be mostly regular Wan 2.2 functionality**
  - Testing shows 95% of functionality is just Wan 2.2 A14B I2V, LoRA provides minimal improvement
  - *From: Kijai*

- **LightX2V 1030 model significantly improved performance**
  - New wan2.2_i2v_A14b_high_noise_lightx2v_4step_1030.safetensors model shows substantial quality improvements over previous versions
  - *From: Zabo*

- **Torch compile causes 50% VRAM increase but 2x speed drop in some cases**
  - User found disabling torch compile reduced VRAM from 15.5+2 shared to 11.3GB plain, speed dropped from 27 it/s to 57 it/s overall
  - *From: Gleb Tretyak*

- **New LoRA storage method improves block swap efficiency**
  - Unmerged LoRAs are now stored as buffers in layers themselves, moved WITH block swap instead of always CPU to GPU
  - *From: Kijai*

- **ChronoEdit uses Wan for image editing**
  - NVIDIA's ChronoEdit model is based on Wan 14B and uses temporal understanding for image edits, working surprisingly well
  - *From: aikitoria*

- **LongCat provides motion continuity through multi-frame input**
  - Can start from multiple frames to maintain motion continuity, which regular Wan with Lynx IP embeds cannot achieve
  - *From: Kijai*

- **ChronoEdit uses temporal reasoning tokens during generation**
  - Model can put whatever it wants in intermediate frames as long as it helps get to the right final result - intermediate frames work like register tokens
  - *From: spacepxl*

- **ChronoEdit works at 81 frames beyond its 29 frame design**
  - Kijai successfully tested it at 81 frames despite being designed for 29 frames
  - *From: Kijai*

- **ChronoEdit temporal reasoning mode modifies input for specific steps**
  - Code selects first and last frame when temporal reasoning is enabled
  - *From: Kijai*

- **New LightX2V 1030 LoRA has better camera control**
  - Specifically stated no camera movement and previous failed with crazy zoom, newest didn't move camera and did wanted character motion
  - *From: Gleb Tretyak*

- **VRAM requirements differ significantly between Chinese cards and NVIDIA**
  - Huawei Atlas 300I DUO has 96GB for $1.5k but much lower performance (TOPS rating like 30 series) vs RTX 6000 Pro at $10k
  - *From: Aaron_PhD*

- **ChronoEdit is a Wan finetune that takes an image and creates a video where the last frame is the edited version**
  - It was trained on 5 frames (normal) and 29 frames ('temporal reasoning' mode)
  - *From: Kiwv*

- **ChronoEdit uses Qwen VL for prompt enhancement**
  - There are 3 ComfyUI implementations available for Qwen VL
  - *From: aikitoria*

- **LongCat was trained on video extension**
  - Could pass in 30 frames and get 60 out
  - *From: Kiwv*

- **LongCat can do 6 second segments with multi start frames on I2V for extension with motion continuity**
  - But has no reference images support, so if character turns around it becomes useless
  - *From: aikitoria*

- **FlashVSR 1.1 has been released**
  - New version available on HuggingFace
  - *From: yi*

- **New wan2.2_lightx2v_1030 LoRA has been released**
  - Available in Kijai's repo at /LoRAs/Wan22_Lightx2v/
  - *From: avataraim*

- **LightX LoRA can generate 5-second segments with only 4 steps**
  - Takes about 12 minutes to generate 1 minute long video this way, though motion is not totally continuous
  - *From: aikitoria*

- **ChronoEdit has a distill LoRA included**
  - Found Wan_2_1_I2V_14B_ChronoEdit_distill_lora_rank32.safetensors in the repo, mentioned in paper
  - *From: mamad8*

- **Qwen Edit at 40 steps produces significantly sharper outputs**
  - 40 steps is night and day different for the sharpness of qwen edit outputs
  - *From: aikitoria*

- **ChronoEdit removes image softening effect**
  - It mostly removes that effect of the image being softened that happens with Qwen
  - *From: aikitoria*


## Troubleshooting & Solutions

- **Problem:** PC crashes when generating images after working fine with videos
  - **Solution:** Hardware-related issue, may need system diagnostics
  - *From: Drommer-Kille*

- **Problem:** Memory issues with 162 frames using 81 length context windows
  - **Solution:** Increase disk swap size, use --cache-none option, or try --highvram/--gpu-only/--normalvram flags
  - *From: Ablejones*

- **Problem:** DWPose Estimator taking 17 minutes for 10sec clip
  - **Solution:** Change bbox detector to .torchscript format, reduces time from 17min to 3min
  - *From: xiver2114*

- **Problem:** Preview nodes with multiple frames slow down ComfyUI
  - **Solution:** Delete preview node completely, not just bypass it, to fix the performance issue
  - *From: mdkb*

- **Problem:** VRAM not clearing properly between workflow runs
  - **Solution:** Need to restart ComfyUI when caught, ongoing issue since recent updates
  - *From: mdkb*

- **Problem:** Missing detection model file backbone.blocks.21.norm2.bias
  - **Solution:** VitPose H model needs the .bin file in addition to other model files
  - *From: Kijai*

- **Problem:** Face detection error with wrong aspect ratio
  - **Solution:** Make sure resolution matches video aspect ratio, swapping width/height causes detection failures
  - *From: Gateway {Dreaming Computers}*

- **Problem:** Black video output with palingenesis i2v model
  - **Solution:** Model appears to be busted or incorrectly uploaded
  - *From: FL13*

- **Problem:** Pose detection taking too long
  - **Solution:** Install onnxruntime-gpu to run on GPU instead of CPU
  - *From: Kijai*

- **Problem:** Can't add denoise to I2I workflow
  - **Solution:** Denoise appears fixed at 1.0 in certain samplers, defeating I2I purpose
  - *From: Kenk*

- **Problem:** Face shaking with movement in new WanAnimate workflow
  - **Solution:** Issue occurs with new preprocessor workflow, older workflow didn't have this problem
  - *From: Kevin "Literally Who?" Abanto*

- **Problem:** Losing face likeness in WanAnimate without LightX LoRA
  - **Solution:** Reduce pose strength and increase face strength, or use LightX LoRA which preserves face better
  - *From: 🦙rishappi*

- **Problem:** Pose lines appearing in VACE output
  - **Solution:** Usually caused by improper composite blending, root cause is the composite method
  - *From: A.I.Warper*

- **Problem:** Overexposure degradation in long WanAnimate runs
  - **Solution:** Use LCM if not already, make settings less strong, use fewer steps, or try context windows instead of frame windowing
  - *From: Kijai*

- **Problem:** Slow CPU performance on cloud setups
  - **Solution:** Cloud setups often have subpar CPU performance, consider using GPU optimized nodes
  - *From: Kijai*

- **Problem:** LoRA seems sped up
  - **Solution:** Make sure video is set to correct fps (16fps)
  - *From: Ryzen*

- **Problem:** HuMO changes ref image significantly
  - **Solution:** Use I2V version of LightX2V LoRA instead of T2V version, avoid FastWan LoRA
  - *From: mdkb*

- **Problem:** Snow/dust artifacts in WAN Animate
  - **Solution:** Add artifacts to negative prompt to prevent them appearing again
  - *From: Charlie*

- **Problem:** ComfyUI queue breaking
  - **Solution:** SyntaxError from unexpected JSON character at position 4
  - *From: Drommer-Kille*

- **Problem:** Flickering black blocks in Wan Animate output
  - **Solution:** Enable the fl2v switch on the node for 2.2 models
  - *From: Kijai*

- **Problem:** Character LoRAs not working in Wan 2.2 Animate
  - **Solution:** Use only 2.1 LoRAs or use only the Low Noise LoRA from 2.2 MOE at weight 1.0, since Wan Animate is based on 2.1
  - *From: Screeb*

- **Problem:** OVI permission errors on Windows
  - **Solution:** Need to change code in io_utils.py file, specific fix shared privately
  - *From: slmonker(5090D 32GB)*

- **Problem:** Body deformations in Wan 2.2 LoRA training
  - **Solution:** Train High Noise and Low Noise LoRAs separately instead of together to avoid deformations
  - *From: Kytra*

- **Problem:** Onnxruntime-gpu crashes in ComfyUI-WanAnimatePreprocess
  - **Solution:** Issue reported but specific solution not provided in discussion
  - *From: Kevin "Literally Who?" Abanto*

- **Problem:** Negative prompt not working with CFG 1.0
  - **Solution:** Use NAG node - CFG at 1.0 ignores negative prompt embed by design
  - *From: Kytra*

- **Problem:** OVI installation flash attention errors
  - **Solution:** Try skipping flashattn or compile from scratch, may need CUDA 12.4 headers
  - *From: seitanism*

- **Problem:** Conda environment conflicts when creating new env while another is active
  - **Solution:** Deactivate current environment before creating/activating new one to prevent cross-contamination
  - *From: seitanism*

- **Problem:** OOM issues during generation cancellation
  - **Solution:** Don't cancel generation during 2nd (low noise) sampler stage as it doesn't properly offload the model
  - *From: seitanism*

- **Problem:** ONNX runtime errors in Animate v2
  - **Solution:** Update/re-install onnxruntime-gpu and onnx, uninstall onnxruntime (without -gpu), or run on CPU
  - *From: Kijai*

- **Problem:** ONNX Runtime JIT compilation error on RTX 50-series GPUs
  - **Solution:** Set ONNX device to CPU for WanAnimate preprocessing nodes
  - *From: D-EFFECTS*

- **Problem:** Black mask box around WanAnimate V2 output
  - **Solution:** Add black images instead of disconnecting face input, or ensure face strength is 1.0+ when using masking
  - *From: Kijai*

- **Problem:** Weird noise pattern with Native Wan Animate
  - **Solution:** Issue appears with WanAnimatePreprocess template but not with wrapper
  - *From: Nekodificador*

- **Problem:** Video gets more color contrast over time in I2V
  - **Solution:** Model struggles to maintain style across 81 frames, especially with conflicting LoRA training data
  - *From: Draken*

- **Problem:** Static scene wobble/shake and dust/grain effects
  - **Solution:** No specific solution provided, user seeking help
  - *From: humangirltotally*

- **Problem:** Black video output
  - **Solution:** Check resolution - must be multiples of 64, with video token number divisible by 128
  - *From: GalaxyTimeMachine (RTX4090)*

- **Problem:** GGUF compatibility error with dtype mismatch
  - **Solution:** Fixed by Kijai - Byte and Half dtype issue resolved
  - *From: Gigi8*

- **Problem:** Vitpose and YOLO models not found in custom paths
  - **Solution:** Use symlinks - models are only picked from ComfyUI absolute path
  - *From: Gigi8*

- **Problem:** Wan Animate doesn't work with Uni3C
  - **Solution:** Disconnect both bg_images and mask inputs
  - *From: Kijai*

- **Problem:** Blurry outputs in I2V
  - **Solution:** Use multiples of 64 for resolution, try 1280x720 instead of 800x800
  - *From: mallardgazellegoosewildcat*

- **Problem:** OVI resolution changing not working
  - **Solution:** Bug in RH-ovi node where setting 720p still outputs 544 res video
  - *From: slmonker(5090D 32GB)*

- **Problem:** Pixelated/blurry outputs on default workflow
  - **Solution:** Switch from FP8 scaled model to FP16 model
  - *From: Ryzen*

- **Problem:** ImageResizeKJv2 node failing with latest ComfyUI updates
  - **Solution:** Re-set the per_batch parameter to 0 or desired value due to bug where new widgets in old workflows don't get default values
  - *From: Kijai*

- **Problem:** OVI node showing as red/unavailable after installation
  - **Solution:** Check console for missing dependencies and pip install them (e.g., pydub)
  - *From: Thom293*

- **Problem:** SageAttn3 not working on RTX 6000 Pro
  - **Solution:** SageAttn3 is Blackwell-only (B200/B300 cards), won't work on older cards
  - *From: Kijai*

- **Problem:** Burned-in look from too many end-frame I2V continuations
  - **Solution:** Use USDU upscale in latent space with VACE Wan 2.2 dual model workflow, masking seams and low denoise upscale/detail runs
  - *From: mdkb*

- **Problem:** Radial attention error with 'sm_120' processor and LLVM ERROR: Cannot select: intrinsic %llvm.nvvm.shfl.sync.bfly.i32
  - **Solution:** Install SpargeAttn package from https://github.com/woct0rdho/SpargeAttn/releases and add dense attention settings node
  - *From: Kijai*

- **Problem:** Palingenisis model producing black boxes with i2v
  - **Solution:** Use insight version or switch to smoothmix which many people prefer
  - *From: FL13*

- **Problem:** OVI installation errors and frustration
  - **Solution:** Wait for native ComfyUI wrapper implementation that's being worked on
  - *From: D-EFFECTS*

- **Problem:** KeyError: 'vace_blocks.0._orig_mod.self_attn.q.weight' when using lightx loras with Fun-VACE
  - **Solution:** Update wrapper, commit a few hours ago to address
  - *From: DawnII*

- **Problem:** OVI workflow not working properly
  - **Solution:** Load ovi video on main loader and ovi audio on extra, use default rope for now
  - *From: patientx/Kijai*

- **Problem:** Slow generation on 5090 with offloading
  - **Solution:** Keep model in VRAM, no offload. With offload it's slow as an old car
  - *From: slmonker(5090D 32GB)*

- **Problem:** NaNs with fp16
  - **Solution:** Use bf16 instead as I had some NaNs with fp16 before
  - *From: Kijai*

- **Problem:** Installing sageattention
  - **Solution:** Don't use ChatGPT as a guide to install sageattention. Everything just broke
  - *From: Zabo*

- **Problem:** OVI model producing noise output
  - **Solution:** Try using sageattn instead of sdpa
  - *From: TransformerMan*

- **Problem:** e4m3fn_scaled not working on 3090 after fresh install
  - **Solution:** Use e5m2 instead - e4 doesn't actually work on 3000 series GPUs
  - *From: Kijai*

- **Problem:** Tiled VAE with VACE extend creates blurry output and position shift
  - **Solution:** Issue with tile size calculation - original defaults are tile_size=(34, 34), tile_stride=(18, 16)
  - *From: Kijai*

- **Problem:** Scaled FP8 models not working without selecting scaled option
  - **Solution:** Scaled FP8 weights don't work without the scaling - need 'scaled_fp8' key in model metadata
  - *From: Kijai*

- **Problem:** Sage attention causing blank outputs with Wan 2.2 animate
  - **Solution:** Switch to different attention mechanism
  - *From: berserk4501*

- **Problem:** Models producing noisy output when not using scaled option
  - **Solution:** If model shows as scaled when loaded, it must be handled as scaled
  - *From: Dita*

- **Problem:** ImageResizeKJv2 node per_batch conversion error
  - **Solution:** Set per_batch to 1 instead of NaN value
  - *From: NoHuman*

- **Problem:** dtype mismatch error: Half and Float8_e4m3fn
  - **Solution:** Switch from v2 to v1 of Wan2_2-Animate-14B_fp8_e4m3fn_scaled_KJ model
  - *From: neitherchef*

- **Problem:** Wan animate generating unchanged video with black artifacts
  - **Solution:** Check that mask is being processed correctly by the sampler and inputted correctly on the wanvideo animate embeds node
  - *From: happy.j*

- **Problem:** ComfyUI files not saving to output folder
  - **Solution:** Files can be found in tmp folder when this happens. API nodes don't save to temp folder
  - *From: Drommer-Kille*

- **Problem:** OOM errors on 32GB VRAM after few runs
  - **Solution:** Bypass or remove blockcache node entirely instead of setting blockcache to 0
  - *From: lostintranslation*

- **Problem:** Videos coming out very dark with OVI
  - **Solution:** Certain scene prompts can cause this darkness issue
  - *From: U̷r̷a̷b̷e̷w̷e̷*

- **Problem:** 5090 crashing with VRAM temperature not accessible
  - **Solution:** Check GPU power connector and system RAM fitting - power connection issues can cause crashes and memory errors
  - *From: Zabo*

- **Problem:** RTX 5090 crashes with black screen and freezing
  - **Solution:** Remove second GPU from dual GPU setup, update to PyTorch 2.7 or 2.9 (avoid 2.8), check PCIe configuration
  - *From: Charlie*

- **Problem:** PyTorch 2.8.0 causing stability issues
  - **Solution:** Use PyTorch 2.7.0 or 2.9.0 instead, 2.8.0 has known problems
  - *From: Tony(5090)*

- **Problem:** First frame flash in VACE 2.2
  - **Solution:** Try lowering CFG scale start to 1.5 or lower, use Lora Block Edit node to switch off first block
  - *From: Rainsmellsnice*

- **Problem:** 5090 FE crashes during inference
  - **Solution:** Power limit GPU to 70% for stability, may be power phase related issue
  - *From: seitanism*

- **Problem:** Alpha transparency in Wan workflow conversion
  - **Solution:** Use proper VAE - 2.2 VAE is needed for 5b model, not TAE
  - *From: Juampab12*

- **Problem:** New Lightx2v LoRA from repo produces glitchy output with lines of noise
  - **Solution:** Use Kijai's extracted LoRA version instead, or use 12 steps minimum
  - *From: Ashtar*

- **Problem:** LoRA shows 'lora key not loaded' errors in console
  - **Solution:** Use the full model or Kijai's properly extracted LoRA
  - *From: Ashtar*

- **Problem:** Ghosting issues with new Lightx2v MoE on simple scheduler
  - **Solution:** Switch to linear quadratic scheduler
  - *From: FL13*

- **Problem:** Need higher steps to avoid ghosting with speed LoRAs
  - **Solution:** Turn up number of steps, ghosting goes away with more steps
  - *From: Zabo*

- **Problem:** Super burned out results with scheduler
  - **Solution:** At low steps you really need the schedule to be precise. Ideally for distil use the schedule it was trained with
  - *From: mallardgazellegoosewildcat*

- **Problem:** Torch compile not worth using with CFG scheduler
  - **Solution:** Because it calls each step with different CFG, it's not worth using torch compile as it will just slow things down due to recompiling
  - *From: GalaxyTimeMachine (RTX4090)*

- **Problem:** Model reloading slowing down CFG scheduler
  - **Solution:** Look into model patch wrapper functions or cfg patches to patch without reloading. Use pre and post cfg functions for dynamic CFG changes
  - *From: Kijai*

- **Problem:** Vertical line artifacts only on widescreen aspect ratios
  - **Solution:** Artifacts happen on both LoRA and finetune versions for landscape/16:9 images but not on portrait images
  - *From: blake37*

- **Problem:** OVI audio latents error
  - **Solution:** Change from fp32 to bf16 on the OVI MMaudio VAE node
  - *From: Colin*

- **Problem:** fp8 compile errors on 3000 series
  - **Solution:** Use triton 3.4+ build with fp8 patches, or switch to e5m2 models instead of e4m3
  - *From: phazei*

- **Problem:** SageAttention DLL import error with '_fused' module
  - **Solution:** Check torch version matches sageattention version, ensure CUDA torch is installed (not CPU-only), add torch DLL folder to PATH
  - *From: woctordho*

- **Problem:** FP8 models not working on older GPUs with 'fp8e4nv not supported' error
  - **Solution:** Leave quantization disabled when using fp8 models on unsupported architectures like RTX 3060
  - *From: U̷r̷a̷b̷e̷w̷e̷*

- **Problem:** OOM issues with FlashVSR on limited VRAM
  - **Solution:** Use text encode cache version to offload cache to file and remove from memory after use
  - *From: mdkb*

- **Problem:** WebM video save error in VACE workflows
  - **Solution:** Change codec/format to h264 instead of webm
  - *From: Kijai*

- **Problem:** Recent ComfyUI update causing OOM on decode
  - **Solution:** Remove fp16_accumulation from startup script, or downgrade resolution to 832x480
  - *From: Ashtar*

- **Problem:** VAE decode crashes after ComfyUI 0.3.65 update with PyTorch 2.9.0
  - **Solution:** Switch VAE to fp32 precision or use Kijai's workaround in WanVideoWrapper
  - *From: Martin_H*

- **Problem:** 1280x720 resolution breaks generation
  - **Solution:** Issue seems related to Triton connection being broken with new update
  - *From: Martin_H*

- **Problem:** FlashVSR produces ghosting with rapid movements when using FlashVSR VAE
  - **Solution:** Use full Wan VAE instead of FlashVSR VAE for better quality with less artifacts
  - *From: Elvaxorn*

- **Problem:** FlashVSR over-sharpness issue
  - **Solution:** Use denoise settings to reduce excessive sharpness, though it may cause color shifts
  - *From: Elvaxorn*

- **Problem:** OOM errors on imagetovideoencode node after ComfyUI update
  - **Solution:** Change encoder to fp32
  - *From: Charlie*

- **Problem:** Long video OOM during resizing for upscaling
  - **Solution:** Process in batches using load video node and meta batch manager
  - *From: Lodis*

- **Problem:** Ghosting/double images with new distill models
  - **Solution:** Switch sampler to uni_pc instead of euler
  - *From: aikitoria*

- **Problem:** Temporal consistency issues when chunking videos
  - **Solution:** Use overlaps (10-20% of frames) when stitching, avoid latent space operations
  - *From: happy.j*

- **Problem:** VRAM issues causing runs to lock up and 'Exception in thread Thread-21' errors
  - **Solution:** Roll back to October 10-11 commit where everything was working fine
  - *From: Miku*

- **Problem:** MOE lora produces wobbly outputs in I2V workflows
  - **Solution:** Use simple unipc on both samplers with 2/2 steps, or try 2.1 LoRA at 3.0 strength with cfg instead
  - *From: Draken*

- **Problem:** FlashVSR produces grid noise/texture that doesn't match video motion
  - **Solution:** This is typical diffusion 'vines' and 'salt' artifacts - at least it doesn't try to resolve motion blur like other upscalers
  - *From: Mads Hagbarth Damsbo*

- **Problem:** WanAnimate cutting off hair in reference images
  - **Solution:** Check resize settings - currently set to 'stretch' by default in KJ workflow
  - *From: BobbyD4AI*

- **Problem:** Wan 2.2 first frame corruption on longer gens
  - **Solution:** Trim first 16 frames or so, or use 5B model for true 24fps
  - *From: garbus*

- **Problem:** Torch compile VRAM issues after ComfyUI update
  - **Solution:** Update ComfyUI - recent fix for pytorch 2.9 issues available
  - *From: JohnDopamine*

- **Problem:** VRAM bloat and weird workflow fails
  - **Solution:** Remove 'ComfyUI Essential' custom node preview nodes - unmaintained for 10 months
  - *From: mdkb*

- **Problem:** OOM on VAE decode
  - **Solution:** Switch to tiled VAE decode when hitting VRAM limits
  - *From: mdkb*

- **Problem:** WanVideoScheduler node broken
  - **Solution:** Scheduler doesn't have lower method - fixed in latest update
  - *From: pagan*

- **Problem:** Torch compile produces oversaturated rainbow output
  - **Solution:** Don't use 'fullgraph' option on torch compile
  - *From: phazei*

- **Problem:** 'WanModel' object has no attribute 'multitalk_audio_proj'
  - **Solution:** Error occurs when using T2V model instead of appropriate model for MultiTalk
  - *From: Draken*

- **Problem:** Getting noise when using 10+10 steps setup
  - **Solution:** Issue was resolved automatically in recent ComfyCloud update, now works out of the box
  - *From: Drommer-Kille*

- **Problem:** WanModel object has no attribute 'multitalk_audio_proj' error
  - **Solution:** Occurs when trying to use multitalk without having multitalk model loaded
  - *From: Kijai*

- **Problem:** HuggingFace download failures
  - **Solution:** Use HF_HUB_DISABLE_XET=1 and HF_HUB_ENABLE_HF_TRANSFER=0 environment variables
  - *From: Kijai*

- **Problem:** Save Latents node crashing ComfyUI
  - **Solution:** New issue reported, no solution provided yet
  - *From: mdkb*

- **Problem:** Woman getting stuck in generation
  - **Solution:** Decrease LoRA strength, or remove ffn layers from lightx2v (like causvid v2 lora approach)
  - *From: Gateway/Kijai*

- **Problem:** Ditto LoRAs break other VACE functionalities
  - **Solution:** This is expected behavior when using style transfer LoRAs
  - *From: Draken*

- **Problem:** Memory error: Unable to allocate 29.3 GiB for array
  - **Solution:** Try --cache-none command line flag to prevent cached stuff from building up, reduce frame count
  - *From: Gateway*

- **Problem:** Video breaks at more than 10 steps on High model
  - **Solution:** Update ComfyUI - this was a known issue that got fixed
  - *From: Zabo/JohnDopamine*

- **Problem:** Context windows with uni3c camera control not working
  - **Solution:** Update Kijai's nodes - bug was just fixed
  - *From: Kijai*

- **Problem:** Audio out of sync when combining video
  - **Solution:** Align FPS between input video and output - input had 24fps while output was 16fps
  - *From: BobbyD4AI*

- **Problem:** High sampler adding too much noise at the end, making video unrecognizable
  - **Solution:** Increase shift value - double it to at least 16. High noise model meant to operate on high sigmas
  - *From: Kijai*

- **Problem:** Mocha shape error '[127776, 1, -1]' is invalid for input
  - **Solution:** Update and clear triton cache - it's triton cache bullshit
  - *From: Kijai*

- **Problem:** VACE just stopping after making masks with no errors
  - **Solution:** No specific solution provided in discussion
  - *From: amli*

- **Problem:** Context window tensor mismatch with MoCha
  - **Solution:** Update to latest version - context windows should work again
  - *From: Kijai*

- **Problem:** Shape mismatch error with two reference images in MoCha
  - **Solution:** Kijai provided fix for weights being masked
  - *From: scf*

- **Problem:** dtype error 'Half and Float8_e4m3fn' with Wan 2.2 animate workflow
  - **Solution:** Issue likely with scheduler or model loading setup
  - *From: topmass*

- **Problem:** Sage attention error on RTX 6000 PRO
  - **Solution:** GPU compute capability issue, not node related, user reverted
  - *From: HeadOfOliver*

- **Problem:** VRAM error 'Expected size 48 but got size 16' with MoCha
  - **Solution:** Was using wrong VAE, switching to correct VAE fixed it
  - *From: VK (5080 128gb)*

- **Problem:** Wan 2.2 inpainting with VACE adding strange artifacts in final result
  - **Solution:** Disable HPS (Human Preference Score) node, use simpler NAG negative prompts
  - *From: Kijai*

- **Problem:** Wan 2.1/2.2 videos play once then show as corrupted on Linux
  - **Solution:** Likely codec/driver related issue, need to update OpenGL drivers and use VLC player
  - *From: Provydets*

- **Problem:** LoRA key not loaded errors with new LightX2V LoRA
  - **Solution:** The diff_m modulation keys don't seem to do anything when loaded and can be ignored
  - *From: Kijai*

- **Problem:** Running out of VRAM with I2V + 3-4 LoRAs
  - **Solution:** Use --reserve-vram 2 on Windows, ensure ComfyUI is updated to fix torch 2.9 3x VRAM bug
  - *From: Kijai*

- **Problem:** Triton installation not working
  - **Solution:** Don't use torch.compile node or download wheel from ComfyUI wheels repo
  - *From: Kijai*

- **Problem:** VHS node webm encoding errors
  - **Solution:** Check the VHS node video format settings, use VHS video combine with h264 format for better system compatibility
  - *From: Kijai*

- **Problem:** CUDA runtime error mid-render
  - **Solution:** Rebuild CUDA paths to point to conda environment libraries instead of system CUDA
  - *From: HeadOfOliver*

- **Problem:** Video playback issues in Linux
  - **Solution:** Use VHS Video Combine node with h264 format instead of default save video node
  - *From: Kijai*

- **Problem:** Ditto giving 'WanModel' object has no attribute 'vace_patch_embedding' error
  - **Solution:** Need to download global model from Google Drive, not HuggingFace, or use VACE model normally with Ditto LoRA
  - *From: Gentleman bunny*

- **Problem:** WSL getting OOM on 480p generation
  - **Solution:** Create .wslconfig file with memory=60GB and swap=60GB settings, restart WSL
  - *From: seitanism*

- **Problem:** Points Editor canvas not rendering in ComfyCloud
  - **Solution:** Browser compatibility issue, check browser console for errors
  - *From: Nekodificador*

- **Problem:** EasyCache causing quality degradation and warping
  - **Solution:** Lower threshold values (0.06 caused issues), may not work well with Wan 2.2
  - *From: seitanism*

- **Problem:** SVI quality degrading over time in chains
  - **Solution:** Use 'shot' LoRA which fills empty frames with initial input to help against degradation
  - *From: Kijai*

- **Problem:** Light/Tiny VAEs don't load in native
  - **Solution:** Requires code changes, not currently supported
  - *From: Kijai*

- **Problem:** WSL performance issues and disk space filling rapidly
  - **Solution:** Set dynamic to false in torch compile, block swap debug to false, non-blocking true. Consider native Linux or Windows instead
  - *From: seitanism*

- **Problem:** SVI LoRAs not working in native
  - **Solution:** Original models are fp32 LoRAs in diffsynth format, need conversion to fp16 safetensors for ComfyUI native
  - *From: Kijai*

- **Problem:** FlashVSR OOM errors
  - **Solution:** Change attention from SDPA to sage attention
  - *From: patientx*

- **Problem:** MTV Crafter pose detection issues
  - **Solution:** Different predictor versions need different inputs, ensure input pose is close to target pose
  - *From: Kijai*

- **Problem:** SVI causing character degradation and color shifts during extension
  - **Solution:** Use VK's method of including original reference image as first frame in each new render sequence
  - *From: VK (5080 128gb)*

- **Problem:** Context window artifacts and ghosting at transitions
  - **Solution:** Need to batch 4 generations to hopefully get 1 good one without artifacts
  - *From: blake37*

- **Problem:** Random reference frame appearing in SVI extended videos
  - **Solution:** Delete the stray frame in post-processing using After Effects or use 'image from batch' node to exclude specific frames
  - *From: VK (5080 128gb)*

- **Problem:** Can't get Sage Attention 2 in WanWrapper
  - **Solution:** Can't have sage1 and sage2 installed simultaneously - it uses whichever version you have installed
  - *From: Kijai*

- **Problem:** SVI film example script issues with padding
  - **Solution:** When ref_pad_num is set to 0, there's no special padding applied - contrary to what developers claimed
  - *From: Kijai*

- **Problem:** Flash artifacts in SVI continuations
  - **Solution:** Use different seeds for each generation, same seed makes burning worse. Also less noticeable in bright areas like sky
  - *From: Kijai*

- **Problem:** Grey frame appearing with 4 frames instead of 5
  - **Solution:** 4 frames = full latent, freaks out not having a starting image for the next. Stick to 5 frames
  - *From: Draken*

- **Problem:** SVI LoRAs not working well on 2.2
  - **Solution:** No 2.1 LoRA works proper on 2.2 high noise, it's too different. Try increasing LoRA strength for high noise or use 2.1
  - *From: Kijai*

- **Problem:** VAE encode/decode degradation in extensions
  - **Solution:** Taking last frames, decoding and re-encoding has big limit. VAE isn't perfect and degrades over time, unlike framepack which worked with latents
  - *From: Draken*

- **Problem:** Code bug preventing proper reference padding
  - **Solution:** Fun inpaint code was zeroing out frames, needed to be fixed to allow proper reference padding in shot method
  - *From: Kijai*

- **Problem:** Reference padding bug was fixed recently
  - **Solution:** Kijai fixed a bug with ref frame padding - previous versions would zero out reference frames when using temporal masks
  - *From: Kijai*

- **Problem:** Film lora freezes with reference frames
  - **Solution:** svi-film lora WILL NOT work with reference frames and WILL freeze - this is correct behavior. Only works with shot/talk/dance loras
  - *From: Ablejones*

- **Problem:** Flashing between extensions
  - **Solution:** Update to latest version for ref frame padding bug fix, use merged lora instead of unmerged, avoid reference padding which can limit movement
  - *From: Kijai*

- **Problem:** ViT pose cropping issue
  - **Solution:** Turn off padding in the draw vit pose node to fix cropping, though positioning becomes an issue
  - *From: Neex*

- **Problem:** Masking confusion between wrapper and native
  - **Solution:** In wrapper: black masks for overlap frames. In native ComfyUI: white masks for overlap frames. But for svi-film with 5 frames, no masks needed
  - *From: Ablejones*

- **Problem:** ComfyUI freezing at Image Batch Multi node
  - **Solution:** Check temp folder before doing anything else - it usually keeps generated videos there
  - *From: JohnDopamine*

- **Problem:** UnicodeDecodeError when using experimental args
  - **Solution:** Error relates to torch inductor compilation, may be system-specific encoding issue
  - *From: NebSH*

- **Problem:** Slow model loading times on RunPod
  - **Solution:** Copy models from ComfyUI network volume to temp folder at root of machine
  - *From: mamad8*

- **Problem:** Video flickering every 5s when using SVI-film lora or opt model
  - **Solution:** SVI-film model works fine, issue appears specific to lora/opt variants
  - *From: army*

- **Problem:** WAN 2.2 not working after moving regions, suggesting insufficient VRAM
  - **Solution:** Check if torch was updated to 2.9 which may cause issues
  - *From: conjark*

- **Problem:** Holocine generates pixelated and noisy results
  - **Solution:** Use same workflow as WAN 2.2, just replace the models
  - *From: avataraim*

- **Problem:** ComfyUI crashes when using video attention split
  - **Solution:** Happens when compiling torch, cause unknown
  - *From: avataraim*

- **Problem:** WAN sometimes turns into anime mode for T2I
  - **Solution:** Try adding terms like lens flare that wouldn't appear in anime, or put 'anime' in negative prompt
  - *From: TimHannan*

- **Problem:** HoloCine doesn't work in fp16, gets NaNs instantly
  - **Solution:** Must use fp32
  - *From: Kijai*

- **Problem:** Wan T2I giving bad results without distill LoRA
  - **Solution:** Try upping the weight or use distill LoRA
  - *From: Ada*

- **Problem:** SVI Film workflow not working on second run
  - **Solution:** Text embeds were missing on second generation
  - *From: VK (5080 128gb)*

- **Problem:** Official HoloCine code is vastly slower than claimed benchmarks
  - **Solution:** Code needs optimization, claimed speeds don't reflect actual implementation
  - *From: aikitoria*

- **Problem:** Video upscaling preserves WAN VAE noise grids
  - **Solution:** No known fix - SeedVR2 and Topaz Starlight both preserve the artifacts
  - *From: aikitoria*

- **Problem:** LongCat sensitive to sampler
  - **Solution:** Didn't like dpm++_sde, use longcat_distill_euler instead of lcm
  - *From: Kijai*

- **Problem:** LongCat generating black frames
  - **Solution:** Specific images can cause black frame generation
  - *From: scf*

- **Problem:** Holocine crashing on ksampler
  - **Solution:** Use without compile, disable sparse attention and try without passing holocine_args first
  - *From: avataraim*

- **Problem:** Text encode node caching issues
  - **Solution:** Add a space somewhere in the prompt and try again or use the shot builder workflow
  - *From: shaggss*

- **Problem:** LongCat I2V showing first frame then turning to T2V
  - **Solution:** Update SageAttention from 1.0.6 to 2.2.0 or switch to SDPA attention
  - *From: Hashu*

- **Problem:** Black frame outputs with some images
  - **Solution:** Use bf16 instead of fp16, or switch to SPDA attention mechanism
  - *From: scf*

- **Problem:** Frame mismatch causing judder in transitions
  - **Solution:** Ensure consistent frame counts between generations (e.g., both 9 or both 13 frames)
  - *From: Kijai*

- **Problem:** Shot attention error with missing text_cut_positions
  - **Solution:** Use shot builder workflow or previous version of holocine_args node
  - *From: shaggss*

- **Problem:** Connection lost issues with modified HoloCine wrapper
  - **Solution:** Reinstall normal WanVideoWrapper node to resolve dependency conflicts
  - *From: Gill Bastar*

- **Problem:** text_cut_position becoming nonetype error
  - **Solution:** Adjusting the prompt to run the textencode solved it, also related to disk_cache usage
  - *From: Cubey*

- **Problem:** WanVideo wrapper crashes after restart
  - **Solution:** Make restart of ComfyUI to fix crashes
  - *From: avataraim*

- **Problem:** KeyError 'blocks.0.ffn.0.bias' with LongCat
  - **Solution:** Need to switch to longcat branch in WanVideoWrapper repo
  - *From: Zabo*

- **Problem:** Torch compile issues with LongCat on RTX3090
  - **Solution:** Install triton-windows or just don't use compile, it's not necessary
  - *From: Kijai*

- **Problem:** VACE 2.2 + pose controlnet produces noisy output at strength 1.0
  - **Solution:** Lower strength reduces noise but less pose following, consider using WanAnimate for pose instead
  - *From: sneako1234*

- **Problem:** Wan 2.2 LightVAE quality loss
  - **Solution:** Stick with Wan2.1 VAE as LightVAE shows considerable quality loss despite claims
  - *From: Fawks*

- **Problem:** ComfyUI-VAE-Utils installation error 'No module named comfy.ldm.wan.vae2_2'
  - **Solution:** Update ComfyUI to version that includes Wan 2.2 5B support
  - *From: spacepxl*

- **Problem:** WanFunCameraControl tensor mismatch error
  - **Solution:** Check that camera motion follows 4+1 rule on frame count
  - *From: Kijai*

- **Problem:** Shot attention error in Holocine
  - **Solution:** Only works with CFG 1.0, higher CFG values cause structured prompt errors
  - *From: NebSH*

- **Problem:** LightX2V distill lora causing overexposed lighting
  - **Solution:** Issue identified but no specific solution provided yet
  - *From: topmass*

- **Problem:** SVI-film flashing between segments
  - **Solution:** Try disabling first block (0) for SVI-Film, or it may be from HuMo itself in i2v mode
  - *From: JohnDopamine*

- **Problem:** Shot attention error: 'text_cut_positions is missing'
  - **Solution:** Issue occurs when using smooth window value of 12, problem with structured prompt metadata
  - *From: NebSH*

- **Problem:** Warning appears when increasing resolution that shot embeddings not injecting properly
  - **Solution:** This is the same problem that existed before the code fix
  - *From: shaggss*

- **Problem:** OVI has 10 second maximum limit, 15 second generations fail
  - **Solution:** Keep generations to 8 seconds or less for better results
  - *From: avataraim*

- **Problem:** Video upscaling should be in pixel space, not latent upscale
  - **Solution:** Use pixel space upscaling for proper results
  - *From: Kijai*

- **Problem:** Need to use add_noise for video extension workflows
  - **Solution:** Enable add_noise setting in the workflow
  - *From: Kijai*

- **Problem:** WanVideoImageToVideoMultiTalk node not working with looping methods
  - **Solution:** Fixed issue with timesteps assignment, now works with WanAnimate loop
  - *From: Kijai*

- **Problem:** Torch compile breaking after ComfyUI update
  - **Solution:** Mixed precision update broke compile in general
  - *From: Kijai*

- **Problem:** Mocha tensor size error with wrapper
  - **Solution:** Mocha only uses one mask for first frame, not whole video - it propagates the mask
  - *From: Kijai*

- **Problem:** Memory issues with WAN 2.2 taking 95-98% RAM on Windows
  - **Solution:** Use --cache-none flag to prevent RAM reservation, or use memory cleanup nodes
  - *From: Kijai*

- **Problem:** Port already in use error after Python terminal crash
  - **Solution:** Use netstat -ano | findstr :8188 to find PID, then taskkill /PID {ID} /F
  - *From: avataraim*

- **Problem:** use_disc_cache on text encode keeping prior prompts
  - **Solution:** Disable use_disc_cache on text encode node to use new prompts properly
  - *From: JohnDopamine*

- **Problem:** Floating menus in ComfyUI causing navigation confusion
  - **Solution:** No current solution found, users adapting to new UI
  - *From: JohnDopamine*

- **Problem:** Morph LoRA showing no effect at normal strength
  - **Solution:** Try higher strengths (3.0-4.0) or lower (0.5 as recommended)
  - *From: Kijai*

- **Problem:** longcat_distill_euler sampler not available
  - **Solution:** Remove longcat branch and download again, ensure ComfyUI restart after branch switch
  - *From: Zabo*

- **Problem:** EXR files causing pose system errors
  - **Solution:** EXR files are not compatible with pose system, use different image formats
  - *From: Guus*

- **Problem:** Torch compile causing silent crashes
  - **Solution:** Use startup args instead: --reserve-vram 2 --max-upload-size 500 --fast pinned_memory --async-offload --use-sage-attention --fast fp16_accumulation
  - *From: Gleb Tretyak*

- **Problem:** FlashVSR meta batch causing jumps/seams
  - **Solution:** Try using SeedVR2 first before FlashVSR, or use SDXL upscale refiner then downscale back to Wan resolution
  - *From: Koba*

- **Problem:** Sage-attention doesn't work with LongCat on RX 6800
  - **Solution:** Triton issue with _get_path_to_hip_runtime_dylib can't find file - model has different architecture than other Wan models
  - *From: patientx*

- **Problem:** Lightning LoRA has exposure issues
  - **Solution:** 
  - *From: Kijai*

- **Problem:** ChronoEdit doesn't work well with short prompts
  - **Solution:** Use LLM node or Qwen for prompt enhancement as suggested in official scripts
  - *From: JohnDopamine*

- **Problem:** LongCat only showing first frame then black
  - **Solution:** Doesn't work on fp16, needs bf16 base precision
  - *From: Kijai*

- **Problem:** Context windows creating artifacts and transitions
  - **Solution:** Use Magref as the low noise model - better with context windows and fine details
  - *From: blake37*

- **Problem:** ChronoEdit workflow scale_t parameter
  - **Solution:** Should be 8.0 not 7.0, but in latest version correct value is 7.0 again
  - *From: comfy*

- **Problem:** Frame number mismatch in Flash node
  - **Solution:** Frame number in Flash node needs to match the input frames
  - *From: ingi // SYSTMS*

- **Problem:** LongCat lack of reference input for face consistency
  - **Solution:** Use simple face inpaint pass with Phantom to fix face consistency issues
  - *From: Ablejones*

- **Problem:** Kijai nodes broke with new ComfyUI update
  - **Solution:** Had to bump up blocks to swap from 20 to 30 to prevent OOMs
  - *From: aipmaster*

- **Problem:** Unmerged LoRAs causing memory issues
  - **Solution:** Unmerged loras now work differently and are part of the block swap, making it obey the block swap rather than being fully swapped out
  - *From: Kijai*

- **Problem:** Color degradation into yellow during long video generation
  - **Solution:** Throwing a color match node between each segment seems to be enough to stop the slow degradation of colors
  - *From: aikitoria*

- **Problem:** Videos getting more blurry during long generation
  - **Solution:** Needs to keep exact level of softness from qwen image edit before being passed to wan to avoid vae noise grids
  - *From: aikitoria*


## Model Comparisons

- **High Noise vs Low Noise for inpainting**
  - Low Noise model performs better for large inpainting tasks, High Noise good for smaller masks
  - *From: Ablejones*

- **Kijai's scaled fp8 vs regular fp8**
  - Kijai's scaled models have better quality results in testing
  - *From: Kijai*

- **Merged vs Unmerged LoRAs**
  - Unmerged LoRAs use more VRAM but provide better quality and runtime flexibility
  - *From: Kijai*

- **Palingenesis vs normal model**
  - Palingenesis shows some improvement but original looks much better in some cases, gets CFG burn type effects
  - *From: mallardgazellegoosewildcat*

- **DYNO vs standard Wan 2.2 14b**
  - DYNO reaches 70% of standard model's dynamic performance vs 50% for original LightX2V
  - *From: slmonker(5090D 32GB)*

- **Photoshop Beta upscaler vs Wan 2.2 upscaler**
  - Photoshop takes 5s vs 10 minutes for Wan, same quality
  - *From: Drommer-Kille*

- **DC-VideoGen speed vs regular Wan**
  - DC-VideoGen: 3.67 mins/video vs regular Wan: 27.88 mins/video
  - *From: Ada*

- **WanAnimate with vs without LightX LoRA**
  - LightX LoRA preserves face likeness better, especially for non-Western subjects. Without LightX produces artifacts and poor face similarity
  - *From: Christian Sandor*

- **InfiniteTalk vs WanAnimate vs HuMo ranking**
  - Infinitetalk > WanAnimate > Humo
  - *From: slmonker(5090D 32GB)*

- **CPU vs GPU performance for mask operations**
  - GPU processing is 33x faster than CPU for DrawMaskOnImage operations (11409.67 vs 341.85 it/s)
  - *From: Kijai*

- **Context windows vs frame windowing**
  - Context windows don't have degradation issues but have worse temporal coherency between windows and are slower
  - *From: Kijai*

- **832x480 vs 1024x576 for HuMO**
  - 1024x576 has better background consistency
  - *From: mdkb*

- **USDU vs ClownShark tiling**
  - USDU faster (25 min vs 35 min) but similar quality
  - *From: FL13*

- **Sage 2 vs Sage 3**
  - Sage 3 has significant quality degradation, radial attention better quality
  - *From: Kijai*

- **MagRef vs HuMO likeness**
  - MagRef was more solid at sticking to reference image
  - *From: mdkb*

- **Wan 2.2 5B vs 14B performance**
  - 5B felt like failed experiment, can do 3 runs of 14B in time of single 5B run due to VAE overhead
  - *From: Draken*

- **OVI video quality vs Wan 5B**
  - OVI video prompt adherence looks like 5B quality, not impressive compared to larger models
  - *From: MysteryShack*

- **T2V with LoRAs vs I2V for character likeness**
  - T2V with LoRAs is often better than I2V for character consistency
  - *From: mallardgazellegoosewildcat*

- **Smooth mix vs regular Wan 2.2**
  - Better prompt adherence and more motion than previous lightx, closer to what full inference 2.2 should be
  - *From: Juampab12*

- **OVI vs standard models**
  - Takes 24GB VRAM in fp8, 5B VAE takes 4x as long to decode, seemed worse than 1.3B
  - *From: Draken*

- **Lightning LoRA T2V vs I2V performance**
  - T2V version always over-exposes results, I2V performance varies
  - *From: Kijai*

- **Dyno as LoRA vs full model**
  - Works poorly as LoRA, that's why full model was released after LoRA version
  - *From: Kijai*

- **InfiniteTalk with FantasyPortrait vs other lip-sync methods**
  - Best lip-sync tracking, especially for multi-person scenes with masking capabilities
  - *From: mdkb*

- **Wan vs Sora 2 pricing**
  - Wan is 3x cheaper - $0.05-0.15 per second vs Sora 2's higher pricing, but quality gap may make price difference irrelevant
  - *From: Juampab12*

- **OVI vs standard models**
  - OVI achieves 70% of Sora 2 quality, significantly better than standard 5B model
  - *From: slmonker(5090D 32GB)*

- **Wrapper vs Native performance**
  - Wrapper completes 121 frames in under 10min, while Native with block swap takes 29:54
  - *From: Drommer-Kille*

- **FusionX quality assessment**
  - FusionX quality is still unmatched for Wan 2.1, considered the perfect finale to Wan 2.1
  - *From: slmonker(5090D 32GB)*

- **FP16 vs FP8 quality and prompt adherence**
  - FP16 superior for quality and better for complex prompts, FP8 is faster but struggles with advanced prompts
  - *From: Dream Making*

- **BF16 vs FP16 detail rendering**
  - FP16 far better in rendering fine details
  - *From: Dream Making*

- **FP32 vs FP16 quality**
  - Quality boost barely notable between FP32 and FP16
  - *From: Dream Making*

- **Wan 2.2 high model vs 2.1**
  - Quality is better than 2.1 but motion coherence is worse, still looking for right LoRAs
  - *From: Dream Making*

- **fp8_e5m2 vs k8 gguf on RTX 3090 with Wan 2.2**
  - fp8_e5m2 = 170s gen time, k8 gguf = 360s gen time - something feels wrong with the large difference
  - *From: Mattis*

- **Different Lightning LoRA versions on low-noise**
  - Lightning LoRA 250928 + 0.25 denoise strength produces better facial expressions and details than 4-steps + auto denoise
  - *From: Lan8mark*

- **Wan 5B vs other models**
  - The wan 5b is starting to look okay to my eye on good seeds
  - *From: mallardgazellegoosewildcat*

- **AniSora vs lightx2v/lightning**
  - Better than lightx2v or lightning too for high noise
  - *From: Kijai*

- **Native vs wrapper results**
  - Not exact same results, there are some differences especially with schedulers
  - *From: Kijai*

- **Wan 2.2 vs Step Video**
  - yi claims Wan 2.2 is 2-3x better and more dynamic, mallardgazellegoosewildcat says Step still benches higher on internal benchmarks
  - *From: yi*

- **Wan 2.2 vs Step Video motion**
  - Step video fell into too much DPO and SFT trap, much less dynamic so things don't move much
  - *From: yi*

- **OVI vs Wan 2.2**
  - If you want audio use OVI, but if you don't need audio, 2.2 is still better
  - *From: Juampab12*

- **Sage 3 vs earlier versions**
  - Considerable quality drop but a bit faster, probably not worth it
  - *From: HeadOfOliver*

- **5B vs 1.3B models**
  - Best thing about 5B is that it's not 1.3B - many 1.3B works are proof of concept only and not practically useful
  - *From: Kijai*

- **OVI fp8 vs bf16**
  - fp8 is softer and has mouth problems, bf16 is better quality
  - *From: Drommer-Kille*

- **Lightx2v vs new rCM LoRA**
  - Lightx2v looks better and has more prompt adherence
  - *From: HeadOfOliver*

- **Sec vs SAM2**
  - Sec-4b looks better than SAM2 for segmentation
  - *From: slmonker*

- **SEC vs SAM2**
  - SEC is much better than SAM2 alone, uses more VRAM but worth it for quality
  - *From: Juampab12*

- **Sage attention versions**
  - Sage 1 still good, Sage 3 is fast but bad quality, SDPA best for quality, Flash deprecated
  - *From: Dream Making*

- **LightX 2.2 vs 2.1 LoRAs**
  - Most LightX 2.2 LoRAs are bad quality, 2.1 LoRAs good quality but mess up movements
  - *From: Dream Making*

- **TAE vs full 2.2 VAE**
  - TAE is preview quality only, full 2.2 VAE needed for proper outputs despite being slower
  - *From: Draken*

- **MagRef vs other consistency models**
  - MagRef outperforms other consistency models, works with both T2V and I2V
  - *From: Elvaxorn*

- **New Lightx2v 2.2 vs Lightning vs Anisora for HN cfg skimming**
  - New lightx wins with cfg, may be step distilled rather than cfg distilled
  - *From: DawnII*

- **2.1 Lightx2v vs 2.2 Lightx2v LoRA vs full model**
  - Old 2.1 lightx2v still undefeated as baseline, but new full model shows promise
  - *From: Kijai*

- **Local vs cloud GPU costs**
  - Local costs more than cloud after electricity - 540€/year for local vs cloud pricing
  - *From: Drommer-Kille*

- **Wan 2.5 vs Sora 2 vs VEO 3**
  - Wan 2.5 is most expensive and worst quality (plastic without details). VEO 3 good for talking videos but overpriced. Sora 2 better than Wan for some tasks like skateboarding
  - *From: Drommer-Kille*

- **StepVideo vs Magi Video vs Wan 2.2**
  - StepVideo and Magi Video are a lot better but depend on GPU. StepVideo gets VAE errors sometimes but does 8-10 seconds duration
  - *From: mallardgazellegoosewildcat*

- **GIMM vs RIFE vs Topaz**
  - GIMM beats Topaz easily and is probably the best interpolator out there
  - *From: HeadOfOliver*

- **New vs old LightX2V LoRA extraction**
  - New full model extracts fine at lower ranks, unlike previous dyno model which needed higher than 512 rank to match full model
  - *From: Kijai*

- **FlashVSR TCDecoder vs normal VAE**
  - FlashVSR is much faster (3 vs 20 seconds) with similar quality
  - *From: Kijai*

- **TaylorSeer vs TeaCache**
  - TaylorSeer is better and much faster, but quality degrades with high movement
  - *From: Zabo*

- **Multiple samplers vs standard 2 samplers**
  - Multiple samplers mainly useful for speed optimization with LoRAs, standard 2 samplers sufficient otherwise
  - *From: DawnII*

- **FlashVSR vs Topaz Starlight**
  - FlashVSR is much faster (150s vs 10-15min) but Topaz produces better quality with less artifacts
  - *From: Elvaxorn*

- **Wan 2.2 low-only vs using both high and low models**
  - Low noise model is basically a slightly finetuned 2.1 model, need high model for improved motion
  - *From: Kijai*

- **FlashVSR VAE vs full Wan VAE**
  - Full Wan VAE produces better quality with less artifacts but is slower
  - *From: Elvaxorn*

- **Wan2.2 4-step distill vs original**
  - Much better than Lightning distill, but 2.1 with cfg still better overall
  - *From: Kijai*

- **Kandinsky 5 2B vs Wan 14B**
  - Kandinsky has analog looking style, different motion characteristics
  - *From: yi*

- **GGUF Q6 vs fp8_scaled_v2**
  - Visual differences shown through difference blend mode comparison
  - *From: Valle*

- **2.2 Lightning vs 2.1 LightX2V LoRAs**
  - Lightning versions have annoying side effects like making everything brighter, recommend forgetting Lightning versions
  - *From: Kijai*

- **rCM vs LightX LoRAs for I2V**
  - rCM changes identity/likeness too much when used in Low noise, and creates artifacts when strength is high enough to have effect in High
  - *From: blake37*

- **FlashVSR vs other upscalers for motion blur**
  - FlashVSR doesn't try to resolve motion blur like most upscalers that incorrectly interpret blurry things as sharp items
  - *From: Mads Hagbarth Damsbo*

- **rCM vs LightX2V**
  - rCM wins for prompt adherence, LightX2V can turn things halloween themed unexpectedly
  - *From: Kijai*

- **FP8 vs FP/BF16 models**
  - FP/BF16 dramatically better for video extension quality, especially noticeable at longer durations
  - *From: Zabo*

- **Wan 2.2 5B vs other variants**
  - Only 5B model is true 24fps, other variants have frame rate limitations
  - *From: garbus*

- **rCM scheduler vs dpm++_sde**
  - No compute difference, dpm++_sde probably better but rCM gives different results
  - *From: Kijai*

- **DGX Spark vs RTX 6000 Pro Blackwell for Wan 2.2**
  - DGX Spark is about 1/5 the speed of RTX 6000 Pro
  - *From: tarn59*

- **2.2 Lightning vs 2.1 Lightx2v for I2V**
  - Lightning preferred for I2V generally, but 2.1 lightx2v still undefeated for low noise due to better lighting
  - *From: FL13*

- **Native vs Wrapper workflows**
  - 3 sampler native gives nice results and is faster than wrapper
  - *From: FL13*

- **Ditto full module vs LoRA**
  - Full module has less artifacting, ghosting and is more reliable
  - *From: Hashu*

- **Using cfg vs speed LoRAs**
  - cfg on first step works fine, variations work well for getting motion
  - *From: Kijai*

- **torch.compile + sdpa vs sage-attention**
  - torch.compile + sdpa faster than sage-attention, but sage has lowest memory usage
  - *From: patientx*

- **WanAnimate + first frame vs other approaches**
  - Better than basic pose control, though pose still has limitations
  - *From: Juampab12*

- **MoCha vs Wan-animate and Kling**
  - MoCha demonstrates superior performance and doesn't need pose like Wan animate
  - *From: Juampab12*

- **Left Fast+Krea vs without fast lora on high sampler**
  - Visual comparison shown but no specific verdict given
  - *From: Drommer-Kille*

- **Krea vs other distillation LoRAs**
  - Quality is disappointing even if it's 14B, similar to causvid issues
  - *From: Kijai*

- **MoCha vs other reference models**
  - MoCha looks like CG, sometimes bad CG, fine for non-realistic but inconsistent quality
  - *From: Screeb*

- **Krea LoRA vs LightX LoRAs**
  - No need for lightX loras with Krea, works better for realistic results
  - *From: Drommer-Kille*

- **RCM vs Krea LoRA**
  - Both are alternatives to lightX, but Krea is causal like CausVid
  - *From: Juampab12*

- **Rolling Forcing vs other models**
  - Goes longer than other models before degrading, shows better temporal consistency
  - *From: Draken*

- **Fun vs Wanimate for character replacement**
  - Fun is much better - Wanimate has sharper characters but doesn't fit the scene well
  - *From: Drommer-Kille*

- **New 1022 LightX2V LoRA vs old versions**
  - New version is the best LightX2V LoRA so far, works better on problematic prompts
  - *From: Ada*

- **MoCha similarity quality**
  - Similarity is pretty bad, inputs real person but gets CGI output
  - *From: berserk4501*

- **Q5_K_S vs Q8 GGUF quality**
  - Never use anything below Q8 unless absolutely necessary, especially not with RTX 5090
  - *From: Kijai*

- **New lightx2v LoRA vs old MoE version**
  - New 1022 version performs much better, closest to 2.1 quality for 2D animation of any 2.2 distill so far
  - *From: Kijai*

- **Mocha vs WanAnimate**
  - Mocha is clearly inferior to WanAnimate and doesn't keep character likeness as well
  - *From: A.I.Warper*

- **2.1 vs 2.2 quality**
  - 2.2 has higher quality and better prompt adherence than 2.1, but 2.1 still performs better for certain specific prompts
  - *From: Juan Gea*

- **Mocha vs other character models**
  - Superior fidelity for body/facial movements but struggles with two-character scenarios and context windows
  - *From: Visionmaster2*

- **SVI vs VACE extensions**
  - SVI for I2V continuations, VACE for T2V extensions with more control/flexibility
  - *From: 42hub*

- **Wan 2.2 vs 2.1 movement quality**
  - Much better movement in 2.2 than 2.1
  - *From: Zabo*

- **Light VAE vs standard VAE**
  - Big drop in details but really fast, uses less memory, unsure if better than tiny VAE
  - *From: Kijai*

- **Ditto vs Runway Gen3**
  - Ditto quality degrades at longer durations, Runway maintains consistency better
  - *From: Drommer-Kille*

- **WSL vs native Linux vs native Windows**
  - Native Linux fastest at loading, native Windows and Linux similar inference speed when everything works. WSL adds complexity for memory management
  - *From: Kijai*

- **SVI-film vs SVI-shot reference frame handling**
  - SVI-shot works well with reference frame repetition for scene continuity, SVI-film fails completely with this technique
  - *From: Ablejones*

- **22.04 Ubuntu vs newer versions**
  - 22.04 more stable, used by Runpod and vast.ai. Newer versions may have compatibility issues
  - *From: Colin*

- **HoloCine vs SVI for extension**
  - HoloCine examples look much better without the washed out bright issues that SVI has when videos get too long
  - *From: Owlie*

- **Wan 2.2 vs 2.1 movement quality**
  - After using 2.2, 2.1 looks slow and strange in comparison - SVI suffers from old 2.1 movements
  - *From: Zabo*

- **HoloCine vs base Wan 2.2 scene switching**
  - Base 2.2 does harder cuts while HoloCine provides smoother transitions between scenes
  - *From: VK (5080 128gb)*

- **Context windows vs normal extension methods**
  - Context windows always go back to I2V input for identity but are much slower and prone to artifacts
  - *From: blake37*

- **InfiniteTalk vs other extension methods**
  - InfiniteTalk is still the king in terms of consistency with hardly any degradation/colorshift
  - *From: seitanism*

- **Film vs Shot LoRA methods**
  - Film continues motion using 5 frames from last video but can degrade. Shot doesn't continue motion but stabilizes long generations by keeping original reference
  - *From: Kijai*

- **First-Frame-Last-Frame vs simple extension**
  - FLF can work better because you never have to give a decoded frame, you have all keyframes. Simple extension degrades on second extension
  - *From: Draken*

- **5 vs 16 frames for motion continuation**
  - 16 frames better for motion continuation, 5 frames better for reducing degradation
  - *From: DawnII*

- **svi-film vs svi-shot**
  - Film uses multiple frames (5) and degrades over time but works for longer videos. Shot uses single frame with reference image capability and can theoretically do infinite length
  - *From: Kijai*

- **merged vs unmerged LoRA**
  - Merged seems to work better, unmerged can sometimes break loras completely or make them work better
  - *From: Kijai*

- **film vs film-opt lora**
  - film-opt is a newer version of the film lora
  - *From: Ablejones*

- **infinitetalk vs humo for portrait**
  - infinitetalk best for long portrait animation, humo good for short portrait animation
  - *From: DawnII*

- **HoloCine vs normal 2.2**
  - HoloCine prevents corrupt first frame that occurs with normal weights
  - *From: Kijai*

- **Film vs Shot LoRA functionality**
  - Film takes 5 input images and continues motion; Shot takes 1 input + reference for infinite generation without degradation but doesn't continue motion
  - *From: Kijai*

- **3 high 3 low with lightx vs 6 high no lora + 3 low with lightx**
  - 3+3 with both lightx gives better results
  - *From: seitanism*

- **LongCat vs WAN 2.2**
  - LongCat has worse T2V scores than WAN 2.2 but half the size, unified model approach, and better long generation stability
  - *From: Kijai*

- **FusionX LoRA on WAN 2.1 vs WAN 2.2 with LightX2V**
  - FusionX on WAN 2.1 produces better results
  - *From: Govind Singh*

- **LongCat distill vs original**
  - 16 step distill version is pretty bad compared to 50 step original
  - *From: aikitoria*

- **Holocine quality vs WAN 2.2**
  - Slightly lower quality than normal WAN 2.2
  - *From: seitanism*

- **Wan 2.2 vs 2.1 motion understanding**
  - Wan 2.2 not as smooth motion-wise and doesn't have same level of understanding for things like driving
  - *From: Ada*

- **HoloCine vs base Wan quality**
  - HoloCine has worse prompt adherence than base but much less degradation
  - *From: DawnII*

- **SVI-Film vs VACE degradation**
  - SVI-Film degradation much better than VACE when used as designed (Wan 2.1 I2V without distill LoRAs)
  - *From: Ablejones*

- **LongCat 30 steps cfg 4.0 vs 15 steps cfg 1.0 with distill LoRA**
  - Distill LoRA allows faster generation with similar quality
  - *From: Kijai*

- **LongCat I2V vs Pusa**
  - Looking at I2V now, seems similar/same to Pusa. LongCat cares about init image even less than Pusa
  - *From: Kijai*

- **LongCat model size vs others**
  - 14B is 5120, 5B is 3072, and LongCat is 4096 - 8 more blocks but slightly smaller dim
  - *From: Kijai*

- **Holocine vs manual prompting**
  - Shot builder workflow vs normal text encode - shot builder missed fewer shots
  - *From: shaggss*

- **LongCat vs Wan 2.2**
  - LongCat is on same level as Wan 2.2, essentially an improved Wan 2.2 5B version but trained from scratch
  - *From: Lodis*

- **LongCat vs Wan speed**
  - Almost identical speed to Wan despite different architecture
  - *From: Kijai*

- **MoCha vs Wan Animate**
  - Sometimes much better, other times worse. Only does replacement and worse at long gens without innate long generation ability
  - *From: Kijai*

- **Euler vs UniPC vs DPM++ samplers for WanAnimate**
  - Euler turned out much better than LCM, UniPC seems slightly sharper in eyes, minimal difference overall
  - *From: A.I.Warper*

- **Distilled vs non-distilled lora for ID preservation**
  - ID feels better with no lora, non-distilled doesn't exhibit eye makeup artifacts as much
  - *From: A.I.Warper*

- **LongCat vs other video models**
  - LongCat is very promising, everything else was a bit 'meh' in tests
  - *From: Gill Bastar*

- **Wan2.2 LightVAE vs Wan2.1 VAE**
  - Wan2.1 VAE is better, LightVAE shows considerable quality loss
  - *From: Fawks*

- **Wan VAE vs video codecs**
  - Wan VAE has compression artifacts like choosing different jpg blocks each frame instead of using motion vectors like real video codecs
  - *From: aikitoria*

- **16x vs 32x VAE compression**
  - Should use 16x spatial compression in VAE with no patchify on transformer for best quality, but nobody does this
  - *From: spacepxl*

- **LongCat vs Wan quality and length**
  - LongCat feels like mix between Wan 2.1 and 2.2 quality, extension only way to get longer than 6 seconds
  - *From: Zabo*

- **WAN 2x VAE vs original VAE**
  - 2x VAE provides significantly better detail and sharpness, comparable to what SDXL refiner wished it could have been
  - *From: spacepxl*

- **GGUF vs FP8 scaled for models**
  - Q8 vs FP8 scaled is a tossup, technically Q8 might be slightly better but FP8 scaled generally used
  - *From: spacepxl*

- **Original LTX vs other models**
  - Original LTX generates uncontrollable garbage, terrible at anything not movie scenes/realism
  - *From: aikitoria*

- **WAN 2.5 vs LTX-2 via API**
  - WAN 2.5 has potential and is a step up from 2.2, LTX-2 seems mediocre at best
  - *From: blake37*

- **FlashVSR vs WAN 2.5**
  - FlashVSR results are better than WAN 2.5 but below Veo/Sora
  - *From: Draken*

- **HoloCine vs WAN 2.5**
  - HoloCine is already better than WAN 2.5 preview minus the sound aspect
  - *From: ZeusZeus (RTX 4090)*

- **LongCat vs Wan models**
  - Better Wan 2.1 with native video continuation training, prevents color drift and quality degradation
  - *From: JohnDopamine*

- **10 steps vs 16 steps on LongCat**
  - Less steps burns less but more mistakes in motion
  - *From: Kijai*

- **dpm++_sde vs other samplers**
  - dmp++_sde with 10 steps ruins generation, not recommended
  - *From: Kijai*

- **Morph LoRA vs base Wan 2.2 I2V**
  - Wan 2.2 I2V transitions seemed better in testing examples
  - *From: shaggss*

- **LightX2V 1030 vs 1022**
  - 1030 is 'a looooot better' according to early testing
  - *From: Zabo*

- **LTX 2 vs Wan quality**
  - Wan has better video quality and coherence than LTX 2, despite LTX 2's technical specs
  - *From: Kijai*

- **LongCat vs Wan foundation**
  - LongCat is clearly an improvement over Wan but may not be enough for people to start training ecosystems on it
  - *From: Kijai*

- **Lightning vs LightX2V LoRAs**
  - LightX2V better - Lightning has exposure issues and not best motion, LightX2V has better prompt adherence
  - *From: Kijai*

- **New 1030 vs previous LightX2V**
  - 1030 has better prompt adherence and camera control
  - *From: Aaron_PhD*

- **Qwen Image Edit vs ChronoEdit**
  - Qwen image edit still wins overall
  - *From: Kiwv*

- **Wan 2.1 vs 2.2 for low noise**
  - 2.1 LightX2V LoRA works fine with 2.2 low noise, no need for new 2.2 low noise LoRA
  - *From: Kijai*

- **ChronoEdit vs Qwen Image 2509**
  - Qwen is definitely better, ChronoEdit fails on same prompts where Qwen fails
  - *From: aikitoria*

- **LongCat vs Wan for T2V**
  - LongCat base model seems to understand concepts better and you don't need 57 models for similar quality as WAN 2.2
  - *From: Pandaabear*

- **LongCat vs Wan memory usage**
  - WAN brings close to OOM often, LongCat barely uses 60% with higher resolution and more frames
  - *From: Pandaabear*

- **MOE vs standard models**
  - MOE model gives better motion without having to increase strength above 1.0 or 1.2
  - *From: blake37*

- **VACE vs LongCat frame extension**
  - VACE gets autoregressive burn in rather quickly and has color drift issues, while LongCat is really good for video extension
  - *From: Benjaminimal*

- **LongCat 2D animation vs LTX 2**
  - LongCat has far better 2D animation quality than LTX 2 which does terrible there
  - *From: Ada*

- **Grok video model vs Wan**
  - Grok looks like Wan trained on porn and audio doesn't line up properly, sounds like mmaudio
  - *From: Kiwv*

- **ChronoEdit vs Qwen**
  - Can't do anything qwen can't so kinda useless, prompts that qwen fails at this also fails at
  - *From: aikitoria*

- **ChronoEdit vs Qwen quality**
  - Quality of qwen edit 2509 at 1664x928 40 steps is vastly better than what ChronoEdit can do before it breaks down
  - *From: aikitoria*

- **Sora vs Veo quality**
  - Sora blows veo out of the water on almost every shot generated, though veo 3.1 is sharper
  - *From: Ruairi Robinson*

- **LTX2 vs Wan potential**
  - If LTX2 is slightly worse quality but cheaper and faster, would still make loras for LTX because of cost/speed advantages
  - *From: Kiwv*


## Tips & Best Practices

- **Stick with Low Noise model for inpainting, try High Noise for smaller tasks**
  - Context: When using VACE inpainting with Wan 2.2
  - *From: Ablejones*

- **Use white masks instead of gray for better results**
  - Context: When working with VACE
  - *From: scf*

- **Turn on face detection settings for better lip sync results**
  - Context: Using Wan Animate for facial animation
  - *From: U̷r̷a̷b̷e̷w̷e̷*

- **Try stronger pose settings like 1.3 for lip sync delay issues**
  - Context: When experiencing timing issues in facial animation
  - *From: Charlie*

- **Check riflex_freq_index setting in sampler - should be zero**
  - Context: Using VACE, non-zero values add strange effects
  - *From: scf*

- **Increase LoRA strength when using fp8 models**
  - Context: Motion LoRAs may need higher strength values with fp8 compared to GGUF
  - *From: Kijai*

- **Use .torchscript bbox detector for faster pose detection**
  - Context: DWPose processing optimization
  - *From: xiver2114*

- **Use reference image with character in same pose and position as first frame of guiding video**
  - Context: For better character consistency in WanAnimate
  - *From: seitanism*

- **Use torch compile to speed up generation**
  - Context: For faster inference when doing I2V with multiple LoRAs
  - *From: seitanism*

- **Use Photoshop Beta for free upscaling during beta period**
  - Context: Has built-in Nano Banana and FLUX Kontext, much faster than Wan upscaling
  - *From: Drommer-Kille*

- **Avoid suspicious code with encrypted/binary files**
  - Context: Red flag when code is shared as .pyd files without source
  - *From: Kijai*

- **Better sampling and more steps reduce noise artifacts**
  - Context: When using LightX 4-step models
  - *From: Ablejones*

- **Try 6 steps first when troubleshooting noise**
  - Context: Instead of sticking to 4 steps with LightX models
  - *From: Ablejones*

- **Good sampler can't fix a bad prompt**
  - Context: The sampler needs to be given something to find, prompt sets up the distribution
  - *From: mallardgazellegoosewildcat*

- **Start with plain and simple characters**
  - Context: When having trouble getting good results, avoid difficult characters initially
  - *From: Tony(5090)*

- **WanAnimate relight LoRA is hit or miss**
  - Context: Leave it in and turn to 0 or 1 depending on need, works better when sources have similar brightness
  - *From: U̷r̷a̷b̷e̷w̷e̷*

- **Use 3 samplers with Lightning LoRA**
  - Context: 0-25-0.5 HN LoRA on first, 1.0 on HN on second, 1.0 LN on third
  - *From: pom*

- **Audio scale settings for lipsync**
  - Context: Audio scale at 1.4, audio cfg at 1 for InfiniteTalk
  - *From: Charlie*

- **Don't use fp8 if avoidable**
  - Context: For best results with model extraction
  - *From: Kijai*

- **Use svd_lowrank algorithm for speed**
  - Context: When extracting model differences
  - *From: Kijai*

- **Use higher resolution reference images for better face results**
  - Context: When using Wan Animate for character likeness, more pixels dedicated to face = higher quality face texture
  - *From: oskarkeo*

- **Match reference frame to video control for better results**
  - Context: Use control net to generate ref image at similar pose to video control
  - *From: hudson223*

- **Use clownshark samplers with res_5s for fewer steps**
  - Context: They solve the model more accurately allowing less steps and have different SDE math adding more noise
  - *From: mallardgazellegoosewildcat*

- **Don't do sample images during LoRA training to save time**
  - Context: GPU to CPU switching for sample generation is costly during training
  - *From: Kytra*

- **Use detailed text prompt on high noise, then low noise does remaining 20%**
  - Context: For character generation with 2.2
  - *From: Juampab12*

- **Clear ComfyUI cache manually from temp folder**
  - Context: ComfyUI doesn't always clear cache on restart, leaves images/videos in temp folder
  - *From: JohnDopamine*

- **Disconnect face_images noodle if you don't want face performance transfer**
  - Context: In Wan Animate, works fine without blocky black mask
  - *From: CaptHook*

- **Iterate prompts multiple times for complex motions**
  - Context: Models may seem incapable but careful prompt engineering can achieve desired results
  - *From: Ablejones*

- **Use CPU fallback for ONNX preprocessing when GPU fails**
  - Context: Still fast on good CPU due to tiny internal resolution
  - *From: D-EFFECTS*

- **Run low-settings generations first, then increase quality**
  - Context: Save time by testing at lower resolution/steps before full quality generation
  - *From: Rainsmellsnice*

- **Trees are problematic in FFLF with camera moves**
  - Context: Always one tree wanders through shot, difficult to fix in post
  - *From: mdkb*

- **Use math nodes for automatic resizing to valid resolutions**
  - Context: Set to multiples of 64 or 128 to avoid black outputs
  - *From: GalaxyTimeMachine (RTX4090)*

- **For character animation, disconnect bg_images and mask**
  - Context: When using WanAnimate for character animation vs character replacement
  - *From: Kijai*

- **Compose character into desired background first**
  - Context: When wanting to generate background from another reference image
  - *From: 42hub*

- **Use speed LoRAs with reduced steps**
  - Context: With LoRAs can keep steps at 4-8 instead of 20 for faster generation
  - *From: Dream Making*

- **Better I2V without LoRAs for base model**
  - Context: Base model should not be blurry for I2V without additional LoRAs
  - *From: Charlie*

- **Use 2 RAM sticks instead of 4 for Intel 13th/14th gen**
  - Context: 4 sticks strain the memory controller and prevent XMP from working properly
  - *From: Ryzen*

- **Use wide-tooth comb for curly hair training data**
  - Context: When training LoRAs for realistic hair combing videos
  - *From: phazei*

- **Close and restart ComfyUI if models get corrupted**
  - Context: When experiencing issues after ComfyUI has been open too long, reselect models after restart
  - *From: Thom293*

- **FP8 is mandatory in user's experience**
  - Context: For practical usage despite quality differences
  - *From: Dream Making*

- **For distill LoRAs, sampler choice matters less - stick with simple ones**
  - Context: When doing low steps with distill loras, use dpm++ sde or lcm, or even just euler
  - *From: Kijai*

- **Use full distill model instead of LoRAs to prevent 'falling off'**
  - Context: Save model + lora combination as some software can have loras fall off
  - *From: hicho*

- **Search through high number of combinations when training LoRAs**
  - Context: Biggest cause of poor LoRA results is not fully exploring settings combinations - can be automated with scripts
  - *From: mallardgazellegoosewildcat*

- **Don't apply sage3 to first and last steps**
  - Context: When using distill lora with 4 steps, sage3 would only apply to 2 steps and still lose quality while gaining almost nothing
  - *From: Kijai*

- **Don't use Lightning LoRA on high-noise model for WAN**
  - Context: I actually haven't thought about not using lightning loras for high. That's actually a pretty good idea! Works wonders too!
  - *From: Zabo*

- **Use different negative prompts for video and audio in OVI**
  - Context: Video and audio uses same positive, but they can use different negative...at least original code does it like that
  - *From: Kijai*

- **Parameter optimization needs to be minimised**
  - Context: Parameter combinations go to infinity
  - *From: mallardgazellegoosewildcat*

- **Save really good seeds for months of reuse**
  - Context: You can save really good seeds and use them for months
  - *From: mallardgazellegoosewildcat*

- **Don't jump models constantly**
  - Context: Better to focus on one model and master it
  - *From: mallardgazellegoosewildcat*

- **Always merge at highest precision then quantize**
  - Context: When working with LoRAs and model merging
  - *From: Kijai*

- **SDE samplers need at least 60 steps and no distil loras**
  - Context: When using SDE sampling methods
  - *From: mallardgazellegoosewildcat*

- **UniPC is a good safe general sampler**
  - Context: When unsure about sampler compatibility
  - *From: mallardgazellegoosewildcat*

- **Be careful with SDE samplers at low steps**
  - Context: SDE samplers add noise and can do harm at low step counts
  - *From: mallardgazellegoosewildcat*

- **Use dialogue tags for OVI audio generation**
  - Context: Format: 'The man says: <S>Hello, how do you do?<E>'
  - *From: ZeusZeus (RTX 4090)*

- **Install Triton on Windows directly**
  - Context: For speed improvements
  - *From: Shadows*

- **Don't use fp8 quantization for WAN**
  - Context: fp8 makes everything blurry and motion is far worse, use Q8 GGUF if you need quantization
  - *From: Ada*

- **Use Kijai's LoRA instead of PT files**
  - Context: For better compatibility and performance
  - *From: Zabo*

- **Install nightly version of nodes for latest updates**
  - Context: To get the absolute latest version and avoid compatibility issues
  - *From: Kijai*

- **Never clone HF repos, use HF CLI instead**
  - Context: Cloning can download outdated model files and create cache issues
  - *From: aikitoria*

- **Prompt length affects quality**
  - Context: Too short and prompt tends to bleed in, too long and it tends to short circuit
  - *From: TK_999*

- **50 steps and higher resolution improve OVI quality**
  - Context: Better than 20 steps at lower resolution for final quality
  - *From: Drommer-Kille*

- **Use manual HF downloads instead of auto-download**
  - Context: Auto-download can pull unnecessary files and uses single stream
  - *From: mdkb*

- **Use LayerForge node with Matting button for character replacement**
  - Context: For character consistency workflows with MagRef
  - *From: Elvaxorn*

- **Avoid going fully cold with serverless deployments**
  - Context: Keep different levels of warm starts for better performance
  - *From: mallardgazellegoosewildcat*

- **Lower CFG for faces to get softer results**
  - Context: Face generation in Wan models
  - *From: mallardgazellegoosewildcat*

- **Use 2.5 CFG on low noise instead of 3.5 for better faces**
  - Context: CFG degrades faces on low noise model
  - *From: Lumifel*

- **Remove all other distill LoRAs when using speed LoRAs unless strength is low**
  - Context: They don't play well together
  - *From: Elvaxorn*

- **Use 3.0 strength for high noise and 1.0 for low noise with 2.1 Lightx2v**
  - Context: Kijai's recommended settings
  - *From: Kijai*

- **Use cfg skimming with higher CFG values to prevent burn while maintaining prompt adherence**
  - Context: For better prompt following with distilled models
  - *From: GalaxyTimeMachine*

- **Use longer prompts for better motion**
  - Context: For Wan 2.2 to get more realistic movement and emotions, especially for T2V rather than I2V
  - *From: Drommer-Kille*

- **Use precise schedules for low step distillation**
  - Context: At low steps you really need the schedule to be precise, at high steps it doesn't matter as much
  - *From: mallardgazellegoosewildcat*

- **Disable torch compile when using dynamic CFG**
  - Context: When CFG changes each step, torch compile will recompile and slow things down
  - *From: GalaxyTimeMachine (RTX4090)*

- **Use 3 sampler workflow for better results**
  - Context: Still worth using 3 sampler setup: 1 step HN no lora cfg 3.5 + 2 step HN with new lightx2v lora + 3 step LN with old 2.1 lightx2v lora
  - *From: FL13*

- **For pose detection issues with distant characters, crop in on person, upscale to at least 480p, generate, then outpaint with VACE**
  - Context: When character is far away from viewer
  - *From: ArtOfficial*

- **Use LoRAs to add movement to T2V when LightX LoRA would be slow motion**
  - Context: Training custom LoRAs for movement
  - *From: Drommer-Kille*

- **For CFG scheduling without lighting LoRAs, use 20 steps (2x10), CFG 3.5 on high and 2.5 on low**
  - Context: Standard CFG settings for quality
  - *From: Lumifel*

- **Clear triton caches when updating torch and using torch compile**
  - Context: After torch updates
  - *From: Kijai*

- **Don't use speed optimization techniques like teacache with only 4 steps**
  - Context: Speed optimizations are useless when running minimal steps
  - *From: Kijai*

- **Use hybrid approaches with CFG for first step as best compromise for Wan 2.2**
  - Context: When distillation LoRAs fail to produce dynamic motion like CFG does
  - *From: Kijai*

- **Use Kijai's color match node over other versions**
  - Context: For video extension workflows, provides better accuracy
  - *From: Tachyon*

- **Use difference blend mode to compare model outputs**
  - Context: When testing different model versions to spot subtle differences
  - *From: Valle*

- **Generate image first then do I2V instead of T2V**
  - Context: More control over final output
  - *From: aikitoria*

- **Use overlaps when stitching video segments**
  - Context: 10-20% frame overlap maintains consistency
  - *From: Dever*

- **For LoRA extractions, get the ones Kijai did on his HF as they have all non-block changes**
  - Context: Some official Lightx2v LoRAs didn't have all changes so performed oddly
  - *From: JohnDopamine*

- **Use VACE with no image input and character loras for face swaps**
  - Context: Works really well, or use with loras to stabilize likeness in addition to ref image
  - *From: Ruairi Robinson*

- **For long video upscaling, split to latent files and process in sections**
  - Context: Upscale in 120 frame sections with 100 frame steps, leaves 17 frames overlap, then use USDU node at low denoise 0.1-0.3
  - *From: mdkb*

- **Include color information in captions when training LoRAs**
  - Context: When training object LoRAs, mentioning specific colors helps with proper generation
  - *From: Dever*

- **Run longer generation and trim if getting pause at start**
  - Context: When dealing with first frame issues, sometimes better to generate extra and chop off frames using Video Helper Suite
  - *From: garbus*

- **Use 2.2 high with 2.1 low for best results**
  - Context: Recommended combination for high/low noise expert models
  - *From: Tachyon*

- **Lower LoRA strengths and use block editing for mixing LoRAs**
  - Context: Helps avoid grainy results when mixing multiple LoRAs
  - *From: flo1331*

- **Use scaled models over fp8 for better quality**
  - Context: General recommendation for maintaining model quality
  - *From: JohnDopamine*

- **Restart ComfyUI after every run to avoid GPU overload**
  - Context: Workaround for current VRAM issues after updates
  - *From: mdkb*

- **Use highest resolution possible for I2V to maintain character likeness**
  - Context: Bigger input provides better reference for models to keep character consistency
  - *From: blake37*

- **Be careful with multiple LoRAs overwhelming character identity**
  - Context: Too many strong LoRAs can override character training data
  - *From: blake37*

- **Use CFG 2 or higher for better style transfer results**
  - Context: CFG 1 may not achieve desired stylization effect
  - *From: Draken*

- **Use cfg only on step 1 for good results with minimal complexity**
  - Context: Works well with or without LoRA, easier than complex multi-step configurations
  - *From: Kijai*

- **Split high/low steps at right point when using speed LoRAs**
  - Context: If you increase high steps without increasing low steps it gets unbalanced
  - *From: Kijai*

- **Use reduced VACE strength with cfg**
  - Context: Examples show using cfg 2.0 on first step with reduced VACE strength
  - *From: Kijai*

- **Match dtypes when extracting LoRAs**
  - Context: Try to always match the dtypes, use model loaders to force bf16 to avoid mismatches
  - *From: Kijai*

- **Lock critical dependencies to prevent environment breakage**
  - Context: Lock numpy and other critical packages so they don't auto-update and break ComfyUI
  - *From: Léon*

- **Muted colors are a GOOD thing - it's always better to have a flat image because it's easier to grade**
  - Context: Contrast is the enemy, oversaturated overcontrasted look baked in AI models can't be undone in post
  - *From: Quality_Control*

- **Use total pixel resize setting**
  - Context: When working with Mocha - change crop to total pixel then h and w as 640 640
  - *From: hicho*

- **Disable wan preset in VHS video loader**
  - Context: When using Mocha - if you refresh, VHS changes the resolution
  - *From: hicho*

- **Use denoised output for high sampler preview**
  - Context: End of high sampler supposed to have leftover noise before passing to low noise - that's how MoE arch works
  - *From: DawnII*

- **Always use prompts with MoCha for best results**
  - Context: Without prompts, model can produce body horror or weird artifacts
  - *From: Kijai*

- **Use upper body shots as reference for better results**
  - Context: When doing character replacement with MoCha
  - *From: Kijai*

- **For NAG prompts, use simple negatives only**
  - Context: NAG negative should only contain unwanted elements, not generic negative prompt word salad
  - *From: Kijai*

- **Use manual masking for better control**
  - Context: Better than auto-masking, only need to do first frame
  - *From: Draken*

- **Try using two references (face + body) for full character transfer**
  - Context: May help avoid face detection issues in body areas
  - *From: Draken*

- **Slow down control video if camera movement is too fast**
  - Context: For Uni3C camera control, misinterpretation of scale causes speed issues
  - *From: Juampab12*

- **You can use Qwen VAE for Wan single image generations**
  - Context: Just not for video generation
  - *From: Kijai*

- **Use fp8_fast mode for ~30% speed improvement**
  - Context: When using fp8 model on RTX 5090
  - *From: Kijai*

- **Avoid normal fp8 (non-scaled) and GGUF below Q8**
  - Context: For optimal quality
  - *From: Kijai*

- **Don't run ComfyUI with --high-vram**
  - Context: Should use automatic model offloading instead
  - *From: Kijai*

- **Use nvtop to monitor VRAM**
  - Context: Best tool for VRAM monitoring on Linux
  - *From: Kijai*

- **Use 2+2 step split for new light LoRA**
  - Context: Most reasonable split for 4 total steps, can use 3+3 for better image quality
  - *From: Ablejones*

- **Avoid 3+1 step configuration**
  - Context: When splitting steps between samplers for distill LoRAs
  - *From: Ablejones*

- **Test without distill LoRAs for accurate comparisons**
  - Context: Distill LoRAs can contaminate tests of new techniques and tools
  - *From: Ablejones*

- **Use CFG settings appropriately**
  - Context: CFG is important for ID consistency, higher CFG with distill LoRAs can overcook results
  - *From: DawnII*

- **Use strength 3 on high and 1 on low for SVI with Wan 2.2**
  - Context: Initial testing parameters for SVI compatibility
  - *From: Zabo*

- **closeups work much better than wide shots**
  - Context: For character consistency in video generation
  - *From: Drommer-Kille*

- **Use fixed seed and same prompt node plus color match**
  - Context: To reduce color shift between generations in multi-batch workflows
  - *From: hicho*

- **Set WSL config with nonblocking and 1 prefetch blocks**
  - Context: For optimal WSL performance with video generation
  - *From: seitanism*

- **Don't use block swap if you don't have VRAM issues**
  - Context: Block swapping can use additional RAM and may cause OOM issues
  - *From: seitanism*

- **Use grey pixels (0.5) for best video extension padding**
  - Context: When manually setting padding frame pixel values for video extensions
  - *From: Ablejones*

- **Close background apps and restart browser for better performance**
  - Context: When experiencing memory issues during generation
  - *From: seitanism*

- **Use LLMs for Linux configuration but not video AI techniques**
  - Context: LLMs good for basic Linux setup but unreliable for video model specifics
  - *From: 42hub*

- **Use LightX2V LoRA with 4 steps and CFG 1 for InfiniteTalk to avoid extremely long generation times**
  - Context: When doing long audio-driven video generation
  - *From: seitanism*

- **Don't always use init image as first frame - can use random frame from earlier video for consistency**
  - Context: When extending videos beyond 2-3 segments
  - *From: VK (5080 128gb)*

- **Increase RAM capacity and use fp8 quantized models to speed up loading**
  - Context: When models fit in RAM, loading is very fast after first load
  - *From: seitanism*

- **Store models within WSL file system rather than accessing from outside**
  - Context: When using WSL on Windows for better performance
  - *From: seitanism*

- **Use less random samplers for better SVI results**
  - Context: No _sde or lcm samplers work better for SVI
  - *From: Kijai*

- **Use different seeds for each SVI generation**
  - Context: Same seed makes burning/flash artifacts worse in continuations
  - *From: Kijai*

- **Manually set mask for only first frame in shot method**
  - Context: Important for shot LoRA to work properly, default masks all images
  - *From: Kijai*

- **Consider content type for flash visibility**
  - Context: Flash artifacts most noticeable in dark scenes, barely visible in bright areas like sky
  - *From: Draken*

- **For 2.2, increase LoRA strength for high noise when using 2.1 LoRAs**
  - Context: 2.1 LoRAs don't work properly on 2.2 high noise due to differences
  - *From: Kijai*

- **Use merged fp16 lora instead of unmerged**
  - Context: When using special loras like shot, sometimes unmerged applying can affect negatively
  - *From: Kijai*

- **Leave off padding frames with film lora**
  - Context: Film lora can't handle padded reference frames
  - *From: Ablejones*

- **For svi-film just send 5 overlap frames as start image**
  - Context: No need to worry about masks when using svi-film, just send the 5 overlap frames
  - *From: Ablejones*

- **Can adjust audio scaling or lock pose with unianimate**
  - Context: To reduce hand movement in portrait animations
  - *From: DawnII*

- **Reference padding only works with shot, talk and dance loras**
  - Context: Film lora will freeze if you try to use reference padding
  - *From: Kijai*

- **Use middle grey (127) not black for padded frames in SVI workflows**
  - Context: When replicating SVI workflows manually outside wrapper, because diffusers converts 0 to middle grey
  - *From: 42hub*

- **Lower lightx2v lora strength works better: 1.5 strength on high noise, 1.0 on low noise**
  - Context: When using HoloCine with lightx2v lora
  - *From: VK (5080 128gb)*

- **Use structured prompts: general description + specific scene prompts separated by |**
  - Context: For HoloCine multi-shot generation - general prompt describes overall setting, specific prompts describe camera motion/cuts for each scene
  - *From: seitanism*

- **Try no SVI LoRA for first sampler to help with motion in first 5 seconds**
  - Context: When first part of video appears too static
  - *From: garbus*

- **Use LightX quantile 0.15 LoRA with high 3.0, low 1.0 strength**
  - Context: For T2V generation
  - *From: Gill Bastar*

- **Generate at lower resolution with max frames, then upscale using context options**
  - Context: For better consistency with long generations
  - *From: mamad8*

- **Keep exact aspect ratio when generating at low resolution**
  - Context: To ensure proper scene switching
  - *From: VK*

- **Feed video with pure background colors that change at each shot end with denoise 0.9-0.95**
  - Context: To force high noise model to differentiate scenes
  - *From: mamad8*

- **Use a 2nd pass with low model to fix quality when using sparse attention**
  - Context: For improving sparse attention results
  - *From: Ada*

- **SVI works much better with WAN22 fun inp model and waninpainttovideo node**
  - Context: For video extension workflows
  - *From: 42hub*

- **Delete the added 5 frames and use ones from previous generation when stitching with SVI**
  - Context: The added frames are glitchy but motion is kept after deletion
  - *From: lemuet*

- **Installing Flash Attention 2.8.3 reduces generation time by 25%**
  - Context: For HoloCine optimization (Blackwell cannot install Flash Attention 3)
  - *From: BNP4535353*

- **Use bucket resolutions for LongCat**
  - Context: Model is picky about input resolution
  - *From: Kijai*

- **Use different seeds per clip extension in SVI**
  - Context: Important to avoid burning and looping if prompt is same
  - *From: JohnDopamine*

- **Make sure all cuts are 4t+1 for Holocine**
  - Context: When using holocine shot args
  - *From: shaggss*

- **Holocine limit is 15 seconds for quality**
  - Context: Beyond 15sec quality degrades significantly
  - *From: avataraim*

- **Use detailed prompts with MoCha for better character likeness**
  - Context: Generic prompts work but more detail improves results, especially for character consistency
  - *From: DawnII*

- **Use 10 steps for good balance of quality and speed with LongCat**
  - Context: 5 steps too fast, 15 steps slower, 10 steps provides good quality/speed balance
  - *From: avataraim*

- **Clear triton caches when torch compile runs old code**
  - Context: When using torch compile and getting unexpected behavior
  - *From: Kijai*

- **For extending videos, take x frames from end of previous gen to start next**
  - Context: Standard extend workflow technique, join result to previous gen minus x frames
  - *From: Kijai*

- **Use shot builder with Holocine text encode instead of WanVideo text encode**
  - Context: When facing weird errors with WanVideo text encode node
  - *From: shaggss*

- **Use different seeds for each shot when extending**
  - Context: For video extension with LongCat using last frame method
  - *From: avataraim*

- **LongCat likes specific prompt structure**
  - Context: More misses without proper prompt structure for T2V
  - *From: Pandaabear*

- **Always connect image embed node or workflow won't work**
  - Context: Workflow needs image embed connected to something to function
  - *From: Cubey*

- **Use NeatVideo for denoising Wan VAE artifacts**
  - Context: Enable temporal and set spatial to low weight to preserve detail
  - *From: spacepxl*

- **Treat VAE training as conditional GAN instead of just decoder**
  - Context: For better detail generation and noise reduction
  - *From: spacepxl*

- **Use context windows for first/middle/last frame reference**
  - Context: Can give each window a latent for frame conditioning
  - *From: blake37*

- **Reduce contrast in driver video for Uni3C controlnet**
  - Context: Helps with stronger overlay effects at higher resolutions
  - *From: paulHAX*

- **For WAN low noise refinement use shift 1, denoise 0.2-0.3, with distill LoRA use 2 steps, without distill use 8-10 steps and CFG 3-5**
  - Context: When refining images after generation
  - *From: spacepxl*

- **Use different seed when doing img2img to avoid same noise causing problems**
  - Context: When getting repeated artifacts in img2img
  - *From: spacepxl*

- **Set shift using SD3 node, default is 5 which makes img2img annoying**
  - Context: For better img2img control
  - *From: spacepxl*

- **Try DPM++ SDE/beta sampler with 6/3 steps for OVI**
  - Context: For faster OVI inference
  - *From: avataraim*

- **Use interpolation on WAN 2.2 for better frame rates**
  - Context: Can get decent 24fps gens with interpolation
  - *From: b̶̈́͠o̶̗̅n̶̽̒k̵̽̿*

- **Disconnect T5 if prompt is cached**
  - Context: To reduce RAM usage, better to use Cached node
  - *From: Kijai*

- **Use layer offloading with AI toolkit for efficient training on 4090**
  - Context: For LoRA training when you need some offloading
  - *From: Kiwv*

- **For video continuation without degradation, use LongCat which is natively pretrained on video continuation tasks**
  - Context: When needing long video generation
  - *From: JohnDopamine*

- **Use 2.1 lightx2v as safe bet for distill LoRA**
  - Context: When choosing distill LoRA for Wan 2.2
  - *From: Kijai*

- **Avoid Lightning LoRAs if you don't want style/exposure changes**
  - Context: When wanting neutral LoRA effects
  - *From: Kijai*

- **For anime style, use AniSora 3.2 for high noise model**
  - Context: When generating anime content
  - *From: Kijai*

- **Don't bother much with low noise side, basic 2.1 lightx2v is good and neutral**
  - Context: When setting up LoRA configuration
  - *From: Kijai*

- **Generate at 720p for better pose following in WanAnimate**
  - Context: Higher resolution gives better results and pose adherence than lower resolutions
  - *From: Charlie*

- **Focus on developing integration tools rather than waiting for perfect models**
  - Context: Open source models succeed by using them together in sequence/simultaneously to fill each other's gaps
  - *From: Ablejones*

- **Use controlled methods for production work**
  - Context: Pure prompt-to-video or image-to-video currently looks like 'AI slop' - controlled methods are the only usable option for production
  - *From: Kijai*

- **Learning current tools gives advantage over waiting**
  - Context: People taking time to learn now will have more capability than those only starting with future tools
  - *From: DawnII*

- **For object removal in video, use Qwen edit or inpaint model on one frame then fill rest with VACE if minimax/VACE alone isn't working**
  - Context: Video object removal workflows
  - *From: spacepxl*

- **Run video through upscale on low denoise second time to reduce degradation**
  - Context: Dealing with video quality degradation
  - *From: VK (5080 128gb)*

- **Use Anisora at 0.5 strength for cartoon content**
  - Context: Cartoon/animated content generation
  - *From: Gleb Tretyak*

- **Don't use CFG with newest LightX2V - adding 2 CFG steps resulted in trash results**
  - Context: Using new v1030 LoRA
  - *From: Gleb Tretyak*

- **Use 'shot' instead of 'camera' in prompts**
  - Context: When trying to control camera movement
  - *From: DawnII*

- **Use cached node to avoid speed issues**
  - Context: After initial processing with slower models
  - *From: DawnII*

- **Can use last frame and continue for extensions**
  - Context: Simple method for extending LongCat videos
  - *From: avataraim*

- **Clean HD regularly to free up space**
  - Context: Spend 30m clearing unused models - often find 300gb of unused stuff
  - *From: Kiwv*

- **Use T5 and CLIP text encoders because they are naturally tuned to relate to images**
  - Context: Compared to other encoders like Qwen which require the video model to do much more work with embeds
  - *From: Kiwv*

- **Scaling up quality data is as effective as scaling up params or compute for improving model clarity**
  - Context: When training video models
  - *From: Kiwv*

- **Use 40 steps for Qwen Edit for much better sharpness**
  - Context: When generating at higher resolutions like 1664x928
  - *From: aikitoria*

- **ChronoEdit works best for animating existing image rather than redrawing from different POV**
  - Context: If you prompt it to redraw the image from a different pov, it's ass
  - *From: Ness*

- **Don't update ComfyUI frequently to avoid breaking nodes**
  - Context: For stability with custom nodes
  - *From: Kiwv*


## News & Updates

- **Hunyuan working on new video model**
  - 200GB model size mentioned, unknown if it will be open source
  - *From: yi*

- **Kijai updated wrapper example to use new preprocessing nodes**
  - Updated example workflow available
  - *From: Kijai*

- **ComfyUI PR for optimizations submitted**
  - GitHub PR #10141 for VRAM optimizations
  - *From: JohnDopamine*

- **LanPaint now supports Wan 2.2**
  - Supports text to image generation with Wan2.2 T2V model
  - *From: s2k*

- **New LightX2V updates coming with date-based versioning**
  - Team adopted new algorithm, subsequent updates will be relatively fast, using dates instead of version numbers
  - *From: slmonker(5090D 32GB)*

- **Ovi model released**
  - 11B video model with audio output based on wan2.2 5B and Mmaudio, weights available
  - *From: yi*

- **Face bbox output added to preprocessing workflow**
  - Same bbox that crops the face, now has output for easier face swapping
  - *From: Kijai*

- **New optimization models released**
  - Palingenesis released a week ago, and Wan 2.2-Lightning 4-step LoRA released 5 days ago
  - *From: Drommer-Kille*

- **Sora 2 code released by OpenAI**
  - Invite codes available for Sora 2 access
  - *From: Draken*

- **Ovi model release**
  - Character.ai released Ovi model based on 5B parameters with audio generation capabilities
  - *From: BecauseReasons*

- **No official VACE for A14B planned**
  - There won't be any official VACE for A14B model, but Fun version works okay
  - *From: Kijai*

- **ComfyUI mask operations optimized**
  - Blockify and DrawMaskOnImage nodes now run on GPU for massive speed improvements
  - *From: Kijai*

- **New Lightning LoRAs released**
  - 250928 LoRAs released 5 days ago, very good for motion preservation
  - *From: pom*

- **Ovi model available with fp8 quantization**
  - Reduces VRAM requirement to 16GB
  - *From: Stad*

- **DC-VideoGen source code released**
  - Promises up to 3.75x speedup for Wan models
  - *From: slmonker*

- **OVI model released**
  - 11B parameter audio-video model based on Wan 2.2 5B with added audio backbone, supports speech generation and sound effects
  - *From: mallardgazellegoosewildcat*

- **OVI ComfyUI integration request opened**
  - GitHub issue opened for ComfyUI support but no timeline confirmed
  - *From: Lodis*

- **OVI developer working on ComfyUI implementation**
  - Character.ai team developing native ComfyUI support
  - *From: Stad*

- **Self Forcing++ from ByteDance announced**
  - Promises minute-long videos, code will be released soon
  - *From: Shubhooooo*

- **Civitai added Sora 2.5 listing**
  - Indicates potential upcoming release
  - *From: Ryzen*

- **OVI ComfyUI implementation being worked on**
  - Developers mentioned on GitHub they're working on it, but no official confirmation yet
  - *From: Stad*

- **OVI model now available in ComfyUI**
  - RunningHub created ComfyUI_RH_Ovi implementation, Kijai looking at adding to WanVideoWrapper
  - *From: slmonker(5090D 32GB)*

- **Sora 2 API pricing announced**
  - Per second pricing: $0.05 for 480p, $0.10 for 720p, $0.15 for 1080p
  - *From: Juampab12*

- **Wan 2.5 speculation**
  - Community expects Wan 2.5 might be 40B MoE model with activated parameters within consumer hardware range
  - *From: slmonker(5090D 32GB)*

- **Kijai merged Lynx branch into main WanVideoWrapper**
  - Includes sample workflow, now available in main branch
  - *From: phazei*

- **OVI nodes now available for ComfyUI**
  - ComfyUI_RH_Ovi repository available on GitHub
  - *From: Lodis*

- **Ovi people pushing Ovi nodes to WanVideoWrapper**
  - 8k lines PR being submitted to integrate Ovi into WanVideoWrapper
  - *From: Stad*

- **OVI native ComfyUI implementation in progress**
  - Kytra working on native implementation with native comfy model loading/patching/encoding/decoding, T2V already working
  - *From: Kytra*

- **AI-Toolkit now supports training LoRAs with mostly RAM**
  - About 50% speed difference, 17s/it for 3000 steps (~14hrs on 6GB laptop), works for various models
  - *From: Ada*

- **Hunyuan 3D 2.1 released**
  - Fast mesh generation from images, works well in Blender
  - *From: U̷r̷a̷b̷e̷w̷e̷*

- **OVI (Open source Veo3-like) released by Kijai**
  - Video with audio generator based on Wan2.2 5B and MMAudio, supports T2V and I2V
  - *From: Stad/Charlie*

- **AniSora extracted into LoRA format**
  - I also extracted it into a lora that works ok
  - *From: Kijai*

- **OVI model available in test branch**
  - 11B audio-video model in the ovi branch of WanVideoWrapper
  - *From: Kijai*

- **rCM LoRA extracted and available**
  - SOTA distillation method from Nvidia, available as LoRA
  - *From: Kijai*

- **Warning about fake 'Eddy' releases**
  - Kijai warns against fake releases like 'sageattn4', 'wan animate v3' etc. - described as bullshit and potentially malicious
  - *From: Kijai*

- **GAGA model coming according to bdsqlsz**
  - Announcement on Twitter about upcoming GAGA release
  - *From: Tony(5090)*

- **Fake Wan 2.5 on HuggingFace**
  - Someone uploaded a fake wan-2.5 model to HuggingFace
  - *From: Lodis*

- **Wan upscaler workflow completed**
  - Handles 720p to 2K and 360p to 2K upscaling with improved stability and sharpness
  - *From: Lan8mark*

- **Neex bumped testing to next week Thursday morning**
  - Will be doing evaluation testing on Thursday morning
  - *From: Neex*

- **ComfyUI memory leak fix implemented**
  - Recent commit addressed memory leak issue causing OOM problems
  - *From: JohnDopamine*

- **SAM 3 announced by Meta**
  - Available through waitlist signup, successor to SAM 2.1
  - *From: Kijai*

- **New RCM LoRA released**
  - Alternative to lightx2v by Nvidia developers for speed/distillation
  - *From: JohnDopamine*

- **SEC nodes available**
  - ComfyUI SEC nodes released for enhanced SAM2 guidance
  - *From: ArtOfficial*

- **PyTorch 2.9 and 2.10 available**
  - Newer PyTorch versions available, 2.8 has known issues
  - *From: Tony(5090)*

- **New Wan 2.2 I2V Lightx2v full distilled models released**
  - 24GB models available on HuggingFace, both high and low noise versions
  - *From: yi*

- **Lightx2v team released LoRA versions alongside full models**
  - LoRAs available in the same repo as the full models
  - *From: JohnDopamine*

- **New LightX2V High model released**
  - Full 28GB model released with better extraction compared to original LoRA that was missing patches
  - *From: JohnDopamine*

- **FlashVSR super resolution model released**
  - New super resolution model based on Wan with only 11GB VRAM usage, much less than other diffusion upscalers
  - *From: yi*

- **Triton 3.5.0 released with fp8 fixes**
  - New release specifically mentions fp8 patch merged to fix compilation issues
  - *From: phazei*

- **Windows wheels available for SageAttention and Triton**
  - Prebuilt packages available at woct0rdho repos
  - *From: Kijai*

- **AI-toolkit now supports video training and has queue feature**
  - Works with Wan 2.2 but has bugs with 2.1
  - *From: Drommer-Kille*

- **Fake news about Higgsfield acquiring Wan 2.5 for $100M**
  - Multiple sources confirm it's AI-generated spam articles on Medium knockoff sites
  - *From: JohnDopamine*

- **Kijai released workaround for PyTorch 2.9.0 VAE issue**
  - Added fix that does conv3d in fp32 to bypass bug while using less VRAM than full fp32
  - *From: Kijai*

- **HuMo best practice guide coming soon**
  - Team announced a Best-Practice Guide for HuMo will be released soon
  - *From: aiacsp*

- **New Wan2.2 4-step distill models released**
  - High noise model is completely new, low noise reuses old one. Much improved over Lightning distill
  - *From: aikitoria*

- **22B video model by cloneofsimo**
  - Trained by small team at Fal, Hunyuan Video level quality, not yet released
  - *From: yi*

- **Kandinsky 5 Pro confirmed for end of November**
  - Expected to compete with Waver, uses Hunyuan VAE
  - *From: yi*

- **DimensionX finally released after 10 month wait**
  - ComfyUI support available
  - *From: Kijai*

- **Lightx2v released reorganized WAN 2.2 distilled models**
  - New release has same SHA256 as previous models, just better organized. High uses MOE lora, Low uses existing models
  - *From: FL13*

- **FlashVSR developers working on consumer GPU version**
  - Working on version without Block-Sparse Attention that maintains quality but will run slower on consumer GPUs
  - *From: JohnDopamine*

- **New UniMMVSR video upscaler from Kling announced**
  - Video upscaler that can use reference image for guidance, similar to what WAN 2.2 I2V does. Code coming soon
  - *From: Shubhooooo*

- **rCM LoRAs released for Wan 2.1**
  - 720p and 480p rCM LoRAs extracted and available, 4-step distillation models
  - *From: Kijai*

- **Wan 2.5 T2I available at FAL**
  - Text-to-image model with 1500 token limit vs 512 for previous versions
  - *From: Drommer-Kille*

- **ComfyUI memory leak patches released**
  - Recent ComfyUI updates patched memory leaks in past week or two
  - *From: JohnDopamine*

- **rCM scheduler added to WanVideoWrapper**
  - New scheduler option available, though not necessarily better than existing options
  - *From: Kijai*

- **New VACE model Ditto released with 3 specialized modules**
  - Ditto uses WanVideoWrapper as ComfyUI example, has global style, global, and sim2real variants
  - *From: Kijai*

- **Ditto added CC 4.0 non-commercial license to their code**
  - License applied retroactively as there was no license before
  - *From: Kijai*

- **Ditto dataset released**
  - 1TB+ dataset still uploading to HuggingFace, contains synthetic-to-real training data
  - *From: Dever*

- **Krea realtime video model released**
  - Based on Wan 2.1, available on HuggingFace
  - *From: Desto Geima*

- **Context window bug with uni3c fixed**
  - Bug that prevented uni3c camera control from working with context windows has been resolved
  - *From: Kijai*

- **Krea realtime went open source**
  - Didn't sell well according to speculation
  - *From: hicho*

- **Wavespeed got new Wan 2.5 modality (video-extend)**
  - New extension capability
  - *From: ZeusZeus (RTX 4090)*

- **MUG-V 10B video model released**
  - Paper available, no samples yet
  - *From: yi*

- **MoCha merged into main branch of WanVideoWrapper**
  - No longer in PR, available in main with new workflow including block swap
  - *From: Kijai*

- **MoCha model released by Orange-3DV-Team**
  - Character replacement model working in ComfyUI via Kijai's implementation
  - *From: Dever*

- **Krea realtime video model and LoRA released**
  - HuggingFace release with distill LoRA for faster generation
  - *From: s2k*

- **Rolling Forcing model initial commit on HuggingFace**
  - Reference-to-video model using WAN 2.1-14B
  - *From: JohnDopamine*

- **Updated Wan 2.2 distill LoRAs from lightx2v**
  - New version marked as 1022, replaces previous versions
  - *From: Gateway {Dreaming Computers}*

- **Mixture of Groups Attention paper released**
  - Technique for long video generation, could improve temporal consistency
  - *From: DawnII*

- **New LightX2V distill LoRAs released**
  - Dated 1022, appear to be improved versions with better prompt following
  - *From: Ada*

- **QwenImage VAE converted for ComfyUI**
  - Available at Kijai's HuggingFace repo in fp32 format
  - *From: Kijai*

- **Rolling Force model released**
  - 1.3B T2V causal model from TencentARC, 17GB due to multiple weight copies
  - *From: yi*

- **Stable Video Infinity released**
  - Claims infinite length video generation with high temporal consistency
  - *From: Kijai*

- **SVI (Stable Video Infinity) model released**
  - Claims unlimited context length, supports up to 4 minute videos with no quality decrease, includes shot and film LoRAs
  - *From: Ada*

- **New lightx2v distill LoRA available**
  - Version 1022 released with improved performance over previous MoE version
  - *From: Kijai*

- **ByteDance open sourced Video-As-Prompt (VAP)**
  - 49-frame video prompting system for Wan 2.1 14B with in-context learning capabilities
  - *From: JohnDopamine*

- **LTX 2 announced by Lightricks**
  - Audio+video generation, 10s+ videos, open source weights coming later this year
  - *From: yi*

- **SVI team planning to train for Wan 2.2**
  - Mentioned in FAQ, will support the 5B model
  - *From: DawnII*

- **LTX 2 coming late November**
  - LTX 2 announced for late November release, weights not available yet
  - *From: Lodis*

- **SVI LoRAs converted to native ComfyUI format**
  - All SVI LoRAs now available in fp16 format compatible with native ComfyUI nodes
  - *From: Kijai*

- **Wan 2.5 expected to respond to LTX 2**
  - Speculation that Wan team will release 2.5 open source version around LTX 2 launch
  - *From: hicho*

- **HoloCine released by Alibaba - T2V model with minute-level generation capability**
  - 14B and 5B variants, supports structured prompting with character consistency, trained on 400k multi-shot samples
  - *From: 42hub*

- **New LightX2V variant called '1022' released**
  - Another speed optimization LoRA variant
  - *From: 42hub*

- **Multiple HoloCine model variants planned**
  - HoloCine-14B-full, HoloCine-14B-sparse, versions for >1 minute, 5B variants for limited memory, HoloCine-audio in planning
  - *From: NebSH*

- **SVI developers request removal of fp8 versions from Kijai's repo**
  - Claim fp8 versions have issues, request use of their codebase instead
  - *From: DawnII*

- **Suplex LoRA uploaded to Civitai**
  - Wrestling move LoRA now available
  - *From: Lodis*

- **HoloCine license changed from Apache 2.0 to CC 4.0 share alike non-commercial**
  - Changed 4 hours after initial commit, but once Apache always Apache - can't change retroactively
  - *From: Kijai*

- **HoloCine released but no ComfyUI implementation yet**
  - Model released 7 hours ago, weights can be tried but multiple shots for long video not implemented yet
  - *From: Kijai*

- **HoloCine sparse model uploaded**
  - Sparse version now available on HuggingFace
  - *From: NebSH*

- **New UniLumos model coming**
  - Another lumos model coming from Alibaba-DAMO-Academy
  - *From: DawnII*

- **Reference padding bug fixed**
  - Kijai fixed bug where reference frames were being zeroed out when using temporal masks
  - *From: Kijai*

- **HoloCine fp8 versions available**
  - Kijai released fp8 quantized versions of HoloCine models
  - *From: Lodis*

- **HoloCine sparse models uploaded**
  - Sparse model versions now available, enabling longer generation with less VRAM
  - *From: Lodis*

- **SVI for I2V confirmed not working with HoloCine setup**
  - SVI won't work in the current HoloCine implementation
  - *From: VK (5080 128gb)*

- **ComfyUI Cloud beta doesn't support custom nodes or models**
  - Only pre-made templates and API nodes available
  - *From: Govind Singh*

- **LongCat-Video released by Meituan (Chinese food delivery platform)**
  - 14B open video model, MIT license, single model for T2V and I2V
  - *From: yi*

- **Holocine models available as FP8 versions**
  - Available in Kijai's HuggingFace folder
  - *From: avataraim*

- **HoloCine one minute version already trained**
  - Will be released after further dataset scaling
  - *From: NebSH*

- **SVI Film 2.2 (both 5B and 14B) on Wan team's todo list**
  - Readme updated a few days ago with this information
  - *From: DawnII*

- **UltraGen released supporting 4K resolution**
  - Uses Wan 1.3B model
  - *From: Shubhooooo*

- **LongCat ComfyUI implementation available**
  - Testing branch available at ComfyUI-WanVideoWrapper/tree/longcat with models on HuggingFace
  - *From: Kijai*

- **Holocine nodes added to ComfyUI**
  - WanVideoHolocineShotBuilder and related nodes now available
  - *From: shaggss*

- **SVI repo updated with seed guidance**
  - SVI devs updated readme to emphasize using different seed per clip extension
  - *From: JohnDopamine*

- **HoloCine support added to ComfyUI via pull request**
  - Working implementation available though described as messy, allows 15 second generation
  - *From: Kijai*

- **LongCat fp8 version uploaded**
  - Kijai provided fp8 quantized version of LongCat model
  - *From: Lodis*

- **SageAttention 2.2.0 available with better torch compile support**
  - Gets rid of graph breaks so torch compile works better, fixes first run VRAM issues
  - *From: Kijai*

- **LongCat implementation in WanVideoWrapper available**
  - Kijai implementing LongCat in separate branch, workflow available in LongCat folder
  - *From: Kijai*

- **Holocine support being added via PR to wrapper**
  - Much work in progress, PR up for wrapper adding HoloCine support
  - *From: Kijai*

- **Latest SageAttention 2.2.0 supports torch compile**
  - Can run Wan without any graph breaks, inductor full graph works, avoids first run VRAM issue
  - *From: Kijai*

- **Triton wheel now supports e4m3fn compilation on 3090**
  - With latest triton wheel compiling e4m3fn works on 3090, finally solved
  - *From: Kijai*

- **Kaleido 14B-S2V model released**
  - Reference to video model based on Wan 2.1 T2V, uses R-RoPE mechanism
  - *From: yi*

- **Ditto developers added Wan denoise/enhance code**
  - Open sourced style/edit tool with Wan enhancement capabilities
  - *From: JohnDopamine*

- **WAN 2.5 is currently commercialized for live streaming and may not be open source**
  - Chinese community feedback suggests performance not ideal yet, prefer refinement before release. Sora 2 and Veo 3.1 launches gave momentum
  - *From: 青龍聖者@bdsqlsz*

- **Holocine proper implementation available with attention code**
  - Repository moved to https://github.com/Dango233/ComfyUI-WanVideoWrapper-Multishot
  - *From: NebSH*

- **New helper node being developed for video extension workflows**
  - Kijai building it for LongCat example, will include in example workflow
  - *From: Kijai*

- **LTX-2 expected open source release**
  - Apparently LTX-2 will be open source end of November
  - *From: Kiwv*

- **WAN 2.5 open source status unclear**
  - WAN team said today's live stream only discusses commercial applications, no notification yet about open source release
  - *From: slmonker(5090D 32GB)*

- **DITTO released this week with Denoise Enhancing**
  - New release includes code for Denoise Enhancing related to their work
  - *From: JohnDopamine*

- **Sage 2.2.0 available with pip**
  - Finally available with pip but still seems to compile
  - *From: Kijai*

- **LongCat model released - Wan architecture trained from scratch**
  - Features native video continuation, refinement LoRA for 720p/30fps output
  - *From: JohnDopamine*

- **New ComfyUI UI changes with floating menus and subgraph support**
  - UI updates causing navigation issues for some users
  - *From: JohnDopamine*

- **Morph LoRA released for multi-frame video generation**
  - Claims to support up to 5 frame inputs for better interpolation
  - *From: VK (5080 128gb)*

- **ChronoEdit released by NVIDIA**
  - Wan-based image editing model with code and weights available
  - *From: JohnDopamine*

- **New ComfyUI offloading flag for faster generation when offloading**
  - Performance improvement for memory-constrained setups
  - *From: Lumifel*

- **Qwen team has open source music model coming soon**
  - Announced by Qwen CEO, both Qwen and Wan are developed by different Alibaba teams
  - *From: JohnDopamine*

- **UMG and Udio reached licensing agreement**
  - New Licensed AI Music Creation Platform - indicates copyright holders are accepting AI licensing rather than fighting it
  - *From: Draken*

- **Major ComfyUI WanVideo update released**
  - Includes LongCat support, norm layers in fp32, improved LoRA storage method, and various optimizations
  - *From: Kijai*

- **Qwen and Wan confirmed as both Alibaba projects**
  - Qwen from Alibaba Cloud team (LLMs), Wan from Ali-Vilab Team (video generation)
  - *From: JohnDopamine*

- **ChronoEdit models released by Kijai**
  - Converted NVIDIA ChronoEdit models available - full model and distill LoRA rank32, defaults: 8 steps, cfg 1.0, shift 2.0
  - *From: Kijai*

- **New LightX2V 1030 LoRA released**
  - Third iteration of 2.2 high noise LoRA with improvements in prompt following and camera control
  - *From: Kijai*

- **LongCat merged into main branch**
  - LongCat architecture now available in main ComfyUI implementation
  - *From: Lodis*

- **FlashVSR v1.1 released**
  - Available on HuggingFace with improvements
  - *From: yi*

- **New wan2.2_lightx2v_1030 LoRA available**
  - High noise LoRA for 4 steps, rank 64, bf16
  - *From: avataraim*

- **ChronoEdit GGUF version released**
  - QuantStack has released ChronoEdit-14B-GGUF
  - *From: YarvixPA*

- **Alibaba officially announced partnership with Higgsfield**
  - Posted on Alibaba Cloud X account
  - *From: ZeusZeus (RTX 4090)*

- **Flash VSR v1.1 has been updated**
  - New version available
  - *From: Lodis*

- **LTX 2 weights expected end of November according to devs**
  - Unless they change their minds, confirmed by LTX team member
  - *From: ZeusZeus*

- **Wan 2.5 may not be open sourced**
  - Someone with insider info recently said they will not release the weights
  - *From: seitanism*

- **LongCat video extension will be possible on fal later today**
  - Ability to upload your own video to be extended
  - *From: Benjaminimal*

- **LTX2 will release end of November**
  - Expected to be competitive with Wan, with realtime 4k video capabilities mentioned
  - *From: Stad*

- **Sora Pro plan limits severely reduced**
  - Went from 99 gens a day to 30 down to 5 for the pro plan
  - *From: Ruairi Robinson*

- **Control flow and loops coming to ComfyUI**
  - Already possible but no purely native core node to do so right now
  - *From: Kijai*


## Workflows & Use Cases

- **Using Wan Alpha with transparent backgrounds for compositing**
  - Use case: Creating B-movie horror effects by combining transparent video with backgrounds in GIMP and Shotcut
  - *From: U̷r̷a̷b̷e̷w̷e̷*

- **VACE dual model workflow for multiple inpainting passes**
  - Use case: Running workflow multiple times with no loss on unmasked areas
  - *From: mdkb*

- **Batch processing with wildcards for character and style variation**
  - Use case: Loop 300 generations at 720x1280 with random characters and styles
  - *From: Drommer-Kille*

- **Using QWen VL for face bbox detection**
  - Use case: Creating face masks for VACE workflows, can describe any part via natural language
  - *From: piscesbody*

- **InfiniteTalk for I2V with FantasyPortrait for V2V**
  - Use case: Audio-driven video generation, stronger with FantasyPortrait, supersedes MultiTalk
  - *From: mdkb*

- **Dual model workflow with InfiniteTalk**
  - Use case: Memory-efficient alternative to Magref fp8 setup, though InfiniteTalk doesn't do much on high noise model
  - *From: mdkb*

- **WanAnimate with built-in embed windows**
  - Use case: Achieving 25-second consistent video generation without traditional context windows
  - *From: A.I.Warper*

- **Using context windows to avoid degradation**
  - Use case: Disable other windowing by setting frame_window_size equal to total frames, then use context as normal
  - *From: Kijai*

- **HuMO + InfiniteTalk combination**
  - Use case: Enhanced lipsync with more expression, using 6 second audio blocks at 65 frames
  - *From: mdkb*

- **3-sampler Lightning LoRA setup**
  - Use case: Best motion preservation with high/low noise split
  - *From: pom*

- **ClownShark tiling for upscaling**
  - Use case: Video upscaling with preview of whole video instead of individual tiles
  - *From: FL13*

- **ByteDance VAE + VibeVoice integration**
  - Use case: Audio reconstruction without finetuning, though adding extra VAE refiner stage takes more time
  - *From: MysteryShack*

- **Wan 2.2 MOE step splitting**
  - Use case: Use High Noise for steps 0-3, Low Noise for steps 3-8 in 8-step generation, or 0-10 and 10-20 for 20 steps
  - *From: Kytra*

- **OVI audio-video generation**
  - Use case: Speech wrapped in <S>...<E> tags, optional audio description in <AUDCAP>...<ENDAUDCAP> tags
  - *From: slmonker(5090D 32GB)*

- **VACE Start End Frame with Replace Image in Batch**
  - Use case: Insert middle keyframes for first-middle-last frame morphing
  - *From: HeadOfOliver*

- **Music video generator using batch latents**
  - Use case: Automated music video creation with frame drift compensation
  - *From: Fill*

- **Multiple renders with different frame lengths in sequence**
  - Use case: Running list of latents into single ksampler for varied content
  - *From: Fill*

- **FFLF VACE driven wrapper with dual model setup**
  - Use case: Creating controlnet driving videos for higher quality clips later
  - *From: mdkb*

- **Face/head swap workflow posted on Civitai**
  - Use case: Character replacement in videos
  - *From: Alisson Pereira*

- **Hybrid model setup: 2.1 + Low 2.2 H + 2.1 distill**
  - Use case: Achieving amazing and different quality results
  - *From: hicho*

- **5B + 2.2 low model combination**
  - Use case: Getting 5B content quality with Wan 2.2 graphics by bypassing VAE
  - *From: hicho*

- **Character animation setup**
  - Use case: Using reference image for background and character with video for motion by disconnecting bg_images and mask
  - *From: Kijai*

- **Speed LoRA configuration**
  - Use case: Using LightX2V with manual sigma lists - speed LoRA on one model with low steps, other model with high steps
  - *From: 42hub*

- **USDU upscale with VACE dual model for fixing extended videos**
  - Use case: Combat burned-in look from multiple I2V continuations, fixing seams in extended videos
  - *From: mdkb*

- **Lightning LoRA with low-noise phase processing**
  - Use case: High quality fast T2V generation - 720p in 160 seconds
  - *From: Lan8mark*

- **High-noise resolution reduction then upscale**
  - Use case: Speed optimization for video generation - use half resolution for high-noise steps, then upscale for low-noise phase
  - *From: Lan8mark*

- **Triple chained samplers with different sigma handoff percentages**
  - Use case: I2V workflows for WAN 2.2, though user seeking definitive best practices
  - *From: 32Bit_Badman*

- **Latent upscaling method for 3-4x speed boost**
  - Use case: 5 steps run at 384p, and just 3 at full 720p. From 1100 seconds down to 160 with no visible quality loss
  - *From: Lan8mark*

- **VACE for keyframing**
  - Use case: You can use vace as inpaint, as in you can use it to any generate/fill any frames in a sequence, start, middle, end, anywhere. Can even be used as interpolation
  - *From: lemuet*

- **Hybrid setup: WAN Fun Control High Noise + WAN I2V Low Noise**
  - Use case: The details carried over perfectly for preserving image details
  - *From: Lan8mark*

- **WAN 2.2-based 2K upscaler**
  - Use case: High-quality video upscaling, claimed as fastest and highest-quality available
  - *From: Lan8mark*

- **Dual model approach with shift control**
  - Use case: Using shift parameter to control step point and work on structure
  - *From: mdkb*

- **WAN animate with temporal masking**
  - Use case: Scene replacement and character replacement with masking support
  - *From: Draken*

- **OVI full scene change**
  - Use case: Complete scene transformation rather than just character replacement
  - *From: Juampab12*

- **MAGREF + WAN 2.2 character consistency**
  - Use case: Multi-character consistency in I2V generation
  - *From: Elvaxorn*

- **Upscaler workflow for WAN videos**
  - Use case: 720p to 2K upscaling in ~150s, 480p to 2K in ~350s on 5090
  - *From: Lan8mark*

- **VACE 2.2 character replacement**
  - Use case: Replace characters in video while maintaining consistency using MagRef and RCM LoRA
  - *From: Elvaxorn*

- **Dual model Wan 2.2 with VACE**
  - Use case: High and low noise model combination with VACE for character control
  - *From: mdkb*

- **Video to video upscaling**
  - Use case: Use Wan 2.2 low noise model for detail enhancement and upscaling
  - *From: ingi // SYSTMS*

- **3 KSampler method with new Lightx2v**
  - Use case: Using 2-2-2 step split works fine with new LoRA
  - *From: asd*

- **Using skimmed CFG with MoE sampler for better prompt adherence**
  - Use case: Higher CFG on first steps, dropping to 1.0 to prevent burn
  - *From: GalaxyTimeMachine*

- **3-sampler Lightning setup**
  - Use case: Better results with new LoRA: 1 step HN no lora cfg 3.5 + 2 step HN with new lightx2v + 3 step LN with old 2.1 lightx2v
  - *From: FL13*

- **2-part OVI + InfiniteTalk**
  - Use case: Combining OVI video generation with InfiniteTalk for talking videos
  - *From: Kijai*

- **VACE for AI interpolation**
  - Use case: Using Wan VACE for true AI interpolation between frames
  - *From: FL13*

- **Using TaylorSeer with Wan models for faster inference**
  - Use case: Speeding up generation by skipping steps with minimal quality loss
  - *From: yi*

- **FlashVSR upscaling integrated with Wan video generation**
  - Use case: Fast video upscaling from 384 to 1024 resolution
  - *From: Kijai*

- **Multi-sampler setup with different CFG values per step**
  - Use case: Fine-tuning generation quality and speed
  - *From: Mattis*

- **3-sampler system for Wan 2.2 without speed LoRAs on high model**
  - Use case: 8 steps total for high model, 4 steps for low with speed LoRA - achieves better motion and quality
  - *From: Zabo*

- **FlashVSR with Cinescale LoRA and context windows**
  - Use case: Video upscaling with 0.75 denoise, processed in chunks like 81 frames at a time
  - *From: Elvaxorn*

- **VACE video stitching using frame inpainting**
  - Use case: Creating long videos by connecting shorter clips with 10 frame overlap
  - *From: Koba*

- **CineScale two-sampler setup**
  - Use case: Generate 1080p then latent upscale to second sampler with RoPE scaling
  - *From: DawnII*

- **Video chunking for long video upscaling**
  - Use case: Use load video node and meta batch manager for processing long videos
  - *From: happy.j*

- **Two-stage pose concatenation system**
  - Use case: Takes two videos and concatenates 3D pose estimations projected into 2D space, with controllable strength mixing
  - *From: Mads Hagbarth Damsbo*

- **rcm + lightning combination for speed**
  - Use case: Using rank148 rcm at high 4.0 + lightning at 1.0 on low, 4 steps dpm++sde, generates 1024x576 upscaled to FHD in under 3 minutes
  - *From: aipmaster*

- **Sectioned video upscaling for long clips**
  - Use case: Split long videos to latent files, upscale in 120 frame sections with 100 frame overlap, combine in DaVinci
  - *From: mdkb*

- **OVI + InfiniteTalk pipeline**
  - Use case: Generate video with OVI then add lipsync with InfiniteTalk at low denoise
  - *From: Charlie*

- **FlashVSR for render cleanup**
  - Use case: Fix bad looking renders at 0.8 strength in single step
  - *From: mdkb*

- **InfiniteTalk vid2vid for lipsync**
  - Use case: Add lipsync to existing video, requires masking setup
  - *From: Kijai*

- **Clownshark sampler with temporal masks**
  - Use case: Advanced sampling with regional conditioning over time
  - *From: TK_999*

- **3 sampler I2V setup**
  - Use case: 1st step no LoRA 3.5 CFG, 2nd step 2-step lightning on high, 3rd step 3-step with 2.1 lightx2v on low
  - *From: FL13*

- **Style transfer with Ditto LoRAs**
  - Use case: Apply style transfer to videos using text prompts like 'Make it Pixel Art'
  - *From: Kijai*

- **RGB control for style transfer**
  - Use case: Easier than pose estimation for basic video stylization
  - *From: Draken*

- **VACE extension for longer videos**
  - Use case: Use VACE extend with last few frames for longer Ditto generations
  - *From: DawnII*

- **Multi-stage I2V looping**
  - Use case: Taking last frame of generated video as starting frame for next generation in a loop
  - *From: Wembleycandy*

- **Krea LoRA with Wan 2.2**
  - Use case: Using extracted Krea realtime LoRA on Wan 2.2 with specific strength settings
  - *From: aipmaster*

- **Colab tunneling for ComfyUI**
  - Use case: Using built-in colab tunneling instead of external services
  - *From: Draken*

- **Sora watermark removal with FlashVSR upscaling**
  - Use case: Combined workflow for watermark removal and upscaling
  - *From: Govind Singh*

- **MoCha character replacement with masking**
  - Use case: Replace characters in videos using reference images and masks
  - *From: Kijai*

- **Krea LoRA with high/low dual sampler**
  - Use case: Fast realistic video generation using Wan 2.2 setup
  - *From: aipmaster*

- **Wan 2.2 with Uni3C camera control**
  - Use case: Camera movement control in video generation
  - *From: DawnII*

- **VACE inpainting with NAG for object removal**
  - Use case: Remove objects/people from videos using inpainting
  - *From: art13.beck*

- **Chaining multiple I2V generations with 5 start frames**
  - Use case: Creating longer videos using SVI technique
  - *From: Kijai*

- **Using multiple start frames for I2V**
  - Use case: Improving temporal coherency and motion continuation
  - *From: Kijai*

- **I2V continuation with multiple frames**
  - Use case: Smooth video continuation by feeding last 5 frames from previous generation into I2V node
  - *From: Kijai*

- **SVI shot workflow with padding**
  - Use case: Uses single start image with reference image padding for extended video generation
  - *From: Kijai*

- **SVI film workflow**
  - Use case: Uses 5 start images with zero padding for scene transitions and different prompts per segment
  - *From: Kijai*

- **SVI film LoRA for video extension**
  - Use case: Extending 5-second videos to 10+ seconds with motion continuity
  - *From: Tony(5090)*

- **Ditto for style transfer and character replacement**
  - Use case: Converting video styles (Ghibli, realistic, psychedelic) and replacing characters
  - *From: Drommer-Kille*

- **2-sampler batch setup for longer Ditto videos**
  - Use case: 72+72 frame batches merged together for extended video length
  - *From: hicho*

- **Video extension using SVI LoRAs**
  - Use case: Extending videos by taking last 5 frames and generating continuation with film LoRA
  - *From: Ablejones*

- **Scene continuity with SVI-shot**
  - Use case: Maintaining same scene for longer videos by repeating reference frame through entire sequence
  - *From: Ablejones*

- **Deforum output conversion through Wan**
  - Use case: Processing Deforum outputs at 0.7 denoise to maintain motion while reducing flickering
  - *From: VK (5080 128gb)*

- **VK's improved SVI extension method**
  - Use case: Better character consistency in video extension by including reference image as first frame in each segment
  - *From: VK (5080 128gb)*

- **InfiniteTalk audio-driven video generation**
  - Use case: Creating long lip-sync videos with minimal degradation using audio file to drive length
  - *From: seitanism*

- **HoloCine structured prompting for multi-shot scenes**
  - Use case: Creating cinematic sequences with character consistency using [character1] tags and [shot cut] markers
  - *From: Tachyon*

- **SVI Film method for motion continuation**
  - Use case: Continue last generation with last 5 frames of previous generation, padded with black
  - *From: Kijai*

- **SVI Shot method for endless I2V**
  - Use case: Last frame as input with original image as reference in all other frames, only first frame masked
  - *From: Kijai*

- **Using API calls with disk caching**
  - Use case: More practical for iterative work than ComfyUI loops, allows trying each segment multiple times
  - *From: Ablejones*

- **SVI film with 5-frame input**
  - Use case: Better consistency for video extension with multiple frame context
  - *From: Kijai*

- **infinitetalk + unianimate combination**
  - Use case: Long portrait animation with pose control and lip sync
  - *From: DawnII*

- **Film SVI with ref image insertion**
  - Use case: Insert ref image into 1 frame of five to help with consistency
  - *From: VK (5080 128gb)*

- **ViT pose retargeting for miniatures**
  - Use case: Animating miniatures and toys with proportion retargeting
  - *From: Neex*

- **HoloCine T2V with multi-shot prompts**
  - Use case: Generate 15+ second videos with scene transitions using | separated prompts
  - *From: seitanism*

- **Seamless video generation with automatic stray frame removal**
  - Use case: Removes stray frames automatically for seamless output without post-editing
  - *From: VK (5080 128gb)*

- **2.2 + SVI film + infinitetalk combination**
  - Use case: Using film LoRA with infinitetalk for enhanced continuity
  - *From: DawnII*

- **Holocine experimental workflow using models and video attention split**
  - Use case: Long video generation with shot transitions
  - *From: avataraim*

- **SVI with WAN 2.2 using Fun InP model and waninpainttovideo node**
  - Use case: Better SVI results
  - *From: Vérole*

- **Context overlap method for long generation**
  - Use case: 350+ frame generation
  - *From: VK*

- **HoloCine structured prompting**
  - Use case: Generate 15-second videos with scene cuts and character consistency using global caption, character descriptions, and shot-specific prompts with cut frames
  - *From: BNP4535353*

- **5-frame SVI method with Wan 2.2**
  - Use case: Video extension while maintaining character appearance consistency
  - *From: VK (5080 128gb)*

- **LongCat I2V extension**
  - Use case: Video extension with 13 start frames, requires character looking at camera at segment end
  - *From: aikitoria*

- **Holocine structured workflow**
  - Use case: Chain WanVideoHolocineShotBuilder for each shot, feed into WanVideoHolocinePromptEncode
  - *From: NebSH*

- **Holocine manual prompt**
  - Use case: Write prompt with [global caption] and [shot cut] markers, use with WanVideoTextEncode
  - *From: NebSH*

- **LongCat basic workflow**
  - Use case: TI2V generation with example workflow in longcat folder
  - *From: Kijai*

- **LongCat video extension using last frame continuation**
  - Use case: Creating longer videos by taking last frames and continuing generation
  - *From: avataraim*

- **HoloCine with shot cuts for 15 second structured video**
  - Use case: Generating cinematic videos with multiple shots and cuts
  - *From: 42hub*

- **LongCat video extension using last frame**
  - Use case: Creating longer videos by continuing from previous last frame with different seeds
  - *From: avataraim*

- **LongCat refinement pipeline**
  - Use case: Two-pass generation: low res first, then refiner lora for 720p/30fps
  - *From: Draken*

- **SVI with 5 frame batches**
  - Use case: Using SVI film loras with 5 start frames instead of 1 for better continuity
  - *From: Kijai*

- **SVI-film + HuMo for extended generations**
  - Use case: Long video generation with character consistency
  - *From: Ablejones*

- **Wan VAE 2x upscaler as hires fix**
  - Use case: Image upscaling without separate upscale model, works with qwen
  - *From: spacepxl*

- **VACE for first/middle/last frame conditioning**
  - Use case: Multi-keyframe video generation with frame conditions
  - *From: spacepxl*

- **OVI inpainting for lip sync and audio generation**
  - Use case: Generate base videos in WAN 2.2 then v2v inpaint with OVI to get lipsync/audio
  - *From: Hashu*

- **Video extension using LongCat LoRA**
  - Use case: Refining video generation with specific sampling parameters
  - *From: Kijai*

- **Multi-character LoRA per shot in Holocine**
  - Use case: Using different character LoRAs for each shot in multi-shot generation
  - *From: NebSH*

- **Latent space upscaling with WAN 2.2**
  - Use case: Upscaling between HN and LN processing, can run VACE WAN 2.2 to 720p on 3060 in 16 minutes
  - *From: mdkb*

- **Using LongCat refinement LoRA in V2V workflow**
  - Use case: Not using as intended but still does decent job for sharpening
  - *From: JohnDopamine*

- **LongCat extended video generation with segment prompting**
  - Use case: Creating long videos with different prompts for each segment
  - *From: JohnDopamine*

- **LLM-assisted prompting for video continuation**
  - Use case: Automatically generating prompts for next segments using last frame
  - *From: JohnDopamine*

- **T2V using I2V workflow without image inputs**
  - Use case: Text-to-video generation by removing image nodes from I2V workflow
  - *From: Pandaabear*

- **Sequential model usage for comprehensive video generation**
  - Use case: Using multiple models in sequence/simultaneously to have each fill gaps of the previous
  - *From: Ablejones*

- **ChronoEdit image editing using Wan temporal understanding**
  - Use case: Using Wan's video generation capabilities for sophisticated image editing tasks
  - *From: slmonker*

- **Using 2 or 3 KSamplers with Holocine + VACE 2.2 + 1030 lightx high + 1020 low**
  - Use case: Getting results on par with Wan 2.5
  - *From: Elvaxorn*

- **First frame + last frame with base Wan 2.2 for 201 frames**
  - Use case: Long video generation works surprisingly well
  - *From: mamad8*

- **ChronoEdit as I2V model at 5 or 29 frames, take last frame**
  - Use case: Image editing using video model as diffusion process
  - *From: Kiwv*

- **ChronoEdit image editing**
  - Use case: Use Wan I2V workflow with ChronoEdit model, use 5 or 29 frames
  - *From: Kiwv*

- **LongCat face consistency fix**
  - Use case: Use face inpaint pass with Phantom to maintain character identity in extensions
  - *From: Ablejones*

- **Context windows for longer generations**
  - Use case: Multiple chunks of 81 frames sampled at once, good for I2V identity preservation
  - *From: blake37*

- **LongCat generates long videos in chunks as video extensions**
  - Use case: All long videos are by their nature video extensions
  - *From: Benjaminimal*

- **VACE autoregressive video extension**
  - Use case: Filling left/right sides of LTX videos, but suffers from color drift and coherence issues
  - *From: Benjaminimal*

- **Long video generation using LightX LoRA with color matching**
  - Use case: Generating 1-minute videos by chaining 5-second segments with color match nodes between each segment
  - *From: aikitoria*


## Recommended Settings

- **riflex_freq_index in sampler**: 0
  - Non-zero values add strange effects with VACE
  - *From: scf*

- **Pose strength**: 1.3
  - Helps with timing delays in lip sync
  - *From: Charlie*

- **bbox_detector**: .torchscript
  - Dramatically faster than default, reduces processing from 17min to 3min
  - *From: xiver2114*

- **Frame count preference**: 97 frames
  - Avoids looping issues
  - *From: U̷r̷a̷b̷e̷w̷e̷*

- **Resolution matching**: Match video aspect ratio exactly
  - Prevents face detection failures
  - *From: Gateway {Dreaming Computers}*

- **Adams-Bashforth sampler**: Use under certain conditions
  - Gives CFG burn effect due to overly strong momentum from multistep
  - *From: mallardgazellegoosewildcat*

- **WanAnimate without LightX parameters**: steps=20, CFG=1, shift=5, scheduler=dmp++
  - Based on official diffusers code reference
  - *From: Christian Sandor*

- **Euler/beta sampler for 12GB VRAM**: Euler/beta scheduler
  - Speed - only slightly worse than dpm++ but much faster
  - *From: U̷r̷a̷b̷e̷w̷e̷*

- **CFG without Lightning LoRAs**: CFG 3.5
  - Need higher CFG when not using lightning or lightx loras
  - *From: DennisM*

- **Frame window size for long videos**: frame_window_size set to 77 for 600 frame video
  - Enables longer video generation with built-in windowing
  - *From: A.I.Warper*

- **Frame count for 3060 12GB**: 65 frames max at 1024x576
  - 81 frames causes OOM on second block
  - *From: mdkb*

- **Audio scale for InfiniteTalk**: 1.4 audio scale, 1.0 audio cfg
  - Good balance for lipsync without being crazy
  - *From: Charlie*

- **HuMO audio settings**: 1.0 audio scale, 2.5 audio cfg scale
  - Provides more lip action/expression
  - *From: mdkb*

- **Wan Animate steps and CFG**: 20 steps total (2x10), CFG 3.5, shift 8
  - Standard settings mentioned for 2.2 I2V FLF
  - *From: Lumifel*

- **LoRA training parameters**: 5e-5 learning rate, rank 32-64, 1200-1500 steps
  - Rank 64 for complex prompting, lower steps prevent overfitting
  - *From: Kytra*

- **Wan 2.2 MOE split ratio**: 0.875 or around 0.5
  - Official code reportedly uses around 0.5 split between high and low noise
  - *From: Draken*

- **CFG**: 1.0 with 8 steps
  - Works well with smooth mix model
  - *From: Juampab12*

- **Resolution**: 864x864
  - Good balance for testing
  - *From: Juampab12*

- **OVI VRAM usage**: 16.4GB steady, climbs to 19GB
  - With model_fp8_e4m3fn on 3090
  - *From: yukass*

- **Lightning LoRA settings**: High 2.5 strength, Low 2 strength, High shift 7.75, Low shift 9
  - Recommended configuration for quality results
  - *From: Juampab12*

- **Lightning LoRA steps**: DDIM beta 3 steps + Euler beta 3 steps (6 total)
  - Better than default 4 steps
  - *From: Juampab12*

- **New lightning sampler settings**: 3 sampler with 0.25 to 0.5 and 3CFG
  - Very nice results
  - *From: pom*

- **HuMo generation**: 50 iterations, 9.74s/it with model_fp8_e4m3fn.safetensors
  - Performance benchmark on RTX 3090
  - *From: yukass*

- **T2V steps**: 1+1 steps
  - Minimal steps needed for T2V generation
  - *From: hicho*

- **I2V steps**: 2+2 steps
  - Recommended for I2V generation
  - *From: hicho*

- **T2V with speed LoRAs**: 10 steps, 5 split
  - Testing configuration with speed LoRAs
  - *From: Dream Making*

- **I2V standard**: 20 steps, CFG 2.5
  - Standard I2V configuration
  - *From: Ryzen*

- **Resolution multiples**: 64 or 128
  - Prevents black output, ensures video token number divisible by 128
  - *From: GalaxyTimeMachine (RTX4090)*

- **Shift parameter**: 5 for WanAnimate, 5-8 for Wan 2.2
  - Controls noise distribution per timestep
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Lightning LoRA strength**: 0.7 with CFG 1.4
  - For optimal quality in low-noise phase
  - *From: Lan8mark*

- **Steps for Lightning LoRA**: 3 steps low noise, 6 total with 3 split
  - Optimal balance for quality and speed
  - *From: Lan8mark*

- **VAE selection**: Wan 2.2 VAE only for 5B model, 14B uses 2.1 VAE
  - Model-specific VAE compatibility
  - *From: Charlie*

- **Shift and split point coordination**: Must adjust shift while accounting for split point - original suggested values are shift 8 for high noise, shift 1 for low noise
  - Foundation for all other parameter tweaks
  - *From: Lan8mark*

- **High-noise sampler for quality**: Euler, shift 12, 30 steps total (19 steps on high)
  - Produces very good results but takes 34 minutes
  - *From: flo1331*

- **Denoise strength for low-noise**: 0.2 to 0.4
  - Manual calibration in this range finds ideal detail level
  - *From: Lan8mark*

- **Steps for WAN generation**: 8 steps total: 5 at 384p, 3 at full 720p
  - Optimal balance of speed and quality
  - *From: Lan8mark*

- **Frame count for controlled cases**: 77 frames
  - Works well with most looping method, used to be 81
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Maximum stable frames on 1 GPU**: 301 frames
  - Pretty stable on 1 GPU, you can go higher in 4 H100
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Triton Windows installation**: pip install -U 'triton-windows<3.5'
  - For Windows speed improvements
  - *From: Shadows*

- **rCM LoRA steps**: 4 steps with dpm++_sde
  - Original rCM has specific scheduler requirements
  - *From: Kijai*

- **rCM LoRA strength**: Bump up the strength a bit
  - Need higher strength to match full model performance
  - *From: Kijai*

- **Shift parameter for dual models**: Raise shift to 11
  - Makes step point change so it stays on HN and works more on structure
  - *From: mdkb*

- **Steps for OVI**: 50 steps
  - Better lip-sync quality and overall results
  - *From: tarn59*

- **Resolution for WAN t2v testing**: 544x544
  - Higher resolutions cause static artifacts
  - *From: U̷r̷a̷b̷e̷w̷e̷*

- **Steps for OVI testing**: 25 steps
  - Good for testing and experimentation
  - *From: U̷r̷a̷b̷e̷w̷e̷*

- **Reserve VRAM with 5090**: 6GB
  - Needed even with high-end GPU
  - *From: Juampab12*

- **OVI generation settings**: 960x512, 20 steps
  - Base settings, 50 steps and 1280x720 for better quality
  - *From: Drommer-Kille*

- **Wan 2.2 stock settings**: 5.5 shift, 1 CFG, 8 steps 4 split
  - Default configuration for Wan 2.2
  - *From: Dream Making*

- **CFG for face closeups**: 5+5 CFG 3
  - Good for closeup face generation
  - *From: hicho*

- **Low noise CFG**: 2.5 instead of 3.5
  - Prevents face degradation on low noise model
  - *From: Lumifel*

- **Power limit for 5090 stability**: 70%
  - Increases stability for problematic 5090 cards
  - *From: seitanism*

- **Lightx2v LoRA strength**: 1.0 on both high and low
  - Recommended starting point
  - *From: Elvaxorn*

- **Steps for new Lightx2v to avoid ghosting**: 6x6 steps minimum, 12 steps for LoRA
  - Lower steps cause severe ghosting
  - *From: Zabo*

- **Scheduler for new Lightx2v**: Linear quadratic instead of simple
  - Simple scheduler causes ghosting issues
  - *From: FL13*

- **CFG fall ratio**: 50% of steps
  - Default hardcoded value in ComfyUI for CFG dropping
  - *From: Kijai*

- **New Light MoE High LoRA strength**: 3.00
  - Provides lots more motion compared to previous setups
  - *From: phazei*

- **Linear quadratic scheduler**: Most reliable
  - Most reliable scheduler when using new LoRA
  - *From: FL13*

- **Low step training resolution**: 256x256
  - Trick to avoid OOM on 5090 when using 81 frames for video training
  - *From: Drommer-Kille*

- **Native workflow steps**: 6 steps (3+3)
  - Less slow motion effect than 4 steps with CFG 1
  - *From: Vérole*

- **FlashVSR sharpness**: Change to 11 for less sharp results
  - Default setting is very sharp
  - *From: yi*

- **CFG for multi-sampler without lighting LoRAs**: CFG 3.5 on high, 2.5 on low, 20 steps total
  - Balanced quality and motion
  - *From: Lumifel*

- **TaylorSeer usage**: Use Lite version
  - Standard version will cause OOM
  - *From: yi*

- **Model sampling shift**: 5 or 8 for Wan (not 7)
  - Standard values used by community, affects sigma computation
  - *From: Lodis*

- **FlashVSR denoise**: 0.75
  - Reduces over-sharpness while providing 20% speed increase
  - *From: Elvaxorn*

- **Lightning LoRA strength**: Not -4.75 (user error)
  - Incorrect negative values cause generation issues
  - *From: topmass*

- **CineScale RoPE scaling**: 1, 20, 20 then 1, 25, 25
  - Prevents repeat effect at larger resolutions
  - *From: DawnII*

- **New distill models**: 4 steps total, 2 high noise + 2 low noise, cfg 1, shift 5
  - Recommended configuration for 4-step distill
  - *From: aikitoria*

- **VAE encoding**: fp32
  - Workaround for torch 2.9.0/2.10 VRAM bug
  - *From: Charlie*

- **VACE frame count**: 25-81 frames optimal
  - Best quality and temporal consistency, follows 4n+1 formula
  - *From: Dever*

- **rcm LoRA strength**: 4.0 on high noise with WAN 2.2
  - Works well for speed with rank148 version, though lower strengths like 1.0 work better for some users
  - *From: aipmaster*

- **FlashVSR upscale ratio**: At least 2x, preferably 4x
  - Less than 2x produces poor quality especially for faces
  - *From: Kijai*

- **Lightning 2.2 I2V strength**: 0.5 on high noise
  - Good I2V results when paired with lightx2v i2v 480p rank 256 at 1.0 on low
  - *From: Persoon*

- **Shift parameter for rcm workflow**: 7
  - Used in successful rcm + lightning combination workflow
  - *From: aipmaster*

- **Blockswap**: 35 (increased from 25)
  - Required more after ComfyUI update for 1120x704 97 frames
  - *From: phazei*

- **FlashVSR strength**: 0.8
  - Effective for fixing bad renders without over-processing
  - *From: mdkb*

- **rCM steps**: 4 steps
  - Used in official examples, 1 step not actually demonstrated
  - *From: Kijai*

- **Clownshark sigma shift**: 4-10 range
  - 4 for static scenes, up to 10 for more dynamic content
  - *From: Kinasato*

- **Sliding window frames**: 8
  - Used with temporal mask setup
  - *From: TK_999*

- **Region bleed**: 0.2
  - Used with temporal mask configuration
  - *From: TK_999*

- **High noise LoRA strength**: 1.7
  - For 2Steps Lightx MoE
  - *From: Canin17*

- **Low noise LoRA strength**: 1.5
  - For 2Steps rCM
  - *From: Canin17*

- **CFG for first sampler**: 3.5
  - Used with no LoRA in 3-sampler native setup
  - *From: FL13*

- **Scheduler recommendation**: Euler with linear quadratic
  - Used across all samplers in FL13's workflow
  - *From: FL13*

- **cfg**: 2.0 on first step only
  - Provides good motion with minimal complexity
  - *From: Kijai*

- **Ditto Global LoRA strength**: 1.2 with lightx t2v adaptive at 1
  - Good balance for style transfer
  - *From: DawnII*

- **High/Low model split**: 6 steps split in middle, first step cfg 2.0
  - lightx2v lora at 3.0 strength high, 1.0 strength low
  - *From: Kijai*

- **Krea LoRA strength**: 3.6+ on high model
  - Going lower than 3.6 on high doesn't work well
  - *From: aipmaster*

- **Krea LoRA strength**: 4 on HN and 1.1 on LN with HPS at 0.75
  - To reduce noise when using on Wan 2.2
  - *From: aipmaster*

- **Shift value for I2V**: Target 0.9 sigma at split
  - High noise model meant to operate on high sigmas, default 0.9 for I2V
  - *From: seitanism*

- **Shift value for T2V**: Target 0.875 sigma at split
  - Default sigma value for T2V workflows
  - *From: Kijai*

- **Shift value minimum**: At least 16 (double from 8)
  - To prevent high sampler from adding too much noise
  - *From: Kijai*

- **MoCha VRAM usage with fp8**: 11GB at default resolution
  - Makes it feasible on mid-range GPUs
  - *From: Kijai*

- **Krea generation time**: 140 seconds for 140 seconds 720p
  - Real-time generation capability on 4090
  - *From: aipmaster*

- **HPS strength adjustment**: Bump up if output too noisy
  - Controls image quality vs noise trade-off
  - *From: aipmaster*

- **--reserve-vram**: 2
  - To offload more VRAM when using monitor on same GPU
  - *From: Kijai*

- **New LightX2V LoRA strength**: 1.0
  - Works well for complex prompts that failed on older versions
  - *From: Ada*

- **Step split for lightx2v LoRA**: 2+2 or 3+3
  - Most reasonable split for 4 total steps, 3+3 gives better image quality
  - *From: Ablejones*

- **SVI padding configuration**: Padding -1 for shot, 0 for film
  - Shot uses reference image padding, film uses zero padding
  - *From: Kijai*

- **Shift values for low step count**: Higher shift (like 11) for very low steps (1 step)
  - The less steps the more shift needed
  - *From: Ada*

- **SVI film frames**: 5 frames from end
  - Optimal for motion continuity between generations
  - *From: Kijai*

- **Ditto character LoRA strength**: 2.0
  - Better character likeness and recognition
  - *From: Drommer-Kille*

- **WSL memory allocation**: memory=60GB, swap=60GB
  - Prevent OOM issues in WSL environment
  - *From: seitanism*

- **LightX2V usage**: 3 low noise steps with LoRA vs 25 without
  - Better quality results with fewer steps when using speed LoRA
  - *From: seitanism*

- **SVI LoRA strength**: High: 3, Low: 1 for Wan 2.2
  - Working configuration for SVI with Wan 2.2
  - *From: Vérole*

- **Anisora 3.2 distill CFG**: CFG 1
  - Distilled model designed to work with CFG 1, higher values don't impact much
  - *From: DawnII*

- **FlashVSR attention**: Sage attention instead of SDPA
  - Prevents OOM errors
  - *From: patientx*

- **Block swap configuration**: 8 normal blocks, 3 VACE blocks
  - Good balance for VRAM management
  - *From: Kijai*

- **InfiniteTalk steps with LightX2V**: 4 steps
  - Avoid extremely long generation times (6+ hours)
  - *From: seitanism*

- **InfiniteTalk CFG with LightX2V**: 1
  - Works with the 4-step acceleration
  - *From: seitanism*

- **SVI ref_pad_num in film mode**: 0
  - No special padding applied when set to 0
  - *From: Kijai*

- **Steps for SVI with distill**: 8 steps with lightx2v
  - Works for quick testing
  - *From: Kijai*

- **Steps for non-distill SVI**: 40 steps
  - Better quality but painfully slow
  - *From: Kijai*

- **CFG for SVI**: 5.0
  - Used in testing
  - *From: Kijai*

- **Resolution for long generations**: 960x540
  - Needed for VRAM handling of 245 frames with full blockswap
  - *From: Hashu*

- **Steps with distill lora**: 8 steps, euler
  - For 1 minute generation efficiency
  - *From: Kijai*

- **Steps without distill**: 30 steps, 3.5 cfg
  - For quality testing
  - *From: Ablejones*

- **svi-shot mask setup**: 1 black mask frame and 80 white mask frames in wrapper
  - Proper masking for shot lora
  - *From: Ablejones*

- **HoloCine generation**: 720x720x241 frames, 3 high 3 low steps with lightx2v lora
  - Achieves 15-second generation in one pass
  - *From: seitanism*

- **Split attention experimental**: Avoid using on first step (0) as it's too strong
  - Works with 2.2 because low noise fixes it, but first step makes it too strong
  - *From: Kijai*

- **HoloCine sparse model**: 30.5GB VRAM with 20 blockswap for 281 frames at 832x480
  - Enables minute-long video generation
  - *From: mamad8*

- **LightX LoRA strength**: High 3.0, Low 1.0
  - Optimal balance for quality
  - *From: avataraim*

- **Swap block**: 40
  - For 30 second generation on RTX 4090
  - *From: avataraim*

- **Video attention split**: 0
  - For experimental Holocine workflow
  - *From: avataraim*

- **Denoise for scene differentiation**: 0.9 or 0.95
  - Forces high noise model to differentiate scenes
  - *From: mamad8*

- **HoloCine generation parameters**: num_frames=241, shot_cut_frames=[37, 77, 117, 157, 197]
  - For 15-second videos with proper scene transitions
  - *From: BNP4535353*

- **LongCat CFG**: cfg 4.0 for 30 steps or cfg 1.0 for 15 steps with distill LoRA
  - Balanced quality and speed
  - *From: Kijai*

- **Ovi resolution hack**: 512x512 at 25 steps
  - Faster generation, changed area calculations in ovi_fusion_engine.py
  - *From: reallybigname*

- **LongCat distill schedule**: 1000.0000, 994.7090, 988.7640, 982.0360, 974.3589, 965.5172, 955.2239, 943.0895, 923.0769, 904.1096, 880.3089, 849.5575, 808.2901, 750.0000, 661.4174, 510.6383
  - Custom schedule for longcat_distill_euler sampler
  - *From: Kijai*

- **Holocine shot cuts**: 41,81,121,161,201 or 50,100,150,200,250
  - Frame cut points for multi-shot generation
  - *From: shaggss*

- **LightX2V LoRA strength**: 1
  - For both high and low noise models with Holocine
  - *From: NebSH*

- **LongCat steps with distill LoRA**: 16 steps
  - Default with distill LoRA, 30+ steps needed without it
  - *From: Kijai*

- **LongCat quality/speed balance**: 10 steps
  - Good balance between quality and generation time
  - *From: avataraim*

- **LongCat fps setting**: 15 fps
  - Native generation rate, interpolates well to 30fps
  - *From: Kijai*

- **Video combine node for LongCat**: 15
  - To reflect original code implementation
  - *From: Kijai*

- **LongCat extension frames**: 17 frames minimum
  - Follows 4+1 rule, 16 wouldn't work properly
  - *From: Kijai*

- **LongCat refinement steps**: 50 steps with timestep threshold 500
  - Only runs steps under threshold, results in about 4 actual steps
  - *From: Kijai*

- **WanAnimate original settings**: shift=5.0, steps=20, guide_scale=1.0, solver=dpm++
  - Default settings from original implementation
  - *From: Mads Hagbarth Damsbo*

- **LongCat refinement lora strength**: 0.6 recommended
  - Full strength (1.0) creates noisy texture, 0.6 provides better balance
  - *From: Kijai*

- **NeatVideo denoising**: Enable temporal, set spatial to low weight or disabled
  - Preserves detail while removing VAE noise
  - *From: spacepxl*

- **Holocine CFG**: 1.0
  - Higher CFG values cause structured prompt errors
  - *From: NebSH*

- **Smooth windows token sharing**: 1-12 range
  - Controls information passed between shots for consistency
  - *From: NebSH*

- **LongCat LoRA strength**: 1.0
  - Works better at full strength with specific sampling setup
  - *From: Kijai*

- **LongCat sampling**: 50 steps, start step 45, Euler or UniPC, CFG 1.0
  - Optimal parameters for LongCat refinement
  - *From: Kijai*

- **WAN low refine**: Shift 1, denoise 0.2-0.3, 8-10 steps, CFG 3-5
  - For refining generated images without distill LoRA
  - *From: spacepxl*

- **OVI generation length**: 8 seconds maximum
  - 10 second limit exists, 15 seconds fails
  - *From: avataraim*

- **--cache-none flag**: enabled
  - Prevents RAM reservation, never reserves that RAM
  - *From: Kijai*

- **Batch size for LoRA training**: 16 or more
  - To remedy cases where WAN picks one category and maxes that out
  - *From: Kiwv*

- **LongCat steps**: 10-16 steps minimum with distill LoRA
  - Balance between quality and generation time
  - *From: Kijai*

- **LongCat T2V distill LoRA**: 1.0 strength with shift 11
  - Provides good quality without major degradation
  - *From: Pandaabear*

- **Morph LoRA strength**: 0.5 (official) or 3.0-4.0 for visible effects
  - Official recommendation vs observed effectiveness
  - *From: Kijai*

- **Steps for acceptable T2V quality**: 6-7 steps minimum
  - Below 5 causes massive lighting smoothness issues and blurriness
  - *From: Pandaabear*

- **New LightX2V 1030 LoRA**: LoRA strength 1.0, CFG 1.0, 6 steps without CFG
  - Optimized settings for the improved 1030 model
  - *From: Kijai*

- **Torch compile alternative startup args**: --reserve-vram 2 --max-upload-size 500 --fast pinned_memory --async-offload --use-sage-attention --fast fp16_accumulation
  - Avoids VRAM issues while maintaining decent performance
  - *From: Gleb Tretyak*

- **VACE generation settings**: 20 steps, CFG 2.5, SDPA attention
  - Balanced quality and performance settings
  - *From: Lumifel*

- **ChronoEdit defaults**: 8 steps, cfg 1.0 with distill lora, shift 2.0
  - Official recommended settings
  - *From: Kijai*

- **LightX2V 1030 usage**: Plain 4+4 euler simple, no CFG
  - Adding CFG steps results in trash results
  - *From: Gleb Tretyak*

- **Anisora strength for cartoons**: 0.5
  - Works well for cartoon content
  - *From: Gleb Tretyak*

- **ChronoEdit scale_t**: 7.0 in latest version
  - Corrected from earlier 8.0 value
  - *From: comfy*

- **ChronoEdit frames**: 5 frames (normal) or 29 frames (temporal reasoning)
  - What it was trained on
  - *From: Kiwv*

- **wan2.2_lightx2v_1030 timing**: 170 secs for 1024x576 on 4090, 7 steps split at 4
  - Performance benchmark
  - *From: Atlas*

- **Qwen Edit steps**: 40 steps
  - Night and day different for sharpness compared to default
  - *From: aikitoria*

- **LightX LoRA steps**: 4 steps
  - Can generate 5-second segments efficiently
  - *From: aikitoria*

- **Blocks to swap**: 30 instead of 20
  - To prevent OOMs with new ComfyUI update
  - *From: aipmaster*


## Concepts Explained

- **Differential diffusion**: Thresholds non-binary masks per step so it blends better than normal latent inpaint
  - *From: Kijai*

- **High Noise vs Low Noise models**: High Noise better for prompt following, composition, and motion. Low Noise better for large inpainting tasks
  - *From: Ablejones*

- **Merged vs Unmerged LoRAs**: Merged LoRAs integrate weights into model (no VRAM hit, precision loss). Unmerged LoRAs use more VRAM but maintain base precision and allow runtime adjustment
  - *From: Kijai*

- **VACE inpainting**: Model feature for inpainting that can be combined with other inpainting techniques
  - *From: Kijai*

- **Palingenesis**: Term meaning 'rebirth' or 'regeneration', refers to merging distill loras into base model
  - *From: Tony(5090)*

- **SA-ODE sampler**: Adams-Bashforth method from 1883, provides decent performance but with CFG burn effects
  - *From: mallardgazellegoosewildcat*

- **Second order lang dynamics**: Advanced sampling technique in LanPaint, most powerful sampler feature
  - *From: mallardgazellegoosewildcat*

- **Generative upscaler**: Essentially img2img processing, can be server-based or local
  - *From: mallardgazellegoosewildcat*

- **Prompt distribution sampling**: Your prompt sets up the distribution that the sampler is sampling from - better to have a better distribution
  - *From: mallardgazellegoosewildcat*

- **ComfyUI as shared inference engine**: ComfyUI seen as a common language for projects to interact, with lots of different projects being compatible
  - *From: mallardgazellegoosewildcat*

- **Blockswapping in AI Toolkit**: Sends 40 blocks to CPU during training to reduce VRAM usage
  - *From: Ryzen*

- **High/Low noise expert split**: MoE architecture in Wan 2.2 with separate experts for different noise levels
  - *From: mdkb*

- **PUSA purpose**: Allows T2V model to do I2V with minimal training cost, use with flowmatch_pusa scheduler and Pusa Noise node
  - *From: JohnDopamine*

- **Wan 2.2 MOE architecture**: High/Low noise expert split with 5B hybrid model, uses different VAE than 14B version
  - *From: mallardgazellegoosewildcat*

- **OVI symmetric twin backbone**: Parallel audio and video branches with identical DiT architecture, video initialized from Wan 2.2 5B
  - *From: mallardgazellegoosewildcat*

- **FLF (First-Last-Frame)**: Video morphing technique using start and end frames, official FLF model available for 2.2
  - *From: Kijai*

- **VACE mask values**: Can use partial denoise with 50% white mask, or spatially varying non-uniform masks for selective diffusion
  - *From: spacemathapocalypse*

- **NAG node**: Makes negative prompt work with 1.0 CFG, though may not work with base ComfyUI nodes for WAN
  - *From: Kytra*

- **Context windows with | split**: Single | in text encoder allows different prompts for different windows of context
  - *From: Kijai*

- **Self-Forcing/Rolling Forcing methods**: New method by ByteDance for real-time generation, trades quality for speed
  - *From: ericxtang*

- **Smooth Mix model behavior**: Model that exaggerates motion at lower fps for better frame interpolation results
  - *From: Rainsmellsnice*

- **Video token number**: Must be divisible by 128. Calculated as frame_size * num_frame. Different formulas for different model sizes
  - *From: GalaxyTimeMachine (RTX4090)*

- **Character Animation vs Character Replacement**: Character Animation uses reference image for background and character with video for motion. Character Replacement inserts character from reference into video background
  - *From: km*

- **Model distillation benefit**: Model distillation often improves quality, as seen with OVI improving visual quality of 5B model
  - *From: Juampab12*

- **Shift parameter**: Controls the amount of noise given per timestep - low shift does much at start and falls off, high shift does more for longer. Beginning timesteps give structure, later timesteps give detail
  - *From: Juampab12*

- **RMS norm function**: Normalization function where new native PyTorch version is much faster than custom Wan implementation, but changes output slightly
  - *From: Kijai*

- **Shift parameter**: Simply adjusts the sigmas in the sampling process - effect is complex but the mechanism is simple
  - *From: Kijai*

- **Sigma sweet spot**: Optimal noise levels for different phases of generation, important to keep steady when switching between high and low noise models
  - *From: Lan8mark*

- **OVI**: Video with audio generator based on Wan2.2 5B and MMAudio, open source kinda veo3
  - *From: Stad/Charlie*

- **Teacache**: Should not be doing much at 10 steps, threshold has to be pretty high to be culling 5 steps
  - *From: DawnII*

- **Latent upscaling vs pixel space upscaling**: What you're doing is running steps at lower res, then decoding into pixel space, upscaling in pixel space and encoding back to latents. Latent upscaling is when you upscale H and W in latent space
  - *From: shaggss*

- **Consistency Model**: A type of distillation that maps points on the trajectory of a parent model directly to finished output - finds shortcuts but needs existing trajectories from parent model
  - *From: mallardgazellegoosewildcat*

- **SDE Samplers**: Samplers that add noise during generation, can cause harm at low step counts
  - *From: mallardgazellegoosewildcat*

- **Scaled FP8**: Quantized model format that requires scaling to work properly, needs 'scaled_fp8' key in metadata
  - *From: Kijai*

- **V2 model versions**: V2 versions are for native node compatibility, not necessarily upgrades
  - *From: DawnII*

- **Temporal mask**: Feature in WAN that allows masking across time for video generation control
  - *From: Kijai*

- **Block cache vs blockcache**: Setting blockcache to 0 can cause memory issues, bypassing entirely is better
  - *From: lostintranslation*

- **SEC masking**: Enhancement for SAM2.1 that provides extra guidance for segmentation, still uses SAM but with better tracking
  - *From: Kijai*

- **RCM LoRA**: Distillation LoRA by Nvidia developers, alternative to lightx2v for speed without killing motion
  - *From: Elvaxorn*

- **TAE VAE**: Tiny VAE for preview purposes only, not suitable for final outputs due to quality loss
  - *From: Kijai*

- **fp8_scaled_e4m3fn vs e5m2**: e4m3fn uses 4 bits exponent, 3 bits mantissa - good balance. e5m2 uses 5 bits exponent, 2 bits mantissa - prioritizes dynamic range over precision
  - *From: Dever*

- **HN and LN**: High Noise and Low Noise models in the MoE architecture
  - *From: FL13*

- **CFG skimming**: Anti-CFG-burn tool that allows higher CFG on early steps then drops to prevent artifacts
  - *From: mallardgazellegoosewildcat*

- **CFG Zero Star**: Was for rectified flow DiTs in general using heuristic approximation, but might not be good for Wan 2.2
  - *From: mallardgazellegoosewildcat*

- **VACE**: Video control system that doesn't modify main model weights at all, only adds extra layers
  - *From: Kijai*

- **Simple consistency model distillation**: Distillation method that can be trained in a few hours, makes mappings from points on parent model path to finished output
  - *From: mallardgazellegoosewildcat*

- **Block sparse attention**: Sage version made for radial attention use, different from standard version
  - *From: Kijai*

- **Text encode cache**: Offloads prompt encoding cache to file, removes from memory after use, helps with OOM issues
  - *From: mdkb*

- **CFG scheduling**: Using different CFG values for each sampling step by providing a list of values
  - *From: Kijai*

- **Model sampling shift**: Parameter used to compute sigmas, affects model behavior - think of it as model creativity level
  - *From: 42hub*

- **Wan 2.2 MoE architecture**: Uses High/Low noise expert split with separate models for different noise levels
  - *From: Kijai*

- **RoPE scaling**: Scaling spatial rope to make larger resolutions work without repeat effect
  - *From: Kijai*

- **VACE frame inpainting**: Using entire frames as input/output masks to generate missing frames in the middle
  - *From: Koba*

- **Meta batch processing**: Using meta batch manager to handle long video processing in chunks
  - *From: happy.j*

- **MoE (Mixture of Experts)**: Architecture with High/Low noise expert split used in WAN 2.2, available as 5B hybrid model
  - *From: community context*

- **Block-Sparse Attention**: Optimization technique in FlashVSR that only works well on A100/A800 GPUs, causes quality degradation on consumer GPUs
  - *From: JohnDopamine*

- **RoPE frequency scaling**: Technique to prevent repetition artifacts at high resolutions, especially important for 1080p+ and high vertical resolutions
  - *From: Kijai*

- **High/Low noise expert split**: Wan 2.2 MoE architecture splits processing between high noise and low noise experts
  - *From: garbus*

- **Substep samplers**: Samplers that use multiple sub-steps within each main step for better convergence, underutilized but powerful
  - *From: Ablejones*

- **vid2vid with noise addition**: Process where you provide encoded latents, skip steps, add noise based on skipped sigmas, model continues from that point
  - *From: Kijai*

- **Temporal masks**: Masks that change over time for regional conditioning in video generation
  - *From: TK_999*

- **VACE**: Video control system that includes style transfer, inpainting, subject-driven, and outpainting capabilities
  - *From: context*

- **Ditto**: New VACE model with 3 modules (global_style, global, sim2real) for video style transfer tasks
  - *From: Kijai*

- **First frame VACE**: Putting image as first frame and freezing it, but Ditto isn't expecting this approach
  - *From: Draken*

- **sim2real capability**: Training model to map stylized videos back to their original real-world source videos
  - *From: ucren*

- **RGB control**: Direct video-to-video style transfer without needing pose estimation
  - *From: Draken*

- **Shift in sigma curve**: Shifts the sigma curve - high noise model meant to operate on high sigmas, modifies sigmas so high will cut off at proper point
  - *From: Kijai*

- **MoE architecture noise handling**: End of high sampler supposed to have leftover noise before passing to low noise - that's how MoE arch works
  - *From: DawnII*

- **Self-Forcing technique**: Technique for converting regular video diffusion models into autoregressive models, used in Krea realtime
  - *From: Dever*

- **Frame dimension concatenation**: MoCha concatenates control video with mask and reference in frame dimension, doubling VRAM usage
  - *From: Kijai*

- **Context windows for video**: Processing longer videos in chunks, each window contains noise + mask + ref
  - *From: Kijai*

- **Causal LoRA**: Krea LoRA is causal like CausVid, affecting temporal consistency
  - *From: Juampab12*

- **NAG (Negative Augmented Generation)**: Technique for better prompt adherence, negative should be simple and specific
  - *From: Kijai*

- **Model parameter sizing**: 1536 = 1.3B, 3072 = 5B, 5120 = 14B parameters based on patch_embedding weight dimensions
  - *From: Kijai*

- **SVI (Stable Video Infinity)**: Multiple I2V generations chained together rather than single generation, uses reference frames and special masking
  - *From: Kijai*

- **REPA training method**: End-to-end VAE training method that speeds up convergence and achieved SOTA ImageNet scores
  - *From: yi*

- **SVI padding mechanism**: Shot workflow sets padding to -1 to pad all frames with reference image instead of black pixels, film workflow uses 0 padding
  - *From: Kijai*

- **I2V conditioning channels**: 16 channels for noise, 16 for image conditioning, 4 for image conditioning mask. Image cond normally is start image + black pixels for rest, mask marks image as 1 and black pixels as 0
  - *From: Kijai*

- **SVI film LoRA**: LoRA that enables I2V model to work with multiple frames for video continuation
  - *From: Kijai*

- **Video-As-Prompt (VAP)**: In-context learning system that uses reference videos to guide generation style and motion
  - *From: JohnDopamine*

- **VACE patch embedding**: Specific model architecture component required for VACE functionality, missing in some model variants
  - *From: DawnII*

- **I2V channel mask**: 36 channels total: 16 for noise, 16 for I2V images, 4 for mask. Binary mask (1 for keep, 0 for generate) concatenated along channels
  - *From: Kijai*

- **SVI padding methods**: SVI-film uses zero padding (black frames), SVI-shot uses original input image padding for reference frames
  - *From: Kijai*

- **empty_frame_level in VACE**: Bias value interpreted by model, >0.5 makes frames lighter, <0.5 darker, but feeding values model wasn't trained on
  - *From: Ablejones*

- **Varlen attention**: Variable length attention mechanism that HoloCine requires, only supported by flash and sage attention methods
  - *From: Kijai*

- **Shot cut frames**: Frame numbers where you want cuts to happen in video generation, supported by some models
  - *From: BobbyD4AI*

- **Context window transitions**: Points where extended video segments join together, often prone to artifacts and ghosting
  - *From: blake37*

- **SVI Shot method**: Uses last frame as input with original image as reference in all other frames, only first frame masked. Doesn't continue motion but prevents degradation
  - *From: Kijai*

- **SVI Film method**: Uses 5 frames from last video, padded with black. Continues motion but can degrade over time
  - *From: Kijai*

- **Reference padding**: Filling non-masked frames with reference image to maintain consistency and reduce degradation
  - *From: Kijai*

- **SVI (Shot/Film) loras**: Special loras that enable multi-frame input and improve consistency. Film works with multiple frames, Shot works with single frame plus reference
  - *From: Kijai*

- **Reference padding**: Using previous frames as reference input to maintain consistency, only works with shot/talk/dance loras, not film
  - *From: Kijai*

- **Control embeds**: Padding with reference frames in the wrapper system
  - *From: scf*

- **HoloCine split attention**: Full method splits whole self attention (not just cross attention like | in prompts), includes RoPE stuff needed for longer generations
  - *From: Kijai*

- **Video latent first frame encoding**: VAE encodes single image to first latent, I2V only works with single image. Can't extract single image from latent containing 4 images without VAE
  - *From: Kijai*

- **Temporal and spatial compression**: Video latents use both temporal and spatial compression simultaneously, making latent manipulation complex
  - *From: Kijai*

- **Holocine prompt structure**: Uses global caption followed by per-shot captions separated by | and [shot cut] markers, should specify number of shots in global caption
  - *From: mamad8*

- **Video attention split**: Method to handle long video generation by splitting attention across video segments
  - *From: avataraim*

- **Multi-frame I2V extension**: LongCat feature allowing extension with motion continuity using 11 frame context
  - *From: aikitoria*

- **Sparse inter-shot self attention**: Holocine technique for handling transitions between shots
  - *From: mamad8*

- **HoloCine windowed attention**: Frames in shot(i) are masked to attend only to global caption and caption(i) so character description in global is visible to all shots
  - *From: shaggss*

- **SVI noise estimation**: Trying to estimate how much 'noise' or bad stuff is added in each pass and reverse it to prevent degradation
  - *From: Ablejones*

- **WAN VAE compression artifacts**: Too highly compressed so if there is sufficient detail in an area it dies, creating noise grids
  - *From: aikitoria*

- **LongCat TI2V**: Text-to-Image-to-Video model that combines T2V and I2V capabilities in single model
  - *From: slmonker*

- **Holocine shot attention**: System for multi-shot video generation with sparse_flash_attn, sparse_fallback, or full attention backends
  - *From: NebSH*

- **Bucket resolutions**: Predefined aspect ratios from 0.26 to 4.00 that LongCat expects for optimal performance
  - *From: Kijai*

- **LongCat architecture**: New foundational model trained from scratch, different from Wan but uses same CLIP/VAE, 14B model that can do both T2V and I2V
  - *From: Draken*

- **Distill LoRA**: Step and cfg distillation LoRA that allows using fewer steps (16 instead of 30+) and lower cfg
  - *From: Kijai*

- **Shot attention**: Feature requiring structured prompt metadata and text_cut_positions for HoloCine multi-shot generation
  - *From: Cubey*

- **Block sparse attention**: Efficiency mechanism in LongCat that's forced enabled when running refinement, requires flash attention implementation
  - *From: Kijai*

- **SVI film loras**: LoRAs with 'film' in name that use 5 start frames instead of 1 for better video continuity
  - *From: Kijai*

- **4+1 rule**: Frame count rule that LongCat follows for proper extension functionality
  - *From: Kijai*

- **R-RoPE (Reference Rotary Positional Encoding)**: Mechanism that shifts spatial dimensions of image conditions to distinct positions from video tokens
  - *From: Draken*

- **Causal convolutions in VAE**: Information carried forward between latent frames, need previous context to decode current frame but not future frames
  - *From: spacepxl*

- **LPIPS loss artifacts**: VGG network in LPIPS has strided convolutions with uneven overlap and max pool causing grid artifacts
  - *From: spacepxl*

- **Shot attention**: Requires structured prompt metadata and text_cut_positions for multi-shot video generation in Holocine
  - *From: NebSH*

- **Smooth window**: Parameter in Holocine that creates transition effects between different scenes, needs careful planning for scene transitions
  - *From: NebSH*

- **Vid2vid process**: Video extension method that starts at later steps, similar to really low denoise strength
  - *From: Kijai*

- **WAN training data limitations**: WAN is trained on like 30m videos, while training on 500m videos at 24fps to 121 frames could be close to SOTA
  - *From: Kiwv*

- **24fps-ifier LoRA concept**: Training a LoRA to make WAN work at 24fps for faster paced content that WAN currently can't handle
  - *From: Kiwv*

- **LongCat refinement LoRA**: Special LoRA trained on model's own outputs to upscale from 480p/15fps to 720p/30fps during inference
  - *From: JohnDopamine*

- **Wan-based architecture**: Uses Wan architecture but can be trained from scratch with modifications to model dimensions
  - *From: Draken*

- **Video continuation vs extension**: Continuation uses latents from previous frames, extension typically re-encodes through VAE
  - *From: aikitoria*

- **Trilinear interpolation in LongCat refinement**: 3-dimensional interpolation (spatial and temporal) used in the refinement LoRA, interpolating before sampling the 2nd stage
  - *From: Kijai*

- **Block swap prefetch optimization**: Method that gives zero speed loss by prefetching blocks, now includes LoRA data moving with block swap
  - *From: Kijai*

- **RGB space processing in refinement LoRA**: Sample 1st stage, decode to pixel/RGB space, upscale and interpolate, encode, then sample 2nd stage with low denoise
  - *From: Kijai*

- **Temporal reasoning tokens**: Intermediate frames in video generation that work like register tokens - model can put whatever it wants there as long as it helps reach the final result
  - *From: spacepxl*

- **ChronoEdit temporal reasoning mode**: Uses 29 frames for generation vs 5 frames normal, modifies input for specific steps, selects first and last frame
  - *From: Kijai*

- **LightX2V vs Lightning naming confusion**: LightX2V is team name, Lightning is different LoRA set. 2.1 LightX2V works with 2.2 low noise, 2.2 Lightning has exposure issues
  - *From: Kijai*

- **Context windows**: Feature that lets you do longer generations with multiple chunks of 81 frames sampled at once, preserves identity better than other extension techniques but can create transition artifacts
  - *From: blake37*

- **Temporal reasoning mode**: ChronoEdit's 29-frame mode vs normal 5-frame mode
  - *From: Kiwv*

- **Preview vs Full model releases**: Preview means beta/still being developed, once development is done they drop the preview word but it's the same model
  - *From: yi*

- **Autoregressive burn in**: Quality degradation that occurs when VACE extends videos autoregressively, causing color drift and coherence loss
  - *From: Benjaminimal*

- **Block swap for unmerged LoRAs**: Unmerged loras are now part of the block swap system, making it faster and avoiding issues, rather than being fully swapped out
  - *From: Kijai*


## Resources & Links

- **WanAnimate Preprocessor** (repo)
  - https://github.com/kijai/ComfyUI-WanAnimatePreprocess
  - *From: hudson223*

- **Wan Animate points editor tutorial** (tutorial)
  - https://www.youtube.com/watch?v=xlsfp4Y_jEo
  - *From: CaptHook*

- **KJNodes resize PR** (repo)
  - https://github.com/kijai/ComfyUI-KJNodes/pull/402
  - *From: stenandrimpy*

- **ComfyUI-Org Wan 2.2 Repackaged** (model)
  - https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/tree/main/split_files/diffusion_models
  - *From: JohnDopamine*

- **Kijai WanVideo fp8 scaled models** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy_fp8_scaled/tree/main/I2V
  - *From: Samy*

- **IntelligentVRAMNode** (tool)
  - https://github.com/eddyhhlure1Eddy/IntelligentVRAMNode
  - *From: ulvord*

- **Palingenesis model** (model)
  - https://huggingface.co/eddy1111111/WAN22.XX_Palingenesis/tree/main
  - *From: hicho*

- **LanPaint with Wan 2.2 support** (tool)
  - https://github.com/scraed/LanPaint
  - *From: s2k*

- **QWen VL Object Detection (modified)** (tool)
  - https://github.com/piscesbody/Comfyui_Object_Detect_QWen_VL
  - *From: piscesbody*

- **Ovi model weights** (model)
  - https://huggingface.co/chetwinlow1/Ovi/tree/main
  - *From: Rainsmellsnice*

- **DC-VideoGen paper** (paper)
  - https://www.reddit.com/r/StableDiffusion/comments/1nw9x83/dcvideogen_efficient_video_generation_with_deep
  - *From: Izaan*

- **WAN22.XX_Palingenesis** (model)
  - https://huggingface.co/eddy1111111/WAN22.XX_Palingenesis/tree/main
  - *From: Drommer-Kille*

- **Wan2.2-Lightning 4-step LoRA** (lora)
  - https://huggingface.co/lightx2v/Wan2.2-Lightning/tree/main/Wan2.2-T2V-A14B-4steps-lora-250928
  - *From: Drommer-Kille*

- **Ovi model** (model)
  - https://github.com/character-ai/Ovi
  - *From: Gateway {Dreaming Computers}*

- **VitPose ComfyUI** (tool)
  - https://huggingface.co/Kijai/vitpose_comfy/tree/main/onnx
  - *From: hicho*

- **YOLOv10 ONNX** (tool)
  - https://huggingface.co/onnx-community/YOLOv10/tree/main
  - *From: hicho*

- **Ovi HuggingFace** (model)
  - https://huggingface.co/chetwinlow1/Ovi/tree/main
  - *From: BecauseReasons*

- **Wanx Troopers documentation** (documentation)
  - https://wanx-troopers.github.io/
  - *From: 42hub*

- **Lightning LoRAs** (model)
  - https://huggingface.co/lightx2v/Wan2.2-Lightning/tree/main/Wan2.2-T2V-A14B-4steps-lora-250928
  - *From: pom*

- **ClownOptions Tile node** (node)
  - https://discord.com/channels/1076117621407223829/1386453178240733235/1423168728933204031
  - *From: xwsswww*

- **DC-VideoGen** (repo)
  - https://github.com/dc-ai-projects/DC-VideoGen
  - *From: Cubey*

- **ComfyUI Queue Manager** (tool)
  - https://github.com/QuietNoise/ComfyUI-Queue-Manager
  - *From: hudson223*

- **Ovi fp8 quantized** (model)
  - https://huggingface.co/rkfg/Ovi-fp8_quantized/tree/main
  - *From: Stad*

- **New 2.2 checkpoint** (model)
  - https://civitai.com/models/1995784?modelVersionId=2260110
  - *From: Ada*

- **OVI GitHub repository** (repo)
  - https://github.com/character-ai/Ovi/pull/11
  - *From: patientx*

- **OVI demo page** (demo)
  - https://aaxwaz.github.io/Ovi/
  - *From: Screeb*

- **ComfyUI-Upscale-CUDAspeed plugin** (tool)
  - https://github.com/piscesbody/ComfyUI-Upscale-CUDAspeed
  - *From: piscesbody*

- **Wan training Discord channel** (community)
  - https://discord.com/channels/1076117621407223829/1344309523187368046
  - *From: seitanism*

- **Smooth mix merge model** (model)
  - https://civitai.com/models/1995784?modelVersionId=2259006
  - *From: Juampab12*

- **WAN 2.2 Prompt Generator** (tool)
  - https://chatgpt.com/g/g-6887849e21b8819183e20c1dc6bcf353-wan-2-2-prompt-generator?model=gpt-4o
  - *From: ArtificialMachine*

- **Matrix bullet time recreation video** (tutorial)
  - https://www.youtube.com/watch?v=iq5JaG53dho
  - *From: Neex*

- **Smooth Mix Wan 2.2 I2V 14B** (model)
  - https://civitai.com/models/1995784/smooth-mix-wan-22-i2v-14b
  - *From: Juampab12*

- **Face/head swap workflow** (workflow)
  - https://civitai.com/articles/20190
  - *From: Alisson Pereira*

- **Wav2vec2 Chinese model for InfiniteTalk** (model)
  - *From: Dever*

- **Self-Forcing method discussion** (article)
  - https://www.reddit.com/r/StableDiffusion/comments/1nyxwe2/selfforcing_new_method_by_bytedance_built_upon/
  - *From: Dream Making*

- **Radial Length Helper** (tool)
  - https://github.com/Hud224/Radial_Length_Helper/tree/main
  - *From: hudson223*

- **WanAnimatePreprocess nodes** (repo)
  - https://github.com/kijai/ComfyUI-WanAnimatePreprocess
  - *From: Dream Making*

- **ComfyUI_RH_Ovi** (repo)
  - https://github.com/HM-RunningHub/ComfyUI_RH_Ovi
  - *From: slmonker(5090D 32GB)*

- **WanVideoWrapper** (repo)
  - https://github.com/kijai/ComfyUI-WanVideoWrapper
  - *From: Dream Making*

- **SmoothMix LoRA** (lora)
  - https://civitai.com/models/1995784?modelVersionId=2260110
  - *From: Dream Making*

- **OVI ComfyUI nodes** (repo)
  - https://github.com/HM-RunningHub/ComfyUI_RH_Ovi
  - *From: Lodis*

- **Lightning LoRA for Wan 2.2** (model)
  - https://huggingface.co/lightx2v/Wan2.2-Lightning/tree/main
  - *From: Dream Making*

- **RadialAttn for ComfyUI** (repo)
  - https://github.com/woct0rdho/ComfyUI-RadialAttn
  - *From: Kijai*

- **Palingenesis model** (model)
  - https://huggingface.co/eddy1111111/WAN22.XX_Palingenesis/tree/main
  - *From: phazei*

- **SpargeAttn package** (tool)
  - https://github.com/woct0rdho/SpargeAttn/releases
  - *From: Kijai*

- **Wan 2.2 5B Turbo models and LoRAs** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/tree/main/Wan22-Turbo
  - *From: crinklypaper*

- **MiniVeo3-Reasoner-Maze-5B** (model)
  - https://huggingface.co/thuml/MiniVeo3-Reasoner-Maze-5B
  - *From: DawnII*

- **Pruned WAN LoRAs collection** (model)
  - https://huggingface.co/woctordho/wan-lora-pruned/tree/main
  - *From: woctordho*

- **OVI models** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/tree/main/Ovi
  - *From: slmonker(5090D 32GB)*

- **AniSora LoRA** (lora)
  - https://huggingface.co/Kijai/WanVideo_comfy/blob/main/LoRAs/AniSora/Wan2_2_I2V_AniSora_3_2_HIGH_rank_64_fp16.safetensors
  - *From: Kijai*

- **CineScale** (repo)
  - https://github.com/Eyeline-Labs/CineScale
  - *From: Kijai*

- **FreeScale** (repo)
  - https://github.com/ali-vilab/FreeScale
  - *From: Kijai*

- **NN Latent Upscale** (repo)
  - https://github.com/Ttl/ComfyUi_NNLatentUpscale
  - *From: Kijai*

- **Latent upscale article** (workflow)
  - https://discord.com/channels/1076117621407223829/1425077677571838056
  - *From: Lan8mark*

- **Flux bokeh LoRA** (lora)
  - https://civitai.com/models/694867/fluxbokeh
  - *From: slmonker(5090D 32GB)*

- **Long video generation methods** (workflow)
  - https://discord.com/channels/1076117621407223829/1386453178240733235
  - *From: 42hub*

- **rCM LoRA for Wan** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/tree/main/LoRAs/rCM
  - *From: Kijai*

- **OVI branch of WanVideoWrapper** (repo)
  - https://github.com/kijai/ComfyUI-WanVideoWrapper/tree/ovi
  - *From: ˗ˏˋ⚡ˎˊ-*

- **SageAttention Windows release** (tool)
  - https://github.com/woct0rdho/SageAttention/releases/tag/v2.2.0-windows.post3
  - *From: Shadows*

- **ComfyUI acceleration helper** (tool)
  - https://github.com/loscrossos/helper_comfyUI_accel
  - *From: ▲*

- **WanMoeKSampler fork with fixes** (node)
  - https://github.com/GalaxyTimeMachine/ComfyUI-WanMoeKSampler
  - *From: GalaxyTimeMachine (RTX4090)*

- **Animal pose detection node** (node)
  - *From: happy.j*

- **Better segmentation for Wan Animate** (tool)
  - https://www.reddit.com/r/StableDiffusion/comments/1o2sves/contextaware_video_segmentation_for_comfyui_sec4b/
  - *From: Shubhooooo*

- **ComfyUI-Ovi repository** (repo)
  - https://github.com/snicolast/ComfyUI-Ovi
  - *From: Drommer-Kille*

- **MAGREF WAN 2.2 integration** (repo)
  - https://github.com/MAGREF-Video/MAGREF/issues/17#issuecomment-3387138859
  - *From: Elvaxorn*

- **ComfyUI-SecNodes** (repo)
  - https://github.com/9nate-drake/Comfyui-SecNodes
  - *From: Vérole*

- **HF CLI blog** (tool)
  - https://huggingface.co/blog/hf-cli
  - *From: happy.j*

- **HF transfer Rust tool** (tool)
  - https://github.com/huggingface/hf_transfer
  - *From: mallardgazellegoosewildcat*

- **ComfyUI Easy Install** (tool)
  - https://github.com/Tavris1/ComfyUI-Easy-Install
  - *From: Ada*

- **SageAttention Windows installer** (tool)
  - https://github.com/Justify87/Install-SageAttention-Windows-Comfyui
  - *From: Ada*

- **SAM 3 waitlist** (model)
  - https://ai.meta.com/sam3/
  - *From: Kijai*

- **SEC ComfyUI nodes** (node)
  - https://github.com/9nate-drake/Comfyui-SecNodes
  - *From: ArtOfficial*

- **SageAttention releases** (tool)
  - https://github.com/woct0rdho/SageAttention/releases
  - *From: ArtOfficial*

- **RCM LoRAs** (lora)
  - https://huggingface.co/Kijai/WanVideo_comfy/tree/main/LoRAs/rCM
  - *From: JohnDopamine*

- **WanVideoWrapper workflows** (workflow)
  - https://github.com/kijai/ComfyUI-WanVideoWrapper/tree/main/example_workflows
  - *From: FL13*

- **TAE VAE model** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/blob/main/taew2_2.safetensors
  - *From: cocktailprawn1212*

- **Wan 2.2 I2V Lightx2v full models** (model)
  - https://huggingface.co/lightx2v/Wan2.2-I2V-A14B-Moe-Distill-Lightx2v
  - *From: yi*

- **Kijai's extracted Lightx2v LoRA** (lora)
  - https://huggingface.co/Kijai/WanVideo_comfy/blob/main/LoRAs/Wan22_Lightx2v/Wan_2_2_I2V_A14B_HIGH_lightx2v_MoE_distill_lora_rank_64_bf16.safetensors
  - *From: Kijai*

- **WanMoE KSampler with CFG adjusting** (node)
  - https://github.com/GalaxyTimeMachine/ComfyUI-WanMoeKSampler
  - *From: Samy*

- **Skimmed CFG node pack** (node)
  - https://github.com/Extraltodeus/Skimmed_CFG
  - *From: mallardgazellegoosewildcat*

- **Kijai's extracted LightX2V High LoRA** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/tree/86ac564b7ca986760f04cb6e0b4e44b31059c9db/LoRAs/Wan22_Lightx2v
  - *From: JohnDopamine*

- **Pre-CFG ComfyUI nodes** (tool)
  - https://github.com/Extraltodeus/pre_cfg_comfy_nodes_for_ComfyUI
  - *From: mallardgazellegoosewildcat*

- **GIMM-VFI ComfyUI implementation** (tool)
  - https://github.com/kijai/ComfyUI-GIMM-VFI
  - *From: Colin*

- **FastVideo sliding window attention** (repo)
  - https://github.com/hao-ai-lab/FastVideo
  - *From: mallardgazellegoosewildcat*

- **StepVideo T2V** (repo)
  - https://github.com/stepfun-ai/Step-Video-T2V
  - *From: mallardgazellegoosewildcat*

- **FlashVSR paper** (repo)
  - https://zhuang2002.github.io/FlashVSR/
  - *From: yi*

- **Triton 3.5.0 with fp8 fixes** (tool)
  - https://github.com/woct0rdho/triton-windows/releases/tag/v3.5.0-windows.post21
  - *From: phazei*

- **Prebuilt Triton Windows wheels** (tool)
  - https://github.com/woct0rdho/triton-windows
  - *From: Kijai*

- **Prebuilt SageAttention Windows wheels** (tool)
  - https://github.com/woct0rdho/SageAttention
  - *From: Kijai*

- **TaylorSeer ComfyUI node** (node)
  - https://github.com/philipy1219/ComfyUI-TaylorSeer
  - *From: yi*

- **FlashVSR repository** (repo)
  - https://github.com/OpenImagingLab/FlashVSR
  - *From: yi*

- **Pusa Wan2.2 training dataset** (dataset)
  - https://huggingface.co/datasets/RaphaelLiu/PusaV1_training
  - *From: JohnDopamine*

- **Working PyTorch nightly build** (installation command)
  - pip3 install --pre -U torch==2.9.0.dev20250909+cu128 torchvision==0.24.0.dev20250905+cu128 torchaudio==2.8.0.dev20250912+cu128 --index-url https://download.pytorch.org/whl/nightly/cu128
  - *From: Kijai*

- **LoRA community tracking list** (resource list)
  - https://wanx-troopers.github.io/LoRA-alchemy.html
  - *From: 42hub*

- **Wan 2.2 VAE bf16** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/blob/main/Wan2_2_VAE_bf16.safetensors
  - *From: DawnII*

- **SeedVR2 block swapping guide** (workflow guide)
  - https://discord.com/channels/1076117621407223829/1393656203241979924/1393656203241979924
  - *From: JohnDopamine*

- **Wan2.2 4-step distill models** (model)
  - https://huggingface.co/lightx2v/Wan2.2-Distill-Models/tree/main
  - *From: ZeusZeus*

- **Wan2.2 distill LoRAs** (lora)
  - https://huggingface.co/lightx2v/Wan2.2-Distill-Loras/tree/main
  - *From: Dever*

- **Wan22-animate-v2 for e5m2** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy_fp8_scaled/blob/main/Wan22Animate/Wan2_2-Animate-14B_fp8_scaled_e5m2_KJ_v2.safetensors
  - *From: Koba*

- **VACE GGUF versions** (model)
  - https://huggingface.co/QuantStack/Wan2.2-VACE-Fun-A14B-GGUF/tree/main
  - *From: DawnII*

- **DimensionX** (repo)
  - https://github.com/wenqsun/DimensionX
  - *From: Kijai*

- **ComfyUI VideoUpscale** (tool)
  - https://github.com/ShmuelRonen/ComfyUI-VideoUpscale_WithModel
  - *From: dipstik*

- **FlashWorld project** (repo)
  - https://github.com/imlixinyang/FlashWorld
  - *From: happy.j*

- **rcm LoRA for WAN** (lora)
  - https://huggingface.co/Kijai/WanVideo_comfy/tree/main/LoRAs/rCM
  - *From: aipmaster*

- **CineScale LoRA** (lora)
  - https://huggingface.co/Kijai/WanVideo_comfy/tree/main/LoRAs/CineScale
  - *From: phazei*

- **WanAnimatePreprocess nodes** (repo)
  - https://github.com/kijai/ComfyUI-WanAnimatePreprocess
  - *From: Kijai*

- **UniMMVSR website** (model)
  - https://shiandu.github.io/UniMMVSR-website/
  - *From: Shubhooooo*

- **FlashVSR upscale workflow** (workflow)
  - https://github.com/kijai/ComfyUI-WanVideoWrapper/blob/main/example_workflows/wanvideo_1_3B_FlashVSR_upscale_example.json
  - *From: Govind Singh*

- **rCM 720p LoRA** (lora)
  - https://huggingface.co/Kijai/WanVideo_comfy/blob/main/LoRAs/rCM/Wan_2_1_T2V_14B_720p_rCM_lora_average_rank_94_bf16.safetensors
  - *From: Kijai*

- **rCM 480p LoRA** (lora)
  - https://huggingface.co/Kijai/WanVideo_comfy/blob/main/LoRAs/rCM/Wan_2_1_T2V_1_3B_480p_rCM_lora_average_rank_64_bf16.safetensors
  - *From: Kijai*

- **Wan 2.5 T2I at FAL** (model)
  - https://fal.ai/models/fal-ai/wan-25-preview/text-to-image
  - *From: Drommer-Kille*

- **ComfyUI HotReload fix** (tool)
  - https://github.com/kijai/ComfyUI-HotReloadHack
  - *From: Kijai*

- **InfiniteTalk example workflow** (workflow)
  - https://github.com/kijai/ComfyUI-WanVideoWrapper/blob/main/example_workflows/wanvideo_I2V_InfiniteTalk_example_03.json
  - *From: JohnDopamine*

- **Rapid AIO GGUF** (model)
  - https://huggingface.co/patientxtr/WAN2.2-14B-Rapid-AllInOne-GGUF/tree/main
  - *From: patientx*

- **Ditto LoRAs converted for ComfyUI** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/tree/main/LoRAs/Ditto
  - *From: Kijai*

- **Ditto GitHub repository** (repo)
  - https://github.com/EzioBy/Ditto
  - *From: Kijai*

- **Ditto models on HuggingFace** (model)
  - https://huggingface.co/QingyanBai/Ditto/tree/main/models_comfy
  - *From: Kijai*

- **Ditto dataset** (dataset)
  - https://huggingface.co/datasets/QingyanBai/Ditto-1M
  - *From: Dever*

- **Krea realtime video model** (model)
  - https://huggingface.co/krea/krea-realtime-video
  - *From: Desto Geima*

- **Ditto project page** (webpage)
  - https://editto.net/
  - *From: ucren*

- **Ditto GitHub repo** (repo)
  - https://github.com/EzioBy/Ditto
  - *From: Kijai*

- **Kijai's Ditto LoRAs** (lora)
  - https://huggingface.co/Kijai/WanVideo_comfy/tree/main/LoRAs/Ditto
  - *From: Govind Singh*

- **Sora watermark removal workflow** (workflow)
  - https://pastebin.com/LUq8Pjat
  - *From: rob*

- **Krea realtime LoRA extracted for Wan** (model)
  - https://huggingface.co/aipmaster/krea-lora/blob/main/Wan_2_1_T2V_14B_krea_realtime_rank256_bf16.safetensors
  - *From: aipmaster*

- **HPS LoRA for noise reduction** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/blob/main/LoRAs/Wan22_FunReward/Wan2.2-Fun-A14B-InP-LOW-HPS2.1_resized_dynamic_avg_rank_15_bf16.safetensors
  - *From: aipmaster*

- **MUG-V 10B video model** (model)
  - https://github.com/Shopee-MUG/MUG-V
  - *From: yi*

- **WoW world model** (model)
  - https://huggingface.co/WoW-world-model/WoW-1-Wan-14B-600k/tree/main
  - *From: asd*

- **MoCha model files** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy_fp8_scaled/tree/main/MoCha
  - *From: CJ*

- **Ditto dataset mini test** (dataset)
  - https://huggingface.co/datasets/QingyanBai/Ditto-1M/tree/main/mini_test_videos
  - *From: hicho*

- **MoCha model** (model)
  - https://orange-3dv-team.github.io/MoCha/
  - *From: Dever*

- **Krea realtime video model** (model)
  - https://huggingface.co/krea/krea-realtime-video
  - *From: s2k*

- **Krea LoRA** (lora)
  - https://huggingface.co/aipmaster/krea-lora/tree/main
  - *From: Dever*

- **Rolling Forcing** (model)
  - https://huggingface.co/TencentARC/RollingForcing
  - *From: JohnDopamine*

- **Updated Wan 2.2 Distill LoRAs** (lora)
  - https://huggingface.co/lightx2v/Wan2.2-Distill-Loras/tree/main
  - *From: Gateway {Dreaming Computers}*

- **ReferEverything** (repo)
  - https://github.com/miccooper9/ReferEverything
  - *From: JohnDopamine*

- **Kaleido reference to video** (repo)
  - https://github.com/CriliasMiller/Kaleido-OpenSourced
  - *From: yi*

- **QwenImage VAE ComfyUI format** (model)
  - https://huggingface.co/Kijai/QwenImage_experimental/blob/main/e2e-qwenimage-vae_comfy_fp32.safetensors
  - *From: Kijai*

- **Rolling Force model** (model)
  - https://huggingface.co/TencentARC/RollingForcing/tree/main
  - *From: yi*

- **New LightX2V LoRAs** (lora)
  - https://huggingface.co/lightx2v/Wan2.2-Distill-Loras/tree/main
  - *From: Ada*

- **Stable Video Infinity** (repo)
  - https://github.com/vita-epfl/Stable-Video-Infinity
  - *From: Kijai*

- **ComfyUI wheels for Triton** (tool)
  - https://github.com/Comfy-Org/wheels/actions/runs/17170280663
  - *From: justinj*

- **TREAD training method** (repo)
  - https://arxiv.org/abs/2501.04765
  - *From: yi*

- **End-to-end VAE paper** (repo)
  - https://arxiv.org/pdf/2504.10483
  - *From: mamad8*

- **New lightx2v LoRA** (model)
  - https://huggingface.co/lightx2v/Wan2.2-Distill-Loras/blob/main/wan2.2_i2v_A14b_high_noise_lora_rank64_lightx2v_4step_1022.safetensors
  - *From: Kijai*

- **SVI model repository** (model)
  - https://huggingface.co/vita-video-gen/svi-model/tree/main/version-1.0
  - *From: Kijai*

- **VHS Video Helper Suite** (tool)
  - https://github.com/Kosinkadink/ComfyUI-VideoHelperSuite
  - *From: Kijai*

- **SVI examples and homepage** (repo)
  - https://stable-video-infinity.github.io/homepage/
  - *From: Dever*

- **Qwen next-scene LoRA v2** (model)
  - https://huggingface.co/lovis93/next-scene-qwen-image-lora-2509
  - *From: Dever*

- **SVI LoRA models** (model)
  - https://huggingface.co/vita-video-gen/svi-model
  - *From: garbus*

- **Video-As-Prompt repository** (repo)
  - https://github.com/bytedance/Video-As-Prompt
  - *From: JohnDopamine*

- **VAP HuggingFace models** (model)
  - https://huggingface.co/ByteDance/Video-As-Prompt-Wan2.1-14B/tree/main
  - *From: JohnDopamine*

- **LightX2V Autoencoders** (model)
  - https://huggingface.co/lightx2v/Autoencoders/tree/main
  - *From: JohnDopamine*

- **Ditto models** (model)
  - https://huggingface.co/QingyanBai/Ditto_models/tree/main
  - *From: Gentleman bunny*

- **Wan community knowledge base** (tool)
  - https://nathanshipley.notion.site/Wan-2-1-Knowledge-Base-1d691e115364814fa9d4e27694e9468f
  - *From: JohnDopamine*

- **Wanx Troopers updates** (tool)
  - https://wanx-troopers.github.io/
  - *From: JohnDopamine*

- **SVI LoRAs converted for ComfyUI native** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/tree/main/LoRAs/Stable-Video-Infinity
  - *From: Kijai*

- **SVI film LoRA fp16** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/blob/main/LoRAs/Stable-Video-Infinity/svi-film_lora_rank_128_fp16.safetensors
  - *From: Kijai*

- **Video-as-Prompt paper** (research)
  - openreview.net/pdf/8171590dbc3bf6b0150a5d8db4e4e66286b2d4c9.pdf
  - *From: Prelifik*

- **LTX 2 playground** (tool)
  - https://app.ltx.studio/ltx-2-playground/t2v
  - *From: yi*

- **Custom mask input node for native ComfyUI** (node)
  - *From: Ablejones*

- **HoloCine fp8 weights** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy_fp8_scaled/tree/main/T2V/HoloCine
  - *From: Kijai*

- **HoloCine official demo site** (demo)
  - https://holo-cine.github.io/
  - *From: VK (5080 128gb)*

- **WanX Troopers timeline and LoRA tracking** (documentation)
  - https://wanx-troopers.github.io/timeline.html
  - *From: 42hub*

- **SVI models via Kijai** (model)
  - https://huggingface.co/vita-video-gen/svi-model
  - *From: JohnDopamine*

- **Aquif-Dream-6B-Exp alternative to Ovi** (model)
  - https://huggingface.co/aquif-ai/aquif-Dream-6B-Exp
  - *From: DawnII*

- **HoloCine** (repo)
  - https://github.com/yihao-meng/HoloCine
  - *From: slmonker(5090D 32GB)*

- **HoloCine sparse model** (model)
  - https://huggingface.co/hlwang06/HoloCine/tree/main/HoloCine_dit/sparse
  - *From: NebSH*

- **UniLumos model** (model)
  - https://huggingface.co/Alibaba-DAMO-Academy/UniLumos/tree/main
  - *From: DawnII*

- **Multitalk + unianimate workflow example** (workflow)
  - https://www.reddit.com/r/comfyui/comments/1lsb5a1/testing_wan_21_multitalk_unianimate_lora_kijai/
  - *From: Shubhooooo*

- **Film SVI workflow** (workflow)
  - https://discord.com/channels/1076117621407223829/1342763350815277067/1431178558205726842
  - *From: VK (5080 128gb)*

- **OpenModelDB for upscaling** (resource)
  - https://openmodeldb.info/
  - *From: Dever*

- **HoloCine fp8 models** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy_fp8_scaled/tree/main/T2V/HoloCine
  - *From: seitanism*

- **SVI training script with dataset** (repo)
  - https://github.com/vita-epfl/Stable-Video-Infinity/blob/main/scripts/train/svi_film.sh
  - *From: Ablejones*

- **SD-Latent-Interposer** (tool)
  - https://github.com/city96/SD-Latent-Interposer
  - *From: Kijai*

- **SVI film workflow for 2.2** (workflow)
  - https://discord.com/channels/1076117621407223829/1396263390296674324/1431508434431246336
  - *From: DawnII*

- **LongCat-Video** (model)
  - https://huggingface.co/meituan-longcat/LongCat-Video
  - *From: yi*

- **LongCat technical report** (documentation)
  - https://github.com/meituan-longcat/LongCat-Video/blob/main/longcatvideo_tech_report.pdf
  - *From: yi*

- **Holocine FP8 models** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy_fp8_scaled/tree/main/T2V/HoloCine
  - *From: avataraim*

- **NotebookLLM with scraped messages** (tool)
  - https://notebooklm.google.com/notebook/a08901b9-0511-4926-bbf8-3c86a12dc306
  - *From: Karo*

- **HoloCine fp8 models** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy_fp8_scaled/tree/main/T2V/HoloCine
  - *From: avataraim*

- **UltraGen 4K video generation** (repo)
  - https://github.com/sjtuplayer/UltraGen/
  - *From: Shubhooooo*

- **Inpaint4Drag** (tool)
  - https://github.com/Visual-AI/Inpaint4Drag
  - *From: ulvord*

- **LongCat discussion thread** (repo)
  - https://github.com/meituan-longcat/LongCat-Video/issues/4#issuecomment-3448130131
  - *From: DawnII*

- **LongCat ComfyUI models** (model)
  - https://huggingface.co/Kijai/LongCat-Video_comfy/tree/main
  - *From: Kijai*

- **LongCat testing branch** (repo)
  - https://github.com/kijai/ComfyUI-WanVideoWrapper/tree/longcat
  - *From: Kijai*

- **LongCat test image** (resource)
  - https://github.com/meituan-longcat/LongCat-Video/blob/main/assets/girl.png
  - *From: Kijai*

- **Holocine nodes implementation** (repo)
  - https://github.com/Dango233/ComfyUI-WanVideoWrapper/tree/main
  - *From: shaggss*

- **Holocine FP8 models** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy_fp8_scaled/tree/main/T2V/HoloCine
  - *From: Shubhooooo*

- **LongCat testing workflow** (workflow)
  - https://github.com/kijai/ComfyUI-WanVideoWrapper/blob/longcat/LongCat/longcat_i2v_testing.json
  - *From: JohnDopamine*

- **SageAttention 2.2.0** (repo)
  - https://github.com/woct0rdho/SageAttention
  - *From: Kijai*

- **HoloCine examples and documentation** (documentation)
  - https://holo-cine.github.io/
  - *From: avataraim*

- **LongCat examples** (documentation)
  - https://meituan-longcat.github.io/LongCat-Video
  - *From: Pandaabear*

- **Video-As-Prompt (VAP)** (repo)
  - https://github.com/bytedance/Video-As-Prompt
  - *From: DawnII*

- **LongCat models and distill lora** (model)
  - https://huggingface.co/Kijai/LongCat-Video_comfy/tree/main
  - *From: JohnDopamine*

- **SVI LoRAs** (lora)
  - https://huggingface.co/Kijai/WanVideo_comfy/tree/main/LoRAs/Stable-Video-Infinity
  - *From: Kijai*

- **LongCat branch of WanVideoWrapper** (repo)
  - https://github.com/kijai/ComfyUI-WanVideoWrapper/tree/longcat/LongCat
  - *From: avataraim*

- **Triton Windows wheel** (tool)
  - https://github.com/woct0rdho/triton-windows/releases
  - *From: Kijai*

- **MediaSyncer video comparison tool** (tool)
  - https://phazei.github.io/MediaSyncer/
  - *From: phazei*

- **PyTorch and dependencies setup commands** (tool)
  - pip install torch==2.7.0 torchvision==0.22.0 torchaudio==2.7.0 --index-url https://download.pytorch.org/whl/cu128
  - *From: avataraim*

- **Wan 2.1 VAE 2x upscaler** (model)
  - https://huggingface.co/spacepxl/Wan2.1-VAE-upscale2x
  - *From: spacepxl*

- **ComfyUI-VAE-Utils** (repo)
  - https://github.com/spacepxl/ComfyUI-VAE-Utils
  - *From: spacepxl*

- **Ditto with Wan enhancement** (repo)
  - https://github.com/EzioBy/Ditto/commit/9912e339c2add7f01f1095b3c06cf228177c79e9
  - *From: JohnDopamine*

- **Kaleido model** (model)
  - https://huggingface.co/Crilias/Kaleido-14B-S2V/tree/main
  - *From: yi*

- **Kaleido experimental fp16** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/blob/main/Kaleido/Wan_2_1_kaleido_14B-S2V_experimental_fp16.safetensors
  - *From: Kijai*

- **Deconv checkerboard explanation** (resource)
  - https://distill.pub/2016/deconv-checkerboard/
  - *From: spacepxl*

- **ComfyUI-WanAnimate-Enhancer** (tool)
  - https://github.com/wallen0322/ComfyUI-WanAnimate-Enhancer
  - *From: A.I.Warper*

- **ComfyUI-WanVideoWrapper-Multishot** (repo)
  - https://github.com/Dango233/ComfyUI-WanVideoWrapper-Multishot
  - *From: NebSH*

- **ComfyUI-VAE-Utils** (repo)
  - https://github.com/spacepxl/ComfyUI-VAE-Utils
  - *From: Quality_Control*

- **The Transformation Engine dev branch** (tool)
  - https://github.com/fblissjr/the-transformation-engine/tree/dev
  - *From: fredbliss*

- **ComfyUI-QwenImageWanBridge** (repo)
  - https://github.com/fblissjr/ComfyUI-QwenImageWanBridge
  - *From: fredbliss*

- **LongCat refinement LoRA** (model)
  - https://huggingface.co/Kijai/LongCat-Video_comfy/tree/main
  - *From: JohnDopamine*

- **DITTO with Denoise Enhancing** (repo)
  - https://github.com/EzioBy/Ditto?tab=readme-ov-file#denoising-enhancing
  - *From: JohnDopamine*

- **Comfyui-Memory_Cleanup** (tool)
  - https://github.com/LAOGOU-666/Comfyui-Memory_Cleanup
  - *From: avataraim*

- **LongCat workflow by Kijai** (workflow)
  - https://discord.com/channels/1076117621407223829/1342763350815277067/1433114940385923192
  - *From: JohnDopamine*

- **Morph frames-to-video LoRA** (model)
  - https://huggingface.co/morphic/Wan2.2-frames-to-video
  - *From: VK (5080 128gb)*

- **Next Scene QWen Edit LoRA** (model)
  - https://huggingface.co/lovis93/next-scene-qwen-image-lora-2509
  - *From: JohnDopamine*

- **VACE module 1.3B** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/blob/main/Wan2_1-VACE_module_1_3B_bf16.safetensors
  - *From: Lodis*

- **ChronoEdit by NVIDIA** (repo)
  - https://github.com/nv-tlabs/ChronoEdit
  - *From: JohnDopamine*

- **Wan2.2 SDNQ optimization** (model)
  - https://huggingface.co/Disty0/Wan2.2-I2V-A14B-SDNQ-uint4-svd-r32
  - *From: Ada*

- **SDNQ optimization tool** (repo)
  - https://github.com/Disty0/sdnq
  - *From: Ada*

- **LightX2V 1030 LoRA** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/blob/main/LoRAs/Wan22_Lightx2v/Wan_2_2_I2V_A14B_HIGH_lightx2v_4step_lora_v1030_rank_64_bf16.safetensors
  - *From: Kijai*

- **ChronoEdit demo** (demo)
  - https://huggingface.co/spaces/nvidia/ChronoEdit
  - *From: JohnDopamine*

- **Qwen music model announcement** (announcement)
  - https://x.com/JustinLin610/status/1982052327180918888
  - *From: JohnDopamine*

- **Radial Attention Wan2.2 commit** (repo)
  - https://github.com/mit-han-lab/radial-attention/commit/af371cad086ad0092a3320c1f8dc8d091b18e2a6
  - *From: JohnDopamine*

- **SDNQ Quantization method** (repo)
  - https://github.com/vladmandic/sdnext/wiki/SDNQ-Quantization
  - *From: JohnDopamine*

- **ComfyUI WanAnimate Enhancer** (tool)
  - https://github.com/wallen0322/ComfyUI-WanAnimate-Enhancer
  - *From: ˗ˏˋ⚡ˎˊ-*

- **SkyReels V2 I2V 1.3B model** (model)
  - https://huggingface.co/Skywork/SkyReels-V2-I2V-1.3B-540P
  - *From: Kijai*

- **BRIA FIBO model** (model)
  - https://huggingface.co/briaai/FIBO
  - *From: Tony(5090)*

- **CamCloneMaster project** (project)
  - https://camclonemaster.github.io/
  - *From: Yan*

- **Video-As-Prompt model** (model)
  - https://huggingface.co/ByteDance/Video-As-Prompt-Wan2.1-14B
  - *From: hicho*

- **Morphic Wan2.2 frames-to-video** (model)
  - https://huggingface.co/morphic/Wan2.2-frames-to-video
  - *From: hicho*

- **ChronoEdit full model** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/blob/main/ChronoEdit/Wan2_1-I2V-14B_ChronoEdit_fp16.safetensors
  - *From: Kijai*

- **ChronoEdit distill LoRA** (lora)
  - https://huggingface.co/Kijai/WanVideo_comfy/blob/main/ChronoEdit/Wan_2_1_I2V_14B_ChronoEdit_distill_lora_rank32.safetensors
  - *From: Kijai*

- **ChronoEdit FP8 versions** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy_fp8_scaled/tree/main/ChronoEdit
  - *From: Kijai*

- **LightX2V 1030 LoRA** (lora)
  - https://huggingface.co/Kijai/WanVideo_comfy/tree/main/LoRAs/Wan22_Lightx2v
  - *From: Gleb Tretyak*

- **ChronoEdit prompting guide** (documentation)
  - https://github.com/nv-tlabs/ChronoEdit/blob/main/docs/PROMPT_GUIDANCE.md
  - *From: Lodis*

- **KJNodes LoRA extraction node** (node)
  - *From: Hashu*

- **LightX2V team LoRAs** (lora)
  - https://huggingface.co/lightx2v/Wan2.2-Distill-Loras/tree/main
  - *From: Elvaxorn*

- **ChronoEdit models** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/tree/main/ChronoEdit
  - *From: Kiwv*

- **ChronoEdit 14B fp16** (model)
  - https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/blob/main/split_files/diffusion_models/chrono_edit_14B_fp16.safetensors
  - *From: comfy*

- **ChronoEdit fp8 version** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy_fp8_scaled/tree/main/ChronoEdit
  - *From: Lodis*

- **FlashVSR v1.1** (model)
  - https://huggingface.co/JunhaoZhuang/FlashVSR-v1.1/tree/main
  - *From: yi*

- **ChronoEdit GGUF** (model)
  - https://huggingface.co/QuantStack/ChronoEdit-14B-GGUF
  - *From: YarvixPA*

- **Qwen VL ComfyUI implementations** (repo)
  - https://github.com/SXQBW/ComfyUI-Qwen-VL, https://github.com/alexcong/ComfyUI_QwenVL, https://github.com/1038lab/ComfyUI-QwenVL
  - *From: aikitoria*

- **FlashVSR workflow** (workflow)
  - https://github.com/kijai/ComfyUI-WanVideoWrapper/blob/main/example_workflows/wanvideo_1_3B_FlashVSR_upscale_example.json
  - *From: DawnII*

- **LongCat face fix workflow** (workflow)
  - provided as image
  - *From: Ablejones*

- **Raylight - GPU pooling solution** (tool)
  - https://github.com/komikndr/raylight
  - *From: Kinasato*

- **ChronoEdit** (tool)
  - https://huggingface.co/Kijai/WanVideo_comfy/tree/main/ChronoEdit
  - *From: Ness*

- **Sora 2 prompting guide** (resource)
  - https://cookbook.openai.com/examples/sora/sora2_prompting_guide
  - *From: Draken*

- **ChronoEdit distill LoRA** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/blob/main/ChronoEdit/Wan_2_1_I2V_14B_ChronoEdit_distill_lora_rank32.safetensors
  - *From: mamad8*

- **Kijai GGUF models** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy_GGUF/tree/main
  - *From: xwsswww*


## Known Limitations

- **Wan 2.2 High Noise model fails with large inpaint masks**
  - Performance depends on mask size, smaller masks work better
  - *From: Ablejones*

- **None of the i2v WAN models understand masking**
  - Makes it difficult to work with different backgrounds in keyframes
  - *From: km*

- **Memory issues persist even with 64GB RAM**
  - Video models have enormous memory requirements, may need 80GB+ swap
  - *From: Ablejones*

- **Current Wan 2.5 lipsync quality is poor**
  - Lipsync performance described as 'terrible'
  - *From: dj47*

- **Palingenesis model lacks documentation**
  - No model card description, difficult to understand what it actually improves
  - *From: mallardgazellegoosewildcat*

- **Face detection fails on certain aspect ratios**
  - Swapping width/height in resolution causes detection to fail completely
  - *From: Gateway {Dreaming Computers}*

- **SageAttention3 incompatible with Wan**
  - Produces artifacts for Wan, workaround exists but not worth it
  - *From: yi*

- **WanAnimate character consistency issues**
  - Poor character consistency (2/10) with certain settings combinations
  - *From: Gleb Tretyak*

- **Palingenesis shows no noticeable improvement**
  - Multiple users report no visible difference from standard model, looks like different seeds
  - *From: Draken*

- **WanAnimate face similarity issues**
  - Can't get face similarity without LightX LoRA, subjects change ethnicity (Japanese appears Indian/African)
  - *From: Christian Sandor*

- **Topaz still has plastic skin issues**
  - Despite generative upscaler improvements, plastic skin artifacts remain
  - *From: Drommer-Kille*

- **Official WanAnimate pipeline unclear**
  - Kijai admits not understanding how official WanAnimate is supposed to work with CFG 1.0
  - *From: Kijai*

- **Context windows have coherency issues**
  - Temporal coherency between windows is probably worse and processing is much slower
  - *From: Kijai*

- **HuMO short generation length**
  - Becomes unusable over certain time duration
  - *From: U̷r̷a̷b̷e̷w̷e̷*

- **720p resolution on 3060**
  - 720p generations rare on 3060 due to VRAM constraints
  - *From: mdkb*

- **Sage 3 quality degradation**
  - Significant quality loss, speed benefit minimal when limiting to certain steps/blocks
  - *From: Kijai*

- **One Trainer doesn't support Wan models**
  - Lacks support for Wan model training
  - *From: xwsswww*

- **OVI English only**
  - Currently only supports English language prompts and speech generation
  - *From: slmonker(5090D 32GB)*

- **OVI lacks scene changes and POV cuts**
  - Missing important cinematic features like scene transitions that Sora 2 has
  - *From: Rainsmellsnice*

- **Wan 2.2 5B performance issues**
  - Significantly slower than 14B version due to VAE overhead, questionable performance gains
  - *From: Draken*

- **OVI sound effects quality**
  - Can do sound effects but not as good as speech generation
  - *From: Screeb*

- **Smooth mix can't be used with CFG**
  - Merged lightx or lightning lora prevents CFG usage
  - *From: Lumifel*

- **OVI requires 24GB VRAM in fp8**
  - 5B distill likely won't work due to increased parameters and 5B VAE computational requirements
  - *From: Draken*

- **Wan 2.1 refuses helmet prompts**
  - Simple prompts like putting on helmet don't work well
  - *From: Dream Making*

- **OVI has no ComfyUI support yet**
  - Only gradio demo available, implementation may be half-baked
  - *From: TK_999*

- **Lip-sync quality degrades after 5 seconds**
  - Most models drift in dialogue scenes, viewers notice small discrepancies
  - *From: mdkb*

- **Lightning LoRA causes child generation bias**
  - With certain LoRAs, model has insane bias towards generating kids only
  - *From: Dream Making*

- **Merging High and Low models causes zero-g effect**
  - Even 4% merge of High into Low causes floating objects
  - *From: Thom293*

- **Character LoRAs from 2.1 don't work well on 2.2**
  - LoRAs trained on Wan 2.1 T2V perform badly on Wan 2.2 T2V
  - *From: Dream Making*

- **I2V face degradation**
  - I2V shows noticeable face degradation and overly intense muscle movement
  - *From: slmonker(5090D 32GB)*

- **OVI NSFW capability limited**
  - OVI has some NSFW capability but just barely
  - *From: slmonker(5090D 32GB)*

- **14B model architecture restriction**
  - 14B model has separate I2V and T2V, only 5B model supports both unified
  - *From: slmonker(5090D 32GB)*

- **SageAttn3 only works on Blackwell cards**
  - Limited to B200/B300 cards with sm120a, won't work on older GPUs like RTX 6000 Pro
  - *From: Kijai*

- **Burned-in look from multiple I2V continuations**
  - Can get about 4 continuations before things start getting blown out due to VAE decoding and extending issues
  - *From: voxJT*

- **Wan 2.2 motion coherence worse than 2.1**
  - While quality is better, motion coherence is not as good as 2.1
  - *From: Dream Making*

- **Most LoRAs not upgraded for 2.2**
  - Only LightX got 2.2 version, CausVid and Movigen still on 2.1
  - *From: Dream Making*

- **SAGE3 attention speedup has limited benefit with distill LoRAs**
  - With 4-step distill LoRA, SAGE3 only applies to 2 steps, loses quality and gains almost nothing
  - *From: Kijai*

- **Attention speedups can randomly harm video quality**
  - Hard to predict when important attention connections are lost, causing random quality degradation
  - *From: mallardgazellegoosewildcat*

- **Direct latent upscaling poorly implemented**
  - Cannot upscale latents with good quality without first decoding to images
  - *From: Lan8mark*

- **VACE 2.1 14B only supports T2V LoRAs**
  - vace is t2v, some keys will load i think, but you most likely want to use the light2x t2v distill lora. It will load 'some stuff' from the i2v lora, but not well at all
  - *From: Draken*

- **Lynx flashing issue with 121 frames**
  - it just doesn't like the 121 frames I guess
  - *From: Kijai*

- **OVI lacks voice consistency**
  - the lack of voice consistency is an issue for anything other than messing around
  - *From: AiAuteur*

- **Latent upscaling destroys fine details**
  - Latent upscaling is when you upscale H and W in latent space it usually leads to artifacts or blurry frames its useless for i2v even t2v coz it destroys the face/character likeness eyes any sort of fine details
  - *From: shaggss*

- **VAE latents don't follow normal 2D geometry**
  - The issue is VAE latents don't follow normal 2D geometry. They do a little bit though so it kinda works with errors. Same reason slicing VAE for decode is lossy
  - *From: mallardgazellegoosewildcat*

- **OVI model currently 5 seconds maximum length**
  - Audio-video generation limited to 5 second outputs
  - *From: Juampab12*

- **e4m3fn_scaled doesn't work on RTX 3000 series**
  - Must use e5m2 instead on 3090 and similar GPUs
  - *From: Kijai*

- **Tiled VAE issues with VACE extend**
  - Creates blurry output and position shifts at certain resolutions like 1280x720 and 1920x1072
  - *From: Lumifel*

- **Many 1.3B models are proof of concept only**
  - Not practically useful compared to 5B alternatives
  - *From: Kijai*

- **Sage 3 has considerable quality drop**
  - While faster, the quality hit makes it not worth upgrading to
  - *From: HeadOfOliver*

- **FP8 quantization quality loss**
  - FP8 makes everything blurry and motion is far worse, especially bad for WAN
  - *From: Ada*

- **OVI camera angle prompting**
  - OVI interprets cinema angles as part of dialogue even when placed elsewhere in prompt
  - *From: Drommer-Kille*

- **OVI style consistency**
  - Unless style is specified, OVI t2v jumps between realism and anime styles
  - *From: Drommer-Kille*

- **Face degradation in longer videos**
  - Using last frame as input for next generation causes face quality to progressively worsen
  - *From: Tachyon*

- **WAN upscaler transitions**
  - Transitions between 5-second clips are still slightly noticeable, needs soft padding
  - *From: Lan8mark*

- **SEC small object detection**
  - Segmentation models like SEC likely have minimum bbox dimensions, may miss very small objects
  - *From: psylent_gamer*

- **TAE VAE quality loss**
  - TAE VAE is only for preview, causes significant quality degradation for final outputs
  - *From: Draken*

- **CLIP embeds not used in 2.2 I2V**
  - CLIP embeds don't make difference in Wan 2.2 I2V workflows
  - *From: Draken*

- **Radial attention quality hit**
  - Radial attention reduces expressiveness, particularly noticeable in lip sync applications
  - *From: blake37*

- **LightX 2.2 LoRA quality issues**
  - Most LightX 2.2 LoRAs have poor quality compared to 2.1 versions
  - *From: Dream Making*

- **First frame flash in VACE 2.2**
  - VACE 2.2 has persistent first frame flashing issue that's difficult to resolve completely
  - *From: mdkb*

- **30xx cards cannot use e4m3fn format**
  - Need to use e5m2 format for 30xx series GPUs
  - *From: mdkb*

- **Official Lightx2v LoRA produces glitchy output at low steps**
  - Needs 12+ steps to work properly, defeats purpose of speed LoRA
  - *From: Ashtar*

- **T2V distill LoRAs greatly diminish movement when used on I2V**
  - Cross-compatibility between T2V and I2V LoRAs is poor
  - *From: Ada*

- **LoRA cannot patch time_embedding and text_embedding layers**
  - ComfyUI limitation prevents full LoRA application to all trained layers
  - *From: JohnDopamine*

- **Wan 2.2 slow motion issues**
  - Still has slow motion effect with new distill models in 4 or 8 steps CFG1. Some call it 'cinematic' but it's actually slow motion
  - *From: Vérole*

- **StepVideo VAE artifacts**
  - Can have VAE artifacts due to more compressive VAE, pros and cons
  - *From: mallardgazellegoosewildcat*

- **OVI 5B model quality**
  - Has a '5B look' in video quality that's noticeable, probably could be refined with another pass
  - *From: Kijai*

- **New LightX2V vertical line artifacts**
  - Artifacts happen on widescreen/16:9 aspect ratios for both LoRA and finetune versions, but not on portrait images
  - *From: blake37*

- **FlashVSR speed only on H100**
  - The 11GB usage and speed benefits only really work at those speeds on H100/etc, big caveat for consumer GPUs
  - *From: JohnDopamine*

- **TaylorSeer quality degrades with high movement**
  - Works well for static scenes but struggles with dynamic content
  - *From: Zabo*

- **FP8 models don't work with quantization on older GPUs**
  - RTX 3060 and similar cards need quantization disabled
  - *From: U̷r̷a̷b̷e̷w̷e̷*

- **No good solution for pose detection with distant characters**
  - Current pose detection struggles when character is far from viewer
  - *From: Kijai*

- **Wan 2.2 generates noise with 20 steps without fast LoRA**
  - Specific issue with step count and model combination
  - *From: Drommer-Kille*

- **Distillation LoRAs fail to produce dynamic motion like CFG for Wan 2.2 high noise**
  - Many attempts made but none match the motion quality of using CFG
  - *From: Kijai*

- **FlashVSR produces more artifacts at higher resolutions**
  - Quality degradation increases with resolution, also has excessive sharpness issues
  - *From: Elvaxorn*

- **TaylorSeer has poor prompt adherence**
  - Results are very wild and not recommended despite speed
  - *From: Tachyon*

- **Wan2.2 VAE noise grids**
  - Generates artifacts especially with sharp images of people with hair, enhanced by SeedVR2
  - *From: aikitoria*

- **VACE strength parameter cannot be separated**
  - Overall strength applies to both reference image and control video, cannot control independently
  - *From: Kijai*

- **No VACE for 5B model**
  - VACE currently only exists for 14B model
  - *From: Kijai*

- **New distill models are I2V only**
  - No T2V version available
  - *From: Lodis*

- **Wan artifacts at 17 frames**
  - 1 second videos create weird artifacts at the start
  - *From: yi*

- **Lightning LoRAs make everything brighter**
  - Have annoying side effects that affect image brightness
  - *From: Kijai*

- **FlashVSR bad for distant faces**
  - Produces poor results for faces that are not very close, faces at distance tend to fall apart
  - *From: Tony(5090)*

- **Most 2.2 LoRAs are crap while 2.1 LoRAs are bad at movement**
  - General quality issues with different LoRA versions for different use cases
  - *From: Dream Making*

- **MOE LoRA doesn't work well in existing I2V workflows**
  - Produces wobbly outputs when used in standard I2V setups
  - *From: Draken*

- **Wan 2.2 non-5B models not true 24fps**
  - Only 5B model supports true 24fps, others have frame rate limitations
  - *From: garbus*

- **OVI poor consistency even at 720p**
  - Terrible consistency issues despite good prompt following and expression
  - *From: mdkb*

- **rCM requires 4 steps minimum**
  - Despite claims of 1-step generation, actual usage requires 4 steps, 1-step not demonstrated
  - *From: Kijai*

- **FP8 dramatic quality reduction**
  - Especially noticeable in video extension tasks and longer generations
  - *From: Zabo*

- **HuMo doesn't do long videos well**
  - Works well with loras but struggles with longer video generation
  - *From: Ablejones*

- **Ditto LoRAs only work well with people/humanoids**
  - Training was mostly around humans, doesn't work well with other subjects like animals
  - *From: Dever*

- **Ditto tends to inject unwanted humans into scenes**
  - Adds faces or people even when not prompted, especially with pixel art style
  - *From: Dream Making*

- **Style transfer can lose original movement/motion**
  - Movement is often lost during style transfer process
  - *From: Dream Making*

- **Lipsync models struggle with eye direction control**
  - Hard to get speakers to look in specific directions, crucial for dialogue scenes
  - *From: mdkb*

- **Ditto breaks other VACE functionalities**
  - Style transfer LoRAs are incompatible with other VACE features
  - *From: Draken*

- **Pose estimation limited to basic movements**
  - Current pose estimators can't handle complex movements well
  - *From: Draken*

- **Ditto works best with specific trained instructions**
  - Works with exact instructions used to train the model, may not generalize well
  - *From: Govind Singh*

- **Krea model very noisy in normal workflows**
  - Rough on normal workflows, supposed to be used 3 latents at a time like causvid
  - *From: Kijai*

- **Krea realtime quality is disappointing even at 14B**
  - Model has to lose tons of quality to handle the strange context
  - *From: Kijai*

- **Krea realtime doesn't work well as LoRA**
  - It's distilled so similar case to causvid as LoRA - only full model worked properly
  - *From: Kijai*

- **MoCha needs background removal for reference**
  - Reference images need background removed for proper function
  - *From: DawnII*

- **Wan 2.2 since release has been more of the same**
  - Basically Wan 2.1 extensions, no relevant release to some users' taste
  - *From: ZeusZeus (RTX 4090)*

- **MoCha only works well with humans**
  - Doesn't work on architecture or non-human subjects
  - *From: Charlie*

- **MoCha produces CG-like results**
  - Often looks artificial, sometimes bad CG quality, inconsistent results
  - *From: Screeb*

- **MoCha context issues with multiple characters**
  - For 300+ frames, applies reference to wrong characters and selected character disappears
  - *From: Visionmaster2*

- **MoCha doubles VRAM usage**
  - Cannot be used like normal model due to frame dimension doubling
  - *From: Kijai*

- **Ditto processing speed varies with motion**
  - Fast-paced sequences take longer to process than closeups/portraits
  - *From: Govind Singh*

- **MoCha mask doesn't work well**
  - Model often ignores the mask and sometimes replaces multiple characters instead of just the masked one
  - *From: Juampab12*

- **QwenImage VAE only works with newer models**
  - Can't get it to work with actual old models that weren't trained with the new VAE
  - *From: Kijai*

- **Rolling Force model not useful for normal workflows**
  - Only for realtime stuff, it's just 1.3B parameters
  - *From: Kijai*

- **Context drift still occurs with video extensions**
  - Information outside given frames still gets lost in long video generation
  - *From: Juampab12*

- **SVI shot workflow motion continuation**
  - Single motion frame limitation means it can't properly continue motion, ends up with jerky transitions
  - *From: Kijai*

- **Character consistency in I2V chaining**
  - If person closes eyes at end of shot, next generation can't guess what the person's eyes look like
  - *From: Draken*

- **Exposure degradation in long generations**
  - Exposure always goes up over time, creating gradual brightness increases that are part of quality degradation
  - *From: Ablejones*

- **Distill LoRA contamination**
  - Distill LoRAs can interfere with testing new techniques and smallest changes can break continuation workflows
  - *From: Kijai*

- **SVI quality degrades over time in long chains**
  - Noticeable quality loss and detail blurring in third chain and beyond
  - *From: voxJT*

- **Mocha fails with two-character scenarios**
  - Either applies reference to both characters or outputs wrong character, gradual disappearance over time
  - *From: Visionmaster2*

- **Ditto has effective 3-second optimal limit**
  - Quality severely degrades beyond 72 frames despite technical capability for longer videos
  - *From: Drommer-Kille*

- **SVI clothing inconsistency with camera movements**
  - Person's clothes change when camera zooms in/out from full body to half body
  - *From: army*

- **Video models perform poorly with dark starting frames**
  - I2V models consistently struggle when given dark initial frames
  - *From: Ablejones*

- **No custom mask input in native ComfyUI**
  - Native ComfyUI nodes don't allow manual adjustment of masks for video generation
  - *From: Ablejones*

- **Wan 2.2 ignores clip embeds in native**
  - Only WanAnimate model uses clip embeds, other 2.2 models ignore them in WanImageToVideo node
  - *From: Kijai*

- **MTV Crafter limited to 49 frames**
  - Model architecture limited to 49 frame generation, may degrade with longer sequences
  - *From: DawnII*

- **Light/Tiny VAEs require code changes for native support**
  - Cannot load light or tiny VAE variants without modifying native implementation
  - *From: Kijai*

- **HoloCine not fully functional without proper implementation**
  - Needs varlen attention and rope setup, currently only works as normal T2V without scene switching capabilities
  - *From: Kijai*

- **SVI degrades significantly after 25 seconds**
  - Gets even worse with lots of movement, causing quality degradation
  - *From: Zabo*

- **Context windows prone to artifacts at transitions**
  - Often need to batch 4 generations to get 1 good result without ghosting
  - *From: blake37*

- **HoloCine currently only 480p resolution**
  - Though GitHub mentions 720p capability
  - *From: aikitoria*

- **5-frame SVI method causes image degradation**
  - Pushing model with 5 images is like 5x the strength, contributes to quality loss
  - *From: Draken*

- **SVI distill LoRAs don't work perfectly**
  - Never gonna work perfectly with distill loras like lightx2v, errors accumulate eventually
  - *From: Kijai*

- **Shot method doesn't continue motion**
  - Can't continue motion from single frame, just I2V. Only stabilizes long continuous generations
  - *From: Kijai*

- **2.1 LoRAs on 2.2 high noise**
  - No 2.1 LoRA works properly on 2.2 high noise, architecture too different
  - *From: Kijai*

- **VAE degradation in extensions**
  - Last frames from output never as clean as original input unless original was super low res. VAE encode/decode degrades over time
  - *From: Draken*

- **ComfyUI loops not practical for iterative work**
  - Can't stop and play with each segment, try multiple times. Set it and forget it doesn't work well for this type of work
  - *From: Ablejones*

- **Film lora degrades over time**
  - Unlike shot lora which can theoretically do infinite length, film lora will degrade over time
  - *From: Kijai*

- **Film lora incompatible with reference padding**
  - Film lora will freeze if you try to use reference frames/padding
  - *From: Ablejones*

- **Color degradation over time**
  - Color still degrades over time even with SVI
  - *From: VK (5080 128gb)*

- **Wan removes extra limbs from niche characters**
  - Accurate training to prevent body horror means characters that should have extra limbs get them removed quickly
  - *From: Ablejones*

- **SVI doesn't work great with Wan 2.2**
  - Shot SVI setup with wan2.2 didn't work great, though film method with multiple frames not tested
  - *From: Draken*

- **SVI Shot LoRA incompatible with Wan 2.2**
  - Shot LoRA completely breaks when used with 2.2, people have tried without success
  - *From: Kijai*

- **Latent manipulation always causes artifacts**
  - Any editing of first frame in latents causes light flashing, color shifting, ghosting, or echo effects. Only trimming end frames works cleanly
  - *From: lemuet*

- **Can't combine video latents without VAE decode**
  - Video latents after first frame contain 4 images each, can't extract single image representation without full VAE decode
  - *From: Kijai*

- **LongCat begins repeating after 6 seconds for single long pieces**
  - Cannot generate truly long videos in one go, needs extension method
  - *From: aikitoria*

- **Holocine character consistency weaker with mixed models**
  - Less strong character consistency when using Holocine high + WAN low
  - *From: mamad8*

- **LongCat distill LoRA poor prompt following**
  - 16 step distill version didn't follow prompt (dog didn't eat ice cream as prompted)
  - *From: aikitoria*

- **WAN VAE produces noise grids on detailed inputs**
  - Same ugly outputs with noise patterns, no progress made on VAE quality
  - *From: aikitoria*

- **FP8 scaled models won't work with original Holocine repo**
  - Compatibility issue between quantized models and original implementation
  - *From: seitanism*

- **HoloCine license restrictions**
  - CC BY-NC-SA 4.0 license requires attribution and prevents commercial use
  - *From: Tony(5090)*

- **WAN VAE noise grids cannot be removed**
  - Video upscaling methods like SeedVR2 and Topaz preserve the artifacts
  - *From: aikitoria*

- **LongCat consistency issues**
  - Heavy consistency degradation when objects leave and return to frame
  - *From: Shubhooooo*

- **SVI-Film only supports 5 frames**
  - Cannot use 9 or 11 frames, only trained for 5-frame input
  - *From: Ablejones*

- **LongCat can't maintain identity well**
  - Seems to care about init image even less than Pusa
  - *From: scf*

- **LongCat no first/last frame setup**
  - Don't have setup for first/last frame, attention split code doesn't account for that possibility
  - *From: Kijai*

- **LongCat lacks control options**
  - No LoRAs or control available yet, more curiosity/novelty right now
  - *From: Kijai*

- **Holocine 15 second limit**
  - Current holocine trained on 15sec, longer generations have quality issues
  - *From: NebSH*

- **LongCat prompt understanding**
  - Doesn't understand prompts as well as Wan 2.2, may need better prompting techniques
  - *From: avataraim*

- **fp16 precision with Wan models**
  - Consistently produces NaN results leading to black outputs, doesn't work with quantizations
  - *From: Kijai*

- **MoCha long generation capability**
  - Worse at long generations as it lacks innate ability, somewhat works with context windows
  - *From: Kijai*

- **HoloCine only 15 second model released**
  - 1 minute model not working/not released yet
  - *From: avataraim*

- **LongCat refinement creates noisy texture at full strength**
  - Refinement lora at 1.0 strength creates noisy texture, especially visible on focused parts like hair
  - *From: Kijai*

- **PUSA doesn't hold reference frames properly with Holocine**
  - Not holding the first frame past the first couple frames, not really 'working' for reference consistency
  - *From: JohnDopamine*

- **WanAnimate doesn't use CFG in original implementation**
  - Original doesn't use CFG at all for efficiency, may need CFG for finer facial expression control
  - *From: Kijai*

- **Wan2.2 LightVAE shows quality loss**
  - Despite claims, shows considerable quality loss compared to Wan2.1 VAE
  - *From: Fawks*

- **Wan VAE has moving grid patterns on hair in i2v**
  - Snaps to different gradient for each patch every frame, especially visible on character hair
  - *From: aikitoria*

- **Spacepxl's VAE upscaler fails on video decoding**
  - Only trained on images, will fail hard if used for video decoding
  - *From: spacepxl*

- **LongCat limited to 6 seconds without extension**
  - Extension is only way to get longer generations
  - *From: Zabo*

- **Wan VAE latents can't be cleanly cut due to temporal information**
  - Can't extract single frame from latent that packs 4 frames due to causal convolutions
  - *From: mamad8*

- **OVI cannot do video-to-video with audio syncing like InfinityTalk**
  - Kijai couldn't get it to work when tried
  - *From: Kijai*

- **OVI has 10 second maximum generation limit**
  - 15 second generations fail, recommend 8 seconds for better results
  - *From: avataraim*

- **Video extension using one frame at a time lacks temporal consistency**
  - Processing individual frames will never give consistency, need temporal context
  - *From: spacepxl*

- **Current WAN models have soft latents causing artifacts**
  - Pupil problems when not enough resolution, probably need more faces in training data
  - *From: spacepxl*

- **Latent space upscalers create ghosting**
  - Almost all upscalers in latent space create ghosting or awful tiling, best found so far is DenRakEiw/WAN_NN_Latent_Upscale but still has ghost entries
  - *From: mdkb*

- **WAN 5B LoRA training difficulties**
  - Impossible to train LoRAs for WAN 5B, VAE seems too tuned to their dataset
  - *From: Kiwv*

- **WAN can't handle faster paced content**
  - For faster pace things WAN just can't do it, needs 24fps capability
  - *From: Kiwv*

- **LongCat has no extra control compared to Wan 2.2**
  - No additional control features, just supposed to work better with I2V
  - *From: Kijai*

- **Video continuation loses reference when subjects turn around**
  - Once a person turns around and video ends, continuation cannot recover original face without reference input
  - *From: Draken*

- **SVI-shot sticks too closely to reference**
  - Tries to snap back to reference image even when scene changes, causing unrealistic effects
  - *From: Ablejones*

- **LongCat incompatible with VACE blocks**
  - Too different architecture and dimensions to work with existing VACE
  - *From: Kijai*

- **Below 5 steps causes major quality issues**
  - Massive lighting smoothness issues, depth inconsistency, and general blurriness
  - *From: Pandaabear*

- **Current AI video quality not suitable for production consumption**
  - Purely prompt-to-video or image-to-video looks like 'AI slop' and not enjoyable for content consumption
  - *From: Kijai*

- **LTX 2 has unusable audio quality**
  - Despite technical specs like 4K 50fps, audio quality makes it unusable compared to Wan
  - *From: Kijai*

- **EXR files incompatible with pose systems**
  - Pose detection/processing systems cannot handle EXR format images
  - *From: Guus*

- **LongCat may not be sufficient improvement for ecosystem development**
  - While clearly better than Wan, may not be enough improvement to justify training new ecosystems around it
  - *From: Kijai*

- **ChronoEdit doesn't work well with short prompts**
  - Needs detailed prompts or LLM enhancement for good results
  - *From: Kijai*

- **LongCat terrible at 2D content**
  - Performance issues with 2D/animated content
  - *From: Ada*

- **ChronoEdit is I2V only, no T2V capability**
  - Purely image-to-video, cannot generate from text alone
  - *From: CJ*

- **Lightning LoRA changes exposure and has poor motion**
  - Makes output brighter and motion quality is not the best
  - *From: Kijai*

- **ChronoEdit does more processing than necessary**
  - Quality is solid but computationally inefficient compared to alternatives
  - *From: Kiwv*

- **ChronoEdit fails on same prompts where Qwen fails**
  - No improvement over existing solutions in problem cases
  - *From: aikitoria*

- **LongCat has no reference images support**
  - If character turns around by bad luck, becomes useless for continuation
  - *From: aikitoria*

- **LongCat is T2V only for some features**
  - HoloCine is T2V only, limiting usefulness
  - *From: aikitoria*

- **Context windows reset subject changes**
  - If subject has a tear running down cheek, tear will disappear in new context window
  - *From: blake37*

- **Context windows increase bad gen chances**
  - Each context window has its own chance of doing something weird or creating hallucinations
  - *From: blake37*

- **New 1030 LoRA tends to zoom in camera**
  - Even with 'camera still' or 'camera stationary' prompts, still does zooming
  - *From: WorldX*

- **VACE has autoregressive burn in and color drift**
  - Gets worse over time with autoregressive extension, not good at staying coherent
  - *From: Benjaminimal*

- **LongCat is hit or miss on prompt adherence**
  - Outputs appear as series of images rather than video in some cases
  - *From: Ness*

- **LongCat has different architecture from Wan**
  - Not trainable with Wan trainer
  - *From: Kiwv*

- **ChronoEdit prompt adherence is random**
  - Works better for animating existing images than redrawing from different perspectives
  - *From: Ness*

- **Long video generation causes progressive blur**
  - Videos get more and more blurry during extended generation chains
  - *From: aikitoria*

- **LightX motion continuity**
  - Motion is not totally continuous when using 4-step generation
  - *From: aikitoria*

- **Veo 3.1 fast motion quality**
  - Motion is awful 99% of the time, overlit, over sharpened, fake AI looking
  - *From: Ruairi Robinson*


## Hardware Requirements

- **RAM for video processing**
  - Even 64GB RAM can have issues, may need 80GB+ swap size. 100GB RAM user also reports memory issues
  - *From: Ablejones*

- **VRAM optimization flags**
  - --highvram, --gpu-only, --normalvram, --cache-none options available for different memory constraints
  - *From: Ablejones*

- **DWPose processing speed**
  - 5090 takes ~17min for 30fps 10sec clip at 720x1280, reduced to 3min with .torchscript
  - *From: rob*

- **ONNX GPU runtime for pose detection**
  - Without onnxruntime-gpu, pose detection runs on CPU and takes much longer
  - *From: Kijai*

- **Wan 2.2 upscaling performance**
  - Takes 10 minutes to upscale single image from 1080 to 4K on RTX 5090
  - *From: Drommer-Kille*

- **H100 performance for I2V**
  - 101 frames at 24fps plus upscale takes roughly 148s on H100 with 2-3 LoRAs + sage attention
  - *From: topmass*

- **Cloud CPU performance**
  - Cloud setups often have subpar CPU performance, affecting mask processing speed dramatically
  - *From: Kijai*

- **GPU vs CPU for mask operations**
  - GPU processing achieves 11409.67 it/s vs CPU 341.85 it/s for DrawMaskOnImage operations
  - *From: Kijai*

- **VRAM for 12GB setup**
  - Euler/beta scheduler works well for 12GB VRAM constraints
  - *From: U̷r̷a̷b̷e̷w̷e̷*

- **3060 12GB limits**
  - Max 65 frames at 1024x576, 25fps, 6 steps, ~7min generation time
  - *From: mdkb*

- **512 video training**
  - Needs 48GB VRAM for 512 resolution video training
  - *From: Ryzen*

- **Ovi fp8 VRAM**
  - 16GB VRAM required even with fp8 quantization
  - *From: Stad*

- **OVI VRAM requirements**
  - Needs high-end GPU, 5090 and up recommended, too heavy for most users currently
  - *From: Charlie*

- **Wan 2.2 5B VRAM**
  - Cannot run on 12GB VRAM without quantization despite being 5B parameters
  - *From: Stad*

- **ComfyUI-Upscale-CUDAspeed acceleration**
  - 50% acceleration on single 4090, 70% with 4090+4070ti, supports 20 series and up
  - *From: piscesbody*

- **OVI runtime environment**
  - Python 3.12.7, torch 2.8.0+cu128, flash-attn 2.7.4.post1 confirmed working
  - *From: TK_999*

- **OVI VRAM**
  - 24GB VRAM in fp8 mode, uses 16.4-19GB on 3090
  - *From: yukass*

- **Smooth mix RAM usage**
  - Causes more frequent OOM crashes, only 2-3 gens vs regular wan
  - *From: Rainsmellsnice*

- **4K upscale processing**
  - CPU gets work during 4K upscale at end of Wan 2.2 workflow
  - *From: Drommer-Kille*

- **HuMo fp8 model**
  - 11.3GB model works on RTX 3090, original 23GB model needs 32GB VRAM
  - *From: yukass*

- **RTX 50-series GPU compatibility**
  - ONNX Runtime 1.23.0 JIT compilation issues with compute capability 9.0+
  - *From: D-EFFECTS*

- **Mask expand operations**
  - 256+ radius expansions slow even with Kornia GPU update
  - *From: Mads Hagbarth Damsbo*

- **OVI VRAM usage**
  - Requires more than 8GB VRAM, needs optimization for lower VRAM usage
  - *From: Stad*

- **OVI generation time**
  - 213 seconds for 720p generation
  - *From: slmonker(5090D 32GB)*

- **Native vs Wrapper performance**
  - Native 121 frames takes 29:54, Wrapper would do under 10 minutes
  - *From: Drommer-Kille*

- **Memory configuration for Intel 13th/14th gen**
  - Use 2x64GB sticks instead of 4x32GB to avoid straining memory controller and enable XMP
  - *From: Ryzen*

- **VRAM for FP16 vs FP8**
  - FP16 uses double the memory compared to FP8, rarely worth the cost unless you have a monster GPU
  - *From: Kijai*

- **RTX 5090 performance**
  - Can achieve 720p video generation in 160 seconds with optimized Lightning LoRA settings
  - *From: Lan8mark*

- **5090 performance example**
  - 81 frames at 720p in 160 seconds using resolution reduction workflow
  - *From: Lan8mark*

- **RTX 3090 Wan 2.2 performance**
  - fp8_e5m2: 170s gen time, k8 gguf: 360s gen time with block swap 20
  - *From: Mattis*

- **Low-end training feasibility**
  - 17s/it, 3000 steps (~14hrs) on 6GB laptop GPU using AI-Toolkit with RAM training
  - *From: Ada*

- **4090 performance benchmark**
  - Sampling 81 frames at 992x512 with 40 steps: 4.29s/it
  - *From: Kijai*

- **5090 performance benchmark**
  - Sampling 121 frames at 992x512 with 40 steps: 3.29s/it with flash_attn, 2.02s/it with sage and fp16 fast. Max allocated memory: 24.534 GB
  - *From: Kijai*

- **ComfyUI storage usage**
  - my current comfy portable install is 1.2 tb, its 800gb in just the main models currently
  - *From: hudson223*

- **VACE 2.2 dual model VRAM usage**
  - those two amount to 19GB of files and yet run without filling up 12GB VRam
  - *From: mdkb*

- **OVI works on 8GB VRAM**
  - User confirmed OVI working on 8GB VRAM setup
  - *From: Stad*

- **160 seconds generation time mentioned**
  - User complaining about slow upscale times of 160 seconds
  - *From: mallardgazellegoosewildcat*

- **RAM upgrade impact**
  - 64GB vs 16GB RAM shows night and day difference - instant prompt changes vs seconds/minutes of waiting
  - *From: Miku*

- **OVI generation time on 5090**
  - 90s for 5s clip at base settings, 173s for 720p 50 steps
  - *From: Drommer-Kille*

- **WAN upscaler performance**
  - 150s for 720p to 2K, 350s for 480p to 2K on 5090
  - *From: Lan8mark*

- **VRAM needs with 4090**
  - User didn't even try WAN animate with 4090, waited for 5090 upgrade
  - *From: Juampab12*

- **RTX 5090 cooling**
  - MSI Suprim Liquid keeps temperatures under 68-72 degrees even during full hour usage
  - *From: GOD_IS_A_LIE*

- **Dual GPU setup issues**
  - Dual RTX setup can cause instability, single 5090 recommended for stability
  - *From: Charlie*

- **RAM limitations**
  - 64GB RAM may not be sufficient for dual GPU setups with heavy workloads
  - *From: Charlie*

- **5090 upscaling setup**
  - 5090 with 128GB RAM recommended for upscaling workflows on vast.ai
  - *From: FL13*

- **Cold start latency**
  - Serverless cold start under 1 second, few seconds for massive models
  - *From: mallardgazellegoosewildcat*

- **Local generation electricity costs**
  - 20 kWh in 48h, equals 540€/year for continuous use
  - *From: Drommer-Kille*

- **New Lightx2v full model size**
  - 24GB per file for high and low noise models
  - *From: Ashtar*

- **VRAM for 1920x1080 I2V**
  - RTX 5090 can handle 1920x1080 I2V generation
  - *From: Drommer-Kille*

- **StepVideo memory usage**
  - 768px × 768px × 102f = 76.42 GB, 1061s generation time
  - *From: Colin*

- **OVI 5B inference time**
  - Takes about an hour on RTX 3060 according to YouTube channel tests
  - *From: mdkb*

- **FlashVSR VRAM**
  - Peak VRAM usage is 11GB, much less than other diffusion upscalers, but speed benefits mainly on H100
  - *From: yi*

- **Video training on RTX 5090**
  - Using 256x256 resolution to avoid OOM when training with 81 frames
  - *From: Drommer-Kille*

- **FlashVSR VRAM usage**
  - Reserves 16GB on RTX 3060 12GB (more than available), works with text encode cache
  - *From: mdkb*

- **SageAttention speed improvement**
  - Can be more than twice as fast depending on resolution, also reduces VRAM usage
  - *From: Kijai*

- **MSI Suprim RTX performance**
  - 20-25% faster than FE at 104% power limit, lower temps, silent at 33% fan speed
  - *From: seitanism*

- **OVI model compatibility**
  - Runs on RTX 3060 12GB with fp8 models and quantization disabled
  - *From: U̷r̷a̷b̷e̷w̷e̷*

- **fp8_fast mode compatibility**
  - Works fine on 2.2 models with 5090, but works poorly quality-wise on 2.1 models
  - *From: Kijai*

- **FlashVSR processing speed**
  - 241 frames at 1248x1568 takes about 5 minutes, 150 seconds for upscaling vs 10-15min with Topaz
  - *From: DawnII*

- **SeedVR2 VRAM usage with block swapping**
  - Can run on 32GB VRAM with block swapping, minimal speed impact (3:56 vs 3:49 without)
  - *From: seitanism*

- **VRAM usage with fp32 VAE**
  - Doubles VRAM usage compared to bf16
  - *From: Kijai*

- **VACE frame scaling**
  - Roughly 2-4 GB per 25 frames at 480p on 14B model, doubles for 720p
  - *From: Dever*

- **Generation speed improvement**
  - New distill models generate video in 1 minute vs 25 minutes
  - *From: aikitoria*

- **FlashVSR VRAM usage**
  - 20GB VRAM for processing larger resolutions, 8.6GB VRAM for 100 frame batches at 1024x576, 10GB system RAM
  - *From: Kijai*

- **WAN Animate frame limits**
  - 720p 1000 frames easily achievable on 5090 with 128GB RAM, should work fine on 4090 with similar specs
  - *From: Charlie*

- **Block-Sparse Attention GPU requirements**
  - Only achieves ideal acceleration on NVIDIA A100/A800 GPUs, H100/H800 may be slower than dense attention
  - *From: JohnDopamine*

- **VRAM usage increase after updates**
  - Blockswap needed to increase from 25 to 35 for same 1120x704 97-frame generation, now uses 99% VRAM
  - *From: phazei*

- **5090 VRAM issues reported**
  - Even 5090 users experiencing OOM on VAE decode, may need tiled VAE
  - *From: Provydets*

- **720p generation time**
  - 1 hour initially, reduced to 30 mins with easycache on RTX 3060
  - *From: mdkb*

- **5090 performance for OVI**
  - Quick generation on RTX 5090 for 720p OVI
  - *From: Charlie*

- **VRAM for Wan 2.2 with Lightning LoRA**
  - DGX Spark vs RTX 6000 Pro performance comparison provided
  - *From: tarn59*

- **RAM upgrade**
  - Charlie got 128GB sticks (FURY Beast 128GB 5600MT/s DDR5 CL36) after having enough with 64GB
  - *From: Charlie*

- **PyTorch version compatibility**
  - Charlie and others recommend staying on PyTorch 2.7.1 instead of 2.9.0+cu128 to avoid issues
  - *From: Charlie*

- **VRAM usage with high frame counts**
  - 177 frames can cause memory issues depending on GPU VRAM, images get converted to 32bit
  - *From: Gateway*

- **RAM allocation issues**
  - 29.3 GiB array allocation errors possible with large generations, use --cache-none flag
  - *From: BestWind*

- **RAM usage for Wan 2.2 14B training**
  - Extremely high RAM usage shown in RunPod training
  - *From: Drommer-Kille*

- **Krea realtime inference speed**
  - 11fps using 4 inference steps on single NVIDIA B200 GPU
  - *From: Dever*

- **MoCha is heavy model to run**
  - Requires significant resources, need to limit input frames
  - *From: Kijai*

- **MoCha VRAM usage**
  - About double normal usage due to frame concatenation, 11GB with fp8 at default resolution
  - *From: Kijai*

- **Krea performance on RTX 4090**
  - 140 seconds 720p video generated in ~140 seconds
  - *From: aipmaster*

- **Sage attention GPU compatibility**
  - Requires SM89 compute capability, RTX 6000 PRO not compatible
  - *From: HeadOfOliver*

- **32GB RAM not enough for some workflows**
  - 32GB system RAM insufficient for Wan 2.2 workflows, especially with upscaling
  - *From: Kijai*

- **RTX 5090 shouldn't need tiled VAE**
  - Unless doing huge resolutions, tiled VAE shouldn't be necessary
  - *From: Kijai*

- **VAE uses ~10GB VRAM normally**
  - Normal VRAM usage for VAE decoding, but not used simultaneously with model
  - *From: Kijai*

- **CUDA version compatibility**
  - Issues arise with CUDA versions less than 12, though 11.8 can work with proper path configuration
  - *From: Lodis*

- **VAE encoding overhead**
  - Multiple frame processing requires VAE decode/encode cycles which increases memory usage
  - *From: CJ*

- **SVI memory usage**
  - No additional VRAM/memory requirements, just LoRA weights
  - *From: Kijai*

- **Long Ditto generations**
  - 24GB VRAM and 128GB system RAM recommended for extended video generation
  - *From: JohnDopamine*

- **Wan 2.2 VAE speed**
  - 2.2 VAE is not fast, lightweight alternatives provide speed at quality cost
  - *From: Kijai*

- **WSL memory configuration**
  - Need to manually configure memory limits in .wslconfig, default allocation insufficient
  - *From: seitanism*

- **WSL memory overhead**
  - WSL uses significant RAM overhead compared to dual boot Linux, 3x slower performance possible with VRAM saturation
  - *From: seitanism*

- **Q8 model + VACE memory usage**
  - Q8 quantized model combined with VACE module requires substantial RAM
  - *From: seitanism*

- **Blackwell GPU driver needs**
  - Latest drivers needed for new Blackwell GPUs at launch, Ubuntu prebuilt drivers usually outdated
  - *From: Kijai*

- **HoloCine model size**
  - 57GB each for high and low noise models in fp32
  - *From: Tachyon*

- **96GB VRAM recommendation**
  - VK suggests 96GB VRAM needs to become norm for these large models
  - *From: VK (5080 128gb)*

- **3090 insufficient for newer Wan models**
  - Can't really push newer Wan models through on 3090
  - *From: TimHannan*

- **SSD performance issues**
  - M.2 SSDs reading at 300-500MB/s instead of advertised 7000MB/s affecting model loading times
  - *From: seitanism*

- **165 frames at 1280x720**
  - Took 36 minutes with 5090
  - *From: Drommer-Kille*

- **245 frames at 960x540**
  - Requires full blockswap for VRAM handling
  - *From: Hashu*

- **HoloCine models**
  - 57GB for both low and high models
  - *From: Koba*

- **fp8_scaled performance**
  - Works with unmerged loras, no significant degradation observed
  - *From: Kijai*

- **HoloCine sparse model VRAM**
  - 30.5GB VRAM with 20 blockswap for 281 frames at 832x480
  - *From: mamad8*

- **Normal 2.2 generation**
  - Max 18.625 GB allocated memory for 241 frames at 832x480 with 6 total steps
  - *From: Kijai*

- **SVI training hardware**
  - Requires medium GPU cluster - authors used 8 to 64 GPUs for training
  - *From: Ablejones*

- **RTX 4090 for 30 second generation**
  - With swap block 40, takes about 500 seconds generation time
  - *From: avataraim*

- **20 minutes for 350 frame generation**
  - Using context overlap method
  - *From: VK*

- **7 minutes for 255 frames**
  - Without context overlap
  - *From: VK*

- **HoloCine VRAM usage**
  - Takes about 70GB VRAM for 480p, 720p crashes on Pro 6000
  - *From: BNP4535353*

- **HoloCine generation speed**
  - 1 hour for 16 seconds on official GitHub implementation, 25% faster with Flash Attention 2.8.3
  - *From: BNP4535353*

- **Wan 2.2 720p benchmark**
  - 189 frames in 142s on H800
  - *From: Ada*

- **LongCat VRAM with offloading**
  - 4090 needs about half offloaded for bf16, full offload under 10GB. 93 frames 640x608 16 steps: max 19.014 GB
  - *From: Kijai*

- **Holocine memory requirements**
  - 241 frames at higher res OOMs at 24GB VRAM + 64GB RAM, requires all frames in VRAM at once
  - *From: Cseti*

- **Holocine checkpoint size**
  - Checkpoints more than 50GB each, FP8 versions available to reduce size
  - *From: Fawks*

- **HoloCine VRAM usage**
  - Around 18GB VRAM usage with swap block 20
  - *From: avataraim*

- **LongCat generation times at 640x384**
  - 5 steps: 45 sec, 10 steps: 75 sec, 15 steps: 110 sec
  - *From: avataraim*

- **SageAttention 2.2.0 Windows requirement**
  - Windows only, requires Python 3.10
  - *From: avataraim*

- **LongCat VRAM usage**
  - Around 17GB VRAM with 30 blocks swapped for 832x480 at 97-149 frames on 24GB card
  - *From: JohnDopamine*

- **LongCat generation speed**
  - 166 seconds for i2v on RTX 4090, about 2-3 minutes for 15 second videos
  - *From: JohnDopamine*

- **LongCat speed issues on RTX 5090**
  - Initially 64s/it, then dropped to 25s/it, performance seems inconsistent
  - *From: Zabo*

- **Native vs ComfyUI speed difference**
  - Native takes 50 minutes per gen, ComfyUI takes only 2-3 minutes for same content
  - *From: avataraim*

- **50+ GB model causing OOM at 1280p**
  - 1280p resolution causes out of memory issues with full precision model, 832x480 works fine
  - *From: BNP4535353*

- **Model precision affects speed significantly**
  - Loading at full precision makes generation much slower with most data offloaded
  - *From: Ada*

- **High-end GPU for large resolutions**
  - User with 96GB VRAM can handle 720p, 5090 limited to 832x480 for 253 frames or 1280x720 for 161 frames
  - *From: BNP4535353*

- **RAM consumption significant**
  - Biggest consumption is actually RAM rather than GPU memory for high resolution generation
  - *From: BNP4535353*

- **RAM usage for WAN 2.2**
  - WSL2 peaks at 92GB RAM with wan high/low (about 16+16+10+1GB models plus overhead)
  - *From: pagan*

- **3090ti for LoRA training**
  - 24GB VRAM, but needs to rent GPUs for large datasets (550 videos, 121 frames each)
  - *From: Kiwv*

- **Memory management recommendation**
  - 256GB RAM ordered for $720 to solve memory issues
  - *From: seitanism*

- **LongCat VRAM usage**
  - 11GB VRAM with 30 blocks swapped, 20GB without swapping on 5090
  - *From: Kijai*

- **LongCat generation time**
  - Around 20 minutes for 16 steps on 5090, 13:54 for 10 steps
  - *From: Kijai*

- **4090 with 128GB system RAM performance**
  - Max memory 11.084GB, generation in 503.10 seconds
  - *From: JohnDopamine*

- **TensorRT interpolation performance**
  - 3 second interpolations when properly set up
  - *From: voxJT*

- **Torch compile VRAM impact**
  - Can increase VRAM usage by 50% while reducing speed, user saw 15.5GB+2 shared vs 11.3GB plain
  - *From: Gleb Tretyak*

- **High resolution Wan2.2 generation**
  - 1200x960x5sec used 12.5GB peak VRAM on RTX 4070 Ti Super (16GB VRAM)
  - *From: Gleb Tretyak*

- **Tested resolutions**
  - Users successfully generated up to 1920x640 (wide angle) and 1600x900, 720p recommended for quality
  - *From: hudson223*

- **Block swap VRAM tradeoff**
  - 600MB LoRA with 20 block swap now uses 300MB more VRAM but moves with block swap for better performance
  - *From: Kijai*

- **ChronoEdit VRAM**
  - At least 5 frames at 1024x1024 with Wan I2V requirements
  - *From: Kijai*

- **Chinese GPU alternatives**
  - Huawei Atlas 300I DUO: 96GB VRAM for $1.5k but much lower TOPS performance vs NVIDIA RTX 6000 Pro at $10k
  - *From: Aaron_PhD*

- **BF16 support**
  - Requires at least 30xx series for BF16, older cards need FP16 conversion
  - *From: Lodis*

- **ChronoEdit model size**
  - 32GB for full model
  - *From: xwsswww*

- **LongCat VRAM usage**
  - Barely uses 60% VRAM with higher resolution and more frames vs WAN bringing close to OOM
  - *From: Pandaabear*

- **LongCat base precision**
  - Needs bf16, doesn't work on fp16
  - *From: Kijai*

- **GPU pooling with Raylight**
  - Get 60-70% performance of second card added to first card inference speed, but downgrades faster card to match slower card
  - *From: Kinasato*

- **4x 5090 setup considerations**
  - 600W x 4 is an issue with 5090s, RTX 6000 Pro might be better alternative
  - *From: Ada*

- **Multi-GPU VRAM pooling**
  - No way to pool VRAM of GPUs, but nice for training. One 5090 is plenty for inference unless doing LLMs
  - *From: Lumifel*


## Community Creations

- **After Effects plugin for VACE inpainting** (tool)
  - Custom plugin for easy VACE inpainting workflows
  - *From: SonidosEnArmonía*

- **Batch resize with configurable batch sizes** (node)
  - Modified resize node that processes giant batches in smaller chunks
  - *From: stenandrimpy*

- **Updated wrapper preprocessing example** (workflow)
  - Updated example workflow using new preprocessing nodes
  - *From: Kijai*

- **Modified QWen VL Object Detection** (tool)
  - Allows model unloading, creates bboxes for face detection workflows
  - *From: piscesbody*

- **Face bbox output for preprocessing** (node)
  - Added face bbox output to existing preprocessing workflow for easier face swapping
  - *From: Kijai*

- **Wanx Troopers documentation site** (documentation)
  - GitHub organization for condensed documentation and tidbits, accepts PRs
  - *From: 42hub*

- **Blockify GPU optimization** (node improvement)
  - Rewrote blockify code in pytorch with GPU device option for massive speed improvements
  - *From: Kijai*

- **AI Toolkit blockswapping implementation** (feature)
  - Built-in blockswapping that offloads to CPU during training
  - *From: Ryzen*

- **HuMO I2V fix** (patch)
  - PR submitted to enable proper I2V functionality in HuMO
  - *From: Ablejones*

- **New checkpoint with Lightning LoRAs** (model)
  - Best 2.2 results with great motion, prompt following, includes light LoRAs without motion loss
  - *From: Ada*

- **ComfyUI-Upscale-CUDAspeed** (tool)
  - High-performance CUDA-accelerated upscaling plugin with multi-GPU support and Tensor Core optimization
  - *From: piscesbody*

- **Wan 2.2 character LoRAs** (lora)
  - Character training using diffusion-pipe repo, 950 images same cosplayer, rank 32, 5e-5 learning rate
  - *From: Kytra*

- **Music analysis suite** (nodes)
  - Custom nodes with 3 algorithms for music analysis, accounting for frame drift
  - *From: Fill*

- **Matrix bullet time effect** (workflow)
  - 1:1 recreation using Wan 2.1 and VACE for interpolation between 10 camera frames
  - *From: Neex*

- **WanAnimate V2 workflow** (workflow)
  - Updated example workflow using preprocessing nodes
  - *From: Kijai*

- **Smooth Mix Wan 2.2 model** (model)
  - Merged model optimized for frame interpolation
  - *From: Community*

- **Radial Length Helper node** (tool)
  - Makes snapped values based on input and gives list of valid lengths for resolution calculation
  - *From: hudson223*

- **ComfyUI_RH_Ovi** (node)
  - ComfyUI implementation for OVI model by RunningHub
  - *From: slmonker(5090D 32GB)*

- **Midas VFX relight system** (tool)
  - Face embedding integrated relight system with self-shadowing capabilities, work-related so cannot be shared
  - *From: Mads Hagbarth Damsbo*

- **Curly hair LoRA** (lora)
  - Special LoRA trained for curly hair since base models don't handle it well
  - *From: Thom293*

- **USDU workflow for video extension fixing** (workflow)
  - Complex workflow using USDU upscale in latent space to fix seams and quality issues in extended videos
  - *From: mdkb*

- **WanVideo Scheduler visualization** (node)
  - Helps visualize sigma values and understand shift parameter effects
  - *From: Kijai*

- **LoRA extraction and pruning tools** (tool)
  - Extract similar models as LoRAs and prune existing LoRAs to reduce storage
  - *From: woctordho*

- **OVI native implementation** (node)
  - Native ComfyUI implementation of OVI with proper model loading/patching
  - *From: Kytra*

- **Flux bokeh LoRA** (lora)
  - Swirl bokeh only - trained on specific lens effects
  - *From: slmonker(5090D 32GB)*

- **Easy WAN 2.2 latent upscale article** (workflow)
  - PDF article about latent upscale and boosting video generation speed by 3–4×
  - *From: Lan8mark*

- **2K video upscaler with WAN 2.2** (workflow)
  - 160 seconds to upscale from 720p to 1440p
  - *From: Lan8mark*

- **WanMoeKSampler with CFG guidance** (node)
  - Fixed sigma_shift/step split with added CFG guidance and tooltips
  - *From: GalaxyTimeMachine (RTX4090)*

- **rCM LoRA extraction** (lora)
  - Extracted LoRA version of rCM consistency model for Wan
  - *From: Kijai*

- **WAN upscaler workflow** (workflow)
  - Handles high-quality upscaling from 720p/360p to 2K with improved stability
  - *From: Lan8mark*

- **ComfyUI Essentials fork** (tool)
  - Modified version with small changes to nodes for upscaler workflow
  - *From: Lan8mark*

- **MAGREF WAN 2.2 integration** (workflow)
  - Multi-character consistency solution for I2V generation
  - *From: Elvaxorn*

- **SEC ComfyUI nodes** (node)
  - Enhanced SAM2 guidance nodes for better video segmentation
  - *From: ArtOfficial*

- **Tiny VAE loader node** (node)
  - Loader for TAE VAE in WanVideoWrapper for faster preview
  - *From: Kijai*

- **RCM LoRA** (lora)
  - Distillation LoRA by Nvidia devs for speed without motion loss
  - *From: JohnDopamine*

- **Kijai's extracted Lightx2v LoRA** (lora)
  - Properly extracted version of the official LoRA that actually works
  - *From: Kijai*

- **WanMoE KSampler with skimmed CFG** (node)
  - Fork of MoE sampler with added CFG adjusting capabilities
  - *From: GalaxyTimeMachine*

- **Kijai's LightX2V High LoRA extraction** (lora)
  - 64 rank LoRA extracted from full model with additional patches missing from original release
  - *From: Kijai*

- **AI Toolkit video training** (tool)
  - Used locally to train Wan 2.2 for specific tricks like skateboard Tre Flip
  - *From: Drommer-Kille*

- **Pusa LoRA** (lora)
  - Allows Wan T2V model to use input images for I2V or frame extension
  - *From: Kijai*

- **CFG Helper Node** (node)
  - Node for creating complex CFG schedules in workflows
  - *From: Kijai*

- **Text Encode Cache Node** (node)
  - Caches text encodings to file to prevent OOM issues
  - *From: mdkb*

- **PyTorch 2.9.0 VAE workaround** (code fix)
  - Workaround that does conv3d in fp32 to bypass PyTorch bug while minimizing VRAM usage
  - *From: Kijai*

- **Video stitching workflow with VACE** (workflow)
  - Uses VACE frame inpainting to connect video segments with temporal consistency
  - *From: Koba*

- **Batch video processing setup** (workflow)
  - Uses load video node and meta batch manager for long video upscaling
  - *From: happy.j*

- **Two-video pose concatenation system** (tool)
  - Concatenates 3D pose estimations from two videos into 2D space with controllable mixing strength
  - *From: Mads Hagbarth Damsbo*

- **WAN 2.2 Mega Rapid AIO GGUF conversion** (model)
  - Converted fp8 model to q5km, q4km, q3km formats - q4 looks similar to fp8 but uses less storage (10.8GB vs 16.1GB)
  - *From: patientx*

- **Car LoRA training** (lora)
  - Trained WAN LoRA on 10 images of same green car, learned impressive details but limited color flexibility
  - *From: Dever*

- **Cartoon style LoRA** (lora)
  - Custom trained cartoon style LoRA for Wan
  - *From: The Shadow (NYC)*

- **WanVideoWrapper memory dump tool** (tool)
  - Tool for generating memory dumps, works on Linux with cuda malloc disabled
  - *From: Kijai*

- **Clownshark temporal mask workflow** (workflow)
  - Complex workflow using clownshark sampler with temporal masks for regional conditioning
  - *From: TK_999*

- **Ditto LoRAs resized to lower rank** (lora)
  - Kijai resized original rank 128 LoRAs to average rank 29 for easier sharing and usage
  - *From: Kijai*

- **Ditto LoRA extraction** (technique)
  - Method for extracting LoRAs from full modules using LoraExtractKJ node
  - *From: Kijai*

- **Krea realtime LoRA** (lora)
  - Extracted LoRA from Krea realtime model for use with Wan 2.2
  - *From: aipmaster*

- **Image concatenation workflow** (workflow)
  - Workflow for comparing results side by side with prompts overlay
  - *From: Kijai*

- **Extracted Krea realtime LoRA** (lora)
  - 2.5GB LoRA extracted from Krea realtime model for use with Wan 2.2
  - *From: aipmaster*

- **Colab tunneling code** (script)
  - Code to use built-in colab tunneling for ComfyUI instead of external services
  - *From: Draken*

- **WanVideoWrapper MoCha support** (node)
  - Kijai implemented MoCha in ComfyUI WanVideoWrapper
  - *From: Kijai*

- **Aipmaster's Krea workflow** (workflow)
  - Complete workflow using Krea LoRA with dual sampling for realistic results
  - *From: aipmaster*

- **VAE conversion script** (tool)
  - Claude-generated script to reverse convert diffusers VAE format to ComfyUI format
  - *From: Kijai*

- **Ditto global style LoRA** (lora)
  - Powerful style transfer for video, can change entire anime episodes to different styles
  - *From: JohnDopamine*

- **Loop nodes for context sliding** (workflow)
  - Automated I2V chaining using ComfyUI's general loop nodes for continuous video generation
  - *From: Kijai*

- **WanVideoWrapper** (node)
  - Kijai's ComfyUI wrapper for Wan video models
  - *From: seitanism*

- **Wanx Troopers knowledge base** (tool)
  - Community-maintained update tracker for Wan ecosystem
  - *From: 42hub*

- **SVI workflow adaptations** (workflow)
  - Community adaptations of SVI for different Wan model versions
  - *From: Dever*

- **Custom mask input node** (node)
  - Allows manual mask specification for native ComfyUI video generation
  - *From: Ablejones*

- **SVI LoRA conversions** (model conversion)
  - Converted SVI LoRAs from fp32 diffsynth format to fp16 safetensors for native ComfyUI
  - *From: Kijai*

- **VK's SVI extension workflow** (workflow)
  - Improved method using reference image as first frame for better consistency in video extension
  - *From: VK (5080 128gb)*

- **Suplex LoRA** (lora)
  - Wrestling suplex move LoRA uploaded to Civitai
  - *From: Lodis*

- **HoloCine sparse model implementation** (tool)
  - Experimental implementation of sparse model for long video generation
  - *From: mamad8*

- **Seamless video workflow with auto frame removal** (workflow)
  - Automatically removes stray frames for seamless output
  - *From: VK (5080 128gb)*

- **Holocine experimental workflow** (workflow)
  - ComfyUI workflow for Holocine using video attention split method
  - *From: avataraim*

- **Mamad8's Holocine implementation** (custom implementation)
  - Implementation of Holocine split prompting + sparse inter-shot self attention in wrapper
  - *From: mamad8*

- **LightX quantile 0.15 LoRA** (lora)
  - Distillation LoRA by Kijai for faster inference
  - *From: Kijai*

- **LongCat distill LoRA merge** (lora)
  - Kijai merged the distill LoRA by renaming layers and splitting fused qkv components
  - *From: Kijai*

- **Ovi 512x512 hack** (workflow)
  - Modified ovi_fusion_engine.py area calculations for faster 512x512 generation
  - *From: reallybigname*

- **Holocine ComfyUI nodes** (node)
  - WanVideoHolocineShotBuilder, WanVideoHolocinePromptEncode, WanVideoHolocineSetShotAttention nodes
  - *From: shaggss*

- **LongCat ComfyUI wrapper** (node)
  - Implementation in WanVideoWrapper for LongCat model support
  - *From: Kijai*

- **SageAttention 2.2.0 Windows wheel** (tool)
  - Pre-built wheel for Windows Python 3.10 users
  - *From: avataraim*

- **HoloCine ComfyUI integration** (node)
  - Pull request adding HoloCine support to WanVideoWrapper
  - *From: Kijai*

- **MediaSyncer improvements** (tool)
  - Side by side video comparison, zooming fills letterboxing, A-B loop option, handles 12+ videos simultaneously
  - *From: phazei*

- **SageAttention Windows wheel** (tool)
  - Windows wheel for SageAttention 2.2.0 with torch compile support
  - *From: avataraim*

- **FP32 to FP8 conversion script** (script)
  - Claude Opus scripted converter for fp32 to fp8 checkpoints
  - *From: JohnDopamine*

- **Wan 2.1 VAE 2x upscaler** (model)
  - Trained VAE decoder that upscales 2x and reduces noise patterns
  - *From: spacepxl*

- **ComfyUI-VAE-Utils** (node)
  - Custom VAE loader and decode nodes for upscaling workflows
  - *From: spacepxl*

- **HuMo i2v mode modifications** (patch)
  - Custom changes to allow HuMo to work in i2v mode
  - *From: Ablejones*

- **WanImageToVideo batch masks node** (node)
  - Allows WanImageToVideo node to work with batch of masks for svi-film
  - *From: Ablejones*

- **LongCat refinement LoRA** (lora)
  - Improves video generation quality when used with specific sampling parameters
  - *From: Kijai*

- **WAN 2x VAE** (model)
  - Provides significant quality improvements with better detail and sharpness
  - *From: spacepxl*

- **Video extension helper node** (node)
  - Being developed to simplify video extension workflows
  - *From: Kijai*

- **24fps-ifier WAN LoRA** (lora)
  - Planned LoRA to make WAN work at 24fps for faster paced content, using 550 videos dataset with 121 frames each
  - *From: Kiwv*

- **Uncensoring LoRA for WAN** (lora)
  - Large dataset LoRA project using 550 videos from r34, manually captioned, to completely uncensor WAN
  - *From: Kiwv*

- **WanVideoWrapper LongCat support** (node)
  - ComfyUI wrapper supporting LongCat model with extended video workflows
  - *From: Kijai*

- **LLM-assisted segment prompting workflow** (workflow)
  - Uses LLM to generate prompts for next video segments based on last frame
  - *From: JohnDopamine*

- **LightX2V 1030 LoRA extraction** (lora)
  - Community member extracted LoRA from full model since official ComfyUI-compatible version wasn't initially available
  - *From: DawnII*

- **WanVideo ComfyUI integration update** (node)
  - Major update including LongCat support, improved LoRA handling, and fp32 norm layers
  - *From: Kijai*

- **ChronoEdit ComfyUI conversion** (model)
  - Converted NVIDIA ChronoEdit to ComfyUI format with distill LoRA
  - *From: Kijai*

- **LightX2V 1030 LoRA** (lora)
  - Third iteration 2.2 high noise distill LoRA with better prompt adherence and camera control
  - *From: Kijai*

- **ChronoEdit distill LoRA** (lora)
  - Distill LoRA for ChronoEdit functionality with Wan models
  - *From: Kijai*

- **wan2.2_lightx2v_1030** (lora)
  - New high noise speed LoRA for 4 steps, rank 64, bf16
  - *From: avataraim*

- **LongCat face consistency workflow** (workflow)
  - Uses face inpaint with Phantom to maintain character identity in video extensions
  - *From: Ablejones*

- **LongCat refinement LoRA** (lora)
  - LongCat_refinement_lora_rank128_bf16.safetensors for assisting upscaling
  - *From: Kijai*
