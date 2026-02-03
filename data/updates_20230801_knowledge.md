# Updates Knowledge Base
*Extracted from Discord discussions: 2023-08-01 to 2026-02-01*


## Technical Discoveries

- **SDXL Motion Module beta released**
  - Can produce 1024x1024 16 frame videos, implemented into Comfy within hours by Kosinkadink
  - *From: pom*

- **Motion Scale control for fine-tuned motion**
  - Allows tuning up and down the amount of motion in output, combined with Motion LoRAs will provide extremely high degree of control
  - *From: pom*

- **SD2.1 CLIP encoding can influence SVD videos**
  - Can use SD2.1 CLIP encoding to influence Stable Video Diffusion output
  - *From: Kijai*

- **LCM LoRAs with AnimateDiff enable ultra-fast vid2vid**
  - Processed 2,467 frames in just 81 minutes with good quality results using LCM LoRAs with AnimateDiff multi-controlnet workflow
  - *From: CoffeeVectors*

- **Text to OpenPose skeleton generation**
  - Workflow that takes text and outputs Openpose skeletons, can be combined with vid2vid for complex motion more reliable than diffusion video models
  - *From: unknown user*

- **IPAdapter batch processing with unfold option**
  - Allows IPAdapter to process batches with Animatediff, unlocking many new possibilities
  - *From: matteo*

- **Controlnet timestep scheduling**
  - Allows determining which part of sampling process a controlnet should influence, helps fix weird artifacts
  - *From: Kosinkadink*

- **FreeInit and Noise Layers added to Comfy**
  - New capabilities added for improved video generation control
  - *From: Kosinkadink*

- **Sample Settings improvements in Comfy**
  - Enhanced sampling control options added
  - *From: Kosinkadink*

- **FaceID Portrait Models integrated**
  - Improved resemblance for portrait generation in various styles
  - *From: matteo*

- **Pseudo outline trick for better guidance**
  - Getting outline of subject instead of line drawings to avoid picking up too much detail on faces/costumes
  - *From: Draken*

- **Unsampling + RGB Video2Video workflow**
  - Process involving unsampling and SparseRGB for smooth video2video transformation with scarily good results
  - *From: whobody*

- **Motion LoRAs can guide motion with a range of precision from soft to hard**
  - Unlike vid2vid which tends to guide with hard precision, Motion LoRAs allow you to provide input videos and make motion 'a little bit like that' in combination with other inputs, giving more direction than highly specific guidance
  - *From: pom*

- **Motion LoRAs can stabilize animations and fix artifacts**
  - Can be used to fix/avoid artifacts in generations by providing good examples at low guidance, such as fixing normal realistic running
  - *From: pom*

- **Tiled IP Adapter works better on non-square images**
  - Solution to IP adapter issues with wider generations losing detail and causing artifacts, though still experimental
  - *From: pom*

- **IPA Tiling provides higher resolution view by breaking input image into components**
  - Breaks up input image into multiple components and feeds them in one-by-one so IPA has far higher resolution view, works in batches/with masks
  - *From: pom*

- **IPA Style Transfer for SDXL implemented**
  - Matteo added style transfer capability for SDXL models
  - *From: pom*

- **Depth maps can adjust movement layers for different motion levels**
  - Superbeast's workflow uses depth maps to adjust movement so different layers have different levels of motion
  - *From: pom*

- **Motion transplanting possible with MotionThief node**
  - Allows transplanting motion from one video onto AD generation
  - *From: logtd*

- **Style transfer implemented for SD1.5**
  - Can be used in Animatediff flows to fix style in particular place for consistent animations
  - *From: matt30*

- **Value scheduling for IPA strength**
  - Schedule animations for IPAs without masks, making it faster and less resource intensive
  - *From: matt30*

- **Motion Thief can use videos to control motion**
  - Videos can be used as motion control sources
  - *From: logtd*

- **Steerable Motion 1.4 supports unlimited frames**
  - Can now do unlimited frames thanks to Matt30's improvements
  - *From: ianiamwright*

- **Spline editor adds major UX improvements to Comfy**
  - Allows for many new possibilities in workflow creation
  - *From: kijai*

- **CameraCtrl enables granular camera motion control**
  - Adds ability to control camera motion granularly in generations
  - *From: kosinkadink*

- **Audioreactive dancing workflow**
  - Building on previous work, adds audio-reactive capabilities to dancing videos with potential for audio-reactive passes on generated videos
  - *From: cyncratic*

- **Vid2Vid upsampling achieves high consistency**
  - Achieves extremely high-consistency and close to no context issues even on HotShot
  - *From: Inner Reflections*

- **LivePortrait mapping approach for character expressions**
  - Mapping expressions onto video feels like a WAY better and more dynamic approach than portrait animation for story-telling
  - *From: pom*

- **Higher resolution Clip Vision using tiling**
  - Tiling Clip Vision to help it see images at higher resolution, catching additional detail and adding coherence to animations
  - *From: Matteo*

- **Cross Window Consistency improvements**
  - Implementing NaiveReuse and ContextRef and other context shift improving methods into ADE
  - *From: Kosinkadink*

- **CogVideoX vid2vid interprets motion rather than copying exact structure**
  - Rather than copying the exact structure, it interprets the motion from input videos
  - *From: pom*

- **CogVideoX supports multi-phase prompts**
  - Can handle complex prompts with scene transitions like 'Scene 1: A blonde female... Transition: A zoom out... Scene 2: A new female...'
  - *From: pom*

- **CogVideo img2vid can render complex reasonably long motion from input images**
  - Using image inputs seems to elevate the amount of detail the model can render
  - *From: pom*

- **CogVideoX can coherently interpret highly imprecise instruction**
  - Model can understand what's in gaps with subtle guidance
  - *From: pom*

- **CogVideoX can track lips and faces with pose control**
  - Face pose controls characters very loosely, can track lip movements
  - *From: pom*

- **Motion drawing now available for CogVideoX via Tora**
  - Motion drawing working in Comfy with 16GB VRAM
  - *From: pom*

- **Moshi optimized by 16x to run on local GPUs**
  - Originally required 4x h100s, now runs on local GPUs within 2 days of release
  - *From: pom*

- **LoRA Training for HunYuan works with only images**
  - Incredibly quick training, very good adherence to subjects, works flexibly in different contexts while retaining details like tattoos
  - *From: pom*

- **Warped Noise technique for guiding video generation**
  - Netflix released technique, integrated into Comfy by Kijai, works with Cog and AnimateDiff
  - *From: pom*

- **HunYuan can run on just 12GB VRAM**
  - Workflow shared that enables playing with Hunyuan with only 12GB VRAM
  - *From: pom*

- **HunYuan can generate high quality in 10-15 steps**
  - Fast generation with good quality results
  - *From: pom*

- **Camera motion control for LTXV**
  - Technique allows guiding LTXV generations with specific camera motions using different trajectories on same input
  - *From: pom*

- **LTXV 0.9.5 combines excellent control with speed**
  - Probably the best control of any modern open video model while being incredibly fast at 3600 frames/min
  - *From: pom*

- **Context window shifting works well with Wan 14b**
  - Shows really nice results with barely noticeable shifts, combining approaches from AnimateDiff ecosystem
  - *From: kijai*

- **Reward LoRA for Hunyuan improves prompt adherence**
  - Very positive impact on prompt adherence - prompt mentioning 'walking' shows much better adherence with the LoRA
  - *From: community member*

- **Sonic can make very expressive speaking from audio input**
  - Can even do dogs, available in ComfyUI
  - *From: community member*

- **Wan Control LoRAs can be trained on any condition with input/output video pairs**
  - Can be used for deblurring, inpainting by training on videos with segments removed, interpolating, drawing trajectories based on optical flow, interpreting hand signals and body movements as motion
  - *From: pom*

- **LTXV 13b is particularly excellent for LoRAs**
  - Model feels amazing for LoRAs with fast training times, can accomplish high quality results in 60-90 minute training runs
  - *From: pom*

- **Video LoRAs can create content that looks completely unlike closed models**
  - Hard to distinguish as AI, can combine multiple LoRAs together for unique effects
  - *From: pom*

- **VACE enables Hollywood-level face-swapping in ComfyUI**
  - Users achieving professional quality face swaps and costume changes with VACE
  - *From: pom*

- **ATI provides finally good motion trajectory control**
  - ATI released offering trajectory control that feels natural and responsive for video generation
  - *From: pom*

- **Normalized Attention Guidance works on distilled models**
  - New negative prompting approach that works on distilled models, breaks Flux out of its typical style
  - *From: pom*

- **Clownshark achieved next-level style transfer with HiDream while reducing VRAM by 4GB**
  - Style/structure transfer without assistant models, achieving MJ sref level versatility
  - *From: pom*

- **4-step distillation method for Wan**
  - ModelTC team launched LightX2V - a 4-step distillation method for Wan
  - *From: pom*

- **VACE masking technique unlocked**
  - Magic VACE masking that allows for precise object manipulation and effects
  - *From: pom*

- **Smooth continuations without color distortion achieved**
  - Finally figured out how to get smooth continuations w/o colour distortion from Wan/VACE
  - *From: pom*

- **Dynamic complete object removal without shadows**
  - Technique for removing objects completely from video without leaving shadow artifacts
  - *From: pom*

- **Wan upscaling comparable to Topaz**
  - Open source upscaler that feels at least as good as the new Topaz upscaler while being infinitely configurable and extendable
  - *From: pom*

- **WanAnimate can track facial features very well and even do pupils**
  - Out of the box it works well for single character animations and can bring static images to life with just 10 steps
  - *From: pom*

- **VitPose with WanAnimate can do animal animations**
  - Successfully demonstrated with quadruped animals like dogs and hippos
  - *From: 614602980943069214*

- **QwenImage 2509 can interpret multi-image inputs and controlnets very impressively**
  - New version shows significant improvements in multi-image processing capabilities
  - *From: pom*

- **Pusa integration shows promise for video extensions**
  - Kijai shared integration with example workflow showing good results for video continuations
  - *From: pom*

- **LoRA trained on Animatediff outputs produces unique motion style**
  - LoRA trained on Animatediff outputs allows for Wan-level motion and image adherence together with distinctly Animatediff-y movement
  - *From: pom*

- **Low strength LoRA application brings subtle motion enhancement**
  - Using the Animatediff LoRA at low strengths brings a subtly Animatediff-y burst of motion to things, works well at just 6 steps
  - *From: pom*

- **VACE masking degradation can be eliminated**
  - Latent noise hijinks can eliminate the VACE masking degradation, allowing seamless placement of old man into any video
  - *From: pom*

- **Context transitions enable scene transformations with subject consistency**
  - Using context transitions allows doing scene transformations while keeping the subject consistent
  - *From: pom*

- **Wan Move represents significant improvement over AI**
  - Wan Move looks impressive and feels like a huge step-up from AI, works even for abstract and irrational content
  - *From: pom*

- **Water morphing LoRA trained efficiently**
  - LoRA for water morphing effects trained on just 6 videos for 1,000 steps
  - *From: pom*

- **LTX-1 LoRAs work with LTX-2**
  - LTX-1 loras all seem to work with LTX-2, and 62 LoRAs from LTX 0.97 were tested to validate compatibility
  - *From: 380911583074975744/464322697418244096*

- **LTX-2 supports multiple types of conditioning at launch**
  - LTX2 can do multiple kinds of conditioning on launch including pose control
  - *From: pom*

- **LTX-2 inpainting appears undetectable**
  - LTX-2 inpainting capability seems almost undetectable in quality
  - *From: pom*

- **LTX-2 runs efficiently on RTX 3090**
  - LTX-2 can run on a 3090 GPU with impressive results
  - *From: 865676776058126386*

- **Flux Klein models show impressive outpainting/colorization**
  - New Flux Kleins are quite impressive for relatively small size - 4b can do outpainting/colorisation in seconds
  - *From: 431893297561337866*

- **IC-LoRA approach for LTX2 control mechanisms**
  - LTX released a IC-LoRA approach for training control mechanisms for LTX2, including luminance map references for lighting control
  - *From: oumoumad*


## Troubleshooting & Solutions

- **Problem:** A1111 extension is broken and various repos have loads of issues
  - **Solution:** Kosinkadink is working on fixing ComfyUI extension and applying learnings to fix A1111
  - *From: pom*

- **Problem:** Background tends to be very chaotic - jumping all over the place with the main subjects in AD
  - **Solution:** This problem is solvable with fine-tuning - train a model on data with steady backgrounds
  - *From: pom*

- **Problem:** DragNUWA can't reveal hidden secrets in artworks
  - **Solution:** Acknowledged limitation - technique doesn't understand object nature well enough
  - *From: Kijai*

- **Problem:** DragNUWA frequently doesn't understand object nature
  - **Solution:** Results in weird transformations - known limitation to be aware of
  - *From: whobody*

- **Problem:** AnimatedDiff v3 initial compatibility issues
  - **Solution:** Rebalance setup around v3 rather than avoiding it - Connor suggests adapting workflows
  - *From: connorrs*

- **Problem:** Live Comfy AD link broken with v3
  - **Solution:** Use specific HuggingFace tree link as alternative
  - *From: pom*

- **Problem:** IP adapters trained at low resolution and only square images cause detail loss and artifacts on wider generations
  - **Solution:** Use tiled IP adapter to work better on non-square images (experimental)
  - *From: pom*

- **Problem:** ComfyUI_LLMVISION nodes had a security exploit
  - **Solution:** There are instructions on how to deal with it in a Reddit post
  - *From: pom*

- **Problem:** Tooncrafter can be inflexible and breaks easily, especially with characters in in-between movements
  - **Solution:** No specific solution provided, noted as a limitation
  - *From: pom*

- **Problem:** Flux VRAM requirements
  - **Solution:** Workflow for getting Flux running with 12GB VRAM
  - *From: Inner Reflections*

- **Problem:** CogVideoX fragmented ecosystem with different LoRAs/CNs for different versions
  - **Solution:** Could likely be fixed with IPA for unconventional styles
  - *From: pom*

- **Problem:** CogVideoX tends to frequently break
  - **Solution:** Could likely be controlled with an IPA
  - *From: pom*

- **Problem:** LTXV breaks down frequently and is overly sensitive to prompting
  - **Solution:** Use RF Inversion with the img2Vid model for better vid2vid results
  - *From: pom*

- **Problem:** New install anxiety with ComfyUI
  - **Solution:** Custom node for managing Comfy environments with tutorial
  - *From: pom*

- **Problem:** WanAnimate doesn't do multicharacter animations out of the box
  - **Solution:** This is a known limitation that hasn't been solved yet
  - *From: pom*

- **Problem:** VRAM limitations for VACE workflows
  - **Solution:** Low VRAM VACE 2.1 workflow that works with under 8GB VRAM
  - *From: 1006234707375173722*

- **Problem:** Motion speed issues with distilled Wan
  - **Solution:** Using Animatediff LoRA helps solve motion speed problems with distilled Wan
  - *From: pom*


## Model Comparisons

- **SD1.5 vs Realistic Vision 5**
  - Equivalent level of progress can be achieved with AD through fine-tuning
  - *From: pom*

- **AD progress vs Pika Labs**
  - AD is improving but Pika started from higher base and is improving at fast pace
  - *From: pom*

- **AnimateDiff vs Stable Video Diffusion**
  - SVD delivers more impressive base outputs especially for 3D motion, but AD's modular approach and ecosystem makes it better for fine-grained control, vid2vid, and creative interpolation. Best used together for different strengths
  - *From: pom*

- **DragNUWA vs Runway's motion brush**
  - DragNUWA feels like a better version with more control
  - *From: pom*

- **AnimatedDiff v3 assessment**
  - v3 probably is the best now, requires setup rebalancing but worth adapting to
  - *From: connorrs*

- **Magnific vs Magnifake workflows**
  - Community workflows replicate $39/month Magnific functionality for free
  - *From: Fictiverse*

- **SVD 1.1 vs previous version**
  - Small step up but still suffers from inconsistency and degradation throughout frames
  - *From: pom*

- **AnimateDiff vs Warpfusion (1 year ago)**
  - Warpfusion clip holds up well in comparison
  - *From: pom*

- **Sora vs AnimateDiff**
  - Sora incredibly impressive but AD overwhelmingly better for precise motion control due to community work
  - *From: pom*

- **DynamiCrafter vs SVD**
  - DynamiCrafter surpasses SVD in terms of quality/dynamism and is promptable, but struggles outside anime/realistic styles and lacks ecosystem
  - *From: pom*

- **DynamiCrafter vs AnimateDiff ecosystem**
  - DynamiCrafter won't see AnimateDiff level of improvement due to limited extensibility and ecosystem
  - *From: pom*

- **ELLA vs SD1.5 and Dall-E**
  - Maybe a juiced-up SD1.5 is all we need
  - *From: pom*

- **CogVideoX vs other video models**
  - Has good, realistic motion but may not be great for extending
  - *From: pom*

- **CogVideoX vs closed-source models**
  - Lower resolution/detail than main closed-source models, but has impressive base motion when it works
  - *From: pom*

- **CogVideoX vs AnimateDiff**
  - CogVideoX motion is promptable unlike AD, but doesn't plug into existing SD1.5 ecosystem
  - *From: pom*

- **Flux vs CogVideoX**
  - Flux Video will almost certainly beat Cog on metrics, but unknown if better for practical creative tasks
  - *From: pom*

- **Open models vs Sora and closed models**
  - Expects Sora to destroy open models on head-to-head basis, but believes open source innovation will make them more creatively empowering - similar to how AnimateDiff vs Pika Labs played out
  - *From: pom*

- **Current AI video vs a year ago**
  - Massive improvement - comparing current AnimateDiff results with similar work from a year ago shows dramatic progress
  - *From: pom*

- **Hunyuan vs CogVideoX**
  - Hunyuan is better model head-to-head but CogVideoX feels best for control
  - *From: pom*

- **Wan(x) 14b vs Sora**
  - Wan(x) beats Sora on VBench rankings despite being 14b variant
  - *From: pom*

- **Open vs closed models prediction**
  - There probably won't be a meaningful gap between open and closed models in 2025 - open models will have considerably more control
  - *From: pom*

- **Wan vs other models for specific tasks**
  - Wan takes 5+ mins to run, likely only best for tasks requiring cohesive motion, other models better for specific tasks
  - *From: pom*

- **LTXV vs Wan**
  - LTXV is overwhelmingly faster than Wan and other models, particularly excellent for LoRAs
  - *From: pom*

- **Cloud 4090 vs Luma for generation**
  - Cloud 4090 costs 20x less than Luma for similar quality, also better quality
  - *From: pom*

- **VRGameDevGirl's Wan Megamerge vs main Wan model**
  - Megamerge combines multiple detailer and speed LoRAs, produces beautiful results
  - *From: pom*

- **Causvid vs LightX2V at 4 steps**
  - Test comparison shown by David Snow
  - *From: pom*

- **Wan VACE vs Warp**
  - Wan VACE described as superior for revisiting pieces
  - *From: pom*

- **Flux vs. Qwen training**
  - Qwen shows superior training results
  - *From: 497770368853999628*

- **WanAnimate vs other face animation models**
  - Finally competitive with high-end solutions, can do pupils and detailed facial tracking
  - *From: pom*

- **WanAnimate and VACE vs Sora**
  - WanAnimate and VACE are to art what Sora is to slop - they offer the level of control needed for admirable artwork
  - *From: pom*

- **New subject LoRA vs Nano + Seedream**
  - Works significantly better than Nano + Seedream for subject + style when paired with InStyle LoRA
  - *From: pom*

- **Z-Image vs Flux 2**
  - Interesting comparisons shared showing differences between Z-Image (left) and Flux (right) in results
  - *From: pom*

- **Animatediff LoRA v1 vs v2**
  - Comparisons done between version 1 and version 2 of the Animatediff LoRA
  - *From: lostless.visuals*

- **SCAIL vs Wan Animate vs other vid2vid approaches**
  - Wan Animate feels so different to SCAIL and other more linear vid2vid approaches
  - *From: pom*

- **Animatediff LoRA trained for both Wan and LTXV**
  - Interesting differences between the two models when using same LoRA
  - *From: 743301749086879808*


## Tips & Best Practices

- **Fine-tuning will be key to unlocking AD**
  - Context: Similar to SD1.5 ecosystem evolution
  - *From: pom*

- **Pair music with art you share**
  - Context: Makes content feel more alive and impactful
  - *From: pom*

- **Use motion scale to control amount of motion**
  - Context: When you need to increase or decrease motion in videos like dogs playing poker
  - *From: Kijai*

- **Combine different AI tools for enhanced results**
  - Context: Use LLM for poem generation, then prompts for prompt travel, then AD for video, then voice gen for narration
  - *From: user*

- **Use attention masking with IPAdapter for better character consistency**
  - Context: When doing video transformations and maintaining coherent characters
  - *From: various users*

- **Share experimental findings when playing with new models**
  - Context: Helps others understand capabilities and enables further development
  - *From: pom*

- **Focus on specific domains and go deep**
  - Context: Better results than trying to do everything - HarrowLogo's logo work as example
  - *From: pom*

- **Reduce friction for frontier explorers**
  - Context: Create workflows that help others get started with new techniques
  - *From: pom*

- **Push styles and vibes to the max**
  - Context: High-effort art that pushes techniques to limits inspires mini-art movements
  - *From: pom*

- **Use multiple Motion LoRAs with LoRA masking for different effects throughout video**
  - Context: Queue multiple LoRAs throughout generation using Kosinkadink's LoRA masking for 'LoRA travel'
  - *From: pom*

- **Build an army of Motion LoRAs for shared repository**
  - Context: Anyone can add LoRAs to shared repository with description, HuggingFace link, and example video
  - *From: pom*

- **IPA plays very nicely with motion loras for powerful steering**
  - Context: When using workflows like Purz Context Smashing or Steerable Motion
  - *From: pom*

- **IPA tiling will likely allow you to increase resolution using existing realistic upscale methods while retaining style**
  - Context: For video upscaling applications
  - *From: pom*

- **Share workflows and learnings openly to help ecosystem thrive**
  - Context: When exploring and building on top of new technologies
  - *From: pom*

- **Browse through the channel and take time to appreciate the work of others to keep ego in check**
  - Context: Making art tends to be a very egotistical pursuit
  - *From: pom*

- **Don't do competitions just for the prizes - do it to push yourself to see how good you can make something**
  - Context: Motivation for entering competitions
  - *From: pom*

- **Create for yourself and not the algo**
  - Context: General creative advice for artists
  - *From: jeru*

- **Use archival footage approach to mask model limitations**
  - Context: For compelling storytelling when working with AI video models
  - *From: pom*

- **Use image inputs with CogVideoX to elevate detail quality**
  - Context: When working with CogVideo img2vid implementation
  - *From: pom*

- **Flux Block LoRA selector helps understand what different LoRA layers are doing**
  - Context: For targeting generations better
  - *From: pom*

- **Use AnimateDiff as upscaler for CogVideoX when rendering at low sizes**
  - Context: Works nicely for improving CogVideoX output
  - *From: pom*

- **Combine multiple control methods for precise AI video control**
  - Context: Key to driving AI video with precision, currently have IPA and CN that can be combined
  - *From: pom*

- **Combining multiple control methods is key to deep creative control**
  - Context: When using video generation models like Mochi or CogVideoX
  - *From: pom*

- **Share workflows that are useful to others to help them start from a higher point and push even further**
  - Context: When developing new model workflows
  - *From: pom*

- **Use director personas for style prompting**
  - Context: When using LTXV - dramatically changes shot characteristics
  - *From: pom*

- **Use refined settings for HunYuan upsampling**
  - Context: Will be even better once Hunyuan CNs are available
  - *From: pom*

- **Motion LoRAs can create unique artistic capabilities**
  - Context: Training LoRAs for distinct motion styles and characteristics from source material
  - *From: pom*

- **Specific artistic capabilities and user experience matter more than raw model power**
  - Context: How good the artistic experience is and predictability/usefulness for creative process
  - *From: pom*

- **Control models and workflows will be extremely important**
  - Context: For unlocking specific capabilities since txt2vid and img2vid are very limited from control perspective
  - *From: pom*

- **Control LoRAs can potentially stack for AD-level control**
  - Context: Though it's an open question how well they stack
  - *From: pom*

- **Video LoRAs have extraordinary potential for both unique styles and consistent styles of motion**
  - Context: For creating cinematic content
  - *From: pom*

- **Use Shift+Esc to mark all spam channels as read**
  - Context: When dealing with Discord spam
  - *From: pom*

- **React with openmuse emoji to push art to OpenMuse**
  - Context: Contributing art you're proud of to the community gallery
  - *From: pom*

- **Use continuation nodes and workflows to avoid discoloration**
  - Context: When working with Wan+
  - *From: pom*

- **Combining models (Multitalk + MAGREF + Uni3c) to achieve impressive results no single model can do**
  - Context: Reminiscent of Stable Diffusion/Animatediff days approach
  - *From: 846408309531213867*

- **Creating anchor images + animating them with edit models for creative exploration**
  - Context: Using edit models for creative workflows
  - *From: 994554775980998696*

- **Use upscaling individual images then vid2vid for better results**
  - Context: Approach common in AnimateDiff days, now applicable to Wan with excellent results
  - *From: 1074404980737450065*

- **Combine context windows and prompts for video continuations**
  - Context: Can achieve impressive results without complex workflows
  - *From: 867727155499499520*

- **Use sliding context windows for long video generation**
  - Context: Can render 2000 frames of InfiniteTalk in just 12 minutes
  - *From: 228118453062467585*

- **Use lower LoRA strengths for subtle motion enhancement**
  - Context: When wanting to add subtle Animatediff-y motion to content
  - *From: pom*

- **Combine anchor images + Humo to add lipsync to i2v generations**
  - Context: For adding lip sync functionality to image-to-video generations
  - *From: pom*

- **Share your work to help the open source ecosystem**
  - Context: People like LTX and Alibaba release models because they believe benefits of being open can outweigh downsides. Sharing work in channels, Twitter, Reddit helps continue this spirit
  - *From: pom*

- **Use well chosen key frames for better results**
  - Context: Extraordinary results can be accomplished with well chosen key frames
  - *From: pom*


## News & Updates

- **Banodoco community launched with focus on open source AI video/image generation**
  - 3 main components: Steerable Motion, Img+Img2Vid models, Creative Assistant
  - *From: pom*

- **Research product coming soon for building and animating videos key-frame by key-frame**
  - Will run on local GPU or cloud
  - *From: pom*

- **B34STW4RS released first version of repo for fine-tuning Animatediff**
  - AD-Evo-Tuner - still early but functional
  - *From: pom*

- **$8k in compute credits offered for experiments**
  - For ideas too big or expensive for individual users
  - *From: pom*

- **Kosinkadink shipped functional ComfyUI extension after days of work**
  - Best place for technically-oriented people to experiment with AD
  - *From: pom*

- **Monthly equity grants announced - 0.125% each to 8 contributors**
  - Part of open-source native company building approach
  - *From: pom*

- **Ceyuan Yang & Yuwei Guo released Motion LoRAs for Animatediff**
  - Examples for camera movements but can be used for much more
  - *From: pom*

- **HotshotXL released - AD-esque motion module trained on SDXL**
  - Trained on 8 frames, made for short gifs
  - *From: pom*

- **The Tobloronés art competition launched**
  - Theme: 'journeying', deadline Oct 22nd, winner gets 4.5kg Toblerone
  - *From: pom*

- **SDXL Motion Module beta released by original AnimateDiff authors**
  - Beta version available on HuggingFace, produces 1024x1024 16 frame videos
  - *From: pom*

- **The Tobloronés #2 art competition announced**
  - Deadline December 20th, theme 'an emotional journey', prize is giant Toblerone
  - *From: pom*

- **Banodoco monthly equity distribution**
  - 1% equity split monthly among contributors for first 8.5 years, shared between people who ship things aligned with open source AI video goals
  - *From: pom*

- **New topic-specific channels created**
  - Vid2vid and Interpolation channels created for deep topic exploration
  - *From: pom*

- **SparseCtrl release from AnimatedDiff team**
  - Video controlnets with RGB and Scribble variants - first video controlnets available
  - *From: pom*

- **AnimatedDiff V3 released**
  - Latest version with improvements, integrated into Comfy within hours
  - *From: pom*

- **HarrlogosXL-v2 release**
  - New version of logo LoRA with logo video animation for SVD
  - *From: HarrowLogo*

- **DragNUWA released by Microsoft**
  - Drag-based control for SVD generations, multiple community implementations
  - *From: pom*

- **IP-Adapter competition announced**
  - 2 NVIDIA 4090s prize sponsored by Glif for creative masking and simple workflow categories
  - *From: pom*

- **Steerable Motion 1.1 v.1 released**
  - Combines IPA with Sparse Ctrl for better creative interpolation
  - *From: pom*

- **Exponential ML released Motion LoRA trainer for AnimateDiff v3**
  - Allows training MotionLora on single video in around 15 minutes for precise motion guidance
  - *From: pom*

- **Kosinkadink released huge AnimateDiff ComfyUI 'gen2' update**
  - Refactors for flexibility, includes scheduling motion model settings, FreeNoise support, View Options, non-looping context options, FreeInit support, multiple model support, improved Mac support
  - *From: pom*

- **Stability released SVD 1.1**
  - Small improvement over previous version but still has consistency and degradation issues
  - *From: pom*

- **Kosinkadink opened GitHub and Patreon sponsorship pages**
  - Community encouraged to support his infrastructure work that enables all workflows
  - *From: pom*

- **Zeroscope now available in Comfy**
  - Cerspense brought the legendary Zeroscope to Comfy with distinct and interesting motion style
  - *From: pom*

- **Deforum launched their nodes on Comfy**
  - Deforum nodes bring all that magic to Comfy, also launched Deforum Studio consumer product
  - *From: pom*

- **DynamiCrafter interpolation version released**
  - New version allows for interpolation from starting image to ending image, Kijai implemented basic version into Comfy
  - *From: pom*

- **Dough beta testing ready**
  - More stable version ready for beta testers, built on top of Steerable Motion and various Comfy nodes
  - *From: pom*

- **ControlNet Reference implemented in Comfy**
  - Kos implemented CN Reference into Comfy, previously only available in A1111
  - *From: pom*

- **Matteo became published paper coauthor**
  - Others released paper featuring Matteo's style transfer work and made him coauthor
  - *From: pom*

- **Art Sharing Wednesday converted to YouTube format**
  - Now a weekly YouTube show up to 10 minutes featuring pieces shared throughout the week
  - *From: pom*

- **ELLA implementation available in ComfyUI**
  - ELLA took the nerd internet by storm and ntialML was quick with Comfy implementation
  - *From: ntialML*

- **Face/Bodyswap workflow released by VK**
  - Workflow allows transforming faces and heads/hair while staying close to context
  - *From: VK*

- **Midjourney.Man shared optimized version of VK's workflow**
  - Iteration with bunch of optimizations
  - *From: Midjourney.Man*

- **Banodoco company raising $1m funding at $10m valuation**
  - First checks in bank, expect to close around end of month
  - *From: pom*

- **Banodoco had first revenue of €224.94 from Doughbot testers**
  - Plans to share profits as it becomes significant
  - *From: pom*

- **The Tobleronés #3 competition announced**
  - Theme uses ComfyUI default images, deadline May 24th, prizes include giant Toblerone bars
  - *From: pom*

- **Banodoco bounties granted to two recipients**
  - One for training better versions of Animatediff and open source Story Diffusion, another for upgrading art sharing bot
  - *From: pom*

- **The Tobloronés #3 competition winners announced**
  - Winners were 'Breaking free' by Brad, 'Alice In LaLaLand' by Material Rabbit, 'Chocolate Land', and 'Comfy Dreams' by Jas
  - *From: pom*

- **Tooncrafter released as evolution of {x}_crafter line of interpolation models**
  - Does impressive interpolation with realistic motion in-between frames, but based on 2.1 so limited other models available
  - *From: pom*

- **Mobius SDXL-based fine-tune released on apache-2.0 license**
  - Results are impressive especially in terms of variety of style possible
  - *From: pom*

- **Dough 0.9.5 released, almost a good artistic tool**
  - Both Dough and Steerable Motion are close to being a great artistic experience
  - *From: pom*

- **Dough 0.9.8 released with new Inspiration Engine feature**
  - Uses LLM + style transfer work to generate hundreds of potential input images to choose from. Pinokio integration coming soon
  - *From: pom*

- **Banodoco equity sharing for May announced**
  - Company shares 1% per month for first 7.5 years with ecosystem participants, sharing 100% of proceeds from ownership
  - *From: pom*

- **Dough v. 0.9.9 release**
  - Now stable and good artistic tool, featuring Steerable Motion with more workflows coming. Cheap version ($0.30/GPU hour) coming soon with 75% profit sharing with community
  - *From: pom*

- **Flux major release**
  - Big week for open source with Flux release, multiple community implementations and fine-tunes
  - *From: pom*

- **SAM2 launch**
  - Near-perfect image segmentation capabilities, nearly as big a deal as Flux
  - *From: pom*

- **StoryDiffusion training approaching**
  - Coming close to training time #1 and looking for braintrust of people who've trained models before
  - *From: pom*

- **Instruct IP-Adapter for SD3**
  - Instruction-driven IP-Adapters that allow prompting IPA alongside image reference, includes first IP-Adapter for SD3 and working towards one for Flux
  - *From: research team*

- **Ostris released Flux LoRA trainer**
  - AI-toolkit now supports Flux1 training with tutorial from promptcrafted
  - *From: pom*

- **CogVideo released image2video implementation**
  - Available using Kijai's Comfy nodes, shows promising base motion capabilities
  - *From: pom*

- **Banodoco monthly update and equity announcement for August**
  - Shared monthly community update
  - *From: pom*

- **Motion I2V released 6 months post paper**
  - Allows guiding AnimateDiff motion by drawing arrows, limited to 16 frames
  - *From: pom*

- **FlippingSigmas Unsampling Variant released**
  - Most coherent vid2vid transformations possible with open models today
  - *From: pom*

- **32 frame context LoRA for AnimateDiff**
  - Continuing quest to defeat AnimatedDiff context switching
  - *From: pom*

- **CosyVoice open source voice model**
  - Very promising for voice2voice capabilities
  - *From: pom*

- **Moshi by Genmo released for local GPU**
  - Optimized to run on local GPUs instead of requiring 4x h100s
  - *From: pom*

- **CogVideoX Interpolation released**
  - Shipped by multiple contributors
  - *From: pom*

- **Tora for CogVideoX available**
  - Motion drawing now working in Comfy with 16GB VRAM
  - *From: pom*

- **CogVideoX 1.5 model released**
  - New version of CogVideoX with improved capabilities
  - *From: pom*

- **Lighttricks open sourced LTXV video model**
  - Speed is primary appeal, produces beautiful results when working well, but breaks down frequently. Full model on open license promised once fully trained
  - *From: pom*

- **Huge AnimateDiff ComfyUI update by Kosinkadink**
  - Major ModelPatcher system rework enabling powerful LoRA masking and scheduling capabilities
  - *From: pom*

- **Huanyuan video model released**
  - Open source model capable of producing high-quality clips on 4090 GPU, with strong vid2vid potential
  - *From: pom*

- **Sora expected to drop**
  - Anticipated release of OpenAI's video model
  - *From: pom*

- **New season of Project Odyssey announced**
  - Competition/art challenge with trailer created
  - *From: pom*

- **Discord restructuring completed**
  - #ad_resources moved to different channel, #ad_comfyui relocated, CogVideoX got new section
  - *From: pom*

- **New LTXV model 0.9.1 released**
  - Better stability, motion, and more while being as fast as previous version
  - *From: pom*

- **Framer finally released**
  - Promising approach that combines interpolation with multiple trajectory drawings, wrapper available
  - *From: pom*

- **Hunyuan3D released - SOTA Image to 3D**
  - New model from Hunyuan team with wrapper available
  - *From: pom*

- **New version of Ryanontheinside nodes**
  - Wide range of improvements and better performance
  - *From: pom*

- **Project Odyssey deadline January 16th**
  - Rendering and VFX category has less than 10 submissions
  - *From: pom*

- **LTXV 0.9.5 released**
  - Best control of any modern open video model, 3600 frames/min speed
  - *From: pom*

- **Sonic released**
  - Can make very expressive speaking from audio input, available in ComfyUI
  - *From: pom*

- **Wan(x) from Alibaba released**
  - 14b variant beats Sora on VBench rankings, very impressive results
  - *From: pom*

- **ADOS Paris event announced**
  - March 28/29 at Artifex-Lab, partnership with Lighttricks, capped at 150 people, scholarships available
  - *From: pom*

- **Video-Depth-Anything released**
  - Does very impressive video depth mapping
  - *From: pom*

- **LTXV 13b model launched**
  - New model release that's faster than Wan and particularly good for LoRAs
  - *From: pom*

- **OpenMuse platform announced**
  - New curated space for video LoRAs and art made with them at openmuse.ai
  - *From: pom*

- **Control LoRAs training code released**
  - Training code shared for creating Control LoRAs
  - *From: pom*

- **VACE released with causevid for generation in <6 steps**
  - Speed boost for Wan allowing much faster generation times
  - *From: pom*

- **LTXV got huge speed boost with distilled version**
  - Distilled version provides significant performance improvements
  - *From: pom*

- **OpenMuse now includes workflows and improved stability**
  - Platform updated to allow workflow sharing and better stability
  - *From: pom*

- **ATI released with trajectory control**
  - New system for controlling motion trajectories in video generation
  - *From: pom*

- **LTXV beta testers given H100s for testing**
  - Some community members have access to H100 hardware for training
  - *From: pom*

- **LightX2V launched by ModelTC team**
  - 4-step distillation method for Wan video generation
  - *From: pom*

- **Multitalk is available on experimental branch**
  - Works for single subjects, on experimental branch of ComfyUI-WanVideoWrapper
  - *From: pom*

- **Kontext is out**
  - New model release with various community applications
  - *From: pom*

- **Official Multitalk support with Context Windows**
  - Kijai added official Multitalk support to ComfyUI-WanVideoWrapper
  - *From: pom*

- **LTXV launched Controlnets and training script**
  - Controlnets for LTXV and training script for training them in a few hours
  - *From: pom*

- **LTXV released new version with very long generations**
  - New LTXV version capable of generating very long video sequences
  - *From: pom*

- **Wan 2.2 released**
  - Already slicing through the Coca-Coca with a meat cleaver benchmark
  - *From: pom*

- **Fun-Control controlnets available for Wan 2.2**
  - Kijai has implemented them and used them to make pandas do the macarena
  - *From: pom*

- **FantasyPortrait now available in Comfy**
  - Implemented by Kijai
  - *From: pom*

- **infiniteTalk landed**
  - Able to do extremely good mouth layering onto existing videos
  - *From: pom*

- **TheMatrix and more world models launched**
  - Check out dedicated channel for exploration
  - *From: pom*

- **HunyuanFoley looks promising as mmaudio successor**
  - Comfy nodes created by 983060020516249670
  - *From: pom*

- **Wan S2V released with pose control**
  - Audio-video generation capabilities
  - *From: pom*

- **Pusa released with Kijai integration**
  - New model with ComfyUI integration available for video extensions
  - *From: pom*

- **WanAnimate released**
  - New face animation model that can track facial features and pupils effectively
  - *From: pom*

- **New VACE for Wan 2.2 by Fun team released**
  - Shows impressive continuations without degradation and good inpainting capabilities
  - *From: pom*

- **QwenImage 2509 released**
  - New version with multi-image input and controlnet support
  - *From: pom*

- **AOOS LA event announced for November 7th**
  - Event will be at Charlie Chaplin's former soundstage, includes day-time unconference and evening event
  - *From: pom*

- **Huggingface offering free LoRA training**
  - Free GPU compute available for AI-Toolkit training including Wan, Qwen and more
  - *From: pom*

- **The Arca Gidan Prize competition launched**
  - Competition to inspire people in the ecosystem to push their art to its limits, 4 winners get to fly to LA, deadline is 7 days, sponsored by Comfy Org
  - *From: pom*

- **Real Time Video Summit in San Francisco**
  - Event featuring Ryanontheinside, Cerspense, DotSimulate and more speakers
  - *From: pom*

- **ADOS LA event happening**
  - Event in LA with community legends hosting roundtables, talks, and workshops
  - *From: pom*

- **Arca Gidan Prize winners announced**
  - 4 prize recipients: 'Static' by nrmopp, 'Duende' by Yurvraj, 'Woven' by PsiClone, 'The Trade' by Kaybroh
  - *From: pom*

- **Community member Alexander Morano passed away**
  - Maintained the Jovimetrix nodepack and moderated the community, passed away in September
  - *From: pom*

- **Daydream running 2 week open source live video hackathon**
  - Interactive AI video program hackathon opportunity
  - *From: pom*

- **LTX-2 release week**
  - LTX-2 launched with audio-based video generation capabilities and multiple conditioning types
  - *From: pom*

- **Banodoco Discord going default public**
  - All data will be public for LLMs to learn from + people to share
  - *From: pom*

- **Paris event planned for April 16-19**
  - Next Banodoco event planned as multiday art hackathon/show in Paris with four months notice
  - *From: pom*

- **Wan Move context window support added**
  - Context window support added to Wan Move
  - *From: 228118453062467585*

- **Wrapper nodes restructured**
  - Wrapper nodes restructured to enable magical capabilities of Wan to be combined to greater degree
  - *From: 228118453062467585*

- **New Banodoco website launched**
  - New Banodoco website created at banodoco.ai
  - *From: pom*

- **SVI-Pro for Wan 2.2 released**
  - New version of SVI-Pro for Wan 2.2 potentially offers path to endless smooth continuations
  - *From: 1143887423957377024*

- **LongCat implementation by Kijai**
  - LongCat implementation available thanks to Kijai's work
  - *From: pom*


## Workflows & Use Cases

- **Using starting and ending frames with ControlNet reference images to control AD**
  - Use case: Interpolation and control
  - *From: pom*

- **Chaining interpolated clips into coherent clip**
  - Use case: Creating longer coherent animations
  - *From: pom*

- **Vid2vid workflow with sliding context windows**
  - Use case: Very powerful video transformations
  - *From: pom*

- **img2gif/txt2gif + upscale workflow**
  - Use case: Creating and upscaling animated content
  - *From: pom*

- **Background masking workflow**
  - Use case: Static/isolated/separately animated backgrounds
  - *From: pom*

- **QR code ControlNet for logo animation using masks**
  - Use case: Logo animation effects
  - *From: pom*

- **Inpainting with AD**
  - Use case: Selective animation of image regions
  - *From: pom*

- **SD/AD combo for infinite zoom**
  - Use case: Creating infinite zoom effects
  - *From: pom*

- **Vid 2 QR 2 Vid workflow**
  - Use case: Interesting video transformations
  - *From: pom*

- **Rotoscoping workflow**
  - Use case: Basic, consistent transformations
  - *From: pom*

- **Vid2Vid with SDXL and HotShot**
  - Use case: Reskinning existing videos with new characters and styles
  - *From: 88822364468412416*

- **Text to OpenPose workflow**
  - Use case: Generate complex motion more reliably than diffusion models alone
  - *From: 310003312936091650*

- **Inpainting with ControlNet**
  - Use case: Direct inpainting applications
  - *From: 586961856271351833*

- **Inpainting with OpenPose over existing videos**
  - Use case: Replace characters in existing video footage
  - *From: 586961856271351833*

- **FaceDetailer for face consistency**
  - Use case: Improve jittery faces that AD often produces
  - *From: 750969956249632859*

- **3-image interpolation**
  - Use case: Create smooth transitions between multiple images
  - *From: pom*

- **Condition Mask Travel**
  - Use case: Use combination of CN masks to guide animations with precision
  - *From: Kijai*

- **Video stitching with FiLM**
  - Use case: Combine videos from different sources and smooth transitions
  - *From: 285445203211452416*

- **Add motion to still images**
  - Use case: Animate static images
  - *From: 1090035586582196326*

- **Target Location workflow**
  - Use case: Consistently render animation where object changes to small size in view
  - *From: 756701878011691029*

- **Mandela Maker**
  - Use case: Creating beautiful animated mandalas
  - *From: 400645014541172756*

- **IPAdapter Video2Video**
  - Use case: Coherent character transformations and soft video transformations
  - *From: 88822364468412416*

- **Character segmentation and greenscreening**
  - Use case: Create and use green screen footage with AI
  - *From: 310003312936091650*

- **SVD chaining**
  - Use case: Complex movements in shots, though still work-in-progress
  - *From: 499629400254447616*

- **Geometric shapes workflow by Cerspense**
  - Use case: Creating distinctive geometric art that others can adapt with unique spins
  - *From: Cerspense*

- **Cyberbear's personal workflow**
  - Use case: Based on Inner Reflections' work, demonstrates advanced techniques
  - *From: cyberbear*

- **Video inpainting workflow using video matting**
  - Use case: Keeps background and foreground completely separate for inpainting over videos
  - *From: Siraj*

- **Magnifake workflows**
  - Use case: Replicating Magnific upscaling functionality to save $39/month
  - *From: Fictiverse*

- **Screen capture to Comfy workflow**
  - Use case: Channeling screen captures directly into Comfy for leveraging faster models
  - *From: Impact Frames*

- **CybearPunk-Vid2Vid-Hotshotxl workflow**
  - Use case: ModelMerge, IPAMultiPorpuse, LoraStack, 4CN, FaceDetailer integration
  - *From: cyberbear*

- **Character segmentation + CN layer workflow**
  - Use case: Segments characters and applies CN to specific layers for vid2vid transformations
  - *From: Marcus Aurelius*

- **RAVE workflow by Kijai**
  - Use case: Advanced video generation with specific techniques
  - *From: Kijai*

- **Militant Hitchhiker's ControlNet Video Builder**
  - Use case: Turning any video input into portable, transferable, and manageable ControlNet videos
  - *From: pom*

- **Scene Assembler by Dkamacho**
  - Use case: Apply different IP-Adapters for background and foreground to achieve specific vid2vid transformations
  - *From: pom*

- **Audio Reactive IPAdapters by VisualFrisson**
  - Use case: Using audio feed to create IP adapter masks for various audio channels for audio reactivity
  - *From: pom*

- **Kijai's 'Gotta Go Fast' superfast vid2vid**
  - Use case: Dramatically increase speed of vid2vid while maintaining high quality
  - *From: pom*

- **LCM Vid2Vid by Inner Reflections**
  - Use case: Near-perfect and near-instantaneous video transformations
  - *From: pom*

- **LCM Img2vid transformations**
  - Use case: Image to video transformations using LCM
  - *From: pom*

- **Context smashing by Purz**
  - Use case: Advanced animation technique with precise control
  - *From: pom*

- **Subject and Background Isolation with AnimateLCM**
  - Use case: Use combination of images to steer character and foreground independently
  - *From: pom*

- **Motion landscapes**
  - Use case: Creating calm, serene landscape animations
  - *From: pom*

- **Water simulation workflow**
  - Use case: Generating water simulations
  - *From: pom*

- **Image2Vid + Interpolation with IPA Tile**
  - Use case: High-quality image to video conversion using IPA tile advances
  - *From: pom*

- **Smooth loop interpolation**
  - Use case: Creating smoother loop animations by interpolating between first and last frames
  - *From: pom*

- **txt2creepyvid**
  - Use case: Text to creepy video generation
  - *From: pom*

- **Motion Brush Image to Video with IPA**
  - Use case: Animate images while sticking closely to input material
  - *From: pom*

- **Smooth & Deep Steerable Motion**
  - Use case: Uses depth maps to adjust movement with different motion levels per layer
  - *From: pom*

- **Face/Bodyswap with Motion Brush**
  - Use case: Transform faces and heads/hair while staying close to context
  - *From: VK*

- **Video outpainting workflow**
  - Use case: Incredible video outpainting results
  - *From: nosecretsai*

- **AutoMask IPA GDINO-SAM Img/Vid-2-Vid LCM**
  - Use case: Advanced vid2vid processing
  - *From: AdamAD*

- **IP2P vid2vid workflow**
  - Use case: Beautiful video to video transformations using Ip2p
  - *From: abstract_chroma*

- **Fading Weights - daisy chained IPAs**
  - Use case: Make pictures move by morphing between images
  - *From: klinter*

- **Nightmare fuel workflow**
  - Use case: Uses Moondream to describe image to become prompt, includes random image selection
  - *From: purz*

- **Enormous Gif animations**
  - Use case: Slices up huge input image to create extremely large gif, great for animated Where's Wally
  - *From: pollyanna*

- **Audio to Video workflow**
  - Use case: Uses Whisper for lyrics extraction and Llama 3 to drive video creation
  - *From: fictiverse*

- **Isaac's Fully Automatic BeatSync AD**
  - Use case: Automated beatsync video generation
  - *From: pom*

- **5 new Steerable Motion workflows with unique motion and adherence types**
  - Use case: Different types of motion control, added to Dough
  - *From: pom*

- **Face-swapping workflow**
  - Use case: Easy face swapping in videos
  - *From: pom*

- **mgfxer's Animated Weights Transition Factory**
  - Use case: Using masks to drive animations in beautiful and subtle ways
  - *From: pom*

- **Dex's workflow for converting character sheets into animations using Tooncrafter**
  - Use case: Character animation from character sheets
  - *From: pom*

- **Music Visualiser Megaflow by audioreactive user**
  - Use case: Audioreactive visualization without requiring input video
  - *From: pom*

- **ComfyUI TensorRT Real-time Generative Filter achieving 2 fps**
  - Use case: Real-time generative filtering
  - *From: pom*

- **Animating from 3D depth maps**
  - Use case: Creating animations from depth map data
  - *From: pom*

- **Steerable Motion with Auto-Prompting using vision model**
  - Use case: Automated prompt generation for better consistency and motion
  - *From: pom*

- **Dreamzoom - infinite zoom workflow with live-prompting control**
  - Use case: Live-controlled infinite zoom videos with Steerable Motion output
  - *From: pom*

- **SDXL-Turbo Vid2Vid + Automation IP2P Masking**
  - Use case: Vid2vid processing on specific parts of video using SDXL
  - *From: pom*

- **mgfxer's Animatediff Weights 2.0**
  - Use case: Mask-driven animations with automatic mask creation and BLIP captioning
  - *From: pom*

- **Fading Weights #3 with Florence2**
  - Use case: Video generation with improved stability
  - *From: workflow creator*

- **IC Light Changer for Videos**
  - Use case: Video relighting effects
  - *From: Jerry Davos*

- **Florence & Kolors image masher**
  - Use case: Image mixing and composition
  - *From: workflow creator*

- **LivePortrait Animatediff combination**
  - Use case: Portrait animation with dynamic backgrounds
  - *From: community member*

- **Style Mix Master**
  - Use case: Batch image transformation and style transfer
  - *From: Jas*

- **Enhanced Visions with Clip Vision Enhancer**
  - Use case: Improved image analysis and processing
  - *From: Klinter*

- **Time dilation workflow**
  - Use case: Creating time dilation effects in video
  - *From: Akatz*

- **Vid2Vid morphing with fading weights**
  - Use case: Morphs through different influencing images during vid2vid processing
  - *From: Cyncratic*

- **Flux x SVD Vid2Vid**
  - Use case: Uses Flux i2i in combination with SVD for interesting video effects
  - *From: pom*

- **Audioreactive noise patterns**
  - Use case: Create audioreactive noise patterns in animation backgrounds
  - *From: Akatz*

- **Image travel with ADV3 + Hyper SD**
  - Use case: Travelling through images using FrameFX nodes & Clip Enhancer
  - *From: pom*

- **HyperFlux inpainting and upscaling**
  - Use case: Inpainting and detailing that works with less than 8gb VRAM
  - *From: Akumetsu971*

- **Updated LCM vid2vid workflow**
  - Use case: Battle-tested through creating many videos
  - *From: pom*

- **SDXL Video2Video Morph workflow**
  - Use case: Result of extensive experimenting for vid2vid SDXL morphs
  - *From: pom*

- **Simple 2 Step Deflicker workflow**
  - Use case: Deflickering videos
  - *From: pom*

- **Combining interpolation + Tora direction in CogVideoX**
  - Use case: Enhanced control for video generation
  - *From: pom*

- **Mochi Vid2Vid experimental implementation by Kijai**
  - Use case: Video-to-video transformation using Mochi model
  - *From: pom*

- **Audio-reactive denoising masks**
  - Use case: Creating audio-reactive visual effects
  - *From: pom*

- **Depth Aware Audio Reactive Particle Systems**
  - Use case: Advanced audio-reactive visual effects with depth awareness
  - *From: pom*

- **Framer frame interpolation + direction drawing**
  - Use case: Combined control methods for video generation with interpolation and directional control
  - *From: pom*

- **Audio-reactive interpolation workflow by Yvann & Liliens**
  - Use case: Audio-reactive traveling between images with tutorial provided
  - *From: pom*

- **In-Context Flux Flora approach**
  - Use case: Using logos in different contexts
  - *From: pom*

- **LTX vid2vid with image reference by VK**
  - Use case: Video-to-video with image reference using LTX unsampling
  - *From: pom*

- **LTX Image2Vid workflow by Avataraim**
  - Use case: Refined Image-to-video generation addressing LTX issues
  - *From: pom*

- **StyleMatch-Flux workflow by Drex**
  - Use case: Style-batching depth workflow combining BFL releases
  - *From: pom*

- **Depth + Redux transfer workflow**
  - Use case: Style transfer using depth and redux, available on HuggingFace
  - *From: pom*

- **Long Controllable Flux + LTXV I2V**
  - Use case: Enables long, controllable video generations
  - *From: pom*

- **Flux Upscaling workflow**
  - Use case: New upscaling approach built on top of Flux
  - *From: pom*

- **Vid2vid workflow with LTXV based on FlowEdit**
  - Use case: Video to video transformation
  - *From: pom*

- **HunYuan upsampling workflow with refined settings**
  - Use case: Better quality upsampling
  - *From: pom*

- **FlowEdit for Wan**
  - Use case: Video editing with flow control
  - *From: community member*

- **Video inpainting with differential diffusion**
  - Use case: LTXV video inpainting workflow shared
  - *From: community member*

- **Hunyuan video inpainting workflow**
  - Use case: Video inpainting with mask tracking capabilities
  - *From: community member*

- **NoiseWarp with SD1.5**
  - Use case: New workflow for using NoiseWarp
  - *From: community member*

- **Control LoRA training for deblurring**
  - Use case: SOTA deblurring trained in under a day on a 3090
  - *From: pom*

- **Room emptying LoRA trained on four images**
  - Use case: First image as control, last as target for transformation effects
  - *From: pom*

- **Combining IRL + Blender + AI**
  - Use case: For superhero landing effects
  - *From: pom*

- **VACE workflow for style/structure transfer**
  - Use case: Transforming video style while maintaining structure
  - *From: Mel*

- **ATI trajectory control workflow**
  - Use case: Controlling motion paths in video generation
  - *From: Adrien*

- **Face-swapping workflow using VACE**
  - Use case: Hollywood-level face replacement in videos
  - *From: ClownShark*

- **Fully-self-contained audio-reactive workflow**
  - Use case: Never-ending audiovisual painting for wall displays
  - *From: users*

- **Style + structure transfer with Wan**
  - *From: pom*

- **VACE x ATI combination for Lego-style animation**
  - *From: pom*

- **Continuation workflow for smooth video extensions**
  - *From: pom*

- **Vid2Vid with continuation nodes**
  - *From: pom*

- **Style transfer with Kontext**
  - *From: pom*

- **Combining Redux & Kontext**
  - *From: pom*

- **Sliding context windows with 4 different prompts for 337 frames**
  - Use case: Extended video generation with Wan 2.2
  - *From: Kijai*

- **6 steps over two samplers approach**
  - Use case: Efficient Wan 2.2 processing
  - *From: 256636116763934731*

- **Phantom + VACE merge workflow**
  - Use case: Enhanced video generation capabilities
  - *From: 88822364468412416*

- **VACE with Wan 2.2 for animating famous movie scenes**
  - Use case: Movie scene animation
  - *From: 766051574400417842*

- **Upscaling Deforum outputs with Wan 2.2**
  - Use case: Combining early-AI motion with modern AI aesthetics
  - *From: 985830005315633193*

- **Flux x Wan x Animatediff combination**
  - Use case: Multi-model video generation
  - *From: 272911326010015745*

- **Cocktail of different tools for simple yet intricate scenes**
  - Use case: Complex scene creation
  - *From: 240980243211354113*

- **FakeVace 2.2 merge for continuations**
  - Use case: Video continuations using merged model
  - *From: 771193439399444490*

- **Endless Travel workflow adaptation**
  - Use case: Continuations without degradation based on pom's original workflow
  - *From: 1074404980737450065*

- **Humo & InfiniteTalk combination for music videos**
  - Use case: Single-shot music video generation combining multiple models
  - *From: 330829305477333022*

- **SuperMegaGigaUpscaler workflow**
  - Use case: Upscaling individual images then applying vid2vid for enhanced quality
  - *From: 1074404980737450065*

- **Travel between images workflow**
  - Use case: Creating smooth transitions between different image scenes
  - *From: 825444296689451039*

- **Animatediff LoRA integration workflow**
  - Use case: Bringing Animatediff-style motion to Wan generations
  - *From: pom*

- **Humo megaflow for music videos**
  - Use case: Generating full videos based on music with tweakable parameters, similar to Deforum but different approach
  - *From: pom*

- **Anchor images + Humo for lipsync**
  - Use case: Adding lipsync to image-to-video generations
  - *From: pom*

- **Particle sims + ATI combination**
  - Use case: Creating specific visual effects
  - *From: pom*

- **Multi-image lip syncing workflow**
  - Use case: Synchronizing lip movements across multiple images
  - *From: pom*

- **SCAIL with Uni3c combination**
  - Use case: Video processing and generation
  - *From: 1074404980737450065*

- **SCAIL with Wan Animate**
  - Use case: Creating dynamic video scenes
  - *From: 322119599657320448*

- **Humo X VACE morph effect**
  - Use case: Music video effects that were previously expensive to create
  - *From: 256636116763934731*

- **Humo-automation-workflow-powered music videos**
  - Use case: Dynamic music video creation with insane potential
  - *From: 330829305477333022*

- **Z-image denoise deforumy travel for vid2vid**
  - Use case: Vid2vid processing
  - *From: 807028745344385034*

- **Black and white replication workflow**
  - Use case: Music video effect replication
  - *From: 256636116763934731*

- **Audio-based video generation for LTX-2**
  - Use case: Audio-driven video creation
  - *From: 228118453062467585*

- **SharkSampler/ClownsharkSampler with LTX-2**
  - Use case: Enhanced LTX-2 sampling
  - *From: 256636116763934731*

- **Humo x Wan 2.2 SVI workflow**
  - Use case: Advanced video generation
  - *From: 256636116763934731*

- **Fully automated image-to-video pipeline for songs**
  - Use case: Full-length music video automation
  - *From: 330829305477333022*

- **Background separation workflow with Animatediff**
  - Use case: Video background manipulation
  - *From: 809159895593123852*


## Recommended Settings

- **Motion Scale**: variable based on desired motion amount
  - Controls the amount of motion in output - can increase or decrease as needed
  - *From: Kosinkadink*

- **SparseCtrl RGB control levels**: Every frame vs 1 up to every 15th frame
  - Different levels provide varying control precision vs smoothness
  - *From: benejamin*

- **AnimatedDiff V3 setup**: Rebalance workflows around v3
  - Better performance than trying to make older setups work
  - *From: connorrs*

- **IPA weight_types**: Various new weight types exposed
  - Allows for better control and tweaking of IPA behavior
  - *From: pom*

- **Motion LoRA trained on weekly art**: WAS26 LoRA
  - Smooths out motion in a general way when applied
  - *From: pom*

- **Control LoRA training time**: Under a day on 3090
  - For SOTA deblurring results
  - *From: pom*

- **LTXV LoRA training time**: 60-90 minutes
  - Can accomplish high quality results in short training runs
  - *From: pom*

- **VACE generation**: <6 steps
  - Speed optimization with causevid
  - *From: pom*

- **Cloud training on Replicate**: 20 minutes with 50 images
  - Quick LoRA training for character insertion
  - *From: user*

- **Ovi model steps**: 10 steps
  - Can bring images to life on 5b base model with minimal steps
  - *From: 228118453062467585*

- **VRAM requirement for low-end workflow**: Under 8GB
  - Enables VACE 2.1 usage on consumer hardware
  - *From: 1006234707375173722*

- **LoRA strength**: Low strength
  - Brings subtle Animatediff-y motion enhancement at just 6 steps
  - *From: pom*

- **Training steps for water morphing LoRA**: 1,000 steps
  - Sufficient for training on 6 videos
  - *From: pom*


## Concepts Explained

- **Sliding context windows**: Allows for longer generations in ComfyUI AnimateDiff
  - *From: pom*

- **Prompt travel**: Technique for creating transitions between different prompts in video generation
  - *From: pom*

- **Motion Scale**: A control that allows tuning up and down the amount of motion in video output
  - *From: pom*

- **Attention Masking**: Feature that allows varying IPAdapter mask throughout video for better control
  - *From: matteo*

- **Timestep Scheduling**: Determines which part of sampling process a controlnet should influence
  - *From: Kosinkadink*

- **SparseCtrl**: Video controlnets that provide more grained control than image CNs, optimized for specific video tasks to avoid AD compatibility issues
  - *From: pom*

- **Creative interpolation**: Technique combining IPA with Sparse Ctrl to handle wider gaps and transformations while adhering to input images
  - *From: pom*

- **Video matting implementation**: Technique for separating background and foreground in video processing
  - *From: pom*

- **Motion LoRAs**: Allows training on single video to guide motion of AnimateDiff generation with varying precision levels
  - *From: pom*

- **LoRA travel**: Queuing multiple LoRAs throughout a generation using LoRA masking to achieve different effects throughout video
  - *From: pom*

- **View Options**: Sub-Context Options that act like context window for Contexts to improve stability of longer animations
  - *From: pom*

- **IPA Tiling**: Breaks up input image into multiple components and feeds them one-by-one so IPA has far higher resolution view on what's happening
  - *From: pom*

- **Context Smashing**: Advanced workflow technique for animation control shared by Purz
  - *From: pom*

- **Steerable Motion**: Technique for steering animations with precision using images alongside motion LoRAs
  - *From: pom*

- **AnimatableGaussians**: A paper released for creating animatable content, likely used in viral meme creation
  - *From: pom*

- **Prompt injection**: Injecting different prompts into specific blocks of the unet for more fine-grained motion control
  - *From: pom*

- **Context Aware SparseCtrl**: Implements additional frames that fill in gaps in the context window where there's no Sparse influence for smoother long-context animations
  - *From: pom*

- **Vid2Vid upsampling**: Technique for improving video consistency and reducing context issues
  - *From: Inner Reflections*

- **Audio-reactive passes**: Adding subtle audio-reactive effects to generated videos
  - *From: pom*

- **Veevee (Flatten2)**: Version 2 of Juxtapoz's Flatten vid2vid optical flow technique
  - *From: pom*

- **Multi-phase prompts**: Complex prompts that include scene transitions and camera movements for video generation
  - *From: pom*

- **Transformer morphs**: A type of transformation that current models can't yet do properly
  - *From: pom*

- **VPadapters**: Proposed way to guide videos using reference videos for different components
  - *From: pom*

- **Video Prompt adapter**: Could theoretically allow using reference videos to guide motion like IPAdapter uses reference images
  - *From: pom*

- **Vid2Vid**: Video-to-video transformation/editing technique
  - *From: pom*

- **RF Inversion**: Technique that works well with LTX model for improved vid2vid results
  - *From: pom*

- **Regional prompting**: Technique for applying different prompts to different regions of an image
  - *From: pom*

- **LoRA masking**: New capability enabling selective application of LoRAs to different parts of images
  - *From: pom*

- **Warped Noise**: Netflix technique for guiding video generation, works with various models
  - *From: pom*

- **FlowEdit**: Implementation used for video transformation workflows
  - *From: pom*

- **Context window shifting**: Technique for handling longer video sequences by shifting the processing window
  - *From: kijai*

- **Reward LoRA**: Type of LoRA that improves prompt adherence in video generation
  - *From: community member*

- **Control LoRAs**: LoRAs that can be trained on any condition where you provide input videos and output videos, enabling various types of control like deblurring, inpainting, interpolating, trajectory drawing
  - *From: pom*

- **VACE**: Video generation system that enables fast style transfer and face swapping
  - *From: pom*

- **ATI**: System for trajectory control in video generation
  - *From: pom*

- **Normalized Attention Guidance**: New negative prompting approach that works on distilled models
  - *From: pom*

- **Multitalk**: Technology for mouth movements in AI video generation, particularly good for single subjects
  - *From: pom*

- **LightX2V**: 4-step distillation method for Wan video generation
  - *From: pom*

- **VACE masking**: Technique for precise masking and object manipulation in video generation
  - *From: pom*

- **Sliding context windows**: Technique for generating long videos by using overlapping context segments
  - *From: 228118453062467585*

- **Banostasis**: LoRA that enables unconventional motion styles and reality-breaking effects with Wan
  - *From: 1074404980737450065*

- **Animatediff-y movement**: Distinctive motion style characteristic of Animatediff outputs when combined with other models
  - *From: pom*

- **VACE masking degradation**: Quality degradation issue when using VACE that can be solved with latent noise techniques
  - *From: pom*

- **Context transitions**: Technique for doing scene transformations while maintaining subject consistency
  - *From: pom*

- **IC-LoRA**: Approach for training control mechanisms for LTX2, such as luminance map references for lighting control
  - *From: pom*

- **SVI-Pro**: Tool for Wan 2.2 that may potentially offer path to endless smooth continuations
  - *From: pom*


## Resources & Links

- **Banodoco roadmap** (website)
  - https://banodoco.ai/Roadmap_&_collaboration
  - *From: pom*

- **AD-Evo-Tuner** (repo)
  - https://github.com/B34STW4RS/AD-Evo-Tuner
  - *From: pom*

- **ComfyUI-AnimateDiff** (repo)
  - https://github.com/Kosinkadink/ComfyUI-AnimateDiff
  - *From: pom*

- **AnimateDiff Motion LoRAs** (repo)
  - https://github.com/guoyww/AnimateDiff
  - *From: pom*

- **ComfyUI_FizzNodes** (repo)
  - https://github.com/FizzleDorf/ComfyUI_FizzNodes
  - *From: pom*

- **animatediff-kaiber** (repo)
  - https://github.com/KaiberAI/animatediff-kaiber
  - *From: pom*

- **viddle-pix2pix-animatediff** (model)
  - https://huggingface.co/viddle/viddle-pix2pix-animatediff
  - *From: pom*

- **Inner Reflections Comfy guide** (guide)
  - https://civitai.com/articles/2379/guide-comfyui-animatediff-guideworkflows-including-prompt-scheduling-an-inner-reflections-guide
  - *From: pom*

- **AnimateDiff LoRA training** (repo)
  - https://github.com/tumurzakov/AnimateDiff
  - *From: pom*

- **HotshotXL** (repo)
  - https://github.com/hotshotco/Hotshot-XL
  - *From: pom*

- **Improved 3D Motion Module** (model)
  - https://civitai.com/models/158389/improved-3d-motion-module
  - *From: pom*

- **Temporal-Image model** (model)
  - https://huggingface.co/CiaraRowles/Temporal-Image
  - *From: pom*

- **AnimateDiff Rotoscoping Workflow** (workflow)
  - https://civitai.com/models/158720/animatediff-rotoscoping-workflow
  - *From: pom*

- **SDXL Motion Module beta** (model)
  - https://huggingface.co/guoyww/animatediff/blob/main/mm_sdxl_v10_beta.ckpt
  - *From: pom*

- **SDXL AnimateDiff Guide** (guide)
  - https://civitai.com/articles/2950/guide-comfyui-animatediff-xl-guide-and-workflows-an-inner-reflections-guide
  - *From: 88822364468412416*

- **IPAdapter Plus** (repo)
  - https://github.com/cubiq/ComfyUI_IPAdapter_plus
  - *From: 237937096717762560*

- **AnimateDiff-Evolved repo** (repo)
  - https://github.com/Kosinkadink/ComfyUI-AnimateDiff-Evolved
  - *From: Kosinkadink*

- **Enfugue app** (tool)
  - https://github.com/painebenjamin/app.enfugue.ai
  - *From: 422902797093306368*

- **Crystallee AnimateDiff controlnet** (model)
  - https://huggingface.co/crishhh/animatediff_controlnet/blob/main/controlnet_checkpoint.ckpt
  - *From: crystallee-ai*

- **IPAdapter attention masking tutorial** (tutorial)
  - https://www.youtube.com/watch?v=vqG1VXKteQg
  - *From: 237937096717762560*

- **Advanced ControlNet repo** (repo)
  - https://github.com/Kosinkadink/ComfyUI-Advanced-ControlNet
  - *From: Kosinkadink*

- **Pixar Luxo Jr. short** (reference)
  - https://www.youtube.com/watch?v=FI0T0Oj7WFE
  - *From: pom*

- **AnimatedDiff V3** (model)
  - https://huggingface.co/guoyww/animatediff/tree/cd71ae134a27ec6008b968d6419952b0c0494cf2
  - *From: pom*

- **HarrlogosXL-v2** (model)
  - https://discord.com/channels/1076117621407223829/1186080234131443752
  - *From: HarrowLogo*

- **Matteo's IPA & Comfy tutorials** (tutorial)
  - https://www.youtube.com/watch?v=6i417F-g37s
  - *From: matteo*

- **SVD Temporal ControlNet** (repo)
  - https://github.com/CiaraStrawberry/svd-temporal-controlnet
  - *From: CiaraRowles*

- **SVD Depth ControlNet** (model)
  - https://huggingface.co/CiaraRowles/temporal-controlnet-depth-svd-v1
  - *From: CiaraRowles*

- **ComfyUI-SVD implementation** (repo)
  - https://github.com/kijai/ComfyUI-SVD
  - *From: Kijai*

- **Enfugue with DragNUWA** (tool)
  - https://discord.com/channels/1076117621407223829/1195599969869119578
  - *From: benejamin*

- **ComfyUI-Llama node** (tool)
  - https://github.com/daniel-lewis-ab/ComfyUI-Llama
  - *From: Mr Pebbles*

- **ComfyDeploy** (tool)
  - https://github.com/BennyKok/comfyui-deploy
  - *From: BennyKok*

- **ControlGif ControlNets** (model)
  - https://huggingface.co/crishhh/animatediff_controlnet/tree/main
  - *From: Crriss*

- **Temporal ControlNet Lineart SVD** (model)
  - https://huggingface.co/CiaraRowles/temporal-controlnet-lineart-svd-v1
  - *From: CiaraRowles*

- **Matteo's Comfy guide** (tutorial)
  - https://www.youtube.com/watch?v=_C7kR2TFIX0
  - *From: matteo*

- **AnimateDiff-MotionDirector** (repo)
  - https://github.com/ExponentialML/AnimateDiff-MotionDirector
  - *From: pom*

- **ComfyUI-DragNUWA** (repo)
  - https://github.com/chaojie/ComfyUI-DragNUWA
  - *From: pom*

- **ComfyUI-AnimateAnyone-Evolved** (repo)
  - https://github.com/MrForExample/ComfyUI-AnimateAnyone-Evolved
  - *From: pom*

- **Tiled IP Adapter** (repo)
  - https://github.com/cubiq/ComfyUI_IPAdapter_plus?tab=readme-ov-file#tiled-ipadapter
  - *From: pom*

- **Kijai's Comfy Motion LoRA Trainer** (repo)
  - https://github.com/kijai/ComfyUI-ADMotionDirector
  - *From: pom*

- **Kosinkadink GitHub Sponsors** (funding)
  - https://github.com/sponsors/Kosinkadink
  - *From: pom*

- **Kosinkadink Patreon** (funding)
  - https://www.patreon.com/Kosinkadink/posts
  - *From: pom*

- **Zeroscope in Comfy** (workflow)
  - https://discord.com/channels/1076117621407223829/1212081072620441631
  - *From: pom*

- **Deforum Comfy nodes** (repo)
  - https://github.com/XmYx/deforum-comfy-nodes
  - *From: pom*

- **Deforum Studio** (tool)
  - https://deforum.studio/animate
  - *From: pom*

- **Dough** (tool)
  - https://github.com/banodoco/dough
  - *From: pom*

- **DynamiCrafter Wrapper** (repo)
  - https://github.com/kijai/ComfyUI-DynamiCrafterWrapper
  - *From: pom*

- **Motion LoRAs by cseti** (model)
  - https://huggingface.co/Cseti/AD_Motion_LORAs/tree/main
  - *From: pom*

- **Motion LoRAs collection** (model)
  - https://huggingface.co/collections/PollyannaIn4D/animatediff-motion-modules-65d0eaa7ad23a67404f066bc
  - *From: pom*

- **Composition IP-Adapter** (model)
  - https://huggingface.co/ostris/ip-composition-adapter
  - *From: pom*

- **IP-Adapter node** (repo)
  - https://github.com/cubiq/ComfyUI_IPAdapter_plus
  - *From: pom*

- **Dissolve motion LoRA** (model)
  - https://huggingface.co/benjamin-paine/motion-lora/blob/main/mmv3/adapter/disintegrate_motion_mmv3_adapter_v1.safetensors
  - *From: pom*

- **More camera angles LoRAs** (model)
  - https://huggingface.co/Cseti/AD_Motion_LORAs
  - *From: pom*

- **MotionThief node** (node)
  - https://github.com/logtd/ComfyUI-MotionThiefExperiment
  - *From: logtd*

- **ELLA ComfyUI implementation** (repo)
  - https://github.com/ExponentialML/ComfyUI_ELLA
  - *From: ntialML*

- **Line2NormalMap LoRA** (model)
  - https://huggingface.co/toyxyz/Line2NormalMap_SD1.5
  - *From: toyxyz*

- **Depth map LoRA** (model)
  - https://civitai.com/models/392921
  - *From: fill*

- **AnimatableGaussians paper** (repo)
  - https://github.com/lizhe00/AnimatableGaussians
  - *From: pom*

- **Hanna's first node - queue colours** (node)
  - https://github.com/hannahunter88/anodes
  - *From: hannahunter88*

- **Art Appreciation Wednesday videos** (video)
  - https://www.youtube.com/watch?v=_1oVYIk88CA
  - *From: pom*

- **Art Appreciation Wednesday videos** (video)
  - https://youtu.be/CriBxdP85PU
  - *From: pom*

- **Banodoco Plan document** (document)
  - https://banodoco.ai/Plan
  - *From: pom*

- **Banodoco Ownership details** (document)
  - https://banodoco.ai/Ownership
  - *From: pom*

- **Comfy Python interpreter** (tool)
  - https://github.com/christian-byrne/python-interpreter-node
  - *From: pom*

- **Mobius SDXL fine-tune** (model)
  - https://huggingface.co/Corcelio/mobius
  - *From: pom*

- **Matteo's prompt injection science video** (educational)
  - https://www.youtube.com/watch?v=0ChoeLHZ48M
  - *From: pom*

- **ComfyUI TensorRT tutorial video** (educational)
  - https://www.youtube.com/watch?v=x0-1lAwXHrY
  - *From: pom*

- **ComfyUI_LLMVISION exploit fix instructions** (security)
  - https://www.reddit.com/r/comfyui/comments/1dbls5n/psa_if_youve_used_the_comfyui_llmvision_node_from/?rdt=55362
  - *From: pom*

- **Make your own Anime V1 action pack** (workflow)
  - *From: pom*

- **SDXL Vid2Vid tutorial on Civit Stream** (educational)
  - https://www.youtube.com/watch?v=Wx9TLb95Nh4&t=1755s
  - *From: pom*

- **Project Odyssey Competition** (competition)
  - https://www.projectodyssey.ai/
  - *From: pom*

- **Matteo's style transfer technique video** (educational)
  - https://www.youtube.com/watch?v=ewKM7uCRPUg
  - *From: pom*

- **FLATTEN nodes for vid2vid** (tool)
  - https://github.com/logtd/ComfyUI-FLATTEN/blob/464ebca0c164d6fa735aad5f4b633e704bef5ee3/nodes/flatten_ksampler_node.py#L19
  - *From: pom*

- **reforum** (tool)
  - https://github.com/reallybigname/sd-webui-deforum/tree/reforum
  - *From: pom*

- **Kolor nodes** (repo)
  - https://github.com/kijai/ComfyUI-KwaiKolorsWrapper
  - *From: Kijai*

- **Florence2 nodes** (repo)
  - https://github.com/kijai/ComfyUI-Florence2
  - *From: Kijai*

- **LivePortrait nodes** (repo)
  - https://github.com/kijai/ComfyUI-LivePortraitKJ
  - *From: Kijai*

- **LivePortrait tutorial** (tutorial)
  - https://www.youtube.com/watch?v=zLSfnO0Ob-I&t=341s
  - *From: community member*

- **Animated transitions on Github** (repo)
  - https://github.com/mgfxer/ComfyUI-FrameFX
  - *From: mgfxer*

- **Flux workflow for 12GB VRAM** (workflow)
  - https://civitai.com/posts/5006398
  - *From: Inner Reflections*

- **SAM2 implementation** (repo)
  - https://github.com/kijai/ComfyUI-segment-anything-2
  - *From: Kijai*

- **IP-Adapter-Instruct** (model)
  - https://unity-research.github.io/IP-Adapter-Instruct.github.io/
  - *From: research team*

- **Banodoco social channels** (social)
  - https://twitter.com/banodoco
  - *From: pom*

- **Ostris Flux trainer** (repo)
  - https://github.com/ostris/ai-toolkit?tab=readme-ov-file#flux1-training
  - *From: pom*

- **Promptcrafted Flux training tutorial** (tutorial)
  - https://youtu.be/HzGW_Kyermg?si=m4UIyukh7QCOkzpa
  - *From: pom*

- **ComfyUI-RefUNet** (repo)
  - https://github.com/logtd/ComfyUI-RefUNet
  - *From: pom*

- **ComfyUI-Veevee** (repo)
  - https://github.com/logtd/ComfyUI-Veevee
  - *From: pom*

- **ComfyUI-FluxTrainer** (repo)
  - https://github.com/kijai/ComfyUI-FluxTrainer
  - *From: pom*

- **ComfyUI-Fluxtapoz** (repo)
  - https://github.com/logtd/ComfyUI-Fluxtapoz
  - *From: pom*

- **CogVideoX Comfy nodes** (repo)
  - https://github.com/kijai/ComfyUI-CogVideoXWrapper?tab=readme-ov-file
  - *From: pom*

- **Kijai normal map LoRA** (model)
  - https://huggingface.co/Kijai/kijai-flux-loras/tree/main
  - *From: pom*

- **FlippingSigmas Unsampling Variant** (workflow)
  - https://discord.com/channels/1076117621407223829/1256359746437517412/1275041848888397849
  - *From: pom*

- **32 frame context LoRA** (lora)
  - https://discord.com/channels/1076117621407223829/1286396380172259338
  - *From: pom*

- **Audio Particles with Depth Injection** (tool)
  - https://discord.com/channels/1076117621407223829/1285036655186546778
  - *From: pom*

- **Motion I2V** (model)
  - https://discord.com/channels/1076117621407223829/1289230376602173471
  - *From: pom*

- **SDXL Video2Video Morph workflow** (workflow)
  - https://discord.com/channels/1076117621407223829/1289175216953753643
  - *From: pom*

- **Any Interface by Ibis** (tool)
  - https://discord.com/channels/1076117621407223829/1289231773691019336
  - *From: pom*

- **AudioReactive Playhead** (node)
  - https://discord.com/channels/1076117621407223829/1289702471710544034/1289702471710544034
  - *From: pom*

- **CosyVoice** (model)
  - https://github.com/FunAudioLLM/CosyVoice
  - *From: pom*

- **DepthFlow Custom Nodes** (node)
  - https://discord.com/channels/1076117621407223829/1292406124867354625/1292406124867354625
  - *From: pom*

- **Simple 2 Step Deflicker workflow** (workflow)
  - https://discord.com/channels/1076117621407223829/1290969553232330773
  - *From: pom*

- **Tora for CogVideoX workflow** (workflow)
  - https://discord.com/channels/1076117621407223829/1270190976237047848/1297676788192772270
  - *From: pom*

- **FluxUnsampling** (tool)
  - https://github.com/logtd/ComfyUI-Fluxtapoz
  - *From: pom*

- **CtrlLoRA** (tool)
  - https://github.com/xyfJASON/ctrlora
  - *From: pom*

- **CogVideoX Interpolation** (tool)
  - https://github.com/feizc/CogvideX-Interpolation/tree/main?tab=readme-ov-file
  - *From: pom*

- **AudioSlime nodes** (node)
  - https://discord.com/channels/1076117621407223829/1296878412002099254
  - *From: pom*

- **ComfyUI-MochiWrapper** (tool)
  - https://github.com/kijai/ComfyUI-MochiWrapper
  - *From: pom*

- **Endless Zoom nodes** (node)
  - https://discord.com/channels/1076117621407223829/1300300095639523389/1300300095639523389
  - *From: pom*

- **Audiovisualisers in Comfy** (node)
  - https://discord.com/channels/1076117621407223829/1299485707173101608
  - *From: pom*

- **MochiEdit** (tool)
  - https://github.com/logtd/ComfyUI-MochiEdit
  - *From: pom*

- **Mochi Vid2Vid workflow** (workflow)
  - https://discord.com/channels/1076117621407223829/1298379698874749048/1301762676191399937
  - *From: pom*

- **Audio-reactive interpolation workflow tutorial** (workflow)
  - https://discord.com/channels/1076117621407223829/1307293725352792114
  - *From: pom*

- **In-Context Flux Flora approach** (workflow)
  - https://discord.com/channels/1076117621407223829/1305560447755223130
  - *From: pom*

- **Feature Reactive Live Portrait node** (node)
  - https://discord.com/channels/1076117621407223829/1310236372279492679/1310236372279492679
  - *From: pom*

- **CogVideoX LoRA training best practices** (guide)
  - https://discord.com/channels/1076117621407223829/1307828124255391825/1310357753490964561
  - *From: pom*

- **Flux Regional Prompting node by Juxtapox** (repo)
  - https://github.com/attashe/ComfyUI-FluxRegionAttention
  - *From: pom*

- **LTX vid2vid with image reference workflow** (workflow)
  - https://discord.com/channels/1076117621407223829/1309520535012638740/1312204860648853506
  - *From: pom*

- **LTX Image2Vid workflow** (workflow)
  - https://discord.com/channels/1076117621407223829/1311675870511108187
  - *From: pom*

- **StyleMatch-Flux workflow** (workflow)
  - https://discord.com/channels/1076117621407223829/1311982636582830100
  - *From: pom*

- **Arcane LoRA by Cseti** (lora)
  - https://discord.com/channels/1076117621407223829/1310686485120421889
  - *From: pom*

- **Flux LoRA by user** (lora)
  - https://civitai.com/models/930359
  - *From: pom*

- **CogVideoX vid2vid workflow** (workflow)
  - https://github.com/kijai/ComfyUI-CogVideoXWrapper/tree/main/examples
  - *From: pom*

- **ComfyUI blog post on LoRA masking and scheduling** (guide)
  - https://blog.comfy.org/masking-and-scheduling-lora-and-model-weights/
  - *From: pom*

- **Depth + Redux workflow** (workflow)
  - https://gist.github.com/nathanshipley/7a9ac1901adde76feebe58d558026f68
  - *From: pom*

- **Flux style shaping HuggingFace space** (tool)
  - https://huggingface.co/spaces/multimodalart/flux-style-shaping
  - *From: pom*

- **HunYuan LoRA trainer by TD Russell** (repo)
  - https://github.com/tdrussell/diffusion-pipe
  - *From: pom*

- **Jinx from Arcane LoRA by Cseti** (lora)
  - https://discord.com/channels/1076117621407223829/1317951471391608913
  - *From: pom*

- **This is fine meme HunYuan Video LoRA** (lora)
  - https://civitai.com/models/1035870/this-is-fine-meme-hunyuan-video-lora?modelVersionId=1161881
  - *From: pom*

- **Warped Noise technique by Netflix** (repo)
  - https://github.com/VGenAI-Netflix-Eyeline-Research/Go-with-the-Flow
  - *From: pom*

- **AnimateDiff Warped Noise MotionLoRA** (model)
  - https://huggingface.co/spacepxl/animatediffv3_warpednoise_motionlora
  - *From: pom*

- **MotionVideoSearch by Ian** (tool)
  - https://github.com/IDGallagher/MotionVideoSearch
  - *From: pom*

- **ComfyUI Christmas Theme** (tool)
  - https://github.com/AEmotionStudio/ComfyUI-ChristmasTheme
  - *From: pom*

- **ComfyUI Environment Manager** (node)
  - https://github.com/akatz-ai/ComfyUI-Environment-Manager
  - *From: pom*

- **BNDC Engine code** (repo)
  - https://github.com/peteromallet/bndc-engine
  - *From: pom*

- **Discord Summary Bot** (repo)
  - https://github.com/peteromallet/discord_summary_bot/tree/main
  - *From: pom*

- **CogVideoX VidVid Tutorial** (tutorial)
  - https://www.youtube.com/watch?v=gHI6PjTkBF4
  - *From: pom*

- **HunYuan unofficial Img2Vid LoRA** (model)
  - https://huggingface.co/leapfusion-image2vid-test/image2vid-960x544/blob/main/img2vid544p.safetensors
  - *From: leapfusion*

- **ComfyUI-ColorshiftColor nodes** (tool)
  - https://github.com/852wa/ComfyUI-ColorshiftColor/
  - *From: community member*

- **Video-Depth-Anything** (repo)
  - https://github.com/DepthAnything/Video-Depth-Anything
  - *From: community*

- **ComfyUI Video-Depth-Anything nodes** (tool)
  - https://github.com/yuvraj108c/ComfyUI-Video-Depth-Anything
  - *From: community member*

- **Sonic ComfyUI implementation** (tool)
  - https://github.com/smthemex/ComfyUI_Sonic
  - *From: community member*

- **Zonos Longform Unleashed HuggingFace space** (tool)
  - https://huggingface.co/spaces/benjamin-paine/zonos-longform-unleashed
  - *From: community member*

- **Boring Reality Hunyuan LoRA** (model)
  - https://huggingface.co/kudzueye/boreal-hl-v1
  - *From: community member*

- **ADOS Paris event** (event)
  - https://lu.ma/cd76ktg2
  - *From: pom*

- **WanTraining** (repo)
  - https://github.com/spacepxl/WanTraining
  - *From: spacepxl*

- **Steamboat Willie LoRA** (model)
  - https://huggingface.co/benjamin-paine/steamboat-willie-14b
  - *From: benjamin-paine*

- **Studio Ghibli Style LoRA** (model)
  - https://civitai.com/models/1404755/studio-ghibli-style-wan21-t2v-14b
  - *From: community member*

- **OpenMuse platform** (tool)
  - https://openmuse.ai/
  - *From: pom*

- **Wallace & Gromit LoRA** (model)
  - https://huggingface.co/Cseti/LTXV-13B-LoRA-Wallace_and_Gromit-v1
  - *From: community member*

- **MatAnyone Comfy implementation** (workflow)
  - *From: community member*

- **VACE Module 14B fp8** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/blob/main/Wan2_1-VACE_module_14B_fp8_e4m3fn.safetensors
  - *From: Kijai*

- **Causvid Lora** (lora)
  - https://huggingface.co/Kijai/WanVideo_comfy/blob/main/Wan21_CausVid_14B_T2V_lora_rank32.safetensors
  - *From: Kijai*

- **ATI workflow** (workflow)
  - https://github.com/kijai/ComfyUI-WanVideoWrapper/blob/main/example_workflows/wanvideo_ATI_testing_01.json
  - *From: Adrien*

- **OpenMuse platform** (platform)
  - https://openmuse.ai/
  - *From: pom*

- **Sprout LoRA** (lora)
  - https://openmuse.ai/assets/loras/59cd019a-c227-41a5-bf6f-1258481e1826
  - *From: user*

- **Red Line LoRA** (lora)
  - https://civitai.com/models/1517145/redline-wan21-t2v-14b
  - *From: user*

- **NormalCrafter wrapper** (tool)
  - *From: user*

- **Replicate Wan LoRA trainer** (tool)
  - https://replicate.com/ostris/wan-lora-trainer/train
  - *From: user*

- **NotebookLM Wan knowledge chat** (tool)
  - https://notebooklm.google.com/notebook/a08901b9-0511-4926-bbf8-3c86a12dc306
  - *From: Nathan*

- **Adrien's tutorial series** (tutorial)
  - https://youtu.be/0cw2N3W7nKo?si=1z2PjaN3ri0chzlH&t=43
  - *From: Adrien*

- **Wan21_T2V_14B_lightx2v_cfg_step_distill_lora_rank32.safetensors** (lora)
  - https://huggingface.co/Kijai/WanVideo_comfy/blob/main/Wan21_T2V_14B_lightx2v_cfg_step_distill_lora_rank32.safetensors
  - *From: pom*

- **ComfyUI-WanVideoWrapper multitalk experimental branch** (repo)
  - https://github.com/kijai/ComfyUI-WanVideoWrapper/tree/multitalk
  - *From: pom*

- **Nekodificador's VFX Tools for Vace** (tool)
  - https://discord.com/channels/1076117621407223829/1384931026740056084
  - *From: pom*

- **Adrien's in-depth VACE x ATI Tutorial** (tutorial)
  - https://www.youtube.com/watch?v=7YmiJxPEMk0
  - *From: pom*

- **Wan Chatbot updated** (tool)
  - https://discord.com/channels/1076117621407223829/1385091877786878074
  - *From: pom*

- **Multitalk deep dive on Creative Explorations** (tutorial)
  - https://www.youtube.com/watch?v=YLFPxm4U4vg
  - *From: pom*

- **Continuation workflow** (workflow)
  - https://discord.com/channels/1076117621407223829/1386453178240733235
  - *From: pom*

- **Official Multitalk workflow with context windows** (workflow)
  - https://github.com/kijai/ComfyUI-WanVideoWrapper/blob/main/example_workflows/wanvideo_multitalk_test_context_windows_01.json
  - *From: pom*

- **Native Deforum in ComfyUI** (tool)
  - https://discord.com/channels/1011314943380959313/1012726643216887890/1389294949509365841
  - *From: pom*

- **ComfyDock Discord** (tool)
  - https://discord.gg/RDkKxRhuc9
  - *From: pom*

- **LTXV training script** (repo)
  - https://github.com/Lightricks/LTX-Video-Trainer
  - *From: pom*

- **Pusa** (tool)
  - https://yaofang-liu.github.io/Pusa_Web/
  - *From: pom*

- **Kontext LoRA for in-scene images** (lora)
  - https://discord.com/channels/1076117621407223829/1395791303639564348/1395791303639564348
  - *From: pom*

- **Pusa workflow for smooth continuations** (workflow)
  - https://discord.com/channels/1076117621407223829/1386453178240733235/1398123737257083032
  - *From: 217815920981049355*

- **Comfycast deep-dive into Wan morphing** (tutorial)
  - https://www.youtube.com/watch?v=lPMhXfNne0E
  - *From: Purz*

- **Reigh tool** (tool)
  - https://reigh.art/
  - *From: pom*

- **Comfy livecast** (livestream)
  - https://www.youtube.com/watch?v=V7oINf8wVjw
  - *From: pom*

- **Beautifully optimised image generator and upscaler for Wan 2.2** (workflow)
  - https://discord.com/channels/1076117621407223829/1401393279790088213
  - *From: 867727155499499520*

- **Fun-Control controlnets for Wan 2.2** (model)
  - https://github.com/kijai/ComfyUI-WanVideoWrapper/tree/main/fantasyportrait
  - *From: Kijai*

- **FakeVace2.2 merge** (model)
  - https://discord.com/channels/1076117621407223829/1402796376932220998
  - *From: 771193439399444490*

- **Crispy upscaler for Wan 2.2** (workflow)
  - https://discord.com/channels/1076117621407223829/1402222216787132526
  - *From: 683646399761350695*

- **Chattable Wan Knowledge base** (knowledge base)
  - https://discord.com/channels/1076117621407223829/1385091877786878074
  - *From: 614602980943069214*

- **Inner Reflections Phantom VACE merge** (model)
  - https://discord.com/channels/1076117621407223829/1403263501421776977
  - *From: 88822364468412416*

- **Aniwan workflow for beautiful transitions** (workflow)
  - https://discord.com/channels/1076117621407223829/1404522024117862520
  - *From: 1081570872994824212*

- **Refined Fun-Control workflow** (workflow)
  - https://discord.com/channels/1076117621407223829/1396263390296674324/1405608908147658855
  - *From: 224611423869730818*

- **HunyuanFoley Comfy nodes** (nodes)
  - https://discord.com/channels/1076117621407223829/1410762212024254545
  - *From: 983060020516249670*

- **QwenEdit style-reference LoRA** (lora)
  - https://discord.com/channels/1076117621407223829/1411067244141744148
  - *From: pom*

- **Pusa integration workflow** (workflow)
  - https://discord.com/channels/1076117621407223829/1342763350815277067/1412941121545568387
  - *From: pom*

- **FakeVace 2.2 continuations workflow** (workflow)
  - https://discord.com/channels/1076117621407223829/1386453178240733235/1412948738439118898
  - *From: pom*

- **Wan 2.2 upscaling workflow** (workflow)
  - https://discord.com/channels/1076117621407223829/1342763350815277067/1413545261027950682
  - *From: pom*

- **Advanced VACE nodes** (repo)
  - https://github.com/drozbay/ComfyUI-WanVaceAdvanced
  - *From: 256636116763934731*

- **Huggingface AI Toolkit training** (tool)
  - https://huggingface.co/spaces/multimodalart/ai-toolkit
  - *From: pom*

- **VACE sampling comparison tests** (tool)
  - https://drozbay.github.io/WanTests/VaceTests/vace_results1_distill_sampler_tests.html
  - *From: 256636116763934731*

- **Chattable Knowledge Base** (tool)
  - https://discord.com/channels/1076117621407223829/1385091877786878074
  - *From: 614602980943069214*

- **Arca Gidan Prize website** (competition)
  - https://arcagidan.com/
  - *From: pom*

- **Competition Discord** (community)
  - https://discord.com/invite/Yj7DRvckRu
  - *From: pom*

- **Real Time Video Summit** (event)
  - https://realtime-video-ai-summit.com/
  - *From: pom*

- **ADOS LA event** (event)
  - https://ados.events/
  - *From: pom*

- **Exploded effect LoRA** (model)
  - https://huggingface.co/Ashmotv/exploded_effect_wan
  - *From: pom*

- **Alexander Morano obituary** (memorial)
  - https://www.dignitymemorial.com/obituaries/richmond-va/alexander-morano-12537385
  - *From: pom*

- **Daydream hackathon** (event)
  - https://daydream.live/interactive-ai-video-program
  - *From: pom*

- **SCAIL tool** (tool)
  - *From: 456226577798135808*

- **Flux 2 trained model** (model)
  - https://www.patreon.com/posts/145298480
  - *From: 755177709071630441*

- **Black and white replication workflow** (workflow)
  - https://discord.com/channels/1076117621407223829/1344057524935983125/1453792629748666378
  - *From: 256636116763934731*

- **Music video workflow** (workflow)
  - https://discord.com/channels/1076117621407223829/1417710283945672764/1452073502969561301
  - *From: 330829305477333022*

- **Reigh tool** (tool)
  - https://reigh.art/home
  - *From: pom*

- **Audio-based video generation workflow** (workflow)
  - https://discord.com/channels/1076117621407223829/1309520535012638740/1458585393950752982
  - *From: 228118453062467585*

- **NotebookLM Knowledge Base for LTX** (resource)
  - https://notebooklm.google.com/notebook/4f07f98c-75b6-4278-bde1-906f9899b60c
  - *From: 614602980943069214*

- **Awesome-ltx2 GitHub list** (repo)
  - https://github.com/wildminder/awesome-ltx2
  - *From: 722168850786943138*

- **ADOS Events website** (resource)
  - https://ados.events/
  - *From: 1061984538332516392*

- **Banodoco website** (resource)
  - https://www.banodoco.ai/
  - *From: pom*

- **SharkSampler workflow for LTX-2** (workflow)
  - https://discord.com/channels/1076117621407223829/1457981813120176138/1461011216578248907
  - *From: 256636116763934731*

- **VibeComfy toolset** (tool)
  - https://discord.com/channels/1076117621407223829/1464312809624965245
  - *From: pom*

- **Humo x Wan 2.2 SVI workflow** (workflow)
  - https://discord.com/channels/1076117621407223829/1455601193660452995
  - *From: 256636116763934731*

- **Automated image-to-video pipeline** (workflow)
  - https://discord.com/channels/1076117621407223829/1463747305802043423
  - *From: 330829305477333022*


## Known Limitations

- **Background tends to be very chaotic in AD**
  - Jumps all over the place with main subjects
  - *From: pom*

- **A1111 extension is broken with loads of issues in various repos**
  - Reduces friction for experimentation
  - *From: pom*

- **SVD less modular approach**
  - Lacks 1.5-esque ecosystem, less certain it will experience improvements for fine-grained motion control like vid2vid and creative interpolation
  - *From: pom*

- **SVD chaining challenges**
  - Challenge is getting consistent movement and lowering degradation across generations
  - *From: 499629400254447616*

- **AD face jittering**
  - AnimateDiff often produces jittery faces that need post-processing with tools like FaceDetailer
  - *From: 750969956249632859*

- **DragNUWA object understanding**
  - Frequently doesn't understand object nature, resulting in weird transformations
  - *From: whobody*

- **DragNUWA can't reveal hidden content**
  - Cannot reveal hidden secrets in artworks as demonstrated
  - *From: Kijai*

- **Steerable Motion 1.1 issues**
  - Still difficult to control, motion can be jerky, color issues persist
  - *From: pom*

- **SVD 1.1 still suffers from inconsistency and degradation throughout frames**
  - Small improvement but core issues remain
  - *From: pom*

- **DynamiCrafter struggles outside anime and realistic styles**
  - Can be unpredictable generally and may not be very extensible, doesn't have ecosystem to build on
  - *From: pom*

- **DynamiCrafter based on SD 2.1**
  - Has limited ecosystem of supporting models and tools
  - *From: pom*

- **Video upscaling has speed problems**
  - Current upscaling workflows have performance issues that need addressing
  - *From: pom*

- **Tooncrafter can be inflexible and breaks easily, especially with characters in in-between movements**
  - Based on 2.1 so limited other models like IP-Adapters available to control it
  - *From: pom*

- **LivePortrait not perfect**
  - While impressive, still has imperfections in facial animation
  - *From: pom*

- **Context issues in video generation**
  - Various models struggle with context consistency, though upsampling helps
  - *From: Inner Reflections*

- **CogVideoX may not be great for extending**
  - Despite having good realistic motion, it has limitations for extension use cases
  - *From: pom*

- **CogVideoX can't yet do transformer morphs**
  - Has issues with lack of guidance and motion breaking up
  - *From: pom*

- **Driving motion with specificity is difficult**
  - While it does good prompting, precise motion control is challenging
  - *From: pom*

- **CogVideoX fragmented ecosystem**
  - LoRAs and CNs work with different versions and licenses on different models
  - *From: pom*

- **CogVideoX doesn't plug into existing ecosystem**
  - Unlike AnimateDiff which could leverage SD1.5 ecosystem
  - *From: pom*

- **CogVideoX deals with unconventional styles weirdly**
  - Though could likely be fixed with IPA
  - *From: pom*

- **CogVideoX Non-Commercial Licensing on 5B model**
  - Licensing restriction
  - *From: pom*

- **Motion I2V limited to 16 frames**
  - Still based on AnimateDiff
  - *From: pom*

- **LTXV breaks down frequently and is overly sensitive to prompting**
  - Despite speed advantages, the model has reliability issues
  - *From: pom*

- **Mochi lacks specific control despite impressive generation capabilities**
  - Can generate amazing content locally but control methods are limited
  - *From: pom*

- **Omnigen is very slow despite impressive results**
  - Promising for image editing and combining elements but speed is a major limitation
  - *From: pom*

- **Wan takes 5+ minutes to run**
  - Only best used for tasks requiring cohesive motion, other models better for specific tasks
  - *From: pom*

- **txt2vid and img2vid have very limited control**
  - Even with powerful prompting, control perspective is very limited
  - *From: pom*

- **Multitalk currently works for single subjects only**
  - On experimental branch, limited to single subject applications
  - *From: pom*

- **Kontext LoRA for in-scene images not perfect**
  - Described as 'not perfect but personally find it useful + significantly better than base Kontext'
  - *From: pom*

- **WanAnimate multicharacter support**
  - Out of the box doesn't handle multiple characters in same scene
  - *From: pom*

- **Huggingface training time limits**
  - Only supports runs up to 6 hours, longer projects need special permissions
  - *From: pom*

- **No mid-training sample support**
  - Current Huggingface integration doesn't show training progress samples
  - *From: pom*

- **Motion speed issues with distilled Wan**
  - One of the biggest problems with distilled Wan is motion speed
  - *From: pom*

- **InScene LoRAs inconsistency**
  - InScene and InScene Annotate LoRAs are a little inconsistent for complex tasks
  - *From: pom*

- **Stable Video Infinity breaks need ironing out**
  - Early experiments with Stable Video Infinity for Wan continuations have breaks that need to be fixed
  - *From: pom*

- **Anti-Flux 2 biases mentioned**
  - User expressed having anti-Flux 2 biases despite acknowledging unique results
  - *From: pom*


## Hardware Requirements

- **Compute resources**
  - $8k in compute credits offered for ambitious experiments
  - *From: pom*

- **LCM processing speed**
  - 2,467 frames processed in 81 minutes using LCM LoRAs with AnimateDiff
  - *From: CoffeeVectors*

- **Competition prize**
  - 2 NVIDIA 4090s offered as prizes for IP-Adapter competition
  - *From: Glif*

- **Motion LoRA training speed**
  - Can train MotionLora on single video in around 15 minutes
  - *From: pom*

- **AnimateLCM generation speed**
  - LoRA guided video generated in just 3 seconds
  - *From: pom*

- **Bounty posted for getting Superbadass upscalers working with less RAM on 4090**
  - Current upscalers require too much RAM for 4090 usage
  - *From: pom*

- **Flux VRAM**
  - Can run on 12GB VRAM with specific workflow
  - *From: Inner Reflections*

- **VRAM for HyperFlux workflow**
  - Works with less than 8gb VRAM for inpainting and upscaling
  - *From: Akumetsu971*

- **CogVideoX 5B VRAM**
  - Can run on as low as 12GB VRAM and do 51 frames of context
  - *From: pom*

- **Tora for CogVideoX VRAM**
  - Works in Comfy with just 16GB VRAM
  - *From: pom*

- **Moshi optimization**
  - Optimized from requiring 4x h100s to running on local GPUs
  - *From: pom*

- **4090 GPU can run Huanyuan video model**
  - Open source model capable of producing high-quality clips on consumer GPU
  - *From: pom*

- **HunYuan VRAM requirement**
  - Can run on just 12GB VRAM with specific workflow
  - *From: pom*

- **LTXV 0.9.5 performance**
  - 3600 frames/min processing speed
  - *From: pom*

- **GPU for Control LoRA training**
  - 3090 can train SOTA deblurring Control LoRA in under a day
  - *From: pom*

- **VRAM reduction with Clownshark's method**
  - 4GB VRAM reduction while maintaining quality
  - *From: pom*

- **H100 access for training**
  - Beta testers have access to H100 GPUs for training
  - *From: pom*

- **VRAM for low-end VACE workflow**
  - Under 8GB VRAM sufficient for VACE 2.1 workflow
  - *From: 1006234707375173722*

- **InfiniteTalk performance**
  - 2000 frames rendered in 12 minutes using sliding context windows
  - *From: 228118453062467585*

- **Wan 2.2 upscaling time**
  - 20 minutes for upscaling using Ultimate SD
  - *From: 153803064858378240*

- **RTX 4090 performance**
  - Humo X VACE can replicate expensive music video effects on a 4090
  - *From: 256636116763934731*

- **RTX 3090 compatibility**
  - LTX-2 can run impressively on a 3090 GPU
  - *From: 865676776058126386*


## Community Creations

- **AD-Evo-Tuner** (tool)
  - Local AnimateDiff motion fine-tuning tool
  - *From: B34STW4RS*

- **ComfyUI-AnimateDiff extension** (node)
  - ComfyUI extension for AnimateDiff with sliding context windows
  - *From: Kosinkadink*

- **Motion LoRAs** (lora)
  - LoRAs for AnimateDiff camera movements and motion control
  - *From: Ceyuan Yang & Yuwei Guo*

- **Improved 3D Motion Module** (model)
  - Fine-tuned AD-15-v2 for better 3D object movement understanding
  - *From: manshoety*

- **HotshotXL** (model)
  - SDXL version of AnimateDiff trained on 8 frames
  - *From: hotshotco*

- **Temporal-Image** (model)
  - AnimateDiff retrained on SD inpainting model for consistent starting images
  - *From: CiaraRowles*

- **Creative Interpolation node** (node)
  - Allows providing batch of images and interpolating between them with varying strength, duration and position
  - *From: 301463647895683072*

- **Robust Video Matting implementation** (node)
  - Create video mattes segmenting input videos
  - *From: 310003312936091650*

- **VisionWeaver GPT** (tool)
  - GPT for creating prompt travel instructions based on input
  - *From: 712453331959808002*

- **ChatGPT Batch prompter** (tool)
  - Batch prompter for animatediff/Hotshot
  - *From: 706657865229664266*

- **SparseCtrl Comfy implementation** (node)
  - Implementation of video controlnets for AnimatedDiff in Comfy
  - *From: Kosinkadink*

- **SVD Temporal ControlNet Depth** (model)
  - First controlnet for Stable Video Diffusion
  - *From: CiaraRowles*

- **IP-Adapter-Plus nodes** (node)
  - Enhanced IP-Adapter implementation with FaceID support
  - *From: matteo*

- **HarrlogosXL-v2** (lora)
  - Logo generation LoRA with video animation capabilities
  - *From: HarrowLogo*

- **Magnifake workflows** (workflow)
  - Community alternative to expensive Magnific upscaling service
  - *From: Fictiverse*

- **PoseDuplicator script** (tool)
  - Script for programmatically manipulating ControlNets with poses
  - *From: Polyanna*

- **CSSR upscaler Comfy implementation** (node)
  - Realistic upscaling implementation for Comfy
  - *From: Kijai*

- **Retro videogame upscaler** (tool)
  - Specialized upscaler for retro game graphics
  - *From: Impact Frames*

- **Steerable Motion 1.1** (workflow)
  - Creative interpolation combining IPA with Sparse Ctrl
  - *From: pom*

- **ControlGif video ControlNets** (model)
  - Series of video ControlNets for AnimatedDiff improving vid2vid consistency
  - *From: Crriss*

- **Militant Hitchhiker's ControlNet Video Builder** (workflow)
  - Turns any video input into portable, transferable, and manageable ControlNet videos
  - *From: pom*

- **DragNUWA Comfy integration** (node)
  - Comfy integration for DragNUWA by Chaojie
  - *From: pom*

- **AnimateAnyone-Evolved** (implementation)
  - High-quality Comfy implementation of AnimateAnyone by Mr Example
  - *From: pom*

- **Tiled IP Adapter** (node)
  - Experimental solution for IP adapter issues on non-square images by Matteo
  - *From: pom*

- **Motion LoRA Army** (repository)
  - Open database of Motion LoRAs that anyone can contribute to and use
  - *From: pom*

- **Proteus 0.4** (model)
  - Model by DataVoid aiming for Midjourney quality with SDXL base architecture and mixture of experts approach
  - *From: pom*

- **3D rotation motion LoRA** (lora)
  - Motion LoRA for 3D rotation camera movements
  - *From: cseti*

- **Bubbling liquids LoRA** (lora)
  - Motion LoRA for bubbling liquid effects
  - *From: nopeburger*

- **Ants LoRA** (lora)
  - Motion LoRA featuring ant movements
  - *From: PollyannaIn4D*

- **Explosive LoRA** (lora)
  - LoRA that makes everything explodey
  - *From: nopeburger*

- **Bouncing motion LoRA** (lora)
  - LoRA for bouncing motion effects
  - *From: community member*

- **Dissolve effect LoRA** (lora)
  - Beautiful dissolve effect motion LoRA
  - *From: benjamin*

- **Composition IP-Adapter** (model)
  - Controls structure of image with guidance image with beautiful subtlety
  - *From: Ostirs*

- **Auto-prompting nodes** (node)
  - ImpactFrames auto-prompting nodes for Comfy
  - *From: ImpactFrames*

- **LLM nodes for Comfy** (node)
  - Nodes for prompt enhancement and local assistant functionality
  - *From: community members*

- **Lightning SDXL Upscaler** (workflow)
  - High-quality upscaling using new models like Lightning and SDXL Tile
  - *From: Andro-Meta*

- **img2parallax animation workflow** (workflow)
  - Creates parallax animations from still image input
  - *From: Jack G*

- **Delusions LCM 1.5** (model)
  - SD1.5 model trained on Fill's generations
  - *From: Fill*

- **WAS26 motion LoRA** (lora)
  - LoRA trained on weekly art sharing posts that smooths out motion generally
  - *From: pom*

- **MotionThief node** (node)
  - Allows transplanting motion from one video onto AD generation
  - *From: logtd*

- **Line2NormalMap LoRA** (lora)
  - Makes normal maps
  - *From: toyxyz*

- **Depth map LoRA** (lora)
  - Makes depth maps
  - *From: fill*

- **Queue colours node** (node)
  - Overlay colour effects into selected frames
  - *From: hannahunter88*

- **ELLA ComfyUI implementation** (node)
  - ComfyUI implementation of ELLA
  - *From: ntialML*

- **Motion LoRAs collection** (lora)
  - Various movement motion loras
  - *From: diffusemotion*

- **Organic and morphology LoRAs** (lora)
  - Organic and morphology focused motion loras
  - *From: nitrosocke*

- **Spline editor for ComfyUI** (tool)
  - Major UX update adding spline editing capabilities
  - *From: kijai*

- **Comfy Python interpreter** (node)
  - Python interpreter for ComfyUI
  - *From: christian-byrne via pom*

- **Prompt injection nodes** (node)
  - Allow injecting different prompts into specific blocks of the unet for fine-grained motion control
  - *From: Datavoid via pom*

- **AnyNode** (node)
  - Uses LLMs to write code that's executed as a node - custom node functionality written by LLMs
  - *From: pom*

- **Deforum's audio-synced masks tool** (tool)
  - Generates audio-synced masks for animations with flexible and interesting results
  - *From: deforum team via pom*

- **Music Visualiser Megaflow** (workflow)
  - Audioreactive flow that doesn't require input video with flexible approach
  - *From: audioreactive user via pom*

- **Comfy Helper nodes** (node)
  - Add capabilities like controlling parameters with text, viewing meta-data, and more
  - *From: TwoPikachus via pom*

- **FLATTEN nodes** (node)
  - New optical flow technique for improved vid2vid performance, achieving near perfect lip-syncing
  - *From: Juxtabox via pom*

- **Animatediff Weights 2.0** (workflow)
  - Automatically creates masks for animating through videos with BLIP captioning for auto-captioning
  - *From: mgfxer*

- **Motion LoRAs** (lora)
  - Walking motion LoRA upgraded, generalizes across different camera positions. Working towards full set of basic motions
  - *From: Cseti*

- **Basic Camera Motion Lora** (lora)
  - Motion loras for zooming, panning, and more camera movements
  - *From: Cseti*

- **AudioReactive Nodes** (node)
  - Adds various types of effects and schedulers on top of existing audioreactive nodes
  - *From: Fai*

- **Local Audio reactive mask generator** (tool)
  - 3D shape generating audio-reactive mask creator
  - *From: community member*

- **Image Upscaler** (tool)
  - Epic image upscaler with insane level of detail and near-perfect adherence to input image
  - *From: Relic*

- **Flux fine tune** (model)
  - First fine tune using Flux
  - *From: community member*

- **Flux prompt enhancer** (tool)
  - Tool for enhancing prompts for Flux
  - *From: community member*

- **Flux prompt generator** (tool)
  - Tool for generating prompts for Flux
  - *From: community member*

- **Flux prompt mixer** (tool)
  - Tool for mixing prompts for Flux
  - *From: community member*

- **General Improved Motion LoRA** (lora)
  - Provides generally better motion to Animatediff v2
  - *From: Cseti*

- **MEAT Flux LoRA** (lora)
  - Flux LoRA focusing on meat/food themes
  - *From: Jeru*

- **HideThePain Harold LoRA** (lora)
  - LoRA trained on Hide the Pain Harold meme
  - *From: Jeru*

- **Particle simulation nodes** (node)
  - Custom nodes for particle simulations inside ComfyUI
  - *From: ryanontheinside*

- **Directory Browser Nodes** (node)
  - Visual image browsing/selection feature for ComfyUI
  - *From: Fill*

- **Flux Block LoRA selector** (node)
  - Node for exploring different layers of LoRA training
  - *From: Klinter*

- **Reactive IPA weights nodes** (node)
  - Nodes for controlling IPA with features extracted from audio
  - *From: ryanontheinside*

- **Multi-Player Comfy** (node)
  - Custom node that allows live collaboration on top of ComfyUI
  - *From: Daxton Caylor*

- **Proximity Driven Depth nodes** (node)
  - Nodes that allow using proximity of an object as driver for depth
  - *From: ryanontheinside*

- **32 frame context LoRA** (lora)
  - LoRA trained on 32 frame context to defeat AnimatedDiff context switching
  - *From: pom*

- **Audio Particles with Depth Injection** (tool)
  - Capability to inject particles based on audio based on depth
  - *From: pom*

- **Any Interface** (tool)
  - Open source tool to build interface with natural language
  - *From: pom*

- **AudioReactive Playhead** (node)
  - Node that uses audio and features to modulate video playback direction
  - *From: pom*

- **DepthFlow Custom Nodes** (node)
  - Nodes to rapidly generate 3d videos from images
  - *From: pom*

- **Simple 2 Step Deflicker** (workflow)
  - Deflickering workflow
  - *From: pom*

- **FluxUnsampling** (tool)
  - Unsampling with Flux implementing RF inversion paper ideas
  - *From: pom*

- **AudioSlime nodes** (node)
  - Audio-based nodes
  - *From: pom*

- **Depthcrafter Nodes** (node)
  - Nodes for depth processing
  - *From: pom*

- **Endless Zoom nodes** (node)
  - Nodes for zooming through batches of images with interesting effect
  - *From: pom*

- **Audioreactive Vid2Vid nodes** (node)
  - Audio-reactive video-to-video processing
  - *From: pom*

- **Audiovisualisers in Comfy** (node)
  - Windows Media Player style visualizations with diffusion
  - *From: pom*

- **Glitch nodes** (node)
  - Upcoming glitch effect nodes
  - *From: pom*

- **MochiEdit** (tool)
  - Video editing for Mochi using RF-Inversion method
  - *From: pom*

- **Audio-reactive denoising masks** (node)
  - Enables audio-reactive visual effects through denoising masks
  - *From: pom*

- **Depth Aware Audio Reactive Particle Systems** (node)
  - Advanced audio-reactive particle system with depth awareness
  - *From: pom*

- **Audio-reactive interpolation nodes by Yvann & Liliens** (node)
  - Enables audio-reactive traveling between images
  - *From: pom*

- **Feature Reactive Live Portrait node** (node)
  - Uses audio characteristics to control LivePortrait
  - *From: pom*

- **Flux Regional Prompting node** (node)
  - Enables regional prompting capabilities for Flux model
  - *From: pom*

- **Arcane LoRA** (lora)
  - Trained to reproduce Arcane animation style, demonstrates promise of new generation models for animation styles
  - *From: pom*

- **CogVideoX extensions compatibility chart** (tool)
  - Useful chart showing compatibility between various CogVideoX extensions
  - *From: pom*

- **Audioreactivity workflow built on Yvann's system** (workflow)
  - Extended workflow built on top of existing audioreactive interpolation tools
  - *From: pom*

- **HelloMemeV2 & Meme Avatar nodes** (node)
  - Avatar generation nodes
  - *From: pom*

- **Ryanontheinside nodes v2** (node)
  - Improved performance audioreactive nodes with wide range of improvements
  - *From: pom*

- **ComfyUI Environment Manager** (node)
  - Manages Comfy environments to eliminate install anxiety
  - *From: pom*

- **ComfyUI Christmas Theme** (theme)
  - Christmas theme for ComfyUI
  - *From: pom*

- **BNDC summary bot** (bot)
  - Bot that summarizes Discord channels and aims to capture open source AI art knowledge
  - *From: pom*

- **MotionVideoSearch** (tool)
  - Search 100k+ reference videos using embeddings to find similar videos
  - *From: pom*

- **HunYuan walking LoRA** (lora)
  - LoRA for training specific walking motions
  - *From: pom*

- **HunYuan Img2Vid LoRA** (lora)
  - Allows for img2vid functionality with HunYuan
  - *From: leapfusion*

- **Reward LoRA for Hunyuan** (lora)
  - Improves prompt adherence significantly
  - *From: community member*

- **GoWithTheFlow LoRA for Hunyuan** (lora)
  - Allows controlling Vid2Vid by shaping motion through noise control
  - *From: community member*

- **Boring Reality Hunyuan LoRA** (lora)
  - Creates distinct motion characteristics different from standard img2vid
  - *From: community member*

- **Arcane LoRA for Wan** (lora)
  - One of the first Wan LoRAs shared
  - *From: community member*

- **ComfyUI ColorshiftColor nodes** (node)
  - Nodes for swapping color palettes in videos
  - *From: community member*

- **Video-Depth-Anything ComfyUI nodes** (node)
  - ComfyUI implementation for video depth mapping
  - *From: community member*

- **Glitchnodes** (node)
  - Nodes combining programmatic art with modern and older models
  - *From: jeru*

- **Stable Diffusion attention visualization tool** (tool)
  - Tool for visualizing Stable Diffusion's attention layers
  - *From: community member*

- **Control LoRA for deblurring** (lora)
  - SOTA deblurring trained on Wan 1.4b
  - *From: spacepxl*

- **Room emptying LoRA** (lora)
  - Trained on four images for transformation effects
  - *From: community member*

- **Timelapse LoRA** (lora)
  - Based on similar approach to room emptying
  - *From: community member*

- **Depth Control LoRA** (lora)
  - For Wan, can be used to pandify videos
  - *From: spacepxl*

- **Arcane LoRA** (lora)
  - Works with Depth Control LoRA
  - *From: community member*

- **Steamboat Willy LoRA** (lora)
  - Gives strong personality effects, can mix with other LoRAs like squishy LoRA
  - *From: benjamin-paine*

- **Cakify LoRA** (lora)
  - Made with LTXV
  - *From: community member*

- **Parkour LoRA** (lora)
  - Motion LoRA for parkour movements
  - *From: community member*

- **Studio Ghibli LoRA** (lora)
  - For Wan, produces visually interesting generations with good composition
  - *From: community member*

- **Woodcut LoRA** (lora)
  - Creates aesthetics unlike typical AI output
  - *From: community member*

- **Redline LoRA** (lora)
  - Creates content that looks completely unlike closed models
  - *From: community member*

- **Pepe LoRA** (lora)
  - Character LoRA
  - *From: community member*

- **Looney Toon effects LoRA** (lora)
  - For LTXV 13b, creates cartoon effects
  - *From: community member*

- **Wallace & Gromit LoRA** (lora)
  - For LTXV 13b, converts content to Wallace & Gromit style
  - *From: community member*

- **Water-flow LoRA** (lora)
  - For water effects
  - *From: community member*

- **Lazy Susan LoRA** (lora)
  - High quality results comparable to professional work
  - *From: community member*

- **Crash zoom LoRA** (lora)
  - For dramatic zoom effects
  - *From: community member*

- **Audio-reactive nodes** (node)
  - For creating audio-reactive content
  - *From: community member*

- **VRGameDevGirl's Wan Megamerge** (model)
  - Merges Wan with multiple detailer and speed LoRAs
  - *From: VRGameDevGirl*

- **Cinematic LoRA for Flux** (lora)
  - Enhances cinematic qualities in Flux generations
  - *From: user*

- **2D Effects LoRA** (lora)
  - Adds 2D visual effects to video generations
  - *From: user*

- **Fire + morphskin LoRAs combination** (lora)
  - Combines action LoRAs for enhanced effects
  - *From: user*

- **Lightning + action running LoRAs** (lora)
  - Combines multiple action LoRAs for dynamic scenes
  - *From: user*

- **Faces pressed against glass LoRA** (lora)
  - Specialized LoRA for specific visual effect
  - *From: user*

- **Audioreactive pose workflow** (workflow)
  - Creates videos with audio-reactive pose movements
  - *From: RyanontheInside*

- **VRGamer Dev Girl's Wan upscaler** (tool)
  - Open source upscaler comparable to Topaz while being infinitely configurable and extendable
  - *From: pom*

- **crinklyboy's Golden Boy style LoRA** (lora)
  - LoRA for Golden Boy animation style
  - *From: pom*

- **Kontext Relight LoRA** (lora)
  - Fine-tuned Kontext for specific relighting tasks
  - *From: pom*

- **Cseti's Wallace & Gromit LoRA** (lora)
  - LoRA that can generate Wallace & Gromit style content and do creative transformations
  - *From: pom*

- **Disney Wan LoRA in training** (lora)
  - Disney-style LoRA being trained for Wan
  - *From: pom*

- **Lovis drone Wan LoRA** (lora)
  - LoRA for drone-style footage generation
  - *From: pom*

- **Disney LoRA on LOTR scenes** (lora)
  - Disney style applied to Lord of the Rings scenes
  - *From: 988068827990458459*

- **Jinx LoRA for Wan 2.2** (lora)
  - Character LoRA for Wan 2.2
  - *From: 1074404980737450065*

- **Phantom + VACE merge** (model)
  - Model merge combining Phantom and VACE capabilities
  - *From: 88822364468412416*

- **FakeVace2.2** (model)
  - Attempt to merge VACE with Wan 2.2
  - *From: 771193439399444490*

- **Reigh tool** (tool)
  - Consumer-grade tool for traveling between images with Wan and other models, successor to Dough
  - *From: pom*

- **HunyuanFoley Comfy nodes** (nodes)
  - ComfyUI nodes for HunyuanFoley audio generation
  - *From: 983060020516249670*

- **QwenEdit style-reference LoRA** (lora)
  - LoRA that significantly improves QwenEdit's ability to generate images based on style-reference
  - *From: pom*

- **FakeVace 2.2 merge** (model)
  - Merged model for video continuations
  - *From: 771193439399444490*

- **Advanced VACE nodes** (node)
  - Enhanced VACE functionality with keyframe control
  - *From: 256636116763934731*

- **Detailer for Wan & VACE 2.1** (workflow)
  - Enhancement tool for improving video quality
  - *From: 256636116763934731*

- **Mega merge for convenience** (model)
  - Combined model merge for easier workflow usage
  - *From: 348514313633267712*

- **High-noise Kinestasis 2.2 LoRA** (lora)
  - LoRA that breaks reality in interesting ways with high noise
  - *From: 1074404980737450065*

- **Subject LoRA for single reference training** (lora)
  - Generates images of subjects based on single reference image
  - *From: 301463647895683072*

- **Banostasis LoRA** (lora)
  - Enables unconventional motion styles far from standard Wan motion
  - *From: 1074404980737450065*

- **Chattable Knowledge Base** (tool)
  - Knowledge base for keeping up to date on AI developments
  - *From: 614602980943069214*

- **Animatediff LoRA** (lora)
  - LoRA trained on Animatediff outputs for unique motion style
  - *From: FlippingSigma*

- **InScene and InScene Annotate LoRAs** (lora)
  - LoRAs for generating images within a scene
  - *From: pom*

- **Exploded effect LoRA** (lora)
  - LoRA for creating exploding/transition effects
  - *From: Ashmotv*

- **Water morphing LoRA** (lora)
  - LoRA for water morphing effects, trained on 6 videos
  - *From: Ashmotv*

- **Knitting-style animation LoRA** (lora)
  - LoRA for creating knitting-style animations
  - *From: Ashmotv*

- **Scooby Doo LoRA** (lora)
  - LoRA for Scooby Doo style content
  - *From: user*

- **Jovimetrix nodepack** (node)
  - Node pack maintained by Alexander Morano with thoughtful design and color coding
  - *From: Alexander Morano*

- **Wan Move Comfy implementation** (tool)
  - Implementation of Wan Move in ComfyUI
  - *From: kijai*

- **Scope local tool with Krea integration** (tool)
  - Local tool with realtime Krea integration
  - *From: user*

- **2D to 360 VR panorama conversion** (tool)
  - Tool for turning any 2D video into a 360 VR panorama
  - *From: user*

- **LLM exploration repo for models** (tool)
  - Repository for exploring models with LLMs
  - *From: user*

- **Flux 2 trained model on personal photos** (model)
  - Model trained on user's photos using Flux 2
  - *From: 755177709071630441*

- **Wan Move standalone LoRA** (lora)
  - Extracting Wan Move to work as standalone LoRA for combination with Humo and more
  - *From: 256636116763934731*

- **Wallace & Gromit LoRA** (lora)
  - LoRA for Wallace & Gromit style generation
  - *From: 1074404980737450065*

- **INFL8 LoRA for Qwen Image Edit** (lora)
  - LoRA for inflation effects in Qwen Image Edit
  - *From: 825444296689451039*

- **Timelapse LoRA for LTX2** (lora)
  - LoRA for creating timelapse effects in LTX2
  - *From: 464322697418244096*

- **Paper cutout style LTX2 LoRA** (lora)
  - LoRA for paper cutout visual style with deep style understanding
  - *From: 257217392298426380*

- **Beauty and The Beast Style LoRA** (lora)
  - LoRA that creates distinctly early Disney animation style
  - *From: 1074404980737450065*

- **AnimateDiff for LTX2** (lora)
  - Brings Animatediff functionality to LTX2
  - *From: 464322697418244096*

- **Deforum LoRA for LTX2** (lora)
  - Brings Deforum functionality to LTX2
  - *From: 985830005315633193*

- **Burst/explosion LoRA** (lora)
  - LoRA for creating burst and explosion effects
  - *From: 825444296689451039*

- **Impasto LoRA** (lora)
  - LoRA for impasto painting style effects
  - *From: 1138907661602136245*

- **Luminance map control IC-LoRA** (lora)
  - Control mechanism that maps lighting inputs onto video
  - *From: oumoumad*

- **Jinx character LoRA** (lora)
  - Character adherence LoRA for Jinx character
  - *From: 1074404980737450065*

- **VHS tapes LoRA** (lora)
  - LoRA trained on old VHS tapes for retro video effects
  - *From: 305792526629994496*

- **Eye zoom LoRA** (lora)
  - LoRA that zooms into person's eye to reveal what they see
  - *From: 627140525916422145*

- **Animatediff LoRA for both Wan and LTXV** (lora)
  - LoRA that works with both Wan and LTXV models
  - *From: 743301749086879808*

- **Knitting effect LoRA** (lora)
  - LoRA for creating knitting visual effects, combined with TTM
  - *From: 1138907661602136245*

- **Balloon inflation LoRA** (lora)
  - LoRA for balloon and inflation effects
  - *From: 825444296689451039*

- **New Deforum LoRA for LTX2** (lora)
  - Updated Deforum LoRA specifically for LTX2
  - *From: 985830005315633193*
