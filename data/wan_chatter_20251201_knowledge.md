# Wan Chatter Knowledge Base
*Extracted from Discord discussions: 2025-12-01 to 2026-01-01*


## Technical Discoveries

- **Wan VAE can use way less VRAM if you offload the cache to CPU**
  - At 720p it's like ~5GB less VRAM used, makes it slower but beats tiled VAE if necessary, has no effect on output unlike tiling
  - *From: Kijai*

- **Low model for Wan 2.2 is just a more trained/fine tuned version of 2.1**
  - You can generate entire video with just the LN model. HN models are specifically good at motion, prompt following, and composition, but have lost ability to create details. Run HN model for first few steps to establish what it's good at, then let any low noise model or Wan 2.1 model take over
  - *From: Ablejones*

- **SteadyDancer works with LightX2V LoRA**
  - Tested and confirmed working combination
  - *From: Kijai*

- **Wrapper updates providing significant VRAM reduction**
  - Reports ranging from 10% to 50% less VRAM used since latest update
  - *From: Kijai*

- **UltraViCo (DiT-Extrapolation) breaks looping and increases video quality when going above 81 frames**
  - Normal I2V at 2x the model's trained length just loops back to start, not allowing much movement. UltraViCo prevents this and improves quality for longer videos
  - *From: Kijai*

- **Base motion is defined very early in Wan models**
  - Models define the base motion really early, so you might not see much difference unless you end sampling super early, especially with low step workflows
  - *From: Kijai*

- **Context stride causes terrible stutter in Wan**
  - Because it packs 4 frames into one latent, it causes terrible stutter. Only real way to utilize it is splitting the process and using stride on early steps, like 2.2 A14B workflows
  - *From: Kijai*

- **First frame in Wan VAE takes 4x memory compared to other frames**
  - 1st frame = context/references for the rest (the root image), which is why it uses significantly more memory
  - *From: Scruffy*

- **Wan frame count should follow 4n+1 formula**
  - Frames should be 4n+1 format (like 145 = 144 or 36 sets of 4 frames, plus 1) for proper processing
  - *From: Scruffy*

- **Diffusion models under 1000 steps have error rates of 1e-3 to 1e-5**
  - This enormous error means discretization precision barely matters for quality
  - *From: mallardgazellegoosewildcat2*

- **8 euler steps will always beat 4 steps of any other 1NFE solver**
  - More euler steps consistently outperforms higher order solvers with fewer steps
  - *From: spacepxl*

- **First-step undistilled sampling improves results**
  - Using 1-2 undistilled steps at the beginning helps with motion and overall quality, especially for I2V
  - *From: mallardgazellegoosewildcat2*

- **Motion blur issues often come from VAE, not the sampler**
  - VAE doesn't handle fast motion well due to compression architecture
  - *From: spacepxl*

- **TCD/TDD distillation works on arbitrary schedules**
  - Unlike some adversarial methods, TCD distillation respects geometry and can handle different timestep schedules
  - *From: mallardgazellegoosewildcat2*

- **SVI 2.0 uses 5 frames for continuation, not 1 frame as initially thought**
  - Updated script shows it uses 5 frames to continue and pads with the original reference image, combining both film and shot approaches
  - *From: Kijai*

- **SVI 2.0 combines SVI-Shot v1 and SVI-film v1 functionality**
  - New version provides motion dynamics of film with shot-style continuation
  - *From: 42hub*

- **Steadydancer has attention mechanism additions, multiple convolution types, and distillation step**
  - Architecture includes low rank training to preserve original model capacity better, addressing trade-off between appearance and motion control
  - *From: mallardgazellegoosewildcat2*

- **UltraViCo works with everything but drops start image/reference over longer generations**
  - Not perfect for maintaining reference consistency in extended generations
  - *From: Kijai*

- **Wan 2.2 14B and 2.1 are capped at 81 frames, will start looping after that**
  - Training was done on 81 frames, model tends to go backwards on longer generations without control signals
  - *From: Kijai*

- **SVI-Shot for Wan 2.2 only needs 1 frame masking instead of 5**
  - The svi version 2.0 for Wan 2.2 is differently trained than the 2.0 for Wan 2.1. 2.1 can use 5 frames while 2.2 can just use one frame
  - *From: Kijai*

- **Masking only first frame prevents flash between extensions**
  - Using 5 frames causes flash between extensions, masking only the first frame works better for Wan 2.2
  - *From: Kijai*

- **Concat technique reduces flash in Wan Animate**
  - Using concat_latent_image made much less flash during 14 hours of generation
  - *From: Gleb Tretyak*

- **Flash attention required for stability**
  - It is necessary to install flash_attn; otherwise, severe artifacts and instability will appear
  - *From: Ablejones*

- **SVI-Shot can use 3-4 frames with minimal flashing**
  - You can get away with 3 or 4 frames with minimal flashing, and it still maintains the reference
  - *From: Ablejones*

- **PyTorch 2.8 causes memory leaks with image resize nodes**
  - Updating to PyTorch 2.9.1+cu130 fixes the memory leak issue where resize nodes don't release cache properly
  - *From: spacepxl*

- **SVI 2.2 works better with SageAttention**
  - Testing showed outputs were better with SageAttention enabled vs disabled
  - *From: Ablejones*

- **FILM VFI in Fill-Nodes pack is significantly faster**
  - 6-8 times faster than other FILM implementations
  - *From: lostintranslation*

- **3 overlap frames seems to be the highest possible with no artifacts for SVI**
  - 3 overlap frames works better than 1, but going higher causes artifacts
  - *From: Ablejones*

- **SVI should not have flash at transition if used correctly**
  - Flashes indicate incorrect usage rather than model limitation
  - *From: Ablejones*

- **Reference strength can be modified in SVI workflows**
  - Been experimenting with changing reference strength as alternative approach
  - *From: Ablejones*

- **HuMo can be used as low noise model in Wan 2.2**
  - Works both on wrapper and native implementations
  - *From: Elvaxorn*

- **Magref can be better on I2V context window generations**
  - Can even use it as the low noise model in Wan 2.2, although you lose a little identity preservation in exchange for some better motion and blending
  - *From: blake37*

- **Flash attention massively affects SVI performance**
  - Selected attention type has significant impact on SVI results
  - *From: Gleb Tretyak*

- **Merged vs unmerged LoRAs produce different effects**
  - The effect is bit different depending on model/LoRA, sometimes stronger sometimes weaker. If merge fixes some issue then increasing strength might do so too
  - *From: Kijai*

- **OneToAll Animation performs better pose retargeting than WanAnimate**
  - OneToAll does better at keeping reference when used correctly and has better pose alignment capabilities
  - *From: Kijai*

- **Token replacement technique in Wan models**
  - Sets timestep of next 2 frames after reference frame to 0 to avoid them changing too much from init. Only used when continuing from previous frames
  - *From: Kijai*

- **OneToAll Animation uses reference + controlnet modules for Wan T2V**
  - Includes alignment code for WanAnimate preprocessor to align reference pose better
  - *From: Kijai*

- **OneToAll Animation has two pose modes**
  - Either aligns input pose to reference, or reference to input pose
  - *From: Kijai*

- **Fraudulent model discovery - aquif-ai uploaded stolen Magic Wan model**
  - Hash comparison confirmed aquif-ai's model is identical to Magic-Wan-Image-v1.0, not a finetune as claimed
  - *From: Kijai*

- **WanAnimate better init adherence with 25 steps euler vs 8 steps lightx2v lora**
  - cfg 1.2 25 steps euler shows better init adherence compared to cfg 1.2 8 steps lightx2v lora, though looks a little scuffed
  - *From: 企鵝（50% CASH 50%GOLD）*

- **OneToAll extension method uses token replacement with 5 frame overlap**
  - 5 frame overlap, mark that part of sequence with zero timestep, and don't include that part in the scheduler. Similar to S2V technique
  - *From: Kijai*

- **OneToAll can extend videos seemingly indefinitely**
  - Generated 613 frames with One-to-all, though it does burn with lightx2v. Can reduce burning by lowering lightx2v strength, lower shift, ending pose control early
  - *From: Kijai*

- **RCM distill version released for Wan 2.2 I2V**
  - worstcoder/rcm-Wan released RCM6.0 merged model for faster generation with fewer steps
  - *From: DawnII*

- **Pose aligner can be stopped early to maintain reference better**
  - You can stop the pose control after few steps and then it keeps the ref better in OneToAll
  - *From: Kijai*

- **Not scaling pose at all sometimes leads to best results**
  - Sometimes not scaling the pose at all still leads to best results in OneToAll
  - *From: Kijai*

- **HuMo fix allows using start image**
  - Recent HuMo fix for wrapper allows using start image as HuMo is I2V model, normally it's not used
  - *From: Kijai*

- **WanMove works at 121 frames, longer than initial 81 frame limit**
  - Model can generate beyond 81 frames and supports custom fps creation
  - *From: Kijai*

- **WanMove maintains better style consistency with I2V models**
  - I2V models keep the style well when using control, better than expected
  - *From: Kijai*

- **WanMove supports mask for tracks, unlike ATI**
  - Has ability to use mask batch to create mask for single track, multiple track masking not yet implemented
  - *From: Kijai*

- **WanMove is compatible with context, unlike ATI**
  - Nothing is hard coded, should work better with context than ATI
  - *From: Kijai*

- **Zooming in using video models works as upscale method**
  - Can use video models for upscaling by zooming in, then use second model to unwarp geometry
  - *From: mallardgazellegoosewildcat2*

- **HuMo can be used as low noise with Wan 2.2 as high noise for lip sync**
  - Works well by using HuMo as the low-noise side and Wan 2.2 as high-noise side at higher shift
  - *From: Ablejones*

- **SVI helps overcome video degradation over time**
  - SVI lora keeps character reference but pushes camera back towards reference, preventing degradation but limiting camera movement
  - *From: Kijai*

- **WanMove trajectory control works better than ATI**
  - Like ATI but better trajectory control system
  - *From: Kijai*

- **SVI 2.2 designed for static shots, not dynamic camera movement**
  - Wan 2.2 is equivalent of 'shot' for 2.1, there is no film version for 2.2
  - *From: DawnII*

- **LightX2V loras cause color drift after 40-45 seconds**
  - Color drift becomes noticeable around 40-45 second generation when using single reference, 30-35s with additional lora
  - *From: Vardogr*

- **Native WanMove implementation uses new Tracks data type**
  - Instead of JSON coords, uses Tracks type that holds path and mask tensors for easier node development
  - *From: Kijai*

- **NAG is implemented as additional attention in the positive pass only, separate from negative CFG passes**
  - NAG ignores negative passes and only affects positive cross attention, shouldn't interfere with CFG
  - *From: Kijai*

- **HuMo generates 4 extra frames automatically**
  - For every reference image given to HuMo, it adds 4 frames to generation, then sampler cuts those 4 frames off
  - *From: Chandler ✨ 🎈*

- **SVI 2.0 lora for Wan2.1 works better with HuMo than SVI 2.2 Wan2.2 LN lora**
  - Plus you get 5 frames of overlap, helps because you can toss out first 5 frames where most HuMo i2v artifacts show up
  - *From: Ablejones*

- **Lightning loras completely remove ability to do dark scenes with T2V**
  - They make everything bright and change results too much
  - *From: Kijai*

- **Q8 GGUF is an improvement overall**
  - No OOM or VRAM clearing needed via Distorch nodes, pushed to 97 frames with no issue on 128GB RAM
  - *From: metaphysician*

- **rCM LoRAs trained on Wan 2.1 don't work properly on Wan 2.2**
  - Can't use LoRAs on different models because consistency models require operating on the same ODE they were trained on
  - *From: mallardgazellegoosewildcat2*

- **OneToAll 1.3B model performs better than expected**
  - Actually produces decent results, not as terrible as anticipated
  - *From: mallardgazellegoosewildcat2*

- **SCAIL model uses 20 input channels and concatenated pose embeddings**
  - I2V model with separate pose patch embed concatenated in sequence dim instead of channel, requires split rope
  - *From: Kijai*

- **SCAIL pose detector uses 3D + 2D mashup format**
  - Uses warm colors on right side and cool colors on left side, which seems important for proper functioning
  - *From: Kijai*

- **Mixing e5m2 normal and scaled quantization can cause issues**
  - Can lead to black generations and NaN outputs
  - *From: Kijai*

- **SCAIL model generalizes well to different pose inputs**
  - SCAIL works with pose inputs it wasn't specifically trained with, showing good generalization capabilities
  - *From: Kijai*

- **Preview as test node works for conditioning outputs**
  - The Preview as test node works for outputs that aren't classes, including conditioning (conds)
  - *From: Kijai*

- **SCAIL pose downsampling by default**
  - By default the pose is downsampled to half the size as it's heavy otherwise, and the default res is 895x512. Model has separate patch embed for pose so doesn't have to match in resolution, but currently only full or half size are supported
  - *From: Kijai*

- **Context windows work with SCAIL**
  - SCAIL works with context windows for longer video generation, though it's slow
  - *From: Kijai*

- **V2 nodes design philosophy**
  - V2 nodes are designed to be modular with separate components: text_embeds, image_embeds, scheduler, extra_args for cleaner workflow
  - *From: Scruffy*

- **ComfyUI-RMBG nodes globally override torch.load to unsafe loading**
  - This breaks NLF model functionality and creates security vulnerabilities by disabling safe pickle loading
  - *From: Kijai*

- **WanMove works with context windows**
  - Can now split longer camera movements across multiple 81-frame context windows using GetTrackRange node
  - *From: Kijai*

- **SCAIL pose input needs half resolution of main input**
  - Model is trained this way - if main input is 512x896, pose input should be 256x448
  - *From: Kijai*

- **Uni3c with SCAIL improves background consistency**
  - Background rotates properly instead of being frozen in longer videos
  - *From: slmonker(5090D 32GB)*

- **Multiple spline interpolation methods available in WanMove**
  - Cardinal, Polar, Step, and other interpolation methods for different motion effects
  - *From: zelgo_*

- **3D pose detection now working for SCAIL**
  - Single person detection implemented with proper finger tracking
  - *From: Kijai*

- **WanMove has speed mode for path control**
  - Can adjust movement speed at specific points by adding control points
  - *From: Kijai*

- **low_rank algorithm is 100x faster than full extraction with almost same quality**
  - For LoRA extraction, low_rank provides massive speed improvement with minimal quality loss
  - *From: Kijai*

- **TurboWan 2.2 model uses activation quantization and sparse attention**
  - Claims 100x speedup over base model, uses RCM distillation with SAGE optimization
  - *From: yi*

- **SCAIL now supports multi-person pose detection**
  - Updated pose node can detect and handle 2 people in videos
  - *From: slmonker(5090D 32GB)*

- **Taichi backend in SCAIL can run on CPU, GPU, OpenGL, or Vulkan**
  - Fast even on CPU, auto-detects architecture when set to 'gpu'
  - *From: Kijai*

- **Swapping left and right hand coordinates fixes SCAIL pose issues**
  - There was an error in the SCAIL_Pose repo where left and right hand coordinates were swapped, causing incorrect hand positioning
  - *From: teal024*

- **SCAIL works better with longer prompts**
  - Long prompts usually yield better control for both motions and background in SCAIL
  - *From: teal024*

- **SCAIL pose control at 0.25 strength gives good results**
  - Using pose control for only 2 out of 6 steps (ending at 0.25) provides effective control without overdoing it
  - *From: Kijai*

- **First step only pose control works well for some scenarios**
  - Using pose control only on the first diffusion step can be effective for certain types of motion
  - *From: Kijai*

- **NLF returns bounding boxes in addition to pose data**
  - The NLF pose detection system outputs bbox information that can be useful for additional processing
  - *From: Kijai*

- **SCAIL performs better than Wan Animate for long-duration generation**
  - For extended video sequences, SCAIL shows superior performance compared to Wan Animate
  - *From: Karthik*

- **SCAIL has better ID retention than WanAnimate but WanAnimate has better facial performance**
  - SCAIL retained ID much better than Wan Animate but facial performance replication was missing
  - *From: A.I.Warper*

- **Higher resolution generates significantly better quality with SCAIL**
  - 1080p looks way better than lower resolutions, difference is more evident than usual
  - *From: A.I.Warper*

- **First CFG step with real CFG boosts motion**
  - 1-2 steps with no distill loras and real CFG, then use distill and cfg=1 for rest helps motion
  - *From: spacepxl*

- **VACE works better with trained LoRAs than image references**
  - VACE is basically just a controlnet on top of unmodified t2v model, so t2v loras work incredibly well. Trained lora will almost always beat image references
  - *From: spacepxl*

- **2.2 low model can refine 2.1 VACE outputs**
  - Often use 2.2 low as a refiner for 2.1 vace, 1-2 steps just to clean it up
  - *From: spacepxl*

- **SCAIL excels at complex motions and generalizing for reference images**
  - Better for dance movements and complex choreography, though not better for simple motions or facial controls
  - *From: Kijai*

- **Wan 2.6 pricing revealed**
  - $0.10 per second for 720p, $0.15 per second for 1080p
  - *From: JohnDopamine*

- **SCAIL has context window morphing issues**
  - Slight background shifts at context windows, can see gaps even with 64 frame overlap
  - *From: slmonker(5090D 32GB)*

- **Multi-person pose tracking in SCAIL flashes between colors**
  - Colors should stay separate but currently flash between them, multi-person needs segmented approach
  - *From: Kijai*

- **SCAIL pose detection works better with 2D anime than DWPose**
  - User reported SCAIL tracking from 2D anime driving video which had serious issues with DWPose
  - *From: metaphysician*

- **SCAIL ref image acts as the start frame**
  - The reference image is already the start frame, not a separate input
  - *From: Kijai*

- **SCAIL can do higher fps output matching control video**
  - SCAIL follows pose video frame by frame, so 24fps input creates 24fps output when not skipping frames
  - *From: Kijai*

- **Wan 2.5+ confirmed closed source**
  - Wan team wants to open source but 'someone big does not' - Wan 2.2 is the last open source model
  - *From: slmonker(5090D 32GB)*

- **Rope cache issue fixed in WanVideoWrapper**
  - ComfyUI rope cache issue causing errors has been resolved
  - *From: Kijai*

- **SCAIL pose input needs to be half the resolution of output**
  - Pose resolution must be half of the output resolution for SCAIL to work properly
  - *From: Kijai*

- **Fun InP fl2v mode needed for First-Last-Frame to work properly**
  - Enabling fl2v mode in the I2V encode node prevents yellow flash when using same image for start and end frames
  - *From: Kijai*

- **SCAIL works with vitpose input for non-humanoid subjects**
  - SCAIL can work with vitpose input for animals and non-human subjects, vitpose can even detect objects
  - *From: Kijai*

- **New T2V distill LoRAs released for Wan 2.2**
  - Latest T2V distill LoRAs available at lightx2v/Wan2.2-Distill-Loras
  - *From: yi*

- **Wan Move LoRA works with Wan 2.2 but not 2.1**
  - 2.2 understood the conditioning while 2.1 was meh and added walking people. Works better when prompting for static elements
  - *From: Gleb Tretyak*

- **SCAIL cannot use Wan Move LoRA due to architectural differences**
  - SCAIL is all in 20 channels while WanMove conditioning is in extra channels that SCAIL doesn't have. WanMove is identical to base Wan 2.1 I2V structure, just finetuned
  - *From: Kijai*

- **Models output whatever bit depth they're run in but quality won't be better just by increasing bit depth**
  - Model trained on 8bit data learns continuous functions, so outputs are smooth up to fp16 precision but range/accuracy similar to 8bit training data
  - *From: spacepxl*

- **Context windows prevent camera from moving much from initial position**
  - Every window has same start image/camera position, tries to get to that and if moves too far away, snaps back
  - *From: Kijai*

- **Differential diffusion works with mask in WanVideo Encode node**
  - Adding mask uses differential diffusion automatically, can also use Set Latent Noise Mask
  - *From: Kijai*

- **UniAnimate strength can be unlocked beyond 1.0**
  - No technical reason for 1.0 limit, was only too strong for 2.1. Can experiment with higher values for 2.2
  - *From: Kijai*

- **Wan 2.2 works with strength LoRAs**
  - Strength LoRAs definitely affect 2.2 output, unlike being locked at 1.0 for 2.1
  - *From: Gleb Tretyak*

- **WanMove works with UniAnimate**
  - Nice to know UniAnimate can work with WanMove for combined motion control
  - *From: Kijai*

- **Prompt weighting works in WanVideoWrapper**
  - Parentheses like (16:9) cause weight multiplication - (16:9) multiplied token '16' weight by 9x causing artifacts
  - *From: Gleb Tretyak*

- **InfiniteTalk Multi needs clean first latent frame**
  - If first latent frame is noise, you get flash/noise artifacts. Must use clean image as first frame
  - *From: Kijai*

- **WorldCanvas uses 2.2 weights with 53 input channels**
  - New model with 53 input channels (vs Fun Control 2.2's 52), appears to be 2.2 with VACE-like features
  - *From: Kijai*

- **LongCat Avatar uses 'enhance_hf' scheduler modification**
  - Their scheduler modification is quite drastic, which could explain implementation issues
  - *From: Kijai*

- **FlashPortrait uses the same face encoder as WanAnimate**
  - FlashPortrait is a 14B 2.1 I2V model that seems to be using the same face encoder as WanAnimate and appears to be using the Fun model architecture
  - *From: Kijai*

- **FlashPortrait acceleration is just lightx2v LoRA**
  - The claimed 6x acceleration does not exist independently - it's literally just using the lightx2v LoRA, and using context windows actually loses that speed advantage
  - *From: Kijai*

- **FlashPortrait renamed lightx2v LoRA without credit**
  - FlashPortrait repo contains 'fast_lora_rank64.safetensors' which is identical to lightx2v's wan2.1_i2v_lora_rank64_lightx2v_4step.safetensors down to the hash, with no credit given
  - *From: Kijai*

- **LongCat Avatar uses previous latents directly as model input**
  - The continuation is mostly from latent space with minimal decode-encode between windows, using previous latents directly as model input rather than full image reconstruction
  - *From: Kijai*

- **LongCat Avatar has method to prevent repetitive actions in long generations**
  - Main advantage over Infinite is a built-in method that prevents repetitive actions during long video generation
  - *From: Kijai*

- **LongCat Avatar ref_latent bug was causing degradation**
  - Kijai discovered a bug where ref_latent wasn't being used, causing identity degradation in longer generations. Fixed in latest commits.
  - *From: Kijai*

- **LongCat Avatar allows significant camera movement without breaking**
  - The model surprisingly handles camera movement well, even with dynamic shots and rotations
  - *From: Kijai*

- **Stand-In LoRA works on Wan 2.2 without code changes**
  - The new Stand-In LoRA can be used directly with Wan 2.2, uploaded as .safetensors format
  - *From: Kijai*

- **LongVie2 controlnet works with just Wan 2.1 I2V**
  - Successfully applied LongVie2 controlnet to Wan 2.1 I2V without using their attention weights, just the controlnet portion
  - *From: Kijai*

- **LongCat-Avatar can generate up to 301 frames successfully**
  - 301 frames took 560sec on 5090, but 141 frames took 154sec - more than doubling frames results in more than triple the time
  - *From: burgstall*

- **LongCat-Avatar works at various resolutions**
  - 480x480x141 and 480x480x201 frames both work, 93 frame windows aren't entirely necessary if you have memory
  - *From: burgstall*

- **Stand-In LoRAs need to be loaded differently**
  - Stand-In LoRAs must be loaded in the model loader lora input as it's a different kind of LoRA
  - *From: Kijai*

- **Pose input resolution requirement for dark output fix**
  - Pose should be half the resolution of the main input, which is done automatically in example workflow
  - *From: Kijai*

- **Context Options don't affect main steps**
  - Context options do multiple model passes per step but don't change the step count
  - *From: Kijai*

- **Denoise value affects actual steps executed**
  - Denoise at 0.21 means only doing 20% of the steps, which is why console shows fewer steps than set
  - *From: Kijai*

- **PUSA LoRA made for 2.2 works better on WAN 2.1 than the PUSA 2.1 version**
  - When testing Stand-In for WAN 2.1, the PUSA 2.2 LoRA actually improved facial consistency better than the version specifically made for 2.1
  - *From: ▲*

- **2.2 LN LoRAs work reliably in WAN 2.1 based models**
  - 2.2 LN wan is just 2.1+++, so you can use 2.2 LN loras pretty reliably in wan 2.1 based models
  - *From: ucren*

- **LongCat-Avatar uses 32 fps as input and samples audio with stride of 2**
  - The model uses 32 fps as input and samples the audio with stride of 2, so the output is 16 fps video
  - *From: Kijai*

- **WanMove depth control strength affects tree persistence**
  - Lowering the control strength to 0.8 seems to allow the tree to persist in depth-controlled generations
  - *From: Kijai*

- **NVFP4 support now available for Blackwell cards**
  - New Wan-NVFP4 model released with NVFP4 kernel support, mostly supported in pytorch nightly
  - *From: yi*

- **Windows 11 shows improved VRAM efficiency over Windows 10**
  - User reports significantly reduced VRAM usage and ability to generate at Full HD directly without running out of VRAM after switching from Windows 10 to Windows 11
  - *From: David Snow*

- **Frame rates need to match between input and output for SCAIL**
  - Using 16fps for both input video and output video improves SCAIL motion transfer quality
  - *From: ucren*

- **vitpose-h-wholebody model improves pose detection**
  - Better pose detection results compared to vitpose-l-wholebody for SCAIL workflows
  - *From: ucren*

- **Padding reference images improves SCAIL results**
  - Reference images that are too tightly cropped cause disproportionate results, padding helps fit the character properly
  - *From: Kijai*

- **StoryMem LoRAs require special alpha scaling**
  - StoryMem LoRAs are rank stabilized and need strength around 22 or automatic scaling code to work properly
  - *From: Kijai*

- **Block swap is relatively fast for model loading**
  - PCI Express 4 interface allows fast transfer between RAM and VRAM, adding only seconds max to generation
  - *From: 42hub*

- **vitpose files need to be in models/detection folder**
  - vitpose-h-wholebody.onnx should be placed in models/detection rather than models/onnx for proper detection
  - *From: JohnDopamine*

- **q4_km GGUF uses less VRAM than fp8 scaled**
  - q4km allows more frames for upscaling compared to fp8 scaled version
  - *From: craftogrammer*

- **Context windows work with WanAnimate after bug fix**
  - WanVideo Encode Latent Batch with context windows now compatible with WanAnimate
  - *From: Kijai*

- **Multiple images and prompts can be used in I2V**
  - Can use multiple images with pipe-separated prompts to generate different video segments in one generation
  - *From: Kijai*

- **SVI 2.0 Pro no longer uses first frame copies for conditioning**
  - Now uses last latent index instead of last frame, allowing cond channel to be utilized by other controls like pose. You lose less frames in cond channel.
  - *From: Gleb Tretyak*

- **SVI 2.0 Pro settings for lightx compatibility**
  - Setting overlap to 4 and motion frames to 1 stops glitches when using lightx2v
  - *From: Benjimon*

- **Wan Alpha 2.0 uses VAE LoRA for transparency**
  - Uses separate vae_fgr and vae_pha models with decoder LoRA loading for foreground and alpha channels
  - *From: Gleb Tretyak*

- **SCAIL scales skeleton of input video TO input image**
  - DWPose from reference image gets applied, then video motion is applied to that skeleton rather than original video bones
  - *From: DawnII*

- **Native QwenVL 2.5 implementation in progress**
  - Kijai working on native implementation, considering 3.0 support. Useful when model uses same text encoder for embeddings
  - *From: Kijai*

- **LightX2V achieves 25x speedup by reducing model passes from 100 (50 steps with cfg) to 4 (4 steps without cfg)**
  - SageAttention provides additional 2x faster model pass, making total speedup 50x faster
  - *From: Kijai*

- **Wan 2.2 works better with fp8 fast compared to 2.1**
  - fp8 fast is even usable with 2.2 while it never was for 2.1
  - *From: Kijai*

- **I2V models have 36 channels (32 + 4 mask channels) while T2V models have 16 channels**
  - This causes tensor mismatch errors when trying to mix I2V and T2V models
  - *From: cyncratic*

- **Wan training with 1k videos at 121 frames requires 32GB VRAM for LoRA training**
  - Can possibly work on 24GB with max block swap but will be slow
  - *From: CJ*

- **SVI 2.0 Pro doesn't need encoding between extensions**
  - Only the init image needs encoding alone, no black padding frames are encoded - padding is just torch zeros directly
  - *From: Kijai*

- **SVI Pro uses clean anchor frame for extensions**
  - Always uses the same first image as anchor, should be able to go long without decode-encode degradation
  - *From: Kijai*

- **Wan wrapper VRAM usage improved significantly**
  - 20% improvement in VRAM usage, user went from 96% to 73% VRAM usage with 1280x720 81f
  - *From: Lumifel*

- **Open-OmniVCus works but feels realism biased**
  - Returns consistent results but has a bias toward realistic content
  - *From: Kijai*

- **Scene changes cause SVI Pro degradation**
  - When scene changes significantly, the original reference frame doesn't apply well, causing degradation
  - *From: Kijai*

- **Stand-in LoRA for Wan 2.2 works best with specific dimensions**
  - Reference must be exactly 512x512 and output 480x832 for best results, other dimensions lose likeness
  - *From: ucren*

- **SVI Pro uses offset parameter to handle different dimensions**
  - Changing offset to 2 for 1088x640 resolution helps with generation
  - *From: ucren*

- **SVI Pro uses previous generation latent directly instead of frames**
  - No decoding/encoding between generations, uses last 4 frames essentially through latent space
  - *From: DawnII*

- **LightX2V causes motion issues with inconsistent pacing**
  - Makes entire video feel choppy, motion becomes unpredictable and slow
  - *From: slmonker(5090D 32GB)*

- **High noise models work better without LightX2V**
  - Much better motion quality when not using LightX2V lora on high noise model
  - *From: slmonker(5090D 32GB)*

- **SVI Pro has hard time following simple prompts**
  - Difficulty with prompt adherence compared to regular generation
  - *From: Kijai*

- **SVI Pro works in portrait orientation**
  - Successfully generates portrait videos
  - *From: DawnII*

- **Ultravico (modified attention) works with frame_tokens corresponding to 832x480**
  - Hard coded frame_tokens may be why ultravico works badly at other resolutions
  - *From: Kijai*

- **First frame alpha decay modification improves longer generations**
  - Modified code to never decay the first frame amount of tokens, though might ruin motion
  - *From: Kijai*

- **SVI Pro can replicate StorymMem functionality with independent anchor latents**
  - Using different anchor samples independently can achieve similar results to StorymMem without needing the actual StorymMem model
  - *From: slmonker(5090D 32GB)*

- **Qwen Image Edit 2511 can generate multiple view anchor samples**
  - Used to generate multiple views as single anchor samples for each phase in SVI workflows
  - *From: slmonker(5090D 32GB)*

- **RCM LoRA improves cohesion and adherence in Wan 2.2**
  - Using RCM LoRA with old lightx2v at 3.0 strength provides better prompt adherence and visual cohesion
  - *From: faceismus*

- **SVI Pro works well for video extension**
  - Can create videos up to 52-57 seconds long with good quality
  - *From: slmonker(5090D 32GB)*

- **Ultravico can generate longer sequences**
  - Can push generations past 121/149 frames, works better with T2V than I2V
  - *From: Kijai*

- **Motion scale control node works with VACE**
  - The new motion scale control node can work with VACE unlike PainterI2V
  - *From: Elvaxorn*

- **Smoothmix has lightx2v LoRA built-in**
  - Smoothmix model includes lightx2v LoRA so you don't need to load it separately
  - *From: Tachyon*

- **SVI Pro can generate up to 2 minute videos**
  - Maximum tested length is 57 seconds but theoretically can go up to 2 minutes
  - *From: avataraim*

- **Augment empty frames strength of 0.2-0.3 works well for motion enhancement**
  - 0.4 introduced artifacts, 0.0-0.3 range produces good comparable results
  - *From: David Snow*

- **VACE 2.1 modules can work with Wan 2.2 T2V models**
  - At least with the Low Noise ones, works fine for certain tasks
  - *From: Ablejones*

- **HuMo I2V capabilities slightly degraded but still functional**
  - Tiny amount of noise on first frame but still works well for I2V
  - *From: Ablejones*

- **Color matching all frames to first frame helps with color drift**
  - Using Color Match node from KJNodes to correct all frames to the first one
  - *From: 42hub*

- **VACE training lost original functionality but improved simple control + reference for realistic content**
  - Training the VACE model seemed to reduce some original capabilities while improving specific use cases
  - *From: Kijai*

- **FreeLong node doesn't actually use FreeLong for long generation**
  - Despite claims, the node just uses last frame and hopes FreeLong within 81 frames does something
  - *From: Kijai*

- **Fun models can work at 161 frames with control**
  - You lose video quality but motion quality is fine due to the control when going past training limits
  - *From: Kijai*

- **FreeLong blends low-frequency global video features with high-frequency local video features**
  - Maintains global consistency while incorporating diverse spatiotemporal details from local videos
  - *From: mallardgazellegoosewildcat2*

- **Enhance-a-video separates temporal tokens from spatial**
  - Similar approach to FreeLong in handling different aspects of video generation
  - *From: Kijai*


## Troubleshooting & Solutions

- **Problem:** Torch compile causing noise/artifacts in Fun VACE
  - **Solution:** Upgrade to PyTorch 2.9.1 from 2.9.0
  - *From: Gleb Tretyak*

- **Problem:** Lynx not working with I2V after recent wrapper update
  - **Solution:** Fixed with code changes, was related to tensor device placement issues
  - *From: Kijai*

- **Problem:** LoRAs never fully offloaded at end of sampling in multi-sampler workflows
  - **Solution:** Fixed in wrapper update, was increasing VRAM cost and leaving less VRAM for VAE decode
  - *From: Kijai*

- **Problem:** Performance degradation after wrapper updates
  - **Solution:** Clear Triton caches at C:\Users\<username>\.triton and torch inductor cache
  - *From: Kijai*

- **Problem:** Out of memory errors that appear as CUDA errors
  - **Solution:** These are actually RAM errors not VRAM, reboot to clear fragmented memory
  - *From: Kijai*

- **Problem:** SAGE attention errors with S2V
  - **Solution:** Input tensors must be in dtype of torch.float16 or torch.bfloat16, falls back to pytorch attention
  - *From: blake37*

- **Problem:** ComfyUI tab loads infinitely after upgrading frontend
  - **Solution:** Move all custom nodes to new directory outside custom_nodes, then move half back in. Use binary search approach to find problematic node
  - *From: Scruffy*

- **Problem:** SageAttention installation issues on Ubuntu 24.04
  - **Solution:** Downgrade to Ubuntu 22.04 or Pop OS 22.04, as CUDA toolkit compatibility is better
  - *From: seitanism*

- **Problem:** torch compile error with QuantizedTensor after ComfyUI update
  - **Solution:** Issue identified but no specific solution provided in this chat
  - *From: Baku*

- **Problem:** VAEUtils_CustomVAELoader error: VAE is invalid
  - **Solution:** The linked file is actually a latent upscale model, not a VAE. Use the latent upscale node instead
  - *From: spacepxl*

- **Problem:** Negative embeddings error with CFG scale > 1.0 in NAG setup
  - **Solution:** Issue was with CFG schedule float list, resolved by changing that component
  - *From: David Snow*

- **Problem:** UltraViCo loses start image influence at 241 frames
  - **Solution:** Known limitation identified but no solution provided
  - *From: Kijai*

- **Problem:** Fast motion causes blur in generated videos
  - **Solution:** Use 2x VFI (video frame interpolation) and v2v to slow down motion, then clean up with v2v
  - *From: spacepxl*

- **Problem:** Multistep samplers underperform with 2+2 split step samplers
  - **Solution:** Stay away from multistep samplers for anything lower than 8 steps, especially for split-model workflows
  - *From: Ablejones*

- **Problem:** FP8 model giving horrid output compared to Q5 GGUF
  - **Solution:** Use Q8 GGUF with distorch model loaders for better control over VRAM/RAM loading
  - *From: David Snow*

- **Problem:** CUDA kernel error on 4090 with --fast and --use-sage-attention flags
  - **Solution:** Remove the custom parameters, error was caused by sage attention needing rebuild for different GPU architectures
  - *From: mamad8*

- **Problem:** UltraViCo returns 'NoneType' object error
  - **Solution:** Works with T2V but fails with I2V and HuMo due to attention calls and input size limitations with block masking
  - *From: aiacsp*

- **Problem:** OOM issues with Steadydancer on 3090
  - **Solution:** Reduce blocks to swap and/or disable non-blocking in block swap settings
  - *From: Kijai*

- **Problem:** SVI 2.0 not working properly with LightX2V
  - **Solution:** LightX2V breaks SVI 2.0, works better without it
  - *From: Kijai*

- **Problem:** SVI 2.0 looking washed out and not working as expected
  - **Solution:** Use 5 frame overlap with proper padding, updated implementation needed
  - *From: Hashu*

- **Problem:** Context stride causing fatal errors with uniform_standard
  - **Solution:** Keep stride at 1, don't use stride value of 4
  - *From: Kijai*

- **Problem:** Flash between video extensions
  - **Solution:** Mask only the first frame instead of all 5 frames for Wan 2.2
  - *From: Kijai*

- **Problem:** Artifacts around mouth in video
  - **Solution:** Install flash_attn to prevent severe artifacts and instability
  - *From: Ablejones*

- **Problem:** DWPose not detecting bones in complex movements
  - **Solution:** Try vit pose using WanAnimate preprocess stuff, or mask out subject on black background before running pose
  - *From: Ablejones*

- **Problem:** ComfyUI memory not releasing properly
  - **Solution:** Use explicit caching by saving and loading intermediate images/videos, or switch to API
  - *From: mallardgazellegoosewildcat2*

- **Problem:** Memory leak with image resize nodes causing crashes
  - **Solution:** Update to PyTorch 2.9.1+cu130 and uninstall version-dependent packages like xformers and flash-attn
  - *From: spacepxl*

- **Problem:** ComfyUI crashes after PyTorch update
  - **Solution:** Update SageAttention and other custom nodes that depend on PyTorch version
  - *From: lostintranslation*

- **Problem:** Memory leak affects multiple resize node types
  - **Solution:** Issue is in ComfyUI's node caching system, not specific nodes - updating PyTorch fixes it
  - *From: spacepxl*

- **Problem:** RuntimeError: GET was unable to find an engine to execute this computation with WanVideo ImageToVideo Encode node
  - **Solution:** Changed bf16 to fp16
  - *From: xwsswww*

- **Problem:** RAM leak issue with torch 2.8.0
  - **Solution:** Update from torch 2.8.0 to 2.9.1
  - *From: Kijai*

- **Problem:** InfiniteTalk modifying too much of the video beyond just mouth
  - **Solution:** Use masking or low steps like 2 to have Infinite modify only the mouth. More steps = more quality is not always true in this specific situation
  - *From: Stef*

- **Problem:** HuMo model loading taking too long (minutes instead of seconds)
  - **Solution:** Issue is usually slow cloud server drives, should load in seconds with fast SSD
  - *From: Kijai*

- **Problem:** OOM with HuMo at 1280x720
  - **Solution:** Use lower resolution like 1024x576
  - *From: AmirKerr*

- **Problem:** Merging LoRAs breaks HuMo model
  - **Solution:** Don't merge LoRAs with HuMo, use unmerged
  - *From: Gleb Tretyak*

- **Problem:** OneToAll Animation model not working from early download
  - **Solution:** Re-download model or rename norm keys (attn1.norm_added_k -> ref_attn_norm_k_img)
  - *From: Kijai*

- **Problem:** SVI LoRAs not working with native ComfyUI
  - **Solution:** Use WanVideoWrapper - native ComfyUI LoRA loader doesn't work with SVI models
  - *From: Ablejones*

- **Problem:** Pose control bias issues
  - **Solution:** Models need to encode videos directly instead of relying on openpose
  - *From: mallardgazellegoosewildcat2*

- **Problem:** VACE mask loading issue
  - **Solution:** Load masked video into 'input frames' slot on VACE encoder with first frame replaced, not as control images
  - *From: ingi // SYSTMS*

- **Problem:** ComfyUI launch breaking
  - **Solution:** Remove westNeighbor_ComfyUI-ultimate-openpose-editor custom node
  - *From: Gleb Tretyak*

- **Problem:** WanVideoDecode error when reusing decoded video
  - **Solution:** Fresh sidecar install with basics resolves the issue - caused by some other custom node conflict
  - *From: Nathan Shipley*

- **Problem:** Memory issues with OneToAll at 81 frames 512x even with fp8 and 30 block swap
  - **Solution:** Issue is with VAE conv3d before sampling starts. 832x480x81 works under 12GB. Apply conv3d fix from hunyuan VAE
  - *From: patientx*

- **Problem:** Saturation changes in normal wan i2v
  - **Solution:** Issue was motion amplitude above 1 in painteri2v node
  - *From: 企鵝（50% CASH 50%GOLD）*

- **Problem:** Dynamic face expressions missing in 2D character control
  - **Solution:** Extract face from ref image as 512x512 then repeat for N frames, use that for face_images
  - *From: FlipYourBits*

- **Problem:** Mask input issues in VACE workflow
  - **Solution:** Mask is only needed in first vace encode for start frame and inpaint areas. Unplug input_masks from pose and depth vace encodes
  - *From: Hashu*

- **Problem:** TinyVAE not showing in vae_approx folder
  - **Solution:** Use normal VAE loader, or use separate tiny vae loader in wrapper. Don't rename the file. Requires recent ComfyUI update
  - *From: Kijai*

- **Problem:** Sage Attention installation on fresh install
  - **Solution:** Install two wheels from woct0rdho repos - super easy now, no need for visual studio or cuda-toolkit
  - *From: Kijai*

- **Problem:** Fp8 scaled models producing black/NaN outputs
  - **Solution:** Issue with recent ComfyUI quantization update, some LoRAs affected differently - lightx2v T2V lora still works
  - *From: Kijai*

- **Problem:** Frame count mismatch error in spline editor
  - **Solution:** Bug when using multiple splines gives wrong count, use single spline or set frame count manually
  - *From: Kijai*

- **Problem:** SVI kills prompt adherence
  - **Solution:** Reduce SVI LoRA strength on high noise to 0.5-0.75 to balance SVI effect with prompt adherence
  - *From: Hashu*

- **Problem:** VAE decoding taking extremely long time
  - **Solution:** First triton run creates cache files causing 17+ minute delays, subsequent runs are normal 20 seconds
  - *From: patientx*

- **Problem:** KJNodes backward compatibility broken
  - **Solution:** Boolean value changes from False to false, need to refresh nodes or update manually
  - *From: Kijai*

- **Problem:** HuMo unhappy being used as I2V, creates transition issues
  - **Solution:** Use SVI 2.0 for 2.1 on the HuMo pass, and do color matching with true HuMo initial generation
  - *From: Ablejones*

- **Problem:** WanMove native spline editor IndexError when adding second spline
  - **Solution:** Update KJNodes - spline editor was outputting combined point count causing mismatch
  - *From: Kijai*

- **Problem:** Character jerking movement at start when reference frame put into first frame
  - **Solution:** Use LCM sampler instead of res4lyf schedulers which cause the problem
  - *From: 企鵝（50% CASH 50%GOLD）*

- **Problem:** Black video output with LightX2V
  - **Solution:** Update ComfyUI - was fixed yesterday
  - *From: Kijai*

- **Problem:** Cannot use CFG with WanMove
  - **Solution:** Bug fixed - negative prompt wasn't using tracks and needed proper casting
  - *From: Kijai*

- **Problem:** InfiniteTalk producing black outputs
  - **Solution:** Issue acknowledged but no solution provided
  - *From: WhimsicalZ*

- **Problem:** WanVideoVAE object has no attribute 'get' error
  - **Solution:** Re-download the model
  - *From: mallardgazellegoosewildcat2*

- **Problem:** cfg float list error when using NAG
  - **Solution:** Need actual negative prompt in main text encode, not just NAG. Empty prompt used for CFG steps
  - *From: Kijai*

- **Problem:** Flashing when using both reference images and start frame in HuMo
  - **Solution:** Use just start frame, avoid connecting both reference_images and start frame together
  - *From: Hashu*

- **Problem:** Snowing/washed out greyish artifacts in low noise video
  - **Solution:** Steps are too large - lower shift, change schedule
  - *From: Ablejones*

- **Problem:** 'free model and node cache' no longer works for recognizing new models
  - **Solution:** F5 to refresh page or use 'R' hotkey
  - *From: David Snow*

- **Problem:** Snow artifacts in video generation
  - **Solution:** Check sigma curves with Kijai's WAN Scheduler node, avoid splitting steps too far from 0.875 T2V or 0.9 I2V boundaries
  - *From: pookyjuice*

- **Problem:** Black generations with VACE
  - **Solution:** Use matching quantization types (both BF16) instead of mixing e5m2 normal and scaled
  - *From: Dream Making*

- **Problem:** NaN outputs and black generations
  - **Solution:** Try disabling SageAttention and using SDPA, or update SageAttention to latest version
  - *From: Kijai*

- **Problem:** VRAM getting stuck during generation
  - **Solution:** Add --reserve-vram 1 argument to ComfyUI startup to reserve 1GB VRAM
  - *From: Kijai*

- **Problem:** Custom node breaking unrelated workflows
  - **Solution:** Use --disable-all-custom-nodes to identify problematic nodes that monkey patch other components
  - *From: Gleb Tretyak*

- **Problem:** White and black frames inverted in VACE keyframe node
  - **Solution:** Update the node as the mask inversion was fixed
  - *From: Flipping Sigmas*

- **Problem:** Dark output videos with SCAIL
  - **Solution:** Try the pose downscaling instead of full pose, and use the I2V LoRA (lightx2v 2.1 I2V for SCAIL)
  - *From: Kijai*

- **Problem:** OOM error on 5090 with e4m3fn versions
  - **Solution:** Try deleting triton cache (C:\Users\username\.triton) and disable non-blocking on block swap if using wrapper workflow
  - *From: NebSH and Kijai*

- **Problem:** RAM error with torch script model
  - **Solution:** Try manually downloading the model file again, could be model file error
  - *From: Kijai*

- **Problem:** Pose frames leaking into main causing black artifacts
  - **Solution:** Use pose downscaling instead of full pose resolution
  - *From: Kijai*

- **Problem:** Issues with low sampler on Wan 2.2
  - **Solution:** Change the sampler - some nodes don't work properly with 2.2
  - *From: Dream Making*

- **Problem:** Keyframes too close together causing issues
  - **Solution:** Add auto spacing feature between keyframes
  - *From: Flipping Sigmas*

- **Problem:** Black border on top and left of FlashVSR output
  - **Solution:** Caused by ComfyUI-RMBG nodes - remove or update them
  - *From: Kijai*

- **Problem:** Merge_loras making VAE decoding slower
  - **Solution:** Disable force_offload or lower tile size to avoid RAM-VRAM transfer overhead
  - *From: Kijai*

- **Problem:** Uni3c incompatible with SCAIL (20 vs 21 channels)
  - **Solution:** Add 4 more frames to uni3c input to account for SCAIL ref taking one latent
  - *From: Kijai*

- **Problem:** RuntimeError: invalid vector subscript in NLF
  - **Solution:** Remove ComfyUI-RMBG nodes that globally override torch.jit settings
  - *From: Kijai*

- **Problem:** Face detection error in multi-person SCAIL
  - **Solution:** Disconnect dwpose input or disable face drawing if no faces detected
  - *From: Kijai*

- **Problem:** triton-windows compatibility issues
  - **Solution:** Downgrade from version 3.5 to 3.3 to match torch version
  - *From: boorayjenkins*

- **Problem:** SCAIL pose background leaking to main sequence
  - **Solution:** Ensure pose resolution is exactly half the main input resolution
  - *From: Kijai*

- **Problem:** SCAIL pose input makes everything dark/black if not downscaled
  - **Solution:** Use 2x downscaling for pose input as model was trained with downsampling
  - *From: teal024*

- **Problem:** REMBG nodes causing dependency conflicts
  - **Solution:** Uninstall REMBG custom nodes - they clash with newer ML dependencies
  - *From: cyncratic*

- **Problem:** SCAIL errors with landscape resolutions
  - **Solution:** Use portrait aspect ratios, resolution must be divisible by 32
  - *From: Flipping Sigmas*

- **Problem:** Hand drifting in SCAIL retargeting
  - **Solution:** Try crop instead of pad, use VITPose-H instead of L, bicubic interpolation
  - *From: Kijai*

- **Problem:** Multi-person SCAIL detection issues
  - **Solution:** Disconnect DWPose when using multi-person, feature not fully complete
  - *From: Kijai*

- **Problem:** Tensor mismatch caused by corrupted cached state when changing frame counts
  - **Solution:** Restart ComfyUI to clear the RoPE cache when switching between different frame counts or pose resolutions
  - *From: Flipping Sigmas*

- **Problem:** Bicubic interpolation fails on driving video but works on reference
  - **Solution:** Use Lanczos interpolation instead, which works reliably though slightly slower
  - *From: Kijai*

- **Problem:** SCAIL skeleton appears off-center regardless of input resolution changes
  - **Solution:** Issue appears related to retargeting alignment, may need manual adjustment of thresholds or turning off retargeting
  - *From: DawnII*

- **Problem:** First frame color bugs out or appears blurry/flashed
  - **Solution:** Avoid using LCM sampler which can discolor first frame, issue may also be related to LightX2V LoRA or scheduler
  - *From: 企鵝（50% CASH 50%GOLD）*

- **Problem:** IndexError when no pose detected in first frame
  - **Solution:** Ensure pose detection works on first frame, or code will use first valid pose found in sequence
  - *From: Kijai*

- **Problem:** Resolution mismatch errors in SCAIL
  - **Solution:** Width and height must be divisible by 32, and resized node dimensions must match the set width/height parameters
  - *From: Gleb Tretyak*

- **Problem:** CUDA allocation error with pose conditioning
  - **Solution:** Increase block swap amount as pose conditioning requires more VRAM than normal generation
  - *From: Kijai*

- **Problem:** RuntimeError with normalized_shape=[1280] in WanVideo Sampler v2
  - **Solution:** Re-download the clip_vision model - same name but file was corrupted
  - *From: patientx*

- **Problem:** NLF prediction hardcoded to use CUDA, won't work with CPU/ROCm
  - **Solution:** No current solution - would need to rebuild NLF and smplfitter repos
  - *From: Kijai*

- **Problem:** DEIS sampler throwing TypeError with cuda tensor conversion
  - **Solution:** Switch to other samplers - DEIS sampler has issues
  - *From: Dream Making*

- **Problem:** UnboundLocalError with callback_latent in UniPC sampler
  - **Solution:** Check if free_init connected by accident, verify doing actual steps, or use custom sigmas meant for 4 total steps
  - *From: Kijai*

- **Problem:** SCAIL nodes appearing red after installation
  - **Solution:** Update WanVideoWrapper nodes - SCAIL nodes were only merged into WanVideoWrapper recently
  - *From: Ablejones*

- **Problem:** No module named 'taichi' error with SCAIL
  - **Solution:** Install taichi dependency
  - *From: xwsswww*

- **Problem:** Resolution mismatch errors
  - **Solution:** Make sure all resolutions match exactly (e.g., not 512x895 vs 512x896), use crop to fix mismatches
  - *From: hicho*

- **Problem:** Wan 2.6 prompt rejection for violence terms
  - **Solution:** Remove words like 'scuffle', 'lunges', 'grabs', 'wrestling' - reframe as accidents or clumsiness instead of fights
  - *From: JohnDopamine*

- **Problem:** SCAIL pose skeleton drawing as flat surfaces instead of cylinders
  - **Solution:** Check taichi version with 'pip show taichi' or try changing render device to CPU
  - *From: Kijai*

- **Problem:** Getting 2 second video with 81 frames in SCAIL
  - **Solution:** FPS automatically pulled from input video - add Set FPS node to control output duration
  - *From: cyncratic*

- **Problem:** SCAIL multi-person hands/face jumping between people
  - **Solution:** Disconnect ref_dw_pose when doing multiple people - it doesn't work even in original implementation
  - *From: Kijai*

- **Problem:** VitPose to DWPose node crashing PC
  - **Solution:** Noted as system stability issue requiring restart
  - *From: Janosch Simon*

- **Problem:** WanVideoSamplerv2 shape error at 1280x720
  - **Solution:** Resolution must be divisible by 32 (use 1280x704) and set in the node properly
  - *From: Gleb Tretyak*

- **Problem:** VACE losing 2 frames (32 input, 30 output)
  - **Solution:** Use 4*n+1 frame count rule for Wan models
  - *From: 42hub*

- **Problem:** I2V model needs I2V embeds not empty embeds
  - **Solution:** Use proper embed type - empty embeds are for T2V only
  - *From: Kijai*

- **Problem:** SCAIL context windows cause background shift
  - **Solution:** Context windows don't work well with moving camera - try continue from last frame instead
  - *From: Kijai*

- **Problem:** Vitpose only returns one person detection
  - **Solution:** Use dwpose for multiple people and face detection
  - *From: Kijai*

- **Problem:** ImportError: Selected attention mode not available with SCAIL
  - **Solution:** Switch from SageAttention to SDPE attention mode - it's a version compatibility issue
  - *From: A.I.Warper*

- **Problem:** SCAIL generations coming out super dark
  - **Solution:** Make sure pose input is half the resolution of output - use math nodes to halve it
  - *From: Kijai*

- **Problem:** Yellow flash when using same image for start and end frames
  - **Solution:** Enable fl2v mode in the I2V encode node in WanVideoWrapper
  - *From: Kijai*

- **Problem:** Background changes during long SCAIL generations
  - **Solution:** Context windowing issue where each window tries to return to reference camera position/background, uni3c can help override this
  - *From: Kijai*

- **Problem:** VRAM memory issues with uni3c doubling time
  - **Solution:** Swap more blocks to avoid running out of memory
  - *From: Kijai*

- **Problem:** WAN move conditioning crashing with multiple tracks
  - **Solution:** When using different amounts of splines between spline editors, use separate spline editors for each track (3 spline editors with 3 masks)
  - *From: Gleb Tretyak*

- **Problem:** SCAIL example workflow cuts off frames (41 input to 37 output)
  - **Solution:** Follow the num_frames value of empty embeds - it generates as many frames as you input there
  - *From: Kijai*

- **Problem:** Uni3C controlnet loading error 'controlnet_blocks.0.bias'
  - **Solution:** No solution provided in chat
  - *From: A.I.Warper*

- **Problem:** Compounding error in long video generation causing oversaturation
  - **Solution:** Split video into separate 81 frame runs and splice together, or use depth-controlled second pass with context windows
  - *From: spacepxl*

- **Problem:** Pose detection issues with DWPose nodes
  - **Solution:** Connect Image dw Pose extractor output to Video Pose detection input, connect that to nlf dw pose. Set width/height from bottom Image resizer to top Video resizer
  - *From: Jumper*

- **Problem:** ComfyUI preview issues after update
  - **Solution:** Add --preview-method auto to command line or check new preview settings location in ComfyUI settings
  - *From: Hashu*

- **Problem:** InfiniteTalk Multi initial flash
  - **Solution:** Use clean image as first latent frame instead of noise. Can also use MultiTalk model which doesn't have this requirement
  - *From: Kijai*

- **Problem:** WanAnimate character replacement masking complexity
  - **Solution:** Use same mask for both background removal and generation area. Alternatively, add character in second pass instead of replacing to use smaller mask
  - *From: Kijai*

- **Problem:** Massive RAM usage with Wan 2.2 after ComfyUI update
  - **Solution:** Uncheck merge/low mem load options. Issue affects systems with 96GB RAM that previously worked
  - *From: Hoernchen*

- **Problem:** CFG > 1.0 error with mixed models
  - **Solution:** Error occurs when mixing 4 models (WanMove, UniAnimate, InfiniteTalk). Likely due to negative conditioning override from one of the models
  - *From: Kijai*

- **Problem:** SCAIL blackouts with animal pose
  - **Solution:** Use VitPose output directly with higher stick width (20), bypass conversion nodes. Draw thicker lines resembling NLF format
  - *From: Kijai*

- **Problem:** Multiple WanVideoWrapper versions causing issues
  - **Solution:** Check custom_nodes folder for different forks/branches like separate -bindweave folder that can cause conflicts
  - *From: Kijai*

- **Problem:** LongCat Avatar T2V giving NoneType error for audio_emb_slice
  - **Solution:** Need to still use extension node and provide audio somehow, can use old multitalk embeds input or set overlap to 0
  - *From: Kijai*

- **Problem:** First frame flash/noise issues with reference models
  - **Solution:** Decreasing mask value on first frame makes it worse, decreasing first_strength leads to stronger contrast shift - issue may be related to encode/decode differences
  - *From: Chandler ✨ 🎈*

- **Problem:** ComfyUI animated previews broken after latest update
  - **Solution:** Add start flag '--preview-method auto' without quotes
  - *From: Jumper*

- **Problem:** Error 'not enough values to unpack (expected 5, got 4)' after ComfyUI update
  - **Solution:** Update VHS (Video Helper Suite) nodes
  - *From: Kijai*

- **Problem:** TAESD preview errors
  - **Solution:** Disable TAESD previews, use latent2rgb instead. TAESD live previews never existed for video anyway
  - *From: Kijai*

- **Problem:** SCAIL BF16 model producing black screen
  - **Solution:** Try disabling prefetch_blocks and/or non-blocking in block swap node, or redownload model file
  - *From: Kijai*

- **Problem:** LongCat Avatar not working without blockswap on 5090
  - **Solution:** Model requires blockswap even at low resolutions like 480x480 due to 31GB model size
  - *From: burgstall*

- **Problem:** Mask list creating frames squared instead of single frame masks
  - **Solution:** Use 'mask list to batch' node to convert properly
  - *From: Kijai*

- **Problem:** Front end UI freezes in large workflows
  - **Solution:** Try using show any node from Comfy-easy-use instead of show text node
  - *From: David Snow*

- **Problem:** LongCat-Avatar not loading audio_proj model
  - **Solution:** Using wrong model - need to use avatar branch model, not normal model
  - *From: Kijai*

- **Problem:** LongCat-Avatar doesn't work in fp16
  - **Solution:** Use bf16 instead - original also uses bf16, fp16 causes issues
  - *From: Kijai*

- **Problem:** Dark output with speed-up LoRAs
  - **Solution:** Try different sageattn modes - overflow issues cause darkening
  - *From: Gleb Tretyak*

- **Problem:** Triton compilation error
  - **Solution:** Clear triton and torch inductor cache at %temp%\torchinductor_%username% and C:\Users\%username%\.triton\cache
  - *From: Ablejones*

- **Problem:** White flash at start of stand-in videos
  - **Solution:** Crop closer to the head, too much white background causes issues
  - *From: Kijai*

- **Problem:** ComfyUI crashes with 'Allocation on device' error
  - **Solution:** Not enough VRAM for the workflow, reduce blockswap or use lower settings
  - *From: Kijai*

- **Problem:** VACE RuntimeError: not enough memory allocating 724775731200 bytes
  - **Solution:** Issue with memory allocation when using 9 images, needs investigation of image dimensions and processing
  - *From: NebSH*

- **Problem:** LongCat Avatar scaled model gives noise with wrong quantization setting
  - **Solution:** LongCat-Avatar-single_fp8_e4m3fn_scaled_mixed_KJ.safetensors works with fp8_e4m3fn_scaled quantization (base_precision: bf16), not regular fp8_e4m3fn
  - *From: Wildminder*

- **Problem:** LongCat Avatar only shows first reference frame, rest black
  - **Solution:** Need to use bf16 base precision with LongCat models, ensure SageAttention 2.2.0 (not 1.0.6), and don't use refinement lora
  - *From: Kijai*

- **Problem:** Multiple WanVideoWrapper versions causing node import issues
  - **Solution:** Make sure there's no other wrapper nodes in custom_nodes folder, use latest version
  - *From: Kijai*

- **Problem:** LongCat Avatar breakdown after third pass in long generations
  - **Solution:** Looks like what happens when you don't give the same initial ref_latent to all extensions
  - *From: Kijai*

- **Problem:** SCAIL causing hand distortions and character inconsistency
  - **Solution:** Set pose control strength to 1.0 instead of 0.5, use reference images with similar proportions and positioning
  - *From: Kijai*

- **Problem:** Character head appearing gigantic and disproportionate in SCAIL
  - **Solution:** Ensure reference image and video have same resolution/aspect ratio, pad reference image if too tightly cropped
  - *From: Kijai*

- **Problem:** vitpose-h-wholebody.onnx not appearing in ONNX Detection Model Loader
  - **Solution:** Move the file from models/onnx to models/detection folder
  - *From: JohnDopamine*

- **Problem:** OOM on VAE decode for long videos
  - **Solution:** Use VAE Decode Batched from VHS nodes or reduce resolution from 1080p to 1280x720
  - *From: boorayjenkins*

- **Problem:** ComfyUI 0.5.1 and 0.6.0 breaking WanVideo
  - **Solution:** Downgrade to ComfyUI 0.5.0 or update to latest WanVideoWrapper which fixes the bug
  - *From: hicho*

- **Problem:** WanVideoWrapper getting stuck at sampling with cfg zero star
  - **Solution:** Update to latest version of WanVideoWrapper which fixes this bug
  - *From: Kijai*

- **Problem:** RuntimeError about tensors on different devices with context windows
  - **Solution:** Fixed in latest WanVideoWrapper update
  - *From: Kijai*

- **Problem:** Triton cache causing VRAM issues after updates
  - **Solution:** Clear Triton cache folders: C:\Users\<username>\.triton and C:\Users\<username>\AppData\Local\Temp\torchinductor_<username>
  - *From: Kijai*

- **Problem:** Text encoder taking forever to load
  - **Solution:** Use cached text encoder node to eliminate RAM/VRAM impact from text encoder
  - *From: Kijai*

- **Problem:** 'WanVideoSampler' object has no attribute 'noise_front_pad_num' error
  - **Solution:** Issue was with WanVideo Enhance-A-Video node breaking whole code when enabled. Fixed by Kijai.
  - *From: avataraim/Kijai*

- **Problem:** Sampling previews gone after ComfyUI update
  - **Solution:** Check main comfy menu settings (execution -> live preview method -> taesd), or add --preview-method taesd to cmd args. Refresh browser after changing.
  - *From: Gleb Tretyak/Kijai*

- **Problem:** Memory leaks with QwenVL implementation
  - **Solution:** Issues noted with existing qwenvl causing performance problems
  - *From: Gleb Tretyak*

- **Problem:** Docker dependency infinite loop issue
  - **Solution:** Disable automatic upgrade on ComfyUI startup to prevent conflicts between downgrade/upgrade cycles
  - *From: Gill Bastar*

- **Problem:** CUDA error with sageattention wheel
  - **Solution:** Error 'no kernel image available' likely due to torch version mismatch - wheel compiled with torch 2.7 but user has torch 2.9
  - *From: scf*

- **Problem:** WanVideoWrapper doing wrong number of steps after update
  - **Solution:** Rolled back to previous version, adjusted sigma to step node from 0.875 to 0.980 to get proper 50% step split
  - *From: Kenk*

- **Problem:** S2V not picking up input image after update
  - **Solution:** Issue noted but no specific solution provided
  - *From: Kenk*

- **Problem:** Getting blurry outputs with latest commit
  - **Solution:** Check step splitting - was caused by incorrect step allocation between high/low noise samplers
  - *From: Kenk*

- **Problem:** SVI Pro color changes between clips
  - **Solution:** Could be due to using fp8, sageattn, or different seeds - try weaker samplers like euler or LCM
  - *From: Kijai*

- **Problem:** Apple Silicon compatibility issues with Wan
  - **Solution:** Change Lanczos to CPU, set force offload to false, use WanVideo Sampler instead of V2 node
  - *From: buggz*

- **Problem:** Second sampler in SVI Pro eating RAM and becoming slow
  - **Solution:** Restart ComfyUI or do a short warmup generation first
  - *From: Zabo*

- **Problem:** SVI Pro not moving, staying at reference image
  - **Solution:** Need overlap frames of 8 for proper functionality
  - *From: DawnII*

- **Problem:** Load latent node looking in wrong folder
  - **Solution:** Core saves to output folder but loads from input folder - need to move files manually
  - *From: Kijai*

- **Problem:** Bright/gray output with SVI Pro native workflow
  - **Solution:** Issue was with LightX2V lora causing problems, removing it fixed the issue
  - *From: slmonker(5090D 32GB)*

- **Problem:** Light flashing between generations with SageAttention
  - **Solution:** Switching back to SDPA fixed the flashing issue
  - *From: DawnII*

- **Problem:** Gray pictures in wrapper vs native
  - **Solution:** Use Kijai's converted SVI loras instead of original repo loras, or set LightX2V 1030 strength to 0.6
  - *From: ucren*

- **Problem:** Preview not showing up in SVI Pro
  - **Solution:** Enable 'Show Progress Images During Generation' in ComfyUI main settings menu and refresh page before sampling
  - *From: Kijai*

- **Problem:** WanImageToVideoSVIPro node not found
  - **Solution:** Update ComfyUI manager first, then install KJNodes again
  - *From: MOV*

- **Problem:** LightX2V 1030 creates hard cuts instead of morphing in FMML
  - **Solution:** Use different LightX lora - older versions work better for morphing workflows
  - *From: VRGameDevGirl84(RTX 5090)*

- **Problem:** LoRA key not loaded errors when using SVI V2 Pro
  - **Solution:** Use the converted LoRAs from Kijai's HuggingFace repo
  - *From: Kijai*

- **Problem:** VAE loading error with Wan2_1_VAE_bf16.safetensors
  - **Solution:** Re-download the VAE file
  - *From: Kijai*

- **Problem:** Grey outputs in SVI wrapper
  - **Solution:** Update the wrapper nodes
  - *From: David Snow*

- **Problem:** Running out of 96GB system RAM when interpolating multiple scenes
  - **Solution:** Combine all batches first, then interpolate, rather than interpolating each batch separately
  - *From: Persoon*

- **Problem:** Loop nodes require ComfyUI cache to function properly
  - **Solution:** Do not disable ComfyUI cache when using loop nodes
  - *From: pagan*

- **Problem:** Image concatenate node fails on first loop iteration
  - **Solution:** Patch the node with: if source_images is None and new_images is not None: return new_images, new_images, new_images
  - *From: pagan*

- **Problem:** Missing WanImageToSVIPro node after updating
  - **Solution:** Update KJNodes pack and ComfyUI, delete and re-clone KJNodes if needed
  - *From: MOV*

- **Problem:** Numpy 2.2.6 breaks multiple nodes
  - **Solution:** Downgrade numpy version as older nodes won't work on numpy 2 versions
  - *From: Kijai*

- **Problem:** LoRA tensor size mismatch errors
  - **Solution:** Kijai fixed the issue with dora scale needing to be reshaped to 2 dim tensor - re-download required
  - *From: Kijai*

- **Problem:** ComfyUI preview stops working after restart
  - **Solution:** Use command arg --preview-method auto, latent2rgb, or taesd
  - *From: LukeG89*

- **Problem:** SVI Pro jumps back to original frame with camera movement
  - **Solution:** Works fine with static camera, use last frame of previous generation as anchor frame for camera movement
  - *From: Cseti*

- **Problem:** SAM3 not masking watermarks
  - **Solution:** Using 'watermark' as prompt doesn't work effectively
  - *From: Persoon*

- **Problem:** First frame appears burned in ultravico
  - **Solution:** Trim the first latent off prior to decoding or 4 frames prior to final save
  - *From: JohnDopamine*

- **Problem:** SVI 2.0 Pro causes video contrast drift
  - **Solution:** Use color matching techniques, batch image color matching can help
  - *From: BNP4535353*

- **Problem:** Washed up colors with color match node active
  - **Solution:** Use augment empty frames at 0.2-0.3 strength
  - *From: David Snow*

- **Problem:** High VRAM usage with VACE nodes
  - **Solution:** Use CPU cache for VAE, reduces to just under 24GB
  - *From: Lumifel*

- **Problem:** Tiled VAE degrades quality with VACE
  - **Solution:** Use CPU cache for VAE instead of tiled VAE
  - *From: Lumifel*

- **Problem:** SDE samplers too sensitive with DiT models in native
  - **Solution:** Use Clown samplers for stable SDE noise
  - *From: Ablejones*

- **Problem:** Loading model checkpoints with weights_only=False creates RCE vulnerability
  - **Solution:** Use .safetensors files which are generally considered safe, or ensure weights_only=True (default since PyTorch 2.6)
  - *From: tazztone*

- **Problem:** FreeLong workflows don't combine segments correctly
  - **Solution:** Fixed workflow to properly handle 1 frame overlap between segments
  - *From: Ablejones*

- **Problem:** SCAIL background shifts around 81 frame boundaries
  - **Solution:** Use reference image with homogeneous background like green screen, or use Uni3C camera control with static image to lock camera
  - *From: 42hub*


## Model Comparisons

- **Seed vs WAN vs Flash for upscaling**
  - Seed is nice but has flickering issues, WAN tends to change stuff (playing with Noise can help), FlashVSR was not really good
  - *From: Gill Bastar*

- **SAM3 vs SeC vs SAM2 for masking**
  - SAM3 > SeC > SAM2 in experience, SAM3 has text prompt to segment feature
  - *From: BitJuggler*

- **SteadyDancer vs WanAnimate**
  - Didn't see anything better than WanAnimate, lack of face control and long gen makes it complex to use
  - *From: Kijai*

- **Classic/tiled animatediff upscale vs newer solutions**
  - Feel like classic/tiled animatediff upscale pass is still probably the best for larger resolutions and higher framecounts
  - *From: Disco_Tek*

- **UltraViCo vs normal SageAttn**
  - UltraViCo runs twice as slow as normal sageattn on same frame count, but provides quality benefits for longer videos
  - *From: Kijai*

- **Kling O1 vs WanAnimate**
  - O1 matches input more closely especially in head area, but WanAnimate has better lighting and feels more natural. O1 is very cut and paste with awful lighting/color blend
  - *From: A.I.Warper*

- **Open source vs commercial models**
  - It's insane that we can even compare big commercial models to local free models
  - *From: dj47*

- **LongCat vs other extension methods**
  - LongCat is the best one for video extension, but otherwise extension methods are not great and degrade over time
  - *From: Kijai*

- **4 steps res_2s vs 8 steps euler**
  - 8 steps euler likely still beats 4 steps res_2s despite same NFE count
  - *From: spacepxl*

- **Higher order samplers vs euler for low step sampling**
  - If heun doesn't improve significantly over euler, higher order samplers don't matter
  - *From: spacepxl*

- **Q8 vs Q6 GGUF**
  - Differences are marginal, only slight noticeable errors in Q6
  - *From: David Snow*

- **Adversarial distillation vs trajectory-focused distillation**
  - Adversarial methods are timestep-sensitive and fragile, trajectory-focused methods like TCD are more robust
  - *From: mallardgazellegoosewildcat2*

- **Steadydancer vs WanAnimate for dancing**
  - Stepvideo is exceptional at dancing, Steadydancer not the smoothest but has good architecture
  - *From: mallardgazellegoosewildcat2*

- **SVI v1 vs v2**
  - V2 solves static object/camera issues that v1 had, but v2 feels washed out
  - *From: Hashu*

- **Training large LoRA vs training-free methods**
  - Still prefer taking largest affordable model and training big LoRA with lots of examples for character/subject and movement
  - *From: mallardgazellegoosewildcat2*

- **Aquif-Image vs Z-image**
  - Aquif has natural look vs Z-Image's over RLd artificial look
  - *From: yi*

- **Using lightx2v vs without**
  - With lightx2v there's more room for error, without everything is more sensitive to wrong params
  - *From: Kijai*

- **Radau vs Gauss solvers**
  - Radau more stable, Gauss higher order. Gauss wins until ODE instability gets bad, then Radau is better
  - *From: mallardgazellegoosewildcat2*

- **FILM vs RIFE interpolation**
  - FILM better for fast movement, RIFE better speed/quality tradeoff
  - *From: lostintranslation*

- **Mitchell vs Lanczos resampling**
  - Mitchell nicer to the eye, Lanczos still competitive and close to optimal
  - *From: mallardgazellegoosewildcat2*

- **SVI v2.0/SVI_Wan2.1 vs v2.0/SVI_Wan2.2**
  - v2.0/SVI_Wan2.1 permits 5 overlap frames while v2.0/SVI_Wan2.2 only allows up to 3 overlap frames
  - *From: 42hub*

- **Video DiTs vs Image DiTs parameter requirements**
  - Video DiTs need around 10x the tokens of img DiTs. 6B for video gonna be a bit squiffy, while img DiTs get at least somewhat okay at 2B
  - *From: mallardgazellegoosewildcat2*

- **OneToAll Animation vs WanAnimate**
  - OneToAll better at pose retargeting and reference keeping, but WanAnimate better at adherence. OneToAll potentially much better for long clips as WanAnimate degrades over time
  - *From: Kijai*

- **HunyuanVideo 1.5 vs Wan 2.2**
  - Wan 2.2 much better - HunyuanVideo 1.5 feels dumb and has uncontrolled camera movement
  - *From: slmonker(5090D 32GB)*

- **SteadyDancer vs WanAnimate**
  - SteadyDancer better at some things but doesn't handle longer videos well
  - *From: Gateway {Dreaming Computers}*

- **DepthAnything V3 vs V2**
  - V2 better quality - V3 looks like garbage for this use case
  - *From: David Snow*

- **OneToAll vs WanAnimate**
  - Still prefers wananimate, but hasn't spent much time optimizing OneToAll
  - *From: Josiah*

- **RCM vs regular on 2.2 I2v**
  - RCM has less artifacting and contrast variance, movement is less but not much movement was prompted
  - *From: DawnII*

- **Context windows vs extension method**
  - Context windows don't degrade (plus), but work worse overall (negative). Extension method is only option for really long sequences
  - *From: Kijai*

- **WanMove vs ATI**
  - WanMove seems better than ATI with less artifacts and clearer results, reuses most ATI functionality
  - *From: Kijai*

- **rCM LoRA vs Lightning LoRA for motion**
  - 1030 lightx2v LoRA on high noise gives much better motion than lightning LoRA
  - *From: Zabo*

- **IndexTTS-2 vs VibevoIce for emotional voice control**
  - IndexTTS-2 better for emotional voice control, VibevoIce has limited emotional range
  - *From: Gleb Tretyak*

- **TTS Audio Suite TTS-2 vs VibevoIce reliability**
  - Switched from VibevoIce to TTS-2 due to VibevoIce problems, much happier with TTS-2
  - *From: Chandler ✨ 🎈*

- **OneToAll vs WanAnimate**
  - O2A has great movement coherence but doesn't adhere to input/likeness as well as WanAnimate
  - *From: Josiah*

- **Wan 2.2 fp16 vs fp8_scaled vs GGUF Q8**
  - FP16 works fine if you have enough RAM, but gain isn't huge vs fp8_scaled or GGUF Q8
  - *From: Kijai*

- **Sage attention vs SDPA**
  - Sage uses more VRAM than SDPA by design, though SDPA can have issues on some setups
  - *From: Kijai*

- **1030 lora vs Lightning 4-step vs 480p lora**
  - 1030 good at prompt following but basic motion. 480p more active but erratic. Lightning 4-step not recommended
  - *From: metaphysician*

- **rCM vs lightx2v**
  - Couldn't get same results from rCM as 2.1 lightx2v in testing
  - *From: Kijai*

- **SVI vs regular continuation for consistency**
  - SVI great for consistency, awful for dynamic flow. Works by building image embedding differently
  - *From: Chandler ✨ 🎈*

- **Using quantization vs scaled fp8 or GGUF**
  - Quantization is slower to load and e5m2 is lowest quality, scaled fp8 or GGUF preferred
  - *From: Kijai*

- **SCAIL vs WanAnimate**
  - SCAIL feels better than WanAnimate for motion capture
  - *From: slmonker(5090D 32GB)*

- **Wrapper vs Native implementation**
  - Wrapper is much nicer than native and perhaps in wider use. Wrapper remains faster to embrace new models/experiments
  - *From: Scruffy*

- **Diffusers vs ComfyUI scheduler handling**
  - In diffusers beta sigmas are applied after shift, while in comfy it's other way around, leading to completely different sigmas when using beta
  - *From: Kijai*

- **FlowFrames vs ComfyUI RIFE node**
  - FlowFrames is much better - it's lightweight, has scene change detection and is fast
  - *From: 企鵝（50% CASH 50%GOLD）*

- **Kandinsky vs Wan 2.2**
  - Kandinsky better at human interactions, 24fps more natural motion, but slower. Wan has better ecosystem
  - *From: Benjimon*

- **STAR vs SeedVR2 for video upscaling**
  - SeedVR2 is better quality, STAR is old and nobody talks about it anymore
  - *From: Gill Bastar*

- **InspyreNet vs other background removal**
  - InspyreNet is probably my favorite for background removal
  - *From: cyncratic*

- **SCAIL vs Wan Animate**
  - SCAIL is better for plain pose control, Wan Animate is more for replacement and lipsync
  - *From: Kijai*

- **SCAIL vs Wan Animate for long duration**
  - SCAIL performs better than Wan Animate for long-duration generation
  - *From: Karthik*

- **SCAIL vs WanAnimate**
  - SCAIL better for ID retention and works better when image isn't same camera angle/size. WanAnimate better for facial performance but nukes ID too much
  - *From: A.I.Warper*

- **VACE vs WanAnimate for VFX work**
  - VACE is 10x more useful than wanimate for real VFX work
  - *From: spacepxl*

- **Lightning LoRAs vs base model quality**
  - Lightning gives less motion/structure variety but better detail quality. Lightning with 8 steps gives much better detail quality than base model with ~30 steps
  - *From: spacepxl*

- **Wan 2.6 vs Veo 2**
  - Veo 2 still looks more real than Wan 2.6
  - *From: Ruairi Robinson*

- **Wan 2.6 quality assessment**
  - Quality looks ok at start then degrades, looks overlit, oversaturated, over contrasty instead of natural and photographic
  - *From: Ruairi Robinson*

- **Wan 2.6 vs 2.5**
  - 2.6 outputs are genuinely worse than 2.5, lacks visual fidelity despite being newer
  - *From: DawnII*

- **Wan 2.6 vs LTX**
  - Looks like LTX but worse than wan 2.1, has same plastic coating look
  - *From: spacepxl*

- **Wan 2.6 sound vs Kling/Sora**
  - Sound is shit compared to Kling 2.6 or Sora, uses mmaudio
  - *From: asd*

- **SCAIL vs other models**
  - SCAIL is the best for now, especially for complex motions
  - *From: slmonker(5090D 32GB)*

- **CFG settings impact on speed**
  - 50 steps with cfg = 100 model passes vs 4 steps with cfg 1.0 = 4 model passes
  - *From: Kijai*

- **TurboDiffusion vs LightX2V**
  - Weights didn't seem better than LightX2V, misleading 'lossless' claims with visible quality loss
  - *From: Kijai*

- **SCAIL vs WanAnimate for character retargeting**
  - SCAIL better for very different character sizes (chibi vs human), WanAnimate better for backgrounds without shifts
  - *From: Juan Gea*

- **Wan 2.6 cost vs other services**
  - Wan 2.6 costs $6.70 for 15s video on FAL, extremely expensive
  - *From: Drommer-Kille*

- **DF11 vs fp16 models**
  - 100% identical quality to fp16 but 30% smaller file size, 5-20% slower than fp8 but faster than bf16
  - *From: Ada*

- **SCAIL vs WanAnimate for character swapping**
  - WanAnimate holds up much better for long runs, SCAIL has issues with close-up face detection
  - *From: xwsswww*

- **Wrapper vs native nodes for Wan 2.1**
  - Wrapper generates significantly better videos, default LoRAs (480p cfg distill) work better than 1030 high + 1022 low
  - *From: Danial*

- **SCAIL vs WanAnimate for reconfiguration**
  - SCAIL does much better with re-configuring body proportions, especially for non-human and exaggerated features. WanAnimate claims to reconfigure but doesn't actually do it well
  - *From: amli*

- **SCAIL vs WanAnimate for faces**
  - SCAIL cannot do faces very well at all, WanAnimate is better for faces
  - *From: AIGambino*

- **SCAIL vs WanAnimate for video processing**
  - SCAIL animates image as whole, WanAnimate still king for swapping someone in existing video. WanAnimate better for long gen stability
  - *From: HeadOfOliver*

- **GIMM VFI vs RIFE for frame interpolation**
  - GIMM seems much better than RIFE
  - *From: dj47*

- **fp16 vs bf16 precision**
  - fp16 has significantly more precision than bf16. bf16 gives roughly 8 bit precision in half the image range (0.5-1.0)
  - *From: spacepxl*

- **1.3B vs 5B models**
  - 1.3B is better than 5B
  - *From: spacepxl*

- **New LightX2V 1217 vs Lightning vs Dyno**
  - Old lightning and dyno still better - new 1217 has weird colors, too much contrast, less dynamic movement
  - *From: crinklypaper*

- **InfiniteTalk Multi vs MultiTalk**
  - MultiTalk slightly better at single speaker tasks, both can do single speaker but optimized for their specific use cases
  - *From: Kijai*

- **Adding character vs replacing character in WanAnimate**
  - Adding character in second pass works better - smaller mask, cleaner results, faster processing
  - *From: boorayjenkins*

- **WorldCanvas vs WanMove**
  - WorldCanvas more feature rich, uses 2.2 weights with VACE-like features vs WanMove's plain 2.1 I2V
  - *From: Kijai*

- **LongCat Avatar vs Infinite Talk**
  - LongCat is slower (10 steps vs 4-6 steps) but runs at 16fps vs 25fps, so actually faster in that sense. Main advantage is prevention of repetitive actions in long gens
  - *From: Kijai*

- **FlashPortrait vs FantasyPortrait for short generations**
  - FlashPortrait is worse than FantasyPortrait for single short generations, seems made for long generation method only
  - *From: Kijai*

- **SVI prompt following and movement**
  - SVI is very bad at following prompt and movements, difficult to fix
  - *From: Zabo*

- **10 steps with distill LoRA vs 40 steps with cfg 3.0**
  - Both produce similar quality results for LongCat Avatar
  - *From: Kijai*

- **LongVie2 with vs without self_attn layers on Wan 2.1**
  - Both work for depth control, unclear how much the additional layers improve results
  - *From: Kijai*

- **Uni3C compatibility with LongCat Avatar**
  - Not compatible at all - LongCat is based on Wan architecture but trained from scratch
  - *From: Kijai*

- **HUMO vs STAND-IN facial consistency**
  - HUMO does facial consistency very well, but below ~65 frames starts losing consistency and becomes grainy. STAND-IN works fine even with very few frames (as low as 9) and is close to HUMO in reference preservation, though not quite at the same level
  - *From: ▲*

- **LongCat Avatar vs InfiniteTalk**
  - For long gen it's better simply because it doesn't repeat itself like InfiniteTalk does
  - *From: Kijai*

- **WanMove vs ATI**
  - It's like ATI but a lot better
  - *From: Kijai*

- **Sage vs Flash vs SDPA attention**
  - sage >>>>>>>>>>>>>>> flash > sdpa with slight exaggeration
  - *From: Kijai*

- **q4_km GGUF vs fp8 scaled Wan models**
  - q4km uses less VRAM and allows more frames for upscaling
  - *From: craftogrammer*

- **vitpose-h-wholebody vs vitpose-l-wholebody**
  - H version provides better pose detection results
  - *From: ucren*

- **4090 vs dual 3090 performance**
  - Single 4090 is twice as fast for Wan, 5090 is maybe 3x faster. Dual 3090 better for LLM due to more VRAM
  - *From: Benjimon*

- **SageAttention 2.1/2.2 vs SageAttention 3**
  - Sage 2.1/2.2 are still mainstream options, Sage 3 has way too high quality loss on 2.1 to be useful
  - *From: Kijai*

- **SageAttention vs TeaCache**
  - SageAttention is almost lossless compared to TeaCache which caused noticeable detail loss and limb deformities
  - *From: slmonker*

- **Foley vs MMAudio for audio generation**
  - MMAudio preferred, foley sucks
  - *From: Benjimon*

- **fp4 vs fp8 quality**
  - fp4 has noticeable quality drop compared to fp8
  - *From: cyncratic*

- **Kandinsky vs Wan**
  - Better at some things but doesn't listen as well and is slower, worth using for some specific cases
  - *From: Benjimon*

- **Lightning LoRAs vs newer distill LoRAs**
  - Avoid Lightning-based LoRAs especially for T2V due to big impact on generation content, use newer distill LoRAs from 11 days ago
  - *From: Kijai*

- **SVI vs SVI Pro motion adherence**
  - Regular SVI had more change/variety compared to SVI Pro which is more restrictive
  - *From: NebSH*

- **LightX2V 1030 vs 1022**
  - 1022 works better with SVI Pro, 1030 had issues with gray output
  - *From: DawnII*

- **High noise with vs without LightX2V**
  - Without LightX2V produces much better motion, more natural pacing
  - *From: slmonker(5090D 32GB)*

- **SVI vs StorymMem for camera movement**
  - StorymMem better for prompt adherence, SVI has better continuity but fights camera prompts
  - *From: Kijai*

- **Different alpha values for ultravico**
  - 0.95 alpha doesn't allow subject to leave frame, first frame alpha 0.95 with rest 0.8 shows promise
  - *From: Kijai*

- **SVI Pro vs manual I2V continuation**
  - SVI Pro is amazing and better than manual last image continuation method
  - *From: avataraim*

- **Motion scale node vs Painter**
  - Motion scale node works better than painter and doesn't make camera go wild
  - *From: Zabo*

- **Ultravico with I2V vs T2V**
  - Harder to use with I2V because it decays the image conditioning, works better with T2V
  - *From: Kijai*

- **Original 2.1 VACE vs Fun VACE 2.2**
  - Original 2.1 better for reference images and inpainting, Fun 2.2 better for depth and pose controls
  - *From: Ablejones*

- **SVI vs HuMo for lipsync**
  - SVI doesn't do lipsync, HuMo still the goto for lipsync
  - *From: NebSH*

- **Storymem vs SVI Pro 2.0**
  - Storymem introduces huge color drift, SVI Pro makes prompts almost fully ignored
  - *From: Gleb Tretyak*

- **SCAIL vs WanAnimate**
  - SCAIL better at complex movements like spinning and multiple characters; WanAnimate better at facial expressions and has two mechanisms for >81 frames vs SCAIL's one
  - *From: 42hub*

- **FreeLong vs raw I2V vs SVI 2.0 Pro**
  - Raw I2V expected to do similar job, SVI 2.0 Pro expected to be even better than FreeLong
  - *From: 42hub*

- **FreeLong vs non-FreeLong generation**
  - FreeLong doesn't improve continuity, right side looked nicer but took twice as long with more complex background
  - *From: Ablejones*


## Tips & Best Practices

- **For maximum speed with compile working, use 'comfy' rope function and enable allow_unmerged_lora_compile if you don't merge loras**
  - Context: When torch compile is working properly
  - *From: Kijai*

- **For VACE inpainting with masks, use full denoise to get VACE to recreate original unmasked part**
  - Context: When doing inpainting operations
  - *From: Ablejones*

- **Can simulate denoise by using non-binary mask to set how much you want area to change, keeping denoise at 1**
  - Context: Alternative to lowering denoise for masked areas
  - *From: Ablejones*

- **Do control only for few steps by ending it early**
  - Context: For getting creative variations with VACE pose/depth control
  - *From: Kijai*

- **Vace works with lower denoise for video-to-video, but for inpainting must keep denoise at 1**
  - Context: Different denoise strategies for different use cases
  - *From: hicho*

- **For VACE 17 frames to match OpenPose properly, feed it to ControlVideo**
  - Context: When working with VACE workflows
  - *From: NodeMancer*

- **Use blank background/huge homogenous level floor + subsequent background outpainting with VACE for SteadyDancer**
  - Context: Background may be problematic with SteadyDancer, works better with context windows for long videos
  - *From: 42hub*

- **Make bird subject fill the whole reference frame and increase mask size**
  - Context: When inserting small subjects like birds into scenes with Wan 2.2 Animate
  - *From: 🦙rishappi*

- **Use pose closer to first frame if you don't want transition effects**
  - Context: When using start image with pose control in Wan
  - *From: Kijai*

- **For CFG schedules, avoid CFG schedule float list with certain samplers**
  - Context: When setting up NAG workflows
  - *From: David Snow*

- **Use eta of 0.5 or greater for SDE sampling**
  - Context: Works fine even with low steps if implementation is correct
  - *From: Ablejones*

- **Test heun sampler to check if higher order sampling helps**
  - Context: Quick test to see if 2NFE per step improves quality enough to be worth it
  - *From: spacepxl*

- **Use gradient estimation sampler for 1NFE with momentum**
  - Context: Sometimes gives good results but depends on the model, works well with restart sampler
  - *From: mallardgazellegoosewildcat2*

- **Upscale whole video then downscale and blur to match**
  - Context: Gets better details when working with limited resolution source
  - *From: spacepxl*

- **Use film grain injection before upscaling for more detail**
  - Context: When doing creative upscaling to add detail to video generations
  - *From: David Snow*

- **Use last 5 frames of first video as start_image for next video with SVI-Film lora**
  - Context: For 15 second I2V generations when SVI isn't working properly
  - *From: Ablejones*

- **Motion frame setting of 5 works for new SVI 2.0, higher values create jumpy overlaps**
  - Context: Using SVI 2.0 lora for video extension
  - *From: xiver2114*

- **Image upscale is better than latent upscale**
  - Context: Multi-pass video generation workflow
  - *From: David Snow*

- **Always look at hair quality to judge video generation quality**
  - Context: Evaluating AI video generation results
  - *From: FL13*

- **Use explicit caching by saving/loading images instead of relying on ComfyUI cache**
  - Context: When working with image batches and masks to avoid recomputation
  - *From: mallardgazellegoosewildcat2*

- **Switch to ComfyUI API to control with python and dodge half the bugs**
  - Context: When dealing with memory management issues
  - *From: mallardgazellegoosewildcat2*

- **Use Claude for code review to check for malicious code**
  - Context: When installing unknown ComfyUI nodes
  - *From: JohnDopamine*

- **Use minimal workflow to diagnose memory issues**
  - Context: When troubleshooting memory leaks or other ComfyUI issues
  - *From: Kijai*

- **Test with --disable-all-custom-nodes to isolate problems**
  - Context: When experiencing crashes or memory issues that might be caused by custom nodes
  - *From: Kijai*

- **Always update torch, torchvision, and torchaudio together**
  - Context: When updating PyTorch to avoid version sync issues
  - *From: spacepxl*

- **Treat SVI like svi-film for overlap frames**
  - Context: Frames should be unmasked, wasn't trained the same way as SVI 2.0 for wan2.1
  - *From: Ablejones*

- **Use high noise LoRA at 0.5 to get more motion/prompt following**
  - Context: When working with SVI workflows
  - *From: Hashu*

- **Check KJ's example workflow for cleaner SVI implementation**
  - Context: Has nice new-ish node that collapses complexity
  - *From: Hashu*

- **Important to note GGUF behavior when using LoRAs**
  - Context: Models like GGUF don't allow merging, thus lora weights are added on top of the de-quantized weight when used
  - *From: Kijai*

- **HuMo does amazing job using reference inputs without too much bias for their input positions**
  - Context: For extension work without using start images
  - *From: Ablejones*

- **Use strength 1.0 with LightX2V LoRAs**
  - Context: Normal usage
  - *From: DawnII*

- **Better hardware doesn't improve quality, only speed**
  - Context: Quality is same on all cards, just faster on better hardware due to memory hierarchy
  - *From: mallardgazellegoosewildcat2*

- **OneToAll Animation sensitive to prompts**
  - Context: Prompting for something else can override the reference
  - *From: Kijai*

- **Reference adherence suffers from misaligned pose and LightX2V**
  - Context: When using OneToAll Animation
  - *From: Kijai*

- **PainterI2V motion amplitude tradeoff**
  - Context: More motion with distill at cost of contrast changes and prompt following. Motion amplitude of 1 might as well not use painteri2v
  - *From: DawnII*

- **Use TTM for best results without audio facial expressions**
  - Context: Time to Move is considered best so far, only issue is can't do audio facial expressions and mouth movements
  - *From: xwsswww*

- **Normalize latent mean and standard deviation each step**
  - Context: Can help with saturation changes in video generation
  - *From: mallardgazellegoosewildcat2*

- **SeedVR2VideoUpscale removes artifacts**
  - Context: Running init image through SeedVR2VideoUpscale first helps with eyes and finer details
  - *From: 企鵝（50% CASH 50%GOLD）*

- **Use 1030 or 1030+1020 on high noise, any wan 2.1 t2v/i2v on low for best I2V results**
  - Context: LightX2V LoRA configuration
  - *From: FL13*

- **Higher LoRA rank closer to full model but diminishing returns above rank 64**
  - Context: LoRA rank selection, larger file size matters for unmerged/GGUF
  - *From: Kijai*

- **Sometimes rank 4-8 can be 90% effective with much smaller size**
  - Context: LoRA optimization
  - *From: Kijai*

- **Use noise injection for wider range of settings tolerance**
  - Context: Better results with SDE that injects noise every step
  - *From: mallardgazellegoosewildcat2*

- **Bump audio cfg to 1.4 or 1.5 for better lip sync in InfiniteTalk**
  - Context: Audio-driven lip sync optimization
  - *From: Charlie*

- **Can adjust trajectory paths instead of tweaking variables for better control**
  - Context: WanMove provides more intuitive control method
  - *From: Kijai*

- **For SVI motion problems, outpaint input image to 480×832 horizontal ratio**
  - Context: SVI trained at 480×832 horizontal, doesn't perform well with very different aspect ratios especially vertical with full-body person
  - *From: xiver2114*

- **Use HuMo at end of flow for better lip sync**
  - Context: When combining multiple models, HuMo works better at the end rather than beginning
  - *From: Scruffy*

- **Adjusting SVI lora strength may affect camera movement**
  - Context: When trying to get more camera movement with SVI
  - *From: Kijai*

- **For SVI 2.2, set 1 frame overlap but provide first 5 frames anyway**
  - Context: Proper setup for SVI 2.2 compared to SVI shot
  - *From: Ablejones*

- **Use precise prompts for NAG instead of huge negative spam prompts**
  - Context: NAG works better with targeted negatives rather than long lists
  - *From: Kijai*

- **Very low CFG should be used with low steps**
  - Context: When using CFG with few steps
  - *From: Kijai*

- **At least one step with CFG makes such a difference**
  - Context: For video generation quality
  - *From: Kijai*

- **Lightning lora on low produces sharper results but changes too much**
  - Context: For I2V generation
  - *From: David Snow*

- **Use manual venv install for ComfyUI**
  - Context: Easiest in the long run for maintaining stable setup over time
  - *From: Kijai*

- **VACE uses T2V sigma boundary of 0.875**
  - Context: Not 0.9 like I2V, important for proper VACE functionality
  - *From: pookyjuice*

- **For 5090 users, use 'auto' mode**
  - Context: Optimal performance setting for RTX 5090
  - *From: Kijai*

- **SCAIL model works best with 896x512 resolution**
  - Context: Not meant for face-only input, needs more body content
  - *From: Kijai*

- **WanAnimate output frames must be divisible by 4 after first frame**
  - Context: Explains why sometimes output has 2-3 fewer frames than input
  - *From: Kijai*

- **Use LightX2V LoRA with SCAIL**
  - Context: For SCAIL use the lightx2v 2.1 I2V LoRA for better results
  - *From: Kijai*

- **Use Skyreel LoRA with T2V for extended frames**
  - Context: Can use Skyreel LoRA with T2V 2.2 to push to 121 frames, use strength higher than 1.0
  - *From: NebSH and Kijai*

- **Use e4m3fn for Blackwell GPUs**
  - Context: Usually e4 for blackwell architecture GPUs if I remember rightly
  - *From: mallardgazellegoosewildcat2*

- **Join multiple reference images manually**
  - Context: For VACE with multiple references, join them into a single image yourself as the model can only use one image
  - *From: Kijai*

- **Buy RAM/SSDs quickly**
  - Context: RAM and SSD prices are rising rapidly - buy as quickly as possible to avoid paying double
  - *From: David Snow*

- **Use 6 images max for 81 frames**
  - Context: 6 images is probably too much for 81 frames, try with 5 only
  - *From: NebSH*

- **Use fp16_fast for faster WanMove generation**
  - Context: When using WanMove model
  - *From: Kijai*

- **Add stationary points where swing chains attach to prevent unwanted movement**
  - Context: When creating swing motion in WanMove
  - *From: Kijai*

- **Use path filters with noise or sine wave for more natural movement**
  - Context: Making camera movements look less mechanical
  - *From: Kijai*

- **720p makes significant difference over 480p for face quality**
  - Context: When working with face-focused content
  - *From: FlipYourBits*

- **Segment faces without stretching for better results**
  - Context: Face processing workflows
  - *From: FlipYourBits*

- **Use 5-frame overlap with SVI-film for context window transitions**
  - Context: When splitting long sequences across context windows
  - *From: Kijai*

- **Clamp should be turned off for LoRA extraction**
  - Context: It seems unnecessary and even detrimental for quality
  - *From: Kijai*

- **Don't use adaptive setting for LoRA extraction anymore**
  - Context: Standard setting works better than adaptive
  - *From: Kijai*

- **Use rank 256 for LoRA extraction as starting point**
  - Context: Good balance for testing, can adjust higher if needed
  - *From: Gleb Tretyak*

- **512x896 resolution yields optimal SCAIL results**
  - Context: This is the tested and recommended resolution
  - *From: teal024*

- **Use longer prompts for better control**
  - Context: When using SCAIL for both motion and background control
  - *From: teal024*

- **Generate at lower resolution first before upscaling**
  - Context: 720p or lower first gives better motion and prompt adherence, then upscale
  - *From: FL13*

- **Use 1080p direct generation for best quality**
  - Context: Output size is the biggest contributor to quality, larger generations have better motion
  - *From: ingi // SYSTMS*

- **Crop ultra long driving hands**
  - Context: Cropping can fix hand extension issues in driving videos
  - *From: Gleb Tretyak*

- **Use v2v workflow for enhanced quality**
  - Context: Upscale then v2v with low noise model works well though takes longer
  - *From: FL13*

- **Use CFG schedule for better motion**
  - Context: Using 2 on first step and cfg 1 for rest with lightx2v LoRAs
  - *From: FL13*

- **Match distill LoRA strengths to total around 1**
  - Context: When mixing multiple distill loras
  - *From: spacepxl*

- **Refresh page after downloading models**
  - Context: Press 'R' to refresh or F5 after downloading SCAIL models
  - *From: David Snow*

- **Higher resolution helps reduce glitchy fingers more than steps**
  - Context: Going higher res helps get less glitchy fingers more than steps, even 12
  - *From: Gleb Tretyak*

- **Use thicker sticks and correct colors for pose visualization**
  - Context: When working with pose generation and visualization
  - *From: Kijai*

- **Use Wan 2.6 generation to access 2.5 for free without queue**
  - Context: Best thing about 2.6 is bypassing 2.5 queues
  - *From: DawnII*

- **SCAIL works better for complex motions, use VACE/Fun Control for simple ones**
  - Context: When choosing between pose control models
  - *From: Kijai*

- **Lora training could help with SCAIL context window morphing**
  - Context: When features not in init image cause morphing issues
  - *From: Kijai*

- **Two-pass approach for longer SCAIL videos**
  - Context: First continue from last frame, then run vid2vid context windows to smooth transitions
  - *From: Kijai*

- **Use dwpose output with SCAIL for face detection**
  - Context: When you need faces in SCAIL pose detection
  - *From: Kijai*

- **Increase overlap for better context windows**
  - Context: Makes generation slower but improves quality
  - *From: Kijai*

- **Choose 'all frames' to avoid frame skipping**
  - Context: When you want higher fps output matching input video
  - *From: Kijai*

- **Use cross dissolve for SCAIL continuations**
  - Context: Overlap 16 frames and cross dissolve in Comfy or externally until model supports continuations
  - *From: 42hub*

- **Use first frame of video as reference with similar pose/position for better SCAIL results**
  - Context: When doing character replacement in SCAIL
  - *From: avataraim*

- **End uni3c early to speed up generation**
  - Context: Uni3c doesn't have much effect after 1-2 steps, can end at 0.01
  - *From: Kijai*

- **Keep fl2v mode always enabled in wrapper**
  - Context: Only affects last frame encoding when provided, makes workflows more consistent
  - *From: Kijai*

- **Use separate prompts for different context windows**
  - Context: Remove/add prompt elements between windows for better consistency (like 'holding onto her dress' or 'glasses')
  - *From: Kijai*

- **Use SCAIL first then WanAnimate for professional results**
  - Context: Use SCAIL for initial character retarget, then WanAnimate for motion detection based on SCAIL video for stability
  - *From: Juan Gea*

- **Use DWPose instead of VitPose for multiple people**
  - Context: VitPose only does one person at a time while DWPose can handle faces for multiple people
  - *From: Kijai*

- **Use first frame as pose control for initial image render**
  - Context: When working with multiple people to avoid positioning issues
  - *From: boorayjenkins*

- **For HDR without training, lower exposure and inpaint highlights with differential diffusion**
  - Context: Can do this multiple times to get more range
  - *From: spacepxl*

- **Use separate processes/models as different tools**
  - Context: Like going from Houdini simulation to Blender for shading - use SCAIL for retargeting, then WanAnimate for stability
  - *From: Juan Gea*

- **For precise face detailing, create stable animated mask**
  - Context: SAM3 masks vibrate, better to use steady animated mask with spline editor to avoid stitching artifacts
  - *From: Juan Gea*

- **Reduce LoRA strength to improve character consistency**
  - Context: When using multiple control methods like WanAnimate, it's a tradeoff with model accuracy (motion, noise, artifacting)
  - *From: Josiah*

- **Generate driving video with character first**
  - Context: Makes I2V/character swap more effective by using WanAnimate to create the driving video
  - *From: Josiah*

- **Use T2V with FOMO instead of I2V for full VACE access**
  - Context: T2V gives full access to VACE features vs limitations with I2V
  - *From: Grimm1111*

- **Skip first 4 frames and add more features if first frame issues**
  - Context: When having trouble with first frame requirements in models like InfiniteTalk
  - *From: Gleb Tretyak*

- **Avoid complex prompts with parentheses in WanVideoWrapper**
  - Context: Parentheses trigger weight multiplication that can cause severe artifacts
  - *From: Gleb Tretyak*

- **For SCAIL with animals, match NLF colors**
  - Context: Draw poses where left side is 'warm' colors and right side is 'cool' colors to match NLF format
  - *From: Kijai*

- **Lower audio_cfg can tone down excessive motion**
  - Context: When using audio-driven models like LongCat Avatar
  - *From: Kijai*

- **Re-color skeleton to same color scheme for better rotations**
  - Context: When not using SCAIL pose, the model learned left/right sides by cool/warm colors
  - *From: Kijai*

- **Old distill LoRA probably ruins longer generations**
  - Context: When using LongCat Avatar with older distillation LoRAs
  - *From: Kijai*

- **Use humanoid rig for humanoid characters rather than primitives**
  - Context: For animation control, free rigs from mixamo or accurig work well with SCAIL
  - *From: dj47*

- **Use first segment latent as reference for consistency in LongCat Avatar extensions**
  - Context: For clips around 20 seconds, changes won't be very noticeable, especially without drastic head turns
  - *From: slmonker(5090D 32GB)*

- **Set overlap to 0 for T2V LongCat Avatar**
  - Context: When using empty image as first frame for T2V generation
  - *From: Kijai*

- **Use previous latent from last sample as reference for extensions**
  - Context: When extending videos, use the first latent of the result as reference for next extension
  - *From: Kijai*

- **Lower audio_cfg to avoid excessive tooth exposure**
  - Context: High audio_cfg (like 3.0) often causes over-exposed teeth, especially with distill LoRA or low steps
  - *From: Kijai*

- **Use higher temporal offset for better results**
  - Context: Made default in stand-in implementation after testing showed improvement
  - *From: Kijai*

- **Use EasyCache starting at step 5 for LongCat**
  - Context: When total steps are 10, don't start cache at default 10 steps
  - *From: burgstall*

- **Adjust start step instead of denoise for easier understanding**
  - Context: When doing refinement passes with low denoise values
  - *From: Kijai*

- **Enable add_noise option when using start step**
  - Context: When forgetting denoise value and using start step method
  - *From: Kijai*

- **Always share full error and workflow when asking for help**
  - Context: Saves everyone time when troubleshooting
  - *From: Kijai*

- **Use chunked FFN for LongCat by default**
  - Context: Drops peak VRAM by ~2GB without visible speed loss
  - *From: Kijai*

- **Use vocal extraction for better lip sync results**
  - Context: For lip-sync models, extract vocals first, use only the vocal track as audio input for lip-syncing, then add instrumental back in editing
  - *From: Kijai*

- **Add noise after vocal extraction for LongCat-Avatar**
  - Context: LongCat-Avatar doesn't handle absolute silence, so some noise is added after vocal extraction for generated embeds
  - *From: Kijai*

- **PUSA LoRA helps with facial consistency**
  - Context: Adding PUSA lora to Stand-In at 0.5 to 1 strength improves facial consistency significantly
  - *From: ▲*

- **Use SEGS Detailer for distant face issues**
  - Context: For faces in the distance that lose likeness, use the SEGS Detailer from Impact node pack fork as an extra pass
  - *From: 42hub*

- **Quality loss from sage is offset by speed gain**
  - Context: The quality loss from sage is so small in most cases that you can more than offset it from the speed gain
  - *From: Kijai*

- **Remove background from reference video for better motion transfer**
  - Context: When using SCAIL for pose transfer
  - *From: ucren*

- **Use similar proportions between reference image and video**
  - Context: Improves SCAIL motion transfer quality
  - *From: souoNeo*

- **Force reference video and output to same frame rate**
  - Context: 16fps recommended for both input and output in SCAIL workflows
  - *From: ucren*

- **Use Qwen Image Edit to prepare reference images**
  - Context: Get character closer to initial frame of reference video before using SCAIL
  - *From: souoNeo*

- **Cache latents to disk for multi-step workflows**
  - Context: Saves time when experimenting with long video workflows that take an hour to generate
  - *From: boorayjenkins*

- **Turn off merge_lora and use minimum block_swap**
  - Context: Reduces 'Loading transformer parameters' time
  - *From: trykiss*

- **Use batch encode node instead of normal encode for multiple reference images**
  - Context: When working with multiple reference images in windowed context
  - *From: Kijai*

- **Disconnect DWPose from input image and NLF node if you want to adapt input image to original video instead of scaling video skeleton to image**
  - Context: When using SCAIL and want different behavior
  - *From: DawnII*

- **Use 1030 iteration after 1022 for lightx models**
  - Context: 1030 is next iteration and might give better results
  - *From: 42hub*

- **Start with 0.3 strength for motion morph LoRAs**
  - Context: When using FlippinRad Motion Morph LoRA for improving morphs
  - *From: 42hub*

- **Use 6 steps instead of 4 for LightX2V when mixing in CFG**
  - Context: 4 is hard to tune properly, 6 gives more room especially with CFG
  - *From: Kijai*

- **Use first step with CFG and remaining steps without**
  - Context: Works better with at least 6 steps total
  - *From: Kijai*

- **Train individual LoRAs in smaller batches instead of one large finetune**
  - Context: For datasets with multiple concepts - easier to confirm adherence and merge later
  - *From: CJ*

- **Use cfg under 2.0 for low CFG with LightX2V**
  - Context: When doing 4 steps with low CFG
  - *From: Kijai*

- **Always run second pass or upscale pass for solid quality**
  - Context: SageAttention loss becomes negligible with additional processing
  - *From: cyncratic*

- **Use start/end steps instead of denoise for clarity**
  - Context: Denoise rounds values and causes confusion with low step counts
  - *From: Kijai*

- **Multiply entire sigmas schedule by 0.0-1.0 for fine grain denoise control**
  - Context: Gives infinite control, 0.90 factor may be like 0.5 denoise
  - *From: Ablejones*

- **Use fp32 VAE only for initial encode in SVI Pro**
  - Context: Minor difference for single frame encode, not worth it for decode
  - *From: Kijai*

- **Consider changing anchor frame when scene changes completely**
  - Context: May help with degradation when moving far from initial reference
  - *From: Kijai*

- **Use lower latent strength for initial image**
  - Context: 0.5 strength works nicely for better results
  - *From: DawnII*

- **Use block wise attention selection for SVI Pro**
  - Context: Could use SDPA on first/last block only like with sage3 to avoid flashing
  - *From: Kijai*

- **Set different seeds for each clip in extension**
  - Context: For better variation in extended sequences
  - *From: avataraim*

- **Keep overlap at 5 frames for SVI Pro**
  - Context: Standard overlap is 4 frames from last latent + 1, don't change this value
  - *From: Kijai*

- **Use motion_latent_count of 2 for extensions**
  - Context: One for anchor latent (init image) and second for last latent of prior generation
  - *From: DawnII*

- **Use different alpha values for first frame vs rest**
  - Context: When using ultravico attention, first frame alpha 0.95, rest 0.8
  - *From: Kijai*

- **Reduce anchor latent strength for better prompt following**
  - Context: When SVI is too anchored to initial image and not following camera prompts
  - *From: Kijai*

- **Use multiple anchor samples instead of previous samples**
  - Context: For better scene transitions without degradation
  - *From: slmonker(5090D 32GB)*

- **Merge images in batches to avoid RAM issues**
  - Context: When interpolating long videos with many frames
  - *From: Cubey*

- **CFG around 20-30 steps works well without LightX**
  - Context: For Wan animate without speed LoRAs
  - *From: TK_999*

- **Use overlap 8-10 with motion_latent_count 2 for better results**
  - Context: When using SVI Pro for stable longer videos
  - *From: avataraim*

- **Save videos at 24fps or 30fps for better speed appearance**
  - Context: Post-processing generated videos
  - *From: JohnDopamine*

- **Use DDIM uniform scheduler for faster motion but requires more work for visual quality**
  - Context: When needing faster motion in videos
  - *From: Elvaxorn*

- **Use motion scale 1.3 as good middle ground, can push to 2.0 for very good motion**
  - Context: Using motion scale control node
  - *From: Elvaxorn*

- **Don't use prompt with MMAudio, works better without one**
  - Context: When generating audio for videos
  - *From: Benjimon*

- **Use 0.2-0.3 strength for augment empty frames**
  - Context: For motion enhancement without artifacts
  - *From: David Snow*

- **Use augment empty frames only on high noise for Wan 2.2**
  - Context: Allows low noise to fix artifacts
  - *From: Kijai*

- **Set pad_frame_value to 0.5 for VACE**
  - Context: When using empty frames padding
  - *From: Kijai*

- **Turn down lightx2v strength on high noise for better motion**
  - Context: Instead of using painter motion fixes
  - *From: ucren*

- **Use split tabs in Brave browser for copying nodes across workflows**
  - Context: Great for managing multiple ComfyUI instances
  - *From: David Snow*

- **Better models are harder to train because they have stronger ideas of what the world is**
  - Context: When training models with strong priors
  - *From: mallardgazellegoosewildcat2*

- **Do each segment manually instead of using looping workflow**
  - Context: For long video generation, as one bad gen will scuttle the entire sequence
  - *From: David Snow*

- **Run high noise separate from low noise**
  - Context: For better control over generation process
  - *From: DawnII*

- **Use 3 sampler method to get right speed, then use VACE to interpolate to 24fps**
  - Context: Alternative to dealing with slow motion look from LightX2V
  - *From: dj47*


## News & Updates

- **Wan 2.6 upgrade announced**
  - Benchmarking against Sora2, improves reference video generation, multi-camera storytelling, generation quality, and duration. Currently recruiting testers but unclear if open source
  - *From: Yan*

- **Speculation about Higgsfield acquiring Wan 2.5**
  - Claims of $100M acquisition, but community skeptical calling it fake news or worst deal in history if true
  - *From: Benjimon*

- **Black Forest Labs working on video model**
  - Temporally consistent Flux basically, likely to be released fully open source
  - *From: cyncratic*

- **DiT-Extrapolation (UltraViCo) code released**
  - GitHub repository released for the long video generation method
  - *From: JohnDopamine*

- **Long gen i2v implementation added to WanVideoWrapper**
  - New implementation added to the wrapper for longer video generation
  - *From: JohnDopamine*

- **Lotus-2 released by EnVision Research**
  - New model/tool released, not yet runnable in ComfyUI
  - *From: A.I.Warper*

- **ComfyUI Wan context options PR in progress**
  - Pull request working through ComfyUI approval process
  - *From: spacepxl*

- **Flux 2 uses Mistral encoder instead of CLIP**
  - Move away from CLIP encoders to more capable language models
  - *From: mallardgazellegoosewildcat2*

- **SVI 2.0 released for both Wan 2.1 and 2.2**
  - New version combines film and shot approaches, uses 5 frame continuation with reference padding
  - *From: Gleb Tretyak*

- **Steadydancer tutorial available**
  - Video tutorial for Steadydancer implementation
  - *From: David Snow*

- **LongCat-Image-Edit model released**
  - New image edit model on par with Seedream 4.0, smaller size, includes camera change editing
  - *From: DawnII*

- **Aquif-Image-14B released**
  - Image model finetuned from Wan2.2, claims to be SOTA image gen model for its size
  - *From: yi*

- **SVI 2.0 has different training for Wan 2.1 vs 2.2**
  - 2.1 can use 5 frames while 2.2 can just use one frame
  - *From: Kijai*

- **SVI 2.0 model released for Wan 2.2**
  - Updated Sequential Video Interpolation model available
  - *From: JohnDopamine*

- **Kijai pushed update to allow I2V start image in HuMo**
  - Was only allowed in the infinite talk loop before, now works for regular I2V and can work both start image + references at same time
  - *From: Kijai*

- **Context windows PR merged with bugfixes and freenoise**
  - Still need to figure better way to handle controls for cond retain and prompt travel, so those are commented out for now
  - *From: Kijai*

- **Kijai added easier way to do padding yesterday for SVI**
  - Nothing special, just workflow improvement
  - *From: Kijai*

- **OneToAllAnimation pose alignment node added**
  - Uses same detection as WanAnimate preprocessor, could be useful for other models too, doesn't do mad limb stretching
  - *From: Kijai*

- **OneToAll Animation model released**
  - New pose retargeting model with better alignment capabilities, fp16 and fp8 versions available
  - *From: Kijai*

- **aquif-ai fraudulent model removed**
  - HuggingFace account deleted after being caught uploading stolen Magic Wan model
  - *From: Nathan Shipley*

- **SCAIL project discovered**
  - From original CogVideo team, handles multiple people and rotation well, but model was pulled
  - *From: Kijai*

- **LTX2 postponed to January 2025**
  - Previously expected in 2025, now specifically January
  - *From: NebSH*

- **New models released end of year**
  - Wan-Move-14B-480P and Live-Avatar models released, possibly due to end of year deadlines
  - *From: DawnII*

- **Live Avatar supports real-time streaming**
  - 20 FPS on 5×H800 GPUs with 4-step sampling, infinite-length interactive avatar video generation
  - *From: David Snow*

- **New rCM LoRA released for Wan 2.2 I2V high noise**
  - Wan22-I2V-A14B-HIGH-rCM6_0_lora_rank_64_bf16 available
  - *From: 42hub*

- **rCM low noise LoRA now available**
  - Wan22-I2V-A14B-LOW-rCM1_0_lora_rank_64_bf16.safetensors released after multiple requests
  - *From: Kijai*

- **WanMove native ComfyUI implementation released**
  - Native node for WanMove added, compatible with ATI workflows
  - *From: Kijai*

- **OneToAll merged into main WanVideoWrapper branch**
  - OneToAll animation feature now in main branch, no longer separate
  - *From: Karthik*

- **New image model based on Wan 2.2 released**
  - Reddit post about new image generation model using Wan 2.2 as base
  - *From: Dream Making*

- **Wan 2.6 announcement expected at offline event on 10th**
  - Event shows 'try all new wan face to face', possible Wan 2.6 release
  - *From: yi*

- **WanMove native support added with new Tracks data type**
  - Native ComfyUI implementation using custom Tracks type for better integration
  - *From: Kijai*

- **RAM pressure cache feature coming to ComfyUI**
  - Feature will unload models from RAM if needed, should solve RAM issues
  - *From: Kijai*

- **ComfyUI 2.9.1 update fixed crashing issues with VRGDG workflow**
  - Sorted problems users were having
  - *From: burgstall*

- **New Tracks node input type PR submitted to core ComfyUI**
  - Should make custom nodes simpler, no need for JSON string stuff
  - *From: Kijai*

- **SpatialTracker V2 released**
  - Major improvement over V1
  - *From: Kijai*

- **SCAIL model implementation in progress**
  - New pose-driven video model with 3D+2D pose control, available in SCAIL branch of wrapper
  - *From: Kijai*

- **OneToAll 1.3B v2 model available**
  - Updated version shows improved performance over original
  - *From: Kijai*

- **SCAIL preview release available**
  - SCAIL (Wan 2.1 14B) preview version available but has no long video generation - full version will have it. Research only license for NLF model component
  - *From: Kijai*

- **V2 nodes in development**
  - New V2 node architecture being developed with modular design - separate components for text_embeds, image_embeds, scheduler, extra_args
  - *From: Kijai*

- **Auto spacing feature added**
  - Auto spacing feature added to address keyframe spacing issues
  - *From: Flipping Sigmas*

- **fp8_e4m3fn_scaled version of SCAIL uploaded**
  - New fp8_e4m3fn_scaled version of Wan21-14B-SCAIL uploaded to HuggingFace
  - *From: Kijai*

- **Alibaba announcing WAN model launch event**
  - https://www.alibabacloud.com/en/events/wan-model-launch
  - *From: seruva19*

- **WanMove now available in native ComfyUI**
  - No longer requires wrapper-only usage
  - *From: Kijai*

- **SCAIL-Pose node package released**
  - 3D pose detection for SCAIL with single and multi-person support
  - *From: Kijai*

- **TurboWan 2.2 I2V 14B model released on HuggingFace**
  - Includes activation quantization and sparse attention optimizations
  - *From: JohnDopamine*

- **Wan 2.6 launch event scheduled for January 17th**
  - Appears to be closed source release based on Alibaba Cloud event
  - *From: TK_999*

- **SCAIL official version coming in later months**
  - Will have native long video support, higher-res, possibly facial injection methods
  - *From: teal024*

- **RAM prices have tripled recently**
  - 128GB RAM kit tripled in value over a few months, making open source harder
  - *From: blake37*

- **Wan 2.6 announced by Alibaba Cloud**
  - New cloud-only model, not available locally. 50B parameters mentioned
  - *From: ZeusZeus (RTX 4090)*

- **SCAIL merged to main branch**
  - SCAIL pose control functionality now available in main branch of WanVideoWrapper
  - *From: Kijai*

- **Hand coordinate swap fixed in SCAIL**
  - Left and right hand coordinates were corrected, significantly improving hand control
  - *From: Kijai*

- **Dependencies cleaned up for SCAIL**
  - Dependencies reduced to just taichi and opencv-python, removing essentials requirement
  - *From: Kijai*

- **Wan 2.6 released but not open source**
  - Changed from 24fps to 30fps, 1080p looks upscaled and filtered
  - *From: Ruairi Robinson*

- **TurboDiffusion released Turbo models for Wan**
  - TurboWan2.2-I2V-A14B-720P and TurboWan2.1-T2V-14B-720P available on HuggingFace, claims 720P 5 secs in 35 secs on 5090
  - *From: Ada*

- **T3-Video models released**
  - 1.3B and 5B wan models finetuned on 4k dataset with 10x faster 4k inference
  - *From: yi*

- **Wan2.2-Turbo appeared on HuggingFace**
  - Suspicious release possibly related to removed aquif-ai accounts, released same day as Turbo diffusion model
  - *From: hicho*

- **Wan 2.6 released but not open source**
  - 15s consistency, multi-shot control, character ID replication, commercial pricing model
  - *From: Léon*

- **CogVideo devs released new video VAE**
  - Recently released as potential improvement
  - *From: yi*

- **Seedance 1.5 launched**
  - New model with paper available
  - *From: yi*

- **LongCat-Video-Avatar released**
  - New video avatar model with GitHub implementation
  - *From: yi*

- **Wan 2.2 turbo models available**
  - New faster inference variants of 2.2
  - *From: Zabo*

- **SCAIL dwpose compatibility added**
  - New node created to convert dwpose output to be compatible with SCAIL
  - *From: Kijai*

- **SCAIL prompt generation snippets released**
  - Google Gemini snippets for reading reference image and driving motion to generate detailed prompts available in gen_prompts_gemini.py
  - *From: teal024*

- **T3-Video released by UltraWan team**
  - New model from APRIL-AIGC/T3-Video on HuggingFace
  - *From: hicho*

- **New T2V distill LoRAs released**
  - Available at huggingface.co/lightx2v/Wan2.2-Distill-Loras/tree/main
  - *From: yi*

- **Alibaba Wan team went closed source**
  - Live stream showing new closed-source model, community feedback negative due to quality drop vs open 2.2
  - *From: Ruairi Robinson*

- **Uni3c optimization update**
  - Added option to disable offloading for faster performance, can run in fp8 with quantization
  - *From: Kijai*

- **DF11 models now support Wan**
  - 30% VRAM reduction models available for Wan 2.2 I2V and T2V at DFloat11 HuggingFace
  - *From: Ada*

- **SCAIL team planning to merge SCAIL_Pose into main repo**
  - Will provide implementation based on Wan Official Framework instead of SAT, add training scripts for community
  - *From: teal024*

- **New LightX2V T2V LoRAs released on 12/17**
  - Available on HuggingFace lightx2v/Wan2.2-Distill-Loras
  - *From: aipmaster*

- **New LongCat Video Avatar model released**
  - From same team, different from Wan but similar architecture. Not very usable without distill LoRA (30 mins for 5 secs). 16fps with audio stride issues
  - *From: Kijai*

- **Comfy-org now paying Kijai for open source contributions**
  - Official sponsorship for ComfyUI development work
  - *From: Kijai*

- **Wan Alpha v2.0 released**
  - New version available on GitHub
  - *From: Hashu*

- **Hand scaling fix and DWPose bug fix pushed**
  - Fixed hand scaling from upstream and bug when using DWPose instead of VitPose (hands no longer swapped)
  - *From: Kijai*

- **ComfyUI Manager integrated, preview options moved**
  - Manager now integrated into ComfyUI, preview options relocated to main ComfyUI settings
  - *From: TK_999*

- **LongCat team working on 24fps version**
  - Current 16fps setup has lipsync issues, team is developing 24fps version to address this
  - *From: Kijai*

- **LongCat team working on new distill LoRA**
  - Team is training a distill LoRA specifically for LongCat Avatar model, said to be coming 'soon' and tested at 16 steps
  - *From: slmonker(5090D 32GB)*

- **SCAIL now available on main branch**
  - SCAIL has been moved from branch to main branch and available for few days
  - *From: Kijai*

- **LongCat Avatar branch updated with ref_latent bug fix**
  - Major bug fix where ref_latent wasn't being used properly, causing identity degradation
  - *From: Kijai*

- **Stand-In LoRA weights released for Wan 2.2**
  - New Stand-In LoRA available as .safetensors format, works without code changes
  - *From: Kijai*

- **Loop decode node added to native ComfyUI**
  - New node for creating looping videos with native context windows
  - *From: Kijai*

- **LongCat-Avatar fp8 quantized model released**
  - Mixed precision fp8_e4m3fn scaled model available, nodes need update to use it
  - *From: Kijai*

- **Stand-In preprocessing officially released**
  - Official Stand-In preprocessing available for better results
  - *From: Vérole*

- **LongVie2 model available**
  - Control part is interesting, continuation doesn't seem great, but control might be usable with other workflows
  - *From: Kijai*

- **HuMo dataset released**
  - HuMoSet dataset containing 670K video samples with diverse reference images, dense video captions, and strict audio-visual synchronization. 133GB download, already 700+ downloads
  - *From: JohnDopamine*

- **NVFP4 model for Blackwell cards**
  - Wan-NVFP4 released on HuggingFace with support for Blackwell cards using NVFP4 kernel
  - *From: yi*

- **StoryMem model released**
  - New model for memory-to-video generation with MI2V and MM2V capabilities for connecting adjacent shots
  - *From: Karthik*

- **WanVideoWrapper version 1.4.5 released**
  - Updated version with fixes for mixed model support and improved compatibility
  - *From: Kijai*

- **LongCat team working on 24fps version**
  - They are working on 24fps version because the current 32/16 fps has some lipsync issues
  - *From: Kijai*

- **Wan 2.6 available as API**
  - New version released but only accessible through API, not open source
  - *From: Ryzen*

- **Wan-Alpha v2.0 released**
  - Based on Wan2.1-14B-T2V with adapted weights and inference code open-sourced
  - *From: Gleb Tretyak*

- **EgoX 2.1 I2V LoRA released**
  - Available on HuggingFace from DAVIAN-Robotics
  - *From: DawnII*

- **OmniVCus model getting release**
  - Model uploading to HuggingFace with recent GitHub updates
  - *From: JohnDopamine*

- **WanVideoWrapper bug fixes**
  - Fixed issues with cfg zero star and ComfyUI compatibility
  - *From: Kijai*

- **SVI 2.0 Pro released**
  - New version with improved workflow compatibility and better handling of conditioning channels
  - *From: DawnII*

- **Open-OmniVCus code is up**
  - Code released but repo is messy as it contains all of diffsynth
  - *From: JohnDopamine*

- **Distilled version of Wan might be possible**
  - Rumors that Wan team might release a distilled version due to pressure, though just rumors
  - *From: slmonker*

- **Kijai waiting for new distill LoRA before touching Turbodiffusion again**
  - Development pause on Turbodiffusion implementation
  - *From: Kijai*

- **Wan NVFP4 28x boost released but needs custom kernels**
  - Requires building cutlass and custom implementation, not just pytorch
  - *From: Kijai*

- **SVI Pro available with significant code changes**
  - Might work with old implementation but has many modifications
  - *From: Benjimon*

- **Wan going to paid API**
  - Wan video generation moving to paid API model
  - *From: Lumifel*

- **New SVI 2.0 Pro model released**
  - Available on HuggingFace, works as LoRA with improved extension capabilities
  - *From: Kijai*

- **New distill LoRAs released 11 days ago**
  - Better quality than Lightning LoRAs, recommended for current use
  - *From: Kijai*

- **Native SVI Pro node added to KJNodes**
  - New WanImageToVideoSVIPro node available with converted LoRAs
  - *From: Kijai*

- **SVI Pro LoRAs converted and available**
  - Converted LoRAs available at huggingface.co/Kijai/WanVideo_comfy/tree/main/LoRAs/Stable-Video-Infinity/v2.0
  - *From: Kijai*

- **Ultravico implementation for Wan 2.2 available**
  - Custom implementation working with parameters: 0.95 alpha, 0.3 beta, 4 gamma
  - *From: Benjimon*

- **FreeLong++ implementation for MultiTalk and VACE**
  - Algorithm that does up to 640 frames in one batch, compatible with VACE/T2V/MultiTalk+VACE
  - *From: campeonchik*

- **Smooth Mix model available**
  - Fusion model with higher motion dynamics available on Civitai for Wan 2.2
  - *From: slmonker(5090D 32GB)*

- **Added ultravico support to SVI workflows**
  - Kijai added ultravico (modified attention) functionality
  - *From: Kijai*

- **Wan Alpha 2.0 DoRA conversion completed**
  - Successfully converted Wan Alpha 2.0 LoRA to DoRA format for ComfyUI
  - *From: Kijai*

- **Tencent released HY-Motion 1.0**
  - New motion model that could be useful for animation production as first pass before Wan
  - *From: NebSH*

- **Kijai added step-specific ultravico control**
  - Can now set ultravico for specific steps, with first step being most important
  - *From: Kijai*

- **New motion scale control node released**
  - Custom node that gives ability to control scale of motion, works with VACE
  - *From: brbbbq*

- **HuMo I2V PR being considered for native ComfyUI**
  - Kosinkadink asking for examples and test workflows to expedite review
  - *From: Kosinkadink*

- **PyTorch 2.6 made weights_only=True the default**
  - Security improvement to prevent RCE vulnerabilities from malicious model files
  - *From: Kijai*


## Workflows & Use Cases

- **Fun VACE v2v with reference image**
  - Use case: Video stylization with 0.6-0.8 denoise using reference images
  - *From: David Snow*

- **Using Lynx with I2V for basic v2v guiding**
  - Use case: Follows basic motion but with more flexibility than VACE depth
  - *From: hablaba*

- **3-chained KSampler setup for I2V quality**
  - Use case: K1 -> High noise, step 0-2 no lora, K2 -> High noise + Lightx2v lora, step 2-8, K3 -> low noise, Lightx2v lora step 8-14 for 81 frames at 1920x800
  - *From: harryB*

- **Crop&stitch for masked subject animation**
  - Use case: Select masked area and feed cropped area to Wan with reference image for subject insertion
  - *From: Valle*

- **Context windows with overlapping for long video generation**
  - Use case: Standard_static context: first window 1-81 frames, second window 65-156, third window 140-221 with proper overlap handling
  - *From: Ablejones*

- **Output clean latent, upscale, then add noise again**
  - Use case: Upscaling latents between LN and HN phases by outputting clean, upscaling clean, then adding noise in low noise ksampler
  - *From: spacepxl*

- **Three-sampler approach: priming + high + low**
  - Use case: Prime with undistilled 1-2 steps, then use high noise model, finish with low noise model
  - *From: Scruffy*

- **Split schedule with euler/gradient estimation sampler**
  - Use case: Helped converge details better than unipc, but gradient estimation had issues with high noise steps
  - *From: spacepxl*

- **SVI 2.0 extension workflow**
  - Use case: Extending videos by using 5 frames for continuation with original reference padding
  - *From: Kijai*

- **VACE long generation with 6 shots**
  - Use case: 25 second total generation using open pose, depth, and driving video for color with mitigated flashes and color shift
  - *From: Juan Gea*

- **4-pass I2V generation with mid-step image upscale**
  - Use case: Outputting 2K resolution videos with better quality than latent upscale
  - *From: FL13*

- **SVI-Shot video extension**
  - Use case: Maintaining scene continuity by applying reference image into i2v frames, can switch scenes by changing reference frame
  - *From: Ablejones*

- **One-to-all pose control with text2vid**
  - Use case: Pose control using just text prompts without additional inputs
  - *From: Kijai*

- **FFLF with VACE for perfect image looping**
  - Use case: Creating seamless loops, works up to about 200 frames but degrades after 3-4 generations
  - *From: Juan Gea*

- **SVI 2.0 workflow adaptation**
  - Use case: Sequential video interpolation for long video generation
  - *From: Hashu*

- **HuMo extension with context windows**
  - Use case: Better handling of color shift issues compared to pure overlap extensions
  - *From: Ablejones*

- **Using few extra overlap frames with SVI**
  - Use case: Better results than 1 frame overlap, 3 frames seems optimal
  - *From: Ablejones*

- **VACE for video extensions**
  - Use case: Tried and tested method for extensions, has faith it should get good results
  - *From: 42hub*

- **SVI Wan 2.2 workflow**
  - Use case: Stable Video Infinity using first and last frame for I2V generation
  - *From: Ablejones*

- **OneToAll Animation with WanAnimate**
  - Use case: Combining OneToAll preprocessing with WanAnimate for better pose control
  - *From: slmonker(5090D 32GB)*

- **OneToAll workflow available**
  - Use case: Video generation and extension
  - *From: Josiah*

- **Main WanAnimate setup with optimization**
  - Use case: Optimized since WanAnimate dropped, getting incredible results
  - *From: Josiah*

- **Two-step TTS to video generation**
  - Use case: Text to speech video when single-step not available - use TTS Audio Suite then feed to InfiniteTalk/HuMo
  - *From: Gleb Tretyak*

- **VACE for video interpolation smoothing**
  - Use case: Smooth out jumps in first-frame-last-frame videos using masking
  - *From: DawnII*

- **TTM (Time-to-Move) with vid2vid**
  - Use case: Masked noise injection for controlled video generation, steps get skipped in vid2vid
  - *From: Kijai*

- **HuMo + SVI 2.2 combination with overlap blending**
  - Use case: Smooth lip sync video generation with transition smoothing
  - *From: Cseti*

- **Wan 2.2 FMML high noise + HuMo low noise**
  - Use case: Automated lip sync video generation
  - *From: VRGameDevGirl84(RTX 5090)*

- **SVI with reference images for character consistency**
  - Use case: Long video generation with stable character appearance
  - *From: Gateway {Dreaming Computers}*

- **Wan 2.2 high noise + HuMo low for lip sync with FMML for I2V**
  - Use case: Infinite length generation with lip sync
  - *From: VRGameDevGirl84(RTX 5090)*

- **SVI with HuMo using SVI 2.0 lora for Wan2.1 instead of 2.2**
  - Use case: Better long video generation with less artifacts
  - *From: Ablejones*

- **Native ComfyUI implementation for SVI + HuMo**
  - Use case: More control over sampling and embedding combination
  - *From: Ablejones*

- **Audio reactive video with HuMo and high pass filter**
  - Use case: Creating audio-responsive video content
  - *From: VRGameDevGirl84(RTX 5090)*

- **Using latent mask with MultiTalk for character-specific LoRAs**
  - Use case: Applying different effects to specific characters in lip-sync videos
  - *From: boorayjenkins*

- **Multikeyframe qwen edit with VACE**
  - *From: Flipping Sigmas*

- **SCAIL pose-driven animation**
  - *From: Kijai*

- **Context windows for longer videos**
  - *From: Kijai*

- **Uni3c + SCAIL for background consistency**
  - Use case: Preventing frozen backgrounds in longer videos over 81 frames
  - *From: slmonker(5090D 32GB)*

- **WanMove with spline paths across context windows**
  - Use case: Creating continuous camera movement in videos longer than 81 frames
  - *From: zelgo_*

- **3D pose-driven SCAIL animation**
  - Use case: Creating character animations with proper pose control and face tracking
  - *From: Kijai*

- **Multi-person SCAIL pose detection**
  - Use case: Generating videos with two characters interacting using pose control
  - *From: slmonker(5090D 32GB)*

- **Chaining multiple LoRA nodes vs single multi-LoRA node**
  - Use case: Both methods work identically for loading multiple LoRAs
  - *From: Kijai*

- **SCAIL pose control workflow**
  - Use case: Character animation with 3D pose control using NLF and optional face/hand control
  - *From: Kijai*

- **Upscale then v2v with low noise**
  - Use case: Enhanced quality workflow using Wan 2.2 i2v low noise fp16 with LightX2V LoRA
  - *From: FL13*

- **Context window extension for long videos**
  - Use case: Creating videos longer than 5 seconds using context window morphing
  - *From: Kijai*

- **SCAIL pose transfer**
  - Use case: Transfer pose from video to reference image while maintaining better ID retention
  - *From: David Snow*

- **2.2 low model as refiner for 2.1 VACE**
  - Use case: Use 1-2 steps of 2.2 low model to clean up 2.1 VACE outputs
  - *From: spacepxl*

- **Mixed CFG scheduling**
  - Use case: 1-2 steps with no distill loras and real CFG, then distill and cfg=1 for rest
  - *From: spacepxl*

- **Chain SCAIL generations with SVI lora**
  - Use case: Creating longer videos with smoother transitions
  - *From: Kijai*

- **Two-pass SCAIL processing**
  - Use case: First continue from last frame, then vid2vid context windows for smoothing
  - *From: Kijai*

- **SCAIL with context windows**
  - Use case: Longer generations with 48-64 frame overlap
  - *From: slmonker(5090D 32GB)*

- **Multi-person SCAIL with segmentation**
  - Use case: Handling multiple people in pose-driven animation
  - *From: Kijai*

- **Using SCAIL generation as pose input for WanAnimate**
  - Use case: Better retargeting for very different character sizes while avoiding background shifts
  - *From: Juan Gea*

- **VACE outpainting after SCAIL generation**
  - Use case: Add new background after SCAIL generation to fix background issues
  - *From: 42hub*

- **SCAIL + WanAnimate + Uni3c combination**
  - Use case: Professional character replacement with stable background and perfect retarget
  - *From: Juan Gea*

- **Multi-person dance with updated SCAIL-pose**
  - Use case: Using dwpose and convert openpose keypoints to DWpose node for multiple people
  - *From: slmonker(5090D 32GB)*

- **Perfect loop generation with same start/end image**
  - Use case: Using same image for start and end frame with fl2v mode enabled for seamless loops
  - *From: Danial*

- **Two-step SCAIL + WanAnimate process**
  - Use case: Use SCAIL for character retargeting, then WanAnimate for stable long generation with same reference frame
  - *From: Juan Gea*

- **Split 1.3B tile + 2.2 low noise upscale**
  - Use case: Clean upscaling results with early changeover point
  - *From: spacepxl*

- **Splice seams method for long videos**
  - Use case: Take last 16 frames of one video and first 16 of another, run inbetween frames to create seamless transitions
  - *From: NodeMancer*

- **Multi-model combination for character animation**
  - Use case: Combining Wan 2.2 I2V, WanMove, UniAnimate and InfiniteTalk Multi for character consistency
  - *From: Gleb Tretyak*

- **Two-pass character animation**
  - Use case: First pass animates main character, second pass drives idle secondary character for multi-character scenes
  - *From: boorayjenkins*

- **Z-image controlnet with T2V**
  - Use case: Using start image with z-image controlnet for T2V generation
  - *From: Kijai*

- **Per-window reference images for context windows**
  - Use case: Inject different reference images for each context window using WanVideo Encode Latent Batch → reference_latent input
  - *From: chrisd0073*

- **TTM with cut and drag for primitive animation**
  - Use case: Move primitive image via cut and drag, can be masked to work with finalized first frame background
  - *From: Gleb Tretyak*

- **VACE with wireframes or point blobs**
  - Use case: Control motion with primitive shapes, can cut off early and do half steps with control signal then half with solid gray inpaint
  - *From: spacepxl*

- **LongCat Avatar multi-angle generation**
  - Use case: Creating videos with multiple camera angles by passing different images as encoded latents to ref and prev latents
  - *From: burgstall*

- **LongCat Avatar V2V with masking**
  - Use case: Video-to-video generation with ability to mask specific parts to affect, using video slice node for correct input video parts
  - *From: Kijai*

- **VACE inpainting with multiple ideal frames**
  - Use case: Input start frame + end frame + middle frames (like 44th, 69th) with masks for better inpainting results
  - *From: Dannhauer80*

- **Face-only MultiTalk refinement**
  - Use case: Apply MultiTalk only to face using SAM masking, then refine with WAN 2.2
  - *From: boorayjenkins*

- **Frame windowing for long generation**
  - Use case: Use 141 frame windows instead of 301 frames for better time efficiency
  - *From: burgstall*

- **Vocal extraction workflow for lip sync**
  - Use case: Improving lip sync quality by using clean vocal tracks
  - *From: Kijai*

- **WanMove with depth control**
  - Use case: Creating consistent camera movements with depth control at 0.8 strength
  - *From: Kijai*

- **VACE with keyframing**
  - Use case: Multiple first to last frame samplers in serial for long video generation
  - *From: DawnII*

- **3D camera control rendering**
  - Use case: Recording camera moves and outputting as images for video generation
  - *From: Kijai*

- **SCAIL + Qwen Image Edit combination**
  - Use case: First use Qwen to get character proportions similar to reference video, then apply SCAIL for motion transfer
  - *From: souoNeo*

- **Multi-step video workflow with caching**
  - Use case: Cache latents to disk between steps to avoid re-running expensive sampling when experimenting with decode settings
  - *From: boorayjenkins*

- **Multiple images with context windows in I2V**
  - Use case: Generate different video segments using multiple reference images and pipe-separated prompts
  - *From: Kijai*

- **SVI 2.0 Pro with lightx2v**
  - Use case: Extended video generation with speed optimization
  - *From: Benjimon*

- **Using batch encode for multiple reference images**
  - Use case: Windowed context with multiple reference images and prompts
  - *From: avataraim*

- **SCAIL with DWPose disconnected**
  - Use case: When you want input image to adapt to original video rather than video adapting to image
  - *From: DawnII*

- **InfiniteTalk v2v for lip sync**
  - Use case: Lip syncing existing video with custom audio using partial denoise
  - *From: 42hub*

- **Three pass workflow with Z Image model**
  - Use case: High quality image generation with refiner
  - *From: David Snow*

- **Using SaveLatent and LoadLatent nodes for chaining video generations**
  - Use case: Save state between video generations to avoid regenerating from start
  - *From: 42hub*

- **SVI 2.0 Pro extension workflow**
  - Use case: Creating seamless video extensions without decode-encode steps
  - *From: Kijai*

- **Save/load latents for memory efficiency**
  - Use case: Avoid model offloading and reloading when result not needed instantly
  - *From: Kijai*

- **SVI Pro + StoryMem combination**
  - Use case: Maintaining character consistency across multiple clips
  - *From: avataraim*

- **SVI Pro extension workflow**
  - Use case: Extending videos by copying extension groups and connecting prev_samples and decoded results
  - *From: Kijai*

- **Full auto infinite SVI Pro workflow**
  - Use case: Automated infinite video generation with multiple loops, achieved 52 second generation
  - *From: Vérole*

- **Character sheet with SVI Pro**
  - Use case: Using character reference sheets with SVI Pro's continuation preference
  - *From: DawnII*

- **T2V + I2V combined workflow**
  - Use case: Generate first video with T2V then continue with I2V, but requires grabbing first frame as input
  - *From: avataraim*

- **SVI Pro with multiple anchor samples workflow**
  - Use case: Creating consistent scene transitions without using previous samples
  - *From: slmonker(5090D 32GB)*

- **SVI loop workflow with prompt splitting**
  - Use case: Automated multiple SVI passes with different prompts per loop
  - *From: Quality_Control*

- **VACE with multiple clip stitching**
  - Use case: Creating longer videos by combining several shorter clips
  - *From: ingi // SYSTMS*

- **SVI Pro with HuMo integration**
  - Use case: Audio-reactive video generation, though produces flash artifacts
  - *From: Ablejones*

- **First-Last frame workflow for cinematic results**
  - Use case: Creating slower, more fluid, cinematic videos instead of fast-moving sequences
  - *From: VRGameDevGirl84(RTX 5090)*

- **Automated long video generation with LLM integration**
  - Use case: Creating long videos with automated prompting and audio length-based segmentation
  - *From: VRGameDevGirl84(RTX 5090)*

- **SVI Pro with anchor image changes**
  - Use case: Changing scenes or subjects mid-generation by using different anchor images
  - *From: NebSH*

- **SVI 2.0 Pro with color matching**
  - Use case: Long video generation with color drift correction
  - *From: BNP4535353*

- **Using different LoRAs for each SVI chunk**
  - Use case: Character LoRA for entire run, motion LoRA only on specific chunks
  - *From: Dever*

- **SVI 2.0 Pro for infinite length sequences**
  - Use case: Avoiding slow motion issues with LightX2V by rendering longer sequences and speeding up in post
  - *From: dj47*

- **VACE character replacement workflow with Phantom and Context Windows**
  - Use case: Advanced video editing combining multiple techniques for character replacement in existing videos
  - *From: 42hub*


## Recommended Settings

- **Fun VACE frame load cap**: 162 frames
  - Set as 81x2 for the dual model architecture
  - *From: David Snow*

- **SteadyDancer workflow FPS**: 16 fps input, 24 fps output
  - Standard configuration in workflow
  - *From: Gateway {Dreaming Computers}*

- **VACE pose/depth control for variations**: Pose 0.4-0.7, Depth 0.1-0.4, Shift 8+
  - For getting creative variations with large mask
  - *From: Dannhauer80*

- **UltraViCo block size**: 64 instead of 128
  - Block size 128 isn't supported on 4090 hardware level, reduced to 64 to make it run
  - *From: Kijai*

- **Context stride**: 1 (mostly not used)
  - Higher values cause terrible stutter, only used on early steps in 2.2 A14B workflows
  - *From: Kijai*

- **Fun Control default frames**: 162 instead of 81
  - For 10 second videos
  - *From: David Snow*

- **VACE FP16**: Standard setting
  - Working configuration for VACE workflows
  - *From: NodeMancer*

- **SDE eta**: 0.5 or greater
  - Works fine even with low steps if properly implemented
  - *From: Ablejones*

- **Euler steps for quality**: 10,000 steps
  - Euler becomes good again with enough steps
  - *From: mallardgazellegoosewildcat2*

- **Context stride**: 1
  - Higher values like 4 can cause fatal errors and crashes
  - *From: Kijai*

- **SVI 2.0 motion frames**: 5
  - Works properly, higher values create jumpy overlaps
  - *From: xiver2114*

- **Block size for UltraViCo**: Modified from default 128
  - Default 128 not supported on 4090 hardware level
  - *From: Kijai*

- **Frame limit for stable generation**: 81 frames
  - Models trained on 81 frames, going over causes looping behavior
  - *From: Juan Gea*

- **return_with_leftover_noise**: disabled
  - To get denoised latent in native nodes
  - *From: Ablejones*

- **CFG for different scenarios**: 3.5/1/1 vs 3.5/3.5/3.5
  - Higher CFG 30% slower but better prompt following
  - *From: N0NSens*

- **SVI overlap frames**: 3-4 frames
  - Minimal flashing while maintaining reference
  - *From: Ablejones*

- **Context windows for long generation**: context_length 81, context_overlap 30
  - For looped generation, though results vary
  - *From: Benjimon*

- **SVI overlap frames**: 3 frames
  - Highest number without artifacts, better than 1 frame
  - *From: Ablejones*

- **High noise LoRA strength**: 0.5
  - Gets more motion and prompt following
  - *From: Hashu*

- **InfiniteTalk steps**: 2 steps
  - Low steps to modify only mouth without affecting rest of video
  - *From: Stef*

- **HuMo resolution for 16GB VRAM**: 1024x576
  - 1280x720 causes OOM
  - *From: AmirKerr*

- **OneToAll Animation default resolution**: 576x1024
  - Default resolution used by the model
  - *From: Kijai*

- **OneToAll Animation scheduler**: shift 7 with euler
  - Recommended settings, though doesn't matter much with LightX2V
  - *From: Kijai*

- **OneToAll Animation steps**: 30 steps with cfg 2.0
  - Good results without LightX2V, 50 steps didn't improve much
  - *From: Kijai*

- **OneToAll default resolution**: 576x1024
  - Default resolution for proper results
  - *From: Kijai*

- **CFG comparison settings**: cfg 1.2 8 steps lightx2v vs cfg 1.2 25 steps euler
  - Better init adherence with euler but looks scuffed
  - *From: 企鵝（50% CASH 50%GOLD）*

- **Max frame window size for WanAnimate**: 1000
  - Maximum setting for frame_window_size in WanVideo Animate Embeds
  - *From: Valle*

- **LightX2V I2V LoRA strength**: 3.0 on low noise
  - Standard setting for I2V with lightx2v distillation
  - *From: patientx*

- **SVI LoRA strength on high noise**: 0.5-0.75
  - Balance between SVI effect and prompt adherence
  - *From: Hashu*

- **Audio CFG for InfiniteTalk**: 1.4-1.5
  - Better lip sync quality
  - *From: Charlie*

- **TTM steps**: 3 steps with vid2vid
  - Vid2vid skips steps, actual generation uses 2 steps
  - *From: Kijai*

- **SVI 2.2 noise split point**: 0.85 for T2V, 0.9 for I2V
  - Original defaults for proper model switching
  - *From: Kijai*

- **SVI 2.2 frame overlap**: 1 frame overlap with 5 frames provided
  - Designed setup for SVI 2.2 vs SVI shot
  - *From: Ablejones*

- **Black levels for image embed nodes**: 0 instead of 0.17
  - User found 0.17 seemed wrong for some nodes
  - *From: Vardogr*

- **1030 lora strength**: 1.0
  - Proper strength for Wan2.2
  - *From: WorldX*

- **480p lora on high**: 3.0
  - Works well but results can be blurry at other strengths
  - *From: metaphysician*

- **SVI loras for Wan2.2**: Both high and low set to 1
  - Recommended setting
  - *From: BarleyFarmer*

- **Old 2.1 lightx2v lora**: 3.0 strength with cfg
  - Never found anything better
  - *From: Kijai*

- **Frame limit for generation**: 125 frames maximum
  - Anything over 125 frames gets weird, quality ok up to 200 but effects undesirable
  - *From: Chandler ✨ 🎈*

- **VACE sigma boundary**: 0.875
  - VACE is T2V model, not I2V
  - *From: pookyjuice*

- **Reserve VRAM argument**: 1GB
  - Prevents getting stuck at VRAM limit
  - *From: Kijai*

- **SCAIL default resolution**: 895x512
  - Default resolution for SCAIL model
  - *From: Kijai*

- **Pose downsampling**: half size
  - Default pose downsampling to half size as full pose is heavy
  - *From: Kijai*

- **Skyreel LoRA strength with T2V 2.2**: higher than 1.0
  - Recommended strength for extending frames to 121
  - *From: Kijai*

- **SCAIL context windows with block swap**: 20 blocks swapped
  - Example setting for 4090 - very slow but works
  - *From: Kijai*

- **WanMove memory usage**: Same as Wan 2.1 14B I2V
  - For VRAM planning
  - *From: Kijai*

- **SCAIL pose resolution**: Half of main input resolution
  - Model training requirement
  - *From: Kijai*

- **Uni3c frame requirement with SCAIL**: Add 4 more frames
  - SCAIL ref takes one latent
  - *From: Kijai*

- **LoRA extraction type**: standard
  - Better than 'full' which is actually full model
  - *From: Kijai*

- **SCAIL resolution**: 512x896
  - Optimal results, must be divisible by 32
  - *From: teal024*

- **Image resize method for SCAIL**: crop instead of pad
  - Reduces hand drifting issues
  - *From: Kijai*

- **VITPose model**: VITPose-H instead of L
  - Better accuracy for pose detection
  - *From: Kijai*

- **Pose control strength**: 0.25 (ending control at 0.25)
  - Uses control for only 2 out of 6 steps, provides effective control without overdoing it
  - *From: Kijai*

- **Sampling steps for fast motion**: 6 steps instead of 4
  - Fast motion doesn't look good with just 4 steps, leaves noise on moving parts
  - *From: Kijai*

- **Resolution requirements**: Width and height divisible by 32
  - Required for proper tensor dimensions and rope calculations
  - *From: Gleb Tretyak*

- **Block swap for SCAIL**: 20/40 blocks swapped with fp8_scaled
  - SCAIL requires more VRAM than normal, block swap helps manage memory
  - *From: Kijai*

- **SageAttention version**: 2.2.0
  - Balance between quality and speed, SageAttention 3 considered drop in quality
  - *From: FL13*

- **LightX2V LoRA configuration**: wan 2.2 latest lightx2v 1030/1022 LoRa on high model + wan 2.1 old lightx2v for low model
  - Recommended setup for best results
  - *From: FL13*

- **CFG schedule**: 2 on first step, cfg 1 for rest
  - Better motion with distill LoRAs
  - *From: FL13*

- **Base precision**: fp16
  - Highest quality you can get
  - *From: FL13*

- **SageAttention installation**: pip install sageattention==2.2.0 --no-build-isolation
  - Proper installation method
  - *From: FL13*

- **SCAIL context window overlap**: 64 frames
  - Better than 48 but still shows gaps
  - *From: slmonker(5090D 32GB)*

- **Default SCAIL framerate**: 16fps
  - Default output framerate
  - *From: Gateway {Dreaming Computers}*

- **CFG vs steps trade-off**: 4 steps with cfg 1.0 = 4 passes vs 50 steps with cfg = 100 passes
  - Massive speed difference
  - *From: Kijai*

- **SCAIL frame skipping**: Choose 'all frames' for higher fps
  - Model can do sparse frames by default, disable skipping for full fps matching input
  - *From: Kijai*

- **Resolution for Wan models**: Must be divisible by 32
  - Prevents shape errors in WanVideoSamplerv2
  - *From: Gleb Tretyak*

- **Wan frame count**: 4*n+1 frames
  - Prevents frame loss in VACE processing
  - *From: 42hub*

- **SCAIL pose resolution**: Half of output resolution
  - Required for proper SCAIL function, use math nodes to halve
  - *From: Kijai*

- **Uni3c end percentage**: 0.01 (after 1-2 steps)
  - Doesn't have much effect after initial steps, saves time
  - *From: Kijai*

- **fl2v mode**: Always enabled
  - Only affects last frame encoding, prevents issues with same start/end frames
  - *From: Kijai*

- **Block swap for SCAIL on 24GB**: Around 16GB used with half blocks swapped
  - Default resolution with normal Wan 14B requirements
  - *From: Kijai*

- **New T2V distill LoRA**: Better at 2 steps for i2v (1022), 4-6 steps for lightx2v
  - Surprisingly better movement at lower steps
  - *From: patientx*

- **Wan 2.2 as high noise + Wan 1.3B as low noise**: 1.3B at 0.15 denoise
  - Good motion but graphics suffer, lower denoise improves appearance
  - *From: hicho*

- **SCAIL embed strength and end_percent**: Default 1 and 0.5
  - Example workflow values, some experimenting with strength 2 for finger matching
  - *From: ucren*

- **Tile LoRA strength**: Higher than 0.1
  - 0.1 strength won't do much, especially at low denoise
  - *From: spacepxl*

- **UniAnimate strength**: Above 1.0 possible
  - 1.0 limit was only for 2.1, 2.2 can handle higher values
  - *From: Kijai*

- **VitPose stick width for animals**: 20
  - Thicker lines help with animal pose detection in SCAIL
  - *From: Kijai*

- **SCAIL control end percent**: 0.5
  - For speed and because control has no big effect after that point, hands/faces may benefit from higher values
  - *From: Kijai*

- **Uni3C strength**: 0.1 for one step
  - Enough to lock background, higher values may cause weird camera movement
  - *From: Kijai*

- **LongCat Avatar steps**: 20
  - Seems enough for it to work, though single window takes 10 minutes to test
  - *From: Kijai*

- **SVI CFG with Lightx2v LoRA**: CFG 2 with LoRA strength 0.5
  - Prevents burning and keeps motion stable, updated from original CFG 1
  - *From: Hashu*

- **LongCat Avatar steps**: 10 steps
  - Works with less steps than normal model, diminishing returns when increasing step count
  - *From: Kijai*

- **LongCat Avatar audio_cfg**: 3.0
  - Maintains good lipsync but doubles generation time
  - *From: Kijai*

- **LongCat Avatar text_cfg**: 1.0
  - Used with distill LoRA at 0.8 strength for stable results
  - *From: Kijai*

- **LongCat Avatar steps**: 12 steps with distill schedule
  - Balanced quality/speed, much faster than 40+ steps
  - *From: Kijai*

- **Context window overlap for Wan**: 2
  - Proper overlap setting for Wan models
  - *From: Kijai*

- **Blockswap for LongCat Avatar**: 20
  - Required even on 5090 due to 31GB model size, enables 960x960x97 generation
  - *From: burgstall*

- **EasyCache start step**: 5
  - When using 10 total steps, don't start at default 10
  - *From: burgstall*

- **Blockswap**: 10-15 on 5090
  - Good balance for 720x720 resolution before upscaling
  - *From: burgstall*

- **Steps**: 10 steps
  - 6 steps doesn't seem that bad but 10 is better
  - *From: burgstall*

- **Frequency offset**: 4
  - Better than default 1, improves stand-in results
  - *From: Kijai*

- **Audio scale**: varies by input
  - Some inputs need higher audio scale, others go crazy with same amount
  - *From: Kijai*

- **PUSA LoRA strength**: 0.5 to 1
  - Helps with facial consistency in Stand-In
  - *From: ▲*

- **WanMove control strength**: 0.8
  - Allows tree to persist in depth-controlled generations
  - *From: Kijai*

- **Audio CFG**: adjustable
  - Has major impact on lipsync quality
  - *From: Kijai*

- **Base precision for LongCat**: bf16
  - Required for LongCat models to work properly
  - *From: Kijai*

- **WAN 2.1 with LightX2V resolution**: 640x320
  - Demo uses tiny resolution, around 30 secs for each 5s segment on 5090
  - *From: Kijai*

- **SCAIL pose control strength**: 1.0
  - Better than default 0.5 for more faithful pose copying
  - *From: Kijai*

- **Frame rate for SCAIL input/output**: 16fps
  - Input and output fps must match for proper motion transfer
  - *From: ucren*

- **AudioCFG for audio issues**: Increase value
  - Can help resolve audio-related generation problems
  - *From: AmirKerr*

- **StoryMem LoRA strength**: 22
  - Rank stabilized LoRAs need high strength values to have effect
  - *From: Kijai*

- **Block swap**: minimum
  - Reduces loading time for transformer parameters
  - *From: trykiss*

- **Merge LoRA**: off
  - Reduces loading time for transformer parameters
  - *From: trykiss*

- **SVI Pro overlap**: 4
  - Stops glitches when using with lightx2v
  - *From: Benjimon*

- **SVI Pro motion frames**: 1
  - Works with overlap=4 to prevent glitches
  - *From: Benjimon*

- **Motion morph LoRA strength**: 0.3
  - Good starting point for FlippinRad Motion Morph
  - *From: 42hub*

- **Sigma to step**: 0.875 for T2V, 0.9 for I2V
  - Proper handoff between high and low noise samplers
  - *From: CJ*

- **CFG value for LightX2V**: Under 2.0
  - Works well for low CFG scenarios
  - *From: Kijai*

- **Shift value range**: Can go as high as 17
  - To force dramatic changes in step allocation
  - *From: CJ*

- **SVI Pro overlap frames**: 8
  - Needed for proper functionality and seamless transitions
  - *From: DawnII*

- **SVI Pro sigma**: 0.9
  - Good middle ground for extension quality
  - *From: Kijai*

- **Steps for SVI Pro**: 6 with 3 split
  - Equivalent to sigma 0.9, provides good quality
  - *From: Kijai*

- **Stand-in LoRA dimensions**: 512x512 reference, 480x832 output
  - Only dimension combo that maintains likeness properly
  - *From: ucren*

- **Offset parameter**: 2
  - Works better for 1088x640 resolution
  - *From: ucren*

- **Latent strength for initial image**: 0.5
  - Provides better balance in SVI Pro generations
  - *From: DawnII*

- **LightX2V 1030 strength**: 0.6
  - Prevents gray/weird output when using converted loras
  - *From: ucren*

- **Motion latent count**: 1 for first generation, 2 for extensions
  - First gen doesn't need overlap, extensions need anchor and previous latent
  - *From: DawnII*

- **Overlap frames**: 5
  - 4 frames from last latent + 1, standard for SVI Pro
  - *From: Kijai*

- **High noise CFG**: 3.5
  - Good balance for high noise model generation
  - *From: slmonker(5090D 32GB)*

- **High noise steps**: 10
  - Standard steps for high noise model
  - *From: slmonker(5090D 32GB)*

- **Low noise steps**: 4
  - Used with LightX2V for low noise model
  - *From: slmonker(5090D 32GB)*

- **Anchor latent strength**: Variable/reduced
  - Lower values improve prompt following when SVI is too anchored
  - *From: Kijai*

- **Alpha for ultravico**: 0.9 default
  - Default setting in original implementation, no gamma parameter
  - *From: Kijai*

- **CFG and steps without LightX**: 20-30 steps
  - Works well for Wan animate without speed LoRAs
  - *From: TK_999*

- **LightX2V 2.1 with RCM combination**: LightX2V with 0.5 RCM strength
  - Provides realistic physics and good motion coherence
  - *From: faceismus*

- **motion_latent_count**: 2
  - Gives better results than default
  - *From: avataraim*

- **overlap**: 8-10
  - Works well with motion_latent_count 2
  - *From: avataraim*

- **RCM LoRA strength**: 1.5
  - Good balance, can be too strong at higher values
  - *From: avataraim*

- **motion scale amplitude**: 1.2-1.3
  - Good middle ground, 2.0 gives very good motion but more artifacts
  - *From: Elvaxorn*

- **ultravico alpha**: 0.91 or higher
  - Needed for proper scene changes in I2V, but creates looping issues
  - *From: Kijai*

- **augment_empty_frames**: 0.2-0.3
  - Good motion enhancement without artifacts
  - *From: David Snow*

- **pad_frame_value**: 0.5
  - Proper color for empty frames with VACE
  - *From: Kijai*

- **lightx2v strength on high noise**: lower values
  - Improves motion quality
  - *From: ucren*


## Concepts Explained

- **Wan 2.2 High/Low model architecture**: High noise models good at motion, prompt following, composition but lost detail ability. Low noise models are fine-tuned Wan 2.1 that handle details. Use HN for first few steps, then LN to finish
  - *From: Ablejones*

- **Context windows for SteadyDancer**: Model didn't have long gen method, so context windows only option for longer generations
  - *From: Kijai*

- **Context windows in video generation**: Process splits video into overlapping windows (e.g., 1-81, 65-156, 140-221), encodes frames to latents, processes each window separately through sampler, then glues results together. Each window is processed independently by the model
  - *From: Ablejones*

- **Graph breaks in torch compilation**: Failure of torch compilation to understand python code resulting in higher VRAM usage. sageattn_compiled prevents these breaks
  - *From: 42hub*

- **4n+1 frame format**: Wan models work with frame counts following 4n+1 formula because they pack 4 frames into one latent plus 1 reference frame
  - *From: Scruffy*

- **Discretization error vs model loss**: They're additive - if score function isn't accurate, no amount of accurate integration will fix it. Model loss is 1.0 to 0.1 average
  - *From: spacepxl*

- **Diffusion trajectory boomerang shape**: 2nd/3rd order samplers can account for expected boomerang curve, which is why they show outsized gains over 4th/5th order
  - *From: mallardgazellegoosewildcat2*

- **Distillation baking curvature into euler steps**: Distillation process essentially bakes higher order solver or many small euler substeps into one large step
  - *From: spacepxl*

- **SVI padding method**: Uses 5 frames to continue generation and pads with original reference image, combining film motion with shot continuation
  - *From: Kijai*

- **Autoregressive-diffusion hybrid**: Future approach for long generations using some causal masking, not necessarily block causal like magi
  - *From: mallardgazellegoosewildcat2*

- **Low rank training regularization**: Form of regularization that preserves original model capacity better, known advantage of LoRA training
  - *From: mallardgazellegoosewildcat2*

- **SVI noise injection training**: They inject calibrated noise during training to match expected errors in inference and change the prediction target slightly, making the model more robust to noise from recycling reference images
  - *From: mallardgazellegoosewildcat2*

- **Latent space color matching**: Color matching with mean/std works pretty well in latent space for style transfer
  - *From: spacepxl*

- **SVI (Sequential Video Interpolation)**: Trains model to be robust to noise from sequential steps and repeated conditioning on end frames, shifts prediction target to be more noise-robust
  - *From: mallardgazellegoosewildcat2*

- **Memory leak vs normal cache behavior**: Leak is when same node run multiple times grows memory each time. Different nodes caching different image sizes is normal behavior
  - *From: Kijai*

- **SVI LoRA frame overlap mechanism**: v2.0/SVI_Wan2.1 permits overlap of 5 frames while v2.0/SVI_Wan2.2 permits less. Each time people write 'SVI 2.0' it's unclear which specific safetensors they're using
  - *From: 42hub*

- **WAN latent encoding structure**: 1st frame in sequence on WAN is encoded differently - with 4x as much space as other frames and subsequent latents use encoding of that frame as reference. Cannot simply chop last latents from previous generation as they're not meaningful on their own
  - *From: 42hub*

- **LoRA merging vs unmerged behavior**: Loads weights and merges LoRA weights into them (native comfy behavior). GGUF models don't allow merging, so lora weights are added on top of de-quantized weight when used. Effect differs by model/LoRA
  - *From: Kijai*

- **Token replacement**: Technique that sets timestep of next 2 frames after reference frame to 0 to prevent them from changing too much from initialization
  - *From: Kijai*

- **Video DiT parameter requirements**: Video DiTs seem to need around 20B parameters, with 15B (like Wan and HunV) doing okay
  - *From: mallardgazellegoosewildcat2*

- **Extension method token replacement**: Frame 0 gets ref_cond and skipped (0 timestep), Frame 1 and 2 get replaced, rest uses normal timestep. Similar to noise mask after certain timestep
  - *From: Kijai*

- **Conv3d memory issue**: Memory problem from hunyuan VAE parts before sampling starts, needs conv3d fix applied
  - *From: Kijai*

- **Patch embed reshaping**: RCM models have fused patch embed that needs reshaping - view(v.shape[0], 36, 1, 2, 2) for I2V, different for T2V
  - *From: Kijai*

- **rCM (rectified Consistency Model)**: Alternative distillation method for speed LoRAs, not just higher resolution
  - *From: Kijai*

- **TTM (Time-to-Move)**: Vid2vid method with masked noise injection for controlled video generation
  - *From: Kijai*

- **LoRA rank**: Higher rank closer to full model but diminishing returns above 64, affects file size especially for unmerged/GGUF
  - *From: Kijai*

- **SVI (Stable Video Interpolation)**: Video control system that trains on error noise to overcome degradation, helps with character consistency but limits camera movement
  - *From: mallardgazellegoosewildcat2*

- **High noise vs Low noise model splitting**: Technique where different models handle different noise levels - HuMo as low noise, Wan 2.2 as high noise
  - *From: Ablejones*

- **Tracks data type**: New ComfyUI data type that holds path and mask tensors for trajectory control, replacing JSON coordinates
  - *From: Kijai*

- **NAG (Negative Attention Guidance)**: Additional attention in positive pass only, separate from CFG negative passes. Less powerful than true negative but better targeted effect
  - *From: Kijai*

- **SVI embedding approach**: Places continuation frame as first image, rest are copies of initial reference image for consistency
  - *From: Chandler ✨ 🎈*

- **Lightning vs lightx2v-distill**: Different methods - Lightning is adversarial (higher quality, less diversity), lightx2v-distill was self-forcing trained
  - *From: Kijai*

- **Consistency model (rCM)**: Works by making jumps along ODE solver trajectory, requires operating on same ODE it was trained on, essentially a ksampler with trained big jumps
  - *From: mallardgazellegoosewildcat2*

- **SCAIL pose format**: Uses warm colors on right side, cool colors on left side, combines 3D and 2D pose information
  - *From: Kijai*

- **SCAIL**: Wan 2.1 14B model variant with pose control capabilities, uses 3D skeleton rendering different from standard OpenPose
  - *From: Kijai*

- **NLF (Natural Language Foundation)**: 3D pose detection system used by SCAIL, requires 3D libraries and has research-only license
  - *From: Kijai*

- **Patch embed for pose**: SCAIL model has separate patch embedding for pose input, so pose doesn't have to match video resolution exactly
  - *From: Kijai*

- **Beta sigmas application order**: In diffusers beta sigmas are applied after shift, while in ComfyUI it's the other way around, leading to completely different sigma schedules
  - *From: Kijai*

- **V2 nodes architecture**: New modular node design with separate components: text_embeds, image_embeds, scheduler, extra_args for cleaner workflows
  - *From: Scruffy*

- **Monkey patching**: Globally overriding library functions like torch.load - considered bad practice
  - *From: FlipYourBits*

- **GetTrackRange**: Node that splits spline paths across multiple context windows for continuous movement
  - *From: Kijai*

- **Speed mode in WanMove**: Feature that allows adjusting movement speed at specific points by adding control points
  - *From: Kijai*

- **Activation quantization**: Optimization technique used in TurboWan for faster inference
  - *From: Kijai*

- **RCM distillation**: Method used in TurboWan for model compression and speedup
  - *From: yi*

- **Taichi backend**: Computing framework that can run on CPU, GPU, OpenGL or Vulkan
  - *From: Kijai*

- **NLF (Neural Light Field)**: 3D pose capture method that's more tolerant to input videos than other existing 3D human-motion capture methods, can handle weird portion inputs
  - *From: teal024*

- **Retargeting in SCAIL**: Process that adjusts poses using thresholds for horizontal and portrait scaling to align reference and driving poses
  - *From: teal024*

- **RoPE cache**: Rotary Position Embedding cache that can cause tensor mismatches when switching between different frame counts or resolutions
  - *From: Flipping Sigmas*

- **Context window morphing**: Technique used for generating videos longer than base model limits, can cause some inconsistencies at transition points
  - *From: Kijai*

- **SCAIL**: Video control system that transfers poses from video to reference images
  - *From: David Snow*

- **Distill LoRAs**: LoRAs that enable fewer sampling steps but reduce motion/structure variety while improving detail quality
  - *From: spacepxl*

- **VACE architecture**: Basically just a controlnet on top of an unmodified t2v model
  - *From: spacepxl*

- **Multi-person NLF tracking**: 3D pose tracking that should handle multiple people but currently flashes between identities without proper segmentation
  - *From: Kijai*

- **Context window morphing**: Background shifts that occur at the boundaries of context windows in longer SCAIL generations
  - *From: slmonker(5090D 32GB)*

- **Patch size optimization**: VIT research confirms patch size 16 is optimal, patch size 32 used in newer models isn't good yet
  - *From: spacepxl*

- **SCAIL reference image**: The reference image in SCAIL acts as the start frame of the generation, not a separate style reference
  - *From: Kijai*

- **Context window bleeding**: Background inconsistency that occurs when using context windows with moving cameras in video generation
  - *From: Kijai*

- **fl2v mode**: First-Last-Frame mode in I2V encode node, affects how last frame is encoded when provided
  - *From: Kijai*

- **Context windowing background drift**: Each window tries to return to reference camera position/background since same reference is used, causing background shifts
  - *From: Kijai*

- **DF11 quantization**: Lossless 30% VRAM reduction technique, 100% identical to fp16 but smaller file size
  - *From: Ada*

- **Differential diffusion**: Automatically used when adding mask to WanVideo Encode node or Set Latent Noise Mask
  - *From: Kijai*

- **Context windows vs frame extension**: Context windows don't usually degrade quality like frame extension, they have blend seams instead
  - *From: spacepxl*

- **fp8 scaled diffusion**: Still uses fp16/bf16 for calculations, only stored weights are fp8. Gets upcast and scaled on the fly
  - *From: spacepxl*

- **Clean latent frame**: In InfiniteTalk, first frame must be actual image data rather than noise to prevent flash artifacts
  - *From: Kijai*

- **NLF (pose detection)**: Detection process that creates skeleton style unique to SCAIL with specific color coding
  - *From: Kijai*

- **Prompt splitting with |**: Using | symbol to provide different prompts per context window in long generations
  - *From: Gleb Tretyak*

- **ref_target_masks**: Masks for InfiniteTalk Multi to target specific speakers in multi-person scenarios
  - *From: Gleb Tretyak*

- **fun_or_fl2v_model toggle**: off = encode last image on its own like first image; on = insert last image as last pixel image and encode all together
  - *From: Kijai*

- **FlashPortrait long generation method**: Uses context windows similar to FantasyPortrait, not actually a novel acceleration technique
  - *From: Kijai*

- **ref_latent in LongCat Avatar**: Reference latent inserted at ref_frame_index position in latent space to maintain consistency in longer extensions
  - *From: Kijai*

- **prev_latents in LongCat Avatar**: Where generation continues from, overlap amount of frames are taken from previous latents
  - *From: Kijai*

- **VACE control batches**: VACE supports multiple control frames - you can input start/end frames plus any intermediate frames for better control
  - *From: Kijai*

- **Frame windows**: 93 frame processing windows aren't entirely necessary if you have enough memory
  - *From: Kijai*

- **Denoise step skipping**: Denoise value skips steps - 0.21 denoise means only doing 20% of total steps
  - *From: Kijai*

- **Mixed precision quantization**: New ComfyUI system allows customizable precision per layer instead of downcasting everything
  - *From: Kijai*

- **LN**: Low noise - refers to the low noise variant of models
  - *From: ucren*

- **MI2V**: Memory + first-frame image conditioning to connect adjacent shots when scene_cut is False
  - *From: NebSH*

- **MM2V**: Memory + first 5 motion frames conditioning to connect adjacent shots when scene_cut is False
  - *From: NebSH*

- **Asset pop-in**: A learned 'feature' where objects appear/disappear inconsistently in generated videos
  - *From: Kijai*

- **NVFP4**: New precision format for Blackwell cards with dedicated kernel support
  - *From: JohnDopamine*

- **Rank stabilized LoRAs**: LoRAs that use different alpha scaling and require special handling, need high strength values or automatic scaling
  - *From: Kijai*

- **Context windows with reference images**: Can use multiple reference images for different segments of video generation, each image applies to corresponding prompt segment
  - *From: Kijai*

- **StoryMem memory frames**: Extracted based on quality score using HPS model, model uses max 3 at once with position being random
  - *From: Kijai*

- **Last latent conditioning**: SVI 2.0 Pro now feeds last latent index instead of last frame for better compatibility with other controls
  - *From: DawnII*

- **VAE LoRA loading**: Wan Alpha 2.0 uses separate foreground and alpha VAE models with LoRA applied to decoder only
  - *From: Gleb Tretyak*

- **Skeleton scaling in SCAIL**: SCAIL scales the skeleton of input video TO the input image, not the other way around
  - *From: DawnII*

- **NVFP4**: Advanced 4-bit quantization method that's more sophisticated than naive 4-bit downcasting, preserves core information while compressing non-essential content
  - *From: Kijai*

- **Distillation in LightX2V context**: Process that reduces inference steps while maintaining quality, allows faster generation
  - *From: Kijai*

- **Tensor format BCHW**: Batch Channel Height Width - how tensors are arranged in ComfyUI, I2V=36 channels, T2V=16 channels
  - *From: cyncratic*

- **Distilling a model**: Training it to use fewer steps, sometimes by training on its own outputs
  - *From: Benjimon*

- **FreeLong spectral blending**: Windowing attention using sliding windows for more frames than model trained for, but not the same as continuing from last frame
  - *From: Kijai*

- **SVI Pro latent continuation**: Uses previous generation latent directly instead of encoding/decoding frames, providing seamless continuity
  - *From: DawnII*

- **FreeLong++ technique**: Low bandpass filter on latents for consistent outputs, can do 81x2, x4, or x8 frame options
  - *From: campeonchik*

- **Anchor samples in SVI Pro**: Initial first frame that keeps generation from degrading over extensions
  - *From: Kijai*

- **Motion latent count**: Number of latents to carry over between generations - includes anchor and previous generation latents
  - *From: DawnII*

- **Ultravico**: Modified attention mechanism with hard coded frame_tokens for 832x480, works poorly at other resolutions
  - *From: Kijai*

- **Anchor latent in SVI**: The initial frame used as anchor to prevent degradation, but if scene changes completely it won't help much
  - *From: Kijai*

- **DoRA vs LoRA**: DoRA uses magnitude_vector weights, ComfyUI can load DoRAs by adding proper prefixes to keys
  - *From: Kijai*

- **StorymMem functionality**: MI2V LoRA continues from last frame, MMI2V from 5 last frames, both can use memory images
  - *From: Kijai*

- **sageattn_ultravico**: An attention_mode that can be chosen on WanVideoModelLoader in Wrapper for extended length generations
  - *From: 42hub*

- **Motion scale control**: Ability to control the speed and timing of motion in video generation, essentially motion-level prompt enforcement
  - *From: Ada*

- **Context Windows**: Method used for partial denoising in models like HuMo and InfiniteTalk to turn them into V2V
  - *From: 42hub*

- **augment_empty_frames**: Adds inverse of start image into empty frames of I2V conditioning to push away from start image, can introduce artifacts
  - *From: Kijai*

- **pad_frame_value**: The color of the empty frames in video generation
  - *From: Kijai*

- **ScaleROPE**: Tells model that frames are different count than actual (like 81 frames are actually 40), can lead to unwanted behavior
  - *From: Kijai*

- **Context Windows**: Generic mechanism to make models generate videos longer than 81 frames even if models weren't originally intended for it
  - *From: 42hub*

- **FreeLong frequency blending**: Blends low-frequency components of global video features with high-frequency components of local video features for consistency
  - *From: mallardgazellegoosewildcat2*


## Resources & Links

- **Upscalers gossip collection** (documentation)
  - https://wanx-troopers.github.io/upscalers.html
  - *From: 42hub*

- **SteadyDancer FP8 model** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy_fp8_scaled/tree/main/SteadyDancer
  - *From: Kijai*

- **SAM3 ComfyUI nodes** (repo)
  - https://github.com/PozzettiAndrea/ComfyUI-SAM3
  - *From: BitJuggler*

- **DiT-Mem-1.3B model** (model)
  - https://huggingface.co/Thrcle/DiT-Mem-1.3B
  - *From: hicho*

- **Apple StarFlow model** (model)
  - https://huggingface.co/apple/starflow
  - *From: shaggss*

- **DiT-Extrapolation (UltraViCo)** (repo)
  - https://github.com/thu-ml/DiT-Extrapolation/commit/bd97f25dd06830d4f01a5eafcb1f07a442bbaa5f
  - *From: JohnDopamine*

- **ComfyUI-AnimateDiff-Evolved Context Options documentation** (documentation)
  - https://github.com/Kosinkadink/ComfyUI-AnimateDiff-Evolved/tree/main/documentation/nodes#context-optionsstandard-uniform
  - *From: Kijai*

- **ComfyUI-outputlists-combiner nodepack** (node pack)
  - https://github.com/geroldmeisinger/ComfyUI-outputlists-combiner
  - *From: Gleb Tretyak*

- **Lotus-2** (model)
  - https://github.com/EnVision-Research/Lotus-2
  - *From: A.I.Warper*

- **LongCat example workflow** (workflow)
  - workflow file shared
  - *From: Kijai*

- **TCD sampler for ComfyUI** (tool)
  - https://github.com/JettHu/ComfyUI-TCD
  - *From: mallardgazellegoosewildcat2*

- **ComfyUI Wan context options PR** (repo)
  - https://github.com/comfyanonymous/ComfyUI/pull/10975
  - *From: spacepxl*

- **Distillation paper on trajectory analysis** (paper)
  - https://arxiv.org/abs/2511.22475
  - *From: spacepxl*

- **ComfyUI-MultiGPU loader** (tool)
  - https://github.com/pollockjj/ComfyUI-MultiGPU
  - *From: David Snow*

- **Long Penis LoRA** (model)
  - https://civitai.com/models/2181569?modelVersionId=2467448
  - *From: harrisonwells*

- **VACE custom node for keyframe insertion** (tool)
  - https://old.reddit.com/r/comfyui/comments/1l93f7w/my_weird_custom_node_for_vace/
  - *From: JohnDopamine*

- **SVI 2.0 converted LoRA** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/blob/main/LoRAs/Stable-Video-Infinity/v2.0/SVI_Wan2.1-I2V-14B_lora_v2.0_rank_128_fp16.safetensors
  - *From: Kijai*

- **Steadydancer tutorial** (tutorial)
  - https://www.youtube.com/watch?v=53QdhJcUjvQ
  - *From: David Snow*

- **One-to-All Animation** (repo)
  - https://github.com/ssj9596/One-to-All-Animation
  - *From: Kijai*

- **SVI 2.0 original model** (model)
  - https://huggingface.co/vita-video-gen/svi-model/tree/main/version-2.0
  - *From: Gleb Tretyak*

- **LongCat-Image-Edit model** (model)
  - https://huggingface.co/meituan-longcat/LongCat-Image-Edit
  - *From: DawnII*

- **WanEx_I2VCustomEmbeds node** (repo)
  - https://github.com/drozbay/WanExperiments
  - *From: Ablejones*

- **ComfyScript** (tool)
  - https://github.com/Chaoses-Ib/ComfyScript
  - *From: mallardgazellegoosewildcat2*

- **DrPanGloss ComfyUI fork** (repo)
  - https://github.com/hiddenswitch/ComfyUI
  - *From: Scruffy*

- **TrentNodes keyframe node** (repo)
  - https://github.com/TrentHunter82/TrentNodes/tree/main
  - *From: Flipping Sigmas*

- **ComfyUI-PromptHelper** (tool)
  - https://github.com/LeonQ8/ComfyUI-PromptHelper
  - *From: Léon*

- **Aquif-Image-14B** (model)
  - https://huggingface.co/aquif-ai/aquif-Image-14B
  - *From: yi*

- **ComfyUI-GIMM-VFI** (repo)
  - https://github.com/kijai/ComfyUI-GIMM-VFI
  - *From: Kijai*

- **ComfyUI_Fill-Nodes** (repo)
  - https://github.com/filliptm/ComfyUI_Fill-Nodes/
  - *From: lostintranslation*

- **ComfyUI-EasyColorCorrector** (repo)
  - https://github.com/regiellis/ComfyUI-EasyColorCorrector
  - *From: lostintranslation*

- **SVI model 2.0** (model)
  - https://huggingface.co/vita-video-gen/svi-model/tree/main/version-2.0
  - *From: JohnDopamine*

- **WanExperiments repository** (repo)
  - https://github.com/drozbay/WanExperiments
  - *From: Ablejones*

- **SVI 2.0 LoRAs** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/tree/main/LoRAs/Stable-Video-Infinity/v2.0
  - *From: Ablejones*

- **ViSAudio video->audio tracking** (repo)
  - https://github.com/kszpxxzmc/ViSAudio
  - *From: Kiwv*

- **MAGI-1 hybrid autoregressive/diffusion model** (repo)
  - https://github.com/SandAI-org/MAGI-1
  - *From: mallardgazellegoosewildcat2*

- **One-to-All-Animation** (repo)
  - https://github.com/ssj9596/One-to-All-Animation
  - *From: Kijai*

- **Flash Attention for Windows** (tool)
  - https://huggingface.co/ussoewwin/Flash-Attention-2_for_Windows/blob/main/flash_attn-2.8.3%2Bcu130torch2.9.1cxx11abiTRUE-cp312-cp312-win_amd64.whl
  - *From: Gleb Tretyak*

- **WanX Troopers SVI documentation** (documentation)
  - https://wanx-troopers.github.io/svi.html
  - *From: 42hub*

- **WanX Troopers extensions documentation** (documentation)
  - https://wanx-troopers.github.io/extensions.html
  - *From: 42hub*

- **WanX Troopers HuMo documentation** (documentation)
  - https://wanx-troopers.github.io/humo.html
  - *From: 42hub*

- **Spiritus skeletal AI animation paper** (research)
  - https://dl.acm.org/doi/10.1145/3746059.3747707
  - *From: Gleb Tretyak*

- **NotebookLM Wan chat model** (tool)
  - https://notebooklm.google.com/notebook/a08901b9-0511-4926-bbf8-3c86a12dc306?pli=1
  - *From: JohnDopamine*

- **OneToAll Animation fp8 model** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy_fp8_scaled/blob/main/OneToAllAnimation/Wan21-OneToAllAnimation_fp8_e4m3fn_scaled_KJ.safetensors
  - *From: Kijai*

- **SVI Wan2.2 workflow** (workflow)
  - https://github.com/vita-epfl/Stable-Video-Infinity/blob/svi_wan22/comfyui_workflow/SVI-Wan22-1207.json
  - *From: Ablejones*

- **Wan ecosystem documentation** (documentation)
  - https://wanx-troopers.github.io/
  - *From: 42hub*

- **LightX2V Distill LoRAs** (lora)
  - https://huggingface.co/Kijai/WanVideo_comfy/tree/main/LoRAs/Wan22_Lightx2v
  - *From: DawnII*

- **SCAIL project** (project)
  - https://teal024.github.io/SCAIL/
  - *From: Kijai*

- **RCM Wan 2.2 I2V model** (model)
  - https://huggingface.co/worstcoder/rcm-Wan/blob/main/Wan2.2-I2V-A14B-high-rCM6.0-merged.pth
  - *From: DawnII*

- **OneToAll workflow** (workflow)
  - https://discord.com/channels/1076117621407223829/1342763350815277067/1447650547841630381
  - *From: Josiah*

- **SCAIL Preview model** (model)
  - https://huggingface.co/zai-org/SCAIL-Preview
  - *From: Kijai*

- **Triton Windows wheels** (tool)
  - https://github.com/woct0rdho/triton-windows
  - *From: Kijai*

- **SageAttention wheels** (tool)
  - https://github.com/woct0rdho/SageAttention
  - *From: Kijai*

- **RCM LoRA conversion** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/blob/main/LoRAs/rCM/Wan22-I2V-A14B-HIGH-rCM6_0_lora_rank_64_bf16.safetensors
  - *From: Kijai*

- **Manim Community repo** (tool)
  - https://github.com/ManimCommunity/manim
  - *From: Scruffy*

- **Wan-Move-14B model** (model)
  - https://huggingface.co/Ruihang/Wan-Move-14B-480P
  - *From: DawnII*

- **Live Avatar model** (model)
  - https://huggingface.co/Quark-Vision/Live-Avatar
  - *From: DawnII*

- **WanMove OneToAll animation workflow** (workflow)
  - https://github.com/kijai/ComfyUI-WanVideoWrapper/blob/main/example_workflows/Wan21_OneToAllAnimation_example_01.json
  - *From: 42hub*

- **LightX2V LoRA guide and links** (guide)
  - https://wanx-troopers.github.io/loras/part-01.html#22-i2v
  - *From: 42hub*

- **rCM high noise LoRA** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/blob/main/LoRAs/rCM/Wan22-I2V-A14B-HIGH-rCM6_0_lora_rank_64_bf16.safetensors
  - *From: Kijai*

- **rCM low noise LoRA** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/blob/main/LoRAs/rCM/Wan22-I2V-A14B-LOW-rCM1_0_lora_rank_64_bf16.safetensors
  - *From: Kijai*

- **TTS Audio Suite** (node pack)
  - https://github.com/diodiogod/TTS-Audio-Suite
  - *From: Gleb Tretyak*

- **WanMove fp8 scaled models** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy_fp8_scaled/tree/main/WanMove
  - *From: slmonker*

- **Ovi TTS workflow** (model)
  - https://github.com/character-ai/Ovi
  - *From: Lumi*

- **Upscaler recommendations** (guide)
  - https://wanx-troopers.github.io/upscalers.html
  - *From: 42hub*

- **VRGameDevGirl84 ComfyUI workflows and custom nodes** (workflow)
  - https://github.com/vrgamegirl19/comfyui-vrgamedevgirl/tree/main/Workflows
  - *From: VRGameDevGirl84(RTX 5090)*

- **UCPE paper/implementation** (repo)
  - https://github.com/chengzhag/UCPE
  - *From: JohnDopamine*

- **WanMove repository** (repo)
  - https://github.com/ali-vilab/Wan-Move
  - *From: Charlie*

- **SVI model on HuggingFace** (model)
  - https://huggingface.co/vita-video-gen/svi-model
  - *From: Cseti*

- **FL-Path-Animator for trajectory control** (tool)
  - https://github.com/filliptm/ComfyUI_FL-Path-Animator
  - *From: Gateway {Dreaming Computers}*

- **WanMove example workflow** (workflow)
  - https://github.com/kijai/ComfyUI-WanVideoWrapper/blob/main/example_workflows/wanvideo_WanMove_I2V_example_01.json
  - *From: CaptHook*

- **Wan2.2 Lightning I2V lora** (lora)
  - https://huggingface.co/Aitrepreneur/FLX/blob/main/Wan2.2-Lightning_I2V-A14B-4steps-lora_LOW_fp16.safetensors
  - *From: David Snow*

- **SVI loras for Wan2.2** (lora)
  - https://huggingface.co/Kijai/WanVideo_comfy/tree/main/LoRAs/Stable-Video-Infinity/v2.0
  - *From: BarleyFarmer*

- **SVI ComfyUI workflow** (workflow)
  - https://github.com/vita-epfl/Stable-Video-Infinity/tree/svi_wan22/comfyui_workflow
  - *From: Doctor Diffusion*

- **WanX Troopers lora collection** (resource)
  - https://wanx-troopers.github.io/loras/part-01.html
  - *From: 42hub*

- **Wan-Move notes** (resource)
  - https://wanx-troopers.github.io/wan-move.html
  - *From: 42hub*

- **SpatialTracker V2** (tool)
  - https://spatialtracker.github.io/
  - *From: Kijai*

- **ComfyUI Tracks node PR** (repo)
  - https://github.com/comfyanonymous/ComfyUI/pull/11247
  - *From: Kijai*

- **OneToAll 1.3B v2 model** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/blob/main/OneToAllAnimation/Wan21-OneToAllAnimation_1_3B_v2_fp16.safetensors
  - *From: Kijai*

- **SageAttention latest release** (repo)
  - https://github.com/woct0rdho/SageAttention
  - *From: Kijai*

- **Triton Windows wheels** (repo)
  - https://github.com/woct0rdho/triton-windows
  - *From: Zabo*

- **MultiGPU ComfyUI extension** (tool)
  - https://github.com/pollockjj/ComfyUI-MultiGPU
  - *From: David Snow*

- **Trent keyframe nodes** (node)
  - https://github.com/TrentHunter82/TrentNodes/tree/main
  - *From: Dream Making*

- **Triton/Sage install tutorial** (tutorial)
  - https://discord.com/channels/1076117621407223829/1145677539738665020/1445821826994405516
  - *From: garbus*

- **SCAIL fp8 model** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy_fp8_scaled/blob/main/SCAIL/Wan21-14B-SCAIL-preview_fp8_e4m3fn_scaled_KJ.safetensors
  - *From: Kijai*

- **Cinematic Fast Cutting LoRA** (model)
  - https://civitai.com/models/2113025/cinematic-fast-cutting-previously-quick-cuts
  - *From: NebSH*

- **WanVideoWrapper example workflows** (workflow)
  - https://github.com/kijai/ComfyUI-WanVideoWrapper/tree/main/example_workflows
  - *From: 42hub*

- **NLF pose detection** (repo)
  - https://github.com/isarandi/nlf
  - *From: 42hub*

- **Online pose editor** (tool)
  - https://zhuyu1997.github.io/open-pose-editor/
  - *From: JohnDopamine*

- **SCAIL documentation** (documentation)
  - https://wanx-troopers.github.io/wan-animates.html#scail
  - *From: 42hub*

- **ComfyUI-SCAIL-Pose** (repo)
  - https://github.com/kijai/ComfyUI-SCAIL-Pose
  - *From: Kijai*

- **TrentNodes (problematic)** (repo)
  - https://github.com/TrentHunter82/TrentNodes
  - *From: Flipping Sigmas*

- **Alibaba WAN model launch event** (announcement)
  - https://www.alibabacloud.com/en/events/wan-model-launch
  - *From: seruva19*

- **SCAIL official repository** (repo)
  - https://github.com/zai-org/SCAIL
  - *From: teal024*

- **ComfyUI SCAIL Pose node** (repo)
  - https://github.com/kijai/ComfyUI-SCAIL-Pose
  - *From: slmonker(5090D 32GB)*

- **TurboWan 2.2 I2V 14B model** (model)
  - https://huggingface.co/TurboDiffusion/TurboWan2.2-I2V-A14B-720P
  - *From: JohnDopamine*

- **SCAIL models for ComfyUI** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy_fp8_scaled/tree/main/SCAIL
  - *From: slmonker(5090D 32GB)*

- **TurboDiffusion technical paper** (repo)
  - https://jt-zhang.github.io/files/TurboDiffusion_Technical_Report.pdf
  - *From: yi*

- **SCAIL GitHub repository** (repo)
  - https://github.com/zai-org/SCAIL
  - *From: teal024*

- **Cinematic Quick Cuts LoRA** (model)
  - https://huggingface.co/neph1/cinematic_quick_cuts_wan
  - *From: DawnII*

- **SCAIL GGUF quantized model** (model)
  - https://huggingface.co/vantagewithai/SCAIL-Preview-GGUF
  - *From: rgeryrfb54r4*

- **Fill Nodes for RIFE interpolation** (node)
  - https://github.com/filliptm/ComfyUI_Fill-Nodes
  - *From: FL13*

- **LightX2V LoRA comparison guide** (guide)
  - https://wanx-troopers.github.io/loras/part-01.html
  - *From: 42hub*

- **SCAIL models** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy_fp8_scaled/tree/main/SCAIL
  - *From: David Snow*

- **LightX2V LoRA guide** (guide)
  - https://wanx-troopers.github.io/loras/part-01.html
  - *From: 42hub*

- **TurboDiffusion Wan models** (model)
  - https://huggingface.co/TurboDiffusion/TurboWan2.2-I2V-A14B-720P
  - *From: Ada*

- **WanViTPoseRetargeter** (node)
  - https://github.com/red-polo/ComfyUI-WanViTPoseRetargeter
  - *From: dj47*

- **T3-Video models** (model)
  - https://huggingface.co/APRIL-AIGC/T3-Video
  - *From: yi*

- **AI Windows wheels** (repo)
  - https://github.com/wildminder/AI-windows-whl
  - *From: JohnDopamine*

- **SCAIL pose control** (repo)
  - https://github.com/zai-org/SCAIL
  - *From: David Snow*

- **SCAIL AudioReactive ComfyUI** (repo)
  - https://github.com/ckinpdx/ComfyUI-SCAIL-AudioReactive
  - *From: ComfyCod3r*

- **TurboDiffusion supporting Wan** (repo)
  - https://github.com/thu-ml/TurboDiffusion
  - *From: tintwotin*

- **LongCat-Video-Avatar** (model)
  - https://meigen-ai.github.io/LongCat-Video-Avatar/ https://github.com/meituan-longcat/LongCat-Video
  - *From: yi*

- **Wan 2.6 creation interface** (tool)
  - https://create.wan.video/
  - *From: Gateway {Dreaming Computers}*

- **TrentNodes for video transitions** (repo)
  - https://github.com/TrentHunter82/TrentNodes
  - *From: cyncratic*

- **SCAIL prompt generation snippets** (repo)
  - https://github.com/zai-org/SCAIL
  - *From: teal024*

- **T3-Video model** (model)
  - https://huggingface.co/APRIL-AIGC/T3-Video
  - *From: hicho*

- **ComfyUI-WarperNodes** (repo)
  - https://github.com/AIWarper/ComfyUI-WarperNodes
  - *From: David Snow*

- **LongCat-Video** (repo)
  - https://github.com/meituan-longcat/LongCat-Video
  - *From: Kijai*

- **LongCat-Video-Avatar** (repo)
  - https://github.com/MeiGen-AI/LongCat-Video-Avatar
  - *From: Kijai*

- **Skyreels models collection** (model)
  - https://huggingface.co/collections/Skywork/skyreels-v2
  - *From: JohnDopamine*

- **New T2V Distill LoRAs** (model)
  - https://huggingface.co/lightx2v/Wan2.2-Distill-Loras/tree/main
  - *From: yi*

- **DF11 Wan Models** (model)
  - https://huggingface.co/DFloat11/Wan2.2-I2V-A14B-DF11
  - *From: Ada*

- **ComfyUI-DFloat11-Extended** (tool)
  - https://github.com/BigStationW/ComfyUI-DFloat11-Extended
  - *From: Ada*

- **Wan Move Model** (model)
  - https://huggingface.co/Ruihang/Wan-Move-14B-480P
  - *From: Gleb Tretyak*

- **DCM Model** (model)
  - https://huggingface.co/cszy98/DCM
  - *From: hicho*

- **TurboDiffusion** (repo)
  - https://github.com/thu-ml/TurboDiffusion
  - *From: patientx*

- **Lumos-Custom relighting model** (model)
  - https://github.com/alibaba-damo-academy/Lumos-Custom
  - *From: Kijai*

- **LightX2V Wan2.2 Distill LoRAs** (model)
  - https://huggingface.co/lightx2v/Wan2.2-Distill-Loras/tree/main
  - *From: aipmaster*

- **VAE-decode-hdr** (repo)
  - https://github.com/netocg/vae-decode-hdr
  - *From: Juan Gea*

- **ComfyUI-HQ-Image-Save** (repo)
  - https://github.com/spacepxl/ComfyUI-HQ-Image-Save
  - *From: spacepxl*

- **Luminance Stack Processor** (repo)
  - https://github.com/sumitchatterjee13/Luminance-Stack-Processor
  - *From: chrisd0073*

- **WASWanExposureStabilizer** (tool)
  - https://github.com/WASasquatch/WAS_Extras
  - *From: 42hub*

- **IC-Effect research** (research)
  - https://cuc-mipg.github.io/IC-Effect/
  - *From: DawnII*

- **Wan Alpha v2.0** (repo)
  - https://github.com/WeChatCV/Wan-Alpha
  - *From: Hashu*

- **Stable Video Infinity** (repo)
  - https://github.com/vita-epfl/Stable-Video-Infinity
  - *From: burgstall*

- **SVI documentation** (documentation)
  - https://wanx-troopers.github.io/svi.html
  - *From: 42hub*

- **Context Windows guide** (documentation)
  - https://wanx-troopers.github.io/what-plugs-where/context-windows.html
  - *From: 42hub*

- **Extensions documentation** (documentation)
  - https://wanx-troopers.github.io/extensions.html
  - *From: 42hub*

- **NLF pose detection** (research)
  - https://istvansarandi.com/nlf/
  - *From: Kijai*

- **WorldCanvas** (model)
  - https://worldcanvas.github.io/
  - *From: Kijai*

- **Z-Image Turbo Fun Controlnet Union** (model)
  - https://huggingface.co/alibaba-pai/Z-Image-Turbo-Fun-Controlnet-Union
  - *From: xwsswww*

- **TurboDiffusion** (repo)
  - https://github.com/thu-ml/TurboDiffusion
  - *From: AiGangster*

- **FlashPortrait** (model)
  - https://huggingface.co/FrancisRing/FlashPortrait
  - *From: DawnII*

- **FlashPortrait** (model)
  - https://github.com/Francis-Rings/FlashPortrait
  - *From: slmonker(5090D 32GB)*

- **LongCat Avatar workflow** (workflow)
  - https://github.com/kijai/ComfyUI-WanVideoWrapper/tree/longcat_avatar
  - *From: asd*

- **OpenPose skeleton for SCAIL** (tool)
  - https://toyxyz.gumroad.com/l/ciojz
  - *From: manzonif_01*

- **Pivot Animator for stick figure animation** (tool)
  - https://pivotanimator.net/index.html
  - *From: Jumper*

- **LongVie for 5-minute videos** (repo)
  - https://github.com/Vchitect/LongVie
  - *From: dj47*

- **DITTO denoising/enhancing** (repo)
  - https://github.com/EzioBy/Ditto
  - *From: JohnDopamine*

- **Ditto LoRA versions** (lora)
  - https://huggingface.co/Kijai/WanVideo_comfy/tree/main/LoRAs/Ditto
  - *From: JohnDopamine*

- **Ditto Full Modules** (model)
  - https://huggingface.co/QingyanBai/Ditto_models/tree/main/models_comfy
  - *From: JohnDopamine*

- **Stand-In LoRA** (lora)
  - https://huggingface.co/Kijai/WanVideo_comfy/tree/main/LoRAs/Stand-In
  - *From: Kijai*

- **LongVie2 paper** (research)
  - https://arxiv.org/html/2512.13604v1
  - *From: Kijai*

- **Stand-In model page** (model)
  - https://huggingface.co/BowenXue/Stand-In
  - *From: DawnII*

- **LongCat-Avatar fp8 model** (model)
  - https://huggingface.co/Kijai/LongCat-Video_comfy/blob/main/Avatar/LongCat-Avatar-single_fp8_e4m3fn_scaled_mixed_KJ.safetensors
  - *From: Kijai*

- **Stand-In Preprocessor** (repo)
  - https://github.com/WeChatCV/Stand-In_Preprocessor_ComfyUI
  - *From: NebSH*

- **LongVie2 model** (model)
  - https://huggingface.co/Vchitect/LongVie2/tree/main
  - *From: slmonker(5090D 32GB)*

- **EgoX project** (repo)
  - https://github.com/DAVIAN-Robotics/EgoX
  - *From: slmonker(5090D 32GB)*

- **WAN documentation** (documentation)
  - https://wanx-troopers.github.io/talkies/longcat-avatar.html
  - *From: 42hub*

- **HuMoSet dataset** (dataset)
  - https://modelscope.cn/datasets/leoniuschen/HuMoSet
  - *From: JohnDopamine*

- **Wan-NVFP4 model** (model)
  - https://huggingface.co/lightx2v/Wan-NVFP4
  - *From: yi*

- **ComfyUI-SCAIL-AudioReactive** (tool)
  - https://github.com/ckinpdx/ComfyUI-SCAIL-AudioReactive
  - *From: Dream Making*

- **ComfyUI-WanSoundTrajectory** (tool)
  - https://github.com/ckinpdx/ComfyUI-WanSoundTrajectory
  - *From: Dream Making*

- **StoryMem repository** (repo)
  - https://github.com/Kevin-thu/StoryMem
  - *From: Karthik*

- **InfCam project** (repo)
  - https://github.com/emjay73/InfCam
  - *From: NC17z*

- **Wan timeline documentation** (resource)
  - https://wanx-troopers.github.io/timeline.html
  - *From: 42hub*

- **SageAttention wheels** (tool)
  - https://github.com/woct0rdho/SageAttention
  - *From: Kijai*

- **Triton and SageAttention installer** (tool)
  - https://github.com/DazzleML/comfyui-triton-and-sageattention-installer
  - *From: NC17z*

- **SCAIL AudioReactive ComfyUI** (repo)
  - https://github.com/ckinpdx/ComfyUI-SCAIL-AudioReactive
  - *From: mmmgigi*

- **Wan NVFP4 model** (model)
  - https://huggingface.co/lightx2v/Wan-NVFP4
  - *From: Zeku*

- **Wan2.1-Turbo-fp8** (model)
  - https://huggingface.co/Aquiles-ai/Wan2.1-Turbo-fp8/tree/main
  - *From: asd*

- **Wan-Alpha v2.0** (model)
  - https://huggingface.co/htdong/Wan-Alpha-v2.0
  - *From: Gleb Tretyak*

- **EgoX project** (project)
  - https://keh0t0.github.io/EgoX/
  - *From: Cubey*

- **EgoX I2V LoRA** (model)
  - https://huggingface.co/DAVIAN-Robotics/EgoX/tree/main
  - *From: DawnII*

- **OmniVCus model** (model)
  - https://huggingface.co/CaiYuanhao/OmniVCus/tree/main
  - *From: JohnDopamine*

- **StoryMem repository** (model)
  - https://huggingface.co/Kevin-thu/StoryMem/tree/main
  - *From: patientx*

- **LongCat Avatar example workflow** (workflow)
  - https://github.com/kijai/ComfyUI-WanVideoWrapper/blob/main/example_workflows/LongCatAvatar_audio_image_to_video_example_01.json
  - *From: 42hub*

- **SVI 2.0 Pro** (repo)
  - https://github.com/vita-epfl/Stable-Video-Infinity/tree/svi_wan22
  - *From: DawnII*

- **FlippinRad Motion Morph LoRA** (model)
  - https://civitai.com/models/2052865/flippinrad-motion-morph
  - *From: 42hub*

- **Morphic Frames to Video LoRA** (model)
  - https://huggingface.co/morphic/Wan2.2-frames-to-video
  - *From: Relven 96gb*

- **Open-OmniVCus** (repo)
  - https://github.com/caiyuanhao1998/Open-OmniVCus
  - *From: JohnDopamine*

- **Wan-NVFP4 speed boost** (model)
  - https://huggingface.co/lightx2v/Wan-NVFP4
  - *From: Zeku*

- **Lightx2v Distill Models** (model)
  - https://huggingface.co/lightx2v/Wan2.2-Distill-Models/tree/main
  - *From: JohnDopamine*

- **Wan NVFP4 boost** (model)
  - https://huggingface.co/lightx2v/Wan-NVFP4
  - *From: Zeku*

- **LightX2V Wan 2.2 LoRAs** (model)
  - https://huggingface.co/lightx2v/Wan2.2-Distill-Loras/tree/main
  - *From: devnullblackcat*

- **Latest Wan 2.2 LightX2V LoRAs** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/tree/main/LoRAs/Wan22_Lightx2v
  - *From: devnullblackcat*

- **HiStream research paper** (research)
  - http://haonanqiu.com/projects/HiStream.html
  - *From: Juampab12*

- **SVI 2.0 Pro model** (model)
  - https://huggingface.co/vita-video-gen/svi-model/tree/main/version-2.0
  - *From: Kijai*

- **New distill LoRAs** (lora)
  - https://huggingface.co/lightx2v/Wan2.2-Distill-Loras/tree/main
  - *From: Kijai*

- **Wan VAE fp32** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/blob/main/Wan2_1_VAE_fp32.safetensors
  - *From: blake37*

- **Open-OmniVCus project** (repo)
  - https://caiyuanhao1998.github.io/project/OmniVCus/
  - *From: cyncratic*

- **FreeLong Spectral Blending node** (tool)
  - https://github.com/shootthesound/comfyUI-LongLook
  - *From: gaben3801*

- **SVI Pro converted LoRAs** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/tree/main/LoRAs/Stable-Video-Infinity/v2.0
  - *From: Kijai*

- **Ultravico Wan 2.2 implementation** (code)
  - https://github.com/maybleMyers/H1111/blob/svipro/wan2_generate_video.py
  - *From: Benjimon*

- **Smooth Mix Wan 2.2 model** (model)
  - https://civitai.com/models/1995784/smooth-mix-wan-22-i2vt2v-14b
  - *From: slmonker(5090D 32GB)*

- **LightX2V LoRAs collection** (model)
  - https://wanx-troopers.github.io/loras/part-01.html
  - *From: 42hub*

- **FlippinRad Motion Morph LoRA** (model)
  - https://civitai.com/models/2052865/flippinrad-motion-morph
  - *From: 42hub*

- **Converted SVI LoRAs** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/tree/main/LoRAs/Stable-Video-Infinity/v2.0
  - *From: Kijai*

- **Wan Alpha 2.0 DoRA converted** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/blob/main/LoRAs/WanAlpha/Wan_Alpha_v2.0_DoRA_2.0_bf16.safetensors
  - *From: Kijai*

- **DITTO stylized VACE fine-tune** (repo)
  - https://github.com/EzioBy/Ditto/blob/main/inference/example_prompts.txt
  - *From: JohnDopamine*

- **InsertAnywhere project** (repo)
  - https://github.com/myyzzzoooo/InsertAnywhere
  - *From: JohnDopamine*

- **Qwen Image Edit 2511 workflow for multi-view generation** (workflow)
  - *From: slmonker(5090D 32GB)*

- **ComfyUI Clip Prompt Splitter node** (tool)
  - https://github.com/elgalardi/comfyui-clip-prompt-splitter
  - *From: David Galardi*

- **Official SVI ComfyUI workflow** (workflow)
  - https://github.com/vita-epfl/Stable-Video-Infinity/tree/svi_wan22/comfyui_workflow
  - *From: Tachyon*

- **Smoothmix model** (model)
  - https://civitai.com/models/1995784/smooth-mix-wan-22-i2vt2v-14b?modelVersionId=2260110
  - *From: LukeG89*

- **SVI Pro native workflow** (workflow)
  - https://discord.com/channels/1076117621407223829/1342763350815277067/1454805653599031358
  - *From: LukeG89*

- **Motion scale control node demo** (tool)
  - https://youtu.be/Zmkn6_vyMN8
  - *From: brbbbq*

- **ComfyUI-LongLook** (node)
  - https://github.com/shootthesound/comfyUI-LongLook
  - *From: Ada*

- **ModelHunter workflow search tool** (tool)
  - https://tr1dae.github.io/ModelHunter/
  - *From: Quality_Control*

- **SVI workflows collection** (workflow)
  - https://wanx-troopers.github.io/svi.html
  - *From: 42hub*

- **HY-Motion 1.0** (model)
  - https://github.com/Tencent-Hunyuan/HY-Motion-1.0
  - *From: NebSH*

- **ComfyUI-PainterI2Vadvanced** (repo)
  - https://github.com/princepainter/ComfyUI-PainterI2Vadvanced
  - *From: LukeG89*

- **SVI examples** (workflow)
  - https://wanx-troopers.github.io/svi.html
  - *From: 42hub*

- **Wan timeline and documentation** (resource)
  - https://wanx-troopers.github.io/
  - *From: 42hub*

- **ComfyUI-MultiPoseToolkit** (repo)
  - https://github.com/Valiant-Cat/ComfyUI-MultiPoseToolkit
  - *From: harrisonwells*

- **ComfyUI-prompt-splitter** (node)
  - https://github.com/elgalardi/comfyui-prompt-splitter
  - *From: David Galardi*

- **SCAIL information and notes** (documentation)
  - https://wanx-troopers.github.io/wan-animates.html#scail
  - *From: 42hub*

- **Uni3C camera control documentation** (documentation)
  - https://wanx-troopers.github.io/control.html#uni3c
  - *From: 42hub*

- **Context Windows documentation** (documentation)
  - https://wanx-troopers.github.io/what-plugs-where/context-windows.html
  - *From: 42hub*

- **Advanced VACE workflow** (workflow)
  - https://wanx-troopers.github.io/wan-t2v-advanced.html#combining-latent-vace-masks-phantom-and-context-windows
  - *From: 42hub*

- **FreeLong workflow without proprietary nodes** (workflow)
  - *From: Ablejones*

- **Civitai status page** (tool)
  - https://status.civitai.com/status/public
  - *From: TK_999*


## Known Limitations

- **SteadyDancer lacks face control and long generation method**
  - Makes it complex to use, not that useful without proper long generation
  - *From: Kijai*

- **SteadyDancer seems mainly made for TikTok dances**
  - Limited use case, requires full weights rather than being modular
  - *From: Kijai*

- **Fun VACE 2.2 requires lot of resources**
  - Resource intensive setup, not many people have tried it yet
  - *From: David Snow*

- **Current upscalers can't do 4K videos reasonably**
  - SeedVR takes forever and crashes, none of the solutions handle 4K well
  - *From: blake37*

- **UltraViCo processes whole video at once**
  - If you want to triple video length, you're looking to triple the VRAM cost. Methods like this do the whole video at once
  - *From: Kijai*

- **UltraViCo loses start image influence on very long videos**
  - At 241 frames with ultravico, it seems to lose the start image influence
  - *From: Kijai*

- **Context stride mostly unusable**
  - Context stride causes terrible stutter because it packs 4 frames into one latent, mostly just not used
  - *From: Kijai*

- **Small subjects in video generation**
  - Very small subjects like tiny birds may not be recognized or animated properly, need to fill more of the frame
  - *From: Juampab12*

- **Fixed mask position prevents movement**
  - When using crop&stitch with masks that stay in same position, it can prevent natural movement animation
  - *From: Juampab12*

- **Quantized diffusion models have error multiplication**
  - Quantization errors can multiply each step, making quality degradation worse than other model types
  - *From: mallardgazellegoosewildcat2*

- **Adversarial training lacks reliability**
  - Has ugly geometry/topology, super chaotic, tends to oscillate rather than converge
  - *From: mallardgazellegoosewildcat2*

- **Distillation reduces variety**
  - Recent paper suggests distilled models have bad variety because their first step is too big, creates deep ruts for common outputs
  - *From: mallardgazellegoosewildcat2*

- **SVI 2.0 only works with I2V models, cannot be combined with T2V VACE**
  - I2V models use extra channels for conditioning while VACE runs extra modules on T2V models, architectures incompatible
  - *From: Kijai*

- **Steadydancer has no face control and whole model was trained unfrozen**
  - Also lacks training for extension/long generation, may not work with other methods due to new weights
  - *From: Kijai*

- **UltraViCo doesn't work well with I2V due to attention calls and block masking limitations**
  - Fails with HuMo audio attention calls and input size restrictions
  - *From: Kijai*

- **Wan 2.2 starts looping after 81 frames**
  - Training limitation causes model to go backwards on generations longer than 81 frames without control signals
  - *From: Kijai*

- **HuMo embeds break after ~30 seconds when using context options**
  - Model breaks completely after approximately 30 seconds with context windows
  - *From: Gleb Tretyak*

- **SVI-Shot outside trained regime causes stutter errors**
  - Using 4 overlap frames (outside the regime that svi was trained for) occasionally results in stutter errors
  - *From: Ablejones*

- **ComfyUI memory management issues**
  - Easy to accidentally trigger reload everything, VRAM management is squiffy
  - *From: mallardgazellegoosewildcat2*

- **SAM3 ComfyUI nodes lack optimization**
  - They work but don't release VRAM quite as well as expected
  - *From: pookyjuice*

- **SVI 2.2 only supports single start frame**
  - Unlike 2.1 which supported multiple start frames
  - *From: Kijai*

- **Perfect looping beyond 81 frames is challenging**
  - Camera shake and jitter become problematic, context windows don't work reliably for many users
  - *From: herpderpleton*

- **VACE extensions degrade after 3-4 generations**
  - Detail loss increases with each generation, practical limit around 200 frames
  - *From: Juan Gea*

- **SVI 2.0 can only carry over 3-5 frames depending on version**
  - v2.0/SVI_Wan2.1 allows 5 frames, v2.0/SVI_Wan2.2 only allows 3, more causes artifacts
  - *From: 42hub*

- **HuMo color shift issues with extensions**
  - Really a HuMo problem because it's not truly an i2v model. Context windows instead of pure overlap extensions do better with this issue
  - *From: Ablejones*

- **Cannot directly use latent space for long video without degradation**
  - Cannot simply take several last latents from previous generation due to WAN's encoding structure where 1st frame is encoded differently
  - *From: 42hub*

- **SVI has bad prompt adherence**
  - Prompt adherence is very bad with the SVI lora, gets flashes between 81 frame intervals sometimes, videos become degraded or heavily blurred after multiple generations
  - *From: xwsswww*

- **570 frames cannot work without context windows**
  - Only works with wan animate embeds when using context window options
  - *From: Kijai*

- **OneToAll Animation missing endless generation**
  - Currently only supports short clips, long generation method not yet implemented
  - *From: Kijai*

- **SVI models hard to break away from reference**
  - Feel muted until you push them to prompting threshold, though new ones are better
  - *From: Ablejones*

- **Wan token limit around 200**
  - Approximately 170-180 words maximum for prompts
  - *From: Zabo*

- **OneToAll turning around still not good**
  - While better at pose retargeting, still struggles with character rotation
  - *From: slmonker(5090D 32GB)*

- **Kung fu motion capture challenges**
  - Large number of motion-blurred frames make kung fu videos challenging
  - *From: slmonker(5090D 32GB)*

- **OneToAll has low motion issue**
  - Model seems to have low motion problems, may need specific settings
  - *From: Kijai*

- **OneToAll burns with long sequences**
  - 613 frames still burns, especially with lightx2v. Quality loss when reducing burning
  - *From: Kijai*

- **Pose aligner fails spectacularly often**
  - Pose alignment frequently fails in OneToAll workflow
  - *From: Kijai*

- **Context windows work worse overall**
  - While they don't degrade, context windows work worse than extension method overall
  - *From: Kijai*

- **WanAnimate is one character only**
  - Current limitation compared to newer models that can handle multiple characters
  - *From: 42hub*

- **Ovi audio quality not great**
  - Audio output from Ovi model is subpar, cannot condition voice/ref voice yet
  - *From: Charlie*

- **WanMove trajectory preview dots misleading**
  - Dot size doesn't indicate accuracy level, just visual representation
  - *From: Kijai*

- **Multiple splines in editor broken**
  - Bug in spline editor when using multiple splines gives wrong frame count
  - *From: Kijai*

- **Fp8 scaled models broken with recent ComfyUI update**
  - Recent quantization update causes issues with fp8 scaled models
  - *From: Kijai*

- **HuMo only does 5 seconds**
  - HuMo limited to 5 second generations, has context window issues
  - *From: Charlie*

- **SVI doesn't work well with very different aspect ratios**
  - Trained at 480×832 horizontal, weak motion/dynamics with vertical aspect ratios especially full-body person
  - *From: xiver2114*

- **HuMo unhappy being used as I2V**
  - Creates transition issues and contrast problems when used improperly
  - *From: Ablejones*

- **SVI limits camera movement**
  - Keeps pushing camera back towards reference image, limiting dynamic camera movement
  - *From: Vardogr*

- **Wan 2.2 has no film version**
  - Only designed for static shots, equivalent of 'shot' version for 2.1
  - *From: DawnII*

- **Lightning loras remove ability to do dark scenes**
  - Make everything bright, particularly with T2V
  - *From: Kijai*

- **SVI suppresses motion quite a bit**
  - When trying with motion, the lora reduces movement significantly
  - *From: Ablejones*

- **HuMo I2V artifacts show up in first 5 frames**
  - Most artifacts appear at beginning of generation
  - *From: Ablejones*

- **Wan Move does weird stuff when pushed too far**
  - Limitations when using extreme parameters
  - *From: ingi // SYSTMS*

- **SCAIL model doesn't work well with face-only input**
  - Needs more body content to function properly, trained for 896x512 resolution
  - *From: Kijai*

- **SVI doesn't work with models it wasn't trained for**
  - Remains stubborn and refuses to cooperate with HuMo
  - *From: 42hub*

- **SVI kills prompts**
  - There has to be a cost of pushing the length
  - *From: Zabo*

- **SCAIL multi-person motion capture not implemented**
  - Multi-person motion capture doesn't seem to be implemented yet
  - *From: slmonker(5090D 32GB)*

- **SCAIL pose detection not fully implemented**
  - None of the pose detection is implemented - just recolored skeleton. Needs 3D libraries for full implementation
  - *From: Kijai*

- **Frame count limitations with background dynamics**
  - If frame count exceeds 81, background dynamics may become unavailable and background might freeze
  - *From: slmonker(5090D 32GB)*

- **NLF research-only license**
  - NLF model has research-only license meaning can't be used officially in commercial capacity
  - *From: Kijai*

- **SCAIL only supports full or half pose resolution**
  - Currently only full or half size pose inputs are supported
  - *From: Kijai*

- **VACE can only use single reference image**
  - The model can only use one reference image, multiple images get concatenated but model limitation remains
  - *From: Kijai*

- **WanMove can't be used simultaneously with VACE**
  - Incompatible control systems
  - *From: Dream Making*

- **Pose retargeting works poorly unless driving pose and reference pose are same**
  - Feature exists in WanAnimate preprocessor but limited effectiveness
  - *From: Kijai*

- **Multi-person SCAIL doesn't have automatic pose alignment**
  - No align code in original multi-people pipeline
  - *From: Kijai*

- **ComfyUI-RMBG nodes break multiple other functionalities**
  - Globally override torch functions affecting NLF and other models
  - *From: Kijai*

- **SCAIL multi-person detection not fully complete**
  - DWPose connection causes issues, feature still in development
  - *From: Kijai*

- **NLF pose predictor only works for humans**
  - Cannot detect skeletons for animals or non-human subjects
  - *From: Kijai*

- **SCAIL has hand drifting issues in retargeting**
  - Hands scale and drift, especially at distance from center
  - *From: Gleb Tretyak*

- **Kandinsky 24fps makes it much slower**
  - Higher frame rate impacts generation speed significantly
  - *From: Kijai*

- **SCAIL only works with human or human-like poses**
  - NLF requires human-like poses for 3D capture, animals would need other methods like MocapAnything
  - *From: teal024*

- **Wan 2.6 is cloud-only**
  - New 50B model only available on Alibaba Cloud, not for local use
  - *From: ZeusZeus (RTX 4090)*

- **Context window causes inconsistencies**
  - Using context windows for long videos can make results inconsistent at transition points
  - *From: Kijai*

- **Resolution stretching at high resolutions**
  - Going bigger than 1080p can cause limb stretching, especially noticeable in 9:16 generations
  - *From: ingi // SYSTMS*

- **SCAIL missing facial performance replication**
  - Retains ID better than WanAnimate but lacks facial performance replication
  - *From: A.I.Warper*

- **NLF prediction CUDA-only**
  - Hardcoded to use CUDA, won't work with CPU or ROCm without rebuilding repos
  - *From: Kijai*

- **Lightning LoRAs reduce motion variety**
  - Give better detail quality but less motion/structure variety due to distillation process
  - *From: spacepxl*

- **Wan 2.6 not open source**
  - Makes it a dead end for many users, can't modify fps or other parameters
  - *From: Ruairi Robinson*

- **DEIS sampler instability**
  - Throws errors during generation, other samplers work fine
  - *From: Dream Making*

- **WanVideoSampler resolution restrictions**
  - Won't do standard TikTok or other common resolutions
  - *From: Mazrael.Shib*

- **Wan 2.6 heavily censored**
  - Omega ultra super duper censored, rejects basic action words, aimed at stopping all conflict
  - *From: Zabo*

- **SCAIL multi-person tracking broken**
  - Can't properly handle multiple people without masking, hands/face jump between people
  - *From: Kijai*

- **SCAIL only works with pose control**
  - Cannot use depth maps, only trained for pose skeleton control
  - *From: Kijai*

- **Wan 2.2 motion consistency issues**
  - Makes things too fast or more frequently too slow, doesn't understand basic motion properly
  - *From: David Snow*

- **Patch size 32 models not good yet**
  - Current models with patch size 32 like Wan 5B, LTX models, Sana aren't optimal
  - *From: spacepxl*

- **SCAIL context windows don't work well with moving cameras**
  - Causes background shift and inconsistencies
  - *From: Kijai*

- **Vitpose only detects one person**
  - Cannot handle multiple people in pose detection
  - *From: Kijai*

- **SCAIL doesn't support separate first frame input**
  - Reference image is the start frame, cannot provide different starting frame
  - *From: Kijai*

- **Wan 2.5+ will remain closed source**
  - Despite team wanting to open source, external forces prevent it
  - *From: slmonker(5090D 32GB)*

- **SCAIL has issues with close-up face detection**
  - Compared to WanAnimate, SCAIL struggles with facial close-ups and pose detection
  - *From: xwsswww*

- **No proper strength control in WanVideoWrapper**
  - Only has latent multiplier, doesn't work as well as expected
  - *From: Kijai*

- **Context windowing causes background drift**
  - Long generations suffer from background changes due to reference image limitations
  - *From: Kijai*

- **SCAIL struggles with non-humanoid shapes**
  - Triangle with arms and head shape not detected properly by pose estimation
  - *From: amli*

- **Wan 2.1 doesn't work well with First-Last-Frame**
  - Only 2.2 works properly with FLF, 2.1 support exists but quality is poor
  - *From: Kijai*

- **SCAIL has context window problem with long generations**
  - Background not stable enough for long gen, WanAnimate more stable for long gens
  - *From: Juan Gea*

- **SCAIL cannot do faces very well**
  - Faces are a weak point compared to other models
  - *From: AIGambino*

- **Wan 2.2 low denoise causes ComfyUI crashes with too many frames**
  - Too slow and unstable for long sequences
  - *From: NodeMancer*

- **1.3B tile LoRA adds color shift/flashing around 3 second mark**
  - Makes it unusable despite adding significant detail and good 720p to 1080p upscaling
  - *From: David Snow*

- **No controlnets available for Wan 2.2 I2V**
  - No LoRAs, modules, or anything for pose control specifically for 2.2 I2V model
  - *From: Gleb Tretyak*

- **Wan 2.1 and 2.2 limited to 81 frames maximum**
  - 16fps in their best quality 14B versions, longer videos remain an open problem
  - *From: 42hub*

- **Context windows problematic for I2V**
  - Initial frame gets screwed up as window moves, making I2V with context windows not feasible
  - *From: 42hub*

- **LongCat Avatar very slow without distill**
  - Single window takes 10 minutes with 20 steps, also runs at 16fps which looks weird for lipsync
  - *From: Kijai*

- **SVI kills movement and prompt adherence**
  - Trade-off for video stability - reduces dynamic movement and prompt following
  - *From: Zabo*

- **WanAnimate model limitation with detailed masks**
  - Too detailed masks completely break down the model
  - *From: Kijai*

- **Animal pose not compatible with SCAIL retargeter**
  - Cannot directly use animal pose nodes with SCAIL's pose retargeting system
  - *From: Kijai*

- **Latent masking limited with Wan 2.2**
  - 4x compression means one mask per 4 frames when using latent masking
  - *From: Kijai*

- **SCAIL does not support inpainting with mask**
  - Unlike WanAnimate, SCAIL cannot do masked inpainting
  - *From: xwsswww*

- **FlashPortrait not useful for short generations**
  - Seems made for long generation method only, worse than FantasyPortrait for single short clips
  - *From: Kijai*

- **SCAIL struggles with exaggerated character proportions**
  - While SCAIL works well generally, it fails to reconfigure characters with super exaggerated proportions
  - *From: amli*

- **First frame quality issues with reference models**
  - Noisy first frame/flash occurs at boundary between provided first frame and subsequent generated frames
  - *From: Gleb Tretyak*

- **LongCat Avatar doesn't support Wan LoRAs**
  - It's not a Wan model - based on Wan architecture but trained from scratch, so no Wan-specific models/LoRAs work
  - *From: Kijai*

- **LongCat Avatar degradation after 20 seconds**
  - Even without distill LoRA, degradation occurs after 20 seconds with 40 steps and CFG 3
  - *From: slmonker(5090D 32GB)*

- **No multi-character support in LongCat Avatar**
  - Currently cannot handle multiple characters talking or complex masking scenarios
  - *From: Kijai*

- **South Park style doesn't work well in Ditto**
  - Despite ranking high in training dataset analysis, South Park style fails in practice, possibly due to hard style or censoring
  - *From: JohnDopamine*

- **LongCat-Avatar only works with Chinese wav2vec model**
  - Facebook English model doesn't work because it's trained with the Chinese one
  - *From: Kijai*

- **Face quality degrades with distill LoRA and low steps**
  - Hands become horror show, face goes crazy towards the end
  - *From: Kijai*

- **TeaCache and MagCache don't work with LongCat**
  - Tuned per model so wouldn't work properly, EasyCache is model agnostic
  - *From: Kijai*

- **EgoX limited resolution and frames**
  - Trained on 448x448(ego), 448x784(exo) resolutions and 49 frames only
  - *From: Kijai*

- **Extreme values cause fp16 issues**
  - Values like -8716288.0 to 2375680.0 in ffn output explain why fp16 doesn't work
  - *From: Kijai*

- **Character loses likeness in face area at distance**
  - Main issue noticed when using 3D model animated in Blender - character loses facial likeness in output video when at reasonable distance from camera, while clothes remain consistent
  - *From: xwsswww*

- **LongCat Avatar doesn't handle absolute silence**
  - Model requires some noise after vocal extraction, can't process completely silent audio
  - *From: Kijai*

- **Wan TTM completely ignores uni3c**
  - User reports that Wan TTM shows very little camera movement and doesn't respond well to uni3c control
  - *From: Dream Making*

- **StoryMem quality deflation**
  - Looking at more examples shows the quality isn't as impressive as initial previews suggested
  - *From: Cubey*

- **WAN models are too slow animation-wise**
  - Common problem with wan models regarding animation speed
  - *From: David Snow*

- **SCAIL cannot combine with depth control**
  - Chicken and egg problem - can't have depth without already having character moving, and no way to use SCAIL with depth control
  - *From: Kijai*

- **Wan-Alpha v2.0 not working in ComfyUI**
  - Attempts to implement in ComfyUI unsuccessful, model loads but doesn't do anything
  - *From: Gleb Tretyak*

- **LongCat Avatar degrades after 3 extensions**
  - Lip-sync gives up and image becomes wonky after multiple time extensions
  - *From: NC17z*

- **OmniVCus is VACE module**
  - Loads without issues but doesn't do anything as is, needs new code to function properly
  - *From: Kijai*

- **SCAIL doesn't work well with partial body videos**
  - Needs full body for pose to work properly, struggles with hip-up or bust-up videos
  - *From: Hot Hams, the God of Meats*

- **Enhance-A-Video has memory issues with compile**
  - Can cause higher than expected memory usage when enabled
  - *From: Kijai*

- **Can't avoid fade with overlap in windowed context**
  - Transitions between different prompts will always have fade effect due to overlap
  - *From: Kijai*

- **Turbodiffusion speed limited to that model itself**
  - Potentially twice as fast as lightx2v + sageattn but only works with specific model
  - *From: Kijai*

- **SageAttention 3 causes visible proportion distortion**
  - Tested on Wan 2.2 T2V - pilot's head bigger than helicopter cockpit
  - *From: slmonker*

- **VACE doesn't work properly with I2V models**
  - Even when forced, it ruins the output
  - *From: Kijai*

- **T2V methods don't work well with WanAnimate**
  - WanAnimate is I2V based so T2V methods like Stand-in are incompatible
  - *From: Kijai*

- **3090 insufficient for large LoRA training**
  - 1k videos at 121 frames likely won't work on 3090
  - *From: CJ*

- **SVI Pro degrades with major scene changes**
  - Original anchor frame becomes less relevant when scene changes significantly
  - *From: Kijai*

- **Apple Silicon compatibility poor for video models**
  - Most video models except HV 1.5 AIO and WAN 2.2 AIO take too long or have device errors
  - *From: buggz*

- **UltraVico doesn't work well with I2V**
  - Loses reference/start image effect after normal length, changes characters unexpectedly
  - *From: Kijai*

- **fp8 quality issues with Kandinsky**
  - fp8 weights perform poorly with Kandinsky model
  - *From: Benjimon*

- **SVI Pro has difficulty with prompt adherence**
  - Hard time following simple prompts compared to regular generation
  - *From: Kijai*

- **SVI Pro designed to stay close to start image**
  - Wouldn't work well if it moved away from initial reference, by design
  - *From: Kijai*

- **Cannot combine T2V and I2V in same workflow**
  - Different channel dimensions in latent information cause crashes
  - *From: DawnII*

- **FreeLong implementation issues**
  - Hard coded to 81 frame latents, doesn't work for longer generations
  - *From: Ablejones*

- **Character sheet degrades over time**
  - When using character sheets with SVI Pro, quality degrades in extended sequences
  - *From: VRGameDevGirl84(RTX 5090)*

- **SVI degradation after 20-30 seconds**
  - Most models degrade too much after 20-30 seconds of generation
  - *From: Kijai*

- **SVI prompt following issues**
  - Prompt following suffers with SVI, especially camera movement prompts due to anchor image fighting the prompt
  - *From: Kijai*

- **Ultravico subject constraint**
  - 0.95 alpha for ultravico doesn't allow subject to leave the frame
  - *From: Kijai*

- **HuMo flash artifacts with SVI**
  - Using HuMo with SVI produces annoying flash artifacts
  - *From: Ablejones*

- **Quality degradation with longer SVI generations**
  - Obvious quality degradation occurs as generation duration increases
  - *From: slmonker(5090D 32GB)*

- **SVI Pro not good at multiple subjects interacting**
  - Very RNG when trying to generate multiple subjects interacting with each other
  - *From: Tachyon*

- **Camera movement causes issues with SVI Pro**
  - Jumps back to original frame when camera moves like zoom-in
  - *From: Cseti*

- **Prompt adherence degrades after 20 seconds**
  - After 20 seconds of extension, prompt following becomes difficult regardless of prompting
  - *From: NebSH*

- **Ultravico has reliability issues**
  - Not convinced on the reliability of ultravico for consistent results
  - *From: Kijai*

- **Motion scale can ruin images at higher values**
  - 1.3 usually completely ruins the image, mainly turning blue or green
  - *From: Cubey*

- **Wan tends towards slow motion**
  - By far its biggest weakness according to users
  - *From: David Snow*

- **SVI 2.0 Pro causes color drift in long videos**
  - Video begins to darken continuously from 10-second mark, progressively worsens
  - *From: BNP4535353*

- **Scaling RoPE leads to unwanted behavior**
  - Often ruins motion as well, never worked great with Wan
  - *From: Kijai*

- **Fun VACE 2.2 struggles with inpainting**
  - Compared to original 2.1 VACE which is better for inpainting
  - *From: Ablejones*

- **SCAIL cannot reproduce facial expressions**
  - Unlike WanAnimate which has this capability
  - *From: 42hub*

- **SCAIL can only generate >81 frames via Context Windows**
  - Not trained with beyond-81-frames capability, leading to background shift issues
  - *From: 42hub*

- **FreeLong massively increases generation time**
  - Makes many extra model calls during generation
  - *From: Ablejones*

- **Action scenes where subject leaves frame cause everything to change**
  - Prompting dynamic scenes with characters exiting frame leads to poor results
  - *From: David Snow*


## Hardware Requirements

- **Fun VACE VRAM usage**
  - VRAM dropped by about 10% after wrapper update, still a RAM/VRAM killer
  - *From: David Snow*

- **Context windows performance**
  - Performance 5x slower without torch compile, 1024x576/105 frames went from 2:05 to over 10 minutes
  - *From: N0NSens*

- **161 frames generation**
  - Works but low pass will OOM if using TTM
  - *From: Cubey*

- **VRAM improvements with wrapper**
  - NVIDIA 30 series cards seeing reduced VRAM usage even without torch compile after PyTorch 2.9.1 upgrade
  - *From: garbus*

- **VRAM for UltraViCo**
  - Triple video length means triple VRAM cost as it processes whole video at once
  - *From: Kijai*

- **4090 block size limitation**
  - Block size 128 isn't supported on 4090 hardware level, need to use 64
  - *From: Kijai*

- **96G VRAM for VACE workflows**
  - NodeMancer uses cloud.comfy with 96G VRAM for VACE workflows
  - *From: NodeMancer*

- **First frame memory usage**
  - 1st frame takes up 4x memory compared to rest of frames in Wan VAE
  - *From: Scruffy*

- **VRAM management for 30GB fp16 models**
  - Use Q8 GGUF with distorch model loaders for better control over VRAM/RAM allocation instead of native loader
  - *From: David Snow*

- **4090 VRAM usage**
  - Steadydancer example workflow uses under 10GB VRAM unmodified
  - *From: Kijai*

- **RAM requirements for video generation**
  - 32GB minimum, 64GB preferred, some have 96GB or 128GB due to memory leaks and data swapping
  - *From: 42hub*

- **Block size compatibility**
  - Default 128 block size not supported on 4090 hardware level, needs modification
  - *From: Kijai*

- **81 frames on 5090 taking 15+ minutes**
  - Wan animate with sage attn on 5090 RunPod taking 15 minutes or more for 81 frames generation
  - *From: stas*

- **RAM limitations for longer generations**
  - Running out of standard RAM in latent space for longer video generations
  - *From: topmass*

- **PyTorch 2.9.1+cu130**
  - Required to fix memory leak issues with resize nodes
  - *From: spacepxl*

- **Memory usage with 4K videos**
  - ComfyUI not great with 4K videos in general
  - *From: Kijai*

- **Gen time improvement with torch upgrade**
  - Gen time went from 21 minutes to 13 minutes after updating torch 2.8 cu128 to torch 2.9.1 cu130
  - *From: Persoon*

- **HuMo VRAM requirements**
  - 1280x720 causes OOM, 1024x576 works on unspecified VRAM amount
  - *From: AmirKerr*

- **SVI upscale node memory leak on 16GB**
  - Run once results are good, run again gets blobby and noisy on 5060ti 16GB due to VRAM leak
  - *From: Scruffy*

- **MAGI memory requirements**
  - 4.5B-distill+fp8_quant model with window_size=1 works on GPUs with at least 12GB memory
  - *From: Gleb Tretyak*

- **OneToAll Animation generation time**
  - ~15 minutes on 4090 at 576x1024 with 30 steps, ~2 minutes with LightX2V
  - *From: Kijai*

- **Low-end GPU compatibility**
  - Even Wan 14B is a lot for low-end GPUs, but will work just slower (potentially 1 hour 45 minutes per prompt on 8GB)
  - *From: mallardgazellegoosewildcat2*

- **FP8 E5 support**
  - Only works on 3090+ or with latest triton-windows update, fixed since October
  - *From: Kijai*

- **OneToAll VRAM usage**
  - 832x480x81 frames easily under 12GB VRAM
  - *From: Kijai*

- **Live Avatar real-time requirement**
  - 20 FPS requires 5×H800 GPUs (~$150k) with 4-step sampling
  - *From: David Snow*

- **Memory issues with 81 frames 512x**
  - Hits memory problems even with fp8 model and 30 block swap due to VAE conv3d
  - *From: patientx*

- **OneToAll model size**
  - 37GB model too large for single 5090, fp8 version available at 18GB
  - *From: topmass*

- **VRAM for fp8 models**
  - Fp8 versions significantly reduce VRAM requirements, 18GB vs 37GB for OneToAll
  - *From: Josiah*

- **Wan 2.2 VRAM usage on 5090**
  - Using 98% VRAM and 98% RAM, 65-83GB RAM usage with Q8 models
  - *From: VRGameDevGirl84(RTX 5090)*

- **Wan 2.2 RAM requirements**
  - Need to juggle 2x 27GB models + 10GB text encoder, RAM is bigger issue than VRAM
  - *From: Kijai*

- **5090 + 128GB RAM usage**
  - Some users report 20% RAM usage, others 80%+ - varies significantly by workflow and models used
  - *From: FlipYourBits*

- **128GB RAM for Q8 GGUF**
  - Allows pushing to 97 frames with no OOM or VRAM clearing needed
  - *From: metaphysician*

- **SageAttention performance improvement**
  - 5090 user reports 5-second videos in under 2 minutes, 960x960 fp16 videos in 4 minutes, down from 10-50 minutes
  - *From: ComfyCod3r*

- **4090 performance with offloading**
  - Can create 1280x544 video in about 300 seconds using RAM offloading
  - *From: David Snow*

- **SCAIL RAM usage**
  - RAM use is same as Wan 14B in general
  - *From: Kijai*

- **SCAIL VRAM with context windows**
  - With 20 blocks swapped on 4090: Max allocated 16.862 GB, Max reserved 21.594 GB, but very slow (24 minutes for 6 steps)
  - *From: Kijai*

- **RAM pricing trend**
  - Kingston FURY Beast 64GB (2x32GB) 3200MHz DDR4 was £160, went to £300, now £370 - prices rising rapidly
  - *From: David Snow*

- **fp8 format for different GPUs**
  - e4m3fn for Blackwell architecture, e5m2 for older GPUs like 3090
  - *From: mallardgazellegoosewildcat2*

- **WanMove VRAM usage**
  - Same memory requirements as Wan 2.1 14B I2V model
  - *From: Kijai*

- **RAM vs VRAM impact with merge_loras**
  - Merged loras moved to RAM at end, unmerged just removed - affects transfer times
  - *From: Kijai*

- **LoRA extraction speed improvement**
  - Went from 1 hour to 77 seconds with low_rank algorithm
  - *From: Gleb Tretyak*

- **RAM pricing impact**
  - 128GB RAM kit tripled in price over few months, affecting accessibility
  - *From: blake37*

- **VRAM usage for SCAIL**
  - 640x1024, 201 frames, 6 steps, fp8_scaled with 20/40 block swap: Max 14.597 GB allocated, 17.750 GB reserved
  - *From: Kijai*

- **Increased VRAM for pose conditioning**
  - Pose conditioning takes more VRAM than normal generation, may require increased block swap
  - *From: Kijai*

- **NLF warmup time**
  - Takes about 10 seconds for torchscript model warmup
  - *From: Kijai*

- **VRAM usage**
  - 1024*512x81 frames wan 2.2 t2v uses significant VRAM during native ksampler
  - *From: hicho*

- **H100 optimization**
  - Use lightx2v lora, sageattn, fp16 precision, consider torch.compile if out of vram
  - *From: FL13*

- **16GB VRAM capabilities**
  - Can handle higher resolutions with 128GB RAM
  - *From: Gleb Tretyak*

- **SCAIL inference speed**
  - 1h10m for 5s 720p video with high CFG settings
  - *From: Juampab12*

- **SCAIL torchscript warmup**
  - Requires profiling run causing annoying warm-up time
  - *From: Kijai*

- **Sparse attention hardware limits**
  - Custom kernels will probably limit hardware compatibility
  - *From: Kijai*

- **SCAIL generation time**
  - 50 minutes for FastWan with RX 6800, 2 steps
  - *From: patientx*

- **Single 1080p 15sec video**
  - Takes 35-45 minutes to generate
  - *From: slmonker(5090D 32GB)*

- **Cloud GPU pricing**
  - RTX 6000 96GB available around $1.2-1.5/hour on Vast
  - *From: PeacewalkerOTHV*

- **SCAIL VRAM usage**
  - Around 16GB used at default resolution with half blocks swapped on 24GB cards
  - *From: Kijai*

- **Uni3c performance impact**
  - Adds about 1s/iteration at 896x640, 10-20% inference speed hit when offloading
  - *From: Kijai*

- **DF11 performance**
  - 5-20% slower than fp8, faster than bf16, can only be faster if makes model fit VRAM fully
  - *From: Kijai*

- **3090 24GB limitations**
  - Nearly obsolete for current workflows, struggles with SCAIL at higher resolutions
  - *From: TimHannan*

- **VRAM usage with multiple models**
  - Running 3+1 different models in one workflow heavily fills SSD and requires significant VRAM
  - *From: Gleb Tretyak*

- **ComfyUI attention performance on AMD**
  - Quad-cross-attention 3-5x faster than SDP on AMD 6800 with new ROCm libraries
  - *From: patientx*

- **RAM usage increase after ComfyUI update**
  - 96GB RAM no longer sufficient for Wan 2.2 with 5 LoRAs on RTX 6000, requires disabling merge/low mem load
  - *From: Hoernchen*

- **128GB RAM insufficient for complex workflows**
  - User with RTX 6000 and 128GB RAM hitting limits with complex multi-model workflows
  - *From: boorayjenkins*

- **Model quantization speed**
  - Quantizing models takes less than five minutes
  - *From: cyncratic*

- **LongVie compute requirements**
  - Generate 5s video clip takes ~8-9 minutes on a single A100 GPU
  - *From: JohnDopamine*

- **LongCat Avatar VRAM**
  - Requires blockswap even on RTX 5090 due to 31GB model size. Cannot run BF16 without blockswap on consumer hardware
  - *From: burgstall*

- **LongCat Avatar generation time**
  - Every 5 seconds takes about 2:55 on RTX 5090 (12 steps), audio_cfg doubles the time
  - *From: Kijai*

- **LongCat Avatar with blockswap**
  - Works at 960x960x97 frames with blockswap set to 20, VRAM at 99%
  - *From: burgstall*

- **LongCat-Avatar VRAM**
  - 640x352x93fr takes 45 minutes on 16GB VRAM, more about RAM (64GB works)
  - *From: N0NSens*

- **5090 performance**
  - 960x960 took 525.75sec with 20 blockswap, 480x480x141 works, 301 frames took 560sec
  - *From: burgstall*

- **Chunked FFN benefit**
  - Drops peak VRAM by ~2GB without visible speed loss on LongCat
  - *From: Kijai*

- **RAM prices**
  - 128GB DDR5 was £360, now almost £1000; 64GB around €700
  - *From: Charlie*

- **5090 performance with WanMove**
  - 832x480 for 801 frames took 16 minutes to generate, ~25 seconds per 5 seconds at 640x352 with lightx2v
  - *From: Kijai*

- **RTX 3090 LongCat compatibility**
  - Requires specific setup with bf16 base precision, SageAttention 2.2.0, and proper model quantization settings
  - *From: Kijai*

- **4090 Full HD generation capability**
  - Can generate 1920p ultrawide directly, VRAM hit 97% but worked, significantly improved performance on Windows 11 vs Windows 10
  - *From: David Snow*

- **Python version for RTX 3090**
  - Had to downgrade to python 3.12 within windows_portable to have latest Triton for RTX 3090 e4m3fn support
  - *From: NC17z*

- **VRAM for long video decode**
  - 1080p 700 frames causes OOM on decode, 1280x720 works without OOM
  - *From: boorayjenkins*

- **48GB VRAM + 50GB RAM for Wan 2.2 fp16**
  - A6000 setup may work but will be slower than RTX5090, block swap helps but reduces speed
  - *From: 42hub*

- **RTX 5090 performance**
  - 3x faster than RTX 3090 for Wan, RTX 4090 is 2x faster than 3090
  - *From: Benjimon*

- **A6000 performance**
  - Miserably slow, block swap cuts down speed a lot, not recommended for inference
  - *From: MysteryShack*

- **Wan 2.5/2.6 size concerns**
  - Models are probably much larger and may not be useful for consumer hardware
  - *From: Kijai*

- **Some open source models need 96GB VRAM**
  - Making open sourcing less meaningful for most users
  - *From: wallen*

- **Activated parameter count in newer Wan models**
  - Won't be massive - Wan team considered community hardware limitations
  - *From: slmonker*

- **LoRA training VRAM**
  - 32GB VRAM (5090 equivalent) for 1k videos at 121 frames, possibly 24GB with max block swap but slow
  - *From: CJ*

- **SageAttention 2.2 speed improvement**
  - Around 1 second improvement per iteration
  - *From: slmonker*

- **LightX2V generation speed**
  - 17 seconds for 480p video generation
  - *From: slmonker*

- **VRAM optimization in Wan wrapper**
  - 20% VRAM reduction, 1600x896 81f possible with only 1 block offloaded
  - *From: Lumifel*

- **SVI Pro VRAM usage**
  - Same as normal I2V since it's just a LoRA, but second sampler can eat RAM on first run
  - *From: Kijai*

- **TorchCompile overhead**
  - 40 seconds downtime + 20 seconds generation vs 20 seconds without compile for Qwen
  - *From: Mngbg*

- **VRAM for Ultravico extended generation**
  - 1056x1280x161 frames with 21 blocks swapped uses 31.2GB VRAM
  - *From: Benjimon*

- **PCIe bandwidth**
  - PCIe 5.0 x4 should be fine for inference, equivalent to PCIe 3.0 x16, compute bound once models load
  - *From: Benjimon*

- **Power consumption**
  - Can run 3 RTX 5090s at 400 watts each with 1500-1600W PSU
  - *From: Benjimon*

- **Power management**
  - RTX 5090s may need power limiting or undervolting to prevent crashes during generation
  - *From: ingi // SYSTMS*

- **System RAM usage**
  - 96GB system RAM can be exceeded when interpolating multiple scenes (972 frames), needs batching approach
  - *From: Persoon*

- **VRAM for long video generation**
  - RTX 5090 with 32GB VRAM and 96GB system RAM can run long video workflows, 16GB VRAM possible with GGUF models and lower res
  - *From: VRGameDevGirl84(RTX 5090)*

- **Full Wan 2.2 processing time**
  - Takes about an hour on RTX 5090 for full model
  - *From: Benjimon*

- **VRAM for VACE workflows**
  - Can use CPU cache to reduce to just under 24GB
  - *From: Lumifel*

- **Qwen edit VRAM usage**
  - Takes 42GB of VRAM
  - *From: Gateway {Dreaming Computers}*

- **2MP video generation**
  - I2V will fit at 2MP on 24GB but VACE won't
  - *From: Lumifel*


## Community Creations

- **Wan Video Blender node** (node)
  - Node for video blending/transitions, included with Steerable Motion
  - *From: BarleyFarmer*

- **Video transition node** (node)
  - Recently made by Kijai with several transition options, consolidates bunch of nodes into one
  - *From: Kijai*

- **Load VAE (Utils) node** (node)
  - Custom VAE loader utility, though noted issue with incorrect file type
  - *From: spacepxl*

- **Dynamic keyframe insertion node** (node)
  - Takes up to 16 keyframes and dynamically adjusts where they go in image sequence, made with Claude assistance
  - *From: Flipping Sigmas*

- **Video + image frame replacement node** (node)
  - Takes image and video input with frame index parameter, outputs new video with replaced frame
  - *From: BitJuggler*

- **SVI 2.0 ComfyUI integration** (node)
  - Added new input in I2V node for padding with given image and single temporal mask support
  - *From: Kijai*

- **Key renaming script for SVI LoRA conversion** (script)
  - Convert SVI LoRA keys from 'pipe.dit.' to 'diffusion_model.' format
  - *From: Kijai*

- **NormalizeVideoLatentStart** (node)
  - Adaptive mean/std normalization from Kandinsky5 now available as core ComfyUI node
  - *From: Kijai*

- **Latent Color Match node** (node)
  - Color matching in latent space for style transfer
  - *From: Gleb Tretyak*

- **mask_channels_preview** (tool)
  - Shows different views of mask data - pixel frames and latent space representation
  - *From: 42hub*

- **WanVideoWrapper SVI support** (node)
  - SVI 2.0 support in Kijai's wrapper, tested with 2.1, 2.2 support pending
  - *From: Kijai*

- **TrentNodes** (node)
  - Includes cross dissolve functionality for video stitching
  - *From: 42hub*

- **WanEx_I2VCustomEmbeds** (node)
  - Custom embeds node that gives full control over conditioning, helps use embeds like start frame
  - *From: Ablejones*

- **OneToAllAnimation pose alignment node** (node)
  - Uses same detection as WanAnimate preprocessor, doesn't do mad limb stretching, useful for other models too
  - *From: Kijai*

- **Reference frame strength modification tool** (tool)
  - Useful tool for modifying the strength of reference frames
  - *From: Ablejones*

- **WanVideoWrapper** (node)
  - Wrapper implementation for Wan models in ComfyUI
  - *From: Kijai*

- **OneToAll Animation implementation** (model)
  - ComfyUI implementation of pose retargeting with better alignment
  - *From: Kijai*

- **WanAnimate preprocessing improvements** (node)
  - Updated preprocessing with auto match capabilities
  - *From: Kijai*

- **RCM conversion script** (tool)
  - Script to convert RCM models with proper patch embed reshaping
  - *From: Kijai*

- **Manim ComfyUI node prototype** (node)
  - Claude-built prototype for openpose->manim->comfyui workflow
  - *From: Scruffy*

- **WanVideoWrapper OneToAll branch** (node)
  - ComfyUI implementation of OneToAll animation, now merged to main
  - *From: Kijai*

- **WanMove native node** (node)
  - Native ComfyUI node for WanMove with same inputs as ATI
  - *From: Kijai*

- **rCM LoRA conversions** (lora)
  - Converted rCM models to LoRA format for both high and low noise
  - *From: Kijai*

- **HuMo scene extension node** (node)
  - Node to handle extending HuMo scenes with audio concatenation like frame overlap
  - *From: Chandler ✨ 🎈*

- **WanVideoWrapper native WanMove support** (node)
  - Native ComfyUI implementation with Tracks data type for trajectory control
  - *From: Kijai*

- **Dynamic Lora Scheduler** (node)
  - Automated lora strength changes while rendering based on noise or motion
  - *From: Léon*

- **Fake point cloud node from depth image** (node)
  - Creates fake point cloud from depth image, allows rotation and coord_point string export
  - *From: ingi // SYSTMS*

- **3D pose lifting nodes with Manim** (node)
  - Lifts 2D poses to 3D and allows camera movement around poses like Matrix camera
  - *From: Scruffy*

- **WanEx I2VCustomEmbeds node with mask feature** (node)
  - Custom embedding node with masking capabilities similar to VACE
  - *From: Ablejones*

- **Audio reactive node with zoom capabilities** (node)
  - Combines with 3D nodes for audio-reactive video generation
  - *From: Chandler ✨ 🎈*

- **WAN Scheduler visualization node** (node)
  - Visualizes sigma curves to help debug generation issues
  - *From: Kijai*

- **Trent VACE Keyframe Builder** (node)
  - Dynamic keyframe sequencing with drag-and-drop UI, frame positioning, supports up to 256 frames
  - *From: Dream Making*

- **Modified NLF drawing node for SCAIL** (node)
  - Adapted to imitate SCAIL mesh format
  - *From: Kijai*

- **Multikeyframe qwen edit VACE workflow** (workflow)
  - Subgraphed workflows combining qwen image edit with VACE for automated keyframe generation
  - *From: Flipping Sigmas*

- **Auto spacing feature** (tool)
  - Feature to automatically space keyframes to avoid issues when they're too close together
  - *From: Flipping Sigmas*

- **V2 WanVideo nodes** (node)
  - Redesigned modular node architecture with separate components for cleaner workflows
  - *From: Kijai*

- **GetTrackRange node** (node)
  - Splits spline paths across multiple context windows in KJNodes
  - *From: Kijai*

- **Simple track generator** (node)
  - Core node for generating simple bezier tracks and paths
  - *From: Kijai*

- **Path filters concept** (node)
  - Proposed node for adding noise, sine wave effects to movement paths
  - *From: Kijai*

- **SCAIL-Pose detection** (node)
  - 3D pose detection with single and multi-person support, face tracking
  - *From: Kijai*

- **ComfyUI SCAIL Pose** (node)
  - Multi-person pose detection node for SCAIL
  - *From: Kijai*

- **WanVideoWrapper SCAIL branch** (node)
  - SCAIL integration for Wan video generation
  - *From: Kijai*

- **SCAIL-Pose Node** (node)
  - ComfyUI node for SCAIL pose control with NLF 3D pose detection and optional face/hand control
  - *From: Kijai*

- **CUDA memory history nodes** (node)
  - Nodes for tracking and graphing CUDA memory usage during generation, helpful for debugging memory issues
  - *From: Kijai*

- **SAT to Wan format converter** (tool)
  - Code to convert SAT format models to original Wan format by renaming keys and unfusing qkv and kv
  - *From: Kijai*

- **WanViTPoseRetargeter** (node)
  - Helps with migrating skeleton proportions to input
  - *From: dj47*

- **Pose color mapping** (code)
  - Custom color definitions for pose visualization with warm colors for right side, cool colors for left side
  - *From: Kijai*

- **Procedural audio-driven SCAIL poses** (workflow)
  - Generating poses procedurally from audio but hard to teach math to dance right
  - *From: Chandler ✨ 🎈*

- **SCAIL pose filtering** (node)
  - Low-effort filter to align detected pose frames based on proximity of joints for multi-person tracking
  - *From: Kijai*

- **ComfyUI node naming optimization** (node)
  - PR for shorter node names since ComfyUI charges by the letter now (joke)
  - *From: Kytra*

- **SCAIL dwpose compatibility node** (node)
  - Converts dwpose output to be compatible with SCAIL
  - *From: Kijai*

- **SCAIL prompt generation script** (tool)
  - Uses Google Gemini to generate detailed prompts from reference image and driving motion
  - *From: teal024*

- **Multi-person SCAIL workflow** (workflow)
  - Updated workflow for handling multiple people with dwpose conversion
  - *From: slmonker(5090D 32GB)*

- **SCAIL + WanAnimate combination workflow** (workflow)
  - Professional pipeline using SCAIL for retarget then WanAnimate for stability
  - *From: Juan Gea*

- **Uni3c speed optimization** (tool)
  - Added offloading disable option and fp8 quantization support
  - *From: Kijai*

- **Wan Move LoRA** (lora)
  - Camera movement control LoRA extracted from WanAnimate, works with Wan 2.2 but not 2.1 or SCAIL
  - *From: Gleb Tretyak*

- **Split tile upscale workflow** (workflow)
  - 1.3B tile + 2.2 low noise combination for clean upscaling results
  - *From: spacepxl*

- **Hand scaling fix** (bugfix)
  - Fixed hand scaling from upstream and DWPose hand swapping bug
  - *From: Kijai*

- **LongCat Avatar implementation** (node)
  - Working on ComfyUI implementation but extension not working yet and very slow without distill
  - *From: Kijai*

- **WorldCanvas analysis** (research)
  - Identified as 2.2-based model with 53 input channels and VACE-like features
  - *From: Kijai*

- **Model decomposition scripts** (tool)
  - Building pyside-based tool to edit DiT blocks, strip and replace blocks from models
  - *From: cyncratic*

- **Tinker app for model viewing** (tool)
  - App to select any block and save at any dtype, rename keys, view safetensors files
  - *From: Kijai*

- **Fake 32-bit nodes for VACE video** (node)
  - Nodes with antigravity for sequence output implemented using VACE for video workflow
  - *From: yukass*

- **Loop decode node** (node)
  - New node for creating looping videos with native context windows, can work with wrapper outputs using rescale node
  - *From: Kijai*

- **Video slice node** (node)
  - Helps slice correct part of input video for each window in V2V workflows
  - *From: Kijai*

- **Face masking refinement node** (node)
  - Takes SEGS batch masks and swaps them for fixed size squares for consistent face tracking
  - *From: boorayjenkins*

- **ComfyUI-SCAIL-AudioReactive** (node)
  - Generate audio-reactive SCAIL pose sequences for character animation without requiring input video tracking
  - *From: Dream Making*

- **ComfyUI-WanSoundTrajectory** (node)
  - Takes path from SplineEditor and modulates it based on audio analysis for camera/object movement that reacts to music
  - *From: Dream Making*

- **3D preview node for NLF poses** (node)
  - Node for previewing NLF poses in 3D, though struggles with MoGE output
  - *From: Kijai*

- **Torch method NLF pose rendering** (tool)
  - LLM generated but functional torch method for rendering NLF poses, making taichi optional
  - *From: Kijai*

- **CropAndStitch context mask node** (node)
  - Does math to draw consistently sized box around segments for CropAndStitch context mask
  - *From: boorayjenkins*

- **Enhanced caching nodes** (node)
  - Expanded Cache Node and Load Cache from WAS Node Suite, added caching for stitcher data and masks
  - *From: boorayjenkins*

- **WanEx I2V implementation** (workflow)
  - Enables I2V behavior through backend model code when WanEx is installed
  - *From: Ablejones*

- **OpenPose to tracks conversion node** (node)
  - Converts openpose points into tracks, created by Gleb Tretyak
  - *From: Gleb Tretyak*

- **Native QwenVL 2.5 implementation** (node)
  - Work in progress native implementation by Kijai
  - *From: Kijai*

- **h1111 project** (tool)
  - Personal implementation for Wan workflows, includes SVI Pro branch
  - *From: Benjimon*

- **SVI 2.0 Pro workflow** (workflow)
  - ComfyUI workflow for seamless video extension without decode-encode steps
  - *From: Kijai*

- **WanVideo wrapper v2 optimizations** (node)
  - Major VRAM usage improvements and torch.compile fixes
  - *From: Kijai*

- **Native SVI Pro node** (node)
  - WanImageToVideoSVIPro node in KJNodes with converted LoRAs support
  - *From: Kijai*

- **FreeLong++ Wan implementation** (node)
  - Fork of WanVideoWrapper with algorithm for up to 640 frames in one batch
  - *From: campeonchik*

- **Ultravico Wan 2.2 implementation** (code)
  - Custom implementation of Ultravico technique for Wan 2.2 I2V
  - *From: Benjimon*

- **Full auto infinite SVI Pro workflow** (workflow)
  - Automated workflow for infinite video generation with loop capabilities
  - *From: Vérole*

- **SVI Pro subgraph workflow** (workflow)
  - Cleaner native example workflow using subgraphs for better organization
  - *From: Kijai*

- **SVI loop workflow with subnet** (workflow)
  - Builds in simple loop subnet for multiple SVI passes with different prompts
  - *From: Quality_Control*

- **ComfyUI Clip Prompt Splitter** (node)
  - CLIP text encoder that splits prompts based on 'Enter' for multiple prompt handling
  - *From: David Galardi*

- **Image concatenate node patch** (node)
  - Fixes first loop iteration issues in SVI workflows
  - *From: pagan*

- **WanMotionScale node** (node)
  - Motion control without shift options, essentially rope scale adjustment
  - *From: Kijai*

- **Motion scale control custom node** (node)
  - Gives ability to control scale of motion in video generation
  - *From: brbbbq*

- **ModelHunter** (tool)
  - Auto-search shortcut that extracts model names from workflows and creates Google searches
  - *From: Quality_Control*

- **ComfyUI-prompt-splitter** (node)
  - Separates prompts by line breaks so you can put them all in a single text box
  - *From: David Galardi*

- **WanExperiments nodes** (node)
  - Includes HuMo I2V functionality in under 80 lines of code
  - *From: Ablejones*

- **Longvie2** (model)
  - Can do 30 seconds at least with depth/spatracker control, available in test branch
  - *From: Kijai*
