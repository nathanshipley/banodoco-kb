# Wan Chatter Knowledge Base
*Extracted from Discord discussions: 2025-07-01 to 2025-08-01*


## Technical Discoveries

- **bypassing clip vision encode in i2v improves motion**
  - Removing clip vision encoding step can improve motion quality in image-to-video generation
  - *From: zoz*

- **RES4LYF res_6s/bong_tangent for production quality**
  - Using RES4LYF with res_6s/bong_tangent settings for higher quality production output
  - *From: TK_999*

- **Creating precise keyframes helps more than using ref image**
  - Making precise keyframes is more effective than using reference images because the model has to stretch itself less
  - *From: Rishi Pandey*

- **SAGEATT 1 works on RTX 2060**
  - Successfully running with noticeable speed improvement, though not as advanced as SAGEATT 2
  - *From: hicho*

- **Bluetooth headset causes audio sync issues with VHS preview**
  - Huge delay on bluetooth headset despite 5+ years of use without noticing issues
  - *From: Kijai*

- **VHS loader audio export doesn't respect frame cap**
  - Exports longer audio than video when cutting clips, causing sync issues in longer runs
  - *From: Tango Adorbo*

- **Dual sampling technique for video masking**
  - Sample first steps to get shape, then use that as mask for rest of generation to avoid unwanted changes
  - *From: Mads Hagbarth Damsbo*

- **Custom mask sampler creates control embeddings**
  - Combines two ksamplers and a mask (eroded and multiplied with diff between unconditional and conditional sampling)
  - *From: Mads Hagbarth Damsbo*

- **Higher shift values (11) better at keeping character consistency**
  - Shift 11 shows improved character preservation vs lower values
  - *From: Kijai*

- **Sage Attention 2.2++ released with performance improvements**
  - New version available but may have compatibility issues with flash_attn
  - *From: yi*

- **Radial attention integration speeds up Wan significantly**
  - Wan14B SVDQuant + Radial + Sage + Light2xv = 30 seconds for 1280*720*81 frame videos
  - *From: yi*

- **LightX2V LoRA at 4 steps provides 5-10x speed improvement**
  - Dramatic speed boost with seemingly no major trade-offs
  - *From: Shawneau 🍁 [CA]*

- **Context windows don't have degradation but require uni3c**
  - No degradation but overall movement is reduced significantly
  - *From: Kijai*

- **MultiTalk affects whole target, not just mouth**
  - The effect extends beyond lip sync to influence entire subject
  - *From: Kijai*

- **Motion_frame parameter affects context window behavior**
  - Testing motion_frame setting of 25 vs 16 shows different results, might control overlap in context windowing
  - *From: Kijai*

- **VACE can work as V2V with low denoise**
  - Successfully used VACE for video-to-video with low denoise settings, can activate LoRAs without prompts
  - *From: hicho*

- **WAN T2V models can generate images effectively**
  - WAN T2V models produce good quality images for text-to-image generation, potentially useful for creating reference frames
  - *From: VRGameDevGirl84(RTX 5090)*

- **LightX2V LoRA strength affects quality**
  - Adjusting LightX2V LoRA strength along with shift, steps, and scheduler can improve results
  - *From: Kijai*

- **Wan works well for single frame generation (text-to-image)**
  - Can generate high quality single frames using T2V model with 1 frame, works better than expected for image generation
  - *From: VRGameDevGirl84(RTX 5090)*

- **LoRAs have massive impact on Wan image quality**
  - Even a small, poorly trained vintage LoRA dramatically improves image quality when combined with LightX LoRA
  - *From: VRGameDevGirl84(RTX 5090)*

- **Skyreels excellent for text-to-image generation**
  - Skyreels T2V model produces very high quality single frame generations, potentially better than Wan for T2I
  - *From: VRGameDevGirl84(RTX 5090)*

- **VACE works with single frame generation for reference**
  - Single frame generation is good way to test how inputs will behave before running longer generations
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Control inputs work in Wan text-to-image**
  - ControlNet depth and other controls work when using Wan for single frame generation
  - *From: VRGameDevGirl84(RTX 5090)*

- **CausVid works better with Phantom model**
  - Works better causvid too
  - *From: chrisd0073*

- **GGUF versions of MAGREF are now available**
  - oooh GGUFs for MAGREF are out at quantstack just spotted them. That's the first GGUF for that model
  - *From: mdkb*

- **Block conditioning allows injecting different prompts into specific DiT blocks**
  - Main Condition: 'A profile shot of a cat walking approaching the camera. The background is a Italian plaza' + Injected Condition in block 8,9 and 10: 'Underwater wide shot from a man swimming at a coral reef, caustics cast on the ground'
  - *From: Mads Hagbarth Damsbo*

- **Self-forcing LoRA enables 4-8 step generation with CFG 1.0**
  - throw it in, do 4-8 steps LCM normal sampler... CFG 1, and the negative prompt is ignored
  - *From: izashin*

- **Wan text2image is 3x faster than Flux**
  - Performance comparison showing significant speed advantage
  - *From: N0NSens*

- **Sky prompt generates different faces and compositions while vanilla generates one face and composition**
  - Testing with 3 seeds showed variation differences between prompts
  - *From: N0NSens*

- **MAGREF GGUF provides better accuracy than Phantom for I2V**
  - First test showed way better results than Phantom for accuracy, perfect match for image of 5 people and beer bottle with branding
  - *From: mdkb*

- **VACE can do text generation on objects**
  - Successfully generated text 'VACE' on woman's forehead with prompt, understands spatial positioning
  - *From: hicho*

- **VACE works better for inpainting than older methods**
  - Better than ProPainter or AnimateDiff-based inpainting solutions
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Desaturating and blurring normal maps makes them work better with VACE**
  - Converts normals to more depth-like input that VACE can understand
  - *From: Kijai*

- **Darkening depth maps improves facial consistency in VACE**
  - User achieved better consistency by darkening the depth map
  - *From: yukass*

- **NAG slows down inference by 3x**
  - Performance testing showed significant slowdown when using NAG
  - *From: ˗ˏˋ⚡ˎˊ-*

- **LightX2V distill is intended to use LCM + uniform scheduler**
  - The distill lora is specifically designed to work with LCM scheduler and ddim_uniform, not euler/simple
  - *From: Screeb*

- **Reference images in VACE need white border padding to work properly**
  - Without white borders, reference images get ignored in VACE. Adding 20% white padding around reference images solves masking issues
  - *From: Hashu*

- **ddim_uniform scheduler with lcm sampler provides better seed variance and style prompt adherence**
  - Compared to euler/simple which produces very similar compositions and cliched stock footage-like results, ddim_uniform gives more varied results and better respects prompts like 'muted colours'
  - *From: Screeb*

- **Wan 2.1 excels at image generation with fast performance**
  - 6 seconds on PC vs 17 seconds for Flux at same 1344x768 resolution, particularly good at nature scenes
  - *From: N0NSens*

- **Full HD ultrawide video generation is possible with 14B model**
  - 1920x1072 resolution, 49 frames worked using only 75% VRAM, though very slow at 6 steps
  - *From: David Snow*

- **VACE prompt specificity is crucial for reference image adherence**
  - Being very explicit about what to do with the reference image in the prompt makes VACE work 10x better, even single word changes can dramatically improve results
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Frame count aliasing follows 4n+1 rule but with unexpected behavior**
  - MultiTalk doesn't follow expected 4n+1 rounding - asking for 250 frames gives 305, asking for 209 gives 249, requires trial and error to get desired frame counts
  - *From: AJO*

- **LightX2V LoRA works best at 4 steps, causes snow/artifacts at higher step counts**
  - Running LightX2V at 10 steps causes white dust/snow artifacts, but works clean at 4 steps
  - *From: Atlas*

- **Wan 14B at 1920 resolution eliminates visual artifacts**
  - At 1920 resolution, stipple artifacts associated with Wan disappear, even at just 6 steps
  - *From: David Snow*

- **Sharp masks work better than feathered masks for VACE inpainting**
  - Feathered/soft masks add halos around objects, sharp masks give better blending results
  - *From: David Snow*

- **VACE works well with SAM2 masks for people but struggles with backgrounds**
  - 100% success rate targeting SAM2 masked people with LoRA, 1% success with other objects using reference images
  - *From: mdkb*

- **Prompt specificity crucial for VACE reference images**
  - Failed with 'a dog is walking down a corridor' but worked with 'a dog is walking down a corridor, with it's tongue flapping out happily'
  - *From: Kijai*

- **16fps produces better faces than 24fps**
  - User getting better face results since switching from 24fps to 16fps video upload
  - *From: xwsswww*

- **E5m2 quantization works with torch.compile on AMD GPUs**
  - While using torch.compile if the model is e5m2 instead of the usual e3m4fn it is usable for AMD GPU and works well
  - *From: patientx*

- **Converting fp16 to fp8_e5m2 is higher quality than converting from fp8_e3m4fn**
  - fp8_e3m4fn has 3 bits for the exponent, while fp8_e5m2 has 5, but you're not making use of that 5 since you started with only 3 bits when converting from e3m4fn
  - *From: patientx*

- **GGUF LORA applying works without merging**
  - LoRA weight is added on the dequantized weight directly, means the lora is then used at its full precision and can set strength at any point
  - *From: Kijai*

- **Q8 GGUF easily beats fp8 in quality**
  - Q8 is much closer to fp16 than fp8, and about same size
  - *From: Kijai*

- **1600p seems to be the sweet spot for generation**
  - 1600p (longest side) then upscale from there gives significantly nicer results than 720p
  - *From: David Snow*

- **Native text encoder with fp8 works better for VRAM management**
  - Use bridge node to use native text encoder, download umt5 fp8, helps with OOM issues
  - *From: hicho*

- **E5M2 format differences from E4M3FN**
  - E5M2 has wider range but lower precision (5 bits exponent, 2 bits mantissa), E4M3FN has higher precision but narrower range (4 bits exponent, 3 bits mantissa)
  - *From: fredbliss*

- **Speed LoRAs work well at 4 steps with wrapper**
  - Using LightX2V LoRA with 4 steps produces clean results
  - *From: David Snow*

- **Silent audio track controls character speech in MultiTalk**
  - Audio 1 controls the character on the far left. Adding silent audio track can make characters stop speaking
  - *From: yukass*

- **Context frames don't work with I2V**
  - Context features only work with T2V, not I2V. For longer I2V generations, need to use VACE extension
  - *From: Kijai*

- **ExVideo LoRA only works with 1.3B model**
  - ExVideo LoRA is limited to the 1.3B variant
  - *From: Kijai*

- **VACE inpainting uses two types of masks**
  - Grey area on video for inpainted mask, black/white mask for VACE encoder where black areas stay same and white is modified
  - *From: Valle*

- **Differential diffusion mask on WanVideo encode node**
  - Can diffuse main character at 1.0 and background at 0.2 for precise control
  - *From: David Snow*

- **Wan 14B works well for T2V fashion photography**
  - Much faster than other models and handles fashion photography very well
  - *From: David Snow*

- **GGUF models work with loras and don't need low_mem_load option**
  - GGUF support allows using loras and can set use_non_blocking to true without CUDA errors
  - *From: Cseti*

- **Frame count calculation for Wan**
  - Number of frames = (value - 1) / 16, and frames should divide evenly (e.g., 33 works, 30 doesn't)
  - *From: Kijai*

- **ATI Tracks requires a custom ATI model to work properly**
  - Using the wrong model results in objects not following tracking paths at all
  - *From: Juampab12*

- **Unianimate and uni3c controls fight when used together**
  - Both try to place characters in different positions, causing conflicts
  - *From: Juampab12*

- **VACE control video frame count must match generation frame count**
  - Mismatched frame counts cause issues in VACE workflows
  - *From: Juampab12*

- **VACE is limited to 81 frames**
  - Cannot generate beyond this frame limit
  - *From: Juampab12*

- **Inpainting works only with gray area without input mask in VACE encode**
  - Input mask 'locks' the area, without it WAN is free to change more than the area
  - *From: Valle*

- **FreeInit can be used iteratively by chaining samplers**
  - Multiple iterations possible for refinement but with heavy time penalty
  - *From: Kijai*

- **Static points needed for ATI to prevent unwanted camera movement**
  - Shows the model that camera shouldn't be moving
  - *From: Juampab12*

- **MAGREF clip embed makes huge impact on reference adherence**
  - Clip embed can cause outputs that look nothing like the reference, disabling it improves reliability significantly
  - *From: DawnII*

- **VACE start/end frame node has new index functionality**
  - Updated logic allows placing frames at any index instead of just first/last positions
  - *From: Kijai*

- **Audio_scale parameter dramatically affects MultiTalk lip-sync quality**
  - Default is 1.0, increasing to 2-3 improves sync significantly, but may introduce artifacts at higher values
  - *From: Charine*

- **FusionX LoRA already contains CausVid**
  - Should not stack FusionX and CausVid LoRAs together as they contain overlapping functionality
  - *From: VRGameDevGirl84(RTX 5090)*

- **LightX2V repository showing increased activity**
  - Multiple recent commits suggesting potential new release preparation
  - *From: JohnDopamine*

- **GGUF model quantization levels have different compatibility**
  - Q4 may have issues, Q6 initially worked best, Q5 and Q8 confirmed working
  - *From: Kijai*

- **Using no prompts with VACE works better when using reference/starting image**
  - When using VACE with reference images, leaving prompts empty produces better results
  - *From: Draken*

- **Torch.compile or RoPE chunking reduces VRAM usage by ~2GB**
  - Either torch.compile or the new chunked RoPE calculation reduces peak VRAM usage by at least 2GB on default 832x480x81 resolution, with larger differences at higher resolutions
  - *From: Kijai*

- **1600p generation gives most benefits of 1920p with better performance**
  - Generating at 1600 pixels instead of 1920 provides most of the quality benefits while being more manageable for upscaling
  - *From: David Snow*

- **Padding depth controlnet helps position objects in scene center**
  - Using KJ's pad image node to place depth maps in center of frame helps position objects in the middle of the background generation
  - *From: hicho*

- **Context windows have no degradation over time but slow down process significantly**
  - Context windowing method maintains quality throughout generation but drastically increases processing time
  - *From: Kijai*

- **GGUF support in WanVideoWrapper enables higher frame counts on lower VRAM**
  - 3060 12GB can now do 1600x900x49 frames in 20 mins, or 1080px41 frames in 40 mins using GGUF models
  - *From: mdkb*

- **SageAttention was never enabled for VACE blocks**
  - Kijai discovered he wasn't passing attentionmode arg to VACE blocks, enabling it made VACE 20% faster
  - *From: Kijai*

- **Torch.compile memory behavior with if/else statements**
  - Having if/else statements in torch.compile code increases memory use even if branches are never reached. Commenting out enhance-a-video check dropped memory use by 700MB
  - *From: Kijai*

- **WanVideoWrapper width value caps at 2048**
  - Width caps at 2048 while height caps at 29048, likely just never thought about higher widths
  - *From: Hashu*

- **1080p resolution improves face structure over 720p**
  - WAN is 720p trained but 1080p generation provides better face structure at middle distance and for crowds/fast camera moves
  - *From: mdkb*

- **GGUF format significantly improves quality and performance for Wan wrapper**
  - User reports GGUF was 'so worth it' and quality is 'crisp' compared to standard format
  - *From: hicho*

- **Chrome browser uses 4x more VRAM than Edge for background tasks**
  - Chrome takes 120MB VRAM while MS Edge takes 30MB - optimization tip for VRAM management
  - *From: hicho*

- **ComfyUI chunked saves 1GB VRAM compared to standard ComfyUI option**
  - Same speed performance but with memory savings
  - *From: hicho*

- **Kijai implemented chunking for RoPE and FFN layers**
  - Chunking both RoPE and FFN to 4 chunks shows significant VRAM reduction in spikes, helps even with torch compile
  - *From: Kijai*

- **Wan Vace has better color matching than base I2V**
  - Vace stays much closer to input image colors and salvaged heavily color shifted generations
  - *From: Hashu*

- **Wan 2.1 animation workflow - 81 frame simple animation took 5 minutes straight from Cascadeur**
  - Can do styling in ComfyUI VACE workflow afterwards
  - *From: mdkb*

- **Semi-transparent masking objects in Control Video work effectively**
  - Using 95% opacity allows VACE to 'peek' and see overlaid objects like fingers, preventing some VACE imagination
  - *From: AmirKerr*

- **VACE ref_images parameter accepts concatenated images but shouldn't be used with videos**
  - Bad idea to put video with many frames there as it automatically concatenates
  - *From: Kijai*

- **Growing mask by 30 pixels enables wild transformations**
  - Example: turned ballerina into SpongeBob, mask expansion allows more dramatic changes
  - *From: David Snow*

- **VACE reference images require white padding/background to work properly**
  - Reference image should have white border around it or subject on full white background for VACE to recognize it
  - *From: Hashu*

- **MultiTalk seed was not working properly**
  - MultiTalk 02 workflow with multitalk sampling method was never using the seed as copied code was just torch.randn without any seed gen linked, now fixed
  - *From: Kijai*

- **Easy Cache works with LightX2V**
  - Results with 6 steps without cache and 10 steps with cache (ending up doing 6 steps) are pretty much the same
  - *From: Kijai*

- **UniPC scheduler gives better details than LCM**
  - LCM was giving blurry results compared to UniPC scheduler
  - *From: xwsswww*

- **Film grain helps trigger model to work on areas**
  - Film grain adds noise and helps trigger the model to work on specific areas, similar to blur but reversible
  - *From: mdkb*

- **Shift modifies sigmas and noise strength**
  - More shift = stronger noise strength, modifies the sigmas curve
  - *From: Kijai*

- **Settings between 0.005 and 0.010 work well**
  - Recommended range for a specific parameter
  - *From: xwsswww*

- **Wan 2.1 gguf provides way better results than AnimateDiff**
  - Can run on 8GB card with quantization
  - *From: xwsswww*

- **VACE can achieve excellent face likeness with proper masking**
  - Using sloppy mask and depth/lineart control with reference image
  - *From: Hashu*

- **Lineart needs to be inverted to work properly with VACE**
  - Black lines on white background required
  - *From: Hashu*

- **Pusa works with lightx2v distill lora**
  - Still has start noise issues but functional
  - *From: Kijai*

- **Anysora is better for 2D content**
  - Character consistency is a big upgrade
  - *From: Rainsmellsnice*

- **Mask input discovered for WanVideo Encode node**
  - Can use mask rendered from Blender with different noise_aug_strengths
  - *From: xwsswww*

- **Pad function now follows crop position**
  - Sneaky update made few days ago
  - *From: Kijai*

- **WAN 2.1 T2V model performs excellently for text-to-image generation**
  - WAN 2.1 T2V model demonstrates strong capabilities for still image generation, not just video
  - *From: slmonker(5090D 32GB)*

- **New LightX2V LoRAs with rank64 available**
  - Both T2V and I2V models now have rank64 LoRA versions, higher rank than previous rank32
  - *From: slmonker(5090D 32GB)*

- **WAN supports Chinese prompts very well**
  - WAN 2.1's model has strong support for Chinese language prompts
  - *From: slmonker(5090D 32GB)*

- **Model merging with Skyreels v2 improves results**
  - Merging WAN T2V with Skyreels v2 at 0.3 ratio boosts prompt adherence and physics understanding
  - *From: ▲*

- **FreeNoise in context options can cause artifacts**
  - Artifacts were resolved by addressing FreeNoise settings in context options
  - *From: Valle*

- **New distilled models work in 2-4 steps**
  - New distill model generates in 2 steps for T2V, 4 steps for I2V with good quality
  - *From: hicho*

- **I2V LoRA works much better for image to video**
  - New I2V light2vx lora is much better motion/prompt following, night and day difference
  - *From: Ada*

- **I2V LoRA works with VACE despite errors**
  - i2v lora works with VACE despite shape mismatch warnings
  - *From: Piblarg*

- **Most users prefer 480p model over 720p**
  - 480p model preferred by most users, 720p doesn't show perceptible quality improvement
  - *From: multiple users*

- **Diffusers 0.34.0 version being used**
  - Users running diffusers version 0.34.0
  - *From: ˗ˏˋ⚡ˎˊ-*

- **New LightX2V v2 distill models released with separate T2V and I2V versions**
  - They released further tuned T2V and also 480P and 720P I2V versions - 4 different Lightx2V distill models total now
  - *From: Kijai*

- **New LightX2V v2 models show improved motion and less burning**
  - Multiple users confirmed more motion, less burnt appearance, better prompt following compared to v1
  - *From: multiple users*

- **Kijai created fast LoRA extraction node using torch.svd_lowrank**
  - Extracts 14B lora in under a minute, 30x faster than previous method while giving good results
  - *From: Kijai*

- **Higher LightX2V strength (1.5-2.0) can improve results but may cause burning**
  - Multiple users tested strength >1.0 with good results, though spatial quality can suffer and illustration style may be lost
  - *From: Hashu*

- **I2V LightX2V works better for VACE than T2V version**
  - Users reported better results using I2V lora even on VACE workflows compared to T2V lora
  - *From: The Shadow (NYC)*

- **VACE can control camera movement using wireframe cube control inputs**
  - Feeding wireframe cube animation to VACE control input creates camera movement that continues through daisy-chained batches
  - *From: The Shadow (NYC)*

- **White dot on dark background can control subject movement in VACE**
  - A simple white dot animation on dark background fed to VACE input_frames controls subject positioning and movement
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Pusa LoRA works with T2V models for I2V generation**
  - Using T2V model + Pusa LoRA with first latent in noise being the image creates I2V functionality with very natural motion
  - *From: Kijai*

- **Pusa motion quality is superior to standard models**
  - Motion appears more realistic and alive compared to standard Wan models, though with some quality tradeoffs
  - *From: Juampab12*

- **LightX2V LoRA provides significant quality improvements at 6 steps**
  - Base model with new LightX2V LoRA at 6 steps produces crisp results comparable to Wan AI site quality
  - *From: garbus*

- **Pusa uses similar sampling approach to Diffusion Forcing**
  - The modulation difference in sampling is pretty much same as in DiffusionForcing, uses per-frame timesteps
  - *From: Kijai*

- **Pusa Lora works at strength 1.4 by default**
  - Default lora strength is 1.4, didn't work at 1.0
  - *From: Kijai*

- **Pusa can use any number of frames to continue from**
  - Can also do in-between frames
  - *From: Kijai*

- **Multitalk can generate 10-15 seconds before degradation**
  - It's like a loop that continues from last frame
  - *From: Kijai*

- **Pusa end frame needs minimum 4 frames**
  - Always in groups of 4, can't do end frame as one frame
  - *From: Kijai*

- **Pusa works by expanding timesteps**
  - Each latent has its own timestep, frames we want to keep have timestep set to 0
  - *From: Kijai*

- **Radial sage attention is slower than expected**
  - First test showed it's slower
  - *From: Kijai*

- **Multitalk works better with isolated vocals**
  - Does almost perfect lipsync with talking but gets distracted by instruments in music tracks. Extract just vocal for better results
  - *From: Charlie*

- **Radial sparse attention provides ~25% speed improvement over standard SageAttention**
  - Sampling 81 frames at 1280x768 with 6 steps: standard sage took 2:04, radial sparse took 1:39
  - *From: Kijai*

- **Pusa LoRA can do extension without context windows on its own**
  - Just like VACE, Pusa has built-in extension capabilities
  - *From: Kijai*

- **GGUF models now work in WanVideoWrapper**
  - Allows low VRAM users to run larger models with model/clip stacks
  - *From: The Shadow (NYC)*

- **VACE supports direct bbox coordinate injection and color-coded object control**
  - User manual shows JSON injection with RAM tag color index for specific object control
  - *From: ingi // SYSTMS*

- **Q8_0 GGUF has better quality than fp8**
  - Q8 output is more vibrant, cleaner, and has less of the 'stippling' artifacts compared to fp8
  - *From: David Snow*

- **Reference image brightness affects generation speed**
  - 50% grey reference works fast at 8it/sec, while 75% grey slows down to 450it/sec. Darker images are more flexible, lighter images appear more stiff and static
  - *From: AmirKerr*

- **RTX 6000 Pro is 6x faster than RTX 3090 Ti**
  - Quality improvement is minimal but speed difference is significant
  - *From: Valle*

- **Radial attention shows real speed benefits at higher resolutions**
  - At 1024x1024 resolution, radial attention provides significant speed improvements
  - *From: Kijai*

- **I2V specific LoRA provides much better quality**
  - Quality is much better when using I2V specific LoRA instead of T2V LoRA for I2V generation
  - *From: yi*

- **Higher rank LightX LoRAs show obvious improvement**
  - Higher rank provides better quality and clarity, though lower rank has cinematic personality with some weirdness
  - *From: Atlas*

- **Radial/sparse attention provides 50% speed boost on 5090**
  - Higher resolution benefits more, can use 1-2 dense steps with rest sparse for distil LoRAs. Benefits scale with resolution - smaller resolutions don't see as much improvement
  - *From: Kijai*

- **LightX2V rank 128 shows faster and more fluid motion than rank 64**
  - Rank 64 appears more like slow motion compared to rank 128
  - *From: David Snow*

- **Model merging enables running on lower VRAM systems**
  - Successfully merged base WAN models with LoRA stacks to avoid OOM on A4500 w/ 20GB VRAM that was failing with LoRAs applied separately
  - *From: The Shadow (NYC)*

- **Dense timesteps setting affects radial attention quality**
  - Start with 1 dense timestep, increase if quality unsatisfactory. For 4-step lightxv2, default 10 is too high
  - *From: Kijai*

- **Multitalk works on 3060 12GB with proper settings**
  - 832x480 x 81 frames in 8-13 minutes on 3060, key was turning off 'use-non-blocking' setting
  - *From: mdkb*

- **Radial attention provides 25-50% speed improvement**
  - Speed increase especially at higher resolutions with slight quality hit
  - *From: Kijai*

- **Sparse steps in radial attention are significantly faster**
  - Need to balance sparse vs dense steps for quality/speed tradeoff
  - *From: Kijai*

- **MultiTalk can change prompting based on audio content**
  - Had 'man at the beach' in prompt but got fire in video because audio contained the word 'fire'
  - *From: hicho*

- **PUSA unlocks improved reference accuracy**
  - Works well with VACE for better image reference likeness
  - *From: DawnII*

- **Phantom needs higher CFG to work properly**
  - CFG 1 with phantom produces poor results, needs at least 8 steps and higher CFG
  - *From: Piblarg*

- **GGUF Q3 vs FP8 memory difference is minimal with full block swapping**
  - Q3 is 200MB per block vs FP8 at 425MB per block, but when swapping all 40 blocks the VRAM difference is negligible
  - *From: Kijai*

- **N0NSens discovered a trick with LightX2V to use low steps to pick a seed**
  - Can use low steps to select specific seed values when using LightX2V LoRA
  - *From: N0NSens*

- **Radial Sage Attention provides speed gains that scale with resolution**
  - Higher resolution provides more speed gain with the radial sage attention node
  - *From: Kijai*

- **Phantom and VACE references are stored in temporal dimension while I2V uses channels**
  - Phantom and vace references are just in temporal dim, while I2V model has the image in channels
  - *From: Kijai*

- **Running higher CFG then dropping to 1.0 helps Phantom**
  - It does work to run some steps with higher cfg and drop off back to 1.0 with the distilled lora. Just using 1.0 all the way through hurts phantom a lot
  - *From: Ablejones*

- **PUSA Lora significantly improves style retention in I2V workflows**
  - Multiple users confirmed PUSA Lora at various strengths (0.75-1.5) dramatically improves input image style consistency compared to just using LightX
  - *From: A.I.Warper*

- **LightX2V performs better at 0.8 strength instead of 1.0**
  - Kijai noted that in many cases lightx2v at slightly lower strength like 0.8 is better than full strength
  - *From: Kijai*

- **PUSA + LightX combination works well at 65% LightX strength with 100% PUSA**
  - Gets sharpening effect but maintains decent colors, though some progressive shape drift occurs across batches
  - *From: A.I.Warper*

- **Phantom is T2V model that provides excellent I2V-like results through encoded latents**
  - Phantom gets reference image information from encoded latents rather than being true I2V architecture, but produces best I2V results for references
  - *From: DawnII*

- **PUSA works better with official default strength 1.4 vs 1.0**
  - With strength 1.0 it jumps away from subject too much
  - *From: Kijai*

- **PUSA adherence can be improved at low steps with specific settings**
  - 3 steps with light i2v 0.85, CausVid 1.5 at 0.5, and Pusa at 1.4
  - *From: phazei*

- **Skyreels can handle 121 frames without context_option**
  - Unlike vanilla which has 81 frame limit
  - *From: N0NSens*

- **Wan t2i can generate 8k images in 27 seconds**
  - Using text to image workflow with upscaler
  - *From: Charlie*

- **FP16/32 models show surprisingly big quality difference**
  - Worth considering for upscaling workflows
  - *From: Kijai*

- **UniPC/beta sampler gives less 'burned' looking images**
  - Alternative sampler recommendation for better quality
  - *From: N0NSens*

- **Fun Control has better control adherence than VACE**
  - Fun control sticks to the control way better than VACE and the first frame ref doesn't have to match 100% so there may be potential to do this with fun instead of base wan
  - *From: Hashu*

- **Fun Control is more flexible with first frame matching**
  - Fun is meant to be more like a start frame but can be flexible so it doesn't have to be exact which is nice cause you don't get the first frame pop you would with VACE start frame if it doesn't match 100%
  - *From: Hashu*

- **PUSA scheduler expands timesteps for individual frame control**
  - When the scheduler is set, it expands the timesteps like how PUSA was trained, meaning every frame gets its own noise level, and we can control what frame is used as reference and what is denoised
  - *From: Kijai*

- **Unmerged LoRA system allows instant weight changes**
  - New unmerged LoRA system allows changing lora weights/strength without any loading times, reduces LoRA merging RAM use, and supports both fp8 scaled models and normal models with unmerged loras
  - *From: Kijai*

- **Original Phantom model uses 3 CFG passes**
  - The original phantom does 3 passes with its own cfg using formula: noise_pred = noise_pred_uncond + phantom_cfg_scale[idx] * (noise_pred_phantom - noise_pred_uncond) + cfg_scale * (noise_pred_cond - noise_pred_phantom)
  - *From: Kijai*

- **Context options work better for long video generation**
  - Context options for long duration wins over other continuation methods. Using 81,4,16 context option fits on 48GB with VACE, Multitalking and T2V 14B
  - *From: samhodge*

- **VACE with context requires smaller window**
  - With VACE needed the context window down to 33 frames down from 121 with a 16 frame overlap
  - *From: samhodge*

- **Uni3C can capture both camera and character motion**
  - Uni3C takes on character motion too, not just camera movement. Can use catwalk motion and other body motions
  - *From: VRGameDevGirl84(RTX 5090)*

- **VACE pose control works better when start frame is not 100% match to control**
  - Fun control shines when you have a start frame that is not 100% a match to your control and it estimates that character/style and follows the control
  - *From: Hashu*

- **White masks needed for VACE pose control**
  - All control masks that overlap with pose control frames need to be white - inpaint masks need to be white to tell VACE to ignore actual image information and only use control signal
  - *From: Ablejones*

- **VACE works better with separate control embeddings**
  - VACE seems to do better if you send in the control frames as separate embeddings, rather than pre-combining them
  - *From: Ablejones*

- **Phantom+VACE merge can fix likeness issues**
  - If using vace+phantom merge model, adding a vace reference of a likeness that is not working can sometimes kick it into working
  - *From: Ablejones*

- **Good descriptions help Phantom significantly**
  - Sometimes you'll have a description where phantom seems to do nothing... then you add a few details to the prompt and suddenly it's like an exact likeness
  - *From: Ablejones*

- **FP8 scaled model closer to FP16 quality**
  - New fp8_scaled_kj model is closer to fp16 than any other fp8 model, better than comfy fp8_scaled which is blurry
  - *From: Kijai*

- **Wan VACE can generate complex actions from simple prompts**
  - Can successfully generate 'grabs mushroom from behind his back and eats it' following hand movements and making mushroom disappear at correct timing
  - *From: enigmatic_e*

- **PUSA LoRA provides better prompt adherence than VACE**
  - User spent whole day struggling with VACE and Wan I2V, but PUSA LoRA one-shot the exact desired output from prompt
  - *From: 3Dmindscaper2000*

- **Wan works exceptionally well as T2I model**
  - Better than any other T2I model currently available when using enough image training data
  - *From: mamad8*

- **Second pass technique effectively reduces noise**
  - Using 0.15 denoise strength in second pass at same resolution removes stipple effect without upscaling penalty
  - *From: mamad8*

- **Scaled quantization models require reduced LoRA strengths**
  - e5m2_scaled and e4m3fn_scaled quantized models need 10-20% reduction in LoRA strength compared to unscaled versions
  - *From: Kijai*

- **I2V + UniC3 equals basic Wan VACE control functionality**
  - Using I2V models combined with UniC3 provides similar capabilities to Wan VACE control system
  - *From: hicho*

- **Text encoder caching added to default wrapper**
  - Disk cache added for text encoder node - caches prompts as 8MB bf16 files, avoids re-encoding unchanged prompts after restarts
  - *From: Kijai*

- **Sparse SageAttention 2.0 available**
  - Radial attention dev released sparse sagettn2, requires compilation but will be used by default if installed
  - *From: Kijai*

- **PerpNegGuider may work better with Phantom**
  - Alternative to regular sampler for Phantom model, uses negative text embeds differently
  - *From: Ablejones*

- **UniC3 trained on point clouds from depth estimations**
  - According to paper, mostly used point clouds based on depth estimations rather than full 3D scenes
  - *From: Ablejones*

- **Context windows with MAGREF work better for longer videos**
  - Using MAGREF with context windows reduces snapping back to init image compared to regular I2V models
  - *From: Kijai*

- **Padding strategy improves context windows performance**
  - Using padded reference images for windows beyond first frame works better than full init image
  - *From: Kijai*

- **Skip every 2 frames technique for longer videos**
  - Generate at twice speed by skipping frames, then slow down in post to get 10s from 5s generation
  - *From: Drommer-Kille*

- **White padding enables MAGREF reference mode**
  - MAGREF treats images with white padding as reference rather than first frame
  - *From: Hashu*

- **Point clouds work better than solid geometry for Uni3C**
  - Sparse point clouds or noise textures on solids provide better features for camera tracking
  - *From: samhodge*

- **Rope function setting affects LoRA strength**
  - Setting rope_function from 'comfy_chunked' back to 'comfy' fixed LoRA strength issues where strength of 2 was needed instead of 1
  - *From: Hashu*

- **fp8_scaled models make LoRAs stronger**
  - Kijai's fp8_scaled_kj models typically make LoRAs stronger, often requiring reduced strength settings
  - *From: Kijai*

- **Context sliding works with MultiTalk**
  - You can use context sliding with MultiTalk for better results
  - *From: Draken*

- **Frame count mismatches cause crashes**
  - When frame counts don't match between uni3c and other inputs, it can crash ComfyUI entirely
  - *From: Kijai*

- **T5 encoder can be disabled**
  - New cache update allows disabling whole T5 loading if prompts are already encoded, and T5 input is now optional
  - *From: Kijai*

- **Disk cache improves development workflow**
  - New disk cache feature is very useful for testing when reloading frequently
  - *From: Kijai*

- **Wan has excellent text generation capabilities**
  - Text rendering in video works well with detailed prompts, especially with 81 frames
  - *From: VK (5080 128gb)*

- **Wan prompts are case sensitive**
  - T5 encoder makes prompts case sensitive
  - *From: garbus*

- **Text in prompts needs detailed descriptions**
  - Being detailed and specific about text appearance is crucial for good text generation
  - *From: hicho*

- **Shattering text effects happen at video end**
  - Text shattering animations always start at the end of videos, can't be forced to start earlier
  - *From: VK (5080 128gb)*

- **Context overlap doesn't fix text timing**
  - Using context overlap doesn't change when text shattering begins in video
  - *From: VK (5080 128gb)*

- **UniC3 works like simple VACE**
  - UniC3 can follow 3D models and control both camera and character movements
  - *From: VRGameDevGirl84(RTX 5090)*

- **Merging LoRAs to scaled model is simple**
  - Just apply the scale to the model weight first when merging
  - *From: Kijai*

- **PUSA workflow delivers better results when used correctly with T2V models**
  - Using PUSA with T2V models, flowmatch_pusa scheduler, and proper frame injection gives much better results than misusing it with I2V
  - *From: Juan Gea*

- **FastWan 1.3B model converted to ComfyUI format works well for anime/cartoon generation**
  - Clean results at 720x720, good performance at 1920x1152x81 frames in 286 seconds on RTX 4090, but not photorealistic
  - *From: Juan Gea*

- **SageAttention 2 provides better performance and quality but requires more VRAM**
  - Better performance and quality than SageAttention 1 but uses more memory, potentially limiting frame count
  - *From: Juan Gea*

- **WAN supports non-rectangular shapes for generation**
  - Can use various shapes, not just rectangles and three-dimensional objects
  - *From: Дмитрий Марков*

- **Being very specific and clear in prompts dramatically improves WAN results**
  - Cutting out LLMs and being precise about what you want to see was a game changer for prompt adherence
  - *From: Yayu*

- **Injecting noise level affects PUSA extension quality**
  - 0.7 noise injection was too much, 0.1 noise injection gave way better results for video extension
  - *From: Juan Gea*

- **Fast Wan 1.3B model available and working**
  - Kijai added fast Wan 1.3B model which can be used directly in workflows as replacement for Wan 2.1
  - *From: patientx*

- **VACE blocks can be added to T2V models using native ComfyUI merge nodes**
  - Can use simple model merge node with strength 0.0 to add VACE blocks to any T2V model, existing keys don't need to match
  - *From: Ablejones*

- **Pusa extension can start from any number of frames**
  - Pusa can do T2V with 2 extensions and start from any frame count, basically implements DiffusionForcing workflow
  - *From: Kijai*

- **Wan 2.2 announcement video specs**
  - Official Wan 2.2 teaser video is 1280x720x30fps according to person in Wan discord
  - *From: Juan Gea*

- **Wan 2.2 still 16fps native**
  - Person with early access confirms Wan 2.2 is still 16fps, not 24fps native
  - *From: JohnDopamine*

- **WAN 2.2 will be free**
  - Confirmation that the upcoming WAN 2.2 model will be available at no cost
  - *From: hicho*

- **NABLA optimization provides 50% inference time reduction**
  - Hugging Face release shows 50% faster inference time with NABLA optimization using flex attention and radial attention
  - *From: DawnII*

- **WAN 2.1 LoRAs compatible with 2.2**
  - Same architecture allows 2.1 LoRAs to work with 2.2, though fine-tuning will give better results
  - *From: ZeusZeus*

- **WAN text-to-image good at inpainting with mask latent**
  - WAN performs well for inpainting tasks when using mask latent approach
  - *From: hicho*

- **Sage Attention 3 released with fp4 support**
  - New version supports fp4 quantization with claims of maintaining accuracy while improving speed
  - *From: aikitoria*

- **MultiTalk can generate up to 10 seconds without context degradation**
  - MultiTalk continuation mode works well for up to 10 seconds, though it degrades quickly beyond that point
  - *From: Kijai*

- **SageAttention 3 setting per_block_mean=False makes it use same VRAM as sage2**
  - Setting per_block_mean=False in SageAttention 3 reduces VRAM usage to match SageAttention 2 levels
  - *From: Kijai*

- **LoKR training extremely efficient for Flux**
  - For training flux likeness, can only train single block 9 and get decent result. LoKR file is just 1.2mb
  - *From: jikan*

- **VACE T2V weights identical to original T2V**
  - The T2V weights that came with VACE are identical to the original model weights
  - *From: Kijai*

- **Radial attention performs better than SageAttention 3**
  - At this point I'd say radial attn > sage3. Same speed benefits as sage3 but sage3 quality feels even lower
  - *From: Kijai*

- **FastWan has 4 steps CFG 1.0 capability**
  - Can generate solid output at 4 steps with CFG 1.0 using DPM++ SDE sampler
  - *From: Kijai*

- **FastWan model has duplicate weights**
  - FastWan model is 60GB because it has duplicate weights, not because it's in fp32
  - *From: Kijai*

- **FastWan + LightX2V combination works for 2 steps**
  - Neither FastWan nor LightX2V can do 2 steps alone without fuzziness, but together they produce solid 2-step results
  - *From: phazei*

- **Wan 2.2 has 30fps output**
  - Wan 2.2 outputs at 30fps for 5 seconds, which is 150 frames (or 156/155 according to tester)
  - *From: 青龍聖者@bdsqlsz*

- **Wan 2.2 is more anime-friendly**
  - 2.2 is more inclined towards 2D illustration style, less 3D, with better anime character rendering
  - *From: 青龍聖者@bdsqlsz*

- **FastWan uses specific timesteps with noise addition**
  - FastWan uses 3 timesteps: 1000,757,522 specifically with euler and adds noise at each step
  - *From: Kijai*

- **VRAM usage improvements in VideoWrapper**
  - VRAM no longer explodes on long generations, possibly due to radial attention or chunked rope
  - *From: MysteryShack*

- **EchoShot supports multiple prompt transitions for character consistency across scenes**
  - Model can handle up to 7 prompts with [1], [2], [3] formatting for scene transitions while maintaining character consistency
  - *From: Kijai*

- **EchoShot works as both full model and LoRA**
  - Can be used as 1.3B full model or as LoRA on base Wan model, with most magic coming from multiple prompt handling in code
  - *From: Kijai*

- **Multiple prompt technique works even without EchoShot weights**
  - Cross-attention splitting and prompt handling provides some transition effects even without the trained weights
  - *From: Kijai*

- **WAN T5 can parse JSON-structured prompts**
  - Model understands and can work with JSON formatting for prompts, similar to VEO style
  - *From: AmirKerr*

- **EchoShot generates up to 257 frames in single pass**
  - Can generate long sequences without context overlap, straight up 200+ frames
  - *From: Kijai*

- **Prompt order affects transitions in EchoShot**
  - Different ordering of prompts ([1][3][2] vs [1][2][3]) produces different transition sequences
  - *From: TK_999*

- **EchoShot LoRA enables first-frame-last-frame morphing for T2V**
  - Can create transitions between scenes using prompts, though weaker than full model
  - *From: Kijai*

- **Wan 2.1 14B has better prompt adherence and scene changing capabilities**
  - Can change car to SUV using distill 14b model with proper prompt formatting
  - *From: hicho*

- **DG models work well with EchoShot LoRA**
  - Produces crisp quality like 14B level when combined properly
  - *From: hicho*

- **Prompt enhancer system prompt from Wan repo works well with Qwen3 8B**
  - Located in their GitHub repo for better prompt generation
  - *From: Kagi*

- **LightX2V LoRA at 0.25 strength reduces over-smoothing**
  - Maintains CFG 1 and low steps like 4-6 without artifacts
  - *From: Drommer-Kille*

- **VAEs don't handle alpha channels**
  - Alpha channels get converted to colors (like gray) and cause errors. The mask input should be used instead of alpha channels.
  - *From: Kijai*

- **Wan VAE packs 4 images per latent**
  - 1 latent = 4 frames in Wan VAE. First frame is handled differently by the temporal VAE due to cross information.
  - *From: Kijai*

- **Wan 2.2 models found in code**
  - Found Wan2.2-TI2V-5B model in DiffSynth Studio code with new VAE (z_dim 16, upsampling factor 16 vs current 8)
  - *From: Kijai*

- **MoE architecture uses dual models**
  - A14B appears to use two separate models run at different timesteps - high and low noise experts
  - *From: Kijai*

- **I2V doesn't use clip embed in new code**
  - The I2V model in the new code doesn't define clip embed usage
  - *From: Kijai*

- **ROPE chunking reduces VRAM peaks significantly**
  - The rope chunked version shows lower peak VRAM usage compared to uncompiled model
  - *From: Kijai*

- **Torch compile reduces VRAM peaks**
  - Torch compile similarly reduces the peaks in VRAM usage during inference
  - *From: Kijai*

- **With full offloading, GGUF is mostly pointless**
  - You end up saving only couple hundred megabytes with GGUF when using full offloading
  - *From: Kijai*

- **First compilation takes very long time**
  - The first time it compiles takes a LONG time and stays at 0% the whole time, compiles in the Interpolate node. After first time won't do it again
  - *From: phazei*

- **Wan 2.2 uses dual model structure**
  - High noise and low noise models - run one for first timesteps to timestep 875, then rest with other model
  - *From: Kijai*

- **5B model uses expanded timesteps**
  - The 5B also uses expanded timesteps similar to DF and Pusa
  - *From: Kijai*

- **New model outputs 48 channels**
  - The model is set to output 48 channels, the VAE works with those
  - *From: Kijai*

- **FP4 quantization works well for Flux but not Wan**
  - FP4 works great for Flux, but haven't seen anyone do FP4 successfully for Wan. GGUF Q4 is terrible quality
  - *From: Kijai*

- **T5 text encoder runs surprisingly fast on CPU**
  - AMD Ryzen 9 9900X 12-Core processes T5 encoding at competitive speeds, though GPU is still 65x faster (9.81it/s vs 643.79it/s)
  - *From: Kijai*

- **Native clip load on CPU is faster than T5 with offloading**
  - Native clip load takes 130s vs much longer with T5 offloading due to VRAM limitations
  - *From: hicho*

- **113 frames is optimal for v2v work without morphing**
  - At 912x512 resolution, 113 frames (7 seconds) completes in 93s and avoids morphing artifacts
  - *From: Drommer-Kille*

- **Wan 2.2 VAE is significantly larger**
  - 2.2 VAE is 1.3GB in bf16 format, much larger than previous versions
  - *From: Kijai*

- **Wan 2.2 supports High Dynamic Range (HDR)**
  - HDR capability hinted at during presentation, light values go from 0 to 1000000 instead of 0 to 1.0
  - *From: samhodge*

- **DiffSynth enables tiling by default for 2.2**
  - Tiling is enabled by default for the new 2.2 model in DiffSynth implementation
  - *From: Kijai*

- **Multiple Wan 2.2 model sizes available**
  - Three variants confirmed: 1.4B, 5B, and 14B models
  - *From: 青龍聖者@bdsqlsz*

- **Wan 2.2 uses MoE architecture with separate experts**
  - MoE (Mixture of Experts) architecture with high-noise and low-noise expert split, separate LoRA adapters needed for each expert with different timestep schedules
  - *From: seruva19*

- **Audio-to-video capability mentioned**
  - One slide shows audio to video functionality, called A14B model, but no examples shown yet
  - *From: Juampab12*

- **Wan 2.2 includes detailer model**
  - Two models mentioned: one first pass and one detailer
  - *From: Juampab12*

- **Wan 2.2 uses separate high noise and low noise models that work together**
  - High noise expert handles early stages focusing on overall layout, low noise expert handles later stages for fine details. Both must be used together.
  - *From: comfy*

- **Wan 2.2 5B model supports both text-to-video and image-to-video in same model**
  - TI2V (Text or Image to video) capability built into single 5B model
  - *From: JohnDopamine*

- **Wan 2.2 VAE has 64x compression compared to 2.1**
  - Much higher compression ratio than previous version
  - *From: mamad8*

- **5B model is faster than old 1.3B model despite being larger**
  - Performance improvement due to better VAE compression
  - *From: comfy*

- **LightX2V LoRA works with Wan 2.2**
  - Confirmed working with 4 steps, cfg 1, though there may be some flashing that could be a settings issue
  - *From: ArtOfficial*

- **Wan 2.2 uses two-stage architecture with high and low noise experts**
  - High noise stage first, then low noise stage. Models load one at a time according to Kijai
  - *From: multiple users*

- **5B model runs much faster than 14B**
  - About on par with 14B lightx performance
  - *From: Draken*

- **Wan 2.1 LoRAs don't work with Wan 2.2**
  - Different model architectures make them incompatible
  - *From: multiple users*

- **Wan 2.2.1 is 4K capable and runs on 4GB VRAM**
  - 2.2.1 supports 4K resolution generation while only requiring 4GB of VRAM
  - *From: Purz*

- **Wan 2.2 has two different model architectures released simultaneously**
  - 14B model uses dual high/low noise architecture compatible with previous 14B LoRAs, 5B model has new VAE with much better compression and speed, both trained on 75% larger dataset
  - *From: Juampab12*

- **5B model runs at 24fps vs 14B at 16fps**
  - The 5B model operates at higher framerate than the 14B variant
  - *From: Juampab12*

- **GGUF quantization is very easy and fast to make**
  - Community can quickly create GGUF versions of new models
  - *From: gokuvonlange*

- **LoRAs from 2.1 work on 2.2 but need higher strength settings**
  - LightX2V LoRA requires strength 2-3 instead of 1.0, FastWAN also works with 2.2
  - *From: patientx*

- **Wan 2.2 has improved prompt adherence compared to 2.1**
  - Users reporting better prompt following capabilities
  - *From: ingi // SYSTMS*

- **VACE works with low-noise model but not high-noise model**
  - Low-noise model responds to VACE blocks, high-noise model completely ignores them
  - *From: Ablejones*

- **2.2 supports both 16fps and 24fps output**
  - 5B model is 24fps, 14B appears to be 24fps despite documentation saying 16fps
  - *From: multiple users*

- **NAG (Negative Guidance) works with Wan 2.2**
  - Testing shows NAG produces clear results
  - *From: GalaxyTimeMachine (RTX4090)*

- **FastWAN LoRA works better with 2.2 than 2.1**
  - Users report improved quality when using FastWAN with 2.2
  - *From: Elvaxorn*

- **Adaptive rank LoRA performs significantly better on 2.2**
  - Comparison shows more detail with adaptive vs regular LightX2V
  - *From: ZeusZeus (RTX 4090)*

- **WAN 2.2 14B uses dual model architecture with high-noise and low-noise expert split**
  - There are now two separate models - one for low noise and one for high noise processing
  - *From: aikitoria*

- **WAN 2.2 14B should use 81 frames at 16 fps, not 121 frames**
  - Official code generates 14B at 81f 16fps and 5B at 121f 24fps. 121 frames causes looping issues
  - *From: aikitoria*

- **Looping issues occur specifically with 121 frame generations**
  - 121f causes looping and low prompt adherence, while 81f works properly
  - *From: Juampab12*

- **LightX2V LoRA breaks 121f generations but works on 81f**
  - LightX2V was trained on 81 frames, so it breaks when used with 121 frame generations
  - *From: Juampab12*

- **WAN 2.2 has improved prompt adherence at proper settings**
  - On 81f with proper settings, prompt adherence reaches 'Veo 3 levels'
  - *From: Juampab12*

- **Wan 2.2 may natively support 24fps output despite being documented as 16fps**
  - Users consistently getting 24fps results, though official documentation only mentions 16fps for 14B model
  - *From: Ablejones*

- **High noise and low noise models serve different purposes**
  - High noise model determines light perception and texture, can't handle low noise steps at all. Low noise model is very similar to Wan 2.1 with more training and can do entire generation by itself
  - *From: slmonker*

- **Mixing Wan 2.1 as low noise sampler with 2.2 high noise works well**
  - User successfully combined base 2.1 model with lightx2v rank 128 lora as low noise sampler, with 2.2 as high noise sampler for 10 steps total
  - *From: slmonker*

- **LightX2V lora causes looping issues at high frame counts**
  - LightX lora falls apart when going above 81 frames, with prompt adherence becoming completely different
  - *From: gokuvonlange*

- **FastWAN lora eliminates problems at longer frame counts**
  - Adding FastWAN at 0.8 strength eliminates problems when using longer frame counts with LightX
  - *From: DawnII*

- **2.2 high noise model provides much better movement and motions than 2.1**
  - The high noise model is specifically responsible for improved camera motion and motion resolution
  - *From: mamad8*

- **VACE control completely doesn't work with high noise model**
  - VACE control system is incompatible with the high noise 2.2 model but works with low noise
  - *From: Ablejones*

- **Motion is always resolved at start of generation**
  - All fancy camera motion comes from the high noise model since motion is resolved in early steps
  - *From: Kijai*

- **VACE has some weak effect on HIGH model**
  - Despite earlier reports of incompatibility, there appears to be some minimal VACE effect on high noise model
  - *From: Kijai*

- **2.2 models appear to be trained for 24fps at 121 frames**
  - Evidence suggests 121 frame training data was at 24fps, making 5*24=120 frames the target
  - *From: multiple users*

- **High and low noise models are close but not identical**
  - Models are similar, possibly finetuned for specific timesteps rather than fully retrained
  - *From: Kijai*

- **High-noise model is responsible for prompt-following and camera motion**
  - Definitive evidence that high-noise model contributes to prompt-following camera motion. Same workflow with only low-noise model shows less motion.
  - *From: Ablejones*

- **High-noise model may be responsible for 24fps-ness of generations**
  - Based on observations that high-noise model seems to have more 121 frame 24fps training
  - *From: Ablejones*

- **Wan 2.2 passes slicing test**
  - Successfully generates tomato slicing with proper physics including light refraction through the tomato showing the knife
  - *From: thaakeno*

- **Higher shift values help a lot with quality**
  - Testing showed shift value of 8 was too high, but higher values than default 2 improved results
  - *From: VRGameDevGirl84(RTX 5090)*

- **5B model quality and movement scale with resolution better than ever**
  - Fails to work on familiar low resolutions completely, but scales impressively at higher resolutions from 512p to 1280p
  - *From: Blink*

- **LightX2V may need double strength to work better with high-noise model**
  - Similar to how other settings need adjustment, VACE may need to be bumped to have bigger effect on high-noise model
  - *From: Hashu*

- **2.2 dropped CLIP embeds**
  - Unlike previous versions, Wan 2.2 doesn't use CLIP embeddings
  - *From: Kijai*

- **Text prompts significantly affect 2.2 output quality**
  - Empty positive prompts show model favors sports and cooking content, proper prompts needed for control
  - *From: OxygenConsumer*

- **Wan 2.2 supports higher resolutions**
  - Works at 1536x1536 and 1920x1088, unlike 2.1 which glitched beyond 1280px
  - *From: GOD_IS_A_LIE*

- **Frame rate appears to be 24fps or 30fps**
  - Definitely not 16fps based on output analysis
  - *From: GOD_IS_A_LIE*

- **5B i2v only works with flowmatch_pusa sampler**
  - Currently the only compatible sampler for 5B image-to-video in wrapper
  - *From: Kijai*

- **CFG affects high-noise vs low-noise sampling differently**
  - Higher CFG on high-noise steps can make results worse, lower CFG (1-3.5) works better
  - *From: VRGameDevGirl84*

- **Shift values must match between high and low noise samplers**
  - Different shift values between samplers causes poor results
  - *From: DawnII*

- **Prompting the high noise model is something else - dramatically different from previous models**
  - High noise model requires different prompting approach compared to standard models
  - *From: Kijai*

- **Wan 2.2 has dramatically improved prompt adherence even for longer lengths like +121 frames**
  - Setup works for T2V with much better prompt following than previous versions
  - *From: gokuvonlange*

- **First stage very important for prompt adherence and motion**
  - The high noise stage is crucial for getting proper prompt following and motion generation
  - *From: MysteryShack*

- **5B model uses different VAE that compresses more images into a single latent**
  - The larger 2.2 VAE is specifically for the 5B model only
  - *From: Piblarg*

- **41 frames produces significantly better I2V outputs**
  - A.I.Warper reports massively noticeable improvement when using only 41 frames for I2V
  - *From: A.I.Warper*

- **Radial attention provides speed improvements and makes timecost more linear**
  - Radial attention makes timecost more linear instead of exponential for longer video generations, provides significant speed boost
  - *From: MysteryShack*

- **Higher LightX2V strength reduces blur**
  - Cranking LightX2V lora strength to 2.5 instead of 1.0 significantly improves blur issues
  - *From: A.I.Warper*

- **Different LightX2V strengths on high vs low noise models affects prompt adherence**
  - Lower LightX2V strength on high model and higher on low model improves prompt adherence - actually got pi symbol to render correctly
  - *From: MysteryShack*

- **Wan 2.2 has excellent camera movement understanding**
  - Model shows pretty good understanding of camera moves/camera direction, can generate different camera movements with slight prompt modifications using same seed
  - *From: Hashu*

- **Scene cuts possible with prompt formatting**
  - Adding 'cut' at the beginning of each scene prompt makes it easier to switch between scenes, similar to Seedamce. Doesn't always work but enables scene transitions in single generation
  - *From: 852話 (hakoniwa)*

- **Wan 2.2 models can be used sequentially without keeping both high/low noise models in VRAM simultaneously**
  - Each pass uses 7GB VRAM on 8GB GPU using Q4 GGUF
  - *From: Blitz*

- **High noise and low noise models can be mixed - 2.2 high noise with 2.1 low noise works**
  - Can swap 2.1 for the low noise model while keeping 2.2 as high noise, potentially better with old loras
  - *From: Kijai*

- **JmySff successfully merged Wan 2.2 fp16 models with VACE and quantized to GGUF Q8**
  - Depth and OpenPose controls are working in the merged model
  - *From: JmySff*

- **Different LoRA strengths needed for high vs low noise models**
  - 3.0 strength on HIGH noise, 1.0 on LOW noise for i2v lightx2v LoRA
  - *From: Kijai*

- **Q3 quantization works surprisingly well with Wan 2.2**
  - User reports amazing quality with Q3 on 12GB VRAM, better than expected compared to 2.1
  - *From: SonidosEnArmonía*

- **Wan 2.2 High noise model works with 2.1 LoRAs but needs different strengths**
  - High noise model is partially compatible with 2.1 LoRAs, memory can be exactly the same if using refiner approach
  - *From: CDS*

- **Wan 2.2 has significantly better prompt adherence than 2.1**
  - Model recognizes character names, anime characters, and follows complex prompts much better
  - *From: Doctor Shotgun*

- **ComfyUI update enables minimap feature**
  - New frontend update includes minimap that allows clicking to jump to sections
  - *From: Kijai*

- **TAEW previews show motion clearly in just 2 steps**
  - With TAEW previews you can see all motion development very early in generation
  - *From: Kijai*

- **Wan 2.2 removes clip vision from model architecture**
  - 2.2 models dropped clip image embed layers, which is why we don't use clip vision with 2.2
  - *From: Kijai*

- **Merged high and low noise models produces only noise**
  - Attempting to merge the high and low noise models results in unusable output
  - *From: Kijai*

- **I2V loops at 121 frames**
  - The I2V model appears to naturally loop when generating 121 frames
  - *From: Kijai*

- **High noise model follows prompts better and creates much more motion**
  - The high noise model is what's new and provides better prompt adherence and motion generation
  - *From: Kijai*

- **Low noise model is not very different from 2.1**
  - The low noise model maintains similar characteristics to the previous 2.1 version
  - *From: Kijai*

- **5B model needs high resolution to work properly**
  - The 5B model functions best at 720p resolution or higher
  - *From: Kijai*

- **CFG steps with motion kickstarting**
  - Using different CFG values per step (2.0 for first step, 1.0 for rest) can kickstart more motion and prompt adherence
  - *From: Kijai*

- **Wan 2.2 control/VACE works with low noise model only**
  - Control inputs are ignored by high noise model but work with the low noise model
  - *From: Kijai*

- **High noise model has great motion and prompt adherence but can't resolve final quality**
  - High noise model excels at motion generation and following prompts but requires low noise pass for quality
  - *From: Kijai*

- **Low noise model alone isn't much different from Wan 2.1**
  - Using only the low noise model without high noise doesn't provide significant improvements over 2.1
  - *From: Kijai*

- **First pass latents can be stored for later refinement**
  - Second sampler mainly handles low-level noise, allowing first pass results to be cached
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Native implementation has automated offloading**
  - Native ComfyUI shows 'loaded partially' messages indicating automatic memory management
  - *From: Kijai*

- **Motion quality decreases with longer frame counts**
  - Motion gets flatter the longer you go, at 160 frames it's basically barely moving
  - *From: Kijai*

- **Only 5B model runs at 24fps, A14B is 16fps**
  - Official sources confirm A14B model runs at 16fps despite some confusion about frame rates
  - *From: Kijai*

- **Different quantization methods affect character details and colors**
  - fp8_e3m2 v2 may look best, e4m3 shows better character details, colors and clothes
  - *From: Kijai*

- **Leftover noise option is essential for high noise sampler**
  - Without leftover noise, the high sampler completely denoises the latent, leaving no noise for the second pass
  - *From: Kijai*

- **Wan 2.2 outputs at 24fps not 16fps as officially published**
  - After generating over 100 videos, observation shows it's definitely 24fps output despite official publications saying 16fps
  - *From: gokuvonlange*

- **VACE inpainting works with Wan 2.2**
  - Successfully demonstrated VACE inpainting functionality working
  - *From: Hashu*

- **Sweet spot resolution is 0.4 Megapixels**
  - Found optimal resolution for generation quality
  - *From: Fictiverse*

- **Higher resolution reduces motion in generations**
  - At 1632x864 resolution, higher red kills motion
  - *From: Valle*

- **Scene switching possible with [cut] prompt control**
  - Can generate four types of scenes in a single video using only prompt control by switching with [cut]
  - *From: 852話 (hakoniwa)*

- **81 frames at 16fps vs 121 frames at 24fps behavior differences**
  - 81/16 and 121/24 frame configurations show different motion characteristics
  - *From: N0NSens*

- **GGUF Q5_K_M works really well for Wan 2.2**
  - Q5_K_M quantized models provide good quality results
  - *From: Samy*

- **DPM++_SDE scheduler works well with LightX2V**
  - This scheduler has been good in experience with LightX2V
  - *From: Kijai*

- **Different seeds for High/Low samplers prevents output loops**
  - Using different start/end seeds prevents generation loops
  - *From: JohnDopamine*

- **Wan 2.2 can work with normal 2.1 T2V workflow**
  - Using 2 ksamplers where second has low denoise of 0.5, works with 4+3 steps distill lora at strength 2 or 3
  - *From: hicho*

- **FusionX removes blockiness on pixel textures**
  - FusionX LoRA helps remove pointy texture artifacts
  - *From: SonidosEnArmonía*

- **5B model excels at fine details like mouse hair**
  - The 5B model can generate very fine details like individual hairs on small subjects
  - *From: TK_999*

- **Wan 2.2 performs well with liminal spaces and found footage styles**
  - The 5B model works particularly well for liminal space and found footage generation
  - *From: Dream Making*

- **LightX2V lora requires specific strength settings for Wan 2.2**
  - 3.0 strength on HIGH noise model and 1.0 strength on LOW noise model to restore prompt adherence and avoid color bleaching
  - *From: gokuvonlange*

- **Context windows with 64 overlap for high noise and 16 for low noise works well**
  - Kijai showed 11 clean seconds of video using this configuration
  - *From: Kijai*

- **Wan 2.2 14B model is limited to 81 frames at 16 fps**
  - Going above 81 frames causes ping-pong or looping effects
  - *From: aikitoria*

- **FP16 at all steps produces insane quality**
  - Running without lightx2v distillation loras gives superior quality results
  - *From: aikitoria*

- **LightX2V currently has compatibility issues with Wan 2.2**
  - The lora was not trained for 2.2 models and causes color shifts and reduced prompt adherence
  - *From: aikitoria*

- **Model extraction experiments between 2.2 variants**
  - 2.2 LOW - 2.1 works but effect unclear, 2.2 HIGH - 2.1 doesn't work (produces noise), 2.2 HIGH applied only to crossattn doesn't fully break generation
  - *From: Kijai*

- **Wan 2.2 14B can generate at 144p resolution successfully**
  - User tested 144p generation and it works without face disfigurement
  - *From: Mngbg*

- **Wan 2.2 5B prefers higher resolution than 14B**
  - 5B model wants higher resolution inputs while 14B works well at lower resolutions
  - *From: Rainsmellsnice*

- **MPS (Metal Performance Shaders) works with i2v**
  - Gives 'lora key not loaded' warning but still functions, needs more testing
  - *From: N0NSens*

- **Wan 2.2 has significantly better prompt adherence than 2.1**
  - Even short succinct prompts are followed quite well in i2v
  - *From: DawnII*

- **LightX2V with Wan 2.2 limited to 81 frames**
  - Can only do 81 frames without weird motion or cuts, same as 2.1
  - *From: NebSH*

- **Old LoRAs partially work with Wan 2.2**
  - Work somewhat with low noise model, pretty weak on high noise model
  - *From: Kijai*

- **Wan can be used for still image generation**
  - Not just for video - can generate still images with shared workflows
  - *From: garbus*

- **Wan 2.2 5B model runs at 24fps while 14B runs at 16fps**
  - The models don't have a real way to control fps, though you could mess with positional embeddings
  - *From: comfy*

- **Character LoRAs from 2.1 work with 2.2**
  - They work just fine, though quality impact is unclear
  - *From: Kenk*

- **2.2 I2V is significantly better than 2.1 I2V**
  - A lot better when comparing equivalent models
  - *From: comfy*

- **Wan 2.2 has excellent prompt adherence**
  - Follows prompts well, can do sequential actions with timeline established by commas
  - *From: Charlie*

- **LightX2V LoRAs work with Wan 2.2**
  - Both rank 64 and 256 work, though 256 files are 3GB and higher ranks may not be noticeably better
  - *From: Ada*

- **High-noise vs Low-noise model architecture explained**
  - High-noise handles complex layouts/structures/motion in early stages, low-noise refines details in later steps. High-noise trained from scratch, low-noise based on 2.1 14B
  - *From: thaakeno*

- **Q4 GGUF uses less VRAM than Q8 GGUF**
  - Q4 quantization allows running on 8GB cards while Q8 may require 24GB VRAM
  - *From: xwsswww*

- **GGUF provides better VRAM efficiency especially for low VRAM users**
  - GGUF quantization allows running larger models on smaller VRAM setups
  - *From: xwsswww*

- **Wan 2.2 5B model can generate 30 second videos on 6GB VRAM using Framepack**
  - Framepack enables extended duration generation with lower VRAM requirements
  - *From: yi*

- **Native offloading with CUDA streams is probably the best method for memory management**
  - Issues around when it activates can be affected by custom nodes and OS VRAM usage
  - *From: Kijai*

- **Wan 2.2 I2V uses slightly less VRAM because image cross attention was removed**
  - 2.2 I2V is more VRAM efficient than previous versions
  - *From: Kijai*

- **LightX2V I2V LoRA works with Wan 2.2 T2V**
  - Setting LightX I2V to strength 2 or 3 on the high model gives good results when used for T2V
  - *From: phazei*

- **FastWan and LightX2V enhance each other when used together**
  - Combined use allows LightX2V to work at lower strength and enables 2 steps with no issues
  - *From: phazei*

- **Context overlap working with MAGREF for 400 frame generations**
  - MAGREF works well with context windows, creating 400 frame videos without crossfade artifacts
  - *From: blake37*

- **VACE works like expected for not being first-last-frame model**
  - No degradation observed, but functions as expected
  - *From: Kijai*

- **T2V model can be used as low noise model in I2V**
  - Quick test bypassing imagetovideo node and feeding prompt conditions directly shows no difference
  - *From: DawnII*

- **Wan i2v node does alter the conditionings and is related to the latent flash at end output**
  - Confirmed through testing with flash in native
  - *From: DawnII*

- **Higher lightx2v lora strength is very similar to higher cfg**
  - You are compensating for the lack of cfg
  - *From: Kijai*

- **Add_noise off means seed has zero impact**
  - If you have add_noise off, like the 2nd sampler in 2.2, it doesn't add noise and thus seed has zero impact
  - *From: Kijai*

- **HighNoise model produces good motion even with very few steps (3) and distill lora**
  - TK_999 found good motion from high noise model at 7 steps res_2s setup, even though preview looked noisy
  - *From: TK_999*

- **HighNoise model without distill lora produces more motion variety across seeds**
  - Running HighNoise model raw with 10 steps produces way bigger distribution of motion variety across seeds compared to using distill lora
  - *From: gokuvonlange*

- **Motion is created in high pass, visuals refined in low pass**
  - Motion-related loras should connect to high, image/upscale loras connect to low
  - *From: Draken*

- **Simple scheduler at shift=1 produces better results than shift=8**
  - User noticed 2.2 looked much better on shift1, while shift 8 felt like 2.1
  - *From: hicho*

- **Sage attention dramatically improves performance**
  - Adding sage attention reduced runtime from 13 minutes to 4 minutes and improved prompt following
  - *From: T2 (RTX6000Pro)*

- **WAN 2.2 has significantly better prompt adherence than 2.1**
  - Especially for camera movements and directions
  - *From: seitanism*

- **High noise model is the 'soul' of 2.2 - handles colors, lights, shadows, cinematic graphics**
  - All visual quality comes from high noise part, low noise just does refinement
  - *From: slmonker(5090D 32GB)*

- **Distill lora on high noise kills 2.2 capabilities**
  - Using distill lora on high noise makes outputs feel like wan 2.1, loses complex prompt understanding and motion
  - *From: gokuvonlange*

- **Higher VACE strength (1.5) improves consistency vs 1.0**
  - At 1.0 strength parts of background suddenly change, at 1.5 everything stays consistent
  - *From: seitanism*

- **2.2 14B works with old VACE**
  - Can use existing VACE with 14B model for video extension
  - *From: seitanism*

- **High noise model response to VACE is mediocre**
  - New training would be needed for VACE compatibility with high noise model specifically
  - *From: Ablejones*

- **High noise model is the core of Wan 2.2 improvements**
  - All new capabilities that 2.2 has over 2.1 come from the high noise model. The low noise model is essentially Wan 2.1 as a refiner
  - *From: Kijai*

- **High noise model excels at complex prompt understanding**
  - The high noise model has crazy good prompt adherence and understands very complex prompts much better than 2.1
  - *From: gokuvonlange*

- **High noise model creates broader motion variety**
  - With wan 2.1 the distribution of possible motion was quite narrow. Now the model stretches further doing surprising motion while still being coherent
  - *From: gokuvonlange*

- **You can use Wan 2.1 as the low noise model**
  - The low model doesn't do anything new really, so 2.1 can be substituted as the low noise model
  - *From: Kijai*

- **LCM sampler for high noise stage eliminates snow/noise artifacts**
  - Using LCM sampler on high noise model with dpmpp_sde on low noise model removes leftover noise and prevents snow particles
  - *From: homem desgraca*

- **Film grain node causes snow particle artifacts**
  - Snow particles in Wan 2.1 generations are caused by the Film grain node, reducing noise makes particles more visible
  - *From: xwsswww*

- **Different samplers between stages can cause snow/particle effects**
  - Using two different samplers for high noise and low noise stages can create snow/particle artifacts
  - *From: MysteryShack*

- **14B model handles any resolution well, 5B struggles below 832x480**
  - 14B performs consistently across resolutions while 5B has quality issues with lower resolutions
  - *From: homem desgraca*

- **Chaining LightX2V LoRA twice at strengths 1 and 3 cuts generation time in half**
  - Accidentally chaining LightX2V twice (1 on first, 3 on second) achieved effective strength of 4 and halved generation time
  - *From: homem desgraca*

- **GGUF e5m2 fp8 model works better than Q4 GGUFs despite larger filesize**
  - 15GB e5m2 fp8 model works better and faster than Q4 GGUFs despite being larger, works with 12GB VRAM
  - *From: mdkb*

- **Wan 2.2 gives anime images anime-style movement**
  - Model properly understands and applies anime-style motion to anime inputs
  - *From: homem desgraca*

- **Wan 2.2 14B has flexibility with resolutions**
  - Model works well across different resolutions unlike some other models
  - *From: homem desgraca*

- **5B model needs full 1280x704 resolution and default negative prompts**
  - 5B model requires proper resolution and Chinese negative prompts to avoid nightmare results
  - *From: garbus*

- **Sequential prompting style from VEO3 can work in WAN 2.2 but doesn't follow prompts closely**
  - Camera movement and character action prompts formatted like VEO3 produce nice output but don't adhere to detailed instructions
  - *From: AJO*

- **WAN 2.2 can generate 240 frames in 110 seconds**
  - Fast generation times achievable with Kijai's wrapper
  - *From: Charlie*

- **WAN 2.2 Vid2Vid quality improves with larger models**
  - 5B model performs better than 1.3B for vid2vid transformations, 14B even better
  - *From: thaakeno*

- **Uni3C works with WAN 2.2**
  - Requires very high strength (3.0) and should be applied only to high noise sampler, turned off or 1.0 for low noise
  - *From: Kijai*

- **First step of high sampler always looks good but quality degrades**
  - High model initial output is often best, then motion becomes unnatural with arm flapping
  - *From: seitanism*

- **Sampler can now return denoised samples for preview**
  - Can preview high model output with tiny VAE before running low noise side
  - *From: Kijai*

- **EchoShot method works with WAN 2.2 without any trained weights**
  - Using prompt splitting with numbered brackets like [1], [2], [3] works on WAN 2.2 high noise model by splitting cross attention to handle multiple prompts
  - *From: Kijai*

- **JSON prompting works with WAN models**
  - Can use structured JSON format for prompts with scenes, camera movements, and detailed descriptions
  - *From: 🦙rishappi*

- **Scene-based prompting with different environments works better**
  - Using [SCENE 1], [SCENE 2] format with different backgrounds/settings produces better scene transitions than same setting
  - *From: Cseti*

- **Context windows can be used with different prompts**
  - Context windows work with prompt variations for extended sequences
  - *From: Kijai*

- **FP8 scaled models work with weight_dtype fp8_fast**
  - Using fp8_fast weight_dtype works well with WAN fp8 models without quality drop
  - *From: 🐝 bumblebee 🐝*

- **Context windows with stride and different prompts per window**
  - Can use stride for high noise pass and different windows/prompts for low noise pass to avoid overlap issues. Works with echoshot formatting using pipe-separated prompts like 'video of a red panda walking in the forest|video of a red panda jumping into a pond'
  - *From: Kijai*

- **Structured prompting with scene formatting works well**
  - Using numbered scene format [1], [2], [3] or dot notation like 1.env, 1.act, 1.cam for environment, action, camera works better than unstructured prompts
  - *From: NebSH*

- **Stride parameter makes context windows work better**
  - Stride 8-10 works, stride 16 crashes. Creates jitter in high noise pass but low noise pass cleans it up. Mixes up the windows more effectively
  - *From: Kijai*

- **Language-specific prompting affects results**
  - Don't bother writing prompts in English if it's not your native language - try different languages for better results, just like WAN 2.1
  - *From: Daflon*

- **Face quality significantly improved in 2.2**
  - Faces are very detailed compared to 2.1 even when far from camera. 2.1 had disfigured and blurry faces
  - *From: xwsswww*

- **High noise model has better prompt understanding**
  - Only high noise model got the improved prompt understanding training. Using only low noise model shows no difference from 2.1 in prompt following
  - *From: Kijai*

- **Using cfg without speed LoRAs produces significantly better quality**
  - Using high and low model without speed up loras with cfg 5 is like a completely different model, much better quality at 15+15 steps at 256x256 resolution
  - *From: mamad8*

- **quantile_0.15 LoRA gives best T2V results**
  - For T2V get the best results using quantile_0.15 - even prompt adherence and motion is pretty good without compromising too much on 2.2 quality
  - *From: gokuvonlange*

- **Model performs better at 24fps vs 16fps in many cases**
  - 24fps often looks better than 16fps, with 89f 24fps showing better results more often than not
  - *From: Juampab12*

- **First step with CFG important even with LightX2V**
  - Using cfg for the first step is important even when using lightx2v - couldn't get proper motion without it
  - *From: Kijai*

- **LightX strength 0.25 fixes drunkeness with minimal drawback**
  - As little as 0.25 lightx fixes the drunkeness with almost no drawback in prompt adherence
  - *From: Juampab12*

- **SLG and TCFG additions improve results significantly**
  - Added SLG on blocks 7,8,9 and TCFG - that was bigger change than imagined
  - *From: Kijai*

- **Using upscale workflow with speed LoRAs at high res works**
  - Generate at low res using full model without speed improvements, upscale result, then generate at high res on low denoise with speed loras
  - *From: mamad8*

- **Q6 quantization can have extreme quality loss in pixel art**
  - Kijai showed comparison demonstrating severe quality degradation with Q6 on pixel art content
  - *From: Kijai*

- **Wan 2.2 14b and a14b are different model versions**
  - 14b is Wan 2.1, a14b is Wan 2.2, both have T2V and I2V capabilities
  - *From: Juampab12*

- **Wan 2.2 has impressive game knowledge**
  - Model demonstrates understanding of GTA gameplay mechanics and physics in generated videos
  - *From: Juampab12*

- **GGUF format doesn't handle model splitting**
  - GGUF is just a storage format, not related to offloading. Block swap is what moves between CPU and GPU regardless of model format
  - *From: Kijai*

- **MPS (Motion Prediction System) improves realism in bear generations**
  - Grizzly bear looks much more like a real bear with MPS enabled
  - *From: Juampab12*

- **LightX LoRA removes motion blur**
  - LightX lora is killing the motion blur in generations
  - *From: Ruairi Robinson*

- **FPS in prompt may have impact**
  - Early testing suggests fps mentioned in prompt might affect generation
  - *From: DawnII*

- **VACE works with Wan 2.2 high noise model**
  - VACE 1.1 was really wan 2.2 high noise, works perfectly when connected properly
  - *From: GOD_IS_A_LIE*

- **Wan 2.2 has better brand recognition**
  - 2.2 has far better brand recognition in its expanded dataset, gets logos right
  - *From: DawnII*

- **Hand problems are fixed in 2.2**
  - Never get 6 or 4 fingers again, hand generation is outstanding
  - *From: mamad8*


## Troubleshooting & Solutions

- **Problem:** dissolving issues with multiple distil loras using LCM sampler
  - **Solution:** Different distil loras don't use LCM sampler the same way, causing divergence. Either change sampler to euler or dpm, or dump all other distil loras when using light2x
  - *From: Vardogr*

- **Problem:** AccVid causing quality degradation
  - **Solution:** Removing AccVid gave huge quality boost when using LightX2V
  - *From: VRGameDevGirl84(RTX 5090)*

- **Problem:** GPU thermal throttling causing slow performance
  - **Solution:** Check GPU temperatures - if reaching 90C, thermal throttling causes performance issues. Proper cooling needed
  - *From: MysteryShack*

- **Problem:** infinite zooms and cross dissolves with Steerable-Motion not respecting prompt
  - **Solution:** Issue with Steerable-Motion doing infinite zooms between input images instead of following prompts
  - *From: sneako1234*

- **Problem:** ghosting in video output
  - **Solution:** Moviegen at strength 1.0 was causing ghosting artifacts. Disabling moviegen or reducing strength resolved the issue
  - *From: VK (5080 128gb)*

- **Problem:** RecamMaster only supports 81 frames
  - **Solution:** Error 'frame84' occurs because RecamMaster has 81 frame limit
  - *From: Kijai*

- **Problem:** VACE embeds getting overwritten with more than two
  - **Solution:** Update to latest version, bug was fixed
  - *From: Kijai*

- **Problem:** RTX 3090 requiring 40 block swaps at 960x480
  - **Solution:** Use compilation with inductor for speed boost and memory efficiency
  - *From: Kijai*

- **Problem:** Memory issues with large mask surfaces
  - **Solution:** Add a bit of static noise into the mask
  - *From: Mads Hagbarth Damsbo*

- **Problem:** MultiTalk deteriorates on longer clips
  - **Solution:** Uses image from previous gen as input which always deteriorates, context windows needed for 10s+ generations
  - *From: Kijai*

- **Problem:** Tensor mismatch error with Uni3C and end frame
  - **Solution:** Set input Uni3C video to 81 frames and main ImagetoVideo Encode to 77 frames
  - *From: sneako1234*

- **Problem:** MultiTalk with VACE tensor size mismatch
  - **Solution:** Use Rudra's multitalk branch fork with proper modifications
  - *From: Tango Adorbo*

- **Problem:** ComfyUI frontend update broke get/set nodes
  - **Solution:** Downgrade with pip install -U comfyui-frontend-package==1.23.4
  - *From: Kijai*

- **Problem:** Sage Attention 2.0++ flash_attn compilation errors
  - **Solution:** Use specific wheel for sm75 GPUs: pip uninstall sageattention first, then install specific wheel
  - *From: hicho*

- **Problem:** VACE audio/frames mismatch causing crashes
  - **Solution:** Pre-process inputs to 25fps with audio attached for consistency
  - *From: Tango Adorbo*

- **Problem:** WanVideo VACE Start To End Frame node consuming 100% RAM
  - **Solution:** No specific solution provided, issue confirmed by multiple users
  - *From: Yae*

- **Problem:** Loop Args node device mismatch error
  - **Solution:** Expected all tensors to be on same device cuda:0 vs cpu error - no solution provided
  - *From: Juan Gea*

- **Problem:** OOM errors with LoRA loading
  - **Solution:** Enable low_mem_load option in LoRA loader to prevent memory spikes
  - *From: Kijai*

- **Problem:** DSA error in multitalk
  - **Solution:** Set use_non_blocks=false on block swap node to prevent memory pinning issues
  - *From: Colin*

- **Problem:** Context window jumping back to first frame every 81 frames
  - **Solution:** Still working on fix for multitalk context window consistency
  - *From: AJO*

- **Problem:** Can't load tokenizer error with Wav2vec Model
  - **Solution:** Check transformers version - works with current latest version
  - *From: Kijai*

- **Problem:** Tensor dimension mismatch error
  - **Solution:** Using T2V model with I2V workflow - need to use I2V model instead
  - *From: 🦙rishappi*

- **Problem:** TensorRT Upscale node broken after ComfyUI update
  - **Solution:** GitHub issue filed, appears to be widespread problem affecting RTX 5000 series cards
  - *From: Shawneau 🍁 [CA]*

- **Problem:** Error with Wan context options: 'cannot access local variable 'partial_audio_proj'
  - **Solution:** Not fully resolved in chat
  - *From: xwsswww*

- **Problem:** TensorRT upscale not working on 5090
  - **Solution:** Updated driver, now task manager temp updates and doesn't go over 60C when sampling
  - *From: VRGameDevGirl84(RTX 5090)*

- **Problem:** Cannot clone tiled-sampler repository
  - **Solution:** Repository URL appears incorrect or not found
  - *From: xwsswww*

- **Problem:** Video extension at 20s causes CFG color burning
  - **Solution:** Tried to video extend using wan 14b i2v by getting the last frame and using it as a first frame. Got to 20s before it started cfg color burning
  - *From: Rainsmellsnice*

- **Problem:** Load image batch not processing I2V correctly
  - **Solution:** Use Fill node from ComfyUI_Fill-Nodes pack for batch processing images to video
  - *From: JohnDopamine*

- **Problem:** Multitalk with multiple audio files causing errors
  - **Solution:** Masks need to be separated properly - overlapping masks cause separation failures. Use box mode or hand-drawn masks with sufficient spacing
  - *From: Kijai*

- **Problem:** Face consistency issues with VACE + Control_Video
  - **Solution:** add the first frame as reference too... It renders objects, walls, and all other textures perfectly... or maybe we just notice the errors much more when it comes to faces
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Problem:** ComfyUI freezing with spline editor node
  - **Solution:** Update to latest ComfyUI and update pyssss (ShowText node)
  - *From: HeadOfOliver*

- **Problem:** VACE not recognizing input frames with control video
  - **Solution:** Need to mask frames properly - use full white masks for reference frames
  - *From: Kijai*

- **Problem:** Reference image getting superimposed in VACE output
  - **Solution:** Align video to reference image using video editor, controlnet needs to line up closely to avoid ghosting
  - *From: mdkb*

- **Problem:** Normal maps bleeding into VACE results
  - **Solution:** VACE not trained on normals, works only through generalization - desaturate and blur normal maps
  - *From: Kijai*

- **Problem:** VACE not swapping into white masked areas without LoRAs
  - **Solution:** For inpainting, need to add grey to masked area in input video AND use corresponding white mask
  - *From: Rishi Pandey*

- **Problem:** Context generation finishing with no video output
  - **Solution:** Issue was with using forked code instead of official Kijai code
  - *From: Juan Gea*

- **Problem:** VACE not using reference images
  - **Solution:** Add white border padding around reference images - they need white borders to work properly
  - *From: mdkb*

- **Problem:** Size tensor mismatch error with WanVideoSampler
  - **Solution:** Switch from Normal Crafter to Deep Crafter, or restart server for 1-2 more generations
  - *From: DreamWeebs*

- **Problem:** RTX 5090 CUDA kernel error with SageAttention
  - **Solution:** Use woct0rdho's SageAttention wheel from GitHub releases - Kijai's precompiled wheel wasn't compiled for 5090
  - *From: AJO*

- **Problem:** ComfyUI freezing after generation
  - **Solution:** Hit play on video in queue history to kick things back into gear when run button stops working
  - *From: phazei*

- **Problem:** MultiTalk frame count inconsistency
  - **Solution:** Use 209 frames to get approximately 249 frames output (10 seconds at 25fps), pad audio to 9.96 seconds to maintain sync
  - *From: AJO*

- **Problem:** VACE not working with reference images
  - **Solution:** Padding reference image isn't reliable, focus on explicit prompting about what to do with the reference
  - *From: mdkb*

- **Problem:** Memory issues after using ControlNet with VACE
  - **Solution:** Need to use blocks with VACE, and reboot ComfyUI if turning off CN to use Wan without blocks at full speed
  - *From: N0NSens*

- **Problem:** Limited head movement in MultiTalk
  - **Solution:** Use vid2vid with MultiTalk, set denoise less than 1.0, or try MagRef model for more movement with slight quality hit
  - *From: samhodge*

- **Problem:** Pixelated results with CausVid
  - **Solution:** May be related to reference image resolution - check if reference image is being read at low resolution
  - *From: xwsswww*

- **Problem:** ImportError: peft>=0.15.0 required but found peft==0.14.0
  - **Solution:** pip install --upgrade peft
  - *From: pagan*

- **Problem:** VACE inpainting producing latent mud/brown splotches
  - **Solution:** Use VACE module (Wan2_1-VACE_module_14B_bf16.safetensors) instead of full model
  - *From: Hashu*

- **Problem:** Mask alignment issues in VACE
  - **Solution:** Update KJNodes to latest version for mask resizing functionality
  - *From: Kijai*

- **Problem:** Snow/white dust artifacts with LightX2V
  - **Solution:** Use 4 steps instead of 10+ steps, reduce LoRA strength
  - *From: Atlas*

- **Problem:** Depth control video affecting final output geometry
  - **Solution:** Lower control strength values, use segmentation masks to isolate specific parts
  - *From: N0NSens*

- **Problem:** WanVideo Context options tensor size mismatch error
  - **Solution:** Remove the context options node if error persists
  - *From: xwsswww*

- **Problem:** ComfyUI VRAM management doesn't account for browser/monitor usage
  - **Solution:** Launch comfy with --reserve-vram <extra memory in gb>, for example --reserve-vram 2 would reserve 2GB
  - *From: Kijai*

- **Problem:** GGUF support breaking with VRAM management
  - **Solution:** Remove VRAM management when using GGUF, block swap works though
  - *From: hicho*

- **Problem:** ValueError with tensor shapes in GGUF VACE models
  - **Solution:** Updated wrapper code to handle Q5 mixed tensor shapes and other GGUF compatibility issues
  - *From: Kijai*

- **Problem:** Context window snapping in I2V models with MultiTalk
  - **Solution:** Every window needs the input image so if output drifts too far from it, it snaps back. Use the other multitalk workflow without context windows but with length limit
  - *From: Kijai*

- **Problem:** OOM with 4060ti 16GB at 33 frames 480p with wrapper
  - **Solution:** Disable 'non-blocking' option in advanced settings
  - *From: Kijai*

- **Problem:** Getting horrible ComfyUI results vs gradio app
  - **Solution:** Use speed LoRAs like LightX2V, use native text encoder with fp8, gradio app is optimized out of the box
  - *From: hicho*

- **Problem:** OOM when loading LoRA on model loader
  - **Solution:** Turn on 'low_mem_load' option on LoRA loader
  - *From: Cseti*

- **Problem:** GGUF models with MultiTalk throwing 'GGUFParameter object has no attribute quant_type' error
  - **Solution:** Disable torch.compile, seems to cause this issue for some users
  - *From: Kijai*

- **Problem:** 2060 GPU not supporting bf16
  - **Solution:** Use fp8 VAE with fp16 instead, GPU doesn't support bf16 due to older CUDA compute version
  - *From: hicho*

- **Problem:** VACE inpainting outputs black when feeding mask
  - **Solution:** Feed mask directly to encode node, don't need start/end frame if feeding all frames
  - *From: Kijai*

- **Problem:** High speed dynamics lora causes noise with GGUF
  - **Solution:** Use at 0.1 strength instead of 1.0, or update to fixed version with fp32 calculations
  - *From: Kijai*

- **Problem:** Some styling loras cause blocking with GGUF
  - **Solution:** detailenhance and realismboost don't work with GGUF in wrapper, but detailz-wan and MPS work
  - *From: mdkb*

- **Problem:** CUDA kernel error when going over certain frame count
  - **Solution:** Likely input dimension not divisible by 16 or frame count issue
  - *From: Kijai*

- **Problem:** Spline editor node hardlocks ComfyUI UI when zooming in
  - **Solution:** Update KJNodes - issue was fixed few weeks ago
  - *From: Kijai*

- **Problem:** Black artifacts in video generation
  - **Solution:** Check if using correct ATI model - appears when not using ATI model
  - *From: Kijai*

- **Problem:** ATI tracking not working
  - **Solution:** Need to use custom ATI model from HuggingFace, not regular model
  - *From: Juampab12*

- **Problem:** Memory leak with GGUF and LoRAs
  - **Solution:** Reboot ComfyUI when RAM usage climbs after changing LoRA settings
  - *From: David Snow*

- **Problem:** LoRAs too strong (10x) after wrapper update
  - **Solution:** Use 0.1 strength instead of normal values
  - *From: Kijai*

- **Problem:** LoRA alpha scaling not working
  - **Solution:** Problem was ComfyUI does scaling on weight calculation, not load - fixed in wrapper update
  - *From: Kijai*

- **Problem:** UnboundLocalError: cannot access local variable 'x0'
  - **Solution:** Fixed in wrapper update
  - *From: Kijai*

- **Problem:** 'WanModel' object has no attribute 'vace_patch_embedding'
  - **Solution:** Need to load a VACE model - use small VACE module files, not large combined files
  - *From: Kijai*

- **Problem:** GGUF models failing to load with wrapper
  - **Solution:** Update to latest wrapper version, or manually convert and quantize models if downloaded weights are corrupted
  - *From: MysteryShack*

- **Problem:** VACE inpainting not working as expected
  - **Solution:** Logic for start/end index was fixed in recent update
  - *From: Kijai*

- **Problem:** Load image and save image nodes not previewing
  - **Solution:** Try updating all nodes and manually updating KJ components in manager
  - *From: mdkb*

- **Problem:** MultiTalk context workflow causing OOM at longer durations
  - **Solution:** Use block swaps at 20, set everything to use offload devices, but may still be limited by VRAM at very long durations
  - *From: AJO*

- **Problem:** Ghosting in anime content with I2V
  - **Solution:** Increase shift value from 1 to higher values to reduce ghosting
  - *From: VRGameDevGirl84(RTX 5090)*

- **Problem:** Stalled and backwards motion in longer generations
  - **Solution:** Use NAG with negative prompting or controlnet depthmaps from Blender animations
  - *From: JohnDopamine*

- **Problem:** Not using first frame properly in VACE workflow
  - **Solution:** Put the reference image into first frame input, not just reference - this is a common mistake people make
  - *From: Draken*

- **Problem:** TeaCache incompatible with FusionX
  - **Solution:** Don't use TeaCache with FusionX - it skips steps and FusionX already has low steps, dropping them too much
  - *From: Juampab12*

- **Problem:** Obvious tile artifacts in SuperUltimateVaceTools upscaling
  - **Solution:** Try using without tiled sampler or use tile lora instead - may be issue with tile stitching
  - *From: David Snow*

- **Problem:** LightX2V kills motion and reduces lora adherence
  - **Solution:** Use CausVid + AccVid combination instead, or adjust to lower lora strengths like Moviigen 0.5, MPS 0.5 for people
  - *From: Kenk*

- **Problem:** Steps parameter forced to 20 regardless of input
  - **Solution:** Check if cfg scheduling is connected - it overrides step count even if not used
  - *From: Kijai*

- **Problem:** OOM on second generation with text encode nodes
  - **Solution:** Issue occurs when splitting to WanVideoTextEncodeSingle nodes, use bridge to text embeds in wrapper workflows
  - *From: mdkb*

- **Problem:** Context Options changing characters every 21 frames
  - **Solution:** This happens with v2v workflows with high denoise, unlike i2v or t2v which maintain consistency
  - *From: mdkb*

- **Problem:** Zombie hordes appearing in background crowds
  - **Solution:** Issue persists even with LoRAs, appears as thousand people staring and not moving in background
  - *From: mdkb*

- **Problem:** Dynamo error with multitalk
  - **Solution:** Error occurs with FakeTensor index out of bounds, related to VRAM limits with multiple audio inputs
  - *From: craftogrammer*

- **Problem:** Invalid tokenizer error with GGUF
  - **Solution:** Need UMT5 for WAN, not regular T5 tokenizer
  - *From: hicho*

- **Problem:** Scheduler error with cfg distill LoRA
  - **Solution:** Don't use certain schedulers, use lcm, lcm/beta, or dpm++ sde instead
  - *From: DawnII*

- **Problem:** LoRAs don't work with Vace I2V
  - **Solution:** LoRAs only work with standard I2V model, not Vace I2V
  - *From: hicho*

- **Problem:** Face changes when using MPS settings
  - **Solution:** Dial down MPS to reduce face changes, but may cause 'sharpen' effects with extra detail appearing on skin
  - *From: lostintranslation*

- **Problem:** Old workflows running slow with KJ wrapper
  - **Solution:** Need to 'fix node' or recreate nodes after updates, remove and create new nodes instead of just updating
  - *From: mdkb*

- **Problem:** Dependency error when loading benji_Wan_Vace-Native-V2V-CN Long Video
  - **Solution:** Install missing dependency - ComfyUI-MultiGPU
  - *From: el marzocco*

- **Problem:** LightX2V at lower strength causes pixelated artifacts
  - **Solution:** Lower LightX2V strength requires more steps to avoid artifacts - 0.8 strength needs more steps than 1.0
  - *From: MysteryShack*

- **Problem:** Depth map issues in VACE
  - **Solution:** Blur the depth map a bit
  - *From: Kijai*

- **Problem:** Tensor size mismatch error 'Expected size 26 but got size 1'
  - **Solution:** Video frame number different from output embed frame number - check output frame number setting
  - *From: mdkb*

- **Problem:** Mask video gets rejected in VACE
  - **Solution:** Convert video to mask and plug into mask slot, don't put video in ref_images
  - *From: ingi // SYSTMS*

- **Problem:** Context shifts in long video generation
  - **Solution:** Increase overlap - more overlap helps but makes it slower, up to 64 overlap tested successfully
  - *From: Kijai*

- **Problem:** Image resize mask node error with Lanczos upscale method
  - **Solution:** Change upscale method from Lanczos to another option
  - *From: The Shadow (NYC)*

- **Problem:** VACE not working well with single frame
  - **Solution:** Try generating 5 frames instead of 1 frame
  - *From: Hashu*

- **Problem:** Resize image v2 mask input missing after update
  - **Solution:** Delete the lowercase 'comfyui-kjnodes' folder and do fresh git clone instead of using ComfyUI Manager
  - *From: Gateway {Dreaming Computers}*

- **Problem:** Snow falling in output when reducing film grain strength
  - **Solution:** Issue occurs but no clear solution provided
  - *From: xwsswww*

- **Problem:** Static snowstorm of last frame when frame count mismatch
  - **Solution:** Make sure frame count in embed video matches the video input frame count
  - *From: mdkb*

- **Problem:** Sage attention dtype error
  - **Solution:** Check if fp32 is selected instead of fp16, use FP16_fast exclusively
  - *From: JohnDopamine*

- **Problem:** Distorch node error after update
  - **Solution:** Use 'fix node' option in ComfyUI to recreate the node
  - *From: mdkb*

- **Problem:** SageAttention outputs only black frames
  - **Solution:** Don't use sage or torch compile node
  - *From: hicho*

- **Problem:** Triton installation error
  - **Solution:** Need triton installed and windows cpp build tools
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Problem:** System RAM being consumed
  - **Solution:** Use --cache-none in ComfyUI boot
  - *From: Gateway {Dreaming Computers}*

- **Problem:** Tensor size mismatch (112) vs (136) at dimension 4
  - **Solution:** Check frame amounts match and resolutions are correct
  - *From: JohnDopamine*

- **Problem:** Discord workflow extraction
  - **Solution:** Need second click on image to get original PNG with workflow, first click gives webp
  - *From: phazei*

- **Problem:** Mask gets grey color when padding
  - **Solution:** Issue acknowledged but workaround needed
  - *From: Gateway {Dreaming Computers}*

- **Problem:** Set/Get nodes causing NAG errors
  - **Solution:** Remove Set/Get nodes from the workflow
  - *From: Valle*

- **Problem:** UNI3C tensor size mismatch error
  - **Solution:** Change VHS Load Video format from AnimateDiff to WAN format
  - *From: Juan Gea*

- **Problem:** T2V rank64 LoRA not working
  - **Solution:** T2V rank64 LoRA appears to have upload issues, but I2V rank64 LoRA works fine
  - *From: slmonker(5090D 32GB)*

- **Problem:** LightX LoRA causing horror movie results on VACE
  - **Solution:** Use DPM++_SDE or LCM scheduler instead of UniPC, and increase strength to 1.1-1.2 for rank32
  - *From: DawnII*

- **Problem:** Model merge nodes don't connect to KJ sampler
  - **Solution:** Native merge nodes cannot directly connect to KJ wrapper nodes due to different architectures
  - *From: DawnII*

- **Problem:** Uni3C not loading with frame count issues
  - **Solution:** Set width to 960 on VHS load, check frame count - error seems about frames
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Problem:** Updating diffusers broke ComfyUI
  - **Solution:** Update peft to >=0.15.0 when updating diffusers, also may need numpy<2
  - *From: Juan Gea*

- **Problem:** VACE + Uni3C incompatibility
  - **Solution:** VACE and Uni3C may be incompatible - causes channel mismatch errors
  - *From: Juan Gea*

- **Problem:** T2V LoRA not working
  - **Solution:** T2V lora still has issues, I2V lora works for both T2V and I2V models
  - *From: multiple users*

- **Problem:** Color drift over time in videos
  - **Solution:** Use color matching node from image reference
  - *From: Juan Gea*

- **Problem:** LoRA key not loaded errors
  - **Solution:** These are warnings that don't prevent functionality - lora still works despite errors
  - *From: Piblarg*

- **Problem:** UNi3C cannot be mixed with VACE - frame mismatch error
  - **Solution:** UNi3C is for I2V models only. VACE adds reference to latents so you'd need +4 Uni3C images, but even then would get input channel count mismatch
  - *From: Kijai*

- **Problem:** Original T2V LightX2V lora is broken
  - **Solution:** Use the newly extracted versions from Kijai's repo instead of the original broken one
  - *From: Kijai*

- **Problem:** Lora key not loaded warnings when using I2V lora on T2V model
  - **Solution:** Those are normal I2V model keys - can be ignored but you probably shouldn't use I2V lora on T2V model
  - *From: Kijai*

- **Problem:** Self-Forcing LoRA not working with Native TorchCompile
  - **Solution:** Use Native TorchCompileModel node instead of KJNode version for Self-Forcing LoRA with Native workflow
  - *From: brbbbq*

- **Problem:** TeaCache breaks LightX2V LoRA completely
  - **Solution:** Remove TeaCache when using LightX2V LoRA - it's not needed and causes issues
  - *From: hicho*

- **Problem:** Bad Self-Forcing LoRA from Civitai causing poor results
  - **Solution:** Use Kijai's LoRA versions from HuggingFace instead of Civitai versions
  - *From: David Snow*

- **Problem:** VACE control images showing up in generation instead of influencing
  - **Solution:** Control images only work properly on first batch in daisy-chained workflows, not continuation batches
  - *From: The Shadow (NYC)*

- **Problem:** LightX2V generated videos cause discoloration when extended with VACE
  - **Solution:** Base Wan generated videos work fine with VACE extension, but LightX2V videos have compatibility issues
  - *From: daking999*

- **Problem:** Resize Image v2 node causing VACE encode validation errors
  - **Solution:** Issue occurs when piping resized masked output into VACE encode mask input
  - *From: Guey.KhalaMari*

- **Problem:** Frame count mismatch error in MultiTalk workflow
  - **Solution:** Check for frame count mismatches between different components
  - *From: Kijai*

- **Problem:** Array must not contain infs or NaNs error with scaled models
  - **Solution:** Scaled models don't work in the wrapper
  - *From: Kijai*

- **Problem:** Pusa end frame flashing badly
  - **Solution:** Workaround is to do 85 frames instead and drop the last latent
  - *From: Kijai*

- **Problem:** TypeError: 'NoneType' object is not iterable
  - **Solution:** Fixed in recent update
  - *From: Kijai*

- **Problem:** Prompt travel with | separator not working
  - **Solution:** Probably broken with an update, feature needs fixing
  - *From: Kijai*

- **Problem:** TypeError: 'NoneType' object is not iterable with lightx2v LoRAs at CFG 2
  - **Solution:** Use CFG 1 or increase steps to at least 10+ with Euler sampler
  - *From: MilesCorban*

- **Problem:** Pusa changes initial frame too much at weight 1.0
  - **Solution:** Use LoRA weight of 1.4 or higher
  - *From: Kijai*

- **Problem:** Radial attention requires dimensions divisible by 128
  - **Solution:** Use resolutions like 1280x768 instead of 1280x720
  - *From: Kijai*

- **Problem:** GTX 1070 8GB struggling with fp8 text encoder
  - **Solution:** Use GGUF text encoder with bridge node
  - *From: Doctor Shotgun*

- **Problem:** ComfyUI slow loading (3-4 minutes)
  - **Solution:** Use SSD for ComfyUI installation, move frequently used models to SSD
  - *From: AmirKerr*

- **Problem:** Slow generation speed on 8GB VRAM
  - **Solution:** Use block swapping. Set block_swap parameter higher (increase by 5) and enable 'no fallback' in NVIDIA control panel to get errors instead of slowdowns
  - *From: Kijai, Juampab12*

- **Problem:** Memory issues causing slowdowns
  - **Solution:** Close browser tabs, especially Chrome and ComfyUI tabs. Windows and browser usage on same GPU can cause memory pressure
  - *From: Kijai*

- **Problem:** VRAM allocation issues
  - **Solution:** Set NVIDIA control panel to 'no fallback' to error on allocation instead of going super slow
  - *From: Juampab12*

- **Problem:** Radial attention requires resolutions divisible by 128
  - **Solution:** Use 1280x768 instead of 1280x720 - Wan isn't strict about exact bucket sizes
  - *From: Kijai*

- **Problem:** FP8 models using 50GB+ system RAM causing OOM
  - **Solution:** Issue started 2-3 days ago, GGUF models work fine as alternative
  - *From: Draken*

- **Problem:** Multitalk OOM on 12GB VRAM
  - **Solution:** Turn off 'use-non-blocking' setting in workflow
  - *From: mdkb*

- **Problem:** Both characters talking in multitalk with single audio
  - **Solution:** Provide silent audio track to second speaker and mask both characters
  - *From: DawnII*

- **Problem:** GGUF conversion of merged models not working
  - **Solution:** Custom node GGUF conversion works for other quantizations but not GGUF unfortunately
  - *From: JmySff*

- **Problem:** GGUF quantization failing on Windows
  - **Solution:** Install latest version of CMake and add it to PATH before launching GGUF quantization
  - *From: JmySff*

- **Problem:** Tensor size mismatch when using WanVaceToVideo and WanPhantomSubjectToVideo together
  - **Solution:** Use patcher node to handle phantom embeds properly
  - *From: Ablejones*

- **Problem:** OOM errors with PUSA and context windows
  - **Solution:** Use dpm++_sde scheduler instead of flowmatch_pusa scheduler with context, or disable PUSA
  - *From: Juan Gea/Kijai*

- **Problem:** Reference image flickering with wrapper + phantom
  - **Solution:** Latent isn't trimmed properly when combined with phantom in wrapper
  - *From: theUnlikely*

- **Problem:** VAE OOM at high resolution
  - **Solution:** Use tiled VAE for high resolution processing like 1920x1152
  - *From: Juan Gea/Kijai*

- **Problem:** Uni3C size errors with radial attention
  - **Solution:** Radial attention requires resolution divisible by 128 (vs Wan's 16)
  - *From: hicho*

- **Problem:** I2V model generating noise when used without image input
  - **Solution:** Switch to T2V model if you don't have start image, can't use i2v model without i2v image embed
  - *From: Kijai*

- **Problem:** First frame flickering and black mask issue with VACE
  - **Solution:** Bug was fixed - cached mask wasn't resetting on resolution change. Use the mask you already had if you don't want node to override
  - *From: Kijai*

- **Problem:** ComfyUI not showing new samplers after update
  - **Solution:** Manually delete the node in custom_nodes and re-install to absolutely make sure
  - *From: Kijai*

- **Problem:** Chinese wav2vec required for MultiTalk sync
  - **Solution:** Only the Chinese wav2vec works, the others won't sync at all. The tencent model is trained on top of the english one so it still works
  - *From: Kijai*

- **Problem:** WAN 14B crashes during VAE decode with RAM filling to 99%
  - **Solution:** Use UMT5 fp8 6GB text encoder and disable block swapping. Achieved 96% VRAM and 92% RAM usage at 480x640 51 frames
  - *From: mborgo*

- **Problem:** Uni3C wrapper errors after update
  - **Solution:** Update wrapper again - issue was uni3c related and fixed for different ComfyUI versions
  - *From: Kijai*

- **Problem:** MultiTalk embed node doesn't work with certain setups
  - **Solution:** Use context windows workflow instead of multitalk embed node
  - *From: Kijai*

- **Problem:** CausVid LoRA requires exactly 4 steps but errors even with 4 steps
  - **Solution:** Set steps to 5 instead of 4, and use flowmatch_pusa scheduler
  - *From: Juan Gea*

- **Problem:** MultiTalk wav2vec attention error
  - **Solution:** Update to latest WanVideoWrapper nodes - the output_attentions SDPA issue was fixed
  - *From: Kijai*

- **Problem:** AttributeError: 'WanModel' object has no attribute 'vace_patch_embedding'
  - **Solution:** Need to load proper VACE model, not just base model
  - *From: Kijai*

- **Problem:** MultiTalkWav2VecEmbeds output_attentions error
  - **Solution:** Delete and reinstall ComfyUI-WanVideoWrapper nodes
  - *From: Kijai*

- **Problem:** WanVideoSampler 'log' is not defined error
  - **Solution:** Update the nodes - was a bug that got fixed
  - *From: Kijai*

- **Problem:** Triton compilation taking 5 minutes with merge_loras false
  - **Solution:** Expected behavior when changing LoRAs, but should be fast normally. Clear triton cache if erroring
  - *From: Kijai*

- **Problem:** Generation above 93 frames starts with flash
  - **Solution:** Use skip frames in final output - expected as model not trained for that length
  - *From: Kijai*

- **Problem:** PUSA doesn't get concepts from existing LoRAs well
  - **Solution:** LoRAs would need to be trained specifically on Pusa
  - *From: phazei*

- **Problem:** Error 'Cannot copy out of meta tensor; no data!' when using merge_lora=false
  - **Solution:** Low mem has to be false too when merge lora is false
  - *From: Kijai*

- **Problem:** Error 'name 'log' is not defined' with WanVideoSampler
  - **Solution:** Disable the 'verbose' in the context options to disable logging, or update to latest version where log is defined
  - *From: Kijai*

- **Problem:** IndexError with Context Options using NAG and CFG=1.0
  - **Solution:** Select 'sdpa' as attention mode in the uni3c node instead of using triton/sageattention
  - *From: Kijai*

- **Problem:** VRAM doesn't clear after failed generation
  - **Solution:** Have to restart ComfyUI, the vram clear on rightclick menu doesn't work for this issue
  - *From: Qok*

- **Problem:** Fun Control model just copies first frame over and over
  - **Solution:** Reference needs to go into fun_ref_image not the imagetovideo encode, that one is for i2v
  - *From: Hashu*

- **Problem:** VACE pose control not working properly
  - **Solution:** Use careful masking - white masks for areas where you want VACE to generate new content, avoid 100% matching start frames
  - *From: Hashu*

- **Problem:** Character looking like openpose rigs
  - **Solution:** Be really careful about masking - need white masks over control pose image frames
  - *From: Ablejones*

- **Problem:** T2V model getting I2V inputs error
  - **Solution:** Weights loaded have 16 channels (T2V model) but workflow giving 36 channel I2V inputs - need to match model type to workflow
  - *From: Kijai*

- **Problem:** V2V workflow barely changing video
  - **Solution:** Using wrong LoRA for model (1.3B LoRA on 14B model), not enough steps (4 steps insufficient), shouldn't use causvid for this type of content
  - *From: Kijai*

- **Problem:** System RAM crashes on cloud VMs
  - **Solution:** Use --cache-none flag to help with crashes when system ram hits limit, though it removes cached nodes that speed things up
  - *From: Gateway {Dreaming Computers}*

- **Problem:** DPM SDE++ not working in native
  - **Solution:** Many native samplers don't work with normal scheduler, need to use wrapper for proper SDE support
  - *From: Draken*

- **Problem:** e5m2_scaled quantization model not loading
  - **Solution:** Fixed missing check in WanWrapper update - e4m3fn_scaled works as alternative
  - *From: Kijai*

- **Problem:** Non-blocking block swap causing CUDA OOM crashes
  - **Solution:** Turn off non-blocking mode for systems with low RAM - pins RAM for async transfers but reserves more VRAM
  - *From: Kijai*

- **Problem:** Blurred results in I2V and VACE generations
  - **Solution:** Issue persists across different samplers and step counts (4,6,8,12) and shift values (1-8) - no solution provided
  - *From: Juan Gea*

- **Problem:** Second pass noise when passing latents directly
  - **Solution:** Use decode VAE then re-encode route, or try different schedulers (dpm++_sde, euler/beta), set rope function to 'comfy', check for seed conflicts
  - *From: mamad8*

- **Problem:** LoRAs at 0 weight still causing loading delays
  - **Solution:** Use Set LoRA node and latest WanWrapper update that includes 0 strength check to skip loading
  - *From: Kijai*

- **Problem:** LightX I2V LoRA throwing tuple error when unmerged
  - **Solution:** Merge the LoRA - when merged it skips problematic 36 ch weights and runs fine. Issue caused by useless 'head' layer keys with dim2
  - *From: DawnII, Kijai*

- **Problem:** UniC3 causing distortion
  - **Solution:** Change scheduler, avoid using too many LoRAs as UniC3 conflicts with some AI effects, use full distill mode
  - *From: VRGameDevGirl84(RTX 5090), hicho*

- **Problem:** Set LoRA node error with VRAM management
  - **Solution:** Use block swap instead of VRAM management, or use WanVideo Set BlockSwap node
  - *From: hicho, 748197775237447781*

- **Problem:** Error when bypassing first frame to use last frame only
  - **Solution:** Functionality may not be properly supported - need to ask developer
  - *From: Ruairi Robinson, VRGameDevGirl84(RTX 5090)*

- **Problem:** LoRA weights taking 15 minutes to compile
  - **Solution:** Use Set LoRA node for faster compilation
  - *From: sneako1234, hicho*

- **Problem:** SageAttention SM89 kernel error on RTX 5090
  - **Solution:** Update xformers, avoid torch 2.9 and cuda 12.9 as they're unstable
  - *From: Charlie*

- **Problem:** MAGREF not working with native ComfyUI nodes
  - **Solution:** Add white background/padding to reference image and ensure frame length > 1
  - *From: Simplesmente IA*

- **Problem:** Context windows snapping back to init image
  - **Solution:** Use MAGREF with padded reference images for windows beyond first frame
  - *From: Kijai*

- **Problem:** High RAM usage with block swap enabled
  - **Solution:** Block swap node can consume 109GB RAM but helps with VRAM limitations
  - *From: Drommer-Kille*

- **Problem:** WanVideoWrapper installation error in ComfyUI Manager
  - **Solution:** Delete the Node folder and install via git clone instead of using the manager
  - *From: Gill Bastar*

- **Problem:** WanVideoEmptyEmbeds error about extra_latents
  - **Solution:** Update the wrapper nodes - it's a version mismatch issue
  - *From: ZeusZeus (RTX 4090)*

- **Problem:** Cannot copy out of meta tensor error with I2V 720P scaled model
  - **Solution:** Disable 'low vram load' option - scaled models only work with unmerged loras and unmerged + lowvram doesn't work
  - *From: Juan Gea*

- **Problem:** ComfyUI not accepting mp4 files for workflow extraction
  - **Solution:** Extract just the 'workflow' part from the metadata, starting after the 'workflow' key and including the closing brace
  - *From: Draken*

- **Problem:** rope_function 'comfy_chunked' causing LoRA issues
  - **Solution:** Set rope_function back to 'comfy' instead of 'comfy_chunked'
  - *From: Hashu*

- **Problem:** Pusa LoRA won't work unmerged
  - **Solution:** LoRA needs to be merged as it's 4GB and terrible to use unmerged
  - *From: Kijai*

- **Problem:** LoRA bug only worked with SetLoRA node
  - **Solution:** Use the SetLoRA node instead of connecting directly to model loader
  - *From: Kijai*

- **Problem:** First few frames super compressed/messy in I2V
  - **Solution:** This was caused by CausVid LoRA - switch to LightX2V
  - *From: hicho*

- **Problem:** Duplication problems with accelerators
  - **Solution:** Issue occurs at 1280x720 resolution, switching to 1280x768 fixes the problem
  - *From: Juan Gea*

- **Problem:** Can't use Pusa with I2V models
  - **Solution:** Pusa is only for T2V models - don't use it with I2V
  - *From: Kijai*

- **Problem:** Long prompts cause errors in WanWrapper
  - **Solution:** Truncate prompts to 512 tokens or modify lines 1157-1158 to handle overflow
  - *From: patientx*

- **Problem:** Flash artifacts appearing in PUSA video extension
  - **Solution:** Use proper frame overlap (4+1 rule, try 13 frames), reduce noise injection, or use frame blending
  - *From: Kijai*

- **Problem:** SetLoras node not working with GGUF
  - **Solution:** Bug was fixed in latest version
  - *From: Kijai*

- **Problem:** OOM issues when using SageAttention 2
  - **Solution:** SageAttention 2 requires more VRAM than version 1, may need to reduce frame count or increase block swap
  - *From: Juan Gea*

- **Problem:** Quality drops over time with PUSA extension
  - **Solution:** Color shifting is less than VACE but aesthetic quality still degrades, slight saturation boost between gens helps
  - *From: DawnII*

- **Problem:** Quality degradation in second generation with blending
  - **Solution:** Try doing full 81 frames instead of shorter sequences, reduce overlap frames
  - *From: Kijai*

- **Problem:** Scheduler error 'only for 4 steps'
  - **Solution:** Denoise modifies step count, that scheduler isn't important anyway
  - *From: Kijai*

- **Problem:** Style drift in I2V with anime LoRA
  - **Solution:** Don't use anime LoRA with I2V - base Wan can handle anime with proper prompting
  - *From: hicho*

- **Problem:** Pusa fails to retain input frame at higher aspect ratios
  - **Solution:** 1280x720 is unreliable, lower resolutions like 832x480 work better
  - *From: Koba*

- **Problem:** Memory usage with LoRA key backups
  - **Solution:** Removed key backup when merging in wrapper and got 20GB RAM free during sampling
  - *From: Kijai*

- **Problem:** WAN doesn't understand 'naked' but reads 'nude'
  - **Solution:** Use 'nude' instead of 'naked' in prompts for better results
  - *From: Ryzen*

- **Problem:** Color degradation and shifting in VACE long-form video
  - **Solution:** Either render full length in one go or use PUSA extension for better continuations instead of cross-fading VACE segments
  - *From: gokuvonlange*

- **Problem:** Skeleton drawings visible in final output
  - **Solution:** Issue acknowledged but no specific solution provided in this discussion
  - *From: Gill Bastar*

- **Problem:** MultiTalk works better in Chinese than English
  - **Solution:** Consider using Chinese phonetics for English speech or use Chinese audio samples for better results
  - *From: Grimm1111*

- **Problem:** Context windows cause less dynamic motion in long videos
  - **Solution:** Use MultiTalk continuation mode instead for better motion preservation up to 10 seconds
  - *From: Kijai*

- **Problem:** SageAttention 3 using excessive VRAM
  - **Solution:** Set per_block_mean=False to reduce VRAM usage to sage2 levels
  - *From: Kijai*

- **Problem:** Florence2 errors after ComfyUI update
  - **Solution:** Probably have to downgrade transformers for now - transformers keeps breaking Florence2
  - *From: Kijai*

- **Problem:** SageAttention 3 going OOM on activation steps
  - **Solution:** Uses about 5GB more VRAM than sage2, requires block swapping on higher resolutions
  - *From: Kijai*

- **Problem:** Building SageAttention 2 on Ubuntu 25.04
  - **Solution:** Can use prebuilt wheels from https://github.com/woct0rdho/SageAttention/releases/tag/v2.2.0-windows or build locally on Linux
  - *From: Kijai*

- **Problem:** Florence not working after ComfyUI update
  - **Solution:** Revert transformers from 4.54.0 to 4.52.0
  - *From: phazei*

- **Problem:** Radial attention not working
  - **Solution:** Need both the WanVideo Radial Attention node and attention_mode set in model loader
  - *From: Kijai*

- **Problem:** Torch compile error on Ampere GPUs
  - **Solution:** Use fp8 e5m2 with compile on Ampere generation GPUs like A6000/3090
  - *From: Kijai*

- **Problem:** ComfyUI updating transformers automatically
  - **Solution:** Edit requirements.txt in ComfyUI root folder and comment out transformers line
  - *From: JohnDopamine*

- **Problem:** MultiTalk only works with specific models
  - **Solution:** MultiTalk needs I2V model in workflow, not T2V models like VACE. Works well with MagRef
  - *From: Kijai*

- **Problem:** 1.3B LoRAs not loading properly in ComfyUI
  - **Solution:** ComfyUI may have compatibility issues with 1.3B LoRAs, thinks they're I2V when they're T2V
  - *From: Drommer-Kille*

- **Problem:** ModuleNotFoundError for diffusers.quantizers.gguf when using EchoShot
  - **Solution:** Need to update diffusers package
  - *From: VK*

- **Problem:** Prompt bleeding between scenes in EchoShot
  - **Solution:** Use uniting phrases across all prompts, like 'a humanoid hamster in a tweed coat' at start of each prompt
  - *From: VK*

- **Problem:** VACE reference makes prompts bleed more in EchoShot
  - **Solution:** VACE seems too strong and keeps the scene, though actions go through. Consider background removal and padding for reference
  - *From: Kijai*

- **Problem:** Division by zero error with context plugged in
  - **Solution:** Update Python dependencies for ComfyUI
  - *From: xwsswww*

- **Problem:** Tensor size error when using mask with resize node v2
  - **Solution:** Ensure both image and mask pass through same resize node
  - *From: hicho*

- **Problem:** Preview nodes not working after updates
  - **Solution:** Make new environment and manually git pull on suspect custom nodes
  - *From: Flipping Sigmas*

- **Problem:** OOM at VAE decode with long sequences
  - **Solution:** Use tiled VAE decode or native VAE node with automatic tiling
  - *From: Kijai*

- **Problem:** Memory issues with high frame counts
  - **Solution:** Use torch.compile, chunked rope, or full block swap
  - *From: Kijai*

- **Problem:** Alpha channel error with body segmentation
  - **Solution:** Strip alpha channel or use color instead. Kijai can update wrapper to strip alpha automatically.
  - *From: hicho/Kijai*

- **Problem:** LoRA won't generalize to different scenes
  - **Solution:** Use detailed captions for all samples and describe the scene/background, not just the action. Caption both first and last frames.
  - *From: mamad8*

- **Problem:** Torch compile gets stuck at 0% on interpolate node
  - **Solution:** Try lower precision like bfloat16 instead of fp32
  - *From: OxygenConsumer/˗ˏˋ⚡ˎˊ-*

- **Problem:** Division by zero error with Minimax remover
  - **Solution:** Issue is no prompts when using context windows - Kijai added logic to handle this
  - *From: A.I.Warper/Kijai*

- **Problem:** Slow generation with wrapper (30min vs 3min)
  - **Solution:** Increase block swap up to 40, swap at least 1 VACE block, use sageattn instead of sdpa
  - *From: Drommer-Kille/Kijai*

- **Problem:** Can't extract single latent from video batch
  - **Solution:** Use KJ GetLatentRangeFromBatch node. Note: cutting latents affects VAE decoding due to temporal nature.
  - *From: mamad8/Kijai*

- **Problem:** Blender depth maps don't work with Wan
  - **Solution:** Blur the depth map a bit, or use DepthAnything v2
  - *From: Drommer-Kille/Kijai*

- **Problem:** Generation taking 22 minutes at 1200x672
  - **Solution:** Reduce resolution to 1024x576 (brought time down to 3 minutes) or use full block swap
  - *From: VK (5080 128gb)*

- **Problem:** VRAM spikes during loading
  - **Solution:** 
  - *From: Draken*

- **Problem:** Wrong T5 encoder causing issues
  - **Solution:** Use the 'enc' version of T5 encoder, not the fp8_e4m3fn_scalled version which won't work
  - *From: phazei*

- **Problem:** OOM errors on VAE
  - **Solution:** Use offloading and proper block swap settings to create headroom for VAE processing
  - *From: hicho*

- **Problem:** MultiTalk phonemes going missing
  - **Solution:** Disable distillation LoRAs, use 30 steps, cfg around 5, and proper MultiTalk cfg values
  - *From: Kijai*

- **Problem:** Florence2 error '_supports_sdpa' attribute missing
  - **Solution:** Downgrade transformers to version 4.49.0, newer versions break compatibility
  - *From: Gateway {Dreaming Computers}*

- **Problem:** Matrix multiplication error in WanVideo Sampler
  - **Solution:** Change transformers version to 4.52, ComfyUI 4.53 causes this issue
  - *From: phazei*

- **Problem:** ImportError for 'dict_to_device' function
  - **Solution:** Kijai forgot to push modified file, update to latest commit
  - *From: Kijai*

- **Problem:** T5 maxing out VRAM with offloading
  - **Solution:** Use CPU mode for T5 encoding instead of offloading to avoid VRAM issues
  - *From: hicho*

- **Problem:** ControlNet model compatibility error with Wan
  - **Solution:** ValueError: Invalid ControlNet model - user seeking correct control net model to use
  - *From: xwsswww*

- **Problem:** Gray background padding issue in first frames
  - **Solution:** Check empty frame level set to 0.50, may be due to mask including grey regions
  - *From: Gateway {Dreaming Computers}*

- **Problem:** First and last frames not matching exactly for looping
  - **Solution:** Use workflow that takes last 15 frames and first 15 frames to generate 30-40 frames between them for better temporal motion
  - *From: gokuvonlange*

- **Problem:** Wan 2.1 LoRAs don't work with 2.2 models
  - **Solution:** 2.2 models are completely new architecture, no backward compatibility with old LoRAs
  - *From: Draken*

- **Problem:** VAE decoding takes long time and high VRAM
  - **Solution:** 22 seconds to decode 124 frames, VAE decode bumps VRAM usage to 31GB
  - *From: Kijai*

- **Problem:** Default example workflow takes 20 minutes on some systems
  - **Solution:** Performance varies significantly by hardware setup
  - *From: Drommer-Kille*

- **Problem:** 5B model runs poorly in fp8 with lots of artifacts
  - **Solution:** Don't use fp8 with 5B, stick to fp16
  - *From: Kijai*

- **Problem:** Never use _fast precision with Wan models
  - **Solution:** Avoid fp8_fast, use regular fp8 or fp16 instead
  - *From: Kijai*

- **Problem:** Poor quality results with 5B
  - **Solution:** 5B needs 720p minimum resolution, lower resolutions produce poor results
  - *From: comfy*

- **Problem:** ComfyUI templates not updating
  - **Solution:** Run 'pip install -U comfyui-workflow-templates' and make sure requirements.txt gets updated
  - *From: multiple users*

- **Problem:** Failed VAE decode after 48 minutes
  - **Solution:** Use Wan 2.1 VAE, not 2.2 VAE for decoding
  - *From: GalaxyTimeMachine*

- **Problem:** CUDA CUBLAS error on 4090
  - **Solution:** No clear solution provided, appears to be ongoing issue
  - *From: ZeusZeus*

- **Problem:** CUDA error: CUBLAS_STATUS_NOT_SUPPORTED with 14B model
  - **Solution:** pip uninstall torch torchvision torchaudio then pip install torch==2.4.1+cu124 torchvision==0.19.1+cu124 torchaudio==2.4.1 --index-url https://download.pytorch.org/whl/cu124
  - *From: ZeusZeus (RTX 4090)*

- **Problem:** Accidental 2x resolution causing slow performance on 5B model
  - **Solution:** Kijai discovered he wasn't scaling dimensions properly with new VAE stride, causing accidental 2x resolution
  - *From: Kijai*

- **Problem:** Resolutions lower than 1280x720 don't work well on 5B
  - **Solution:** Use minimum 1280x720 resolution for 5B model
  - *From: Njb*

- **Problem:** Native ComfyUI templates not showing after update
  - **Solution:** Update frontend specifically with pip install -U comfyui-workflow-templates
  - *From: JohnDopamine*

- **Problem:** Blurry output when using split samplers
  - **Solution:** Must adjust end_at_step parameter to match total steps - if using 4 steps, first sampler should end at step 2, second should start at step 2
  - *From: Juampab12*

- **Problem:** Text encoder compatibility issues
  - **Solution:** Use the scaled text encoder from ComfyUI HuggingFace repo, not the 'enc' version
  - *From: Juan Gea*

- **Problem:** LightX2V producing blurred results
  - **Solution:** Try different rank versions (32 vs 64) and increase strength to 2-3
  - *From: Nekodificador*

- **Problem:** 5B model not working properly
  - **Solution:** Use fp8 loading for 16GB VRAM, but quality may be poor - model still needs work
  - *From: Mikerhinos*

- **Problem:** VACE color shifting
  - **Solution:** Fix coming in a few weeks from VACE team, they need input video/mask/prompt triplets for validation
  - *From: pom*

- **Problem:** Washed out and greyed out video outputs with LightX2V
  - **Solution:** Adjust LoRA strength - use 3 strength for first pass, 1.5 strength for second pass
  - *From: Juampab12*

- **Problem:** OOM errors on second/third generation
  - **Solution:** Restart ComfyUI from scratch between generations
  - *From: Nekodificador*

- **Problem:** Pure noise output images
  - **Solution:** Check step configuration settings
  - *From: Juampab12*

- **Problem:** Excessive VRAM usage with LightX adaptive
  - **Solution:** Use other LightX variants or restart ComfyUI
  - *From: Nekodificador*

- **Problem:** Slow generation times on 3090/4090
  - **Solution:** Use LightX2V LoRA with reduced steps and CFG
  - *From: Juan Gea*

- **Problem:** OOM errors and ComfyUI freezing
  - **Solution:** Use --reserve-vram flag and consider upgrading to 128GB system RAM
  - *From: makeitrad*

- **Problem:** I2V giving key errors with LightX lora
  - **Solution:** 2.2's i2v is ~27gb like 2.1's t2v, no ~32gb model anymore, so i2v trained loras from 2.1 will get key errors
  - *From: JohnDopamine*

- **Problem:** Poor face quality with 5B model
  - **Solution:** Multiple users report 5B model produces inferior faces compared to 1.3B, may need specific workflow adjustments
  - *From: DiXiao*

- **Problem:** First frame flash issues
  - **Solution:** Issue occurs with 121 frames, possibly related to LightX lora. Using 81 frames or FastWAN lora helps
  - *From: Kijai*

- **Problem:** CUDA error with CUBLAS_STATUS_NOT_SUPPORTED
  - **Solution:** Could be issue with videocombine preview node, latest UI broke that functionality
  - *From: JohnDopamine*

- **Problem:** Low noise model by itself looks washed out
  - **Solution:** Use both high and low noise models together as intended
  - *From: Ablejones*

- **Problem:** LightX2V doesn't work properly with 2.2 models
  - **Solution:** LightX2V needs to be retrained for both new models to give good results
  - *From: aikitoria*

- **Problem:** First sampler showing only noise in preview
  - **Solution:** This is expected behavior - generation is unfinished after first sampler, second sampler removes remaining noise
  - *From: mamad8*

- **Problem:** ComfyUI org fp8 scaled models don't work in wrapper
  - **Solution:** Use Kijai's fp8 scaled versions instead from his HuggingFace repo
  - *From: Kijai*

- **Problem:** Getting slow motion results
  - **Solution:** May be caused by LightX2V affecting motion, try without it
  - *From: Juan Gea*

- **Problem:** Block error with I2V on wrapper
  - **Solution:** Kijai pushed update that should allow I2V to load
  - *From: Kijai*

- **Problem:** Memory management issues on Windows
  - **Solution:** Use --reserve-vram 2 argument to fix memory management issues
  - *From: Nekodificador*

- **Problem:** OOM on second wrapper sampler pass
  - **Solution:** Try disabling non-blocking in block swap, increase swap file size, or use larger swap
  - *From: Kijai*

- **Problem:** I2V A14B GGUF conversion issues
  - **Solution:** GGUF converter didn't account for image layers, causing channel mismatch errors
  - *From: Draken*

- **Problem:** No previews on wrapper samplers
  - **Solution:** Frontend update killed TAESD previews, use Latent2RGB instead
  - *From: Cubey*

- **Problem:** Faded/washed out colors in I2V
  - **Solution:** Issue with color saturation, avoid shift value of 2 as it's very bad
  - *From: GOD_IS_A_LIE*

- **Problem:** FP8 type not supported on 3090
  - **Solution:** Don't use torch compile with e4m3fn, could use e5m2 instead
  - *From: Kijai*

- **Problem:** Black output with Wan 2.2 wrapper
  - **Solution:** Issue with ComfyUI scaled fp8 model, use alternative fp8 model from Kijai's repo
  - *From: Kijai*

- **Problem:** Shared memory consumption with 40GB RAM
  - **Solution:** Disable non-blocking transfers if using block swap
  - *From: Kijai*

- **Problem:** OOM when increasing frame count
  - **Solution:** Recent ComfyUI update fixed shared memory issue, requeue now corrects itself
  - *From: Piblarg*

- **Problem:** T5 encoder very slow on bf16
  - **Solution:** Use fp32 instead on older GPUs that don't support bf16 properly, or use native text encoding
  - *From: hicho*

- **Problem:** Decoloration at start with 121 frames
  - **Solution:** Fixed by correcting model configuration in workflow
  - *From: PATATAJEC*

- **Problem:** Black screen outputs with I2V workflow
  - **Solution:** Use scaled models from Kijai repo - scaled models from comfy org don't work on wrapper yet
  - *From: mamad8*

- **Problem:** Tensor size mismatch with VAE
  - **Solution:** Switch to Kijai's scaled fp8 models instead of comfy-org models
  - *From: crinklypaper*

- **Problem:** Text encoder loading takes 8 minutes
  - **Solution:** Change text encoder node from CPU to GPU - was set to CPU by default in workflow
  - *From: mamad8*

- **Problem:** Wrapper not switching models on subsequent runs
  - **Solution:** Check that split step value hasn't been accidentally changed to negative (ComfyUI mouse events can change values)
  - *From: MysteryShack*

- **Problem:** Getting outputs with color filters (reddish, pinkish, yellowish)
  - **Solution:** May be caused by rare tokens in dataset - check prompt for unusual character names or tokens
  - *From: mamad8*

- **Problem:** Can't use 2.1 LoRAs on 2.2
  - **Solution:** Models are too different - 2.1 LoRAs won't work with 2.2, need to train new ones
  - *From: Kijai*

- **Problem:** Text encoding taking much longer than usual
  - **Solution:** Switch text encoder from CPU to GPU in wrapper settings
  - *From: mamad8*

- **Problem:** Blurry outputs at end of clips
  - **Solution:** Increase steps to 12-30, split at appropriate point, and use CFG 2 on LOW sampler
  - *From: jeffcookio*

- **Problem:** First frame flickering over 81 frames
  - **Solution:** Known issue when going over 81 frames, may need different approach for longer videos
  - *From: MysteryShack*

- **Problem:** Grayed out/washed out I2V results
  - **Solution:** Use same sampler for both passes, increase steps to 12 split at 6, set shift to 5 on both passes
  - *From: Vardogr*

- **Problem:** Distorted outputs in wrapper
  - **Solution:** Make sure to change the start step for part 2 properly, ensure first sampler starts at step 0
  - *From: Zuko*

- **Problem:** System RAM OOM kills on 128GB RAM
  - **Solution:** Use GGUF models or increase swap file, issue occurs even with large RAM amounts
  - *From: 748197775237447781*

- **Problem:** ComfyUI reserve_vram flag ignored on Wan 2.2
  - **Solution:** Flag doesn't work properly with 2.2 VAE, may actually make VRAM usage worse
  - *From: TK_999*

- **Problem:** Black video outputs with T2V
  - **Solution:** Update ComfyUI to fix scaled fp8 issue in wrapper
  - *From: Kijai*

- **Problem:** Blurry dissolve effect with LightX2V
  - **Solution:** Use LCM/simple sampler, CFG 1.0, LoRA strength 2.0, correct start/end steps
  - *From: Jonathan*

- **Problem:** Wrong start/end steps causing issues
  - **Solution:** Match start/end steps to total steps - if using 10 steps, set 0-5 for first pass, 5-10 for second
  - *From: ✧ฅโ๑ↀᆺↀ ๑ใฅ✧PookieNumnums*

- **Problem:** 6-step workflows producing poor results
  - **Solution:** Increase to 12+ steps for better quality, 6 steps only works when barely anything moves
  - *From: jeffcookio*

- **Problem:** Slow motion effect with speed LoRAs
  - **Solution:** Use different LoRA strengths for high/low noise, or try CausVid instead of LightX2V
  - *From: Drommer-Kille*

- **Problem:** Text encoder running on CPU takes 10+ minutes
  - **Solution:** Change text encoder device to GPU in workflow settings
  - *From: Kijai*

- **Problem:** Matrix mismatch errors in workflows
  - **Solution:** Keep resolution in multiples of 64, don't change resolution from original workflow
  - *From: MysteryShack*

- **Problem:** First sampler end step must equal second sampler start step
  - **Solution:** Connect split_step to both end step and start step, or set Split_step to half of Steps number
  - *From: Kijai*

- **Problem:** Preview issues fixed by updating VHS nodes
  - **Solution:** Update VHS nodes to fix preview problems with TAESD
  - *From: Kijai*

- **Problem:** Crystools causing GPU monitoring errors and monitor shutdown
  - **Solution:** Disable crystools to prevent hardware monitoring issues
  - *From: Rainsmellsnice*

- **Problem:** KeyError for blocks.0.cross_attn.k_img.weight
  - **Solution:** Update to latest nightly version of WanVideoWrapper
  - *From: Kijai*

- **Problem:** Crashes when done sampling during VAE decoding
  - **Solution:** Likely out of RAM - try increasing swap size. At that point you have 2x 15GB models + ~10GB text encoder offloaded (in fp8 that's ~40GB RAM)
  - *From: Kijai*

- **Problem:** Garbled/noisy output between stage 1 and 2
  - **Solution:** Make sure your 2 samplers have the same number of steps, and that sampler one starts at step 0 and ends at the half way point, and sampler two starts at the same frame as the other one ends. Check that end step of 1st = start step of 2nd
  - *From: ✧ฅโ๑ↀᆺↀ ๑ใฅ✧PookieNumnums*

- **Problem:** OOM with wrapper but native works
  - **Solution:** Use 2 block swap nodes - one for 1st sampler and other for 2nd sampler. Set TE on CPU and turn on merge in LoRAs. Increase swap file if you have NVME
  - *From: hicho*

- **Problem:** Running out of RAM with 2 models
  - **Solution:** Disable non-blocking on block swap to help with RAM issues
  - *From: Kijai*

- **Problem:** Out of memory errors on second sampler
  - **Solution:** Turn off 'use non-blocking' option and increase disk swap
  - *From: Kijai*

- **Problem:** Channel mismatch error (expected 36 channels, got 32)
  - **Solution:** Something not updated, probably need to update ComfyUI components
  - *From: Kijai*

- **Problem:** VHS preview not displaying in wrapper samplers
  - **Solution:** Update VHS if using latest ComfyUI frontend
  - *From: Kijai*

- **Problem:** CFG scheduler causing memory errors
  - **Solution:** Remove CFG scheduler node as it can cause memory issues and overrides sampler step count
  - *From: Kijai*

- **Problem:** Yellow tint when using low noise model alone
  - **Solution:** Use proper dual sampler setup instead of low noise only
  - *From: Qok*

- **Problem:** Sampler shows video but output is noise
  - **Solution:** Don't connect decode to first sampler, only to final output
  - *From: Kenk*

- **Problem:** Blurriness in generated videos
  - **Solution:** Increase resolution - minimum 720p recommended, 0.8 megapixels worse than 0.4
  - *From: Fictiverse*

- **Problem:** OOM issues with latest wrapper update
  - **Solution:** Reverted commit 234cffb which was loading scaled models in fp16 instead of fp8, doubling VRAM usage
  - *From: fredbliss*

- **Problem:** Start_step parameter showing as empty in old workflows
  - **Solution:** Manually enter 0 as start_step - node shows 0 but is actually empty when clicked
  - *From: OxygenConsumer*

- **Problem:** Model unloading/reloading causing 20-30 minute generation times
  - **Solution:** Use regular fp8 VACE module instead of scaled version to prevent noise in outputs
  - *From: xiaoc*

- **Problem:** Strong saturation/color issues with VACE
  - **Solution:** Remove step on the high noise sampler to improve color matching
  - *From: Sal TK FX*

- **Problem:** Video reversals with 121 frames using lightx
  - **Solution:** lightx can't work well with 121 frames, causing video reversals. Better to use 81 frames or wait for proper 121 frame support
  - *From: N0NSens*

- **Problem:** System RAM OOM with over 100GB committed
  - **Solution:** Issue caused by nonblocking transfers reserving excessive memory. Turn off 'Offload to CPU' to help with OOM
  - *From: Doctor Shotgun*

- **Problem:** VACE error on second sampler execution
  - **Solution:** Model used is not VACE model or doesn't have VACE module loaded
  - *From: Kijai*

- **Problem:** Split step input disconnected when loading workflow before updating
  - **Solution:** Split step should connect to end step of first and start step of second sampler, or reload browser and workflow
  - *From: Kijai*

- **Problem:** System memory OOM with LoRA + 720p x 81f in native ComfyUI
  - **Solution:** Use wrapper which manages RAM better, or enable swap file
  - *From: Doctor Shotgun*

- **Problem:** ComfyUI caching causes excessive RAM usage
  - **Solution:** Kijai deleted LoRA backup to free RAM since wrapper doesn't have hot unmerging anyway
  - *From: Kijai*

- **Problem:** CFG needs actual negative prompt
  - **Solution:** Don't use only NAG (Negative Attention Guidance), provide proper negative prompt for CFG
  - *From: Kijai*

- **Problem:** Value not in list error
  - **Solution:** Update the node pack - usually caused by workflow using newer settings than current node version
  - *From: rryyaann*

- **Problem:** Running out of RAM with Wan 2.2 14B dual model setup
  - **Solution:** Use SaveLatent and LoadLatent nodes to run HIGH and LOW generation separately
  - *From: Mngbg*

- **Problem:** Color bleaching and poor prompt adherence with LightX2V
  - **Solution:** Use strength 3.0 on HIGH and 1.0 on LOW, try the adaptive lightx2v lora variant
  - *From: gokuvonlange*

- **Problem:** Resolution mismatch errors when upscaling between samplers
  - **Solution:** Use proper latent upscale nodes between the two samplers, ensure resolution compatibility
  - *From: SonidosEnArmonía*

- **Problem:** bf16 text encoder not loading
  - **Solution:** Ensure umt5-xxl-enc-bf16.safetensors is in the correct folder, refresh browser, avoid linked folders in new ComfyUI installs
  - *From: SonidosEnArmonía*

- **Problem:** System RAM issues with second sampler not loading in Wan 2.2
  - **Solution:** Use Save/Load Latent nodes workflow to manage memory
  - *From: The Shadow (NYC)*

- **Problem:** Missing vllm-c module preventing LightX2V inference
  - **Solution:** Affects both gradio inference and ComfyUI nodes, user planning to retry
  - *From: hicho*

- **Problem:** Weird snow artifacts when high noise/low noise balance is wrong
  - **Solution:** Adjust balance between high and low noise models, try different sampler/scheduler
  - *From: Ablejones*

- **Problem:** I2V immediately changing to another image then doing prompt
  - **Solution:** User directed to NSFW channel for troubleshooting
  - *From: 273183253207318530*

- **Problem:** Snow artifacts in vid2vid
  - **Solution:** Not specified in detail, user asking for solutions
  - *From: xwsswww*

- **Problem:** OOMing mid-generation with wrapper
  - **Solution:** Memory fix pushed for I2V on 5B model
  - *From: comfy*

- **Problem:** Can't find Wan2_2_VAE_bf16.safetensors
  - **Solution:** Use wan2.2_vae.safetensors from Comfy-Org repo instead
  - *From: DiXiao*

- **Problem:** name 'Wan22' is not defined error
  - **Solution:** Update ComfyUI
  - *From: TK_999*

- **Problem:** Model trying to loop at >81 frames
  - **Solution:** Don't use LightX for now, proper LoRA not available yet
  - *From: N0NSens*

- **Problem:** OOM errors when using Wan 2.2
  - **Solution:** Use block swap node with 40 blocks, disable non_blocking, or use lower quantization like Q4 instead of Q8
  - *From: VK (5080 128gb)*

- **Problem:** Comfy crashing with OOM instead of just running out of memory
  - **Solution:** Disable 'non_blocking' on block swap node to see where OOM actually happened
  - *From: Daflon*

- **Problem:** Models loading sequentially instead of simultaneously
  - **Solution:** Check if hitting RAM limits rather than VRAM limits
  - *From: phazei*

- **Problem:** Black videos when using Wan 2.2 + VACE
  - **Solution:** Update CUDA and PyTorch, check xformers installation
  - *From: SpacelessTuna*

- **Problem:** ComfyUI manager not showing WanVideoWrapper needs updating
  - **Solution:** Node needs latest/nightly version, manager may show outdated version
  - *From: GalaxyTimeMachine (RTX4090)*

- **Problem:** Low noise sample not following prompt in Wan 2.2
  - **Solution:** Check if using Chinese negative prompt that contains words conflicting with desired style
  - *From: Jackie*

- **Problem:** Color degradation by end of video in FFLF workflow
  - **Solution:** Adjust denoise settings - more steps make it look more like source video
  - *From: art13.beck*

- **Problem:** Comfy shutdown when trying to VAE decode
  - **Solution:** No solution provided, user reports shutdown with loaded Wan VAE
  - *From: 🐝 bumblebee 🐝*

- **Problem:** Seed not working/generating same videos
  - **Solution:** Check if add_noise is disabled on sampler, disable LoRAs one by one to isolate issue
  - *From: Kijai*

- **Problem:** Different contrast and texture for first few frames
  - **Solution:** 14B model is not 121 frames, anything past 81 can cause various issues like that
  - *From: Kijai*

- **Problem:** OOM on second generation
  - **Solution:** Use --reserve-vram 2 arg or give more vram using block swap
  - *From: hicho*

- **Problem:** Extremely noisy output when keeping distill on low pass and running 15 steps on high
  - **Solution:** Use more than 3 steps on HighNoise model if not using distill lora
  - *From: DawnII*

- **Problem:** Color shift ruining loop videos
  - **Solution:** Not resolved in chat
  - *From: Yae*

- **Problem:** Native workflow not matching wrapper results
  - **Solution:** Could be related to lora application being unmerged - same values don't transfer unmerged
  - *From: DawnII*

- **Problem:** Slowmo issues with lightxv2 lora
  - **Solution:** Try increasing strength to 3.5 on HIGH and 1.0 on LOW, or use higher CFG values
  - *From: gokuvonlange*

- **Problem:** Significant anatomical warping without NAG at low CFG
  - **Solution:** Always use NAG (Negative Augmented Generation) with CFG 1, especially on high noise model
  - *From: Ant*

- **Problem:** Jibmix decode image has grid overlay
  - **Solution:** Use WanVideo Decode node instead of native VAE decode node
  - *From: jeffcookio*

- **Problem:** First person POV being ignored in prompts
  - **Solution:** Use explicit terms like 'first-person view', include visible body elements, match camera movement to motion
  - *From: The Shadow (NYC)*

- **Problem:** Getting random strings, bubbles and garbage in outputs
  - **Solution:** Usually caused by wrong 2-sampler setup - check that split step node is connected properly. Also avoid using 'enhance a video' node and keep denoise at 1.0
  - *From: Kijai*

- **Problem:** Split step node disconnected after update
  - **Solution:** Refresh browser after updating before loading workflows, otherwise new widgets load incorrectly
  - *From: Kijai*

- **Problem:** Dark frames at start of video
  - **Solution:** Usually happens when using frame count other than 81 frames
  - *From: Kijai*

- **Problem:** Sampler won't do more than 5 steps
  - **Solution:** Both samplers need to have the same total steps value for sigma schedule to match properly
  - *From: zelgo_*

- **Problem:** Black video output when using 2.2 with wrapper
  - **Solution:** Use Kijai's models from HuggingFace instead of ComfyUI models
  - *From: crinklypaper*

- **Problem:** TypeError 'NoneType' object is not iterable with wrapper
  - **Solution:** Update wrapper nodes and use correct model paths
  - *From: VRGameDevGirl84*

- **Problem:** OOM errors with 121 frames on Wan 2.2
  - **Solution:** Use 81 frames or rent cloud GPU with more VRAM
  - *From: xwsswww*

- **Problem:** Blurry and washed out videos with consolidated model
  - **Solution:** Remove the problematic node causing the issue
  - *From: Simjedi*

- **Problem:** Snow particles appearing in generated videos
  - **Solution:** Remove Film grain node or use LCM sampler for high noise stage
  - *From: xwsswww*

- **Problem:** Set LoRA node error about low_mem_load
  - **Solution:** Disable low_mem_load and merge_loras in the LoRA select node
  - *From: xwsswww*

- **Problem:** SageAttention causing crashes
  - **Solution:** Remove SageAttention from ComfyUI or find alternative
  - *From: shockgun*

- **Problem:** Xformers crash with CUDA error
  - **Solution:** Upgrade xformers or disable it entirely
  - *From: trax*

- **Problem:** Wan 2.2 14B GGUF not generating after first ksampler
  - **Solution:** Check python version (3.12), torch (2.71), and sage attention (2.2) setup
  - *From: Abx*

- **Problem:** Blurry/washed out results
  - **Solution:** Use higher resolution (above 600), avoid too low resolutions like 640x528
  - *From: VK (5080 128gb)*

- **Problem:** Preview method causing issues
  - **Solution:** Change preview method from TAESD to fix sampling problems
  - *From: thaakeno*

- **Problem:** 'blocks.0.cross_attn.k_img.weight' KeyError
  - **Solution:** Update nodes - likely using outdated version or conflicting fork
  - *From: Kijai*

- **Problem:** Conflicts showing in ComfyUI Manager for WanVideoWrapper
  - **Solution:** Clean reinstall of nodes, conflicts may be from other forks like MultiTalk
  - *From: Kijai*

- **Problem:** IndexError: index 0 is out of bounds for dimension 0 with size 0
  - **Solution:** Set denoise to 1.0, increase start step on first sampler and enable add_noise
  - *From: Kijai*

- **Problem:** Error with denoise below 0.5
  - **Solution:** Keep denoise at 0.5 or higher to avoid errors
  - *From: Flipping Sigmas*

- **Problem:** TorchCompileModelWanVideo2 not working on RTX 3090
  - **Solution:** Use GGUF, fp16, or e5m2 scaled weights instead of fp8_e4m3fn which doesn't work with torch compile on 3000 series
  - *From: Kijai*

- **Problem:** Noise particles/snowflakes in output
  - **Solution:** Avoid increasing CFG on sampler 1 and dropping lightx LoRA - try different samplers
  - *From: Quality_Control*

- **Problem:** VAE resolution mismatch in V2V workflow
  - **Solution:** Use correct VAE - 5B VAE is only for 5B model, need different VAE for 14B
  - *From: Kijai*

- **Problem:** FP8 models not working with TorchCompile
  - **Solution:** Disable TorchCompile Node when using fp8 models
  - *From: Ashtar*

- **Problem:** taew2_1.safetensors not found in extra paths
  - **Solution:** Either move file to install folder or update nodes to respect extra paths
  - *From: Kijai*

- **Problem:** Long generation times on 3060 12GB
  - **Solution:** Don't use 121 frames - causes memory issues and doesn't work well, use shorter frame counts
  - *From: N0NSens*

- **Problem:** Lora not detected errors
  - **Solution:** Some keys not detected by certain models but important keys still load, can ignore these errors
  - *From: DawnII*

- **Problem:** Context windows causing errors with I2V
  - **Solution:** Context implementation not fully done for I2V, use | separation in latest commit
  - *From: Kijai*

- **Problem:** Double rendering/overlapping generations in I2V
  - **Solution:** Unclear - user reported issue with lightx2v_T2V and FastWan_T2V loras at guidance 1, shift 5 but no clear solution provided
  - *From: davids0025*

- **Problem:** TAESD preview failing after git pull
  - **Solution:** Frontend refresh fixed it. Also need to update VHS if it breaks
  - *From: DawnII*

- **Problem:** Context settings causing ComfyUI crashes
  - **Solution:** Updated with safety check function that errors out instead of crashing when context settings are invalid
  - *From: Kijai*

- **Problem:** LightX2V lora giving blurry results
  - **Solution:** Check that second sampler start step is correct (user had it at step 10 when should be different)
  - *From: jxy1k*

- **Problem:** Decode-merge-encode breaking in upscale workflow
  - **Solution:** Need 'return_leftover_noise' functionality which isn't available without changing node codes
  - *From: Juampab12*

- **Problem:** Can't use low mem or merge loras with Set loras node
  - **Solution:** Two issues: nodes not up to date (typo indicates this) and you can't use low mem or merge loras with the Set loras node
  - *From: Kijai*

- **Problem:** Tiny VAE not loading in tiny vae loader
  - **Solution:** Save tiny vae to /models/vae_approx folder, not regular vae folder
  - *From: Kijai*

- **Problem:** Denoise < 1.0 confusion with native samplers
  - **Solution:** Stop thinking about denoise and just use start/end steps instead. Use nodes like 'Inject noise to latent' and intercept latent between samplers
  - *From: Juampab12*

- **Problem:** 5B model destroying faces in LoRA training
  - **Solution:** Switch to FusionX GGUF - faces are ok and don't get destroyed, face keeps consistent for 3 seconds
  - *From: Drommer-Kille*

- **Problem:** Workflow not loading from PNG
  - **Solution:** Don't download webp, open image then save it. If using browser discord, download the app instead
  - *From: Kenk*

- **Problem:** 'TAEHV' object has no attribute 'encode' error
  - **Solution:** TAEW support not added to image encode node, shouldn't be used for single image encoding anyway
  - *From: Kijai*

- **Problem:** Loop detected error with cg-use-everywhere extension
  - **Solution:** Check for conflicts in custom node manager or disable cg-use-everywhere extension
  - *From: thaakeno*

- **Problem:** Start_step INT conversion error in VACE
  - **Solution:** Delete the start step value and type 0 again, even if it shows the same number
  - *From: Daflon*

- **Problem:** Tiled VAE error in v2v workflows
  - **Solution:** Issue was fixed by Kijai in recent update
  - *From: Kijai*

- **Problem:** 'NoneType' object is not iterable with CFG float list
  - **Solution:** Use regular text embed node instead of NAG when using CFG. NAG requires 3 prompts, not negative prompt
  - *From: Kijai*

- **Problem:** Memory issues with low noise pass
  - **Solution:** Disable non blocking, use unmerged loras
  - *From: Kijai*

- **Problem:** RAM hitting max during low pass
  - **Solution:** Use disk cache and disable T5 loader after first run to save ~10GB RAM
  - *From: Kijai*

- **Problem:** Multitalk not working with 2.2
  - **Solution:** Only works with low noise model, not high noise model
  - *From: Kijai*

- **Problem:** OOM with color match on longer videos
  - **Solution:** KJnodes matcher works but is super slow as alternative
  - *From: lostintranslation*

- **Problem:** CGF 0 produces gore content
  - **Solution:** Never use CFG 0, caused unwanted violent content
  - *From: hicho*


## Model Comparisons

- **LightX2V at 0.7 vs 1.0 strength**
  - 0.7 strength much better motion than full strength, but some fast moving videos had bad trails
  - *From: TK_999*

- **High Speed Dynamic (HSD) vs MPS/AccVid/HPS loras**
  - HSD provides huge improvement in motion without degrading colors or detail like AccVid and HPS does. Better improvement over MPS lora for fixing lightx2v's motion degradation
  - *From: Jonathan*

- **FusionX vs LightX optimized settings**
  - LightX with proper settings (no AccVid, increased moviigen and mps) produces results very close if not on par with fusionX outputs
  - *From: VRGameDevGirl84(RTX 5090)*

- **Stock ComfyUI WAN workflow vs modified Civitai workflow**
  - Getting MUCH faster generations with stock comfyui WAN example workflow compared to modified Civitai workflow
  - *From: Vardogr*

- **SAGEATT 1 on vs off on RTX 2060**
  - Noticeable speed improvement, can run on older GPUs unlike SAGEATT 2
  - *From: hicho*

- **fp16 vs fp8 performance difference**
  - Not huge difference, noticeable but not night and day
  - *From: Kijai*

- **Native vs Wrapper speed**
  - Native is slow compared to wrapper
  - *From: VRGameDevGirl84(RTX 5090)*

- **ThinkSound vs MMAudio**
  - ThinkSound is a lot better than MMAudio
  - *From: yi*

- **fp16 vs fp8 model quality**
  - fp8 is just as good as fp16
  - *From: VRGameDevGirl84(RTX 5090)*

- **4 steps vs 12 steps with LightX2V**
  - 12 steps shows more secondary motion
  - *From: Todd*

- **Wan vs Skyreels quality**
  - Never got good quality results with Skyreels
  - *From: VRGameDevGirl84(RTX 5090)*

- **VACE depth vs MultiTalk competition**
  - They seem to be competing - depth with VACE already captures lip movement well
  - *From: amli*

- **WAN T2V vs Flux vs Krea for image generation**
  - WAN produces good results with less plastic/shiny skin appearance than Flux, comparable quality
  - *From: VRGameDevGirl84(RTX 5090)*

- **Different schedulers for WAN T2V**
  - DPM++ Beta and UniPC produce good results for image generation
  - *From: Colin*

- **SeedVR2 VideoUpscaler quality**
  - Not that good, high VRAM requirements make it not worth the trouble
  - *From: slmonker(5090D 32GB)*

- **Wan vs Skyreels for text-to-image**
  - Skyreels produces more photorealistic results, Wan produces good stylized results
  - *From: VRGameDevGirl84(RTX 5090)*

- **With vs without vintage LoRA on same seed/prompt**
  - Dramatic difference in quality and style with LoRA applied
  - *From: VRGameDevGirl84(RTX 5090)*

- **1.3B vs 14B model for single frame**
  - 1.3B produces decent results in 17 seconds with 25 steps, quality comparable to 1.5 SD models
  - *From: VRGameDevGirl84(RTX 5090)*

- **1.3B vs 14B for upscaling**
  - I think 1.3B is more suited for upscales... the quality is insane for 1.3b
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Self-forcing LoRA quality vs regular 14B**
  - Getting decent quality output now and it's silly fast, but scale of motion seems to be much lower than my old workflow without self force
  - *From: lostintranslation*

- **MAGREF vs Phantom for I2V accuracy**
  - MAGREF GGUF much better for accuracy, perfect match vs Phantom failing
  - *From: mdkb*

- **VACE vs Kontext for one-frame operations**
  - VACE is like Kontext but much better
  - *From: hicho*

- **Zonos vs Chatterbox for TTS**
  - Zonos handles accents better, has emotion sliders for more control, but Chatterbox gets things right more often first time
  - *From: blake37*

- **VACE vs FloweEdit for inpainting**
  - VACE mostly supersedes FloweEdit according to community knowledge
  - *From: mdkb*

- **Fusion VACE GGUF vs standard VACE**
  - User prefers adding individual fusion loras for more control rather than full fusion model
  - *From: mdkb*

- **Draw Things vs ComfyUI for VACE**
  - Draw Things uses 26GB RAM vs 110GB in ComfyUI for same video, and is 30% faster
  - *From: Todd*

- **4090 offloading to RAM vs Mac unified memory**
  - 4090 with RAM offloading is multiple times faster than Mac unified memory
  - *From: Kijai*

- **LightX2V vs AccVid distill**
  - LightX2V keeps what the model can do, unlike AccVid. Can't use AccVid with LightX for T2V as it does bad things
  - *From: Kijai*

- **Context windows vs Uni3c for character animation**
  - Without Uni3c you can get much more expressive characters, but Uni3c provides stable and continuous results
  - *From: Kijai*

- **Euler/simple vs LCM/ddim_uniform schedulers**
  - LCM/ddim_uniform produces much better results with LightX2V distill - the difference is stark
  - *From: Screeb*

- **ddim_uniform vs euler/simple schedulers**
  - ddim_uniform provides more varied compositions and better prompt adherence, euler/simple produces samey, cliche results but with higher contrast detail
  - *From: Screeb*

- **Wan vs Flux image generation**
  - Wan is faster (6s vs 17s) and makes Flux look 'poopy' especially for hands and faces at 1920x1072
  - *From: Colin*

- **MagRef vs Phantom for reference adherence**
  - MagRef better at sticking to exact reference images, Phantom more flexible but does what it wants
  - *From: mdkb*

- **MultiTalk vs Phantom for movement**
  - Phantom has more dynamic movement and exciting scenes, MultiTalk has people 'planted' but better lip sync
  - *From: AJO*

- **Magref vs Phantom for likeness**
  - Magref better for likeness/consistency, can handle 3 images well
  - *From: mdkb*

- **Euler vs UniPC samplers**
  - Euler most consistently pleasing, very subjective choice
  - *From: David Snow*

- **LightX2V vs CausVid for artifacts**
  - Switching from LightX2V to CausVid eliminates snow artifacts
  - *From: ingi // SYSTMS*

- **GGUF vs fp8 speed**
  - GGUF is quite a bit slower than fp8
  - *From: Kijai*

- **E4 vs E5 precision**
  - E4 is smaller in range but more precise than E5
  - *From: ˗ˏˋ⚡ˎˊ-*

- **GGUF Q6 vs fp8 quality and speed**
  - Q6 little bit slower and image quality quite a few bit lower
  - *From: slmonker(5090D 32GB)*

- **Wrapper vs Native output quality**
  - After comparing for hours, wrapper output looks about the same or slightly better
  - *From: David Snow*

- **GGUF Q8 vs fp8 downcast**
  - Q8 GGUF is far better quality than fp8 downcast, but 20% slower due to dequantization overhead
  - *From: Kijai*

- **Gradio app vs ComfyUI results**
  - Gradio app produces better results out of the box, appears more optimized especially for VACE model
  - *From: hicho*

- **Wan vs HiDream for fashion**
  - Wan might be better than HiDream for certain use cases
  - *From: Nekodificador*

- **Wan vs Flux for realism**
  - Wan is much better than Flux in realism
  - *From: Siraj*

- **4 steps vs 6 steps**
  - 6 step output looks a bit unnatural compared to 4 steps
  - *From: David Snow*

- **Q8 GGUF vs fp8**
  - Q8 is better quality than fp8, about same size, but GGUF is always about 20% slower
  - *From: Kijai*

- **Q6 GGUF vs fp8**
  - Q6 is very comparable to fp8 quality
  - *From: Kijai*

- **Skyreels vs standard models**
  - Skyreels is better for human-centric content, works well with WAN LoRAs
  - *From: VRGameDevGirl84*

- **LightX2V vs CausVid**
  - LightX2V is better version of CausVid and can be substituted with strength 1.0 at 5 steps
  - *From: MilesCorban*

- **Dedicated image models vs video models for image generation**
  - Dedicated image models better for image outputs as video models encode motion in latents
  - *From: Clownshark Batwing*

- **DrawThings vs MLX on Mac**
  - DrawThings 30% faster and uses less memory (26GB vs 110GB) than native MLX implementations
  - *From: Todd*

- **VACE I2V vs classic I2V**
  - VACE allows for editing capabilities and controlnet functionality that's harder to achieve in standard I2V
  - *From: hicho*

- **FusionX vs ingredients workflow with LightX2V**
  - FusionX still better overall - LightX2V ingredients workflow has motion issues and prompt adherence problems
  - *From: MysteryShack*

- **Native vs wrapper for GGUF models**
  - Native works fine with GGUF, wrapper has issues with some lora combinations
  - *From: mdkb*

- **AccVid performance with different models**
  - AccVid works well for I2V and helps, but doesn't work well with T2V
  - *From: VRGameDevGirl84*

- **VACE vs other WAN models**
  - VACE produces 'dull' and flat video on its own, needs booster LoRAs. WAN i2v/t2v/fun models animate reference directly instead of treating as embed
  - *From: Grimm1111*

- **Quality LoRA effects**
  - Higher LoRA strength affects faces making them look 'flux like' and AI, but adds pop and realism. MPS creates snow-like flickery noise if too high
  - *From: Grimm1111*

- **AniSora vs AniWan**
  - AniSora needs time to cook for V3, AniWan currently performs better in tests
  - *From: DevouredBeef*

- **GGUF vs SFT model for LoRA loading**
  - GGUF has faster LoRA loading while SFT model is slow with LoRA loading
  - *From: hicho*

- **3B FP8 vs 3B FP16 for SeedVR2**
  - Don't use FP8 model - it's heavier than FP16 because it gets converted to bf16
  - *From: Adrien Toupet*

- **Wan vs Flux for character LoRA adherence**
  - Wan consistency in training is 'insane' and 'miles better than Flux' for character LoRA adherence
  - *From: Dream Making*

- **I2V vs T2V motion generation with distilled models**
  - Distilled models on I2V generally produce less motion compared to T2V, but not always
  - *From: Kijai*

- **Wan 2.1 upscaling vs AnimateDiff**
  - Way way better than AnimateDiff
  - *From: xwsswww*

- **5090 vs 4090 performance**
  - 5090 is 60-80% faster than 4090 for most things tested plus added VRAM is great
  - *From: A.I.Warper*

- **Topaz vs GIMM and RIFE upscaling**
  - Topaz kicks their ass for upscaling quality
  - *From: mdkb*

- **Wan vs Hunyuan for T2I rollercoaster scene**
  - Hunyuan performed better for realistic person on rollercoaster scene
  - *From: JohnDopamine*

- **720p models vs lower resolution models**
  - 720p models generate worse than lower-resolution models
  - *From: JohnDopamine*

- **Wan 1.3B vs LTX for speed**
  - Wan 1.3B with LoRA better than LTX, LTX 0.96 8 step vs Wan 1.3B VACE T2V with CausVid LoRA 4 steps
  - *From: shockgun*

- **SDXL ControlNets vs other precision methods**
  - Nothing beats SDXL controlnets in precision
  - *From: Kijai*

- **Wan T2I vs Flux**
  - Wan T2I better than Flux
  - *From: shockgun*

- **Wan 2.1 vs AnimateDiff**
  - Wan 2.1 way better results, deleting AnimateDiff models
  - *From: xwsswww*

- **LightX vs CausVid for VACE**
  - 14B uses lightx2v not causvid, 1.3B VACE uses causvid
  - *From: mdkb*

- **SeedVR2 vs TensorRT**
  - SeedVR2 takes longer and uses more VRAM but may add more details
  - *From: Gill Bastar*

- **HunyuanVideo vs Wan for face likeness**
  - HunyuanVideo holds look better than Wan
  - *From: mdkb*

- **Q8_0 vs Q4KM quantization**
  - Both mentioned as working options for different use cases
  - *From: mdkb*

- **PUSA 10 steps vs WAN 2.1 50 steps vs WAN LightX 4 steps**
  - PUSA 10 step is 5x faster than WAN 2.1 50 step, but WAN LightX runs in 4 steps
  - *From: shockgun*

- **Rank64 vs Rank32 LoRA comparison**
  - Visual comparison showed minimal differences between rank64 and rank32 versions
  - *From: slmonker(5090D 32GB)*

- **480p vs 720p models**
  - Some claim 480p does better job than 720p, but opinions vary. 720p trained on higher res data
  - *From: Hashu*

- **New I2V LoRA vs old T2V LoRA**
  - New I2V LoRA much better for motion and prompt following
  - *From: Ada*

- **480p vs 720p model**
  - 480p preferred by most users, no perceptible quality difference at higher resolutions
  - *From: multiple users*

- **R16 T2V lightx vs new lightx2v**
  - R16 still better for VACE/Phantom at 0.7, 1 and 1.3 strength
  - *From: DawnII*

- **Wan vs Skyreels**
  - Wan model consistently beats Skyreels in testing despite Skyreels being more 'cinematic'
  - *From: mdkb*

- **LightX2V v1 vs v2**
  - v2 has more motion, less burning, better prompt adherence, but may sacrifice some fine detail quality
  - *From: multiple users*

- **Different LightX2V ranks for image generation**
  - Rank 4 and 8 clearly inferior, only after rank 16 comparable to v1, things change significantly after rank 32
  - *From: patientx*

- **2 steps vs 4 steps with new LightX2V**
  - 2 steps pretty bad, 4 minimum recommended. Initially seemed new one might need more steps due to added motion
  - *From: Kijai*

- **PUSA vs Wan I2V**
  - PUSA obtains VBench-I2V score of 87.32% vs Wan-I2V's 86.86% - not a lot of improvement
  - *From: Siraj*

- **MAGREF vs VACE vs Phantom for face likeness**
  - MAGREF achieves 95% likeness (best), Phantom 80%, VACE only 60%, but MAGREF is 480p model with different prompt adherence
  - *From: gokuvonlange*

- **Pusa LoRA motion vs standard Wan**
  - Pusa creates much more natural, alive-looking motion but with some quality tradeoffs
  - *From: ZeusZeus (RTX 4090)*

- **LightX2V rank 64 vs other ranks**
  - Rank 64 was most popular choice throughout the day, though rank 128 is slightly better for accuracy
  - *From: Ada*

- **Euler/bong_tangent vs LCM/Beta samplers**
  - Both work well with LightX2V, LCM/Beta allows down to 4 steps
  - *From: garbus*

- **Pusa vs Hunyuan I2V**
  - Pusa i2v results remind of failed HunyuanVideo I2V with flash and flicker during first frame
  - *From: JohnDopamine*

- **Pusa at strength 1.0 vs 1.3**
  - At 1.0 strength too weak to keep first frame likeness
  - *From: Kijai*

- **Lightx2v vs other distillation**
  - Lightx is just insanely good, don't think any distill will outdo it
  - *From: Draken*

- **Pusa beats Hunyuan i2v**
  - At least beats hunyuan i2v
  - *From: Kijai*

- **AccVid vs LightX2V LoRA**
  - LightX2V preferred - AccVid has too much of its own style
  - *From: Kijai*

- **Pusa vs regular I2V for handshake generation**
  - Regular I2V models better for specific character interactions
  - *From: David Snow*

- **Standard vs radial attention quality**
  - Quality hit with radial but can rerun for better quality if needed
  - *From: Kijai*

- **PUSA vs LightX2V for I2V**
  - Getting better results with I2V + LightXv2 than T2V + PUSA. PUSA workflow shows flashing especially when intercalating frames
  - *From: Juan Gea*

- **Without PUSA vs With PUSA for T2V**
  - Without PUSA looks better for some use cases
  - *From: el marzocco*

- **Sage vs Radial attention performance**
  - 768x384 350 frames: Sage takes 344 seconds, Radial takes 361 seconds. At 5090 1280x768: Sage 15.15s/it vs Radial 10.92s/it for 3/4 steps
  - *From: slmonker, Kijai*

- **LightX rank 64 vs rank 128**
  - Higher rank shows obvious improvement in quality and clarity, lower rank has cinematic personality but with weirdness
  - *From: The Shadow (NYC), Atlas*

- **LightX2V rank 256 vs 128 vs 64**
  - 128 shows significantly faster motion than 64, 256 shows marginal improvement over 128 for specific use cases
  - *From: A.I.Warper*

- **GGUF vs FP8 models**
  - GGUF ~20% slower but uses less VRAM, each LoRA added slows it more since applied on-the-fly
  - *From: Kijai*

- **Ampere vs Blackwell speed gains**
  - 5090 gets 50% speed boost with radial attention, Ampere cards see limited improvement
  - *From: MysteryShack*

- **New LightX2V vs old LightX**
  - New version is sometimes too fast/speedy for scenes with humans or animals, requires trial and error
  - *From: JohnDopamine/Gill Bastar*

- **VACE vs Phantom references**
  - Phantom references are better, VACE tries to use references in similar position but not exact
  - *From: Piblarg*

- **GGUF vs FP8 efficiency**
  - GGUF is slower in general, biggest benefit is RAM saved, not always the answer for speed
  - *From: Kijai*

- **LightX2V vs other distilled LoRAs**
  - LightX2V v2 gives better results than v1, both quality and movement improvements
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Flux vs WAN for outpainting**
  - Flux fill/outpaint then fed to WAN is better than using WAN directly for outpainting from 9x16 to 16x9
  - *From: ˗ˏˋ⚡ˎˊ-*

- **PUSA LoRA quality vs motion trade-off**
  - PUSA LoRA reduces motion because it tries to fit reference but you can lower strength to balance reference matching vs motion
  - *From: Hashu*

- **PUSA + LightX vs LightX alone**
  - PUSA dramatically improves style retention and likeness to input image
  - *From: A.I.Warper*

- **Phantom vs base WAN/VACE for movement**
  - Phantom loses too much movement compared to base wan/vace but beats pure vace for reference matching
  - *From: Hashu*

- **VACE vs Phantom+VACE**
  - Pure VACE has better motion, Phantom kills some of the nice motion but provides better reference matching
  - *From: Hashu*

- **MultiTalk performance: fp8 vs q6 GGUF**
  - fp8 takes 3-4 minutes, q6 GGUF takes 6-7 minutes
  - *From: Draken*

- **SeedVR2 vs other upscalers**
  - SeedVR2 performs best but is very resource heavy even on RTX 5090
  - *From: orabazes*

- **Skyreels vs vanilla Wan**
  - Skyreels can do 121 frames vs 81, allows 24fps generation
  - *From: N0NSens*

- **FP16/32 vs FP8 models**
  - Surprisingly big quality difference, especially for upscaling
  - *From: Kijai*

- **PUSA i2v vs t2v modes**
  - Effect is noticeably less in i2v workflows compared to t2v generation
  - *From: Дмитрий Марков*

- **Fun Control vs VACE reference adherence**
  - Fun reference adherence not as reliable as VACE, but Fun Control sticks to control better than VACE
  - *From: trax/Hashu*

- **fp8_scaled vs normal fp8**
  - fp8_scaled feels a little too different, varies more than expected. Normal fp8 may be better
  - *From: Hashu*

- **Merged vs unmerged LoRA performance**
  - Unmerged is slower per iteration (4.7s/it vs 6.5s/it for 32 frames) but saves 30-60 seconds of loading time
  - *From: phazei*

- **Native vs Wrapper GGUF VRAM usage**
  - Native offloads automatically, in wrapper you set it yourself. With chunked rope wrapper uses less than native
  - *From: Kijai*

- **Wrapper vs Native VRAM efficiency**
  - Native nodes seemed to be more vram efficient but gets some weird OOM errors
  - *From: Piblarg*

- **FP8 scaled models quality comparison**
  - Q8 GGUF on par with fp8 scaled from full fp32, new fp8_scaled_kj closer to fp16 than comfy's fp8_scaled
  - *From: Kijai*

- **Wrapper vs Native speed**
  - Multiple people say wrapper is slower than native but this may be misinformation
  - *From: samhodge*

- **E4M3FN vs E5M2 for Wan**
  - E4M3FN probably better for Wan since fp16 is better than bf16, indicating precision more important than range
  - *From: Kijai*

- **PUSA vs DiffusionForcing**
  - Very similar functionality - both extend timesteps to frame count and set to 0 for frames to keep, main difference may be cheaper training
  - *From: Kijai*

- **Merged vs unmerged LoRAs**
  - Merged models still preferred - test with LoRAs then merge if using same combination regularly
  - *From: patientx*

- **e5m2_scaled vs e4m3fn_scaled vs regular e5m2**
  - Scaled versions require 10-20% lower LoRA strengths, merged and unmerged results very close with first two
  - *From: patientx*

- **PerpNegGuider vs regular sampler with Phantom**
  - No huge reason found to choose PerpNegGuider over regular sampler in testing
  - *From: Piblarg*

- **UniC3 with/without prompt**
  - With prompt maintains AI effects and character movement, without prompt creates pure 3D space movement but can be boring
  - *From: hicho*

- **Video vs 3D for camera animation**
  - Video output better than 3D source for certain camera movements
  - *From: hicho*

- **Wire vs solid geometry for Uni3C**
  - Solid works better, wire causes backward movement
  - *From: VRGameDevGirl84*

- **MAGREF vs regular I2V for context windows**
  - MAGREF snaps back less, works better for longer videos
  - *From: Kijai*

- **PUSA vs VACE for video extension**
  - PUSA shows way less color shifting than VACE for video extension
  - *From: Hashu*

- **Official LightX2V LoRA vs other versions**
  - Official LightX2V LoRA works identically to other versions - Kijai doublechecked with HuggingFace weights
  - *From: Kijai*

- **Skyreels V2 vs Wan 2.1**
  - Skyreels V2 is same architecture as Wan 2.1 with different aesthetic and 24fps instead of 16fps, requires 50% more compute
  - *From: yi*

- **Scaled model performance with/without LoRA merging**
  - Merged models are still fastest despite new LoRA system being faster than old one
  - *From: patientx*

- **Multiple steps for text generation**
  - 8 steps produces better results than 4 steps for text generation
  - *From: VK (5080 128gb)*

- **FastWan 1.3B vs LTX**
  - FastWan 1.3B is better than LTX for anime/cartoon content
  - *From: Juan Gea*

- **FastWan 1.3B vs self-forcing trained 1.3B**
  - Self-forcing model is better - FastWan models have always been misses
  - *From: Kijai*

- **PUSA vs VACE for extension**
  - PUSA has less color shifting than VACE but more aesthetic quality degradation over time
  - *From: DawnII*

- **WAN 2.2 vs WAN 2.1**
  - 2.2 biggest advantage is RL simplifies prompts - even simple prompts like 'a girl dancing' work well vs strange results in 2.1
  - *From: 青龍聖者@bdsqlsz*

- **GGUF Q4 quality**
  - GGUF Q4 is pretty terrible with Wan, usable with Flux where nunchaku is amazing
  - *From: Kijai*

- **Fast Wan 1.3B vs Wan 14B**
  - 1.3B not as good with hands and fingers, better for anime/cartoon than realistic content
  - *From: Juan Gea*

- **Fast Wan 1.3B vs standard models**
  - 1.3B gives complete human anatomy at higher resolutions like 1024x1536, worse at lower resolutions
  - *From: patientx*

- **LightX2V I2V vs T2V LoRAs**
  - I2V version has less color contrast, T2V version generally preferred for most use cases
  - *From: TheSwoosh*

- **WAN vs VEO3**
  - VEO3 beats WAN in sound and lipsync, but WAN beats VEO3 everywhere else. Cost: VEO3 >>> WAN
  - *From: MysteryShack*

- **WAN vs Runway/Luma for skateboard tricks**
  - WAN successfully follows skateboard tricks in v2v where Runway and Luma both fail
  - *From: Drommer-Kille*

- **WAN vs Chroma for image generation**
  - WAN faster than Chroma - 1024x1536 in 18 sec/it vs Chroma's 1024x1024 in 15-16 sec, plus WAN needs fewer steps
  - *From: patientx*

- **VACE vs FLF for long video generation**
  - VACE more reliable and controllable than First-Last-Frame method, FLF results are choppy with obvious shifts
  - *From: DawnII*

- **SageAttention 3 vs SageAttention 2**
  - Sage3 is faster but uses ~5GB more VRAM. At 720p: sage2 takes 1:45, sage3 with 20 block swap takes 1:38. Useless on low res due to memory overhead
  - *From: Kijai*

- **Radial attention vs SageAttention 3**
  - Radial attn > sage3. Same speed benefits but sage3 has lower quality. They are mutually exclusive
  - *From: Kijai*

- **VACE T2V vs dedicated T2V 14B model**
  - VACE T2V produces inferior results compared to T2V 14B model when doing prompt-only generation. VACE better for inpainting/outpainting/v2v
  - *From: gokuvonlange*

- **FastWan vs LightX2V**
  - FastWan doesn't compare to LightX2V quality, produces less motion
  - *From: Kijai*

- **Wan 2.2 vs 2.1**
  - 2.2 has much better physics than 2.1, more anime-friendly with better 2D style
  - *From: 青龍聖者@bdsqlsz*

- **Radial vs Sage3 attention**
  - Radial attention is more worthwhile than sage3
  - *From: Kijai*

- **1.3B vs 14B model quality**
  - 1.3B is like SD vanilla 1.5 - much lower quality. 14B gets style in 250-500 steps while 1.3B takes much longer
  - *From: Drommer-Kille*

- **DMD vs bidirectional LoRAs**
  - Bidirectional LoRA helps more with transitions, major difference in quality
  - *From: Kijai*

- **EchoShot prompt adherence**
  - Model doesn't follow prompts super strong, especially with VACE
  - *From: Kijai*

- **DG aesthetic vs other models**
  - Very flux-like appearance
  - *From: DawnII*

- **Resolve vs DepthAnything depth maps**
  - Resolve depth is better quality but slower
  - *From: Drommer-Kille*

- **ComfyUI native vs wrapper memory handling**
  - Native has better automated offloading, wrapper benefits more from compile
  - *From: Kijai*

- **Resolve vs ComfyUI AIO depth processing**
  - Resolve v20 takes 1s without noise vs ComfyUI AIO 2min with noise
  - *From: Drommer-Kille*

- **Q5 model quality**
  - Q5 is terrible quality
  - *From: Kijai*

- **1.3B vs CogVideoX 2B**
  - Wan 1.3B is better than CogVideoX 2B
  - *From: VK*

- **Full blocks vs partial blocks**
  - Full block swap was key for higher resolutions, allows better VRAM utilization
  - *From: VK (5080 128gb)*

- **GGUF vs FP8 for RAM usage**
  - GGUF does save RAM even though it saves less VRAM with full offloading
  - *From: Kijai*

- **Chrome vs Edge browser VRAM usage**
  - Chrome takes 100mb+ VRAM while Edge takes 40mb with hardware acceleration turned off
  - *From: hicho*

- **GPU vs CPU T5 encoding speed**
  - GPU is 65x faster but CPU avoids offloading overhead
  - *From: Kijai*

- **VACE vs regular Wan i2i**
  - VACE i2i produces better similarity to input images
  - *From: hicho*

- **TeaCache vs EasyCache**
  - EasyCache should theoretically be better and works with any model without coefficients
  - *From: Kijai*

- **Wan 2.2 14B vs closed source models**
  - Absolutely astonishing and can truly compete with closed source models
  - *From: yo9o*

- **VACE reference vs Phantom**
  - VACE reference better than Phantom
  - *From: hicho*

- **Wan 2.2 5B vs old 1.3B**
  - 5B is faster despite being larger due to better VAE
  - *From: comfy*

- **Wan 2.2 quality vs Hailuo 2**
  - Might be Hailuo 2 level quality based on acrobatics examples
  - *From: thaakeno*

- **Wan 2.1 vs Wan 2.2 5B vs Fast Wan 1.3B**
  - Wan 2.1 still considered best by some users, 2.2 needs time to mature
  - *From: patientx*

- **5B vs 1.3B quality**
  - 5B worse than 1.3B in some tests, may need different prompting approach
  - *From: Kijai*

- **Wan 2.2 vs Wan 2.1**
  - 2.2 looks more realistic but 2.1 has matured more
  - *From: Thom293*

- **fp8 vs fp16 performance on 5B**
  - fp16 significantly better quality than fp8 on 5B model
  - *From: Kijai*

- **Q8 vs other quantizations**
  - Q8 is clearly the best quantization option
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Wan 2.2 vs anisorav3**
  - Wan 2.2 easily beats anisorav3
  - *From: PolygenNoa*

- **5B T2V quality vs other models**
  - 5B T2V is not very good, far worse than even 1.3B according to Kijai
  - *From: Kijai*

- **14B quality vs smaller models**
  - 14B 2.1 is much better quality than 1.3B or 5B, no reason to use smaller models since 14B with FusionX is fast
  - *From: Dream Making*

- **Both new Wan models vs 2.1 for I2V**
  - Both new Wans blow away 2.1 for image to video
  - *From: Ada*

- **2.1 vs 2.2 motion quality**
  - Motion is definitely better with 2.2
  - *From: Charlie*

- **20 steps vs 4 steps LightX2V**
  - 20 steps 3.5cfg is WORSE than 4 steps lightx2v on 14B i2v
  - *From: ZeusZeus (RTX 4090)*

- **Regular LightX2V vs Adaptive**
  - Adaptive is more detailed but may need more steps
  - *From: Juampab12*

- **2.1 vs 2.2 for T2I**
  - Got better t2i results from 2.1
  - *From: GalaxyTimeMachine (RTX4090)*

- **WAN 2.2 vs 2.1 quality**
  - 2.2 is definitely a step up in quality at full steps + CFG
  - *From: gokuvonlange*

- **Full steps vs LightX2V speed**
  - LightX2V: 68s per step vs 172s per step full quality on 4090
  - *From: Juan Gea*

- **WAN 2.2 5B I2V vs 2.1 I2V 14B**
  - Comparison test shared showing differences
  - *From: toyxyz*

- **20 steps CFG 3.5 vs 10 steps CFG 1 with LightX**
  - Left side (full) is much better in every way
  - *From: Quality_Control*

- **Wan 2.1 vs 2.2**
  - 2.2 shows better expression quality, more cinematic results, and improved prompt adherence. Motion and realism improvements noted
  - *From: gokuvonlange*

- **5B vs 1.3B model quality**
  - 5B produces worse faces than 1.3B model, despite being larger
  - *From: DiXiao*

- **Wan 2.2 vs Kling quality**
  - 2.2 is close to Kling quality
  - *From: QANICS*

- **2.2 vs MovieGen**
  - User thinks 2.2 is more cinematic than MovieGen
  - *From: slmonker*

- **2.2 vs 2.1 quality**
  - 2.2 provides better motion and camera movement, but 2.1 feels cleaner with LightX2V
  - *From: Kijai*

- **FP16 vs FP8 models**
  - FP16 giving better results and same speed as FP8 scaled models
  - *From: Juan Gea*

- **High vs Low noise models**
  - High noise model is more interesting and provides better motion, low noise is closer to classic 14B
  - *From: Ablejones*

- **High-noise vs Low-noise model motion**
  - High-noise model produces more interesting and better motion than low-noise
  - *From: Kijai*

- **Wan 2.2 vs 2.1 prompt following**
  - 2.2 follows prompts better than 2.1
  - *From: Charlie*

- **LightX2V on High-Noise vs Low-Noise only**
  - LightX2V does something useful for High-Noise sampler but effect seems weaker
  - *From: Ablejones*

- **LightX vs CausVid for prompt adherence**
  - 
  - *From: DawnII*

- **5B vs 14B motion quality**
  - 
  - *From: Nekodificador*

- **FusionX vs LightX LoRA**
  - 
  - *From: VRGameDevGirl84*

- **Different step counts affect quality**
  - 
  - *From: Kenk*

- **LightX i2v rank 256 vs rank 64**
  - 
  - *From: PATATAJEC*

- **Wan 2.2 vs 2.1 FusionX**
  - 2.2 has better facial expression, prompt following, global composition and motion. More complex motion capability. Skin detail looks more natural
  - *From: mamad8*

- **Character_ai workflow vs ComfyUI default workflow**
  - Character_ai workflow produces far better results than default ComfyUI workflow for both T2V and I2V
  - *From: GOD_IS_A_LIE*

- **Native vs Wrapper for 2.2**
  - Native produces better results than wrapper with exact same config (loras, resolution, steps, cfg)
  - *From: mamad8*

- **2.2 I2V vs 2.1**
  - I2V at 4 steps is much better than 2.1 - dramatically improved
  - *From: Jonathan*

- **Euler scheduler vs UniPC**
  - Euler scheduler kills/outperforms UniPC for this model
  - *From: GOD_IS_A_LIE*

- **6 steps vs 20-40 steps**
  - Higher step counts (20-40) reduce corruption and blurring, but some users get good results at 6 steps with proper settings
  - *From: jeffcookio*

- **Wan 2.2 vs Wan 2.1 motion quality**
  - Motion is way better and more lifelike in 2.2, follows prompts much better, definite step up but slower
  - *From: Grimm1111*

- **Wan 2.2 vs Veo3**
  - Using high+low stages properly yields pretty much Veo3 quality, beyond Veo3 in cinematics, probably equal in motion and prompt adherence
  - *From: MysteryShack*

- **res_2s + big_tangent vs other schedulers**
  - Produces noise and bad blur, not recommended
  - *From: GOD_IS_A_LIE*

- **Native vs Wrapper**
  - Native doesn't work on older Ampere cards, wrapper more compatible but native with GGUF saves 60% memory
  - *From: MysteryShack*

- **Wan 2.2 vs 2.1 style handling**
  - 2.2 is much better at handling different styles compared to 2.1
  - *From: TK_999*

- **5B vs 14B model performance**
  - 5B is slower than 14B due to very slow VAE, 14B has better quality
  - *From: Drommer-Kille*

- **Q3 quantization 2.1 vs 2.2**
  - Q3 sucked with 2.1 but works surprisingly well with 2.2
  - *From: Jonathan*

- **Wan 2.2 vs 2.1 quality**
  - 2.2 has markedly better prompt adherence and character recognition
  - *From: VK*

- **Lightx2v vs vanilla 2.2 speed**
  - Lightx2v: 70 seconds vs Vanilla: 16 minutes, but vanilla has more movement
  - *From: Drommer-Kille*

- **Radial attention impact on results**
  - Can have very negative effects on results, especially with high noise model
  - *From: Kijai*

- **5B vs 14B model quality**
  - 5B will never beat 14B, especially new 14B with refiner
  - *From: Draken*

- **Wan 2.1 vs 2.2**
  - 2.1 vs 2.2 is like comparing 1.3b with 2.1 in terms of quality difference
  - *From: hicho*

- **5B vs 14B models**
  - 14B is way better than 5B, but 5B vanilla can be used without problems and is faster. 14B needs lightx for fast generations but that LoRA kills the motion
  - *From: Nekodificador*

- **Q6 vs scaled models**
  - Q6 is worse of all quantization options and quite lossy, especially for extreme prompts
  - *From: Kijai*

- **SageAttention3**
  - Disappointing with huge quality hit. You have to limit when it's applied so much that it loses speed benefit
  - *From: Kijai*

- **Radial attention vs SageAttention3**
  - Radial attention seems better choice than SageAttention3, still has quality hit but not as bad
  - *From: Kijai*

- **5B vs LTX-Video**
  - At least wan2.2-5B is more consistent than ltxv. LTX would give cardboard instead of detailed hair
  - *From: QANICS🕐*

- **Works fine vs best quality**
  - Single sampler works but dual sampler setup produces better results
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Q8 vs fp8 model sizes**
  - Q8 is actually larger than fp8, contrary to expectations
  - *From: Kijai*

- **Different fp8 quantization methods**
  - fp8_e3m2 v2 may look best overall, e4m3 better for character details
  - *From: Kijai*

- **Native ComfyUI vs Wrapper for Wan 2.2**
  - Wrapper had better memory management and avoided channel errors that native implementation was giving
  - *From: fredbliss*

- **High-noise vs Low-noise model performance**
  - High-noise model better at everything except fine details. Should run high-noise to lower sigma levels then use low-noise for refinement
  - *From: Ablejones*

- **Wrapper vs Native ComfyUI memory management**
  - Wrapper manages RAM better than native ComfyUI
  - *From: Doctor Shotgun*

- **FP8 wrapper vs FP16 native generation speed**
  - FP16 native can be quicker than FP8 wrapper in some cases
  - *From: BobbyD4AI*

- **5B vs 14B model performance**
  - 5B generates in 150 seconds vs 30 minutes for 14B, but 5B is rubbish for faces
  - *From: AJO*

- **Wan 2.2 vs Hailou 2 with same prompt**
  - Both produce good results with different characteristics
  - *From: Drommer-Kille*

- **Wan 2.2 14B vs 2.1**
  - 2.2 14B blows away 2.1 in quality, prompt adherence, and motion
  - *From: Ada*

- **5B model vs latest 1.3B**
  - 5B model is currently worse and slower than the latest 1.3B
  - *From: Mngbg*

- **FP16 full steps vs LightX2V distillation**
  - 4min vs 40sec sampling time, but quality difference may not be significant with proper LightX2V settings
  - *From: MilesCorban*

- **Native vs LightX2V results**
  - LightX2V produces very different results, almost like running a completely different seed rather than just being worse
  - *From: orabazes*

- **High noise vs Low noise models**
  - High noise does composition and motion, low noise is basically tuned up wan2.1 for details
  - *From: Ablejones*

- **Wan 2.2 vs 2.1**
  - Much greater improvement than .1 version would suggest, insanely good upgrade with way better prompt adherence
  - *From: Juampab12*

- **Wan 2.2 5B vs 14B for movement**
  - 5B has terrible movement compared to 2.2 14B model
  - *From: Kijai*

- **Wan vs AnimateDiff for vid2vid**
  - Wan 2.1 was better than AnimateDiff, hoping 2.2 5B gives even better results
  - *From: xwsswww*

- **1.3B vs 5B model quality**
  - 1.3B looks better than 5B from examples posted
  - *From: Corneilious Pickleberry*

- **Wan 2.2 vs closed models**
  - Got among the best motion compared to closed models in official project testing
  - *From: NebSH*

- **Wan 2.2 vs FusionX**
  - Both good but different, 2.2 is more crisp in some cases
  - *From: VRGameDevGirl84(RTX 5090)*

- **5B vs 14B quality**
  - 5B T2V works poorly compared to 14B, faces are problematic in 5B
  - *From: DiXiao*

- **GGUF vs safetensors performance**
  - GGUF slower but uses less VRAM, safetensors faster but needs more VRAM
  - *From: thaakeno*

- **F8 scaled vs Q8 GGUF quality**
  - F8 scaled better than F8, worse than Q8 GGUF
  - *From: Daflon*

- **Q4 vs Q8 GGUF**
  - Q4 uses less VRAM, generation speed same if you have enough memory
  - *From: Jonathan*

- **GGUF vs block swap**
  - GGUF is like optimized version of base model, block swap and GGUF are similar
  - *From: Kijai*

- **Kijai scaled models vs Comfy team models**
  - Different but hard to say which is better, just different scaling method
  - *From: N0NSens*

- **fp16 vs bf16 VAE quality**
  - fp16 quality is better than bf16 when it works
  - *From: comfy*

- **Phantom_Wan_14B_FusionX_LoRA vs LightX2V on Wan 2.2 I2V**
  - Phantom appears better for motion and artifacts
  - *From: linoy*

- **MAGREF vs other WAN models for long generation**
  - MAGREF more consistent for 400 frame gens without artifacts vs other models that create crossfades
  - *From: blake37*

- **Wan 2.2 vs Kling for food video**
  - The fact that an open source model is better than closed source at this is insane
  - *From: thaakeno*

- **Wan 2.2 vs Kling 2.1 Master**
  - Wan 2.2 comes very near it too and doesn't cost $1 per clip
  - *From: gokuvonlange*

- **Vanilla 5B vs 14B vs Lightx**
  - 5B worth it for very dynamic shots with motion, 14B less dynamic than expected for camera orbit
  - *From: Nekodificador*

- **HighNoise with vs without distill lora**
  - Without lora may produce more interesting motion and better prompt adherence, but needs more steps
  - *From: gokuvonlange*

- **FastWan vs LightX2V loras**
  - FastWan alone gives good motion but lots of warping, LightX2V gives slow videos, combining both at 1.0 produces best motion with little warping
  - *From: Ant*

- **I2V with distill lora vs raw model**
  - I2V with lightxv2 lora feels like wan 2.1, loses some of the interesting motion that 2.2 adds
  - *From: gokuvonlange*

- **Different shift values**
  - Shift 1 looks much better than shift 8, which felt like 2.1
  - *From: hicho*

- **All-in-one merge vs native 2.2**
  - Merged model looks like pure 2.1, loses 2.2 soul and capabilities
  - *From: slmonker(5090D 32GB)*

- **2.2 vs 2.1 prompt following**
  - 2.2 follows prompts better and can understand complex prompts with amazing motion
  - *From: Godhand*

- **With vs without distill lora on high noise**
  - Without distill lora maintains cinematic tone, with it returns to flat TV series colors
  - *From: slmonker(5090D 32GB)*

- **Wan 2.2 vs 2.1**
  - 2.2 is crazy how much better than 2.1. Using only low noise model is pretty much exactly same as 2.1 outputs
  - *From: Ada*

- **5B vs 14B motion quality**
  - 5B motion isn't even close to same category as 2.2 14B, but image quality potential is pretty high on 5B
  - *From: Kijai*

- **High noise with vs without distill LoRA**
  - Leaving HighNoise model with no distill will produce faaar better results than using lightX LoRA, though you get ok results on par with wan 2.1 using lightX LoRA on I2V
  - *From: gokuvonlange*

- **4090 vs 5090 performance**
  - 5090 is ~40% faster with significantly higher throughput
  - *From: Juampab12*

- **2.2 generation times vs 2.1**
  - 2.1 took 20min on 4090, now 2.2 takes 5min with better quality
  - *From: Juampab12*

- **14B vs 5B model quality**
  - 14B is much better than 5B, 5B seems worse than 1.3B for some use cases
  - *From: VK*

- **fp8_e5m2 vs fp8_e4m3fn quality**
  - e5m2 is 0.3% worse quality than e4m3 but allows torch compile
  - *From: phazei*

- **Consolidated 2.2 model quality**
  - Degraded to HunyuanVideo quality level, not recommended
  - *From: gokuvonlange*

- **dpmpp_sde vs LCM sampler**
  - dpmpp_sde is WAY better than LCM
  - *From: homem desgraca*

- **14B vs 5B model quality**
  - 14B produces significantly better results than 5B, especially for faces and motion
  - *From: VK (5080 128gb)*

- **GGUF vs fp8 models**
  - fp8 e5m2 works better than Q4 GGUF despite larger size, GGUF is 20% slower due to dequantization
  - *From: mdkb*

- **Wan 2.2 vs Veo3**
  - Wan 2.2 exceeds Veo3 quality (not counting audio)
  - *From: MysteryShack*

- **5B vs 1.3B model improvement**
  - Jump from 1.3B to 5B is smaller than from 2.1 to 2.2 14B
  - *From: homem desgraca*

- **5B vs 1.3B model for vid2vid**
  - 5B performs better for transformations but quality may suffer with GGUF quantization
  - *From: thaakeno*

- **All-in-one merges vs true 2.2**
  - All-in-one merges are more like 2.1 than 2.2, very misleading to call them 2.2
  - *From: Kijai*

- **WAN 2.2 two-stage vs traditional vid2vid**
  - Works much better than traditional models for vid2vid
  - *From: Draken*

- **81 frames vs 121/161 frames**
  - 81 frames works best, longer sequences cause looping issues and aren't properly trained
  - *From: Kijai*

- **WAN 2.2 14B vs 5B quality**
  - 14B quality is far better than 5B model, but 5B model described as 'so bad'
  - *From: thaakeno*

- **WAN 2.2 vs 2.1 for EchoShot**
  - EchoShot method works better on 2.1 than 2.2 for some prompts
  - *From: Kijai*

- **WAN 2.2 5B GGUF vs 14B speed**
  - 5B GGUF took 13mins vs 14B taking 23mins for similar output
  - *From: Abx*

- **WAN 2.2 vs 2.1 faces**
  - 2.2 has much more detailed faces even when far from camera, 2.1 had disfigured blurry faces
  - *From: xwsswww*

- **Speed LoRAs vs pure 2.2**
  - Speed LoRAs feel more like WAN 2.1.5 rather than 2.2, destroys the soul of what makes 2.2 amazing
  - *From: gokuvonlange*

- **WAN 2.2 prompt understanding vs others**
  - Best in open source by wide margin for prompt understanding
  - *From: Kijai*

- **FP8 e4m vs FP16**
  - e4m2 v2 looks just like fp16, e4 has slightly more skin details than fp16
  - *From: Gill Bastar*

- **TAEW vs latent upscale**
  - TAEW is faster and better quality than latent upscale
  - *From: Kijai*

- **CFG vs LightX2V motion and quality**
  - Full steps + cfg gives more motion than lightx2v and follows prompts better in some cases, but cfg gives more saturation. LightX2V at 6.0 strength is still fine
  - *From: Hashu*

- **5B vs 14B model quality**
  - 5B looks bad compared to 14B. 14B q3 is great while 5B has poor consistency and object permanence issues
  - *From: SonidosEnArmonía*

- **Wan 2.2 vs other models**
  - Rawdogging the model is like Kling 2.1 Master. Distill lora feels like slightly better hunyuan / wan 2.1
  - *From: gokuvonlange*

- **2.2 high+low vs 2.2 high+2.1 low vs 2.2 high+Skyreels**
  - Last two look the same - questioning if low noise is just skyreels
  - *From: VRGameDevGirl84*

- **Q8 vs fp8 scaled**
  - fp8 is ~20% faster, Q8 is slightly better quality but also larger file size
  - *From: Kijai*

- **GGUF vs fp8 scaled performance**
  - GGUF is tightly packed but requires unpacking causing speed loss. fp8 scaled dequantizes much faster with single float value
  - *From: Kijai*

- **Wan 2.1 vs 2.2 quality**
  - Left sample (2.2) has better skin detail quality
  - *From: VRGameDevGirl84(RTX 5090)*

- **NAG processing time impact**
  - NAG adds 11 seconds (191s vs 180s) with minimal quality benefit
  - *From: VRGameDevGirl84(RTX 5090)*

- **Wan 2.1 loras on 2.2**
  - Work poorly, bring noise and quality loss. Retraining for 2.2 works 100x better
  - *From: lovis.io*

- **5090 vs 4090 on RunPod**
  - 4090 with blockcache at 20 performed better (190s) than RunPod 5090 (200+ seconds)
  - *From: Quality_Control*

- **2.2 vs 2.1 for violence**
  - 2.2 completely censored violence while 2.1 could do some grimy stuff
  - *From: Juampab12*

- **High noise vs Low noise models**
  - Low noise is closer to 2.1, high noise is more different and better quality
  - *From: Juampab12*


## Tips & Best Practices

- **Use first segment with fusionX recipe, then light2x for extending**
  - Context: Light2x is faster and doesn't burn the video for extensions
  - *From: Vardogr*

- **Generate first segment with quality settings, use speed loras for extending**
  - Context: For video extension workflows to maintain quality while improving speed
  - *From: Vardogr*

- **Try all default settings first before changing**
  - Context: Many people change settings then complain videos don't look good
  - *From: VRGameDevGirl84(RTX 5090)*

- **Always compile with inductor for speed and memory boost**
  - Context: When using larger models, except when troubleshooting as it obfuscates error logs
  - *From: Kijai*

- **Use 'lettuce' as good modifier for organic patterns**
  - Context: When prompting for coral/organic textures
  - *From: Mads Hagbarth Damsbo*

- **Run comparison tests after initial model loading**
  - Context: To get accurate timing comparisons without model load times
  - *From: VRGameDevGirl84(RTX 5090)*

- **Use NAG with CFG 1.0 for most generations**
  - Context: Current recommended settings for quality
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Use dpm++_sde scheduler with shift 5.0 for LightX2V**
  - Context: Personal preference for better results
  - *From: Kijai*

- **Disable tea cache, slg and experimental args when using LightX2V at 4 steps**
  - Context: They won't do anything anyway with the LoRA
  - *From: Kijai*

- **Use masked face instead of full depth for better MultiTalk results**
  - Context: Reduces competition between VACE depth and MultiTalk
  - *From: Tango Adorbo*

- **Replace first image in batch with original unmasked to keep exact likeness**
  - Context: Prevents ref image drift in VACE workflows
  - *From: Tango Adorbo*

- **Use DaVinci Resolve or After Effects for great animated masks**
  - Context: Best approach for inpainting workflows
  - *From: Nekodificador*

- **Use pip freeze > requirements.txt before installing new nodes**
  - Context: To backup working environment before making changes that could break existing setup
  - *From: manu_le_surikhate_gamer*

- **Color match node helps maintain reference image colors**
  - Context: When doing video generation to preserve original image coloring
  - *From: VRGameDevGirl84(RTX 5090)*

- **Film grain node improves WAN image output**
  - Context: Adds texture and reduces artificial appearance
  - *From: VRGameDevGirl84(RTX 5090)*

- **Use Sameface Fix LoRA with Flux**
  - Context: Gets rid of default Flux face for better variety
  - *From: David Snow*

- **Use Canny control only when you want very detailed control**
  - Context: Canny gets too detailed for most use cases unless trying to match exactly
  - *From: VRGameDevGirl84(RTX 5090)*

- **For Skyreels, set all LoRAs to 0.2 strength**
  - Context: LoRAs have different effects in Skyreels compared to Wan, need lower strength
  - *From: VRGameDevGirl84(RTX 5090)*

- **Use grey masks around edges for VACE merging**
  - Context: When trying to merge two images, VACE will fill in the blanks around grey mask areas
  - *From: Jonathan*

- **Use normals instead of depth for better face control**
  - Context: Depth alone isn't strong enough signal for fine facial control, normals provide more detail
  - *From: spacepxl*

- **Single frame generation good for testing inputs**
  - Context: Test how inputs behave before running longer generations
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Use expanding masks for fire effects in VACE**
  - Context: Just expanding the mask works... prompting is SO important in VACE
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Make ComfyUI snapshot before updating**
  - Context: Make a snapshot via comfy manager, then update
  - *From: CJ*

- **Use infer one frame to test VACE prompting**
  - Context: sometimes the whole setup is fine but the prompt, I started to use the 'infer' one frame to see how it's interpreted
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Reduce LoRA strength for more steps with self-forcing**
  - Context: if you want to do more steps you should reduce the LoRA strength... usually I've noticed it just sort of gets burned if you do too many steps with the lora
  - *From: Kijai*

- **Use pose controlnet over depthmap when wanting face structure to stay same**
  - Context: Gives VACE more control options, use with reference image of face
  - *From: mdkb*

- **Use last frame selector by media mixer for video extension**
  - Context: More elegant than get image range for extending videos
  - *From: hicho*

- **Expand SAM2 masks as they are often too tight**
  - Context: When using SAM2 masks for VACE inpainting
  - *From: ˗ˏˋ⚡ˎˊ-*

- **For VACE inpainting, fill masked area with grey in RGB and use white in mask**
  - Context: Grey in RGB tells model to generate, white in mask provides specific control
  - *From: Rishi Pandey*

- **Use distorch offload to RAM for lower VRAM cards**
  - Context: Can put 14GB in RAM to avoid OOMs on 12GB card
  - *From: mdkb*

- **Combine VACE with other conventional tools for better results**
  - Context: VACE works well as part of larger workflows
  - *From: yukass*

- **Use 'still camera' prompt instead of Uni3c**
  - Context: Easier to get more character movement in frame than turning on Uni3c and getting a static dummy
  - *From: N0NSens*

- **Image datasets work very well on text to video**
  - Context: Training LoRAs with image datasets produces excellent results for T2V generation
  - *From: VRGameDevGirl84*

- **Some prompts work better with different shift values**
  - Context: Higher shift values can remove strange particle noise in some generations
  - *From: VRGameDevGirl84*

- **Use Transform Image node for padding**
  - Context: Better than dedicated padding nodes for adding borders to images
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Use explicit prompting with VACE for reference images**
  - Context: When trying to get VACE to use reference images effectively
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Set LightX2V LoRA strength to 1.0**
  - Context: When using the distilled LoRA version
  - *From: Screeb*

- **Work with the 4n+1 frame limitation rather than fighting it**
  - Context: When dealing with MultiTalk frame count issues
  - *From: samhodge*

- **Use Wan for generating init images for consistency**
  - Context: Using same model for both image and video generation ensures better consistency and faster performance
  - *From: Impactframes.*

- **Use contrast node for post-processing rather than relying on scheduler differences**
  - Context: When dealing with contrast issues from different schedulers
  - *From: David Snow*

- **Use transparent background reference images for better VACE results**
  - Context: Only the subject is visible, prevents unwanted elements transferring
  - *From: David Snow*

- **Describe the full video including the object when prompting VACE**
  - Context: Instead of just 'dog', describe the entire scene with the dog
  - *From: ingi // SYSTMS*

- **Generate at 1600 pixel range as sweet spot for quality vs VRAM**
  - Context: Can't do full 81 frames at 1920 with 24GB VRAM
  - *From: David Snow*

- **Use segmentation to mask depth maps for controlled background generation**
  - Context: Target person with depth/pose control, let background generate from prompt only
  - *From: mdkb*

- **Always convert to fp8_e5m2 from original fp16, not from fp8_e3m4fn**
  - Context: Avoids doing lossy conversion on lossy conversion
  - *From: patientx*

- **Set quant to disabled when using GGUF**
  - Context: Best practice for GGUF usage in wrapper
  - *From: Kijai*

- **Use LightX2V at full strength, causvid and accvideo at much lower strengths**
  - Context: LightX2V is superior, others just boost quality a bit
  - *From: David Snow*

- **Try lower resolution like 1600x900 then upscale for full HD**
  - Context: Full HD generation is too resource intensive and slow
  - *From: David Snow*

- **Use experimental args and enhance video options**
  - Context: Small but noticeable quality improvement with wrapper
  - *From: David Snow*

- **Use color match node for desaturated results**
  - Context: When generated videos have color issues
  - *From: David Snow*

- **Use VACE for extending I2V generations**
  - Context: Can start from image then extend results with VACE using multiple images
  - *From: Kijai*

- **Merging LoRA is done on GPU to avoid slow performance**
  - Context: Use low_mem_load if you have VRAM constraints, loads model and applies LoRA layer by layer
  - *From: Kijai*

- **Use start/end frame node only to create empty frames for VACE**
  - Context: If feeding all frames, start/end frame node doesn't do anything
  - *From: Kijai*

- **Stop using film grain for video**
  - Context: Works OK for text to image but bad for video generation
  - *From: VRGameDevGirl84(RTX 5090)*

- **Use UniAnimate with bones only, not white dots**
  - Context: UniAnimate is trained with bones, not face dots
  - *From: Kijai*

- **Apply Uni3C only to first step**
  - Context: May be unnecessary altogether when using with UniAnimate
  - *From: Kijai*

- **Use single frame generation first to test prompts and settings quickly before increasing frame count**
  - Context: Instead of treating it like a slot machine and wasting energy
  - *From: ▲*

- **Nuclear solution for long video context issues is more overlap**
  - Context: Won't work for I2V without strong control signal
  - *From: Kijai*

- **Use differential diffusion masks to control background diffusion strength**
  - Context: White controls strength in grey inpaint mask, darker background for everything else
  - *From: David Snow*

- **Disable clip embed for better MAGREF reliability**
  - Context: When using MAGREF for reference image consistency
  - *From: A.I.Warper*

- **Use CFG with first step for better prompt adherence**
  - Context: When using CFG 1.0 which may reduce prompt adherence
  - *From: Kijai*

- **Preprocess raw video with controlnet**
  - Context: When VACE stylization isn't working on raw video input
  - *From: MilesCorban*

- **Use pose for character and depth for background separately**
  - Context: To avoid over-constraining character to depth map while maintaining camera lock
  - *From: Sal TK FX*

- **Reduce FusionX detail LoRA strength to 0.5 and increase steps to 30-40**
  - Context: For single frame generation experiments
  - *From: Shawneau 🍁 [CA]*

- **Use depth for restyle and background, DW pose for humans with Florence prompt**
  - Context: When doing style transfer with human subjects
  - *From: hicho*

- **Use uni3c to lock camera and prevent context window jumps**
  - Context: When using context windows with MultiTalk
  - *From: Kijai*

- **For people videos, set Moviigen to 0.5, MPS to 0.5**
  - Context: Better results when generating videos with human subjects
  - *From: VRGameDevGirl84(RTX 5090)*

- **Use shift value of 2 and dpm++_sde/beta scheduler for background issues**
  - Context: When getting cursed nonsense backgrounds
  - *From: VRGameDevGirl84(RTX 5090)*

- **Use 'fix node' after updating to get GGUFs to show up in old workflows**
  - Context: After wrapper updates
  - *From: mdkb*

- **Turn off 'use-non-blocking' to enable LoRA usage on low VRAM**
  - Context: For 3060 users with wrapper workflows
  - *From: mdkb*

- **Get all encoders to fp16 and t5 to GGUF using bridge**
  - Context: For low VRAM optimization
  - *From: mdkb*

- **Use shift 5-8 for maintaining reference, shift 16-20 for motion LoRAs or VACE control**
  - Context: When balancing reference adherence vs motion
  - *From: DawnII*

- **Ditch AccVid, have LightX around 1, play with LoRA values and shift/steps**
  - Context: For photorealistic humans with quality LoRAs
  - *From: Grimm1111*

- **Use video extension as basic VACE test**
  - Context: Feed 4-16 frames of existing video and watch it infer the rest
  - *From: DawnII*

- **Pad Wan Vace outputs so they don't take whole screen**
  - Context: When using Vace for better framing
  - *From: hicho*

- **Use Virtual Memory settings on Windows 10 for low RAM systems**
  - Context: Allows running LoRA stacks on systems with limited system RAM
  - *From: The Shadow (NYC)*

- **Balance LightX2V with low strength ACC or CausVid**
  - Context: To compensate for artifacts when using lower LightX2V strength
  - *From: phazei*

- **Use GGUF text encoders to save RAM without big quality hit**
  - Context: For systems with limited RAM
  - *From: Kijai*

- **Don't use batch size 1 for SeedVR2 - causes poor temporal consistency**
  - Context: Use higher batch sizes like 45, ideally matching longest shot frame count
  - *From: Adrien Toupet*

- **Use integer nodes and connect them for width/height/frames**
  - Context: So you don't have to change it manually in every node
  - *From: ingi // SYSTMS*

- **Make mask way lighter at the tips to achieve fading effect**
  - Context: For flame tips and similar effects
  - *From: AmirKerr*

- **Expand mask incrementally for better lighting integration**
  - Context: When handling lighting from objects like fireballs on surrounding area
  - *From: AmirKerr*

- **Prompt is everything in VACE workflows**
  - Context: Reference images may have minimal effect, detailed prompts are crucial
  - *From: AmirKerr*

- **Set frame load limit to match intended generation frames**
  - Context: When using videos with more frames than you're generating
  - *From: ingi // SYSTMS*

- **Lower face detailer weight to retain more facial motion**
  - Context: When using face detailer LoRA, reducing weight from 1.00 to 0.5 brings back more facial animation
  - *From: VRGameDevGirl84(RTX 5090)*

- **Use constant node for frame count instead of dynamic**
  - Context: When switching between test (5 frames) and full runs (41 frames), use int-constant to avoid mismatches
  - *From: mdkb*

- **Reference image works for first frame propagation but not cross-shot consistency**
  - Context: Reference works fine to propagate first frame to entire video but not for feeding frames from other shots
  - *From: Nekodificador*

- **Use firewall that asks permission for internet access**
  - Context: Best security practice - allow python for pip installs but restrict afterwards
  - *From: Draken*

- **Use depth and openpose separately with VACE**
  - Context: Can get away with blending but not always reliable
  - *From: David Snow*

- **Make reference image roughly same position as start frames**
  - Context: When not matching positions, gets ghosts in background
  - *From: mdkb*

- **Use multiply blend with 50% opacity for lineart**
  - Context: More lineart gives details but less subject likeness
  - *From: Hashu*

- **Only mask eyes/mouth area for control**
  - Context: Prevents defining head shape while maintaining expression control
  - *From: Hashu*

- **Celebrity LoRAs work well due to base model presence**
  - Context: LoRAs converge quickly and help retain face throughout video
  - *From: gokuvonlange*

- **Famous faces always need LoRA for consistency**
  - Context: Easy dataset availability for every angle and expression
  - *From: mdkb*

- **Use Flux as first step, then WAN 2.1 T2V for low amplitude repaint**
  - Context: For enhanced text-to-image generation workflow
  - *From: slmonker(5090D 32GB)*

- **Use anylineart preprocessor at lower resolution (512 or 256)**
  - Context: When working with lineart for better face movement control
  - *From: Hashu*

- **Boost MPS over 1.3 and tweak shift to 8+ when using Skyreels merges**
  - Context: To counteract greyish results from Skyreels and improve performance
  - *From: ▲*

- **Use higher LoRA strength for VACE with LightX**
  - Context: 1.1-1.2 for rank32, 1.3-1.4 for rank16 when using LightX LoRA with VACE
  - *From: DawnII*

- **Use I2V LoRA for both T2V and I2V workflows**
  - Context: When T2V LoRA doesn't work properly
  - *From: DawnII*

- **Disable ComfyUI node cache on command line**
  - Context: Saves significant system RAM usage
  - *From: Gateway {Dreaming Computers}*

- **Update KJ custom nodes for VACE performance**
  - Context: VACE now works full speed with sage attention after recent updates
  - *From: mdkb*

- **Use 2-step generation approach for higher resolution**
  - Context: Better to run lower res first, then use result for higher res upscaling
  - *From: Draken*

- **Rank 16 seems best for avoiding double birds/artifacts**
  - Context: Testing different LoRA ranks
  - *From: Gateway {Dreaming Computers}*

- **Rank 64 appears to be the sweet spot for most use cases**
  - Context: Multiple users testing different ranks
  - *From: David Snow*

- **Try bumping up LightX2V lora strength - works really well**
  - Context: Can push to 1.5-2.0 strength for better results
  - *From: Hashu*

- **Use I2V lora for VACE workflows even though VACE is technically T2V**
  - Context: Better results reported with I2V lora on VACE
  - *From: The Shadow (NYC)*

- **Get rid of AccVid when using new LightX2V - might be nuking too much**
  - Context: Lora stacking advice
  - *From: Kijai*

- **Use Q8 GGUF for better quality and memory efficiency**
  - Context: When running VACE or other memory-intensive workflows
  - *From: garbus*

- **Remove 'ice cream machine' from prompts as it messes up generation**
  - Context: When using food-related prompts that aren't working properly
  - *From: garbus*

- **Use separate VACE embeds instead of blended depth/op controls**
  - Context: For better control results in most cases
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Try Motion Boost LoRA to replace ACC LoRA**
  - Context: KJ mentioned dropping ACC earlier, Motion Boost starting at 0.5 strength
  - *From: The Shadow (NYC)*

- **Use spline editor in KJ nodes for dot animation**
  - Context: When creating control animations for VACE
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Keep torch compile at default settings**
  - Context: Other modes like reduce-overhead take ages and may break
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Use lightx2v with Pusa at strength 1.4**
  - Context: For best results with Pusa lora
  - *From: David Snow*

- **Extract vocals from music for better lip sync**
  - Context: When using Multitalk with music tracks
  - *From: Charlie*

- **Pad/resize image to same dimensions as target video**
  - Context: For face retention with loras
  - *From: gokuvonlange*

- **Use clear shot of face only, no shoulders or outfit**
  - Context: For better face retention to avoid bleeding into video
  - *From: gokuvonlange*

- **Don't use other loras with Pusa**
  - Context: Other loras will break Pusa's functionality
  - *From: Kijai*

- **Use higher CFG and more steps with distilled models to reduce blurriness**
  - Context: When using LightX2V LoRAs
  - *From: Piblarg*

- **Pusa LoRA needs weight 1.4+ to avoid changing initial frame too much**
  - Context: When using Pusa for I2V
  - *From: Kijai*

- **Use DPM++SDE sampler with Phantom model for better results**
  - Context: Phantom needs more steps to cook properly
  - *From: Guey.KhalaMari*

- **Phantom doesn't work well with LCM scheduler**
  - Context: Use UniPC instead for better results
  - *From: Doctor Shotgun*

- **Use Q8 for best quality on consumer hardware**
  - Context: When choosing between different model formats
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Disable interpolation for anime-style content**
  - Context: 12 fps feels more anime than interpolated 24 fps
  - *From: el marzocco*

- **Set radial attention start step lower than total steps**
  - Context: If start step is higher than total steps, radial attention won't activate. Start step 0 is fastest but quality suffers
  - *From: Kijai*

- **Use disk instances on RunPod for model storage**
  - Context: Keep models and nodes on persistent disk that can connect to any pod, including serverless
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Close terminal and restart ComfyUI for faster recovery**
  - Context: When ComfyUI gets stuck on long tasks, restarting is usually faster than waiting
  - *From: AmirKerr, Juampab12*

- **Use torch compile to reduce peak VRAM usage**
  - Context: Default settings are fine, provides considerable VRAM reduction
  - *From: Kijai*

- **Start with 1 dense timestep for radial attention**
  - Context: Increase only if quality isn't satisfactory, can fine-tune with blocks parameter
  - *From: Kijai*

- **Try decay factor setting higher for better quality**
  - Context: When using radial attention, higher decay factor seems to improve quality
  - *From: Kijai*

- **Use block swapping for longer generations**
  - Context: 8-16 blocks swapped adds minimal time penalty, enables higher resolution/longer frames
  - *From: MatiaHeron*

- **Start with dense_steps at 0 then increase until satisfied with quality**
  - Context: When using radial attention
  - *From: Kijai*

- **Describe action and movement without mentioning camera**
  - Context: To achieve static camera shots
  - *From: Charlie*

- **Use --cache-none on ComfyUI startup to free system RAM**
  - Context: Trade-off as it won't cache nodes
  - *From: Gateway {Dreaming Computers}*

- **First step is most important with distill, same with start of blocks**
  - Context: When optimizing radial attention steps
  - *From: Kijai*

- **Retime anime-style videos to 8 or 12 fps for more authentic look**
  - Context: When trying to achieve anime-style movement
  - *From: Juan Gea/N0NSens*

- **Use Flux for initial outpainting then feed to WAN**
  - Context: When outpainting from 9x16 to 16x9, better to use Flux fill/outpaint first then use that as start frame with control video
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Higher resolution reduces motion blur/smudging**
  - Context: Increased resolution does reduce motion blur and smudging issues in WAN
  - *From: Piblarg*

- **Use Model Loader Advanced for block swap adjustments**
  - Context: That way you can adjust block swap without re-loading the model
  - *From: Kijai*

- **Refresh (R) is enough to register new LoRAs**
  - Context: Don't need to restart ComfyUI, refresh is enough to register new LoRAs
  - *From: Kijai*

- **Use flowmatch_pusa scheduler for proper PUSA functionality**
  - Context: Only the Pusa scheduler currently enables the expanded time steps it's meant to be used with
  - *From: Kijai*

- **Don't add PUSA as LoRA to I2V model without proper scheduler**
  - Context: Adding it as a LoRA to I2V model doesn't do anything useful without the proper sampling method
  - *From: Kijai*

- **Use LightX + PUSA at different strengths for better results**
  - Context: lightx at 1 and Pusa 0.75 works better than both set to 1
  - *From: chrisd0073*

- **Try realistic explosion prompts for better explosion effects**
  - Context: WAN tends to produce cartoonish explosions, training a lora on cinematic explosions would fix this
  - *From: gokuvonlange*

- **Use lower strength LightX2V for comparison testing**
  - Context: When testing PUSA benefits, compare against lower strength lightx2v instead of assuming PUSA is helping
  - *From: Kijai*

- **Use MAGREF as base model with Pusa 1.0 and i2v rank64 LoRAs**
  - Context: For better face consistency, cfg 1, 6 steps, flowmatch_pusa
  - *From: ZeusZeus*

- **Prompt that face doesn't make wild expression shifts**
  - Context: To control face morphing in videos
  - *From: gokuvonlange*

- **Use unianimate LoRA with pose video for body movements**
  - Context: For improving hand/body movements in MultiTalk
  - *From: Gateway*

- **Smaller faces have greater probability of unlikeness**
  - Context: Face consistency depends on face size in frame
  - *From: N0NSens*

- **Use Fun Control for better control adherence**
  - Context: When VACE control isn't sticking well enough
  - *From: Hashu*

- **Phantom works better with CFG**
  - Context: If using lightx with phantom, run more steps than normal and run first few steps with cfg ~3
  - *From: Ablejones*

- **Crop characters to same shape for VACE**
  - Context: Cropping characters to roughly the same shape as they are to appear helps with VACE
  - *From: Piblarg*

- **Use dual CFG guider for Phantom's 2 negative embeds**
  - Context: For proper Phantom implementation with its multiple CFG passes
  - *From: Kijai*

- **Reduce LightX2V strength for normal fp8 unmerged**
  - Context: Had to drop the strength of lightx2v to 0.8 for normal fp8 and unmerged
  - *From: Kijai*

- **Generate image from flux/hidream, feed to Fun to get 100% start match frame, then use in VACE**
  - Context: When you want perfect character matching for VACE
  - *From: Hashu*

- **Use basic 14B model + lightx2v LoRA first, then add other stuff if needed**
  - Context: For V2V workflows, easier to troubleshoot
  - *From: Kijai*

- **Lower VACE strengths when using multiple VACEs**
  - Context: When using multiple VACE controls together
  - *From: Kijai*

- **VACE sucks at non-realistic references**
  - Context: When working with stylized or cartoon references
  - *From: Piblarg*

- **Phantom can be quite seed-dependent**
  - Context: When trying to get consistent character likeness
  - *From: Ablejones*

- **Use power limiting to 500W on 5090 to manage temperatures**
  - Context: RTX 5090 running hot (80-83°C) during video generation
  - *From: Kijai*

- **Start Phantom testing with minimal setup**
  - Context: Use base Phantom model, CFG 5, 20 steps for baseline before adding distill LoRAs
  - *From: Ablejones*

- **Use two-pass generation for quality improvement**
  - Context: Generate at target resolution then second pass at 0.15-0.3 denoise strength same resolution - as fast as first pass
  - *From: mamad8*

- **For longer videos, use multiple K-samplers with overlap**
  - Context: Cut video into 81-frame segments with fixed seed to work around frame limitations
  - *From: hicho*

- **Convert training videos to 15 fps then use VHS loader**
  - Context: Most applications don't support 16fps, so convert to 15fps then use Video Helper Suite to convert to 16fps in ComfyUI
  - *From: hicho*

- **Use more dense blocks or dense steps when radial attention affects quality**
  - Context: When experiencing jarring morphing with radial attention
  - *From: Kijai*

- **Use LightX LoRA with Pusa LoRA for I2V**
  - Context: Reduces slow motion effects when combined properly
  - *From: VRGameDevGirl84(RTX 5090)*

- **Don't mention camera movement in prompts when using UniC3**
  - Context: Let UniC3 handle camera movement, prompts should focus on scene/subject
  - *From: VRGameDevGirl84(RTX 5090)*

- **Lower UniC3 strength to preserve prompt effects**
  - Context: When you want both 3D camera movement and prompt-driven effects like fire
  - *From: hicho*

- **Use wireframe instead of solid cubes for UniC3**
  - Context: Seems to work better for camera motion tracking
  - *From: VRGameDevGirl84(RTX 5090)*

- **UniC3 should be used always with I2V**
  - Context: Results are much more boring without UniC3 camera control
  - *From: hicho*

- **Use worldspace gingham texture on solid renders for Uni3C**
  - Context: Provides better features for camera tracking than plain geometry
  - *From: samhodge*

- **Try multiple seeds when MAGREF isn't working**
  - Context: MAGREF can be particular about what images it works with
  - *From: Hashu*

- **Use 64 overlap for better context window performance**
  - Context: Twice the normal overlap reduces snapping issues
  - *From: Kijai*

- **VACE + I2V is best for production work**
  - Context: Preserves art direction better than T2V alone
  - *From: Gill Bastar*

- **Use 0.6 denoise for v2v**
  - Context: For video-to-video generation to get better quality results
  - *From: samhodge*

- **Use 20+ steps at CFG 4-6 for production**
  - Context: For overnight renders when you want higher quality
  - *From: Gateway {Dreaming Computers}*

- **Keep frame counts matching to avoid crashes**
  - Context: When using uni3c with other inputs
  - *From: Kijai*

- **Use mask preview node to confirm masking**
  - Context: To verify that reference frames are marked black and generation frames are marked white
  - *From: Kijai*

- **Set empty_frame_level to 0.5 for gray frames**
  - Context: When using VACE start to end frame node for video extension
  - *From: Hashu*

- **Use 81 frames for best prompt understanding**
  - Context: Wan understands prompts better with full 81 frame generation
  - *From: hicho*

- **Put text descriptions at front of prompt**
  - Context: When generating text in video, try placing text descriptions at the beginning
  - *From: Cubey*

- **Use 10-20% lower LoRA strengths with scaled models**
  - Context: Scaled models work better with reduced LoRA strength
  - *From: Kijai*

- **Use real videos for UniC3 instead of point clouds**
  - Context: Real video movements work better than synthetic 3D data for UniC3
  - *From: mamad8*

- **Use multiples of 16fps for optimal generations**
  - Context: Since Wan is trained on 16fps, use 16, 32, 48fps etc. for best results
  - *From: yi*

- **Don't stack LoRAs on I2V as it changes style**
  - Context: Multiple LoRAs on I2V will alter the visual style
  - *From: hicho*

- **Use PUSA correctly: T2V models + flowmatch_pusa scheduler + frame injection**
  - Context: Many people misuse PUSA with I2V models where it doesn't work properly
  - *From: Kijai*

- **For PUSA extension, use 4+1 rule for frame overlap**
  - Context: When extending videos with PUSA, try 13 frames overlap instead of 12
  - *From: Kijai*

- **Increase PUSA LoRA weight for more adherence to input frames**
  - Context: Higher PUSA LoRA strength reduces motion but increases adherence to provided latents
  - *From: DawnII*

- **Use rank 64 for PUSA LoRA as sweet spot**
  - Context: Based on testing different ranks
  - *From: ZeusZeus (RTX 4090)*

- **Be very clear and specific in prompts for better WAN results**
  - Context: Instead of using LLMs, directly state what you want to see
  - *From: Yayu*

- **Consider structured prompts like VEO3 format**
  - Context: Camera: wide-angle shot, Characters: one running man, Location: suburban street - more detailed structured approach
  - *From: Juan Gea*

- **Use full 81 frames for better continuation coherence**
  - Context: When doing Pusa extensions to avoid quality degradation
  - *From: Kijai*

- **Don't downscale training images to 512**
  - Context: Keep high resolution images at 1080p or 1024, let model downscale automatically
  - *From: Thom293*

- **Use CFG 3.0 for first step in extensions**
  - Context: When doing Pusa video extensions for better results
  - *From: Kijai*

- **Remove overlap frames instead of cross-fading**
  - Context: When combining extended video sequences
  - *From: Kijai*

- **Use Florence to describe input images for prompting**
  - Context: When needing help with prompting, Florence can provide good image descriptions
  - *From: samhodge*

- **Describe individual gym items instead of just 'gym'**
  - Context: When WAN doesn't understand complex scenes like gyms
  - *From: samhodge*

- **Use 'blue glowing plasma around her hand' instead of vague magic terms**
  - Context: For better magical effects generation, be specific about visual elements
  - *From: samhodge*

- **Don't stare at progress bars, wedge it out and leave overnight**
  - Context: For long generation times, better to queue and wait rather than watch
  - *From: samhodge*

- **Use PUSA extension for better video continuations**
  - Context: Alternative to VACE cross-fading which causes quality degradation
  - *From: The Shadow*

- **Apply mask when using MultiTalk for non-talking scenes**
  - Context: MultiTalk affects whole generation even without vocals, masking can help control this
  - *From: DawnII*

- **Always composite inpainting results on top of original**
  - Context: When using differential diffusion/inpainting with WAN
  - *From: Kijai*

- **Use 0.50 denoise for stylizing with T2V model and latent masking**
  - Context: When doing video-to-video stylization with masking
  - *From: hicho*

- **Model patching order rarely matters in general**
  - Context: When setting up LoRA and block swap nodes
  - *From: Kijai*

- **Don't use CausVid with control methods**
  - Context: Lose a lot of control adherence when using CausVid with VACE
  - *From: DawnII*

- **Use NAG to stop characters talking**
  - Context: NAG is exceptional at preventing anime characters from constantly talking in generations
  - *From: Cubey*

- **Try Chinese prompts for better adherence**
  - Context: Translating prompts to Chinese can improve results, though hit or miss
  - *From: MysteryShack*

- **Masking latent works only at denoise 0.55**
  - Context: When using T2V model with masking latent, higher denoise values cause offscreen results
  - *From: hicho*

- **Negative prompts work with CFG 1 when using NAG**
  - Context: Even at CFG 1, negative prompts make big difference when NAG is enabled
  - *From: Drommer-Kille*

- **Use LLM-style detailed prompts for better EchoShot results**
  - Context: Model really needs LLM prompts to work properly
  - *From: Kijai*

- **Include consistent character description across all EchoShot prompts**
  - Context: Need uniting phrase in all prompts for character consistency
  - *From: VK*

- **Use Florence for prompting WAN with still motion**
  - Context: Florence is good at prompting to WAN as long as you give it a shot with still motion, can describe motion if present
  - *From: hicho*

- **Try translating prompts to Mandarin for more precise videos**
  - Context: Chinese prompts may work better with WAN models
  - *From: Sal TK FX*

- **Use precise prompts without prose and filler words**
  - Context: For better generation results with Wan models
  - *From: Yayu*

- **Don't change batch size with small image datasets**
  - Context: Makes training slower with worse results
  - *From: Drommer-Kille*

- **Pre-process control nets to video files to save RAM**
  - Context: Every preprocessor doubles RAM usage by keeping originals in memory
  - *From: Gateway*

- **Connect secondary GPU to monitors to save 2GB VRAM on main GPU**
  - Context: Frees up full VRAM on primary inference GPU
  - *From: Juan Gea*

- **Launch ComfyUI with --reserve-vram 2 for native workflows**
  - Context: Keeps 2GB free for Windows usage when using monitor on same GPU
  - *From: Kijai*

- **Use detailed captions for LoRA training**
  - Context: Use Gemini 2.5 Flash to generate detailed captions, describe scenes not just actions
  - *From: mamad8*

- **Save checkpoints frequently during training**
  - Context: Save every 250-500 steps to avoid overtrained final checkpoints
  - *From: Drommer-Kille*

- **Use dpm++_sde scheduler with lightx2v**
  - Context: LCM also works but is less saturated
  - *From: Kijai*

- **Use native TE on CPU to free 11GB VRAM**
  - Context: When generating high frame counts
  - *From: hicho*

- **For I2I single frame, set rebatch to 1**
  - Context: Set denoise higher if you want motion, can go as low as 1 step for no motion
  - *From: hicho*

- **Blur Blender depth maps for Wan compatibility**
  - Context: Raw Blender depth maps don't work well
  - *From: Kijai*

- **Look at VRAM usage to find sweet spot**
  - Context: If VRAM use is past 95% during generation, that's the sweet spot for that generation
  - *From: Kijai*

- **Close unnecessary applications**
  - Context: Close Steam (takes VRAM) and browsers to free up VRAM for generation
  - *From: hicho*

- **Use TE on CPU with 6gb umt5**
  - Context: When VRAM limited, put text encoder on CPU using the 6gb umt5 version
  - *From: hicho*

- **Raise radical attention decay to 0.4**
  - Context: Default radical attention settings are decent but raising decay to 0.4 improves results
  - *From: MysteryShack*

- **Skip every 2nd frame of source for less morphing**
  - Context: When processing source material, skipping frames reduces morphing artifacts
  - *From: Drommer-Kille*

- **Use context options for infinite frame length**
  - Context: When doing inpaint, VACE, or vid2vid with sufficient VRAM
  - *From: samhodge*

- **Use code versioning for workflows and runtime environments**
  - Context: When being paid to produce reliable output
  - *From: samhodge*

- **Change ComfyUI requirements.txt to prevent transformer updates**
  - Context: To avoid repeated downgrade issues
  - *From: phazei*

- **Use humanlike model with Uni3c to keep character still while changing angle**
  - Context: When wanting to maintain character consistency while changing camera angle
  - *From: Flipping Sigmas*

- **Use JD2 downloader for faster downloads**
  - Context: Downloads from HuggingFace and ModelScope get 10x speed on Windows
  - *From: yi*

- **Use built-in ComfyUI mask editor for masking**
  - Context: When needing to create masks for images in ComfyUI workflows
  - *From: DawnII*

- **You must use both high noise and low noise models together**
  - Context: Try using only one and you'll see why both are needed
  - *From: comfy*

- **Wait for distilled versions if you want speed over quality**
  - Context: Current models prioritize quality, distilled versions will be faster
  - *From: Juampab12*

- **Use complex prompts with lighting and camera framing for better 5B results**
  - Context: When working with the 5B model
  - *From: Gateway {Dreaming Computers}*

- **Model works well at 416x240 if resolution isn't important**
  - Context: For faster generation when high resolution not needed
  - *From: samurzl*

- **Sage attention has bigger quality hit on 5B than other models**
  - Context: When using attention optimizations
  - *From: Kijai*

- **Use 4 steps high noise, 4 steps low noise for optimal results**
  - Context: When using the two-stage 14B model
  - *From: ArtOfficial*

- **Use bf16 version of 2.1 VAE for better outputs**
  - Context: When working with Wan 2.2
  - *From: Jas*

- **Split samplers offer more control - first and second pass may work better with different samplers/schedulers**
  - Context: Using dual high/low noise model setup
  - *From: gokuvonlange*

- **Use 6 steps (3 and 3) when using lightx2v**
  - Context: For optimal results with lightx2v LoRA
  - *From: Shawneau 🍁 [CA]*

- **Use CFG of 1 when using LightX2V LoRA**
  - Context: High CFG causes issues with the LoRA
  - *From: 🦙rishappi*

- **Combine LightX2V with other LoRAs for better performance**
  - Context: 2.2 performs better when multiple LoRAs are used together
  - *From: itok*

- **Try 3+3 or 4+4 step configurations instead of 2+2**
  - Context: Higher step counts may produce better quality
  - *From: multiple users*

- **Use 121 frames at 24fps for optimal results**
  - Context: Template workflow uses these settings
  - *From: multiple users*

- **Don't use 121 frames for 14B model**
  - Context: Use 81 frames at 16fps instead to avoid looping
  - *From: aikitoria*

- **Adjust LightX2V LoRA strengths for better quality**
  - Context: 3 strength first pass, 1.5 strength second pass works better
  - *From: Juampab12*

- **Use static shots with low motion if using 121f**
  - Context: 121f works for static shots but causes issues with high motion
  - *From: Juampab12*

- **Washed out results are better than too much contrast**
  - Context: Easy to add contrast later, impossible to recover lost details
  - *From: Quality_Control*

- **Use uneven step distribution favoring low noise model**
  - Context: Better to put 2/3s of steps to low noise model rather than even split, or use ratios like 1/3 (high/low)
  - *From: JohnDopamine*

- **Use specific LightX strength settings**
  - Context: Try 3.0 strength first pass, 1.5 strength second pass with 2+2, 3+3, or 4+4 steps
  - *From: Juampab12*

- **Avoid using distill model for high noise sampler**
  - Context: Distill model kills motion and cinematic quality on high noise model, use base 2.1 instead
  - *From: slmonker*

- **Use structured prompting for better results**
  - Context: Detailed structured prompts with camera angles, movement, and scene descriptions work well for complex actions like skateboarding
  - *From: Drommer-Kille*

- **Use different seeds for high and low noise samplers**
  - Context: When using dual sampler setup for 2.2
  - *From: Yayu*

- **Add specific ending descriptions to prompts for better looping**
  - Context: Added 'the video ends with a large splash as she starts swimming into the horizon' improved 121 frame looping
  - *From: DawnII*

- **Don't use quantization below Q6 unless lacking RAM**
  - Context: Quality degrades significantly below Q6, better to offload to RAM
  - *From: Kijai*

- **Use torch compilation for 20% speed boost**
  - Context: Free performance improvement, though first run is slower
  - *From: pagan*

- **Split prompts between high and low noise models**
  - Context: Focus on camera and subject motion in first stage, character and environment details in second stage to avoid dilution
  - *From: Ablejones*

- **Use both video and image when sharing results**
  - Context: PNG contains workflow metadata that can be shared, video alone doesn't preserve metadata on Discord
  - *From: Kenk*

- **Be careful with shift when splitting the process**
  - Context: When using dual model setup with high/low noise models
  - *From: Kijai*

- **Use DDMIN in second sampler for better details**
  - Context: Alternative sampler choice for detail enhancement
  - *From: ArtificialMachine*

- **Use euler with custom sigmas to match native flowmatch_causvid**
  - Context: When trying to replicate native sampler behavior
  - *From: Kijai*

- **Set end step to -1 for last step**
  - Context: When configuring sampler end steps
  - *From: Kijai*

- **Bump LightX2V strength to 3.0 for high noise model**
  - Context: For better prompt adherence with 2.2
  - *From: Kijai*

- **Different seeds on second pass act like variations**
  - Context: Gives similar but slightly different results
  - *From: Draken*

- **Use VACE strength 4.0 for high-noise model section**
  - Context: When using VACE controls for better results
  - *From: Ablejones*

- **Wouldn't go below Q4 quantization or quality gets horrible**
  - Context: When using quantized models
  - *From: Kijai*

- **Train LoRAs on just 512 resolution even for T2V 14B**
  - Context: Training character LoRAs - learns faster and still works great for higher res like 1280x720
  - *From: gokuvonlange*

- **Remove duplicate backgrounds and outfits from training dataset**
  - Context: Training character LoRAs - similar backgrounds bleed into the LoRA even with good captions
  - *From: gokuvonlange*

- **Use learning rate 0.0001 and train for 2000-3000 steps**
  - Context: Training LoRAs with 20 images
  - *From: gokuvonlange*

- **Can do two-pass generation: low-res Wan 2.2 first pass, then high-res Wan 2.1 pass**
  - Context: For faster generation while maintaining quality
  - *From: VRGameDevGirl84(RTX 5090)*

- **Use FastWan 0.4 + FusionX 0.4 + LightX2V 0.4 combination**
  - Context: Helps significantly with T2V quality
  - *From: mamad8*

- **Don't use LightX2V on high noise pass**
  - Context: Use LightX2V only on low noise pass at 0.85-1.0 strength to avoid overblurring/oversaturation
  - *From: Vardogr*

- **Set Windows to performance mode**
  - Context: Can help with generation speed issues, lots of Windows tweaks available for better performance
  - *From: Charlie*

- **Use VACE with Wan 2.1 first before trying with 2.2**
  - Context: Wan 2.2 doesn't respond to VACE the same way, especially high-noise model
  - *From: Ablejones*

- **Both samplers need same step count**
  - Context: If aiming for 8 steps total, both samplers should be set to 8 steps
  - *From: Jonathan*

- **Use gpu-only flag for faster loading**
  - Context: Even if it OOMs initially, disk cache will make subsequent loads faster
  - *From: MysteryShack*

- **Use 16fps instead of 24fps for 14B model**
  - Context: 24fps makes motion look worse and causes slow-motion appearance
  - *From: Jonathan*

- **Set LoRA strength to 2.0 for LightX2V, 1.0 will cause blurry mess**
  - Context: When using speed LoRAs with Wan 2.2
  - *From: Jonathan*

- **Use radial attention for faster generation**
  - Context: Good for users who want to avoid slow generation times
  - *From: MysteryShack*

- **Different LoRA strengths for high vs low noise passes**
  - Context: High noise model requires stronger LoRA strength than low noise
  - *From: Kijai*

- **Higher rank LoRAs are slightly stronger**
  - Context: When choosing between different LoRA variants
  - *From: Kijai*

- **Use radial attention only on low noise (second pass) for better results**
  - Context: Radial attention can hurt motion with high noise model
  - *From: Kijai*

- **Use detailed prompts expanded with ChatGPT for better results**
  - Context: Model responds well to elaborate descriptions
  - *From: VK*

- **For video-driven motion, use denoise on first sampler only**
  - Context: Using denoise on second sampler produces junk noise
  - *From: VK*

- **LightX2V strength should be at least 3.0 on high noise**
  - Context: Bad things happen when strength is lower than 3 on high noise
  - *From: MysteryShack*

- **You can use low noise model only but you can't use high noise model only**
  - Context: When setting up dual sampler workflow
  - *From: Kijai*

- **VACE works very badly with the high noise model, at least start frame or reference**
  - Context: When using VACE with 2.2 models
  - *From: Kijai*

- **Try adding 慢动作 (slow motion) to negative prompt**
  - Context: May help with motion generation
  - *From: kendrick*

- **Use block swap to offload to CPU and max all blocks**
  - Context: For VRAM management with large models
  - *From: hicho*

- **Set different CFG values per step for better motion**
  - Context: Use 2.0 for first step, 1.0 for rest to kickstart motion and prompt adherence
  - *From: Kijai*

- **Don't use too much CFG with high LoRA strength**
  - Context: Will burn the output, and CFG steps take twice as much time
  - *From: Kijai*

- **Use LightX2V LoRA at strength 3 on HIGH and strength 1 on LOW**
  - Context: For faster generation with good results
  - *From: gokuvonlange*

- **Lower CFG to 1 when using LightX LoRA**
  - Context: CFG 3.5 with LightX creates overcooked look and takes more time
  - *From: gokuvonlange*

- **Don't go past 81 frames**
  - Context: Motion quality degrades significantly beyond 81 frames
  - *From: Kijai*

- **Minimize browser windows during generation**
  - Context: 10-20% speed boost when minimizing ComfyUI browser or switching tabs
  - *From: Ablejones*

- **Use torch.compile for VRAM savings**
  - Context: Helps significantly with VRAM usage, alternative is chunked rope function
  - *From: Kijai*

- **Character LoRAs benefit from higher weight on high noise model**
  - Context: Similar to LightX2V, character LoRAs need higher strength on high noise pass
  - *From: hablaba*

- **Be careful with radial sage attention on high noise model**
  - Context: May not even use it on high noise model, can cause issues
  - *From: Kijai*

- **Use quantile estimation for scale calculation to prevent outliers**
  - Context: When using scaled models to improve quantization quality
  - *From: Kijai*

- **Remove first 5 frames from 121 frame generations**
  - Context: To get clean 6 second videos from 7 second generations
  - *From: Kenk*

- **New LoRAs should be trained specifically on high-noise model**
  - Context: Low-noise model works fine with old LoRAs but high-noise needs specific training
  - *From: Ablejones*

- **Turn off 'Offload to CPU' setting if experiencing OOM**
  - Context: Helps prevent out of memory issues during generation
  - *From: N0NSens*

- **Use swap file for memory management**
  - Context: Increase swap file to 500GB if you have disk space to avoid system memory OOM
  - *From: Ablejones*

- **Use different seeds for High/Low samplers**
  - Context: Prevents output loops in generation
  - *From: JohnDopamine*

- **Download PNG workflows correctly from browser**
  - Context: Don't download as webp, use console inspector or drag from Discord app to ComfyUI
  - *From: Kenk*

- **Use ProRes for highest quality post-processing**
  - Context: ProRes HQ avoids compression artifacts, though overkill for 8-bit source
  - *From: rryyaann*

- **Set CRF value to 10 for MP4**
  - Context: Decreases compression artifacts while maintaining reasonable file size
  - *From: Dream Making*

- **Use different shift values between high and low noise models**
  - Context: For better control over generation characteristics
  - *From: CJ*

- **Test generations with only high-noise model vs only low-noise model**
  - Context: To understand the difference between the two models
  - *From: Ablejones*

- **Run generations in background for long fp16 renders**
  - Context: When doing 25+ minute generations, let them run while working on other things
  - *From: aikitoria*

- **Use 81 frames as the sweet spot**
  - Context: Going above causes issues, 81 frames works well for most use cases
  - *From: Samy*

- **Run full 40 samples to avoid grid stepping artifacts**
  - Context: Low sample count videos have weird grid stepping artifacts that disappear with proper sampling
  - *From: aikitoria*

- **Use similar prompts for character consistency with Dreamina model**
  - Context: With Dreamina model, similar prompts generate similar characters
  - *From: slmonker(5090D 32GB)*

- **Generate at 144p for quick testing of LoRAs and models**
  - Context: Good for seeing if a LoRA or model works before full generation
  - *From: patientx*

- **Disable high pass and add LightX2V LoRA at 2 steps**
  - Context: Alternative workflow approach
  - *From: Rainsmellsnice*

- **Update WanVideoWrapper with git pull for Wan 2.2 support**
  - Context: No new dependencies needed if wrapper already working
  - *From: Kijai*

- **Use Q4_K_M quantization for both high and low noise models**
  - Context: For GGUF models to balance quality and VRAM usage
  - *From: thaakeno*

- **Leave prompt blank to see how image is being interpreted**
  - Context: Good for understanding model's interpretation in I2V
  - *From: Daflon*

- **Sequential events can be established with commas instead of numbering**
  - Context: For creating timeline-based prompts
  - *From: Cubey*

- **Use 7 seconds at 24fps or 10 seconds at 16fps maximum**
  - Context: For stable generation without issues
  - *From: Juan Gea*

- **Use block swap with 40 blocks for 64GB RAM setups**
  - Context: When running Wan 2.2 to avoid OOM errors
  - *From: VK (5080 128gb)*

- **Run largest model your machine supports that produces images in reasonable time**
  - Context: When choosing between quantization levels
  - *From: Daflon*

- **Disable non_blocking on block swap when using wrapper**
  - Context: To properly handle memory management
  - *From: Kijai*

- **Cache prompt and don't load T5 for actual run to save RAM**
  - Context: When running context workflows to reduce memory usage
  - *From: Kijai*

- **Save/load latent instead of chaining samplers**
  - Context: To reduce memory usage in complex workflows
  - *From: Kijai*

- **Use Chinese negative prompt: 'bright colors, overexposed, static, blurred details, subtitles, style, artwork, painting, picture, still'**
  - Context: For better prompt adherence
  - *From: Jackie*

- **Use FastWan and LightX2V together for enhanced results**
  - Context: Allows lower LightX2V strength and enables 2-step generation
  - *From: phazei*

- **Use higher lora strength for the high noise model**
  - Context: Helpful for better results, even 3.0 strength
  - *From: Kijai*

- **Use 81 frames to rule out issues**
  - Context: Better for motion anyway
  - *From: Kijai*

- **Most basic way to interpolate is doing 3x and then getting every 2nd frame to end up with 24fps**
  - Context: For frame interpolation
  - *From: Kijai*

- **Use rank 256 if you have high VRAM, rank 64 for low VRAM**
  - Context: For LightX2V LoRA selection
  - *From: thaakeno*

- **Use NAG (Negative Augmented Generation) always for CFG 1, especially on high noise model**
  - Context: Prevents anatomical warping and people merging
  - *From: Ant*

- **Balance the two models - high noise for motion concepts, low noise for visual refinement**
  - Context: The balance of steps between high and low has huge effects on results
  - *From: Draken*

- **If getting bad results, remove all speedup loras from high and run with 10 steps and normal cfg**
  - Context: Produces good motion around 80% of time
  - *From: Ant*

- **For low model, lightx2v is okay with more steps giving better quality, diminishing returns start at 12/6**
  - Context: Step optimization for low noise model
  - *From: Ant*

- **Don't use distill lora on high noise model**
  - Context: Preserves 2.2's superior motion and prompt following capabilities
  - *From: gokuvonlange*

- **Use higher VACE strength for better consistency**
  - Context: 1.5 strength prevents sudden background changes vs 1.0
  - *From: seitanism*

- **Don't touch the high noise model**
  - Context: Best practice for maintaining 2.2 quality
  - *From: slmonker(5090D 32GB)*

- **Generate seeds using only high noise sampler first**
  - Context: To better understand what the high noise model does before using both samplers
  - *From: gokuvonlange*

- **Use enhance node only on low noise side**
  - Context: Enhance makes more sense on the low noise side only, applying to both causes issues
  - *From: Kijai*

- **Stick to 81 frames for best results**
  - Context: Using frame counts other than 81 often causes issues like dark frames at start
  - *From: Draken*

- **Use context windows with persistent control**
  - Context: Context windows work best with some sort of control that persists through all frames, as T2V with same prompt tends to create similar starting points
  - *From: Kijai*

- **Use at least 1 step with CFG > 1 for HighNoise model**
  - Context: For better prompt adherence and quality
  - *From: Ablejones*

- **Don't add LightX2V LoRA to HighNoise model at high strength**
  - Context: Reduces vibrancy and wan magic, better to keep raw model
  - *From: gokuvonlange*

- **Use blank negative with caution**
  - Context: Standard negative prompt is still needed for quality results
  - *From: DawnII*

- **FastWAN + LightX2V combination works well**
  - Context: Some users report better results with this combo
  - *From: gokuvonlange*

- **Split high noise samplers with different CFG values**
  - Context: Use few steps with CFG, then steps with CFG=1, then low noise model for better composition
  - *From: TK_999*

- **5B model works better at higher resolutions like 1024**
  - Context: For getting decent faces and avoiding weird motion
  - *From: TK_999*

- **Use CausVid LoRA for speed boost**
  - Context: Can improve generation time significantly
  - *From: VK (5080 128gb)*

- **Try 161 frames instead of 121 for longer videos**
  - Context: Works better for avoiding obvious glitches
  - *From: aikitoria*

- **Keep denoise at 1.0 and increase start step instead**
  - Context: New vid2vid implementation works differently
  - *From: Kijai*

- **Put 'running' in negative prompt to improve flying animations**
  - Context: When generating flying characters that look like running through air
  - *From: seitanism*

- **Use start step close to split value for subtle changes in vid2vid**
  - Context: When you want minimal changes to input video
  - *From: VK (5080 128gb)*

- **Lower shift makes less change in vid2vid**
  - Context: For more conservative transformations
  - *From: Kijai*

- **Use 129 frames at 25fps and trim 1 latent for final output**
  - Context: Results in 125 frames ultimately
  - *From: JohnDopamine*

- **Increase Uni3C strength significantly for WAN 2.2**
  - Context: Need strength of 3.0, much higher than usual
  - *From: Kijai*

- **Try 161 frames instead of 121 for better results**
  - Context: Using original sampling config at 40 steps
  - *From: aikitoria*

- **Use add_noise_to_samples option with start_step 2**
  - Context: When having trouble getting good V2V results
  - *From: Kijai*

- **Start earlier (lower start_step) to get bigger changes but color changes are tough**
  - Context: When trying to change colors in V2V without changing everything else
  - *From: Kijai*

- **For 3x interpolation to 24fps, drop every 2nd frame using 'select every nth image' node**
  - Context: When converting 16fps to 24fps with RIFE
  - *From: seitanism*

- **Use different backgrounds/settings for better scene transitions**
  - Context: When using scene-based prompting methods
  - *From: 🦙rishappi*

- **More steps on high noise, fewer on low noise when not using distill LoRAs on high side**
  - Context: When removing distill LoRAs from high noise sampler
  - *From: Kijai*

- **Use different seeds and prompts for each context window**
  - Context: When using context windows for long video generation
  - *From: Kijai*

- **Save at 24fps to avoid slow motion look**
  - Context: When generating appears too slow at 16fps
  - *From: Kijai*

- **Don't use TCFG when cfg is 1 or lower**
  - Context: TCFG should only be used when cfg > 1
  - *From: IceAero*

- **Generate image with same model for better I2V results**
  - Context: All these models work better with I2V when you generate the input image with the same model
  - *From: fredbliss*

- **Use dot notation or structured prompts**
  - Context: Compressed structured prompts work better than verbose scene descriptions
  - *From: fredbliss*

- **Keep sage always on for both 2.2 passes**
  - Context: Given the models switcharoo between high and low noise
  - *From: Kijai*

- **Use no lightx on high noise with cfg for better prompt adherence**
  - Context: Since lightx is not optimized for 2.2 yet
  - *From: Juampab12*

- **For I2V keep High noise untouched for now**
  - Context: I2V works best keeping High noise untouched while T2V works well with quantile_0.15
  - *From: gokuvonlange*

- **Try 10/10 steps and 3/3 or 3.5/3.5 cfg instead of 25/25**
  - Context: To avoid overkill and burnt/cartoony results
  - *From: seitanism*

- **Don't use high noise model for upscale part**
  - Context: Just do normal v2v when upscaling generated video
  - *From: Kijai*

- **Use one additional step to offset fp8 quality loss**
  - Context: When using scaled fp8 models for speed boost
  - *From: Kijai*

- **For 4090 users, use fp8 scaled over GGUF for better speed**
  - Context: 4090 has hardware acceleration for fp8 math
  - *From: thaakeno*

- **Use cfg 3.5 on high pass instead of loras to avoid quality issues**
  - Context: When getting artifacts with lora usage
  - *From: Juampab12*

- **Avoid using 2.1 loras on 2.2 for professional work**
  - Context: Significant quality loss especially at 720p resolution
  - *From: lovis.io*

- **Use CFG 2 max with LightX LoRA**
  - Context: Anything above CFG 2 with lightx lora gives artifacts or overcooked contrast
  - *From: gokuvonlange*

- **Test CFG on complex motion**
  - Context: Simple camera push-in works at every cfg, need complex motion to properly test cfg settings
  - *From: N0NSens*

- **Use 14B at 720p then upscale with 5B**
  - Context: Generate at 720p with 14B, then upscale and resample in 5B with 0.2 denoise to avoid 14B limitations
  - *From: Juan Gea*


## News & Updates

- **sage++ update added to main repo**
  - Windows wheel available for sage++ mode, only enabled on sm89 (4000 series) in their code
  - *From: Kijai*

- **KJ updated wrapper to work with VACE**
  - Latest changes make wrapper work with VACE, but breaks old workflows by rearranging image and text embed positions
  - *From: Guey.KhalaMari*

- **Wan 2.2 release in 2 weeks**
  - Confirmed timeline from conference, will remain open source
  - *From: slmonker(5090D 32GB)*

- **Wan 2.5/3.0 might release in October**
  - Huge update planned, still confirmed as open source model
  - *From: slmonker(5090D 32GB)*

- **ThinkSound video-to-audio model released**
  - New model from Wan team for generating audio from video
  - *From: yi*

- **OmniAvatar released 2 weeks ago**
  - New avatar generation system, requires about 20GB VRAM
  - *From: Tango Adorbo*

- **SAGEATT 2 hacked to work on older GPUs**
  - Community member working on compatibility for older hardware
  - *From: hicho*

- **Sage Attention 2.2++ released**
  - New version available on GitHub with potential improvements for RTX 40xx and 50xx
  - *From: chancelor*

- **FusionX officially recognized**
  - Mentioned in official context with spoiler alert
  - *From: izashin*

- **Wan 2.2 coming in approximately 2 weeks**
  - Requires 10 steps according to upcoming model info
  - *From: yi*

- **ComfyUI frontend update caused compatibility issues**
  - Broke get/set nodes requiring downgrade
  - *From: Kijai*

- **AniSora V3 preview announced by BiliBili**
  - Will share progress at Siggraph on 07/11, V2 was never publicly released
  - *From: DevouredBeef*

- **Multitalk branch not yet merged to main**
  - Still in development branch, not available in main branch yet
  - *From: Kijai*

- **MediaSyncer v0.2 released**
  - Added zoom/pan functionality, playback speed control, updated UI with icons and improved appearance
  - *From: Jonathan*

- **GGUF versions of MAGREF released**
  - First GGUF for that model available at quantstack
  - *From: mdkb*

- **Block conditioning custom node will be released**
  - nah it's a custom node, ill publish it later today if you want to try it out
  - *From: Mads Hagbarth Damsbo*

- **Box mode added to Florence2 mask separation node**
  - added box mode to this node as it was very simple thing to do
  - *From: Kijai*

- **Kyutai TTS released**
  - released just in time to use with MT lol https://kyutai.org/next/tts
  - *From: DawnII*

- **Kijai merged MultiTalk to main branch**
  - MultiTalk now available in version 1.2.1 of WanVideo wrapper
  - *From: Kijai*

- **Omni-Avatar released 1.3B version**
  - Works on 8GB VRAM according to GitHub issue example
  - *From: mdkb*

- **Radial Attention now supports Wan2.1_14B_FusionX LoRA**
  - Can get high-quality videos in just 8 steps (100 seconds on H100), from Stanford/MIT/Nvidia/Berkeley team
  - *From: ZeusZeus (RTX 4090)*

- **LightX2V updated with audio conditioning support**
  - Recent commit shows audio model integration, may have ties to Wan 2.2 release
  - *From: ZeusZeus (RTX 4090)*

- **MultiTalk now works with MagRef in latest build**
  - Previously had compatibility issues but now functional with the recent updates
  - *From: Draken*

- **Kijai considering making unified patcher node for native ComfyUI**
  - Would serve as similar sandbox to the wrapper, addressing compatibility issues with teacache, NAG etc.
  - *From: Kijai*

- **Radial attention available for diffusers version of WAN**
  - MIT Han Lab released radial attention implementation
  - *From: MysteryShack*

- **VRGameDevGirl84's custom node available in ComfyUI Manager**
  - First custom node now available through the manager
  - *From: VRGameDevGirl84(RTX 5090)*

- **GGUF support added to WanVideoWrapper**
  - Works with T2V, I2V and VACE, supports LoRA loading without merging, works with blockswap
  - *From: Kijai*

- **MultiTalk runs with GGUF as main model**
  - Confirmed working with GGUF quantized models
  - *From: Kijai*

- **Wallace and Gromit LoRA released for 14B model**
  - New character LoRA available
  - *From: Cseti*

- **BAAI MTVCraft model announced**
  - New model from BAAI, though appears to have quality issues compared to MultiTalk
  - *From: DawnII*

- **GGUF support added to Wan wrapper**
  - Allows using quantized models with lora support
  - *From: multiple users*

- **High speed dynamic lora noise issue fixed**
  - LoRA calculations now done in fp32 to prevent noise at full strength
  - *From: Kijai*

- **MTVCraft GitHub updated**
  - New framework for music-to-video generation, HF demo added
  - *From: JohnDopamine*

- **FreeInit support added to wrapper with sample chaining capability**
  - If samples provided, skips first iteration and uses samples instead
  - *From: Kijai*

- **LoRA alpha scaling bug fixed in wrapper**
  - Problem was scaling wasn't implemented in weight calculation
  - *From: Kijai*

- **Debugging output accidentally left in wrapper, now removed**
  - Was causing console messages on every generation
  - *From: Kijai*

- **VACE start/end frame node logic updated**
  - Fixed padding issues and added index positioning functionality
  - *From: Kijai*

- **LightX2V repository active with recent commits**
  - Multiple commits suggesting potential release preparation
  - *From: JohnDopamine*

- **ThinkSound project receiving active development**
  - Recent updates to fix audio generation issues
  - *From: Bingo*

- **Wan Knowledge Base and chatbot created**
  - Comprehensive knowledge base with NotebookLM chatbot for full channel logs
  - *From: JohnDopamine*

- **Improved and faster TeaCache released**
  - New version with code available at https://github.com/zishen-ucap/PromptTea
  - *From: yi*

- **Kijai added chunked RoPE calculation option**
  - Alternative function that processes RoPE in chunks to reduce VRAM usage for users not using torch.compile
  - *From: Kijai*

- **VRGameDevGirl84 released WanFusionXFaceNaturalizer lora**
  - New lora that smooths out detail loras baked into FusionX model, helps make faces more natural at 0.7 strength
  - *From: VRGameDevGirl84(RTX 5090)*

- **Index-anisora anime I2V model officially released**
  - WAN I2V finetuned model for anime, available as fp8 version from Kijai
  - *From: DawnII*

- **GGUF support added to WanVideoWrapper**
  - Can now use GGUF models directly in wrapper workflows for better VRAM management
  - *From: mdkb*

- **SageAttention enabled for VACE**
  - 20% speed improvement after Kijai fixed missing attentionmode argument
  - *From: Kijai*

- **Kijai added GGUF support to Wan wrapper**
  - GGUF format now supported in wrapper, showing significant performance improvements
  - *From: Multiple users*

- **Sage attention improvements in dev branch**
  - Performance improvements available in dev branch only, not main branch yet
  - *From: DawnII*

- **Adrien Toupet released new SeedVR2 Deep Dive video**
  - 3-week project covering one-step video upscaling with BlockSwap technique
  - *From: Adrien Toupet*

- **ThinkSound audio generation model released**
  - New audio generation model from FunAudioLLM, but early reports suggest poor quality
  - *From: Multiple users*

- **Wan Video Wrapper dev merged to main with major improvements**
  - Fix VACE to use sageattention (~20% faster), chunked more things when chunked RoPE enabled for drastically reduced VRAM, model code refactoring
  - *From: Kijai*

- **Open-OmniVCus released with Wan support**
  - Context for videos with trajectory control, does many video editing tasks
  - *From: hicho*

- **New LightX2V models uploaded**
  - Wan2.1-T2V-14B-Lightx2v and Wan2.1-I2V-14B-720P-Lightx2v appeared on HuggingFace but details unclear
  - *From: yi*

- **chinese-wav2vec2-base-fairseq-ckpt.pt no longer needed for MultiTalk**
  - File is not actually used and can be safely deleted, updated code to not download it anymore
  - *From: Kijai*

- **New transition node created for scene transitions**
  - Made new node that's simpler and supports other transitions for connecting multiple scenes
  - *From: Kijai*

- **Pusa V1 for Wan 2.1 released**
  - Claims 200x cheaper training, supports vectorized timesteps
  - *From: yi*

- **Index-anisora 14B model available**
  - HuggingFace repo with 14B model
  - *From: Ada*

- **Sharp version of SeedVR2 7B released**
  - More edge sharpening variant available
  - *From: DawnII*

- **EchoShot preview built off 1.3B**
  - New model preview available
  - *From: DawnII*

- **Q8_0 quantized versions available**
  - Can use with regular wan workflows
  - *From: Hashu*

- **New LightX2V LoRAs released**
  - Rank64 LoRAs for both T2V and I2V models available, though T2V version has issues
  - *From: slmonker(5090D 32GB)*

- **PUSA video generation model announced**
  - New model from Yaofang-Liu with thousands timesteps video diffusion
  - *From: VRGameDevGirl84(RTX 5090)*

- **ALG framework released for I2V with LTX and WAN**
  - New research framework for improving I2V generation speed and quality
  - *From: hicho*

- **New distilled models released**
  - Wan2.1-I2V-14B-480P-StepDistill-CfgDistill-Lightx2v and T2V variants with 2-4 step generation
  - *From: hicho*

- **LightX2V LoRAs updated**
  - Both T2V and I2V LoRAs updated, T2V still having issues but I2V works well
  - *From: CJ*

- **GGUF support now working in wrapper**
  - Kijai's wrapper now supports GGUF with more code attention than native
  - *From: mdkb*

- **Wan 2.2 expected this month according to developers**
  - Wan devs saying Wan 2.2 should be released this month
  - *From: Ada*

- **PUSA model released - Wan finetune with 120GB disk space requirement**
  - New model with improved I2V performance but heavy installation requirements
  - *From: multiple users*

- **Wan team created their own ComfyUI wrapper**
  - Released ComfyUI-Lightx2vWrapper on GitHub, though somewhat redundant to existing solutions
  - *From: Kijai*

- **Bad LightX2V LoRA fixed on official site**
  - Official site had problematic LoRA early in day, fixed versions now available
  - *From: The Shadow (NYC)*

- **Pusa LoRA extracted and made available by Kijai**
  - Wan21_PusaV1_LoRA_14B_rank512_bf16.safetensors now available on Kijai's HuggingFace
  - *From: Kijai*

- **New LightX2V LoRAs available in multiple ranks**
  - I2V (480 flavor) and T2V (720) versions available in ranks 16, 32, 64, 128
  - *From: The Shadow (NYC)*

- **Pusa lora released**
  - 4.9GB rank512 lora that turns T2V model into I2V and more
  - *From: Kijai*

- **Echoshot mentioned in updated Wan 2.1 readme**
  - Readme updated 3 hours ago with Echoshot reference
  - *From: Gill Bastar*

- **Radial Attention now compatible with SageAttention version 1**
  - Recent compatibility update
  - *From: Lumi*

- **Radial attention implementation added to experimental branch**
  - Hardcoded to 10 dense steps initially, needs Sparse_SageAttention_API installed
  - *From: Kijai*

- **New chunked rope_function added to sampler node**
  - Reduces memory usage significantly
  - *From: Kijai*

- **WanVideoWrapper node names updated**
  - Empty embeds node now called 'extra latents' instead of 'first latents'
  - *From: Hashu*

- **Radial attention now in main WanVideoWrapper**
  - Can be faster but affects quality. Need to balance start step and quality settings
  - *From: Kijai*

- **Sparse SageAttention API integrated**
  - No need to install separately anymore, sparse API code included
  - *From: Kijai*

- **PusaV1 models updated**
  - Updated 40 minutes ago with their own LoRA extract
  - *From: JohnDopamine*

- **New adaptive rank LoRA released**
  - lightx2v_14B_T2V_cfg_step_distill_lora_adaptive_rank_quantile_0.15_bf16.safetensors uses layer-by-layer adaptive ranks like lycoris/locon
  - *From: Kijai*

- **Radial attention implementation added to wrapper**
  - Promises faster WAN generations with settings for dense timesteps and decay factor
  - *From: MysteryShack*

- **New rank 256 LightX2V LoRA available**
  - lightx2v_T2V_14B_cfg_step_distill_v2_lora_rank256_bf16.safetensors released
  - *From: Kijai*

- **Radial Sage Attention mask caching bug fixed**
  - Fixed bug that didn't reset the cached mask on resolution change
  - *From: Kijai*

- **New samplers added to wrapper**
  - Euler ancestral and other samplers being considered for addition to WanVideoWrapper
  - *From: Kijai*

- **Kijai added radial attention custom block select**
  - Can now select any dense block instead of just number from start for more advanced experimentation
  - *From: Kijai*

- **Scaled model support with unmerged LoRAs**
  - Can now disable lora merging on normal models, so LoRAs are used in full precision with no loading time
  - *From: Kijai*

- **Fixed important radial attention bugs**
  - Fixed bugs that screwed up radial attention if you changed resolution
  - *From: Kijai*

- **Possible new Hunyuan video model in development**
  - Pusa developer suggested on Twitter that Hunyuan has another video model in the oven
  - *From: JohnDopamine*

- **ARC-Hunyuan-Video got initial commit on Tencent's HF**
  - Possibly a new video understanding/multimodal model rather than generation
  - *From: JohnDopamine*

- **Major LoRA system overhaul**
  - New support for fp8 scaled models with unmerged loras, normal models with unmerged loras, instant lora weight changes, and reduced LoRA merging RAM use
  - *From: Kijai*

- **Upcoming LoRA controls on the fly**
  - Next feature will be controls for the loras on the fly, allowing timestep scheduling or even strength curves over time
  - *From: Kijai*

- **New VACE+Phantom combination node**
  - New node created that combines VACE and Phantom with extra control on the values of the vace conditioning tensors that overlap with phantom embeds
  - *From: Ablejones*

- **New fp8_scaled_kj models released**
  - Better quality fp8 models that are closer to fp16, moved to new repo at huggingface.co/Kijai/WanVideo_comfy_fp8_scaled
  - *From: Kijai*

- **Flowmatch_pusa scheduler now in main branch**
  - PUSA scheduler available in main branch of wrapper
  - *From: Kijai*

- **Triton installation much easier now**
  - Don't even need to install triton manually anymore, woct0rdho has pre-built wheels
  - *From: Kijai*

- **WanWrapper update includes 0 strength LoRA check**
  - Now skips loading LoRAs set to 0 weight, improving performance
  - *From: Kijai*

- **PyTorch 2.7 provides 20% performance boost**
  - Free 20% boost from fast fp16 with 16 accumulation for users still under that version
  - *From: Kijai*

- **Radial attention now has sparse attention code path for sageattention2**
  - New optimization that may affect character transfer
  - *From: MysteryShack*

- **Sparse SageAttention 2.0 released**
  - Available from radial attention dev, requires compilation, automatically used if installed
  - *From: Kijai*

- **Text encoder disk caching added to wrapper**
  - Stores cached embeddings to avoid re-encoding unchanged prompts after restarts
  - *From: Kijai*

- **LightX LoRA compatibility fixes**
  - Head layer skipped to resolve tuple errors with certain LoRA weights
  - *From: Kijai*

- **Kijai added Uni3C support to context windows**
  - New experimental feature for longer videos with camera control
  - *From: Kijai*

- **Wan 2.2 expected soon but delayed**
  - Was supposed to release last week but no official date confirmed
  - *From: Charlie*

- **Kijai will convert 720p I2V model later**
  - Currently working on scaled version of 720p model
  - *From: Kijai*

- **New WanVideo cache improvements**
  - Changed cache to handle positive and negative separately, made T5 input optional so you can disable T5 loading if prompts already encoded
  - *From: Kijai*

- **OmniAvatar-14B model released**
  - New 14B model available on HuggingFace, appears to be audio-conditioned
  - *From: hicho*

- **FastVideo models available**
  - Wan FastVideo models on HuggingFace - 1.3B populated with files, 14B t2v still processing
  - *From: JohnDopamine*

- **Wan 2.2 information revealed**
  - Wan 2.2 is just Wan 2.1 with RL applied, same architecture, planned for end of July with possible delays to August
  - *From: yi*

- **SeedVR GGUF quantization available**
  - GGUF quantization for SeedVR video upscaler released
  - *From: Alisson Pereira*

- **Wan audio implementation in progress**
  - LightX2V team working on official Wan audio implementation with audio scheduler in code
  - *From: hicho*

- **T5 input made optional for cached prompts**
  - T5 encoder doesn't need to be loaded if prompt is already cached
  - *From: Kijai*

- **FastWan 1.3B model converted to ComfyUI format released**
  - Available on HuggingFace as Wan2_1-T2V_FastWan_1_3B_bf16.safetensors
  - *From: Kijai*

- **WAN 2.2 in alpha testing with T2I, T2V, and I2V**
  - No NDA but alpha doesn't represent final results. Uses RL training, no distilled version yet. Same architecture as 2.1 but with reinforcement learning
  - *From: 青龍聖者@bdsqlsz*

- **YUME I2V model released at 540p**
  - Autoregressive approach similar to framepack, 720p version upcoming, trained only on street/drone footage
  - *From: DawnII*

- **SageAttention 3 signup available but not yet distributed**
  - Form filled out but no response yet, Apache license so one person getting access could share
  - *From: aikitoria*

- **Wan 2.2 officially teased by Alibaba**
  - Official Twitter account posted teaser suggesting imminent release
  - *From: A.I.Warper*

- **Fast Wan 1.3B model now available**
  - Kijai added fast Wan 1.3B model to ComfyUI implementation
  - *From: patientx*

- **WAN 2.2 could be released in a few hours**
  - Insider information suggesting imminent release
  - *From: 青龍聖者@bdsqlsz*

- **Sage Attention 3 released with fp4 support**
  - New version available as separate package, suggests 2x speed improvement using fp4 cores
  - *From: aikitoria*

- **WAN 2.2 will have different aesthetics due to RL effects**
  - Reinforcement learning effects will change the visual style, making it more Midjourney-like
  - *From: 青龍聖者@bdsqlsz*

- **NABLA optimization released for WAN 2.1**
  - 50% inference time reduction available on Hugging Face
  - *From: DawnII*

- **Wan 2.2 heavily teased with new demo videos**
  - Alibaba posted 3 new 5-second videos showing improved motion and camera control, but no official release yet
  - *From: izashin*

- **New LightX2V version released**
  - They released new version recently that has better motion, and separate I2V version as well
  - *From: Kijai*

- **Kling Elements updated**
  - There was an update to kling elements with new features
  - *From: aikitoria*

- **FastWan 14B model released**
  - FastVideo released FastWan 14B models on HuggingFace
  - *From: JohnDopamine*

- **Kijai converted FastWan to LoRA format**
  - Converted FastWan to LoRA format and uploaded scaled fp8 versions
  - *From: Kijai*

- **Wan 2.2 alpha testing ongoing**
  - Community member has access to Wan 2.2 website for testing
  - *From: 青龍聖者@bdsqlsz*

- **WAN 2.2 might release during WAIC conference**
  - China hosting World Artificial Intelligence Conference, Chinese time Saturday to Monday. Would be first model release on weekend
  - *From: 青龍聖者@bdsqlsz*

- **New WAN 2.2 tease posted**
  - Alibaba posted colorful and crisp teaser, hoping it's not just merged with MPS LoRAs
  - *From: hicho*

- **EchoShot model released by JonneyWang**
  - 1.3B model for multi-scene character consistency, community interest may lead to 14B version
  - *From: hicho*

- **Wan 2.2 releasing January 28th at 8PM Beijing time**
  - Equivalent to 7AM ET in US, announced on Twitter
  - *From: Siraj*

- **Wan 2.2 uses same VAE as previous versions**
  - Ecosystem conversion should be easy
  - *From: 青龍聖者@bdsqlsz*

- **Wan 2.2 will have zero-day ComfyUI support**
  - If architecture hasn't changed, it will work immediately like any 2.1 finetune
  - *From: Kijai*

- **Wan 2.2 code discovered**
  - Found in DiffSynth Studio commit with 5B model and new VAE architecture
  - *From: Kijai*

- **Multiple ComfyUI devs added to Wan-AI HuggingFace org**
  - Wasn't the case 2 weeks before, possibly developing workflows
  - *From: yi*

- **Wan 2.2 announcement expected tomorrow**
  - Based on livestream announcements
  - *From: community*

- **Wan 2.2 release scheduled for tomorrow**
  - 20:00 Beijing time (15 hours from discussion), will include 5B model and possibly VACE
  - *From: multiple users*

- **New NABLA attention method available**
  - Cuts inference time in half using new attention, models released on HuggingFace
  - *From: phazei*

- **Prompt caching feature added**
  - New feature caches prompts (4MB per prompt) so T5 doesn't need to load to RAM again for same prompts
  - *From: Kijai*

- **Wan 2.2 release scheduled for July 28, 2025 at 20:00 Beijing time**
  - Official announcement from Alibaba_Wan X account
  - *From: JohnDopamine*

- **Wan 2.2 specifications revealed in DiffSynth commit**
  - A14B model uses high/low noise expert split, 5B model has unified TI2V architecture
  - *From: JohnDopamine*

- **Kijai has no pre-access to Wan 2.2 model**
  - Contradicts expectations that he would have early access
  - *From: Kijai*

- **Wan 2.2 models releasing during livestream**
  - Multiple Wan 2.2 models available tonight 8-10 PM Beijing Time, with more to come this year
  - *From: Screeb*

- **ModelScope link for Wan 2.2 available**
  - ModelScope link shared: https://modelscope.cn/models/Wan-AI/Wan2.2-TI2V-5B
  - *From: Kijai*

- **Wan 2.2 VAE model available**
  - 1.41GB VAE model available at https://www.modelscope.cn/models/muse/wan2.2-vae
  - *From: yi*

- **Livestream starting soon**
  - Official Alibaba Wan livestream starting at 8 PM Beijing time with English subtitles
  - *From: multiple users*

- **Wan 2.2 models released with native ComfyUI support**
  - Available on ModelScope and HuggingFace, ComfyUI added native support immediately
  - *From: zelgo_*

- **ComfyUI separated the models into split files**
  - Models available in repackaged format for easier downloading
  - *From: Kijai*

- **Two model variants: 5B (new) and A14B (updated 14B)**
  - 5B supports both T2V and I2V, 14B is updated version
  - *From: multiple users*

- **Wan 2.2 released with 5B and 14B variants**
  - 5B is unified T2V/I2V model, 14B uses MoE architecture with high/low noise experts
  - *From: multiple users*

- **Native ComfyUI support available**
  - Templates updated to v3.46 with native Wan 2.2 support
  - *From: multiple users*

- **Wan competition announced**
  - Available at wan.video/activity/muse-enlist
  - *From: Siraj*

- **Wan 2.2.1 released and available in ComfyUI native**
  - Can be tested in ComfyUI native implementation, supports 4K generation with 4GB VRAM
  - *From: Juan Gea*

- **Community GGUF versions available quickly**
  - GGUF versions of Wan 2.2 models already available from community
  - *From: 🦙rishappi*

- **VACE color shift fix coming in a few weeks**
  - Team needs user examples with input video, mask, and prompts for validation
  - *From: pom*

- **Experimental VACE models available for testing**
  - VACE scopes extracted from 2.1 and injected into 2.2 14B for testing
  - *From: lym0*

- **WAN 2.2 released with 14B and 5B variants**
  - 14B uses dual model architecture, 5B is hybrid model with new VAE
  - *From: multiple users*

- **LightX team working on audio projects**
  - Community requesting LightX2V retrain for 2.2 but team is busy with audio
  - *From: hicho*

- **Kijai working on Wan 2.2 wrapper nodes**
  - First test runs shown, not yet fully ready but in development
  - *From: Kijai*

- **User starting LightX2V finetuning for both high and low noise A14B models**
  - Experimenting with training LightX lora specifically for 2.2 architecture
  - *From: mamad8*

- **2.2 models now work in WanVideoWrapper**
  - Kijai updated wrapper to support the new dual model system
  - *From: Kijai*

- **GGUF format works for 2.2**
  - GGUF quantization is confirmed working for the 14B models
  - *From: Draken*

- **Wan 2.2 wrapper I2V support added**
  - Kijai pushed update to allow I2V loading in wrapper, though not fully tested yet
  - *From: Kijai*

- **VACE and Phantom don't work with 2.2 yet**
  - These control systems haven't been adapted for the new architecture
  - *From: Kijai*

- **New TCFG feature added by PR**
  - New CFG technique available for testing
  - *From: Kijai*

- **Sage Attention 2.2 released**
  - Drop-in replacement for 2.0, now available on official GitHub
  - *From: aikitoria*

- **ComfyUI update required for Wan 2.2**
  - Tensor shape errors require fully updated ComfyUI
  - *From: Kosinkadink*

- **New fp8 scaled model available**
  - Kijai released updated fp8 scaled model for better compatibility
  - *From: Kijai*

- **Currently only DiffSynth-Studio allows training for Wan2.2**
  - Limited training options available for the new model
  - *From: mamad8*

- **VACE expected to release soon**
  - T-35 minutes to 2.2 vace release mentioned
  - *From: TK_999*

- **Wan 2.2 models available on different HuggingFace pages**
  - Kijai has hosted the models on different pages than usual, found on Comfy-Org repackaged versions
  - *From: VK*

- **New VAE only for 5B model**
  - The new VAE is specifically for the 5B model, not for 14B
  - *From: Doctor Shotgun*

- **Native ComfyUI workflows available in frontend templates**
  - Native workflows are available in the frontend templates and on HuggingFace
  - *From: DawnII*

- **Fixed scaled fp8 issue in ComfyUI wrapper**
  - Resolves black video output problems
  - *From: Kijai*

- **Multiple recent fixes and updates to wrapper nodes**
  - Users should update nodes for latest bug fixes
  - *From: Kijai*

- **Wan 2.2 released with high/low noise architecture**
  - New two-stage system with separate high and low noise models
  - *From: blake37*

- **ComfyUI frontend update with minimap feature**
  - New minimap allows navigation by clicking sections
  - *From: Kijai*

- **LightX2V models temporarily removed from HuggingFace**
  - Official LightX2V repository deleted all models, may be relocating
  - *From: Draken*

- **LightX2V models are back but no info if anything changed**
  - The models have been re-uploaded but without changelog
  - *From: Kijai*

- **LightX2V WAN 2.2 distill being worked on**
  - Development is in progress for WAN 2.2 compatible distilled models
  - *From: Doctor Shotgun*

- **Wan 2.2 English guide released**
  - Full guide with prompts and good information available
  - *From: hicho*

- **Wrapper updated to support Wan 2.2**
  - A14B works okay, 5B probably doesn't work properly yet
  - *From: Kijai*

- **New fp8_e3m2 scaled model released**
  - Very close to Q8 quality without speed loss, works in native as well
  - *From: Kijai*

- **Updated e5m2 scaled models released**
  - New fp8_e5m2_scaled models for both HIGH and LOW variants available
  - *From: Kijai*

- **Fixed VRAM usage issue in wrapper**
  - Pushed fix for scaled model dtype handling to prevent excessive VRAM usage
  - *From: Kijai*

- **Wan 2.2 fps rates confirmed**
  - 5B outputs 24fps and 14B outputs 16fps
  - *From: AJO*

- **Memory usage improvements in latest wrapper**
  - Latest wrapper changes improve memory management behavior
  - *From: Kenk*

- **WanVideoWrapper updated for Wan 2.2 support**
  - Update available via git pull, no new dependencies required
  - *From: Kijai*

- **Context windows may be implemented into native ComfyUI**
  - Kosinkadink asked by ComfyUI team to implement, hopefully opportunity soon
  - *From: Kosinkadink*

- **Luma Labs announcing Wan 2.2 coming to most tools**
  - Posted link to Luma Labs tweet about upcoming integration
  - *From: NebSH*

- **Memory fix pushed for I2V on 5B model**
  - Should fix slow I2V performance, was a problem in original code
  - *From: comfy*

- **VACE working in wrapper**
  - User confirmed VACE functionality in wrapper implementation
  - *From: hicho*

- **GGUF models available for Wan 2.2**
  - Easy to create with one script, conversion takes couple minutes
  - *From: gokuvonlange*

- **Wan 2.2 GGUF models now available**
  - Q4, Q6, Q8 quantizations available for 14B model in M, L, S variants
  - *From: xwsswww*

- **ComfyUI subgraph feature released**
  - Allows creating reusable template components for dual model loaders and samplers
  - *From: JohnDopamine*

- **Wan2.1 Apex Framepack released**
  - Framepack implementation based on Wan 2.1 instead of HYV
  - *From: yi*

- **ComfyUI native Wan 2.2 support in development**
  - PR submitted for native support, currently available through blepping's nodes
  - *From: Kijai*

- **Trainer for 5b is out**
  - New trainer release announcement
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Sage 3 added with radial attention support**
  - Works well for blackwell architecture, updated to work with sage2
  - *From: Kijai*

- **LightX2V team is working on 2.2 distillation**
  - Team needs community support (stars on GitHub) and encourages using their inference framework and ComfyUI nodes
  - *From: hicho*

- **Fredbliss working on tuning high model for performance**
  - Looking into performance optimizations for other use cases, will share fork later
  - *From: fredbliss*

- **New TCFG experimental argument available**
  - New CFG booster feature in experimental args
  - *From: Kijai*

- **All-in-one WAN 2.2 merge released**
  - Merges high/low noise models with PUSA and 2.1 models, claims 4 steps at CFG 1
  - *From: DawnII*

- **MediaSyncer tool for comparing video outputs**
  - Drag and drop up to 8+ videos for smooth comparison in browser tab
  - *From: JohnDopamine*

- **Wan 2.2 14B LoRAs already available**
  - Instagram women Wan 2.1 and 2.2 LoRAs now available on Civitai, though they are only slightly better than Wan 2.1
  - *From: hicho*

- **Wan 2.2 5B single model available from Kijai**
  - Available on HuggingFace in TI2V folder
  - *From: hicho*

- **Community comparative testing of sampler configurations ongoing**
  - Multiple users conducting systematic tests of CFG, steps, and LoRA combinations
  - *From: Ablejones*

- **Kijai overhauled vid2vid implementation**
  - Can now use start/end steps, denoise is only used to set start/end step
  - *From: Kijai*

- **Wan 2.2 doesn't have image cross attention layers anymore**
  - Doesn't use clip embeds, so some LoRA keys go unused but rest are still applied
  - *From: Kijai*

- **Xformers is pretty much useless now**
  - Most people using SageAttention for video gen (2x faster on higher res) or torch attention
  - *From: Kijai*

- **WAN 2.2 LoRAs expected next week**
  - Community anticipates new LoRAs specifically trained for 2.2
  - *From: thaakeno*

- **MultiTalk fork no longer needed**
  - Functionality integrated into main wrapper, causing confusion in Manager
  - *From: Kijai*

- **Sampler updated to return denoised samples**
  - New preview capability added to wrapper
  - *From: Kijai*

- **EchoShot method implemented in wrapper**
  - Wrapper now supports prompt splitting for multiple scenes using numbered brackets
  - *From: Kijai*

- **Fixed extra paths support for taew2_1.safetensors**
  - Updated nodes to respect extra paths for VAE approximation file
  - *From: Kijai*

- **New safety check for context settings**
  - Kijai pushed update that errors out instead of crashing ComfyUI when context settings are invalid
  - *From: Kijai*

- **LightX team interested in WAN 2.2 LoRA**
  - No concrete confirmation but LightX team has expressed interest in creating LoRA for 2.2
  - *From: DawnII*

- **New LightX version is in development**
  - New lightx version is in the works, which should stabilize current mixed information
  - *From: Juampab12*

- **Wan 2.2 ControlNet depth model released**
  - TheDenk released wan2.2-ti2v-5b-controlnet-depth-v1 on HuggingFace, though quality is questionable
  - *From: VK*

- **Multiple 5B LoRAs appearing on HuggingFace**
  - Seeing LoRAs for 5B model on HuggingFace including ostris/wan22_5b_i2v_crush_it_lora
  - *From: VK*

- **Replicate offers Pruna 2.2 14b at competitive pricing**
  - Cheaper than local inference costs
  - *From: Drommer-Kille*

- **Tiled VAE error in v2v workflows fixed**
  - Recent fix implemented by Kijai
  - *From: Kijai*

- **Custom combined sampler node in development**
  - VRGameDevGirl84 created custom node that combines both samplers into 1, auto splits steps and handles start/end steps
  - *From: VRGameDevGirl84*

- **Gemini masking capability for ComfyUI**
  - Gemini is pretty great at masking, can be paired with comfyui wan workflows
  - *From: thaakeno*


## Workflows & Use Cases

- **Endless Travel workflow for video extension**
  - Use case: Taking last frames from previous part and blending for extension without morphing
  - *From: N0NSens*

- **One step Ultimate SD Upscaler**
  - Use case: Simple upscaler that can be added to any 14B workflow without dumping models from VRAM
  - *From: David Snow*

- **Tile lora workflow for upscaling**
  - Use case: Adds details during upscaling, more sophisticated than basic refinement
  - *From: David Snow*

- **Dual sampling mask generation**
  - Use case: Creating precise masks for explosions and effects while preserving background
  - *From: Mads Hagbarth Damsbo*

- **MultiTalk with VACE integration**
  - Use case: Lip sync with additional video controls, though less accurate than MultiTalk alone
  - *From: Tango Adorbo*

- **Context extension for MultiTalk**
  - Use case: Longer video generation using internal windowing method, though quality degrades after 15 seconds
  - *From: Kijai*

- **VACE + MultiTalk with masked face**
  - Use case: Lip sync with face masking to avoid depth/MultiTalk competition
  - *From: Tango Adorbo*

- **LightX mix workflow with optimal LoRA stack**
  - Use case: Fast I2V and T2V generation with multiple enhancement LoRAs
  - *From: VRGameDevGirl84(RTX 5090)*

- **Context windows for longer videos**
  - Use case: Extending video length without degradation using uni3c
  - *From: N0NSens*

- **VACE inpainting with gray fill**
  - Use case: Object removal/replacement in videos
  - *From: Nekodificador*

- **VACE for VFX effects on existing videos**
  - Use case: Using paid software like EmberGen, 3dsmax, or free alternatives like Blender/Houdini to create effects, then blend with VACE
  - *From: hicho*

- **Using WAN T2V for image generation then I2V**
  - Use case: Generate reference image with WAN T2V model, then use for video generation to maintain consistency
  - *From: VRGameDevGirl84(RTX 5090)*

- **VACE inpainting for product insertion**
  - Use case: Repeat image 5 times to satisfy latent size and inpaint reference objects into masked areas
  - *From: Hashu*

- **Text-to-image using Wan T2V model**
  - Use case: Generate single high-quality images using video model with 1 frame
  - *From: VRGameDevGirl84(RTX 5090)*

- **Combined image generation + video creation**
  - Use case: Workflow that creates image first, then uses it for I2V generation in single process
  - *From: VRGameDevGirl84(RTX 5090)*

- **Skyreels text-to-image generation**
  - Use case: Using Skyreels T2V for high-quality single frame generation
  - *From: VRGameDevGirl84(RTX 5090)*

- **Tile LoRA with depth mask for stylization**
  - Use case: Used a depthmap (mask) and set latent noise mask to only diffuse the girl, then added my Cyberpop lora and increased denoise. Instant stylization
  - *From: David Snow*

- **Two-pass masking for VACE inpainting**
  - Use case: My two pass setup is just for isolation... the critical part of the masking is just to ensure that the soroundings does not get affected
  - *From: Mads Hagbarth Damsbo*

- **MultiTalk with multiple speakers**
  - Use case: Multi-person lip sync with separate audio tracks and masks for each speaker
  - *From: Kijai*

- **VACE with controlnet for video-to-video styling**
  - Use case: Improving general video style using depthmap/pose controlnet with reference image
  - *From: mdkb*

- **MultiTalk with vid2vid and LivePortrait**
  - Use case: Getting lip sync with character movement, but character consistency issues remain
  - *From: samhodge*

- **Using image detail transfer on normalcrafter output**
  - Use case: Combining desaturated normals with depth anything output for better results
  - *From: Flipping Sigmas*

- **Frame injection into VACE using custom node**
  - Use case: Allows single frame or set of frames from video input with control maps
  - *From: BarleyFarmer*

- **Video extension using last 15 frames**
  - Use case: Reading last frames of previous video to continue seamlessly for smooth results
  - *From: D-EFFECTS*

- **Vid2vid multitalking workflow**
  - Use case: Combining video-to-video with MultiTalk for lip sync applications
  - *From: samhodge*

- **Vid2Vid with MultiTalk for more natural head movement**
  - Use case: Getting more dynamic movement in lip-sync videos
  - *From: samhodge*

- **16fps frame rate workaround for vid2vid**
  - Use case: Overcoming WAN 2.1's 16fps cap limitation that causes frame loss
  - *From: yo9o*

- **Using Wan for both image generation and video input**
  - Use case: Ensuring consistency and faster performance by using same model throughout pipeline
  - *From: Impactframes.*

- **Two-stage VACE approach for background changes**
  - Use case: Change everything with first frame redo, then target people again using video as control to maintain structure
  - *From: mdkb*

- **Tiled upscaling with inpainting for seam fixing**
  - Use case: Crop and stitch upscaling with VACE inpainting to fix seams between tiles
  - *From: Grimm1111*

- **Skyreels I2V workflow for removing flux face**
  - Use case: Cleaning up datasets and removing AI-generated face artifacts
  - *From: VRGameDevGirl84(RTX 5090)*

- **Two-pass generation: flux first pass, skyreels second pass**
  - Use case: Use flux on first pass then 2nd pass can be skyreels to get rid of flux face, upscale and provide more natural skin texture
  - *From: VRGameDevGirl84(RTX 5090)*

- **I2V with LightX2V LoRA at 4 steps using wrapper**
  - Use case: Clean video generation with minimal steps
  - *From: David Snow*

- **VACE extension for video extending**
  - Use case: Creating longer generations from I2V by extending results
  - *From: Kijai*

- **Using silent audio tracks in MultiTalk**
  - Use case: Control which character speaks in multi-character scenes
  - *From: yukass*

- **Wan T2I then I2V pipeline**
  - Use case: Using Wan for base image generation then standard I2V for complete Wan-based process
  - *From: David Snow*

- **MultiTalk + LightX2V + UniAnimate + Uni3C**
  - Use case: Combining lip sync, pose control, and camera movement for complex character animation
  - *From: Gateway {Dreaming Computers}*

- **VACE with differential diffusion mask**
  - Use case: Precise control over diffusion strength in different areas of the video
  - *From: David Snow*

- **VACE inpainting with differential diffusion**
  - Use case: Control background denoising strength separately from masked areas
  - *From: David Snow*

- **Using ATI tracking with static points**
  - Use case: Object tracking while preventing unwanted camera movement
  - *From: Juampab12*

- **FreeInit iterative refinement**
  - Use case: Quality improvement through multiple sampler iterations
  - *From: Kijai*

- **VACE inpainting with mask control**
  - *From: David Snow*

- **MultiTalk with VACE OpenPose integration**
  - *From: Juan Gea*

- **Automated prompting with LLM integration**
  - *From: fredbliss*

- **VACE with no prompts and reference image as first frame**
  - Use case: Style transfer and controlled generation
  - *From: Draken*

- **Using VACE extend capability to extend videos and fix color shifts**
  - Use case: Creating longer videos when hitting frame limits
  - *From: Hashu*

- **Nuke integration with WAN for frame-by-frame processing**
  - Use case: VFX production work, cleanup, and relighting
  - *From: Nekodificador*

- **Crop and stitch upscaling for WAN**
  - Use case: Run cropped pieces through upscaling workflow then stitch back together, using DaVinci for color matching
  - *From: Grimm1111*

- **Character LoRA masking with SAM2**
  - Use case: Train LoRAs on WAN t2v 1.3B and swap them using SAM2 to target people individually
  - *From: mdkb*

- **Automatic podcast generation**
  - Use case: Uses Qwen to generate story/dialogue, Chatterbox for TTS, processes through multitalk in loops for full conversations
  - *From: AJO*

- **Multi-level face reinforcement**
  - Use case: Character LoRA for SDXL image, WAN LoRA for generation, then FaceFusion face swap, finally Topaz upscale
  - *From: boorayjenkins*

- **Using Blender animations with Vace for camera movements**
  - Use case: Create 81 frame rough animations in Blender, convert to depthmap in ComfyUI, restyle with Vace for camera shots
  - *From: mdkb*

- **MultiTalk with Video Unbatch for scene transitions**
  - Use case: Generate 10 scenes in loop, use Video Unbatch to break batches for concatenation, potentially add crossfade for smoother transitions
  - *From: AJO*

- **Using Uni3C to fix camera wobble and smooth scene transitions**
  - Use case: Applied to 3.5 minute generation, fixed wobble and made smooth transitions
  - *From: AJO*

- **Cascadeur to VACE styling pipeline**
  - Use case: Create simple animations in Cascadeur then do styling in ComfyUI VACE workflow
  - *From: mdkb*

- **VACE masking with semi-transparent objects**
  - Use case: Isolating and transforming specific elements like fireballs while maintaining realistic lighting
  - *From: AmirKerr*

- **Power Lora Loader with WanWrapper**
  - Use case: Simplified workflow that doesn't require loading extra model into loader node
  - *From: phazei*

- **Character creation pipeline using Flux and Wan**
  - Use case: Train character for Flux, create images, use Wan360 turntable effect, extract frames for character LoRA
  - *From: Gateway {Dreaming Computers}*

- **Kontext chaining for dataset creation**
  - Use case: Use Kontext to build first image, chain 3+ prompts (cat -> action figure -> boxed), use ComfyUI queue for 30 iterations to build dataset
  - *From: Gateway {Dreaming Computers}*

- **MultiTalk with dual audio tracks**
  - Use case: Got MultiTalk working with both tracks - rabbit following rock speech while man chills to song
  - *From: Benjimon*

- **VACE with depth/lineart blend for face replacement**
  - Use case: Maintaining facial expressions while changing identity
  - *From: Hashu*

- **VACE for video-to-video lipsync**
  - Use case: Swapping faces while maintaining mouth movement
  - *From: mdkb*

- **Mask-based inpainting with VACE**
  - Use case: Adding objects or effects to specific video regions
  - *From: SpacelessTuna*

- **Flow edit for face replacement**
  - Use case: Alternative method for changing faces in existing videos
  - *From: theUnlikely*

- **Flux + WAN 2.1 T2V repaint**
  - Use case: Enhanced text-to-image generation using Flux for initial image then WAN for low amplitude repaint
  - *From: slmonker(5090D 32GB)*

- **Model merging with switches**
  - Use case: Using merge nodes with switch and group bypass to alternate between I2V and T2V models on the fly
  - *From: ▲*

- **VACE with mid-generation control introduction**
  - Use case: Introducing control masks during middle steps of generation for expression matching
  - *From: DawnII*

- **VACE with endless travel**
  - Use case: Extending video clips with reference control
  - *From: Gateway {Dreaming Computers}*

- **Color matching from image reference**
  - Use case: Fixing color drift over time in generated videos
  - *From: Juan Gea*

- **Simple T2V with GGUF and fusion LoRA mix**
  - Use case: Basic text to video generation with 16x9 and 9x16 options
  - *From: Gateway {Dreaming Computers}*

- **Single frame generation with Wan**
  - Use case: Using Wan to generate single images instead of video
  - *From: patientx*

- **VACE without starting frame acts as T2V**
  - Use case: Can use VACE module without input image for T2V generation
  - *From: Draken*

- **Video to video upscaling with low denoise**
  - Use case: Upscaling videos with 0.3 denoise, though RAM intensive for 1080p
  - *From: Juan Gea*

- **Camera control using wireframe cube in VACE**
  - Use case: Creating smooth camera movements that continue through batch extensions
  - *From: The Shadow (NYC)*

- **Subject control using white dot animation**
  - Use case: Controlling character or object movement in VACE generations
  - *From: ˗ˏˋ⚡ˎˊ-*

- **GGUF VACE workflow for memory-constrained systems**
  - Use case: Running VACE on systems with limited VRAM using Q4_K_S or Q3 quantization
  - *From: The Shadow (NYC)*

- **Daisy-chained 49f batches with VACE**
  - Use case: Creating longer videos by chaining 49f batches with overlap to yield 5s clips at 24fps
  - *From: The Shadow (NYC)*

- **Pusa workflow with T2V model**
  - Use case: Convert T2V to I2V functionality using image input to first latent socket
  - *From: David Snow*

- **Multitalk with vocal extraction**
  - Use case: Better lip sync by separating vocals from music tracks
  - *From: Charlie*

- **Pusa with lightx2v at cfg 1, 4 steps**
  - Use case: Fast generation with Pusa + lightx combination
  - *From: ZeusZeus*

- **Tiled upscaling with WAN**
  - Use case: Adding detail while minimizing unwanted movement
  - *From: mono*

- **VACE + MultiTalk + first frame control**
  - Use case: Combining lip sync with style control
  - *From: DeeX*

- **Pusa T2V by disconnecting first latent from I2V workflow**
  - Use case: Converting I2V Pusa workflow to T2V
  - *From: David Snow*

- **Use Freeinit pass with random seed for T2V**
  - Use case: Adding cinematic realism to T2V generations
  - *From: Atlas*

- **wget command in terminal for downloading models**
  - Use case: Getting custom LoRAs/models on RunPod
  - *From: AmirKerr*

- **Text2Image2Video pipeline**
  - Use case: Using Skyreels for T2I then I2V, shares nodes for efficiency without model swapping
  - *From: VRGameDevGirl84(RTX 5090)*

- **Model merging for low VRAM systems**
  - Use case: Merge base models with LoRA stacks to run on borderline VRAM setups
  - *From: The Shadow (NYC)*

- **Multi-character lip sync with masking**
  - Use case: Use separate audio tracks and masks for each character, silent track for non-speaking characters
  - *From: DawnII*

- **Using PUSA LoRA with VACE for better reference accuracy**
  - Use case: Improving character likeness and reference adherence
  - *From: DawnII*

- **Merging VACE and Phantom models for combined benefits**
  - Use case: Getting both VACE controlnet capabilities and better Phantom references
  - *From: Piblarg*

- **Using multiple reference frames with VACE**
  - Use case: Add n*4 frames for each reference frame in VACE encode
  - *From: Piblarg*

- **PUSA LoRA with VACE+ref for character consistency**
  - Use case: T2V VACE+ref with no control using full strength PUSA LoRA and LightX2V - 4 steps for character matching
  - *From: Hashu*

- **Steerable motion continuation with overlap**
  - Use case: 81 frames per section with 9 frame overlap using WanPhantomSubjectToVideo node
  - *From: Ablejones*

- **Phantom/VACE merge with multiple CFG stages**
  - Use case: 3 steps at cfg 2.5 and 7 steps at cfg 1.0 for better Phantom results
  - *From: Ablejones*

- **PUSA + LightX + VACE multi-batch generation**
  - Use case: Extended video generation with style consistency, though has progressive degradation issues
  - *From: A.I.Warper*

- **Phantom + VACE combined workflow**
  - Use case: Getting best of both worlds - VACE control + phantom reference matching
  - *From: Hashu*

- **Uni3C for camera motion control**
  - Use case: Using control videos for camera motion instead of motion LoRAs
  - *From: VRGameDevGirl84*

- **1.3B model for upscaling workflow**
  - Use case: Fits 96 frames at 1080p with only 71% RAM usage on 24GB system
  - *From: Juan Gea*

- **PUSA first/last frame setup**
  - Use case: Encode batch where first frame is start, last 4 images are end frame, rest black
  - *From: Kijai*

- **Album cover animation workflow**
  - Use case: Turn album covers into realistic style and animate, potentially with MultiTalk
  - *From: Gateway*

- **Pose transfer with VACE**
  - Use case: Working i2i and v2v pose transfer using Wan VACE
  - *From: Valle*

- **VACE with 48GB setup**
  - Use case: Long video generation with 81,4,16 context option using VACE, Multitalking and T2V 14B with 40 blocks swapped and 15 VACE blocks swapped
  - *From: samhodge*

- **Stacking multiple LoRAs with 0 weights**
  - Use case: Load all LoRAs you want with weights at 0, then set only the one you want to 1.0 to avoid loading times when switching
  - *From: mamad8*

- **VACE+Phantom combination**
  - Use case: Using both VACE reference and Phantom embeds together for better character consistency
  - *From: Ablejones*

- **Vid2vid with CGI to photorealism**
  - Use case: Converting CGI synthesibians to photorealistic with lipsync
  - *From: samhodge*

- **VACE+Phantom+LightX v2 for character consistency**
  - Use case: Character-consistent video generation with pose control
  - *From: Ablejones*

- **Generate perfect start frame for VACE**
  - Use case: When needing exact character matching
  - *From: Hashu*

- **Two-pass noise reduction**
  - Use case: Remove stipple effect from Wan generations without upscaling - first pass normal settings, second pass 0.15 denoise 3-4 steps
  - *From: mamad8*

- **Multi-segment long video generation**
  - Use case: Generate videos longer than 81 frames by using multiple K-samplers with overlap and fixed seed
  - *From: hicho*

- **VACE for complex action generation**
  - Use case: Generate specific hand movements and object interactions by prompting detailed actions
  - *From: enigmatic_e*

- **First frame restyle to video using I2V and UniC3**
  - Use case: Take any first frame, restyle with SD1.5, then animate with I2V + UniC3
  - *From: hicho*

- **Video to UniC3 then first frame to I2V**
  - Use case: Extract camera motion from existing video, apply to new first frame
  - *From: hicho*

- **I2V + UniC3 for VACE-like control**
  - Use case: Alternative to Wan VACE for camera control without needing full VACE setup
  - *From: hicho*

- **Dense Human Pose Estimation + Wan VACE**
  - Use case: Human pose-driven video generation
  - *From: Дмитрий Марков*

- **VACE + I2V for production**
  - Use case: Client work requiring art direction control
  - *From: samhodge*

- **Vid2vid with phantom for CGI templates**
  - Use case: Converting CGI renders to realistic video
  - *From: samhodge*

- **Context windows with padded MAGREF**
  - Use case: Extending I2V beyond 81 frames
  - *From: Kijai*

- **Video extension using VACE**
  - Use case: Take X frames from end of video and extend by 81-X frames using reference frames and masking
  - *From: lostintranslation*

- **Text transformation effects with T2V + VACE**
  - Use case: Create text that morphs into ink, fire, or other effects using reference images and control
  - *From: VK (5080 128gb)*

- **I2V batch processing with multiple KSamplers**
  - Use case: Endless video generation using last frame of each generation with 4, 9, or 20 KSamplers
  - *From: hicho*

- **Text generation with masking**
  - Use case: Mask regions of video and prompt for text to get better text placement
  - *From: VK (5080 128gb)*

- **Camera motion with 3D reference**
  - Use case: Import image into Blender as reference, animate camera, use with UniC3 for controlled camera movement
  - *From: VRGameDevGirl84(RTX 5090)*

- **Extension workflow with stitching**
  - Use case: Video extension using VACE with proper stitching between segments
  - *From: lostintranslation*

- **Chaining samplers with last 5 frames**
  - Use case: Use Pusa workflow then chain more samplers feeding in the last 5 frames
  - *From: Hashu*

- **PUSA video extension using frame overlap**
  - Use case: Extending videos beyond 5 seconds by injecting last frames as starting frames for next generation
  - *From: Juan Gea*

- **Multitalk + uni3C for reference video camera dynamics**
  - Use case: Combining lip sync with camera movement transfer from reference videos
  - *From: Дмитрий Марков*

- **PUSA with T2V model for frame injection**
  - Use case: Using T2V models with PUSA LoRA and flowmatch_pusa scheduler to inject starting frames
  - *From: Kijai*

- **Pusa extension with overlap removal**
  - Use case: Creating longer videos by chaining 25-frame generations with 5-frame overlap, removing overlap frames
  - *From: Juan Gea*

- **VACE camera control with reference videos**
  - Use case: Using simple line/shape videos as control input for VACE to maintain camera consistency across batches
  - *From: The Shadow (NYC)*

- **Model merging for VACE blocks**
  - Use case: Adding VACE functionality to T2V models using native ComfyUI merge nodes at 0.0 strength
  - *From: Ablejones*

- **PUSA extension for video continuations**
  - Use case: Creating long-form videos without VACE quality degradation issues
  - *From: The Shadow*

- **WAN VACE with pose and depth control**
  - Use case: Controlled video generation using both pose and depth inputs
  - *From: Valle*

- **MultiTalk with building collapse**
  - Use case: Using audio to drive longer generations even for non-talking subjects
  - *From: Sal TK FX*

- **WAN inpainting with mask latent**
  - Use case: Background changes and object modifications in images
  - *From: hicho*

- **T2V model with latent masking for video stylization**
  - Use case: Stylizing parts of existing videos using T2V model with masked regions
  - *From: hicho*

- **VACE for inpainting, outpainting, v2v only**
  - Use case: Use VACE strictly for inpainting, outpainting, v2v but use dedicated models for T2V or I2V
  - *From: gokuvonlange*

- **2-step generation with FastWan + LightX2V**
  - Use case: Ultra-fast video generation using UniPC sampler
  - *From: phazei*

- **Using VACE with multiple character angles**
  - Use case: Input multiple images of same character from different angles for better likeness
  - *From: ingi // SYSTMS*

- **Blender 3D to video rendering**
  - Use case: Using 3D rendered scene from Blender as input to generate realistic video
  - *From: Sal TK FX*

- **EchoShot multi-prompt transitions**
  - Use case: Generate videos with character consistency across multiple scenes using numbered prompts [1][2][3]
  - *From: Kijai*

- **VACE + EchoShot combination**
  - Use case: Using VACE reference with EchoShot for controlled transitions, though prompts may bleed more
  - *From: Kijai*

- **Blender render + WAN animation**
  - Use case: Render viewport from Blender with camera movement, use one Flux frame as style reference, apply to entire video using controlnet
  - *From: Sal TK FX*

- **V2V generation using 280 frames at 4-6 steps**
  - Use case: Video-to-video with minimal morphing artifacts
  - *From: Drommer-Kille*

- **Extraction workflow for all control nets**
  - Use case: Pre-process depth, canny, pose, mask to save memory in main workflow
  - *From: Gateway*

- **Image-to-image with mask using KSampler**
  - Use case: Wan-based inpainting without VACE training
  - *From: hicho*

- **VACE I2I to V2V pipeline**
  - Use case: Restyle first frame with depth, then generate video using depth control
  - *From: hicho*

- **270 frame generation with context windows**
  - Use case: Long video generation in 10 minutes on native workflow
  - *From: Drommer-Kille*

- **T2V with image rebatch for I2V**
  - Use case: 2-step generation using distill model with Fast Wan LoRA
  - *From: hicho*

- **Batch processing with AIO**
  - Use case: Processing multiple video files, but be aware everything stays in RAM during batch processing
  - *From: Drommer-Kille*

- **Using bridge node for TE offloading**
  - Use case: Alternative to wrapper's built-in offloading for text encoder management
  - *From: Draken*

- **SuperUltimateVaceTools + 14B I2V + Lightx2v V2**
  - Use case: Perfect upscale and style transfer combination
  - *From: Дмитрий Марков*

- **Manual video stitching with VACE**
  - Use case: Creating longer videos by chaining clips with consistent elements
  - *From: Drommer-Kille*

- **Looping video with frame interpolation**
  - Use case: Better looping method using last 15 frames and first 15 frames to generate 30-40 frames between them
  - *From: gokuvonlange*

- **WanVideo Integration with LoRA Manager**
  - Use case: WanVideo Lora Select (LoraManager) node compatible with ComfyUI-WanVideoWrapper for streamlined lora usage
  - *From: pagan*

- **Use both high and low noise models in sequence**
  - Use case: All Wan 2.2 generation requires both models working together
  - *From: comfy*

- **TI2V workflow supports both text and image inputs**
  - Use case: Single model can handle both text-to-video and image-to-video
  - *From: multiple users*

- **Two-stage 14B generation**
  - Use case: High quality video generation using high noise then low noise experts
  - *From: multiple users*

- **5B unified model**
  - Use case: Single model for both T2V and I2V generation
  - *From: multiple users*

- **Dual high/low noise model setup for 14B**
  - Use case: 10 steps on high noise model, then remainder noise with 10 steps on low noise model. Found in Browse Templates > Video in updated ComfyUI
  - *From: gokuvonlange*

- **14B I2V with lightx2v working workflow**
  - Use case: Image to video generation with speed optimization
  - *From: JohnDopamine*

- **Split sampler setup for 2.2**
  - Use case: Proper step distribution between high and low noise models
  - *From: multiple users*

- **VACE testing with low-noise only**
  - Use case: Working VACE implementation using only low-noise model
  - *From: Ablejones*

- **Model merging with 100% ratio**
  - Use case: Using ModelMergeSimple with ratio 1.0 to use only first model
  - *From: Alisson Pereira*

- **WAN 2.2 with LightX2V dual pass**
  - Use case: Fast generation with 4-6 steps total, CFG 1
  - *From: cyncratic*

- **Use WAN 2.1 for low-noise, WAN 2.2 for high-noise**
  - Use case: Avoid LoRA compatibility issues
  - *From: Ablejones*

- **Multiple LoRA combination: LightX, PusaV1, FusionX**
  - Use case: Fast generation in 80 seconds
  - *From: thaakeno*

- **Dual sampler setup with mixed models**
  - Use case: Using 2.2 high noise + 2.1 base with LightX2V lora for low noise, 10 steps total
  - *From: slmonker*

- **I2V with FastWAN and LightX combination**
  - Use case: 121+ frame generation using FastWAN at 0.8 strength with LightX to prevent looping
  - *From: DawnII*

- **Low noise model only generation**
  - Use case: Skip high noise model entirely, use only low noise model for faster generation
  - *From: Kijai*

- **Dual sampler setup for 2.2**
  - Use case: High noise model for 2-4 steps, then low noise model for remaining steps with same total step count
  - *From: multiple users*

- **Multi-stage with upscaling**
  - Use case: 2.2 high noise at low resolution, latent upscale, then 2.1 for final pass
  - *From: Cubey*

- **Mixed LoRA approach**
  - Use case: FastWan 1.0 for high noise, then LightX I2V for low noise
  - *From: DawnII*

- **Dual model VACE approach**
  - Use case: 1 step Low-Noise with VACE first, then 7 steps High-Noise, then 12 steps Low-Noise again
  - *From: Ablejones*

- **Interpolation instead of upscaling**
  - Use case: Using GIMMVFI for interpolation instead of traditional upscaling, looks great without upscale
  - *From: Kenk*

- **Two-stage sampling with different LoRAs**
  - Use case: High noise model with CausVid/LightX, low noise with different LoRA
  - *From: DawnII*

- **VACE control with high strength**
  - Use case: Using VACE strength 4.0 on high-noise section for better control
  - *From: Ablejones*

- **Multi-step CFG adjustment**
  - Use case: Different CFG values for high noise (3.5-1) vs low noise passes
  - *From: VRGameDevGirl84*

- **Two-pass generation using Wan 2.2 for first pass and Wan 2.1 for high-res pass**
  - Use case: Fast generation with quality upscaling - 1280x720 in 142 seconds total
  - *From: VRGameDevGirl84(RTX 5090)*

- **Training separate LoRAs on high and low noise models simultaneously**
  - Use case: Training for Wan 2.2 - start two instances with same dataset on both models
  - *From: mamad8*

- **Dual-stage MoE workflow**
  - Use case: Wan 2.2 T2V requires running high noise model first, then low noise model with leftover noise
  - *From: MatiaHeron*

- **High noise at 4 steps euler/simple, low noise at 4 steps LCM/beta**
  - Use case: Best success workflow with no loras on first pass, LightX2V at 0.85-1.0 on second pass
  - *From: Vardogr*

- **Prompt scheduling for long videos**
  - Use case: For 81+ frame generation, use prompt scheduling since T5 can only handle 81 frame consistency
  - *From: Relven 96gb*

- **Video-to-video using Wan 2.2 with 7 steps**
  - Use case: T2V model conversion to video generation
  - *From: JmySff*

- **Dual-pass generation with mixed models**
  - Use case: Using 2.2 high noise with 2.1 low noise for better LoRA compatibility
  - *From: Kijai*

- **Two-stage Wan 2.2 with LightX2V**
  - Use case: Fast high-quality T2V generation using high noise + low noise models
  - *From: Kijai*

- **Video-driven motion at low denoise**
  - Use case: Using input video to drive motion while changing content at 0.1-0.3 denoise
  - *From: VK*

- **I2V with detailed anime character descriptions**
  - Use case: Generating anime characters with specific appearance details
  - *From: VK*

- **V2V (video-to-video) workflow**
  - Use case: Video restyling and transformations, works reliably with known motion
  - *From: Kijai*

- **Dual sampler setup for 2.2**
  - Use case: Using high noise and low noise models together with proper step coordination
  - *From: Multiple users*

- **T2V with empty embeds**
  - Use case: Text-to-video generation using same workflow as I2V but with empty image embeds instead
  - *From: Kijai*

- **Dual sampler setup with step splitting**
  - Use case: First KSampler 0-2 steps, Second KSampler 2-4 steps, both at 4 total steps
  - *From: gokuvonlange*

- **T2V with NAG and block swap**
  - Use case: Text-to-video generation with memory optimization toggles
  - *From: patientx*

- **Video enhancement using wrapper's enhance node**
  - Use case: Improving existing videos with Wan 2.2
  - *From: GalaxyTimeMachine*

- **VACE inpainting with Wan 2.2**
  - Use case: Inpainting and style transfer applications
  - *From: Hashu*

- **Two-pass generation with separate high/low noise models**
  - Use case: Better quality by running high-noise first then low-noise for refinement with different denoise settings
  - *From: Kenk*

- **Two-stage sampling with split steps**
  - Use case: High noise sampler followed by low noise sampler with split step configuration
  - *From: Multiple users*

- **Wan 2.2 with speed LoRAs**
  - Use case: Using LightX2V and other speed LoRAs for faster inference
  - *From: stas*

- **VACE style transfer and control**
  - Use case: Video control system for style transfer, inpainting, subject-driven content
  - *From: SpacelessTuna*

- **SaveLatent/LoadLatent workflow for RAM-limited systems**
  - Use case: Running Wan 2.2 14B on systems with insufficient RAM by processing high and low noise separately
  - *From: Mngbg*

- **Context windows with different overlap settings**
  - Use case: 64 overlap for high noise, 16 for low noise to generate longer sequences
  - *From: Kijai*

- **Latent upscaling between samplers**
  - Use case: Generate at low resolution then upscale between high and low noise samplers for higher resolution output
  - *From: DawnII*

- **Basic MultiTalk workflow with Wan models**
  - Use case: Creating short movies with lip-sync, using 2.1 for talking parts and 2.2 i2v for non-talking clips
  - *From: slmonker(5090D 32GB)*

- **Save/Load Latent nodes for memory management**
  - Use case: Running Wan 2.2 on systems with limited RAM by splitting the process
  - *From: The Shadow (NYC)*

- **Two-stage sampling with high/low noise models**
  - Use case: First sampler for first half, second sampler resamples second half
  - *From: l҈u҈c҈i҈f҈e҈r҈*

- **MagRef as i2v with Wan 2.1**
  - Use case: Using MagRef model for image-to-video generation
  - *From: N0NSens*

- **Using 2.1 distill then 2.2 low as second pass**
  - Use case: Multi-stage generation process
  - *From: hicho*

- **I2V with character LoRAs**
  - Use case: Character consistency in video generation
  - *From: gokuvonlange*

- **Native workflow for 2.2 on 4090**
  - Use case: Running on lower VRAM cards with blockswap + 64GB RAM
  - *From: comfy*

- **Dual model loader and dual sampler setup using subgraphs**
  - Use case: Converting Wan 2.1 workflows to Wan 2.2 efficiently
  - *From: JohnDopamine*

- **FFLF (First Frame Last Frame) with Wan 2.2**
  - Use case: Video morphing and extension
  - *From: JmySff*

- **Context windows with MAGREF**
  - Use case: 400+ frame video generation without artifacts
  - *From: blake37*

- **Vid2Vid using I2V with low denoise**
  - Use case: Video enhancement and style transfer
  - *From: VK (5080 128gb)*

- **V2V workflow for Wan 2.2**
  - Use case: Video to video generation with very good results
  - *From: Yan*

- **Using VACE FLF (First-Last-Frame)**
  - Use case: Video control with first and last frame morphing
  - *From: JmySff*

- **Two-step generation with load/save latent**
  - Use case: Manual two-step process for better control
  - *From: Juan Gea*

- **High noise model at CFG 3.5 with no distill lora, Low noise at CFG 1 with rank256 I2V lightxv2 lora**
  - Use case: Best I2V results in shortest time while maintaining 2.2 quality
  - *From: gokuvonlange*

- **T2V with 6 steps using lightxv2 lora matching original model at 20/30 steps**
  - Use case: Fast T2V generation with quality preservation
  - *From: gokuvonlange*

- **Combining lightx2v and fastwan loras at 1.0 strength with 2/2 sampling**
  - Use case: Best motion with minimal anatomical warping
  - *From: Ant*

- **High noise with lightx=1 cfg=1, then low noise without lightx cfg=5**
  - Use case: Maintaining 2.2 quality while using speed optimizations
  - *From: TK_999*

- **2.2 T2V with VACE for first/last frame using random images**
  - Use case: Creating transitions between unrelated images
  - *From: JmySff*

- **Local VLM creates prompts to connect start/end images**
  - Use case: Automated prompt generation for image transitions
  - *From: JmySff*

- **High/Low noise split with different settings**
  - Use case: 50/50 split: First sampler 20 steps ending at 10 (CFG 3.5), Second sampler 10 steps starting at 5 (CFG 1 + I2V distill LoRA rank256)
  - *From: gokuvonlange*

- **Basic looping setup**
  - Use case: Generate 177 frames with context window and loop output once for seamless loops
  - *From: Kijai*

- **Speed optimized setup**
  - Use case: 6 steps total: 6 steps high noise (no LoRA), 2-3 steps low noise with LightX2V
  - *From: slmonker*

- **Two-stage sampling with different samplers**
  - Use case: Speed optimization while maintaining quality - dpmpp_sde for low noise, LCM for high noise
  - *From: homem desgraca*

- **Context window with 121 frames using 40 frame overlap**
  - Use case: Extended video generation beyond 81 frame limit
  - *From: samhodge*

- **Phantom LoRA with vid2vid and MultiTalking**
  - Use case: Identity preservation in lip-sync workflows
  - *From: samhodge*

- **Vid2vid using denoise with video samples**
  - Use case: Converting video to video with style changes
  - *From: VK (5080 128gb)*

- **Three sampler setup with 3, 2, 1 CFG**
  - Use case: 2 high noise samplers, 1 low noise for balanced results
  - *From: Simjedi*

- **LCM + LCM for fast results**
  - Use case: Quick generation when quality isn't critical
  - *From: homem desgraca*

- **Wan 2.2 with MMaudio integration**
  - Use case: Adding audio to generated videos
  - *From: thaakeno*

- **Sequential prompting with camera movements and character actions**
  - Use case: Creating cinematic sequences with detailed camera work
  - *From: AJO*

- **Using masks with encoder for background preservation**
  - Use case: Keeping original background while animating foreground
  - *From: VK (5080 128gb)*

- **Taking last frame of each sequence as initial image for next**
  - Use case: Avoiding phantom effects in long sequences, 6 sequences tested
  - *From: manu_le_surikhate_gamer*

- **Real scenes to anime transformation using vid2vid**
  - Use case: Style transfer from realistic footage to anime
  - *From: VK (5080 128gb)*

- **WAN 2.2 14B GGUF V2V workflow**
  - Use case: Video-to-video transformation using GGUF quantized models
  - *From: thaakeno*

- **EchoShot prompting with scene transitions**
  - Use case: Creating videos with multiple scene changes using structured prompts
  - *From: Kijai*

- **JSON structured prompting**
  - Use case: Complex scene descriptions with camera movements and detailed actions
  - *From: 🦙rishappi*

- **Context windows with different prompts**
  - Use case: Extended sequences with varying prompt content
  - *From: Kijai*

- **Multi-resolution I2V with upscale**
  - Use case: Generate at low res (384x512) then upscale to high res (1024x1536) by decoding, swapping first frame with original, re-encoding
  - *From: mamad8*

- **Context windows with stride for long videos**
  - Use case: Creating coherent long videos (257+ frames) using different prompts per window and stride parameter
  - *From: Kijai*

- **Two-pass upscaling for T2V**
  - Use case: Generate motion at low res with high noise model, then gradually upscale - works because model is worse at high res
  - *From: Kijai*

- **Two-pass upscaling with speed LoRAs**
  - Use case: Generate low res with full model, upscale, then high res pass with speed LoRAs for quality+speed balance
  - *From: mamad8*

- **V2V workflow for video-to-video**
  - Use case: Give latent of uploaded video to high noise model for video transformation
  - *From: thaakeno*

- **Text to image with 2.2**
  - Use case: 2.2 adds more detail to images when doing text to image compared to 2.1
  - *From: VRGameDevGirl84*

- **Two-pass 2.2 workflow with proper step distribution**
  - Use case: 6 steps total: first sampler start 0 end 3, second sampler start 4 end 9999
  - *From: Juampab12*

- **Video extension using VACE**
  - Use case: Extending videos with uninterrupted motion, but only works with T2V models
  - *From: lostintranslation*

- **Individual I2V generations stitched with VACE**
  - Use case: Creating indefinitely long videos by stitching I2V generations together
  - *From: Daflon*

- **Disk cache workflow optimization**
  - Use case: Run prompt once with disk cache enabled, then disable T5 loader on next runs to save 10GB RAM
  - *From: Kijai*


## Recommended Settings

- **LightX2V strength**: 0.3
  - Better results than 1.0, though user questions if should be 1.0
  - *From: mdkb*

- **LightX2V strength**: 0.7
  - Much better motion than full strength
  - *From: TK_999*

- **Shift setting for LightX text to video**: 5
  - Works without much issue, though has slow motion effect
  - *From: crinklypaper*

- **High Speed Dynamic lora strength**: 2-3
  - Provides good motion improvement, strength 3 tends to default to specific angles
  - *From: VK (5080 128gb)*

- **Moviegen lora strength**: 0.5-0.6
  - Prevents ghosting artifacts that occur at strength 1.0
  - *From: Guey.KhalaMari*

- **Block swaps on RTX 3090**: ~20 blocks for 1280x720x81 on fp8
  - Optimal memory usage
  - *From: Kijai*

- **Model memory calculation**: Divide model size by 40
  - Rough calculation for individual block memory usage
  - *From: Kijai*

- **CFG setting**: 1.0
  - Current recommended setting
  - *From: Kijai*

- **Precision settings for RTX 3090**: fp16 base_precision, fp8_e5m for quant
  - Memory optimization
  - *From: ˗ˏˋ⚡ˎˊ-*

- **LightX2V LoRA steps**: 4 steps
  - Distilled at 4 steps, going beyond may worsen results
  - *From: JohnDopamine*

- **LightX2V scheduler**: dpm++_sde
  - Personal preference over unipc
  - *From: Kijai*

- **Shift value for character consistency**: 11
  - Better at keeping character vs lower values
  - *From: Kijai*

- **LightX2V LoRA strength combinations**: Lightx 0.7, Fusion 0.3, High Speed Dynamic 1.0
  - Good motion and stability in 4 steps
  - *From: zoz*

- **Block swap for 4090**: 20 blocks, all options false
  - 4090 has enough VRAM to not need aggressive swapping
  - *From: Colin*

- **Motion_frame parameter**: 25 vs 16 testing
  - Higher values may improve context window behavior
  - *From: Kijai*

- **VRAM usage with fp8 and block swap**: 1280x720x81 uses 6.5GB VRAM
  - Efficient memory usage with proper settings
  - *From: Kijai*

- **WAN T2V image generation**: 4 steps, 26-39 seconds on RTX 5090
  - Good balance of speed and quality
  - *From: VRGameDevGirl84(RTX 5090)*

- **Vintage LoRA strength**: 0.5
  - Good balance for style effect without overpowering
  - *From: VRGameDevGirl84(RTX 5090)*

- **Skyreels LoRA strengths**: 0.2 for all LoRAs
  - LoRAs have different effects in Skyreels, need lower strength
  - *From: VRGameDevGirl84(RTX 5090)*

- **Skyreels shift parameter**: 7-8
  - Higher shift values produce better results, different from Wan
  - *From: VRGameDevGirl84(RTX 5090)*

- **Flow matching scheduler for Skyreels**: 8.0 for T2V, 5.0 for I2V
  - Recommended parameters from official documentation
  - *From: Guey.KhalaMari*

- **Self-forcing LoRA**: CFG 1.0, 4-8 steps, LCM sampler
  - Enables fast generation with decent quality
  - *From: izashin*

- **MultiTalk LoRA strength**: 1.2 at 4 steps
  - tends to work better at 1.2 strength at 4 steps
  - *From: Kijai*

- **dpm++_sde sampler preference**: dpm++_sde over LCM
  - I still prefer dmp++_sde in most cases, but lcm is fine too
  - *From: Kijai*

- **33 frames for 720x1280 on 14B i2v**: Maximum frames achievable on RTX 3090
  - Hardware limitation
  - *From: Rainsmellsnice*

- **CFG setting of 4**: Used without speed LoRAs
  - Different approach to optimization
  - *From: mdkb*

- **Context window 81 frames with 32 overlap**: For 162 frame generation
  - Long video generation
  - *From: Juan Gea*

- **LightX2V LoRA with 4 steps**: Minimal steps for speed
  - Fast inference
  - *From: AI_Fan*

- **LightX2V LoRA strength**: 1.2 with dpm_sde++
  - Optimal settings for distill lora performance
  - *From: Kijai*

- **Motion LoRA strength**: 2.00
  - To help achieve faster motion in generated videos
  - *From: VRGameDevGirl84*

- **VACE reference image padding**: 20% white border
  - Required for reference images to be properly recognized and used
  - *From: mdkb*

- **Face enhancer LoRA strength**: 0.5
  - With other LoRAs at 0.2 and moviigen/MPS at 0.8 for balanced results
  - *From: VRGameDevGirl84*

- **LightX2V LoRA strength**: 1.0
  - Standard recommended strength for distilled LoRA
  - *From: Screeb*

- **Audio CFG in wav2vec**: 3-5
  - For more accurate lipsync and faster speech recognition
  - *From: DawnII*

- **Shift parameter**: 2-5
  - Shift 1 causes glitches, shift 2+ is usable, higher values increase contrast
  - *From: Screeb*

- **Frame rate**: 16fps
  - Locked frame rate for consistency across all workflows
  - *From: mdkb*

- **MultiTalk frame request**: 209 frames
  - Produces approximately 249 frames (10 seconds) output
  - *From: AJO*

- **LightX2V LoRA strength**: 1.0
  - Recommended unlike CausVid LoRA extraction
  - *From: JohnDopamine*

- **LightX2V steps**: 4 for test, 6-8 for final
  - 4 steps sufficient for testing, 6-8 for final quality
  - *From: David Snow*

- **Native sampler/scheduler**: Euler / ddim_uniform
  - David Snow's preferred settings for native
  - *From: David Snow*

- **Wrapper sampler**: Euler
  - Most consistently pleasing results
  - *From: David Snow*

- **Control strength for depth maps**: Lower values
  - Prevents depth control video from affecting final output geometry
  - *From: N0NSens*

- **Steps for GGUF models**: Same as regular models
  - No difference in step requirements
  - *From: Kijai*

- **CFG for GGUF models**: Same as regular models
  - No difference in CFG requirements
  - *From: Kijai*

- **Reserve VRAM**: 2-3GB
  - Accounts for browser and monitor usage to prevent VRAM capping
  - *From: Kijai*

- **Steps with LightX2V LoRA**: 4 steps
  - Produces clean results with speed LoRA
  - *From: David Snow*

- **Quantization for older GPUs**: fp8_e5m2
  - Better compatibility, though e4m3fn and e5m2 are same size in memory
  - *From: Kijai*

- **Text encoder quantization**: Use native TE with fp8
  - Better VRAM management than wrapper TE
  - *From: hicho*

- **High speed dynamics lora strength**: 0.1
  - Prevents noise while maintaining equivalent effect
  - *From: Kijai*

- **UniAnimate strength**: 0.5
  - Used in combination workflow with Uni3C at 0.7
  - *From: Gateway {Dreaming Computers}*

- **Frame count**: Values divisible by 16 (e.g., 33, 81)
  - Frames must divide evenly for proper generation
  - *From: Kijai*

- **LoRA strength with updated wrapper**: 0.1
  - LoRAs became 10x stronger after alpha scaling fix
  - *From: Kijai*

- **FreeInit iterations**: Single iteration
  - Consistently better than base generation, but heavy time penalty for multiple
  - *From: Kijai*

- **audio_scale in MultiTalk**: 2-3
  - Improves lip-sync quality significantly, but watch for artifacts at higher values
  - *From: Charine*

- **LightX2V LoRA strength**: 1.0 at 5 steps
  - Optimal settings when substituting for CausVid
  - *From: MilesCorban*

- **FusionX steps**: Up to 10 steps
  - Diminishing returns beyond 10 steps, but improves details and secondary motion
  - *From: Todd*

- **CFG for single frame generation**: Above 1.0 with 30-40 steps
  - Interesting results when combined with reduced LoRA strength
  - *From: Shawneau 🍁 [CA]*

- **Shift value for I2V**: Higher than 1
  - Reduces ghosting in anime content
  - *From: VRGameDevGirl84(RTX 5090)*

- **Block swapping**: 40 regular and 15 vace
  - Maximum block swaps for extending frame range
  - *From: Hashu*

- **WanFusionXFaceNaturalizer lora strength**: 0.7
  - Good balance of detail and natural faces
  - *From: VRGameDevGirl84(RTX 5090)*

- **Shift value**: 1.5 or 2
  - Helps with background issues and prompt adherence
  - *From: VRGameDevGirl84(RTX 5090)*

- **Scheduler**: dpm++_sde/beta
  - Can fix background noise issues
  - *From: VRGameDevGirl84(RTX 5090)*

- **Shift value**: 1.5 or 2
  - Helps reduce strange noise when combined with dmp++_sde/beta scheduler
  - *From: VRGameDevGirl84*

- **LightX weight with rank16**: 1.2-1.4
  - Better performance with rank16 version
  - *From: DawnII*

- **CausVid 1 weight with VACE**: 0.3-0.5
  - Helps when using VACE controlnets
  - *From: DawnII*

- **Steps for LightX**: 6-8 steps
  - 4 steps doesn't cut it, 6-8 work well with lightx=1, shift=5, unipc
  - *From: garbus*

- **FreeInit iters minimum**: 2
  - Should be minimum of 2, first one gets skipped if samples provided
  - *From: Kijai*

- **Noise aug strength**: 0.8
  - Higher than default 0.3 for more motion
  - *From: VRGameDevGirl84*

- **LightX2V strength**: 0.8 requires more steps, 1.0 for faster inference
  - Lower strength causes pixelated artifacts without more steps
  - *From: MysteryShack*

- **SeedVR2 batch size**: 45 or match longest shot frame count
  - Batch size 1 causes poor temporal consistency like ESRGAN
  - *From: Adrien Toupet*

- **cache_model for SeedVR2**: false when VRAM limited
  - Slower startup but saves memory when stretched for VRAM
  - *From: Adrien Toupet*

- **Character LoRA training**: 20 images, 512x512, no captions, just trigger word
  - Captions not mandatory for character LoRA training on Wan
  - *From: Dream Making*

- **VACE mask expansion**: 30 pixels
  - Enables wild transformations and better integration
  - *From: David Snow*

- **Context overlap for long videos**: Up to 64
  - Better continuity but slower generation
  - *From: Kijai*

- **Fire LoRA strength**: 3.0
  - Effective for fire generation in VACE
  - *From: AmirKerr*

- **VACE opacity for control objects**: 95%
  - Allows VACE to peek and see overlaid objects
  - *From: AmirKerr*

- **Face detailer LoRA weight**: 0.5 instead of 1.00
  - Brings back more facial motion while retaining detail improvements
  - *From: VRGameDevGirl84(RTX 5090)*

- **LightX2V with LCM/Simple**: 4 steps
  - Good results for testing, but remove for production runs
  - *From: Gateway {Dreaming Computers}*

- **Max frames for VRAM limit**: 41 frames at 1600x900
  - Maximum before OOM on certain hardware setup
  - *From: mdkb*

- **Noise augmentation strength**: 0.005 to 0.010
  - Optimal range for quality
  - *From: xwsswww*

- **Lineart blend opacity**: 50% multiply
  - Balance between detail and subject likeness
  - *From: Hashu*

- **Depth/pose blend**: 0.25 screen blend
  - Recommended in workflow video
  - *From: mdkb*

- **Pusa inference steps**: 50 steps T2V, 30 steps I2V
  - Default in example scripts despite claims of fewer steps
  - *From: Kijai*

- **LightX2V LoRA steps**: 4 steps
  - Achieves good results with new rank64 I2V LoRA
  - *From: slmonker(5090D 32GB)*

- **Skyreels merge ratio**: 0.3 or lower
  - Higher ratios cause greyish results and artifacts
  - *From: ▲*

- **VACE LightX LoRA strength**: 1.1-1.2 for rank32, 1.3-1.4 for rank16
  - Required strength for proper function with VACE
  - *From: DawnII*

- **Scheduler for LightX LoRA**: DPM++_SDE or LCM
  - Needed for proper noise introduction per step
  - *From: DawnII*

- **Steps for distilled models**: 2 steps for T2V, 4 steps for I2V
  - Optimal performance with new distilled models
  - *From: hicho*

- **CFG for distilled I2V LoRA**: 1 CFG
  - Works well with 4 steps, generates in ~35 seconds on 4090
  - *From: Ada*

- **Scheduler for distilled models**: LCM
  - Used with 4 steps and 1 CFG for good results
  - *From: Ada*

- **Virtual memory for FP8 conversion**: 90 GB
  - Required to convert models to FP8 format
  - *From: hicho*

- **Steps for LightX2V v2**: 4 minimum, 6 steps preferred by some users
  - 2 steps too low quality, more steps may be needed due to added motion
  - *From: Kijai*

- **LightX2V strength**: 1.0-1.5, can push to 2.0
  - Higher strength improves motion and realism but may cause burning or lose illustration style
  - *From: multiple users*

- **LoRA rank recommendation**: 32-64
  - 32 is small enough (~300MB), 64 for full quality. Higher ranks may not provide benefit
  - *From: Draken*

- **Steps with LightX2V**: 4-6 steps
  - LightX2V allows very low step counts while maintaining quality
  - *From: garbus*

- **Resolution for quality results**: 960x544
  - Good balance of quality and memory usage, no upscaling needed
  - *From: garbus*

- **LightX2V LoRA strength**: 1.0
  - Standard strength for LightX2V, compared to 0.5 for CausVid
  - *From: Gateway {Dreaming Computers}*

- **CFG with LightX2V**: 1
  - Low CFG works well with distilled models
  - *From: Gateway {Dreaming Computers}*

- **Pusa LoRA strength**: 1.0-1.5
  - Works at different strengths, 1.4 matches their examples
  - *From: Kijai*

- **Motion Boost LoRA strength**: 0.5
  - Good starting point when replacing ACC LoRA
  - *From: The Shadow (NYC)*

- **Pusa lora strength**: 1.4
  - Default that works, 1.0 too weak
  - *From: Kijai*

- **Default Pusa steps and cfg**: 10 steps with cfg 5.0
  - Their cited default settings
  - *From: Kijai*

- **Pusa with lightx**: cfg 1.0 works
  - Can work with distilled lora
  - *From: Kijai*

- **Distillation loras**: Lower strength, cfg 2-3 range, 8-12 steps
  - Work better than cfg 1 and 4 steps
  - *From: spacepxl*

- **Pusa LoRA weight**: 1.4
  - Prevents excessive changes to initial frame
  - *From: Kijai*

- **Phantom model steps**: 6-10
  - Needs more steps to cook properly compared to other models
  - *From: Guey.KhalaMari*

- **WAN 14B T2V shift**: 6
  - Works nicely for most things
  - *From: Piblarg*

- **Radial attention dense steps**: 10
  - Hardcoded default for initial implementation
  - *From: Kijai*

- **block_swap**: Increase by 5 from current, up to 40
  - Prevents VRAM overflow and slowdowns
  - *From: Juampab12*

- **NVIDIA control panel**: Set to 'no fallback'
  - Get errors instead of extreme slowdowns when exceeding VRAM
  - *From: Juampab12*

- **radial_attention_start_step**: Lower than total steps, 0 for fastest
  - Controls when radial attention activates, 0 is fastest but lower quality
  - *From: Kijai*

- **image dimensions**: Must be divisible by 128
  - Required for radial attention to work
  - *From: Kijai*

- **Dense timesteps**: 1 (start)
  - For radial attention, increase only if quality unsatisfactory
  - *From: Kijai*

- **Decay factor**: higher values
  - Better quality with radial attention
  - *From: Kijai*

- **Block swap**: 8-16 blocks
  - Minimal time penalty for longer/higher res generations
  - *From: MatiaHeron*

- **LightX2V rank**: 128
  - Better motion fluidity than rank 64
  - *From: David Snow*

- **radial_steps**: 5 with 6 sampling steps
  - Good balance of speed vs quality
  - *From: Kijai*

- **dense_steps**: Start at 0, increase until satisfied
  - All steps at 0 gives shit quality, need to find balance
  - *From: Kijai*

- **strength**: 1-1.2 would be ideal
  - Increasing strength increases vibrance and contrast mostly
  - *From: Atlas*

- **LightX2V with distill**: 2 steps with shift at 5
  - Gives good results and makes fusionx merge faster
  - *From: hicho*

- **CFG with Phantom**: Higher than 1, at least 8 steps
  - CFG 1 produces poor results with Phantom
  - *From: Piblarg*

- **MultiTalk FPS**: 25fps locked
  - AFAIK it's locked at 25fps for lip sync
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Radial Sage Attention block size**: 64 or 128
  - Block size 64 allows more resolutions but is slower than 128
  - *From: Kijai*

- **PUSA LoRA strength balance**: Variable (lower for more motion)
  - Lower the pusa lora strength to find balance between reference matching vs motion
  - *From: Hashu*

- **LightX2V strength**: 0.8
  - Better results than 1.0 in many cases
  - *From: Kijai*

- **PUSA strength for I2V**: 1.5
  - Works well for I2V workflows
  - *From: Charlie*

- **LightX + PUSA combination**: LightX 0.65, PUSA 1.0
  - Gets sharpening effect while maintaining decent colors
  - *From: A.I.Warper*

- **Steps and CFG for Phantom**: 18 steps, CFG 3
  - Good results with control+phantom combination
  - *From: Ablejones*

- **fp16 model recommended for quality**: fp16
  - Optimal for quality over fp8
  - *From: Kijai*

- **PUSA strength**: 1.4
  - Official default, prevents jumping away from subject
  - *From: Kijai*

- **PUSA low-step config**: light i2v 0.85, CausVid 1.5 at 0.5, Pusa 1.4, 3 steps
  - Maintains adherence at low steps
  - *From: phazei*

- **MAGREF setup**: cfg 1, 6 steps, flowmatch_pusa with i2v rank64 LoRAs
  - Better face consistency
  - *From: ZeusZeus*

- **LightX2V strength with unmerged fp8**: 0.8
  - Normal fp8 with unmerged LoRAs requires lower strength
  - *From: Kijai*

- **Context window with VACE**: 33 frames with 16 frame overlap
  - VACE requires smaller context window compared to 121 frames without VACE
  - *From: samhodge*

- **Block swap for 48GB VRAM**: 40 blocks swapped and 15 VACE blocks swapped
  - To fit VACE, Multitalking and T2V 14B on 48GB card
  - *From: samhodge*

- **VACE control mask**: White masks for areas to generate, black masks to preserve
  - Tells VACE whether to use control signal only or also image information
  - *From: Ablejones*

- **Vid2vid denoise strength**: 0.6
  - Grabs movement from source video while allowing style transformation
  - *From: samhodge*

- **RTX 5090 power limit**: 500W
  - Manages temperatures (80-83°C) while maintaining good performance
  - *From: Kijai*

- **VACE strength with multiple controls**: Lower strengths (0.5 mentioned)
  - Prevents conflicts when using multiple VACE controls
  - *From: Drommer-Kille*

- **LoRA strength with scaled quantization**: 10-20% reduction from normal values
  - Scaled quantized models (e5m2_scaled, e4m3fn_scaled) make LoRAs stronger
  - *From: Kijai*

- **Phantom CFG progressive**: CFG 3 for first 3 steps, CFG 1 for last 5 steps with 8-step distill
  - Phantom is very sensitive and needs proper CFG scheduling
  - *From: Ablejones*

- **Second pass denoise**: 0.15 for noise reduction, 0.3+ for content correction
  - Lower values for just noise, higher for fixing hands or other details
  - *From: mamad8*

- **Phantom baseline**: CFG 5, 20 steps, 24fps, 121 frames
  - Model trained at these settings, works at 81/97 frames too
  - *From: Ablejones*

- **Phantom CFG with PerpNegGuider**: cfg 3, neg_scale 1.0
  - Testing alternative to standard sampler
  - *From: Ablejones*

- **UniC3 steps for I2V**: 3 steps
  - Fast generation with full distill mode
  - *From: hicho*

- **Comfy chunked scheduler**: Use over old comfy option
  - Reduces VRAM usage by up to 1GB
  - *From: hicho*

- **VRAM args**: 0.95 for offload
  - Memory management on 3090 24GB
  - *From: sneako1234*

- **Context window overlap**: 64 frames
  - Reduces snapping back to init image
  - *From: Kijai*

- **Uni3C strength**: 2.0
  - For strong camera movement control
  - *From: Kijai*

- **Frame skip technique**: Skip every 2 frames
  - Double generation speed for 10s videos
  - *From: Drommer-Kille*

- **rope_function**: comfy
  - comfy_chunked causes LoRA strength issues
  - *From: Hashu*

- **denoise_strength**: 0.6
  - Works well for video-to-video generation
  - *From: samhodge*

- **cfg_scale**: 4-6
  - Good for production renders with 20+ steps
  - *From: Gateway {Dreaming Computers}*

- **empty_frame_level**: 0.5
  - Creates proper gray frames for VACE generation
  - *From: Hashu*

- **uni3c_strength**: 2.0
  - Works well with MAGREF model
  - *From: Kijai*

- **Steps for text generation**: 8 steps
  - Better results than 4 steps
  - *From: VK (5080 128gb)*

- **LoRA strength for scaled models**: 10-20% lower
  - Scaled models work better with reduced strength
  - *From: Kijai*

- **Shift parameter for UniC3**: 10
  - Helped with UV texture tracking
  - *From: N0NSens*

- **Resolution for avoiding duplication**: 1280x768 instead of 1280x720
  - Fixes astigmatism-like duplication issues
  - *From: Juan Gea*

- **Scheduler for I2V distill model**: UniPC beta
  - Recommended for distill I2V model without LoRAs
  - *From: hicho*

- **FastWan 1.3B parameters**: CFG 1.0, 5-10 steps, res_multistep or dpm++_sde scheduler
  - Works reasonably well though no official documentation available
  - *From: Kijai*

- **PUSA noise injection**: 0.1 instead of 0.7
  - 0.7 was too much noise, 0.1 gave much better extension results
  - *From: Juan Gea*

- **PUSA frame overlap**: 13 frames following 4+1 rule
  - Better results than 12 frames, reduces flash artifacts
  - *From: Kijai*

- **FastWan resolution and performance**: 1920x1152x81 frames, 4 steps, euler, 286 seconds on RTX 4090
  - Good performance for anime/cartoon content
  - *From: Juan Gea*

- **Block swap for high resolution**: 40 (can be decreased)
  - Enables 1920x1152x81 frame generation on single RTX 4090
  - *From: Juan Gea*

- **CFG**: 3.0 for first step, 5.0 for subsequent steps
  - Better results in Pusa extensions
  - *From: Kijai*

- **Overlap frames**: 5 frames
  - Good balance for video extensions without quality loss
  - *From: Kijai*

- **Steps for Fast Wan 1.3B**: 8 + 4 (like other models)
  - Same as Wan 2.1 with LightX2V
  - *From: patientx*

- **Resolution for 1.3B**: 480p or higher supported, avoid lower
  - Higher resolutions give better anatomy, lower resolutions worse quality
  - *From: hicho*

- **denoise**: 0.65 for v2v
  - Good balance for video-to-video generation
  - *From: samhodge*

- **denoise**: 0.9
  - Higher denoise for more dramatic changes
  - *From: samhodge*

- **quantization**: fp8_scaled
  - Latest quantization method being used
  - *From: MysteryShack*

- **MultiTalk duration**: up to 10 seconds
  - Works well without context degradation up to this point
  - *From: Kijai*

- **Sage Attention 3 timestep scheduling**: Use 2++ for first and last step, 3 for middle steps
  - Recommended usage pattern for optimal performance
  - *From: aikitoria*

- **per_block_mean**: False
  - Reduces VRAM usage to sage2 levels in SageAttention 3
  - *From: Kijai*

- **denoise**: 0.50
  - Works best for stylizing original video with T2V model and masking
  - *From: hicho*

- **FastWan LoRA strength**: 1.0 for 4 steps, 1.5 for 3 steps
  - Optimal balance between quality and speed
  - *From: phazei*

- **Radial attention steps**: 5 steps maximum
  - Quality hit becomes noticeable if run on all steps
  - *From: Kijai*

- **VRAM optimization**: Always connect torch compile node if you have working Triton
  - Better memory management and beneficial performance
  - *From: Kijai*

- **Denoise for masking**: 0.55
  - Higher values cause offscreen results with T2V model masking
  - *From: hicho*

- **EchoShot prompt format**: [1] prompt text [2] prompt text [3] prompt text
  - Required numbering format for scene transitions
  - *From: Kijai*

- **WAN token limit**: 512 tokens
  - Maximum tokens WAN is trained with, 46 tokens per prompt should be enough for multi-prompt use
  - *From: Kijai*

- **LoRA strength combinations**: DMD 0.4 with CausVid bidirectional 0.6
  - Good balance for quality transitions
  - *From: Kijai*

- **VACE denoise for motion influence**: 0.6 denoise
  - Actually influences the motion, good for image rebatch or video input latent
  - *From: VK*

- **LightX2V LoRA strength**: 0.25
  - Reduces over-smoothing while maintaining quality
  - *From: Drommer-Kille*

- **Steps for T2V**: 6
  - Good quality without artifacts when using reduced LoRA strength
  - *From: Drommer-Kille*

- **Steps for V2V**: 4
  - Sufficient for video-to-video with proper LoRA settings
  - *From: Drommer-Kille*

- **EchoShot max shots**: 6
  - System limitation - input shot num must be between 2-6
  - *From: Kagi*

- **Reserve VRAM**: 2GB
  - Prevents Windows from using inference VRAM
  - *From: Kijai*

- **Block swap**: Up to 40, at least 1 VACE block
  - Better memory management and performance
  - *From: Kijai*

- **Scheduler with lightx2v**: dpm++_sde
  - Recommended over other schedulers
  - *From: Kijai*

- **Attention mechanism**: sageattn
  - Much faster than sdpa
  - *From: Kijai*

- **LoRA training**: 1 sample per 50-100 steps
  - Better than batch training for small datasets
  - *From: Ryzen/Drommer-Kille*

- **I2V for I2I**: Rebatch=1, embed=1
  - Single frame image-to-image generation
  - *From: hicho*

- **Block swap**: Full blocks (40+ blocks)
  - Key for higher resolutions like 1400, enables better VRAM utilization
  - *From: VK (5080 128gb)*

- **Radical attention decay**: 0.4
  - Better than default settings
  - *From: MysteryShack*

- **MultiTalk proper settings**: 30 steps, cfg 5, disable distillation LoRAs
  - For better quality when not using fast inference
  - *From: Kijai*

- **cfg**: 6.0
  - Works well with uni3d and shift 5.0 for quality results
  - *From: samhodge*

- **shift**: 5.0
  - Combined with cfg 6.0 and uni3d for optimal results
  - *From: samhodge*

- **audio cfg**: 5.0
  - Better results with audio scale 2.0 for multitalking
  - *From: samhodge*

- **lightx2v lora rank**: 64
  - Good enough quality for most applications
  - *From: phazei*

- **audio cfg**: 3.0
  - Used in overnight generation run
  - *From: samhodge*

- **audio scale**: 1.0
  - Used in overnight generation run
  - *From: samhodge*

- **context window**: 121 context with 40 frame overlap
  - Fits on GPU at 480p for 265 frames
  - *From: samhodge*

- **empty frame level**: 0.50
  - To avoid gray frame issues
  - *From: Yae*

- **Steps**: 20 steps required
  - Back to 20 steps for quality generation
  - *From: DawnII*

- **FPS**: 24 fps
  - Native output framerate
  - *From: Kijai*

- **Resolution**: 1280x704
  - Default resolution for faster generation
  - *From: Gateway*

- **Resolution for 5B**: 720p minimum
  - Lower resolutions produce poor quality results
  - *From: comfy*

- **Precision for 5B**: fp16
  - fp8 causes lots of artifacts
  - *From: Kijai*

- **Steps for 14B with LightX**: 8 steps total (4+4)
  - Gives decent results with 14B i2v
  - *From: 1355535090716901396*

- **CFG for low step generation**: CFG 1
  - Works well with 4 steps on each stage
  - *From: hicho*

- **CFG**: 1
  - Used with 4 steps and no LoRA for good results
  - *From: Jas*

- **Steps for lightx2v**: 4 steps total or 6 steps (3+3)
  - Optimal performance with lightx2v LoRA
  - *From: multiple users*

- **Resolution for 5B model**: Minimum 1280x720
  - Lower resolutions don't work well
  - *From: Njb*

- **Sampler**: Euler, LCM, or UniPC
  - All work well with the models
  - *From: multiple users*

- **LightX2V strength**: 2.0-3.0
  - Higher strength needed for 2.2 compatibility
  - *From: multiple users*

- **CFG scale with LightX2V**: 1.0
  - Higher CFG causes issues
  - *From: 🦙rishappi*

- **Steps configuration**: 4 total (2+2 or 3+3)
  - Proper distribution between samplers
  - *From: multiple users*

- **Frame rate**: 24fps for 121 frames
  - Template default and optimal motion
  - *From: multiple users*

- **LightX2V LoRA strength**: 3.0 for first pass, 1.5 for second pass
  - Better quality than equal strengths
  - *From: Juampab12*

- **Steps for LightX2V**: 4-6 steps total (2+2 or 3+3)
  - Good balance of speed and quality
  - *From: multiple users*

- **CFG with LightX2V**: CFG 1 with UniPC beta sampler
  - Works well with speed LoRA
  - *From: cyncratic*

- **Frame count for 14B**: 81 frames at 16fps
  - Official specification, avoids looping issues
  - *From: aikitoria*

- **Step distribution**: 1 step high noise, 3 steps low noise (1/3 ratio)
  - Better balance and quality than even split
  - *From: DawnII*

- **LightX2V strength**: 3.0 first pass, 1.5 second pass
  - Optimal results reported by multiple users
  - *From: Juampab12*

- **Frame count with LightX**: 81 frames maximum
  - LightX lora breaks down above 81 frames
  - *From: gokuvonlange*

- **FPS setting**: 24fps preferred over 16fps
  - 16fps feels too slow, 24fps more natural
  - *From: gokuvonlange*

- **LightX adaptive quantile strength**: 3.0 for high noise, 1.5 for low noise
  - Reported to work great with dual model setup
  - *From: gokuvonlange*

- **LightX2V strength with 2.2**: 1.0
  - Lower strength needed, FastWan doesn't have much weighting
  - *From: DawnII*

- **Dual sampler step distribution**: Total steps same for both, e.g., 6 total: first sampler 0-3, second sampler 3-6
  - Maintains proper sampling trajectory
  - *From: Juan Gea*

- **Torch compile cache reservation**: --reserve-vram 2 (2GB)
  - Reserves VRAM for compilation cache
  - *From: Kijai*

- **CFG**: 1
  - Used with LightX2V and Euler sampler for fast generation
  - *From: thaakeno*

- **Steps**: 4 steps
  - Fast generation with CFG 1 and LightX2V
  - *From: thaakeno*

- **Shift**: Higher than 2, but not 8
  - Shift 2 is very bad, 8 is too high, values in between work better
  - *From: VRGameDevGirl84(RTX 5090)*

- **Default shift for Wan models**: 8.0
  - Default in native ComfyUI when no ModelSampling shift is specified
  - *From: Ablejones*

- **LightX2V strength**: 3
  - Used with high-noise model for better effect
  - *From: Hashu*

- **Block swap**: 20-40 for both models
  - Apply same block swap settings to both high and low noise models separately
  - *From: Kijai*

- **LightX2V strength**: 3.0
  - Better prompt adherence with high noise model
  - *From: Kijai*

- **VACE strength**: 4.0
  - Improved control on high-noise model section
  - *From: Ablejones*

- **CFG for high noise**: 1-3.5
  - Higher values make results worse
  - *From: VRGameDevGirl84*

- **FastWan on low noise**: 0.4
  - Good balance with LightX i2v at 1.0
  - *From: DawnII*

- **Frame count**: 121 vs 161 frames
  - Longer frames can break prompts
  - *From: Relven 96gb*

- **Shift parameter**: Around 8 (was 5 initially but got no motion)
  - Better motion generation
  - *From: Kijai*

- **Shift parameter alternative**: 4
  - Tested range 1-10, worked best for specific user
  - *From: VRGameDevGirl84(RTX 5090)*

- **Shift parameter**: 5
  - Better results than 8, closer to official recommendation
  - *From: Relven 96gb*

- **Steps for 5B model**: 40 steps (not 20)
  - Original code uses 50 steps default, ComfyUI 20 is too low
  - *From: orabazes*

- **High/Low boundary**: 15 steps (not 10)
  - Matches original code better
  - *From: aikitoria*

- **Sampler**: unipc (not euler)
  - Matches original code
  - *From: aikitoria*

- **Frame count**: 81 frames recommended, 121 can work but worse quality
  - Model designed for 81, longer reduces prompt adherence
  - *From: Kijai*

- **Quantization**: Q6 minimum, don't go below Q4
  - Quality preservation
  - *From: Kijai*

- **Scheduler**: simple
  - Matches what original code does best according to analysis
  - *From: aikitoria*

- **LightX2V lora strength**: 2.5 instead of 1.0
  - Significantly reduces blur
  - *From: A.I.Warper*

- **CFG**: 1.0
  - Works well with NAG sampler
  - *From: MysteryShack*

- **Steps for I2V**: 12 steps split at 6
  - Reduces blurring and corruption issues
  - *From: VK*

- **LightX2V for GGUF**: 2.0 strength at 4 steps
  - Optimal for GGUF models on lower VRAM
  - *From: Jonathan*

- **DPM2 SGM_uniform sampler**: 15+ steps
  - Works great, can use Euler simple for lower steps around 10
  - *From: Relven 96gb*

- **Shift parameter**: 5 on both passes
  - Helps with grayed out I2V results
  - *From: Akshvodae | Joe*

- **LightX2V LoRA strength**: 2.0 for both passes
  - 1.0 strength causes blurry mess
  - *From: Jonathan*

- **Sampler**: LCM/simple
  - Works best with LightX2V LoRA
  - *From: Jonathan*

- **CFG**: 1.0
  - Required for LCM sampler with speed LoRAs
  - *From: Jonathan*

- **FPS**: 16fps for 14B model
  - 24fps causes slow-motion appearance and worse motion
  - *From: Jonathan*

- **Steps**: 4-8 steps with LightX2V
  - All tested step counts work with proper settings
  - *From: Jonathan*

- **i2v LoRA strength**: 3.0 on HIGH noise, 1.0 on LOW noise
  - High noise model requires stronger strength
  - *From: Kijai*

- **Shift value**: 6 instead of 8
  - Higher shift values cause doubling and ghosting
  - *From: Charlie*

- **LightX2V strength**: 3.0 for high noise, 1.0 for low noise
  - Optimal balance for two-stage generation
  - *From: Kijai*

- **Steps configuration**: 4 steps each (8 total), split at step 4
  - Efficient generation with good quality
  - *From: SonidosEnArmonía*

- **CFG**: 1.0
  - Works well with Euler simple scheduler
  - *From: CDS*

- **Resolution**: Must be multiples of 64
  - Prevents matrix mismatch errors
  - *From: MysteryShack*

- **VRAM usage**: 640x640 takes 21.7gb VRAM on 81 frames, 768x768 wan2.2 81 frames is 23.5gb VRAM
  - Hardware planning
  - *From: ✧ฅโ๑ↀᆺↀ ๑ใฅ✧PookieNumnums*

- **Block size**: 64 vs 128
  - 64 is slower than 128 but helps balance VRAM usage
  - *From: Kijai*

- **CFG scheduling**: 2.0 for first step, 1.0 for remaining steps
  - Kickstarts more motion and prompt adherence
  - *From: Kijai*

- **Resolution for 5B model**: 720x720 or higher
  - 5B model needs high resolution to work properly
  - *From: Kijai*

- **LightX2V LoRA strength**: 3 for HIGH, 1 for LOW
  - Model differences require higher strength on high noise
  - *From: gokuvonlange*

- **CFG**: 1-2
  - CFG 1 for speed, CFG 2 for better prompt adherence on complex prompts
  - *From: gokuvonlange*

- **Block swap**: 35-40 blocks
  - Memory management for 4090 users
  - *From: Sal TK FX*

- **Step count**: 4 steps total
  - Split as 0-2 for high noise, 2-4 for low noise
  - *From: gokuvonlange*

- **Use non-blocking**: Off
  - Prevents memory allocation errors
  - *From: Kijai*

- **Return with leftover noise**: On for high noise sampler
  - Essential for proper dual sampler workflow
  - *From: Kijai*

- **start_step**: 0
  - Required for first sampler in new wrapper setup
  - *From: Kijai*

- **lightx2v LoRA strength**: 3.0 for first pass, 1.0 for second pass
  - Optimal settings for two-pass generation
  - *From: fredbliss*

- **frames**: 81 frames for stability, 121 for native
  - 81 frames more stable with lightx, 121 frames native to model but can cause reversals
  - *From: N0NSens*

- **Denoise for second sampler**: 0.5
  - Works well in two-stage workflow
  - *From: hicho*

- **CFG value**: 2
  - Good balance for quality
  - *From: AJO*

- **Steps for fast generation**: 6 steps
  - Achieves good results in shorter time
  - *From: AJO*

- **Block swap setting**: 30 blocks instead of 40
  - Better memory management for 4090
  - *From: Kenk*

- **Scheduler**: dpm++_sde
  - Default scheduler that works well
  - *From: BobbyD4AI*

- **LightX2V strength**: 3.0 on HIGH, 1.0 on LOW
  - Restores prompt adherence and prevents color bleaching
  - *From: gokuvonlange*

- **Context overlap**: 64 for high noise, 16 for low noise
  - Produces clean long sequences
  - *From: Kijai*

- **Frame limit**: 81 frames max
  - Going above causes ping-pong effects
  - *From: aikitoria*

- **Split step ratio with LightX2V**: May need adjustment from default 50/50
  - LightX2V affects the recommended split
  - *From: MilesCorban*

- **LightX2V LoRA strength**: 2 steps
  - Alternative to high pass workflow
  - *From: Rainsmellsnice*

- **Frame count with LightX2V**: 81 frames max
  - Beyond this causes weird motion or cuts
  - *From: NebSH*

- **Sampling steps for quality**: 40 steps
  - Eliminates grid stepping artifacts present in low sample counts
  - *From: aikitoria*

- **CFG scheduling**: CFG Schedule Float List
  - Used with Wan 2.1 for better results
  - *From: N0NSens*

- **Sampler for Wan 2.2 5B**: flowmatch_pusa
  - Only sampler that currently works with 5B model
  - *From: Kijai*

- **Steps for 14B with LightX2V**: 4 steps (2+2)
  - Works for both T2V and I2V
  - *From: Daflon*

- **CFG and steps for 14B**: 8 steps, 4/4
  - Good balance of speed and quality
  - *From: Juan Gea*

- **Resolution for 5B**: 1024x1600x121 or 1024x1952x121
  - Higher resolution works well on 24GB
  - *From: TK_999*

- **Scheduler change**: LCM/beta57
  - For specific generation needs
  - *From: Juan Gea*

- **Block swap blocks**: 40 blocks
  - Optimal for 64GB RAM systems
  - *From: VK (5080 128gb)*

- **LightX2V I2V strength on high model**: 2 or 3
  - Good results when using I2V LoRA for T2V
  - *From: phazei*

- **Steps combination**: 2+3 or 4+4
  - Balance between quality and memory usage
  - *From: phazei*

- **Denoise for vid2vid**: 0.1
  - Low denoise makes output look more like source video
  - *From: VK (5080 128gb)*

- **Non-blocking on block swap**: disabled
  - Better memory management and error visibility
  - *From: Daflon*

- **FastWan + LightX2V combination**: high: light:2 fastwan:1, low: light:1 fastwan:1
  - Enhanced results with combined LoRAs
  - *From: phazei*

- **Frames**: 81 for 14B, 121 for 5B
  - 14B model trained for 81 frames, 5B for 121
  - *From: MiGrain*

- **FPS**: 16 for 14B, 24 for 5B
  - Model-specific training parameters
  - *From: N0NSens*

- **LightX2V LoRA strength**: 1.0 to 3.0
  - Compensates for lack of cfg, higher strength for high noise model
  - *From: Kijai*

- **Shift**: 8
  - Works fine, though differences hard to track across seeds
  - *From: thaakeno*

- **lightx2v lora strength**: rank64, 2.0 strength on both samplers, LCM/simple, 4 steps (0,2 and 2,4), 1 CFG, 6 shift
  - Optimal performance settings
  - *From: Jonathan*

- **Beta57 scheduler**: Same as beta scheduler with parameters 0.5 and 0.7
  - Better handling of two sampling regimes
  - *From: Ablejones*

- **FastWan + LightX2V combination**: LightX2V 1.0 + FastWan 0.8, 2high/2low for 4 total steps
  - Best motion with res_6s beta57
  - *From: Ant*

- **Denoise strength for upscaling**: 0.2 instead of 0.6
  - Fixes upscaling issues in WanVideo Sampler
  - *From: hiroP*

- **LightX2V lora strength**: 3.0 on high noise model
  - Most people running at this strength, higher than typical 0.8
  - *From: Ablejones*

- **VACE strength**: 1.5
  - Prevents background inconsistencies vs 1.0 strength
  - *From: seitanism*

- **Steps split**: 3 steps high, 11 steps low
  - Balances quality and speed
  - *From: TK_999*

- **High noise steps**: 6 steps
  - Enough to confirm tones, lights and movements
  - *From: slmonker*

- **Low noise steps**: 3-4 steps
  - Sufficient for refinement when using distill LoRA
  - *From: slmonker*

- **Shift value**: Around 8
  - Wan 2.2 seems to work better around shift 8
  - *From: zelgo_*

- **CFG for high noise**: 3.5
  - Good balance for first sampler in split setup
  - *From: gokuvonlange*

- **CFG for low noise**: 1
  - Works well with distill LoRA on second sampler
  - *From: gokuvonlange*

- **Frame rate**: 14B: 16fps, 5B: 24fps
  - Official specifications for each model variant
  - *From: Rainsmellsnice*

- **Optimal 6-step configuration**: HighNoise: CFG 3, 1 step, No LoRA | HighNoise: CFG 1, 2 steps, LightX2V 3.0 | LowNoise: CFG 1, 3 steps, LightX2V 1.0
  - Best balance of speed to quality
  - *From: Ablejones*

- **Juampab12's optimized settings**: HighNoise: CFG 1, 3 steps, LightX2V 3.0, ddim shift 7.75 | LowNoise: CFG 1, 3 steps, LightX2V 2.5, ddim shift 9.0
  - User-optimized configuration
  - *From: Juampab12*

- **Speed generation settings**: 4-5 steps total, 5 minutes for 3 second video
  - Good balance for experimentation
  - *From: homem desgraca*

- **5B model steps**: 30 steps
  - Default from ComfyUI workflow for decent results
  - *From: garbus*

- **5B model resolution**: 1280x704 or 704x1280
  - Model requires these specific resolutions
  - *From: Benjimon*

- **LightX2V LoRA strength**: Rank 64
  - Commonly used setting for low step generation
  - *From: VK (5080 128gb)*

- **CausVid LoRA strength**: 0.25
  - Good balance for motion improvement
  - *From: Simjedi*

- **Vid2vid start steps**: Start step 3 of 12 total
  - Good balance for maintaining input video similarity
  - *From: VK (5080 128gb)*

- **Total steps**: 10, split at 7, start at values close to split for subtle changes
  - Controls how much change occurs in vid2vid
  - *From: VK (5080 128gb)*

- **Uni3C strength**: 3.0 for high noise sampler, off or 1.0 for low noise
  - WAN 2.2 requires much higher strength than typical
  - *From: Kijai*

- **Frame count**: 81 frames optimal, avoid 121+ frames
  - Model not trained for longer sequences, causes looping issues
  - *From: Kijai*

- **Denoise threshold**: 0.5 or higher
  - Below 0.5 causes index errors
  - *From: Flipping Sigmas*

- **LoRA rank**: Anything past rank16 viable, minimal gains after 128
  - Lower rank is faster and uses less VRAM
  - *From: Kijai*

- **cfg schedule**: 2.0 for first step, then 1.0 for rest with lightx2v
  - Proper CFG scheduling for distill LoRA
  - *From: Kijai*

- **high/low steps without distill**: 7 high steps at 3.5 cfg, 3 low steps with distill lora at cfg 1
  - Alternative to using distill on both samplers
  - *From: seitanism*

- **lightx lora strength on high model**: Higher than 1, try 3
  - Need more action/motion in output
  - *From: smithyIAN*

- **block offloading**: 40 blocks offloaded for 14B model
  - Reduces VRAM usage from 24GB+ to ~21GB
  - *From: hiroP*

- **resolution**: 1280x704 or 1280x720
  - Standard resolutions for WAN models
  - *From: seitanism*

- **Stride**: 8-10
  - Higher values like 16 crash ComfyUI, creates effective window mixing
  - *From: Kijai*

- **High noise steps**: 5
  - Works well with 4 distilled low steps
  - *From: seitanism*

- **Distill strength and CFG for T2V**: str 1.0, cfg 3.0
  - Prevents weirdness with people interacting
  - *From: IceAero*

- **I2V settings**: CFG 1, accvid 1.5, lightx 2.5-3
  - Standard I2V configuration that works well
  - *From: DawnII*

- **LightX2V LoRA strength**: 2.5
  - Appears to be optimal strength setting
  - *From: Jonathan*

- **CFG for both high and low noise**: 3/2.5
  - Good balance, can try no lightx on high noise with cfg for better prompt adherence
  - *From: Juampab12*

- **Steps for quality generation**: 15+15 steps
  - At 256x256 resolution without speed LoRAs produces much better quality
  - *From: mamad8*

- **LightX strength for motion fix**: 0.25
  - Fixes drunkeness with minimal drawback in prompt adherence
  - *From: Juampab12*

- **Frame rate preference**: 24fps
  - Often looks better than 16fps, model may be intended for 24fps
  - *From: Juampab12*

- **LightX2V strength for quality**: 6.0
  - Still maintains fine quality while providing speed boost
  - *From: Kijai*

- **LightX quantile strength for first pass**: strength 3 with cfg 1, or strength 0.25 with cfg 5
  - Optimal quality balance
  - *From: Juampab12*

- **LightX quantile strength for second pass**: strength 2.5 with cfg 1
  - Best results in testing
  - *From: Juampab12*

- **CFG recommendation for 2.2**: cfg 5 for better prompt adherence
  - Much better prompt following
  - *From: Juampab12*

- **Steps configuration for 2.2**: 3/3 steps (3 steps each pass)
  - Better prompt adherence than other configurations
  - *From: Juampab12*

- **CFG with LightX**: 2.0 maximum
  - Prevents artifacts and overcooked contrast
  - *From: gokuvonlange*

- **LightX LoRA strength**: 1.00 on 2nd pass
  - Reduces generation time from 465s to 166s
  - *From: VRGameDevGirl84*

- **Steps configuration**: 20 steps CGF 3.5 Shift 8
  - Good baseline without loras or lightX
  - *From: VRGameDevGirl84*

- **Q8 FP16 configuration**: shift 8, 16 steps, switch step at 14, low step at 6
  - Produces really good results
  - *From: GOD_IS_A_LIE*


## Concepts Explained

- **distil loras**: Speed optimization loras including causvid, accvid, light2x, self-forcing lora that use different sampling approaches
  - *From: Vardogr*

- **thermal throttling**: GPU automatically reducing performance when temperatures reach ~90C to prevent damage
  - *From: MysteryShack*

- **Self forcing vs causal models**: LightX2V is trained using self forcing but isn't causal, while initial self forcing model was also causal - creates confusion
  - *From: Kijai*

- **Mask sampler technique**: Runs sampler twice (with/without condition) for low frequency detail, takes diff to create mask for main condition
  - *From: Mads Hagbarth Damsbo*

- **MultiTalk L-Rope**: Could potentially be modified for control of specific body parts, not just lips
  - *From: Tango Adorbo*

- **SAGEATT++**: About 5% faster at standard sizes, 7% faster at 1280x720x81
  - *From: Kijai*

- **Context windows**: Method to pass context along for longer videos but doesn't make context strong
  - *From: Draken*

- **VACE T2V**: Using VACE workflow without input image for better prompt adherence
  - *From: Rainsmellsnice*

- **Temporally compressed frames**: 4 frames compressed into latent representation, only Skyreels A2 uses this
  - *From: Kijai*

- **Motion_frame parameter**: Setting that affects context windowing behavior, possibly controls overlap between frames
  - *From: Kijai*

- **Block swap**: Memory management technique to handle large models by swapping model blocks between VRAM and RAM
  - *From: Kijai*

- **Low_mem_load**: Loading weights one by one and applying LoRA, then moving to RAM to prevent VRAM spikes
  - *From: Kijai*

- **Block conditioning**: Injecting different prompts or conditions into specific DiT blocks to control different aspects - early blocks control fine details/textures, middle blocks blend local/global structure, late blocks control global coherence/scene layout
  - *From: Mads Hagbarth Damsbo*

- **Self-forcing LoRA**: A LoRA that enables very fast inference (4-8 steps) at CFG 1.0 by essentially distilling the model behavior
  - *From: izashin*

- **Grey masking in VACE inpainting**: Grey areas in RGB input tell model to generate content, combined with white mask for precise control
  - *From: Rishi Pandey*

- **Context windows in video generation**: Separate generations blended together with overlap on each step, model sees them as individual gens with noise/latents and control info
  - *From: Kijai*

- **Audio-driven cross attention**: Method used by FantasyTalking and MultiTalk to add audio conditioning to video models
  - *From: Kijai*

- **Asymmetric distillation**: Extends CausVid framework, breaks bidirectional teacher context into smaller chunks with causal attention across chunks
  - *From: ZeusZeus (RTX 4090)*

- **Tile LoRA**: Functionally identical to a tile controlnet, makes upscaling easier by training on tiled image data
  - *From: David Snow*

- **4n+1 frame aliasing**: Wan wrapper rounds frame counts to nearest value following 4n+1 formula, causing unpredictable frame count outputs
  - *From: samhodge*

- **Audio CFG in wav2vec**: Does a 3rd pass that helps separate audio results from normal results, requires normal CFG and increases inference time 3x
  - *From: Kijai*

- **Uni3c context windows**: Reduces movement in videos but provides consistency, not needed if input doesn't introduce camera movement
  - *From: Kijai*

- **VACE module vs full model**: VACE module (Wan2_1-VACE_module_14B_bf16.safetensors) should be used instead of full model for inpainting tasks
  - *From: Hashu*

- **LightX2V distillation**: Speed LoRA designed to reduce steps needed, meant for 4 steps, overcooks at higher step counts
  - *From: Draken*

- **Two-stage sampling**: Complex sampling method that may help with motion compliance issues when using distilled LoRAs
  - *From: Ethan*

- **fp8_e5m2 vs fp8_e3m4fn**: fp8_e3m4fn has 3 bits for the exponent, while fp8_e5m2 has 5 bits, making e5m2 higher quality when converted properly
  - *From: patientx*

- **Context window snapping**: In I2V models with context windows, every window needs the input image so if output drifts too far from it, it snaps back
  - *From: Kijai*

- **E5M2 vs E4M3FN**: E5M2 uses 5 bits for exponent and 2 for mantissa (wider range, lower precision). E4M3FN uses 4 bits for exponent and 3 for mantissa (narrower range, higher precision). Both are same size in memory.
  - *From: Kijai*

- **FP8 quantization process**: Master weights stay in FP16/BF16 for accuracy and are converted to scaled FP8 format only for computation-heavy steps. Uses dynamic scaling factor to prevent overflow/underflow.
  - *From: Kijai*

- **Regional compile in torch 2.5**: Feature in inductor that makes compiling identical layers super fast in transformer models, reduces compile time from 5-30 minutes to few seconds
  - *From: Kijai*

- **Differential diffusion mask**: Mask that allows different diffusion strengths for different parts of the image/video
  - *From: David Snow*

- **FreeInit**: Old AnimateDiff method that runs process multiple times for consistent motion through noise filtering
  - *From: Kijai*

- **VACE mask types**: Two mask types: grey inpainted areas on video, and black/white input mask for encoder control
  - *From: Valle*

- **LoRA Alpha**: Baked in strength values per layer, different from LoRA strength setting
  - *From: Kijai*

- **VACE control video**: Must match generation frame count for proper operation
  - *From: Juampab12*

- **Static points in ATI**: Points that show model you don't want camera movement
  - *From: Juampab12*

- **VACE addon module vs base model**: Addon module (~6GB) is VACE extracted for use with other models, base model (~30GB) is the full implementation
  - *From: DawnII*

- **Context windows in video generation**: Helps with longer clips but has motion quality hit and memory limitations
  - *From: Kijai*

- **torch.compile invalidation**: Recompiles when input changes besides batch size, can be optimized by not compiling prompts
  - *From: TK_999*

- **First frame vs reference in VACE**: First frame input is different from reference input - image should go into first frame for proper temporal consistency
  - *From: Draken*

- **Context windows**: Method that runs model multiple times and blends results on each step, works with any model without training but incompatible with I2V models
  - *From: Kijai*

- **RoPE chunking**: Processing RoPE (Rotary Position Embedding) calculations in chunks to reduce peak VRAM consumption
  - *From: Kijai*

- **FusionX**: Collection of LoRAs that make up a fusion system, not a single model
  - *From: VRGameDevGirl84*

- **Boilerplate negative**: Large negative prompt, though it may not work with LightX2V
  - *From: lostintranslation*

- **Differential diffusion mask**: Made by taking difference between original plate and explosion pass run for few steps, used with animated masks
  - *From: pookyjuice*

- **BlockSwap in SeedVR2**: Technique that makes VRAM consumption manageable for video upscaling, though VAE still uses significant VRAM
  - *From: Adrien Toupet*

- **Temporal consistency in upscaling**: Higher batch sizes needed to maintain consistency between frames - batch size 1 breaks temporal consistency like ESRGAN
  - *From: Adrien Toupet*

- **RoPE and FFN chunking**: Memory optimization technique that chunks both RoPE (initial spike) and FFN layers (huge pillar) to reduce VRAM usage
  - *From: Kijai*

- **VACE ref_images concatenation**: Parameter accepts multiple reference images but automatically concatenates them - not suitable for video input
  - *From: Kijai*

- **Context window shifts**: Issue where video generation snaps back to starting image every 81 frames due to insufficient overlap
  - *From: A.I.Warper*

- **Chunked RoPE**: Feature that drastically reduces VRAM use when not using torch.compile
  - *From: Kijai*

- **Shift parameter**: Modifies the sigmas and sigmas modify noise strength, more shift equals stronger noise
  - *From: Kijai*

- **Easy Cache method**: Checks input/output difference with no calibration, works but doesn't work with samplers that add noise like dpm++_sde and lcm
  - *From: Kijai*

- **Self-forcing in step cfg distill**: The step cfg distill is trained with self-forcing, so 14B model has this capability
  - *From: Kijai*

- **VACE white border requirement**: Reference images need white border around them to work with VACE
  - *From: Hashu*

- **Vectorized timesteps**: Architecture that supports arbitrary frame conditioning, similar to LTXV
  - *From: spacepxl*

- **Diffusion forcing**: Autoregressive style diffusion technique
  - *From: spacepxl*

- **LoRA rank 512**: Very high rank LoRA used in Pusa, resulting in 4GB file size
  - *From: Kijai*

- **NAG (Negative Augmented Generation)**: Allows use of negative prompts with WAN, particularly useful at CFG 1.0
  - *From: The Shadow (NYC)*

- **Low amplitude repaint**: Using WAN T2V model to refine an existing image with minimal changes
  - *From: slmonker(5090D 32GB)*

- **Mid-generation control introduction**: Adding control inputs like depth or lineart during middle steps of generation rather than from start
  - *From: DawnII*

- **Shape mismatch warnings**: LoRA key not loaded warnings that appear but don't prevent functionality
  - *From: Piblarg*

- **Rank 16 vs Rank 64 LoRA**: Higher rank LoRA (64) vs lower rank (16), affects model complexity
  - *From: Ada*

- **torch.svd_lowrank**: Method for fast LoRA extraction that's 30x faster than previous methods while maintaining good results
  - *From: Kijai*

- **diff_m**: Difference of modulation - a parameter in LoRA training that may not have significant effect in inference
  - *From: DawnII*

- **LightX2V distillation**: Now have 4 different models: original T2V, new T2V v2, 480P I2V, and 720P I2V (pending)
  - *From: Kijai*

- **Bong_tangent sampler**: Custom sampler from ClownsharkBatwing's RES4LYF nodeset that improves generation quality
  - *From: JohnDopamine*

- **Per-frame timesteps**: Pusa uses different timesteps for each frame, requiring model modifications, similar to Diffusion Forcing approach
  - *From: Kijai*

- **VTA Components**: Vectorized Timestep Adaptation components in Pusa - separate layers for temporal control that aren't standard LoRA pairs
  - *From: JohnDopamine*

- **Pusa**: More like a new model in lora format that changes how T2V model works, not a regular lora
  - *From: Kijai*

- **Flowmatch_pusa scheduler**: New scheduler required for Pusa that expands timesteps so each latent has its own
  - *From: Kijai*

- **VACE module**: A module for T2V model, not I2V itself
  - *From: Kijai*

- **Radial sparse attention**: Attention mechanism that uses dense steps for initial processing then sparse attention for remaining steps, providing speed improvements
  - *From: Kijai*

- **Dense vs sparse timesteps**: Dense steps use full attention, sparse steps use optimized radial attention for speed
  - *From: Kijai*

- **ATI coordinate control**: Takes JSON coordinates directly rather than frame references for precise object trajectory control
  - *From: Juampab12*

- **Block swapping**: Memory management technique that swaps model blocks between VRAM and RAM to handle larger models on limited VRAM
  - *From: Juampab12*

- **RunPod Serverless**: Dockerized workers that start on request, process the task, and respond with results. Only charges for processing time, waiting is free
  - *From: Juampab12*

- **Radial attention**: Attention mechanism that can be faster but affects quality. Has configurable start step to balance speed vs quality
  - *From: Kijai*

- **Radial/sparse attention**: Speed optimization that uses sparse attention for most steps, dense attention only for critical timesteps. Benefits scale with resolution
  - *From: Kijai*

- **Dense timesteps**: Number of steps using full attention in radial attention mode, rest use sparse attention
  - *From: Kijai*

- **Adaptive rank**: LoRA technique using different ranks per layer, similar to lycoris/locon approach
  - *From: Kijai*

- **Radial attention sparse/dense steps**: Sparse steps are faster, dense steps maintain quality. Each step goes through 40 blocks.
  - *From: Kijai*

- **VACE reference positioning**: VACE uses references in the position you put them or similar but not exact, unlike Phantom which has better reference accuracy
  - *From: Piblarg*

- **Context windows with PUSA**: PUSA scheduler causes timestep expansion to full frame count, incompatible with context window splitting
  - *From: Kijai*

- **I2V model channel structure**: Image + mask, so 16 for noise + 16 for image + empties + 4 for mask so I2V model input is 36 channels, while T2V model input is always just the 16
  - *From: Kijai*

- **Radial Sage Attention block size**: Block size refers to the attention mask, sort of tile size. Not transformer blocks but attention mask tiling
  - *From: Kijai*

- **Phantom model sensitivity**: Phantom is very sensitive and any less of it destroys it, while VACE is robust, but I2V stuff is the first to break
  - *From: Piblarg*

- **Phantom latent dropping**: Phantom latents are cut at end of sampling, not beginning like some other models
  - *From: Kijai*

- **I2V vs T2V architecture difference**: Different number of channels to account for image attention - can't merge I2V and T2V models
  - *From: DawnII*

- **PUSA proper usage**: PUSA is meant for T2V with proper scheduler and inserting images into latents, not as LoRA on I2V
  - *From: Kijai*

- **Radial attention**: Provides more speed with some quality sacrifice, fixed bugs related to resolution changes
  - *From: Kijai*

- **PUSA LoRA compatibility**: Existing LoRAs don't work well with PUSA regardless of strength - they'd need to be trained specifically on Pusa
  - *From: phazei*

- **Wan frame limitations**: Model not trained for >93 frames, causes flash at start. Skyreels can do 121 vs vanilla's 81 frame limit
  - *From: Kijai*

- **PUSA timestep expansion**: PUSA expands timesteps so every frame gets its own noise level, allowing control of what frame is used as reference and what is denoised
  - *From: Kijai*

- **Unmerged LoRA system**: LoRA weights are applied as patches on the fly during inference instead of being merged at the beginning, allowing instant weight changes
  - *From: Kijai*

- **fp8 scaled models**: Models where more components are kept at full precision compared to normal fp8 quantization
  - *From: Kijai*

- **VACE masking**: White masks tell VACE to generate new content for those areas using only control signal, black masks preserve existing content
  - *From: Ablejones*

- **FP8 scaling**: Method to quantize models from fp32 to fp8 while maintaining quality closer to fp16, involves scaling factors
  - *From: Kijai*

- **PUSA scheduler**: Allows setting custom timestep values (0-1000) for different frames, 0 for init frame or frames you don't want denoised
  - *From: Kijai*

- **Radial attention**: Attention mechanism that provides speed improvements, currently caps speed so focus should shift to optimizing FFN and rope components
  - *From: Kijai*

- **Non-blocking block swap**: Pins RAM to allow async device transfers for faster performance but reserves more VRAM as pinned memory can't be instantly freed
  - *From: Kijai*

- **Radial attention**: Sparse attention with mask designed for video models - doesn't need LoRA to function, just applies attention mask
  - *From: Kijai*

- **PUSA functionality**: LoRA that makes Wan 14B T2V work as I2V model with extension capability, similar to VACE and Fun InP - works by extending timesteps to frame count
  - *From: Kijai*

- **Text encoder caching**: Stores processed text embeddings to disk to avoid re-encoding unchanged prompts after ComfyUI restarts
  - *From: Kijai*

- **Block swap vs VRAM management**: Different memory management approaches, block swap works better with Set LoRA node
  - *From: hicho*

- **Full distill mode**: Faster generation mode, great for quick iterations
  - *From: hicho*

- **Context windows**: Method to extend video generation beyond normal limits while maintaining VRAM efficiency
  - *From: Kijai*

- **MAGREF padding strategy**: Using white-padded images as reference vs first frame in different context windows
  - *From: Kijai*

- **Bundle optimization**: Computer vision technique to determine camera movement from point features
  - *From: samhodge*

- **VACE masking**: Two types of masking: input frames use 0.5 gray for empty areas to fill (spatial/temporal inpainting), and actual mask marks what can/can't be changed
  - *From: Kijai*

- **Video extension workflow**: Load video, cut into reference and original parts, pad reference to 81 frames, generate new video with reference frames, stitch after original frames
  - *From: lostintranslation*

- **Scaled models**: Models that have scaling applied to weights, can be merged with LoRAs by applying scale first
  - *From: Kijai*

- **Context overlap**: Feature that doesn't affect text timing in generations
  - *From: VK (5080 128gb)*

- **Out of distribution problem**: Doing inference outside of training data, like using 1080p when model trained on 720p
  - *From: samhodge*

- **Text encoder cache system**: Prompt-based cache that keeps TE on CPU and skips processing if prompt already cached
  - *From: mamad8*

- **PUSA correct usage**: Must use T2V models with flowmatch_pusa scheduler and inject frames as extra latents, not as I2V input
  - *From: Kijai*

- **4+1 rule for frame overlap**: When extending videos, use multiples of 4+1 frames for overlap (like 13 frames)
  - *From: Kijai*

- **Reinforcement Learning in WAN 2.2**: Uses RL to increase probability of good outcomes and decrease bad ones, simplifies prompt effects so simple prompts work better
  - *From: 青龍聖者@bdsqlsz*

- **Self-forcing training technique**: Training technique that enables very fast generation, used in lightx2v distill and 1.3B models
  - *From: Kijai*

- **DiffusionForcing workflow**: Technique where Pusa can extend videos from any number of input frames
  - *From: Kijai*

- **Key backup in LoRA merging**: System that backs up non-merged keys during LoRA application, consumes significant RAM
  - *From: Kijai*

- **PUSA extension**: Alternative method for video extension that avoids quality degradation issues of VACE cross-fading
  - *From: The Shadow*

- **NABLA optimization**: Technique using flex attention and radial attention to achieve 50% inference time reduction
  - *From: DawnII*

- **Context windows**: Method for endless generation but with downside of less dynamic motion, becomes repetitive
  - *From: Kijai*

- **v2v vs t2v**: Video-to-video uses existing video as input vs text-to-video generates from scratch
  - *From: samhodge*

- **LoKR**: A training method that's much smarter and smaller than regular LoRA. Can achieve decent results training only single blocks with tiny file sizes (1.2mb)
  - *From: jikan*

- **Differential diffusion**: The method used by WAN's mask encode node for inpainting, doesn't do latent masking so requires compositing result on original
  - *From: Kijai*

- **VSA (Video Sparse Attention)**: Attention mechanism that may only be usable on H100 GPUs, includes gate_compress layer
  - *From: Kijai*

- **Pusa LoRA**: Makes T2V model able to use images, supports multiple images for extension and start/end frame functionality
  - *From: Kijai*

- **NAG (Negative Guidance)**: Technique that allows negative prompts to work even at CFG 1.0, effective at controlling unwanted behaviors
  - *From: Kijai*

- **EchoShot cross-attention splitting**: Technique only affects cross attention (text conditioning), model weights tuned for multiple prompt handling
  - *From: Kijai*

- **Prompt bleeding**: When different scene prompts influence each other unintentionally, creating mixed results
  - *From: Kijai*

- **Self-forcing LoRA**: LoRA technique for consistency, LightX is essentially self-forcing adapted to 14B
  - *From: DawnII*

- **Block swap**: Moves model components to RAM to free VRAM, can save up to 16GB on fp8
  - *From: Kijai*

- **Tiled VAE**: Processes video frames in sections to avoid VRAM OOM on decode
  - *From: Kijai*

- **Chunked rope**: Memory optimization technique for handling long sequences
  - *From: Kijai*

- **FFLF**: First-Frame-Last-Frame morphing for T2V generation
  - *From: hicho*

- **Temporal VAE**: VAE that has cross-information between frames, making it impossible to join Wan outputs in latent space
  - *From: Kijai*

- **MoE architecture**: Mixture of Experts using high/low noise expert split with dual models at different timesteps
  - *From: community*

- **First frame handling**: First frame is processed differently by Wan VAE, causing issues when cutting latent batches
  - *From: Kijai*

- **Block swap**: Simplest way to offload model parts between GPU and CPU memory during inference
  - *From: Kijai*

- **VRAM peaks**: The most intense memory usage moments during inference - you need to fit these peaks in VRAM, other parts use far less
  - *From: Kijai*

- **Dual model structure (Wan 2.2)**: Uses high noise and low noise models - first model handles early timesteps up to 875, second model handles remaining timesteps
  - *From: Kijai*

- **15fps as efficiency measure**: 15fps is more a way to try get longer video lengths from fewer latents, since 30fps would halve video length
  - *From: Draken*

- **A14B model architecture**: Uses 2 models (high and low noise) run sequentially, high noise up to timestep 875 then low noise for rest
  - *From: Kijai*

- **TI2V-5B model**: Unified Text and Image to Video model, uses new Wan2.2 VAE
  - *From: phazei*

- **Context options**: Feature allowing infinite frame length generation when sufficient VRAM available
  - *From: samhodge*

- **MoE (Mixture of Experts)**: Architecture with high-noise and low-noise expert split, requires separate LoRA adapters for each expert with different timestep schedules
  - *From: seruva19*

- **HDR (High Dynamic Range)**: Light values range from 0 to 1000000 instead of traditional 0 to 1.0 range
  - *From: samhodge*

- **Traveling context windows**: Method mentioned for longer video generation, though noted as 'not so mint' by user
  - *From: samhodge*

- **MoE architecture with noise expert split**: High noise expert for early stages/layout, low noise expert for later stages/details
  - *From: mrassets*

- **TI2V**: Text or Image to Video - single model supporting both input types
  - *From: Juampab12*

- **MoE (Mixture of Experts) in Wan 2.2**: Uses separate models for high noise and low noise stages, similar to SDXL refiner concept but for different noise levels
  - *From: multiple users*

- **High/Low noise expert split**: 14B model uses one expert for high noise denoising and another for low noise denoising
  - *From: multiple users*

- **MoE architecture with High/Low noise expert split**: Wan 2.2's architecture splits processing between high noise and low noise expert models for better quality
  - *From: context*

- **VAE stride scaling**: Proper dimension scaling needed with new VAE to avoid accidental resolution doubling
  - *From: Kijai*

- **MoE (Mixture of Experts)**: Architecture where you mix the expert models yourself rather than automatic switching
  - *From: Rainsmellsnice*

- **High/Low noise expert split**: 2.2 uses separate models for high noise and low noise phases of generation
  - *From: multiple users*

- **Sigma scheduling**: Each step uses progressively lower sigma values, end step and start step don't use same sigma
  - *From: JohnDopamine*

- **MoE architecture**: Mixture of Experts with High/Low noise expert split in WAN 2.2
  - *From: multiple users*

- **Dual model system**: WAN 2.2 uses separate models for high-noise and low-noise processing
  - *From: aikitoria*

- **High noise vs Low noise models**: High noise model handles early denoising steps and determines light perception/texture. Low noise model handles final steps and is similar to 2.1 with more training
  - *From: Ablejones*

- **SNR metric splitting**: Original model page specified splitting by Signal-to-Noise Ratio rather than just step count
  - *From: Ablejones*

- **Multistep sampler limitations**: Can't properly split multistep samplers (2m, 3m variants) using normal KSampler due to needing multiple previous latents
  - *From: Ablejones*

- **High/Low noise expert split**: 2.2 uses MoE architecture where high noise model handles early denoising steps and low noise model handles final steps
  - *From: multiple users*

- **Blockswap**: Memory management technique for switching between models during generation, can cause memory issues with dual models
  - *From: Draken*

- **High/Low noise expert split**: 2.2 MoE architecture splits processing between high noise and low noise experts for different denoising stages
  - *From: Multiple users*

- **ModelSamplingSD3 to 2**: Setting that doesn't work well with 2.2 unlike with 2.1
  - *From: GOD_IS_A_LIE*

- **High noise vs Low noise models**: 2.2 uses split architecture where high noise model handles early denoising, low noise handles refinement
  - *From: Kijai*

- **Crossattn selection**: T2V vs I2V selection, 2.2 doesn't use img crossattn
  - *From: Kijai*

- **Timestep alignment**: High noise model used when timestep > 0.9, can be affected by distill LoRAs
  - *From: aikitoria*

- **High/Low noise expert split**: Wan 2.2 uses separate models for different noise levels - high noise for composition/motion, low noise for details
  - *From: mamad8*

- **Timestep boundary**: High noise model handles timesteps above 875, low noise handles below 875
  - *From: mamad8*

- **Radial attention**: Attention mechanism that can be used with Wan models for different generation patterns
  - *From: MysteryShack*

- **MoE (Mixture of Experts) architecture**: Wan 2.2 uses High/Low noise expert split requiring two-stage generation process
  - *From: MatiaHeron*

- **Radial attention**: Speed optimization that makes timecost more linear instead of exponential for longer generations
  - *From: MysteryShack*

- **Reserve VRAM flag**: Adds estimated memory to what ComfyUI thinks is needed, but doesn't guarantee actual reservation
  - *From: Ablejones*

- **High/Low noise model architecture**: Wan 2.2 uses separate models for high and low noise passes, can be mixed with older models
  - *From: Kijai*

- **CFG scheduler**: Sets first step to use CFG and rest not, used for controlling guidance
  - *From: Kijai*

- **High/Low noise expert split**: Wan 2.2 uses MoE architecture with separate models for high noise and low noise stages
  - *From: blake37*

- **TAEW previews**: Preview system that shows motion development clearly even at 2 steps
  - *From: Kijai*

- **Radial attention**: Attention mechanism that can improve or hurt results depending on model stage used
  - *From: Kijai*

- **High/Low noise expert split**: 2.2 uses MoE architecture where high noise model handles early denoising steps with better prompt adherence and motion, low noise model handles final steps
  - *From: Kijai*

- **Block swap**: Technique to offload model blocks to CPU RAM to manage VRAM usage
  - *From: Multiple users*

- **CFG scheduling**: Using different CFG values per step instead of fixed CFG throughout generation
  - *From: Kijai*

- **MoE architecture**: Wan 2.2 uses Mixture of Experts with High/Low noise expert split in 5B hybrid model
  - *From: context*

- **High vs Low noise models**: High noise handles motion/structure, low noise handles final quality/details
  - *From: Kijai*

- **Leftover noise**: Option that prevents complete denoising in first pass, leaving noise for second sampler
  - *From: Ablejones*

- **Automated offloading**: Native implementation automatically manages memory by partially loading models
  - *From: Kijai*

- **Two sampler setup**: Uses separate high-noise and low-noise models with different timesteps and sigma scheduling
  - *From: Kijai*

- **Quantile estimation**: Method to compute scale values for tensor normalization using random samples for large tensors or whole data for small ones, based on 99.9th percentile of absolute values
  - *From: AJO*

- **VACE**: Video control system for style transfer, inpainting, subject-driven generation, and outpainting
  - *From: Sal TK FX*

- **Split step configuration**: Split step should go into end step of first and start step of second sampler
  - *From: Kijai*

- **ComfyUI caching**: ComfyUI holds references in output cache preventing garbage collection, causing memory issues
  - *From: fredbliss*

- **Weakref proxy**: Creates a fake object that allows original model to be garbage collected when no strong references exist
  - *From: fredbliss*

- **High noise vs Low noise expert split**: High noise focuses on composition, motion, and prompt comprehension; Low noise focuses on details and refinement
  - *From: thaakeno*

- **Context windows**: Method to generate longer sequences by processing overlapping segments
  - *From: Kijai*

- **MoE architecture**: Mixture of Experts - Wan 2.2 uses separate models for high and low noise processing
  - *From: multiple users*

- **MoE architecture**: Wan 2.2 uses Mixture of Experts with High/Low noise expert split in 5B hybrid model
  - *From: system*

- **TCFG and zero star refine cfg steps**: Small impact optimization that's generally always better
  - *From: Kijai*

- **SLG**: Like negative conditioning boost, generally great with CFG
  - *From: Kijai*

- **EasyCache**: Like TeaCache but doesn't require tuning, only one that makes sense with 5B because no tuning available yet
  - *From: Kijai*

- **High-noise vs Low-noise models**: High-noise handles complex layouts and motion in early stages, low-noise refines details in later steps
  - *From: thaakeno*

- **GGUF quantization levels**: Q4_K_M is golden middle, Q8 best quality, files get larger with higher ranks
  - *From: thaakeno*

- **GGUF quantization levels**: Q4, Q6, Q8 represent different compression levels - higher numbers = better quality but more VRAM needed
  - *From: Daflon*

- **High/Low noise expert split in Wan 2.2**: MoE architecture uses separate models for high and low noise levels in generation process
  - *From: context*

- **Context options reference latent**: Used with MAGREF - padded version of init image used as reference for context windows that don't include first frame
  - *From: Kijai*

- **Block swap**: Memory management technique that offloads model parts to RAM when VRAM is insufficient
  - *From: context*

- **MoE (Mixture of Experts)**: Architecture with High/Low noise expert split in Wan 2.2
  - *From: system*

- **VACE**: Video control system for style transfer, inpainting, subject-driven, outpainting
  - *From: system*

- **First-Last-Frame morphing**: Video extension technique using first and last frame
  - *From: system*

- **High/Low noise model split**: Motion is created in the high pass (noise model), visuals are refined in the low pass
  - *From: Draken*

- **Beta57 scheduler**: Beta schedule with modified parameters (alpha = 0.5, beta = 0.7)
  - *From: Juan Gea*

- **SNR (Signal-to-Noise Ratio) for sampling**: What matters more than number of steps is the SNR/sigma value that HighNoise model ends on
  - *From: Ablejones*

- **High noise vs Low noise models**: High noise handles motion, prompt following, and visual foundation; Low noise does refinement
  - *From: slmonker(5090D 32GB)*

- **2.2 soul**: The unique capabilities of 2.2 including complex prompt understanding and motion, primarily from high noise model
  - *From: gokuvonlange*

- **High vs Low noise model roles**: High model = groundwork, composition, layout, motion. Low model = colors, contrast, details, sharpening
  - *From: gokuvonlange*

- **MoE architecture**: High noise part is where the Wan team's hard work is integrated - it's the soul part of the model
  - *From: slmonker*

- **Context window looping**: Generates whole video at once but lets it overlap from start to end, different from VACE loop workflows
  - *From: Kijai*

- **Snow particles/leftover noise**: Artifacts that appear when noise isn't properly cleaned between sampling stages or from certain nodes
  - *From: gokuvonlange*

- **Wan magic**: The natural vibrancy and motion quality of the raw 2.2 model that can be reduced by adding distillation LoRAs
  - *From: gokuvonlange*

- **Start/end steps in vid2vid**: Higher start steps make output more similar to input video, lower steps allow more changes
  - *From: Kijai*

- **Block swap offloading**: Method to manage VRAM by swapping model blocks, works with both GGUF and regular models
  - *From: Kijai*

- **Effective LoRA strength**: Chaining LoRAs combines their strengths additively
  - *From: homem desgraca*

- **High/Low noise expert split**: Wan 2.2 uses different models for high and low noise processing
  - *From: context*

- **Split step in WAN 2.2**: Point where generation switches from high noise to low noise sampler, similar to denoise but with different behavior
  - *From: Draken*

- **Start step proximity to split**: Closer start step to split value = more similar to input video, lower start step = more changes
  - *From: VK (5080 128gb)*

- **High/Low noise expert split**: 2.2 architecture uses different models for high and low noise, losing this in merged models ruins what makes 2.2 good
  - *From: Kijai*

- **Block offloading**: 14B models have 40 transformer blocks, 5B models have 30. Can offload blocks to CPU to save VRAM but slows generation
  - *From: Kijai*

- **Denoise vs start/end steps**: Denoise sets start/end step by dividing steps - they are alternative methods, doesn't make sense to use both
  - *From: Kijai*

- **EchoShot method**: Splits cross attention to handle multiple prompts for scene transitions, targets different parts of sequence with different text embeds
  - *From: Kijai*

- **Stride**: Parameter that controls frame skipping in context windows - skips frames to decide which to pay attention to, like picking key checkpoints instead of every frame
  - *From: thaakeno*

- **Echoshot prompting**: Using pipe-separated prompts for different scenes in context windows, like 'scene1|scene2|scene3'
  - *From: Kijai*

- **High/Low noise model split**: High noise model trained for motion and composition in early denoising steps, low noise model cleans up details. High noise model has better prompt understanding
  - *From: Kijai*

- **Quantile LoRA**: A type of distilled LoRA (quantile_0.15) that works better for T2V generation with good prompt adherence and motion without compromising 2.2 quality
  - *From: gokuvonlange*

- **Rawdogging the model**: Using the model without any speed LoRAs or distillation, gives quality comparable to Kling 2.1 Master
  - *From: gokuvonlange*

- **Sigma schedule**: Total step count sets the sigma schedule, and when you skip steps it affects noise level of what's added to input samples
  - *From: Kijai*

- **GGUF format**: Storage format that's tightly packed requiring unpacking for use, causing speed loss. Not related to model splitting or offloading
  - *From: Kijai*

- **fp8 scaled models**: Use single float scale value for dequantization, much faster than GGUF unpacking. 4090 has hardware acceleration for fp8
  - *From: Kijai*

- **Block swap**: Feature that moves model components between CPU and GPU memory, works regardless of model format
  - *From: Kijai*

- **MPS (Motion Prediction System)**: Feature that improves realism in generations, particularly effective for animals like bears
  - *From: Juampab12*

- **High vs Low noise models**: High noise deals with early denoising, Low noise handles final details. Low noise is closer to 2.1 behavior
  - *From: Ryzen*


## Resources & Links

- **RES4LYF** (tool)
  - https://github.com/ClownsharkBatwing/RES4LYF
  - *From: TK_999*

- **Wan2.1 SkyreelsV2 VACE workflow** (workflow)
  - https://civitai.com/models/1615710/wan21-skyreelsv2-vace-14b-t2v-i2v-extend-and-loop?modelVersionId=1904209
  - *From: Vardogr*

- **High Speed Dynamic lora** (lora)
  - https://civitai.com/models/1698719/high-speed-dynamic?modelVersionId=1922492
  - *From: VK (5080 128gb)*

- **sage++ wheel for Windows** (tool)
  - https://huggingface.co/Kijai/PrecompiledWheels/blob/main/sageattention-2.2.0-cp312-cp312-win_amd64.whl
  - *From: Kijai*

- **ThinkSound model** (model)
  - https://huggingface.co/spaces/FunAudioLLM/ThinkSound
  - *From: yi*

- **OmniCam-Wan** (model)
  - https://huggingface.co/yangxiaoda/OmniCam-Wan/tree/main
  - *From: yi*

- **OmniAvatar** (repo)
  - https://github.com/Omni-Avatar/OmniAvatar
  - *From: Tango Adorbo*

- **SAGEATT hacked for older GPUs** (repo)
  - https://github.com/woct0rdho/SageAttention/releases
  - *From: hicho*

- **Rudra's MultiTalk fork** (repo)
  - https://github.com/Rudra-ai-coder/ComfyUI-WanVideoWrapper/tree/multitalk
  - *From: Tango Adorbo*

- **Tiled sampling fork** (repo)
  - https://github.com/nilor-corp/ComfyUI-WanVideoWrapper/tree/tiled-sampler
  - *From: stenandrimpy*

- **Sage Attention 2.2++ wheel** (tool)
  - https://github.com/woct0rdho/SageAttention/releases
  - *From: chancelor*

- **Wan 2.2 presentation info** (news)
  - https://x.com/bdsqlsz/status/1939574417144869146
  - *From: JohnDopamine*

- **FlowEdit for subtle changes** (tool)
  - https://github.com/fallenshock/FlowEdit
  - *From: chrisd0073*

- **LLM ComfyUI tutorial** (tutorial)
  - https://youtu.be/c5p0d-cq7uU?si=GTlQWKAjl_kig4Rs
  - *From: VRGameDevGirl84(RTX 5090)*

- **Radial attention repository** (repo)
  - https://github.com/mit-han-lab/radial-attention/
  - *From: s2k*

- **MediaSyncer** (tool)
  - https://whatdreamscost.github.io/MediaSyncer/
  - *From: Jonathan*

- **MediaSyncer GitHub** (repo)
  - https://github.com/WhatDreamsCost/MediaSyncer
  - *From: Jonathan*

- **SeedVR2 VideoUpscaler** (tool)
  - https://github.com/numz/ComfyUI-SeedVR2_VideoUpscaler
  - *From: chrisd0073*

- **DCM model based on WAN 1.3B** (model)
  - https://huggingface.co/cszy98/DCM
  - *From: hicho*

- **GPU-Z monitoring tool** (tool)
  - https://www.techpowerup.com/gpuz/
  - *From: garbus*

- **Self-Forcing VACE models** (model)
  - https://huggingface.co/lym00/Wan2.1_T2V_1.3B_SelfForcing_VACE/tree/main
  - *From: xwsswww*

- **Sameface Fix Flux LoRA** (lora)
  - https://civitai.com/models/766608/sameface-fix-flux-lora
  - *From: David Snow*

- **WanVideo CausVid 1.3B LoRA** (lora)
  - https://huggingface.co/Kijai/WanVideo_comfy/blob/main/Wan21_CausVid_bidirect2_T2V_1_3B_lora_rank32.safetensors
  - *From: xwsswww*

- **Vintage LoRA for Wan** (lora)
  - shared privately in Discord
  - *From: VRGameDevGirl84(RTX 5090)*

- **Text-to-image workflow for Wan** (workflow)
  - shared as ComfyUI workflow file
  - *From: VRGameDevGirl84(RTX 5090)*

- **ComfyUI FaceParsing implementation** (repo)
  - https://github.com/Bwebbfx/ComfyUI_FaceParsing
  - *From: Tango Adorbo*

- **OmniAvatar for audio-driven avatars** (repo)
  - https://github.com/Omni-Avatar/OmniAvatar
  - *From: Will.G*

- **ComfyUI DeZoomer Nodes for captioning** (repo)
  - https://github.com/De-Zoomer/ComfyUI-DeZoomer-Nodes
  - *From: Faust-SiN*

- **MediaSyncer v0.2** (tool)
  - https://github.com/WhatDreamsCost/MediaSyncer
  - *From: Jonathan*

- **SkyReels V2 GGUF model** (model)
  - https://huggingface.co/QuantStack/SkyReels-V2-T2V-14B-720P-VACE-GGUF
  - *From: Faust-SiN*

- **ComfyUI_Fill-Nodes** (node pack)
  - https://github.com/filliptm/ComfyUI_Fill-Nodes
  - *From: JohnDopamine*

- **Self-forcing LoRA for Wan 14B** (lora)
  - https://civitai.com/models/1585622?modelVersionId=1909719
  - *From: izashin*

- **MAGREF GGUF models** (model)
  - quantstack
  - *From: mdkb*

- **Tile LoRA upscaler workflow** (workflow)
  - https://discord.com/channels/1076117621407223829/1342763350815277067/1388973374818226256
  - *From: David Snow*

- **MultiTalk examples** (examples)
  - https://github.com/MeiGen-AI/MultiTalk/tree/main/examples/multi/1
  - *From: Kijai*

- **Kyutai TTS** (tool)
  - https://kyutai.org/next/tts
  - *From: DawnII*

- **MAGREF GGUF with native workflow** (model)
  - https://huggingface.co/QuantStack/MAGREF_Wan2.1_I2V_14B-GGUF/blob/main/README.md
  - *From: mdkb*

- **Omni-Avatar 1.3B version** (model)
  - https://github.com/Omni-Avatar/OmniAvatar
  - *From: mdkb*

- **VACE Benchmark dataset** (dataset)
  - https://huggingface.co/datasets/ali-vilab/VACE-Benchmark
  - *From: ˗ˏˋ⚡ˎˊ-*

- **ComfyUI-Veevee flow predictors** (repo)
  - https://github.com/logtd/ComfyUI-Veevee
  - *From: Kijai*

- **Fusion VACE GGUF** (model)
  - https://huggingface.co/QuantStack/Wan2.1_T2V_14B_FusionX_VACE-GGUF
  - *From: yukass*

- **VACE workflows collection** (workflow)
  - https://huggingface.co/QuantStack/Wan2.1_14B_VACE-GGUF/tree/main
  - *From: mdkb*

- **Image batcher custom node** (node)
  - https://huggingface.co/Stkzzzz222/remixXL/blob/main/image_batcher_by_indexz.py
  - *From: BarleyFarmer*

- **Wan chatter archive chatbot** (tool)
  - https://notebooklm.google.com/notebook/a08901b9-0511-4926-bbf8-3c86a12dc306
  - *From: JohnDopamine*

- **Chatterbox Dialog fork** (repo)
  - https://github.com/pmarmotte2?tab=repositories
  - *From: manu_le_surikhate_gamer*

- **Draw Things Community** (repo)
  - https://github.com/drawthingsai/draw-things-community
  - *From: Todd*

- **SageAttention RTX 5090 wheel** (tool)
  - https://github.com/woct0rdho/SageAttention/releases
  - *From: AJO*

- **WarperNodes** (node)
  - https://github.com/AIWarper/ComfyUI-WarperNodes
  - *From: A.I.Warper*

- **High Speed Dynamic LoRA** (lora)
  - https://civitai.com/models/1698719/high-speed-dynamic?modelVersionId=1922492
  - *From: VRGameDevGirl84*

- **AniWan model** (model)
  - https://civitai.green/models/1626197/aniwan2114bfp8e4m3fn
  - *From: Colin*

- **Realismboost LoRA** (lora)
  - https://civitai.com/models/1626063
  - *From: VRGameDevGirl84*

- **LightX2V distill discussion** (resource)
  - https://huggingface.co/lightx2v/Wan2.1-T2V-14B-StepDistill-CfgDistill/discussions/4
  - *From: Screeb*

- **WanVideoWrapper MultiTalk test** (workflow)
  - https://www.reddit.com/r/comfyui/comments/1lowymq/first_long_multi_talk_test/
  - *From: samhodge*

- **Flash Depth** (tool)
  - https://x.com/gene_ch0u/status/1938750636021162003
  - *From: chrisd0073*

- **Control vector experiments** (repo)
  - https://github.com/fblissjr/steering-mlx/tree/main
  - *From: fredbliss*

- **VLM tinkering repo** (repo)
  - https://github.com/fblissjr/tinkering-with-vlms
  - *From: fredbliss*

- **16fps workaround workflow** (workflow)
  - https://discord.com/channels/1076117621407223829/1391076101652086785
  - *From: yo9o*

- **heylookitsanllm** (repo)
  - https://github.com/fblissjr/heylookitsanllm
  - *From: fredbliss*

- **shrug-prompter** (repo)
  - https://github.com/fblissjr/shrug-prompter
  - *From: fredbliss*

- **VACE module 14B** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/blob/main/Wan2_1-VACE_module_14B_bf16.safetensors
  - *From: Hashu*

- **MAGREF 14B fp8** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/blob/main/Wan2_1-Wan-I2V-MAGREF-14B_fp8_e4m3fn.safetensors
  - *From: David Snow*

- **Loop Anything with Wan21 VACE** (workflow)
  - https://openart.ai/workflows/nomadoor/loop-anything-with-wan21-vace/qz02Zb3yrF11GKYi6vdu
  - *From: daking999*

- **Steerable Motion** (repo)
  - https://github.com/banodoco/steerable-motion
  - *From: xwsswww*

- **MAGREF GGUF models** (model)
  - https://huggingface.co/QuantStack/MAGREF_Wan2.1_I2V_14B-GGUF/tree/main
  - *From: mdkb*

- **Pexels for face datasets** (resource)
  - https://www.pexels.com/search/face/
  - *From: David Snow*

- **Freepik for datasets** (resource)
  - freepik dot com
  - *From: N0NSens*

- **Radial attention for WAN** (repo)
  - https://github.com/mit-han-lab/radial-attention/blob/main/wan_t2v_inference.py
  - *From: MysteryShack*

- **Skyreels workflows for WAN** (workflow)
  - https://civitai.com/models/1742500
  - *From: VRGameDevGirl84(RTX 5090)*

- **Calcuis WAN GGUF models** (model)
  - https://huggingface.co/calcuis/wan-gguf/tree/main
  - *From: Kijai*

- **QuantStack VACE GGUF models** (model)
  - https://huggingface.co/QuantStack/Wan2.1_T2V_14B_LightX2V_StepCfgDistill_VACE-GGUF/tree/main
  - *From: anever*

- **E5m2 conversion scripts** (tool)
  - https://huggingface.co/phazei/phazei-SkyReels-V2-fp8-e5m2/tree/main
  - *From: phazei*

- **GGUF models for Wan** (model)
  - https://huggingface.co/calcuis/wan-gguf/tree/main
  - *From: Kijai*

- **Quantized GGUF models** (model)
  - https://huggingface.co/QuantStack/Wan2.1_T2V_14B_LightX2V_StepCfgDistill_VACE-GGUF/tree/main
  - *From: Kijai*

- **MultiTalk model fp8** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/blob/main/WanVideo_2_1_Multitalk_14B_fp8_e4m3fn.safetensors
  - *From: Kijai*

- **Original MultiTalk model** (model)
  - https://huggingface.co/MeiGen-AI/MeiGen-MultiTalk/blob/main/multitalk.safetensors
  - *From: Kijai*

- **Wallace and Gromit LoRA** (lora)
  - https://civitai.com/models/1736052?modelVersionId=1964792
  - *From: Siraj*

- **shrug-prompter ComfyUI nodes** (tool)
  - https://github.com/fblissjr/shrug-prompter
  - *From: fredbliss*

- **heylookitsanllm API server** (tool)
  - https://github.com/fblissjr/heylookitsanllm
  - *From: fredbliss*

- **ATI point editor tool** (tool)
  - shared via Discord
  - *From: Juampab12*

- **MTVCraft** (repo)
  - https://github.com/baaivision/MTVCraft
  - *From: JohnDopamine*

- **Uni3C documentation** (documentation)
  - https://alibaba-damo-academy.github.io/Uni3C/
  - *From: Gateway {Dreaming Computers}*

- **Wan Reddit post example** (example)
  - https://www.reddit.com/r/StableDiffusion/comments/1lu7nxx/wan_21_txt2img_is_amazing/
  - *From: multiple users*

- **WAN and Skyreels Text to Image Workflows** (workflow)
  - https://civitai.com/models/1742500/wan-and-skyreels-text-to-image-workflows
  - *From: VRGameDevGirl84*

- **MultiTalk comparison on Reddit** (comparison)
  - https://www.reddit.com/r/StableDiffusion/comments/1luqc53/4_vs_5_vs_6_vs_8_steps_multitalk_comparison_4/
  - *From: Juampab12*

- **VACE lock-on stabilization example** (example)
  - https://www.reddit.com/r/StableDiffusion/comments/1luo3wo/smooth_lockon_stabilization_with_wan21_vace/
  - *From: Juampab12*

- **Nekodificador's conference talk on WAN** (presentation)
  - https://youtu.be/JQHDw4pjZTg
  - *From: Nekodificador*

- **pom's conference talk on VACE** (presentation)
  - https://www.youtube.com/watch?v=HJ45pnrON2Y
  - *From: pom*

- **Wan Knowledge Base** (knowledge base)
  - https://nathanshipley.notion.site/Wan-2-1-Knowledge-Base-1d691e115364814fa9d4e27694e9468f
  - *From: JohnDopamine*

- **Wan chatbot with full channel logs** (chatbot)
  - https://notebooklm.google.com/notebook/a08901b9-0511-4926-bbf8-3c86a12dc306?pli=1
  - *From: JohnDopamine*

- **ThinkSound audio generation** (repo)
  - https://github.com/FunAudioLLM/ThinkSound
  - *From: Bingo*

- **FusionX LoRA** (lora)
  - https://civitai.com/models/1678575/wan21fusionx-the-lora
  - *From: Todd*

- **shrug-prompter for automated prompting** (tool)
  - https://github.com/fblissjr/shrug-prompter
  - *From: fredbliss*

- **DrawThings AI** (repo)
  - https://github.com/drawthingsai
  - *From: fredbliss*

- **ComfyUI-DrawThings-gRPC** (node)
  - https://github.com/Jokimbe/ComfyUI-DrawThings-gRPC
  - *From: Todd*

- **ComfyUI-SuperUltimateVaceTools** (tool)
  - https://github.com/bbaudio-2025/ComfyUI-SuperUltimateVaceTools
  - *From: hicho*

- **PromptTea (improved TeaCache)** (tool)
  - https://github.com/zishen-ucap/PromptTea
  - *From: yi*

- **WanFusionXFaceNaturalizer lora** (lora)
  - https://civitai.com/models/1755105/wanfusionxfacenaturalizer
  - *From: patientx*

- **VACE extend workflow** (workflow)
  - https://discord.com/channels/1076117621407223829/1391076101652086785
  - *From: Hashu*

- **FusionXLightning Ingredients Workflows** (workflow)
  - https://civitai.com/models/1736052
  - *From: VRGameDevGirl84*

- **VRGameDevGirl ComfyUI nodes** (repo)
  - https://github.com/vrgamegirl19/comfyui-vrgamedevgirl
  - *From: VRGameDevGirl84*

- **ComfyUI LoRA Manager for WAN** (tool)
  - https://github.com/willmiao/ComfyUI-Lora-Manager
  - *From: hicho*

- **SmartResizer node** (node)
  - https://github.com/slikvik55/ComfyUI-SmartResizer
  - *From: Flipping Sigmas*

- **LightX rank16 LoRA** (model)
  - https://huggingface.co/Soup-Quantum/quantum-soup-twinkler/blob/main/14b/Utility/wan_lcm_r16_fp32_comfy.safetensors
  - *From: DawnII*

- **Index-anisora anime model** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/blob/main/Wan2_1-Anisora-I2V-480P-14B_fp8_e4m3fn.safetensors
  - *From: DawnII*

- **SeedVR2 Deep Dive video** (tutorial)
  - https://youtu.be/I0sl45GMqNg
  - *From: Adrien Toupet*

- **ThinkSound** (model)
  - https://github.com/FunAudioLLM/ThinkSound
  - *From: A.I.Warper*

- **FaceNaturalizer LoRA** (lora)
  - https://civitai.com/models/1755105
  - *From: VRGameDevGirl84(RTX 5090)*

- **Diffusion-pipe training tool** (tool)
  - https://github.com/tdrussell/diffusion-pipe/tree/main
  - *From: Dream Making*

- **SuperClaude agent framework** (tool)
  - https://github.com/NomenAK/SuperClaude
  - *From: LarpsAI*

- **Paint splash LoRA** (lora)
  - civitai link in wan_chatter
  - *From: VRGameDevGirl84(RTX 5090)*

- **Wan 2.1 Knowledge Base** (documentation)
  - https://nathanshipley.notion.site/Wan-2-1-Knowledge-Base-1d691e115364814fa9d4e27694e9468f#1d691e11536481f380e4cbf7fa105c05
  - *From: mdkb*

- **SkyReels V2 I2V 14B 540P GGUF** (model)
  - https://huggingface.co/wsbagnsv1/SkyReels-V2-I2V-14B-540P-GGUF/tree/main
  - *From: The Shadow (NYC)*

- **SkyReels V2 T2V 14B 720P VACE GGUF** (model)
  - https://huggingface.co/QuantStack/SkyReels-V2-T2V-14B-720P-VACE-GGUF
  - *From: The Shadow (NYC)*

- **Realistic Fire Wan 2.1 T2V LoRA** (lora)
  - https://civitai.com/models/1376174/realistic-fire-wan21-t2v-lora
  - *From: JohnDopamine*

- **Wan2.1 14B VACE GGUF** (model)
  - https://huggingface.co/QuantStack/Wan2.1_14B_VACE-GGUF/tree/main
  - *From: JohnDopamine*

- **VACE User Guide** (documentation)
  - https://github.com/ali-vilab/VACE/blob/main/UserGuide.md
  - *From: hicho*

- **Open-OmniVCus** (repo)
  - https://github.com/caiyuanhao1998/Open-OmniVCus
  - *From: hicho*

- **ComfyUI GIMM VFI** (repo)
  - https://github.com/kijai/ComfyUI-GIMM-VFI
  - *From: ˗ˏˋ⚡ˎˊ-*

- **ComfyUI Cache Cleaner** (node)
  - https://github.com/AIToldMeTo/comfyui-cache-cleaner
  - *From: Kijai*

- **RunPod ComfyUI Wan Template** (template)
  - https://console.runpod.io/explore/758dsjwiqz
  - *From: Siraj*

- **Deadpool LoRA for Wan** (model)
  - https://civitai.com/models/1756172/deadpool?modelVersionId=1987510
  - *From: hicho*

- **Redhead painted LoRA** (model)
  - https://civitai.com/models/1622042/readheadpainted?modelVersionId=1835745
  - *From: hicho*

- **Wan Knowledge Base** (documentation)
  - https://nathanshipley.notion.site/Wan-2-1-Knowledge-Base-1d691e115364814fa9d4e27694e9468f
  - *From: Gateway {Dreaming Computers}*

- **SageAttention source** (repo)
  - https://github.com/thu-ml/SageAttention
  - *From: Kijai*

- **SageAttention Windows wheels** (tool)
  - https://github.com/woct0rdho/SageAttention/releases
  - *From: Kijai*

- **Wan T2I workflow** (workflow)
  - https://civitai.com/models/1757056/wan-21-text-to-image-workflow
  - *From: Gateway {Dreaming Computers}*

- **LightX2V T2V model** (model)
  - https://huggingface.co/lightx2v/Wan2.1-T2V-14B-Lightx2v
  - *From: yi*

- **LightX2V I2V model** (model)
  - https://huggingface.co/lightx2v/Wan2.1-I2V-14B-720P-Lightx2v
  - *From: yi*

- **Kijai WanVideo Q8_0 quantized model** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/blob/main/Wan2_1-Anisora-I2V-480P-14B_Q8_0.gguf
  - *From: Hashu*

- **Index-anisora 14B model** (model)
  - https://huggingface.co/IndexTeam/Index-anisora/tree/main/14B
  - *From: Ada*

- **Video comparison tool** (tool)
  - https://github.com/casterpollux/video-compare-bmo
  - *From: 🦙rishappi*

- **Pusa V1** (model)
  - https://huggingface.co/RaphaelLiu/PusaV1
  - *From: yi*

- **Pusa GitHub repository** (repo)
  - https://github.com/Yaofang-Liu/Pusa-VidGen
  - *From: JohnDopamine*

- **SeedVR2 7B Sharp** (model)
  - https://huggingface.co/ByteDance-Seed/SeedVR2-7B/blob/main/seedvr2_ema_7b_sharp.pth
  - *From: DawnII*

- **EchoShot webpage** (model)
  - https://johnneywang.github.io/EchoShot-webpage/
  - *From: DawnII*

- **YouTube workflow tutorial** (tutorial)
  - https://www.youtube.com/watch?v=ZE9kxEut7lo
  - *From: mdkb*

- **CameraBench dataset** (dataset)
  - https://huggingface.co/datasets/syCen/CameraBench
  - *From: Valle*

- **Camera control WAN LoRAs** (loras)
  - https://www.reddit.com/r/StableDiffusion/comments/1kviphp/i_just_opensourced_10_camera_control_wan_loras/
  - *From: Gateway {Dreaming Computers}*

- **LightX2V new LoRAs** (loras)
  - https://huggingface.co/lightx2v
  - *From: The Shadow (NYC)*

- **FLUX1East model** (model)
  - https://civitai.com/models/1336544/flux1east-fp16
  - *From: slmonker(5090D 32GB)*

- **ALG framework** (repo)
  - https://github.com/choi403/ALG
  - *From: hicho*

- **PUSA model** (model)
  - https://yaofang-liu.github.io/Pusa_Web/
  - *From: s2k*

- **CausVid + SkyReels merge** (model)
  - https://huggingface.co/Zuntan/Wan-SkyReels-CausVid/tree/main
  - *From: hicho*

- **Wan2.1-I2V-14B-480P-StepDistill-CfgDistill-Lightx2v** (model)
  - https://huggingface.co/lightx2v/Wan2.1-I2V-14B-480P-StepDistill-CfgDistill-Lightx2v/tree/main/distill_models
  - *From: hicho*

- **Wan2.1-T2V-14B-StepDistill-CfgDistill-Lightx2v** (model)
  - https://huggingface.co/lightx2v/Wan2.1-T2V-14B-StepDistill-CfgDistill-Lightx2v/tree/main/distill_models
  - *From: hicho*

- **Shinkai anime style LoRA** (lora)
  - https://huggingface.co/Cseti/wan-14b-shinkai-anime-style-lora-v1
  - *From: hicho*

- **Wan 2.1 Knowledge Base** (documentation)
  - https://nathanshipley.notion.site/Wan-2-1-Knowledge-Base-1d691e115364814fa9d4e27694e9468f
  - *From: Gateway {Dreaming Computers}*

- **VSF NAG alternative** (tool)
  - https://github.com/weathon/VSF
  - *From: Screeb*

- **ani_Wan model** (model)
  - https://civitai.com/models/1626197?modelVersionId=1852433
  - *From: Ada*

- **Kijai's LightX2V extractions** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/tree/main/Lightx2v
  - *From: Kijai*

- **PUSA model** (model)
  - https://huggingface.co/RaphaelLiu/PusaV1
  - *From: yo9o*

- **GGUF VRAM calculator** (tool)
  - https://huggingface.co/spaces/oobabooga/accurate-gguf-vram-calculator
  - *From: DawnII*

- **Wan GGUF models** (model)
  - https://huggingface.co/city96/Wan2.1-T2V-14B-gguf/tree/main
  - *From: Gateway {Dreaming Computers}*

- **AI Toolkit for training** (tool)
  - https://github.com/ostris/ai-toolkit
  - *From: Gateway {Dreaming Computers}*

- **Official LightX2V ComfyUI wrapper** (tool)
  - https://github.com/ModelTC/ComfyUI-Lightx2vWrapper
  - *From: Kijai*

- **PUSA repository** (repo)
  - https://github.com/Yaofang-Liu/Pusa-VidGen
  - *From: multiple users*

- **RES4LYF custom samplers** (repo)
  - https://github.com/ClownsharkBatwing/RES4LYF
  - *From: JohnDopamine*

- **Kijai's LightX2V LoRAs** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/tree/main/Lightx2v
  - *From: David Snow*

- **Motion Boost LoRA** (model)
  - https://civitai.com/models/1698719/high-speed-dynamic?modelVersionId=1922492
  - *From: The Shadow (NYC)*

- **GGUF CLIP models** (model)
  - https://huggingface.co/city96
  - *From: The Shadow (NYC)*

- **Pusa LoRA by Kijai** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/blob/main/Pusa/Wan21_PusaV1_LoRA_14B_rank512_bf16.safetensors
  - *From: Kijai*

- **MTB batch tools for dot animation** (tool)
  - https://github.com/melMass/comfy_mtb/wiki/nodes-batch
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Pusa lora** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/tree/main/Pusa
  - *From: Kijai*

- **Lightx2v variants** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/tree/main/Lightx2v
  - *From: JohnDopamine*

- **Pusa research paper** (repo)
  - https://github.com/Yaofang-Liu/Pusa-VidGen
  - *From: David Snow*

- **Basic Pusa workflow** (workflow)
  - Discord workflow file
  - *From: David Snow*

- **MTVCrafter** (model)
  - https://huggingface.co/yanboding/MTVCrafter
  - *From: DawnII*

- **Pusa model repository** (repo)
  - https://github.com/Yaofang-Liu/Pusa-VidGen
  - *From: David Snow*

- **Pusa LoRA** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/tree/main/Pusa
  - *From: David Snow*

- **Sparse_SageAttention_API** (repo)
  - https://github.com/jt-zhang/Sparse_SageAttention_API
  - *From: Kijai*

- **VACE User Guide** (documentation)
  - https://github.com/ali-vilab/VACE/blob/main/UserGuide.md
  - *From: ingi // SYSTMS*

- **RAM tag color list** (resource)
  - https://huggingface.co/ali-vilab/VACE-Annotators/blob/main/layout/ram_tag_color_list.txt
  - *From: ingi // SYSTMS*

- **Wan 2.1 official models** (model)
  - https://huggingface.co/Wan-AI/models
  - *From: Juampab12*

- **ComfyUI repackaged Wan models** (model)
  - https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/tree/main/split_files/diffusion_models
  - *From: ˗ˏˋ⚡ˎˊ-*

- **LightX2V I2V LoRA** (lora)
  - https://huggingface.co/Kijai/WanVideo_comfy/blob/main/Lightx2v/lightx2v_I2V_14B_480p_cfg_step_distill_rank32_bf16.safetensors
  - *From: yi*

- **PusaV1 updated models** (model)
  - https://huggingface.co/RaphaelLiu/PusaV1/tree/main
  - *From: JohnDopamine*

- **LoRAEdit model** (repo)
  - https://github.com/cjeen/LoRAEdit
  - *From: Juampab12*

- **VSF repository** (repo)
  - https://github.com/weathon/VSF
  - *From: The Shadow (NYC)*

- **Fantasy Portrait** (repo)
  - https://github.com/Fantasy-AMAP/fantasy-portrait
  - *From: ˗ˏˋ⚡ˎˊ-*

- **ACE++ LoRAs** (lora)
  - https://civitai.com/models/1183391/ace-more-convenient-replacement-of-everything
  - *From: Shawneau 🍁 [CA]*

- **LightX2V rank 256 LoRA** (lora)
  - https://huggingface.co/Kijai/WanVideo_comfy/blob/main/Lightx2v/lightx2v_T2V_14B_cfg_step_distill_v2_lora_rank256_bf16.safetensors
  - *From: Kijai*

- **Adaptive rank LightX2V LoRA** (lora)
  - https://huggingface.co/Kijai/WanVideo_comfy/blob/main/Lightx2v/lightx2v_14B_T2V_cfg_step_distill_lora_adaptive_rank_quantile_0.15_bf16.safetensors
  - *From: Kijai*

- **Jack Nicholson soundboard** (tool)
  - https://www.101soundboards.com/boards/10395-jack-nicholson-sounds
  - *From: hicho*

- **ControlNet AnimalPose** (repo)
  - https://github.com/abehonest/ControlNet_AnimalPose
  - *From: AmirKerr*

- **VaceWanAdvancedTests** (repo)
  - https://github.com/drozbay/VaceWanAdvancedTests
  - *From: Ablejones*

- **Spline Path Control tool** (tool)
  - https://whatdreamscost.github.io/Spline-Path-Control/
  - *From: Piblarg*

- **Aesthetic Quality Modifiers LoRA** (model)
  - https://civitai.com/models/929497/aesthetic-quality-modifiers-masterpiece?modelVersionId=1498121
  - *From: Juan Gea*

- **Studio Ghibli Wan2.1 LoRA** (model)
  - https://civitai.com/models/1404755/studio-ghibli-wan21-t2v-14b?modelVersionId=1587891
  - *From: Juan Gea*

- **PUSA Motion LoRA workflow example** (workflow)
  - *From: Hashu*

- **Flux-Kontext-InScene LoRA** (model)
  - https://huggingface.co/peteromallet/Flux-Kontext-InScene
  - *From: ˗ˏˋ⚡ˎˊ-*

- **FP8 conversion scripts** (tool)
  - https://huggingface.co/phazei/phazei-SkyReels-V2-fp8-e5m2/tree/main/scripts
  - *From: phazei*

- **Explosion LoRA** (lora)
  - https://huggingface.co/Remade-AI/Explode
  - *From: orabazes*

- **ComfyUI-Lightx2vWrapper** (repo)
  - https://github.com/ModelTC/ComfyUI-Lightx2vWrapper
  - *From: hicho*

- **Uni3C workflow** (workflow)
  - mentioned but not directly linked
  - *From: Guey.KhalaMari*

- **Deformed heads LoRA** (model)
  - https://civitai.com/models/1779359/deformed-heads
  - *From: Guey.KhalaMari*

- **Skyreels morphing LoRA** (model)
  - https://civitai.com/models/1525175/wan-i2v-skyreels-i2v-morphing-into-plushtoy-trained-on-sr-v2-i2v?modelVersionId=1725658
  - *From: JohnDopamine*

- **VACE keyframing custom node** (node)
  - https://old.reddit.com/r/comfyui/comments/1l93f7w/my_weird_custom_node_for_vace/
  - *From: JohnDopamine*

- **WAN LoRAs collection** (model)
  - https://huggingface.co/ApacheOne/WAN_loRAs
  - *From: patientx*

- **Consistent character poses workflow** (workflow)
  - https://civitai.com/models/1796490/consistent-character-poses-workflow
  - *From: Valle*

- **UMT5 text encoder** (model)
  - https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/blob/main/split_files/text_encoders/umt5_xxl_fp8_e4m3fn_scaled.safetensors
  - *From: Kijai*

- **Wan2GP low VRAM solution** (tool)
  - https://github.com/deepbeepmeep/Wan2GP
  - *From: JohnDopamine*

- **Fun Control v1.1 14B model** (model)
  - https://huggingface.co/alibaba-pai/Wan2.1-Fun-V1.1-14B-Control/tree/main
  - *From: Hashu*

- **Kijai's fp8 scaled models** (model)
  - https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/tree/main/split_files/diffusion_models
  - *From: Kijai*

- **VACE+Phantom combination node** (tool)
  - https://github.com/drozbay/VaceWanAdvancedTests
  - *From: Ablejones*

- **Wan continuation tools** (workflow)
  - https://github.com/bbaudio-2025/ComfyUI-SuperUltimateVaceTools/tree/main/workflows
  - *From: samhodge*

- **Wan continuation Twitter demo** (demo)
  - https://x.com/toyxyz3/status/1947292079467499525?s=46&t=Z_g6MJK4iC3TfVv-z1OTfQ
  - *From: pom*

- **FP8 scaled models** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy_fp8_scaled/tree/main
  - *From: Kijai*

- **Triton Windows wheels** (tool)
  - https://github.com/woct0rdho/triton-windows
  - *From: Kijai*

- **Hunyuan tiny VAE for native** (repo)
  - https://github.com/blepping/ComfyUI-bleh
  - *From: Kijai*

- **Wan ControlNet models** (model)
  - https://huggingface.co/TheDenk
  - *From: Kijai*

- **Dance video for pose testing** (resource)
  - https://www.youtube.com/watch?v=7xnn3cZgmm8
  - *From: Ablejones*

- **CHORDS paper** (repo)
  - https://github.com/hanjq17/CHORDS
  - *From: yi*

- **LightX2V I2V 480P LoRAs** (model)
  - https://huggingface.co/lightx2v/Wan2.1-I2V-14B-480P-StepDistill-CfgDistill-Lightx2v/tree/main/loras
  - *From: mamad8*

- **PUSA training dataset** (dataset)
  - https://huggingface.co/datasets/RaphaelLiu/PusaV1_training/raw/main/metadata.csv
  - *From: fredbliss*

- **Torchcache for disk caching** (tool)
  - https://github.com/meakbiyik/torchcache
  - *From: Kijai*

- **Caching ComfyUI node** (node)
  - https://github.com/alastor-666-1933/caching_to_not_waste
  - *From: Hedge*

- **Wan pregnancy details LoRA** (lora)
  - https://civitai.com/models/1789374/wan21-14b-pregnancy-details-480p-and-720p?modelVersionId=2024979
  - *From: Ryzen*

- **Sparse SageAttention 2.0** (optimization)
  - https://github.com/Radioheading/Block-Sparse-SageAttention-2.0
  - *From: Kijai*

- **UniC3 documentation** (documentation)
  - https://alibaba-damo-academy.github.io/Uni3C/
  - *From: hicho*

- **HAMER (human pose)** (tool)
  - https://github.com/geopavlakos/hamer
  - *From: pookyjuice*

- **SMPLX (human body)** (tool)
  - https://github.com/vchoutas/smplx
  - *From: hicho*

- **SageAttention releases** (repo)
  - https://github.com/woct0rdho/SageAttention/releases
  - *From: Hashu*

- **Camera movement database** (dataset)
  - https://huggingface.co/datasets/syCen/CameraBench/viewer
  - *From: Gateway {Dreaming Computers}*

- **VACE I2V workflow** (workflow)
  - https://drive.google.com/file/d/1Ys1RTKmZ-K4SHyjaqQQn_yprrDq6ZyVM/view?usp=drivesdk
  - *From: samhodge*

- **Gingham shader for features** (repo)
  - https://github.com/samhodge/catpicnic
  - *From: samhodge*

- **FusionX Ingredients Workflows** (workflow)
  - https://civitai.com/models/1690979/fusionxingredientsworkflows
  - *From: Gateway {Dreaming Computers}*

- **Kijai WanVideo fp8_scaled models** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy_fp8_scaled/tree/main/I2V
  - *From: Kijai*

- **Relighting Kontext LoRA** (lora)
  - https://huggingface.co/kontext-community/relighting-kontext-dev-lora-v3
  - *From: orabazes*

- **Kontext Relight Space** (tool)
  - https://huggingface.co/spaces/kontext-community/kontext-relight
  - *From: orabazes*

- **OmniAvatar-14B** (model)
  - https://huggingface.co/OmniAvatar/OmniAvatar-14B/tree/main
  - *From: hicho*

- **Wan FastVideo models** (model)
  - https://huggingface.co/FastVideo/models
  - *From: JohnDopamine*

- **ComfyUI Hot Reload Hack** (tool)
  - https://github.com/logtd/ComfyUI-HotReloadHack
  - *From: Kijai*

- **Wan model PDF documentation** (documentation)
  - https://files.alicdn.com/tpsservice/5c9de1c74de03972b7aa657e5a54756b.pdf
  - *From: hicho*

- **Wan prompt enhancement site** (tool)
  - https://wan.video/
  - *From: hicho*

- **Skyreels V2 models** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/tree/main/Skyreels
  - *From: yi*

- **Qwen2.5-VL-7B for prompt improvement** (model)
  - *From: hicho*

- **LightX2V I2V distill model** (model)
  - https://huggingface.co/lightx2v/Wan2.1-I2V-14B-480P-StepDistill-CfgDistill-Lightx2v/blob/main/distill_models/distill_model.safetensors
  - *From: hicho*

- **LightX2V T2V distill model** (model)
  - https://huggingface.co/lightx2v/Wan2.1-T2V-14B-StepDistill-CfgDistill-Lightx2v/blob/main/distill_models/distill_model.safetensors
  - *From: hicho*

- **SeedVR GGUF quantization PR** (repo)
  - https://github.com/numz/ComfyUI-SeedVR2_VideoUpscaler/pull/78
  - *From: Alisson Pereira*

- **FastWan 1.3B ComfyUI model** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/blob/main/Wan2_1-T2V_FastWan_1_3B_bf16.safetensors
  - *From: Kijai*

- **WAN 2.2 research paper** (research)
  - https://arxiv.org/html/2507.16116v1
  - *From: samhodge*

- **YUME I2V model** (model)
  - https://huggingface.co/stdstu123/Yume-I2V-540P
  - *From: DawnII*

- **YUME code repository** (repo)
  - https://github.com/stdstu12/YUME
  - *From: aikitoria*

- **Spline Path Control for morphing** (tool)
  - https://whatdreamscost.github.io/Spline-Path-Control/
  - *From: Дмитрий Марков*

- **Uni3C workflow shared** (workflow)
  - *From: Flipping Sigmas*

- **VRGameDevGirl Custom Node Dev Branch** (node)
  - https://github.com/vrgamegirl19/comfyui-vrgamedevgirl/tree/Dev
  - *From: VRGameDevGirl84(RTX 5090)*

- **Camera control reference videos** (workflow)
  - *From: The Shadow (NYC)*

- **DiffSynth Studio LoRA** (model)
  - https://huggingface.co/Evados/DiffSynth-Studio-Lora-Wan2.1-ComfyUI
  - *From: hicho*

- **YUME Project** (tool)
  - https://stdstu12.github.io/YUME-Project/
  - *From: hicho*

- **NABLA optimized WAN 2.1** (model)
  - https://huggingface.co/ai-forever/Wan2.1-T2V-14B-NABLA-0.7
  - *From: DawnII*

- **PromptTea for WAN 2.1** (tool)
  - https://github.com/zishen-ucap/PromptTea/blob/main/PromptTea4Wan2.1/README.md
  - *From: cocktailprawn1212*

- **WAN technical deep dive video** (resource)
  - https://youtu.be/iv-5mZ_9CPY?si=AAUSGQZTtAsFigGF
  - *From: The Shadow*

- **WAN multitalk test context windows workflow** (workflow)
  - wanvideo_multitalk_test_context_windows_01.json
  - *From: Hashu*

- **Alibaba WAN Twitter** (resource)
  - https://x.com/Alibaba_Wan/status/1948436898965586297
  - *From: Ruairi Robinson*

- **SageAttention 2.2.0 Windows wheels** (tool)
  - https://github.com/woct0rdho/SageAttention/releases/tag/v2.2.0-windows
  - *From: Kijai*

- **ComfyUI-NAG custom node** (node)
  - https://github.com/ChenDarYen/ComfyUI-NAG/tree/main/workflows
  - *From: Дмитрий Марков*

- **FastWan 14B model** (model)
  - https://huggingface.co/FastVideo/FastWan2.1-T2V-14B-480P-Diffusers/tree/main
  - *From: JohnDopamine*

- **FastWan LoRA conversions** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/tree/main/FastWan
  - *From: Kijai*

- **FastWan scaled fp8 model** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy_fp8_scaled/blob/main/T2V/Wan2_1-T2V-14B-FastWan-480p_fp8_e4m3fn_scaled_KJ.safetensors
  - *From: Kijai*

- **Block-Sparse-SageAttention** (repo)
  - https://github.com/Radioheading/Block-Sparse-SageAttention-2.0
  - *From: Kijai*

- **FastVideo research paper** (paper)
  - https://arxiv.org/abs/2505.13389
  - *From: DawnII*

- **FastVideo ComfyUI extension** (tool)
  - https://github.com/hao-ai-lab/FastVideo/tree/main/comfyui
  - *From: ˗ˏˋ⚡ˎˊ-*

- **EchoShot model** (model)
  - https://github.com/JoHnneyWang/EchoShot
  - *From: Kijai*

- **EchoShot HuggingFace** (model)
  - https://huggingface.co/JonneyWang/EchoShot
  - *From: hicho*

- **High speed motion LoRA** (lora)
  - https://civitai.com/models/1698719?modelVersionId=1922492
  - *From: Hippotes*

- **DMD self-forcing LoRA** (lora)
  - https://huggingface.co/lym00/Wan2.1_T2V_1.3B_SelfForcing_VACE/blob/main/Wan2.1_T2V_1.3B_SelfForcing_DMD-FP16-LoRA-Rank32.safetensors
  - *From: Kijai*

- **CausVid bidirectional LoRA** (lora)
  - https://huggingface.co/Kijai/WanVideo_comfy/blob/main/Wan21_CausVid_bidirect2_T2V_1_3B_lora_rank32.safetensors
  - *From: Kijai*

- **EchoShot ComfyUI files** (workflow)
  - https://huggingface.co/Kijai/WanVideo_comfy/tree/main/EchoShot
  - *From: Kijai*

- **EchoShot LoRA for Wan 2.1** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/blob/main/EchoShot/Wan2_1_EchoShot_1_3B_lora_rank_128_fp16.safetensors
  - *From: Kijai*

- **DG models collection** (model)
  - https://huggingface.co/Evados/DiffSynth-Studio-Lora-Wan2.1-ComfyUI/tree/main
  - *From: Kijai*

- **Wan prompt enhancer system prompt** (repo)
  - https://github.com/Wan-Video/Wan2.1/blob/7c81b2f27defa56c7e627a4b6717c8f2292eee58/wan/utils/prompt_extend.py#L41
  - *From: Kagi*

- **WanVideoWrapper example workflows** (workflow)
  - https://github.com/kijai/ComfyUI-WanVideoWrapper/tree/main/example_workflows
  - *From: Gateway*

- **MultiGPU ComfyUI node** (tool)
  - https://github.com/pollockjj/ComfyUI-MultiGPU
  - *From: AJO*

- **DiffSynth Studio Wan 2.2 commit** (repo)
  - https://github.com/modelscope/DiffSynth-Studio/commit/9015d08927331a7b5b559ed17412558279690c33
  - *From: Kijai*

- **Wan-AI HuggingFace org** (model)
  - https://huggingface.co/Wan-AI
  - *From: yi*

- **ComfyUI-GIMM-VFI** (repo)
  - https://github.com/kijai/ComfyUI-GIMM-VFI
  - *From: OxygenConsumer*

- **AI Toolkit for Wan LoRA training** (tool)
  - *From: gokuvonlange*

- **Wan2.1-NABLA models** (model)
  - https://huggingface.co/ai-forever/Wan2.1-T2V-14B-NABLA-0.7
  - *From: phazei*

- **NABLA GitHub repo** (repo)
  - https://github.com/gen-ai-team/Wan2.1-NABLA
  - *From: phazei*

- **DiffSynth-Studio Wan 2.2 branch** (repo)
  - https://github.com/modelscope/DiffSynth-Studio/tree/wan2.2
  - *From: Kijai*

- **SeC segmentation model** (repo)
  - https://github.com/OpenIXCLab/SeC
  - *From: MysteryShack*

- **lightx2v converted model** (model)
  - https://huggingface.co/maithink/lightx2vfp8/tree/main
  - *From: hicho*

- **LM-Studio image to text node** (node)
  - https://github.com/mattjohnpowell/comfyui-lmstudio-image-to-text-node
  - *From: phazei*

- **Kijai's Lightx2v LoRAs** (lora)
  - https://huggingface.co/Kijai/WanVideo_comfy/tree/main/Lightx2v
  - *From: phazei*

- **Wan 2.2 ModelScope link** (model)
  - https://modelscope.cn/models/Wan-AI/Wan2.2-TI2V-5B
  - *From: Kijai*

- **Wan 2.2 VAE** (model)
  - https://www.modelscope.cn/models/muse/wan2.2-vae
  - *From: yi*

- **Loop video workflow** (workflow)
  - https://openart.ai/workflows/nomadoor/loop-anything-with-wan21-vace/qz02Zb3yrF11GKYi6vdu
  - *From: gokuvonlange*

- **Alibaba livestream** (livestream)
  - https://live.bilibili.com/31811590
  - *From: multiple users*

- **DiffSynth training script** (repo)
  - https://github.com/modelscope/DiffSynth-Studio/blob/29663b25a65d35f129a88dadbe28e74e895c0a49/examples/wanvideo/model_training/lora/Wan2.2-T2V-A14B.sh
  - *From: seruva19*

- **VACE workflow documentation** (documentation)
  - https://scrapbox.io/work4ai/%F0%9F%A6%8AWan2.1_VACE
  - *From: Дмитрий Марков*

- **Wan-AI ModelScope** (model)
  - https://modelscope.cn/organization/Wan-AI
  - *From: zelgo_*

- **Wan-AI HuggingFace** (model)
  - https://huggingface.co/Wan-AI
  - *From: zelgo_*

- **ComfyUI repackaged models** (model)
  - https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/tree/main/split_files/diffusion_models
  - *From: Kijai*

- **ComfyUI examples** (workflow)
  - https://comfyanonymous.github.io/ComfyUI_examples/wan22/
  - *From: comfy*

- **ComfyUI blog post** (documentation)
  - https://blog.comfy.org/p/wan22-day-0-support-in-comfyui
  - *From: N0NSens*

- **GitHub repository** (repo)
  - https://github.com/Wan-Video/Wan2.2.git
  - *From: samhodge*

- **Wan 2.2 ComfyUI Repackaged** (model)
  - https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Wan 2.2 Original/Diffusers** (model)
  - https://huggingface.co/collections/multimodalart/wan-22-688767e313337b434ed55112
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Kijai WanVideo fp8 scaled** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy_fp8_scaled
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Wan official website** (website)
  - https://wan.video/welcome
  - *From: Siraj*

- **Hunyuan fp8 optimization code** (repo)
  - https://github.com/Tencent-Hunyuan/HunyuanVideo/blob/main/hyvideo/modules/fp8_optimization.py
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Wan 2.2 GGUF test models** (model)
  - https://huggingface.co/lym00/Wan2.2_TI2V_5B-gguf-test/tree/main
  - *From: Valle*

- **Wan 2.2 I2V 14B GGUF** (model)
  - https://huggingface.co/bullerwins/Wan2.2-I2V-A14B-GGUF
  - *From: 🦙rishappi*

- **Wan 2.1 ControlNets collection** (model)
  - https://huggingface.co/collections/TheDenk/wan21-controlnets-68302b430411dafc0d74d2fc
  - *From: xwsswww*

- **Wan 2.2 Prompt Generator GPT** (tool)
  - https://chatgpt.com/g/g-6887849e21b8819183e20c1dc6bcf353-wan-2-2-prompt-generator
  - *From: JohnDopamine*

- **Official ComfyUI Wan 2.2 documentation** (documentation)
  - https://docs.comfy.org/tutorials/video/wan/wan2_2
  - *From: Purz*

- **ComfyUI Wan 2.2 examples** (workflow)
  - https://comfyanonymous.github.io/ComfyUI_examples/wan22/
  - *From: crinklypaper*

- **RES4LYF sampler repository** (repo)
  - https://github.com/ClownsharkBatwing/RES4LYF
  - *From: Alisson Pereira*

- **VACE test models** (model)
  - https://huggingface.co/lym00/Wan2.2_T2V_14B_VACE-test/tree/main
  - *From: yo9o*

- **Scaled text encoder** (model)
  - https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/blob/main/split_files/text_encoders/umt5_xxl_fp8_e4m3fn_scaled.safetensors
  - *From: QANICS🕐*

- **Adaptive rank LoRA** (lora)
  - JohnDopamine's HuggingFace
  - *From: JohnDopamine*

- **LightX2V LoRA for WAN 2.2** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/blob/main/Lightx2v/lightx2v_14B_T2V_cfg_step_distill_lora_adaptive_rank_quantile_0.15_bf16.safetensors
  - *From: Juampab12*

- **WAN 2.2 training script** (repo)
  - https://github.com/modelscope/DiffSynth-Studio/blob/main/examples/wanvideo/model_training/lora/Wan2.2-I2V-A14B.sh
  - *From: Alisson Pereira*

- **WAN 2.2 official config** (repo)
  - https://github.com/Wan-Video/Wan2.2/blob/main/wan/configs/shared_config.py
  - *From: aikitoria*

- **LightX2V issue for WAN 2.2 support** (repo)
  - https://github.com/ModelTC/LightX2V/issues/173
  - *From: hicho*

- **Wan 2.2 Prompt Generator GPT** (tool)
  - https://chatgpt.com/g/g-6887849e21b8819183e20c1dc6bcf353-wan-2-2-prompt-generator
  - *From: Juampab12*

- **ComfyUI official Wan 2.2 documentation** (documentation)
  - https://docs.comfy.org/tutorials/video/wan/wan2_2
  - *From: Purz*

- **LightX2V i2v lora** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/blob/main/Lightx2v/lightx2v_14B_T2V_cfg_step_distill_lora_adaptive_rank_quantile_0.15_bf16.safetensors
  - *From: Juampab12*

- **Distill 2.1 model** (model)
  - https://huggingface.co/maithink/lightx2vfp8/tree/main
  - *From: hicho*

- **Wan 2.2 GGUF quantizations** (model)
  - https://huggingface.co/QuantStack/Wan2.2-T2V-A14B-GGUF/tree/main
  - *From: hicho*

- **Self-Forcing Plus repo for distill models** (repo)
  - https://github.com/GoatWu/Self-Forcing-Plus
  - *From: yi*

- **Janky memory patcher for OOM issues** (tool)
  - https://github.com/drozbay/janky_memory_patcher
  - *From: JohnDopamine*

- **Kijai's fp8 scaled models** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy_fp8_scaled/tree/main/T2V
  - *From: Kijai*

- **WanVideoWrapper update** (repo)
  - https://github.com/kijai/ComfyUI-WanVideoWrapper/pull/883
  - *From: Kijai*

- **Wan 2.2 Prompt Generator** (tool)
  - https://chatgpt.com/g/g-6887849e21b8819183e20c1dc6bcf353-wan-2-2-prompt-generator
  - *From: Nekodificador*

- **BlockSwap helper node** (tool)
  - https://github.com/orssorbit/ComfyUI-wanBlockswap
  - *From: Persoon*

- **Wan 2.2 prompter (mostly uncensored)** (tool)
  - https://prompter--thaakeno.on.websim.com/
  - *From: thaakeno*

- **Wan 2.2 tomato slicing example tweet** (demo)
  - https://x.com/thaakeno/status/1949934224980492324
  - *From: thaakeno*

- **TCFG technique documentation** (research)
  - https://5410tiffany.github.io/tcfg.github.io/
  - *From: Kijai*

- **Working GGUF I2V High-Noise model** (model)
  - https://huggingface.co/QuantStack/Wan2.2-I2V-A14B-GGUF/resolve/main/HighNoise/Wan2.2-I2V-A14B-HighNoise-Q6_K.gguf?download=true
  - *From: Kijai*

- **Official ComfyUI workflows** (workflow)
  - https://comfyanonymous.github.io/ComfyUI_examples/wan22/
  - *From: JohnDopamine*

- **Kijai fp8 scaled model** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy_fp8_scaled
  - *From: Kijai*

- **VACE test model** (model)
  - https://huggingface.co/lym00/Wan2.2_T2V_A14B_VACE-test
  - *From: TK_999*

- **ComfyUI issue about sage attention** (repo)
  - https://github.com/comfyanonymous/ComfyUI/issues/8274
  - *From: phazei*

- **Kijai's scaled fp8 models** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy_fp8_scaled
  - *From: Kijai*

- **QuantStack Wan2.2 GGUF models** (model)
  - https://huggingface.co/QuantStack/Wan2.2-I2V-A14B-GGUF
  - *From: Kijai*

- **VRGameDevGirl84's workflow** (workflow)
  - *From: VRGameDevGirl84(RTX 5090)*

- **LightX2V I2V LoRA** (lora)
  - https://huggingface.co/lightx2v/Wan2.1-I2V-14B-480P-StepDistill-CfgDistill-Lightx2v/tree/main/loras
  - *From: Jonathan*

- **LightX2V T2V LoRA** (lora)
  - https://huggingface.co/lightx2v/Wan2.1-T2V-14B-StepDistill-CfgDistill-Lightx2v/tree/main/loras
  - *From: Jonathan*

- **Wan 2.2 I2V GGUF** (model)
  - https://huggingface.co/bullerwins/Wan2.2-I2V-A14B-GGUF
  - *From: Jonathan*

- **Wan 2.2 T2V GGUF** (model)
  - https://huggingface.co/bullerwins/Wan2.2-T2V-A14B-GGUF
  - *From: Jonathan*

- **ComfyUI workflows** (workflow)
  - https://comfyanonymous.github.io/ComfyUI_examples/wan22/
  - *From: Jonathan*

- **FastWan LoRA** (lora)
  - https://huggingface.co/Kijai/WanVideo_comfy/tree/main/FastWan
  - *From: mamad8*

- **FusionX LoRA** (lora)
  - https://huggingface.co/vrgamedevgirl84/Wan14BT2VFusioniX/tree/main/FusionX_LoRa
  - *From: mamad8*

- **Wan 2.2 GGUF alternative** (model)
  - https://huggingface.co/QuantStack/Wan2.2-T2V-A14B-GGUF
  - *From: halkony*

- **Comfy-Org Repackaged Models** (model)
  - https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/tree/main/split_files/diffusion_models
  - *From: Zuko*

- **Wan 2.2 Prompt Creator GPT** (tool)
  - https://chatgpt.com/g/g-688805b301ec81918e3a5a45dbb8405b-wan2-2-prompt-creator
  - *From: ✧ฅโ๑ↀᆺↀ ๑ใฅ✧PookieNumnums*

- **LightX2V i2v LoRA rank64** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/blob/main/Lightx2v/lightx2v_I2V_14B_480p_cfg_step_distill_rank64_bf16.safetensors
  - *From: Kijai*

- **Simplified Wan 2.2 i2v workflow** (workflow)
  - shared as image
  - *From: Vardogr*

- **Kijai WanVideoWrapper fp8_scaled models** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy_fp8_scaled/
  - *From: Kijai*

- **TAEW VAE safetensors** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/blob/main/taew2_1.safetensors
  - *From: Kijai*

- **WanVideoWrapper example workflows** (workflow)
  - https://github.com/kijai/ComfyUI-WanVideoWrapper/tree/main/example_workflows
  - *From: Janosch Simon*

- **LightX2V LoRAs backup location** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/tree/main/Lightx2v
  - *From: Kijai*

- **Wan prompt format reference** (repo)
  - https://github.com/Wan-Video/Wan2.2/blob/388807310646ed5f318a99f8e8d9ad28c5b65373/wan/utils/system_prompt.py#L3
  - *From: kendrick*

- **WAN 2.2 prompt guide** (guide)
  - https://alidocs.dingtalk.com/i/nodes/jb9Y4gmKWrx9eo4dCql9LlbYJGXn6lpz
  - *From: slmonker(5090D 32GB)*

- **TCFG implementation** (technique)
  - https://5410tiffany.github.io/tcfg.github.io/
  - *From: Kijai*

- **Kijai's scaled WAN 2.2 models** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy_fp8_scaled
  - *From: Kijai*

- **LightX2V issue tracker** (repo)
  - https://github.com/ModelTC/LightX2V/issues/173#issuecomment-3130873877
  - *From: Doctor Shotgun*

- **Wan 2.2 English Guide** (guide)
  - https://alidocs.dingtalk.com/i/nodes/EpGBa2Lm8aZxe5myC99MelA2WgN7R35y
  - *From: hicho*

- **WanVideo fp8_e3m2 scaled model** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy_fp8_scaled
  - *From: Kijai*

- **ComfyUI example I2V workflow** (workflow)
  - https://github.com/comfyanonymous/ComfyUI_examples/blob/3eb0ae663ac044729494be42cb0f17a8c4151ec5/wan22/image_to_video_wan22_14B.json
  - *From: hiroP*

- **T2V wrapper workflow with NAG** (workflow)
  - *From: patientx*

- **Wan 2.2 ComfyUI Repackaged** (model)
  - https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged
  - *From: Dream Making*

- **WanVideo ComfyUI Wrapper** (repo)
  - https://huggingface.co/Kijai/WanVideo_comfy/tree/main
  - *From: JohnDopamine*

- **LightX2V LoRAs** (lora)
  - https://huggingface.co/Kijai/WanVideo_comfy/tree/main/Lightx2v
  - *From: Kijai*

- **FastWan LoRAs** (lora)
  - https://huggingface.co/Kijai/WanVideo_comfy/tree/main/FastWan
  - *From: Kijai*

- **Updated e5m2 scaled models** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy_fp8_scaled/blob/main/T2V/
  - *From: Kijai*

- **Distillation research paper** (paper)
  - https://arxiv.org/pdf/2507.14805
  - *From: fredbliss*

- **wan22FastWorkflow81FramesIn5Minutes_v10** (workflow)
  - civitai
  - *From: Samy*

- **Alibaba Wan 2.2 documentation** (documentation)
  - https://alidocs.dingtalk.com/i/nodes/EpGBa2Lm8aZxe5myC99MelA2WgN7R35y
  - *From: drbaph*

- **shrug-prompter** (tool)
  - https://github.com/fblissjr/shrug-prompter
  - *From: fredbliss*

- **Wan 2.2 workflow with SaveLatent/LoadLatent** (workflow)
  - embedded in Discord image
  - *From: Mngbg*

- **ControlNet workflow for Wan 2.2** (workflow)
  - embedded in Discord image
  - *From: SonidosEnArmonía*

- **DJZ-Nodes for automated save/load** (repo)
  - https://github.com/MushroomFleet/DJZ-Nodes
  - *From: The Shadow (NYC)*

- **Dreamina by CapCut** (tool)
  - https://dreamina.capcut.com/
  - *From: slmonker(5090D 32GB)*

- **LightX2V repository** (repo)
  - https://github.com/ModelTC/LightX2V
  - *From: hicho*

- **Wan 2.2 T2V A14B VACE test model** (model)
  - https://huggingface.co/lym00/Wan2.2_T2V_A14B_VACE-test
  - *From: loopen44*

- **DJZ Load Latent V2 documentation** (tool)
  - https://github.com/MushroomFleet/DJZ-Nodes/blob/main/DJZLoadLatentV2.md
  - *From: The Shadow (NYC)*

- **Denge AI Prompt Generator for Wan 2.2** (tool)
  - https://dengeai.com/prompt-generator
  - *From: hicho*

- **Wan 2.2 GGUF models** (model)
  - https://huggingface.co/bullerwins/Wan2.2-I2V-A14B-GGUF/tree/main
  - *From: Daflon*

- **Wan 2.2 VAE** (model)
  - https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/resolve/main/split_files/vae/wan2.2_vae.safetensors
  - *From: DiXiao*

- **LightX2V LoRAs** (lora)
  - https://huggingface.co/Kijai/WanVideo_comfy/tree/main/Lightx2v
  - *From: Daflon*

- **Wan 2.2 14B GGUF models** (model)
  - https://huggingface.co/QuantStack/Wan2.2-T2V-A14B-GGUF/tree/main/HighNoise
  - *From: xwsswwx*

- **ComfyUI MultiGPU nodes** (node)
  - https://github.com/pollockjj/ComfyUI-MultiGPU
  - *From: Jonathan*

- **Wan2.1 Apex Framepack** (model)
  - https://huggingface.co/totoku/Wan2.1-Apex-Framepack
  - *From: yi*

- **Apex Framepack code** (repo)
  - https://github.com/totokunda/apex
  - *From: yi*

- **ComfyUI-bleh nodes for native Wan 2.2** (node)
  - https://github.com/blepping/ComfyUI-bleh
  - *From: Kijai*

- **Wan 2.2 VAE fp16** (model)
  - https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/blob/main/split_files/vae/wan2.2_vae.safetensors
  - *From: comfy*

- **Tiny VAE for Wan** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/blob/main/taew2_1.safetensors
  - *From: Kijai*

- **FastWan LoRAs** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/tree/main/FastWan
  - *From: phazei*

- **Wan 2.2 prompt creator GPT** (tool)
  - https://chatgpt.com/g/g-688805b301ec81918e3a5a45dbb8405b-wan2-2-prompt-creator
  - *From: ✧ฅโ๑ↀᆺↀ ๑ใฅ✧PookieNumnums*

- **RES4LYF custom nodes** (repo)
  - https://github.com/ClownsharkBatwing/RES4LYF
  - *From: Juan Gea*

- **LightX2V LoRAs** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/tree/main/Lightx2v
  - *From: SonidosEnArmonía*

- **Nunchaku Flux Kontext** (model)
  - https://huggingface.co/nunchaku-tech/nunchaku-flux.1-kontext-dev
  - *From: ˗ˏˋ⚡ˎˊ-*

- **DJZ-Nodes auto load latent** (repo)
  - https://github.com/MushroomFleet/DJZ-Nodes/blob/main/DJZLoadLatentV2.md
  - *From: The Shadow (NYC)*

- **DeepGraph documentation** (tool)
  - https://www.deepgraph.co/kijai/ComfyUI-WanVideoWrapper
  - *From: thaakeno*

- **DeepWiki documentation** (tool)
  - https://deepwiki.com/kijai/ComfyUI-WanVideoWrapper
  - *From: ˗ˏˋ⚡ˎˊ-*

- **ComfyUI-NAG nodes** (repo)
  - https://github.com/ChenDarYen/ComfyUI-NAG
  - *From: TK_999*

- **LightX2V ComfyUI Wrapper** (repo)
  - https://github.com/ModelTC/ComfyUI-Lightx2vWrapper
  - *From: DrJKL*

- **LightX2V main repo** (repo)
  - https://github.com/ModelTC/lightx2v
  - *From: hicho*

- **Skywork-UniPic-1.5B** (model)
  - https://huggingface.co/Skywork/Skywork-UniPic-1.5B
  - *From: TK_999*

- **All-in-one WAN 2.2 merge** (model)
  - https://huggingface.co/Phr00t/WAN2.2-14B-Rapid-AllInOne
  - *From: DawnII*

- **MediaSyncer video comparison tool** (tool)
  - https://whatdreamscost.github.io/MediaSyncer/
  - *From: JohnDopamine*

- **MediaSyncer GitHub repo** (repo)
  - https://github.com/WhatDreamsCost/MediaSyncer
  - *From: JohnDopamine*

- **Instagram women Wan 2.1 and 2.2 LoRAs** (model)
  - https://civitai.com/models/1539088/instagram-women-wan-21-and-22?modelVersionId=2065096
  - *From: hicho*

- **SageAttention 2.2.0 releases** (tool)
  - https://github.com/woct0rdho/SageAttention/releases
  - *From: MiGrain*

- **Kijai's Wan 2.2 models** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy_fp8_scaled
  - *From: crinklypaper*

- **Wan 2.2 5B model** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy_fp8_scaled/tree/main/TI2V
  - *From: hicho*

- **Consolidated 2.2 model** (model)
  - https://huggingface.co/Phr00t/WAN2.2-14B-Rapid-AllInOne
  - *From: wange1002*

- **Ablejones' test workflow** (workflow)
  - shared in PNG file
  - *From: Ablejones*

- **LightX2V T2V LoRA** (lora)
  - https://huggingface.co/Kijai/WanVideo_comfy/tree/main/Lightx2v
  - *From: VK (5080 128gb)*

- **Skyreels i2v 540p fp8 e5m2 model** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/tree/main/Skyreels
  - *From: mdkb*

- **Wan 2.2 workflow with MMaudio** (workflow)
  - *From: thaakeno*

- **SageAttention 2.2** (tool)
  - https://github.com/woct0rdho/SageAttention/releases
  - *From: Ashtar*

- **MediaSyncer web app** (tool)
  - https://whatdreamscost.github.io/MediaSyncer/
  - *From: JohnDopamine*

- **WAN 2.2 model files** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy_fp8_scaled
  - *From: Kijai*

- **T5 encoder** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/blob/main/umt5-xxl-enc-bf16.safetensors
  - *From: Kijai*

- **Basic T2V workflow for WAN 2.2 14B** (workflow)
  - *From: AJO*

- **VioletEvergarden anime LoRA** (lora)
  - https://civitai.com/models/1759310/violetevergardenstyle-wan21-t2v-14b?modelVersionId=1991078
  - *From: VK (5080 128gb)*

- **WAN 2.2 14B GGUF V2V workflow** (workflow)
  - *From: thaakeno*

- **Motion LoRA camera push-in for WAN 14B** (lora)
  - https://civitai.com/models/1784288/motion-lora-camera-push-in-wan-14b-720p-i2v
  - *From: shockgun*

- **EchoShot repository** (repo)
  - https://github.com/D2I-ai/EchoShot
  - *From: Kijai*

- **LightX2V repository** (repo)
  - https://github.com/ModelTC/LightX2V
  - *From: hicho*

- **LightX2V LoRA for 14B** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/blob/main/Lightx2v/lightx2v_14B_T2V_cfg_step_distill_lora_adaptive_rank_quantile_0.15_bf16.safetensors
  - *From: Juampab12*

- **Cseti WAN 2.2 T2V workflow** (workflow)
  - https://github.com/cseti007/ComfyUI-Workflows/blob/main/cseti_dance_wanvideo2_2_T2V_A14B_example.json
  - *From: Cseti*

- **ColPali multi-vector embedding** (repo)
  - https://github.com/illuin-tech/colpali
  - *From: fredbliss*

- **quantile_0.15 LoRA** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/blob/main/Lightx2v/lightx2v_14B_T2V_cfg_step_distill_lora_adaptive_rank_quantile_0.15_bf16.safetensors
  - *From: The Shadow (NYC)*

- **Wan 2.2 ControlNet Depth** (model)
  - https://huggingface.co/TheDenk/wan2.2-ti2v-5b-controlnet-depth-v1
  - *From: VK*

- **5B I2V LoRA** (model)
  - https://huggingface.co/ostris/wan22_5b_i2v_crush_it_lora
  - *From: hicho*

- **V2V Workflow** (workflow)
  - https://huggingface.co/thaakeno46/ComfyUI-Workflows/resolve/main/WAN%202.2%2014B%20(GGUF)%20V2V.json
  - *From: thaakeno*

- **AbstractEyes encoder system** (repo)
  - https://github.com/AbstractEyes
  - *From: TK_999*

- **Pruna AI service** (service)
  - https://www.pruna.ai
  - *From: gokuvonlange*

- **Person mask generator ComfyUI node** (tool)
  - https://github.com/djbielejeski/a-person-mask-generator
  - *From: gokuvonlange*

- **CausVid 2.2 support request** (repo)
  - https://github.com/tianweiy/CausVid/issues/54
  - *From: hicho*

- **Benji's AI Playground channel** (educational)
  - https://www.youtube.com/@BenjisAIPlayground
  - *From: lovis.io*

- **Wan 2.2 VACE test model** (model)
  - https://huggingface.co/lym00/Wan2.2_T2V_A14B_VACE-test
  - *From: lovis.io*


## Known Limitations

- **LightX2V has slow motion effect**
  - Might be trained on higher fps videos (24/25) so outputting at 16 fps creates slow motion appearance
  - *From: Vardogr*

- **Context windows don't work with camera movement**
  - Context windows fail if there's any camera movement, uni3c is a bandaid but affects overall motion quality too much
  - *From: Kijai*

- **RecamMaster quality not very usable**
  - Quality is low, maybe usable with 2nd pass
  - *From: Kijai*

- **High Speed Dynamic lora undertrained**
  - HSD lora is a little undertrained but shows great potential with more data
  - *From: Jonathan*

- **MultiTalk deteriorates on longer clips**
  - Not even same person at 15 seconds, uses image from previous gen causing quality loss
  - *From: Kijai*

- **VACE with MultiTalk less accurate**
  - Works but accuracy definitely not the same as doing MultiTalk solo
  - *From: Tango Adorbo*

- **MultiTalk context window issues**
  - Creates attention masks internally but can't carry them over to next segment properly
  - *From: Tango Adorbo*

- **ThinkSound adds unwanted music**
  - Getting music in every video test, hard to control audio output
  - *From: VRGameDevGirl84(RTX 5090)*

- **VACE doesn't take frame exactly as is**
  - More like an interpretation rather than exact frame reproduction
  - *From: Juan Gea*

- **Moving camera with uni3c doesn't work well**
  - I2V tries to snap back to init image on each window
  - *From: Kijai*

- **Extension method degrades over time**
  - Better movement and audio sync but quality degrades with longer duration
  - *From: Kijai*

- **LightX2V black output issue with I2V models**
  - Reported issue with no solution provided
  - *From: Persoon*

- **Radial attention doesn't work for RTX 3xxx**
  - Only improves speed on RTX 40xx and 50xx GPUs
  - *From: phazei*

- **Context window degradation**
  - Long generations still degrade over time, can't reliably do 1000 frames
  - *From: Kijai*

- **VACE not great at likeness**
  - VACE struggles with maintaining character likeness, Phantom might be better
  - *From: Hashu*

- **Multiple face generation quality**
  - WAN struggles with complex scenes or multiple faces, similar to SDXL limitations
  - *From: Colin*

- **WAN pixel art understanding**
  - WAN can't understand pixel style properly
  - *From: shockgun*

- **Skyreels continuity issues across seams**
  - When using forcing for extensions, continuity across seams is not satisfactory
  - *From: samhodge*

- **Depth control insufficient for faces**
  - Depth alone isn't strong enough signal for fine control of faces, not enough detail even with perfect CGI depth
  - *From: spacepxl*

- **LoRAs trained on images may affect motion**
  - Image-trained LoRAs can negatively affect motion of faces in video generation
  - *From: Jonathan*

- **Skyreels needs different settings**
  - LoRA strengths and shift parameters need to be adjusted differently compared to Wan
  - *From: VRGameDevGirl84(RTX 5090)*

- **14B high resfix LoRA doesn't exist**
  - It's harder to implement the method I use with the other models because the I2V system and its method are constantly trying to match the start and end images
  - *From: Juampab12*

- **Self-forcing LoRA reduces motion scale**
  - scale of motion seems to be much lower than my old workflow without self force
  - *From: lostintranslation*

- **MultiTalk requires 8GB+ VRAM**
  - with full block swap it might work, if you have the RAM... probably not
  - *From: Kijai*

- **RTX 3090 limited to 33 frames at 720x1280 for 14B i2v**
  - Cannot increase frame count without partial loading
  - *From: Rainsmellsnice*

- **VACE not trained with normal maps**
  - If normals work, it's through generalization not understanding, many normal maps don't work at all
  - *From: Kijai*

- **Character consistency issues with MultiTalk vid2vid**
  - Faces change during generation, would need fine-tuned LoRAs for consistency
  - *From: samhodge*

- **Context windows create jarring transitions**
  - More jarring than VACE extension because model only has noise/latents/control to stitch, no trained continuation method
  - *From: Kijai*

- **Older RTX GPUs (2000 series) have worse AI generation results**
  - Even with same workflows and sufficient RAM, results inferior to RTX 4000/5000 series
  - *From: xwsswww*

- **ComfyUI single progress bar limitation**
  - Cannot show subgraph execution in realtime, makes context generation progress unclear
  - *From: Kijai*

- **LightX2V has unwanted effects on I2V models**
  - T2V base distill doesn't work well with I2V, can cause issues when character needs to move
  - *From: Kijai*

- **Fast motion is difficult to achieve**
  - Fast motion seems to be a downside of current models, motion LoRAs help but only slightly
  - *From: Atlas*

- **Context windows have repetition and limited movement**
  - Though no degradation occurs, movement is restricted compared to other methods
  - *From: Kijai*

- **LCM sampler produces stippled effect**
  - Creates unwanted texture artifacts that may require post-processing to remove
  - *From: David Snow*

- **VACE doesn't work reliably with padding reference images**
  - Padding reference images isn't a definite solution, success is hit and miss
  - *From: mdkb*

- **MagRef limited to exact reference image content**
  - Very hard to prompt for different outfits or variations from reference images
  - *From: David Snow*

- **MultiTalk causes static character positioning**
  - People appear 'planted' compared to more dynamic movement possible with Phantom
  - *From: AJO*

- **No multi-GPU parallel attention support**
  - ComfyUI doesn't have anything that allows using VRAM from multiple GPUs for actual parallel processing
  - *From: Kijai*

- **VACE struggles with non-human reference images**
  - Works well with people using SAM2 masks but has very low success rate with other objects
  - *From: mdkb*

- **Magref LoRA didn't work well**
  - Kijai tried making a LoRA version but it didn't give decent results even on base I2V
  - *From: Kijai*

- **Style consistency issues with VACE**
  - Realistic style overrides stylized input images, changes to realistic on second frame
  - *From: 3Dmindscaper2000*

- **Motion compliance reduced with distilled LoRAs**
  - LightX2V and similar speed LoRAs seem to reduce compliance with motion LoRAs
  - *From: Ethan*

- **GGUF models are significantly slower than fp8**
  - Quite a bit slower performance compared to fp8 models
  - *From: Kijai*

- **Can't mix GGUF model + normal VACE module**
  - Currently not supported, need to use full VACE GGUF instead
  - *From: Kijai*

- **MultiTalk with VACE has lip sync issues**
  - It works but the lip sync is always somewhat off
  - *From: Kijai*

- **Full HD generation is resource intensive**
  - Too slow and resource heavy, better to generate at lower res and upscale
  - *From: David Snow*

- **Context frames don't work with I2V**
  - Context functionality is only available for T2V, not I2V workflows
  - *From: Kijai*

- **ExVideo LoRA limited to 1.3B model**
  - Cannot use ExVideo LoRA with 14B model variants
  - *From: Kijai*

- **Older GPUs don't support certain quantization**
  - 2060 doesn't support bf16 or fp8 natively due to older CUDA compute version
  - *From: hicho*

- **GGUF models are 20% slower**
  - Due to dequantization overhead during inference
  - *From: Kijai*

- **Some loras don't work with GGUF**
  - detailenhance and realismboost cause blocking with GGUF models in wrapper
  - *From: mdkb*

- **Frame count restrictions**
  - Less than 81 frames don't work as well, need frames divisible by certain values
  - *From: Kijai*

- **Film grain lora issues**
  - Works for T2I but causes problems in video generation
  - *From: VRGameDevGirl84(RTX 5090)*

- **VACE frame count limit**
  - Limited to 81 frames maximum
  - *From: Juampab12*

- **Cannot change inner speed/acceleration inside timeline**
  - Can only stretch and compress timelines, not modify internal motion dynamics
  - *From: Juampab12*

- **FreeInit heavy performance cost**
  - Runs whole generation again per iteration
  - *From: Kijai*

- **Context switching noticeable after each block**
  - Visible transitions when using context in wrapper for long videos
  - *From: ▲*

- **Wan model coherent output limited to 81 frames**
  - Cannot do coherent outputs past 81 frames without control
  - *From: Kijai*

- **MultiTalk voice dependency**
  - Not trained on every possible voice type, struggles with certain voices and fast audio
  - *From: Draken*

- **Progressive quality degradation above 81 frames**
  - Quality gets progressively worse with higher frame counts
  - *From: el marzocco*

- **Memory caching methods not viable on consumer hardware**
  - DiT hidden state caching uses too much memory and doesn't improve speed
  - *From: Kijai*

- **VACE depth control very strong**
  - Will morph input to fit depth map, difficult to control strength
  - *From: Draken*

- **Context windows incompatible with I2V models**
  - Can't provide init image to consequential windows since process is split
  - *From: Kijai*

- **LightX2V destroys motion when used with certain loras**
  - BJ movement lora gets destroyed when using LightX2V, even with increased CFG
  - *From: Kenk*

- **TeaCache incompatible with FusionX**
  - FusionX has built-in optimizations that conflict with TeaCache
  - *From: Juampab12*

- **Small faces always have detail problems**
  - Even using higher than 8 steps doesn't improve small face details much, needs detailer
  - *From: patientx*

- **Context Options change characters in v2v workflows**
  - Every context window shows new person when using high denoise v2v, unlike i2v/t2v
  - *From: mdkb*

- **Quality LoRAs cause face changes**
  - MPS and AccVid are usual suspects for causing face changes when added
  - *From: lostintranslation*

- **Multitalk imperfect lipsync and motion issues**
  - Lip sync way out with non-human faces, messes up motion when used with LightX2V
  - *From: AJO*

- **VACE produces dull/flat video without boosters**
  - Needs booster LoRAs to add pop and realism
  - *From: Grimm1111*

- **LoRA effects don't work with Vace I2V**
  - LoRAs only work with standard I2V model, not the Vace I2V variant
  - *From: hicho*

- **SeedVR2 VAE is major VRAM bottleneck**
  - Even with BlockSwap, VAE still consumes significant VRAM and needs tiling implementation
  - *From: Adrien Toupet*

- **SeedVR2 has no CFG scale control**
  - Currently lacks CFG scale flexibility, though workarounds exist
  - *From: Adrien Toupet*

- **ThinkSound produces poor quality audio**
  - Early tests show 'alien comms' quality, not matching demo samples
  - *From: JohnDopamine*

- **Distilled models reduce motion in I2V**
  - Step distilled models on I2V generally produce less motion compared to base models
  - *From: Kijai*

- **VACE doesn't work well with single frame generation**
  - Hit and miss results, better to use 5 frames
  - *From: Hashu*

- **VACE reference images have minimal effect**
  - Prompt is everything, reference images may be irrelevant in many cases
  - *From: AmirKerr*

- **VACE doesn't support blurred masks well for inpainting**
  - Gray values should stay consistent during inpainting
  - *From: ingi // SYSTMS*

- **SkyReels masking workflow doesn't work**
  - User reported SkyReels just didn't work at all for their use case
  - *From: AmirKerr*

- **VACE character consistency across shots**
  - Hard to get same character (gorilla) in every shot, reference image and same seed don't work for cross-shot consistency
  - *From: Nekodificador*

- **Easy Cache doesn't work with noise-adding samplers**
  - Doesn't work with samplers that add noise like dpm++_sde and lcm, which is bad for lightx2v
  - *From: Kijai*

- **Kontext lacks precision for pose control**
  - Not precise enough for actual pose following, only vaguely follows poses and uses image proportions instead of mannequin proportions
  - *From: Kijai*

- **No IPAdapter available for Wan**
  - No IPAdapter exists for Wan, spent hours looking and hacking with no success
  - *From: VRGameDevGirl84(RTX 5090)*

- **VACE less forgiving on single frame generation**
  - VACE is less forgiving when working with single frame situations
  - *From: mdkb*

- **Pusa training dataset too small**
  - Only 4K examples vs 10M+ for proper training
  - *From: Ada*

- **VACE depth maps fight with reference images**
  - Shape conflicts between depth map and reference image
  - *From: theUnlikely*

- **LightX2V LoRA incompatible with flow edit**
  - Cannot use speed optimization with flow edit
  - *From: theUnlikely*

- **Strong non-commercial use licenses**
  - Many models have restrictive licensing
  - *From: mdkb*

- **SeedVR2 over-sharpening**
  - Tends to oversharpen content
  - *From: gokuvonlange*

- **VACE inpainting degraded performance**
  - Previously working workflows now have problems
  - *From: David Snow*

- **VACE required for mid-frame interpolation**
  - Only VACE model can do mid-frame generation, not available in regular I2V
  - *From: Kijai*

- **Model merge nodes don't work with KJ wrapper**
  - Native model merge nodes cannot connect to KJ wrapper sampler due to different loading architectures
  - *From: DawnII*

- **Skyreels produces greyish results standalone**
  - Skyreels as standalone often gives bad output and artifacts, works better when merged
  - *From: ▲*

- **LoRA changes trigger model reloading in wrapper**
  - Changing LoRA strength or stack in wrapper causes full model reload, unlike native nodes
  - *From: gokuvonlange*

- **T2V LoRA not working properly**
  - New T2V lightx2v lora produces errors and doesn't function correctly
  - *From: multiple users*

- **VACE and Uni3C incompatibility**
  - Cannot use VACE with Uni3C due to channel mismatch errors
  - *From: Juan Gea*

- **Extended generation degradation**
  - Extended video generation has degradation problem, solved for first 18 seconds
  - *From: Juan Gea*

- **720p I2V poor performance at lower resolutions**
  - 720p I2V model struggles with lower resolution inputs unlike 480p model
  - *From: Draken*

- **Original T2V LightX2V lora is broken**
  - Cannot be used properly, need to use re-extracted versions
  - *From: Kijai*

- **720P I2V LightX2V not yet available**
  - Repository exists but is empty, only 480P I2V version currently available
  - *From: multiple users*

- **PUSA requires 120GB disk space**
  - Heavy installation requirement that prevents many users from testing
  - *From: multiple users*

- **New LightX2V may sacrifice fine detail for motion**
  - Trade-off between motion improvement and spatial/detail quality
  - *From: Kijai*

- **Higher LightX2V strength can cause burning or lose illustration style**
  - At 2.0 strength loses adherence to prompt and illustration style
  - *From: patientx*

- **Pusa LoRA not CFG distilled**
  - Unlike LightX2V, Pusa requires higher step counts and doesn't work with other LoRAs
  - *From: Kijai*

- **VACE control only works on first batch**
  - Control images influence first batch properly but show up visually in continuation batches instead of controlling
  - *From: The Shadow (NYC)*

- **LightX2V videos incompatible with VACE extension**
  - Videos generated with LightX2V cause discoloration when extended with VACE, unlike base Wan videos
  - *From: daking999*

- **Uni3C is I2V only**
  - Uni3C cannot be used with VACE T2V workflows as it's designed for I2V
  - *From: ˗ˏˋ⚡ˎˊ-*

- **RES4LYF samplers don't work with wrapper**
  - Custom samplers from RES4LYF nodeset only work with native ComfyUI, not the wrapper
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Skyreels only model supporting native 24fps**
  - For true 24fps generation, Skyreels is the only option available
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Pusa last frame flashing**
  - Last frame flashes pretty bad, need workaround
  - *From: Kijai*

- **Pusa requires specific frame counts**
  - Must be 4 images minimum, always in groups of 4
  - *From: Kijai*

- **Scaled models don't work in wrapper**
  - Never looked into why scaled models fail
  - *From: Kijai*

- **Pusa not cfg distilled**
  - Using CFG reduces speed without quality benefit
  - *From: Kijai*

- **Radial attention not suitable for single frame generation**
  - Gets slower with each step for single frames, designed for video/movies
  - *From: patientx*

- **Pusa can't use context windows**
  - Has its own extension capabilities but incompatible with context window system
  - *From: Kijai*

- **LightX2V 720p repository is empty**
  - Only 480p versions available currently
  - *From: Doctor Shotgun*

- **Pusa not CFG distilled**
  - Cannot use CFG 1 effectively, needs proper CFG values
  - *From: Juampab12*

- **480p I2V LoRA doesn't deliver enough detail for 720p**
  - The 480p I2V LoRA lacks sufficient detail and quality for 720p generation
  - *From: Juan Gea*

- **PUSA workflow causes flashing with specific frames**
  - Main problem when trying to get specific frames, especially when intercalating frames
  - *From: Juan Gea*

- **Radial attention causes quality degradation**
  - Can be faster but affects quality. Shows crackling and strange effects on wrinkles
  - *From: Kijai, Draken*

- **PUSA modulation uses too much VRAM for longer generations**
  - Modulation takes so much VRAM that it doesn't get past 129 frames with more frames
  - *From: Kijai*

- **Radial attention requires resolutions divisible by 128**
  - Eliminates most default bucket sizes like 1280x720, 480x832, 832x480 except 512x512 and 768x768
  - *From: MatiaHeron*

- **Cannot merge multiple LoRAs efficiently with torch compile**
  - Torch compile doesn't work with model routing techniques for keeping multiple LoRAs in RAM
  - *From: Kijai*

- **GGUF model conversion failing for merged models**
  - Custom node can convert other quantizations but not GGUF
  - *From: patientx*

- **PUSA incompatible with context windows**
  - Scheduler causes timestep expansion that prevents context window chunking
  - *From: Kijai*

- **Phantom produces poor results at CFG 1**
  - Needs higher CFG and at least 8 steps, needs negative embeds to work properly
  - *From: Piblarg*

- **Uni3C cannot be combined with VACE**
  - Uni3C is img2vid based so incompatible with VACE
  - *From: Piblarg*

- **Style LoRAs destroy Phantom performance**
  - Any sort of style LoRA negatively impacts Phantom results
  - *From: Piblarg*

- **New LightX2V can be too fast/speedy**
  - Especially problematic for scenes with humans or animals
  - *From: JohnDopamine/Gill Bastar*

- **Uni3C incompatible with VACE**
  - Uni and vace cannot be merged as they are based on different models. Uni3C is for I2V models only
  - *From: Piblarg*

- **Hard-baked motion blur in WAN**
  - Very much hard baked in motion blur. Whether it's a limitation on training/parameter size, if you observe any wan - high motion has it
  - *From: Piblarg*

- **Phantom struggles with animated content**
  - Phantom does have limitations - does realism well and struggles with animated stuff at times
  - *From: Piblarg*

- **WAN outpainting quality issues**
  - Left and right sides of outpainted image do not look good quality, appears dithered
  - *From: Gateway {Dreaming Computers}*

- **WAN produces cartoonish explosions**
  - Explosions look very comical, would need specific LoRA training on cinematic explosions to fix
  - *From: gokuvonlange*

- **Cannot join WAN latents for seamless extension**
  - Joining 2 sampler results causes artifacts on the seam, probably due to temporal VAE decoding latents in pairs
  - *From: Kijai*

- **Progressive degradation in multi-batch workflows**
  - Each 41 frame batch shows progressive shape drift, likely due to VAE encode/decode cycles
  - *From: A.I.Warper*

- **VACE loses lipsync when applied to CGI**
  - Using VACE depth pass on CGI input loses all lipsync
  - *From: samhodge*

- **Phantom model fragility**
  - The model itself is quite fragile to loras/other merges
  - *From: Piblarg*

- **PUSA can't use existing LoRAs effectively**
  - LoRAs would need to be trained specifically on Pusa model
  - *From: phazei*

- **Wan models have frame count limits**
  - Vanilla limited to 81 frames, >93 frames causes flash at start
  - *From: Kijai*

- **UNI3C requires I2V model**
  - Cannot be used with VACE
  - *From: Kijai*

- **Face consistency depends on face size**
  - Smaller faces in frame have greater probability of unlikeness
  - *From: N0NSens*

- **Phantom can be picky with subject interpretation**
  - Often you can get it to 'lock on' with a good enough description, but sometimes it just seems to almost ignore a subject
  - *From: Ablejones*

- **Fun Control reference adherence less reliable than VACE**
  - Fun reference adherence not as reliable as VACE for reference matching
  - *From: trax*

- **Unmerged LoRA performance penalty**
  - Unmerged LoRAs are slower per iteration, won't be great with too many LoRAs
  - *From: Kijai*

- **VACE module can't be used with GGUF models**
  - You can't stick the vace module into a gguf, all VACE gguf models have the module builtin
  - *From: Ablejones*

- **VACE pose control issues**
  - Pose control doesn't work as well as depth/lineart, may need different preprocessor
  - *From: Hashu*

- **Native sampler compatibility**
  - Many native samplers don't work with normal scheduler, DPM SDE++ produces foggy bad output in native
  - *From: Draken*

- **Phantom can be finicky**
  - Phantom can be finicky to trigger reference images, sometimes produces weird blends
  - *From: Piblarg*

- **FP8 FFN layer quality loss**
  - Something kills quality if you do FFN layers with fp8 matmul, so not worth using full fp8
  - *From: Kijai*

- **E4M3FN compatibility**
  - E4M3FN not supported on AMD RDNA2 and NVIDIA under 4000 series - only fp8e5 supported
  - *From: patientx*

- **VACE changes input images due to T2V nature**
  - Being T2V model first, VACE suffers from changing the input image and requires hyper-specific prompts
  - *From: 3Dmindscaper2000*

- **I2V models don't do frame interpolation**
  - I2V models are great but don't do interpolation of frames and cannot use ControlNet style guidance
  - *From: 3Dmindscaper2000*

- **Fun InP can't use control guidance**
  - Great for interpolation but cannot use any control guidance unlike other models
  - *From: 3Dmindscaper2000*

- **PUSA doesn't work with I2V models**
  - PUSA LoRA is designed for T2V models and won't function with I2V variants
  - *From: Kijai*

- **Quality degrades with longer single-shot generations**
  - Wan quality gets worse when generating many frames in one shot, requiring multi-segment approach
  - *From: enigmatic_e*

- **UniC3 conflicts with some LoRAs**
  - Too many LoRAs can cause conflicts with UniC3's 3D effects, kills some AI prompt effects
  - *From: hicho*

- **Last frame only mode may not work properly**
  - Errors occur when trying to bypass first frame and use only last frame
  - *From: Ruairi Robinson*

- **Cube-only scenes limit camera motion**
  - Simple cube scenes don't provide enough parallax information for complex camera movements
  - *From: pookyjuice, Ablejones*

- **UniC3 camera presets challenge**
  - Difficult to create universal camera motion presets that work with any input image
  - *From: VRGameDevGirl84(RTX 5090)*

- **Context windows still snap back to init image**
  - Even with MAGREF, some snapping occurs especially with weak camera movements
  - *From: Kijai*

- **MAGREF particular about input images**
  - Only works with certain images and prompts, requires experimentation
  - *From: Hashu*

- **Context windows are slow**
  - Has lots of issues and slower generation compared to normal inference
  - *From: Kijai*

- **5-step generation without LightX2V doesn't work well**
  - Despite claims it should work with 5 steps, actual results are poor without acceleration LoRAs
  - *From: Kijai*

- **DMP++_SDE sampler issues with scaled models**
  - User reported poor results with dmp++_sde sampler on scaled I2V model even with LightX2V
  - *From: Juan Gea*

- **Text generation accuracy**
  - AI-generated text in videos is often inaccurate, though the visual effects work well
  - *From: VK (5080 128gb)*

- **Text shattering timing**
  - Text shattering effects always start at the end of videos, cannot be controlled to start earlier
  - *From: VK (5080 128gb)*

- **Pusa incompatibility with I2V**
  - Pusa scheduler and LoRA only work with T2V models, not I2V
  - *From: Kijai*

- **Color drift in VACE extension**
  - Noticeable color drift and oversaturation when using VACE extension workflow
  - *From: lostintranslation*

- **VRAM constraints at high resolution**
  - Cannot process more than 26 frames at 1920x1152 resolution
  - *From: Juan Gea*

- **FPS artifacts with cross-model LoRAs**
  - Wan LoRAs might not work 100% with Skyreels V2 due to FPS change causing artifacts
  - *From: yi*

- **FastWan 1.3B not photorealistic**
  - Good for anime/cartoon content but not useful for photorealistic generation despite being 1.3B model
  - *From: Juan Gea*

- **PUSA doesn't work properly with I2V models**
  - I2V input is not in main latents, so PUSA LoRA has no effect when used incorrectly with I2V
  - *From: Kijai*

- **WAN 2.2 still limited to 5 seconds**
  - No modifications made during training for longer videos, still needs workarounds like kv cache or framepack
  - *From: 青龍聖者@bdsqlsz*

- **YUME trained only on street/drone footage**
  - Limited dataset makes it unsuitable for general use, aimed at controllable world model not general generation
  - *From: yi*

- **SageAttention 4-bit can't be used fully with WAN**
  - Sage3 must be used selectively by timesteps or layers, full 4-bit attention doesn't work
  - *From: Kijai*

- **Long video extension causes jerky movements**
  - Batch workflows for extension eventually introduce artifacts like heads spinning 300 degrees
  - *From: Gill Bastar*

- **Pusa creates new body parts instead of using existing ones**
  - When prompted 'raises hands up in surprise', creates new hands instead of moving existing hands in frame
  - *From: Kijai*

- **Fast Wan 1.3B poor hand and finger quality**
  - 1.3B model not as good as 14B model for hands and fingers
  - *From: patientx*

- **Quality degradation in video extensions**
  - Sudden camera changes and artifacts when extending videos over multiple sequences
  - *From: Juan Gea*

- **Pusa weak with new prompts during extension**
  - Adding new actions like 'blows out candle' produces minimal changes
  - *From: Kijai*

- **MultiTalk doesn't work well for lipsync**
  - Gets some syllables but misses others completely, loses phonemes
  - *From: MysteryShack*

- **WAN doesn't understand complex scenes like 'gym'**
  - Need to describe individual items instead of using general terms
  - *From: Ryzen*

- **16fps generation rate problematic for film work**
  - Makes it difficult for movie production that needs 24fps, interpolation not suitable for high-speed kinetic content
  - *From: Ruairi Robinson*

- **VACE has color degradation and shifting in long-form**
  - Cross-fading VACE segments always introduces quality degradation
  - *From: gokuvonlange*

- **Context windows reduce dynamic motion**
  - Becomes very repetitive for expressive motions like hand gestures
  - *From: Kijai*

- **WAN lacks concept understanding for abstract ideas**
  - Doesn't understand concepts like 'aura of death touch' or grass withering
  - *From: MysteryShack*

- **SageAttention 3 memory overhead**
  - Uses ~5GB more VRAM than sage2, making it useless on low resolutions. Requires block swapping on higher resolutions which negates speed benefits
  - *From: Kijai*

- **VACE T2V quality vs dedicated model**
  - VACE T2V has bad prompt adherence and produces inferior results compared to dedicated T2V 14B model for prompt-only generation
  - *From: gokuvonlange*

- **SageAttention 3 only works on RTX 50 series**
  - It's 5000 series only anyway
  - *From: Kijai*

- **Quality loss with SageAttention 3**
  - Output has weird wobbliness and looks like it has quality degradation compared to sage2
  - *From: Draken*

- **FastWan has less motion than LightX2V**
  - Produces solid images but significantly less motion compared to LightX2V
  - *From: phazei*

- **VSA/STA only works on H100**
  - Sliding Tile Attention and some VSA features are only usable on H100 GPUs
  - *From: Kijai*

- **Wan 2.2 30fps increases VRAM requirements**
  - 30fps means 160+ frames for 5 seconds, doubling VRAM usage to potentially 28GB+ for 720p
  - *From: Kijai*

- **Radial attention has quality hit**
  - Running radial attention on all steps produces noticeable quality degradation
  - *From: Kijai*

- **EchoShot only works with 1.3B model**
  - Currently limited to 1.3B variant, 14B version not available
  - *From: ZeusZeus*

- **EchoShot doesn't support image input**
  - Model doesn't have I2V cross-attention layers, only works with text prompts
  - *From: Kijai*

- **Quality issues with 1.3B base model**
  - Much lower quality compared to 14B, described as 'bad as SD vanilla 1.5'
  - *From: Drommer-Kille*

- **Limited LoRA selection for 1.3B model**
  - Very few LoRAs available for 1.3B compared to 14B
  - *From: VK*

- **Prompt adherence issues**
  - Model doesn't follow prompts super strong, especially when combined with VACE
  - *From: Kijai*

- **EchoShot produces weaker results than full model**
  - Works but quality is reduced compared to native capabilities
  - *From: Kijai*

- **Phantom model doesn't work well with VACE**
  - Compatibility issues when trying to combine them
  - *From: Kijai*

- **Skyreels has glitch at ~85 frames with high movement**
  - Jump/reverse/glitch occurs due to 81 frame training limitation
  - *From: N0NSens*

- **Multi-GPU doesn't reduce VRAM usage**
  - Only saves RAM and loading times, no VRAM benefit over offloading
  - *From: Kijai*

- **480p vs 720p models have no memory difference**
  - Resolution doesn't affect VRAM usage significantly
  - *From: Kijai*

- **VAE cannot handle alpha channels**
  - Alpha gets converted to colors causing dimension mismatch errors
  - *From: Kijai*

- **Cannot join Wan outputs in latent space**
  - Due to temporal VAE cross-information
  - *From: Kijai*

- **First frame problems beyond 81 frames**
  - Common issue when generating outside normal frame lengths
  - *From: Kijai*

- **VACE color shift issue**
  - Color matching doesn't seem to work effectively
  - *From: Dream Making*

- **Potential LoRA incompatibility with MoE**
  - Dual model architecture may break existing LoRA compatibility
  - *From: Kijai*

- **GGUF loading is slower**
  - GGUF models load slower initially compared to other formats
  - *From: Kijai*

- **CPU T5 encoding is major waste of time**
  - Running T5 on CPU instead of GPU significantly slows down processing
  - *From: Kijai*

- **Old LoRAs likely won't work with dual model structure**
  - The dual model structure of Wan 2.2 means old LoRAs probably won't be compatible
  - *From: Kijai*

- **Multitalking quality issues**
  - Audio quality is poor, regular talking doesn't work as well as singing
  - *From: samhodge*

- **EchoShot compatibility**
  - Only works with dpm++_sde scheduler and can stop working unexpectedly
  - *From: phazei*

- **Model compatibility uncertainty**
  - Unknown if existing LoRAs will work with Wan 2.2, especially 5B model
  - *From: phazei*

- **Canny control not working well with Wan**
  - User reports no influence when trying Canny with gguf model for i2i, possibly due to doubled up lines
  - *From: xwsswww*

- **VACE first-to-last looping imperfect**
  - First and last frames in output not exactly the same, making it hard to loop perfectly
  - *From: Yae*

- **Interpolation artifacts in motion**
  - Video motion shows jolts in fits and starts, especially noticeable with irregular organic motion like wheat fields or ocean waves
  - *From: Ruairi Robinson*

- **No backward compatibility with 2.1 LoRAs**
  - Completely new model architecture means old LoRAs won't work
  - *From: Draken*

- **Heavy VAE processing time**
  - VAE is 3x bigger and takes 22 seconds to decode 124 frames
  - *From: Kijai*

- **High VRAM usage**
  - VAE decode uses 31GB VRAM
  - *From: Gateway*

- **Wan 2.1 LoRAs incompatible with 2.2**
  - Different architectures make existing LoRAs unusable
  - *From: multiple users*

- **5B model quality issues**
  - Sometimes performs worse than 1.3B model, may need different approach
  - *From: Kijai*

- **VAE quality issues**
  - 5B VAE described as 'rough as all balls' with quality problems
  - *From: Draken*

- **High VRAM requirements for 14B**
  - Requires significantly more VRAM than single-stage models
  - *From: multiple users*

- **5B T2V model quality is poor**
  - Reported as not very good, far worse than even 1.3B model
  - *From: Kijai*

- **5B I2V also not good quality**
  - Both T2V and I2V variants of 5B model have quality issues
  - *From: Vérole*

- **CausVid doesn't work with Wan 2.2**
  - Previous speed optimization LoRA not compatible
  - *From: cyncratic*

- **Most existing 2.1 tools don't work with 2.2**
  - CausVid, FastWAN, and other 2.1 tools not compatible with 2.2
  - *From: Nokai*

- **5B model poor quality**
  - Even with fp8 loading, quality is poor across different samplers
  - *From: Mikerhinos*

- **High-noise model doesn't respond to VACE**
  - Only low-noise model responds to VACE blocks
  - *From: Ablejones*

- **Prompt adherence issues with high LoRA strength**
  - Setting LightX2V to strength 3+ causes poor prompt following
  - *From: Juampab12*

- **2.1 LoRAs not optimal on 2.2**
  - While compatible, LoRAs trained on 2.1 don't perform as well on 2.2
  - *From: anever*

- **Existing LoRAs cause quality degradation**
  - Old LoRAs trained on 2.1 don't work properly with 2.2, causing washed out results
  - *From: multiple users*

- **121 frame generations cause looping**
  - Using 121 frames results in video loops and poor prompt adherence
  - *From: Juampab12*

- **Poor prompt adherence with speed LoRAs**
  - LightX2V reduces prompt following ability compared to full steps
  - *From: gokuvonlange*

- **Model reloading required mid-generation**
  - Need to reload models between high and low noise passes
  - *From: Juampab12*

- **5B model produces poor face quality**
  - Multiple users report 5B model generates inferior faces compared to 1.3B model
  - *From: DiXiao*

- **LightX lora breaks above 81 frames**
  - Prompt adherence becomes completely different and looping occurs when using more than 81 frames with LightX
  - *From: gokuvonlange*

- **High noise model cannot handle low noise steps**
  - High noise model has no capability for low noise denoising steps
  - *From: Ablejones*

- **I2V loras from 2.1 incompatible with 2.2**
  - Key errors occur when using 2.1 i2v trained loras with 2.2 due to model size changes
  - *From: JohnDopamine*

- **VACE control doesn't work with high noise model**
  - Complete incompatibility between VACE and high noise model
  - *From: Ablejones*

- **LightX2V not optimized for 2.2**
  - Existing LightX2V LoRA needs retraining for proper compatibility with new models
  - *From: aikitoria*

- **Quality degradation with low quantization**
  - Quantization below Q6 causes significant quality loss, Q4 starts to fall apart
  - *From: Kijai*

- **Memory management issues with dual models**
  - Blockswap and memory management becomes more complex with two models
  - *From: Draken*

- **VACE doesn't work with 2.2 yet**
  - Control system not adapted for new architecture
  - *From: Kijai*

- **Phantom doesn't work with 2.2**
  - Character consistency model not compatible yet
  - *From: Kijai*

- **5B model fails on low resolutions**
  - Completely fails to work on familiar low resolutions, needs higher resolution to function
  - *From: Blink*

- **I2V destroys first frame with full step generation**
  - Using low noise only with full steps damages the input frame
  - *From: GOD_IS_A_LIE*

- **Some GGUF conversions are broken**
  - I2V A14B GGUF converter didn't account for image layers, causing errors
  - *From: Draken*

- **5B model face quality issues**
  - Disappointing face generation compared to 1.3B model
  - *From: DiXiao*

- **LightX kills motion**
  - Using LightX LoRA reduces dynamic motion in videos
  - *From: Nekodificador*

- **12GB VRAM insufficient for 14B models**
  - Requires offloading to system RAM, needs more than 32GB RAM
  - *From: Kijai*

- **Some wrapper samplers don't work with split models**
  - LCM/beta samplers may not work with 2.2 architecture
  - *From: Cubey*

- **Model switching issues in wrapper on subsequent runs**
  - After first generation, wrapper may not properly switch between high/low noise models
  - *From: MysteryShack*

- **Frame count limits prompt adherence**
  - Beyond 121 frames, prompt adherence breaks down significantly
  - *From: Relven 96gb*

- **2.2 VAE only works with 5B model**
  - 14B models still use 2.1 VAE, 2.2 VAE is 5B-specific
  - *From: multiple users*

- **Can't render 121 frames at 1080p on 5090**
  - Hardware limitations prevent full resolution at maximum frame count
  - *From: GOD_IS_A_LIE*

- **First frame flickering over 81 frames**
  - Known issue when generating videos longer than 81 frames
  - *From: MysteryShack*

- **Repackaged models not compatible with Kijai's wrapper**
  - The repackaged models aren't playing nice with Kijai's wrapper nodes currently
  - *From: halkony*

- **VACE doesn't work well with Wan 2.2**
  - Especially the high-noise model doesn't respond the same way as 2.1, requires hacking to make it work
  - *From: Ablejones*

- **LightX2V diminishes prompt adherence**
  - Higher LightX2V strength can reduce how well the model follows prompts
  - *From: MysteryShack*

- **T5 encoder only handles 81 frame consistency**
  - For longer videos, prompt scheduling needed as T5 can't maintain consistency beyond 81 frames
  - *From: Relven 96gb*

- **6-step generation only works with minimal motion**
  - Low step counts require barely any movement to work properly
  - *From: jeffcookio*

- **Speed LoRAs cause slow-motion effect**
  - LightX2V and CausVid both produce slow-motion appearance
  - *From: kendrick*

- **No proper distillation for high noise model yet**
  - Any LoRAs applied with low steps will ruin motion quality
  - *From: Kijai*

- **5B model has very slow VAE**
  - Makes 5B slower than 14B despite smaller size
  - *From: Drommer-Kille*

- **Model appears trained with 81 frames limit**
  - Going above 81 frames produces blurry or poor results
  - *From: Kijai*

- **Speed LoRAs suffer from not working well with high noise stage**
  - More steps required as speed optimizations don't work as effectively
  - *From: blake37*

- **Can't get video to look exactly like input even at 0.01 denoise**
  - Even minimal denoise changes the appearance significantly
  - *From: VK*

- **Radial attention has high chance of hurting motion with high model**
  - Too risky to use on high noise stage
  - *From: Kijai*

- **VACE compatibility issues with high noise model**
  - VACE works very badly with the high noise model, especially for start frame or reference
  - *From: Kijai*

- **LightX2V kills motion with 14B model**
  - Using LightX2V LoRA with 14B model reduces motion quality significantly
  - *From: Nekodificador*

- **Cannot use high noise model alone**
  - High noise model must be paired with low noise model, cannot run independently
  - *From: Kijai*

- **Long generation times without acceleration**
  - 14B model without LoRA takes 15-20 minutes per video
  - *From: Nekodificador*

- **Control/VACE doesn't work with high noise model**
  - Can only use control inputs with low noise model
  - *From: Kijai*

- **Motion quality degrades beyond 81 frames**
  - At 160 frames motion becomes barely visible
  - *From: Kijai*

- **High noise model can't resolve final quality**
  - Requires low noise pass for proper image quality
  - *From: Kijai*

- **5B model support incomplete**
  - 5B model works but not tested enough to confirm correctness
  - *From: Kijai*

- **Wan 14B unrunnable with 12GB VRAM**
  - Even with Q4 quantization and high noise only, not enough memory
  - *From: QANICS*

- **Resolution affects motion quality**
  - 0.8 megapixels produces worse results than 0.4 megapixels
  - *From: Fictiverse*

- **LoRAs not trained on exact model perform poorly**
  - LoRAs trained on different models don't transfer well to Wan 2.2
  - *From: Kijai*

- **LightX2V issues with 121 frames**
  - Can't work well with 121 frames, causes video reversals. Works better with 81 frames
  - *From: N0NSens*

- **VACE color matching problems**
  - Animation follows movement well but color doesn't match reference image properly
  - *From: Sal TK FX*

- **Memory management issues with ComfyUI caching**
  - Python won't free memory if there's reference to it, and ComfyUI caches node outputs so models can't be fully freed
  - *From: Kijai*

- **5B model poor face quality**
  - 5B model has been rubbish for faces compared to 14B
  - *From: AJO*

- **System memory OOM with large workflows**
  - Native ComfyUI struggles with LoRA + 720p x 81f workflows causing system memory crashes
  - *From: Doctor Shotgun*

- **ComfyUI cache management**
  - ComfyUI wasn't designed for video generation, stores every frame as fp32 tensor eating memory
  - *From: Kijai*

- **Frame count limited to 81 for 14B model**
  - Going above causes ping-pong or looping effects
  - *From: aikitoria*

- **High resolution generation issues**
  - Higher resolutions like 1600x944 produce poor motion quality, not well trained for high res
  - *From: Kijai*

- **LightX2V lora compatibility**
  - Current lora not properly trained for 2.2, causes color shifts and reduced prompt adherence
  - *From: aikitoria*

- **RAM requirements for dual model setup**
  - Need significant RAM to hold both high and low noise models simultaneously
  - *From: Mngbg*

- **Wan 2.2 no vid2vid workflow yet**
  - Only i2v workflows available currently
  - *From: Kijai*

- **5B model has terrible movement compared to 14B**
  - Image quality isn't terrible but motion is limited
  - *From: Kijai*

- **Multiple image input doesn't work usefully with 5B**
  - Doesn't seem trained to understand multiple image inputs
  - *From: Kijai*

- **Old LoRAs don't fully work with Wan 2.2**
  - Work somewhat with low noise model, weak on high noise model
  - *From: Kijai*

- **LightX2V needs retraining for Wan 2.2**
  - Original LightX2V was good with 2.1 but needs retraining to be good with 2.2
  - *From: aikitoria*

- **5B model has poor T2V performance**
  - Faces are wonky, overall quality issues compared to 14B
  - *From: DiXiao*

- **VACE doesn't work yet**
  - Still experimental, user reports issues
  - *From: Daflon*

- **Above 81 frames is risky**
  - Similar to 2.1, can cause looping issues
  - *From: Daflon*

- **No proper LoRA for 5B model yet**
  - No LightX, no PUSA LoRA available
  - *From: thaakeno*

- **Wan 2.1 14B model struggles on 8GB VRAM cards**
  - Requires GGUF quantization or smaller models for low VRAM setups
  - *From: xwsswwx*

- **Tiny VAE doesn't work with 5B model**
  - Only compatible with 14B models
  - *From: Kijai*

- **VACE had poor results with 13B model**
  - Works better with 14B model, performance depends on model size
  - *From: xwsswwx*

- **Framepack training data mostly portrait videos**
  - Results tend toward dance/Instagram style monotone videos
  - *From: yi*

- **End of video artifacts in I2V**
  - Sometimes shows overlaid videos or disappearing objects with faster motion
  - *From: phazei*

- **Context windows only work properly with MAGREF**
  - Other models don't handle context switching as well
  - *From: Kijai*

- **LightX2V kills motion quality**
  - Vanilla without lightx will always be very slow but has better motion
  - *From: Juan Gea*

- **VACE doesn't handle reference images very well**
  - Not dedicated to wan 2.2, but video control and FFLF work well with tweaking
  - *From: JmySff*

- **Quality impact too big on radial attention for high noise model**
  - Be careful with radial on the high noise model, but fine on low noise side
  - *From: Kijai*

- **FP4 quality is terrible**
  - Not worth using despite speed benefits
  - *From: Kijai*

- **Distill loras on I2V lose some 2.2 motion quality**
  - I2V with lightxv2 lora feels more like wan 2.1, missing some interesting motion that 2.2 adds
  - *From: gokuvonlange*

- **Some loras work on low but not high noise model**
  - Low alone produces results very similar to 2.1 with better quality, but some loras affect high not in intended way
  - *From: Ant*

- **Slowmo tendency with certain lora combinations**
  - If WAN decides it will be slowmo, it will be slowmo - difficult to control
  - *From: N0NSens*

- **Longer video lengths produce washed look and repetitive motion**
  - User reported issues with longer generation lengths
  - *From: gokuvonlange*

- **Object clipping through surfaces**
  - 2.2 does clipping frequently, possibly from over-training on video game engine physics
  - *From: QuintForms*

- **VACE not designed for 2.2**
  - Especially problematic with reference images, though OpenPose and Depth work well for vid2vid
  - *From: JmySff*

- **All-in-one merge loses 2.2 capabilities**
  - Merged model performs like 2.1, loses complex prompt understanding
  - *From: slmonker(5090D 32GB)*

- **Context windows difficult with T2V**
  - Every window has same prompt so naturally creates similar starting points instead of continuation. Overlap often not enough to fix this
  - *From: Kijai*

- **Context windows don't work well for I2V**
  - Only works if subject doesn't move out of frame, like dancing or multitalk scenarios
  - *From: Kijai*

- **5B model motion limitations**
  - Should stick to low-motion only, motion quality not close to 2.2 14B category
  - *From: QuintForms*

- **Distill LoRA reduces variance**
  - The distill LoRA kills a lot of variance in outputs
  - *From: seitanism*

- **5B model poor performance at low resolutions**
  - Quality issues with anything below 832x480, worse than 1.3B model
  - *From: homem desgraca*

- **LightX2V reduces prompt adherence on high noise model**
  - Raw model picks up complex prompts better than distilled version
  - *From: gokuvonlange*

- **No context window support through dual samplers**
  - Cannot use rolling context with 2.2's two-stage sampling
  - *From: Cubey*

- **Consolidated model severely degraded quality**
  - Quality drops to HunyuanVideo level, not recommended
  - *From: gokuvonlange*

- **5B model has poor face quality except in closeups**
  - Faces generally look bad unless in close-up shots
  - *From: TK_999*

- **GGUF is 20% slower due to dequantization**
  - Has to dequantize on the fly during processing
  - *From: Kijai*

- **5B model produces weird faces and motion**
  - Known issues with 5B model requiring optimization
  - *From: Lodis*

- **Wan 2.2 model not optimized for longer than 5-8 seconds**
  - Longer durations can have quality issues
  - *From: thaakeno*

- **System RAM OOM issues with batch processing**
  - Python and ComfyUI don't release RAM properly
  - *From: mdkb*

- **WAN 2.2 not optimized for videos longer than 81 frames**
  - Causes looping and repetitive motion patterns, clear training limitation
  - *From: Kijai*

- **Vid2vid cannot do targeted changes without masking**
  - Cannot selectively modify specific elements while keeping others identical
  - *From: Kijai*

- **Color changes difficult in vid2vid**
  - Would need manual recoloring or filtering before encoding
  - *From: Kijai*

- **LoRAs from 2.1 work weaker on 2.2**
  - Cross-model compatibility reduces effectiveness
  - *From: Draken*

- **Prompt bleeding between hair and body**
  - Difficult to control different motion for different body parts
  - *From: seitanism*

- **121 frames doesn't work well on 14B model**
  - Causes memory issues and poor results, stick to shorter frame counts
  - *From: N0NSens*

- **Color changes difficult in V2V**
  - Changing colors without changing everything else is tough, may need to start earlier in denoising process
  - *From: Kijai*

- **First frames look weird when interpolating over 81 frames**
  - Going over 81 frames with interpolation causes first frame artifacts
  - *From: blird*

- **EchoShot method inconsistent**
  - Works well for some prompts (like panda) but fails on others where scene doesn't change
  - *From: Kijai*

- **Context windows don't work well with I2V**
  - Image is continuously reinforced per window causing looping issues. Better to use VACE extension or MAGREF
  - *From: DawnII*

- **Speed LoRAs reduce model quality**
  - Using LightX and other speed LoRAs makes output feel more like WAN 2.1.5, loses the quality that makes 2.2 special
  - *From: gokuvonlange*

- **Model worse at very high resolutions**
  - High resolution generations don't work as well, better to generate at lower res and upscale
  - *From: Kijai*

- **I2V upscaling loses initial image details**
  - When doing latent upscale for I2V, loses details from input image, needs full decode/re-encode workflow
  - *From: gokuvonlange*

- **5B model has poor face quality**
  - 5B destroys faces in training up to 4000 steps, faces are destroyed in both T2V and I2V
  - *From: Drommer-Kille*

- **Object permanence issues in 5B**
  - Very bad object permanence - cups turn into lemons, bullets explode but are still there after exploding
  - *From: seitanism*

- **Slowmo effect persists**
  - Still having slowmo problem that can't be solved, though 24fps looks less slow than 16fps
  - *From: Juampab12*

- **LightX2V constraints motion distribution**
  - For complex prompts with 3-4 animated elements, lightxv2 lora constraints motion distribution across seeds while full model handles it better
  - *From: gokuvonlange*

- **VACE only works with T2V models**
  - I2V loras don't work properly with VACE, causing bland/robotic motion
  - *From: lostintranslation*

- **LightX causes motion blur loss**
  - Makes every frame super sharp like high shutter speed, looks like stop motion
  - *From: Ruairi Robinson*

- **2.1 loras poor compatibility with 2.2**
  - Bring noise and significant quality loss, especially at 720p
  - *From: lovis.io*

- **Higher resolution causes quality degradation**
  - Upscaling from 832x480 to 1280x720 results in faded, low movement, bad quality
  - *From: 🐝 bumblebee 🐝*

- **Multitalk doesn't work with high noise model**
  - Only works with low noise model, couldn't get more than one syllable on high model
  - *From: Kijai*

- **2.2 completely censored violence**
  - Unable to get a single punch, slap or any violence at all, unlike previous versions
  - *From: Juampab12*

- **VACE not great with 2.2**
  - Haven't seen a reason to use 2.2 with VACE over 2.1
  - *From: Kijai*

- **LoRAs don't work well with high noise**
  - High noise model has issues with LoRA compatibility
  - *From: Juampab12*


## Hardware Requirements

- **GPU cooling critical for performance**
  - RTX 5090 with liquid cooling running at 25C enables max clock speed all the time, much faster than cloud GPUs. Thermal throttling at 90C causes major slowdowns
  - *From: VRGameDevGirl84(RTX 5090)*

- **RTX 4090 generation times**
  - 5-second clip upscaling from 512x512 to 1024x1024 should take about 1 minute, not hours if properly configured
  - *From: VRGameDevGirl84(RTX 5090)*

- **GPU temperature monitoring**
  - Normal temps: RTX 4090 idles at 40C, reaches 70C when generating videos. 25C indicates possible driver bug or exceptional cooling
  - *From: zoz*

- **RTX 3090 memory usage**
  - 40 blocks swap needed at 960x480 on fp16/fp8_e5m, 200sec/it vs 20sec/it when swapping
  - *From: ˗ˏˋ⚡ˎˊ-*

- **MultiTalk memory usage**
  - Fits on 24GB without offloading for decode, barely fits and offloading slows it down significantly
  - *From: Kijai*

- **OmniAvatar VRAM**
  - Claims 40GB but can run with about 20GB
  - *From: Tango Adorbo*

- **SAGEATT 1 compatibility**
  - Only version that supports RTX 2060 and older GPUs
  - *From: hicho*

- **LightX2V speed improvement**
  - 110 seconds on RTX 4090 for 4-step generation
  - *From: zoz*

- **Radial + Sage + SVDQuant performance**
  - 30 seconds for 1280*720*81 frame videos on appropriate hardware
  - *From: yi*

- **MultiTalk frame capacity**
  - Able to get 420 frames at 30fps (14 seconds) maximum tested
  - *From: voxJT*

- **RTX 3060 limitations**
  - Maximum 81 frames, considering multi-GPU setup for expansion
  - *From: mdkb*

- **RTX 4090 OOM with multiple LoRAs**
  - Even 4090 can OOM with many LoRAs loaded without proper memory management
  - *From: humangirltotally*

- **RTX 3080 12GB low memory workflow**
  - Works with low_vram_load and proper offloading settings
  - *From: garbus*

- **RTX 5090 T2V performance**
  - 26-39 seconds for WAN T2V image generation at 4 steps
  - *From: VRGameDevGirl84(RTX 5090)*

- **RTX 2060 6GB VACE**
  - OOM on single 720p image with VACE
  - *From: hicho*

- **Skyreels memory usage**
  - 81 frames at 1024x576 with 4 steps: Max allocated 17.879 GB, Max reserved 18.469 GB, 89.60 seconds
  - *From: VRGameDevGirl84(RTX 5090)*

- **1.3B model performance**
  - 25 steps took 17 seconds for single frame generation
  - *From: VRGameDevGirl84(RTX 5090)*

- **GPU temperature monitoring**
  - Doesn't exceed 60C when sampling with proper driver updates
  - *From: VRGameDevGirl84(RTX 5090)*

- **MultiTalk VRAM needs**
  - Requires more than 8GB VRAM, full block swap with 32GB RAM probably won't work
  - *From: Kijai*

- **Upscaling 81+ frames**
  - v2v upscaled from 1280x720 to 1920x1072. 40 block swapped, 11 mins... does anyone know a reliable method to upscale more than 81 frames?
  - *From: Atlas*

- **RTX 3090 VRAM capacity**
  - Can handle 33 frames at 720x1280 for 14B i2v model
  - *From: Rainsmellsnice*

- **Omni-Avatar 1.3B VRAM**
  - Works on 8GB VRAM according to GitHub examples
  - *From: mdkb*

- **Sky reels A2 model size**
  - Model itself is 16GB, user has 24GB VRAM to work with
  - *From: Rainsmellsnice*

- **VRAM optimization with distorch**
  - Can put 14GB in RAM to avoid OOMs on 12GB card
  - *From: mdkb*

- **RTX 4080 for MultiTalk vid2vid**
  - Card used for MultiTalk workflow testing
  - *From: N0NSens*

- **Basic T2V generation**
  - 4090: 832x480x81 frames in 4 steps takes ~23 seconds using distill lora
  - *From: Kijai*

- **Long video generation**
  - 512x832, 997 frames, 5 steps: Max allocated 18.602GB VRAM, total time 11:29
  - *From: Kijai*

- **VACE memory usage**
  - Draw Things: 26GB RAM for 8 second video vs ComfyUI: 110GB for similar content
  - *From: Todd*

- **Full HD video generation**
  - Used 75% VRAM on unspecified GPU for 1920x1072, 49 frames at 6 steps, very slow performance
  - *From: David Snow*

- **MultiTalk long form**
  - 35 seconds at 576x1024 using A6000 48GB VRAM and 128GB system RAM
  - *From: samhodge*

- **GGUF virtual VRAM**
  - Set 14GB virtual on 12GB card, prevents OOMs when using Distorch loaders
  - *From: mdkb*

- **High resolution video**
  - 1280x1920 video with 25 frames possible on 4090, requires trained LoRA at that resolution
  - *From: Persoon*

- **VRAM for Full HD generation**
  - Can't do full 81 frames at 1920x832 with 24GB VRAM, sweet spot around 1600 pixels
  - *From: David Snow*

- **MAGREF 14B model size**
  - 18GB model, won't work on 8GB cards, 6GB Q2 versions available but quality questionable
  - *From: David Snow*

- **LoRA training on 12GB**
  - Possible to train LoRA on 12GB in 4 hours using WSL2 Ubuntu with Wan 2.1 T2V 1.3B
  - *From: mdkb*

- **24GB VRAM for 1280x720x81 frames**
  - Should fit in fp8 easy with maybe 30 blocks, without multitalk around 20 swapped is generally enough
  - *From: Kijai*

- **E5m2 quantization for AMD GPUs**
  - Required for torch.compile to work on AMD GPUs, similar to 3xxx series nvidia cards
  - *From: patientx*

- **Full block swap needed for 720p MultiTalk**
  - MultiTalk increases VRAM use, need a lot of block swap to do 720p
  - *From: Kijai*

- **4060ti 16GB with wrapper**
  - Can OOM at 33 frames 480p, needs non-blocking disabled. 1280x720x81 should fit under 16GB with block swap
  - *From: Kijai*

- **LoRA loading on 16GB VRAM**
  - Model loader goes above 16GB when using LoRAs like LightX2V, requires low_mem_load option
  - *From: Cseti*

- **4090 OOM at 720x1280**
  - Can OOM with 6 seconds at 720x1280 resolution
  - *From: Siraj*

- **VRAM for e5m2 models**
  - e5m2 models won't fit on 3060 12GB VRAM, need models under 12GB
  - *From: mdkb*

- **GGUF models for low VRAM**
  - Q8 GGUF models provide excellent quality while using less VRAM than fp8
  - *From: David Snow*

- **CUDA compatibility**
  - Some torch compile issues with specific GPU configurations, may need dimension adjustments
  - *From: Kijai*

- **GGUF vs native memory usage**
  - GGUF versions below Q8 use lower VRAM than fp8, but are 20% slower
  - *From: Kijai*

- **VACE generation time**
  - 5 minutes for 1024x576 4-5 seconds of video
  - *From: MysteryShack*

- **MultiTalk context workflow VRAM**
  - 32GB VRAM still causes OOM at longer durations (90+ seconds)
  - *From: AJO*

- **Mac Studio M3 Ultra performance**
  - 10 minutes for 8 step 1024x512 moderate frames, memory spikes to 110GB
  - *From: Todd*

- **DrawThings Mac efficiency**
  - 30% faster than MLX, never exceeds 26GB memory usage
  - *From: Todd*

- **GGUF model quantization**
  - Q4 slower on consumer GPUs, Q8 and Q5 work well
  - *From: mdkb*

- **VRAM for 1080p 81 frames**
  - Really pushing it even for 24GB systems, 3060 12GB can do 21 frames at 1080p max
  - *From: mdkb*

- **Full HD upscaling on 4090**
  - 73% VRAM usage for full HD 81 frames, generation takes ~15 minutes unoptimized, ~7 minutes optimized
  - *From: David Snow*

- **2060 6GB limitations**
  - Can only do 512x81 frames, endless loop if exceeding VRAM
  - *From: hicho*

- **3060 12GB VRAM capabilities**
  - Can do 1600x900x49 frames in 20 mins, or 1080px41 frames in 40 mins using GGUF and optimizations
  - *From: mdkb*

- **VRAM management with torch.compile**
  - Using sageattention increases memory use over sdpa when using torch.compile, if/else statements increase memory even if never reached
  - *From: Kijai*

- **Memory optimization techniques**
  - Use smallest acceptable model, DisTorch/block swap for VRAM management, offload VAE and transformers
  - *From: Grimm1111*

- **SeedVR2 VRAM usage**
  - 4080 16GB can do 864x480->1152 with batch 13 max, 1024x576->1152 requires batch 1, causes OOM easily
  - *From: CaptHook*

- **Character LoRA training on 3090**
  - 20 images at 512x512 took almost 20 hours for 35 epochs, but converged much earlier
  - *From: Dream Making*

- **Wan LoRA training**
  - 10 images, 256x256, 1.3B T2V model takes 4 hours on 12GB VRAM
  - *From: mdkb*

- **GGUF memory optimization**
  - Enables running larger models on systems with limited VRAM/RAM, significant improvement for constrained systems
  - *From: Multiple users*

- **VRAM optimization with chunked RoPE**
  - Chunked RoPE drastically reduces VRAM use when not using torch.compile, saves 1GB+ in some cases
  - *From: Kijai*

- **5090 performance gains**
  - 60-80% faster than 4090 with additional VRAM benefits
  - *From: A.I.Warper*

- **14B model chunking benefits**
  - Considerable VRAM gains when not using torch.compile, peak is sageattention so chunking whole attention gets complicated
  - *From: Kijai*

- **PCIe lanes for GPUs**
  - x1 PCIe is too slow for 5090, x8 PCIe v5 has no impact compared to v4 x8 or v3 x8
  - *From: hicho*

- **Kijai's GPU setup**
  - MSI GeForce RTX 5090 GAMING TRIO OC 32 GB, runs OC but at lower settings
  - *From: Kijai*

- **VRAM limit for frame generation**
  - 41 frames maximum at 1600x900 resolution before running out of memory
  - *From: mdkb*

- **VRAM for Wan 2.1**
  - 8GB card can run with Q8_0 quantization
  - *From: xwsswww*

- **VRAM for full Anisora**
  - 70GB VRAM needed for full model
  - *From: Rainsmellsnice*

- **Memory usage with Pusa**
  - 9.2GB temporary modulation variables per block for 1280x720x81 video
  - *From: spacepxl*

- **System RAM optimization**
  - --cache-none flag helps with RAM consumption
  - *From: Gateway {Dreaming Computers}*

- **GPU compatibility**
  - RTX 20 series doesn't support SageAttention and Triton
  - *From: hicho*

- **Model merging memory usage**
  - Running merged models (17GB + 14GB) requires significant VRAM and RAM
  - *From: hicho*

- **Generation time with I2V LoRA**
  - ~35 seconds per generation on 4090 with 4 steps, 1 CFG
  - *From: Ada*

- **Virtual memory for FP8 conversion**
  - 90 GB virtual memory needed to convert models to FP8
  - *From: hicho*

- **System RAM usage**
  - ComfyUI node cache uses significant system RAM, can be disabled via command line
  - *From: Gateway {Dreaming Computers}*

- **GGUF enables 14B on 8GB**
  - Someone running 14B model on 8GB VRAM using GGUF format
  - *From: Draken*

- **System RAM for low VRAM setups**
  - With wrapper low_vram lora loading is rough on system RAM, but 64GB RAM + 2060 6GB can use VACE and T2V Q8 with blockswap
  - *From: hicho*

- **NVME vs SATA for AI models**
  - NVME recommended over SATA SSD for AI model storage
  - *From: hicho*

- **VACE memory usage**
  - User with 16GB VRAM/64GB RAM can do 1024x576/121f in 2m30s but VACE causes OOM even with block swap
  - *From: N0NSens*

- **GGUF quantization levels**
  - Q4_K_S works on A4500 with 20GB VRAM, Q8 provides better quality, Q6 may still cause OOM on some systems
  - *From: The Shadow (NYC)*

- **VACE with LoRAs memory impact**
  - LoRAs significantly increase memory usage with VACE, couldn't load even one LoRA with fp8 on A4500 system
  - *From: The Shadow (NYC)*

- **Pusa lora size**
  - 4.9GB rank512 lora file
  - *From: gokuvonlange*

- **VRAM for VACE**
  - 16GB VRAM user getting OOM with VACE workflow
  - *From: jab*

- **WAN 1.3B on 8GB VRAM**
  - Easily possible with GGUF and blockswap
  - *From: Kijai*

- **WAN 14B on 8GB VRAM**
  - Possible with 32GB RAM using Q4 GGUF models and aggressive blockswap
  - *From: Kijai*

- **ComfyUI performance**
  - SSD strongly recommended, loads in 40-50 seconds vs 3-4 minutes on HDD
  - *From: AmirKerr*

- **Q4KM GGUF performance**
  - T2V 1600x900, 41 frames in 20 minutes on 12GB VRAM setup
  - *From: mdkb*

- **8GB VRAM needs block swapping**
  - Without block swapping, generation is not viable on 8GB cards
  - *From: AmirKerr, Kijai*

- **RTX 6000 Pro performance vs RTX 3090 Ti**
  - 96GB VRAM, 6x faster than RTX 3090 Ti, minimal quality difference, costs $2/hour on RunPod
  - *From: Valle*

- **Wan 14B model memory usage**
  - Max allocated: 13.397 GB, Max reserved: 16.844 GB with fp8 and 20 blocks swapped
  - *From: Kijai*

- **4090 VRAM limits**
  - Can do fp8 at certain resolutions, max reserved up to 23.9GB without monitor
  - *From: ZeusZeus, Kijai*

- **Model file size**
  - wan2.1_t2v_14B_bf16.safetensors is 28GB
  - *From: Valle*

- **RTX 5090 performance**
  - 81 frames at 1024x1024 with 4 steps in 1:10 (17.51s/it) with GGUF model, 50% speed boost with radial attention
  - *From: Kijai*

- **3060 12GB multitalk performance**
  - 832x480 x 81 frames in 8-13 minutes, only using 4GB VRAM with proper settings
  - *From: mdkb*

- **System RAM usage increase**
  - FP8 models now using 50GB+ system RAM, up from previous 16-17GB usage
  - *From: Draken*

- **A4500 20GB VRAM capability**
  - Can run base models but OOMs with LoRAs, resolved by model merging approach
  - *From: The Shadow (NYC)*

- **VRAM usage with GGUF quantization**
  - Q3: 200MB per block, FP8: 425MB per block. Swapping 20 blocks difference becomes 4GB
  - *From: Kijai*

- **High resolution processing**
  - 1080p video is huge, 1920x1152 with 93 frames causes VAE OOM, needs tiled VAE
  - *From: Juan Gea/Kijai*

- **Radial attention works with RTX 2060**
  - Successfully tested with Sage1 model
  - *From: hicho*

- **PUSA LoRA VRAM usage**
  - 512 rank PUSA is around 5GB which eats a lot of VRAM
  - *From: Elvaxorn*

- **Radial Sage Attention performance scaling**
  - Higher the resolution, more you gain in speed. Should work on 3080
  - *From: Kijai*

- **1280x768 generation timing**
  - 1024x512 6 steps 49 length in 51 seconds using 64 block size, 1280x768 5 steps 49 frames in 89 seconds
  - *From: MatiaHeron*

- **32GB RAM bottleneck for RTX 4090**
  - 32GB RAM causes bottleneck, need to reduce resolution and frame count
  - *From: hicho*

- **WAN 14B VRAM/RAM usage**
  - With optimizations: 96% VRAM and 92% RAM usage at 480x640 51 frames on RTX 4090
  - *From: mborgo*

- **L40S optimal settings**
  - 48GB VRAM + 64GB system RAM can run highest quality with fp16 models
  - *From: The Shadow (NYC)*

- **SeedVR2 resource requirements**
  - Very resource heavy even on RTX 5090
  - *From: orabazes*

- **1.3B model efficiency**
  - Fits 96 frames at 1080p with only 71% RAM usage on 24GB system
  - *From: Juan Gea*

- **VRAM for different models**
  - Wan2GP supports as low as 6GB VRAM, 720p model uses 74% of VRAM for 121 frames on adequate hardware
  - *From: JohnDopamine*

- **Python version compatibility**
  - Python 3.12 recommended, works with current ComfyUI portable
  - *From: Kijai*

- **Triton and SageAttention**
  - Sage can be 2x+ faster at higher resolutions, SageAttention2 slightly faster than v1
  - *From: Kijai*

- **48GB VRAM setup**
  - Can run 81,4,16 context with VACE, Multitalking and T2V 14B using 40 blocks swapped and 15 VACE blocks swapped with 128GB system RAM
  - *From: samhodge*

- **Unmerged LoRA memory usage**
  - Expanded timesteps take more memory when using PUSA scheduler with unmerged LoRAs
  - *From: Kijai*

- **16GB VRAM capability**
  - Can run Wan video on 16GB VRAM, difference vs 24GB is gen speed and higher resolution flexibility
  - *From: DawnII*

- **RTX 5090 temperatures**
  - Running at 80-83°C with VRAM maxed during video generation, ~30-40% faster than 4090
  - *From: avillabon*

- **High VRAM for quality**
  - 192GB cards joked about, 48GB mentioned as available for high resolution (1280x720) work
  - *From: samhodge*

- **FP8 performance**
  - FP8 scaled matmul on 4090 around 30% faster than fp16, fp16 with allow_fp16_accumulation 20% faster than normal fp16
  - *From: Kijai*

- **14B model VRAM usage**
  - 14B model uses ~15GB in fp8, text encoder ~6.5GB, leaving little VRAM headroom
  - *From: Kijai*

- **Q6 GGUF 1-frame generation**
  - Should be possible on 12GB VRAM, with block swap even 1024x resolution possible at 20-25GB
  - *From: patientx*

- **High resolution desktop impact**
  - Windows desktop can consume significant VRAM with high resolution monitors
  - *From: Hedge*

- **Non-blocking mode RAM requirements**
  - Requires sufficient system RAM as it pins memory - doesn't work well with very low system RAM
  - *From: Draken*

- **Text cache storage**
  - 8MB per cached prompt at bf16 precision, stored in custom_nodes/ComfyUI-WanVideoWrapper/text_embed_cache
  - *From: Kijai*

- **VRAM savings with comfy chunked**
  - Up to 1GB less VRAM usage compared to old comfy scheduler option
  - *From: hicho*

- **Long model loading times**
  - I2V-14B-480p_fp8_e4m3fn taking 10+ minutes to load on 3090 24GB VRAM with 128GB RAM
  - *From: sneako1234*

- **Context windows VRAM usage**
  - Same as 81 frames regardless of total length, uses more RAM for image storage
  - *From: Kijai*

- **1920x1080 at 81 frames**
  - Possible with 48GB VRAM (A6000) and 128GB system RAM
  - *From: Gateway {Dreaming Computers}*

- **512x65 frames on 6GB VRAM**
  - Possible with KJ wrapper optimizations on RTX 2060
  - *From: hicho*

- **Block swap node RAM usage**
  - Can use 109GB RAM but enables generation on lower VRAM GPUs
  - *From: Drommer-Kille*

- **720p generation time**
  - 720p video took 10 minutes to generate (specific hardware not mentioned)
  - *From: Drommer-Kille*

- **3090 capability**
  - Single 3090 has enough power to drive ComfyUI, can do full HD though render times are slow
  - *From: OftenBen*

- **4090 OOM issues**
  - 4090 user reports never reaching 1080p due to out of memory errors
  - *From: Juan Gea*

- **Scaled models and low VRAM**
  - Scaled models only work with unmerged LoRAs, and unmerged + low VRAM mode doesn't work
  - *From: Kijai*

- **High resolution generation**
  - 1080p (1920x1152) works without accelerators but takes 45 minutes for 2 seconds, limited to 26 frames max
  - *From: Juan Gea*

- **Skyreels V2 compute**
  - Requires 50% more compute than Wan 2.1 due to higher frame count (73 vs 49 frames for 3 second clip)
  - *From: yi*

- **FastWan 1.3B VRAM usage**
  - 1280x768x81 frames uses ~20% RAM, 1920x1152x81 frames ~30% RAM on RTX 4090
  - *From: Juan Gea*

- **PUSA high resolution VRAM**
  - 1920x1152 with 40 block swap uses 98% VRAM with everything offloaded on RTX 4090
  - *From: Juan Gea*

- **SageAttention 2 VRAM increase**
  - Uses more VRAM than SageAttention 1 and slightly more than sdpa+torch.compile
  - *From: Kijai*

- **Performance comparison**
  - PUSA workflow: 70s/it vs previous lightx2v workflow: 20s/it
  - *From: Drommer-Kille*

- **RAM usage with LoRA backups**
  - Key backup system can use 20GB+ RAM, removing it frees significant memory
  - *From: Kijai*

- **System RAM recommendations**
  - 96GB RAM may not be enough for some workflows, get as much as affordable
  - *From: Thom293*

- **Memory pooling on dual 5090s unclear**
  - Uncertainty about how to pool memory across multiple 5090 GPUs
  - *From: samhodge*

- **48GB card mentioned**
  - Reference to using 48GB GPU for testing workflows
  - *From: samhodge*

- **Twin 5090s needed for full bf16/fp16**
  - Only would use full precision with dual 5090 setup
  - *From: MysteryShack*

- **SageAttention 3 VRAM usage**
  - 1280x720x81 frames uses 30GB with sage2, needs 20 block swap with sage3 to achieve same memory usage. At 832x480: sage3 uses 17.7GB max vs sage2 15.9GB max
  - *From: Kijai*

- **RTX 50 series requirement**
  - SageAttention 3 only works on RTX 5000 series GPUs
  - *From: Kijai*

- **Wan 720p 81 frames VRAM**
  - Around 25GB VRAM for 720p 81 frames, potentially 28GB
  - *From: Kijai*

- **Wan 2.2 30fps VRAM**
  - Double VRAM usage compared to 2.1 due to 160+ frames vs 81 frames
  - *From: Kijai*

- **Ampere GPU torch compile**
  - A6000 and 3090 need fp8 e5m2 for torch compile to work
  - *From: Kijai*

- **VSA kernel hardware**
  - VSA kernel appears to only work on H100 GPUs
  - *From: Kijai*

- **EchoShot generation speed**
  - 149 frames took 2 minutes 14 seconds on RTX 5080
  - *From: VK*

- **Fast generation with combined LoRAs**
  - FastWAN + LightX + FusionX: 57 seconds for 2 steps on RTX 5090
  - *From: VRGameDevGirl84*

- **V2V generation performance**
  - 12 second V2V video generated in 130 seconds with RTX 5090
  - *From: Drommer-Kille*

- **RAM limitations for AI**
  - 32GB RAM feels unusable for AI stuff, at least for blockswapping
  - *From: VK*

- **VRAM usage for 81 frames at 1280x720**
  - 30GB VRAM usage, 26-28GB with torch.compile
  - *From: Gateway*

- **5090 OOM at VAE decode with long sequences**
  - 20 seconds (320 frames) too long even with 128GB RAM
  - *From: Drommer-Kille*

- **Secondary GPU for display saves 2GB VRAM**
  - Windows uses ~2GB, Linux ~1GB on primary GPU for display
  - *From: Juan Gea*

- **1080 with 12GB VRAM for swapping**
  - Not worth it - same or worse performance than 12GB more RAM
  - *From: Kijai*

- **273 frames at 832x480**
  - Uses 19GB max on RTX 4090 with 4 steps
  - *From: Kijai*

- **270 frames generation**
  - Possible on RTX 5090, takes 240 seconds
  - *From: Drommer-Kille*

- **VRAM optimization**
  - Native TE on CPU frees 11GB VRAM
  - *From: hicho*

- **VRAM usage optimization**
  - With full block swap at 1400 resolution, user reported using most of 16GB VRAM. RAM becomes limiting factor with smaller VRAM cards
  - *From: VK (5080 128gb)*

- **T5 encoder VRAM usage**
  - 11GB umt5 model can be run on 6GB VRAM using proper offloading and block swap
  - *From: hicho*

- **System VRAM overhead**
  - Windows 11 takes 500MB VRAM, browsers take 40-100MB+ depending on hardware acceleration settings
  - *From: hicho*

- **Resolution limits with VRAM**
  - 113 frames can go up to 1136x656 before OOM, close to 1280x720
  - *From: Drommer-Kille*

- **RAM usage for A14B model**
  - Will use more RAM as both high/low noise models need to be loaded unless disk offloading implemented
  - *From: Kijai*

- **CPU performance for T5**
  - AMD Ryzen 9 9900X achieves 7-9 it/s for T5 encoding
  - *From: Kijai*

- **VRAM usage increase expected**
  - 2.2 VAE is 1.3GB in bf16, significantly larger than previous versions
  - *From: Kijai*

- **High-end hardware likely needed**
  - Speculation that offline usage requires 200K investment in kit, otherwise cloud credits needed
  - *From: samhodge*

- **VRAM usage**
  - 31GB VRAM for VAE decode, TI2V model runs at 1280x704
  - *From: Gateway*

- **Generation time**
  - 75 seconds from cold start, 155 seconds for longer sequences, 8 minutes on RTX 5090 for default workflow
  - *From: AJO*

- **14B model compatibility**
  - 14B runs on RTX 4090 (24GB VRAM) but may be slower due to model swapping
  - *From: multiple users*

- **5B model VRAM**
  - Doesn't fit in 8GB VRAM (RTX 3080/4060Ti class)
  - *From: Blitz*

- **14B model VRAM**
  - Requires 2GB more VRAM than Wan 2.1 14B
  - *From: thaakeno*

- **5B generation time**
  - L4 GPU: 75% completion in ~4 minutes for 81 frames 720p
  - *From: Draken*

- **14B generation time**
  - 4090: 20 steps in 03:34 (10.74s/it) for i2v
  - *From: Janosch Simon*

- **Long generation times**
  - 1280x704 121 frames takes 35 minutes on 5090
  - *From: slmonker*

- **14B model VRAM usage**
  - Around 56GB total for both high and low models, requires offloading to system RAM on 24GB cards
  - *From: Purz*

- **5B model performance**
  - 8GB VRAM, 13s/it on unspecified hardware
  - *From: Blitz*

- **4090 performance with 14B I2V**
  - 78-172 seconds for generation depending on settings and workflow
  - *From: JohnDopamine*

- **3090 can run 14B T2V**
  - Confirmed working on 3090, though with longer generation times
  - *From: crinklypaper*

- **Fp16 models fit in 32GB VRAM**
  - 720p resolution, 81 frames confirmed to fit
  - *From: Shawneau 🍁 [CA]*

- **5B model VRAM**
  - Fits in 16GB VRAM when loaded in fp8
  - *From: Mikerhinos*

- **Generation speed**
  - 14B 2.1 is much faster than 2.2, 232 seconds for 4-step generation
  - *From: A.I.Warper*

- **Memory usage**
  - Can generate 1280x768x81 frames on 4090 without issues
  - *From: Juan Gea*

- **VRAM usage for WAN 2.2**
  - 29GB VRAM for 1280x704 on 5090, 83% usage for 1024x576 on 4090
  - *From: cyncratic*

- **Generation times**
  - 172s per step full quality, 68s per step with LightX2V on 4090 at 1280x720
  - *From: Juan Gea*

- **3090 performance**
  - 1 hour for 10 steps at default settings, very slow
  - *From: 1274762680451989577*

- **5090 performance**
  - 20 minutes for full workflow, 6 minutes with optimized settings
  - *From: VRGameDevGirl84*

- **VRAM for 14B FP16**
  - RTX 4090 24GB can run 14B at FP16, takes 8-9 minutes for generation
  - *From: makeitrad*

- **System RAM for stability**
  - 128GB system RAM recommended over 64GB to avoid OOM issues and ComfyUI freezing
  - *From: makeitrad*

- **5090 generation times**
  - RTX 5090: ~94 seconds for 81 frames at 1024x576 16fps, ~143 seconds for 10 steps with FusionX
  - *From: VRGameDevGirl84*

- **4090 generation times**
  - RTX 4090: ~7 minutes for 121 frames 24fps with LightX lora, 44 minutes for 81 frames base 14B no loras
  - *From: makeitrad*

- **VRAM for different quantizations**
  - Q8 recommended for 8GB VRAM, Q6 minimum for quality, Q3-Q4 with offloading possible
  - *From: multiple users*

- **RAM requirements**
  - Need sufficient RAM for model offloading when VRAM is insufficient
  - *From: Kijai*

- **Performance benchmarks**
  - 80 minutes for 121 frames 1280x720 I2V on RTX 5090 reported as poor performance
  - *From: GOD_IS_A_LIE*

- **VRAM usage**
  - I2V 832x464x121 24fps takes 11:22 on 3060 12GB
  - *From: Daflon*

- **Generation time**
  - 330s on RTX 3090 for 5B fp16 workflow, maxed out VRAM
  - *From: halkony*

- **Fast generation**
  - 100s on L4 GPU using LightX2V with 3 LoRAs (LightX, Phantom, FusionX, Pusa v1)
  - *From: thaakeno*

- **Memory management**
  - Heavy on RAM when using 2 models simultaneously in wrapper
  - *From: Kijai*

- **FP8 compatibility**
  - 3090 doesn't support fp8e4nv, needs 4090+ or use e5m2 instead
  - *From: halkony*

- **14B models VRAM**
  - 12GB VRAM insufficient, requires RAM offloading with 64GB+ system RAM
  - *From: Samy*

- **T5 encoder performance**
  - bf16 very slow on older GPUs (230s vs 30s fp32), ~6 seconds on CPU
  - *From: hicho*

- **Sage attention compilation**
  - Takes very long time to compile
  - *From: aikitoria*

- **VRAM for different quantizations**
  - Q4 minimum for acceptable quality, Q6 recommended. Don't go below Q4 or quality becomes horrible
  - *From: Kijai*

- **Generation time scaling**
  - 1440x816 40 steps 121 frames takes ~28 minutes per pass on high-end hardware
  - *From: Relven 96gb*

- **Compute capability for fp8**
  - ComfyUI scaled fp8 models require compute 8.9 or higher
  - *From: MysteryShack*

- **VRAM for 14B model**
  - RTX 3060 12GB can run 14B GGUF Q5 or Q4, takes 90 seconds for 2-second video with LightX2V
  - *From: Jonathan*

- **System RAM usage**
  - 128GB RAM still experiences OOM kills, may need swap file or GGUF models to reduce memory usage
  - *From: Doctor Shotgun*

- **Multi-GPU setup**
  - 4x3090 setup generates 720p 5B video in 4.5 minutes using original code without optimizations
  - *From: intervitens*

- **Generation speed**
  - 5090 generates I2V in 100 seconds, T2V 12 steps at 768x512 in 121 seconds
  - *From: Charlie*

- **Compute capability**
  - fp8_scaled requires compute 8.9 or higher, older Ampere cards not supported for native
  - *From: MysteryShack*

- **VRAM usage for Wan 2.2**
  - 7GB per pass on Q4 GGUF, fits on 8GB GPU with smart memory management
  - *From: Blitz*

- **3090 compatibility confirmed**
  - Wan 2.2 works fine on RTX 3090 with wrapper
  - *From: ✧ฅโ๑ↀᆺↀ ๑ใฅ✧PookieNumnums*

- **Q3 quantization viable on 12GB VRAM**
  - Can run Q3 14B model with good quality on 12GB VRAM
  - *From: SonidosEnArmonía*

- **Memory usage with 2.2**
  - Memory requirements markedly higher, but can be same as 2.1 if using model swapping
  - *From: blake37*

- **VRAM for 1280x720 generation**
  - Needs VRAM Debug to clear memory between passes on 5090
  - *From: stenandrimpy*

- **Total system memory usage**
  - Running both 14B models requires 64GB RAM plus 90GB virtual memory (100GB total)
  - *From: hicho*

- **RAM usage for 2.2**
  - 2x 15GB models + ~10GB text encoder offloaded = ~40GB RAM in fp8. Total memory usage is about 100GB
  - *From: Kijai*

- **Performance benchmarks**
  - T2V 1024x576 on 3090 takes about 5 minutes, I2V 720x720 on 3090 takes ~5 minutes, 14B T2V on 4090 took 1 hour 24 mins, 240 frames with High Noise model in 155 seconds
  - *From: Multiple users*

- **VRAM requirements**
  - Can run on 6GB VRAM with proper offloading and block swap setup
  - *From: hicho*

- **RAM for fp8 models**
  - fp8 model alone 30GB, text encoder 10GB, Windows overhead - easily caps system RAM
  - *From: Kijai*

- **VRAM for Wan 2.2 14B**
  - 4090 users need 35-40 block swap for 480p 29 frames
  - *From: Sal TK FX*

- **Minimum RAM recommendation**
  - 64GB minimum, 128GB may be overkill but helps with larger models
  - *From: Elvaxorn*

- **5090 compatibility**
  - Will handle latest Wan models but requires new PSU, case, possibly motherboard
  - *From: lomerio*

- **VRAM usage increased with recent update**
  - Latest wrapper update caused models to load in fp16 instead of fp8, doubling VRAM usage and causing 4090 OOMs
  - *From: fredbliss*

- **40 blocks with 4090 gets maxed on second sampler**
  - RTX 4090 with 40 blocks reaches VRAM limit during second sampler pass
  - *From: Kenk*

- **System RAM OOM over 100GB committed**
  - Native implementation causing excessive system RAM usage with nonblocking transfers
  - *From: Doctor Shotgun*

- **RAM usage**
  - User with 128GB RAM still experiencing memory issues, 79GB RAM usage observed, 64GB users will find issues
  - *From: Doctor Shotgun*

- **Generation speed comparison**
  - 5B: 150 seconds vs 14B: 30 minutes for same generation, 3 minutes for 6 steps on 14B
  - *From: AJO*

- **VRAM management**
  - FP16 models for both low and high noise, block swapping helps with VRAM management
  - *From: Doctor Shotgun*

- **Linux vs Windows**
  - 64GB on Linux seems fine, Windows worse with RAM management than Linux
  - *From: Kijai*

- **VRAM for Wan 2.2 14B**
  - Can run on single GPU as models load one at a time, but need RAM to cache both models
  - *From: Ada*

- **RAM for dual model workflow**
  - Need sufficient RAM to hold both 30GB models, or use disk swapping which adds 5+ minutes load time
  - *From: Mngbg*

- **Performance comparison**
  - 4x 5090s expected to be ~3x faster than one RTX 6000 Pro, similar price point (~8000€ vs 8000€)
  - *From: aikitoria*

- **Wan 2.2 5B VRAM usage**
  - 13GB VRAM at fp16 with no offloading for 1024x1024x121 frames
  - *From: Kijai*

- **Wan 2.2 dual model RAM usage**
  - 14B with both models eating up 48GB RAM
  - *From: Rainsmellsnice*

- **Minimum RAM for Wan 2.2**
  - 32GB RAM users experiencing issues, need memory management solutions
  - *From: Kijai*

- **Wan 2.2 5B generation speed**
  - 1024x1024x121 frames with 30 steps took 1:40 (3.35s/it)
  - *From: Kijai*

- **16GB VRAM compatibility**
  - Can run with 64GB RAM using wrapper, may need swap file optimization
  - *From: N0NSens*

- **16GB VRAM + 32GB RAM**
  - Should work for most models
  - *From: Mngbg*

- **4060Ti 16GB + 64GB RAM**
  - Can run 14B wrapper in 365 seconds
  - *From: . Not Really Human :.*

- **RTX 3060 12GB**
  - Can run GGUF Q8_0 at 560x912x101 in 404 seconds
  - *From: Daflon*

- **24GB VRAM**
  - 5B at higher res surprisingly easy to run, 1024x1600x121 takes 12 minutes
  - *From: TK_999*

- **32GB VRAM for native fp16**
  - Can run up to 81 frames, need fp8 for 125 frames
  - *From: Shawneau 🍁 [CA]*

- **96-128GB RAM for GGUF conversion**
  - Needed for converting safetensors to GGUF
  - *From: Benjimon*

- **VRAM for Q4 vs Q8 GGUF**
  - Q4 works on 8GB cards, Q8 may need 24GB VRAM
  - *From: xwsswwx*

- **System RAM for Wan 2.2**
  - 64GB RAM recommended, 128GB allows longer videos. Uses up to 99% of 64GB RAM
  - *From: xwsswwx*

- **GPU temperature**
  - 79°C is completely fine for generation
  - *From: Kijai*

- **Memory for 250-400 frame generation**
  - 250 frames works without OOM, 400 frames may cause OOM depending on setup
  - *From: VK (5080 128gb)*

- **Generation speed with different hardware**
  - 60-70 seconds for 64 frames on 3090 with 64GB RAM
  - *From: phazei*

- **RAM impact on Wan 2.2**
  - VRAM usage same as 2.1, but RAM usage much higher
  - *From: Kijai*

- **VRAM usage**
  - V2V run used 100gb of RAM with 5090, 40 steps on i2v took 16mins on 4070
  - *From: Drommer-Kille*

- **Memory management**
  - Vanilla 14B just the high noise pass on 4090 took 41:35 for 10 steps
  - *From: Nekodificador*

- **Speed comparison**
  - With q5ks, lightx2v and fastwan loras on 3090 get same speed as wan2.1
  - *From: MiGrain*

- **VRAM usage increase**
  - 5B I2V showing 6GB higher memory usage than previous runs, around 31GB total
  - *From: orabazes*

- **14B performance**
  - 5 second 14B i2v taking 45 minutes on 4090 with default workflow at high res 121 frames
  - *From: pom*

- **Generation speeds**
  - User reporting 100-185 seconds per generation, 480 frames in 13 minutes
  - *From: Juan Gea*

- **5B model RAM usage**
  - 42GB RAM + 12GB VRAM
  - *From: Corneilious Pickleberry*

- **Generation speed on 5090**
  - 1024x576 121 frames in 115 seconds, but model loading time often exceeds generation time at 6 steps
  - *From: slmonker(5090D 32GB)*

- **Storage recommendation**
  - PCIe 5.0 SSD recommended over USB4 enclosure for faster model loading
  - *From: slmonker(5090D 32GB)*

- **RAM configuration**
  - 192GB@5200 shows no difference with DOCP on/off in ComfyUI. 4 sticks vs 2 sticks has minimal real-world impact
  - *From: cyncratic*

- **SageAttention compatibility**
  - SageAttention 2.2.0 recommended for 3090 24GB, use sageattn on auto. Version 2.1 also works
  - *From: Kijai*

- **3090 performance**
  - 10 steps, 1280x704x81 frames takes 4 minutes 52 seconds
  - *From: seitanism*

- **4090 vs 3090 performance**
  - 4090 takes 20 minutes for high-res, 3090 struggles more
  - *From: MiGrain*

- **5090 performance improvement**
  - 40% faster than 4090, better throughput
  - *From: Juampab12*

- **VRAM usage with wrapper**
  - Same VRAM as 2.1, just extra loading time between models
  - *From: MysteryShack*

- **Model loading time**
  - About 2 seconds with sufficient RAM, 30+ seconds with insufficient
  - *From: seitanism*

- **5B Q4 GGUF model VRAM**
  - 6GB VRAM but offloads a lot to RAM, making it slower
  - *From: thaakeno*

- **fp8 e5m2 model**
  - 15GB file size but works with 12GB VRAM
  - *From: mdkb*

- **SageAttention version requirements**
  - Sage v1 works from RTX 2000 series, Sage v2 requires RTX 3000 series and up
  - *From: Kijai*

- **161 frame generation**
  - Takes very long time but works without obvious looping artifacts
  - *From: aikitoria*

- **RTX 3090 compatibility**
  - Cannot use torch compile with fp8_e4m3fn weights, need GGUF, fp16, or e5m2 scaled versions
  - *From: Kijai*

- **Context options for memory management**
  - Use on both samplers if insufficient memory for full frame count
  - *From: Kijai*

- **Lower rank LoRAs**
  - Use less VRAM when unmerged, faster inference
  - *From: Kijai*

- **VRAM usage with block offloading**
  - 40 blocks offloaded uses ~21GB of 24GB available on high-end GPU
  - *From: hiroP*

- **RTX 3060 12GB performance**
  - Takes 23 minutes for 14B model generation, 13 minutes for 5B GGUF
  - *From: Abx*

- **4090 upscaling limit**
  - Can upscale to 1440x832 (5 minutes) but 1920x1088 causes OOM/lockup
  - *From: hiroP*

- **FP16 14B model**
  - Needs ~128GB RAM to run FP16 version on consumer hardware
  - *From: Kijai*

- **FP8 14B model**
  - Runs on 3090 with 64GB RAM using blockswap
  - *From: Juampab12*

- **GGUF Q4_K_M**
  - Runs on 12GB A2000 in 8 minutes for 6 steps with LightX
  - *From: tncchris.*

- **5B model memory usage**
  - 32GB RAM + 16GB VRAM for Phr00t's merge
  - *From: Mikerhinos*

- **VRAM usage for 5B model**
  - 5B model fixed VRAM usage in latest ComfyUI update. 512x33 frames works on RTX 2060. Higher resolution causes over-VRAM issues during decoding
  - *From: hicho*

- **Processing speed comparison**
  - Can process 720p video in 2 minutes, 1080p takes longer. Without CausVid, 5B is as slow as 14B with lightx
  - *From: Ryzen*

- **VRAM for different model formats**
  - GGUF allows splitting between VRAM and RAM for 12GB/16GB cards to avoid OOM. 4090 has fp8 hardware acceleration
  - *From: thaakeno*

- **RAM requirements for 2.2**
  - User needed 90GB swap file with 64GB RAM and 6GB VRAM for 2.2
  - *From: hicho*

- **Model size constraints**
  - e4m3fn v2 is 15GB, won't fit on 3090
  - *From: MiGrain*

- **Memory usage comparison**
  - 5090 generation at 1024x576: 435 seconds. 4090 with optimizations: 190s second run vs 5090 200+ seconds
  - *From: VRGameDevGirl84*

- **RAM requirements**
  - 64GB RAM systems never go higher than 80% usage, but 32GB commonly maxes out
  - *From: Charlie*

- **Model memory usage**
  - Wan 14B uses 40 blocks, 1.3B uses 30 blocks
  - *From: Ryzen*


## Community Creations

- **VRGameDevGirl84's LightX workflow** (workflow)
  - Optimized LightX2V workflow with specific lora settings achieving fusionX quality in ~75 seconds
  - *From: VRGameDevGirl84(RTX 5090)*

- **David Snow's USD upscaler workflow** (workflow)
  - One step Ultimate SD Upscaler that can be added to 14B workflows without VRAM dumping
  - *From: David Snow*

- **Mask Sampler** (custom node)
  - Combines two ksamplers and creates masks from conditional/unconditional differences
  - *From: Mads Hagbarth Damsbo*

- **Tiled sampling implementation** (fork)
  - Adds tiled sampling support to WanVideoWrapper
  - *From: stenandrimpy*

- **MultiTalk with VACE integration** (fork)
  - Modified version enabling MultiTalk to work with VACE controls
  - *From: Rudra-ai-coder*

- **LightX mix workflow** (workflow)
  - Optimal LoRA stack with good settings for fast generation
  - *From: VRGameDevGirl84(RTX 5090)*

- **Monster workflow for testing** (workflow)
  - Complex workflow for advanced VACE + MultiTalk integration
  - *From: N0NSens*

- **New Wan LoRA** (lora)
  - Custom LoRA uploaded to community
  - *From: Cseti*

- **VACE inpainting technique** (workflow)
  - Method for object removal/replacement using masks
  - *From: Nekodificador*

- **MediaSyncer** (tool)
  - Web-based media player for playing multiple videos in sync for comparing generations
  - *From: Jonathan*

- **Custom ChatGPT prompt generator** (tool)
  - Instructions for creating custom ChatGPT for WAN prompt generation with different settings for 49f vs 81f
  - *From: The Shadow (NYC)*

- **Vintage LoRA** (lora)
  - 1990s style LoRA trained on small dataset, creates dramatic style changes
  - *From: VRGameDevGirl84(RTX 5090)*

- **ComfyUI FaceParsing** (node)
  - Face parsing with selectable elements (eyes, skin, hair) for single mask output, useful for MultiTalk control
  - *From: Tango Adorbo*

- **Text-to-image Wan workflow** (workflow)
  - Optimized workflow for using Wan T2V model for single frame image generation
  - *From: VRGameDevGirl84(RTX 5090)*

- **Combined T2I + I2V workflow** (workflow)
  - Automated workflow that generates image then creates video from it in single process
  - *From: VRGameDevGirl84(RTX 5090)*

- **Block conditioning node** (node)
  - Allows injecting different prompts into specific DiT blocks for fine-grained control
  - *From: Mads Hagbarth Damsbo*

- **Video comparison player** (tool)
  - Simple way to compares multiple videos/images in sync for comparing gens
  - *From: Jonathan*

- **Florence2 mask separation with box mode** (node)
  - Updated node with box mode for better mask separation in MultiTalk
  - *From: Kijai*

- **VRGameDevGirl custom node pack** (node)
  - Includes custom color match node, film grain node, and sharpen node for faster processing
  - *From: VRGameDevGirl84(RTX 5090)*

- **Chatterbox Dialog** (node)
  - Forked version of Chatterbox with dialog capabilities and speaker isolation
  - *From: manu_le_surikhate_gamer*

- **Image batcher by indexz** (node)
  - Allows injecting frames into VACE with granular control, supports up to 6 inputs and control maps
  - *From: BarleyFarmer*

- **Start/end frame node with index settings** (node)
  - Kijai planning to add start/end index settings for simpler frame control
  - *From: Kijai*

- **Face enhancer LoRA** (lora)
  - Trained on 58 images of diverse people to improve face detail, no caption or trigger word
  - *From: VRGameDevGirl84*

- **Optical flow visualization node** (node)
  - Node for visualizing optical flow maps in WarperNodes package
  - *From: A.I.Warper*

- **16fps workaround workflow** (workflow)
  - Overcomes WAN 2.1's 16fps cap limitation in vid2vid workflows
  - *From: yo9o*

- **VACE/Phantom merge** (model)
  - Mixed model combining VACE and Phantom capabilities for native ComfyUI
  - *From: Latent Dream*

- **WanVideoWrapper PowerLoraLoader integration** (workflow)
  - WorkFlow to use RGThree PowerLoraLoader with WanWrapper, no extra nodes necessary
  - *From: phazei*

- **Custom detail LoRA** (lora)
  - New LoRA without Flux face characteristics for better face quality
  - *From: VRGameDevGirl84(RTX 5090)*

- **Vintage LoRA for WAN/Skyreels** (lora)
  - LoRA being tested for vintage effects, showing subtle but good results
  - *From: VRGameDevGirl84(RTX 5090)*

- **Paint splash LoRA** (lora)
  - Potential LoRA for paint splash effects, useful for person getting splattered transitions
  - *From: VRGameDevGirl84(RTX 5090)*

- **Wallace and Gromit LoRA** (lora)
  - Character LoRA for 14B model, works great with VACE
  - *From: Cseti*

- **shrug-prompter** (node)
  - Custom ComfyUI nodes for automated prompting using OpenAI compatible VLMs
  - *From: fredbliss*

- **heylookitsanllm** (tool)
  - OpenAI API compatible server for GGUF and MLX models with hot swapping and caching
  - *From: fredbliss*

- **Paint splatter lora** (lora)
  - LoRA for adding paint splatter effects to videos
  - *From: VRGameDevGirl84(RTX 5090)*

- **Reverse detail lora** (lora)
  - LoRA that removes built-in detail effects from FusionX model to prevent overcooking
  - *From: VRGameDevGirl84(RTX 5090)*

- **Enhanced face lora** (lora)
  - Face detail lora trained on upscaled and enhanced dataset
  - *From: VRGameDevGirl84(RTX 5090)*

- **ATI trajectory editor** (tool)
  - Point editor tool for creating movement trajectories, exports JSON format
  - *From: Juampab12*

- **Face Naturalizer LoRA** (lora)
  - Designed specifically for FusionX to smooth out baked-in detail LoRAs
  - *From: VRGameDevGirl84(RTX 5090)*

- **detailboost node** (node)
  - Works well on defaults for adding extra noise to improve quality
  - *From: Clownshark Batwing*

- **spline generator** (tool)
  - For VACE point/spline control, best with black outline on white background
  - *From: Jonathan*

- **ComfyUI-SuperUltimateVaceTools** (tool)
  - Tiled upscaling tool for VACE with reference frame propagation
  - *From: hicho*

- **WanFusionXFaceNaturalizer** (lora)
  - Lora that smooths out detail loras in FusionX for more natural faces
  - *From: VRGameDevGirl84(RTX 5090)*

- **Chunked RoPE calculation** (optimization)
  - Alternative RoPE function processing in chunks to reduce VRAM usage
  - *From: Kijai*

- **Film grain and color match nodes** (node)
  - Faster and better working film grain and color matching nodes, plus sharpening nodes
  - *From: VRGameDevGirl84*

- **Paint splash LoRA** (lora)
  - LoRA for paint splash effects, trained on images
  - *From: VRGameDevGirl84*

- **Automatic podcast generator workflow** (workflow)
  - Uses Qwen + Chatterbox + Multitalk to generate full conversational podcasts from simple prompts
  - *From: AJO*

- **Beard LoRA dataset** (lora)
  - In development beard LoRA for better facial hair in WAN videos
  - *From: VRGameDevGirl84*

- **Paint splash LoRA** (lora)
  - LoRA for paint splash effects with vibrant colors including neon, works well at strength 3.0 for I2V
  - *From: VRGameDevGirl84(RTX 5090)*

- **ChatGPT image captioning script** (script)
  - Script that loops through images and creates text file captions using GPT-4o API
  - *From: VRGameDevGirl84(RTX 5090)*

- **GGUF wrapper implementation** (node)
  - Kijai implemented GGUF support in Wan wrapper for improved performance and quality
  - *From: Kijai*

- **Beard LoRA** (lora)
  - User testing beard LoRA for character generation
  - *From: VRGameDevGirl84(RTX 5090)*

- **Updated Power Lora Loader workflow** (workflow)
  - Simplified workflow for WanWrapper that doesn't require loading extra model
  - *From: phazei*

- **Face Detailer LoRA** (lora)
  - Makes face/skin look more detailed/realistic, testing with different weights for motion retention
  - *From: VRGameDevGirl84(RTX 5090)*

- **Video transition node** (node)
  - New node for adding transitions between video scenes, simpler and supports multiple transition types
  - *From: Kijai*

- **Wan & SkyReels T2I Workflows** (workflow)
  - Native Wan & SkyReels workflows for text to image generation
  - *From: VRGameDevGirl84(RTX 5090)*

- **WanVideoWrapper** (node)
  - ComfyUI implementation by Kijai
  - *From: multiple users*

- **Resize Image v2 node** (node)
  - Updated version with improved functionality
  - *From: Kijai*

- **Video comparison tool** (tool)
  - Tool for comparing video outputs
  - *From: 🦙rishappi*

- **Tile LoRA for stylization** (lora)
  - Used for v2v stylization with 1.3B model
  - *From: David Snow*

- **FP8 converted distilled models** (model conversion)
  - Converted new distilled T2V and I2V models to FP8 format
  - *From: hicho*

- **Simple T2V workflow with fusion LoRA** (workflow)
  - Clean T2V workflow using GGUF with fusion LoRA mix and 16x9/9x16 options
  - *From: Gateway {Dreaming Computers}*

- **Fast LoRA extraction node** (node)
  - Extracts 14B lora in under a minute using torch.svd_lowrank method
  - *From: Kijai*

- **Character LoRA training workflow** (workflow)
  - Using Flux fine-tuning, character sheets, Wan360 turntables, then training with AI Toolkit
  - *From: Gateway {Dreaming Computers}*

- **RES4LYF samplers** (node)
  - Custom sampler nodeset including bong_tangent and other unique samplers for improved generation quality
  - *From: ClownsharkBatwing*

- **Pusa LoRA extraction** (lora)
  - Extracted Pusa LoRA from original model for ComfyUI compatibility
  - *From: Kijai*

- **MTB batch tools** (node)
  - Tools for creating animated control inputs like dot animations for VACE
  - *From: melMass*

- **Pusa lora** (lora)
  - 4.9GB rank512 lora that converts T2V to I2V functionality
  - *From: Kijai*

- **flowmatch_pusa scheduler** (scheduler)
  - New scheduler for Pusa that handles timestep expansion
  - *From: Kijai*

- **Radial attention branch** (feature)
  - Sparse attention implementation for speed improvements in WanVideoWrapper
  - *From: Kijai*

- **GGUF bridge node** (node)
  - Allows GGUF text encoders to work with WAN models
  - *From: mdkb*

- **Tiled upscaler workflow** (workflow)
  - Work-in-progress tiled upscaling system using WAN
  - *From: mono*

- **Sparse SageAttention wheel** (tool)
  - Pre-built wheel for installing Sparse SageAttention API in ComfyUI
  - *From: Kijai*

- **Radial attention optimization** (optimization)
  - Caching the mask made radial attention 40x faster by avoiding redundant calculations
  - *From: Kijai*

- **Model router node** (node)
  - Keeps multiple LoRAs in RAM for easy switching without reload penalty, but incompatible with torch compile
  - *From: mamad8*

- **Video dataset preparation script** (tool)
  - Takes folder of videos and cuts them up while changing fps and resolution
  - *From: Cubey*

- **VACE phantom conditioning patcher** (node)
  - Custom node to properly inject phantom latents into VACE conditioning at correct positions
  - *From: Ablejones*

- **WanVaceToVideoAdvanced node** (node)
  - Custom reference strength control and phantom embed handling
  - *From: Ablejones*

- **Spline Path Control tool** (tool)
  - Tool for creating spline paths as video exports for camera control
  - *From: community member on server*

- **Phantom/VACE merge** (model)
  - Merged model combining Phantom character consistency with VACE controls, though has some color shift issues
  - *From: Piblarg*

- **FP8 conversion ignore list** (tool)
  - Ignore list for FP8 conversion: norm, head, bias, time_in, vector_in, patch_embedding, text_embedding, time_, img_emb, modulation
  - *From: Kijai*

- **Custom camera motion node** (node)
  - Pre-built camera motion from dropdown with built-in resize, could replace motion LoRAs
  - *From: VRGameDevGirl84*

- **Latent replacement node** (node)
  - Node to replace latents between VACE embeds and sampler to reduce degradation
  - *From: A.I.Warper*

- **Album cover animation workflow** (workflow)
  - Converts album covers to realistic style and animates them, can combine with MultiTalk
  - *From: Gateway*

- **VACE keyframing custom node** (node)
  - Custom node for easier VACE keyframe setup
  - *From: JohnDopamine*

- **Consistent character poses workflow** (workflow)
  - Working i2i pose transfer implementation using Wan VACE
  - *From: Valle*

- **VACE+Phantom combination node** (node)
  - Node that combines VACE and Phantom with extra control on conditioning tensor values
  - *From: Ablejones*

- **Custom Uni3C camera presets node** (node)
  - Node with presets for different camera motions like crash zoom, catwalk motion, zoom into eye
  - *From: VRGameDevGirl84(RTX 5090)*

- **AI explosion LoRA remake** (lora)
  - Remade AI explosion lora for testing the new unmerged LoRA system
  - *From: hicho*

- **Vid2vid LoRAs and workflow** (workflow)
  - Complete pipeline for CGI to photorealism conversion with lipsync support
  - *From: samhodge*

- **FP8 scaled models from fp32** (model)
  - Better quality fp8 quantization that's closer to fp16 than existing methods
  - *From: Kijai*

- **Pregnancy details LoRA** (lora)
  - Adds stretch mark details on stomach, back, legs for 480p and 720p
  - *From: Ryzen*

- **Text encoding cache node concept** (node)
  - Caches T5 text encoding results to disk to avoid reprocessing same prompts
  - *From: mamad8*

- **Custom vision LLM server project** (tool)
  - Open source project with custom nodes and vision LLM server for niche use cases
  - *From: fredbliss*

- **Camera motion presets custom node** (node)
  - Custom node with camera motion presets including Arc Right, Arc over head, Orbit around, Pan down/up, crash zoom, dolly zoom
  - *From: VRGameDevGirl84(RTX 5090)*

- **WanVideo Set BlockSwap** (node)
  - Node for block swap memory management with LoRA operations
  - *From: 748197775237447781*

- **Context window padding strategy** (technique)
  - Method to reduce init image snapping in longer generations
  - *From: Kijai*

- **ComfyUI Audio Separation pack** (node)
  - Basic audio separation for multitalking, has other useful audio tools
  - *From: Kijai*

- **Relighting node** (node)
  - Node for controlling light source in x,y,z coordinates for relighting effects
  - *From: A.I.Warper*

- **Disk caching node** (node)
  - Standalone anything to anything caching node with disk cache functionality
  - *From: Hedge*

- **Custom camera motion node** (node)
  - Node for creating camera animations with presets and custom video input support
  - *From: VRGameDevGirl84(RTX 5090)*

- **SetLoRA node usage pattern** (workflow)
  - Using SetLoRA node instead of connecting LoRAs directly to model loader for better performance
  - *From: Kijai*

- **WanVideoWrapper SetLoras node** (node)
  - Additional node for setting LoRAs, works with main LoRA selection node
  - *From: Kijai*

- **Video blending node for extension** (node)
  - Node for blending frames when extending videos to reduce artifacts
  - *From: Ablejones*

- **Uni3C workflow with auto-prompting** (workflow)
  - Workflow using Google API key for automatic prompting or can be turned off
  - *From: Flipping Sigmas*

- **Updated Uni3C Custom Node** (node)
  - Custom video input support, no need for additional nodes
  - *From: VRGameDevGirl84(RTX 5090)*

- **Camera control reference videos** (workflow)
  - Set of reference videos for VACE camera control with various movements
  - *From: The Shadow (NYC)*

- **WAN LoRAs on Civitai** (lora)
  - Style and character LoRAs created by AI_Characters user, many were removed
  - *From: patientx*

- **Sage Attention 3 package** (tool)
  - Separate package for fp4 attention optimization
  - *From: aikitoria*

- **PUSA continuations workflow** (workflow)
  - Workflow for seamless video continuations without quality degradation
  - *From: pom*

- **WanVideoWrapper LoKR support** (node)
  - Kijai implemented LoKR support in WAN video wrapper, works as expected with trigger words
  - *From: jikan*

- **Latent masking in encode node** (feature)
  - Mask input in the encode node for differential diffusion inpainting
  - *From: Kijai*

- **FastWan LoRA extraction** (lora)
  - Extracted FastWan as LoRA against bf16 base model using svd_lowrank method
  - *From: Kijai*

- **Scaled fp8 FastWan conversion** (model)
  - Converted FastWan to fp8 e4m3fn scaled format for better efficiency
  - *From: Kijai*

- **Model combining script** (tool)
  - Python script to combine split safetensors files into single file
  - *From: ingi // SYSTMS*

- **WAN EchoShot ComfyUI implementation** (node)
  - ComfyUI wrapper for EchoShot multi-prompt transitions, works with WAN wrapper encode
  - *From: Kijai*

- **FusionX Phantom merged model** (model)
  - Phantom model merged with FusionX LoRAs, compatible with VACE workflows
  - *From: VRGameDevGirl84*

- **LoRA creation node with SVD** (node)
  - Modified ComfyUI node with SVD lowrank for creating LoRAs in seconds from model differences
  - *From: Kijai*

- **EchoShot LoRA** (lora)
  - Enables first-frame-last-frame morphing for T2V generation
  - *From: Kijai*

- **Control net extraction workflow** (workflow)
  - Pre-processes depth, canny, pose, mask to save memory
  - *From: Gateway*

- **Custom Flux LoRA training** (lora)
  - 146MB LoRA trained on 5 images in 3 hours using ComfyUI trainer
  - *From: VRGameDevGirl84*

- **WanVideoWrapper** (node)
  - ComfyUI wrapper for Wan models with various optimizations
  - *From: Kijai*

- **GetLatentRangeFromBatch** (node)
  - KJ node for extracting specific latents from video batches
  - *From: Kijai*

- **Finnish forest LoRA** (lora)
  - LoRA trained for Finnish forest scenes
  - *From: Drommer-Kille*

- **NABLA attention optimization** (optimization)
  - New attention method that cuts inference time in half for Wan models
  - *From: phazei*

- **lightx2vfp8 converted model** (model)
  - Converted lightx2v model with multiple LoRAs combined
  - *From: hicho*

- **SuperUltimateVaceTools workflow** (workflow)
  - Combines 14B I2V with Lightx2v V2 for upscaling and style transfer
  - *From: Дмитрий Марков*

- **Video grid generation node** (node)
  - Node to load videos from folder and create comparison grids
  - *From: Kijai*

- **Wan 2.2 Prompt Generator** (tool)
  - Custom GPT that generates Wan 2.2 optimized prompts based on official guidelines
  - *From: Nekodificador*

- **System prompt for LLM prompt generation** (tool)
  - Detailed prompt template for any LLM to generate Wan 2.2 style prompts
  - *From: thaakeno*

- **WanVideoWrapper** (node)
  - Kijai's ComfyUI wrapper for Wan models
  - *From: mentioned*

- **Fast unsharp sharpen and film grain nodes** (node)
  - Nodes that help with realism when combined with VFI upscaling
  - *From: Shawneau 🍁 [CA]*

- **Enhanced workflow with adjusted LoRA strengths** (workflow)
  - Optimized WAN 2.2 workflow with 3/1.5 strength ratio for LightX2V
  - *From: Juampab12*

- **Memory patcher for partial loading** (tool)
  - Janky memory patcher to help with VRAM issues
  - *From: Ablejones*

- **Wan 2.2 GGUF workflows** (workflow)
  - Workflows for tomato and steak generation using Q4 GGUF models
  - *From: thaakeno*

- **Evelyn Parker LoRA** (lora)
  - Character LoRA tested with 2.2 models using same workflow as 2.1
  - *From: Kenk*

- **WanVideoWrapper** (node)
  - Kijai's wrapper implementation for Wan models in ComfyUI
  - *From: Kijai*

- **WanVideoWrapper** (node)
  - Kijai's ComfyUI wrapper for Wan models
  - *From: Kijai*

- **Multiple LoRA experiments** (lora)
  - Community testing various LoRA combinations and strengths
  - *From: Ryzen*

- **WanVideoWrapper** (node)
  - ComfyUI wrapper for Wan models with high/low noise sampling
  - *From: Kijai*

- **Character_ai workflow adaptation** (workflow)
  - Modified workflow that produces better results than default ComfyUI workflows
  - *From: GOD_IS_A_LIE*

- **Custom FusionX LoRA** (lora)
  - 200 images with detailed captions for Flux, looking for feedback
  - *From: VRGameDevGirl84(RTX 5090)*

- **Character AI workflow update** (workflow)
  - Updated workflow that reduces ugly motion blur
  - *From: GOD_IS_A_LIE*

- **Wan 2.2 + VACE merged model** (model)
  - FP16 models merged and quantized to GGUF Q8 with depth and pose controls
  - *From: JmySff*

- **Wan 2.2 Prompt Creator** (tool)
  - GPT that helps create prompts for Wan 2.2 based on community documentation
  - *From: ✧ฅโ๑ↀᆺↀ ๑ใฅ✧PookieNumnums*

- **fp8_e5m2_scaled models** (model)
  - Alternative quantization for 3090 users with compile
  - *From: Kijai*

- **Experimental VACE merge** (model)
  - Wan2.2 with VACE scopes injected for control
  - *From: AniWanefrrr*

- **WanVideoWrapper** (node)
  - Kijai's ComfyUI wrapper implementation for WAN models
  - *From: Kijai*

- **Shinkai anime LoRA** (lora)
  - Anime style LoRA that works with WAN models, though strength varies by seed
  - *From: Cseti*

- **WanVideoWrapper updated for 2.2** (node)
  - Kijai's wrapper updated to support Wan 2.2 with A14B working properly
  - *From: Kijai*

- **T2V workflow with optimizations** (workflow)
  - Includes NAG toggle, block swap controls, and LoRA strength settings
  - *From: patientx*

- **WanVideoWrapper** (node)
  - ComfyUI wrapper for Wan 2.2 with two-sampler setup and improved memory management
  - *From: Kijai*

- **VACE workflow for inpainting** (workflow)
  - Working VACE inpainting setup with color and animation controls
  - *From: Sal TK FX*

- **Wan 2.2 prompt analysis tools** (tool)
  - Google AI Studio prompt analysis and JavaScript generator for Wan 2.2 prompts
  - *From: GOD_IS_A_LIE*

- **WanVideoWrapper** (wrapper)
  - Kijai's wrapper for Wan models with better memory management
  - *From: Kijai*

- **Memory management nodes** (nodes)
  - Nodes for clearing VRAM and managing memory in ComfyUI
  - *From: MilesCorban*

- **WanVideoWrapper** (node)
  - Kijai's wrapper for Wan models in ComfyUI, updated for 2.2 support
  - *From: Kijai*

- **Save/Load Latent workflow** (workflow)
  - Memory management solution for limited RAM systems
  - *From: The Shadow (NYC)*

- **ClownSharkChainSampler** (node)
  - Alternative to SharkChainSampler for chain sampling workflows
  - *From: Clownshark Batwing*

- **Smoking LoRA** (lora)
  - 1 hour trained LoRA for smoking effects, working with 2.2
  - *From: Kenk*

- **Dual Loaders/Dual Samplers subgraphs** (workflow)
  - Reusable template components for converting Wan 2.1 to 2.2 workflows
  - *From: JohnDopamine*

- **Wan 2.2 prompt creator** (tool)
  - ChatGPT model trained on official Wan prompt guide for generating proper prompts
  - *From: ✧ฅโ๑ↀᆺↀ ๑ใฅ✧PookieNumnums*

- **Adaptive rank LightX2V LoRA** (lora)
  - Works best out of all ranks LoRA tried, quantile 0.15 bf16
  - *From: gokuvonlange*

- **Custom Kontext LoRA training** (lora)
  - Training custom kontext lora for changing scenes to pair with wan 2.2
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Beta57 scheduler implementation** (node)
  - Custom beta scheduler with 0.5/0.7 parameters for better two-regime sampling
  - *From: Ablejones*

- **Custom sigma schedule visualization** (tool)
  - Linear quadratic schedule with exposed inflection % and threshold noise parameters
  - *From: Ablejones*

- **Dummy node for wrapper** (node)
  - Added to wan wrapper for additional functionality
  - *From: Kijai*

- **GGUF Q8 quantized models** (model)
  - Merged and quantized both high/low noise models
  - *From: JmySff*

- **Vid2vid workflow with video samples** (workflow)
  - Adds video samples into samples and lowers denoise on first sampler
  - *From: VK (5080 128gb)*

- **Modified 5B model workflow** (workflow)
  - Workflow adapted for 5B model without block swapping
  - *From: thaakeno*

- **MMaudio integrated workflow** (workflow)
  - Combines Wan 2.2 video generation with audio synthesis
  - *From: thaakeno*

- **Basic T2V example workflow** (workflow)
  - Simple text-to-video workflow for WAN 2.2 14B with LightX integration
  - *From: AJO*

- **Vid2vid workflow for GGUF models** (workflow)
  - Video-to-video transformation workflow optimized for GGUF quantized models
  - *From: thaakeno*

- **WAN 2.2 14B GGUF V2V workflow** (workflow)
  - Video-to-video workflow using GGUF quantized WAN 2.2 14B model
  - *From: thaakeno*

- **Enhanced taew2_1.safetensors support** (node update)
  - Fixed extra paths support for VAE approximation file
  - *From: Kijai*

- **Multi-resolution I2V workflow** (workflow)
  - Decode after small resolution pass, swap first frame with original, reprocess at higher resolution
  - *From: mamad8*

- **Context safety check** (tool)
  - GPT4.1 generated safety check function to prevent ComfyUI crashes from invalid context settings
  - *From: Kijai*

- **WanVideoWrapper T2I workflow** (workflow)
  - Clean text-to-image workflow for Wan 2.2 with embedded PNG
  - *From: VRGameDevGirl84*

- **V2V workflow for 14B GGUF** (workflow)
  - Complete video-to-video workflow using Wan 2.2 14B model
  - *From: thaakeno*

- **LightX quantile LoRA** (lora)
  - Speed enhancement LoRA with specific strength recommendations for different CFG values
  - *From: Juampab12*

- **FusionX LoRA** (lora)
  - Quality enhancement LoRA working on Wan 2.2, used on second pass
  - *From: VRGameDevGirl84(RTX 5090)*

- **Combined sampler node** (node)
  - Combines both samplers into 1, auto splits steps and handles start/end steps automatically
  - *From: VRGameDevGirl84*

- **Color match node optimization** (workflow)
  - Working on lower VRAM implementation for 16GB systems
  - *From: VRGameDevGirl84*
