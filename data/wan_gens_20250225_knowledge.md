# Wan Gens Knowledge Base
*Extracted from Discord discussions: 2025-02-25 to 2026-02-03*


## Technical Discoveries

- **720p model performs significantly better at native resolution**
  - Using 720p model at 480x480 produces poor results with flashing, but at proper 720p resolutions (1280x720, 720x720) produces very clean, consistent output
  - *From: wooden tank*

- **Chinese/Mandarin prompts work much better than English**
  - Multiple users confirmed that using Mandarin prompts produces significantly better adherence to prompts compared to English
  - *From: Monero*

- **1.3B model produces surprisingly good results**
  - 1.3B model performs on-par with or sometimes better than 14B for certain use cases like anime generation, and is much faster
  - *From: DiXiao*

- **Higher steps reduce artifacts significantly**
  - Testing showed that increasing steps from 30 to 50 to 100 progressively reduced artifacts in generations
  - *From: DiXiao*

- **Differential diffusion works with 1.3B model**
  - Soft mask inpainting technique can be applied to Wan 1.3B for localized style control without affecting composition
  - *From: spacepxl*

- **Torch compile requires Triton recompilation for RTX 5090**
  - RTX 5090 needs Triton compiled from latest source for sm120 architecture to enable torch compile
  - *From: Kijai*

- **Prompt adherence in 14B model is exceptional**
  - The 14B model shows insane prompt adherence compared to smaller variants
  - *From: ingi // SYSTMS*

- **Running 720p model at wrong resolution affects quality**
  - Was running the 720p model at 720x420 instead of 1280x720, which impacted results
  - *From: Zuko*

- **Last frame to first frame continuation workflow**
  - Workflow divided into sections where each last frame of current section is passed precisely to start of next section
  - *From: JmySff*

- **Long duration causes generation degradation**
  - Last frames become bad when duration is too long (91 frames mentioned)
  - *From: ingi // SYSTMS*

- **16:9 aspect ratio works better than other ratios**
  - Majority of dataset likely 16:9, performs much better than 4:3 or other ratios
  - *From: A.I.Warper*

- **Chinese prompts provide better adherence**
  - Longer prompts in Chinese show good adherence, though short English prompts also work
  - *From: DawnII*

- **Wan 1.3B model can handle 2048x2048 resolution**
  - Testing single frame video at various resolutions - 1024x1024, 1536x1536, 2048x2048 all work, but red squares appear at 1776x1776+
  - *From: DiXiao*

- **Wan 14B model supports 513 frames with sliding context**
  - 832x480 resolution, 513 frames using sliding context windowing with window size 81, overlap 16, took 50 mins on 5090
  - *From: Kijai*

- **TeaCache maximum steps is 209**
  - With 210 steps get errors, 500 doesn't work either
  - *From: DiXiao*

- **Context windowing and TeaCache are incompatible**
  - TeaCache works without activating context but can't use both together
  - *From: NebSH*

- **FP8 model performs as well as BF16 with half the time**
  - Testing GGUF, BF16 and FP8 720p I2V versions - FP8 looks just as good and takes half the time
  - *From: ShiftingDimensionsAI*

- **MultiGPU scaling works with Wan**
  - 1.85x to 1.9x scaling on 2 GPUs vs 1 GPU, no code changes required for both 1.3B and 14B models
  - *From: Kosinkadink*

- **Wan supports multiple languages**
  - Model understands Russian, Arabic, French and other languages, likely due to multilingual T5
  - *From: DiXiao*

- **720p width vs 768 width difference**
  - 720 pixel width produces better results than default 768x768 for 9:16 ratio generation
  - *From: ShiftingDimensionsAI*

- **TEACache has significant quality degradation**
  - TEACache values above 0.4 reduce quality noticeably, with 0.25 being a safer maximum. Some users avoid it entirely for best quality
  - *From: spacepxl*

- **14B model has better motion but 1.3B has better detail rendering**
  - 1.3B model at 50+ steps produces superior hair details and textures compared to 14B, but 14B has much better motion consistency
  - *From: spacepxl*

- **Sliding context windows now work with experimental implementation**
  - Kijai implemented a way to make sliding context windows work with Wan that didn't work before
  - *From: Kijai*

- **LoRAs don't work with TEACache in native workflow**
  - When using LoRAs with native ComfyUI workflow, TEACache causes issues and needs to be disabled
  - *From: Fred*

- **Image aspect ratio affects LoRA performance**
  - Squish LoRA only worked when using landscape orientation images, not portrait
  - *From: GalaxyTimeMachine (RTX4090)*

- **Wan 2.1 can work well with low-resolution training data**
  - LoRA trained at 168x350 resolution still produces quality results, showing model's ability to upscale effectively
  - *From: Juampab12*

- **Using nightly torch with fp16_fast provides speed improvements**
  - Upgrading to nightly torch and selecting fp16_fast in model loader node can reduce inference time
  - *From: BestWind*

- **Torch compile node can provide additional speed improvements**
  - Using torch compile node that was previously unused provided further performance gains
  - *From: BestWind*

- **Sage attention patch can cause black video output**
  - Disabling sage attention patch fixed black video generation issue
  - *From: 211685818622803970*

- **LoRAs can be trained from existing AnimateDiff clips**
  - Successfully used old AnimateDiff clips as training data for i2v LoRA training
  - *From: JohnDopamine*

- **T2V models are preferred by some users over I2V models**
  - User prefers experimenting with T2V models, finding them more telling of a model's capabilities
  - *From: Kytra*

- **Wan 2.1 can handle native 1920x1080 generation**
  - Direct inference at 1920x1080 is possible with 80GB VRAM, taking about 2 hours
  - *From: Benjaminimal*

- **Context window method works better for looping than loop-args**
  - Loop-args destroys quality, context options preferred for looping functionality
  - *From: Kijai*

- **Preview method helps optimize seed selection**
  - Can tell from preview if generation isn't doing what was hoped for, better to reroll than waste time
  - *From: Cubey*

- **Vehicle montage lora works better with lower CFG than previous training**
  - Testing different epochs showed this concept requires lower CFG settings for optimal results
  - *From: Kytra*

- **WAN can generate backwards motion from training data with certain seeds**
  - Found specific seeds where the motion direction is reversed from what was trained
  - *From: Kytra*

- **Character lora trained on just 4 HD images and 30+ video clips produces excellent results**
  - 1.3B character lora for Ryza trained on minimal data - 4 images plus 30 hand-picked 3-4 second video clips from gameplay
  - *From: Kytra*

- **WAN doesn't care about stretched/distorted aspect ratios during training**
  - Images can be resized to target resolution without preserving aspect ratio as long as captions are consistent
  - *From: Kytra*

- **Left pan lora can generate different pan types through prompting despite being trained on one movement**
  - Even with consistent camera movement training, can achieve horizontal, rotating pans through prompt variations
  - *From: ArtOfficial*

- **V2V with mask plus first frame inpainting embed using I2V 14B model works very well**
  - Combining masked V2V with first frame inpainting through I2V 14B produces high quality results
  - *From: IllumiReptilien*

- **WAN can be run at 150 frames for extended sequences**
  - Successfully generated 150 frame videos with the model
  - *From: 168373586812207104*

- **Control LoRA works well with 80% depth map and 20% grayscale original video blend**
  - Best results from control lora come from blending the original image in grayscale with depth map at 80% depth map and 20% grayscale
  - *From: Kytra*

- **Wan responds to i2v based on image aesthetic**
  - Wan itself seems to respond to i2v based on the aesthetic of the image, at least on anime ones - model inferred blanket from 'bedroom' context in prompt
  - *From: PolygenNoa*

- **res_2m sampler produces higher quality than UniPC**
  - Consistently gotten better results with res_2m with specific settings than uni pc, with similar runtime. Better coherence, structure, detail, fewer mutations
  - *From: Clownshark Batwing*

- **Bongmath sampling method provides significant improvement**
  - Makes each step sample forwards and backwards at the same time within the step, no performance hit but enormous difference in many cases
  - *From: Clownshark Batwing*

- **Multiple start frames work better than single frame for Fun InP model**
  - wan2.1-fun-1.3B-InP works really well with multiple frames instead of just 1 as start condition. Same seed with 1 start frame vs 5 start frames shows significant difference
  - *From: spacepxl*

- **Fun Control model has access to many preprocessors**
  - With the new Fun control model you can use preprocessors like lineart, dense pose, openpose etc to drive the video
  - *From: IllumiReptilien*

- **Fun models may be trained on different frame rate**
  - The Wan Fun models were trained on a different frame rate than the original model. Try 12fps playback instead of 16fps
  - *From: 片ヨ亡亡丹片*

- **8 steps produces good results for close-up people videos**
  - With close up videos of people doing basic motions it does really well at low steps from around 8 to 10
  - *From: Mr_J*

- **1.3B model can produce high quality results**
  - All high quality videos shown were using the base Wan2.1 1.3B model
  - *From: Ablejones*

- **VACE works with existing 1.3B LoRAs**
  - You can use pre-existing 1.3B LoRAs with VACE, but not with control-fun from the WAN team
  - *From: Kytra*

- **WAN 14B can handle ultra-wide panoramic shots**
  - Successfully generated 2500x500x69 and 500x2500x69 panoramic videos using FLUX -> Wan21-i2v720
  - *From: ZombieMatrix*

- **Dense prompts work better for T2V than simple prompts**
  - For T2V, more detailed prompts help guide the output better, while I2V doesn't need dense prompts since the image already captures context
  - *From: Amirsun(Papi)*

- **VACE enables style transfer in under 3 minutes**
  - What previously took 30+ minutes in warpfusion now takes less than 3 minutes with WAN + VACE
  - *From: Kytra*

- **Duplicating reference images strengthens VACE effect**
  - Haven't found a proper way to strengthen only the ref image, but duplicating it or giving multiple ones in different poses is interesting
  - *From: Kijai*

- **VACE encoder strength can be adjusted for better results**
  - Good results achieved by setting VACE encoder strength to 0.5-0.6
  - *From: TimHannan*

- **Wan can be used as an image generator with extreme aspect ratios**
  - Limited to 2048 width but can push far in height dimension. Images repeat but each repetition is unique
  - *From: Jas*

- **Fading out depth maps can be used for specific movements**
  - Used fading depth maps with prompting to make subject lie down
  - *From: Zuko*

- **Triangular attention mask keeps character consistency during scene changes**
  - Using triangular attention mask maintains character despite scene transformation
  - *From: Clownshark Batwing*

- **VACE works well for subject removal and background preservation**
  - Can remove subjects while keeping background elements like cars intact
  - *From: ArtOfficial*

- **Clownshark sampler (res_2m, res_3m) converges faster than standard samplers in terms of wall time**
  - res_3m and res_2m samplers make 1 model call and reuse 2 or 1 previous steps respectively, compared to res_3s/res_2s which make 3 or 2 model calls per step
  - *From: Clownshark Batwing*

- **Sliding window self-attention enables much longer video generation**
  - Can generate 601 frames (37.5 seconds) in one shot, taking 40 minutes on 4090. Normal attention sees every frame, but sliding window limits how many frames each frame can 'see'
  - *From: Clownshark Batwing*

- **VACE lineart input is inverted from ControlNet**
  - VACE requires black lines on white background, opposite of what you'd expect from ControlNet lineart inputs
  - *From: Kytra*

- **Higher step counts help with crowded or dynamic scenes**
  - Gold spot around 50-75 steps. If you see blurry animations with distorted elements, bump up steps. Only useful for complex scenes like many people or high speed chases
  - *From: Level Higher*

- **Wan can generate extremely wide resolutions like 3000x600 and 2500x500**
  - ZombieMatrix successfully generated ultra-wide videos using Flux->Wan pipeline, found these wide gens run faster than expected
  - *From: ZombieMatrix*

- **Wan as image generator works better with EmptySD3LatentImage than EmptyHunyuanLatentVideo**
  - EmptyHunyuanLatentVideo introduces more artifacting and noisier output when using Wan for single frame generation
  - *From: ZombieMatrix*

- **Custom sigma schedulers can dramatically improve movement in Wan**
  - Using custom scheduler nodes significantly increases movement quality, especially with 1.3B model
  - *From: 𝖑𝖚𝖈𝖎𝖋𝖊𝖗*

- **Diffusion Forcing models enable temporal coherence across multiple video segments**
  - 14B SkyReels DF model passes the 'windmill test' with 5 distinct generations maintaining coherence, 17 frame overlap used
  - *From: Ablejones*

- **cfg 1.0 uses positive prompt only**
  - Setting CFG to 1.0 makes the model use only the positive prompt, requiring double loading with one model handling positive and other handling negative
  - *From: Clownshark Batwing*

- **Sliding window attention allows 601 frames on 24GB**
  - Can generate up to 601 frames maximum with advanced Rewan patcher on 24GB VRAM, takes about 45 minutes, or 25 second clip in 30 minutes at 16fps
  - *From: Clownshark Batwing*

- **Bongmath sampling technique**
  - A technique that allows sampler to work forwards and backwards simultaneously, dramatically improving results without changing generation time or VRAM usage noticeably
  - *From: Clownshark Batwing*

- **Less quantized CLIP helps quality**
  - Using less quantized CLIP version actually helps improve results, though fp32 version may not be available for ComfyUI
  - *From: 88822364468412416*

- **Resampling powerful with Wan**
  - Resampling works very well with Wan models, especially useful when DF model gets funky - can fix issues like transforming 'triceratops foot to human hand'
  - *From: Ablejones*

- **VACE chops off a frame from input frames**
  - When using VACE, one frame gets removed from the input frames - unclear why this happens
  - *From: 88822364468412416*

- **TeaCache dramatically reduces generation time**
  - Dropped generation time from almost 2 hours to around 20 minutes for 1600x528, 85 frames, 50 steps
  - *From: 🏁🫰GridSnap*

- **Higher resolution input images may affect quality**
  - Using 1536x864 or 2048x1152 input images seems to improve generation quality even though images are auto-adjusted
  - *From: ezMan*

- **SageAttention impacts output quality**
  - Even SageAttention makes an unacceptable impact on output quality
  - *From: jdl_grmck*

- **Reward LoRAs make videos sharper and less chaotic**
  - Using reward LoRAs improves sharpness and reduces chaos in generations
  - *From: pom*

- **Base Wan LoRAs work with DF**
  - Regular Wan LoRAs are compatible with DF workflow without modification
  - *From: Cseti*

- **Wan can be used for image generation, not just video**
  - ZombieMatrix demonstrated using Wan T2V 14B model for high-resolution image generation at 5248x1040 resolution
  - *From: ZombieMatrix*

- **Wan is better at blending LoRAs than SD**
  - Successfully used two LoRA nodes set to 0.75 with all blocks enabled for clean blending
  - *From: ingi // SYSTMS*

- **res_2m/res_2s samplers work better with Wan than ksampler**
  - Better motion, fewer mutations, better prompt adherence, especially with bongmath enabled
  - *From: Clownshark Batwing*

- **VACE can extend videos using previous frames**
  - Used 21 frames from previous video to generate next 60 frames, tried 41 frames for more consistent movements
  - *From: DiXiao*

- **Wan has better efficiency for width than height in generations**
  - Can get a 5MP image around 5000x1000 in about half the time it takes to generate a 4000x2000 image
  - *From: ZombieMatrix*

- **Wan can generate single images by setting frames to 1 or using EmptySD3LatentImage**
  - Use t2v models like Flux for image generation
  - *From: ZombieMatrix*

- **CausVid can run with CFG 1.0 and only 4 steps**
  - CFG distilled model instead of usual 30 steps
  - *From: yi*

- **Wan 1.3B works well for tiled upscaling**
  - Can upscale from 480x480 to 1536x1536 using only 7GB VRAM with tiled approach
  - *From: Clownshark Batwing*

- **CausVid with 1.3B generates decent quality in under a minute**
  - Gets low-res gens in under a minute, decent resolutions in 2-3 minutes on 3080
  - *From: garbus*

- **Wan + VACE + CausVid combination works well**
  - 1 minute 30 seconds per video generation time
  - *From: ˗ˏˋ⚡ˎˊ-*

- **VACE + LoRA combination is very powerful**
  - Works well for style transfer applications
  - *From: ˗ˏˋ⚡ˎˊ-*

- **VACE maps reference based on inputs intelligently**
  - Uses prompt, image, and control inputs to determine what to take from reference vs what to generate
  - *From: ˗ˏˋ⚡ˎˊ-*

- **VACE understands context and selective reference usage**
  - If reference doesn't match prompt, it bails out and doesn't try to steer towards it
  - *From: ˗ˏˋ⚡ˎˊ-*

- **CausVid LoRA extracted from T2V works with I2V**
  - Kijai extracted a LoRA from the t2v model that works fine with i2v
  - *From: JohnDopamine*

- **VACE automatically trims reference latent**
  - The wrapper is coded to automatically trim the reference latent
  - *From: DawnII*

- **Context options enable consistent long generations**
  - Using context option in sampler allows for 14+ second consistent outputs
  - *From: 852話 (hakoniwa)*

- **VACE inpainting requires specific setup**
  - Need to fill masked area with gray (127) and provide mask to mask input
  - *From: ˗ˏˋ⚡ˎˊ-*

- **CFG scheduling can help with style LoRAs**
  - CFG at 1 hurts style loras, but WanVideo CFG Schedule Float List node can ramp up CFG in early steps to retain style
  - *From: Zlikwid*

- **Reference pose node retargets joints for characters with different proportions**
  - The reference pose node rescales the main pose against different character proportions, useful for non-standard human characters
  - *From: A.I.Warper*

- **Pose detector doesn't work on animated characters**
  - DWPose doesn't draw anything when run on animated character references
  - *From: Guey.KhalaMari*

- **VACE can handle dissimilar control inputs without override**
  - Even with very different control video and reference image inputs, VACE still produces coherent results
  - *From: Thom293*

- **Wan loses character likeness with longer sequences**
  - Character likeness degraded when generating 161 frames with context windows
  - *From: A.I.Warper*

- **VACE Skyreel 24fps is smoother than standard versions**
  - VACE Skyreel GGUF version at 24fps provides smoother motion compared to standard models
  - *From: Vérole*

- **CausVid works with VACE Skyreel**
  - CausVid LoRA at 0.3 strength works well with VACE Skyreel, fewer defects with 8 steps
  - *From: Vérole*

- **Merged speed LoRAs into Phantom model works well**
  - JohnDopamine merged causvid/accvid LoRAs into base Phantom model with LLM scripted standalone merger for speed improvements
  - *From: JohnDopamine*

- **CausVid with block 0 disabled works best**
  - Testing shows original CausVid LoRA with block 0 disabled (V1.5) performs better than V2 across the board
  - *From: JohnDopamine*

- **Context window 49 frames works better than 81 for some styles**
  - At 81 frames the model starts to understand it's looking at a human and bleeds through abstract style, 49 frames maintains style better
  - *From: Zlikwid*

- **Face + clothing consistency method**
  - Use big face shot plus clothed shot of same person together for character consistency in multiple scenes
  - *From: AJO*

- **VACE face fixing technique**
  - Do VACE with full body ref, crop out face from result, do VACE again with close-up face ref, stitch back - preserves outfit and face
  - *From: hau*

- **Multiple LoRA merging into single model**
  - VRGameDevGirl84 successfully merged CausVid, AccVid, MPS rewards, women enhancer, and realism LoRAs into single T2V model with optimal settings
  - *From: VRGameDevGirl84*

- **Shift parameter value of 1 works exceptionally well for natural realism**
  - VRGameDevGirl84 found shift=1 gives much better results for realistic content, while shift=3+ works for stylized content. For higher resolutions like 1080x720, increase shift by 1 (so 2-2.5 for realism)
  - *From: VRGameDevGirl84(RTX 5090)*

- **AccVid I2V LoRA significantly improves image-to-video results**
  - AccVid I2V LoRA is much better at retaining resemblance than T2V LoRA, fixes overblown colors, provides better prompt adherence and more fluid movement. Stable at higher strengths up to 4.0, with 2.0 being optimal
  - *From: Jonathan*

- **T2V gives better motion than I2V**
  - Text-to-video generation produces more dynamic movement compared to image-to-video
  - *From: Jonathan*

- **VACE can blend depth + dwpose control for better character animation**
  - Using repeat image batch to create gray frames blended with depth video reduces depth map strength, useful when outfit conflicts with character but dwpose alone is too glitchy
  - *From: MysteryShack*

- **TeaCache was causing generation issues in workflows**
  - MysteryShack discovered TeaCache was causing problems in generations, not the 40-50 frame count as previously thought
  - *From: MysteryShack*

- **Wan architecture may support audio tensors**
  - The Wan VAE has 16 channels and the technical paper indicates video-to-audio capability may be built into the architecture, with audio tensors potentially exposed in current models
  - *From: ZombieMatrix*

- **Wan has strong bias for width over height in generation time**
  - For highest resolution spectrogram chunks in least time, better to train them rotated 90-degrees and derotate on assembly
  - *From: ZombieMatrix*

- **Melspec audio encoding in video frames**
  - Can encode melspecs as strips on video frames for frame-accurate audio. Grayscale gives 8bit audio, mix of 2 colors gives 16bit, all 3 colors gives 24bit. For stereo need 2 separate melspec bands or overlay 2 colors (restricts to 8bit)
  - *From: ZombieMatrix*

- **AccVid has separate I2V version**
  - Must use I2V version of AccVid with reference images, using wrong version wrecks the image
  - *From: The Dude*

- **Moviigen may cause issues in I2V Phantom**
  - Even at 0.25 strength, minor detail increase isn't worth weird induced movement or loss of input likeness
  - *From: The Dude*

- **720p model training lacks lower resolution data**
  - If you generate too low resolution with 720p model you get hallucinations like white dots
  - *From: DawnII*

- **VRGameDevGirl84's I2V merge works differently than T2V merge**
  - Some LoRAs that worked in T2V merge did not work well in I2V, so different LoRAs and settings were used. Moviigen was removed because it didn't work right with I2V
  - *From: VRGameDevGirl84(RTX 5090)*

- **Resolution makes huge difference in quality**
  - 1024x576 is SO much better than 864x480. Higher steps really help quality, especially faces. 8 steps considerably better than 6, 10 is better but may not be worth extra time
  - *From: CaptHook*

- **First generations on close/mid shots don't need face fixes**
  - The quality at higher steps and resolution means first gens don't feel like they need face fix or swap because of eyes on close/mid shots
  - *From: CaptHook*

- **VRGameDevGirl84's I2V merge works well with LoRAs at only 3 steps**
  - Tested with various LoRAs and achieved good results with just 3 steps using the merge
  - *From: patientx*

- **GGUF Q3 model performs very well for text to video**
  - The fusionX gguf Q3 model produces super good results for T2V
  - *From: VRGameDevGirl84(RTX 5090)*

- **Phantom model was trained on 24fps data vs 16fps for base Wan**
  - This explains why Phantom generates smoother motion and higher quality video
  - *From: JohnDopamine*

- **Chinese prompts work better for some concepts**
  - 突然 碰撞 works much better for collisions than any English prompting
  - *From: garbus*

- **Self-Forcing model achieves 17 FPS on 1 H100 GPU with sub-second latency**
  - Uses KV caching + diffusion distillation, fixes autoregressive video diffusion's exposure bias by training on own outputs
  - *From: SS*

- **Fusion significantly reduces render times**
  - Instead of 15 minutes for 5 seconds video, now only 5 minutes
  - *From: Level Higher*

- **VACE with shift value adjustments controls realism vs motion**
  - Shift at 1 makes everything super realistic but static, shift at 5 gives less sharp but much more natural motion
  - *From: ingi // SYSTMS*

- **VACE can be combined with text descriptions for backgrounds**
  - Using ref for subject and text description for background allows any style of background that matches the subject
  - *From: ingi // SYSTMS*

- **Phantom has first frame quality issues that clear up**
  - First few frames look like crap then it clears up
  - *From: Gateway {Dreaming Computers}*

- **Bigger generation resolution improves quality**
  - The bigger the generation, the better the quality tends to get
  - *From: ingi // SYSTMS*

- **Prompts are extremely important for good results**
  - How insanely important prompts are when it comes to getting extremely good results
  - *From: ingi // SYSTMS*

- **Eye prompting dramatically improves eye quality**
  - If you put _anything_ about eyes in the prompt it makes them better. Doesn't have to be super detailed. Just 'long eyelashes' or 'big eyes' or 'magic eyes' is usually enough to improve them
  - *From: Thom293*

- **LightXv2 removes CausVid blotches at 4 steps**
  - At 4 steps it removes the causvid blotches (mostly) and adds some minor details
  - *From: Thom293*

- **Self Forcing LoRA adds or extends motion**
  - Adds or extends motion, fusion is good quality but has limited motion at least while using comfy nodes
  - *From: patientx*

- **Wan I2V shifts color more with red objects**
  - For some reason wan i2v will shift more when there is red coloring in the base image. Like a red dress, or a red object
  - *From: CJ*

- **WAN context options can generate long videos by repeatedly sampling chunks**
  - Using 81 context frames, can generate 1000 frame videos (~35 seconds) by repeatedly sampling 81 frames one after another until all frames are rendered
  - *From: Yae*

- **Black backgrounds work significantly better with VACE for motion tracking**
  - Black backgrounds allow VACE to follow control points much better than complex backgrounds, especially noticeable with complex motion
  - *From: Jonathan*

- **Higher FPS improves lip sync accuracy**
  - Using 60 fps helps with every word being pronounced, especially with rap music. 30 fps also improves sync over lower framerates
  - *From: patientx*

- **Multitalk needs adaptation time with high gain audio**
  - When starting with high audio gain, Multitalk needs time to adapt to text or sound, which is why it struggles at the start
  - *From: Charlie*

- **1xDeJPG upscale model yields best results for WAN video upscaling**
  - Tested all available upscale models, 1xDeJPG gave best results and is very fast for non-diffusion upscaling
  - *From: The Shadow (NYC)*

- **All 14B WAN models are somewhat compatible with other 14B LoRAs**
  - 14B Wan models can work with other 14B loras with varying results
  - *From: Ablejones*

- **Additional control information from depth/normal helps prevent LoRAs from drifting into body horror**
  - Using depth/normal maps alongside other controls prevents visual artifacts when using LoRAs
  - *From: Faust-SiN*

- **Multi-GPU setup allows longer video generation**
  - By loading clip, vae, and clipvision on 3090 and main model on 5090, can generate 289 frame video vs 173 frames on 5090 alone
  - *From: el marzocco*

- **Helper GPU power consumption drops after model loading**
  - Once helper GPU loads models, it goes to idle and runs at 30w while main GPU takes over computation
  - *From: el marzocco*

- **Plugging monitor into helper GPU frees up 2gb VRAM on main GPU**
  - Display output from secondary GPU preserves VRAM on primary generation GPU
  - *From: el marzocco*

- **VACE can understand content without prompts**
  - VACE restyle works with no prompt, understanding the content automatically
  - *From: hicho*

- **FusionX model has causvid built into it**
  - FusionX already includes causvid functionality, so external causvid LoRA shouldn't be stacked
  - *From: VRGameDevGirl84(RTX 5090)*

- **Wan loses consistency at 1080p like SD does at larger sizes**
  - Image structure consistency degrades at higher resolutions, but detail level improves
  - *From: ingi // SYSTMS*

- **LightX2V with 4 steps produces good results**
  - Found a good mix using LightX with 4 steps for faster inference
  - *From: VRGameDevGirl84(RTX 5090)*

- **Skyreels models are 24fps instead of 16fps**
  - Max frames is 121 instead of 81, but models are very human-centric
  - *From: Kijai*

- **Higher shift brings more motion but makes it 3D cartoon style**
  - Testing FusionX showed shift parameter affects both motion and visual style
  - *From: Atlas*

- **MPS heavily affects resemblance in I2V**
  - MPS parameter significantly impacts facial consistency in image to video generation
  - *From: Jonathan*

- **Resolution has major impact on generation quality**
  - Prompt adherence and overall motions are much better at higher resolutions, not just detail
  - *From: T2 (RTX6000Pro)*

- **VACE model was trained on specific shade of grey**
  - According to Kijai, VACE model was trained on mid-grey, which is why users typically use mid-grey for empty frames
  - *From: 783977668278222869*

- **VACE 1.3B vs 14B background editing capability**
  - VACE 1.3B couldn't edit the background while 14B could
  - *From: hicho*

- **14B model is much easier to deal with than 1.3B**
  - User found the 14B model significantly easier to work with compared to 1.3B with VACE
  - *From: Cseti*

- **Fast movement doesn't play well with FusionX LoRA**
  - Fast movement causes artifacts when using FusionX LoRA, even at high step counts. Better results with slower motion at ~10 steps
  - *From: Todd*

- **Context works with V2V in MultiTalk**
  - When using context, there's no frame limit for MultiTalk V2V generations
  - *From: N0NSens*

- **WAN VACE can handle 3D animations for restyle and material changes**
  - Using depth + canny as control video only, with prompts describing objects then background. Objects can interact with AI generation even if depth doesn't mention it, like water ripples being added from prompts
  - *From: hicho*

- **Custom depth and control passes from 3D software work better than ComfyUI-generated ones**
  - Custom Canny works more consistently and cleanly without glitches, no need to manually clamp or adjust value ranges. Same with custom depth and mask AOVs
  - *From: Andy Kush*

- **Black backgrounds in control videos act as automatic masking**
  - Used MJ jean video as control video with no masking - black areas activate AI generation without needing explicit masks
  - *From: hicho*

- **Depth map manipulation in Nuke enables advanced compositing control**
  - Can merge depth maps from different sources (dog video + street still) using Max operation to control object placement behind other elements
  - *From: T2 (RTX6000Pro)*

- **GGUF Q4 KS enables high resolution generation on lower VRAM**
  - Can do 600x480x81 frames without capping 6GB VRAM using GGUF Q4 KS format
  - *From: hicho*

- **Two-pass generation technique for more creative freedom**
  - First pass with low denoise (.65) gives model freedom to interpret prompts but lower quality. Second pass with high denoise (.95) tightens quality while keeping added elements
  - *From: T2 (RTX6000Pro)*

- **FusionX model excels at 4 steps with res_2s and bong tangent scheduler**
  - FusionX model is described as 'OP' and produces excellent results with just 4 steps using res_2s scheduler and bong tangent
  - *From: l҈u҈c҈i҈f҈e҈r҈*

- **WAN T2V model works well for image-to-image editing with low denoise**
  - Can use T2V model for i2i by inputting image to latent and lowering denoise to 0.50, with very low denoise (0.01) giving semi-real look
  - *From: hicho*

- **Different schedulers and shift values required for I2V vs T2V/VACE**
  - For normal VACE/VACE I2V use dpmpp_sde scheduler and shift around 1.5. For I2V (Wan2_1-I2V-ATI-14B) use flowmatch_causvid scheduler and shift at 5
  - *From: Atlas*

- **LightX LoRA strength should be lowered from default 1.0**
  - Lowering lightx strength from 1.0 consistently gives better motion, prompt adherence, and prevents over-beautifying
  - *From: garbus*

- **VACE inpainting uses specific RGB values for masking**
  - For input_frames: areas to change should be 127,127,127 RGB. For input_masks: areas to change should be white, areas to keep same should be black
  - *From: Hashu*

- **Higher FPS helps with fast motion handling**
  - Increasing FPS from base 16 to 30 handles fast motion very well, giving more frames to work with
  - *From: Nekodificador*

- **3D biped animations work directly with VACE without dwpose processing**
  - OpenPose-compliant mesh skinned to 3dsmax biped can be used directly in VACE without dwpose processing, providing 100% accuracy
  - *From: Duranovsky*

- **LightX2V works better than CausVid for realistic content and lighting dynamics**
  - LightX is designed for realism & lighting dynamics, far as I understand
  - *From: The Shadow (NYC)*

- **LightX2V can be used to speed up renders with minimal steps**
  - you can use it to speed up your renders.. you set your cfg to 1 and steps to 4 with lightx2v
  - *From: Gateway {Dreaming Computers}*

- **Lowering LightX LoRA strength prevents cross-batch degradation**
  - if you lower the lightX lora strength to something like 0.5 you dont get that cross batch degredation that compounds over time
  - *From: A.I.Warper*

- **Google Media Pipe provides excellent face landmarking for lip sync control**
  - Google media pipe is the tits. this is from face landmarking option and they have python code for video or webcam use
  - *From: mdkb*

- **VACE works well with depth control and multiple passes for complex effects**
  - Creates an organic, almost 3D mask with the first pass and uses that to drive the final output
  - *From: Sal TK FX*

- **Using very low resolution depth guide (128x64) prevents Wan from obsessing about detail while absorbing motion**
  - Allows keeping strength at 1.0 for reference image absorption without squeezing everything into depth reference dimensions
  - *From: Quality_Control*

- **Uni3C can extract camera motion from other videos**
  - Works for both camera and character motion transfer from reference videos
  - *From: hicho*

- **Chinese prompting works better for Wan models**
  - Comparison showed better results when prompting in Chinese vs English
  - *From: l҈u҈c҈i҈f҈e҈r҈*

- **VACE works with middle gray (RGB 127,127,127) for inpainting areas**
  - Apply mask to footage making masked part middle gray, VACE inpaints only the gray areas while leaving rest untouched
  - *From: Neex*

- **3D node recording works great with Uni3C for camera motion**
  - Can use 3D models purely for camera motion reference, making AI feel like 3D animation
  - *From: hicho*

- **Wan has an image generation model that was available from release**
  - Underutilized image model available on wan.video site with prompts and inspiration
  - *From: hicho*

- **Wan consistently associates 'bored' with specific look/gesture**
  - The word 'bored' produces predictable facial expressions and poses in T2V generations
  - *From: garbus*

- **Chinese translation of 'bored' (无聊的) gives inconsistent results**
  - The Chinese equivalent doesn't produce the same consistent results as the English word
  - *From: garbus*

- **Two-pass generation technique improves quality**
  - 4+4 steps (first pass + second pass) produces more detailed results than single pass
  - *From: patientx*

- **Fastwan LoRA works on top of LightX**
  - Can stack Fastwan LoRA with LightX for better results at lower steps
  - *From: patientx*

- **Wan 2.2 has high noise and low noise expert models**
  - MoE architecture separates high and low noise processing into different expert models
  - *From: patientx*

- **Second pass without LoRAs removes artifacts**
  - Running second pass with only LightX2V removes dot matrix artifacts from other LoRAs
  - *From: ingi // SYSTMS*

- **Wan 2.2 5B uses different VAE than 14B**
  - 5B model requires 2.2 VAE while 14B models use 2.1 VAE
  - *From: TK_999*

- **Wan 2.2 runs at 24 fps**
  - Confirmed framerate for 2.2 model
  - *From: GOD_IS_A_LIE*

- **First frame preservation in I2V**
  - 2.2 no longer destroys the first frame in I2V generations, eliminates disgusting motion blur
  - *From: GOD_IS_A_LIE*

- **Wan 2.2 excels at camera movements**
  - Model shows exceptional performance with camera movements and physics
  - *From: Fictiverse*

- **Motion issues fixed in 2.2**
  - No weird blur, legs don't blend, butterflies consistent, style picked up properly, no slow down
  - *From: 138234075931475968*

- **Character consistency improvements**
  - Multiple characters moving separately without phasing through objects or random artifacts
  - *From: 138234075931475968*

- **5B model generates very fast**
  - 5B model can be inconsistent but produces results in 9 seconds
  - *From: Benjaminimal*

- **Camera movement terminology works**
  - Industry terms like 'camera trucks in', 'dollies out', 'tilts up' are effective
  - *From: TK_999*

- **Upscaling workflow necessity**
  - For resolutions above 3 MPx, upscale + 2nd pass are mandatory as Wan starts to duplicate prompt elements or collapse
  - *From: 128578659047964672*

- **Wan2.2_I2V is the standout feature**
  - Atlas noted that I2V seems to be the star of the show compared to other capabilities
  - *From: Atlas*

- **2.2 handles lighting changes very well**
  - Model shows strong performance with cinematic lighting effects
  - *From: Zlikwid*

- **Cinematic prompting and lighting effects are the highlight of 2.2**
  - These are noted as the definitive strengths of the 2.2 model
  - *From: TRASHTRASH*

- **2.2 breathing new life into old prompts**
  - Previously used prompts work much better with the new model
  - *From: 138234075931475968*

- **The model removes things properly**
  - 2.2 shows improved ability to remove objects from scenes
  - *From: TK_999*

- **New model seems to listen best at 81 frames**
  - Benjimon found 81 frames to be the optimal length, requiring work in small chunks unless it's a really simple scene
  - *From: Benjimon*

- **2.2 did a good job animating an old photo**
  - Image to video with 720p lora produced good results on vintage photos
  - *From: 298806150353387520*

- **High noise is really the king of the architecture**
  - High noise sampler controls the main generation architecture while low noise just fills in details
  - *From: DawnII*

- **GGUF Q8 compatibility confirmed**
  - User successfully used GGUF Q8 with wrapper and Kijai's i2v example workflow modified for t2v
  - *From: Cseti*

- **Character LoRAs work better with only low noise model loaded**
  - User found their Panam character LoRA works better when only the low noise model is loaded, rather than both high and low
  - *From: 465174342225887233*

- **Wan 2.2 has excellent prompt adherence**
  - User reports spending less time gambling for good shots and more time getting work done due to better prompt following
  - *From: 273122300096937984*

- **Video upscaling workflow using latent feeding**
  - Take latent of uploaded video and feed to high-noise model. Start step 8-9 out of 12 for upscaling without changes, start step 4 for motion fixes and more changes
  - *From: thaakeno*

- **LightX2V does not work with 5B model**
  - Multiple users confirmed that LightX2V LoRA is not compatible with the 5B model
  - *From: 397653550345486337*

- **Without LightX2V results are more crispy**
  - User found that removing LightX2V gave crisper results, kept it only on low noise model
  - *From: NebSH*

- **Model performs best at larger sizes like 720p**
  - The model tends to do its best work at larger resolutions rather than smaller sizes
  - *From: ingi // SYSTMS*

- **New Lightning LoRAs v1.1 released with improved quality**
  - Wan2.2-Lightning_T2V-v1.1-A14B-4steps-lora_HIGH_fp16.safetensors and low variant available
  - *From: patientx*

- **I2V LoRAs work on 2.1 model with good results**
  - New 2.2 i2v lora is working so good on 2.1 model, though 2.2 model h n l are overwhelming
  - *From: hicho*

- **JSON prompting works with Wan 2.2**
  - Structured JSON prompts with time segments and visual descriptions produce good results
  - *From: AshmoTV*

- **Prompt weights are effective with Wan models**
  - Can use syntax like (vibrant streaks of electric... :2.0) to emphasize certain elements
  - *From: The Shadow (NYC)*

- **New AIO wan model released but has stability issues**
  - New release available but generations show erratic behavior, described as 'possessed'
  - *From: l҈u҈c҈i҈f҈e҈r҈*

- **VACE can work with multiple stylized frames for longer generations**
  - Generate short stylized sequences first, then use all frames in longer generation via frame extension
  - *From: Zuko*

- **Prompt scheduling with I2V is working well**
  - JSON prompting was working to some extent but model had problems recognizing exact timesteps and scenes. Simple timesteps followed by visual instructions works better than JSON format
  - *From: AshmoTV*

- **Wan 2.2 5B model has been fixed and works much better**
  - The new updated model on Kijai's repo does significantly better than the older 5B version
  - *From: l҈u҈c҈i҈f҈e҈r҈*

- **Wan 2.2 handles different styles well without LoRAs**
  - Style mixing test showed impressive results with various styles without requiring LoRAs
  - *From: R.*

- **Wan generates illustrations by default with certain prompts**
  - When no particular style is mentioned and CFG is used, Wan starts to imagine and creates illustration-style outputs. Adding 'photorealistic style, ultra details, 4K' helps get more realistic results
  - *From: N0NSens*

- **Two-pass workflow works better than default single-pass**
  - Using high_noise model for 4 steps, then second pass with 0.2 denoise using low_noise model for 2-3 steps gives better results than the normal workflow with denoise 1 on both
  - *From: patientx*

- **Wan 2.2 is also effective as a modern image generator**
  - Can generate text/words properly and works well for image generation tasks
  - *From: 132313738710614016*

- **Wan 2.2 has excellent low latent representation**
  - They trained at every level of the latent space, even down at 80x80 pixels. Best low latent representation out of any model hands down, including images.
  - *From: Fill*

- **Lightning LoRA performs well on RTX 3060**
  - 4 steps takes about 300 seconds (5 minutes) on RTX 3060, first generation takes longer due to model loading but subsequent gens are around 200 seconds
  - *From: Abx*

- **Stand-In LoRA causes videos to render at 24fps**
  - KJ mentioned this LoRA was making things 24fps because it was trained on 24fps data
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Context window works well for long videos on high VRAM**
  - Can generate 12 seconds straight with Wan 2.2 on RTX 5090, up to 19 seconds possible with good quality
  - *From: Charlie, ComfyCod3r*

- **LightX2V LoRA works at very low CFG**
  - User successfully running LightX2V with CFG 2, 6 steps
  - *From: NebSH*

- **Anime style LoRA trained on small dataset**
  - Custom anime LoRA trained on only 32 images from one show (368 screen captures + 79 video clips)
  - *From: 138234075931475968*

- **fp16 model significantly outperforms GGUF for Wan 2.2**
  - fp16 gives much better quality than GGUF versions, with user stating 'with wan2.2 the fp16 is OP'
  - *From: l҈u҈c҈i҈f҈e҈r҈*

- **Multi-resolution training technique for LoRAs**
  - Training LoRAs at multiple resolutions from 256 up to 1280 pixels produces better results
  - *From: Fill*

- **Two-stage upscaling workflow for better quality**
  - Generate at low res (512x256), pick best result, upscale in pixel space to 2048, then run through low noise model only at full resolution
  - *From: Fill*

- **Context window settings affect smoothness**
  - 121 frames for context gives better results than 81 frames for smoother transitions between windows
  - *From: xwsswww*

- **Multitalk significantly improves lip sync performance**
  - Adding Multitalk to Fantasy Portrait workflows dramatically improves mouth movement quality
  - *From: T2 (RTX6000Pro)*

- **Phantom model excels at character consistency in T2V**
  - HN model is amazing at following character descriptions, only LN stage uses Phantom for character consistency
  - *From: Ablejones*

- **InfiniteTalk can generate lip sync without driving video**
  - Uses only 1 image with MAGREF and InfiniteTalk, lipsync purely driven by audio file
  - *From: seitanism*

- **Wan 2.2 shows more detail than Wan 2.1 Control**
  - Direct comparison shows 2.2 is definitely much more detailed using same sampler
  - *From: Dream Making*

- **Split sigmas with latent noise runs fast on i2v**
  - Significant speed improvement observed
  - *From: l҈u҈c҈i҈f҈e҈r҈*

- **3 Sampler method with Wan-Lighting brings more motion**
  - Definitely makes a difference in bringing in more motion with 3min generations
  - *From: ArtOfficial*

- **Split sigmas technique with inject latent noise**
  - Testing 2 high + 4 low vs 4 high + 2 low configurations, with excess noise on right due to latent noise injection
  - *From: l҈u҈c҈i҈f҈e҈r҈*

- **Interpolation significantly improves video quality**
  - 2x interpolation using Topaz makes video look completely natural and real, especially helps with head movements
  - *From: A.I.Warper*

- **Wan 2.2 runs at 16fps with 81 frames for 5 second videos**
  - Confirmed frame rate and duration specifications
  - *From: U̷r̷a̷b̷e̷w̷e̷*

- **WAN 2.2 Lightning loras work with WAN 2.1 as speedup option**
  - Cross-compatibility discovered for acceleration
  - *From: Todd*

- **1600x900 resolution is sweet spot for fixing faces with Wan**
  - 720p can't quite do it, but 900p nails face fixing. Works well for crowd faces using Wan 2.2 Low noise model
  - *From: mdkb*

- **Phantom model excels at replicating exact details from references**
  - Underappreciated capability for precise reference matching
  - *From: Ablejones*

- **Orbit LoRA enables full 360-degree camera movement**
  - Using same image in first and last frame creates exact circle orbit
  - *From: 128578659047964672*

- **2+2 steps produces surprisingly good quality results**
  - When Wan 2.2 first came out, 2+2 was disliked, but later testing showed it works amazingly well for t2v
  - *From: U̷r̷a̷b̷e̷w̷e̷*

- **Pusa LoRA fixes slow motion issues with LightX2V**
  - Using Pusa LoRA with Wan 2.2 + LightX2V eliminates the slow motion artifacts
  - *From: .: Not Really Human :.*

- **Ultimate SD Upscaler with Wan destroys other upscalers**
  - Using Ultimate SD Upscaler with Wan T2V low noise model produces better results than Topaz or SeedVR2 for video upscaling
  - *From: 153803064858378240*

- **2.1 LoRAs don't work well on Wan 2.2 high model**
  - General compatibility issue between 2.1 and 2.2 versions
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Wan 2.2 lightx2v LoRAs have more issues than 2.1**
  - No perfect combo yet, but 2.2 on high and 2.1 on low is preferred
  - *From: ˗ˏˋ⚡ˎˊ-*

- **PUSA LoRA doesn't seem to affect I2V workflows**
  - User tested with and without PUSA and saw no change
  - *From: patientx*

- **GGUF Q3 conversions from BF16 can be effective**
  - Q3 around 7GB per model, considered 'low quality' but Q8 at fp8 size would be better
  - *From: patientx*

- **Q4 to Q6 GGUF have fairly good results**
  - User reports good results in this quantization range
  - *From: .: Not Really Human :.*

- **Q6 performs as well as Q8 for text encoder**
  - Someone tested and couldn't find difference between Q6 and Q8, Q5=fp8, Q6=Q8 according to test
  - *From: patientx*

- **Wan 2.2 T2V can do phantom-like effects**
  - Can achieve similar results to phantom model
  - *From: hicho*

- **Wan has issues understanding concept of taking a bite**
  - Food doesn't lose mass when animated eating, needs a LoRA
  - *From: BecauseReasons*

- **AMD users can run Wan with ZLUDA and native torch**
  - Part of AMD's upcoming 'the rock' pytorch environment, not as good as Nvidia but functional
  - *From: patientx*

- **PUSA extension potential discovered**
  - PUSA shows good potential for quality improvement in Wan 2.2 generations
  - *From: Mu5hr00m_oO (5080 + 64)*

- **Wan 2.2 14B working well with 6 steps using Pusa/Lightx2v**
  - Successful generation using Wan 2.2 14B T2V with 6 steps, Pusa/Lightx2v, plus Topaz and MMAudio post-processing
  - *From: . Not Really Human :.*

- **MPS and HPS LoRAs work with Wan 2.2**
  - MPS (boosts average image quality) and HPS (boosts human-perceived aesthetics) LoRAs designed for Wan 2.1 seem to work in some cases for 2.2
  - *From: . Not Really Human :.*

- **New Wan 2.2 MPS/HPS LoRAs released**
  - Official Wan 2.2 versions of MPS/HPS LoRAs have been released on Kijai's HuggingFace
  - *From: mdkb*

- **Tiling workflow for higher resolution processing**
  - Tiling approach allows processing at higher resolutions but requires careful padding to avoid seams
  - *From: 153803064858378240*

- **VAE tiling decode from ComfyUI core node causes flickering issues**
  - The core VAE tiling decode node is identified as the source of flickering problems in video generation
  - *From: 153803064858378240*

- **Wan 2.2 can be used as a text2image generator**
  - User tested Wan 2.2 as T2I and found it follows prompts better than Flux, Qwen etc. Used 1920x1080 30 steps res_2s with Clownshark sampler
  - *From: Simonj*

- **Core context window node now works**
  - The native core context window node is now functional for Wan, allowing for longer generation contexts
  - *From: l҈u҈c҈i҈f҈e҈r҈*

- **High noise works for Wan 2.1, but not low noise**
  - Wan 2.1 supports high noise training but not low noise, contrary to what some might expect
  - *From: 253611044595826688*

- **Training improvements with rank and noise settings**
  - Better training results achieved by lowering training speed, changing LoRA rank from 32 to 64, and using high noise
  - *From: 253611044595826688*

- **Resolution quality varies - lower can be better**
  - Different resolutions produce different qualities, sometimes lower resolution produces better results than higher
  - *From: mdkb*

- **WAN 2.2 tends to make outputs realistic even when trying to maintain artistic styles**
  - When using VACE 2.2 with stylized inputs, the model often converts them to photorealistic output instead of maintaining the artistic style
  - *From: 151330553629638656*

- **Mixing WAN 2.1 and 2.2 models can cause compatibility issues**
  - Using bf16 WAN 2.1 with WAN 2.2 Q8 GGUF models together in workflows can cause problems - keeping models aligned (same type/version) works better
  - *From: mdkb*

- **WAN 2.1 VACE maintains artistic styles better than 2.2**
  - For stylized content, WAN 2.1 VACE produces better results that stay closer to the input style compared to 2.2
  - *From: 151330553629638656*

- **VACE 2.2 has no degradation with context windows for extension**
  - Unlike other models, VACE 2.2 doesn't suffer from quality degradation when extending videos using context windows
  - *From: Vérole*

- **Frame length should be multiple of 16 + 1 for optimal results**
  - 81 frames is the sweet spot, and video length should follow the pattern of 16n+1 for best performance
  - *From: ingi // SYSTMS*

- **WAN Animate maintains facial expressions and input fidelity very well**
  - The WAN Animate model preserves subtle expressions and doesn't change the input image significantly while adding motion
  - *From: 151330553629638656*

- **Mixing pose and depth controls gives best results for VACE**
  - Using both pose and depth controlnets together provides better control and consistency than using either alone
  - *From: 𝕯𝖗. 𝕸𝖆𝖈𝖆𝖇𝖗𝖊 ☠*

- **Wan animate preprocessor improves eye target matching**
  - The wan animate preprocessor makes eye targets match the reference more closely
  - *From: AR*

- **Different face crops work well with wan animate**
  - Using different face crop inputs can produce good results
  - *From: hicho*

- **Wan 2.5 adds audio to image-to-video**
  - Unlike VEO3, Wan 2.5 allows adding audio to i2v generation
  - *From: VK (5080 128gb)*

- **Lightning LoRA causes super slow motion**
  - Lightning LoRA works but makes videos appear in slow motion for some reason
  - *From: ingi // SYSTMS*

- **Pose strength affects lip sync quality**
  - At pose strength 0.7, lip sync seems off, but at 0.2 it may be better depending on the seed
  - *From: Léon*

- **Wan 1280p generation maxes out around 65GB VRAM**
  - User reported hitting VRAM limits at 1280p resolution
  - *From: 767614506250665985*

- **Wan 2 steps generation capability**
  - Many generations can be done with only 2 steps
  - *From: Antonella The Princess*

- **Humo trained at 121 frames**
  - Model supports up to 121 frames natively
  - *From: Ablejones*

- **WanVideo Long I2V Multi node can be modified for better continuity**
  - By default uses only first frame, can be modified to use multiple frames for smoother transitions
  - *From: Rävlik*

- **1280p is a sweet spot for quality**
  - Users report good quality results at 1280p resolution
  - *From: 767614506250665985*

- **T2V LoRA works with I2V**
  - The new T2V LoRA can be used with I2V workflows successfully
  - *From: Benjimon*

- **VIT Pose detects animal skeletons**
  - VIT Pose in WanAnimatePreprocess nodes can detect animal skeletons, enabling WanAnimate to work with quadrupeds
  - *From: Nathan Shipley*

- **Context window method improves character consistency**
  - Using context window method helps with character likeness and consistency
  - *From: U̷r̷a̷b̷e̷w̷e̷*

- **New Lightning LoRAs improve T2V quality**
  - The updated lightning loras make t2v significantly better, with improved motion and less slow-mo issues
  - *From: U̷r̷a̷b̷e̷w̷e̷*

- **Dramatic camera changes can cause cut shots**
  - When prompting for very dramatic camera changes, T2V can produce cut shots within a single generation
  - *From: U̷r̷a̷b̷e̷w̷e̷*

- **Wan 2.2 dyno LoRAs with 2+2 steps setup**
  - Using dyno high model from lightx team and dyno low LoRA merged to wan 2.2 base model, running 2 steps for high and 2 steps for low
  - *From: hicho*

- **3 sampler setup improves cinematic quality**
  - Adding extra sampler with its own model load, no LoRA, and CFG 3.5 before the standard 2+2 setup makes results more cinematic
  - *From: garbus*

- **New dyno LoRAs make T2V worthwhile again**
  - The new lightning LoRAs have significantly improved text-to-video generation quality
  - *From: U̷r̷a̷b̷e̷w̷e̷*

- **Wan 2.2 i2v works well with GGUF Q4**
  - Image-to-video functionality working good since i2v LoRA release, compatible with GGUF quantized models
  - *From: hicho*

- **sa_ode_stable sampler improves prompt adherence**
  - Better image detail and more accurate prompt following, less bleed between concepts/characters
  - *From: garbus*

- **8 steps produces best quality results**
  - User found 8 steps optimal for generation quality
  - *From: hicho*

- **OVI model has issues with certain resolutions**
  - Generates static when trying to gen at 640x640 or 704x704
  - *From: U̷r̷a̷b̷e̷w̷e̷*

- **Wan 2.2 can be combined with OVI for enhanced results**
  - OVI + InfiniteTalk upscale pass for 3 steps maintains audio sync
  - *From: Kijai*

- **ComfyCloud provides significant speed improvements**
  - Real-time generation speeds compared to local hardware
  - *From: Vérole*

- **Video masking integration with Wan VACE depth**
  - Successfully implemented video masking for use with Wan VACE depth control
  - *From: hicho*

- **First Last Frame technique with upscaled frames**
  - Extract last frame from video, upscale to 2048x2048, then use as first frame for next video segment to maintain consistency
  - *From: The Coin Hunter*

- **Lightning LoRA high/low speed settings**
  - Use Lightning Lora high and low at strength 1 + Lora Lightning WAN2.1 at strength 3 on high and 0.25 on low, enables 4 steps with 2+2 samplers for good motion without slow motion
  - *From: Vérole*

- **909 frames long generation possible**
  - Generated 909 frames in 12, 77-frame windows at 1280x720 resolution
  - *From: A.I.Warper*

- **Colormatch option fixes color shift**
  - Gradual color shift in long generations can be fixed using colormatch option
  - *From: A.I.Warper*

- **VACE at super low step counts creates analog horror effects**
  - VACE with low step counts and weird settings produces interesting analog horror aesthetic
  - *From: Dream Making*

- **Vérole using Q8 model from merge of FP16 + lorawan2.2 + lorawan2.1**
  - Generated 4 steps 2*2 with this merged quantized model
  - *From: Vérole*

- **VACE interpolation can create smooth sequences with frame gaps**
  - Single 81 frame gen with 3 frame gaps between clips, no prompt needed
  - *From: ingi // SYSTMS*

- **HuMo works effectively without start image**
  - HuMo is technically based on I2V model but can generate videos without start image with no problem
  - *From: Ablejones*

- **HuMo excels at face replacement for similar faces**
  - Face replacement only works well if faces are somewhat similar, probably can't replace woman with blonde man
  - *From: Ablejones*

- **Two-stage face replacement workflow using VACE then HuMo**
  - Do rough replacement using VACE with reference and controls at high denoise, then refine with HuMo
  - *From: Ablejones*

- **Anime characters have issues with mouth scaling in WanAnimate**
  - Anime characters have smaller mouth shape and forcing normal human anatomical shape causes issues
  - *From: AR*

- **Lightx2v LoRAs (1022 version) bring good motion to Wan 2.2**
  - The 1022 Lightx2V I2V lora are pretty good and definitely bring the motion
  - *From: JohnDopamine*

- **Fill's RIFE node is significantly faster**
  - Easily 10x faster than other RIFE implementations
  - *From: Fill*

- **Wan 2.2 is better at prompt following than Wan 2.1**
  - Wan 2.2 is so good at prompt following that it did the groin shot every time, while it was almost impossible with Wan 2.1
  - *From: Ablejones*

- **res_2s sampling keeps quality significantly higher throughout extended generations**
  - Using res_2s sampling maintains quality better for longer HuMo generations
  - *From: Ablejones*

- **Last latent extraction requires specific node combination**
  - Use 'reverse latent sequence' + 'trim latent' to properly get the last latent frame instead of running through entire latent
  - *From: phant*

- **TensorRT RIFE is extremely fast**
  - Takes only 1-2 seconds for processing
  - *From: 591699889197678592*

- **Wan 2.5 performs better with no lora, 4 steps, cfg 2**
  - No lora on high gives better result, avoids same faces issue
  - *From: hicho*

- **SVI-shot reference image technique prevents image burning**
  - Keeps things very consistent but means less variations throughout generation
  - *From: Ablejones*

- **Wan 2.2 has frame limitations**
  - ATI is locked at 81 frames, errors when trying 121 frames
  - *From: AR/Fill*

- **Wan 2.2 smoothmix performs better than base + lora**
  - Generates higher quality output compared to using base model with loras
  - *From: hicho*

- **Long context prompts work well with Wan**
  - Wan loves long ass prompts broken down to segments
  - *From: hicho*

- **Effective workflow using I2V as edit model**
  - Using I2V model with 17-33 frames like using a long edit prompt, changes pose but makes what you want
  - *From: hicho*

- **Specific scheduler configuration improves results**
  - Running HN steps with no lora and CFG, using lightx for only LN with CFG 1
  - *From: Ablejones*

- **Length 121 frames automatically creates loops**
  - When generating 121 frames, Wan tends to automatically make a loop out of the video
  - *From: samurzl*

- **Humo can handle 257 frames for 10 seconds**
  - Single generation with 257 frames produces about 10 seconds of video, can even do 20 seconds but sync quality degrades
  - *From: reallybigname*

- **Time-to-Move works without masking**
  - TTM can be effective by just flipping images instantly instead of animating them slowly
  - *From: 153803064858378240*

- **Higher resolution drastically improves quality**
  - 1152x640 is hugely better than 960x540, quality improves drastically with resolution
  - *From: Simonj*

- **Contrastive loss training improves LoRAs significantly**
  - Training LoRAs with contrastive loss makes them way better even with very little training data
  - *From: samurzl*

- **Res 3S scheduler is a game changer**
  - Exponential samplers are less brutal in early steps when using Res 3S scheduler
  - *From: 𝕯𝖗. 𝕸𝖆𝖈𝖆𝖇𝖗𝖊 ☠*

- **High resolution inputs produce crisp videos**
  - Using crisp hires images results in crisp video output - quality is directly related to input resolution
  - *From: 𝕯𝖗. 𝕸𝖆𝖈𝖆𝖇𝖗𝖊 ☠*

- **OVI 1.1 combining video and audio in latent space gives more natural results**
  - The latent space combining video and audio at the same time gives much more natural results than separate processing
  - *From: MarkDalias*

- **Gemini 3 video captioning significantly improves LoRA training results**
  - Using Gemini 3 for video captioning made a big difference in training quality - 'it's kinda crazy how much good captions can do'
  - *From: ingi // SYSTMS*

- **Small dataset LoRA training can work with just 3 videos**
  - Successfully trained a water bending effect LoRA using only 3 videos from higgsfield dataset in 1.5 hours at 600 steps
  - *From: AshmoTV*

- **LightX2V VAE now works in native ComfyUI**
  - LightX2V VAE is now functional in native implementation and produces crisp results with Wan VAE
  - *From: hicho*

- **FFLF workflow with end image works better than start image for certain animations**
  - Using generated embroidery images as end point instead of start point allows model to interpret starting position of animation, useful for 'forming' animations
  - *From: AshmoTV*

- **Context window boundaries cause contrast changes in videos**
  - Contrast changes happen at context window boundaries, not VACE overlaps
  - *From: Ablejones*

- **Combining SVI 2.2 with Hard Cut lora enables scene cutting**
  - Can cut back to same scene if padding frames are set up properly, outdoor scenes look consistent across cuts
  - *From: Ablejones*

- **4 frame overlap reduces camera movement shifts**
  - 4 frame overlap between segments has small flashing but beats odd camera movement shifts from 1 frame overlap
  - *From: Ablejones*

- **WAN 2.2 GGUF Q4 works without block swap on 6GB VRAM**
  - Native ComfyUI with WAN 2.2 GGUF Q4 no longer requires block swap on 6GB cards
  - *From: hicho*

- **3 sampler setup improves dynamic movement**
  - Using extra sampler without speed LoRA improves successful dynamic fast movement generation
  - *From: dj47*

- **Long detailed prompts work better with WAN than short ones**
  - WAN actually likes long prompts, using AI prompt generators for detailed descriptions improves results
  - *From: hicho*

- **Wan 2.6 seems to upscale the first frame over time**
  - Observation that Wan 2.6 has a tendency to enhance or upscale the quality of the first frame as the video progresses
  - *From: hicho*

- **Context windows don't exhibit the same level of frying as built-in WanAnimate windows**
  - VACE context windows produce less degradation compared to the native WanAnimate context windowing system
  - *From: A.I.Warper*

- **Can combine Wan high model with other T2V models for style transfer**
  - Using Wan high model for 2 steps then Kandinsky or HY1.5 for additional steps at 0.5 denoise to change graphics while keeping motion
  - *From: hicho*

- **Wan 2.2 remix needs low model at less than 0.45 denoise to use both high and low models effectively**
  - If using light v2v denoising, you wouldn't employ the high model. For more high model usage, low model should be less than 0.45 denoise
  - *From: hicho*

- **HuMo doesn't need start image, only reference image**
  - HuMo is built from i2v model but designed to not use start image, only reference image. Using start image causes artifacts on first few frames
  - *From: Ablejones*

- **Suno lyric separation helps prevent mouth movement during non-speech sections**
  - Using Suno lyric separation reduces unwanted lip movement when there's no speaking
  - *From: VRGameDevGirl84(RTX 5090)*

- **First-middle-middle-last frame technique with Wan 2.2**
  - Using Wan 2.2 with first middle middle last frame logic for video generation
  - *From: VRGameDevGirl84(RTX 5090)*

- **SVI Pro + HuMo combination works well**
  - Using SVI Pro for Wan22 High Noise + SVI Film for HuMo as Low Noise creates good results
  - *From: Ablejones*

- **HuMo is surprisingly capable of generalizing concepts**
  - HuMo can handle whole scene references even without people when given a good starting point
  - *From: Ablejones*

- **Disabling sageattention on HuMo improves results**
  - Speech sync appears better and overall quality improved when sageattention is disabled on HuMo
  - *From: Ablejones*

- **Context windows can be used for morphing effects**
  - Injecting different references into each context window enables morphing and concept mixing
  - *From: Ablejones*

- **KJ implemented block specific attention in the wrapper**
  - DawnII has been experimenting with block specific attention combined with SVI
  - *From: DawnII*

- **SageAttention reduces audio drift in HuMo**
  - SageAttention has much less impact on audio-video sync compared to older versions, though segments after the first are more likely to have spurious mouth movements
  - *From: Ablejones*

- **Changing step counts on HN sampler can help with mouth movements**
  - Adjusting step counts prevents biasing mouth movements too much in HuMo generations
  - *From: Ablejones*

- **SVI extensions allow changing anchor images**
  - You can change the anchor image for each extension in SVI workflows, works most of the time but sometimes requires trying new seeds for seamless motion
  - *From: craftogrammer*

- **LTX to Wan v2v enhancement workflow**
  - Can skip LTX2 second stage and use Wan low v2v at 0.2 denoise with low model only for crazy detail results
  - *From: hicho*

- **GMFSS interpolation handles fast movement better than FILM**
  - FILM is good for smooth motion but horrible for fast movement, while GMFSS handles large motions much better
  - *From: brbbbq*

- **VACE doesn't like blurred masks**
  - You will get more artifacts around the edges with a blurred mask. Better to expand mask to cover bit of person but don't blur it
  - *From: Hashu*

- **SVI Talk LoRA improves InfiniteTalk**
  - SVI Talk LoRA helps with prompt adherence and motion compared to native InfiniteTalk alone
  - *From: 254379502879113216*

- **LTX2 to Wan v2v pipeline works for upscaling**
  - Can use LTX2 then Wan v2v for upscaling with low model and low latent denoise of 0.15
  - *From: hicho*


## Troubleshooting & Solutions

- **Problem:** RTX 5090 torch compile error with 'sm_120' not defined
  - **Solution:** Recompile Triton from latest source on Linux to support sm120 architecture
  - *From: Kijai*

- **Problem:** 720p model producing flashing results at non-native resolutions
  - **Solution:** Use proper aspect ratios - 720p model works best with 1280x720/720x1280, 480p model with 832x480/480x832
  - *From: intervitens*

- **Problem:** 1.3B T2V results appearing overcooked and too sharp
  - **Solution:** Try different schedulers like DPM++ SDE instead of DPM++, and increase steps to 30+ to reduce morphing
  - *From: burgstall*

- **Problem:** Image noise augment node causing grain
  - **Solution:** Turn off image noise augment node
  - *From: Zuko*

- **Problem:** Generations ending with glitches at 91 frames
  - **Solution:** Reduce duration length to avoid degradation
  - *From: NebSH*

- **Problem:** Fast setting not working
  - **Solution:** May need to download fp16 versions for model/vae/encoder
  - *From: AJO*

- **Problem:** Strange dots and murky appearance when zoomed in
  - **Solution:** Use higher steps (50) and fp32 instead of low steps and quantization
  - *From: Juampab12*

- **Problem:** VRAM usage on AMD/Zluda
  - **Solution:** UnetLoaderGGUFDisTorchMultiGPU + MultiGPUGGUF Dual Clip Loader nodes don't free VRAM for AMD users, works differently than Nvidia
  - *From: Screeb*

- **Problem:** Over-exposed lighting in generations
  - **Solution:** Try Shift=1 to improve lighting issues
  - *From: N0NSens*

- **Problem:** I2V workflow errors
  - **Solution:** Ensure 81 frames with same resolution are indicated everywhere for iv2v process
  - *From: DiXiao*

- **Problem:** FlowEdit not changing image enough
  - **Solution:** Use Florence to make structured base prompt, then edit parts you want changed in target prompt. Increase conditioning of target
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Problem:** LoRA not working with squish effect
  - **Solution:** Use landscape orientation images and include proper trigger words
  - *From: GalaxyTimeMachine (RTX4090)*

- **Problem:** Poor LoRA results in native workflow
  - **Solution:** Disable TEACache when using LoRAs - it causes interference
  - *From: Fred*

- **Problem:** Quality degradation with optimizations
  - **Solution:** Avoid high TEACache values, high shift settings, and very low step counts
  - *From: spacepxl*

- **Problem:** Black video output when generating
  - **Solution:** Disable sage attention patch
  - *From: 211685818622803970*

- **Problem:** CUDA out of memory errors
  - **Solution:** Reduce blocks_to_swap parameter (try 10, adjust based on VRAM)
  - *From: Fred*

- **Problem:** System freezing during generation
  - **Solution:** Likely running out of VRAM - balance blocks_to_swap parameter to fit VRAM with small margin
  - *From: Fred*

- **Problem:** Cannot use swap blocks and VRAM management together
  - **Solution:** These nodes cannot be connected together - use one or the other
  - *From: Fred*

- **Problem:** Slow generation times on 3090
  - **Solution:** Use proper memory management, 32GB RAM may be insufficient (40-50GB used), consider upgrading RAM
  - *From: Fred*

- **Problem:** Loop-args destroys video quality
  - **Solution:** Disable teacache and use context options instead for looping
  - *From: avataraim/Kijai*

- **Problem:** Uniform looped context window producing black frames
  - **Solution:** Ensure frames align well, use 169 total frames with 81 context window, 16 overlap
  - *From: Kijai*

- **Problem:** Low activity/boring animation in I2V
  - **Solution:** Try different seeds, explore for the right seed, use specific prompts mentioning movement
  - *From: Cubey*

- **Problem:** Strange grain/noise on renders
  - **Solution:** Increase step count from 20 - grain disappears in post-processing with Topaz upscaling
  - *From: Level Higher*

- **Problem:** Text/drawings flickering in video
  - **Solution:** Use more steps to reduce temporal inconsistency
  - *From: Juampab12*

- **Problem:** Single frame video generation showing black output in Kijai workflow
  - **Solution:** No specific solution provided in chat
  - *From: wayward_18*

- **Problem:** OOM errors on model loading with 4090
  - **Solution:** Set to offload_device in settings
  - *From: Kijai*

- **Problem:** Noise and artifacts in I2V generations
  - **Solution:** Disable teacache and Enhance A Video, try different samplers like euler, adjust step count to 45+
  - *From: Screeb*

- **Problem:** Getting grain/artifacts in renders at 20 steps
  - **Solution:** 20 steps is too light, bump up to 30 or 40 steps to clear up sampling issues
  - *From: Clownshark Batwing*

- **Problem:** ComfyUI disconnects when loading 14B model
  - **Solution:** Use GGUF files and appropriate quants for your VRAM
  - *From: A.I.Warper*

- **Problem:** Artifacts when using optimization settings
  - **Solution:** Looks like too strong SLG - lower CFG or smaller SLG range
  - *From: Kijai*

- **Problem:** 1 frame length doesn't work with Kijai's nodes
  - **Solution:** Just a black image output - issue needs investigation
  - *From: wayward_18*

- **Problem:** I2V output appears greyed out with old movie filter
  - **Solution:** Issue appears to be with conditioning/text encoder - need proper CLIP model
  - *From: PirateWolf*

- **Problem:** Missing text encoder causing dimension errors
  - **Solution:** Need umt5_xxl_fp8_e4m3fn_scaled.safetensors or fp16 version from Comfy-Org/Wan_2.1_ComfyUI_repackaged
  - *From: Ablejones*

- **Problem:** Last frame condition colors get screwed up
  - **Solution:** Last frame expects a first frame latent for the last frame condition, can't just encode first/last frame with gray frames in between
  - *From: spacepxl*

- **Problem:** Start and end images not working with Fun model
  - **Solution:** Need to use wrapper with KJ's fun toggle, or use proper native nodes for Fun InP model
  - *From: AJO*

- **Problem:** Strange grain/noise in renders
  - **Solution:** Check if using fp32 VAE and UNIPC sampler, may need to adjust TeaCache settings
  - *From: Level Higher*

- **Problem:** Garbled/splotchy video output that seems prompt-related
  - **Solution:** Problem was prompt being too long. Florence with 'more detailed caption' sometimes generates prompts that are way too long for the model
  - *From: ingi // SYSTMS*

- **Problem:** Control Video not working in Native without start-frame
  - **Solution:** If you're not using a start image you also shouldn't use the clip vision
  - *From: spacepxl*

- **Problem:** ComfyUI ops like tea sage fp8 causing issues
  - **Solution:** Disabling ops like tea sage fp8 fixes a lot of problems
  - *From: Benjimon*

- **Problem:** Camera panning causing loss of style in VACE
  - **Solution:** Issue mentioned but no clear solution provided
  - *From: 273122300096937984*

- **Problem:** Mask not working properly with VACE
  - **Solution:** Need to use specific node before VACE encode for mask to work
  - *From: Vérole*

- **Problem:** First frames having issues with VACE
  - **Solution:** Not fully resolved, acknowledged as ongoing issue
  - *From: TimHannan*

- **Problem:** DWPose being jittery for mouth movement tracking
  - **Solution:** Acknowledged problem, looking for better facial expression tracking techniques
  - *From: ArtOfficial*

- **Problem:** MediaPipe struggles with low resolution or distant subjects
  - **Solution:** Use higher resolution or closer subjects for better tracking
  - *From: ZombieMatrix*

- **Problem:** End frame not sticking when using ControlNet
  - **Solution:** Disconnect end frame when using ControlNet as it becomes useless
  - *From: Vérole*

- **Problem:** Getting cursed slowmo in video generation
  - **Solution:** Use specific workflow combinations and settings - one user found success with a particular workflow that avoided slowmo issues
  - *From: Quality_Control*

- **Problem:** VACE messing up video quality
  - **Solution:** Use low denoise pass (0.4 to 0.6) to clean up VACE output
  - *From: 88822364468412416*

- **Problem:** DG model not playing well with VACE for realism
  - **Solution:** Use regular T2V model instead of DG for better VACE results
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Problem:** Generation times being too long for 161+ frames
  - **Solution:** Use sliding window self-attention to reduce VRAM usage and enable longer generations
  - *From: Clownshark Batwing*

- **Problem:** Black outputs from FLF 720P model without TeaCache
  - **Solution:** Use 1.3B InP model instead, or check ComfyUI installation for issues
  - *From: 𝖑𝖚𝖈𝖎𝖋𝖊𝖗, yi*

- **Problem:** Face distortion in dancing animations
  - **Solution:** Turn off TeaCache for highest quality, use lower steps (not 100+), consider CFG scheduling with high CFG for first steps
  - *From: DawnII, N0NSens, artemonary*

- **Problem:** High step counts (100+) causing color blob artifacts
  - **Solution:** Drop to 30 steps with TeaCache enabled, 100 steps too much for high/wide resolutions
  - *From: ZombieMatrix*

- **Problem:** 14B SkyReels DF model OOMing immediately
  - **Solution:** Change TeaCache mode to 'e', reduce frame count if needed, use high block swap (38+)
  - *From: Ablejones*

- **Problem:** Quality degradation with overlap in long generations
  - **Solution:** Use 17 frame overlap by default instead of reducing it, avoid TeaCache for long generations
  - *From: Kijai*

- **Problem:** fp8_fast significant quality hit
  - **Solution:** Avoid using fp8_fast variant as there's a serious quality degradation that may not be obvious without A:B testing
  - *From: Clownshark Batwing*

- **Problem:** Hand/detail issues with stylized LoRAs
  - **Solution:** Increase image size so model has more to work with, increase step count, or adjust sigma schedule. Good sampling can only get best out of model weights
  - *From: Clownshark Batwing*

- **Problem:** Eye color changes in long generations
  - **Solution:** Use consistency models like Phantom or MagRef, or implement reference to previous generations to retain consistency
  - *From: Ablejones*

- **Problem:** LoRA strength above 1.0 introduces artifacts
  - **Solution:** Keep LoRA strength at 1.0 or below to avoid artifacts
  - *From: sneako1234*

- **Problem:** Artifacts in generations
  - **Solution:** Try lowering CFG number to reduce artifacting
  - *From: TimHannan*

- **Problem:** First frame noise issues
  - **Solution:** Problem with low denoised vid input in latent samples with 14b_t2v
  - *From: sneako1234*

- **Problem:** Chattering in camera pans
  - **Solution:** Lower SLG blocks from 10 to 8, or use lower teacache
  - *From: ezMan*

- **Problem:** Controlnet causing generation issues
  - **Solution:** User error - lineart controlnet was running and ruining generations
  - *From: sneako1234*

- **Problem:** Sampler freezes during generation
  - **Solution:** Not specified in the discussion
  - *From: Cross Product*

- **Problem:** Triton error causing generation to stop
  - **Solution:** Revert to CUDA 12.4.1 - remove nvidia/cuda packages, install cuda 12.4.1, install legacy drivers
  - *From: ZombieMatrix*

- **Problem:** Only getting 86 frames at 1024x576 with 24GB 3090
  - **Solution:** Upgrade to 64GB system RAM - workflows offload to system RAM and 32GB can be limiting
  - *From: ZombieMatrix*

- **Problem:** Camera prompts don't work consistently
  - **Solution:** N0NSens concluded it's 'pure randomness' after testing different i2v camera prompt options
  - *From: N0NSens*

- **Problem:** Wan sits forever at high resolutions like 5000 pixels wide
  - **Solution:** Dumps to system RAM, try lower resolutions like 3000 pixels wide
  - *From: ZombieMatrix*

- **Problem:** ComfyUI Wan wrapper installation fails
  - **Solution:** Try manual installation or use standard comfy nodes with teacache node
  - *From: ZombieMatrix*

- **Problem:** Sentencepiece compilation error in ComfyUI
  - **Solution:** Install Visual Studio Community or MS C++ Build Tools, or use --prefer-binary flag
  - *From: ZombieMatrix*

- **Problem:** CMake error during installation
  - **Solution:** Install cmake from official releases
  - *From: ZombieMatrix*

- **Problem:** Skip layer guidance disabled by ReWan patcher
  - **Solution:** Order of nodes doesn't seem to matter, may be incompatible
  - *From: 88822364468412416*

- **Problem:** Reference frame showing up in final output
  - **Solution:** Generation frame count was higher than driving video frames - match sampler frames to driving video length
  - *From: ArtOfficial*

- **Problem:** Reference frame appearing in output
  - **Solution:** First 3 frames are dropped by default in Kijai's workflow to combat this issue
  - *From: MilesCorban*

- **Problem:** VACE reference gets tacked to first latent
  - **Solution:** There are things to trim it off before decoding
  - *From: 88822364468412416*

- **Problem:** Line drawings becoming dark in output
  - **Solution:** Need to re-match colors of output, changing aspect ratio of input/output often leads to bad results
  - *From: DreamWeebs*

- **Problem:** Low quality with style LoRAs at CFG 1
  - **Solution:** Use WanVideo CFG Schedule Float List node to ramp up CFG in early steps
  - *From: Zlikwid*

- **Problem:** Dark stains appearing in video generations
  - **Solution:** Try avoiding teacache, zero star, and bypass shift - issue may be related to CausVid
  - *From: 88822364468412416*

- **Problem:** Reference pose not working with animated characters
  - **Solution:** Try scaling down the threshold value in the pose node
  - *From: Guey.KhalaMari*

- **Problem:** UNetTemporalAttentionMultiply does nothing with Wan
  - **Solution:** Use SLG (Skip Layer Guidance) in the wrapper instead, available under experimental args
  - *From: Kijai*

- **Problem:** VAE error with workflow
  - **Solution:** Remove 'Latent to Cuda' node or just remove it entirely
  - *From: hicho*

- **Problem:** OOM errors on 4090 with looping workflow
  - **Solution:** Use blockswap 40 and reduce resolution to 848x480
  - *From: Jas*

- **Problem:** Comfy crashes on 5060TI
  - **Solution:** Suspected FP8 to FP16 issue specifically with 5060ti architecture on linux, try using fp16 models with bf16 instead of fp16
  - *From: craftogrammer*

- **Problem:** CausVid V2 makes everything darker and less detailed
  - **Solution:** Revert to original CausVid LoRA (V1) or V1.5 with block 0 disabled for better quality
  - *From: Thom293*

- **Problem:** Face gets too small and loses reference with full body VACE
  - **Solution:** Use combination of close-up face shot and full body clothed shot, or do two-pass VACE process
  - *From: AJO*

- **Problem:** VACE inpainting fills person-shaped masks with people
  - **Solution:** Use rectangular masks instead of person-shaped masks for clean plate generation
  - *From: ArtOfficial*

- **Problem:** VRAM issues when removing blockswap
  - **Solution:** Blockswap is mandatory for VACE - removing it barely improves speed and risks running out of VRAM
  - *From: MysteryShack*

- **Problem:** Error when using VACE + Uni3C together
  - **Solution:** Disconnect Uni3C and use only VACE to resolve the issue
  - *From: Juan Gea*

- **Problem:** Cursed/poor quality generations
  - **Solution:** Check if resize made the video too small - this can cause fast generation but poor quality
  - *From: MysteryShack*

- **Problem:** Context options not allowing more frames
  - **Solution:** Use default settings in normal frame length field, ensure context parameters are set correctly, and use blockswap for longer sequences
  - *From: VRGameDevGirl84(RTX 5090)*

- **Problem:** OOM errors with longer frame counts
  - **Solution:** Enable block swapping and adjust resolution accordingly
  - *From: VRGameDevGirl84(RTX 5090)*

- **Problem:** White dots appearing in low resolution generations with 720p model
  - **Solution:** Try 640 resolution, use higher shift values, or add reward LoRAs to counter inconsistencies
  - *From: N0NSens/Jonathan*

- **Problem:** Detailz LoRA causing heads spinning backwards and odd movement
  - **Solution:** Avoid using or use at very low strength
  - *From: VRGameDevGirl84(RTX 5090)*

- **Problem:** Visible transition in middle of longer generations
  - **Solution:** Use Exvideo LoRA, context options, or add another generation with last frame
  - *From: Simonj*

- **Problem:** Burn-in like color effects and random dots in generations
  - **Solution:** Try shift of at least 2 for I2V instead of 1, use dpm++_sde/beta sampler, could be too low shift, too high causvid/accvid strength, or wrong model version
  - *From: Jonathan, VRGameDevGirl84(RTX 5090)*

- **Problem:** TeaCache not working - bad renders
  - **Solution:** User had TeaCache starting at last step (0.22). Should use values like 0.22, 0.1, 1.0 and not start at last step
  - *From: Kijai*

- **Problem:** Workflow showing model loaded but actually NULL
  - **Solution:** Check if model actually loaded by clicking on unet - if shows NULL, files may be misplaced on drive
  - *From: Level Higher*

- **Problem:** Uni_pc scheduler causing artifacts
  - **Solution:** Uni_pc needs simple scheduler, not normal scheduler
  - *From: izashin*

- **Problem:** OLLAMA issues in looping video workflow
  - **Solution:** Can be fixed via CMD commands
  - *From: Level Higher*

- **Problem:** Error: type fp8e4nv not supported in this architecture
  - **Solution:** Use fp8_e5m2 quantization for RTX 3090
  - *From: Guey.KhalaMari*

- **Problem:** Ghosting when Vace ref is too different from where model wants to place subject
  - **Solution:** Raising the shift value can help counteract this
  - *From: VRGameDevGirl84(RTX 5090)*

- **Problem:** Characters walking in reverse direction or wrong motion
  - **Solution:** More common in gens longer than 49 frames, try adding 'walking backwards' to negative prompt
  - *From: ingi // SYSTMS*

- **Problem:** Unable to merge LoRAs due to technical issues
  - **Solution:** Extract a LoRA from the merged fp16 model instead
  - *From: VRGameDevGirl84(RTX 5090)*

- **Problem:** Context options gives much worse output
  - **Solution:** Generate manually with 81 frame windows and stitch after
  - *From: Yae*

- **Problem:** OOM errors with looping workflow
  - **Solution:** Something wrong with the workflow that needs debugging
  - *From: Jas*

- **Problem:** Loading weights takes 20 minutes on second run
  - **Solution:** Disable torch compile, use Purge VRAM nodes
  - *From: ZeusZeus (RTX 4090)*

- **Problem:** First frames looking bad in Phantom
  - **Solution:** Issue not resolved, user has same problem
  - *From: ingi // SYSTMS*

- **Problem:** Frame count issues causing glitches
  - **Solution:** Use exact multiples of 16 frames, need math node to ensure always multiple of 16
  - *From: garbus*

- **Problem:** OOM when generating at 1920x1080 with Vace Encode
  - **Solution:** Need bigger GPU on Runpod or similar
  - *From: ingi // SYSTMS*

- **Problem:** Vace sticking to pose too much
  - **Solution:** Set Vace to 0.75 otherwise it stuck to the pose too much
  - *From: ingi // SYSTMS*

- **Problem:** Color variation between video chunks
  - **Solution:** Color match node helps, if not do it manually in davinci
  - *From: Yae*

- **Problem:** Kijai nodes causing memory problems
  - **Solution:** Most of the time cause memory problems for me
  - *From: patientx*

- **Problem:** NAG temp folder issues
  - **Solution:** Still running with this issue with NAG, even if I delete the temp folder
  - *From: Nekodificador*

- **Problem:** Yellow color outputs with ani-wan
  - **Solution:** Color match the reference image after inference, drop causvid and go with lightxv lora instead
  - *From: CJ*

- **Problem:** I2V model used with T2V workflow
  - **Solution:** VACE uses T2V model, not I2V
  - *From: Kijai*

- **Problem:** Multitalk has trouble with mashup words like 'wanna' and 'gonna'
  - **Solution:** Use higher audio gain (tried up to 3 from default 1) and add a full second at start for adaptation
  - *From: Thom293*

- **Problem:** Animation characters doing endless talking
  - **Solution:** Use LiveWallpaper LoRA at low strength to stop anime character endless talking
  - *From: Yae*

- **Problem:** Lens bokeh not looking good with upscaling
  - **Solution:** Consider using different upscale model instead of DeJPG for second pass when dealing with bokeh effects
  - *From: The Shadow (NYC)*

- **Problem:** Sync issue with control video data
  - **Solution:** There's a mismatch between where control video is sampled and frames used during inference, working on fixing the desync
  - *From: Faust-SiN*

- **Problem:** Jump during last segment
  - **Solution:** Result of scene transition that should have been cut out
  - *From: Faust-SiN*

- **Problem:** Motion image instability at 480p
  - **Solution:** Using gguf, fusionx, accvid and causvid lora - looking for methods to fix instability
  - *From: shockgun*

- **Problem:** Upscaling causes jitter background
  - **Solution:** Avoiding upscaling due to weird jitter artifacts in background
  - *From: AiGangster*

- **Problem:** OOM errors when trying longer videos
  - **Solution:** Breaking 44 seconds into 12s chunks with 2 seconds overlap to make it easier to blend
  - *From: voxJT*

- **Problem:** Audio length padding/interpolation issues with Multitalk
  - **Solution:** Issues when feeding short-form audio into multitalk encode node, moved on to other solutions
  - *From: CJ*

- **Problem:** Euler scheduler doesn't work well with VACE depth control
  - **Solution:** Avoid using Euler with VACE depth control
  - *From: Faust-SiN*

- **Problem:** People's facial features change in I2V
  - **Solution:** Issue might be related to moviigen or MPS settings
  - *From: zoz*

- **Problem:** Workflow images saved as webp instead of PNG
  - **Solution:** Use Discord app instead of browser, or click 'open in browser' then save PNG
  - *From: Hashu*

- **Problem:** Color gets darker and changes in I2V
  - **Solution:** Use color correction node to keep video same color as reference image
  - *From: VRGameDevGirl84(RTX 5090)*

- **Problem:** Low resolution tests don't translate to full res
  - **Solution:** Can't rely on low res tests as full res significantly changes performance
  - *From: T2 (RTX6000Pro)*

- **Problem:** OpenPose CN renders into output image
  - **Solution:** Can be resolution-dependent issue, sometimes resolves with step and shift changes over time
  - *From: Guey.KhalaMari*

- **Problem:** Getting OOMs when VACE was loading
  - **Solution:** Use tiled VAE to avoid OOMs and enable larger resolutions
  - *From: ingi // SYSTMS*

- **Problem:** Random dust and debris appearing in MultiTalk footage
  - **Solution:** No specific solution provided, but acknowledged as a known issue
  - *From: humangirltotally*

- **Problem:** Kontext ignoring prompts
  - **Solution:** Making keyframes is acknowledged as the hardest part, no specific solution given
  - *From: Ablejones*

- **Problem:** Color shift in extended WAN videos
  - **Solution:** Color shift is only apparent when subject is moving, can be fixed in post-processing
  - *From: 455300561034543105*

- **Problem:** CPU/GPU device mismatch errors
  - **Solution:** Happens when model runs on CUDA and other nodes run on CPU - remove the CPU node
  - *From: hicho*

- **Problem:** Depth Crafter causing device issues
  - **Solution:** Use Depth Anything instead of Depth Crafter to avoid device conflicts
  - *From: T2 (RTX6000Pro)*

- **Problem:** Camera following car instead of staying static in 3D renders
  - **Solution:** Add static objects like trees to lock camera in place when prompting for static camera
  - *From: Sal TK FX*

- **Problem:** Broken outputs when using tiling upscaler
  - **Solution:** Use non-tiling upscaler version, though this limits frame count on some GPUs
  - *From: Sal TK FX*

- **Problem:** Context shifts with MultiTalker
  - **Solution:** Try using without clip
  - *From: A.I.Warper*

- **Problem:** ATI model deviating from intended output
  - **Solution:** Use flowmatch_causvid scheduler and shift at 5 instead of default settings
  - *From: Atlas*

- **Problem:** OOM issues with WanWrapper nodes
  - **Solution:** Use WanWrapper nodes for better memory management and less OOM
  - *From: patientx*

- **Problem:** Depth mapping selective areas (like mouth only) causes white mist artifacts
  - **Solution:** Not resolved - user reports it's all or nothing for depth maps, can't mask just mouth areas
  - *From: mdkb*

- **Problem:** Workflow settings reset when updating KJ wrapper
  - **Solution:** Screenshot settings first before updating, then 'fix nodes' afterwards
  - *From: mdkb*

- **Problem:** VACE masking not working properly
  - **Solution:** Use LightX2V instead of CausVid LoRA, ensure mask isn't blurred, pad reference image with white border, use expand mask 20 with no blur
  - *From: Sal TK FX*

- **Problem:** Blurred masks don't work correctly in VACE
  - **Solution:** Don't blur masks because colors in blurred area are not 127,127,127
  - *From: Sal TK FX*

- **Problem:** ComfyUI Manager security error installing MMAudio
  - **Solution:** Download and extract zip manually instead of using manager
  - *From: N0NSens*

- **Problem:** FusionX LoRA causing issues with smoke effects and human faces
  - **Solution:** Try generation without FusionX LoRA
  - *From: hicho*

- **Problem:** Uni3C at full strength kills the prompt
  - **Solution:** Use 0.5 strength on Uni3C to preserve prompt better
  - *From: hicho*

- **Problem:** Floor cracks moving and zoom/morph at bottom
  - **Solution:** Use 3 steps radial attention at 2 to fix the issue
  - *From: hicho*

- **Problem:** VACE not working for object removal
  - **Solution:** Use pure black (#000000) for mask, white areas get altered by AI, prompt for background and removal
  - *From: 783977668278222869*

- **Problem:** 121 frame generations becoming unstable
  - **Solution:** Use 81 frames for better stability, 121 frames hit magic loop number causing issues
  - *From: Quality_Control*

- **Problem:** CUDA error with i2v Wan 2.2 workflow
  - **Solution:** CUBLAS_STATUS_NOT_SUPPORTED error when calling cublasLtMatmulAlgoGetHeuristic
  - *From: ZeusZeus (RTX 4090)*

- **Problem:** Wan wrapper slower than native on AMD GPU
  - **Solution:** User reports native implementation faster on AMD, wrapper better on NVIDIA
  - *From: patientx*

- **Problem:** Channel mismatch error with GGUF
  - **Solution:** Getting '36 channels but got 32 channels' error with GGUF, safetensors works
  - *From: phant*

- **Problem:** Wan 2.2 VAE doesn't work
  - **Solution:** User reports 2.2 VAE not working for them
  - *From: phant*

- **Problem:** MoE not working as intended
  - **Solution:** Issue with mixture of experts functionality, expected to be fixed
  - *From: Rainsmellsnice*

- **Problem:** Black screen in Kijai workflow
  - **Solution:** Use Kijai's model not ComfyUI ones - https://huggingface.co/Kijai/WanVideo_comfy_fp8_scaled
  - *From: 138234075931475968*

- **Problem:** Picture jump with LightX
  - **Solution:** Similar jumps occur when trying to generate 121 frames with LightX
  - *From: N0NSens*

- **Problem:** 1920x1080 impossible on RTX 5090
  - **Solution:** 
  - *From: GOD_IS_A_LIE*

- **Problem:** VACE doesn't work with Wan 2.2
  - **Solution:** 
  - *From: Sal TK FX*

- **Problem:** High model collapses sooner
  - **Solution:** 
  - *From: 128578659047964672*

- **Problem:** Many gens look burned due to steps/cfg issues
  - **Solution:** Need to adjust CFG and steps settings for cleaner results
  - *From: BecauseReasons*

- **Problem:** Need to crank high noise associated lora much higher with KJ's workflow
  - **Solution:** Use higher lora strength values with Kijai's workflow/nodes compared to native ones to get more action
  - *From: smithyIAN - 4080ti Super 16gig*

- **Problem:** Slow motion effect at 81 frames
  - **Solution:** Use higher fps, Lightx is trained for 24fps but sometimes 20fps looks better
  - *From: 128578659047964672*

- **Problem:** Snowflakes appearing in generations
  - **Solution:** Issue acknowledged but no clear solution provided
  - *From: Quality_Control*

- **Problem:** T2V morphs drawings and non-human illustrations into people with blank prompts in i2v
  - **Solution:** High noise model might be necessary for i2v unlike with t2v
  - *From: Rainsmellsnice*

- **Problem:** Grainy effect with KJ I2V Wan 2.2 workflow
  - **Solution:** User was helped but specific solution not detailed in messages
  - *From: cAItlyn GENner*

- **Problem:** Epoch 30 LoRA was bad quality
  - **Solution:** Use Epoch 10 LoRA instead which works better
  - *From: el marzocco*

- **Problem:** Broken faces and hands with morphing issues
  - **Solution:** Set CFG to 1 when using LightX2V, try different sampler like Euler, reduce LoRA strength
  - *From: Atlas*

- **Problem:** Clothing consistency issues in I2V
  - **Solution:** No specific solution provided, user asking for tips on maintaining cloth consistency
  - *From: iimate24*

- **Problem:** Motion issues at smaller resolutions
  - **Solution:** Use larger resolutions like 720p, try 4/4 steps instead of 2/2, lower LightX2V strength to 1.5 or 1, increase CFG on high noise to 3
  - *From: ingi // SYSTMS*

- **Problem:** Style transfer only works on very short generations
  - **Solution:** Use VACE frame extension - generate short stylized sequence first, then use those frames to extend longer video
  - *From: Zuko*

- **Problem:** Lightning LoRAs cause slow motion effects
  - **Solution:** Still being worked on, no clear solution yet
  - *From: TRASHTRASH*

- **Problem:** Black outputs when using sage with lightning
  - **Solution:** Disable sage when using lightning LoRAs
  - *From: l҈u҈c҈i҈f҈e҈r҈*

- **Problem:** Anime characters keep talking constantly
  - **Solution:** Try adding 'talking' to negative prompt, specify facial expressions, or give other actions that override talking
  - *From: garbus*

- **Problem:** Checkerboard pattern artifacts in generations
  - **Solution:** More present in v1.0 LoRAs, less in v1.1 version
  - *From: patientx*

- **Problem:** FLF has gaps between videos
  - **Solution:** No clear solution provided, seeking community input
  - *From: 312993351307755520*

- **Problem:** Background changes in video generation
  - **Solution:** User asking how to avoid this but no clear solution provided in the discussion
  - *From: NebSH*

- **Problem:** I2V gets burn in from light/dark values from input image on low noise step
  - **Solution:** Issue identified but no solution provided
  - *From: kendrick*

- **Problem:** Vace DWPose rig being ignored
  - **Solution:** 2.2 doing everything in its power to ignore a Vace DWPose rig - issue noted but no fix given
  - *From: ingi // SYSTMS*

- **Problem:** Man disappearing in I2V generations
  - **Solution:** Issue noted but no specific solution provided, seems to be intermittent
  - *From: NebSH*

- **Problem:** LoRA leaking between multiple characters
  - **Solution:** Observed when trying to prompt two characters with LoRA - it leaks between them
  - *From: NebSH*

- **Problem:** No decent open-source V2V lip-sync solution
  - **Solution:** Suggested using Wan VACE with driving video to DWPose conversion
  - *From: shockgun*

- **Problem:** Control not working on native Wan 2.2
  - **Solution:** User has solid native for normal 2.2 but control seems different and not playing nice
  - *From: Fill*

- **Problem:** Videos generating in slow motion
  - **Solution:** Always generate at 24fps instead of default, use 5*24+1 frame count
  - *From: Immac*

- **Problem:** Wan 2.2 context windows not smooth like AnimateDiff
  - **Solution:** Use 121 frames instead of 81 frames for context, and consider longer render times for better transitions
  - *From: xwsswww*

- **Problem:** Pattern artifacts appearing in 2.2 background
  - **Solution:** Affects background more than character, but no specific solution provided
  - *From: ingi // SYSTMS*

- **Problem:** GGUF models require more steps
  - **Solution:** GGUF needs more steps compared to fp16 models, which is why some users avoid it
  - *From: hicho*

- **Problem:** Fantasy Portrait characters mumble when source isn't speaking
  - **Solution:** No solution provided, acknowledged as known issue
  - *From: smithyIAN - 4080ti Super 16gig*

- **Problem:** Vace reference not working properly
  - **Solution:** Need to preprocess reference video and ensure output size doesn't crop character out
  - *From: ingi // SYSTMS*

- **Problem:** Lip movements too fast
  - **Solution:** Reduce speed of input video, then increase speed back to match audio after generation
  - *From: shockgun*

- **Problem:** VACE preprocessing issues
  - **Solution:** Use ControlnetAUX AIO node with DepthAnything V2 preprocessor for image preprocessing
  - *From: ingi // SYSTMS*

- **Problem:** Wrong frame numbers for Wan
  - **Solution:** Wan expects frame numbers to be multiples of 16+1, so use 33 or 49 instead
  - *From: ingi // SYSTMS*

- **Problem:** Color shifting during generation
  - **Solution:** Use color correction node between every ksampler and pull color reference from initial frame
  - *From: Zlikwid*

- **Problem:** Multitalk doesn't work in French
  - **Solution:** Fantasy + multitalk works in French after some troubleshooting
  - *From: 𝕯𝖗. 𝕸𝖆𝖈𝖆𝖇𝖗𝖊 ☠*

- **Problem:** Characters talking constantly
  - **Solution:** Add 'talk', 'speech', 'talking', 'speaking' to negative prompt
  - *From: NebSH*

- **Problem:** Low VRAM handling for upscale/interpolation
  - **Solution:** Use meta batch node to break down parts for upscaling/interpolation, making it easier for 4GB VRAM
  - *From: AiGangster*

- **Problem:** GGUF models not recognized by nodes
  - **Solution:** Need to be on nightly branch and use GGUF models in diffusion models folder. If using GGUF main model, must use GGUF infinitetalk model
  - *From: DawnII*

- **Problem:** OOM issues with InfiniteTalk
  - **Solution:** Update to nightly branch and reload browser
  - *From: DawnII*

- **Problem:** Lightning generation issues
  - **Solution:** Take a frame or 3, inpaint lightning, composite back with bright frames for lightning flash effect rather than relying on model
  - *From: 177039592808120321*

- **Problem:** res_2m sampler giving too much noise
  - **Solution:** Use res_2m/beta instead of bong_tangent for 10 steps as bong_tangent is too aggressive
  - *From: Ablejones*

- **Problem:** Losing character likeness with VACE/Phantom
  - **Solution:** Need to balance conditioning with VACE and phantom embed tensors being different sizes, mostly use phantom in the mix
  - *From: 88822364468412416*

- **Problem:** Lightning lora reducing or removing motion and camera motion
  - **Solution:** Remove the HIGH lora or decrease strength to 0.5
  - *From: . Not Really Human :.*

- **Problem:** Burning and swirly lines in output
  - **Solution:** Caused by too many steps with distill loras or too high CFG
  - *From: Kijai*

- **Problem:** Native S2V workflow lagging like wan demo
  - **Solution:** Use KJ wrapper which fixes the slow issues
  - *From: hicho*

- **Problem:** First frames corrupted in native workflow
  - **Solution:** Switch to KJ wrapper to avoid corrupted first frames
  - *From: Fictiverse*

- **Problem:** Character likeness lost during VACE upscaling
  - **Solution:** Use another VACE workflow to add character faces back in
  - *From: mdkb*

- **Problem:** 5B VAE taking longer than sampling time
  - **Solution:** Complaint noted but no solution provided
  - *From: l҈u҈c҈i҈f҈e҈r҈*

- **Problem:** S2V sync issues with loras
  - **Solution:** Beginning to think loras are causing sync problems, testing different fps
  - *From: U̷r̷a̷b̷e̷w̷e̷*

- **Problem:** No speedup LoRAs allowed on high noise
  - **Solution:** Period. At all. Also CFG 1 is not allowed on high noise - must use full CFG for first majority of steps
  - *From: MysteryShack*

- **Problem:** Bad branch of wrapper causing burnt low noise output
  - **Solution:** Switch to correct branch of wrapper
  - *From: aipmaster*

- **Problem:** Cartoon bird appearing instead of realistic small bird
  - **Solution:** Need better prompting to avoid Disney-style birds
  - *From: 441459285759754250*

- **Problem:** OOM issues with Q8_0 version on 24GB VRAM
  - **Solution:** Use Q6_K version instead, can also disable sage or torch behind ksampler
  - *From: asd*

- **Problem:** Black output when using multi-mask setup in InfiniteTalk
  - **Solution:** 
  - *From: U̷r̷a̷b̷e̷w̷e̷*

- **Problem:** Slow motion effect returning at higher steps
  - **Solution:** 
  - *From: 𝕯𝖗. 𝕸𝖆𝖈𝖆𝖇𝖗𝖊 ☠*

- **Problem:** InfiniteTalk very slow on first generation
  - **Solution:** 
  - *From: U̷r̷a̷b̷e̷w̷e̷*

- **Problem:** Wan makes everything look HDR burned
  - **Solution:** 
  - *From: BecauseReasons*

- **Problem:** Weird flickering when upscaling
  - **Solution:** 
  - *From: 153803064858378240*

- **Problem:** Point cloud-like artifacts in 2.1
  - **Solution:** 
  - *From: ingi // SYSTMS*

- **Problem:** Topaz Starlight won't download locally
  - **Solution:** Use Topaz Proteus instead, as Starlight is too slow and unusable for most purposes
  - *From: . Not Really Human :.*

- **Problem:** Choppy motion after upscaling
  - **Solution:** Try reducing interpolation gap (16 to 50fps instead of 60fps) and doing 2x upscale instead of larger
  - *From: . Not Really Human :.*

- **Problem:** Warping issues with dpmpp_2m sampler
  - **Solution:** Try switching from dpmpp_2m to Euler sampler with beta scheduler for more stable results
  - *From: . Not Really Human :.*

- **Problem:** Slow motion effect with MPS/HPS LoRAs
  - **Solution:** Reduce strength - try 0.5 instead of 1.0, or disable on high noise and use 1.0 on low noise only
  - *From: GalaxyTimeMachine (RTX4090)*

- **Problem:** Custom nodes import errors
  - **Solution:** Comment out problematic import lines (like line 28) or update DEV branch with missing lib folder
  - *From: VRGameDevGirl84(RTX 5090)*

- **Problem:** Seams in tiled processing
  - **Solution:** Make sure to increase padding when using tiling workflows
  - *From: 153803064858378240*

- **Problem:** OOM errors during generation
  - **Solution:** Increase block_to_swap parameter (0 to 40 max)
  - *From: .: Not Really Human :.*

- **Problem:** OOM errors with native version
  - **Solution:** Reduce steps to 2 and decrease tile size height/width. Use 512x512 tiling with 2 steps, keep denoise at 0.1 or lower to avoid artifacts
  - *From: mdkb*

- **Problem:** Visible tiling artifacts in upscaling
  - **Solution:** Increase tile padding to 96-128 to reduce seams between tiles
  - *From: 153803064858378240*

- **Problem:** High RAM usage during tiling
  - **Solution:** Increase tile count (disable preview for speed) and use context window node set to around half of total video frames
  - *From: 153803064858378240*

- **Problem:** VACE control videos being ignored
  - **Solution:** Use gray images (127,127,127 or 50% gray) between frames instead of black images, or use the Vace start/end frame node
  - *From: ingi // SYSTMS*

- **Problem:** VACE compatibility issues
  - **Solution:** Ensure VACE and WAN models are the exact same type (e.g., all fp8_e5m2) to avoid compatibility problems
  - *From: mdkb*

- **Problem:** WAN 2.2 converting artistic styles to realistic output
  - **Solution:** Remove 'intricate details' from prompt and add 'realism' to negative prompt. Consider using WAN 2.1 VACE instead for better style preservation
  - *From: ingi // SYSTMS*

- **Problem:** VACE mask not working properly
  - **Solution:** Ensure mask is connected and inverted before plugging into the workflow
  - *From: ingi // SYSTMS*

- **Problem:** Control inputs degrading style when combined
  - **Solution:** Ensure control inputs match the style frames in composition and are generated from the same source video
  - *From: ingi // SYSTMS*

- **Problem:** Reference image popping back every 81 frames with context windows
  - **Solution:** Use overlap of 10 frames and proper blending nodes to create smooth transitions between context windows
  - *From: Vérole*

- **Problem:** GGUFS compatibility issues with VACE
  - **Solution:** VACE may not work properly with GGUF models - fp8 e3m2 models recommended instead
  - *From: mdkb*

- **Problem:** ComfyUI randomly stopped working with mixed models
  - **Solution:** Use same model types and versions for both VACE and WAN components - don't mix bf16 2.1 with Q8 GGUF 2.2
  - *From: mdkb*

- **Problem:** Mouths moving during silence with 2 steps
  - **Solution:** Use 4 steps instead to eliminate mouth movement during silent parts
  - *From: 1348584179440418868*

- **Problem:** Glitching at scene changes
  - **Solution:** Expected behavior when scene changes occur in the video
  - *From: U̷r̷a̷b̷e̷w̷e̷*

- **Problem:** Second to last frame glitching
  - **Solution:** Need to retrieve the second to last frame to stop the glitching
  - *From: The Coin Hunter*

- **Problem:** Person in foreground gets mangled by mask
  - **Solution:** Sometimes works, sometimes doesn't when trying to replace people not in foreground
  - *From: U̷r̷a̷b̷e̷w̷e̷*

- **Problem:** Content blocked for celebrities
  - **Solution:** Complete face swap works, but minor modifications like changing hair color or race aren't enough to bypass detection
  - *From: Jas*

- **Problem:** GPU running hot at 1280p
  - **Solution:** Need to figure out better cooling for GPU
  - *From: 767614506250665985*

- **Problem:** Slow motion results with Wan 2.1/2.2 I2V
  - **Solution:** No specific solution provided, user asking for suggestions
  - *From: army*

- **Problem:** Darker frames at beginning of Humo clips
  - **Solution:** Use settings from VRGameDevGirl to resolve
  - *From: 𝕯𝖗. 𝕸𝖆𝖈𝖆𝖇𝖗𝖊 ☠*

- **Problem:** Poor lipsync results
  - **Solution:** Turn off SageAttention, especially in native workflows
  - *From: Ablejones*

- **Problem:** Juan Gea getting 'samples' error when porting 2.1 template to 2.2
  - **Solution:** No specific solution provided in this chunk
  - *From: Juan Gea*

- **Problem:** Quality degradation and color issues over time
  - **Solution:** Use context windows to maintain quality consistency
  - *From: AR*

- **Problem:** VACE dual model compatibility issues
  - **Solution:** Ensure model format consistency (avoid mixing bf16 vace with fp8 main model)
  - *From: mdkb*

- **Problem:** Doubled LoRA causing quality issues
  - **Solution:** Check for accidentally duplicated LoRAs in workflow
  - *From: U̷r̷a̷b̷e̷w̷e̷*

- **Problem:** Character ID loss with CFG steps
  - **Solution:** Train a LoRA for faces when doing character-specific work
  - *From: ingi // SYSTMS*

- **Problem:** Fast film grain node missing after update
  - **Solution:** Python file got overwritten, fixed by restoring the file
  - *From: VRGameDevGirl84(RTX 5090)*

- **Problem:** Chinese negative prompts too aggressive in 3 sampler setup
  - **Solution:** Be careful with default Chinese negative prompts (慢动作, 字幕, 静态, 画面, 静止, 静止不动的画) as they work very strongly and can be dangerous
  - *From: garbus*

- **Problem:** WanAnimate long generations running out of RAM
  - **Solution:** Need more than 64GB RAM for long generations without context - 128GB recommended for storing all frames in memory with offloading
  - *From: Charlie*

- **Problem:** WanAnimate overexposure issue
  - **Solution:** WanAnimate tends to overexpose characters slightly in output
  - *From: Charlie*

- **Problem:** Pig dancing with human pose not working
  - **Solution:** Model can't detect pig face properly for human poses - try using kontext to make pig stand instead
  - *From: hicho*

- **Problem:** Color shift between clips from various origins
  - **Solution:** Consider using upscaler workflow to reduce grading shift between clips
  - *From: 𝕯𝖗. 𝕸𝖆𝖈𝖆𝖇𝖗𝖊 ☠*

- **Problem:** Depth control giving vignette effect
  - **Solution:** Need to find way to improve depth, issue not resolved
  - *From: hicho*

- **Problem:** Model sitting at 0% before moving with high VRAM
  - **Solution:** Use block swap to make generation go faster
  - *From: VRGameDevGirl84(RTX 5090)*

- **Problem:** DWPose preprocessor leaking into video
  - **Solution:** Lower VACE strength (though specific fix was forgotten)
  - *From: Dream Making*

- **Problem:** Wan video blender deteriorating source over time
  - **Solution:** Avoid using the blender node as it corrupts beginning frames the more clips are merged
  - *From: 𝕯𝖗. 𝕸𝖆𝖈𝖆𝖇𝖗𝖊 ☠*

- **Problem:** Camera angle changes difficult with I2V
  - **Solution:** Use Uni3c, controlnet with depth maps/DW pose, or 3D modeling in Blender to control camera movements precisely
  - *From: mdkb*

- **Problem:** Character consistency in camera rotations
  - **Solution:** Models tend to rotate objects instead of camera view, better to use 3D modeling approach
  - *From: mdkb*

- **Problem:** Fade-in issues in morphing sequences
  - **Solution:** Specifically forbid fade-in in workflow, focus on mutation and morphing only
  - *From: 𝕯𝖗. 𝕸𝖆𝖈𝖆𝖇𝖗𝖊 ☠*

- **Problem:** Unmatching colors between last and first frames
  - **Solution:** Use prompts with camera controls and color palettes to manage transitions
  - *From: The Coin Hunter*

- **Problem:** LLM prompt not working correctly after resolution change
  - **Solution:** LLM morphing worked in 832x480 but failed in 720p, issue was lost prompt when changing resolution
  - *From: 𝕯𝖗. 𝕸𝖆𝖈𝖆𝖇𝖗𝖊 ☠*

- **Problem:** Anime character replacement looking too photorealistic
  - **Solution:** Bypass relight LoRA, remove mask and background connections for full video replacement
  - *From: AR*

- **Problem:** WanAnimate adding lips to masked characters
  - **Solution:** Animate makes lips on every character regardless of ref image - generate multiple seeds until getting closer match
  - *From: Sal TK FX*

- **Problem:** Flash upscaler producing noisy videos
  - **Solution:** Use at least 2x upscaling from original resolution, ideally 4x, works better on low res source
  - *From: Tony(5090)*

- **Problem:** Mocha fails with face tracking jumping to other characters
  - **Solution:** This is inherent to mocha - it has to determine segmentation propagation on its own from first frame mask, causing hallucinations outside mask
  - *From: DawnII*

- **Problem:** Mario appearing in unrelated prompts
  - **Solution:** This is caused by lightx2v LoRA bias towards certain characters like Buzz Lightyear, Baby Yoda, people in business suits - converges to whatever character emerges from noise first
  - *From: garbus*

- **Problem:** HuMo 4 second clip limit
  - **Solution:** Use SVI extension with res_2s sampling to solve extended HuMo generations
  - *From: Ablejones*

- **Problem:** Audio sync issues in visualfrisson workflow
  - **Solution:** Pull back original song and put it in place when audio glitches occur
  - *From: Gateway {Dreaming Computers}*

- **Problem:** Trim to audio enabled causing issues
  - **Solution:** Disable 'trim to audio' in second video combine node
  - *From: 𝕯𝖗. 𝕸𝖆𝖈𝖆𝖇𝖗𝖊 ☠*

- **Problem:** Error when running more than 81 frames
  - **Solution:** Issue mentioned but solution not provided in chat
  - *From: Charlie*

- **Problem:** WanAnimate memory issues
  - **Solution:** Finally got it to run without running out of memory
  - *From: The Coin Hunter*

- **Problem:** Color and light shifts with lightx lora
  - **Solution:** Stopped using the lora due to these issues
  - *From: Cseti*

- **Problem:** Wan Mocha 512x512 VRAM limit
  - **Solution:** 512x512 appears to be limit for 12GB VRAM
  - *From: Blink*

- **Problem:** Wrong SVI LoRA causing transition issues
  - **Solution:** Use SVI shot lora from Kijai's HF repo, not the official SVI repo which is set up for diffusers and not compatible with comfy
  - *From: Ablejones*

- **Problem:** Light LoRA hurts style LoRA effect
  - **Solution:** Use Light LoRA at lower strength (0.3) instead of usual settings, or reduce steps to preserve style LoRA effect
  - *From: KevenG*

- **Problem:** Weird motions in generations
  - **Solution:** Fixed by setting shift to 8
  - *From: hicho*

- **Problem:** Audio running faster than video
  - **Solution:** Use audio delay node to add silence (around .16) before final merge to counter timing issues
  - *From: JohnDopamine*

- **Problem:** PainterLongVideo doesn't actually do special processing
  - **Solution:** It's literally just image-to-video with last frame to first frame continuation, no special motion copying
  - *From: Ablejones*

- **Problem:** VACE inpainting degrades unchanged parts of video
  - **Solution:** Use latent noise masking to protect unchanged parts from degradation during sampling
  - *From: Ablejones*

- **Problem:** ComfyUI built-in mask interpolation fails with fast motion
  - **Solution:** Created custom node to fix trilinear interpolation issues with video latent masks
  - *From: Ablejones*

- **Problem:** Video speed changes between segments in Fun Vace 2.2
  - **Solution:** Use DaVinci Resolve with cross dissolve effect and speed ramping to fix timing issues
  - *From: Ablejones*

- **Problem:** ClownsharKsampler runtime error with mat1 and mat2 shapes
  - **Solution:** Use correct CLIP model for native ComfyUI, not the wrapper CLIP model
  - *From: Ablejones*

- **Problem:** VACE node gray value error
  - **Solution:** Updated TrentNodes repo fixes the gray value coming out of VACE node
  - *From: Flipping Sigmas*

- **Problem:** Bottle distortion and text issues in video
  - **Solution:** Use more steps, higher resolution, include bottle description with text in prompt like 'glass bottle with black letters LA on label'
  - *From: garbus*

- **Problem:** Weird lights artifacts in taxi scene
  - **Solution:** Issue identified but no clear solution provided yet
  - *From: Albert*

- **Problem:** HuMo causing first 4 frames to mess up when using start image
  - **Solution:** Don't use start image with HuMo, only use reference image to avoid first frame artifacts
  - *From: Ablejones*

- **Problem:** Wan generations appearing sped up
  - **Solution:** FPS issue - was set to 24fps but output appeared accelerated
  - *From: hicho*

- **Problem:** Flickering in video generations
  - **Solution:** User's workflow modifications resolved flickering issues
  - *From: Albert*

- **Problem:** Failed HUMO FMML workflow outputs
  - **Solution:** VR provided guidance on fixing noise issues to get workflow running smoothly
  - *From: 152993277631528960*

- **Problem:** Motion not looking fluid
  - **Solution:** Use 24fps instead of 16fps, or match fps to reference video
  - *From: 🦙rishappi*

- **Problem:** VACE only generating content inside laptop screen instead of coming out
  - **Solution:** Use masking with point editor and ensure proper mask setup
  - *From: Albert*

- **Problem:** ClownsharKSampler freezing at 99% VRAM
  - **Solution:** Try replacing with KSampler nodes or run a second time to clear memory
  - *From: Ablejones*

- **Problem:** Fun Vace 2.2 not following prompts as well as expected
  - **Solution:** Switch back to original Vace 2.1 model for better prompt following
  - *From: Ablejones*

- **Problem:** Video too long for VACE generation
  - **Solution:** Set frame_load_cap to maximum of 97 frames for single generation, lower force_rate to 16 for more duration
  - *From: Ablejones*

- **Problem:** VACE mask color issues
  - **Solution:** Change Draw Mask On Image node color to grey (127,127,127) instead of black
  - *From: Ablejones*

- **Problem:** Necklace animation not working in inpainted region
  - **Solution:** Mask must cover all areas where changes occur, including where pieces will fall
  - *From: Ablejones*

- **Problem:** Hard cuts and light flashes in video extensions
  - **Solution:** Reduce LoRA strength to fix hard cuts and light flashes, makes cuts more seamless
  - *From: VRGameDevGirl84(RTX 5090)*

- **Problem:** Character eager to run off screen in HuMo SVI
  - **Solution:** Issue mentioned but no specific solution provided, affects subsequent clips
  - *From: Chandler*

- **Problem:** Can't get background to change in HuMo
  - **Solution:** No matter what prompting is used, background remains stubborn to change
  - *From: Chandler*

- **Problem:** Insane degradation when changing anchor images
  - **Solution:** The prompt needs to be important and describe the new frame, requires tweaking on each run to prevent drifting
  - *From: craftogrammer*

- **Problem:** VAE decode issues with Wan Animate native
  - **Solution:** Still getting dumb VAE decode issues when testing Wan Animate native using Wrapper pre processors + ClownShark samplers
  - *From: Dream Making*

- **Problem:** Background replacement looking fake
  - **Solution:** Need to relight the subject to match new background lighting conditions. Use color matching on reference image and composite original footage back for maximum quality
  - *From: Albert*

- **Problem:** Characters barely opening mouths with SCAIL
  - **Solution:** Use Wan Animate instead - SCAIL is only for body movements, not facial expressions
  - *From: ingi // SYSTMS*


## Model Comparisons

- **1.3B vs 14B model performance**
  - 1.3B is on-par with Hunyuan, 14B not massively better but has very good I2V capabilities
  - *From: YatharthSharma*

- **Wan vs Hunyuan quality**
  - Wan is better than Hunyuan, especially for the models released this week
  - *From: burgstall*

- **1.3B vs 14B generation speed**
  - 1.3B: 1 min 30 seconds, 14B: 8 minutes for same settings on RTX 4070
  - *From: BoricuaPab*

- **Wan vs LTX I2V quality**
  - LTX highly underrated, but Wan 14B seems like SOTA for open source
  - *From: ˗ˏˋ⚡ˎˊ-*

- **1.3B anime style vs 14B**
  - 1.3B model produces better anime style than 14B model
  - *From: DiXiao*

- **Wan vs Kling for complex camera movements**
  - Kling is much better for specific shots like character removing blindfold
  - *From: A.I.Warper*

- **Wan vs Runway vs Kling for gas pedal prompt**
  - Comparison showed different strengths, with Kling having concerning results
  - *From: FutureFlix*

- **Float16 vs BF16 weights**
  - Differences visible in final frames, float16 recently uploaded to comfyorg huggingface
  - *From: Kytra*

- **GGUF Q8 vs other formats**
  - Q8 GGUF provides better quality
  - *From: JmySff*

- **Wan vs Hunyuan visual quality**
  - Hunyuan is blurry but doesn't look horrible up close like Wan's dot-matrix appearance
  - *From: BecauseReasons*

- **Wan vs CogVideoX creativity**
  - Wan is more creative, CogVideoX stays closer to prompt but less inventive
  - *From: ByArlooo*

- **FP8 vs BF16 model performance**
  - FP8 performs just as well as BF16 with half the generation time
  - *From: ShiftingDimensionsAI*

- **Different scheduler comparison**
  - Unipc has the clearest hair, minimal difference between schedulers overall
  - *From: DiXiao*

- **TeaCache step count effects**
  - No particular difference after 50 steps, 100 and 125 same as 150 and 209
  - *From: DiXiao*

- **1.3B vs 14B model quality vs speed**
  - 14B takes ~2x time of 1.3B at same settings but has better motion. 1.3B has better detail rendering at higher step counts
  - *From: burgstall*

- **Wan vs Kling for realistic I2V**
  - Kling still wins for realistic img2vid according to testing
  - *From: Nathan Shipley*

- **H100 vs RTX4090 performance**
  - Apart from more VRAM, not much performance difference observed between H100 and 4090
  - *From: ingi // SYSTMS*

- **UltraSharp vs NMKD-Siax upscaler**
  - UltraSharp good for smooth textures, NMKD-Siax better at preserving texture details
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Wan 2.1 vs Veo2**
  - Wan quality is almost up there with Veo2
  - *From: fredbliss*

- **14B vs 1.3B model**
  - 1.3B is fast but much worse quality, 14B is very slow but higher quality
  - *From: NebSH*

- **3090 vs 3080ti performance**
  - 3090 about 10-25% faster than 3080ti depending on workload
  - *From: Fred*

- **14B vs 1.3B model quality**
  - 14B has much improved texture quality over 1.3B model but is slower
  - *From: Kytra*

- **1.3B performs better with loop functionality**
  - Loop-args works somewhat with 1.3B model but not with others
  - *From: Kijai*

- **14B vs 1.3B WAN model speed**
  - 1.3B is 4x quicker to generate than 14B while maintaining good quality at 1280x720
  - *From: Jas*

- **WAN vs other models for pixel art**
  - WAN and HunyuanVideo do decent pixel animations but don't adhere well to pixel art rules, similar to SDXL limitations
  - *From: TK_999*

- **Wan vs Hunyuan Video for coherence**
  - Wan coherence is insane, way better than hunyuan video
  - *From: Dream Making*

- **res_2m vs UniPC sampler quality**
  - res_2m produces better resolved images with more structure, detail, fewer mutations
  - *From: Clownshark Batwing*

- **res_2m vs res_multistep**
  - Get better results with res_2m over res_multistep due to different implementation with better noise method and initialization
  - *From: Clownshark Batwing*

- **1.3B vs 14B model quality**
  - 14B shows significant quality improvement - 'the quality diff is pretty huge'
  - *From: TimHannan*

- **8 steps vs 20 steps**
  - 8 steps fine for basic quality, change to 20 steps to boost quality
  - *From: AJO*

- **T2V vs I2V with guide image**
  - T2V with guide image works well, I2V has different effect and requires reversing frame weights
  - *From: Ablejones*

- **WAN Fun InP 14B FP8 vs FP16 vs base 14B i2v**
  - No big difference between FP8 or FP16 with WanFun, but base model is better for i2v
  - *From: Vérole*

- **WAN 1.3B vs 14B for vid2vid**
  - Vid2Vid works better overall with 14B
  - *From: 88822364468412416*

- **VACE vs control-fun**
  - You can pretty much skip the control-fun stuff altogether and jump straight to VACE
  - *From: Kytra*

- **GIMM-VFI vs RIFE-Tensorrt**
  - RIFE-Tensorrt is 10x faster than GIMM or normal RIFE
  - *From: burgstall*

- **Wan 14B vs Hyn Video**
  - Comparison shown with same prompt and LoRA trained on same dataset
  - *From: Dream Making*

- **Wan vs paid services like Runway**
  - Wan capabilities make paid services seem unnecessary, Runway is overpriced
  - *From: Level Higher*

- **Wan vs Hailuo**
  - While Wan is amazing for what it can do, it can't create the kind of clips Hailuo can yet, but potential is there
  - *From: TimHannan*

- **1.3B model performance**
  - 1.3B has no right being this good - surprisingly capable
  - *From: 88822364468412416*

- **Wan vs Runway Gen 4 bird movements**
  - Wan makes realistic bird movements while Runway Gen 4 can't handle it - 'We are really ahead of the game'
  - *From: Level Higher*

- **Wan vs Kling vs Hailuo for fight scenes**
  - Wan did the best job recreating Mufasa vs Scar fight scene
  - *From: 𝖑𝖚𝖈𝖎𝖋𝖊𝖗*

- **uni-pc vs res_3m sampler**
  - res_3m gives better quality, uni-pc took 50% longer in test
  - *From: Clownshark Batwing*

- **14B vs 1.3B SkyReels DF for temporal coherence**
  - 14B maintains coherence much better over time, 1.3B degrades faster especially on distant objects
  - *From: Ablejones*

- **Wan vs Skyreels for spatial interactions**
  - Wan handles spatial interactions better, Skyreels ignores them and causes deformation after falls
  - *From: ezMan*

- **Image2Vid vs Text2Vid control**
  - Image2Vid provides more control over scenery in user's experience
  - *From: Level Higher*

- **res_3m vs unipc sampler**
  - res_3m produces significantly better results, particularly for hands and overall quality. UniPC isn't that great, though better than Euler
  - *From: Clownshark Batwing*

- **14B vs 1.3B model degradation**
  - 14B degrades way less than 1.3B for long generations
  - *From: Kijai*

- **SkyReels DF vs WanFun resampling**
  - WanFun 1.3B InP with MPS reward LoRA significantly improves SkyReels DF 1.3B results when used for resampling
  - *From: Ablejones*

- **Kijai's wrapper vs official implementation**
  - Kijai has once again surpassed the official implementation with his wrapper
  - *From: ezMan*

- **LTXV vs Wan for subtle movements**
  - LTXV sometimes does better than Wan on subtle movements but is more temperamental
  - *From: ZombieMatrix*

- **CogVideoX vs Wan resolution**
  - CogVideoX could do higher res much easier than Wan and packed more detail
  - *From: TK_999*

- **Wan T2V vs I2V usefulness**
  - T2V is pretty useless at this stage of development, I2V is better
  - *From: N0NSens*

- **Hunyuan vs Wan scene changes**
  - DiXiao mentioned Hunyuan's scene changes are better than Wan's but didn't provide test results
  - *From: DiXiao*

- **Animated vs realistic content artifacts**
  - Artifacts are less noticeable in animated content compared to realistic content
  - *From: seruva19*

- **Wan vs Hunyuan for high resolution**
  - Hunyuan has hard max around 2500 pixels in either direction, Wan can go much higher with coherent results at 4K and ultrawides
  - *From: ZombieMatrix*

- **Wan significantly better at i2i than t2i**
  - Image-to-image performs better than text-to-image
  - *From: ZombieMatrix*

- **LTX vs Wan for latent guides**
  - LTX latent too compressed spatially, doesn't pick up fine details well. Wan 1.3b much better visual quality with same settings
  - *From: Ablejones*

- **SkyReels vs base Wan2.1**
  - SkyReels worse quality than base, but good for 24fps and LoRA training
  - *From: Ada*

- **CausVid quality vs speed tradeoff**
  - Trade-offs exist but getting low-res gens in under a minute is very good
  - *From: garbus*

- **Wan vs MoviiGen**
  - Quality hit or miss on MoviiGen, Wan generally preferred. MoviiGen more tuned toward modern film vs 70s/80s style
  - *From: TK_999*

- **Wan vs MoviiGen temporal consistency**
  - Wan has much better temporal consistency - Hunyuan/MoviiGen has issues like double fox tails when turning around, much less present on Wan
  - *From: comfy*

- **Wan vs Hunyuan VAE**
  - Hunyuan has stronger VAE but can be harder to converge DiT training with
  - *From: deleted_user_2ca1923442ba*

- **Wan vs AnimatedDiff for pose control**
  - Wan works much better - scenarios that wouldn't work at all with AnimatedDiff work with Wan, even better than DWPose + depth + normal
  - *From: 88822364468412416*

- **14B vs 1.3B Wan quality**
  - 14B is so much better than 1.3B version, significantly higher quality results
  - *From: HeadOfOliver*

- **Phantom custom vs standard models**
  - Phantom 14b custom is the best model seen so far, not quite LoRA quality but pretty close at keeping likeness
  - *From: Thom293*

- **CausVid V1 vs V2**
  - V1 (with block 0 disabled) produces better quality, V2 is darker and less detailed but may work better with adjusted CFG
  - *From: JohnDopamine*

- **Context window 49 vs 81 frames**
  - 49 frames better for abstract styles, 81 frames causes human recognition bleeding
  - *From: Zlikwid*

- **Merged model vs separate LoRAs**
  - Merged model offers convenience and optimized settings but separate LoRAs provide more flexibility
  - *From: VRGameDevGirl84*

- **AccVid I2V LoRA vs T2V LoRA**
  - I2V LoRA much better at retaining resemblance, fixes overblown colors, better prompt adherence and more fluid movement
  - *From: Jonathan*

- **Image-as-video V2V vs traditional I2V workflow**
  - Image-as-video V2V is faster than traditional I2V workflow
  - *From: hicho*

- **Wan vs Veo3 quality**
  - Wan quality very close to Veo3, though Veo3 seems more alive out of the box. Wan wins on style preference
  - *From: ZeusZeus (RTX 4090)*

- **VRGameDevGirl84's merge model vs base model**
  - Merge model shows better consistency and face detail retention, less distortion
  - *From: ZombieMatrix*

- **flowmatch vs uni pc samplers**
  - flowmatch better with details, gets rid of strange artifacts
  - *From: VRGameDevGirl84(RTX 5090)*

- **fp16 vs fp32 VAE**
  - No difference confirmed with Difference Checker node
  - *From: MilesCorban*

- **720p vs 480p models at same speed**
  - 720p always better than 480p at same speed but has small problems at low res
  - *From: patientx*

- **HeyGem vs Fantasy Talking for lip sync**
  - HeyGem can do up to 30mins of lipsync vs Fantasy Talking's 5ish seconds, uses 14gb VRAM, takes 10mins for 15min video. Fantasy Talking has better audio syncing but shorter duration
  - *From: ArtOfficial, Guey.KhalaMari*

- **VACE vs ATI**
  - vace >= ati, VACE is good alternative for ATI
  - *From: Jonathan*

- **Phantom vs VACE quality**
  - Phantom results are far better than VACE, more defined with better skin rendering, almost professional quality
  - *From: GOD_IS_A_LIE*

- **Self-Forcing vs standard models**
  - Matches quality of slower models (e.g., Wan2.1) but much faster
  - *From: SS*

- **FusionX vs FusionX + Self Forcing LoRA vs Wan21 base + Self Forcing LoRA**
  - FusionX + lora seems to be the best
  - *From: patientx*

- **LightXv2 vs CausVid**
  - LightXv2 is a level up, feels very solid. Can do cause but at maybe a .1
  - *From: Gateway {Dreaming Computers}*

- **LightX vs CausVid for blotches**
  - LightX at 6 steps and blotches seem completely gone
  - *From: Thom293*

- **Topaz models for upscaling**
  - Rhea 4x works for most things, Starlight makes video look WAY MORE AI-generated if detail is already good
  - *From: ingi // SYSTMS*

- **WAN T2V vs commercial models (Kling and VEO)**
  - WAN T2V quality is far better than every commercial model seen
  - *From: Dream Making*

- **40% vs 100% ControlNet strength**
  - 40% ControlNet looks much better than 100% strength
  - *From: Thom293*

- **Diffusion vs Non-Diffusion upscaling methods**
  - Diffusion looks better but slightly less true to original content. Non-diffusion stays very close to original
  - *From: The Shadow (NYC)*

- **WAN vs other models**
  - WAN (Nag) clearly a winner over other unnamed model in side-by-side test
  - *From: uff*

- **1440x768 vs 1080p resolution**
  - 1440x768 looks decent, while 1080p loses consistency
  - *From: ingi // SYSTMS*

- **1280x1280 vs other resolutions**
  - 1280x1280 looks good for Wan generation
  - *From: ingi // SYSTMS*

- **FusionX model vs general wan model with FusionX LoRA**
  - Better results using FusionX model without LoRA than combining general model with FusionX LoRA
  - *From: AiGangster*

- **Different step counts (2,4,6,8,10 steps)**
  - 8 steps more natural and better than 4 steps
  - *From: AiGangster*

- **SkyReels models vs base Wan for training**
  - SkyReels worked better for human likenesses, full fine-tuned by professionals with 24fps content
  - *From: JohnDopamine*

- **LightX vs Causvid**
  - LightX is a better version of causvid, don't use them both together
  - *From: VRGameDevGirl84(RTX 5090)*

- **Wan models vs Veo 3**
  - It's safe to say that Veo 3 just bit the dust
  - *From: T2 (RTX6000Pro)*

- **HSD lora vs accvid and HPS**
  - HSD greatly improves lightx2v motion without degrading colors/detail like accvid and HPS does
  - *From: Jonathan*

- **VACE with vs without reference image**
  - When control input frames are present, they completely take over influence from reference image
  - *From: Ablejones*

- **720 vs 1280 resolution**
  - Big difference in performance and composition, higher resolution much better
  - *From: T2 (RTX6000Pro)*

- **VACE 1.3B vs 14B**
  - 14B is much easier to deal with and can edit backgrounds while 1.3B cannot
  - *From: Cseti*

- **FusionX LoRA vs LightXv2 LoRA stack**
  - LightXv2 at 50% weight with AccVid LoRA at 50% performs better for fast motion, especially with MPS LoRA disabled
  - *From: Todd*

- **4 steps vs 8 steps for text to image**
  - 8 steps is obviously better than 4 steps, but 4 is still enough
  - *From: patientx*

- **WAN vs Flux image quality**
  - WAN faces look much better than Flux, even without face LoRAs. Much better quality than what can be achieved with Flux at same step counts
  - *From: 455300561034543105*

- **WAN vs AnimateDiff for 3D animation processing**
  - WAN produces much better results for 3D animation restyle compared to AnimateDiff which had bad results
  - *From: hicho*

- **Custom vs ComfyUI-generated control passes**
  - Custom Canny and depth from 3D software work more consistently and cleanly than ComfyUI generated versions
  - *From: Andy Kush*

- **Vanilla WAN T2V vs Skyreels model**
  - Skyreels gets finer details better but makes image look unnatural, vanilla WAN looks more like real picture
  - *From: l҈u҈c҈i҈f҈e҈r҈*

- **FusionX vs AniWAN**
  - Comparison shown but no specific verdict given in text
  - *From: patientx*

- **WAN vs Flux for image generation**
  - User won't go back to Flux after WAN results
  - *From: patientx*

- **CausVid vs LightX2V LoRA**
  - CausVid seems to give better results
  - *From: AR*

- **LightX2V vs CausVid**
  - LightX2V is better - designed for realism & lighting dynamics
  - *From: The Shadow (NYC)*

- **Wan NAG vs CFG for negative prompts**
  - Rather use CFG if you want neg prompts. NAG is like creating a virus yourself and finding a cure for it
  - *From: l҈u҈c҈i҈f҈e҈r҈*

- **Pusa vs AccVid+MPS with LightX2V**
  - Pusa is more natural with little weight shifts, better movement quality
  - *From: Blitz*

- **Chinese vs English prompting**
  - Chinese prompting produces better results for complex actions
  - *From: l҈u҈c҈i҈f҈e҈r҈*

- **WanWrapper vs Native ComfyUI**
  - Wrapper more consistent, native has variable speed and OOM issues
  - *From: patientx*

- **Wan vs HiD for style transfer**
  - Wan needs only single clip while HiD requires stack of clips but gives trash results
  - *From: l҈u҈c҈i҈f҈e҈r҈*

- **Wan vs Pusa physics handling**
  - Wan is way better at handling physics compared to Pusa
  - *From: Dream Making*

- **Wan 2.2 vs 2.1 for zombies**
  - 2.2 does zombies slightly better, bigger dataset helped somewhat
  - *From: TK_999*

- **Wan 2.1 vs 2.2 slime generation**
  - 2.2 significantly better at generating green slime covering city scenes
  - *From: TK_999*

- **LightX destroys quality vs without**
  - LightX generally reduces quality but wasn't catastrophic with 2.1
  - *From: TK_999*

- **Wan 2.2 vs 2.1**
  - 2.2 is 100x better, all motion issues fixed
  - *From: 138234075931475968*

- **Wan 2.2 I2V vs KLING**
  - Likeness holds up on a level close to KLING
  - *From: DaxRedding*

- **5B vs LTXV**
  - Same generation time as LTXV with better results and camera motions
  - *From: 823564252748709918*

- **Wan 2.2 vs Kling 2.1**
  - Wan 2.2 understands camera movement prompts better than Kling 2.1
  - *From: 312993351307755520*

- **2.2 vs early SDXL**
  - Garbled faces remind of early SDXL days, similar potential to reach SDXL-like final form
  - *From: Atlas*

- **Wan2.2 vs Kling**
  - Kling didn't even try with prompts that Wan2.2 handled well
  - *From: Atlas*

- **Video LoRAs trained from 2.1 vs 2.2**
  - 2.1-trained LoRAs don't work as well on 2.2
  - *From: Atlas*

- **Wan transitions vs Runway morphing**
  - Wan transitions are much better and more interesting to watch than Runway
  - *From: Charlie*

- **Open source Wan + Comfy vs proprietary platforms**
  - Don't know a single proprietary platform that has anything on Wan + Comfy for control
  - *From: ingi // SYSTMS*

- **5B vs 14B model quality**
  - Good quality achieved with 5B model, making it a relief for those finding 14B overwhelming
  - *From: hicho*

- **KJ default shift of 8 vs other values**
  - KJ default of 8 was best
  - *From: CaptHook*

- **Wan 2.2 vs Sora availability**
  - We got Sora at home before official sora for pay
  - *From: VK (5080 128gb)*

- **50 steps full model vs 8 steps with lightning LoRA**
  - Full Wan 2.2 model preferred over speedup LoRAs, despite longer generation time
  - *From: Zuko*

- **bf16 vs fp32 model performance**
  - fp32 makes a big difference in quality, rabbit was supposed to jump on shoulder
  - *From: Benjimon*

- **With vs without LightX2V**
  - Without LightX2V gives more crispy results
  - *From: NebSH*

- **New vs old Lightning LoRAs**
  - New ones are better quality but kill motion, old ones could handle more complex scenes
  - *From: patientx*

- **Wan 2.1 vs 2.2 for same prompts**
  - 2.2 sometimes better but not everything works as well, some prompts work better on 2.1
  - *From: patientx*

- **Lightning v1.0 vs v1.1**
  - v1.1 has less checkerboard pattern artifacts
  - *From: patientx*

- **Website vs local Wan results**
  - Website seems to have superior version, local can't replicate same quality
  - *From: xwsswww*

- **Flux vs Wan for same prompt**
  - Flux has cinematic vibe but Wan is much more 'solid' with better details like reflections in glasses
  - *From: N0NSens*

- **Wan 2.2 new 5B vs old 5B**
  - New updated model does significantly better than the older 5B version
  - *From: l҈u҈c҈i҈f҈e҈r҈*

- **15 steps vs 12 steps**
  - 15 steps looks better than 12 steps
  - *From: R.*

- **Fun Control vs regular Wan quality**
  - Fun Control follows movement really well and is flexible, can use at 0.25 strength and still follow general movement, but quality is much weaker than regular Wan
  - *From: Hashu*

- **Wan 14B vs 5B model**
  - 14B is very forgiving, 5B requires more details in description and unnecessary details work against you
  - *From: Mngbg*

- **Image-to-Video vs VACE extended**
  - I2V has better image consistency, VACE has smoother motion - seeking way to combine both benefits
  - *From: 535638716413116416*

- **MultiTalk I2V vs V2V**
  - MultiTalk is for I2V, V2V is not good for MultiTalk
  - *From: shockgun*

- **fp16 vs GGUF models**
  - fp16 significantly better quality, GGUF needs more steps and produces worse results
  - *From: l҈u҈c҈i҈f҈e҈r҈*

- **Lightning vs LightX2V LoRAs**
  - Both work well, with user showing same prompt results from both
  - *From: 138234075931475968*

- **Wan22-I2V-FastMix_v10 vs vanilla fp16**
  - Comparison shown visually but no specific verdict given
  - *From: l҈u҈c҈i҈f҈e҈r҈*

- **Context frames 81 vs 121**
  - 121 frames gives better, smoother results than 81 frames
  - *From: xwsswww*

- **InfiniteTalk vs Multitalk**
  - InfiniteTalk seems better, works without driving video
  - *From: Juan Gea*

- **Wan 2.2 vs 2.1 Control**
  - 2.2 is definitely much more detailed
  - *From: Dream Making*

- **GGUF 4S performance**
  - Works for close-up faces but worse for far view faces
  - *From: AiGangster*

- **Wan 2.2 5B vs other variants**
  - Very fast but has slip/morphing issues, manageable VAE at fp16, usable for 8GB GPUs with fp8
  - *From: patientx*

- **Different samplers on Wan 2.2**
  - euler/beta seems really bad, for 10 steps bong_tangent is way too aggressive
  - *From: Dream Making*

- **Chatterbox vs other TTS**
  - Much better at giving speech the right energy but doesn't support French
  - *From: 𝕯𝖗. 𝕸𝖆𝖈𝖆𝖇𝖗𝖊 ☠*

- **Wan 2.1 vs 2.2 T2V on same prompt**
  - 2.1 nailed it better for woman painting face with blue paint prompt
  - *From: hicho*

- **InfiniteTalk vs MultiTalk lipsync quality**
  - MagRef seems to hit lipsync better, but 480 base model stays more true to original image
  - *From: Bleedy (Madham)*

- **KJ wrapper vs native S2V**
  - KJ wrapper is smoother and faster, native has lag issues like wan demo
  - *From: hicho*

- **Left vs right with/without Pusa lora**
  - Visual comparison shown but no specific verdict given
  - *From: l҈u҈c҈i҈f҈e҈r҈*

- **Wan 2.2 T2V vs SeedVR2**
  - Wan with low denoise is better - SeedVR2 is sharper but has more artifacts and temporal consistency issues
  - *From: Juan Gea*

- **InfiniteTalk vs MultiTalk**
  - InfiniteTalk feels better than MultiTalk and better than new Wan S2V
  - *From: 441459285759754250*

- **Ultimate SD Upscaler vs Topaz/SeedVR2**
  - Ultimate SD Upscaler with Wan destroys Topaz and other upscalers
  - *From: 153803064858378240*

- **Wan 2.2 vs 2.1 remake comparison**
  - 2.2 shows significant improvement over 2.1 in same scenes
  - *From: ingi // SYSTMS*

- **GGUF vs FP8 models**
  - GGUF is faster, Q8 same size as FP8 but may be better quality
  - *From: patientx*

- **MagicWan vs regular Wan models**
  - Some users don't see much difference with regular model
  - *From: N0NSens*

- **Wan 2.2 22 vs 21 comparison**
  - 22 shows better performance in tested scenarios
  - *From: hicho*

- **InfiniteTalk vs S2V**
  - InfiniteTalk produces much better results than S2V for lip-sync applications
  - *From: U̷r̷a̷b̷e̷w̷e̷*

- **PUSA strength comparison**
  - Light2x alone vs Light2x + PUSA at 1.5 strength - PUSA adds noticeable enhancement
  - *From: Abx*

- **Wan vs other T2I models**
  - Wan is more realistic but Qwen trained on more diverse dataset, so Qwen better for obscure prompts
  - *From: Hevi*

- **Qwen Edit quality**
  - Qwen Edit produces blurry/low res results for realism by default, but mind blowing for stylized outputs
  - *From: AshmoTV*

- **Different VACE model variants**
  - Testing showed differences between VACE 2.1, Fun VACE high/low, FakeVace merges in explosion generation workflow
  - *From: JohnDopamine*

- **WAN 2.1 VACE vs WAN 2.2 VACE for artistic styles**
  - WAN 2.1 VACE maintains artistic styles much better than 2.2, which tends to convert to photorealistic output
  - *From: 151330553629638656*

- **VACE 2.2 vs other models for video extension**
  - VACE 2.2 has no degradation with context windows unlike other models that suffer quality loss
  - *From: Vérole*

- **AnimateDiff vs WAN for art styles**
  - AnimateDiff is better for maintaining artistic styles and non-realistic outputs
  - *From: AshmoTV*

- **Depth vs Pose controls in VACE**
  - Pose control maintains character consistency better, depth affects overall scene structure differently
  - *From: Zuko*

- **HuMo vs InfiniteTalk for dialogue**
  - InfiniteTalk is better for dialogue, HuMo is more suited to music videos
  - *From: mdkb*

- **Wan 2.5 audio vs VEO3**
  - Wan 2.5 allows i2v with audio while VEO3 doesn't
  - *From: VK (5080 128gb)*

- **Wan 2.5 audio vs mmaudio/hunyuanfoley**
  - Wan 2.5 audio is tinny and compressed, similar quality to mmaudio/hunyuanfoley
  - *From: DawnII*

- **4 steps vs 3 steps quality**
  - 4 steps increases quality significantly compared to 3, but is really slow
  - *From: 153803064858378240*

- **Wan vs Kling**
  - Some Wan tests worked better than Kling ones
  - *From: hicho*

- **Humo lipsync quality**
  - Definitely the best lipsync worked with so far, very good character resemblance
  - *From: Ablejones*

- **Dyno vs 3-Sampler setup**
  - 3-Sampler setup produces better motion than Dyno for parkour scenes
  - *From: garbus*

- **Dyno vs standard models**
  - Dyno has no benefit over usual models and doesn't cooperate well with phantom merge
  - *From: 88822364468412416*

- **Full Dyno model vs LoRA version**
  - Full model gives better results than LoRA for motion, T2V only
  - *From: 153803064858378240*

- **Neo Banana vs Qwen Edit Plus**
  - Neo Banana is like a Koenigsegg Agera vs Qwen Edit Plus being a Corvette - much more powerful but requires cloud compute
  - *From: U̷r̷a̷b̷e̷w̷e̷*

- **Wan 2.1 vs Wan 2.2 i2v**
  - 2.2 is more realistic, 2.1 has better camera focus effects. 2.1 gave better camera focus in gun closeup test
  - *From: hicho*

- **Old lightxV2 LoRAs vs new dyno LoRAs**
  - New dyno ones might influence style more, old lightxV2 recommended for some use cases
  - *From: garbus*

- **1280x720 vs 1024x576 resolution**
  - Question about quality improvement at higher resolution
  - *From: A.I.Warper*

- **Hunyuan styler vs other stylers**
  - Hunyuan styler is even better than other options
  - *From: hicho*

- **ChatGPT vs Florence for prompting**
  - User prefers Florence with string functions for editing text, while another uses ChatGPT node for Wan-style prompts
  - *From: hicho*

- **OVI vs standard models for non-human faces**
  - OVI generally darker lighting, works well for creatures but dog is most unconvincing
  - *From: Thom293*

- **Old VACE vs new capabilities**
  - Old VACE does well on background movement
  - *From: chrisd0073*

- **Resolution impact on model performance**
  - Changing resolution can make difference to end result due to training at certain resolution
  - *From: The Coin Hunter*

- **HuMo vs other models for face consistency**
  - HuMo is best one-shot subject-to-video model, maintains resemblance very well even at high denoise
  - *From: Ablejones*

- **Wan Animate vs MoChA**
  - Wan Animate gives more artistic freedom and better results with LoRAs, while MoChA adapts more accurately to original video movements/lights/shadows but can be limiting
  - *From: yukass*

- **Wan 2.5 vs Wan 2.2**
  - Prefers 2.2 in ComfyUI with different variants and controls over 2.5
  - *From: Juan Gea*

- **MoE lora vs new 1030 lora**
  - 1030 has better camera control, following prompts almost exactly
  - *From: U̷r̷a̷b̷e̷w̷e̷*

- **rCM vs Lightx on base WAN2.2**
  - Both have style issues, base WAN2.2 is partially to blame for character bias
  - *From: garbus*

- **AnimateDiff 1 year ago vs current Wan capabilities**
  - AI is developing fast - can now achieve much better results than AnimateDiff from a year ago
  - *From: Charlie*

- **Qwen edit vs Wan I2V for editing**
  - Wan I2V faster for 2060 users since Qwen edit runs slow on GPU
  - *From: hicho*

- **Wan 2.2 smoothmix vs base + lora**
  - Smoothmix produces higher quality output, only finetune that could do certain car generations
  - *From: hicho*

- **Old lightx2v lora vs newer versions**
  - Old lightx2v lora has less motion but doesn't experience the same problems
  - *From: Cseti*

- **Light LoRA high vs low strength for style preservation**
  - Lower Light LoRA strength (0.3) with 16 steps preserves pen strokes better than usual settings with 6 steps
  - *From: KevenG*

- **Image-trained vs video-trained LoRAs**
  - Video-trained LoRAs precisely capture hand-drawn feel better than image-trained ones for animation
  - *From: AshmoTV*

- **Krea vs Wan 2.2**
  - krea>>wan2.2 according to user assessment
  - *From: 283534753251065856*

- **FFLF vs VACE for animation**
  - FFLF has better animation, but VACE is better when you need something very specific and accurate
  - *From: ingi // SYSTMS*

- **Wan 2.2 I2V vs other models for VACE stitching**
  - Much higher success rate using Wan 2.2 I2V 16fps videos with VACE than using Kling/Midjourney 1080P 24fps videos
  - *From: NodeMancer*

- **WAN 2.2 smoothmix vs base model**
  - Smoothmix is better - smoother, less noisy on same steps, works well for I2V
  - *From: hicho*

- **GGUF Q4 vs FP8**
  - GGUF Q4 produces great gens and uses around 50% RAM vs higher usage with FP8
  - *From: Tony(5090)*

- **Distilled with more steps vs without**
  - Distilled with more steps looks better
  - *From: 88822364468412416*

- **Wan 2.6 vs Wan 2.1 same prompt**
  - Wan 2.6 shows huge leap in quality, much better prompt adherence
  - *From: hicho*

- **Wan 2.6 vs Wan 2.2 T2V**
  - Wan 2.6 has better prompt adherence but weird aesthetic - 30fps yet looks jittery, everything looks slow motion and too smooth/unrealistic
  - *From: dj47*

- **Wan 2.6 vs Sora 2 for realism**
  - For realism, Sora 2 still beats them all
  - *From: hicho*

- **Z image vs Wan for text preservation**
  - Z image does better for text preservation than Wan, so using Z image + Wan i2v is better than Wan t2v
  - *From: Albert*

- **Wan base 2.2 vs Wan 2.2 smoothmix**
  - Smoothmix has specific motion preferences and uses old distil loras
  - *From: hicho*

- **Right vs left generation with FastWan LoRA**
  - Right one (with FastWan LoRA) has slightly more detail in face and is sharper overall, handles upscaling better
  - *From: VRGameDevGirl84(RTX 5090)*

- **Smoothmix H + Wan 2.2 base low vs Wan 2.2 base in both**
  - Smoothmix H + 2.2 base low is better for graphics and motion
  - *From: hicho*

- **Dasiwa vs Smoothmix**
  - Dasiwa is much better than smoothmix
  - *From: asd*

- **Fun Vace 2.2 vs original Vace 2.1**
  - Original Vace 2.1 better for prompt following in inpainting
  - *From: Ablejones*

- **HuMo vs InfiniteTalk**
  - Prefers HuMo for reference matching capabilities combined with Wan A14B's prompt matching ability, not extremely familiar with InfiniteTalk
  - *From: Ablejones*

- **Wan vs Kling for line art**
  - Kling's motion control gets line art better/faster than WAN, took ~50 runs to get 1 correct result with WAN
  - *From: AR*

- **SVI Pro 2.2 vs LTX2**
  - SVI Pro 2.2 > LTX2 AI Slop, though 16fps and low dynamic motion make Wan pretty obsolete for certain uses
  - *From: Janosch Simon, dj47*

- **LTX 4 steps vs LTX + Wan 2 steps**
  - LTX + Wan 2 steps using same prompt produces crazy detail improvement
  - *From: hicho*

- **FILM vs GMFSS interpolation**
  - GMFSS handles large motions much better than FILM for fast movement
  - *From: brbbbq*

- **Native InfiniteTalk vs InfiniteTalk + SVI Talk LoRA**
  - SVI Talk LoRA version shows better prompt adherence and motion
  - *From: 254379502879113216*

- **SCAIL vs Wan Animate for facial animation**
  - Wan Animate is better for mouth movements, SCAIL is only for body movements
  - *From: ingi // SYSTMS*


## Tips & Best Practices

- **Use Mandarin prompts for better results**
  - Context: All prompting, especially complex scene descriptions
  - *From: Juampab12*

- **Use proper aspect ratios for each model**
  - Context: 720p model: 1280x720/720x720/720x1280, 480p model: 832x480/480x832/480x480
  - *From: AJO*

- **Increase steps to 50+ for 1.3B model**
  - Context: Higher step counts significantly improve quality and reduce artifacts
  - *From: DiXiao*

- **Lower shift value to 4 for better quality**
  - Context: Using shift=4 with higher steps improves output quality
  - *From: DiXiao*

- **Use 1.3B model for faster experimentation**
  - Context: Much faster generation makes it ideal for testing prompts and settings before using 14B
  - *From: TK_999*

- **Low flowshift (like 2) and higher steps (20) dramatically improve I2V**
  - Context: For better I2V results
  - *From: Faust-SiN*

- **Use 16:9 aspect ratios for best results**
  - Context: Based on likely dataset composition
  - *From: A.I.Warper*

- **Longer captions in Chinese provide good adherence**
  - Context: For better prompt following
  - *From: DawnII*

- **Use cfg_end parameter to save time on renders**
  - Context: With GGUF, but be careful not to set too low
  - *From: JmySff*

- **Quality realistic input images are key**
  - Context: Model doesn't invent small details well, needs good source material
  - *From: ShiftingDimensionsAI*

- **Use Florence for FlowEdit prompts**
  - Context: Use 'more detailed caption' mode to create base prompt, then edit specific parts for target
  - *From: ˗ˏˋ⚡ˎˊ-*

- **FlowEdit parameter baseline**
  - Context: 5 skip steps, 15 drift steps, 30 total steps, 1-2 CFG source, 6-10 CFG target
  - *From: Zuko*

- **Better aspect ratio for cinematic look**
  - Context: Ultrawide aspect ratio appears more cinematic than standard ratios
  - *From: burgstall*

- **Use mandarin chinese prompts**
  - Context: Running prompts through translation to mandarin chinese may improve results
  - *From: burgstall*

- **CPU offload for VRAM management**
  - Context: Offload clip to CPU to free up space for GPU inference when using GGUF models
  - *From: 215983606227664896*

- **Use 832x480 resolution for best results with 480p model**
  - Context: Native resolution works best, higher resolutions may reduce quality
  - *From: burgstall*

- **50+ steps on 1.3B can beat quality of optimized 14B workflows**
  - Context: When prioritizing quality over speed
  - *From: spacepxl*

- **For FlowEdit, source and target images still need to somewhat line up**
  - Context: Mirrored images don't work well for transformations
  - *From: mono*

- **TEACache 0.25 or lower recommended for quality**
  - Context: Values above 0.4 cause noticeable quality loss
  - *From: c1t1zen1*

- **Can replicate closed-source effects by training LoRAs**
  - Context: Pay for 20 videos or use free videos from social media to create LoRAs of effects like Pika Labs
  - *From: Juampab12*

- **Use Chinese prompts for better results**
  - Context: Translating prompts to Chinese can improve generation quality
  - *From: GalaxyTimeMachine (RTX4090)*

- **Need to play seed lottery with effect LoRAs**
  - Context: Effect LoRAs like cakify require trying multiple seeds for best results
  - *From: Zuko*

- **Use example prompts from LoRA galleries**
  - Context: Copy prompts from gallery videos, don't just use keywords from description
  - *From: Juampab12*

- **Measure average generation times**
  - Context: Generation times can vary between runs due to memory organization, so measure averages
  - *From: Fred*

- **Really explore for the right seed, cut losses and reroll if preview looks wrong**
  - Context: When doing I2V animation
  - *From: Cubey*

- **Use masterpiece, best quality, curvy, smooth motion, slowly, anime style as base prompt**
  - Context: For I2V generation
  - *From: 133784166977372160*

- **For steamboat willie lora use format: steamboat willie style, golden era animation, <prompt>**
  - Context: Using Benjaminimal's steamboat willie lora
  - *From: Benjaminimal*

- **81 frame loops need larger context - use 169 frames with 81 context window**
  - Context: Creating loops with context options
  - *From: Kijai*

- **Use Blender with Mixamo models for consistent camera movement training**
  - Context: For training camera motion loras - create generalized 3D models and stage consistent camera movements while changing models for variety
  - *From: Kytra*

- **Caption training data with consistent paradigms**
  - Context: For traveling lora: 'kxsr, [describe person/thing and interior], outside the [describe movement/happenings outside]'
  - *From: Kytra*

- **Remove problematic frames from training data**
  - Context: Remove video clips with lightning bolts or solid white frames that could interfere with training
  - *From: Kytra*

- **Use identical motion across all training videos for camera movement loras**
  - Context: Consistent motion is crucial - slight variations make camera movement training difficult
  - *From: Kytra*

- **Use Google Colab with ngrok tunnel for free cloud compute**
  - Context: Launch ComfyUI on free Google Colab and create ngrok tunnel to access remotely
  - *From: Kytra*

- **Resize video clips to target resolution before training**
  - Context: All video clips should be resized to training resolution (like 1280x720) regardless of source resolution
  - *From: Kytra*

- **Use loops instead of last frame chaining**
  - Context: If you can't guarantee the subject's face is in the last frame each time, you get nonsense output - better to have complete control over faces
  - *From: AJO*

- **Input first frame without change to help consistency**
  - Context: When doing video inpainting workflows
  - *From: IllumiReptilien*

- **Control LoRA skews hard to realism**
  - Context: You'll have to use LoRAs to push it around if you want anything other than realism
  - *From: Fill*

- **Use higher resolutions for end frame implementation**
  - Context: works very nicely with end frame implementation but only at higher resolutions
  - *From: pom*

- **Try multiple start frames instead of single frame**
  - Context: When using Fun InP model for better motion continuity
  - *From: spacepxl*

- **Add slight lineart instead of just depth**
  - Context: If you don't want additional animations when using Fun Control model
  - *From: JmySff*

- **Use VFI x2 or x3 then select every nth frame**
  - Context: For improving frame rates and smoothness
  - *From: AJO*

- **Slow down input for fast paced movements**
  - Context: The limitation is low fps to track fast paced movements, counteract by slowing input
  - *From: DawnII*

- **Use higher step counts for better quality**
  - Context: WAN was trained originally expecting at least 50 steps. Aim for 50-60 steps minimum, can go up to 75 for very dynamic scenes
  - *From: Kytra*

- **Add 'dynamic motion' to prompts for more movement**
  - Context: For scenes requiring more motion
  - *From: Level Higher*

- **Use CFG closer to 4/4.5 for better results**
  - Context: When getting garbled output, lower CFG can help
  - *From: ingi // SYSTMS*

- **Connect first and last frames with padding for better I2V**
  - Context: Current I2V encodes frames separately then joins them, better approach would be to join with padding then VAE encode like inpaint model
  - *From: spacepxl*

- **Train LoRAs at 1536 on longest edge for high-res inference**
  - Context: Allows inference at super high resolution in different styles
  - *From: Kytra*

- **Match bbox color to wanted background**
  - Context: For better subject replacement, keep bbox gray but tint it darker or lighter to match background
  - *From: ArtOfficial*

- **Use full frame portrait reference for face swapping**
  - Context: Better to show only the face rather than unpainted first frame for VACE faceswapping
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Adjust mask growth based on subject type**
  - Context: For cars, don't need to grow mask as much, but for people and animals need to grow it more
  - *From: ArtOfficial*

- **End frame becomes useless when using ControlNet**
  - Context: When using start frame with ControlNet in VACE, can disconnect the end frame
  - *From: Vérole*

- **Use padding for reference images**
  - Context: Padding image is useful for reference in VACE workflows
  - *From: Vérole*

- **Use VLM for better prompting and follow the Wan prompt guide**
  - Context: For getting high quality anime-style generations
  - *From: 133784166977372160*

- **Add 'talking, speaking' in negatives to stop yapping animations**
  - Context: When you don't want characters to have mouth movements
  - *From: 133784166977372160*

- **Upscale image before feeding to MoGe and include reference image**
  - Context: For better VACE inpaint results with 3D scene models
  - *From: DevouredBeef*

- **Use Florence2 to describe images for I2V prompting**
  - Context: Running folders of images overnight for automated video generation
  - *From: jeru*

- **Use 20 FPS base render for smoother motion**
  - Context: Gives more frames for complex movements and expressions, better for Topaz interpolation to 60FPS
  - *From: Level Higher*

- **90% input, 10% prompting for character control**
  - Context: When doing character animations like winking, rely heavily on image inputs rather than prompts
  - *From: andrewrasmussen.*

- **Use reverse generation for difficult actions**
  - Context: Easier to generate putting object down than picking up, then reverse in post
  - *From: 164879244210470913*

- **Specify detailed fall descriptions in prompts**
  - Context: Instead of just 'falls to ground', describe 'falls gradually on legs then with torso'
  - *From: Level Higher*

- **Use 75 steps and long descriptive prompting without LoRAs**
  - Context: For better results with dynamic motion, works well with CFG 6.5
  - *From: Level Higher*

- **Use external cooling for GPU temperature management**
  - Context: USB fan placed below GPU from outside can drop temperature by 12°C
  - *From: Level Higher*

- **Higher order samplers help with details**
  - Context: When having issues with hands or details, try res_4s_friedli, res_5s, res_8s for better results
  - *From: Clownshark Batwing*

- **Use variety of caption styles for LoRA training**
  - Context: Include captions with only trigger word when image/video is just the effect on its own
  - *From: ingi // SYSTMS*

- **Use different prompts for each sampler**
  - Context: When using DF workflow for better results
  - *From: Cseti*

- **Don't use intense negative prompts**
  - Context: Better results without default negative prompt terms, just use simple terms like 'bad quality, blurry'
  - *From: JohnDopamine*

- **Use SLG blocks 8-9 with percent ranges start .2-.4, end .6-.8**
  - Context: For most cases, other values were worse
  - *From: ezMan*

- **Use hybrid approach for video generation**
  - Context: Technically I2V but using Wan as image generator first
  - *From: ZombieMatrix*

- **Start with Flux then alternate with Wan for upscaling**
  - Context: Flux -> Wan -> Flux -> Wan -> Flux process helps with composition and details
  - *From: ZombieMatrix*

- **Use GPT-4o while high for creative prompt generation**
  - Context: For generating unique and creative video prompts
  - *From: 🏁🫰GridSnap*

- **Avoid fast montage cuts or rapid motion**
  - Context: These are the biggest threats to context preservation in Wan generations
  - *From: seruva19*

- **Use PDF methodology for consistent prompting**
  - Context: Create PDF guide, feed to LLM with image and animation idea for consistent results
  - *From: Level Higher*

- **Add some frame overlap with self-attention**
  - Context: Usually good to have a few frames overlap to get less sudden transitions in regional workflows
  - *From: Clownshark Batwing*

- **Wide images render faster than tall images**
  - Context: Diffusion models hate height aspect, always better time-wise to create wide vs tall images
  - *From: ZombieMatrix*

- **Use exponential increase of CFG level over total generation process for upscaling**
  - Context: Helps bring out fine details in upscale process
  - *From: ZombieMatrix*

- **Wan is significantly better at i2i than t2i**
  - Context: When choosing between text-to-image and image-to-image workflows
  - *From: ZombieMatrix*

- **Use --reserve-vram 12.0 launch arg for high resolution on 3090**
  - Context: For 1360x768 generation to avoid OOM/system memory fallback
  - *From: TK_999*

- **Higher steps (75) can reduce distortions and artifacts**
  - Context: Despite longer generation times, provides cleaner movement and less blurry outcomes
  - *From: Level Higher*

- **Use context option for long consistent videos**
  - Context: Essential for generating 14+ second videos with consistency
  - *From: 852話 (hakoniwa)*

- **Describe what you want the reference to carry forward in prompt**
  - Context: VACE understands if you don't describe scenery, it takes from reference, but you can override with specific prompts
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Match generation frames to driving video length**
  - Context: Prevents reference frames appearing in final output
  - *From: ArtOfficial*

- **Disconnect context node for testing**
  - Context: Run small number of frames first to verify workflow works, then bump total and connect context
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Use ChatGPT for prompt engineering**
  - Context: Feed it articles on Wan 2.1 prompt engineering and use for generating prompts
  - *From: Dkamacho*

- **Avoid depth control with different character proportions**
  - Context: Pose detection doesn't work well with stylized characters of different proportions
  - *From: Guey.KhalaMari*

- **For looping videos, use Kijai's start and end frame helper**
  - Context: Take end n frames as start frames and start n frames as end frames
  - *From: 88822364468412416*

- **Use white boxes with black outlines for 3D control**
  - Context: Remove shading from 3D shapes so it's just white with black outlines to avoid too much shape information
  - *From: ingi // SYSTMS*

- **Split complex generations into separate passes**
  - Context: For complex scenes, generate table, character, and background separately then composite in After Effects
  - *From: enigmatic_e*

- **Use Florence to describe characters for consistent prompting**
  - Context: When testing different styles with VACE, use Florence to describe each character for the prompt
  - *From: ingi // SYSTMS*

- **Use multiple reference images for better character consistency**
  - Context: When generating multiple scenes with same character
  - *From: AJO*

- **Try euler/beta or unipc samplers instead of LCM/beta**
  - Context: To avoid rubbery/doll-like people appearance
  - *From: ZeusZeus*

- **Split sampling with different CFG values**
  - Context: Use CFG 3-5 for step 1, CFG 1 for remaining steps with CausVid
  - *From: phazei*

- **Use 2-step generation for quick testing**
  - Context: Great for testing prompts and movement before doing full generation
  - *From: Jonathan*

- **Use shift=1 for realistic content, shift=3+ for stylized content**
  - Context: Adjust based on desired output style and resolution
  - *From: VRGameDevGirl84(RTX 5090)*

- **Optimal LoRA combination: causvid 0.5, accvid i2v 2.0, mps 1.0**
  - Context: Best mix for low step generation
  - *From: Jonathan*

- **When using merged models, bypass all individual LoRAs to avoid conflicts**
  - Context: Since LoRAs are already merged into the model
  - *From: VRGameDevGirl84(RTX 5090)*

- **T2V LoRAs work with I2V models**
  - Context: Can use T2V trained LoRAs with I2V and Phantom models
  - *From: Thom293*

- **UniPC scheduler gives more natural look compared to DPM++ variants**
  - Context: Scheduler choice affects the final aesthetic
  - *From: VRGameDevGirl84(RTX 5090)*

- **For audio generation through LoRA, encode optical audio inspired melspec band across bottom of video frame**
  - Context: Creates frame-accurate audio like Veo3 in lo-fi quality
  - *From: ZombieMatrix*

- **In Phantom can use 1 image and black image in second slot**
  - Context: Black/white image gets ignored by Phantom, useful when only wanting 1 input without breaking lines
  - *From: Thom293*

- **Higher shift values give VACE better similarity to reference**
  - Context: Can sort of override depth control, keeps outfit and hairstyle better
  - *From: MysteryShack*

- **Use reward LoRAs to counter inconsistencies when using 720p model at lower resolutions**
  - Context: Helps with hallucinations from resolution mismatch
  - *From: Jonathan*

- **Use Image Blend at 0.50 for VACE workflows**
  - Context: 0.70-1.0 the pose control can sometimes bleed through. Gives good physics/depth fullness with DepthMap
  - *From: CaptHook*

- **Mask out background and use subject alpha for Ref Image background 100%**
  - Context: For VACE workflows with pose control
  - *From: CaptHook*

- **Better to use separate LoRAs instead of baked merges**
  - Context: Baked merges can't adjust LoRA strengths, so what works great for some generations won't work well for others
  - *From: Jonathan*

- **For seamless looping, make your video separately first then feed to loop workflow**
  - Context: This was best solution found after struggling with seamless looping across various models
  - *From: The Shadow (NYC)*

- **Maintain 720 pixels on shortest edge for various aspect ratios**
  - Context: Most normal aspect ratios will work grand (16:9, 16:10, 3:2 + vertical equivalents)
  - *From: DevouredBeef*

- **Use concatenated 16:9 videos stacked vertically for comparisons**
  - Context: When comparing different generations side by side
  - *From: A.I.Warper*

- **Use real face images as reference for best Phantom results**
  - Context: Gets much better quality than AI-generated faces
  - *From: VRGameDevGirl84(RTX 5090)*

- **Keep Google translate open when WAN doesn't respond to English**
  - Context: Chinese prompts often work better
  - *From: garbus*

- **Dial down end percentage of camera control for VACE to 0.05 when using with Phantom**
  - Context: Helps avoid distortion and glitches, use strength at 0.9
  - *From: Guey.KhalaMari*

- **Generate manually rather than using context options**
  - Context: Context options give much worse output quality
  - *From: Yae*

- **Use self-forcing VACE with LCM for fast results**
  - Context: Works well with 4-8 steps for quick testing
  - *From: hicho*

- **Use fewer points in ATI when they overlap**
  - Context: Sometimes when i had a lot points that overlap each other, it would mess up in ATI
  - *From: Nathan Shipley*

- **Use 'large eyes' for natural results with people**
  - Context: For people I actually use 'large eyes' which will give a natural result (mostly)
  - *From: Thom293*

- **Source video quality matters for upscaling**
  - Context: Topaz is not great at fixing things, so the source needs to be as good as possible
  - *From: ingi // SYSTMS*

- **Train separate full body and face LoRAs**
  - Context: I usually end up with 2 chr lors.. full body and face.. depends on the shot
  - *From: Gateway {Dreaming Computers}*

- **Use color match for every I2V**
  - Context: I do color match same way for every single i2v
  - *From: CJ*

- **Use lower ControlNet strength for better results**
  - Context: 40% controlnet looks much better than 100% for character consistency
  - *From: Thom293*

- **Add full second at start for Multitalk adaptation**
  - Context: When using high audio gain, gives model time to adapt to tonality
  - *From: Charlie*

- **Use prompt changes between chunks for variety**
  - Context: Random prompts for each chunk + different ref images can create more interesting results
  - *From: TK_999*

- **Colors really matter with VACE - use black backgrounds**
  - Context: Black backgrounds make VACE track control points much better, especially for complex motion
  - *From: Jonathan*

- **Don't replace current LoRAs in FusionX workflow**
  - Context: The current LoRAs make up FusionX, but you can add more. Can swap CausVid for LightX though
  - *From: VRGameDevGirl84(RTX 5090)*

- **Use more than one image from video for extension to prevent jumping**
  - Context: When extending videos
  - *From: 88822364468412416*

- **The prompt is very important for v2v workflow**
  - Context: When using video-to-video workflows
  - *From: chrisd0073*

- **Cut out scene transitions to avoid jumps**
  - Context: When processing longer video segments
  - *From: Faust-SiN*

- **Break long videos into chunks with overlap for blending**
  - Context: For processing videos longer than GPU memory allows
  - *From: voxJT*

- **Lower shift to 1-2 for better motion**
  - Context: If using 4+ shift it will greatly degrade motion
  - *From: Jonathan*

- **Use accvid at high strength to fix causvid's motion degradation**
  - Context: When using causvid LoRA
  - *From: Jonathan*

- **Switch to 1.3b models/loras for faster upscaling**
  - Context: 1.3b takes 2-4min while 14b takes 10x longer
  - *From: N0NSens*

- **Remove background and only have character with grey 127,127,127 color value**
  - Context: For better character consistency in reference images
  - *From: Gateway {Dreaming Computers}*

- **Use fixed seed and simplify concepts for practice runs**
  - Context: When dialing in VACE settings
  - *From: Guey.KhalaMari*

- **Don't place camera control points on objects mentioned in prompt**
  - Context: VACE might confuse and move the object instead of camera
  - *From: Jonathan*

- **Don't place camera spline start on completely empty area**
  - Context: VACE might try to inpaint something or not know what's moving
  - *From: Jonathan*

- **Visualize how 2 points will move over time (parallax effect)**
  - Context: For camera movement with VACE splines
  - *From: Jonathan*

- **Don't plug monitor into main model GPU**
  - Context: Consumes 0.5-1GB VRAM in multi-GPU setup
  - *From: el marzocco*

- **Use mid-grey for empty frames in VACE**
  - Context: When setting up VACE workflows, since the model was trained on this shade
  - *From: Ablejones*

- **Lower frame counts improve quality**
  - Context: 17 frames gave really good quality while 81 frames lost quality on 12GB VRAM
  - *From: mdkb*

- **Consider GPU load when using add-ons**
  - Context: For 12GB VRAM, avoid pushing too hard with all add-ons and use less of them
  - *From: Atlas*

- **Explicit prompting needed for specific objects**
  - Context: Only got lighter and cigarette when explicitly prompted for them
  - *From: Cseti*

- **Don't mention character in prompt for VACE integration**
  - Context: When using VACE with ref image, not mentioning character allows it to integrate into whatever is in the image
  - *From: ingi // SYSTMS*

- **Use edge glow prompting technique**
  - Context: Add 'the edges of [object] glows with a warm golden hue under the soft morning sunlight, creating a beautiful interplay of light and shadow' to prompts for enhanced lighting effects
  - *From: hicho*

- **Render first frame in 3D and send to WAN VACE with depth animation**
  - Context: When wanting to keep 3D render look while adding AI enhancements
  - *From: hicho*

- **Use Florence prompting for reference consistency**
  - Context: When you want consistent reference without morphing effects
  - *From: hicho*

- **Blur depth maps to control unwanted details**
  - Context: Blur depth of a woman so you don't get unwanted anatomy when prompting for a man
  - *From: hicho*

- **Use VAE decode tiled for better output quality**
  - Context: When using Benji's workflow, replace standard VAE decode with VAE decode tiled
  - *From: Vérole*

- **Frame rate interpolation workflow for higher FPS**
  - Context: Use GIMM x2 then RIFE x2 to get from 16fps to 64fps, then upscale from 832x480 to 1920x1080
  - *From: mdkb*

- **Use old SDXL/Flux prompts directly with WAN**
  - Context: Copy-paste old prompts work well, but WAN also works with basic prompts
  - *From: patientx*

- **For T2I use 8 steps optimal, for video 3-4 steps OK**
  - Context: Image generation needs more steps than video generation for quality
  - *From: N0NSens*

- **Use ChatGPT to expand prompts**
  - Context: Describe what you want in short sentence, get ChatGPT to make it medium length
  - *From: Atlas*

- **Break long videos into parts for upscaling**
  - Context: At 992p can only upscale 4 second videos at a time on RTX 5090 before running out of VRAM
  - *From: el marzocco*

- **Use LightX2V LoRA at 0.5 strength to prevent degradation in batch processing**
  - Context: When doing multiple batch generations
  - *From: A.I.Warper*

- **Don't blur masks in VACE - use clean masks with proper gray values**
  - Context: When using VACE inpainting
  - *From: Sal TK FX*

- **Pad reference images with white borders for VACE**
  - Context: When preparing reference images for VACE
  - *From: Sal TK FX*

- **Use style refs over prompts for more control**
  - Context: Professional use cases where control is important
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Create composite masks (arm + flame alpha) for complex VACE effects**
  - Context: When wanting elements that interact with subjects in 3D space
  - *From: Sal TK FX*

- **Use animated garbage masks for VACE instead of tracking**
  - Context: AI is smart enough to track characters automatically if mask roughly covers the area
  - *From: Hashu*

- **More generation steps improve likeness quality**
  - Context: Rushing generations in 4 steps causes drastically varying results
  - *From: Guey.KhalaMari*

- **Use 'ingredients' workflows instead of merge models**
  - Context: Easier to swap components and customize, less maintenance needed
  - *From: VRGameDevGirl84(RTX 5090)*

- **Fixed seed 666 works well for Chroma and Wan**
  - Context: User's preferred seed for consistent results
  - *From: l҈u҈c҈i҈f҈e҈r҈*

- **Drop 'concept check' into workflow for quick prompt testing**
  - Context: When testing how specific words affect generations without reloading
  - *From: garbus*

- **Avoid LLM generated prompts for precise control**
  - Context: LLMs casually add strong style words like 'baroque' that have huge effects
  - *From: garbus*

- **Use Florence for input image descriptions**
  - Context: When doing image rebatch to T2V with low denoise
  - *From: hicho*

- **Use CFG 1 with Fast Wan 1.3B model**
  - Context: 1.3B fast model runs optimally with CFG 1
  - *From: l҈u҈c҈i҈f҈e҈r҈*

- **Always use shift 1 for cfg and shift**
  - Context: User reports consistent good results with these settings since day 1
  - *From: patientx*

- **4 steps first pass + 8 steps second pass works better**
  - Context: Better than 8+4, produces more natural looking results
  - *From: patientx*

- **Add 'very slow motion' to prompt for better quality**
  - Context: Dramatically improves quality of results
  - *From: GOD_IS_A_LIE*

- **Use detailed prompting for character consistency**
  - Context: For T2V character stability across frames
  - *From: Cseti*

- **Add timing specifications to prompts**
  - Context: Use 'suddenly' or other timing words for better control
  - *From: garbus*

- **Use industry camera terminology**
  - Context: Terms like 'trucks in', 'dollies out', 'tilts up' work well
  - *From: TK_999*

- **Grade in post instead of chasing deeper colors**
  - Context: Use color correction nodes rather than manipulating model output
  - *From: Quality_Control*

- **Use very long prompts with slight modifications**
  - Context: Keep same seed and modify parts of prompt for character consistency
  - *From: KevenG*

- **Use Lightx2v lora for reducing total steps required**
  - Context: For fast generation with WAN2.2
  - *From: Atlas*

- **Default settings work great for CFG, Steps, and Scheduler**
  - Context: When using WAN2.2 14B in wrapper
  - *From: Atlas*

- **Bumped steps to 50 since original code**
  - Context: Using Kijai's 5b i2v workflow for better results
  - *From: orabazes*

- **Use 11-frame overlap with end/start frames**
  - Context: For creating seamless transitions between video clips using VACE
  - *From: ingi // SYSTMS*

- **Give VACE enough info so it knows how to handle motion**
  - Context: When creating transitions, main thing is providing sufficient motion context
  - *From: ingi // SYSTMS*

- **9 steps seems to be the sweet spot**
  - Context: For T2V wan 2.2 generation
  - *From: AshmoTV*

- **Use shift key when unhooking workflow nodes**
  - Context: When wanting to purposely mismatch step settings for custom splits
  - *From: 465174342225887233*

- **Low noise model manages character identity well**
  - Context: For character LoRAs, low model should handle details like tattoos better
  - *From: 465174342225887233*

- **Use Q8_0 GGUF for memory efficiency**
  - Context: When running on 12GB VRAM like RTX 3060
  - *From: 993837056159649822*

- **V2V is best for people who don't want complex prompting**
  - Context: Simpler alternative to elaborate text prompts
  - *From: hicho*

- **More LoRA strength = less steps needed**
  - Context: General relationship between LoRA strength and sampling steps
  - *From: hicho*

- **Use generation previews to find good settings**
  - Context: Especially helpful when working with new Lightning LoRAs
  - *From: Rainsmellsnice*

- **Tell first sampler it's going for 20 steps even when only doing 4**
  - Context: Works better with new Lightning LoRA
  - *From: Rainsmellsnice*

- **Generate at 720p resolution**
  - Context: Required for proper workflow function
  - *From: AshmoTV*

- **Use fast wan lora at 0.5 on low noise pass**
  - Context: For better results in multi-sampler workflows
  - *From: AshmoTV*

- **Remove negative prompt for vibrant colors**
  - Context: Negative prompt contains 'Vibrant colors' which can wash out colorful prompts
  - *From: kendrick*

- **Try running models with empty prompts**
  - Context: Good way to see what the model generates naturally, often produces coherent results
  - *From: 142265542647087104*

- **Use simple timesteps followed by visual instructions instead of JSON format**
  - Context: For prompt scheduling with I2V
  - *From: AshmoTV*

- **Add 'photorealistic style, ultra details, 4K' to prompts**
  - Context: When you want realistic results instead of illustrations
  - *From: N0NSens*

- **Use two-pass workflow with denoise 0.2 on second pass**
  - Context: Better results than default single-pass workflow
  - *From: patientx*

- **Merge 1.1 LoRAs with high and low noise models**
  - Context: New 1.1 LoRAs work well and surprisingly good with low step counts
  - *From: patientx*

- **Stack controlnet images for better control in WanFun 2.2**
  - Context: Better control but may need to crop the output
  - *From: smithyIAN - 4080ti Super 16gig*

- **Use lower control strength with Fun Control**
  - Context: Can lower control to 0.25 and still get it to follow general movement due to its strength
  - *From: Hashu*

- **Schedule LoRA strength for image-only trained LoRAs**
  - Context: Start lower on both high/low noise models so motion isn't affected, ramp to max strength, then taper down. Use slightly lower values on low noise model
  - *From: ingi // SYSTMS*

- **Use Fun reference instead of start frame**
  - Context: Smart enough to blend differences and not pop on first frame
  - *From: Hashu*

- **Generate at small resolution then upscale**
  - Context: Generate at 512x256 then 4x upscale to 2048x1024 in one shot for better results
  - *From: Fill*

- **Keep things simple first**
  - Context: Only make things complex when simple doesn't work
  - *From: Fill*

- **Use batch generation and pick best result**
  - Context: Generate batch of 4 at 512x256, pick best one before upscaling
  - *From: Fill*

- **Training vs complex workflows**
  - Context: Instead of building complex workflows, consider training a LoRA - 'prompt magic? no just training'
  - *From: Fill*

- **Use diffusion pipe for WAN tools**
  - Context: When asked about preferred tools for WAN
  - *From: Fill*

- **CFG scheduling with Lightning models**
  - Context: Drop CFG from regular setting to CFG1 in later steps
  - *From: TK_999*

- **Use JSON structured prompts for better following**
  - Context: JSON structure helps model follow prompts more accurately
  - *From: Juan Gea*

- **Use Qwen image edit paired with VACE**
  - Context: Very useful combination for video generation
  - *From: Dream Making*

- **Update WanVideoWrapper before using InfiniteTalk**
  - Context: Required for proper functionality
  - *From: seitanism*

- **Use LLM for camera movement prompt structure**
  - Context: When having difficulty structuring prompts for camera movements
  - *From: NebSH*

- **Try InfiniteTalk with silent audio for non-talking characters**
  - Context: When you want characters to not talk during action
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Always resize if image resolution is big**
  - Context: Use 480x480 for sure when working with limited VRAM
  - *From: AiGangster*

- **Don't pull hair out over video generation limitations**
  - Context: If you can get 90% there with generation, do light editing for the rest like lightning effects
  - *From: 177039592808120321*

- **Use angry facial expression in initial image for emotional TTS**
  - Context: To get angry expression in lip sync, start with image showing angry face since TTS voice alone won't convey emotion
  - *From: Charlie*

- **Fantasy Portrait has slight slow motion effect**
  - Context: Always small slow motion effect that was bothersome before infinite talk, may need addressing
  - *From: 𝕯𝖗. 𝕸𝖆𝖈𝖆𝖇𝖗𝖊 ☠*

- **Use lightx2v lora strength at 1.5**
  - Context: Works better according to KJ tests
  - *From: hicho*

- **Keep distill lora high setting on 3**
  - Context: For quality results
  - *From: Charlie*

- **Use CFG 1 with lightx2v, not higher values**
  - Context: For proper lora performance
  - *From: hicho*

- **Be careful not to do too many steps with distill loras**
  - Context: To prevent burning and maintain consistency
  - *From: Kijai*

- **Align reference image with control video for good results**
  - Context: When using Fun Control with reference image
  - *From: hicho*

- **Separate prompts work better than one long prompt for movies**
  - Context: Split prompt per video iteration for better results
  - *From: 621093216959201281*

- **Mask only mouth on some scenes with InfiniteTalk**
  - Context: Prevents issues like moving eyes suddenly stopping
  - *From: 𝕯𝖗. 𝕸𝖆𝖈𝖆𝖇𝖗𝖊 ☠*

- **Use batch masking and multiple audio for each character**
  - Context: For MultiTalk to get right people speaking the lines
  - *From: 𝕯𝖗. 𝕸𝖆𝖈𝖆𝖇𝖗𝖊 ☠*

- **Use 2+2 for t2v but 4+4 on i2v**
  - Context: For optimal quality balance
  - *From: U̷r̷a̷b̷e̷w̷e̷*

- **Use natural face expressions for lip sync**
  - Context: Because of context window - init image will be repeated each window
  - *From: N0NSens*

- **Keep around 4 frames with start frame to prevent madness**
  - Context: When using Pusa LoRA
  - *From: 𝕯𝖗. 𝕸𝖆𝖈𝖆𝖇𝖗𝖊 ☠*

- **Use recommended Pusa settings 1.5/1.4 with right prompts**
  - Context: Following Throttlekitty's example prompts helps get very good results
  - *From: Gill Bastar*

- **Use 'woman' not 'girl' in prompts to avoid inappropriate content**
  - Context: When generating human subjects
  - *From: kendrick*

- **Try multiple seeds before judging model or prompt**
  - Context: One seed isn't enough to evaluate performance
  - *From: hicho*

- **Seed really matters for quality**
  - Context: Batch of 10 may only yield 3 good results
  - *From: T2 (RTX6000Pro)*

- **Use BF16 as base for GGUF conversion**
  - Context: Don't convert FP8 to GGUF, use BF16 base
  - *From: patientx*

- **Need more motion for better V2V results**
  - Context: InfiniteTalk works better with more dynamic movement
  - *From: U̷r̷a̷b̷e̷w̷e̷*

- **Up the steps to get coherent hands with InfiniteTalk**
  - Context: Hand generation improvement
  - *From: TimHannan*

- **Plan video segments with varying lengths for better results**
  - Context: Use different frame counts (some very short, most 41 frames, some 81 frames) and abstract shapes as key images with motion design keywords
  - *From: 947112250198618162*

- **Use Nano Banana for image editing between generations**
  - Context: Edit images with 'add speed lines', 'change angle', etc. and use Wan for transitions between edited images
  - *From: 947112250198618162*

- **HPS LoRA problematic for I2V**
  - Context: HPS tries to draw details where it shouldn't in I2V, better for T2V use cases
  - *From: N0NSens*

- **MPS LoRA starting point**
  - Context: 0.5 strength is a good starting point for MPS LoRA to improve movement
  - *From: N0NSens*

- **Different MPS/HPS settings for high vs low noise**
  - Context: Try 0.5 on high noise, 1.0 on low noise, or disable HPS on high and use 1.0 on low for details
  - *From: GalaxyTimeMachine (RTX4090)*

- **Use 50% gray images between control frames**
  - Context: When using VACE with first-last frame workflow for better control
  - *From: ingi // SYSTMS*

- **Close background apps for long generations**
  - Context: When generating long videos with InfiniteTalk, turn off Discord and other apps so PC only works with ComfyUI
  - *From: Charlie*

- **Use low denoise for character consistency**
  - Context: When using USDU detailer for upscaling - low denoise adds detail without losing character consistency
  - *From: mdkb*

- **Gen at lower resolution first**
  - Context: Generate at low resolution like 624x368 or 480x480, then upscale with Topaz for efficiency
  - *From: U̷r̷a̷b̷e̷w̷e̷*

- **Use 720p for better lip sync**
  - Context: 720p generates better lip sync results with the 720 model in InfiniteTalk
  - *From: Charlie*

- **Separate vocals with UVR5 for cleaner audio-driven video**
  - Context: Use UVR5 to separate vocals from background music/SFX, use clean vocals for video gen, then combine with original audio
  - *From: U̷r̷a̷b̷e̷w̷e̷*

- **Use 10 frame overlap for smooth transitions in context windows**
  - Context: When extending videos with VACE 2.2 context windows
  - *From: Vérole*

- **Automasking faces out of controlnets can improve results**
  - Context: When people get closer to camera in VACE generations
  - *From: 151330553629638656*

- **Use blend mode 'screen' at 0.25 strength for combining controlnets**
  - Context: When combining pose and depth maps for better control
  - *From: mdkb*

- **Keep video length at 81 frames and multiple of 16+1**
  - Context: For optimal performance with WAN models
  - *From: ingi // SYSTMS*

- **Use fp8 e3m2 models for both VACE and WAN to avoid compatibility issues**
  - Context: When running complex workflows with multiple model components
  - *From: mdkb*

- **Test at lower resolution first with fast settings, then increase resolution and steps**
  - Context: When developing workflows to save time during testing
  - *From: VRGameDevGirl84(RTX 5090)*

- **Avoid full body shots for long videos**
  - Context: Full body shots get wonky in longer video generations
  - *From: VRGameDevGirl84(RTX 5090)*

- **Use headshot for reference image to maximize input details**
  - Context: For HuMo generations, then prompt for body shape/outfit
  - *From: 1348584179440418868*

- **Use camera and lighting in prompts**
  - Context: Remember to specify camera and lighting to help convey the story when using Wan prompt generator
  - *From: The Coin Hunter*

- **Disable SAM masking for raw background images**
  - Context: Use pretty much default settings but disable SAM masking and use raw background images
  - *From: VK (5080 128gb)*

- **Use detailed source images**
  - Context: For WanAnimate, the source image needs to have the same level of detail as desired output
  - *From: T2 (RTX6000Pro)*

- **Use slow-motion content for better results**
  - Context: Fast moving content is harder to process well
  - *From: T2 (RTX6000Pro)*

- **Mask only one character**
  - Context: For interaction scenes, leave one character unmasked
  - *From: T2 (RTX6000Pro)*

- **Try several seeds for I2V extensions**
  - Context: When extending clips with only one frame to go off of, multiple attempts needed
  - *From: Ablejones*

- **Use Kling prompts for inspiration**
  - Context: Can go to Kling videos and get inspired, then use prompts with Wan
  - *From: hicho*

- **Lower steps and adjust settings for style transfer**
  - Context: For better artistic results, try 6/3 steps split, shift to 2, and higher resolution at 1280
  - *From: Dkamacho*

- **Use empty prompt with certain workflows**
  - Context: When experiencing issues, try leaving the prompt empty
  - *From: Charlie*

- **Include transparency trigger in prompt for Wan Alpha**
  - Context: Add 'the background of this video is transparent' in your prompt when using Wan Alpha LoRA
  - *From: U̷r̷a̷b̷e̷w̷e̷*

- **Work with AI-generated effects as storytelling elements**
  - Context: If AI gives you flickering light effects, incorporate them as firelight for campfire storytelling scenes
  - *From: mdkb*

- **Use specific seed for consistent animal card effects**
  - Context: Seed 44665634 makes animals remain on cards when they step out
  - *From: U̷r̷a̷b̷e̷w̷e̷*

- **Use LoRAs at strength 1 for dyno setup**
  - Context: When using the new dyno high and low LoRAs in 2+2 configuration
  - *From: U̷r̷a̷b̷e̷w̷e̷*

- **Extract frame 1, edit with seedream, use SAM masking workflow**
  - Context: For character replacement in WanAnimate using Kijai's example workflow
  - *From: A.I.Warper*

- **Ensure hands/paws visible in reference image**
  - Context: For WanAnimate - otherwise it hallucinates slightly furry hands when they need to appear
  - *From: A.I.Warper*

- **Extract last frame as image from previous run for consistency**
  - Context: To maintain character consistency across multiple runs in HuMo workflow
  - *From: Charlie*

- **Use cond in negative prompts**
  - Context: For proper conditioning in Wan 2.2 setup
  - *From: garbus*

- **Use Kinestasis LoRA with 'Banostasis concept' trigger**
  - Context: Inject more motion in T2V and I2V Wan22 runs, use 0.5-0.7 strength, HN only
  - *From: The Shadow (NYC)*

- **Disconnect mask and background option for better character focus**
  - Context: When using wan animate node and ref input takes account for background
  - *From: AR*

- **Use first-frame-last-frame for smooth transitions**
  - Context: Effective technique for creating seamless video sequences
  - *From: The Coin Hunter*

- **Record yourself moving to beat for audio-reactive animation**
  - Context: For creating characters that move in sync with music
  - *From: Dever*

- **Use detailed prompting with color palette specifications**
  - Context: For smooth morphing transitions between scenes
  - *From: The Coin Hunter*

- **Use Florence to describe first and last frames, then instruct LLM to morph**
  - Context: For precise morphing between two images while avoiding fade-in and camera moves
  - *From: 𝕯𝖗. 𝕸𝖆𝖈𝖆𝖇𝖗𝖊 ☠*

- **Start with crisp anime images from Qwen and generate in 720p**
  - Context: For achieving high quality morphing results
  - *From: 𝕯𝖗. 𝕸𝖆𝖈𝖆𝖇𝖗𝖊 ☠*

- **Have reference image match initial pose with hands visible**
  - Context: For better character consistency in video generation
  - *From: 800884790713647164*

- **Use ChatGPT for prompt generation**
  - Context: For creating good prompts for video sequences
  - *From: The Coin Hunter*

- **Test at 2 steps, final render at 8 steps with fixed seed**
  - Context: Workflow for efficient video generation
  - *From: gpbhupinder*

- **Use 'talking' in prompt for lip movement**
  - Context: When you want character lips to move
  - *From: hicho*

- **Change watermelon to other objects in cowboy prompt for variety**
  - Context: For dynamic western scenes
  - *From: hicho*

- **Use looping workflows to avoid manual repetitive work**
  - Context: Set up automated queuing for multiple clips
  - *From: reallybigname*

- **Cut prompts into pieces and change parts for alternative outputs**
  - Context: Avoids thinking about prompts from scratch
  - *From: hicho*

- **Use clean dataset for LoRA training**
  - Context: Main thing for successful LoRA training
  - *From: AshmoTV*

- **25f or 49f seems to be sweetspot for frame batches**
  - Context: Helps keep style from weakening over longer sequences
  - *From: The Shadow (NYC)*

- **FFLF approach works better than VACE for snappy transitions**
  - Context: When animation style lends itself to quick cuts
  - *From: The Shadow (NYC)*

- **Use LM Studio for faster processing**
  - Context: Qwen 3 VL 2B GGUF in LM Studio is faster than using model native in ComfyUI
  - *From: hicho*

- **Use ChatGPT to describe reference for VACE**
  - Context: For Fun VACE, got ChatGPT to describe the reference and used that as prompt
  - *From: AR*

- **Mix long prompts with system prompts for better results**
  - Context: Example: 'describe this image then add that the car gets hit by a huge rock' with custom system prompt
  - *From: hicho*

- **Hard cuts work better with loras**
  - Context: Wan model can do okay hard cuts without loras but lora makes it much more consistent
  - *From: Ablejones*

- **Use repeats, commas, and ellipses in Ovi prompts for more realistic speech**
  - Context: Mimicking natural speech hitches improves emotion and realism
  - *From: Thom293*

- **Add motion prompts between phrases in Ovi**
  - Context: Helps with more natural delivery and emotional expression
  - *From: Thom293*

- **Include cuss words for emotional context in Ovi**
  - Context: Profanity naturally adds emotional weight to speech generation
  - *From: Thom293*

- **Resample second half of schedule for high noise**
  - Context: Make full 20 step schedule then resample second half down to 2-3 steps for HN workflow
  - *From: Ablejones*

- **Use 2K input with 720p output for I2V**
  - Context: Basic settings: 10 steps, 5/5 split, produces good results
  - *From: 𝕯𝖗. 𝕸𝖆𝖈𝖆𝖇𝖗𝖊 ☠*

- **Focus on consistency over length**
  - Context: Having consistent characters and multi-angle shots is more important than achieving the longest shot
  - *From: 𝕯𝖗. 𝕸𝖆𝖈𝖆𝖇𝖗𝖊 ☠*

- **Use 'comfy_chunked' rope setting and 'use_cpu_cache' true in VAE Loader**
  - Context: Lowers VRAM usage by 10-50% and prevents OOMs, allows full 1280x720 generation on 12GB card
  - *From: garbus*

- **Trim the first 4 frames after decoding FFGO output**
  - Context: Remove the first 4 frames (one latent) which is 1/4 second at 16fps to get clean output
  - *From: Zuko*

- **Start FFGO prompts with activation phrase then continue like normal Wan2.2 prompt**
  - Context: Use 'ad23r2 the camera view suddenly changes' then add detailed Wan2.2 prompting
  - *From: Zuko*

- **Use reference image as both first frame and in ref_images batch**
  - Context: Gives better consistency when using multiple references with HuMo
  - *From: 1076915303251988562*

- **Use precise, detailed prompting for better results**
  - Context: Model doesn't understand vague actions like 'takes bottle from sink' - specify exactly how, what she does with it
  - *From: Ablejones*

- **Include object descriptions in prompt to preserve details**
  - Context: When generating videos with text or specific objects, describe them in detail in the prompt
  - *From: garbus*

- **Use embroidery images as end frames rather than start frames**
  - Context: For formation/building animations where object should form into view
  - *From: AshmoTV*

- **Flip reference positions to change character spots in video**
  - Context: When using multiple characters with reference images
  - *From: Ablejones*

- **Use realistic descriptive prompts for better faces**
  - Context: To avoid plastic-looking faces, use prompts like 'realistic cute blond woman with red lips, blue eyes'
  - *From: hicho*

- **Don't use high model on sigma < 0.8**
  - Context: For proper Wan 2.2 usage with high/low model combination
  - *From: Ablejones*

- **Be specific rather than overly verbose in prompts**
  - Context: Complex detailed prompts might hurt prompt adherence, better to be specific than verbose
  - *From: Ablejones*

- **Use mask to exclude face from generation region**
  - Context: Only way to perfectly maintain face during video generation
  - *From: Ablejones*

- **For object addition/removal, use simple inpaint with gray box mask**
  - Context: Don't need complex conditioning for basic VACE inpainting tasks
  - *From: chrisd0073*

- **Increase resolution for better VACE inpainting results**
  - Context: Small objects like items on shelves need higher resolution to be properly inpainted
  - *From: Ablejones*

- **Use isolated reference images with white background**
  - Context: VACE works better with cleanly isolated reference images surrounded by white space
  - *From: Ablejones*

- **Position reference objects close to intended inpaint location**
  - Context: Reference image object placement should match where you want it inpainted in the video
  - *From: Ablejones*

- **Avoid mentioning object names when you want them to break**
  - Context: Instead of 'pearl necklace', use 'string of pearls delicately placed' for better breakage animation
  - *From: Ablejones*

- **Use Grow Mask with Blur for animated mask expansion**
  - Context: Allows mask to expand over time for objects falling or moving outside original area
  - *From: Ablejones*

- **Use reference images showing teeth for better likeness**
  - Context: Having the subject show teeth prevents perfect teeth which would reduce likeness in HuMo
  - *From: dj47*

- **Use 24fps for better SVI Pro 2.2 results**
  - Context: 24fps works better than other frame rates, helps with speed/motion consistency
  - *From: JohnDopamine*

- **Curation is everything for long-form content**
  - Context: Even with prompt automation, need perfect shot design, seed selection - variables compound and chances of greatness diminish to zero without curation
  - *From: ingi // SYSTMS*

- **Use Gemini for prompt generation**
  - Context: Can share video with Gemini and ask for prompts for specific effects, has generous free tier
  - *From: AshmoTV*

- **For background replacement, composite original footage back and add blur at image composite stage rather than on masks**
  - Context: When doing VACE background replacement workflows
  - *From: Hashu*

- **Use color matching on reference image to relight subject for new background**
  - Context: When replacing video backgrounds to make lighting look realistic
  - *From: Albert*

- **Keep workflow simple to start, then add complexity once it works**
  - Context: When troubleshooting VACE workflows - remove teacache, slg etc initially
  - *From: Hashu*


## News & Updates

- **Experimental TEACache added to long context example workflow**
  - Kijai added TEACache support to the context scheduling workflow
  - *From: Kijai*

- **New LoRAs available on Civitai**
  - Squish LoRA, Cakify LoRA, and Street Fighter Hadoken LoRA released
  - *From: multiple users*

- **Multiple Pika Labs effect LoRAs released**
  - Cakify, Squish, Inflate/Deflate, 360 rotation, Flying, and other effect LoRAs now available
  - *From: various users*

- **Musubi now supports Wan t2v training**
  - JohnDopamine got t2v training working with Musubi, though diffusion-pipe still has OOM issues
  - *From: JohnDopamine*

- **Mobius project for perfect looping**
  - New project for perfect video loops: https://github.com/YisuiTT/Mobius
  - *From: 211685818622803970*

- **Multiple concept loras in development**
  - Series including bossfight, traveling, stairwell, kungfu, driving and parkour loras for both 14B and 1.3B, trained on 100 videos each
  - *From: Kytra*

- **Native 1920x1080 generation confirmed working**
  - Just set latent size to 1920x1080, requires 80GB VRAM and ~2 hours
  - *From: Benjaminimal*

- **Multiple new concept loras released**
  - KXSR Cinematic Chase, First Person Flight, and character loras for Ryza released on Civitai with both 14B and 1.3B versions
  - *From: Kytra*

- **Vehicle montage lora completed and being tested**
  - Training completed, testing different epochs to find optimal version
  - *From: Kytra*

- **V2V masking workflow now available**
  - Video-to-video with masking capabilities working well with the wrapper
  - *From: IllumiReptilien*

- **Chasm's Call LoRA released for 1.3B**
  - LoRA for Pwnisher's newest youtube challenge trained by Kytra and collaborator, 14B param weights coming in next 24 hours
  - *From: Kytra*

- **Boss fight LoRA released for 1.3B**
  - Just dropped Boss fight lora for 1.3B model
  - *From: Fill*

- **VACE is now available for WAN**
  - Video control system with style transfer, currently supports LTXV and 1.3B WAN, works in KJ Wrapper
  - *From: DawnII*

- **New Ghibli Style T2V LoRA released**
  - SingularUnity WAN2.1 Ghibli Style T2V model available on Civitai with T2V metadata saved in outputs
  - *From: Amirsun(Papi)*

- **New high-res LoRAs for Wan released**
  - New wan hi-res loras came out, increases sharpness and clarity but may add too much contrast and saturation
  - *From: Jas*

- **14B Fun Control is back available**
  - 14b fun control is back on the menu, can't daisy chain like VACE but has good capabilities
  - *From: DawnII*

- **TheDirectorV2 tool released on MimicPC and coming to Civitai**
  - Does everything including music generation and prompting automatically
  - *From: AJO*

- **Adrien Toupet preparing masterclass on WAN 2.1 - 1.3b and VACE**
  - Shared YouTube preview of upcoming educational content
  - *From: Adrien Toupet*

- **VACE works with Diffusion Forcing**
  - DF works with VACE, tested within one window successfully
  - *From: Kijai*

- **Regional conditioning works with Wan**
  - Regional prompting works with Wan using rewanpatcher node, temporal conditioning also works allowing conditioning changes by frame range
  - *From: Clownshark Batwing*

- **Fun 1.1 fp8 version expected**
  - Fun 1.1 should be noticeably better for interpolation, waiting for fp8 version
  - *From: ezMan*

- **New LoRA training on Skyreels V2 I2V**
  - Training LoRAs on Skyreels V2 I2V using Musubi is now possible with different fp16 safetensors
  - *From: JohnDopamine*

- **Judy Hopps LoRA released for Wan2.1 14B**
  - Available on Civitai
  - *From: MisterMango*

- **VACE 14B model dropped**
  - New model for 14B released, preview version for 1.3B was already available
  - *From: JohnDopamine*

- **CausVid 1.3B demo available**
  - Can be used as regular model with 4 steps instead of usual 30
  - *From: yi*

- **Autoregressive CausVid generation coming**
  - Way faster than traditional method, not in ComfyUI yet
  - *From: yi*

- **New Phantom 14B custom model released**
  - Custom Phantom model available with improved likeness retention
  - *From: Thom293*

- **VACE Skyreel GGUF 24fps version available**
  - New 24fps version of VACE Skyreel in GGUF format provides smoother motion
  - *From: Vérole*

- **New toon LoRA and cinematic LoRA released**
  - Community member created new LoRAs for cartoon and cinematic styles
  - *From: VRGameDevGirl84(RTX 5090)*

- **Native ComfyUI support for Wan2.1/VACE being tested**
  - yukass testing native support that allows running 14B GGUF model on 4060 16GB
  - *From: yukass*

- **New anime mouth LoRA in development**
  - AIGambino working on anime mouth LoRA trained on video clips to capture proper talking movements
  - *From: AIGambino*

- **DMT v2 model released**
  - New fast model on top of wan and causvid, works as T2V, can be inserted into any wan workflow as pt file
  - *From: hicho*

- **McLaren 720s LoRA released**
  - Car LoRA released in community
  - *From: MisterMango*

- **Retro 90s Anime Golden Boy Style LoRA released**
  - Works for both T2V and I2V, includes detailed training description
  - *From: 138234075931475968*

- **FusionX LoRA released**
  - LoRA extracted from fp16 version of FusionX model, works as if all LoRAs were merged into single LoRA
  - *From: VRGameDevGirl84(RTX 5090)*

- **New Self-Forcing trained Wan 1.3b model released**
  - Claims real-time HD video generation with 17 FPS on 1 H100, fixes exposure bias problem
  - *From: SS*

- **FAL now allows T2V checkpoint LoRA training**
  - Can train LoRAs on still images for video generation
  - *From: A.I.Warper*

- **Phantom Pro model slated for release**
  - Trained on higher resolutions than the current 14b model
  - *From: JohnDopamine*

- **New distillation dropped**
  - New distillation dropped today
  - *From: TK_999*

- **Particle Grid Animator updated with export frames**
  - Now features export frames button which makes a .ZIP with PNG image sequence
  - *From: Nathan Shipley*

- **New Color Correction LoRA V2 in testing**
  - V2 being tested at 480p, V3 coming with stronger sharpness
  - *From: 211685818622803970*

- **FusionX model trending on HuggingFace**
  - VRGameDevGirl84's FusionX model organically trending, created accessibility for WAN
  - *From: fredbliss*

- **New DiffTrack model released**
  - New tracking model from CVLAB-KAIST dropped
  - *From: TK_999*

- **Kijai is on vacation**
  - Only got 1 person multitalk working, progress on multitalk stalled
  - *From: CJ*

- **ComfyUI Musubi trainer project available**
  - New LoRA training project for ComfyUI
  - *From: Guey.KhalaMari*

- **New retro anime/golden boy lora released**
  - Updated version works for both T2V and I2V
  - *From: 138234075931475968*

- **Skyreels models available on Kijai's HuggingFace**
  - Both T2V and I2V versions, 24fps with unlimited length
  - *From: VRGameDevGirl84(RTX 5090)*

- **SageAttention speed improvements coming to VACE**
  - Kijai discovered he left VACE off the SageAttention speed optimization, will be rolled out soon
  - *From: mdkb*

- **Pusa V1.0 new video model released**
  - New open source video generator based on Wan claiming better results and faster performance, Kijai extracted a LoRA version
  - *From: brbbbq*

- **New LightX2V LoRA version available**
  - Updated version that works better with Pusa
  - *From: VRGameDevGirl84(RTX 5090)*

- **Pusa is now supported by Kijai's wrapper**
  - Already integrated into the ComfyUI ecosystem
  - *From: hicho*

- **ARC-Hunyuan-Video got initial commit on Tencent's HuggingFace**
  - Possible new model on the way from Tencent
  - *From: JohnDopamine*

- **Fastwan LoRA released**
  - Released 5 hours ago, extracted from 14B fastwan 480p model
  - *From: DawnII*

- **Wan 2.2 is out**
  - New version with MoE architecture and improved capabilities
  - *From: multiple users*

- **Wan-KF2V (keyframe-to-video) in development**
  - Extension of i2v to n-image keyframe video generation
  - *From: Benjaminimal*

- **8-hour speedrun implementation**
  - Team had 8-hour call to implement 2.2 without advance code or weights
  - *From: Benjaminimal*

- **Video-to-audio capability coming**
  - Wan v2a (video-to-audio) shown in development streams
  - *From: Benjaminimal*

- **GGUF versions available for Wan2.2**
  - Q8 GGUF versions confirmed working with wrapper
  - *From: Cseti*

- **bf16 version of 14b-i2v model released**
  - Mixed weights model that preserves important fp32 parts available on HuggingFace
  - *From: Benjimon*

- **Yoshiaki Kawajiri retro anime style LoRA released**
  - Experimental Wan 2.2 LoRA available on Civitai, high noise model still needs training
  - *From: tarn59*

- **High noise version of anime style LoRA released**
  - Released high noise version on Civitai, still wants to add more to dataset and train low model more
  - *From: tarn59*

- **Lightning LoRAs v1.1 released**
  - Available on Kijai's HuggingFace repo with improvements over v1.0
  - *From: patientx*

- **I2V LoRAs now available**
  - Released alongside the T2V v1.1 updates
  - *From: Rainsmellsnice*

- **New AIO Wan model released**
  - New version available but showing unstable behavior
  - *From: l҈u҈c҈i҈f҈e҈r҈*

- **New 5B model variant available**
  - Another model option released
  - *From: l҈u҈c҈i҈f҈e҈r҈*

- **Wan 2.2 5B model has been fixed**
  - Updated model available on Kijai's repo performs much better
  - *From: l҈u҈c҈i҈f҈e҈r҈*

- **5B Fun model coming**
  - Based on code branch analysis
  - *From: DawnII*

- **Kijai implemented res_multistep in the wrapper**
  - Recently added sampler option
  - *From: TK_999*

- **Wan 2.2 version expected for Stand-In LoRA**
  - Stand-In LoRA currently designed for 2.1, but 2.2 version is on their to-do list
  - *From: orabazes*

- **MultiTalk v2 speculation clarified**
  - User clarified they misinterpreted v2v (video-to-video) as Version 2, no actual MultiTalk v2 exists
  - *From: 444330516385103883*

- **Kijai made e5m2 model for Phantom**
  - New model posted to HF repo, solves 3060 incompatibility issues
  - *From: mdkb*

- **WAN Fun 2.2 integrated but having issues**
  - Newly integrated Wan Fun producing weird results, applying ref image to video instead of driving with it
  - *From: 𝕯𝖗. 𝕸𝖆𝖈𝖆𝖇𝖗𝖊 ☠*

- **InfiniteTalk integration in WanVideoWrapper**
  - New lip sync system that works without driving video, just released
  - *From: JohnDopamine*

- **Multiple people support for Fantasy Portrait**
  - Pull request added to support multiple people in Fantasy Portrait
  - *From: ManglerFTW*

- **Melband audio node added by KJ recently**
  - New audio processing node available for workflows
  - *From: Bleedy (Madham)*

- **WanFaceDetailer tool available**
  - New face detailing tool for Wan videos posted on Reddit
  - *From: 1048309186322243594*

- **Pusa LoRA now works in native ComfyUI**
  - Previously only worked in wrapper, now available natively
  - *From: asd*

- **Debut dates for FA Berlin event**
  - September 26th-28th at fa-berlin.com/en/
  - *From: fzyx*

- **New Fun HPS and Fun MPS LoRAs available**
  - Tested at 0.5 and 1.0 strength, definitely help even at 4 steps
  - *From: patientx*

- **Kijai has been very active with WanVideoWrapper updates**
  - Frequent updates to the wrapper
  - *From: DennisM*

- **Skin enhancer nodes in development**
  - Trying to replicate Enhancer AI functionality
  - *From: asd*

- **Wan 2.2 MPS/HPS LoRAs officially released**
  - New versions specifically for Wan 2.2 available on Kijai's HuggingFace repository
  - *From: mdkb*

- **VRGameDevGirl84 DEV branch updated**
  - Updated DEV branch for MagRef-InfiniteTalk Music video creator workflow
  - *From: VRGameDevGirl84(RTX 5090)*

- **ComfyUI Wan prompt generator translated fork**
  - English translation fork created for Chinese Wan prompt generator node
  - *From: GalaxyTimeMachine (RTX4090)*

- **WAN Animate model now available**
  - New WAN Animate model available on HuggingFace Spaces that maintains facial expressions and input fidelity while adding motion
  - *From: 168373586812207104*

- **Wan 2.5 available for testing**
  - Wan 2.5 can be tested on the Wan Video website and wavespeed.ai
  - *From: Visionmaster2*

- **VRGameDevGirl84 updating custom nodes soon**
  - Will update custom nodes with audio split node built in
  - *From: VRGameDevGirl84(RTX 5090)*

- **Wan 2.5 available**
  - Available on create.wan.video/generate with T2V and audio generation
  - *From: DawnII*

- **Free generation with queue system**
  - Everything is free, just need to wait in queue. 1080p with audio generated without credits
  - *From: DawnII*

- **New LightX T2V LoRA Released**
  - Wan2.2-Lightning T2V LoRA was released by lightx2v team with comparison tests
  - *From: BNDC APP*

- **Dyno model released**
  - New t2v high noise model from lightrx team available as full model and in fp8 version
  - *From: asd*

- **VACE 2.2 transition workflow shared**
  - Ingi shared the transition workflow for VACE 2.2 object replacement
  - *From: ingi // SYSTMS*

- **Wan 2.2 finally fixed with dyno LoRAs**
  - Community confirms Wan 2.2 is now working well with the new dyno lightning LoRAs
  - *From: hicho*

- **Time to remove Wan 2.1**
  - Suggestion that Wan 2.2 improvements make 2.1 obsolete
  - *From: hicho*

- **MMAudio for ComfyUI now available**
  - https://github.com/kijai/ComfyUI-MMAudio
  - *From: Vérole*

- **ComfyCloud in beta testing**
  - Currently free during beta, will likely become paid service
  - *From: Vérole*

- **WanHumoMVC_V7.1 released**
  - Updated version of the workflow
  - *From: WackyWindsurfer*

- **Holocine model available**
  - Can be used with implementation or just weights
  - *From: Benjimon*

- **New Mocha model released**
  - Being tested by community
  - *From: Dkamacho*

- **Wan 2.5 available on create.wan.video**
  - Available on official platform
  - *From: hicho*

- **New 10s OVI released**
  - Much less static than old OVI, better motion
  - *From: Simonj*

- **HuMo I2V compatibility patch available**
  - Made a patch to allow HuMo to work with I2V
  - *From: Ablejones*

- **Wan 2.5 released and working**
  - Users are successfully generating with Wan 2.5
  - *From: hicho*

- **SAM3 (Meta) released within past week**
  - Text prompts to masks functionality, seems really good at mask generation
  - *From: JohnDopamine*

- **DaVinci recent update added AI FX for frame generation**
  - Can generate 1-2 frames to make cuts smooth, works pretty well
  - *From: Lumifel*

- **WanVaceAdvanced nodes updated to support context windows with VACE**
  - Needs pending ComfyUI PR to be merged for full functionality
  - *From: Ablejones*

- **TrentNodes repository updated with VACE keyframe builder**
  - New nodes for placing keyframes for VACE, fixes gray value error
  - *From: Flipping Sigmas*

- **ComfyUI updates improved GGUF support**
  - Recent ComfyUI updates allow WAN 2.2 GGUF Q4 to run without block swap on 6GB cards
  - *From: hicho*

- **New node announced**
  - Someone mentioned a new node being announced but couldn't find the message about it
  - *From: 800884790713647164*

- **SVI 2.2 Pro available**
  - The new SVI 2.2 Pro model is available and performing well
  - *From: JohnDopamine*

- **ingi releasing Wan 2.2 LoRAs**
  - Dropping some Wan 2.2 LoRAs on the same link as Qwen Image Edit LoRA
  - *From: ingi // SYSTMS*


## Workflows & Use Cases

- **Multi-segment video generation with LLM prompting**
  - Use case: Generate longer sequences by using last frame as input for next segment with AI-generated prompts
  - *From: AJO*

- **V2V upscaling pipeline**
  - Use case: Upscale lower resolution videos to higher resolution using V2V with low noise (0.05-0.25)
  - *From: DiXiao*

- **LoRA training workflow**
  - Use case: Train custom LoRAs on Wan models using DiffSynth repo training code
  - *From: Kytra*

- **Multi-section continuation using last frame as next section start**
  - Use case: Creating longer sequences by chaining generations
  - *From: JmySff*

- **FlowEdit for T2V and I2V operations**
  - Use case: Using FlowEdit with bypass of I2V conditioning nodes for T2V
  - *From: Zuko*

- **Infinite SNES sprite creator using trained LoRAs**
  - Use case: Game asset creation with consistent sprite generation
  - *From: Kytra*

- **Game asset generation at low resolution**
  - Use case: Creating pixel art game assets by scaling down to 64 pixels
  - *From: Fill*

- **T2V -> HV -> UPSC -> MMA pipeline**
  - Use case: Generate with Wan T2V, enhance with HunyuanVideo, upscale and add audio
  - *From: burgstall*

- **T2V 640*360 -> 2x upscale -> HYVID I2I -> 2x upscale**
  - Use case: Multi-stage upscaling and enhancement workflow
  - *From: burgstall*

- **Infinite looping system**
  - Use case: Generate 5 loops of 81 frames each at 832x480, with 2xRIFE and compile at 25fps
  - *From: AJO*

- **Wan + HunyuanVideo enhancement**
  - Use case: Use Wan for initial T2V then HunyuanVideo as second step to enhance and upscale
  - *From: VRGameDevGirl84(RTX 5090)*

- **FlowEdit video-to-video**
  - Use case: Use FlowEdit on first frame, then run through Wan I2V for style transfer and character variations
  - *From: Zuko*

- **Two-pass rendering with 14B lowres + 1.3B upscale**
  - Use case: Getting good motion from 14B then detail enhancement with 1.3B
  - *From: spacepxl*

- **Video extension using last frame with different models**
  - Use case: Extending videos by reversing frames and blending
  - *From: DevouredBeef*

- **Multidiffusion temporal and spatial upscaling**
  - Use case: Upscaling video with both time and space tiling
  - *From: Benjaminimal*

- **LTXV to Wan v2v transfer**
  - Use case: Video style transfer and enhancement
  - *From: ZombieMatrix*

- **Hunyuan T2V + Wan extensions**
  - Use case: Long video generation with audio
  - *From: Organoids*

- **Multi-generation extension workflow**
  - Use case: Extended video sequences
  - *From: Organoids*

- **Storyboarding system with FlowChain nodes**
  - Use case: Automating complex multi-step workflows by embedding whole workflow APIs inside another workflow
  - *From: AJO*

- **T2V then I2V x6 extension**
  - Use case: Creating longer videos by chaining multiple I2V generations
  - *From: garbus*

- **Automated storyboarding system**
  - Use case: Generate multiple scene videos from single reference image with LLM-driven scene creation
  - *From: AJO*

- **7-clip generation and merging for longer content**
  - Use case: Create extended sequences by generating multiple clips with t2v + depth + character lora, then merge
  - *From: Cseti*

- **I2V with latent masking in native ComfyUI**
  - Use case: Image-to-video with selective masking for targeted animation
  - *From: ArtOfficial*

- **V2V with Sam2 nodes for inpainting**
  - Use case: Video inpainting using Kijai I2V workflow combined with Sam2 segmentation
  - *From: IllumiReptilien*

- **Video inpainting with Flux first frame**
  - Use case: Inpaint what you want on first frame with flux, load in workflow, mask the video where needed
  - *From: IllumiReptilien*

- **Automated story generation with image selection**
  - Use case: Single queue using looping with start images generated inside queue with LLMs, system pauses to let user choose images
  - *From: AJO*

- **Regional conditioning for video**
  - Use case: Split video into 3 regions with different conditioning, works along temporal dimension too
  - *From: Clownshark Batwing*

- **Multi-pass workflow with WAN + AnimateDiff + upscaler**
  - Use case: WAN raw output sent through second animatediff pass using depth and softedge, then third pass through upscaler to reduce noise
  - *From: StableVibrations*

- **Background replacement with inpainting + WAN**
  - Use case: Simple inpainting with flux for background, then WAN lineart plus pose on original footage with video editor cleanup
  - *From: IllumiReptilien*

- **AI Influencer workflow**
  - Use case: 6 scenes, 30 mins cloud/20 mins on 5090, 8 steps, 480p
  - *From: AJO*

- **Ultra-wide panoramic video generation**
  - Use case: Creating cinematic wide shots at 2500x500 resolution using FLUX -> Wan21-i2v720
  - *From: ZombieMatrix*

- **VACE with segment anything 2 for V2V**
  - Use case: Video-to-video with precise masking using auto masking with Florence or points segments
  - *From: Vérole*

- **T2V guide mode using Clownshark sampler**
  - Use case: Using encoded image latent as guide for T2V generation with empty hunyuan video latent
  - *From: Clownshark Batwing*

- **Multi-scene character consistency system**
  - Use case: Generating multiple scenes with the same character, not for frame extension
  - *From: AJO*

- **VACE with auto masking systems**
  - Use case: Two automatic masking systems (Florence2 and Masking Points) integrated with VACE
  - *From: Vérole*

- **Subject removal using VACE**
  - Use case: Remove subjects from videos while preserving background elements
  - *From: ArtOfficial*

- **Face swapping with VACE**
  - Use case: Replace faces in videos using masking and reference images
  - *From: ArtOfficial*

- **Temporal conditioning with attention masking**
  - Use case: T2V with temporal attention masking tricks for scene transitions
  - *From: Clownshark Batwing*

- **TheDirector multi-scene generation**
  - Use case: Generate multiple scenes in single run with finished video output
  - *From: AJO*

- **VACE inpaint with MoGe generated scene models and Blender camera movements**
  - Use case: Creating 3D scene-based video inpainting
  - *From: DevouredBeef*

- **Fun vid2vid with 220 frames using frame extend and highres LoRAs**
  - Use case: Long video generation with 1.3B model
  - *From: Pol*

- **VACE with reference and control inputs**
  - Use case: Style transfer and character consistency
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Two-pass process: VACE first, then low denoise pass for cleanup**
  - Use case: Improving VACE output quality
  - *From: 88822364468412416*

- **Flux->Wan pipeline for ultra-wide generation**
  - Use case: Creating 5:1 aspect ratio videos for theater display, start with Flux at 2500x500 then upscale through Wan
  - *From: ZombieMatrix*

- **Wan->Wan->Wan->Flux->Wan sequence**
  - Use case: Upscaling process for high resolution outputs
  - *From: ZombieMatrix*

- **Gemini-powered automated generation**
  - Use case: 480 seed prompts feed Gemini for image prompts, then image+prompt feed Gemini again for video prompts
  - *From: 186438699213389825*

- **Diffusion Forcing temporal extension**
  - Use case: Extending videos while maintaining temporal coherence using 17 frame overlap
  - *From: Ablejones*

- **Long video generation with resampling**
  - Use case: Generate long videos using SkyReels 1.3b DF for individual clips, then refine each segment with WanFun 1.3b Inp with MPS reward LoRA
  - *From: Ablejones*

- **Bulk rendering queue system**
  - Use case: Work on images as keyframes first, then bulk animate 100-150 queued renders over 24-48 hours for multiple YouTube channels
  - *From: Level Higher*

- **Vid2vid quality improvement**
  - Use case: Use vid2vid from 1.3B to 14B model for quality enhancement
  - *From: ZombieMatrix*

- **VACE to 14B pipeline**
  - Use case: Style transfer using depth map and partial denoise, then 14B generation and upscale
  - *From: 88822364468412416*

- **DF (DreamForge) workflow**
  - Use case: Creating longer videos with 53 + 97 + 97 frames using different prompts per sampler
  - *From: Cseti*

- **Flux-Wan hybrid upscaling**
  - Use case: Complex workflow going Flux -> Wan -> Flux -> Wan -> Flux for upscaling from 2048w to 3520w
  - *From: ZombieMatrix*

- **Automated LLM to video pipeline**
  - Use case: Automatic workflow from LLM -> picture -> video using Wan Fun 1.1 1.3b
  - *From: Vérole*

- **Batch image-to-video with Florence2 descriptions**
  - Use case: Automated video generation from image sets
  - *From: reallybigname*

- **Flux + Wan upsampling process**
  - Use case: Ultra high-resolution image generation
  - *From: ZombieMatrix*

- **Logo animation technique**
  - Use case: Animating logos within scenes
  - *From: Level Higher*

- **AI-automated video production pipeline**
  - Use case: Automated social media content creation
  - *From: Level Higher*

- **Scene generation based on style, genre, time period**
  - Use case: Organizing generations with concatenated prompts for action sequences
  - *From: ZombieMatrix*

- **Tiled upscaling with 1.3B model**
  - Use case: Upscaling videos while keeping VRAM usage low
  - *From: Clownshark Batwing*

- **Latent guide video-to-video**
  - Use case: Using original video latents as guides for style transfer
  - *From: Ablejones*

- **Chain sampling for mid-generation parameter changes**
  - Use case: Changing models, parameters during generation process
  - *From: Clownshark Batwing*

- **VACE + LoRA for style transfer**
  - Use case: Applying artistic styles while maintaining character likeness
  - *From: JohnDopamine*

- **Reference + random pose + LoRA + CausVid**
  - Use case: Character likeness transfer with motion
  - *From: JohnDopamine*

- **Hand-drawn animation to video**
  - Use case: Converting drawn animations to video with consistent character movement
  - *From: 852話 (hakoniwa)*

- **Multiple model passes for refinement**
  - Use case: 14b VACE raw output → RecamMaster → 1.3b for background change → upscale/interpolation
  - *From: DawnII*

- **Context-based long video generation**
  - Use case: Generating videos longer than 81 frames using context chunks
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Video looping with VACE inpainting**
  - Use case: Creating seamless loops by splitting 30-frame video, putting second 15 frames at start, 51 blank frames in middle, first 15 frames at end
  - *From: Nathan Shipley*

- **3D to video pipeline with Blender + FlowEdit + Wan**
  - Use case: Professional VFX workflow using Blender for framing, FlowEdit techniques for img2img, Wan 2.1 with Remade AI LoRAs
  - *From: Nekodificador*

- **Character inpainting with VACE**
  - Use case: Inpainting characters into scenes while maintaining consistency
  - *From: Simonj*

- **Multi-pass generation and compositing**
  - Use case: Generate table, character, and background separately then composite in After Effects for complex scenes
  - *From: enigmatic_e*

- **Long video generation by chaining 81-frame runs**
  - Use case: Creating 400+ frame videos by splitting into batches and stitching in workflow
  - *From: A.I.Warper*

- **Two-pass VACE for face/clothing consistency**
  - Use case: First pass with full body ref, second pass cropping and fixing face with close-up ref
  - *From: hau*

- **Upscale then V2V for quality improvement**
  - Use case: Upscale with model node, resize, then run through V2V with T2V 14B at 0.3 denoise
  - *From: ArtOfficial*

- **VACE rough generation then Phantom refinement**
  - Use case: Generate rough video with VACE in 81-frame chunks, then refine with Phantom using context window
  - *From: tttADs*

- **Spline editor for camera movement control**
  - Use case: Creating complex camera movements and latent space transitions
  - *From: Nekodificador*

- **Image-as-video then V2V processing**
  - Use case: Faster alternative to traditional I2V, brings any image to life
  - *From: hicho*

- **Flux/Wan upsampler → Wan I2V → Wan T2V V2V pass**
  - Use case: Converting paintings to realistic animated scenes
  - *From: ZombieMatrix*

- **VACE with depth+dwpose blend control**
  - Use case: Character animation with outfit/pose control
  - *From: MysteryShack*

- **VACE with pose control instead of depth for character replacement**
  - Use case: Character replacement using pose data and style LoRA, with face inpainting for detail retention
  - *From: ingi // SYSTMS*

- **Multi-step video creation with upscale and inpainting**
  - Use case: Upscale in Topaz, mask with Sam2, crop and generate mask + base video in AE, inpaint, comp in AE
  - *From: ingi // SYSTMS*

- **Batch generation in Phantom**
  - Use case: Generate multiple consistent character videos using reference images
  - *From: VRGameDevGirl84(RTX 5090)*

- **Longer generation using context frames**
  - Use case: Generate videos longer than base frame limit, though first frame looks different even with same seed
  - *From: Zlikwid*

- **Loop workflow using OpenArt**
  - Use case: Creating seamlessly looped videos from existing videos
  - *From: Jonathan*

- **VACE workflow with DWPose+Depth and Image Blend**
  - Use case: Better physics and depth control with pose estimation
  - *From: CaptHook*

- **VRGameDevGirl84's FusionX workflow**
  - Use case: Fast I2V generation with optimized settings and LoRA combinations
  - *From: VRGameDevGirl84(RTX 5090)*

- **Manual 81-frame generation and stitching**
  - Use case: Creating longer videos by feeding last frame into new generation
  - *From: Yae*

- **VACE with depth from video for motion plus ref image**
  - Use case: Transferring motion from source video to different character
  - *From: VK (5080 128gb)*

- **Looping workflow with +3 seconds extension**
  - Use case: Creating seamless loops by adding frames to existing video
  - *From: Level Higher*

- **Using VACE for subject ref with text prompt backgrounds**
  - Use case: Maintaining subject likeness while varying background styles
  - *From: ingi // SYSTMS*

- **Phantom with multiple reference images**
  - Use case: Better character consistency by providing more reference material
  - *From: Guey.KhalaMari*

- **720p generation then upscale pass**
  - Use case: 720p, then a second pass with a upscale model and wan 1.3 model with no prompt and low denoise to get more resolution
  - *From: Gateway {Dreaming Computers}*

- **Character creation flow**
  - Use case: Start with concepts with flux workflow, get chr sheet, build flux lora, use wan360 lora for 360 turntable, train wan lora with frames
  - *From: Gateway {Dreaming Computers}*

- **Vace first-last frames for looping**
  - Use case: Looping longer videos
  - *From: Yae*

- **1000 frames per run with 81 context frames**
  - Use case: Long video generation with context overlap
  - *From: Yae*

- **Long video generation with context options**
  - Use case: Generate 35+ second videos by stitching 1000-frame chunks together in DaVinci Resolve
  - *From: Yae*

- **Orbit camera movement using multiple DF passes**
  - Use case: Creating smooth camera orbits by chaining multiple DF (Diffusion Forcing) runs with different prompts and control LoRAs
  - *From: Ablejones*

- **Two-pass upscaling: WAN V2V + Non-diffusion upscale**
  - Use case: Upscale from 576x1024 to 1080x1920+ using WAN diffusion v2v first, then upscale with model
  - *From: The Shadow (NYC)*

- **Endless video extension workflow**
  - Use case: Smooth video continuations with minimal seams, extends video 6x initially
  - *From: pom*

- **VACE self forcing with black background**
  - Use case: Better motion tracking by using black backgrounds with VACE
  - *From: Jonathan*

- **V2V pipeline for character consistency**
  - Use case: Long form storytelling with lipsync - used original video for motion, Flux for character generation, VACE for processing, upscaling, then Multitalk for lipsync
  - *From: voxJT*

- **Context windows for endless video**
  - Use case: Creating longer continuous video content
  - *From: Zlikwid*

- **VACE with depth/normal control**
  - Use case: Preventing LoRA drift into body horror while maintaining control
  - *From: Faust-SiN*

- **Multi-GPU generation setup**
  - Use case: Longer video generation by splitting model loading across GPUs
  - *From: el marzocco*

- **VACE ControlNet pose + align pose node + Spline Path Control**
  - Use case: Precise pose and motion control
  - *From: Jonathan*

- **Endless travel workflow for character and environment consistency**
  - Use case: Taking max advantage of consistency from new models like Kontext/Omnigen
  - *From: Ablejones*

- **Multi-GPU setup for VACE**
  - Use case: Load main model on one GPU and everything else on another
  - *From: el marzocco*

- **Video2video with VACE using 3D model source**
  - Use case: Rotating pyramid 3D model with clever prompts
  - *From: Gateway {Dreaming Computers}*

- **VACE travel workflow**
  - Use case: Creating travel sequences with amazing possibilities
  - *From: NelsonPorto111*

- **Keyframe generation with Kontext/Omnigen2 for long videos**
  - Use case: Creating keyframes for long video generations, splitting sampler where first steps use keyframe and remaining steps don't
  - *From: Ablejones*

- **Multiple first-frame-last-frame merged with VACE**
  - Use case: Creating longer coherent videos by merging multiple VACE segments
  - *From: hicho*

- **3D animation restyling with depth + VACE**
  - Use case: Taking 3D simulations/animations and restyling them using SDXL image2image then VACE with depth control
  - *From: hicho*

- **Phantom + MultiTalk two-pass workflow**
  - Use case: Generate video with Phantom for character consistency, then pass through MultiTalk V2V for lip sync
  - *From: AJO*

- **Segment Anything + VACE with masking**
  - Use case: Using Kijai's segment anything workflow with VACE workflow and style LoRA for character consistency
  - *From: Cseti*

- **3D viewport rendering to WAN processing**
  - Use case: Take 3D animation from viewport and render high quality results that would be impossible in 3D apps, avoiding scene management and light setup complexity
  - *From: hicho*

- **Benji's VACE extending workflow with POM transitions**
  - Use case: Long video generation with better transitions using WAN Video Blender node and modified math expression (a+b-10 instead of a+b)
  - *From: Vérole*

- **Depth map manipulation in Nuke for compositing**
  - Use case: Merge depth maps from different sources to control object placement and camera positioning
  - *From: T2 (RTX6000Pro)*

- **Magnifying glass control for body part focus**
  - Use case: Using custom magnifying node as control for VACE to focus on specific body parts like belly or hands
  - *From: ingi // SYSTMS*

- **FusionX + FaceNaturalizer LoRA workflow**
  - Use case: High quality image generation at 8 steps, 1024x1536 with no upscale
  - *From: patientx*

- **3D biped to VACE video generation**
  - Use case: Using 3dsmax biped with openpose-compliant mesh for accurate motion control
  - *From: Duranovsky*

- **VACE with controlnets for lipsync**
  - Use case: Pure v2v with controlnets and reference image, no multitalk needed
  - *From: mdkb*

- **Sequential image workflow**
  - Use case: Processing multiple images with default input length of 81 per image
  - *From: T2 (RTX6000Pro)*

- **VACE fire arm effect with dual mask approach**
  - Use case: Creating realistic fire effects that wrap around 3D objects
  - *From: Sal TK FX*

- **Neo removal workflow using VACE paint-out**
  - Use case: Removing objects from dynamic scenes with 10s duration
  - *From: Neex*

- **Multi-step character replacement process**
  - Use case: High quality character swapping: 1) Flux Inpainting + Redux + Shakker ControlNet with depth, 2) Wan VACE with depth + pose, 3) Cropped refinement
  - *From: brbbbq*

- **Lightning ingredients workflow with new LightX and Pusa**
  - Use case: Fast generation using just new LightX and Pusa LoRAs with Wan I2V base model
  - *From: VRGameDevGirl84(RTX 5090)*

- **I2V + Uni3C with multiple LoRAs**
  - Use case: Creating high quality video with camera motion transfer
  - *From: N0NSens*

- **VACE with Phantom combo**
  - Use case: Getting exact adherence to reference images
  - *From: Guey.KhalaMari*

- **Pusa setup with LightX2V**
  - Use case: Cinematic quality video generation
  - *From: SS*

- **3D scene in Houdini to depth map export**
  - Use case: Controlling camera motion with baked depth maps
  - *From: Quality_Control*

- **Two-pass generation with latent-to-latent**
  - Use case: 4 steps generation + 4 steps refinement at 0.3 denoise for detail enhancement
  - *From: patientx*

- **Image rebatch to T2V with low denoise**
  - Use case: Bringing still images to life without using I2V model
  - *From: hicho*

- **VACE for style transfer and inpainting**
  - Use case: Production style concept work and previsualization
  - *From: Guey.KhalaMari*

- **Using RMBG for auto masking in inpaint**
  - Use case: Automatic hair and face masking for inpainting workflows
  - *From: hicho*

- **VACE and stitching clips for long videos**
  - Use case: Creating extended video sequences
  - *From: Qok*

- **Wan 2.2 with LightX2V LoRA**
  - Use case: Text-to-image single frame generation with 4+4 and 4+8 steps
  - *From: patientx*

- **Low noise as refiner for 2.1**
  - Use case: Retains full LoRA compatibility while using 2.2 features
  - *From: Qok*

- **10 steps low > 2x upscale > 10 steps low**
  - Use case: High resolution generation workflow for 9 MPx
  - *From: 128578659047964672*

- **FFLF (First-Frame-Last-Frame) with 2.2**
  - Use case: Video morphing and extension
  - *From: JmySff*

- **Depth+OpenPose with VACE**
  - Use case: Controlled video generation with reference
  - *From: JmySff*

- **T2V using context windows with 4 different prompts**
  - Use case: Creating 337 frame videos at 24fps
  - *From: Kijai*

- **T2V for original shots then end/start frames with 11-frame overlap**
  - Use case: Creating seamless transitions between video clips
  - *From: ingi // SYSTMS*

- **First/last frame morphing with VACE**
  - Use case: Creating transitions between unrelated shots
  - *From: JmySff*

- **Using both high noise and low noise LoRAs**
  - Use case: Character LoRA implementation requiring both samplers
  - *From: el marzocco*

- **Video upscaling with motion fixing**
  - Use case: Upscale existing videos with optional motion correction using start step control
  - *From: thaakeno*

- **VACE + Wan 2.2 merge for FFLF control**
  - Use case: Better first-frame-last-frame control than standard Wan 2.2 I2V
  - *From: R.*

- **High-res generation pipeline**
  - Use case: Generate 14B at lower res, then upscale with 5B model to avoid block swapping issues
  - *From: Juan Gea*

- **Two-stage high resolution generation**
  - Use case: 14B model at 1600x960, then 5B upscale to 3072x1840 with 0.35 denoise
  - *From: Juan Gea*

- **Multi-sampler CFG scheduling**
  - Use case: Using 3 samplers or CFG schedule node with 2 samplers for better control
  - *From: AshmoTV*

- **VACE frame extension for style transfer**
  - Use case: Generate short stylized sequence, then use those frames to extend longer video maintaining style
  - *From: Zuko*

- **MMaudio V2A integration**
  - Use case: Simple workflow: load video → mmaudio model → vae/encoder/sync models → sampler → save
  - *From: U̷r̷a̷b̷e̷w̷e̷*

- **Mixed composition with VACE/Masking/V2V**
  - Use case: Combining different techniques for complex video compositions
  - *From: vanhex*

- **Deforum + Wan upscaling**
  - Use case: Running old deforum videos through Wan upscale workflow for enhanced results
  - *From: 985830005315633193*

- **Two-pass generation with different denoise levels**
  - Use case: Better quality than default workflow - high_noise model 4 steps, then second pass 0.2 denoise with low_noise model 2-3 steps
  - *From: patientx*

- **T2V with overlapping context windows and multiple prompts**
  - Use case: Creating longer sequences with 20 different prompts
  - *From: kendrick*

- **Three separate renders stitched together**
  - Use case: Alternative to context windows for longer content
  - *From: VK (5080 128gb)*

- **Kontext for editing then I2V**
  - Use case: Remove objects, paste new elements, relight, then animate with Wan
  - *From: A.I.Warper*

- **FFLF with Fun Inpaint 2.2**
  - Use case: First-frame-last-frame morphing with video extension
  - *From: R.*

- **VACE transition workflow**
  - Use case: Creating smooth transitions between shots using 10/29/10 frame splits with gray frames in between, assembled in After Effects
  - *From: ingi // SYSTMS*

- **Hybrid high/low noise sampling**
  - Use case: Use T2V for low noise, can add 3rd sampler with Wan T2V low noise to finish and keep more control
  - *From: Hashu*

- **Small resolution upscaling**
  - Use case: Generate at 512x256 then direct 4x upscale to 2048x1024
  - *From: Fill*

- **Context window for long videos**
  - Use case: Generate videos up to 19 seconds on RTX 5090 with good quality
  - *From: ComfyCod3r*

- **Two-stage upscaling process**
  - Use case: Generate high quality videos from low res generations by upscaling in pixel space then running through low noise model
  - *From: Fill*

- **Fantasy Portrait with Multitalk and context windows**
  - Use case: High quality character videos with improved lip sync using MAGREF checkpoint
  - *From: A.I.Warper*

- **First-Last-Frame animation with multiple tools**
  - Use case: Use Qwen for first image, Kontext for pose changes, then WAN FLF to animate
  - *From: U̷r̷a̷b̷e̷w̷e̷*

- **Extended video generation without context options**
  - Use case: Making very long videos using alternative method
  - *From: xwsswww*

- **Seamless loop workflow for I2V**
  - Use case: Creating looping videos
  - *From: 777222267331543050*

- **Native ComfyUI for Wan 2.2 with upscale/interpolation**
  - Use case: Add sage attention and model patch, then upscale & interpolate separately
  - *From: AiGangster*

- **Fantasy Portrait + Multitalk for lip sync**
  - Use case: Lip synchronization with driving video
  - *From: multiple users*

- **MAGREF + InfiniteTalk**
  - Use case: Lip sync from single image without driving video
  - *From: seitanism*

- **Krea Flux first frame to Wan VACE**
  - Use case: High quality first frame generation then video
  - *From: hicho*

- **Split sigmas with inject latent noise**
  - Use case: T2V generation with different high/low noise expert configurations
  - *From: l҈u҈c҈i҈f҈e҈r҈*

- **VACE/Phantom combination workflow**
  - Use case: Character consistency with style transfer, took hundreds of hours to develop compatibility
  - *From: 88822364468412416*

- **First frame last frame with TouchDesigner**
  - Use case: Beat sync videos by generating 6 videos at 81 frames each and syncing to song mids
  - *From: A.I.Warper*

- **Upscaling/detailer workflow**
  - Use case: Keeps likeness while adding/fixing details and textures, still has tiling issues
  - *From: mono*

- **Endless workflow for Flux/Wan/MMAudio**
  - Use case: Generate image with Flux, six Wan generations, add sound with MMAudio
  - *From: 621093216959201281*

- **Multi-stage upscaling process**
  - Use case: Phantom-vace FFLF 832x480x81 @ 16fps, VACE upscale, character face restoration, Wan22 Low noise upscaler to 1600x900x81, RIFE x3 interpolation to 24fps, standard upscaler to 1080p
  - *From: mdkb*

- **InfiniteTalk with 78 windows for full song**
  - Use case: 5551 frames at 832x480 with 4 steps, completed in 41:52 on 5090
  - *From: Kijai*

- **3 KSampler setup for Pusa**
  - Use case: First pass no lora with cfg 3.5, second with 1.3 strength (cfg 1), third at 1 (cfg 1)
  - *From: asd*

- **Ultimate SD Upscaler for video upscaling**
  - Use case: Resize video with lanczos then feed into Ultimate SD Upscaler with Wan T2V low noise model
  - *From: 153803064858378240*

- **Kijai's InfiniteTalk workflow 1**
  - Use case: Better than MultiTalk for lip sync applications
  - *From: 441459285759754250*

- **Pusa extension workflow for long shots**
  - Use case: Creating extended video sequences with Wan 2.2
  - *From: 391574267306704897*

- **3 Ksampler native mode with lightx2v**
  - Use case: Standard processing with interpolation
  - *From: . Not Really Human :.*

- **Multiple context window loop**
  - Use case: Extended video generation
  - *From: Benjimon*

- **2.2 FLF (First-Last-Frame) workflow**
  - Use case: Smooth transitions between video segments
  - *From: 947112250198618162*

- **Right-click Upscayl integration**
  - Use case: Quick 2x upscaling outside ComfyUI for AMD users
  - *From: patientx*

- **Multi-stage FF-LF generation**
  - Use case: 1+1 good, 1+2 better, 2+2 perfect for video generation using First-Frame-Last-Frame morphing
  - *From: patientx*

- **MagRef-InfiniteTalk Music video creator**
  - Use case: Creating music videos with lip-sync using multiple input images and audio timing
  - *From: VRGameDevGirl84(RTX 5090)*

- **Kijai's I2V with Fun/FL2V flag**
  - Use case: I2V generation with last frame input and FL2V flag enabled in encoder
  - *From: A.I.Warper*

- **Tiled processing for high resolution**
  - Use case: Processing videos at higher resolutions like 4K using tiling approach
  - *From: 153803064858378240*

- **USDU for Wan wrapper upscaling**
  - Use case: Upscaling videos with tiling to avoid OOM, includes context window support
  - *From: 153803064858378240*

- **HuMo endless workflow**
  - Use case: One-shot generation with reference image and prompt per 3-second shot, combines into single video
  - *From: VRGameDevGirl84(RTX 5090)*

- **Audio source separation pipeline**
  - Use case: Use UVR5 to separate vocals, generate video with clean audio, then recombine with original soundtrack
  - *From: U̷r̷a̷b̷e̷w̷e̷*

- **Multi-character lip sync editing**
  - Use case: Split audio into parts, run different images with InfiniteTalk, then edit together in video editor
  - *From: JohnDopamine*

- **VACE with pose control**
  - Use case: Use VACE 2.2 with open pose but without face detect to avoid messy dots, then apply InfiniteTalk
  - *From: 𝕯𝖗. 𝕸𝖆𝖈𝖆𝖇𝖗𝖊 ☠*

- **Background V2V with character I2V compositing**
  - Use case: Create background with Wan V2V, characters with Wan I2V on greenscreen, composite in After Effects
  - *From: VK (5080 128gb)*

- **VACE 2.2 video extension with context windows**
  - Use case: Extending videos beyond 81 frames without quality degradation using 10-frame overlaps and blending
  - *From: Vérole*

- **First-Frame-Last-Frame with controlnet guidance**
  - Use case: Maintaining structure and pose consistency through video generation using pose and depth maps
  - *From: mdkb*

- **Humo long generation workflow**
  - Use case: Creating full music videos with automatic LLM prompt generation every 5 seconds
  - *From: VRGameDevGirl84(RTX 5090)*

- **3-pass WAN 2.2 I2V with MMAudio and Ace-Step**
  - Use case: High-quality video generation with multiple processing passes and audio integration
  - *From: 132313738710614016*

- **Auto-indexing and combining videos for any length**
  - Use case: Queue up as many times as needed for song length, auto indexes and combines created videos
  - *From: VRGameDevGirl84(RTX 5090)*

- **LLM-generated prompts from lyrics**
  - Use case: Song split into 3s chunks, lyrics transcribed, fed to LLM to generate scene prompts for one-shot auto-vid
  - *From: 1348584179440418868*

- **LLM prompt generation every 5 seconds**
  - Use case: Using Florence and Groq with last frame + last prompt + 5 randomized words
  - *From: JohnDopamine*

- **Background-only reference workflow**
  - Use case: Workflow that applies reference image only to background, keeping subject unchanged
  - *From: 𝕯𝖗. 𝕸𝖆𝖈𝖆𝖇𝖗𝖊 ☠*

- **Video upscaling workflow shared**
  - Use case: For upscaling wan/video generations
  - *From: 153803064858378240*

- **Basic I2V workflow with dozens of short clips**
  - Use case: Making selections and choices while building longer content
  - *From: Rävlik*

- **Using Fun-inp and Fun-vace with InfiniteTalk**
  - Use case: Creating smooth transitions and extending clips
  - *From: Rävlik*

- **Humo two-generation extension**
  - Use case: First generation conditioned from reference, second uses last frame of first as starting frame in I2V mode
  - *From: Ablejones*

- **V2V with different prompts**
  - Use case: Get exactly what you prompt but with motion of original video, easy with more control and no controlnet
  - *From: hicho*

- **Style transfer with video blending**
  - Use case: Blending input video with liquid fx video for control input in VACE
  - *From: Dkamacho*

- **3-Sampler setup for better motion**
  - Use case: First sampler at 4 steps to establish motion, then regular settings on other two samplers
  - *From: garbus*

- **Wan Alpha for transparent video creation**
  - Use case: Generate transparent background videos for compositing with stock footage
  - *From: U̷r̷a̷b̷e̷w̷e̷*

- **VACE 2.2 transitions**
  - Use case: Multiple T2V videos combined using Vace with multiple frames as start/end frames
  - *From: ingi // SYSTMS*

- **HuMo Music video creator**
  - Use case: Totally automated workflow - upload image and song, enter file path and run. 3.5 min song took 40 mins
  - *From: VRGameDevGirl84(RTX 5090)*

- **3 sampler setup with 2+2 steps**
  - Use case: More cinematic T2V results - first sampler 3-4 steps with no LoRA and CFG 3.5, then standard 2+2 dyno setup
  - *From: garbus*

- **HuMo automated lip-sync workflow**
  - Use case: Automated process for generating lip-synced videos from audio input using LLM prompts
  - *From: VRGameDevGirl*

- **WanAnimate with SAM masking**
  - Use case: Character replacement in dance/motion videos using Kijai's example workflow with SAM masking
  - *From: A.I.Warper*

- **Multiple image anchors using FLF stitching**
  - Use case: Using 3 image anchors for better control over video generation
  - *From: pom*

- **T2V V2V with messed up background edit**
  - Use case: When passing to V2V, lighting will be corrected, using Florence for better prompts
  - *From: hicho*

- **Qwen text to image then Wan I2V pipeline**
  - Use case: Two-stage process for better control
  - *From: The Coin Hunter*

- **I2V then smooth travel for continuous sequences**
  - Use case: Creating longer video sequences with last frame to first frame transitions
  - *From: 𝕯𝖗. 𝕸𝖆𝖈𝖆𝖇𝖗𝖊 ☠*

- **OVI + Depth control using 5B controlnet**
  - Use case: Enhanced control with HED and Canny options available
  - *From: Hashu*

- **Manual I2V chaining with upscaling**
  - Use case: Creating longer consistent video sequences by upscaling last frames and feeding back as first frames
  - *From: The Coin Hunter*

- **3D model + controlnet approach**
  - Use case: Use Hunyuan 3D and Blender to create 3D scenes, animate camera, then use depth/pose controlnet to drive AI video generation for precise camera angles
  - *From: mdkb*

- **Automated music video generation**
  - Use case: LLM-driven prompts based on lyrics with automated queuing system for multiple scene generation
  - *From: VRGameDevGirl84(RTX 5090)*

- **VACE 2.2 with masking and LoRAs**
  - Use case: Object/character replacement using modified workflow with masking support
  - *From: Dream Making*

- **Video continuation using last frame extraction**
  - Use case: Creating seamless follow-up clips by extracting last frame for next generation input
  - *From: 𝕯𝖗. 𝕸𝖆𝖈𝖆𝖇𝖗𝖊 ☠*

- **Multi-stage video creation with multiple models**
  - Use case: Train loras + 2x Wan 2.2 videos + VACE transition + VibeVoice + Infinite Talk for complete production
  - *From: Dever*

- **Batch queue system for long videos**
  - Use case: Send 20 prompts in queue, Comfy generates from last frame, assemble in Premiere
  - *From: Dream Making*

- **3D to 2D pipeline using Hunyuan 3D and Blender**
  - Use case: Generate 3D models, animate in Blender for camera positions, then use VACE for character insertion
  - *From: mdkb*

- **FFLF (First Frame Last Frame) chained approach**
  - Use case: Creating longer videos with style consistency, avoiding style weakening
  - *From: The Shadow (NYC)*

- **SVI with multiple extensions using variables**
  - Use case: Creating extended video sequences
  - *From: Vérole*

- **Automated looping workflow with cycle nodes**
  - Use case: Queuing multiple clips automatically with global vars like start image and count
  - *From: reallybigname*

- **Two-stage process for complex scenes**
  - Use case: First make clip with Wan 2.2, then feed as guide to remake with Wan 2.1 + SVI
  - *From: Ablejones*

- **Full auto I2V with AI decision making**
  - Use case: Let Qwen 2.5 VL 7b decide what happens next with system prompt
  - *From: Vérole*

- **HuMo with SVI extension**
  - Use case: Solving HuMo's 4 second clip limit for longer generations
  - *From: Ablejones*

- **Flux Krea w/ pullid ==> WanS2v ==> Qwen 2509 ==> Wan Animate 2.2**
  - Use case: Complete generation pipeline
  - *From: Zlikwid*

- **Qwen edit + cinematic hard cut lora + Wan2.2 i2v first FFLF**
  - Use case: Creating hard cuts in video
  - *From: Ablejones*

- **Using final frame node to save last frame for I2V editing**
  - Use case: Iterative video editing
  - *From: hicho*

- **HuMo with I2V workflow**
  - Use case: Audio-reactive video with I2V
  - *From: Ablejones*

- **Multi-act FFLF workflow for longer content**
  - Use case: Creating longer sequences with scene transitions using first-frame-last-frame chaining
  - *From: patientx*

- **Holocine T2V high + 2.2 low upscaling**
  - Use case: Generate with Holocine T2V high model then split and upscale using 2.2 low for 15 second stories
  - *From: Daviejg*

- **Florence 2 segmentation with Vace transitions**
  - Use case: Using Florence 2 nodes for region_proposal and referring_expression_segmentation, then adding transitions with Vace
  - *From: ingi // SYSTMS*

- **Upscaling passes for video smoothing**
  - Use case: Upscale video slightly (1.25x) and run additional passes to smooth out video and add details each pass
  - *From: JohnDopamine*

- **MJ images + Vace transitions for storytelling**
  - Use case: Transition-focused storytelling using Midjourney shots with Vace for seamless transitions
  - *From: ingi // SYSTMS*

- **Wan 2.1 Endless with custom LoRAs to Wan 2.2 V2V upscale**
  - Use case: Using Zlikwid LoRA and AnimateDiff LoRA in Wan 2.1 then upscaling with Wan 2.2
  - *From: Zlikwid*

- **Z-image + Wan I2V using end image instead of start**
  - Use case: Using Z-image for generation then Wan I2V with the image as end frame instead of start frame
  - *From: AshmoTV*

- **Vace 2.2 HN to Vace 2.1 Phantom with dual masking**
  - Use case: Using both Vace masking and latent noise masking with custom projection to prevent ghosting
  - *From: Ablejones*

- **Z-image + WAN FFLF workflow for embroidery animations**
  - Use case: Creating embroidery formation animations using end image guidance
  - *From: AshmoTV*

- **Multi-keyframe timeline with 3 sampler setup**
  - Use case: Dynamic movement generation using first pass sampler without speedup LoRA
  - *From: Chandler*

- **SVI 2.2 with Hard Cut LoRA**
  - Use case: Creating videos that can cut back to same scenes with proper padding frames
  - *From: Ablejones*

- **VACE with context windows**
  - Use case: Long form video generation with different prompts for background changes
  - *From: Ablejones*

- **V2V using T2V model with input video and start step of 2 instead of 0**
  - Use case: Easy video-to-video conversion that respects prompt and keeps motion
  - *From: hicho*

- **VACE for first half of sampling, HuMo for second half**
  - Use case: Creating morphing transitions between subjects
  - *From: Ablejones*

- **Two pass process: 1) WanAnimate w/ Uni3C 2) Extract Depth using VDA 3) ReRun with VACE and Context Windows**
  - Use case: Creating long consistent generations with depth control
  - *From: NebSH*

- **Automated FMML/Humo workflow using ChatGPT for JSON prompts and ZImage for frame generation**
  - Use case: Fully automated video generation based on audio and themes
  - *From: VRGameDevGirl84(RTX 5090)*

- **VACE context windows with different references for each window through conditionings**
  - Use case: Directed context window travel for consistent character morphing
  - *From: Ablejones*

- **Audio reactive video generation using WanSoundTrajectory**
  - Use case: Creating videos that respond to audio input with movement
  - *From: Ablejones*

- **VACE clip joiner workflow**
  - Use case: Seamlessly joining video clips with subtle transitions
  - *From: Vérole*

- **Context windows with reference injection**
  - Use case: Morphing between different concepts using context windows
  - *From: Ablejones*

- **First frame editing + VACE generation**
  - Use case: Better object animation by editing first frame instead of using reference images
  - *From: Ablejones*

- **SVI Pro + HuMo pipeline**
  - Use case: High quality video generation with good lip sync
  - *From: Ablejones*

- **HuMo + Wan A14B workflow**
  - Use case: Audio-reactive video generation with reference matching and prompt matching capabilities
  - *From: Ablejones*

- **SVI extension workflow with changing anchor images**
  - Use case: Building longer videos in 4s chunks, each chunk has its own prompt, video can keep getting longer
  - *From: 152993277631528960*

- **Automated HuMo workflow with prompt generation**
  - Use case: Creates prompts automatically from audio file and lyrics, only need to paste prompts and upload audio
  - *From: VRGameDevGirl84(RTX 5090)*

- **LTX to Wan v2v enhancement**
  - Use case: Skip LTX2 second stage, use Wan for v2v enhancement instead for better detail
  - *From: hicho*

- **Background replacement using Wan 2.1 VACE**
  - Use case: Replacing video backgrounds while keeping subjects, using QIE 2511 for reference image creation
  - *From: Albert*

- **Resampling old AnimateDiff with Wan**
  - Use case: Upscaling and improving quality of old AnimateDiff generations
  - *From: brbbbq*

- **LTX2 to Wan v2v pipeline**
  - Use case: Using LTX2 then Wan v2v for upscaling existing videos
  - *From: hicho*


## Recommended Settings

- **Steps for 1.3B model**: 50 steps
  - Significantly reduces artifacts compared to lower step counts
  - *From: DiXiao*

- **Shift parameter**: 4
  - Improves quality with flow matching models
  - *From: spacepxl*

- **V2V noise strength for upscaling**: 0.05
  - Maintains similarity to original while upscaling resolution
  - *From: DiXiao*

- **Block swap for 48GB VRAM**: 0
  - Much faster inference with sufficient VRAM
  - *From: Juampab12*

- **Scheduler recommendation**: DPM++ SDE
  - Better results than standard DPM++ for some cases
  - *From: Screeb*

- **Steps and flowshift**: 20 steps with flowshift of 2
  - Dramatically improves I2V quality
  - *From: Faust-SiN*

- **I2V resolution and steps**: 30 steps at 16:9 (720p)
  - Good quality results
  - *From: A.I.Warper*

- **High quality generation**: 50 steps fp8
  - Reduces dot artifacts compared to low steps and quants
  - *From: Juampab12*

- **cfg_end parameter**: 0.8
  - Saves render time without significant quality loss
  - *From: JmySff*

- **TeaCache rel_l1_thresh**: 0.040
  - Good balance for quality vs speed
  - *From: DiXiao*

- **TeaCache start_step**: 10
  - Optimal starting point for caching
  - *From: DiXiao*

- **CFG**: 6.0
  - Standard CFG setting for Wan
  - *From: DiXiao*

- **Shift**: 5.0
  - Standard shift parameter
  - *From: DiXiao*

- **Scheduler**: unipc
  - Produces clearest hair detail
  - *From: DiXiao*

- **Context window size**: 81
  - Used with overlap 16 for sliding context
  - *From: Kijai*

- **Context overlap**: 16
  - Works with window size 81 for smooth transitions
  - *From: Kijai*

- **Resolution for 9:16**: 720 width
  - Better results than default 768x768
  - *From: ShiftingDimensionsAI*

- **TEACache**: 0.25 or lower
  - Values above 0.4 cause quality degradation
  - *From: c1t1zen1*

- **Steps for 1.3B model**: 50+ steps
  - Needed to get good detail quality that can compete with 14B
  - *From: spacepxl*

- **Resolution for 480p model**: 832x480
  - Native resolution works best
  - *From: burgstall*

- **H100 optimization**: fp8_e4m3fn + torch compile + tea cache
  - Reduced time from 2761s to 1515s
  - *From: ingi // SYSTMS*

- **TeaCache**: 0.4
  - User was testing but found it may be too high
  - *From: BestWind*

- **blocks_to_swap**: 10
  - Good balance for 3090 users to avoid OOM while maintaining speed
  - *From: Fred*

- **Sampler/Scheduler**: unipc sampler, 5 shift 6 cfg, 30 steps
  - Standard settings used by Zuko for effect LoRAs
  - *From: Zuko*

- **Model precision**: fp16_fast with nightly torch
  - Provides speed improvements on compatible hardware
  - *From: BestWind*

- **Low resolution generation**: 480w x 272h
  - For faster generation times while testing
  - *From: ZombieMatrix*

- **Steps for I2V**: 8 steps with GGUF 8 480p
  - Faster inference - 300 seconds for 5 seconds output
  - *From: AJO*

- **Lora strength for aging effects**: 0.6 works well, 0.3 makes video very still
  - Balance between effect and motion
  - *From: NebSH*

- **Context window for looping**: 169 total frames, 81 context window, 16 overlap, uniform_looped
  - Better loop quality than loop-args
  - *From: Kijai*

- **Lora training resolution**: 1280x720 with frame buckets set to 73 maximum
  - Good generalization for concept loras
  - *From: Kytra*

- **Native high resolution**: 1920x1072 latent size
  - Direct high-res generation without upscaling
  - *From: Benjaminimal*

- **Frame count for character lora**: 65 frames
  - Good balance of length and quality for 1280x720 generations
  - *From: Kytra*

- **Step count for high quality**: 50+ steps
  - Necessary for good quality at 1280x720 resolution, especially with loras
  - *From: Kytra*

- **Training epochs for concept loras**: 6 epochs
  - Sufficient for learning concepts with 80+ videos across 8xH100s
  - *From: Kytra*

- **Frame buckets for training**: [1,33,73]
  - Used for traveling lora training with distinct captioning paradigm
  - *From: Kytra*

- **Resolution for low VRAM**: 544x304
  - I2V still looks decent at this low resolution
  - *From: garbus*

- **Blockswap setting for 14B on 40GB**: 40
  - Allows 14B 720p generation but may affect quality
  - *From: Jas*

- **CFG for I2V troubleshooting**: 5-6
  - Higher values can cause overcooking and high contrast artifacts
  - *From: Ghost*

- **Steps for clean renders**: 30-40 steps
  - 20 steps is too light and causes sampling issues/grain
  - *From: Clownshark Batwing*

- **Control LoRA blend ratio**: 80% depth map, 20% grayscale original
  - Produces best results from control lora
  - *From: Kytra*

- **Preferred resolution for 14B model**: 1280x720
  - Optimal if setup can handle it
  - *From: garbus*

- **Steps**: 8 steps for basic, 20 for higher quality
  - Good balance of speed vs quality
  - *From: AJO*

- **Resolution**: 1024x1024x33 frames
  - Good results with 1.3B model
  - *From: ZombieMatrix*

- **CFG**: 6.5
  - Used in 55 minute render on RTX3090
  - *From: Level Higher*

- **Steps**: 25 steps
  - For 10 second video, high quality output
  - *From: Level Higher*

- **Fun InP frames**: 10 steps
  - Works well with 1.3 Fun I2V model
  - *From: VK (5080 128gb)*

- **Resolution and frame parameters**: 480x864, 75 steps, 4 seconds video, 81 frames, 20 FPS
  - Closest to 9x16 aspect ratio for YouTube shorts with high quality realistic results
  - *From: Level Higher*

- **Denoise levels for guide mode**: 0.35 denoise for following light behavior, 0.6 denoise reduces prompt following
  - Lower denoise follows the guide image more closely
  - *From: TK_999*

- **CFG and shift values**: CFG 4-4.5, shift 5
  - Better results than higher CFG values
  - *From: ingi // SYSTMS*

- **Tea cache retention**: 0.15 with FETA enhance-a-video
  - Light tea cache setting for enhanced video processing
  - *From: ingi // SYSTMS*

- **VACE encoder strength**: 0.5-0.6
  - Achieves good results
  - *From: TimHannan*

- **Learning rate for LoRA training**: 2e-4
  - Faster training, completed overnight
  - *From: 88822364468412416*

- **MPS LoRA strength**: 0.7
  - Good maintenance of reference style with 14B fun control
  - *From: DawnII*

- **Generation parameters for optimized inference**: 640×480×81 frames in 5 minutes on RTX 3090
  - Using optimizations in Kijai's T2V workflow
  - *From: seruva19*

- **Steps for video generation**: 20 steps typically, 30 for complex scenes
  - Balance between quality and generation time
  - *From: Clownshark Batwing*

- **Steps for LoRA training**: 6,000 steps
  - For explosion style LoRA
  - *From: ingi // SYSTMS*

- **Optimal step range**: 50-75 steps
  - Gold spot for quality, only for crowded/dynamic scenes
  - *From: Level Higher*

- **Low denoise pass strength**: 0.4 to 0.6
  - For cleaning up VACE output
  - *From: 88822364468412416*

- **Frame count**: 81 or 101 frames, 121 for complex prompts
  - Good balance for animation length and complexity
  - *From: Level Higher*

- **Steps for quality**: 75 steps with TeaCache
  - Provides good quality, around 25 minutes render time on RTX 3090
  - *From: Level Higher*

- **Steps for wide resolutions**: 30 steps with TeaCache
  - 100+ steps cause artifacts at high/wide resolutions
  - *From: ZombieMatrix*

- **TeaCache for highest quality**: Turn off
  - Disabling gives highest quality output
  - *From: DawnII*

- **Block swap for 14B DF**: 38 or higher
  - Required to fit 14B SkyReels DF model on 16GB VRAM
  - *From: Ablejones*

- **Frame overlap**: 17 frames
  - Default recommended value, reducing overlap can cause more degradation
  - *From: Kijai*

- **Steps for res_3m**: 20 steps
  - Produces good results, tried 50 for unipc and wasn't much better
  - *From: Clownshark Batwing*

- **CFG**: 6.5
  - Makes model listen to prompt well, good for dynamic motion with UniPC over Euler
  - *From: Level Higher*

- **GPU temperature safety**: Below 95°C tjunction
  - Safety limit for RTX 3090 non-ti tjunction hot spot temperature
  - *From: Benjimon*

- **LoRA strength for 2D FX**: 0.8 or higher
  - Lower than 0.8 makes everything 2D instead of just adding effects
  - *From: ingi // SYSTMS*

- **CFG**: 2-4
  - Used for good quality generations
  - *From: 88822364468412416*

- **Steps with TeaCache**: 20 steps
  - Reduces time dramatically while maintaining quality
  - *From: 🏁🫰GridSnap*

- **Resolution dependency on length**: 576p max without block swapping on 5090
  - Resolution is dependent on video length
  - *From: 88822364468412416*

- **SLG blocks**: 8-9
  - Better than 10 blocks in most cases
  - *From: ezMan*

- **DF frame counts**: 97 frames take around 7 minutes
  - On slower cards for DF workflow
  - *From: Cseti*

- **Speed-optimized parameters**: fp8_e52m checkpoint + torch.compile + sageattention 2 + teacache (0.250/6) + enhance-a-video + fp16_fast + slg (9, 0.2/0.8) + unipc + 20 steps + cfg 6 + shift 7
  - For speed-optimized output while maintaining quality
  - *From: seruva19*

- **LoRA blending**: Two nodes set to 0.75 with all blocks enabled
  - Effective blending of multiple LoRAs in Wan
  - *From: ingi // SYSTMS*

- **VACE frame overlap**: 21 frames overlap for 60 frame generation, 41 frames for more consistency
  - Better movement consistency in extended videos
  - *From: DiXiao*

- **CausVid CFG**: 1.0
  - CFG distilled model
  - *From: yi*

- **CausVid steps**: 4
  - Instead of usual 30 steps
  - *From: yi*

- **Teacache model shift**: 3.0
  - Used with steps skip 3, UniPC, 75 steps for higher quality
  - *From: Level Higher*

- **Guide weights for epsilon mode**: 0.5, 0.4, 0.3, 0.2
  - Different strengths for latent guide control
  - *From: Ablejones*

- **VACE strength with CausVid**: 0.5 to 1.2
  - 0.5 for subtler effects, 1.2 for stronger
  - *From: DawnII*

- **CausVid LoRA strength**: 0.5
  - Used with 14B + 5 steps for good results
  - *From: DiXiao*

- **CausVid LoRA strength for 1.3B**: 0.8
  - 4 steps, CFG 1, for 10 seconds in 40 seconds generation
  - *From: Vérole*

- **Context chunks**: 81 frames (default)
  - Default setting works well for long video generation
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Steps with VACE + CausVid**: 8-9 steps
  - Good balance of quality and speed
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Inpainting mask fill**: Gray (127)
  - Required for VACE inpainting to work properly
  - *From: ˗ˏˋ⚡ˎˊ-*

- **CausVid LoRA strength**: 0.3
  - Works well with VACE Skyreel, fewer defects
  - *From: Vérole*

- **VACE steps**: 8
  - Better quality than default 6 steps with Skyreel
  - *From: Vérole*

- **Phantom settings**: 0.76 strength, 12 steps, cfg 1, shift 6, unipc
  - Good quality with CausVid LoRA
  - *From: HeadOfOliver*

- **Context window**: 65 frames
  - Used with 272 frame generation
  - *From: Kendo*

- **FETA weight**: 0.7 start 0.2 end 0.8
  - Good balance for VACE control
  - *From: Kendo*

- **CFG and steps for merged speed model**: CFG 1, 5-7 steps
  - Optimal settings for model with merged speed LoRAs
  - *From: JohnDopamine*

- **CausVid V2 with higher CFG**: CFG 2 with CausVid V2
  - CFG 1 led to less movement, CFG 2 provides enough motion without negative effects
  - *From: DevouredBeef*

- **Context window optimization**: 49 frame context with 16 overlap
  - Better style preservation than 81 frames for abstract styles
  - *From: Zlikwid*

- **Split sampling CFG**: First step CFG 3-5, remaining steps CFG 1
  - Prevents burn while maintaining quality with CausVid
  - *From: phazei*

- **Optimal 3-step settings**: CausVid 0.5, AccVid 2.0, MPS 1.0
  - Balanced settings for 3-step generation with good quality
  - *From: Jonathan*

- **Resolution**: 1024x576
  - Sweet spot for RTX 4080, higher resolution than lower res options
  - *From: CaptHook*

- **Shift parameter**: 1 for realism, 3+ for stylized
  - Controls output style - lower for natural look, higher for artistic
  - *From: VRGameDevGirl84(RTX 5090)*

- **AccVid I2V LoRA strength**: 2.0
  - Great middle ground, stable at higher strengths compared to T2V variant
  - *From: Jonathan*

- **CausVid LoRA strength**: 0.5
  - Part of optimal low-step combination
  - *From: Jonathan*

- **Steps**: 8-10 steps
  - Good balance of quality and speed
  - *From: VRGameDevGirl84(RTX 5090)*

- **Scheduler**: UniPC
  - Gives more natural look compared to DPM++ variants
  - *From: VRGameDevGirl84(RTX 5090)*

- **Denoiser strength for V2V**: 0.75
  - Better motion results than lower values
  - *From: hicho*

- **FusionX merge runs in as little as 8 steps**: 8 steps or even lower
  - Merge eliminates need for LoRAs
  - *From: VRGameDevGirl84(RTX 5090)*

- **Detail LoRAs in merge at 0.4 strength**: 0.4
  - Allows adding more LoRAs for extra enhancement if needed
  - *From: VRGameDevGirl84(RTX 5090)*

- **Shift sensitivity testing from 1 to 11**: 1-11
  - Testing theory that one LoRA locks shift while another creates sensitivity
  - *From: The Dude*

- **Shift value of 2.76 for better VACE reference similarity**: 2.76
  - Helps override depth control and maintain outfit/hairstyle
  - *From: MysteryShack*

- **Shift for I2V**: At least 2, start with 2 and go up by 1
  - Shift 1 might cause burn-in effects and artifacts
  - *From: VRGameDevGirl84(RTX 5090)*

- **CFG for CausVid**: 1
  - Standard setting when using CausVid LoRA
  - *From: patientx*

- **Steps with CausVid**: 4-8 steps
  - CausVid allows very low step counts with good quality
  - *From: The Dude*

- **CaptHook's favorite settings**: 1024x576, 81f, 8 steps, shift 1, Uni-pc, blocks 40,15, 512sec
  - Tested combination that works well on 4080 16gb
  - *From: CaptHook*

- **I2V steps**: 20 steps, maybe 25-30 for high quality
  - Most I2V generations work fine at these step counts
  - *From: izashin*

- **Steps for Self-Forcing**: 4-8 steps
  - Fast generation while maintaining quality
  - *From: hicho*

- **Shift value for VACE realism**: 1 for realistic but static, 5 for natural motion
  - Controls balance between realism and motion
  - *From: ingi // SYSTMS*

- **VACE camera control end percentage with Phantom**: 0.05
  - Prevents distortion and glitches when combining VACE and Phantom
  - *From: Guey.KhalaMari*

- **VACE strength with Phantom**: 0.9
  - Works well with low camera control percentage
  - *From: Guey.KhalaMari*

- **Frame limit for standard Wan**: 81 frames max
  - Model trained on 5 second videos
  - *From: patientx*

- **Quantization for RTX 3090**: fp8_e5m2
  - Supported format for this architecture
  - *From: Guey.KhalaMari*

- **Vace strength**: 0.75
  - Otherwise it stuck to the pose too much
  - *From: ingi // SYSTMS*

- **LightXv2 steps for blotch removal**: 6 steps
  - Blotches seem completely gone
  - *From: Thom293*

- **Self Forcing LoRA weight**: 1.0
  - Adds or extends motion
  - *From: patientx*

- **New distillation settings**: 4-6 steps, lcm or dpm++_sde scheduler, shift of around 5-6 for vace
  - What we've worked out so far
  - *From: MysteryShack*

- **Resolution preference**: 1536x896
  - My go to resolution
  - *From: HeadOfOliver*

- **LightXv2 settings**: 720x1280, 113 frames, 5 steps, cfg 1, sampler lcm, scheduler simple
  - Working configuration
  - *From: Gateway {Dreaming Computers}*

- **Vace DepthV2 settings**: 1024x576, 4 steps, shift 2, Realism 0.3, AccVid 0.5, CausVid 0.4
  - Working configuration
  - *From: CaptHook*

- **AniWan step count**: 20-30 steps
  - 8 is too low for the regular model
  - *From: TK_999*

- **Context frames**: 81 frames
  - Standard chunk size for long video generation
  - *From: Yae*

- **Steps for FusionX with LightX**: 4 steps
  - Way faster than 10 steps, quality slightly different but still good
  - *From: VRGameDevGirl84(RTX 5090)*

- **FusionX optimal settings**: 8 steps, 1 CFG, 1 Shift
  - Good balance of quality and speed
  - *From: Dream Making*

- **Audio gain for Multitalk**: 3 (from default 1)
  - Improves pronunciation of difficult words
  - *From: Thom293*

- **FPS for lip sync**: 30 or 60 fps
  - Higher FPS helps with word pronunciation, especially rap music
  - *From: patientx*

- **Denoise for upscaling**: Under 0.7
  - Keeps original input intact when not using prompt for creative upscaling
  - *From: VRGameDevGirl84(RTX 5090)*

- **LiveWallpaper LoRA strength**: Low strength
  - Stops anime character endless talking without major quality impact
  - *From: Yae*

- **ControlNet strength**: 40% vs 100%
  - Lower strength (40%) looks much better for character consistency
  - *From: Thom293*

- **Denoise**: 0.5
  - For 1080p rendering
  - *From: notid*

- **Steps with LightX2V**: 4 steps
  - Way faster than other configurations
  - *From: VRGameDevGirl84(RTX 5090)*

- **Causvid strength**: 0.5-0.6
  - For maximum quality with 4 steps
  - *From: Jonathan*

- **Accvid strength**: 2.0
  - High strength fixes causvid's motion degradation
  - *From: Jonathan*

- **MPS strength**: 0.8
  - For 4-step generation
  - *From: Jonathan*

- **Shift**: 1-2
  - Shift 4+ greatly degrades motion
  - *From: Jonathan*

- **CFG**: 1
  - For low VRAM 4GB setup
  - *From: AiGangster*

- **Sampler**: LCM simple
  - For 4-6 step counts
  - *From: Thom293*

- **VACE samples**: At least 4
  - Too low samples (less than 4) gives mixed results
  - *From: Guey.KhalaMari*

- **CFG and Shift**: CFG: 1, Shift: 1
  - Working configuration shared
  - *From: AiGangster*

- **Video2video denoiser**: 0.50
  - For real video input with depth control
  - *From: hicho*

- **Native workflow generation time**: 59.58 seconds
  - Fast execution time achieved
  - *From: VRGameDevGirl84(RTX 5090)*

- **MultiTalk V2V denoise**: 0.7 denoise
  - For lip sync quality
  - *From: AJO*

- **LightXv2 and AccVid LoRA weight**: 50%
  - Better performance for fast motion when combined with disabling MPS LoRA
  - *From: Todd*

- **Steps for fast motion with LoRAs**: 20+ steps
  - Improves results when dealing with fast movement and artifacts
  - *From: Todd*

- **Frame count for 12GB VRAM**: 17 frames
  - Maintains quality better than 81 frames on limited VRAM
  - *From: mdkb*

- **Resolution and frames for low VRAM**: 512 resolution, 33 frames, under 5 minutes generation time
  - Efficient generation on limited hardware
  - *From: hicho*

- **Steps for good quality**: 8 steps at 1024x1536
  - Good quality without upscaling needed
  - *From: patientx*

- **GGUF 2-step generation**: Q4 KS, 2 steps
  - Very fast generation with acceptable quality
  - *From: hicho*

- **Denoise for creative freedom**: First pass .65 denoise, second pass .95 denoise
  - Low denoise adds creative elements, high denoise preserves quality
  - *From: T2 (RTX6000Pro)*

- **FaceNaturalizer LoRA strength**: 0.7
  - Good face enhancement without over-processing
  - *From: patientx*

- **Steps for FusionX**: 4 steps with res_2s and bong tangent
  - Optimal performance for FusionX model
  - *From: l҈u҈c҈i҈f҈e҈r҈*

- **Steps for T2I**: 8 steps
  - Optimal for image generation
  - *From: N0NSens*

- **Denoise for I2I editing**: 0.50 or as low as 0.01
  - Lower values give more control and semi-real look
  - *From: hicho*

- **LightX LoRA strength**: Less than 1.0
  - Better motion, prompt adherence, prevents over-beautifying
  - *From: garbus*

- **VACE I2V scheduler**: dpmpp_sde with shift around 1.5
  - Works well for normal VACE/VACE I2V
  - *From: Atlas*

- **ATI I2V scheduler**: flowmatch_causvid with shift at 5
  - Required for Wan2_1-I2V-ATI-14B model
  - *From: Atlas*

- **FPS for fast motion**: 30 instead of base 16
  - Handles fast motion very well
  - *From: Nekodificador*

- **FusionX video steps**: 10 steps at 720p
  - Used for 3D biped animation workflow
  - *From: Duranovsky*

- **CFG and steps with LightX2V**: CFG 1, steps 4
  - For speed optimization
  - *From: Gateway {Dreaming Computers}*

- **LightX LoRA strength for batching**: 0.5
  - Prevents cross-batch degradation over time
  - *From: A.I.Warper*

- **VACE mask expand**: 20 with no blur
  - Better mask control without artifacts
  - *From: Sal TK FX*

- **FaceNaturalizer LoRA strength**: 0.7
  - Used consistently in patientx's workflow
  - *From: patientx*

- **High quality character replacement settings**: 12 steps, CFG 1.0, unic_pc, normal
  - Settings from successful character replacement workflow
  - *From: brbbbq*

- **Uni3C strength**: 0.5
  - Prevents killing the prompt while maintaining motion transfer
  - *From: hicho*

- **Radial attention steps**: 3 steps at level 2
  - Fixes floor crack movement and zoom/morph issues
  - *From: hicho*

- **VACE strength**: 1.0 (dentist setting)
  - Proper inpainting with middle gray mask areas
  - *From: Neex*

- **Duration frames**: 121 to 181 frames possible
  - Extended duration without context windows, hardware dependent
  - *From: Guey.KhalaMari*

- **Denoise for image-to-image**: Less than 0.70
  - Higher values produce full T2I instead of I2I
  - *From: hicho*

- **Two-pass denoise**: 0.3
  - For latent-to-latent second pass without upscale
  - *From: patientx*

- **CFG for Fast Wan 1.3B**: 1
  - Model designed to run with CFG 1
  - *From: l҈u҈c҈i҈f҈e҈r҈*

- **Step configuration preference**: 4+8 instead of 8+4
  - Produces more natural results, less oversaturated
  - *From: patientx*

- **LightX2V recommended shift**: 5
  - Official recommendation for LightX_V2
  - *From: Dita*

- **Fastwan recommended shift**: 3
  - Recommended setting for Fastwan
  - *From: Dita*

- **LoRA strength for merged model**: 80%
  - Used for comparing normal merge vs LoRAs
  - *From: patientx*

- **LightX2V strength**: 3
  - Effective strength for both samplers
  - *From: 138234075931475968*

- **Blockswap**: 20
  - Stock setting in Kijai workflow
  - *From: Janosch Simon*

- **Resolution**: 960x540
  - Optimal for 4090, 88 seconds generation time
  - *From: Janosch Simon*

- **Steps for I2V**: 7 steps
  - Effective for detailed I2V generation
  - *From: JmySff*

- **Prompt weight limits**: 3 max, 4 causes problems
  - T5 model weight limits
  - *From: Rainsmellsnice*

- **Lightx2v strength**: 3.0 high noise, 1.5 low noise
  - For good motion with reduced steps
  - *From: Juan Gea*

- **Steps configuration**: 4 steps (2/2)
  - With Lightx2v for fast generation
  - *From: Juan Gea*

- **Scheduler**: lcm
  - Works well with beta57 sampler
  - *From: Juan Gea*

- **CFG values**: CFG 1 or 3 for high noise at 3 steps, CFG varies
  - Testing different configurations for optimal results
  - *From: DawnII*

- **LoRA strengths**: High noise 3.0, low noise 1.0 for lightx2v
  - Standard configuration for T2V
  - *From: N0NSens*

- **Steps for high/low**: 3 high without lightx2v cfg 3, 3 high with lightx2v at 3 cfg 1, 3 low lightx2v 1 cfg 1
  - 9 total steps seems to be sweet spot
  - *From: AshmoTV*

- **Frame count**: 640x512x361 frames with RadialAttn, 8+12 steps CFG 1
  - For longer generations on powerful hardware
  - *From: 128578659047964672*

- **Steps split**: 8 steps 3-5 split or 15 steps of 20 on high model then 5 left on low
  - Custom step distribution for different model usage
  - *From: 465174342225887233*

- **CFG with LightX2V**: 1
  - Prevents morphing and broken faces/hands
  - *From: Atlas*

- **LightX2V strength**: 3 on high, 1 on low
  - Default values in KJ shared workflow
  - *From: NebSH*

- **Video upscale start step**: 8-9 out of 12 for upscaling, 4 for motion fixes
  - Controls how much the video changes during upscaling
  - *From: thaakeno*

- **High-res generation denoise**: 0.35
  - For 5B upscaling stage in two-stage pipeline
  - *From: Juan Gea*

- **Steps for quality**: 4/4 instead of 2/2
  - Better motion and quality results
  - *From: ingi // SYSTMS*

- **Lightning LoRA steps**: 4 steps high, 2 steps low
  - Works well with new lightning lora for speed
  - *From: Rainsmellsnice*

- **Steps for 14B model**: 10 start / 6 end for both KSamplers
  - Good for social media content
  - *From: Wist*

- **Steps for 5B model**: 30 steps
  - Recommended setting
  - *From: Wist*

- **Scheduler preference**: res_2m scheduler takes 2x time but is key for quality
  - Better quality despite slower speed
  - *From: patientx*

- **Fast wan lora strength**: 0.5 on low noise pass
  - Optimal strength for quality
  - *From: AshmoTV*

- **New LoRAs**: 5+7 steps with unipc-beta
  - Good results with NAG
  - *From: patientx*

- **Steps configuration**: 4+2 or 4+3 steps in two-pass workflow
  - Better results than default single-pass
  - *From: patientx*

- **Denoise on second pass**: 0.2
  - Works well with two-pass workflow
  - *From: patientx*

- **LoRA strength**: 1.0 on both high and low, though some use 2.25 on high 1.5 on low
  - For Lightning 1.1 LoRAs
  - *From: patientx*

- **Euler/beta scheduler**: euler, shift 8, cfg 1, 6 steps (3/3)
  - Working configuration for quality results
  - *From: CaptHook*

- **Lightning i2v LoRA strengths**: 1.5/1 (high/low)
  - Used in successful generation
  - *From: CaptHook*

- **LightX2V with low CFG**: CFG 2, 6 steps
  - Works well for fast generation
  - *From: NebSH*

- **LightX2V LoRA strength**: High/Low 3/1 for 2.1, strength 2 for 2.2
  - Different strengths needed for different model versions
  - *From: NebSH*

- **Anime LoRA training**: High/Low str1 with 3/4 split on steps, 20 steps (10/10 split)
  - Good balance for anime style generation
  - *From: 138234075931475968*

- **Frame count for 24fps**: 5*24+1 frames
  - Avoids slow motion artifacts
  - *From: Immac*

- **Character LoRA strength**: 1/1 and 1.3
  - For character consistency
  - *From: NebSH*

- **Context frames**: 121 frames
  - Better smoothness than 81 frames
  - *From: xwsswww*

- **LoRA training resolution**: 256 to 1280 pixels multi-res
  - Better quality results
  - *From: Fill*

- **Generation batch size**: 4 at 512x256
  - Pick best result before upscaling
  - *From: Fill*

- **Context window settings for long renders**: 875 frames total, specific overlap settings
  - Better results for 30 second material
  - *From: T2 (RTX6000Pro)*

- **CFG scheduling**: Regular CFG then drop to CFG1
  - Better results in multi-step process
  - *From: TK_999*

- **VACE empty frame level**: 0.5 instead of 0
  - Mid-gray (127,127,127) helps model understand frames to fill
  - *From: ingi // SYSTMS*

- **Audio CFG scale**: 1.3
  - Better lip sync
  - *From: Yae*

- **CFG for Wan 2.2 14B**: 3.5 for first 3 steps on HN model
  - Increase prompt adherence
  - *From: AshmoTV*

- **InfiniteTalk settings**: 25 steps, cfg 3.5, shift 8, audio cfg scale 4, 9 motion frames
  - Working configuration
  - *From: seitanism*

- **Long generation settings**: 32 steps, 3.5 cfg, 7 shift, 3.5 audio cfg scale, dpm++ sde
  - For 2400 frame generations
  - *From: seitanism*

- **Block swapping**: 40 blocks
  - Can swap with 14B models
  - *From: 𝕯𝖗. 𝕸𝖆𝖈𝖆𝖇𝖗𝖊 ☠*

- **Steps for Wan 2.2 quality/speed balance**: 8 steps, 220 seconds
  - Good mix of quality and speed
  - *From: ArtOfficial*

- **Wan 2.2 5B Turbo**: 4 steps
  - Very fast generation
  - *From: patientx*

- **LightX2V LoRA**: 3/1
  - Used with 6 steps for good results
  - *From: NebSH*

- **Lazy cache threshold**: Default values work better than 0.1
  - 0.1 threshold caused bad, stunted movements
  - *From: Vérole*

- **Wan 2.2 without LightX2V**: 40 steps, CFG 3.5
  - Good results with lazy cache
  - *From: Vérole*

- **S2V native workflow settings**: Wan 2.1 fusionx + lightx2v T2V loras at 1 strength, UniPC/simple 6 steps, 480 res
  - Low res baseline testing
  - *From: U̷r̷a̷b̷e̷w̷e̷*

- **Orbit lora strength**: Everything at 1 for high and low orbit loras
  - For full orbit effect
  - *From: 128578659047964672*

- **S2V with CFG and lora**: CFG 3 and lightx2v i2v lora at strength 1.0
  - Working configuration
  - *From: Ablejones*

- **Lightx2v with steps**: 4 steps or 6 steps, lora strength 1.5, CFG 1
  - Optimal performance settings
  - *From: hicho*

- **InfiniteTalk audio scale**: 1.25
  - Good lipsync results
  - *From: Bleedy (Madham)*

- **Wan upscaler denoise**: Between 0.1 and 0.4, sometimes up to 0.79
  - Right balance to not lose structure of original video
  - *From: mdkb*

- **Steps for quality results**: 2+2 (4 total) or 3+3 (6 total)
  - Good quality without excessive compute
  - *From: .: Not Really Human :.*

- **Lightning LoRA configuration**: LOW: lightning 0.8, HIGH: Lightning 1.2, 4 steps
  - Better results after testing
  - *From: Ashtar*

- **LightX strength on high noise**: 5.6
  - Found in Reddit workflow
  - *From: l҈u҈c҈i҈f҈e҈r҈*

- **Sampler for multi-KSampler workflow**: UniPC beta instead of Euler
  - Reduces flashing artifacts
  - *From: asd*

- **InfiniteTalk performance**: 1 minute per second of video on 12GB 3060
  - Balanced speed vs quality
  - *From: U̷r̷a̷b̷e̷w̷e̷*

- **MagicWan with Lightning LoRAs**: High at 0.7, Low at 0.7
  - Good balance for hybrid model
  - *From: patientx*

- **MagicWan optimal config**: 4 steps, res_2s, beta57, cfg 1
  - Final recommended settings
  - *From: patientx*

- **Fun HPS/MPS LoRAs**: 0.5 to 1.0 strength
  - Definite improvement even at 4 steps
  - *From: patientx*

- **Wan 2.2 Lightning LoRAs**: High and low both at 0.7
  - Works well with lightx2v_v2
  - *From: patientx*

- **Low model V2V**: 0.30 denoise
  - Low model works amazingly at this setting
  - *From: hicho*

- **Native workflow minimal**: 2 steps (1 step per sampler)
  - Fast generation while maintaining quality
  - *From: patientx*

- **Lightx2v LoRA strength**: 5.6 and 2.0
  - Used on both models in multi-stage generation
  - *From: patientx*

- **MPS/HPS LoRA strength**: 0.5
  - 1.0 makes slow motion, 0.5 provides good balance
  - *From: patientx*

- **Resolution for PUSA**: 480x832px or 576x1024px
  - Standard resolutions used with PUSA extension
  - *From: . Not Really Human :.*

- **Topaz upscale settings**: Proteus/Chronos_fast upscale x4, 60fps + manual grain/details/sharpness
  - Better performance than Starlight with good quality
  - *From: . Not Really Human :.*

- **MPS/HPS for Wan 2.2**: 0.5 high noise, 1.0 low noise
  - Reduces slow motion while maintaining quality improvements
  - *From: GalaxyTimeMachine (RTX4090)*

- **T2I generation settings**: 1920x1080, 30 steps, res_2s with Clownshark sampler
  - Good prompt following for T2I use
  - *From: Simonj*

- **Low VRAM upscaling**: 512x512 tiling, 2 steps, denoise 0.1 or lower
  - Works on 3060 RTX for 1080p 121 frames without artifacts
  - *From: mdkb*

- **Tile padding**: 96-128 pixels
  - Reduces visible seams between tiles in upscaling
  - *From: 153803064858378240*

- **Context window**: Half of total video frames (33 or 49)
  - Balances memory usage with generation quality
  - *From: 153803064858378240*

- **LoRA training settings**: LoRA rank 64, high noise, slower training speed
  - Improved training results compared to rank 32
  - *From: 253611044595826688*

- **Long generation resolution**: 800x480px
  - Works without OOM for 321 frame generations, 848x480 caused OOM
  - *From: l҈u҈c҈i҈f҈e҈r҈*

- **InfiniteTalk generation**: 6 steps with NAG ksampler
  - Better results than vanilla sampler
  - *From: l҈u҈c҈i҈f҈e҈r҈*

- **S2V improvements**: 6 steps with 2.1 lightx2v and fusionx LoRAs both at strength 1
  - Better S2V results than default settings
  - *From: U̷r̷a̷b̷e̷w̷e̷*

- **Video length**: 81 frames (multiple of 16+1)
  - Sweet spot for model performance and memory usage
  - *From: ingi // SYSTMS*

- **Context window overlap**: 10 frames
  - Provides smooth transitions without degradation in VACE 2.2
  - *From: Vérole*

- **Image blend mode**: Screen at 0.25 strength
  - Optimal for combining controlnet inputs like pose and depth
  - *From: mdkb*

- **Denoise strength for video-to-video**: 0.7
  - Good balance for maintaining input while allowing changes
  - *From: hicho*

- **Audio scale**: 1
  - Best setting to not over exaggerate mouth movements
  - *From: 1348584179440418868*

- **Steps for HuMo**: 4
  - Gets rid of problem of mouths moving on silence (2 steps has this problem)
  - *From: 1348584179440418868*

- **Resolution for 5090**: 544x960
  - Used with 121 frames each in about 4 windows, took ~10 min
  - *From: AR*

- **12GB VRAM settings**: Q5KM GGUF wanimate, sage/triton/blockswap, 6 steps, 1 cfg, 624x368 res
  - Working settings for 12GB VRAM, 15s video in about 12 minutes
  - *From: U̷r̷a̷b̷e̷w̷e̷*

- **Denoise for upscaling**: 0.25-0.3
  - Keeps tile seams from being obvious
  - *From: 153803064858378240*

- **Steps with LightX**: 10 steps (5/5)
  - Used with Wan 2.2 for good results
  - *From: ingi // SYSTMS*

- **Pose strength**: 0.2
  - Better lip sync quality compared to 0.7
  - *From: Léon*

- **Steps split**: 6/3 with shift to 2
  - Better results for style transfer at higher resolution 1280
  - *From: Dkamacho*

- **Sampler split**: 50/50 seemed better than 25/75
  - For Euler/Karras with Lightx2V, though scheduler limitations noted
  - *From: garbus*

- **SageAttention**: Off
  - Improves lipsync quality, especially in native workflows
  - *From: Ablejones*

- **Humo steps**: 8 steps
  - Effective for audio-driven generation
  - *From: hicho*

- **LightX 2.1 settings**: High: 0,3,2,2 Low: 0,1,1,1 with 3.5 CFG for first step
  - Optimal balance for quality
  - *From: ingi // SYSTMS*

- **New Lightning LoRA**: Strength 1 for both high/low with no CFG
  - Works well with new lightning loras
  - *From: ingi // SYSTMS*

- **Dyno steps**: 4 steps on low, 4 steps on high
  - Standard configuration for Dyno model
  - *From: NebSH*

- **Generation time on RTX 5090**: 250 seconds for standard generations
  - Performance benchmark
  - *From: AiAuteur*

- **HuMo workflow timing**: 43 minutes total generation time on RTX 4090
  - Performance reference for audio-reactive content
  - *From: kendrick*

- **Steps configuration**: 2+2 for high and low models
  - Optimal balance - tried 6 steps but didn't see enough difference to warrant it
  - *From: U̷r̷a̷b̷e̷w̷e̷*

- **CFG for first sampler in 3-sampler setup**: 3.5
  - Used with no LoRA in the initial sampler for cinematic quality
  - *From: garbus*

- **First sampler steps**: 3-4 steps
  - For the initial sampler in 3-sampler configuration
  - *From: garbus*

- **Scheduler options**: euler/beta64 or euler/sigmoid_offset
  - Works well with lightx2v LoRA
  - *From: garbus*

- **LCM/beta with shift**: 4 shift
  - Used for specific generations
  - *From: U̷r̷a̷b̷e̷w̷e̷*

- **audio_scale**: 1.5
  - For getting emotes from non-human faces
  - *From: AR*

- **audio_cfg_scale**: 1.2
  - Used with audio_scale 1.5, LCM sampler minimizes burn-in effect
  - *From: AR*

- **Steps for OVI**: 30 steps
  - Used for 720p OVI test with good results
  - *From: Simonj*

- **Resolution for quality**: 1536 x 864
  - Rendered on 5090 then upscaled 2x with Topaz
  - *From: Kytra*

- **Upscaling denoise**: 0.18-0.25
  - Better than 0.30 to reduce seams, increase padding and mask blur
  - *From: 153803064858378240*

- **Lightning LoRA configuration**: High and low strength 1, Lightning WAN2.1 strength 3 on high and 0.25 on low
  - Enables 4 steps with good motion, eliminates slow motion
  - *From: Vérole*

- **Frame count for quality**: 125 frames for 5 seconds
  - Standard frame count for 5-second generations
  - *From: AiAuteur*

- **Resolution for I2V**: 640x640 over 480x480
  - Much better results despite longer render times
  - *From: The Coin Hunter*

- **Render time on 3060**: 9 minutes per 5 seconds at 640x640
  - Performance benchmark for RTX 3060 12GB with 16GB RAM
  - *From: The Coin Hunter*

- **Resolution for morphing**: 832x480
  - Works better than 720p for LLM-guided morphing
  - *From: 𝕯𝖗. 𝕸𝖆𝖈𝖆𝖇𝖗𝖊 ☠*

- **Steps for testing vs final**: 2 steps test, 8 steps final
  - Efficient workflow with fixed seed and resolution
  - *From: gpbhupinder*

- **WanAnimate scheduler**: Try LCM or UniPC instead of DPM++_SDE
  - May help with anime character issues
  - *From: AR*

- **WanAnimate resolution**: 480x832
  - Working resolution for character replacement
  - *From: Tachyon*

- **Upscaling ratio**: At least 2x, ideally 4x from original
  - Flash upscaler works best with significant upscaling from very low res
  - *From: Tony(5090)*

- **Wan 2.2 square aspect ratio, 35 steps**: 2m30s per 5 second clip
  - Performance reference on 4090
  - *From: reallybigname*

- **Wan 2.5 steps and cfg**: 4 steps, cfg 2
  - Better results with no lora, avoids same faces
  - *From: hicho*

- **SVI steps comparison**: 4 steps vs 8 steps
  - Testing different step counts
  - *From: Vérole*

- **HuMo SVI overlap**: 1 frame overlap
  - Causes some discontinuities but HuMo voice guidance keeps flow smooth
  - *From: Ablejones*

- **Holocine frames**: 253fr 480*480
  - Test configuration
  - *From: NebSH*

- **Wan Animate 2.2 lightweight**: 101 frames 720x400, under 200 seconds
  - Performance on 3090
  - *From: TimHannan*

- **visualfrisson workflow**: 8 steps, 720p
  - Good balance of quality and speed
  - *From: Gateway {Dreaming Computers}*

- **Fun VACE extensions**: 20 steps, CFG 3.5
  - Without distill loras
  - *From: Ablejones*

- **Wan 2.2 I2V**: GGUF Q4 quantization
  - For car generation quality
  - *From: hicho*

- **Long cat settings**: Torch compile turned off, SDPA instead of sageattn
  - Better character consistency and transitions
  - *From: smithyIAN*

- **HN/LN step configuration**: HN steps with no lora and CFG, lightx for LN with CFG 1
  - Avoid color/light shifts
  - *From: Ablejones*

- **CFG for High Noise**: 2.5 or 3.0 typically
  - User preference though no specific technical reason given
  - *From: Ablejones*

- **Basic I2V settings**: 10 steps, 5/5 split, 2K input, 720p output, RIFE 50fps
  - Produces good quality results with reasonable generation time
  - *From: 𝕯𝖗. 𝕸𝖆𝖈𝖆𝖇𝖗𝖊 ☠*

- **Light LoRA strength for style preservation**: High at 1.0, Low at 0.3 for 16 steps
  - Better preserves style LoRA effects compared to usual 6-step settings
  - *From: KevenG*

- **Denoising tweaking**: Adjust by 0.1 increments
  - Fine-tuning approach for optimizing image quality
  - *From: 𝕯𝖗. 𝕸𝖆𝖈𝖆𝖇𝖗𝖊 ☠*

- **FFGO LoRA steps**: 12 steps with start_step at 3
  - Starting at step 1 makes monkey not follow input motion, step 3 works better
  - *From: Nathan Shipley*

- **Euler/Beta57 for T2V**: 4/5/5 steps
  - Good results for T2V generations with lightxV2 LoRA
  - *From: garbus*

- **Small LoRA training**: 600 steps, 1.5 hours on A100-80
  - Sufficient for testing if concept works with 3 video dataset
  - *From: AshmoTV*

- **VACE strength**: 0.6
  - Sweet spot for masking control in VACE
  - *From: FlipYourBits*

- **Frame overlap for SVI**: 4 frames
  - Reduces camera movement shifts compared to 1 frame overlap
  - *From: Ablejones*

- **SVI overlap frames**: 1 frame
  - Standard setting being tested
  - *From: Benjimon*

- **Mask strength for middle frames**: Configurable/reduced for long gens
  - Higher strength for legal length gens, lower for longer generations to prevent flashing
  - *From: Chandler*

- **Technically Color WAN LoRA strength**: 0.45
  - Good balance for color enhancement
  - *From: hicho*

- **HuMo steps**: 4
  - Fast generation - about 1 minute each, good quality for speed
  - *From: 152993277631528960*

- **FFGO default resolution then upscale**: 1280x720 to 1920x1080
  - 8 minutes per run, manageable VRAM usage
  - *From: Dkamacho*

- **WanAnimate default values**: 720p resolution
  - Using default KJ template without touching other settings
  - *From: 153803064858378240*

- **FastWan LoRA with 2 steps**: 2 steps
  - Can retain motion with added detail
  - *From: patientx*

- **frame_load_cap**: maximum 97
  - Single VACE generation limit
  - *From: Ablejones*

- **force_rate**: 16
  - Provides more video duration
  - *From: Ablejones*

- **CFG**: 1.0
  - At this value, negative prompts are not used
  - *From: Ablejones*

- **Draw Mask On Image color**: 127,127,127
  - Grey works better than black for VACE masking
  - *From: Ablejones*

- **V2V denoise on both H and L**: 0.2
  - Good balance for video-to-video generation
  - *From: hicho*

- **Wan 2.2 resolution test**: 1280x720 8 steps
  - High quality but takes 9 mins per group
  - *From: VRGameDevGirl84(RTX 5090)*

- **HuMo generation**: 1280x720 8 steps
  - Used for long overnight generations with first/last frame workflow
  - *From: VRGameDevGirl84(RTX 5090)*

- **Wan v2v denoise**: 0.2 denoise with low model
  - For LTX to Wan v2v enhancement to get crazy detail results
  - *From: hicho*

- **SVI Pro 2.2 sampling**: 2.0cfg no lightx2v then 3/3 high/low
  - Template setup for 3 samplers, though not necessarily beneficial
  - *From: JohnDopamine*

- **Resolution for VACE background replacement**: 720x1280
  - Higher resolution gives better results
  - *From: Hashu*

- **Sampler and steps for VACE**: 6 steps with dpm++_sde
  - Recommended settings for background replacement
  - *From: Hashu*

- **Model variant for VACE**: fp8_scaled instead of just fp8
  - May provide better results
  - *From: Hashu*

- **Denoise for LTX2 to Wan v2v**: Low latent denoise of 0.15
  - For upscaling existing videos
  - *From: hicho*

- **Resolution for workflow**: 1024x576 in ComfyUI
  - Standard working resolution, then export as 1080p in post
  - *From: VRGameDevGirl84(RTX 5090)*


## Concepts Explained

- **Differential diffusion**: Soft mask inpainting technique that works with non-inpaint models for localized control
  - *From: spacepxl*

- **RifeX vs RIFE**: RifeX modifies model weights to generate more original frames, RIFE does frame interpolation to increase FPS
  - *From: Juampab12*

- **Block swap**: Memory management technique - setting to 0 with sufficient VRAM significantly speeds up inference
  - *From: Juampab12*

- **TeaCache**: Caching mechanism that speeds up generation by reusing computations from specified start step
  - *From: DiXiao*

- **Sliding context windowing**: Technique to generate longer videos by processing overlapping windows of frames
  - *From: Kijai*

- **FlowEdit**: Not like IP-Adapter, requires source and target prompts for video-to-video style transfer
  - *From: Zuko*

- **Window blending**: Technique to blend context windows to reduce noise, happens after CFG math
  - *From: Kijai*

- **Sliding context windows**: Method for generating longer videos by processing overlapping segments
  - *From: Kijai*

- **Multidiffusion**: Technique using temporal and spatial tiling for upscaling video
  - *From: Benjaminimal*

- **FlowEdit**: Video transformation technique that requires source and target images to somewhat align
  - *From: mono*

- **FlowChain nodes**: Allows embedding whole workflow APIs inside another workflow, exposing choice of inputs/outputs that can be chained together to simplify complex workflows
  - *From: AJO*

- **Frame buckets**: Setting used during lora training to control maximum frame count
  - *From: Kytra*

- **Frame buckets**: Training parameter [1,33,73] used to structure how the model learns from video sequences
  - *From: Kytra*

- **First frame inpainting embed**: Technique combining first frame inpainting with I2V model for enhanced control - full explanation pending
  - *From: IllumiReptilien*

- **Context windows**: Method for extending video length beyond base model capabilities
  - *From: chrisd0073*

- **MADness**: Issues caused by recursive training on synthetic data - Model Autophagy Disorder
  - *From: spacepxl*

- **Bongmath**: Sampling method that makes each step sample forwards and backwards simultaneously within the step
  - *From: Clownshark Batwing*

- **Regional conditioning**: Attention masks that split up cross and self attention both, allowing different conditioning for different regions
  - *From: Clownshark Batwing*

- **Frame weights reversal**: When using I2V model with guide image, should reverse frame weights to not interfere with starting image
  - *From: Ablejones*

- **Conditioning error (77)**: Anytime you see 77 in errors, that's almost certainly text encoder/clip/conditioning/T5/etc related
  - *From: Clownshark Batwing*

- **First frame latent for last frame**: Fun InP model expects a first frame latent as the last frame condition, which causes color issues if done incorrectly
  - *From: spacepxl*

- **VACE**: Video control system for style transfer, inpainting, subject-driven generation, and outpainting. Works like an IP-adapter for WAN
  - *From: Vérole*

- **Guide mode in samplers**: Method to use an encoded image latent as guidance for T2V generation while using empty latent for main sampler input
  - *From: Clownshark Batwing*

- **Dense prompts for T2V**: Detailed prompts work better for T2V because they help guide the output, while I2V doesn't need them since the image already captures context
  - *From: Amirsun(Papi)*

- **VaceSwap**: Term coined for face swapping technique using VACE
  - *From: ArtOfficial*

- **Triangular attention mask**: Attention masking technique that maintains character consistency during scene changes
  - *From: Clownshark Batwing*

- **Temporal conditioning**: Technique using two prompts - one describing first frame, one describing last frame
  - *From: Clownshark Batwing*

- **Regional conditioning**: Technique that works really well for controlling specific areas of generation
  - *From: Clownshark Batwing*

- **Sliding window self-attention**: Limits how many frames each frame can 'see' instead of every frame seeing every other frame. Reduces VRAM usage quadratically, enabling much longer video generation
  - *From: Clownshark Batwing*

- **res_3m vs res_3s samplers**: res_3m makes 1 model call and reuses 2 previous steps, while res_3s makes 3 model calls per step. Both start with euler but can be configured differently
  - *From: Clownshark Batwing*

- **Steps analogy**: Steps like running meat through slicer - you want 1 pound total, steps determine slice thickness. Too thin loses context in latent noise
  - *From: ZombieMatrix*

- **Diffusion Forcing sampling**: Creates individual sampler for each latent, enables temporal coherence across video segments
  - *From: Kijai*

- **Time embeds memory usage**: 14B model time embeds expanded to sequence length take 4GB+ extra VRAM
  - *From: Kijai*

- **Sliding window attention**: Technique that makes self attention cost scale subquadraticarly, allowing generation of very long videos (601 frames) in single shot without quality degradation, though composition can drift more
  - *From: Clownshark Batwing*

- **ModelSamplingSD3 shift**: Parameter that affects movement in scene - high value decreases movement, lower value increases movement
  - *From: ZombieMatrix*

- **Bongmath**: Technique allowing sampler to work forwards and backwards simultaneously for dramatically improved results
  - *From: Clownshark Batwing*

- **VACE workflow**: Video control system that can do style transfer, uses depth maps and partial denoise
  - *From: 88822364468412416*

- **DF (DreamForge)**: 24fps infinite generation system that actually works for extensions
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Partial denoise**: Encoding input and piping straight into samples for video processing
  - *From: 88822364468412416*

- **Block swapping**: VRAM optimization technique needed for higher resolutions on certain GPUs
  - *From: 88822364468412416*

- **bongmath/bongsampling methodology**: A sampling method that can be activated in Clownshark's nodes, provides better results than standard ksampler
  - *From: Clownshark Batwing*

- **teacache**: Optimization technique used in speed-optimized settings with values like (0.250/6)
  - *From: seruva19*

- **Context window**: Feature for extending video generation capability, used for longer sequences
  - *From: DiXiao*

- **Tiled upscaling**: Method to upscale large images/videos by processing in tiles to manage VRAM usage
  - *From: Clownshark Batwing*

- **Chain sampling**: Technique to change parameters, models, or settings mid-generation using multiple connected samplers
  - *From: Clownshark Batwing*

- **Latent guides**: Using latent representations of images/videos to guide generation for video-to-video workflows
  - *From: Ablejones*

- **Guide modes**: Different modes like 'flow', 'lure', 'data', 'pseudoimplicit', 'epsilon' for controlling latent guidance behavior
  - *From: Ablejones*

- **VACE intelligence**: VACE understands context and selectively uses reference based on prompt compatibility
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Reference latent trimming**: VACE tacks reference to first latent, but wrapper automatically trims it before decoding
  - *From: DawnII*

- **Context processing**: Processes X (context length) frames at a time to allow more frames without AllocationOnDevice errors
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Tiled attention vs tiled latents**: Tiled attention computes Q globally but restricts KV to local tiles, giving full generation quality with tiled speed
  - *From: deleted_user_2ca1923442ba*

- **Reference pose**: Node that retargets joints for characters with different proportions by rescaling the main pose
  - *From: Guey.KhalaMari*

- **FETA weight**: Parameter for controlling VACE influence with start and end values
  - *From: Kendo*

- **Context window**: Number of frames the model considers for temporal consistency
  - *From: Kendo*

- **Block 0 disabled**: Technique to improve CausVid LoRA performance by disabling specific transformer block
  - *From: JohnDopamine*

- **Context bleeding**: When longer context windows cause the model to recognize subjects and interfere with style transfer
  - *From: Zlikwid*

- **Clean plate generation**: Removing objects from video by using rectangular masks and inpainting techniques
  - *From: ArtOfficial*

- **Shift parameter**: Controls the stylistic output - lower values (1) for realism, higher values (3+) for stylized content. Needs adjustment based on resolution
  - *From: VRGameDevGirl84(RTX 5090)*

- **TeaCache**: A caching system that can cause generation issues in workflows when not properly configured
  - *From: MysteryShack*

- **Blockswap**: Memory management technique mandatory for VACE to prevent VRAM overflow
  - *From: MysteryShack*

- **Image-as-video V2V**: Technique of converting single image to video format then processing through V2V for faster results than traditional I2V
  - *From: hicho*

- **res_multistep sampler**: Sampler geared towards video, made by nvidia for Cosmos release, default sampler for ace_step music model
  - *From: MilesCorban*

- **Optical audio from film reels**: Inspiration for encoding mel spectrum band across bottom of video frame for frame-accurate audio generation
  - *From: ZombieMatrix*

- **FusionX**: VRGameDevGirl84's optimized merge model that significantly reduces render times while maintaining quality
  - *From: VRGameDevGirl84(RTX 5090)*

- **VACE masking**: Method for character consistency using mask-based control in video generation
  - *From: Charine*

- **Context options**: Feature that allows longer generations by maintaining context awareness, though it has limitations like looping artifacts
  - *From: Guey.KhalaMari*

- **Self-Forcing**: Training method that fixes autoregressive video diffusion's exposure bias by training models on their own outputs instead of just ground truth
  - *From: SS*

- **FusionX LoRA**: LoRA extracted from merged fp16 model, equivalent to merging all original LoRAs into single LoRA
  - *From: VRGameDevGirl84(RTX 5090)*

- **Shift value in VACE**: Parameter that controls balance between realism and motion - lower values more realistic but static, higher values more natural motion
  - *From: ingi // SYSTMS*

- **NAG (Normalized Attention Guidance)**: A node from kjnodes that adds the ability to negative prompt at cfg1
  - *From: MysteryShack*

- **Self Forcing LoRA**: LoRA that adds or extends motion in video generation
  - *From: patientx*

- **Context overlap**: Using overlapping frames between chunks for consistency in long video generation
  - *From: Yae*

- **WAN Context Options**: System that allows generating long videos by setting context frames (e.g., 81) and total frames (e.g., 1000), repeatedly sampling chunks until complete
  - *From: Yae*

- **Diffusion Forcing (DF)**: Video extension technique that can be chained multiple times with different settings for complex camera movements
  - *From: Ablejones*

- **VACE Self Forcing**: Using VACE for motion control with better tracking on black backgrounds
  - *From: Jonathan*

- **VACE frame strength**: Different strength applied to VACE frame, but didn't make much difference until pushed hard where it breaks generation
  - *From: Ablejones*

- **Parallax effect for camera movement**: Visualize how 2 points will move over time to create proper camera splines
  - *From: Jonathan*

- **Control input frames vs reference image**: Control input frames completely take over influence from reference image when present
  - *From: Ablejones*

- **VACE reference input**: Allows using reference images to guide video generation while maintaining flexibility with reduced end frame strength
  - *From: Ablejones*

- **Context in MultiTalk**: Feature that removes frame limits for V2V generations in MultiTalk
  - *From: N0NSens*

- **Pure edit with VACE**: Using VACE to modify existing content while maintaining structure through controlnets like depth
  - *From: ingi // SYSTMS*

- **GGUF Q4 KS**: Quantized model format that enables higher resolution generation on lower VRAM hardware
  - *From: hicho*

- **Viewport rendering**: Rendering directly from 3D software viewport instead of full scene setup, then using AI for enhancement
  - *From: hicho*

- **Control video vs reference image**: Using video as control input vs single reference image - video control allows for more dynamic animation
  - *From: various*

- **VACE inpainting masking**: Input_frames: areas to change = 127,127,127 RGB. Input_masks: areas to change = white, areas to keep = black
  - *From: Hashu*

- **Biped workflow**: 3dsmax biped with mocap file loaded, mesh skinned to biped acts as openpose driver for VACE
  - *From: Duranovsky*

- **3D mask vs 2D mask in VACE**: AI can create masks that appear more dimensional and wrap around objects naturally, versus flat 2D masks created in traditional software
  - *From: Sal TK FX*

- **Flow match scheduler**: A scheduler option available in Kijai's wrapper, designed for use with Pusa model
  - *From: patientx*

- **Cross-batch degradation**: Quality loss that compounds over time when doing multiple batch generations
  - *From: A.I.Warper*

- **VACE middle gray inpainting**: Use RGB 127,127,127 in masked areas, VACE only inpaints gray areas leaving rest untouched
  - *From: Neex*

- **Uni3C motion transfer**: I2V only feature that transfers both camera and character motion from reference videos
  - *From: N0NSens*

- **Ingredients workflows**: Modular approach using LoRAs instead of merged models for easier customization
  - *From: VRGameDevGirl84(RTX 5090)*

- **Concept check**: Quick workflow switch to test how specific prompt words affect generation without reloading
  - *From: garbus*

- **Two-pass generation**: Running generation through two separate samplers for detail enhancement, like 4+4 steps
  - *From: ingi // SYSTMS*

- **Latent-to-latent**: Second pass processing that doesn't require VAE encode-decode, making it faster
  - *From: patientx*

- **Wan-KF2V**: Keyframe-to-video: wan-i2v (1 image) | wan-flf2v (2 images) | wan-kf2v (n images)
  - *From: Benjaminimal*

- **FFLF**: First-Frame-Last-Frame morphing for video extension
  - *From: JmySff*

- **Industry camera terms**: Professional terminology like 'trucks in', 'dollies out', 'tilts up' for camera movement
  - *From: TK_999*

- **High noise vs Low noise architecture**: High noise sampler controls the main generation architecture while low noise just fills in details
  - *From: DawnII*

- **Context windows**: Technique for using multiple prompts across longer video generations
  - *From: Kijai*

- **Frame overlap technique**: Using end frames from first clip and start frames from next clip to create seamless transitions
  - *From: ingi // SYSTMS*

- **VACE merge with Wan 2.2**: Merge of WAN 2.2 High and Low models with Vace for better image control, reference images don't work with Vace v1 but image control works fine
  - *From: R.*

- **Block swapping**: Memory management technique that causes instability and random artifacts in generations, avoided by using smaller models for upscaling
  - *From: Juan Gea*

- **Start step control in video upscaling**: Higher start steps (8-9/12) preserve content for upscaling, lower start steps (4/12) allow more motion changes and fixes
  - *From: thaakeno*

- **NAG (Normalized Attention Guidance)**: Technique that improves generation quality, referenced in relation to better results
  - *From: patientx*

- **High/Low noise passes**: Wan 2.2 uses MoE architecture with separate expert handling for high and low noise
  - *From: various*

- **FLF (First-Last-Frame)**: Morphing technique between first and last frames for video extension
  - *From: various*

- **CFG scheduling**: Method using multiple samplers or schedule nodes to control generation guidance
  - *From: AshmoTV*

- **Two-pass workflow**: Using high_noise model for initial steps, then connecting latent to second ksampler with lower denoise for refinement, rather than default workflow with denoise 1 on both
  - *From: patientx*

- **Prompt scheduling**: Using timesteps followed by visual instructions to control video generation over time, works better than JSON format
  - *From: AshmoTV*

- **VACE empty frame level**: Determines color of empty frames - 0 is black, 1 is white, 0.5 is mid-gray. Mid-gray tells VACE to fill in frames between start/end
  - *From: ingi // SYSTMS*

- **Two-stage generation process**: Generate at low resolution first, then upscale and run through low noise model only at full resolution
  - *From: Fill*

- **Context windows**: Overlapping frame segments that allow generation of longer videos with smooth transitions
  - *From: xwsswww*

- **Block swapping**: Memory optimization technique allowing 8GB VRAM with 64GB RAM to handle larger models
  - *From: xwsswww*

- **MAGREF**: I2V likeness system for character consistency
  - *From: context*

- **InfiniteTalk**: Audio-reactive lip sync system that works without driving video
  - *From: seitanism*

- **Fantasy Portrait**: Lip sync system that requires driving video input
  - *From: multiple users*

- **Split sigmas**: Technique involving different configurations of high and low noise experts with latent noise injection
  - *From: l҈u҈c҈i҈f҈e҈r҈*

- **Bong_tangent sampler**: Aggressive sampler that works well for image models but too aggressive for 10-step Wan video generation
  - *From: Ablejones*

- **FFLF**: First-Frame-Last-Frame morphing technique
  - *From: KevenG*

- **Melband**: Audio node added by KJ for audio processing
  - *From: Bleedy (Madham)*

- **Distill loras**: LoRAs like lightx2v that require careful step management to avoid burning
  - *From: Kijai*

- **Pusa LoRA**: A 'magic' LoRA that helps fix slow motion issues and improves motion quality in Wan 2.2
  - *From: 𝕯𝖗. 𝕸𝖆𝖈𝖆𝖇𝖗𝖊 ☠*

- **Context Window**: Init image will be repeated each window, affecting consistency in lip sync
  - *From: N0NSens*

- **High/Low Noise Expert Split**: MoE architecture in Wan 2.2 with different experts for high and low noise levels
  - *From: system*

- **res_2s**: Double generation time scheduler, equivalent to 8 steps in reality when set to 4 steps
  - *From: patientx*

- **MagicWan**: Wan 2.2 high+low hybrid model available on Civitai
  - *From: patientx*

- **PUSA**: A way to make I2V with T2V Wan, extension technique
  - *From: ˗ˏˋ⚡ˎˊ-*

- **FLF**: First-Last-Frame morphing technique
  - *From: 947112250198618162*

- **MPS LoRA**: Boosts average image quality (objective score) - tries to make movement better
  - *From: . Not Really Human :.*

- **HPS LoRA**: Boosts human-perceived aesthetics (subjective score) - adds visual appeal but can be problematic for I2V
  - *From: . Not Really Human :.*

- **FF-LF**: First-Frame-Last-Frame morphing technique for video generation
  - *From: A.I.Warper*

- **Tile padding**: Overlapping pixels between tiles to avoid seams. For 1920x1080 with 2x2 tiling (960x540 base), adding 64 pixel padding creates 1024x604 tiles that overlap when composited back to reduce seaming
  - *From: 153803064858378240*

- **High/Low noise in Wan models**: Wan 2.1 supports high noise training but not low noise. High noise is not exclusive to Wan 2.2
  - *From: 253611044595826688*

- **Core context node**: Native Wan context window implementation that allows longer generation contexts, different from wrapper version
  - *From: l҈u҈c҈i҈f҈e҈r҈*

- **Context windows**: Method of extending video length beyond model limits by generating overlapping segments and blending them together
  - *From: Vérole*

- **Multiple of 16+1 frame length**: Frame counts that follow pattern 16n+1 (like 81) work optimally with the model architecture
  - *From: ingi // SYSTMS*

- **Model mixing compatibility**: Using different model types (bf16 vs GGUF vs fp8) together can cause compatibility issues and workflow failures
  - *From: mdkb*

- **FFLF**: First-Frame-Last-Frame morphing/transition technique
  - *From: Charlie*

- **DWPose Estimator**: Pose estimation tool with body-only mode enabled
  - *From: AR*

- **Face crop input**: Important for eye and lip sync in wan animate
  - *From: hicho*

- **V2V (Video to Video)**: Get exactly what you prompt but with motion of the original video, provides more control without controlnet
  - *From: hicho*

- **Fun Control Camera**: Version made for camera movement prompting, as regular prompting for camera movement has limited success
  - *From: Rävlik*

- **Keyframes**: Method for creating long generations by using start/end frames
  - *From: Charlie*

- **Dyno**: New t2v high noise model from lightrx team, available as full model or LoRA, designed for improved motion
  - *From: asd*

- **Context windows**: Method to maintain quality and consistency across longer video generations
  - *From: AR*

- **3-Sampler setup**: Using three samplers in sequence - first establishes motion, others refine with regular settings
  - *From: garbus*

- **Dyno LoRAs**: Lightning LoRAs for Wan 2.2 that enable fast 2+2 step generation with high and low noise expert models
  - *From: hicho*

- **3 sampler method**: Using an additional sampler before the standard high/low setup, with its own model load, no LoRA, and different CFG for more cinematic results
  - *From: garbus*

- **Embed windows vs context windows**: 77 frame embed windows used for WanAnimate generation, different from context windows
  - *From: A.I.Warper*

- **Block swap**: Technique to make generation faster by swapping blocks between RAM and VRAM, especially useful with high RAM systems
  - *From: VRGameDevGirl84(RTX 5090)*

- **Wan VACE**: Video control system that can be used with depth control and masking
  - *From: hicho*

- **First Frame Last Frame morphing**: Technique for video extension and smooth transitions between clips
  - *From: The Coin Hunter*

- **Next Scene LoRA**: LoRA designed to help with camera angle transitions between scenes
  - *From: mdkb*

- **Campfire test**: Test of model's ability to move camera to opposite side of scene and look back - most models fail this spatial reasoning task
  - *From: mdkb*

- **Context windows for long generation**: Method of breaking long videos into smaller overlapping segments (e.g., 909 frames in 12 context windows)
  - *From: A.I.Warper*

- **Video continuation generation node**: Node that merges follow-up clips perfectly by managing frame transitions
  - *From: 𝕯𝖗. 𝕸𝖆𝖈𝖆𝖇𝖗𝖊 ☠*

- **Morphing vs fade-in**: Morphing is physical transformation of elements, fade-in is simple opacity change - morphing preferred for seamless transitions
  - *From: 𝕯𝖗. 𝕸𝖆𝖈𝖆𝖇𝖗𝖊 ☠*

- **Differential diffusion**: Using latent noise mask for V2V with inpainting, works well with HuMo
  - *From: Ablejones*

- **VACE edit global mode**: Edit directly without needing depth video or edit first frame in edit mode like kontext
  - *From: hicho*

- **Mocha segmentation propagation**: Model determines how to propagate segmentation on its own from first frame mask, can hallucinate outside mask
  - *From: DawnII*

- **SVI-shot reference image technique**: Keeps whole image from burning, stays very consistent but means less variations
  - *From: Ablejones*

- **Holocine format**: Requires specific prompting with [global caption] and [per shot caption] structure
  - *From: NebSH*

- **FFLF**: First-Frame-Last-Frame morphing technique
  - *From: Ablejones*

- **I2V as edit model**: Using image-to-video model like using a long edit prompt to modify content
  - *From: hicho*

- **FFGO (First Frame Go)**: LoRA that creates camera view changes - you create init image with all elements on white background, use activation phrase 'ad23r2 the camera view suddenly changes'
  - *From: Zuko*

- **Latent noise masking**: Technique to protect unchanged parts of video from degradation during sampling by masking at latent level
  - *From: Ablejones*

- **Context windows with Vace splitting**: Using context windows combined with code that allows Vace to work in segments for longer generations
  - *From: Ablejones*

- **TTM (Time To Move)**: Method of running WAN 2.2 I2V with special code modifying sampling steps, uses specially prepared video in noise samples and references in I2V channels
  - *From: 800884790713647164*

- **Latent noise masks**: Fundamental way to change denoising process by providing latent with noise only on specific parts, model focuses on noisy areas without needing explicit mask
  - *From: Ablejones*

- **Context window prompting**: Using different prompts for backgrounds in each context window for scene transitions
  - *From: Ablejones*

- **FMML**: First Middle Middle Last - a technique for frame generation
  - *From: Janosch Simon*

- **FFGO**: First Frame Go - Wan 2.2 based model that can use several image references with strong prompt adherence
  - *From: Dkamacho*

- **Context windows frying**: Quality degradation that occurs when using built-in WanAnimate context windows vs VACE context windows
  - *From: A.I.Warper*

- **VACE masking principle**: Mask defines where video changes, everything outside mask stays the same. For falling objects, must mask all areas where changes occur
  - *From: Ablejones*

- **Context windows morphing**: Using context window tendency to morph things by injecting different references into each window
  - *From: Ablejones*

- **VACE context vs context windows**: VACE context refers to stacked VACE inputs, different from context windows - context_index selects which VACE input to modify
  - *From: Ablejones*

- **Block specific attention**: A feature implemented in KJ's wrapper that DawnII has been experimenting with in combination with SVI
  - *From: DawnII*

- **HN sampler step counts**: Parameter that can be adjusted to prevent biasing mouth movements too much in HuMo audio-reactive generation
  - *From: Ablejones*

- **SVI extensions**: Method of building longer videos in 4 second chunks, where each chunk has its own prompt and anchor image
  - *From: 152993277631528960*


## Resources & Links

- **Native ComfyUI workflow for Wan** (workflow)
  - https://cdn.discordapp.com/attachments/1342763350815277067/1344074945776451594/ComfyUI_260717_.webp
  - *From: Screeb*

- **AuraSR v2 upscaler** (model)
  - https://huggingface.co/fal/AuraSR-v2
  - *From: yi*

- **Gradient estimation sampler** (tool)
  - https://github.com/ToyotaResearchInstitute/gradient-estimation-sampler
  - *From: ˗ˏˋ⚡ˎˊ-*

- **DiffSynth repository training code** (repo)
  - *From: Kytra*

- **WanVideo fp8 model** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/blob/main/Wan2_1-I2V-14B-480P_fp8_e4m3fn.safetensors
  - *From: Fannovel16*

- **Video upscaling database** (tool)
  - https://openmodeldb.info/
  - *From: Juampab12*

- **FlowEdit workflow** (workflow)
  - https://discord.com/channels/1076117621407223829/1342763350815277067/1345107543751655485
  - *From: Zuko*

- **David Snow's workflow** (workflow)
  - *From: burgstall*

- **Wan GGUF models** (model)
  - https://huggingface.co/calcuis/wan-gguf/tree/main
  - *From: Teslanaut*

- **ComfyUI-GGUF** (repo)
  - https://github.com/city96/ComfyUI-GGUF
  - *From: TK_999*

- **ComfyUI-Fluxtapoz** (repo)
  - https://github.com/logtd/ComfyUI-Fluxtapoz
  - *From: Zuko*

- **ComfyUI-Florence2** (repo)
  - https://github.com/kijai/ComfyUI-Florence2
  - *From: ˗ˏˋ⚡ˎˊ-*

- **FlowEdit project page** (resource)
  - https://matankleiner.github.io/flowedit/
  - *From: Zuko*

- **FlashVideo** (repo)
  - https://github.com/FoundationVision/FlashVideo
  - *From: yi*

- **VEnhancer** (repo)
  - https://github.com/Vchitect/VEnhancer
  - *From: yi*

- **City96 HuggingFace** (model)
  - hf.co/city96
  - *From: TK_999*

- **MagicTime prompts** (resource)
  - https://github.com/PKU-YuanGroup/MagicTime/blob/main/__assets__/promtp_opensora.txt
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Fal.ai inference service** (service)
  - https://fal.ai/
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Wan2.1-T2V-1.3B-crush-smol-v0** (model)
  - https://huggingface.co/finetrainers/Wan2.1-T2V-1.3B-crush-smol-v0
  - *From: DiXiao*

- **4x_NMKD-Siax_200k upscaler** (model)
  - https://huggingface.co/gemasai/4x_NMKD-Siax_200k/tree/main
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Squish LoRA** (lora)
  - https://civitai.com/models/1132089/flat-color-style
  - *From: Fred*

- **Cakify LoRA** (lora)
  - https://civitai.com/models/1337473/cakify-cake-everything-wan-14b-i2v
  - *From: JohnDopamine*

- **Taproot multidiffusion code** (repo)
  - https://github.com/painebenjamin/taproot/blob/main/src/taproot/tasks/generation/video/wan/model/pipeline.py#L221
  - *From: Benjaminimal*

- **Cakify LoRA** (lora)
  - https://civitai.com/models/1337473/cakify-cake-everything-wan-14b-i2v?modelVersionId=1511416
  - *From: Zuko*

- **Squish Effect LoRA** (lora)
  - https://civitai.com/models/1340141/squish-effect-wan21-i2v-lora?modelVersionId=1513385
  - *From: Zuko*

- **360 Degree Rotation LoRA** (lora)
  - https://civitai.com/models/1346623/360-degree-rotation-microwave-rotation-wan21-i2v-lora?modelVersionId=1520902
  - *From: slmonker(5090D 32GB)*

- **Steamboat Willie Style LoRA** (lora)
  - https://huggingface.co/benjamin-paine/wan-lora/resolve/main/steamboat-willie.bf16.safetensors
  - *From: Benjaminimal*

- **Pika Labs effects reference** (reference)
  - https://twitter.com/pika_labs/status/1846295401491845213
  - *From: JohnDopamine*

- **Reddit opensourced effects post** (reference)
  - https://www.reddit.com/r/StableDiffusion/comments/1j99ha8/i_just_opensourced_8_more_viral_effects_request/
  - *From: Juampab12*

- **Mobius looping project** (repo)
  - https://github.com/YisuiTT/Mobius
  - *From: 211685818622803970*

- **Art style LoRA for Hunyuan** (lora)
  - https://civitai.com/models/1264662?modelVersionId=1426201
  - *From: 211685818622803970*

- **Steamboat Willie 14B Lora** (lora)
  - https://huggingface.co/benjamin-paine/wan-lora/resolve/main/steamboat-willie-14b.bf16.safetensors
  - *From: Benjaminimal*

- **Live Wallpaper Style Lora** (lora)
  - https://civitai.com/models/1264662/live-wallpaper-style
  - *From: 211685818622803970*

- **Diffusion Pipe training framework** (repo)
  - https://github.com/tdrussell/diffusion-pipe/tree/main
  - *From: Benjaminimal*

- **ComfyUI VideoHelperSuite** (tool)
  - https://github.com/Kosinkadink/ComfyUI-VideoHelperSuite
  - *From: Cubey*

- **Spiral Staircase concept lora** (lora)
  - https://civitai.com/models/1371822
  - *From: Kytra*

- **KXSR Traveling Concept Lora** (lora)
  - https://civitai.com/models/1372884/kxsr-traveling-concept-wan-14b-t2v?modelVersionId=1551153
  - *From: Kytra*

- **KXSR Side-Scroll Cinematic Lora** (lora)
  - https://civitai.com/models/1374791/kxsr-side-scroll-cinematic-concept-wan-14b-t2v
  - *From: Kytra*

- **KXSR Cinematic Chase Concept** (model)
  - https://civitai.com/models/1379019/kxsr-cinematic-chase-concept-wan-14b-t2v
  - *From: Kytra*

- **KXSR First Person Flight Concept** (model)
  - https://civitai.com/models/1380083/kxsr-first-person-flight-concept-wan-14b-13b-t2v
  - *From: Kytra*

- **Ryza Character Lora** (model)
  - https://civitai.com/models/1382398?modelVersionId=1562078
  - *From: Kytra*

- **Side Scroll Cinematic Lora 1.3B** (model)
  - https://civitai.com/models/1374791?modelVersionId=1567353
  - *From: Kytra*

- **Diffusion-pipe training repo** (repo)
  - *From: Kytra*

- **Superman GoPro reference video** (workflow)
  - https://www.youtube.com/watch?v=H0Ib9SwC7EI&pp=ygUoc3VwZXJtYW4gZmlyc3QgcGVyc29uIHBlcnNwZWN0aXZlIHZpZGVvcw%3D%3D
  - *From: Kytra*

- **ClownsharkBatwing RES4LYF** (tool)
  - https://github.com/ClownsharkBatwing/RES4LYF
  - *From: Clownshark Batwing*

- **Kijai control example workflows** (workflow)
  - https://github.com/kijai/ComfyUI-WanVideoWrapper/tree/main/example_workflows
  - *From: StableVibrations*

- **Wan Restyled First Frame Workflow** (workflow)
  - https://civitai.com/models/1376578/wanrestyledfirstframeworkflow?modelVersionId=1555341
  - *From: A.I.Warper*

- **Chasm's Call LoRA** (model)
  - https://civitai.green/models/1391922/kxsr-cinematic-chasm-concept-wan-13b-t2v
  - *From: Kytra*

- **Boss Fight LoRA** (model)
  - https://civitai.com/models/1392349?modelVersionId=1573723
  - *From: Fill*

- **RES4LYF Repository** (repo)
  - https://github.com/ClownsharkBatwing/RES4LYF
  - *From: Clownshark Batwing*

- **MADness Paper** (research)
  - https://arxiv.org/abs/2408.16333
  - *From: spacepxl*

- **Wan Online Service** (tool)
  - https://wan.video/wanxiang/videoCreation
  - *From: 133784166977372160*

- **RES4LYF sampler repository** (repo)
  - https://github.com/ClownsharkBatwing/RES4LYF
  - *From: Ablejones*

- **WAN 2.1 text encoders** (model)
  - https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/tree/main/split_files/text_encoders
  - *From: Ablejones*

- **UMT5 text encoder** (model)
  - https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/blob/main/split_files/text_encoders/umt5_xxl_fp8_e4m3fn_scaled.safetensors
  - *From: Ablejones*

- **Depth/pose workflow** (workflow)
  - https://discord.com/channels/1076117621407223829/1342763350815277067/1355028335809531914
  - *From: VK (5080 128gb)*

- **Multiple start frames workflow** (workflow)
  - *From: spacepxl*

- **SingularUnity WAN2.1 Ghibli Style T2V** (model)
  - https://civitai.com/models/1419443/singularunity-wan21-ghibli-style-t2v
  - *From: Amirsun(Papi)*

- **WanRestyled First Frame Workflow** (workflow)
  - https://civitai.com/models/1376578/wanrestyledfirstframeworkflow?modelVersionId=1555341
  - *From: A.I.Warper*

- **GIMM-VFI interpolation node** (tool)
  - https://github.com/kijai/ComfyUI-GIMM-VFI
  - *From: ZombieMatrix*

- **Flat Color Style LoRA** (model)
  - https://civitai.com/models/1132089/flat-color-style
  - *From: fearnworks*

- **GraphCap captioning system** (tool)
  - https://github.com/Open-Model-Initiative/graphcap
  - *From: fearnworks*

- **ComfyUI-Crystools** (tool)
  - https://github.com/crystian/ComfyUI-Crystools
  - *From: Level Higher*

- **Topaz Video Enhance AI** (tool)
  - https://www.topazlabs.com/topaz-video-ai
  - *From: ZombieMatrix*

- **Studio Ghibli LoRA for Wan 2.1** (lora)
  - https://civitai.com/models/1404755/studio-ghibli-style-wan21-t2v-14b
  - *From: seruva19*

- **RES4LYF - Temporal conditioning nodes** (repo)
  - https://github.com/ClownsharkBatwing/RES4LYF
  - *From: Clownshark Batwing*

- **TheDirector V1.5** (tool)
  - https://youtu.be/L7SYD_pbraA?si=l1DpnmMA6_AdWiXZ
  - *From: AJO*

- **Subject Replace Workflow** (workflow)
  - https://discord.com/channels/1076117621407223829/1342763350815277067/1359493641273606194
  - *From: ArtOfficial*

- **Wan prompt guide** (guide)
  - https://alidocs.dingtalk.com/i/nodes/EpGBa2Lm8aZxe5myC99MelA2WgN7R35y?spm=a2ty_o02.30011085.0.0.2620e41ecthL0j&utm_scene=team_space
  - *From: 133784166977372160*

- **TheDirectorV2 on MimicPC** (tool)
  - https://home.mimicpc.com/discover-detail?from=workflow&id=a0ac9f1bc1b040ba8e3054d5d9b5c0f2
  - *From: AJO*

- **TheDirectorV2 on Civitai** (model)
  - https://civitai.com/models/1476469?modelVersionId=1670194
  - *From: AJO*

- **Higgsfield motion training examples** (training_data)
  - https://higgsfield.ai/motion/f226ac67-43d3-4726-ad9c-132608bda8b3
  - *From: NebSH*

- **Adrien Toupet WAN masterclass preview** (tutorial)
  - https://www.youtube.com/watch?v=TrJiuTUnUFw
  - *From: Adrien Toupet*

- **WanVideo Diffusion Forcing Sampler workflow** (workflow)
  - *From: Ablejones*

- **Lenticular 3D displays** (hardware)
  - https://www.akwil.com/171-22-82-inch-holographic-3d-tvs-lenticular-displays
  - *From: ZombieMatrix*

- **Inflate LoRA** (lora)
  - https://huggingface.co/Remade-AI/Inflate
  - *From: Adrien Toupet*

- **URFT Flux fine-tune** (model)
  - https://civitai.com/models/978314?modelVersionId=1413133
  - *From: 𝖑𝖚𝖈𝖎𝖋𝖊𝖗*

- **Better Hands LoRA** (lora)
  - On Civitai
  - *From: Tachyon*

- **Teaser video mixing Wan models** (workflow)
  - https://youtu.be/36g_j4sEKn4?si=R--G_OWXRFwOrm-s
  - *From: Adrien Toupet*

- **Plushtoy morph LoRA** (lora)
  - https://civitai.com/models/1525175
  - *From: JohnDopamine*

- **FramePack workflows** (workflow)
  - https://github.com/kijai/ComfyUI-FramePackWrapper/tree/main/example_workflows
  - *From: Janosch Simon*

- **FramePack original** (repo)
  - https://github.com/lllyasviel/FramePack
  - *From: Janosch Simon*

- **360 degree tracking LoRA** (lora)
  - https://civitai.com/models/1409524/360degreetracking
  - *From: Ablejones*

- **Throwaway 1.3 LoRA** (lora)
  - https://huggingface.co/CCP6/throwaway-1.3-lora-for-kicks/tree/main
  - *From: JohnDopamine*

- **Wan prompting methodology guide** (guide)
  - https://www.mimicpc.com/learn/wan-ai-video-prompts-guide-for-text-to-video-generation
  - *From: Level Higher*

- **ChatGPT Wan2.1 Video Prompt Extender** (tool)
  - https://chatgpt.com/g/g-67c66b4ab8048191871c6e1240c5717a-wan2-1-video-prompt-extender
  - *From: 🏁🫰GridSnap*

- **Judy Hopps LoRA for Wan2.1 14B** (lora)
  - https://civitai.com/models/1133220?modelVersionId=1743913
  - *From: MisterMango*

- **Ghibli LoRA gallery** (lora)
  - Civitai page with 1947 clips
  - *From: seruva19*

- **ComfyUI Wan workflows** (workflow)
  - https://comfyanonymous.github.io/ComfyUI_examples/wan/
  - *From: ZombieMatrix*

- **TeaCache node** (node)
  - https://github.com/welltop-cn/ComfyUI-TeaCache
  - *From: ZombieMatrix*

- **CMake installer** (tool)
  - https://github.com/Kitware/CMake/releases/download/v4.0.2/cmake-4.0.2-windows-x86_64.msi
  - *From: ZombieMatrix*

- **Frutiger LoRA** (lora)
  - https://huggingface.co/dreamer8/FrutigerLora14B_Wan
  - *From: Dream Making*

- **UltraCascade native implementation** (repo)
  - https://github.com/ClownsharkBatwing/UltraCascade
  - *From: Clownshark Batwing*

- **Explosion LoRA** (lora)
  - https://civitai.com/models/1295945/huge-explosion-vfx-hunyuan-video-lora?modelVersionId=1588426
  - *From: JohnDopamine*

- **Realistic Fire LoRA** (lora)
  - https://civitai.com/models/1376174/realistic-fire-wan21-t2v-lora?modelVersionId=15549590
  - *From: JohnDopamine*

- **Wan 2.1 14B LoRAs collection** (collection)
  - https://huggingface.co/collections/Remade-AI/wan21-14b-t2v-loras-67dc73d82f66cfac2b4eb253
  - *From: ˗ˏˋ⚡ˎˊ-*

- **CausVid workflow** (workflow)
  - https://discord.com/channels/1076117621407223829/1342763350815277067/1372710585283645631
  - *From: ˗ˏˋ⚡ˎˊ-*

- **CausVid T2V LoRA for I2V** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/blob/main/Wan21_CausVid_14B_T2V_lora_rank32.safetensors
  - *From: JohnDopamine*

- **Fun Control 14B model** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/blob/main/Wan2.1-Fun-Control-14B_fp8_e4m3fn.safetensors
  - *From: 852話 (hakoniwa)*

- **FastVideo tiled attention** (repo)
  - https://github.com/hao-ai-lab/FastVideo
  - *From: deleted_user_2ca1923442ba*

- **Bullet time/camera orbiting LoRA** (lora)
  - https://civitai.com/models/1475368
  - *From: N0NSens*

- **Felted Flux LoRA** (lora)
  - https://civitai.com/models/1374456/felted-flux
  - *From: AJO*

- **LoRA training tutorial video** (tutorial)
  - https://youtu.be/mSvo7FEANUY?si=hcXagm_zUlRg9Kai&t=1263
  - *From: 138234075931475968*

- **VACE Skyreel GGUF 24fps** (model)
  - https://huggingface.co/QuantStack/SkyReels-V2-T2V-14B-720P-VACE-GGUF
  - *From: Vérole*

- **Phantom custom model** (model)
  - https://huggingface.co/CCP6/blahblah/tree/main
  - *From: Thom293*

- **Toon LoRA** (lora)
  - https://civitai.green/models/1613519?modelVersionId=1825996
  - *From: VRGameDevGirl84(RTX 5090)*

- **Raven Teen Titans LoRA** (lora)
  - https://civitai.com/models/1624734/raven-teen-titans-2003-lora-wan-21-14b-t2v-i2v?modelVersionId=1838873
  - *From: 138234075931475968*

- **Kijai's example workflows** (workflow)
  - https://github.com/kijai/ComfyUI-WanVideoWrapper/tree/main/example_workflows
  - *From: JohnDopamine*

- **Native ComfyUI Wan workflows** (workflow)
  - https://comfyanonymous.github.io/ComfyUI_examples/wan/
  - *From: JohnDopamine*

- **UniAnimate project** (repo)
  - https://unianimate.github.io/
  - *From: Guey.KhalaMari*

- **Remade AI LoRAs** (lora)
  - https://huggingface.co/Remade-AI
  - *From: Nekodificador*

- **Fluxtapoz techniques** (repo)
  - https://github.com/logtd/ComfyUI-Fluxtapoz
  - *From: Nekodificador*

- **JohnDopamine's merged Phantom model with speed LoRAs** (model)
  - https://huggingface.co/CCP6/blahblah/tree/main
  - *From: JohnDopamine*

- **CausVid version comparison discussion** (discussion)
  - https://old.reddit.com/r/StableDiffusion/comments/1l0jz1o/causvid_v2_help/mve6qsp/
  - *From: JohnDopamine*

- **PhazeiComfyUI CausVid workflow** (workflow)
  - https://civitai.com/articles/15189
  - *From: phazei*

- **Execution inversion for ComfyUI loops** (repo)
  - https://github.com/BadCafeCode/execution-inversion-demo-comfyui/tree/main
  - *From: hablaba*

- **Flowframes interpolation software** (tool)
  - https://nmkd.itch.io/flowframes
  - *From: GalaxyTimeMachine*

- **AJO's character consistency workflow** (workflow)
  - shared in chat
  - *From: AJO*

- **VRGameDevGirl84's Wan14B T2V Master Model** (model)
  - https://huggingface.co/vrgamedevgirl84/Wan14BT2V_MasterModel
  - *From: GalaxyTimeMachine (RTX4090)*

- **Kijai WanVideoWrapper example workflows** (workflow)
  - https://github.com/kijai/ComfyUI-WanVideoWrapper/tree/main/example_workflows
  - *From: GalaxyTimeMachine (RTX4090)*

- **AccVid I2V LoRA** (lora)
  - https://huggingface.co/Kijai/WanVideo_comfy/resolve/main/Wan21_AccVid_I2V_480P_14B_lora_rank32_fp16.safetensors?download=true
  - *From: 🦙rishappi*

- **Live Wallpaper LoRA** (lora)
  - https://civitai.com/models/1264662
  - *From: 211685818622803970*

- **Wan Technical Paper** (research)
  - https://arxiv.org/pdf/2503.20314
  - *From: ZombieMatrix*

- **ComfyUI-MMAudio by Kijai** (node)
  - https://github.com/kijai/ComfyUI-MMAudio
  - *From: 🦙rishappi*

- **WanArxiv ChatGPT Assistant** (tool)
  - https://chatgpt.com/g/g-68432d6927448191b122092b5148e329-wanarxiv
  - *From: VRGameDevGirl84(RTX 5090)*

- **VRGameDevGirl84's FusionX merge model** (model)
  - https://civitai.com/models/1651125
  - *From: VRGameDevGirl84(RTX 5090)*

- **VACE workflow with pose control** (workflow)
  - https://discord.com/channels/1076117621407223829/1373520070596231251
  - *From: VRGameDevGirl84(RTX 5090)*

- **CoTracker ComfyUI node** (repo)
  - https://github.com/s9roll7/comfyui_cotracker_node/blob/main/example.md
  - *From: tttADs*

- **Multi-image to video workflow** (workflow)
  - https://civitai.com/models/630602/multi-image-to-video-workflow-for-comfyui
  - *From: VRGameDevGirl84(RTX 5090)*

- **Zlikwid WAN LoRA v2** (model)
  - https://huggingface.co/Zlikwid/zlikwid_wan21_14b_v2
  - *From: Zlikwid*

- **Loop workflow** (workflow)
  - https://openart.ai/workflows/nomadoor/loop-anything-with-wan21-vace/qz02Zb3yrF11GKYi6vdu
  - *From: Jonathan*

- **HeyGem Open Source project** (tool)
  - https://github.com/duixcom/Duix.Heygem
  - *From: Vérole*

- **WAN 2.1 ComfyUI repackaged** (model)
  - https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/tree/main/split_files/diffusion_models
  - *From: Charlie*

- **VACE 14B GGUF** (model)
  - https://huggingface.co/QuantStack/Wan2.1-VACE-14B-GGUF
  - *From: TK_999*

- **VRGameDevGirl84's FusionX model** (model)
  - https://civitai.com/models/1651125
  - *From: VRGameDevGirl84(RTX 5090)*

- **Animated Wallpaper LoRA** (model)
  - https://civitai.com/models/1264662
  - *From: Yae*

- **Retro 90s Anime LoRA** (model)
  - https://civitai.com/models/1671285/retro-90s-anime-golden-boy-style-lora-wan-14b-t2v-i2v?modelVersionId=1891658
  - *From: 138234075931475968*

- **Audioreactive Everything** (tool)
  - https://discord.com/channels/1076117621407223829/1379114968028287106/1379114968028287106
  - *From: Thom293*

- **MultiTalk** (tool)
  - https://github.com/MeiGen-AI/MultiTalk
  - *From: The Shadow (NYC)*

- **Self-Forcing paper and demo** (research)
  - https://self-forcing.github.io/ and https://www.youtube.com/watch?v=v53Hdk1695Y
  - *From: SS*

- **FusionX model and LoRA** (model)
  - https://civitai.com/models/1651125?modelVersionId=1878555
  - *From: VRGameDevGirl84(RTX 5090)*

- **Wan Cinematic Video Prompt Generator** (tool)
  - https://chatgpt.com/g/g-67c3a6d6d19c81919b3247d2bfd01d0b-wan-cinematic-video-prompt-generator
  - *From: VRGameDevGirl84(RTX 5090)*

- **Golden Boy Style LoRA** (lora)
  - https://civitai.com/models/1671285/retro-90s-anime-golden-boy-style-lora-wan-14b-t2v-i2v?modelVersionId=1891658
  - *From: 138234075931475968*

- **Wan Knowledge Base** (documentation)
  - https://nathanshipley.notion.site/Wan-2-1-Knowledge-Base-1d691e115364814fa9d4e27694e9468f#1d691e115364811183bfd88310a50e31
  - *From: JohnDopamine*

- **ComfyUI Wan VACE Long Gen Helper** (tool)
  - https://github.com/s9roll7/comfyui_wan_vace_long_gen_helper
  - *From: tttADs*

- **Musubi Tuner for LoRA training** (tool)
  - https://github.com/kohya-ss/musubi-tuner
  - *From: MisterMango*

- **Musubi Tuner WAN trainer docs** (documentation)
  - https://github.com/kohya-ss/musubi-tuner/blob/main/docs/wan.md
  - *From: MisterMango*

- **Particle Grid Animator** (tool)
  - https://nathanshipley.github.io/particleGridAnimator/
  - *From: Nathan Shipley*

- **Phantom FusionX+NAG workflow** (workflow)
  - *From: SS*

- **ATI tutorial** (tutorial)
  - https://www.youtube.com/watch?v=7YmiJxPEMk0
  - *From: SS*

- **Fetishistic Giallo Video LoRA** (lora)
  - https://civitai.com/models/1455041/fetishisticgiallovideo?modelVersionId=1646423
  - *From: TK_999*

- **Self-Forcing LoRA prompts** (prompts)
  - https://github.com/guandeh17/Self-Forcing/tree/main/prompts
  - *From: 312993351307755520*

- **LightXv2 LoRA** (lora)
  - https://civitai.com/models/1634180?modelVersionId=1849754
  - *From: hicho*

- **Demoness LoRA** (lora)
  - https://civitai.com/models/1672509?modelVersionId=1910187
  - *From: izashin*

- **Music video via Wan Vace** (video)
  - https://youtu.be/MmvlgU_-bBc
  - *From: Level Higher*

- **1min Azmon video** (video)
  - https://youtu.be/hkwikAsKRkA?si=UiPvdmuv5I8PHp5e
  - *From: Yae*

- **FusionX LoRA workflow** (workflow)
  - https://civitai.com/models/1681541/workflows-for-wan21fusionx-loras
  - *From: Dream Making*

- **Electric Alien WAN LoRA** (lora)
  - https://huggingface.co/CCP6/electaln-wan/tree/main
  - *From: JohnDopamine*

- **FusionX with tweakable LoRAs** (workflow)
  - https://civitai.com/models/1690979
  - *From: VRGameDevGirl84(RTX 5090)*

- **360-Orbit LoRA** (lora)
  - https://huggingface.co/Remade-AI/360-Orbit/tree/main
  - *From: Dream Making*

- **Orbit LoRA (alternative)** (lora)
  - https://civitai.com/models/1379629
  - *From: Ablejones*

- **SepAudio tool** (tool)
  - https://github.com/fblissjr/sepaudio
  - *From: fredbliss*

- **Particle Grid Animator** (tool)
  - https://nathanshipley.github.io/particleGridAnimator/
  - *From: Nathan Shipley*

- **CoTracker node** (node)
  - https://github.com/s9roll7/comfyui_cotracker_node
  - *From: Nathan Shipley*

- **DiffTrack model** (model)
  - https://cvlab-kaist.github.io/DiffTrack/
  - *From: TK_999*

- **Color Correction LoRA V1** (lora)
  - https://civitai.com/models/1683455?modelVersionId=1905361
  - *From: 211685818622803970*

- **ComfyUI VideoUpscale_WithModel** (node)
  - https://github.com/ShmuelRonen/ComfyUI-VideoUpscale_WithModel
  - *From: The Shadow (NYC)*

- **1x-DeJPG-realplksr-otf upscale model** (model)
  - https://openmodeldb.info/models/1x-DeJPG-realplksr-otf
  - *From: The Shadow (NYC)*

- **Morphing Into Plushtoy LoRA** (lora)
  - https://civitai.com/models/1525175/wan-i2v-skyreels-i2v-morphing-into-plushtoy-trained-on-sr-v2-i2v
  - *From: JohnDopamine*

- **ComfyUI JankDiffuseHigh** (node)
  - https://github.com/blepping/comfyui_jankdiffusehigh
  - *From: TK_999*

- **Spline Path Control editor** (tool)
  - https://whatdreamscost.github.io/Spline-Path-Control/
  - *From: Jonathan*

- **Spline Path Control repo** (repo)
  - https://github.com/WhatDreamsCost/Spline-Path-Control
  - *From: Jonathan*

- **wanvideo_vid2vid_example_01.json** (workflow)
  - https://github.com/kijai/ComfyUI-WanVideoWrapper/blob/main/example_workflows/wanvideo_vid2vid_example_01.json
  - *From: chrisd0073*

- **SkyReels models diffusion-pipe support** (repo)
  - https://github.com/tdrussell/diffusion-pipe/commit/ed947867f363b7fa39596561ed2054b919cff2f6
  - *From: JohnDopamine*

- **mdkb workflows collection** (workflow)
  - https://markdkberry.com/workflows/footprints/
  - *From: mdkb*

- **Text to video workflow** (workflow)
  - https://civitai.com/models/1690979?modelVersionId=1913734
  - *From: AiGangster*

- **VRGameDevGirl image to vid workflow** (workflow)
  - https://civitai.com/models/1651125?modelVersionId=1882322
  - *From: el marzocco*

- **VRGameDevGirl FusionX workflows** (workflow)
  - https://civitai.com/models/1690979
  - *From: el marzocco*

- **ComfyUI-MultiGPU** (repo)
  - https://github.com/pollockjj/ComfyUI-MultiGPU
  - *From: el marzocco*

- **Realistic Fire WAN 2.1 T2V LoRA** (model)
  - https://civitai.com/models/1376174/realistic-fire-wan21-t2v-lora
  - *From: JohnDopamine*

- **Huge Explosion VFX LoRA** (model)
  - https://civitai.com/models/1295945/huge-explosion-vfx-hunyuan-video-lora
  - *From: JohnDopamine*

- **Retro 90s Anime Golden Boy Style LoRA** (model)
  - https://civitai.com/models/1671285/retro-90s-anime-golden-boy-style-lora-wan-14b-t2v-i2v?modelVersionId=1963359
  - *From: 138234075931475968*

- **VRGameDevGirl84 workflows** (workflow)
  - https://civitai.com/models/1736052?modelVersionId=1964792
  - *From: VRGameDevGirl84(RTX 5090)*

- **Wan2.1 VACE 14B quanto model** (model)
  - https://huggingface.co/DeepBeepMeep/Wan2.1/blob/main/wan2.1_Vace_14B_quanto_mfp16_int8.safetensors
  - *From: hicho*

- **WanVideoWrapper by Kijai** (node)
  - *From: VRGameDevGirl84(RTX 5090)*

- **Kijai's segment anything + VACE workflow** (workflow)
  - *From: Cseti*

- **MultiTalk V2V workflow** (workflow)
  - https://discord.com/channels/1076117621407223829/1342763350815277067/1387639570010607677
  - *From: AJO*

- **WAN FusionX FaceNaturalizer LoRA** (lora)
  - https://civitai.com/models/1755105/wanfusionxfacenaturalizer
  - *From: patientx*

- **FusionX merged model** (model)
  - https://civitai.com/models/1736052?modelVersionId=1964791
  - *From: patientx*

- **Hallett AI workflows** (workflow)
  - https://www.hallett-ai.com/workflows
  - *From: Sal TK FX*

- **VRGameDevGirl ComfyUI nodes** (node)
  - https://github.com/vrgamegirl19/comfyui-vrgamedevgirl
  - *From: patientx*

- **AI Windows WHL repository** (repo)
  - https://github.com/wildminder/AI-windows-whl
  - *From: JohnDopamine*

- **Retro 90s Anime LoRA** (lora)
  - https://civitai.com/models/1671285/retro-90s-anime-golden-boy-style-lora-wan-14b-t2v-i2v?modelVersionId=1963359
  - *From: el marzocco*

- **ThinkSound audio processing** (tool)
  - https://huggingface.co/spaces/FunAudioLLM/ThinkSound
  - *From: Vérole*

- **WAN and Skyreels text-to-image workflows** (workflow)
  - https://civitai.com/models/1742500/wan-and-skyreels-text-to-image-workflows
  - *From: l҈u҈c҈i҈f҈e҈r҈*

- **FusionX model** (model)
  - https://civitai.com/models/1651125?modelVersionId=1868891
  - *From: l҈u҈c҈i҈f҈e҈r҈*

- **Archive.org historic videos** (resource)
  - https://archive.org/search?query=subject%3A%22historic%22&sort=-downloads&and%5B%5D=mediatype%3A%22movies%22
  - *From: el marzocco*

- **3dsmax biped animation files** (resource)
  - https://3dsmaxdepot.com/bip-bvh-files/
  - *From: hicho*

- **Cascadeur animation software** (tool)
  - https://cascadeur.com/plans
  - *From: xwsswww*

- **Wan FusionX Lightning Workflow** (workflow)
  - https://civitai.com/models/1651125/wan2114bfusionx
  - *From: el marzocco*

- **Amber character LoRA** (lora)
  - https://civitai.com/models/1777474?modelVersionId=2011655
  - *From: hicho*

- **Pusa LoRA** (lora)
  - https://huggingface.co/Kijai/WanVideo_comfy/tree/main/Pusa
  - *From: Charlie*

- **Pusa GitHub repository** (repo)
  - https://github.com/Yaofang-Liu/Pusa-VidGen
  - *From: brbbbq*

- **LightX2V LoRA** (lora)
  - https://huggingface.co/Kijai/WanVideo_comfy/tree/main/Lightx2v
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Wan 2.1 VACE + ATI tutorial video** (tutorial)
  - https://youtu.be/OhKoh0CsVFo
  - *From: 455300561034543105*

- **Wan blog** (documentation)
  - https://wan.video/welcome?spm=a2ty_o02.30011076.0.0.6c9ee41eCcluqg
  - *From: hicho*

- **Minimax CineMation Prompter GPT** (tool)
  - https://chatgpt.com/g/g-71Fq47Ec6-minimax-cinemotion-prompter
  - *From: l҈u҈c҈i҈f҈e҈r҈*

- **Wan.video image section** (resource)
  - https://wan.video/
  - *From: hicho*

- **Simple Uni3C workflow** (workflow)
  - https://discord.com/channels/1076117621407223829/1342763350815277067/1396678821289398293
  - *From: Guey.KhalaMari*

- **Default VACE workflow** (workflow)
  - https://docs.comfy.org/tutorials/video/wan/vace#vace-video-to-video-workflow
  - *From: Qok*

- **Lenin LoRA** (lora)
  - huggingface
  - *From: VK (5080 128gb)*

- **ComfyUI VRGameDevGirl nodes** (repo)
  - https://github.com/vrgamegirl19/comfyui-vrgamedevgirl
  - *From: patientx*

- **X AI prompts** (resource)
  - https://x.com/TechieBySA/status/1948791863047033208
  - *From: hicho*

- **Wan 2.2 ComfyUI examples** (workflow)
  - https://comfyanonymous.github.io/ComfyUI_examples/wan22/
  - *From: GOD_IS_A_LIE*

- **Golden Boy LoRA training details** (model)
  - https://civitai.com/models/1671285
  - *From: 138234075931475968*

- **Music video using AI generation** (video)
  - https://youtu.be/SXJwFVMqoKQ?si=Kjo4COIasC6ImJqG
  - *From: RubyNian*

- **Kijai WanVideo ComfyUI models** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy_fp8_scaled
  - *From: 138234075931475968*

- **Kijai Wan wrapper workflows** (workflow)
  - https://github.com/kijai/ComfyUI-WanVideoWrapper/tree/main/example_workflows
  - *From: Janosch Simon*

- **Wan 2.2 camera terminology guide** (documentation)
  - https://alidocs.dingtalk.com/i/nodes/EpGBa2Lm8aZxe5myC99MelA2WgN7R35y
  - *From: TK_999*

- **VR 360 Panoramic for Flux** (model)
  - https://civitai.com/models/848337/vr-360-panoramic-for-flux
  - *From: 164879244210470913*

- **Wan 2.2 workflow fix** (workflow)
  - https://civitai.com/models/1819098?modelVersionId=2060207
  - *From: Fictiverse*

- **241 frame workflow** (workflow)
  - https://discord.com/channels/1076117621407223829/1275200677718659162/1399722305965260902
  - *From: orabazes*

- **Wan2.2-T2V-A14B-GGUF** (model)
  - https://huggingface.co/QuantStack/Wan2.2-T2V-A14B-GGUF/tree/main
  - *From: Cseti*

- **WAN 2.2 14B GGUF V2V workflow** (workflow)
  - https://huggingface.co/thaakeno46/ComfyUI-Workflows/blob/main/WAN%202.2%2014B%20(GGUF)%20V2V.json
  - *From: thaakeno*

- **EchoShot prompting technique** (repo)
  - https://github.com/D2I-ai/EchoShot
  - *From: NebSH*

- **Lo-Fi Sci-Fi AI-Slop episode 4** (video)
  - https://youtu.be/sl1_RU6qoT4?si=EAEPLfPgUo8KRPKE
  - *From: 559434151435042816*

- **Experimental Wan 2.2 Yoshiaki Kawajiri retro anime style LoRA** (lora)
  - https://civitai.com/models/1833906/experimental-wan22-yoshiaki-kawajiri-retro-anime-style
  - *From: tarn59*

- **bf16 14b-i2v model and mixed weights model** (model)
  - https://huggingface.co/maybleMyers/wan_files_for_h1111/tree/main
  - *From: Benjimon*

- **High noise version of anime style LoRA** (lora)
  - https://civitai.com/models/1833906?modelVersionId=2078569
  - *From: tarn59*

- **Ace Step for music generation** (tool)
  - https://github.com/ace-step/ACE-Step
  - *From: U̷r̷a̷b̷e̷w̷e̷*

- **SwarmUI for video generation** (tool)
  - https://swarmui.net/
  - *From: U̷r̷a̷b̷e̷w̷e̷*

- **OpenShot Video Editor** (tool)
  - https://www.openshot.org/
  - *From: U̷r̷a̷b̷e̷w̷e̷*

- **Lightning LoRAs v1.1** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/tree/main/Wan22-Lightning
  - *From: patientx*

- **Wan upscaler workflow** (workflow)
  - https://huggingface.co/thaakeno46/ComfyUI-Workflows/blob/main/WAN2.2_GGUF_UPSCALER_14B.json
  - *From: thaakeno*

- **NAG implementation** (repo)
  - https://github.com/ChenDarYen/Normalized-Attention-Guidance
  - *From: 401839506493538304*

- **VRDevGameGirl workflow** (workflow)
  - Shared in Wan Chatter area
  - *From: T2 (RTX6000Pro)*

- **Tool pipeline video** (tutorial)
  - https://youtu.be/ycSm_iBwkOw
  - *From: {clam}*

- **Updated Wan 2.2 5B model** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy_fp8_scaled/blob/main/TI2V/Wan2_1-TI2V-5B_fp8_e5m2_scaled_KJ.safetensors
  - *From: l҈u҈c҈i҈f҈e҈r҈*

- **LTXV Arcane Style LoRA** (lora)
  - https://civitai.com/models/1575766/ltxv-13b-lora-arcane-style
  - *From: Cseti*

- **LatentSync lip-sync tool** (tool)
  - https://github.com/bytedance/LatentSync
  - *From: CaptHook*

- **Prompt scheduling discussion** (discussion)
  - https://discord.com/channels/1076117621407223829/1342763350815277067/1401041090160758998
  - *From: AshmoTV*

- **Stand-In reference workflow** (workflow)
  - https://github.com/kijai/ComfyUI-WanVideoWrapper/blob/main/example_workflows/wanvideo_Stand-In_reference_example_01.json
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Stand-In LoRA repository** (repo)
  - https://github.com/WeChatCV/Stand-In
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Video upscale workflow** (workflow)
  - https://civitai.com/models/1714513/video-upscale-or-enhancer-using-wan-fusionx-ingredients?modelVersionId=1940207
  - *From: ManglerFTW*

- **Anime dataset reference** (model)
  - https://civitai.com/models/1671285
  - *From: 138234075931475968*

- **ComfyUI workflow** (workflow)
  - https://civitai.com/models/1824027?modelVersionId=2104669
  - *From: GalaxyTimeMachine*

- **Fantasy Portrait model** (model)
  - https://huggingface.co/acvlab/FantasyPortrait
  - *From: ManglerFTW*

- **WAN 2.1 Seamless Loop Workflow** (workflow)
  - https://civitai.com/models/1426572/wan-21-seamless-loop-workflow-i2v
  - *From: 777222267331543050*

- **Community chatbot with all Discord knowledge** (tool)
  - https://notebooklm.google.com/notebook/a08901b9-0511-4926-bbf8-3c86a12dc306?pli=1
  - *From: 𝕯𝖗. 𝕸𝖆𝖈𝖆𝖇𝖗𝖊 ☠*

- **WAN Video Wrapper example workflows** (workflow)
  - *From: ManglerFTW*

- **InfiniteTalk Repository** (repo)
  - https://github.com/MeiGen-AI/InfiniteTalk
  - *From: JohnDopamine*

- **WanVideoWrapper** (repo)
  - https://github.com/kijai/ComfyUI-WanVideoWrapper
  - *From: JohnDopamine*

- **WanVideoWrapper Example Workflows** (workflow)
  - https://github.com/kijai/ComfyUI-WanVideoWrapper/tree/main/example_workflows
  - *From: JohnDopamine*

- **FLF2V workflow** (workflow)
  - https://github.com/kijai/ComfyUI-WanVideoWrapper/blob/main/example_workflows/wanvideo_FLF2V_720P_example_02.json
  - *From: NebSH*

- **Animation breakdown video** (tutorial)
  - https://www.youtube.com/watch?v=fwSuZpMq3QQ
  - *From: Desto Geima*

- **Wan VACE experiment** (tutorial)
  - https://www.reddit.com/r/StableDiffusion/comments/1mwa53y/experimenting_with_wan_21_vace/
  - *From: ThatVideoGuy*

- **WAN2.2 Continuous Generation Subgraphs** (workflow)
  - https://civitai.com/models/1866565/wan22-continous-generation-subgraphs
  - *From: NebSH*

- **InfiniteTalk models** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/tree/main/InfiniteTalk
  - *From: DawnII*

- **WAN2.2-14B-Rapid-AllInOne** (model)
  - https://huggingface.co/Phr00t/WAN2.2-14B-Rapid-AllInOne
  - *From: 1048309186322243594*

- **Italian Story with Wan 2.2** (example)
  - https://youtu.be/VpC1nN6yqOA
  - *From: 3DBicio*

- **Orbit shot LoRA** (lora)
  - https://huggingface.co/ostris/wan22_i2v_14b_orbit_shot_lora/tree/main
  - *From: 128578659047964672*

- **VibeVoice ComfyUI implementation** (repo)
  - https://github.com/wildminder/ComfyUI-VibeVoice
  - *From: JohnDopamine*

- **TTS Audio Suite with VibeVoice** (repo)
  - https://github.com/diodiogod/TTS-Audio-Suite
  - *From: BecauseReasons*

- **Upscaling workflow tutorial** (workflow)
  - https://www.youtube.com/watch?v=ViBnJqoTwig
  - *From: mdkb*

- **Pusa LoRA for Wan 2.2** (lora)
  - https://huggingface.co/RaphaelLiu/Pusa-Wan2.2-V1
  - *From: .: Not Really Human :.*

- **WanFaceDetailer Reddit Post** (tool)
  - https://www.reddit.com/r/StableDiffusion/comments/1n5zwzu/wanfacedetailer/
  - *From: 1048309186322243594*

- **Qwen Image Edit InStyle** (model)
  - https://huggingface.co/peteromallet/Qwen-Image-Edit-InStyle
  - *From: pom*

- **Wan 2.2 Lightning LoRA** (lora)
  - https://huggingface.co/lightx2v/Wan2.2-Lightning
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Wan 2.2 T2V I2V Kijai's Wrapper Workflow** (workflow)
  - https://civitai.com/models/1824027/wan-22-t2v-i2v-kijais-wrapper-workflow-k3nk
  - *From: el marzocco*

- **Kijai's Pusa extension workflow** (workflow)
  - https://github.com/kijai/ComfyUI-WanVideoWrapper/blob/main/example_workflows/wanvideo_2_2_14B_Pusa_extension_example_01.json
  - *From: 391574267306704897*

- **Lightx2v Wan 2.2 Lightning discussion** (discussion)
  - https://huggingface.co/lightx2v/Wan2.2-Lightning/discussions/30#68ac62ad87f7967db83badfd
  - *From: ˗ˏˋ⚡ˎˊ-*

- **PUSA technique website** (technique)
  - https://yaofang-liu.github.io/Pusa_Web/
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Reddit post on artistic prompting with Wan** (discussion)
  - https://www.reddit.com/r/StableDiffusion/comments/1n8l9ph/wan_gets_artistic_if_prompted_in_verse/
  - *From: The Shadow (NYC)*

- **Puza tutorial video** (tutorial)
  - https://youtu.be/Lu_WgtRP-0w
  - *From: hicho*

- **Terminator 2 T-1000 reference scene** (reference)
  - https://www.youtube.com/watch?v=gwxbr9iDhYs
  - *From: Dever*

- **Wan 2.2 MPS/HPS LoRAs** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/tree/main/Wan22_FunReward
  - *From: mdkb*

- **ComfyUI Wan Prompt Generator (English)** (repo)
  - https://github.com/GalaxyTimeMachine/ComfyUI-wan-prompt-generator
  - *From: GalaxyTimeMachine (RTX4090)*

- **VRGameDevGirl84 DEV branch** (repo)
  - https://github.com/vrgamegirl19/comfyui-vrgamedevgirl/tree/Dev
  - *From: VRGameDevGirl84(RTX 5090)*

- **Clip.cafe** (tool)
  - https://clip.cafe/
  - *From: U̷r̷a̷b̷e̷w̷e̷*

- **USDU upscaling workflow** (workflow)
  - https://discord.com/channels/1076117621407223829/1342763350815277067/1413545261027950682
  - *From: 153803064858378240*

- **InfiniteTalk V2V workflow** (workflow)
  - https://github.com/kijai/ComfyUI-WanVideoWrapper/blob/main/example_workflows/wanvideo_InfiniteTalk_V2V_example_02.json
  - *From: U̷r̷a̷b̷e̷w̷e̷*

- **UVR5 vocal separation** (tool)
  - https://github.com/Anjok07/ultimatevocalremovergui
  - *From: U̷r̷a̷b̷e̷w̷e̷*

- **Audio clip sources** (resource)
  - https://clip.cafe/ and https://movie-sounds.org/
  - *From: U̷r̷a̷b̷e̷w̷e̷*

- **Hunyuan Foley** (model)
  - https://github.com/Tencent-Hunyuan/HunyuanVideo-Foley
  - *From: Dever*

- **VACE model testing workflow** (workflow)
  - Reference to discord message about FakeVace merges
  - *From: JohnDopamine*

- **HuMo endless workflow** (workflow)
  - https://discord.com/channels/1076117621407223829/1417710283945672764
  - *From: VRGameDevGirl84(RTX 5090)*

- **Wan 2.2 Mega Rapid AIO** (workflow)
  - https://discord.com/channels/1076117621407223829/1417271949351981056
  - *From: garbus*

- **WAN Animate HuggingFace Space** (model)
  - https://huggingface.co/spaces/Wan-AI/Wan2.2-Animate
  - *From: 168373586812207104*

- **VACE context window workflow** (workflow)
  - https://discord.com/channels/1076117621407223829/1386453178240733235/1418215699297472582
  - *From: Vérole*

- **Google Drive video sample** (resource)
  - https://drive.google.com/file/d/1Jc99kh5k7E0jDsz4EXGS_Jlj0U7kgXWS/view?usp=sharing
  - *From: 151330553629638656*

- **Humo long generation workflow** (workflow)
  - https://discord.com/channels/1076117621407223829/1417710283945672764
  - *From: VRGameDevGirl84(RTX 5090)*

- **Video upscaler workflow** (workflow)
  - https://discord.com/channels/1076117621407223829/1393656203241979924
  - *From: JohnDopamine*

- **ACE-Step GitHub** (repo)
  - https://github.com/ace-step/ACE-Step?tab=readme-ov-file
  - *From: The Shadow (NYC)*

- **VRGameDevGirl84's music video workflow** (workflow)
  - https://discord.com/channels/1076117621407223829/1417710283945672764
  - *From: 1348584179440418868*

- **Video upscaling workflow** (workflow)
  - https://discord.com/channels/1076117621407223829/1342763350815277067/1413545261027950682
  - *From: 153803064858378240*

- **Wan 2.5 testing** (tool)
  - https://wavespeed.ai/collections/wan-2-5
  - *From: s2k*

- **Wan prompt generator resources** (tool)
  - https://discord.com/channels/1076117621407223829/1400081347678306304
  - *From: 1348584179440418868*

- **Official Wan guide** (documentation)
  - https://alidocs.dingtalk.com/i/nodes/EpGBa2Lm8aZxe5myC99MelA2WgN7R35y
  - *From: 1348584179440418868*

- **Wan official website** (tool)
  - https://wan.video/
  - *From: Tonon*

- **Wan 2.5 generation** (tool)
  - https://Create.wan.video/generate
  - *From: DawnII*

- **ToonComposer** (tool)
  - https://tooncomposer.com/
  - *From: GOD_IS_A_LIE*

- **ToonComposer installation tutorial** (tutorial)
  - https://www.youtube.com/watch?v=LRYa8oS6-Mk
  - *From: GOD_IS_A_LIE*

- **ToonComposer professional animation explanation** (tutorial)
  - https://m.youtube.com/watch?v=bk11g3hZX5s&time_continue=101&source_ve_path=NzY3NTg&embeds_referring_euri=https%3A%2F%2Fwww.google.com%2F
  - *From: GOD_IS_A_LIE*

- **Humo and Chroma1 Radiance support blog** (documentation)
  - https://blog.comfy.org/p/humo-and-chroma1-radiance-support
  - *From: Vérole*

- **ComfyUI HuMo I2V pull request** (repo)
  - https://github.com/comfyanonymous/ComfyUI/pull/10034
  - *From: Juan Gea*

- **Dyno model** (model)
  - https://huggingface.co/lightx2v/Wan2.2-Lightning/tree/main/Wan2.2-T2V-A14B-4steps-250928-dyno
  - *From: asd*

- **Kijai fp8 Dyno** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy_fp8_scaled/tree/main/T2V
  - *From: asd*

- **Wan22-Lightning LoRAs** (lora)
  - https://huggingface.co/Kijai/WanVideo_comfy/tree/main/LoRAs/Wan22-Lightning
  - *From: Bleedy (Madham)*

- **WanAnimate relight lora** (lora)
  - https://huggingface.co/AtelierDarren/Wan2.2_Animate/blob/main/WanAnimate_relight_lora_fp16.safetensors
  - *From: 246646497129660416*

- **3-Sampler I2V workflow** (workflow)
  - *From: garbus*

- **VACE 2.2 transition workflow** (workflow)
  - https://discord.com/channels/1076117621407223829/1423047061808615645
  - *From: ingi // SYSTMS*

- **Wan22-Lightning LoRAs** (lora)
  - https://huggingface.co/Kijai/WanVideo_comfy/tree/main/LoRAs/Wan22-Lightning
  - *From: hicho*

- **Indiana Jones LoRA for Wan** (lora)
  - https://huggingface.co/CCP6/indy/blob/main/Indy-Wan2.1-t2v-Trigger-is-ohwx%20person.safetensors
  - *From: JohnDopamine*

- **ComfyUI-Ovi workflow** (workflow)
  - https://github.com/snicolast/ComfyUI-Ovi/tree/main/workflow_example
  - *From: Anchorite*

- **Ovi ComfyUI implementation** (repo)
  - https://www.reddit.com/r/StableDiffusion/comments/1nzzlsp/comfyuiovi_no_flash_attention_required/
  - *From: Anchorite*

- **Kinestasis LoRA** (model)
  - https://huggingface.co/Cseti/wan2.2-14B-Kinestasis_concept-lora-v1
  - *From: 800884790713647164*

- **MMAudio ComfyUI integration** (repo)
  - https://github.com/kijai/ComfyUI-MMAudio
  - *From: Vérole*

- **Upscaling workflow** (workflow)
  - https://discord.com/channels/1076117621407223829/1423587284321566760
  - *From: ingi // SYSTMS*

- **ComfyUI upscale workflows collection** (workflow)
  - https://discord.com/channels/1076117621407223829/1373291419434877078
  - *From: 800884790713647164*

- **RyanOnTheInside reactive audio nodes** (repo)
  - https://github.com/ryanontheinside/ComfyUI
  - *From: yukass*

- **WAN resources page** (workflow)
  - https://discord.com/channels/1076117621407223829/1373291419434877078
  - *From: 132313738710614016*

- **Next Scene QWEN Image LoRA** (model)
  - https://huggingface.co/lovis93/next-scene-qwen-image-lora-2509
  - *From: mdkb*

- **Google Maps 3D scene creation tutorial** (tutorial)
  - https://www.youtube.com/watch?v=OhMP4X79JW8
  - *From: mdkb*

- **Cosmos native ComfyUI tutorial** (tutorial)
  - https://docs.comfy.org/tutorials/video/cosmos/cosmos-predict2-video2world
  - *From: BestWind*

- **NVIDIA Cosmos models** (model)
  - https://build.nvidia.com/search?q=%22cosmos%22+-nemotron&ncid=no-ncid
  - *From: BestWind*

- **WaveSpeed AI LoRA trainer** (tool)
  - https://wavespeed.ai/models/wavespeed-ai/wan-2.2-i2v-lora-trainer
  - *From: NebSH*

- **mdkb's workflow collection** (workflow)
  - https://markdkberry.com/workflows/research/
  - *From: mdkb*

- **GoWithTheFlow discussion** (workflow)
  - https://discord.com/channels/1076117621407223829/1371060071328645191
  - *From: Dream Making*

- **Rick and Morty style LoRA** (lora)
  - https://huggingface.co/DeverStyle/rick-and-morty-style-wan-21
  - *From: Dever*

- **VRGameDevGirl's workflows and custom nodes** (repo)
  - https://github.com/vrgamegirl19/comfyui-vrgamedevgirl/tree/main
  - *From: VRGameDevGirl84(RTX 5090)*

- **WanAnimate preprocess workflow** (workflow)
  - https://github.com/kijai/ComfyUI-WanVideoWrapper/blob/main/example_workflows/wanvideo_WanAnimate_preprocess_example_02.json
  - *From: AR*

- **Ultra realistic WAN 2.2 example** (example)
  - https://www.reddit.com/r/StableDiffusion/comments/1oanats/wan_22_realism_motion_and_emotion/
  - *From: 481339785513009152*

- **Lightx2v Wan2.2 Distill LoRAs** (model)
  - https://huggingface.co/lightx2v/Wan2.2-Distill-Loras/tree/main
  - *From: Tachyon*

- **HoloCine repository** (repo)
  - https://github.com/yihao-meng/HoloCine/blob/main/HoloCine_inference_full_attention.py
  - *From: Benjimon*

- **Holocine Reddit discussion** (resource)
  - https://www.reddit.com/r/StableDiffusion/comments/1oemcri/holocine_holistic_generation_of_cinematic/
  - *From: s2k*

- **Stable Video Infinity** (repo)
  - https://github.com/vita-epfl/Stable-Video-Infinity
  - *From: avataraim*

- **Wan 2.5 platform** (tool)
  - https://create.wan.video/generate
  - *From: hicho*

- **ComfyUI LM Studio image to text node** (node)
  - https://github.com/mattjohnpowell/comfyui-lmstudio-image-to-text-node
  - *From: hicho*

- **Cinematic hard cut LoRA** (lora)
  - https://civitai.com/models/2088559?modelVersionId=2376295
  - *From: Ablejones*

- **Wan 2.2 Lightx2v LoRA** (lora)
  - https://huggingface.co/Kijai/WanVideo_comfy/blob/main/LoRAs/Wan22_Lightx2v/Wan_2_2_I2V_A14B_HIGH_lightx2v_4step_lora_v1030_rank_64_bf16.safetensors
  - *From: hicho*

- **Music video creation workflow** (workflow)
  - https://www.reddit.com/r/StableDiffusion/comments/1osi1q0/wan_22_more_motion_more_emotion/
  - *From: 481339785513009152*

- **Jujutsu Kaisen Anime LoRA for Wan 2.2** (lora)
  - https://civitai.com/models/2114480/jujutsu-kaisen-anime-lora-wan-video-22-t2v
  - *From: samurzl*

- **No Mercy music video using Wan ecosystem** (video)
  - https://youtu.be/dPPR5NSGxo4?si=YcKA4c85uPwbBy0Z
  - *From: Gateway {Dreaming Computers}*

- **Kling AI vs Custom Workflow benchmark article** (article)
  - https://medium.com/@lydie_cd/i-benchmarked-kling-ai-against-my-custom-workflow-heres-what-actually-won-e7848ac6cd0b
  - *From: Lydie Decat*

- **VisualFrisson's Wanimate workflow** (workflow)
  - *From: Charlie*

- **WanExperiments pack by Ablejones** (repo)
  - github.com/drozbay/WanExperiments
  - *From: Ablejones*

- **CineScale upscaling tool** (repo)
  - https://github.com/Eyeline-Labs/CineScale
  - *From: harryB*

- **Exploded effect LoRA** (model)
  - https://huggingface.co/Ashmotv/exploded_effect_wan
  - *From: AshmoTV*

- **WanExperiments custom implementation** (repo)
  - https://github.com/drozbay/WanExperiments
  - *From: Ablejones*

- **ComfyUI SAM3 implementation** (repo)
  - https://github.com/wouterverweirder/comfyui_sam3
  - *From: JohnDopamine*

- **WanVaceAdvanced node pack** (repo)
  - https://github.com/drozbay/ComfyUI-WanVaceAdvanced
  - *From: Ablejones*

- **Wan22-Lightning LoRAs** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/tree/main/LoRAs/Wan22-Lightning/old
  - *From: asd*

- **Hard Cut LoRA** (lora)
  - https://civitai.com/models/2088559?modelVersionId=2446376
  - *From: Ablejones*

- **SVI LoRAs for ComfyUI** (lora)
  - https://huggingface.co/Kijai/WanVideo_comfy/tree/main/LoRAs/Stable-Video-Infinity
  - *From: Ablejones*

- **WanKeyframeBuilder** (repo)
  - https://github.com/ckinpdx/ComfyUI-WanKeyframeBuilder
  - *From: Chandler*

- **TrentNodes with VACE keyframe builder** (repo)
  - https://github.com/TrentHunter82/TrentNodes
  - *From: Flipping Sigmas*

- **WanVaceAdvanced nodes** (repo)
  - https://github.com/drozbay/ComfyUI-WanVaceAdvanced
  - *From: Ablejones*

- **WanExperiments repository** (repo)
  - https://github.com/drozbay/WanExperiments
  - *From: Ablejones*

- **H1111 SVI implementation** (repo)
  - https://github.com/maybleMyers/H1111/tree/svi
  - *From: Benjimon*

- **Water morphing LoRA** (lora)
  - https://huggingface.co/Ashmotv/water_morping_wan
  - *From: AshmoTV*

- **Technically Color WAN LoRA** (lora)
  - https://civitai.com/models/2106471?modelVersionId=2383077
  - *From: hicho*

- **HuMo workflow** (workflow)
  - https://discord.com/channels/1076117621407223829/1417710283945672764
  - *From: 152993277631528960*

- **VACE inpainting tutorial example** (tutorial)
  - https://cdn.discordapp.com/attachments/1342763350815277067/1408110821904744528/WanVideoWrapper_VACE_startendframe_00002_3.mp4
  - *From: chrisd0073*

- **VFI tool for motion smoothing** (tool)
  - https://wanx-troopers.github.io/vfi.html
  - *From: 800884790713647164*

- **FMML/Humo automation workflow** (workflow)
  - https://discord.com/channels/1076117621407223829/1417710283945672764
  - *From: VRGameDevGirl84(RTX 5090)*

- **WanSoundTrajectory node** (tool)
  - https://github.com/ckinpdx/ComfyUI-WanSoundTrajectory
  - *From: Ablejones*

- **VACE clip joiner workflow** (workflow)
  - https://civitai.com/models/2024299
  - *From: Vérole*

- **Exploded effect LoRA** (lora)
  - https://huggingface.co/Ashmotv/exploded_effect_wan
  - *From: pom*

- **WanVaceAdvanced repository** (repo)
  - https://github.com/drozbay/ComfyUI-WanVaceAdvanced
  - *From: Ablejones*

- **Context windows documentation** (documentation)
  - https://wanx-troopers.github.io/what-plugs-where/context-windows.html
  - *From: 800884790713647164*

- **Vace Fun 22 GGUF model** (model)
  - https://huggingface.co/QuantStack/Wan2.2-VACE-Fun-A14B-GGUF/tree/main
  - *From: Vérole*

- **WanVideoWrapper workflow** (workflow)
  - https://discord.com/channels/1076117621407223829/1455601193660452995/1455601385755115550
  - *From: Ablejones*

- **SVI 2.2 Pro LoRAs** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/tree/main/LoRAs/Stable-Video-Infinity/v2.0
  - *From: JohnDopamine*

- **KJ's subgraph workflow** (workflow)
  - https://discord.com/channels/1076117621407223829/1342763350815277067/1454805653599031358
  - *From: JohnDopamine*

- **AshmoTV's LoRA thread** (resource)
  - https://discord.com/channels/1076117621407223829/1448704169958576188
  - *From: AshmoTV*

- **HuMo extension workflow** (workflow)
  - https://discord.com/channels/1076117621407223829/1455601193660452995
  - *From: 152993277631528960*

- **Qwen Image Edit LoRA for inflatable effects** (lora)
  - https://discord.com/channels/1076117621407223829/1461424284810481774
  - *From: ingi // SYSTMS*

- **ComfyUI_Yvann-Nodes audio reactive plugin** (tool)
  - https://github.com/yvann-ba/ComfyUI_Yvann-Nodes
  - *From: 439811659729469441*

- **Beat editor tutorial video** (tutorial)
  - https://youtu.be/sjX6fcoxDII?si=33kFg_ARc4r3p_eQ
  - *From: VRGameDevGirl84(RTX 5090)*


## Known Limitations

- **High motion causes garbling**
  - High motion scenes tend to produce garbled results, especially with fp8 model
  - *From: BecauseReasons*

- **Cars pass through objects**
  - Multiple instances of vehicles phasing through trash cans and other objects during generation
  - *From: Screeb*

- **Looping artifacts above 81 frames**
  - Generating more than 81 frames tends to produce looping artifacts
  - *From: Juampab12*

- **V2V at 0.05 noise doesn't work well for long sequences**
  - Low noise settings fail with many frames in V2V upscaling workflow
  - *From: DiXiao*

- **Poor text rendering**
  - Model struggles with generating readable text in scenes
  - *From: DawnII*

- **Degradation at long durations**
  - Last frames become bad when running 91 frames or longer sequences
  - *From: ingi // SYSTMS*

- **Strange dots and murky appearance up close**
  - Everything looks dot-matrix like when zoomed in, caused by low-res and precision errors
  - *From: BecauseReasons*

- **Poor small detail invention**
  - Doesn't invent small details well, needs quality realistic input
  - *From: ShiftingDimensionsAI*

- **Anime/2D struggles**
  - Animation I2V services struggle with good motion for 2D drawings compared to realistic I2V
  - *From: ShiftingDimensionsAI*

- **Red squares at high resolution**
  - Wan 1.3B generates red squares at 1776x1776 and higher resolutions
  - *From: DiXiao*

- **TeaCache and context incompatibility**
  - Cannot use TeaCache with context options enabled
  - *From: NebSH*

- **Character consistency issues**
  - Character consistency can fall apart during generation
  - *From: BecauseReasons*

- **AMD/Zluda optimization issues**
  - Missing optimizations that Nvidia gets, GGUF nodes don't free VRAM on AMD
  - *From: Screeb*

- **Model struggles with hippos**
  - Wan 2.1 doesn't generate hippos well
  - *From: Kijai*

- **Anime style images don't work well**
  - Poor results when using anime-style input images
  - *From: aikitoria*

- **LoRAs incompatible with TEACache in native workflow**
  - Must disable TEACache when using LoRAs with native ComfyUI implementation
  - *From: Fred*

- **Effect LoRAs are hit and miss**
  - Inflate/deflate LoRAs don't always work as expected, require seed lottery
  - *From: burgstall*

- **Gender transformation LoRA poor quality**
  - Gender transformation LoRA described as 'shit' quality
  - *From: burgstall*

- **LoRA mixing generally unsuccessful**
  - Users report failed attempts at mixing multiple LoRAs together
  - *From: N0NSens*

- **Cross-resolution LoRA compatibility issues**
  - LoRAs trained on 720p may not work well on 480p models, quality drops with artifacts
  - *From: 211685818622803970*

- **T2V produces plastic/fake skin appearance**
  - T2V generations often have artificial-looking skin texture
  - *From: 263709484742868993*

- **Loop-args feature destroys video quality**
  - Known issue that disabling teacache partially fixes but still looks weird on I2V
  - *From: 192951193763315712*

- **Context looping not good at small frame counts**
  - 81 frame loops don't work well, need larger context like 169 frames
  - *From: Kijai*

- **I2V looping has alignment issues**
  - Never had much luck with I2V for looping, works better with T2V
  - *From: Kijai*

- **Depth control not responsive to fast movements**
  - WAN Depth Control Lora follows structure well but struggles with rapid motion
  - *From: irregularsizes*

- **Camera motion training requires identical movement**
  - Slight variations in camera movement across training data make learning difficult
  - *From: ArtOfficial*

- **Single frame video generation issues**
  - Cannot generate single frame videos (images) - outputs show black in Kijai workflow
  - *From: wayward_18*

- **Gun firing actions difficult to prompt**
  - Prompts for 'shooting a xyz' rarely result in actual gun firing animation
  - *From: Ghost*

- **PULID/Ace++ struggle with consistent clothing variations**
  - Face consistency tools have difficulty maintaining character likeness when clothing differs from reference
  - *From: AJO*

- **Control LoRA bias toward realism**
  - Skews really hard to realism, need LoRAs to push to other styles
  - *From: Fill*

- **Last frame chaining reliability**
  - Can't guarantee subject's face is in last frame each time, leads to nonsense output
  - *From: AJO*

- **Wan online service usage limit**
  - Only 5 generations per day limit
  - *From: 133784166977372160*

- **Last frame condition color issues**
  - If you encode first/last frame with gray frames in between like a proper inpaint model, the colors get screwed up at the end
  - *From: spacepxl*

- **Low fps tracking for fast movements**
  - The limitation is low fps to track fast paced movements, need to slow down input to counteract
  - *From: DawnII*

- **16fps limitation for inference**
  - The weakness is low fps for tracking fast paced movements during inference
  - *From: DawnII*

- **Last few frames flash brighter**
  - Last few frames flash brighter or higher contrast, similar to color issues with improper frame conditioning
  - *From: spacepxl*

- **WAN starts hitting ceiling around 1.5MP resolution**
  - 2500x500 works well at 1.2MP, but pushing to 3000x600 gives less reliable results
  - *From: ZombieMatrix*

- **VACE adds significant compute overhead**
  - Makes it hard to do anything over 1280 on longest edge with 4090 local setup
  - *From: Kytra*

- **LTXV doesn't handle tall panoramic shots well**
  - Unlike wide shots which work fine, tall pano shots cause issues with LTXV
  - *From: ZombieMatrix*

- **Custom blender rigs not ideal for pose control**
  - Hands don't always match up and it ignores mouth/eyes, just follows the chin
  - *From: Kytra*

- **Noise on long generations**
  - Getting noise on long generations, unclear if more steps help or if it's limitation until full model
  - *From: TimHannan*

- **First frame issues with VACE**
  - Not sure what is causing problems with first frames in VACE generations
  - *From: TimHannan*

- **14B Fun Control can't daisy chain**
  - Unlike VACE, 14B fun control cannot be daisy chained
  - *From: DawnII*

- **Hi-res LoRAs may over-process**
  - New hi-res LoRAs increase sharpness but may add too much contrast and saturation
  - *From: Jas*

- **DG model struggles with VACE for realistic results**
  - Regular T2V model works better with VACE than DG model
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Long videos in one pass 'kinda sucks but not completely broken'**
  - Quality degrades for very long single-pass generations
  - *From: Benjimon*

- **Difficulty getting balance between good motion and good quality in I2V**
  - Especially challenging with anime styled images
  - *From: TK_999*

- **Skyreels ignores spatial interactions**
  - Model completely ignores spatial interactions, causes deformation after falling actions
  - *From: ezMan*

- **Style consistency issues**
  - Model doesn't stick with consistent style across generation
  - *From: HUBERT THE ADVENTURER*

- **1.3B model temporal degradation**
  - Degrades faster over time compared to 14B, especially on distant objects
  - *From: Ablejones*

- **FLF2V doesn't support non-standard aspect ratios**
  - First-Frame-Last-Frame to Video doesn't work with unusual aspect ratios
  - *From: ezMan*

- **Quality degradation in long generations**
  - 1.3B model degrades more than 14B in long generation attempts, even with proper overlap settings
  - *From: Ablejones*

- **Sampling can't fix poor model weights**
  - Good sampling only gets the absolute best out of the model, can't fix weights that are really far from being able to do something
  - *From: Clownshark Batwing*

- **Scene divergence in long videos**
  - Without reference to previous generations or initial video/image, scenes diverge quickly in long video generation
  - *From: Ablejones*

- **Video length context loss**
  - Longer videos start losing context quickly, especially at far edges. Fence posts don't retain patterns in longer generations
  - *From: ZombieMatrix*

- **VACE frame limitation**
  - VACE chops off a frame from input, can cause issues if not corrected
  - *From: 88822364468412416*

- **Resolution vs length tradeoff**
  - Higher resolution scenes lose context more rapidly than smaller ones due to too much to keep track of
  - *From: ZombieMatrix*

- **T2V current usefulness**
  - T2V is pretty useless at current stage of development
  - *From: N0NSens*

- **Camera control inconsistency**
  - Wan often tries to make handheld camera movement regardless of prompts, camera prompts work inconsistently
  - *From: N0NSens*

- **Scene change capability**
  - Wan's scene changes are reportedly not as good as Hunyuan's
  - *From: DiXiao*

- **Depth control for 3D objects**
  - Circular objects treated as flat circles, doesn't understand 3D rotation even with clear prompts when depth is involved
  - *From: Đỗ Quốc Hưng - Team 05*

- **Hunyuan has hard resolution limit**
  - Hard max around 2500 pixels in either direction, probably max total pixels
  - *From: ZombieMatrix*

- **High resolution generations extremely slow**
  - 5000 pixels wide takes 8+ hours, may not complete step 1
  - *From: ZombieMatrix*

- **LoRAs don't work well with CausVid**
  - Explosion and fire LoRAs produce garbage results with CausVid
  - *From: JohnDopamine*

- **SkyReels doesn't work well with VACE**
  - Compatibility issues between SkyReels model and VACE
  - *From: JohnDopamine*

- **Wan quality decreases over 80-100 frames**
  - Quality decrease and weird staring frames at longer durations
  - *From: 88822364468412416*

- **LoRA likeness bleeding to multiple people**
  - If there are background people or 2 people, they'll both pick up the likeness from LoRA
  - *From: JohnDopamine*

- **Style LoRAs finicky with VACE**
  - Style LoRA worked in simple t2v workflow but not doing much in VACE workflow
  - *From: JohnDopamine*

- **MoviiGen resistant to funky sampler combinations**
  - Seemed resistant to doing funky stuff with clown guides or some sampler/scheduler combos
  - *From: TK_999*

- **Fantasy Talk movement stiffness**
  - Found it difficult to master because movements were very stiff
  - *From: 852話 (hakoniwa)*

- **Wan resolution breaking point**
  - Going higher than 10.48MP (7280x1440) seems close to breaking point for Wan
  - *From: ZombieMatrix*

- **Pose detection with stylized characters**
  - Pose detection doesn't always work well with stylized characters
  - *From: Guey.KhalaMari*

- **Character likeness degrades with longer sequences**
  - Lost character likeness when generating 161 frames with context windows
  - *From: A.I.Warper*

- **Pose detection doesn't work on animated characters**
  - DWPose fails to detect poses on animated character references
  - *From: Guey.KhalaMari*

- **Hair control becomes unpredictable beyond 49 frames**
  - Art direction of hair using scribble control becomes unpredictable beyond 49 frames
  - *From: Guey.KhalaMari*

- **Smoking effects don't work well**
  - Smoking effects cause issues across multiple AI video models including Wan
  - *From: Sebastian Torres*

- **VACE doesn't work well with person-shaped masks**
  - Tries to fill person-shaped masks with people, needs rectangular masks instead
  - *From: ArtOfficial*

- **CausVid V2 quality issues**
  - Makes outputs darker and less detailed compared to V1
  - *From: Thom293*

- **Face reference gets too small in full body shots**
  - When using full body reference images, face becomes too small and loses likeness
  - *From: AJO*

- **Context window bleeding at 81 frames**
  - Model starts recognizing humans and interferes with abstract style transfer
  - *From: Zlikwid*

- **VACE is very memory intensive**
  - Requires blockswap to prevent VRAM overflow, removing blockswap gives minimal speed boost but risks OOM
  - *From: MysteryShack*

- **Sampler doesn't support 1920x1080 resolution**
  - Higher resolutions may not be supported by current sampler implementations
  - *From: fearnworks*

- **Context options don't always allow longer frame generation**
  - May still hit VRAM limits even with context settings enabled
  - *From: humangirltotally*

- **Full T2V produces less motion without input video**
  - Using denoiser 0.5 with input video provides better motion than pure T2V
  - *From: hicho*

- **Context windows change appearance**
  - Can't do shorter frames to preview what longer generation will look like using context windows - will look different in first frame even with same seed
  - *From: Zlikwid*

- **Prompting in Phantom very different from normal T2V**
  - Requires different approach than standard text-to-video generation
  - *From: VRGameDevGirl84(RTX 5090)*

- **Hair consistency issues in Phantom batch generation**
  - Character hair changes between generations in batch processing
  - *From: VRGameDevGirl84(RTX 5090)*

- **HeyGem needs 720p minimum resolution**
  - Upscaling could be a problem for longer videos, not sure if there's a way to upscale minute long videos yet
  - *From: ArtOfficial*

- **Context options cause looping artifacts**
  - The mouth doesn't loop properly when using context options for longer generations
  - *From: Guey.KhalaMari*

- **MultiTalk not yet available for ComfyUI**
  - Developers don't plan to support ComfyUI, will take ages to happen
  - *From: ZeusZeus (RTX 4090)*

- **Loop workflow shows artifacts on overlaps**
  - Strange artifacts appear at the beginning with squared pattern and on overlapping sections
  - *From: Thom293, Level Higher*

- **VACE causes color drift**
  - Color drifts much harder when trying to continue video with VACE
  - *From: Yae*

- **VACE likeness is never 100%**
  - Good at likeness but not perfect character consistency
  - *From: ingi // SYSTMS*

- **Reverse motion issues in longer generations**
  - Characters walking in wrong direction or background moving opposite way, especially common in gens longer than 49 frames
  - *From: ingi // SYSTMS*

- **Context options produce worse output**
  - Manual generation and stitching required for better quality
  - *From: Yae*

- **CausVid LoRA changes anime character faces**
  - Affects character consistency when used
  - *From: DreamWeebs*

- **Can't generate past 1080p without OOM**
  - Couldn't get it past the Vace Encode without an OOM at 1920x1080
  - *From: ingi // SYSTMS*

- **FusionX doesn't do red skin very well**
  - Doesn't really do red skin very well, but that can probably be fixed
  - *From: Thom293*

- **Can't do splashes well**
  - I dont think it can do splashes well though
  - *From: Thom293*

- **Phantom sometimes won't grab face as well when mixed**
  - When you mix phantom it will slow it down a tiny bit and it sometimes wont grab a face as well
  - *From: Thom293*

- **14B LoRAs not compatible with 1.3B**
  - The Loras used are were created for the 14B model
  - *From: VRGameDevGirl84(RTX 5090)*

- **SeedVR upscaler is very slow**
  - Takes 10 minutes per second of video on RTX 4090, even with fp8 3b model
  - *From: burgstall*

- **LightX vs CausVid trade-offs**
  - LightX at 4 steps makes videos look less real and more AI, not cinematic compared to longer generation
  - *From: VRGameDevGirl84(RTX 5090)*

- **Distilled models lose edge cases**
  - Distilled models tend to average out and lose the edges, reducing ability to do fewer things and steer toward bizarre concepts
  - *From: fredbliss*

- **AniWan character face consistency issues**
  - Really difficult for AniWan to keep character's face consistent with accelerated LoRAs like CausV2 and LightX2V
  - *From: DreamWeebs*

- **Multitalk struggles with raspy voices**
  - Doesn't seem to 'hear' raspy parts of voice very well
  - *From: Thom293*

- **Multitalk only works with 1 person currently**
  - Kijai only got 1 person multitalk working, 4 people support exists but not implemented in ComfyUI
  - *From: CJ*

- **720p+ resolutions cause OOM on lower VRAM**
  - 720x720 or 720x480 takes more than 1 hour on 4GB VRAM
  - *From: AiGangster*

- **Long video generation hits OOM over 81 frames**
  - Exponential chance of OOM over 81 frame length on 12GB VRAM
  - *From: mdkb*

- **Audio length degradation in longer generations**
  - MMaudio and audiox degrade at longer lengths
  - *From: Guey.KhalaMari*

- **LightX interferes with continuation generations**
  - LightX seems to mess with specific continuation gens, especially long ones
  - *From: Ablejones*

- **Pose control insufficient for mouth sync**
  - Pose is not enough for proper lip sync to audio, need separate model
  - *From: Ablejones*

- **WAN models have problems with explosions**
  - They make nice explosions but continue forever, likely due to training data cutoff
  - *From: Mads Hagbarth Damsbo*

- **Crowds are very hard to animate**
  - Most generations fail, only occasional good results
  - *From: Atlas*

- **Skyreels models are very human-centric**
  - Not suitable for all purposes
  - *From: Kijai*

- **VACE only works with specific models**
  - Technique won't work with other WAN models, might work with WAN Fun
  - *From: Jonathan*

- **Faces need at least 720 resolution**
  - With 512 res, faces are completely disfigured
  - *From: xwsswww*

- **Quan2.1 VACE model doesn't work with ComfyUI**
  - Works in Gradio app with 2 steps but needs conversion for ComfyUI
  - *From: hicho*

- **Fast movement causes artifacts with FusionX LoRA**
  - Even with high step counts, fast motion doesn't work well and causes artifacts
  - *From: Todd*

- **Kontext difficult to prompt and ignores instructions**
  - Sometimes completely ignores what you want, making keyframe creation the hardest part
  - *From: Ablejones*

- **MultiTalk V2V too fixed on start image**
  - Doesn't handle action scenes well, stays too focused on the initial image
  - *From: AJO*

- **Model loses quality with busy scenes**
  - Super fast or fine details movement challenging without artifacts, especially with busy backgrounds like lots of smoke, waves, or splashes
  - *From: Thom293*

- **Crowd generation quality issues**
  - Model loses coherence with crowd scenes, faces become poor quality at middle distances
  - *From: mdkb*

- **Style LoRAs can interfere with style prompts**
  - When using style LoRAs, certain style prompts like 'ink wash style' may be ignored
  - *From: hicho*

- **WAN native framerate is 16fps**
  - Need to use interpolation tools like GIMM and RIFE to achieve higher framerates
  - *From: mdkb*

- **Start and end frame precision issues**
  - Using start and end frames makes video less precise compared to just using video reference with one image frame
  - *From: Sal TK FX*

- **Depth maps don't process full 16-bit range**
  - No SOTA video model processes data in float - it doesn't read full range of 16bit depth map, gets clamped
  - *From: Guey.KhalaMari*

- **VACE 7B model VRAM usage**
  - At 992p can only upscale 4 second videos at a time on RTX 5090 before OOM, anything over 720p uses exponentially more VRAM
  - *From: el marzocco*

- **Old mocap files availability**
  - Some mocap files for biped are very old, grabbing TikTok dance will always be faster than using available mocap
  - *From: Duranovsky*

- **DWPose processing accuracy**
  - DWPose processing sometimes screws up, 3D biped approach gives 100% accuracy but limited to available animations
  - *From: Duranovsky*

- **Depth mapping is all-or-nothing**
  - Cannot selectively depth map just mouth areas - causes white mist artifacts when trying to mask specific regions
  - *From: mdkb*

- **Camera motion prompting issues**
  - Difficulty getting reliable camera-only movement on static scenes - keeps generating unwanted character motion instead
  - *From: Quality_Control*

- **Multitalk VRAM requirements**
  - Won't run on 12GB VRAM systems
  - *From: mdkb*

- **121 frames hit magic loop number**
  - Causes instability, 81 frames work better for consistent results
  - *From: Quality_Control*

- **FusionX LoRA issues with smoke effects and human faces**
  - Can cause problems in specific generation scenarios
  - *From: hicho*

- **Uni3C only works with I2V**
  - Not compatible with T2V, need to use VACE for similar T2V results
  - *From: Guey.KhalaMari*

- **Hard to mix camera motion with character motion**
  - Uni3C affects both camera and character movement simultaneously
  - *From: N0NSens*

- **Wan doesn't like to break or destroy things**
  - Especially reluctant to show people being harmed or objects being broken
  - *From: N0NSens*

- **Cannot generate head explosions or car accidents**
  - Built-in safety limitations prevent violent content generation
  - *From: Charlie*

- **Orbit camera movement not working reliably**
  - Despite prompting for orbit shots, camera movement doesn't follow instruction
  - *From: hicho*

- **Translation inconsistency**
  - Chinese translations of English prompts give inconsistent results
  - *From: garbus*

- **Wan 2.2 I2V produces disappointing results**
  - User reports poor quality compared to Wan 2.1 VACE
  - *From: GOD_IS_A_LIE*

- **Resolution limits on RTX 5090**
  - 1920x1080 impossible even with GGUF 6
  - *From: GOD_IS_A_LIE*

- **VACE compatibility with 2.2**
  - VACE control system doesn't work with Wan 2.2
  - *From: Sal TK FX*

- **5B model inconsistency**
  - 5B model can be inconsistent but produces fast results
  - *From: Benjaminimal*

- **High model resolution limits**
  - 2.2 High starts to duplicate/collapse sooner than Low at high resolutions
  - *From: 128578659047964672*

- **Style LoRAs affect motion quality**
  - LoRAs can make motion worse and cause unwanted behaviors like excessive talking
  - *From: Cseti*

- **Some things are too hard for this model**
  - Complex scenarios may require Wan 3.0 for proper handling
  - *From: seitanism*

- **Not enough slow-mo guys footage in training data**
  - Specific types of content are underrepresented in training
  - *From: seitanism*

- **Double Q8 OOMs on some setups**
  - Full Q8 control not possible on all hardware configurations
  - *From: garbus*

- **848x480 is pushing it to near system limit**
  - Higher resolutions approach hardware constraints
  - *From: U̷r̷a̷b̷e̷w̷e̷*

- **LightX2V incompatible with 5B model**
  - LightX2V LoRA does not work at all with the 5B model
  - *From: 397653550345345337*

- **Block swapping causes instability**
  - At high resolutions with 14B model, block swapping causes random artifacts and instability
  - *From: Juan Gea*

- **Tea Cache LoRA not good with limbs**
  - Tea Cache LoRA has issues rendering hands and limbs properly
  - *From: Atlas*

- **Higher resolution takes much longer**
  - Higher resolution generation took 30 minutes but had more errors, need optimizations to try multiple attempts
  - *From: 138234075931475968*

- **Speedup LoRAs affect quality negatively**
  - User prefers full model over speedup LoRAs despite longer generation time
  - *From: Zuko*

- **New Lightning LoRAs reduce motion quality**
  - They kill motion and create slow motion effects, though speed is improved
  - *From: U̷r̷a̷b̷e̷w̷e̷*

- **Style transfer fails on longer generations**
  - Only adheres to reference on very short videos, loses style consistency with longer frame counts
  - *From: 151330553629638656*

- **FLF morphing has gaps between videos**
  - Still visible transitions between segments in first-last-frame workflows
  - *From: 312993351307755520*

- **Website vs local quality disparity**
  - Local implementations can't match the quality achieved on official website
  - *From: AshmoTV*

- **New AIO model instability**
  - New release shows erratic, 'possessed' behavior in generations
  - *From: l҈u҈c҈i҈f҈e҈r҈*

- **Smooth transitions not possible with FFLF**
  - First-Frame-Last-Frame morphing has limitations for smooth transitions
  - *From: R.*

- **JSON prompting has issues**
  - Model has problems recognizing exact timesteps and scenes with JSON format
  - *From: AshmoTV*

- **Wan seems to hate certain types of images**
  - Some image types don't work well with the model
  - *From: hicho*

- **V2V lip-sync quality**
  - No decent open-source solution for video-to-video lip syncing. LatentSync and MultiTalk V2V attempts are not good
  - *From: 783977668278222869*

- **Fun Control quality trade-off**
  - While it follows movement well, the quality is much weaker than regular Wan
  - *From: Hashu*

- **Character LoRA leaking**
  - When prompting multiple characters with LoRA, it leaks between them
  - *From: NebSH*

- **Stand-In LoRA compatibility**
  - Currently designed for Wan 2.1, unclear if it works well with 2.2
  - *From: orabazes*

- **5B model sensitivity**
  - More difficult to achieve desired results, requires specific details and unnecessary details work against you
  - *From: Mngbg*

- **LoRA training causes 'mecha' to generate Gundams in early epochs**
  - Training artifacts that resolve as training progresses
  - *From: 138234075931475968*

- **Fantasy Portrait causes mumbling when source character isn't speaking**
  - Character appears to mumble if source video character isn't talking
  - *From: smithyIAN - 4080ti Super 16gig*

- **GGUF models need more steps and produce lower quality**
  - GGUF quantization requires more steps and gives worse results than fp16
  - *From: hicho*

- **Pattern artifacts in 2.2 backgrounds**
  - Background gets pattern artifacts more than character
  - *From: ingi // SYSTMS*

- **Complex action scenes difficult to achieve**
  - User struggling with lasers from eyes, explosions, complex compositions after 100+ iterations
  - *From: seitanism*

- **LightX2V LoRA reduces prompt adherence**
  - Significantly reduces prompt adherence
  - *From: ArtOfficial*

- **GGUF performance on distant faces**
  - Quite good for close-up faces but worse for far view faces
  - *From: AiGangster*

- **Character consistency issues**
  - Always get deformed result when character is moving
  - *From: AiGangster*

- **Characters talking constantly**
  - General problem with motion in high noise model, characters yapping the whole time
  - *From: AffenBrot*

- **Wan 2.2 5B has slip/morphing issues**
  - Objects slip from ground, cars have consistency issues, even Kijai can't solve it
  - *From: patientx*

- **Most video generators can't do lightning well**
  - Need to use inpainting and compositing techniques instead of relying on generation
  - *From: 177039592808120321*

- **Wan struggles with zooming out/outpainting**
  - Model has difficulty with outpainting operations
  - *From: Rainsmellsnice*

- **Context window issues with long generations**
  - Issues like earrings disappearing due to context window limitations
  - *From: A.I.Warper*

- **S2V lipsync not fully synced**
  - Mouth moves with sound but doesn't look like saying the words
  - *From: U̷r̷a̷b̷e̷w̷e̷*

- **Resolution artifacts at 880x880**
  - Fault appears at bottom of video at 10+ seconds, not present at 768x768
  - *From: Vérole*

- **InfiniteTalk changes character consistency**
  - Moving eyes suddenly stop moving, character features can change
  - *From: 𝕯𝖗. 𝕸𝖆𝖈𝖆𝖇𝖗𝖊 ☠*

- **Limited background motion in talking head videos**
  - Breaks immersion when only head moves while speaking
  - *From: BecauseReasons*

- **Color palette drift in long InfiniteTalk generations**
  - Colors shift over time during extended sequences
  - *From: tarn59*

- **No negative prompting in Foley audio model**
  - Completely ignores negative prompts for background music removal
  - *From: T2 (RTX6000Pro)*

- **SeedVR2 temporal consistency issues**
  - Has artifacts and needs batch size 5 for better consistency, but causes OOM on 5090
  - *From: 153803064858378240*

- **InfiniteTalk not as good with non-humans**
  - Performance degrades with non-human subjects compared to human lip sync
  - *From: CaptHook*

- **Wan image generation too slow for live production**
  - Takes 60s vs 10s for Qwen, only usable offline
  - *From: Marco_vdm*

- **Wan limited to 720p resolution**
  - Need upscaler to achieve higher resolutions like 4K
  - *From: 153803064858378240*

- **InfiniteTalk not ideal for animals like camels**
  - Facial animation works better on human subjects
  - *From: 𝕯𝖗. 𝕸𝖆𝖈𝖆𝖇𝖗𝖊 ☠*

- **PUSA LoRA intended for T2V only**
  - Not designed for I2V workflows though some users report it works
  - *From: . Not Really Human :.*

- **MagicWan workflow ridiculously slow**
  - Slower than expected with questionable quality improvement
  - *From: N0NSens*

- **Lack of control on 2.2 for production quality**
  - Issues achieving production-level control and quality
  - *From: AIGambino*

- **HPS LoRA issues with I2V**
  - HPS tries to draw details where it shouldn't in Image-to-Video generations
  - *From: N0NSens*

- **MPS/HPS LoRAs cause slow motion**
  - At 1.0 strength, both LoRAs tend to create slow motion effects
  - *From: patientx*

- **Topaz Starlight unusable**
  - Too slow for most practical purposes and has download issues
  - *From: . Not Really Human :.*

- **Video input quality degradation**
  - Using video as input instead of images causes quality degradation and takes much longer
  - *From: VRGameDevGirl84(RTX 5090)*

- **Tiling creates seams**
  - Tiled processing for higher resolutions can create visible seams without proper padding
  - *From: 153803064858378240*

- **InfiniteTalk motion limitations**
  - InfiniteTalk produces less motion, users asking how to solve this problem
  - *From: army*

- **HuMo video length restriction**
  - HuMo can generate maximum 10 seconds in wrapper
  - *From: asd*

- **Resolution vs VRAM constraints**
  - Even RTX 5090 cannot generate 1920x1080 out of the box, requires upscaling workflow
  - *From: Charlie*

- **Maximum quality rendering time**
  - Max quality 1980x1088 100 steps takes 2 hours on H100 GPU for 1 second of video, or 20 minutes with 8 H100s chained
  - *From: mdkb*

- **Lip flap issues**
  - Need to reduce excessive lip movement in generated videos
  - *From: VK (5080 128gb)*

- **HuMo mouth movement quality**
  - HuMo seems sluggish on mouth movements compared to other models
  - *From: 𝕯𝖗. 𝕸𝖆𝖈𝖆𝖇𝖗𝖊 ☠*

- **WAN 2.2 tends to convert artistic styles to photorealistic**
  - The model has a strong bias toward realistic output even when given stylized inputs
  - *From: 151330553629638656*

- **VACE may not work properly with GGUF models**
  - Compatibility issues reported with GGUF model format for VACE workflows
  - *From: ingi // SYSTMS*

- **Long videos beyond 81 frames require context windows**
  - Model context limit requires special techniques for longer video generation
  - *From: ingi // SYSTMS*

- **Model mixing causes compatibility issues**
  - Different model formats and versions don't work well together in the same workflow
  - *From: mdkb*

- **WAN Animate limited to 17 seconds maximum**
  - Even with high-end hardware like RTX 5090, length appears capped
  - *From: 𝕯𝖗. 𝕸𝖆𝖈𝖆𝖇𝖗𝖊 ☠*

- **Full body shots get wonky in longer videos**
  - Need to avoid full body shots for extended video generation
  - *From: VRGameDevGirl84(RTX 5090)*

- **Audio reactive video doesn't hit correctly**
  - When uploading drum parts, the video should follow and hit correctly but it doesn't
  - *From: Tonon*

- **Text replacement looks sloppy**
  - Text replacement in Wan 2.5 appears similar to sloppy Photoshop text replacement
  - *From: DawnII*

- **Audio quality is tinny and compressed**
  - Most of the generated audio is tinny and compressed, similar to mmaudio/hunyuanfoley
  - *From: DawnII*

- **VACE too unstable on slow motion**
  - User found it unsuitable for slow motion content, suggests inpainting with tracking as solution
  - *From: GOD_IS_A_LIE*

- **Wan trained heavily on realism**
  - Makes artistic style transfer challenging, especially for painted styles
  - *From: 88822364468412416*

- **VACE great at projecting style but won't know how to make style move**
  - Particularly challenging for painted oil effects that need frame-by-frame variation
  - *From: ingi // SYSTMS*

- **HuMo context window doesn't seem to work for long generations**
  - User cannot make long generations with HuMo despite context window
  - *From: Juan Gea*

- **Skin detail degradation over time**
  - Slight degradation of skin details like wrinkles over time in generations
  - *From: 767614506250665985*

- **Dyno has detail issues**
  - Dyno model doesn't perform well for fine details
  - *From: 152993277631528960*

- **Character shimmy with static prompts**
  - Dyno makes characters do a shimmy or walk in place when prompted to be fairly static
  - *From: 152993277631528960*

- **Wan struggles with human violence**
  - Wan doesn't like human to human violence - fighting scenes work sometimes but often look like fighting in a dream
  - *From: U̷r̷a̷b̷e̷w̷e̷*

- **LoRA can't patch everything**
  - LoRA won't work properly for Dyno as it patches things that LoRA fundamentally can't change
  - *From: JohnDopamine*

- **WanAnimate adds human artifacts to animals**
  - When using WanAnimate with animals, it's jittery and adds funny little human hands
  - *From: Nathan Shipley*

- **Model can't detect pig faces for human poses**
  - WanAnimate struggles with animal face detection when trying to apply human poses
  - *From: hicho*

- **WanAnimate has preprocessing detection issues**
  - Detection did not capture tutu completely in ballet pose preprocessing
  - *From: U̷r̷a̷b̷e̷w̷e̷*

- **Character consistency issues in long generations**
  - HuMo workflow can lose character consistency for 3 clips in second run before picking back up
  - *From: Charlie*

- **S2V prone to OOM errors**
  - Native S2V implementation prone to out-of-memory errors when trying longer generations
  - *From: 481339785513009152*

- **OVI static generation at certain resolutions**
  - Generates static when trying to gen at 640x640 or 704x704
  - *From: U̷r̷a̷b̷e̷w̷e̷*

- **Color matching between clips**
  - I2V then smooth travel causes dramatic color changes between clips
  - *From: 𝕯𝖗. 𝕸𝖆𝖈𝖆𝖇𝖗𝖊 ☠*

- **InfiniteTalk with non-human creatures**
  - More challenging results the more anatomy differs from humans, dogs are most unconvincing
  - *From: AR*

- **High detail upscaling can look too AI-generated**
  - At 2560x1440 scale, detail felt too much and started to look super AI generated
  - *From: ingi // SYSTMS*

- **Models cannot do proper 360-degree camera rotations**
  - Nano and other models struggle with accurate 360-degree rotations and spatial camera movements
  - *From: mdkb*

- **Object consistency when out of frame**
  - Models forget what objects look like when they move out of frame (e.g., swords disappearing)
  - *From: Dever*

- **Wan Animate lacks depth map controlnet**
  - Only has pose controlnet, making complex camera moves with non-pose data challenging
  - *From: AR*

- **Floaty pose skeleton in character animation**
  - Hard to portray weight in characters due to jittery skeleton poses
  - *From: 151330553629638656*

- **HuMo probably won't work with VACE**
  - Due to being technically based on I2V model
  - *From: Ablejones*

- **WanAnimate struggles with anime characters**
  - Face warps randomly, doesn't match original well, especially bad with 2D anime images
  - *From: Tachyon*

- **I2V unable to handle large scene changes**
  - Model struggles when trying to morph between very different scenes
  - *From: Dream Making*

- **WanAnimate adds lips regardless of reference**
  - Model forces human anatomical features even on characters that shouldn't have them
  - *From: Sal TK FX*

- **HuMo 4 second clip limit**
  - Primary issue with HuMo was the 4 second clip restriction
  - *From: Ablejones*

- **Lightx2v character bias**
  - Has bias towards Buzz Lightyear, Baby Yoda, people in business suits, converges to whatever character emerges from noise
  - *From: garbus*

- **16GB VRAM insufficient for good results**
  - Making 5 sec video above 480p is difficult and slow, even with block swapping and optimization
  - *From: Iridium Storm*

- **SVI not designed for Wan 2.2**
  - SVI wasn't designed to work with Wan 2.2, requires workarounds
  - *From: Ablejones*

- **OVI node limitations**
  - Can only input an image, no point in capturing last latent which is more than 1 frame anyway
  - *From: reallybigname*

- **HuMo profile angle issues**
  - Profile looks nothing like reference but head-on does
  - *From: VRGameDevGirl84(RTX 5090)*

- **ATI frame limit**
  - Pretty locked at 81 frames, errors with higher counts
  - *From: Fill*

- **Wan 2.2 character change issues**
  - Goes totally bonkers with abrupt character changes
  - *From: AR*

- **Mixing art styles difficult**
  - Hard time mixing concepts like 2d and realism, model tends to move into realism or anime rather than understanding mixing different styles
  - *From: AshmoTV*

- **Color/light shifts with lightx lora**
  - Getting color and light shifts when using the lightx lora
  - *From: Cseti*

- **Humo sync degrades with longer videos**
  - Can do 20 seconds but doesn't sync as well, people keep talking when audio ends
  - *From: reallybigname*

- **Light LoRA reduces style LoRA effectiveness**
  - Using Light LoRA at normal strength significantly hurts the effect of style LoRAs
  - *From: KevenG*

- **Wan struggles with complex human poses**
  - AI can't figure out strange yoga positions, produces freaky distorted results
  - *From: The Coin Hunter*

- **Character consistency issues in multi-scene workflows**
  - Characters can change appearance in the middle of sequences
  - *From: Ashtar*

- **Wan's 16fps is annoying compared to other models**
  - User appreciates that LTX team has fps conditioning unlike Wan
  - *From: Zuko*

- **Fun Vace 2.2 has video speed changes between segments**
  - Often the video speed will change between two segments even with overlapping seams
  - *From: Ablejones*

- **Original Vace was pretty weak with pose control**
  - Compared to newer implementations, original Vace had limited pose control capabilities
  - *From: Ablejones*

- **Small dataset LoRAs need more training**
  - 3-video dataset LoRA was 'undercooked' and would benefit from 6-8 videos for better results
  - *From: AshmoTV*

- **WAN not good with text preservation**
  - Text gets distorted during generation, compositing recommended as workaround
  - *From: dj47*

- **SVI likeness changes at the end**
  - Character consistency issues in longer SVI generations
  - *From: xwsswww*

- **ComfyUI workflow size limits**
  - There's a limit to workflow size ComfyUI can handle, very large workflows cause crashes
  - *From: Chandler*

- **WAN struggles with car orientations**
  - WAN 2.2 frequently flips car front and back views
  - *From: hicho*

- **Kling 2.6 doesn't support timestamped prompts**
  - Cannot use time-coded prompt instructions
  - *From: NodeMancer*

- **Wan 2.6 has weird aesthetic**
  - 30fps yet looks jittery or low dynamics, everything looks slow motion, visuals too smooth and unrealistic, img2vid generates cartoony animations
  - *From: dj47*

- **Subject shifting in context windows**
  - When using context windows for long generations, there's always minor shift in subject or background despite using references
  - *From: Ablejones*

- **Wan base issue with hand generation**
  - Tendency to generate bad hands, may pick bad hand even when overall generation improves
  - *From: hicho*

- **VACE can't perfectly maintain faces**
  - No settings in VACE to perfectly maintain person's face during video generation without masking
  - *From: Ablejones*

- **VACE can't change areas outside the mask**
  - If you want objects to fall or move outside original area, you must expand the mask to cover those areas
  - *From: Ablejones*

- **Models have difficulty 'breaking' objects**
  - Models don't understand objects are made of individual parts, making break/shatter animations challenging
  - *From: Ablejones*

- **VACE reference images constrain results**
  - When using reference image, VACE tries to maintain object integrity, making breakage/transformation difficult
  - *From: Ablejones*

- **Pure inpainting lighting limitations**
  - Unmasked subjects can't adapt lighting when placed in new environments
  - *From: Ablejones*

- **Audio drift in HuMo**
  - Segments after the first one are more likely to have spurious mouth movements, though improved with SageAttention
  - *From: Ablejones*

- **Background changes in HuMo**
  - No matter what prompting, can't get background to change
  - *From: Chandler*

- **Character consistency in extensions**
  - Character eager to run off screen which wrecks subsequent clips
  - *From: Chandler*

- **Wan dynamic motion**
  - 16fps and low dynamic motion (how much different motion can be crammed into same 5 seconds) make Wan pretty obsolete for certain uses
  - *From: dj47*

- **Line art generation**
  - Challenging to get right with WAN, took ~50 runs to get 1 correct result
  - *From: AR*

- **Plain Wan 2.2 length limitations**
  - User prefers not using long video tricks like first frame last frame, wants control over shorter generations
  - *From: Dodge Coin*

- **SCAIL only does body movements**
  - Cannot handle facial expressions like mouth opening, only body movements
  - *From: ingi // SYSTMS*


## Hardware Requirements

- **RTX 4090 480x480x81 14B model**
  - 10 minutes generation time at 50 steps
  - *From: ˗ˏˋ⚡ˎˊ-*

- **RTX 4070 14B T2V**
  - 8 minutes with sage attention
  - *From: BoricuaPab*

- **RTX 4070 1.3B T2V**
  - 1 minute 30 seconds with sage attention
  - *From: BoricuaPab*

- **RTX 5090 720p 876x640x81**
  - 30 minutes at 50 steps with 20 block offload
  - *From: TK_999*

- **RTX 4090 720x1280 81 frames**
  - 34 minutes at 30 steps, max 17GB VRAM, 18.8GB reserved
  - *From: wooden tank*

- **RTX 4090 14B model 35 steps**
  - 680 seconds (11+ minutes) generation time
  - *From: ingi // SYSTMS*

- **14B model VRAM**
  - 32GB model size, needs offloading on 24GB VRAM (RTX 4090) with noticeable slowdown
  - *From: Fannovel16*

- **4090 performance**
  - Runs 480p fine, even 720p works. Example: 22min for 81f I2V 720 q8 20steps
  - *From: Fannovel16*

- **A100 cloud performance**
  - Used for 1280x720 generation with good results
  - *From: Zuko*

- **3090 capability**
  - Can run small model, example: t2v 1.3B 832x480x33 in 200sec
  - *From: ˗ˏˋ⚡ˎˊ-*

- **8GB VRAM capability**
  - Can run 832x480x33 Hunyuan with Q8 GGUF and CPU offload on 8GB
  - *From: 215983606227664896*

- **3080 performance**
  - 5 min generation for 81 frame I2V with TeaCache
  - *From: garbus*

- **4070 performance**
  - 480x832 with I32V-14B-480p-Q3_k_S.gguf at 52.23s/it
  - *From: HUBERT THE ADVENTURER*

- **3080ti performance**
  - 249 frames at 24FPS possible with optimizations
  - *From: Teslanaut*

- **5090 performance**
  - 513 frames at 832x480 in 50 minutes with sliding context
  - *From: Kijai*

- **MultiGPU scaling**
  - 1.85x to 1.9x performance improvement with 2x4090 vs 1x4090
  - *From: Kosinkadink*

- **RTX 3090 performance**
  - 832x480 14B: 619sec, 1.3B: 154sec. 1280x720 1.3B: 415sec
  - *From: burgstall*

- **RTX 4080 timing**
  - 1.3B 50 steps: 3min, 14B 20 steps: 5min
  - *From: N0NSens*

- **RTX 3080Ti timing**
  - 448x448 81 frames: 8 minutes
  - *From: Fred*

- **H100 timing**
  - 720x1280 125 frames: 2516s base, 1515s with optimizations
  - *From: ingi // SYSTMS*

- **RAM usage**
  - Using 40-50GB RAM during generation, 32GB may be insufficient
  - *From: Fred*

- **3090 performance**
  - 6.32s/it for 30 steps at 480w x 272h with 14B fp8_e4 model, 64GB RAM recommended
  - *From: ZombieMatrix*

- **Generation times**
  - 89 frames taking 16-30 minutes on 3090 with t2v 14B model
  - *From: CJ*

- **1.3B model VRAM**
  - 1.3B model uses significantly less VRAM, can generate at higher resolutions without VRAM management
  - *From: TK_999*

- **Quantization compatibility**
  - 3090 can work with both e5m2 and e4m3fn quantization, same inference time
  - *From: BestWind*

- **High-resolution generation**
  - 80GB VRAM needed for native 1920x1080, takes about 2 hours
  - *From: Benjaminimal*

- **Lora training**
  - 75GB/80GB VRAM across 8 H100 GPUs for 14B model training
  - *From: Benjaminimal*

- **Generation speed comparison**
  - 5090 with 96GB RAM: ~1 minute per second output; slower on L40s with 48GB VRAM
  - *From: AJO*

- **8GB VRAM performance**
  - 61 minutes to create 5 seconds on 8GB VRAM using I2V
  - *From: Level Higher*

- **3090 performance**
  - 720x1280 I2V: 21 minutes for 49 frames
  - *From: burgstall*

- **14B model at 720p**
  - Needs 40-48GB VRAM, 18-19 minute render times for 65-81 frames
  - *From: Kytra*

- **1.3B model performance**
  - Runs 4x faster than 14B, works well at 1280x720 on lower VRAM
  - *From: Jas*

- **8GB VRAM capability**
  - Can run WAN with workarounds, 7 minute renders possible with optimizations
  - *From: Level Higher*

- **1024x576 generation**
  - Takes nearly an hour on unspecified hardware but produces good results
  - *From: TK_999*

- **Training requirements**
  - Character lora trained in 35 minutes across 8xH100s
  - *From: Kytra*

- **A100 40GB cloud performance**
  - 18 minutes per generation at 1280x720, 73 frames
  - *From: Kytra*

- **14B model VRAM**
  - RTX 3090 with 24GB VRAM should work fine, can use GGUF files for memory management
  - *From: garbus*

- **4090 compatibility**
  - 4090 laptop with 16GB VRAM and 32GB RAM works on Windows
  - *From: IllumiReptilien*

- **Generation speed examples**
  - 38 seconds of video in 48 minutes on 5090 with 96GB RAM, 20 seconds 480p i2v in 22 minutes at 8 steps on L40S 48GB
  - *From: AJO*

- **3090 performance**
  - ~50 s/it for 480p i2v workflow, 81 frames at 832x480 takes 16-20 minutes
  - *From: PirateWolf*

- **5090 vs cloud performance**
  - 6 scenes took 30 mins in cloud, 20 mins on 5090, 480p resolution
  - *From: AJO*

- **RTX3090 render time**
  - 10 second video, 55 minutes render, 25 steps, 24 FPS, 24GB VRAM, CFG 6.5
  - *From: Level Higher*

- **3060 experience**
  - Very slow - 3%|1/30 [01:30<43:37, 90.25s/it]
  - *From: Dream Making*

- **Ultra-wide video generation time**
  - 2500x500x69 takes 10 minutes on 4080 with teacache, around 65 minutes on downclocked 3090
  - *From: ZombieMatrix*

- **Ultra-tall panoramic generation time**
  - 500x2500x69 takes 5-6 hours on RTX4080 for first gen, then 30 minutes for subsequent gens
  - *From: ZombieMatrix*

- **Standard generation time**
  - 480p, 8 steps, 1 queue takes 20-41 minutes depending on setup
  - *From: AJO*

- **VRAM for multi-scene generation**
  - RTX 5090 running at 67% for multi-scene generation, 31 minutes for multiple scenes
  - *From: AJO*

- **Optimized inference performance**
  - RTX 3090 can generate 640×480×81 frames in 5 minutes using optimizations
  - *From: seruva19*

- **Ultrawide generation performance**
  - 2500x500x33 (5:1 aspect ratio) takes ~20 minutes on downclocked 3090
  - *From: ZombieMatrix*

- **LoRA training speed**
  - RTX 5090 enables overnight LoRA training with 2e-4 learning rate
  - *From: 88822364468412416*

- **VRAM for long generations**
  - Can't do 141 frames normally at 480x480 on 24GB, but sliding window enables 141+ frames. 161 frames still too much even with sliding window
  - *From: Clownshark Batwing*

- **Generation times**
  - 141 frames takes 11 min on 4090, 301 frames takes 26 min, 601 frames takes 40 min. 97 frames at 640x640 takes 870s on 5090
  - *From: Clownshark Batwing*

- **24GB VRAM capabilities**
  - Can run Fun Control bf16 vs fp16 weights comparison
  - *From: Benjimon*

- **14B SkyReels DF VRAM**
  - Eats terrible amount of memory, needs 38+ block swap on 16GB, takes 4GB+ extra for time embeds
  - *From: Kijai, Ablejones*

- **Ultra-wide generation performance**
  - Wide resolutions run faster than expected, 20-26 hours for 50 generations at 2500x500
  - *From: ZombieMatrix*

- **Quality generation time**
  - 75 steps with TeaCache takes ~25 minutes on RTX 3090
  - *From: Level Higher*

- **RTX 3090 performance**
  - 15-20 minutes for 4 second generations at 50-75 steps with 14B i2v model
  - *From: Level Higher*

- **RTX 4080 ultra-wide generation**
  - 2500x500@33 resolution takes around 18 minutes each generation
  - *From: ZombieMatrix*

- **GPU temperature management**
  - 65-70°C is good operating temperature, 80°C is safe, 95°C tjunction limit for RTX 3090 non-ti
  - *From: Level Higher/Benjimon*

- **24GB VRAM for sliding window**
  - Can handle up to 601 frames with advanced Rewan patcher on 24GB VRAM
  - *From: Clownshark Batwing*

- **5090 VRAM capacity**
  - Can do 576p without block swapping, resolution dependent on video length
  - *From: 88822364468412416*

- **Generation time on slower cards**
  - 97 frames take around 7 minutes on slower GPUs
  - *From: Cseti*

- **4080/3090 performance**
  - 10 minutes to upscale from 2048w to 3520w on 4080 or 3090
  - *From: ZombieMatrix*

- **H100 potential**
  - H100 has 80gb VRAM, could potentially create very long generations
  - *From: 🏁🫰GridSnap*

- **Ultra high-res generation**
  - Single 3090 handles 5248x1040 generation, hits 23GB VRAM and 64GB system RAM, takes 28-36 minutes
  - *From: ZombieMatrix*

- **System RAM for video workflows**
  - Modern video/audio workflows can use up to 60GB+ system RAM due to offloading, 32GB can be limiting
  - *From: ZombieMatrix*

- **Long generation times**
  - Ultra tall portraits can take 6.5 hours, ultra wide takes 20-30m, height is more computationally expensive than width
  - *From: ZombieMatrix*

- **High RAM usage**
  - bitseq regularly maxes out 96GB RAM, looking to upgrade to 192GB
  - *From: bitseq*

- **4000+ pixel width generation**
  - Requires significant VRAM, dumps to system RAM on 3090
  - *From: ZombieMatrix*

- **Tiled upscaling VRAM usage**
  - Peak 19GB for 14B model, 7GB for 1.3B model upscaling to 1536x1536
  - *From: Clownshark Batwing*

- **CausVid generation speed**
  - 2 minutes on 4060Ti, 2-3 minutes decent resolution on 3080
  - *From: Vérole*

- **High resolution generation on 4090**
  - 1366x768 takes 24 minutes, needs --reserve-vram 12.0 on 3090 to avoid OOM
  - *From: TK_999*

- **FP8 optimization**
  - 4xxx cards have optimized FP8 handling, 3xxx cards upcast FP8 to FP16 at inference
  - *From: ˗ˏˋ⚡ˎˊ-*

- **VRAM usage for large images**
  - 89GB system RAM and 22GB VRAM at peak for 21.8MP image generation
  - *From: ZombieMatrix*

- **4080 performance**
  - Can generate action scenes with fast motion in one day
  - *From: Dkamacho*

- **3090 with CausVid**
  - Less than 5 min on 3090 for 1280x720x81 frames with 1.3B + CausVid
  - *From: HeadOfOliver*

- **4060ti speed**
  - 10 seconds generated in 45 seconds, 4/4 iterations at 11.46s/it
  - *From: Vérole*

- **System RAM limitation**
  - System RAM becomes limiting factor before VRAM in large image workflows
  - *From: ZombieMatrix*

- **VACE 14B fp16 generation**
  - 272 frames at 720x1280, 6 steps, context window 65 frames
  - *From: Kendo*

- **1.3B model speed**
  - 1 minute to generate 1024x576x81 frames on RTX 3090
  - *From: HeadOfOliver*

- **14B model with CausVid**
  - 4 min 45 sec using 36GB VRAM
  - *From: HeadOfOliver*

- **Fast T2V generation**
  - 126.41 seconds for 81 frames at 1024x576 with 6 steps on RTX 5090
  - *From: VRGameDevGirl84(RTX 5090)*

- **CausVid v2v batch processing**
  - 110 frames processed in 150 seconds
  - *From: hicho*

- **14B model VRAM needs**
  - Requires RTX 5090 minimum, 29GB VRAM usage observed, struggles on RTX 5060TI
  - *From: craftogrammer*

- **Long video generation memory**
  - 412 frames at 1024x576 requires substantial VRAM and system memory management
  - *From: A.I.Warper*

- **Dual sampler VRAM limitations**
  - Running two Wan samplers with different LoRAs can exceed VRAM/memory limits even with pagefiles
  - *From: DevouredBeef*

- **PyTorch memory allocation**
  - PyTorch sets 40GB committed memory preallocated, requires large pagefile on top of system RAM
  - *From: phazei*

- **RTX 4080 performance**
  - Can handle 1024x576 resolution as maximum
  - *From: CaptHook*

- **RTX 4090 T2V performance**
  - 2 minutes for T2V generation, 16 seconds video takes 385 seconds to generate
  - *From: GalaxyTimeMachine (RTX4090)*

- **A6000 Pro performance**
  - 52 seconds for 832x480, 78 seconds for 1024x576, cost $8.5k plus additional motherboard/CPU upgrades needed for dual GPU setup
  - *From: fearnworks*

- **RTX 6800 (AMD) performance**
  - 384x512, 97 frames x 2, 6 seconds took 24 minutes using ZLUDA
  - *From: patientx*

- **RTX 5090 capability**
  - Can do 1280x720 without block swapping at 81 frames, maximum 121 frames possible with context options
  - *From: VRGameDevGirl84(RTX 5090)*

- **RTX 5090 generation speed**
  - 5 video batch completes in around 250 seconds, T2V very fast but VACE takes longer
  - *From: VRGameDevGirl84(RTX 5090)*

- **Ampere cards performance**
  - 120-140 s/it at 6 steps on smaller dimensions over 512, described as 'really bad'
  - *From: MysteryShack*

- **MMaudio speed on RTX 3060**
  - Takes only a few seconds to generate audio
  - *From: Jonathan*

- **H100 training time**
  - Custom LoRA trained for 17 hours on H100 with ~50 images + 15 videos at maybe 45 epochs, 5 repeats, 15k steps
  - *From: ingi // SYSTMS*

- **HeyGem VRAM usage**
  - Uses about 14gb VRAM for lip sync generation
  - *From: ArtOfficial*

- **CaptHook's setup**
  - RTX 4080 16gb, no torch/teacache/slg or other loras, runs 1024x576 well
  - *From: CaptHook*

- **GGUF file placement**
  - Put GGUF files in diffusion_models folder with the safetensors models
  - *From: TK_999*

- **Self-Forcing speed**
  - 17 FPS on 1 H100 GPU with sub-second latency
  - *From: SS*

- **VACE with depth control render time**
  - 140 frames took 40 minutes on RTX 5080, 12 steps with context overlap
  - *From: VK (5080 128gb)*

- **Self-Forcing VACE speed**
  - 161 frames in 7 minutes, 6 steps with DPM++
  - *From: VK (5080 128gb)*

- **Standard generation time reduction**
  - Fusion reduces 5-second video render from 15 minutes to 5 minutes
  - *From: Level Higher*

- **Performance benchmark**
  - 121 frames @ 24 FPS, execution time: 132s on RTX 4090 with 8 swap blocks at 1024x576
  - *From: 312993351307755520*

- **VRAM for higher resolution**
  - Might need to throw it at a bigger GPU on Runpod to see what happens at 1080p
  - *From: ingi // SYSTMS*

- **RTX 4080 setup**
  - Wrapper, torch, sage, blocks - everything I could install to speed things up, using purge vram in every wf
  - *From: N0NSens*

- **RTX 5060 Ti generation time**
  - 1 hour for 314 frames at 10 steps
  - *From: VK (5080 128gb)*

- **A4500 upscaling performance**
  - About 10 minutes for each 576x1024 81f upscale pass on A4500 with 24GB VRAM
  - *From: The Shadow (NYC)*

- **4GB VRAM setup**
  - 480x256 resolution, 10 steps, FusionX GGUF q5_M, 9-10 minutes generation time on 3050ti
  - *From: AiGangster*

- **Multi-GPU setup**
  - 5090 + 3090 can generate 289 frames vs 173 on 5090 alone, 95 seconds for 5 second video
  - *From: el marzocco*

- **VRAM for upscaling**
  - 1.3b models take 2-4min for upscaling on 16GB VRAM, 14b takes 10x longer
  - *From: N0NSens*

- **Context generation**
  - 480 frames 24fps took 20:47 on high-end hardware
  - *From: VRGameDevGirl84(RTX 5090)*

- **Multitalk processing**
  - 133 seconds for 4 seconds of video
  - *From: VRGameDevGirl84(RTX 5090)*

- **128GB RAM with blockswapping**
  - Prevents OOM with sufficient regular RAM
  - *From: VK (5080 128gb)*

- **Mac memory usage**
  - WAN often goes over 170GB for larger generation sizes/more frames on 256GB unified memory
  - *From: Todd*

- **ComfyUI memory consumption**
  - Consuming ~70GB for dancing sample, much more for sword examples
  - *From: Todd*

- **Multi-GPU VRAM**
  - Monitor connection consumes 0.5-1GB VRAM on main GPU
  - *From: el marzocco*

- **Mac compatibility**
  - Can run WAN on M4 Max with 128GB unified RAM, though may need swap disk for larger sizes
  - *From: Todd*

- **VRAM for different resolutions**
  - 1280x720 81 frames works on 3090, 216 frames at 576x1024 caused OOM on 4090, 17 frames better than 81 frames on 12GB VRAM
  - *From: multiple users*

- **AMD RX 6800 performance**
  - 832x480 @ 53 frames takes 90 sec/it with blockswap due to insufficient VRAM
  - *From: patientx*

- **4GB VRAM generation times**
  - 9-10 minutes for 480x256, 81 frames. Up to 12 minutes with more than 2 LoRAs. 6 minutes without LoRAs if lucky
  - *From: AiGangster*

- **4090 performance with upscaler**
  - Can only generate 25 frames at 1920x1072 with 4090 using upscaler, 188 seconds for upscaling 223 images from 512x288 to 2048x1152
  - *From: Sal TK FX*

- **RTX 2060 capabilities**
  - Can handle 600x480x80 frames generation
  - *From: hicho*

- **AMD RX 6800 performance**
  - 1 step takes 10-12 seconds at full power, 27 seconds when power limited to 70W
  - *From: patientx*

- **4GB VRAM for I2V**
  - I2V 14B FusionX at 480x480, 81 frames, 8 steps takes 28 minutes on 4GB VRAM
  - *From: AiGangster*

- **VRAM for VACE 7B upscaling**
  - RTX 5090: 992p limited to 4 second videos, 720p+ uses exponentially more VRAM, maximum block swap used
  - *From: el marzocco*

- **Low VRAM video generation**
  - First Frame Last Frame: 480x480, 81 frames in 13 minutes on 4GB VRAM
  - *From: AiGangster*

- **Mac OS generation time**
  - VACE config generates in about 1.5 minutes on Mac OS using Draw Things
  - *From: Todd*

- **Neo removal workflow VRAM**
  - 10 second video using low res and tons of block swapping, just barely scraped by on 24GB
  - *From: Neex*

- **Multitalk VRAM**
  - Requires more than 12GB VRAM
  - *From: mdkb*

- **AMD GPU support**
  - Works on RX 6800 with comfyui-zluda fork for AMD on Windows
  - *From: patientx*

- **VRAM for SeedVR upscaler**
  - Doesn't use all VRAM on 5090, should work fine on 4090
  - *From: Charlie*

- **RTX 2060 6GB performance**
  - 37 seconds generation time for image generation
  - *From: hicho*

- **RTX 5090 performance**
  - 23 seconds for image generation + 4x upscale
  - *From: Charlie*

- **RTX 4090 Wan 2.2 5B I2V**
  - 4 minutes per generation at 1280x704
  - *From: Janosch Simon*

- **RTX 3060 Wan 2.2 5B**
  - 13 minutes generation time
  - *From: Abx*

- **RTX 5090 Wan 2.2 14B I2V**
  - 80 minutes for 121 frames at 1280x720, uses 29GB VRAM
  - *From: GOD_IS_A_LIE*

- **RTX 3080 12GB Wan 2.2**
  - 219 seconds with LightX2 LoRA
  - *From: garbus*

- **FastWan 1.3B VRAM usage**
  - Runs at 1920x1024 81 frames with 16GB VRAM
  - *From: Vérole*

- **RTX 4090 performance**
  - 960x540 generation in 88.62 seconds on 4090
  - *From: Janosch Simon*

- **14B model memory usage**
  - Peak memory usage 10GB on 14B model with low and high noise combo, ~100 seconds per clip
  - *From: Mads Hagbarth Damsbo*

- **4080 Super performance**
  - 150 seconds for I2V with GGUF4 and LightX LoRA
  - *From: smithyIAN - 4080ti Super 16gig*

- **Dual GPU setup**
  - VRAM offloading to 2nd GPU working for 14B models at 1536x704
  - *From: Xodroc*

- **12gb VRAM for 5-7 minute generations**
  - Depending on video length with 2.2 model
  - *From: U̷r̷a̷b̷e̷w̷e̷*

- **8 minutes on 5090**
  - For 640x512x361 frames with RadialAttn, 8+12 steps
  - *From: 128578659047964672*

- **366 seconds cold run**
  - With fp16 models and dtype fp8_e4m3fn_fast for 1280x704*81 frames
  - *From: Juan Gea*

- **RTX 3060 12GB performance**
  - Can run 1024x576 resolution in about 10 minutes using GGUF Q8_0
  - *From: 993837056159649822*

- **High-res generation timing**
  - RTX4090: 3072x1840x81 frames total 1725 seconds (14B: 787s, 5B: 434s, encoding/decoding overhead)
  - *From: Juan Gea*

- **5090 performance**
  - 1280x704 generation in 130.36 seconds with 3+3 steps using LightX2V
  - *From: NebSH*

- **Block swap settings**
  - 40 block swap for 14B model, 30 blocks for 5B model at high resolutions
  - *From: Juan Gea*

- **RTX 3060 compatibility**
  - Can run workflows but may need 720p generation and reduced frames (61 frames mentioned)
  - *From: Abx*

- **Long generation performance**
  - 1621 frames took 52 minutes on 4090 with sliding context
  - *From: kendrick*

- **Speed considerations**
  - 18-20 sec per step acceptable, but 40 sec per step too slow for practical use
  - *From: patientx*

- **VRAM usage for different resolutions**
  - 1920x1080 takes 60 sec per step vs 1024x1024 takes 12 sec per step, around 300 sec total for 4-step generation
  - *From: patientx*

- **RTX 3060 12GB capability**
  - Can run Wan 2.2 effectively
  - *From: cancer32*

- **6GB VRAM**
  - Sufficient to run Wan 2.1 u3c
  - *From: hicho*

- **RTX 3060 Lightning LoRA performance**
  - 4 steps takes about 300 seconds, with first generation taking longer due to model loading
  - *From: Abx*

- **RTX 5090 long video capability**
  - Can generate 12-19 seconds straight with Wan 2.2 at good quality
  - *From: Charlie, ComfyCod3r*

- **High VRAM for context window**
  - Lots of VRAM needed to fit all frames for long generations without context window
  - *From: ˗ˏˋ⚡ˎˊ-*

- **4GB VRAM can handle 648x1080 and 908x1440**
  - With GGUF models and proper optimization
  - *From: AiGangster*

- **5090 can handle 1920x640, 81 frames**
  - Takes 270 seconds, uses 96-97% VRAM with Q6K GGUF
  - *From: 152993277631528960*

- **8GB VRAM with 64GB RAM can use block swapping**
  - Allows handling larger models through CPU RAM offloading
  - *From: xwsswww*

- **ComfyUI and wrapper very optimized for low VRAM**
  - Offloading leaves full 4GB available for AI compute
  - *From: hicho*

- **Long generation performance**
  - 2400 frames took 06:12:52 on 5090, 480x720x81
  - *From: seitanism*

- **4GB VRAM capability**
  - Can run Wan 2.2 i2v 14B with GGUF, upscaled with Wan 2.1 t2v 1.3b
  - *From: AiGangster*

- **3090 compatibility**
  - Can run at 480p resolution depending on settings
  - *From: NebSH*

- **InfiniteTalk on 12GB VRAM**
  - Can run InfiniteTalk in about 8 minutes total generation time
  - *From: U̷r̷a̷b̷e̷w̷e̷*

- **Wan 2.2 5B performance**
  - 832x1248x121 frames took 25 minutes on RX 6800, reduced to 15 minutes with optimizations
  - *From: patientx*

- **5090 performance**
  - 1100 seconds (under 20 mins) for longer generations, 20 mins for 960 frames
  - *From: AJO*

- **Upscaling workflow performance**
  - Takes around 30 minutes on 6000 Blackwell GPU
  - *From: mono*

- **VRAM usage for 720p Q3**
  - 99% VRAM usage on 16GB card
  - *From: N0NSens*

- **5090 performance**
  - InfiniteTalk 5551 frames at 832x480, 4 steps completed in 41:52
  - *From: Kijai*

- **3060 RTX capabilities**
  - Can handle 1600x900x81 in 30 minutes for upscaling with 32GB system RAM
  - *From: mdkb*

- **5090 upscaling speed**
  - 5 minutes to upscale video to 1440p
  - *From: 153803064858378240*

- **VRAM for different quantizations**
  - Q8_0 causes OOM on 24GB VRAM (3090), Q6_K works fine
  - *From: Ashtar*

- **Generation time on RTX 4080**
  - 10 seconds for fast sampler at 1600x912, 30 seconds for slow sampler
  - *From: N0NSens*

- **Upscaling performance**
  - 18 minutes to upscale 5 second video to 4K
  - *From: 153803064858378240*

- **Low-end GPU performance**
  - RTX 2060 can handle 1024x700 * 33 frames with good quality using KJ wrapper
  - *From: hicho*

- **InfiniteTalk on 12GB 3060**
  - 1 minute per second of video generation
  - *From: U̷r̷a̷b̷e̷w̷e̷*

- **AMD system compatibility**
  - 5700x3d CPU, RX 6800 GPU, 32GB RAM - can run Wan with ZLUDA/native torch
  - *From: patientx*

- **AMD upscaling performance**
  - AMD not good with upscaling in ComfyUI, external tools like Upscayl preferred
  - *From: patientx*

- **GGUF model sizes**
  - Q3 around 7GB per model, Q8 around FP8 size
  - *From: patientx*

- **Processing time example**
  - About 5 minutes on RTX 4090 for T2V with lightx2v, MPS+HPS, Lanczos upscale x1.5 and USDU
  - *From: GalaxyTimeMachine (RTX4090)*

- **RTX 3060 InfiniteTalk performance**
  - RTX 3060 12GB with 32GB RAM can do 1:30 single shot, averages 1 minute per 1 second of video. Maxed at 3 minute gen (OOM on last step). Gen at 624x368 or 480x480 square
  - *From: U̷r̷a̷b̷e̷w̷e̷*

- **RTX 5090 InfiniteTalk performance**
  - On 1280x720, 2 minute generation takes about 1 hour
  - *From: Charlie*

- **RTX 3060 upscaling capability**
  - Can upscale 1080p 121 frames using USDU with proper tile settings
  - *From: mdkb*

- **RAM usage per tile**
  - Around 7GB RAM per tile during upscaling process
  - *From: Hevi*

- **High-end generation times**
  - H100 GPU takes 2 hours for 1 second at max quality (1980x1088, 100 steps), reducible to 20 minutes with 8x H100 setup
  - *From: mdkb*

- **RTX 5090 training speed**
  - RTX 5090 trains LoRAs quickly, allowing for rapid iteration
  - *From: 253611044595826688*

- **RTX 3060 can handle 720p WAN generation**
  - 720p video generation confirmed working on RTX 3060 hardware
  - *From: mdkb*

- **Ultimate SD upscaler takes 18 minutes on RTX 5090**
  - 4K upscaling with max quality settings requires significant processing time even on high-end hardware
  - *From: 153803064858378240*

- **Humo long generation workflow takes 40 minutes for 1 minute output**
  - Full music video generation with multiple passes requires substantial processing time
  - *From: ˗ˏˋ⚡ˎˊ-*

- **4090 performance**
  - 50 minutes on 4090 with 4 steps at 1280x720 for 1m2s clip
  - *From: 1348584179440418868*

- **5090 performance**
  - ~10 minutes on 5090, 544x960 res, 121 frames each in about 4 windows
  - *From: AR*

- **12GB VRAM setup**
  - Q5KM GGUF wanimate with 48GB RAM, 15s video in about 12 minutes at 624x368 resolution
  - *From: U̷r̷a̷b̷e̷w̷e̷*

- **VRAM for 1280p**
  - Maxing out around 65GB VRAM for 1280p Wan animate
  - *From: 767614506250665985*

- **GPU cooling**
  - Need better cooling for GPU when running 1280p generations due to high heat
  - *From: 767614506250665985*

- **Dyno model size**
  - 28gb for full fp16 model
  - *From: Charlie*

- **RTX 5090 performance**
  - 250 seconds for standard generations
  - *From: AiAuteur*

- **RTX 4090 HuMo timing**
  - 43 minutes total generation time for audio-reactive content
  - *From: kendrick*

- **800 frames at 576x1024**
  - Successfully generated with context windows on capable hardware
  - *From: AR*

- **RAM for long WanAnimate**
  - 64GB not enough for long generations without context, 128GB recommended for storing all frames in memory
  - *From: Charlie*

- **5090 performance**
  - Can handle 77 frame windows for WanAnimate, used for various long-form generations
  - *From: A.I.Warper*

- **3090 performance with Ovi**
  - 20 steps takes ~3 minutes on 3090 using gradio app
  - *From: Anchorite*

- **5090 Ovi performance**
  - 2 minutes generation time on 5090
  - *From: Thom293*

- **VRAM for high resolution**
  - 1536 x 864 generation possible on RTX 5090
  - *From: Kytra*

- **RAM for block swap efficiency**
  - 128GB RAM enables faster block swapping for generation
  - *From: VRGameDevGirl84(RTX 5090)*

- **Generation time scaling**
  - Half hour for 1 minute of video at 1280x720 with 20 block swap on RTX 5090
  - *From: VRGameDevGirl84(RTX 5090)*

- **Upscaling processing time**
  - Upscaling workflow took ~34 minutes without face detailer
  - *From: Dever*

- **Long generation VRAM/RAM needs**
  - 909 frames at 720p: Max VRAM 27.458GB, Required 260GB system RAM
  - *From: A.I.Warper*

- **RTX 3060 performance**
  - 9 minutes to render 5 seconds at 640x640 with 12GB VRAM and 16GB RAM
  - *From: The Coin Hunter*

- **High-end system specs**
  - Runpod with 1.7TB system RAM available for extreme long generations
  - *From: A.I.Warper*

- **VRAM for different models**
  - User with 3060 had issues getting VACE to work, while 5090 users had better success
  - *From: The Coin Hunter*

- **5090 performance**
  - 5 days focused work for ultra-realistic video including LoRA training
  - *From: 481339785513009152*

- **Flash upscaler performance**
  - 50 seconds per 81 frames when warmed up
  - *From: Tony(5090)*

- **WanAnimate performance**
  - Prompt executed in 01:19:03 for 924 frames at 1080p resolution
  - *From: A.I.Warper*

- **4090 performance**
  - 2m30s for each 5 second clip with square aspect ratio and 35 steps
  - *From: reallybigname*

- **3090 performance**
  - 101 frames 720x400 in under 200 seconds with lightweight gguf model
  - *From: TimHannan*

- **16GB VRAM limitations**
  - Difficult to make 5 sec video above 480p, slow even with optimizations
  - *From: Iridium Storm*

- **H200 performance**
  - 1080p video 360 frames took 45 minutes to render
  - *From: AR*

- **12GB VRAM limit**
  - 512x512 appears to be limit for Wan Mocha on 12GB VRAM
  - *From: Blink*

- **2060 performance**
  - Qwen edit runs very slow on 2060, Wan I2V faster alternative
  - *From: hicho*

- **VRAM for different resolutions**
  - 16GB GPU can do close to 720p 10s (1152x640) but not full 720p
  - *From: Simonj*

- **Qwen BF16 performance**
  - Takes 10 minutes to generate first pass on high-end setup
  - *From: 𝕯𝖗. 𝕸𝖆𝖈𝖆𝖇𝖗𝖊 ☠*

- **4090 capabilities**
  - Can handle Humo default workflow for 20 second generations
  - *From: reallybigname*

- **VRAM optimization with new settings**
  - comfy_chunked rope setting + use_cpu_cache true allows full 1280x720 on 12GB card, 10-50% VRAM reduction
  - *From: garbus*

- **Training performance varies with dataset size**
  - 3-video dataset: 11-12s/it, 11-video dataset: 5-6s/it on A100-80 GPU
  - *From: AshmoTV*

- **VACE generation speed**
  - Takes 10 minutes to generate 49 frames with VACE even on RTX 6000 Pro
  - *From: NodeMancer*

- **System for advanced workflows**
  - 5090 with 64GB RAM for complex context window and dual sampler setups
  - *From: Ablejones*

- **WAN 2.2 GGUF Q4 VRAM**
  - Runs on 6GB VRAM without block swap using native ComfyUI, uses around 50% RAM
  - *From: hicho*

- **H200 performance for long video**
  - 1690 frames at 1080x1920 rendered in 1hr 15mins on H200
  - *From: AR*

- **RAM usage for 8GB VRAM setup**
  - Uses up to 90% of RAM for WAN generations on 8GB VRAM cards
  - *From: Tony(5090)*

- **RTX 5090 performance**
  - 55 minutes for full HuMo workflow generation, 4-step generations take about 1 minute each, FMML takes about 5 mins per group at default res
  - *From: 152993277631528960*

- **VRAM limitations for higher resolutions**
  - User runs out of RAM trying to render 1920x1080, questioning if GGUF vs fp8 models make difference in VRAM usage
  - *From: dj47*

- **RTX 3090 performance comparison**
  - User feels RTX 3090 feels sluggish compared to RTX 5090 for Wan generation
  - *From: dj47*

- **VRAM usage for 1280x720**
  - Takes 9 minutes per group at 8 steps
  - *From: VRGameDevGirl84(RTX 5090)*

- **SVI 2 Pro VRAM efficiency**
  - Each segment only takes as much VRAM as a single clip would
  - *From: Ablejones*

- **Wan 2.2 LoRA training**
  - Minimum 48GB VRAM needed, 16GB VRAM is not enough
  - *From: 545077836898369546*

- **LTX2 on 3060**
  - Need to get LTX2 running on 3060 before training LoRAs for it
  - *From: AshmoTV*


## Community Creations

- **Multi-segment generation workflow** (workflow)
  - 4-stage generation system with LLM vision prompting for extended sequences
  - *From: AJO*

- **V2V upscaling workflow** (workflow)
  - Pipeline to upscale videos using V2V with frame-by-frame upscaling
  - *From: DiXiao*

- **Color palette node** (node)
  - Uses images as color palettes for generation
  - *From: Fill*

- **Infinite looper WIP** (workflow)
  - Work in progress infinite looping generation system
  - *From: AJO*

- **SNES sprite LoRAs** (lora)
  - Trained LoRAs for infinite SNES sprite creation workflow
  - *From: Kytra*

- **Window blending implementation** (technique)
  - Blends context windows to reduce noise in sliding context generation
  - *From: Kijai*

- **TeaCache integration** (optimization)
  - Caching system that speeds up generation by reusing computations
  - *From: DiXiao*

- **MultiGPU support** (optimization)
  - Enables Wan to run across multiple GPUs for faster inference
  - *From: Kosinkadink*

- **Squish LoRA** (lora)
  - Creates squishing/crushing effects on objects, trigger: 'sq41sh squish effect'
  - *From: multiple users*

- **Cakify LoRA** (lora)
  - Transforms objects into cake versions
  - *From: JohnDopamine*

- **Street Fighter Hadoken LoRA** (lora)
  - Generates Street Fighter style energy attacks
  - *From: codexq*

- **Plushtoy morphing LoRA** (lora)
  - I2V LoRA for morphing objects into plush toys
  - *From: JohnDopamine*

- **Art style LoRA** (lora)
  - Custom art style LoRA trained for 3 days, works with both Wan and Hunyuan
  - *From: 211685818622803970*

- **Steamboat Willie LoRA** (lora)
  - Style LoRA for Steamboat Willie aesthetic, available for both 1.3B and 14B models
  - *From: Benjaminimal*

- **Steamboat Willie style lora** (lora)
  - 14B version trained for golden era animation style
  - *From: Benjaminimal*

- **Multiple concept loras series** (lora)
  - Bossfight, traveling, stairwell, kungfu, driving and parkour loras trained on 100 videos each
  - *From: Kytra*

- **Sci-Chrome artwork style lora** (lora)
  - Trained on artist's personal artwork style
  - *From: Jas*

- **Aging lora** (lora)
  - For aging effects in video generation
  - *From: NebSH*

- **Princess transformation lora** (lora)
  - Character transformation lora
  - *From: garbus*

- **KXSR Traveling Concept Lora** (lora)
  - Creates traveling/movement scenes, trained on 80+ videos with distinct captioning paradigm
  - *From: Kytra*

- **Left Pan Camera Lora** (lora)
  - Camera movement lora for left panning motion, trained using Blender with consistent movement
  - *From: ArtOfficial*

- **Ryza Character Lora** (lora)
  - Character lora for Atelier game character, available in both 1.3B and 14B versions
  - *From: Kytra*

- **First Person Flight Lora** (lora)
  - POV flying lora trained on Superman GoPro footage with hand visibility control
  - *From: Kytra*

- **Automated storyboarding system** (tool)
  - Fully automated system that generates multi-scene videos from reference images using LLM
  - *From: AJO*

- **Chasm's Call LoRA** (lora)
  - Cinematic concept LoRA for Pwnisher's youtube challenge, 1.3B and 14B variants
  - *From: Kytra*

- **Boss Fight LoRA** (lora)
  - LoRA for boss fight scenes, 1.3B model
  - *From: Fill*

- **Frutiger LoRA** (lora)
  - Trained at 10 epochs, 10 repeats, 395 steps per epoch with insane coherence
  - *From: Dream Making*

- **RES4LYF Sampling Suite** (node)
  - Advanced sampling nodes with regional conditioning, higher quality than standard samplers
  - *From: Clownshark Batwing*

- **Plant growth LoRA** (lora)
  - Training a LoRA on 70+ videos of plants for plant growth animation
  - *From: pom*

- **Rotate LoRA** (lora)
  - LoRA for rotation effects in video generation
  - *From: DawnII*

- **Panning LoRAs** (lora)
  - Training LoRAs for camera panning effects, struggling with following streets
  - *From: ArtOfficial*

- **Character LoRA** (lora)
  - 4800 steps of character lora training
  - *From: TimHannan*

- **Bloom filter in JovGLSL** (node)
  - Shader-based bloom effect using gamma ramp with area blur
  - *From: 137009159173308416*

- **Clownshark sampler beta with guide mode** (tool)
  - Sampler with guide mode functionality for using reference images in T2V generation
  - *From: Clownshark Batwing*

- **WanVideoWrapper** (node)
  - Kijai's ComfyUI wrapper for WAN video generation
  - *From: Kijai*

- **GraphCap captioning system** (tool)
  - AI captioning system for video with guided chain of thought and structured output for WAN prompting
  - *From: fearnworks*

- **Studio Ghibli LoRA** (lora)
  - LoRA for Studio Ghibli style video generation
  - *From: seruva19*

- **CivChan LoRA** (lora)
  - LoRA created for character consistency
  - *From: 88822364468412416*

- **Sci-chrome LoRA** (lora)
  - LoRA used for sci-fi chrome aesthetic
  - *From: Jas*

- **RES4LYF nodes** (node)
  - Custom nodes for temporal conditioning and attention masking
  - *From: Clownshark Batwing*

- **TheDirector** (tool)
  - Multi-scene video generation system with audio integration
  - *From: AJO*

- **Subject Replace workflow** (workflow)
  - Workflow for removing/replacing subjects in videos using VACE
  - *From: ArtOfficial*

- **Explosion style LoRA** (lora)
  - LoRA for 2D explosion effects contrasting realistic scenes, trained for 6000 steps
  - *From: ingi // SYSTMS*

- **Ghibli LoRA for 1.3B** (lora)
  - Studio Ghibli style LoRA working with 1.3B model
  - *From: 88822364468412416*

- **Horror/film industry LoRA** (lora)
  - LoRA for effects hard to do with CGI, for film industry course preparation
  - *From: Adrien Toupet*

- **Auto-prompting workflow** (workflow)
  - Modified LTXV workflow using Florence2 and Groq LLM API with Wan prompt guide integration
  - *From: stenandrimpy*

- **Bullet time LoRA** (lora)
  - Enables bullet time effects in generations
  - *From: ezMan*

- **Sci-chrome style LoRA** (lora)
  - Based on Flux Redux artwork mixing 4-5 images, trained on 30 images
  - *From: Jas*

- **Animation style LoRA from dataset** (lora)
  - Trained on user's dataset, maintains stroke style
  - *From: 88822364468412416*

- **Custom sigma scheduler node** (node)
  - Allows manual control of denoising schedule for improved movement
  - *From: Clownshark Batwing*

- **Pepe LoRA** (lora)
  - Works well for vid2vid, training by community member
  - *From: 88822364468412416*

- **2D FX LoRA** (lora)
  - Adds 2D effects without influencing overall style, trained through 50+ runs on H100s
  - *From: ingi // SYSTMS*

- **Rewanpatcher node** (node)
  - Enables regional conditioning with Wan models
  - *From: Clownshark Batwing*

- **Regional conditioning implementation** (workflow)
  - Model-agnostic regional conditioning system that works with Wan
  - *From: Clownshark Batwing*

- **Water FX LoRA** (lora)
  - Work-in-progress water effects LoRA showing interesting results
  - *From: ingi // SYSTMS*

- **Plushtoy morph LoRA** (lora)
  - LoRA for morphing humans into plush toys, trained on Skyreels V2 I2V
  - *From: JohnDopamine*

- **WanVaceToVideo native node** (node)
  - Native ComfyUI node for VACE workflow
  - *From: artemonary*

- **Tarot Card LoRA** (lora)
  - LoRA for Skyreels generating tarot card styled content
  - *From: 542962452988559360*

- **Custom liquid artwork LoRA** (lora)
  - LoRA trained on liquid artwork for Wan2.1, to be uploaded soon
  - *From: Zlikwid*

- **Ghibli LoRA** (lora)
  - LoRA with 1947 clips on Civitai, 1197 more prompts pending for testing
  - *From: seruva19*

- **Inflation LoRA** (lora)
  - Work-in-progress LoRA for inflation effects
  - *From: ingi // SYSTMS*

- **Clownshark's sampling nodes** (node)
  - Custom nodes with res_2m/res_2s samplers and bongmath methodology, work better than standard ksampler
  - *From: Clownshark Batwing*

- **Old Samsung Galaxy Ace 2 LoRA** (lora)
  - Trained on old Samsung Galaxy Ace 2 footage
  - *From: Dream Making*

- **Frutiger LoRA 14B** (lora)
  - Frutiger Aero style LoRA for Wan
  - *From: Dream Making*

- **CleanCore LoRA** (lora)
  - No captions, no trigger words LoRA
  - *From: Dream Making*

- **Morphing into plush toy LoRA** (lora)
  - I2V LoRA that morphs subjects into plush toys, trained on SkyReels v2
  - *From: JohnDopamine*

- **Pixel art LoRA** (lora)
  - Self-trained using NovelAI outputs for pixel art style generation
  - *From: 852話 (hakoniwa)*

- **Teen Titans Raven LoRA** (lora)
  - In progress training for Teen Titans style character consistency
  - *From: 138234075931475968*

- **Cyberpop style LoRA** (lora)
  - Style LoRA trained on batch of cyberpop style images
  - *From: JohnDopamine*

- **WanVideo CFG Schedule Float List node** (node)
  - Node to ramp up CFG in early steps to help retain style with LoRAs
  - *From: Zlikwid*

- **Toon LoRA** (lora)
  - Cartoon style LoRA for Wan, trained for 3000 buzz
  - *From: VRGameDevGirl84(RTX 5090)*

- **Cinematic LoRA** (lora)
  - LoRA for cinematic style video generation
  - *From: VRGameDevGirl84(RTX 5090)*

- **Raven Teen Titans LoRA** (lora)
  - Character LoRA for Raven from Teen Titans 2003
  - *From: 138234075931475968*

- **Liquid art LoRA** (lora)
  - LoRA for trippy liquid art style effects
  - *From: Zlikwid*

- **Video looping workflow** (workflow)
  - Custom workflow for creating seamless video loops using frame splitting and VACE inpainting
  - *From: Nathan Shipley*

- **VRGameDevGirl84's merged optimization model** (model)
  - T2V model with CausVid, AccVid, MPS rewards, women enhancer, and realism LoRAs merged with optimized settings
  - *From: VRGameDevGirl84*

- **AJO's character consistency workflow** (workflow)
  - Workflow for maintaining face and clothing consistency across multiple scene generations
  - *From: AJO*

- **A.I.Warper's long video generation system** (workflow)
  - Method for creating 400+ frame videos by chaining 81-frame generations with stitching
  - *From: A.I.Warper*

- **Anime mouth movement LoRA** (lora)
  - In-development LoRA trained on video clips to capture proper anime character mouth movements for talking
  - *From: AIGambino*

- **VRGameDevGirl84's T2V Master Model** (merge)
  - Merged model combining multiple LoRAs including CausVid and other improvements for better T2V generation
  - *From: VRGameDevGirl84(RTX 5090)*

- **Live Wallpaper LoRA** (lora)
  - LoRA trained for creating live wallpaper style animations, merged with CausVid in base model
  - *From: 211685818622803970*

- **ComfyUI-ZLUDA fork** (tool)
  - Fork enabling Wan to work on AMD GPUs through ZLUDA
  - *From: patientx*

- **Style LoRA in training** (lora)
  - Custom style LoRA at 120 epochs, upscaled and interpolated to 32fps, showing character style improvements
  - *From: 138234075931475968*

- **FusionX merge model** (model)
  - Merge that eliminates need for LoRAs and runs in 8 steps or lower
  - *From: VRGameDevGirl84(RTX 5090)*

- **Curly hair LoRA** (lora)
  - Trained on SDXL images and videos, possibly overtrained
  - *From: Thom293*

- **Graphic Novel Style LoRA** (lora)
  - Trained on 150 still images at 25-30 epochs for graphic novel aesthetic
  - *From: Thom293*

- **LaFerrari model LoRA** (lora)
  - Car model trained specifically for LaFerrari
  - *From: MisterMango*

- **Liquid art LoRA** (lora)
  - Trained on custom videos and still images for liquid effects
  - *From: Zlikwid*

- **I2V merge model** (model)
  - New image-to-video merge model in development
  - *From: VRGameDevGirl84(RTX 5090)*

- **VRGameDevGirl84's I2V merge** (model)
  - Modified version of T2V merge optimized for I2V with different LoRA combinations
  - *From: VRGameDevGirl84(RTX 5090)*

- **FusionX model** (model)
  - Optimized merge that cuts render time from 16+ minutes down to a few minutes
  - *From: VRGameDevGirl84(RTX 5090)*

- **Zlikwid WAN LoRA v2** (lora)
  - LoRA for WAN 2.1 14B model
  - *From: Zlikwid*

- **Retro 90s Anime Style LoRA** (lora)
  - Golden Boy anime style LoRA for both T2V and I2V, includes detailed training process documentation
  - *From: 138234075931475968*

- **FusionX LoRA** (lora)
  - LoRA extracted from FusionX merged model, equivalent to merging all component LoRAs
  - *From: VRGameDevGirl84(RTX 5090)*

- **Golden Boy Style LoRA** (lora)
  - Retro 90s anime style LoRA trained on 30 still images, captures mid-90s look especially environments
  - *From: 138234075931475968*

- **Kiss LoRA** (lora)
  - LoRA for kiss animations, works with fusion model
  - *From: Yae*

- **Particle Grid Animator** (tool)
  - Tool for creating motion patterns for ATI animations
  - *From: Nathan Shipley*

- **WAN Cinematic Video Prompt Generator** (tool)
  - ChatGPT tool trained on WAN docs to generate 5 prompts for any request
  - *From: VRGameDevGirl84(RTX 5090)*

- **Particle Grid Animator** (tool)
  - Fun to play with and exports usable tracks for ATI, keyframable, runs in browser, made with Claude Opus 4
  - *From: Nathan Shipley*

- **Phantom Merge with LightX** (model)
  - Merged LightX with Phantom using Phantom Merge as a base, removes causvid blotches at 4 steps
  - *From: Thom293*

- **Hologram displays LoRA** (lora)
  - Trained on hologram displays, does them pretty well, able to overlay a face and keep the details
  - *From: Thom293*

- **Custom character LoRAs** (lora)
  - Full body and face character LoRAs with custom training workflow
  - *From: Gateway {Dreaming Computers}*

- **Qwen prompt generator** (prompt)
  - Generates prompts for video generation model following 1970s Giallo film theme
  - *From: TK_999*

- **FusionX** (lora)
  - Collection of LoRAs that work together, trending on HuggingFace, provides accessibility to WAN
  - *From: VRGameDevGirl84(RTX 5090)*

- **Electric Alien WAN LoRA** (lora)
  - Retrain of Electric Alien for WAN, creates electrical effects
  - *From: JohnDopamine*

- **Color Correction LoRA V2** (lora)
  - Improves various problems beyond original focus, V3 coming with stronger sharpness
  - *From: 211685818622803970*

- **Endless travel workflow** (workflow)
  - Smooth video continuations with minimal seams, modified for native ComfyUI
  - *From: pom*

- **Two-pass upscaling workflow** (workflow)
  - Combines WAN diffusion v2v with non-diffusion upscaling to reach 1080x1920+
  - *From: The Shadow (NYC)*

- **Experimental general LoRA** (lora)
  - Testing how much random content can be crammed into a LoRA without breaking it
  - *From: Thom293*

- **Sketch LoRA for SDXL** (lora)
  - Currently training stage 2 of sketch LoRA
  - *From: Thom293*

- **20 Hunyuan LoRAs for Wan** (lora)
  - Converting 20 Hunyuan LoRAs for use with Wan, making 4 base models for different styles
  - *From: Thom293*

- **Multi-GPU nodes** (node)
  - Replaced regular loaders with multi-GPU versions for distributed processing
  - *From: el marzocco*

- **Latent sync tool** (tool)
  - New latent synchronization tool for video processing
  - *From: VRGameDevGirl84(RTX 5090)*

- **Color correction node** (node)
  - Helps keep video same color as reference image for I2V
  - *From: VRGameDevGirl84(RTX 5090)*

- **VACE frame strength node** (node)
  - Applies different strength to VACE frame
  - *From: Ablejones*

- **FusionX-VACE-FP8 model** (model)
  - Merged model with built-in realism
  - *From: VRGameDevGirl84(RTX 5090)*

- **HSD lora** (lora)
  - Greatly improves lightx2v motion without degrading colors/detail
  - *From: Jonathan*

- **Liquid ink LoRA** (lora)
  - Used in travel workflow generations
  - *From: NelsonPorto111*

- **90's vintage LoRA** (lora)
  - LoRA for vintage 90s style video generation, trained on vintage dataset
  - *From: VRGameDevGirl84(RTX 5090)*

- **Shinkai anime style LoRA** (lora)
  - Anime style LoRA used with VACE for character styling
  - *From: Cseti*

- **Goldenboy style LoRA** (lora)
  - LoRA for Goldenboy anime style
  - *From: el marzocco*

- **Wallace and Gromit LoRA** (lora)
  - LoRA for Wallace and Gromit character style
  - *From: Cseti*

- **LLM prompt description node** (node)
  - Custom node that uses LLM to describe reference images for better prompting
  - *From: ingi // SYSTMS*

- **Custom canny shader for Houdini** (tool)
  - Custom canny edge detection shader inside Houdini using COP + Karma for v2v workflows
  - *From: Andy Kush*

- **Wave distortion node** (node)
  - Custom node written by Grok 4 to add waves to videos and distort depth passes
  - *From: ingi // SYSTMS*

- **Magnifying glass control node** (node)
  - Custom node for magnifying specific areas as control for VACE
  - *From: ingi // SYSTMS*

- **Save queue nodes** (node)
  - Nodes for saving and loading generation queues to prevent loss when closing ComfyUI
  - *From: patientx*

- **FusionX merge workflow** (workflow)
  - Merged model combining WAN 2.1 14B 720p, Moviigen 1.0, LightXv2 1.0, MPS rewards 1.0, Motion boost 0.5, Realism boost 0.2, Detail enhancer 0.2
  - *From: patientx*

- **FusionX LoRA** (lora)
  - High-performance LoRA that works well at 4 steps with specific schedulers
  - *From: multiple users*

- **FaceNaturalizer LoRA** (lora)
  - Used with FusionX for improved face generation at 8 steps
  - *From: patientx*

- **OpenPose-compliant mesh for 3dsmax biped** (tool)
  - Mesh that mimics openpose skeleton, skinned to biped for VACE control
  - *From: Duranovsky*

- **Custom Sapiens node for mouth/lip separation** (node)
  - Provides better lip separation control for lip sync work, planned for release
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Trail generation node** (node)
  - Generates trails emitted from specific body parts for smoke/fire effects
  - *From: ingi // SYSTMS*

- **Graphic Novel Style LoRA** (lora)
  - Creates graphic novel style video generations, trained through multiple epochs
  - *From: Thom293*

- **FusionX model** (merge)
  - Cinematic quality merge, different from using LightX LoRA
  - *From: VRGameDevGirl84(RTX 5090)*

- **Lightning Ingredients Workflows** (workflow)
  - Modular LoRA-based approach for easy customization
  - *From: VRGameDevGirl84(RTX 5090)*

- **ComfyUI-ZLUDA fork** (tool)
  - Maintained for AMD users on Windows
  - *From: patientx*

- **Disney clips custom LoRA** (lora)
  - Trained on Disney animation clips
  - *From: notid*

- **Wallace and Gromit LoRA** (lora)
  - Works well with 'Lego animation' prompting
  - *From: U̷r̷a̷b̷e̷w̷e̷*

- **FusionX LoRA set** (lora)
  - Merged LoRA set including LightX2V and other optimizations
  - *From: patientx*

- **Fastwan LoRA** (lora)
  - LoRA extracted from 14B fastwan 480p model for faster inference
  - *From: DawnII*

- **Gurren Lagann style LoRA** (lora)
  - 441 images at 960x540 from first season, training for anime style
  - *From: 138234075931475968*

- **Golden Boy LoRA** (lora)
  - Anime-specific LoRA with detailed training process
  - *From: 138234075931475968*

- **WanVideoWrapper** (node)
  - ComfyUI wrapper for Wan models by Kijai
  - *From: Janosch Simon*

- **Prompt generator for Wan 2.2** (tool)
  - JavaScript prompt generator using Google AI Studio for Wan 2.2
  - *From: GOD_IS_A_LIE*

- **Claude/Gemini/GPT-4o prompt node** (node)
  - Node that uses AI to write prompts based on input images
  - *From: ingi // SYSTMS*

- **Character LoRA for Wan 2.2** (lora)
  - Requires both high noise and low noise LoRA versions
  - *From: el marzocco*

- **Custom GPT for Wan prompting** (tool)
  - Trained on official Wan fodder for generating prompts
  - *From: The Shadow (NYC)*

- **2.5d smoke and explosion LoRA** (lora)
  - Custom LoRA for creating 2.5D smoke and explosion effects
  - *From: ingi // SYSTMS*

- **GoldenBoy Style LoRA** (lora)
  - Anime style LoRA used at strength 1.0 on both high and low models for consistent anime aesthetics
  - *From: 138234075931475968*

- **Character LoRAs for Cyberpunk characters** (lora)
  - Panam character LoRA that works better with only low noise model loaded
  - *From: 465174342225887233*

- **Lightning LoRA for speed** (lora)
  - New lightning LoRA for faster generation, though some users prefer full model quality
  - *From: l҈u҈c҈i҈f҈e҈r҈*

- **Details LoRA** (lora)
  - LoRA for enhancing details, used in NebSH's workflow
  - *From: NebSH*

- **WanVideoWrapper by Kijai** (node)
  - ComfyUI implementation for Wan models
  - *From: various*

- **Character LoRAs for Wan 2.2** (lora)
  - Custom character training, can be challenging due to dual model system
  - *From: Cseti*

- **Lightning LoRAs v1.1** (lora)
  - Speed optimization LoRAs with improved quality over v1.0
  - *From: Kijai*

- **Upscaler workflow** (workflow)
  - Wan 2.2 14B upscaling workflow for enhancing existing videos
  - *From: thaakeno*

- **Additional schedulers hack for wrapper** (workflow modification)
  - Quick hack to use additional schedulers with the wrapper by loading GGUF model that doesn't actually load during generation but feeds into other components
  - *From: garbus*

- **Custom LoRAs for Wan 2.2** (lora)
  - Model handles training quite well for custom LoRAs
  - *From: Fill*

- **Character LoRA trained on fal** (lora)
  - LoRA that works well with conversion script from fal to ComfyUI
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Custom anime style LoRA** (lora)
  - Trained on Flux generations using 3 custom Flux LoRAs, one of which was trained on 2 custom SDXL LoRAs. Uses 32 images total.
  - *From: NebSH*

- **Anime LoRA from single show** (lora)
  - Trained on 368 screen captures and 79 video clips from one anime show, works well with LightX2V
  - *From: 138234075931475968*

- **Style LoRA** (lora)
  - Custom style LoRA trained on normal 2.2 model, prevents 'mecha' generating Gundams
  - *From: 138234075931475968*

- **VACE Phantom merge** (model)
  - Merged model by Inner Reflections available in WAN resources channel
  - *From: Abyss*

- **Merged Lightx2v LoRAs** (lora)
  - Merged various Lightx2v LoRAs using DARE/Concat methods with layer modifications
  - *From: JohnDopamine*

- **Steampunk Willy LoRA** (lora)
  - LoRA for steampunk character generation
  - *From: 422902797093306368*

- **People doing sigma face LoRA** (lora)
  - LoRA for sigma face expressions
  - *From: patientx*

- **Crash zoom LoRA** (lora)
  - LoRA for crash zoom camera effects
  - *From: patientx*

- **Melband audio node** (node)
  - Audio processing node for InfiniteTalk workflows
  - *From: Kijai*

- **KJ wrapper for S2V** (wrapper)
  - Fixes lag and corruption issues in native S2V workflow
  - *From: Kijai*

- **Batch masking workflow for MultiTalk** (workflow)
  - 2 masks and unite node for multiple character speaking
  - *From: 𝕯𝖗. 𝕸𝖆𝖈𝖆𝖇𝖗𝖊 ☠*

- **WanFaceDetailer** (tool)
  - Face detailing tool for improving face quality in Wan videos
  - *From: 1048309186322243594*

- **Custom Mecha Transformation LoRA** (lora)
  - Trained for mecha transformation style that works smoothly with Wan 2.2
  - *From: 312993351307755520*

- **Skin enhancer nodes** (node)
  - In development, trying to replicate Enhancer AI functionality for cleaning up plastic-looking skin
  - *From: asd*

- **MagicWan hybrid model** (model)
  - Wan 2.2 high+low hybrid model shared on Civitai
  - *From: patientx*

- **PatientX AMD fork** (tool)
  - ComfyUI fork for AMD users, downloaded 400+ times daily
  - *From: patientx*

- **Upscayl right-click integration** (workflow)
  - Right-click menu shortcut for auto 2x upscaling outside ComfyUI
  - *From: patientx*

- **ComfyUI Wan Prompt Generator English Fork** (node)
  - Translated version of Chinese Wan prompt generator for English users
  - *From: GalaxyTimeMachine (RTX4090)*

- **MagRef-InfiniteTalk Music Video Creator** (workflow)
  - Complex workflow for creating music videos with lip-sync using multiple scenes and audio timing
  - *From: VRGameDevGirl84(RTX 5090)*

- **Type animation LoRAs for 2.2** (lora)
  - LoRAs being developed for typography animation in Wan 2.2 high + low noise
  - *From: ingi // SYSTMS*

- **Tiled processing workflow** (workflow)
  - Reworked workflow for processing videos at higher resolutions using tiling approach
  - *From: 153803064858378240*

- **USDU wrapper for Wan** (workflow)
  - USDU implementation for Wan video upscaling with tiling support
  - *From: 153803064858378240*

- **HuMo endless workflow** (workflow)
  - One-shot workflow that generates multiple 3-second segments with individual prompts and combines them
  - *From: VRGameDevGirl84(RTX 5090)*

- **FakeVace model merges** (model)
  - 50/50 merges of Fun/Fake VACE models using Claude Opus scripted merger
  - *From: JohnDopamine*

- **Dixamaru 3 ksampler workflow** (workflow)
  - 3 ksampler workflow that produces clean clips with good sharpness and no color shifting
  - *From: asd*

- **Wan 2.2 Mega Rapid AIO** (workflow)
  - All-in-one rapid workflow for Wan 2.2 by Phr00t
  - *From: garbus*

- **Video splitter node** (node)
  - Splits videos into segments to avoid multiple load video nodes, works with any video input including WAN VACE
  - *From: VRGameDevGirl84(RTX 5090)*

- **Humo endless video-to-video workflow** (workflow)
  - Automated workflow for creating long-form video content with Humo model
  - *From: VRGameDevGirl84(RTX 5090)*

- **Style frame insertion node** (node)
  - Creates image sequences with style frames and matching masks, simplifying the workflow setup
  - *From: ingi // SYSTMS*

- **Auto music video workflow** (workflow)
  - Automatically creates videos of any length matching song duration with auto-indexing and combining
  - *From: VRGameDevGirl84(RTX 5090)*

- **Custom LoRA for 2.2** (lora)
  - Originally trained on 2.1, being retrained for 2.2
  - *From: ingi // SYSTMS*

- **Modified WanVideo Long I2V Multi node** (node)
  - Modified to use multiple frames instead of just first frame for smoother clip continuity
  - *From: Rävlik*

- **HuMo I2V modification** (workflow)
  - Small code change that allows HuMo to work as I2V for basic extensions from single image
  - *From: Ablejones*

- **ComfyUI-SuperUltimateVaceTools** (tool)
  - Used for VACE 1.0 Style Transfer with upscale functionality
  - *From: Дмитрий Марков*

- **Phantom Merge model** (model)
  - Custom controlnet setup with overlapping pose over black blurred mask and line art to help capture tricky camera arcs and scene rotations
  - *From: Dkamacho*

- **HuMo Music video creator workflow V6** (workflow)
  - Totally automated workflow for creating music videos from image and song input
  - *From: VRGameDevGirl84(RTX 5090)*

- **Custom nodes for LLM context** (node)
  - Updated custom nodes to add more context to prompts for LLM processing
  - *From: VRGameDevGirl84(RTX 5090)*

- **Fast film grain node** (node)
  - Node for adding film grain effects
  - *From: VRGameDevGirl84(RTX 5090)*

- **WanAnimate animal detection** (workflow)
  - Using VIT Pose for animal skeleton detection with WanAnimate
  - *From: Nathan Shipley*

- **HuMo workflow** (workflow)
  - Automated lip-sync workflow that takes audio input and generates lip-synced videos using LLM prompts, getting mouth sync issues resolved
  - *From: VRGameDevGirl*

- **Automatic movie generator** (workflow)
  - Takes short prompt and creates edited scene with Suno music and titles
  - *From: Simonj*

- **WanVideoWrapper improvements** (tool)
  - Kijai's wrapper with example workflows and SAM masking for character replacement
  - *From: Kijai*

- **Kinestasis concept LoRA** (lora)
  - Adds motion injection capability for T2V and I2V
  - *From: Cseti*

- **Custom ChatGPT prompting node** (node)
  - Gets ChatGPT to write Wan-style prompts based on input frames
  - *From: ingi // SYSTMS*

- **New style LoRA trained on MJ sref** (lora)
  - Style LoRA being tested, took 3+ hours to train
  - *From: NebSH*

- **RCM LoRA** (lora)
  - Custom LoRA being tested for specific visual effects
  - *From: JohnDopamine*

- **LazySusan LoRA** (lora)
  - Camera rotation LoRA trained on 6 videos from higgfields, works with both I2V and T2V, trained at 150 steps for $7.5
  - *From: NebSH*

- **Custom image loop node** (node)
  - Node for loading batch of pre-made images for overnight automated processing
  - *From: The Coin Hunter*

- **Prompt creator node V7** (node)
  - Automated LLM-based prompt generation from lyrics and user categories with dropdown options
  - *From: VRGameDevGirl84(RTX 5090)*

- **Rick and Morty style LoRA for WAN 2.1** (lora)
  - Style transfer LoRA for Rick and Morty animation style
  - *From: Dever*

- **Motion LoRA for WAN** (lora)
  - Trained on 7 videos with 33 frames each, creates interesting motion effects for motion graphics and product videos
  - *From: AshmoTV*

- **Gemini-generated LLM prompt for morphing** (prompt)
  - Visual Effects Director prompt for UMT5-XXL-BF16 with comprehensive morphing instructions and hard constraints
  - *From: 𝕯𝖗. 𝕸𝖆𝖈𝖆𝖇𝖗𝖊 ☠*

- **WAN HuMo music video workflow** (workflow)
  - Workflow combining WAN with HuMo for creating music videos
  - *From: VRGameDevGirl84(RTX 5090)*

- **Fill's RIFE node** (node)
  - 10x faster RIFE implementation
  - *From: Fill*

- **Custom transition LoRA** (lora)
  - Trained on 10 videos with morphing transitions
  - *From: AshmoTV*

- **Car transformation LoRA** (lora)
  - Trained on car to car transformation dataset, some overtraining issues
  - *From: AshmoTV*

- **SVI workflow with multiple extensions** (workflow)
  - Allows multiple extensions via variables
  - *From: Vérole*

- **Full auto workflow with AI decision making** (workflow)
  - Uses Qwen 2.5 VL 7b to decide what happens next
  - *From: Vérole*

- **VRGameDevGirl HuMo nodes** (node)
  - Story mode nodes for HuMo
  - *From: fearnworks*

- **Audio reactive workflow** (workflow)
  - Speed reactive nodes for audio synchronization
  - *From: 272911326010015745*

- **WAN Animate lightweight workflow** (workflow)
  - Optimized workflow for WAN Animate
  - *From: TimHannan*

- **Playblast/3D viewport LoRA** (lora)
  - Trained on playblast videos and 3D software UI, low poly models, rigs - creates 'it's not AI, here's the playblast to prove it' effect
  - *From: ingi // SYSTMS*

- **Mechanical transformation LoRA** (lora)
  - For mechanical transformation effects, currently undercooked but being improved
  - *From: AshmoTV*

- **Photogrammetry and lidar scans LoRA** (lora)
  - Trained on photogrammetry and lidar scans, produces freaky results
  - *From: ingi // SYSTMS*

- **HuMo I2V patch** (tool)
  - Patch to allow HuMo to work with I2V
  - *From: Ablejones*

- **Pencil drawing LoRA for Wan 2.2** (lora)
  - Private LoRA that creates ink pen drawing style
  - *From: KevenG*

- **Jujutsu Kaisen LoRA trained with contrastive loss** (lora)
  - Anime style LoRA trained on videos using contrastive loss for better results
  - *From: samurzl*

- **Audio delay node** (node)
  - Simple node to add silence and counter audio/video timing issues
  - *From: JohnDopamine*

- **Bano LoRA trained on I2V** (lora)
  - LoRA trained specifically on I2V data
  - *From: NebSH*

- **Exploded effect LoRA** (lora)
  - LoRA for water bending/explosion effects trained on higgsfield dataset
  - *From: AshmoTV*

- **Transition LoRA** (lora)
  - LoRA for seamless transitions between scenes, trained with Gemini 3 captions
  - *From: ingi // SYSTMS*

- **WanVaceAdvanced nodes** (node)
  - Custom nodes to properly match Vace controls with Phantom and handle latent masking
  - *From: Ablejones*

- **Custom HuMo implementation** (node)
  - Allows multiple image references and starting image frame input for native ComfyUI
  - *From: Ablejones*

- **WanKeyframeBuilder** (node)
  - Creates timeline with batch of images and masks for WAN 2.2, configurable mask strength for long generations
  - *From: Chandler*

- **Custom SAM3 masking nodes** (node)
  - Nodes for segmenting scene parts and expanding them over frames, includes noise addition to masks
  - *From: FlipYourBits*

- **VACE keyframe builder** (node)
  - Node to place keyframes for VACE system
  - *From: Flipping Sigmas*

- **Embroidery LoRA** (lora)
  - Provides detailed thread animations in close-up macro scenes
  - *From: AshmoTV*

- **Knitting style LoRA** (lora)
  - LoRA for knitting-style animations and effects
  - *From: AshmoTV*

- **Water morphing LoRA** (lora)
  - LoRA for water morphing effects
  - *From: AshmoTV*

- **Automation system with fallback mechanism** (tool)
  - System using WAN + Grok Imagine + Gemini Pro 3 for automated video generation
  - *From: gpbhupinder*

- **Custom VACE reference input optimization** (node)
  - Custom code to make VACE reference inputs lighter so you don't need to encode control video for each different reference
  - *From: Ablejones*

- **Audio reactive pose node integration** (workflow)
  - Using audio reactive pose node with SCAIL for synchronized character animation
  - *From: NebSH*

- **WanSoundTrajectory** (node)
  - Audio reactive video generation tool
  - *From: ckinpdx*

- **VACE clip joiner workflow** (workflow)
  - Seamlessly joins video clips with transitions
  - *From: Vérole*

- **Exploded effect LoRA** (lora)
  - Creates explosion effects, needs good prompt to shine
  - *From: AshmoTV*

- **WanVaceAdvanced nodes** (node)
  - Advanced VACE control nodes with context windows
  - *From: Ablejones*

- **Impasto paint smears LoRA** (lora)
  - Training a new LoRA for impasto paint smear effects, works with FFLF
  - *From: AshmoTV*

- **Exploded effect v2 LoRA** (lora)
  - LoRA for explosion effects, can be combined with other LoRAs like 360 rotation
  - *From: AshmoTV*

- **Inflation LoRA** (lora)
  - Re-training inflation LoRA with completely new dataset to handle inflating people not just clothing
  - *From: ingi // SYSTMS*

- **Transition LoRA** (lora)
  - LoRA for assisting transitions between clips, works well with FFLF and connecting different pre-existing clips
  - *From: ingi // SYSTMS*

- **HardCut LoRA** (lora)
  - LoRA used with SVI for scene transitions, works well when seed is lucky
  - *From: patientx*

- **Saturday Morning Cartoons LoRA** (lora)
  - LoRA for cartoon-style animation, used with InfiniteTalk
  - *From: U̷r̷a̷b̷e̷w̷e̷*

- **Expl0sion Lora V2** (lora)
  - Explosion effects LoRA
  - *From: AshmoTV*

- **Beat editor Gradio app** (tool)
  - App for creating video cuts with intro/outro functionality
  - *From: VRGameDevGirl84(RTX 5090)*

- **Control LoRAs for Wan and Qwen Edit** (lora)
  - Control LoRAs made by ingi for various models
  - *From: ingi // SYSTMS*
