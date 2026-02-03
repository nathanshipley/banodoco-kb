# Wan Chatter Knowledge Base
*Extracted from Discord discussions: 2025-06-01 to 2025-07-01*


## Technical Discoveries

- **AccVid + CausVid combination significantly improves quality**
  - AccVid 1.5 strength + CausVid 0.5 strength with dpmpp_2m and sgm_uniform at 3 steps looks better than 8 steps with just CausVid
  - *From: Jonathan*

- **CausVid LoRA brings native and wrapper I2V outputs closer together**
  - Using CausVid reduces differences between native and wrapper implementations
  - *From: Kijai*

- **Enhance feature helps with motion when using CausVid**
  - Enhance actually helps with motion quite a bit with causvid
  - *From: Kijai*

- **HPS LoRA may be beneficial to add**
  - Adding HPS LoRA may not be a bad idea either
  - *From: Kijai*

- **Phantom 14B shows much better results than 1.3B**
  - Movement is great as well as the colors and camera overall. way better than 1.3b
  - *From: stas*

- **MPS Reward LoRA dramatically improves Wan video quality and details**
  - Using MPS (prompt adherence) reward LoRA with strength 1 alongside CausVid produces significant quality improvements - described as 'night and day' difference
  - *From: VRGameDevGirl84*

- **Combining multiple LoRAs produces best results for low step workflows**
  - Best combo found: CausVid + AccVid (improves prompt adherence, movement, detail) + HLS (further improves prompt adherence and movement) at 3 steps
  - *From: Jonathan*

- **T2V LoRAs work with I2V models**
  - T2V LoRAs can be used with I2V models, I2V LoRAs work with T2V but perform worse
  - *From: ZeusZeus*

- **Any image LoRA trained at 1024 improves quality on any model**
  - Image-only LoRAs trained at 1024 resolution act as detailers and pull up quality when used on video models
  - *From: Thom293*

- **Fun InP 1.3B is actually an image to video model**
  - Despite the name, it functions as I2V
  - *From: hicho*

- **Detail Transfer node can improve mouth movements with masking**
  - Using Detail Transfer node with mouth mask provides better lip sync results
  - *From: A.I.Warper*

- **Resolution mismatch causes VACE encoder stacking issues**
  - Different preprocessor output resolutions prevent normals and DW pose from working together
  - *From: Neex*

- **MoviiGen LoRA adds significant prompt adherence**
  - At strength 0.75, MoviiGen dramatically improves following detailed camera movement prompts
  - *From: VRGameDevGirl84(RTX 5090)*

- **Wan-Toy-Transform LoRA converts things in images to fluffy JellyCat-style toys**
  - Trigger prompt: 'The video opens with a clear view of a $name. Then it transforms to a b6e9636 JellyCat-style $name. It has a face and a cute, fluffy and playful appearance.'
  - *From: hicho*

- **ATI trajectories can go out of frame and still work properly**
  - Trajectories extending beyond image boundaries are handled correctly by the model
  - *From: Kijai*

- **Wan needs 121 points for 81 frames due to fps conversion**
  - Something to do with the expectation that you do the points in 24fps while the model is 16fps
  - *From: Kijai*

- **VACE inpainting can work even without connecting masks**
  - Forgot to connect the masks for vace inpainting, and ran only with the gray mask input video. Somehow, it still worked.
  - *From: Johnjohn7855*

- **Face area trimming and upscaling improves facial expressions**
  - Trim the face area and upscale to 720p, then pass into preprocessor and sampler. After that, downscale back to original size and stitch back into video
  - *From: DeZoomer*

- **540p model works on 360x640 resolution**
  - You just need to come in under the stated resolution for skyreels+vace
  - *From: Zuko*

- **CausVid v2 at 10 steps performs significantly better than 5 steps**
  - Huge difference between 5 -> 10 steps, but 10 -> 15 steps isn't worth it
  - *From: MilesCorban*

- **External pose detection works better than ComfyUI's DWPose**
  - DWPose in ComfyUI doesn't work as well as HuggingFace demos, sometimes spits out black frames
  - *From: A.I.Warper*

- **MPS LoRA at strength 2.0 removes flux face**
  - Testing showed MPS lora strength 2 removes flux face LOL
  - *From: VRGameDevGirl84(RTX 5090)*

- **On-the-fly model merging using ModelMergeSimple node**
  - Can merge models without saving using ModelMergeSimple node, allows for dynamic testing
  - *From: ▲*

- **ATI trajectory editor now has official release**
  - Official editor uploaded with timeline support
  - *From: Juampab12*

- **ATI hardcoded to 121 frames in 24fps which corresponds to 81 frames in 16fps**
  - Original code limitation prevents using other frame counts
  - *From: Kijai*

- **ATI solves motion almost on the first step**
  - Motion control is applied very early in the denoising process
  - *From: Kijai*

- **Using 121 points in spline editor gives better results than 81 for ATI**
  - Despite 81 frame output, 121 trajectory points work better
  - *From: TK_999*

- **Model makes things bright green when failing**
  - Green hue indicates generation problems or parameter conflicts
  - *From: TK_999*

- **CausVid v1 consistently outperforms v1.5 and v2 for both I2V and T2V**
  - After 300 generations of testing
  - *From: Jonathan*

- **Wan can generate 81 frames at 2 steps looking better than 1 frame at 2 steps with image models**
  - Video model efficiency surprising at low step counts
  - *From: Jonathan*

- **Temperature and top_k values for ATI initially don't seem to do much**
  - May affect more with many trajectory points
  - *From: Kijai*

- **VACE embed strength can be lowered to reduce color washout and jankiness across batch seams**
  - Using 70% strength with depth only reduces artifacts, especially where depth detection fails and areas approach black
  - *From: A.I.Warper*

- **Inverting colors in gaze control makes people get glasses**
  - Interesting side effect when using gaze control preprocessing
  - *From: Mads Hagbarth Damsbo*

- **Different samplers affect quality significantly**
  - UniPC gives results in fewer steps but lower quality. DPM++ 2M/SGM_uniform and Euler provide better image quality but require more steps
  - *From: Jonathan*

- **GGUF models respond better to CausVid/AccVideo LoRAs**
  - GGUF format seems to work better with motion LoRAs for unknown reasons
  - *From: CJ*

- **GGUF LoRAs behave differently than regular LoRAs**
  - When using GGUF LoRAs are not merged into the main model, instead the weights are added during the dequant of the weights, that often makes LoRAs stronger... but also means that every LoRA you add slows it down a bit and uses more memory
  - *From: Kijai*

- **AccVid I2V performance is step-dependent**
  - AccVid is heavily dependent on steps. AccVid works much better at a higher strength, increasing the motion, detail and prompt adherence greatly. At higher steps it will 'overcook' the video. Even raising the steps from 2 to 4 at a high accvid strength will overcook the colors quite a bit.
  - *From: Jonathan*

- **Sampler choice dramatically affects output quality**
  - Massive difference between euler and dpmpp_2. Euler has natural skin tone and better natural lighting. dpmpp_2 plus beta outputs very detailed bright video type.
  - *From: Thom293*

- **SageAttention 2 provides huge performance improvements**
  - Minimum 30% speed improvement, can double speed at higher resolutions like 1024+, also reduces VRAM usage
  - *From: Jonathan/Kijai*

- **CausVid 2-step workflow good for fast testing**
  - Fast objects are blurry at 2 steps, can bump to 3 steps for quick testing
  - *From: Jonathan*

- **Phantom model isn't flexible with other additions**
  - Adding anything to Phantom model makes it work worse, need to use lower strength if combining with CausVid
  - *From: Kijai*

- **CFG above 1.0 causes extreme saturation in Native**
  - With Accvid, causvid 1/1.5, mps - output gets extremely saturated when CFG raised above 1.0
  - *From: Persoon*

- **ATI works with CausVid**
  - CausVid works pretty great with ATI (Animated Track Interpolation)
  - *From: Kijai*

- **TeaCache works with CausVid at lower thresholds**
  - TeaCache sort of works with CausVid, just not at as high threshold as without CausVid
  - *From: Jonathan*

- **FP32 VAE is worth using for single image encoding**
  - Better quality for encoding single images
  - *From: Kijai*

- **AccVid strength increases motion by 50% per strength level**
  - AccVid at 4.00 has very dynamic motion, works best at 2-3 steps
  - *From: Jonathan*

- **CausVid takes away motion, AccVid adds motion**
  - They work well together as complementary tools
  - *From: jdl_grmck*

- **Higher AccVid strength works better on low steps**
  - The higher the steps, the more overcooked videos look with high AccVid
  - *From: Jonathan*

- **Vace conditionings are now stackable in ComfyUI native**
  - Recent commit allows stacking different Vace conditions
  - *From: artemonary*

- **Raising causvid lora to 0.75 greatly increases motion when used with accvid at high strengths**
  - Also raising causvid strength seems to fix overcooked colors that high accvid strengths cause
  - *From: Jonathan*

- **Original causvid gives better results than V2 in some cases**
  - Looks better when ran with just wan though strange
  - *From: VRGameDevGirl84(RTX 5090)*

- **LoRAs do load in Native workflow despite console errors**
  - Testing confirmed loras ARE actually loading regardless of what the console says
  - *From: VRGameDevGirl84(RTX 5090)*

- **Prompt adherence is better with certain lora combinations**
  - The prompt had 'Kite' flying in background, so prompt adherence is better in the 2nd one
  - *From: VRGameDevGirl84(RTX 5090)*

- **VRAM usage grows with pixel count - 1080p to 4k is like 16x pixels**
  - If able to gen 5s without issues in 720x720 with 12gb, should be able to do better on ggufs with better setups
  - *From: The Punisher*

- **3 steps produces surprisingly good quality**
  - User achieved insane quality for 3 steps with specific settings, though some artifacts like weird carpet texture remain
  - *From: The Punisher*

- **Simple scheduler works best for low steps**
  - Testing shows simple scheduler outperforms beta, linear quadratic, and kl_optimal for 3-step generation
  - *From: The Punisher*

- **Q8 GGUF quality comparison**
  - Q8 GGUF is roughly equivalent to fp16 safetensors quality but half the size, significantly better than fp8
  - *From: The Punisher*

- **Seeds matter significantly for video generation**
  - Some seeds work fantastically well while others produce complete failures, contrary to typical randomness expectations
  - *From: ▲*

- **Phantom may prefer character positioning**
  - Testing suggests phantom performs better when characters are positioned optimally in the reference image
  - *From: ▲*

- **Reference image size in canvas affects dominance**
  - Parts of reference image that occupy more space in canvas dominate the outputs more
  - *From: Johnjohn7855*

- **AccVid I2V LoRA is much better than T2V version**
  - Better resemblance retention, fixes overblown colors, greater prompt adherence, more fluid dynamic movement, more stable at higher strengths up to 4.0
  - *From: Jonathan*

- **CFG scheduling 4,3,2,1,1,1,1,1,1,1 is key to success**
  - This CFG scheduling is described as 'the whole secret of success' for workflows
  - *From: AJO*

- **Separating VACE encodes affects control strength**
  - Single VACE embed with start frame and control has stronger control than separating first frame into its own encode and control into its own
  - *From: hablaba*

- **Reducing shift parameter helps with transition speed**
  - Reducing shift from 8 to 5 helped with how fast the model changes between frames
  - *From: 3Dmindscaper2000*

- **Blurring depth maps while increasing strength improves results**
  - Turned up strength of depth control but blurred it more to compensate for better results
  - *From: A.I.Warper*

- **Shift values significantly affect video generation results in merged models**
  - VRGameDevGirl84's merge performs best with shift=1-2, while standard Wan typically uses higher shift values around 5-14
  - *From: VRGameDevGirl84*

- **Hair artifacts can be reduced with proper shift tuning**
  - Hair issues appear with higher shift values (8+) and can be minimized by finding optimal shift range for specific models
  - *From: The Punisher*

- **Step count affects minimum viable shift values**
  - 3 steps requires higher shift values, 4+ steps allows lower shift values. Formula suggested: steps*0.5 for safe shift value
  - *From: The Punisher*

- **GGUF vs FP16 may cause quality differences**
  - Hair artifacts may be related to using GGUF quantized models vs full precision FP16 weights
  - *From: The Punisher*

- **Detail transfer can be applied selectively using pose landmarks**
  - Mouth coordinates from MediaPipe/DWPose can be used to create tracking masks for selective detail enhancement
  - *From: A.I.Warper*

- **VACE inpainting requires mid-grey masks (127, 127, 127) not white masks**
  - Standard white masks don't work - need specific RGB value of 127, 127, 127 for proper inpainting
  - *From: David Snow*

- **Multiple VACE encodes improve video quality**
  - Using separate VACE encodes for different controls at lower strengths improves video quality compared to combining controls
  - *From: David Snow*

- **FP32 precision dramatically improves quality**
  - Using FP32 for VAE and T5 text encoder produces significantly better quality results than lower precision
  - *From: Dream Making*

- **Phantom ignores reference elements not mentioned in prompt**
  - Phantom is very specific about prompting and will ignore anything in reference images that isn't explicitly mentioned in the prompt
  - *From: ingi // SYSTMS*

- **CausVid V2 needs higher strength settings for photorealistic content**
  - Phantom 14b with photorealistic content needs CausVid V2 lora strength around 2.0
  - *From: zelgo_*

- **Model dimensions must be divisible by 16**
  - The model has a hard requirement that dimensions must be divisible by 16, ComfyUI automatically adds pixels if not
  - *From: Kijai*

- **720p model significantly outperforms 480p model**
  - 720p model fixes realistic movement issues that 480p struggles with, even at lower resolutions. 480p gives slowed down fluid motion while 720p provides realistic dynamic movement
  - *From: Jonathan*

- **Even step counts work better than odd step counts with shift formula**
  - Formula 'steps * 0.5 - 0.25' works for even steps (4,6,8), but odd steps (3,5,7) need additional +8 and look worse with glitches
  - *From: The Punisher*

- **FP32 doubles inference time compared to FP16**
  - Running 1.3B model at FP32 was extremely slow, FP16 without quantization works better
  - *From: ingi // SYSTMS*

- **12 steps with Phantom and Causvid produces decent results**
  - Good quality output achieved with this combination
  - *From: ingi // SYSTMS*

- **Flowmatch_Causvid scheduler disables shift settings**
  - According to gemini AI, using Flowmatch_Causvid basically disables shift parameter functionality
  - *From: The Dude*

- **Custom sigmas work better with low shift than normal sigmas**
  - Custom sigmas with low shift provide better detail than normal sigmas with high shift (9.75)
  - *From: The Punisher*

- **Color shift occurs during video extension with Skyreels DF**
  - Heavy color shift happens when extending videos with Skyreels DF, can be fixed with color match node
  - *From: Persoon*

- **DPM++ SDE Beta works best for Phantom**
  - Scheduler testing shows DPM++ SDE Beta performs best with Phantom model
  - *From: VRGameDevGirl84(RTX 5090)*

- **Phantom reference adds a latent causing frame count mismatch**
  - When using Phantom with uni3c, phantom adds an extra latent causing tensor size mismatch (Expected size 11 but got size 9)
  - *From: Kijai*

- **Wan wrapper strength value behaves like a blend percent between inpaint and original, not as reference image weighting**
  - User expected strength to weight reference image information but it acts more like a blend factor
  - *From: the_darkwatarus_museum*

- **Phantom wrapper batching multiple images doesn't work as expected initially**
  - Only first latent is accounted for, but lowering latent_strength to around 0.65 on each latent input helps with comprehending differences between people
  - *From: the_darkwatarus_museum*

- **VACE only processes the first reference frame when multiple are passed**
  - Code will just use the first frame even if batch of reference frames is sent
  - *From: Piblarg*

- **FP32 configuration significantly improves quality**
  - Configuring model in fp32 increases quality noticeably, especially at 720p, with less 'weird nose' artifacts and noise
  - *From: Juan Gea*

- **CausVid V2 requires much higher strength settings**
  - V2 works much better with strength around 2.0, also 20-30% faster than previous versions
  - *From: David Snow*

- **Native VACE is about 10 times quicker than KJ wrapper**
  - Performance difference observed during testing
  - *From: samhodge*

- **Phantom can take up to 4 batched images**
  - Multiple encode nodes possible but effect wasn't great, causes blending rather than unique processing
  - *From: Piblarg*

- **VACE loses control on longer videos**
  - Works fine at 45 frames, starts losing at 85 frames, and for 161 frames does not follow anymore
  - *From: Piblarg*

- **Wan models work worse beyond 81 frames**
  - Anything beyond the 81 frames just works worse, except with models trained with more frames like skyreels
  - *From: Kijai*

- **FP16_fast provides 20% speed boost**
  - Torch 2.7.0 provides about 20% speed boost for Wan in general with fp16_fast
  - *From: Kijai*

- **VACE latents are actually empty**
  - Information is passed through conditioning pipes not latent ones, latent just needs to be same size
  - *From: Piblarg*

- **Self-forcing model from Adobe achieves 16 fps generation speed**
  - Takes ~5 seconds to do 81 frames on 4090 with 1.3B and 6 steps, equivalent to about 16 frames per second
  - *From: Kijai*

- **Self-forcing works with VACE for I2V despite being T2V model**
  - 1.3B self-forcing model can work with VACE conditioning for image-to-video generation
  - *From: slmonker*

- **Skip Layer Guidance can fix screen door artifacts**
  - Using SLG as a second pass V2V with low denoise can eliminate high-frequency detail artifacts
  - *From: chrisd0073*

- **FP32 VAE only helps on encode, not decode**
  - FP32 VAE provides very slight quality improvement on encode only, never saw it do anything on decode
  - *From: Kijai*

- **DPM++_SDE/Beta sampler reduces noise/screendoor effects**
  - Using DMP++_SDE sampler with 10 steps, CFG 1, Shift 2 for I2V with start/end frame reduces screendoor artifacts
  - *From: Juan Gea*

- **Self-Forcing models have no 81 frame limit**
  - N0NSens confirmed that Self-Forcing models can generate beyond 81 frames without restrictions
  - *From: N0NSens*

- **Self-Forcing model is 6-7x faster than WAN + CausVid**
  - Jonathan reports 6-7x faster generation on 12GB card compared to already accelerated WAN with CausVid/AccVid
  - *From: Jonathan*

- **Self-Forcing generates frame sequentially/autoregressively**
  - MysteryShack explains it generates frames sequentially, depending on previous frame for next one, different from standard WAN parallel generation
  - *From: MysteryShack*

- **LoRAs have more influence on Self-Forcing model**
  - Kaïros reports LoRAs seem to have stronger effect and produce consistent results across different sampler/scheduler combinations
  - *From: Kaïros*

- **Self-Forcing model has near-zero prompt adherence in I2V**
  - N0NSens demonstrates poor prompt following with spacesuit example using VACE I2V
  - *From: N0NSens*

- **CausVid kills motion, AccVid restores it**
  - Jonathan explains CausVid reduces movement while AccVid increases it, recommending AccVid at 1.5-2.0 strength
  - *From: Jonathan*

- **Lowering shift increases motion significantly**
  - Jonathan advises lowering shift parameter can greatly increase motion in generations
  - *From: Jonathan*

- **ProRes crushes blacks on Windows due to Mac gamma vs PC gamma difference**
  - Built for Mac gamma, causes black crushing on Windows systems
  - *From: Ruairi Robinson*

- **fp8_e4 doesn't work with compile, use fp8_e5 instead**
  - Compatibility issue with torch compile
  - *From: Dream Making*

- **Self-forcing model license is CC4 non-commercial share-alike**
  - Important licensing restriction for commercial use
  - *From: Kijai*

- **Self-forcing training took only 2 hours with many H100s**
  - Suggests 14B version could potentially be trained in a day
  - *From: Kijai*

- **VACE+Phantom merge requires tensor size matching**
  - Need to add 4 images to VACE conditioning for every Phantom image to match tensor sizes
  - *From: Piblarg*

- **Self-forcing achieves 16 fps on Wan 1.3B on H100**
  - Significant speed improvement for video generation
  - *From: izashin*

- **Wan DCM lora can be extracted and used separately from main model**
  - Even when used incorrectly, the extracted DCM lora shows significant improvement. They split training into 'semantics' (DCM lora for first few steps) and 'details' (rest of model)
  - *From: Kijai*

- **Phantom model has better face consistency at 480p than 720p**
  - The Phantom-Wan-14B model was trained on 480p data, explaining better performance at that resolution
  - *From: Yan/chrisd0073*

- **VACE can work with batched reference images for Phantom**
  - Users successfully using batched images as reference input for Phantom with VACE
  - *From: Piblarg*

- **AniWan Merge at 25% with OgWan works well for I2V**
  - Using AniWan Merge at 25% with OgWan 480p I2V, 2 Step Wan I2V Workflow, LiveWallpaper 480p Strng 0.25 + CausVid Strng 0.5 + Upscale with Deflicker workflow produces good results
  - *From: ZRNR*

- **Self-forcing model is very fast with acceptable results**
  - Works as low as 3-5 steps, 8 steps is best. Only works with 1.3b loras
  - *From: patientx*

- **Detail transfer helps maintain quality when upscaling**
  - Using detail transfer with upscaling workflows maintains fine details better than standard upscaling
  - *From: ZRNR*

- **NAG (Negative Augmented Generation) shows impressive results with Wan**
  - Initial test results show significant improvement, only added to crossattn so speed loss is negligible
  - *From: Kijai*

- **Causal sampling running in realtime**
  - Wild seeing the video in realtime in the preview, does 3 latents at a time. Even works for T2V
  - *From: Kijai*

- **Multiple VACE embeds work with proper setup**
  - Can use 2-3 VACE embeds simultaneously for different controls (depth, pose, ref image)
  - *From: Kijai*

- **NAG (Normalized Attention Guidance) PR merged and working**
  - NAG PR is merged and can be used with Wan models, basically CFG distillation that adds motion and is nearly free computationally
  - *From: Kijai*

- **MagCache performs similarly to TeaCache**
  - MagCache is almost exactly the same as TeaCache, requires 10x lower threshold values than defaults to work properly
  - *From: Kijai*

- **Native/GGUF runs twice as fast as wrapper**
  - Same settings, not running out of VRAM anywhere, but native implementation is significantly faster
  - *From: MysteryShack*

- **Wan adds padding frames for incompatible frame counts**
  - When using 100 frame video, it samples 101 frames but outputs 97, includes reference latents in sampling count
  - *From: Kijai*

- **VACE precision doesn't matter much**
  - Higher precision VACE module gets quantized to same as main model anyway
  - *From: Kijai*

- **NAG (Negative Attention Guidance) works with 1 CFG**
  - Allows negative prompting without regular CFG, can remove things from video without changing main composition or change details
  - *From: Juampab12*

- **CausVid sampling needs specific timesteps**
  - Playing with timesteps can break compatibility with other components
  - *From: Kijai*

- **TeaCache doesn't work well with low steps**
  - At low steps, TeaCache doesn't provide meaningful improvement over just using fewer steps
  - *From: Kijai*

- **Phantom considers colors, backgrounds, positions and scale from reference images**
  - Need to position references on 2D board roughly, avoid cropping ref image smaller than output
  - *From: ▲*

- **Phantom works better when merged with T2V model at 0.15-0.25 strength**
  - LoRAs work way better with this merge, pure Phantom often produces 'monstrosity' with LoRAs
  - *From: ▲*

- **NAG memory usage is minimal**
  - Max allocated memory increased from 16.915GB to 16.924GB, reserved from 18.156GB to 18.562GB
  - *From: Kijai*

- **Cosmos Predict2 uses WAN VAE and architecture**
  - Config shows '_class_name': 'WanModel', same 14B size as WAN, likely finetune or same architecture trained from scratch
  - *From: Ada*

- **Self-forcing model is 5-6x faster than Wan 14B and works well with t2v, i2v, and vace**
  - After 500 tests, consistently faster performance with comparable quality to 14B model
  - *From: Jonathan*

- **Self-forcing model retains composition at 2 steps, allowing faster testing**
  - Unlike 14B model, can generate at 2 steps and retain composition for rapid testing of vace control, movement, and seeds
  - *From: Jonathan*

- **NAG keeps things more intact when pushing values compared to scheduled CFG**
  - More evident results and better timing control than scheduled CFG for initial steps
  - *From: ▲*

- **Camera movement can be controlled with simple splines on background in VACE**
  - Longer splines = faster movement, shorter = slower. Two splines in opposite directions create rotation. Size changes enable zoom in/out
  - *From: Jonathan*

- **Changing frame rate of control affects movement speed while keeping output frame rate**
  - Can speed up or slow down movement by adjusting control frame rate independently
  - *From: Jonathan*

- **Phantom has character LoRA bleeding solution**
  - Can put two different characters in one scene with no bleeding using reference (latent strength s > 1) and LoRA (strength S < s)
  - *From: ZeusZeus (RTX 4090)*

- **Torch compiler works with fp8_e5m2 setting**
  - Only works with this specific setting, not with default or fp8_e4m3f
  - *From: ▲*

- **Phantom may be trained on realistic images only**
  - Testing suggests it struggles with non-realistic inputs, explaining inconsistent performance
  - *From: Piblarg*

- **VACE with phantom produces better i2v results than standard 14B t2v/VACE**
  - Phantom/VACE combination shows much better face stability and detail, especially after first few frames
  - *From: David Snow*

- **VACE can do i2v using just start image**
  - Use start to end frame node with just start image connected, acts like i2v
  - *From: David Snow*

- **VACE is good at filling in motion from partial control**
  - Can provide just a few frames of control and VACE continues the motion for rest of video
  - *From: Jonathan*

- **FusionX with VACE produces high quality results**
  - CV VACE with fusion lora at 4 steps is faster and better than original i2v
  - *From: hicho*

- **Phantom allows up to 121 frames instead of 81**
  - Can generate longer videos at 24fps compared to standard i2v
  - *From: David Snow*

- **Causal sampling does 3 latents at a time**
  - Can theoretically go endlessly, trained with 3 latents so struggles with normal 81 frame workflows that do 21 latents
  - *From: Kijai*

- **Context options allow 241+ frame videos**
  - Effectively stitches together multiple 81 frame videos with overlapping frames
  - *From: blake37*

- **FusionX is 90% CausVid with other loras merged**
  - The main performance boost comes from CausVid, with other loras providing additional quality improvements
  - *From: Kijai*

- **NAG node provides massive improvement to prompt following and motion quality at 1 CFG**
  - New node that allows CFG-like results without the 2x generation time penalty
  - *From: Ada*

- **Skip layer guidance with 1.3B at 0.1 denoise does a nice job for cleanup**
  - Can be used to improve results from 14B generations
  - *From: chrisd0073*

- **Reward loras from diffsynth are without alpha, so they are twice as strong**
  - Need to account for doubled strength when using these loras
  - *From: Kijai*

- **Using FusionX as a lora with NAG and HPS at 0.4 gives CFG-like results without CFG**
  - Combination provides good results with noise_aug_strength
  - *From: Ada*

- **VACE can do image extension instead of pure i2v when used like t2v**
  - Acts more like text-to-video if reference image isn't properly plugged in
  - *From: hicho*

- **Tiled upscaling allows Full HD ultrawide generation on 4090**
  - 81 frames at 1920x544 using only 60% VRAM with Ultimate SD Upscale
  - *From: David Snow*

- **NAG can be used in native ComfyUI with new NAG node from KJNodes**
  - Just plug it into the model and plug in the negative conditioning. ModelSamplingSD3 node can change shift in native
  - *From: Screeb*

- **Self-forcing model uses shifted sigmas like 'warp' causvid**
  - Similar to the causvid warp functionality
  - *From: Kijai*

- **Self-forcing model was trained very quickly**
  - Appears to have been done in just a few days
  - *From: Kijai*

- **LightX2V/self-forcing LoRA doesn't have causvid motion issues**
  - Can use at full strength without first block issues that causvid has
  - *From: Kijai*

- **LightX2V handles motion loras much better than CausVid or AccVid with half the cost**
  - Better performance with motion-specific loras
  - *From: DevouredBeef*

- **Context windows work by mixing clips during sampling**
  - All done at the same time, which is why start frame doesn't work well and it's slower and less consistent
  - *From: Kijai*

- **ATI (I2V) with context windows is complicated due to init image handling**
  - Reference image is easy as it's not absolute like first frame init image
  - *From: Kijai*

- **New LightX2V LoRA replaces CausVid for speed**
  - LightX2V is a new speed LoRA that provides improved motion and can replace CausVid. It's trained for 4 steps and provides transformative results
  - *From: David Snow*

- **LightX2V performs better at 4 steps than higher step counts**
  - The LoRA is specifically trained for 4 steps. At 6+ steps it becomes overcooked, while 4-5 steps provide optimal results
  - *From: Kijai*

- **MovieGen benchmark prompts available for testing**
  - Self-Forcing repo contains MovieGen benchmark prompts that are useful for testing video generation models
  - *From: Kijai*

- **Merged models use less VRAM than loading multiple LoRAs**
  - Using a merged model eliminates VRAM overhead from loading multiple LoRAs dynamically, allowing for better performance without block swap
  - *From: MysteryShack*

- **UniPC scheduler has issues separating camera and object movement**
  - UniPC scheduler cannot move only objects without camera movement - everything moves together when using UniPC
  - *From: N0NSens*

- **Context window shifts are visible in video generation**
  - You can visually detect when the context window shifts during video generation, affecting motion continuity
  - *From: Nekodificador*

- **NAG enables negative prompts to work with CFG 1 workflows**
  - NAG allows negative prompts to function again for accelerated CFG 1 workflows like caus/acc derived workflows
  - *From: blake37*

- **MAGREF uses pixel-wise masks with channel concatenation**
  - Unlike previous methods that concatenate reference images along token dimension, MAGREF applies pixel-wise masks and combines via channel concatenation for better identity preservation
  - *From: TK_999*

- **MAGREF works out of the box without modifications**
  - MAGREF I2V model works immediately without needing any special setup or changes
  - *From: Kijai*

- **T2V LoRAs work on I2V models**
  - LoRAs trained for T2V models can be used effectively on I2V models, including cfg/step distill LoRAs
  - *From: Kijai*

- **lightx2v LoRA excellent for morphs and animated logos**
  - The lightx2v LoRA produces unexpected and awesome results for morphs and animated logos
  - *From: David Snow*

- **Context windows work better with MAGREF than normal I2V**
  - Context windows perform better with MAGREF I2V model compared to standard I2V
  - *From: Kijai*

- **LightX2V LoRA works for both T2V and I2V**
  - Can be used with both text-to-video and image-to-video generation modes
  - *From: The Shadow (NYC)*

- **MAGREF works better with 121 frames @ 24 fps**
  - Testing shows improved performance at this specific frame count and fps setting
  - *From: ボグダンおじさん*

- **Preview capability allows quick iteration**
  - With lightx2v LoRA you can see what generation will look like in first or second step, allowing quick cancellation of bad looking ones
  - *From: crinklypaper*

- **MAGREF + ATI combination suggested for testing**
  - Kijai suggests trying MAGREF with ATI (moving points tech) together
  - *From: Kijai*

- **ComfyUI memory leak issue identified**
  - Workflows that worked for months now causing OOM with RAM on every run unless ComfyUI is restarted
  - *From: jeru*

- **Widget to string KJ node causes workflow resampling issues**
  - The node is set to re-run each time on purpose with specific code that makes any node re-evaluate on each queue, causing samplers to resample even with same parameters
  - *From: the_darkwatarus_museum*

- **UniPC scheduler provides significant quality jump with wrapper**
  - The quality improvement is likely due to wrapper's use of stateful FlowUniPCMultistepScheduler which isn't compatible with native ComfyUI
  - *From: phazei*

- **MagCache is faster and better than TeaCache**
  - With 5 steps, MagCache skips 2 of them and is somehow still faster than 3 steps without MagCache
  - *From: phazei*

- **MultiTalk can generate 177 frames without context tricks**
  - Audio-driven lip sync can generate long sequences in single pass, though their pipeline does three passes making it very slow
  - *From: Kijai*

- **Phantom samples extra reference frames**
  - When setting 81 frames, Phantom actually samples 89 frames because references are included in the sampled latents
  - *From: wowee*

- **LightX2V LoRA used at far too low shift values**
  - Should use 7.0 sigma_max and 100 shift with 2 sampler workflow for better motion and quality
  - *From: Ada*

- **Context window transitions cause cross fades with speed LoRAs**
  - 100% occurrence rate when using stack of LoRAs, less frequent with 8-step workflow
  - *From: blake37*

- **VACE mask requirements**
  - Needs RGB 123,123,123 exactly for gray fill, mask shape influences assumptions
  - *From: ingi // SYSTMS*

- **Native vs Wrapper speed difference resolved**
  - Initially showed 3x speed difference (4s/it vs 12s/it) but fixed after restart - speeds are equal when configured correctly
  - *From: jacinda*

- **Mixing T2V with Phantom allows better prompt adherence and produces output that regular T2V can't do**
  - Everything gets amplified, including stuff in long prompts that struggle to appear, but artifacts are also amplified. Use a small percentage of Phantom
  - *From: ▲*

- **Shift parameter relationship to sigma_max**
  - About 14 shift per 1.0 sigma was about right to balance the increase in sigma_max
  - *From: Ada*

- **High shift values create more motion and feel sped up**
  - Higher shift gives more movement and is a way to get 'more frames' for the same speed
  - *From: Ada*

- **NAG hurts movement**
  - User stopped using NAG because it reduced movement in generations
  - *From: Ada*

- **MagRef works better without clip vision for character likeness**
  - Character likeness is much higher when removing clip vision
  - *From: ボグダンおじさん*

- **One step Ultimate SD Upscale produces nearly identical results to four steps**
  - At denoise 0.4, visual difference between 1 step and 4 steps is minimal, saves significant time
  - *From: David Snow*

- **dpm_2_ancestral sampler with beta scheduler produces exceptional quality**
  - Described as 'exceptional' quality for Wan, though quite slow. Same combination also worked well with HunyuanVideo
  - *From: David Snow*

- **Multitalk uses 3 model predictions per step in original code**
  - Does positive, negative, and without audio predictions with 40 steps, making it extremely slow
  - *From: Kijai*

- **Multitalk has local audio attention**
  - Audio attention is very localized - background characters don't get animated by the audio
  - *From: Kijai*

- **Camera movement breaks multitalk contexting**
  - Moving camera disrupts the lip sync and animation quality
  - *From: Kijai*

- **UltraWan LoRA trained on 4K dataset**
  - Based on Wan-T2V-1.3B, small model size, works in any workflow
  - *From: yi*

- **Wan models perform worse past 81 frames without context windows**
  - Quality degrades when going beyond 81 frames unless using context windows
  - *From: Kijai*

- **1.3B model can be used for upscaling with good results**
  - Using specific workflows with MPS + HPS + Self Forcing LoRAs helps immensely since 1.3B was not trained on high quality dataset
  - *From: yi*

- **UltraWan LoRA enables 1k/4k resolution videos on Wan 1.3B T2V**
  - Generates high resolution videos but has CC4 non-commercial license due to YouTube dataset
  - *From: Alisson Pereira*

- **MultiTalk lip-sync works on 12GB VRAM**
  - Successfully generated 321 frames with 5 steps on 12GB card
  - *From: DawnII*

- **Custom node for automatic resolution optimization**
  - Node automatically finds optimal resolution for WanVideo and resizes input accordingly - 1920×1080 becomes 832×480 for 480p or 1280×720 for 720p
  - *From: 327467189525282816*

- **lightx2v scheduler preference dramatically affects results**
  - ddim_uniform scheduler is WAY better than simple/normal schedulers - others kill camera motion, seed variation, and style-based prompt adherence
  - *From: Screeb*

- **5090 performance with MultiTalk**
  - 1041 frames at 832x480 with 5 steps completed in 10:32 (126.45s/it), much faster without blockswapping
  - *From: Kijai*

- **uni3c can lock camera movement for context windows**
  - Using uni3c with just 32 overlap can lock camera position, reducing artifacts in context windows
  - *From: Kijai*

- **loudnorm is crucial for MultiTalk quality**
  - The model is likely trained with loudnorm, making it very important for proper results
  - *From: Kijai*

- **MultiTalk works primarily with English and Chinese**
  - Spanish doesn't work well, French seems to work. Audio language support is limited
  - *From: Juampab12*

- **Static camera videos work better for long context generation**
  - Using static camera reference videos reduces motion artifacts and repetitive behavior in long generations
  - *From: Juampab12*

- **Block swap memory usage scales with VRAM**
  - 16GB VRAM needs 6 blocks swapped, 24GB VRAM needs 25 blocks swapped
  - *From: Juampab12*

- **Audio sampling rate affects playback speed**
  - 48kHz audio plays slower in ComfyUI, converting to 44.1kHz fixes timing issues
  - *From: burgstall*

- **MultiTalk can handle edge cases like coughing and special sounds**
  - MultiTalk specifically picked up on arm raise and cough into sleeve actions, and handles various sound effects beyond just speech
  - *From: A.I.Warper*

- **MultiTalk works with T2V models**
  - Can use MultiTalk with T2V models like Phantom and VACE, though VACE code needs slight modifications
  - *From: Kijai*

- **MAGREF model works better than I2V for MultiTalk**
  - MAGREF gets much more freedom than I2V models and works way better with context windows
  - *From: Kijai*

- **MultiTalk can use multiple reference images**
  - Testing shows you can feed multiple images to MultiTalk for different angles/poses
  - *From: A.I.Warper*

- **Diffusers 0.33 required for Uni3C**
  - Need to update diffusers to version 0.33 to resolve 'No module named diffusers.models.transformers.transformer_wan' error
  - *From: Juampab12*

- **MultiTalk works with pure text-to-video using denoise 1**
  - Can generate lip-synced videos directly from text prompt and audio without needing input images
  - *From: hicho*

- **MAGREF model works in native ComfyUI without custom nodes**
  - I2V model that produces good likeness similar to Phantom, doesn't require wrapper nodes
  - *From: zelgo_*

- **Video-to-video with lower denoising values preserves more of original video**
  - The more you lower denoiser in ksampler the more you get output of the original video
  - *From: hicho*

- **Using input video guides even with light guidance improves results**
  - Results end up looking much better even if the guidance is light, gives dynamism from input video
  - *From: Ablejones*

- **UltraWan LoRA has two variants - 1k and 4k resolution**
  - High-res LoRA for 1.3B model trained on very high res content, 1k variant works but 4k causes black output
  - *From: VRGameDevGirl84*

- **NAG allows negative prompts with CFG=1 models**
  - New method that lets you use CFG-like functionality when CFG has to be 1, works for video generation
  - *From: JohnDopamine*

- **Wrapper workflows don't show the weird first few frames flash/grid thingy**
  - The flash/grid artifact seems to be built into the sampler node and only appears with high frame counts
  - *From: MilesCorban*

- **UltraWan 1k LoRA produces much cleaner results than 4k version**
  - 4k version duplicates things and produces garbage, while 1k works well at 6 steps and 1600x688 resolution
  - *From: David Snow*

- **GGUF models produce cleaner videos**
  - Native GGUF setup produces insanely clean results at 2-4 steps
  - *From: David Snow*

- **MultiTalk works with animals and draws realistic teeth**
  - Unlike FantasyTalking, MultiTalk can work with animals and properly draws cat teeth instead of human teeth
  - *From: N0NSens*

- **NAG affects entire composition, not just targeted elements**
  - Rejecting 'blonde hair' changed the entire video composition because NAG operates at conceptual level where hair color associates with lighting, environments, and other visual elements
  - *From: VRGameDevGirl84(RTX 5090)*

- **Fun InP MPS with LightX2V works at 3 steps**
  - Combination generates videos in 3 steps, but 4 steps produces buggy/noisy results
  - *From: Alisson Pereira*

- **Chinese-wav2vec2-base trained at 16fps, MagRef at 15fps**
  - Different frame rates between models may cause syncing issues, while MultiTalk Wav2Vec node hardcoded to 25fps
  - *From: Guey.KhalaMari*

- **44.1khz audio frequency is key for MultiTalk lip sync**
  - Using 44.1khz audio instead of default 48khz significantly improves lip synchronization quality
  - *From: burgstall*

- **MultiTalk works with solid black frame as input**
  - Can use a solid black frame as input image for MultiTalk instead of requiring a face image, useful for generating speakers from scratch
  - *From: burgstall*

- **Phone camera movement can drive Uni3C for organic motion**
  - Recording handheld camera movement with phone and feeding to Uni3C creates more organic movement than 3D rendered paths
  - *From: Nekodificador*

- **LightX2V may eliminate need for CausVid and AccVid**
  - Testing shows LightX2V alone provides same speed as using multiple LoRAs with better detail retention and less flux-face artifacts
  - *From: Thom293*

- **UltraWan 1K LoRA can work with Wan 14B through zero padding**
  - Expanding 2D LoRA weights from 1536x1536 to 5120x5120 by copying original values to upper left and filling rest with zeros allows some compatibility
  - *From: Alisson Pereira*

- **UltraWan + self-forcing works on Wan 1.3B**
  - Alisson Pereira tested UltraWan + self forcing for Wan 1.3B showing visible improvement
  - *From: Alisson Pereira*

- **Chatterbox provides voice cloning comparable to ElevenLabs**
  - Zero-shot voice cloning using short audio samples, performs TTS and voice-to-voice conversion
  - *From: VRGameDevGirl84(RTX 5090)*

- **MultiTalk supports video-to-video with lip sync**
  - Can take input video and apply lip sync while preserving video content
  - *From: VRGameDevGirl84(RTX 5090)*

- **Higher fps improves lip sync quality**
  - 48fps and 60fps with CFG 1 produce better lip sync than 30fps CFG 6
  - *From: patientx*

- **Self-forcing LoRA works with up to 4 steps, tested with 8 steps**
  - Self-forcing DMD can work with low step counts for acceleration
  - *From: Alisson Pereira*

- **T2V LoRAs on I2V can change style**
  - Using T2V LoRAs on I2V skips the input image but provides same context, allowing style changes
  - *From: hicho*

- **Wan 14B generates better at small resolutions like 350x350 without anime artifacts**
  - Unlike 1.3B which tends toward anime style at small resolutions
  - *From: hicho*

- **Wan v2v can upscale extremely low resolution videos effectively**
  - Successfully upscaled 160x90 video to 1280x720 and 385x216 to 1280x720 with good results using FusionX + LightX
  - *From: VRGameDevGirl84(RTX 5090)*

- **Denoise strength affects upscale quality dramatically**
  - 0.1-0.5 denoise keeps similar to original, 0.7+ removes pixelation better, 1.0 becomes creative upscale
  - *From: VRGameDevGirl84(RTX 5090)*

- **FusionX model performs better than base Wan for upscaling**
  - Base Wan with LightX looks more pixelated compared to FusionX with LightX for same upscaling task
  - *From: VRGameDevGirl84(RTX 5090)*

- **MultiTalk controlnet strength affects movement significantly**
  - 40% controlnet strength provides better movement than 100%, 0% gives too much movement but good character transformation
  - *From: Thom293*

- **More steps allows higher CFG values in LightX**
  - 12 steps enables CFG >1 which can be helpful, contrary to expectation that more steps would be 'fried'
  - *From: Piblarg*

- **Block swapping enables 1920x1080 upscaling on RTX 5090**
  - Using block swapping to manage memory, was able to upscale videos to 1920x1080 resolution
  - *From: VRGameDevGirl84(RTX 5090)*

- **MultiTalk works with 720p model**
  - MultiTalk lip sync works on 720p model, though settings may need adjustment
  - *From: burgstall*

- **Audio gain significantly improves MultiTalk results**
  - Turning up audio gain from default 1 to 2 or 3 dramatically improves lip sync quality, even picks up inhales and neck muscle movements
  - *From: Thom293*

- **LightX2V at 2.0 strength restores hand movements**
  - Cranking LightX2V to 2.0 strength brought back hand movements that were lost at lower settings
  - *From: burgstall*

- **Video to video upscaling much faster than Ultimate SD upscale**
  - Video to video workflow significantly faster than Ultimate SD upscale for same quality results
  - *From: VRGameDevGirl84(RTX 5090)*

- **UltraWan enables 1920x1080 generation with Wan 1.3b**
  - LoRA trained on 58.8k high-resolution videos to enable 1080p/4k video generation using Wan 1.3b model
  - *From: Alisson Pereira*

- **Non-diffusion upscaling can be very fast**
  - Non-diffusion upscale methods can be much faster - 138s for 81 frames scaling from 576x1024 x2
  - *From: The Shadow (NYC)*

- **MultiTalk can be combined with uni3C for camera movement**
  - The lipsync is in multitalk branch but camera movement is in master using uni3C, which can infer motion while keeping other inputs working
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Phantom can create full 3D character perspectives from single image**
  - Can create entire 3D perspective set with 2-3 phantom generations using rotation/pan prompts, then extract stills for character training
  - *From: Thom293*

- **WAN differential diffusion works automatically with inpainting**
  - Differential diffusion is automatically enabled for WAN inpainting without manual setup
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Video upscaling with context options works well**
  - Context options set to 121 with block swap 40 successfully processed 630 frames at 1024x576 using only 7.5GB max VRAM
  - *From: VRGameDevGirl84(RTX 5090)*

- **Uni3C has frame limitation**
  - Uni3C doesn't work above 81 frames, even with context window off
  - *From: burgstall*

- **MultiTalk error fix**
  - TypeError 'NoneType' object not callable was caused by wrong wav2vec model
  - *From: Draken*

- **MagRef tensor errors from aspect ratios**
  - 1024x600 causes tensor size mismatch errors, 1024x576 works fine
  - *From: MysteryShack*

- **Normal maps work better than depth for VACE**
  - Normal maps give better adherence and sharper outputs than depth maps, without color bleeding
  - *From: HeadOfOliver*

- **BlockSwap node improves results**
  - Just plugging in the blockswap node without swapping anything makes cloth simulation better
  - *From: HeadOfOliver*

- **GGUF models produce superior results**
  - Native workflows with GGUF models give better quality than wrapper versions
  - *From: David Snow*

- **UltraWan LoRA can be used for upscaling Wan videos**
  - Using 1.3B model with UltraWan LoRA to upscale 14B videos to FHD, shows subtle improvements in face, eyes, clothes and hands detail
  - *From: David Snow*

- **Color match node eliminates flash issues**
  - Color match node combined with other tweaks can eliminate the slight flash introduced during upscaling
  - *From: David Snow*

- **Removing CausVid causes generations to follow prompt less**
  - Removing causvid makes generations follow the prompt less, but doesn't seem to make quality difference otherwise
  - *From: blake37*

- **Image saturation node fixes color/brightness variation**
  - Adding image saturation node between decoder and video combine at 0.85-0.90 fixes color consistency issues and WAN flash
  - *From: Bleedy (Madham)*

- **Phantom can be used as text-to-image generator**
  - Need to create at least 9 frames and pick the last one, doesn't work well with less than 9 frames, similar to runway's frames or midjourney omni reference
  - *From: VRGameDevGirl84(RTX 5090)*

- **Rank 16 vs Rank 32 LoRA format differences**
  - Rank16 version caused brightness variation issues, switching formats within same LoRA can resolve problems
  - *From: Geoff*

- **FusionX can be used for video-to-video upscaling with high quality results**
  - Takes input video and processes through FusionX model, can add prompts for creative upscaling or use no prompt for enhancement
  - *From: VRGameDevGirl84(RTX 5090)*

- **Block swapping enables processing very long videos on consumer hardware**
  - 473 frames at 1024x576 running at only 20.6GB VRAM usage, meaning possible on 3090 cards at home
  - *From: samhodge*

- **WanVideoWrapper upscaler workflow shows dramatic quality improvements**
  - Significant enhancement of video quality, described as 'CSI Miami enhance' level improvement
  - *From: VRGameDevGirl84(RTX 5090)*

- **Context options critical for avoiding OOMs on longer sequences**
  - User was getting OOMs under 81 frames on 48GB card until enabling context options
  - *From: samhodge*

- **MultiTalk branch works better than expected**
  - Try the MultiTalk branch of Kijai's repo. Works way better than would have been guessed
  - *From: MilesCorban*

- **Wan14B with audio support released**
  - From LightX2V guys, appears to be a speech to video model
  - *From: yi*

- **14B LoRAs don't work on 1.3B models**
  - 14b loras can silently fail when loaded on 1.3B models, will look like it's loading but not give error in UI
  - *From: Draken*

- **Context overlap fixes MultiTalk loops on longer videos**
  - Setting context_overlap to around 64 on videos 321+ frames stops introducing extra loops
  - *From: Bleedy (Madham)*

- **Uni3C doesn't support context currently**
  - Major limitation for now is that uni3c doesn't support context
  - *From: ˗ˏˋ⚡ˎˊ-*

- **LightX2V realism is reduced compared to FusionX**
  - Realism is a bit lost with LightX VS fusionX lora settings
  - *From: VRGameDevGirl84(RTX 5090)*

- **Radial attention implementation coming to ComfyUI**
  - New optimization technique from MIT Han Lab coming soon
  - *From: ZeusZeus (RTX 4090)*

- **Using LightX LoRA at 1.0 strength with 4 steps produces significantly faster generation but less cinematic realism**
  - 77 seconds vs 129 seconds for same prompt/seed. Quality trade-off noted for text-to-video
  - *From: VRGameDevGirl84(RTX 5090)*

- **Context overlap affects consistency vs variation**
  - More overlap means more windows generated but more consistency, but also less opportunity for variation between flanking windows
  - *From: DawnII*

- **Q8 GGUF produces slightly nicer videos than regular models**
  - Based on extensive testing with human faces
  - *From: David Snow*

- **SageAttention causes slight quality degradation with graininess**
  - Comparison shows grainy artifacts when SageAttention is enabled
  - *From: zelgo_*

- **VACE 1.3B can generate in 6 seconds with CausVid or self-forcing 5 steps at 480p**
  - Fast generation possible at lower resolutions
  - *From: DawnII*

- **Wan VAE decoding requires context to properly decode video**
  - When clipping out a single frame from a latent video output, the decoded frame has distorted high saturation color/look (flash). With 5 frames clipped, first 2-3 frames flash then remaining look normal. At 10 frames, full clip decodes normal with no flashing.
  - *From: CJ*

- **Wan can be used as text-to-image generator**
  - Set frame count to 1 and use save image instead of video combine. Works almost on par with other T2I models and can avoid 'flux face'
  - *From: VRGameDevGirl84(RTX 5090)*

- **Denoise threshold affects reference image usage**
  - When using denoise with ref image: 0.80+ ignores ref image and creates new image, 0.79 and under actually uses the ref image
  - *From: VRGameDevGirl84(RTX 5090)*

- **Single frames render weird on WAN**
  - Better to repeat frame 5 times instead of generating just 1 frame
  - *From: burgstall*

- **Camera shake in I2V can be caused by specific settings**
  - Camera shake was caused by a particular setting, setting it to 0 removed the shake
  - *From: Juan Gea*

- **Turning up MPS to 1.00 helps with quality when doing text to image**
  - Setting moviigen/MPS to maximum strength improves quality for T2I generation
  - *From: VRGameDevGirl84(RTX 5090)*

- **VACE face consistency issues at resolutions below 1024x576**
  - VACE struggles with reference similarity and faces below certain resolution, unfortunately that resolution is higher than 1024x576 which is practical for most VRAM setups including 48GB
  - *From: MysteryShack*

- **LCM sampler + ddim_uniform scheduler fixes seed variation issues**
  - For native workflows, using LCM sampler with ddim_uniform scheduler fixes motion and style sensitivity issues that other schedulers kill
  - *From: Screeb*

- **Context overlap helps with videos longer than 5 seconds**
  - Wan doesn't support anything over 5 seconds without workarounds, but context overlap or using last frame of prior as input for next 5 seconds helps
  - *From: VK (5080 128gb)*

- **Tile lora upscaler can add significant detail**
  - Using tile lora with noise injection allows adding significant fine detail to upscaled videos, achieving true upscaling that doesn't change essence of original
  - *From: David Snow*

- **Align pose node can transfer poses across different scales/positions**
  - The align pose node can match ControlNet pose to position and scale of person in image, allowing pose transfer from any reference video regardless of aspect ratio/scale/position
  - *From: Jonathan*

- **New Sage Attention 2 Plus provides ~7% speed improvement on RTX 4090**
  - At 1280x768x81 frames around 7% faster, at 832x480x81 around 5% faster on 4090
  - *From: Kijai*

- **GGUF files provide slightly higher quality than safetensor versions**
  - David Snow confirmed quality is slightly higher with GGUF versions
  - *From: David Snow*

- **MAGREF works better with context windows than other I2V models**
  - Only I2V model that 'works' because it won't reset to init image on each window
  - *From: Kijai*

- **LightX2V performs better for I2V than T2V**
  - Multiple users report better results using LightX2V for image-to-video workflows
  - *From: VRGameDevGirl84(RTX 5090)*

- **CausVid V2 is only half the weights of original with attention layers only**
  - V2 version has first block removed entirely and is experimental concept by Kijai
  - *From: Kijai*

- **MPS LoRA provides significant quality improvement for Wan models**
  - Works with non-FUN models and makes a huge quality improvement
  - *From: VRGameDevGirl84*

- **Color Match node can help fix I2V color shifting**
  - When doing image to video, colors normally get darker after first frame. A ComfyUI color match node with reference image input can fix this quickly
  - *From: VRGameDevGirl84*

- **Context windows chunk sampling per step, not per batch**
  - On every step the model samples the amount of context windows determined by context window size, overlap, context method and overall frame count, then results are blended together
  - *From: Kijai*

- **VACE can work with MultiTalk but requires specific setup**
  - VACE uses T2V model while MultiTalk typically uses I2V, but they can work together with proper configuration
  - *From: VRGameDevGirl84*


## Troubleshooting & Solutions

- **Problem:** Depth control causing face morphing issues
  - **Solution:** Disable depth control and only use dwpose for better character consistency
  - *From: wange1002*

- **Problem:** Flux generating strange bars and lines at high resolution
  - **Solution:** Use Tiled Diffusion node and don't generate above 1 MP in 1 tile, or use Ultimate SD Upscale with proper tiling
  - *From: Colin*

- **Problem:** CausVid causing first frame glitching/artifacts
  - **Solution:** Use CausVid v1.5 which has block 0 disabled, or manually disable block 0 with block disable node
  - *From: JohnDopamine*

- **Problem:** Characters talking excessively or barely moving in Phantom
  - **Solution:** Add 'talking' to negative prompts, adjust steps (Q8 4 steps slows motion, 6 steps causes chattering)
  - *From: TRASHTRASH*

- **Problem:** Background flickering when using CausVid
  - **Solution:** Put a completely black or white image in one of the input nodes to stop flicker
  - *From: Thom293*

- **Problem:** Uni3C nodes not appearing despite being in main repo
  - **Solution:** User may have installed different branch - check ComfyUI-WanVideoWrapper main repo
  - *From: Nekodificador/Kijai*

- **Problem:** Fun reward LoRAs show console warnings but still work
  - **Solution:** Command window indicates it's not 100% happy but quality improvement is still significant
  - *From: Daviejg*

- **Problem:** VACE encoder stacking causes strength issues
  - **Solution:** Only the first node in encoder chain can have lower strength/step cutoffs - later nodes affect all previous encoders
  - *From: Neex*

- **Problem:** Normals and DW pose encoders won't stack together
  - **Solution:** Check for resolution mismatch between preprocessor outputs
  - *From: Neex*

- **Problem:** Facial hair interferes with mouth transfer/lip sync
  - **Solution:** Shaving improves mouth movement detection accuracy
  - *From: voxJT*

- **Problem:** Mouth movement detection unreliable
  - **Solution:** Use Detail Transfer node with mouth masking, though still not 100% reliable
  - *From: A.I.Warper*

- **Problem:** Hand motion blur in stylized outputs
  - **Solution:** 720p resolution shows small improvement over 576p for small details
  - *From: Piblarg*

- **Problem:** Using i2v workflow for VACE without i2v model
  - **Solution:** You need an i2v model for this workflow. If you want to use VACE, look at Kijai's examples in the WANVideoWrapper repo
  - *From: MilesCorban*

- **Problem:** Tensor mismatch error 'The size of tensor a (139) must match the size of tensor b (138)'
  - **Solution:** Check your clip model - the name may have changed. Re-download the clip file
  - *From: Valle*

- **Problem:** Dimensions causing errors
  - **Solution:** The dimensions need to be divisible by 16. 1114 is not (neither is 866)
  - *From: Kijai*

- **Problem:** OOM issues with bf16
  - **Solution:** Use fp8 models and turn all nodes to fp16. Never use bf16
  - *From: hicho*

- **Problem:** ComfyUI crashes when using context options without ref image
  - **Solution:** Context options requires a ref image in the last encode, otherwise it breaks ComfyUI process
  - *From: DeZoomer*

- **Problem:** First couple i2v frames distorted and bright
  - **Solution:** Reduce CausVid strength from 1.0 to 0.8
  - *From: GalaxyTimeMachine (RTX4090)*

- **Problem:** Model merge error with SkyReels
  - **Solution:** unet unexpected: ['model_type.SkyReels-V2-DF-14B-720P'] - compatibility issue between models
  - *From: VRGameDevGirl84(RTX 5090)*

- **Problem:** OOM when adding WAN Start/End Frame node to VACE workflows
  - **Solution:** Set block swapping beat to 40, reduce frame count
  - *From: amli*

- **Problem:** DWPose not detecting complex poses in ComfyUI
  - **Solution:** Try lowering keypoint threshold from 0.3 to 0 in wholebody.py
  - *From: Fannovel16 🇻🇳*

- **Problem:** VACE artifacts when reference image structure differs from input video
  - **Solution:** Reference image structure should match first frame of input video for better results
  - *From: VRGameDevGirl84(RTX 5090)*

- **Problem:** AttributeError: 'list' object has no attribute 'replace'
  - **Solution:** Code modifications needed in ComfyUI-WanVideoWrapper\ATI\nodes.py for trajectory handling
  - *From: Juampab12*

- **Problem:** LoRA keys not loading with MPS LoRA on Fun models
  - **Solution:** Works fine despite error messages - trained on Fun which has img attn channels
  - *From: DawnII*

- **Problem:** ATI only works with 81 frames, other frame counts fail with tensor shape errors
  - **Solution:** Use 81 frames as it's hardcoded in original implementation
  - *From: Adrien Toupet*

- **Problem:** ATI start/end percentage parameters not working
  - **Solution:** Bug fixed - parameter naming mismatch between 'percentage' and 'percent'
  - *From: Adrien Toupet*

- **Problem:** MPS LoRA errors with 1.3B model
  - **Solution:** Use correct model size - MPS LoRA is for 14B model
  - *From: Cubey*

- **Problem:** Green hue in ATI results
  - **Solution:** May be caused by LoRA combinations, try different LoRA settings
  - *From: Valle*

- **Problem:** Motion starts before trajectory begins in ATI
  - **Solution:** Add background static points to freeze camera and control unwanted motion
  - *From: Juampab12*

- **Problem:** SageAttention error on RTX 5080
  - **Solution:** Update Triton and SageAttention versions, ensure torch 2.7.0+
  - *From: Valle*

- **Problem:** 'vace_blocks.8.modulation' error when loading VACE
  - **Solution:** Nodes need updating for VACE 14B compatibility
  - *From: Kijai*

- **Problem:** 'WanModel' object has no attribute 'vace_patch_embedding'
  - **Solution:** Had wrong VACE model loaded, needed correct version
  - *From: Juan Gea*

- **Problem:** VACE only works with T2V message when using I2V
  - **Solution:** VACE has its own start frame process designed around T2V workflow
  - *From: Piblarg*

- **Problem:** UniPC causing lack of sharpness and ghosting/aura around characters
  - **Solution:** Switch to Euler, Euler A, or DPM++ 2M samplers for better quality
  - *From: Samuca*

- **Problem:** RTX 5090 TensorRT compatibility issues
  - **Solution:** Need CUDA Toolkit 12.9 or 12.8, look for 'sm_125' support in CUDA_COMPUTE_CAPABILITIES. When there's a new CUDA compute version it can take a while for NVIDIA and PyTorch to get in sync.
  - *From: samhodge*

- **Problem:** LoRA merging failed
  - **Solution:** Can't merge LoRAs if they target different layers - If LoRA 1 uses transformer.block.0.attn.q_proj.lora_A but LoRA 2 uses transformer.block.4.mlp.fc1.lora_A they don't stack, they sit separately unless merged directly into a base model
  - *From: VRGameDevGirl84(RTX 5090)*

- **Problem:** SageAttention Windows compatibility
  - **Solution:** Download from https://github.com/sdbds/SageAttention-for-windows/releases for Windows systems
  - *From: samhodge*

- **Problem:** VACE mask halo effect
  - **Solution:** Issue discussed but no specific solution provided - sometimes shows up, sometimes fine, rules unclear
  - *From: Ruairi Robinson*

- **Problem:** SageAttention SM8 kernel error on RTX 5080
  - **Solution:** Install SageAttention 2.1.1 from woct0rdho's Windows releases with bundled CUDA, update Triton to 3.3, change attention mode from auto to specific mode
  - *From: Kijai/lomerio*

- **Problem:** Black output videos in I2V
  - **Solution:** Wan I2V wouldn't work on 'auto' attention mode - try first mode after auto
  - *From: Kijai*

- **Problem:** Violent shake in generated video
  - **Solution:** Too low resolution (368x720) and too little frames - increase both
  - *From: Kijai*

- **Problem:** Generations getting stuck
  - **Solution:** Check GPU memory and utilization - likely silent OOM failure. Use blockswap or shut down other GPU memory apps
  - *From: blake37*

- **Problem:** CFG Schedule causing 10x slowdown
  - **Solution:** Ignore batched_cfg for any model besides 1.3B - it uses more VRAM and is only viable for cloud GPUs on 14B models
  - *From: Kijai*

- **Problem:** CFG schedule 'list index out of range' error
  - **Solution:** If starting cfg schedule at 1.0 causes error, start at 1.01 instead
  - *From: toyxyz*

- **Problem:** Spline handles appearing as circles instead of parallel
  - **Solution:** Make sure not in 'path' mode and update wrapper nodes
  - *From: Kijai*

- **Problem:** Only getting one track out of 3 spline editors
  - **Solution:** May be caused by recent KJnodes update, try updating
  - *From: Johnjohn7855*

- **Problem:** Uni3C model error
  - **Solution:** Need diffusers 0.33 or newer
  - *From: Kijai*

- **Problem:** Vace inpainting halo artifacts
  - **Solution:** Use correct gray value for the shot, lower the value to remove halo
  - *From: chrisd0073*

- **Problem:** Regular Wan model not working with Uni3C
  - **Solution:** Must use ATI model for trajectory control
  - *From: Juampab12*

- **Problem:** ATI with Spline Editor not working
  - **Solution:** Frames and spline points to sample needs to match
  - *From: Nekodificador*

- **Problem:** CausVid looking 'fake'
  - **Solution:** Usually caused by CausVid and AccVid strengths set too high
  - *From: Johnjohn7855*

- **Problem:** System memory fills up and dies during sampling
  - **Solution:** Block swap would only help so much since ram gets so full by the end of sampling; comfy just dies when trying to load the vae
  - *From: TK_999*

- **Problem:** Torch compile disables loras in native wrapper
  - **Solution:** Try disabling torch compile node
  - *From: boorayjenkins*

- **Problem:** Mat error when using merge in Native
  - **Solution:** Change resolution maybe, or check workflow settings
  - *From: Thom293*

- **Problem:** High contrast/overcooked colors with high accvid
  - **Solution:** Raise causvid strength to fix overcooked colors that high accvid strengths cause
  - *From: Jonathan*

- **Problem:** Fast motion gets messed up with 3 steps
  - **Solution:** Raise accvid strength to 2 and up for 2-3 steps to work
  - *From: Jonathan*

- **Problem:** OOM on sampling with high frame counts
  - **Solution:** Use --reserve-vram 2 startup argument
  - *From: The Punisher*

- **Problem:** Workflow corruption when sharing with Get/Set nodes
  - **Solution:** Issue traced to purge VRAM nodes causing API calls and model reloads, remove cache clearing nodes to fix loading
  - *From: AJO*

- **Problem:** Hair falls apart and looks stringy with VACE
  - **Solution:** Try different control nets (pose, depth, canny), use higher steps, add accvid and mps lora, check ref image quality
  - *From: Jonathan*

- **Problem:** OOM with VACE workflows
  - **Solution:** Switch to GGUF models for better VRAM management, Q4 gives 20GB more memory
  - *From: lomerio*

- **Problem:** Characters always talking regardless of prompted scene
  - **Solution:** Add 'talking, conversation' to negative prompts or hunt for good seed. If using CFG1, negatives don't work
  - *From: Johnjohn7855*

- **Problem:** Instant OOM when trying to split VACE ref_image embed
  - **Solution:** Try tiling VACE encode, use GGUF text encoder and GGUF VACE model
  - *From: DawnII*

- **Problem:** Over-saturation at end of video generations
  - **Solution:** Set CFG to 1 when using certain merged models, avoid CFG scheduling with some models
  - *From: VRGameDevGirl84(RTX 5090)*

- **Problem:** Uni3C causing tensor errors
  - **Solution:** No specific solution provided, user couldn't get workflow running
  - *From: The Dude*

- **Problem:** AccVid T2V LoRA causing saturation/contrast issues at high strengths
  - **Solution:** Use AccVid I2V LoRA instead, which doesn't have these issues even at higher strengths
  - *From: Jonathan*

- **Problem:** Hair artifacts in generated videos
  - **Solution:** Lower shift values (1-2 range) and use 4+ steps instead of 3 steps
  - *From: The Punisher*

- **Problem:** Mouth segmentation fails on low resolution video
  - **Solution:** Use pose landmark coordinates instead of segmentation for reliable mouth tracking
  - *From: A.I.Warper*

- **Problem:** Video Depth Anything causing OOM errors
  - **Solution:** Modified version that properly offloads model to CPU after inference to free VRAM
  - *From: A.I.Warper*

- **Problem:** Enhanced video processing being too slow
  - **Solution:** Enhanced processing has minimal speed impact when properly implemented - if slow, check for broken patches
  - *From: Kijai*

- **Problem:** 4 channel error in VACE
  - **Solution:** Remove alpha channel from input images - error indicates presence of alpha channel
  - *From: Kijai*

- **Problem:** OOM errors with wrapper
  - **Solution:** Use block swap feature for manual memory management, or switch to native workflows which have automated memory management
  - *From: Kijai*

- **Problem:** Halos/outlines in VACE inpainting
  - **Solution:** Lower the mask values and avoid feathering the mask - similar to greenscreen compositing
  - *From: chrisd0073*

- **Problem:** Control video not working with combined controls
  - **Solution:** Don't combine lineart and depth controls - use separate VACE encodes instead
  - *From: David Snow*

- **Problem:** VAE noise/artifacts in generations
  - **Solution:** Switch T5 text encoder and VAE to FP32 precision instead of quantized versions
  - *From: ingi // SYSTMS*

- **Problem:** VACE pose control showing through in render
  - **Solution:** Drop the blend factor to 0.9 or lower to fix it
  - *From: CaptHook*

- **Problem:** Depth control introducing background elements from driving video
  - **Solution:** Isolate the subject in driving video by masking out the background
  - *From: CaptHook*

- **Problem:** ComfyUI frontend update broke spline editor causing freezing
  - **Solution:** Update to latest KJNodes to fix the freezing issue
  - *From: Kijai*

- **Problem:** partial_add_cond error when using WanVideo Context Options
  - **Solution:** Error occurs when context options node hits sampler, disappears when context options disabled
  - *From: voxJT*

- **Problem:** WanVideoWrapper showing as N/A in ComfyUI Manager
  - **Solution:** Frontend update issue, needs ComfyUI fix or update KJNodes
  - *From: CaptHook*

- **Problem:** Invisible nodes in ATI workflow causing ComfyUI to freeze
  - **Solution:** Update KJNodes or try different workflow, problem occurs when ComfyUI can't load certain nodes
  - *From: the_darkwatarus_museum*

- **Problem:** ModuleNotFoundError: No module named 'diffusers.models.transformers.transformer_wan'
  - **Solution:** Need diffusers 0.33 or higher
  - *From: Kijai*

- **Problem:** ComfyUI Manager shows nodes as N/A and freezing/disappearing
  - **Solution:** Change security to 'Weak' in ComfyUI-Manager/config.ini
  - *From: AJO*

- **Problem:** TypeError: FlowMatchEulerDiscreteScheduler.__init__() got an unexpected keyword argument 'use_beta_sigmas'
  - **Solution:** Kijai acknowledged this as his mistake and will fix it
  - *From: Kijai*

- **Problem:** WAN Context Options causing issues
  - **Solution:** Kijai acknowledged this as his mistake and will fix it
  - *From: Kijai*

- **Problem:** Phantom with uni3c tensor size mismatch
  - **Solution:** uni3c is only for I2V models and Phantom is technically T2V model - they're incompatible
  - *From: Kijai*

- **Problem:** Color shift when extending videos with DF
  - **Solution:** Use Kijai's color match node and add color filters after
  - *From: Colin*

- **Problem:** CUDA errors after updating to CUDA 12.9-1 and pytorch 2.7.1
  - **Solution:** Use --disable-cuda-malloc flag when starting ComfyUI
  - *From: makeitrad*

- **Problem:** Block swap causing CUDA issues
  - **Solution:** Set use non-blocking to false in block swap settings
  - *From: ZeusZeus (RTX 4090)*

- **Problem:** Wan wrapper appearing to reload model when changing LoRA settings
  - **Solution:** Setting to main device would keep it loaded instead of offloading
  - *From: the_darkwatarus_museum*

- **Problem:** Getting patches of noise in outputs with patterned textures
  - **Solution:** Tried increasing causvid, accvid, enhance-a-video strength, steps and shift but none worked
  - *From: Johnjohn7855*

- **Problem:** VACE inpainting with phantom showing white frames or gray canvas
  - **Solution:** Issue occurs when combining VACE inpainting/control video input with phantom while running causvid
  - *From: Johnjohn7855*

- **Problem:** ATI and Uni3C balance issues
  - **Solution:** For uni3c to work, had to remove all static points for ATI first, otherwise uni3c had no effects
  - *From: Johnjohn7855*

- **Problem:** Tensor size mismatch when using reference images
  - **Solution:** Reference image setup needs 1 less latent to match up properly
  - *From: Piblarg*

- **Problem:** ATI node errors after updates
  - **Solution:** Need to update both wrapper and KJNodes - output format changed when multiple splines support was added
  - *From: Kijai*

- **Problem:** Euler sampler too blurry with Causvid at 6 steps
  - **Solution:** Change to dpmpp_2m sampler, euler does not converge quickly enough
  - *From: Thom293*

- **Problem:** VRAM hitting 100% causes slowdown
  - **Solution:** Use startup argument --reserve-vram 2 to leave 2GB more VRAM free
  - *From: Kijai*

- **Problem:** TeaCache and VACE compatibility
  - **Solution:** Fixed in updated patch nodes - TeaCache was broken and disabled VACE
  - *From: Kijai*

- **Problem:** Self-forcing model won't load in ComfyUI
  - **Solution:** Model needs conversion from subdict structure - use Kijai's conversion script or update wrapper to handle model. prefix
  - *From: Kijai*

- **Problem:** Screen door effect in high-frequency detail areas
  - **Solution:** Use more steps (30+), DPM++_SDE sampler, avoid VAE tiling, or use Skip Layer Guidance as second pass
  - *From: multiple users*

- **Problem:** Real-time generation not working with self-forcing
  - **Solution:** Real-time not achievable - even at 512px resolution still needs 1.3+ seconds per frame, limit is about 6fps
  - *From: slmonker*

- **Problem:** TeaCache acting strange after update
  - **Solution:** Set start percent to 0.03 (was previously showing as 3%)
  - *From: DawnII*

- **Problem:** ComfyUI disconnecting during generation
  - **Solution:** Update the wrapper - David Snow confirms it works fine in updated wrapper
  - *From: David Snow*

- **Problem:** Flash attention taking hours to install
  - **Solution:** Version 1 takes hours, version 2 installs much faster - use version 2 or find pre-built wheel
  - *From: Charlie*

- **Problem:** Flashing/artifacts at video start
  - **Solution:** Use node to remove first 3-4 latent frames, or prepare control videos with extra frames at start
  - *From: JohnDopamine*

- **Problem:** Self-Forcing OOM on 5090
  - **Solution:** May need to use fp8 precision or adjust settings - still being investigated
  - *From: orabazes*

- **Problem:** Using checkpoint loader on diffusion model wastes VRAM
  - **Solution:** Don't use checkpoint loader function on diffusion models in ComfyUI - use proper diffusion model loader
  - *From: Clownshark Batwing*

- **Problem:** Invalid WanVideo model selected error
  - **Solution:** Update the wrapper
  - *From: N0NSens*

- **Problem:** Torch compile issues
  - **Solution:** Don't use torch compile
  - *From: hicho*

- **Problem:** Cache issues
  - **Solution:** Clear cache by deleting triton folder in temp folder
  - *From: Mads Hagbarth Damsbo*

- **Problem:** ControlNet tensor size mismatch with Phantom
  - **Solution:** Need to pad control frames since Phantom adds latent(s)
  - *From: Kijai*

- **Problem:** Multiple spline editor not working
  - **Solution:** Update KJNodes to latest version
  - *From: Nathan Shipley*

- **Problem:** Self-forcing i2v conversion
  - **Solution:** Use Kijai's conversion script to convert self_forcing_dmd.pt to safetensors format
  - *From: Jonathan*

- **Problem:** VACE struggles with character consistency when combined with control or style loras
  - **Solution:** Use VACE alone without other controls for better character preservation, or train character-specific loras
  - *From: Piblarg*

- **Problem:** Context window creates discontinuous video generation
  - **Solution:** Multiple attempts needed for consistency, still struggles with maintaining details like sleeve length across sections
  - *From: Ruairi Robinson*

- **Problem:** Low quality results with fp8 models and distillation loras
  - **Solution:** Increase steps or increase strength on distillation loras like CausVid
  - *From: Kijai*

- **Problem:** VACE encoder strength affects camera movement vs lighting control
  - **Solution:** Lower strength gives better prompt control but less camera following, higher strength locks in reference look but reduces lighting flexibility
  - *From: Ruairi Robinson*

- **Problem:** Missing matplotlib library for points editor
  - **Solution:** pip install matplotlib
  - *From: Juampab12*

- **Problem:** CUDA out of memory on WanVideoSampler
  - **Solution:** Try increasing blocks to 30 to test if VRAM is sufficient
  - *From: VK (5080 128gb)*

- **Problem:** ComfyUI doesn't see models in subfolders
  - **Solution:** Need to manually re-select them in workflows, checking subfolders for same filename is complex
  - *From: Ruairi Robinson*

- **Problem:** OOM with multiple VACE embeds
  - **Solution:** Must use VACE block swap and at least single VACE block. With block swap enabled, results move to offload_device so should only use more RAM
  - *From: Kijai*

- **Problem:** Torch out of memory vs allocation error
  - **Solution:** If torch out of memory (NOT allocation) it's RAM - disable non-blocking transfers and maybe offload less blocks
  - *From: Kijai*

- **Problem:** Start/End frame node causing OOM crashes
  - **Solution:** Remove the node or enable block swap, crashes happen when inputs are too large for memory
  - *From: amli*

- **Problem:** Flowmatch_causvid dimension error after updates
  - **Solution:** Scheduler shouldn't be used outside of actual causvid sampling
  - *From: DiXiao*

- **Problem:** ComfyUI performance issues and OOM
  - **Solution:** Roll back ComfyUI to previous version, recent updates causing problems
  - *From: JohnDopamine*

- **Problem:** CFG schedule float list error in T2V
  - **Solution:** Context issue - 'NoneType' object not iterable error in T2V workflows
  - *From: Zlikwid*

- **Problem:** Group nodes ignore LoRAs
  - **Solution:** Issue with set/get nodes not working with group nodes, use direct connections instead
  - *From: MatiaHeron*

- **Problem:** VACE color shift in extensions
  - **Solution:** Try lowering causvid to 0.7, use 30 steps without causvid, change seed by one, remove ref input for extensions
  - *From: chrisd0073*

- **Problem:** 576x1024 resolution maxing out VRAM in new workflow vs old working one
  - **Solution:** Use block swap - the new sampler needs more VRAM management
  - *From: Kijai*

- **Problem:** NAG node increases memory usage by 1.2GB and slows computer
  - **Solution:** NAG does two attention passes holding first results in memory, causing extra VRAM usage
  - *From: Kijai*

- **Problem:** ComfyUI broken after installing MAG and NAG
  - **Solution:** Not explicitly resolved in chat
  - *From: ▲*

- **Problem:** Phantom degrades quality of 14B model
  - **Solution:** Try merging Phantom with T2V model at 0.15-0.25 strength instead of using pure Phantom
  - *From: ▲*

- **Problem:** Kijai wrapper freezing and requiring reboot when stopping inference
  - **Solution:** Connect main model to model_to_offload input on text encoder node to prevent VRAM issues
  - *From: Kijai*

- **Problem:** CausVid does not work well with self-forcing model
  - **Solution:** Avoid using CausVid with self-forcing model regardless of strength settings
  - *From: Jonathan*

- **Problem:** Torch compiler only works with fp8_e5m2
  - **Solution:** Use fp16 model and let the node quantize it, don't use pre-quantized fp8 models with e5m2
  - *From: HeadOfOliver*

- **Problem:** Reference images hit or miss with VACE
  - **Solution:** Be quite specific with prompts when using reference images
  - *From: David Snow*

- **Problem:** Characters randomly spawning at same location in i2v workflows
  - **Solution:** Check autoprompt connections - may be trying to generate multiple characters from single person prompt
  - *From: David Snow*

- **Problem:** Mouth won't stop moving in generated videos
  - **Solution:** Try DPM++ scheduler, raise shift parameter, or exclude 'talking' token from prompts
  - *From: VK (5080 128gb)*

- **Problem:** Kontext API nodes throw errors with first frame
  - **Solution:** Use remove image alpha node - API outputs image with alpha channel
  - *From: Flipping Sigmas*

- **Problem:** NAG causing OOM on 4090 after few hours
  - **Solution:** Issue occurs even with decent free VRAM and only 20 blocks swapped
  - *From: ezMan*

- **Problem:** Wan2.1 controlnet tensor size mismatch
  - **Solution:** Check actual sizes after resize nodes, width/height need to be divisible by 16. 853 height was problematic
  - *From: Kijai/BondoMan*

- **Problem:** UniAnimate 'WanModel' object has no attribute 'dwpose_embedding'
  - **Solution:** Load the UniAnimate lora
  - *From: BondoMan*

- **Problem:** First frame/last frame workflow loops first image instead of ending on second
  - **Solution:** Adjust ClipVision Encode ratio and strength settings, reduce strength_1 to 0.8
  - *From: Guey.KhalaMari*

- **Problem:** OOM and flaky performance with Native nodes
  - **Solution:** Use --cache-none in combination with --disable-smart-memory
  - *From: JohnDopamine*

- **Problem:** ComfyUI memory management issues
  - **Solution:** Use janky_memory_patcher node to override comfy's memory management
  - *From: TK_999*

- **Problem:** Triton permission error
  - **Solution:** Follow Reddit fix for sudden Triton error
  - *From: Dream Making*

- **Problem:** Color mismatch in VACE looping
  - **Solution:** No clear solution found, can try blending latents or color correction in post
  - *From: Piblarg*

- **Problem:** NAG corrupts output with self-forcing models
  - **Solution:** Issue identified but no solution provided
  - *From: jacinda*

- **Problem:** Native i2v test looks nothing like source image
  - **Solution:** Check if using correct i2v model vs VACE
  - *From: hicho*

- **Problem:** NAG + torch compile error
  - **Solution:** Delete folder c:\Users\******\AppData\Local\Temp\torchinductor_******
  - *From: N0NSens*

- **Problem:** FP8 error on RTXA5000
  - **Solution:** GPU can't do FP8, need to choose another model or use e5m2 version instead
  - *From: Tomber*

- **Problem:** Ultimate SD upscale tensor size mismatch error
  - **Solution:** Try disabling the trim latent node - may be trimming video to incompatible frame count
  - *From: David Snow*

- **Problem:** VACE interpreting flashing lights as masks
  - **Solution:** May need to resort to other means like denoisers in Nuke
  - *From: A.I.Warper*

- **Problem:** Can't get self-forcing model working alone
  - **Solution:** Add causvid lora - couldn't get variety of strength or sampler to work with just the lora alone
  - *From: DawnII*

- **Problem:** Self-forcing with phantom breaks down at 6 steps
  - **Solution:** Use 4-5 steps maximum with phantom
  - *From: DawnII*

- **Problem:** White specs/noise artifacts appearing in renders with LightX2V
  - **Solution:** Issue resolved by using correct step count (4 steps) instead of higher values like 8 steps
  - *From: A.I.Warper*

- **Problem:** LightX2V giving pure noise at 4 steps with Shift 1
  - **Solution:** Use higher shift values like 5 or 8 instead of shift 1
  - *From: MilesCorban*

- **Problem:** Flashes in video generation when using CausVid below strength 1
  - **Solution:** Set new LightX2V LoRA to strength 1.0 and use LCM scheduler to eliminate flashes
  - *From: chrisd0073*

- **Problem:** VRAM overflow causing slow block swap
  - **Solution:** Use merged models instead of loading multiple LoRAs to reduce VRAM overhead, and run VACE at largest possible resolutions
  - *From: MysteryShack*

- **Problem:** CFG scheduling NoneType error
  - **Solution:** Return to default text encode node instead of using wanvideo textencodesingle node with NAG
  - *From: ボグダンおじさん*

- **Problem:** ComfyUI memory management accumulating RAM
  - **Solution:** Need to reboot ComfyUI after one or two runs when changing LoRA settings due to RAM accumulation
  - *From: David Snow*

- **Problem:** MinimaxRemover masked image error
  - **Solution:** Masked image needs to be gray, just like VACE. Update WanVideoWrapper to fix the bug
  - *From: Kijai*

- **Problem:** Multiple reference images creating nightmare fuel
  - **Solution:** Use seed hunting to improve results when using multiple images of same person with MAGREF
  - *From: David Snow*

- **Problem:** Ultimate SD Upscale only outputting single image instead of video
  - **Solution:** Need to plug in the upscale model - it's not optional as initially thought
  - *From: David Snow*

- **Problem:** Ultimate SD Upscale murdering PC
  - **Solution:** Change default tile size from 512 to 256 in custom_nodes\comfyui_ultimatesdupscale\modules\processing.py
  - *From: David Snow*

- **Problem:** CFG Schedule Float List causing 'NoneType' object not iterable error
  - **Solution:** Can't use TextEncodeSingle node with CFG - need to use regular TextEncode nodes
  - *From: Kijai*

- **Problem:** NAG not working with CFG scheduling
  - **Solution:** Don't use TextEncode single node with NAG, use the combined output from NAG node
  - *From: Zlikwid*

- **Problem:** Phantom model causing excessive mouth movement
  - **Solution:** Use reference image with closed mouth and add facial expression descriptions to prompt
  - *From: ingi // SYSTMS*

- **Problem:** VRAM constantly maxing out after ComfyUI updates
  - **Solution:** Restart ComfyUI between runs to clear memory leaks
  - *From: blake37*

- **Problem:** Widget to string node causing workflow resampling
  - **Solution:** Comment out or delete the 3 lines of code that force re-evaluation on each queue in nodes.py file
  - *From: Kijai*

- **Problem:** SLG not working with wrapper
  - **Solution:** Set SLG start to 0 instead of 0.2 when using denoise, as ComfyUI handles denoise differently than diffusers
  - *From: Kijai*

- **Problem:** Video output 2 frames short when using controlnets
  - **Solution:** Issue may be related to shift value, CFG, or SLG cutting off last frames
  - *From: AI_Fan*

- **Problem:** ATI compatibility with last frame causing tensor size mismatch
  - **Solution:** Drop 4 frames from generation frame count as last frame adds a latent causing mismatch
  - *From: Kijai*

- **Problem:** NAG causing 'NoneType' object is not iterable error
  - **Solution:** Can't use single encode with CFG - need two prompts as main embeds or set CFG to 1.0
  - *From: Kijai*

- **Problem:** Context window cross fades with speed LoRAs
  - **Solution:** More overlap may help, but context windows only work with tight motion control
  - *From: Kijai*

- **Problem:** VACE adding unwanted subjects in mask
  - **Solution:** Use gray fill RGB 123,123,123 exactly, use box instead of human-shaped mask, save as image sequence not mp4
  - *From: ingi // SYSTMS*

- **Problem:** OOM errors with 32GB VRAM
  - **Solution:** Use offload_device for anything under 80GB VRAM with 14B model, force_offload=true on text encoders
  - *From: Kijai*

- **Problem:** NAG compilation error on Windows
  - **Solution:** Clear triton cache at C:\Users\username\.triton, may need pip install triton-windows
  - *From: Kijai*

- **Problem:** Progressive color burning in video extension
  - **Solution:** Add color match node after each VAE decode, match to initial frame
  - *From: MilesCorban*

- **Problem:** VRAM Management node causing errors
  - **Solution:** Bypass the VRAM Management node
  - *From: AmirKerr*

- **Problem:** Windows path length issue with Triton
  - **Solution:** Edit cache.py and add [:8] after rnd_id in temp_dir line
  - *From: Nekodificador*

- **Problem:** VACE mask not working properly with shadows
  - **Solution:** Make sure mask is big enough and doesn't include shadows from masked objects
  - *From: Fawks*

- **Problem:** Hip OOM with wrapper nodes in T2V
  - **Solution:** Use ComfyUI native nodes instead of wrapper for T2V, wrapper works better for I2V
  - *From: patientx*

- **Problem:** Camera movement not working with masked video input
  - **Solution:** Try generating full canvas without mask then compositing and re-diffusing
  - *From: seb bae*

- **Problem:** 'NoneType' object is not callable error with multitalk
  - **Solution:** Need to use the Chinese wav2vec model instead of the English one
  - *From: Kijai*

- **Problem:** Out of memory with multitalk on AMD
  - **Solution:** Try disabling non_blocking transfers and adjusting block swap settings
  - *From: Kijai*

- **Problem:** Teacache causing issues with multitalk
  - **Solution:** Remove teacache entirely - it probably doesn't trigger with low steps and can cause problems
  - *From: Kijai*

- **Problem:** Differential diffusion darkening characters in Wan
  - **Solution:** Try using native implementation instead of wrapper nodes, or adjust mask strength
  - *From: A.I.Warper*

- **Problem:** VACE inpainting not working
  - **Solution:** Make sure noise is enabled - disabling noise breaks the process
  - *From: Piblarg*

- **Problem:** Color shifting in video extensions
  - **Solution:** Use color matching node to match to original reference image
  - *From: MilesCorban*

- **Problem:** huggingface_hub LocalEntryNotFoundError for Wav2VecModel
  - **Solution:** Use huggingface-cli login then huggingface-cli download TencentGameMate/chinese-wav2vec2-base --local-dir . Also pip install pyloudnorm
  - *From: Purz*

- **Problem:** fp8 e4m3fn can be finicky on 3090
  - **Solution:** Use e5m2 instead of e4m3fn on 3090 cards
  - *From: Purz*

- **Problem:** ComfyUI Manager broken with WanVideoWrapper nodes
  - **Solution:** Delete old folder and install manually
  - *From: CaptHook*

- **Problem:** Multitalk error 'expected input to have 16 channels, but got 36 channels'
  - **Solution:** Need to use I2V model instead of T2V model
  - *From: Kijai*

- **Problem:** VACE color shift/oversharpen when extending videos
  - **Solution:** Use specific settings with denoise 0.4-0.6, then use DaVinci Resolve Magic Mask subject inverted to blur/tweak background
  - *From: CaptHook*

- **Problem:** OOM error during decoding due to clamp operation on GPU
  - **Solution:** Modified code to move clamp operation off GPU
  - *From: Kijai*

- **Problem:** Uni3c tensor size mismatch error
  - **Solution:** Ensure uni3c video dimensions match starting frame dimensions exactly
  - *From: Juampab12*

- **Problem:** Audio timing issues in MultiTalk
  - **Solution:** Convert audio from 48kHz to 44.1kHz for proper sync
  - *From: burgstall*

- **Problem:** MultiTalk requires diffusers>=0.33
  - **Solution:** Update diffusers to version 0.33 or higher
  - *From: Kijai*

- **Problem:** Context window jumps in long videos
  - **Solution:** Use uni3c repeat with low strength to maintain consistency
  - *From: Juampab12*

- **Problem:** Frame size crashes with certain dimensions
  - **Solution:** 636x636 crashes but 631x631 works fine - avoid specific problematic dimensions
  - *From: AJO*

- **Problem:** Windows users experiencing performance issues with MultiTalk
  - **Solution:** Turn off Discord/streaming/everything and ensure not maxing out VRAM. First run may be bad but subsequent runs should be fine
  - *From: Purz*

- **Problem:** AttributeError: 'VaceWanAttentionBlock' object has no attribute 'audio_cross_attn'
  - **Solution:** VACE code needs slight change to work with MultiTalk
  - *From: Kijai*

- **Problem:** Uni3C error 'No module named diffusers.models.transformers.transformer_wan'
  - **Solution:** Update diffusers to 0.33 or use pip update diffusers
  - *From: Juampab12*

- **Problem:** MultiTalk nodes not updating through manager
  - **Solution:** Use git pull instead of manager updates. Switch to multitalk branch with 'git checkout multitalk' then 'git pull'
  - *From: AJO*

- **Problem:** MMAudio generating unwanted vocal background noise
  - **Solution:** Use vocal separator tools like Ultimate Vocal Remover or deepextract nodes to remove vocals from background
  - *From: JohnDopamine*

- **Problem:** OOM errors with WAN encoder at higher frame counts
  - **Solution:** Keep frame counts below 500 to avoid GPU memory issues, though some users report success at 2k frames
  - *From: A.I.Warper*

- **Problem:** OOM with high frame counts during VAE decode
  - **Solution:** VRAM issue, tensor on GPU during clamp operation on decode node, needs more VRAM (worked on 5090 with 2k frames)
  - *From: Kijai*

- **Problem:** Flash at start of videos with higher frame counts
  - **Solution:** More frames causes flash at start, avoid going over 81 frames for T2V, use multiples of 4+1 for frame counts
  - *From: VRGameDevGirl84*

- **Problem:** Wav2Vec tokenizer loading error
  - **Solution:** Missing tokenizer files (tokenizer_config.json, vocab.json, special_tokens_map.json), manually download from HuggingFace
  - *From: VRGameDevGirl84*

- **Problem:** UltraWan 4k LoRA causing black output
  - **Solution:** Use 1k variant instead, 4k variant not working properly in ComfyUI
  - *From: VRGameDevGirl84*

- **Problem:** VideoHelperSuite color shift issue
  - **Solution:** Loading and resaving same video makes it more red each time with h264-mp4
  - *From: hablaba*

- **Problem:** Lipsync fails with longer videos
  - **Solution:** Limited to around 69 frames with 41 context, longer durations break consistency and lipsync
  - *From: ZRNR*

- **Problem:** Weird motion artifacts in high frame count generations
  - **Solution:** Use Wrapper workflows instead of native nodes to avoid first frame flash/grid artifacts
  - *From: MilesCorban*

- **Problem:** MagRef with MultiTalk causing OOM on 3090 48GB RAM
  - **Solution:** Try block swap up to 40, use low_mem_load on LoRA loader, or stick with base I2V model
  - *From: Guey.KhalaMari*

- **Problem:** UltraWan 4k LoRA producing duplicated/garbage results
  - **Solution:** Use the 1k version instead, which works much better
  - *From: David Snow*

- **Problem:** Fun InP MPS becoming buggy at 4 steps
  - **Solution:** Use exactly 3 steps for clean results
  - *From: Alisson Pereira*

- **Problem:** CausVid strength too high for T2V 1.3B
  - **Solution:** Lower CausVid strength to 0.5 for better results
  - *From: Alisson Pereira*

- **Problem:** MultiTalk only using first image in looping setup
  - **Solution:** Need to loop both text prompts and images for MultiTalk, not just the prompts
  - *From: AJO*

- **Problem:** Flux face/chin dimple persisting despite NAG
  - **Solution:** Try NAG prompts like 'pointy chin, sharp chin, cleft chin, chin dimple' but effect varies by seed
  - *From: VRGameDevGirl84(RTX 5090)*

- **Problem:** Tensor errors when connecting Flux Kontext to MultiTalk in loops
  - **Solution:** RGBA vs RGB channel mismatch - ensure all images have same number of channels before concatenation
  - *From: AJO*

- **Problem:** Generation time slows drastically after 10-15 generations
  - **Solution:** Common issue affecting many users, time changes from 350sec to 1000sec on 4090 after multiple generations
  - *From: KuriousKatz*

- **Problem:** Context windows causing visual jumps every 81 frames
  - **Solution:** Issue with I2V context windows resending first frame repeatedly - attempted progressive reference frame system but resulted in noise/negative frames
  - *From: AJO*

- **Problem:** OOM on RTX 5090 with smaller model
  - **Solution:** 10 second video was too long, caused memory issues
  - *From: orabazes*

- **Problem:** Chatterbox nodes breaking ComfyUI installation
  - **Solution:** Remove the nodes to save ComfyUI installation
  - *From: hicho*

- **Problem:** UltraWan LoRA keys not loading in wrapper
  - **Solution:** May need to update wrapper version
  - *From: Draken*

- **Problem:** Context options mess up video-to-video results
  - **Solution:** Cannot use context options for video-to-video workflow
  - *From: VRGameDevGirl84(RTX 5090)*

- **Problem:** All frames coming out black
  - **Solution:** Update diffusers library
  - *From: burgstall*

- **Problem:** Color shifting in VACE extend
  - **Solution:** Have a start image on the original video to prevent color shifting
  - *From: Piblarg*

- **Problem:** Need multitalk branch for wrapper
  - **Solution:** Switch to multitalk branch: git fetch --all, git switch multitalk
  - *From: TK_999*

- **Problem:** Slow generation times on 4090 24GB
  - **Solution:** Increase block_swap from 10 to 25-40, monitor until speed improves
  - *From: Juampab12*

- **Problem:** Color shifting and compounding sharpening in extensions
  - **Solution:** Try no reference frames, increase steps to 12, use longer prompts, try CFG 3
  - *From: Piblarg*

- **Problem:** MultitTalk missing dependency error
  - **Solution:** pip install pyloudnorm package
  - *From: Charlie*

- **Problem:** Upscaling very pixelated videos
  - **Solution:** Use higher denoise (0.7-0.8) and blur input slightly to reduce noise amplification
  - *From: VRGameDevGirl84(RTX 5090)*

- **Problem:** VACE and MultiTalk layer conflicts
  - **Solution:** Modified wrapper patches VACE to ignore MultiTalk layers by processing them as no-op, allowing both to work together
  - *From: Tango Adorbo*

- **Problem:** MultiTalk settings for 720p unclear
  - **Solution:** Use audio cfg 2, cfg 2, 5 steps 4 shift, audio scale 1.5-2 for 720p model
  - *From: Guey.KhalaMari*

- **Problem:** White background artifacts in upscaling
  - **Solution:** Changing background color to black or green solved artifacts that appeared on white backgrounds
  - *From: Faux*

- **Problem:** OOM issues with high resolution
  - **Solution:** Use block swapping or FusionX GGUF model to handle memory constraints
  - *From: VRGameDevGirl84(RTX 5090)*

- **Problem:** pyloudnorm package not found error in MultiTalk
  - **Solution:** Install using the specific Python executable: python_embeded\python.exe -m pip install pyloudnorm
  - *From: lomerio*

- **Problem:** Steps showing one less than set in console
  - **Solution:** Console shows steps minus 1, so set to 5 to get actual 4 steps
  - *From: VRGameDevGirl84(RTX 5090)*

- **Problem:** Black screen in video combine node
  - **Solution:** Check show preview enabled setting or check output folder directly
  - *From: Thom293*

- **Problem:** Phantom I2V requires second image input
  - **Solution:** Use black, white, or any placeholder image as second input - it gets ignored
  - *From: Thom293*

- **Problem:** 1.3B VACE model AttributeError with WanVideoSampler
  - **Solution:** Use the module version from Kijai's repo: Wan2_1-VACE_module_1_3B_bf16.safetensors
  - *From: David Snow*

- **Problem:** MultiTalk wav2vec error
  - **Solution:** Use correct wav2vec model
  - *From: Draken*

- **Problem:** MagRef tensor mismatch on nonstandard ratios
  - **Solution:** Use standard aspect ratios like 1024x576 instead of 1024x600
  - *From: MysteryShack*

- **Problem:** Black outputs with fp8_e4m3fn quantization
  - **Solution:** Use fp16 without quantization for stable results, slightly slower but no black outputs
  - *From: patientx*

- **Problem:** Wan I2V blue chunks output
  - **Solution:** Remove weights from positive text prompts
  - *From: jeffcookio*

- **Problem:** Color picker nodes not working
  - **Solution:** Issue with recent updates affecting color picker system in multiple node packs
  - *From: Nekodificador*

- **Problem:** VRAM OOM with VACE embeds
  - **Solution:** Use distorch node and set RAM limits, clear RAM between runs
  - *From: mdkb*

- **Problem:** RuntimeError about tensors on different devices when using multiple control inputs
  - **Solution:** Not fully resolved in the discussion
  - *From: Faust-SiN*

- **Problem:** mat1 and mat2 shapes multiplication error in WanVideo Diffusion Forcing Sampler
  - **Solution:** Switch from fp8 to fp16 version of umt5-xxl-enc-fp8_e4m3fn.safetensors file
  - *From: MilesCorban*

- **Problem:** Color/brightness variation with lightx2v LoRA
  - **Solution:** Use image saturation node between decoder and video combine at 0.85-0.90 values
  - *From: Bleedy (Madham)*

- **Problem:** OOM issues with Multitalk on 3090
  - **Solution:** Reduce frame count - 500 frames worked, 1440 caused OOM, trying 720
  - *From: NebSH*

- **Problem:** Audio frame length mismatch in Multitalk
  - **Solution:** Calculate frames by multiplying audio seconds by chosen FPS, change settings in 3 places: frame, multitask node, and VHS node
  - *From: voxJT*

- **Problem:** Black output from multitalk v2v workflow
  - **Solution:** Update LoRAs with correct local models - LightX takes over for CausVid
  - *From: VRGameDevGirl84(RTX 5090)*

- **Problem:** Missing connections in workflow after loading
  - **Solution:** Restart ComfyUI or update it - workflow loads correctly on fresh install
  - *From: VRGameDevGirl84(RTX 5090)*

- **Problem:** OOM on 4090 with upscaler workflow
  - **Solution:** Enable block swap to reduce VRAM usage
  - *From: VRGameDevGirl84(RTX 5090)*

- **Problem:** OOM issues under 81 frames on 48GB card
  - **Solution:** Enable context options which resolved the issue completely
  - *From: samhodge*

- **Problem:** PreviewImage 'NoneType' object is not subscriptable error
  - **Solution:** Check that base examples node is in inputs folder, can replace with any image
  - *From: the_darkwatarus_museum*

- **Problem:** Classic Wan error with wrong frame count or image size
  - **Solution:** Check frame count and image dimensions are correct
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Problem:** MultiTalk doesn't work with context options
  - **Solution:** Image begins to shift when context windows take over, even with higher context_overlap
  - *From: Tango Adorbo*

- **Problem:** OOM issues when upscaling
  - **Solution:** Use context options with block swap set to 40, allows processing any amount of frames
  - *From: VRGameDevGirl84(RTX 5090)*

- **Problem:** VACE default negatives work against source image
  - **Solution:** Default negatives (especially Chinese ones referencing 'colorful, artwork, painting') can hurt realism if not going for realistic output
  - *From: garbus*

- **Problem:** Reference images cause wicked flash in VACE workflows
  - **Solution:** Issue noted, no specific solution provided
  - *From: David Snow*

- **Problem:** Tensor dimension mismatch error when going from 720x1280 to 1080x1920
  - **Solution:** Change divisible by to 16, use 1088 and crop after the fact if needed
  - *From: VRGameDevGirl84(RTX 5090)*

- **Problem:** LightX LoRA causes overexposure in outputs
  - **Solution:** Reduce steps from 6 to 4 and set lightx strength from 1.2 to 1.0
  - *From: Valle*

- **Problem:** MMaudio OOMing on 44 second videos
  - **Solution:** Use smaller model (mmaudio_small) or split audio into shorter segments
  - *From: Jonathan*

- **Problem:** RecamMaster artifacts
  - **Solution:** Use Uni3C instead
  - *From: Juampab12*

- **Problem:** People talking in generations despite negative prompts
  - **Solution:** Adjust NAG node values, reference provided to parameter breakdown
  - *From: JohnDopamine*

- **Problem:** OOM errors when loading LoRAs
  - **Solution:** Enable low vram mode on the wrapper lora node - takes longer to load but prevents OOM
  - *From: Draken*

- **Problem:** Video resolution not working
  - **Solution:** Resolution needs to be divisible by 16. Change 1920x1080 to 1920x1072
  - *From: ingi // SYSTMS*

- **Problem:** KSampler mat1 and mat2 shapes error
  - **Solution:** Dimensions aren't a multiple of 16
  - *From: Jonathan*

- **Problem:** Full OOM error in multitalk
  - **Solution:** Remove all purge caching stuff as it confuses ComfyUI which handles that automatically (native nodes guarantee this)
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Problem:** OOM issues with upscaler workflow
  - **Solution:** Increase block swap setting
  - *From: Draken*

- **Problem:** Camera shake in I2V generations
  - **Solution:** Set the problematic setting to 0 to remove shake
  - *From: Juan Gea*

- **Problem:** Resize node causing errors
  - **Solution:** On resize nodes, avoid choosing 'resize' on the keep proportions selection as this can cause errors
  - *From: RollmeWanKenobi*

- **Problem:** Canny preprocessor maxing out 24GB VRAM and OOM
  - **Solution:** Use an unload node after the preprocessor to manage VRAM usage
  - *From: Jonathan*

- **Problem:** Color problems and changes with CausVid
  - **Solution:** CausVid for 1.3B completely changes colors, visible in details like moss on wood
  - *From: Alisson Pereira*

- **Problem:** Self-forcing and speed LoRAs not properly implemented
  - **Solution:** ComfyUI only benefits from part of what self-forcing and CausVid can do, similar to how CausVid isn't properly implemented
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Problem:** Random flashing/color shift in upscaled videos
  - **Solution:** Issue originates in low-res generation causing flashes, needs to be fixed at generation stage
  - *From: N0NSens*

- **Problem:** Multitalk error with transformers update
  - **Solution:** Downgrade transformers to version 4.52.4
  - *From: DawnII*

- **Problem:** MMAudio installation breaking existing WAN workflows
  - **Solution:** Installing MMAudio requirements can cause VRAM/memory issues and workflow failures
  - *From: The Shadow (NYC)*

- **Problem:** GPU running at 92C and throttling
  - **Solution:** Temperature is too high and causing performance issues
  - *From: MysteryShack*

- **Problem:** Loading both VACE and WAN in native flow
  - **Solution:** Need VACE version that includes 14B model, recommend Q8 GGUF version
  - *From: David Snow*

- **Problem:** RAM not clearing after failed runs
  - **Solution:** Disable non-blocking transfers or restart ComfyUI to clear pinned memory
  - *From: Kijai*

- **Problem:** MultiTalk with VACE compatibility issues
  - **Solution:** Use multitalk branch of WanVideoWrapper or apply patches from Rudra-ai-coder fork
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Problem:** Context window error in workflow
  - **Solution:** Error was fixed in recent update, may need to update WanVideoWrapper
  - *From: Kijai*

- **Problem:** Color Match node issues with dark reference images
  - **Solution:** Color match with mkl sometimes messes up if reference image is dark, consider using hm-mvgd-hm instead
  - *From: zoz*

- **Problem:** VACE with MultiTalk model mismatch
  - **Solution:** When using VACE module, must use T2V model not I2V model
  - *From: VRGameDevGirl84*


## Model Comparisons

- **3 steps with AccVid + CausVid vs 6 steps CausVid only**
  - Huge difference with AccVid combination being much better
  - *From: Jonathan*

- **CausVid v1/v1.5 vs v2**
  - V1.5 and v1 work best, v2 sucks for quality and has huge negative effects on stylized outputs
  - *From: Jonathan/Kijai*

- **Native vs Wrapper workflows**
  - Native is much cleaner, uses half the nodes, takes no guess work, and is more compatible
  - *From: Jonathan*

- **14B Phantom vs 1.3B**
  - 14B shows dramatically better movement, colors and camera work
  - *From: stas*

- **Wan ecosystem vs other models**
  - 14B > Flux Dev, 1.3B > Flux Schnell, CausVid > LCM, VACE > ControlNet, Phantom > IPAdapter
  - *From: Nekodificador*

- **Low steps with CausVid vs 20 steps without**
  - Night and day difference in motion and quality, CausVid much faster
  - *From: ZeusZeus*

- **Kontext vs ChatGPT edit**
  - Kontext is 100% better quality, makes ChatGPT look like a toy
  - *From: Nekodificador*

- **1.3B speed improvement**
  - 1.3B with optimizations brings generation to seconds - 42.36 seconds vs 131.13 seconds for 14B
  - *From: VRGameDevGirl84*

- **CausVid v1.5 vs v2 for stylized outputs**
  - Original CausVid v1.5 (first block removed) works better for stylized content than v2
  - *From: Piblarg*

- **CausVid v2 vs AccVid**
  - CausVid v2 renders more smooth but limits motion, AccVid kills less motion but has blurring problems
  - *From: PolygenNoa*

- **720p vs 576p resolution**
  - 720p shows small improvement for small details like hands, reduces motion blur slightly
  - *From: Piblarg*

- **fp16 vs fp8**
  - fp16 > fp8 in quality, but fp8 should be fine with minimal degradation
  - *From: MilesCorban*

- **GGUF Q8 vs fp8**
  - GGUF Q8 is higher quality than fp8, Q6 about same, below that it generally gets worse
  - *From: Kijai*

- **Phantom vs VACE**
  - Phantom is better for referencing/identity, VACE is more compatible with different controls and prompting
  - *From: Johnjohn7855*

- **ATI trajectory vs Kling motion brush**
  - ATI is like Kling motion brush but 10x better
  - *From: Juampab12*

- **720p vs 540p VACE performance**
  - 720p performs better than 540p with VACE, even at same resolution. 540p shows box artifacts
  - *From: Zuko*

- **CausVid v2 8 steps vs 10 steps**
  - 10 steps looks better but takes longer (103.12s vs 127.23s)
  - *From: VRGameDevGirl84(RTX 5090)*

- **With CausVid (10 steps, 135s) vs without CausVid (25 steps, 920s)**
  - Without CausVid was expected to look better but surprisingly didn't
  - *From: VRGameDevGirl84(RTX 5090)*

- **MPS vs HPS reward LoRAs**
  - MPS is better, HPS tends to override other loras and makes faces look artificial
  - *From: David Snow*

- **External RTMPose vs ComfyUI DWPose**
  - External pose detection significantly more reliable than ComfyUI implementation
  - *From: A.I.Warper*

- **CausVid v1 vs v1.5 vs v2**
  - v1 consistently outperforms both newer versions
  - *From: Jonathan*

- **CausVid alone vs CausVid + AccVid**
  - Adding AccVid improves motion, detail and prompt adherence by 40%+
  - *From: Jonathan*

- **CausVid v2 at strength 1 with cfg 3 vs other combinations**
  - Best results with most motion and resemblance, simpler setup
  - *From: hablaba*

- **AccVid vs CausVid for prompt adherence**
  - AccVid wins more often for prompt adherence
  - *From: DevouredBeef*

- **Phantom-Wan-1.3B vs Phantom-Wan-14B**
  - 1.3B sometimes gives better results than 14B regardless of LoRA combinations used
  - *From: Mngbg*

- **AccVid T2V vs I2V versions**
  - I2V worked on photoreal but terrible on non-photoreal, just like T2V version
  - *From: Kijai*

- **Different samplers quality**
  - DPM++ 2M is clear winner when comparing frame by frame, UniPC gives fewer steps but lower quality
  - *From: Jonathan*

- **MPS vs HPS for face resemblance**
  - HPS retains resemblance more than MPS but at cost of less motion. MPS affects face resemblance the most
  - *From: Jonathan*

- **AccVid T2V vs I2V**
  - AccVid I2V is no better or worse than T2V when used in I2V at face value, still doesn't help the motion loras
  - *From: DevouredBeef*

- **CausVid v1 vs v2**
  - The first causvid is still superior. V2 causevid hurts image quality and makes them too dark
  - *From: Jonathan*

- **Euler vs DPM++ samplers**
  - Euler has natural skin tone and better lighting, dpm++ 2m is still better overall but dpmpp_2 plus beta outputs very detailed bright video
  - *From: Jonathan*

- **SageAttention modes**
  - Triton mode vs CUDA mode - CUDA mode works better, Triton can cause weird outputs
  - *From: lomerio*

- **SageAttention 1 vs 2**
  - Don't waste time with SageAttention 1, SageAttention 2 is much better
  - *From: Jonathan*

- **Single vs dual VACE embeds**
  - 2 embeds more VRAM intensive but more reliable than merged controls, but with VACE block swap should not increase VRAM significantly
  - *From: Kijai*

- **Uni3C vs Wan-fun camera control**
  - Uni3C is way better for camera control
  - *From: Kijai*

- **Luma AI vid2vid vs VACE**
  - Dragon example comparable or better than VACE
  - *From: A.I.Warper*

- **Wrapper vs Native ComfyUI**
  - Wrapper quicker to implement new features, Native more stable but missing features like Vace module, Uni3c, Unianimate, ATI
  - *From: David Snow*

- **Native vs Wrapper workflow differences**
  - Differences are pretty enormous between native and wrapper
  - *From: MilesCorban*

- **Autoregressive 1.3b vs 14b master model**
  - Auto aggressive model is crazy fast
  - *From: hicho*

- **Q8 vs Q5 GGUF models**
  - Q8 for quality, Q5_K_M saves 24gb VRAM with minimal quality loss
  - *From: Jonathan*

- **Wrapper vs Native performance**
  - Wrapper generally produces better results, native seems to have issues with causvid blocks and some LoRA handling
  - *From: TK_999*

- **GGUF vs Safetensors**
  - If VRAM limited or want max quality go GGUF, if want speed and have enough VRAM go safetensors. GGUF only slightly slower
  - *From: The Punisher*

- **CausVid v2 vs v1**
  - v2 sucks, breaks hair, v1.5 recommended over v2
  - *From: Jonathan*

- **3 vs 6 steps**
  - 6 steps can be overcooked, 3-5 steps optimal range with right settings
  - *From: The Punisher*

- **AccVid I2V LoRA vs T2V LoRA**
  - I2V LoRA much better at retaining resemblance, fixes overblown colors, better prompt adherence, more stable at higher strengths
  - *From: Jonathan*

- **Current Wan results vs Luma AI**
  - Wan better for foreground subjects, Luma better for background movement like leaves rustling
  - *From: A.I.Warper*

- **Single VACE embed vs separated encodes**
  - Single embed has stronger control, separation allows independent strength control but may require strength >1
  - *From: hablaba*

- **GGUF vs FP16 weights**
  - FP16 may produce better hair detail and fewer artifacts than quantized GGUF models
  - *From: The Punisher*

- **CausVid v1 vs v1.5**
  - v1.5 works better overall despite v1 having fewer hair issues in some cases
  - *From: The Punisher*

- **Different shift values on merged model**
  - Lower shift (1-2) produces more cinematic results, higher shift (8+) causes hair artifacts
  - *From: VRGameDevGirl84*

- **With vs without Enhanced Video**
  - Enhanced makes results sharper but more FLUX-like, without Enhanced looks more realistic
  - *From: MilesCorban*

- **Open source vs proprietary models**
  - Open source video models have reached par quality with Kling and Hailuo
  - *From: 🦙rishappi*

- **CausVid V1 vs V2**
  - V2 needs more steps but has less negative effects on motion
  - *From: Kijai*

- **Native vs wrapper workflows**
  - Should only use wrapper for features that don't exist in native - native has automated memory management
  - *From: Kijai*

- **720p vs 480p Wan model**
  - 720p is significantly better - 2x better quality, handles complex prompts and movements much better, same VRAM usage
  - *From: Jonathan*

- **Blend vs multiple VACE encoders**
  - Blend method is superior for output quality
  - *From: CaptHook*

- **MPS vs HPS LoRAs**
  - MPS better for motion but affects details and facial resemblance more negatively than HPS. Don't go higher than 0.5 with MPS for facial work
  - *From: Jonathan*

- **GGUF Q6_K vs Q8**
  - Q6_K supposed to be better at staying true to prompts than Q8 with minimal quality difference
  - *From: blake37*

- **CausVid v1.5 vs v2**
  - V1.5 works better - v2 did not work well for many users
  - *From: Johnjohn7855*

- **VACE vs Wan vanilla for FLF2V quality**
  - VACE is better quality
  - *From: samhodge*

- **Wrapper vs Native**
  - Wrapper has faster performance and more features but requires full model reload when changing loras; Native is better with VRAM and experimentation-friendly
  - *From: Piblarg*

- **CausVid V1.5 vs V2**
  - V1.5 more stable and better for character consistency, V2 more natural but loses reference images. V1.5 sharper overall, V2 more natural
  - *From: David Snow*

- **T2V vs I2V in Wan**
  - I2V is next level compared to T2V, gives much better control from initial frame
  - *From: JohnDopamine*

- **Wrapper vs Native Wan**
  - Native is more VRAM/RAM friendly and causes fewer OOM errors than wrapper
  - *From: Thom293*

- **Segment Anything Ultra v2 vs SAM2**
  - Ultra v2 usually gives better results than SAM2 but is slower
  - *From: N0NSens*

- **Native vs Wrapper optimization**
  - Native does automatic offloading while wrapper requires manual block swap configuration
  - *From: Kijai*

- **Windows vs Linux memory handling**
  - Windows shared memory is incredibly slow when near VRAM cap, Linux may perform better
  - *From: Kijai*

- **Self-forcing vs CausVid**
  - Self-forcing provides similar speedup to CausVid LoRAs but with slightly better quality
  - *From: Kijai*

- **1.3B self-forcing vs LTX**
  - Self-forcing quality and speed makes LTX forgettable according to user testing
  - *From: slmonker*

- **DMD vs other self-forcing variants**
  - DMD variant appears to have better results, especially visible in face quality
  - *From: slmonker*

- **WAN 14B vs Self-Forcing 8 steps**
  - Self-Forcing much faster: 1 minute vs 3 minutes for similar output
  - *From: VK (5080 128gb)*

- **Self-Forcing quality vs speed trade-off**
  - Lower quality than WAN but much faster - some users accept quality loss for speed gain
  - *From: Kaïros*

- **CausVid bidirectional 1.3B vs Self-Forcing**
  - Kijai thinks CausVid 1.3B bidirectional is better when used correctly
  - *From: Kijai*

- **Native workflows vs WanVideoWrapper VRAM usage**
  - Native workflows much more VRAM efficient - native stays under 16GB up to 480x720-97frames, wrapper fills VRAM instantly even at 192x256
  - *From: patientx*

- **Q8 GGUF vs fp8 models**
  - Q8 has nicer outputs than fp8 models
  - *From: David Snow*

- **14B vs 1.3B self-forcing results**
  - 14B has ruined expectations, self-forcing results not satisfying compared to 14B quality
  - *From: David Snow*

- **Self-forcing vs CausVid motion quality**
  - Self-forcing distillation has negative effects on motion when used differently than trained
  - *From: Kijai*

- **Phantom vs VACE for character consistency**
  - Phantom significantly better for character consistency, especially for characters the model can't naturally generate like Frieren
  - *From: MysteryShack/Piblarg*

- **VEO3 vs MultiTalk vs FantasyTalking for naturalness**
  - VEO3 > MultiTalk > FantasyTalking in terms of naturalness of both characters and voices
  - *From: ZeusZeus*

- **Training loras locally vs cloud (Replicate)**
  - Cloud training on H100 takes 20 minutes vs 4-5 hours on local 3090/4090, costs $1.50
  - *From: Ruairi Robinson*

- **AniWan 100% vs 25% merge**
  - Higher than 25% deforms the eyes, 25% is better
  - *From: ZRNR*

- **GGUF vs native models for speed**
  - GGUF is slower in general, fp8 preferred for speed over fp16/GGUF
  - *From: Kijai*

- **Phantom improvement on fp16 vs BF16**
  - Improvement compared to BF16 is massive on phantom
  - *From: Dream Making*

- **MagCache vs TeaCache**
  - Testing shows MagCache works better than TeaCache, includes calibration code unlike TeaCache
  - *From: yi*

- **Skyreels V2 vs Wan2.1**
  - Still prefers Skyreels V2 over most current Wan2.1 models due to shutter offset, Wan looks jittery without native framerate training
  - *From: Mads Hagbarth Damsbo*

- **Native vs Wrapper speed**
  - Native/GGUF runs twice as fast as wrapper with same settings
  - *From: MysteryShack*

- **MagCache vs TeaCache**
  - MagCache is almost exactly the same as TeaCache performance-wise
  - *From: Kijai*

- **New Cosmos vs Wan**
  - Even if Cosmos beats Wan, unlikely to be adopted due to lack of control features that Wan has
  - *From: yi*

- **NAG vs scheduled CFG**
  - NAG is only 10-20% slower vs CFG doubling inference time, but uses more VRAM
  - *From: Kijai*

- **Different samplers with CausVid**
  - Colors were less burnt and more natural than UniPC
  - *From: DiXiao*

- **TeaCache vs no TeaCache with CausVid**
  - TeaCache potentially causes mistakes with CausVid and low steps, better quality without it
  - *From: Fawks*

- **WAN vs other video models ecosystem**
  - WAN is the SD 1.5 moment of video - 20+ different models built on top
  - *From: Juampab12*

- **Phantom with T2V merge vs pure Phantom**
  - Merged version works way better with LoRAs, pure Phantom often produces poor results
  - *From: ▲*

- **Self-forcing vs Wan 14B**
  - Self-forcing is 5-6x faster with comparable quality, better for testing and simple shots
  - *From: Jonathan*

- **Phantom vs standard models for style adherence**
  - Phantom is great for style adherence and style mixing
  - *From: David Snow*

- **Kontext vs Redux**
  - Kontext has stronger reference input but can easily alter scenes, unlike Redux
  - *From: Draken*

- **HiDream vs Flux**
  - HiDream may be better for certain uses but significantly more resource heavy
  - *From: David Snow*

- **FusionX vs other models**
  - FusionX has better prompt following but is a merge with baked LoRAs
  - *From: Ada*

- **Hunyuan vs Wan at high resolution**
  - Hunyuan at 1080p creates extremely good images, whole model steers differently at higher res (likely real life video training data)
  - *From: Juampab12*

- **Phantom/VACE vs 14B t2v/VACE for i2v**
  - Phantom version produces much better face stability and detail
  - *From: David Snow*

- **FusionX lora vs merge**
  - Merge looks significantly better than lora versions
  - *From: Juampab12*

- **Causal sampling quality at different steps**
  - 3 steps looks like crap, 9 steps overcooked, maybe 6 is optimal. 1.3B fast but low quality
  - *From: Kijai*

- **FusionX vs individual loras**
  - FusionX works better for i2v than regular lora stack according to some users
  - *From: N0NSens*

- **Wrapper vs Native**
  - Some find wrapper more nightmare, others prefer it; depends on use case and hardware
  - *From: Jonathan*

- **14B vs 1.3B for cleanup**
  - 1.3B isn't good enough for videos generated with 14B, destroys fine detail
  - *From: David Snow*

- **ComfyUI vs external tools for frame interpolation**
  - Standalone FLOWFRAMES app is much quicker than ComfyUI for same RIFE models
  - *From: ▲*

- **MPS effect on different scenarios**
  - MPS can turn 3D characters into real-looking humans without prompting, but affects facial resemblance
  - *From: ▲*

- **Self-forcing 4 steps vs causvid V2 lora at 10 steps**
  - Comparable quality after 30+ generations
  - *From: yi*

- **Self-forcing vs causvid motion coherence**
  - Massive difference in motion coherence, self-forcing much better
  - *From: David Snow*

- **480*320 5 sec video generation speed**
  - Self-forcing 20 seconds (2x faster than causvid lora)
  - *From: yi*

- **LightX2V follows prompts vs causvid**
  - Follows prompts so much better and has better motion quality than causvid
  - *From: Ada*

- **Self-forcing quality vs their demo videos**
  - Model seems good but their own demo examples are horrible, possibly wrong inference parameters
  - *From: Ada*

- **LightX2V vs CogVid**
  - Initially worse than cogvid based on demos
  - *From: Juampab12*

- **Wan vs SDXL usage**
  - Don't see a use for SDXL now that Wan has more than enough controlnets and speedups. Only use for SDXL is anime and image2video
  - *From: yi*

- **LightX2V vs CausVid speed**
  - LightX2V generates in ~42 seconds vs CausVid at ~49 seconds on same hardware
  - *From: MilesCorban*

- **4 steps vs 5 steps with LCM scheduler**
  - 5 steps is overcooked mess, 4 steps provides clean results with LCM
  - *From: CJ*

- **FusionX LoRA vs LightX2V for I2V**
  - FusionX LoRA performs better than LightX2V for image-to-video tasks
  - *From: N0NSens*

- **HPS vs MPS LoRAs**
  - Left (HPS) looks better for image quality, right (MPS) has better movement
  - *From: Juampab12*

- **MAGREF vs Phantom**
  - MAGREF much better at likeness but seems less flexible than Phantom
  - *From: David Snow*

- **Wan I2V vs T2V performance**
  - Wan I2V has always outperformed T2V
  - *From: Kijai*

- **CausVid vs Lightx2v for anime**
  - CausVid seems to perform better than Lightx for 2d anime
  - *From: Charine*

- **14B VACE vs 1.3B MinimaxRemover**
  - 14B VACE can probably be better than 1.3B MinimaxRemover
  - *From: Kijai*

- **MAGREF vs Phantom**
  - MAGREF is slightly less accurate but faster than Phantom
  - *From: toyxyz*

- **LightX2V vs CausVid**
  - LightX2V is better than CausVid according to testing
  - *From: Piblarg*

- **Native vs Wrapper workflows with LightX2V**
  - Wrapper with NAG provides much better prompt adherence than native
  - *From: jacinda*

- **MagRef vs Phantom**
  - MagRef gets higher quality and better character accuracy, but Phantom is more flexible for outfit/hairstyle changes
  - *From: David Snow*

- **UniPC vs LCM with LightX2V**
  - UniPC is solid at 3 steps while LCM was fuzzy, though LCM generally works better for Phantom
  - *From: phazei*

- **MagCache vs TeaCache**
  - MagCache is much better, faster even when skipping steps
  - *From: phazei*

- **Wrapper vs Native for vid2vid**
  - Native is better for vid2vid, wrapper vid2vid isn't very good
  - *From: Kijai*

- **LightX2V vs CausVid/AccVideo**
  - LightX2V has better motion and overall quality, replaces acc/caus completely
  - *From: jacinda*

- **Native vs Wrapper speed**
  - Should be equal when configured correctly, 3x difference indicates memory/configuration issue
  - *From: Kijai*

- **Wan vs Midjourney Video**
  - Midjourney better at complex camera motions, but quality similar to good Wan 14B I2V with LoRAs
  - *From: Jonathan*

- **AccVideo with LightX2V**
  - AccVideo gives speed boost with no quality loss for realism but has negative effects on other styles
  - *From: Kijai*

- **LightX2V vs CausVid v2**
  - LightX2V creates excessive wrinkle-type textures on skin compared to CausVid v2
  - *From: Persoon*

- **VACE vs Fun Control**
  - VACE is better and more versatile than Fun Control
  - *From: TK_999*

- **Depth Anything VitG vs VitL vs DepthCrafter**
  - VitG marginally better, most notable in faces and background circles, but difference not monumental
  - *From: David Snow*

- **Res S samplers vs others**
  - Res S samplers are generally more accurate but much slower
  - *From: TK_999*

- **LightX2V vs CausVid**
  - LightX2V is much better - 'proper distillation' while CausVid was 'more a hack we were using'
  - *From: Kijai*

- **Normal I2V model vs MAGREF**
  - MAGREF provides significantly better likeness/character consistency
  - *From: Kijai*

- **Phantom vs other models for character consistency**
  - Phantom is better at likeness consistency than other options
  - *From: amli*

- **lightx2v vs causvid**
  - lightx2v works twice as strong without adverse effects, uses self-forcing training instead of causal training, works with normal 21 latent count
  - *From: Kijai*

- **MultiTalk vs closed source lip-sync solutions**
  - MultiTalk is better than closed source solutions but requires high compute
  - *From: Draken*

- **5090 vs 4090 for Wan**
  - 5090 is ~50% better - 40% faster plus memory advantages when usable
  - *From: Kijai*

- **Block swap vs no block swap performance**
  - 5090 with 32GB doesn't need block swap at 832x480, significantly faster than 4090 needing 30 mins for 800 frames
  - *From: Kijai*

- **MAGREF vs regular I2V models for MultiTalk**
  - MAGREF gets much more freedom and works way better with context windows than I2V models
  - *From: Kijai*

- **Closed source tools vs MultiTalk for laughter**
  - None of the closed source tools can do laughter - Hedra intentionally mutes audio during laughter due to issues
  - *From: A.I.Warper*

- **5090 vs other GPUs for MultiTalk**
  - MultiTalk is 'a hell of a lot faster on a 5090'
  - *From: Purz*

- **Open source MultiTalk quality assessment**
  - 'how is this open source, those are the best results i've seen so far and we don't even know how to use it properly'
  - *From: Nekodificador*

- **LightX2V vs CausVid**
  - LightX2V is proper diffusion while CausVid was a hack, LightX2V replaces CausVid but some users get better results with CausVid at 10 steps
  - *From: mdkb*

- **Text-to-video vs Image-to-video speed**
  - Text-to-video is faster than I2V in some setups
  - *From: VRGameDevGirl84*

- **1.3B vs 14B models for 8GB cards**
  - 1.3B models can run on 8GB or even 6GB cards, 14B needs more VRAM unless using system RAM offloading
  - *From: Ablejones*

- **UltraWan 1k vs 4k LoRA**
  - 1k version is miles better, 4k produces duplicated/garbage results
  - *From: David Snow*

- **Phantom vs MagRef for MultiTalk**
  - Phantom would be better fit since it's trained on 24fps vs MagRef at 15fps
  - *From: Guey.KhalaMari*

- **MultiTalk vs FantasyTalking**
  - MultiTalk works with animals and draws realistic animal teeth, FantasyTalking couldn't work with animals
  - *From: N0NSens*

- **MagRef vs Base Wan for MultiTalk**
  - MagRef keeps original image colors better and motion seems more natural, less jittery than base Wan
  - *From: orabazes*

- **30fps vs 60fps for MultiTalk**
  - 60fps better for fast singing/rapping, 30fps sufficient for normal speech. 60fps takes 2x generation time and can look too hyperactive
  - *From: patientx*

- **Phantom vs MagRef for I2V consistency**
  - Phantom provides better temporal consistency between context windows than MagRef, especially for family/personal content
  - *From: Guey.KhalaMari*

- **Chatterbox vs ElevenLabs TTS**
  - Chatterbox is just as good as ElevenLabs for being free
  - *From: VRGameDevGirl84(RTX 5090)*

- **SkyReels 14B and 1.3B v2 vs other models**
  - Still go-to models, keep going back to them while adding new LoRAs
  - *From: Colin*

- **48fps CFG1 vs 30fps CFG6**
  - 48fps looks better, 60fps not needed
  - *From: patientx*

- **Wan 14B vs 1.3B for small resolutions**
  - 14B better at 350x350 without anime artifacts that 1.3B produces
  - *From: hicho*

- **0.1 vs 0.5 denoise in v2v**
  - Almost identical results, no significant difference
  - *From: VRGameDevGirl84(RTX 5090)*

- **FusionX vs Base Wan for upscaling**
  - FusionX with merged LoRAs produces better quality upscales
  - *From: VRGameDevGirl84(RTX 5090)*

- **MultiTalk 40% vs 100% controlnet strength**
  - 40% strength provides much better movement, 100% too restrictive
  - *From: Thom293*

- **Wan v2v vs Sora v2v**
  - Better than Sora vid2vid according to user testing
  - *From: VK (5080 128gb)*

- **Video to video vs Ultimate SD upscale**
  - Video to video much faster for similar quality results
  - *From: VRGameDevGirl84(RTX 5090)*

- **MultiTalk uni3c strength 0.5 vs others**
  - 0.5 strength looks best, should try going even lower
  - *From: Juampab12*

- **Audio gain 1 vs 2 vs 3 for MultiTalk**
  - 3 is best, 2 is good too, much better than default 1
  - *From: Thom293*

- **MultiTalk distill LoRA vs base MAGREF**
  - Distill LoRA (cfg 1, 4 steps) was better quality, faster, and same audio sync vs base (cfg 5, 20 steps). Distill took 5 minutes vs 40 minutes for base
  - *From: ZeusZeus (RTX 4090)*

- **LightX2V vs CausVid distill models**
  - LightX2V is much better than CausVid for WAN
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Kijai VAE vs Comfy VAE**
  - Try Kijai's VAE if Comfy version gives garbled outputs
  - *From: garbus*

- **Video Depth Anything vs regular depth**
  - Video Depth Anything is way better, especially with vitG model
  - *From: Nekodificador*

- **Normal maps vs depth maps for VACE**
  - Normal maps provide better adherence and sharper outputs without color bleeding
  - *From: HeadOfOliver*

- **UltraWan 1K vs Wan 2.1 T2V**
  - UltraWan 1K with self-forcing DMD VACE 1.3B allows higher resolutions on lower VRAM
  - *From: mdkb*

- **Native vs wrapper workflows**
  - Native with GGUF models produces superior results but has VRAM offloading issues
  - *From: David Snow*

- **Q8 vs Q4_KM models**
  - Q4_KM gives just as good results but faster, decided to always use Q4_KM
  - *From: mdkb*

- **OG2 vs other models**
  - OG2 results feel like examples on repo are cherry picked, nowhere near Kontext quality
  - *From: 🦙rishappi*

- **RealisDance-DiT results**
  - Results look pretty crap, movement is nice but focused more on final video quality
  - *From: David Snow*

- **Wan FusionX vs Flux for text-to-image**
  - Shows comparison images but no explicit verdict given
  - *From: VRGameDevGirl84(RTX 5090)*

- **MagRef vs other character models**
  - MagRef seems to be performing the best for character consistency
  - *From: Impactframes.*

- **AnimateDiff vs Wan**
  - AnimateDiff is a predecessor to Wan and not directly connected - they don't work together despite some confusion
  - *From: Tango Adorbo*

- **AnimateDiff limitations vs Wan capabilities**
  - AnimateDiff being stuck at 16 frames was biggest flaw, Wan handles much longer sequences
  - *From: VK (5080 128gb)*

- **Phantom and VACE vs MagRef**
  - Still prefer VACE and/or phantom, MagRef was a disappointment as it's only an image to video model
  - *From: chrisd0073*

- **Uni3C vs Wan for camera motion**
  - Uni3c is much better for style transfer, unlike control it's much 'softer' and really good for camera
  - *From: ˗ˏˋ⚡ˎˊ-*

- **MultiTalk vs new Wan Audio**
  - New Wan Audio might be more general and flexible than MultiTalk, could be interesting for things other than speech
  - *From: ZeusZeus (RTX 4090)*

- **Wan FP8 vs full model on 4090**
  - 30sec vs 143sec generation time, no noticeable quality difference, not worth the extra time
  - *From: Mathew*

- **LightX vs CausVid quality**
  - CausVid at 10 steps produces more cinematic realism than LightX at 4 steps for text-to-video
  - *From: VRGameDevGirl84(RTX 5090)*

- **VACE 1.3 vs Cosmos text2world**
  - VACE 1.3 outperforms in quality despite both being slow
  - *From: Rainsmellsnice*

- **LTX 2B 0.9.6 distilled vs 13B model**
  - 2B model much faster (under a minute vs hours), 13B higher quality but much slower
  - *From: RollmeWanKenobi*

- **VACE vs Fun models**
  - Fun models are poor man's VACE models. VACE can do everything Fun models do and more
  - *From: mdkb*

- **Full lightx2v VACE model vs 14b VACE with lora**
  - Full lightx2v VACE model performs better than just using 14b VACE with the lora
  - *From: Jonathan*

- **LightX2V vs CausVid motion**
  - CausVid/AccVid/Reward loras still give better motion, but LightX2V is more stable
  - *From: Jonathan*

- **LightX2V stability vs motion**
  - LightX2V outputs are remarkably stable, sometimes different seed doesn't change anything, but motion is muted
  - *From: jdl_grmck*

- **VACE setup vs Cosmos**
  - VACE now blows Cosmos out of the water
  - *From: Rainsmellsnice*

- **LightX2V vs CausVid v2**
  - LightX is fast but not as good quality as CausVid v2. LightX gets worse with more steps while CausVid v2 can be refined with increased steps
  - *From: hablaba*

- **1.3B vs 14B for upscaling**
  - 1.3B is better, faster, considerably less resource intensive for upscaling. Haven't been able to get same details with 14B without high denoise that changes source video
  - *From: David Snow*

- **Q8 GGUF vs FP8**
  - Q8 GGUF will look better than fp8, Q6 will have next to no difference, Q5 and Q4 are good, Q3 sucks
  - *From: Jonathan*

- **Native vs Wrapper workflows**
  - Native with GGUFs is necessary for 12GB VRAM. For 24GB+ wrapper is preferred for anything that isn't VACE or basic I2V/T2V
  - *From: Jonathan*

- **LightX2V vs CausVid motion quality**
  - LightX2V has better detail and image resemblance but kills motion, CausVid + AccVid has 5x better motion but degrades output
  - *From: Jonathan*

- **Self-forcing 1.3B vs 14B LightX2V**
  - Self-forcing 1.3B model has more realistic motion speed than 14B LightX2V
  - *From: Jonathan*

- **FlowMatch_CausVid vs DPM++_SDE/Beta schedulers**
  - FlowMatch more stable but less natural skin, DPM++_SDE/Beta more realistic/natural looking
  - *From: VRGameDevGirl84(RTX 5090)*

- **Sage Attention 2 Plus speed boost on RTX 5090**
  - Not statistically significant speed boost, sometimes same or slower generation times
  - *From: blake37*

- **Topaz vs other upscaling methods**
  - Hard to beat Topaz, especially with two-step process using Gaia for upscale and Iris for cleanup
  - *From: blake37*

- **Normal I2V vs controlled methods**
  - Normal I2V is pretty useless, works fine with control like VACE, UniAnimate or MultiTalk
  - *From: Kijai*


## Tips & Best Practices

- **Use dwpose instead of depth control for character consistency**
  - Context: When generating videos with characters to avoid face morphing
  - *From: Piblarg*

- **Use real images instead of controlnet preprocessors with Phantom**
  - Context: For better results with Phantom model
  - *From: JohnDopamine*

- **Expand the mask when character proportions are very different**
  - Context: Makes it easier for the model to fit the character
  - *From: N0NSens*

- **Use separate VACE embed nodes for reference and control**
  - Context: When mixing reference with VACE control, set different strength/start/end percentages
  - *From: Johnjohn7855*

- **Use CausVid strength 1 or it gets wonky**
  - Context: When using CausVid LoRA, don't go over strength 1
  - *From: VRGameDevGirl84*

- **MPS strength over 0.5 may stop following preprocessors**
  - Context: Requires back and forth to find sweet spot for MPS reward LoRA
  - *From: DeZoomer*

- **Meeting for expensive hardware purchases**
  - Context: Meet at police station or bank for safety when buying scalped GPUs
  - *From: Colin/Ruairi Robinson*

- **Use input video at strength 0.3-0.4 as control**
  - Context: Helps get facial movement without changing output much
  - *From: VRGameDevGirl84(RTX 5090)*

- **Prompt for teeth to get teeth**
  - Context: When trying to capture specific mouth shapes
  - *From: A.I.Warper*

- **Use LLM descriptions for better prompt adherence**
  - Context: Florence 2 or Qwen descriptions help input images stick better
  - *From: cyncratic*

- **Merge LoRAs for speed**
  - Context: Creating merged models is faster than applying multiple LoRAs each time
  - *From: VRGameDevGirl84(RTX 5090)*

- **Use simple prompts with Phantom**
  - Context: Descriptive prompts tend to take away the model's focus and result in losing identity of reference images
  - *From: Johnjohn7855*

- **For Wan prompting, keep it under 150 words with literal descriptions**
  - Context: Use single flowing paragraph, focus on motion, visuals, atmosphere, no abstract phrasing
  - *From: GalaxyTimeMachine*

- **Use GGUF text encoders**
  - Context: 0 difference in quality and 1/3 the size
  - *From: Jonathan*

- **Mix normal map with depth map for better details**
  - Context: Take the normal map, turn it into black and white and mix it with the depth map, it increases a lot the details
  - *From: Nekodificador*

- **Ensure input video is high quality for v2v**
  - Context: Make sure the original video is crisp at high res. Going low res will make the gen low quality even if you generate at 4k
  - *From: hicho*

- **Use MPS LoRA at low weights like 0.3-0.4**
  - Context: When using multiple LoRAs to avoid overriding other effects
  - *From: David Snow*

- **Reference image structure should match input video first frame**
  - Context: For VACE face swapping to avoid blue artifacts
  - *From: VRGameDevGirl84(RTX 5090)*

- **Use ModelMergeSimple node for on-the-fly testing**
  - Context: Avoid saving permanent merges, use recipes instead
  - *From: ▲*

- **Lower shift to 5 and steps to 8 for VACE troubleshooting**
  - Context: When experiencing issues with VACE processing
  - *From: Johnjohn7855*

- **Add static background points when using ATI to freeze camera**
  - Context: Prevents unwanted camera movement during trajectory control
  - *From: Juampab12*

- **Use Florence captioning or Gemini to describe movement for ATI**
  - Context: Better prompting based on trajectory shown in initial image
  - *From: Juampab12*

- **More points needed between joints for pose-based ATI**
  - Context: When converting OpenPose to ATI trajectories
  - *From: toyxyz*

- **Use video editor deflicker effect or raise resolution/samples to fix flickering**
  - Context: Common issue with GGUF models
  - *From: Jonathan*

- **Lower MPS LoRA to 0.7 strength**
  - Context: To reduce overfitting while maintaining benefits
  - *From: Johnjohn7855*

- **Use box mask with VACE for subject replacement**
  - Context: With accurate mask, VACE will place back a subject similar to the mask shape
  - *From: Valle*

- **Get silhouette as close as possible for motion transfer**
  - Context: When doing motion transfer to different environments, matching silhouettes reduces motion differences
  - *From: chrisd0073*

- **Freeze workflows at some point to finish projects**
  - Context: Need to stop optimizing and stick with working parameters to actually complete work
  - *From: mamad8*

- **High resolutions help with I2V + controlnet for static scenes**
  - Context: 1536x1024 generation improves static scenes but might lose coherence for non-static scenes
  - *From: mamad8*

- **Don't stack LoRAs on human faces for resemblance**
  - Context: Stacking motion LoRAs reduces face resemblance, better for non-human subjects like clouds or volcanoes
  - *From: Jonathan*

- **Use AccVid at 1.5-2.0 strength for best results**
  - Context: If you want to retain resemblance while getting the most motion out of the lora
  - *From: Jonathan*

- **Fantasy Talker LoRA works well at 70-80% strength**
  - Context: For talking head generation, tested at various strengths
  - *From: A.I.Warper*

- **Use Euler sampler for stylized content**
  - Context: Euler is the way to go for anything stylized
  - *From: DawnII*

- **For face enhancer LoRAs, fully describe the person**
  - Context: Hard to explain lol u have to fully describe the person or they end up not looking great
  - *From: VRGameDevGirl84(RTX 5090)*

- **Use previews to instantly see if generation works**
  - Context: Black videos will show as black on first step in preview
  - *From: Kijai*

- **Place 2 spline points on top of each other for static points**
  - Context: When using spline editor for ATI
  - *From: Kijai*

- **Use CFG scheduling only on first step with AccVid**
  - Context: To avoid saturation issues when using CFG above 1.0
  - *From: Kijai*

- **Cache preprocessors for VACE to avoid memory issues**
  - Context: Some preprocessors use VRAM and don't flush properly
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Use group nodes to clean up messy LoRA chains**
  - Context: When switching to KJ wan sampler requires many LoRAs in sequence
  - *From: Colin/Kijai*

- **Use static points for trajectory control**
  - Context: Stack 2 points together to act as static points for ATI
  - *From: Johnjohn7855*

- **Describe background in prompt for consistency**
  - Context: When using VACE keyframes to prevent background inconsistencies
  - *From: TK_999*

- **Lower WanVaceToVideo strength to avoid artifacts**
  - Context: Around 0.70 strength to avoid artifacts in rendered output
  - *From: Cloudsurfer101*

- **Use 720p as default resolution**
  - Context: Models use 720p as default, not 480p
  - *From: Kijai*

- **Control is the only way AI video is useful**
  - Context: Better to spend 15 minutes making perfect vid and rerun 3 times vs rerun 100 vids and choose one
  - *From: Juampab12*

- **Use sgm_uniform scheduler instead of simple for better results**
  - Context: When using accvid and causvid
  - *From: Jonathan*

- **You only need 3 steps with accvid**
  - Context: When using accvid for speed
  - *From: Jonathan*

- **Training a wan lora on the person helps stabilize their features at every angle**
  - Context: For I2V when trying to reduce changes to objects and people's features
  - *From: Ruairi Robinson*

- **Use causvid at 0.5 as a sweet spot**
  - Context: To avoid contrast issues while maintaining quality
  - *From: The Punisher*

- **Start at 1-3 frames when experimenting**
  - Context: When testing new settings or resolutions
  - *From: Thom293*

- **Use CFG always on 1 with speed LoRAs**
  - Context: When using causvid and accvid, raising CFG over 1 doesn't work well
  - *From: The Punisher*

- **Lower mps strength for better facial resemblance**
  - Context: Use mps at 0.5-0.75 instead of 1.0 for maximum facial resemblance
  - *From: Jonathan*

- **Don't use reward loras with I2V**
  - Context: Reward loras ruin input image consistency in I2V at any strength, but work great in T2V
  - *From: ▲*

- **Hunt for good seeds and stick with them**
  - Context: Seeds really matter for video models, important to find good ones
  - *From: Johnjohn7855*

- **Use 3:4 or 9:16 ratios to avoid side bars**
  - Context: These ratios help prevent unwanted side bars in generated videos
  - *From: Johnjohn7855*

- **Use detailed prompts describing every reference image**
  - Context: Paper states this is needed to understand which image is which and what it's for
  - *From: AJO*

- **Prompt 'moving forward' for vehicles**
  - Context: Vehicles prefer to go backwards by default
  - *From: zelgo_*

- **Only put control frames through VACE, not reference images when using with Phantom**
  - Context: Putting ref image through both causes glitched videos
  - *From: ingi // SYSTMS*

- **Use very high quality HD images when training LoRAs**
  - Context: Will help with video generation quality
  - *From: Thom293*

- **Start with very small dataset for LoRA training**
  - Context: Don't need much for something the model already knows like car logos
  - *From: Thom293*

- **Test multiple shift values for production quality**
  - Context: For maximum quality, test 8 different shift values per video and pick the best one
  - *From: Jonathan*

- **Use shift formula for consistent results**
  - Context: steps*0.5 provides safe shift value, steps*0.5-0.25 is riskier but potentially better
  - *From: The Punisher*

- **Phantom models prefer low shift values**
  - Context: When using Phantom character consistency, keep shift around 2.2 or lower
  - *From: ▲*

- **Use pose landmarks for selective detail enhancement**
  - Context: When you need to enhance only specific facial features like mouth or eyes
  - *From: A.I.Warper*

- **Use simple descriptive prompts with Phantom**
  - Context: For better character consistency and prompt adherence
  - *From: 🦙rishappi*

- **Create masks in After Effects for more manual control**
  - Context: When doing video inpainting work
  - *From: Ruairi Robinson*

- **Use Image Batch Mult for multiple reference images of same person/object**
  - Context: Don't use for multiple different characters as it creates mashups
  - *From: zelgo_*

- **Cut out objects over white background in ComfyUI**
  - Context: For better Phantom reference image processing
  - *From: zelgo_*

- **Use shift formula (steps*0.5-0.25) for automatic shift calculation**
  - Context: Helps maintain quality across different step counts
  - *From: The Punisher*

- **Use pose+depth for better motion transfer with blend method**
  - Context: When using VACE for motion control
  - *From: CaptHook*

- **Use additional input images or up the weights for better face consistency**
  - Context: When trying to refine faces to match reference images
  - *From: The Dude*

- **Lower shift for more detail at end of gens, raise for more detail at beginning**
  - Context: 4-5 seems to be middle ground for shift values
  - *From: Jonathan*

- **Don't go higher than 0.5 with MPS LoRA for facial work**
  - Context: Higher strengths apply beauty filter effect and change facial features
  - *From: Jonathan*

- **Use even step counts for better shift performance**
  - Context: Steps * 0.5 - 0.25 formula may work better with even steps
  - *From: The Punisher*

- **Higher shift needed for odd step counts**
  - Context: Need to add +8 to shift for odd step numbers to avoid glitching
  - *From: The Punisher*

- **Test schedulers extensively with Phantom**
  - Context: Schedulers make a big difference in Phantom performance
  - *From: VRGameDevGirl84(RTX 5090)*

- **Use 17 frames overlap for DF extension**
  - Context: Default workflow uses 17 frames from input video as overlap for Skyreels DF
  - *From: Colin*

- **CausVid strength affects shift sensitivity**
  - Context: Too low CausVid (0.5) causes shift issues, higher values work better
  - *From: The Punisher*

- **Generate first frame in SDXL/Flux then use I2V for better control**
  - Context: Eliminates guesswork and gets exactly what you want
  - *From: Jonathan*

- **Use CausVid V2 at strength 2.0 for optimal results**
  - Context: V2 requires radically different settings than V1.5
  - *From: David Snow*

- **For phantom with two people, describe each person in prompt**
  - Context: Doesn't need to be detailed, could be 'man in black' or 'woman with red hair'
  - *From: Johnjohn7855*

- **Place static points appropriately in ATI for desired motion**
  - Context: Most important aspect for getting motion you want with ATI
  - *From: Johnjohn7855*

- **Change style of first frame/reference image rather than trying to transform video style directly**
  - Context: Easier approach for anime style transformation
  - *From: Johnjohn7855*

- **Use purge model/vram nodes liberally throughout workflow**
  - Context: Keeps VRAM free and prevents lockups, use after model loads, ksampler, result compile
  - *From: the_darkwatarus_museum*

- **Keep VACE strength at 1 for first pass**
  - Context: Wrapper strength doesn't behave like native VACE, acts more like blend factor
  - *From: chrisd0073*

- **Lower shift values produce more realistic results**
  - Context: Shift 1 is best for inpainting, higher values make it less realistic
  - *From: Simonj*

- **Use FP32 VAE to potentially reduce grid patterns**
  - Context: May help with artifact issues in fine details
  - *From: Simonj*

- **Use natural language for complex prompts with multiple characters**
  - Context: Works 90% of the time for complicated scenarios
  - *From: Thom293*

- **First pass needs high resolution and 50+ samples for Skip Layer Guidance fix**
  - Context: When using SLG to fix screendoor artifacts
  - *From: chrisd0073*

- **Turn off TeaCache when using self-forcing model**
  - Context: Leaving TeaCache on produces corrupted results
  - *From: slmonker*

- **Don't use VAE tiling if you can avoid it**
  - Context: Tiling can be costly and should be avoided when possible
  - *From: Kijai*

- **Manually prompt for every moving background element**
  - Context: To increase background movement, explicitly describe all moving elements like 'clouds move fast in the wind, leaves move in the wind'
  - *From: Jonathan*

- **Use ultrawide resolutions for better pixel efficiency**
  - Context: 1280x544 or 1472x626 for widescreen gives more quality per pixel than standard resolutions
  - *From: David Snow*

- **Always plan for professional color grading**
  - Context: Models often have crushed blacks and gamma issues requiring post-processing in Premiere or DaVinci
  - *From: Gateway {Dreaming Computers}*

- **Balance resolution vs frame count based on needs**
  - Context: Choose resolution that allows desired frame count - 260 frames at 1024x576 is one working example
  - *From: Gateway {Dreaming Computers}*

- **Use 80% GPU power limit for temperature control**
  - Context: Maintains performance while reducing temps from 86 to 70 degrees
  - *From: Dream Making*

- **Use image blending to reduce color differences in VACE loop videos**
  - Context: When creating looping videos with VACE
  - *From: toyxyz*

- **Use ExVideo LoRA for sequences beyond 123 frames**
  - Context: With original T2V model for longer generations
  - *From: chrisd0073*

- **Use VACE for control and Phantom for character consistency**
  - Context: Better results than trying to stack both for same purpose
  - *From: Piblarg*

- **Use phantom as starting image rather than VACE for character consistency**
  - Context: Phantom better trained for reference, VACE more precise for control
  - *From: Piblarg*

- **Use img2img on first frame of control video as reference for VACE**
  - Context: For consistent characters/backgrounds without needing multiple reference images
  - *From: Jonathan*

- **Generate character with prompt first, then use VACE for consistency**
  - Context: Works better than trying to force VACE to generate something it can't naturally create
  - *From: Piblarg*

- **Use static points to anchor parts of image in ATI**
  - Context: Essential for controlling which elements move vs stay static in trajectory control
  - *From: Kijai*

- **Control all elements that can move, even if you don't want them to move**
  - Context: Use static points for elements you want to keep stationary
  - *From: Kijai*

- **Use detail transfer for upscaling to maintain quality**
  - Context: When upscaling Wan videos
  - *From: ZRNR*

- **Downscale for LoRas to work better**
  - Context: Hulk LoRa needed downscaling to sort of work, was cherry picked after many attempts
  - *From: Guey.KhalaMari*

- **Higher resolution can improve lipsync alignment**
  - Context: Rendering at 720 instead of 576 res made lipsync feel more aligned
  - *From: A.I.Warper*

- **Use cfg 1 with empty negative prompt**
  - Context: cfg 3 for all 12 steps works, but cfg 1 fine with empty negative
  - *From: Piblarg*

- **Combine VACE preproc instead of multiple nodes**
  - Context: Can combine openpose+depth+lineart with lineart very low instead of having several vace nodes
  - *From: JmySff*

- **Depth works more reliably than openpose for VACE**
  - Context: VACE video control
  - *From: Piblarg*

- **Use block swap for VACE**
  - Context: Essential when using VACE to prevent VRAM issues, especially with start/end frame nodes
  - *From: Kijai*

- **Use fp8 instead of fp16 for memory efficiency**
  - Context: Enables running 1280x720 on 48GB VRAM, keep VAE on fp16
  - *From: Nathan Shipley*

- **Preview motion with just 3 steps**
  - Context: Can check if motions will be correct early in generation
  - *From: Juampab12*

- **Update BIOS when upgrading to RTX 5090**
  - Context: Important for compatibility when swapping high-end GPUs
  - *From: chrisd0073*

- **Use 41 frames and last frame as first for next batch**
  - Context: Switch before lighting starts to change to avoid color shifts
  - *From: chrisd0073*

- **Change seed by one for extensions**
  - Context: Helps prevent color shift issues when extending videos
  - *From: chrisd0073*

- **Don't use zero_init, zero star itself is fine**
  - Context: General sampler settings
  - *From: Kijai*

- **Avoid fp8_fast as it reduces quality too much**
  - Context: Use alternative mode without ffn layers for better quality
  - *From: Kijai*

- **Position reference images carefully for Phantom**
  - Context: Use 2D board positioning, don't crop smaller than output, mirror edges and blur
  - *From: ▲*

- **For Phantom consistency, describe minimal character details**
  - Context: Just 'a woman drinking' worked better than detailed descriptions
  - *From: Yan*

- **Merge Phantom with T2V model at 0.15-0.25 strength for LoRA compatibility**
  - Context: When using LoRAs with Phantom
  - *From: ▲*

- **Disable TeaCache when using Phantom and CausVid with 10 steps**
  - Context: Quality is much better without TeaCache in this combination
  - *From: Fawks*

- **Use MPS and HPS sparingly with self-forcing model**
  - Context: Can cause hallucinations and artifacts at higher strengths, HPS affects composition while MPS retains it
  - *From: Jonathan*

- **Generate at max resolution (720p) for better mouth movement**
  - Context: Helps significantly with lip-sync and facial animation quality
  - *From: A.I.Warper*

- **Exclude 'talking' token from prompts**
  - Context: Prevents constant mouth jabbering throughout the video
  - *From: A.I.Warper*

- **Use throw away frames at start to deal with flash issues**
  - Context: Can use split images node after VAE decode to remove unwanted initial frames
  - *From: A.I.Warper*

- **Leave NAG blank initially, fix seed, run, then add negative based on results**
  - Context: Better workflow for using Negative Attention Guidance effectively
  - *From: Guey.KhalaMari*

- **Phantom struggles with multiple reference images**
  - Context: Works better with single reference images for consistency
  - *From: Piblarg*

- **Use last frame as first frame approach for long videos**
  - Context: Works best for extending video generations
  - *From: Draken*

- **Use overlapping frames for video extension**
  - Context: Take last 20 frames of generation as first 20 of next to reduce quality loss
  - *From: Colin*

- **Use color match node to maintain consistency**
  - Context: Match all frames to first frame of first generated video
  - *From: Colin*

- **Use reward loras carefully in i2v workflows**
  - Context: Can ruin consistency in image-to-video workflows
  - *From: ▲*

- **Use negative prompting with 'talking, speaking'**
  - Context: May help control mouth movement when using VACE with control
  - *From: David Snow*

- **Use start to end frame for i2v in VACE to avoid same-look generation**
  - Context: When wanting different results from same source
  - *From: Jonathan*

- **Test MPS on closeups to see the difference**
  - Context: MPS effects are more evident on close-up faces
  - *From: ▲*

- **Keep MPS strength below 0.37 for i2v**
  - Context: Higher strengths negatively affect facial resemblance
  - *From: ▲*

- **Drag model files into ComfyUI to see creation workflow**
  - Context: Models with metadata show the merge recipe and settings used
  - *From: VRGameDevGirl84*

- **Use shift value changes to control when denoising happens**
  - Context: Earlier vs later denoising steps for different effects
  - *From: Juampab12*

- **Consider training time vs quality improvement ratio**
  - Context: 4 hours of training increased quality by 4% in referenced study
  - *From: DiXiao*

- **Use lcm + normal scheduler for self-forcing model**
  - Context: Self-forcing kind of requires it
  - *From: yi*

- **Use Deis with beta scheduler instead of UniPC for 1 frame gens**
  - Context: UniPC is very bad for 1 frame generations
  - *From: yi*

- **Start with LCM sampler for new lightX2V lora**
  - Context: Good starting point, works similar to causvid lora
  - *From: Kijai*

- **For ATI with new lora, try strength 1.25 instead of 1.0**
  - Context: Better results with animate-to-image
  - *From: Juampab12*

- **Don't combine lightX2V with causvid - use as replacement**
  - Context: No benefit to using them together
  - *From: Kijai*

- **Use 'reduce noise' in Topaz video AI for face cleanup**
  - Context: Good for cleaning up face debris in videos
  - *From: David Snow*

- **Use MPS LoRA at low weight for consistent quality**
  - Context: MPS is always good to have at a low weight in video generation
  - *From: Ada*

- **Use CausVid 1.5 at lower strengths for sharper videos**
  - Context: CausVid v1.5 produces slightly sharper videos than v2 but requires lower strengths - 0.5 for normal use, 0.2 with merge models
  - *From: David Snow*

- **Save LoRA combinations as node templates**
  - Context: You can save all LoRAs already setup as templates in ComfyUI to avoid reconfiguring each time
  - *From: Nekodificador*

- **Adjust shift values for different schedulers**
  - Context: LightX2V is more sensitive to scheduler/sigmas, adjusting shift is recommended and has big effect on results
  - *From: Kijai*

- **Use CFG 2 for 20% of total steps**
  - Context: Better results than just using with, when using acceleration LoRAs
  - *From: ボグダンおじさん*

- **Keep LoRA strengths low when combining acceleration LoRAs**
  - Context: Too high strength burns the image when combining causvid with other LoRAs
  - *From: David Snow*

- **Use higher LoRA strengths with Phantom**
  - Context: Significantly higher strengths required for accvideo and causvid LoRAs when using with Phantom
  - *From: David Snow*

- **Reference images must match output resolution**
  - Context: For MAGREF model to work properly
  - *From: Draken*

- **Use 0.6-0.8 strength for lightx2v LoRA**
  - Context: 1.0 can sometimes burn, this is decent sweet spot. Higher with Phantom
  - *From: DawnII*

- **SLG causes burning with LightX2V and is not needed**
  - Context: When using the LightX2V LoRA
  - *From: Piblarg*

- **Use closed mouth reference images to reduce excessive mouth movement**
  - Context: When using Phantom model for character consistency
  - *From: Thom293*

- **Add facial expression descriptions to prompt**
  - Context: Helps control facial behavior in Phantom generations
  - *From: ingi // SYSTMS*

- **Always paste back to source video for object removal**
  - Context: To avoid entire image being VAE encoded, only the painted area
  - *From: A.I.Warper*

- **Use self forcing at 1.25 + HPS at 0.2 + MPS at 0.7 with 4 steps**
  - Context: For better results than complex LoRA combinations
  - *From: yi*

- **Don't use AccVideo with self-forcing recipes**
  - Context: AccVideo breaks the effectiveness of self-forcing workflows
  - *From: yi*

- **Use input method instead of ID-based retrieval for widget to string**
  - Context: Node numbers can change making ID method unstable
  - *From: the_darkwatarus_museum*

- **LightX2V should be full strength without SLG**
  - Context: Using SLG breaks LightX2V and is no longer needed
  - *From: Piblarg*

- **Use 4 steps instead of 8 with LightX2V LoRA**
  - Context: Speed optimization with quality LoRAs
  - *From: blake37*

- **Fill VACE masks with gray RGB 123,123,123**
  - Context: For proper inpainting behavior
  - *From: ingi // SYSTMS*

- **Monitor VRAM to be around 95% with block swapping**
  - Context: Optimal performance with 4090
  - *From: Kijai*

- **Use box-shaped masks instead of human-shaped for better prompt following**
  - Context: VACE inpainting
  - *From: ingi // SYSTMS*

- **Enhance-A-Video no longer needed with speed LoRAs**
  - Context: TeaCache in general less relevant with distill loras
  - *From: The Shadow (NYC)*

- **Use higher strength from VACE controls when mixing with Phantom**
  - Context: Requires more strength than VACE alone
  - *From: DawnII*

- **Use rectangular masks with no soft borders for VACE**
  - Context: Works much better than blurred edges
  - *From: Simonj*

- **Use hard mask borders at exactly 127,127,127 RGB for VACE**
  - Context: Blurred edges with wrong gray levels cause bad results
  - *From: MilesCorban*

- **Bump up strength parameter for better I2V results**
  - Context: When using distill LoRAs with multitalk
  - *From: Kijai*

- **Use 34 input frames instead of default 17 for extending**
  - Context: For 10 second videos at 16fps, works well with color match node
  - *From: Colin*

- **Use LightX2V LoRA for better quality**
  - Context: Works well with LCM/simple samplers and provides significant quality improvement
  - *From: MilesCorban*

- **Use stationary camera prompting with multitalk**
  - Context: Helps prevent camera movement that breaks lip sync quality
  - *From: Kijai*

- **Apply uni3c only to first step for camera control**
  - Context: Prevents dampening all motion while still controlling camera movement
  - *From: Kijai*

- **Use audio_scale below 1.0 to reduce multitalk expressiveness**
  - Context: Can tone down overly expressive lip sync, works as low as 0.3
  - *From: CJ*

- **Leave out CLIP vision for better MAGREF reference consistency**
  - Context: Text embeds can still be used, but removing CLIP vision improves character consistency
  - *From: DawnII*

- **Use white canvas/padding when concatenating images for MAGREF**
  - Context: Better results when combining multiple reference images
  - *From: DawnII*

- **Use NAG with lightx distill for negative prompts at CFG 1**
  - Context: When using lightx2v distillation LoRA
  - *From: Screeb*

- **Make frames divisible by 80 then +1 for MultiTalk**
  - Context: For optimal performance with context windows
  - *From: Kijai*

- **Boost distill LoRA strength for similar effect as double CFG**
  - Context: When using distill LoRAs that can't use double CFG
  - *From: Kijai*

- **Click image to zoom in then save to preserve PNG workflow embedding**
  - Context: Discord converts to webp when saving directly, losing embedded workflows
  - *From: phazei*

- **Repeating first frame helps with static camera shots**
  - Context: Using uni3c control for camera guidance
  - *From: Juampab12*

- **Use loudnorm for better MultiTalk results**
  - Context: Model likely trained with audio normalization
  - *From: Kijai*

- **Record yourself talking in middle of room with good articulation**
  - Context: Better reference video for MultiTalk than using random footage
  - *From: Juampab12*

- **Use static camera reference videos for long context generation**
  - Context: Reduces artifacts and repetitive motion in extended videos
  - *From: Juampab12*

- **Set uni3c strength very low to allow more movement**
  - Context: High strength reduces expressiveness too much
  - *From: Kijai*

- **Match frame count for uni3c context windows**
  - Context: Prevents tensor dimension errors
  - *From: Kijai*

- **Use separate TTS feed for MultiTalk, combine audio after**
  - Context: When dealing with MMAudio background noise issues
  - *From: DawnII*

- **Try with MAGREF instead of I2V models**
  - Context: When MultiTalk results aren't satisfactory
  - *From: Kijai*

- **Use git pull from folder instead of manager for Kijai's nodes**
  - Context: Manager doesn't always work properly for updates
  - *From: Thom293*

- **Run vocal separator on MMAudio to remove unwanted voices**
  - Context: When MMAudio adds unwanted vocal sounds
  - *From: burgstall*

- **Frame count must be divisible by (n-1)/4 for long videos**
  - Context: For 60 second video: 60s * 25fps = 1500 frames, but use 1501 frames
  - *From: A.I.Warper*

- **Add 'neutral facial expression' to prompt to reduce unwanted mouth movement**
  - Context: When trying to prevent constant talking/mouth movement in generated videos
  - *From: VRGameDevGirl84*

- **Use closed mouth image and non-expressive face for I2V**
  - Context: To prevent mouths from constantly trying to talk in image-to-video generation
  - *From: Thom293*

- **Can use prompt scheduling with timestep syntax**
  - Context: Format: [0s: description] [5s-10s: description] for different parts of video
  - *From: Bleedy*

- **Add silence before audio and trim first frames to avoid flash**
  - Context: Solution for initial flash problem in lip-sync videos
  - *From: VRGameDevGirl84*

- **Use NAG negative prompts: 'talking, speaking, speak, talk, yelling, yell'**
  - Context: To prevent unwanted mouth movement in video generation
  - *From: humangirltotally*

- **Use NAG sparingly for targeted changes**
  - Context: NAG operates at conceptual level and affects entire composition, so be specific in positive prompt and keep NAG minimal for hair color changes only
  - *From: VRGameDevGirl84(RTX 5090)*

- **Test base model before adding LoRAs**
  - Context: When troubleshooting issues like flux face/chin problems, isolate by testing base model first
  - *From: Guey.KhalaMari*

- **Use low CFG with high NAG influence**
  - Context: CFG 1 with NAG turned up steers very hard away from keywords
  - *From: VRGameDevGirl84(RTX 5090)*

- **Use LightX2V as primary acceleration LoRA**
  - Context: Can switch from 8 steps FusionX workflow to 4 steps with custom mix using LightX2V
  - *From: blake37*

- **Use Audacity to convert audio to 44.1khz for better MultiTalk sync**
  - Context: When preparing audio files for MultiTalk lip sync
  - *From: burgstall*

- **Record phone camera movement for Uni3C instead of 3D rendering**
  - Context: For more organic, handheld camera movement in videos
  - *From: Nekodificador*

- **Remove first frame from VACE morph videos**
  - Context: First frame often looks weird in VACE morphing workflows
  - *From: Dream Making*

- **Use strength 0.3 for Uni3C when driving with motion video**
  - Context: When feeding movement video into Uni3C for camera control
  - *From: AJO*

- **Use self-forcing with exactly 0.25 strength, not 1.0**
  - Context: Otherwise video will be buggy
  - *From: Alisson Pereira*

- **Remove audio input link in video combine node**
  - Context: When you don't want audio from input video
  - *From: hicho*

- **Use empty prompt with random seed for video-to-video**
  - Context: Can work better than using original prompt and seed
  - *From: VRGameDevGirl84(RTX 5090)*

- **Use denoise 0.7 for video-to-video**
  - Context: Good balance for preserving input while allowing changes
  - *From: VRGameDevGirl84(RTX 5090)*

- **12-16 images better than 30+ for character LoRA training**
  - Context: Overtraining limits range of motion in video
  - *From: Jas*

- **Save videos as H264 MP4 with CRF 2 for quality**
  - Context: Instead of WebM or GIF for better quality output
  - *From: Alisson Pereira*

- **Use ChatGPT to create new prompts from first frame for creative upscaling**
  - Context: When doing v2v upscaling for more creative results
  - *From: VRGameDevGirl84(RTX 5090)*

- **Turn off uni3c and context windows for videos under 251 frames**
  - Context: Improves performance and reduces restrictions for shorter videos
  - *From: Juampab12*

- **Include other people/creatures in LoRA training datasets**
  - Context: Prevents LoRA bleeding into other objects in the scene
  - *From: Juampab12*

- **Use smaller shapes with thin borders in VACE**
  - Context: Large shapes or thick borders may show up in output
  - *From: Jonathan*

- **Use ChatGPT to help create prompts from first frame**
  - Context: For upscaling workflows, can give ChatGPT a snippet of first frame to help generate appropriate prompts
  - *From: VRGameDevGirl84(RTX 5090)*

- **Lower denoise keeps closer to input video**
  - Context: Lower denoise values preserve more of the original video but may bring back pixels/noise depending on input quality
  - *From: VRGameDevGirl84(RTX 5090)*

- **Add padding at start for audio sync**
  - Context: Leave padding at the left/start of audio - model needs more time to adapt for better sync
  - *From: Juampab12*

- **Use 'still camera' prompt for context window issues**
  - Context: When using context options with MultiTalk, prompt 'still camera' may help avoid camera movement glitches
  - *From: N0NSens*

- **Use NAG with MultiTalk for better results**
  - Context: Negative words like 'audio out of sync' improve sync quality
  - *From: ZeusZeus (RTX 4090)*

- **Keep denoise low to preserve faces in upscaling**
  - Context: Denoise 0.1-0.2 range, higher values will lose faces
  - *From: N0NSens*

- **Use flowmatch_distill scheduler with distill models**
  - Context: Better quality results when using distilled LoRAs
  - *From: ZeusZeus (RTX 4090)*

- **Avoid emotion prompts with MultiTalk**
  - Context: Don't add prompts like 'smiling, joyful' as they battle with MultiTalk processing
  - *From: Charlie*

- **Use simple prompts like 'high quality video' for upscaling**
  - Context: When doing enhancement/upscaling without caring about losing original face
  - *From: VK (5080 128gb)*

- **Use solid masks without blur for VACE inpainting**
  - Context: When doing character replacement, solid mask without gray fill works better
  - *From: Nekodificador*

- **Split VACE embeds for better control**
  - Context: Use separate VACE embeds for different control types (depth, pose, reference)
  - *From: Nathan Shipley*

- **Reverse video for better SAM2 tracking**
  - Context: If subject isn't visible in first frame, reverse video so they appear first, then re-reverse after masking
  - *From: mdkb*

- **Use SAM2 keyframes for complex masking**
  - Context: Feed multiple frames into SAM2 with different keyframe points to refresh mask info
  - *From: Nekodificador*

- **Low denoise for upscaling**
  - Context: Use denoise 0.1-0.2 with UltraWan for polishing/upscaling without changing characters much
  - *From: mdkb*

- **Remove pose hands and face for cleaner results**
  - Context: When using pose control, disable hands and face detection for better character replacement
  - *From: Nekodificador*

- **Use 3 steps sometimes helps with generation**
  - Context: When experimenting with different settings
  - *From: ▲*

- **Turn up audio gain to 3 in Multitalk**
  - Context: Helps with audio processing quality
  - *From: Thom293*

- **Collapse nodes with Alt+C to manage canvas space**
  - Context: Especially useful with Spline Editor nodes that take up lots of space
  - *From: Nekodificador*

- **Use crop and stitch for faces in upscaling**
  - Context: When using skip layer guidance workflows
  - *From: chrisd0073*

- **Don't use TeaCache with Light LoRA workflows**
  - Context: TeaCache skips steps but Light doesn't have enough steps to skip
  - *From: voxJT*

- **30 fps is sweet spot for Multitalk**
  - Context: 60 fps gets too frenetic, good for rapping but not normal speech
  - *From: voxJT*

- **Use normal maps for better face/lighting details in VACE**
  - Context: When doing video processing with VACE controlnet
  - *From: Tango Adorbo*

- **Set VACE inputs at 25fps to control motion speed**
  - Context: When using VACE for video control
  - *From: Tango Adorbo*

- **Start with lower denoise values for true upscaling**
  - Context: 0.3-0.5 range maintains input video characteristics better than higher values
  - *From: Tango Adorbo*

- **Use 121 frame context for optimal results**
  - Context: Recommended context window size for processing
  - *From: VRGameDevGirl84(RTX 5090)*

- **Use higher context_overlap for longer MultiTalk videos**
  - Context: For videos 321+ frames, set context_overlap to around 64 to prevent extra loops
  - *From: Bleedy (Madham)*

- **Check console for silent LoRA failures**
  - Context: LoRAs can silently fail without UI errors, especially when using wrong model sizes
  - *From: Draken*

- **Use Power LoRA Loader from rgthree for stacking LoRAs**
  - Context: Can stack multiple LoRAs on the same node
  - *From: manu_le_surikhate_gamer*

- **Lower denoise strength for better likeness in upscaling**
  - Context: Drop denoise to around 0.2-0.3 for closer resemblance to original
  - *From: Mathew*

- **Add original prompt for upscaling control**
  - Context: Can help prevent overly creative changes, though works better without prompt for clean upscale
  - *From: zelgo_*

- **Search discord channel for 'context stride' to find existing experiments**
  - Context: When troubleshooting context window issues
  - *From: Faux*

- **Make LightX2V more dominant when combining speed LoRAs**
  - Context: It's the best one by far according to testing
  - *From: David Snow*

- **LightX works well for non-realistic looks but loses cinematic realism**
  - Context: Choose based on speed vs quality needs
  - *From: VRGameDevGirl84(RTX 5090)*

- **For VACE reference image issues, may be using wrong controlnets**
  - Context: Main controlnets (canny, depth, pose) work from start, normals and lineart fail completely
  - *From: mdkb*

- **Use SAM2 points editor with VACE for fast masking**
  - Context: For video masking and object targeting
  - *From: mdkb*

- **Disable MPS or movement loras when using Remade camera loras**
  - Context: Remade loras fight with Fusion X loras
  - *From: mdkb*

- **Use reference image plugged into VACE Wan Encoder for I2V-like functionality**
  - Context: Works well for underlying video passed through controlnet with reference image and prompt
  - *From: mdkb*

- **Cancel generation when first frame appears in points editor, set points, then run again**
  - Context: Workflow for SAM2 point setting
  - *From: mdkb*

- **Offloading to RAM is better than offloading to CPU**
  - Context: For systems that must offload model parts
  - *From: Jonathan*

- **Use spline editor for better camera control than loras**
  - Context: Spline method appears to be top choice for camera movement
  - *From: mdkb*

- **Use scheduling for LoRAs**
  - Context: Try scheduling the lora to be on for last steps but not first steps
  - *From: Piblarg*

- **Add noise when upscaled video gets too smooth**
  - Context: When upscaling results lose fine detail and look too smooth, add noise through the lora or film grain
  - *From: David Snow*

- **UltraWan 1K only works well in landscape**
  - Context: UltraWan 1K does NOT work well on portrait mode, only landscape videos
  - *From: phazei*

- **Use multiple LoRAs together for 1.3B**
  - Context: Use SF DMD FP16 at 0.25, CausVid bidirect2 at 1.0, MPS at 0.25, and UltraWan 1K at 0.25 for best results
  - *From: phazei*

- **Add resolution terms to caption for UltraWan**
  - Context: UltraWan was trained in T2V mode, try adding '4k, hdr, high resolution' to caption when using for upscaling
  - *From: Alisson Pereira*

- **Use distorch loaders from multigpu pack with GGUF files**
  - Context: Works similar to blockswap and keeps browser responsive
  - *From: David Snow*

- **Don't use full CausVid at 1.0 strength**
  - Context: Full CausVid destroys motion, use reduced strength like V2
  - *From: Kijai*

- **Use AccVid I2V lora instead of T2V version for image-to-video**
  - Context: I2V version is 100 times better and fixes problems with T2V lora
  - *From: Jonathan*

- **Try rank 16 extraction at higher weight**
  - Context: Addresses motion and seed variance concerns with LightX2V
  - *From: DawnII*

- **Break long videos into smaller chunks for MultiTalk**
  - Context: Cap around 420 frames at a time with 2 second overlap for matching
  - *From: voxJT*

- **Use negative prompting (nag) for I2V**
  - Context: Very important for image to video generation quality
  - *From: zoz*

- **Prompt I2V differently than T2V**
  - Context: Don't use same prompting approach for image to video as text to video
  - *From: VRGameDevGirl84*

- **Create video with sound first, then use MultiTalk on second pass**
  - Context: Better approach than trying to combine VACE and MultiTalk in single pass
  - *From: VRGameDevGirl84*

- **Use detailed motion descriptions for I2V prompts**
  - Context: Include specific actions like 'first she places cigarette in mouth, then blows smoke' for better results
  - *From: zoz*


## News & Updates

- **Improved i2v accuracy model released**
  - New model version with improved accuracy for image-to-video generation
  - *From: 852話 (hakoniwa)*

- **CausVid v2 and v1.5 variants available**
  - v1.5 has block 0 disabled, v2 has additional blocks disabled but may reduce quality
  - *From: JohnDopamine*

- **BFL promises slightly less quality open source version soon**
  - But concern about slow rollout to normalize API payments
  - *From: JohnDopamine*

- **Stability emailing users to pay for SD3 in ComfyUI**
  - Raises concerns about future free model availability
  - *From: JohnDopamine*

- **50 new LoRAs released for motion control**
  - After Effects and motion control LoRAs like Pika Labs and Higgsfield AI
  - *From: SS*

- **50 new LoRAs for motion control released**
  - Collection of Wan2.1 14B 480p I2V LoRAs for after effects and motion control like Pika Labs
  - *From: SS*

- **CausVid v2 explanation posted**
  - Kijai's detailed explanation of CausVid LoRA differences and usage recommendations
  - *From: MilesCorban*

- **Wan-Toy-Transform LoRA released by Alibaba Research**
  - LoRA finetuned on Wan-I2V-14B-480P that turns things into fluffy toys
  - *From: hicho*

- **VideoX-Fun repo has Wan support for ComfyUI**
  - Alternative ComfyUI implementation: https://github.com/aigc-apps/VideoX-Fun
  - *From: hicho*

- **Enhance-A-Video node available for Wan**
  - Video enhancement functionality from NUS-HPC-AI-Lab repo
  - *From: fazeaction*

- **ATI official trajectory editor released**
  - Official editor uploaded to ByteDance ATI repo with timeline support
  - *From: Juampab12*

- **New ComfyUI VACE advanced node released**
  - BigStationW released ComfyUi-WanVaceToVideoAdvanced with enhanced features
  - *From: hicho*

- **Official ATI web app released for creating trajectories**
  - ByteDance released official trajectory creation tool
  - *From: TK_999*

- **ContentV-8B model released by ByteDance**
  - Efficient DiT-based video generation model, reuses SD3.5
  - *From: ramonguthrie*

- **New lipsync project OmniSync announced**
  - May not be open source
  - *From: hau*

- **AccVideo I2V 14B version now available**
  - New I2V version released on HuggingFace
  - *From: yi*

- **FlowMo paper for improving WAN 2.1 motions**
  - Significantly improves motions but doubles inference time, easy to implement
  - *From: yi*

- **4-bit quantization coming to WAN 2.1**
  - MIT han-lab working on 4-bit WAN support, 4-bit T5 encoder already released
  - *From: Mngbg*

- **FlowMo implementation pushed for testing**
  - Kijai has pushed FlowMo implementation for community testing
  - *From: Kijai*

- **Gaze control ComfyUI node released**
  - New gaze control preprocessing node available on GitHub
  - *From: Mads Hagbarth Damsbo*

- **AccVid released an I2V model**
  - New I2V model available for testing
  - *From: JohnDopamine*

- **Point tracking now available**
  - CoTracker node released: https://github.com/s9roll7/comfyui_cotracker_node
  - *From: tttADs*

- **Multiple splines now available in ATI**
  - Multiple spline support added to spline editor
  - *From: Kijai*

- **CausVid v2 released**
  - CausVid v2 available, needed if you want to use CFG, should drop AccVid when using CFG with v2
  - *From: Kijai*

- **Banodoco Wan Video Discussion KB created**
  - Public NotebookLM knowledge base with scraped Wan channel discussions: https://notebooklm.google.com/notebook/a08901b9-0511-4926-bbf8-3c86a12dc306
  - *From: Nathan Shipley*

- **DCM distillation method available**
  - New distillation technique for Wan models, currently only 1.3B version available
  - *From: yi*

- **VRGameDevGirl84 releases master merge model**
  - Wan14BT2V_MasterModel with CausVid baked in, no LoRAs needed, 8-10 steps
  - *From: VRGameDevGirl84(RTX 5090)*

- **Wan 3.1 announced**
  - Will feature infinite length 1080p encoding with VAE and audio capabilities, though no ETA provided
  - *From: ZeusZeus (RTX 4090)*

- **Context splitting code not yet implemented**
  - Kijai hasn't added the code for splitting input for longer context yet
  - *From: Kijai*

- **Phantom merge not yet published**
  - VRGameDevGirl84 has not published the phantom merge yet
  - *From: VRGameDevGirl84(RTX 5090)*

- **A.I.Warper released ComfyUI-WarperNodes**
  - New node collection including mouth tracking using pose coordinates, available on GitHub
  - *From: A.I.Warper*

- **Video Depth Anything modified for better VRAM management**
  - Updated to properly offload models and avoid xformers dependency, tested on 300+ frames
  - *From: A.I.Warper*

- **Multiple splines support added to ATI**
  - Can now use multiple splines on single canvas instead of requiring multiple canvases
  - *From: Kijai*

- **Fixed enhance patch that was disabling sageattention**
  - Applied fix that seems to work for better performance
  - *From: Kijai*

- **ATI support for native workflows is simple to add**
  - Kijai confirmed it can be added with little effort
  - *From: Kijai*

- **AniSora V2 model added to benchmark**
  - Seen in AniSora repo, though no guarantee of public release
  - *From: DevouredBeef*

- **Wan paper mentions unreleased features**
  - Audio generation model and VACE for images mentioned in paper but not released
  - *From: Jonathan*

- **VRGameDevGirl84 created Phantom merge model**
  - Phantom merge model uploaded to CivitAI with specific workflow and settings
  - *From: VRGameDevGirl84(RTX 5090)*

- **MultiTalk lip-sync model released by MeiGen-AI**
  - New lip-sync technology with impressive quality, appears to be I2V based due to character consistency in zoom-ins
  - *From: toyxyz*

- **SkyReels-Audio published technical report**
  - Omni Audio-Conditioned Talking Portraits in Video Diffusion Transformers, released June 1, 2025
  - *From: hicho*

- **Wan 1.3B I2V models exist and are underrated**
  - Both Alibaba Fun InP 1.3B I2V and SkyReels V2 I2V 1.3B 540P available, can generate up to 60s video
  - *From: hicho*

- **Fixed patch nodes for VACE compatibility**
  - TeaCache now works, enhance-a-video fixed, new compile works without awkward weight order patch
  - *From: Kijai*

- **Native Phantom implementation available**
  - Implemented via WanPhantomSubjectToVideo node in ComfyUI
  - *From: lym0*

- **MultiTalk weights released**
  - Wan-based lip-sync model with 480p single GPU, 720p multi-GPU requirements
  - *From: ZeusZeus*

- **Self-forcing model released by Adobe**
  - Frame-by-frame autoregressive generation method for Wan 1.3B T2V, trained in 2 hours
  - *From: multiple users*

- **FusionX model released**
  - Model merge by user with CausVid and other components baked in
  - *From: Juan Gea*

- **SkyReels V2 released**
  - Updated version with native 121f and 97f models for ~5 second generation
  - *From: Impactframes*

- **Kijai added QoL updates to nodes**
  - New spline editor features, spawn under cursor functionality
  - *From: Kijai*

- **Self-Forcing models released**
  - New autoregressive diffusion models from gdhe17 available on HuggingFace, only 1.3B parameter size currently
  - *From: MysteryShack*

- **WAN 1.3B model with layer support released**
  - Kijai mentions new WAN 1.3B model that supports layers and uses VACE
  - *From: Kijai*

- **Wrapper node fixed for disconnection issues**
  - Recent update to Kijai's wrapper resolves ComfyUI disconnection problems
  - *From: JohnDopamine*

- **Self-forcing Wan models released with VACE merge**
  - Available on HuggingFace as merge of Self-Forcing and Wan2.1-VACE-1.3B
  - *From: hicho*

- **VACE+Phantom merge model released**
  - Available on HuggingFace for native ComfyUI use
  - *From: Piblarg*

- **Multiple spline support added to spline editor**
  - Latest KJNodes update enables multiple spline creation
  - *From: Nathan Shipley*

- **MultiTalk team considering ComfyUI support**
  - Community pressure for ComfyUI integration, as adoption requires ComfyUI support
  - *From: ZeusZeus*

- **MagCache speed optimization released**
  - New caching method that could provide 3x speed improvements, similar to improved TeaCache
  - *From: MaQue*

- **SeedVR video super resolution models available**
  - Video super resolution by StableSR creators, models on HuggingFace with GitHub repo posted
  - *From: JohnDopamine*

- **Disney suing Midjourney over AI-generated characters**
  - Lawsuit claims Midjourney used and distributed AI-generated characters from Star Wars, The Simpsons and other films
  - *From: Level Higher*

- **MultiTalk devs added ComfyUI to task list**
  - As result of discussion with dev, they added ComfyUI support to their roadmap
  - *From: ZeusZeus (RTX 4090)*

- **MagCache ComfyUI nodes released**
  - ComfyUI nodes from MagCache author now available
  - *From: yi*

- **SageAttention code release dates announced**
  - SageAttention2++ code releasing June 15, SageAttention3 code releasing July 10
  - *From: Raphaël*

- **NAG support merged into WanVideoWrapper**
  - Normalized Attention Guidance from official demo integrated, basically CFG distillation
  - *From: Kijai*

- **New Cosmos models released**
  - Nvidia released Cosmos Predict2 models supposedly beating Wan
  - *From: ZeusZeus (RTX 4090)*

- **Topaz new AI upscaler released**
  - New upscaler model in early access, very slow but high quality
  - *From: hicho*

- **SeedVR2-3B released**
  - ByteDance released SeedVR2-3B which could be good diffusion-based upscaler
  - *From: hicho*

- **LoRAEdit project released**
  - New project for LoRA editing, forked from diffusion-pipe
  - *From: toyxyz*

- **New ContentV-8B model from ByteDance**
  - WAN-based model released, uses WAN VAE
  - *From: hicho*

- **NVIDIA Cosmos Predict2 models released**
  - 14B and 2B variants, uses WAN architecture and VAE, focused on robotics/autonomous driving
  - *From: Ada*

- **Magic-TryOn project based on WAN 2.1**
  - WAN 2.1 repo updated to mention this new project
  - *From: JohnDopamine*

- **HyperMotion controlnets for WAN coming**
  - Weights will be released this month
  - *From: yi*

- **Self-forcing model available as Wan 1.3B variant**
  - Claims real-time HD video generation at 17 FPS on H100 with sub-second latency
  - *From: SS*

- **LightX2V team made 14B cfg+step distill model**
  - Should work better in normal workflows than CausVid, also working on 14B self-forcing
  - *From: Kijai*

- **HyperMotion weights released on HuggingFace**
  - Available at huggingface.co/shuolin/HyperMotion/tree/main
  - *From: yi*

- **Phantom 14B pro still to be released**
  - Upcoming release mentioned by ZeusZeus
  - *From: ZeusZeus (RTX 4090)*

- **ComfyUI Nodes v3 live Office Hour announced**
  - Friday June 13th 7pm PST / 10pm EST with core team
  - *From: SS*

- **Sage 2 expected June 15/19**
  - New version should provide speed improvements
  - *From: JohnDopamine*

- **Sage3 will be 5000 series GPU only**
  - Sage2++ will probably work on 3000 series and up
  - *From: Kijai*

- **Cosmos Predict2 now works in native ComfyUI**
  - Recent commit enables native support, uses Wan2.1 VAE
  - *From: JohnDopamine*

- **Wan 3.1 coming in couple months**
  - Will have infinite length videos with audio, speculation based on 2.1 capabilities
  - *From: Jonathan*

- **Sage Attention 2++ release slipping to January 20th**
  - Delayed from original schedule
  - *From: blake37*

- **New research paper on video generation training efficiency**
  - Claims code and models coming soon, trained on 1.3B model
  - *From: yi*

- **GigaVideo-1 research published**
  - New approach to video generation training
  - *From: yi*

- **No 14B self-forcing model coming**
  - Based on Chinese discussion suggesting only 1.3B version in development
  - *From: hicho*

- **Points editor app nearly ready for release**
  - Should be available tomorrow, with skeleton rigging capabilities
  - *From: Juampab12*

- **LightX2V Wan2.1 T2V 14B StepDistill-CfgDistill model released**
  - 4-step distillation model for faster inference, comparable to accvideo
  - *From: yi*

- **Kijai extracted LightX2V as LoRA**
  - Available as Wan21_T2V_14B_lightx2v_cfg_step_distill_lora_rank32.safetensors
  - *From: Kijai*

- **SeedVR upscaling tool announced**
  - Free diffusion-based upscaler, can upscale 420p to 1080p in single step, waiting for ComfyUI version
  - *From: shockgun*

- **Renamon Digimon Video lora updated**
  - Available on community channel
  - *From: MisterMango*

- **Self-Forcing 14B LoRA released**
  - Self-forcing for 14B model is now available and can be used in both native ComfyUI and wrapper implementations
  - *From: mamad8*

- **New LightX2V speed LoRA available**
  - Wan21_T2V_14B_lightx2v_cfg_step_distill_lora_rank32.safetensors released on Kijai's HuggingFace repo
  - *From: David Snow*

- **MAGREF weights released**
  - MAGREF-Video model weights available on HuggingFace
  - *From: yi*

- **MinimaxRemover support added**
  - Kijai added MinimaxRemover support - 1.3B model without crossattn, no prompts needed
  - *From: Kijai*

- **Kijai taking week break from midsummer**
  - Planning to take a break for about a week starting from midsummer
  - *From: Kijai*

- **MAGREF developers posted update about new model coming**
  - Updated model will be released down the road according to recent post
  - *From: JohnDopamine*

- **Cosmos_predict2 released weights**
  - Can now use it to create backgrounds and then use VACE to inpaint consistent characters
  - *From: Fawks*

- **LatentSync 1.6 now available with 512s training**
  - New model trained on 512 second clips
  - *From: A.I.Warper*

- **MultiTalk project released for audio-driven lip sync**
  - Can generate up to 201 frames, uses 14B model with 9GB additional size, does three passes making it slow
  - *From: Kijai*

- **Widget to string node issue identified and fix available**
  - Code causing re-evaluation can be commented out, may not be needed anymore due to ComfyUI execution order changes
  - *From: Kijai*

- **MultiTalk implementation in wrapper**
  - Single talking without frame extension, on multitalk branch - incomplete/experimental
  - *From: Kijai*

- **Kijai going on vacation**
  - Leaving Saturday, winding down development
  - *From: Kijai*

- **Midjourney Video Model v1 released**
  - I2V only, up to 21 seconds, $0.33 per second pricing
  - *From: Jonathan*

- **New distillation model released**
  - lightx2v/Wan2.1-T2V-14B-StepDistill-CfgDistill without causal aspect, just distillation
  - *From: Kijai*

- **Chattable NotebookLM Knowledge Base updated with FusionX information**
  - Current as of yesterday, includes utilities to create custom knowledge bases
  - *From: Nathan Shipley*

- **MagRef I2V model available**
  - Similar to Phantom model
  - *From: zelgo_*

- **Video super resolution using Stable Diffusion paper released**
  - Models apparently coming soon
  - *From: yi*

- **Multitalk implementation available in Kijai's wrapper**
  - Available in separate branch, work in progress implementation of lip sync functionality
  - *From: Kijai*

- **UltraWan LoRA released**
  - 4K dataset trained LoRA for Wan-T2V-1.3B, includes captioned dataset
  - *From: yi*

- **MAGREF model now available**
  - I2V model with improved character consistency, released just a few days ago
  - *From: Kijai*

- **Kijai released pruned fp8 MultiTalk model**
  - WanVideo_2_1_Multitalk_14B_fp8_e4m3fn.safetensors - saves disk space and loading time
  - *From: Kijai*

- **MultiTalk currently on separate branch**
  - Works for single subjects but not finished, available on multitalk branch of WanVideoWrapper
  - *From: Kijai*

- **MultiTalk branch updated with uni3c context window support**
  - Can now handle more than 81 frames without errors
  - *From: Kijai*

- **New 1.3B Wan model trained with 1080p and 4K data**
  - UltraWanComfy model available, likely trained on video podcasts
  - *From: Juampab12*

- **Kijai going away for a week**
  - Development will pause, MultiTalk features like 2-person chat will be delayed
  - *From: Kijai*

- **MultiTalk now available in separate branch**
  - Currently in its own branch, need to manually switch to multitalk branch to access
  - *From: Kijai*

- **MultiTalk file size reduced to 2GB**
  - Recent optimization made the model much smaller
  - *From: hicho*

- **Tencent songgen now works with English**
  - They updated code and weights within the last week, now works with English audio
  - *From: DawnII*

- **Multiple new releases in one week**
  - MAGREF, MultiTalk, MinimaxRemover, UltraWan, Lightx2v distill, and NAG all released
  - *From: phazei*

- **UltraWan LoRA available for 1.3B model**
  - High-resolution LoRA trained on UltraVideo dataset for 4k and 8k generation
  - *From: TK_999*

- **Superres LoRA released for 1.3B model**
  - New LoRA that enables 4k generation with 1.3B model
  - *From: JohnDopamine*

- **ChatterBox TTS integration available**
  - ComfyUI node for text-to-speech using any voice sample
  - *From: CJ*

- **Flux NAG implementation coming this week**
  - Developer confirmed Flux pipeline will be released this week for NAG node
  - *From: JohnDopamine*

- **New SeedVR2 VideoUpscaler released**
  - New upscaling tool available but very slow - 10 minutes for 1 second on 4090
  - *From: hicho*

- **MagRef update coming with more diverse dataset**
  - Official repo indicates update coming to address current limitations
  - *From: JohnDopamine*

- **MultiTalk main repo updated download link**
  - May fix issues with model loading
  - *From: JohnDopamine*

- **Kijai on vacation for about a week**
  - Main WanVideoWrapper developer is on vacation, MultiTalk branch updates paused
  - *From: Nekodificador*

- **LoRAEdit released for better VACE inpainting**
  - New tool that preserves more context than standard VACE inpaint by not completely blocking reference
  - *From: hablaba*

- **MultiTalk support added to WanVideoWrapper**
  - Kijai added MultiTalk support in separate branch
  - *From: orabazes*

- **Chatterbox integration working with Wan ecosystem**
  - Voice cloning and TTS now available in ComfyUI workflows
  - *From: VRGameDevGirl84(RTX 5090)*

- **New continuation node created by pom**
  - Made PR to fix continuations color distortion and detail loss problems
  - *From: pom*

- **SkyReels V2 models available**
  - SkyReels-V2-I2V-1.3B-540P released on HuggingFace
  - *From: Colin*

- **Pom released a continuation node for longer video generation**
  - Works with 81 frame chunks for extended video generation
  - *From: JohnDopamine*

- **Modified MultiTalk code available for VACE compatibility**
  - Code modification allows MultiTalk to work with VACE T2V
  - *From: VRGameDevGirl84(RTX 5090)*

- **LightX2V commit update available**
  - New commit available on ModelTC/lightx2v repository
  - *From: yi*

- **Kijai on vacation until Saturday/Sunday**
  - Main developer away, community exploring other pipeline parts during break
  - *From: burgstall*

- **Modified WanVideoWrapper available**
  - Temporary fork available that allows VACE and MultiTalk to work together
  - *From: Tango Adorbo*

- **SwapAnyHead new paper released**
  - New research paper on head swapping technology
  - *From: hicho*

- **SageAttention early access available**
  - Early access to Sage update available at github commit d64abd1626ccec3f45681b7583d9cb4221f710db
  - *From: JohnDopamine*

- **MultiTalk is available but not finalized**
  - Available in separate branch of WAN wrapper nodes, Kijai on vacation so more development expected later
  - *From: phazei*

- **Multitalk now available in branch**
  - Available via git pull && git checkout multitalk command
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Wan LCM Accelerator LoRA released on Civitai**
  - Rank 16 extraction of lightx2v Wan2.1-T2V-14B-StepDistill-CfgDistill
  - *From: hicho*

- **Alisson Pereira released UltraWan LoRA V2**
  - Trained on better dataset using YouTube videos processed with Topaz and After Effects, used Automagic optimizer with individual learning rates per parameter
  - *From: Alisson Pereira*

- **Ratatoskr Wan 2.1 I2V model released**
  - Full finetune for animal/creature/furry content using DiffSynth, possibly also merged LoRAs
  - *From: Alisson Pereira*

- **Ostris released a LoRA trainer for OmniGen2**
  - New training capability available for OmniGen2 model
  - *From: A.I.Warper*

- **Native ComfyUI context options for VACE releasing soon**
  - Context options for native VACE workflow expected to release tomorrow
  - *From: the_darkwatarus_museum*

- **New SOTA depth model available**
  - Aether from OpenRobotLab - more than just depth, includes temporal consistency
  - *From: samhodge*

- **FLUX Kontext Dev released with open weights**
  - Available in native ComfyUI, image editing model similar to phantom but for images
  - *From: A.I.Warper*

- **Wan Audio branch discovered in LightX2V**
  - Image and audio to video with audio generation, similar to MultiTalk but potentially more flexible
  - *From: yi*

- **FLUX Kontext GGUF models available**
  - GGUF quantized versions released
  - *From: DawnII*

- **Kontext weights are out**
  - Release announcement
  - *From: burgstall*

- **Flux updated their license to restrict commercial use more strictly**
  - Cannot receive direct or indirect payment from model output, affects dev model not schnell
  - *From: Piblarg*

- **Spline Path Control v2.3 released**
  - Added Multi-Editing, Curve Editors for Easing and Scale, UI overhaul with dark/light themes, CTRL+V image pasting, Delete key support, and many quality of life changes
  - *From: Jonathan*

- **NAG node available for Native**
  - KJ has made a NAG node for native ComfyUI, still in beta but part of the KJ nodes pack
  - *From: zelgo_*

- **Boolean invert node added to MTB**
  - Added NOT functionality for automated logic - true becomes false, false becomes true
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Wan 2.2 beta access given at ModelScope conference**
  - Beta access for Wan 2.2 given out at ModelScope conference in China. Structure hasn't changed so VACE etc. will work for it
  - *From: pom*

- **FusionX mentioned in Wan 2.2 conference slide**
  - FusionX was mentioned on conference slide with Chinese text translating to 'open source integration package'
  - *From: Screeb*

- **Sage Attention 2 Plus speed boost negligible**
  - With Sage Attention 2 Plus activated, speed boost is negligible - gens that took 660 seconds now take around 650
  - *From: blake37*

- **Wan 2.2 imminent arrival confirmed**
  - Tweet confirms open source release but not from official sources yet
  - *From: pom*

- **Anicrafter released on HuggingFace**
  - MyNiuuu/Anicrafter_release is now available
  - *From: DawnII*

- **Radial Attention mechanism released**
  - MIT, NVIDIA, Princeton released O(n log n) attention mechanism with 1.9x faster inference, 4x longer videos, 4.4x reduced training costs
  - *From: yo9o*


## Workflows & Use Cases

- **AccVid + CausVid 3-step generation**
  - Use case: Fast high-quality video generation with AccVid 1.5 + CausVid 0.5 at 3 steps
  - *From: Jonathan*

- **Phantom with VACE control using real images**
  - Use case: Character-consistent video generation without controlnet preprocessing
  - *From: JohnDopamine*

- **Video inpainting with Phantom embeds + VACE**
  - Use case: Cut off between 0.2-0.5 of steps for better inpainting seams
  - *From: Zuko*

- **Kontext for first frame generation in Wan**
  - Use case: Generate start and end frames for video workflows
  - *From: Flipping Sigmas/Nekodificador*

- **Video upscaling with tiled approach**
  - Use case: 33 frame vid from 640x960 to 1288x1864 in 8 minutes using CausVid/AccVid
  - *From: Persoon*

- **Vid2vid in Native ComfyUI**
  - Use case: Run image sequence through encode/decode and Wan T2V with low denoise
  - *From: Persoon*

- **Batch prompting for scene generation**
  - Use case: Creating full scenes with different camera angles, stitches segments together
  - *From: VRGameDevGirl84(RTX 5090)*

- **Detail Transfer with mouth masking**
  - Use case: Improving lip sync by transferring mouth details from source
  - *From: A.I.Warper*

- **DWpose with face deactivated + FYE landmarks**
  - Use case: Using image blend node set to screen for facial landmarks while using DWpose for body
  - *From: A.I.Warper*

- **Face enhancement workflow**
  - Use case: Improving facial expressions in videos by processing face areas separately
  - *From: DeZoomer*

- **VACE keyframe interpolation**
  - Use case: Creating in-between frames by inserting gray frames with proper masks
  - *From: Nekodificador*

- **Batch prompting for frame extension**
  - Use case: Extending video length by looping through a batch of prompts and stitching them together
  - *From: VRGameDevGirl84*

- **ATI trajectory visualization**
  - Use case: Creating precise motion control using coordinate trajectories
  - *From: Juampab12*

- **VACE face swapping with pose control**
  - Use case: Face replacement in videos using reference images and pose guidance
  - *From: AJO*

- **Multi-controlnet setup with pose, depth, normals and masking**
  - Use case: Comprehensive video control while retaining background
  - *From: MilesCorban*

- **Single frame scribble to video generation**
  - Use case: Creating video from single sketch input using scribble-trained models
  - *From: TK_999*

- **Complete VACE face swap rewrite replacing Reactor**
  - Use case: Face consistency across video scenes, takes 950 seconds
  - *From: AJO*

- **OpenPose to ATI conversion**
  - Use case: Converting pose keypoints to trajectory coordinates for motion control
  - *From: toyxyz*

- **Low weight depth + reference image for style control**
  - Use case: 162 frame generation with style consistency
  - *From: A.I.Warper*

- **Motion transfer using VACE with depth preprocessor**
  - Use case: Changing car and environment while keeping original motion from driving footage
  - *From: chrisd0073*

- **Uni3C for camera trajectory control**
  - Use case: Following perspective changes of reference video for precise camera movement
  - *From: Johnjohn7855*

- **First/Last Frame morphing workflow**
  - Use case: Video extension using FLF2V template with image inputs
  - *From: Juan Gea*

- **Static scene generation with I2V + controlnet**
  - Use case: High resolution static scene generation at 1536x1024
  - *From: mamad8*

- **3D point cloud to trajectory conversion**
  - Use case: Generate precise motion vectors for ATI motion control from 3D data
  - *From: Juampab12*

- **LoRA testing workflow created**
  - Use case: Centralized place for testing and documenting LoRA experiments
  - *From: VRGameDevGirl84(RTX 5090)*

- **Video enhancement with Topaz upscale and interpolation**
  - Use case: Post-processing WAN outputs for higher quality
  - *From: CJ*

- **2-step AccVid testing methodology**
  - Use case: Testing AccVid performance at different steps and strengths
  - *From: Jonathan*

- **2-step CausVid workflow for quick testing**
  - Use case: Fast movement testing, can bump to 3 steps if needed
  - *From: Jonathan*

- **Phantom + CausVid combination**
  - Use case: Better results than other combinations in experiments
  - *From: AJO*

- **Multiple VACE embeds vs merged controls**
  - Use case: Chain prev_embeds input for multiple controls, more reliable than merge
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Two-stage sampling with different LoRAs**
  - Use case: Stage 1: AccVid with 4 steps for motion, Stage 2: remaining 6 steps with CausVid
  - *From: MilesCorban*

- **Multi-step upscaling pipeline**
  - Use case: Wan T2V + Vace → AE with Neat Video denoising → AnimateDiff upscale → Topaz 4x upscale
  - *From: Gavmakes*

- **VACE keyframes with 3 images**
  - Use case: Start, middle, and end keyframe workflow for controlled animation
  - *From: sneako1234*

- **Model merging using load diffusion model, then loraloadermodelonly then modelsave**
  - Use case: Creating custom merged models with multiple loras
  - *From: VRGameDevGirl84(RTX 5090)*

- **Using VACE with depth pass isolation and layer movement**
  - Use case: Foreground removal and subject repositioning
  - *From: samhodge*

- **Multi-controlnet testing system**
  - Use case: Extracts all control types, saves as videos, then tests each one with queue system using switch
  - *From: Gateway {Dreaming Computers}*

- **LLM-generated prompting system**
  - Use case: Uses 4 LLMs generating prompting across different stages for better results
  - *From: AJO*

- **Camera change with VACE inpainting**
  - Use case: Creating angle changes and camera movements, can be used with other video models like LTXV
  - *From: toyxyz*

- **VACE + Phantom combination**
  - Use case: Use VACE control with Phantom by scheduling to different timesteps or adjusting strengths
  - *From: Kijai*

- **3-stage agentic costume design**
  - Use case: 1) Interpret story arc, 2) Use Flux to produce designs, 3) Apply to video generation
  - *From: AJO*

- **Selective mouth detail enhancement using pose tracking**
  - Use case: Adding detail to mouth area only in low resolution videos using tracked coordinates
  - *From: A.I.Warper*

- **Q8 720x1280x73f on 12GB VRAM**
  - Use case: High quality I2V generation with specific LoRA combinations and optimized settings
  - *From: The Punisher*

- **VACE inpainting with proper mask conversion**
  - Use case: Video inpainting with correct grey mask values
  - *From: David Snow*

- **Multiple VACE encodes at lower strengths**
  - Use case: Improved video quality with multiple control inputs
  - *From: David Snow*

- **Two sampler approach for lora injection**
  - Use case: Split process to control when lora affects generation
  - *From: Kijai*

- **Using trajectory resize script for different resolutions**
  - Use case: When you need to resize ComfyUI image without screwing up point trajectories
  - *From: Juampab12*

- **GGUF workflow for long high-res videos**
  - Use case: 120 frame I2V at 1280x848 on 5090 in under 5 minutes with 4 steps
  - *From: blake37*

- **T2V > DF extend > V2V pipeline**
  - Use case: Creating longer videos with quality improvement pass
  - *From: Colin*

- **Video extension using last frames as input**
  - Use case: Extending videos by taking end frames and using as context for DF
  - *From: Colin*

- **V2V pass after initial generation**
  - Use case: Like 'hires fix' for images - improves quality of initial video generation
  - *From: Colin*

- **VACE start/end frame morphing with T2V LoRA**
  - Use case: Creating smooth transitions between generated frames
  - *From: Dream Making*

- **Generate 162 frames at reduced resolution then upscale with Topaz**
  - Use case: Creating longer videos when context options cause issues
  - *From: Nekodificador*

- **Multiple 81 frame videos stitched together with last frame overlap**
  - Use case: Creating longer sequences while maintaining motion continuity
  - *From: chrisd0073*

- **Separate workflows for building reference and generating video**
  - Use case: VACE technique with better organization of the process
  - *From: Nekodificador*

- **Phantom and VACE inpainting combination**
  - Use case: Advanced facial expression and lighting control with second/third pass capability
  - *From: chrisd0073*

- **Using Latent Bridge Matching for cleanup**
  - Use case: Clean up background from people, leaving only subject over background as reference
  - *From: chrisd0073*

- **Phantom with HiDream for car variations**
  - Use case: Create multiple car design variations while retaining base shape
  - *From: David Snow*

- **Skip Layer Guidance two-pass workflow**
  - Use case: Fixing screendoor artifacts in high-frequency details using V2V second pass with low denoise
  - *From: chrisd0073*

- **Self-forcing with VACE**
  - Use case: Fast I2V generation using T2V self-forcing model with VACE conditioning
  - *From: slmonker*

- **Self-Forcing for rapid iteration**
  - Use case: Fast video generation at acceptable quality for users who prioritize speed over maximum quality
  - *From: Jonathan*

- **VACE + Phantom with depth control**
  - Use case: Character consistency with environmental depth guidance, though may cause frame sampling issues
  - *From: ingi // SYSTMS*

- **Widescreen film resolution generation**
  - Use case: 1472x626 resolution for 2.35-2.40:1 aspect ratios with same pixel count as 720p
  - *From: Ruairi Robinson*

- **Loop video creation with VACE**
  - Use case: Creating seamless video loops with natural flow
  - *From: toyxyz*

- **VACE i2v with reference image workflow**
  - Use case: Image-to-video generation using VACE conditioning
  - *From: chrisd0073*

- **Parallel VACE+Phantom generation**
  - Use case: Character consistency with motion control by running both conditioning systems together
  - *From: Piblarg*

- **Phantom + VACE for character swapping**
  - Use case: Generate starting frame with Phantom, then use with VACE for character consistency
  - *From: Piblarg*

- **Character lora training on cloud then VACE usage**
  - Use case: Train character lora on Replicate in 20 minutes, then use with VACE for perfect character consistency
  - *From: Ruairi Robinson*

- **Float + VACE outpainting for talking characters**
  - Use case: Create AI character final frame cropped neck up for Float at 24fps, then VACE outpainting with Skyreels
  - *From: TRASHTRASH*

- **After Effects animation to ATI/Spline Editor conversion**
  - Use case: Converting AE keyframes to ComfyUI trajectories for video generation
  - *From: Nathan Shipley*

- **Long video generation with frame batching**
  - Use case: 243 frames stitched from 3 batches of 81 frames each, using custom node to extract final frame as start frame of next batch
  - *From: A.I.Warper*

- **Automatic width/height assignment for video aspect ratios**
  - Use case: Sets proper width and height automatically based on input video (landscape or portrait) to avoid manual swapping
  - *From: Gateway {Dreaming Computers}*

- **VACE + Phantom merge workflow**
  - Use case: Control video with VACE and use image reference with Phantom simultaneously
  - *From: JmySff*

- **VACE inpainting with Phantom embeds**
  - Use case: Character replacement and face swapping at VFX quality
  - *From: David Snow*

- **Batch stitching with 5*41 frames**
  - Use case: Creating longer videos by merging 41-frame batches with last frame as first frame of next
  - *From: A.I.Warper*

- **ATI/After Effects puppet tool preview**
  - Use case: Using puppet tool to animate character as preview before Wan render
  - *From: Mickmumpitz*

- **Video background swap with VACE**
  - Use case: Replacing backgrounds in videos
  - *From: SS*

- **Phantom with pose control and reference image**
  - Use case: Character consistency with motion adaptation - input pose video modified by prompt instructions
  - *From: Yan*

- **VACE + Phantom combination**
  - Use case: Character generation with motion, works similar to VACE
  - *From: chrisd0073*

- **Compositing reference images before Phantom input**
  - Use case: Better character consistency by positioning references on 2D board
  - *From: ▲*

- **Self-forcing model workflow**
  - Use case: Can replace any 1.3B or 14B workflow for t2v and vace, use vace with start frame for i2v
  - *From: Jonathan*

- **Phantom/VACE merge workflow**
  - Use case: Character consistency with VACE controls, though can be finicky
  - *From: Piblarg*

- **Camera movement with splines in VACE**
  - Use case: Control camera movement, rotation, and zoom using background splines
  - *From: Jonathan*

- **Video looping with batch stringing**
  - Use case: Using last frame of previous batch as start of next, VRAM intensive but works well
  - *From: Flipping Sigmas*

- **VACE i2v using start frame only**
  - Use case: Image to video generation with better stability than standard i2v
  - *From: David Snow*

- **Overlapping frame video extension**
  - Use case: Creating longer videos (160+ frames) with maintained quality using 34 frame overlap
  - *From: Colin*

- **Phantom + VACE for extended i2v**
  - Use case: Generate up to 121 frames at 24fps with better face stability
  - *From: David Snow*

- **Skeleton rig trajectory creation**
  - Use case: Better control for specific movements that are hard to achieve with text prompts
  - *From: Juampab12*

- **Tiled upscaling for Full HD generation**
  - Use case: Upscaling 14B model outputs without OOM on 4090
  - *From: David Snow*

- **Track points on face and place on another face for trajectories**
  - Use case: Better control than VACE for facial animation
  - *From: Juampab12*

- **Chaining multiple VACE samplers with overlap**
  - Use case: Long-form video generation with frame overlap control
  - *From: the_darkwatarus_museum*

- **Using VACE for inpainting empty middle parts of frames**
  - Use case: Style transfer from outer frames to fill missing content
  - *From: Mngbg*

- **FPS conversion calculator for Rife**
  - Use case: Converting 16fps Wan output to 24/25/30fps for matching other tools
  - *From: AJO*

- **Two-pass workflow with Skip layer guidance**
  - Use case: Adding clarity to lowres generated videos using v2v with very low denoise
  - *From: chrisd0073*

- **Tiled sampling using Ultimate SD Upscale**
  - Use case: Video upscaling while maintaining temporal consistency
  - *From: David Snow*

- **Voice addition to long video**
  - Use case: Creating looping video with Wan then retouching face with Live Portrait
  - *From: toyxyz*

- **Skip layer guidance for fixing tiled upscale seams**
  - Use case: Fixing seams on tiled upscaled video, tested with 1.3b model
  - *From: chrisd0073*

- **VACE inpaint + pose combined workflow**
  - Use case: Combining pose control with inpainting by blending pose into mid grey mask using single VACE encode
  - *From: David Snow*

- **Separate control videos workflow**
  - Use case: Using separate workflows for control videos to manage VRAM constraints better
  - *From: MysteryShack*

- **MAGREF reference setup**
  - Use case: Use reference image instead of first image - subjects on white canvas, same resolution as output
  - *From: Kijai*

- **Video extension with last frames**
  - Use case: Take last 4 images, pad with blank/grey images to make 81 frames, encode to latent for another pass
  - *From: Gateway {Dreaming Computers}*

- **NAG native connection**
  - Use case: Model -> LoRA -> NAG -> NAG model out to ksampler, condition from neg into NAG
  - *From: Gateway {Dreaming Computers}*

- **Image morphing using VACE and LightX2V**
  - Use case: Great for animated logos and transitions between images
  - *From: David Snow*

- **Multi-stage automated video generation**
  - Use case: 5 scene automated generation with LLM-created dialogue, emotion-to-voice, sound effects using phantom + lip sync
  - *From: AJO*

- **Stable Video + VACE for lip sync improvement**
  - Use case: Use stable video for initial lip sync, then VACE to enhance lip detail and quality
  - *From: Mads Hagbarth Damsbo*

- **VACE + Phantom + self-forcing combination**
  - Use case: Character consistency with style control
  - *From: wowee*

- **Digital transitions between animated videos**
  - Use case: Creating transitions between two videos instead of static images using start/end frame
  - *From: David Snow*

- **MatAnyone for greenscreen replacement**
  - Use case: Background replacement without traditional greenscreen
  - *From: JohnDopamine*

- **Daisy chain start/end frame for long videos**
  - Use case: Creating longer sequences by using end frame as start frame for next run
  - *From: Purz*

- **2 sampler workflow with high shift values**
  - Use case: Better motion and quality with LightX2V at sigma_max 7.0 and shift 100
  - *From: Ada*

- **VACE + Phantom combo**
  - Use case: Character consistency, can use VACE references without phantom embeds
  - *From: DawnII*

- **Color matching for video extension**
  - Use case: Match each extended clip to initial frame to prevent progressive color burning
  - *From: MilesCorban*

- **Phantom + T2V merge for difficult prompts**
  - Use case: When standard T2V can't achieve desired results, mix small percentage of Phantom
  - *From: ▲*

- **Auto-extending video loop system**
  - Use case: Send last frame of video to new generation automatically, exports individual and final videos
  - *From: Nekodificador*

- **Two-stage generation with TAEW**
  - Use case: Stage 1 with 1 step for preview, Stage 2 with more steps if approved
  - *From: aipmaster*

- **Multitalk lip sync with uni3c for camera control**
  - Use case: Generate lip synced video with static camera by repeating init frame to video length
  - *From: Kijai*

- **MAGREF I2V with concatenated reference images**
  - Use case: Better character consistency by using multiple reference images as input
  - *From: DawnII*

- **VACE inpainting with SAM2 and points editor**
  - Use case: Character LoRA swapping and targeted item replacement in videos
  - *From: mdkb*

- **Two-pass VACE for better control**
  - Use case: Chain 2 VACE nodes - first with ref_img, second with control vid at 0.6 strength
  - *From: MilesCorban*

- **1.3B upscaling with MPS + HPS + Self Forcing LoRAs**
  - Use case: Improving quality of 1.3B model outputs
  - *From: yi*

- **VACE video extension with color correction**
  - Use case: Extending videos while minimizing color shift using DaVinci Resolve post-processing
  - *From: CaptHook*

- **Video outpainting with VACE**
  - Use case: Converting 16:9 videos to 9:16 by padding with gray (127,127,127 RGB) and using VACE inpainting
  - *From: MilesCorban*

- **MultiTalk with context windows for long audio**
  - Use case: Creating long talking videos with consistent camera
  - *From: Kijai*

- **Remote desktop setup for ComfyUI**
  - Use case: Running ComfyUI remotely to avoid heat in main workspace
  - *From: Juampab12*

- **Uni3c with repeat frames for camera consistency**
  - Use case: Reducing context window artifacts in long videos
  - *From: Juampab12*

- **Automated video generation with multiple LLMs**
  - Use case: 5 second loops that will jump to 10 second scenes for 50 seconds of automated movie with sound and dialogue
  - *From: AJO*

- **T2V + MultiTalk combination**
  - Use case: Using T2V models like Phantom with MultiTalk for audio-synced video generation
  - *From: DawnII*

- **Multi-angle video generation**
  - Use case: Generate video from several angles, then use audio-reactive setup to pull batches from each set and combine
  - *From: A.I.Warper*

- **Pure text-to-video with MultiTalk**
  - Use case: Generate lip-synced videos directly from text and audio without input images
  - *From: hicho*

- **Video-to-video with lower denoising**
  - Use case: Transfer motion from source video while changing appearance, use denoising 0.45 for better results
  - *From: hicho*

- **I2V merge with AniWan at 25%**
  - Use case: Combine different models for better lip-sync results, limited to 69 frames
  - *From: ZRNR*

- **ChatterBox + MultiTalk integration**
  - Use case: Generate custom voice audio and lip-sync in single workflow
  - *From: CJ*

- **Multi-angle MultiTalk using Flux Kontext**
  - Use case: Creating varied talking head videos
  - *From: burgstall*

- **NAG testing for color changes**
  - Use case: Testing model responses to targeted negative conditioning
  - *From: VRGameDevGirl84(RTX 5090)*

- **UltraWan upscaling workflow**
  - Use case: Getting more detail from 1.3B model in upscaling pipeline
  - *From: David Snow*

- **Spline Path Control for motion**
  - Use case: Precise motion control for any element in video
  - *From: Jonathan*

- **VACE style transfer morph using reference video**
  - Use case: Style transfer between start frame and last frame of reference video
  - *From: Dream Making*

- **I2V + Uni3C for camera-driven motion**
  - Use case: Using real camera movement video to drive synthetic video motion
  - *From: Nekodificador*

- **MultiTalk with black frame input for T2V speaking**
  - Use case: Generating speakers from scratch without needing face reference image
  - *From: burgstall*

- **Video-to-video with MultiTalk lip sync**
  - Use case: Take existing video and add lip sync while preserving visuals
  - *From: VRGameDevGirl84(RTX 5090)*

- **Second pass upscale with UltraWan + Self-Forcing**
  - Use case: Improve and upscale existing videos
  - *From: Alisson Pereira*

- **Character LoRA training with Flux Kontext/Runway**
  - Use case: Build image datasets from single source image for character consistency
  - *From: Jas*

- **Batch video processing with lip sync**
  - Use case: Create videos first, then add lip sync later in batches
  - *From: VRGameDevGirl84(RTX 5090)*

- **V2V upscaling with FusionX + LightX**
  - Use case: Upscaling old low resolution videos to higher quality
  - *From: VRGameDevGirl84(RTX 5090)*

- **MultiTalk with reduced controlnet strength**
  - Use case: Getting more natural movement in talking head videos
  - *From: Thom293*

- **VACE with original video as reference**
  - Use case: Using control_input and VACE encode for guided generation
  - *From: Dream Making*

- **Video to video upscaling**
  - Use case: Upscale low resolution videos to 1920x1080 using Wan FusionX with LightX, works for enhancing/upscaling
  - *From: VRGameDevGirl84(RTX 5090)*

- **Two-pass upscaling with UltraWan**
  - Use case: Using UltraWan as second pass for better upscaling results with VACE + Self Forcing DMD
  - *From: Alisson Pereira*

- **MultiTalk video to video lip sync**
  - Use case: Add mouth movements to existing video using audio input, similar to Runway's Act-1 but with audio instead of mocap
  - *From: VRGameDevGirl84(RTX 5090)*

- **Phantom character dataset creation**
  - Use case: Create full training dataset from single image using rotation prompts, then train LoRA
  - *From: Thom293*

- **Video continuation with depth control**
  - Use case: Split intro video into chunks, pass to control_video input through depth processing for seamless extension
  - *From: pom*

- **MultiTalk with VACE acting**
  - Use case: Use VACE to act out mouth movements silently, then apply audio later via video-to-video
  - *From: VRGameDevGirl84(RTX 5090)*

- **First frame Flux to VACE pipeline**
  - Use case: Take first frame, run through Flux with depth/normal maps, then use as VACE reference for consistent character in new scenes
  - *From: voxJT*

- **Phone video to stylized character**
  - Use case: Record video on phone, use first frame Flux, then VACE with normal maps to create consistent stylized character
  - *From: voxJT*

- **DaVinci masking to ComfyUI**
  - Use case: Do complex rotoscoping in DaVinci Resolve, export for use with VACE inpainting
  - *From: Nekodificador*

- **Multiple VACE embeds**
  - Use case: Use up to 5 separate VACE encodes for granular control over different aspects
  - *From: DawnII*

- **UltraWan upscaling workflow**
  - Use case: Upscale 14B videos to FHD using 1.3B model with UltraWan LoRA
  - *From: David Snow*

- **VACE with T2V LoRA for coloring**
  - Use case: Transform T2V LoRA into I2V functionality using VACE module with reference image
  - *From: Alisson Pereira*

- **4K upscaling with model upscale**
  - Use case: Generate at 1080p then upscale with 4xCaptureReality to 4K (actually 8K then downscale)
  - *From: HeadOfOliver*

- **Uni3C for camera control**
  - Use case: Simple I2V workflow with Uni3C embed and control video for unique camera/object movements
  - *From: AshmoTV*

- **FusionX upscaling workflow**
  - Use case: Video enhancement and creative upscaling - can use prompts for creative changes or no prompt for pure enhancement
  - *From: VRGameDevGirl84(RTX 5090)*

- **VACE with normal maps for lighting control**
  - Use case: Improving facial details and lighting while maintaining structure during video processing
  - *From: Tango Adorbo*

- **Long video processing with context windows**
  - Use case: Processing 400+ frame videos using 121 frame context windows with block swapping
  - *From: samhodge*

- **Endless travel using Flux Kontext for frame generation**
  - Use case: Creating dream sequence-like videos using Kontext-generated frames
  - *From: VRGameDevGirl84(RTX 5090)*

- **MultiTalk with VACE and extension**
  - Use case: Combining lip sync with style transfer and video extension
  - *From: Tango Adorbo*

- **Automated 81-frame segment processing**
  - Use case: Splitting longer videos into segments and processing each with different samplers
  - *From: Faust-SiN*

- **VACE reference image + pose controlnet using wrapper**
  - Use case: Controlled video generation with character reference and pose guidance
  - *From: David Snow*

- **Endless travel generation at 512x512 then upscale to 1080p**
  - Use case: Creating looping travel videos
  - *From: VRGameDevGirl84(RTX 5090)*

- **MiniMax remover 1.3B workflow from Benji Futurethinker**
  - Use case: Removing watermarks without installing additional nodes
  - *From: mdkb*

- **Endless latent space generation**
  - Use case: Remaining fully within latent space for continuous video generation by clipping last frames and concatenating with gray padding
  - *From: CJ*

- **VACE for post-edit video processing**
  - Use case: Targeting things to change or remove with SAM2, or full V2V restyling using controlnets to maintain video structure
  - *From: mdkb*

- **Wan as text-to-image generator**
  - Use case: Set frame count to 1, use save image instead of video combine for single image generation
  - *From: VRGameDevGirl84(RTX 5090)*

- **Context options node usage**
  - Use case: Instead of generating 200 frames at once, generate X frames at a time with Y frames overlap, then blend the output
  - *From: CJ*

- **Tile lora upscaler for adding detail**
  - Use case: True upscaling that adds fine detail rather than just refining edges, works with 1.3B model using noise injection
  - *From: David Snow*

- **Context overlap for longer videos**
  - Use case: Extending Wan generations beyond 5 seconds using context options on sampler in wrapper
  - *From: VK (5080 128gb)*

- **Pose transfer with align node**
  - Use case: Transfer pose from any reference video to any image regardless of scale/position/aspect ratio, combined with spline editor for camera control
  - *From: Jonathan*

- **UltraWan 1K upscaling pipeline**
  - Use case: Using UltraWan 1K going into self-forcing-DMD-VACE 1.3B with denoise 0.1 and LCM scheduler for consistency up to 720p
  - *From: mdkb*

- **V2V + MultiTalk combination**
  - Use case: Video-to-video with lip sync, works but very slow and requires context options for long videos
  - *From: N0NSens*

- **I2V with LightX ingredients workflow**
  - Use case: Fast image-to-video generation in ~100 seconds at 1280x720x81
  - *From: zoz*

- **FusionX ingredients with individual LoRA control**
  - Use case: Exposes individual LoRAs from FusionX for custom mixing and testing
  - *From: VRGameDevGirl84(RTX 5090)*

- **Two-pass video generation with talking**
  - Use case: First create video with sound, then use MultiTalk on second vid2vid pass
  - *From: VRGameDevGirl84*

- **VACE auto-compositing for 3D assets**
  - Use case: Using VACE/Wan for production-quality 3D asset compositing
  - *From: Neex*

- **Topaz two-step upscaling**
  - Use case: Gaia for upscaling, Iris for cleanup, then 16fps to 60fps interpolation
  - *From: blake37*


## Recommended Settings

- **AccVid + CausVid combination**: AccVid 1.5 strength, CausVid 0.5 strength, 3 steps
  - Better quality than 8 steps with CausVid alone
  - *From: Jonathan*

- **CausVid v2 with Phantom**: 1.0 strength, 4 steps, CFG 1
  - Works well with phantom for good results
  - *From: Jonathan*

- **Phantom generation**: 1024x1200x81x6 steps on 5090 takes ~550 seconds
  - Performance benchmark
  - *From: Thom293*

- **Sampler for video generation**: dpmpp_2m with sgm_uniform scheduler
  - Works exceptionally well for video, better than other samplers in frame-by-frame comparison
  - *From: Jonathan*

- **CausVid + MPS combination**: CausVid strength 1, MPS strength 1, 8 steps
  - Dramatic quality improvement
  - *From: VRGameDevGirl84*

- **Best low-step combo**: CausVid + AccVid + HLS at 3 steps
  - Improves prompt adherence, movement, and detail
  - *From: Jonathan*

- **MPS optimal strength**: 0.5 or lower
  - Higher values may stop following preprocessors
  - *From: DeZoomer*

- **MPS LoRA strength**: 1.0
  - Default recommended strength
  - *From: VRGameDevGirl84(RTX 5090)*

- **CausVid v2 steps**: 8-12
  - v2 is weaker and needs more steps than original
  - *From: MilesCorban*

- **MoviiGen LoRA strength**: 0.75
  - Provides significant prompt adherence improvement
  - *From: VRGameDevGirl84(RTX 5090)*

- **5090 frame capacity**: 161 frames at 720p
  - Maximum capacity for RTX 5090
  - *From: Piblarg*

- **Sampler/scheduler combo**: dpmpp_2m/sgm_uniform
  - Consistently gives better results in video workflows
  - *From: Jonathan*

- **Frame rate**: 16fps
  - Should match video combine settings
  - *From: Jonathan*

- **Resolution for 14B model**: Higher than 720x368
  - Current resolution is even lower than recommended for 1.3B
  - *From: Valle*

- **Enhance-A-Video guidance**: 4
  - 1 is not high enough for many frames
  - *From: DawnII*

- **VRAM management**: Full
  - Needed for fp16 on low VRAM cards like 2060
  - *From: Kijai*

- **CausVid v2 steps**: 10
  - Significant quality improvement over 5 steps, diminishing returns beyond 10
  - *From: MilesCorban*

- **MPS LoRA strength**: 0.3-0.4
  - Recommended range to avoid overriding other LoRAs
  - *From: David Snow*

- **HPS/MPS reward LoRA weights**: 0.7 for both
  - Alibaba's official recommendation for 14B models
  - *From: Johnjohn7855*

- **Block swapping beat**: 40
  - Helps avoid OOM when processing longer sequences
  - *From: AJO*

- **CausVid + AccVid + MPC combination**: CausVid 0.5, AccVid 1.5, MPC 1.0
  - 40% improvement over CausVid alone
  - *From: Jonathan*

- **CausVid + AccVid + MPC + MPS combination**: CausVid 0.5, AccVid 1.5, MPC 1.0, MPS 1.0
  - Additional 25% improvement
  - *From: Jonathan*

- **AccVid strength for maximum motion**: 2.0
  - 15% more improvement but sacrifices resemblance in I2V
  - *From: Jonathan*

- **Steps with LoRA combinations**: 3-10 steps
  - Can go as low as 3 steps with LoRA combinations
  - *From: Jonathan*

- **CausVid v2 optimal setup**: Strength 1.0, CFG 3, 8 steps
  - Best motion and resemblance balance
  - *From: hablaba*

- **CausVid v1 strength**: 0.5
  - Recommended for AccVid usage
  - *From: Jonathan*

- **AccVid strength**: 1.5
  - Works well with CausVid v1 0.5 strength
  - *From: Jonathan*

- **MPS strength**: 1.0
  - Standard setting for motion enhancement
  - *From: Jonathan*

- **CFG for CausVid v2**: 1
  - Can go as low as 3 steps with this CFG
  - *From: Jonathan*

- **VACE embed strength**: 70%
  - Reduces color washout and batch seam issues
  - *From: A.I.Warper*

- **Face resemblance combo**: CausVid 0.5, MPS 0.7, AccVid 1.5
  - Best balance for face resemblance retention
  - *From: Jonathan*

- **Uni3C frame count**: 49 frames
  - Required frame count for Uni3C workflow
  - *From: Valle*

- **Generation resolution for static scenes**: 1536x1024
  - High resolution helps I2V + controlnet for static scenes
  - *From: mamad8*

- **AccVid strength**: 1.5-2.0
  - Best balance of motion and resemblance retention
  - *From: Jonathan*

- **Fantasy Talker LoRA strength**: 0.7
  - Good default, can be adjusted based on prompt
  - *From: VRGameDevGirl84(RTX 5090)*

- **Steps for 2-step generation**: 2 steps
  - Can get insane quality at just 2 steps with AccVid
  - *From: Jonathan*

- **Frame count and resolution**: 81 frames at 1024x576 with 10 steps
  - Good performance balance - completed in ~137 seconds
  - *From: VRGameDevGirl84(RTX 5090)*

- **Sampler choice**: euler/beta on native
  - Better results than UniPC for certain use cases
  - *From: MilesCorban*

- **CausVid with Phantom strength**: Lower strength
  - Phantom becomes less flexible when combined with other additions
  - *From: Kijai*

- **SageAttention mode**: Specific mode instead of auto
  - Auto mode can cause issues, specific modes more reliable
  - *From: Kijai*

- **CFG Schedule start value**: 1.01
  - Starting at 1.0 causes 'list index out of range' error
  - *From: toyxyz*

- **VACE block swap**: 40/15
  - Used successfully with 4080 16GB + 64GB RAM at 1024x576 81 frames
  - *From: CaptHook*

- **AccVid strength for low steps**: 3.5-4.0
  - Huge increase in motion, only works on low steps
  - *From: Jonathan*

- **LoRA stack for fast generation**: CausVid v2: 1, AccVid: 1, MPS: 1, Moviigen: 1, 6 steps, unipc simple
  - 211s on 4060 8GB laptop
  - *From: Blitz*

- **Recommended LoRA strengths with GGUF**: CausVid v1: 0.5, MPS: 1.0, AccVid: 1.5-2.0
  - Good balance, AccVid can go up to 3.5 at low steps
  - *From: Jonathan*

- **Steps and shift for CausVid**: 8 steps with shift 5
  - Better results than other combinations
  - *From: Johnjohn7855*

- **I2V Riflex setting**: 12
  - Good balance for I2V generation
  - *From: toyxyz*

- **Causvid LoRA strength**: 0.75
  - Greatly increases motion when used with accvid at high strengths
  - *From: Jonathan*

- **AccVid strength**: 2.0
  - Works better for 2-3 step generation
  - *From: Jonathan*

- **Block swap**: 10
  - For 24GB VRAM systems to manage memory
  - *From: VRGameDevGirl84(RTX 5090)*

- **Steps**: 3
  - Works with accvid, saves time
  - *From: Jonathan*

- **Scheduler**: sgm_uniform
  - Better results than simple scheduler
  - *From: Jonathan*

- **Causvid strength in Native**: 3
  - Need to up the shift in native vs wrapper
  - *From: VRGameDevGirl84(RTX 5090)*

- **CFG**: 1
  - Works best with speed LoRAs like causvid and accvid
  - *From: Jonathan*

- **CausVid v1 strength**: 0.5
  - Good starting point
  - *From: Jonathan*

- **AccVid strength**: 1.0 then raise as needed
  - Start at 1.0 and increase until it looks too cooked
  - *From: Jonathan*

- **MPS strength**: 0.5-0.75
  - For maximum facial resemblance, 1.0 changes too much
  - *From: Jonathan*

- **Steps for speed LoRAs**: 3-6
  - Optimal range with dpm++ 2m/sgm_uniform sampler
  - *From: Jonathan*

- **AccVid with Phantom**: 0.9
  - Lowered from 1.5 to 0.9 for better ID preservation
  - *From: Johnjohn7855*

- **CausVid + AccVid I2V + MPS**: CausVid 0.5, AccVid I2V 2.0, MPS 1.0
  - Best mix for low steps according to testing
  - *From: Jonathan*

- **CFG scheduling**: 4,3,2,1,1,1,1,1,1,1
  - Great compromise that locks the face in
  - *From: AJO*

- **VACE strength for separated encodes**: >1.0
  - When separating first frame and control into different encodes, may need strength above 1
  - *From: hablaba*

- **Shift parameter**: 5 instead of 8
  - Helps with smoother transitions between frames
  - *From: 3Dmindscaper2000*

- **Shift**: 1-2 for VRGameDevGirl84's merge
  - Produces more cinematic results and avoids hair artifacts
  - *From: VRGameDevGirl84*

- **Steps**: 4 minimum for hair quality
  - 3 steps causes hair issues, 4+ steps allows proper hair rendering
  - *From: The Punisher*

- **Shift formula**: steps*0.5
  - Provides safe baseline shift value for consistent results
  - *From: The Punisher*

- **MPS LoRA strength**: 0.1
  - Higher values lose skin detail, needs to be balanced carefully
  - *From: The Punisher*

- **CFG with CausVid**: 1
  - Required for proper CausVid lora function
  - *From: Thom293*

- **CausVid steps**: 4-8 steps standard, some use 2
  - Optimal range for CausVid lora
  - *From: Thom293*

- **Base I2V settings**: CFG 4.5/6
  - Good starting point for image to video
  - *From: ingi // SYSTMS*

- **Phantom with CausVid**: 4-8 steps
  - Works fine for speed improvement
  - *From: zelgo_*

- **VACE depth control strength**: 0.9
  - Good starting strength for depth control
  - *From: ingi // SYSTMS*

- **Shift formula for even steps**: steps * 0.5 - 0.25
  - Works well for even step counts (4,6,8) to get good detail
  - *From: The Punisher*

- **VACE blend factor**: 0.9 or lower
  - Prevents pose control from showing through in render
  - *From: CaptHook*

- **1080x720 fp16 generation time**: 271.40 seconds
  - Performance benchmark result
  - *From: VRGameDevGirl84(RTX 5090)*

- **125 frames with GGUF Q6_K**: 242-253 seconds
  - Performance with sage2 and fp16 accumulation on 5090
  - *From: blake37*

- **Phantom recommended settings**: Steps 8, CFG 1, Shift 5, Scheduler UniPC
  - Optimal settings for Phantom merge model
  - *From: VRGameDevGirl84(RTX 5090)*

- **Shift for 3 steps**: 9.25
  - Minimum shift that works without glitching for 3 steps
  - *From: The Punisher*

- **AccVid minimum strength**: 1.75
  - Required minimum for good results with certain settings
  - *From: The Punisher*

- **Diffusers version**: 0.33 or higher
  - Required for uni3c model compatibility
  - *From: Kijai*

- **CausVid V2 strength**: 2.0
  - V2 requires much higher settings than V1.5
  - *From: David Snow*

- **CausVid V1.5 strength**: 0.4-0.5
  - Works like original causvid lora
  - *From: David Snow*

- **AccVid strength with CausVid**: 2-3
  - Recommended to combine with CausVid V2
  - *From: David Snow*

- **MPS LoRA strength**: 0.4-0.7
  - Optimal range for motion enhancement
  - *From: David Snow*

- **TeaCache L1 threshold for I2V 480p**: 0.26
  - Good balance for caching efficiency
  - *From: Danial*

- **TeaCache start percent**: 0.30 (or 0.20 for faster)
  - 0.20 cuts true steps by 50% but maintains quality
  - *From: the_darkwatarus_museum*

- **ATI strength with CausVid V1.5**: 0.4 or 0.5 for causvid + 1.5 for accvid
  - Good balance for motion control
  - *From: Johnjohn7855*

- **Model precision**: fp32 for transformer, fp32 for T5, fp16 for VAE
  - Significantly improves quality especially at 720p
  - *From: Juan Gea*

- **Causvid strength**: 0.35
  - Lower values require higher samples but provide more control, reduces VACE control strength
  - *From: Guey.KhalaMari*

- **Sampler for Causvid**: dpmpp_2m with sgm_uniform or UniPC with simple 10 steps
  - Better convergence than euler at low step counts
  - *From: CJ*

- **Steps without Causvid**: 25-50 steps
  - For best quality when fine detail and movement artifacts need to be minimized
  - *From: Thom293*

- **DPM++_SDE sampler**: 10 steps, CFG 1, Shift 2
  - Reduces noise and screendoor effects for I2V
  - *From: Juan Gea*

- **Self-forcing LCM sampler**: 6 steps, CFG 1.0
  - Optimal settings for self-forcing model performance
  - *From: Kijai*

- **FP32 settings**: Set VAE/T5/Model to FP32 but compile model
  - Improves quality while preventing RAM issues
  - *From: Juan Gea*

- **DPM++_SDE steps**: Twice the amount compared to other samplers
  - DPM++_SDE is much slower so needs more steps for fair comparison
  - *From: Kijai*

- **Self-Forcing basic settings**: LCM/SGM uniform scheduler, CFG 1, 4-6 steps (6-8 recommended)
  - Optimal settings for Self-Forcing model performance
  - *From: Jonathan*

- **AccVid strength for motion**: 1.5-2.0
  - Higher AccVid strength increases motion, counters CausVid motion reduction
  - *From: Jonathan*

- **CausVid v1 strength**: 0.5-0.6
  - If using CausVid v1, keep at moderate strength to avoid killing motion
  - *From: Jonathan*

- **CausVid v2 strength**: 1.25
  - If must use CausVid v2, use higher strength than v1
  - *From: Jonathan*

- **MPS LoRA strength**: 1.0 for T2V, 0.5-0.75 for I2V
  - 1.0 for motion/detail, lower for I2V to preserve facial resemblance
  - *From: Jonathan*

- **CausVid with Self-Forcing**: 0.05-0.1
  - Very low strength needed as Self-Forcing already incorporates CausVid-like features
  - *From: Kaïros*

- **CFG for MPS LoRA**: 1
  - Lower CFG recommended when using MPS LoRA
  - *From: Jonathan*

- **GPU power limit**: 80%
  - Maintains performance while significantly reducing temperature
  - *From: Gavmakes*

- **Memory overclock with power limit**: +1200 MHz memory with 60% power limit
  - Returns to original 100% power limit performance
  - *From: Gavmakes*

- **CFG for self-forcing**: CFG 1.5
  - Works well with merged models in 6 steps
  - *From: hicho*

- **Denoiser strength for motion**: 0.5-0.7
  - Gets motion from latent noise in vid2vid scenarios
  - *From: hicho*

- **VACE encoder strength**: Balance needed
  - Lower strength (better prompt control, less camera following) vs higher strength (better camera movement, locked lighting)
  - *From: Ruairi Robinson*

- **Character lora strength**: 1.0 for lora, 0.3 for CausVid
  - Perfect face results but may need more steps for fine details with fp8 models
  - *From: Janosch Simon*

- **AniWan merge percentage**: 25%
  - Higher percentages deform eyes
  - *From: ZRNR*

- **Self-forcing model steps**: 8 steps optimal, 3-5 minimum
  - 8 is best quality, works as low as 3-5 for speed
  - *From: patientx*

- **CausVid + AccVid with ATI**: 12 steps
  - Required even with CausVid and AccVid for ATI workflows
  - *From: Juampab12*

- **CFG for VACE workflows**: cfg 1
  - Works fine with empty negative prompt, decent rendering time
  - *From: JmySff*

- **VACE block swap**: 40 + 5 blocks
  - Necessary for multiple VACE embeds to avoid OOM
  - *From: A.I.Warper*

- **GGUF Q8 Wan + VACE render time**: ~2min15 for 1024x576, 8 steps, 81frames
  - Reasonable render time on RTX4090
  - *From: JmySff*

- **Block swap for VACE**: 15
  - Prevents OOM issues on 4090
  - *From: Juampab12*

- **Causvid strength for color shift**: 0.5-0.7
  - Helps reduce color shift issues in extensions
  - *From: Simonj*

- **CFG without causvid**: 2-4.5
  - When not using causvid loras, increase CFG from 1
  - *From: chrisd0073*

- **Steps without causvid**: 5-10
  - Higher step count when not using causvid acceleration
  - *From: chrisd0073*

- **Causvid with 6 steps**: 1.5
  - David Snow's setup for fast high-quality generation
  - *From: David Snow*

- **CausVid power**: 1
  - For T2V generation
  - *From: DiXiao*

- **Phantom + T2V merge ratio**: 0.15 to 0.25
  - Better LoRA compatibility, higher ratios lose 'phantomity'
  - *From: ▲*

- **Steps with TeaCache and CausVid**: Disable TeaCache
  - Low steps with TeaCache doesn't provide meaningful improvement
  - *From: Kijai*

- **Self-forcing model parameters**: lcm/simple, 1 cfg, 2 shift, 4-8 steps
  - Best results found after 500 tests, higher steps cause oversaturation
  - *From: Jonathan*

- **Block swapping**: 20 default, raise if OOMing
  - Can go up to 39-40 for main model, 15 for VACE if needed
  - *From: JohnDopamine*

- **Torch compiler weight dtype**: fp8_e5m2
  - Only works with this setting on older compute capabilities, use fp16 model and let node quantize
  - *From: HeadOfOliver*

- **HPS lora with MPS**: MPS 0.2 to 1, use HPS lora for images
  - Helps with quality, especially for single frame generation
  - *From: yi*

- **Generation steps for short videos**: 13+ steps for anything under 13 frames
  - Need more steps for single frame/short generations
  - *From: ▲*

- **VACE with fusion lora**: 4 steps, CFG 1
  - Faster and better than original i2v
  - *From: hicho*

- **Context frames for extension**: 34 input frames
  - Better quality maintenance in extended generations
  - *From: Colin*

- **ClipVision strength adjustment**: Reduce strength_1 to 0.8, latent strength 0.8-1
  - Helps with first/last frame workflow
  - *From: Guey.KhalaMari*

- **MPS strength for i2v**: 0.5 or lower
  - Higher values negatively affect facial resemblance
  - *From: VRGameDevGirl84*

- **Skip layer guidance denoise**: 0.1
  - Good balance for cleanup work
  - *From: chrisd0073*

- **HPS strength with NAG**: 0.4
  - Works well with FusionX for CFG-like results
  - *From: Ada*

- **Shift value for weak noise**: 1
  - Makes noise really weak
  - *From: Kijai*

- **Native resolution for 3060 RTX**: 832x480, 81 frames
  - Avoids OOM issues while maintaining good results
  - *From: mdkb*

- **Self-forcing steps**: 4 steps
  - Meant to be used with 4 steps according to commit
  - *From: yi*

- **Self-forcing scheduler**: lcm + normal
  - Self forcing kind of requires it
  - *From: yi*

- **LightX2V LoRA strength**: Full strength, all layers
  - Trained for normal sampling, don't need to play with strength
  - *From: Kijai*

- **Shift value for lightX2V**: 8
  - Working setting mentioned
  - *From: Ada*

- **Context shifting with fusion_X**: Tweaked settings needed
  - User experiencing bad context shifting, asking for better settings
  - *From: Gavmakes*

- **LightX2V LoRA strength**: 1.0
  - Recommended strength for optimal results with the new speed LoRA
  - *From: David Snow*

- **LightX2V steps**: 4
  - LoRA is specifically trained for 4 steps, higher values cause overcooking
  - *From: Kijai*

- **LightX2V CFG**: 1.0
  - Standard CFG setting for the distilled LoRA
  - *From: Kijai*

- **CausVid v1.5 strength**: 0.5 (0.2 with merges)
  - Lower strength needed compared to v2 for optimal sharpness without artifacts
  - *From: David Snow*

- **Best ATI settings**: DPM++SDE beta, shift 8.5, steps 5
  - Optimal settings found for ATI video generation
  - *From: Juampab12*

- **CausVid at low weight with LightX2V**: 0.3
  - Helps clear blurriness without much effect on generation quality
  - *From: Ada*

- **CFG**: 1.0
  - Required for distill LoRAs
  - *From: David Snow*

- **Steps**: 4
  - Starting point for self-force acceleration
  - *From: Kijai*

- **lightx2v LoRA strength**: 0.5
  - Testing value for motion preservation
  - *From: Gateway {Dreaming Computers}*

- **VACE grey color**: 127,127,127 RGB (0.5)
  - Specific grey value that works for VACE
  - *From: Kijai*

- **Sampler**: LCM or DPM++/SDE
  - Good samplers for wrapper with acceleration LoRAs
  - *From: Kijai*

- **CFG**: 1.0
  - Should be set to 1.0 when using Phantom model
  - *From: David Snow*

- **Steps**: 4
  - 4 steps with LightX2V are sufficient for most cases instead of 8
  - *From: Fawks*

- **Points to sample**: Same as number of steps
  - When using spline editor float output for CFG scheduling
  - *From: jellybean5361*

- **Inference stop**: 65%
  - For color image embeddings to not be too influential
  - *From: Mads Hagbarth Damsbo*

- **Self forcing + HPS + MPS**: 1.25 + 0.2 + 0.7 with 4 steps
  - Better than complex LoRA combinations
  - *From: yi*

- **LightX2V + MPS + AccVid + DetailZ**: 0.5 + 0.7 + 0.5 + 0.1 with 8 steps UniPC
  - Much better motion than CausVid
  - *From: Daviejg*

- **Shift value for motion control**: 5-8 range
  - 8 gives more motion, 5 gives less motion
  - *From: yi*

- **CFG with LightX2V**: 1.0
  - Must be 1 for speed benefit, higher CFG loses speed and may burn
  - *From: DawnII*

- **SLG start with wrapper denoise**: 0
  - ComfyUI handles denoise differently than diffusers
  - *From: Kijai*

- **LightX2V shift**: 100 with sigma_max 7.0
  - Massive difference in motion and quality
  - *From: Ada*

- **Context window overlap**: More overlap
  - May help with cross fade issues
  - *From: Kijai*

- **VACE mask gray**: RGB 123,123,123
  - Exact value required for proper inpainting
  - *From: ingi // SYSTMS*

- **CFG with SLG and LightX2V**: Limited CFG range, lower LoRA strength
  - SLG is CFG boosting, LightX2V is CFG distilled
  - *From: Kijai*

- **LightX2V**: cfg 3, steps 3, LCM sampler
  - Works well for fast generation
  - *From: Gateway {Dreaming Computers}*

- **Context window overlap**: 48 overlap works well, 64 is overkill
  - Balance between quality and generation time
  - *From: Kijai*

- **VACE mask color**: #a2ad9c or 50% grey (127,127,127 RGB)
  - Proper mask recognition
  - *From: Kijai*

- **MultiTalk memory usage**: +9GB in bf16, half that in fp8
  - VRAM requirements on top of base model
  - *From: Kijai*

- **dpm_2_ancestral sampler**: with beta scheduler
  - Produces exceptional quality results
  - *From: David Snow*

- **Multitalk FPS**: 25fps
  - Default recommended setting, was hardcoded in original
  - *From: Kijai*

- **NAG alpha for Phantom**: 0.1
  - Better results than default settings
  - *From: DawnII*

- **Empty frames best**: 0.5
  - Optimal setting for VACE workflows
  - *From: DawnII*

- **Audio scale for multitalk**: Below 1.0 (as low as 0.3)
  - Reduces overly expressive lip sync
  - *From: CJ*

- **Multitalk context overlap**: 16 overlap
  - Works well with stationary camera setup
  - *From: Kijai*

- **MultiTalk context frames**: Make divisible by 80 then +1
  - Optimal performance with context windows
  - *From: Kijai*

- **lightx2v sampler**: LCM with ddim_uniform scheduler
  - Avoids killing camera motion and seed variation
  - *From: Screeb*

- **1.3B upscale parameters**: 8 steps, CFG 2.5, denoise 0.1
  - For clean up and blemish removal
  - *From: mdkb*

- **VACE extension denoise**: 0.4-0.6
  - Reduces color shift and oversharpen issues
  - *From: CaptHook*

- **lightx2v steps and CFG**: 5 steps, no CFG (CFG=1)
  - Works with distillation training
  - *From: Kijai*

- **lightx2v strength for MultiTalk**: 1.2-1.5
  - Increased motion for talking videos, 1.8 too much
  - *From: Juampab12*

- **uni3c overlap**: 32
  - Sufficient for locked camera with uni3c
  - *From: Kijai*

- **block swap blocks**: 40 for 3090, 25 for 24GB VRAM
  - Prevents OOM while maintaining performance
  - *From: burgstall*

- **context window frames**: 81
  - Match model training chunk size
  - *From: Juampab12*

- **audio sample rate**: 44.1kHz
  - Prevents timing issues in ComfyUI
  - *From: burgstall*

- **MultiTalk frame count**: Must be divisible by (n-1)/4
  - Mathematical requirement for proper processing
  - *From: A.I.Warper*

- **Context overlap for MultiTalk**: 81,4,32
  - Original workflow settings still being used
  - *From: A.I.Warper*

- **VRAM usage for MultiTalk**: Actual inference 12-13GB, but loading models can use full 24GB
  - Need to account for model loading overhead
  - *From: Purz*

- **Block swap configuration**: 10 block swaps for 549 frames
  - Working configuration for extended video generation
  - *From: A.I.Warper*

- **Frame count for T2V**: Maximum 81 frames
  - Higher counts cause flash and instability
  - *From: Ruairi Robinson*

- **VRAM usage for 1000 frames**: 21GB VRAM
  - Actual measurement during generation
  - *From: A.I.Warper*

- **UltraWan LoRA strength**: 0.25
  - Recommended strength from model documentation
  - *From: Alisson Pereira*

- **Steps for MultiTalk**: 2 steps with CausVid model
  - Fast generation while maintaining quality
  - *From: hicho*

- **Context length for lipsync**: 41 context, 69 frames max
  - Longer durations break lipsync consistency
  - *From: ZRNR*

- **NAG alpha/scale**: Lowered from initial values
  - After testing with blonde hair changes, reduced strength for more controlled effects
  - *From: VRGameDevGirl84(RTX 5090)*

- **Fun InP MPS steps**: 3 steps
  - 4 steps produces buggy/noisy results
  - *From: Alisson Pereira*

- **CausVid strength for T2V 1.3B**: 0.5
  - Higher values produce buggy results
  - *From: Alisson Pereira*

- **UltraWan 1k LoRA steps**: 6 steps at 1600x688
  - Works well for upscaling workflow
  - *From: David Snow*

- **MultiTalk minimum frames**: 25 frames
  - To match MultiTalk training, though 9 frames possible but janky
  - *From: Guey.KhalaMari*

- **Block swap for MagRef OOM**: Up to 40
  - Helps with VRAM management when using MagRef
  - *From: Guey.KhalaMari*

- **Audio CFG for MultiTalk**: 3-5 optimal, up to 6 for better sync
  - Controls lip synchronization accuracy, higher values improve sync but increase generation time
  - *From: ˗ˏˋ⚡ˎˊ-*

- **MultiTalk frame count**: 81 frames at 25 FPS optimal
  - Model was trained on 81-frame videos, longer clips may reduce prompt-following performance
  - *From: ˗ˏˋ⚡ˎˊ-*

- **TeaCache threshold**: 0.2 to 0.5 range
  - Optimal acceleration range, higher values increase speed but may reduce quality
  - *From: ˗ˏˋ⚡ˎˊ-*

- **LightX2V strength**: 1.67
  - Used with 44.1khz audio for optimal MultiTalk results
  - *From: burgstall*

- **Self-forcing LoRA strength**: 0.25
  - Prevents buggy video output
  - *From: Alisson Pereira*

- **Video-to-video denoise**: 0.7
  - Good balance for transformation
  - *From: VRGameDevGirl84(RTX 5090)*

- **Audio CFG for MultiTalk**: 1-2
  - Higher values don't slow generation
  - *From: patientx*

- **Character LoRA training images**: 12-16 images
  - Better than 30+ to avoid overtraining
  - *From: Jas*

- **AccVid LoRA strength**: 1.5
  - Used with CausVid 0.5 and MPS/HPS 1.0
  - *From: Faux*

- **Video framerate for lip sync**: 48fps
  - Better than 30fps, 60fps not necessary
  - *From: patientx*

- **block_swap**: 25-40
  - Optimal for 24GB VRAM to avoid slow generation
  - *From: Juampab12*

- **denoise for upscaling**: 0.7-0.8
  - Good balance for removing pixelation while maintaining structure
  - *From: VRGameDevGirl84(RTX 5090)*

- **MultiTalk controlnet strength**: 40%
  - Better movement than 100%, avoids over-restriction
  - *From: Thom293*

- **steps with LightX**: 12
  - Allows CFG >1 and improves quality without being 'fried'
  - *From: Piblarg*

- **scheduler**: euler simple or unipc
  - Both work fine, euler is preferred by community
  - *From: Piblarg*

- **MultiTalk audio gain**: 2-3 (vs default 1)
  - Significantly improves lip sync quality, picks up quieter sounds
  - *From: Thom293*

- **LightX2V strength for hand movements**: 2.0
  - Restores hand movements that get lost at lower strengths
  - *From: burgstall*

- **Video to video denoise**: 0.5-0.6
  - Good balance between staying close to input and enhancing quality
  - *From: VRGameDevGirl84(RTX 5090)*

- **MultiTalk 720p settings**: 5 steps, 4 shift, audio scale 1.5-2, cfg 2
  - Recommended settings for 720p model
  - *From: Guey.KhalaMari*

- **UltraWan with CausVid**: 0.25 strength
  - At strength 1.0, CausVid leaves very strong colors that bugs everything
  - *From: Alisson Pereira*

- **Context options**: 121
  - Successfully processed long videos without VRAM issues
  - *From: VRGameDevGirl84(RTX 5090)*

- **Block swap**: 40
  - Used with context options for efficient long video processing
  - *From: VRGameDevGirl84(RTX 5090)*

- **Denoise for face preservation**: 0.1-0.2
  - Higher values will lose faces in upscaling
  - *From: N0NSens*

- **Denoise for enhancement**: 0.75 max
  - 0.8 makes video totally different/random without prompt
  - *From: VRGameDevGirl84(RTX 5090)*

- **Steps for distill models**: 5 (shows as 4)
  - Console displays one step less than set
  - *From: VRGameDevGirl84(RTX 5090)*

- **MultiTalk chunk overlap**: 16-20
  - Reduces seams compared to 10 overlap
  - *From: pom*

- **Uni3C frame limit**: 81 frames maximum
  - Doesn't work above this limit even with context window off
  - *From: burgstall*

- **Start/end percent for Uni3C**: 0.0 to 0.1
  - Proper range for Uni3C operation
  - *From: burgstall*

- **Context window for long videos**: 41 frame context with 21 overlap
  - Better results than 16 overlap for reducing seams
  - *From: A.I.Warper*

- **Denoise for upscaling**: 0.1-0.2
  - Maintains character consistency while polishing
  - *From: mdkb*

- **Denoise for style changes**: 0.5-0.7
  - 0.5 keeps original well, 0.8+ creates new video
  - *From: VRGameDevGirl84*

- **Skip layer guidance layers**: 8 for 1.3B, 9 for 14B
  - Optimal layer skipping for different model sizes
  - *From: chrisd0073*

- **UltraWan upscaling denoise**: 0.15
  - Nothing gets changed at this low denoise level
  - *From: patientx*

- **Image saturation node**: 0.85 to 0.90
  - Fixes color consistency and WAN flash issues
  - *From: Bleedy (Madham)*

- **4K upscaling denoise**: 0.65-0.75
  - 0.65 for basic upscaling, 0.75 would look better
  - *From: VRGameDevGirl84(RTX 5090)*

- **UltraWan LoRA strength**: 0.2
  - V1 is very strong LoRA so lower strength needed
  - *From: Monster*

- **Denoise level for upscaling**: 0.3-0.5 for maintaining input, 0.77-0.8+ for creative changes
  - Lower values preserve original characteristics, higher values allow more creative freedom
  - *From: VRGameDevGirl84(RTX 5090)*

- **Context window size**: 121 frames
  - Optimal balance for processing longer sequences
  - *From: VRGameDevGirl84(RTX 5090)*

- **Block swap configuration**: 10-11 blocks enabled
  - Reduces VRAM usage significantly for long sequences
  - *From: samhodge*

- **VACE normal map strength**: 0.7
  - Higher values cause blue artifacts to come through
  - *From: VRGameDevGirl84(RTX 5090)*

- **LightX2V steps**: 4
  - Replace CausVid with LightX and drop steps to 4
  - *From: VRGameDevGirl84(RTX 5090)*

- **LightX2V strength**: 1.00
  - Strength should be 1.00 for lightX lora
  - *From: VRGameDevGirl84(RTX 5090)*

- **Shift for realism**: 1
  - For text to video realism, shift should be at 1. Higher values look less real
  - *From: VRGameDevGirl84(RTX 5090)*

- **Context overlap for long videos**: 64
  - Prevents extra loops in videos 321+ frames
  - *From: Bleedy (Madham)*

- **Block swap for upscaling**: 40
  - Allows processing any amount of frames without OOM
  - *From: VRGameDevGirl84(RTX 5090)*

- **Context overlap**: Higher values
  - More consistency but less variation opportunity
  - *From: DawnII*

- **LightX LoRA strength**: 1.0
  - Optimal balance, reduce from 1.2 if overexposed
  - *From: Valle*

- **Steps with LightX**: 4 steps
  - Optimal for speed, down from 6-10 steps
  - *From: VRGameDevGirl84(RTX 5090)*

- **Denoise for T2V**: 1.0
  - When converting V2V workflow to T2V
  - *From: David Snow*

- **Resolution divisible by**: 16
  - Prevents tensor dimension errors at higher resolutions
  - *From: VRGameDevGirl84(RTX 5090)*

- **Denoise for reference image usage**: 0.79 and under to use ref image, 0.80+ ignores ref image
  - Controls whether reference image is actually used or ignored
  - *From: VRGameDevGirl84(RTX 5090)*

- **MPS/Moviigen for T2I quality**: 1.00
  - Helps with quality when doing text to image generation
  - *From: VRGameDevGirl84(RTX 5090)*

- **Tile upscale denoise**: 0.3 for demonstration, can go much stronger
  - Controls strength of detail enhancement
  - *From: David Snow*

- **Video resolution requirement**: Must be divisible by 16
  - Wan general requirement for proper processing
  - *From: ingi // SYSTMS*

- **Steps for LightX2V T2V**: 6 steps
  - Recommended by experienced user
  - *From: David Snow*

- **CFG with CausVid and self-forcing DMD**: 1.0
  - CFG has to be 1.0 when using CausVid and self-forcing DMD lora
  - *From: David Snow*

- **UltraWan 1K denoise with self-forcing**: 0.1
  - Works well for upscaling 832x480 to 720p with self-forcing model
  - *From: mdkb*

- **Multiple LoRA strengths for 1.3B**: SF DMD FP16 at 0.25, CausVid bidirect2 at 1.0, MPS at 0.25, UltraWan 1K at 0.25
  - Optimal combination for best results
  - *From: phazei*

- **Tile upscaler resolution jump**: 1280x544 to 1920x832
  - Achievable resolution increase with good results using 1.3B model
  - *From: David Snow*

- **Self forcing LoRA strength**: 0.7
  - Good results for I2V with motion and no color shift
  - *From: zoz*

- **FusionX LoRA strength**: 0.5
  - Good results for I2V with motion and no color shift
  - *From: zoz*

- **LightX2V LoRA strength**: 0.8
  - Recommended strength for better results
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Context frames for long videos**: 121
  - Used for 497 frame (19 second) video generation
  - *From: VRGameDevGirl84(RTX 5090)*

- **Steps for speed workflows**: 4 steps
  - Fast generation with DPMM++SDE scheduler
  - *From: zoz*

- **DPM++ SDE Beta sampler**: 4 steps
  - Good results for I2V generation
  - *From: zoz*

- **Topaz upscale**: 4x upscale with Iris model
  - Good quality results
  - *From: zoz*

- **Topaz interpolation**: 60fps with Chronus
  - Smooth motion results
  - *From: zoz*


## Concepts Explained

- **Block 0 disabling**: CausVid v1.5 is CausVid with Block 0 disabled to fix first frame glitching artifacts
  - *From: JohnDopamine*

- **MoE architecture difference**: v2 has additional blocks disabled beyond just block 0, but may reduce quality especially for stylized outputs
  - *From: JohnDopamine*

- **Non-causal attention in video models**: Video models use non-causal attention, so generating shorter sequences changes output drastically
  - *From: aikitoria*

- **MPS vs HPS reward LoRAs**: MPS improves prompt adherence, HPS improves visuals. No trigger words needed.
  - *From: JmySff*

- **Reward LoRAs function**: Work like detailers to improve quality and prompt adherence, similar to Higgsfield concept
  - *From: Nekodificador*

- **MPS vs HPS LoRAs**: MPS LoRAs improve prompt adherence, HPS LoRAs improve visuals
  - *From: Bleedy (Madham)*

- **CausVid training method**: Trained for autoregressive causal sampling, which impacts motion when used with normal sampling
  - *From: MilesCorban*

- **Detail Transfer node**: Node originally made for IC Light to add detail back to normal maps, now useful for facial detail transfer
  - *From: A.I.Warper*

- **Moviigen**: A Wan fine-tune trained on shots from movies, available as both model and LoRA version
  - *From: Ruairi Robinson*

- **ATI trajectory points**: Coordinate system that needs 121 points for 81 frames due to 24fps to 16fps conversion
  - *From: Kijai*

- **VACE keyframe interpolation**: Using gray frames as placeholders that Wan can interpolate between, with black masks on inserted frames
  - *From: Nekodificador*

- **Control points mode**: Feature in trajectory editor allowing manual spacing of points for more precise control
  - *From: Kijai*

- **On-the-fly model merging**: Using ModelMergeSimple node to merge models temporarily without saving permanent files, allowing dynamic testing
  - *From: ▲*

- **Trajectory editing**: System for defining motion paths in video generation using JSON format with x,y coordinates over time
  - *From: Juampab12*

- **ATI (Alibaba Trajectory Interface)**: Motion guidance system using trajectory points to control object/camera movement in video generation
  - *From: Juampab12*

- **MPC and HPS LoRAs**: Reward LoRAs that improve prompt adherence and motion, part of Fun-Reward-LoRAs collection
  - *From: Jonathan*

- **Temperature and top_k in ATI**: Parameters controlling randomness and token selection in trajectory following
  - *From: Kijai*

- **Clean plate**: In VFX, removing talent and rolling frames to get background-only footage for compositing
  - *From: samhodge*

- **CausVid v1.5**: Version with first block removed, that's the only difference from original
  - *From: Kijai*

- **CausVid v2**: Further tuned version without first block, weaker allowing more steps and CFG, trading speed for quality
  - *From: Kijai*

- **SVDQuant**: Quantization technique with int4 (works on 20xx GPUs) and fp4 (needs 50xx GPUs) variants
  - *From: YatharthSharma*

- **FlowMo**: Motion optimization technique that uses gradients and inner optimization loop through WanModel
  - *From: A.I.Warper*

- **SPDA**: Alternative attention mechanism, can be confused with SageAttention in workflow dropdowns
  - *From: samhodge*

- **Batched CFG**: CFG option that should be ignored for models besides 1.3B due to VRAM usage
  - *From: Kijai*

- **Block swap**: VACE feature that offloads models to reduce VRAM usage
  - *From: Kijai*

- **Riflex**: Setting for I2V generation, controls some aspect of the generation process
  - *From: Juan Gea*

- **ATI model**: Special variant of Wan model designed for trajectory control, different from regular Wan model
  - *From: Juampab12*

- **DCM distillation**: New distillation method for accelerating video generation models
  - *From: yi*

- **Q8 GGUF quantization**: Q8_0 quantization provides quality roughly equivalent to fp16 but at half the file size, much better than fp8
  - *From: The Punisher*

- **Guide images in CSBW nodes**: Input image can heavily steer composition and colors, great for breaking away from ordinary compositions while still performing your prompt
  - *From: TK_999*

- **Context splitting**: Method to handle longer sequences by splitting input, not yet implemented in current version
  - *From: Kijai*

- **VACE embed separation**: Splitting reference images from control frames into separate encodes to control their strengths independently
  - *From: A.I.Warper*

- **CFG scheduling**: Using different CFG values at different steps, e.g. starting high and reducing over time
  - *From: AJO*

- **Shift**: Adjusts the noise removal curve in later sampling steps. Higher shift = more noise in later steps (more detail or messiness), lower shift = less noise (softer/blander results)
  - *From: TK_999*

- **SLG**: Enhance guidance towards detailed structure by having another set of CFG negative with skipped layers - acts as a speedup when using CFG
  - *From: TK_999*

- **Block swap**: Manual memory management feature in wrapper - choose number of blocks to control VRAM usage
  - *From: David Snow*

- **Tensor format [batch, channels, frames, height, width]**: How ComfyUI displays tensor dimensions for debugging
  - *From: Kijai*

- **Shift parameter**: Controls generation quality but can cause artifacts if set incorrectly, needs to scale with step count
  - *From: The Punisher*

- **Trajectory resizing**: Need to use resize_trajectories.py script when changing image dimensions to maintain point motion paths
  - *From: Juampab12*

- **Timeline feature in ATI editor**: Allows scheduling different point movements at different times with start/stop points
  - *From: Juampab12*

- **Diffusion Forcing (DF)**: Takes end frames from video and uses as input context to extend videos, overlaps frames during generation
  - *From: Colin*

- **Shift parameter sensitivity**: Odd step counts require much higher shift values than even steps, possibly due to scheduler behavior
  - *From: The Punisher*

- **Fun InP**: First-Frame-Last-Frame morphing and video extension system, includes 1.3B I2V model from Alibaba
  - *From: hicho*

- **Diffusion forcing**: Extension technique for WanVideo, has specific sampler and example workflows available
  - *From: samhodge*

- **Static points in ATI**: Key placement points that determine motion trajectories in ATI, most important aspect for getting desired motion
  - *From: Johnjohn7855*

- **Block swap in wrapper**: Manual VRAM management technique needed in wrapper, while native does automatic offloading
  - *From: Kijai*

- **VACE strength in wrapper vs native**: In wrapper acts like blend/merge factor, in native acts like reference weight
  - *From: the_darkwatarus_museum*

- **Self-forcing**: Autoregressive video generation method that generates frames in order rather than denoising entire clip over time
  - *From: multiple users*

- **Screen door effect**: Artifacts appearing as small dark dots in areas of high-frequency detail like foliage or hair
  - *From: Nathan Shipley*

- **Skip Layer Guidance**: Technique that can be used as second pass to improve video quality and fix artifacts
  - *From: chrisd0073*

- **Self-Forcing**: Autoregressive diffusion model that generates video frames sequentially, each frame depending on the previous one, different from standard parallel generation
  - *From: MysteryShack*

- **VACE I2V conversion**: VACE can convert any T2V model into I2V functionality by using reference images
  - *From: N0NSens*

- **Attention quadratic scaling**: Video attention grows quadratically with length, so limiting attention scope reduces VRAM usage significantly for longer videos
  - *From: Piblarg*

- **Self-forcing**: New method to drastically improve generation speed, requires autoregressive sampling with kv_cache which isn't supported in ComfyUI yet
  - *From: Kijai*

- **VACE tensor size matching**: When using VACE with Phantom, need to add 4 images to VACE conditioning for every Phantom image to match tensor dimensions
  - *From: Piblarg*

- **Vid2vid with T2V models**: Using T2V models for video-to-video by encoding input as latent with lower denoiser values
  - *From: Kijai*

- **DCM lora extraction**: The semantics part of Wan training can be extracted as LoRA layers and used separately from the main detail model
  - *From: Kijai*

- **Static points in ATI**: Points that anchor parts of the image to prevent unwanted movement, like thumbtacks for specific elements
  - *From: Kijai/Thom293*

- **AniWan Merge**: A simple merge to reduce the strength of AniWan Lora embedded in the model
  - *From: ZRNR*

- **Detail Transfer**: Technique for maintaining fine details when upscaling videos
  - *From: ZRNR*

- **Self-forcing model**: Fast inference model that works with very low steps but limited to 1.3b loras
  - *From: patientx*

- **VACE block swap**: Memory optimization technique that moves results to offload_device to manage VRAM usage
  - *From: Kijai*

- **NAG (Negative Augmented Generation)**: Technique that only adds to crossattn with negligible speed loss but improves results
  - *From: Kijai*

- **NAG (Normalized Attention Guidance)**: CFG distillation technique that works like negative prompts but with CFG 1, good at following negative prompts and removing/improving elements
  - *From: Juampab12*

- **VACE block swap**: Memory management technique that offloads VACE processing to prevent VRAM overflow
  - *From: Kijai*

- **TeaCache vs MagCache**: Both are caching systems for video generation, MagCache performs similarly to TeaCache
  - *From: Kijai*

- **NAG (Negative Attention Guidance)**: Allows negative prompting with 1 CFG, 10-20% slower than normal but much faster than CFG
  - *From: Juampab12*

- **Phantom 'phantomity'**: Character consistency capability that gets lost when merged too strongly with T2V model
  - *From: ▲*

- **Block swap**: VRAM management technique needed for higher resolution generation in some workflows
  - *From: Kijai*

- **Self-forcing**: Training method that fixes autoregressive video diffusion's exposure bias by training models on their own outputs, not just ground truth
  - *From: SS*

- **CausVid and self-forcing relationship**: Pretty much the same thing but different tuning methods, only use distillation from them, don't use together
  - *From: Kijai*

- **NAG (Negative Attention Guidance)**: Cross attention patching technique that can be added to native the same way SLG was added
  - *From: Kijai*

- **Causal sampling**: Does 3 latents at a time with sliding window kv_cache, can theoretically generate infinite length but not yet working well in ComfyUI
  - *From: Kijai*

- **Differential diffusion with VACE**: Use mask on WanVideo encode node to control which parts of image are modified
  - *From: David Snow*

- **First Frame Last Frame (FFLF)**: Technique to anchor video generation between specific start and end frames
  - *From: blake37*

- **AccVideo**: A distillation lora for speed improvement, not as aggressive as CausVid
  - *From: TK_999*

- **HPS and MPS reward loras**: HPS favors prompt adherence, MPS prefers output video quality
  - *From: TK_999*

- **Shift parameter**: Changes timesteps, controls when most denoising happens in early vs later steps
  - *From: Juampab12*

- **Skip layer guidance**: Technique for improving results, works well with 1.3B model at low denoise
  - *From: chrisd0073*

- **NAG (Negative Augmentation Guidance)**: Node that provides CFG-like benefits at 1 CFG without 2x generation time penalty
  - *From: Ada*

- **Shift parameter**: Controls sigma decay curve - higher shift increases noise at the end of generation, giving more freedom for new structure at expense of finer detail
  - *From: voxJT*

- **Custom sigmas**: Creating custom scheduler with your own decay curve by overwriting the default scheduler settings
  - *From: voxJT*

- **MAGREF**: I2V model that handles input image as reference, takes up to 3 reference images
  - *From: Kijai*

- **MinimaxRemover**: 1.3B model without crossattn, no prompts or anything needed
  - *From: Kijai*

- **Purple models**: Native models have purple nodes due to how data is wrapped, different from custom wrapper nodes
  - *From: phazei*

- **ATI**: Moving points technology
  - *From: Draken*

- **MAGREF**: I2V (Image-to-Video) model that can't be merged with Phantom since they serve different purposes
  - *From: Kijai*

- **Set/Get nodes caching**: Virtual nodes that are technically same as direct connection, just visual
  - *From: Kijai*

- **Self-forcing**: A technique that improves video generation quality, works at 1.25 strength combined with other parameters
  - *From: yi*

- **ComfyUI vs Diffusers denoise handling**: ComfyUI adds steps when doing denoise so always ends up doing same steps, while diffusers just skips steps without adding them
  - *From: Kijai*

- **Digital transitions**: Animated transitions (wipes, fades, glitches) between two videos instead of static images
  - *From: David Snow*

- **Context window cross fades**: Non-continuity at transition points when extending videos, especially with speed LoRAs
  - *From: blake37*

- **Block swapping**: Memory optimization technique, native does automatically, wrapper requires manual configuration
  - *From: Kijai*

- **Progressive latent fusion**: Strategy for long smooth videos, similar to mimicmotion latent blending
  - *From: A.I.Warper*

- **Self-forcing**: A VACE technique for video processing
  - *From: Raphaël*

- **Flowmatch scheduler**: Scheduler used with LightX model, may not be the intended usage method
  - *From: TK_999*

- **Block swap**: Memory optimization technique that divides VRAM usage
  - *From: Kijai*

- **MAGREF**: I2V model that uses image embedding for reference, provides better character consistency than standard I2V
  - *From: DawnII*

- **Context windows vs latent method**: Two different approaches for long video generation - context windows can do endless generation while latent method cannot
  - *From: Kijai*

- **Differential diffusion in Wan**: Built into VACE, works differently than ComfyUI version - uses 127 grey values and prefers sharp edges over feathered masks
  - *From: DawnII*

- **Self Forcing**: Training technique - originally released as 1.3B models, adapted to 14B as 4step distill, then extracted as LoRA
  - *From: DawnII*

- **NAG (Normalized Attention Guidance)**: Allows negative prompts to work with CFG=1 when using distill LoRAs
  - *From: Screeb*

- **lightx2v distillation**: Uses self-forcing training instead of causal training, works with normal 21 latent count unlike causvid's 3 latents autoregressive approach
  - *From: Kijai*

- **uni3c**: Video control system that can lock camera movement and provide motion consistency
  - *From: Kijai*

- **loudnorm**: Audio normalization that the MultiTalk model was likely trained with
  - *From: Kijai*

- **block swap**: Memory management technique that moves transformer blocks between GPU and CPU to handle large models
  - *From: Kijai*

- **context windows**: Technique for generating longer videos by processing in overlapping chunks
  - *From: Juampab12*

- **MultiTalk masking for multiple subjects**: You mask the subjects and target the audio to specific faces for multi-speaker scenarios
  - *From: Kijai*

- **MAGREF model behavior**: Since it's reference model it's not strictly sticking to the start frame, but if you don't pad the input, it still starts from it
  - *From: Kijai*

- **NAG (Negative Attention Guidance)**: Method that allows negative prompting when CFG=1, works on attention mechanism with smart scaling
  - *From: TK_999*

- **MAGREF**: I2V model similar to Phantom that produces good likeness, works in native ComfyUI
  - *From: zelgo_*

- **UltraWan**: High-resolution LoRA for 1.3B model trained on 4k/8k content from UltraVideo dataset
  - *From: TK_999*

- **LightX2V vs CausVid**: LightX2V is proper diffusion implementation, CausVid was temporary hack solution
  - *From: mdkb*

- **NAG (Normalized Attention Guidance)**: Operates at conceptual level, rejecting related visual/thematic elements beyond just the specified keywords. Hair color associates with lighting, environments, and other aesthetic elements
  - *From: VRGameDevGirl84(RTX 5090)*

- **Context window limitations**: 81/121 frame limits affect continuity and may reset during long generations
  - *From: Guey.KhalaMari*

- **Flux face/chin**: Common artifact showing chin dimples/cleft chins that persist across generations, possibly from training data bias
  - *From: VRGameDevGirl84(RTX 5090)*

- **Progressive Reference Frame System**: Attempted solution to context window visual jumps by extracting latents from frames 75-80 of each context and using them as reference for next window
  - *From: AJO*

- **Zero Padding for LoRA compatibility**: Expanding smaller LoRA weight matrices by copying original values to corner and filling remainder with zeros to maintain compatibility across different model architectures
  - *From: Alisson Pereira*

- **Self-forcing**: LoRA technique that works with LCM for acceleration, can work with up to 4 steps
  - *From: Alisson Pereira*

- **Video-to-video**: Using existing video as input to generate new video with modifications while preserving structure
  - *From: VRGameDevGirl84(RTX 5090)*

- **Zero-shot voice cloning**: Creating voice clones from short audio samples without training
  - *From: TK_999*

- **Creative upscale**: Using denoise of 1.0 in v2v that essentially becomes text-to-video generation
  - *From: VRGameDevGirl84(RTX 5090)*

- **Self forcing LoRA**: LoRA that improves prompt following, particularly for 1.3B model
  - *From: Juampab12*

- **LoRA bleeding**: When LoRA characteristics affect other objects in scene unintentionally
  - *From: Jas*

- **UltraWan**: LoRA trained on 58.8k high-resolution videos to enable 1920x1080 or 4k video generation using the Wan 1.3b model
  - *From: Alisson Pereira*

- **Audio gain in MultiTalk**: Parameter that amplifies audio input detection, helping model pick up quieter sounds and improve lip sync accuracy
  - *From: Thom293*

- **Block swapping**: Memory management technique that helps with OOM issues when upscaling to high resolutions
  - *From: VRGameDevGirl84(RTX 5090)*

- **First Frame Flux**: Workflow that takes the first frame of video and runs it through Flux using depth/normal maps to create new style, then uses as VACE reference
  - *From: voxJT*

- **Self-forcing DMD**: Method used with VACE 1.3B model for better results on lower VRAM setups
  - *From: mdkb*

- **VACE embed splitting**: Using multiple separate VACE encodes for different control types rather than blending preprocessing renders together
  - *From: Nathan Shipley*

- **Diff Diff**: Feature hard coded into VACE encode for differential processing, activated by masks in various places
  - *From: A.I.Warper*

- **Zero_init_steps**: Always meant to be set to 1
  - *From: David Snow*

- **Model_threshold and Buffer in memory patcher**: Model_threshold set high initially then adjust based on VRAM usage, Buffer treated as ceiling/off-limits amount
  - *From: TK_999*

- **Automagic optimizer**: Optimizer that adjusts individual learning rate for each parameter instead of single rate for all parameters
  - *From: Alisson Pereira*

- **Block swapping**: Memory management technique that moves transformer blocks between CPU and GPU to reduce VRAM usage while processing
  - *From: samhodge*

- **Context extension with VACE**: VACE doesn't work with context extension, but driven frames seem to keep consistency when pushing through more frames on RAM
  - *From: Tango Adorbo*

- **Uni3C camera motion injection**: Unlike control, it's much 'softer' and really good for camera motion, but requires another video for reference
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Context overlap in MultiTalk**: Represents frames in batches, higher values reduce likelihood of introducing unwanted elements too early
  - *From: Bleedy (Madham)*

- **Silent LoRA failure**: LoRAs can appear to load without errors but actually fail silently, especially when using wrong model sizes
  - *From: Draken*

- **Context windows**: Batches of frames processed together, with overlap affecting consistency vs variation
  - *From: DawnII*

- **VACE**: Video control system for style transfer, inpainting, subject-driven, outpainting
  - *From: context*

- **Speed LoRAs**: LightX2V, CausVid for faster inference, trade quality for speed
  - *From: context*

- **Context options node**: Instead of generating 200 frames at once, you can choose to generate X frames at a time with an overlap of Y frames per generation, then blend the resulting output
  - *From: CJ*

- **VAE context dependency**: The VAE needs context to properly decode frames - single frame clips cause color distortion/flash, but clips with more frames decode properly
  - *From: CJ*

- **Pipe delimited text encoder**: A text encoding method that uses pipe symbols as delimiters
  - *From: VRGameDevGirl84(RTX 5090)*

- **Context overlap**: Feature that connects to 'Context Options' on sampler if using wrapper to handle videos longer than 5 seconds
  - *From: VK (5080 128gb)*

- **Self-forcing DMD**: Similar to CausVid but requires fewer steps, must use LCM scheduler
  - *From: David Snow*

- **Tile lora**: LoRA that enables true upscaling by adding fine detail rather than just cleaning edges, works with noise injection
  - *From: David Snow*

- **Align pose node**: Node that can match ControlNet pose to position and scale of person in image, allowing pose transfer across different scales/positions
  - *From: Jonathan*

- **Distorch loaders**: From multigpu pack, works similar to blockswap for memory management
  - *From: David Snow*

- **Sage++ mode**: Enhanced version of Sage Attention providing 5-7% speed improvement
  - *From: Kijai*

- **Context windows**: Method for generating longer videos by chunking into smaller batches with overlap
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Context windows in video generation**: Memory usage doesn't grow and blending is smoother, but gets really slow on long clips. Model still works best at frame count it was trained at
  - *From: Kijai*

- **ACC Vid scheduler**: Uses 50 steps as base to create time steps then chooses only about 10, the scheduler itself is probably unnecessary
  - *From: Kijai*


## Resources & Links

- **ComfyUI-TiledDiffusion** (repo)
  - https://github.com/shiimizu/ComfyUI-TiledDiffusion
  - *From: Colin*

- **ComfyUI-MultiGPU** (repo)
  - https://github.com/pollockjj/ComfyUI-MultiGPU
  - *From: Jonathan*

- **ComfyUI_PromptBatcher** (repo)
  - https://github.com/synthetai/ComfyUI_PromptBatcher
  - *From: VRGameDevGirl84(RTX 5090)*

- **Improved i2v accuracy model** (model)
  - https://civitai.com/models/1626197?modelVersionId=1852433
  - *From: 852話 (hakoniwa)*

- **DeZoomer's video inpainting workflow thread** (workflow)
  - https://discord.com/channels/1076117621407223829/1377706250376319106/1377706250376319106
  - *From: Zuko*

- **Fun Reward LoRAs** (lora)
  - https://huggingface.co/Kijai/Wan2.1-Fun-Reward-LoRAs-comfy/tree/main
  - *From: Daviejg*

- **Original Alibaba Reward LoRAs** (lora)
  - https://huggingface.co/alibaba-pai/Wan2.1-Fun-Reward-LoRAs
  - *From: Jonathan*

- **AccVideo repo** (repo)
  - https://github.com/aejion/AccVideo
  - *From: VRGameDevGirl84*

- **Phantom repo** (repo)
  - https://github.com/Phantom-video/Phantom
  - *From: VRGameDevGirl84*

- **VRGameDevGirl84's LoRAs on CivitAI** (lora)
  - https://civitai.green/models/1626063 and https://civitai.green/models/1613519
  - *From: VRGameDevGirl84*

- **50 new motion control LoRAs** (lora)
  - https://huggingface.co/collections/Remade-AI/wan21-14b-480p-i2v-loras-67d0e26f08092436b585919b
  - *From: SS*

- **Kontext playground** (tool)
  - https://playground.bfl.ai/image/generate
  - *From: Nekodificador*

- **Kontext API** (tool)
  - https://fal.ai/models/fal-ai/flux-pro/kontext
  - *From: Juampab12*

- **SkyReels-V2-I2V-1.3B-540P** (model)
  - https://huggingface.co/Skywork/SkyReels-V2-I2V-1.3B-540P/tree/main
  - *From: Colin*

- **Wan2.1 14B 480p I2V LoRAs collection** (lora collection)
  - https://huggingface.co/collections/Remade-AI/wan21-14b-480p-i2v-loras-67d0e26f08092436b585919b
  - *From: SS*

- **Fun Reward LoRAs (MPS/HPS)** (lora)
  - https://huggingface.co/Kijai/Wan2.1-Fun-Reward-LoRAs-comfy/tree/main
  - *From: VRGameDevGirl84(RTX 5090)*

- **CausVid LoRAs** (lora)
  - https://huggingface.co/Kijai/WanVideo_comfy/tree/main
  - *From: Bleedy (Madham)*

- **ComfyUI-CoCoTools_IO** (tool)
  - https://github.com/Conor-Collins/ComfyUI-CoCoTools_IO
  - *From: Nekodificador*

- **ComfyUI pose interpolation** (tool)
  - https://github.com/toyxyz/ComfyUI_pose_inter
  - *From: TK_999*

- **CausVid explanation Reddit post** (documentation)
  - https://old.reddit.com/r/StableDiffusion/comments/1l0jz1o/causvid_v2_help/mve6qsp/
  - *From: MilesCorban*

- **Uni3C configuration video** (tutorial)
  - https://www.youtube.com/watch?v=nDSoGe6K2U8
  - *From: yukass*

- **Wan-Toy-Transform LoRA** (model)
  - https://huggingface.co/Alibaba-Research-Intelligence-Computing/wan-toy-transform
  - *From: hicho*

- **Wan14B-Cyberpop-Lora** (model)
  - https://huggingface.co/davesnow1/Wan14B-Cyberpop-Lora
  - *From: David Snow*

- **VideoX-Fun ComfyUI support** (repo)
  - https://github.com/aigc-apps/VideoX-Fun
  - *From: hicho*

- **Enhance-A-Video** (repo)
  - https://github.com/NUS-HPC-AI-Lab/Enhance-A-Video
  - *From: fazeaction*

- **ATI Trajectory Editor** (tool)
  - https://github.com/bytedance/ATI
  - *From: Juampab12*

- **Pixelization node** (tool)
  - https://github.com/WuZongWei6/Pixelization
  - *From: Juampab12*

- **NAG spline editor** (tool)
  - https://chendaryen.github.io/NAG.github.io/
  - *From: Nekodificador*

- **Wan Cinematic Video Prompt Generator** (tool)
  - https://chatgpt.com/g/g-67c3a6d6d19c81919b3247d2bfd01d0b-wan-cinematic-video-prompt-generator
  - *From: VRGameDevGirl84*

- **ATI Official Trajectory Editor** (tool)
  - https://github.com/bytedance/ATI/commit/e9d745e45a768802a419fcc1ed1d6677f18d73e9
  - *From: Juampab12*

- **RTMPose Body2d model** (model)
  - https://huggingface.co/qualcomm/RTMPose_Body2d
  - *From: David Snow*

- **X-Pose repository** (repo)
  - https://github.com/IDEA-Research/X-Pose
  - *From: A.I.Warper*

- **ComfyUi-WanVaceToVideoAdvanced** (node)
  - https://github.com/BigStationW/ComfyUi-WanVaceToVideoAdvanced
  - *From: hicho*

- **Wan Detailer LoRA** (lora)
  - https://civitai.com/models/1626063
  - *From: VRGameDevGirl84(RTX 5090)*

- **RealisDance** (repo)
  - https://github.com/damo-cv/RealisDance
  - *From: Kijai*

- **OmniConsistency** (model)
  - https://huggingface.co/showlab/OmniConsistency/tree/main
  - *From: hicho*

- **Comfyui_OmniConsistency** (node)
  - https://github.com/lc03lc/Comfyui_OmniConsistency
  - *From: hicho*

- **ATI GitHub repository** (repo)
  - https://github.com/bytedance/ATI
  - *From: toyxyz*

- **ATI example workflow** (workflow)
  - https://github.com/kijai/ComfyUI-WanVideoWrapper/blob/main/example_workflows/wanvideo_ATI_testing_01.json
  - *From: toyxyz*

- **Wan Fun-Reward-LoRAs** (model)
  - https://huggingface.co/alibaba-pai/Wan2.1-Fun-Reward-LoRAs
  - *From: Jonathan*

- **ContentV-8B model** (model)
  - https://huggingface.co/ByteDance/ContentV-8B
  - *From: ramonguthrie*

- **AccVideo WanX I2V** (model)
  - https://huggingface.co/aejion/AccVideo-WanX-I2V-480P-14B
  - *From: mkt*

- **OmniSync lipsync project** (repo)
  - https://ziqiaopeng.github.io/OmniSync/
  - *From: hau*

- **ComfyUI Lora Manager** (tool)
  - https://github.com/willmiao/ComfyUI-Lora-Manager/raw/main/static/images/one-click-send.jpg
  - *From: hicho*

- **AccVideo I2V 14B LoRA** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/blob/main/Wan21_AccVid_I2V_480P_14B_lora_rank32_fp16.safetensors
  - *From: Kijai*

- **CameraBench dataset** (dataset)
  - https://huggingface.co/datasets/syCen/CameraBench
  - *From: mamad8*

- **Uni3C paper and examples** (research)
  - https://ewrfcas.github.io/Uni3C/
  - *From: Juampab12*

- **FlowMo paper** (research)
  - https://arxiv.org/pdf/2506.01144
  - *From: yi*

- **FlowMo project page** (research)
  - https://arielshaulov.github.io/FlowMo/
  - *From: yi*

- **Gaussian Splats implementation** (repo)
  - https://github.com/btsmart/splatt3r?tab=readme-ov-file
  - *From: Juampab12*

- **Gaze Control ComfyUI node** (node)
  - https://github.com/Malu05/ComfyUI-Gaze/tree/main
  - *From: Mads Hagbarth Damsbo*

- **Pennzoil Viper commercial reference** (reference)
  - https://www.youtube.com/watch?v=PUodFjt01CY
  - *From: Ruairi Robinson*

- **WAN LoRA thread** (thread)
  - https://discord.com/channels/1076117621407223829/1379128970183839846
  - *From: VRGameDevGirl84(RTX 5090)*

- **Fun Reward LoRAs** (model)
  - https://huggingface.co/alibaba-pai/Wan2.1-Fun-Reward-LoRAs
  - *From: Jonathan*

- **TensorRT 10.10.0.31 for Windows** (tool)
  - https://developer.nvidia.com/downloads/compute/machine-learning/tensorrt/10.10.0/zip/TensorRT-10.10.0.31.Windows.win10.cuda-12.9.zip
  - *From: samhodge*

- **CUDA Downloads** (tool)
  - https://developer.nvidia.com/cuda-downloads
  - *From: samhodge*

- **SageAttention for Windows** (tool)
  - https://github.com/sdbds/SageAttention-for-windows/releases
  - *From: samhodge*

- **ComfyUI Save File Formatting docs** (documentation)
  - https://blenderneko.github.io/ComfyUI-docs/Interface/SaveFileFormatting/
  - *From: ˗ˏˋ⚡ˎˊ-*

- **WanVideo ComfyUI models** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy
  - *From: samhodge*

- **Wan 2.1 ComfyUI repackaged** (model)
  - https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/blob/main/split_files/diffusion_models/wan2.1_i2v_480p_14B_bf16.safetensors
  - *From: MilesCorban*

- **SageAttention Windows releases** (tool)
  - https://github.com/woct0rdho/SageAttention/releases/tag/v2.1.1-windows
  - *From: Kijai*

- **Triton Windows** (tool)
  - https://github.com/woct0rdho/triton-windows
  - *From: Kijai*

- **CoTracker ComfyUI node** (node)
  - https://github.com/s9roll7/comfyui_cotracker_node
  - *From: tttADs*

- **Banodoco Wan Discussion KB** (knowledge base)
  - https://notebooklm.google.com/notebook/a08901b9-0511-4926-bbf8-3c86a12dc306
  - *From: Nathan Shipley*

- **Wan ATI 14B model** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/blob/main/Wan2_1-I2V-ATI-14B_fp8_e4m3fn.safetensors
  - *From: Juampab12*

- **DCM GitHub repository** (repo)
  - https://github.com/Vchitect/DCM
  - *From: yi*

- **BETA Helper Nodes** (tool)
  - https://github.com/Burgstall-labs/ComfyUI-BETA-Helpernodes
  - *From: AJO*

- **ATI workflow example** (workflow)
  - https://github.com/kijai/ComfyUI-WanVideoWrapper/blob/main/example_workflows/wanvideo_ATI_testing_01.json
  - *From: Juampab12*

- **CausVid autoregressive checkpoint** (model)
  - https://huggingface.co/tianweiy/CausVid/tree/main/autoregressive_checkpoint_warp_4step_cfg2
  - *From: hicho*

- **FlowMo repository** (repo)
  - https://github.com/arielshaulov/FlowMo
  - *From: JohnDopamine*

- **Master merge model** (model)
  - https://huggingface.co/vrgamedevgirl84/Wan14BT2V_MasterModel
  - *From: VRGameDevGirl84(RTX 5090)*

- **VRGameDevGirl84's Wan14BT2V Master Model** (model)
  - https://huggingface.co/vrgamedevgirl84/Wan14BT2V_MasterModel
  - *From: hicho*

- **CausVid autoregressive checkpoint** (model)
  - https://huggingface.co/tianweiy/CausVid/tree/main/autoregressive_checkpoint_warp_4step_cfg2
  - *From: hicho*

- **Realism Boost LoRA** (lora)
  - https://civitai.com/models/1626063
  - *From: VRGameDevGirl84(RTX 5090)*

- **Invisible Person Living Clothes LoRA** (lora)
  - https://civitai.com/models/1650084/invisible-person-living-clothes-wan21-t2v-i2v-14b?modelVersionId=1867692
  - *From: hicho*

- **Wan2.1-VACE-14B-GGUF** (model)
  - https://huggingface.co/QuantStack/Wan2.1-VACE-14B-GGUF
  - *From: samhodge*

- **CausVid v1.5 no first block** (lora)
  - https://huggingface.co/Kijai/WanVideo_comfy/resolve/main/Wan21_CausVid_14B_T2V_lora_rank32_v1_5_no_first_block.safetensors
  - *From: The Punisher*

- **ClownShark_BatWing guide image writeup** (guide)
  - https://discord.com/channels/1076117621407223829/1342763350815277067/1380049063897993247
  - *From: TK_999*

- **RES4LYF repository** (repo)
  - https://github.com/ClownsharkBatwing/RES4LYF
  - *From: TK_999*

- **TIC-FT research** (research)
  - https://kinam0252.github.io/TIC-FT/
  - *From: toyxyz*

- **AccVid I2V LoRA** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/blob/main/Wan21_AccVid_I2V_480P_14B_lora_rank32_fp16.safetensors
  - *From: Jonathan*

- **Google AI Studio API** (tool)
  - https://aistudio.google.com/apikey
  - *From: Flipping Sigmas*

- **FlowMo** (repo)
  - https://github.com/arielshaulov/FlowMo
  - *From: MisterMango*

- **Wan official site** (website)
  - https://wan.video/
  - *From: TK_999*

- **Text-to-pose model** (repo)
  - https://github.com/clement-bonnet/text-to-pose
  - *From: JohnDopamine*

- **ComfyUI-WarperNodes** (repo)
  - https://github.com/AIWarper/ComfyUI-WarperNodes
  - *From: A.I.Warper*

- **Detail LoRA for Wan** (model)
  - https://huggingface.co/kayte0342/wan2.1_lora/blob/main/detailz-wan.safetensors
  - *From: The Punisher*

- **ComfyUI Ultimate OpenPose Editor** (tool)
  - https://github.com/toyxyz/ComfyUI-ultimate-openpose-editor
  - *From: A.I.Warper*

- **Wan14B MasterModel GGUF** (model)
  - https://huggingface.co/lym00/Wan14BT2V_MoviiGen_AccVid_CausVid_MasterModel_GGUF
  - *From: The Punisher*

- **Nathan's NotebookLM** (tool)
  - https://notebooklm.google.com/notebook/a08901b9-0511-4926-bbf8-3c86a12dc306
  - *From: chrisd0073*

- **Wan NotebookLM** (tool)
  - https://notebooklm.google.com/notebook/a08901b9-0511-4926-bbf8-3c86a12dc306
  - *From: Nathan Shipley*

- **WAN2114BT2V-FusionX merge** (model)
  - https://civitai.com/models/1651125/wan2114bt2v-fusionx
  - *From: VRGameDevGirl84(RTX 5090)*

- **FlowMo** (repo)
  - https://github.com/arielshaulov/FlowMo
  - *From: MisterMango*

- **Pixel3DMM** (repo)
  - https://github.com/SimonGiebenhain/pixel3dmm
  - *From: Nekodificador*

- **Wan2GP speech-audio to character** (repo)
  - https://github.com/deepbeepmeep/Wan2GP
  - *From: Valle*

- **CausVid V2 Lora** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/blob/main/Wan21_CausVid_14B_T2V_lora_rank32_v2.safetensors
  - *From: Danial*

- **ATI, Uni3C, NormalCrafter & Any2Bokeh deep dive** (tutorial)
  - https://www.youtube.com/watch?v=0cw2N3W7nKo
  - *From: Adrien Toupet*

- **AniSora V2 benchmark update** (repo)
  - https://github.com/bilibili/Index-anisora/commit/0b2a6fec8d
  - *From: DevouredBeef*

- **ATI trajectory editor rebuilt version** (tool)
  - provided by Juampab12
  - *From: Juampab12*

- **Workflow resources in Discord** (workflows)
  - Multiple Discord channel links provided
  - *From: Adrien Toupet*

- **VRGameDevGirl84 Phantom Merge** (model)
  - https://civitai.green/models/1651125?modelVersionId=1878555
  - *From: Colin*

- **Quick Connections ComfyUI Node** (tool)
  - https://github.com/niknah/quick-connections
  - *From: Valle*

- **WAN I2V Example Workflow** (workflow)
  - https://github.com/comfyanonymous/ComfyUI_examples/blob/master/wan/image_to_video_wan_example.json
  - *From: samhodge*

- **WAN V2V Example Workflow** (workflow)
  - https://github.com/kijai/ComfyUI-WanVideoWrapper/blob/main/example_workflows/wanvideo_vid2vid_example_01.json
  - *From: Colin*

- **MultiTalk GitHub** (repo)
  - https://github.com/MeiGen-AI/MultiTalk
  - *From: toyxyz*

- **MultiTalk Issues** (repo)
  - https://github.com/MeiGen-AI/MultiTalk/issues/2
  - *From: toyxyz*

- **CausVid 1.3B LoRA** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/blob/main/Wan21_CausVid_bidirect2_T2V_1_3B_lora_rank32.safetensors
  - *From: David Snow*

- **CausVid V1.5 LoRA** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/blob/main/Wan21_CausVid_14B_T2V_lora_rank32_v1_5_no_first_block.safetensors
  - *From: David Snow*

- **Wan Fun Reward LoRAs** (model)
  - https://huggingface.co/alibaba-pai/Wan2.1-Fun-Reward-LoRAs/tree/main
  - *From: David Snow*

- **Alibaba Fun InP 1.3B I2V** (model)
  - https://huggingface.co/alibaba-pai/Wan2.1-Fun-V1.1-1.3B-InP/tree/main
  - *From: hicho*

- **SkyReels V2 I2V 1.3B** (model)
  - https://huggingface.co/Skywork/SkyReels-V2-I2V-1.3B-540P/tree/main
  - *From: hicho*

- **WanVideo Diffusion Forcing Example** (workflow)
  - https://github.com/kijai/ComfyUI-WanVideoWrapper/blob/main/example_workflows/wanvideo_skyreels_diffusion_forcing_extension_example_01.json
  - *From: samhodge*

- **MatAnyone Kytra for masking** (tool)
  - https://github.com/KytraScript/ComfyUI_MatAnyone_Kytra?tab=readme-ov-file
  - *From: hicho*

- **SageAttention installation** (tool)
  - https://github.com/thu-ml/SageAttention
  - *From: Colin*

- **ComfyUI LBM** (tool)
  - https://github.com/1038lab/ComfyUI-LBM
  - *From: chrisd0073*

- **Native VACE guide** (documentation)
  - https://docs.comfy.org/tutorials/video/wan/vace
  - *From: lym0*

- **Phantom example workflow** (workflow)
  - https://huggingface.co/QuantStack/Phantom_Wan_14B-GGUF/resolve/main/Phantom_example_workflow.json
  - *From: lym0*

- **Quick connections ComfyUI plugin** (tool)
  - https://github.com/niknah/quick-connections
  - *From: the_darkwatarus_museum*

- **Self-forcing conversion script** (script)
  - *From: Kijai*

- **FusionX model** (model)
  - https://civitai.com/models/1651125?modelVersionId=1882322
  - *From: Juan Gea*

- **MultiTalk repository** (repo)
  - https://github.com/MeiGen-AI/MultiTalk
  - *From: ZeusZeus*

- **Self-forcing repository** (repo)
  - https://github.com/guandeh17/Self-Forcing
  - *From: NebSH*

- **SkyReels V2** (repo)
  - https://github.com/SkyworkAI/SkyReels-V2
  - *From: Impactframes*

- **Wan prompt format guide** (workflow)
  - *From: MilesCorban*

- **NotebookLM Wan knowledge base** (tool)
  - https://notebooklm.google.com/notebook/a08901b9-0511-4926-bbf8-3c86a12dc306
  - *From: Nathan Shipley*

- **ComfyUI-leo-RealisDance** (repo)
  - https://github.com/leeooo001/ComfyUI-leo-RealisDance
  - *From: jellybean5361*

- **Self-Forcing models** (model)
  - https://huggingface.co/gdhe17/Self-Forcing/tree/main/checkpoints
  - *From: Jonathan*

- **Self-Forcing GitHub repository** (repo)
  - https://github.com/guandeh17/Self-Forcing
  - *From: MysteryShack*

- **MPS LoRA for motion and detail** (model)
  - https://huggingface.co/alibaba-pai/Wan2.1-Fun-Reward-LoRAs
  - *From: Jonathan*

- **MultiTalk lip-sync** (repo)
  - https://github.com/MeiGen-AI/MultiTalk
  - *From: orabazes*

- **Triton installation guide** (tool)
  - https://civitai.com/articles/12851/easy-installation-triton-and-sageat
  - *From: Charlie*

- **NotebookLM ChatGPT based on channel** (tool)
  - https://notebooklm.google.com/notebook/a08901b9-0511-4926-bbf8-3c86a12dc306
  - *From: pom*

- **Wan loop video workflow** (workflow)
  - https://github.com/toyxyz/ComfyUI_toyxyz_test_nodes/blob/main/workflow/wan_2_1_vace_loop_vid.json
  - *From: toyxyz*

- **Self-forcing VACE merge model** (model)
  - https://huggingface.co/lym00/Wan2.1-T2V-1.3B-Self-Forcing-VACE
  - *From: hicho*

- **VACE+Phantom merged model** (model)
  - https://huggingface.co/Inner-Reflections/Wan2.1_VACE_Phantom
  - *From: Piblarg*

- **Self-forcing paper and demo** (research)
  - https://self-forcing.github.io/
  - *From: izashin*

- **ComfyUI native workflow examples** (workflow)
  - https://blog.comfy.org/p/wan21-vace-native-support-and-ace
  - *From: Jonathan*

- **Ostris WAN LoRA trainer** (tool)
  - https://replicate.com/ostris/wan-lora-trainer/train
  - *From: Ruairi Robinson*

- **MagCache optimization** (repo)
  - https://github.com/Zehong-Ma/MagCache
  - *From: MaQue*

- **SeedVR video super resolution** (repo)
  - https://github.com/ByteDance-Seed/SeedVR
  - *From: JohnDopamine*

- **ComfyUI MultiGPU offloading** (tool)
  - https://github.com/pollockjj/ComfyUI-MultiGPU
  - *From: Jonathan*

- **ComfyUI Model Unloader** (tool)
  - https://github.com/SeanScripts/ComfyUI-Unload-Model
  - *From: Jonathan*

- **AE Keyframe Converter web app** (tool)
  - https://claude.ai/public/artifacts/42e5c3cc-f8be-4157-abde-759747e5ee19
  - *From: Nathan Shipley*

- **AE Keyframe Export Script** (script)
  - https://gist.github.com/nathanshipley/fb7ff367364f12923952cf8510558e70
  - *From: Nathan Shipley*

- **Video walkthrough for AE conversion** (tutorial)
  - https://youtu.be/RQkKLuACzfQ
  - *From: Nathan Shipley*

- **Wan LoRA trainer** (tool)
  - https://replicate.com/ostris/wan-lora-trainer/train
  - *From: Ruairi Robinson*

- **VACE FusionX model** (model)
  - https://civitai.com/models/1651125?modelVersionId=1868891
  - *From: Ruairi Robinson*

- **Supervision tracking library** (repo)
  - https://github.com/roboflow/supervision
  - *From: A.I.Warper*

- **MagCache ComfyUI nodes** (repo)
  - https://github.com/Zehong-Ma/ComfyUI-MagCache
  - *From: yi*

- **MagRef video project** (repo)
  - https://magref-video.github.io/magref.github.io/
  - *From: Dream Making*

- **Phantom video project** (repo)
  - https://github.com/Phantom-video/Phantom
  - *From: Juampab12*

- **Self-Forcing model** (model)
  - https://huggingface.co/gdhe17/Self-Forcing/blob/main/checkpoints/self_forcing_sid_v2.pt
  - *From: Mngbg*

- **Wan2GP workflow** (workflow)
  - https://github.com/deepbeepmeep/Wan2GP
  - *From: Thom293*

- **NAG official demo** (demo)
  - https://huggingface.co/spaces/ChenDY/NAG_wan2-1-fast
  - *From: Kijai*

- **NAG GitHub repository** (repo)
  - https://github.com/ChenDarYen/Normalized-Attention-Guidance
  - *From: zelgo_*

- **Cosmos Predict2 models** (model)
  - https://huggingface.co/collections/nvidia/cosmos-predict2-68028efc052239369a0f2959
  - *From: ZeusZeus (RTX 4090)*

- **VACE long form scripts** (workflow)
  - https://www.patreon.com/posts/vace-long-form-130737806
  - *From: chrisd0073*

- **LoRAEdit project** (repo)
  - https://github.com/cjeen/LoRAEdit
  - *From: toyxyz*

- **VRGameDevGirl84 Phantom model** (model)
  - https://civitai.com/models/1651125?modelVersionId=1878555
  - *From: David Snow*

- **ComfyUI-FLOAT VRAM optimization** (tool)
  - https://www.reddit.com/r/comfyui/comments/1l9f11u/great_news_for_comfyuifloat_users_vram_usage/
  - *From: scf*

- **ComfyUI-DirGir for batching** (node)
  - https://github.com/AshMartian/ComfyUI-DirGir
  - *From: DevouredBeef*

- **ComfyUI-keitNodes** (node)
  - https://github.com/keit0728/ComfyUI-keitNodes
  - *From: 327467189525282816*

- **LoRAEdit** (tool)
  - https://github.com/cjeen/LoRAEdit
  - *From: Juampab12*

- **MultiTalk** (model)
  - https://github.com/MeiGen-AI/MultiTalk
  - *From: Juampab12*

- **Magic-TryOn** (project)
  - https://vivocameraresearch.github.io/magictryon/
  - *From: JohnDopamine*

- **HyperMotion** (controlnet)
  - https://vivocameraresearch.github.io/hypermotion/
  - *From: yi*

- **ContentV-8B** (model)
  - https://huggingface.co/ByteDance/ContentV-8B
  - *From: hicho*

- **Self-forcing paper and demo** (research)
  - https://self-forcing.github.io/ and https://www.youtube.com/watch?v=v53Hdk1695Y
  - *From: SS*

- **Pixel3DMM for VACE inputs** (tool)
  - https://github.com/SimonGiebenhain/pixel3dmm
  - *From: A.I.Warper*

- **FLAME for VACE inputs** (tool)
  - https://flame.is.tue.mpg.de/
  - *From: A.I.Warper*

- **Cosmos1 diffusion renderer** (repo)
  - https://github.com/nv-tlabs/cosmos1-diffusion-renderer
  - *From: A.I.Warper*

- **MAGREF models/code** (repo)
  - https://github.com/MAGREF-Video/MAGREF
  - *From: JohnDopamine*

- **HyperMotion weights** (model)
  - https://huggingface.co/shuolin/HyperMotion/tree/main
  - *From: yi*

- **LightX2V 14B distill model** (model)
  - https://github.com/ModelTC/lightx2v/commit/76bb342122e68885c4f0661fb77554b830b1eb34
  - *From: Kijai*

- **Yi's custom sampler and scheduler** (workflow)
  - https://discord.com/channels/1076117621407223829/1342763350815277067/1383486714349224146
  - *From: yi*

- **FusionX workflows and loras** (workflow)
  - https://civitai.com/models/1681541/workflows-for-wan21fusionx-loras
  - *From: blake37*

- **FusionX lora** (lora)
  - https://civitai.com/models/1678575/wan21fusionx-the-lora
  - *From: blake37*

- **DagThomas LLM nodes for ComfyUI** (repo)
  - https://github.com/dagthomas/comfyui_dagthomas?tab=readme-ov-file#ollamanode
  - *From: JohnDopamine*

- **SmolLM2-1.7B-Instruct** (model)
  - https://huggingface.co/HuggingFaceTB/SmolLM2-1.7B-Instruct
  - *From: hicho*

- **Wavespeed.ai Bytedance models** (tool)
  - https://wavespeed.ai/collections/bytedance
  - *From: scf*

- **Wan 2.1 official paper** (paper)
  - https://arxiv.org/abs/2503.20314
  - *From: Jonathan*

- **Wan official website** (website)
  - https://wan.video/
  - *From: Jonathan*

- **LightX2V optimization repo** (repo)
  - https://github.com/ModelTC/lightx2v
  - *From: yi*

- **ComfyUI Cosmos examples** (workflow)
  - https://github.com/comfyanonymous/ComfyUI_examples/tree/master/cosmos
  - *From: slmonker*

- **ComfyUI-MultiGPU** (repo)
  - https://github.com/pollockjj/ComfyUI-MultiGPU
  - *From: chrisd0073*

- **ComfyUI Ultimate SD Upscale** (repo)
  - https://github.com/atdigit/ComfyUI_Ultimate_SD_Upscale
  - *From: David Snow*

- **janky_memory_patcher** (tool)
  - https://github.com/drozbay/janky_memory_patcher
  - *From: TK_999*

- **ComfyUI-AjoNodes** (repo)
  - https://github.com/AJO-reading/ComfyUI-AjoNodes
  - *From: AJO*

- **Wan seamless loop workflow** (workflow)
  - https://civitai.com/models/1426572/wan-21-seamless-loop-workflow-i2v
  - *From: Alisson Pereira*

- **Wan14B_realismboost_t2v** (model)
  - https://civitai.com/models/1626063/wan14bdetailerenhancert2v
  - *From: MilesCorban*

- **GigaVideo-1 research** (research)
  - https://gigavideo-1.github.io/
  - *From: yi*

- **SageAttention GitHub** (repo)
  - https://github.com/thu-ml/SageAttention
  - *From: blake37*

- **SeedVR upscaler** (tool)
  - https://github.com/ByteDance-Seed/SeedVR
  - *From: shockgun*

- **LightX2V Wan2.1 T2V 14B model** (model)
  - https://huggingface.co/lightx2v/Wan2.1-T2V-14B-StepDistill-CfgDistill
  - *From: yi*

- **LightX2V LoRA by Kijai** (lora)
  - https://huggingface.co/Kijai/WanVideo_comfy/blob/main/Wan21_T2V_14B_lightx2v_cfg_step_distill_lora_rank32.safetensors
  - *From: Kijai*

- **LightX2V scheduler code** (code)
  - https://github.com/ModelTC/lightx2v/blob/76bb342122e68885c4f0661fb77554b830b1eb34/lightx2v/models/schedulers/wan/step_distill/scheduler.py
  - *From: Kijai*

- **LightX2V LoRA** (lora)
  - https://huggingface.co/Kijai/WanVideo_comfy/blob/main/Wan21_T2V_14B_lightx2v_cfg_step_distill_lora_rank32.safetensors
  - *From: David Snow*

- **MovieGen benchmark prompts** (repo)
  - https://github.com/guandeh17/Self-Forcing/tree/main/prompts
  - *From: Kijai*

- **LightX full model** (model)
  - https://huggingface.co/lightx2v/Wan2.1-T2V-14B-StepDistill-CfgDistill/tree/main
  - *From: chrisd0073*

- **MAGREF HuggingFace** (model)
  - https://huggingface.co/MAGREF-Video/MAGREF/tree/main
  - *From: yi*

- **MAGREF paper** (paper)
  - https://magref-video.github.io/magref.github.io/
  - *From: yi*

- **Spline Path Control Tool** (tool)
  - https://whatdreamscost.github.io/Spline-Path-Control/
  - *From: Jonathan*

- **MAGREF 14B fp8 model** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/blob/main/Wan2_1-Wan-I2V-MAGREF-14B_fp8_e4m3fn.safetensors
  - *From: Kijai*

- **lightx2v LoRA** (lora)
  - https://huggingface.co/Kijai/WanVideo_comfy/blob/main/Wan21_T2V_14B_lightx2v_cfg_step_distill_lora_rank32.safetensors
  - *From: David Snow*

- **Wan21_T2V_14B_lightx2v_cfg_step_distill_lora_rank32.safetensors** (lora)
  - https://huggingface.co/Kijai/WanVideo_comfy/blob/main/Wan21_T2V_14B_lightx2v_cfg_step_distill_lora_rank32.safetensors
  - *From: Jas*

- **Wan 2.1 Knowledge Base** (documentation)
  - https://nathanshipley.notion.site/Wan-2-1-Knowledge-Base-1d691e115364814fa9d4e27694e9468f#1d691e11536481f380e4cbf7fa105c05
  - *From: JohnDopamine*

- **NotebookLM Wan chatbot** (tool)
  - https://notebooklm.google.com/notebook/a08901b9-0511-4926-bbf8-3c86a12dc306
  - *From: Nathan Shipley*

- **ComfyUI-HunyuanAvatar_Sm** (repo)
  - https://github.com/smthemex/ComfyUI_HunyuanAvatar_Sm
  - *From: AJO*

- **LatentSync ComfyUI Wrapper** (repo)
  - https://github.com/ShmuelRonen/ComfyUI-LatentSyncWrapper
  - *From: AJO*

- **MAGREF model** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/tree/main
  - *From: JohnDopamine*

- **Minimax Remover model** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/blob/main/Wan2_1-MiniMaxRemover_1_3B_fp16.safetensors
  - *From: toyxyz*

- **MultiTalk project** (project)
  - https://meigen-ai.github.io/multi-talk/
  - *From: Kijai*

- **LightX2V LoRA** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/blob/main/Wan21_T2V_14B_lightx2v_cfg_step_distill_lora_rank32.safetensors
  - *From: David Snow*

- **MatAnyone ComfyUI node** (tool)
  - https://github.com/KytraScript/ComfyUI_MatAnyone_Kytra
  - *From: JohnDopamine*

- **UltraSharp LoRA** (model)
  - https://civitai.com/models/1683455/ultrasharpcc
  - *From: The Shadow (NYC)*

- **Wan 2.1 CausVid workflow** (workflow)
  - https://civitai.com/articles/15189/wan21-causvid-workflow-for-t2v-i2v-vace-all-the-things
  - *From: phazei*

- **LightX2V Step+CFG Distill model** (model)
  - https://huggingface.co/lightx2v/Wan2.1-T2V-14B-StepDistill-CfgDistill
  - *From: Kijai*

- **LightX2V LoRA** (lora)
  - https://huggingface.co/Kijai/WanVideo_comfy/blob/main/Wan21_T2V_14B_lightx2v_cfg_step_distill_lora_rank32.safetensors
  - *From: Kijai*

- **VACE User Guide** (documentation)
  - https://github.com/ali-vilab/VACE/blob/main/UserGuide.md
  - *From: ingi // SYSTMS*

- **FlowMatch Scheduler** (node)
  - https://github.com/BigStationW/flowmatch_scheduler-comfyui
  - *From: Ada*

- **AniWan model** (model)
  - https://civitai.com/models/1626197/aniwan2114bfp8e4m3fn?modelVersionId=1852433
  - *From: ZRNR*

- **Depth Anything V2 VitG** (model)
  - https://huggingface.co/Nap/depth_anything_v2_vitg
  - *From: DawnII*

- **ChronoDepth** (repo)
  - https://github.com/jiahao-shao1/ChronoDepth
  - *From: A.I.Warper*

- **ComfyUI-bleh for TAESD** (repo)
  - https://github.com/blepping/ComfyUI-bleh
  - *From: Kijai*

- **Video super resolution paper** (paper)
  - https://arxiv.org/abs/2506.15591
  - *From: yi*

- **WanVideo ComfyUI models** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy
  - *From: TK_999*

- **MeiGen MultiTalk model** (model)
  - https://huggingface.co/MeiGen-AI/MeiGen-MultiTalk/blob/main/multitalk.safetensors
  - *From: Kijai*

- **Chinese wav2vec2 model** (model)
  - https://huggingface.co/TencentGameMate/chinese-wav2vec2-base/tree/main
  - *From: Kijai*

- **UltraWan LoRA and dataset** (model)
  - https://huggingface.co/APRIL-AIGC/UltraWan/tree/main
  - *From: yi*

- **UltraVideo dataset** (dataset)
  - https://huggingface.co/datasets/APRIL-AIGC/UltraVideo
  - *From: yi*

- **MAGREF model** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/blob/main/Wan2_1-Wan-I2V-MAGREF-14B_fp8_e4m3fn.safetensors
  - *From: The Shadow (NYC)*

- **GlitchNodes for video masking** (tool)
  - https://github.com/pxl-pshr/GlitchNodes?tab=readme-ov-file#vhsonacid-node
  - *From: MilesCorban*

- **UltraWan LoRA** (model)
  - https://xzc-zju.github.io/projects/UltraVideo/
  - *From: Alisson Pereira*

- **Self-Forcing 1.3B models** (model)
  - https://huggingface.co/gdhe17/Self-Forcing
  - *From: DawnII*

- **lightx2v distill LoRA** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/blob/main/Wan21_T2V_14B_lightx2v_cfg_step_distill_lora_rank32.safetensors
  - *From: Kijai*

- **DOVE upscaling research** (repo)
  - https://github.com/zhengchen1999/DOVE
  - *From: yi*

- **MultiTalk fp8 model** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/blob/main/WanVideo_2_1_Multitalk_14B_fp8_e4m3fn.safetensors
  - *From: Kijai*

- **Audio separation nodes** (tool)
  - https://github.com/christian-byrne/audio-separation-nodes-comfyui
  - *From: burgstall*

- **Chain-of-Zoom research** (repo)
  - https://github.com/bryanswkim/Chain-of-Zoom
  - *From: Draken*

- **MultiTalk repository** (repo)
  - https://github.com/MeiGen-AI/MultiTalk
  - *From: ˗ˏˋ⚡ˎˊ-*

- **UltraWanComfy model** (model)
  - https://huggingface.co/Alissonerdx/UltraWanComfy
  - *From: A.I.Warper*

- **MultiTalk workflow in Kijai examples folder** (workflow)
  - *From: Kijai*

- **Ultimate Vocal Remover** (tool)
  - https://github.com/Anjok07/ultimatevocalremovergui
  - *From: JohnDopamine*

- **MVSEP free audio separation** (tool)
  - https://mvsep.com/en/home
  - *From: JohnDopamine*

- **MAGREF model fp8** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/blob/main/Wan2_1-Wan-I2V-MAGREF-14B_fp8_e4m3fn.safetensors
  - *From: A.I.Warper*

- **Chinese wav2vec2 model** (model)
  - https://huggingface.co/TencentGameMate/chinese-wav2vec2-base
  - *From: DevouredBeef*

- **MultiTalk original paper** (repo)
  - https://github.com/MeiGen-AI/MultiTalk?tab=readme-ov-file
  - *From: burgstall*

- **AniWan models collection** (model)
  - https://civitai.com/models/1626197
  - *From: Yae*

- **MAGREF model** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/blob/main/Wan2_1-Wan-I2V-MAGREF-14B_fp8_e4m3fn.safetensors
  - *From: zelgo_*

- **UltraWan LoRA** (lora)
  - https://huggingface.co/Alissonerdx/UltraWanComfy
  - *From: TK_999*

- **UltraVideo dataset** (dataset)
  - https://huggingface.co/datasets/APRIL-AIGC/UltraVideo
  - *From: TK_999*

- **ChatterBox TTS ComfyUI nodes** (node)
  - https://github.com/filliptm/ComfyUI_Fill-ChatterBox
  - *From: CJ*

- **ChatterBox original repo** (repo)
  - https://github.com/resemble-ai/chatterbox
  - *From: CJ*

- **MotionStreamer** (tool)
  - https://zju3dv.github.io/MotionStreamer/
  - *From: yi*

- **Spline Path Control v2** (tool)
  - https://whatdreamscost.github.io/Spline-Path-Control/
  - *From: Jonathan*

- **Spline Path Control source code** (repo)
  - https://github.com/WhatDreamsCost/Spline-Path-Control
  - *From: Jonathan*

- **NAG node for SDXL/SD1.5** (repo)
  - https://github.com/pamparamm/sd-perturbed-attention/commit/783901f5e017d287c187a0380941ac53fe6f1573
  - *From: JohnDopamine*

- **SeedVR2 VideoUpscaler** (repo)
  - https://github.com/numz/ComfyUI-SeedVR2_VideoUpscaler
  - *From: hicho*

- **UltraVideo documentation** (repo)
  - https://github.com/xzc-zju/UltraVideo
  - *From: Alisson Pereira*

- **UltraVideo project page** (documentation)
  - https://xzc-zju.github.io/projects/UltraVideo/
  - *From: Alisson Pereira*

- **Audio separation nodes** (repo)
  - https://github.com/christian-byrne/audio-separation-nodes-comfyui.git
  - *From: zelgo_*

- **Wan2.1-T2V-1.3B-Self-Forcing-VACE model** (model)
  - https://huggingface.co/lym00/Wan2.1-T2V-1.3B-Self-Forcing-VACE-Addon-Experiment/blob/main/Wan2.1-T2V-1.3B-Self-Forcing-DMD-VACE-FP16.safetensors
  - *From: ▲*

- **Google AI Studio** (tool)
  - https://aistudio.google.com/app/prompts/new_chat
  - *From: JohnDopamine*

- **ComfyUI-TuZi-Flux-Kontext nodes** (node)
  - *From: blake37*

- **ComfyUI_MatAnyone_Kytra for background removal** (repo)
  - https://github.com/KytraScript/ComfyUI_MatAnyone_Kytra
  - *From: JohnDopamine*

- **LoRAEdit for better VACE inpainting** (tool)
  - https://github.com/cjeen/LoRAEdit
  - *From: hablaba*

- **Audacity for audio conversion** (tool)
  - https://www.audacityteam.org/
  - *From: burgstall*

- **RES4LYF nodes** (repo)
  - https://github.com/ClownsharkBatwing/RES4LYF
  - *From: JohnDopamine*

- **UltraWan ComfyUI LoRA** (model)
  - https://huggingface.co/Alissonerdx/UltraWanComfy
  - *From: Alisson Pereira*

- **ComfyUI-VideoUpscale_WithModel** (repo)
  - https://github.com/ShmuelRonen/ComfyUI-VideoUpscale_WithModel
  - *From: Gateway {Dreaming Computers}*

- **ComfyUI-SeedVR2_VideoUpscaler** (repo)
  - https://github.com/numz/ComfyUI-SeedVR2_VideoUpscaler
  - *From: hicho*

- **Progressive Reference Frame MultiTalk fork** (repo)
  - https://github.com/adamreading/ComfyUI-WanVideoWrapper-MultiTalk
  - *From: AJO*

- **UltraWan 1K LoRA** (lora)
  - *From: Alisson Pereira*

- **Self-Forcing VACE Addon LoRA** (lora)
  - https://huggingface.co/lym00/Wan2.1-T2V-1.3B-Self-Forcing-VACE-Addon-Experiment/blob/main/Wan2.1-T2V-1.3B-Self-Forcing-DMD-FP16-LoRA-Rank32.safetensors
  - *From: Alisson Pereira*

- **CausVid bidirectional LoRA** (lora)
  - https://huggingface.co/Kijai/WanVideo_comfy/blob/main/Wan21_CausVid_bidirect2_T2V_1_3B_lora_rank32.safetensors
  - *From: JohnDopamine*

- **SkyReels V2 1.3B model** (model)
  - https://huggingface.co/Skywork/SkyReels-V2-I2V-1.3B-540P
  - *From: Colin*

- **ComfyUI VibeVoiceSelector** (node)
  - https://github.com/pmarmotte2/Comfyui-VibeVoiceSelector
  - *From: AJO*

- **SageAttention installation guide** (guide)
  - https://civitai.com/articles/12848/step-by-step-guide-series-comfyui-installing-sageattention-2
  - *From: voxJT*

- **Video continuation fix workflows** (workflow)
  - https://discord.com/channels/1076117621407223829/1386453178240733235
  - *From: pom*

- **Modified MultiTalk for VACE** (repo)
  - https://github.com/Bwebbfx/ComfyUI-WanVideoWrapper-MtV
  - *From: VRGameDevGirl84(RTX 5090)*

- **Self forcing LoRA for 1.3B** (model)
  - https://civitai.com/models/1585622?modelVersionId=1909719
  - *From: Slavrix*

- **LightX2V update** (repo)
  - https://github.com/ModelTC/lightx2v/commit/9c0a897399a54b659f910d6b7c115ca3857cbb66
  - *From: yi*

- **LoraEdit research paper** (research)
  - https://cjeen.github.io/LoraEditPaper/
  - *From: yo9o*

- **UltraWan model** (model)
  - https://huggingface.co/Alissonerdx/UltraWanComfy
  - *From: Alisson Pereira*

- **UltraVideo dataset** (dataset)
  - https://huggingface.co/datasets/APRIL-AIGC/UltraVideo
  - *From: Alisson Pereira*

- **Modified WanVideoWrapper** (repo)
  - https://github.com/TangoAdorboBG/ComfyUI-WanVideoWrapper
  - *From: Tango Adorbo*

- **ComfyUI-VideoUpscale_WithModel** (repo)
  - https://github.com/ShmuelRonen/ComfyUI-VideoUpscale_WithModel
  - *From: The Shadow (NYC)*

- **ATI model** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/blob/main/Wan2_1-I2V-ATI-14B_fp8_e4m3fn.safetensors
  - *From: Juampab12*

- **MAGREF model** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/blob/main/Wan2_1-Wan-I2V-MAGREF-14B_fp8_e4m3fn.safetensors
  - *From: The Shadow (NYC)*

- **SwapAnyHead paper** (paper)
  - https://humanaigc.github.io/SwapAnyHead/
  - *From: hicho*

- **1x-ReFocus-V3 upscale model** (model)
  - https://openmodeldb.info/models/1x-ReFocus-V3
  - *From: Alisson Pereira*

- **Wan2_1-VACE_module_1_3B_bf16.safetensors** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/blob/main/Wan2_1-VACE_module_1_3B_bf16.safetensors
  - *From: David Snow*

- **360 degree character workflow** (workflow)
  - https://www.youtube.com/watch?v=8DRQenukHhk
  - *From: mdkb*

- **SageAttention update** (repo)
  - https://github.com/thu-ml/SageAttention/commit/d64abd1626ccec3f45681b7583d9cb4221f710db
  - *From: JohnDopamine*

- **RLT training method** (repo)
  - https://github.com/SakanaAI/RLT
  - *From: ZeusZeus (RTX 4090)*

- **DeJPG upscaler model** (model)
  - https://openmodeldb.info/models/1x-DeJPG-realplksr-otf
  - *From: The Shadow (NYC)*

- **SeedVR2 Video Upscaler** (tool)
  - https://github.com/numz/ComfyUI-SeedVR2_VideoUpscaler
  - *From: The Shadow (NYC)*

- **Video Depth Anything vitG model** (model)
  - https://huggingface.co/Nap/depth_anything_v2_vitg/tree/main
  - *From: HeadOfOliver*

- **Kijai WAN VAE** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/blob/main/Wan2_1_VAE_bf16.safetensors
  - *From: garbus*

- **ComfyUI-WarperNodes** (repo)
  - https://github.com/AIWarper/ComfyUI-WarperNodes
  - *From: A.I.Warper*

- **Face Poke expression changer** (tool)
  - https://huggingface.co/spaces/jbilcke-hf/FacePoke
  - *From: JohnDopamine*

- **DepthCrafter** (repo)
  - https://github.com/Tencent/DepthCrafter
  - *From: JohnDopamine*

- **Detail enhancer LoRA V2** (lora)
  - https://civitai.com/models/1683455
  - *From: Alisson Pereira*

- **janky_memory_patcher** (tool)
  - https://github.com/drozbay/janky_memory_patcher
  - *From: TK_999*

- **RealisDance-DiT project** (model)
  - https://thefoxofsky.github.io/project_pages/RealisDance-DiT/index
  - *From: David Snow*

- **Steerable-Motion VideoContinuationGenerator** (tool)
  - https://github.com/banodoco/Steerable-Motion
  - *From: Monster*

- **Christian Sandor's Wan experiments blog** (resource)
  - https://drsandor.net/ai/minecraft/
  - *From: Christian Sandor*

- **VideoNoiseWarp** (tool)
  - https://github.com/kijai/ComfyUI-VideoNoiseWarp
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Spline Path Control** (tool)
  - https://whatdreamscost.github.io/Spline-Path-Control/
  - *From: TK_999*

- **Particle Grid Animator** (tool)
  - https://nathanshipley.github.io/particleGridAnimator/
  - *From: TK_999*

- **Caching nodes** (tool)
  - https://github.com/alastor-666-1933/caching_to_not_waste
  - *From: patientx*

- **Wan LCM Accelerator LoRA** (lora)
  - https://civitai.com/models/1713337?modelVersionId=1938875
  - *From: hicho*

- **UltraWan LoRA** (lora)
  - https://huggingface.co/Alissonerdx/UltraWanComfy/tree/main
  - *From: ▲*

- **UltraWan V2 LoRA** (lora)
  - https://civitai.com/models/1683455
  - *From: Alisson Pereira*

- **Ratatoskr Wan 2.1 I2V** (model)
  - https://civitai.com/models/1713721/ratatoskr-wan-21-i2v-animal-creature-and-furry?modelVersionId=1939308
  - *From: Alisson Pereira*

- **Aether depth model** (repo)
  - https://github.com/OpenRobotLab/Aether
  - *From: samhodge*

- **Radial Attention paper** (repo)
  - https://github.com/mit-han-lab/radial-attention
  - *From: toyxyz*

- **VRGameDevGirl84's upscale workflow** (workflow)
  - https://discord.com/channels/1076117621407223829/1387232079078625389/1387233252250484806
  - *From: VRGameDevGirl84(RTX 5090)*

- **MultiTalk branch** (repo)
  - *From: MilesCorban*

- **Wan14B Audio commit** (repo)
  - https://github.com/ModelTC/lightx2v/commit/bf8976c00abe9ac3b67da7668b55b311b7231af1
  - *From: yi*

- **Self-Forcing VACE Addon** (model)
  - https://huggingface.co/lym00/Wan2.1-T2V-1.3B-Self-Forcing-VACE-Addon-Experiment/tree/main
  - *From: mdkb*

- **Wan14B Detailer/Enhancer T2V** (lora)
  - https://civitai.com/models/1626063/wan14bdetailerenhancert2v
  - *From: mdkb*

- **FLUX Kontext Dev** (model)
  - https://huggingface.co/black-forest-labs/FLUX.1-Kontext-dev
  - *From: A.I.Warper*

- **ComfyUI Kontext workflows** (workflow)
  - https://comfyanonymous.github.io/ComfyUI_examples/flux/#flux-kontext-image-editing-model
  - *From: A.I.Warper*

- **FLUX Kontext GGUF** (model)
  - https://huggingface.co/bullerwins/FLUX.1-Kontext-dev-GGUF
  - *From: DawnII*

- **Radial Attention** (repo)
  - https://github.com/mit-han-lab/radial-attention
  - *From: ZeusZeus (RTX 4090)*

- **DitherDeleter upscaling model** (model)
  - https://openmodeldb.info/models/1x-DitherDeleterV3-Smooth
  - *From: Persoon*

- **LightX2V LoRA** (lora)
  - https://huggingface.co/Kijai/WanVideo_comfy/blob/main/Wan21_T2V_14B_lightx2v_cfg_step_distill_lora_rank32.safetensors
  - *From: David Snow*

- **CausVid LoRA** (lora)
  - https://huggingface.co/Kijai/WanVideo_comfy/blob/main/Wan21_CausVid_14B_T2V_lora_rank32_v1_5_no_first_block.safetensors
  - *From: David Snow*

- **AccVid LoRA** (lora)
  - https://huggingface.co/Kijai/WanVideo_comfy/blob/main/Wan21_AccVid_T2V_14B_lora_rank32_fp16.safetensors
  - *From: David Snow*

- **FusionX workflows** (workflow)
  - https://civitai.com/models/1683455
  - *From: David Snow*

- **MiniMax remover model** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/blob/main/Wan2_1-MiniMaxRemover_1_3B_fp16.safetensors
  - *From: samhodge*

- **Benji Futurethinker MiniMax workflow** (workflow)
  - https://www.youtube.com/watch?v=KqkdKtx91SM
  - *From: mdkb*

- **Soundly audio library** (tool)
  - https://getsoundly.com/
  - *From: Jonathan*

- **Wan21_CausVid_14B_T2V_lora_rank32_v2.safetensors** (lora)
  - https://huggingface.co/Kijai/WanVideo_comfy/blob/main/Wan21_CausVid_14B_T2V_lora_rank32_v2.safetensors
  - *From: David Snow*

- **Endless travel workflow with loras** (workflow)
  - https://discord.com/channels/1076117621407223829/1386453178240733235/1388166825459585207
  - *From: VRGameDevGirl84(RTX 5090)*

- **Spline Path Control editor** (tool)
  - https://editor.p5js.org/whatdreamscost/full/R02ht0HqI
  - *From: Jonathan*

- **Spline Path Control v2.3** (tool)
  - https://whatdreamscost.github.io/Spline-Path-Control/
  - *From: Jonathan*

- **Spline Path Control GitHub** (repo)
  - https://github.com/WhatDreamsCost/Spline-Path-Control
  - *From: Jonathan*

- **Wan2.1_T2V_14B_LightX2V_StepCfgDistill_VACE-GGUF** (model)
  - https://huggingface.co/lym00/Wan2.1_T2V_14B_LightX2V_StepCfgDistill_VACE-GGUF
  - *From: Jonathan*

- **Wan2.1-VACE-14B-fp8** (model)
  - https://huggingface.co/Kamikaze-88/Wan2.1-VACE-14B-fp8/tree/main
  - *From: Faust-SiN*

- **Remade-AI camera LoRAs** (lora)
  - https://huggingface.co/Remade-AI
  - *From: mdkb*

- **Quick connections for wire styling** (tool)
  - https://github.com/niknah/quick-connections
  - *From: Valle*

- **OpenMuse AI** (resource)
  - https://openmuse.ai/
  - *From: ˗ˏˋ⚡ˎˊ-*

- **WanVideo I2I Expression Changer** (lora)
  - https://civitai.com/models/1421989/wanvideo-i2i-480p-expression-changer-perspective-changer
  - *From: Juampab12*

- **Wan2.1_T2V_14B_LightX2V_StepCfgDistill_VACE** (model)
  - https://huggingface.co/lym00/Wan2.1_T2V_14B_LightX2V_StepCfgDistill_VACE/tree/main
  - *From: hicho*

- **UltraWan 1K ComfyUI** (lora)
  - https://huggingface.co/Alissonerdx/UltraWanComfy/blob/main/ultrawan_1k_comfy.safetensors
  - *From: hicho*

- **Self-forcing VACE FP16** (model)
  - https://huggingface.co/lym00/Wan2.1_T2V_1.3B_SelfForcing_VACE/tree/main
  - *From: mdkb*

- **NAG paper** (paper)
  - https://huggingface.co/papers/2505.21179
  - *From: Benjimon*

- **LoRAEdit technique** (paper)
  - https://cjeen.github.io/LoraEditPaper/
  - *From: phazei*

- **One-click dataset creator** (workflow)
  - https://discord.com/channels/1076117621407223829/1388930627931340820
  - *From: burgstall*

- **ThinkSound paper** (paper)
  - https://arxiv.org/html/2506.21448v1
  - *From: ZeusZeus (RTX 4090)*

- **Hunyuan 3D 2.1** (tool)
  - https://huggingface.co/spaces/tencent/Hunyuan3D-2.1
  - *From: Charlie*

- **Wan2.1_14B_VACE-GGUF Q8 version** (model)
  - https://huggingface.co/QuantStack/Wan2.1_14B_VACE-GGUF/tree/main
  - *From: David Snow*

- **ComfyUI-MultiGPU pack** (repo)
  - https://github.com/pollockjj/ComfyUI-MultiGPU
  - *From: David Snow*

- **Spline Path Control workflows** (workflow)
  - https://github.com/WhatDreamsCost/Spline-Path-Control/tree/main/example_workflows
  - *From: Kba-Notes*

- **Skibidi-SageAttention2plus mirror** (repo)
  - https://github.com/Many0therFunctions/Skibidi-SageAttention2plus
  - *From: MysteryShack*

- **Execution inversion demo for loops** (repo)
  - https://github.com/BadCafeCode/execution-inversion-demo-comfyui
  - *From: ˗ˏˋ⚡ˎˊ-*

- **ComfyUI-Speaker-Isolation** (repo)
  - https://github.com/pmarmotte2/ComfyUI-Speaker-Isolation.git
  - *From: manu_le_surikhate_gamer*

- **NSFW Wan 14B model** (model)
  - https://huggingface.co/NSFW-API/NSFW_Wan_14b
  - *From: MisterMango*

- **Radial Attention paper** (repo)
  - https://www.arxiv.org/abs/2506.19852
  - *From: yo9o*

- **SageAttention2 wheels** (tool)
  - https://wheels.melmassadian.com/sageattention
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Fusion X Ingredients workflow** (workflow)
  - https://civitai.com/models/1690979
  - *From: VRGameDevGirl84*

- **ControlFlowUtils** (tool)
  - https://github.com/VykosX/ControlFlowUtils
  - *From: ˗ˏˋ⚡ˎˊ-*

- **MultiTalk VACE compatibility fork** (repo)
  - https://github.com/Rudra-ai-coder/ComfyUI-WanVideoWrapper
  - *From: ˗ˏˋ⚡ˎˊ-*

- **WanVideoWrapper MultiTalk branch** (repo)
  - https://github.com/kijai/ComfyUI-WanVideoWrapper/tree/multitalk
  - *From: ˗ˏˋ⚡ˎˊ-*


## Known Limitations

- **AccVid has negative effects on stylized outputs**
  - While it may work for people, it significantly degrades stylized video generation
  - *From: Kijai*

- **CFG 1 prevents use of negative prompts**
  - With CFG set to 1, negative prompts cannot be used which limits control
  - *From: Persoon*

- **Context window changes cause inconsistencies**
  - Random differences between video sections including clothing, hair, and pose changes across sliding context windows
  - *From: Ruairi Robinson*

- **Kontext relighting quality**
  - Poor relighting compared to ICLight, only gets colors but doesn't create proper rim lighting
  - *From: Nekodificador*

- **Kontext control limitations**
  - Works entirely based on prompt, lacks mask and ControlNet control compared to traditional inpainting
  - *From: Nekodificador*

- **High MPS strength issues**
  - Setting MPS strength over 0.5 may cause it to stop following preprocessors
  - *From: DeZoomer*

- **Motion blur baked into stylized models**
  - High contrast detail in small areas suffers from motion blur, especially hands at distance
  - *From: Piblarg*

- **Facial hair interferes with mouth detection**
  - Goatee and low resolution make mouth movement detection unreliable
  - *From: A.I.Warper*

- **VACE encoder strength inheritance**
  - Setting later encoders to lower strength affects all previous encoders in the chain
  - *From: Neex*

- **Normal Crafter mouth movement range**
  - Works great for close-ups and exaggerated movements but fails on far away shots
  - *From: VRGameDevGirl84(RTX 5090)*

- **AccVid doesn't help much with stylized outputs**
  - Limited benefit observed for stylized content
  - *From: Piblarg*

- **Pattern handling issues**
  - Wan commonly produces jitter with difficult patterns, especially at lower resolutions
  - *From: Valle*

- **GGUF performance with LoRAs**
  - GGUF is slower and every LoRA added increases memory use and slows it down since LoRAs can't be merged on the fly
  - *From: Kijai*

- **540p VACE model artifacts**
  - 540p model shows box artifacts around subjects when pushed beyond 81 frames or at higher resolutions
  - *From: Zuko*

- **ATI trajectory editor missing code**
  - Official ATI repo is missing index.html file, making the trajectory editor non-functional
  - *From: Juampab12*

- **DWPose tracking fails on complex spinning motions**
  - Simple character spin is enough to break pose detection in fight scenes
  - *From: David Snow*

- **HPS LoRA overrides other LoRAs**
  - Makes faces look artificial with default Flux face appearance
  - *From: David Snow*

- **VACE produces artifacts when reference doesn't match input structure**
  - Blue artifacts appear when reference image structure differs from input video
  - *From: VRGameDevGirl84(RTX 5090)*

- **Sapiens pose detection struggles with complex poses**
  - Fingers detection is inaccurate, not much better than existing solutions
  - *From: David Snow*

- **ATI trajectory system has point allocation limits**
  - Too many points for allocated timeframe causes errors
  - *From: Juampab12*

- **ATI only works with 81 frames**
  - Hardcoded limitation in original implementation
  - *From: Kijai*

- **ATI shows green hue when failing**
  - Indicates parameter conflicts or model failure
  - *From: TK_999*

- **Motion LoRAs may overfit with distillation**
  - Specific motion LoRAs struggle to expand beyond trained motion with CausVid/AccVid
  - *From: DevouredBeef*

- **Sapiens models locked to single resolution**
  - Portrait resolution only, limits usefulness
  - *From: Kijai*

- **FlowMo doubles inference time**
  - Improvement comes at cost of significantly slower generation
  - *From: yi*

- **AccVid I2V terrible on non-photoreal content**
  - Works on photoreal but fails on stylized or non-photorealistic content
  - *From: Kijai*

- **Uni3C limited to 49 frames**
  - Current implementation restricted to specific frame count
  - *From: Valle*

- **VACE designed for T2V workflow**
  - Has its own start frame process, not optimized for I2V usage
  - *From: Piblarg*

- **Stacking LoRAs reduces face resemblance**
  - Multiple motion LoRAs hurt facial consistency, especially on human subjects
  - *From: Jonathan*

- **High resolution loses coherence on non-static scenes**
  - 1536x1024 generation works for static scenes but may fail on dynamic content due to training resolution
  - *From: mamad8*

- **LoRA merging constraints**
  - Cannot merge LoRAs that target different transformer layers - they don't stack and won't show combined effects unless merged into base model
  - *From: VRGameDevGirl84(RTX 5090)*

- **AccVid overcooking at higher steps**
  - At higher steps AccVid will overcook the video, even raising steps from 2 to 4 at high strength overcooks colors significantly
  - *From: Jonathan*

- **Motion LoRAs still limited**
  - AccVid still confines motion to only the specific context of the lora
  - *From: DevouredBeef*

- **VACE mask halo effects**
  - Soft fringe around masked objects due to mask expansion/blurring, inconsistent occurrence with unclear rules
  - *From: Ruairi Robinson*

- **TeaCache limited effectiveness with distilled models**
  - Won't work as intended especially when using coefficients on distilled model, hard to configure meaningfully at low steps
  - *From: Kijai*

- **ATI only works with 81 frames**
  - Fixed frame count requirement for Animated Track Interpolation
  - *From: Juampab12*

- **CFG scheduling performance impact**
  - Goes from 143 seconds to 1400 seconds when using CFG schedule due to VRAM usage
  - *From: Juan Gea*

- **Regular Wan model doesn't work with trajectory control**
  - Need ATI model specifically for trajectory control features
  - *From: Juampab12*

- **High AccVid strength only works at low steps**
  - Higher steps make videos look overcooked with high AccVid values
  - *From: Jonathan*

- **Riflex extension can be glitchy**
  - Frame extension using riflex has inconsistent results
  - *From: TK_999*

- **VAE resolution limit**
  - VAE can only see so many pixels, probably diminishing returns above 720p
  - *From: MilesCorban*

- **Quality of motion gets messed up with longer than 6-8s videos**
  - Current limitation with longer video generation
  - *From: The Punisher*

- **4K video generation is way too expensive in VRAM terms**
  - Would need like 400gb or so for 4K
  - *From: The Punisher*

- **Stretching and distorted results at 1080p without proper training**
  - Everything is stretched and out of place because it tries to fill funny
  - *From: Thom293*

- **High resolution requires longer processing time and slows down motion**
  - High res takes 5x longer and drastically slows down motion (CausVid amplifies this)
  - *From: MilesCorban*

- **ATI frame/spline point restrictions**
  - Currently only works with 121 points/81 frames, doesn't work with context yet
  - *From: Kijai*

- **CausVid v2 hair issues**
  - v2 breaks hair rendering, making it look stringy and fall apart
  - *From: Thom293*

- **Side bars at certain resolutions**
  - Even at suggested resolutions, side bars can occur, less often with 3:4 or 9:16 ratios
  - *From: ▲*

- **Context beyond 81/121 frames not currently supported**
  - Kijai hasn't implemented the splitting code yet for longer sequences
  - *From: Kijai*

- **Cannot change CFG from 1 when using certain merged models**
  - Some merged models with CausVid built-in don't allow CFG changes
  - *From: VRGameDevGirl84(RTX 5090)*

- **VACE + Uni3C compatibility issues**
  - User got errors when trying to use both together
  - *From: Juan Gea*

- **Background movement limited with depth control**
  - Depth control can make backgrounds static, affects far background capture
  - *From: A.I.Warper*

- **Normal maps too strong for most use cases**
  - Using normals as control results in weird hybrid creatures
  - *From: A.I.Warper*

- **Shift behavior is inconsistent and seed-dependent**
  - No universal shift formula works - results vary randomly between generations even with same settings
  - *From: Jonathan*

- **Low resolution video segmentation unreliable**
  - Mouth segmentation fails on low-res videos, requiring alternative approaches like pose landmarks
  - *From: A.I.Warper*

- **Hair rendering issues with certain configurations**
  - Persistent hair artifacts appear with specific shift/step combinations, may be related to GGUF quantization
  - *From: The Punisher*

- **VACE can only handle single reference image**
  - Cannot process multiple reference images natively
  - *From: Kijai*

- **Phantom 3D prints cars when same image used in all encoders**
  - Using identical images in all inputs creates unrealistic 3D effect
  - *From: ingi // SYSTMS*

- **Phantom changes intended camera movements**
  - Can change sideways walk cycles to forward movement even with controls
  - *From: ingi // SYSTMS*

- **5-step generation causes artifacts**
  - Consistently produces weird distortion effects, even steps work better
  - *From: The Punisher*

- **GGUF models don't support VACE addon in native ComfyUI**
  - Kijai's wrapper won't support GGUFs and native with GGUFs doesn't support VACE addon
  - *From: The Punisher*

- **Odd step counts cause glitches with shift**
  - Steps 3,5,7 have issues with hair becoming noisy mess, motion gets affected with high shift - birds stop flapping
  - *From: The Punisher*

- **Model timeline complexity limitations**
  - Complex timelines might need retries as model likely wasn't trained with complex timeline scheduling
  - *From: Juampab12*

- **LoRAs don't work as well with Phantom**
  - LoRAs work but with reduced effectiveness compared to standard WAN models
  - *From: Thom293*

- **Uni3c completely ignores camera input**
  - Camera movement controls are not working with uni3c model
  - *From: Dream Making*

- **Flowmatch scheduler disables shift in Phantom**
  - Using Flowmatch_Causvid in Phantom produces bad results and disables shift functionality
  - *From: VRGameDevGirl84(RTX 5090)*

- **Wrapper requires full model reload for lora changes**
  - Any change to loras or pre-model loader nodes requires complete model reload, taking 2-10 minutes
  - *From: the_darkwatarus_museum*

- **FP32 configuration limits frame count due to VRAM constraints**
  - Limited to 48 frames (or 64) at 720p with 24GB VRAM when using fp32
  - *From: Juan Gea*

- **Models like ATI can only run with 81 frames maximum**
  - Restriction for certain control models
  - *From: Nekodificador*

- **VACE only processes first reference frame from batch**
  - Multiple reference frames are ignored, only first is used
  - *From: Piblarg*

- **Reference images combined with phantom embeds produce strong flashes**
  - Known issue when combining these features
  - *From: David Snow*

- **T2V not good for unusual or precise requirements**
  - Works for typical content but struggles with unusual or very specific prompts
  - *From: N0NSens*

- **Native Wan doesn't support SkyReels layers**
  - Feature limitation in native implementation
  - *From: hicho*

- **Multiple images in VACE blend rather than process separately**
  - Chaining multiple encode nodes results in blending of various inputs rather than unique processing
  - *From: Piblarg*

- **Cannot mix VACE reference frame with Phantom**
  - Compatibility issue between the two control methods
  - *From: Piblarg*

- **Hair artifacts at low steps with movement**
  - Wind blown hair and fine details show patterning artifacts, especially with high movement
  - *From: Thom293*

- **ATI hardcoded to 80 frames maximum**
  - Uni3C can go beyond but ATI has restriction built in
  - *From: Guey.KhalaMari*

- **Self-forcing only works with 1.3B T2V model**
  - Cannot be used with 14B variant, scaling to 14B would be very difficult
  - *From: MilesCorban*

- **Real-time generation not achievable with self-forcing**
  - Even at 512px resolution needs 1.3+ seconds per frame, maximum practical rate is 6fps
  - *From: slmonker*

- **Self-forcing has restrictive license**
  - License terms are problematic for commercial use
  - *From: Kijai*

- **Screen door artifacts persist in high-frequency areas**
  - Appears in foliage, hair, and fine details especially with movement, may be fundamental model limitation
  - *From: multiple users*

- **Self-forcing not optimal for videos beyond 5 seconds**
  - Model trained on 5sec at 16fps, performance degrades beyond this length
  - *From: JohnDopamine*

- **Self-Forcing doesn't work with WAN LoRAs**
  - Jonathan reports WAN LoRAs don't work with Self-Forcing models, though 1.3B LoRAs do work
  - *From: Jonathan*

- **Self-Forcing has poor prompt adherence**
  - N0NSens demonstrates near-zero prompt following in I2V mode
  - *From: N0NSens*

- **Self-Forcing has hallucination issues**
  - hicho notes it has more hallucination compared to regular WAN models
  - *From: hicho*

- **CausVid and Self-Forcing not properly supported in ComfyUI**
  - Kijai clarifies people are sampling the models wrong - they work but not as intended
  - *From: Kijai*

- **SLG kills motion in videos**
  - crinklypaper demonstrates SLG parameter reduces video motion significantly
  - *From: crinklypaper*

- **Self-forcing autoregressive sampling not supported**
  - ComfyUI can use weights but not the proper autoregressive sampling with kv_cache
  - *From: Kijai*

- **Self-forcing probably won't work with VACE**
  - Would need new sampler node, wouldn't be compatible with VACE
  - *From: Kijai*

- **MultiTalk won't be added to WanVideoWrapper**
  - Confirmed by Kijai that it's not planned
  - *From: Kijai*

- **LoRAs don't work as well with Phantom**
  - Phantom's character pasting approach interferes with LoRA effectiveness
  - *From: Piblarg*

- **14B ControlNets aren't great quality**
  - Not widely used after initial release, mediocre results
  - *From: David Snow*

- **VACE causes instability over time**
  - Adding noise makes generation unstable over longer sequences
  - *From: chrisd0073*

- **VACE wants to place reference where located in test image**
  - Has issues combining with control inputs or style loras, works best alone
  - *From: Piblarg*

- **Context window inconsistency**
  - Difficult to maintain consistency between sections, changes details like clothing between context windows
  - *From: Ruairi Robinson*

- **FantasyTalking and Phantom cannot run simultaneously**
  - FantasyTalking is I2V, Phantom is T2V - incompatible for simultaneous use
  - *From: Kijai*

- **MultiTalk requires 48GB VRAM**
  - Even with offloading, still needs 48GB VRAM making it inaccessible for most users
  - *From: Cubey*

- **Self-forcing model only works with 1.3b loras**
  - Cannot use other lora types with the self-forcing fast model
  - *From: patientx*

- **AccVid has detrimental effect on non-realistic outputs**
  - Would never use accvid due to negative impact on non-realistic content
  - *From: Kijai*

- **ATI precision errors with complicated trajectories**
  - Loses consistency halfway through complex movements like backflips
  - *From: Juampab12*

- **VACE video control doesn't follow reliably**
  - Even with strength 1 doesn't follow the video very well sometimes, especially with openpose
  - *From: JmySff*

- **Model merges presented as new models cause confusion**
  - Complicates things when you don't really know what's going on, creates support requests for 'new' models that are just base + loras
  - *From: Kijai*

- **MagCache patches break other patches**
  - Patches over forward method breaking every other patch that does the same, doesn't support VACE initially
  - *From: Kijai*

- **VACE color shift in extensions**
  - Color shifts occur at frame boundaries when extending videos, becomes worse with each extension
  - *From: Simonj*

- **MagCache default values don't work**
  - Default threshold values are too high, need 10x lower values to function properly
  - *From: Kijai*

- **Context options crash with <81 frames**
  - Using context options on videos with fewer than 81 frames causes crashes
  - *From: DeZoomer*

- **Flux kontext throws NSFW frequently**
  - Flux kontext model often triggers NSFW filters inappropriately
  - *From: A.I.Warper*

- **Set/Get nodes don't work with group nodes**
  - Group nodes cause LoRAs to be ignored when using set/get node system
  - *From: MatiaHeron*

- **Phantom degrades native WAN2.1 quality**
  - Similar settings produce lower quality compared to base WAN2.1
  - *From: Fawks*

- **Phantom LoRA extraction unsuccessful**
  - Initial attempts to extract Phantom as LoRA were not successful
  - *From: Kijai*

- **TeaCache with CausVid and low steps causes issues**
  - Potentially causes mistakes and doesn't provide meaningful improvement
  - *From: Kijai*

- **NAG in ATI seems to worsen results**
  - Testing showed degraded quality when using NAG with ATI
  - *From: Juampab12*

- **Self-forcing model doesn't work well with CausVid**
  - No matter what strength used, avoid combining them
  - *From: Jonathan*

- **Steps higher than 8 cause oversaturation in self-forcing model**
  - Will begin to over saturate/contrast the output and stray from reference in i2v
  - *From: Jonathan*

- **MagCache brutalizes video quality**
  - Significant quality degradation observed, especially at lower step counts like 6
  - *From: David Snow*

- **Phantom may struggle with non-realistic reference images**
  - Inconsistent performance with stylized or non-photographic inputs
  - *From: Piblarg*

- **Reference images can be hit or miss with VACE**
  - Inconsistent adherence to reference images in VACE workflows
  - *From: David Snow*

- **Mouth movement issues across all models**
  - Persistent challenge with lip-sync and facial animation, no universal solution
  - *From: David Snow*

- **Causal sampling quality issues**
  - KV cache may not be great for quality, looks like crap at 3 steps and overcooked at 9 steps
  - *From: Kijai*

- **Wan alters subject body proportions**
  - User asking if there's way to prevent this alteration
  - *From: TheRealDude*

- **VACE makes model appear skinnier**
  - Consistently changes body proportions despite user preference
  - *From: TheRealDude*

- **Sage2 will only work on 50 series GPUs**
  - Hardware limitation for upcoming speed improvements
  - *From: Jonathan*

- **VEO3 won't generate majority of prompts**
  - Heavily censored, image to video won't have audio
  - *From: MysteryShack*

- **MPS not suitable for i2v models**
  - Causes instant deviation from input image, especially noticeable on closeups
  - *From: ▲*

- **1.3B not good enough for 14B cleanup**
  - Destroys fine detail when used as second pass on 14B generated videos
  - *From: David Snow*

- **Quality degradation with chained samplers**
  - More samplers in sequence lead to quality degradation as each uses previous results
  - *From: the_darkwatarus_museum*

- **Color mismatch in VACE looping**
  - Well documented issue with no clear solution, loop segment has color mismatch
  - *From: Piblarg*

- **NAG corrupts output with self-forcing models**
  - Weird corruption occurs when combining NAG with new self-forcing models
  - *From: jacinda*

- **Long context reduces prompt adherence**
  - Around 250-300 frames, model stops following prompts effectively
  - *From: Gateway {Dreaming Computers}*

- **SeedVR requires 80GB VRAM for 720P**
  - Model is small but still needs massive VRAM, offloading wouldn't help much
  - *From: Kijai*

- **Ultimate SD upscale works but creates flash artifacts**
  - Clears up most shimmer but flash remains, see black parts of shoe
  - *From: David Snow*

- **Current upscaling methods not satisfying**
  - Tested every variation (ADiff, video upscaling by model, WAN Low Noise V2V, LTXV) - improvements but overall not satisfying
  - *From: uff*

- **Context windows don't work well with start frame**
  - New start frame doesn't exist for next clip, also slower and not consistent without control
  - *From: Kijai*

- **Wan image generation quality**
  - The images wan generates are not that good
  - *From: Juampab12*

- **AnimateDiff bad for video upscaling**
  - Tested extensively - amazing for creativity/change but opposite of what you want for upscaling
  - *From: David Snow*

- **UniPC cannot separate camera and object movement**
  - When using UniPC scheduler, both camera and objects move together - cannot isolate object movement only
  - *From: N0NSens*

- **LightX2V overcooks at higher step counts**
  - Using more than 4-5 steps with LightX2V results in overcooked, degraded output quality
  - *From: Kijai*

- **Depth LoRA for 1.3B doesn't generalize well to 14B**
  - The depth LoRA works amazingly for 1.3B but badly generalized and doesn't work with most inputs on 14B
  - *From: Kijai*

- **MAGREF couldn't work as LoRA**
  - Attempts to convert MAGREF to LoRA format failed completely
  - *From: Kijai*

- **MAGREF has no VACE support**
  - Downside of MAGREF is no VACE compatibility
  - *From: Kijai*

- **CFG scheduling doesn't work with self-force**
  - None of the CFG stuff will work with self-force acceleration
  - *From: Kijai*

- **Context windows don't work well with MAGREF**
  - MAGREF doesn't play so well with context windows
  - *From: Kijai*

- **Negative prompts don't work with CFG 1**
  - At CFG 1 for accelerated workflows, negative prompts don't work well or at all
  - *From: blake37*

- **MAGREF doesn't work well with start/end frame approach**
  - Testing start/end frame with MAGREF didn't really work
  - *From: Kijai*

- **MAGREF inconsistent results**
  - Turns out to be either a mess or something completely different from what is prompted
  - *From: N0NSens*

- **LatentSync crashes with partial face frames**
  - Can't cope with frames where face is not 100% in view and crashes the whole workflow wasting 30 minutes
  - *From: AJO*

- **MAGREF poor with double character references**
  - Not so friendly to double characters reference
  - *From: slmonker(5090D 32GB)*

- **Minimax Remover quality degrades at higher resolutions**
  - Looks awkward at higher resolutions, works better at lower res
  - *From: toyxyz*

- **Native Wan + LightX2V poor prompt adherence**
  - Pretty poor prompt adherence compared to wrapper with NAG
  - *From: jacinda*

- **Phantom talking issue**
  - Characters generated with Phantom tend to have open mouths as if talking/explaining, needs quiet people training data
  - *From: Thom293*

- **MagRef inflexibility**
  - Struggles with multiple reference images of same character and changing outfits/hairstyles
  - *From: David Snow*

- **ATI hardcoded to 81 frames**
  - Cannot use ATI with less than 81 frames, it's hardcoded
  - *From: Kijai*

- **MultiTalk 3D style requirement**
  - Works with 3D styles but worse with flat/2D styles
  - *From: Kijai*

- **Context windows only work with tight motion control**
  - Cross fades occur at transition points, especially with speed LoRAs
  - *From: Kijai*

- **MultiTalk loses expressiveness beyond 81 frames**
  - Forcing 177 frames makes results worse
  - *From: Kijai*

- **SLG with LightX2V turns into baked ultra-nightmare**
  - Counterintuitive as SLG boosts CFG while LightX2V is CFG distilled
  - *From: jacinda*

- **VACE adds unwanted subjects in human-shaped masks**
  - Shape of mask influences model assumptions about content
  - *From: BEE*

- **Phantom amplifies artifacts along with desired features**
  - Everything gets amplified including unwanted elements, needs to be used at low percentages
  - *From: ▲*

- **VACE gets distracted by shadows easily**
  - Annoying when trying to replace characters while keeping the rest of the scene intact
  - *From: Valle*

- **Context windows with I2V cause reference frame reapplication**
  - Every context reset reapplies the reference frame causing jumps
  - *From: Nekodificador*

- **All depth tools miss distant background objects**
  - Black values are too high for distant objects
  - *From: A.I.Warper*

- **Multitalk becomes overly expressive**
  - Default settings can produce exaggerated lip sync movements
  - *From: CJ*

- **Camera movement breaks multitalk contexting**
  - Moving cameras disrupt lip sync quality and consistency
  - *From: Kijai*

- **Context windows inefficient for long generations**
  - Very inefficient processing method, takes much longer than latent method
  - *From: Kijai*

- **Uni3c dampens all motion**
  - When used for camera control, it affects both camera and in-frame movement
  - *From: N0NSens*

- **Performance degrades past 81 frames without context**
  - Quality drops when generating longer videos without context windows
  - *From: Kijai*

- **UltraWan LoRA has CC4 non-commercial license**
  - Due to dataset being taken from YouTube, limits commercial use
  - *From: Kijai*

- **1.3B model not trained on high quality dataset**
  - Requires additional LoRAs like MPS, HPS, Self Forcing to achieve good results
  - *From: yi*

- **MultiTalk language support limited**
  - Spanish doesn't work well, seems to be primarily trained on specific languages
  - *From: Juampab12*

- **8GB VRAM insufficient for newer models**
  - AI has moved beyond 8GB cards, need 24GB+ for latest features
  - *From: JohnDopamine*

- **MultiTalk language support limited**
  - Works well with English and Chinese, poor with Spanish, French seems to work
  - *From: Juampab12*

- **Long context videos become repetitive**
  - Motions seem repetitive at 2000+ frames, model only trained with 81 frame chunks
  - *From: Kijai*

- **Uni3c reduces video expressiveness**
  - Even at low strength, significantly reduces facial expressions and movement
  - *From: Guey.KhalaMari*

- **Camera embeds not implemented**
  - Camera control features not yet available in current implementation
  - *From: Kijai*

- **Two person chat not available yet**
  - Requires feature masking functionality that hasn't been implemented
  - *From: Kijai*

- **MultiTalk doesn't work well with animals**
  - Testing shows it 'works' but gets quite confused with non-human subjects
  - *From: Kijai*

- **Closed source tools can't handle laughter**
  - Hedra and other tools intentionally mute audio during laughter due to technical issues
  - *From: A.I.Warper*

- **MMAudio adds unwanted vocal sounds**
  - Generates 'mumbly asmr vocal noises' and background voices even with negative prompts
  - *From: AJO*

- **Frame count limitations for OOM**
  - Users hitting OOM errors above 500 frames on WAN encoder, though some report success at 2k frames
  - *From: A.I.Warper*

- **Multi-speaker needs additional coding**
  - Multiple faces in image needs more code added and subject masking
  - *From: Kijai*

- **UltraWan 4k LoRA not working**
  - Causes black output, only 1k variant works properly
  - *From: VRGameDevGirl84*

- **Frame count limits for lipsync**
  - Cannot exceed 69 frames with 41 context without breaking lipsync consistency
  - *From: ZRNR*

- **High frame count causes flash**
  - More than 81 frames causes strange flash at video start
  - *From: VRGameDevGirl84*

- **UltraWan LoRA requires T2V model**
  - Gives key errors when used with I2V models, needs T2V base model
  - *From: Alisson Pereira*

- **NAG conflicts with some LoRAs**
  - LoRAs that modify CFG behavior can fight with NAG since both affect guidance
  - *From: JohnDopamine*

- **NAG changes entire composition**
  - Cannot isolate changes to specific elements like hair color - affects lighting, mood, background due to conceptual associations
  - *From: VRGameDevGirl84(RTX 5090)*

- **SeedVR2 VideoUpscaler extremely slow**
  - Takes 10 minutes for 1 second of video on 4090, uses 90GB VRAM
  - *From: burgstall*

- **UltraWan 4k LoRA produces poor results**
  - Duplicates objects and produces garbage output
  - *From: Alisson Pereira*

- **MagRef needs update**
  - Developers acknowledge need for more diverse dataset to improve quality
  - *From: JohnDopamine*

- **Frame rate mismatches in MultiTalk**
  - Chinese-wav2vec2-base at 16fps, MagRef at 15fps, MultiTalk node at 25fps causes sync issues
  - *From: Guey.KhalaMari*

- **Context exponential scaling**
  - Context window processing becomes exponentially more expensive with length
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Flux face persists despite NAG**
  - Chin dimples and cleft chins difficult to remove completely, NAG only works for specific seeds
  - *From: Guey.KhalaMari*

- **Context windows cause visual jumps every 81 frames in I2V**
  - I2V with context sends first frame repeatedly to each context window, causing jarring transitions
  - *From: Nekodificador*

- **I2V incompatible with context options when using Uni3C**
  - I2V with context sends first frame in loop which breaks Uni3C camera control
  - *From: Nekodificador*

- **Manual I2V context system produces inconsistent movement**
  - Using last frame as first for next window works but movement becomes inconsistent as model can't know frame origin
  - *From: Nekodificador*

- **Progressive reference frame system produces noise/negative frames**
  - Attempted solution for context continuity resulted in corrupted diffusion process with plain noise and negative effect frames
  - *From: AJO*

- **LightX LoRA doesn't work on 1.3B**
  - Only works with 14B model
  - *From: VRGameDevGirl84(RTX 5090)*

- **Context options break video-to-video workflow**
  - Cannot use context options when doing video-to-video generation
  - *From: VRGameDevGirl84(RTX 5090)*

- **Long videos cause OOM even on RTX 5090**
  - 10 second videos too long for smaller model
  - *From: orabazes*

- **MultiTalk fps limited to 60**
  - Node doesn't support framerates higher than 60fps
  - *From: patientx*

- **Chatterbox can't do singing voice conversion**
  - Unlike RVC, cannot convert talking voice to singing
  - *From: MysteryShack*

- **1.3B model poor at prompt following in I2V**
  - Doesn't follow prompts well, better suited for VACE and Phantom only
  - *From: hicho*

- **Subject consistency lost at high denoise**
  - At denoise 1.0, original subject changes significantly in upscaling
  - *From: voxJT*

- **Memory usage increases non-linearly with frames**
  - Each additional frame must compute attention with every other frame
  - *From: Draken*

- **VACE and MultiTalk not compatible**
  - VACE is T2V, MultiTalk is I2V - requires code modification
  - *From: Juampab12*

- **VACE and MultiTalk layer competition**
  - They compete a bit and can interfere with each other, better sync results from T2V than when using both together
  - *From: Tango Adorbo*

- **UltraWan 4k generation bugged**
  - 4k generation with UltraWan has issues/bugs
  - *From: Alisson Pereira*

- **Camera movement with MultiTalk context**
  - Any camera movement gets trimmed and glitchy when using context options with MultiTalk
  - *From: N0NSens*

- **Fun Camera Control instability**
  - Fun camera control is unstable, may break input image and switch to T2V with lots of frames, requires lots of VRAM
  - *From: N0NSens*

- **Compute capability requirement**
  - torch._scaled_mm requires CUDA devices with compute capability >= 9.0 or 8.9, blocking RTX A5000 (8.6) usage
  - *From: Slavrix*

- **MultiTalk cannot process 3+ minute audio in one generation**
  - Even with context windowing, 3min audio OOMs on 24GB VRAM at 352x480 resolution
  - *From: burgstall*

- **uni3C doesn't work properly with context over 81 frames**
  - Works for 81 frames but has problems beyond that length
  - *From: N0NSens*

- **Chinese encoder recognition issues**
  - MultiTalk doesn't recognize all English words due to Chinese encoder
  - *From: Charlie*

- **ControlNet maps can bleed into generation**
  - Control maps sometimes bleed into the generation, needs better controlnet type selection
  - *From: Nekodificador*

- **Character turning difficulty**
  - Hard to make characters turn away from camera, always faces camera
  - *From: Nekodificador*

- **Uni3C frame count restriction**
  - Cannot process more than 81 frames regardless of context window settings
  - *From: burgstall*

- **Normal maps color bleeding**
  - Sometimes normal maps can color the output like a normal map instead of just providing structure
  - *From: Neex*

- **VACE masking complexity**
  - Multiple mask inputs make it confusing to understand which activates diff diff functionality
  - *From: A.I.Warper*

- **Character consistency outside trained scene**
  - VACE-generated characters may not maintain consistency when moved to different scenes
  - *From: voxJT*

- **Native VRAM offloading issues**
  - Native implementation has odd VRAM offloading that can max out 128GB system RAM
  - *From: JohnDopamine*

- **UltraWan 4k LoRA not great**
  - 4k version doesn't perform as well as 1k version
  - *From: David Snow*

- **OG2 implementation causes blown out images**
  - No matter what settings used, consistently got blown out images
  - *From: blake37*

- **Multitalk with VACE less accurate**
  - Works but isn't as accurate as when multitalk is run alone
  - *From: Tango Adorbo*

- **ATI quants don't work with native ATI node**
  - FP8 model extremely slow, need workaround for quant versions
  - *From: Jonathan*

- **Uni3C doesn't work with context windows**
  - Trained on I2V only, won't work with seamless workflows that require context windows
  - *From: AshmoTV*

- **VACE controlnet not effective for v2v workflows**
  - Control strength adjustments are minuscule and results are often just different videos rather than controlled modifications
  - *From: Zlikwid*

- **VACE doesn't work with context extension**
  - VACE competes with context extension - they don't work together effectively
  - *From: Tango Adorbo*

- **Denoise above 0.8 creates random videos**
  - Higher denoise values lose connection to input video and generate unrelated content
  - *From: VRGameDevGirl84(RTX 5090)*

- **MultiTalk moves whole body**
  - No way to mask specific people, MultiTalk moves the whole body. Would need to create new video with only target person, then composite
  - *From: Juampab12*

- **Uni3C doesn't support context**
  - Major limitation for now preventing use with longer sequences
  - *From: ˗ˏˋ⚡ˎˊ-*

- **LoRA cross-compatibility issues**
  - 1.3B and 14B LoRAs can't transfer, 14B LoRAs will silently fail on 1.3B models
  - *From: Draken*

- **Context options break MultiTalk**
  - Image begins to shift when context windows take over, even with higher overlap settings
  - *From: Tango Adorbo*

- **LightX breaks some VACE functionality like first frame**
  - Issues noted with VACE compatibility
  - *From: Piblarg*

- **GGUF model loader not available in Wan wrapper**
  - People have been asking for eternity, unlikely to be implemented
  - *From: David Snow*

- **1.3B models tend to add sweaty/greasy look to skin**
  - Annoying problem, solution unknown
  - *From: David Snow*

- **MMaudio limited to 10 seconds maximum**
  - 1-30 seconds supported according to documentation
  - *From: mdkb*

- **VACE normals and lineart controlnets fail completely**
  - Only produce normals and line art, don't work for video generation
  - *From: mdkb*

- **LightX2V has reduced motion**
  - Motion is quite muted compared to other loras, though more stable
  - *From: jdl_grmck*

- **Single frame latent decoding causes color distortion**
  - Clipping single frames from latent causes flash/color issues, needs context of multiple frames
  - *From: CJ*

- **Tile lora doesn't work on heavily degraded videos**
  - Video was too degraded for the tile lora to process effectively
  - *From: David Snow*

- **NAG makes models significantly slower**
  - NAG makes flux kontext 2-10x slower, potentially makes WAN unacceptably slow
  - *From: MysteryShack*

- **VACE face consistency at low resolution**
  - VACE struggles with reference similarity and faces below 1024x576 resolution, faces shift around and artifact horribly at lower resolutions
  - *From: MysteryShack*

- **Wan length limitation**
  - Wan doesn't support anything over 5 seconds without workarounds like context overlap
  - *From: Jonathan*

- **UltraWan 1K portrait mode**
  - UltraWan 1K does NOT work well on portrait mode, only landscape videos
  - *From: phazei*

- **LightX2V step scaling**
  - LightX2V gets worse with more steps rather than better, can't increase steps for quality refinement
  - *From: hablaba*

- **MultiTalk context window**
  - MultiTalk is bad for anything over 81 frames, context window keeps returning to first frame
  - *From: AJO*

- **LightX2V kills motion and makes everything look slowed down**
  - Makes videos look unnatural, as if in space or underwater
  - *From: Jonathan*

- **Original CausVid at 1.0 strength destroys motion completely**
  - Why V2 version was created with reduced strength
  - *From: Kijai*

- **MultiTalk is very slow and has frame limits**
  - Takes forever to process and needs to be broken into chunks of ~420 frames
  - *From: Gateway {Dreaming Computers}*

- **Context options don't work well with I2V**
  - Specifically mentioned as problematic for image-to-video workflows
  - *From: zoz*

- **DDIM_uniform scheduler not available in wrapper**
  - Would help with LightX2V motion issues but not implemented
  - *From: Screeb*

- **Normal I2V and T2V are pretty useless without control**
  - Only work well with controlnets, VACE, UniAnimate or MultiTalk
  - *From: Kijai*

- **ACC Vid LoRA has too much style trained in**
  - Kijai doesn't like it because of built-in style bias
  - *From: Kijai*

- **Context windows get slow on long clips**
  - While memory efficient and smoother blending, performance degrades with length
  - *From: Kijai*

- **Starlight mini is very slow**
  - Takes significant time to process
  - *From: blake37*


## Hardware Requirements

- **121 frames at 1280x720**
  - Took 1 hour, used 80GB VRAM and 90GB RAM on A100 instance
  - *From: Zuko*

- **Phantom 1024x1200x81 frames**
  - 6 steps takes approximately 550 seconds on RTX 5090
  - *From: Thom293*

- **3 vs 6 step generation time**
  - 3 steps: 14 minutes for 189 frames, 6 steps: 29 minutes for same length
  - *From: Ruairi Robinson*

- **System RAM usage with Wan**
  - Went from 32GB to 96GB, 64GB probably adequate. Wan process is very system RAM hungry even below VRAM limits
  - *From: jdl_grmck*

- **RTX 5090 performance**
  - 85 frames at 1024x576, 8 steps: 110.31 seconds (22.614 GB max allocated memory)
  - *From: VRGameDevGirl84*

- **1.3B model speed**
  - Same generation in 42.36 seconds vs 131.13 seconds for 14B model
  - *From: VRGameDevGirl84*

- **RTX 5090 capacity**
  - Can handle 161 frames at 720p resolution
  - *From: Piblarg*

- **Film grain processing time**
  - Adds 30 seconds to processing time
  - *From: AJO*

- **Multi-GPU setup issues**
  - Adding 3090 alongside 4090 caused hard locking problems
  - *From: boorayjenkins*

- **24GB VRAM still needs swap**
  - Even with 24GB VRAM, block swapping is still necessary
  - *From: Dream Making*

- **Resolution vs generation time scaling**
  - 1280x536 takes 6 minutes, 640x264 takes 86 seconds - 4x speed improvement for 1/4 pixels
  - *From: Jonathan*

- **fp16 on RTX 2060**
  - RTX 2060 with 64GB RAM struggles with bf16, needs fp16 models with VRAM management at full
  - *From: hicho*

- **5090 FE pricing**
  - Scalped 5090 FE costs around $2850, compared to $3500+ on eBay
  - *From: Ruairi Robinson*

- **fp8 format compatibility**
  - fp8_e4m3fn for 4090, fp8_e5m2 for 3090, torch.compile causes inductor errors with fp8_e4m3fn
  - *From: TK_999*

- **VRAM for long sequences**
  - 5090 with 32GB can handle 409 frames at 768x512, may need block swapping for longer sequences
  - *From: AJO*

- **81 frames at 480p with LoRA combinations**
  - 90 seconds on unspecified hardware, 3.5 minutes for full combo
  - *From: hablaba*

- **MPS LoRA size**
  - 1.4GB file size
  - *From: DevouredBeef*

- **VACE face swap workflow**
  - 950 seconds processing time
  - *From: AJO*

- **SageAttention compatibility**
  - Requires updated Triton and torch 2.7.0+
  - *From: Valle*

- **4-bit quantization GPU requirements**
  - SVDQuant int4 works on 20xx series and up, fp4 needs 50xx series GPUs
  - *From: YatharthSharma*

- **FlowMo VRAM usage**
  - Uses gradients and inner optimization loop, requires significant VRAM despite gradient checkpointing
  - *From: Kijai*

- **VRAM usage**
  - Max allocated memory: 18.932 GB, Max reserved memory: 20.812 GB for 81 frames at 1024x576
  - *From: VRGameDevGirl84(RTX 5090)*

- **RTX 5090 compute capability**
  - Requires CUDA compute capability 8.9 support, needs sm_125 in CUDA_COMPUTE_CAPABILITIES
  - *From: samhodge*

- **High-end system specs**
  - 128GB SDRAM with 48GB Ampere A6000 for large frame inpainting workflows
  - *From: samhodge*

- **RTX 5080 SageAttention compatibility**
  - Requires SageAttention 2.1.1, Triton 3.3, PyTorch 2.7.0+cu128, CUDA 12.8
  - *From: lomerio/Kijai*

- **16GB VRAM limitations**
  - 16GB VRAM not enough for some workflows like uni3pc, need to use blockswap
  - *From: lomerio*

- **High resolution performance**
  - 1280x720 generation takes 50 minutes on certain setups, SageAttention can double speed at higher resolutions
  - *From: AJO/Kijai*

- **LoRA extraction from 14B models**
  - Takes 1 hour on 4090, inefficient for RAM, loads both models fully
  - *From: Kijai*

- **64GB RAM not enough for fp16 14B models**
  - Will cause swapping, need more RAM
  - *From: Kijai*

- **200GB RAM for video model operations**
  - Upgraded from 64GB when it wasn't enough for Hunyuan operations
  - *From: Thom293*

- **14B + VACE + preprocessing memory usage**
  - 14B + Vace + tons of preprocessors + offloading + high resolution = Total RAM annihilation
  - *From: David Snow*

- **Fast generation on low-end hardware**
  - 211s for video generation on 4060 8GB laptop with optimized LoRA stack
  - *From: Blitz*

- **VRAM for different resolutions**
  - 720x720 works with 12GB, 1080p needs more, 4K needs ~400GB
  - *From: The Punisher*

- **System RAM issues with multiple LoRAs**
  - 32GB VRAM and 128GB RAM for loading 4+ loras with no issue
  - *From: VRGameDevGirl84(RTX 5090)*

- **Dual RTX 5090 power requirements**
  - 1500W PSU might be enough for 2x RTX 5090 FE but may need undervolting
  - *From: Ruairi Robinson*

- **RTX 5090 undervolting benefits**
  - 10% less power usage but only 2% performance loss
  - *From: Ruairi Robinson*

- **48GB VRAM optimization**
  - Can reach 97+ frames at 1080p with GGUF models, Q8 saves 10GB, Q5_K_M saves 24GB
  - *From: Jonathan*

- **VRAM savings with GGUF**
  - Q4 GGUF gives 20GB more memory compared to fp16, Q8 roughly half the size of fp16
  - *From: Jonathan*

- **5090 performance expectations**
  - Should be much faster than reported times, 1280x848x125 frames in 5 minutes seems slow for 5090
  - *From: Jonathan*

- **3060 capabilities**
  - Can handle 1280x534 resolution without issues
  - *From: Jonathan*

- **VRAM usage with VACE**
  - VACE takes more VRAM, requires aggressive offloading and swapping blocks to system RAM
  - *From: MilesCorban*

- **Video depth preprocessing**
  - High resolution video depth processing causes frequent OOMs, recommend batch processing image sequences
  - *From: A.I.Warper*

- **Context processing speed**
  - Using more than 81 frames with context drastically increases generation speed
  - *From: Valle*

- **Minimum 8GB VRAM for 14B model**
  - 6GB might work but quality suffers. Needs 32GB RAM for offloading, 16GB RAM marginal. Block swapping less effective than GGUF+distorch
  - *From: The Punisher*

- **Video Depth Anything VRAM usage**
  - 275 frames at 720p uses <10GB VRAM with VitS model, VitL model is heavier
  - *From: A.I.Warper*

- **Q8 720x1280x73f generation**
  - Runs on 12GB VRAM, takes ~59 seconds per iteration
  - *From: The Punisher*

- ****
  - Current workflows max out 96GB of system RAM, requires ComfyUI restart after few runs
  - *From: David Snow*

- ****
  - Can run FP32 T5 and VAE with quantization enabled, reaches 98% during text encoding then 60% during generation
  - *From: Juan Gea*

- ****
  - RTX 3090 takes 1 hour for 33 frames at 720p, RTX 5090 much faster at 3 minutes for similar
  - *From: Dream Making*

- ****
  - 65 frames at 720p in 3 minutes with CausVid lora
  - *From: ingi // SYSTMS*

- **Any GPU can run FP32**
  - Even GTX 1060 can run FP32, base model is actually FP8 not FP32
  - *From: Dream Making*

- **5090 performance with GGUF**
  - 120+ frames at 1280x848 in under 5 minutes, 125 frames in 242-253 seconds
  - *From: blake37*

- **12GB VRAM works with full version**
  - Full FP8 version from HuggingFace works on 12GB VRAM
  - *From: TRASHTRASH*

- **RTX 5090 performance boost**
  - Major speed improvement for testing - user reports ability to test much faster than with 3080ti
  - *From: VRGameDevGirl84(RTX 5090)*

- **L40 rental performance**
  - 480x832 with 121 frames takes 173 seconds on rented L40
  - *From: The Dude*

- **24GB VRAM for fp32 at 720p**
  - Can handle 48 frames at 720p with model compilation/quantization
  - *From: Juan Gea*

- **64GB RAM not enough for fp32 VAE at 720p**
  - System memory limitation when using fp32 precision for VAE
  - *From: Dream Making*

- **Wrapper uses more VRAM/RAM than native**
  - More likely to cause OOM errors compared to native implementation
  - *From: Thom293*

- **VRAM management**
  - 48GB VRAM can handle 720p 81 frames, Windows uses 1-4GB VRAM for display
  - *From: samhodge*

- **Resolution limits with 4080**
  - 1024x576 81 frames is maximum resolution achievable
  - *From: CaptHook*

- **Torch 2.7.0 recommended**
  - Required for fp16_fast which provides 20% speed boost
  - *From: Kijai*

- **Self-forcing VRAM**
  - Works within 16GB VRAM for 720p generation
  - *From: zelgo_*

- **MultiTalk GPU requirements**
  - 480p can run on single GPU, 720p requires multiple GPUs
  - *From: ZeusZeus*

- **Self-forcing speed**
  - 4090 generates 81 frames in ~5 seconds with 6 steps, 35-43 seconds for full workflow
  - *From: slmonker*

- **Self-Forcing VRAM usage**
  - Uses almost all of 15GB VRAM, similar to regular 1.3B models
  - *From: MysteryShack*

- **Self-Forcing performance by GPU**
  - RTX 3060: 512x768, 65 frames, 2 steps in 17 seconds. Performance varies significantly by GPU generation
  - *From: Kaïros*

- **MultiTalk installation requirements**
  - Flash-attn is the main problematic dependency, takes long time to compile
  - *From: orabazes*

- **5090 capabilities**
  - Can handle 161 frames without rewanpatcher, potentially 10+ minute videos in single shot with memory optimization
  - *From: Piblarg*

- **VRAM usage comparison**
  - Native workflows: under 16GB for 480x720-97frames, Wrapper: fills VRAM instantly even at 192x256-33frames on AMD RX 6800
  - *From: patientx*

- **Self-forcing speed benchmark**
  - 21 seconds for 832x480@16fps on older A6000 GPU
  - *From: MilesCorban*

- **WAN Context Window VRAM usage**
  - 832x420x82 frames fits in 12GB with block swap on CUDA
  - *From: Kijai*

- **SeedVR memory requirements**
  - Claims 80GB for 720p 100 frames, unclear if fp32 figures
  - *From: Kijai*

- **Character lora training times**
  - H100: 20 minutes, 4090: couple hours, 3090: 4-5 hours
  - *From: Ruairi Robinson/JohnDopamine/Owlie*

- **Multiple VACE embeds VRAM usage**
  - Single VACE embed takes 47GB VRAM on current setup, multiple embeds can cause OOM even on 80GB cards
  - *From: HeadOfOliver*

- **GGUF Q8 Wan + VACE performance**
  - ~2min15 render time for 1024x576, 8 steps, 81 frames on RTX4090
  - *From: JmySff*

- **VRAM for Wan 14B with VACE**
  - Working set around 70GB system RAM, 48GB VRAM for 1280x720 with fp8
  - *From: jellybean5361*

- **RTX A6000 performance**
  - 118GB RAM, A6000 GPU - native runs twice as fast as wrapper
  - *From: MysteryShack*

- **RTX 5090 vs 4090 Topaz performance**
  - RTX 5090 slower than RTX 4090 in Topaz (30 mins vs 20 mins for 720p 8sec clip)
  - *From: Ruairi Robinson*

- **4090 VACE settings**
  - Can run VACE fine with block swap 15, runs 41 frames without issues
  - *From: chrisd0073*

- **NAG VRAM usage**
  - Adds approximately 1.2GB VRAM usage due to two attention passes
  - *From: wange1002*

- **NAG works on 6GB cards**
  - Successfully runs on RTX 2060 6GB
  - *From: hicho*

- **WAN models storage space**
  - Various WAN model files occupy approximately 500GB storage space total
  - *From: wange1002*

- **Block swap for high resolution**
  - 576x1024 generation may require block swap for VRAM management
  - *From: MatiaHeron*

- **Self-forcing model speed**
  - 17 FPS on 1 H100 GPU with sub-second latency
  - *From: SS*

- **AMD GPU compatibility**
  - WAN working on AMD graphics cards with proper setup, most plus features not usable
  - *From: patientx*

- **Torch compiler GPU requirements**
  - fp8_e5m2 for compute capabilities under 4000 series, normal fp8 works with 40 series and up
  - *From: HeadOfOliver*

- **4090 OOM with longer VACE generations**
  - Needed to switch to A100 for longer generations, or render normal crafter frames first
  - *From: Flipping Sigmas*

- **Causal sampling VRAM usage**
  - KV cache size enormous, 24GB not enough for VRAM, had to create on CPU then move to GPU
  - *From: Kijai*

- **5090 performance for 241 frames**
  - Can handle extended context generations effectively
  - *From: blake37*

- **Cosmos model performance**
  - 14B 720p 63 frames took 957 seconds on 5090, 2B 720p 121 frames took 669 seconds
  - *From: slmonker*

- **RTX 3060 12GB VRAM**
  - Can run 832x480, 81 frames with native nodes, under 10 minutes without OOM
  - *From: mdkb*

- **RTX 4090 tiled upscaling**
  - Can handle 81 frames at 1920x544 using 60% VRAM with tiled sampling
  - *From: David Snow*

- **RTX 4090 context length**
  - Can fit 41 frames at 720p resolution
  - *From: A.I.Warper*

- **NAG performance impact**
  - Slows generation by 10-20% instead of 2x CFG penalty
  - *From: Juampab12*

- **832*480 33 frames generation**
  - 20 seconds on 4080 super with self-forcing 4 steps
  - *From: yi*

- **832x480 81 frames generation**
  - 35 seconds on 4090, 1min 50sec on 4060ti 16GB VRAM with 4 steps
  - *From: Ada*

- **720x1280 generation**
  - 270 seconds on 3090 with new lora plus style lora
  - *From: crinklypaper*

- **480x832 generation**
  - 107 seconds on 3090
  - *From: crinklypaper*

- **FP8 support**
  - RTXA5000 cannot do FP8, need newer GPU or use e5m2 version
  - *From: Tomber*

- **RTX 3090 performance with LightX2V**
  - 4 steps generation takes approximately 5 minutes on RTX 3090
  - *From: Valle*

- **Full LightX model size**
  - Full model is 28.6GB (14B parameter size), requires significant VRAM or quantization
  - *From: Thom293*

- **RAM usage with MAGREF**
  - Loading everything on first run uses 86% of 96GB RAM, accumulates with changes requiring reboots
  - *From: David Snow*

- **Model size**
  - MAGREF 14B model is 17GB
  - *From: Gateway {Dreaming Computers}*

- **VRAM and RAM usage increasing**
  - 5090 with 32GB VRAM and 96GB system RAM starting to max out, causing hard crashes
  - *From: blake37*

- **Memory management issues**
  - ComfyUI keeps offloaded content in RAM and adds it again, causing memory problems
  - *From: ingi // SYSTMS*

- **MultiTalk model size**
  - Uses 14B model plus additional 9GB on top
  - *From: Kijai*

- **80GB VRAM threshold**
  - Anything under 80GB needs offload_device with 14B model
  - *From: Kijai*

- **32GB VRAM with 14B**
  - Still needs text encoder offloading to avoid OOM
  - *From: jacinda*

- **VRAM monitoring**
  - Should be around 95% usage with proper block swapping
  - *From: Kijai*

- **MultiTalk VRAM usage**
  - +9GB in bf16, half that in fp8, plus base model requirements
  - *From: Kijai*

- **TAEW requires non-parallel processing for higher res**
  - OOMs at higher resolutions even with 24GB VRAM on 4090
  - *From: aipmaster*

- **Context overlap performance impact**
  - 48 overlap: 7 minutes generation time, 64 overlap pushes to even longer
  - *From: Kijai*

- **Multitalk VRAM usage on Linux**
  - 7GB VRAM on Linux vs higher on Windows, 18GB max allocated memory total
  - *From: A.I.Warper*

- **ATI LoRA extraction on 4090**
  - Takes about 40 minutes, requires lots of RAM for fp16 models
  - *From: Kijai*

- **Multitalk with context windows performance**
  - About 1 minute per second of video on 5090, very slow due to inefficiency
  - *From: burgstall*

- **Wav2vec model size**
  - Chinese wav2vec model is about 1GB
  - *From: Kijai*

- **MultiTalk VRAM**
  - Works on 12GB VRAM cards, generates 321 frames successfully
  - *From: DawnII*

- **MultiTalk struggles on 24GB**
  - 24GB VRAM / 64GB system RAM still having issues, may need optimization
  - *From: TK_999*

- **5090 performance**
  - Much faster performance without blockswapping, 1041 frames in 10:32
  - *From: Kijai*

- **Minimum VRAM recommendation**
  - Really need 24GB and beyond to play with newest AI video tools
  - *From: JohnDopamine*

- **5090 performance advantage**
  - 32GB VRAM eliminates need for block swap at 832x480, ~50% faster than 4090
  - *From: Kijai*

- **Memory usage for 2000 frames**
  - Max allocated 19.808GB, max reserved 20.938GB for decoding
  - *From: Kijai*

- **3090 VRAM limitations**
  - 25GB total requirement means heavy block swapping needed
  - *From: Kijai*

- **Block swap scaling**
  - 16GB VRAM needs 6 blocks, 24GB needs 25 blocks swapped
  - *From: Juampab12*

- **MultiTalk VRAM usage**
  - Actual inference: 12-13GB, but model loading can use full 24GB. Much faster on 5090
  - *From: Purz*

- **Long video generation time**
  - 1 minute 45 second video took 30 minutes on L40S
  - *From: manu_le_surikhate_gamer*

- **21 second 720p generation**
  - Successfully generated 21 second 720p video
  - *From: slmonker(5090D 32GB)*

- **Cloud GPU costs**
  - Dollar per hour for 4090/RTX 6000, about 6 videos per hour. 5090s on select European servers with slow internet
  - *From: MysteryShack*

- **2000 frames generation**
  - Requires RTX 5090 level VRAM to fit
  - *From: Kijai*

- **1000 frames generation**
  - Uses 21GB VRAM
  - *From: A.I.Warper*

- **14B model on 6GB GPU**
  - Possible with 64GB system RAM for offloading
  - *From: hicho*

- **8GB GPU compatibility**
  - 1.3B models can run on 8GB or even 6GB cards
  - *From: Ablejones*

- **High frame count VRAM usage**
  - Limited to 95 frames on 14.99GB VRAM
  - *From: MysteryShack*

- **MagRef VRAM usage**
  - Causes OOM on 3090 with 48GB RAM when combined with MultiTalk, larger model than base
  - *From: Jemmo*

- **SeedVR2 VideoUpscaler requirements**
  - 90GB VRAM usage, extremely slow performance
  - *From: DawnII*

- **MultiTalk processing time**
  - 3 seconds takes 1m40s on 3090, 50 seconds takes 900 seconds on unspecified hardware
  - *From: ˗ˏˋ⚡ˎˊ-*

- **MultiTalk generation times on RTX 4090**
  - 140s at cfg 1/25fps vs 236s at cfg 6/30fps vs 346s at 60fps
  - *From: voxJT*

- **Generation slowdown after multiple runs**
  - Time increases from 350sec to 1000sec after 10-15 generations on RTX 4090
  - *From: KuriousKatz*

- **720p 30fps generation**
  - 17.789 GB max allocated memory, 20.094 GB max reserved on RTX card, 2514.51 seconds execution
  - *From: burgstall*

- **RTX 5090 OOM with 10 second video**
  - Smaller Wan model still causes out of memory with longer videos
  - *From: orabazes*

- **3060 RTX limitations**
  - Cannot get 720p generation, limited to lower resolutions
  - *From: mdkb*

- **VRAM for 14B self-forcing LoRA**
  - 24GB card required, may need fp8_e4m3fn quantization and low frame count
  - *From: MilesCorban*

- **Block swap settings for 24GB**
  - Use 25-40 block_swap for optimal performance on 4090
  - *From: Juampab12*

- **Generation speed examples**
  - 77 frames at 1280x720 with 4 steps in 198.63 seconds on RTX 5090
  - *From: VRGameDevGirl84(RTX 5090)*

- **1920x1080 upscaling**
  - 150-200 seconds generation time on RTX 5090, block swapping helps with OOM
  - *From: VRGameDevGirl84(RTX 5090)*

- **UltraWan 1080p generation**
  - 3m 30s for 81 frames 1920x1080 8 steps on RTX 4090
  - *From: Juampab12*

- **MultiTalk 720p**
  - Works on older RTX 3090 but quite slow
  - *From: burgstall*

- **24GB VRAM limitation**
  - 24GB not enough for some 4K generations
  - *From: Dream Making*

- **MultiTalk long generations**
  - 3min generation OOMs on RTX 3090 24GB VRAM even at 352x480
  - *From: burgstall*

- **720p 2min MultiTalk**
  - Used 97% VRAM on RTX 5090
  - *From: Charlie*

- **630 frame upscaling**
  - Max 7.5GB VRAM allocated on RTX 5090 for 1024x576
  - *From: VRGameDevGirl84(RTX 5090)*

- **720p WAN processing**
  - RTX 3060 can handle 720p with UltraWan 1K and 1.3B model in 5 minutes
  - *From: mdkb*

- **Video LoRA training**
  - 4 hours for 10 images on RTX 3060
  - *From: mdkb*

- **3060 RTX capabilities**
  - Can run 1280x720 with UltraWan 1K and self-forcing DMD VACE 1.3B, limited to 720p max
  - *From: mdkb*

- **VACE multi-embed VRAM**
  - Can stack 2 VACE embeds on 3060 12GB in native workflows at lower resolutions
  - *From: mdkb*

- **4090 for DepthCrafter**
  - 4090 is enough for DepthCrafter but may need memory shuffling depending on settings
  - *From: JohnDopamine*

- **Ampere card quantization**
  - Use fp8e5m2 on Ampere cards, avoid fp8_e4m3fn which causes black outputs
  - *From: jeffcookio*

- **4K upscaling VRAM usage**
  - 15GB VRAM for 1080p generation then upscale, 50GB regular RAM for upscale with model
  - *From: HeadOfOliver*

- **3090 Multitalk frame limits**
  - 500 frames works, 1440 frames causes OOM, trying 720 frames
  - *From: NebSH*

- **B200 for 1080p generations**
  - Using B200 on Runpod for 1080P generations at full fp32
  - *From: ingi // SYSTMS*

- **VRAM usage with block swapping**
  - 473 frames at 1024x576 uses only 20.6GB VRAM with block swapping enabled, making it possible on RTX 3090 cards
  - *From: samhodge*

- **Context processing capabilities**
  - 48GB card can handle 300+ frames at 480p, can push to 1280x720 with 41 frame context
  - *From: VRGameDevGirl84(RTX 5090)*

- **Block swap memory distribution**
  - 3352.31MB on CPU, 10056.94MB on GPU, 13409.26MB total for transformer blocks
  - *From: samhodge*

- **VRAM management for upscaling**
  - Use context options with block swap 40 for 1920x1080 upscaling without OOM issues
  - *From: VRGameDevGirl84(RTX 5090)*

- **4090 limitations for full models**
  - Uncertainty about running full Kontext model on RTX 4090, recommending fp8 version
  - *From: Mathew*

- **4070 Super performance**
  - 3 second video generation taking 15 hours with Wan2.1 i2v 480p 14B model, seeking faster alternatives
  - *From: RollmeWanKenobi*

- **Memory usage with context overlap**
  - A little higher but not severe difference unless very long video
  - *From: DawnII*

- **Temperature increase from upscaling**
  - 44 second video upscaling raised room temperature by 11 degrees
  - *From: voxJT*

- **VRAM for lightx2v VACE**
  - Can use 10gb Q_4_S.gguf model on 12gb VRAM, 24gb can probably use Q6 or higher
  - *From: Jonathan*

- **Undervolted 4090 performance**
  - 216 seconds generation time with ultrawan and tile lora at 1600x900, 50% undervolt using SDPA
  - *From: David Snow*

- **VACE model size**
  - 32gb for full model, can use quantized versions for lower VRAM
  - *From: Rainsmellsnice*

- **3090 performance with VACE**
  - 60s generations with 3090, 24gb VRAM
  - *From: Rainsmellsnice*

- **VACE VRAM needs**
  - VACE only supports blockswap in wrapper, not full VRAM offload like MagRef. Lower resolution makes face consistency impossible
  - *From: MysteryShack*

- **3060 RTX workflow adaptation**
  - 3060 RTX requires converting wrapper workflows to native with GGUF models to work, often needs butchering workflows
  - *From: mdkb*

- **Tile upscaler VRAM usage**
  - 121 frames at 1920x1080 takes nearly all VRAM on high-end GPU, slowing generation
  - *From: David Snow*

- **Storage performance**
  - Don't try running models from standard HDD, needs SSD for proper performance
  - *From: mdkb*

- **VRAM usage increase with MMAudio**
  - Installing MMAudio requirements pushes VRAM usage over edge for A4500 with 20GB
  - *From: The Shadow (NYC)*

- **SeedVR2 upscaler performance**
  - 10 minutes per second of upscale on RTX 4090
  - *From: burgstall*

- **Sage Attention 2 Plus speed on RTX 4090**
  - 5-7% faster generation times depending on resolution
  - *From: Kijai*


## Community Creations

- **Vintage style LoRA** (lora)
  - Trained on vintage style images, works well with Wan 14B, adds natural colors and removes AI look
  - *From: VRGameDevGirl84(RTX 5090)*

- **Anamorphic lens LoRA** (lora)
  - LoRA for anamorphic lens effects in text-to-video generation
  - *From: Ruairi Robinson*

- **Soviet T-54 Tank LoRA** (lora)
  - Tank model LoRA coming soon to Civitai
  - *From: MisterMango*

- **CausVid V1.5 'no first block'** (lora)
  - Original CausVid with block 0 disabled, extracted by Kijai
  - *From: JohnDopamine*

- **CausVid V2** (lora)
  - Block 0 and other blocks removed to eliminate need for block settings node
  - *From: TK_999*

- **Vintage LoRA** (lora)
  - VRGameDevGirl84's first locally trained LoRA that acts as detailer even without vintage prompts
  - *From: VRGameDevGirl84*

- **Detail Transfer node fork** (node)
  - Forked Detail Transfer node into NormalCrafter pack for facial detail transfer
  - *From: A.I.Warper*

- **Film grain workflow** (workflow)
  - Film grain node that doesn't crash and adds grain at various strengths (0.01-0.2)
  - *From: AJO*

- **Normal Crafter preprocessor** (preprocessor)
  - Best normal map preprocessor currently available
  - *From: VRGameDevGirl84(RTX 5090)*

- **Custom detailer LoRA** (lora)
  - Personal detailer booster LoRA used at 0.5 strength
  - *From: VRGameDevGirl84(RTX 5090)*

- **Wan14B-Cyberpop-Lora** (lora)
  - Cyberpunk style LoRA for T2V 14B model with various test results
  - *From: David Snow*

- **Custom ATI trajectory editor** (tool)
  - Improved trajectory editor with circle presets and keyframe support created with Claude
  - *From: Juampab12*

- **Wan Cinematic Video Prompt Generator** (tool)
  - Custom GPT trained for generating optimized Wan prompts
  - *From: VRGameDevGirl84*

- **ATI trajectory editor modifications** (tool)
  - Code modifications to handle JSON trajectory format in ComfyUI wrapper
  - *From: Juampab12*

- **DWPose to ATI trajectory converter** (script)
  - Python script to convert DWPose JSON output to ATI trajectory format
  - *From: Mngbg*

- **Power LoRA node proposal** (node)
  - VRGameDevGirl84 considering creating power lora node for wrapper compatibility
  - *From: VRGameDevGirl84(RTX 5090)*

- **Custom trajectory points editor** (tool)
  - HTML app for creating ATI trajectory points with timeline features
  - *From: Juampab12*

- **POSE_KEYPOINT to Coord_str node** (node)
  - Converts OpenPose keypoints to ATI coordinate format
  - *From: toyxyz*

- **ChatGPT generated ATI code** (tool)
  - Code for trajectory creation in ATI
  - *From: VRGameDevGirl84*

- **SageAttention patch node** (node)
  - Enables SageAttention in KJNodes
  - *From: Kijai*

- **Uni3C workflow for static scenes** (workflow)
  - Optimized workflow for camera movement control in static scenes
  - *From: mamad8*

- **CameraBench conversion script** (script)
  - Converts dataset to 16fps and removes videos with less than 49 frames
  - *From: mamad8*

- **Gaze Control node** (node)
  - ComfyUI node for controlling eye gaze direction with solid/outline iris options
  - *From: Mads Hagbarth Damsbo*

- **Glamour Refiner LoRA** (lora)
  - Trained on 50 headshot photos of women, adds detail and glamour effect at 0.4 strength
  - *From: VRGameDevGirl84(RTX 5090)*

- **Point cloud to trajectory converter** (tool)
  - Converts 3D point cloud data to 2D motion vectors for ATI control
  - *From: Juampab12*

- **Face enhancer LoRA** (lora)
  - Trained on 4K resolution face images, seems to help with framing and face quality
  - *From: VRGameDevGirl84(RTX 5090)*

- **Vintage film LoRA** (lora)
  - Test LoRA for vintage film effects, limited dataset but functional
  - *From: VRGameDevGirl84(RTX 5090)*

- **Merged mega LoRA** (lora)
  - Attempted merge of CausVid, AccVid, MovieGen and custom LoRAs - partially successful
  - *From: VRGameDevGirl84(RTX 5090)*

- **LoRA merger script** (tool)
  - Script for merging multiple LoRAs, though with limitations based on layer compatibility
  - *From: VRGameDevGirl84(RTX 5090)*

- **Banodoco Wan Knowledge Base** (tool)
  - NotebookLM-based searchable knowledge base of all Wan channel discussions
  - *From: Nathan Shipley*

- **CoTracker ComfyUI integration** (node)
  - Point tracking capabilities for ComfyUI
  - *From: tttADs*

- **3D trajectory control app** (tool)
  - Unity-based app for 3D trajectory control with point cloud generation from 1-2 images
  - *From: Juampab12*

- **Master merge model** (model)
  - Wan14BT2V model with CausVid baked in, no LoRAs needed
  - *From: VRGameDevGirl84(RTX 5090)*

- **BETA Helper Nodes pack** (node)
  - Includes frame trimming and sharpest frame selection nodes
  - *From: burgstall*

- **Wan14BT2V Master Model** (merged model)
  - Custom merge with multiple LoRAs for better results
  - *From: VRGameDevGirl84(RTX 5090)*

- **Face dataset training** (dataset)
  - 4K res 60 image extra detailed Face dataset trained for better facial features
  - *From: VRGameDevGirl84(RTX 5090)*

- **VRGameDevGirl84's Master Model merge** (model)
  - Blend of all good loras (causvid, accvid, mps, etc) merged into single model with optimized settings
  - *From: VRGameDevGirl84*

- **Color matching node** (node)
  - Post-processing node to fix contrast issues in low-step generation
  - *From: The Punisher*

- **VACE patch node for native** (node)
  - Works with 1.3b 100%, 14b might have issues, not compatible with GGUFs
  - *From: The Punisher*

- **Realism LoRA** (lora)
  - LoRA that improves realism, works well at 2.0 strength
  - *From: VRGameDevGirl84(RTX 5090)*

- **Lightricks Rendering Nodes** (node)
  - Still in development, used for creating camera change workflows with masking
  - *From: toyxyz*

- **MultiGPU node** (node)
  - Helps with VRAM management by distributing load across multiple GPUs
  - *From: MilesCorban*

- **ComfyUI-WarperNodes** (node)
  - Collection including mouth tracking using pose landmarks for selective detail enhancement
  - *From: A.I.Warper*

- **Modified Video Depth Anything** (node)
  - Version that doesn't require xformers and properly manages VRAM by offloading models
  - *From: A.I.Warper*

- **VRGameDevGirl84's Wan merge** (model)
  - Custom merge that works optimally with low shift values (1-2) for cinematic results
  - *From: VRGameDevGirl84*

- **WAN2114BT2V-FusionX** (model merge)
  - I2V merge model with specific non-commercial licensing
  - *From: VRGameDevGirl84(RTX 5090)*

- **Wildcard processing node** (node)
  - Node that processes wildcard strings for video models where native wildcards don't work
  - *From: the_darkwatarus_museum*

- **ATI GGUFs** (quantized models)
  - GGUF versions of ATI model uploaded for GPU-poor users
  - *From: The Punisher*

- **Nissan car LoRAs** (lora)
  - 370z and GTR Skyline V-Spec 2 video LoRAs for car generation
  - *From: MisterMango*

- **VACE version GGUF converter** (script)
  - Script to add VACE part to safetensors file then convert to GGUF
  - *From: The Punisher*

- **ATI trajectory editor rebuilt** (tool)
  - Rebuilt from scratch with timeline features and better maintainability
  - *From: Juampab12*

- **Agentic system for channel analysis** (tool)
  - System using n8n to analyze Discord channel outputs for Q&A without bothering users
  - *From: AJO*

- **Custom sigma schedules** (technique)
  - Custom sigma values that work better with low shift than standard sigmas with high shift
  - *From: The Punisher*

- **Phantom merge model** (model)
  - Merged model that works with Phantom for I2V with popular loras baked in
  - *From: VRGameDevGirl84(RTX 5090)*

- **LaFerrari LoRA** (lora)
  - Car model LoRA created by community member
  - *From: MisterMango*

- **Fusion model merge** (model)
  - Model merge that's easier and faster than LoRA stacking
  - *From: VRGameDevGirl84(RTX 5090)*

- **DWPose masker with facial option** (tool)
  - Added full facial option to DWPose masker
  - *From: A.I.Warper*

- **Updated patch nodes** (node)
  - Fixed TeaCache, enhance-a-video, and VACE compatibility issues
  - *From: Kijai*

- **FusionX** (model)
  - Wan model merge with CausVid and other LoRAs baked in, compared to how Pony was for SDXL
  - *From: VRGameDevGirl84*

- **McLaren 720s LoRA** (lora)
  - Car model LoRA released on community channel
  - *From: MisterMango*

- **Converted self-forcing model** (model)
  - Self-forcing model converted to work with ComfyUI wrapper
  - *From: Kijai*

- **Detail LoRA for 1.3B** (lora)
  - VRGameDevGirl84's detail enhancement LoRA works with Self-Forcing at various strengths
  - *From: VRGameDevGirl84*

- **Pad Image Batch Interleaved node** (node)
  - Node for replacing every nth frame with blank frames for VACE control techniques
  - *From: TK_999*

- **Fancy guide modes for inpainting** (workflow)
  - Clownshark Batwing's model-agnostic guide systems for advanced inpainting control
  - *From: Clownshark Batwing*

- **VACE+Phantom merge** (model)
  - Merged model allowing both VACE control and Phantom character consistency to work together
  - *From: Piblarg*

- **Wan loop video workflow** (workflow)
  - Workflow for creating seamless video loops with image blending to reduce color differences
  - *From: toyxyz*

- **Self-forcing conversion script** (script)
  - Python script to convert self_forcing_dmd.pt to ComfyUI-compatible safetensors format
  - *From: Jonathan*

- **Points editor script for ATI** (tool)
  - Custom trajectory editor with saving projects, timeline, autotracking, keyframes for ATI control
  - *From: Juampab12*

- **Jennifer Connelly character lora** (lora)
  - Successfully trained character lora showing good likeness and consistency in Star Wars scene
  - *From: Ruairi Robinson*

- **Trajectory editor app** (tool)
  - Custom trajectory editor with rigging capabilities, freehand drawing, skeleton animation with keyframes
  - *From: Juampab12*

- **Custom frame batching node** (node)
  - Splits input frames into batches of 81 frames and extracts final frame as start frame for next batch
  - *From: A.I.Warper*

- **Hair LoRA (curly hair)** (lora)
  - Trained on curly hair using upscaled thumbnail images and hand-edited hair in Krita
  - *From: Thom293*

- **Sydney Sweeney LoRA** (lora)
  - Character LoRA that works with VACE model
  - *From: Ruairi Robinson*

- **NAG implementation for Wan** (node)
  - Non-functional PR converted to working NAG implementation showing impressive results
  - *From: Kijai*

- **NAG integration PR** (node)
  - Normalized Attention Guidance support added to WanVideoWrapper by kabachuha
  - *From: Kijai*

- **Florence prompt composer** (workflow)
  - Takes subject from one image and setting from another to compose prompts
  - *From: hicho*

- **VRAM poor batching system** (workflow)
  - Uses ComfyUI-DirGir to manage VRAM for long video generation by writing frames to directory
  - *From: DevouredBeef*

- **ComfyUI-keitNodes** (node)
  - Resizes images to resolution below max_pixels while preserving aspect ratio for video generation
  - *From: 327467189525282816*

- **Custom workflow with prompt composer and florence** (workflow)
  - WAN generation using prompt composer and Florence integration
  - *From: hicho*

- **NAG (Negative Attention Guidance) node** (node)
  - Cross attention patching for better negative prompt control
  - *From: Kijai*

- **Phantom/VACE merge nodes** (node)
  - Native ComfyUI nodes for combining Phantom and VACE workflows
  - *From: Piblarg*

- **WanVideo TextEncodeSingle node** (node)
  - Cleaner interface for single text encoding in WAN workflows
  - *From: Guey.KhalaMari*

- **Self-forcing workflow implementation** (workflow)
  - ComfyUI workflow for the new self-forcing model
  - *From: SS*

- **Police car lora** (lora)
  - U.S.A police car style lora for Wan
  - *From: MisterMango*

- **Happy Tree Friends lora** (lora)
  - Beta lora in Happy Tree Friends animation style
  - *From: MisterMango*

- **Prompt composer workflow** (workflow)
  - Removes background people and repositions subjects automatically
  - *From: hicho*

- **Skeleton rig trajectory system** (workflow)
  - Uses skeleton rigs to create precise movement trajectories for video generation
  - *From: Juampab12*

- **FusionX merge** (model)
  - Merge of CausVid, AccVideo, MPS, HPS and other loras for improved quality and speed
  - *From: VRGameDevGirl84*

- **Points tracking app** (tool)
  - App for extracting trajectories using RAFT model and placing on other images
  - *From: Juampab12*

- **FPS calculator node** (node)
  - Builds skip list for Rife frame interpolation based on start/end fps
  - *From: AJO*

- **Chained VACE sampler workflow** (workflow)
  - Allows chaining multiple VACE samplers with controllable frame overlap
  - *From: the_darkwatarus_museum*

- **Happy tree friends lora** (lora)
  - Style lora for cartoon aesthetic
  - *From: MisterMango*

- **Wan21_T2V_14B_lightx2v_cfg_step_distill_lora_rank32** (lora)
  - LoRA extraction of LightX2V self-forcing model for 4-step inference
  - *From: Kijai*

- **NAG node in KJNodes** (node)
  - Enables NAG usage in native ComfyUI
  - *From: Screeb*

- **Video captioner batch workflow** (workflow)
  - Working video captioner that runs in batches but loads everything at once
  - *From: Thom293*

- **Spline Path Control Tool** (tool)
  - Web tool for creating control splines for camera/object movement, mix of kijai's spline node and create shape on path node with speed controls
  - *From: Jonathan*

- **Image morph workflows for VACE + LightX2V** (workflow)
  - Simple workflow for morphing between images using VACE and lightx2v lora
  - *From: David Snow*

- **Ultimate SD Upscale video workflow** (workflow)
  - Work in progress upscaling workflow for videos
  - *From: David Snow*

- **Automated multi-scene video generation system** (workflow)
  - Complex automated system using LLMs for dialogue, emotion, voice, sound effects across 5 scenes
  - *From: AJO*

- **stfuLORA** (lora)
  - LoRA trained on quiet people to fix Phantom talking issue
  - *From: Thom293*

- **Comprehensive VACE + Phantom workflow** (workflow)
  - Extensive workflow with grouping for I2V with VACE and Phantom integration
  - *From: phazei*

- **MultiTalk branch** (wrapper)
  - Single talking head implementation, experimental/incomplete
  - *From: Kijai*

- **FlowMatch Scheduler workflow** (workflow)
  - 2 sampler setup for high shift values with LightX2V
  - *From: Ada*

- **Auto-extending video loop workflow** (workflow)
  - Automatically sends last frame to new generation, exports individual and final videos
  - *From: Nekodificador*

- **Character masking workflow for VACE** (workflow)
  - Workflow for character masking that inpaints and replaces with reference image
  - *From: MilesCorban*

- **NAG node implementation** (node)
  - Native NAG implementation built with Claude, though overly complex
  - *From: CJ*

- **Multitalk implementation** (node)
  - Lip sync functionality in separate branch of WanVideoWrapper
  - *From: Kijai*

- **Native VACE workflows** (workflow)
  - VACE inpainting workflows with SAM2 integration for character swapping
  - *From: mdkb*

- **UltraWan LoRA** (lora)
  - 4K dataset trained LoRA for improved quality on Wan-T2V-1.3B
  - *From: yi*

- **WanVideoOptimalResizer** (node)
  - Automatically finds optimal resolution for WanVideo and resizes input accordingly
  - *From: 327467189525282816*

- **WanVideoResolutionFinder** (node)
  - Returns width and height without resizing, more efficient for single resolution targets
  - *From: 327467189525282816*

- **Modified VACE Encoder** (node)
  - Attempts to accept latents from previous generation to reduce color shifting
  - *From: Simonj*

- **Indexed LoRA loader** (node)
  - Dynamic input count LoRA loader using JavaScript, change index to switch LoRAs
  - *From: burgstall*

- **Fusion Ingredients workflow** (workflow)
  - Modular workflow allowing easy LoRA stacking and modification
  - *From: VRGameDevGirl84*

- **1.3B detailer LoRA** (lora)
  - Custom LoRA that improves detail in 1.3B model outputs
  - *From: VRGameDevGirl84*

- **Spline Path Control v2** (tool)
  - Web-based tool for controlling motion via splines, works with VACE, includes scene saving as PNG
  - *From: Jonathan*

- **Multi-LoRA node** (node)
  - Prefilled node with 4 LoRA options to replace powerloader functionality
  - *From: JohnDopamine*

- **FusionX merge** (model)
  - Stacked LoRA combination including LightX2V and other acceleration LoRAs
  - *From: VRGameDevGirl84(RTX 5090)*

- **Custom NAG prompts for flux face** (workflow)
  - Specific negative prompts to combat flux face: 'pointy chin, sharp chin, overly smooth skin, wide anime eyes'
  - *From: VRGameDevGirl84(RTX 5090)*

- **Progressive Reference Frame MultiTalk Implementation** (tool)
  - Failed attempt to solve context window visual jumps by implementing progressive reference frame system in MultiTalk
  - *From: AJO*

- **UltraWan 1K ComfyUI conversion** (lora)
  - Converted UltraWan 1K LoRA for ComfyUI use with zero-padding technique for Wan 14B compatibility
  - *From: Alisson Pereira*

- **Video Continuation Generator node** (node)
  - Fixes color distortion and detail loss in video continuations
  - *From: pom*

- **Video-to-video MultiTalk workflow** (workflow)
  - Combines video-to-video with lip sync and optional Chatterbox
  - *From: VRGameDevGirl84(RTX 5090)*

- **Wan merging tools via LLM** (tool)
  - DARE method for merging models instead of just adding
  - *From: JohnDopamine*

- **Continuation node** (node)
  - Enables longer video generation with 81 frame chunks
  - *From: pom*

- **MultiTalk VACE modification** (code)
  - Modified code to make MultiTalk work with VACE T2V
  - *From: VRGameDevGirl84(RTX 5090)*

- **Difference Checker node** (node)
  - Creates black image showing only differences between two pictures/videos
  - *From: MilesCorban*

- **Modified WanVideoWrapper** (tool)
  - Fork that patches VACE to work with MultiTalk by ignoring MultiTalk layers
  - *From: Tango Adorbo*

- **Video to video upscaling workflow** (workflow)
  - Workflow for upscaling videos using Wan FusionX with LightX, supports creative and enhancement modes
  - *From: VRGameDevGirl84(RTX 5090)*

- **UltraWan LoRA** (lora)
  - LoRA trained on 58.8k high-resolution videos for 1080p/4k generation with Wan 1.3b
  - *From: Alisson Pereira*

- **WAN 360 LoRA** (lora)
  - Enables 360 degree character rotation for multi-view generation
  - *From: mdkb*

- **Video upscaling workflow by Pom** (workflow)
  - Exposes LoRA controls for video enhancement and upscaling
  - *From: VRGameDevGirl84(RTX 5090)*

- **ComfyUI-WarperNodes** (node)
  - Includes RAFT optical flow preprocessing node for VACE
  - *From: A.I.Warper*

- **Detail enhancer LoRA V2** (lora)
  - Sharpness and color correction LoRA, pulls towards red/orange tones
  - *From: Alisson Pereira*

- **SAM2 multi-keyframe workflow** (workflow)
  - Templates for using SAM2 with multiple keyframe points for complex masking
  - *From: Nekodificador*

- **droz_pom_vace_continue_native_ksampler_3** (workflow)
  - VACE continuation workflow
  - *From: JohnDopamine*

- **Spline Path Control tool** (tool)
  - UI for making movement control for ATI
  - *From: TK_999*

- **UltraWan LoRA V2** (lora)
  - Enhanced quality LoRA trained with Automagic optimizer on improved dataset
  - *From: Alisson Pereira*

- **Extended VACE workflow** (workflow)
  - Allows using more frames from control video in native VACE workflow, alternative to wrapper context options
  - *From: the_darkwatarus_museum*

- **Dataset maker for LoRA training** (tool)
  - Feeds video and extracts/captions sequences with emphasis on movements or actions in frames
  - *From: Impactframes.*

- **Prompt adapter system prompt** (tool)
  - System prompt for LLM-toolkit using OpenAI 4.1-mini to generate video prompts from three chronological frames
  - *From: Impactframes.*

- **Upscale workflow** (workflow)
  - Workflow for upscaling Wan outputs with various quality settings
  - *From: VRGameDevGirl84(RTX 5090)*

- **NAG implementation** (node)
  - Alternative NAG implementation for ComfyUI
  - *From: The Shadow (NYC)*

- **Upscaling workflow variations** (workflow)
  - Various upscaling methods being developed and shared
  - *From: VRGameDevGirl84(RTX 5090)*

- **Universal NAG node** (node)
  - Works with multiple models including Flux/HYV, created by Gemini Pro/Claude Opus
  - *From: JohnDopamine*

- **Tile lora workflow** (workflow)
  - Upscaling workflow using tile lora for detail enhancement
  - *From: David Snow*

- **Local LLM random prompt generator** (tool)
  - Takes text, video and audio as inspiration inputs using Qwen Omni or Qwen Instruct/Skycaptioner, can generate voice outputs for multi-talk
  - *From: Thom293*

- **SAM2 VACE workflow** (workflow)
  - Uses causvid and lora for character swapping, includes points editor for targeting objects
  - *From: mdkb*

- **Spline Path Control v2.3** (tool)
  - Advanced spline editor with multi-editing, curve editors for easing and scale, UI overhaul with dark/light themes
  - *From: Jonathan*

- **Updated tile lora upscaler workflow** (workflow)
  - Refined workflow for true upscaling that adds fine detail using tile lora with noise injection
  - *From: David Snow*

- **One-click dataset creator** (workflow)
  - Automated tool for creating single-image datasets using WAN
  - *From: burgstall*

- **Image insert node for VACE** (node)
  - Custom node that can receive image and index value to insert image at specific position in batch and replace mask
  - *From: MauroZSS*

- **Frame count adjustment node** (node)
  - Adjusts video frame counts to meet Wan2.1 requirements by rounding up and adding blank frames
  - *From: Flipping Sigmas*

- **Speaker isolation node** (node)
  - Separates multiple speakers from audio for MultiTalk processing
  - *From: manu_le_surikhate_gamer*

- **FusionX ingredients workflow** (workflow)
  - Exposes individual LoRAs from FusionX bundle for custom mixing
  - *From: VRGameDevGirl84(RTX 5090)*

- **I2V workflow with color matching** (workflow)
  - Includes color match node and optional end frame support for better I2V results
  - *From: VRGameDevGirl84*

- **VACE auto-compositing workflow** (workflow)
  - Production-quality 3D asset compositing using VACE/Wan
  - *From: Neex*
