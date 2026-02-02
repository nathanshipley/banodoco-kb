# Ltx Gens Knowledge Base
*Extracted from Discord discussions: 2026-01-01 to 2026-02-01*


## Technical Discoveries

- **LTX Video 2 supports text-to-video generation with audio**
  - Model generates both video and audio simultaneously in T2V mode
  - *From: Multiple users*

- **Old LoRAs from LTX 0.97 are compatible with LTX Video 2**
  - NebSH confirmed compatibility and demonstrated multiple LoRAs working without conversion
  - *From: NebSH*

- **Model has strong cartoon/animation memorization**
  - Generates perfect Peppa Pig voices and characters, Amazing World of Gumball style, SpongeBob recognition
  - *From: Phr00t*

- **LTX 2 supports multiple languages for audio generation**
  - French audio generation confirmed working with proper accents
  - *From: Vérole*

- **NebSH's 0.97 camera LoRAs work with LTX-2 out of the box**
  - Old 0.9x LoRAs applied to LTX-2 work without processing - tested 62 different camera motion LoRAs including dolly out, 360 orbit, whip pan, crash zoom, dutch angle, etc.
  - *From: NebSH*

- **Vertical motion works better with specific prompting techniques**
  - Describing mouth movement and other specific movements creates better results than just prompting 'she says...' which didn't move image at all
  - *From: gopnik*

- **LTX-2 can generate music and sound effects**
  - Model acts as music generator - can create realistic sound effects and music matching video content
  - *From: Fictiverse*

- **Scene transitions need 2-3 seconds between cuts to avoid confusion**
  - Model leans towards one long shot rather than cutting scenes, needs adequate time between transitions
  - *From: cyncratic*

- **BF16 has considerable quality difference over FP8**
  - Noticeable quality improvement when using BF16 full model versus FP8 quantized version
  - *From: NebSH*

- **Short prompts work better when given audio input**
  - Simple prompts like 'A punk rock music video in a public bathroom. A Man wearing sunglasses and a leather jacket' work well with audio latents
  - *From: 305792526629994496*

- **Distill LoRA affects skin rendering**
  - The model likes to make shiny skin, and the distill lora might have an impact on this
  - *From: Owlie*

- **Using different LoRA configurations affects output**
  - Comparison shows detailer lora on stage 1 vs stage 2 vs both stages produces different results
  - *From: gopnik*

- **LTX2 can handle multi-language audio**
  - Model performs well with German and French language generation, with some spelling complexities in French
  - *From: gopnik*

- **Big negative prompts can cause stuttery outputs**
  - Large default negative prompts may be causing stuttery video outputs
  - *From: TK_999*

- **Model supports audio conditioning and masking**
  - Can use audio masking to preserve original audio in specific time ranges
  - *From: Dragonyte*

- **CFG1 distilled models ignore encoding, so can reuse single encoding to save time**
  - When using distilled models with CFG1, the encoding is ignored anyway, so you can reuse a single encoding to save processing time
  - *From: TK_999*

- **LTX2 might work as world model base**
  - LTX2 could potentially be used as a foundation for world models in the future
  - *From: TK_999*

- **Music has big effect on motion speed**
  - The audio/music input significantly affects the speed and intensity of generated motion in videos
  - *From: Benjimon*

- **No background gives better results**
  - Cropping out backgrounds or using no background naturally seems to produce better generation results
  - *From: JUSTSWEATERS*

- **Model can sync dancing to audio beat**
  - LTX2 can generate dancing that is timed to the beat of input audio
  - *From: Marco_vdm*

- **Distilled model needs adjustment for better quality**
  - To avoid plastic look with distilled model, add detail LoRA on both samplers, reduce distilled LoRA to 0.6, and use detail daemon with enhance image node
  - *From: dj47*

- **Grid patterns appear in dark scenes**
  - Strong grid patterns visible in dark scenes, can be adjusted with LTXV Spatio Temporal Tiled VAE Decode settings
  - *From: garbus*

- **Natural looking breathing makes videos appear more alive**
  - Breathing animation improves realism in character videos
  - *From: Rainsmellsnice*

- **Changed fps from 24 to 25 fixed temporal jerkyness**
  - Temporal upscaler expects 25 fps, works even at high frame counts like 461 frames
  - *From: HeadOfOliver*

- **Empty audio latent for upscale stage improves audio quality**
  - Instead of running first stage audio latent output into upscale, use new empty audio latent for better i2v audio
  - *From: dischordo*

- **Negative distill lora at -0.50 removes film grain**
  - Using negative distill lora strength helps remove excessive film grain and damage artifacts
  - *From: Nathan Shipley*

- **FlowMatchEuler scheduler maintains sharpness in long videos**
  - FlowMatch scheduler doesn't degrade video quality over time, keeps sharp last frames even on 15 steps
  - *From: neofuturo*

- **Increasing FPS helps reduce blur and improve detail quality**
  - Higher FPS makes videos less blurry and increases detail, but reduces effective video length you can render
  - *From: GalaxyTimeMachine (RTX4090)*

- **LTX2 can generate stereo audio with spatial positioning**
  - Model supports stereo audio generation and has some sense of spatial audio positioning
  - *From: ezMan*

- **Detail LoRA is primarily for v2v upscaling**
  - Detail LoRA is more used with video-to-video upscaling rather than initial generation
  - *From: The Shadow (NYC)*

- **Motion blur may be from overtrained dataset or latent space compression**
  - The mushiness/motion blur issues could be from being overtrained on motion blur or a side effect of latent space compression
  - *From: nikolatesla20*

- **LTX2 doesn't need large datasets for camera/effect LoRAs**
  - Can train effective camera movement and effect LoRAs with as few as 6 generated AI videos
  - *From: NebSH*

- **Audio generation may be random when not explicitly prompted**
  - Background music generation appears random when audio description isn't included in prompt
  - *From: ezMan*

- **Distilled 8-step with custom sigmas works well**
  - Using er_sde sampler with distilled model and 8-step custom sigmas produces high quality results
  - *From: GalaxyTimeMachine (RTX4090)*

- **48fps conditioning gives less blurry speech generation**
  - Using 48fps as conditioning frame rate reduces blur during speech, then can export back to 24fps for cinematic feel
  - *From: ucren*

- **Distilled LoRA with negative strength improves likeness**
  - Using distilled LoRA at negative strength (like -0.4) helps fix overbaked distilled model and improves face consistency
  - *From: ucren*

- **Multiple frame extension workflow (FFLF) works well**
  - First, middle, last frame workflow with multiplier node allows adding more frames for extensions
  - *From: neofuturo*

- **LTX2 knows character voices well**
  - Model can generate Rick and Morty voices without pre-generated audio clips, just from prompting
  - *From: herpderpleton*

- **Inpainting maintains better likeness**
  - Using inpainting/extending with many latent samples helps maintain face consistency better than straight generation
  - *From: ucren*

- **Audio latent strength can be reduced**
  - Using latent multiply at 0.75 strength on audio latent reduces exaggerated expressions
  - *From: ucren*

- **Second masked upscale pass improves audio sync**
  - Adding a second masked upscale pass significantly helps with audio extend/clone quality
  - *From: ucren*

- **Distilled model can be 'debaked' using distill LoRA at negative values**
  - Using distill LoRA at -0.4 makes a huge difference on plastic skin issues
  - *From: ucren*

- **GGUF lipsync solution found**
  - Use one stage Kijai-based workflow with GGUF distilled model, distilled lora at -0.3, and normal connector on clip (not distilled)
  - *From: Alpha-Neo*

- **Frame count formula discovered**
  - Frame count must be 8n+1 (e.g., 241 frames for 10 seconds at 24fps)
  - *From: N0NSens*

- **Tiled VAE decoding causes visible grid patterns in dark scenes**
  - Grid patterns appear as double lines where tiles overlap, visible in dark scenes but masked in bright areas
  - *From: ucren*

- **Audio normalization issues in v2v extend**
  - Huge volume changes and distortion occur when using v2v extend functionality
  - *From: U̷r̷a̷b̷e̷w̷e̷*

- **Two-stage vs one-stage workflow differences**
  - One stage workflow has better camera adherence and prompt following, two-stage is hit and miss
  - *From: Alpha-Neo*

- **LTX2 can handle very long videos with RTX 5090**
  - 5090 can generate 1000 frames at 1280x720 resolution
  - *From: NebSH*

- **Frame injection technique for controlled transitions**
  - Can inject 3-5 frames at specific frame indexes for precise control over video transitions
  - *From: neofuturo*

- **Camera static LoRA combined with negative distill LoRA improves stability**
  - Camera static LoRA at 0.5 and distill LoRA at -0.3 resolved camera static issues
  - *From: mdkb*

- **Audio-to-video works well with musical content**
  - Model shows good audio reactivity and can generate music videos from audio input
  - *From: multiple users*

- **Dev model with distill LoRA at lower strength reduces oversaturation**
  - Using dev model with distill LoRA at 0.6 helps control oversaturation compared to pure distilled model
  - *From: U̷r̷a̷b̷e̷w̷e̷*

- **Charlie generated 1500 frames in one go with LTX2**
  - Successfully generated 1500 frames in a single generation
  - *From: Charlie*

- **Direct resolution at 1504/832 gives better motion than 1280/720 then upscale**
  - First pass at higher resolution produces better motion quality than upscaling from lower resolution
  - *From: Vérole*

- **Charlie can do 2000 frames in 1 go**
  - Extended frame generation capability demonstrated
  - *From: Charlie*

- **LTX2 supports text-to-image generation**
  - Model can generate static images as well as video, described as realistic
  - *From: hicho*

- **Prompt structure affects i2v vs t2v behavior**
  - Simple prompts like 'woman is walking and sings' maintain i2v mode, complex prompts not matching reference image switch to t2v mode
  - *From: hicho*

- **Audio prompting order matters for speech generation**
  - Structure like 'person speaks in harsh low voice and says' works better than 'person speaks saying [text] in harsh low voice'
  - *From: U̷r̷a̷b̷e̷w̷e̷*

- **T2AV (text-to-audio-video) prompting works well**
  - Single pass t2v audio prompting produces good results
  - *From: 152993277631528960*

- **Heavy noise helps LTX output quality**
  - Adding noise to input improves generation results
  - *From: 152993277631528960*

- **Keeping everything in silhouette avoids artifacts**
  - Silhouette approach reduces visual artifacts in generations
  - *From: 152993277631528960*

- **Motion LoRA on first pass produces better results**
  - Using motion LoRA at 1920/1088 first pass then upscale preferred over preprocessor on first stage
  - *From: Vérole*

- **LTX2 knows Super Mario Bros Super Show content**
  - Key phrase 'A cartoon from the Super Mario Bros Super Show' enables character generation from that series
  - *From: U̷r̷a̷b̷e̷w̷e̷*

- **Using dev+lora at 0.6 strength helps maintain face quality during camera rotation**
  - User reports improved face consistency when using this configuration
  - *From: U̷r̷a̷b̷e̷w̷e̷*

- **IC detailer lora at 0.5 strength works for T2V but breaks I2V/V2V**
  - Using IC detailer lora on I2V or V2V messes up matching and changes faces significantly
  - *From: U̷r̷a̷b̷e̷w̷e̷*

- **Static camera control lora helps prevent camera wandering**
  - Testing shows it definitely helps keep the camera from moving unexpectedly
  - *From: Benjimon*

- **New LTX Multimodal Guider shows significant improvement over old guider**
  - Comparison shows dramatically better results with the new guider
  - *From: garbus*


## Troubleshooting & Solutions

- **Problem:** I2V outputs static for 3 seconds then deforms
  - **Solution:** Lower noise mask to 0.6 (strength parameter on native workflow)
  - *From: Dragonyte*

- **Problem:** Out of memory errors on first run
  - **Solution:** Run batch of 2 - first will fail, second will work
  - *From: VK (5080 128gb)*

- **Problem:** CLIP encoder causing OOM errors
  - **Solution:** Use fp8 gemma 3 model
  - *From: Phr00t*

- **Problem:** Audio quality is tinny/wonky
  - **Solution:** Listed as known issue, no solution provided yet
  - *From: burgstall*

- **Problem:** OOM/crashes during VAE decode on longer videos
  - **Solution:** Use tiled VAE decode, increase RAM, or reduce resolution/frame count
  - *From: Tachyon*

- **Problem:** Tensor mismatch in native workflow
  - **Solution:** Use shared working workflows from community members
  - *From: HeadOfOliver*

- **Problem:** Model occasionally produces slideshow-like images with no motion
  - **Solution:** Unknown trigger, appears random in automatic scene generation
  - *From: Simonj*

- **Problem:** Green squares appear on screen during high-resolution long renders
  - **Solution:** Reboot system - likely unstable overclock/downvolt issue
  - *From: 305792526629994496*

- **Problem:** Custom audio not working
  - **Solution:** Issue with custom audio functionality, still unresolved
  - *From: VRGameDevGirl84(RTX 5090)*

- **Problem:** Static video with short prompts
  - **Solution:** Use longer, more detailed prompts. Short prompts result in static videos that barely move
  - *From: VRGameDevGirl84(RTX 5090)*

- **Problem:** Enhancer node causing errors
  - **Solution:** Remove the prompt enhancer node from workflow to fix mat1/mat2 errors
  - *From: GalaxyTimeMachine(RTX4090)*

- **Problem:** OOM errors on second sampler
  - **Solution:** Set aggressive tiling settings, use reserve VRAM setting at 6, ensure using FP8 models
  - *From: D'Squarius Green, Jr.*

- **Problem:** Face warping and eye issues in T2V
  - **Solution:** 
  - *From: gopnik*

- **Problem:** Preview mode causing mat1/mat2 errors
  - **Solution:** Disable preview mode to fix matrix multiplication errors
  - *From: gopnik*

- **Problem:** Cursed fingers with distilled model
  - **Solution:** Full model needs 40 steps to avoid cursed fingers, distilled gets it mostly right but changes the face
  - *From: 421114995925843968*

- **Problem:** Plastic look with distilled model
  - **Solution:** Add detail LoRA on both samplers, reduce distilled LoRA to 0.6, add detail daemon and enhance image node
  - *From: dj47*

- **Problem:** Grid patterns in dark scenes
  - **Solution:** Adjust LTXV Spatio Temporal Tiled VAE Decode settings - 2/8/16/8 appears best but doubles VRAM use
  - *From: garbus*

- **Problem:** Image degradation when using last frame for continuation
  - **Solution:** Still looking for solution to maintain continuation while avoiding degradation
  - *From: NebSH*

- **Problem:** Blotchy face in wider shots during character motion in I2V
  - **Solution:** No specific solution provided, user asking for advice
  - *From: Choowkee*

- **Problem:** I2V produces garbage with short prompts
  - **Solution:** LTX2 requires long prompts same as LTX 0.9.8 did - short prompts produce garbage
  - *From: cyncratic*

- **Problem:** Audio has hissing and distortion
  - **Solution:** Need more steps or different sampler during upscale, multistep/complex schedulers seem better
  - *From: garbus*

- **Problem:** Temporal jerkyness in upscaler above 241 frames
  - **Solution:** Change fps to 25 instead of 24, upscaler expects 25 fps
  - *From: HeadOfOliver*

- **Problem:** i2v was broken, generations taking longer
  - **Solution:** Use negative node in workflow, switch to ksampler approach
  - *From: hicho*

- **Problem:** Extend workflow spitting out input video
  - **Solution:** Install 2 prerequisites for gemma to work with gemma 3 model loader node
  - *From: Mazrael.Shib*

- **Problem:** Jerkyness every few frames
  - **Solution:** Decrease detail-lora strength or change fps to 25
  - *From: N0NSens*

- **Problem:** Background elements appearing jittery/boiling even with minimal movement
  - **Solution:** Use dpmpp_sde + normal (50% slower) or res_2s (4x slower) samplers
  - *From: Arts Bro*

- **Problem:** NoneType object has no attribute 'Params' on checkpoint node
  - **Solution:** Delete the 'ckpt_name' thing and select everything manually
  - *From: Zueuk*

- **Problem:** GEMMA model load destroys hardware on 3090
  - **Solution:** Try using quantized GEMMA or GGUF GEMMA
  - *From: Tachyon*

- **Problem:** Upscaling uses all 24GB VRAM regardless of GGUF model size
  - **Solution:** Model size doesn't affect latent frame buffer - VRAM usage depends on latent video frames at resolution, not model size
  - *From: Volkin*

- **Problem:** Image-to-video often produces still images
  - **Solution:** Use audio+image to video instead of just image to video for better motion
  - *From: Mazrael.Shib*

- **Problem:** Loss of lip sync with faster workflows
  - **Solution:** Speed improvements may come at cost of lip sync quality - trade-off between speed and sync
  - *From: Simonj*

- **Problem:** Face changes too much in I2V with audio
  - **Solution:** Use distilled LoRA at negative strength (-0.4 to -0.6), reduce audio latent strength to 0.75, and consider using non-famous faces
  - *From: ucren*

- **Problem:** Sage attention errors with FP32
  - **Solution:** Use KJ checkpoint loader to force FP16 loading to avoid sage switching to pytorch attention
  - *From: nikolatesla20*

- **Problem:** OOM errors on high resolution long videos
  - **Solution:** Use --reserve-vram 2.0 startup parameter and Kijai's Chunk Feed Forward node
  - *From: garbus*

- **Problem:** Motion artifacts in longer extensions
  - **Solution:** Higher conditioning fps (48fps) creates more motion artifacts in long extensions, 24fps conditioning works better for longer clips
  - *From: ucren*

- **Problem:** LTXVPREPROCESS node causing issues
  - **Solution:** Set LTXVPREPROCESS node to 0
  - *From: Jonathan Scott Schneberg*

- **Problem:** Tiled VAE decode grid artifacts in dark scenes
  - **Solution:** Increase tiled overlap to 256 or use non-tiled decoding with 1 tile and 0 overlap
  - *From: ucren*

- **Problem:** No lipsync with GGUF Q8 dev model
  - **Solution:** Use distilled model with distilled LoRA at -0.3 and normal clip connector
  - *From: Alpha-Neo*

- **Problem:** Frozen frame issues with GGUF at higher resolutions
  - **Solution:** Balance LTXImgToVideoInPlace (start at 0.4) and LTXVPreprocess (10-33, usually 25) settings
  - *From: mdkb*

- **Problem:** Audio volume inconsistency in v2v extend
  - **Solution:** Create audio normalization node that analyzes video before segment and auto-normalizes
  - *From: U̷r̷a̷b̷e̷w̷e̷*

- **Problem:** Prompt control varies between resolutions
  - **Solution:** Need to rebalance LTXImgToVideoInPlace and LTXVPreprocess when changing resolution
  - *From: mdkb*

- **Problem:** Character loses likeness in audio-driven video
  - **Solution:** Adjust mask timing - too early preserves likeness but loses mouth movement, too late gets movement but loses likeness
  - *From: Nekodificador*

- **Problem:** Video extension consistency issues and RAM problems
  - **Solution:** Use Kijai's new memory efficiency nodes and NAG for better control
  - *From: mdkb*

- **Problem:** Frame count error for video extension
  - **Solution:** Need 1 + 8 * x frames (e.g., 1, 9, 17, ...). Sometimes need to add +1 to frame count manually
  - *From: mdkb*

- **Problem:** Audio volume jumps when switching to LTX generation
  - **Solution:** Use audio enhancement and normalization nodes with auto mode that analyzes first 3 seconds of source audio
  - *From: U̷r̷a̷b̷e̷w̷e̷*

- **Problem:** High CFG causing artifacts
  - **Solution:** User had CFG set too high, switching back to CFG 1.0 for distilled model fixed artifacts
  - *From: Nekodificador*

- **Problem:** Color bug with vertical upscale outputs over 1536 pixels
  - **Solution:** Top and bottom get blue hue and hallucinations at high vertical resolutions
  - *From: dischordo*

- **Problem:** Frame count issues in video processing
  - **Solution:** Change inbound video to 146 frames or reduce cutoff frames in increments of 1 until finding working number
  - *From: mdkb*

- **Problem:** FPS related generation issues
  - **Solution:** Set FPS to 25 to fix the problem
  - *From: boop*

- **Problem:** Memory issues on 5080 16GB with controlnet
  - **Solution:** Use GGUF models in fp4, or try KJ loader and force fp16
  - *From: hicho*

- **Problem:** Grid deforming faces in generations
  - **Solution:** Issue acknowledged but no specific fix provided yet
  - *From: hicho*

- **Problem:** Video codec playback issues
  - **Solution:** Use standard h.264 MP4 format with VHS node for better compatibility
  - *From: 152993277631528960*

- **Problem:** Wrong aspect ratio in prompt causes split screen effect
  - **Solution:** Ensure correct aspect ratio is specified in the prompt
  - *From: 152993277631528960*

- **Problem:** Face drift and identity loss during generation
  - **Solution:** Attempted using identity lora but results were similar - issue persists
  - *From: NebSH*

- **Problem:** Face gets messed up during camera rotation prompts
  - **Solution:** Switch to dev+lora at 0.6, use manual sigma settings with euler, and use IC detailer lora at 0.5 for T2V only
  - *From: U̷r̷a̷b̷e̷w̷e̷*


## Model Comparisons

- **LTX 2 vs WAN 2.2**
  - LTX has better everything except per-pixel resolution and physics. WAN better for texture fidelity
  - *From: dj47*

- **LTX 2 vs Sora 2**
  - Both have character dialogue assignment issues, but LTX has less problems
  - *From: dj47*

- **Dev model vs Distilled model for movement**
  - Dev model helps with movement quality, recommend 40 steps with dev then 3 with distill for upscale
  - *From: Benjimon*

- **Portrait vs landscape orientation**
  - Portrait works fine, Sora portrait often better than landscape
  - *From: VK*

- **Full model vs FP8 for LoRA quality**
  - Considerable quality difference with BF16 full model being superior
  - *From: NebSH*

- **Distill workflow vs full model workflow**
  - Full model workflow has better prompt adherence and detail due to higher CFG and more steps
  - *From: gopnik*

- **T2V vs I2V stability**
  - Getting more stable results overall with T2V than I2V
  - *From: 305792526629994496*

- **Motion quality at different resolutions**
  - Motion is not as good at higher resolution
  - *From: Benjimon*

- **Stage 2 vs both stages for LoRA**
  - Stage 2 alone produces more natural car movement, both stages makes it look floating
  - *From: Tonon*

- **Different upscalers**
  - res_2s takes extra 100s to generate compared to euler_a
  - *From: chancelor*

- **T2V vs original video idea**
  - LTX2 T2V got surprisingly close to replicating video concepts, though not exact
  - *From: garbus*

- **Distilled vs full model quality**
  - Full model produces better quality but distilled is faster - distilled has plastic look
  - *From: NebSH*

- **8 steps distill vs 40 steps full model**
  - Full model at 40 steps produces more natural look than distilled at 8 steps
  - *From: NebSH*

- **Distilled vs Dev model for audio/video masking**
  - Distilled has more motion and grain, more overcooked and angry; Dev matches original footage better, less angry
  - *From: Nathan Shipley*

- **LTX-2 vs WAN 2.2 for car lifting prompt**
  - WAN 2.2 did it in one shot, LTX-2 took over 20 workflow runs
  - *From: nikolatesla20*

- **15 steps distilled vs dev model for i2v**
  - 15 steps on distilled works like a charm, dev model produces crap with i2v
  - *From: neofuturo*

- **LTX western cartoon vs anime capability**
  - LTX2 knows how to do western cartoon somewhat, but struggles with anime
  - *From: Choowkee*

- **LTX2 vs Wan2**
  - Wan has better character retention and physics, but LTX2 has sound, higher FPS, dynamic motion and realistic speed. Currently a tie with LTX2 having better potential as base
  - *From: dj47*

- **Non-distilled vs distilled for audio**
  - Non-distilled often produces better sound quality than distilled version
  - *From: ezMan*

- **Phroot merge fp8 vs distilled gguf q4km**
  - Phroot merge in fp8 format is about 1.5x larger but actually faster in all parts
  - *From: patientx*

- **LTX2 vs WAN for visual quality**
  - LTX2 has watery effects and detail loss similar to WAN 2.1, behind WAN 2.2 in visual quality but faster
  - *From: Juan Gea*

- **LTX2 vs InfiniteTalk for face consistency**
  - InfiniteTalk better for face consistency, LTX2 changes faces too much but much faster (82 seconds vs 8 minutes)
  - *From: nikolatesla20*

- **LTX2 vs WAN speed**
  - LTX2 much faster - can generate 8 seconds in 30 seconds vs WAN taking much longer
  - *From: 152993277631528960*

- **Dev vs Distilled model quality**
  - Dev + distill lora @0.6 seems same quality as distilled for most cases
  - *From: ucren*

- **Flux Klein vs Flux Kontext for image editing**
  - Klein is smaller, faster (4-5 seconds on RTX 3090), and produces better results than the older Kontext model
  - *From: nikolatesla20*

- **LTX vs InfiniteTalk with Magref for lipsync**
  - InfiniteTalk produces better 'communique' results, LTX attempts were disappointing and more challenging than expected
  - *From: mdkb*

- **One-stage vs two-stage workflow**
  - One-stage superior with better camera adherence like 'kling 2.6', two-stage makes more blancmange artifacts
  - *From: Alpha-Neo*

- **Dev model vs distilled model**
  - Dev with distill LoRA at 0.6 gives less washed out results but takes twice as long as pure distilled
  - *From: U̷r̷a̷b̷e̷w̷e̷*

- **LTX2 vs WAN model**
  - LTX2 system prompt is essential unlike WAN which works with simple sentences
  - *From: hicho*

- **GGUF Q5 models vs full models**
  - GGUF Q5 can generate high resolution (3072x2048) on lower VRAM but takes 20-30 minutes
  - *From: The Shadow (NYC)*

- **LTX2 vs WAN for video-to-video**
  - LTX2 v2v with latent low denoise is very bad unlike WAN, but LTX2 IC LoRA with controlnet works better
  - *From: hicho*

- **Motion LoRA vs preprocessor on first stage**
  - Motion LoRA on first pass preferred over preprocessor
  - *From: Vérole*

- **Single resolution vs upscale workflow**
  - Direct high resolution (1504/832) better motion than lower resolution (1280/720) then upscale
  - *From: Vérole*

- **Old guider vs new LTX Multimodal Guider**
  - New guider produces significantly better results
  - *From: garbus*


## Tips & Best Practices

- **Videos have time to breathe and linger, allowing realistic pacing**
  - Context: Unlike cramming everything into 5 seconds
  - *From: KakerMix*

- **Try other languages for different voice effects**
  - Context: Model supports multiple languages with proper accents
  - *From: garbus*

- **Use WAN upscaling on LTX 2 output for quality improvement**
  - Context: Hybrid workflow for better final results
  - *From: VK (5080 128gb)*

- **Use dolly out camera LoRA for better vertical motion**
  - Context: When trying to achieve vertical movement in videos
  - *From: gopnik*

- **Describe specific movements in prompts rather than generic actions**
  - Context: For better animation results - describe mouth moving rather than just 'she says'
  - *From: gopnik*

- **Close Civitai tabs during generation for better performance**
  - Context: Having Civitai tabs open affects performance especially in final VAE decode step
  - *From: Hell G.*

- **Use timestamp prompting for scene control**
  - Context: [0-3s] format works well with LTX-2 and can handle cuts/transitions
  - *From: brent*

- **Sequential prompting works without markup**
  - Context: Can prompt sequentially without timestamp notation
  - *From: TK_999*

- **Use detailed prompting for better results**
  - Context: Prompting rewrites improve the quality of the result quite a bit
  - *From: chancelor*

- **Use LLM nodes for prompt enhancement**
  - Context: Create workflow that uses LLM nodes to help with prompting, taking image and text prompts to create video prompts
  - *From: VRGameDevGirl84(RTX 5090)*

- **Sound helps video stability**
  - Context: Including sound in generations helps with overall video stability
  - *From: Benjimon*

- **Different samplers may help with skin issues**
  - Context: To address shiny skin problems, try different samplers like sa_solver or lcm
  - *From: Phr00t*

- **Image preprocessing recommended**
  - Context: Use image compression preprocessing node for better I2V results
  - *From: Phr00t*

- **Use frame slice node to get proper frame count**
  - Context: GIF needs to be 8n+1 frames - had to slice off 1 frame to get 17 frames
  - *From: Scruffy*

- **Add your own smearish frame in middle**
  - Context: Adding custom intermediate frames can improve motion
  - *From: JUSTSWEATERS*

- **Use LLM to enhance prompts**
  - Context: Copy instructions from enhancer node and put through LLM for better I2V prompts
  - *From: Choowkee*

- **Long prompts work better**
  - Context: LTX2 requires long detailed prompts like LTX 0.9.8, short prompts produce poor results
  - *From: cyncratic*

- **Sometimes big prompt changes do nothing, single words change everything**
  - Context: After 200 prompt tweaks, learned that prompting behavior is unpredictable
  - *From: jiffyam*

- **For i2v, less intricate prompts work much better**
  - Context: Complex prompts cause loss of input image quickly
  - *From: Arts Bro*

- **Use dev fp8 + 0.5 distilled lora with half the steps**
  - Context: Get quality results with fewer steps by combining models
  - *From: Arts Bro*

- **40-50fps better for fast motion**
  - Context: Higher fps helps with fast motion sequences
  - *From: nikolatesla20*

- **Videos need couple seconds at least, should be long enough for intended action/dialogue**
  - Context: Many people don't give enough time for the action they want
  - *From: garbus*

- **Simple prompts sometimes work better than detailed ones**
  - Context: LTX prompting can be unpredictable
  - *From: HeadOfOliver*

- **Using Sora2 system prompt works with LTX**
  - Context: Cross-model prompting techniques
  - *From: hicho*

- **Use ChatGPT with specific formatting for better prompts**
  - Context: Give ChatGPT a structured format template, then describe what you want and it will format prompts for LTX-2 that work better than manual typing
  - *From: nikolatesla20*

- **Lower LoRA strength when combining multiple effects**
  - Context: When using snorricam LoRA with outfit change, had to lower snorricam to 0.4 for better results
  - *From: NebSH*

- **Use 'interrupted' instead of 'disturbed' for character interactions**
  - Context: Better word choice for prompting character dialogue interruptions
  - *From: Mazrael.Shib*

- **Create x2 interpolation after generation for smoother results**
  - Context: Generate at 32 fps then apply 2x interpolation for better detail and smoothness
  - *From: GalaxyTimeMachine (RTX4090)*

- **Use separate passes for upscaling quality control**
  - Context: Output first low-res pass, check if it's OK, then send to upscaler pass
  - *From: N0NSens*

- **Be very specific in prompts for crowd scenes**
  - Context: For busy sidewalk scenes, specify exact movements like 'he pushes past the people' rather than vague descriptions
  - *From: U̷r̷a̷b̷e̷w̷e̷*

- **Use LLMs for prompt enhancement**
  - Context: ChatGPT 4o mini, Gemma3, Qwen3 via OpenRouter work well for enhancing prompts
  - *From: U̷r̷a̷b̷e̷w̷e̷*

- **Include spoken text in prompts for better results**
  - Context: When doing audio-driven generation, typing out what the character says in the prompt can help, especially for inpainting continuations
  - *From: ucren*

- **Lower diffused lora strength for longer generations**
  - Context: Reduce to about 0.6 to help with focus issues on longer generations
  - *From: Mazrael.Shib*

- **Keep models loaded for faster generation**
  - Context: When doing series of similar generations, keeping models loaded speeds up process significantly
  - *From: 152993277631528960*

- **Use minimal prompting for i2v**
  - Context: More descriptive prompts cause model to ignore image and add unwanted elements
  - *From: mdkb*

- **Include non-masked audio in prompt for v2v**
  - Context: Helps with audio continuity when extending videos
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Normalize audio to loud levels like -14LUFS**
  - Context: Helps with lipsync quality
  - *From: mdkb*

- **Use negative prompts for accent control**
  - Context: Can control unwanted accents by putting them in negative prompt
  - *From: mdkb*

- **Do 5-10 seconds setup then extend with fresh prompt**
  - Context: Works well for lazy prompting approach instead of highly structured prompts
  - *From: garbus*

- **Use system prompt for better results**
  - Context: LTX2 system prompt is essential for good results unlike other models
  - *From: hicho*

- **Static shots can go very long without degradation**
  - Context: For mostly static shots with little motion, can generate very long videos
  - *From: garbus*

- **Mask input image for video extension**
  - Context: When getting errors in video extension, try masking the input image
  - *From: mdkb*

- **Use smaller first stage then upscale**
  - Context: Start with small resolution like 480x420 then upscale for better results
  - *From: JUSTSWEATERS*

- **First and last frame workflow works better with specific weights**
  - Context: Use 1.0 for first frame, 0.75 for subsequent frames, and change second frame to 1.00 for better results
  - *From: VRGameDevGirl84*

- **Use simple prompts for image-to-video to avoid switching to text-to-video mode**
  - Context: When you want to maintain reference image fidelity
  - *From: hicho*

- **Structure speech prompts as 'person speaks in [voice] and says [text]'**
  - Context: For better audio generation results
  - *From: U̷r̷a̷b̷e̷w̷e̷*

- **Generate at 1920x1080 resolution for better quality**
  - Context: Low resolution always looks poor, higher resolution helps significantly
  - *From: nikolatesla20*

- **Usually generate with at least 960x960 for good results**
  - Context: General generation guidelines, though higher resolution is always better
  - *From: U̷r̷a̷b̷e̷w̷e̷*

- **Add 'GLITCH' in various prompt places to create artifacts**
  - Context: For intentional glitch effects
  - *From: 305792526629994496*

- **Use phrase 'A cartoon from the Super Mario Bros Super Show' to generate Mario content**
  - Context: For generating content from that specific animated series
  - *From: U̷r̷a̷b̷e̷w̷e̷*

- **Create T2V with complex prompt, take first frame, convert to desired style, then use same prompt in I2V**
  - Context: Workflow for style transfer and consistency
  - *From: VK (5080 128gb)*

- **Only use IC detailer lora on T2V, not I2V or V2V**
  - Context: Using it on I2V/V2V will mess up matching and change faces
  - *From: U̷r̷a̷b̷e̷w̷e̷*

- **Bad audio can be replaced with groove music to change the video's tone**
  - Context: Can transform epic war scenes into fashion show-style content
  - *From: U̷r̷a̷b̷e̷w̷e̷*

- **Create perfect loops by copying and pasting end to end**
  - Context: 4-second loops can be extended to any length needed
  - *From: U̷r̷a̷b̷e̷w̷e̷*


## News & Updates

- **ComfyUI templates added for LTX Video 2**
  - Official templates available in ComfyUI pull request
  - *From: LukeG89*

- **Training scripts released for LTX Video 2**
  - Model is trainable with open source training scripts
  - *From: AshmoTV*

- **LoRA training documentation released including audio training**
  - Official documentation available for training LoRAs with audio capabilities
  - *From: 305792526629994496*

- **Wallace and Gromit LoRA available on HuggingFace**
  - Community LoRA working with LTX-2
  - *From: ˗ˏˋ⚡ˎˊ-*

- **LTX team is impressed with community creations**
  - Team spoke about being super impressed with community work
  - *From: 210245371002093570*

- **Community showcase video created featuring recent work**
  - Showcase video made featuring cool community creations from recent days
  - *From: 210245371002093570*

- **LTX devs have fix for audio stability coming soon**
  - Developers said they had a good idea for fixing audio stability issues but it didn't make it in time for current release, will be in next release
  - *From: TK_999*

- **New workflow and nodes released**
  - Updated nodes and new workflow released that helped stop still images and no talking issues
  - *From: 130694557913317377*

- **VHS LoRA trained on old tapes**
  - LoRA trained on VHS tapes from late 80s/early 90s with commercials and desert footage
  - *From: 305792526629994496*

- **AnimateDiff LoRA available**
  - AnimateDiff style LoRA for LTX2 available on HuggingFace
  - *From: neofuturo*


## Workflows & Use Cases

- **ChainneR app for reusing I2V workflows**
  - Use case: Streamlining I2V generation process
  - *From: magix*

- **LTX 2 to WAN upscaling pipeline**
  - Use case: Improving final video quality
  - *From: VK (5080 128gb)*

- **Two-stage rendering: 20 steps half-res then distill at full-res**
  - Use case: High quality renders - splits first 20 steps at half resolution then 4 distill steps at full resolution
  - *From: 305792526629994496*

- **Automatic scene generation from Reddit stories**
  - Use case: One-click conversion from text stories to video scenes using multiple LLM calls
  - *From: Simonj*

- **Audio input workflow for custom sound**
  - Use case: Adding custom audio with selectable start point and duration
  - *From: Helikaon23s*

- **LLM-enhanced prompting with random image generation**
  - Use case: Uses LLM nodes with zimage to create random images, then LLM takes image and text prompt to create new image-to-video prompt
  - *From: VRGameDevGirl84(RTX 5090)*

- **Kijai's Audio Continuity workflow**
  - Use case: For maintaining audio continuity across video generation
  - *From: Tachyon*

- **Video extension using latent concatenation**
  - Use case: Continue videos by giving multiple frames instead of single image, similar to Google Flow extend
  - *From: 421114995925843968*

- **Multi-scene automated generation**
  - Use case: Automated workflow for creating multiple scenes with scheduler applet
  - *From: magix*

- **Extension from audio using image and audio driving to video**
  - Use case: Creating videos that sync motion to audio beat
  - *From: Vérole*

- **Flux2 keyframes with character reference then LTX**
  - Use case: Character consistency across video sequences
  - *From: magix*

- **Single frame from each segment as input**
  - Use case: Creating longer sequences by using keyframes
  - *From: magix*

- **Extend with last frame of each sequence or add picture at start**
  - Use case: Video extension using z-image and qwen edit 2511
  - *From: Vérole*

- **Half res generation then upscaled 4 step distill**
  - Use case: Managing VRAM constraints while maintaining quality
  - *From: 305792526629994496*

- **Keyframes made in Flux 2 then LTX**
  - Use case: Creating longer narrative content with consistent characters
  - *From: ˗ˏˋ⚡ˎˊ-*

- **I2V 640x640 1st sampler + 1280x1280 upscaler**
  - Use case: Two-stage upscaling process for better quality
  - *From: Elvaxorn*

- **Audio re-take workflow for perfect video with new sound**
  - Use case: When video is perfect but audio needs retrying
  - *From: garbus*

- **Video continue/extend using gemma 3 model loader**
  - Use case: Extending existing video clips
  - *From: Mazrael.Shib*

- **T2V/I2V GGUF workflows with updated video VAE**
  - Use case: Efficient generation on 12GB/48GB systems
  - *From: U̷r̷a̷b̷e̷w̷e̷*

- **T2I2V pipeline with auto-prompting LLMs**
  - Use case: Text to image to video with automated prompt generation using LLMs and z-image creation
  - *From: GalaxyTimeMachine (RTX4090)*

- **First/Last/Middle keyframe workflow**
  - Use case: Creating videos with multiple keyframes but struggles with lip sync
  - *From: Simonj*

- **Frame-to-frame implementation**
  - Use case: Processing with 3 random frames for faster generation but loses lip sync
  - *From: neofuturo*

- **FFLF (First, Middle, Last Frame) extension**
  - Use case: Extending videos by using key frames with multiplier nodes
  - *From: neofuturo*

- **48fps conditioning with frame interpolation**
  - Use case: Interpolate source to 48fps, use for conditioning, then export back to 24fps for better speech quality
  - *From: ucren*

- **Multi-stage upscaling with masking**
  - Use case: Two-pass rendering with masked upscale for better audio sync quality
  - *From: ucren*

- **Audio-driven I2V with automatic calculations**
  - Use case: Modified workflow that auto-calculates frames from audio duration and separates vocals
  - *From: nikolatesla20*

- **Klein image edit for character consistency**
  - Use case: Create multiple poses and scenes from single starting image without LoRAs
  - *From: nikolatesla20*

- **Partial automation workflow for music videos**
  - Use case: Full video generation in 40 minutes including transitions
  - *From: VRGameDevGirl84(RTX 5090)*

- **IC Control workaround for GGUF lipsync**
  - Use case: Generate i2v first for camera control, then use IC Control for lipsync - slower but works
  - *From: Alpha-Neo*

- **Three-stage upscaling pipeline**
  - Use case: LTX2 Undistilled with CFG > distilled + detailed LoRAs with CFG=1 > FlashVSR for high resolution outputs
  - *From: The Shadow (NYC)*

- **Audio-to-video workflow for 16GB VRAM**
  - Use case: Can generate 1000 frames of 1280x720px videos from audio + text prompt on RTX 5080
  - *From: meakwa23*

- **Frame injection with 2 nodes**
  - Use case: Guide nodes for general guidance, inplace nodes for precise frame positioning like 'on frame 54'
  - *From: neofuturo*

- **LTX automation with re-do feature**
  - Use case: Full automation workflow with ability to re-do specific scenes by index number
  - *From: VRGameDevGirl84*

- **2-chunk 20-second video generation for 40-second output**
  - Use case: Creating longer videos by combining multiple chunks
  - *From: Vérole*

- **T2AV, TA2V, I2V, or IA2V all-in-one workflow**
  - Use case: Universal workflow supporting multiple input types
  - *From: Vérole*

- **Using SRT files for automated scene timing in music videos**
  - Use case: Creating music videos with precise scene cuts based on timing data
  - *From: VRGameDevGirl84(RTX 5090)*

- **Auto beat node for music video generation**
  - Use case: Automatically adding cuts based on beats in songs, with inputs for drums and bass
  - *From: VRGameDevGirl84(RTX 5090)*

- **Hybrid CGI-AI production setup**
  - Use case: Commercial automotive work where product is CGI but enhanced with AI
  - *From: 520191580007563264*

- **Using Flux Klein 9B for keyframe generation with LoRA and reference image**
  - Use case: Enhanced keyframe generation for video production
  - *From: 520191580007563264*

- **Film grain and color filtering in CapCut for AI look reduction**
  - Use case: Post-processing to make AI-generated content appear more natural
  - *From: VRGameDevGirl84(RTX 5090)*

- **2-stage workflow with audio and image inputs**
  - Use case: Creating videos with synchronized audio
  - *From: Janosch Simon*

- **T2AV 1-pass generation**
  - Use case: Single-pass text-to-audio-video generation
  - *From: 152993277631528960*

- **I2V with new nodes**
  - Use case: Image-to-video generation using updated workflow components
  - *From: NebSH*

- **Using Midjourney for images, CosyVoice 3 for TTS, then LTX2 for video**
  - Use case: Multi-tool pipeline for complete video creation
  - *From: Janosch Simon*


## Recommended Settings

- **Noise mask/strength for I2V**: 0.6
  - Prevents static output and deformation
  - *From: Dragonyte*

- **Steps for basic generation**: 8 steps
  - Sufficient for decent quality at 5 second clips
  - *From: Owlie*

- **WAN upscale denoise**: 0.3
  - Good balance for v2v upscaling
  - *From: VK (5080 128gb)*

- **Sampler**: res_2s
  - LTX team recommended over euler, improves quality but increases generation time
  - *From: 498275793852432384*

- **Steps for dev + distill combo**: 40 steps dev + 3 steps distill
  - Good balance for upscaling workflow
  - *From: Benjimon*

- **FPS options**: 16, 24, 48 fps
  - Various frame rates supported and tested
  - *From: TK_999*

- **LoRA strength testing**: 0.6, 0.8, 0.9
  - Different strengths tested, can disable on upscaler stage
  - *From: NebSH*

- **CFG**: 3.5
  - Used in high-quality 1920x1088 generation
  - *From: gopnik*

- **Steps**: 40
  - Used for detailed high-resolution outputs
  - *From: gopnik*

- **FPS**: 24
  - Standard frame rate for cinematic results
  - *From: gopnik*

- **Sampler**: euler_ancestral
  - Produces good results in high-resolution generations
  - *From: gopnik*

- **Distilled LoRA strength**: 1
  - Full strength when using distilled model
  - *From: gopnik*

- **Detailer LoRA strength**: 0.75
  - Applied to both stage 1 and 2 for enhanced detail
  - *From: gopnik*

- **Reserve VRAM**: 6
  - Prevents OOM errors on RTX 4090
  - *From: gopnik*

- **CFG**: 4
  - Used with Euler sampler for audio continuity workflow
  - *From: Tachyon*

- **Compression**: 33
  - Used for first and last frame processing
  - *From: Vérole*

- **Force**: 1
  - Used with compression setting for frame processing
  - *From: Vérole*

- **Denoise**: 0.3
  - Used with LoRA generation
  - *From: VK (5080 128gb)*

- **Distilled LoRA strength**: 0.5
  - Used with 20 steps cfg 3 for distill
  - *From: NebSH*

- **CFG**: 3
  - Used with distill 0.5 20 steps
  - *From: NebSH*

- **CFG**: 4
  - Used with no distill 40 steps
  - *From: NebSH*

- **VAE Decode tiling**: 2/8/16/8
  - Best setting for reducing grid patterns but doubles VRAM use
  - *From: garbus*

- **Detail daemon start**: 0.8
  - Set start point for detail daemon sampler
  - *From: jiffyam*

- **FPS**: 25
  - Temporal upscaler expects 25 fps, fixes jerkyness
  - *From: HeadOfOliver*

- **Distilled lora strength**: -0.50
  - Removes excessive film grain and artifacts
  - *From: Nathan Shipley*

- **Steps for distilled model**: 15
  - Works well for 720p single stage, good quality
  - *From: neofuturo*

- **CFG for dev model**: 5
  - Avoids mess that occurs at CFG 4
  - *From: Nathan Shipley*

- **Animatediff lora strength**: 2.0
  - Higher strength helps with effect, works well with deforum loras
  - *From: NebSH*

- **Audio normalization**: -23 default
  - Helps improve audio quality
  - *From: U̷r̷a̷b̷e̷w̷e̷*

- **Custom sigmas for distilled upscale**: 0.975, 0.909375, 0.725, 0.421875, 0.0
  - 4 steps instead of 3 for better upscaling results
  - *From: dischordo*

- **Sampler configuration**: er_sde with 8 steps using distilled model
  - Produces high quality results
  - *From: GalaxyTimeMachine (RTX4090)*

- **Resolution for detail**: 1792x1088 at 32 fps
  - Good balance of detail without being full HD
  - *From: GalaxyTimeMachine (RTX4090)*

- **Maximum frames for 16GB VRAM**: 480 frames MAX at 1920x1080 (20 seconds)
  - Hardware limitation regardless of model precision
  - *From: Volkin*

- **Distilled LoRA strength**: -0.4 to -0.6
  - Fixes overbaked distilled model and improves face consistency
  - *From: ucren*

- **Audio latent multiply**: 0.75
  - Reduces exaggerated expressions in audio-driven generation
  - *From: ucren*

- **Steps for quality boost**: 8->15 steps on first pass
  - Gives noticeable quality improvement
  - *From: ucren*

- **Fast generation settings**: 7 steps, 1 CFG, LCM sampler
  - For quick generation when models stay loaded
  - *From: 152993277631528960*

- **LTXVPREPROCESS**: 0
  - Prevents issues in workflow
  - *From: Jonathan Scott Schneberg*

- **Conditioning fps**: 30-48 fps
  - Higher fps helps reduce motion artifacts
  - *From: Elvaxorn*

- **Distill LoRA strength**: -0.4
  - Debakes plastic skin issues in distilled model
  - *From: ucren*

- **Tiled spatial overlap**: 256
  - Helps reduce but doesn't eliminate VAE tiling artifacts
  - *From: Ablejones*

- **LTXImgToVideoInPlace**: 0.4 starting point
  - Controls image likeness and character consistency, needs adjustment per resolution
  - *From: mdkb*

- **LTXVPreprocess**: 10-33, usually 25
  - Prevents blancmange on face, lower if issues return
  - *From: mdkb*

- **Camera static LoRA strength**: 0.1
  - Lower strength helps with GGUF lipsync issues
  - *From: mdkb*

- **Frame count for 10 seconds**: 247 frames
  - Compensates for LTX cutting 7 frames, following 8n+1 rule gives 241
  - *From: VRGameDevGirl84(RTX 5090)*

- **CFG for undistilled model**: 4.0
  - When not using distill LoRA, should use CFG 4.0 instead of 1.0
  - *From: NebSH*

- **Distill LoRA strength for dev model**: 0.6
  - Helps control oversaturation while maintaining quality
  - *From: U̷r̷a̷b̷e̷w̷e̷*

- **Camera static LoRA**: 0.5
  - Combined with distill LoRA at -0.3 to fix camera static issues
  - *From: mdkb*

- **VHS LoRA strength**: 2.0 for maximum crispy, 1.3 for better balance
  - Control intensity of VHS effect
  - *From: 305792526629994496*

- **Steps for dev + distill workflow**: 8 steps first sampler, 3 steps second sampler
  - Efficient workflow with spatial upscale between samplers
  - *From: U̷r̷a̷b̷e̷w̷e̷*

- **Distilled LoRA strength on first sampler**: 0.2
  - For 10-second FFLF generation with motion enhancement
  - *From: Simonj*

- **Upscale distill strength**: 0.6
  - For 3-step upscaling process
  - *From: Simonj*

- **Upscale sampler steps**: 20 steps at 1/2 res, 3 steps upscale
  - Memory optimization for 16GB GPU
  - *From: Simonj*

- **Denoise for upscaling**: 0.2
  - For 2+2 steps using upscale to ksampler
  - *From: hicho*

- **Guide resolution for 1920x1024 video**: 1920x1024
  - Should match generated video resolution
  - *From: Simonj*

- **Manual sigma values Stage 1**: 1., 0.99375, 0.9875, 0.98125, 0.975, 0.909375, 0.725, 0.421875, 0.0
  - 8 steps for better quality
  - *From: U̷r̷a̷b̷e̷w̷e̷*

- **Manual sigma values Stage 2**: 0.8025, 0.6332, 0.3425, 0.0
  - 4 steps for refinement
  - *From: U̷r̷a̷b̷e̷w̷e̷*

- **Dev+lora strength**: 0.6
  - Helps maintain face quality during camera rotation
  - *From: U̷r̷a̷b̷e̷w̷e̷*

- **IC detailer lora strength**: 0.5
  - For T2V only - improves detail without breaking consistency
  - *From: U̷r̷a̷b̷e̷w̷e̷*


## Concepts Explained

- **Pickletensors**: Dangerous .pt models that can contain arbitrary Python code - avoid using them
  - *From: cyncratic*

- **Snorricam shot**: Camera technique where camera is mounted to subject's chest, keeping them centered while background moves
  - *From: NebSH*

- **Stop-motion on twos**: Animation technique with stepped/limited timing, held poses every two frames, frame registration wiggle, minimal motion blur
  - *From: The Shadow (NYC)*

- **Audio latents**: Audio spectrograms used as input for video generation, resolution tied to video resolution
  - *From: TK_999*

- **Tiled VAE decode**: Method to handle memory limitations during video decoding by processing in tiles
  - *From: Tachyon*

- **Stage 1 vs Stage 2 LoRA application**: LoRAs can be applied to either stage 1, stage 2, or both stages of the two-stage generation process, with different visual effects
  - *From: gopnik*

- **Audio masking**: Technique to preserve original audio in specific time ranges while allowing model to generate audio in other parts
  - *From: Dragonyte*

- **Object POV**: Point of view from an object's perspective, used in LoRA training
  - *From: NebSH*

- **Transition roll**: Camera transition technique that rolls/sweeps between scenes
  - *From: NebSH*

- **Hero shot**: Cinematic camera technique for dramatic angles, available as LoRA
  - *From: NebSH*

- **IC-LoRA training**: Powerful training method mentioned in official documentation
  - *From: 305792526629994496*

- **FFLF**: First Frame Last Frame workflow technique
  - *From: chancelor*

- **De-baking distill model**: Using negative lora strength to reverse distillation effects
  - *From: ucren*

- **Temporal stutter artifacts**: Jerkyness that appears every few frames in temporal upscaling
  - *From: HeadOfOliver*

- **Object permanence in LTX**: LTX has trouble maintaining consistent objects like dents throughout a video sequence
  - *From: nikolatesla20*

- **Latent frame buffer**: The memory space that holds latent video frames during processing - more important for VRAM usage than model size
  - *From: Volkin*

- **NAG node**: Allows negative conditioning even when using distilled models
  - *From: nikolatesla20*

- **Inpainting/extending**: Technique where model continues from existing video frames rather than generating from scratch, helps maintain consistency
  - *From: ucren*

- **Watery effects**: Visual quality issue where details become soft/blurred, common problem in LTX2
  - *From: Juan Gea*

- **8n+1 rule**: Video frames must follow pattern of 8n+1 (e.g., 121, 241 frames)
  - *From: N0NSens*

- **Debaking distilled model**: Using distill LoRA at negative values to reduce plastic skin artifacts in distilled models
  - *From: ucren*

- **Blancmange**: Facial artifact that appears as smooth, featureless texture, controlled by LTXVPreprocess settings
  - *From: mdkb*

- **Token limit sweet spot**: Every model has a maximum resolution/frame length sweet spot, LTX2 is more forgiving than others
  - *From: TK_999*

- **Frame injection**: Technique to inject specific frames at precise positions for controlled video transitions
  - *From: neofuturo*

- **First Last Frame workflow**: Method using specific frame indexes (0 for first, -1 for last) to control video start and end points
  - *From: VRGameDevGirl84*

- **FFLF (First Frame Last Frame)**: Video generation technique using first and last frame guidance
  - *From: Simonj*

- **I2V vs T2V mode switching**: LTX2 can switch from image-to-video mode to text-to-video mode when prompts don't match reference image
  - *From: hicho*

- **T2AV**: Text-to-Audio-Video generation capability
  - *From: 152993277631528960*


## Resources & Links

- **ComfyUI-LTXVideo workflows** (workflow)
  - https://github.com/Lightricks/ComfyUI-LTXVideo/tree/master/example_workflows
  - *From: xdestroyer*

- **ComfyUI templates PR** (repo)
  - https://github.com/comfyanonymous/ComfyUI/pull/11652
  - *From: LukeG89*

- **Merge safetensors tool** (tool)
  - https://github.com/dkotel/merge-safetensors
  - *From: Scruffy*

- **NebSH's LoRA collection** (model)
  - https://civitai.com/collections/9825789
  - *From: NebSH*

- **ComfyChainer** (tool)
  - https://github.com/XmYx/ComfyChainer
  - *From: magix*

- **Wallace and Gromit LoRA** (lora)
  - https://huggingface.co/Cseti/LTXV-13B-LoRA-Wallace_and_Gromit-v1
  - *From: ˗ˏˋ⚡ˎˊ-*

- **LTX-2 ComfyUI workflow** (workflow)
  - https://civitai.com/models/2287923/ltx-2-workflow-text-to-video-and-image-to-video
  - *From: Hell G.*

- **LTX-2 prompting guide** (guide)
  - https://ltx.io/model/model-blog/prompting-guide-for-ltx-2
  - *From: GalaxyTimeMachine (RTX4090)*

- **GalaxyAce LoRA** (lora)
  - *From: gopnik*

- **Audio input workflow template** (workflow)
  - *From: Helikaon23s*

- **Official LTX2 prompting guide** (guide)
  - https://ltx.io/model/model-blog/prompting-guide-for-ltx-2
  - *From: GalaxyTimeMachine(RTX4090)*

- **LTX2 API documentation prompting guide** (documentation)
  - https://docs.ltx.video/api-documentation/prompting-guide
  - *From: Anchorite*

- **Official prompt template** (template)
  - https://github.com/Lightricks/LTX-2/blob/main/packages/ltx-core/src/ltx_core/text_encoders/gemma/encoders/prompts/gemma_t2v_system_prompt.txt
  - *From: chancelor*

- **ComfyUI-OpenAI-API** (tool)
  - https://github.com/hekmon/comfyui-openai-api
  - *From: chancelor*

- **Vast.ai GPU rental** (service)
  - https://cloud.vast.ai/?ref_id=343946
  - *From: Xor*

- **Official LTX-2 trainer script** (repo)
  - https://github.com/Lightricks/LTX-2/blob/main/packages/ltx-trainer/README.md
  - *From: NebSH*

- **Inflate LoRA** (model)
  - https://huggingface.co/kabachuha/ltx2-inflate-it
  - *From: VK (5080 128gb)*

- **Audio workflow** (workflow)
  - https://discord.com/channels/1076117621407223829/1309520535012638740/1458505971801395424
  - *From: Vérole*

- **Hero shot LoRA shared in resources channel** (model)
  - *From: NebSH*

- **Fable show runner** (tool)
  - *From: dj47*

- **T2V/I2V GGUF workflows V1.1** (workflow)
  - https://civitai.com/models/2304098?modelVersionId=2593987
  - *From: U̷r̷a̷b̷e̷w̷e̷*

- **Deforum loras** (model)
  - https://huggingface.co/mixy89/LTXV_Deforum/tree/main
  - *From: GalaxyTimeMachine*

- **Animatediff lora** (model)
  - https://huggingface.co/Nebsh/LTX2_Animatediff_Lora/blob/main/AnimateDiff_step2000.safetensors
  - *From: 210245371002093570*

- **Community showcase video** (video)
  - https://www.youtube.com/watch?v=7uaU4Rm7fEo#t=13m27s
  - *From: 210245371002093570*

- **Camera techniques video** (educational)
  - https://www.youtube.com/watch?v=j2bUsYemG-M
  - *From: Arts Bro*

- **ComfyUI_Yvann-Nodes** (repo)
  - https://github.com/yvann-ba/ComfyUI_Yvann-Nodes
  - *From: Golden*

- **Kijai's LTXV chunk feedforward** (workflow)
  - https://github.com/kijai/ComfyUI/blob/ltx2_memory/comfy/ldm/lightricks/av_model.py
  - *From: Peera*

- **Twin Peaks Episode 8 reference footage** (reference)
  - https://www.youtube.com/watch?v=Xrnm1dxUIEQ
  - *From: Arts Bro*

- **ComfyUI-AudioSR** (tool)
  - https://github.com/Saganaki22/ComfyUI-AudioSR
  - *From: ucren*

- **ComfyUI-NovaSR** (tool)
  - https://github.com/Saganaki22/ComfyUI-NovaSR
  - *From: justinj*

- **NovaSR** (repo)
  - https://github.com/ysharma3501/NovaSR
  - *From: justinj*

- **LTX LLM for questions** (tool)
  - https://discord.com/channels/1076117621407223829/1460390123547000935
  - *From: jiffyam*

- **FirstFrameGo paper** (research)
  - https://firstframego.github.io/
  - *From: NebSH*

- **Flux Klein Image Edit** (model)
  - *From: nikolatesla20*

- **ComfyUI-Egregora-Audio-Super-Resolution** (tool)
  - https://github.com/lucasgattas/ComfyUI-Egregora-Audio-Super-Resolution
  - *From: HeadOfOliver*

- **Test-time training for video** (repo)
  - https://github.com/test-time-training/ttt-video-dit
  - *From: dj47*

- **AnimateDiff LoRA for LTX2** (lora)
  - https://huggingface.co/Nebsh/LTX2_Animatediff_style/
  - *From: neofuturo*

- **South Park LoRA** (lora)
  - https://discord.com/channels/1076117621407223829/1464203426496778386
  - *From: NebSH*

- **Snorricam LoRA** (lora)
  - https://civitai.com/models/1557338/snorricam
  - *From: NebSH*

- **12GB GGUF Workflows Collection** (workflow)
  - https://civitai.com/models/2304098?modelVersionId=2623604
  - *From: U̷r̷a̷b̷e̷w̷e̷*

- **ComfyUI AudioTools** (tool)
  - https://github.com/Urabewe/ComfyUI-AudioTools
  - *From: U̷r̷a̷b̷e̷w̷e̷*

- **VCR LoRA for LTX2** (lora)
  - *From: 305792526629994496*

- **AnimateDiff LoRA** (lora)
  - *From: hell2heights2*

- **Fill's LTX LoRA Image2Video Adapter** (lora)
  - https://huggingface.co/MachineDelusions/LTX-2_Image2Video_Adapter_LoRa
  - *From: 520191580007563264*

- **HeartMula local music generation** (tool)
  - https://heartmula.github.io/
  - *From: Janosch Simon*

- **LEVO local music generation** (tool)
  - https://levo-demo.github.io/
  - *From: Janosch Simon*

- **Suno song example** (resource)
  - https://suno.com/s/EsvTKVKnDv7Tow88
  - *From: Vérole*

- **YouTube video test example** (resource)
  - https://www.youtube.com/shorts/yn5UOBFls2o?feature=share
  - *From: hicho*

- **Sample video output** (resource)
  - https://www.huge.com/denrakeiw/160922-ghost-of-the-grid
  - *From: 520191580007563264*

- **Klipy video hosting** (resource)
  - https://klipy.com/gifs/misty-dance-2
  - *From: hicho*

- **OIIA Spinning Cat weights** (model)
  - https://civitai.com/models/2018677/oiia-spinning-cat
  - *From: 710895360981205003*

- **V2V matching example video** (example)
  - https://www.youtube.com/watch?v=GUXBpjHIuw0
  - *From: U̷r̷a̷b̷e̷w̷e̷*


## Known Limitations

- **Character dialogue assignment issues**
  - Actions and dialogue can bleed between characters, making narrative difficult
  - *From: dj47*

- **Body horror without NSFW training**
  - Model deliberately not trained on NSFW content leading to anatomy issues
  - *From: dj47*

- **Audio context not maintained**
  - Cannot keep same voice/character consistency across generations
  - *From: KakerMix*

- **Model doesn't recognize some military hardware**
  - No knowledge of B-17 bombers or flak guns
  - *From: Tachyon*

- **Model substitutes most celebrities when prompted**
  - Will replace celebrities with generic faces - only handful of exceptions work
  - *From: brent*

- **Inconsistent vertical motion**
  - Not yet sure when vertical motion works and when it doesn't
  - *From: gopnik*

- **Scene changes difficult to control**
  - Model prefers continuous shots over cuts, needs specific prompting techniques
  - *From: cyncratic*

- **Dead air in longer generations with short prompts**
  - Found a lot of 'dead air' waiting periods when prompt isn't long enough for frame count
  - *From: 305792526629994496*

- **Text generation inconsistency**
  - LTX prompting guide says you really can't expect consistent text in generated videos
  - *From: garbus*

- **Model defaults to human-like features**
  - The model likes to snap to humans a lot of the time, even when generating other subjects
  - *From: Benjimon*

- **Face quality degradation**
  - Loss of detail pretty quickly into the video, face warping and eye issues common
  - *From: Phr00t*

- **Violence and adult content restrictions**
  - Model has limitations with violence and nudity generation, likely due to training data restrictions
  - *From: dj47*

- **Audio quality needs improvement**
  - Audio quality needs a bump, sounds generic like tutorial narrator voice
  - *From: HeadOfOliver*

- **Japanese language understanding**
  - LTX2 doesn't understand Japanese very well
  - *From: DreamWeebs*

- **Prompt comprehension**
  - Prompt comprehension is poor, takes many generations to get something correct
  - *From: nikolatesla20*

- **Text generation**
  - Text is generally an issue for LTX
  - *From: dj47*

- **Character consistency in longer sequences**
  - Characters change too much in longer sequences
  - *From: NebSH*

- **Beatboxing concept**
  - LTX doesn't know what beatboxing is but can work with some prompting
  - *From: N0NSens*

- **Speed advantage negated by higher steps/detailed samplers**
  - Using res_2s or higher steps defeats the speed benefits LTX team promotes
  - *From: nikolatesla20*

- **Temporal upscaler artifacts above 241 frames**
  - Strange temporal stutter artifacts when going above 241 frames
  - *From: HeadOfOliver*

- **Characters forgotten when moving out of frame**
  - Model forgets non-human character details when they move out of frame
  - *From: Mazrael.Shib*

- **Scene cuts break image guidance**
  - Image guidance doesn't survive when LTX decides to do scene cuts
  - *From: BitPoet*

- **Prompt comprehension issues**
  - Complex actions like car lifting require many attempts vs other models
  - *From: nikolatesla20*

- **Detail lora causes problems with flat 2D anime generations**
  - Using detail lora with anime style causes issues
  - *From: Choowkee*

- **Can't handle upside down objects well**
  - Asking for flipped cars or upside down things creates monstrosities
  - *From: nikolatesla20*

- **Fast movement creates mouth and teeth issues**
  - Any fast movement, even at 2048x800 raw resolution, creates problems with facial features
  - *From: Arts Bro*

- **Audio quality lacks layers**
  - Audio needs more layers for background noises like wind, rain, waves, destruction - not just voice
  - *From: GalaxyTimeMachine (RTX4090)*

- **Struggles with smaller faces**
  - Generally has trouble with smaller faces in frame, gets better when camera is closer
  - *From: Simonj*

- **Difficulty following complex prompts accurately**
  - Hard to get accurate scene following with complex multi-step prompts, may need 10+ generations
  - *From: Fictiverse*

- **Face consistency in I2V with audio**
  - LTX2 changes faces significantly when using custom audio, especially with non-famous faces
  - *From: nikolatesla20*

- **Motion artifacts at higher fps for long clips**
  - 48fps conditioning creates more motion artifacts in longer extensions
  - *From: ucren*

- **Cartoon over-training**
  - Model seems overtrained on cartoons, defaults to cartoon style easily and has more distortion with animation
  - *From: nikolatesla20*

- **Watery visual effects**
  - Detail loss and soft/blurred effects that aren't production-ready quality
  - *From: Juan Gea*

- **People turning/spinning issues**
  - LTX2 does not handle people turning around or spinning well
  - *From: ucren*

- **GGUF models have lipsync issues without LoRAs**
  - Q8 dev model requires distilled LoRA or camera LoRA to achieve lipsync
  - *From: Alpha-Neo*

- **Prompt control varies between resolutions**
  - Settings that work at 256p don't work at 480p, requiring rebalancing
  - *From: mdkb*

- **Tiled VAE decoding artifacts in dark scenes**
  - Visible grid patterns appear in dark areas, can't be fully eliminated with current implementations
  - *From: ucren*

- **Audio-video mask timing trade-off**
  - Early masking preserves likeness but loses mouth movement, late masking gets movement but loses likeness
  - *From: Nekodificador*

- **Character consistency issues**
  - LTX does not maintain consistent character appearance across longer generations
  - *From: dj47*

- **Face consistency issues in video extension**
  - Consistency degrades over time, eyes don't hold together well, becomes chaotic
  - *From: mdkb*

- **Color artifacts at high vertical resolutions**
  - Vertical outputs around or over 1536 pixels get blue color hue and hallucinations at top/bottom
  - *From: dischordo*

- **Model doesn't recognize specific objects well**
  - Still doesn't know what drill presses look like
  - *From: nikolatesla20*

- **Prompt following issues**
  - LTX doesn't listen to prompts well in either dev or distilled mode
  - *From: N0NSens*

- **LTX2 struggles with mouth and eyes detail**
  - Poor quality even on closeups, needs second stage and high resolution
  - *From: hicho*

- **Low resolution always looks poor**
  - At low resolution quality is consistently bad
  - *From: nikolatesla20*

- **32GB RAM insufficient for long video generation**
  - 32GB RAM won't get you far for extended video generation
  - *From: Charlie*

- **Random switching from I2V to T2V mode**
  - Sometimes randomly switches to text-to-video instead of maintaining image-to-video, can't force it to happen consistently
  - *From: U̷r̷a̷b̷e̷w̷e̷*

- **V2V with latent low denoise performs poorly**
  - Video-to-video with low denoise latent approach is very bad compared to WAN
  - *From: hicho*

- **Grid artifacts deform faces**
  - Grid processing causes face deformation issues
  - *From: hicho*

- **Full AI production still time-consuming in post**
  - For commercial clients, especially automotive, full AI workflows require extensive post-production work
  - *From: 520191580007563264*

- **Face drift during long generations**
  - Faces lose consistency and drift significantly during video generation
  - *From: NebSH*

- **Camera rotation prompts can mess up faces**
  - 360-degree camera rotation prompts often result in face distortion
  - *From: VRGameDevGirl84(RTX 5090)*

- **IC detailer lora breaks I2V and V2V**
  - Using IC detailer lora on image-to-video or video-to-video workflows causes mismatching and face changes
  - *From: U̷r̷a̷b̷e̷w̷e̷*


## Hardware Requirements

- **Minimum VRAM**
  - Works with 4GB VRAM (reported by someone) and 3060 confirmed, but needs >64GB RAM
  - *From: Tachyon*

- **3090 performance**
  - 1:45 generation time for 5 second video at 8 steps using system swap
  - *From: Owlie*

- **4090 capability**
  - Can handle 1280x1024 resolution without dying
  - *From: TK_999*

- **High frame counts**
  - 351 frames at 720p possible on 5090, I2V OOMs over 121 frames
  - *From: NebSH*

- **RTX 6000**
  - Can handle 1920x1088 at 513 frames in ~10 minutes with full model
  - *From: 305792526629994496*

- **RTX 5090 + 64GB RAM**
  - Can do 2048x1152, needs 25GB VRAM, maxes out RAM during VAE decode
  - *From: el marzocco*

- **RTX 4090 + 24GB GPU**
  - Can handle 609 frames with specific settings
  - *From: Benjimon*

- **128GB RAM recommended**
  - Helps significantly with tiled VAE decode and longer generations
  - *From: Hell G.*

- **Full fine-tune needs 8 H100s**
  - Full model fine-tuning not feasible for most users
  - *From: dj47*

- **VRAM for different resolutions**
  - 1920x1088 takes 645 seconds on RTX 4090, 1280x1280 121 frames requires aggressive tiling settings even on RTX 5090
  - *From: gopnik*

- **RAM usage**
  - Goes up to 96GB RAM usage out of 192GB available, 64GB RAM can be limiting factor
  - *From: PATATAJEC*

- **Generation times by resolution**
  - 1920x1088: 645 seconds, 480p: 150 seconds on RTX 4090
  - *From: gopnik*

- **Upscaling performance**
  - Generation takes 2 minutes, upscaling takes 20 minutes
  - *From: N0NSens*

- **3060 12GB with 48GB RAM**
  - Successfully running LTX2
  - *From: U̷r̷a̷b̷e̷w̷e̷*

- **3090 24GB with 64GB RAM**
  - Successfully running LTX2
  - *From: clockstopper*

- **RTX 5090**
  - Running LTX2 with ComfyUI locally
  - *From: Dkamacho*

- **1280 x 732 resolution**
  - 792 frames was too many for 1920 resolution, had to use lower res
  - *From: 305792526629994496*

- **VRAM usage doubles**
  - Using 2/8/16/8 VAE decode settings doubles VRAM usage
  - *From: garbus*

- **Full HD 20 seconds possible**
  - Able to generate 1920x1080 20 second videos
  - *From: magix*

- **VRAM for 1536x1536 video**
  - Generated in 457.63 seconds on 12GB/48GB system
  - *From: U̷r̷a̷b̷e̷w̷e̷*

- **VRAM for i2v 1000x1000**
  - Works on 8GB VRAM, 32GB RAM system, takes about 550 seconds
  - *From: cocktailprawn1212*

- **RTX 6000 Ada performance**
  - 15 steps render in 5-6 minutes with 48GB VRAM
  - *From: Nathan Shipley*

- **RAM usage for WAN upscaling**
  - Uses up to 220GB RAM for 2560x1440x241 upscale, takes 20 minutes
  - *From: seitanism*

- **VRAM for 10-second 1080p generation**
  - Can generate 10-second 1080p videos with chunk feedforward modification, up from 6-second limit
  - *From: Peera*

- **VRAM frame limits**
  - 16GB VRAM can fit 480 frames MAX at 1920x1080 (20 seconds) regardless of FP16/FP8/FP4
  - *From: Volkin*

- **3060ti performance**
  - Can generate 2k images in 30 seconds on 3060ti
  - *From: neofuturo*

- **RTX 5080 16GB VRAM**
  - Can generate 10 seconds at 1280x704 resolution
  - *From: meakwa23*

- **System RAM for long videos**
  - Need adequate system RAM for 20+ second generations, 8-9GB VRAM usage typical
  - *From: garbus*

- **RTX 5090**
  - Enables very fast generation - 8 seconds of video in 30 seconds with proper settings
  - *From: 152993277631528960*

- **VRAM for distilled LoRA**
  - 7.5GB LoRA may not fit on 12GB VRAM systems
  - *From: mdkb*

- **RAM for long frame counts**
  - Less than 64GB RAM causes pagefile/swapfile usage and delayed generation speed for >241 frames
  - *From: Volkin*

- **GGUF Q8 model requirements**
  - RTX 5090 with 64GB RAM generates 10s video, RTX 4080 with 64GB RAM also works
  - *From: Alpha-Neo*

- **Generation time for 50 seconds**
  - 50 seconds at 480p took 30 minutes on RTX 3060
  - *From: mdkb*

- **40 seconds generation time**
  - Took 307 seconds on RTX 5090
  - *From: ezMan*

- **RTX 5090 for long high-res videos**
  - 32GB VRAM, can handle 1000 frames at 1280x720
  - *From: NebSH*

- **A4500 for high resolution**
  - 20GB VRAM + 28GB system RAM can generate 3072x2048 videos in 20-30 minutes using GGUF Q5
  - *From: The Shadow (NYC)*

- **RTX 5080 for audio workflows**
  - 16GB VRAM can generate 1000 frames of 1280x720px videos from audio
  - *From: meakwa23*

- **RTX 3060 12GB still viable**
  - Can run workflows with proper memory management, good value option
  - *From: U̷r̷a̷b̷e̷w̷e̷*

- **16GB VRAM performance**
  - Can handle 10-second FFLF at 1080p with memory optimizations
  - *From: Simonj*

- **32GB RAM limitation**
  - 32GB RAM insufficient for long video generation workflows
  - *From: Charlie*

- **2060 card capability**
  - Successfully generated up to 450 frames on RTX 2060
  - *From: hicho*

- **5080 16GB memory issues**
  - Struggles with controlnet, hitting memory issues where renders vary from 1-6 minutes
  - *From: VK (5080 128gb)*

- **GGUF model performance**
  - GGUF models are slower, FP4 is better alternative, but can help with memory constraints
  - *From: hicho*

- **RTX 3090 performance benchmark**
  - 589 seconds (around 10 minutes) to render 1280x720 i2v 15 second video with lipsync external audio
  - *From: nikolatesla20*

- **Generation time for 2-pass workflow**
  - ~3 minutes for generation, ~10-15 minutes for refinement
  - *From: N0NSens*

- **Higher resolution needs more GPU power**
  - User wishes for more computer power to make content at 1080p
  - *From: U̷r̷a̷b̷e̷w̷e̷*


## Community Creations

- **Snorricam LoRA** (lora)
  - Creates snorricam camera movement effect
  - *From: NebSH*

- **Switch Focus LoRA** (lora)
  - Changes focus between subjects in scene
  - *From: NebSH*

- **Bullet Time LoRA** (lora)
  - Creates Matrix-style bullet time effects
  - *From: NebSH*

- **Car Chasing LoRA** (lora)
  - Generates car chase sequences
  - *From: NebSH*

- **Through Object LoRA** (lora)
  - Camera moves through objects in scene
  - *From: NebSH*

- **62 camera motion LoRAs** (lora)
  - Collection including dolly out, 360 orbit, whip pan, crash zoom, dutch angle, flying, incline, crane shots, etc.
  - *From: NebSH*

- **Wallace and Gromit LoRA** (lora)
  - Character style LoRA working with LTX-2
  - *From: Cseti*

- **GalaxyAce LoRA** (lora)
  - Replicates early 2010s Samsung Galaxy Ace smartphone video style
  - *From: gopnik*

- **Amgery LoRA** (lora)
  - Custom trained LoRA by community member
  - *From: NebSH*

- **Audio input workflow** (workflow)
  - ComfyUI workflow for adding custom audio with timing controls
  - *From: Helikaon23s*

- **Deforum style LoRA** (lora)
  - LoRA trained by Safety Marc that adds deforum-style transformations and effects
  - *From: NebSH*

- **Character LoRA** (lora)
  - Double dolly + character LoRA for consistent character generation
  - *From: NebSH*

- **Detailer LoRA** (lora)
  - LoRA for enhancing detail in generated videos, costs $9 to train
  - *From: NebSH*

- **Hero shot LoRA** (lora)
  - 89 bucket training for cinematic hero shots
  - *From: NebSH*

- **Object POV LoRA** (lora)
  - Point of view from objects like microwave perspective
  - *From: NebSH*

- **Transition roll LoRA** (lora)
  - Fast rolling camera transitions sweeping between scenes, T2V tested
  - *From: NebSH*

- **Push to glass LoRA** (lora)
  - Camera effect LoRA
  - *From: NebSH*

- **Group photo LoRA** (lora)
  - Step 500 and 750 versions available
  - *From: burgstall*

- **Earth zoom out LoRA** (lora)
  - Step 500 and 1000 versions, shows zoom out from Earth
  - *From: burgstall*

- **Guitar playing LoRA** (lora)
  - For guitar playing scenes
  - *From: burgstall*

- **Timelapse Human LoRA** (lora)
  - Creates timelapse effects with humans
  - *From: NebSH*

- **Outfit check LoRA** (lora)
  - For outfit checking scenes
  - *From: NebSH*

- **Animatediff lora** (lora)
  - Creates animatediff-style effects, works well at strength 2.0, combines well with deforum loras
  - *From: NebSH*

- **Scooby Doo lora** (lora)
  - Character lora for Scooby Doo, creator planning to retrain from scratch
  - *From: 138234075931475968*

- **Anime character lora** (lora)
  - 700 steps out of 3000 training, showing typical anime motion
  - *From: Choowkee*

- **South Park lora** (lora)
  - Works with non-South Park prompts for style transfer
  - *From: NebSH*

- **TouchDesigner lora** (lora)
  - In training, intended for audioreactive output effects
  - *From: NebSH*

- **Beauty and the Beast lora** (lora)
  - Character lora showing good results
  - *From: JUSTSWEATERS*

- **Outfit switch LoRA** (lora)
  - Allows characters to change outfits during video, works well with other LoRAs
  - *From: NebSH*

- **Nuclear explosion LoRA** (lora)
  - Creates nuclear explosion effects
  - *From: NebSH*

- **Hand transition LoRA** (lora)
  - Creates smooth hand-based scene transitions, trained on only 6 videos
  - *From: NebSH*

- **Handheld run LoRA** (lora)
  - Creates handheld camera running motion effects
  - *From: NebSH*

- **Deep Zoom LoRA** (lora)
  - Creates deep zoom camera effects
  - *From: oumoumad*

- **Herocam LoRA** (lora)
  - Smooths out images, recommended for camera effects
  - *From: NebSH*

- **TouchDesigner + AnimateDiff LoRA combination** (lora)
  - Style and motion effects for psychedelic visuals
  - *From: NebSH*

- **Anime character LoRA training method** (lora)
  - Training with videos first, then continuing with images helps establish character likeness
  - *From: Choowkee*

- **Saturday morning cartoons LoRA** (lora)
  - 80s cartoon style LoRA for use with LTX
  - *From: U̷r̷a̷b̷e̷w̷e̷*

- **Static Camera LoRA** (lora)
  - LoRA for maintaining static camera shots
  - *From: nikolatesla20*

- **Negative training technique LoRA** (lora)
  - LoRA trained with negative strength (-1) for improved results
  - *From: 305792526629994496*

- **Audio normalization node** (node)
  - Analyzes video before segment and auto-normalizes audio to prevent volume spikes
  - *From: U̷r̷a̷b̷e̷w̷e̷*

- **Frame count calculator** (workflow)
  - Formula that calculates correct frame count following 8n+1 rule for given duration
  - *From: N0NSens*

- **AnimateDiff Lora for creepy effects** (lora)
  - LoRA for creating creepy/horror-style animations
  - *From: hell2heights2*

- **ComfyUI AudioTools** (tool)
  - Audio enhancement and normalization nodes with auto modes for V2V, requires resampy and soundfiles
  - *From: U̷r̷a̷b̷e̷w̷e̷*

- **VHS LoRA** (lora)
  - Trained on old VHS tapes from late 80s/early 90s with commercials and personal footage
  - *From: 305792526629994496*

- **LTX automation workflow with re-do feature** (workflow)
  - Full automation with ability to re-do specific scenes by index number
  - *From: VRGameDevGirl84*

- **12GB GGUF workflow collection** (workflow)
  - Complete set of GGUF-based workflows for t2v, i2v, v2v, ia2v, ta2v on 12GB cards
  - *From: U̷r̷a̷b̷e̷w̷e̷*

- **VCR LoRA** (lora)
  - Video generation LoRA trained on captioned dataset, latest version in testing
  - *From: 305792526629994496*

- **OIIA Spinning Cat LoRA** (lora)
  - First LoRA trained for LTX-2, includes sound effects
  - *From: 710895360981205003*

- **Music video automation workflow with SRT support** (workflow)
  - Automated music video generation using SRT files for scene timing
  - *From: VRGameDevGirl84(RTX 5090)*

- **Python app for SRT file creation** (tool)
  - App that plays song and lets you tap down arrow for cuts, creates SRT with start/end times
  - *From: VRGameDevGirl84(RTX 5090)*

- **Auto beat detection node** (node)
  - Node that adds cuts based on beats in songs, supports separate inputs for drums and bass
  - *From: VRGameDevGirl84(RTX 5090)*

- **Static camera control lora** (lora)
  - Helps prevent camera from wandering during generation
  - *From: Benjimon*
