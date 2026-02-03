# Wan Comfyui Knowledge Base
*Extracted from Discord discussions: 2025-09-23 to 2026-02-03*


## Technical Discoveries

- **New torch RMSnorm function changes results slightly and improves speed**
  - Available in PyTorch nightly, clearly faster without torch.compile, barely noticeable with compile
  - *From: Kijai*

- **Kontext workflow useful for characters with different proportions**
  - Works well when reference character has different proportions than driving pose, like smaller characters
  - *From: Kijai*

- **DWPose adds to noise before model pass in UniAnimate**
  - The pose information is injected into noise rather than replacing first frame
  - *From: Kijai*

- **WanAnimate extends automatically with sliding window**
  - Uses 1 frame overlap, processes in chunks like Frames 0-77, then 76-153, then 152-229
  - *From: Kijai*

- **Mask grow node updated to use GPU**
  - Previously slow CPU-based growing is now GPU accelerated
  - *From: Kijai*

- **VitPose retargeting works better than DWPose for character scaling**
  - Good for height/body differences, though doesn't perfectly resize leg height proportions
  - *From: SpacelessTuna*

- **Hand pose detection can be disabled for better results**
  - Set hand_stick_width to -1 to disable hand detection in VitPose
  - *From: Kijai*

- **Using RGB input instead of pose for WanAnimate works well, especially for scenes with foreground elements causing pose jitter**
  - RGB loses likeness slightly more but handles problematic scenes better
  - *From: Hashu*

- **WanAnimate as a model follows reference really well when mask and bg image are disconnected**
  - Pretty much 1-1 with reference, even picks up light watermarks. Adding bg and mask causes likeness to fall apart
  - *From: Hashu*

- **Anisora V3.2 has new prompt structure with quality and motion scores**
  - aesthetic score: X.X. motion score: X.X. There is no text in the video.
  - *From: DawnII*

- **12 fps works better for consistency than 24 fps with WanAnimate**
  - 24 fps had awkward cuts and pose failures, 12 fps better consistency but worse image quality
  - *From: Kijai*

- **Higher noise lightx2v model strength affects motion - lower strength = more motion, higher strength = less motion**
  - Changing strength of high noise lightx2v model changes motion in the picture
  - *From: CHUCK*

- **CFG=2 dramatically improves face similarity but can cause overfitting**
  - Face similarity improved dramatically but overall picture seems overfitted
  - *From: piscesbody*

- **VACE wrapper now works with differential diffusion using latent masks**
  - In wrapper adding latent mask enables differential diffusion, and native workflows can enable it with the node normally
  - *From: Kijai*

- **Anisora v3.2 has distillation baked in**
  - 8 step inference works, can run with 3+4 steps at cfg 1 without distillation loras
  - *From: DawnII*

- **HuMo can work as I2V model while retaining audio matching/lip syncing**
  - Modified model code to allow i2v latent input instead of overwriting with empty one, enables true I2V with audio conditioning
  - *From: Ablejones*

- **FP8 models load much faster in wrapper vs native**
  - FP8 model takes 1 second to load in wrapper while native takes 10 seconds
  - *From: hicho*

- **SageAttention negatively impacts HuMo audio tracking**
  - Visible degradation in lip sync quality when SageAttention is enabled
  - *From: Ablejones*

- **denoise_strength is roundabout way to set start_step with add_noise_to_samples=True**
  - Denoise 0.5 moves start_at_step and toggles add_noise_to_samples rather than acting like a mask
  - *From: 42hub*

- **Lynx works with VACE**
  - Lynx lite version successfully works with VACE for face ID control
  - *From: Kijai*

- **WanAnimate requires inverted canny**
  - Unlike regular canny edge detection, WanAnimate works better with inverted canny (white background with black edges)
  - *From: Ablejones*

- **AniSora 3.2 is distilled for cfg 1.0 and 8 steps**
  - AniSora 3.2 uses distillation technique, works at cfg 1.0 with 8 steps, sometimes better prompt adherence than cfg scheduling
  - *From: DawnII*

- **Anisora high noise LoRA extraction works**
  - Successfully extracted high noise LoRA from AniSora 3.2, works as distillation LoRA
  - *From: Kijai*

- **Wan 2.2 5B is 121 frames, not 81**
  - Wan 2.2 5B T2V model supports 121 frames for consistency, unlike other models capped at 81
  - *From: DawnII*

- **Remap mask range helps background blending**
  - Adding remap mask range to mask improves blending into background but makes output look more like source
  - *From: VK (5080 128gb)*

- **WanAnimate original code doesn't use CFG**
  - The original implementation doesn't use classifier-free guidance and uses hardcoded prompt '视频中的人在做动作'
  - *From: Kijai*

- **Chinese vs English negative prompts have significant impact**
  - Chinese negative prompt tokenizes to 126 tokens vs English 99 tokens, and produces dramatically different results even when translated
  - *From: Kijai*

- **Running text embed at fp32 increases prompt following**
  - Setting text embeddings to fp32 precision improves how well the model follows prompts
  - *From: Kijai*

- **720p resolution significantly improves HuMo quality**
  - HuMo performs noticeably better at 720p resolution as mentioned on project page
  - *From: Ablejones*

- **Pose detection and drawing separated in new preprocessor**
  - New node separates pose detection from drawing so you don't have to run detection again when adjusting drawing parameters
  - *From: Kijai*

- **WanAnimate CFG setting in early access vs final code**
  - In early access code they had CFG functionality but it was never used. In final code it's used but CFG is set to 1.0, so it's effectively not used
  - *From: Kijai*

- **Face input masking dependency**
  - If you don't use face input but use masking, you should input black images to the face input to avoid masking artifacts. The masking breaks if face embeds aren't applied at all
  - *From: Kijai*

- **WanAnimate strength scaling effects**
  - At strength 2.0 on Wan 2.2 it's too much. Blocks 0-15 yield nice results but hair can be overexposed. WanAnimate is generally too strong and ruins prompt following and motion
  - *From: Kijai*

- **Block selection flexibility for WanAnimate**
  - Can use partial blocks (0-5, 0-9, 0-15, 15-39, 10-39) with different strengths to control the effect and allow combination with other tools
  - *From: Kijai*

- **Start percentage scheduling for character models**
  - Using start percentage 0.5 with WanAnimate allows better prompt following and motion while still getting likeness. Only needs a few steps to get likeness
  - *From: Hashu*

- **IP adapter weakness in WanAnimate**
  - IP image input does something but is very weak. Setting IP to 0 gets all motion back, setting IP to 1 and ref to 0 loses likeness completely
  - *From: Hashu*

- **KJ loader is faster than native model loading**
  - User complained about native model load speed being slow, found KJ loader significantly faster
  - *From: hicho*

- **HUMO + InfiniteTalk embed mixing improves results**
  - Mixing embeds from both models provides better acting from characters, better prompt adherence, and respects starting frame details more faithfully than either model alone
  - *From: Juan Gea*

- **LightX2V with FastWan LoRA at 2 steps very fast**
  - LightX2V + FastWan at 2 steps executed in 31.49 seconds vs 70.63 seconds for LightX2V alone at 4 steps
  - *From: VRGameDevGirl84(RTX 5090)*

- **Fun VACE 2.2 is better than VACE 2.1**
  - Better in every way from testing, even ignoring the extra High Noise part
  - *From: Ablejones*

- **High noise model has better prompt adherence than low noise model**
  - In prompt about blue rims of car, H model had blue rims but final output after L model was silver rim
  - *From: hicho*

- **HUMO stops talking when provided silence in audio**
  - Unlike the constant mouth movement issue, HUMO respects silent clips
  - *From: Juan Gea*

- **Camera control prompting technique for I2V**
  - For pan right mention 'camera reveals something' or 'camera pans down revealing a white tiled floor' - works for controlling camera movement
  - *From: hicho*

- **Lynx makes WAN models run at 24fps instead of 16fps**
  - Users observed that using Lynx with WAN models changes the frame rate to 24fps, which was originally intended only for the lite version
  - *From: Kijai*

- **LightX2V LoRAs affect motion characteristics**
  - Using LightX2V LoRAs on both models vs only on LOW model produces different motion effects
  - *From: Dream Making*

- **Lynx reference strength needs careful tuning**
  - At 0.6 strength works well, 1.0+ is too strong and creates 'face glued on video' effect, 1.5+ creates nightmare fuel
  - *From: Kijai*

- **Different model combinations produce visual improvements**
  - Using 2.1 as high model + 2.2 low gives content of 2.1 with look of 2.2, acts like unofficial upgrade
  - *From: hicho*

- **OVI model shows better quality than base WAN 5B**
  - Some OVI generations are better than WAN 2.5 480p generations, with better sound/speech quality
  - *From: ZeusZeus*

- **Lynx works with I2V models but with different effects**
  - Lynx + I2V makes generation faster and changes timing, though unclear if doing much else
  - *From: Kijai*

- **Kytra got native ComfyUI implementation working**
  - Implementation supports native comfy lora loading and everything native that can possibly be native without changing base ComfyUI
  - *From: Kytra*

- **OVI video model is essentially 5B model with extra layers**
  - Works even without using the extra layers, shares cross attention when used with audio model
  - *From: Kijai*

- **Audio model can potentially work alone**
  - Question remains whether audio model works independently from video model
  - *From: Kijai*

- **Audio tensor is 1 dimensional with 157 length**
  - Default audio length for 31 latents (121 image frames)
  - *From: Kijai*

- **OVI generates audio automatically**
  - Different usecase from Wan 2.2 Animate + Infinite Talk - OVI generates the audio too rather than lip-syncing
  - *From: Kijai*

- **5 seconds of audio encodes to 156 length**
  - When encoding exactly 5 seconds of audio, it results in length of 156
  - *From: Kijai*

- **Audio addition makes motion more realistic**
  - Audio and video keep each other in check - can't have big sound without big action and vice versa
  - *From: Draken*

- **VAE memory issue is related to pytorch nightly version**
  - Current nightly causes VAE failures, downgrading to 2.8.0 stable fixes it
  - *From: Kijai*

- **Specific torch versions work with Wan VAE**
  - torch==2.9.0.dev20250909+cu128, torchaudio==2.8.0.dev20250912+cu128, torchvision==0.24.0.dev20250905+cu128
  - *From: Kijai*

- **Ovi model works with French language**
  - Not perfect but generates French speech with some accuracy
  - *From: mamad8*

- **SLG affects both video and audio**
  - Audio model is fully Wan model with 1 dimensional latent, both models run simultaneously and share cross attention
  - *From: Kijai*

- **rCM lora shows better prompt following**
  - Bird lands on head or close to it 100% of seeds tested, better than base model
  - *From: Kijai*

- **Context options work better when used only on first high noise steps**
  - Best results using context options for first two high noise steps, then one high noise step without context, and last 3 low noise steps without context
  - *From: Cseti*

- **Clip embeds were never used in WanAnimate code causing huge difference in quality**
  - Minimal effect with distil loras but huge difference when running 20 steps cfg 1.0 like the original
  - *From: Kijai*

- **FlashVSR works as fast upscaler**
  - One-step diffusion-based video super-resolution framework, reaches ~17 FPS at 768×1408 on single A100
  - *From: Kijai*

- **EasyCache with OVI shows little difference from full 50 steps**
  - Pretty safe to use EasyCache for significant speed improvement
  - *From: Kijai*

- **OVI is around 11B model size**
  - Smaller than people think, heaviness comes from original implementation and wrappers not using offloading
  - *From: Kijai*

- **Strength setting added to combat oversharpening in FlashVSR**
  - Setting at 0.8 reduces oversharpening effects
  - *From: Kijai*

- **FlashVSR can upscale from 1280x720 to 2560x1440**
  - Works well at this resolution range
  - *From: Kijai*

- **FlashVSR uses tiny conditional decoder with LR frames as auxiliary inputs**
  - Leverages LR frames in addition to latents for HR reconstruction
  - *From: mamad8*

- **Multi-step FlashVSR workflow using 2 samplers**
  - First sampler: 4 steps, seed 74, start_step 0, end_step 2, add_noise_to_samples true. Second sampler: 4 steps, seed 76, start_step 2, end_step 4, add_noise_to_samples false
  - *From: Mngbg*

- **FlashVSR can do pseudo image upscaling using repeated frames**
  - Video of 5 repeating images from 480x640 to 1536x2048
  - *From: Mngbg*

- **FlashVSR causes slight browning of colors**
  - Noticeable color shift during processing
  - *From: mdkb*

- **torch.compile recompile limit causes OOM errors**
  - When hitting torch._dynamo config.recompile_limit (64), memory usage increases and can cause OOM. Increasing cache size limit can help temporarily
  - *From: Kijai*

- **Faster cancellation commit causes more OOM issues**
  - The faster cancellation feature (commit 3374e900d0f310100ebe54944175a36f287110cb) multiplies recompile count and causes allocation errors faster, even without pressing cancel button
  - *From: BestWind*

- **LightX2V now has native ComfyUI fp8 models**
  - New fp8 models available that don't require LoRA, including wan2.2_i2v_A14b_high_noise_scaled_fp8_e4m3_lightx2v_4step_comfyui.safetensors
  - *From: hicho*

- **Torch 2.9 resolves compile issues**
  - Upgrading to torch 2.9.0+cu130 with updated triton and sageattention fixes previous torch compile problems
  - *From: BestWind*

- **SageAttention torch.compile compatibility added**
  - New sageattn mode allows torch.compile to work with latest SageAttention version, primarily reduces peak VRAM usage by about 1GB (15.749GB -> 14.667GB max allocated)
  - *From: Kijai*

- **Force parameter static shapes toggle can resolve cl.exe compilation errors**
  - Setting 'Force_parameter_static_shape' to false temporarily resolved cl.exe/algorithm header compilation errors, even when set back to true afterwards
  - *From: BestWind*

- **SageAttention 2.2 performance improvement**
  - Upgraded from months-old workflow to latest SageAttention turned 255 second generation into 191 second generation
  - *From: Persoon*

- **Dynamic parameter in torch compile causes cl.exe errors on Windows**
  - Setting Dynamic to true triggers cl.exe lookup and algorithm header file errors. Setting to false resolves the issue.
  - *From: BestWind*

- **MoCha model uses double compute by concatenating original frames along temporal dimension**
  - Memory use similar to 161 frames when generating 81 frames, making it much more resource intensive than standard models
  - *From: Kijai*

- **Safetensors uses memory mapping by default**
  - Weights are loaded only when actually used, not instantly loaded to memory when loading state dict
  - *From: Kijai*

- **Reference latents can be used with I2V for multiple context windows**
  - Context window node was updated to take latents, allowing you to provide starting frames for each context window using VAE to convert series of images into latents
  - *From: blake37*

- **Empty positive prompts work better for character consistency**
  - Leaving positive prompt completely empty improves character likeness, especially for non-human characters. Only exception is cats where adding 'cat' in positive helps
  - *From: Charlie*

- **Background removal improves character likeness**
  - Using RemBG to remove background and replace with white background, then disabling mask input and background input while disabling relight lora significantly improves character consistency
  - *From: Tachyon*

- **LCM scheduler reduces burn with distill LoRAs**
  - When using more steps with distill LoRAs, LCM scheduler prevents overcooked/burned images compared to dpm++_sde
  - *From: Kijai*

- **Wan 2.1 and 2.2 low noise LoRAs work with WAN Animate**
  - Confirmed that LoRAs designed for Wan 2.1 or 2.2 low noise models can be used with Animate workflow
  - *From: Tachyon*

- **Detail enhancer LoRAs add character detail to video**
  - Using detail enhancer LoRAs can improve character details in video output
  - *From: Charlie*

- **Exact same likeness achieved with tiger reference**
  - Tiger in generated video matches exactly the reference image
  - *From: Charlie*

- **Some fp32 layers improve fp8_scaled performance**
  - Running some layers in fp32 seems to make fp8_scaled work better
  - *From: Kijai*

- **SVI LoRA has some effect with VACE but limited**
  - SVI LoRA works with VACE for better consistency but still loops without control past 201 frames, not as effective as with I2V
  - *From: Hashu*

- **Light VAE can be used to speed up VAE processing**
  - Light VAE is faster on high resolution and more frames, especially helpful for low VRAM setups like 2060. Works with wrapper but not native ComfyUI yet. Quality loss but speed gain is significant.
  - *From: hicho*

- **New ComfyUI pinned memory flag speeds up offloading**
  - --fast pinned_memory flag speeds up weight offloading, fixes long durations with 'Using accelerate to load and assign model weights to device' messages
  - *From: JohnDopamine*

- **Wrapper decode node can decode latents from native workflows**
  - Can use wrapper decode node to decode latents from native workflows, enables mixing between implementations
  - *From: Kijai*

- **New RAM pressure cache system implemented in ComfyUI**
  - Cache sensitive to RAM pressure that evicts RAM-expensive nodes when headroom drops below threshold. Measures models and tensors directly for RAM usage with OOM scoring.
  - *From: JohnDopamine*

- **VACE strength can be set per step in wrapper**
  - In wrapper you can set vace strength per step - control, ref, and original frame strength. For 2.2 high: ref strength at 1, depth at 0.3, pose at 0.4
  - *From: JalenBrunson*

- **Empty frame value should be applied (e.g. black if 0 instead of always 0.5 grey) for better control**
  - The empty_frame_value parameter wasn't being applied correctly and was defaulting to 0.5 grey instead of proper values like black (0)
  - *From: Phr00t*

- **Modified control images can slowly bring in raw video for VACE motion pickup**
  - By modifying control images to gradually incorporate raw video content, VACE can pick up motion patterns more effectively
  - *From: Phr00t*

- **High and low models have 2x different generation times**
  - For WAN I2V specifically, high noise model consistently takes 2x longer than low noise model (e.g. 30 sec vs 15 sec per iteration)
  - *From: patientx*

- **GGUF models show opposite performance pattern**
  - With GGUF versions, the performance ratio is reversed compared to regular models
  - *From: cephy*

- **E5M2 models have slow transformer loading issues**
  - E5M2 format takes significantly longer to load transformer compared to E4M3FN and GGUF versions, despite using torch.compile
  - *From: patientx*

- **Character LoRAs make T2V look significantly better**
  - Using character-specific LoRAs improves T2V generation quality noticeably
  - *From: hicho*

- **SVI-shot instead of SVI-film reduces degradation**
  - Change LoRA to svi-shot (kj rank128 version) and set overlap frames to 1
  - *From: Ablejones*

- **Wan 2.2 can generate high quality still images**
  - Set frame number to 1, increase output size, and lower shift to 2 or 3
  - *From: ingi // SYSTMS*

- **HuMo works with image to video conditioning**
  - Model is capable of I2V but implementations don't pass image conditioning. Modification is simple but required
  - *From: Ablejones*

- **Wan models produce 4*n+1 frames in latent space**
  - Each latent frame encodes 4 real frames plus 1 extra. Frame counts should be 49, 53, etc.
  - *From: 42hub*

- **I2V conditioning uses specific latent channels**
  - Channels 1-16 are standard noisy latents, 17-20 are I2V mask, 21-36 are I2V conditioning inputs
  - *From: Ablejones*

- **Gray values should be used for overlapping I2V conditioning latents**
  - All latents that overlap with noise latents should be gray values, not zeros. Only unused bindweave references should be zeros
  - *From: Ablejones*

- **I2V channel color values significantly affect generation**
  - White seems to increase prompt adherence, different grayscale values change video output completely on same seed
  - *From: Gleb Tretyak*

- **HuMo works well at 81 frames for preventing lip sync issues, but can work up to 97 frames consistently**
  - 81 frames is more reliable for preventing slow motion or lip sync issues, though 97 frames still works
  - *From: Ablejones*

- **Flash issues in HuMo may be related to using wrong frame counts**
  - Using 89 frames instead of 81 might cause flash artifacts
  - *From: Gleb Tretyak*

- **Using fp16 models fixes HuMo flash issues**
  - Using Humo fp16 with fp16 VAE fixes flash artifacts vs using scaled fp8 models
  - *From: JohnDopamine*

- **HuMo works much better with gray frames vs not provided frames or first frame copy frames**
  - Gray frames as intermediate frames produce better results with fewer steps (5 vs 12)
  - *From: Gleb Tretyak*

- **Video to video lip sync with HuMo is possible**
  - Can add lip sync to existing videos, also enables face swap with lip sync functionality
  - *From: VRGameDevGirl84(RTX 5090)*

- **Combining Wan 2.2 High Noise with HuMo as second pass creates good results**
  - Using Wan 2.2 for first pass and HuMo for lip sync injection works well
  - *From: VRGameDevGirl84(RTX 5090)*

- **Wan 2.1 FLF model can work as high pass for first-last frame generation**
  - Using FLF model designed for first-last frame instead of normal i2v method can give better results
  - *From: VRGameDevGirl84(RTX 5090)*

- **MagRef works well as High Noise model in multi-pass workflows**
  - Can use MagRef model for first pass in combination workflows
  - *From: VRGameDevGirl84(RTX 5090)*

- **wan2.2_i2v_A14b_low_noise_lora_rank64_lightx2v_4step_1022 as distill model has main impact on reducing HuMo flash issue**
  - Using this specific distill model, combined with mid gray frames after first frame, shift decreased to 4, steps increased to 6, and strong sampler/scheduler (dpmpp_sde_2s/beta57) helps fix flashing
  - *From: Gleb Tretyak*

- **HuMo can be used as a second pass with any first pass model**
  - Can use T2V with VACE as first pass and HuMo as second pass, or use WanAnimate, Magref, or Wan2.1FLF as first pass
  - *From: VRGameDevGirl84(RTX 5090)*

- **HuMo flash issue wasn't caused by HuMo itself but by the sampler**
  - Sampler was duplicating first latent frame and padding at front when frame counts didn't match, pushing real frames forward. Fixed by changing sampler to only pad/trim at end
  - *From: Scruffy*

- **VAE produces grid noise when sampling results in blurry latent data**
  - VAE is trained on normal non-blurry videos, so blurry frames are 'out of domain' and produce horrible results
  - *From: 42hub*

- **VitPose can extract human joints from sketches unlike DWPose**
  - Allows WanAnimate to work with hand-drawn sketches and stick figures as driving source
  - *From: dj47*

- **Wan latent space is compressed by factor of 8 spatially, 4 temporally**
  - Error 'Expected size 128 but got size 80' means 80*8=640 vs 128*8=1024 resolution mismatch
  - *From: Kijai*

- **FlashVSR Triton PTX error on Blackwell GPUs can be fixed with environment variables**
  - Setting TORCH_COMPILE_BACKEND=eager and TRITON_PTXAS_PATH environment variables in ComfyUI startup fixes 'Value sm_121a is not defined for option gpu-name' error
  - *From: Ashtar*

- **Wan 2.2 I2V can do upscaling/refinement without VACE**
  - Using reference image with rough animation (cut-outs of character moving) can generate new video keeping likeness without needing VACE
  - *From: lemuet*

- **VACE inpainting requires baking mask into original video as grey areas**
  - The control video for VACE can't just be the mask - you need to bake the mask into the original video so masked areas appear as grey, then VACE samples those areas
  - *From: Juan Gea*

- **WanVideo mask previews show different frame counts for different embed types**
  - Bindweave embeds show 21 frame latents (17 frames + 4 references), vanilla I2V shows 17 frames matching video length. Masks show 9 frames for Bindweave, 5 for vanilla I2V
  - *From: 42hub*

- **Wan models can do inpainting using latent noise mask without control inputs**
  - Any Wan model supports inpainting with latent noise masks, though it has higher chance of getting weird and works best with fractional denoising
  - *From: Ablejones*

- **Wan video masks in latent space get reshaped to match latent video dimensions**
  - 17 frame video becomes 5 frames in latent space. Masks tensor [17,480,480] becomes [1,4,5,60,60] where 4 channels store masks for each frame
  - *From: Ablejones*

- **Wan 2.2 I2V models don't have img_emb layers**
  - Unlike Wan 2.1 I2V which has img_emb layers, Wan 2.2 I2V models lack these layers so clip vision inputs get ignored
  - *From: Ablejones*

- **HuMo flash issue can be mitigated by separating conditioning**
  - Providing only FF2LF embeds to HN and only HuMo embeds to LN reduces flash, avoiding combined conditioning
  - *From: Gleb Tretyak*

- **Context windows work with native Wan implementation**
  - Non-Wan context windows node with dim==2 works for longer generations, but combining with HuMo conditioning still causes issues at higher frame counts
  - *From: Gleb Tretyak*

- **HuMo native ComfyUI implementation only uses one reference image**
  - The native code truncates reference images to just use the last one in the list, throwing away the rest. Wrapper implementation correctly supports multiple reference images (up to 4 like Phantom)
  - *From: Ablejones*

- **Context windows work in latent space for Wan**
  - 16 length context window = 16 latents, not 16 frames. 81 context is actually 81 * 4 frames. Context windows get disabled if above frame count
  - *From: Kijai*

- **HuMo supports multiple reference images in wrapper**
  - Can use up to 4 reference images with batch loading. Native implementation was incorrectly coded to only use one
  - *From: VRGameDevGirl84*

- **Audio embeds can work with context windows for HuMo**
  - Required modifying context windows to properly handle HuMo audio embedding slicing
  - *From: Ablejones*

- **Wan 2.1 VACE module performs better than Fun VACE 2.2 Low-Noise Module for low-noise sampling**
  - Testing shows 2.1 VACE gives more natural and integrated results on low-noise side
  - *From: Ablejones*

- **2.1 T2V model with extracted A14B LN lora performs even better for low-noise sampling**
  - Combining 2.1 T2V + A14B LN Lora on low-noise side produces superior results
  - *From: Ablejones*

- **Multiple input images work with Wan 2.2 i2v models for overlap**
  - Can feed 5 images in batch to wanimagetovideo node for smooth continuations, use frame counts matching latent requirements (1, 5, 9 frames)
  - *From: Ablejones*

- **Conditioning lines carry all references and embeddings**
  - Don't need Humo latent output, conditioning lines handle references
  - *From: Ablejones*

- **Context windows only apply character references to first window**
  - Character drift occurs because subsequent windows ignore references, needs custom code to align
  - *From: Ablejones*

- **Kijai added PainterI2V motion amplification to WanVideoWrapper**
  - New experimental feature: augment_empty_frames parameter (0.0-10.0) to force more motion by augmenting empty frames with difference to start image
  - *From: JohnDopamine*

- **Wan 2.2 High with HuMo Low combination provides better prompt adherence and motion**
  - T2V with Wan 2.2 as High noise and HuMo as Low noise gives better motion and prompt adherence compared to just HuMo alone
  - *From: VRGameDevGirl84(RTX 5090)*

- **Initial step without LightX LoRA improves motion and character consistency**
  - Using 1-3 steps without speed LoRA at the beginning of sampling helps lock in better motion and character consistency
  - *From: garbus*

- **Audio-reactive WanMove with pose detection works well**
  - Generated sound modulated tracks with pose detection can create dynamic motion effects that sync with audio
  - *From: Chandler ✨ 🎈*

- **Humo works well for maintaining character consistency across different perspectives**
  - HuMo effectively frames the subject in the same scene but from different perspectives
  - *From: Ablejones*

- **Torch 2.9 breaks AudioEncoderEncode node**
  - AudioEncoderEncode fails with NotImplementedError on torch 2.9 due to flash attention compatibility issues with RTX 5090, works with torch 2.8
  - *From: Scruffy*

- **Context windowing works well with specific model types**
  - Models where I2V and T2V are the same model just tuned differently (like Kandinsky, HunyuanVideo1.5) work better with context windowing
  - *From: Kijai*

- **SCAIL can be used with dance moves from AIST dataset**
  - Dataset converted from pkl to npy format and hosted on Huggingface, autodownloads when library is called in nodes
  - *From: Chandler ✨ 🎈*

- **Qwen edit multiple angles lora works well for rotation consistency**
  - Works amazingly for handling subjects that rotate and show different angles in video
  - *From: Ablejones*

- **Custom slicing of context windows is now merged into ComfyUI**
  - Allows using context windows with Vace and Phantom inputs, enables custom conditioning input slicing
  - *From: Ablejones*

- **Multiple character support added to SCAIL audio nodes**
  - Updated dance library with multiple character support in the repo
  - *From: Chandler ✨ 🎈*

- **FBX animations can be converted to openpose**
  - New custom node uses Blender in background to obtain JSON info from FBX files
  - *From: metaphysician*

- **Phantom is best for handling subject rotation**
  - Most effective for cases where subjects rotate extensively showing front and back
  - *From: Ablejones*

- **ONNX model files have 4GB limit requiring separate .onnx and .bin files**
  - Both files must be in same folder and you load the onnx file
  - *From: Kijai*

- **SCAIL requires matching starting pose between reference image and animation**
  - Gorilla starting in standing pose doesn't work well with crouching woman reference video
  - *From: ucren*

- **SCAIL animates your image so starting composition matters**
  - For shots where person runs away, start from full body shot that moves to camera then runs away to have all ref content from first frame
  - *From: ucren*

- **Native nodes more RAM hungry than wrapper nodes**
  - BF16 Wan 2.2 high/low + Humo workflow using 96% of 128GB RAM and 78% of 96GB VRAM
  - *From: ingi // SYSTMS*

- **Block 0 causes unwanted behavior in WanMove LoRA**
  - Setting block 0 to 0.0 makes output much better and more coherent
  - *From: Ablejones*

- **WanMove LoRA works naturally on Wan 2.2 without block modifications**
  - 2.2 just naturally understood the conditioning, but failed on 2.1 models
  - *From: Gleb Tretyak*

- **SVI Pro is a recent totally new trained version of SVI that needs totally different input types**
  - It's for Wan2.2 HN/LN workflow and does frame anchoring of SVI-shot with smooth continuations of SVI-film, fully compatible with Wan2.2 and LightX2V
  - *From: Ablejones*

- **WanMove can be extracted as a LoRA**
  - Testing showed you can extract WanMove as a lora by testing it with Wan2.2
  - *From: Ablejones*

- **Frames in console log are in latent space**
  - The calculation is (41 - 1) / 4 + 1 = 11
  - *From: Ablejones*

- **Motion latent count logic**
  - 1 latent = 4 frames +1, so if you set motion latent count to 2, you need overlap to 9
  - *From: LukeG89*

- **SVI 2.0 Pro was trained with 1 motion latent (4 frames)**
  - Setting to anything else would be wrong
  - *From: 42hub*

- **SCAIL vs LTX 2 trade-offs**
  - SCAIL is better at movements and copying poses from video but worse at facial consistency. LTX 2 is better at face/skin quality and consistent facial expressions but worse at pose copying.
  - *From: Kevin "Literally Who?" Abanto*

- **Skyreels V3 includes InfiniteTalk**
  - When using Skyreels V3 as base model, you don't need to connect the InfiniteTalk model separately as it's already included
  - *From: Kijai*

- **Skyreels works without ref video**
  - Skyreels can function without reference video, though it becomes similar to multitalk without it
  - *From: slmonker(5090D 32GB)*

- **Reference video helps longer generations**
  - Reference video in Skyreels is more meant to help with longer video generations
  - *From: Kijai*


## Troubleshooting & Solutions

- **Problem:** 36 channel error in WanAnimate workflow
  - **Solution:** Update nodes to main branch and check for conflicting installations with same class names
  - *From: Kijai*

- **Problem:** Set node stuck in STRING mode after update
  - **Solution:** Delete old set node and create new one with same name 'pose_images'
  - *From: Kijai*

- **Problem:** Memory errors with high frame count videos
  - **Solution:** VHS and ComfyUI struggle with high frame counts, reduce frame count or use Load Video from Path node
  - *From: Kijai*

- **Problem:** Minutes-long generation times
  - **Solution:** Usually indicates running out of VRAM, monitor with GPUz and restart ComfyUI when VRAM hits 6000MB
  - *From: Kijai*

- **Problem:** Black rectangle artifacts from mask
  - **Solution:** Update to latest commit, ensure mask block size isn't too small, keep face strength at 1.0
  - *From: Kijai*

- **Problem:** Dependency conflicts causing channel errors
  - **Solution:** Use virtual environments, check for conflicting pydantic and numpy versions
  - *From: Josiah*

- **Problem:** FP8 e4m3fn compatibility with RTX 3000/AMD
  - **Solution:** Use fp8_e5m2 quantization instead when using torch.compile
  - *From: patientx*

- **Problem:** Can't use built-in looping of WanAnimate with multiple samplers
  - **Solution:** Deactivate built-in looping by having frame_window_size and num_frames equal, use shorter clips or context windows instead
  - *From: Kijai*

- **Problem:** Error when passing WanAnimate embeds to sampler without WanAnimate model
  - **Solution:** Use normal I2V node on the other sampler instead
  - *From: Kijai*

- **Problem:** Can't set use_non_blocking to true, always hits OOM
  - **Solution:** It's about RAM - bigger vitpose model might push to RAM limit
  - *From: Kijai*

- **Problem:** Denoise strength set to zero still applies denoising
  - **Solution:** Denoise just adjusts start step - use start_step parameter instead for Wan 2.2
  - *From: Kijai*

- **Problem:** WanAnimatePreprocess nodes not loading despite no errors
  - **Solution:** Browser cache issue - restart browser or clear cache
  - *From: Kijai*

- **Problem:** utf-8 codec error with .onnx files
  - **Solution:** Compute SHA256 checksum on .onnx files and compare against huggingface - likely broken file
  - *From: 42hub*

- **Problem:** start_step must be 0 when denoise_strength is used error
  - **Solution:** Set denoise to 1 and increase start_step instead. For 4 total steps, use start step of 2
  - *From: theUnlikely*

- **Problem:** Missing detection folder for preprocessor nodes
  - **Solution:** Create detection folder inside models/ directory: mkdir -p /workspace/ComfyUI/models/detection
  - *From: Léon*

- **Problem:** ComfyUI shows 0 in sampler but field is actually empty
  - **Solution:** Click on the field and manually fill in 0 again
  - *From: Martin_H*

- **Problem:** WanAnimate native workflow shows black image while wrapper works
  - **Solution:** All conditions need to be the same, check model loading and settings
  - *From: xbobos*

- **Problem:** GPU disabling and computer freezing with Wan Animate on RTX 5090
  - **Solution:** Likely power supply issue - Wan Animate has larger blocks so heavier compute load
  - *From: Draken*

- **Problem:** SAM2Segmentation bbox error
  - **Solution:** Use points instead of box input, or rebuild the node if conflicts with other custom nodes
  - *From: mightynice*

- **Problem:** Wrapper not loading in latest ComfyUI
  - **Solution:** Remove xformers from lib folder - it's outdated and causes conflicts
  - *From: hicho*

- **Problem:** UnicodeDecodeError on WanVideoWrapper startup
  - **Solution:** Update the wrapper to latest version to resolve UTF-8 encoding issue
  - *From: Kijai*

- **Problem:** UTF-8 error persists after update
  - **Solution:** Issue acknowledged, user will find own solution
  - *From: piscesbody*

- **Problem:** Weird long hangs after recent update
  - **Solution:** Update everything again and remove unused custom nodes
  - *From: Kijai*

- **Problem:** OOM on 5090 with multiGPU nodes
  - **Solution:** No solution provided, VAE and text encoders successfully offloaded to 3090
  - *From: 𝕯𝖗. 𝕸𝖆𝖈𝖆𝖇𝖗𝖊 ☠*

- **Problem:** Background completely static in WanAnimate
  - **Solution:** Use inverted canny instead of regular canny, prompt for motion like 'driving a car'
  - *From: A.I.Warper*

- **Problem:** Infinitetalk doesn't work with 2.2
  - **Solution:** Connect multitalk only to high model sampler, use normal image embeds for low model, don't connect multitalk model to low sampler
  - *From: hicho*

- **Problem:** Missing mask frames causes reference image mismatch
  - **Solution:** Ensure mask has no gaps across all frames, create continuous mask in After Effects
  - *From: VK (5080 128gb)*

- **Problem:** VAE decode times varying dramatically (10s vs 3 minutes)
  - **Solution:** Check if tiling is activating automatically - terminal might show 'cant decode, using vae tiling'
  - *From: Draken*

- **Problem:** onnxruntime module not found error
  - **Solution:** Need to pip install onnxruntime-gpu in ComfyUI virtual environment, some systems may need specific version like 1.18 for AMD
  - *From: patientx*

- **Problem:** Pose detection running on CPU instead of GPU
  - **Solution:** Install onnxruntime-gpu instead of onnxruntime - installing regular onnxruntime can force CPU usage
  - *From: Kijai*

- **Problem:** Blocks visible in WanAnimate subject replacement
  - **Solution:** Native implementation doesn't send empty pixels when face isn't used - need to ensure face adapter executes or use wrapper implementation
  - *From: Ablejones*

- **Problem:** CFG generations looking worse than distill versions
  - **Solution:** CFG > 1 often produces worse results than distill LoRAs - try simpler prompts or stick with distill approach
  - *From: Tony(5090)*

- **Problem:** Grid noise pattern in WanAnimate results
  - **Solution:** Fixed by using the new v2 fp8 scaled model which works properly in native ComfyUI
  - *From: Kijai*

- **Problem:** SageAttention auto mode doesn't work with WanAnimate on 4090
  - **Solution:** Issue occurs when using clip vision in native. ComfyUI has a workaround that can be activated with command line arg
  - *From: Kijai*

- **Problem:** Black result when torch compiling WanAnimate
  - **Solution:** Related to SageAttention auto mode issue with clip vision
  - *From: Kijai*

- **Problem:** Masking artifacts when not using face input
  - **Solution:** Input black pixels/frames to face input instead of leaving disconnected. In wrapper this is handled automatically, but in native you need to do it manually
  - *From: DawnII*

- **Problem:** Custom sigmas producing black/broken images
  - **Solution:** Never have two sigma values that are the same in the list
  - *From: Ablejones*

- **Problem:** HUMO unwanted mouth movement when no audio
  - **Solution:** Delete line in prompt guider that was part of 'do not quote lyrics line' - this stopped unwanted mouth movements
  - *From: hudson223*

- **Problem:** Wrapper fp8_scaled_fast error with empty LoRA
  - **Solution:** Bug occurs when empty LoRA list is passed, fixed by Kijai checking for empty list vs None
  - *From: pagan*

- **Problem:** OOM on 4090 with 125 frames
  - **Solution:** Drop frame window size from 81 to 41, or use batching approach with last frame carryover
  - *From: humangirltotally*

- **Problem:** Color shift/washout in I2V chain extensions
  - **Solution:** Use VACE with last few frames instead of single frame, crossfade between videos to hide color shifting gradually
  - *From: lemuet*

- **Problem:** WanAnimate face shaking with movement in new workflow
  - **Solution:** Issue identified with new Kijai workflow with preprocessor, didn't happen in old workflow
  - *From: Kevin "Literally Who?" Abanto*

- **Problem:** Wan 2.2 I2V last 10 frames degradation
  - **Solution:** Consistently happening issue visible from high noise model generation, changing samplers/shift didn't work
  - *From: Dever*

- **Problem:** sageattn_varlen doesn't work on AMD
  - **Solution:** Use sdpa with masking (though slow) or flash_attn_varlen alternatives
  - *From: Kijai*

- **Problem:** Lynx shows 'no lynx reference adapter layers found' error
  - **Solution:** Need to use correct base model that includes lynx layers, check example workflow notes
  - *From: DawnII*

- **Problem:** ONNX CUDA error with insightface dependency
  - **Solution:** Missing insightface dependency compilation, needs proper installation
  - *From: pagan*

- **Problem:** WAN 2.2 5B VAE suddenly using much more VRAM
  - **Solution:** Issue appeared after updates, may need tiled decode which takes longer
  - *From: Kijai*

- **Problem:** Video previews not working after ComfyUI update
  - **Solution:** Switch from h265 to h264 codec
  - *From: Janosch Simon*

- **Problem:** Lynx causing instant OOM with previously working settings
  - **Solution:** Use full block swap and reduce resolution (e.g., 320x240 for 121 frames)
  - *From: patientx*

- **Problem:** Video output issues fixed with latent scaling
  - **Solution:** Use latent scaling suggestion
  - *From: Kytra*

- **Problem:** GGUF quantization changing audio tensor shape
  - **Solution:** Added ModelWanAudio class in convert.py with correct keys_detect and keys_hiprec
  - *From: patientx*

- **Problem:** Getting Nans and corrupted results
  - **Solution:** Use bf16 instead of fp16 for base precision - fp16 causes issues with this model
  - *From: Kijai*

- **Problem:** Video going black on last step with fp16_fast
  - **Solution:** Use bf16 base precision - fp16 has issues with this model
  - *From: Kijai*

- **Problem:** Audio sounding like gibberish or thug-like
  - **Solution:** Use SLG (set to 11) and proper CFG values - CFG and SLG matter a lot for audio
  - *From: Kijai*

- **Problem:** Missing OVI nodes in ComfyUI
  - **Solution:** Switch to OVI branch: git fetch --all, git switch ovi, and install missing dependencies
  - *From: Kijai*

- **Problem:** Rendering freezing at final stage
  - **Solution:** Add block swap node for VRAM issues, or try turning OVI CFG up to 5
  - *From: Kijai*

- **Problem:** fp16 precision causes black output
  - **Solution:** Video looks fine until last step then gets NaNs and goes black
  - *From: Kijai*

- **Problem:** Video stops abruptly while audio continues
  - **Solution:** Caused by webm encoding issues, switch to mp4 format
  - *From: JmySff*

- **Problem:** ComfyUI crashes when loading Wan node on ovi branch
  - **Solution:** Install librosa and omegaconf dependencies manually
  - *From: Lumi*

- **Problem:** VACE workflow error 'too many values to unpack'
  - **Solution:** Switch back to main branch or use updated VACE fix
  - *From: yukass*

- **Problem:** OOM on 4090 with OVI
  - **Solution:** Use fp8 models and full block swap (30 blocks), disable torch compile and easycache
  - *From: Stad*

- **Problem:** Lynx error with wrong resampler
  - **Solution:** Use LITE resampler with LITE ip model, not FULL resampler
  - *From: U̷r̷a̷b̷e̷w̷e̷*

- **Problem:** Error 'blocks.0.audio_block.modulation' KeyError
  - **Solution:** Update the wrapper to fix the issue
  - *From: Juan Gea*

- **Problem:** Can't pass CFG list to WanVideo OVI CFG
  - **Solution:** TypeError occurs with audio_cfg_scale calculations, known issue
  - *From: TK_999*

- **Problem:** Getting black output with darker scenes in OVI
  - **Solution:** Try more steps, change prompts, adjust lighting in prompt
  - *From: U̷r̷a̷b̷e̷w̷e̷*

- **Problem:** Image degradation with InfiniteTalk audio_scale above 1.0
  - **Solution:** No clear solution found, artifacts and saturation increase with higher audio_scale
  - *From: blake37*

- **Problem:** Colors drifting in WanAnimate
  - **Solution:** Use context options vs original - context minimizes color drift but causes background morphing
  - *From: Mak*

- **Problem:** UnboundLocalError with LQ_images in FlashVSR
  - **Solution:** Update the wrapper to latest version
  - *From: scf*

- **Problem:** FlashVSR doesn't process all frames
  - **Solution:** 161 frames input resulted in 157 frames output - known issue
  - *From: Dever*

- **Problem:** Strength setting turns to NaN when opening new workflows
  - **Solution:** Have to manually set it to 0 again each time
  - *From: BestWind*

- **Problem:** Getting 'got multiple values for keyword argument is_uncond' error
  - **Solution:** Right click sampler and pick 'Fix Node (recreate)' to fix after sampler modifications
  - *From: JohnDopamine*

- **Problem:** TinyVAE (taew2_1) stopped working after update
  - **Solution:** Fixed by Kijai in latest update
  - *From: art13.beck*

- **Problem:** Mono audio causing 'too many values to unpack' error
  - **Solution:** Fixed unsqueeze issue - audio was being reshaped to 1,1,1,length instead of B,C,L
  - *From: Kijai*

- **Problem:** RAM stays high after generations and doesn't clear
  - **Solution:** Remove upscale model node if present as it doubles image size and creates copies
  - *From: Kijai*

- **Problem:** torch._dynamo hit config.recompile_limit (64) error
  - **Solution:** Increase cache size limit to 128 or higher, clear triton caches, use --reserve-vram 2 flag
  - *From: Kijai*

- **Problem:** Triton cache causing compilation errors
  - **Solution:** Delete triton caches at C:\Users\<username>\AppData\Local\Temp\torchinductor_<username>\triton and C:\Users\<username>\.triton
  - *From: Kijai*

- **Problem:** Black output with new I2V Wan2.2 models
  - **Solution:** Use the ComfyUI-specific version of the model, original version has incorrect format
  - *From: Kijai*

- **Problem:** OOM errors after ComfyUI update
  - **Solution:** Update WanVideoWrapper node with git pull, disable torch compile nodes if needed
  - *From: Ashtar*

- **Problem:** Triton compilation errors on Windows
  - **Solution:** Clear triton cache, check antivirus exceptions, may need to reinstall triton or use different version
  - *From: yukass*

- **Problem:** First run with torch compile uses more VRAM
  - **Solution:** Torch 2.8.0 has this issue, workaround is to run another workflow first or upgrade to 2.9
  - *From: Kijai*

- **Problem:** FlashVSR resize node 'per_batch' input error
  - **Solution:** Right click the node and click 'Fix node (recreate)', then re-enter the values. The per_batch input was experimental and later reverted
  - *From: Ablejones*

- **Problem:** Video dimensions mismatch in VSR sampler
  - **Solution:** Use a node to check what the Load Video node actually loaded and make sure dimensions and number of frames match what the sampler expects
  - *From: Ablejones*

- **Problem:** 27GB LoRA causing OOMs
  - **Solution:** That's actually a full fp16 model categorized as LoRA, should be called a checkpoint instead
  - *From: FL13*

- **Problem:** SageAttention DLL load failed error
  - **Solution:** Delete 'flow match' folder inside custom_nodes, restart ComfyUI. Issue related to incorrect SageAttention and Triton installation
  - *From: David Galardi*

- **Problem:** Workflow errors mentioning ovi and lynx when using Wan
  - **Solution:** Update the wrapper and kjnodes to fix compatibility issues
  - *From: Thom293*

- **Problem:** cl.exe algorithm header compilation errors
  - **Solution:** Toggle 'Force_parameter_static_shape' to false, which can reset the compilation system. May also need proper Visual Studio C++ paths set
  - *From: BestWind*

- **Problem:** SageAttention compile producing noisy output
  - **Solution:** Use regular sage mode instead of sage_compile if getting noisy results
  - *From: scf*

- **Problem:** Cannot open include file: 'algorithm' error on Windows
  - **Solution:** Add INCLUDE system environment variable with path to MSVC include directory or set Dynamic to false in torch compile
  - *From: TK_999*

- **Problem:** Torch compile dynamic mode fails on Windows
  - **Solution:** Set dynamic parameter to false - Windows triton isn't full triton
  - *From: BestWind*

- **Problem:** Memory leak in loops with custom nodes
  - **Solution:** JoyCaption node doesn't unload models properly - check custom nodes for proper memory management
  - *From: Dever*

- **Problem:** VAE torch compile causes rainbow flickering after first run
  - **Solution:** Issue occurs when dragging compile option to VAE, works first time but corrupts subsequent outputs
  - *From: phazei*

- **Problem:** SDPA with torch compile causes crashes
  - **Solution:** Make sure attention is set to sage instead of sdpa when using torch compile
  - *From: phazei*

- **Problem:** WanVideoEncode error 'local variable out referenced before assignment'
  - **Solution:** Issue appears to be related to VAE loading in the loop. Try updating ComfyUI Essential nodes or modifying VAE loader within the loop
  - *From: Juan Gea*

- **Problem:** Mocha error 'view_as_complex only supported for half, float and double tensors, but got BFloat16'
  - **Solution:** Update the wrapper and clear triton cache. Delete C:\Users\<username>\.triton folder
  - *From: Kijai*

- **Problem:** Portrait resolutions failing with OVI
  - **Solution:** Set divisible by to 32 instead of 16. Issue is latent space requirements - something divisible by 2 isn't necessarily divisible by 16
  - *From: Kijai*

- **Problem:** Mocha generating max 5 seconds
  - **Solution:** If using context options, set context frame count to same as frame window count
  - *From: CJ*

- **Problem:** Face appearing despite face_strength set to 0
  - **Solution:** Disable the LoRA entirely and run at 20 steps for correct results without face generation
  - *From: AR*

- **Problem:** Context window transition artifacts in WAN Animation
  - **Solution:** Try different High and Low noise settings in Wan 2.2, or use Magref model for Wan 2.1 workflows as it handles transitions better
  - *From: blake37*

- **Problem:** Face likeness degradation with CFG 3 on low noise
  - **Solution:** Use higher CFG on high noise (3.5-4) and lower on low noise (2.5) to prevent face degradation
  - *From: Lumifel*

- **Problem:** LongCat changes broke other models with head_norm error
  - **Solution:** Kijai pushed a fix for the WanI2VCrossAttention.__init__() unexpected keyword argument 'head_norm' error
  - *From: Kijai*

- **Problem:** Fun InP doesn't support control images
  - **Solution:** Use Fun Control model for control images - Fun InP is only for in-between frames
  - *From: Kijai*

- **Problem:** Hair doesn't fit within driving video mask
  - **Solution:** Expand the mask around head area to accommodate voluminous hair that extends beyond the tight bbox
  - *From: seitanism*

- **Problem:** CUDA OOM errors with latest ComfyUI nightly
  - **Solution:** Turn off non-blocking in block swap node or roll back ComfyUI version. New RAM management changes causing issues.
  - *From: CJ*

- **Problem:** RAM usage peaks much higher and inconsistent
  - **Solution:** Disable non-blocking on block swap node. May need to increase block swap count due to LoRA weights now attached to blocks.
  - *From: lemuet*

- **Problem:** Can't install LightVAE
  - **Solution:** Use with wrapper instead of native ComfyUI - native support coming later
  - *From: hicho*

- **Problem:** Lightning4step LoRA makes everything super bright with fake details
  - **Solution:** Switch to lightx2v LoRA which is more realistic but may need contrast adjustments. Can try mixing both LoRAs or use at 0.25 strength.
  - *From: DaxRedding*

- **Problem:** LightX2V LoRA causes washed out colors and detail loss
  - **Solution:** Use at 0.25 strength to maintain speed without losing quality on low noise. Consider using t2v detailers with very low denoise for retouching.
  - *From: mdkb*

- **Problem:** Second sampler taking 12-15GB more RAM and failing
  - **Solution:** Try using LoRA merging option instead of applying on the fly
  - *From: JohnDopamine*

- **Problem:** GGUF models not being found in checkpoint folder
  - **Solution:** Models need to be moved to diffusion folder instead of checkpoint folder
  - *From: devnullblackcat*

- **Problem:** CUDA OOM issues with recent ComfyUI updates
  - **Solution:** Add --disable-pinned-memory to launch script
  - *From: JohnDopamine*

- **Problem:** Neck and shoulders not showing up in first frames during pose retargeting
  - **Solution:** This is normal behavior from pose estimation, not a bug
  - *From: Draken*

- **Problem:** WAN 2.2 Animate forcing 5-second output when input is shorter
  - **Solution:** The number of frames generated is set by the embed creation node, not input length - it fills missing frames with blanks
  - *From: lemuet*

- **Problem:** Issues with WAN and GGUF models
  - **Solution:** Try --disable-pinned-memory argument
  - *From: U̷r̷a̷b̷e̷w̷e̷*

- **Problem:** fp8 dtype causing 'mul_cuda' not implemented error
  - **Solution:** Don't use fp8 for text projection input, cast to fp32 or use base torch ops
  - *From: Ablejones*

- **Problem:** Tiled VAE extremely slow with wrapper nodes
  - **Solution:** Update to latest wrapper version and clear Triton caches, or use native VAE with WanVideoToVAELatents node
  - *From: Kijai*

- **Problem:** Tiled VAE temporal blending at frame 45
  - **Solution:** Increase temporal_size setting to match or exceed total frames (e.g., 84 for 81 frames)
  - *From: FL13*

- **Problem:** Wan Animate cutting frames
  - **Solution:** Use frame counts that follow 4*n+1 pattern (49, 53, etc.) as model works with these in latent space
  - *From: 42hub*

- **Problem:** VAE 2x upscaler size mismatch with Wan 2.2
  - **Solution:** Use VAE utils node by spacepxl for loading VAE and VAE decode
  - *From: FL13*

- **Problem:** SVI continuation color shift and contrast degradation
  - **Solution:** Use svi-shot instead of svi-film, try more overlap frames (9 or 13), use weight scaling
  - *From: Ablejones*

- **Problem:** Getting '36 channels vs 32 channels' error
  - **Solution:** Check for model mismatch, particularly VAE file as first step
  - *From: hudson223*

- **Problem:** Bindweave workflow error about 'ref_images' vs 'ref_masks'
  - **Solution:** Update to latest WanExperiments repo and ensure all nodes are updated
  - *From: Ablejones*

- **Problem:** OutOfMemoryError after ComfyUI update
  - **Solution:** Remove --fast flag from launch parameters and update WanVideoWrapper
  - *From: JohnDopamine*

- **Problem:** SVI-shot not working with different segment shots
  - **Solution:** Use Kijai's version of svi-shot LoRA and ensure WanExperiments repo is installed
  - *From: Ablejones*

- **Problem:** BlockSwap node glitching
  - **Solution:** Right click and select 'fix recreate'
  - *From: hicho*

- **Problem:** Confetti artifacts in first frames
  - **Solution:** Usually related to LoRA or step size on schedule, try lowering shift parameter
  - *From: Ablejones*

- **Problem:** Qwen Edit defaulting to original image
  - **Solution:** Switch from full model to fp8 quantization
  - *From: ingi // SYSTMS*

- **Problem:** KeyError: 'samples' when connecting WanAnimate samples to second sampler
  - **Solution:** Issue with samples output from WanAnimate not being compatible with standard sampler input
  - *From: VRGameDevGirl84(RTX 5090)*

- **Problem:** Sizes of tensors must match error with Fun Control model
  - **Solution:** Resolution mismatch - control video was 640x1024 but expected 1024x640, caused by DWPose resizing output
  - *From: Juan Gea*

- **Problem:** HuMo causing bad first frames and missing frames
  - **Solution:** Apply sampler fix that prevents padding at front - only pad/trim at end to preserve real motion
  - *From: Scruffy*

- **Problem:** Grid noise in generated videos
  - **Solution:** Use more steps, lightx loras, disable sage attn, use 2.2 low noise + lightning or lightx2v
  - *From: spacepxl*

- **Problem:** Bright red colors appearing in videos
  - **Solution:** Remove lighting-related terms from prompts, may be caused by too many frames for wan 2.2 or fire scenes amplifying colors
  - *From: VRGameDevGirl84(RTX 5090)*

- **Problem:** VACE reference image causing tensor size mismatch
  - **Solution:** Ensure all images, control masks, and videos have same resolution, width, height and frame count
  - *From: VRGameDevGirl84(RTX 5090)*

- **Problem:** FlashVSR PTXASError on Blackwell GPU with 'sm_121a' not defined
  - **Solution:** Set environment variables TORCH_COMPILE_BACKEND=eager and TRITON_PTXAS_PATH in ComfyUI startup
  - *From: Ashtar*

- **Problem:** start_step must be less than end_step error when using denoise parameter
  - **Solution:** Either use denoise OR start_step, not both. Set denoise to 1.0 and use start_step/end_step instead
  - *From: 42hub*

- **Problem:** Incomplete/broken video when starting sampling at higher step numbers
  - **Solution:** Enable 'add noise to samples' in the high noise sampler when doing partial steps
  - *From: Kijai*

- **Problem:** VACE inpainting not working - mask being ignored
  - **Solution:** Bake the mask into the original video as grey areas rather than using mask separately. Can also try inverting mask due to wrapper vs native polarity differences
  - *From: Juan Gea*

- **Problem:** First frame flashing/artifacts in Wan 2.2 first-last frame workflows
  - **Solution:** Enable 'add noise to samples' toggle as Wan 2.2 acts like FL2V model
  - *From: Kijai*

- **Problem:** HuMo causing severe color drift when replacing 2.1 LN
  - **Solution:** Don't combine FF2LF and HuMo embeds - separate conditioning to HN and LN respectively
  - *From: Gleb Tretyak*

- **Problem:** Context windows not working with Wan-specific node
  - **Solution:** Use non-Wan context windows node with dim==2 instead of Wan-specific version
  - *From: Gleb Tretyak*

- **Problem:** Wrapper OOMing on 17 frames
  - **Solution:** Enable blockswap, clear triton cache, disable torch compile, or reduce resolution
  - *From: Kijai*

- **Problem:** HuMo making lips flap constantly
  - **Solution:** Use lip sync suppress node or adjust audio scale settings
  - *From: Chandler ✨ 🎈*

- **Problem:** First frame flash in HuMo generations
  - **Solution:** Discard first few frames and use overlap with 5 frames, replacing start frames with clean end frames from previous generation
  - *From: Ablejones*

- **Problem:** CLIPVisionLoader error 'clip_vision_h.safetensors' not in list
  - **Solution:** Need to add the clip_vision_h.safetensors model to the clip vision folder and select it in the loader node
  - *From: Suomsoh*

- **Problem:** Instant OOM issue with wrapper
  - **Solution:** Remove --async-offload flag. The more you offload with blockswap, the worse it gets
  - *From: Gleb Tretyak*

- **Problem:** KeyError: 'randomref_embedding_pose.0.weight' with svi-dance
  - **Solution:** Need to load the unianimate lora on the model loader, not the set node, because it patches the model too
  - *From: Kijai*

- **Problem:** Context windows causing 'bad first frames' in HuMo
  - **Solution:** Change sampler to pad/trim at the end instead of front to preserve real frames and avoid garbage at start
  - *From: Chandler*

- **Problem:** Native offloading issues
  - **Solution:** Add --reserve-vram flag for few gigabytes. Issues caused by custom nodes breaking automatic offloading or Windows VRAM fluctuations
  - *From: Kijai*

- **Problem:** Shared GPU memory usage causing extreme slowdowns (100+ s/it)
  - **Solution:** Set Nvidia control panel to 'prefer no sysmem fallback', check task manager for processes using shared GPU memory, comment out PYTORCH_CUDA_ALLOC_CONF environment variable
  - *From: Ablejones*

- **Problem:** Native Wan block swap node crashes ComfyUI
  - **Solution:** Node is deprecated and blocked because it never worked properly and breaks newer offloading features. Use --reserve-vram 2 instead
  - *From: Kijai*

- **Problem:** HuMo audio encoder errors on fresh ComfyUI install
  - **Solution:** Use Scruffy's fixed Humo node from WanExperiments repo which allows multiple image references instead of just one
  - *From: Scruffy*

- **Problem:** Context windows WF requires updated ComfyUI
  - **Solution:** Use Kijai's context windows PR branch with git commands: git fetch origin pull/10975/head:pr-10975, git checkout pr-10975, git merge --no-edit master
  - *From: Ablejones*

- **Problem:** Poor HuMo lip sync with custom audio
  - **Solution:** Check audio quality with Preview Audio node, use detailed prompts describing speech patterns, run vocals through separator first
  - *From: Ablejones*

- **Problem:** Browser tab visibility slowing generation
  - **Solution:** Minimize browser tab or use remote setup, hardware acceleration in browser uses 500-1000MB VRAM
  - *From: Kijai*

- **Problem:** Black screens at 720x720 with comfy_chunked
  - **Solution:** Revert to wrapper version 1.3.9 or switch back to using 'comfy' instead of 'comfy_chunked'
  - *From: garbus*

- **Problem:** OOM errors after updates
  - **Solution:** Complete ComfyUI reinstall can resolve persistent OOM issues that occur every 18 seconds
  - *From: Chandler ✨ 🎈*

- **Problem:** Out of RAM errors with block swap
  - **Solution:** Swap less blocks and/or disable the non-blocking on the block swap node
  - *From: Kijai*

- **Problem:** AudioEncoderEncode crashes on torch 2.9
  - **Solution:** Downgrade to torch 2.8 to fix flash attention compatibility issues
  - *From: Scruffy*

- **Problem:** Sampling artifacts with different shift values
  - **Solution:** Keep the same shift value across all samplers in chain sampling - shift defines the schedule for entire sampling process
  - *From: Ablejones*

- **Problem:** LoRA key not loaded errors with LightX2V on Wan 2.2
  - **Solution:** Remove incompatible keys from LoRA file using Python script, or use --verbose CRITICAL flag to suppress console output
  - *From: patientx*

- **Problem:** Context windowing artifacts
  - **Solution:** Works best with controlled backgrounds, single frame masks, or strong controls like VACE. Limited to specific circumstances
  - *From: Ablejones*

- **Problem:** SCAIL frame range restriction around 600 frames causing errors
  - **Solution:** Set per_batch to a frame count you can handle so it doesn't try to do it all at once
  - *From: Kijai*

- **Problem:** VRAM stalling with GGUF Q5 models in WanVideoWrapper
  - **Solution:** Increase block swap amount (e.g., to 30) to prevent stalling
  - *From: Kijai*

- **Problem:** Time To Move high noise sampler only doing 1 step when using 4 total steps
  - **Solution:** TTM skips first step like vid2vid, so with 4 total steps split at center and TTM skip, high noise does 2 steps but appears as 1
  - *From: Kijai*

- **Problem:** Glitched out fingers and infinitely long fingers in SCAIL
  - **Solution:** Try blurring the input image a bit to reduce artifacts
  - *From: Kijai*

- **Problem:** ComfyUI Desktop app cannot install certain custom nodes
  - **Solution:** Consider using portable or venv installation instead
  - *From: dj47*

- **Problem:** Exposure gain at beginning of frame batches and loss at end
  - **Solution:** Use WASWanExposureStabilizer node which averages luminance gains from stable middle batch and applies fixes to beginning/end frames
  - *From: WAS*

- **Problem:** CUBLAS_STATUS_INTERNAL_ERROR with SCAIL
  - **Solution:** Update triton-windows package - issue fixed in October for older GPUs and fp8 e4m3fn
  - *From: Kijai*

- **Problem:** Torch compile not working with fp8 wan models on RTX 3090
  - **Solution:** Update triton-windows or change RMS norm mode to 'pytorch' in model loader for pytorch 2.9+
  - *From: Kijai*

- **Problem:** Wan2.1 workflows generating noise after first generation
  - **Solution:** Clear torch and cuda cache, update to pytorch 2.9.1 or newer
  - *From: Gleb Tretyak*

- **Problem:** LongCat Avatar bf16 model OOM on 4090
  - **Solution:** Disable 'keep_model_in_vram' option in model loader
  - *From: Kijai*

- **Problem:** RTX 5090 significant performance drop in multi-window SCAIL
  - **Solution:** Try switching use_non_blocking to false in WanVideo BlockSwap and increase blocks_to_swap
  - *From: 42hub*

- **Problem:** Video combine only runs once instead of looping after ComfyUI update
  - **Solution:** Need to find setting to fix looping behavior
  - *From: Zabo*

- **Problem:** Draw faces option in SCAIL-Pose only applies to main subject
  - **Solution:** Bug confirmed and fixed by Kijai
  - *From: Kijai*

- **Problem:** ComfyUI workflow crashes saying 'Reconnecting' and 'press any key to continue' during SVI Pro second ksampler
  - **Solution:** Use Clear VRAM node after first ksampler - it's an OOM issue
  - *From: GWX-Reloaded*

- **Problem:** WanVideoSampler 'vace_blocks.8.modulation' error with fp8 models
  - **Solution:** Use bf16 versions instead, the base model there is 1.3B
  - *From: Kijai*

- **Problem:** Old workflow with start_step bug
  - **Solution:** Set the start_step again in the sampler node, it's a comfy bug that doesn't see it as 0
  - *From: Kijai*

- **Problem:** Missing SVI Pro node after update
  - **Solution:** Do git pull from nightly after uninstalling and reinstalling - nodes.py wasn't updating
  - *From: devnullblackcat*

- **Problem:** SCAIL detection phase hard locking PC
  - **Solution:** Keep detection around 15fps, reducing resolution helps more than reducing frame rate
  - *From: devnullblackcat*

- **Problem:** mat1 and mat2 shapes error with gguf text encoders
  - **Solution:** Try loading the gguf model into regular model loader and using regular clip
  - *From: hudson223*

- **Problem:** ClipLoaderGGUF error 'only 0-dimensional arrays can be converted to Python scalars'
  - **Solution:** Update gguf custom node, there are compatibility issues with recent ComfyUI updates
  - *From: xwsswww*

- **Problem:** Crop/uncrop VACE inpainting showing seams and quality degradation
  - **Solution:** Add more padding of unmasked area, use bigger sampling area, composite back with grow mask and border blending
  - *From: Hashu*

- **Problem:** SM89 kernel not available error on Linux
  - **Solution:** SageAttention setup used wrong GPU spec when compiling - needs recompilation with correct GPU specifications
  - *From: kaibioinfo*

- **Problem:** Recent ComfyUI versions causing huge memory use increase with Wan
  - **Solution:** Revert to ComfyUI commit 2e9d51680a90bca9cc375ba7767f7bf3ed27d563 from 3 weeks ago
  - *From: chancelor*

- **Problem:** Sudden OOM issues in ComfyUI
  - **Solution:** Remove --fast and --use-sage-attention flags, add --disable-pinned-memory and --reserve-vram 2
  - *From: JohnDopamine*

- **Problem:** AttributeError: 'WanVideoModel' object has no attribute 'diffusion_model' after ComfyUI update
  - **Solution:** Revert to ComfyUI commit 4064062e7d2d5abdca6767b6944e331b70065ee8 or update wrapper (fixed by Kijai)
  - *From: devnullblackcat*


## Model Comparisons

- **VitPose vs DWPose**
  - VitPose is larger model, uncertain which is better overall, but VitPose works better for retargeting
  - *From: Kijai*

- **Sapiens vs VitPose/DWPose**
  - Sapiens is probably the best pose estimation model currently available
  - *From: Kijai*

- **WIP WanAnimate workflow vs example workflow**
  - WIP workflow with preprocessor gives substantially better quality, better faces, no artifacts
  - *From: seitanism*

- **UniAnimate vs WanAnimate for pose**
  - UniAnimate still wins with pose handling
  - *From: SpacelessTuna*

- **bf16 vs fp8_scaled quality difference**
  - Difference is not major, only noticeable when specifically looking for it, not worth chasing unless doing final polish
  - *From: Kijai*

- **Kijai's workflow vs native WanAnimate workflow**
  - Kijai's works several times better, only native advantage is better cleanup of backplate (removal of old character)
  - *From: Juan Gea*

- **12 fps vs 24 fps for WanAnimate**
  - 12 fps better for consistency, 24 fps has awkward cuts and pose failures
  - *From: Kijai*

- **RGB vs pose input for WanAnimate**
  - RGB works for problematic scenes with FG elements, loses likeness slightly vs pose
  - *From: Hashu*

- **Anisora without loras vs with loras**
  - Better likeness and quality without loras, distillation is baked in so adding distill lora causes burning
  - *From: DawnII*

- **FP8 vs GGUF models on 30xx cards**
  - FP8_e5m2 gives better action, loads dual model (19GB each HN/LN) reaching 720p on 3060 12GB
  - *From: mdkb*

- **Wrapper vs Native workflow performance**
  - Better action from FP8 in wrapper than GGUF in native in 99% of cases
  - *From: mdkb*

- **HuMo vs other lipsync models**
  - Best quality audio to video but worst length of generations
  - *From: Kijai*

- **Native vs Wrapper model loading speed**
  - Native is actually faster, wrapper appears faster due to unmerged LoRAs
  - *From: Kijai*

- **AniSora 3.2 vs Lightning for animated content**
  - AniSora 3.2 distillation may be far better than lightning for animated content
  - *From: DawnII*

- **Lynx lite vs full model**
  - Full Lynx makes huge difference, lite only does face ID while full does reference with larger IP adapter applied on crossattn on all blocks
  - *From: Kijai*

- **WanAnimate vs VACE character consistency**
  - WanAnimate isn't great at character consistency, nothing like VACE in 2.1
  - *From: SonidosEnArmonía*

- **Distill LoRAs vs full CFG generations**
  - 90% of cases distill LoRAs produce better results than 50-step CFG generations
  - *From: Tony(5090)*

- **WanAnimate vs VACE for character swaps**
  - WanAnimate possibly better than VACE for simple swaps and accuracy, but VACE does more than just swaps
  - *From: mdkb*

- **HuMo vs Lynx**
  - HuMo seems better overall, Lynx head looks pasted into video like PuLID
  - *From: Ablejones*

- **Lynx full model vs lite version**
  - Lite version works better despite being much smaller - full model IP adapter doesn't seem effective
  - *From: Kijai*

- **WanAnimate vs other character models**
  - Nothing you couldn't already do with just VACE or Phantom. Currently not worth anything on its own
  - *From: Kijai*

- **GGUF vs fp8 for 3000 series GPUs**
  - Kijai recommends using GGUF on 3000 series. GGUF has slight quality advantage normally
  - *From: Kijai*

- **20 steps CFG 5.0 vs 6 steps CFG 1.0 WanAnimate**
  - Both tested, 20 steps version had issues with jerky motion
  - *From: Kijai*

- **Uni3c camera movements with Wan 2.2**
  - Works well for camera pans left/right and zoom in/out, but not as good for camera rotation around a person. Needs version compatible with 2.2
  - *From: xwsswww*

- **HUMO vs InfiniteTalk**
  - Different results - HUMO provides better acting/facial expressions, InfiniteTalk enables long generation. Mixed together works better than either alone
  - *From: Juan Gea*

- **GGUF Q8 vs FP8 quality on Wan**
  - Wan has bigger quality hit from fp8 than QwenImage, GGUF Q8 should only be slightly slower and better quality
  - *From: Kijai*

- **LightX2V speed tests**
  - LightX2V + FastWan 2 steps: 31.49s, LightX2V 4 steps: 70.63s, LightX2V + FastWan 4 steps: 50.29s
  - *From: VRGameDevGirl84(RTX 5090)*

- **2.1 T2V vs 2.2 low T2V**
  - Barely any difference for T2V, more difference for I2V
  - *From: Kijai*

- **LCM vs DPM++_SDE for Lynx**
  - LCM burns less VRAM and is more natural, DPM++_SDE may be too much
  - *From: Kijai*

- **OVI vs WAN 2.5**
  - Some OVI gens better than WAN 2.5 480p, better speech quality
  - *From: ZeusZeus*

- **VACE vs FUN for control**
  - VACE allows specific control not achievable without it, better quality than FUN
  - *From: Juan Gea*

- **OVI vs Wan 2.2 Animate + Infinite Talk**
  - OVI generates audio automatically but Wan 2.2 Animate + Infinite Talk may be better quality for lip-sync scenarios
  - *From: AmirKerr*

- **OVI vs 2.2 14B**
  - OVI looks more real than 2.2 14B due to audio addition making motion more realistic
  - *From: Draken*

- **SLG 11 vs SLG 7,8,9**
  - SLG 11 has better expression, SLG 7,8,9 has more background motion and better audio
  - *From: Kijai*

- **rCM vs base model motion**
  - rCM makes movements faster similar to base model, LightX2V makes movements much slower
  - *From: yi*

- **5B turbo vs fastwan**
  - Turbo is bad, fastwan is amazing according to tests
  - *From: hicho*

- **Local vs wan.video**
  - Local great quality, some ways better apart from lighting issues
  - *From: Juampab12*

- **Clip embeds vs no clip embeds in WanAnimate**
  - With clip embeds: better identity but worse lighting. Without: better lighting but worse identity
  - *From: Kijai*

- **rCM lora vs lightx2v lora**
  - rCM always gives subject some hair, lightx2v more stable
  - *From: Kijai*

- **New 2.2 MoE lora vs old 2.1 lora at higher strength**
  - Not convinced new lora is better than using old 2.1 lora at higher strength
  - *From: Kijai*

- **FlashVSR vs SeedVR2**
  - SeedVR2 comparable quality but more VRAM hungry, FlashVSR much faster at 1 step
  - *From: PATATAJEC*

- **FlashVSR performance on faces vs other elements**
  - Great for clothes, horses, trees but struggles with small distant faces, can make them worse
  - *From: mdkb*

- **Torch 2.8 vs 2.9**
  - 2.9 fixes compile issues that 2.8 had, but requires CUDA 13.0 and updated drivers
  - *From: Kijai*

- **SageAttention vs SDPA**
  - SageAttention makes inference faster but doesn't reduce memory usage significantly, SDPA more stable
  - *From: Kijai*

- **Wan 2.2 Wrapper vs Native T2V**
  - Slightly different randomness, wrapper shows bird sitting in air while native has it properly positioned. One run isn't enough sample size to determine quality differences
  - *From: Kijai*

- **FlashVSR on already high-res vs low-res content**
  - FlashVSR meant for 4x upscaling from very low res. Using on 1280x768 produces blurry results with over-sharpening. Better for initial low-res to mid-res upscaling
  - *From: Juan Gea*

- **MoCha vs WanAnimate**
  - MoCha has better eye movement and lighting control but uses double compute and no pose detection needed
  - *From: Draken*

- **MoCha ID preservation vs VACE 2.1/Animate**
  - ID isn't as good as VACE 2.1/Animate but lighting is super impressive
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Context windows vs continuous motion**
  - Context doesn't deteriorate over time but slower with window continuation issues on backgrounds
  - *From: Kijai*

- **Wan Animate vs Mocha**
  - Animate needs to mask entire video and is faster, Mocha only needs first frame masked but is slower. Quality is subjective based on use case
  - *From: Dever*

- **Krea Realtime 14B vs StreamDiffusion + SDXL**
  - Krea delivers higher visual quality and temporal stability but lacks fine-grained control. StreamDiffusion gives more tweakability but temporal consistency is challenging
  - *From: ericxtang*

- **VACE vs WAN 2.2 for animation**
  - VACE tends to morph images between keyframes while WAN 2.2 provides better actual animation movement
  - *From: GWX-Reloaded*

- **MoCha vs WAN Animate**
  - MoCha is better at placing subject in scene but has vague identity preservation due to lower Wan 2.1 base quality. WAN Animate has better identity preservation
  - *From: blake37*

- **Native WAN vs Wrapper loading times**
  - Native WAN takes 13 seconds to load while wrapper takes 2 seconds
  - *From: hicho*

- **Light VAE vs Wan VAE**
  - Light VAE is significantly faster, especially on high resolution, but has quality loss. Good for testing and low VRAM situations.
  - *From: hicho*

- **Lightning4step vs LightX2V LoRA**
  - Lightning4step makes everything super bright and fake looking. LightX2V is more realistic but colors are washed out with some detail loss.
  - *From: DaxRedding*

- **ComfyUI new vs old cache system**
  - New version uses more RAM, reduced frame capacity from 97 to 69 frames at 1024x1024 with same settings
  - *From: lemuet*

- **RCM vs no LoRA for I2V**
  - RCM improves prompt following but burns out I2V outputs more
  - *From: blake37*

- **MoCha vs WAN Animate**
  - MoCha gives better integration into scenes but worse image quality, feels like CGI from a few years ago
  - *From: blake37*

- **ChronoEdit vs standard QIE**
  - PROs: better results for realistic settings, marginally better than QIE with no LoRAs. CONs: generation time for video instead of single image, difficult for high-res editing
  - *From: Dever*

- **Ovi i2v vs Wan 2.2 i2v**
  - Wan 2.2 much better - 5B vs 14B, no chance for Ovi
  - *From: Juampab12*

- **Native tiled VAE vs wrapper tiled VAE performance**
  - Native performs much better - 83 seconds vs 18+ minutes for same task
  - *From: brbbbq*

- **Ubuntu vs WSL2 vs Windows for model loading**
  - Ubuntu fastest, then WSL2, then Windows for model loading times
  - *From: pagan*

- **Wan 2.2 S2V vs InfiniteTalk**
  - InfiniteTalk is better, especially for longer generations. S2V had pose control but burned out eventually and wasn't infinite
  - *From: Kijai*

- **Native Bindweave with vs without embeddings**
  - Best output was without the annoying embeddings (CLIP Vision and QwenVL) that took forever to implement
  - *From: Ablejones*

- **Wan 2.2 HN vs Wan 2.1 FLF as first pass**
  - Results vary by case - sometimes FLF is better, sometimes HN performs better for the same content
  - *From: VRGameDevGirl84(RTX 5090)*

- **Native vs Wrapper Wan 2.2 quality**
  - Wrapper produces significantly better quality results than native implementation
  - *From: Gleb Tretyak*

- **I2V vs T2V quality**
  - I2V is known for better quality than T2V
  - *From: Gleb Tretyak*

- **Wan 2.2 vs 2.1 motion**
  - 2.2 is known for better motion than 2.1
  - *From: Gleb Tretyak*

- **VACE vs TimeToMove for interpolation**
  - TimeToMove works better for hand-drawn animation interpolation, VACE tries to morph frames too literally
  - *From: lemuet*

- **VACE 2.2 vs VACE 2.1 modules**
  - VACE 2.2 module is bad, use VACE 2.1 with Wan 2.2 models instead
  - *From: hicho*

- **T2V quantile 0.15 LoRA vs I2V LoRA for I2V workflows**
  - T2V quantile 0.15 version is smoother and better without oversharpening, though some may consider it overkill at 2GB
  - *From: FL13*

- **HuMo vs InfiniteTalk**
  - HuMo has more motion and better lip sync/subject replication, but InfiniteTalk is designed for long duration generations. HuMo requires creative workflows for longer videos
  - *From: Ablejones*

- **S2V vs HuMo vs InfiniteTalk**
  - S2V does extensions natively with less struggle, but not as good as InfiniteTalk for long videos or HuMo for lip sync and expressiveness
  - *From: Ablejones*

- **HuMo vs InfiniteTalk for lip sync**
  - HuMo's motion and lipsync is better by a mile. InfiniteTalk ends up stiff, feels pasted on. HuMo is more body-aware and lifelike
  - *From: Scruffy*

- **HuMo vs FFGO for multiple references**
  - HuMo beats FFGO. FFGO is hacky - forces all references into one white background frame vs HuMo's native multi-reference support
  - *From: Scruffy*

- **Wrapper vs Native HuMo implementation**
  - Wrapper is better - supports multiple reference images correctly while native was coded wrong and only uses one
  - *From: Scruffy*

- **Wrapper vs Native ComfyUI**
  - Wrapper users complain native doesn't work, native users complain they can't use wrapper. Wrapper manually sets memory management while native uses torch functions
  - *From: Kijai*

- **HunyuanVideo 1.5 vs Wan for anime**
  - HunyuanVideo has better consistency but much slower than Wan for same/worse quality in quick i2v tests
  - *From: dj47*

- **Wan 2.1 VACE vs Fun VACE 2.2 for low-noise**
  - Wan 2.1 VACE performs better on low-noise side, more natural and integrated results
  - *From: Ablejones*

- **Wan 2.2 High + HuMo Low vs HuMo only**
  - 2.2 combo provides better motion and prompt adherence, character reference works less well but can be improved with better prompting
  - *From: VRGameDevGirl84(RTX 5090)*

- **WanMove vs Wan 2.1 I2V VRAM usage**
  - WanMove doesn't increase VRAM use at all from Wan 2.1 I2V, sampling part is identical
  - *From: Kijai*

- **Context windowing vs extension methods**
  - Context windowing generates whole video at once while extension methods continue from last frame(s) - fundamentally different approaches
  - *From: Kijai*

- **GGUF Q5 vs fp8 performance**
  - GGUF Q5 somewhat slower than fp8 but not drastically, sdpa attention mode is lot slower than sageattn
  - *From: Kijai*

- **vitpose-H vs dwpose for pose detection**
  - vitpose-H generally better than dwpose but only does one person while dwpose can do multiple
  - *From: Kijai*

- **Native workflow vs WanVideoWrapper speed**
  - Same Q5 models run much faster in native workflow (few minutes) vs WanVideoWrapper (can take 51 minutes)
  - *From: Danial*

- **Torch compile vs no compile**
  - Maybe 10-20% speed boost, not huge difference
  - *From: Kijai*

- **SCAIL vs WanAnimate**
  - WanAnimate better for facial animation/dialogue, SCAIL better for multiple characters and advanced motion
  - *From: HeadOfOliver*

- **TurboDiffusion vs existing optimizations**
  - Essentially repackaging of existing techniques like sage attention, speed LoRAs, quantization - maybe 2x faster than current optimizations
  - *From: Kijai*

- **SCAIL vs SteadyDancer**
  - SCAIL delivers better quality for movement but doesn't have good long gen system like Animate
  - *From: Juan Gea*

- **SteadyDancer vs OneToAll Animation**
  - SteadyDancer accurately reproduces faces but always has glitches, OneToAll barely reproduces the face
  - *From: Kevin "Literally Who?" Abanto*

- **fp8 vs GGUF for VACE workflows**
  - fp8 e5m2 works better on 3060 setup than GGUFs for VACE 2.2 modules
  - *From: mdkb*

- **SCAIL vs LTX 2**
  - SCAIL better for movements/pose copying, LTX 2 better for facial consistency and skin quality
  - *From: Kevin "Literally Who?" Abanto*

- **MOVA vs HuMo**
  - MOVA looks better than HuMo, but no direct comparison possible since MOVA is unified model while HuMo requires audio input
  - *From: Draken*


## Tips & Best Practices

- **Cover entire character with mask, better too much than too little**
  - Context: When using WanAnimate masking
  - *From: Kijai*

- **Disable relight LoRA for 2D characters**
  - Context: Often has negative effect on more stylized/2D characters
  - *From: Kijai*

- **Use larger face references and higher resolutions**
  - Context: For better character similarity in WanAnimate
  - *From: Kijai*

- **Prompting helps with object handling**
  - Context: When model struggles with objects like swords, better prompting about how character handles object can help
  - *From: hicho*

- **Match frame rate to your input video**
  - Context: Model is 16fps but should match input video frame rate
  - *From: Kijai*

- **Use Load Video from Path node for large videos**
  - Context: Has no size limitations unlike upload node
  - *From: scf*

- **Prompt everything you can including eye color for better character consistency**
  - Context: When getting different characters in generations
  - *From: Kijai*

- **Make masks larger and blocky for more freedom in character shape**
  - Context: Mask shape forces character shape a lot
  - *From: Kijai*

- **Use face crop improvement and proper pose estimation for better output**
  - Context: dwpose is too thick in general, model expects specific pose format
  - *From: Kijai*

- **Start with higher CFG (3.5) for first steps to improve motion, then lower to 1**
  - Context: Using CFG scheduling with lightx2v lora for faster generation
  - *From: Juan Gea*

- **For v2v with video input, use denoise 0.35 or 0.50 on high model**
  - Context: When using video input with Wan models
  - *From: hicho*

- **Use v2v method with H+L models: 0.35 denoise, 2 steps instead of start/end step**
  - Context: For passing high model output to low model
  - *From: hicho*

- **Activate 'use video input v2v' setting when doing video to video**
  - Context: Needed for proper v2v workflow
  - *From: hicho*

- **For WanAnimate masking with wrapper, supply masks and input frames with masked area colorized to grey**
  - Context: Using VACE with masks
  - *From: DawnII*

- **Disconnect both background images and masks when doing full scene replace in WanAnimate**
  - Context: To animate just the character without background constraints
  - *From: Juan Gea*

- **Always go with wrapper since it has more speed and allows more testing**
  - Context: Choosing between wrapper and native workflows
  - *From: Léon*

- **For InfiniteTalk frame rate sync: interpolate WanAnimate 16fps to 32fps, then load at 25fps for InfiniteTalk**
  - Context: Syncing different frame rates between models
  - *From: PATATAJEC*

- **Use prompting for motion in WanAnimate**
  - Context: When background isn't moving even with control inputs
  - *From: A.I.Warper*

- **Use remap mask range for better background blending**
  - Context: When subject doesn't blend well with background
  - *From: VK (5080 128gb)*

- **Don't use distillation LoRAs with models that already have distillation baked in**
  - Context: When using pre-distilled models
  - *From: DawnII*

- **Use face crop instead of full frame for Lynx reference**
  - Context: When using Lynx reference adapter
  - *From: Kijai*

- **Connect infinitetalk only to high model in 2.2**
  - Context: When trying to use infinitetalk with Wan 2.2
  - *From: hicho*

- **Use Chinese negative prompts for better results**
  - Context: Chinese prompts may produce significantly different and potentially better results than English translations
  - *From: Kijai*

- **Avoid masking in character replacement**
  - Context: Masking tries to fit person in shape of other person and reduces consistency
  - *From: Piblarg*

- **Lower pose and face strength for difficult swaps**
  - Context: When swapping between very different body types (like Trump to thin woman), reduce control strengths
  - *From: PATATAJEC*

- **Use 256x256 face crops for reference adapters**
  - Context: Original implementations crop faces to 256x256 for reference adapters
  - *From: Kijai*

- **Generic wan negative prompts often don't help**
  - Context: The standard negative prompts used in examples may not actually improve results most of the time
  - *From: Ablejones*

- **Use empty wall prompting and negative prompts**
  - Context: To prevent unwanted objects appearing in background during character animation
  - *From: Kijai*

- **Use HuMo with InfiniteTalk for long generation**
  - Context: InfiniteTalk node with HuMo model uses normal i2v past the first window, can combine both audio embeds
  - *From: Kijai*

- **Adjust frame_window_size parameter when generating specific frame counts**
  - Context: When generating 81 frames, make sure to adjust frame_window_size in Wanvideo Animate Embeds Node to prevent video looping
  - *From: Gill Bastar*

- **Use context options for long video upscaling**
  - Context: For upscaling 400+ frame videos without running out of VRAM/RAM
  - *From: Cseti*

- **Use VACE for long video clip seam fixing**
  - Context: Split around seam, patch with grey frames and white masks for frames to fix, black mask for untouched frames
  - *From: mdkb*

- **Mix HUMO and InfiniteTalk embeds using WanVideo Combine Embeds node**
  - Context: Put HuMo Embeds first, InfiniteTalk second for improved results
  - *From: Juan Gea*

- **For dialogue use cases, try mixing IT and HUMO**
  - Context: Helps fight unwanted mouth movements and improves facial emotion expression
  - *From: mdkb*

- **Use tiling option to reduce VRAM reservation**
  - Context: Tiling lowered reserved VRAM from 17.47GB to 6.22GB for VAE operations
  - *From: scf*

- **Prompt location setting for consistent backgrounds**
  - Context: Prompt 'video is filmed in nightclub' to keep all video in same location
  - *From: Charlie*

- **Keep prompts simple for WAN Animate to reduce artifacts**
  - Context: Use ChatGPT to describe reference image then strip to bare minimum
  - *From: AR*

- **Reference images work better when facing camera**
  - Context: For better likeness preservation in WAN Animate
  - *From: hicho*

- **Use replace images in batch instead of inject latent for previewing sequences**
  - Context: For previewing frame injection workflows like VACE
  - *From: Kijai*

- **Use speech and audio tags as specified in OVI paper**
  - Context: Speech format: <S>text<E>, audio guidance with <AUDCAP>description<ENDAUDCAP>
  - *From: ZeusZeus*

- **Use same LoRA twice on both high and low noise models**
  - Context: When using LoRAs with Wan 2.2
  - *From: Dream Making*

- **Use 256 rank LoRA at 2.5 strength on high noise model**
  - Context: For best t2v results
  - *From: hudson223*

- **Use Flux resolution calculator for Wan**
  - Context: When finding correct resolution
  - *From: Dream Making*

- **Use prompt structure with <S> and <E> tags**
  - Context: Mandatory for OVI as both models use same prompt
  - *From: Kijai*

- **Add commas and ellipses for small pauses**
  - Context: For better audio timing in OVI
  - *From: Thom293*

- **DPM++ sampler with lower CFG (3) works well for realistic people**
  - Context: OVI generation settings
  - *From: slmonker(5090D 32GB)*

- **Start SLG later rather than full range**
  - Context: Better results than using full range like original code
  - *From: Kijai*

- **Use merged LoRAs for stronger effect**
  - Context: Merged loras are stronger than using base + lora
  - *From: Draken*

- **Switch VHS node output from webm to mp4**
  - Context: webm has compatibility issues on various platforms
  - *From: Thom293*

- **Use 50 steps minimum for proper results**
  - Context: Lower steps like 20 cause visual issues and added words
  - *From: Draken*

- **Use higher shift around 8 for OVI**
  - Context: Helps with quality, affects audio as well
  - *From: TK_999*

- **Change OVI audio cfg to 4.5**
  - Context: Same as used in mmaudio, seems to improve results
  - *From: U̷r̷a̷b̷e̷w̷e̷*

- **Make sure no groups are disabled when using audio workflows**
  - Context: For proper autoqueuing of generations
  - *From: VRGameDevGirl84(RTX 5090)*

- **Prompt has huge impact on OVI results**
  - Context: Can get garbled mess but then perfect results by changing one or two words with same seed
  - *From: U̷r̷a̷b̷e̷w̷e̷*

- **Use strength 0.8 to reduce oversharpening**
  - Context: FlashVSR default can be too sharp
  - *From: Kijai*

- **FlashVSR works best with really low quality inputs**
  - Context: Their examples are from 384x384 resolution
  - *From: Kijai*

- **Match input frame count with num_frames setting**
  - Context: To avoid frame processing issues
  - *From: Kijai*

- **Process at lower resolution first, then upscale**
  - Context: Perform inference at lower res for speed, then upscale with FlashVSR, then final upscale with wan for killer combo
  - *From: Juan Gea*

- **Use smaller context window to reduce VRAM usage**
  - Context: 48 frame context instead of full 85 frames reduces VRAM at cost of small glitch in middle
  - *From: PATATAJEC*

- **Apply slight temperature change for color correction**
  - Context: To counteract the browning effect FlashVSR causes
  - *From: CJ*

- **Resize reference image to match wan output resolution**
  - Context: Feeding 1080p reference to 720p wan output takes more VRAM
  - *From: hicho*

- **Clear triton caches after updates**
  - Context: Especially after comfy code updates to prevent compilation issues
  - *From: Kijai*

- **Use --reserve-vram 2 on Windows with monitor on same GPU**
  - Context: Helps prevent OOM when display uses same GPU as ComfyUI
  - *From: Kijai*

- **Convert git-managed custom nodes for easy updates**
  - Context: Use git init, add remote, fetch, checkout to enable git pull updates
  - *From: BestWind*

- **Test new torch versions on separate ComfyUI install**
  - Context: Avoid breaking working setup when testing bleeding edge versions
  - *From: hicho*

- **Use total pixel scaling for GPU VRAM constraints**
  - Context: When GPU can only handle specific total pixels (like 600,000 pixels max), calculate resolution ratios to stay within limits while preserving aspect ratio
  - *From: Ashtar*

- **Blur footage slightly before upscaling with FlashVSR**
  - Context: Gives the upscaler more room to work, at cost of not keeping exactly the original
  - *From: Draken*

- **Resolution is about signal to noise ratio, not just pixel count**
  - Context: A file marked as 1280x720 doesn't mean it was captured/rendered at that resolution. Real quality depends on how 'noisy' each frame is compared to signal
  - *From: Draken*

- **Start with base Wan 2.2 models before trying fine-tunes**
  - Context: Base model is still king, unlike SDXL/SD1.5 where base models weren't very capable
  - *From: Ablejones*

- **Use LoRAs for NSFW content instead of full model merges**
  - Context: Video models are hard to make complete new merges for, but LoRAs work fine for NSFW applications
  - *From: Canin17*

- **Use slightly larger tile dimensions than exact factors**
  - Context: For tiling, dimensions slightly larger than exact factors of original image make overlap work more efficiently
  - *From: Ablejones*

- **Use Linux to avoid low level torch/triton problems**
  - Context: Windows triton has limitations
  - *From: Kijai*

- **Set force_offload to true on samplers to free memory**
  - Context: Memory is freed right after sampler finishes
  - *From: Kijai*

- **Second run indicates torch compile benefit**
  - Context: First run includes compiling so can be slower
  - *From: Kijai*

- **Use converted LoRAs instead of native VACE module to save VRAM**
  - Context: Native module is bf16, converted gives almost identical results
  - *From: Kijai*

- **Two reference images work better than one**
  - Context: Can provide close up of face and full body so you don't have to pick
  - *From: Draken*

- **Use 'human' in negative prompt for non-human characters**
  - Context: When generating non-human character animations, always add 'human' to negative prompt
  - *From: Charlie*

- **Don't use FP8 on text encoder nodes unless absolutely necessary**
  - Context: FP8 on text encoder nodes has no memory footprint benefit and shouldn't be used unless VRAM is extremely limited
  - *From: Kijai*

- **Disable relight LoRAs for better character likeness**
  - Context: When trying to maintain character consistency and likeness to reference image
  - *From: Charlie*

- **Use res_2s/bong tangent samplers for better realism**
  - Context: Slower but delivers better results in general, though not available in wrapper currently
  - *From: Juan Gea*

- **Disable LightX LoRA but keep WanAnimate relight LoRA**
  - Context: When not using LightX acceleration, keep relight LoRA enabled to avoid burnt/orange video appearance
  - *From: Charlie*

- **Use higher resolution for better identity preservation**
  - Context: Higher resolution makes biggest difference with preserving identity, especially for character likeness
  - *From: blake37*

- **Match reference image pose and size to driving video**
  - Context: Reference image should show person in similar pose and size to driving video person to avoid big mismatches
  - *From: seitanism*

- **Continue from last 5 frames with film LoRAs**
  - Context: When using film LoRAs for longer videos, continue generation from last 5 frames of previous generation
  - *From: Kijai*

- **Use HuMo i2v model patcher for embedded mask manipulation**
  - Context: For SVI and dialogue replacement workflows
  - *From: Ablejones*

- **Generate with 2.2 first, then use HuMo/InfiniteTalk for lip sync**
  - Context: For difficult shots requiring control - use total freedom in 2.2 generation, then V2V for lip sync
  - *From: Juan Gea*

- **Save latent to disk between samplers to reduce RAM usage**
  - Context: When second sampler uses significantly more RAM than first
  - *From: lemuet*

- **Use MagRef for low pass instead of standard Wan 2.2 low**
  - Context: Preserves more detail from input I2V image and creates less context artifacts
  - *From: blake37*

- **Cut off last few frames of previous generation for better lipsync transitions**
  - Context: When creating clips to stitch together, words landing between clips cause weirdness
  - *From: Ablejones*

- **Face should take up 1/3 of frame at 544p-720p for best lipsync results**
  - Context: When not practical, generate at lower resolution then detail the face at higher resolution with 0.5 denoise
  - *From: Ablejones*

- **Use overlapping frames for any video consistency**
  - Context: Need overlapping frames to get consistency when stitching video segments
  - *From: Ablejones*

- **Reduce LoRA strength to remove blurry spots**
  - Context: When Krea LoRA adds extra details but creates blur
  - *From: hicho*

- **Reduce window size to fit higher resolutions in LongCat**
  - Context: Can reduce from 81 frames to 77 or even 66 frames to accommodate higher resolution generations
  - *From: Juan Gea*

- **Use larger face regions for HuMo inpainting**
  - Context: Crop image, blow face up to high res, denoise, then paste back into original video
  - *From: Ablejones*

- **Use 960x960 resolution for optimal results**
  - Context: Model is trained for this resolution, higher resolutions may cause issues
  - *From: Kijai*

- **Use 81 frames for best results**
  - Context: Model is trained for 81 frames, other frame counts may not work as well
  - *From: Kijai*

- **Use gamma exposure operation to handle color shift**
  - Context: For dealing with continuation color shift issues in long generations
  - *From: samhodge*

- **Use SDPA instead of SageAttn for better quality**
  - Context: When generating still images with Wan 2.2
  - *From: ingi // SYSTMS*

- **Use middle gray (127,127,127 RGB) for solid frames**
  - Context: For I2V conditioning frames that should be generated
  - *From: Ablejones*

- **Use umt5-xxl-fp16.safetensors instead of umt-xxl-enc-bf16.safetensors**
  - Context: The 'enc' version only works with WanVideoWrapper, remove 'enc' for native ComfyUI
  - *From: Ablejones*

- **Pressure on mouse when sending matters for generation quality**
  - Context: Technique for getting good results
  - *From: samhodge*

- **Can disrupt SVI reference frame bias by changing reference frames, SVI LoRA strength, or reference latent strength**
  - Context: When SVI-shot keeps head tilted based on reference frame
  - *From: Ablejones*

- **Use custom sigmas with shift 1.0 to prevent morphing from turning into fade**
  - Context: For maintaining dynamic morphs instead of fades in video generation
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Set shift to 50 to stay in 1-0.875 timestep range for LoRA training**
  - Context: When using LoRAs trained with TREAD in that specific range
  - *From: ingi // SYSTMS*

- **Remove lightning LoRA and use full 20-30 steps for better Qwen Edit results**
  - Context: When lightning LoRA causes issues with image editing
  - *From: AshmoTV*

- **Use video and mask it like Animate for InfiniteTalk v2v**
  - Context: For masked video-to-video with InfiniteTalk
  - *From: Dever*

- **Use fp32 VAE for better results**
  - Context: Can be loaded in ComfyUI for improved quality
  - *From: Gleb Tretyak*

- **Use mid gray frames (127,127,127 RGB) after first frame for HuMo**
  - Context: Helps reduce flashing issues when using HuMo
  - *From: Gleb Tretyak*

- **Use headshot of character for better HuMo results**
  - Context: Model performs better when it can see character clearly from front
  - *From: VRGameDevGirl84(RTX 5090)*

- **Check resolution with Get Size & Count node**
  - Context: Useful for debugging tensor size mismatch errors
  - *From: lemuet*

- **Use eta 1.0 on sampler settings for HuMo fix**
  - Context: Part of configuration to reduce flashing issues
  - *From: Gleb Tretyak*

- **Use Load Audio node from Video Helper Suite for audio trimming**
  - Context: Has seek parameter and duration value for selecting specific parts of audio for InfiniteTalk
  - *From: atom.p*

- **Always set denoise to 1.0 and use start_step/end_step for clearer control**
  - Context: In wrapper, denoise parameter can cause confusing situations
  - *From: 42hub*

- **For VACE with OpenPose, use black background and blend with original video**
  - Context: When combining multiple controls like mask and pose for VACE inpainting
  - *From: Ablejones*

- **Use Phantom on low stage for better resemblance in VACE workflows**
  - Context: When doing character consistency in VACE inpainting
  - *From: Ablejones*

- **Use fractional denoising for Wan inpainting**
  - Context: When using latent noise mask inpainting, use denoise < 1.0 like 0.6 or 0.7, or start at step > 0 in wrapper
  - *From: Ablejones*

- **Masks can be feathered or blurred**
  - Context: Any Wan model mask can have values between 0 and 1 and be blurred, sometimes works better
  - *From: Ablejones*

- **Test samplers and schedulers separately**
  - Context: When testing HuMo flash mitigation, constrain parameter space by testing one variable at a time to get meaningful results
  - *From: Ablejones*

- **Check model layers to see if clip vision is used**
  - Context: Inspect model's HF layers - models without img_emb layers will ignore clip vision embeddings
  - *From: Ablejones*

- **Use full body reference images for HuMo**
  - Context: If model has to guess missing parts (like pants), it will likely guess differently in longer clips causing inconsistencies
  - *From: Scruffy*

- **Describe reference images in prompts**
  - Context: HuMo works better when you describe the reference images in the prompt, not just rely on the images alone
  - *From: VRGameDevGirl84*

- **When in doubt with context windows: more overlap**
  - Context: Increasing overlap from 30 to 50 helps blend context windows better
  - *From: Kijai*

- **Use Load Multiple Images (batch) node for multiple references**
  - Context: Best way to batch reference images for HuMo. Images don't need to be same size
  - *From: Scruffy*

- **For better 2.2 motion with HuMo: Run first few steps with Wan 2.2 HN using prompts to match target character, then let HuMo take over for remaining steps**
  - Context: When combining 2.2 high noise with HuMo low noise for better motion + audio sync
  - *From: Ablejones*

- **Run inpainting pass on faces if they are small in HuMo videos**
  - Context: Crop faces, upscale, sample with HuMo, paste back into original video for better results
  - *From: Ablejones*

- **Use detailed prompts for HuMo lip sync**
  - Context: Instead of just 'talking', use descriptions like 'She very slowly says two words, separated by silence. After the first word she pauses and takes a breath'
  - *From: Ablejones*

- **Don't hook up HuMo node to sampler if not using HuMo model**
  - Context: Only connect HuMo node when actually using the HuMo model in that sampler
  - *From: Ablejones*

- **Use depth maps instead of pose for sketchy drawings**
  - Context: DW pose doesn't work well on drawings, but depth maps work surprisingly well for sketches
  - *From: dj47*

- **Test strength of WanVideo VACE encode**
  - Context: Experiment with different encode strength values to find what works best for your content
  - *From: dj47*

- **Use 81 or 97 frames minimum for context windows**
  - Context: Setting frames too low can cause weird results in context window sampling
  - *From: Ablejones*

- **Use 3-4 steps without LightX LoRA at start for better motion**
  - Context: For T2V, adding initial steps without speed LoRA before main sampling improves dynamics
  - *From: garbus*

- **Use lower shift values with I2V (around 5)**
  - Context: I2V generally works better with shift around 5, higher shift may be needed when not using distill LoRA
  - *From: Ablejones*

- **Keep prompts simple for MMAudio**
  - Context: Over-prompting MMAudio makes it perform worse, simple prompts or no prompt work better
  - *From: dj47*

- **Use CFG 5.5 and negatives for better MMAudio results**
  - Context: Higher CFG and negative prompts help reduce unwanted sounds and moaning
  - *From: dj47*

- **Match frame rates between video and MMAudio**
  - Context: Ensuring frame rate matching is important for MMAudio to sync properly with video
  - *From: dj47*

- **Use not-quite black background for VACE Pose input**
  - Context: Straight black backgrounds can cause issues with VACE pose conditioning
  - *From: Ablejones*

- **Monitor VRAM during ksampler - if you have 500+ mb free VRAM steps should warm up quickly**
  - Context: For detecting VRAM issues, especially on cards like 2060
  - *From: hicho*

- **Use skip_final_model_call option to avoid context windows time stepping issues**
  - Context: When using substep samplers with context windows, minimal output difference
  - *From: Ablejones*

- **Increasing resolution of subject in frame improves quality of subject transfer**
  - Context: Can then insert the subject into target video later using traditional video editing
  - *From: Ablejones*

- **Use #202020 background color for better results**
  - Context: Personal preference that has been working well lately
  - *From: Ablejones*

- **Always backup your venv and keep dev/production versions**
  - Context: Before updating ComfyUI or making major changes
  - *From: Gateway {Dreaming Computers}*

- **Use WanMove with spline editor for keyframe animation support**
  - Context: Can span over several context windows for Time to Move
  - *From: zelgo_*

- **Default pose workflow ends at 0.5, increase to 1.0 to help with pose adherence**
  - Context: When using SCAIL pose control
  - *From: Kijai*

- **Match starting pose and composition for SCAIL animation**
  - Context: Reference image should have similar starting pose as source animation
  - *From: ucren*

- **Use rank 512 for LoRA extraction and adjust strength above 1.0 for Wan 2.2 high**
  - Context: WanMove LoRA extraction and usage
  - *From: Gleb Tretyak*

- **Set block 0 to 0.0 when using extracted LoRAs**
  - Context: Reduces unwanted artifacts and improves coherence
  - *From: Ablejones*

- **Check RAM/VRAM usage if experiencing dramatic performance drops**
  - Context: Multi-window SCAIL performance issues
  - *From: 42hub*

- **Use both LoRAs for better motion accuracy**
  - Context: When working with experimental motion LoRAs
  - *From: Ablejones*

- **Keep HuMo ref disconnected or set to very low strength**
  - Context: It tends to snap image back to ref and interferes with motion
  - *From: Ablejones*

- **Lean into practically infinite canvas and make gigantic workflows rather than using loops**
  - Context: Loops are fragile and don't allow stopping/starting partial executions
  - *From: Ablejones*

- **Use brute-force curation and feed VACE different 16-frame sets until it clicks**
  - Context: For seamless video transitions
  - *From: NodeMancer*

- **The tighter the crop to masked area, the more visible seams are**
  - Context: VACE inpainting - add more padding for better results
  - *From: Hashu*

- **Use --disable-pinned-memory flag for OOM issues**
  - Context: When experiencing sudden out of memory problems in ComfyUI
  - *From: JohnDopamine*

- **Set NVIDIA driver CUDA sysmem fallback policy to 'Prefer NO sysmem fallback'**
  - Context: For better performance in ComfyUI by preventing driver-level block swapping
  - *From: JohnDopamine*

- **Check Windows page file settings**
  - Context: Make sure page file isn't too low for what ComfyUI is handling when experiencing performance issues
  - *From: JohnDopamine*


## News & Updates

- **VitPose separated pose detection and drawing with new options**
  - Don't have to detect again when changing drawing parameters
  - *From: Kijai*

- **ComfyUI now has native workflow template**
  - Latest ComfyUI update includes template for native Wan workflow
  - *From: zelgo_*

- **Index team updated Anisora LoRA to V3.2**
  - Adapted to work with Wan 2.2
  - *From: DawnII*

- **Kijai resized relight lora from 1.44GB to 273MB with no visible difference**
  - Resized from 128 to dynamic 22
  - *From: Kijai*

- **Anisora V3.2 released - trained on Wan2.2, can reduce inference steps to 8**
  - Total 110GB model, same as Wan 2.2 just fp32
  - *From: asd*

- **Kijai released Anisora V3.2 fp8 scaled models for high and low noise**
  - Available on HuggingFace in fp8_e4m3fn_scaled format
  - *From: Kijai*

- **ComfyUI memory leak fix merged to master**
  - Fix memory leak by properly detaching model finalizer committed 38 minutes ago
  - *From: JohnDopamine*

- **HuMo longer generation model coming next month**
  - Alibaba mentioned version capable of longer generations releasing next month
  - *From: Kijai*

- **WanAnimate can work without face input**
  - Latest commit should be able to work without face input
  - *From: DawnII*

- **New channel created to avoid 2.5 speculation discussions**
  - Separate wan_comfyui channel created to focus on technical discussions
  - *From: Kijai*

- **New Lightning LoRA released**
  - Wan2.2-T2V-A14B-4steps-lora-250928 released on HuggingFace
  - *From: 🦙rishappi*

- **AniSora 3.2 uses 8 steps cfg 1.0**
  - Latest AniSora release is distilled for much faster generation
  - *From: Kijai*

- **Seedance added first-last frame to PRO version**
  - First-last frame functionality that was in lite version has been added to PRO
  - *From: Draken*

- **New WanAnimate preprocessor separates pose detection and drawing**
  - Updated preprocessor allows adjusting drawing parameters without re-running detection
  - *From: Kijai*

- **HuMo long generation model in development**
  - They said they have long gen model in the works and aiming to release this month
  - *From: Kijai*

- **New WanAnimate fp8 v2 model released**
  - Works properly in native ComfyUI, fixes grid noise pattern issue, uses slightly less VRAM than v1
  - *From: Kijai*

- **WanAnimate V2 released**
  - Bug fix for native workflows, resolves noise grid issues but slightly lower quality than V1 for wrapper users
  - *From: Kijai*

- **New Ovi model from Character AI based on Wan**
  - Interesting for audio capabilities, better than basic mmaudio, but quality not immediately useful
  - *From: seitanism*

- **Lynx implementation being worked on**
  - Kijai working on wrapping up Lynx, separating full ref and IP layers for loading flexibility
  - *From: Kijai*

- **Lynx face ID system released**
  - New face identity preservation system for WAN models, works with T2V and I2V
  - *From: Kijai*

- **OVI (audio+video) model working in ComfyUI**
  - Joint video+audio generation model now functional, 5B parameters, 24fps output
  - *From: Kijai*

- **Lynx GGUF quantized versions available**
  - Q2_K, Q3_K_M, Q4_K_M, Q8_0 versions created and tested successfully
  - *From: patientx*

- **Kijai released fp8_scaled and bf16 versions of OVI models**
  - Available on HuggingFace with .safetensors versions of VAE
  - *From: Kijai*

- **Fixed EasyCache for OVI**
  - Cache system now works with OVI, skips audio latent when video is skipped
  - *From: Kijai*

- **Added audio latent length control node**
  - New node allows experimenting with different audio latent lengths
  - *From: Kijai*

- **Ovi branch will be merged into main eventually**
  - Currently in testing phase, needs more testing to ensure no workflow breaks
  - *From: Kijai*

- **New 2.2 tiny VAE available**
  - Useful with Ovi, finally added support
  - *From: Kijai*

- **rCM LoRAs extracted and available**
  - Available on HuggingFace Kijai/WanVideo_comfy repo
  - *From: Kijai*

- **RCM model from NVlabs available**
  - Model based on Wan2.1 t2v, requires custom implementation
  - *From: JohnDopamine*

- **New I2V lora released for Wan 2.2**
  - Better than previous version: Wan_2_2_I2V_A14B_HIGH_lightx2v_MoE_distill_lora_rank_64_bf16.safetensors
  - *From: Kijai*

- **FlashVSR implementation added**
  - One-step diffusion-based video super-resolution framework
  - *From: Kijai*

- **ComfyUI cancel button improvement committed**
  - ModelPatchFastTerminate functionality being implemented natively
  - *From: JohnDopamine*

- **NVidia pulled rCM from public**
  - License remains free to use but repo taken down
  - *From: JohnDopamine*

- **Representation Autoencoders (RAE) paper released**
  - Potentially the end of VAEs, making big waves on Twitter
  - *From: JohnDopamine*

- **FlashVSR support added to WanVideoWrapper**
  - New upscaling capability with strength control and 1-step processing
  - *From: Kijai*

- **Updated wrapper to truncate with num_frames and do padding on input**
  - To not miss any frames during processing
  - *From: Kijai*

- **Triton-windows 3.5.0 released**
  - Fixes fp8e4nv support for 30xx cards
  - *From: Kijai*

- **LightX2V released native fp8 ComfyUI models**
  - No longer need separate LoRA, models have LightX2V integrated directly
  - *From: hicho*

- **ComfyUI fixes for torch compile issues merged**
  - Workarounds for cancellation calls and compile disable on problematic code merged to main
  - *From: Kijai*

- **Torch 2.9 released with Wan VAE fixes**
  - Requires latest ComfyUI version to work properly with new torch version
  - *From: Kijai*

- **SageAttention v2.2.0-windows.post4 released**
  - Latest release available at GitHub, provides performance improvements
  - *From: hicho*

- **Triton updated to version 3.5**
  - Latest Triton version used for testing new SageAttention compile compatibility
  - *From: Kijai*

- **MoCha model released with PR support for wrapper**
  - Orange-3DV team released MoCha model with character replacement, lighting control, and made PR for wrapper integration
  - *From: Kijai*

- **Sage attention compiled option added to wrapper**
  - New option available for compiled sage attention
  - *From: blake37*

- **LongGen release upcoming for HuMo**
  - Community waiting for LongGen release for HuMo model
  - *From: mightynice*

- **Krea Realtime model open sourced**
  - Real-time video-to-video model now available as open source
  - *From: Juampab12*

- **Mocha open sourced**
  - Similar to Wan Animate but doesn't need pose detection
  - *From: Juampab12*

- **Wan VACE Ditto released**
  - VACE variant that doesn't require controlnet, works with image input for video style transfer
  - *From: hicho*

- **LongCat model available in separate branch**
  - LongCat (13.6B model, 15fps) is available in longcat branch of WanVideoWrapper
  - *From: Kijai*

- **MochaEmbeds node available in main branch**
  - MochaEmbeds node has been available in main branch of wrapper for a while
  - *From: Kijai*

- **OVI integrated in main ComfyUI branch**
  - OVI (lipsyncing tool) is now integrated in the main ComfyUI branch
  - *From: Kijai*

- **New LightX2V i2v models released**
  - Updated i2v models from LightX2V team fixing some issues
  - *From: hicho*

- **ComfyUI RAM pressure cache system merged**
  - PR 10454 implementing cache sensitive to RAM pressure with automatic eviction of expensive nodes
  - *From: JohnDopamine*

- **New ComfyUI launch flags for memory optimization**
  - --fast pinned_memory flag for faster weight offloading, though may cause crashes
  - *From: JohnDopamine*

- **HuMo i2v model patcher node added**
  - Added to ComfyUI-WanVaceAdvanced repo for embedded mask manipulation
  - *From: Ablejones*

- **LongCat support added to wrapper release version**
  - LongCat functionality is now available in the main wrapper release
  - *From: Juan Gea*

- **LightVAE released for WAN 2.2**
  - Much faster VAE decoding but with quality loss - good for testing, can always decode with full quality later
  - *From: Kijai*

- **Lucy Edit got updated on ComfyUI**
  - New version available on HuggingFace
  - *From: hicho*

- **InfinityStar model released**
  - Claims to make 10-second videos, has small VAE and not large CLIP like Qwen VL
  - *From: hicho*

- **WanExperiments repo released**
  - New custom nodes for WanEx I2VCustomEmbeds, HuMo I2V patches, and Bindweave implementation
  - *From: Ablejones*

- **Functional PR for multi/inf talk in native**
  - Kijai has a working pull request for these features
  - *From: Kijai*

- **HuMo team didn't start training long generation model**
  - They're building new dataset to train new model, long gen release delayed from October
  - *From: Kijai*

- **SVI working on new svi-shot version to overcome reference frame limitation**
  - Mentioned 3 weeks ago, addresses bias toward reference frame positioning
  - *From: Ablejones*

- **Ablejones published WanExperiments pack for native HuMo i2v workflows**
  - Enables running HuMo with i2v in native workflows
  - *From: Ablejones*

- **TimeToMove node released for video-to-video processing**
  - New node that allows using reference video to influence motion generation, available in wrapper example workflows
  - *From: lemuet*

- **HuMo sampler fix available**
  - Patch available to fix first frame duplication and missing frames issue
  - *From: Chandler ✨ 🎈*

- **Kijai has PR for context windows with Freenoise and multiple prompt support**
  - New branch adds Freenoise and multiple prompt support like in wrapper to native implementation
  - *From: Kijai*

- **Phantom/HuMo developer possibly picked up by ByteDance**
  - Original dev behind Phantom/HuMo may have joined ByteDance, Omni-Insert announced 2 months ago never released
  - *From: JohnDopamine*

- **Ablejones created fixed HuMo node supporting multiple references**
  - Added to WanExperiments pack - fixes native ComfyUI limitation of only using one reference image
  - *From: Ablejones*

- **Context windows fixes available in Kijai's branch**
  - Fixes available at https://github.com/kijai/ComfyUI/tree/contextwindows with options for latent index reuse and condition splitting
  - *From: Kijai*

- **New model Playmate2 released yesterday**
  - Another model option available
  - *From: Kijai*

- **Context windows PR is being tracked as draft**
  - Kijai's context windows implementation from wrapper being ported to native ComfyUI core
  - *From: Kijai*

- **Recent optimizations in ComfyUI core offloading**
  - Lot of work done optimizing offloading in comfy core, improvements made but work not finished yet
  - *From: Kijai*

- **Wan 2.2 has no connection to sampler/scheduler**
  - Discovery that fixing Humo flash via sampler/scheduler changes is pointless
  - *From: Gleb Tretyak*

- **Kijai's wrapper now accepts combined I2V and HuMo embeds**
  - Recent commits allow combining output from WanVideo ImageToVideo Encode and HuMo Embeds using a combine embeds node
  - *From: 42hub*

- **WanMove node merged into ComfyUI nightly**
  - Native WanMove node is now available in ComfyUI nightly builds via git pull
  - *From: Kijai*

- **Custom slicing of context windows merged into ComfyUI**
  - GitHub commit 77b2f7c228a0db6643bb7f29be4db0bff6799db2, enables context windows with Vace and Phantom
  - *From: Ablejones*

- **New WASWanExposureStabilizer node released**
  - Helps correct exposure gain at beginning of frame batches and exposure loss at end
  - *From: WAS*

- **SCAIL audio nodes updated with AIST dataset dance moves**
  - Added real dance moves from dataset, fixed scaling issues
  - *From: Chandler ✨ 🎈*

- **Wan 2.5/2.6 remain commercial models**
  - Despite pre-release hints about open sourcing, Wan 2.5 never became open source, 2.6 coming soon but also commercial
  - *From: 42hub*

- **KJNodes Conditioning Combine Multi node bug fixed**
  - Node was concatenating conditionings in reverse order
  - *From: Kijai*

- **SCAIL draw faces bug fixed**
  - Draw faces option now applies to all subjects, not just main pose subject
  - *From: Kijai*

- **TurboDiffusion ComfyUI implementation available**
  - New implementation at github.com/anveshane/Comfyui_turbodiffusion
  - *From: Anchorite*

- **Kijai released SVI Pro node for native nodes**
  - For video extension with better continuity
  - *From: LukeG89*

- **HuMoveLora prototype version released**
  - Experimental LoRA for motion control
  - *From: Ablejones*

- **ComfyUI dynamic inputs should eliminate need for forced typing workarounds**
  - Kijai needs to rebuild lots of nodes with new functionality
  - *From: Kijai*

- **MOVA model released**
  - Audio DiT model from OpenMOSS-Team, only 2-3GB extra on top of Wan 2.2 14B, Apache 2.0 licensed, HuggingFace space coming soon
  - *From: Draken*

- **Kijai fixed WanVideoModel attribute error**
  - Fixed AttributeError in wrapper after ComfyUI updates
  - *From: Kijai*


## Workflows & Use Cases

- **Kontext + WanAnimate for character retargeting**
  - Use case: When reference character has different proportions than driving pose
  - *From: Kijai*

- **WanAnimate with VitPose and masking**
  - Use case: Character animation with pose control and face preservation
  - *From: Kijai*

- **Native conditioning with NAG using bridge node**
  - Use case: Using negative prompts with wrapper by connecting to bridge node first
  - *From: patientx*

- **Multi-sampler setup with Wan 2.2**
  - Use case: Using last 4-6 steps with low noise model after first sampler with WanAnimate
  - *From: Shubhooooo*

- **CFG scheduling with multiple samplers**
  - Use case: High CFG for motion in first steps, CFG 1 for speed in later steps
  - *From: Juan Gea*

- **Wan 2.2 H+L v2v method**
  - Use case: Pass high model output to low model via v2v with 0.35 denoise, 2 steps
  - *From: hicho*

- **WanAnimate + InfiniteTalk pipeline**
  - Use case: First WanAnimate for character animation, then InfiniteTalk for enhanced lip sync to audio
  - *From: PATATAJEC*

- **HuMo I2V continuation**
  - Use case: Modified HuMo to work as I2V while retaining audio conditioning for video extension
  - *From: Ablejones*

- **VACE last frame only control**
  - Use case: Control only the ending frame of generation, leave first frame empty
  - *From: Ablejones*

- **Lynx with VACE integration**
  - Use case: Face ID control with style transfer
  - *From: Kijai*

- **WanAnimate with inverted canny + pose**
  - Use case: Character animation with background movement
  - *From: A.I.Warper*

- **Infinitetalk with 2.2 workaround**
  - Use case: Lip sync with Wan 2.2 using only high model connection
  - *From: hicho*

- **Subject replacement with WanAnimate**
  - Use case: Character swapping with better consistency than VACE for simple swaps
  - *From: mdkb*

- **Using Scale image to total pixels node**
  - Use case: Models may be more concerned with megapixel range than specific resolutions
  - *From: the_darkwatarus_museum*

- **WanAnimate with block selection**
  - Use case: Using partial blocks (e.g., 0-15) with specific strengths to control character consistency while maintaining some motion
  - *From: Kijai*

- **HuMo + InfiniteTalk combination**
  - Use case: Mixing HuMo embeds with InfiniteTalk for longer generation, can use audio from either or both
  - *From: Juan Gea*

- **VACE for long video upscaling**
  - Use case: Using VACE with mask strength to denoise, processing video in 81-frame chunks with overlapping frames
  - *From: Ablejones*

- **VACE for seam repair in extended clips**
  - Use case: Fix jumps and blemishes at seam points in 32+ second clips using grey/white frame masking
  - *From: mdkb*

- **Batched long video generation**
  - Use case: Generate 81 frame batches, skip first 81 frames for next batch, stitch together with last frame carryover
  - *From: Charlie*

- **HUMO + InfiniteTalk mixed embeds**
  - Use case: Long form dialogue generation with better facial expressions and acting
  - *From: Juan Gea*

- **High noise to Low noise batch processing**
  - Use case: Pass batched outputs of high noise samplers through single low noise sampler for better I2V transitions
  - *From: DawnII*

- **Multi-model step workflow with 7 K-samplers**
  - Use case: Combining different models per step for motion/quality balance
  - *From: hicho*

- **Lynx + WanAnimate combination**
  - Use case: Face identity preservation with animation, better than Lynx alone
  - *From: DawnII*

- **Phantom + Lynx face-only workflow**
  - Use case: Character consistency with face padding in phantom embeds
  - *From: DawnII*

- **Converting existing 5B T2V/I2V workflows to OVI**
  - Use case: Adding audio generation to existing video workflows
  - *From: Kijai*

- **I2V implementation for OVI**
  - Use case: Image to video with audio generation (not fully implemented yet)
  - *From: Kijai*

- **Context options selective usage**
  - Use case: Use context options for first 2 high noise steps, then disable for remaining steps
  - *From: Cseti*

- **Lynx+VACE+PUSA combination**
  - Use case: Face swap morphing effects
  - *From: yukass*

- **OVI autoqueues middle runs for long audio**
  - Use case: Automatically handles full song generation, if last run is less than 16 groups need to disable groups and run again
  - *From: VRGameDevGirl84(RTX 5090)*

- **Use Ovi + one step InfiniteTalk to clean up**
  - Use case: Single step already cleans up OVI output nicely
  - *From: Kijai*

- **Video Aspect Ratio Expander**
  - Use case: Workflow being developed for expanding video aspect ratios
  - *From: yo9o*

- **FlashVSR upscaling workflow**
  - Use case: Fast 1-step video upscaling from low quality inputs
  - *From: Kijai*

- **Multi-step FlashVSR using 2 samplers**
  - Use case: Better quality results using split step processing with different seeds
  - *From: Mngbg*

- **FlashVSR batch processing for long videos**
  - Use case: Process long videos by looping through segments
  - *From: Kijai*

- **1280x720x81 generation on RTX 3090**
  - Use case: Video generation with optimizations for 24GB VRAM
  - *From: BestWind*

- **T2V then I2V for longer videos**
  - Use case: For generating videos longer than 5 seconds with Wan 2.2 - do T2V first, then use last frame for I2V extension
  - *From: hicho*

- **Batch long video generation with 2 KSamplers**
  - Use case: Generate 80+80 frame videos using 2 KSamplers and image merge to combine outputs
  - *From: hicho*

- **Multi-stage upscaling pipeline**
  - Use case: Low-res inference -> FlashVSR to mid-res -> final upscale with other techniques for production quality
  - *From: Juan Gea*

- **VACE T2V distill with LoRA effects**
  - Use case: Setup VACE module with T2V distill natively, using LoRA effects and character LoRAs with Wan VACE depth
  - *From: hicho*

- **Dynamic video outpaint workflow shared**
  - Use case: Video outpainting with dynamic control
  - *From: yo9o*

- **Complex extension workflow using HuMo and InfiniteTalk**
  - Use case: Generate with HuMo 97 frames, extend with InfiniteTalk, V2V on new frames, stitch back
  - *From: Ablejones*

- **I2V with reference latents for context windows**
  - Use case: Using series of images as starting frames for each context window to maintain consistency across long generations
  - *From: blake37*

- **Character animation without face generation**
  - Use case: Remove background, use white background, disable mask input, disable relight LoRA, keep positive prompt empty
  - *From: Tachyon*

- **VACE keyframe animation with custom node**
  - Use case: Setting multiple keyframes within single video generation for animation
  - *From: lemuet*

- **Double VACE setup**
  - Use case: Using two VACE encoders - one for image reference at strength 1.0, another for video frames at lower strength
  - *From: VK*

- **Enhanced Wan2.2 AIO Infinite Video workflow**
  - Use case: Longer video generation with reduced artifacts using chained approach
  - *From: GalaxyTimeMachine*

- **HuMo dialogue replacement with inpainting**
  - Use case: Adding dialogue to characters in scenes using SVI film for segment stitching
  - *From: Ablejones*

- **Two-stage generation for difficult shots**
  - Use case: Generate with 2.2 using pose controls, then V2V with HuMo/InfiniteTalk for lip sync
  - *From: Juan Gea*

- **Using wrapper decode with native workflows**
  - Use case: Enables partial sampling and switching models mid-sampling
  - *From: Ablejones*

- **T2V with character LoRAs using Wild Prompter node**
  - Use case: Creating styled generations from WAN site examples in ComfyUI
  - *From: hicho*

- **HuMo with SVI-film LoRA for lipsync**
  - Use case: Audio-driven talking head generation with film-style processing
  - *From: Ablejones*

- **LongCat for extended video generation**
  - Use case: 28-second seamless coherent video generation, can do 1280x768 directly without upscaling
  - *From: Juan Gea*

- **Two-pass upscaling: 480p then 720p with refine LoRA**
  - Use case: Official way for 720p: first generate 480p, upscale to 720p, then vid2vid with refine LoRA for 5 steps at low denoise (50 steps, start 45)
  - *From: Kijai*

- **HuMo vid2vid with denoise 0.5-0.6**
  - Use case: Changing words coming out of someone's mouth, use higher denoise for more changes
  - *From: Ablejones*

- **Crop-denoise-paste technique for face inpainting**
  - Use case: Crop face to high resolution, denoise with HuMo, paste back to original video
  - *From: Ablejones*

- **SVI-shot continuation with custom nodes**
  - Use case: Video extension with reduced degradation using WanExperiments nodes
  - *From: Ablejones*

- **Multi-pass Wan 2.2 + HuMo for lip sync**
  - Use case: Adding lip sync to existing videos or creating face swap with lip sync
  - *From: VRGameDevGirl84(RTX 5090)*

- **Native Bindweave with position swapping**
  - Use case: Reliable subject positioning in generated videos
  - *From: Ablejones*

- **VACE start/end frame with wrapper I2V**
  - Use case: Create batches and masks for multi-frame reference in wrapper workflows
  - *From: Kijai*

- **Custom sigmas with high shift for morph retention**
  - Use case: Preventing morphing transitions from turning into fades
  - *From: ingi // SYSTMS*

- **Two-pass generation with any model + HuMo**
  - Use case: Use any model (T2V+VACE, WanAnimate, Magref) as first pass, then HuMo as second pass for lip sync and refinement
  - *From: VRGameDevGirl84(RTX 5090)*

- **FML (First Middle Middle Last) frame workflow with Wan2.2 + HuMo**
  - Use case: Create morphing sequences by using last frame of previous generation as first frame of next
  - *From: VRGameDevGirl84(RTX 5090)*

- **VACE interpolation with Pad Image Batch Interleaved**
  - Use case: Frame interpolation by inserting empty frames between keyframes and using masks
  - *From: lemuet*

- **TimeToMove with frame blending for animation**
  - Use case: Video-to-video processing using reference motion from blended keyframes
  - *From: lemuet*

- **Wan FML (First, Middle, Last Frame) node workflow**
  - Use case: Video generation with specific frame constraints
  - *From: atom.p*

- **I2V upscaling without VACE using reference image and rough animation**
  - Use case: Refining low quality video while keeping character likeness
  - *From: lemuet*

- **VACE inpainting with baked masks and multiple controls**
  - Use case: Inpainting specific parts of video while maintaining pose/structure
  - *From: Juan Gea*

- **HuMo extension with frame overlap**
  - Use case: Extending HuMo generations by discarding first frames and using 5-frame overlap, replacing corrupted start frames with clean end frames
  - *From: Ablejones*

- **Separated conditioning for HuMo flash mitigation**
  - Use case: Provide FF2LF embeds only to HN and HuMo embeds only to LN to reduce flash artifacts
  - *From: Gleb Tretyak*

- **HuMo with context windows for long generation**
  - Use case: 30+ second coherent videos with lip sync and character consistency
  - *From: Ablejones*

- **HuMo + multiple reference images**
  - Use case: Better character consistency and scene control using up to 4 reference images
  - *From: VRGameDevGirl84*

- **Context windows + uni3c for camera lock**
  - Use case: Long HuMo generation with stable camera movement
  - *From: Kijai*

- **Three-stage sampling: 2.2 HN + HuMo LN + inpainting**
  - Use case: Getting better motion from 2.2 while maintaining HuMo character consistency and lip sync
  - *From: Ablejones*

- **Long video generation with overlapping frames**
  - Use case: Creating videos longer than 5 seconds by feeding last 5 frames of previous generation into next i2v generation
  - *From: Ablejones*

- **VACE control slicing with context windows**
  - Use case: Very long video generation with VACE control, though causes character drift without reference frames
  - *From: Ablejones*

- **Two-stage HuMo with different context window settings**
  - Use case: Attempting to reduce scene transitions by varying window sizes and overlap between sampler stages
  - *From: Ablejones*

- **3-sampler chain for improved motion**
  - Use case: 1-3 steps without LightX, then high noise with LightX, then low noise - improves motion and character consistency
  - *From: garbus*

- **Audio-reactive WanMove with pose detection**
  - Use case: Generating trajectory paths with audio modulation and pose keypoint detection for dynamic character movement
  - *From: Chandler ✨ 🎈*

- **Multi-image ref with HuMo Low continuation**
  - Use case: Using multi-image reference Wan 2.2 high with HuMo low for character consistency
  - *From: Chandler ✨ 🎈*

- **Context windowing with VACE for inpainting**
  - Use case: Using VACE to mask background of existing video for inpainting prevents background changes during context windowing
  - *From: Ablejones*

- **Context windows with VACE using WanVaceAdvanced nodes**
  - Use case: Using context windows with Vace and includes latent noise mask with multiple samplers
  - *From: Ablejones*

- **Vace + Phantom for subject consistency**
  - Use case: Best approach for handling rotating subjects that show multiple angles
  - *From: Ablejones*

- **SCAIL with multiple models chaining**
  - Use case: Move for dancing, SCAIL for background effects, then Humo for lipsync
  - *From: Chandler ✨ 🎈*

- **Crop-uncrop with animated masks**
  - Use case: Extract subject, refine with higher resolution, paste back for better quality
  - *From: uff*

- **Automated Wan2.2 FMML workflow with GPT story generation**
  - Use case: Creates 4 images using zimage from LLM-generated prompts, then processes through video generation
  - *From: VRGameDevGirl84(RTX 5090)*

- **Mobile monitoring portal with Discord alerts**
  - Use case: Monitor generations from phone, get alerts when new content generated, run workflows remotely
  - *From: boorayjenkins*

- **For loop batch processing**
  - Use case: Process multiple prompts and images through video generation automatically
  - *From: Gateway {Dreaming Computers}*

- **VACE continuation for long videos**
  - Use case: 16 frames from end of first video + 17 frames generated by VACE + 16 frames from beginning of second video
  - *From: NodeMancer*

- **SVI Pro extension workflow**
  - Use case: Video extension with frame anchoring and smooth continuations
  - *From: LukeG89*

- **VACE interpolation for frame rate doubling**
  - Use case: Space out frames so every other frame is from video, rest are gray with matching mask
  - *From: ingi // SYSTMS*

- **First-frame-last-frame for video extension**
  - Use case: Extending videos beyond 5 seconds, though can cause flickering and color changes
  - *From: kaibioinfo*

- **SVI 2.0 Pro**
  - Use case: Video extension workflow, though complex with many dependencies
  - *From: sir_AXE (Eugene)*

- **Wan VACE for vid2vid**
  - Use case: Video-to-video conversion that keeps background consistent
  - *From: Godhand*


## Recommended Settings

- **hand_stick_width**: -1
  - Disables hand detection in VitPose when hands are problematic
  - *From: Kijai*

- **face_strength**: 1.0
  - Values under 1.0 can cause black rectangle artifacts
  - *From: Kijai*

- **cfg_schedule**: >1 for first step only
  - Adds about 20% generation time but improves quality
  - *From: seitanism*

- **quantization**: fp8_e5m2
  - Better compatibility with RTX 3000/AMD when using torch.compile
  - *From: patientx*

- **sampler**: dmp++_sde or res4lyfe
  - Work best for WanAnimate, euler-simple gives lighter colors with more movement
  - *From: Neex*

- **denoise**: 1.0
  - Don't need to touch denoise for multi-sampler setup, leave at default
  - *From: Kijai*

- **frame_window_size**: equal to num_frames
  - To deactivate built-in looping when using multiple samplers
  - *From: Kijai*

- **retarget_padding**: 0
  - 0 uses original code with no scaling, >0 activates bounded crop
  - *From: Kijai*

- **blocks**: 40
  - WanAnimate has 40 blocks to swap, just slightly bigger blocks
  - *From: Kijai*

- **Wan 2.2 low noise steps**: 4+4 steps with 0.35 denoise
  - For good quality when using as second pass after high model
  - *From: hicho*

- **Anisora v3.2 steps**: 3+4 steps, cfg 1
  - Distillation is baked in, works without additional loras
  - *From: DawnII*

- **InfiniteTalk v2v settings**: 7 steps starting from 5th step
  - Alternative to denoise method for better control
  - *From: PATATAJEC*

- **Resolution sweet spot**: 1280x720
  - Good balance of quality and VRAM usage, takes about 64GB VRAM
  - *From: ReDiff*

- **AniSora 3.2 cfg**: 1.0
  - Distilled for cfg 1.0 operation
  - *From: DawnII*

- **AniSora 3.2 steps**: 8
  - Optimized for 8-step generation
  - *From: Kijai*

- **Context frames for 2.2**: 81 for most cases
  - Related only to frame count the model can do well
  - *From: Kijai*

- **Anisora LoRA strength**: 0.5 for animate, 1.5 for rotation effects
  - Different strengths produce different effects
  - *From: Shubhooooo*

- **Pose strength**: 0.5
  - Better consistency when doing difficult character swaps
  - *From: piscesbody*

- **Face strength**: 0.4-0.7
  - Range for balancing consistency vs subject following
  - *From: piscesbody*

- **Shift parameter**: 8.0 instead of 3.0
  - Diffusers uses 3.0 default for 480P but 8.0 may produce better results
  - *From: Kijai*

- **Steps for pose detection**: 1-2 seconds for 81 frames
  - Expected performance on 4090 with latest onnx and onnxruntime-gpu
  - *From: Kijai*

- **WanAnimate blocks**: 0-15 for good results without overexposure
  - Blocks 0-15 yield nice results, main issue is hair overexposure
  - *From: 42hub*

- **WanAnimate strength with start percentage**: 0.5 start percent with various strengths
  - Allows better prompt following and motion while maintaining likeness
  - *From: Hashu*

- **Uni3c with Wan 2.2**: Works for pans and zooms, not optimal for rotation
  - Uni3c not meant for 2.2, needs compatible version for camera rotation
  - *From: xwsswww*

- **Denoise for sigma scheduling**: Start at lower value like 0.8 instead of 1.0
  - Starts at 80% noise instead of 100%, preserves some original image essence
  - *From: Ablejones*

- **Context window frames**: 81 frames
  - Good balance for quality without excessive VRAM usage
  - *From: Charlie*

- **Steps for quality vs speed**: 4 steps
  - No significant quality hit compared to 8 steps, much faster
  - *From: Charlie*

- **LightX2V + FastWan LoRA strength**: 1.00
  - Used in speed testing workflow
  - *From: VRGameDevGirl84(RTX 5090)*

- **FPS for HUMO**: 25 fps recommended
  - Standard recommendation, though some suspect audio drift issues may relate to fps mismatch
  - *From: Juan Gea*

- **Lynx reference strength**: 0.6
  - Good balance, 1.0+ too strong, creates artifacts
  - *From: Kijai*

- **Steps for Lynx**: 4 with dpm++_sde, 6 with LCM
  - LCM burns less VRAM and more natural
  - *From: Kijai*

- **CFG for OVI with FastWAN LoRA**: 1.0
  - Works well for 10 steps generation
  - *From: Kijai*

- **Split point for LightX2V**: 5 out of 10 steps
  - For testing different model combinations
  - *From: Dream Making*

- **SLG**: 7,8,9 for video, 11 for blocks
  - Default values, can experiment with others
  - *From: Kijai*

- **CFG**: 3 for video, 2 for audio
  - Good balance for quality
  - *From: Kijai*

- **Audio CFG**: 5
  - Helps with audio quality issues
  - *From: Thom293*

- **Base precision**: bf16
  - fp16 causes Nans and corrupted results
  - *From: Kijai*

- **Steps for audio**: 40+ recommended
  - Audio model doesn't get distillation so needs more steps than FastWAN's 10
  - *From: Kijai*

- **Block swap**: 1 or higher
  - Faster than bypassing block swap, reduces VRAM usage
  - *From: slmonker(5090D 32GB)*

- **Audio CFG**: 3
  - Used with video CFG 4 and 50 steps
  - *From: Vérole*

- **LightX strength**: 1 instead of 1.2
  - Fixes overlighting issues in specific cases
  - *From: Juampab12*

- **Fastwan steps**: 10 steps with no CFG
  - Sometimes works fine, most of the time not
  - *From: Kijai*

- **Block swap**: 30 blocks full swap
  - Required for 6GB VRAM usage with fp8 models
  - *From: Kijai*

- **OVI audio CFG**: 4.5
  - Same as used in mmaudio, improves results
  - *From: U̷r̷a̷b̷e̷w̷e̷*

- **InfiniteTalk audio_scale**: 1.7
  - Good balance for emoting without too much degradation
  - *From: Canin17*

- **Steps without distill lora**: 40 minimum
  - Need more steps when not using distill loras
  - *From: ˗ˏˋ⚡ˎˊ-*

- **CFG without distill**: 3-5
  - Good range for non-distill workflows
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Shift without distill**: 5-12
  - Good range for non-distill workflows
  - *From: ˗ˏˋ⚡ˎˊ-*

- **FlashVSR strength**: 0.8
  - Reduces oversharpening while maintaining quality
  - *From: Kijai*

- **FlashVSR strength for subtle processing**: 0.6
  - For users who find 0.8 still too sharp
  - *From: mdkb*

- **Context window frames**: 48
  - Reduces VRAM usage compared to full 85 frames
  - *From: PATATAJEC*

- **FlashVSR steps**: 1
  - Designed for single step processing for speed
  - *From: Kijai*

- **torch compile cache size limit**: 128 (up from default 64)
  - Prevents hitting recompile limit that causes OOM
  - *From: Kijai*

- **--reserve-vram**: 2
  - Reserves VRAM for Windows display when using same GPU
  - *From: Kijai*

- **force_static_shapes**: false
  - New parameter in torch compile node to reduce recompilation issues
  - *From: BestWind*

- **FlashVSR strength**: Reduce from default
  - Helps with over-sharpening issues
  - *From: Kijai*

- **Wan resolution requirements**: Multiples of 16
  - Wan expects height and width to be divisible by 16, not 32
  - *From: Ashtar*

- **CFG for T2V comparison**: 5.0
  - Used in basic T2V comparison with 50 steps in fp16
  - *From: Kijai*

- **Scale factor for fast testing**: 0.15 or 0.20
  - Allows fast testing with less VRAM for people with limited hardware
  - *From: hicho*

- **Dynamic in torch compile**: false
  - Prevents cl.exe errors on Windows systems
  - *From: BestWind*

- **force_offload**: true
  - Ensures memory is freed after sampler finishes
  - *From: Kijai*

- **MoCha frames at 832x480**: 81 frames, 6 steps
  - Used 15.6GB max memory with full block swap
  - *From: Kijai*

- **Divisible by**: 32
  - Required for latent space with portrait resolutions, 16 may not work
  - *From: Kijai*

- **Face strength**: 0
  - To prevent face generation in character animations, may need to disable LoRA entirely
  - *From: AR*

- **Steps with LightX disabled**: 20
  - Provides good quality when not using distill LoRAs
  - *From: AR*

- **Positive prompt**: empty
  - Better character consistency, especially for non-human characters
  - *From: Charlie*

- **Steps without LightX**: At least 20
  - LightX allows 4 steps, but without it you need minimum 20 steps
  - *From: Charlie*

- **CFG for WAN**: 2 to 3.5
  - Recommended CFG range for good results
  - *From: Tachyon*

- **CFG for high/low noise**: High: 3.5-4, Low: 2.5
  - Higher CFG on high noise for better prompt adherence, lower on low to prevent face degradation
  - *From: Lumifel*

- **Shift parameter**: 5 to 8, with 8 working fine
  - Recommended shift range for good results
  - *From: Lumifel*

- **VACE strength for animation**: Around 0.85
  - Sweet spot between motion quality and likeness preservation
  - *From: GWX-Reloaded*

- **VACE strength per step**: ref strength 1, depth 0.3, pose 0.4
  - Better motion when using reference image in vid to vid for 2.2 high
  - *From: JalenBrunson*

- **LightX2V LoRA strength**: 0.25
  - Maintains speed on low noise while preserving quality
  - *From: mdkb*

- **Block swap adjustment for unmerged LoRAs**: Few blocks more than before
  - LoRA weights now attached to blocks, using more VRAM than before
  - *From: Kijai*

- **CFG for lightning LoRAs**: CFG=2 for both high and low, with skimmed CFG=1
  - Works well with 1030 high at strength 1, 1022 low at strength 1
  - *From: dipstik*

- **Steps for lightning LoRAs**: 2+2 steps with LCM/beta scheduler
  - Provides decent results with 1030 lightning LoRAs
  - *From: dipstik*

- **Shift parameter**: 8 for shift
  - Works with lightning LoRA setup
  - *From: dipstik*

- **LoRA strengths for combined setup**: 1030 high at 2, FastWan at 1, MPS high at 0.5
  - Good results when using only with High model
  - *From: Elvaxorn*

- **LongCat frame reduction**: 80 frames per sequence instead of default
  - Allows fitting 1280x768 resolution within VRAM limits
  - *From: Juan Gea*

- **overlap frames for SVI-shot**: 1
  - Designed for single frame overlap
  - *From: Ablejones*

- **overlap frames for SVI-film**: 5
  - Trained for 5 frame overlap
  - *From: Ablejones*

- **denoise for HuMo vid2vid**: 0.5-0.6
  - Good balance for changing mouth movements
  - *From: Ablejones*

- **shift value for still images**: 2 or 3
  - Better quality for single frame generation
  - *From: ingi // SYSTMS*

- **minimum steps for most samplers**: 5
  - Most samplers need 5 steps minimum unless using custom sigmas
  - *From: Kijai*

- **HuMo max frames**: 97
  - Can push HuMo model to 97 frames with higher resolution
  - *From: Ablejones*

- **HuMo frames**: 81 frames at 24 fps
  - Trained specification, more reliable for preventing lip sync issues
  - *From: Ablejones*

- **HuMo denoise for lip sync injection**: 0.5 or 0.6
  - Sufficient for lip sync without over-processing
  - *From: Ablejones*

- **Custom sigma shift**: 50
  - Keeps generation in 1-0.875 timestep range for TREAD-trained LoRAs
  - *From: ingi // SYSTMS*

- **Sigma curve for shift 3.0/8 steps**: [1.0, 0.955, 0.90, 0.833, 0.75, 0.643, 0.5, 0.3]
  - Reference curve normalized to 1.0 as highest value
  - *From: ˗ˏˋ⚡ˎˊ-*

- **DPM++ sampler steps**: At least 15 steps
  - DPM++ needs minimum steps, not meant for distills
  - *From: ˗ˏˋ⚡ˎˊ-*

- **shift**: 4
  - Helps reduce HuMo flashing when decreased from default
  - *From: Gleb Tretyak*

- **steps**: 6
  - Increased from default helps with HuMo flash reduction
  - *From: Gleb Tretyak*

- **sampler/scheduler**: dpmpp_sde_2s/beta57
  - Strong sampler/scheduler combination helps with quality
  - *From: Gleb Tretyak*

- **VAE precision**: fp32
  - Better quality results than default precision
  - *From: Gleb Tretyak*

- **eta**: 1.0
  - Part of sampler settings for HuMo fix
  - *From: Gleb Tretyak*

- **Resolution for I2V workflows**: 1088x720
  - Works well for detailed generation, can be adjusted as needed
  - *From: lemuet*

- **Mask growth for VACE inpainting**: 5 pixels
  - Added before sending input for control masks to improve blending
  - *From: Ablejones*

- **Frame generation limit**: 81 frames instead of 113
  - 113 frames is more than people usually generate in one batch with Wan 2.2 14B
  - *From: 42hub*

- **denoise**: 0.6 or 0.7
  - Works best for Wan inpainting with latent noise mask
  - *From: Ablejones*

- **blockswap**: 40 blocks maximum
  - There are only 40 blocks available, setting higher doesn't help wrapper VRAM issues
  - *From: Kijai*

- **Context window overlap**: 50 (up from 30)
  - Better blending between context windows
  - *From: Ablejones*

- **Context window type**: standard_uniform with overlap-linear
  - Better performance than other context window types
  - *From: Ablejones*

- **--reserve-vram**: few gigabytes
  - Solves automatic VRAM estimation issues, especially on Windows
  - *From: Kijai*

- **CFG and steps for Wan animate matrix test**: 1 CFG, 6 steps
  - Standard test parameters for sampler/scheduler comparisons
  - *From: Gleb Tretyak*

- **Resolution and timing for tests**: 1280x720, ~2 seconds
  - Consistent test parameters with relight lora and lightx lora
  - *From: Gleb Tretyak*

- **Context window settings for first sampler**: 81 frames, 35 overlap
  - Working parameters for multi-stage sampling
  - *From: Chandler ✨ 🎈*

- **Context window settings for second sampler**: 97 frames, 45 overlap
  - Different window size for second stage, though effectiveness uncertain
  - *From: Chandler ✨ 🎈*

- **Wan model frame rates**: 16 fps for Wan2.1 and Wan2.2 A14 base models, 25 fps for HuMo
  - Training frame rates for different models
  - *From: Ablejones*

- **Reserve VRAM parameter**: --reserve-vram 2
  - Alternative to block swap node for VRAM management
  - *From: Kijai*

- **Frame recommendations for context windows**: 81 or 97 frames minimum
  - Lower frame counts can cause weird results
  - *From: Ablejones*

- **Shift value**: Same across all samplers in chain
  - Shift defines the schedule for entire sampling process, can't change mid-sampling
  - *From: Ablejones*

- **Shift for I2V**: Around 5
  - Lower shift leaves more time for detailing steps in I2V
  - *From: Ablejones*

- **MMAudio CFG**: 5.5
  - Higher CFG helps reduce unwanted sounds and improves coherence
  - *From: dj47*

- **Model sampling shift**: 8 for first, 5 for others
  - Prevents sigma schedule conflicts in chain sampling
  - *From: Ablejones*

- **LightX LoRA strength on first sampler**: 0.4-0.5
  - Lower strength allows using lower shift while avoiding large steps
  - *From: Ablejones*

- **lcm/simple HN, dpmpp_sde/sgm_uniform LN**: Good results for wan22 i2v
  - Tested configuration showing good results
  - *From: cephy*

- **SCAIL input dimensions**: Must be divisible by 32
  - 704 instead of 720, or 768
  - *From: Kijai*

- **Block swap amount for GGUF models**: Increase to 30
  - Prevents VRAM stalling
  - *From: Danial*

- **TTM steps configuration**: 6 total steps, split at 3, TTM skips first step
  - Default working configuration, 4 steps may not work well
  - *From: Kijai*

- **Pose end value**: 1.0
  - Helps with pose adherence (default is 0.5)
  - *From: Kijai*

- **WanMove LoRA strength on Wan 2.2 high**: Above 1.0 (like 2.2)
  - Wan 2.2 high needs higher strength, low needs 0.7 or 0.55
  - *From: Gleb Tretyak*

- **LoRA extraction rank**: 512
  - Higher rank may matter for better extraction quality
  - *From: Gleb Tretyak*

- **RMS norm mode**: pytorch
  - Get some speed boost without torch compile on pytorch 2.9+
  - *From: Kijai*

- **Block 0 alpha weight**: 0.0
  - Reduces unwanted behavior and artifacts in WanMove LoRA
  - *From: Ablejones*

- **Split sigmas**: For 8 total steps split at 3: 3 steps to high_sigmas, 5 to low_sigmas
  - Divides the steps between high and low noise models
  - *From: LukeG89*

- **Motion latent count**: 1 (recommended)
  - SVI 2.0 Pro was trained with 1 motion latent (4 frames)
  - *From: 42hub*

- **SCAIL detection frame rate**: Around 15fps
  - Prevents hard locking of PC
  - *From: devnullblackcat*

- **ComfyUI launch parameters**: Remove --fast and --use-sage-attention, add --disable-pinned-memory --reserve-vram 2
  - Prevents OOM issues and improves memory management
  - *From: JohnDopamine*


## Concepts Explained

- **Pose retargeting**: Adjusting pose proportions to match reference character dimensions, done automatically by VitPose in WanAnimate
  - *From: Kijai*

- **Mask block size**: WanAnimate uses block-based masking rather than pixel-perfect masks for easier generalization
  - *From: Kijai*

- **Sliding window extension**: WanAnimate automatically extends videos using 1-frame overlap between segments
  - *From: Kijai*

- **retarget_padding**: 0 = no scaling using original code, >0 = activates bounded crop. Not meant to be used with masking
  - *From: Kijai*

- **CFG scheduling**: Start with high CFG (3.5) for motion, then lower to 1. CFG needs 2nd pass through model so 1 step with CFG = 2 steps time-wise
  - *From: Kijai*

- **denoise vs start_step**: Denoise just adjusts start step - it's alternative way to set it. Better to use actual start_step with low steps
  - *From: Kijai*

- **V2V method**: Using denoise strength instead of start_step/end_step for model chaining
  - *From: hicho*

- **Differential diffusion**: Using latent masks to control which areas of the image get modified during generation
  - *From: Kijai*

- **Noise scheduling**: Amount of noise added is based on sigmas of skipped steps, imitating noise of sigma schedule to fool model
  - *From: Kijai*

- **MoE architecture High/Low noise split**: Wan 2.2 uses separate expert models for high and low noise, bypassing this loses benefits of 14B model
  - *From: DawnII*

- **Lynx reference adapter**: Runs one step through model with reference image first, similar to oldschool ref only approach
  - *From: Kijai*

- **Distilled models**: Models trained to achieve similar results with fewer steps and lower cfg values
  - *From: DawnII*

- **Set LoRAs stacking**: Multiple Set LoRA nodes stack their effects - if you set same LoRA with 0.5 strength twice, it becomes 1.0 total
  - *From: patientx*

- **CFG formula**: noise_pred = noise_pred_uncond + cfg_scale * (noise_pred_cond - noise_pred_uncond)
  - *From: Kijai*

- **Face adapter execution**: Native implementation doesn't execute face adapter at all if nothing is connected, unlike wrapper
  - *From: Ablejones*

- **Sigmas in diffusion**: Sigmas operate on step size, not just values. The value used in math is (current sigma) - (next sigma). Higher sigma means more noise, lower means less noise. Normal sampling goes from high to low
  - *From: Ablejones*

- **Denoise parameter behavior**: In wrapper/diffusers denoise sets the start step. In ComfyUI native it also increases max steps to match step count. Fundamentally changes how much noise you start with
  - *From: Kijai*

- **Unsampling**: When sigma values go up instead of down, it adds noise instead of removing it, which is called unsampling
  - *From: Ablejones*

- **Block swapping**: Memory optimization technique where weights don't need to fit GPU all at once, works for any architecture
  - *From: Kijai*

- **Embed mixing**: Combining embeddings from different models (like HUMO + InfiniteTalk) for improved results
  - *From: Juan Gea*

- **High noise vs Low noise models**: Dual model approach where high noise model has better prompt adherence, low noise refines output
  - *From: hicho*

- **Lynx system**: Face identity preservation system with IP adapter and reference adapter components, lite vs full versions
  - *From: Kijai*

- **MoE architecture split**: High/Low noise expert split in WAN 2.2, can use different models for different noise levels
  - *From: hicho*

- **Joint model sync**: OVI audio+video model requires sync at every step through shared cross attention
  - *From: Kijai*

- **Audio latent length**: Default is 157 for 31 latents (121 image frames), can be adjusted for different video lengths
  - *From: Kijai*

- **OVI prompt structure**: Must use <S> and <E> tags around speech, with <AUDCAP> and <ENDAUDCAP> for audio description
  - *From: Kijai*

- **Audio latent ratio**: Audio extension approximately 30+1 per 8 seconds of video, 248 audio latent for 193 frames
  - *From: patientx*

- **5 second audio limit**: Audio doesn't generate correctly after 157 latents or ~5 seconds, similar to other audio models
  - *From: patientx*

- **CFG above 1.0 is double compute**: Anything above 1.0 cfg doubles compute time, 1.0 or below is half the compute time
  - *From: Draken*

- **2.2 doesn't use img_emb layers**: Only 2.1 I2V model and loras have img_emb layers for clip vision embeds, 2.2 just doesn't use them (WanAnimate is exception)
  - *From: Kijai*

- **FlashVSR conditional decoder**: Tiny decoder that uses LR frames as auxiliary inputs in addition to latents for HR reconstruction
  - *From: mamad8*

- **Context options in FlashVSR**: Feature to process long videos in segments to manage memory usage
  - *From: BestWind*

- **torch.compile recompiles**: When torch encounters different tensor shapes or conditions, it recompiles the model. Too many recompiles hit a limit and cause memory issues
  - *From: Kijai*

- **triton cache**: Cached compilation files stored on disk that can grow over time and cause issues if corrupted
  - *From: Kijai*

- **Signal to noise ratio in video**: Better metric than resolution - measures how 'noisy' each frame is compared to useful signal. A 1280x720 file doesn't necessarily mean it was captured at that resolution
  - *From: Draken*

- **Diffusion model vs checkpoint separation**: Unlike SD1.5/SDXL checkpoints that bundled everything, Wan separates diffusion model, text encoder (CLIP), and VAE as individual components due to size constraints
  - *From: Ablejones*

- **Total pixel scaling**: Calculating resolution based on total pixel count while maintaining aspect ratio, useful for GPU VRAM limitations
  - *From: Ashtar*

- **NAG in InfiniteTalk**: Way to enable negative prompt when using CFG 1
  - *From: Juan Gea*

- **MoCha double compute**: Original frames concatenated along temporal dimension, requiring double the memory/compute
  - *From: Kijai*

- **Safetensors memory mapping**: Weights loaded only when actually used, not instantly loaded to memory
  - *From: Kijai*

- **Reference latents**: Feature allowing you to provide starting images converted to latents for each context window in I2V generation
  - *From: blake37*

- **Divisible by requirement**: Images must have dimensions divisible by specified number (16 or 32) due to latent space requirements in the model
  - *From: Kijai*

- **RCM (Wan VACE Ditto)**: VACE variant that can add style and effects to videos without needing controlnet, just uses image input
  - *From: hicho*

- **Context window artifacts**: Strong transition effects that appear in WAN Animation, causing degradation after third 77-frame iteration
  - *From: eraxor_*

- **Fun InP vs Fun Control**: Fun InP is for in-between frames (FFLF morphing), Fun Control is for ControlNet inputs like Canny, Depth, Pose
  - *From: Kijai*

- **Double VACE**: Using two VACE encoders - one for single image reference at high strength, another for video frames at lower strength for better control
  - *From: VK*

- **Latent Rescale**: Normalization scaling, not dimensional scaling. Native and wrapper do it at different times so node needed when using VAE from other implementation.
  - *From: Kijai*

- **Non-blocking block swap**: Setting that affects RAM usage - can cause crashes if insufficient RAM but provides performance benefits when working
  - *From: Kijai*

- **Pinned memory**: New ComfyUI feature behind --fast flag that increases RAM usage but speeds up operations, may cause crashes
  - *From: Ablejones*

- **VACE motion pickup**: VACE can detect and incorporate motion patterns from raw video when control images are gradually modified to include video content
  - *From: Phr00t*

- **Video latent burning**: Phenomenon where I2V outputs become overexposed or degraded when certain LoRAs like RCM are applied
  - *From: blake37*

- **Lightning LoRA combinations**: Using multiple lightning LoRAs (like 1030 and 1022) together with specific CFG and step settings for faster inference
  - *From: dipstik*

- **I2V latent channels**: T2V uses 16 channels for noise. I2V adds 20 more (36 total): channels 17-20 for mask, 21-36 for conditioning inputs
  - *From: Ablejones*

- **4*n+1 frame pattern**: Wan models work with latent frames that each encode 4 real frames plus 1 extra, so use frame counts like 49, 53, etc.
  - *From: 42hub*

- **VACE architecture**: Uses only 16 channels like T2V. VACE blocks are parallel set added to model that interact in complex ways
  - *From: Ablejones*

- **Phantom conditioning**: Adds reference image at end of regular noise latent, model understands this without extra blocks
  - *From: Ablejones*

- **SVI reference frame bias**: SVI-shot prefers the reference frame positioning, keeping subjects in similar poses/angles as the reference
  - *From: Ablejones*

- **Flash artifacts in HuMo**: Noise on first few frames that makes transitions noticeable when extending videos
  - *From: lemuet*

- **Motion amplitude in PainterI2V**: Unique parameter that augments empty frames with inverse of start image to force more motion
  - *From: Ablejones*

- **Distill model**: Specific LoRA model used in the low noise pass that significantly impacts quality and flashing issues
  - *From: Gleb Tretyak*

- **VACE conditioning**: System using input frames and masks as separate conditioning data for video generation, allows precise control over which frames to preserve or generate
  - *From: 42hub*

- **Latent space compression**: Wan compresses video by factor of 8 spatially and 4 temporally - helps understand tensor size errors
  - *From: Kijai*

- **Grid noise**: Artifacts caused when VAE encounters blurry latent data that's outside its training domain of normal sharp videos
  - *From: 42hub*

- **Mask polarity**: Whether white or black pixels represent the masked area - different between wrapper and native implementations
  - *From: Scruffy*

- **Denoise parameter**: In wrapper, denoise simply overrides start_step - denoise 0.8 with 10 steps means start at step 2
  - *From: 42hub*

- **4-frame latent block rule**: Unlike VACE where images can be inserted anywhere, I2V must respect 4+1 frames rule to avoid glitches like color shift or flashing
  - *From: lemuet*

- **fractional denoising**: Using denoise < 1.0 or starting at step > 0 in wrapper, partially obliterates input samples with correct amount of noise
  - *From: Ablejones*

- **channel masks**: Extra dimension added to mask tensors to store masks for each frame when converting from pixel to latent space, also called temporal masks
  - *From: Ablejones*

- **Context windows in latent space**: Context length refers to latent frames, not pixel frames. 16 context = 16 latents = 64 actual frames
  - *From: Kijai*

- **Reference latent padding issue**: When HuMo adds reference images, it changes frame count. Before fix, sampler padded front with noise causing confetti. After fix, pads tail which gets cut off
  - *From: Chandler*

- **PainterI2V motion amplification**: Single line of code that modifies empty i2v channel latents to squeeze in more motion, like making car drive more exciting by driving on slippery ice - more dynamic but less controlled
  - *From: Ablejones*

- **Context windows frame handling**: Wan context windows node uses real frames not latent frames. First frame is special in Wan, encoded differently than subsequent frames
  - *From: Ablejones*

- **Shared GPU memory problem**: When shared GPU memory usage goes over 5%, GPU waits 99% of time for CPU, causing extreme slowdowns
  - *From: Ablejones*

- **Differential diffusion**: Technique that converts blurred/feathered latent masks into series of increasing binary masks, simulating blur effect progressively
  - *From: Ablejones*

- **Latent noise mask**: Mask sent through latent line that tells model there is no noise in unmasked regions, applied before being sent to model
  - *From: Ablejones*

- **Context windowing vs extension methods**: Context windowing generates whole video at once, extension methods continue from last frames - fundamentally different approaches
  - *From: Kijai*

- **Sigma schedule consistency**: Schedule created on first sampler carries through to others, like planning a road trip route that can't be changed mid-journey
  - *From: Ablejones*

- **Z-Image trick with Normal Map and High Pass**: Enhancement process for second pass in MoE workflow, allows upscaling during same t2v pass
  - *From: WAS*

- **True MoE process**: Don't return left over noise on high, use add noise on low, enables Z-Image enhancement
  - *From: WAS*

- **SCAIL pose generation**: Creates skeleton for input image and moves it according to audio features like beat, bass, treble, mids and onset
  - *From: Chandler ✨ 🎈*

- **Context windows vs internal technique in WanAnimate**: Context windows won't degrade over time but has scene/background shift. Internal window won't shift much but degrades considerably after 3 extensions
  - *From: Juan Gea*

- **ONNX 4GB limit**: ONNX format has 4GB file size limit requiring model to be split into .onnx and .bin files
  - *From: Kijai*

- **Multi approach in conditioning nodes**: Has to be reversed due to how the combining works - explicit mechanism is more robust than dynamic input widgets
  - *From: Kijai*

- **Motion latent count logic**: 1 latent equals 4 frames plus 1, so motion latent count of 2 needs overlap of 9
  - *From: LukeG89*

- **Switchover levels**: The sigma at which you transition from high noise model to low noise model (0.9 for I2V, 0.875 for T2V)
  - *From: 42hub*

- **VACE continuation**: Using VACE to generate bridge sections between separately generated video clips
  - *From: NodeMancer*


## Resources & Links

- **VitPose Huge ONNX model** (model)
  - https://huggingface.co/Kijai/vitpose_comfy/tree/main/onnx
  - *From: Kijai*

- **Wan2.2 bf16 High/Low models** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/
  - *From: Kijai*

- **Sapiens pose detection** (repo)
  - https://github.com/smthemex/ComfyUI_Sapiens
  - *From: scf*

- **WanAnimate issue tracker** (repo)
  - https://github.com/kijai/ComfyUI-WanVideoWrapper/issues/1291
  - *From: Gleb Tretyak*

- **MoG-VFI interpolation** (repo)
  - https://github.com/MCG-NJU/MoG-VFI
  - *From: Gleb Tretyak*

- **Kijai's workflows** (repo)
  - https://github.com/kijai
  - *From: 🦙rishappi*

- **WanAnimate relight lora resized** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/blob/main/LoRAs/Wan22_relight/WanAnimate_relight_lora_fp16_resized_from_128_to_dynamic_22.safetensors
  - *From: Kijai*

- **ComfyUI-WanAnimatePreprocess** (repo)
  - https://github.com/kijai/ComfyUI-WanAnimatePreprocess
  - *From: Mak*

- **Anisora V3.2** (model)
  - https://huggingface.co/IndexTeam/Index-anisora/tree/main/V3.2
  - *From: asd*

- **Anisora V3.2 fp8 High Noise** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy_fp8_scaled/blob/main/I2V/AniSora/Wan2_2-I2V_AniSoraV3_2_HIGH_14B_fp8_e4m3fn_scaled_KJ.safetensors
  - *From: Kijai*

- **Anisora V3.2 fp8 Low Noise** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy_fp8_scaled/blob/main/I2V/AniSora/Wan2_2-I2V_AniSoraV3_2_LOW_14B_fp8_e4m3fn_scaled_KJ.safetensors
  - *From: Kijai*

- **ComfyUI-WanAnimatePreprocess** (repo)
  - https://github.com/kijai/ComfyUI-WanAnimatePreprocess.git
  - *From: 42hub*

- **WanAnimate_relight_lora** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/tree/main/LoRAs/Wan22_relight
  - *From: Le Fourbe*

- **ComfyUI memory leak fix** (repo)
  - https://github.com/comfyanonymous/ComfyUI/commit/c8d2117f02bcad6d8316ffd8273bdc27adf83b44
  - *From: JohnDopamine*

- **X-NEMO inference for lipsync** (repo)
  - https://github.com/bytedance/x-nemo-inference
  - *From: BecauseReasons*

- **MagCache for Wan 2.2 PR** (repo)
  - https://github.com/Wan-Video/Wan2.2/pull/70/files
  - *From: ˗ˏˋ⚡ˎˊ-*

- **AniSora High Noise LoRA** (lora)
  - https://huggingface.co/Kijai/WanVideo_comfy/blob/main/LoRAs/AniSora/Wan2_2_I2V_AniSora_3_2_HIGH_rank_64_fp16.safetensors
  - *From: Kijai*

- **Lightning LoRA for Wan 2.2** (lora)
  - https://huggingface.co/lightx2v/Wan2.2-Lightning/tree/main/Wan2.2-T2V-A14B-4steps-lora-250928
  - *From: 🦙rishappi*

- **Patajec Nodes for pose/canny blending** (node)
  - https://github.com/PATATAJEC/ComfyUI-PatatajecNodes
  - *From: PATATAJEC*

- **Wan Knowledge Base** (documentation)
  - https://nathanshipley.notion.site/Wan-2-1-Knowledge-Base-1d691e115364814fa9d4e27694e9468f#1d691e11536481f380e4cbf7fa105c05
  - *From: ReDiff*

- **ComfyUI-WanAnimatePreprocess** (repo)
  - https://github.com/kijai/ComfyUI-WanAnimatePreprocess
  - *From: AR*

- **Infinite-Forcing** (repo)
  - https://github.com/SOTAMak1r/Infinite-Forcing
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Phantom Tests Results** (test results)
  - https://drozbay.github.io/WanTests/PhantomTests/results2_distill_loras.html
  - *From: Ablejones*

- **WanAnimate fp8 v2 model** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy_fp8_scaled/blob/main/Wan22Animate/Wan2_2-Animate-14B_fp8_scaled_e4m3fn_KJ_v2.safetensors
  - *From: Kijai*

- **Car Consistency LoRA** (lora)
  - https://huggingface.co/drnighthan/CarConsistency-Wan2.2-I2V-ConsistencyLoRA1
  - *From: DawnII*

- **GGUF WanAnimate models** (model)
  - https://huggingface.co/QuantStack/Wan2.2-Animate-14B-GGUF/tree/main
  - *From: patientx*

- **Diffusion theory video** (educational)
  - https://www.youtube.com/watch?v=egn5dKPdlCk&t=4s
  - *From: Ablejones*

- **VACE upscaling guide** (guide)
  - https://claude.ai/public/artifacts/5d363576-3a02-4d52-bbc0-9269414bc420
  - *From: Ablejones*

- **Wan2.2-Animate V2 GGUF Q8** (model)
  - https://huggingface.co/QuantStack/Wan2.2-Animate-14B-GGUF/tree/main
  - *From: Kijai*

- **VRGameDevGirl HUMO workflow** (workflow)
  - https://github.com/vrgamegirl19/comfyui-vrgamedevgirl
  - *From: WackyWindsurfer*

- **Wan 2.2 GitHub issues** (repo)
  - https://github.com/Wan-Video/Wan2.2/issues
  - *From: DawnII*

- **OVI model** (model)
  - https://github.com/character-ai/Ovi
  - *From: seitanism*

- **Wan2.2-Lightning T2V LoRA** (lora)
  - https://huggingface.co/lightx2v/Wan2.2-Lightning/tree/main/Wan2.2-T2V-A14B-4steps-lora-250928
  - *From: Dream Making*

- **Lynx GGUF quantized models** (model)
  - https://huggingface.co/patientxtr/Wan2_1-T2V-14B-Lynx-GGUF/tree/main
  - *From: patientx*

- **Live reporting site for Lynx** (documentation)
  - https://wanx-troopers.github.io/lynx.htm
  - *From: 42hub*

- **Latent preview tools** (tool)
  - https://github.com/xl0/latent-tools
  - *From: mdkb*

- **OVI I2V on Replicate** (model)
  - https://replicate.com/character-ai/ovi-i2v/
  - *From: Draken*

- **OVI fp8_scaled models** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy_fp8_scaled/tree/main/TI2V/Ovi
  - *From: Kijai*

- **OVI bf16 models** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/tree/main/Ovi
  - *From: Kijai*

- **OVI example prompts** (repo)
  - https://github.com/character-ai/Ovi/tree/main/example_prompts
  - *From: Kijai*

- **OVI branch workflow** (workflow)
  - https://github.com/kijai/ComfyUI-WanVideoWrapper/blob/ovi/Ovi/wanvideo_2_2_5B_ovi_testing.json
  - *From: Stad*

- **OVI branch repository** (repo)
  - https://github.com/kijai/ComfyUI-WanVideoWrapper/tree/ovi
  - *From: slmonker(5090D 32GB)*

- **rCM LoRAs** (lora)
  - https://huggingface.co/Kijai/WanVideo_comfy/tree/main/LoRAs/rCM
  - *From: Kijai*

- **Tiny VAE 2.2** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/blob/main/taew2_2.safetensors
  - *From: Kijai*

- **RCM model** (model)
  - https://huggingface.co/worstcoder/rcm-Wan/tree/main
  - *From: JohnDopamine*

- **Lynx models** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/tree/main/Lynx
  - *From: VK*

- **Fixed WanMoeKSampler** (repo)
  - https://github.com/GalaxyTimeMachine/ComfyUI-WanMoeKSampler
  - *From: GalaxyTimeMachine*

- **New I2V lora for Wan 2.2** (lora)
  - https://huggingface.co/Kijai/WanVideo_comfy/blob/main/LoRAs/Wan22_Lightx2v/Wan_2_2_I2V_A14B_HIGH_lightx2v_MoE_distill_lora_rank_64_bf16.safetensors
  - *From: Kijai*

- **FlashVSR models** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/tree/main/FlashVSR
  - *From: Kijai*

- **rCM LoRA** (lora)
  - https://huggingface.co/Kijai/WanVideo_comfy/tree/main/LoRAs/rCM
  - *From: JohnDopamine*

- **Lightx2v compatible lora** (lora)
  - https://huggingface.co/Kijai/WanVideo_comfy/blob/main/Lightx2v/lightx2v_I2V_14B_480p_cfg_step_distill_rank256_bf16.safetensors
  - *From: FL13*

- **VibeVoice TTS ComfyUI** (tool)
  - https://github.com/Enemyx-net/VibeVoice-ComfyUI
  - *From: mdkb*

- **ModelPatchFastTerminate node** (node)
  - https://gist.github.com/blepping/99aeb38d7b26a4dbbbbd5034dca8aca8
  - *From: GalaxyTimeMachine (RTX4090)*

- **WanX Troopers connection guide** (guide)
  - https://wanx-troopers.github.io/what-plugs-where.html
  - *From: 42hub*

- **FlashVSR example workflows** (workflow)
  - https://github.com/kijai/ComfyUI-WanVideoWrapper/tree/main/example_workflows
  - *From: Dever*

- **FlashVSR examples inputs** (examples)
  - https://github.com/OpenImagingLab/FlashVSR/tree/main/examples/WanVSR/inputs
  - *From: Kijai*

- **Triton-windows 3.5.0** (tool)
  - https://github.com/woct0rdho/triton-windows/releases/tag/v3.5.0-windows.post21
  - *From: Kijai*

- **LightX2V Wan2.1 Distill Models** (model)
  - https://huggingface.co/lightx2v/Wan2.1-Distill-Models/tree/main
  - *From: hicho*

- **Triton Windows installation guide** (repo)
  - https://github.com/woct0rdho/triton-windows
  - *From: Lodis*

- **SmoothMix Animation Style** (model)
  - https://civitai.com/models/2040641/smoothmix-animation-style?modelVersionId=2309690
  - *From: hicho*

- **Wan Animate tutorial video** (tutorial)
  - https://www.youtube.com/watch?v=tP3Hfvaqnfw
  - *From: hicho*

- **ComfyUI-GGUF quantization tools** (tool)
  - https://github.com/city96/ComfyUI-GGUF/tree/main/tools
  - *From: Kijai*

- **ComfyUI-ModelQuantizer** (tool)
  - https://github.com/lum3on/ComfyUI-ModelQuantizer
  - *From: Kijai*

- **Lucy Edit ComfyUI** (tool)
  - https://github.com/decartAI/lucy-edit-comfyui
  - *From: Charlie*

- **SageAttention v2.2.0** (optimization)
  - https://github.com/woct0rdho/SageAttention/releases/tag/v2.2.0-windows.post4
  - *From: hicho*

- **ComfyUI Resolution Master** (node)
  - https://github.com/Azornes/Comfyui-Resolution-Master
  - *From: harrisonwells*

- **ComfyUI LayerForge** (node)
  - https://github.com/Azornes/Comfyui-LayerForge
  - *From: hicho*

- **Wan2_1_VAE_bf16** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/blob/main/Wan2_1_VAE_bf16.safetensors
  - *From: Léon*

- **MoCha converted model** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy_fp8_scaled/blob/main/MoCha/Wan2_1_mocha-14B-preview_fp8_e4m3fn_scaled_KJ.safetensors
  - *From: Kijai*

- **MoCha project page** (project)
  - https://orange-3dv-team.github.io/MoCha/
  - *From: Kijai*

- **Ditto LoRAs** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/tree/main/LoRAs/Ditto
  - *From: Kijai*

- **DiT360 panorama generation** (project)
  - https://fenghora.github.io/DiT360-Page/
  - *From: 42hub*

- **Dynamic video outpaint workflow** (workflow)
  - https://discord.com/channels/1076117621407223829/1430158482547413000
  - *From: yo9o*

- **WildPromptor ComfyUI node** (node)
  - https://github.com/1038lab/ComfyUI-WildPromptor
  - *From: hicho*

- **Mocha FP8 scaled model** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy_fp8_scaled/tree/main/MoCha
  - *From: blake37*

- **LayerForge for image positioning** (tool)
  - https://github.com/Azornes/Comfyui-LayerForge
  - *From: scf*

- **Group offloading implementation** (tool)
  - https://github.com/hiddenswitch/ComfyUI/blob/master/comfy_extras/nodes/nodes_group_offloading.py
  - *From: doctorpangloss*

- **Ditto web interface** (tool)
  - https://editto.net/
  - *From: shockgun*

- **Custom keyframe animation node** (node)
  - https://gist.github.com/thelemuet/9318d0e9b19d3c8473ca14722d104aa8
  - *From: lemuet*

- **Enhanced Wan2.2 AIO Infinite Video workflow** (workflow)
  - https://civitai.com/models/2059542/enhanced-wan22-aio-infinite-video-nsfw-no-loop-workflow?modelVersionId=2330617
  - *From: GalaxyTimeMachine*

- **VitPose models** (model)
  - https://huggingface.co/Kijai/vitpose_comfy/tree/main/onnx
  - *From: VK*

- **Endless travel VACE workflow** (workflow)
  - https://discord.com/channels/1076117621407223829/1386453178240733235
  - *From: JohnDopamine*

- **ComfyUI-LightVAE** (repo)
  - https://github.com/ModelTC/ComfyUI-LightVAE
  - *From: hicho*

- **LightX2V updated i2v models** (model)
  - https://huggingface.co/lightx2v/Wan2.2-Distill-Models/tree/main
  - *From: hicho*

- **HuMo i2v model patcher** (node)
  - https://github.com/drozbay/ComfyUI-WanVaceAdvanced
  - *From: Ablejones*

- **ComfyUI RAM pressure cache PR** (repo)
  - https://github.com/comfyanonymous/ComfyUI/pull/10454
  - *From: JohnDopamine*

- **Lightning LoRA for Wan** (lora)
  - https://civitai.com/models/1585622/lightning-lora-massive-speed-up-for-wan21-wan22-made-by-lightx2v-kijai
  - *From: JS Aguilar*

- **Wan FP4 quantized model** (model)
  - https://huggingface.co/wanvideoquant/wan-t2v-nvfp4-high-4-2-2/tree/main
  - *From: VK (5080 128gb)*

- **WanVACEStartToEnd custom node** (node)
  - https://huggingface.co/Phr00t/WAN2.2-14B-Rapid-AllInOne/tree/main/Custom-Advanced-VACE-Node
  - *From: Phr00t*

- **Celebrity character LoRAs collection** (model)
  - https://huggingface.co/malcolmrey/wan/tree/main/wan2.1
  - *From: hicho*

- **Wan 2.2 10-step models** (model)
  - https://huggingface.co/StefanFalkok/Wan_2.2_10steps/tree/main
  - *From: hicho*

- **Flux models collection** (model)
  - https://huggingface.co/malcolmrey/flux/tree/main
  - *From: Dream Making*

- **WAN 2.2 I2V GGUF workflow** (workflow)
  - https://civitai.com/models/1822764/wan-22-i2v-gguf-compact-speed-wf-or-lightning-lora-44-steps
  - *From: geterothis*

- **Lightning LoRAs for high noise model** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/blob/main/LoRAs/Wan22_Lightx2v/Wan_2_2_I2V_A14B_HIGH_lightx2v_4step_lora_v1030_rank_64_bf16.safetensors
  - *From: FL13*

- **Lightning LoRAs for low noise model** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/blob/main/Lightx2v/lightx2v_I2V_14B_480p_cfg_step_distill_rank64_bf16.safetensors
  - *From: FL13*

- **Mocha workflows** (workflow)
  - https://github.com/kijai/ComfyUI-WanVideoWrapper/commit/7916f89c337d792cbe52f423003575066ce04663
  - *From: Tony(5090)*

- **ComfyUI-HQ-Image-Save** (tool)
  - https://github.com/spacepxl/ComfyUI-HQ-Image-Save
  - *From: hudson223*

- **Krea LoRA** (model)
  - https://huggingface.co/aipmaster/krea-lora/tree/main
  - *From: postIt*

- **ComfyUI-CoCoTools_IO** (tool)
  - https://github.com/Conor-Collins/ComfyUI-CoCoTools_IO
  - *From: jhnmnnnnthftr*

- **LightCompress** (tool)
  - https://github.com/ModelTC/LightCompress
  - *From: hicho*

- **InfinityStar model** (model)
  - https://huggingface.co/FoundationVision/InfinityStar
  - *From: gpbhupinder*

- **Lucy Edit Dev ComfyUI** (model)
  - https://huggingface.co/decart-ai/Lucy-Edit-Dev-ComfyUI/tree/main
  - *From: hicho*

- **RollingForcing model** (model)
  - https://huggingface.co/TencentARC/RollingForcing
  - *From: hicho*

- **WanExperiments repository** (repo)
  - https://github.com/drozbay/WanExperiments
  - *From: Ablejones*

- **SVI-shot LoRA (KJ version)** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/tree/main/LoRAs/Stable-Video-Infinity
  - *From: Ablejones*

- **Bindweave project feature extraction** (repo)
  - https://github.com/bytedance/BindWeave/blob/8305c96d8584d7858c7147a10c4c63e7a2b30df2/s2v/OpenS2V-Eval/test_case_with_features.json
  - *From: Ablejones*

- **WanExperiments** (repo)
  - https://github.com/drozbay/WanExperiments
  - *From: Ablejones*

- **Kijai's SVI-shot LoRA** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/tree/main/LoRAs/Stable-Video-Infinity
  - *From: eraxor_*

- **SageAttention for Windows** (repo)
  - https://github.com/woct0rdho/triton-windows
  - *From: Kijai*

- **SageAttention main repo** (repo)
  - https://github.com/woct0rdho/SageAttention
  - *From: Kijai*

- **PainterLongVideo** (repo)
  - https://github.com/princepainter/ComfyUI-PainterLongVideo
  - *From: Dream Making*

- **Wan22FMLF custom node** (repo)
  - https://github.com/wallen0322/ComfyUI-Wan22FMLF
  - *From: hicho*

- **FastVideo causal i2v** (repo)
  - https://github.com/hao-ai-lab/FastVideo
  - *From: hicho*

- **Sigma reference guide** (resource)
  - wanx-troopers.github.io/sigmas.html
  - *From: 42hub*

- **WanVideo_comfy_fp8_scaled VACE models** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy_fp8_scaled/tree/main/VACE
  - *From: lemuet*

- **ComfyUI-WanViTPoseRetargeter** (repo)
  - https://github.com/red-polo/ComfyUI-WanViTPoseRetargeter
  - *From: dj47*

- **ComfyUI-WanAnimatePreprocess** (repo)
  - https://github.com/kijai/ComfyUI-WanAnimatePreprocess
  - *From: dj47*

- **Wan I2V tricks documentation** (documentation)
  - https://wanx-troopers.github.io/wan-i2v-tricks.html#painteri2v
  - *From: 42hub*

- **ComfyUI-PainterLongVideo** (repo)
  - https://github.com/princepainter/ComfyUI-PainterLongVideo
  - *From: JohnDopamine*

- **VRGameDevGirl84 Discord server** (community)
  - https://discord.gg/a8Fat7ct2U
  - *From: Scruffy*

- **Audio separation nodes for ComfyUI** (repo)
  - https://github.com/christian-byrne/audio-separation-nodes-comfyui
  - *From: 🦙rishappi*

- **Triton PTX Blackwell issue** (repo)
  - https://github.com/triton-lang/triton/issues/8539
  - *From: Ashtar*

- **Wan 2.2 I2V LoRAs** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/blob/main/LoRAs/Wan22_Lightx2v/ and https://huggingface.co/lightx2v/Wan2.2-Distill-Loras/blob/main/
  - *From: lemuet*

- **Wan2.2 I2V StartEndframes workflow** (workflow)
  - https://civitai.com/models/1818841/wan-22-workflow-t2v-i2v-t2i-kijai-wrapper
  - *From: herpderpleton*

- **WanExperiments repo with new nodes** (repo)
  - https://github.com/drozbay/WanExperiments
  - *From: Ablejones*

- **Chandler's HuMo nodes** (repo)
  - https://github.com/ckinpdx
  - *From: Scruffy*

- **SVI-film LoRA for multi-frame I2V** (lora)
  - https://wanx-troopers.github.io/svi.html#svi-film
  - *From: 42hub*

- **STCDiT video super-resolution framework** (repo)
  - https://github.com/JyChen9811/STCDiT
  - *From: JohnDopamine*

- **Context windows fixes** (repo)
  - https://github.com/kijai/ComfyUI/tree/contextwindows
  - *From: Kijai*

- **WanExperiments pack with fixed HuMo node** (repo)
  - https://github.com/drozbay/WanExperiments
  - *From: Ablejones*

- **HuMo example workflow** (workflow)
  - https://raw.githubusercontent.com/kijai/ComfyUI-WanVideoWrapper/refs/heads/main/example_workflows/wanvideo_HuMo_example_01.json
  - *From: Scruffy*

- **FFGO Video Customization** (repo)
  - https://github.com/zli12321/FFGO-Video-Customization/
  - *From: Scruffy*

- **AnimateDiff context windows documentation** (repo)
  - https://github.com/Kosinkadink/ComfyUI-AnimateDiff-Evolved/tree/main/documentation/nodes#context-optionsstandard-uniform
  - *From: ˗ˏˋ⚡ˎˊ-*

- **WanExperiments repository with fixed HuMo node** (repo)
  - https://github.com/drozbay/WanExperiments
  - *From: Scruffy*

- **Kijai's context windows PR** (repo)
  - https://github.com/comfyanonymous/ComfyUI/pull/10975
  - *From: Kijai*

- **Cinematic hard cut LoRA (new version)** (model)
  - https://civitai.com/models/2088559?modelVersionId=2376295
  - *From: Ablejones*

- **ComfyUI-LG_HotReload** (tool)
  - https://github.com/LAOGOU-666/ComfyUI-LG_HotReload/tree/master
  - *From: JohnDopamine*

- **PainterVRAM node** (tool)
  - https://github.com/princepainter/Comfyui-PainterVRAM
  - *From: hicho*

- **SteadyDancer model** (model)
  - https://github.com/MCG-NJU/SteadyDancer
  - *From: Juan Gea*

- **SteadyDancer GGUF version** (model)
  - https://huggingface.co/smthem/SteadyDancer-14B-gguf/tree/main
  - *From: Juan Gea*

- **ComfyUI-WanSoundTrajectory** (repo)
  - https://github.com/ckinpdx/ComfyUI-WanSoundTrajectory
  - *From: Chandler ✨ 🎈*

- **Kijai wrapper commits for combined embeds** (repo)
  - https://github.com/kijai/ComfyUI-WanVideoWrapper/commit/123c9ca3124ffdeffaf9c36cd9e90ef80fcb486e
  - *From: 42hub*

- **ComfyLiterals node** (repo)
  - https://github.com/M1kep/ComfyLiterals
  - *From: garbus*

- **ChainSampling tutorial video** (tutorial)
  - https://www.youtube.com/watch?v=A6CXfW4XaKs
  - *From: Ablejones*

- **Sampling techniques video** (tutorial)
  - https://www.youtube.com/watch?v=egn5dKPdlCk
  - *From: Ablejones*

- **3-sampler setup guide** (tutorial)
  - https://wanx-troopers.github.io/loras/part-01.html#20251123
  - *From: 42hub*

- **ComfyUI-WanVaceAdvanced context windows workflow** (repo)
  - https://github.com/drozbay/ComfyUI-WanVaceAdvanced
  - *From: Ablejones*

- **ComfyUI PR for context windows** (repo)
  - https://github.com/comfyanonymous/ComfyUI/pull/11208
  - *From: Ablejones*

- **SCAIL Audio Reactive nodes** (repo)
  - https://github.com/ckinpdx/ComfyUI-SCAIL-AudioReactive
  - *From: Chandler ✨ 🎈*

- **WanSoundTrajectory example workflows** (repo)
  - https://github.com/ckinpdx/ComfyUI-WanSoundTrajectory/tree/main/example_workflows
  - *From: Dream Making*

- **LongCat Video Avatar** (repo)
  - https://github.com/MeiGen-AI/LongCat-Video-Avatar
  - *From: JohnDopamine*

- **FBX Import custom node** (repo)
  - https://github.com/Clivey1234/ComfyUI_FBX_Import
  - *From: metaphysician*

- **Time To Move GUI alternative** (repo)
  - https://github.com/siraxe/ComfyUI-WanVideoWrapper_QQ
  - *From: Danial*

- **AE Animation English Mod** (repo)
  - https://github.com/Verolelb/ComfyUI-AE-Animation-English-Mod
  - *From: Vérole*

- **TurboDiffusion ComfyUI implementation** (repo)
  - https://github.com/anveshane/Comfyui_turbodiffusion
  - *From: Anchorite*

- **SCAIL AudioReactive nodes** (repo)
  - https://github.com/ckinpdx/ComfyUI-SCAIL-AudioReactive
  - *From: Kagi*

- **ControlFlowUtils for looping** (repo)
  - https://github.com/VykosX/ControlFlowUtils
  - *From: Kijai*

- **Execution inversion demo** (repo)
  - https://github.com/BadCafeCode/execution-inversion-demo-comfyui
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Sparse Linear Attention paper** (paper)
  - https://arxiv.org/html/2509.24006v2
  - *From: Scruffy*

- **Wan cropping workflows** (workflow)
  - https://wanx-troopers.github.io/workflows/crop-uncrop/
  - *From: 42hub*

- **HuMoveLora** (model)
  - https://huggingface.co/drozbay/HuMoveLora
  - *From: Ablejones*

- **SVI v2 Pro LoRAs** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/blob/main/LoRAs/Stable-Video-Infinity/v2.0/
  - *From: LukeG89*

- **LightX2V official LoRAs** (model)
  - https://huggingface.co/lightx2v/Wan2.1-Distill-Loras/tree/main
  - *From: LukeG89*

- **ComfyUI-Easy-Use with loops** (repo)
  - https://github.com/yolain/ComfyUI-Easy-Use
  - *From: neilmendoza*

- **ComfyUI-FFmpeg nodes** (repo)
  - https://github.com/MoonHugo/ComfyUI-FFmpeg/blob/main/README_EN.md
  - *From: hudson223*

- **VACE 2.2 GGUF models** (model)
  - https://huggingface.co/QuantStack/Wan2.2-VACE-Fun-A14B-GGUF/tree/main
  - *From: mdkb*

- **VACE workflows and memory management** (workflow)
  - https://markdkberry.com/workflows/research/
  - *From: mdkb*

- **MOVA model** (model)
  - https://huggingface.co/OpenMOSS-Team/MOVA-720p
  - *From: Draken*

- **MOVA GitHub issues** (repo)
  - https://github.com/OpenMOSS/MOVA/issues/17
  - *From: TK_999*

- **ComfyUI-WanVideoWrapper workflows** (workflow)
  - https://github.com/kijai/ComfyUI-WanVideoWrapper/issues/1718
  - *From: sir_AXE (Eugene)*

- **SimplePod.ai platform** (tool)
  - https://www.youtube.com/watch?v=mM-yT1aQV2o
  - *From: Tytanick*


## Known Limitations

- **VitPose finger detection inadequate**
  - Can't properly detect complex finger poses, struggles with stress test poses
  - *From: Kijai*

- **WanAnimate struggles with object manipulation**
  - Has difficulty with swords and similar objects extending properly
  - *From: Kijai*

- **Character similarity loss with facial expressions**
  - Face reference loses similarity when expressions change significantly
  - *From: piscesbody*

- **VHS frame count handling**
  - ComfyUI and VHS struggle with high frame counts like 800 frames at high resolution
  - *From: Kijai*

- **GGUF Q8 vs bf16 precision mixing**
  - Uncertain compatibility when mixing different precision models and modules
  - *From: Kijai*

- **WanAnimate is I2V only**
  - Cannot generate from text prompt alone, requires reference image
  - *From: DawnII*

- **WanAnimate doesn't handle extreme eye movements like crossed eyes or rolling back**
  - It tracks pupils when it sees them but fails on extreme poses
  - *From: Kijai*

- **Built-in looping feature can't be used with multiple samplers**
  - No latents returned when using built-in looping
  - *From: Kijai*

- **Anisora as lora with WanAnimate ruined pose control**
  - Didn't make WanAnimate better, on the contrary ruined pose control
  - *From: Kijai*

- **Raising steps >4 in Animate produces strange results**
  - Character clapping hands results in character with something like baseball bat
  - *From: SpacelessTuna*

- **HuMo short generation length**
  - Worst length of generations among lipsync models, limited to ~121 frames
  - *From: Kijai*

- **InfiniteTalk changes source video too much**
  - Tends to modify source video significantly, hard to find middle ground between lipsync improvement and preserving original
  - *From: 𝕯𝖗. 𝕸𝖆𝖈𝖆𝖇𝖗𝖊 ☠*

- **SAM2 doesn't support multiple boxes in video mode**
  - Need to use separate nodes and merge masks for multiple object detection
  - *From: Kijai*

- **Anisora still not production ready**
  - Long way from being production-ready despite improvements
  - *From: Gill Bastar*

- **WanAnimate watermarking still a problem**
  - Persistent watermarking issues in generated videos
  - *From: DawnII*

- **MagCache not compatible with FlashAttn**
  - Cannot use MagCache optimization with Flash Attention
  - *From: ˗ˏˋ⚡ˎˊ-*

- **WanAnimate poor character consistency**
  - Not as good as VACE for maintaining character consistency
  - *From: SonidosEnArmonía*

- **Lynx full model requires flash_attn**
  - Full Lynx model needs flash attention compilation, lite version works without
  - *From: Kijai*

- **AniSora low noise LoRA doesn't work well**
  - Extracted low noise LoRA produces poor results, may not be distilled
  - *From: Kijai*

- **Infinitetalk nodes don't work properly with 2.2**
  - Cannot sample output from high model with infinitetalk nodes using low model and standard embeds
  - *From: Juan Gea*

- **Context window shows visible seams**
  - Window context produces clearly visible seams in long generations
  - *From: Juan Gea*

- **MTV_Crafter won't work past 49 frames**
  - Model has hard limit at 49 frames despite being most generalized motion transfer available
  - *From: Kijai*

- **Lynx IP adapter ineffective in full model**
  - Full model's IP adapter adds 4GB but doesn't seem to do much - resemblance fine but everything else poor
  - *From: Kijai*

- **CFG > 1 produces worse results than distill**
  - Multiple users report CFG above 1.0 consistently produces inferior results compared to distill LoRAs
  - *From: Gleb Tretyak*

- **VACE strips out lipsync**
  - VACE removes lip synchronization which needs to be tested separately with WanAnimate
  - *From: mdkb*

- **WanAnimate bias towards front-facing poses**
  - Strongly makes character face forward, biased towards humans dancing with not much clothing. Even at 0.5 start percent it still tries to face forward
  - *From: Hashu*

- **Single image character consistency models**
  - One image input models like Lynx, Phantom, MagRef are not optimal for serious production work. Need multiple views of character for proper consistency
  - *From: xwsswww*

- **WanAnimate reduces motion and prompt following**
  - Too strong effect that ruins prompt following and motion. Can't get results that couldn't be done with Phantom
  - *From: Kijai*

- **HUMO length limitation**
  - Only does 3.8 seconds, team said they would release longer generation model this month but still waiting
  - *From: Kijai*

- **I2V LoRA camera control**
  - Character motion works great but camera control is static with only zoom motion available
  - *From: Rainsmellsnice*

- **Wan 2.2 I2V last frame degradation**
  - Consistently happening issue with last 10 frames of 161 frame video, visible from high noise generation
  - *From: Dever*

- **Color shift in I2V extensions**
  - VAE decoding causes color shifting when chaining I2V generations, no perfect fix found
  - *From: lemuet*

- **Lynx only works with human faces, not cartoon characters**
  - For cartoon characters like Donald Duck, need to combine with WanAnimate
  - *From: Rainsmellsnice*

- **WAN Animate loses character identity easily**
  - Uses only 1 reference image, identity preservation is challenging
  - *From: humangirltotally*

- **VACE doesn't maintain first frame likeness well**
  - Starts similar but mutates over time, difficult to force exact frame respect
  - *From: Juan Gea*

- **Flash at start of 121+ frame generations**
  - Normal behavior when going past 81 frames on models that don't support it
  - *From: Kijai*

- **FusionX LoRA kills likeness**
  - T2V-only LoRA that affects likeness when used incorrectly with I2V
  - *From: hicho*

- **Audio model needs more steps**
  - FastWAN 10 steps not suitable for audio - needs 30+ steps for good results
  - *From: Kijai*

- **Prompt bleeding**
  - Sometimes parts of prompt outside tags bleed into generated speech
  - *From: Kijai*

- **I2V not fully implemented**
  - I2V functionality exists but not yet implemented in the wrapper
  - *From: Kijai*

- **Resolution constraints**
  - Limited resolution options work (576x352, 352x288) but nothing in between
  - *From: patientx*

- **fp16 precision issues**
  - fp16 causes Nans and corrupted results, must use bf16
  - *From: Kijai*

- **Audio extension beyond 5 seconds**
  - Audio won't generate correctly after 157 latents, video can extend to 10+ seconds but audio is limited
  - *From: patientx*

- **fp16 precision issues**
  - Causes NaNs and black output in final steps
  - *From: Kijai*

- **Fastwan inconsistency**
  - Works fine sometimes with 10 steps no CFG, most of the time not at all
  - *From: Kijai*

- **rCM only for Wan 2.1**
  - Currently only available for Wan 2.1, not 2.2
  - *From: yi*

- **webm compatibility issues**
  - webm format has problems on Windows and Linux, audio only on some platforms
  - *From: Thom293*

- **OVI doesn't support non-English languages well**
  - Finnish did not work at all, other languages may have issues
  - *From: Kijai*

- **Face consistency lost in video extensions**
  - Each successive iteration throws off face consistency when using last frame as input
  - *From: Tachyon*

- **VACE transitions fail with rCM lora**
  - rCM works for basic generation but fails on VACE extended workflows with transitions
  - *From: JohnDopamine*

- **Dark scenes become too dark/black in OVI**
  - Any scene that's not completely full lit becomes too dark to see
  - *From: U̷r̷a̷b̷e̷w̷e̷*

- **FlashVSR struggles with small distant faces**
  - Makes faces worse when they are too small to define better
  - *From: mdkb*

- **FlashVSR causes slight color browning**
  - Noticeable color shift in sky and other elements
  - *From: mdkb*

- **FlashVSR doesn't support images currently**
  - Only works with video input
  - *From: wallen*

- **FlashVSR designed for low quality inputs**
  - Works best from 384x384 resolution, may overfit on HD inputs
  - *From: piscesbody*

- **FlashVSR may not process all input frames**
  - 161 frame input resulted in 157 frame output
  - *From: Dever*

- **Wan Animate only trained with pose controlnet**
  - Depth maps and other controlnets don't work properly, pose detection issues with complex scenes
  - *From: Kijai*

- **MPS and HPS Fun LoRAs biased toward human aesthetics**
  - Don't work well for non-human subjects like demons, will make them more human-like
  - *From: WAS*

- **Original LightX2V models incompatible with ComfyUI**
  - Need specifically formatted ComfyUI versions due to different model structure
  - *From: Kijai*

- **FlashVSR not suitable for high resolution upscaling**
  - Designed for 4x upscaling from very low resolution. Using on already decent resolution like 1280x768 produces blurry, over-sharpened results
  - *From: Kijai*

- **Merging T2V 2.1 LoRA with I2V 2.2 LoRA doesn't work properly**
  - Merged LoRAs don't produce same results as using both LoRAs together in workflow, unlike other 2.2 merges
  - *From: Kenk*

- **SageAttention compile mode can produce noisy output**
  - Regular sage mode works fine, but sage_compile can introduce noise artifacts
  - *From: scf*

- **MoCha has double compute requirements**
  - Memory usage similar to 161 frames when generating 81 frames due to frame concatenation
  - *From: Kijai*

- **MoCha doesn't support context windows yet**
  - Code needs changes for context window support
  - *From: Kijai*

- **Windows triton limitations with dynamic mode**
  - Windows triton isn't full triton, dynamic mode doesn't work properly
  - *From: Kijai*

- **Torch compile VAE causes visual artifacts**
  - Rainbow flickering after first successful run when compile is applied to VAE
  - *From: phazei*

- **Context windows cause artifacts on transitions**
  - I2V context windows commonly produce snap back or cross fade artifacts at window boundaries, though settings can mitigate this
  - *From: blake37*

- **Hallucinations in I2V context windows**
  - Model imagines content behind subjects that wasn't in original image, and different context windows don't agree on same hallucination causing inconsistency
  - *From: blake37*

- **Wan original rope never worked with compile**
  - Compilation issues with the original Wan rope implementation persist
  - *From: Kijai*

- **Mocha uses twice the VRAM of other models**
  - Significantly higher VRAM requirements compared to other video generation models
  - *From: Kijai*

- **VACE produces morphing rather than true animation**
  - VACE tends to morph images between keyframes with balloon effect rather than creating smooth animation movement
  - *From: GWX-Reloaded*

- **Full body shots lose facial likeness**
  - When generating full body shots, facial likeness tends to degrade compared to portrait shots
  - *From: humangirltotally*

- **Artifacts accumulate in chained generation**
  - Color distortion and random artifacts worsen after third 77-frame iteration in longer videos
  - *From: eraxor_*

- **SVI LoRA loops without control past 201 frames**
  - Even with VACE, SVI LoRA will still loop without control beyond 201 frames
  - *From: Hashu*

- **Light VAE has quality loss**
  - Faster processing but noticeable quality degradation compared to standard Wan VAE
  - *From: hicho*

- **Eye contact control in lip sync models**
  - Very difficult to maintain eye contact in over-shoulder shots, subjects won't maintain gaze direction as prompted
  - *From: mdkb*

- **New ComfyUI memory flags can cause crashes**
  - Pinned memory feature may cause unexpected crashes and RAM spikes
  - *From: scf*

- **SVI film has no reference so degrades over time**
  - Does 5 frame overlap but lacks reference causing degradation in extended sequences
  - *From: Ablejones*

- **I2V start image affects entire sequence**
  - Not possible to gradually reduce start image influence over time in I2V - the start image affects the whole sequence inherently
  - *From: Kijai*

- **Video generation is not frame-by-frame**
  - Video generation processes all frames simultaneously, making per-frame modifications difficult
  - *From: Kijai*

- **ChronoEdit not practical for high resolution**
  - Generation time becomes prohibitive for higher resolution image editing with ChronoEdit
  - *From: Dever*

- **LightVAE quality loss**
  - LightVAE provides much faster decoding but with noticeable quality degradation, not recommended for image generation
  - *From: Kijai*

- **WAN Animate quality degrades after 121+ frames**
  - Significant quality degradation occurs in WAN Animation when generating more than 121 frames
  - *From: humangirltotally*

- **HuMo faces keep moving with empty audio**
  - Hard to get HuMo faces to stop talking/quivering even with no audio input
  - *From: Ablejones*

- **SVI-shot requires custom nodes**
  - Won't work properly without WanExperiments custom nodes, using it off-label may produce poor results
  - *From: Ablejones*

- **Wan continuation inherent contrast shift**
  - Default behavior is for contrast to shift over multiple generations, requires various tricks to mitigate
  - *From: Ablejones*

- **Tiled VAE causes temporal artifacts**
  - Can cause weird temporal blending and seams if temporal_size not set properly
  - *From: brbbbq*

- **GGUF Q4 quality degradation**
  - Q4 quantization can have pretty bad quality hit in general
  - *From: Kijai*

- **HuMo not designed for true I2V**
  - Flash artifacts occur because HuMo wasn't actually designed for I2V even though it works well
  - *From: Ablejones*

- **Subgraphs are buggy with get/set nodes**
  - Links disconnect randomly, connect to wrong outputs when using subgraphs with get/set nodes
  - *From: Ablejones*

- **Frame count mismatch between models**
  - Hard to go over 100 frames because HuMo needs 25 FPS but other models trained on 16 FPS
  - *From: VRGameDevGirl84(RTX 5090)*

- **5B model works poorly with multi-frame reference**
  - Multi-frame reference approach doesn't work well with 5B model
  - *From: Kijai*

- **Character consistency challenging with Wan**
  - Difficult to maintain character consistency, especially for non-humanoid characters
  - *From: placebo_yue*

- **VACE struggles with hand-drawn sketch interpolation**
  - Tries to morph frames too literally instead of generating new frames matching animation style, works better with consistent objects/shapes
  - *From: lemuet*

- **Fun models produce lower quality results**
  - Fun Control and Fun VACE models don't achieve same quality as standard models
  - *From: Gleb Tretyak*

- **Painter node breaks HuMo lip sync**
  - When using Painter as first pass, HuMo second pass doesn't produce lip sync movement
  - *From: Chandler ✨ 🎈*

- **Native implementation quality issues**
  - Native Wan 2.2 produces significantly lower quality than wrapper implementation
  - *From: Gleb Tretyak*

- **Context options remain obscure**
  - Context windows approach for continuity is not well understood and not widely used, suggesting poor effectiveness
  - *From: 42hub*

- **VACE 2.2 module quality issues**
  - VACE 2.2 module performs poorly compared to VACE 2.1
  - *From: hicho*

- **Can't use both denoise and start_step parameters simultaneously**
  - Will cause 'start_step must be less than end_step' error
  - *From: 42hub*

- **4-frame latent block constraint in I2V**
  - Must respect 4+1 frames rule or get glitches like weird color shift or flashing
  - *From: lemuet*

- **HuMo not designed for long duration generations**
  - HuMo can work for longer videos but requires creative workflows, unlike InfiniteTalk which is built for long videos
  - *From: Ablejones*

- **HuMo color drift when replacing 2.1 LN**
  - Same settings that work with 2.1 LN cause severe color drift when switching to HuMo, even without HuMo embeds
  - *From: Gleb Tretyak*

- **Context windows fundamental issue with start image**
  - Camera can't really move and character can't leave frame when using start image with context windows
  - *From: Kijai*

- **PainterLongVideo node is non-functional**
  - Reference image and motion frames inputs don't work, reference_motion only used by S2V model, produces same results as single frame I2V
  - *From: Ablejones*

- **Context windows don't work with i2v channel stuff**
  - Context windows incompatible with I2V conditioning channels and similar features
  - *From: Ablejones*

- **HuMo quality suffers with context windows**
  - While technically possible, quality drops to same level as other models that already do long generation natively
  - *From: Kijai*

- **Native HuMo implementation incomplete**
  - Only uses one reference image instead of supporting multiple like the model actually can
  - *From: Ablejones*

- **Context windows cause background shifting**
  - Every window uses same start image causing background inconsistencies, though less than usual with some models
  - *From: Kijai*

- **Context windows cause character drift**
  - Only first context window gets character references, subsequent windows ignore them causing identity loss
  - *From: Ablejones*

- **DW pose doesn't work well for drawings**
  - Pose detection fails on non-real human subjects like sketches or animated characters
  - *From: dj47*

- **Resolution and upscaling issues for anime**
  - Even working workflows look poor quality, no great way to upscale anime found
  - *From: dj47*

- **Frame rate inconsistencies between models**
  - Models trained at different fps (16 vs 25) and even same models can go slow motion or fast unexpectedly
  - *From: Ablejones*

- **Wan 2.2 Fun VACE doesn't support 2.2 LoRAs**
  - Built on 2.2 Fun architecture, not as flexible as 2.1 VACE for complex tasks
  - *From: Danial*

- **Context windowing artifacts in general use**
  - Only works well with controlled backgrounds, static cameras, or strong controls like VACE. Limited applicability for general video generation
  - *From: Ablejones*

- **HuMo with SVI 2.2 compatibility issues**
  - Couldn't make HuMo work properly with SVI 2.2, creates transition issues
  - *From: Cseti*

- **Character reference degradation in multi-pass**
  - Using Wan 2.2 + HuMo makes character reference work less well compared to single model use
  - *From: VRGameDevGirl84(RTX 5090)*

- **Flash attention compatibility on RTX 5090**
  - torch 2.9 flash attention doesn't support RTX 5090 capability (12,0) and float32 dtype
  - *From: Scruffy*

- **SCAIL only works for 81 frames natively**
  - Anything beyond requires context windows with usual problems, full version will have extension method
  - *From: Kijai*

- **SCAIL background shifts when camera moves away from original background**
  - Not model fault, inherent limitation of the approach
  - *From: Kijai*

- **Humo works better without traditional image embeds**
  - It's a t2v model wearing an i2v model's skin
  - *From: Ablejones*

- **vitpose-H only does one person while dwpose can do multiple**
  - Trade-off between quality and multi-person support
  - *From: Kijai*

- **InfiniteTalk only works with Chinese model but knows English**
  - wav2vec not needed for English as Chinese model handles it
  - *From: Kijai*

- **SCAIL only supports single person with ViTPose**
  - WanAnimate code limitation, doesn't show multi person hands/face
  - *From: Kijai*

- **Path animator node only outputs 121 frames**
  - Matches Wan ATI training, frame_count only changes path sampling, not output length
  - *From: Fill*

- **WanMove and SCAIL incompatible on base level**
  - Cannot use both techniques together
  - *From: Gleb Tretyak*

- **TurboDiffusion int8 quantized weights incompatible with LoRAs**
  - Would need to run LoRA separately, making it potentially pointless
  - *From: Kijai*

- **InfiniteTalk FPS cannot be changed**
  - Trained with 25fps, cannot change to 16fps to match other wan clips
  - *From: Kijai*

- **No specific 720p LightX2V LoRA**
  - 480p works with 720p model, 720p version was same LoRA merged to 720p model
  - *From: Kijai*

- **ComfyUI loops are fragile**
  - Don't allow starting/stopping partial executions, can't change something mid-loop and continue
  - *From: Ablejones*

- **Phantom is very fragile model**
  - Could LoRA it but wouldn't be very helpful
  - *From: Piblarg*

- **VACE inpainting seams with tight crops**
  - Tighter crop to masked area creates more visible seams
  - *From: Hashu*

- **SCAIL facial expression fidelity**
  - SCAIL isn't as faithful at maintaining facial expressions compared to LTX 2
  - *From: Kevin "Literally Who?" Abanto*

- **LTX 2 pose copying**
  - LTX 2 has poor fidelity in copying poses from video despite trying various settings (steps, cfg, IC Lora strength, prompting, etc.)
  - *From: Kevin "Literally Who?" Abanto*

- **First-frame-last-frame flickering**
  - Using first-frame-last-frame for video extension often results in weird flickering and color changes
  - *From: kaibioinfo*


## Hardware Requirements

- **VRAM monitoring**
  - Use GPUz to monitor VRAM, restart ComfyUI when hitting 6000MB to avoid long generation times
  - *From: hicho*

- **24GB VRAM still insufficient**
  - A5000 with 24GB VRAM still runs into memory issues with WanAnimate on larger videos
  - *From: Slavrix*

- **CUDA toolkit versions**
  - PyTorch 2.10 nightly available for CUDA 12.8, CUDA 13.0 has known incompatibility with SageAttention
  - *From: IceAero*

- **VRAM for 720/400 81 frames v2v**
  - Specific VRAM usage mentioned but amount not specified
  - *From: hicho*

- **RAM for non-blocking processing**
  - Bigger vitpose model might push to RAM limit causing OOM
  - *From: Kijai*

- **1280x720 resolution**
  - Takes about 64GB VRAM for generation
  - *From: ReDiff*

- **FP8 dual model loading**
  - 19GB per model (HN and LN) reaches 720p on 3060 12GB VRAM with 32GB system RAM
  - *From: mdkb*

- **Wan Animate GPU stability**
  - May cause GPU disable/computer freezing, likely PSU power issue due to larger compute blocks
  - *From: Draken*

- **6GB VRAM for 1280x720 81 frames**
  - Possible but VAE becomes bottleneck and very slow
  - *From: hicho*

- **65-70GB VRAM for 4K generations**
  - RTX Pro 6000 Blackwell with 96GB used for 4K video generation
  - *From: ReDiff*

- **256GB RAM pushed by 4K generations**
  - Even 256GB RAM gets pushed when storing 28s of 4K frames
  - *From: ReDiff*

- **24GB VRAM for 864x1344x321 frames**
  - Takes 99% of 24GB VRAM during VACE encoding, peak usage defined by width * height * length
  - *From: scf*

- **VRAM for pose detection**
  - 1-2 seconds for 81 frames on 4090 with latest onnx and onnxruntime-gpu
  - *From: Kijai*

- **Generation time without optimizations**
  - Goes from 10 minutes to nearly 40 minutes for 720p 77 frames when disabling optimizations
  - *From: Ablejones*

- **HuMo generation speed**
  - 3.88 seconds for 6 steps with LightX v2
  - *From: Ablejones*

- **GGUF recommendation for RTX 3000 series**
  - Kijai recommends using GGUF on 3000 series GPUs over fp8
  - *From: Kijai*

- **WanAnimate Q4_K_S performance on RTX 3060**
  - Around 50 frames took about 800 seconds on RTX 3060
  - *From: Abx*

- **Torch compile time for WanAnimate**
  - Takes 2 minutes to compile WanAnimate workflow in native, has tons of device copies
  - *From: Kijai*

- **RAM for long videos**
  - 32GB not enough for long videos, 64GB recommended, 128GB ideal for all AI work especially with VACE
  - *From: Charlie*

- **VRAM usage with models**
  - 19GB file size models run on 12GB VRAM card without filling up due to block swap/offloading
  - *From: mdkb*

- **Memory bandwidth comparison**
  - RTX 5070ti: 0.9Tb/sec, RTX 5090: 1.7Tb/sec, GB200: 8Tb/sec
  - *From: 42hub*

- **VRAM reservation for VAE**
  - 81x704x1088 frames uses max 1.18GB allocated but 17.47GB reserved, tiling reduces to 6.22GB
  - *From: scf*

- **Lynx VRAM usage**
  - Full model +8GB, lite+full ref around +5GB more than base model
  - *From: Kijai*

- **OVI VRAM requirements**
  - Close to 24GB VRAM, basically double of base 5B model, less than 14B with block swap
  - *From: ZeusZeus*

- **OVI performance**
  - 20 steps takes about 250 seconds on RTX 4090
  - *From: ZeusZeus*

- **FP8 compatibility**
  - Wrong FP8 version (e5m4) for RTX 30xx series, need different format
  - *From: U̷r̷a̷b̷e̷w̷e̷*

- **VRAM usage with full block swap and fp8**
  - Around 5.8-6.5GB VRAM on Linux, 8GB on Windows
  - *From: Kijai*

- **VRAM usage standard**
  - 24GB VRAM without optimizations, can use block swap over 20 for lower VRAM
  - *From: slmonker(5090D 32GB)*

- **Performance with 5090**
  - 121 frames at 992x512, 40 steps in 1:24 with max 24.567GB allocated
  - *From: Kijai*

- **Low VRAM compatibility**
  - Works on 8GB VRAM with fp8 weights and proper settings
  - *From: Stad*

- **OVI VRAM usage**
  - 24GB without block swap or quants, fits in 7GB with full block swap up to 680x680, works on 4060
  - *From: Stad*

- **6GB VRAM for OVI**
  - Use fp8 models with full block swap (30 blocks)
  - *From: Kijai*

- **3060 performance with OVI**
  - Very slow at 200s/it, not practical for regular use
  - *From: U̷r̷a̷b̷e̷w̷e̷*

- **Context window memory impact**
  - Memory requirements multiply for low noise steps without context options
  - *From: blake37*

- **OVI VRAM usage on RTX 3090**
  - 60% VRAM usage, about 6 minutes per generation with EasyCache
  - *From: Rainsmellsnice*

- **OVI on RTX 5090**
  - 121 frames at 704x704 with 50 steps: 128.20 seconds, max allocated 17.141 GB
  - *From: Kijai*

- **OVI estimated on RTX 3090**
  - Should be around 5 minutes (compared to 2+ minutes on 5090)
  - *From: Kijai*

- **OVI model size**
  - Around 11GB, smaller than people think
  - *From: Kijai*

- **FlashVSR VRAM usage**
  - 7.605 GB max for 33 frames at 1920x1088 with SDPA, can get much lower with optimizations
  - *From: Kijai*

- **FlashVSR processing time on 3060**
  - 580 seconds for 1920x1072 output, 16GB RAM usage at VRAM limit
  - *From: mdkb*

- **FlashVSR context processing**
  - 360 seconds for 157 frames at 1024x1024 with context options
  - *From: mdkb*

- **SeedVR2 VRAM usage**
  - Hit 24GB VRAM at 1600x1600, needs smaller VAE tiling for higher resolutions
  - *From: PATATAJEC*

- **FlashVSR speed comparison**
  - Sage attention: 50 seconds, SDPA: 3 minutes for 1280x720 to 1920x1072 upscale
  - *From: piscesbody*

- **High RAM usage after generations**
  - RAM stays elevated after each generation due to image caching, upscale model node doubles memory usage
  - *From: BestWind*

- **RTX 3090 with 64GB RAM + 50GB page file**
  - Can load Wan 2.2 models + Flux depth, uses ~30GB from page file saving RAM upgrade
  - *From: hicho*

- **CUDA 13.0 drivers required for torch 2.9**
  - Need to update NVIDIA drivers when upgrading from torch 2.8 to 2.9
  - *From: BestWind*

- **Torch compile provides 30% speed boost on RTX 4090/5090**
  - First compilation takes ~10 seconds, reduces VRAM usage significantly
  - *From: Kijai*

- **VRAM usage with SageAttention compile**
  - Reduces peak VRAM from 15.749GB to 14.667GB max allocated memory with minimal speed difference (11.87s vs 11.80s per iteration)
  - *From: Kijai*

- **4080 Super 16GB VRAM with 96GB RAM**
  - Still experiences OOMs with 27GB LoRAs and certain workflows, needs tiled processing
  - *From: smithyIAN - 4080ti Super 16gig*

- **2060 GPU capability improvement**
  - Months ago could only generate 1 second video, now capable of much more with optimizations
  - *From: hicho*

- **MoCha VRAM usage**
  - Couldn't do 81 frames 720p on L40S 48GB VRAM, 832x480 used 15.6GB max
  - *From: Shubhooooo*

- **CUDA driver update increases VRAM consumption**
  - Newer NVIDIA driver consumes more VRAM, can't run same workflows as before
  - *From: scf*

- **Ditto VRAM needs**
  - OOMs on 8GB when using their VACE module in bf16, works with fp8/GGUF
  - *From: Stad*

- **PyTorch version compatibility**
  - Recommended: PyTorch 2.7.1 or 2.9.0 with CUDA 12.8 and CUDA Toolkit. Avoid 2.8.0 on Windows
  - *From: Juan Gea*

- **Triton cache clearing**
  - Delete C:\Users\<username>\.triton folder to clear triton cache when encountering tensor type errors
  - *From: Kijai*

- **VRAM for low-end users**
  - Group offloading with diffusers provides better performance than block swap for VRAM-limited setups
  - *From: doctorpangloss*

- **Krea Realtime performance**
  - 11 fps on B200 GPU, may work at low res on 5090
  - *From: Dever*

- **VRAM for LongCat refiner**
  - LongCat refiner stage may require more than 24GB VRAM (4090) to run properly, possibly needs 32GB (5090)
  - *From: JohnDopamine*

- **RAM usage increased with new ComfyUI**
  - Reduced capacity from 97 to 69 frames at 1024x1024, second sampler using 12GB more RAM than first
  - *From: lemuet*

- **Wan 2.1 fp16 model VRAM**
  - 28GB technically, requires offloading on 24GB cards
  - *From: Kijai*

- **Light VAE benefits low VRAM users**
  - Especially helpful for 4GB VRAM setups, speeds up processing significantly
  - *From: hicho*

- **Speed improvements with new memory management**
  - 9s/it gain on old PC with Wan 20 steps, 4s to 2.5s/it on Qwen edit with bf16
  - *From: Lumifel*

- **3B model VRAM usage**
  - 24GB VRAM cannot handle 1920 resolution with 3B model
  - *From: Dream Making*

- **LongCat VRAM for 23 seconds**
  - 5060 Ti 16GB can handle LongCat generation for 23 seconds by reducing frames per segment
  - *From: Juan Gea*

- **Recommended budget setup**
  - RTX 2060 + 64GB RAM can handle extensive generations effectively
  - *From: hicho*

- **Cache RAM setting**
  - For 32GB RAM system, use appropriate --cache-ram setting value
  - *From: devnullblackcat*

- **System RAM for long durations**
  - 128GB local, 288GB on rental boxes. Always system RAM that becomes bottleneck with long videos
  - *From: samhodge*

- **Professional GPU rental costs**
  - RTX 6000 Pro rentals under $2/hour with 500GB disk, 288GB RAM, 16vCPUs. Heavy usage under $30/week
  - *From: samhodge*

- **CUDA compatibility for SageAttention 2**
  - Works with CUDA 12.8.1 + PyTorch 2.8. CUDA 13 compatibility issues with Python 3.13, works with downgrade to 3.12
  - *From: samhodge*

- **VRAM management**
  - Recent ComfyUI updates caused memory issues, need to disable --fast flag and pinned memory
  - *From: JohnDopamine*

- **SageAttention GPU compatibility**
  - Works with Blackwell GPUs, includes TORCH_CUDA_ARCH_LIST for 8.0, 8.6, 8.9 architectures
  - *From: samhodge*

- **VRAM for Wan 2.2 14B**
  - Can run on 8GB VRAM with low VRAM settings, 16GB VRAM is sufficient
  - *From: Tony(5090)*

- **fp8 precision for RTX 3090**
  - Use fp8_e5m2 or with latest triton-windows can use fp8_e4m3fn
  - *From: Kijai*

- **Block swap recommended for 3090**
  - For 3090 with 64GB RAM, use block swap for memory management
  - *From: lemuet*

- **Performance on RTX 3060 12GB**
  - Can produce 13 second video in about 15 minutes using infinite video workflow
  - *From: atom.p*

- **VRAM for wrapper**
  - InfiniteTalk runs under 10GB VRAM easy with blockswap enabled
  - *From: Kijai*

- **Resolution limits**
  - 1000x1000 resolution with 17 frames causes OOM on 16GB VRAM with wrapper
  - *From: Gleb Tretyak*

- **VRAM management with --async-offload**
  - Using --async-offload can cause instant OOM issues, especially with blockswap. More offloading makes it worse
  - *From: Gleb Tretyak*

- **--reserve-vram for Windows**
  - Windows has fluctuating VRAM usage that automatic estimation doesn't account for. Reserve a few GB to solve this
  - *From: Kijai*

- **VRAM usage should be near 98%**
  - 98% VRAM usage is normal and desired, only issue is when it spills over causing errors
  - *From: Ablejones*

- **Browser hardware acceleration uses 500-1000MB VRAM**
  - Having ComfyUI open in browser with hardware acceleration can cause generations to stop
  - *From: Kijai*

- **Shared GPU memory should be under 5%**
  - Over 5% shared GPU memory causes GPU to wait 99% of time for CPU, massive slowdowns
  - *From: Ablejones*

- **VRAM usage with Wan 2.2**
  - User hitting 98% VRAM and 98% RAM with RTX 5090, compared to 50% usage with 96GB RAM system
  - *From: VRGameDevGirl84(RTX 5090)*

- **WanMove VRAM usage**
  - Doesn't increase VRAM use at all from Wan 2.1 I2V, sampling part is identical
  - *From: Kijai*

- **VRAM monitoring for 2060**
  - If VRAM maxed out, coil whine indicates issues, need 500+ MB free for quick warmup
  - *From: hicho*

- **RTX 5090 SCAIL performance**
  - 500 frames at 512x896 takes 20 minutes
  - *From: Chandler ✨ 🎈*

- **ONNX Runtime CUDA 13 compatibility**
  - Not yet completely compatible, getting there in nightlies but may still work
  - *From: JohnDopamine*

- **SageAttention 1.0.6 compatibility**
  - Should work on RTX 2080 but could be wrong
  - *From: Kijai*

- **LongCat Avatar bf16 on 4090**
  - Needs 30 blocks swapped at 832x480, requires disabling keep_model_in_vram for 64GB RAM
  - *From: Kijai*

- **RTX 5090 multi-window performance issue**
  - 161 frames takes ~30 min vs 5 min single window, while 4090 doesn't have this issue
  - *From: billchen*

- **For loops memory usage**
  - Big hit to RAM, can cause memory leaks and crash ComfyUI if looping too much
  - *From: FL13*

- **SVI Pro VRAM usage**
  - Pushes to ~29GB VRAM with auto swap to shared, ~50GB RAM on 3090 with 64GB RAM
  - *From: Anchorite*

- **VACE 2.2 modules memory**
  - fp8 e5m2 19GB HN + 19GB LN files don't blow out 12GB 3060 VRAM with 32GB system RAM
  - *From: mdkb*

- **Large frame processing**
  - 256-512 frames at 1920x1280 causes memory issues, need FFmpeg nodes and FreeMemory nodes
  - *From: Persoon*

- **96GB VRAM still getting memory errors**
  - User with 96GB VRAM experiencing 'ran out of memory' warnings with VAE decoding for <1080p 64 frame videos
  - *From: AIGambino*


## Community Creations

- **WanVideoAnimateEmbeds node updates** (node)
  - Separated pose detection and drawing with new options
  - *From: Kijai*

- **GPU-accelerated mask grow node** (node)
  - Updated mask growing to use GPU instead of slow CPU processing
  - *From: Kijai*

- **CFG Schedule integration** (workflow)
  - Method to use CFG scheduling with LoRA strength for quality improvement
  - *From: patientx*

- **WanAnimate relight lora resized** (lora)
  - Resized from 1.44GB to 273MB with no visible difference to full version
  - *From: Kijai*

- **Anisora V3.2 fp8 scaled models** (model)
  - Converted Anisora V3.2 to fp8 format for better efficiency
  - *From: Kijai*

- **HuMo I2V modification** (code modification)
  - Modified HuMo model code to work as I2V while retaining audio conditioning capabilities
  - *From: Ablejones*

- **ComfyUI-WanAnimatePreprocess** (custom node)
  - Preprocessing nodes for WanAnimate including VitPose and YOLO detection
  - *From: Kijai*

- **Patajec Nodes** (node)
  - Custom node for blending pose on black with canny on white backgrounds
  - *From: PATATAJEC*

- **AniSora LoRA extraction** (lora)
  - High noise LoRA extracted from AniSora 3.2 for distilled generation
  - *From: Kijai*

- **Car Consistency LoRA** (lora)
  - LoRA for maintaining car consistency across scene cuts, keeps details like license plates
  - *From: DawnII*

- **HUMO automated workflow** (workflow)
  - Stitches together HUMO fragments for any length audio, almost fully automated
  - *From: VRGameDevGirl84(RTX 5090)*

- **High noise to Low noise transition workflow** (workflow)
  - Batched high noise processing through single low noise sampler for better I2V transitions
  - *From: DawnII*

- **Lynx GGUF quantizations** (model)
  - Q2_K through Q8_0 quantized versions of Lynx models for lower VRAM usage
  - *From: patientx*

- **Multi-sampler workflow** (workflow)
  - 7 K-samplers workflow combining different models per step
  - *From: hicho*

- **Spine editor with primitive node fix** (workflow)
  - Using primitive nodes instead of direct INT connections for points_to_sample
  - *From: Kijai*

- **Native ComfyUI OVI implementation** (node)
  - Supports native ComfyUI LoRA loading and integrates with base ComfyUI
  - *From: Kytra*

- **ModelWanAudio quantization support** (tool)
  - Custom class for GGUF quantization of audio model
  - *From: patientx*

- **Fixed WanMoeKSampler** (node)
  - Fixed sigma_shift bug that was ignoring the parameter and splitting steps 50/50
  - *From: GalaxyTimeMachine*

- **Video Aspect Ratio Expander** (workflow)
  - Workflow for expanding video aspect ratios, will be released soon
  - *From: yo9o*

- **ModelPatchFastTerminate** (node)
  - Makes ComfyUI cancel button work much quicker instead of waiting minutes
  - *From: GalaxyTimeMachine (RTX4090)*

- **Git pull automation script for custom nodes** (workflow)
  - Commands to convert manager-installed nodes to git-updatable versions
  - *From: BestWind*

- **Triton cache clearing batch file** (tool)
  - Automated script to clear triton cache folders
  - *From: humangirltotally*

- **Perfect Resolution Calculator** (node)
  - Node to calculate optimal resolution for GPU constraints while preserving aspect ratio
  - *From: Ashtar*

- **SwarmUI Wan extension with LLM enhancement** (tool)
  - Extension with enhance options for Qwen, Wan, and Ovi with LLM-enhanced prompts
  - *From: U̷r̷a̷b̷e̷w̷e̷*

- **JoyCaption memory fix** (fix)
  - Pull request to fix memory leak in JoyCaption node
  - *From: Dever*

- **MoCha PR integration** (integration)
  - Orange-3DV team submitted PR for MoCha model support in wrapper
  - *From: Kijai*

- **WildPromptor Ditto prompts** (node_extension)
  - Added Ditto-specific prompts to WildPromptor node for better prompt generation
  - *From: hicho*

- **Extended preprocessor with Flux and Qwen** (workflow)
  - Enhanced preprocessing workflow that matches scene content in masked areas using Flux and Qwen
  - *From: Mads Hagbarth Damsbo*

- **Custom keyframe batch preparation node** (node)
  - Single node to prepare image batches and masks for keyframe animation without noodle mess
  - *From: lemuet*

- **HuMo i2v model patcher node** (node)
  - Allows embedded mask manipulation for SVI and dialogue workflows
  - *From: Ablejones*

- **WanVACEStartToEnd custom node** (node)
  - Modified Kijai's node to allow start images and control motions simultaneously with ease-in feature
  - *From: Phr00t*

- **Light VAE integration** (tool)
  - Faster VAE processing for high resolution and more frames, wrapper support
  - *From: hicho*

- **HuMo I2V Patch Node** (node)
  - Prevents ComfyUI from deleting image embedding when using HuMo model, enabling proper I2V functionality
  - *From: Ablejones*

- **WanVideo Cache Node** (node)
  - Text encoder cache management for the wrapper
  - *From: mdkb*

- **ComfyUI-SocksLatentPatcher** (tool)
  - Claims to turn WAN output latent into input latent without decode, though effectiveness is questionable
  - *From: Draken*

- **WanExperiments custom nodes** (node)
  - Provides WanEx I2VCustomEmbeds, HuMo I2V patches, Bindweave implementation
  - *From: Ablejones*

- **SVI-shot workflow with custom embeds** (workflow)
  - Video continuation workflow with reduced degradation using custom I2V embedding node
  - *From: Ablejones*

- **WanExperiments** (node pack)
  - Enables native HuMo i2v workflows and Bindweave functionality
  - *From: Ablejones*

- **Wan 2.2 + HuMo workflow** (workflow)
  - Multi-pass workflow combining Wan 2.2 with HuMo for lip sync and face swap
  - *From: VRGameDevGirl84(RTX 5090)*

- **Custom model merge** (model)
  - Combination of MagRef, Pusa, and LightX models
  - *From: VRGameDevGirl84(RTX 5090)*

- **HuMo sampler fix patch** (code patch)
  - Fixes first frame duplication issue by preventing front padding in sampler
  - *From: Chandler ✨ 🎈*

- **Chinese to English translation tool** (script)
  - CLI tool that translates Chinese text in nodes/workflows or removes Chinese when English is present
  - *From: JohnDopamine*

- **Wan Story workflow** (workflow)
  - Customized infinite video workflow that takes starter image and 3-5 prompts for changes every 81 frames
  - *From: atom.p*

- **HuMo Music Video Creator** (workflow)
  - Automated workflow for creating music videos using FML technique with frame transitions
  - *From: VRGameDevGirl84(RTX 5090)*

- **WanVideoWrapper safeTailPadCrop fix** (node)
  - Pull request to fix tail padding crop issues in wrapper
  - *From: 42hub*

- **Preview Embedded Masks and Latents node** (node)
  - Node to inspect basic embedded latents and masks used by WanVideoWrapper
  - *From: Ablejones*

- **PainterI2V noise modulation nodes** (node)
  - Stripped PainterI2V math into separate nodes for applying noise modulation after any I2V node, includes masking support
  - *From: Ablejones*

- **Lip sync suppress node** (node)
  - Node to reduce HuMo lip flapping with silent audio by working on audio projection layers
  - *From: Chandler ✨ 🎈*

- **Fixed HuMo node** (node)
  - Modified HuMo node that supports multiple reference images instead of just one
  - *From: Ablejones*

- **Context windows audio embed fix** (node)
  - PR to allow HuMo audio embeds to work with context windows
  - *From: Ablejones*

- **Fixed HuMo node** (node)
  - Correctly allows multiple image references instead of just one, good results with 6+ references
  - *From: Scruffy*

- **WanEx_PainterMotionAmplitude node** (node)
  - Rewritten Painter node implementation, supposedly better than original
  - *From: Dream Making*

- **Custom node for complex frame handling** (node)
  - Adds last frame, modulates frame strength, beyond basic wanimagetovideo capabilities
  - *From: Ablejones*

- **WanSoundTrajectory** (node)
  - Audio-reactive trajectory generation for WanMove with pose detection and sound modulated tracks
  - *From: Chandler ✨ 🎈*

- **Pose data transfer nodes** (node)
  - Transfers pose data to new target regardless of starting position with 3D support
  - *From: ingi // SYSTMS*

- **LoRA key removal script** (tool)
  - Python script to remove incompatible keys from LoRA files to prevent console errors
  - *From: patientx*

- **3D OpenPose integration** (node)
  - Adding 3D support and poseImage->posedata conversion for pose workflows
  - *From: Scruffy*

- **WASWanExposureStabilizer** (node)
  - Corrects exposure gain at beginning of frame batches and exposure loss at end
  - *From: WAS*

- **SCAIL Audio Reactive nodes** (node)
  - Generates poses for SCAIL driven by audio with multiple character support
  - *From: Chandler ✨ 🎈*

- **WanVaceAdvanced nodes** (node)
  - Enables context windows with VACE and proper latent noise masking
  - *From: Ablejones*

- **FBX Import node** (node)
  - Loads FBX animations and converts to openpose using Blender in background
  - *From: metaphysician*

- **Enhanced dance pose library** (tool)
  - Extended pose styles and sequences including Hip Hop, Rock Concert, Pop Dance, and Crazy Mix
  - *From: NebSH*

- **Mobile monitoring portal** (tool)
  - Web portal to monitor generations from phone with Discord alerts and remote workflow execution
  - *From: boorayjenkins*

- **WanMove LoRA extraction** (lora)
  - LoRA extracted from diff between WanMove and base models, works well on Wan 2.2 with proper block modifications
  - *From: Ablejones*

- **Automated story generation workflow** (workflow)
  - Uses GPT to create stories and prompts, then LLM creates 4 images with zimage for video generation
  - *From: VRGameDevGirl84(RTX 5090)*

- **HuMoveLora** (lora)
  - Experimental LoRA for motion control, merging WanMove capabilities
  - *From: Ablejones*

- **Spline editor clipboard copy** (tool)
  - Option to copy BG image to clipboard from embedded low quality jpg
  - *From: Ablejones*

- **SVI Pro native node** (node)
  - Native ComfyUI implementation of SVI Pro for video extension
  - *From: Kijai*
