# Wan Chatter Knowledge Base
*Extracted from Discord discussions: 2025-05-01 to 2025-06-01*


## Technical Discoveries

- **Q8 GGUF version has higher quality than fp8**
  - Despite being slower, Q8 GGUF produces better quality than fp8 version
  - *From: MilesCorban*

- **TeaCache skips conditional and unconditional steps automatically**
  - Shows skipped steps like [7, 9, 11, 13, 15, 17, 19, 21, 23] during generation
  - *From: VRGameDevGirl84(RTX 5090)*

- **SLG requires half the CFG value**
  - If using 6 CFG without SLG, use 3 CFG with SLG
  - *From: Miku*

- **Fun camera control has issues with extreme rotations**
  - Model wasn't trained with major rotational changes, tends to push beyond limits
  - *From: Kijai*

- **Fun camera control works better at 768p and higher resolution**
  - Low resolutions like 656x384 cause bad results with camera movement
  - *From: Kijai*

- **1.3B model is worse with extreme camera angles than 14B**
  - 14B can handle more extreme angles sometimes, 1.3B struggles more
  - *From: Kijai*

- **Fun 1.1 models support reference image feature**
  - New feature allows reference image input, different from start image
  - *From: Kijai*

- **LoRA effects diminish dramatically after 3 steps in v2v workflows**
  - Effects are strongest on the 2nd step, after the third step style changes into more generic AI look. Can observe this by watching preview as it samples
  - *From: David Snow*

- **Two-pass v2v technique for better stylization**
  - Stop first sampler after 3 steps, then feed to second sampler for refinement. Gets rock solid results at low step counts (6-7 steps total) with much stronger stylization
  - *From: David Snow*

- **Video Depth Anything has bad banding issues that affect VACE and Fun Control**
  - Creates hard lines/ridges in depth pass that cause wobbling artifacts in results, regular Depth Anything v2 performs better despite flickering
  - *From: Nathan Shipley*

- **LoRA training timestep distribution affects performance**
  - Sigmoid focuses on central steps for character, shift focuses on start/end for style. General consensus is shift for style, sigmoid for character
  - *From: mamad8*

- **Video Depth Anything produces banding artifacts on depth maps**
  - Creates ugly lazily-undulating banding lines on walls and gradients, where the model fixates on banding and turns them into edges in generations
  - *From: Nathan Shipley*

- **Depth Anything V2 performs better than Video Depth Anything for VACE**
  - The chattery/flickery nature of regular depth anything actually benefits generations because banding gets averaged out over generation versus being fixated on by the model
  - *From: Nathan Shipley*

- **Multiplying inverted AnyLine pass on top of depth pass helps stabilize**
  - Combining AnyLine with depth maps provides better stabilization for VACE control
  - *From: Nathan Shipley*

- **Binary thresholding at 0.5 helps VACE line art control**
  - For line art with VACE, thresholding values at 0.5 to make the map binary is really helpful
  - *From: Rishi Pandey*

- **VACE struggles with multiple control types**
  - There is so much specificity in what the control map needs to be, VACE has difficulty using multiple control types effectively
  - *From: Rishi Pandey*

- **Optical flow can be used as VACE input**
  - VACE paper shows optical flow data as input, could lead to interesting effects based on movement - no signal until something moves
  - *From: Nathan Shipley*

- **Ex LoRA enables up to 225 frames comfortably**
  - Using the extension LoRA, you can comfortably generate up to 225 frames
  - *From: Rishi Pandey*

- **DepthCrafter produces more stable results than Video Depth Anything**
  - Ranking: Depthcrafter > Video-depth-anything > depthanything V2
  - *From: David Snow*

- **Torch compile optimization works well with wan models**
  - Multiple users report successful compilation for speed improvements, though some encounter triton-related errors
  - *From: Kijai*

- **DF models can be chained for longer video generation**
  - Generate 5 second video, feed last frames to next section, drop duplicated frames and combine
  - *From: MilesCorban*

- **Wan 720p and 480p have identical generation times**
  - Testing shows no speed difference between resolutions, 720p has better prompt adherence
  - *From: N0NSens*

- **Style transfer working with WAN using new method**
  - Successfully implemented style transfer that doesn't transfer structure, works with both WAN and LTXV
  - *From: Clownshark Batwing*

- **Normal maps produce better results than depth for some workflows**
  - After extensive testing, normal maps provide additional information that improves generation quality
  - *From: David Snow*

- **WanVideoSampler has teacache support that can be controlled with use_non_blocking parameter**
  - Setting self.use_non_blocking = False in line 879 of model.py fixes CUDA runtime errors
  - *From: ZeusZeus (RTX 4090)*

- **Wan 2.1 has frame limits based on variant**
  - Vanilla has 81 frame limit before looping, Skyreels v2 540p has 97 frames, 720p has 121 frames
  - *From: N0NSens*

- **Skyreels runs at different fps than vanilla**
  - Vanilla runs at 16fps, Skyreels at 24fps, but fps is abstract and can be adjusted during output
  - *From: N0NSens*

- **Wan 2.1 context length varies by model**
  - 201 frames is the loop point for some variants, 81 is recommended chunk size
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Multiple LoRAs have merging issues in Wan**
  - When using 2 LoRAs, one often doesn't get used properly, lowering strength doesn't help
  - *From: Dream Making*

- **VACE can handle 720p resolution**
  - VACE has no problem with 720p generation when properly configured
  - *From: David Snow*

- **CausVid 14B works with 2-4 steps and cfg 1.0**
  - Single step works but 4 steps seems optimal, no CFG needed
  - *From: Kijai*

- **CausVid needs torch.compile to run**
  - Out of memory without torch.compile even with small inputs
  - *From: Kijai*

- **CausVid has flex attention support**
  - Need to set frame per block to 3 for flex attention block mask
  - *From: Kijai*

- **Setting Empty embed value to 97 fixes tensor size error**
  - Changed from 53 to 97, other Empty embeds also at 97
  - *From: Dream Making*

- **Format setting to 'Wan' auto-adjusts frames for model conditioning**
  - Will add/subtract a frame to fit the model conditionings
  - *From: Valle*

- **PyTorch 2.7.0+cu126 incompatible with xformers**
  - Need xformers-0.0.31.dev1030 for compatibility
  - *From: A.I.Warper*

- **CausVid inference is extremely fast**
  - 193 frames in 2 minutes on 4060ti, 4 steps gets 90% quality
  - *From: Vérole*

- **IPAdapter runs at 256x256 resolution**
  - Makes it hard to get enough detail for consistent character generation
  - *From: Draken*

- **Shift parameter doesn't affect CausVid**
  - Set timestep schedule ignores shift values, can use shift 1.0
  - *From: Kijai*

- **CausVid model has unusually high saturation in videos**
  - Wan base model looks better than CausVid due to saturation issues
  - *From: yi*

- **CausVid uses sliding window with kv_cache for generation**
  - Uses 3 latents in sliding window, can generate videos endlessly and show video in real time while generating
  - *From: Kijai*

- **Flex attention fixes latent flicker at beginning**
  - Uses BlockMask to have attention only attend adjacent frames in sequence dimension
  - *From: Kijai*

- **CausVid seed variation is very limited**
  - Next to no variation of seed, only way to get big changes is to change the prompt
  - *From: Cubey*

- **MoviiGen has better prompt adherence than base Wan**
  - Prompt adherence seems to be a little better with MoviiGen finetune
  - *From: yi*

- **MoviiGen LoRAs work but may need higher strength**
  - LoRAs work with MoviiGen but lora strength needs to be a little higher
  - *From: yi*

- **VACE 14B applies less frequently than 1.3B - every 5th block vs every other block**
  - 14B VACE is relatively faster than 1.3B VACE due to fewer block applications, though still slower overall due to larger size
  - *From: Kijai*

- **14B VACE works better at higher resolutions, 1.3B works better at low res**
  - 720x720 and 1024x1024 work well with 14B, while 1.3B handles lower resolutions better
  - *From: Kijai*

- **VACE can work with Causvid distilled models**
  - Successfully tested 14B VACE with Causvid for faster inference
  - *From: DawnII*

- **New VACE 1.3B final version produces sharper but less motion compared to preview**
  - Final version shows improved sharpness but reduced movement, may need setting adjustments
  - *From: multiple users*

- **VACE uses different concept than I2V - places images in latents rather than cross-attention embeds**
  - VACE is technically an extension for T2V model, not traditional I2V
  - *From: Kijai*

- **VACE can extend video infinitely using cyclical setup**
  - Generate 81 frames at a time where each video drives the next one making it smooth
  - *From: Juampab12*

- **CausVid has autoregressive capability for longer videos**
  - CausVid has autoregressive mode for actual autoregression, not just VACE extension
  - *From: DawnII*

- **VACE 14B needs higher resolution to work properly**
  - Initial impression is that 14B VACE mostly needs higher resolution - comparison shows 640x640 vs 720x720 vs 1024x1024
  - *From: Kijai*

- **MoviiGen outputs at 24fps**
  - MoviiGen is trained on cinematic data and outputs 24fps, not 16fps as initially thought
  - *From: DawnII*

- **CausVid has very low seed variation**
  - CausVid produces nearly identical outputs across different seeds with only minor differences
  - *From: TK_999*

- **CausVid can be extracted as a LoRA and works better with VACE at reduced strength**
  - CausVid extracted as LoRA rank32, works at 0.2-0.4 strength, allows VACE to work better, sweet spot around 0.2-0.4 strength
  - *From: Kijai*

- **CausVid LoRA works well at just 4 steps with CFG 1.0**
  - 4 steps appears to be sweet spot for quality vs speed, generates in ~41 seconds
  - *From: Kijai*

- **Lineart for VACE needs to be inverted**
  - When using VACE control with lineart, the input needs to be inverted
  - *From: DawnII*

- **Reference images for VACE should have white background padding and not be full frame**
  - Reference image should be background removed subject or image with white padding, not first frame
  - *From: Kijai*

- **Using masks helps with VACE consistency**
  - Masks can improve consistency issues with VACE
  - *From: DawnII*

- **Flex attention is detrimental when using reduced CausVid LoRA strength**
  - When using CausVid LoRA at reduced strength, flex attention shouldn't be used
  - *From: Kijai*

- **CausVid LoRA reduces generation time by 5x with minimal quality loss**
  - 4 steps with CausVid LoRA takes ~1 minute vs 5 minutes with usual workflow on RTX 3090
  - *From: seruva19*

- **CausVid LoRA works with both T2V and I2V models**
  - LoRA can be applied to both model types, though effectiveness on I2V not fully tested
  - *From: Kijai*

- **14B CausVid at 4 steps is faster than 1.3B at 20-30 steps**
  - Speed comparison showing 14B model with distillation outperforms 1.3B base model
  - *From: DawnII*

- **CausVid makes generations more deterministic**
  - Same prompt tends to produce similar results despite seed changes
  - *From: Ada*

- **LoRA strength affects noise quality but motion remains consistent**
  - Different strength values change visual quality but preserve motion patterns
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Combining multiple LoRAs requires higher CausVid strength**
  - When using UniAnimate + CausVid, CausVid needs 0.8-0.9 strength vs normal 0.4-0.6
  - *From: Kijai*

- **CausVid 1.3B as LoRA doesn't have the latent flashing issue at all**
  - Works better as a normal model for T2V generation compared to the full CausVid model
  - *From: Kijai*

- **14B VACE is vastly superior for reference image consistency**
  - Much better at keeping reference image fidelity compared to 1.3B version
  - *From: ˗ˏˋ⚡ˎˊ-*

- **FreSca works with CausVid at cfg 1.0**
  - Only enhancement technique that functions with CausVid, but requires lowered values to avoid noise
  - *From: Kijai*

- **VACE 14B better understands control video nuances**
  - Better at handling complex movements like legs crossing over each other, character spinning around
  - *From: A.I.Warper*

- **FP32 DWPose embeds crash ComfyUI with long UniAnimate clips**
  - Changing DWPose embeds to model dtype fixes the crashes
  - *From: Kijai*

- **VACE reference images work exceptionally well with Wan models**
  - Using reference images with VACE produces high quality results that maintain character consistency and can handle wide shots with character and scenery
  - *From: ˗ˏˋ⚡ˎˊ-*

- **VACE can do effective outpainting**
  - VACE outpainting works well and respects prompts intelligently, choosing 'union type' from inputs/prompt
  - *From: ˗ˏˋ⚡ˎˊ-*

- **CausVid LoRA should be placed after other LoRAs**
  - Placing CausVid LoRA after other LoRAs in the chain fixes blurry results
  - *From: yi*

- **Gray mask color (127,127,127 RGB or 0.5) is optimal for VACE inpainting/outpainting**
  - 0.5 gray is what VACE tries to fill, more important for inpainting and temporal masks
  - *From: Kijai*

- **VACE remembers object details well in outpainting**
  - VACE successfully remembers what objects like scooters look like when outpainting
  - *From: slmonker(5090D 32GB)*

- **Context ref works in timing dimension**
  - Context reference appears to work effectively in the timing dimension for VACE
  - *From: slmonker(5090D 32GB)*

- **CausVid LoRA works with both 1.3B and 14B models**
  - Kijai extracted CausVid LoRA for both model sizes, available on HuggingFace
  - *From: DiXiao*

- **CausVid 1.3B generates 1280x720x81 video very fast**
  - 26 seconds generation + 30 seconds VAE decoding on 4070Ti, total 56 seconds
  - *From: DiXiao*

- **CausVid inference logic is not used as intended currently**
  - The proper inference logic would be different but current implementation works, especially good combined with VACE
  - *From: ˗ˏˋ⚡ˎˊ-*

- **1.3B CausVid generates anime content particularly well**
  - User noticed significantly better anime generation quality with CausVid compared to standard 1.3B
  - *From: DiXiao*

- **Official 1.3B VACE full model available**
  - 6GB full model that doesn't require separate VACE model loading
  - *From: slmonker(5090D 32GB)*

- **Shift parameter affects background quality but not motion**
  - Shift 30 kills grass/road detail compared to shift 8, but motion remains the same
  - *From: N0NSens*

- **Causvid Lora significantly reduces generation time**
  - Cut wan time down by 30x compared to normal generation
  - *From: The Punisher*

- **Lower Causvid strength with more steps improves quality**
  - 0.25 strength at 6 steps gives incredible quality while maintaining good motion
  - *From: The Punisher*

- **Lower denoise improves motion with Causvid**
  - For i2v with causvid lora, lowering denoise to 0.75 improves movement and prompt adherence significantly
  - *From: Jonathan*

- **Inverted openpose prevents stick artifacts in VACE**
  - Haven't seen the sticks appear since switching to inverted openpose with VACE 14B
  - *From: ArtOfficial*

- **Q3_K_S GGUF VACE module works**
  - Successfully generated 400x400x49f video with Q3_k_s GGUF VACE, 6 steps, causvid lora 0.25
  - *From: artemonary*

- **GGUF VACE models work with native ComfyUI implementation**
  - Q5_K_S GGUF provides significantly better quality than Q3_K_S, working well for video generation
  - *From: The Punisher*

- **Model offloading to RAM doesn't significantly impact speed**
  - Can offload CLIP to second GPU and model to RAM without major speed penalty
  - *From: The Punisher*

- **Causvid LoRA works with GGUF models**
  - Compatible with native VACE workflow using GGUF quantized models
  - *From: The Punisher*

- **VACE reference encoding affects quality**
  - Encoding reference image separately from control improves results
  - *From: Piblarg*

- **Style transfer works better at lower resolution**
  - VACE style transfer with HiDream transfers more closely at lower res
  - *From: Clownshark Batwing*

- **Beta57 scheduler available for VACE**
  - Alternative scheduler option for VACE generation
  - *From: Clownshark Batwing*

- **Shift parameter of 2.5 works well for CausVid generations**
  - User found shift values over 15 give blurry details, need to reduce below 5, with 2.5 being solid
  - *From: Jemmo*

- **14 steps significantly improves quality over 8 steps with minimal time penalty**
  - 14 steps smooths out shimmer that appears in 8 step outputs, adds quality for small gen time increase
  - *From: CaptHook*

- **CausVid LoRA with MoviiGen model produces better results than CausVid LoRA with CausVid model**
  - Image quality much better, especially lighting and movie texture when using CausVid lora + MoviiGen model vs both CausVid components
  - *From: slmonker(5090D 32GB)*

- **Reward LoRAs fix blurry and oversaturated look of CausVid**
  - HPS and MPS reward loras improve generation quality 50-80%, both aim to improve motion and quality
  - *From: yi*

- **MoviiGen may be best model for start/end frame generation**
  - User reports it works particularly well for this use case
  - *From: DawnII*

- **Style guide videos transfer motion information better than images**
  - Using images for style guides results in stuttering, videos provide better motion transfer
  - *From: Clownshark Batwing*

- **Normal I2V workflow supports end frame input without FLF or VACE**
  - Can plug end image into normal I2V workflow and it works for first-frame-last-frame transitions
  - *From: VRGameDevGirl84(RTX 5090)*

- **VACE with T2V model can replicate I2V functionality 4x faster**
  - Using VACE workflow with start image, turning off end image, using T2V model + CausVid LoRA can achieve same I2V results but 4x faster (1min vs 4-5min generation time)
  - *From: N0NSens*

- **V2V produces very clean results**
  - Video-to-video using 0.6 denoise produces clean output quality
  - *From: ˗ˏˋ⚡ˎˊ-*

- **14B model timing performance on RTX 3090**
  - 238 seconds for 121 frames at 960x544 with 5 steps using sky14b720p+causvid, 146 seconds for 832x480 at 30 blocks
  - *From: N0NSens*

- **Depth map provides better facial movement than MediaPipe**
  - Depth preprocessing shows more facial movement transfer compared to MediaPipe face mesh
  - *From: VRGameDevGirl84(RTX 5090)*

- **Sapiens provides superior facial transfer precision**
  - Sapiens facial preprocessing is much more precise than standard media pipe face for face control
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Reference image doesn't need to match first frame**
  - VACE reference image can be completely unrelated to input video first frame, making it much more flexible than expected
  - *From: VRGameDevGirl84(RTX 5090)*

- **VACE was trained with DWPose, not MediaPipe**
  - VACE training used DWPose rather than MediaPipe for pose control
  - *From: A.I.Warper*

- **CausVid and TeaCache don't work well together**
  - Low-step CausVid workflows have issues when TeaCache is enabled
  - *From: MilesCorban*

- **Depth preprocessor works better than pose/mediapipe for facial movement in VACE**
  - Tested pose/mediapipe, facemesh, and depth - depth gets the facial movement best
  - *From: VRGameDevGirl84(RTX 5090)*

- **CausVid Lora works with Fantasy Talking for fast generation**
  - Sampling 81 frames at 720x720 with 5 steps, completed in 65.39 seconds with max VRAM usage of 21.382 GB
  - *From: VRGameDevGirl84(RTX 5090)*

- **Multiple VACE embeds can be combined using separate encoders**
  - Using depth and pose together with separate VACE embeds, but using reference image in both can cause overcooking
  - *From: VRGameDevGirl84(RTX 5090)*

- **Face landmark nodes work with WAN VACE for facial movement**
  - Face landmark detection can be used as control input, works both inverted (white on black) and non-inverted
  - *From: VRGameDevGirl84(RTX 5090)*

- **Iterative latent upscale works with VACE**
  - Video restyle with triple sampler passes using latent upscale, all at denoise 1.0, with depth and pose blend as control
  - *From: yo9o*

- **CausVid LoRA noise_aug_strength helps with movements**
  - Using noise_aug_strength at about 0.5 or more helps with movements in CausVid, though it makes output slightly blurry requiring small upscale after
  - *From: Ada*

- **CausVid shift parameter only affects sigma curve**
  - Shift parameter affects sigma curve, not CFG, so has no effect with low CFG values like 1 used with CausVid
  - *From: Kijai*

- **Inverted MediaPipe pose works for control**
  - Blending normal pose with inverted MediaPipe pose creates interesting control effects
  - *From: Vérole*

- **FP16 model with FP8 quantization uses less VRAM than native FP8**
  - FP16 model quantized to FP8 uses less VRAM than the native FP8 model (around 88% on 5090)
  - *From: ingi // SYSTMS*

- **FP32 precision dramatically improves quality**
  - Running FP16 model at FP32 precision gives insane quality, especially with T5 and VAE upcast improving prompt adherence
  - *From: ingi // SYSTMS*

- **CausVid LoRA makes 14B model viable for practical use**
  - Allows for high quality output at 4-9 steps with significant speed improvements
  - *From: David Snow*

- **Multiple VACE embeds enhance output quality**
  - Using separate embeds for pose and depth produces better results than blending them
  - *From: David Snow*

- **Single reference image works better with multiple VACE embeds**
  - When using multiple VACE encoders, using only one reference image produces better results
  - *From: ˗ˏˋ⚡ˎˊ-*

- **VACE can infer motion from masked RGB frames without control**
  - VACE appears to analyze RGB information even with simple flat masks to understand motion
  - *From: ˗ˏˋ⚡ˎˊ-*

- **TeaCache requires higher threshold values with VACE 14B CausVid setup**
  - Need threshold of 0.6+ instead of normal values, though quality may suffer
  - *From: David Snow*

- **Every 5th block disabling improves VACE pose following**
  - Disabling every 5th block when using CausVid with 14B reduces interference with VACE inputs
  - *From: DawnII*

- **VACE 14B can run on 12GB VRAM with block swapping**
  - 81 frames possible on 12GB VRAM using block swapping technique
  - *From: A.I.Warper*

- **VACE always adds 4 frames to the set frame count**
  - When setting 97 frames, it generates 101 frames. This is because latents are batches of 4, plus one for init frame
  - *From: N0NSens*

- **Normal maps work well with VACE for facial tracking**
  - Using Sapiens normal maps or NormalCrafter gives good facial tracking results at 0.9 strength
  - *From: VRGameDevGirl84(RTX 5090)*

- **CausVid LoRA works at different strengths for different use cases**
  - 0.3 strength with 12 steps or 0.6 strength with 4 steps work well. For motion with other LoRAs, 0.7 strength is better than 0.5
  - *From: CFSStudios*

- **Double control (depth + pose) produces better VACE outputs**
  - Using two VACE encode nodes with different control types (depth and pose) and compositing them together
  - *From: slmonker(5090D 32GB)*

- **Pose control works better than face mesh for character animation**
  - Testing showed pose-based control gives better results than face mesh for VACE workflows
  - *From: VRGameDevGirl84(RTX 5090)*

- **CausVid dramatically speeds up generation**
  - Using CausVid with 1280x780 reduced generation time from 30 minutes to 4 minutes
  - *From: boorayjenkins*

- **Memory optimization fix for TeaCache**
  - Fixed TeaCache using ~750MB unnecessary VRAM at 1280x780 by reversing .clone() and .to(device) operations - move to cpu first then clone
  - *From: Kijai*

- **Single frame generation with WAN T2V as image generator**
  - Can set WAN to one frame at very high resolution to use as image generator instead of loading separate models like Flux
  - *From: Thom293*

- **CFG 1.5 with SLG shows improvement over CFG 1.0**
  - 5 steps with cfg 1.5 + SLG produces better results than cfg 1.0, worth the 2x inference time
  - *From: Kijai*

- **VACE supports inpainting by using both gray area (RGB 127, 127, 127) and input mask together**
  - Fill the inpaint area with gray (127, 127, 127) in the RGB input AND provide a black/white mask where black areas are kept as-is
  - *From: Kijai*

- **VACE 14B works better with separated control and reference using two embed nodes**
  - Using separate embed nodes for control and reference images works much better with 14B model than before
  - *From: Kijai*

- **VACE takes actual composition of reference image into account**
  - The model considers the full composition and layout of the reference image, not just the subject
  - *From: Kijai*

- **CausVid LoRA dramatically improves inference speed**
  - Makes inference time bearable for 14B model
  - *From: Kijai*

- **240 frames possible on 4090 with CausVid LoRA**
  - User successfully generated 240 frames on 4090 using 14B model with CausVid LoRA, no longer needs teacache
  - *From: Cubey*

- **Character sheets work better for behind/back views**
  - Using character sheet format helps generate views of subjects from behind that wouldn't be visible in single reference
  - *From: Kijai*

- **CausVid supports very low step counts with good quality**
  - CausVid can generate videos with as few as 4 steps, with good starting point being 0.5 strength and 4 steps
  - *From: ˗ˏˋ⚡ˎˊ-*

- **CausVid strength affects step requirements**
  - Lower CausVid strength requires more steps. 0.4 with 8 steps or 0.5 with 4 steps work well
  - *From: ˗ˏˋ⚡ˎˊ-*

- **VACE inpainting requires both gray fill and mask**
  - VACE inpainting needs the area filled with gray on the color image AND also a mask - using only mask doesn't replace anything, gray only oversaturates
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Raw input frames can be used directly with reduced strength**
  - Plugging input video straight into input frames at 0.505 strength plus normal map encoder at 0.500 gives good results
  - *From: VRGameDevGirl84(RTX 5090)*

- **Normal map significantly improves VACE results**
  - Having normal map makes a big difference compared to not using it when doing direct input frame processing
  - *From: VRGameDevGirl84(RTX 5090)*

- **Context options can interfere with motion tracking**
  - Using context options with CausVid can make it not follow motion at all, removing context improved results
  - *From: VK (5080 128gb)*

- **TeaCache properly skips diffusion steps**
  - TeaCache literally skips the diffusion step and moves to the next one. You can see it working when progress jumps a step - if it doesn't jump, TeaCache isn't doing anything
  - *From: Draken*

- **VACE reference frame alignment is critical**
  - Key is setting up reference frame to be as aligned as possible. Usually you can do any 2 of: control video + reference frame + LoRA, but all three together ends up ignoring the reference frame
  - *From: Piblarg*

- **First frame restyle technique**
  - You don't need control frames in every frame - can use them to create a better starting frame that VACE will pick up on. Better to do a short run first and then use a frame from that for your longer run
  - *From: Piblarg*

- **VACE mask behavior**
  - The mask that goes into VACE works as: black = use input directly, white = controlnet mode. It's not like traditional CN masking
  - *From: Draken*

- **WAN can generate high resolution single frames**
  - WAN 14B can generate 10.48MP images (7280x1440) with good detail. Going much higher starts losing detail like the 1.3B model. Works best when fed Flux generations to guide it
  - *From: ZombieMatrix*

- **Context window generation slows down significantly**
  - 81 frames takes 2 minutes, but 200 frames with context takes 20-30 minutes
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Context window frame math must be precise**
  - Formula is (4*n)+1, so 101 frames works but 99 frames doesn't work with context window
  - *From: A.I.Warper*

- **Input video strength 0.3 loses facial details**
  - At 0.3 the input video is lost so the facial basically goes away for the most part
  - *From: VRGameDevGirl84(RTX 5090)*

- **Shift parameter affects image clarity**
  - Having any shift at all made it blurry, removing shift entirely (set to 1) improved results
  - *From: Ada*

- **Input video combined with normal map captures facial movement**
  - Using input video at 0.4 and normal at 0.6 without latent sync captured mouth movement better than other methods
  - *From: VRGameDevGirl84(RTX 5090)*

- **VACE reference image strength can be set above 1.0 with Causvid**
  - Previously setting reference strength above 1.0 caused messed up outputs, but with Causvid it works okay and helps maintain character consistency when fighting against control inputs like depth
  - *From: Johnjohn7855*

- **Separate VACE encode nodes for different control types**
  - Using two separate VACE embed nodes - one for reference image and one for depth video - allows setting different strengths for each control input
  - *From: Johnjohn7855*

- **Depth video effects start above 0.53 strength**
  - In testing, depth video control begins to have noticeable effect above 0.53 strength, becomes very strong above 0.6
  - *From: Johnjohn7855*

- **Adding depth around face helps preserve identity**
  - Adding a tiny bit of depth information around the face area helps maintain character identity better, though eyes still need consideration
  - *From: Mads Hagbarth Damsbo*

- **CFG=1 required for 4-step LoRA with standard WAN T2V**
  - When using the 4-step LoRA with standard WAN T2V, CFG must be set to 1 for proper function
  - *From: JohnDopamine*

- **Grid search for settings works better than manual tuning**
  - Doing systematic grid searches for optimal settings produces better results than trying to set parameters manually
  - *From: deleted_user_2ca1923442ba*

- **Spline editor can control VACE strength and CFG per step**
  - Both CFG and VACE strength can be scheduled/animated using spline editor functionality on a per-step basis
  - *From: Kijai*

- **Context windows loses character likeness but retains camera movement from pose data**
  - 161 frame test showed context windows implementation loses character identity but preserves camera movement even with only pose control data provided
  - *From: A.I.Warper*

- **Batching method preserves character likeness but loses camera movement**
  - Using 2x 81 frame batches keeps character identity but camera movement is lost and background gets sharper at stitching points
  - *From: A.I.Warper*

- **VACE extension causes color discoloration**
  - Video extensions using VACE show noticeable color shifts/discoloration at transition points between segments
  - *From: pom*

- **Using original input video with masking produces higher quality results**
  - Feeding original video while masking everything but the face maintains facial expressions better than other methods
  - *From: VRGameDevGirl84(RTX 5090)*

- **DWPose/ControlNet model differs from official implementation**
  - ComfyUI DWPose implementation produces different skeleton visualization compared to official HF demo, official version is cleaner with no dropped frames
  - *From: A.I.Warper*

- **VACE can do seamless video extension with overlapping frames**
  - Using overlapping frames from previous clip as input to next clip creates seamless transitions with minimal visible seams
  - *From: seitanism*

- **VAE encoding/decoding causes color shifts in video extensions**
  - Using extracted frames from compressed MP4 causes color shifts, but using lossless PNGs directly from VAE decode avoids this issue
  - *From: seitanism*

- **CausVid LoRA at strength 1.0 with 4 steps gives very fast generation**
  - 85 frames at 1024x576 generated in 150 seconds on RTX 5090
  - *From: VRGameDevGirl84(RTX 5090)*

- **System RAM can be used as shared VRAM for longer videos**
  - A5000 24GB with 128GB RAM can generate 300-450 frames using shared virtual GPU memory
  - *From: Guey.KhalaMari*

- **Wan 14B model significantly better than 1.3B for understanding complex objects like full length dresses**
  - Same settings and seed produced fake-looking results on 1.3B but realistic results on 14B
  - *From: traxxas25*

- **VACE reference image concatenates multiple images into single image automatically**
  - If you feed VACE a batch of images as reference, it concatenates them under the hood into a single image
  - *From: Kijai*

- **CausVid works with VACE and Fun Control modules**
  - CausVid LoRA is compatible with VACE for T2V but not I2V, and works with Fun Control
  - *From: deleted_user_2ca1923442ba*

- **Phantom model supports up to 3-4 reference images unlike VACE**
  - Phantom can use multiple reference images, different from VACE's single image limitation
  - *From: Kijai*

- **VACE minimum frame requirement for proper reference image usage**
  - Single frame doesn't work well with VACE reference images, need at least 5 frames for proper results
  - *From: Kijai*

- **VACE face change using pose transition**
  - Modified the pose transition code to control the timing of the appearance of poses that do not exist in the preceding image
  - *From: toyxyz*

- **VACE inpainting works with single encode**
  - Successfully achieved inpainting by overlaying mid grey mask over video footage, but multi encode with dwpose degrades video quality
  - *From: David Snow*

- **Seamless looping achievable with Wan**
  - Generated video that loops seamlessly using separate workflow processing
  - *From: The Shadow (NYC)*

- **Style transfer from reference image**
  - Used cartoon frog in suit prompt with reference image, style came from the reference image automatically
  - *From: David Snow*

- **Body correction in pose interpolation**
  - Added body correction to interpolate poses while maintaining body shape for more natural transitions
  - *From: toyxyz*

- **Long video generation with overlapping batches**
  - Created system that breaks reference video into batches with overlaps for arbitrary length videos, but colors drift over time becoming crispier
  - *From: notid*

- **CausVid LoRA works with Base VACE GGUF**
  - Sample workflow available on HuggingFace
  - *From: AshmoTV*

- **Context options node works for extending videos to thousands of frames**
  - Can generate videos with thousands of frames using context options node connected to context options socket
  - *From: David Snow*

- **Motion blur understanding in first frames**
  - Model understands context so well that it preserves motion blur from reference images in generated output
  - *From: David Snow*

- **CausVid LoRA stabilizes chaotic LoRAs but has tranquilizing effect**
  - Makes chaotic LoRAs more stable but reduces expressiveness of well-working LoRAs, likely due to low CFG
  - *From: hablaba*

- **ComfyUI has built-in batch processing for videos**
  - Video load and combine nodes have a built-in batch feature that can process long videos in chunks (e.g., 80 frames at a time), restart with next batch, and combine at the end
  - *From: VRGameDevGirl84(RTX 5090)*

- **VACE control video empty frames should be gray, not white**
  - For VACE extension, control video empty frames should be gray value 0.5 (127, 127, 127), mask should be correct
  - *From: Kijai*

- **CausVid LoRA strength affects VACE control**
  - Too high CausVid LoRA strength reduces VACE control strength. Above 0.4 strength prevented mouth movement
  - *From: Kijai*

- **AccVideo scheduler works as a standalone feature**
  - Uses 10 actual steps when set to 50, works with cfg 1.0, timestamps: [1000.0000, 977.8983, 951.5095, 919.4528, 879.6821, 829.0320, 762.3315, 670.5145, 536.1040, 320.5109]
  - *From: Kijai*

- **Color shift in VACE can be addressed with frame blending**
  - Overlapping frames can be cross-faded to reduce seams, occurs over 16 frame overlap
  - *From: Piblarg*

- **Wan can generate lip sync motion when prompted with 'talking'**
  - Even in v2v without audio input, prompting talking makes mouth move
  - *From: VRGameDevGirl84(RTX 5090)*

- **CausVid with Florence find and replace works well for v2v**
  - User found this combination effective for video-to-video generation
  - *From: hicho*

- **AccVid LoRA can be combined with CausVid LoRA**
  - Users successfully combined CausVid 0.15 + AccVid 0.5, and another user merged CausVid/AccVid at 0.5 strength each
  - *From: ▲, JohnDopamine*

- **VACE works with single encode using multiple control inputs**
  - Expanded mask, depth, normals and pose can all be fed into a single VACE encode node and it works
  - *From: David Snow*

- **Context options work with 14B but have issues with 1.3B**
  - Context options for longer videos work fine with 14B model but don't work properly with 1.3B model
  - *From: N0NSens*

- **AccVid LoRA works better at higher strengths**
  - AccVid LoRA works well at 1.7 strength with 6 steps, and at 1.0 strength for regular use
  - *From: Kijai, 🦙rishappi*

- **Wan LoRAs trained on images work with video generation**
  - LoRA trained with 60 images on CivitAI works effectively with Wan 14B T2V model
  - *From: VRGameDevGirl84(RTX 5090)*

- **Phantom 14B model released**
  - Available on HuggingFace, not quantized so download all safetensors files
  - *From: DawnII*

- **VACE can work with Phantom models**
  - Phantom gets the references and VACE module gets other preprocessors
  - *From: DawnII*

- **AccVid LoRA speeds up rendering**
  - Can be used with CausVid LoRA for faster inference
  - *From: Johnjohn7855*

- **Mediapipe face mesh needs cropping for better face detection**
  - Crop and paste faces, then process with mediapipe and crop back
  - *From: Valle*

- **TeaCache skips specific steps during sampling**
  - TeaCache skipped 16 conditional, unconditional, and prediction_2 steps at positions [7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37]
  - *From: Kijai*

- **CausVid works better with more steps on Phantom**
  - CausVid at 0.3 strength starts working much better with more steps, there's hope
  - *From: Kijai*

- **Phantom can take up to 4 reference images**
  - You can give it up to 4 images for reference
  - *From: Kijai*

- **VACE input + Phantom ref preserves identity better**
  - VACE input (no ref) + phantom ref works and identity is preserved much better than vace ref
  - *From: Zuko*

- **480p works better than 720p for some cases**
  - 480p got basically every detail right with the hairs, seems we're supposed to use this in 480p not 720p
  - *From: aikitoria*

- **Official specs suggest 121 frames at 24fps**
  - Papers suggest 121 frames at 24fps instead of 81 frames
  - *From: aikitoria*

- **Quality improves significantly over 81 frames**
  - Quality definitely improved over 81 frames when using 121 frames
  - *From: Kijai*

- **CausVid causes flicker at strength 1.0**
  - 1.0 CausVid causes that flicker issue like always
  - *From: Kijai*

- **Phantom sometimes fails to render multiple characters**
  - Phantom keeps failing and only rendering one of the 2 characters sometimes
  - *From: aikitoria*

- **Reference latents appear in preview**
  - References are in the latents, same with VACE, causing flashing in preview
  - *From: Kijai*

- **Phantom works with reference latents for T2V**
  - It's a T2V model that takes in reference latents, not pure T2V
  - *From: Kijai*

- **SageAttention significantly speeds up Phantom**
  - Makes Phantom about twice as fast when installed in same venv
  - *From: aikitoria*

- **Phantom requires 121 frames and 24 fps**
  - Old workflows work but need changing to 121 frames and 24 fps
  - *From: aikitoria*

- **Multiple encoders allow individual strength control**
  - Can use separate encoders for control video, ref image, and input video with individual strength settings
  - *From: VRGameDevGirl84(RTX 5090)*

- **MMA Audio frame rate conversion workaround**
  - Wan generates 16fps, MMAudio requires 24fps - custom setup needed to avoid generating sound for only 3 out of 5 seconds
  - *From: Mngbg*

- **Using first 3 blocks at reduced strength eliminates CausVid flash**
  - Kijai found that not applying CausVid LoRA to first 3 blocks gets rid of flash, even at full strength on remaining blocks
  - *From: Kijai*

- **First block at 0.5 strength also eliminates flash**
  - Reducing just the first block to 0.5 strength removes the CausVid flash issue
  - *From: Kijai*

- **CausVid loses strength without first block**
  - When first block is disabled, CausVid significantly loses its effectiveness and may need compensation with CFG or more steps
  - *From: Kijai*

- **bf16 gives same results as fp16 but with more artifacts**
  - Testing showed bf16 produces basically identical results to fp16 but introduces additional artifacts
  - *From: aikitoria*

- **fp32 is 4x slower than fp16, not 2x as expected**
  - Running at fp32 precision resulted in 4x performance hit instead of expected 2x
  - *From: aikitoria*

- **Using euler scheduler gets rid of black noise**
  - Euler scheduler eliminates black noise issues with Wan models
  - *From: Kijai*

- **CausVid with all blocks but first works better**
  - Applying CausVid on all blocks except the first gives better results than including first block
  - *From: Kijai*

- **Phantom works with four images of same subject**
  - Can use four reference images to cover different angles of a single subject (face, back of jacket, etc.)
  - *From: David Snow*

- **32 frame overlap greatly improves context videos**
  - Using 32 frame context overlap produces much better results than default settings
  - *From: Nekodificador*

- **MoviiGen LoRA acts like a detailer**
  - Adds minor details and helps clean up noise, making outputs cleaner, but can affect character likeness
  - *From: Johnjohn7855*

- **Phantom 14B works better with 3+ subjects than 1.3B**
  - 14B model handles multiple subjects more effectively than the 1.3B variant
  - *From: DawnII*

- **Phantom can be combined with VACE for inpainting**
  - Phantom character consistency can be used together with VACE inpainting capabilities
  - *From: David Snow*

- **Uni3C works with any video with camera motion**
  - Can use any video with camera movement, not just depth-processed videos, as control input
  - *From: N0NSens*

- **Phantom cfg at 1.0 doesn't capture likeness well**
  - Using cfg 1.0 with phantom reduces likeness accuracy, especially with well-known faces
  - *From: ZeusZeus (RTX 4090)*

- **Adding original video input at low denoise improves face detection**
  - Using wan video encode node with input video at 0.85 denoise helps model understand where character's face is located
  - *From: David Snow*

- **VACE masks should be grayscale format**
  - VACE expects mask videos in grayscale format for proper inpainting
  - *From: David Snow*

- **Input video at 0.3 strength significantly helps mouth movement**
  - Adding original video as input at 0.3 strength in separate encoder improves mouth animation compared to no input
  - *From: VRGameDevGirl84(RTX 5090)*

- **Overlaying pose on mask works better than separate VACE encodes**
  - Combining pose control with inpaint mask in single encode gives better results than using multiple VACE encodes
  - *From: David Snow*

- **Block swapping doesn't work with Uni3C controlnet**
  - VRAM management works but block swapping causes issues with Uni3C
  - *From: mamad8*

- **Inpainting works with the triple sample workflow**
  - User confirmed inpainting functionality works well with the triple sample workflow
  - *From: hau*

- **Uni3C can rotate subjects**
  - User discovered Uni3C has rotation capabilities for subjects in video
  - *From: hau*

- **Uni3C requires similar subject sizes between input image and control video**
  - For Uni3C to work well, the subjects in the input image and control video need to be similar in size
  - *From: toyxyz*

- **First Frame Last Frame model prefers Chinese prompts**
  - Wan FLF2V model prefers prompts in Chinese because that's how it was trained
  - *From: Guey.KhalaMari*

- **WanVideoWrapper supports skip layer guidance**
  - The wrapper includes SLG arguments support
  - *From: hau*

- **Phantom 14B is trained on more frames**
  - Phantom 14B doesn't have the 81 frame limit that applies to other models
  - *From: DawnII*

- **1.3B Phantom + VACE works fine vs 14B issues**
  - 1.3b phantom+vace works fine, suggesting issues with 14b vace may be related to lower block application
  - *From: DawnII*

- **VACE + Phantom inpainting works by cutting VACE early and masking original input latents**
  - Cut VACE at 0.8 strength and stop at 0.2, mask both the input latents (with blurred mask) and VACE input frames (with hard edges)
  - *From: Zuko*

- **PerpNegGuider works well with Phantom using negative_img_text as empty negative**
  - Feed normal negative and negative_img_text to PerpNegGuider, neg_scale controls how far from actual image embedding while retaining subject context
  - *From: Ablejones*

- **Phantom works better with Chinese prompts**
  - Model was trained mostly with Chinese, adheres better to Chinese prompts than English
  - *From: DawnII*

- **Character LoRAs trained on T2V work only 30% with Phantom**
  - T2V LoRAs have limited compatibility with Phantom model
  - *From: ZeusZeus*

- **CausVid LoRA helps most when not applied to first block or applied at max 0.5 to first block**
  - Rest of blocks can be 1.0 strength, but first block should be reduced or disabled
  - *From: Kijai*

- **CausVid includes CFG distillation and should use CFG 1.0**
  - Both CausVid and AccVid distillation includes cfg distillation so they'd use 1.0, which is same as disabled
  - *From: Kijai*

- **CFG can be used for certain steps with distilled models**
  - It's possible to use cfg only for certain steps, which works pretty well too
  - *From: Kijai*

- **First few steps with CFG most impactful**
  - CFG is most impactful at early steps
  - *From: Kijai*

- **CausVid v2 works better with CFG**
  - The new version works better with cfg indeed
  - *From: Kijai*

- **Shift less than 1.0 has positive effect for 14B model**
  - The main thing I learned is that shift less than 1 has a very positive effect. but only for model 14b
  - *From: Mngbg*

- **Florence is very powerful with Wan**
  - florence is very powerful with wan - works great for detailed prompts
  - *From: hicho*

- **Character description text fixes consistency**
  - Its this description text that fixes the character consistency - the model wants to have a description of each ref image every time
  - *From: AJO*

- **CausVid v2 at strength above 1.0 with CFG works best**
  - You could also try the v2 with strength above 1.0 tho, and with some cfg it's probably best
  - *From: Kijai*

- **CausVid v2 can be used at full strength (1.0) without destroying motion in normal T2V and doesn't have the flash**
  - Major improvement over previous versions that required lower strengths
  - *From: Kijai*

- **CausVid v2 already has block 0 removed**
  - No need for manual block removal node when using v2
  - *From: Kijai*

- **ATI model released with trajectory control functionality**
  - New ByteDance model supporting trajectory-based motion control with anchor points
  - *From: JohnDopamine*

- **Phantom is faster than VACE for similar results**
  - VACE: 738.22 seconds vs Phantom: 253.29 seconds
  - *From: VRGameDevGirl84(RTX 5090)*

- **FP8 quantized Phantom gives half the generation time compared to FP16**
  - Significant speed improvement with FP8 version
  - *From: AJO*

- **Wan LoRAs work with Phantom model**
  - LoRAs trained for Wan 14B T2V are compatible with Phantom model
  - *From: VRGameDevGirl84(RTX 5090)*

- **LoRAs can be merged at strength 1.0 successfully**
  - Multiple LoRAs (CausVid V2, Phantom, detail enhancers) can be merged at full strength 1.0 to create custom models
  - *From: VRGameDevGirl84(RTX 5090)*

- **CausVid V2 provides significant speed improvements**
  - New CausVid V2 makes generation much faster compared to previous versions
  - *From: VRGameDevGirl84(RTX 5090)*

- **Multiple reference images supported in Phantom**
  - You can bring in as many reference images as you want and they can all be of different things (person, background, objects)
  - *From: VRGameDevGirl84(RTX 5090)*

- **Reference image quality significantly affects output**
  - The quality and type of reference image makes a huge difference on the quality of the ending result
  - *From: VRGameDevGirl84(RTX 5090)*

- **Merged models work without needing separate LoRAs**
  - Successfully merged Phantom, CausVid V2, MoviiGen, and detail LoRAs into single model that produces same quality as stacked LoRAs
  - *From: VRGameDevGirl84(RTX 5090)*

- **CausVid v2 was tuned on T2V and requires CFG >1 with scheduling for 1 step out of 8 total steps**
  - Kijai mentioned that v2 needs different settings than v1, with cfg more than 1 and scheduled for 1 step
  - *From: Johnjohn7855*

- **Film grain can reduce reactor jitter**
  - Adding film grain after reactor processing helps reduce jitter artifacts, especially around eyes and mouth
  - *From: Johnjohn7855*

- **VACE works with Normal Craft normal maps but not all normal map types**
  - Normal Craft works well, Sapients one works but not as well. VACE not trained on normals but can work to some extent
  - *From: VRGameDevGirl84(RTX 5090)*

- **Wan VAE should never require tiling with 24GB VRAM**
  - Kijai states the Wan VAE literally never needs tiling
  - *From: Kijai*

- **ATI requires 121 points even for 81 frames**
  - Setting 121 points prevents cutting off the end, even when doing 81 frames
  - *From: Kijai*

- **Single track in ATI usually does camera motion only**
  - Need anchor points that don't move to avoid just camera motion
  - *From: Kijai*


## Troubleshooting & Solutions

- **Problem:** Context windows change input image when frames exceed 81
  - **Solution:** Each window needs an image or this happens when it doesn't get it
  - *From: Kijai*

- **Problem:** RuntimeError about tensor size mismatch
  - **Solution:** Issue with expanded size of tensor (1024) vs existing size (1198)
  - *From: Dream Making*

- **Problem:** Steps value randomly changing to different numbers
  - **Solution:** Mouse mishap or node updates shifting field values
  - *From: ingi // SYSTMS*

- **Problem:** Computer crashes when running on GPU2 vs GPU1
  - **Solution:** Try switching power cables, avoid splitter cables that come in box
  - *From: ingi // SYSTMS*

- **Problem:** Skeleton lines appearing in VACE control renders
  - **Solution:** Increase strength to 1.0, though may be situation specific
  - *From: David Snow*

- **Problem:** Strange colors and artifacts with Kijai's node vs native
  - **Solution:** Use CFG 3 with SLG, keep denoise at 1.0 for T2V
  - *From: Miku*

- **Problem:** Grid pixel glitch patterns in videos
  - **Solution:** Try Euler/beta scheduler instead of uni_pc, increase step count from too low values, test 81 frames without context loops to isolate issues
  - *From: chrisd0073*

- **Problem:** DG models prone to flashing
  - **Solution:** Higher version DG models more flash prone, use stock versions as they're closest to base 1.3B. It's an ongoing issue with stronger models
  - *From: David Snow*

- **Problem:** VAE flashing and artifacts in v2v
  - **Solution:** Usually cfg or step count issue, increasing shift strengthens style but also increases burn - eternal balancing act
  - *From: David Snow*

- **Problem:** Eyes don't follow/move properly in face videos
  - **Solution:** Run through LivePortrait afterwards, or use Runway Act One for lip sync. Fun-control somewhat better for eye following but has other issues
  - *From: David Snow*

- **Problem:** VACE tries to recreate input video instead of inpainting
  - **Solution:** Need to inpaint the first frame and pass it as guide - the inpainted first frame should have subject removed and area around inpainting should be gray
  - *From: ArtOfficial*

- **Problem:** Blurry or pixelated results with Wan Fun workflows
  - **Solution:** Remove batched CFG - never gotten good results from that
  - *From: Colin*

- **Problem:** Flickering artifacts in long generations
  - **Solution:** Change both schedulers to uni pc and remove all experimental args
  - *From: Flipping Sigmas*

- **Problem:** ComfyUI node disconnection glitch
  - **Solution:** Happens when disconnecting nodes - they appear disconnected but still function as connected. More common in Opera browser, less in Chrome
  - *From: Flipping Sigmas*

- **Problem:** Kijai had problems with Blender depth maps
  - **Solution:** Had to blur high quality Blender depth maps because VACE was likely trained on DepthAnything V2 outputs
  - *From: David Snow*

- **Problem:** FP8 not supported on RTX 3090
  - **Solution:** Disable FP8 in model loader settings, change value to disable compilation
  - *From: Juan Gea*

- **Problem:** Triton bundler os.replace error on Windows
  - **Solution:** Change line 268 in triton_bundler.py from os.replace to os.rename
  - *From: Faust-SiN*

- **Problem:** CUDA invalid argument error with LoRAs
  - **Solution:** Disable torch compile, teacache, and SLG nodes - issue appears to be permissions/triton related
  - *From: ZeusZeus (RTX 4090)*

- **Problem:** VHS node loading issues after ComfyUI update
  - **Solution:** Delete VHS custom node folder and git pull fresh copy instead of using manager
  - *From: TK_999*

- **Problem:** Ubuntu 24.04 compatibility issues with CUDA
  - **Solution:** Downgrade to Ubuntu 22.04 or properly install Nvidia CUDA toolkit
  - *From: UsamaAhmedKhan*

- **Problem:** GIMM-VFI node segfaults with torch compile
  - **Solution:** Disable torch_compile in DownloadAndLoadGIMMVFIModel
  - *From: gshawn*

- **Problem:** Block swap causing CUDA errors
  - **Solution:** Switch to VRAM Management node instead of Block swap node
  - *From: Colin*

- **Problem:** CUDA error: invalid argument with WanVideoWrapper
  - **Solution:** Set self.use_non_blocking = False in line 879 of model.py
  - *From: ZeusZeus (RTX 4090)*

- **Problem:** TeaCache causing CUDA runtime errors
  - **Solution:** Issue is RAM-related, non_blocking reserves more RAM. Need more than 32GB RAM or use auto_cpu_offload
  - *From: Kijai*

- **Problem:** Low system memory preventing TeaCache use
  - **Solution:** Use 'auto_cpu_offload' setting on wrapper, it's better for RAM but slower
  - *From: Draken*

- **Problem:** Slow generation times on 3090 Ti
  - **Solution:** Use optimizations - native ComfyUI has fewer options than wrapper
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Problem:** Depthcrafter resolution mismatch with NormalCrafter
  - **Solution:** Make other preprocessors conform to Depthcrafter's multiple of 64 requirement
  - *From: David Snow*

- **Problem:** OOM errors with DepthAnything node
  - **Solution:** Set depth anything node to fp16 instead of fp32
  - *From: A.I.Warper*

- **Problem:** VACE generating different character appearance
  - **Solution:** Add start frame twice to beginning with no mask, or train a character LoRA
  - *From: TimHannan*

- **Problem:** Runpod disk allocation issues
  - **Solution:** Check container disk limit - 20GB default is too small, increase to 80-100GB
  - *From: chrisd0073*

- **Problem:** RuntimeError: tensor size mismatch (14) vs (17)
  - **Solution:** Set Empty embed value to 97 instead of 53
  - *From: Dream Making*

- **Problem:** xformers incompatibility with PyTorch 2.7.0
  - **Solution:** pip install --pre xformers or use xformers-0.0.31.dev1030
  - *From: A.I.Warper*

- **Problem:** LBM model asking for SDXL base model download
  - **Solution:** Check HF token setup in config file
  - *From: slmonker*

- **Problem:** CausVid FloatTensor/cuda.FloatTensor type mismatch
  - **Solution:** Use native wrapper instead of WAN wrapper
  - *From: MilesCorban*

- **Problem:** Artifacts/glitch at beginning of CausVid videos
  - **Solution:** Remove first 8 frames from generated output
  - *From: Vérole*

- **Problem:** CFG 3.5 burns CausVid output
  - **Solution:** Use CFG 1.0 or no CFG
  - *From: Kijai*

- **Problem:** TAEW preview bugging out after node update
  - **Solution:** Change to latent2rgb preview
  - *From: Kijai*

- **Problem:** 9 steps gives garbage results with CausVid
  - **Solution:** Use 3 steps instead of 9 steps
  - *From: Kijai*

- **Problem:** CausVid has blocking artifacts
  - **Solution:** No current fix available
  - *From: yi*

- **Problem:** Triton CUDA version error (12.8 < 10.0)
  - **Solution:** May need to reinstall triton-windows, use without compile option
  - *From: Juampab12*

- **Problem:** Blurry results with MoviiGen using TEAcache
  - **Solution:** Turn off teacache
  - *From: slmonker(5090D 32GB)*

- **Problem:** 14B VACE shows 'vace_blocks.8.modulation' error
  - **Solution:** Need to update wrapper, 14B uses different blocks than 1.3B and won't work out of box
  - *From: Kijai*

- **Problem:** Static frames when using VACE for I2V
  - **Solution:** Don't use I2V nodes with VACE, use VACE nodes directly and connect start frame only
  - *From: multiple users*

- **Problem:** Cannot load VACE module in model loader
  - **Solution:** VACE module is not a full model - load base model in model loader, VACE module goes in VACE video select node
  - *From: Kijai*

- **Problem:** 14B native nodes don't work yet
  - **Solution:** 14B uses different blocks, only works with wrapper currently, 1.3B works with native nodes
  - *From: Kijai*

- **Problem:** Flex attention doesn't work with VACE currently
  - **Solution:** Use SDPA instead when running VACE
  - *From: Kijai*

- **Problem:** RTX 4080 16GB getting OOM errors even at 480x480 resolution
  - **Solution:** Change vace_blocks_to_swap to 8 (not 35), select proper model quantization
  - *From: DawnII*

- **Problem:** Random noise output instead of video
  - **Solution:** Disable enhance_a_video node or lower its value to 2
  - *From: Hashu*

- **Problem:** Video turns green and ControlNet pose visible in output with VACE 14B
  - **Solution:** Must use T2V model, not I2V model with VACE
  - *From: Kijai*

- **Problem:** Workflow stuck at 0% on RTX 5090
  - **Solution:** Use block swap node even with high-end GPUs, swap at least 1 VACE block
  - *From: Kijai*

- **Problem:** OpenPose visible in VACE output
  - **Solution:** Lower strength/start/end percent values when using multiple VACE encodes
  - *From: David Snow*

- **Problem:** CausVid + VACE compatibility issues
  - **Solution:** Update nodes to latest version for 14B VACE compatibility
  - *From: Kijai*

- **Problem:** VACE consistency issues with flickering between reference images
  - **Solution:** Use white background padding on reference images, try turning off WanVideo TeaCache, use masks for better consistency
  - *From: Kijai*

- **Problem:** Canny always showing up as outlines in VACE output when blending with depth
  - **Solution:** Blur the depth map to prevent VACE from going into colorization mode, blurring controlnet conditions helps in general
  - *From: Kijai*

- **Problem:** High contrast and plasticky output with CausVid
  - **Solution:** Use CFG 1.0 and steps <9, softer colors require more steps with low-step methods
  - *From: DawnII*

- **Problem:** Block swap error appearing randomly
  - **Solution:** Set non-blocking off when swapping blocks, though this slows things down
  - *From: Stad*

- **Problem:** VACE Module 14B not working
  - **Solution:** Need clean install, git pull wasn't enough
  - *From: ZRNR*

- **Problem:** OOM with CausVid LoRA
  - **Solution:** Use low VRAM load option on the LoRA loader
  - *From: Kijai*

- **Problem:** Messy results with CausVid
  - **Solution:** Use CFG 1.0, disable everything related to CFG, disable teacache
  - *From: Kijai*

- **Problem:** Slow prompt changes taking 5+ minutes
  - **Solution:** Use fp8 text encoder or increase system RAM (32GB not enough for 14B)
  - *From: Kijai*

- **Problem:** OOM on 3090 with 14B model
  - **Solution:** Enable fp8 quantization in settings even if model is already fp8, use block swap to 30-40
  - *From: Kijai*

- **Problem:** Reference fading over time in DF
  - **Solution:** Reference only fed to first sampler in DF, use prefix_samples input instead of VACE encode
  - *From: DawnII*

- **Problem:** VACE outpainting giving bogus results
  - **Solution:** Outpaint area should be gray not white, only the mask should be white
  - *From: Kijai*

- **Problem:** Flickering with CausVid LoRA
  - **Solution:** Apply block edit node to CausVid LoRA to skip VACE blocks
  - *From: seruva19*

- **Problem:** Artifacts at high CausVid strength
  - **Solution:** Lower CausVid strength to 0.5-0.6 and increase steps to 6
  - *From: Jonathan*

- **Problem:** VACE 14B outpainting issues with color changes
  - **Solution:** Use T2V model instead of I2V model, and use WAN text encoder instead of native encoder
  - *From: Stad*

- **Problem:** Hair strands not moving with CausVid LoRA
  - **Solution:** Lower LoRA strength to 0.3, and disable LoRA for VACE blocks
  - *From: Kijai*

- **Problem:** Context node causing blurred frames at end of batches
  - **Solution:** Copy entire node pack for next 81 frames using final frame from run 1 as ref for run 2
  - *From: A.I.Warper*

- **Problem:** Memory overflow with CausVid LoRA + I2V model setup
  - **Solution:** Issue identified but no solution provided
  - *From: N0NSens*

- **Problem:** Getting static results with CausVid
  - **Solution:** Turn off WanVideo Experimental Args nodes for 1.3B model
  - *From: Mngbg*

- **Problem:** OOM errors when running CausVid + VACE14B repeatedly
  - **Solution:** Use 'Clear VRAM Used' node between sampler and VAE decode, restart ComfyUI between runs, or lower block swap values
  - *From: The Punisher*

- **Problem:** Artifacts and pose rigs appearing in output
  - **Solution:** Disable all enhancements like TeaCache, SLG - use only torchcompile/model/lora
  - *From: aipmaster*

- **Problem:** Don't use TeaCache with CausVid
  - **Solution:** TeaCache causes issues with CausVid, disable it
  - *From: DawnII*

- **Problem:** VACE doesn't work well with multiple combined controls
  - **Solution:** Separate depth and pose into different VACE encoders, don't combine depth and pose controls
  - *From: DawnII*

- **Problem:** RAM errors with Wan 14B on 16GB VRAM
  - **Solution:** Disable non-blocking transfer if using blockswap, use quantized text encoders, swap fewer blocks
  - *From: Kijai*

- **Problem:** CausVid giving blurry results
  - **Solution:** Use 0.5-1 LoRA strength, 4-6 steps, place CausVid LoRA after other LoRAs
  - *From: DawnII*

- **Problem:** MediaPipe-FaceMeshPreprocessor error after ComfyUI update
  - **Solution:** Downgrade mediapipe version or reinstall via pip
  - *From: Mads Hagbarth Damsbo*

- **Problem:** CausVid LoRA produces blurry/fogged output with base Wan14B
  - **Solution:** Use CFG1, disable TeaCache, SLG, and other enhancements. Set shift to 5 instead of default
  - *From: Fawks*

- **Problem:** CausVid LoRA doesn't play well with other LoRAs
  - **Solution:** Load CausVid last and use higher strength to compensate, or disable other LoRAs first
  - *From: DawnII*

- **Problem:** Marigold v2 nodes require diffusers>=0.28 error
  - **Solution:** Check requirements file - error message contains incorrect required version
  - *From: Mngbg*

- **Problem:** CausVid 14B T2V produces bad results with latent hitching
  - **Solution:** More common issue with Caus 14B, try different settings or use with VACE instead
  - *From: DawnII*

- **Problem:** ComfyUI nightly memory management issues
  - **Solution:** Models not unloading correctly, block swapping not working. Roll back to earlier commit
  - *From: The Punisher*

- **Problem:** VACE reference image latent appearing at beginning of video
  - **Solution:** Check that video length matches number of frames - issue was video shorter than frame count
  - *From: ArtOfficial*

- **Problem:** Running out of system RAM with blockswap
  - **Solution:** Add 8GB swap memory - everything runs smoothly without noticeable slowdown
  - *From: Captain of the Dishwasher*

- **Problem:** VACE controls revealing preprocessor artifacts
  - **Solution:** Don't combine multiple controls like depth + pose in single pass, use separate VACE embed nodes chained with prev_embeds input
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Problem:** V2V with ControlNet and Causvid 4 steps produces poor outputs
  - **Solution:** Increase to 6 steps for better results
  - *From: The Punisher*

- **Problem:** Weird lines appearing in generated video
  - **Solution:** Likely a settings issue, Q5_K_S GGUF resolved the problem
  - *From: The Punisher*

- **Problem:** LoRA key errors when using Fun LoRAs
  - **Solution:** Error occurs when using Fun LoRAs on non-Fun models, but LoRAs still work
  - *From: David Snow*

- **Problem:** 14B VACE crashes inconsistently on 4090
  - **Solution:** Memory leak suspected, use lower max image size/frames or quantization
  - *From: hablaba*

- **Problem:** Reference image heavily ignored in VACE
  - **Solution:** Reference image needs same resolution as video, use padding of 128 then resize
  - *From: DennisM*

- **Problem:** ComfyUI crash with 14B fp8
  - **Solution:** Set quantization to fp8_e4 to match the model, use 45 block swap (40 base + 5 VACE)
  - *From: DawnII*

- **Problem:** Native VACE serious OOM issues even with offloading
  - **Solution:** Use wrapper for better VRAM management, or switch to GGUF models
  - *From: Draken*

- **Problem:** OOM errors on 3060 12GB with 14B model
  - **Solution:** Enable tiled VAE, use block swap to offload to RAM, reduce resolution
  - *From: Kijai*

- **Problem:** GGUF giving noised unfinished output with 4 steps
  - **Solution:** Set CFG to 1, update ComfyUI to nightly, use correct LoRA (14B vs 1.3B)
  - *From: The Punisher*

- **Problem:** Control pose not working in VACE
  - **Solution:** Use inverted lineart instead of control pose, because lineart alone doesn't work in VACE
  - *From: Nokai*

- **Problem:** Wrong connections in VACE workflow
  - **Solution:** Control input should go to control_video, not reference. Both bones and start/end frames go in control input
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Problem:** Sharp artificial edges in CausVid generations
  - **Solution:** Lower denoising to 0.75 can add motion and reduce artificial look
  - *From: JohnDopamine*

- **Problem:** RuntimeError: No frames generated
  - **Solution:** Check skip_first_frame parameter - if it's higher than video length it causes this error. Set to 0 or disconnect the input. Also set frame_load_cap to 0 or 81
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Problem:** Mushy output with CausVid LoRA
  - **Solution:** Ensure CFG is set to 1.0, turn off TeaCache and SLG enhancers, use CausVid LoRA strength 0.3-0.6
  - *From: zelgo_*

- **Problem:** Context option causing 'No frames generated' error
  - **Solution:** Disable context option when using input video with fewer than 81 frames
  - *From: DeZoomer*

- **Problem:** Wrong text encoder error 'tensor size mismatch'
  - **Solution:** Use correct text encoder - umt5-xxl for T2V workflows, or use ComfyUI native encoder with bridge node
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Problem:** Slow LoRA loading (15+ minutes)
  - **Solution:** Likely hardware issue with disk - check SMART status using CrystalDiskInfo, consider disk cleanup if 85%+ full
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Problem:** VACE patch not being recognized in custom node
  - **Solution:** Model state dict may be modified correctly but sampler doesn't understand it's VACE - shows 'WAN21' instead of 'WAN21_vace'
  - *From: The Punisher*

- **Problem:** Yellow tinted video outputs in VACE
  - **Solution:** Issue resolved by using proper depth preprocessing instead of DepthCrafter node which was too VRAM intensive for RTX 3090
  - *From: BestWind*

- **Problem:** Reference frame appearing at end/beginning of inpainting video
  - **Solution:** Use frame trimming node to remove extra reference frames from output
  - *From: JohnDopamine*

- **Problem:** Poor quality results with CausVid
  - **Solution:** Disable TeaCache when using CausVid workflows, especially low-step ones
  - *From: MilesCorban*

- **Problem:** Copy-paste in ComfyUI not preserving connections
  - **Solution:** Known issue after recent ComfyUI update affecting multiple users
  - *From: VRGameDevGirl84(RTX 5090)*

- **Problem:** Poor generation quality
  - **Solution:** High CFG values (like 12) can cause poor results, use lower CFG
  - *From: Dream Making*

- **Problem:** Sapiens requiring unsafe checkpoint loading
  - **Solution:** Need to use comfyui-unsafe-torch custom node to disable security for Sapiens models
  - *From: MilesCorban*

- **Problem:** 'WanModel' object has no attribute 'vace_patch_embedding' error
  - **Solution:** Use T2V base model instead of I2V - VACE only works with T2V models
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Problem:** ValueError: You are attempting to load a VACE module as a WanVideo model
  - **Solution:** Load VACE module in the vace_model input, not the main model loader. Use matching T2V base model
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Problem:** RuntimeError: tensor size mismatch (20250 vs 21060)
  - **Solution:** Check input resizing - must be divisible by 16
  - *From: Kijai*

- **Problem:** Combined VACE processors causing oversaturated/cooked results
  - **Solution:** Use blank/grey reference image for second embed, reduce strength on second encoder, don't use reference image in multiple encoders
  - *From: VRGameDevGirl84(RTX 5090)*

- **Problem:** HiDream cache clearing during WAN inference
  - **Solution:** Delete ComfyUI-HiDream-Sampler folder from custom_nodes and restart ComfyUI
  - *From: 100a*

- **Problem:** CausVid not following reference or control properly
  - **Solution:** Use classic WAN T2V 14B model with CausVid lora, not the full CausVid model
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Problem:** VACE model select node not updating
  - **Solution:** Update wrapper nodes using git commands: cd to ComfyUI-WanVideoWrapper, git checkout main, git fetch, git pull
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Problem:** Video getting dark at end with CausVid
  - **Solution:** Problem was end_latent_strength set to 0, fixing this resolved the darkening issue
  - *From: DiXiao*

- **Problem:** OOM with depth crafter
  - **Solution:** Downscale input to 768 longest side before running through depthcrafter
  - *From: David Snow*

- **Problem:** Xformers compatibility error after update
  - **Solution:** Need correct xformers version 0.0.30 for pytorch 2.7.0+cu126, install with specific wheel or pip install xformers --index-url https://download.pytorch.org/whl/cu124
  - *From: David Snow*

- **Problem:** xformers installation failure
  - **Solution:** Download xformers wheel file and install manually with pip: python -m pip install xformers-0.0.30-cp312-cp312-win_amd64.whl
  - *From: David Snow*

- **Problem:** VACE overlaying pose skeletons on output video
  - **Solution:** Use two separate encoders - first with pose at strength 1, second with depth at strength 0.5, remove ref image from second encoder
  - *From: Boop*

- **Problem:** Video deformations with DOF scenes
  - **Solution:** Remove diorama/DOF references from prompt or add explicit DOF description, or create images without DOF and add in post
  - *From: DevouredBeef*

- **Problem:** Context window artifacts
  - **Solution:** User reports no luck with context_window but shows it working without window
  - *From: N0NSens*

- **Problem:** SapiensLoader weights loading error
  - **Solution:** Check Ultralytics version in Git repo for compatibility issues
  - *From: zelgo_*

- **Problem:** VACE control failed at editing cuts while Fun was ok
  - **Solution:** Switch to Fun Control for handling video cuts
  - *From: N0NSens*

- **Problem:** Sapiens nodes not loading into ComfyUI
  - **Solution:** Check Github page about incompatibility with ultralytics 8.3.41
  - *From: Valle*

- **Problem:** VACE overloading memory with 14B + CausVid
  - **Solution:** Reduce CausVid LoRA strength to at least half, or use specific blocks
  - *From: Kijai*

- **Problem:** Depth map appearing in output instead of reference image
  - **Solution:** First encoder should be pose strength 1, second encoder depth strength 0.5, no reference image in depth encoder
  - *From: VRGameDevGirl84(RTX 5090)*

- **Problem:** UniPC creating visible noise with CausVid
  - **Solution:** Use Euler sampler for cleaner results, though it has ghost-like effects
  - *From: N0NSens*

- **Problem:** VACE doesn't work with I2V models
  - **Solution:** Don't use the VACE module at all if loading i2v model - VACE only works with T2V models
  - *From: DawnII*

- **Problem:** WAN wrapper nodes not loading/updating
  - **Solution:** Uninstall bitsandbytes - it's the triton import that diffusers does when bitsandbytes is installed that causes loading failures
  - *From: Kijai*

- **Problem:** ComfyUI desktop version auto-updates causing crashes
  - **Solution:** Don't use desktop version for production work - use separate instances with symlinks, one for careful updates and one for daily updates
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Problem:** VACE with CausVid on skyreels looks like noise
  - **Solution:** Switch to T2V model instead of I2V when using VACE - skyreels I2V is incompatible with VACE
  - *From: DawnII*

- **Problem:** Points Editor limitations - can't remove first/last points
  - **Solution:** Click 'new canvas' to reset to single point, or work within the constraint that you can't delete first or last points
  - *From: Kijai*

- **Problem:** VACE inpainting not working with just mask input
  - **Solution:** Use both gray-filled RGB input (127, 127, 127 in inpaint area) AND input mask together
  - *From: Kijai*

- **Problem:** Blurred masks don't work for inpainting in VACE
  - **Solution:** Keep mask sharp but expanded rather than blurred
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Problem:** Over-saturation in VACE output
  - **Solution:** Use input mask to avoid saturation issues
  - *From: Kijai*

- **Problem:** Can't get exact poses without controlnets in Hidream
  - **Solution:** Use non-full denoise or switch back to Flux for specific pose control
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Problem:** Third VACE embed has no effect
  - **Solution:** Likely limitation in wrapper code rather than model
  - *From: Kijai*

- **Problem:** Block swap node causing errors
  - **Solution:** Run off the bottom 'non_blocking' input of block swap node, or bypass if swapping zero blocks
  - *From: ArtOfficial*

- **Problem:** ComfyUI browser freezing
  - **Solution:** Sometimes fake-frozen - minimize and bring browser back up to fix, or happens when adding too many video combine nodes
  - *From: TK_999*

- **Problem:** OOM at high resolutions
  - **Solution:** Try 40 blocks to swap for high resolution generations like 1280x720
  - *From: Valle*

- **Problem:** Context options causing crashes
  - **Solution:** Error with WanVideo Context Options causing ComfyUI crashes with IndexKernel assertion failed
  - *From: MilesCorban*

- **Problem:** TeaCache with CausVid low steps
  - **Solution:** Turn off teacache when using CausVid since low steps mess up the video, though some report it working at 8 steps
  - *From: MilesCorban*

- **Problem:** RTX 5090 crashing at max resolution
  - **Solution:** Setting enable_vae_tiling to True stopped crashes
  - *From: AJO*

- **Problem:** More than 2 VACEs not working properly
  - **Solution:** Fixed bug where prev embeds were reset between nodes, so only the 2nd to last was being added
  - *From: Kijai*

- **Problem:** MultiGPU tensor device mismatch
  - **Solution:** Expected all tensors to be on same device error - need to follow stack trace and cast tensor to right device
  - *From: Kijai*

- **Problem:** Noisy output
  - **Solution:** Higher resolution, 2nd refine pass, or both can reduce noise
  - *From: N0NSens*

- **Problem:** Depth map masking issues
  - **Solution:** Trying to mask depth map areas gives human with no head or literal depth image blended with normal human
  - *From: Draken*

- **Problem:** Memory allocation issues when changing resolution
  - **Solution:** Enable block swapping with higher values (try 30 for 4090)
  - *From: VRGameDevGirl84(RTX 5090)*

- **Problem:** Size mismatch errors when changing aspect ratio
  - **Solution:** Ensure all num_frames values match everywhere and use frame_count output from load video node
  - *From: A.I.Warper*

- **Problem:** GGUF models not working correctly
  - **Solution:** Hard-coded stuff prevents GGUF from working properly, but VACE GGUF versions on HuggingFace work fine in native
  - *From: The Punisher*

- **Problem:** Lora strength reduced with CausVid
  - **Solution:** Use WanVideo CFG Schedule node to bring back intended lora look while still speeding up process
  - *From: Zlikwid*

- **Problem:** VACE node input missing in newest version
  - **Solution:** Downgrade to older version of the node - newer version has input but no node to feed it
  - *From: MilesCorban*

- **Problem:** UniAnimate giving 'Got 5D input, but bilinear mode needs 4D input' error
  - **Solution:** Use VACE embed node instead of encode node for proper functionality
  - *From: Kijai*

- **Problem:** Spline editor error when attaching to manage VACE strength
  - **Solution:** Update to nightly version of nodes, set points to sample to number of steps being used
  - *From: Kijai*

- **Problem:** Depth control overpowering reference image
  - **Solution:** Use separate VACE embed nodes with different strengths - reference image at higher strength, depth at lower strength
  - *From: Johnjohn7855*

- **Problem:** Reference image losing influence with higher steps/shift
  - **Solution:** Lower shift value first (try shift 4 instead of 8), then adjust other parameters
  - *From: Johnjohn7855*

- **Problem:** UniAnimate pose detection failing
  - **Solution:** Use 512x768 dimensions, generate neutral A-pose version of character, set score threshold to 0 if needed
  - *From: Guey.KhalaMari*

- **Problem:** MP4 output losing alpha channel
  - **Solution:** Delete the alpha layer as MP4 format doesn't support alpha channels
  - *From: Valle*

- **Problem:** Pose control not working with spinning dress/complex clothing
  - **Solution:** Manually draw pose in Photoshop or overlay pose on top of A-pose as workaround
  - *From: Guey.KhalaMari*

- **Problem:** CFG float error when starting at 0.7 percent
  - **Solution:** IndexError: list index out of range in teacache_state processing
  - *From: DawnII*

- **Problem:** VACE FaceReference node struggles with identity at glancing angles
  - **Solution:** Node tends to fail at non-frontal face angles, has limitations with pose variations
  - *From: Mads Hagbarth Damsbo*

- **Problem:** Pose processor failing to detect stylized characters
  - **Solution:** Consider manually placing DW pose bones over reference image to get coordinates and remap
  - *From: A.I.Warper*

- **Problem:** Color degradation in video extensions
  - **Solution:** Isolate problematic batch and color correct before doing 2nd pass cleanup
  - *From: A.I.Warper*

- **Problem:** Memory errors on previously working configurations
  - **Solution:** Possible shadow updates to nodes causing OOM issues, restart ComfyUI
  - *From: Cubey*

- **Problem:** CUDA error: invalid argument on A100 80GB
  - **Solution:** Issue was insufficient RAM - everything offloads by default eating lots of RAM. Can disable offloading by using main_device as load device and disabling force_offload
  - *From: Kijai*

- **Problem:** VHS_SelectImages error with 'Index '74None80' must be an integer'
  - **Solution:** Update ComfyUI - this happens when frontend package version is behind the workflow version
  - *From: JohnDopamine*

- **Problem:** Double VACE Encode with Context Options fails without reference image
  - **Solution:** Known issue that Kijai hasn't accounted for yet
  - *From: Kijai*

- **Problem:** CppCompileError with Chroma model
  - **Solution:** Disable Torch Compile nodes, especially if using workflows with compile functionality
  - *From: MilesCorban*

- **Problem:** Halo edge ringing effect in Wan/MoviGen outputs
  - **Solution:** Too high CFG can cause structured/HDR look with edge sharpening artifacts
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Problem:** VACE not following reference image
  - **Solution:** Canny edge detection should be inverted for VACE, use Kijai's WanVideoWrapper instead of native nodes
  - *From: Kijai*

- **Problem:** CausVid + TeaCache compatibility issues
  - **Solution:** TeaCache skips steps while CausVid optimizes steps - they don't pair well and TeaCache uses more VRAM with CausVid
  - *From: Cubey*

- **Problem:** WanVideoWrapper installation failing with cmake/sentencepiece errors
  - **Solution:** Use VS 2017, check if using correct Python version (portable is 3.12 now), do git pull to update repository
  - *From: Cubey*

- **Problem:** Reference image losing face likeness with full body shots
  - **Solution:** Split clothing and face reference images separately rather than using single full body reference
  - *From: AJO*

- **Problem:** CLIP text encode taking majority of generation time
  - **Solution:** Force offload the main model using model_to_offload input, likely memory related issue
  - *From: Kijai*

- **Problem:** Node inputs greyed out
  - **Solution:** GGUF nodes need updating, restart ComfyUI to resolve
  - *From: Kijai*

- **Problem:** Multi encode inpainting quality issues
  - **Solution:** Avoid using multiple encodes simultaneously, stick to single encode for better results
  - *From: David Snow*

- **Problem:** RAM usage not clearing after model unload
  - **Solution:** Python/ComfyUI memory management issue, Framepack can use 50GB RAM while model is only 16GB
  - *From: Draken*

- **Problem:** Context issues with 275 frames
  - **Solution:** Tried with full input image and isolated, same problem persists
  - *From: N0NSens*

- **Problem:** Video combine node saving unwanted PNG
  - **Solution:** PNG saved for lighter workflow storage, modify node code or request feature from maintainer
  - *From: MilesCorban*

- **Problem:** Flashing artifacts on first frames of videos
  - **Solution:** Remove first few frames using TrimVideoLatent node or Get Image/Mask Range from Batch node
  - *From: David Snow*

- **Problem:** WSL2 CUDA out of memory errors when same workflow works in Windows
  - **Solution:** Disable use_non_blocking on block swap node, use fp8 quantization, and configure .wslconfig properly
  - *From: Kijai*

- **Problem:** Color changes ruining transitions between video clips
  - **Solution:** Use same 15 frames for end of one video and beginning of next for seamless transition
  - *From: Piblarg*

- **Problem:** VACE 1.3B not working with context options
  - **Solution:** Context options works fine with 14B but may have issues with 1.3B models
  - *From: N0NSens*

- **Problem:** TypeError: only integer tensors of a single element can be converted to an index
  - **Solution:** Roll back to previous version of WanVideoWrapper - latest update may have broken compatibility with certain workflows
  - *From: VRGameDevGirl84(RTX 5090)*

- **Problem:** CUDA out of memory with multi-key frames
  - **Solution:** Total number of frames from Pad Image Batch Interleaved must match total frames being loaded (frame load cap), and disable block swap for small frame counts
  - *From: jerms_ai_(4090_24g)*

- **Problem:** Follow your emoji not working in VACE
  - **Solution:** Try reducing CausVid LoRA strength to 0.4 or below, and increase VACE strength to 1.2 to balance it out
  - *From: Kijai*

- **Problem:** VACE 14B model loading error
  - **Solution:** Load normal WAN model in loader, then hook the VACE module using the 'vace_model' output from the loader. Update wrapper nodes if getting compatibility errors
  - *From: Draken*

- **Problem:** ComfyUI crashing with memory issues
  - **Solution:** Never use bf16 if you have memory issues - use fp8 models, set nodes to fp16, and use native text encoder that runs on fp8
  - *From: hicho*

- **Problem:** Ghost pose appearing in generations when using multiple control inputs
  - **Solution:** Each control net needs its own encoder, can't blend them through single encoder
  - *From: VRGameDevGirl84(RTX 5090)*

- **Problem:** AccVideo scheduler gives step error with denoise under 1.0
  - **Solution:** It won't work with denoise under 1.0 because it's taken from 50 steps
  - *From: Kijai*

- **Problem:** Color shift and degradation when using last frame as reference
  - **Solution:** Image quality degrades each batch because taking from Wan output repeatedly lowers quality
  - *From: VRGameDevGirl84(RTX 5090)*

- **Problem:** Teacache (KJNodes) gives error with AccVideo weight
  - **Solution:** Known compatibility issue, no solution provided
  - *From: yi*

- **Problem:** OOM errors during sampling
  - **Solution:** Lower resolution/length, increase block swapping (higher numbers), use tiled VAE. Set blocks so VRAM usage is 96-98%, not 99%
  - *From: N0NSens, JohnDopamine*

- **Problem:** AccVid disabled torch.compile for 10 days
  - **Solution:** Re-enable torch.compile for better performance
  - *From: Kijai*

- **Problem:** CausVid artifacts in first frames
  - **Solution:** Use fp8 and new AccVid model, CausVid artifacts happen because it uses different sampling method
  - *From: hicho, Kijai*

- **Problem:** Background noise in CausVid generations
  - **Solution:** Try working workflows, adjust settings properly
  - *From: MisterMango, VRGameDevGirl84(RTX 5090)*

- **Problem:** Canny outlines appearing in longer generations
  - **Solution:** Check control video matches ref image, lower controlnet strength from 0.8, avoid blending with other controlnets
  - *From: enigmatic_e, VRGameDevGirl84(RTX 5090)*

- **Problem:** Invalid credentials in Authorization header for HuggingFace
  - **Solution:** Export HUGGING_FACE_HUB_TOKEN="your_token_here" or use huggingface-cli login
  - *From: jerms_ai_(4090_24g)*

- **Problem:** Black background when inpainting
  - **Solution:** Check mask setup - mask should be white box on black background for area to inpaint
  - *From: Johnjohn7855*

- **Problem:** Eyes being added to character wearing sunglasses
  - **Solution:** Turn off 'detect face' in DWPose if you don't need facial movements
  - *From: ingi // SYSTMS*

- **Problem:** Wrong T5 encoder causing garbage VACE results
  - **Solution:** Use umt5-xxl-enc-bf16.safetensors with wrapper, not umt5_xxl_fp16.safetensors from native
  - *From: aikitoria*

- **Problem:** TeaCache skipping generation on subsequent runs
  - **Solution:** Issue acknowledged, first generation works but subsequent ones skip main sampler
  - *From: thebaker*

- **Problem:** RuntimeError: Input type (CUDABFloat16Type) and weight type (CPUBFloat16Type) mismatch
  - **Solution:** T5 encoder must be run on GPU, not CPU
  - *From: mamad8*

- **Problem:** Chattery tiled noise all over foreground/background
  - **Solution:** Up sampling steps, reduce TeaCache threshold, or use slower input if using VACE
  - *From: zelgo_*

- **Problem:** VACE default shift too low causing artifacts
  - **Solution:** Use VACE default shift of 16 instead of lower values
  - *From: Kijai*

- **Problem:** Flashes of noise at beginning with Phantom + VACE
  - **Solution:** Lower the strength of VACE embeds for the video input
  - *From: Johnjohn7855*

- **Problem:** VACE color shifts
  - **Solution:** Use color match node as partial solution, or prompt for specific colors
  - *From: David Snow*

- **Problem:** Mask appearing at beginning of VACE inpainting
  - **Solution:** Lower the strength of VACE embeds for the video input
  - *From: Johnjohn7855*

- **Problem:** Mouth movement continues after character stops talking
  - **Solution:** Works better with close-up shots, far away shots make accurate lip sync difficult
  - *From: VRGameDevGirl84(RTX 5090)*

- **Problem:** Video flicker in random frames
  - **Solution:** Issue being investigated, may be related to reference image usage or sampler settings
  - *From: humangirltotally*

- **Problem:** Phantom only shows one character sometimes
  - **Solution:** More clearly describe that there are two characters in prompt for better reliability
  - *From: aikitoria*

- **Problem:** SageAttention build failing
  - **Solution:** Use --no-build-isolation flag and ensure building in same venv as torch
  - *From: aikitoria*

- **Problem:** CausVid flash at beginning of videos
  - **Solution:** Use LoRA block selection to reduce first block strength to 0.5 or disable first 3 blocks entirely
  - *From: Kijai*

- **Problem:** RuntimeError: mat1 and mat2 shapes cannot be multiplied (512x768 and 4096x1536)
  - **Solution:** Check text encoder model - likely have wrong T5 text encoder selected
  - *From: Kijai*

- **Problem:** Mask showing up as frame in phantom+vace inpainting
  - **Solution:** Try using empty prompt or very short prompts, long prompts can cause flash issues
  - *From: pom*

- **Problem:** ValueError type fp8e4nv not supported with compile
  - **Solution:** Change to e5m2 format - older nvidia GPUs don't support compile with e4m3fn
  - *From: Kijai*

- **Problem:** ComfyUI crashes when using Phantom + VACE
  - **Solution:** Usually caused by running out of RAM, check RAM usage at crash moment
  - *From: Kijai*

- **Problem:** Context windows breaking at 81+ frames
  - **Solution:** Disable context options for higher frame counts
  - *From: Valle*

- **Problem:** Flashing with Phantom setup
  - **Solution:** Add LoRA block edit with block 0 turned off, or lower CausVid to 0.4
  - *From: David Snow*

- **Problem:** Characters constantly talking in Phantom
  - **Solution:** Add 'talking' or 'conversation' to negative prompt, avoid 'not talking' in positive
  - *From: Johnjohn7855*

- **Problem:** Tensor dimension errors with Uni3C
  - **Solution:** Check that input video and output resolution dimensions match
  - *From: N0NSens*

- **Problem:** MoviiGen LoRA causing flashes
  - **Solution:** Flash comes from MoviiGen, turning off block 0 doesn't help, lower strength instead
  - *From: N0NSens*

- **Problem:** OOM error when encoding 1024x576 video with 33 frames on 5090
  - **Solution:** VHS video loader node not properly resizing or capping frames - use KJ resize node v2 and cap at 33 frames
  - *From: Kijai*

- **Problem:** Skip first frames in VHS node unreliable
  - **Solution:** Often gives wrong part of video, use alternative frame selection methods
  - *From: David Snow*

- **Problem:** Expected scalar type Half but found Float error with Uni3C
  - **Solution:** Block swapping doesn't work with Uni3C, use VRAM management instead
  - *From: mamad8*

- **Problem:** Uni3C taking 277 s/it at 480p on 3090
  - **Solution:** Performance issue confirmed but no specific solution provided
  - *From: sneako1234*

- **Problem:** WebP format doesn't work well with Phantom
  - **Solution:** Convert to other image formats for better results
  - *From: DawnII*

- **Problem:** Tensor error with Uni3C: sizes must match except dimension 1
  - **Solution:** May occur when using mixed control with 1.3B models, 14B models don't have this issue
  - *From: N0NSens*

- **Problem:** Wan sampler outputs slightly different resolution than specified
  - **Solution:** Issue is likely due to VAE (/16) - specifying 480x980 results in 480x976 output
  - *From: hau*

- **Problem:** Block swapping causing half and float error with Uni3C
  - **Solution:** Enable quantization to fix the block swapping issue
  - *From: mamad8*

- **Problem:** Wrong Uni3C controlnet model causing bias error
  - **Solution:** Use Kijai's modified version: Wan21_Uni3C_controlnet_fp16.safetensors instead of the original ewrfcas version
  - *From: Kijai*

- **Problem:** 14B depth controlnet stalling and not using VRAM
  - **Solution:** Switch from offload device to main device - device mismatch was causing the stall
  - *From: David Snow*

- **Problem:** ComfyUI-IPAdapterWAN project completely ineffective
  - **Solution:** Project is fundamentally broken and creator closed it after issue report
  - *From: slmonker(5090D 32GB)*

- **Problem:** Phantom losing mouth movements in V2V
  - **Solution:** Use crop&stitch node to maintain consistent face size, and lower denoising to 0.10-0.15 to preserve motion
  - *From: DeZoomer*

- **Problem:** FILM VFI doubling frames causing generation failure
  - **Solution:** Use get image or masked range from batch to cut out every other frame
  - *From: David Snow*

- **Problem:** Grey flashes when using anchor/starting frames with VACE
  - **Solution:** Appears to be related to morphing transformations, may need camera control or pose/depth map interpolation
  - *From: pom*

- **Problem:** SamplerCustomAdvanced doesn't behave same as ClownSharkSampler with PerpNegGuider
  - **Solution:** Use SharkSampler instead of SamplerCustomAdvanced for consistent results
  - *From: Ablejones*

- **Problem:** Phantom inconsistent character and clothing consistency
  - **Solution:** Use detailed prompts describing each reference image, crop head-only for face ref, crop below-neck for outfit ref
  - *From: AJO*

- **Problem:** GGUF Phantom has weird noise artifacts with CausVid
  - **Solution:** Use fp8 instead of GGUF Q8 for better compatibility with CausVid
  - *From: hicho*

- **Problem:** Ladder reappearing in inpainting longer videos
  - **Solution:** Remove ladder from first frame reference image, use pose control of original video back to VACE
  - *From: Johnjohn7855*

- **Problem:** Phantom CFG causes 3x slower generation
  - **Solution:** Use main CFG 1.0 to disable phantom CFG
  - *From: Kijai*

- **Problem:** CausVid causes flash in first frames
  - **Solution:** Use CausVid lora with first block disabled or the v2 version
  - *From: Kijai*

- **Problem:** CFG scheduling node errors with non-zero start percent
  - **Solution:** Use manual list or spline editor for complex CFG scheduling
  - *From: Kijai*

- **Problem:** Gemini nodes broken by ComfyUI core update
  - **Solution:** ComfyUI Core released paid Gemini version with same node names, custom node maker needs to change names
  - *From: AJO*

- **Problem:** Color saturation issues with VACE continuations
  - **Solution:** Prompt for specific colors to offset saturation issues
  - *From: pom*

- **Problem:** WSL loading transformer parameters extremely slow
  - **Solution:** WSL RAM allocation issues - need to edit config to give more RAM
  - *From: MilesCorban*

- **Problem:** CausVid v2 causing over-saturation when combined with high CFG
  - **Solution:** Lower CFG from 5 to avoid burning/over-saturation, use CFG 5 only for first step
  - *From: Kijai*

- **Problem:** Reactor face swap causing flickery eyes and stuttery motion
  - **Solution:** Changed to codeformer v1, but still produces less quality than original
  - *From: AJO*

- **Problem:** Permission error with triton backends on 5090
  - **Solution:** Reboot recommended, though didn't solve in this case
  - *From: JohnDopamine*

- **Problem:** CausVid v2 not working well with AccVid
  - **Solution:** User reverted to v1.5, may need different parameter combinations
  - *From: Johnjohn7855*

- **Problem:** OOM errors at higher resolutions
  - **Solution:** Add block swapping - works for 1280x720 with 5 blocks swapped
  - *From: VRGameDevGirl84(RTX 5090)*

- **Problem:** Getting storage sense warnings
  - **Solution:** Delete unwanted merged models to manage disk space - video models consume lots of storage
  - *From: Thom293*

- **Problem:** Reactor causes jitter around face features
  - **Solution:** Use film grain after reactor processing, or composite only the face part back using masks
  - *From: Johnjohn7855*

- **Problem:** ATI crashes with wrong dimensions
  - **Solution:** Ensure dimensions are divisible by 16 (e.g., 608 not 600)
  - *From: Kijai*

- **Problem:** Blender depth maps too detailed for VACE
  - **Solution:** Add 1 pixel blur to make them work as depth
  - *From: Kijai*

- **Problem:** Out of memory when using CausVid LoRa
  - **Solution:** Disable non-blocking on block swap, use fp8 text encoder
  - *From: Kijai*

- **Problem:** CUDA error on 5090 with runpod template
  - **Solution:** Triton may not support nvfp4 yet, try using unsupported model settings
  - *From: TK_999*

- **Problem:** Fp8_e4m3fn doesn't work with compile on RTX 3000 series causing triton/tensor errors
  - **Solution:** Use fp8_e5m2 format instead or don't use compile
  - *From: Kijai*

- **Problem:** Tensor error with frame processing
  - **Solution:** Check that image size is divisible by 16 and verify correct number of frames from source video
  - *From: TK_999*

- **Problem:** Significant facial changes in VACE animated videos
  - **Solution:** Make reference image match start frame position, avoid using uncropped image as both character reference and background, or interpolate position. Also check depth map matches if using depth control
  - *From: Piblarg*

- **Problem:** Green artifacts appear when model fails to track movement
  - **Solution:** Model goes green when it gets no trajectory points - ensure you have enough points for all frames
  - *From: Kijai*


## Model Comparisons

- **FantasyTalker vs Omnihuman lip sync**
  - Omnihuman is much better for lip sync quality
  - *From: Kytra*

- **VACE vs Fun Control**
  - VACE is better but more random, Fun Control bad when movement hard to detect
  - *From: Dream Making*

- **1.3B vs 14B Fun Control quality**
  - 14B is much better quality, notable jump from Fun 1.0 to 1.1 for 1.3B
  - *From: Nathan Shipley*

- **Q8 GGUF vs fp8 quality**
  - Q8 GGUF higher quality despite slower speed
  - *From: MilesCorban*

- **LTX vs Fun camera control**
  - LTX better for static scenes - 9sec/gen 1280x720 vs 1min+ for Fun 832x480
  - *From: N0NSens*

- **DPM++ vs UniPC with DG models**
  - Outputs look almost identical, DPM++ has ever so slight edge on detail
  - *From: David Snow*

- **Higher vs lower DG model versions**
  - Need stronger versions for more stylization, but stronger models introduce more flashes - exercise in frustration
  - *From: David Snow*

- **Video Depth Anything vs Depth Anything v2**
  - Regular Depth Anything v2 performs better despite flickering, Video Depth Anything has bad banding that causes artifacts
  - *From: Nathan Shipley*

- **VACE 1.1 vs control video**
  - 1.1 is more forgiving than VACE, but control video has huge impact on style retention
  - *From: Rishi Pandey*

- **Fun vs VACE for multiple control types**
  - Fun better for combining multiple control inputs, VACE struggles with specificity requirements
  - *From: Rishi Pandey*

- **FramePack vs Wan DiffusionForcing**
  - FramePack faster than wan and handles scene shifts better than DF, but lacks control options
  - *From: Draken*

- **HunyuanVideo vs Wan for control**
  - If HY had anything close to vace, no one would be talking about WAN - main issue with HY has always been control
  - *From: Draken*

- **Wan Fun vs AnimDiff**
  - 1.3B is miles better than animdiff - things don't morph over time, far more consistent especially for v2v. But for abstract stuff and creativity, animdiff is better
  - *From: David Snow*

- **Wan 720p vanilla vs Sky variants**
  - 720p Sky at 832x480 has better prompt following than vanilla, Sky 540p has worst quality
  - *From: N0NSens*

- **14B vs 1.3B LoRA compatibility**
  - No compatibility between 1.3B and 14B models, but 1.3B LoRAs should work with 1.3DF
  - *From: MilesCorban*

- **Phantom vs Skyreels vs VACE vs Hunyuan Custom**
  - Still prefer Phantom, Skyreels, or VACE over Hunyuan custom
  - *From: slmonker(5090D 32GB)*

- **14B vs 1.3B Wan models**
  - 14B is ungodly slow, 5B model more exciting for practical use
  - *From: David Snow*

- **VACE vs LTX 13B for I2V**
  - LTX 13B gives great results in fraction of the time compared to VACE
  - *From: David Snow*

- **Higher parameter models for LoRA training**
  - High param count makes LoRA training easier - Flux can learn in 60 steps unprecedented before
  - *From: deleted_user_2ca1923442ba*

- **Desktop vs Portable ComfyUI**
  - Portable recommended - desktop version has fewer users for support and limited module installation options
  - *From: David Snow*

- **CausVid 14B vs regular Wan 14B**
  - CausVid is much faster (3 steps vs standard) but has quality trade-offs
  - *From: Kijai*

- **Wan 1.3B vs LTXV quality**
  - LTXV is better quality than 1.3B Wan, but 14B Wan beats LTXV at 5x slower speed
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Skyreels i2v vs Wan2.1-Fun-V1.1-1.3B-InP**
  - Fun-V1.1 was better, Skyreels was a flop
  - *From: Ada*

- **4 steps vs 9 steps CausVid**
  - 4 steps gets 90% of quality, 9 steps unnecessary
  - *From: yi*

- **CausVid vs Wan base**
  - Wan base looks way better due to CausVid's high saturation issues
  - *From: yi*

- **3 steps vs 9 steps CausVid**
  - Both look like 1.3b not 14b, 9 steps gives garbage results
  - *From: slmonker(5090D 32GB)*

- **VACE 1.3B vs 14B benchmarks**
  - 1.3B often performs better than 14B even for depth, unless you want 720p
  - *From: Juampab12*

- **Full finetunes vs LoRAs**
  - Full finetunes can be higher quality but can also unlearn and fragment ecosystem
  - *From: yi*

- **VACE final vs preview 1.3B**
  - Final is sharper but has less movement, preview may be better for some use cases
  - *From: David Snow*

- **1.3B vs 14B VACE**
  - 14B works better at higher resolutions, 1.3B sufficient for controlled generation
  - *From: Juampab12*

- **Causvid performance with VACE**
  - Causvid working well with VACE, producing good results in fewer steps
  - *From: DawnII*

- **VACE 1.3B vs 14B quality**
  - Not much difference except 14B works better at higher resolutions like 720p
  - *From: Valle*

- **MoviiGen vs CausVid**
  - Different purposes - CausVid is lower step, MoviiGen is finetune on cinematographic shots
  - *From: ˗ˏˋ⚡ˎˊ-*

- **DG Wan boost vs base model**
  - DG version is smoother with less obvious morphing, can do 6-8 steps instead of 20-30
  - *From: David Snow*

- **1024x576 vs 1280x720 with VACE 1.3B**
  - 1024x576 seems to have more charm for style
  - *From: David Snow*

- **CausVid as full model vs LoRA**
  - LoRA version allows VACE compatibility and better control at reduced strength
  - *From: Kijai*

- **VACE vs FLF2V (First Last Frame To Video)**
  - VACE seems to do a better job than FLF2V
  - *From: DawnII*

- **14B CausVid vs 1.3B VACE quality**
  - 14B with CausVid is close to 1.3B quality wise but much faster
  - *From: ˗ˏˋ⚡ˎˊ-*

- **CausVid vs normal workflow speed**
  - 5x speedup - 1 minute vs 5 minutes on RTX 3090 for same quality
  - *From: seruva19*

- **VACE DF vs VACE with context**
  - Context windows more viable with CausVid due to speed, reference works across context windows
  - *From: Kijai*

- **4 step CausVid LoRA vs 20 steps normal**
  - CausVid is order of magnitude faster - 94 seconds vs very long time
  - *From: A.I.Warper*

- **14B CausVid vs 1.3B speed**
  - 14B CausVid faster by a landslide, order of magnitude faster
  - *From: A.I.Warper*

- **4 step CausVid vs 8 step David's workflow**
  - CausVid much faster: 10min vs 300s for same quality
  - *From: DawnII*

- **VACE 1.3B vs 14B for reference consistency**
  - 14B vastly superior for reference image fidelity
  - *From: ˗ˏˋ⚡ˎˊ-*

- **LTX vs WAN speed**
  - LTX still much faster but WAN better quality for specific use cases
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Wan vs AnimateDiff replacement**
  - AnimateDiff still has its own style which is good, Wan doesn't completely replace it
  - *From: Piblarg*

- **HiDream vs Flux for reference images**
  - A.I.Warper personally prefers HiDream over Flux
  - *From: A.I.Warper*

- **CausVid 1.3B vs 14B**
  - 14B listens to prompts much better than 1.3B but has degradation over time
  - *From: N0NSens*

- **Bidirectional vs Causal CausVid**
  - Bidirectional attends to past and future frames, causal only attends to past frames (LLM-like)
  - *From: deleted_user_2ca1923442ba*

- **1.3B vs 14B CausVid speed**
  - 1.3B: 45 seconds vs 14B: 1:30 for same content, but 14B much better quality for faces
  - *From: ˗ˏˋ⚡ˎˊ-*

- **1.3B face quality vs 14B**
  - 1.3B: 'looks like that guy', 14B: 'it is that guy!' - much better face fidelity
  - *From: slmonker(5090D 32GB)*

- **CausVid works better with DG models vs vanilla**
  - DG Boost models show better results with CausVid LoRA than vanilla 1.3B
  - *From: David Snow*

- **CausVid vs regular Wan inference**
  - CausVid much faster but more plastic/worse physics, quality trade-off for speed
  - *From: DiXiao*

- **1.3B vs 14B VACE quality**
  - 14B model is much better with references, 1.3B is quite bad with references
  - *From: Stad*

- **Causvid 0.25 vs 0.55 strength**
  - 0.25 strength looks much more natural, 0.55 looks a little baked
  - *From: traxxas25*

- **Q8_0 vs other quants**
  - Q8_0 is basically nearly the same as f16 with half the size, wouldn't go lower than Q4_K_S for regular generating
  - *From: The Punisher*

- **Q5_K_S vs Q3_K_S GGUF**
  - Q5_K_S is significantly better quality, Q3_K_S has noticeable patterning issues
  - *From: The Punisher*

- **14B vs 1.3B for fast motion**
  - 14BN significantly better for faster motion like Matrix fight scenes
  - *From: A.I.Warper*

- **VACE reference vs Phantom reference**
  - VACE reference leaves something to be desired compared to Phantom
  - *From: DawnII*

- **8 steps vs 4 steps with Causvid**
  - 8 steps too contrasty, 4 steps lacks motion, 6 steps may be optimal
  - *From: David Snow*

- **Wrapper vs Native VACE**
  - Wrapper has better support and VRAM management, Native limited but works fine
  - *From: Draken*

- **WAN vs Runway Gen4**
  - Quality very close, WAN generates faster (2.5min vs 5min), but Runway has better lens flare interaction and color
  - *From: VRGameDevGirl84(RTX 5090)*

- **CausVid LoRA + MoviiGen vs CausVid LoRA + CausVid model**
  - MoviiGen combination much better for image quality, lighting and movie texture
  - *From: slmonker(5090D 32GB)*

- **8 steps vs 14 steps CausVid**
  - 14 steps removes shimmer present in 8 step outputs, significant quality improvement
  - *From: CaptHook*

- **4 steps vs 8 steps for wide shots**
  - 8 steps much better for wide shots, 4 steps may be enough for medium/close shots
  - *From: ˗ˏˋ⚡ˎˊ-*

- **T2V vs I2V without control**
  - I2V is superior when not using control
  - *From: ˗ˏˋ⚡ˎˊ-*

- **30+ steps without CausVid vs CausVid LoRA**
  - 30+ steps without CausVid gives much better quality but is 5x longer, worth it for perfect shots
  - *From: Yae*

- **WAN vs Runway for video generation**
  - WAN actually looks better than Runway, but Runway can do 20 seconds vs WAN's ~6 seconds due to OOM issues
  - *From: VRGameDevGirl84(RTX 5090)*

- **Depth vs MediaPipe for facial control**
  - Depth map provides better facial movement than MediaPipe
  - *From: VRGameDevGirl84(RTX 5090)*

- **Sapiens vs standard MediaPipe**
  - Sapiens much more precise for facial transfer but harder to setup
  - *From: ˗ˏˋ⚡ˎˊ-*

- **14B vs 1.3B model quality**
  - 14B much better quality, can generate long dresses and has almost no artifacting where 1.3B failed
  - *From: traxxas25*

- **Follow Your Emoji preprocessor vs aux preprocessor**
  - Follow Your Emoji MediaPipe preprocessor is better than aux
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Depth vs other preprocessors for VACE**
  - Depth preprocessor works better than pose/mediapipe/facemesh for facial movement
  - *From: VRGameDevGirl84(RTX 5090)*

- **With vs without TeaCache for CausVid**
  - 30% slower without TeaCache (12min vs 8min), but quality appears similar
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Single vs combined VACE processors**
  - Combined processors show more detail (wrinkles) but can look oversaturated/cooked
  - *From: VRGameDevGirl84(RTX 5090)*

- **Depth vs Pose control**
  - Depth alone can achieve good facial movement and is faster, pose adds some help with face movements but may not be necessary
  - *From: VRGameDevGirl84(RTX 5090)*

- **MediaPipe vs DWPose**
  - Both have positives and negatives, MediaPipe better at following original face expression, DWPose gives more natural settled look
  - *From: VRGameDevGirl84(RTX 5090)*

- **DepthCrafter vs DepthAnything**
  - DepthCrafter is the best depth model, DepthAnything V2 is fine too, depends on quality obsession level
  - *From: David Snow*

- **14B success rate vs other models**
  - Success rate with 14B is extremely high, makes a nice change from other models
  - *From: David Snow*

- **SkyReels vs base WAN 2.1**
  - SkyReels just different, trained at 24fps, LoRAs work between base and SkyReels but not with MoviiGen
  - *From: JohnDopamine*

- **VACE vs base WAN 14B for single reference animation**
  - WAN 14B has better video quality, but VACE is more versatile for complex operations
  - *From: zelgo_*

- **14B success rate vs other models**
  - 14B has much higher success rate - two thirds of overnight batches are pretty good vs lower rates for other models
  - *From: David Snow*

- **TeaCache with/without coefficients on VACE 14B CausVid**
  - 382s vs 203s generation time, but quality differences noted
  - *From: David Snow*

- **MPS vs HPS reward LoRAs**
  - For T2V both can be used, for I2V use MPS only. HPS changes faces drastically and overpowers other LoRAs
  - *From: N0NSens*

- **Euler vs UniPC samplers with CausVid**
  - Euler produces cleaner results but has ghost-like effects, UniPC is fine but can create visible noise
  - *From: N0NSens*

- **VACE vs Fun Control for video cuts**
  - Fun Control handles cuts better than VACE
  - *From: N0NSens*

- **MatAnyone vs BiRefNet for background removal**
  - MatAnyone: 6.54s (short video), 22.02s (long video) vs BiRefNet: 9.60s (short), 18.22s (long). MatAnyone includes loose hairs but can cause NormalCrafter issues
  - *From: MilesCorban*

- **WAN T2V as image generator vs Flux**
  - WAN can generate single frames but Flux likely produces better quality images. WAN approach helps with consistency across video clips
  - *From: Nokai*

- **WAN VACE vs Runway Vid to Vid**
  - VACE works way better than Runway's Vid to Vid for video-to-video conversion
  - *From: VRGameDevGirl84(RTX 5090)*

- **VACE 14B vs HY Custom**
  - VACE 14B achieves more in 10 minutes than a week with HY Custom
  - *From: AJO*

- **VACE 14B vs 1.3B**
  - 14B is worlds better than 1.3B
  - *From: Piblarg*

- **Skyreels vs standard models**
  - Skyreels has better motion for human subjects, native 24fps vs 16fps, and higher resolution (540p vs 480p)
  - *From: DawnII*

- **WAN vs Veo 3**
  - Veo 3 shows significant advancement in prompt following and dialogue capabilities that open source hasn't matched yet
  - *From: Draken*

- **VACE vs Fun Control**
  - VACE is far ahead of anything else for controlling video output
  - *From: Ada*

- **CausVid 14B vs 1.3B**
  - 14B is better quality but 1.3B is good for secondary v2v passes and super fast
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Different frame counts with NormalCrafter**
  - 49 frames vs 81 frames yields entirely different results even with fixed seed, making development difficult
  - *From: Guey.KhalaMari*

- **Wan vs LTX**
  - Wan is the more powerful model, LTX's advantage is speed
  - *From: David Snow*

- **GGUF vs other quantization methods**
  - GGUF is slower but nicer quality, whereas fp8/int8/fp4/int4 can be faster with size reduction
  - *From: deleted_user_2ca1923442ba*

- **Quality comparison BF16 vs GGUF Q8 vs FP8**
  - bf16 > GGUF Q8 > fp8 in quality
  - *From: MilesCorban*

- **CausVid with and without CFG Schedule**
  - No CausVid reflects lora intention better, CausVid with CFG Schedule brings back lora look while maintaining speed
  - *From: Zlikwid*

- **Hunyuan Custom vs VACE**
  - VACE has better quality and support, Hunyuan Custom is 5-10 times slower to generate with shocking quality and no community traction
  - *From: AJO*

- **WAN vs HunyuanVideo**
  - WAN is better quality due to 14B parameters, but HunyuanVideo has more LoRAs, been around longer, and is faster/smaller. HunyuanVideo doesn't start in same position - uses face and can put it anywhere
  - *From: MilesCorban*

- **Movii base vs WAN base for I2V**
  - Movii as base model has better prompt adhesion than WAN base model when used with VACE for I2V
  - *From: Johnjohn7855*

- **Causvid distillation level**
  - Causvid may have distilled slightly too much for some uses, similar to SDXL DMD2 going to 4 steps when 8 steps can be better balance
  - *From: deleted_user_2ca1923442ba*

- **UniAnimate vs standard pose for character consistency**
  - UniAnimate has better consistency of the character compared to standard pose controls
  - *From: Johnjohn7855*

- **Context windows vs batching method**
  - Batching followed by cleanup pass is superior method - preserves character likeness
  - *From: A.I.Warper*

- **Using own face vs latent sync for lip sync**
  - Using own face input produces higher quality results than latent sync
  - *From: VRGameDevGirl84(RTX 5090)*

- **Official DWPose vs ComfyUI implementation**
  - Official implementation is cleaner, works on more content, no dropped frames
  - *From: A.I.Warper*

- **MediaPipe vs other face detection**
  - MediaPipe breaks when more than 45 degrees or mouth too open
  - *From: Mads Hagbarth Damsbo*

- **VACE extension vs Skyreels Diffusion Forcing**
  - VACE has better movement and quality but noticeable color shift, Skyreels doesn't have color shift
  - *From: ArtOfficial*

- **Chroma vs Base Flux speed**
  - Chroma is slower than base Flux, needs higher step count and has CFG making it twice as slow
  - *From: mamad8*

- **GGUF vs FP8 on WAN models**
  - GGUF more precise but quite a bit slower than fp8, fp8 doesn't need much offloading on 5090
  - *From: Kijai*

- **Wan 14B vs 1.3B model quality**
  - Night and day difference - 14B much better at understanding complex objects and producing realistic results
  - *From: David Snow*

- **Wan 1.3B vs 14B for dress understanding**
  - 1.3B kept producing fake results and never understood full length dress, 14B worked perfectly with same settings
  - *From: traxxas25*

- **CausVid speed vs standard inference**
  - CausVid is extremely fast compared to normal inference
  - *From: mamad8*

- **TeaCache vs CausVid optimization approaches**
  - TeaCache skips steps, CausVid optimizes every step to need fewer - different approaches that don't work well together
  - *From: Cubey*

- **14B vs 1.3B generation time**
  - 1.3B does 163 frames in 5 minutes vs 20 minutes for 14B
  - *From: VK (5080 128gb)*

- **Native vs GGUF loader performance**
  - GGUF took 40 minutes, native loader took 17 minutes for same generation
  - *From: The Shadow (NYC)*

- **Normal Wan vs other models for VACE**
  - Normal Wan has been best so far, skyreels for human centric videos, moviegen for realistic high res cinematic
  - *From: Kijai*

- **Flux vs SDXL for stylized content**
  - SDXL better for heavily stylized stuff, Flux awful unless using LoRA, Flux controlnets much worse than SDXL
  - *From: A.I.Warper*

- **SDXL vs Flux controlnets**
  - Xinsir + mistoline still peak controlnet, mistoline Flux version much worse, even VACE better in many things
  - *From: Kijai*

- **Vace 1.3B vs 14B**
  - 14B works fine with context options, 1.3B may not work properly with context options
  - *From: N0NSens*

- **David Snow's workflow vs vid2vid workflow**
  - New workflow is complete character replacement vs stylization, can do things vid2vid workflow cannot
  - *From: David Snow*

- **SkyReels CausVid vs normal CausVid**
  - SkyReels CausVid at 720p gives crisp results but not as prompt adherent as normal CausVid
  - *From: hicho*

- **VACE vs I2V model speed**
  - VACE shouldn't be faster than I2V since it's T2V model + 8 more VACE blocks, but user reports faster performance with native nodes
  - *From: aikitoria*

- **RTX 5070 vs 5060 Ti**
  - 5070 is faster than 5060 Ti in specs, and for AI if models fit. 5060 Ti slightly slower than 3080
  - *From: VK (5080 128gb)*

- **Euler vs Euler/AccVideo scheduler**
  - Very hard to spot difference, Euler might be marginally sharper
  - *From: David Snow*

- **AccVideo full model vs LoRA**
  - Full model better, LoRA worse but maybe good enough - fur better on full model
  - *From: Kijai*

- **14B t2v + vace vs 14B vace standalone**
  - t2v + vace handles v2v moves better than standalone vace
  - *From: Nokai*

- **UniPC vs Euler schedulers**
  - UniPC timesteps: [999, 978, 952, 921, 882, 833, 769, 681, 555, 357]
  - *From: Kijai*

- **AccVid vs CausVid for T2V**
  - AccVid seems worse than CausVid for unintended use, CausVid better for stylized content, AccVid better for realistic
  - *From: Kijai*

- **AccVid vs CausVid quality**
  - AccVid output seems better than CausVid, but CausVid way better at 0.5 weight
  - *From: 🦙rishappi, Ada*

- **AccVid vs CausVid prompt following**
  - I2V with AccVid has decent quality but prompt following is gone, later seed did follow prompt but quality wasn't great
  - *From: Kijai*

- **Hunyuan AccVid vs Wan**
  - Hunyuan AccVid makes everything realistic and is slower than Wan with bad V2V results at 0.50 denoiser
  - *From: Kijai, hicho*

- **BAGEL ComfyUI implementation**
  - Not that good, takes lot of time, got 2 blurry outputs for image edit. To be frank, it SUX
  - *From: slmonker(5090D 32GB)*

- **DepthCrafter vs DepthAnything v2**
  - DepthCrafter has less flicker and looks smoother but takes longer
  - *From: Gateway {Dreaming Computers}*

- **Phantom vs VACE for identity preservation**
  - Phantom has better identity preservation for reference images and better multi-reference handling
  - *From: Johnjohn7855*

- **Phantom 14B vs regular models speed**
  - Phantom 14B is significantly slower due to 3 noise predictions and CFG requirement
  - *From: Kijai*

- **CausVid vs no CausVid on Phantom**
  - Without causvid the quality is ridiculously higher
  - *From: ZeusZeus (RTX 4090)*

- **VACE ref vs Phantom ref for identity**
  - Identity is preserved much better than vace ref with VACE input + phantom ref
  - *From: Zuko*

- **480p vs 720p generation quality**
  - 480p got basically every detail right, works better for some cases
  - *From: aikitoria*

- **Moviigen vs regular WAN**
  - Model performs better on average at higher res, Moviigen can be pretty noisy
  - *From: TK_999*

- **Phantom vs Kling Elements**
  - Kling Elements is better quality and higher res, but Phantom is closest local model has gotten to that level
  - *From: aikitoria*

- **Phantom vs other models**
  - Slowest model used so far, but no other model can do what it does
  - *From: aikitoria*

- **Phantom facial consistency vs Kling**
  - Phantom may have better facial consistency than Kling for single reference use cases
  - *From: hau*

- **causvid vs causvid+accvid**
  - causvid+accvid combo provides better results, accvid helps with blur that causvid alone has
  - *From: Ada*

- **Phantom vs 14B for morphing**
  - 14B gave better morphing results than Phantom in limited testing
  - *From: David Snow*

- **1024x576 vs 864x480 vs 960x544**
  - 1024x576 produces WAY better output than 864x480 and much better than 960x544
  - *From: CaptHook*

- **6 steps vs 8 steps vs 10 steps**
  - 6 steps showed occasional morphing and less sharpness, 8 steps optimal, 10 steps too long with too much contrast
  - *From: CaptHook*

- **RTX 6000 Pro vs 4090 speed**
  - RTX 6000 Pro about double the speed of 4090 on wan, maybe a little less
  - *From: aikitoria*

- **Phantom vs other models for motion transfer**
  - Best model seen so far for motion transfer
  - *From: Kijai*

- **VACE vs Phantom for character consistency**
  - Phantom is better for character consistency, VACE better for control
  - *From: aikitoria*

- **CausVid vs AccVid effectiveness**
  - CausVid does most of the heavy lifting, didn't like what AccVid adds
  - *From: Kijai*

- **Phantom 14B vs 1.3B for multiple subjects**
  - 14B much better with 3+ subjects than 1.3B
  - *From: DawnII*

- **Phantom alone vs Phantom + VACE**
  - VACE alone may be sufficient since it already provides subject consistency via ref image
  - *From: VRGameDevGirl84(RTX 5090)*

- **VACE generation time vs Phantom + VACE**
  - VACE alone: 177.56 seconds, Phantom + VACE: 261.39 seconds
  - *From: VRGameDevGirl84(RTX 5090)*

- **Phantom with random AI images vs well-known celebrities**
  - Very accurate on random AI images, obvious differences become apparent with well-known faces
  - *From: David Snow*

- **Phantom cfg between 1 and 10 with CausVid**
  - Haven't seen much difference between cfg 1 and 10 when using CausVid
  - *From: DawnII*

- **Phantom alone vs Phantom + VACE**
  - Phantom alone maintains good likeness, but coupling with VACE causes character consistency to go out the window and produces artifacts
  - *From: David Snow*

- **Topaz vs ComfyUI upscalers**
  - All upscalers in ComfyUI are better than Topaz technically, but Topaz is plug-and-play while ComfyUI requires complex multi-pass workflows
  - *From: chrisd0073*

- **Different video generation speeds**
  - CausVid is hard to top - killer performance
  - *From: JohnDopamine*

- **14B Phantom vs 1.3B Phantom**
  - 14B far better quality but really slow
  - *From: Kijai*

- **Phantom vs LoRA training**
  - Phantom does hair as well or better than trained LoRAs right out of the box
  - *From: Thom293*

- **All-in-one model vs separate Phantom + CausVid**
  - All-in-one suffers from LoRA integration, separate loading preferred
  - *From: Kijai*

- **CausVid with block 0 disabled vs other variants**
  - CausVid w/ block 0 disabled is definitely the 'right' way for Phantom
  - *From: JohnDopamine*

- **Full Phantom model vs distilled versions**
  - Full model was much better - difference was massive in quality and movement
  - *From: TK_999*

- **VACE vs I2V methods**
  - I2V have very good consistency, different results but haven't tested which is actually better
  - *From: wooden tank*

- **Kontext vs other editing tools**
  - Kontext very limited in practice - can't do perspective shifts like Runway, can't do major out of context edits well like 4o
  - *From: pom*

- **CausVid v2 vs v1.5**
  - v2 preferred - can use full strength, less plasticy looking, has block 0 already removed
  - *From: AJO*

- **Phantom vs VACE with reference image**
  - Phantom faster (253s vs 738s) and produces better results
  - *From: VRGameDevGirl84(RTX 5090)*

- **FP8 vs FP16 Phantom**
  - FP8 half the generation time with similar quality
  - *From: AJO*

- **Merged CausVid model vs base Phantom + v2 lora**
  - Merged model seems better than separate lora application
  - *From: Thom293*

- **LoRAs vs no LoRAs**
  - LoRAs made a HUGE difference in quality
  - *From: VRGameDevGirl84(RTX 5090)*

- **Merged model vs stock model**
  - You can't get this quality with stock model - looks really bad without the LoRAs
  - *From: VRGameDevGirl84(RTX 5090)*

- **Merged model vs stacked LoRAs**
  - Same quality but merged model generates faster
  - *From: VRGameDevGirl84(RTX 5090)*

- **SkyReels A2 vs Phantom**
  - Not nearly as accurate as phantom, and far less references can be given
  - *From: DawnII*

- **Film-like vs vibrant outputs**
  - Film-like outputs (flatter, less saturated) preserve dynamic range better for post-processing, while vibrant outputs look good immediately but have blown highlights
  - *From: Ruairi Robinson*

- **CausVid v1 vs v1.5 vs v2**
  - v1.5 similar settings to v1 but helps eliminate flashes, v2 needs >1 CFG
  - *From: Johnjohn7855*

- **Normal Craft vs Sapients normal maps**
  - Normal Craft works great, Sapients works but not as well
  - *From: VRGameDevGirl84(RTX 5090)*

- **VACE vs FaceFusion for face swapping**
  - VACE is incomparably better - handles lighting changes perfectly, works with partial face obscuration, doesn't lose tracking easily like FaceFusion which turns into flickery mess
  - *From: Ruairi Robinson*


## Tips & Best Practices

- **Never use denoise other than 1.0 unless doing vid2vid**
  - Context: For T2V generation
  - *From: Kijai*

- **Use block 8 with 1.3B model**
  - Context: Better results with 1.3B variant
  - *From: Kijai*

- **Use reference image as start image in Fun 1.1**
  - Context: Works better than using actual start image, especially if start doesn't match source
  - *From: Hashu*

- **Reverse video if reference object hidden in first frame**
  - Context: When trying to give reference to something not visible initially
  - *From: ingi // SYSTMS*

- **Higher audio CFG helps with lip sync**
  - Context: Improving sync quality in FantasyTalker
  - *From: Kijai*

- **Use conda environments for AI projects**
  - Context: Prevents breaking ComfyUI when new projects have special requirements
  - *From: MilesCorban*

- **Use DG models for T2V with 1.3B**
  - Context: Can get usable results in 6 steps instead of 25-30, though still not good quality. Ares V3 is current favorite, V5 versions too cooked
  - *From: David Snow*

- **Mask shadows when removing people with VACE**
  - Context: When trying to remove a person, need to mask their shadow as well or VACE will use shadow to add a person back
  - *From: traxxas25*

- **Use bbox instead of person-shaped mask for VACE**
  - Context: Better results when removing objects/people from scenes
  - *From: ArtOfficial*

- **Higher CFG values retain motion better**
  - Context: Head movements follow better with higher CFG values in v2v workflows
  - *From: chrisd0073*

- **For edge control, do something between scribble and layout**
  - Context: Works kind of well with hard lines but outlining your overall motion
  - *From: Rishi Pandey*

- **Consider using depth map layer where applicable**
  - Context: Usually gives better results than poses or just poses with scribble, can blur parts if faces get too detailed
  - *From: Blink*

- **For long v2v animations, encode base video directly instead of using start frame**
  - Context: Superior in most cases - single start frame is limited when hands move off-screen or background changes
  - *From: David Snow*

- **Kitbash different preprocessors for best results**
  - Context: Combining different control preprocessors as RGB data opens room for creativity
  - *From: chrisd0073*

- **Add noise or grain to prevent gradient banding**
  - Context: Old trick to make gradients not have banding artifacts before compression
  - *From: Nathan Shipley*

- **Use Skyreels v2 with shift over 10 for better movement**
  - Context: Otherwise no movement in generated videos
  - *From: Colin*

- **Only overlap by 4 frames when chaining DF videos**
  - Context: For video extension workflows to minimize redundancy
  - *From: MilesCorban*

- **Include color correction for extended videos**
  - Context: Needed for i2v workflows or videos get progressively brighter
  - *From: MilesCorban*

- **Use normal maps with depth for better control**
  - Context: Additional information in normal maps produces better results than depth alone
  - *From: David Snow*

- **Set frame load cap to anything divisible by 4 plus 1 frame**
  - Context: For proper frame handling in video workflows
  - *From: Flipping Sigmas*

- **Use context node for videos longer than 81 frames**
  - Context: When generating long sequences to avoid looping artifacts
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Train character LoRAs for consistency**
  - Context: Use 10 images and 2-3 clips with diffusion pipe to solve character consistency issues
  - *From: A.I.Warper*

- **Add start frame twice for better consistency**
  - Context: When using VACE, add start frame twice at beginning with no mask for morphing control
  - *From: TimHannan*

- **Increase resolution to reduce noise in VACE output**
  - Context: When getting noisy results from VACE processing
  - *From: N0NSens*

- **Process order: upscale then interpolate**
  - Context: For video post-processing workflow
  - *From: TimHannan*

- **Turn off TeaCache when using LoRAs**
  - Context: For better LoRA compatibility with Wan 14B I2V
  - *From: hablaba*

- **Use musubi-tuner for Wan LoRA training**
  - Context: For training LoRAs on Wan models
  - *From: MisterMango*

- **Use Redux + ACE++ Fill + InstantID SDXL for consistent character workflows**
  - Context: For start/end frame generation
  - *From: Draken*

- **Put LoRA trigger words at beginning of prompt**
  - Context: For Wan LoRAs
  - *From: Cubey*

- **Remove first 8 frames from CausVid output**
  - Context: To eliminate artifacts at video start
  - *From: Vérole*

- **Use format 'Wan' to auto-adjust frame counts**
  - Context: When getting tensor size errors
  - *From: Valle*

- **Use custom schedule with CausVid**
  - Context: CausVid had custom schedule available in the node
  - *From: Kijai*

- **Use flex attention with CausVid for proper results**
  - Context: Eliminates start weirdness/latent flicker
  - *From: Kijai*

- **MoviiGen likely wants 720p minimum resolution**
  - Context: Finetuned on high resolution content, lower resolutions may cause strangeness
  - *From: Draken*

- **Extract full finetunes as LoRAs if needed**
  - Context: We can extract MoviiGen as a lora while keeping benefits of full finetune
  - *From: yi*

- **VACE 14B max blocks to swap is 8**
  - Context: When configuring block swapping for memory management
  - *From: DawnII*

- **Swapping even one block offloads VACE results and saves VRAM**
  - Context: For memory optimization with VACE wrapper
  - *From: Kijai*

- **Separate preprocessor inputs rather than blend for better lip sync results**
  - Context: When using multiple control inputs
  - *From: DawnII*

- **1.3B is good enough for controlled generation**
  - Context: When deciding between model sizes
  - *From: Juampab12*

- **For VACE combined controls, use 2 VACE embeds nodes with prev_embeds input**
  - Context: When using multiple control inputs
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Use bounding box with no feathering for better subject control**
  - Context: When trying to control subject movement along paths
  - *From: Kijai*

- **Set CFG to 2 and use 6 steps for faster generation**
  - Context: For quick previews and seed hunting with base 1.3B model
  - *From: David Snow*

- **Pose can be stronger but depth is better at lower strength**
  - Context: When setting VACE embed strength values
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Remove 'enhance-a-video' for lip sync as it adds unwanted details**
  - Context: When working with FantasyTalking lip sync
  - *From: ingi // SYSTMS*

- **Use multiple VACE encoders for blending different control inputs**
  - Context: When you need to blend depth and canny without artifacts
  - *From: Kijai*

- **Use gray or black images for additional VACE encoders when using multiple**
  - Context: When using multiple VACE encoders with reference images
  - *From: Kijai*

- **e5m2 quantization recommended for 3090s and 30XX series**
  - Context: When choosing quantization for older GPUs
  - *From: happy.j*

- **Start CausVid LoRA strength at 0.5, adjust based on needs**
  - Context: Lower strength requires more steps, higher strength can cause artifacts
  - *From: Kijai*

- **Skip VACE blocks when using CausVid LoRA**
  - Context: Gives VACE breathing room and reduces conflicts
  - *From: Kijai*

- **Use multiple reference images by composing them in single frame**
  - Context: Better than batch feeding which concatenates horizontally
  - *From: Kijai*

- **Use context windows instead of long single generations**
  - Context: More efficient and reference works across context windows
  - *From: Kijai*

- **Select fp8 quantization even for fp8 models**
  - Context: Prevents weight casting to base precision
  - *From: Kijai*

- **Reduce LoRA strength to allow more motion transfer**
  - Context: When using CausVid LoRA with VACE for better movement
  - *From: Kijai*

- **Use cfg 1.0 and 2-4 steps with CausVid LoRA**
  - Context: CausVid is distilled for both cfg and steps
  - *From: Kijai*

- **Disable teacache, enhance-a-video, slg, and zero_star with CausVid**
  - Context: These don't work at cfg 1.0
  - *From: Kijai*

- **Keep shift around 8 with CausVid LoRA**
  - Context: Don't move to shift 1 like with other speed optimizations
  - *From: Kijai*

- **Turn off WanVideo Experimental Args for 1.3B model**
  - Context: Prevents issues with 1.3B model generation
  - *From: Mngbg*

- **Use reference and start frame together for best results**
  - Context: When using the same image as both reference and start frame
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Train LoRAs for both image and video generation**
  - Context: For maintaining specific styles that aren't realism
  - *From: Piblarg*

- **Use skip layer guidance for refining hands**
  - Context: Hands are Wan's weakness, but skip layer guidance can help refine them
  - *From: Piblarg*

- **Filter out finger bones when using pose control**
  - Context: To avoid hand/paw confusion in character generation
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Have only around 1GB VRAM free for optimal performance**
  - Context: When using block swapping with Wan models
  - *From: DawnII*

- **Use offload device in the loader for memory management**
  - Context: When running into OOM issues with limited VRAM
  - *From: Stad*

- **For CausVid LoRA, always use CFG 1.0 and disable all enhancements**
  - Context: TeaCache, SLG, enhance video should all be off
  - *From: Kijai*

- **Use 2-4 steps with CausVid, nothing else**
  - Context: Keep it minimal for best results
  - *From: Kijai*

- **1.3B cannot handle images with small heads**
  - Context: Use half body or medium shots instead of wide shots
  - *From: slmonker(5090D 32GB)*

- **VACE doesn't like combined controls**
  - Context: Combining pose and depth is unreliable, use one at a time
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Use Color Match node for VACE results**
  - Context: Results come out darker than reference, color matching helps
  - *From: N0NSens*

- **For multiple image references, batch node auto-stacks horizontally**
  - Context: Can manually pad/assemble for more precise control
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Use closeup shots for better detail with 1.3B model**
  - Context: 1.3B isn't great with details, so zoom in on subjects for better results
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Higher CFG with no prompt for better preprocessor following**
  - Context: In Fun Control, higher cfg with no prompt makes video follow preprocessor movement better
  - *From: chrisd0073*

- **Fun Control is better than VACE for facial expressions**
  - Context: VACE is unstable for facial expression and hard to get right if person is completely different, Fun Control is way better but slower
  - *From: chrisd0073*

- **Use symlinks or model path configuration to share models between ComfyUI installations**
  - Context: When having separate installations for different workflows
  - *From: The Punisher*

- **Remove background and pad between subjects for multi-person VACE**
  - Context: When trying to use VACE with multiple people, though subject bleed may still occur
  - *From: DawnII*

- **Use GetLatentRangeFromBatch to avoid decode/encode to pixel**
  - Context: For video stitching workflows to improve efficiency
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Lower preprocessing resolution for speed over quality**
  - Context: When pose preprocessing takes too long
  - *From: DawnII*

- **Adjust LoRA strength significantly affects results**
  - Context: When using CausVid LoRA
  - *From: DawnII*

- **Chain VACE embeds for multiple controls**
  - Context: Put depth on one embed, frames for inpainting on another, reference can feed to both
  - *From: DawnII*

- **Use reward LoRAs to enhance CausVid generations**
  - Context: Fixes blurry and oversaturated look
  - *From: yi*

- **Lower LoRA strength requires higher step count**
  - Context: When using CausVid LoRA
  - *From: JohnDopamine*

- **Don't make VACE reference input too large**
  - Context: No point in oversized reference frames
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Reduce CausVid LoRA strength to 0.3, use 12 steps with UniPC scheduler**
  - Context: For better quality with less speed impact than 0.5 strength with 4 steps
  - *From: Ada*

- **Use KJ set/get nodes instead of Anything Anywhere**
  - Context: Much less prone to breaking and more reliable
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Try lower version numbers for DG models**
  - Context: Higher version numbers tend to produce flashes and artifacts - too strong
  - *From: David Snow*

- **Use first frame of video with FLUX ControlNet to create re-style as reference image**
  - Context: For better stylization in VACE workflows
  - *From: VRGameDevGirl84(RTX 5090)*

- **Understand workflows before running them**
  - Context: Don't just copy - try to understand why each component is there, especially when stacking multiple LoRAs
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Scale up reference image for better detail extraction**
  - Context: When using VACE reference images
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Crop reference image to head only unless you want t-shirt details**
  - Context: For better face focus in VACE
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Test with and without prompts for different results**
  - Context: Prompts make a big difference in VACE output quality
  - *From: VRGameDevGirl84(RTX 5090)*

- **Use DepthAnything (DA) instead of DepthCrafter for lower VRAM usage**
  - Context: When depth preprocessing is needed but VRAM is limited
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Try skipping every 5th block when using CausVid with 14B VACE**
  - Context: For more efficient processing when combining CausVid and 14B VACE
  - *From: JohnDopamine*

- **Use cfg 1.0 and lora strength 0.3-0.6 with CausVid - lower values need more steps**
  - Context: CausVid allows 4-8 step inference
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Disable TeaCache and step-based optimizations for low step counts**
  - Context: When using 4-10 steps with CausVid
  - *From: JohnDopamine*

- **Use separate VACE embeds for multiple controls instead of blending**
  - Context: When combining depth and pose controls
  - *From: Johnjohn7855*

- **Reduce strength when using multiple VACE embeds on same timesteps**
  - Context: Prevents burning/overcooking with multiple controls
  - *From: Kijai*

- **Use neutral grey image for secondary VACE embed reference**
  - Context: When combining multiple controls to avoid overcooking
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Colors matter for VACE controls - desaturate normal maps, grey areas get inpainted**
  - Context: For masks: white=change, black=ignore. Pose doesn't need color adjustment
  - *From: DawnII*

- **CausVid works well for v2v with denoise 0.2**
  - Context: Video-to-video workflow with LoRAs
  - *From: hicho*

- **Use end_percentage instead of strength for VACE control**
  - Context: Stops the control at certain point during process, better than just stopping at certain step
  - *From: Draken*

- **Create reference image from first frame of input video**
  - Context: Helps with consistency when using VACE controls, optional but recommended
  - *From: VRGameDevGirl84(RTX 5090)*

- **Use decay curve over time for control**
  - Context: Much better than just stopping control at certain step, gives more natural progression
  - *From: Nekodificador*

- **Set depth strength to 0.5 when combining with pose**
  - Context: When depth is too strong it distorts the source image, combining at 0.5 with pose gives better balance
  - *From: VRGameDevGirl84(RTX 5090)*

- **Turn off Fresca enhancement when using 14B with CausVid LoRA**
  - Context: Other enhancements are fine but Fresca will screw up output
  - *From: David Snow*

- **Use contrast node set to 0.5 to lighten baked control lines**
  - Context: When lines control bakes lines into output
  - *From: David Snow*

- **For multi-reference setup: pose at strength 1 in first encoder, depth at 0.5 in second, no ref in second**
  - Context: When using multiple VACE encoders for better control
  - *From: VRGameDevGirl84(RTX 5090)*

- **Use grow mask blur to match character body size**
  - Context: When mapping characters and needing size consistency
  - *From: yo9o*

- **Simple backgrounds help reduce artifacts in long generations**
  - Context: For extended video generation and context handling
  - *From: Draken*

- **Reduce CausVid LoRA strength to at least half when using with VACE**
  - Context: Memory management and better results
  - *From: Kijai*

- **Use specific blocks application with VACE for better results**
  - Context: When using control inputs
  - *From: Kijai*

- **Remove background from reference images for better VACE results**
  - Context: When VACE is using background instead of subject
  - *From: ingi // SYSTMS*

- **Match reference image closely to first frame when using normal maps**
  - Context: At high strength (0.9), otherwise drop to 0.5 strength
  - *From: VRGameDevGirl84(RTX 5090)*

- **Prompt 'the animated character is talking' or 'the Disney character' for better character recognition**
  - Context: When model doesn't recognize specific characters like Shrek
  - *From: Piblarg*

- **Use photo terminology instead of 'photorealistic' or 'realistic'**
  - Context: For better photorealistic outputs, use terms like '4k, uhd, 8k, high definition, detailed, raw photo, photoshoot, studio session, IMAX, National Geographic'
  - *From: Thom293*

- **Start with 0.5 strength for NormalCrafter when face differs significantly**
  - Context: When the reference face is very different from the control video face, start at 0.5 and work up until it gets wonky
  - *From: VRGameDevGirl84(RTX 5090)*

- **Remove backgrounds or use black wall for better VACE results**
  - Context: Having a clean background (like a black wall) improves VACE performance for character animation
  - *From: VRGameDevGirl84(RTX 5090)*

- **Lower depth effect strength to avoid edge limitations**
  - Context: When using double control (depth+pose), reduce depth strength and start/end percentages so depth doesn't limit the edges
  - *From: slmonker(5090D 32GB)*

- **Prompt for elements not in reference image**
  - Context: For VACE, need to prompt for items like skirts or accessories that aren't visible in the reference image, or it might generate different clothing
  - *From: Kijai*

- **Use reference images with characters on white background for better character consistency**
  - Context: When creating multiple story scenes with same character
  - *From: Piblarg*

- **Disconnect control inputs when not needed for reference-only generation**
  - Context: When using VACE with just reference images
  - *From: Kijai*

- **Use DF (DeepFloyd) for better consistency through context windows**
  - Context: When extending videos beyond base frame limits
  - *From: DawnII*

- **Minimum 5 frames needed for VACE with reference to work properly**
  - Context: When testing ideas with minimal frame counts
  - *From: Kijai*

- **Use CausVid strength between 0.3 and 0.6**
  - Context: Lower requires more steps, 0.5 and 4 steps is good starting point
  - *From: ˗ˏˋ⚡ˎˊ-*

- **CFG 1.0 when using CausVid**
  - Context: CFG > 1.0 isn't recommended unless using SLG which doubles generation time
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Use last N frames for video extension**
  - Context: Take the end frames of video you want to extend (like last 20) and put them in start images
  - *From: Piblarg*

- **Reduce mask strength to avoid first frame jump**
  - Context: When using reference image, first frame shows the reference - need to stylize first frame or adjust approach
  - *From: ▲*

- **Turn off Sage and TeaCache for VACE/CausVid**
  - Context: Recommended settings, though some report TeaCache working at 8 steps
  - *From: Gateway {Dreaming Computers}*

- **Use aligned reference frames**
  - Context: When combining control video + reference frame + LoRA, align the reference frame as closely as possible to avoid it being ignored
  - *From: Piblarg*

- **Keep only face over whole body**
  - Context: Found much better results from keeping just the face rather than whole body, and it picks up color cues from tiny remaining outline
  - *From: AJO*

- **Use ChatGPT for first frame creation**
  - Context: ChatGPT is really good for first frame generation - gets close enough but isn't super locked in like classic controlnets
  - *From: Draken*

- **Blend black layer on depth maps**
  - Context: Depth maps cause output to follow shapes too much, but blending in black layer on top makes it less visible, works like a strength control
  - *From: ▲*

- **MultiGPU doesn't save VRAM for inference**
  - Context: Everything is always offloaded for inference anyway, only benefit is saving offload time. Makes sense for T5 but less so for VAE
  - *From: Kijai*

- **Use multiple reference images as single combined image rather than chaining**
  - Context: When using multiple VACE encoders with different references
  - *From: DawnII*

- **Use 1.3B model and/or CausVid LoRA for long context generation**
  - Context: When generating videos longer than 81 frames to manage slowness
  - *From: Kijai*

- **Find 16:9 aspect ratio resolutions that are divisible by 16**
  - Context: When changing from default 512x512 resolution
  - *From: A.I.Warper*

- **Blur depth mask for better results**
  - Context: When using depth control with VACE
  - *From: Piblarg*

- **Use face masking to isolate facial details from input video**
  - Context: When trying to preserve facial movement while controlling other aspects
  - *From: VRGameDevGirl84(RTX 5090)*

- **Use high quality for first video when doing 2-stage character replacement**
  - Context: When creating initial video to later replace characters, use high quality (14B) since second pass only replaces/refines character and leaves rest as-is
  - *From: MilesCorban*

- **Don't use FlowMatch sampler with Causvid LoRA**
  - Context: UniPC is recommended scheduler instead of the FlowMatch sampler from Causvid repo
  - *From: JohnDopamine*

- **Be careful with values above 1.0**
  - Context: Going over strength values of 1.0 is not always safe, though it can work with Causvid
  - *From: Guey.KhalaMari*

- **Break down complex tasks into stages**
  - Context: Instead of trying to do everything in one generation, create strong still images first then use fewer controls for motion
  - *From: Guey.KhalaMari*

- **Use black image as reference for depth-only control**
  - Context: When using only depth video control, put black image as reference for the depth node, though this may darken output
  - *From: Johnjohn7855*

- **Match reference frame to first pose frame**
  - Context: Have starting frame/ref frame as close to the pose first frame to prevent morphing the reference to work with control
  - *From: Draken*

- **Use Sobol or Latin Hypercube sampling for parameter testing**
  - Context: These methods fill parameter space more evenly than random sampling, avoiding clumping issues
  - *From: deleted_user_2ca1923442ba*

- **Use batching method followed by cleanup pass for long sequences**
  - Context: When generating sequences longer than 81 frames to maintain character consistency
  - *From: A.I.Warper*

- **Start with high resolution base image for multi-angle generation**
  - Context: When extracting frames from animations for different viewpoints
  - *From: David Snow*

- **Use gray (RGB 127 or #808080) for masked areas**
  - Context: When masking parts of input video for VACE processing
  - *From: DawnII*

- **Use input video strength of at least 0.6 to maintain mouth movements**
  - Context: When using original video input with face masking
  - *From: VRGameDevGirl84(RTX 5090)*

- **Blend face detection methods at 0.5 strength as starting point**
  - Context: When combining DWPose and MediaPipe face detection
  - *From: Gateway {Dreaming Computers}*

- **Use overlapping frames for seamless video extension**
  - Context: When extending videos with VACE, use last 6-10 frames as input for next generation
  - *From: zelgo_*

- **Remove overlapping frames from first clip instead of second**
  - Context: First clip frames get changed slightly during generation, so remove those instead of the newly generated ones
  - *From: seitanism*

- **Use different seeds for each extension stage**
  - Context: Same seeds for upscaling usually results in higher micro contrast and burnt look
  - *From: zelgo_*

- **Increase step count when extending clips with CausVid**
  - Context: 12 steps works well with dynamic movement for extensions
  - *From: zelgo_*

- **Use higher resolution rendering for better small face quality**
  - Context: Render at 1280x720 on A6000 to help with small faces in wide shots
  - *From: traxxas25*

- **Construct reference image manually for optimal VACE results**
  - Context: Don't rely on automatic concatenation, build your reference image yourself to avoid wasting space
  - *From: Kijai*

- **Prompt for background motion with abstract reference images**
  - Context: When using abstract reference images, explicitly prompt for background movement to help VACE understand the scene
  - *From: David Snow*

- **Use 5+ frames minimum with VACE reference images**
  - Context: Single frame sampling doesn't work well with reference images, duplicate pose image 5 times for better results
  - *From: Kijai*

- **Match input video when using normal maps for facial movement**
  - Context: Normal maps work best for close-up shots and good facial movement but input video must match or results get wonky
  - *From: VRGameDevGirl84(RTX 5090)*

- **Use simple prompts with pose interpolation**
  - Context: For better pose transition results
  - *From: toyxyz*

- **Raise Confidence Threshold when body parts are obscured**
  - Context: For pose detection accuracy
  - *From: toyxyz*

- **Use inspyrenet rembg for immaculate masks**
  - Context: Easiest way to get great masks for video processing
  - *From: David Snow*

- **Use set latent noise mask for native workflows**
  - Context: When doing inpainting with native ComfyUI nodes
  - *From: David Snow*

- **Use Euler sampler for most reliable results**
  - Context: UniPC gives subtle 'dancing haze'
  - *From: David Snow*

- **CFG 1.0 is important for speed**
  - Context: Generations take significantly longer if CFG is raised
  - *From: David Snow*

- **Enable quant unless you want your PC to die**
  - Context: When using 14B model
  - *From: David Snow*

- **Use DG Boost models with Vace 1.3B**
  - Context: Base 1.3B model wasn't as good, DG models are better for inpainting workflows
  - *From: David Snow*

- **Use face segmentation node for single faces**
  - Context: Gives accurate shape instead of bounding box for better face replacement
  - *From: David Snow*

- **Use euler sampler for VACE**
  - Context: Most reliable sampler choice, though best is subjective
  - *From: David Snow*

- **Use 1024x576 resolution to save time**
  - Context: Alternative to 1280x544 ultrawide when processing speed is important
  - *From: David Snow*

- **Make block swap dynamic based on pixel counts**
  - Context: Use conditional nodes with thresholds for different block swap amounts
  - *From: DevouredBeef*

- **For VACE inpainting, inpaint every frame in starting video or starting image for I2V, then feed output and mask to VACE encoder**
  - Context: When doing subject removal or area inpainting
  - *From: Stad*

- **Use DG Boost models instead of base 1.3B model for better inpainting performance**
  - Context: When using VACE with 1.3B models
  - *From: David Snow*

- **Reference images are notorious for causing flashes and artifacts - first 10 frames often unusable**
  - Context: When using reference images in VACE workflows
  - *From: David Snow*

- **You can balance multiple LoRAs by adjusting VACE strength when they overpower style LoRAs**
  - Context: When using multiple LoRAs with VACE
  - *From: David Snow*

- **For 4070 12GB with 32GB RAM, use VACE 1.3B with DG Boost models or continue with Q5 GGUF if that's only option**
  - Context: Hardware-specific model recommendations
  - *From: David Snow*

- **Use separate encoders for each control net**
  - Context: When using multiple control inputs with VACE
  - *From: VRGameDevGirl84(RTX 5090)*

- **Use built-in ComfyUI templates for learning**
  - Context: Select workflows -> browse templates -> video section for VACE workflows
  - *From: Gateway {Dreaming Computers}*

- **Be selective about reference images with CausVid**
  - Context: It takes too much lighting from ref image, can't control lighting override
  - *From: David Snow*

- **Avoid shiny disco balls until you get basics down**
  - Context: When learning new workflows, focus on fundamentals first
  - *From: Gateway {Dreaming Computers}*

- **Training LoRA on high quality images makes output sharper**
  - Context: For improving Wan output quality
  - *From: Thom293*

- **Use depth at 0.5 strength for similar camera movement**
  - Context: When trying to copy motion for background camera movement
  - *From: Valle*

- **For longer videos, high frame count makes process really slow**
  - Context: When generating videos longer than 81 frames
  - *From: Valle*

- **Remove depth and normals from multi-input VACE**
  - Context: Depth and normals constrain style too much, makes it too similar to source footage
  - *From: David Snow*

- **Try normal pass for very hard movement**
  - Context: Can help with complex motion in VACE
  - *From: N0NSens*

- **Use HED controlnet with lowered strength (0.5) for subtle control**
  - Context: When you want control but don't want it to overpower the generation
  - *From: VRGameDevGirl84(RTX 5090)*

- **Use pasteback with inpainting to avoid VAE compression**
  - Context: When doing inpainting workflows
  - *From: A.I.Warper*

- **Reduce VACE encode strength and add detailed prompt if you want to change it a lot**
  - Context: When making significant changes with VACE
  - *From: VK (5080 128gb)*

- **Reduce Vace_end_percent for better inpainting blending**
  - Context: Top is 1 and bottom is 0.80 for comparison
  - *From: VK (5080 128gb)*

- **Lower CausVid LoRA to 3.5 range and adjust shift value in sampler**
  - Context: Too strong CausVid negates VACE controls
  - *From: Guey.KhalaMari*

- **Switch off freenoise on context options**
  - Context: When using sliding context for longer videos
  - *From: chrisd0073*

- **Use CausVid at 0.5 strength to avoid artifacts**
  - Context: When using CausVid with Phantom to prevent quality issues
  - *From: Kijai*

- **Use CFG ending at 0.1 with CausVid**
  - Context: For better results with CausVid acceleration
  - *From: Kijai*

- **Set TeaCache threshold to 0.2**
  - Context: For optimal performance balance
  - *From: Kijai*

- **Use two VACE encode nodes for different strengths**
  - Context: One with depth and one with reference to play with strength values
  - *From: Kijai*

- **Set Phantom CFG high (5) and sampler CFG to 1**
  - Context: For decent results when using caus+vace+phantom together
  - *From: DawnII*

- **Don't mix pose and depth controlnets**
  - Context: Generally not good idea, depth and normals can be mixed
  - *From: David Snow*

- **Prompt for specific colors to help with VACE color shifts**
  - Context: Prompting for colours actually helps quite a bit with color shifts
  - *From: pom*

- **Don't pass ref image to VACE when combining with Phantom embeds**
  - Context: When using VACE encode with Phantom embeds
  - *From: aikitoria*

- **Use encoder strength 0.4-0.5 for original video input**
  - Context: When using original video as control input in multi-encoder setup
  - *From: VRGameDevGirl84(RTX 5090)*

- **Keep source video at original frame rate**
  - Context: When doing v2v or using source video for controlnets, don't convert to 16fps
  - *From: David Snow*

- **Use AccVid at 1.5 and CausVid at 0.5 for best results**
  - Context: When combining both LoRAs for speed and quality
  - *From: David Snow*

- **Use cfg scheduling instead of fixed cfg**
  - Context: CFG doesn't do much after halfway through steps, so schedule it for best results
  - *From: Kijai*

- **Add 16 more frames then cut first 16 to avoid flash**
  - Context: When flash appears in first second of output
  - *From: Johnjohn7855*

- **Use only 1 image with black image in other slot to avoid flash**
  - Context: When using Phantom with multiple image inputs
  - *From: Thom293*

- **Use simple/short prompts to avoid flash issues**
  - Context: Long prompts can cause flash problems, especially with inpainting
  - *From: pom*

- **Be precise with prompts for context windows**
  - Context: Don't give model too much freedom to change between windows, describe clothing, aspects, etc.
  - *From: Kijai*

- **Use white background for reference images**
  - Context: Phantom requires white background for source images, especially if removing background
  - *From: Kijai*

- **VACE reference image helps with consistency**
  - Context: Using VACE reference image helps a lot with maintaining consistency across context windows
  - *From: Kijai*

- **Add 'mute' to positive prompt to prevent talking**
  - Context: Alternative to negative prompting for reducing unwanted speech
  - *From: Ro*

- **Multiple LoRAs work well together**
  - Context: Combination of causvid 0.4 + accvid 1.5 + moviigen 0.4 + detailz 0.9 works well
  - *From: Johnjohn7855*

- **Use Shift+Ctrl+V to paste nodes while keeping connections**
  - Context: When copying groups of nodes in ComfyUI
  - *From: David Snow*

- **Prompt 'walking towards the camera' for better inpainting results**
  - Context: When using phantom with VACE inpainting
  - *From: David Snow*

- **Use separate VACE encodes to control each input strength individually**
  - Context: When combining multiple controls like ref image, depth, and lineart
  - *From: hau*

- **Add 'face visible' to prompt when face isn't appearing**
  - Context: When using VACE reference images
  - *From: hau*

- **Consider using original video input at low strength for better control**
  - Context: Helps with mouth movement and character positioning
  - *From: VRGameDevGirl84(RTX 5090)*

- **Use prompting for better Uni3C results**
  - Context: Better to use rough camera language to describe movements when using Uni3C
  - *From: slmonker(5090D 32GB)*

- **Lower shift value for better reference preservation**
  - Context: When using 1.3b phantom, lowering the shift preserves details from reference images better
  - *From: Johnjohn7855*

- **Use reactor face swap before video combine**
  - Context: To maintain face ID when using phantom + vace inpainting
  - *From: Johnjohn7855*

- **Smaller face = lower chances for face movements**
  - Context: Face size affects the ability to capture facial movements in generation
  - *From: DeZoomer*

- **Blur Wan outputs before using Starlight upscaler**
  - Context: Starlight is trained on blurred images, so adding small blur removes blocks and improves temperature
  - *From: chrisd0073*

- **Reduce block swap amount until 95% VRAM usage**
  - Context: For optimal performance when using block swapping
  - *From: Kijai*

- **Lower denoising and reduce reference strength**
  - Context: Decreasing lora strength helps preserve original face movements but loses likeness, adding ref image with ~0.2 strength helps recover it
  - *From: DeZoomer*

- **Use live preview to detect Phantom failures early**
  - Context: Can tell after 5-10 steps if generation will fail, restart with new seed
  - *From: aikitoria*

- **Prompt Phantom with single blurb describing final image, use keywords relating to reference images**
  - Context: Don't describe reference images directly, describe what you want to keep from them
  - *From: aikitoria*

- **Use simple prompts with Phantom and VACE**
  - Context: Extensive descriptions take away focus from reference image identity
  - *From: Johnjohn7855*

- **Send multiple reference images frame by frame rather than combined**
  - Context: Better results when feeding images separately to Phantom
  - *From: hicho*

- **Use DocVQA mode in Florence for outfit descriptions**
  - Context: Gives simple one-sentence color descriptions perfect for Phantom outfit reference
  - *From: Johnjohn7855*

- **Use low CFG for few steps without losing much speed**
  - Context: When using distilled models to get some benefit from CFG
  - *From: Kijai*

- **Describe reference images in prompts for character consistency**
  - Context: Model wants description of each ref image every time
  - *From: AJO*

- **Use CausVid at 0.5 strength for better results**
  - Context: Found good balance with causvid 0.5 + accvid 0.5
  - *From: Ada*

- **Expand mask area to avoid halos in VACE**
  - Context: When using VACE inpainting to prevent artifacts
  - *From: MilesCorban*

- **Use CFG for first 2-4 steps then disable**
  - Context: With 6-8 step generations using CausVid
  - *From: Kijai*

- **CausVid loras can be pushed quite far in strength**
  - Context: causvid 0.5 / accvideo 1.5 or causvid 1.0 / accvideo 2.0 work well
  - *From: David Snow*

- **Use CFG scheduling with early high CFG only**
  - Context: CFG 5 for first step/few steps, then lower to 1 for distilled models
  - *From: Johnjohn7855*

- **For distilled models, CFG 5 may be too much**
  - Context: If it burns/over-saturates, lower the CFG
  - *From: Kijai*

- **Add unbatch video node between VAE and video combiner when looping**
  - Context: To get separate videos out instead of one combined video
  - *From: AJO*

- **Stationary anchor points are important in ATI trajectory control**
  - Context: For proper motion control with trajectory system
  - *From: Kijai*

- **Use close-up reference images for better results**
  - Context: Up close reference images work better than distant shots
  - *From: VRGameDevGirl84(RTX 5090)*

- **HD LoRAs really amp up the models**
  - Context: Using high-definition LoRAs provides significant quality improvements
  - *From: Thom293*

- **Merging is the way to greatness**
  - Context: Create entirely new models by merging multiple LoRAs, then add more LoRAs on top
  - *From: Thom293*

- **Film-like outputs preserve dynamic range**
  - Context: Choose flatter, less saturated outputs for better post-processing flexibility
  - *From: Ruairi Robinson*

- **Use film grain settings of 0.03 for all parameters**
  - Context: When fixing reactor jitter, don't go over 0.1 or effect is too much
  - *From: Johnjohn7855*

- **Use separate encoders for each control type**
  - Context: For VACE controls like depth and normal, allows individual strength adjustment
  - *From: Johnjohn7855*

- **Lower strength for lineart/canny controls**
  - Context: Otherwise the lines will appear in the outputs
  - *From: Johnjohn7855*

- **Use anchor points that don't move in ATI**
  - Context: To avoid only getting camera motion with single track
  - *From: Kijai*

- **Shift click to add more points in spline editor**
  - Context: For creating complex motion paths in ATI
  - *From: Kijai*

- **Few trajectory points are sufficient for good results**
  - Context: When using trajectory-based controls, similar to TORA
  - *From: Kijai*

- **Eye correction can be done with VACE but requires advanced techniques**
  - Context: For precise facial animation control
  - *From: chrisd0073*

- **Easy approach leaves you at mercy of seed, advanced approach gives full control but takes longer**
  - Context: When doing facial animation work
  - *From: chrisd0073*

- **VACE works best with base AI case scenarios - people in controlled environments rather than extreme motion**
  - Context: For optimal face tracking and animation results
  - *From: chrisd0073*


## News & Updates

- **Fun 1.1 models released with reference image support**
  - New feature allowing reference image input, can be used with start image too
  - *From: Kijai*

- **CausVid model available - 4-step distilled version**
  - Claims to distill 50-step diffusion into 4-step generator with 9.4 FPS streaming
  - *From: David Snow*

- **New Framepack model released**
  - https://huggingface.co/lllyasviel/FramePack_F1_I2V_HY_20250503/tree/main
  - *From: slmonker(5090D 32GB)*

- **Judy Hopps LoRA updated for Wan2.1 14B**
  - Released on Civitai, was previously for different model
  - *From: MisterMango*

- **14B VACE model development in progress**
  - Updates visible on dev branch, expected to be game changer
  - *From: JohnDopamine*

- **LTXV 13B released**
  - New model release discussed in LTXV channel
  - *From: Gateway {Dreaming Computers}*

- **CausVid model available for Wan 2.1**
  - Generate videos in seconds, but no UI implementations yet
  - *From: yi*

- **VACE 14B mentioned in code**
  - Code referencing VACE 14B was added yesterday, indicating potential release
  - *From: Kijai*

- **Distilled faster Wan model exists**
  - They have a faster distilled model mentioned in the paper but haven't released it yet
  - *From: Kijai*

- **New no_ffn parameter appeared**
  - no_ffn parameter was added about a week ago
  - *From: Dream Making*

- **VACE 14B released**
  - May 14 release announced on Wan2.1 dev branch, model links not working yet
  - *From: JohnDopamine*

- **CausVid I2V code added**
  - I2V implementation added to repository 2 hours ago
  - *From: Kijai*

- **CausVid distilled models available**
  - Step and CFG distilled 14B model working with 2-4 steps
  - *From: yi*

- **Skyreels V2 roadmap includes CFG and step distillation**
  - Also AccVideo author has it on roadmap
  - *From: yi*

- **VACE 14B and 1.3B official release**
  - Released at 22:00 Beijing time 14/5, both 1.3B and 14B variants available
  - *From: slmonker(5090D 32GB)*

- **MoviiGen 1.1 released**
  - New model based on WAN 2.1, can do 1080p, appears to be FP32 format
  - *From: Njb*

- **New sliding window Wan kernel on GitHub**
  - Available for Hopper architecture only
  - *From: deleted_user_2ca1923442ba*

- **VACE 14B released**
  - 14B VACE module now available, uses different architecture than 1.3B
  - *From: community*

- **HuggingFace gate removed for VACE**
  - Models now freely downloadable
  - *From: Kijai*

- **New VACE 1.3B final version released**
  - Improved version with different characteristics than preview
  - *From: community*

- **New wrapper update available**
  - Updates needed for 14B VACE compatibility
  - *From: Dream Making*

- **Index-anisora v2 model released**
  - Wan 14B finetune for anime/multi-style generation, compatible with VACE
  - *From: A.I.Warper*

- **MoviiGen 1.1 released**
  - Available in Q3 quantization, works with standard Wan workflows
  - *From: The Punisher*

- **Official Comfy repackaged VACE 14B model**
  - 35GB model that doesn't suffer from two tail problem
  - *From: comfy*

- **14B VACE model weights have been released**
  - Available on HuggingFace, multiple variants including FP8
  - *From: Vincent_luo*

- **CausVid LoRA extracted and released**
  - Wan21_CausVid_14B_T2V_lora_rank32.safetensors available on Kijai's HuggingFace
  - *From: Kijai*

- **New depth processor added to VACE annotators**
  - They may have switched from midas in training
  - *From: DawnII*

- **CausVid converted to LoRA format for compatibility**
  - Allows combining with VACE and other LoRAs, though not used as originally intended
  - *From: Kijai*

- **I2V model referenced in code but not openly shared yet**
  - Alibaba has I2V model according to code updates but not publicly available
  - *From: Kijai*

- **VACE 14B module released**
  - Can now use 14B VACE as module instead of full model
  - *From: multiple users*

- **CausVid LoRA versions available for both 1.3B and 14B**
  - Kijai extracted CausVid models as LoRAs for better compatibility with VACE
  - *From: Kijai*

- **Index-anisora model announced**
  - New anime model based on Wan14B, V2 version, files appearing on HuggingFace
  - *From: slmonker(5090D 32GB)*

- **Marigold 1.1 models released**
  - Includes intrinsics model, new depth and normal model, released yesterday
  - *From: Kijai*

- **CausVid LoRA extracted for both 1.3B and 14B models**
  - Available on Kijai's HuggingFace repo
  - *From: DawnII*

- **Official 1.3B VACE full model released**
  - 6GB model available at Wan-AI/Wan2.1-VACE-1.3B
  - *From: slmonker(5090D 32GB)*

- **VACE 14B GGUF quantizations available**
  - Q3_K_S and Q8_0 versions tested and working, Q4_K_S and Q5_K_S in progress
  - *From: The Punisher*

- **Wrapper nodes updated for VACE compatibility**
  - Need to update wrapper nodes to use new VACE modules, released yesterday
  - *From: ˗ˏˋ⚡ˎˊ-*

- **T2V LoRAs for 14B model released**
  - Collection of T2V LoRAs specifically for Wan 14B model
  - *From: ˗ˏˋ⚡ˎˊ-*

- **VACE 14B GGUF models released**
  - Q3_K_S, Q5_K_S, Q6 variants available for native ComfyUI use
  - *From: The Punisher*

- **Hunyuan Image expected to release**
  - Speculation about release timing, open source status unclear
  - *From: The Punisher*

- **CausVid repo updated with warping_4step model**
  - New autoregressive_checkpoint_warp_4step_cfg2 model released 7 hours ago on HuggingFace
  - *From: JohnDopamine*

- **MoviiGen training and inference code released**
  - ZulutionAI released training/inference code on GitHub, was private until May 17
  - *From: JohnDopamine*

- **MoviiGen 1.1 Prompt Rewriter uploaded to HF**
  - New model for prompt enhancement uploaded by MoviiGen developers
  - *From: JohnDopamine*

- **ComfyUI native VACE support released**
  - Official ComfyUI documentation and workflows now available
  - *From: jerms_ai_(4090_24g)*

- **Better CausVid version will remain closed source**
  - Original CausVid team keeping improved version proprietary, trained on 400K videos vs 15K in open version
  - *From: Ada*

- **ComfyUI widgets now have inputs by default**
  - Latest ComfyUI version automatically adds inputs to widgets, eliminating need to manually convert
  - *From: traxxas25*

- **New captioning model from ByteDance**
  - Seed1.5-VL described as best new captioning model
  - *From: Ada*

- **New 4-step CausVid checkpoint released for 1.3B model**
  - 4 steps with cfg 2, available at tianweiy/CausVid autoregressive_checkpoint_warp_4step_cfg2
  - *From: hicho*

- **Tiling support added for I2V high resolution generation**
  - Can now generate 1280x1280 I2V after Kijai added tiling support
  - *From: DiXiao*

- **New Origami LoRA available for WAN**
  - shauray/Origami_WanLora on HuggingFace
  - *From: hicho*

- **WAN VACE 1.3B no longer preview version**
  - New model released last week with more contrast and better control embeds
  - *From: Blink*

- **Native VACE module support in development**
  - The Punisher successfully created native ComfyUI support for VACE modules, though still needs GGUF and Sage attention fixes
  - *From: The Punisher*

- **Wan model separation added to Civitai**
  - Models are now organized separately on the platform
  - *From: DiXiao*

- **MTVCrafter released - WAN-based model**
  - New 21B parameter model based on WAN architecture for video generation
  - *From: yi*

- **TeaCache memory optimization fixed in wrapper**
  - Fixed unnecessary 750MB VRAM usage in TeaCache by optimizing clone/device operations
  - *From: Kijai*

- **ComfyUI torch compile fix available**
  - PR available to fix loras and other features not working with torch compile node
  - *From: Kosinkadink*

- **Veo 3 released with dialogue capabilities and advanced prompt following**
  - Google's new model can generate videos with realistic dialogue and complex scene understanding, priced at $249/month
  - *From: Draken*

- **VACE 14B significantly outperforms previous versions**
  - Major improvement over 1.3B and HY Custom models
  - *From: AJO*

- **RealisDance-DiT weights released**
  - Controllable dance video generation model weights now available on HuggingFace
  - *From: yi*

- **Updated torch.compile wrapper**
  - Added proper wrapper for torch.compile into ComfyUI core. Now works with LoRAs without special patching. Can target only transformer blocks for faster recompilation
  - *From: Kijai*

- **Added VACE strength control over timesteps**
  - Added list support for VACE strength values - can control strength over timesteps with list of floats same length as steps
  - *From: Kijai*

- **VACE is supported in native ComfyUI**
  - Has been supported for about a week
  - *From: Kosinkadink*

- **Lora masking implemented into core ComfyUI**
  - Not just for AnimateDiff but implemented into core ComfyUI
  - *From: Kosinkadink*

- **Custom node for VACE with native being developed**
  - Don't know if it's been released yet
  - *From: David Snow*

- **TheDirector workflow available on Civitai**
  - Latest working version of automated movie generation workflow that won $800 in MimicPC AI Influencer competition
  - *From: AJO*

- **Minecraft LoRA created for WAN 2.1 T2V 14B**
  - Custom LoRA for Minecraft content generation, coming soon
  - *From: MisterMango*

- **Minecraft LoRA available for Wan 2.1 14B**
  - New Minecraft LoRA released for the 14B model, can be found in showcase channel
  - *From: MisterMango*

- **MoviiGen with VACE now available as GGUF**
  - MoviiGen 1.1 with VACE control uploaded as GGUF quantizations to HuggingFace
  - *From: The Punisher*

- **FantasyTalking model input added**
  - New fantasytalking_model input added to WanVideo model loader for lip sync, limited to 3 seconds
  - *From: seitanism*

- **Jenga inference pipeline released**
  - Novel pipeline combining dynamic attention carving with progressive resolution generation for speedup
  - *From: mamad8*

- **Native ComfyUI now supports VACE**
  - VACE support added to native ComfyUI workflows a few days ago
  - *From: zelgo_*

- **Phantom 14B model release planned**
  - Phantom has 14B release on its roadmap
  - *From: Kijai*

- **New UltraSharpV2 upscaler released**
  - DAT version of upscaler available on HuggingFace
  - *From: DawnII*

- **ComfyUI pose interpolation repo updated**
  - Modified version with timing control for pose appearance uploaded 12 minutes ago
  - *From: toyxyz*

- **ComfyUI has Wan templates in official UI**
  - Templates available in workflow browser, need latest version
  - *From: Gateway {Dreaming Computers}*

- **SkyReels CausVid model released**
  - Merged model combining SkyReels and CausVid available on HuggingFace
  - *From: hicho*

- **RTX 6000 Blackwell 96GB available for testing**
  - 2x faster than RTX4090, free trial available through simplepod.ai
  - *From: Tytanick*

- **New Remade LoRAs released**
  - Wan2.1 14B 480p I2V LoRAs collection available
  - *From: DawnII*

- **MisterMango war vehicles pack available**
  - Wan2.1 T2V 14B war vehicles pack posted in loras channel
  - *From: MisterMango*

- **New AccVideo WanX T2V 14B model released**
  - Distillation model similar to CausVid, available on HuggingFace
  - *From: JohnDopamine*

- **TheDenk released ControlNet models for Wan**
  - HED ControlNet for both 1.3B and 14B T2V models on HuggingFace
  - *From: hicho*

- **Gateway releasing comprehensive workflow package**
  - CN extraction workflow, Flux workflow with Redux/depth/PuLID, and Wan VACE/CausVid workflow
  - *From: Gateway {Dreaming Computers}*

- **AccVid LoRA released**
  - Kijai released Wan21_AccVid_T2V_14B_lora_rank32_fp16.safetensors
  - *From: Kijai*

- **Uni3C camera control for Wan**
  - Camera control controlnet available, works with new Wan HED controlnet
  - *From: slmonker(5090D 32GB), hicho*

- **OmniConsistency for first frame styling**
  - Flux-related tool for first frame styling that can overlap with VACE functionality
  - *From: happy.j*

- **BAGEL ComfyUI implementation available**
  - ComfyUI nodes for BAGEL released but performance is poor
  - *From: fazeaction, slmonker(5090D 32GB)*

- **Jenga research paper released**
  - New research about faster generation or training, unclear if practical application
  - *From: hicho*

- **Phantom 14B model released**
  - Available on HuggingFace, trained on 480P data but can work at 720P+
  - *From: DawnII*

- **HunyuanPortrait released by Tencent**
  - Based on Stable Video Diffusion, not HunyuanVideo model
  - *From: Gateway {Dreaming Computers}*

- **HunyuanAvatar coming out this week**
  - Will be based on HunyuanVideo model
  - *From: Kijai*

- **Torch compile bug fixed in WanVideoWrapper**
  - Had silly mistake for 10 days that ignored torch compile arguments, fixed yesterday
  - *From: Kijai*

- **New WAN ControlNet depth model released**
  - TheDenk/wan2.1-t2v-14b-controlnet-depth-v1 available on HuggingFace
  - *From: hicho*

- **Phantom CFG scheduling support added**
  - Need to update nodes as CFG scheduling for Phantom was just added today
  - *From: Kijai*

- **TAEW (Tiny Auto Encoder WAN) experimental support**
  - TAEW2_1.safetensors model for much higher quality preview, requires placement in comfyui/models/vae_approx folder
  - *From: Kijai*

- **Phantom model released**
  - New T2V model that works with reference latents, requires 121 frames at 24fps
  - *From: multiple users*

- **Two new lipsync models released**
  - Released in lipsync channel
  - *From: TK_999*

- **New Wan21_T2V_14B_MoviiGen_lora released**
  - Kijai released untested MoviiGen LoRA for T2V model
  - *From: Kijai*

- **Controlnet support and partial uni3c support added**
  - New controlnet support added with partial uni3c controlnet support (no camera embed stuff yet)
  - *From: Kijai*

- **Phantom cfg scheduling support added**
  - Recent updates allow scheduling phantom cfg among other small changes
  - *From: Kijai*

- **Hakoniwa anime wan model released**
  - svjack released hakoniwa_anime_wan2_1_models - anime style adjusted model
  - *From: DawnII*

- **HD/Pro version of Wan appearing on HuggingFace**
  - aikitoria spotted HD version appearing on HF, not final form yet
  - *From: aikitoria*

- **Depth ControlNet released for Wan**
  - New depth controlnet available that works with Phantom and T2V models
  - *From: Kijai*

- **MoviiGen LoRA released**
  - New LoRA for detail enhancement and noise cleanup, affects character likeness
  - *From: David Snow*

- **Uni3C controlnet released**
  - New controlnet for camera control using reference videos
  - *From: David Snow*

- **Native ComfyUI VACE implementation working**
  - VACE can now patch other models natively in ComfyUI within the lazy eval patching system
  - *From: Ablejones*

- **John Dopamine created faster Phantom merge**
  - Custom merged model that provides faster inference than standard Phantom
  - *From: Thom293*

- **Camera motion LoRAs updated**
  - Some camera motion loras were updated 3 days ago and might work with VACE as alternative to Uni3C
  - *From: Johnjohn7855*

- **Jenga dev-wan branch available**
  - New development branch for Jenga targeting Wan models appeared on GitHub
  - *From: JohnDopamine*

- **VORTA claims 14x speed up**
  - New speed optimization claiming significant performance improvement, though with usual caveats about VRAM costs
  - *From: Kijai*

- **DiffPhy project improves physics**
  - New project trained LoRA on top of Wan to hugely improve physics simulation
  - *From: pom*

- **Native Phantom support added to ComfyUI**
  - New node WanPhantomSubjectToVideo added with two negative outputs
  - *From: The Punisher*

- **Flux 1 Kontext announced by Black Forest Labs**
  - Official context multimodal editing model, not open-sourced yet
  - *From: slmonker*

- **GGUF quantizations of Phantom 14B released**
  - Q8 and other quantizations available on HuggingFace
  - *From: The Punisher*

- **New Wan model from ByteDance ATI**
  - Another new Wan model.. it's like daily occurance - trajectory model like TORA on steroids
  - *From: Kijai*

- **ByteDance released Dream-O ComfyUI implementation**
  - Semi-Wan related - could be helpful if it works
  - *From: JohnDopamine*

- **New LayerAnimate tech released**
  - More new tech: https://layeranimate.github.io
  - *From: DawnII*

- **Native ComfyUI now has VACE templates**
  - In the latest Comfy there are even templates for VACE
  - *From: zelgo_*

- **CausVid v2 LoRA released**
  - Can be used at strength 1.0, has block 0 already removed, no flash issues
  - *From: David Snow*

- **ATI model from ByteDance released**
  - Trajectory-based video generation with motion control via anchor points
  - *From: JohnDopamine*

- **Direct3D-S2 model released**
  - I-to-3D generation model
  - *From: Mngbg*

- **CausVid v1.5 no first block version released**
  - Released 3 hours after v2, has block 0 removed
  - *From: AJO*

- **New Phantom 14B model available**
  - Referred to as 'wondermus' model
  - *From: VRGameDevGirl84(RTX 5090)*

- **CausVid V2 released with speed improvements**
  - Significantly faster generation times compared to previous versions
  - *From: VRGameDevGirl84(RTX 5090)*

- **ATI (motion control) released for Wan**
  - Allows spline-based motion control, needs better interface for drawing
  - *From: Kijai*

- **CausVid v2 available**
  - Tuned differently than v1, requires CFG scheduling
  - *From: Johnjohn7855*


## Workflows & Use Cases

- **Two-stage video transition**
  - Use case: Creating smooth transitions between aerial and ground views
  - *From: notid*

- **LTX Five sampler setup for batch generation**
  - Use case: Generating 1000 videos overnight with multiple parallel generations to pick best results
  - *From: David Snow*

- **Fun Control with reference + start image**
  - Use case: Better control results by using both reference and start images
  - *From: Nathan Shipley*

- **Fun 1.1 then VACE refinement**
  - Use case: Run Fun 1.1 with reference, then use first frame for VACE to get better results
  - *From: Hashu*

- **Two-pass v2v for strong stylization**
  - Use case: Getting better style transfer at low step counts (6-7 steps total). First sampler 2-3 steps, second sampler 4 steps for refinement
  - *From: David Snow*

- **V2V workflow shared for stylization**
  - Use case: V2V tests with LoRAs, needs both sets of preprocessors despite slower speed. Different videos require different settings
  - *From: David Snow*

- **Double pass workflow with DepthCrafter**
  - Use case: Long consistent video generation with control, uses depth crafter and ex lora with context options
  - *From: David Snow*

- **First-Frame-Last-Frame inpainting setup**
  - Use case: VACE inpainting requiring inpainted first frame as guide with gray surrounding areas
  - *From: ArtOfficial*

- **Text-to-documentary maker using DF**
  - Use case: Automated documentary creation workflow using DiffusionForcing
  - *From: Colin*

- **DF video extension with 3 sections**
  - Use case: Creating longer videos by chaining multiple 5-second generations
  - *From: MilesCorban*

- **Style transfer with WAN**
  - Use case: Transferring style without structure using new method
  - *From: Clownshark Batwing*

- **Multi-pass workflow with depth controlnet**
  - Use case: Style transfer-like approach using depth control
  - *From: Ablejones*

- **NormalCrafter + DepthCrafter + Blender relighting**
  - Use case: Video relighting using normal maps generated from video
  - *From: David Snow*

- **Redux+Fill+ControlNet+InstantID for start-end frames**
  - Use case: Creating consistent character videos with FLF2V by generating controllable start and end frames
  - *From: slmonker(5090D 32GB)*

- **VACE + hires pass workflow**
  - Use case: Improving VACE output quality with upscaling pass
  - *From: Dream Making*

- **Control 1.3 + ref image + mask + AnimateDiff + Ultimate SD upscale**
  - Use case: 720 to 1920 upscaling pipeline taking around 30 minutes
  - *From: Gavmakes*

- **Consistent character generation using Redux + ACE++ Fill + InstantID**
  - Use case: Creating start/end frames for character animation
  - *From: slmonker*

- **CausVid basic inference with 4 steps, CFG 1.0**
  - Use case: Fast video generation in 2-5 minutes
  - *From: Vérole*

- **Real-time video generation with CausVid**
  - Use case: Generate videos in sliding window with real-time preview using kv_cache
  - *From: Kijai*

- **UniAnimate with MoviiGen**
  - Use case: UniAnimate could work with the MoviiGen model
  - *From: Kijai*

- **Combining VACE and Phantom**
  - Use case: Possible to connect both for advantages of each, but results unpredictable
  - *From: DawnII*

- **Start/end frame morphing with VACE**
  - Use case: Video transitions between two frames
  - *From: multiple users*

- **Face control with VACE using mediapipe/dwpose**
  - Use case: Facial animation and lip sync
  - *From: Kijai*

- **VACE with Causvid for faster inference**
  - Use case: Speed up generation while maintaining quality
  - *From: DawnII*

- **VACE outpainting**
  - Use case: Extending video canvas spatially
  - *From: Kijai*

- **Start/end frame morphing with VACE**
  - Use case: Creating smooth transitions between two unrelated images
  - *From: David Snow*

- **Context options for long videos**
  - Use case: Splitting 810 frames into 10 batches with 81 frame contexts and overlap
  - *From: Valle*

- **Temporal extension with CausVid**
  - Use case: Extending video length beyond base model capabilities
  - *From: DawnII*

- **Use CausVid LoRA with VACE at reduced strength**
  - Use case: Fast 4-step generation with good quality, compatible with VACE
  - *From: Kijai*

- **Multiple VACE encoders for control blending**
  - Use case: Blending different control inputs like depth and canny
  - *From: Kijai*

- **Use reference image instead of first frame for longer videos**
  - Use case: Better consistency for context options and longer processing
  - *From: Kijai*

- **CausVid LoRA + VACE + 14B model for fast generation**
  - Use case: High quality video generation in ~1 minute instead of 5+ minutes
  - *From: seruva19*

- **CausVid + UniAnimate for character animation**
  - Use case: Character-driven video generation with distillation speedup
  - *From: Kijai*

- **Skyreels DF with CausVid for long videos**
  - Use case: Chained generation for extended video lengths
  - *From: DawnII*

- **Video extension with 13 frame overlap using VACE 14B**
  - Use case: Extending videos while maintaining continuity
  - *From: Ablejones*

- **Chaining 81-frame runs using last frame as reference**
  - Use case: Creating longer videos (162+ frames) by connecting multiple generations
  - *From: A.I.Warper*

- **VACE with optical flow control input**
  - Use case: Using optical flow as control method for video generation
  - *From: DawnII*

- **HiDream with RF_inversion for reference images**
  - Use case: Creating reference-based generations without needing adapters
  - *From: A.I.Warper*

- **Multiple VACE encoders for complex control**
  - Use case: Separating depth, pose, and mediapipe face controls into different encoders
  - *From: David Snow*

- **Context options for long video generation**
  - Use case: Generating 10+ second videos, up to 9 seconds at 24fps demonstrated
  - *From: Valle*

- **CausVid with VACE for fast I2V**
  - Use case: Quick character animation with reference image and control
  - *From: slmonker(5090D 32GB)*

- **NormalCrafter + detail transfer for normal creation**
  - Use case: Creating normal maps for relighting
  - *From: David Snow*

- **Multi-step resolution upscaling with CausVid**
  - Use case: Generate low res then upscale latent for higher resolution output
  - *From: DiXiao*

- **Generate poses from video for VACE**
  - Use case: Use Dwpose preprocessor then blend with depth or other controls using image blend node
  - *From: cyncratic*

- **Multiple VACE controls**
  - Use case: Chain multiple VACE embed nodes using prev_embeds input instead of combining controls in single pass
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Multi-part video stitching with VACE**
  - Use case: Creating longer videos by generating 41-frame segments and stitching with last frame as next start
  - *From: A.I.Warper*

- **Two-pass VACE processing**
  - Use case: Generate with 14B VACE then cleanup with 1.3B model for quality improvement
  - *From: David Snow*

- **Style transfer with HiDream + VACE**
  - Use case: Combining HiDream preprocessing with VACE for style transfer applications
  - *From: Clownshark Batwing*

- **Will Smith video using 3 sequential 81-frame generations**
  - Use case: Long video creation by forwarding 8 frames and adding new end frame each time
  - *From: DawnII*

- **Style guide video transfer**
  - Use case: Encoding one video and using as style guide for another video generation
  - *From: Clownshark Batwing*

- **VACE multi-control setup**
  - Use case: Chaining embeds for depth, inpainting, and reference controls
  - *From: DawnII*

- **V2V with pose control using VACE**
  - Use case: Complex shot replication using begin frame, end frame, and pose control without depth or line controls
  - *From: jerms_ai_(4090_24g)*

- **VACE with T2V model for I2V simulation**
  - Use case: Faster I2V generation by using VACE with start image only and T2V model + CausVid LoRA
  - *From: N0NSens*

- **Context-based long video generation**
  - Use case: Generate videos up to 300+ frames by chunking into 81-frame segments, though context switches may cause jumps
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Flux + VACE automated pipeline**
  - Use case: Auto-generates reference image from first frame using Flux T2I, then uses it with VACE for video generation
  - *From: VRGameDevGirl84(RTX 5090)*

- **Two-pass depth + CausVid generation**
  - Use case: First pass for motion, second pass for quality enhancement using depth control
  - *From: BestWind*

- **V2V with samples input**
  - Use case: Encode input frames with WanVideoEncode and use samples input with denoise below 1.0 for video-to-video
  - *From: ˗ˏˋ⚡ˎˊ-*

- **VACE inpainting with pose control in masked regions**
  - Use case: Control pose only in specific masked areas of video while preserving background
  - *From: aipmaster*

- **Face replacement using VACE with reference character**
  - Use case: Replace face of character with any reference, works on 3090
  - *From: BestWind*

- **Iterative latent upscale with VACE triple sampler**
  - Use case: Video restyle with progressive quality improvement using depth and pose blend
  - *From: yo9o*

- **CausVid + Fantasy Talking combination**
  - Use case: Fast lip-sync generation at 81 frames, 720x720, 5 steps
  - *From: VRGameDevGirl84(RTX 5090)*

- **Combined depth and pose VACE processing**
  - Use case: Better facial movement control by combining multiple preprocessors
  - *From: VRGameDevGirl84(RTX 5090)*

- **Multi-encoder VACE setup**
  - Use case: Using separate encoders for pose (higher strength) and depth (lower strength) gives more control over output
  - *From: MilesCorban*

- **Context for long videos**
  - Use case: Using context node with wrapper allows generation of 401+ frames, though may lose some info between chunks
  - *From: ˗ˏˋ⚡ˎˊ-*

- **VACE extension using last frames**
  - Use case: Feed last 4 frames from first run into second VACE encode to extend videos
  - *From: Draken*

- **Dual VACE/WAN 14B workflow for versatility and quality**
  - Use case: Combines VACE versatility with WAN 14B quality using both models together
  - *From: zelgo_*

- **Multiple VACE embeds with separate pose/depth encoders**
  - Use case: Better control than blending - first encoder with pose, second with depth at different strengths
  - *From: VRGameDevGirl84(RTX 5090)*

- **Chaining last frames from one generation as start of next**
  - Use case: Long video generation by using last frame as start frame in new encoders/samplers
  - *From: A.I.Warper*

- **VACE with normal maps for facial tracking**
  - Use case: Capturing facial expressions and movements using normal map control
  - *From: VRGameDevGirl84(RTX 5090)*

- **I2V with CausVid LoRA for speed**
  - Use case: Faster video generation with reduced steps
  - *From: DevouredBeef*

- **Double VACE control with depth and pose**
  - Use case: Creating more accurate character animations by combining two control types
  - *From: slmonker(5090D 32GB)*

- **VACE inpainting with masks**
  - Use case: Removing or replacing subjects in videos while retaining background
  - *From: MilesCorban*

- **Single frame WAN generation for consistency**
  - Use case: Using WAN T2V at one frame high resolution to generate consistent images for video clips instead of using separate models
  - *From: Thom293*

- **Video face replacement using reactor node**
  - Use case: Fast and easy face swapping in videos
  - *From: slmonker*

- **Multi-keyframe VACE setup using pad nodes**
  - Use case: Adding multiple control frames at specific intervals for complex camera movements
  - *From: Kijai*

- **Separate control and reference embed workflow**
  - Use case: Better results with 14B model when control and reference are processed separately
  - *From: Kijai*

- **Context window extension for long videos**
  - Use case: Generate videos longer than 81 frames using overlapping windows with blended seams
  - *From: Kijai*

- **Video extension using white frame padding**
  - Use case: Extend DWPose output video by padding with white frames
  - *From: MilesCorban*

- **Character replacement with masking**
  - Use case: Takes character, puts gray mask over them, composites with original to remove/replace character
  - *From: MilesCorban*

- **Direct input frame processing**
  - Use case: Use input video directly in input frames with reduced strength plus normal map for style transfer effects
  - *From: VRGameDevGirl84(RTX 5090)*

- **Two-pass video refinement**
  - Use case: Use first pass with VACE, then second pass with different model for refinement using encoded latents and denoise
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Video extension with gray frames**
  - Use case: For extending video, use solid gray frames for areas to generate and black masks for frames to preserve
  - *From: DawnII*

- **Text + control to video**
  - Use case: Use LoRA + WAN with DWPose control without reference image or input video, just text + control
  - *From: Neex*

- **Two-pass workflow using 1.3b for smoothing**
  - Use case: Use promptless 1.3b v2v second pass at low denoise, steps and CFG to smooth out CausVid artifacting
  - *From: Faust-SiN*

- **Face and body separate encoding**
  - Use case: Using one encoder for face and one for body to try to get better facial control
  - *From: VRGameDevGirl84(RTX 5090)*

- **Input video + normal map without latent sync**
  - Use case: Getting facial movement by using input video at 0.4 strength and normal map at 0.6 strength
  - *From: VRGameDevGirl84(RTX 5090)*

- **Two-stage character replacement**
  - Use case: Create initial video with rough character description, then use VACE with reference to replace character while preserving motion
  - *From: AJO*

- **Phantom + VACE + Causvid combination**
  - Use case: Using Phantom embed nodes with VACE embed input for better identity preservation in character animation
  - *From: Johnjohn7855*

- **Dual VACE embed setup**
  - Use case: Separate VACE embed nodes for reference image and control video to set different strengths for each input
  - *From: Johnjohn7855*

- **Video splitting for multiple processing**
  - Use case: Load one video and extract different frame ranges to different samplers using split_index parameter
  - *From: Boop*

- **Video extension with VACE using first 20 frames plus gray frames**
  - Use case: Extending video sequences by feeding initial frames and empty gray frames
  - *From: Rishi Pandey*

- **Multi-angle character generation using Wan i2v iterations**
  - Use case: Generate consistent character at different angles by using Wan itself to create viewpoint variations
  - *From: David Snow*

- **Face-only masking with DWPose body control**
  - Use case: Keep original face while changing everything else (hair, clothing, background)
  - *From: VRGameDevGirl84(RTX 5090)*

- **Start/end frame morphing with DWPose control**
  - Use case: Character morphing using pose control with defined start and end states
  - *From: David Snow*

- **Video extension with overlapping frames using VACE**
  - Use case: Creating longer videos by extending clips with seamless transitions
  - *From: ArtOfficial*

- **First-frame-last-frame morphing using VACE**
  - Use case: Creating smooth transitions between two different subjects or styles
  - *From: David Snow*

- **Get image or mask from batch method for video extension**
  - Use case: Simpler method for extending videos without reloading compressed video
  - *From: zelgo_*

- **Auto face masking for video processing**
  - Use case: Automatically mask face in input video for pose-driven face swapping
  - *From: VRGameDevGirl84(RTX 5090)*

- **SDXL first frame styling with VACE**
  - Use case: Style first frame with SDXL/Flux then use as reference image for VACE video processing
  - *From: Valle*

- **Multi-pass video extension technique**
  - Use case: Take last few frames from first pass and feed into another Wan instance, then combine passes for longer video
  - *From: Gateway {Dreaming Computers}*

- **Tiled video processing for higher resolution**
  - Use case: Start big 720p video, stop at 20% steps, cut into 4 tiles and do vid2vid on each to finish
  - *From: deleted_user_2ca1923442ba*

- **VACE inpainting with mask overlay**
  - Use case: Character replacement in video while maintaining scene context
  - *From: David Snow*

- **Overlapping batch processing for long videos**
  - Use case: Creating arbitrary length videos with maintained consistency
  - *From: notid*

- **Seamless looping workflow**
  - Use case: Creating perfectly looped video content
  - *From: The Shadow (NYC)*

- **SAM2 points editor for masking**
  - Use case: Creating precise masks for video editing
  - *From: David Snow*

- **VACE inpainting workflow with context options**
  - Use case: Character replacement and video extension up to thousands of frames
  - *From: David Snow*

- **Face replacement using face segmentation**
  - Use case: Single character face swapping with accurate masks
  - *From: David Snow*

- **Video extension with consistent color transitions**
  - Use case: Chaining videos using same 15 frames for seamless transitions
  - *From: Piblarg*

- **VACE inpainting workflow for subject removal/replacement**
  - Use case: Removing subjects from video and replacing with new content using masks and prompts
  - *From: David Snow*

- **Multi-key frame interpolation with VACE**
  - Use case: Using 4 image keys with pose control for video-to-video generation
  - *From: jerms_ai_(4090_24g)*

- **Batch video processing for long videos**
  - Use case: Processing long videos in chunks (80 frames at a time) and automatically combining results
  - *From: VRGameDevGirl84(RTX 5090)*

- **V2V with CausVid and Florence find and replace**
  - Use case: Video style transfer and modification
  - *From: hicho*

- **Multi-batch video extension with last frame reference**
  - Use case: Creating longer videos by using last frame as reference for next batch
  - *From: VRGameDevGirl84(RTX 5090)*

- **Motion extraction to VACE pipeline**
  - Use case: Extract motion controls from video, process first frame through Flux, then generate with VACE
  - *From: Gateway {Dreaming Computers}*

- **Multiple VACE encodes for character replacement**
  - Use case: Use RMBG to create mask, make mask gray, feed into VACE as control video. Second VACE node with openpose and reference image
  - *From: MilesCorban*

- **Chained VACE inputs for character insertion**
  - Use case: Chain guide inputs in wrapper for adding character to background without character
  - *From: TK_999*

- **Loop workflow with video concatenation**
  - Use case: For creating looping videos with Wan21 VACE
  - *From: daking999*

- **Inpainting with multiple control inputs**
  - Use case: Use expanded mask, depth, normals and pose in single VACE encode for inpainting
  - *From: David Snow*

- **VACE inpainting with pasteback**
  - Use case: Avoiding VAE compression when inpainting
  - *From: A.I.Warper*

- **Mask inversion for background inpainting**
  - Use case: Keeping character and replacing background instead of replacing character
  - *From: voxJT*

- **Multiple control inputs combined**
  - Use case: Inpaint mask, pose, depth and normal all into one encode
  - *From: David Snow*

- **Phantom with VACE module**
  - Use case: Using phantom example workflow from kijai and adding wan video vace encode node
  - *From: Johnjohn7855*

- **Phantom with dual reference images**
  - Use case: Character consistency with multiple reference points
  - *From: Kijai*

- **VACE + Phantom combination**
  - Use case: Better identity preservation than VACE ref alone
  - *From: Zuko*

- **CausVid with CFG scheduling**
  - Use case: Faster inference with quality preservation using CFG ending at 0.1
  - *From: Kijai*

- **Two VACE encode nodes with different strengths**
  - Use case: Separate control over depth and reference strength
  - *From: Kijai*

- **Multi-encoder VACE setup**
  - Use case: Individual strength control for control video, ref image, and input video
  - *From: VRGameDevGirl84(RTX 5090)*

- **Phantom with VACE combination**
  - Use case: Combining Phantom embeds with VACE encode for enhanced control
  - *From: multiple users*

- **Frame rate conversion for MMAudio**
  - Use case: Converting Wan 16fps output to 24fps for MMAudio compatibility
  - *From: Mngbg*

- **VACE loop workflow**
  - Use case: Creating looping videos, would be perfect except for Wan flash issue
  - *From: David Snow*

- **Phantom + VACE combination**
  - Use case: Extended duration videos using both models in tandem
  - *From: JohnDopamine*

- **3D-to-wan workflow**
  - Use case: Veo3 + Flux + Hunyuan3D + Wan with VACE pipeline
  - *From: Yae*

- **Uni3C controlnet for camera motion**
  - Use case: Transfer motion from existing videos, works with simple motions better than extreme ones like orbit
  - *From: Kijai*

- **Phantom + VACE inpainting**
  - Use case: Character replacement in existing videos with consistency
  - *From: David Snow*

- **Uni3C camera control**
  - Use case: Transfer camera movements from any video or 3D rendered sequence
  - *From: N0NSens*

- **Multiple LoRA stack**
  - Use case: Enhanced detail and speed with causvid + accvid + moviigen + detailz
  - *From: Johnjohn7855*

- **Four-image Phantom reference**
  - Use case: Complete subject coverage using multiple angles of same subject
  - *From: David Snow*

- **SAM2 points editor for mask creation**
  - Use case: Creating mask videos for VACE inpainting using subject tracking
  - *From: David Snow*

- **Face detailing with crop and stitch**
  - Use case: Detailed face processing by cropping face region, processing, and stitching back
  - *From: David Snow*

- **Multiple VACE encodes for control combination**
  - Use case: Using separate encodes for ref image, depth, and lineart with individual strength control
  - *From: JohnDopamine*

- **Phantom + VACE combination**
  - Use case: Combining Phantom character consistency with VACE controls
  - *From: VRGameDevGirl84(RTX 5090)*

- **Triple sample workflow with inpainting**
  - Use case: Combining inpainting functionality with triple sampling approach
  - *From: hau*

- **Moge to ComfyUI Load 3D workflow**
  - Use case: Convert image to glb using Moge, upload to Load 3D node, and record screen for 3D control
  - *From: toyxyz*

- **Over-engineered face replacement workflow**
  - Use case: Works for any video regardless of face size, potentially expandable to whole person replacement
  - *From: DeZoomer*

- **Wan i2v with Uni3C for FLF model**
  - Use case: Using Chinese prompts with FLF2V model and Uni3C for camera control
  - *From: Guey.KhalaMari*

- **Video enhancement/upscaling using loras**
  - Use case: Using existing low-res videos as input with LoRAs for enhancement, completed in 90.50 seconds with causVid
  - *From: VRGameDevGirl84(RTX 5090)*

- **VACE + Phantom inpainting with dual masking**
  - Use case: Character replacement while preserving background
  - *From: Zuko*

- **Phantom with LLM prompt generation**
  - Use case: Auto-generate detailed character and outfit descriptions for consistent Phantom results
  - *From: AJO*

- **Video game footage → Florence → Wan CausVid T2V**
  - Use case: Convert video game graphics with motion matching using low denoiser (0.10)
  - *From: hicho*

- **Automatic outfit designer workflow**
  - Use case: Automatically designing outfits for characters in video generation
  - *From: AJO*

- **CFG scheduling with CausVid**
  - Use case: 4 steps with 4 cfg and 4 without using end percent 0.5
  - *From: Ada*

- **Multi-reference image processing**
  - Use case: Using LLM to embed description text at start of every scene for character consistency
  - *From: AJO*

- **1st frame from vid > cosxl = init img, vace > depth from vid + init img = gen**
  - Use case: Alternative approach to video generation
  - *From: N0NSens*

- **5 scene looping with CausVid v2 and Phantom**
  - Use case: Creating multi-scene storyboards with consistent character
  - *From: AJO*

- **Batch prompt processing with phantom**
  - Use case: Creating multiple videos automatically from folder of prompts
  - *From: VRGameDevGirl84(RTX 5090)*

- **Face detailing with crop and reprocess**
  - Use case: Improving face quality in generated videos through cropping and re-generation
  - *From: mamad8*

- **ATI trajectory control**
  - Use case: Directing specific motion paths in video generation using anchor points
  - *From: Kijai*

- **Multi-prompt looping workflow**
  - Use case: Load prompts from text files, loop through them, encode and stitch together for music videos - 5 scenes in 254 seconds total
  - *From: VRGameDevGirl84(RTX 5090)*

- **Phantom + reference image + multiple LoRAs**
  - Use case: Character consistency with style enhancement using reference image, Phantom, CausVid V2, and detail LoRAs
  - *From: VRGameDevGirl84(RTX 5090)*

- **Reactor -> RIFE -> Film Grain for face consistency**
  - Use case: Reducing jitter from reactor face swapping across multiple scenes
  - *From: AJO*

- **One-shot story generation with costume consistency**
  - Use case: Generate complete stories with 1 ref image, 5 scenes, consistent character across scenes
  - *From: AJO*

- **Using latent sync for multi-scene consistency**
  - Use case: Creating consistent characters across multiple video scenes
  - *From: VRGameDevGirl84(RTX 5090)*

- **Two encoder setup for VACE controls**
  - Use case: Using both depth and normal maps with separate strength controls
  - *From: Johnjohn7855*

- **Using VACE for music video post-production fixes**
  - Use case: Fixing character consistency and doing edits on video generation outputs when direct editing is difficult
  - *From: Ruairi Robinson*


## Recommended Settings

- **CFG with SLG**: 3 (half of normal CFG)
  - SLG requires lower CFG values
  - *From: Miku*

- **Denoise for T2V**: 1.0
  - Never use other values unless doing vid2vid
  - *From: Kijai*

- **Block setting for 1.3B**: 8
  - Better results with 1.3B model
  - *From: Kijai*

- **Context frames for FantasyTalker**: 169
  - Works well with context windows, though math unclear
  - *From: Kijai*

- **Shift skip for loop_args**: Half of latents (e.g. 10 for 80 frames)
  - 4 frames per latent, so 80 frames = 20 latents, half = 10
  - *From: BondoMan*

- **VACE strength for skeleton lines**: 1.0
  - Counterintuitively helps avoid skeleton artifacts
  - *From: David Snow*

- **First pass steps for two-pass v2v**: 2-3 steps
  - LoRA effects strongest on 2nd step, diminish after 3rd step
  - *From: David Snow*

- **Second pass steps for two-pass v2v**: 4 steps
  - For refinement after first pass captures strong stylization
  - *From: David Snow*

- **DG model steps for T2V**: 6 steps
  - Usable results compared to 25-30 steps with base models
  - *From: David Snow*

- **V2V denoise for lip sync results**: 0.6
  - Good balance for following lips while maintaining style
  - *From: Jas*

- **Ex LoRA context frames**: 161 frames with overlap of 24
  - Enables long animation generation with proper blending
  - *From: David Snow*

- **Double pass sampling**: 3 and 6 samples split between two samplers, max 10 total
  - Fast generation while maintaining quality
  - *From: David Snow*

- **Line art thresholding for VACE**: 0.5 binary threshold
  - Makes control map more compatible with VACE training
  - *From: Rishi Pandey*

- **TeaCache with low steps**: Don't use TeaCache with 8 steps
  - 8 steps too low to benefit from TeaCache
  - *From: Draken*

- **FramePack chunk size**: 33 frame chunks
  - FP model was trained at 33 frame chunks
  - *From: Draken*

- **FP8**: disabled
  - RTX 3090 doesn't support FP8, causes compilation errors
  - *From: Juan Gea*

- **Frame overlap**: 4 frames
  - Optimal for video extension without excessive redundancy
  - *From: MilesCorban*

- **Shift parameter**: over 10
  - Required for movement in Skyreels v2
  - *From: Colin*

- **Resolution comparison**: 720p preferred over 480p
  - Same generation time but better prompt adherence
  - *From: N0NSens*

- **Frame chunks**: 81 frames
  - Recommended chunk size for context processing
  - *From: ˗ˏˋ⚡ˎˊ-*

- **RAM requirement**: 64GB minimum, 128GB preferred
  - 64GB fine for most use cases, 128GB needed for larger model conversions
  - *From: Kijai*

- **Resolution for 16GB VRAM**: 832x480 for 720p/81fr
  - Maximum resolution possible with 16GB VRAM
  - *From: N0NSens*

- **DepthAnything precision**: fp16
  - Prevents OOM on 4090 compared to fp32
  - *From: A.I.Warper*

- **CausVid steps**: 2-4 steps
  - 4 steps gets 90% quality, diminishing returns beyond
  - *From: yi*

- **CausVid CFG**: 1.0
  - CFG distilled model, higher values burn output
  - *From: Kijai*

- **Empty embed value**: 97
  - Fixes tensor size mismatch errors
  - *From: Dream Making*

- **Flex attention frame per block**: 3
  - Required for proper block mask operation
  - *From: Kijai*

- **Shift parameter for CausVid**: Any value
  - Parameter is ignored due to set timestep schedule
  - *From: Kijai*

- **CausVid steps**: 3 steps
  - 9 steps produces garbage results
  - *From: Kijai*

- **CausVid sampling**: one latent at a time in sliding window
  - How it's meant to be sampled with kv_cache
  - *From: Kijai*

- **CausVid window size**: 3 latents
  - Standard window size for sliding generation
  - *From: Kijai*

- **UniPC scheduler**: Works with 9 steps
  - 9 steps works with unipc scheduler
  - *From: aipmaster*

- **VACE block swapping**: Max 8 blocks for 14B
  - Hardware limitation and architecture design
  - *From: DawnII*

- **Causvid with VACE**: 3-4 steps, CFG 1.0
  - Optimal balance of speed and quality
  - *From: Kijai*

- **14B VACE resolution**: 720x720 or 1024x1024
  - Works better at higher resolutions
  - *From: Kijai*

- **VACE empty frame color**: 0=black, 1=white, 0.5=neutral gray
  - Controls background for masked areas
  - *From: Kijai*

- **vace_blocks_to_swap**: 8 for 14B model
  - Prevents OOM errors on RTX 4080 16GB
  - *From: DawnII*

- **CFG**: 2.0
  - Enables generation in 6 steps instead of 20-30
  - *From: David Snow*

- **steps**: 2 steps with CausVid
  - CausVid enables very low step generation
  - *From: Kijai*

- **VACE strength**: 1.5
  - Higher strength for better control
  - *From: Kijai*

- **context_overlap**: 16
  - Good default for blending batches in long videos
  - *From: David Snow*

- **CausVid LoRA strength**: 0.2-0.4
  - Sweet spot for quality, 0.2 loses quality, above 0.4 may be too strong
  - *From: Kijai*

- **Steps with CausVid LoRA**: 4
  - Appears to be sweet spot for quality vs speed
  - *From: Kijai*

- **CFG with CausVid**: 1.0
  - CausVid is CFG distilled, higher values don't work properly
  - *From: Kijai*

- **Block swap for 14B**: 20 for general, 5-7 for VACE
  - Memory management for large models
  - *From: JohnDopamine*

- **CausVid LoRA strength**: 0.4-0.6 with VACE, 0.8-0.9 with other LoRAs
  - Balance between quality and artifacts
  - *From: Kijai*

- **CFG scale**: 1.0
  - Required for CausVid distillation model
  - *From: Kijai*

- **Steps**: 4 steps
  - Optimal for CausVid distillation
  - *From: Kijai*

- **Block swap**: 30-40 for 3090, 8 VACE blocks
  - Manage VRAM usage on lower-end cards
  - *From: Kijai*

- **VACE block application**: Every 5th block for 14B, every 2nd for 1.3B
  - Default VACE block patterns
  - *From: Kijai*

- **CausVid LoRA strength**: 0.3-0.5
  - 0.3 allows proper hair movement, 0.5 gives cleaner results at 4 steps
  - *From: A.I.Warper*

- **Steps with CausVid LoRA**: 2-4 steps
  - CausVid is step-distilled, works well at very low step counts
  - *From: Kijai*

- **CFG with CausVid**: 1.0
  - CausVid is CFG-distilled, doubles compute speed
  - *From: Draken*

- **Shift parameter with CausVid**: 8
  - Don't reduce to 1 like other optimizations
  - *From: Kijai*

- **Resolution**: 576x1024
  - Working resolution for testing, 720p had issues with hair movement
  - *From: A.I.Warper*

- **CausVid LoRA strength**: 0.5-1.0
  - Optimal balance for quality without artifacts
  - *From: DawnII*

- **CausVid steps**: 4-6 steps
  - Good quality with reasonable generation time
  - *From: DawnII*

- **Block swap**: 20
  - Good balance for 16GB VRAM systems
  - *From: N0NSens*

- **VACE mask color**: 127,127,127 RGB (0.5 gray)
  - What VACE tries to fill for inpainting/outpainting
  - *From: Kijai*

- **Max frames at 1024x576**: 81 frames
  - VRAM limitation for single batch
  - *From: A.I.Warper*

- **CFG for CausVid**: 1
  - Standard setting for distilled models
  - *From: Valle*

- **CausVid LoRA strength**: 0.2-0.6, commonly 0.5
  - Optimal balance, 0.7 may be better for some cases
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Steps for CausVid**: 4-5 steps
  - Less motion shots can use 4 or less, more motion needs 5+
  - *From: N0NSens*

- **CFG for CausVid**: 1.0
  - Always use CFG 1 with CausVid LoRA
  - *From: Multiple users*

- **Shift parameter**: 8-10 for quality, avoid 30
  - Higher shift values damage background details
  - *From: N0NSens*

- **Block swap for 14B models**: 40 blocks for 14B + 5 for VACE
  - VRAM optimization
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Causvid Lora strength**: 0.25 with 6 steps
  - Incredible quality while maintaining good motion
  - *From: The Punisher*

- **Causvid Lora for i2v**: 0.5 strength for 4 steps, 0.6 for 6 steps
  - Tested multiple times for optimal results
  - *From: Jonathan*

- **Denoise for i2v with Causvid**: 0.75
  - Improves movement and prompt adherence significantly
  - *From: Jonathan*

- **Base precision and quant**: base_precision fp16, quant fp8_e5 for <4xxx cards or fp8_e4 for >4xxx cards
  - Optimal performance based on GPU generation
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Causvid LoRA strength**: 0.25 for normal I2V, 0.6-0.3 range generally
  - Good balance of speed and quality
  - *From: The Punisher*

- **Steps for Causvid**: 6 steps
  - 4 steps show issues, 6 steps resolve them while maintaining speed
  - *From: The Punisher*

- **CFG for Causvid LoRA**: 1.0
  - Required for distilled model, higher values double computation time
  - *From: zelgo_*

- **VACE strength**: 80%
  - 100% pushes too far into parrot mode
  - *From: A.I.Warper*

- **Denoise for second pass**: 80%
  - Used in two-pass workflow for cleanup
  - *From: A.I.Warper*

- **Block swap**: 45 (40 base model + 5 VACE)
  - Prevents crashes with 14B VACE models
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Shift parameter**: 2.5
  - Solid results, values over 15 cause blurry details
  - *From: Jemmo*

- **CFG**: 1
  - Required for CausVid LoRA to work properly
  - *From: Davidodave*

- **Steps**: 14
  - Removes shimmer from 8-step outputs with minimal time penalty
  - *From: CaptHook*

- **CausVid LoRA strength**: 0.40
  - Good balance for quality
  - *From: CaptHook*

- **Denoising**: 0.75
  - Can add motion and reduce artificial look
  - *From: JohnDopamine*

- **Eta**: 0.5
  - Good general value for noise addition in custom sampler
  - *From: Clownshark Batwing*

- **CausVid LoRA strength**: 0.3-0.6
  - Lower values need more steps, higher values work with fewer steps
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Steps with CausVid**: 4-12 steps
  - Depends on LoRA strength - lower strength needs more steps
  - *From: ˗ˏˋ⚡ˎˊ-*

- **CFG with CausVid**: 1.0
  - Required for proper CausVid LoRA function
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Denoise for V2V**: 0.6
  - Good balance for video-to-video transformation
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Block swap for 14B model**: 40 blocks
  - For memory efficiency with 16GB VRAM
  - *From: N0NSens*

- **CausVid steps**: 4-5 steps
  - Good balance of speed and quality
  - *From: Multiple users*

- **Block swap**: 35 transformer blocks
  - Reduces VRAM usage significantly while maintaining performance
  - *From: N0NSens*

- **Overlap frames for context**: 32 frames
  - Recommended overlap setting
  - *From: Flipping Sigmas*

- **Denoise for V2V**: Below 1.0
  - Required when using samples input for video-to-video
  - *From: ˗ˏˋ⚡ˎˊ-*

- **CausVid CFG**: 1.0
  - Required for CausVid LoRA to work properly
  - *From: ˗ˏˋ⚡ˎˊ-*

- **CausVid LoRA strength**: 0.3-0.6
  - Lower values need more steps, 0.5 commonly used
  - *From: ˗ˏˋ⚡ˎˊ-*

- **CausVid steps**: 4-8
  - Allows much lower step inference than standard
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Second VACE embed strength**: 0.2-0.5
  - When combining multiple controls, lower strength prevents overcooking
  - *From: VRGameDevGirl84(RTX 5090)*

- **Video-to-video denoise with CausVid**: 0.2
  - Works well with LoRAs for v2v workflow
  - *From: hicho*

- **Video upload width**: 960 (can reduce to 512)
  - Determined by Video Upload node, can reduce for VRAM constraints
  - *From: ˗ˏˋ⚡ˎˊ-*

- **CausVid LoRA strength**: 0.3-0.5
  - Base is 0.5 with 4 steps, 0.3 with 8 steps preferred, above 0.6 gives burned outputs
  - *From: ˗ˏˋ⚡ˎˊ-*

- **CausVid CFG**: 1
  - Always use CFG=1 with CausVid LoRA
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Steps for quality**: 6 for standard, 4 for previews, 8 for final
  - Balances speed and quality
  - *From: David Snow*

- **VACE encode strength and end_percent**: strength 0.9, end_percent 0.8
  - Good starting values for VACE reference
  - *From: Fawks*

- **Reserve VRAM**: 2-3
  - Prevents OOM by limiting VRAM usage to max minus reserved amount
  - *From: BestWind*

- **CausVid LoRA parameters**: 4-9 steps, CFG 1.0, LoRA strength 0.4-0.8, shift 8
  - Optimal settings for speed and quality with CausVid
  - *From: Johnjohn7855*

- **VACE block swapping for 12GB VRAM**: Block swap 40 and 5 of VACE
  - Enables running on lower VRAM systems
  - *From: sneako1234*

- **TeaCache threshold with VACE 14B CausVid**: 0.6 or higher
  - Lower values don't work properly with this setup
  - *From: David Snow*

- **Multi-VACE encoder strengths**: Pose: strength 1, Depth: strength 0.5
  - Maintains reference image structure while adding control
  - *From: VRGameDevGirl84(RTX 5090)*

- **CausVid LoRA strength**: 0.3 with 12 steps or 0.6 with 4 steps
  - Balance between speed and quality
  - *From: CFSStudios*

- **VACE normal map strength**: 0.9
  - Good facial tracking without artifacts
  - *From: VRGameDevGirl84(RTX 5090)*

- **CFG and shift for UniPC with CausVid**: CFG 1 and shift 8
  - Optimal settings for UniPC sampler
  - *From: Cubey*

- **VACE strength for pose control**: 0.6
  - Good balance for control without artifacts
  - *From: Kijai*

- **CFG scale**: 1.5 with SLG
  - Better results than CFG 1.0, worth the 2x inference time
  - *From: Kijai*

- **Steps for WAN**: 25-50 steps maximum
  - 75 steps is way too much, no benefit over 50 and even that is quite high for most use cases
  - *From: Juampab12*

- **NormalCrafter resolution**: 1024
  - Recommended resolution setting for NormalCrafter
  - *From: VRGameDevGirl84(RTX 5090)*

- **NormalCrafter encoder strength**: Start at 0.5
  - When face differs significantly from reference, start at 0.5 and increase until it gets wonky
  - *From: VRGameDevGirl84(RTX 5090)*

- **Inpaint RGB fill**: 127, 127, 127 (gray)
  - Required for VACE inpainting to work properly
  - *From: David Snow*

- **Control strength for separated embeds**: 0.7
  - Good balance for control influence when using separate control/reference
  - *From: Kijai*

- **Denoise for latent upscale second pass**: 0.65
  - Maintains consistency when upscaling
  - *From: DawnII*

- **base_precision**: fp16_fast
  - Recommended for RTX 4090 performance
  - *From: Cubey*

- **Context frames**: 81 (default)
  - Use default 81 frame windows for memory efficiency in long generations
  - *From: Kijai*

- **CausVid LoRA strength**: 0.3-0.6
  - Lower requires more steps, 0.4 with 8 steps or 0.5 with 4 steps work well
  - *From: ˗ˏˋ⚡ˎˊ-*

- **CFG for CausVid**: 1.0
  - Higher values not recommended unless using SLG which doubles gen time
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Steps with CausVid**: 4-8 steps
  - 4 steps with 0.5 strength or 8 steps with 0.4 strength
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Direct input strength**: 0.505
  - For using input video directly in input frames
  - *From: VRGameDevGirl84(RTX 5090)*

- **Normal map strength**: 0.500
  - When combining with direct input processing
  - *From: VRGameDevGirl84(RTX 5090)*

- **Block swap for high res**: 40 blocks
  - For 1280x720 resolution generations to avoid OOM
  - *From: Valle*

- **CausVid parameters**: 9 steps, 1.0 cfg, 0.7 weight, 1 shift, euler, beta scheduler
  - Sweet spot for CausVid - follows prompts as good as with cfg, looks good at 9 steps, blurry without shift
  - *From: Ada*

- **VACE strength over time**: List of floats with same length as steps
  - Allows controlling VACE strength at different timesteps for more refined control
  - *From: Kijai*

- **Second pass denoise**: Much lower denoise (around 0.75 or less)
  - High denoise like 0.75 keeps too much structure from input when doing second pass refinement
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Block swapping**: 30 for 4090 24GB
  - To avoid memory allocation issues when increasing resolution
  - *From: VRGameDevGirl84(RTX 5090)*

- **Input video strength sweet spot**: 0.4-0.5
  - 0.3 loses facial details, need to find balance
  - *From: VRGameDevGirl84(RTX 5090)*

- **Optimal settings for gun shot scene**: 0.7 weight, uni_pc, kl_optimal, 1.0 cfg, 15 steps, 1 shift
  - Found ideal settings for image to video without cfg issues
  - *From: Ada*

- **CFG Schedule for liquid art lora**: Use WanVideo CFG Schedule node
  - CausVid severely limits lora strength, CFG schedule helps restore it
  - *From: Zlikwid*

- **CFG**: 1
  - Required when using 4-step LoRA with standard WAN T2V
  - *From: JohnDopamine*

- **Reference image strength**: Above 1.0 (with Causvid)
  - Helps maintain character consistency when fighting against control inputs
  - *From: Johnjohn7855*

- **Depth video strength**: 0.53-0.65
  - Effects start above 0.53, becomes very strong above 0.6
  - *From: Johnjohn7855*

- **Steps/Shift combination**: 4 steps, shift 4
  - Lower shift improves hair consistency from reference, prevents loss of reference influence
  - *From: boorayjenkins*

- **UniAnimate resolution**: 512x768
  - Better pose detection success rate at this resolution
  - *From: Guey.KhalaMari*

- **Pose detection threshold**: 0
  - Can help detect poses when standard thresholds fail
  - *From: Guey.KhalaMari*

- **Sampler**: DMP++
  - Gives different variations but minimal effect on reference/depth control balance
  - *From: boorayjenkins*

- **Points to sample in spline**: Number of steps
  - For CFG and VACE strength scheduling, must match step count
  - *From: Kijai*

- **MoviiGen VACE steps**: 6 steps with 0.3 strength
  - Provides decent results without artifacts
  - *From: The Punisher*

- **Input video strength for mouth preservation**: 0.6 minimum
  - Maintains mouth movement integrity from original video
  - *From: VRGameDevGirl84(RTX 5090)*

- **Face mesh strength for hair movement**: 0.4
  - Helps with hair movement but reduces mouth expressiveness
  - *From: VRGameDevGirl84(RTX 5090)*

- **Mask color for VACE**: Gray RGB 127 or #808080
  - Standard masking color for VACE processing
  - *From: DawnII*

- **CausVid strength**: 0.3 with 8-12 steps
  - Good balance between speed and quality for video generation
  - *From: seitanism*

- **CausVid high speed setting**: strength 0.5 with 5 steps
  - Very fast generation but may show visible patterns
  - *From: patientx*

- **VACE overlap frames**: 6-10 frames
  - Provides good motion consistency between clips
  - *From: ArtOfficial*

- **Frame limit before VRAM issues**: 160 frames at 720p
  - Typical limit before running out of VRAM
  - *From: Gateway {Dreaming Computers}*

- **CausVid LoRA strength with Phantom**: around 1.0
  - Phantom requires higher strength for CausVid to work effectively
  - *From: zelgo_*

- **Wan LoRA training images**: 50 images at 1024x1024 for 14B
  - Standard good amount for training on 14B model
  - *From: VRGameDevGirl84(RTX 5090)*

- **TeaCache with low step counts**: Don't use TeaCache with 10 steps
  - Too low step count means too much changes, TeaCache can't effectively skip frames
  - *From: Cubey*

- **CausVid LoRA strength**: 0.5
  - Optimal balance for quality and adherence
  - *From: David Snow*

- **CFG Scale**: 1.0
  - Important for speed, higher values significantly slow generation
  - *From: David Snow*

- **Steps**: 6
  - Works well with CausVid LoRA
  - *From: David Snow*

- **VACE steps**: 12
  - For high quality 960x720 output
  - *From: Neex*

- **CausVid LoRA for VACE**: 0.3
  - Good balance for face animation control
  - *From: Neex*

- **Context overlap**: 32
  - For longer video generation with good blending
  - *From: VK (5080 128gb)*

- **Resize divisible by**: 16
  - Only hard requirement for Wan
  - *From: Kijai*

- **CausVid LoRA steps**: 6 steps
  - Allows nice animations in 6 steps instead of 20-30
  - *From: David Snow*

- **Vid2vid with CausVid denoise**: 0.50
  - Follows prompt well and takes camera motion
  - *From: hicho*

- **Blocks to swap**: 40
  - For higher resolution processing with sufficient VRAM
  - *From: Ruairi Robinson*

- **VACE blocks to swap**: 15 (max)
  - Maximum setting available for VACE blocks
  - *From: Ruairi Robinson*

- **WSL2 memory allocation**: 64GB memory, 16GB swap
  - For 128GB system RAM in WSL2 configuration
  - *From: jerms_ai_(4090_24g)*

- **Base precision**: fp16 instead of bf16
  - Better memory efficiency, no point to upcast
  - *From: Kijai*

- **Use_non_blocking**: disabled
  - Reserves less RAM, helps with memory issues
  - *From: Kijai*

- **CausVid LoRA strength**: 0.3-0.4
  - Above 0.4 reduces VACE control strength and prevents mouth movement
  - *From: Kijai*

- **VACE strength**: 1.2
  - Can balance out high CausVid LoRA strength
  - *From: Kijai*

- **Steps for CausVid**: 8
  - Used with 0.3-0.4 LoRA strength and shift of 1
  - *From: A.I.Warper*

- **Resolution for human portraits**: 512x512
  - Works best for human portrait and closeups
  - *From: hicho*

- **CausVid LoRA strength**: 0.5 default, 0.3-0.6 range
  - Higher values make generations look artificial
  - *From: David Snow*

- **CFG with CausVid**: 1.0
  - Other values dramatically increase generation times
  - *From: David Snow*

- **AccVideo scheduler steps**: 50 (uses 10 actual)
  - Required setting for AccVideo scheduler to work
  - *From: David Snow*

- **VACE maximum frames**: 161 frames
  - Can go this high without degradation on 5090 with 32GB
  - *From: Piblarg*

- **Character LoRA training dataset**: 10-15 images
  - 2 front, 2 each side, 2 back, 2 3/4 turn, plus angles
  - *From: Thom293*

- **AccVid LoRA strength**: 1.0 for regular use, 1.7 for 6 steps
  - Optimal performance balance
  - *From: 🦙rishappi, Kijai*

- **AccVid steps and CFG**: 10 steps, CFG 1.0
  - Standard AccVid configuration
  - *From: Kijai*

- **AccVid T2V steps**: 4 steps at 1.0 strength, 5-10 steps generally
  - Fast generation with good quality
  - *From: Kijai, slmonker(5090D 32GB)*

- **CausVid configuration**: CFG 1, 5 steps
  - Standard CausVid setup
  - *From: Boop*

- **VRAM optimization**: Keep VRAM usage at 96-98%, not 99%
  - 99% usage makes generation very slow
  - *From: N0NSens*

- **Context options default**: 81 frame contexts with 16 frame overlap
  - Default settings work fine for longer videos
  - *From: David Snow*

- **AccVid LoRA strength**: 1.5
  - Used in combination with CausVid LoRA
  - *From: David Snow*

- **CausVid LoRA strength**: 3.5 range
  - Too strong negates VACE controls
  - *From: Guey.KhalaMari*

- **Wan sampler**: Euler
  - Better overall than UniPC
  - *From: David Snow*

- **Resolution for Phantom 14B**: 720p
  - Original training resolution, 768 works but 720 is preferred
  - *From: Kijai*

- **CausVid LoRA strength**: 0.5
  - Prevents artifacts and flicker issues
  - *From: Kijai*

- **CausVid LoRA strength for RTX 4090**: 1.1
  - Works fine with 5-6 steps instead of 4
  - *From: ZeusZeus (RTX 4090)*

- **TeaCache threshold**: 0.2
  - Optimal performance balance
  - *From: Kijai*

- **VACE default shift**: 16
  - Default recommended value, lower values can cause artifacts
  - *From: Kijai*

- **Phantom + VACE + CausVid CFG**: Phantom CFG: 5, Sampler CFG: 1
  - Decent results for combined workflow
  - *From: DawnII*

- **CausVid I2V configuration**: 0.5 strength, 12 steps, 2.5-3 CFG for first steps
  - Works pretty good with I2V at 720p
  - *From: ボグダンおじさん*

- **Merged model configuration**: CFG: 1, Steps: 6-7
  - For merged CausVid + AccVid model, no LoRA needed
  - *From: JohnDopamine*

- **Phantom CFG**: 1
  - Full model requires CFG=1
  - *From: JohnDopamine*

- **Phantom steps**: 40 minimum
  - Below 40 steps is very artifacty, 40 still has some artifacts
  - *From: aikitoria*

- **Merged model steps**: 6-7 steps
  - JohnDopamine's CausVid/AccVid/Phantom merge works with fewer steps
  - *From: JohnDopamine*

- **freenoise**: false
  - Better for videos longer than 81 frames and consistent results
  - *From: chrisd0073*

- **Resolution**: 1024x576
  - WAY better output vs 864x480 and much better vs 960x544
  - *From: CaptHook*

- **Steps**: 8
  - 6 steps showed occasional morphing, 10 steps too long with too much contrast
  - *From: CaptHook*

- **Shift**: 5
  - 1-3 too low causes morphing, 8-10 too high causes occasional morphing and too much contrast
  - *From: CaptHook*

- **AccVid LoRA strength**: 1.0-1.5
  - Little difference beyond 1.0, but 1.5 works well with CausVid 0.5
  - *From: Johnjohn7855*

- **CausVid LoRA strength**: 0.4-0.5
  - Higher than 0.5 makes flashes inevitable
  - *From: Johnjohn7855*

- **CFG with AccVid+CausVid**: 3.5
  - Better prompt following than CFG 1, CFG 6 burns it, CFG 2 kills prompt following
  - *From: Ada*

- **Frames for Phantom**: 49 or 81
  - Standard frame counts that work well
  - *From: Johnjohn7855*

- **FPS**: 16
  - Works well with 1024x576 resolution for 8.5min generation time
  - *From: CaptHook*

- **MoviiGen LoRA strength**: 0.4-0.7
  - Higher values lose ID consistency to reference image
  - *From: Johnjohn7855*

- **AccVideo + CausVid**: accvideo: 1.5, causvid: 0.5
  - Recommended combination for speed improvement
  - *From: David Snow*

- **Context overlap frames**: 32
  - Much better results than default overlap
  - *From: Nekodificador*

- **CFGDistill LoRA strength**: 0.1
  - Way too strong at higher values, affects reference image details
  - *From: Johnjohn7855*

- **CausVid strength when flashing occurs**: 0.4
  - Helps reduce flashing issues
  - *From: Johnjohn7855*

- **Block 0 disable**: off
  - Helps with flashes when using LoRA block edit
  - *From: David Snow*

- **CausVid LoRA strength**: 0.5
  - Standard strength for speed improvement
  - *From: David Snow*

- **AccVid LoRA strength**: 1.5
  - Recommended strength, though preferences vary
  - *From: David Snow*

- **CFG with speed LoRAs**: 1.0
  - When using CausVid and AccVid LoRAs
  - *From: David Snow*

- **Denoise for input video bleed**: 0.85
  - Allows some input video to help model understand face location
  - *From: David Snow*

- **Input video strength**: 0.3-0.4
  - Helps with mouth movement and character positioning
  - *From: VRGameDevGirl84(RTX 5090)*

- **detail_wanz**: 0.4 and 1.0 tested
  - Testing different detail levels
  - *From: hau*

- **Skip Layer Guidance blocks**: 9,10 with 0.0 to 0.9
  - SLG configuration for improved results
  - *From: hau*

- **CFG for Phantom without causvid**: 7.5
  - Default setting that works well
  - *From: aikitoria*

- **Shift for Phantom**: 5
  - Reduced from 10 for better performance
  - *From: David Snow*

- **Phantom reference strength**: ~0.2
  - Helps recover likeness when using reduced lora strength
  - *From: DeZoomer*

- **Denoising for motion preservation**: 0.10-0.15
  - Low denoising helps preserve motion in video-to-video
  - *From: hicho*

- **Block swap optimization**: Adjust until 95% VRAM used
  - Optimal memory usage without slowdown
  - *From: Kijai*

- **CausVid with merged model**: 7 steps, 1.0 CFG
  - Fast generation with distillation built in
  - *From: Thom293*

- **Phantom 14B without CausVid**: 30+ steps recommended
  - 16 steps not enough without distillation
  - *From: Kijai*

- **VACE + Phantom inpainting**: 0.8 VACE strength, cut at 0.2
  - Allows Phantom superior reference fidelity to come through
  - *From: Zuko*

- **PerpNegGuider neg_scale**: 0.25-0.5 recommended
  - Controls divergence from input image while retaining subject context
  - *From: Ablejones*

- **CausVid LoRA block application**: First block 0.5 max, rest 1.0
  - Most important part is reducing first block application
  - *From: Kijai*

- **CFG with CausVid distilled**: 1.0
  - Distillation includes CFG distillation
  - *From: Kijai*

- **Phantom CFG**: 5.0
  - Original paper setting
  - *From: Guey.KhalaMari*

- **CausVid v2 CFG scheduling**: 5.0 start, end percent 0.5
  - Prevents flash while maintaining speed
  - *From: Ada*

- **Wan21-I2V-14B-480P with CausVid**: LORA: 1.0, steps: 4, cfg: 1, shift 0.30, scheduler: euler/beta
  - Good parameters found through testing
  - *From: Mngbg*

- **CausVid strength with AccVid**: CausVid 0.5 + AccVid 0.5
  - Good balance found
  - *From: ▲*

- **CFG with distilled for early steps**: 3-4 CFG for 2-4 steps with 6-8 total steps
  - Most impactful at early steps
  - *From: Kijai*

- **CausVid v2 strength**: 1.0
  - Can handle full strength without motion destruction
  - *From: Kijai*

- **CFG scheduling for CausVid v2**: Start 5, end 1, stop at 0.3, 6 steps
  - Avoid over-saturation while maintaining quality
  - *From: Johnjohn7855*

- **Steps for fast generation**: 8 steps
  - Good balance of speed and quality
  - *From: VRGameDevGirl84(RTX 5090)*

- **ATI generation**: CFG 1
  - Works well with trajectory control
  - *From: Kijai*

- **MoviiGen LoRA**: 0.3 + 0.6 detailz lora
  - Improves quality without over-processing
  - *From: mamad8*

- **Steps**: 8 steps
  - Works well with Phantom and CausVid V2
  - *From: VRGameDevGirl84(RTX 5090)*

- **LoRA merge strength**: 1.0
  - Full strength merging works effectively for multiple LoRAs
  - *From: VRGameDevGirl84(RTX 5090)*

- **Block swapping**: 5 blocks
  - Enables 1280x720 generation without OOM
  - *From: VRGameDevGirl84(RTX 5090)*

- **CFG with CausVid**: 1
  - CausVid is tuned for CFG 1
  - *From: MilesCorban*

- **Shift**: 8
  - Standard setting that works well
  - *From: MilesCorban*

- **Film grain parameters**: 0.03 for all three parameters
  - Higher values create too much effect
  - *From: Johnjohn7855*

- **CausVid v2 CFG**: >1 with scheduling
  - Tuned on T2V, needs different approach than v1
  - *From: Johnjohn7855*

- **ATI points**: 121 points for 81 frames
  - Prevents cutting off the end
  - *From: Kijai*

- **RIFE multiplier minimum**: 2
  - Setting to 1 doesn't add frames
  - *From: Johnjohn7855*

- **Normal Craft strength**: 0.8 on encoder
  - Follows expressions well
  - *From: HeadOfOliver*


## Concepts Explained

- **TeaCache**: Optimization that skips certain conditional and unconditional steps during generation
  - *From: VRGameDevGirl84(RTX 5090)*

- **Context windows**: Window size for processing longer videos, should be something model can do (81 default)
  - *From: Kijai*

- **Latent frame ratio**: Each latent contains 4 frames in WanVideo
  - *From: Draken*

- **SLG**: Setting that requires lower CFG values (half of normal) for proper results
  - *From: Miku*

- **DG Wan models**: Distilled versions of 1.3B with extra tweaks, requires less steps than base models. Multiple versions available with Ares V3 being current favorite
  - *From: David Snow*

- **LoRA timestep distribution**: Different training approaches - sigmoid (central steps for character), linear, shift (start/end for style). Affects which timesteps the LoRA focuses on
  - *From: mamad8*

- **4+1 latent rule**: For frame to latent conversion: latentCount = (frameCount - 1) / 4, always need the +1, so 33 frames = 8 latents
  - *From: Kijai*

- **Context frames**: Number of frames per batch when doing longer animations - think of it as doing longer animations in batches, blends based on frame overlap setting
  - *From: David Snow*

- **VACE control map specificity**: VACE requires very specific control maps that match training data - if control map isn't nearly exactly how it appeared during training, doesn't work well
  - *From: Rishi Pandey*

- **VACE module**: Separate module that works with any 1.3B model, not a full model itself
  - *From: Kijai*

- **DF (Diffusion Forcing)**: Method for extending videos beyond 5 seconds by chaining generations
  - *From: MilesCorban*

- **Style transfer without structure**: New method that transfers visual style while preserving original structure/movement
  - *From: Clownshark Batwing*

- **Frame looping in Wan**: Wan models loop back at certain frame counts - 81 for vanilla, 97/121 for Skyreels variants
  - *From: N0NSens*

- **TeaCache non_blocking**: Parameter that controls memory allocation method - non_blocking reserves more RAM
  - *From: Kijai*

- **FLF2V**: First-Frame-Last-Frame morphing technique, described as best start-end method
  - *From: slmonker(5090D 32GB)*

- **CausVid**: Distilled version of Wan 14B with step and CFG distillation for faster inference
  - *From: yi*

- **Flex Attention**: Memory optimization technique that requires torch.compile and specific frame per block settings
  - *From: Kijai*

- **ACE++ Fill**: Inpainting technique better than standard Fill for consistent character workflows
  - *From: Draken*

- **Flex attention**: Relatively new fully customizable attention in pytorch, uses BlockMask for adjacent frame attention
  - *From: Kijai*

- **kv_cache in CausVid**: How sliding windows work, enables endless generation and real-time preview
  - *From: Kijai*

- **Block mask**: Used with flex attention to limit attention to adjacent frames in sequence dimension
  - *From: Kijai*

- **R2V**: Reference to video - input person without forcing first frame
  - *From: Juampab12*

- **VACE reference vs start image**: Two separate concepts - reference image for style/subject, start image for temporal beginning
  - *From: Kijai*

- **VACE latent placement**: VACE places images in latents rather than using cross-attention embeds like traditional I2V
  - *From: Kijai*

- **VACE temporal inpainting**: Can inpaint spatially and temporally, meaning I2V would be inpainting every other frame besides first
  - *From: Kijai*

- **VACE as ControlNet**: Should think of VACE as a controlnet for T2V model rather than standalone
  - *From: Kijai*

- **Block swapping**: Technique to reduce VRAM usage by swapping model blocks to system memory
  - *From: Kijai*

- **Context batches**: Each context acts as a batch (81 frames default) that blends with others based on overlap
  - *From: David Snow*

- **CausVid LoRA**: Extracted version of CausVid model that can be used as LoRA with base T2V 14B model for faster inference
  - *From: Kijai*

- **VACE reference vs first frame**: Reference image is NOT first frame - if you have first frame to animate, put it in control images with input mask
  - *From: Kijai*

- **FLF2V**: First Last Frame To Video - start/end frame model with weird naming, 720p only
  - *From: Kijai*

- **Block masking training**: CausVid trained with 3 latent windows, causing quality loss when used differently
  - *From: Kijai*

- **VACE block skipping**: Technique to avoid applying certain LoRAs to blocks used by VACE control
  - *From: Kijai*

- **Clip vision embeds**: Used in I2V models for image conditioning, affects all frames throughout generation
  - *From: Kijai*

- **Context windows**: Method for generating long videos by processing overlapping segments
  - *From: Kijai*

- **CausVid**: Distilled model for both CFG and steps, allows cfg 1.0 and low steps (2-4) for much faster generation
  - *From: Draken*

- **VACE blocks**: Can be disabled for LoRA to allow more motion transfer while reducing adverse effects
  - *From: Kijai*

- **Model dtype for DWPose**: DWPose embeds should match model dtype instead of fp32 to prevent crashes with long clips
  - *From: Kijai*

- **VACE**: Video control system that is essentially inpainting a panel, works with style transfer, inpainting, subject-driven, outpainting
  - *From: deleted_user_2ca1923442ba*

- **CausVid**: Converts bidirectional attention models into causal attention models, then distills them using DMD2 method
  - *From: deleted_user_2ca1923442ba*

- **Causal vs Bidirectional attention**: Causal attention only attends to past frames (like ChatGPT), bidirectional attends to both past and future frames
  - *From: deleted_user_2ca1923442ba*

- **Diffusion Forcing**: Hybrid between diffusion and autoregressive methods
  - *From: deleted_user_2ca1923442ba*

- **Shift parameter**: Has to do with frame interpolation - more dynamic or more subtle, need to find balance with CFG
  - *From: chrisd0073*

- **Distorch**: Like block swap, offloads nearly entire model with only 10% speed loss, gives more space for latent/video so higher res or frames possible
  - *From: The Punisher*

- **K quants vs 0 quants**: K quants are generally better/more efficient than Q4_0, should always use K quants when available
  - *From: The Punisher*

- **CFG distillation**: Models trained to work at CFG 1.0, doubling speed by eliminating negative prompt computation
  - *From: Draken*

- **Subject bleed**: When using multiple subjects in VACE reference, characteristics may blend between subjects
  - *From: DawnII*

- **Fun LoRAs vs regular models**: LoRAs trained on Fun models may cause key errors on regular models but still function
  - *From: David Snow*

- **Shift parameter**: Controls detail quality in CausVid, values too high cause blur
  - *From: Jemmo*

- **Reward LoRAs**: LoRAs trained to improve motion and quality, HPS and MPS variants available
  - *From: yi*

- **Eta in custom sampler**: Amount of noise added after each step, 0.0 is ODE like dpmpp_2m, >0.0 is SDE like dpmpp_2s_a
  - *From: Clownshark Batwing*

- **MoviiGen**: Fine-tuned WAN T2V model for enhancing film and television styles, like WAN with integrated LoRA
  - *From: slmonker(5090D 32GB)*

- **Inverted lineart**: Alternative to control pose that works with VACE when regular lineart alone doesn't work
  - *From: Nokai*

- **Block swap memory**: Memory management technique - shows transformer blocks on CPU vs GPU, enables running larger models with limited VRAM
  - *From: N0NSens*

- **Context switching in video generation**: When generating long videos, the model processes in chunks (e.g. 81 frames), causing potential jumps between segments
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Samples input**: Input method for encoded video frames in V2V workflows, requires denoise below 1.0
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Block swap**: Memory management technique that keeps some transformer blocks on CPU to reduce VRAM usage
  - *From: N0NSens*

- **Safe checkpoint loading**: Security feature that validates model checkpoints, some models like Sapiens require disabling this
  - *From: MilesCorban*

- **MoviiGen**: A cinematic finetune of WAN
  - *From: yo9o*

- **VACE module vs full model**: Module only works with KJ wrapper, full model compatible with both native and wrapper
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Inverted vs non-inverted face landmarks**: White on black rather than black on white landmark detection
  - *From: ˗ˏˋ⚡ˎˊ-*

- **end_percentage in VACE**: Parameter that stops the control at a certain point during the whole generation process
  - *From: Draken*

- **Context in video generation**: Feature allowing longer video generation by chunking, may lose some information between chunks
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Block swapping**: Technique to manage VRAM by swapping model blocks to system RAM, slower but allows larger models
  - *From: BestWind*

- **Every 5th block disabling**: VACE applies to every 5th block on 14B, so disabling reduces interference with VACE inputs
  - *From: DawnII*

- **SLG and Zero Star optimizations**: These optimizations do nothing with CFG 1.0 as their code is never executed
  - *From: Kijai*

- **VACE embed chaining**: Chain multiple VACE encoders together like ControlNets for cumulative effects
  - *From: David Snow*

- **CausVid LoRA distillation**: They are using brute force distillation rather than the causal aspect, not using proper causal sampling method
  - *From: Kijai*

- **VACE frame batching**: Latents are processed in batches of 4, plus one for init frame, which is why it adds extra frames
  - *From: Cubey*

- **Double VACE encode**: Using two separate VACE encode nodes with different control types (like depth and pose) and compositing the results for better output quality
  - *From: slmonker(5090D 32GB)*

- **WAN FPS behavior**: WAN models are trained at 16fps (24fps for Skyreels). Changing FPS in video output just changes playback speed, not generation framerate. 16 frames always equals 1 second of model time
  - *From: Juampab12*

- **TeaCache memory issue**: When doing .clone() then .to(device), it reserves VRAM unnecessarily. Moving to CPU first then cloning frees the memory properly
  - *From: Kijai*

- **Context windows**: Method to generate videos longer than base limit by running multiple 81-frame generations and blending seams, uses same memory as single 81-frame gen
  - *From: Kijai*

- **VACE input mask**: Black and white mask where black areas are kept as-is, white areas are regenerated
  - *From: Kijai*

- **CausVid LoRA**: Speed optimization LoRA that makes inference time bearable for larger models
  - *From: Kijai*

- **VACE recolorizing mode**: When giving VACE plain input footage at 1.0 strength with no control frame, it will 'recolorize' the video - one of the tasks VACE was trained on
  - *From: Piblarg*

- **Video extension with last frames**: Take the last N frames (like 20) of a video you want to extend and put them in start images to create seamless extension
  - *From: Piblarg*

- **Context adapter blocks**: Alternative to full model fine-tuning, uses Res-Tuning scheme to inject tokens into transformer blocks for plug-and-play editing
  - *From: AJO*

- **VACE mask behavior**: Black areas use input directly, white areas use controlnet mode. Different from traditional controlnet masking
  - *From: Draken*

- **First frame restyle**: Technique of using controlnets to create better aligned starting frames, then removing them for longer runs
  - *From: Draken*

- **Relative head motion**: Custom technique that normalizes reference head and transforms it to target head, with relative movement calculated as diff from first frame to current frame
  - *From: Mads Hagbarth Damsbo*

- **Context window frame math**: Formula is (4*n)+1 for proper frame count with context window
  - *From: A.I.Warper*

- **VACE reference image processing**: Multiple references are better combined into single image or batched horizontally rather than chained
  - *From: DawnII*

- **Block swapping**: Helps with memory management but can be adjusted - start high and lower until first step generates
  - *From: MilesCorban*

- **VACE embed vs encode nodes**: Use VACE embed node instead of encode node for proper functionality, especially with control inputs
  - *From: Kijai*

- **Regional LoRAs**: Using masks to drive LoRAs for selective application to different parts of the image/video
  - *From: sneako1234*

- **Control input battle**: When multiple control inputs (reference image, depth, pose) compete for influence, requiring careful strength balancing
  - *From: Johnjohn7855*

- **Pose retargeting**: Process of mapping pose from one character to another, often causes issues like extended arms due to proportion differences
  - *From: Kijai*

- **VACE start/end frame morphing**: Method using start and end frame images with control data to create smooth transitions between different characters or states
  - *From: David Snow*

- **Context windows vs batching**: Two different approaches to handling long sequences - context windows process full length but lose consistency, batching maintains consistency but requires stitching
  - *From: A.I.Warper*

- **Face blending with pose control**: Combining DWPose body detection with MediaPipe face detection at blended strengths for better facial animation
  - *From: Gateway {Dreaming Computers}*

- **Block swapping**: Technique for managing VRAM by offloading model parts to system RAM, handled automatically in native ComfyUI
  - *From: zelgo_*

- **Context sliding**: Method for generating longer videos by using overlapping context from previous frames
  - *From: Draken*

- **Digi-doubles**: VFX term for digital replicas of humans or products without training custom LoRAs
  - *From: humangirltotally*

- **VACE reference image handling**: VACE can only use single reference image which gets inserted as first latent, multiple images get concatenated automatically
  - *From: Kijai*

- **Causal model KV caching**: Causal models get access to additional speedup called KV caching for faster inference
  - *From: deleted_user_2ca1923442ba*

- **VACE mask values**: For input mask: white is active, black is inactive. For input frames: gray is empty value to inpaint
  - *From: Kijai*

- **CausVid dual functionality**: CausVid does both distillation and conversion to causal, but Wan CausVid in ComfyUI only has distillation so far
  - *From: deleted_user_2ca1923442ba*

- **Block swap**: Slows things down, goal is to use as few blocks as possible, not for speed improvement
  - *From: David Snow*

- **Differential diffusion**: Method for compositing masked changes back into original video
  - *From: David Snow*

- **Set latent noise mask**: Node required for inpainting when using native ComfyUI workflows
  - *From: David Snow*

- **Context overlap**: Blend between batches when generating longer animations in segments
  - *From: David Snow*

- **CausVid LoRA distillation**: Distills step and cfg, culling anything that isn't 'solid' in network knowledge and making network converge in fewer steps
  - *From: Draken*

- **Flow edit**: Vid2vid with LoRA and flow edit for changing only specific parts like faces
  - *From: chrisd0073*

- **Block swap**: Memory management technique to swap model blocks between VRAM and RAM
  - *From: Kijai*

- **VACE mask colors**: White = active area, black = inactive area (kept as is). For inpainting, black area is preserved
  - *From: Kijai*

- **Control video frame colors**: Empty frames should be gray (0.5 or 127,127,127), keyframes should be black, new frames white on mask
  - *From: Kijai*

- **Block swap**: Puts most of model into regular RAM and swaps when needed during sampling. Don't need until hitting allocation errors
  - *From: Kijai*

- **AccVideo**: Distillation technique similar to CausVid that allows faster inference
  - *From: Draken*

- **VACE separate layers**: VACE applies itself over WAN as separate layers, so T2V LoRA training should work fine
  - *From: Piblarg*

- **Frame overlap blending**: Cross-fading overlapping frames to reduce color shifts and seams in extended videos
  - *From: Piblarg*

- **Stride in context**: How many frames the model skips when picking frames. Stride = 1 uses every frame (smooth, detailed, slower), Stride = 4 uses every 4th frame (faster, less smooth)
  - *From: chrisd0073*

- **RAM Tag color scheme**: Color scheme from recognize anything annotator that VACE is trained with, used for layout control inputs
  - *From: Kijai*

- **Block swapping**: Higher blocks = more RAM used, less VRAM used. Blocks swap data from VRAM to RAM. More swaps = longer generation but helps with VRAM limitations
  - *From: N0NSens*

- **Pasteback**: Image composite technique using mask to avoid VAE compression in inpainting
  - *From: A.I.Warper*

- **Vace_end_percent**: Parameter that controls inpainting blending, lower values like 0.80 blend better than 1.0
  - *From: VK (5080 128gb)*

- **Sliding context windows**: Method to generate longer videos without increasing memory use by keeping constant sampled frames
  - *From: Kijai*

- **Riflex**: Breaks looping of positional embeds for frames beyond 81, doesn't affect memory use
  - *From: Kijai*

- **TeaCache**: Caching system that skips certain steps during sampling to improve performance
  - *From: Kijai*

- **TAEW**: Tiny Auto Encoder WAN - provides much higher quality preview but slightly slower
  - *From: Kijai*

- **Reference latents in preview**: References are embedded in the latents, causing flashing between reference images and generated content in preview
  - *From: Kijai*

- **freenoise**: Controls noise addition - true uses random noise for natural motion, false reuses same noise for consistency and looping
  - *From: chrisd0073*

- **Phantom reference latents**: T2V model that takes reference latents as input rather than pure text-to-video
  - *From: Kijai*

- **Wan flash**: Predictable flash/contrast shift that appears at beginning of Wan videos, especially with CausVid LoRA
  - *From: David Snow*

- **LoRA block selection**: Technique to apply LoRA to specific blocks only, can eliminate flash by avoiding first blocks
  - *From: Kijai*

- **Uni3C controlnet**: Camera control system that can transfer motion from existing videos even without camera embeds
  - *From: Kijai*

- **Context windows**: Method for extending video duration, potentially works with Phantom
  - *From: Kijai*

- **Empty_frame_level**: Parameter in context processing, specific function unclear from discussion
  - *From: Yae*

- **Uni3C**: Controlnet that transfers camera movements from reference videos to generated content
  - *From: N0NSens*

- **Phantom latents**: Character embedding system that provides high consistency with reference images
  - *From: David Snow*

- **VACE mask format**: VACE expects mask videos in grayscale format for proper inpainting
  - *From: David Snow*

- **Uni3C architecture limitation**: Uni3C constructs latent from I2V input (36 channels), making it incompatible with T2V models currently
  - *From: Kijai*

- **VACE reference latent addition**: VACE adds extra latent when using reference image, which can cause frame count mismatches
  - *From: Kijai*

- **Skip Layer Guidance (SLG)**: Feature supported by WanVideoWrapper with configurable arguments
  - *From: hau*

- **Temporal mask in WanVideo ImageToVideo Encode**: Not implemented yet, would allow masking active/inactive frames for temporal inpainting, only works with fun inp models
  - *From: Kijai*

- **Block swapping**: Technique that offloads some GPU data to system RAM, slowing down the process but allowing larger models to run
  - *From: Thom293*

- **Crop&stitch**: Method to normalize face sizes by cropping and scaling faces then pasting back, similar to old deep face lab scripts
  - *From: DeZoomer*

- **Perpendicular guidance**: Uses normal negative and empty negative to get negative component more unrelated to positive embedding
  - *From: Ablejones*

- **negative_img_text**: Negative without the image component, acts like empty negative for PerpNegGuider
  - *From: Ablejones*

- **Diffdiff latent masking**: Needs blurred mask for encoding latents, different from VACE input frames which need hard edges
  - *From: Zuko*

- **CFG distillation**: Process included in CausVid and AccVid that allows using CFG 1.0 (effectively disabled)
  - *From: Kijai*

- **First block effect**: First block of CausVid LoRA causes flash artifacts, removing it retains motion without flash
  - *From: Kijai*

- **Phantom CFG**: Additional CFG parameter specific to Phantom model that causes 3x slower generation
  - *From: Kijai*

- **Block swap**: Technique with 40 blocks (0-39) for training longer videos
  - *From: Kijai*

- **Block 0 removal**: Removing first block from CausVid LoRA to improve results, now built into v2
  - *From: Kijai*

- **ATI trajectory control**: System using anchor points (stationary and moving) to direct motion in video generation
  - *From: Kijai*

- **Differential diffusion**: Method to apply denoising only to masked areas of video frames
  - *From: David Snow*

- **CFG scheduling**: Using different CFG values at different steps, higher at start then lower
  - *From: Johnjohn7855*

- **Film vs video color response**: Video content has blown out oversaturated highlights while film/cinema has non-linear highlight rolloff that preserves dynamic range for post-processing
  - *From: Ruairi Robinson*

- **Log images**: Professional cameras output log images with very low contrast and smooth highlight curves to preserve full dynamic range, similar to RAW images
  - *From: Ruairi Robinson*

- **CFG scheduling**: Setting CFG to apply only for specific steps out of total, like 1 step out of 8
  - *From: Johnjohn7855*

- **Block swap**: Primary cause of slowdown on consumer GPUs, more VRAM eliminates need for it
  - *From: Kijai*

- **ATI**: Motion control system for Wan using spline-based trajectory editing
  - *From: Kijai*

- **Trajectory points**: Control points used to guide model movement - model fills gaps naturally when you suggest how it should move, similar to TORA system
  - *From: Kijai*


## Resources & Links

- **CausVid Wan 2.1 14B model** (model)
  - https://huggingface.co/lightx2v/Wan2.1-T2V-14B-CausVid
  - *From: David Snow*

- **DG Custom Node for Wan** (workflow)
  - https://huggingface.co/Evados/DiffSynth-Studio-Lora-Wan2.1-ComfyUI
  - *From: Dream Making*

- **IPAdapter WAN (experimental)** (repo)
  - https://github.com/SirLatore/ComfyUI-IPAdapterWAN
  - *From: Gavmakes*

- **Camera control blender addon** (tool)
  - Referenced but no direct link provided
  - *From: VRGameDevGirl84(RTX 5090)*

- **CCP6 dsnow LoRA** (model)
  - https://huggingface.co/CCP6/dsnow/tree/main
  - *From: JohnDopamine*

- **CyberPop LoRA** (lora)
  - https://huggingface.co/CCP6/dsnow/tree/main
  - *From: David Snow*

- **DG Wan models collection** (models)
  - https://huggingface.co/Evados/DiffSynth-Studio-Lora-Wan2_1_v1_3b_t2v_Boost_Final
  - *From: David Snow*

- **Judy Hopps 14B LoRA** (lora)
  - https://civitai.com/models/1133220?modelVersionId=1743913
  - *From: MisterMango*

- **Claymation LoRA** (lora)
  - https://civitai.com/models/1439375/claydoh
  - *From: Jas*

- **New Framepack model** (model)
  - https://huggingface.co/lllyasviel/FramePack_F1_I2V_HY_20250503/tree/main
  - *From: slmonker(5090D 32GB)*

- **Ex video LoRA for increased animation length** (model)
  - https://huggingface.co/Evados/DiffSynth-Studio-Lora-Wan2.1-ComfyUI/tree/main
  - *From: David Snow*

- **ComfyUI Hot Reload Hack** (tool)
  - https://github.com/logtd/ComfyUI-HotReloadHack
  - *From: Kijai*

- **FramePack Studio standalone** (tool)
  - https://github.com/colinurbs/FramePack-Studio/
  - *From: ˗ˏˋ⚡ˎˊ-*

- **TTP ComfyUI FramePack** (node)
  - https://github.com/TTPlanetPig/TTP_Comfyui_FramePack_SE
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Kijai FramePack Wrapper** (node)
  - https://github.com/kijai/ComfyUI-FramePackWrapper
  - *From: ˗ˏˋ⚡ˎˊ-*

- **GeometryCrafter - upgraded DepthCrafter** (model)
  - https://github.com/TencentARC/GeometryCrafter
  - *From: Soutlkf*

- **ParaAttention optimization** (tool)
  - https://github.com/chengzeyi/ParaAttention/commit/42e9bb7a5bf273f24854c13c08dbfb6209da8a49
  - *From: JohnDopamine*

- **Triton Windows compilation** (repo)
  - https://github.com/woct0rdho/triton-windows
  - *From: Kijai*

- **DF extension workflow** (workflow)
  - https://github.com/kijai/ComfyUI-WanVideoWrapper/blob/main/example_workflows/wanvideo_skyreels_diffusion_forcing_extension_example_01.json
  - *From: MilesCorban*

- **CausVid model** (model)
  - https://huggingface.co/lightx2v/Wan2.1-T2V-14B-CausVid
  - *From: yi*

- **CausVid paper** (paper)
  - https://causvid.github.io/
  - *From: Vérole*

- **Fun v1.1 models collection** (model)
  - https://huggingface.co/collections/alibaba-pai/wan21-fun-v11-680f514c89fe7b4df9d44f17
  - *From: DeZoomer*

- **Sonic lip sync repo** (repo)
  - https://github.com/jixiaozhong/Sonic
  - *From: Flipping Sigmas*

- **14B VACE development branch** (repo)
  - https://github.com/Wan-Video/Wan2.1/commits/dev/vace/
  - *From: JohnDopamine*

- **NormalCrafter** (tool)
  - https://normalcrafter.github.io/
  - *From: Gateway {Dreaming Computers}*

- **Hunyuan Custom** (repo)
  - https://github.com/Tencent/HunyuanCustom?tab=readme-ov-file
  - *From: Soutlkf*

- **NormalCrafter ComfyUI wrapper** (node)
  - https://github.com/AIWarper/ComfyUI-NormalCrafterWrapper
  - *From: A.I.Warper*

- **Tiger Tank LoRA for Wan 2.1** (lora)
  - https://civitai.com/models/1158489?modelVersionId=1767754
  - *From: MisterMango*

- **T34 Tank LoRA for Wan 2.1** (lora)
  - https://civitai.com/models/1562203/wan21-t2v-soviet-tank-t34
  - *From: MisterMango*

- **Sherman Tank LoRA for Wan 2.1** (lora)
  - https://civitai.com/models/1564089?modelVersionId=1769923
  - *From: MisterMango*

- **Mi-24 Helicopter LoRA** (lora)
  - https://civitai.com/models/1568410?modelVersionId=1774838
  - *From: MisterMango*

- **AH-64 Helicopter LoRA** (lora)
  - https://civitai.com/models/1568429?modelVersionId=1774865
  - *From: MisterMango*

- **KA-52 Helicopter LoRA** (lora)
  - https://civitai.com/models/1569158?modelVersionId=1775683
  - *From: MisterMango*

- **FLF2V workflow on RunningHub** (workflow)
  - https://www.runninghub.ai/post/1921875986818744321
  - *From: David Snow*

- **ComfyUI context tutorial** (tutorial)
  - https://www.youtube.com/watch?v=PcrwJ5C3zGM
  - *From: pom*

- **Beeble AI relighting tool** (tool)
  - https://beeble.ai
  - *From: Valle*

- **CausVid 14B fp8 model** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/blob/main/Wan2_1-T2V-14B_CausVid_fp8_e4m3fn.safetensors
  - *From: Kijai*

- **CausVid project page** (project)
  - https://causvid.github.io/
  - *From: slmonker*

- **CausVid paper and info** (research)
  - https://news.mit.edu/2025/causevid-hybrid-ai-model-crafts-smooth-high-quality-videos-in-seconds-0506
  - *From: yi*

- **Xformers compatibility wheel** (tool)
  - https://download.pytorch.org/whl/xformers/
  - *From: David Snow*

- **German Panther tank LoRA** (lora)
  - https://civitai.com/models/1574908/wan21-t2v-14b-german-panther-ga-tank
  - *From: MisterMango*

- **Pz.IV H tank LoRA** (lora)
  - https://civitai.com/models/1574943/wan21-t2v-14b-german-pziv-h-tank-panzer-4
  - *From: MisterMango*

- **M18 Hellcat Tank LoRA** (lora)
  - https://civitai.com/models/1578601/wan21-t2v-14b-us-army-m18-gmc-hellcat-tank
  - *From: MisterMango*

- **VACE 14B dev branch** (repo)
  - https://github.com/Wan-Video/Wan2.1/tree/dev/vace?tab=readme-ov-file#model-download
  - *From: JohnDopamine*

- **CausVid I2V branch** (repo)
  - https://github.com/tianweiy/CausVid/tree/i2v
  - *From: yi*

- **CausVid GGUF quantized model** (model)
  - https://huggingface.co/Njbx/Wan2.1-T2V-14B-CausVid-GGUF
  - *From: Njb*

- **MoviiGen 1.1 FP8** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/blob/main/Wan2_1-MoviiGen1_1_fp8_e4m3fn.safetensors
  - *From: Kijai*

- **VACE 1.3B module** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/blob/main/Wan2_1-VACE_1_3B_bf16.safetensors
  - *From: Kijai*

- **MoviiGen original** (model)
  - https://huggingface.co/ZuluVision/MoviiGen1.1
  - *From: Njb*

- **VACE 14B official** (model)
  - https://huggingface.co/Wan-AI/Wan2.1-VACE-14B
  - *From: ingi // SYSTMS*

- **VACE 1.3B official** (model)
  - https://huggingface.co/Wan-AI/Wan2.1-VACE-1.3B
  - *From: DawnII*

- **LightX2V config** (repo)
  - https://github.com/ModelTC/lightx2v/blob/main/configs/wan_t2v_causvid.json
  - *From: Kijai*

- **TaylorSeer caching discussion** (repo)
  - https://github.com/Shenyi-Z/TaylorSeer/issues/5#issuecomment-2862664196
  - *From: yi*

- **Wan livestream** (tool)
  - https://x.com/i/broadcasts/1eaKbWYRBEYGX
  - *From: Juampab12*

- **VACE 14B fp8 module** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/blob/main/Wan2_1-VACE_module_14B_fp8_e4m3fn.safetensors
  - *From: Kijai*

- **VACE 14B bf16 module** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/blob/main/Wan2_1-VACE_module_14B_bf16.safetensors
  - *From: Kijai*

- **Causvid 14B fp8** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/blob/main/Wan2_1-T2V-14B_CausVid_fp8_e4m3fn.safetensors
  - *From: Colin*

- **Modelscope download command** (tool)
  - pip install modelscope; modelscope download --model Wan-AI/Wan2.1-VACE-14B
  - *From: JohnDopamine*

- **Model merger tool** (tool)
  - https://drive.google.com/file/d/1iJ4T54opP5-fyEaKY4DrTkrSJVZZuvXL/view?usp=sharing
  - *From: The Punisher*

- **MoviiGen 1.1 GGUF** (model)
  - https://huggingface.co/wsbagnsv1/MoviiGen1.1-GGUF
  - *From: The Punisher*

- **Index-anisora model** (model)
  - https://huggingface.co/IndexTeam/Index-anisora
  - *From: A.I.Warper*

- **MoviiGen 1.1** (model)
  - https://huggingface.co/ZuluVision/MoviiGen1.1
  - *From: DawnII*

- **DG Wan boost models** (model)
  - https://huggingface.co/Evados/DiffSynth-Studio-Lora-Wan2.1-ComfyUI/tree/main/DG_Model_Wan2_1_v1_3b_t2v_Boost_Final
  - *From: David Snow*

- **Comfy repackaged VACE 14B** (model)
  - https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/blob/main/split_files/diffusion_models/wan2.1_vace_14B_fp16.safetensors
  - *From: comfy*

- **VACE 1.3B module** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/blob/main/Wan2_1-VACE_module_1_3B_bf16.safetensors
  - *From: David Snow*

- **CausVid LoRA** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/blob/main/Wan21_CausVid_14B_T2V_lora_rank32.safetensors
  - *From: Kijai*

- **14B VACE FP8 module** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/blob/main/Wan2_1-VACE_module_14B_fp8_e4m3fn.safetensors
  - *From: happy.j*

- **14B VACE full model** (model)
  - https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/blob/main/split_files/diffusion_models/wan2.1_vace_14B_fp16.safetensors
  - *From: DawnII*

- **NormalCrafter for depth processing** (repo)
  - https://github.com/AIWarper/ComfyUI-NormalCrafterWrapper
  - *From: David Snow*

- **IC-Light for detail transfer** (repo)
  - https://github.com/kijai/ComfyUI-IC-Light
  - *From: David Snow*

- **VACE mask usage guide** (documentation)
  - https://github.com/ali-vilab/VACE/issues/45
  - *From: DawnII*

- **DistillT5 for faster text encoding** (repo)
  - https://github.com/LifuWang-66/DistillT5
  - *From: deleted_user_2ca1923442ba*

- **MoviiGen GGUFs** (model)
  - https://www.reddit.com/r/StableDiffusion/comments/1kmuccc/new_moviigen11ggufs/
  - *From: The Punisher*

- **CausVid LoRA workflow** (workflow)
  - *From: seruva19*

- **Wan VACE workflows on Civitai** (workflow)
  - https://civitai.com/models
  - *From: Nokai*

- **Context options documentation** (documentation)
  - https://github.com/Kosinkadink/ComfyUI-AnimateDiff-Evolved/tree/main/documentation/nodes
  - *From: ˗ˏˋ⚡ˎˊ-*

- **CausVid 1.3B LoRA** (lora)
  - https://huggingface.co/Kijai/WanVideo_comfy/blob/main/Wan21_CausVid_bidirect2_T2V_1_3B_lora_rank32.safetensors
  - *From: Kijai*

- **CausVid 14B LoRA** (lora)
  - https://huggingface.co/Kijai/WanVideo_comfy/blob/main/Wan21_CausVid_14B_T2V_lora_rank32.safetensors
  - *From: N0NSens*

- **VACE 1.3B example workflow** (workflow)
  - https://github.com/kijai/ComfyUI-WanVideoWrapper/blob/main/example_workflows/wanvideo_1_3B_VACE_examples_03.json
  - *From: Nokai*

- **Optical flow ComfyUI nodes** (tool)
  - https://github.com/seanlynch/comfyui-optical-flow/tree/main
  - *From: DawnII*

- **Triton Windows build discussion** (tool)
  - https://www.reddit.com/r/StableDiffusion/comments/1kmcddj/updated_triton_v320_updated_v330_py310_updated/
  - *From: TK_999*

- **Kijai WanVideo models** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/tree/main
  - *From: VK (5080 128gb)*

- **Index-anisora model** (model)
  - https://huggingface.co/IndexTeam/Index-anisora
  - *From: slmonker(5090D 32GB)*

- **ComfyUI-WanVideoWrapper** (repo)
  - https://github.com/kijai/ComfyUI-WanVideoWrapper.git
  - *From: JohnDopamine*

- **ImagePadKJ node for outpainting** (node)
  - *From: slmonker(5090D 32GB)*

- **CausVid 1.3B LoRA** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/blob/main/Wan21_CausVid_bidirect2_T2V_1_3B_lora_rank32.safetensors
  - *From: DiXiao*

- **Official 1.3B VACE full model** (model)
  - https://huggingface.co/Wan-AI/Wan2.1-VACE-1.3B/tree/main
  - *From: slmonker(5090D 32GB)*

- **Tiny VAE for VRAM reduction** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/blob/main/taew2_1.safetensors
  - *From: DawnII*

- **Kijai's WanVideo ComfyUI models** (repo)
  - https://huggingface.co/Kijai/WanVideo_comfy/tree/main
  - *From: ˗ˏˋ⚡ˎˊ-*

- **14B VACE GGUF models** (model)
  - https://huggingface.co/QuantStack/Wan2.1-VACE-14B-GGUF
  - *From: The Punisher*

- **Base Model 14B T2V fp8** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/blob/main/Wan2_1-T2V-14B_fp8_e4m3fn.safetensors
  - *From: ˗ˏˋ⚡ˎˊ-*

- **VACE Module 14B fp8** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/blob/main/Wan2_1-VACE_module_14B_fp8_e4m3fn.safetensors
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Causvid Lora 14B** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/blob/main/Wan21_CausVid_14B_T2V_lora_rank32.safetensors
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Causvid Lora 1.3B** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/blob/main/Wan21_CausVid_bidirect2_T2V_1_3B_lora_rank32.safetensors
  - *From: ˗ˏˋ⚡ˎˊ-*

- **ComfyUI MultiGPU fork** (repo)
  - https://github.com/pollockjj/ComfyUI-MultiGPU
  - *From: The Punisher*

- **Sapiens Pose** (repo)
  - https://github.com/smthemex/ComfyUI_Sapiens
  - *From: Nokai*

- **LTX Video VAE** (model)
  - https://huggingface.co/Lightricks/LTX-Video-0.9.7-distilled/blob/main/vae/diffusion_pytorch_model.safetensors
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Native VACE documentation** (documentation)
  - https://docs.comfy.org/tutorials/video/wan/vace
  - *From: The Punisher*

- **City96 GGUF nodes** (repo)
  - https://github.com/city96/ComfyUI-GGUF
  - *From: artemonary*

- **T2V LoRAs for 14B** (model)
  - https://huggingface.co/collections/Remade-AI/wan21-14b-t2v-loras-67dc73d82f66cfac2b4eb253
  - *From: ˗ˏˋ⚡ˎˊ-*

- **ControlFlowUtils** (repo)
  - https://github.com/VykosX/ControlFlowUtils/tree/main
  - *From: ˗ˏˋ⚡ˎˊ-*

- **VACE GitHub repo** (repo)
  - https://github.com/ali-vilab/VACE
  - *From: ˗ˏˋ⚡ˎˊ-*

- **VACE 14B GGUF Reddit post** (post)
  - https://www.reddit.com/r/StableDiffusion/comments/1koefcg/new_wan21vace14bggufs/
  - *From: The Punisher*

- **Wan2.1-Fun-Reward-LoRAs-comfy** (model)
  - https://huggingface.co/Kijai/Wan2.1-Fun-Reward-LoRAs-comfy/tree/main
  - *From: yi*

- **CausVid paper** (research)
  - https://arxiv.org/abs/2412.07772
  - *From: DawnII*

- **MoviiGen1.1 training code** (repo)
  - https://github.com/ZulutionAI/MoviiGen1.1
  - *From: JohnDopamine*

- **WAN LoRAs collection** (model)
  - https://huggingface.co/collections/Remade-AI/wan21-14b-t2v-loras-67dc73d82f66cfac2b4eb253
  - *From: DawnII*

- **ComfyUI VACE documentation** (documentation)
  - https://docs.comfy.org/tutorials/video/wan/vace
  - *From: ˗ˏˋ⚡ˎˊ-*

- **CausVid quantized model** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/blob/main/Wan2_1-T2V-14B_CausVid_fp8_e4m3fn.safetensors
  - *From: quase*

- **Ghibli WAN LoRA** (model)
  - https://civitai.com/models/1474964/ghibli-wan-13b
  - *From: BestWind*

- **DG_Model_Wan2_1_v1_3b_t2v_Boost_Final** (model)
  - https://huggingface.co/Evados/DiffSynth-Studio-Lora-Wan2.1-ComfyUI/tree/main/DG_Model_Wan2_1_v1_3b_t2v_Boost_Final
  - *From: David Snow*

- **CrystalDiskInfo** (tool)
  - https://crystalmark.info/en/software/crystaldiskinfo/
  - *From: ˗ˏˋ⚡ˎˊ-*

- **WAN upscaling tutorial** (tutorial)
  - https://www.youtube.com/watch?v=xY56o8wxQu0&ab_channel=Benji%E2%80%99sAIPlayground
  - *From: CaptHook*

- **Sapiens ComfyUI node** (node)
  - https://github.com/smthemex/ComfyUI_Sapiens
  - *From: VRGameDevGirl84(RTX 5090)*

- **Follow Your Emoji Wrapper** (node)
  - https://github.com/kijai/ComfyUI-FollowYourEmojiWrapper
  - *From: A.I.Warper*

- **Unsafe torch loading node** (node)
  - https://github.com/ltdrdata/comfyui-unsafe-torch
  - *From: MilesCorban*

- **CausVid-Plus repository** (repo)
  - https://github.com/GoatWu/CausVid-Plus
  - *From: aipmaster*

- **Seed1.5-VL captioning model** (model)
  - https://huggingface.co/spaces/ByteDance-Seed/Seed1.5-VL
  - *From: Ada*

- **Inspire Pack nodes** (node)
  - https://github.com/ltdrdata/ComfyUI-Inspire-Pack
  - *From: MilesCorban*

- **PySceneDetect** (tool)
  - https://github.com/Breakthrough/PySceneDetect
  - *From: Piblarg*

- **CausVid 14B LoRA** (lora)
  - https://huggingface.co/Kijai/WanVideo_comfy/blob/main/Wan21_CausVid_14B_T2V_lora_rank32.safetensors
  - *From: VRGameDevGirl84(RTX 5090)*

- **All WAN ComfyUI models** (repo)
  - https://huggingface.co/Kijai/WanVideo_comfy/tree/main
  - *From: ˗ˏˋ⚡ˎˊ-*

- **VACE 14B GGUF models** (model)
  - https://huggingface.co/QuantStack/Wan2.1-VACE-14B-GGUF/tree/main
  - *From: hicho*

- **Origami WAN LoRA** (lora)
  - https://huggingface.co/shauray/Origami_WanLora
  - *From: hicho*

- **4-step CausVid checkpoint** (model)
  - https://huggingface.co/tianweiy/CausVid/tree/main/autoregressive_checkpoint_warp_4step_cfg2
  - *From: hicho*

- **HiDream Sampler removal fix** (repo)
  - https://github.com/SanDiegoDude/ComfyUI-HiDream-Sampler/
  - *From: 100a*

- **KeySync lip-sync tool** (tool)
  - https://antonibigata.github.io/KeySync/
  - *From: Zuko*

- **WanVideo VACE workflows** (workflow)
  - https://ptb.discord.com/channels/1076117621407223829/1342763350815277067/1373677243917926401
  - *From: ˗ˏˋ⚡ˎˊ-*

- **CausVid 1.3B LoRA** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/blob/main/Wan21_CausVid_bidirect2_T2V_1_3B_lora_rank32.safetensors
  - *From: ˗ˏˋ⚡ˎˊ-*

- **MoviiGen1.1** (model)
  - https://github.com/ZulutionAI/MoviiGen1.1
  - *From: JohnDopamine*

- **WAN VACE 14B bf16 model** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/blob/main/Wan2_1-VACE_module_14B_bf16.safetensors
  - *From: David Snow*

- **SAM2 points editor for masking** (tool)
  - https://github.com/kijai/ComfyUI-segment-anything-2
  - *From: David Snow*

- **DetailZ WAN detail enhancer LoRA** (lora)
  - https://civitai.com/models/1385506/detailz-wan-detail-enhancer-for-wan-videos?modelVersionId=1565668
  - *From: David Snow*

- **WAN prompt generator for LLMs** (tool)
  - https://pastebin.com/WiuEUFQp
  - *From: aipmaster*

- **ComfyUI Sapiens nodes** (node)
  - https://github.com/smthemex/ComfyUI_Sapiens/tree/main
  - *From: hablaba*

- **NormalCrafterWrapper** (node)
  - https://github.com/AIWarper/ComfyUI-NormalCrafterWrapper
  - *From: ArtOfficial*

- **ComfyUI_Sapiens** (node)
  - https://github.com/smthemex/ComfyUI_Sapiens
  - *From: Boop*

- **Wan2.1-Fun-Reward-LoRAs** (model)
  - https://huggingface.co/alibaba-pai/Wan2.1-Fun-Reward-LoRAs
  - *From: Kijai*

- **WanVideo_comfy models** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/tree/main
  - *From: JohnDopamine*

- **MediaPipe Iris tracking** (tool)
  - https://research.google/blog/mediapipe-iris-real-time-iris-tracking-depth-estimation/
  - *From: DawnII*

- **NormalCrafter Wrapper** (repo)
  - https://github.com/AIWarper/ComfyUI-NormalCrafterWrapper
  - *From: VRGameDevGirl84(RTX 5090)*

- **MTVCrafter** (repo)
  - https://github.com/DINGYANB/MTVCrafter
  - *From: yi*

- **WAN documentation** (documentation)
  - https://docs.comfy.org/tutorials/video/wan/wan-video
  - *From: zelgo_*

- **WAN Japanese guide** (guide)
  - https://scrapbox.io/work4ai/%F0%9F%A6%8AWan2.1_VACE
  - *From: Guey.KhalaMari*

- **ComfyUI torch compile fix PR** (repo)
  - https://github.com/comfyanonymous/ComfyUI/pull/8213
  - *From: Kosinkadink*

- **MatAnyone node** (repo)
  - https://github.com/KytraScript/ComfyUI_MatAnyone_Kytra
  - *From: JohnDopamine*

- **WanVideoWrapper example workflows** (workflow)
  - *From: Kijai*

- **VACE 14B model** (model)
  - *From: Kijai*

- **CausVid LoRA** (lora)
  - *From: Colin*

- **Skyreels base model** (model)
  - *From: DawnII*

- **RealisDance-DiT** (model)
  - https://huggingface.co/theFoxofSky/RealisDance-DiT
  - *From: yi*

- **RealisDance-DiT project page** (documentation)
  - https://thefoxofsky.github.io/project_pages/RealisDance-DiT/index
  - *From: yi*

- **Video extension workflow** (workflow)
  - https://pastebin.com/sY0zSHce
  - *From: MilesCorban*

- **Custom VACE GPT guide** (tool)
  - https://chatgpt.com/g/g-682d7773290c819188afd2c5e09a0811-wan2-1-vace-video-guide
  - *From: AJO*

- **GRAT speed optimization** (research)
  - https://oliverrensu.github.io/project/GRAT/
  - *From: Ada*

- **ComfyUI OIIO plugin** (tool)
  - https://github.com/melMass/comfy_oiio
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Headless Wan2GP fork** (repo)
  - https://github.com/peteromallet/Headless-Wan2GP
  - *From: pom*

- **Wan2.1-VACE-14B model** (model)
  - https://huggingface.co/Wan-AI/Wan2.1-VACE-14B/tree/main
  - *From: Valle*

- **Wan2.1 control LoRAs** (lora)
  - https://huggingface.co/spacepxl/Wan2.1-control-loras
  - *From: ˗ˏˋ⚡ˎˊ-*

- **SkyReels-A1** (repo)
  - https://github.com/SkyworkAI/SkyReels-A1
  - *From: chrisd0073*

- **GRAT attention** (repo)
  - https://github.com/OliverRensu/GRAT
  - *From: ZeusZeus (RTX 4090)*

- **Pepe Lora** (lora)
  - https://civitai.com/models/1518710?modelVersionId=1718279
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Live Wallpaper Style** (model)
  - https://civitai.com/models/1264662/live-wallpaper-style
  - *From: Mngbg*

- **RollingDepth** (repo)
  - https://github.com/prs-eth/rollingdepth
  - *From: yo9o*

- **RollingDepth demo** (demo)
  - https://rollingdepth.github.io/
  - *From: yo9o*

- **WanVideoWrapper** (repo)
  - https://github.com/kijai/ComfyUI-WanVideoWrapper
  - *From: yo9o*

- **Kijai's WanVideo models** (models)
  - https://huggingface.co/Kijai/WanVideo_comfy/tree/main
  - *From: jerms_ai_(4090_24g)*

- **Frame Interpolation schedule** (reference)
  - https://github.com/Fannovel16/ComfyUI-Frame-Interpolation/blob/main/interpolation_schedule.png
  - *From: JohnDopamine*

- **Aspect ratio calculator** (tool)
  - https://www.aspectratiocalculator.com/16-9.html
  - *From: A.I.Warper*

- **TheDirector workflow** (workflow)
  - https://civitai.com/models/1476469/thedirector
  - *From: AJO*

- **ComfyUI Browser for XY plotting** (tool)
  - https://github.com/talesofai/comfyui-browser
  - *From: Johnjohn7855*

- **Kijai IC-Light with spline editor** (repo)
  - https://github.com/kijai/ComfyUI-IC-Light
  - *From: Johnjohn7855*

- **UniAnimate-W project** (repo)
  - https://github.com/Isi-dev/ComfyUI-UniAnimate-W
  - *From: Guey.KhalaMari*

- **MoviiGen 1.1 VACE GGUF** (model)
  - https://huggingface.co/QuantStack/MoviiGen1.1-VACE-GGUF
  - *From: The Punisher*

- **360 degree rotation LoRA** (lora)
  - https://civitai.com/models/1346623/360-degree-rotation-microwave-rotation-wan21-i2v-lora
  - *From: Yae*

- **Bullet time camera LoRA** (lora)
  - https://civitai.com/models/1475368
  - *From: N0NSens*

- **ControlNet MediaPipe Face** (model)
  - https://huggingface.co/CrucibleAI/ControlNetMediaPipeFace
  - *From: Gateway {Dreaming Computers}*

- **VACE workflow collection** (workflow)
  - https://www.patreon.com/posts/comfyui-workflow-129211762
  - *From: Gateway {Dreaming Computers}*

- **COCO WholeBody pose dataset** (repo)
  - https://github.com/jin-s13/COCO-WholeBody/
  - *From: A.I.Warper*

- **RTMPose implementation** (repo)
  - https://github.com/open-mmlab/mmpose/tree/main/projects/rtmpose
  - *From: A.I.Warper*

- **Samaritan 3D Cartoon SDXL LoRA** (lora)
  - https://civitai.com/models/121932/samaritan-3d-cartoon-sdxl
  - *From: David Snow*

- **VACE Benchmark examples** (dataset)
  - https://huggingface.co/datasets/ali-vilab/VACE-Benchmark/tree/main/assets/examples
  - *From: fazeaction*

- **VACE User Guide** (documentation)
  - https://huggingface.co/datasets/ali-vilab/VACE-Benchmark/blob/main/UserGuide.md
  - *From: ˗ˏˋ⚡ˎˊ-*

- **WAN 2.1 ComfyUI models** (model)
  - https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/tree/main/split_files/diffusion_models
  - *From: ArtOfficial*

- **Jenga GitHub repository** (repo)
  - https://github.com/dvlab-research/Jenga
  - *From: JohnDopamine*

- **TimeUi ComfyUI Timeline Node** (node)
  - https://github.com/jimmm-ai/TimeUi-a-ComfyUi-Timeline-Node
  - *From: chrisd0073*

- **ComfyUI-MotionDiff** (repo)
  - https://github.com/Fannovel16/ComfyUI-MotionDiff
  - *From: Kijai*

- **WAN Video ComfyUI Documentation** (documentation)
  - https://docs.comfy.org/tutorials/video/wan/wan-video
  - *From: zelgo_*

- **Wan 2.1 LoRA collection for 14B T2V** (model)
  - https://huggingface.co/collections/Remade-AI/wan21-14b-t2v-loras-67dc73d82f66cfac2b4eb253
  - *From: ˗ˏˋ⚡ˎˊ-*

- **AziibPixelMix XL checkpoint** (model)
  - https://civitai.com/models/451177/aziibpixelmix-xl
  - *From: A.I.Warper*

- **ComfyUI Pose Interpolation node** (tool)
  - https://github.com/toyxyz/ComfyUI_pose_inter
  - *From: toyxyz*

- **UltraSharpV2 upscaler** (model)
  - https://huggingface.co/Kim2091/UltraSharpV2
  - *From: DawnII*

- **DiffSynth Studio LoRA collection** (model)
  - https://huggingface.co/Evados/DiffSynth-Studio-Lora-Wan2.1-ComfyUI/tree/main/DG_Model_Wan2_1_v1_3b_t2v_Boost_Final
  - *From: David Snow*

- **ComfyUI pose interpolation** (repo)
  - https://github.com/toyxyz/ComfyUI_pose_inter
  - *From: toyxyz*

- **Clarity upscale workflows** (workflow)
  - https://github.com/roblaughter/comfyui-workflows
  - *From: David Snow*

- **InspyreNet RemBG** (repo)
  - https://github.com/john-mnz/ComfyUI-Inspyrenet-Rembg
  - *From: David Snow*

- **SAM2 segment anything** (repo)
  - https://github.com/kijai/ComfyUI-segment-anything-2
  - *From: David Snow*

- **SkyReels CausVid merged model** (model)
  - https://huggingface.co/Zuntan/Wan-SkyReels-CausVid/tree/main
  - *From: hicho*

- **MatAnyone for video matting** (repo)
  - https://github.com/FuouM/ComfyUI-MatAnyone
  - *From: chrisd0073*

- **RES4LYF node pack** (repo)
  - https://github.com/ClownsharkBatwing/RES4LYF
  - *From: A.I.Warper*

- **ComfyUI_FaceAnalysis** (repo)
  - https://github.com/cubiq/ComfyUI_FaceAnalysis
  - *From: David Snow*

- **CausVid LoRA for Wan21 14B T2V** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/blob/main/Wan21_CausVid_14B_T2V_lora_rank32.safetensors
  - *From: David Snow*

- **Remade AI Wan2.1 LoRAs collection** (model)
  - https://huggingface.co/collections/Remade-AI/wan21-14b-480p-i2v-loras-67d0e26f08092436b585919b
  - *From: DawnII*

- **ComfyUI_pose_inter** (repo)
  - https://github.com/toyxyz/ComfyUI_pose_inter
  - *From: toyxyz*

- **Bjornulf custom nodes** (repo)
  - https://github.com/justUmen/Bjornulf_custom_nodes
  - *From: UsamaAhmedKhan*

- **VACE GGUF workflow** (workflow)
  - https://huggingface.co/QuantStack/Wan2.1-VACE-14B-GGUF/tree/main
  - *From: AshmoTV*

- **String formatting node** (node)
  - *From: Guey.KhalaMari*

- **SkyReels CausVid LoRA** (model)
  - https://huggingface.co/Zuntan/Wan-SkyReels-CausVid/tree/main
  - *From: hicho*

- **SkyReels V2 GGUF with CausVid LoRA** (model)
  - https://huggingface.co/QuantStack/SkyReels-V2-T2V-14B-720P-VACE-GGUF/tree/main
  - *From: Vérole*

- **Wan2.1 Fun Reward LoRAs** (model)
  - https://huggingface.co/alibaba-pai/Wan2.1-Fun-Reward-LoRAs/tree/main
  - *From: David Snow*

- **DiffSynth Studio LoRA for Wan2.1** (model)
  - https://huggingface.co/Evados/DiffSynth-Studio-Lora-Wan2.1-ComfyUI/tree/main
  - *From: hicho*

- **Wan2.1 VACE 14B GGUF Q5** (model)
  - https://huggingface.co/QuantStack/Wan2.1-VACE-14B-GGUF/blob/main/Wan2.1-VACE-14B-Q5_0.gguf
  - *From: David Snow*

- **VACE inpainting workflow** (workflow)
  - https://discord.com/channels/1076117621407223829/1342763350815277067/1376124067261714434
  - *From: David Snow*

- **Bagel AI - picture movement and rotation tool** (tool)
  - https://bagel-ai.org/
  - *From: Mngbg*

- **TheDenk Wan ControlNet HED 1.3B** (model)
  - https://huggingface.co/TheDenk/wan2.1-t2v-1.3b-controlnet-hed-v1
  - *From: hicho*

- **TheDenk Wan ControlNet HED 14B** (model)
  - https://huggingface.co/TheDenk/wan2.1-t2v-14b-controlnet-hed-v1
  - *From: pom*

- **AccVideo WanX T2V 14B** (model)
  - https://huggingface.co/aejion/AccVideo-WanX-T2V-14B/tree/main
  - *From: JohnDopamine*

- **Spacepxl Wan Control LoRAs** (model)
  - https://huggingface.co/spacepxl/Wan2.1-control-loras
  - *From: hicho*

- **DG Boost Wan models** (model)
  - https://huggingface.co/Evados/DiffSynth-Studio-Lora-Wan2.1-ComfyUI/tree/main/DG_Model_Wan2_1_v1_3b_t2v_Boost_Final
  - *From: David Snow*

- **Uni3C** (repo)
  - https://github.com/ewrfcas/Uni3C
  - *From: yi*

- **RealisDance** (repo)
  - https://github.com/damo-cv/RealisDance
  - *From: yi*

- **Jenga** (repo)
  - https://github.com/dvlab-research/Jenga
  - *From: MisterMango*

- **Wan21_AccVid_T2V_14B_lora_rank32_fp16.safetensors** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/blob/main/Wan21_AccVid_T2V_14B_lora_rank32_fp16.safetensors
  - *From: Kijai*

- **Uni3C camera control** (repo)
  - https://github.com/ewrfcas/Uni3C, https://huggingface.co/ewrfcas/Uni3C/tree/main
  - *From: slmonker(5090D 32GB)*

- **OmniConsistency** (model)
  - https://huggingface.co/showlab/OmniConsistency
  - *From: happy.j*

- **ComfyUI-BAGEL** (repo)
  - https://github.com/neverbiasu/ComfyUI-BAGEL
  - *From: hicho, fazeaction*

- **BAGEL online demo** (tool)
  - https://huggingface.co/spaces/ByteDance-Seed/BAGEL
  - *From: slmonker(5090D 32GB)*

- **ComfyUI-UNO** (repo)
  - https://github.com/jax-explorer/ComfyUI-UNO
  - *From: JohnDopamine*

- **Jenga research** (repo)
  - https://github.com/dvlab-research/Jenga
  - *From: hicho*

- **Loop workflow** (workflow)
  - https://www.reddit.com/r/StableDiffusion/comments/1ktljys/loop_anything_with_wan21_vace/
  - *From: daking999*

- **Phantom 14B model** (model)
  - https://huggingface.co/bytedance-research/Phantom
  - *From: DawnII*

- **AccVid LoRA** (lora)
  - https://huggingface.co/Kijai/WanVideo_comfy/blob/main/Wan21_AccVid_T2V_14B_lora_rank32_fp16.safetensors
  - *From: Johnjohn7855*

- **HunyuanPortrait** (model)
  - https://huggingface.co/tencent/HunyuanPortrait
  - *From: Gateway {Dreaming Computers}*

- **Mat Anyone ComfyUI node** (tool)
  - https://github.com/KytraScript/ComfyUI_MatAnyone_Kytra
  - *From: JohnDopamine*

- **Wan 2.1 Knowledge Base guide** (guide)
  - https://nathanshipley.notion.site/Wan-2-1-Knowledge-Base-1d691e115364814fa9d4e27694e9468f
  - *From: JohnDopamine*

- **ComfyUI QwenVL for prompting** (tool)
  - https://github.com/alexcong/ComfyUI_QwenVL
  - *From: Johnjohn7855*

- **TAEW2_1.safetensors** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/blob/main/taew2_1.safetensors
  - *From: Kijai*

- **WAN ControlNet Depth v1** (model)
  - https://huggingface.co/TheDenk/wan2.1-t2v-14b-controlnet-depth-v1
  - *From: hicho*

- **Ultimate OpenPose Editor** (tool)
  - https://github.com/toyxyz/ComfyUI-ultimate-openpose-editor
  - *From: toyxyz*

- **MoviiGen Prompt Rewriter** (tool)
  - https://huggingface.co/ZuluVision/MoviiGen1.1_Prompt_Rewriter/tree/main
  - *From: sneako1234*

- **Merged CausVid + AccVid Model** (model)
  - https://huggingface.co/CCP6/blahblah/tree/main
  - *From: JohnDopamine*

- **JohnDopamine's merged model** (model)
  - https://huggingface.co/CCP6/blahblah/tree/main
  - *From: JohnDopamine*

- **SageAttention** (repo)
  - https://github.com/thu-ml/SageAttention
  - *From: aikitoria*

- **SageAttention compiled wheel** (tool)
  - https://huggingface.co/Alissonerdx/sageattention-2.1.0-cu128torch270-cp312-cp312-linux_x86_64.whl/tree/main
  - *From: MaQue*

- **WarperNodes** (node)
  - https://github.com/AIWarper/ComfyUI-WarperNodes
  - *From: A.I.Warper*

- **All Wan models collection** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/tree/main
  - *From: Nekodificador*

- **Wan21_T2V_14B_MoviiGen_lora** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/blob/main/Wan21_T2V_14B_MoviiGen_lora_rank32_fp16.safetensors
  - *From: Kijai*

- **Hakoniwa anime wan models** (model)
  - https://huggingface.co/svjack/hakoniwa_anime_wan2_1_models
  - *From: DawnII*

- **VACE loop workflow** (workflow)
  - https://discord.com/channels/1076117621407223829/1342763350815277067/1375946880793710703
  - *From: David Snow*

- **Phantom model merge** (model)
  - https://discord.com/channels/1076117621407223829/1344057524935983125/1377153370950729809
  - *From: Thom293*

- **Wan 2.1 prompting paper** (paper)
  - https://arxiv.org/pdf/2502.11079v2
  - *From: aikitoria*

- **Normalized Attention Guidance paper** (paper)
  - https://arxiv.org/pdf/2505.21179
  - *From: Ada*

- **SageAttention++ paper** (paper)
  - https://arxiv.org/pdf/2505.21136
  - *From: Ada*

- **MoviiGen LoRA** (lora)
  - https://huggingface.co/Kijai/WanVideo_comfy/blob/e79b038af91ca315fdb638bc4f9fbb543258856f/Wan21_T2V_14B_MoviiGen_lora_rank32_fp16.safetensors
  - *From: David Snow*

- **Uni3C ControlNet** (controlnet)
  - https://huggingface.co/Kijai/WanVideo_comfy/blob/e79b038af91ca315fdb638bc4f9fbb543258856f/Wan21_Uni3C_controlnet_fp16.safetensors
  - *From: David Snow*

- **Depth ControlNet** (controlnet)
  - https://huggingface.co/TheDenk/wan2.1-t2v-14b-controlnet-depth-v1
  - *From: Kijai*

- **DetailZ LoRA** (lora)
  - https://civitai.com/models/1385506/detailz-wan-detail-enhancer-for-wan-videos?modelVersionId=1565668
  - *From: David Snow*

- **ComfyUI OpenPose Editor** (tool)
  - https://github.com/toyxyz/ComfyUI-ultimate-openpose-editor
  - *From: toyxyz*

- **SkyReels V2** (model)
  - https://github.com/SkyworkAI/SkyReels-V2
  - *From: N0NSens*

- **CFGDistill LoRAs** (lora)
  - https://huggingface.co/spacepxl/wan-cfgdistill-loras
  - *From: The Shadow (NYC)*

- **Custom Phantom merge workflow** (workflow)
  - https://discord.com/channels/1076117621407223829/1344057524935983125/1377153370950729809
  - *From: Thom293*

- **SAM2 nodes and workflows** (repo)
  - https://github.com/kijai/ComfyUI-segment-anything-2
  - *From: David Snow*

- **Inpaint Crop and Stitch nodes** (repo)
  - https://github.com/lquesada/ComfyUI-Inpaint-CropAndStitch
  - *From: David Snow*

- **Multiple VACE encodes workflow** (workflow)
  - https://discord.com/channels/1076117621407223829/1342763350815277067/1373697534773563573
  - *From: JohnDopamine*

- **Uni3C controlnet model** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/blob/main/Wan21_Uni3C_controlnet_fp16.safetensors
  - *From: manwanggege*

- **Wan controlnet HED model** (model)
  - https://huggingface.co/TheDenk/wan2.1-t2v-1.3b-controlnet-hed-v1/discussions
  - *From: manwanggege*

- **Wan21_Uni3C_controlnet_fp16.safetensors** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/blob/main/Wan21_Uni3C_controlnet_fp16.safetensors
  - *From: Kijai*

- **ComfyUI-MoGe** (repo)
  - https://github.com/kijai/ComfyUI-MoGe
  - *From: toyxyz*

- **Remade-AI Wan21 14B LoRAs collection** (model)
  - https://huggingface.co/collections/Remade-AI/wan21-14b-480p-i2v-loras-67d0e26f08092436b585919b
  - *From: Johnjohn7855*

- **ComfyUI-Inpaint-CropAndStitch** (repo)
  - https://github.com/lquesada/ComfyUI-Inpaint-CropAndStitch
  - *From: DeZoomer*

- **DiffPhy project** (model)
  - https://bwgzk-keke.github.io/DiffPhy/
  - *From: pom*

- **Jenga dev-wan branch** (repo)
  - https://github.com/dvlab-research/Jenga/tree/dev-wan
  - *From: JohnDopamine*

- **DualParal WAN-based project** (repo)
  - https://github.com/DualParal-Project/DualParal
  - *From: Cseti*

- **LayerAnimate-DiT** (model)
  - https://huggingface.co/Yuppie1204/LayerAnimate-DiT
  - *From: YatharthSharma*

- **CameraBench dataset** (dataset)
  - https://huggingface.co/datasets/syCen/CameraBench
  - *From: mamad8*

- **Phantom 14B GGUF quantizations** (model)
  - https://huggingface.co/QuantStack/Phantom_Wan_14B-GGUF
  - *From: The Punisher*

- **Merged Phantom + CausVid + AccVid model** (model)
  - https://huggingface.co/CCP6/blahblah/tree/main
  - *From: MilesCorban*

- **PerpNeg paper** (paper)
  - https://perp-neg.github.io
  - *From: zelgo_*

- **seed-vc voice swap** (tool)
  - https://github.com/Plachtaa/seed-vc
  - *From: DeZoomer*

- **LatentSync** (tool)
  - https://github.com/ShmuelRonen/ComfyUI-LatentSyncWrapper
  - *From: DeZoomer*

- **TheDirector workflow** (workflow)
  - https://civitai.green/models/1476469/thedirector
  - *From: AJO*

- **CausVid v2 LoRA - attention layers only** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/blob/main/Wan21_CausVid_14B_T2V_lora_rank32_v2.safetensors
  - *From: Kijai*

- **CausVid v1.5 no first block** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/blob/main/Wan21_CausVid_14B_T2V_lora_rank32_v1_5_no_first_block.safetensors
  - *From: Kijai*

- **OpenPose to Mixamo converter** (tool)
  - https://github.com/Astropulse/mixamotoopenpose
  - *From: Relven 96gb*

- **OpenPose rig for Blender** (tool)
  - https://toyxyz.gumroad.com/l/ciojz?layout=profile
  - *From: toyxyz*

- **Dream-O ComfyUI implementation** (repo)
  - https://github.com/ToTheBeginning/ComfyUI-DreamO
  - *From: JohnDopamine*

- **LayerAnimate** (tool)
  - https://layeranimate.github.io
  - *From: DawnII*

- **CausVid v2 LoRA** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/blob/main/Wan21_CausVid_14B_T2V_lora_rank32_v2.safetensors
  - *From: David Snow*

- **ATI trajectory model** (model)
  - https://huggingface.co/bytedance-research/ATI/tree/main
  - *From: JohnDopamine*

- **ATI GitHub repo** (repo)
  - https://github.com/bytedance/ATI
  - *From: Kijai*

- **Ani Wan model** (model)
  - https://civitai.com/models/1626197?modelVersionId=1840868
  - *From: Cubey*

- **Phantom GGUF version** (model)
  - https://huggingface.co/QuantStack/Phantom_Wan_14B-GGUF
  - *From: The Punisher*

- **Direct3D-S2** (model)
  - https://huggingface.co/wushuang98/Direct3D-S2/tree/main
  - *From: Mngbg*

- **Instagram Women LoRA** (model)
  - https://civitai.green/models/1539088/instagram-women
  - *From: VRGameDevGirl84(RTX 5090)*

- **Realism Boost LoRA** (model)
  - https://civitai.green/models/1626063
  - *From: VRGameDevGirl84(RTX 5090)*

- **Wan14B_Detailer/Enhancer_T2V LoRA** (lora)
  - https://civitai.green/models/1626063
  - *From: VRGameDevGirl84(RTX 5090)*

- **Detailz Wan Detail Enhancer LoRA** (lora)
  - https://civitai.green/models/1385506/detailz-wan-detail-enhancer-for-wan-videos
  - *From: VRGameDevGirl84(RTX 5090)*

- **2D Animation Effects LoRA and workflow** (lora)
  - https://discordapp.com/channels/1076117621407223829/1344309523187368046/1377548588804083722
  - *From: 852話 (hakoniwa)*

- **ComfyUI_RopeWrapper** (tool)
  - https://github.com/fssorc/ComfyUI_RopeWrapper
  - *From: AJO*

- **ComfyUI-AdvancedLivePortrait** (tool)
  - https://github.com/PowerHouseMan/ComfyUI-AdvancedLivePortrait
  - *From: toyxyz*

- **Better Film Grain node** (node)
  - https://civitai.com/models/1476469?modelVersionId=1670194
  - *From: AJO*

- **DeZoomer's VACE workflow** (workflow)
  - https://discord.com/channels/1076117621407223829/1377706250376319106/1377706250376319106
  - *From: DeZoomer*

- **Normal maps example** (workflow)
  - https://discord.com/channels/1076117621407223829/1373520070596231251/1374398950924357802
  - *From: VRGameDevGirl84(RTX 5090)*

- **Wan2_1-Wan-I2V-ATI-14B_fp8_e5m2.safetensors** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/blob/main/Wan2_1-Wan-I2V-ATI-14B_fp8_e5m2.safetensors
  - *From: Kijai*

- **Music video example using FaceFusion** (workflow)
  - https://www.youtube.com/watch?v=KVoiooE8C0c&lc=UgxYYcSbDpI5grL_BVJ4AaABAg
  - *From: Ruairi Robinson*


## Known Limitations

- **FantasyTalker lip sync quality**
  - Sync is always a little off, even in official demos
  - *From: amli*

- **VACE face issues at low resolution**
  - Badly screws faces at 640x360 when face is mid-distance
  - *From: xwsswww*

- **Fun camera control rotation limits**
  - 180 rotation around subject potentially too far within 81 frames
  - *From: DevouredBeef*

- **Context windows beyond 81 frames**
  - Breaks hard after 81 frames, changes input image
  - *From: slmonker(5090D 32GB)*

- **Fun camera creates 2D parallax effect**
  - Movement feels fake, like 2D parallax rather than true 3D rotation
  - *From: N0NSens*

- **Eyes don't move/follow properly in 1.3B models**
  - Biggest problem with face videos, eyeballs don't track motion. Only way to deal with this is post-processing with LivePortrait
  - *From: David Snow*

- **DG models introduce flashing with stronger versions**
  - Higher versions more likely to flash, need stronger versions for stylization but they're flash prone
  - *From: David Snow*

- **Video Depth Anything has banding issues**
  - Creates hard lines and ridges that cause wobbling artifacts in VACE and Fun Control results
  - *From: Nathan Shipley*

- **VACE always adds people when trying to remove objects**
  - Difficult to remove people/objects from scenes, tends to re-add them
  - *From: PirateWolf*

- **Only about 5 useful style LoRAs for 1.3B**
  - Main usable ones are flat color, studio ghibli, and cyberpop. Much fewer good 1.3B LoRAs compared to checkpoints
  - *From: David Snow*

- **VACE struggles with multiple control types**
  - Due to specificity requirements in control maps matching training data
  - *From: Rishi Pandey*

- **Base 1.3B can't use pose control**
  - Can only use depth, lineart or normals - pose requires VACE
  - *From: David Snow*

- **HunyuanVideo FramePack lacks control**
  - Only has prompt travel which is far from real control, no equivalent to VACE
  - *From: Draken*

- **HunyuanVideo starts looping at 201 frames**
  - Model begins to create loops when generating beyond 201 frames
  - *From: Draken*

- **Single start frame is limited for complex scenes**
  - Problems when hands move off-screen, backgrounds change, or other elements not visible in start frame
  - *From: David Snow*

- **FP8 not supported on RTX 3090 and older GPUs**
  - Causes compilation errors with triton, must be disabled
  - *From: Juan Gea*

- **VACE only works with 1.3B models**
  - Cannot use VACE with 14B models, limited to smaller model size
  - *From: Christian Sandor*

- **No LoRA compatibility between 1.3B and 14B**
  - LoRAs trained for one size don't work with the other
  - *From: MilesCorban*

- **Ubuntu 24.04 has CUDA compatibility issues**
  - Causes various problems, 22.04 recommended instead
  - *From: UsamaAhmedKhan*

- **CausVid has no UI implementations yet**
  - Model available but no ComfyUI or other UI support
  - *From: yi*

- **Frame count limits cause looping**
  - Generating more than 81 frames (vanilla) causes videos to loop backwards or show artifacts
  - *From: Nokai*

- **LoRA merging issues**
  - Using multiple LoRAs often results in one not being applied properly
  - *From: Dream Making*

- **1.3B model quality limitations**
  - Lacks concept understanding compared to 14B, harder to train LoRAs on
  - *From: Piblarg*

- **VACE character consistency**
  - Generates slightly different images than input, character appearance can drift
  - *From: Valle*

- **CausVid has artifacts at video start**
  - First 8 frames often have glitches that need removal
  - *From: Vérole*

- **CausVid can't use TeaCache or FETA**
  - Optimization techniques don't work with distilled model
  - *From: Kijai*

- **CausVid motion doesn't work properly beyond 81 frames**
  - Needs additional code implementation for longer videos
  - *From: Kijai*

- **Consistent character workflow still has issues**
  - Hair changes, clothing color changes even with full pipeline
  - *From: David Snow*

- **IPAdapter only 256x256 input resolution**
  - Not enough detail for precise character consistency
  - *From: Draken*

- **CausVid not properly usable yet**
  - Current implementation doesn't match intended sampling method with sliding window and kv_cache
  - *From: Kijai*

- **MoviiGen is T2V only**
  - Cannot do I2V, just T2V finetune
  - *From: Kijai*

- **FP8 quality degradation**
  - FP8 has quality hit and won't stack with fp16_fast for significant benefit
  - *From: Kijai*

- **TEAcache quality loss**
  - TEAcache can lower quality a fair bit
  - *From: deleted_user_2ca1923442ba*

- **MoviiGen huge file size**
  - Model is very large, probably in FP32 format
  - *From: Dream Making*

- **14B VACE doesn't work with native ComfyUI nodes yet**
  - Uses different blocks, only wrapper implementation available
  - *From: Kijai*

- **VACE modules are only available in bf16**
  - No fp8 versions for VACE modules
  - *From: Kijai*

- **14B works poorly at low resolutions where 1.3B excels**
  - Resolution-dependent performance differences
  - *From: Kijai*

- **Fast motion causes quality degradation**
  - Motion speed affects output quality
  - *From: Kijai*

- **VACE doesn't work with Fun models**
  - Only works with original T2V based models, Fun models are incompatible
  - *From: Kijai*

- **CausVid reduces reference strength with VACE**
  - When used together, CausVid can't do precise control and weakens reference
  - *From: Kijai*

- **MoviiGen preview still shows teacache artifacts**
  - Quality issues persist in preview generations
  - *From: DawnII*

- **VACE 14B requires significant VRAM**
  - 35GB model, needs block swapping even on high-end GPUs
  - *From: Kijai*

- **CausVid not fully implemented yet**
  - KJ mentioned it's not done at all and proper use wouldn't support VACE
  - *From: Kijai*

- **TeaCache and SLG don't work with CausVid**
  - Because CausVid doesn't use CFG, these nodes won't work
  - *From: Kijai*

- **No proper way to use multiple first frames at different starting points**
  - Context options always take first frame as reference, works better with reference instead
  - *From: Kijai*

- **Flex attention very strict about dimensions**
  - Most dimensions tried just errored out, 14B at 480p gives poor results
  - *From: Kijai*

- **Difficult to blend control inputs with VACE**
  - Fundamentally difficult due to how VACE works, only working way is using multiple VACEs
  - *From: Kijai*

- **CausVid seems deterministic**
  - Same results for a prompt regardless of seed
  - *From: Ada*

- **CausVid not used as originally intended**
  - Model meant for 3 latent windows with specific sampling code, current usage is hacky
  - *From: Kijai*

- **Reference fading in long generations**
  - VACE reference only fed to first sampler, loses strength over time in DF
  - *From: DawnII*

- **Prompt delay in CausVid generations**
  - Prompt doesn't seem to take effect until ~2 seconds into video
  - *From: Jonathan*

- **UniAnimate needs I2V model**
  - Cannot combine UniAnimate with CausVid on T2V models
  - *From: Kijai*

- **CausVid has adverse effects when not used as intended**
  - Model not trained to be used as LoRA, but control methods like VACE mitigate most issues
  - *From: Kijai*

- **Detail loss with distilled models**
  - Small details are lost, happens to some extent with these models generally
  - *From: Kijai*

- **1.3B model insufficient for understanding specifics**
  - Cannot understand specific details as well as 14B model
  - *From: Piblarg*

- **VACE breaks at high speed complex scenes**
  - Expected to fail with complex martial arts scenes or high-speed movement
  - *From: cyncratic*

- **Blurry hands remain an issue**
  - Hands still come out blurry even with VACE 14B
  - *From: Piblarg*

- **Wan's weakness is hands**
  - Hand generation is problematic, though skip layer guidance can help
  - *From: Piblarg*

- **CausVid has degradation over time**
  - Especially apparent with CausVid, each subsequent iteration is slower with quality degradation
  - *From: DawnII*

- **VACE doesn't work well with combined controls**
  - Combining depth and pose controls is unreliable and often reveals pose bones
  - *From: ˗ˏˋ⚡ˎˊ-*

- **SkyDF 1.3B doesn't understand input images**
  - While extremely fast, SkyDF 1.3B is extremely useless because it doesn't understand what to do with input images
  - *From: N0NSens*

- **1.3B poor face quality in wide shots**
  - Cannot handle images with small heads, needs medium/close shots
  - *From: slmonker(5090D 32GB)*

- **CausVid produces plastic look and broken physics**
  - Quality trade-off for speed, worse than regular models
  - *From: DiXiao*

- **CausVid not properly implemented**
  - Current inference logic different from intended use, but works anyway
  - *From: ˗ˏˋ⚡ˎˊ-*

- **VACE unreliable with combined controls**
  - Combining pose and depth often produces artifacts
  - *From: ˗ˏˋ⚡ˎˊ-*

- **1.3B has low-level noise and poor detail**
  - Noticeable quality degradation compared to 14B
  - *From: ˗ˏˋ⚡ˎˊ-*

- **1.3B model poor with references**
  - 1.3B model is quite bad with references compared to 14B, not great with details
  - *From: Stad*

- **VACE unstable for facial expressions**
  - VACE is unstable for facial expression and hard to get right if the person is completely different from reference
  - *From: chrisd0073*

- **Native VACE doesn't support addons**
  - Native workflow doesn't allow VACE addons for now, unlike wrapper implementation
  - *From: The Punisher*

- **Wrapper doesn't support GGUF**
  - Kijai's wrapper doesn't support GGUF models, need to use native workflow for GGUF
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Cannot use two GPUs in parallel for generation**
  - Can offload CLIP to second GPU but not run models simultaneously
  - *From: The Punisher*

- **GGUF models don't work with Kijai wrapper**
  - Only compatible with native ComfyUI implementation
  - *From: The Punisher*

- **Causvid LoRA unpredictable results**
  - Works well but results can be inconsistent
  - *From: artemonary*

- **VACE doesn't support multiple control types well**
  - Combination of several controls causes issues
  - *From: artemonary*

- **Native VACE limited compared to wrapper**
  - Cannot load as addon to another model, wrapper has better support
  - *From: Draken*

- **Distilled models lose motion**
  - Speed optimization comes at cost of motion detail
  - *From: Draken*

- **GGUF models don't work with Kijai's wrapper**
  - Quantized GGUF versions only work with native ComfyUI workflows
  - *From: Davidodave*

- **CausVid kills quality with some FX LoRAs**
  - Very drastic quality hit when combined with certain effect LoRAs
  - *From: JohnDopamine*

- **MoviiGen only supports T2V**
  - No I2V capability, only text-to-video generation
  - *From: JohnDopamine*

- **MoviiGen + VACE + CausVid LoRA I2V produces poor results**
  - Combination doesn't work well for image-to-video
  - *From: N0NSens*

- **VACE removes 16fps restriction but adds complexity**
  - While solving framerate issues, requires more complex workflow setup
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Long video generation limited by VRAM**
  - OOM issues when going over 121 frames on RTX 5090, maximum ~6 seconds vs Runway's 20 seconds
  - *From: VRGameDevGirl84(RTX 5090)*

- **Context switching creates jumps in long videos**
  - When generating 300+ frames in chunks, visible jumps occur at context boundaries (background characters appearing/disappearing)
  - *From: ˗ˏˋ⚡ˎˊ-*

- **H.265 video compatibility**
  - H.265 encoded videos don't play in some browsers/Discord clients, though they save disk space
  - *From: ˗ˏˋ⚡ˎˊ-*

- **14B model memory requirements**
  - Even with 96GB RAM, extensive offloading is needed for 14B models
  - *From: David Snow*

- **Animal pose detection is poor quality**
  - ControlNet_aux animal pose detection produces very bad results, advised against using
  - *From: David Snow*

- **MediaPipe doesn't capture mouth movement well**
  - Standard MediaPipe face mesh fails to capture detailed mouth movements
  - *From: VRGameDevGirl84(RTX 5090)*

- **Sapiens has color-based errors for body detection**
  - Sapiens can misassign human parts when colors cause confusion
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Original CausVid only supports 1.3B model**
  - Original CausVid implementation doesn't support 14B models
  - *From: aipmaster*

- **VACE only works with T2V models, not I2V**
  - Attempting to use I2V models with VACE causes attribute errors
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Multiple VACE embeds can cause oversaturation**
  - Using reference images in multiple encoders leads to cooked/oversaturated results
  - *From: VRGameDevGirl84(RTX 5090)*

- **Input resolution must be divisible by 16**
  - Tensor size mismatches occur if input dimensions aren't properly divisible
  - *From: Kijai*

- **TeaCache may interfere with low step generation**
  - Step-based optimizations can have more weight impact on 4-8 step generation
  - *From: JohnDopamine*

- **Limited 1.3B model LoRAs available**
  - Most LoRAs are for 14B models, only 1 LoRA available for 1.3B
  - *From: Mngbg*

- **VACE context loses information between chunks**
  - When using context for long videos, some information can be lost between chunks, like clothing changes
  - *From: ˗ˏˋ⚡ˎˊ-*

- **CausVid 1.3B quality is poor**
  - Quality of 1.3B CausVid is really bad, not same team behind it and needs special sampling code
  - *From: ˗ˏˋ⚡ˎˊ-*

- **First few frames of VACE Reference output are noisy**
  - VACE Reference produces noisy first frames, may be related to reference not matching video being generated
  - *From: Fawks*

- **LoRA compatibility between models**
  - LoRAs trained on base WAN work with SkyReels but not with MoviiGen
  - *From: JohnDopamine*

- **SLG and Zero Star don't work with CFG 1.0**
  - Code never executes with CFG 1.0, so these optimizations have no effect
  - *From: Kijai*

- **TeaCache coefficients not calculated for CausVid setup**
  - Using TeaCache with distillation models may not work properly as coefficients are off
  - *From: Kijai*

- **VACE doesn't separate ref from input frames/mask**
  - Everything is processed as one unit, need multiple VACEs for separate control
  - *From: Kijai*

- **Lines control bakes lines into output**
  - Even with semi-transparent lines, they get baked into the final video
  - *From: Blink*

- **Face preprocessors output points that VACE can't interpret**
  - Point-based face controls don't work well with VACE
  - *From: ˗ˏˋ⚡ˎˊ-*

- **VACE struggles with less realistic content**
  - Has difficulty with animated or stylized characters
  - *From: Piblarg*

- **CausVid makes generations feel stiff and lose dynamics**
  - Characters get frozen facial expressions and jerky movement, similar to VEO2
  - *From: amli*

- **VACE doesn't capture eye movement well**
  - Eye darting movements are often lost in generation
  - *From: VRGameDevGirl84(RTX 5090)*

- **LivePortrait is very picky about head position**
  - Moving head too much causes bobble head effect
  - *From: VRGameDevGirl84(RTX 5090)*

- **Model doesn't know specific characters without descriptive prompts**
  - Needs explicit description like 'animated character' or 'Disney character' to recognize characters like Shrek
  - *From: VRGameDevGirl84(RTX 5090)*

- **VACE incompatible with I2V models**
  - VACE module only works with T2V versions of WAN, cannot be used with I2V models
  - *From: DawnII*

- **CausVid doesn't work with I2V in wrapper currently**
  - CausVid LoRA cannot be used with I2V models in the wrapper workflow currently
  - *From: Kijai*

- **Points Editor can't delete first or last points**
  - JavaScript limitations prevent deleting the first or last point in the points editor - always maintains a point pair
  - *From: Kijai*

- **540p Skyreels quality is poor**
  - 540p version of Skyreels produces terrible results in testing
  - *From: Ada*

- **Native ComfyUI VACE lacks module support**
  - Native ComfyUI only supports full VACE model, no module version to use with other WAN models
  - *From: zelgo_*

- **VACE doesn't support blurred masks for inpainting**
  - Sharp masks work but blurred masks cause issues
  - *From: Kijai*

- **Model limited to 81 frames properly, longer videos start to break down**
  - Requires context windows or other techniques for longer generations
  - *From: Kijai*

- **Third VACE embed appears to have no effect**
  - Likely code limitation in wrapper
  - *From: Kijai*

- **Under 5 frames with reference doesn't work reliably**
  - Need minimum 5 frames for reference-based generation
  - *From: Kijai*

- **Context options break motion tracking**
  - Using context options with CausVid can make it completely not follow motion
  - *From: VK (5080 128gb)*

- **NormalCrafter inconsistent with different frame counts**
  - 49 vs 81 frames yields entirely different results even with fixed seed
  - *From: Guey.KhalaMari*

- **Direct input only works with similar structure**
  - Input frames method only works if reference image has same structure as first frame of video
  - *From: VRGameDevGirl84(RTX 5090)*

- **High resolution memory requirements**
  - 1280x720 at 85 frames crashes at decode stage even with 40 block swap on RTX 5090
  - *From: AJO*

- **Video models trained on 8-bit color**
  - All image/video models and VAEs are trained on 8-bit, tensors are 32-bit but represent 8-bit colors
  - *From: ˗ˏˋ⚡ˎˊ-*

- **VACE control combinations**
  - Difficult to use control video + reference frame + LoRA all together - usually can only do 2 of 3 successfully
  - *From: Piblarg*

- **VACE masking doesn't work like traditional controlnets**
  - Can't properly mask VACE effect like traditional controlnets - trying to mask depth maps results in no head or literal depth image artifacts
  - *From: Draken*

- **High resolution limits**
  - Going much higher than 7280x1440 causes the model to start losing detail like the 1.3B model
  - *From: ZombieMatrix*

- **MPS LoRA compatibility**
  - MPS LoRA only works with Fun model, not compatible with normal WAN models
  - *From: ˗ˏˋ⚡ˎˊ-*

- **VACE cannot target loras to specific masks**
  - Currently not possible to apply different loras to different parts of the image using masks
  - *From: David Snow*

- **DWPose doesn't work well for distant shots**
  - DW pose does not work well for far away shots for mouth movement, also normal and depth don't grab facial unless super close
  - *From: VRGameDevGirl84(RTX 5090)*

- **Context window generation is very slow**
  - Best to use with 1.3B model and/or CausVid LoRA due to extreme slowness
  - *From: Kijai*

- **81 frames not enough for scene transformation**
  - 81 frames is not enough for a scene transformation seemingly
  - *From: AJO*

- **Latent sync requires 25 FPS**
  - Latent sync requires 25 FPS which causes sync issues with other frame rates
  - *From: VRGameDevGirl84(RTX 5090)*

- **UniAnimate pose retargeting fails with arm extension**
  - Almost always extends arms incorrectly when retargeting poses, barely works except with their example inputs
  - *From: Kijai*

- **Depth control overpowers reference image for body shape**
  - When trying to change body proportions, depth control is too strong and loses reference image details
  - *From: boorayjenkins*

- **VACE redraws characters even with pose-only control**
  - VACE tends to redraw the input character even when only using pose control without other inputs like depth or normals
  - *From: N0NSens*

- **Pose detection fails with complex clothing**
  - Spinning dresses and complex clothing items cause pose detection to fail completely
  - *From: A.I.Warper*

- **I2V with Causvid has poor prompt adherence**
  - Model listens to prompts very poorly when using I2V with Causvid LoRA
  - *From: N0NSens*

- **OpenPose preprocessing is unreliable**
  - OpenPose preprocessing is the biggest limitation holding back open source video generation
  - *From: Draken*

- **FantasyTalking model only supports 3 seconds**
  - New lip sync model is limited to very short durations and is extremely slow
  - *From: VRGameDevGirl84(RTX 5090)*

- **VACE FaceReference fails at glancing angles**
  - Face reference node struggles with identity preservation when face is not frontal
  - *From: Mads Hagbarth Damsbo*

- **MediaPipe face detection breaks beyond 45 degrees**
  - MediaPipe fails when face angle exceeds 45 degrees or mouth is too open
  - *From: Mads Hagbarth Damsbo*

- **Context windows lose character likeness in long sequences**
  - Processing 161+ frames with context windows results in character identity drift
  - *From: A.I.Warper*

- **CausVid LoRA compatibility unclear**
  - Uncertain if CausVid LoRA works with i2v, VACE models or only t2v
  - *From: patientx*

- **VACE can't perform miracles with unrelated poses**
  - Images need to have some relation to the desired pose/movement for VACE to work effectively
  - *From: David Snow*

- **Color shifts occur when extending videos**
  - Noticeable color changes and quality degradation when using multiple VACE extensions, likely due to VAE encoding/decoding
  - *From: ArtOfficial*

- **Native ComfyUI VACE is not modular**
  - Native VACE support lacks the flexibility of Kijai's wrapper implementation
  - *From: David Snow*

- **LoRAs trained on 1.3B model don't work with 14B model**
  - LoRAs are not compatible between different model sizes
  - *From: MilesCorban*

- **Wan struggles with small faces in wide shots**
  - Even with 14B model, small faces in wide shots remain challenging
  - *From: traxxas25*

- **VACE doesn't work well with blended control net inputs**
  - Can't blend multiple control net outputs like depth + pose, they need separate encoders
  - *From: VRGameDevGirl84(RTX 5090)*

- **CausVid doesn't work with I2V models**
  - CausVid LoRA incompatible with image-to-video models, only works with T2V
  - *From: Cubey*

- **Frame interpolation quality issues**
  - Current frame interpolation technology produces undesirable results, need better morphing tech
  - *From: deleted_user_2ca1923442ba*

- **Wan prompt weighting not working**
  - Weighted prompts like (text:0.5) appear to be treated as full 1.0 weight
  - *From: the_darkwatarus_museum*

- **Multi encode VACE degrades quality**
  - Adding second encode with dwpose makes video quality go to shit
  - *From: David Snow*

- **FollowYourEmoji threshold unforgiving**
  - Only works with 'big' faces, would need face crop -> analyze -> repaste workflow
  - *From: Valle*

- **Color drift in long videos**
  - Colors drift over time becoming crispier and crispier with overlapping batch method
  - *From: notid*

- **VACE not as sharp on higher resolutions**
  - Friend reported VACE not as sharp as normal Wan on higher resolutions
  - *From: The Punisher*

- **Context issues persist**
  - 275 frame context problems occur with both full input image and isolated input
  - *From: N0NSens*

- **CausVid LoRA reduces expressiveness**
  - Makes well-working LoRAs less expressive due to tranquilizing effect
  - *From: hablaba*

- **VACE model visual quality issues**
  - Visual quality is garbage compared to original i2v 720p at full samples
  - *From: aikitoria*

- **Vid2vid with CausVid setup difficulty**
  - Step counts and denoise values are tricky to setup for vid2vid with CausVid
  - *From: Kijai*

- **Impossible character fitting**
  - Cannot fit characters with very different shapes (e.g., Spongebob into human silhouette)
  - *From: David Snow*

- **VACE extension works poorly with masks and has motion/color shifts**
  - Extension causes different motion and colors to shift, and phases to slightly wrong video rather than seamless continuation
  - *From: Kijai*

- **FantaTalker not compatible with VACE**
  - FantaTalker is for I2V model and I2V conditioning is not compatible with VACE
  - *From: Kijai*

- **VACE extension unusable for video extension on 14B**
  - Giving initial image + last 16 frames results in visible break and low quality, unusable for extension
  - *From: aikitoria*

- **DiffSynth only available for 1.3B model**
  - No DiffSynth support for 14B model currently
  - *From: hicho*

- **Wan can't hear audio**
  - Not multimodal, lip sync is from prompting 'talking' not audio input
  - *From: VRGameDevGirl84(RTX 5090)*

- **AccVideo scheduler requires denoise 1.0**
  - Won't work with denoise settings under 1.0
  - *From: Kijai*

- **Quality degradation in extended videos**
  - Using last frame as reference repeatedly degrades quality each batch
  - *From: VRGameDevGirl84(RTX 5090)*

- **VACE lighting override**
  - Takes too much lighting from reference image, overrides scene lighting, can't control this
  - *From: Ruairi Robinson*

- **Wan frame count restrictions**
  - Can't do 44 frames, can do 41 or 45. Formula: divide by 4 plus 1
  - *From: David Snow*

- **AccVid seems worse for stylized content**
  - AccVid good for realistic content but useless for stylized, definitely seems worse than CausVid for unintended use
  - *From: Kijai*

- **AccVid I2V loses prompt following**
  - I2V with AccVid has decent quality but prompt following is gone, though some seeds do follow prompt
  - *From: Kijai*

- **TeaCache not good with AccVid**
  - TeaCache generates messy results with AccVid and only saves 10 seconds
  - *From: TK_999*

- **Context options don't work with 1.3B**
  - Context options for longer videos work with 14B but not with 1.3B model
  - *From: N0NSens*

- **VACE GGUF support unlikely**
  - Would be a lot of work for something developer wouldn't use
  - *From: Kijai*

- **Phantom 14B doesn't work well with CFG distillation**
  - Relies on CFG and has 3 noise predictions making it slow
  - *From: Kijai*

- **Phantom 14B trained on 480P data**
  - Can work at 720P+ but results may be less stable
  - *From: Guey.KhalaMari*

- **CausVid LoRA doesn't work well with Phantom**
  - Phantom needs CFG so acceleration methods are limited
  - *From: Kijai*

- **Sliding context windows have visible seams**
  - Without tight control like VACE, windows don't blend well and seams are visible
  - *From: Kijai*

- **Mediapipe face detection is unreliable**
  - Very hit or miss, half the time doesn't detect face even when prominent
  - *From: David Snow*

- **Phantom extremely slow generation**
  - 1375.69 seconds on RTX Pro 6000, described as 'unbelievably slow'
  - *From: aikitoria*

- **CausVid quality degradation**
  - Quality drop is pretty immense with CausVid, causes flicker at 1.0 strength
  - *From: Kijai*

- **Phantom character rendering failures**
  - Sometimes fails and only renders one of multiple characters
  - *From: aikitoria*

- **VACE color shifts**
  - VACE causes color shifts that need correction
  - *From: pom*

- **Video artifacts with fast movement**
  - Fast movements cause chattery tiled noise, sometimes only solution is slower input
  - *From: Kijai*

- **Preview flashing with references**
  - Preview flashes between reference images and generated content due to latent structure
  - *From: aikitoria*

- **Phantom is very slow**
  - ~55 seconds/step at 480p, slower than other models
  - *From: hau*

- **CausVid works very badly with new Phantom**
  - Will technically produce result but quality is poor
  - *From: aikitoria*

- **Lip sync difficult on wide shots**
  - Only really works with close-up shots, far away shots make mouth movement inaccurate
  - *From: VRGameDevGirl84(RTX 5090)*

- **Phantom file size is huge**
  - Large model size causes storage issues
  - *From: multiple users*

- **Prompt adherence is really bad**
  - Difficulty getting range of emotions from faces, struggles with complex prompts
  - *From: hau*

- **Quality looks more plasticky with merged models**
  - Speed improvement comes at cost of more plastic-looking output
  - *From: hau*

- **Adding controls to Phantom reduces quality**
  - Any additional controls added to phantom reduce quality and take away ID preserving functionality
  - *From: Johnjohn7855*

- **1280x720 causes OOM**
  - Resolution limit on 4080 16gb system
  - *From: CaptHook*

- **Black noise prevalent in fp8**
  - fp8 quantization introduces black noise artifacts
  - *From: Kijai*

- **Uni3C extreme motions don't work well**
  - Orbit motion is too extreme, works better with simpler motions
  - *From: Kijai*

- **VACE + Phantom compatibility issues**
  - Haven't had much success using VACE with Phantom, causes wicked flashes
  - *From: Kijai*

- **CausVid affects motion with I2V**
  - Works but affects motion quite a bit when used with I2V models
  - *From: Kijai*

- **AccVid affects character consistency**
  - AccVideo changes character consistency too much when combined with Phantom
  - *From: David Snow*

- **Frame limitations with certain models**
  - Model doesn't like using more than 121 frames
  - *From: aikitoria*

- **DWPose failures on stylized characters**
  - ComfyUI DWPose fails frequently on stylized characters
  - *From: A.I.Warper*

- **Phantom extraction as LoRA unsuccessful**
  - Tried to extract Phantom as LoRA but it didn't work at all
  - *From: Kijai*

- **Uni3C only works with I2V models**
  - Cannot currently work with T2V models due to latent architecture differences
  - *From: Kijai*

- **VACE doesn't work with I2V models**
  - Architecture incompatibility prevents VACE from working with I2V
  - *From: Kijai*

- **Uni3C + VACE combination not possible**
  - Since Uni3C requires I2V and VACE works with T2V, they cannot be combined
  - *From: Kijai*

- **4K processing challenging in ComfyUI**
  - Pipeline issues and VRAM limitations make 4K processing difficult
  - *From: chrisd0073*

- **Phantom accuracy degrades with multiple controls**
  - Adding more controls to Phantom reduces its ability to maintain consistency
  - *From: Thom293*

- **Uni3C doesn't work with VACE**
  - Uni3C is I2V model so incompatible with VACE, though paper suggests it should be compatible
  - *From: Guey.KhalaMari*

- **Phantom loses referencing when combined with other tools**
  - Phantom is good alone but loses referencing functionality when combined with anything else like VACE or controlnets
  - *From: Johnjohn7855*

- **14B depth controlnet has limited effectiveness**
  - Works fine or great with some inputs, then not at all with others, similar to Flux controlnets
  - *From: Kijai*

- **DollyZoom doesn't work with Uni3C**
  - Attempting to use DollyZoom in/out with Uni3C produces no working results
  - *From: slmonker(5090D 32GB)*

- **Can't fully capture likeness with speed LoRAs**
  - Have to switch off causvid and accvideo loras to get proper character likeness, making testing prohibitive due to long generation times
  - *From: David Snow*

- **Phantom can't be used with Uni3C**
  - Since Phantom is T2V and Uni3C requires I2V, they are incompatible
  - *From: Johnjohn7855*

- **AccVid doesn't work well on its own**
  - From personal testing, AccVid needs to be combined with CausVid + Phantom, doesn't work well with VACE
  - *From: Johnjohn7855*

- **Uni3c doesn't work well with very short generations**
  - Really short generations probably just don't work well
  - *From: Kijai*

- **Some images don't want to animate properly with Uni3c**
  - Success depends on input image, complex camera movements can cause failure
  - *From: N0NSens*

- **Characters try to adjust to camera rather than follow prompt with Uni3c**
  - Feeling that characters adapt to camera movement instead of prompt instructions
  - *From: N0NSens*

- **T2V character LoRAs don't work with VACE**
  - Only I2V character LoRAs would work, but none found
  - *From: hicho*

- **Phantom extracting as LoRA doesn't work**
  - Kijai tried extracting Phantom as LoRA but it didn't work
  - *From: Johnjohn7855*

- **All-in-one models suffer from LoRA integration**
  - Merged models lose ability to adjust LoRA settings and suffer quality loss
  - *From: Kijai*

- **VACE can't blur masked input area**
  - You can't blur the masked area in the input, the one that's supposed to be gray. Because then it's no longer gray for the blurred area
  - *From: Kijai*

- **Kontext limited for major edits**
  - Can't do perspective shifts like Runway, can't do major out of context edits well like 4o
  - *From: pom*

- **CausVid v2 poor prompt following**
  - v2 sucks for the prompt following
  - *From: hicho*

- **Full power Phantom too slow**
  - It's just too slow for me to bother with - referring to full Phantom without distillation
  - *From: Kijai*

- **Character LoRA not viable option**
  - Character lora will never be an option unfortunately
  - *From: AJO*

- **ATI missing HTML trajectory editor**
  - Model released without the web interface for creating trajectories
  - *From: Mngbg*

- **ATI may not work properly at small resolutions**
  - Potentially issues with 640x480 resolution
  - *From: Mngbg*

- **ATI is I2V only, doesn't work with VACE**
  - Limited to image-to-video, not compatible with VACE system
  - *From: Kijai*

- **Uni3c kills prompt following**
  - When using reference video for camera motion, prompt adherence suffers
  - *From: mamad8*

- **Phantom doesn't work well when paired with VACE**
  - Good by itself but compatibility issues with VACE
  - *From: David Snow*

- **VACE face variance**
  - There will be some variance in faces - close but not exact, good for generic face swaps but bad for specific exact face swaps
  - *From: David Snow*

- **Text/lettering issues**
  - WAN has problems with generating accurate lettering
  - *From: TimHannan*

- **Prompt following with CausVid**
  - CFG stuck at 1 means prompt following isn't fantastic
  - *From: MilesCorban*

- **Inpainting replaces rather than removes**
  - Inpainting tends to replace objects with other things rather than cleanly removing them
  - *From: Johnjohn7855*

- **VACE not trained on normal maps**
  - Can work to some extent but doesn't understand them as proper normal maps
  - *From: Kijai*

- **Reactor causes jitter around facial features**
  - Particularly around eyes and mouth, affects ornaments around face
  - *From: Johnjohn7855*

- **ATI spline editor can't handle very fast movements**
  - Too fast movements cause the system to stop working properly
  - *From: Mngbg*

- **Model primarily trained on realistic images**
  - Works less well with stylized or cartoon content
  - *From: Mngbg*

- **VACE requires controlled scenarios for optimal results**
  - Works best with people in stable environments rather than extreme motion scenarios at high speeds
  - *From: chrisd0073*

- **FaceFusion licensing restrictions**
  - Mostly non-commercial licensing limits commercial use
  - *From: chrisd0073*

- **Model produces green artifacts when trajectory tracking fails**
  - When insufficient trajectory points provided or tracking is lost, model fills gaps with green coloring
  - *From: Kijai*


## Hardware Requirements

- **RTX 5090 performance**
  - 5-7 minutes for 81 frames at 768x768 with 30 steps, max 21-24GB VRAM usage
  - *From: VRGameDevGirl84(RTX 5090)*

- **RTX 4090 vs 5090 speed**
  - 5090 about 40% faster or more if you can utilize memory over offloading
  - *From: Kijai*

- **RTX 4090 performance**
  - 4:08 for 640x480 @ 81 frames with Q8 GGUF, under 5 min for 1024x512
  - *From: MilesCorban*

- **Fun Control 14B timing**
  - 1.3B takes 02:30, 14B takes 15:30 on RTX 6000 Ada
  - *From: Nathan Shipley*

- **5090 power issues**
  - Can spike over 600w, avoid splitter cables that come in box
  - *From: ingi // SYSTMS*

- **720p Fun Control on RTX 4080**
  - Very slow, no OOM with 40 blocks at 720p but takes too much time
  - *From: N0NSens*

- **LoRA training time on 4090**
  - Takes about 1 hour for 1.3B LoRA training using ai-toolkit
  - *From: Jas*

- **1001 frame generation possible with ex LoRA**
  - Long generation achievable using extension LoRA with context windowing
  - *From: Flipping Sigmas*

- **VRAM for 4080**
  - 3:50 generation time for video, can handle various Wan models
  - *From: N0NSens*

- **RTX 3090 FP8 limitation**
  - FP8 not supported, must use fp8_e5m2 or disable FP8 entirely
  - *From: Kijai*

- **4070 VRAM**
  - 12GB VRAM recognized correctly, sufficient for basic operations
  - *From: Boop*

- **Ubuntu version compatibility**
  - 22.04 recommended over 24.04 for CUDA toolkit compatibility
  - *From: UsamaAhmedKhan*

- **VRAM for 81 frames at various resolutions**
  - 24GB VRAM handles 1024x576, 16GB can do 832x480 at 720p/81fr
  - *From: N0NSens*

- **RAM for TeaCache**
  - 32GB RAM minimum, issues occur with non_blocking=True. 128GB recommended for large models
  - *From: Kijai*

- **Generation speed reference**
  - 3090: 3 minutes for 81 frames with VACE, 3090 Ti taking 14+ minutes indicates optimization issues
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Runpod container disk space**
  - Default 20GB too small, recommend 80-100GB container disk for ComfyUI
  - *From: chrisd0073*

- **CausVid 14B VRAM**
  - 4060ti can run 193 frames in 2-5 minutes at 832x480
  - *From: Vérole*

- **CausVid requires torch.compile**
  - Out of memory without it even on small inputs
  - *From: Kijai*

- **Regular Wan 14B**
  - 1001 frames takes 41 minutes on 4090
  - *From: Flipping Sigmas*

- **MoviiGen VRAM**
  - Same as normal 14B base model, just a finetune
  - *From: Kijai*

- **MoviiGen system RAM**
  - Need lots of system RAM to hold and convert the large model
  - *From: Draken*

- **LTX 13B**
  - Can do 97 frames FHD on 24GB GPU using all VRAM
  - *From: David Snow*

- **Kijai's setup**
  - Has 128GB RAM and 1gbps internet
  - *From: ZeusZeus (RTX 4090)*

- **14B + VACE VRAM usage**
  - Challenging to run on 16GB VRAM, successfully run on 12GB 4070 with optimizations
  - *From: DawnII*

- **VACE 14B performance**
  - 10-20% slower than base 14B when using TeaCache
  - *From: DawnII*

- **Causvid VACE timing**
  - 4 steps in 2:46 on unspecified hardware
  - *From: DawnII*

- **VACE 14B VRAM usage**
  - Max 17.738 GB allocated with 20 blocks swapped on RTX 4090, 85 frames at 720x720
  - *From: Kijai*

- **RTX 4080 16GB limitations**
  - Needs 8 blocks swapped for VACE 14B, VRAM at 99% usage
  - *From: Nokai*

- **Generation speed**
  - RTX 4090: ~300 seconds, RTX 4070: ~500 seconds per step
  - *From: David Snow*

- **VRAM for 14B VACE**
  - User getting OOM even with 48GB, 24GB 3090Ti should work with proper block swap settings
  - *From: Shubhooooo*

- **CausVid LoRA generation time**
  - 1280x720, 69 frames, 4 steps takes ~2 minutes, max allocated 14.763GB VRAM
  - *From: Kijai*

- **Fast generation with CausVid LoRA**
  - 4 steps, 41 seconds generation time, 5 second videos in under a minute total
  - *From: Nokai*

- **RTX 3090 performance**
  - 1mn30 for 832x480x81 frames with CausVid, needs fp8 quantization and block swap
  - *From: ˗ˏˋ⚡ˎˊ-*

- **System RAM for 14B model**
  - 32GB RAM insufficient for smooth prompt changes, causes 5-minute freezes
  - *From: Draken*

- **VRAM for 14B model**
  - Manageable on 4090 at 480p, incredibly slow at 720p
  - *From: Kijai*

- **5090 performance**
  - 40 minutes for VACE processing, much more capable for standard workflows
  - *From: Piblarg*

- **VRAM usage**
  - 2 seconds to generate 81 frames at 1.3B with CausVid, 17 seconds for different test
  - *From: Kijai*

- **Memory management**
  - VAE decoding takes longer than generation time
  - *From: Kijai*

- **Performance timing**
  - 162 frames in 233 seconds, 129.86 seconds for 81 frames at 576x1024
  - *From: A.I.Warper*

- **VRAM for VACE 14B + CausVid**
  - Can run on 16GB VRAM with proper block swapping (20 blocks), 4060Ti 16GB works with fp8 quants and block swap 30
  - *From: N0NSens*

- **RAM requirements**
  - 32GB RAM may not be sufficient, 64GB recommended for comfortable operation, especially with 24GB VRAM systems
  - *From: Captain of the Dishwasher*

- **Performance at 832x480**
  - 97 frames at 832x480 with 4 steps takes ~1:18 on 16GB VRAM system, 121 frames takes ~17:47
  - *From: N0NSens*

- **Max batch size**
  - 81 frames at 1024x576 max for single batch, 41 frames at 720p also works
  - *From: A.I.Warper*

- **CausVid 1.3B performance**
  - 4070Ti: 56 seconds for 1280x720x81 frames
  - *From: DiXiao*

- **CausVid speed comparison**
  - 3090: 45sec for 1.3B vs 1:30 for 14B, same content
  - *From: ˗ˏˋ⚡ˎˊ-*

- **14B VRAM with block swap**
  - 16GB should work with 40 block swap + 5 for VACE
  - *From: DiXiao*

- **5090D performance**
  - 10-35 seconds for various resolutions with CausVid
  - *From: slmonker(5090D 32GB)*

- **VRAM usage with optimizations**
  - 720x720x81f with Q8_0 uses max 8.7GB VRAM on 4070ti with distorch, completes in 115-164 seconds
  - *From: The Punisher*

- **RAM requirements for VACE 14B**
  - 24GB VRAM + 32GB RAM user had issues, fixed by adding 8GB swap memory
  - *From: Captain of the Dishwasher*

- **1.3B generation speed**
  - 40 seconds for 81 frames at ~960x420 on RTX 3090
  - *From: ˗ˏˋ⚡ˎˊ-*

- **VRAM usage with GGUF Q5_K_S**
  - 10.272GB VRAM for 720x720x81f with distorch optimization
  - *From: The Punisher*

- **Q5_K_S works on 12GB VRAM**
  - Confirmed working configuration for mid-range GPUs
  - *From: The Punisher*

- **14B model issues on 4090**
  - Consistent problems running 14B VACE on RTX 4090, memory management issues
  - *From: David Snow*

- **System RAM important for model loading**
  - Models shuttled to system RAM before VRAM, insufficient RAM causes disk paging
  - *From: MilesCorban*

- **4080 16GB performance**
  - 832x464 24fps 73frames 8step: 267.57s total, 29.41s/it, 62GB RAM usage
  - *From: CaptHook*

- **Native VACE OOM issues**
  - 24GB VRAM + 64GB RAM still limited to 320x320x49, offloading not effective
  - *From: TK_999*

- **14B model VRAM needs**
  - 12GB can work with tiled VAE and RAM offloading, 16GB+ recommended, needs lots of RAM
  - *From: Kijai*

- **162 frames generation**
  - Takes 8 minutes on RTX 3090, uses max 17.6GB VRAM, 20.3GB reserved
  - *From: ˗ˏˋ⚡ˎˊ-*

- **81 frames at 1280x704**
  - Uses 26.6GB max allocated memory on RTX 5090
  - *From: VRGameDevGirl84(RTX 5090)*

- **CausVid memory usage**
  - Only uses memory for 3 latents worth plus KV cache
  - *From: Kijai*

- **MoviiGen generation time**
  - 22 minutes for 1280x720 generation
  - *From: ArtOfficial*

- **14B model performance on RTX 3090 24GB**
  - 238 seconds for 121 frames at 960x544, 146 seconds for 832x480, requires 40 block swap
  - *From: N0NSens*

- **LoRA memory usage**
  - Each LoRA adds approximately 200MB of VRAM
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Recommended specs for workflows**
  - RTX 3090 with 64GB RAM works well for 14B models with proper block swapping
  - *From: BestWind*

- **RTX 3090 VRAM usage**
  - 21.455 GB max allocated for 125 frames at 1024x576 with 5 steps, 268 seconds generation time
  - *From: VRGameDevGirl84(RTX 5090)*

- **RTX 3090 with CausVid**
  - 8.278 GB max allocated, 10.969 GB reserved for 85 frames at 480x832 with 4 steps, 183 seconds
  - *From: Jemmo*

- **Block swap memory usage**
  - 13484.13MB on CPU, 1926.30MB on GPU, 15410.43MB total for transformer blocks
  - *From: N0NSens*

- **DepthCrafter VRAM requirements**
  - Too much VRAM for RTX 3090, use DepthAnything instead
  - *From: BestWind*

- **VACE fits in 16GB VRAM**
  - Can run on 12GB, 16GB confirmed working
  - *From: Boop*

- **CausVid + Fantasy Talking VRAM usage**
  - Max allocated: 21.382 GB, Max reserved: 23.031 GB for 81 frames at 720x720
  - *From: VRGameDevGirl84(RTX 5090)*

- **3090 compatibility confirmed**
  - Face replacement and VACE workflows work on RTX 3090
  - *From: BestWind*

- **Long video generation RAM usage**
  - 401 frames generation used 105GB RAM with context
  - *From: ˗ˏˋ⚡ˎˊ-*

- **VACE 14B VRAM with block swapping**
  - 14B model runs on RTX 3090 24GB with 128GB RAM using block swapping (40 base blocks, 5 VACE blocks)
  - *From: sneako1234*

- **FP16 model on RTX 5090**
  - FP16 14B model with FP8 quantization uses ~88% VRAM on RTX 5090 with no block swapping
  - *From: ingi // SYSTMS*

- **FP32 precision performance**
  - FP32 precision took nearly an hour for 49 frames at 1280x720 but gave insane quality
  - *From: ingi // SYSTMS*

- **VACE 14B VRAM usage**
  - Can run on 12GB VRAM with block swapping (40 and 5 blocks)
  - *From: sneako1234*

- **Generation times with optimizations**
  - With SLG: 8-12 minutes, without optimizations: 16 minutes on unspecified hardware
  - *From: ˗ˏˋ⚡ˎˊ-*

- **5090 generation time**
  - 15 minutes for full generation with default context settings
  - *From: 852話 (hakoniwa)*

- **TeaCache speed improvement**
  - 382s vs 203s (47% faster) with coefficient-disabled TeaCache on VACE 14B CausVid
  - *From: David Snow*

- **VRAM usage with VACE + 14B + CausVid**
  - Can overload 16GB VRAM and 64GB RAM even with 20-30 blocks
  - *From: N0NSens*

- **Memory usage with TeaCache**
  - TeaCache adds VRAM usage as trade-off for speed, not recommended with CausVid
  - *From: Cubey*

- **High memory usage with VACE**
  - 128GB RAM and 24GB VRAM both nearly maxed out during generation
  - *From: Valle*

- **VRAM usage for TeaCache**
  - TeaCache was using ~750MB unnecessary VRAM at 1280x780 resolution before optimization fix
  - *From: Kijai*

- **CausVid speed improvement**
  - CausVid at 1280x780 reduced generation time from 30 minutes to 4 minutes
  - *From: boorayjenkins*

- **RTX 4090 can handle 240 frames with CausVid LoRA**
  - Using 14B model, significant improvement over previous capabilities
  - *From: Cubey*

- **Context windows don't increase VRAM usage**
  - Uses same memory as single 81-frame generation regardless of total length
  - *From: Kijai*

- **RTX 5090 performance**
  - 640x960 81 frames in 57 seconds, 544x832 501 frames possible with fp8 and no block swapping
  - *From: seitanism*

- **RTX 3090 performance**
  - 960x544 takes 20 minutes, much slower than newer cards
  - *From: ˗ˏˋ⚡ˎˊ-*

- **RTX 5080 performance**
  - 832x480 VACE 81 frames, 4 steps, no CausVid takes 13 minutes, with CausVid only 6 minutes
  - *From: VK (5080 128gb)*

- **RTX 4080 capacity**
  - 864x480 121f or 960x544 73f (97f OOM) with blocks 40/7
  - *From: CaptHook*

- **Memory usage at high resolution**
  - 1280x720 85 frames uses max 18.745 GB allocated, 21.250 GB reserved
  - *From: AJO*

- **RTX 5090 VRAM usage**
  - Requires VAE tiling at max resolution to prevent crashes
  - *From: AJO*

- **4070 performance**
  - 50 s/it at 768x512 resolution with CausVid, around 3s/it for second pass refinement
  - *From: Boop*

- **H100 capability**
  - User with H100s interested in running 14B VACE + WAN models
  - *From: Christian Sandor*

- **VRAM for higher resolutions**
  - 576x1024 at 85 frames with 4 steps takes 2:39, max allocated 10.090 GB on 14B model
  - *From: A.I.Warper*

- **Block swapping for 4090**
  - Need block swapping value of 30 for 4090 24GB to avoid OOM with higher resolutions
  - *From: VRGameDevGirl84(RTX 5090)*

- **GGUF loading with limited VRAM**
  - Can load Q8 16GB wan with 12GB VRAM without issues using distorch for offloading
  - *From: The Punisher*

- **Performance at reduced resolution**
  - 864x480 121f 24fps 6steps = 8.27m on RTX 4080 16gb
  - *From: CaptHook*

- **Memory limits on cloud platforms**
  - Users hitting device and disk limits on RunPod with 41GB VRAM RTX 4090, 100GB volume when running 14B fp16 model
  - *From: stas*

- **VRAM management for ControlNet preprocessing**
  - ControlNet preprocessors consume significant VRAM and don't release it properly, causing OOM issues
  - *From: MilesCorban*

- **1024x1200 resolution processing time**
  - Can process 1024x1200 resolution in under 3 minutes on appropriate hardware
  - *From: Thom293*

- **VRAM for 720p generation**
  - 160 frames at 720p before hitting VRAM limits on high-end cards
  - *From: Gateway {Dreaming Computers}*

- **System RAM for longer videos**
  - 128GB system RAM allows 300-450 frames with shared virtual GPU memory on A5000 24GB
  - *From: Guey.KhalaMari*

- **A100 80GB VRAM usage**
  - May run out of system RAM due to offloading, needs sufficient RAM allocation
  - *From: sneako1234*

- **5090 performance with CausVid**
  - 85 frames at 1024x576 in 150 seconds with strength 1.0 and 4 steps
  - *From: VRGameDevGirl84(RTX 5090)*

- **Higher resolution rendering for quality**
  - Used A6000 on RunPod to render 1280x720 for better results with wide shots
  - *From: traxxas25*

- **VRAM usage with TeaCache and CausVid**
  - TeaCache takes up more VRAM and slows inference when used with CausVid
  - *From: Cubey*

- **14B model VRAM usage**
  - Kills PC without quantization, 96GB RAM user still hitting limits
  - *From: David Snow*

- **RAM usage with Wan**
  - Framepack can use 50GB RAM while model is only 16GB, 128GB gets full
  - *From: AR*

- **2060 with 64GB RAM**
  - Can run 14B Wan using ComfyUI offloading to RAM
  - *From: hicho*

- **4090 performance**
  - 163 frames in 20 minutes for 14B vs 5 minutes for 1.3B
  - *From: VK (5080 128gb)*

- **RTX 6000 Blackwell**
  - 96GB VRAM, 2x faster than RTX4090
  - *From: Tytanick*

- **4090 with 128GB RAM**
  - Confirmed working setup for VACE 14B workflows
  - *From: Ruairi Robinson*

- **Higher resolution memory usage**
  - 1280x720 resolution causes system to struggle even with 4090/128GB
  - *From: Ruairi Robinson*

- **VRAM management for lower-end GPUs**
  - 2060 6GB can offload to 64GB RAM using vram_management setting of 1
  - *From: hicho*

- **WSL2 memory allocation**
  - Need proper .wslconfig setup for WSL2 to avoid out of memory errors
  - *From: jerms_ai_(4090_24g)*

- **14B model with quantization**
  - For 4090 24GB, should enable quantization and block swap for 14B models. Can do 1280x720x81 on fp16 without quant when swapping all blocks with 128GB RAM
  - *From: Kijai*

- **4070 12GB recommendations**
  - Should use 1.3B VACE models or Q5 GGUF. 14B models may work with native but will test system limits. 32GB RAM helpful
  - *From: David Snow*

- **Memory management**
  - Use fp8 models with fp16 node settings, avoid bf16 for memory issues. Block swap not needed until allocation errors occur
  - *From: hicho*

- **RTX 5070 vs 5070 Ti performance**
  - 5070 gets Flux image in 9 seconds, 5070 Ti in 7 seconds. 5070 essentially 3090 with 12GB VRAM
  - *From: VK (5080 128gb)*

- **VACE 161 frames**
  - Possible on RTX 5090 with 32GB RAM without degradation
  - *From: Piblarg*

- **Wan I2V vs VACE memory**
  - User can run Wan I2V 14B 480p Q8 but not VACE 14B Q8
  - *From: Boop*

- **Multi-GPU setup**
  - User has 48GB VRAM across two RTX 3090 cards
  - *From: SegmentationFault*

- **VRAM management**
  - Keep VRAM usage at 96-98% for optimal performance. 99% usage makes generation very slow. Use block swapping for OOM issues
  - *From: N0NSens*

- **System RAM for block swapping**
  - 64GB+ RAM essential if swapping all blocks (40 and 15) to avoid VRAM OOM
  - *From: JohnDopamine*

- **Performance examples**
  - RTX 5090: 321 frames at 960x576, 5 steps in 616 seconds. RTX 3090: 81 frames, 4 steps in 500 seconds. RTX 4090: 720p 81 frames in 229 seconds
  - *From: VRGameDevGirl84(RTX 5090), Valle, slmonker(5090D 32GB)*

- **Phantom 14B performance**
  - Very slow, estimated 30+ minutes on 4090, 2/40 steps taking 89.10s each
  - *From: Kijai*

- **RTX Pro 6000 performance**
  - 96GB VRAM, torch.compile doesn't work, not 2x faster than 5090
  - *From: aikitoria*

- **TeaCache optimization**
  - Can be enabled from step 6 to speed up generation
  - *From: Kijai*

- **VRAM usage Phantom 89 frames 1280x768**
  - Max allocated: 13.303 GB, Max reserved: 19.250 GB
  - *From: Kijai*

- **VRAM usage CausVid 89 frames 1280x720**
  - Max allocated: 21.446 GB, Max reserved: 27.188 GB
  - *From: Kijai*

- **Performance RTX 4090**
  - Phantom 1024x576 89 frames 6 steps: 119.92 seconds
  - *From: JohnDopamine*

- **Performance comparison 480p vs 720p**
  - 480p: 413.80 seconds vs 1375.69 seconds for higher resolution on RTX Pro 6000
  - *From: aikitoria*

- **Phantom VRAM usage**
  - Max allocated 12.836 GB, max reserved 13.875 GB for generation
  - *From: JohnDopamine*

- **Phantom speed**
  - ~55 seconds/step at 832x480 with 40 steps on fp16 14B with flash_attn2
  - *From: hau*

- **Merged model performance**
  - 133 seconds total for generation without SageAttention
  - *From: Thom293*

- **4080 16GB performance**
  - 1024x576 16fps 8steps = 8.5min generation time, 1280x720 causes OOM
  - *From: CaptHook*

- **4070ti performance**
  - 480p 81fps generation in just two minutes
  - *From: MaQue*

- **RTX 6000 Pro vs 4090**
  - RTX 6000 Pro about double the speed of 4090 on wan, also has 96GB VRAM
  - *From: aikitoria*

- **Generation speed with 14B**
  - ~16s/step at 7 steps reported
  - *From: hau*

- **Phantom generation time**
  - 1280x720 completed in 262 seconds
  - *From: Thom293*

- **VRAM for 1024x576**
  - 24GB VRAM user experiencing OOM at 1024x576 with combo model
  - *From: The Shadow (NYC)*

- **VACE processing time**
  - 189 frame shots at 1280x720 take 26-30 minutes on RTX 4090
  - *From: Ruairi Robinson*

- **Temperature monitoring**
  - 76 degrees on RTX 3090ti should be fine, not causing crashes
  - *From: Kijai*

- **Phantom 14B VRAM usage**
  - 89 frames at 1024x576 with 8 steps: Max allocated 22.296 GB, Max reserved 24.500 GB, completed in 188.08 seconds
  - *From: VRGameDevGirl84(RTX 5090)*

- **Uni3C performance on 3090**
  - Taking 277 s/it at 480p, 25 frames - significantly slow
  - *From: sneako1234*

- **VRAM usage optimization**
  - Should adjust block swap until reaching 95% VRAM usage for optimal performance
  - *From: Kijai*

- **Video enhancement speed**
  - 1280x720 video enhancement with LoRA completed in 90.50 seconds using CausVid on RTX 5090
  - *From: VRGameDevGirl84(RTX 5090)*

- **Frame limitations for RTX 2060**
  - 81 frames at 720p causes issues on RTX 2060, requiring restart and reduction of resolution and frames
  - *From: hicho*

- **Windows VRAM monitoring limitations**
  - nvtop not available for Windows, nvitop limited to total VRAM usage, can't show process-specific usage
  - *From: Kijai*

- **Phantom 14B generation time**
  - 25 minutes for 1x832x480 at 40 steps on RTX 4090
  - *From: Janosch Simon*

- **Character LoRA training on Wan T2V 14B**
  - 20 images dataset, ~40 minutes training time, requires 32GB VRAM
  - *From: DeZoomer*

- **WSL RAM allocation issues**
  - WSL would only use a percentage of system RAM and would start swapping way before it needed to
  - *From: MilesCorban*

- **Loading transformer parameters slow on WSL**
  - Loading transformer parameters to cpu taking 8+ minutes on WSL vs instant on other systems
  - *From: mamad8*

- **VRAM for batch processing**
  - 768x480 resolution, 8 steps, batch prompts took 335.75 seconds on RTX 5090
  - *From: VRGameDevGirl84(RTX 5090)*

- **Speed comparison**
  - 5 scenes, 81 frames, 8 steps took 300 seconds
  - *From: AJO*

- **FP8 performance boost**
  - FP8 quantization provides roughly half the generation time vs FP16
  - *From: AJO*

- **VRAM for 1024x576, 45 frames**
  - Max allocated: 18.113 GB, Max reserved: 18.750 GB, 48.60 seconds
  - *From: VRGameDevGirl84(RTX 5090)*

- **VRAM for 1024x576, 85 frames**
  - Max allocated: 21.914 GB, Max reserved: 23.062 GB, 103.29 seconds
  - *From: VRGameDevGirl84(RTX 5090)*

- **VRAM for 1280x720, 85 frames with block swapping**
  - Max allocated: 25.309 GB, Max reserved: 26.969 GB, 217.20 seconds with 5 blocks swapped
  - *From: VRGameDevGirl84(RTX 5090)*

- **VRAM for Wan VAE**
  - 24GB sufficient, never requires tiling
  - *From: Kijai*

- **RAM for model offloading**
  - Insufficient system RAM causes OOM when using CausVid LoRa
  - *From: TK_999*

- **nvfp4 support**
  - Only available on Blackwell (5090) and up, not useful for 4xxx series
  - *From: aikitoria*

- **Film grain node VRAM usage**
  - Takes up significant VRAM for unknown reasons
  - *From: Johnjohn7855*

- **RTX 3000 series compatibility issue**
  - Fp8_e4m3fn format doesn't work with compile on RTX 3000 series GPUs, need to use fp8_e5m2 instead
  - *From: Kijai*

- **RTX 8000 compatibility question**
  - User asking about running Wan 2.1 and VACE on RTX 8000 with 48GB each in dual GPU NVLinked setup
  - *From: Ruairi Robinson*


## Community Creations

- **Python 3D camera control app** (tool)
  - Mouse movement through 3D space with WASD keys like FPS game to create camera movements
  - *From: VRGameDevGirl84(RTX 5090)*

- **CbrPnK style LoRA** (lora)
  - Custom style LoRA trained for 14000 steps with trigger 'cbrpnk style'
  - *From: JohnDopamine*

- **Two-pass v2v workflow** (workflow)
  - Workflow for strong stylization using two samplers with 3+4 step split for better LoRA effects
  - *From: David Snow*

- **CyberPop LoRA** (lora)
  - Style LoRA based on latentpop mixed with other LoRAs, trigger 'cbrpnk style', better as v2v LoRA due to 1.3B limitations
  - *From: David Snow*

- **FP8 quantized Fun v1.1 InP** (model)
  - Community member created FP8 version of 47GB Fun v1.1 model
  - *From: JmySff*

- **NormalCrafter ComfyUI node** (node)
  - Node implementation for NormalCrafter normal map generation
  - *From: A.I.Warper*

- **Long form video workflow** (workflow)
  - Corrected workflow for extended video generation
  - *From: Flipping Sigmas*

- **NormalCrafter ComfyUI Wrapper** (node)
  - Wrapper for NormalCrafter to generate normal maps from video
  - *From: A.I.Warper*

- **Multiple military vehicle LoRAs** (lora)
  - Tiger Tank, T34, Sherman, Mi-24, AH-64, KA-52 LoRAs for Wan 2.1
  - *From: MisterMango*

- **FLF2V workflow with character consistency** (workflow)
  - Uses Redux+Fill+ControlNet+InstantID for consistent character generation
  - *From: slmonker(5090D 32GB)*

- **Custom frame removal node** (node)
  - Removes first N frames from video output
  - *From: Vérole*

- **WanVideoWrapper** (wrapper)
  - ComfyUI wrapper for Wan models by Kijai
  - *From: Kijai*

- **Tank LoRAs series** (lora)
  - German Panther, Pz.IV H, M18 Hellcat tank models
  - *From: MisterMango*

- **Fruitiger LoRA** (lora)
  - Works with MoviiGen model
  - *From: Dream Making*

- **Model conversion script** (tool)
  - Combines multipart models into single safetensors and saves to fp16
  - *From: Juampab12*

- **CausVid LoRA extraction** (lora)
  - Extracted CausVid as LoRA for use with base T2V 14B model, took 30 minutes to extract
  - *From: Kijai*

- **Blender relighting setup** (workflow)
  - Simple relighting using normals test with NormalCrafter and IC-Light
  - *From: David Snow*

- **CausVid LoRA conversion** (lora)
  - Converted CausVid distillation model to LoRA format for compatibility
  - *From: Kijai*

- **Block edit node for CausVid** (node)
  - Node to skip specific blocks when applying CausVid LoRA
  - *From: seruva19*

- **WanVideoWrapper updates** (node)
  - Updated example workflows and outpainting fixes
  - *From: Kijai*

- **CausVid LoRA extraction** (lora)
  - Extracted CausVid models as LoRAs for better VACE compatibility
  - *From: Kijai*

- **WanVideoWrapper updates** (node)
  - Removed blocks option from VACE loader node, improved compatibility
  - *From: Kijai*

- **Juxtapoz fluxtapoz nodes fork** (node)
  - Forked nodes for use with HiDream and RF_inversion
  - *From: A.I.Warper*

- **Clean VRAM Used node** (node)
  - From comfyui easy used, works for preventing OOMs between generations
  - *From: The Punisher*

- **VACE 14B GGUF quantizations** (model)
  - Q3_K_S, Q8_0, Q4_K_S, Q5_K_S quantized versions of VACE 14B module
  - *From: The Punisher*

- **Installation scripts for Windows portable** (tool)
  - One-click installers for CUDA 12.8, Triton, Sage attention, xformers, and torch 2.8 dev
  - *From: The Punisher*

- **VACE 14B GGUF models** (model)
  - Q3_K_S, Q5_K_S, Q6 quantized versions of VACE 14B for native ComfyUI
  - *From: The Punisher*

- **Second pass cleanup workflow** (workflow)
  - Two-stage process using 14B for generation and 1.3B for cleanup
  - *From: David Snow*

- **Custom sampler with advanced options** (node)
  - Sampler with eta, bongmath, steps control, and scheduler options
  - *From: Clownshark Batwing*

- **VACE workflow for low VRAM** (workflow)
  - Working VACE setup for GGUF models on low VRAM systems
  - *From: The Punisher*

- **Style guide video workflow** (workflow)
  - System for using one video as style reference for another
  - *From: Clownshark Batwing*

- **Flux + VACE workflow** (workflow)
  - Automated pipeline that generates reference image from video first frame using Flux, then processes with VACE
  - *From: VRGameDevGirl84(RTX 5090)*

- **CausVid 14B support** (lora)
  - Extended CausVid to support Wan2.1-14B model with 9-step distillation
  - *From: aipmaster*

- **Face replacement workflow** (workflow)
  - Replace face of character with any reference using VACE
  - *From: BestWind*

- **Combined depth+pose VACE workflow** (workflow)
  - Uses separate VACE embeds for depth and pose with blend controls
  - *From: VRGameDevGirl84(RTX 5090)*

- **Fantasy Talking + CausVid workflow** (workflow)
  - Fast lip-sync generation using CausVid LoRA
  - *From: VRGameDevGirl84(RTX 5090)*

- **Character LoRAs for 14B model** (lora)
  - Multiple LoRAs trained on David Snow's image set for 14B model, various epochs available
  - *From: JohnDopamine*

- **VACE model patching code** (tool)
  - Code to add VACE patch to standard WAN models, though still missing 30 layers and config issues
  - *From: The Punisher*

- **Native VACE module support** (node)
  - Native ComfyUI implementation of VACE modules, works but needs GGUF and Sage attention fixes
  - *From: The Punisher*

- **WAN prompt generator** (tool)
  - Gemini-generated prompt templates for WAN models, works with various LLMs
  - *From: aipmaster*

- **DetailZ LoRA for WAN** (lora)
  - Detail enhancer specifically trained for WAN models, adds additional detail to outputs
  - *From: David Snow*

- **Custom GGUF DistORCH loader** (node)
  - Custom implementation for GGUF compatibility with VACE
  - *From: The Punisher*

- **Custom safetensors node for WAN** (node)
  - Works with safetensors (1.3b version) but not GGUFs yet
  - *From: The Punisher*

- **Double VACE workflow** (workflow)
  - Workflow using two VACE encode nodes with depth and pose controls for better character animation
  - *From: slmonker(5090D 32GB)*

- **Video inpainting workflow** (workflow)
  - 500+ frame video face replacement workflow being developed
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Custom VACE GPT** (tool)
  - GPT trained on VACE/WAN documentation to guide users through setup, prompts, and troubleshooting
  - *From: AJO*

- **Color consistency LoRA** (lora)
  - LoRA trained for color and contrast consistency across multiple generations
  - *From: Mads Hagbarth Damsbo*

- **Headless Wan2GP** (tool)
  - Headless fork of deepmeepbeeps VRAM efficient Wan repo - one command setup
  - *From: pom*

- **Relative head motion node** (node)
  - Custom node for stabilized view with head rotations - combines pose of heads with relative movement from first frame
  - *From: Mads Hagbarth Damsbo*

- **Updated torch.compile node** (node)
  - Updated compile node to use ComfyUI core wrapper, works with LoRAs without special patching
  - *From: Kijai*

- **VACE custom node for native** (node)
  - Custom node to make VACE work with native ComfyUI
  - *From: The Punisher*

- **WanVideo CFG Schedule node** (node)
  - Node for dynamically changing CFG during generation
  - *From: Kijai*

- **VACE GGUF models** (model)
  - GGUF versions of VACE models that work in native without custom nodes
  - *From: The Punisher*

- **Boolean invert node for automated stacking** (node)
  - Simple custom node that automatically determines stacking based on whether image is vertical or horizontal
  - *From: Valle*

- **Scipy-based parameter optimization node** (node)
  - Uses Scipy methods for more efficient parameter testing than grid search or random search
  - *From: deleted_user_2ca1923442ba*

- **FaceReference node** (node)
  - Custom node attempting to replace LivePortrait functionality for face reference, currently in development with NC licensing issues
  - *From: Mads Hagbarth Damsbo*

- **ControlNet + Masking workflow** (workflow)
  - Workflow that processes video input to generate pose, depth, canny, MediaPipe face controls and subject masks using Segment Anything v2
  - *From: Gateway {Dreaming Computers}*

- **Video extension workflow with color matching** (workflow)
  - Complex workflow for extending videos with overlapping frames and color correction
  - *From: ArtOfficial*

- **Get image or mask from batch method** (workflow)
  - Simplified approach to video extension without reloading compressed video
  - *From: zelgo_*

- **ComfyUI Pose Interpolation** (node)
  - Node for creating smooth pose transitions between different poses
  - *From: toyxyz*

- **Flux Redux with PuLID workflow** (workflow)
  - Comprehensive Flux workflow including Redux, PuLID, face detailer and upscaler for character concept creation
  - *From: Gateway {Dreaming Computers}*

- **Auto face masking workflow nodes** (workflow)
  - Embedded workflow nodes for automatic face masking in video processing
  - *From: VRGameDevGirl84(RTX 5090)*

- **Modified pose interpolation** (tool)
  - Controls timing of pose appearance with body shape correction
  - *From: toyxyz*

- **Overlapping batch video system** (workflow)
  - Breaks reference video into batches with overlaps for arbitrary length videos
  - *From: notid*

- **Seamless looping workflow** (workflow)
  - Processes generated video to create perfect loops
  - *From: The Shadow (NYC)*

- **TrimVideoLatent node** (node)
  - Node for removing frames from video latents
  - *From: Guey.KhalaMari*

- **Dynamic block swap system** (workflow)
  - Conditional nodes based on pixel counts with thresholds for different block swap amounts
  - *From: DevouredBeef*

- **Custom node for last frame reference** (node)
  - Grabs most recent PNG from output folder and saves last frame from output video for next batch reference
  - *From: VRGameDevGirl84(RTX 5090)*

- **AccVideo LoRA extraction** (lora)
  - Kijai working on extracting LoRA from AccVideo model
  - *From: Kijai*

- **Comprehensive workflow package** (workflow)
  - CN extraction, Flux with Redux/depth/PuLID, and Wan VACE/CausVid workflows
  - *From: Gateway {Dreaming Computers}*

- **Toon style LoRA for Wan 14B** (lora)
  - Trained with 60 images on CivitAI, works effectively with Wan 14B T2V
  - *From: VRGameDevGirl84(RTX 5090)*

- **AccVid LoRA extraction** (lora)
  - Extracted AccVid LoRA from the model for use in workflows
  - *From: Kijai*

- **VACE workflow with multiple inputs** (workflow)
  - Single VACE encode using expanded mask, depth, normals and pose together
  - *From: David Snow*

- **Merged CausVid + AccVid Model** (model)
  - Combined LoRA merge using Claude-assisted tool, fp16 format, no separate LoRA needed
  - *From: JohnDopamine*

- **OpenPose Body Editor** (tool)
  - Tool for scaling skeleton proportions for character adaptation
  - *From: toyxyz*

- **CausVid/AccVid/Phantom merge** (model)
  - Merged model combining CausVid, AccVid and Phantom for faster inference
  - *From: JohnDopamine*

- **Cinematic LoRA** (lora)
  - Acts more as a detailer, works with VACE at strengths 1.5-2.0
  - *From: VRGameDevGirl84(RTX 5090)*

- **DWPose scaler node** (node)
  - Single node for scaling DWPose output
  - *From: A.I.Warper*

- **Phantom model merge** (model)
  - Merge of fp16 phantom model with accvid and causvid LoRAs integrated
  - *From: JohnDopamine*

- **Cinematic model LoRA** (lora)
  - Cinematic model converted to LoRA format, can help reduce Phantom's animated tendency
  - *From: Juampab12*

- **Hakoniwa anime model** (model)
  - Adjusted model to give stronger anime style output
  - *From: 852話 (hakoniwa)*

- **Ultimate OpenPose Editor** (node)
  - Tool for editing OpenPose with automatic scaling based on target keypoints
  - *From: toyxyz*

- **Phantom custom merge** (model)
  - Faster Phantom model merged with CausVid and AccVid
  - *From: Johnjohn7855*

- **Native ComfyUI VACE implementation** (node)
  - Allows VACE to patch other models natively in ComfyUI lazy eval system
  - *From: Ablejones*

- **John Dopamine's Phantom merge** (model)
  - Faster version of Phantom model with improved inference speed
  - *From: JohnDopamine*

- **Arnold LoRA for Wan2.1** (lora)
  - Character LoRA trained for Arnold Schwarzenegger
  - *From: JohnDopamine*

- **Over-engineered face replacement workflow** (workflow)
  - Month-long project creating organized workflow for face replacement that works with any video regardless of face size
  - *From: DeZoomer*

- **GGUF quantizations of Phantom 14B** (model)
  - Q8 and other quantized versions of Phantom model
  - *From: The Punisher*

- **Merged Phantom + CausVid + AccVid model** (model)
  - All-in-one model with distillation built in for faster generation
  - *From: JohnDopamine*

- **Character LoRA training workflow** (workflow)
  - Local training with ai-toolkit using 20 images on Wan T2V 14B
  - *From: DeZoomer*

- **Open Pose Interpolation node update** (node)
  - Updated to allow for Pose Sequence input, can change body shape naturally
  - *From: toyxyz*

- **CFG Schedule node in WanVideoWrapper** (node)
  - Node for CFG scheduling with CausVid
  - *From: Ada*

- **CausVid LoRA variants** (lora)
  - Multiple pruned versions including attention layers only and first block disabled versions
  - *From: Kijai*

- **Face detailer node for videos** (node)
  - Detects faces, crops across all frames, reprocesses for detail enhancement
  - *From: mamad8*

- **LoRA merger workflow** (workflow)
  - ComfyUI nodes for merging multiple LoRAs into single model
  - *From: Thom293*

- **GGUF Phantom workflow** (workflow)
  - Native ComfyUI workflow for GPU-poor users to run high quality generations
  - *From: The Punisher*

- **2D Animation Effects LoRA** (lora)
  - Outputs 2D animation effects based on simple instruction videos made in After Effects, controllable drawing amount, can create water, waves, smoke, spray, flames, explosions through prompts
  - *From: 852話 (hakoniwa)*

- **Merged Phantom + CausVid V2 + detail LoRAs model** (model)
  - Combined model with Phantom, CausVid V2, MoviiGen, and detail enhancement LoRAs merged at strength 1.0
  - *From: VRGameDevGirl84(RTX 5090)*

- **Custom face cropping node** (node)
  - Crops faces in video so all faces have same size, created with LLM help
  - *From: mamad8*

- **ComfyUI-trained GPT** (tool)
  - GPT model trained on ComfyUI to help create custom nodes
  - *From: VRGameDevGirl84(RTX 5090)*
