# Wan Chatter Knowledge Base
*Extracted from Discord discussions: 2025-08-01 to 2025-09-01*


## Technical Discoveries

- **VACE 2.2 is functional**
  - Successfully working with openpose as controlnet, though results can be strange with limited controlnet types
  - *From: GOD_IS_A_LIE*

- **Wan 2.2 can handle inpainting well**
  - Model is smart enough to solve inpainting puzzles at very high denoise (0.7-0.8), going from nonsense to near perfect results
  - *From: Shawneau 🍁 [CA]*

- **GGUF Q3 may outperform FP8 in some cases**
  - User observed better quality with GGUF Q3 compared to FP8 version
  - *From: hicho*

- **Denoise parameter affects T2V generation significantly**
  - Changing denoise from default to 0.5, 0.7 produces dramatically different results in custom node implementations
  - *From: VRGameDevGirl84(RTX 5090)*

- **WANVideo wrapper now skips T5 loading when prompt is cached**
  - The text encoder won't assign weights if the prompt was cached, even if T5 is connected, improving efficiency
  - *From: Kijai*

- **WAN 2.2 supports multi-scene generation without EchoShot**
  - Can write multiple scenes separated by | in prompts, works natively with 2.2 without needing separate models
  - *From: Yan*

- **Q4 quantized model produces good quality results**
  - Tested Q4 model shows surprisingly good quality output
  - *From: avataraim*

- **Context windows work well with WAN 2.2**
  - Using context options with | separator produces smooth scene transitions in long videos
  - *From: thaakeno*

- **T2V is more dynamic and realistic than I2V**
  - T2V generates more varied and realistic motion compared to I2V which often starts slower
  - *From: seitanism*

- **Radial attention is faster than sage but requires quality tweaking**
  - RadialAttention provides speed improvements but needs careful settings adjustment to maintain quality
  - *From: Kijai*

- **WAN 2.2 frame limit for I2V is 109 frames instead of 81**
  - From 113 frames it begins to reverse/loop. Maximum is 109 frames giving +1.5 seconds of video
  - *From: N0NSens*

- **Context options can generate 15 second videos successfully**
  - 15 sec, 3 context windows achieved, though first context change is quite noticeable
  - *From: Cseti*

- **Different resolutions affect motion quality in I2V**
  - 480x720 has more motion, 576x1024 looks like slowmo. WAN 2.2 14B performs best at maximum resolution of 1024×576
  - *From: shockgun*

- **Stride settings help with window blending in context options**
  - Stride on high noise model helps window blending, no stride on low noise fixes it mostly. Successfully used 10 stride, 48 overlap
  - *From: Kijai*

- **Models from Kijai repo avoid black output issue**
  - Black output occurs when using wrapper with ComfyUI provided models, using models from Kijai repo fixes this
  - *From: crinklypaper*

- **WAN 2.2 shows improved leaf/foliage noise compared to 2.1**
  - Noise in leaves was common in 2.1 generations, not happening as much in 2.2
  - *From: Juan Gea*

- **3-stage sampling works well for I2V**
  - 9 Steps: 3H no Lora, 3H LightX2V@3, 3L@1
  - *From: BobbyD4AI*

- **CFG 3.5 technique improves adherence**
  - Using CFG 3.5 on high pass improves prompt adherence
  - *From: Juan Gea*

- **FP8 model has better adherence than quants**
  - Better luck with adherence using the fp8 model instead of the quants, and also steps above 2 for the high
  - *From: nacho.money*

- **5B model can do ultrawide generation**
  - Wan 2.2 ultrawide test at 256x2048 resolution
  - *From: Дмитрий Марков*

- **Loop args only work on 1.3B model**
  - Loop/long video strategy only ever worked on the 1.3B model, didn't blend well with anything else
  - *From: Kijai*

- **Context windows work with 5B model**
  - 5B with context windows, passing the image to each window - interesting results
  - *From: Kijai*

- **6 steps needed for low noise upscaling**
  - You need 6 steps of low noise to clean a wan 2.2 high noise generation for an upscaling latent by 2
  - *From: GOD_IS_A_LIE*

- **Different samplers needed for high/low noise**
  - You need to use euler for the low noise sampler and another one for the high noise generation
  - *From: GOD_IS_A_LIE*

- **BF16 weights may be better than FP16 for Wan 2.2**
  - Testing shows BF16 has max error 0.003890 vs FP16 max error 0.748233 when converting. Original code runs at FP32.
  - *From: Benjimon*

- **Token padding with numbers can improve motion control**
  - Adding string '1234567898765432123456789' between prompt elements may help control motion better in I2V generations
  - *From: Rainsmellsnice*

- **Context options work with piped prompts**
  - Automatically spreads piped prompts evenly over frame count, per window basis
  - *From: Kijai*

- **F16 accumulation makes massive performance difference**
  - Significantly improves generation speed
  - *From: AJO*

- **Manual prompt scheduling works well without prompt scheduler node**
  - Breaking down shots into frame stamps and adding camera movements directly in positive prompt works well for camera control
  - *From: Bleedy (Madham)*

- **First-Last-Frame works with Wan 2.2**
  - Works fantastic even without positive prompt, AI knows what to do motion wise
  - *From: Lodis*

- **Shift affects motion characteristics**
  - High shift on high model cures slow motion
  - *From: Simjedi*

- **Different shift values create style variations while retaining same actions**
  - Shift 12 stable, shift 5 adds detail, shift 3 makes subjects older/crabby, shift 1 creates abominations
  - *From: nacho.money*

- **Context windows work better with different settings for high/low noise models**
  - Low noise side doesn't need as much overlap, making it faster. Staggering overlaps helps with blending
  - *From: Kijai*

- **Wan 2.2 14B model works well for V2V upscaling from 480p to 1080p**
  - Successfully upscaled video while fixing LED lightbar issues on cars
  - *From: thaakeno*

- **High noise vs low noise models produce different results during upscaling**
  - Low noise model shows better detail for people in background during upscaling
  - *From: thaakeno*

- **Start step parameter controls how much video changes during V2V**
  - Lower start step (like 4 out of 12) changes more content but can fix motion, higher values stay closer to input
  - *From: thaakeno*

- **Wan models can generate camera operator shadows in video**
  - Model adds realistic camera shadows as if hiring a camera operator in latent space
  - *From: N0NSens*

- **Chinese prompts may work better for T2V but not I2V in Wan 2.1**
  - Native Chinese speaker reported Chinese worked well for T2V but not I2V
  - *From: JohnDopamine*

- **More steps on low noise pass improves T2I quality**
  - 30 steps on low noise and 20 on high noise results in better sharpness and quality
  - *From: 🐝 bumblebee 🐝*

- **Qwen 2.5 integrated for prompt extension with zero memory usage after completion**
  - Added to wrapper for local prompt enhancement using original system prompts
  - *From: Kijai*

- **Wan 2.2 I2V supports First Frame Last Frame (FLF) natively**
  - Unlike 2.1, Wan 2.2 I2V can work with first and last frame inputs without needing separate models
  - *From: Juampab12*

- **Wan 2.2 can be used for V2V upscaling**
  - Using high start step (like step 9 out of 12) to minimize changes while upscaling
  - *From: thaakeno*

- **Can combine Wan 2.2 high + 2.1 low for smooth refinement**
  - Using high 2.2 + 2.1 with 2 steps denoise of 0.10 to smooth the high while keeping its look
  - *From: hicho*

- **First frame + last frame conditioning works well with Wan 2.2 for 161 frames (10 seconds)**
  - Works pretty well but is slow to generate
  - *From: comfy*

- **Non-guiding frames are grey in Wan 2.2 - can manually feed grey and normal frames as start image**
  - For 2.2 first frame only: [first frame] + [x grey frames], last frame: [x grey frames] + [last frame]
  - *From: comfy*

- **Middle frame conditioning works with proper implementation**
  - Kijai confirmed middle frame works, showing start to end to start transitions
  - *From: Kijai*

- **Sage attention provides minimal quality difference but massive speed difference vs flash attention**
  - Sage attention recommended over flash attention for speed
  - *From: Kijai*

- **Context options with stride 8+ improves continuity for longer videos**
  - Increasing stride to 8 or more improves continuity with context options
  - *From: xwsswww*

- **VACE 2.2 compatibility is limited**
  - Some modalities don't work at all, some work weakly. Nothing worth using over 2.1 VACE for high noise model
  - *From: Kijai*

- **Wan 2.2 naturally supports first-last-frame morphing without special implementation**
  - Model itself handles FLF without needing special fork or fancy implementation, works with both methods
  - *From: Kijai*

- **Different prompts on high vs low noise passes - low noise pass ignores different prompts**
  - Using completely different prompt on low noise pass didn't add or change anything
  - *From: Kagi*

- **Video models can handle random training techniques that wouldn't work on image models**
  - Video models just figure things out, can get away with techniques that probably wouldn't work in image models
  - *From: Fill*

- **Wan 2.2 model architecture allows parallel video generation**
  - 20 videos at 512 bucketed resolution, 49 frames rendered in 6 minutes total
  - *From: Fill*

- **bf16 precision produces better quality than fp16 and fp8**
  - Visual comparison shows bf16 has most details in generated videos, though sometimes 'goes too much' on certain elements
  - *From: Kijai*

- **Original Alibaba code converts model to bf16 not fp16**
  - The original code uses bf16 and doesn't quantize the VAE at all, producing higher quality than ComfyUI
  - *From: aikitoria*

- **Wan 2.2 original VAE is designed for higher resolution**
  - The new VAE doubles compression on each axis, suggesting it's meant for 2560x1440 video generation which hasn't been released
  - *From: aikitoria*

- **Mixed precision models preserve quality**
  - Using fp32 for norms and fp16 for weights (99% fp16, 1% fp32) improves listening/adherence to prompts
  - *From: Benjimon*

- **First-Frame-Last-Frame (FFLF) feature works well for morphing**
  - FFLF allows morphing between start and end images, produces good transitions with some fog/dust in middle parts
  - *From: MACRO*

- **FP8 vs BF16 quantization testing shows minimal differences in quality**
  - FP8 sometimes performs better than BF16 in specific scenarios - BF16 character didn't eat ice cream while FP8 did, FP8 had leaves swinging in wind while BF16 had static pines
  - *From: Kijai*

- **Batch size affects temporal stability**
  - Higher batch size leads to more temporally stable video generation according to official repo
  - *From: MiGrain*

- **Wan 2.2 is essentially 28B parameters total**
  - The combined size of high and low noise models makes it massive
  - *From: Draken*

- **Video models quantize very well**
  - Models are larger than needed considering how well they compress with quantization
  - *From: Draken*

- **Character LoRA trained in 9 minutes with good results**
  - Low_noise_model T2V 14B, 24 source images at 512px resolution, training time 9min with min_t=0, max_t=1
  - *From: Kenk*

- **5B model can upscale 14B output effectively**
  - 1280x768 output from 14B can be upscaled to 1090x1152 with 5B using 0.5 denoise, providing same starting frame and simple quality prompts
  - *From: Juan Gea*

- **Maximum resolution achieved: 2560x1536 for 81 frames**
  - Upscaling from 14B at 1600x960 using 5B model
  - *From: Juan Gea*

- **Sigma value 0.875 intended for model switching**
  - Wan team intended the high/low noise model switch at sigma 0.875, occurs at step 8/20 with shift=5.0, step 10/20 with shift=8.0
  - *From: Ablejones*

- **Model doesn't like changing object states**
  - Difficult to get model to show ice cream being stolen - it maintains woman has ice cream even when it should be gone
  - *From: Kijai*

- **Prompt scheduling works with context options in wrapper**
  - Can use format [1] Prompt 1, [2] Prompt 2 for extending videos - cuts frames uniformly and applies prompt to each segment
  - *From: mamad8*

- **LoRA timestep scheduling added to wrapper**
  - Only works when unmerged, can schedule per step (0 skips applying it altogether on that step), enables curves and dropoff control
  - *From: Kijai*

- **Disabling LoRA on first step improves quality**
  - Since lightx2v doesn't work properly with high noise model, do first step(s) with cfg instead without LoRA loaded
  - *From: Kijai*

- **Wan understands multiple languages well**
  - Sometimes even better than English - Finnish prompts worked with good understanding
  - *From: Daflon*

- **Chinese prompts give better prompt adherence on Wan 2.2**
  - Heard to give way better prompt adherence compared to English prompts
  - *From: thaakeno*

- **Shift 1 produces better T2I results than default shift values**
  - Using shift 1 for text-to-image generation gives perfectly sharp images, even though this doesn't respect the intended boundary between high/low noise models
  - *From: aikitoria*

- **LightX LoRA helps add details in T2I**
  - Using LightX at 0.5 strength on second pass with 20 steps each improves detail quality compared to no LoRA with 40 steps
  - *From: VRGameDevGirl84(RTX 5090)*

- **Prompting has much stronger impact in Wan 2.2 than 2.1**
  - The prompt has a much stronger impact on output quality in Wan 2.2, with detailed Claude-generated prompts producing better results on first try than manual prompting
  - *From: Alisson Pereira*

- **Shift value dramatically affects Wan 2.2 output quality**
  - Shift 12 matches original Alibaba code timesteps but may cause too much movement/instability. Users found different optimal shift values work better in practice.
  - *From: aikitoria*

- **T2V and I2V use opposite step ratios in official implementation**
  - T2V uses 25 steps high noise, 15 steps low noise. I2V uses 15 steps high noise, 25 steps low noise. Makes sense because I2V already has image so needs less composition steps.
  - *From: aikitoria*

- **LightX2V LoRA changes Wan 2.2 behavior significantly**
  - Using LightX2V makes 2.2 output more like 2.1 with less realistic motion. Even one step without LightX gives vastly more 'real' looking motion.
  - *From: Draken*

- **Beta scheduler works better than simple scheduler at shift 12**
  - Beta scheduler has more gradual dropoff which helps when using LoRA for low noise section only
  - *From: Ablejones*

- **Wan 2.2 5B last frame encoding works when done separately**
  - Previously thought it didn't work at all, but encoding the last frame separately makes it functional
  - *From: Kijai*

- **Wan 2.2 High Noise Expert provides significantly better motion than 5B model**
  - Quality is fine on 5B but the motion doesn't come close to what the high noise can do
  - *From: Kijai*

- **Wan 2.1 LoRAs work on Wan 2.2 Low Noise with minimal compatibility issues**
  - You can use old loras on 2.2 low mostly just fine, but they fall short when character is wide-distance or heavy motion scenes
  - *From: Kijai*

- **Wan 2.2 Lightning LoRAs had hardcoded alpha values causing issues**
  - Alpha 8, rank 64 = 0.125 strength. Original LoRAs didn't include alpha and had it hardcoded in the code
  - *From: Kijai*

- **Higher shift values needed for Wan due to linear scheduling**
  - Wan is linear and needs a high shelf at start. Shift around 8-9 is good for short steps
  - *From: Simjedi*

- **VACE strength affects generation behavior significantly**
  - High strength like 1 tries to put your ref or prompt subject on the masked area. Lowering the strength gives it more freedom to give a more realistic form
  - *From: SonidosEnArmonía*

- **New Wan 2.2 Lightning LoRAs work at 1.0 strength instead of 0.125**
  - Kijai's fixed versions can be used at 1.0 strength making them easier to control
  - *From: Kijai*

- **Lightning LoRAs work better on high noise side only**
  - There's no real need to run the new lightning LoRA on the low noise side
  - *From: Kijai*

- **Old lightx2v can still be used on low noise side for styling**
  - You can use the old lightx2v on the low side if you prefer it, as it affects the final look and detail level
  - *From: Kijai*

- **Single CFG 3.5 step without LoRA improves lighting**
  - Better lighting results with: 1 step w/ cfg=3.5 (no lora), then remaining steps with cfg=1 and new LoRAs
  - *From: IceAero*

- **3+1 sigma split works better than even splits**
  - For 4 total steps, 3 high noise steps and 1 low noise step works better than 2+2
  - *From: Kijai*

- **New LightX2V Lightning LoRAs for Wan 2.2 released with 4-step generation capability**
  - Wan 2.2 Lightning LoRAs can generate videos in 4 steps vs previous higher step counts
  - *From: gokuvonlange*

- **Old LightX2V 2.1 LoRA works better on high noise pass than new 2.2 Lightning LoRA**
  - Mixing old 2.1 LoRA on high noise with new 2.2 Lightning on low noise produces better results
  - *From: Doctor Shotgun*

- **New Lightning LoRAs do not include text embed layers**
  - Lightning LoRA missing text embed layers which have significant effect on LightX2V performance
  - *From: Kijai*

- **720p resolution works better than 480p for Lightning LoRAs**
  - 480p results in slow motion and weird artifacts, 720p produces faster motion
  - *From: Kijai*

- **Lower LoRA strength values on first steps of generation produce less fake-looking results**
  - Using 0.4 strength for high LightX and 0.6 for low LightX on early steps looks more natural
  - *From: PATATAJEC*

- **Lightning LoRA strength scheduling with list of floats**
  - Can now provide a list of float values for LoRA strength scheduling across steps in the wrapper
  - *From: Kijai*

- **FastWan 5B model performance**
  - FastWan 5B can generate 121 frames at 1280x704 in ~14 seconds sampling + ~20 seconds decode, total ~34 seconds
  - *From: Kijai*

- **Lightning LoRA works better on Low Noise model**
  - Lightning 2.2 LoRA for low noise model performs well, not much difference vs no LoRA at higher CFG/more steps
  - *From: gokuvonlange*

- **GGUF model quality correlation**
  - Higher GGUF model sizes (Q8 vs Q6_K) provide better prompt adherence and video quality
  - *From: Kijai*

- **Using both lightx2v and lightning loras together can improve motion**
  - When applied like the lightx2v lora, camera motion improves but character motion decreases. Using both loras could fix the motion altogether
  - *From: Rainsmellsnice*

- **New lightning lora degrades quality and motion significantly**
  - The new lora honestly really degrades the quality and motion, only use it on the low noise model if you want full motion
  - *From: flo1331*

- **Chinese text prompts may work with Wan models**
  - Model prompts in Chinese just fine, wouldn't say it's any better or worse than English. Text encoder being better in one language for specific words due to English ambiguity
  - *From: TK_999*

- **T2V loras can work on I2V with some success**
  - T2V loras like fastwan work on I2V, kind of weird what works with what and what doesn't
  - *From: mdkb*

- **Torch compile reduces VRAM and speeds up generation with no quality impact**
  - It has no quality impact, reduces VRAM used and speeds up generation, win-win. Hard part is installing Triton on Windows
  - *From: Kijai*

- **LightX2V 2.1 loras work better than new Lightning loras**
  - Multiple users report switching back to LightX2V after testing Lightning
  - *From: screwfunk*

- **Mixing old and new LightX loras gives good motion results**
  - New lora in high (1 strength) and old lora in low (1.5 strength), 7-8 steps total, both cfg 1
  - *From: Ashtar*

- **High model encodes significant data into latents**
  - Base colors and motion are already there after 3 steps on high noise side
  - *From: Kijai*

- **2.1 loras work differently on high vs low models**
  - 2.1 loras need 3x strength on high model but work normally on low model, low model is basically just 2.1
  - *From: Kijai*

- **Qwen Image VAE is finetune of Wan 2.1 VAE**
  - New Qwen image model reuses wan's VAE encoder/latent space with new image decoder, significantly higher reconstruction quality
  - *From: spacepxl*

- **Wan 2.2 FLF (First-Frame-Last-Frame) produces exceptional quality**
  - Multiple users report Wan 2.2 FLF as superior to other FLF implementations, with excellent character consistency and environment generation
  - *From: thaakeno*

- **Stacking specific LoRAs dramatically improves Wan 2.2 I2V quality**
  - Using phantom fusionx + pusa + lightx2v LoRAs together provides much better I2V results than lightning LoRA alone
  - *From: Ada*

- **Lightning LoRA falls apart on complex prompts**
  - The new lightning LoRA works fine for simple prompts but fails on complex scenarios that base Wan 2.2 handles well
  - *From: Kijai*

- **Using cfg with lightx2v LoRA enables 2.2-style motion**
  - Combining lightx2v LoRA with cfg provides the characteristic Wan 2.2 motion quality, though it's slower at 6 steps
  - *From: Kijai*

- **Scene cutting technique for subject preservation**
  - Can input an image and use prompts like 'the scene abruptly hard cuts to' or 'the scene immediately changes to' to maintain subject resemblance without VACE or Phantom. Works with prompt structure: Original Subject Description + Scene Cut Prompt + New Scene Description
  - *From: Jonathan*

- **Lightning LoRAs work better with proper timestep scheduling**
  - Lightning 2.2 requires euler/simple with shift of 5.0 and flowmatch_distill scheduler matching their timesteps for 4 steps
  - *From: Kijai*

- **dpmpp_2m sampler much faster on Wan 5B**
  - dpmpp_2m is 2-4x faster than other samplers like euler on Wan 5B native, though output quality may be compromised
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Multiple VACE processing behavior**
  - When using same reference image in both VACE embeds, it's calculated twice and can't be separated. Mask part is especially problematic when using multiple VACEs
  - *From: Kijai*

- **WAN and Qwen-Image VAEs are virtually identical**
  - Testing shows 99.98% compatibility with MSE of 0.000040 and PSNR of 43.95dB. They share same architecture components, hyperparameters, and latent statistics
  - *From: fredbliss*

- **You can decode WAN videos with Qwen-Image VAE**
  - Cross-compatibility works - can generate WAN video and decode with Qwen-Image VAE, producing interesting results
  - *From: fredbliss*

- **Two reference images at different aspect ratios work well with WAN 2.2**
  - Using 2 reference images with WAN 2.2 at different aspect ratios produces good results for scene transitions
  - *From: Jonathan*

- **Scene transition prompts maintain character resemblance in I2V**
  - Using prompts like 'the scene immediately and abruptly cuts to' with character descriptions maintains likeness better than other methods
  - *From: Jonathan*

- **VAE tile size optimization significantly reduces decode time**
  - Using tile sizes 512x384 instead of default 272x144 cuts VAE decoding time in half on 16GB VRAM
  - *From: patientx*

- **Quantizing Qwen2.5-VL encoder has much larger impact than VAE differences**
  - PSNR drops to 35.17dB when quantizing the encoder vs 43.95dB for VAE differences
  - *From: fredbliss*

- **Qwen VAE doesn't work for video decoding**
  - The qwen vae doesn't work for video output, though you can use it for encoding
  - *From: aikitoria*

- **Qwen image has superior text rendering**
  - Text in qwen image is insanely better - they dynamically created ppts to train off of
  - *From: fredbliss*

- **Adding 'on a white background' improves reference consistency**
  - Makes it properly use the reference consistently for I2V workflows
  - *From: Jonathan*

- **Different LightX ranks for different workflows**
  - T2I uses rank 64, I2V uses rank 32
  - *From: N0NSens*

- **Wan 2.2 14B is native 16FPS**
  - The 14B model generates at 16fps natively, while 5B can do 720p 24fps
  - *From: Kijai*

- **5B model has different latent space requirements**
  - Some resolutions won't work - 1280x720 won't work but 1280x704 will
  - *From: Kijai*

- **WAN 2.2 5B model performs better with hands than Kling Master**
  - Even though limited to 1280x720 locally on 4090, WAN 2.2 produces better hand generation than Kling Master at 1920x1080 5s generation
  - *From: Persoon*

- **WAN 2.2 5B VAE is significantly heavier than 2.1**
  - 5B VAE is 4x heavier at least - 2.1 fp32 is 480mb vs 1.4GB for 2.2, with 8x8 vs 16x16 architecture
  - *From: Kijai*

- **Lower shift values produce sharper images**
  - Shift 0.5 produces much sharper results than shift 5.0, especially for image generation
  - *From: Kijai*

- **QwenImage outputs can now be used directly in WAN wrapper**
  - Added functionality to use QwenImage latent outputs directly without PNG write, includes scaling back for compatibility
  - *From: Kijai*

- **Specific prompt structure maintains character consistency**
  - Using detailed character descriptions with 'maintains exact appearance' and hard cut transitions helps retain similarity across scenes
  - *From: Juampab12*

- **Kijai's custom prompt splitting method works better than EchoShot implementation**
  - Using | character for prompt splitting works as well or better than EchoShot's method, and worked before EchoShot came out. EchoShot implementation often doesn't trigger properly
  - *From: Kijai*

- **EchoShot may just be a finetune with better weights**
  - Results suggest EchoShot works better with their specific weights rather than adding novel functionality
  - *From: Kijai*

- **VACE 2.2 compatibility issues traced to patch_embedding differences**
  - Big part of VACE not working on 2.2 is that the high noise patch_embedding is totally different from 2.1
  - *From: Kijai*

- **Lowering VACE strength gives model room for coherence**
  - More strength in first steps to fix composition and movement, lower strength in later steps allows model to build its own coherence
  - *From: Nekodificador*

- **Reference image background affects results significantly**
  - Using SDXL refined reference instead of original reference dramatically improved results
  - *From: Nekodificador*

- **Using DisableNoise node instead of RandomNoise when continuing generation**
  - When continuing a generation from saved latent, use DisableNoise node instead of RandomNoise to avoid adding unnecessary noise that won't be removed in remaining steps
  - *From: Ablejones*

- **Merging VACE 2.1 with Wan 2.2 models for reference following**
  - Can merge VACE 2.1 patch embedding and block 0 with 2.2 models to get reference following capability, though motion quality may be affected
  - *From: Kijai*

- **Block 0 adjustment affects identity vs motion tradeoff**
  - Adjusting block 0 can improve identity matching but reduces motion quality - need to balance the merge weights
  - *From: Kijai*

- **Early blocks have strongest effect in model merging**
  - Early transformer blocks typically control composition while later blocks handle style/refinement
  - *From: Kijai*

- **2.2 14B can handle up to 109 frames for I2V**
  - While trained on 81 frames, can generate up to 109 frames with I2V, though motion may loop back after training limit
  - *From: N0NSens*

- **LightX2V LoRA from version 2.1 performs better on T2V than the 2.2 Lightning**
  - Doesn't reduce prompt adherence as much. Used strength 2 for high noise model and 1 for low noise model with faithful element following
  - *From: shuzhi*

- **Perfect cinematic resolution found for radial attention**
  - 1216x512 (21:9 ratio) with 350s render time provides good balance between quality/speed
  - *From: : Not Really Human :.*

- **FP8 handles block swap better than GGUFs for higher resolutions**
  - Achieved 1600x900x81 frames on 3060 12GB where before was limited to 41 frames
  - *From: mdkb*

- **VACE frames need to be black for proper conditioning**
  - White or grey frames cause major issues. Black frames make huge, reliable difference
  - *From: Piblarg*

- **Speed LoRAs have colossal effect on changing image style**
  - LightX turns everything into anime. Lightning and LightX have significant style influence beyond just speed
  - *From: Дмитрий Марков*

- **Waver 12B model as good as Veo3**
  - New 12B DiT model using flow matching, performs on same level as Veo3 on video arena, uses 32B Qwen2.5 text encoder
  - *From: yi*

- **ComfyUI frontend update broke VHS previews**
  - Latest ComfyUI frontend package caused preview issues that were fixed by updating VHS nodes
  - *From: Kijai*

- **Add noise setting creates dreamy effects in FlF2V**
  - Using add noise with higher shift values (8-10) in FlF2V creates dreamy morphing effects when using LoRAs
  - *From: piscesbody*

- **LightX2V 2.1 outperforms 2.2 Lightning LoRA**
  - Lightx2v (high noise strength set to 2) consistently outperforms the 2.2 lighting one
  - *From: shuzhi*

- **Frame count affects style consistency**
  - More frames move generation closer to prompt - frame 1 is comical, frame 5 is mixed, frame 9 moves to realism
  - *From: Дмитрий Марков*

- **VACE character swapping works with Wan 2.2**
  - VACE module with Low noise fp8_e5m2 Wan t2v 14B model with image ref and SAM2 points editor swaps characters perfectly
  - *From: mdkb*

- **New T2V 1.1 LoRA works better on I2V workflows than I2V LoRA**
  - Multiple users report better results using the T2V 1.1 LoRA for I2V generation compared to the dedicated I2V LoRA
  - *From: NebSH*

- **New Lightning LoRAs work with all CFG steps on HN model**
  - Can use 4 HN steps at cfg=3.5 with the LoRA without ruining anything, unlike 2.1 where cfg=1 was needed
  - *From: IceAero*

- **LoRA rank inspection available on HuggingFace**
  - Can inspect LoRA ranks at https://huggingface.co/Kijai/WanVideo_comfy/tree/main/Lightx2v with ffn layers up to rank 319
  - *From: Kijai*

- **Lightning LoRAs refuse to do dark/night scenes**
  - LoRAs force daylight scenes and break on dark prompts, likely due to dataset limitations
  - *From: Kijai*

- **First step without LoRA enables dark scenes**
  - Using a single pre-step without LoRA allows dark scene generation, then apply LoRA for remaining steps
  - *From: IceAero*

- **Lightning 1.1 LoRA causes severe issues with motion and lighting**
  - New lightning LoRA dramatically redraws everything between frames, causes overbrightness, destroys lighting capabilities, can't make dark scenes with dim lights
  - *From: N0NSens*

- **MagCache now supports Wan 2.2 with 1.5-2x speedup**
  - Official support added for Wan 2.2 with significant speed improvements
  - *From: NebSH*

- **ATI team added motion transfer trajectories tool**
  - New code for creating motion transfer trajectories from a video, works as a script based on co-tracker
  - *From: Kijai*

- **VACE 2.1 works with Wan 2.2 including High Noise model**
  - Works with specific settings and strengths, requires custom workflow
  - *From: Ablejones*

- **Lightning I2V LoRA works well at different strength ratios for motion control**
  - 1/1 lora = slowish motion, 2/1 = fastish motion, 1.5/1 = goldilocks balanced motion
  - *From: CaptHook*

- **Wan 2.2 14B can generate at 1536x768 resolution natively**
  - Rendered in 11 minutes using Q5_K_M quantized version with Lightning I2V LoRA
  - *From: : Not Really Human :*

- **High resolution generation possible with Wan 2.2**
  - Successfully generated at 1600x960 resolution
  - *From: SonidosEnArmonía*

- **Radial sampler works inconsistently**
  - Sometimes works fine but other times produces strange artifacts depending on the seed
  - *From: N0NSens*

- **Lightning 2.2 distilled for specific resolutions and frame counts**
  - High_noise_model and low_noise_model distilled simultaneously for 81x720x1280, 81x1280x720, 81x480x832, 81x832x480 sizes
  - *From: CaptHook*

- **Wan 2.2 Fun Control has inpainting functionality combined**
  - The Fun Control code can call for mask latents, bringing it closer to VACE functionality
  - *From: DawnII*

- **Wan 2.2 Fun Control model supports 52 channels input instead of standard 48**
  - Kijai discovered the new Fun Control model has 52 channels input and couldn't identify what the extra 4 channels are for
  - *From: Kijai*

- **Fun Control model supports inpainting in addition to control**
  - The control model now also supports inpainting functionality, making it more versatile
  - *From: Kijai*

- **Lightning LoRAs force bright, well-lit daytime style**
  - The newest lightning LoRAs work well with 2.2 but force a really bright well-lit daytime style on everything, even forcing clothing colors lighter
  - *From: Ablejones*

- **MultiTalk works well but lip sync quality degrades after 7-8 seconds**
  - User getting good lip sync for 7-8 seconds in middle of 10sec generation, but quality degrades beyond that point
  - *From: hiroP*

- **Fun Control can generate 257 frames straight**
  - Kijai demonstrated generating 257 frames in one go, though quality goes down with longer generations
  - *From: Kijai*

- **Control end_percent affects WAN 2.2 stability**
  - When control end_percent is too low, it causes errors in Fun Control workflows
  - *From: DawnII*

- **Frame count changes WAN 2.2 output**
  - Using the same seed with different frame counts produces different outputs
  - *From: VRGameDevGirl84(RTX 5090)*

- **Default workflow settings may be incorrect**
  - Reddit analysis suggests some default parameters were off, particularly related to noise scheduling
  - *From: MysteryShack*

- **Control signals can extend beyond 81 frame limitation**
  - Using control signals (VACE or Fun) allows generating more than the standard 81 frame limit
  - *From: Kijai*

- **WAN automatically trims frames to 4n+1 format**
  - The model automatically adjusts frame count to fit the required mathematical format
  - *From: Nekodificador*

- **Wan 2.2 MoE architecture uses high and low noise models with specific transition boundary**
  - Process starts with high noise model and switches to low noise at later denoising stages. Switch happens at modified_sigma boundary of 0.875
  - *From: fredbliss*

- **Lightning LoRAs should only be applied to low noise model, not high noise**
  - High noise model needs full processing power, lightning optimization works better on low noise refinement stage
  - *From: fredbliss*

- **High noise model creates rough structure, low noise refines details**
  - High noise stage outputs mostly formed structure with face and limbs outlined, low noise stage acts like vid2vid to add details and cleanup
  - *From: MysteryShack*

- **Distilled LoRAs don't reach 50% signal-to-noise ratio at same timestep as full models**
  - Sigma boundaries shift differently for distill models, making them look less formed at equivalent stages compared to full step models
  - *From: MysteryShack*

- **Fun Control models can handle both control AND inpainting simultaneously**
  - Input size difference reveals mask support, suggesting the model can do control and inpainting together
  - *From: Kijai*

- **First step should never use any LoRA to avoid slow-motion issues**
  - All distill loras should have weight of zero on first step to fix both lighting and slow-mo problems
  - *From: MysteryShack*

- **Wan2.2 VACE can be used with single frame controlnet input**
  - Using Kijai's WanVideo VACE Start to End Frame node - pass controlnet input to start image connector, output goes to native WanVaceToVideo control video input. Results in non-static video that follows prompt and can add reference image
  - *From: Lodis*

- **FP8 + FP8 operations not supported in PyTorch**
  - torch doesn't support fp8 weight + fp8 weight add or mul operations, only matrix multiplication is supported
  - *From: Kijai*

- **Split threshold for high/low noise models**
  - T2V threshold to switch is 0.875, I2V threshold is 0.9. Check sigma values in logs to determine proper split point
  - *From: Kijai*

- **14 high / 6 low steps gives better results than 11 high / 9 low**
  - Testing with euler sampler on LoRA training showed better ripples, face definition, and detail preservation with 14/6 split
  - *From: crinklypaper*

- **Vace with Wan2.2 workaround using step 2 injection**
  - Hacky vid2vid workflow that injects reference video as latents and starts denoising at step 2 on first sampler, as step 1 obliterates Vace guidance
  - *From: ingi // SYSTMS*

- **Lambda function patching with compile() prevents VRAM release**
  - Using lambda function to patch linear layer with torch.compile wouldn't let it release VRAM, but GGUF didn't have this issue as it patches the whole Linear layer instead of just forward
  - *From: Kijai*

- **FP8 implementation fixed by changing patching method**
  - Implemented fp8 same way as GGUF (patching whole Linear layer instead of lambda forward) and VRAM issue is gone
  - *From: Kijai*

- **Sapiens can find 11 people maximum**
  - Sapiens detected up to 11 people in a 192 frame video, took about 5 minutes on 4090
  - *From: fredbliss*

- **TorchScript + AMP provides best performance for Sapiens**
  - 30-40% faster than original PyTorch, works with bfloat16/fp16 for memory savings, production-ready and portable
  - *From: fredbliss*

- **BFloat16 models offer 50% memory reduction**
  - Native BF16 models provide 50% memory reduction with <0.5% accuracy loss on Ampere+ GPUs
  - *From: fredbliss*

- **Wan 2.2 supports split-screen prompts**
  - Can generate split-screen videos with detailed prompts describing synchronized perspectives
  - *From: 🦙rishappi*

- **Meta's BF16 models don't work with PyTorch >2.0**
  - The published bf16 models from Meta have compatibility issues with newer PyTorch versions
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Frame count affects slow motion in Wan 2.2**
  - At 81 frames, videos show slow motion effect. Reducing to 77 frames eliminates slow motion. This is likely because 81 doesn't match Wan 2.2's 16-frame architecture (16 x 5 = 80)
  - *From: xwsswww*

- **Bypassed LoRA nodes can cause workflow issues**
  - Bypassed LoRA nodes can be saved in a bad state, causing 'Required input is missing: model' errors. Unbypassing and rebypassing the LoRA nodes fixes the issue
  - *From: TK_999*

- **GGUF models show cleaner results than fp8 scaled**
  - Comparison between GGUF 2.2 and ComfyUI scaled fp8 shows GGUF produces cleaner results. The difference is larger with LoRAs due to how they're applied
  - *From: Draken*

- **Prompt content affects slow motion in Wan 2.2**
  - If prompts don't have enough action for 81 frames, the model stretches it out creating slow motion. More action in prompts allows full speed at higher frame counts
  - *From: Hashu*

- **GGUF version improves image quality and sharpness**
  - GGUF version makes text in ground sharp and creates more realistic interiors compared to FP16, though it adds unwanted elements like cars
  - *From: Drommer-Kille*

- **GGUF vs FP16 performance comparison**
  - FP16: 107.66 seconds, GGUF: 97.05 seconds for same prompt
  - *From: Drommer-Kille*

- **Wan 2.2 14B is 16fps, not 24fps**
  - Only the 5B model runs at 24fps, 14B variant is still 16fps
  - *From: Drommer-Kille*

- **V2V workflow for style refinement**
  - Can feed video to wrapper samples input for V2V processing, acts like denoise control by adjusting low-high step cutoff point
  - *From: Drommer-Kille*

- **Combining Vace 2.1 with Wan 2.2 for enhanced realism**
  - Using Vace as first pass then Wan 2.2 as second pass adds significant realism that Vace alone cannot achieve
  - *From: Drommer-Kille*

- **SeedVR2 VRAM usage scaling**
  - 480p->720p 81 frames took 760 seconds, 720p->1080p uses 98% VRAM on RTX 3090
  - *From: Hevi*

- **Fun 2.2 control model can do temporal inpainting**
  - The new Fun 2.2 control model appears capable of temporal inpainting functionality
  - *From: Kijai*

- **Fun 2.2 control model lost reference input capability**
  - The Fun 2.2 control model no longer works with reference inputs, unlike Fun 1.1 which still works with reference
  - *From: Kijai*

- **Fun 2.2 control refuses to work beyond 81 frames**
  - The model won't move at all if trying to generate more than 81 frames
  - *From: Kijai*

- **Wan 2.2 has attention sinks that could enable extension**
  - Similar to LLMs with BOS tokens, finding attention sinks in Wan could enable video extension capabilities
  - *From: fredbliss*

- **ComfyUI progress bar interrupt now frees memory**
  - Fixed the progress bar to catch interrupts in try/except block, now properly frees memory when generation is cancelled
  - *From: Kijai*

- **Wan 2.2 low noise model can be used as an upscaler by swapping it for 2.1 model**
  - Works in same workflow setups, can achieve 1600x900x81 frames on 3060 GPU
  - *From: mdkb*

- **Skyreels LoRA can help break 121 frame loop in 2.2**
  - When applied, allows old man to leave frame in 121 frame generation, addresses looping issue
  - *From: Kijai*

- **5B controlnet support available**
  - Traditional depth controlnet works with 5B model, generates in few seconds
  - *From: Kijai*

- **FastWan 5B released**
  - Available for few days, used for controlnet tests
  - *From: Kijai*

- **2.2 I2V low noise behaves differently than 2.1 I2V when used standalone**
  - Notable behavioral differences observed
  - *From: Kijai*

- **Official Flash version claims 12x faster inference speed than Wan 2.1**
  - Reasoning speed improvement, though translation may be unclear
  - *From: scf*

- **Fun models handle composited control inputs**
  - Fun models used to handle composited control inputs fine
  - *From: Kijai*

- **Block swap has minimal speed impact on high-end systems**
  - Transfer time ~0.1 seconds per block on high-end systems, but first block transfer can take 5+ seconds on some systems
  - *From: Kijai*

- **WAN 2.2 I2V loops at 121 frames**
  - 2.2 I2V generally just loops at 121 frames
  - *From: Kijai*

- **Skyreels LoRA allows 121 frames**
  - Skyreels 720p is trained on 121 frames, allows extending WAN 2.2 to that length
  - *From: Kijai*

- **Block swap profiling shows compute dominates transfer time**
  - Most blocks show compute_time of 0.2-0.3s vs transfer_time of 0.0001-0.0002s
  - *From: Kijai*

- **Prefetch option significantly improves block swap performance**
  - Makes generation 1 minute faster (on 6 minute total) for 3090
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Lightning + LightX2V LoRA combination works well**
  - Lightning LoRAs at strength 1.0 followed by older LightX2V LoRAs at 0.2-0.5 strength clears up imaging and acts like glue for multiple LoRAs
  - *From: screwfunk*

- **2.2 works better at 1280x720 than 480p**
  - Lightning LoRAs or wan2.2-fun had significantly less artifacts at 720p vs 480p
  - *From: ArtOfficial*

- **WAN fp8 fits on 5090 without block swap**
  - wan fp8 fits quite nicely on the 5090, no need for block swap
  - *From: pagan*

- **Skyreels LoRA works with T2V when configured correctly**
  - Wan2_1_Skyreels-v2-I2V-720P_LoRA works with T2V using high = [3.5,3.5,4,4] (float list) and low = 2.0
  - *From: avataraim*

- **LoRA strength scheduling improves results**
  - Can schedule LoRA strength from 2.0 to 1.0 over steps for better convergence
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Wan 2.2 14B naturally runs at 16fps**
  - Both Wan 2.1 and 2.2 14B models output at 16fps natively
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Frame count limits for looping**
  - Up to 109 frames there are no loops, after 121 frames looping can break
  - *From: N0NSens*

- **VACE can handle very long sequences**
  - With VACE on 2.1, generated 350 frames in one go, worked much better than context
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Wan 2.2 wrapper calculates denoise based on steps differently than native**
  - Wrapper does denoise calculation based on steps unlike native - need to increase steps to get more denoising steps
  - *From: DawnII*

- **Stand-In LoRA uses shared attention mechanism**
  - Much cleaner than having extra latent in sequence all the way, uses shared attention for face consistency
  - *From: Kijai*

- **Stand-In input image resolution is handled separately**
  - Input image doesn't have to be same resolution as output, handled separately. In their code it's always 512x512
  - *From: Kijai*

- **Stand-In is trained at 24FPS**
  - The Stand-In model was trained at 24 frames per second
  - *From: mamad8*

- **torch.compile caches for same input size only**
  - Torch compile issue where it caches for the same input size only, causes varying performance
  - *From: Kijai*

- **Stand-in LoRA works better with larger reference images**
  - 640x640 worked better than 512x512, and higher resolutions like 768x768 and 1024x1024 show improved results
  - *From: Kijai*

- **Can use multiple reference images in a batch**
  - Repeated same reference image 8x in a batch, works without errors and may improve results
  - *From: Kijai*

- **Stand-in LoRA doesn't work well with Wan 2.2 high noise**
  - Limited effect on 2.2 high noise setting, better suited for other configurations
  - *From: Kijai*

- **Lightning i2v LoRA performs better than t2v version**
  - i2v lightning just 'works' way more compared to t2v lightning which requires more settings adjustment
  - *From: Draken*

- **res_2s sampler gives better results**
  - Does double the steps in essence, provides nicer results due to higher order method with smaller truncation error
  - *From: Draken*

- **Stand-in doesn't work well with Wan 2.2 LOW model but works very good with Wan 2.1**
  - Confirmed through testing, compatibility issue specifically with 2.2 LOW
  - *From: Hevi*

- **Skyreels v2 can push Wan to 121 frames**
  - Using Skyreels v2 LoRA allows extending video length to 121 frames
  - *From: NebSH*

- **Q8 quantization is very close to fp16 quality**
  - Visual comparison shows minimal difference between Q8 and fp16, with Q8 being much more efficient
  - *From: Kijai*

- **Native Wan implementation does automatic block swapping while wrapper doesn't**
  - Native reports as partial load and manages VRAM automatically, wrapper needs manual block swap setting
  - *From: Kijai*

- **Uni3c control helps stabilize context windows for long generations**
  - Using Uni3c to lock camera makes context windows stable for extended video generation
  - *From: Kijai*

- **FP8 e4m3fn models need to be replaced with e5m2 versions to avoid torch compile errors**
  - FP8 e4m3fn not supported in certain architectures, need e5m2 instead
  - *From: Hevi*

- **Wan 2.2 LN (Low Noise) model can be used standalone as an improved version of Wan 2.1**
  - The Low Noise model from Wan 2.2 works by itself and is essentially a further trained version of Wan 2.1 with better quality
  - *From: Ablejones*

- **You can extract a LoRA from Wan 2.2 LN using Wan 2.1 as base**
  - Users can create a LoRA from the Wan 2.2 Low Noise model to apply its improvements to other Wan 2.1 models like Phantom
  - *From: Ablejones*

- **Wan 2.2 LN shows massive upgrade from 2.1**
  - Users report significant quality improvements when switching from Wan 2.1 to Wan 2.2 LN model
  - *From: Josiah*

- **Fun Control has different patch embedding structure**
  - Fun Control uses 52 input channels (16+16+16+4 for noise + image cond + control + mask) vs T2V's 16 channels and I2V's 36 channels
  - *From: Kijai*

- **Wan 2.2 doesn't snap strongly to init images**
  - The 2.2 low noise model recreates the first frame but then quickly diverges from the init image, which could be useful for context windows
  - *From: Kijai*

- **VACE with guidance frames allows fewer steps without acceleration LoRAs**
  - When using guidance frames via VACE, you can use as few as 8 steps without needing distillation LoRAs
  - *From: pom*

- **Stand-In reference LoRA provides good likeness when properly configured**
  - Users found that Stand-In can provide good likeness results, but proper masking and single-person prompts work better
  - *From: Intellectus Prime*

- **FantasyPortrait working for face motion transfer**
  - Face motion transfer adapter for Wan 2.1 14B is functional, though still work in progress
  - *From: Kijai*

- **Fun 2.2 camera control expects normal I2V model for low noise sampler**
  - Camera control workflow requires normal I2V model, not the Fun model for the low noise sampler
  - *From: Kijai*

- **fp8 scaled Fun 2.2 control models don't work if ref_conv layer is in fp8**
  - Reference functionality fails silently when this specific layer is in fp8 format
  - *From: Kijai*

- **Stand-in doesn't work with VACE + MultiTalk combination**
  - Testing showed it couldn't get good results when combining all three, though stand-in + VACE or stand-in + MultiTalk works fine individually
  - *From: piscesbody*

- **MAGREF works well with context windows using reference latents**
  - Can utilize reference image instead of first frame for context windows, works better than traditional I2V for this use case
  - *From: Kijai*

- **Fantasy Portrait works surprisingly well with animals**
  - Cat test showed good results despite being designed for human portraits
  - *From: Kijai*

- **PyTorch 2.7 to 2.9 upgrade reduces RAM usage**
  - WSL2 RAM usage dropped from 85gb to 65gb for 2 sampler wan22 workflows
  - *From: pagan*

- **Wan 2.2 Fun InP models work, but Fun Control Camera model has issues with GGUF format**
  - Fun INP GGUF works fine, but Fun Control Camera GGUF has gradient errors and tensor type mismatches
  - *From: Daflon*

- **Stand-in LoRA works with VACE**
  - Standard workflow from Kijai's repo works, though results can be hit or miss
  - *From: ArtOfficial*

- **Phantom works with Wan 2.2**
  - Shows good character consistency across different frame counts
  - *From: Ablejones*

- **MultiTalk can work with Wan 2.2 using block swap**
  - Main wan2.2 model can be block swapped, MultiTalk fits in 23G VRAM when combined
  - *From: nacho.money*

- **Q8 GGUF models provide better quality**
  - User reports better results with Q8 GGUF compared to regular models
  - *From: xwsswww*

- **Wan 2.1 LoRAs work on Wan 2.2 but with differences**
  - Results work but camera may move away, requires prompting adjustments like 'fixed shot, static camera'
  - *From: Mngbg*

- **Q8 gguf seems to prompt faster than Q6**
  - User observed Q8 quantization performing faster than Q6 in testing
  - *From: xwsswww*

- **LightX2V rank 128 gives better prompt adherence than rank 256**
  - Lower rank LoRA showing better prompt following than higher rank
  - *From: xwsswww*

- **Rank 16 was the only one to correctly generate koala and bird scene**
  - Specific scene generation working better with lowest rank tested
  - *From: SonidosEnArmonía*

- **Higher rank LoRA is stronger but stronger isn't always better**
  - Higher rank means closer to original model it's extracted from, but may be too strong for some use cases
  - *From: Kijai*

- **Fun 2.2 trajectory control with image doesn't work with reference input but works with start image**
  - Reference image input breaks trajectory control, start image input works properly
  - *From: Kijai*

- **VACE 2.1 is better than 2.2 for VACE tasks**
  - Older version of VACE performs better than newer one
  - *From: Kijai*

- **Fun 2.2 seems lot better than 2.1 Fun**
  - Newer Fun model shows significant improvement over previous version
  - *From: Kijai*

- **FusionX is Wan 2.1 with 5-6 LoRAs saved, then single LoRA extracted**
  - Popular model is actually a composite that was then re-extracted
  - *From: Kijai*

- **Wan 2.2 I2V can do FLF (First-Last-Frame) morphing**
  - Doesn't always work but it has the capability, needs enough frames and can't do too quick transitions
  - *From: Kijai*

- **VRAM profiling shows different peaks between 1.3B and 14B models**
  - In 1.3B the FFN is the peak, but in 14B it's rarely the peak. Uncompiled shows RoPE as mountains, compiled shows attention as peaks
  - *From: Kijai*

- **Torch compile significantly reduces VRAM peaks**
  - Evens out the peaks during sampling, making memory usage more consistent
  - *From: Kijai*

- **Block swap reduces the constant memory use underneath the peaks**
  - It affects the baseline memory usage, not the peak spikes
  - *From: Kijai*

- **Wan 2.2 demonstrates world model capabilities**
  - Remembers the location of things in generated videos
  - *From: Дмитрий Марков*

- **Zero RAM usage possible with Wan 2.1**
  - Can run from start to finish with zero RAM usage using proper setup
  - *From: Kijai*

- **Native ComfyUI has automatic offloading that many users don't know exists**
  - It's always on and provides super granular weight swapping
  - *From: Kosinkadink*

- **Reserve-vram flag dramatically improves performance**
  - Using --reserve-vram 5 changed generation time from 'taking ages to do 1 step' to '90 secs with 10 steps'
  - *From: Nekodificador*

- **CFG 1.0 doubles speed by eliminating negative prompt evaluation**
  - When cfg is 1.0, negative prompt pass is disabled, meaning twice the speed since only positive prompt needs evaluation
  - *From: Kosinkadink*

- **NAG allows negative conditioning at CFG 1**
  - NAG node provides cheaper negative prompting while maintaining CFG 1 speed benefits
  - *From: DawnII*

- **Sage attention 3 improves speed with blocks set to 40**
  - User achieved better speed than ksampler workflow by setting blocks to 40 and using sage attention 3
  - *From: cocktailprawn1212*

- **Wan 2.2 understands time-based prompting**
  - Can specify '0.0 seconds- 0.3 seconds: write what u want here' to solve slow motion issues, 81 frames ≈ 0.5 seconds
  - *From: xwsswww*

- **FantasyPortrait node achieves 40 it/s on CPU**
  - AMD Ryzen 9 9900X achieves 40 it/s, initially thought to be GPU but actually runs on CPU
  - *From: Kijai*

- **VACE + Phantom combined workflow working in 1.3B model**
  - Successfully combined 1.3B VACE + Phantom (style from prompt) in a working workflow
  - *From: Kijai*

- **Phantom model can be tricked to work with VACE despite compatibility issues**
  - User managed to get phantom model working but encountered tensor size mismatch errors when trying to use VACE with it
  - *From: mdkb*

- **Lightning loras may have censoring behavior at high strengths**
  - Lightning I2V lora generates objects to block body parts at strength 0.7+, behavior stops at 0.65 strength. Does not affect lightx2v loras
  - *From: MysteryShack*

- **VACE reference works more like FaceID V2 than simple IPAdapter**
  - VACE reference requires high quality input and behaves more like FaceID V2 for identity preservation rather than a simple IPAdapter
  - *From: Nekodificador*

- **More frames causes slower motion in generated videos**
  - 33 frames vs 66 frames causes motion speed to halve, regardless of prompt modifications
  - *From: Drommer-Kille*

- **WanFM (Frame Morphing) sampling method**
  - Samples from both directions and blends - forward and reverse pass with reversed RoPE frequencies on each step, doubles sampling cost but improves morphing between frames
  - *From: Kijai*

- **ComfyUI frontend now passes data through bypassed/muted nodes**
  - Recent ComfyUI update changed behavior - bypassed and muted nodes now pass data through, breaking workflows that relied on them blocking data
  - *From: phazei*

- **Wan 2.2 naturally handles bidirectional sampling**
  - Wan 2.2 already does similar bidirectional processing internally, making WanFM potentially redundant
  - *From: Kijai*

- **Empty audio track with MultiTalk stops unwanted character talking**
  - Using empty audio with MultiTalk can shut up characters from talking when not desired
  - *From: Kijai*

- **Block swap uses disk space for memory**
  - Block swap setting stores memory overflow on disk, space doesn't automatically clear after generation completes
  - *From: ˗ˏˋ⚡ˎˊ-*

- **PUSA sampling uses more VRAM regardless of weight format**
  - Merging PUSA LoRA doesn't reduce VRAM usage because PUSA sampling itself is inherently more VRAM intensive
  - *From: Kijai*

- **PUSA is actually a whole new model in LoRA format**
  - Makes T2V able to do I2V and start/end frame functionality, trained with only 4000 videos and $500 as a cheap training method proof of concept
  - *From: Kijai*

- **RoPE implementation was incorrect for ComfyUI**
  - Had RoPE reverse wrong for comfy rope, causing low noise side to make jittery mess. Now uses default rope always with WanFM
  - *From: Kijai*

- **WanFM method works with both 2.1 and 5B models**
  - The WanFM sampling method that does forwards and backwards predictions per step works across model variants
  - *From: Kijai*

- **Low noise model in Wan2.2 primarily handles lip-syncing**
  - High noise looks like almost done LCM sampler, low noise turns that into crisp visuals and does most of the lipsyncing
  - *From: MysteryShack*

- **LCM on high noise model provides better prompt adherence**
  - LCM gives 50% noise look that the low noise model is looking for, finally achieving good prompt adherence
  - *From: MysteryShack*

- **SDPA attention needed for InFrame with fp16 models**
  - SageATTN was ruining likeness with wan t2v fp16, needed to use SDPA. SageATTN works fine on fp8 model
  - *From: hablaba*

- **MultiTalk captures song emotions realistically**
  - Extremely good at capturing emotions of songs and looks realistic compared to other methods, though quality degrades over longer generations
  - *From: seitanism*

- **VACE single image inpainting requires exactly 5 frames - first frame with the change/mask, 4 completely empty/full gray**
  - Only works with this specific setup, trying to mask all 5 frames breaks it completely
  - *From: Nekodificador*

- **VACE single image only works with wrapper, not native**
  - Native implementation has problems with single image VACE
  - *From: Nekodificador*

- **Shape and size of mask have huge impact on VACE results**
  - Much more impact than expected during inpainting tests
  - *From: Nekodificador*

- **Qwen-image latents can be bridged directly to WAN 2.2 without VAE decode**
  - Same latent format allows direct conversion from Qwen-image to WAN video
  - *From: fredbliss*

- **VACE works better than Redux for inpainting**
  - Confirmed through testing comparison
  - *From: Nekodificador*

- **81 frames = 21 latents due to 4x VAE compression**
  - Important for latent bridging calculations
  - *From: Kijai*

- **Qwen image and Wan share the same VAE and latent space**
  - Both models from Alibaba use same/similar VAE, enabling direct latent passing between models without decode
  - *From: fredbliss*

- **Negative prompts cause skull-like shapes in early diffusion steps**
  - Every generation with negative prompts shows skull shapes at first step due to how CFG works, removing negative prompt eliminates this
  - *From: SonidosEnArmonía*

- **Fantasy Portrait can work with first/last frame inputs**
  - Using extracted first and last frames from input video as start/end frames creates video-to-video workflow
  - *From: VRGameDevGirl84(RTX 5090)*

- **Video LoRA training needs both video and image datasets**
  - For video LoRAs with outfit variations, adding image dataset alongside video dataset fixes outfit generation issues
  - *From: Ryzen*

- **GGUF version of VACE_Phantom works with fp8 scaled i2v model but not with gguf**
  - Phantom_vACE merged scaled model works with scaled f8 i2v, but didn't work with gguf because Kijai's WanVideo VACE select doesn't support gguf
  - *From: xwsswww*

- **Q8 gguf gives better results than f8 scaled but f8 scaled is faster**
  - Quality vs speed tradeoff between quantization formats
  - *From: xwsswww*

- **MAGREF + context windows work well for long stable generations**
  - MAGREF being a hybrid model combined with control signals enables stable long video generation up to 700 frames
  - *From: Kijai*

- **Context windows work better in latent space**
  - InfiniteTalk does sliding windows in latent space which is better than decoded space
  - *From: Kijai*

- **MultiTalk improves lip sync in long generations**
  - Adding MultiTalk to MAGREF + Fantasy Portrait workflow significantly improves lip synchronization
  - *From: Kijai*

- **GGUF Q8 sometimes faster than FP8 in wrapper despite theoretical slowness**
  - User reported GGUF Q8 generating 486s vs FP8 505s total time, despite inference being slower
  - *From: Josiah*

- **MTV Crafter only works with 49 frames**
  - Model is hardcoded to only work with 49 frames, not 81 frames as expected
  - *From: Kijai*

- **Context window memory usage is context frames * width * height**
  - Not total frames - need enough RAM to handle frame count after decode
  - *From: Kijai*

- **InfiniteTalk uses slice-by-slice generation with noise overlap**
  - Continues from last frame with overlap in noise, new model should not degrade over time
  - *From: Kijai*

- **New 3D pose control system**
  - Controlled by 3D pose, not 2D like other pose controls. Stick figure is just visualization
  - *From: Kijai*

- **Scene cuts can be achieved through training with prompting**
  - Training model on 5 second clips with cuts in the middle, using consistent shots so model learns consistency naturally
  - *From: Ablejones*

- **MTV Crafter motion adapter works with MAGREF**
  - Extracted motion adapter from MTV Crafter and added to MAGREF, it actually does something and shows promise
  - *From: Kijai*

- **UniAnimate with MAGREF produces better results than MTV weights**
  - Using pose pred as just RGB from same predictor MTV uses, but not using MTV weights, produces superior results
  - *From: Kijai*

- **Multi-stage sampling improves Wan 2.2 motion quality**
  - Model won't do proper motion without CFG, so do some steps with CFG and no lora, or lora at lower strength
  - *From: Kijai*

- **Scene cuts work with both T2V and I2V using specific prompting**
  - Can use prompts like '[scene 1] description [cut] [scene 2]' for cuts, works well with 2/3 scenes being optimal
  - *From: NebSH*

- **Using input video directly as control video without depth works well**
  - By mistake used straight input video as control instead of depth/other controls and got good results
  - *From: VRGameDevGirl84(RTX 5090)*

- **Fun Control 2.2 works similarly to VACE for style transfer**
  - Can use ref image with input video for style transfer effects
  - *From: VRGameDevGirl84(RTX 5090)*

- **InfiniteTalk can replace MultiTalk in existing workflows**
  - Just swap the model in the multitalk slot and it works with improved results
  - *From: NC17z*

- **InfiniteTalk allows much longer video generation**
  - Went from 250 frames max with MultiTalk to 1000 frames with InfiniteTalk
  - *From: NC17z*

- **Face landmarks from Fantasy Portrait work with Fun 2.2**
  - Can use the same face landmark detection system for control
  - *From: VRGameDevGirl84(RTX 5090)*

- **Normal i2v workflow with start and end frames works as well as FLF2V**
  - Regular i2v model performs similarly to the specialized first-last frame model
  - *From: VRGameDevGirl84(RTX 5090)*

- **InfiniteTalk can generate 1000 frames using context windows workflow**
  - Just swap MultiTalk model for InfiniteTalk model in existing workflows
  - *From: NC17z*

- **InfiniteTalk uses improved looping method**
  - Continues from last frames with mixed latents, prevents quality degradation over time
  - *From: Kijai*

- **InfiniteTalk has single and multi versions**
  - Single version is 5GB vs MultiTalk's 2.7GB, trained separately for better task performance
  - *From: Kijai*

- **Qwen Image Edit requires disabling sage attention**
  - Only works if sage attention is disabled, causes black output otherwise
  - *From: Lodis*

- **Cache-none flag improves frame capacity**
  - Adding --cache-none to ComfyUI startup allows generating over 1000 frames
  - *From: samhodge*

- **InfiniteTalk works with MagRef**
  - Can combine InfiniteTalk with MagRef for identity preservation
  - *From: Kijai*

- **ByteDance MegaTTS3 has god-tier vocoder**
  - Uses semantic-like tokens despite claiming phoneme input, supports speech2speech
  - *From: MysteryShack*

- **Audio scale parameter controls conditioning strength in InfiniteTalk**
  - Audio scale 2.0 provides better results, multiplies conditioning in every case unlike audio_cfg_scale which only works with main CFG
  - *From: Kijai*

- **MAGREF provides more freedom and stability**
  - Gives more control and image doesn't degrade as much compared to normal I2V model, works better without clip embeds for stronger reference
  - *From: Kijai*

- **InfiniteTalk acts as endless I2V with audio control**
  - Model seems specifically made for this type of sampling, audio provides guidance unlike basic I2V
  - *From: Kijai*

- **Model can process silence to force mouth closure**
  - The model actually processes silence too, it can be used to force people to keep their mouths shut
  - *From: Kijai*

- **FP8 quality degradation on 2.1 models with fast settings**
  - FP8 fast has quality hit on 2.1 models, produces significantly worse quality than GGUF Q8
  - *From: iShootGood*

- **Q8 is superior to fp8 in quality but not speed on 3090**
  - Q8 GGUF provides better quality than fp8 on RTX 3090, especially with torch.compile, though fp8 is faster
  - *From: [˗ˏˋ⚡ˎˊ-]*

- **GGUF LoRAs work better unmerged**
  - Most major thing to know about using GGUF is that Loras are always used unmerged and they work better, in both native and wrapper
  - *From: Kijai*

- **InfiniteTalk adds 28 extra frames**
  - InfiniteTalk strategy adds 28 frames to generation, which can cause sync issues
  - *From: DawnII*

- **E5m2 is worse than e4m3fn quantization**
  - e5m2 quantization produces worse quality than e4m3fn, and unscaled is terrible
  - *From: Kijai*

- **GGUF models require main model to also be GGUF**
  - If using GGUF InfiniteTalk model, the main model must also be GGUF format
  - *From: Kijai*

- **Frame window size affects multitalk processing**
  - Frame window size is like context window length, should be set to frame number you generate normally (81)
  - *From: DawnII*

- **Wan 2.2 with InfiniteTalk V2V uses keyframing approach**
  - Analysis of code shows it skips every 72 frames by default, so it's not proper V2V but keyframing with start frames every 72 frames
  - *From: DawnII*

- **InfiniteTalk can work with video input through uni3c**
  - The uni3c component uses the original video, so keyframe + uni3c + talk combination is possible
  - *From: Kijai*

- **GGUF files can mix different quantization types**
  - It's perfectly fine to mix GGUF qtypes in the same file
  - *From: Kijai*

- **Uni3c node modified for automatic video slicing**
  - Edited uni3c node so you don't have to put latents in it - when using multitalk sampling it uses input video and slices by audio indices
  - *From: Kijai*

- **Block swap files are not saved on drive**
  - Block swap data is kept in memory, not written to disk storage
  - *From: Kijai*

- **Higher LoRA rank parameters have bigger effect**
  - Rank 256 produces much more movement than rank 32, especially in extracted loras like lightx2v
  - *From: 𝕯𝖗. 𝕸𝖆𝖈𝖆𝖇𝖗𝖊 ☠*

- **I2V makes crazy T2V when there is no image**
  - Wan 2.2 I2V generates interesting text-to-video results when no image is provided
  - *From: hicho*

- **Using Qwen2.5 VL then feeding to T5 for better results**
  - Process of using Qwen2.5 VL to describe image and reprompting to get base image correct before feeding to Wan2.2 I2V workflow gives crazy results
  - *From: Josiah*

- **Qwen2.5-VL best for input prompt**
  - Qwen2.5-VL will always be best for input prompt because that's what they used to train it
  - *From: fredbliss*

- **9 frame motion overlap works fine and is faster**
  - Motion frame setting of 9 works fine compared to 25 and is significantly faster (15:35 vs 20:33)
  - *From: Kijai*

- **CFG 1 doesn't use negative prompts**
  - When using CFG=1, the negative prompt is not being used
  - *From: mamad8*

- **Lightning T2V 1.1 HIGH works better than LOW model in some cases**
  - User accidentally used HIGH on LOW model and found it worked better, could be due to tuning
  - *From: phazei*

- **Swap blocks setting may only take effect on new prompts**
  - Changing from 35 to 20 swap blocks didn't show speed improvement until prompt was changed, then it went from 11 minutes to 7 minutes 30 seconds
  - *From: . Not Really Human :.*

- **MultTalk branch ksampler re-initializes timesteps and scheduler**
  - This causes it to completely ignore start and end steps of the ksampler
  - *From: MysteryShack*

- **Wan 2.2 fp32/fp16 mixed model has performance issues**
  - Model stuck at 22GB VRAM usage, did 1 step after 8 minutes with only 50% GPU utilization instead of normal 78°C
  - *From: seitanism*

- **DawnII achieved good V2V results using magref**
  - Successfully performed video-to-video generation with magref model, creating quality results
  - *From: DawnII*

- **InfiniteTalk has noise at beginning due to extra latent conditioning**
  - The noise at the beginning of InfiniteTalk generations is a feature - it expects extra latents or conditioning that aren't processed in regular ksampler pass
  - *From: MysteryShack*

- **Manual sigma scheduling works better than BetaSamplingScheduler**
  - Using manual sigmas [1.0000, 0.9375, 0.8750, 0.4375, 0.0000] on T2V gives better results than trying to adjust BetaSamplingScheduler for 4 steps
  - *From: phazei*

- **InfiniteTalk model cannot handle full noise, it never does in the loop**
  - The first frame noise issue in InfiniteTalk is caused by the model not being able to handle full noise. To fix this, encode the init image and add it to noise.
  - *From: Kijai*

- **Using the same initial frame with noise for all 81 frames can produce better T2V results**
  - Randomly tried repeating the same initial frame with noise for all 81 frames and it produced significantly better video results instead of shitty output.
  - *From: fredbliss*

- **Qwen image -> Wan video integration working via T2V**
  - Successfully got Qwen-image to Wan video pipeline working through T2V method, with aligned results when using same prompt for both Qwen image and Wan.
  - *From: fredbliss*

- **Qwen2.5-VL can be used for image captioning to generate better Wan prompts**
  - Using structured data output from Qwen2.5-VL, then rewriting into short paragraph style that Wan likes improves results
  - *From: fredbliss*

- **Qwen Image latents can be passed directly to Wan sampler without text prompts**
  - Still captures concepts from the original image even without prompt, qwen image at 1024x1024 becomes 768x768 in wan
  - *From: fredbliss*

- **Wan 2.2 I2V model behaves differently from 2.1**
  - Doesn't strongly stick to the init image, which could be useful for long I2V generations
  - *From: Kijai*

- **Light2XV LoRA from Wan 2.1 works better on Wan 2.2 than the new 1.1 speed LoRAs**
  - Settings: 3 on high noise, 1 on low noise pass
  - *From: NebSH*

- **Video looping technique improves long audio generation**
  - Generate short 3 second video with Wan 2.2, put in loop, then use with long audio for better results
  - *From: NebSH*

- **Wan model works at 729p resolution**
  - Not limited to 480p, higher resolutions work fine
  - *From: Kijai*

- **InfiniteTalk produces extra tail frames at the end**
  - Model always produces constant input, extra second of frames is normal behavior
  - *From: Kijai*

- **Start step 2 in vid2vid means first 2 steps are considered done**
  - Noise is added to input video based on what noise should be on those steps, same principle as img2img
  - *From: Kijai*

- **Audio CFG should not be close to 1**
  - Audio scale being too high changes the face, at least on 2.2 low noise
  - *From: MysteryShack*

- **GGUF VACE modules now supported**
  - Can load GGUF VACE modules, don't have to be same Q-type
  - *From: Kijai*

- **Context windows use overlapping frames**
  - Each window is 81 frames with 9 overlap for smooth transitions
  - *From: Kijai*

- **Differential diffusion for inpainting was in wrong place and never worked properly**
  - Kijai discovered the differential diffusion implementation in wrapper inpainting was incorrectly positioned, causing it to not function as intended for a year
  - *From: Kijai*

- **Wan 2.2 14B doesn't make photo prompts into actual photos unlike other models**
  - When using default sample prompt 'photo of chess playing in park', Wan 2.2 14B is first model that doesn't make it a photo, while 2.1 and 2.2 5b do
  - *From: Drommer-Kille*

- **InfiniteTalk requires finished denoised output for proper I2V chaining**
  - You can't use noisy input to I2V model - it has to finish the previous window for the method to work properly
  - *From: Kijai*

- **Normal map control in VACE bleeds into colors heavily**
  - Normal map control causes significant color bleeding issues making it unusable, though lowering saturation prevents 90% of bleed
  - *From: Blink*

- **Wan models feel like they're meant to be interpolated**
  - Raw wan output feels like it's skipping every other frame, probably byproduct of cutting 30fps videos down to 16fps
  - *From: ArtOfficial*

- **VACE inpaint mask decides which part of the video will be processed**
  - Best combination is to fill the mask with corresponding ControlNet, leaving outside unprocessed. If you blur the mask, artifacts and ghosting appear
  - *From: Nekodificador*

- **VACE reference is underrated if used well**
  - Works well for inpainting existing subjects, less effective for adding new subjects where they don't exist
  - *From: Nekodificador*

- **First-to-last frame technique for VACE**
  - Input first frame and leave rest grey/gray - gives VACE inertia but model dreams the rest. Repeating all frames makes model get stuck
  - *From: Nekodificador*

- **NAG is applied to positive conditioning, not negative**
  - With cfg 1.0, normal negative isn't used. NAG affects the positive prompt
  - *From: Kijai*

- **Mixed fp32/fp16 models show minimal difference**
  - 99% fp16 with fp32 bias adds only 6mb. Difference is honestly minimal and mostly random compared to pure fp16
  - *From: Kijai*

- **WanVideoWrapper supports Qwen text enhancement**
  - Qwen with system prompts to enhance your prompt, uses similar captioning as training data
  - *From: ˗ˏˋ⚡ˎˊ-*

- **MultiTalk uses static box masks, not frame-by-frame**
  - Multitalk node needs audio for each speaker and mask for each speaker in a batch. Uses static masks, not precise mouth targeting
  - *From: Kijai*

- **Extra latent addition improves WAN 2.2 I2V prompt adherence for jump cuts and scene changes**
  - Adding an extra latent to I2V node fixes issues with background dissolve and scene changes that were previously resulting in blackness around characters
  - *From: MysteryShack*

- **First latent as reference technique works differently than normal I2V**
  - Replacing first latent with image itself works more like VACE, where normal I2V uses full noise for first latent and image in separate 16 channel input
  - *From: Kijai*

- **Lightning LoRA is censored and affects character consistency**
  - Using lightning i2v lora gives better prompt adherence but censors content and reduces character consistency
  - *From: MysteryShack*

- **Inpainting differential diffusion code placement fixed**
  - Differential diffusion code was moved to correct place, improving inpainting results significantly
  - *From: Kijai*

- **Control splines in Blender work well for camera and object movement**
  - Using grease pencil outlines, curves and spheres in Blender for control splines provides more information than just openpose
  - *From: Blink*

- **Gradation in masks works better with differential diffusion than black/white masks**
  - Grayscale masks provide better blending results when using differential diffusion
  - *From: ˗ˏˋ⚡ˎˊ-*

- **CineScale uses 2-stage sampling process with latent upscale**
  - First sampler at 1920x1088 with RoPE [1.0, 20.0, 20.0], then upscale and second sampler at 2880x1632 with RoPE [1.0, 25.0, 25.0]
  - *From: Kijai*

- **CineScale LoRA without NTK scale produces overblown results**
  - The RoPE scaling is important for proper results, spatial base frequency is scaled while temporal stays at 1.0
  - *From: Kijai*

- **Phantom model shows decreasing consistency below 121 frames**
  - Perfect character consistency at 121 frames, clothing/face loses consistency at 81, introduces midget at 49 frames
  - *From: mdkb*

- **FP8 vs FP16 shows minimal quality difference for prompt adherence**
  - Comparisons showed hardly any quality difference between fp8 and fp16 scaled models
  - *From: seitanism*

- **Wan 2.2 with latent upscale works poorly as it's too noisy**
  - The original code finishes the gen on the first sampler, and bilinear works better than nearest exact
  - *From: Kijai*

- **Cinescale uses 1.5x upscale workflow**
  - They do full generation on first sampler (50 steps), then vid2vid on second starting from step 15 with latent upscale in between
  - *From: Kijai*

- **RoPE scaling is useful even without cinescale**
  - Messing with the rope scale seems to be useful even without cinescale
  - *From: Kijai*

- **Three sampler combination fights against slowmo**
  - 1x high (no acceleration lora, cfg 3.5, 4 steps), 1x high (acceleration lora, cfg 1, 4 steps), 1x low (acceleration too, cfg 1, 4 steps)
  - *From: Juan Gea*

- **Qwen VAE vs Wan VAE differences for single images**
  - QwenImage VAE is smoother and more aesthetically pleasing but also blurrier compared to Wan VAE for single image generation
  - *From: Kijai*

- **Qwen VAE produces better alignment in small patches compared to Wan VAE**
  - Qwen VAE produces more natural blurring while Wan VAE creates effects similar to upscalers inventing detail where there's no info
  - *From: Kijai*

- **MAGREF can adjust strength by padding images with white**
  - Even full frame it's weaker when padded, and you can use different images for context windows beyond the start image
  - *From: Kijai*

- **I2V models are incompatible with context windows by nature**
  - I2V models being start image models makes them incompatible with context windows concept, only MAGREF allows this functionality
  - *From: Kijai*

- **Skyreels LoRA works to get 121 frames and breaks looping in 2.2**
  - Successfully broke the looping in 2.2 I2V when trying 121 frames
  - *From: Kijai*

- **CineScale LoRA released for 4K video generation**
  - New LoRA came out for upscaling video generation to 4K resolution
  - *From: Kijai*

- **Wan 2.2 has ping pong effect after 81 frames**
  - Video tries to go back to first frame after 81 frames, related to 16fps training
  - *From: JohnDopamine*

- **CFG scheduling with LightX2V LoRA strength scheduling gives best results**
  - Using 6-8 total steps split at middle, first step lora at 1.0, cfg around 3, then 2nd step cfg 2, lora 2, then lora 3, cfg 1.0
  - *From: Kijai*

- **Prompt adherence is mostly from the high noise side**
  - The high noise side is responsible for most prompt adherence in WAN 2.2
  - *From: Kijai*

- **CausVid is better than other distill LoRAs for high noise**
  - CausVid performs better than alternatives for high noise sampling in WAN 2.2
  - *From: DawnII*

- **VAE decoding performance varies significantly by precision on AMD**
  - fp16: 1:16, fp32: 3:20, bf16: 2:33 for VAE decoding
  - *From: patientx*

- **MelBandRoFormer vocal separation model performs better than demucs in some cases**
  - Can separate vocals and instruments from audio, processes 3min song in 33sec
  - *From: Kijai*

- **Wan 2.2 Low I2V model produces superior quality with specific settings**
  - Using euler/beta combination, 8 steps, old lightning lora at 1.0 on 720x720 images gives vastly superior quality and details, though artifacts occur on every other gen
  - *From: gordo*

- **Speed LoRAs don't work with high noise model**
  - LightX2V and other speedup loras don't work at all with high noise model unless trained specifically for it
  - *From: MysteryShack*

- **Multi-sampler setup can make speed LoRAs work with Wan 2.2**
  - 3 sampler setup with 1 step full HN, or distribution like 3full/1lightning/3/1 with proper shift adjustments
  - *From: Karo*

- **CFG Schedule improves prompt adherence**
  - Wrapper with CFG Schedule reads prompts better and has more prompted look compared to native
  - *From: Drommer-Kille*

- **VACE requires perfect masks without blur**
  - VACE doesn't work with blurry masks, masks need to be perfect with no blur
  - *From: SonidosEnArmonía*

- **Mix color by mask technique for VACE inpainting**
  - When doing inpainting with VACE, feed the original video with white on the mask area besides providing the mask itself, using mix color by mask node to do this automatically
  - *From: SonidosEnArmonía*

- **VAE cache memory leak in InfiniteTalk**
  - VAE cache doesn't get cleared between windows in InfiniteTalk loop, causing 2-3GB more VRAM usage from 2nd window onwards
  - *From: Kijai*

- **Lightning 1.1 High LoRA with WAN 2.2 Low gives better results**
  - Using the wrong Lightning LoRA (1.1 High with 2.2 Low) in upscaling workflow gave better results - less saturated, more detailed
  - *From: InsalaIlive*

- **CFG scheduling enables motion blur in WAN**
  - Using CFG scheduling got WAN to finally do motion-blur, at least sort of
  - *From: Drommer-Kille*

- **High noise WAN 2.2 model with CFG gives more motion**
  - With the high noise 2.2 model, using CFG gives you more motion and more prompt adherence, not quality
  - *From: Kijai*

- **4 or 5 steps minimum required for high noise model**
  - Can't go below N number of steps on the high noise model - 4 or 5 steps is an epic fail, speedup LoRAs may not work properly with too few steps
  - *From: MysteryShack*

- **Context windows don't work with I2V**
  - Context windows only work with T2V, not I2V models
  - *From: Kijai*

- **Context windows work better with limited movement**
  - Works for content with pretty much no moving camera and repeating actions like dancing, as long as subject stays in frame
  - *From: Draken*

- **2.2 works better with existing quantizations than 2.1**
  - 2.2 even works with fp8_fast while 2.1 quality dies with it
  - *From: Kijai*

- **Block swapping is only faster if it prevents VRAM overflow**
  - Block swapping is way faster than memory fallback, but only provides speed benefit when it saves you from going above 95% VRAM usage
  - *From: Kijai*

- **New CFG handling method**
  - Changed how cfg input is handled - now extends list by last value or cuts it to match steps instead of setting steps to match cfg
  - *From: Kijai*

- **CFG scheduling hack for first step only**
  - Setting end percent to 0.01 applies CFG float to only the initial step - not actual math, just a hack to ensure CFG 2 lands only on first step
  - *From: DawnII*

- **Control latent strength 0 keeps generation static**
  - Setting control latent str to 0 keeps the whole generation static
  - *From: DawnII*

- **FantasyPortrait face detector improvement**
  - Updated to use previous working detection for missing faces instead of failing or getting out of sync, prevents audio desync with Infinite/MultiTalk
  - *From: Kijai*

- **VRAM optimization for Long I2V Multi/InfiniteTalk**
  - Optimizations reduce VRAM use by 2-3GB at default res by clearing VAE cache between windows
  - *From: Kijai*

- **Hidden helper node for mask operations**
  - Has helper node for VACE mask purposes, originally for Fun InP but works for other uses by inverting the mask
  - *From: Kijai*

- **Keyframe interpolation is basic VACE feature**
  - VACE always had interpolation capabilities, it's a basic feature that many people miss
  - *From: Kijai*

- **VACE requires accurate positioning of reference images to work properly**
  - Position matters in the reference image setup - had to overlay reference image in Krita over original at exact position to get proper character replacement
  - *From: mdkb*

- **White padding around VACE reference images affects output drastically**
  - Adding 50px white padding changed jacket color to bright blue, removing padding fixed the issue
  - *From: mdkb*

- **VACE reference images are cropped to same size as video**
  - If you have a tall reference image with your subject filling the image, it will be cropped to just the person's waist
  - *From: Ablejones*

- **Wan 2.2 Lightning LoRAs have bias towards bright lighting**
  - Lightning 2.2 lora absolutely loves bright lights and results in more well-lit videos
  - *From: Ablejones*

- **Model loading times are inconsistent in latest wrapper version**
  - Generation times fluctuate between 15-18 sec/it with latest version vs steady 14 sec/it with older version from August 19th
  - *From: patientx*

- **2.2 VAE is only for the 5B model, 14B still uses 2.1 VAE**
  - Users were confused about which VAE to use with different model variants
  - *From: DawnII*

- **VACE + standin works very well for a full one shot solution**
  - Combination provides effective single-step workflow
  - *From: ˗ˏˋ⚡ˎˊ-*

- **MAGREF doesn't degrade video quality over time but has lower image fidelity**
  - Appears blurry in comparison to other models but maintains consistency
  - *From: Kijai*

- **Wan 2.2 low noise model works great for T2I generation**
  - Unexpected application discovered for single image generation
  - *From: Gateway {Dreaming Computers}*

- **Kijai converted wav2vec2 model to safetensors format with fp16 version**
  - Single file loading like all models, fp16 version for slight RAM savings and faster loading
  - *From: Kijai*

- **N0NSens got 2.2 + InfiniteTalk + color match working well**
  - Uses simple color match node after generation, works better than VACE for color consistency
  - *From: N0NSens*

- **Canny control needs to be inverted for VACE workflows**
  - Use image invert node after canny for proper results
  - *From: mdkb*

- **JalenBrunson chains multiple VACE encoders with different controlnets**
  - 1 vace encoder with dwpose, 1 with depth, 1 with ref image, adjusting strength for best combination
  - *From: JalenBrunson*

- **Wan 2.2 S2V has pose control ability built-in**
  - The model includes pose control functionality similar to UniAnimate
  - *From: DawnII*

- **VRAM usage reduction with iGPU setup**
  - Switching monitor to motherboard iGPU saves 4% VRAM on 5090 (from 7% to 3% baseline usage)
  - *From: Drommer-Kille*

- **Wan 2.2 InfiniteTalk tends to move camera regardless of prompt**
  - No matter what's in prompt, it tends to move the camera, with no visible glitches using context_opt
  - *From: N0NSens*

- **WanFM doubles inference time with minimal quality improvement**
  - Results are almost same as just using 2.2 without it, while taking twice as long
  - *From: Kijai*

- **Wan S2V outputs are 16 fps**
  - The video is saved at 16 fps in their code, outputs are 16 fps
  - *From: ZeusZeus/Kijai*

- **Wan S2V uses interpolation from 50 fps input to 16 fps**
  - Input fps is hardcoded to 50, sample rate is 16, involves interpolation between these rates
  - *From: Kijai*

- **Wan S2V is heavier on VRAM than Wan 2.2 A14B but easier on RAM**
  - The new S2V model requires more VRAM than the 14B model but uses less RAM
  - *From: Kijai*

- **Wan S2V is actually 4 models combined**
  - Consists of base model + pose model + audio model + framepack
  - *From: Kijai*

- **Reference latent is used exactly like Phantom**
  - The ref latent implementation follows the same pattern as Phantom model
  - *From: Kijai*

- **CFG Schedule with normal steps and sampler works better than 3 samplers**
  - Changing Create CFG Schedule Float List to normal steps makes wonders, keeps prompt adherence and is faster than using 3 samplers
  - *From: Mu5hr00m_oO*

- **S2V requires specific resolution formula for successful generation**
  - Always ensure (width÷16) × (height÷16) × frames ÷ 30 is a whole number. Examples: 832x480 with 81 frames works, 320x320x121 doesn't, 480x480 with 121 frames works
  - *From: patientx*

- **S2V appears to respond to music rhythm**
  - Character's dance changes with the rhythm of the music when using audio input
  - *From: slmonker*

- **CFG Skimming is CFG interpolation**
  - CFG Skimming experiment allows 4 steps (2+2) Lightning generation with LoRA on HIGH & LOW
  - *From: DawnII*

- **WAN 2.2 defaults to 16 fps output**
  - The model generates at 16 fps by default, not 24 fps
  - *From: DawnII*

- **CFG 1 reduces motion and prompt adherence in WAN 2.2**
  - Setting CFG to 1 diminishes motion and prompt adherence, ideally need full CFG for high noise steps
  - *From: MysteryShack*

- **Context windows don't increase VRAM usage**
  - Generating 1000 frames uses same VRAM as 81 frames, same principle as framepack
  - *From: Kijai*

- **WAN S2V uses framepack architecture**
  - The S2V implementation is based on framepack technology
  - *From: Kijai*

- **Native ComfyUI implementation can do infinite length video**
  - Once properly implemented, the native version will support infinite length video generation
  - *From: comfy*

- **bf16 performs better than other precisions for Wan**
  - bf16 bit better as expected
  - *From: Kijai*

- **Original code drops initial frames**
  - even the original code drops some of the inital frames btw
  - *From: Kijai*

- **S2V works better with simpler prompts**
  - weirdly works better with less words in the prompt? huh just 'man talking' giving me better results than a detailed description
  - *From: pewpewpew*

- **Audio needs to be zeroed for uncond in CFG**
  - boosting lightx2v strength actually does improve it, and at least in the wrapper I had cfg implemented wrong, the audio needs to be zeroed for uncond
  - *From: Kijai*

- **Custom linear sigmas work better for Lightning LoRA**
  - for lightning lora and exactly 4 steps the key is to have 4 linear sigmas, normal schedulers tend to put the last sigma way too low. you would use custom sigmas with 1.0, 0.75, 0.5, 0.25 and shift 5
  - *From: Kijai*

- **Resolution affects LoRA strength requirements**
  - lower the res, less strong should the lightx2v be, and also shift should be lower. and at higher res it benefits a lot from stronger lightx2v or cfg
  - *From: Kijai*

- **CLIP vision can be used to split image attention**
  - It will split the image cross attention so that the start image affects first half of the video and end image the latter half....it's not super strong effect but somewhat useful if your start and end are very different images
  - *From: Kijai*

- **Merged vs unmerged LoRAs behave very differently in wrapper**
  - Unmerged LoRAs can completely break custom LoRAs that work fine in native, while merged LoRAs work similarly to native. Native always merges LoRAs, while GGUF is always unmerged
  - *From: mamad8, Kijai, Draken*

- **LightX 2.1 LoRAs work with Wan 2.2**
  - Users report LightX 2.1 LoRAs give good results with Wan 2.2, better than Lightning LoRAs
  - *From: Lodis*

- **S2V pose control just works without additional setup**
  - OpenPose control works with S2V model without needing complex configuration
  - *From: Kijai*

- **Scheduler state reset issue between generations**
  - Scheduler isn't properly reset between iterations, causing index out of bounds errors on second generation
  - *From: Mu5hr00m_oO*

- **Context window frame count must not exceed input frames**
  - Setting context window frame count higher than input frames causes errors
  - *From: T2 (RTX6000Pro)*

- **VACE doesn't support combined controls, Fun Control does**
  - VACE embeds can be chained but don't support combined controls, while Fun Control supports combined inputs
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Multiple VACE encoders reduce skeleton artifacts**
  - Using multiple VACE encoders instead of image blend of controlnets shows skeleton artifacts less frequently
  - *From: JalenBrunson*

- **Lora merge explanation solves quality issues**
  - Matching configurations between quantized and non-quantized versions, with proper lora merging giving perfect results on 6 steps using wrapper
  - *From: mamad8*

- **VACE inpainting adds extra frames at beginning instead of end**
  - When num_frames is larger than input control video, extra frames are added at beginning rather than end
  - *From: SonidosEnArmonía*

- **Zero frames for motioner fixes start issue**
  - Setting zero frames for the motioner gets rid of the start issue, though the code suggests it should set ref latent instead
  - *From: Kijai*

- **S2V model outputs 16 fps while MultiTalk outputs 25 fps**
  - S2V has stop motion/lagging issues compared to MultiTalk's smoother 25fps output
  - *From: Kijai*

- **Face points only pose control reduces teeth artifacts**
  - Using only facial pose points instead of full body pose reduces excessive teeth generation
  - *From: Kijai*

- **Pose condition layer shouldn't be in fp8**
  - Initial fp8 model had issues, pose cond layer needs to stay in higher precision while audio injection layers work fine in fp8
  - *From: Kijai*

- **First step only with 0.5 multiplied pose condition works better**
  - Using pose condition only on first step and multiplying by 0.5 reduces artifacts
  - *From: Kijai*

- **Sapiens pose detection works better than DWPose for VACE**
  - Sapiens with filtered side bones provides better pose control for VACE, avoiding headphone artifacts
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Context windows don't burn framepack implementation**
  - Framepack method doesn't have burning issues but lipsync quality is reduced due to overlap
  - *From: Kijai*

- **GGUF models offer better quality than fp8 quantization for Wan models**
  - GGUF provides superior visual quality compared to fp8 quantized models, making it worth supporting despite complexity
  - *From: Kijai*

- **S2V model can be used for infinite video generation without audio**
  - S2V model has reference motion capability and can extend videos indefinitely without requiring audio input
  - *From: comfy*

- **S2V model is hardcoded to 16fps output**
  - The S2V model does interpolation to maintain 16fps output regardless of input audio characteristics
  - *From: Kijai*

- **Speed LoRAs don't work well with S2V model for T2V**
  - LightX and Lightning LoRAs lead to very blurry results with S2V model, and regular LoRAs need strength 2.0+ to show proper changes
  - *From: flo1331*

- **wav2vec2 model outputs at 50fps but bucketing function expects 16fps**
  - The wav2vec2 model outputs what's considered 50fps with 30 being the norm, but this model trained with 16 so their bucketing function expects that. The 16 is determined in the bucket function
  - *From: Kijai*

- **S2V can interpret depth maps**
  - S2V appears to have the ability to interpret depth maps in addition to other inputs
  - *From: DawnII*

- **S2V model is closer to 2.1 than 2.2 high noise**
  - S2V is much closer to 2.1 than the high noise model is for sure, but also further than 2.2 low noise
  - *From: Kijai*

- **Infinite talk doesn't like complex prompts**
  - User realized infinite talk doesn't work well with overly complex prompts
  - *From: l҈u҈c҈i҈f҈e҈r҈*

- **uni3c extracts camera motion from reference videos**
  - uni3c can look at what's happening in iPhone videos and apply camera movements (snap zooms, pans, orbits) to generations
  - *From: T2 (RTX6000Pro)*

- **Image encode extreme slowdown problem was resolved**
  - User experienced extreme slowdown with image-to-video encode that got resolved after recent updates
  - *From: cocktailprawn1212*

- **Memory issues fixed with merged LoRAs**
  - Model loading bugs when using merged LoRAs were fixed, which would not leave memory for encode node to work properly
  - *From: Kijai*

- **MAGREF is a full Wan I2V model, not a clip vision model**
  - MAGREF is not a clip vision model but a complete Wan I2V model that can still use clip vision but it's not necessary
  - *From: Kijai*

- **VACE encode memory usage is optimized**
  - VACE encode peaked at 15GB VRAM for 85 frames at 1280x720 with 6 steps, taking 2:47 to complete
  - *From: Kijai*

- **Framepack quality degrades over time**
  - Framepack goes bad the longer it goes, need to use weak settings or find balance between motion and image quality
  - *From: Kijai*

- **Context windows vs Framepack tradeoff**
  - Context windows give better quality for long gens but lipsync isn't as good compared to Framepack
  - *From: Kijai*

- **Beta scheduler differences between ComfyUI and diffusers**
  - ComfyUI scheduler beta is completely different from diffusers beta - diffusers applies shift first then beta, while ComfyUI may do it the other way around
  - *From: Kijai*

- **CFG guidance works differently with empty negative prompts vs no conditioning**
  - CFG with empty negative prompt still runs unconditional passes and subtracts that result, it's not the same as subtracting zero
  - *From: Ablejones*

- **Context windows work better for Wan than other extension methods**
  - Zero degradation over time compared to other approaches, though increases inference time due to overlap areas
  - *From: Kijai*

- **VACE can be used for scene transitions by setting strength to 0.0**
  - Dropping VACE strength low enough can change scenes mid-clip while maintaining style/subject coherence
  - *From: Ablejones*

- **Alpha channel information is preserved in different ways**
  - VACE can animate subjects while keeping backgrounds even with transparent input because RGB data is preserved under alpha
  - *From: hicho*

- **Wrapper automatically burns alpha backgrounds with framepack**
  - When using rgba images, the wrapper with framepack burns the alpha into the background automatically
  - *From: Kijai*

- **S2V pose control is more absolute than FantasyPortrait**
  - S2V control works in pixel space absolutely, while FP does it relatively. S2V at full strength is strict but at lower strength and first step only it's less strict
  - *From: ˗ˏˋ⚡ˎˊ- and Kijai*

- **Multiple control methods can be combined**
  - Can use FantasyPortrait + S2V + InfiniteTalk + VACE all together
  - *From: Kijai*

- **Character LoRAs help with FantasyPortrait character changes**
  - Using character LoRAs helps prevent FP from changing the character too much at full strength
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Context windows work with prompt travel**
  - Prompt travel functionality works with context windows and infinite talk loop
  - *From: Kijai*

- **Padding embeddings with zero vectors works for torch compile**
  - Fixed torch compile issues by padding the embedding with zero vectors instead of tokenized string padding
  - *From: phazei*

- **Fun Control 5b can mimic Uni3c in 2.2**
  - Can mimic uni3c camera motion in 2.2 model using 5b fun control by providing video with camera motion without controlnet
  - *From: hicho*

- **InfiniteTalk can work with T2V for short generations**
  - For short gens it just works, for long gens maybe with context windows. Doesn't work with the long gen loop
  - *From: Kijai*

- **Regular Wan model can handle up to 109 frames**
  - Regular model do 81. sky do 121. Regular can do up to 109 and has no issues with 105 frames in terms of following prompt
  - *From: N0NSens*

- **InfiniteTalk setup for T2V requires specific configuration**
  - T2V only put infinitetalk on the high sample - user found this was what they were doing wrong
  - *From: NebSH*

- **Lightx2v LoRA works better with native S2V at specific settings**
  - Try with the Lightx2v I2V lora, run 8 steps, at CFG 2.5 or 3.0, strength 1.0 on the lora
  - *From: Ablejones*

- **Camera control can be done entirely through prompts without complex nodes**
  - User discovered they don't need crazy nodes for camera control, everything can be done in the prompt
  - *From: Akumetsu971*

- **Multiple characters can work with InfiniteTalk**
  - Found method to have multi-character conversations with infinite
  - *From: 𝕯𝖗. 𝕸𝖆𝖈𝖆𝖇𝖗𝖊 ☠*

- **Context window panda T2V can be converted to I2V**
  - Successfully converted by replacing empty embeds and T2V models with I2V models
  - *From: Dever*


## Troubleshooting & Solutions

- **Problem:** Thaakenos workflow error with custom nodes
  - **Solution:** Disable the VAE node that sends VAE everywhere
  - *From: GOD_IS_A_LIE*

- **Problem:** ComfyUI memory not releasing after model unload
  - **Solution:** Use --cache-none flag for everything out of memory, --disable-smart-memory for VRAM clearing
  - *From: mdkb*

- **Problem:** ComfyUI Manager not installing nodes properly
  - **Solution:** Manually git clone the missing node repositories into custom_nodes folder
  - *From: Simjedi*

- **Problem:** VAE getting stuck in crawl mode after several generations
  - **Solution:** Full PC restart required, WSL2 recommended for easier instance restart
  - *From: Ghost*

- **Problem:** Memory issues with WAN 2.2 after updates
  - **Solution:** Use --cache-none launch flag to prevent node caching and reduce RAM usage
  - *From: Kijai*

- **Problem:** VRAM fills up on second generation
  - **Solution:** Enable 'offload_device' setting on first sampler to free VRAM
  - *From: Kijai*

- **Problem:** RadialAttention resolution errors
  - **Solution:** Image size must be divisible by block size (128), use 1280x768 instead of 1280x704
  - *From: NebSH*

- **Problem:** Triton compilation errors with RadialAttention
  - **Solution:** Install Triton from woct0rdho/triton-windows repository rather than self-compiling
  - *From: Kijai*

- **Problem:** WanVideoTextEncodeSingle meta tensor error
  - **Solution:** Update to latest wrapper version - bug was fixed in single encode node
  - *From: Kijai*

- **Problem:** Preview not showing on sampler nodes
  - **Solution:** Update ComfyUI and wrapper - may be related to ComfyUI preview code changes
  - *From: au*

- **Problem:** WanVideoSampler error: invalid literal for int() with base 10
  - **Solution:** Change starting steps from 0,-1 to 1,10000. End step -1 is correct for latest version
  - *From: Jas*

- **Problem:** Frontend update broke wrapper with VHS nodes
  - **Solution:** Need latest VHS nodes to work, refresh frontend
  - *From: Kijai*

- **Problem:** Context options causing 'Dimension out of range' error
  - **Solution:** Update to latest version, Kijai fixed this issue recently
  - *From: Kijai*

- **Problem:** VRAM OOM on second sampler with context windows
  - **Solution:** Don't connect context options to second sampler, or use less overlap on low noise side
  - *From: Kijai*

- **Problem:** Wrapper sampler previews broken
  - **Solution:** Use latent2rgb instead of TAESD, though quality is worse
  - *From: lostintranslation*

- **Problem:** Black output when disabling lightx2v
  - **Solution:** Check if using correct models from Kijai repo instead of ComfyUI provided models
  - *From: crinklypaper*

- **Problem:** Loop detected error when using workflows from Discord
  - **Solution:** Copying the entire workflow and pasting it into a blank comfy session fixes it
  - *From: T2 (RTX6000Pro)*

- **Problem:** Resolution tensor issues with 2.2 VAE
  - **Solution:** Update ComfyUI - the error just means your comfyui is not updated
  - *From: Kijai*

- **Problem:** 5Bi2v workflow not working
  - **Solution:** If you disconnect samples from extra latents it works
  - *From: Dita*

- **Problem:** Silent OOM state after canceling jobs
  - **Solution:** Nothing except the top bar free and node cache actually clears VRAM properly
  - *From: StableVibrations*

- **Problem:** CG use everywhere custom node conflict
  - **Solution:** Install the nightly version of the cg use everywhere custom node
  - *From: xwsswww*

- **Problem:** NAG context error with split_cross_attn_ffn
  - **Solution:** This happens when you prompt with | - NAG not added there yet
  - *From: Kijai*

- **Problem:** IndexError with dimension out of range
  - **Solution:** Needs negative prompt when CFG is enabled - NAG prompt doesn't count
  - *From: Kijai*

- **Problem:** LoadLora with CLIP on Wan 2.2 tries to make loop in I2V generation
  - **Solution:** Issue reported but no solution provided
  - *From: 1022987353859575808*

- **Problem:** Error 'nag_context is not supported in split_cross_attn_ffn'
  - **Solution:** No solution provided
  - *From: Yae*

- **Problem:** Sageattention related errors in workflows
  - **Solution:** Turn off sageattention
  - *From: Kijai*

- **Problem:** Color shift in middle of video with sliding windows
  - **Solution:** Known issue with sliding window approach
  - *From: 1296968408147169280*

- **Problem:** RAM maxing out and system freezing
  - **Solution:** Use --disable-smart-memory and --cache-none flags when booting ComfyUI, create large swap files on NVME SSD
  - *From: mdkb*

- **Problem:** Latest ComfyUI core update breaking things
  - **Solution:** Issue identified as breaking hotreload hack
  - *From: Kijai*

- **Problem:** Wrapper restarting runs even with no changes
  - **Solution:** Update ComfyUI core to latest version along with wrapper
  - *From: Rau*

- **Problem:** Context options lack continuity, video replays after 81 frames
  - **Solution:** This is a known issue with I2V - context doesn't work well with I2V due to strong image conditioning
  - *From: Kijai*

- **Problem:** 5B model LoRAs don't work with 14B model due to size mismatch
  - **Solution:** Cannot merge different shaped weights - connect LoRAs to correct model size
  - *From: Kijai*

- **Problem:** CFG 3.5 requires negative prompt to work
  - **Solution:** Must add negative text encode node, not just NAG conditioning
  - *From: Kijai*

- **Problem:** Burnt frames when generating at 24fps
  - **Solution:** Generate at 16fps then interpolate to 24fps using RIFE, as 14B model not optimized for 24fps
  - *From: thaakeno*

- **Problem:** Washed out video output with wrapper
  - **Solution:** Use high noise without lightx2v LoRAs at CFG 3.5, then low noise with lightx2v at CFG 1
  - *From: BondoMan*

- **Problem:** TAESD previews not working after update
  - **Solution:** Need to enable specific settings in manager - taew2_1 should be in vae_approx
  - *From: DawnII*

- **Problem:** Mat1 and mat2 shapes cannot be multiplied error
  - **Solution:** Wrong text encoder being used for native ComfyUI clip loader
  - *From: Kijai*

- **Problem:** Model loader not working with default setting
  - **Solution:** Manually select fp8_e5m2 vs default in model loader
  - *From: topmass*

- **Problem:** Blurry outputs with working generation
  - **Solution:** Switch back to 2.1 VAE, increase steps from 10 to 25
  - *From: topmass*

- **Problem:** WanVideoVAE38 object has no attribute 'z_dim' error
  - **Solution:** Update the wrapper - this was fixed recently
  - *From: Kijai*

- **Problem:** VAE 2.2 only works with 5B model
  - **Solution:** Use VAE 2.1 for 14B model, VAE 2.2 only compatible with 5B
  - *From: Kijai*

- **Problem:** System crashing when second model loads
  - **Solution:** Set --cache-none in ComfyUI config if system RAM is filling up
  - *From: zelgo_*

- **Problem:** Input size error 'The size of tensor a (11400) must match the size of tensor b (11685)'
  - **Solution:** Input must be divisible by 32 - change from 960x656 to compatible resolution
  - *From: daking999*

- **Problem:** Character LoRAs from 2.1 not triggering in 2.2
  - **Solution:** No definitive solution provided, reported as ongoing issue
  - *From: screwfunk*

- **Problem:** TypeError: argument of type 'NoneType' is not iterable
  - **Solution:** Check for bypassed nodes before set node, ensure prompt nodes are properly connected
  - *From: Kijai*

- **Problem:** Middle frame conditioning not working properly
  - **Solution:** Dial up the lora strength on the high noise
  - *From: Faux*

- **Problem:** Issues with middle frame implementation
  - **Solution:** Mask values need to be correct - frames you keep = 1, not 0 as in some implementations
  - *From: Kijai*

- **Problem:** SageAttention CUDA compatibility issues with 12.9
  - **Solution:** Recompile Triton, use torch-2.9.0.dev20250802+cu129 with triton-3.4.0
  - *From: Kijai*

- **Problem:** Need to restart ComfyUI between runs
  - **Solution:** Use built-in clear VRAM buttons or add clear VRAM to VAE decode node
  - *From: Ryzen*

- **Problem:** H100 slower performance with sage attention
  - **Solution:** Use 'auto' mode on H100, not specific sage attention modes
  - *From: Kijai*

- **Problem:** Burned/overexposed renders in Wan 2.2
  - **Solution:** Add 'low quality' to negative prompts
  - *From: Ryzen*

- **Problem:** Character LoRAs from 2.1 not working in 2.2 I2V
  - **Solution:** No definitive solution found, still being investigated
  - *From: screwfunk*

- **Problem:** Lighting strobing with CFG 3.5 on high steps
  - **Solution:** Enable zero star and TCFG to eliminate strobing while maintaining quality
  - *From: phazei*

- **Problem:** System memory usage regression in wrapper
  - **Solution:** Identified commit 5406a72f62adf4a31a8a0a0e4923cc5288399652 as culprit via git bisect
  - *From: Doctor Shotgun*

- **Problem:** Camera motion keywords being ignored
  - **Solution:** Need more high steps to 'fit it in', try full workflow or improve prompts
  - *From: Rainsmellsnice*

- **Problem:** Training LoRA without affecting face/facial bleeding
  - **Solution:** Blur faces in training data and caption them as blurred to isolate from normal faces
  - *From: Fill*

- **Problem:** fp8 model causing upscaling issues with flashing/blipping textures
  - **Solution:** Model converts back to bf16 during process, block swap settings may need adjustment
  - *From: MiGrain*

- **Problem:** Fog/dust appearing in middle of FFLF transitions
  - **Solution:** Likely caused by using over 81 frames, reducing frame count improves quality
  - *From: Kijai*

- **Problem:** fp8 model hallucinating incorrect objects
  - **Solution:** fp8 can change subject matter (making divers into seaweed), use higher precision for accuracy
  - *From: hicho*

- **Problem:** Official Alibaba code extremely slow (25 min on B200)
  - **Solution:** Code quantizes from fp32 to bf16 every run, plus uses large model chunks causing slowdown
  - *From: aikitoria*

- **Problem:** Burnt/overexposed video output in WanWrapper
  - **Solution:** Refresh browser after updating to see new start/end step widgets, reconnect split step node
  - *From: nacho.money*

- **Problem:** Missing start and end step widgets in sampler nodes
  - **Solution:** Make sure to update properly, refresh browser, and reload workflow. Check for conflicting installations
  - *From: Kijai*

- **Problem:** ComfyUI Manager update issues
  - **Solution:** Delete from custom_nodes and use git pull instead of manager installation
  - *From: voxJT*

- **Problem:** Multistep samplers causing burning with model switching
  - **Solution:** Add single step of euler when switching to LN model to reset multistep sampling
  - *From: Ablejones*

- **Problem:** Multitalk won't sync with Wan 2.2
  - **Solution:** Currently doesn't work properly with 2.2, works better with 2.1
  - *From: Kijai*

- **Problem:** Character LoRA affecting face when training body
  - **Solution:** Crop body only and caption correctly that it's cropped showing specific parts
  - *From: mamad8*

- **Problem:** OOM at 3496 x 2096 resolution
  - **Solution:** Actually was OOM despite different error message - reduce resolution
  - *From: Juan Gea*

- **Problem:** Core dump with torchcompile on 5090
  - **Solution:** Issue with Triton or something similar, works on Linux with latest nightly and latest triton
  - *From: Kijai*

- **Problem:** Blurry outputs on larger than 512px with lightx2v
  - **Solution:** Use higher LoRA strength (3.0+) and proper scheduler/sampler combinations
  - *From: Kijai*

- **Problem:** Snow effect when using lightx2v
  - **Solution:** Fix by using it at higher strength
  - *From: Kijai*

- **Problem:** GGUF compatibility issues
  - **Solution:** Fixed with latest update, should work with GGUF now
  - *From: Kijai*

- **Problem:** Torch compile errors with native
  - **Solution:** Try compiling only transformer blocks instead of full model
  - *From: Kijai*

- **Problem:** WanVideoSampler cannot import 'Wan22' error
  - **Solution:** Need to use Wan 2.2 model or rollback wrapper version when trying to use updated wrapper with Wan 2.1
  - *From: ChristianAr(3090)*

- **Problem:** T2I attempts producing poor quality
  - **Solution:** Use shift 1 instead of higher shift values for single frame generation
  - *From: aikitoria*

- **Problem:** MMaudio producing weird output for laughter
  - **Solution:** Use dead simple prompts like 'woman laugh' or 'the woman is laughing' instead of complex descriptions
  - *From: TK_999*

- **Problem:** Static video glitch output in first sampler
  - **Solution:** Check if input image is connected properly to VAE encoder and ensure VAE is connected to multiple nodes as needed
  - *From: TK_999*

- **Problem:** Mat1 and mat2 error when using non-fp8 CLIP
  - **Solution:** Use e5 fp8 weights for Ampere cards (3090s) as they have known compatibility issues
  - *From: samhodge*

- **Problem:** JSON prompts causing weird errors in Wan 2.2
  - **Solution:** Normal prompts work fine, issue may be JSON formatting or prompt length specific to model
  - *From: thaakeno*

- **Problem:** LoRA scheduling doesn't work with merge_loras ON
  - **Solution:** Use separate high and low LoRAs - high without merge, low with merge, or add 3rd sampler
  - *From: Kijai*

- **Problem:** CFG list sampling crashes at 50% with list index out of range error
  - **Solution:** Issue occurs when using CFG list of values, crashes around 6th step of 12 steps
  - *From: gokuvonlange*

- **Problem:** Cannot import 'Wan22' from comfy.latent_formats error
  - **Solution:** Need to update ComfyUI itself, not just the wrapper
  - *From: Kijai*

- **Problem:** Multitalk generating noise instead of proper output
  - **Solution:** Disable merge lora option - the lightx merge lora causes the issue
  - *From: Kijai*

- **Problem:** Wan 2.2 Lightning LoRAs only producing noise
  - **Solution:** Use strength 0.125 for both high and low noise LoRAs instead of default strength
  - *From: Kijai*

- **Problem:** Character consistency issues with VACE without LoRA
  - **Solution:** Nearly impossible to get consistency without a character LoRA at this point
  - *From: Nekodificador*

- **Problem:** Original repo LoRAs don't work in native ComfyUI
  - **Solution:** Use Kijai's fixed versions - original ones don't use ComfyUI standard key naming and are fp32 format issues
  - *From: zelgo_/Kijai*

- **Problem:** Black screen in T2I workflow with lightning LoRA
  - **Solution:** Check model compatibility and LoRA strength settings
  - *From: N0NSens*

- **Problem:** New lightning LoRAs produce overly bright/overexposed results
  - **Solution:** 
  - *From: gokuvonlange/IceAero*

- **Problem:** Static/slow motion videos with new Lightning LoRAs
  - **Solution:** Use old LightX2V 2.1 LoRA on high noise pass, new Lightning on low noise pass
  - *From: Doctor Shotgun*

- **Problem:** New 2.2 Lightning high noise LoRA produces weird camera fade out effects
  - **Solution:** Switch to old LightX2V 2.1 LoRA for high noise pass
  - *From: Doctor Shotgun*

- **Problem:** Overburned/oversaturated results with new Lightning LoRAs
  - **Solution:** Use CFG scheduling or lower LoRA strengths
  - *From: N0NSens*

- **Problem:** First/Last frame encoding error with 5B model
  - **Solution:** Update WanVideoWrapper node to latest version for 5B first/last frame support
  - *From: Kijai*

- **Problem:** WanVideo Empty Embeds error without image connection
  - **Solution:** Connect an image to extra_latents in WanVideo Empty Embeds node, otherwise it refuses to work
  - *From: Juan Gea*

- **Problem:** LoRA merging error with scaled models
  - **Solution:** Disable merge LoRAs toggle on LoRA loader or use non-scaled model. If memory issues occur, update Kijai nodes
  - *From: Ashtar*

- **Problem:** FLF workflow error
  - **Solution:** Update ComfyUI - the error was fixed yesterday or day before
  - *From: Kijai*

- **Problem:** LoRA strength list bug
  - **Solution:** Fixed bug where if first weight was 0, it would skip all LoRAs on that step
  - *From: Kijai*

- **Problem:** Split view generation with camera movement prompts
  - **Solution:** The word 'cut' in prompts causes split screen effect
  - *From: IceAero*

- **Problem:** OOM error on native while wrapper runs fine
  - **Solution:** Run comfy with --reserve-vram 2 or higher value. Native is more efficient offloading but automated estimation fails when GPU used for other tasks
  - *From: Kijai*

- **Problem:** Sigmas Split Value and HN init steps nodes causing errors
  - **Solution:** Update RES4LYF by navigating to directory and typing 'git pull' since it's not registered in manager
  - *From: Ablejones*

- **Problem:** Overburned trash results with 5B model
  - **Solution:** Try 4 steps euler and higher shift
  - *From: Kijai*

- **Problem:** ComfyUI making machines crash with Wan 2.2
  - **Solution:** Use --disable-smart-memory argument and set up static swap file on SSD drive
  - *From: mdkb*

- **Problem:** torch._inductor.exc.InductorError: PY_SSIZE_T_CLEAN macro must be defined
  - **Solution:** No solution provided
  - *From: IceAero*

- **Problem:** RuntimeError: mat1 and mat2 shapes cannot be multiplied (77x768 and 4096x5120)
  - **Solution:** Use umt5xxl from comfy link or fp8 scaled version for native
  - *From: hablaba*

- **Problem:** Videos from high and low sampler not matching up
  - **Solution:** No solution provided
  - *From: The Dude*

- **Problem:** White noise output with sliding context
  - **Solution:** Issue occurs with I2V model, context windows work poorly with I2V anyway
  - *From: Kijai*

- **Problem:** New Lightning loras producing noise in wrapper
  - **Solution:** Use strength 0.125 for original version or 1.0 for Kijai's converted version
  - *From: Kijai*

- **Problem:** Width/height must be divisible by 32 error
  - **Solution:** Change resolution from 480x832 to 704x1280 or other values divisible by 32
  - *From: Dita*

- **Problem:** NameError: name 'Wan22' is not defined
  - **Solution:** Update ComfyUI - Wan22 was added when Wan 2.2 was released
  - *From: Kijai*

- **Problem:** index 0 is out of bounds for dimension 0 with size 0
  - **Solution:** Set start step to 0 instead of having same start and end step values
  - *From: Kijai*

- **Problem:** type NoneType doesn't define __round__ method in LoRA loader
  - **Solution:** The strength parameter is being passed as None - ensure all LoRA strengths are set to numeric values
  - *From: screwfunk*

- **Problem:** bong_tangent scheduler not working well with low steps
  - **Solution:** bong_tangent needs at least 20 steps, use beta or beta57 schedulers for higher step counts with video models instead
  - *From: Ablejones*

- **Problem:** Lightning LoRAs burning colors and not converging
  - **Solution:** Try strength 0.2-0.35 and higher start steps. FastWan LoRA doesn't work well with I2V
  - *From: 3DBicio*

- **Problem:** torchcompile fp8_e4m3fn hanging on 3090s
  - **Solution:** It hangs due to one line in inductor, use e5 instead (though technically worse for Wan) or scaled e5 version
  - *From: Kijai*

- **Problem:** Wan 2.2 templates not showing in ComfyUI
  - **Solution:** Manager update may show as updated but not actually update to latest version, try installing fresh ComfyUI
  - *From: Blink*

- **Problem:** SystemError: PY_SSIZE_T_CLEAN macro must be defined for '#' formats
  - **Solution:** Restart ComfyUI to clear torch compile cache - caused by Anything Everywhere nodes auto-connecting compile args
  - *From: IceAero*

- **Problem:** Denoise below 0.5 causes 'index 0 is out of bounds' error on 14B model
  - **Solution:** Use denoise values 0.5 and above, update ComfyUI and refresh browser
  - *From: Juan Gea*

- **Problem:** External masks from Photoshop/Krita/Blender don't work in ComfyUI
  - **Solution:** Use 'Image to Mask' node to convert external masks, ensure mask is resized to same size as input manually
  - *From: Kijai*

- **Problem:** Qwen Image VAE causes burnout errors
  - **Solution:** Set Qwen Image model to fp8_e5m2 precision instead of fp8_e4m3fn
  - *From: fredbliss*

- **Problem:** Hard drive full affecting swap and maxing out RAM
  - **Solution:** Use 'Release node cache' button in ComfyUI Manager to free up space
  - *From: Rainsmellsnice*

- **Problem:** ComfyUI reloading models on each generation
  - **Solution:** Models don't all fit in VRAM at once, causing reload. Use lower precision (VAE fp16, UMT5 on CPU) to save VRAM
  - *From: aikitoria*

- **Problem:** SageAttention patching message on every generation
  - **Solution:** This is normal and doesn't take long - it just swaps which code is executed during steps
  - *From: aikitoria*

- **Problem:** LatentCompositeMasked error with video
  - **Solution:** This node doesn't handle video latents - it's meant for images only
  - *From: Kijai*

- **Problem:** Flash_attn_2_cuda errors with torch 2.8
  - **Solution:** Just uninstall flash attention - it's not actually used if not explicitly selected and SageAttention works fine
  - *From: Kijai*

- **Problem:** Slow motion videos from Wan 2.2
  - **Solution:** Use CFG > 1 to fix slow motion issues
  - *From: Kijai*

- **Problem:** Blurry/foggy results with low contrast
  - **Solution:** Increase CFG from 1.0 to 2.0, increase shift from 1.0 to 5.0, reduce LoRA strength to 0.7, stick with 81 frames
  - *From: Kijai*

- **Problem:** Context window crashes ComfyUI with SageAttention
  - **Solution:** SageAttention uses Triton which does some compiling in scenarios, disable compile to get proper error messages
  - *From: Kijai*

- **Problem:** KSamplerAdvanced error with channel mismatch
  - **Solution:** Reinstall ComfyUI - issue with weight size expecting 36 channels but getting 32
  - *From: SonidosEnArmonía*

- **Problem:** WAN 2.2 5B OOM on Mac M4 with 128GB RAM
  - **Solution:** OOM occurs on VAE which is super heavy on fp32, 5B VAE is 4x heavier than 2.1
  - *From: Kijai*

- **Problem:** Depth + pose combined control issues
  - **Solution:** Don't combine depth and pose for VACE, use separate VACE nodes for each control type
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Problem:** RuntimeError: required rank 4 tensor to use channels_last format with ComfyUI native Wan
  - **Solution:** No solution provided in discussion
  - *From: fredbliss*

- **Problem:** Burned/overexposed results when using LightX2V LoRA with wrapper
  - **Solution:** Try lowering LoRA strength or adjusting CFG settings. For I2V, shift=1 breaks everything, use shift=8
  - *From: Juan Gea*

- **Problem:** EchoShot implementation not triggering properly
  - **Solution:** Use Kijai's | character prompt splitting method instead
  - *From: Kijai*

- **Problem:** Gorilla getting unwanted clothing/accessories in martial arts scenes
  - **Solution:** Try specific outfit prompts or detailed anatomy descriptions like 'highly realistic silverback gorilla, natural anatomy, visible powerful muscles under thick fur'
  - *From: Mancho*

- **Problem:** Noisy output when using save/load latent workflow
  - **Solution:** Use DisableNoise node instead of RandomNoise when continuing generation from saved latent
  - *From: Ablejones*

- **Problem:** RAM issues with save/load latent workflows
  - **Solution:** Use --cache-none flag to automatically clear memory after each node
  - *From: Kijai*

- **Problem:** Poor results at higher resolutions like 1280x720
  - **Solution:** Try higher CFG (5+) and more steps (20+) when not using Lightning LoRAs
  - *From: N0NSens*

- **Problem:** Model compilation fails after merging
  - **Solution:** Save the merged model and reload it before compiling - don't compile directly after merging
  - *From: Ablejones*

- **Problem:** Reference image not working with HN model
  - **Solution:** VACE blocks don't work on HN model without merging 2.1 patch embedding and block 0
  - *From: Kijai*

- **Problem:** Motion loops back or undoes in longer generations
  - **Solution:** Stick to 81 frames or less for consistent motion, longer sequences may repeat/undo actions
  - *From: Hoernchen*

- **Problem:** Snow particles showing up in Wan 2.1 and 2.2 output videos
  - **Solution:** Occurs when prompt is too short or shift too high, but no definitive solution found yet
  - *From: JohnDopamine*

- **Problem:** First preview step looks good but next step ruins details
  - **Solution:** Try higher shift value if first step of high noise has discernable preview - indicates too big first step
  - *From: Ablejones*

- **Problem:** No preview being generated regardless of sampler
  - **Solution:** Reboot ComfyUI, happens sometimes when swapping between workflows
  - *From: DawnII*

- **Problem:** FP8 version not running on A5000 card
  - **Solution:** A5000 is compute 8.6, needs 8.9. 3000 series lacks native fp8 support, need at least 4000 series
  - *From: Lodis*

- **Problem:** Memory issues with 64GB RAM
  - **Solution:** Use --disable-smart-memory in bat file and create large static swap file on SSD
  - *From: mdkb*

- **Problem:** ComfyUI previews not working after nightly update
  - **Solution:** Update VHS (Video Helper Suite) nodes to latest version or rollback frontend to previous version
  - *From: Kijai*

- **Problem:** Out of memory with VAE decode even with tiling enabled
  - **Solution:** Use fp16 or bf16 VAE instead of fp32 - fp32 provides minimal visual improvement but uses much more VRAM
  - *From: Kijai*

- **Problem:** Color drift in first/last frame generation
  - **Solution:** Can be fixed with contrast/saturation/tint keyframes in DaVinci Resolve
  - *From: CaptHook*

- **Problem:** LoRA corruption error with Wan 2.2 Lightning
  - **Solution:** Use fp8e5 checkpoint if compiling, or bypass sigma values list - error may indicate borderline OOM conditions
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Problem:** White noise results without LoRA
  - **Solution:** Normal euler ends up with too low sigma on last step at 4 steps, won't remove all noise properly
  - *From: Kijai*

- **Problem:** New LoRAs don't play well with GGUF quants
  - **Solution:** Use 6 steps instead of 4 for better results with GGUF
  - *From: Josiah*

- **Problem:** LoRA not reloading in workflow
  - **Solution:** Replacing file directly caused workflow to not reload new LoRA, previously loaded LoRA was in memory
  - *From: piscesbody*

- **Problem:** Node taking super long to load
  - **Solution:** Put the device to default solved the loading issue
  - *From: AffenBrot*

- **Problem:** Camera gets jerky with low steps using CFG
  - **Solution:** Issue absent with cfg=1, or use more steps at higher sigmas to smooth out
  - *From: IceAero*

- **Problem:** Lightning LoRAs cause overbrightness and destroy contrast
  - **Solution:** Add a ksampler for first step cfg 3.5 without any lora to render brightness like vanilla wan2.2
  - *From: pagan*

- **Problem:** Small window size in MultiTalk not working properly
  - **Solution:** Don't reduce window size, there's overlap and small windows can't create many new frames per iteration
  - *From: Kijai*

- **Problem:** Image quality degradation in MultiTalk
  - **Solution:** Problem is about amount of windows, not video length - too many windows result in poor quality
  - *From: Kijai*

- **Problem:** First frame flash when going over 81 frames
  - **Solution:** Lowering to 85 frames removes first frame flash
  - *From: MysteryShack*

- **Problem:** NAG with WanVideo TextEncode Cached causing black output
  - **Solution:** Error occurs specifically when using cached node with apply NAG
  - *From: patientx*

- **Problem:** Cached embeds causing issues
  - **Solution:** Flush cache and use two separate text encode nodes (one for positive, one for negative) with NAG enabled
  - *From: patientx*

- **Problem:** Latent composite masked node doesn't work for videos
  - **Solution:** Node only works for images, not video latents - confirmed by Kijai
  - *From: xwsswww*

- **Problem:** Tensor mismatch errors
  - **Solution:** Usually happens when resolution isn't divisible by 16
  - *From: WorldX*

- **Problem:** New I2V LoRA producing all slow motion results
  - **Solution:** Adjust LoRA strength ratios - higher values for faster motion, lower for slower
  - *From: WorldX*

- **Problem:** Fun Control model not loading due to unsupported 52 channels
  - **Solution:** Update WanVideo wrapper to latest version to support the new channel count
  - *From: Kijai*

- **Problem:** fun_ref_image not working in Fun Control
  - **Solution:** Feature appears to have some effect but doesn't work properly - first frame works as alternative
  - *From: Kijai*

- **Problem:** Native ComfyUI throwing CPU/GPU tensor errors with low VRAM
  - **Solution:** Launch ComfyUI with --reserve-vram 2 command line argument to reserve extra VRAM for proper offloading
  - *From: Kijai*

- **Problem:** System RAM OOM with long video generations
  - **Solution:** Use save latent node to save to disk before decode, then load and decode in separate session, or use --cache-none flag
  - *From: Kijai*

- **Problem:** MultiTalk lip sync degrading after 7-8 seconds
  - **Solution:** Try raising audio scale parameter and use better vocal separation tools like Spleeter
  - *From: Kijai*

- **Problem:** WAN 2.2 Fun crashing with OOM before second ksampler
  - **Solution:** Use T5 node that fully removes from RAM, try --cache-none, keep block swap counts consistent (use 30 instead of mixing 20/30)
  - *From: Kijai*

- **Problem:** MultiTalk lip sync going off at 9 seconds
  - **Solution:** Use vocal only track, increase audio_scale and audio_cfg_scale, check chunk_overlap settings in AudioSeparation node
  - *From: hiroP*

- **Problem:** MultiTalk not working in video-to-video
  - **Solution:** Use fusionx model instead of base WAN 2.1, set audio_scale to 3, ensure audio is loud and clear
  - *From: SonidosEnArmonía*

- **Problem:** T5 error in wrapper but not native
  - **Solution:** Update to minimum required versions
  - *From: Kijai*

- **Problem:** Fun Control tensor size error (56 instead of 52)
  - **Solution:** Fixed by removing unused clip vision connection and correcting channel concatenation
  - *From: Kijai*

- **Problem:** Sapiens pose video not working
  - **Solution:** Remove the input video from the workflow
  - *From: fredbliss*

- **Problem:** Tensor mismatch error with Fun workflow
  - **Solution:** Image size must be divisible by 16, resize accordingly (e.g., 1280x542 to 1280x528)
  - *From: HeadOfOliver*

- **Problem:** WanVideoModelLoader error 'cannot access local variable model_type'
  - **Solution:** Delete and reinstall custom node, make sure using nightly version not latest
  - *From: Rainsmellsnice*

- **Problem:** Camera and cameraman appearing in reflective objects
  - **Solution:** Remove 'camera' from prompt, use negatives, refer to official Wan prompt guide for camera movement descriptions
  - *From: Dan*

- **Problem:** Fun Control reference input not working
  - **Solution:** Model needs matching start image to control first frame, reference image input may be defunct
  - *From: Kijai*

- **Problem:** GGUF model tensor error when encoding without control input
  - **Solution:** Control embed channel is expected - ensure proper control input connection
  - *From: Cubey/DawnII*

- **Problem:** FP8 scaled with torch compile VRAM leak
  - **Solution:** Kijai working on memory fixes but recommends not updating if current setup works
  - *From: Kijai*

- **Problem:** GGUF loading OOM at 60GB during WanVideo VACE Encode
  - **Solution:** Check node connections, particularly DWPose connections
  - *From: AmirKerr*

- **Problem:** VideoX fun and easyAnimate node packs conflict
  - **Solution:** Kijai clarified his workflows don't use those deprecated node packs
  - *From: AR/Kijai*

- **Problem:** RuntimeError: Sizes of tensors must match except in dimension 0
  - **Solution:** Input dimension mismatch - make sure inputs are same and divisible by 16
  - *From: Kijai*

- **Problem:** UniAnimate doesn't work with GGUF unmerged
  - **Solution:** Needs merging - easiest to make a merge
  - *From: Kijai*

- **Problem:** Color issues at end of generation with WanVideo Sampler
  - **Solution:** Need to add noise to samples on first sampler and connect split steps
  - *From: ingi // SYSTMS*

- **Problem:** Validation error with fp8_e4m3fn_scaled quantization
  - **Solution:** Update WanVideoWrapper nodes and refresh browser, or check for multiple fork installations
  - *From: Kijai*

- **Problem:** Mysterious camera shake with 2.2 I2V lightning LoRAs
  - **Solution:** Lower the strength to 1 or less, using 3x3 steps
  - *From: XWAVE*

- **Problem:** Grainy output in WanVideoWrapper
  - **Solution:** Use WanVideo Decode node instead of VAE Decode node when using the wrapper
  - *From: Hashu*

- **Problem:** Multitalk workflow error with two samplers
  - **Solution:** Can't use multitalk image embed node with two samplers because it's a loop from last frame. Use context window approach for long multitalk instead
  - *From: Kijai*

- **Problem:** VRAM leakage causing slowdowns after few generations
  - **Solution:** Using WSL2 with wsl --shutdown to restart WSL instead of full PC reboot helps with memory management
  - *From: pagan*

- **Problem:** Color/lighting changes in frame2frame i2v segments
  - **Solution:** Issue occurs when using same image for end frame and first frame of next segment - lighting changes from start to end of each segment
  - *From: PTMarks*

- **Problem:** Context windows error in MultiTalk
  - **Solution:** torch._dynamo.exc.TorchRuntimeError with shape mismatch in encoder_kv.view
  - *From: NebSH*

- **Problem:** Wan wrapper v1.2.7 device error
  - **Solution:** Downgrade to v1.2.6 - v1.2.7 has 'Expected all tensors to be on the same device, but found at least two devices, cuda:0 and cpu!' error
  - *From: army*

- **Problem:** Preview sampler node running at 4fps with overlapped frames
  - **Solution:** Use tiny VAE model (taew2_1.safetensors) in models/vae_approx folder, update video helper suite
  - *From: Kijai*

- **Problem:** Xformers compatibility issue on 5090
  - **Solution:** Uninstall xformers - it's not needed for anything and causes tensor device errors
  - *From: Kijai*

- **Problem:** Intermittent OOM issues when cancelling Wan 2.2 gen
  - **Solution:** Connect the model to offload node, requires full ComfyUI restart to recover
  - *From: Hoernchen*

- **Problem:** VACE workflow producing mangled output after ComfyUI update
  - **Solution:** Update Kijai's nodes and ComfyUI, disconnect unused Samples input from WanVideo sampler, enable add_noise if using samples input with denoise 1.0
  - *From: Kijai*

- **Problem:** Florence2Run error 'Cache only has 0 layers'
  - **Solution:** Update nodes manually by deleting folder and reinstalling, ComfyUI manager has issues with updates
  - *From: Kijai*

- **Problem:** SageAttention installation issues
  - **Solution:** Install Triton from https://github.com/woct0rdho/triton-windows and SageAttention wheel from releases, use pip install with python.exe in portable's python_embeded folder
  - *From: Kijai*

- **Problem:** Quick flash effect at beginning of T2V generations
  - **Solution:** Issue mentioned but solution not provided in this chunk
  - *From: DaxRedding*

- **Problem:** Fun workflow reference image only flashing for 1 frame
  - **Solution:** Issue mentioned but solution not provided in this chunk
  - *From: D'Squarius Green, Jr.*

- **Problem:** Inpainting only works with WanVideo Vace encode node
  - **Solution:** Use Vace encode node instead of latent mask or WanVideo Encode node
  - *From: xwsswww*

- **Problem:** VHS custom node causing issues
  - **Solution:** Update VHS custom node to fix problems
  - *From: Lodis*

- **Problem:** VHS node update caused lower quality preview
  - **Solution:** Check preview quality settings after update
  - *From: crinklypaper*

- **Problem:** torch._inductor.exc.InductorError with CompiledKernel
  - **Solution:** Check if torch compile/triton is installed properly or disconnect torch compile args
  - *From: kendrick*

- **Problem:** Training character LoRA on images causes slow motion output
  - **Solution:** Try 77 frames or add videos to training dataset, lower LoRA strength, or mix images with videos
  - *From: Juampab12*

- **Problem:** Video2Video output too close to original
  - **Solution:** Adjust denoise strength, but lower denoise may reduce motion
  - *From: DaxRedding*

- **Problem:** Lightning LoRA for 2.2 has style bias issues
  - **Solution:** Avoid for dark scenes, causes oversaturation and brightness bias
  - *From: Kijai*

- **Problem:** MultiTalk can't use 1280x720, only works at lower res like 832x480
  - **Solution:** Use lower resolution for MultiTalk generation
  - *From: NebSH*

- **Problem:** Block swap causing significant slowdown
  - **Solution:** Use prefetch option to improve transfer speeds
  - *From: Kijai*

- **Problem:** Text encoder incompatibility error
  - **Solution:** Use original T5 model, not scaled version, or use Cached Text Encoder node or Text Embed Bridge node
  - *From: Kijai*

- **Problem:** FP8e4nv not supported error on 3090
  - **Solution:** Use fp8e5m2 models for torch compile on 3090, not fp8e4
  - *From: Josiah*

- **Problem:** Out of memory with prefetch
  - **Solution:** Prefetch uses more VRAM (about single block amount), disable if causing OOM
  - *From: Kijai*

- **Problem:** WanTimeTextImageEmbedding.forward() got an unexpected keyword argument 'timestep_seq_len'
  - **Solution:** Update diffusers with pip install -U git+https://github.com/huggingface/diffusers.git
  - *From: Kijai*

- **Problem:** LoRAs not loading with mismatched models
  - **Solution:** ComfyUI silently ignores incompatible LoRAs - check console for warnings
  - *From: Kijai*

- **Problem:** Image resolution mismatch in I2V
  - **Solution:** Use KJ Resize v2 node after input image to match generation size, and use correct Wan 2.1 VAE
  - *From: The Shadow (NYC)*

- **Problem:** Radial attention block size error
  - **Solution:** Image size must be divisible by block size (128), use closest valid sizes like 640x896
  - *From: el marzocco*

- **Problem:** VACE Encode incorrectly connected to Control Embeds
  - **Solution:** VACE is T2V so shouldn't use image encode at all, VACE embeds connects directly to image_embeds on sampler
  - *From: DawnII*

- **Problem:** Only getting 1 step when setting 2 steps with 0.3 denoise in wrapper
  - **Solution:** Increase to 4 steps to get 2 actual steps - wrapper calculates denoise based on steps differently
  - *From: DawnII*

- **Problem:** Background people faces constantly mutating even with high steps
  - **Solution:** Problem is insufficient pixel resolution, not background position. Need 1152p or higher, or crop/upscale faces to 1024x1024 then stitch back
  - *From: Juan Gea*

- **Problem:** MultiTalk denoises everything at 0.7, lower values don't move lips
  - **Solution:** Try differential diffusion with mask for inpainting, give more strength to audio for expressiveness
  - *From: Juan Gea*

- **Problem:** SeedVR2 OOM error with 32GB VRAM
  - **Solution:** Use GGUF models with offloading, try Q6 or Q8 with 32GB
  - *From: AmirKerr*

- **Problem:** Incomplete MultiTalk node update
  - **Solution:** Update nodes again, push was incomplete by accident
  - *From: Kijai*

- **Problem:** AssertionError: All tensors must have the same dtype when using Stand-in LoRA
  - **Solution:** Remove other LoRAs like MovieGenn or MPS, or disable SageAttention
  - *From: Hashu*

- **Problem:** Stand-in LoRA causing cryptic SageAttention errors
  - **Solution:** Disable SageAttention to resolve the issue
  - *From: pagan*

- **Problem:** Stand-in workflow outputting full white
  - **Solution:** Need to apply a mask in the image using the built-in editor or use rembg node for cropping
  - *From: pagan*

- **Problem:** Wrong VAE error with Wan 2.2 5B
  - **Solution:** 5B model requires the 2.2 VAE, not the standard one used for 14B
  - *From: Kijai*

- **Problem:** Memory issues when queueing multiple generations
  - **Solution:** Use cached text encode node instead of memory cleaner nodes
  - *From: .: Not Really Human :.*

- **Problem:** Stand-in LoRA not working with GGUF models
  - **Solution:** Latest update fixed GGUF compatibility with Stand-in, allows using SageAttention without errors
  - *From: garbus*

- **Problem:** torch._inductor.exc.InductorError with fp8e4nv not supported
  - **Solution:** Either bypass torch compile node or download e5m2 model instead of e4m3fn
  - *From: Hevi*

- **Problem:** OOM on 720p 121 I2V with wrapper vs native using same VRAM
  - **Solution:** Native does automatic block swapping, wrapper needs manual block swap setting
  - *From: Kijai*

- **Problem:** AssertionError: All tensors must have the same dtype with sage attention
  - **Solution:** Change sageatt to sdpa or apply patch
  - *From: shockgun*

- **Problem:** WanVideoSampler tensor size mismatch error
  - **Solution:** Sounds like input size mismatch, check resolution compatibility
  - *From: Kijai*

- **Problem:** Context windows causing ghosting and unstable generations
  - **Solution:** Use uni3c to lock camera, works especially well with multitalk embeds
  - *From: Kijai*

- **Problem:** Can't import SageAttention error
  - **Solution:** Disable sage_attention in the Diffusion Model Loader KJ if you don't have sageattention installed
  - *From: Ablejones*

- **Problem:** fp8_e4m3fn doesn't work with torch compile on GPUs prior to 4000 series
  - **Solution:** Use fp8_e5m2 instead for older GPUs
  - *From: Kijai*

- **Problem:** RAM not clearing after execution in ComfyUI
  - **Solution:** Only restarting ComfyUI helps, clearing node cache doesn't fully clear RAM
  - *From: iShootGood*

- **Problem:** Set latent mask causes red tinting in unmasked areas
  - **Solution:** This is a known issue with diff diff and model split in the wrapper
  - *From: Kijai*

- **Problem:** Temporary VRAM usage peak after updating
  - **Solution:** After updating, first run may need to recompile causing temporary VRAM spike, should only affect first run with sage
  - *From: Kijai*

- **Problem:** Runtime error with shape mismatch when using last frame instead of first frame
  - **Solution:** Enable a specific option in the workflow settings
  - *From: Kijai*

- **Problem:** Control_start_percent error on nightly WanVideoWrapper
  - **Solution:** Downgrade from nightly to latest version or wait for fix
  - *From: ronnykhalil*

- **Problem:** Indentation error causing control_start_percent issue
  - **Solution:** Fixed with code update
  - *From: Kijai*

- **Problem:** Width 840 not supported causing broadcast dimension error
  - **Solution:** Use 832 instead, follow divisible by 16 rule
  - *From: Kijai*

- **Problem:** AssertionError about tensor dtype mismatch with sage attention
  - **Solution:** Switch to SDPA in model loader or try without torch compile
  - *From: Daflon*

- **Problem:** Flash attention errors after torch updates
  - **Solution:** Uninstall flash attention entirely - it's not necessary
  - *From: Kijai*

- **Problem:** Stand-In likeness degraded after wrapper update
  - **Solution:** Issue with kv_cache implementation affecting performance vs quality
  - *From: Kijai*

- **Problem:** Official FUN workflow OOMs on RTX 5090 with Canny
  - **Solution:** Add resize node before Canny preprocessing - the workflow was missing this essential step
  - *From: Drommer-Kille*

- **Problem:** Stand-in workflow produces black output with RuntimeWarning
  - **Solution:** Merge LoRAs to true or use fp16 models instead of fp8
  - *From: patientx*

- **Problem:** Gaming USB keyboard doesn't activate early enough for BIOS access
  - **Solution:** Use Windows 'advanced startup' option to restart to BIOS
  - *From: Kijai*

- **Problem:** MediaPipe face mesh node fails to parse
  - **Solution:** Use alternative face detection methods like DWPose or Florence2, or install missing requirements: pip install onnx onnxruntime-gpu
  - *From: Kijai*

- **Problem:** Fun 2.2 reference not working
  - **Solution:** Issue was fp8 scaling of ref_conv layer - use unscaled models or fp16 versions
  - *From: Kijai*

- **Problem:** Fantasy Portrait node errors on initial setup
  - **Solution:** Install missing requirements: pip install opencv-python onnx onnxruntime-gpu scipy tqdm accelerate
  - *From: 852話 (hakoniwa)*

- **Problem:** All WanVideoWrapper nodes fail to load due to FantasyPortrait dependencies
  - **Solution:** Install onnxruntime dependency, Kijai updated code to catch exceptions
  - *From: SonidosEnArmonía*

- **Problem:** Wan 2.2 Fun Control Camera GGUF has gradient errors and tensor type mismatches
  - **Solution:** Update WanVideoWrapper to latest version, Kijai added fixes for gradient issues
  - *From: Daflon*

- **Problem:** High noise sampler looking blown out without lightning/light2x
  - **Solution:** Try plugging same lora into both high and low noise, possibly turn up strength in HIGH
  - *From: anever*

- **Problem:** Stand-in not using reference image properly
  - **Solution:** Prompt also contributes a lot, need to avoid conflicting prompts like 'white glasses' when not wanted
  - *From: T2 (RTX6000Pro)*

- **Problem:** Wan 2.2 Lightning LoRAs destroying motion quality
  - **Solution:** Try 1.0 strength for both high and low instead of 3.0/1.0, or stick with LightXV 2.1 LoRAs
  - *From: Lodis*

- **Problem:** Canny control producing bad output with canny lines
  - **Solution:** Use inverted canny (black lines, white background) and reduce strength from 1.5 to 1.0
  - *From: xwsswww*

- **Problem:** Context windows causing snapping to start frame
  - **Solution:** Stride helps but may not give good results with context
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Problem:** Canny map not working properly
  - **Solution:** Inverting the canny map fixed the problem
  - *From: Lodis*

- **Problem:** I2V resize resizing from 720 to 704
  - **Solution:** Must be divisible by 32 for proper functioning
  - *From: mdkb*

- **Problem:** Fantasy Portrait IndexError: list index out of range
  - **Solution:** Probably frame count mismatch or face detection failure in some frame
  - *From: Kijai*

- **Problem:** FantasyPortrait face detection issues
  - **Solution:** Use video with trackable face, check for frame mismatch issues
  - *From: Josiah*

- **Problem:** CompilationError with fp8e4nv not supported
  - **Solution:** Use e5m2 quantization instead of e4m3fn when using torch.compile on RTX 3090
  - *From: Kijai*

- **Problem:** Memory allocation crashes with large RAM usage
  - **Solution:** Remove all block offloading to solve RAM-related crashes
  - *From: Obsolete*

- **Problem:** VACE inpainting showing annoying lines in output
  - **Solution:** Don't blur the mask, only blur the final composition. First frame with no mask causes VACE to register black lines as desired content
  - *From: Kijai*

- **Problem:** Missing onnx installation causing node failures
  - **Solution:** Install onnx and onnxruntime-gpu: pip install -U onnx onnxruntime-gpu
  - *From: Kijai*

- **Problem:** I2V model channel mismatch (32 vs 36 channels)
  - **Solution:** Must use WanImageToVideo node which adds required mask, can't use I2V model without it
  - *From: Kijai*

- **Problem:** Image was RGBA causing workflow failure
  - **Solution:** Add an image to RGB node to convert RGBA to RGB
  - *From: ManglerFTW*

- **Problem:** OOM during model loading
  - **Solution:** Use offload_device and don't launch comfy with --high-vram
  - *From: Kijai*

- **Problem:** Block swap causing ComfyUI crash
  - **Solution:** Use lower block swap values, try 20 instead of 40
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Problem:** WanVideo nodes not showing up
  - **Solution:** Delete all WanVideoWrapper folders, do fresh git pull and reinstall. Manager doesn't work well for this node
  - *From: T2 (RTX6000Pro)*

- **Problem:** Fuse_method validation error with value '6'
  - **Solution:** Change fuse_method from 6 to 'pyramid' or 'linear'
  - *From: Drommer-Kille*

- **Problem:** Extremely slow generation with WanVideoSampler
  - **Solution:** Use block swap (try setting blocks_to_swap to 20) to prevent VRAM saturation
  - *From: Kijai*

- **Problem:** ComfyUI freezing with native nodes on 4090
  - **Solution:** Increase --reserve-vram value (try 5 instead of 2)
  - *From: Kosinkadink*

- **Problem:** Wan 2.2 taking forever on first step due to shared GPU memory usage
  - **Solution:** Use --reserve-vram 5 flag to prevent VRAM spillover to slow shared memory
  - *From: Kosinkadink*

- **Problem:** FantasyPortrait nodes error 'module onnxruntime has no attribute InferenceSession'
  - **Solution:** pip uninstall onnxruntime onnxruntime-gpu, then pip install onnxruntime-gpu==1.22.0
  - *From: A.I.Warper*

- **Problem:** FantasyPortrait running extremely slow (1.75it/s)
  - **Solution:** Remove conflicting onnxruntime package, keep only onnx and onnxruntime-gpu
  - *From: Kijai*

- **Problem:** Wan 2.2 first frame OK but degrading after with denoise 0.60
  - **Solution:** Not explicitly solved but identified as common issue
  - *From: DeeX*

- **Problem:** Windows VRAM estimation causes slow swap to RAM
  - **Solution:** Windows driver does super slow swap instead of OOM - reserve-vram flag prevents this
  - *From: Kosinkadink*

- **Problem:** RuntimeError: The size of tensor a (48360) must match the size of tensor b (53040) at non-singleton dimension 1
  - **Solution:** Ensure all dimensions and frame counts are the same between VACE input vs model input
  - *From: Kijai*

- **Problem:** 'WanVideoVAE' object has no attribute 'get' error
  - **Solution:** Re-create the VAE node and re-connect it, or use muting instead of bypassing nodes
  - *From: Kijai*

- **Problem:** Ghosting issues with Fun Control models
  - **Solution:** Increase high noise pass steps (try 4+4 instead of 2) and ensure correct lora strengths
  - *From: Kijai*

- **Problem:** Context options with Wan 2.2 not smooth between slots
  - **Solution:** Flow between context slots restarts from first frame, unlike AnimateDiff which was smoother - no permanent solution provided
  - *From: xwsswww*

- **Problem:** Switch nodes breaking with bypassed nodes overnight
  - **Solution:** Use lazy switches instead of bypass/muting, or switch to different switch node types that work with current ComfyUI
  - *From: Nekodificador*

- **Problem:** Unwanted character talking/yapping in generations
  - **Solution:** Use empty audio track with MultiTalk, or negative prompts with 'character is talking' when using CFG
  - *From: Kijai*

- **Problem:** ComfyUI queue stops working and loader nodes won't accept input
  - **Solution:** Disable multithread option in color match node as potential fix
  - *From: Kijai*

- **Problem:** No input found for flattened id error with GetNode
  - **Solution:** Error occurs when GetNode is bypassed in new ComfyUI - frontend change now passes data through bypassed nodes
  - *From: phazei*

- **Problem:** Block swap disk space doesn't clear after generation
  - **Solution:** Need to restart PC to clear disk swap buildup, or use old ComfyUI menu instead of new menu
  - *From: xwsswww*

- **Problem:** Flash effect when using full latents for video continuation
  - **Solution:** Use I2V model instead of T2V for latent continuation, as I2V can handle full latents better
  - *From: Kijai*

- **Problem:** GGUF conversion requires llama.cpp compilation
  - **Solution:** Use nodes that auto-build llama.cpp or install full CUDA toolkit with nvcc
  - *From: Kijai*

- **Problem:** PUSA LoRA hitting max VRAM on ksampler while i2v 2.2 works fine
  - **Solution:** PUSA sampling inherently uses more VRAM regardless of LoRA format - this is expected behavior
  - *From: Kijai*

- **Problem:** FantasyPortrait nodes not available due to import error
  - **Solution:** Install onnx and onnxruntime-gpu: pip install onnx onnxruntime-gpu
  - *From: Kijai*

- **Problem:** ComfyUI memory management issues with model offloading
  - **Solution:** Use --disable-smart-memory flag, create 32GB static swap file, trade everything to RAM possible
  - *From: mdkb*

- **Problem:** Fun-Control reference image not working with fp8_scaled model
  - **Solution:** Use fixed versions of models from Kijai's HF repo - initial models had mistake in ref_conv layer for fp8
  - *From: Kijai*

- **Problem:** Saved latent file not appearing in LoadLatent dropdown
  - **Solution:** Move the .latent file to the /input directory for ComfyUI to recognize it
  - *From: gokuvonlange*

- **Problem:** Model loading order causing OOM with dual samplers
  - **Solution:** Set second model loader load_device to offload_device instead of main_device
  - *From: phazei*

- **Problem:** UnboundLocalError: local variable 'bidirectional_sampling' referenced before assignment
  - **Solution:** Fixed in latest commit on main branch
  - *From: Kijai*

- **Problem:** VACE single image failing with error about latent dimensions
  - **Solution:** Use 5 frames: first with change/mask, 4 empty gray frames
  - *From: Nekodificador*

- **Problem:** Qwen-image to WAN bridge creating only noise
  - **Solution:** Connect to image conditioning input, not samples input, and ensure correct temporal dimensions (21 latents for 81 frames)
  - *From: fredbliss*

- **Problem:** Context windows causing drift and inconsistency
  - **Solution:** Use 48 overlap, but still has limitations with I2V models that need start images
  - *From: Kijai*

- **Problem:** WAN 2.2 outputs appearing sped up compared to 2.1
  - **Solution:** Consider saving at 12fps then doubling with RIFE instead of 16fps
  - *From: Fawks*

- **Problem:** WanVideoContextOptions error: fuse_method '6' not in list
  - **Solution:** Use 'linear' or 'pyramid' as fuse_method values instead of numeric values
  - *From: 𝕯𝖗. 𝕸𝖆𝖈𝖆𝖇𝖗𝖊 ☠*

- **Problem:** Double LightX LoRA causing exaggerated movements
  - **Solution:** Remove duplicate LightX LoRA connections
  - *From: VRGameDevGirl84(RTX 5090)*

- **Problem:** Video LoRA only focused on one outfit despite captions
  - **Solution:** Add image dataset with outfit variations alongside video dataset
  - *From: Ryzen*

- **Problem:** Bidirectional sampling OOMs on RTX 3090
  - **Solution:** Issue identified and PR submitted to fix
  - *From: Kosinkadink*

- **Problem:** Fantasy Portrait arms don't move
  - **Solution:** Use end frame where arms are positioned down
  - *From: VRGameDevGirl84(RTX 5090)*

- **Problem:** Tensor size mismatch errors with context windows
  - **Solution:** Check that frame count is divisible by 16 and use valid frame counts like 57, 61 instead of 60
  - *From: Kijai*

- **Problem:** 12-pin connector melting during training
  - **Solution:** System shutdown required, cable melted from center but connector side was okay
  - *From: Ryzen*

- **Problem:** ONNX dependency missing for FantasyPortrait
  - **Solution:** Install onnx and onnxruntime-gpu: pip install onnx onnxruntime-gpu
  - *From: Kijai*

- **Problem:** Context window drift with fantasy portrait
  - **Solution:** Use more overlap (32 instead of 16) and 81 frame context size
  - *From: Kijai*

- **Problem:** Jiggling motion with Lightning 4-steps
  - **Solution:** Try CFG=2 on HIGH and CFG=1 on LOW, adjust shift value and CFG to find right motion
  - *From: Ashtar*

- **Problem:** MMAudio expecting 25fps but Wan generates 16fps
  - **Solution:** Use 3x interpolation then drop every other frame to get close to 25fps
  - *From: Kijai*

- **Problem:** WanModel.__init__() got unexpected keyword argument 'use_motion_attn'
  - **Solution:** Fixed in repository update
  - *From: Kijai*

- **Problem:** torch.compile errors with GGUF on second generation
  - **Solution:** Claude suggested fix worked - input tensors on cuda:0, weight tensors after dequantization on cpu
  - *From: patientx*

- **Problem:** Rounding difference errors in video generation
  - **Solution:** Set divisible by 16 or 32, ensure frame count and resolution match across inputs
  - *From: Kijai*

- **Problem:** OutOfMemoryError with context windows
  - **Solution:** Increase block swap amount, reduce resolution to test, use save latent node for long videos
  - *From: Kijai*

- **Problem:** Face not detected in FantasyPortrait
  - **Solution:** Input resolution needs to be higher or more direct face view
  - *From: Kijai*

- **Problem:** Block swap with use_non_blocking fails with torch.compile
  - **Solution:** Turn off use_non_blocking when using torch.compile
  - *From: scf*

- **Problem:** Input shape mismatch error in Wan video wrapper
  - **Solution:** Check image resolutions and/or frame count compatibility
  - *From: Kijai*

- **Problem:** Tensor size error with native context
  - **Solution:** Sizes of tensors must match except in dimension 1. Expected size 21 but got size 42
  - *From: Draken*

- **Problem:** Queue control feature not working properly
  - **Solution:** Clicking queue control runs full queue instead of selective execution
  - *From: Ablejones*

- **Problem:** Audio stops after 5s in Multi-talk workflow despite 16s video
  - **Solution:** Issue with audio passthrough in Multi-talk-long workflow
  - *From: BobbyD4AI*

- **Problem:** Looping effect with skyreels lora on 2.2
  - **Solution:** Increase LoRA strength to 1.8/1.5 (high/low) to break the looping
  - *From: NebSH*

- **Problem:** MultiTalk and InfiniteTalk mouth not moving
  - **Solution:** Set multitalk fps to 30 and audio cfg to 2
  - *From: Charlie*

- **Problem:** Talking models not working properly
  - **Solution:** Set add noise to samples to true and drop denoise down to 0.7
  - *From: VRGameDevGirl84(RTX 5090)*

- **Problem:** CUDA cache issues with fragmentation
  - **Solution:** Cache management is unpredictable - fragments and grows due to ecosystem interactions
  - *From: Clownshark Batwing*

- **Problem:** FP32/FP16 mixed model running very slowly
  - **Solution:** Model should use 30gb dedicated and 40gb total VRAM with 40 blocks swapped for proper performance
  - *From: seitanism*

- **Problem:** Mismatched landmarks between ref image and driving video
  - **Solution:** Replace first frame of driving video with ref image to align landmarks, then use VHS nodes to merge frames
  - *From: mamad8*

- **Problem:** Infinite embed errors when using InfiniteTalk
  - **Solution:** Cannot have both KJ's wrapper and MeiGen-AI's fork installed simultaneously
  - *From: Kijai*

- **Problem:** WanVideoSampler tensor size mismatch error
  - **Solution:** Disable all FantasyPortrait related nodes
  - *From: SonidosEnArmonía*

- **Problem:** VACE embedding causes core dumps and disk filling
  - **Solution:** Use MagRef instead for identity preservation
  - *From: mdkb*

- **Problem:** Qwen Image Edit black output
  - **Solution:** Disable sage attention in settings
  - *From: Lodis*

- **Problem:** Can't see InfiniteTalk option in node
  - **Solution:** Remove MeiGen-AI fork and use only KJ's wrapper
  - *From: Kijai*

- **Problem:** Scaled model compatibility
  - **Solution:** Both main and extra models must be _scaled versions or neither
  - *From: Kijai*

- **Problem:** Noise output when using fp8_scaled models with merged LoRAs
  - **Solution:** Disable merge_loras or use unmerged LoRAs - merging not working with _scaled multitalk models
  - *From: Kijai*

- **Problem:** Audio/video sync issues in InfiniteTalk
  - **Solution:** Use input fps to feed output fps, keep 25fps for embeds and use exact frame calculation from audio length
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Problem:** Error with clip_embeds NoneType
  - **Solution:** Loop expects clip embeds to always be there, can work around by setting strengths to 0 or providing clip embeds
  - *From: Kijai*

- **Problem:** Can't use Image to Video MultiTalk with context options
  - **Solution:** Use normal I2V node instead with context - they are not compatible conceptually
  - *From: Kijai*

- **Problem:** Latent previews not working
  - **Solution:** Need to update VHS nodes and refresh browser fully after update
  - *From: Kijai*

- **Problem:** KeyError 'samples' in WanVideoWrapper
  - **Solution:** Don't use multitalk image to vid node with regular samplers - it makes the first sampler loop and decode in the loop, so it never returns latents
  - *From: Kijai*

- **Problem:** Black generation when changing LoRA with scaled model
  - **Solution:** Need to restart when changing LoRAs with scaled models
  - *From: ArtOfficial*

- **Problem:** Out of memory with InfiniteTalk + FantasyPortrait
  - **Solution:** Use blockswap (try 20-40), reduce resolution, or use context windows instead of multitalk node
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Problem:** Audio sync issues with InfiniteTalk
  - **Solution:** Don't use multitalk node for 81 frames and under, use regular I2V node instead
  - *From: Kijai*

- **Problem:** Scaled fp8 model error
  - **Solution:** Set quantization to '_scaled' when using scaled fp8 models
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Problem:** Extra video frames beyond audio length
  - **Solution:** For short clips under 81 frames, don't use the multitalk node at all
  - *From: Kijai*

- **Problem:** ComfyUI nodes out of date for InfiniteTalk
  - **Solution:** Don't update through manager, it can't keep up with Kijai - use git pull directly from folder or GitHub Desktop
  - *From: DawnII*

- **Problem:** Error with torch.compile on RTX 3090
  - **Solution:** Need 4000 series GPU or higher to use torch.compile with fp8_e4m3fn weights, use e5m2 or GGUF Q8 instead on 3090
  - *From: Kijai*

- **Problem:** numpy remapping warning
  - **Solution:** Install numpy==1.26.4 with 'python -m pip install numpy==1.26.4' - manager is forcing numpy version under 2.0
  - *From: shockgun*

- **Problem:** ComfyUI refresh nodes after UI change
  - **Solution:** Use 'R' shortcut key to refresh nodes without restarting
  - *From: Kijai*

- **Problem:** Bad T2I quality results
  - **Solution:** Check CFG settings - user had CFG set to wrong value, also avoid using CFG with no negative prompt
  - *From: Dream Making*

- **Problem:** InfiniteTalk fails at specific frame lengths
  - **Solution:** Try doing more frames - fails at certain lengths due to overlap issues
  - *From: Kijai*

- **Problem:** First frame noise issues in videos
  - **Solution:** Use multitalk image to video encode node and change mode to 'infinitetalk', get rid of context windows, or add empty buffer frames to start
  - *From: ArtOfficial, Kijai*

- **Problem:** Tensor creation error with negative dimension when using context
  - **Solution:** Getting error 'Trying to create tensor with negative dimension -10: [16, -10, 60, 104]' on high noise when plugging context
  - *From: NebSH*

- **Problem:** Motion reverses or does weird stuff
  - **Solution:** Try context options with different context lengths for each, consider doing only one step on high noise since it seems to break in high noise but low noise is fine
  - *From: Tango Adorbo*

- **Problem:** LoRA only generating one type of outfit
  - **Solution:** Lower LoRA strength to 0.8, set CFG to 3 instead of 1, use NAG to add specific outfit keywords to negative when using LoRA
  - *From: Ryzen, mamad8*

- **Problem:** OutOfMemoryError after updating WanWrapper
  - **Solution:** Allocation error is about VRAM not RAM, check batch size settings
  - *From: shockgun, Kijai*

- **Problem:** Wan Video NAG does not work with gguf clip encoder
  - **Solution:** User got it working but didn't specify the exact solution
  - *From: xwsswww*

- **Problem:** TypeError: sageattn() got an unexpected keyword argument 'tensor_layout'
  - **Solution:** Need to have the Sage Attention lib installed and working
  - *From: . Not Really Human :.*

- **Problem:** V2V with InfiniteTalk requires exact frame matching
  - **Solution:** Input sample length must equal frame_window_size, may need to split input video into 81 frame chunks
  - *From: MysteryShack*

- **Problem:** Wan 2.2 low noise upscale causing OOM
  - **Solution:** Use image upscaling instead of latent space
  - *From: VRGameDevGirl84(RTX 5090)*

- **Problem:** Static appearing at start of each section in endless workflow with InfiniteTalk
  - **Solution:** Need to adjust settings and create custom node to remove static
  - *From: VRGameDevGirl84(RTX 5090)*

- **Problem:** ComfyUI preview broke after update
  - **Solution:** Update VHS
  - *From: Lodis*

- **Problem:** Node connection issues in workflow
  - **Solution:** Clear cache and reboot
  - *From: 𝕯𝖗. 𝕸𝖆𝖈𝖆𝖇𝖗𝖊 ☠*

- **Problem:** MMaudio only generating 3 seconds of audio for 5-second video
  - **Solution:** Need to be at 25 fps for audio to match video duration. MMaudio is initially set to 8 seconds but requires 25 fps sync
  - *From: .: Not Really Human :.*

- **Problem:** Latent input connection issue after update
  - **Solution:** Refresh browser after update - the latent input to that node is optional in current version
  - *From: Kijai*

- **Problem:** High swap usage in wrapper
  - **Solution:** Use --cache-none or --disable-smart-memory flags
  - *From: MysteryShack and mdkb*

- **Problem:** InfiniteTalk producing first frame noise when not using loop
  - **Solution:** Update nodes and set 'encode init image' option when NOT using the Multitalk image to video loop sampling. The code detects when InfiniteTalk is loaded and injects encoded image to first latent on every step.
  - *From: Kijai*

- **Problem:** MAGREF_Wan2.1_I2V_14B-Q6_K.gguf producing all noise output with InfiniteTalk
  - **Solution:** Don't mix gguf with other model types. Use gguf InfiniteTalk model with gguf Wan models, or safetensors with safetensors. LoRAs can be mixed with either type.
  - *From: Kijai*

- **Problem:** ComfyUI custom node conflicts causing issues
  - **Solution:** If multiple node packs have identical node names, only one is used. Remove conflicting forks and ensure you're running the most recent code version. Use git pull and check you're on the correct branch.
  - *From: Kijai*

- **Problem:** Wan 2.2 FLF second input going grey
  - **Solution:** Need at least 81 frames for Wan 2.2 FLF to work properly. Second input also goes grey when going 180+ frames - must stay within bounds.
  - *From: cyber jock*

- **Problem:** Cannot copy out of meta tensor; no data! issues with gguf Q8
  - **Solution:** Use pytorch version: 2.8.0+cu129
  - *From: yukass*

- **Problem:** RuntimeError: Trying to create tensor with negative dimension
  - **Solution:** Update WanVideoWrapper nodes
  - *From: DawnII*

- **Problem:** Fantasy Portrait Face Detector extremely slow on GPU
  - **Solution:** Uninstall and reinstall onnxruntime-gpu
  - *From: theUnlikely*

- **Problem:** Control signal only works with Fun-Control model error
  - **Solution:** Update Kijai nodes - support was added today
  - *From: Kijai*

- **Problem:** Extra tail frames being generated
  - **Solution:** Audio frames should be (n*total frames - n*motion frames)
  - *From: DawnII*

- **Problem:** Can't mix GGUF with non-GGUF models
  - **Solution:** Use matching format models - GGUF InfiniteTalk needs GGUF main Wan model
  - *From: Kijai*

- **Problem:** Preview Actual Frames doesn't work
  - **Solution:** Nodes not up to date, need latest push from Kijai
  - *From: Kijai*

- **Problem:** Extra 81 tail frames appearing at end
  - **Solution:** This is normal behavior, can cut off the extra frames
  - *From: Kijai*

- **Problem:** MultiTalkWav2VecEmbeds error 'audio' vs 'audio_1'
  - **Solution:** Need to load multitalk weights and connect multitalk loader to WAN model
  - *From: samhodge*

- **Problem:** Video degrading quality
  - **Solution:** Update to nightly version of WanVideoWrapper and set mode to InfiniteTalk
  - *From: sawlike*

- **Problem:** Can't find mode option in InfiniteTalk node
  - **Solution:** Need to manually update with 'git pull' from ComfyUI-WanVideoWrapper folder, nightly is behind latest
  - *From: Josiah*

- **Problem:** Character inconsistency in vid2vid
  - **Solution:** Later start step with less denoise means less change from original, need controlnet or crop/paste for better consistency
  - *From: DawnII*

- **Problem:** Getting noise from low noise sampler in Wan 2.2
  - **Solution:** Need denoised output from high noise stage - samples doesn't return same dict in infinitetalk mode, just returns video entry instead of samples and denoised samples
  - *From: MysteryShack*

- **Problem:** VACE and Phantom won't work together
  - **Solution:** Both work perfectly alone but fail when combined - possible bug when VACE model is plugged into combo of nodes with Phantom model
  - *From: mdkb*

- **Problem:** Ghost effect at borders with blurred masks in inpainting
  - **Solution:** Binary masks work much better than blurred masks for this type of inpainting
  - *From: Nekodificador*

- **Problem:** InfiniteTalk locked at 1000 frames
  - **Solution:** Check max frames setting in the workflow - there's a parameter that can be adjusted
  - *From: JohnDopamine*

- **Problem:** Quality degradation in I2V with Ksampler low
  - **Solution:** Use native 2 ksamplers: first stage high 2 steps without lora, second low stage 2 steps with lora
  - *From: Not Really Human*

- **Problem:** VACE doesn't handle blurred masks properly
  - **Solution:** Use binary masks instead of blurred ones for better results
  - *From: Kijai*

- **Problem:** InfiniteTalk became very slow after wrapper update
  - **Solution:** Check audio_cfg value - it does 3 passes. Roll back wrapper or debug configuration
  - *From: seitanism*

- **Problem:** Getting noise with 3x ksampler trick
  - **Solution:** Check shift node connection and ksampler step settings - ensure consistent step counts
  - *From: Ghost*

- **Problem:** Multi VACE broke after recent update
  - **Solution:** Revert to commit 6d51934ae816e9c87fb9b6183fb644d7fd564943 which works
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Problem:** Fantasy Portrait fails when no face detected
  - **Solution:** Face detection skips frames without faces, causing len(frame_list)=0. Check face detection in input frames
  - *From: fredbliss*

- **Problem:** VACE acting weird after update
  - **Solution:** Fixed by Kijai - was a bug when using multiple VACEs
  - *From: chrisd0073*

- **Problem:** Runtime error with mat1 and mat2 shapes in WAN bridge
  - **Solution:** Was passing input image latent into samples instead of correct input
  - *From: fredbliss*

- **Problem:** Windows Explorer crashes when selecting video files from WanVideoSampler
  - **Solution:** Remove metadata with ffmpeg or disable metadata saving in VHS node - issue caused by large workflow metadata (214KB)
  - *From: Ashtar*

- **Problem:** Error 'cannot access local variable noise_mask' in infinitetalk
  - **Solution:** Fixed by Kijai - was testing without mask and forgot to handle that case
  - *From: Intellectus Prime*

- **Problem:** WanVideoEncode pbar error
  - **Solution:** Force update of WanVideoWrapper nodes
  - *From: Juan Gea*

- **Problem:** 5B model generating slow motion despite settings
  - **Solution:** No specific solution provided, acknowledged as ongoing issue
  - *From: Juan Gea*

- **Problem:** Latent noise mask not working for vid2vid
  - **Solution:** Need to set mask for both high and low noise sides, and original image required for 2nd sampler
  - *From: Kijai*

- **Problem:** Masks not working from Blender renders
  - **Solution:** Ensure masks are white on black, convert to mask in ComfyUI. Source doesn't matter if format is correct
  - *From: Kijai*

- **Problem:** GGUF InfiniteTalk model not appearing in MultiTalk Model Loader
  - **Solution:** Update WanVideoWrapper nodes or check for conflicting installations overwriting nodes
  - *From: Kijai*

- **Problem:** Differential diffusion works poorly with low steps
  - **Solution:** Thresholds should be calculated from total steps rather than actual sampler steps
  - *From: Kijai*

- **Problem:** UniAnimate with GGUF models causes errors
  - **Solution:** UniAnimate won't work with GGUF models, use non-GGUF versions
  - *From: Kijai*

- **Problem:** Blurred video output
  - **Solution:** Check scheduler, CFG settings, and step count. Use steps 4, cfg 1, shift 1 for distill models
  - *From: samhodge*

- **Problem:** Latent upscale not working with nearest exact
  - **Solution:** Use bilinear instead and apply cinescale lora on both high and low, but works better on low
  - *From: Kijai*

- **Problem:** ComfyUI shutting down when using prompt extender
  - **Solution:** Change base precision from fp16 to bf16 in the qwen loader
  - *From: seitanism*

- **Problem:** Getting OOM with text encoders
  - **Solution:** Issue was torch compiler - disabling it reduces VRAM use quite a bit
  - *From: Kenk*

- **Problem:** Repeat latent batch not working for static camera
  - **Solution:** Repeat the image first, then encode - don't repeat the latents directly
  - *From: DawnII*

- **Problem:** T2V with 5B turbo getting confetti and distortion
  - **Solution:** Use A14B model instead of E5, and use dpm++_sde sampler instead of flowmatch_distill for T2V
  - *From: Kijai*

- **Problem:** CUDA out of memory errors with VACE Start End Frame
  - **Solution:** Disable non-blocking on block swap setting - CUDA out of memory = RAM error, not VRAM
  - *From: Kijai*

- **Problem:** Film grain node OOM errors on 800+ frame videos
  - **Solution:** Node has limitations for processing very long videos, no current workaround for that length
  - *From: Kenk*

- **Problem:** Multitalk error 'cannot reshape tensor of 0 elements'
  - **Solution:** Error means empty input or zero batch size, check audio loading and don't use Multitalk long I2V node with audio under 5 seconds
  - *From: Kijai*

- **Problem:** Bidirectional sampling OOM errors even on RTX 5090
  - **Solution:** Known issue, no current solution provided
  - *From: Roman_S*

- **Problem:** Context windows producing size of tensor errors in native version
  - **Solution:** Very difficult to run without errors, context windows not intended to work on 2.2 model yet
  - *From: Mngbg*

- **Problem:** First frames overexposure in videos longer than 5 seconds
  - **Solution:** Use skyreels LoRA, though the fix node mentioned may not actually solve this issue
  - *From: Kijai*

- **Problem:** Control signal only works with Fun-Control model error
  - **Solution:** Update nodes or check for conflicting WanVideoWrapper versions in custom nodes folder
  - *From: Kijai*

- **Problem:** Hard crashes after low noise model finishes
  - **Solution:** Use Cached text encoder node to save 10GB RAM - swap regular text encoder for cached version
  - *From: Kijai*

- **Problem:** No audio in InfiniteTalk output
  - **Solution:** Cannot have bypass on audio processing nodes - remove bypass
  - *From: Kijai*

- **Problem:** Torch compile using more VRAM on first run
  - **Solution:** Use more block swap to get past initial VRAM spike, issue seems related to torch 2.8 update
  - *From: Kijai*

- **Problem:** Video breaks halfway in short clips
  - **Solution:** Don't use multitalk node for clips under 7s, use normal I2V node instead
  - *From: Kijai*

- **Problem:** Strobe flashing in i2v generations
  - **Solution:** Use more compute/original parameters, issue occurs when not using enough compute
  - *From: aikitoria*

- **Problem:** LoRAs not working with CFG Schedule in wrapper
  - **Solution:** Bump lora strength to 2.0 to make them work with CFG Schedule
  - *From: Drommer-Kille*

- **Problem:** Color degradation with Wan 2.2
  - **Solution:** Issue acknowledged but no specific solution provided
  - *From: Kenk*

- **Problem:** InfiniteTalk cutting audio short
  - **Solution:** No solution provided, issue acknowledged
  - *From: amli*

- **Problem:** InfiniteTalk OOM on 12GB VRAM
  - **Solution:** Memory issue caused by VAE cache not clearing between windows - fix in development
  - *From: Kijai*

- **Problem:** UniAnimate crash with resolution mismatch
  - **Solution:** Need enough pose images to match the total frames including overlap - looping method needs more frames than window size due to overlap
  - *From: Kijai*

- **Problem:** VACE quality issues at 1280x720
  - **Solution:** Check mask quality (must be perfect, no blur) and consider using PUSA LoRA for color preservation
  - *From: dg1860*

- **Problem:** FP8 fast mode won't work with unmerged LoRAs
  - **Solution:** Use the merge_loras switch in the lora select node
  - *From: Kijai*

- **Problem:** Image resizing in wrapper
  - **Solution:** Images not divisible by 16 get automatically resized (e.g. 512x910 becomes 512x896)
  - *From: Gateway {Dreaming Computers}*

- **Problem:** First 1-3 frames with InfiniteTalk look corrupted
  - **Solution:** Try using additional nodes and connecting to first sampler cfg input
  - *From: Kenk*

- **Problem:** VRAM hitting 100% causing infinite generation times
  - **Solution:** Keep VRAM below 95% on Windows by increasing block swap amount
  - *From: Kijai*

- **Problem:** Colors taking a hit when using InfiniteTalk
  - **Solution:** Hook InfiniteTalk only into high sampler, not both high and low
  - *From: Draken*

- **Problem:** Fantasy face detector node failing
  - **Solution:** Needs a video input, not a single image. Some frames may be skipped if no faces detected
  - *From: Kijai*

- **Problem:** Double application of shift values
  - **Solution:** Set sampler shift to 1.0 to avoid double applying when using shift on both dummy object and sampler
  - *From: Kijai*

- **Problem:** InfiniteTalk V2V workflow broken after WanNode update
  - **Solution:** Fixed in update
  - *From: Yae/Kijai*

- **Problem:** Openpose appearing in video outputs
  - **Solution:** Condition separately, decrease VACE strength, try seed changes
  - *From: Piblarg*

- **Problem:** Mixing control signals when combining pose/depth/lineart
  - **Solution:** Use WanVacePhantomDualV2 for separate control inputs instead of combining into single control image
  - *From: Ablejones*

- **Problem:** InfiniteTalk losing coherence at end with extensions
  - **Solution:** Fix first latent noise by injecting the image as encoded latent to index 0 using extra_latents
  - *From: Kijai*

- **Problem:** FantasyPortrait overdoing teeth generation
  - **Solution:** Tone down FantasyPortrait settings
  - *From: Kijai*

- **Problem:** Video not starting with input image in InfiniteTalk
  - **Solution:** Mentioned as Problem 2 by user, no solution provided in chat
  - *From: Gill Bastar*

- **Problem:** Artifacts at end of InfiniteTalk videos
  - **Solution:** Might be related to LoRAs being used, no specific solution provided
  - *From: Gill Bastar*

- **Problem:** Slow ImageToVideo encoding with BigASP SDXL images
  - **Solution:** Resize image before the node - source model makes zero difference to encoding
  - *From: Kijai*

- **Problem:** VACE keeps generating cowboys/Brokeback Mountain theme instead of intended character
  - **Solution:** Position the reference image accurately - overlay it in image editor at exact position where character should appear in final video
  - *From: mdkb*

- **Problem:** InfiniteTalk video artifacts get progressively worse
  - **Solution:** Set mode to 'infinitetalk' in the node and update wanvideowrapper to nightly
  - *From: brock0ut11*

- **Problem:** First 4-5 frames appear latent/pixelated in InfiniteTalk
  - **Solution:** Use the proper InfiniteTalk workflow from wrapper - set first latent to be the start image as InfiniteTalk model expects
  - *From: Kijai*

- **Problem:** Fun InP model channel mismatch error
  - **Solution:** Cannot use control with InP model - must use Fun-Control model for control inputs. InP = 36 channels, Fun-Control = 52 channels
  - *From: Kijai*

- **Problem:** Temporal mask casting error in image encoding
  - **Solution:** Fixed in latest update - was related to fp32 VAE optimization
  - *From: Kijai*

- **Problem:** Fun-Control reference image won't work with fp8_scaled model
  - **Solution:** Fixed in latest version of the model, requires redownload
  - *From: scf*

- **Problem:** OOM error with 96GB VRAM and 128GB RAM when loading fp16 model
  - **Solution:** Need to add paging file/swap file even with large RAM amounts
  - *From: Ablejones*

- **Problem:** Cannot access local variable 'h_len' error when using standin
  - **Solution:** Update to latest version with fix
  - *From: Kijai*

- **Problem:** Infinite Talk color degradation in I2V mode
  - **Solution:** Use MAGREF model to prevent degradation, though it's blurrier
  - *From: seitanism*

- **Problem:** Multitalk doesn't work with regular models
  - **Solution:** Update nodes and use specified models
  - *From: Gill Bastar*

- **Problem:** Mmaudio truncation with 16fps Wan output
  - **Solution:** Mmaudio expects 24 or 25 fps input
  - *From: Kijai*

- **Problem:** ComfyUI-WanVideoWrapper tensor size mismatch error in WanVideo Sampler
  - **Solution:** Kijai fixed variable definition error, update the wrapper
  - *From: Kijai*

- **Problem:** VAE decode errors with second samplers in FFLF workflows
  - **Solution:** Update wrapper - was error in variable definition affecting 2.2 first frame last frame workflows
  - *From: Kijai*

- **Problem:** Get/set nodes causing errors when bypassing
  - **Solution:** Known ComfyUI issue since recent frontend updates
  - *From: Kijai*

- **Problem:** Ghosting/blurry generations with default Wan 2.2 i2v workflow
  - **Solution:** Try changing resolution to match source aspect ratio (e.g. 432x768), check high/low lightx LoRAs are correct
  - *From: garbus*

- **Problem:** Characters keep talking despite prompting for silence
  - **Solution:** Try multitalk node with 5 seconds of silence in audio, or prompts like 'characters do not talk to each other' at end
  - *From: mdkb*

- **Problem:** 2.2 + infinite context causing OOM
  - **Solution:** Won't work with any 2 sampler setup, check max frames not set as frame window size
  - *From: Kijai*

- **Problem:** Non-blocking block swap stops workflow on 3060
  - **Solution:** Disable non-blocking religiously on 3060
  - *From: mdkb*

- **Problem:** Video pixelation with InfiniteTalk when using Tea Cache
  - **Solution:** Tea Cache doesn't work with LoRA accelerators, disable it
  - *From: .: Not Really Human :.*

- **Problem:** Color degradation with 2.2 + multitalk
  - **Solution:** Use color match node after generation
  - *From: N0NSens*

- **Problem:** Getting picture instead of video with InfiniteTalk
  - **Solution:** Make sure WanVideo Long I2V Multi/InfiniteTalk node is included - it's necessary for InfiniteTalk to work
  - *From: Mancho*

- **Problem:** Control input missing error (52 vs 36 channels)
  - **Solution:** Control model is loaded but input is normal I2V input missing the control part of 16 channels
  - *From: Kijai*

- **Problem:** HotReloadHack broken after ComfyUI update
  - **Solution:** Switch to Kijai's fork: https://github.com/kijai/ComfyUI-HotReloadHack
  - *From: Kijai*

- **Problem:** VRAM OOM with WanFM on A100 80GB
  - **Solution:** Cancel bidirectional_sampling to make it work
  - *From: Yan*

- **Problem:** Differential diffusion affecting areas outside mask
  - **Solution:** Should do normal pixel space composition after sampling since latent masking always affects whole image through VAE
  - *From: Kijai*

- **Problem:** Wan 2.2 Turbo em52 not working well with e5 model
  - **Solution:** Try the fp16 model instead
  - *From: Kijai*

- **Problem:** WanVideoWrapper error on second run - 'cannot copy out of meta tensor; no data!'
  - **Solution:** Roll back to previous version, issue appears to be with latest version
  - *From: Kenk*

- **Problem:** Blurry unusable results with Wan 2.2 I2V default workflow
  - **Solution:** Try 6 or 8 steps instead of 4, update PyTorch to 2.7+, use shift of 8 for both samplers
  - *From: JohnDopamine/screwfunk*

- **Problem:** Beta sigma conversion applied twice
  - **Solution:** Don't use both beta sigmas and beta version of scheduler together, use normal dpm++_sde
  - *From: Kijai*

- **Problem:** Tensor dimension error with negative values
  - **Solution:** Check for batch mismatch in workflow
  - *From: DawnII*

- **Problem:** Block swap error on second generation with T2V models
  - **Solution:** Fixed in latest update - model loading issue with merged LoRAs resolved
  - *From: Kijai*

- **Problem:** IndexError: index 3 is out of bounds for dimension 0 with size 3
  - **Solution:** Wrong wav2vec2 model - need to use correct model from HuggingFace
  - *From: Kijai*

- **Problem:** einops.EinopsError with S2V resolutions
  - **Solution:** Use resolution formula: (width÷16) × (height÷16) × frames ÷ 30 must be whole number
  - *From: patientx*

- **Problem:** Error running sage attention: Input tensors must be on cuda
  - **Solution:** Don't use --use-sage-attention flag at startup, select it in WanVideo model loader instead
  - *From: patientx*

- **Problem:** Missing AudioEncoderLoader node
  - **Solution:** Need to update to ComfyUI nightly build and git pull
  - *From: Kijai*

- **Problem:** WanVideoSampler stride error with GGUF models
  - **Solution:** Use Kijai's VACE models from HuggingFace instead of VACE+Phantom model - the combined model doesn't work well with wrapper or isn't compatible with WAN 2.2
  - *From: xwsswww*

- **Problem:** Memory spikes and instability in latest WanVideoWrapper
  - **Solution:** Older version of WanVideoWrapper is more stable, latest dev changes cause VRAM spikes
  - *From: Kenk*

- **Problem:** InfiniteTalk creates extra noise frames at end
  - **Solution:** Pad audio with 2 seconds of silence that can be cut off later
  - *From: ArtOfficial*

- **Problem:** ComfyUI native S2V resolution errors
  - **Solution:** Use the bf16 model specifically designed for native implementation with lightx2v
  - *From: patientx*

- **Problem:** Context options causing VRAM OOM on low sampler
  - **Solution:** Connect context options to low sampler, can use less overlap (like 16) on low side while high noise may need up to 48
  - *From: Kijai*

- **Problem:** Context windows cause overblown start in videos
  - **Solution:** so the overblown start is probably something to be expected
  - *From: Kijai*

- **Problem:** Generic issue with Uni3C offloading
  - **Solution:** this should be fixed now, it was generic issue with Uni3C offloading introduced in the refactor. first run would work but any 2nd run would fail because it was accidentally clearing it's weights too along with the model
  - *From: Kijai*

- **Problem:** Memory issues with WanWrapper vs native nodes
  - **Solution:** probably because the offloading is automatic in native and in the wrapper it's manual with the block swap
  - *From: Kijai*

- **Problem:** E5 model not working
  - **Solution:** Try using gguf instead
  - *From: Slavrix*

- **Problem:** fp8_e5m2_fast mode issues
  - **Solution:** you need 4000+ series GPU to use the _fast mode. fp16 fast thing should work on 3090
  - *From: Kijai*

- **Problem:** VAE loader automatically selecting wrong VAE
  - **Solution:** stupid vae loader automatically selecting ae.safetensors each time
  - *From: patientx*

- **Problem:** S2V video gets noised when decoding
  - **Solution:** enabling the second sampler seems to have 'fixed'
  - *From: Kenk*

- **Problem:** Index out of bounds error on second generation
  - **Solution:** Force node reset between runs using cache-clearing nodes or restart workflow
  - *From: GDuque, ˗ˏˋ⚡ˎˊ-*

- **Problem:** Custom LoRAs not working in wrapper
  - **Solution:** Enable merge option in wrapper, as unmerged LoRAs behave differently than native
  - *From: mamad8, Kijai*

- **Problem:** S2V nodes missing in ComfyUI
  - **Solution:** Switch to nightly branch of ComfyUI and s2v branch of WanVideoWrapper
  - *From: ingi // SYSTMS*

- **Problem:** Cannot copy out of meta tensor error with InfiniteTalk
  - **Solution:** Disable offloading when using block swap, as offloading isn't needed
  - *From: Kijai*

- **Problem:** Trying to create tensor with negative dimension error
  - **Solution:** Check audio length and frame count compatibility, ensure proper audio preprocessing
  - *From: Slavrix*

- **Problem:** Color degradation with InfiniteTalk beyond 1 minute
  - **Solution:** Try disabling LightX LoRAs or adjusting their strength
  - *From: boorayjenkins*

- **Problem:** Slow model loading on better GPU
  - **Solution:** Issue may be related to non-native filesystem (NTFS/exFAT on Linux) causing FUSE performance problems
  - *From: MysteryShack*

- **Problem:** VACE Encode OOM with 48GB VRAM on 119 frames 1280x720
  - **Solution:** Issue reported, likely related to recent updates
  - *From: AmirKerr*

- **Problem:** Rife-VFI making 7 second video from 4 second original
  - **Solution:** Probably didn't change fps settings
  - *From: Mu5hr00m_oO*

- **Problem:** DWPose adding excessive teeth in generations
  - **Solution:** Use face points only or multiply pose condition by 0.5
  - *From: Kijai*

- **Problem:** S2V branch installation issues
  - **Solution:** Use git fetch --all, git switch s2v, then git switch main to go back. Use git pull only updates current branch
  - *From: Kijai*

- **Problem:** KeyError: 'frame_packer.proj.weight' in S2V
  - **Solution:** Model loading issue with framepack implementation
  - *From: DawnII*

- **Problem:** Color shift issues with VACE
  - **Solution:** Color Match helps but doesn't solve extreme cases, not a full relight solution
  - *From: Dream Making*

- **Problem:** GGUF models had memory offloading issues causing high VRAM usage
  - **Solution:** Fixed bug where offloading didn't work with GGUF models due to int8 weights not supporting meta device
  - *From: Kijai*

- **Problem:** Chunked rope error in WanVideo model causing RuntimeError
  - **Solution:** Disable compile for now or use e5m2_scaled quantization instead
  - *From: Kijai*

- **Problem:** High and Low noise models were connected incorrectly causing mosaic/confetti artifacts
  - **Solution:** Ensure High noise model goes to second sampler, Low noise model goes to first sampler
  - *From: DawnII*

- **Problem:** Control signals only work with Fun-Control model, not 1.3B model
  - **Solution:** Use Fun-Control model specifically when using control inputs
  - *From: N0NSens*

- **Problem:** Missing start_step value in sampler causing conversion error
  - **Solution:** Right-click on ksampler and pick 'fix node' to reset moved values from updates
  - *From: JohnDopamine*

- **Problem:** S2V model generates wrong number of frames and audio sync issues
  - **Solution:** Check frame count settings and use proper audio loading nodes, model pads with empty if more frames than audio
  - *From: Kijai*

- **Problem:** Error when control lora wasn't last in the list
  - **Solution:** Fixed by ensuring control lora is the last lora in the list
  - *From: Kijai*

- **Problem:** S2V color mismatch in first few frames
  - **Solution:** Comfy posted a fixed workflow for that issue
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Problem:** Git branch switching issues with WanVideoWrapper
  - **Solution:** Reclone the wrapper repository to fix git issues
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Problem:** Memory accumulation in Framepack loop
  - **Solution:** Fixed memory use by putting cache clear in correct place - was accumulating endlessly leading to 7GB wasted
  - *From: Kijai*

- **Problem:** Inpainting distortion in wrapper
  - **Solution:** Disable tiled VAE on the WanVideo VACE encode node to fix center pixel shifting
  - *From: SonidosEnArmonía*

- **Problem:** S2V generates too much music
  - **Solution:** Use negative prompt to control unwanted audio generation, similar to how mmaudio had tendency to add speech
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Problem:** OOM errors and extreme slowdown after updating
  - **Solution:** Set model loader to offload_device instead of main device, and enable tiling on video encoder
  - *From: T2 (RTX6000Pro)*

- **Problem:** Pure noise in I2V infinite talk workflow
  - **Solution:** Connect the VAE - this was missing
  - *From: Kijai*

- **Problem:** InfinityTalk workflow showing KeyError about cross_attn weights
  - **Solution:** Roll back a few commits (git checkout bc22008) - caused by block prefetch feature change
  - *From: SonidosEnArmonía*

- **Problem:** ComfyUI crashing when generating 500+ frames
  - **Solution:** Change main device to offload_device in model loader settings
  - *From: 𝕯𝖗. 𝕸𝖆𝖈𝖆𝖇𝖗𝖊 ☠*

- **Problem:** Artifacts and overlap in infinite talk outputs
  - **Solution:** Remove AccVid LoRA - it was causing the artifacts
  - *From: VRGameDevGirl84(RTX 5090)*

- **Problem:** Resolution error with T2V
  - **Solution:** Bump resolution from 384x640 to 392x648, and make sure using T2V model not I2V model
  - *From: jeffcookio*

- **Problem:** Uni3C not working with VACE
  - **Solution:** Uni3C only works with I2V, not with VACE workflows
  - *From: DawnII*

- **Problem:** Camera movement in VACE when unwanted
  - **Solution:** Use spline editor to lock motion by keeping spline static on background, or use FUN control
  - *From: DawnII*

- **Problem:** Wan 2.2 adding random body parts frequently
  - **Solution:** Remove negative prompts, add 'human' and 'body' to negatives if needed
  - *From: SonidosEnArmonía*

- **Problem:** Trash output with control LoRAs after update
  - **Solution:** Reduce denoise value when switching from old to new WanVideoSampler node
  - *From: N0NSens*

- **Problem:** VACE color changes between different scenes
  - **Solution:** Color matching can help slightly but gets worse with very different scenes
  - *From: yukass*

- **Problem:** InfiniteTalk cutting video length shorter than audio
  - **Solution:** Unknown - user reported 1:09 audio only generating 45 seconds
  - *From: amli*

- **Problem:** Wan 2.2 I2V producing poor quality results in native
  - **Solution:** Use wrapper version instead, or ensure no shortcuts, no LoRAs on high noise model, and use full CFG
  - *From: N0NSens and MysteryShack*

- **Problem:** VRAM issues with upscaling workflow on RTX 5090
  - **Solution:** Try Q8 quantized models instead of FP16, or use quantization on both nodes
  - *From: Gill Bastar*

- **Problem:** Context windows work poorly with I2V
  - **Solution:** I2V works poorly with context windows, MAGREF can work but technique cannot work with regular I2V
  - *From: Kijai*

- **Problem:** First-to-last frame generation coming out noisy
  - **Solution:** Connect first sampler output to second sampler properly
  - *From: Abx*

- **Problem:** Disk space not clearing after block swap
  - **Solution:** Need to do hard restart to clear disk space
  - *From: xwsswww*

- **Problem:** RAM usage issues resolved
  - **Solution:** New pytorch update helps with RAM usage - setting memory allocator to 0 makes it give memory back to OS more aggressively
  - *From: comfy and Ablejones*

- **Problem:** Error 'int' object has no attribute 'clone' in WanVideoEncode
  - **Solution:** Something is wrong with the image input into your WanVideoEncode node, probably the one with the ref video. Double check to make sure that the image input is getting a real image batch
  - *From: Ablejones*

- **Problem:** Shape error with T2V 2.2 + InfiniteTalk
  - **Solution:** Error during model prediction: shape '[21, 32, 2, 40, 128]' is invalid for input of size 13434880
  - *From: NebSH*

- **Problem:** VHS nodes progress bar keeps going after workflow completion
  - **Solution:** Bug where while workflow is done based by console output, the VHS nodes progress bar keeps going for a lot longer time before you get the output visible. Fixed by updating front end version
  - *From: Kijai*

- **Problem:** Beyond 45 frames getting blurred smoke results
  - **Solution:** Max 81 is stable if you dont use any extension methods. Beyond that may not have enough memory for longer frames
  - *From: Mu5hr00m_oO*

- **Problem:** Recent OOM issues with wrapper
  - **Solution:** Need to increase blockswaps from 20 to 26 for 480x720 resolution
  - *From: .: Not Really Human :.*

- **Problem:** Sudden OOM on second generation filling 96GB VRAM
  - **Solution:** Issue persists even with older commits, suggesting recent changes causing memory leaks
  - *From: HeadOfOliver*


## Model Comparisons

- **SDXL vs Flux vs Wan**
  - SDXL still top for artistic creation, especially with IPAdapterV2 for style control. Flux useful for editing/cleaning SDXL pictures but disliked overall. Wan great for generation but impossible to control light colors
  - *From: GOD_IS_A_LIE*

- **Wan 2.2 vs Veo 3**
  - If Wan 2.2 could do 24fps and longer generations consistently, it would be better than Veo 3. Veo has better content control and timestamping, Wan has better camera control
  - *From: Ruairi Robinson*

- **WAN 2.2 vs closed models**
  - 2.2 has best quality but +15 min runs still not worth it compared to closed models
  - *From: Drommer-Kille*

- **T2V vs I2V workflow preference**
  - T2V more dynamic/realistic, I2V requires extensive seed hunting but gives more control
  - *From: seitanism*

- **RadialAttention vs SageAttention**
  - Radial is faster but requires quality tweaking, sage more stable
  - *From: Kijai*

- **SageAttention3 quality**
  - Early access shows terrible quality, can be mitigated by using on certain steps/blocks only
  - *From: Kijai*

- **WAN 2.2 vs VEO3 I2V quality**
  - Very similar quality, both 1280x720x24fps. WAN 2.2 is on correct path to match VEO3. VEO3 better at prompt adherence, WAN better at avoiding leaf noise
  - *From: Juan Gea*

- **Native vs Kijai wrapper performance**
  - Wrapper much faster - 400 seconds vs 20+ minutes for same 1536x768x81 frames on RTX 5090
  - *From: IceAero*

- **WAN 2.1 vs 2.2 for LoRAs**
  - Can use 2.1 LoRAs on 2.2 14B for NSFW. I2V works great with LoRAs, T2V not as much
  - *From: crinklypaper*

- **DDIM vs DPMPP_SDE samplers**
  - DDIM runtime 12m vs DPMPP_SDE 21m - DDIM is twice as fast
  - *From: The Shadow (NYC)*

- **5B vs 14B motion quality**
  - 14B motion is far superior to 5B, though 5B image quality is great
  - *From: Kijai*

- **Q3 GGUF vs FP8 results**
  - Q3 was giving better results than fp8, possibly due to lora not being active on fp8
  - *From: hicho*

- **5090 vs 4090 performance**
  - 5090 is ~30-40% faster than 4090, about 3x faster than 4080
  - *From: Kijai*

- **Native vs Wrapper with LightX performance**
  - Native: 30 mins for 5 seconds. Wrapper with LightX: 2-3 mins for 5 seconds
  - *From: AJO*

- **Wan 2.2 vs FusionX quality**
  - Wan 2.2 shows better prompt adherence and camera movement
  - *From: VRGameDevGirl84(RTX 5090)*

- **LightX vs no LoRA on Wan 2.2**
  - No LoRA shows better hair details and galloping movement, but LightX is much faster (146s vs 431s)
  - *From: VRGameDevGirl84(RTX 5090)*

- **I2V distill vs other approaches**
  - I2V distill described as 'the best'
  - *From: hicho*

- **0-2-10 vs 5B upscale**
  - 0-2-10 has better detail than 5B upscale
  - *From: shockgun*

- **VACE 2.1 vs 2.2 compatibility**
  - VACE works fine on low noise model, terrible on high noise model
  - *From: Kijai*

- **FP8/FP16 vs GGUF quantized models**
  - Only FP8 or FP16 models work well, Q models don't work good
  - *From: avataraim*

- **Pyramid vs Linear fuse method for context windows**
  - Pyramid almost always better - smoother blend, less ghosting artifacts
  - *From: thaakeno*

- **14B model vs 5B model for upscaling**
  - 14B better for upscaling with LoRAs, 5B purpose may be just basic upscaling
  - *From: thaakeno*

- **High overlap (48) vs lower overlap (16) for context windows**
  - 48 overlap takes much longer, 16 overlap with 4 stride is good balance
  - *From: thaakeno*

- **Different CFG values for prompt adherence**
  - Sometimes lower CFG (1.5) works when higher CFG (3.5) fails
  - *From: Juampab12*

- **Wan 2.1 vs 2.2 for FLF support**
  - 2.2 supports FLF natively while 2.1 does not
  - *From: Juampab12*

- **SeedVR2 quality vs expectations**
  - Results look oversharpened and don't match original samples closely
  - *From: gokuvonlange*

- **Fun models vs VACE**
  - Can mostly forget about Fun models now that VACE exists, though there are fringe use cases
  - *From: Kijai*

- **Wan 2.2 vs 2.1 physics**
  - Physics are much better with 2.2 14B
  - *From: Fill*

- **Native vs Wrapper performance**
  - Native prevents RAM maxing during encoder caching, wrapper sometimes maxes RAM
  - *From: Fill*

- **Sage vs Flash attention**
  - Minimal quality difference, massive speed advantage for Sage
  - *From: Kijai*

- **5B vs 14B models**
  - 5B is faster but generally pretty garbage quality compared to 14B
  - *From: Screeb*

- **Topaz vs other upscalers**
  - Topaz is better for upscaling if video has enough detail
  - *From: Dan*

- **3090 to 4090 performance**
  - 4090 is roughly double the speed of 3090
  - *From: screwfunk*

- **2.2 vs 2.1 artifacts**
  - 2.2 eliminates the 'wanny motion' and strange artifacts present in 2.1
  - *From: Draken*

- **Precision quality ranking**
  - fp32 > bf16 > fp16 > fp8 E5 ≈ fp8 E4, with bf16 showing most details in practice
  - *From: Juan Gea*

- **ComfyUI scaled models vs GGUF models**
  - Official ComfyUI scaled models have very bad quality compared to bullerwins GGUF models
  - *From: Дмитрий Марков*

- **Original Alibaba code vs ComfyUI**
  - Original code produces less noise artifacts and higher quality, but much slower
  - *From: aikitoria*

- **FlashAttention vs SageAttention**
  - Quality difference exists between flash and sage, but not between flash and sdpa
  - *From: Kijai*

- **FP8 vs BF16 quantization**
  - Differences are minimal, sometimes FP8 performs better in specific motion scenarios
  - *From: Kijai*

- **Wan 2.2 vs 2.1 with lightx**
  - 2.2 with lightx slightly better than 2.1, worth upgrading
  - *From: Karo*

- **Text vs JSON prompt formatting**
  - Text-based prompts perform much better than JSON format, though JSON is mostly understood
  - *From: mamad8*

- **bf16 vs fp8 for ice cream generation**
  - bf16 keeps ice cream consistent, better lighting, doesn't burn out easily, looks more like real animal vs guy in costume
  - *From: HeadOfOliver*

- **h1111 vs wangp for speed**
  - wangp is faster than h1111
  - *From: hicho*

- **2.1 + VACE vs Wan 2.2 FLF2V**
  - 2.1 + VACE much better than Wan 2.2 FLF2V
  - *From: Kijai*

- **Wan 2.2 vs Flux Krea for detailed face generation**
  - Wan 2.2 shows superior detail quality, especially for close-up faces
  - *From: VRGameDevGirl84(RTX 5090)*

- **I2V with good image model vs T2V**
  - I2V with a really good image model input is probably better than any T2V could ever be
  - *From: Draken*

- **Wan 2.2 motion vs 2.1**
  - 2.2 feels like 30fps downsampled to 16fps instead of raw 16fps, much more realistic motion
  - *From: Draken*

- **With vs without LightX2V LoRA**
  - Without LightX gives vastly more realistic motion, with LightX makes output more like 2.1
  - *From: Draken*

- **Beta vs simple scheduler at shift 12**
  - Beta scheduler produces better results due to more gradual dropoff
  - *From: Ablejones*

- **Wan 2.2 5B vs 14B High Noise motion quality**
  - 5B has good image quality but motion doesn't come close to high noise capabilities
  - *From: Kijai*

- **Wan 2.2 vs 2.1 VACE requirements**
  - 2.2 needs better masks and more accurate prompts than 2.1. Used to work with controlnet + mask + short prompt, now needs more accurate prompting
  - *From: JalenBrunson*

- **5B vs 14B popularity and LoRA availability**
  - 14B more popular having part of old LoRA etc working for it. No LoRAs seen for 5B since release
  - *From: QANICS🕐*

- **New vs Old LightX LoRAs**
  - Old LightX looks better for some use cases, new is faster because it works on both passes
  - *From: VRGameDevGirl84*

- **Official repo LoRA vs Kijai fixed LoRA**
  - Kijai's version works better at proper strength, gets hands right compared to original
  - *From: RRR*

- **Wan 2.2 vs 2.1 dynamic range**
  - 2.2 Lightning has significantly reduced dynamic range compared to 2.1
  - *From: wange1002*

- **New Lightning 2.2 vs Old LightX2V 2.1 LoRAs**
  - Old 2.1 LoRA has better prompt adherence and motion on high noise pass
  - *From: Doctor Shotgun*

- **14B Lightning vs 5B model quality**
  - Both produce similar results, 5B model appears to handle prompts differently
  - *From: TK_999*

- **Lightning 4 steps vs LightX2V 3.0/1.0 strength**
  - LightX2V still produces better overall quality
  - *From: Kijai*

- **Wan 2.2 vs FusionX**
  - Results comparable for similar prompts
  - *From: VRGameDevGirl84(RTX 5090)*

- **Lightning LoRA vs original LightX2V**
  - Original LightX2V v1 performs better than new Lightning LoRA, especially for complex camera movements
  - *From: Luis Clement*

- **CFG 1 vs CFG 5 with Lightning LoRA**
  - CFG=1 is 30% faster but details lacking compared to CFG=5
  - *From: The Shadow (NYC)*

- **2 steps CFG 1 vs 10 steps CFG 3.5**
  - 2 steps on CFG 1 definitely better than 10 steps on CFG 3.5
  - *From: gokuvonlange*

- **Wan 2.2 vs 2.1 motion quality**
  - Wan 2.2 has more realistic movement, timing of each move is less visible, better micro motions/subsecond motion
  - *From: loopen44*

- **New lightning lora vs old lightx2v lora**
  - Old one is better for I2V, new one works but degrades motion and quality
  - *From: N0NSens*

- **Wan 2.2 vs Wan 2.1**
  - 2.2 has more knowledge, increased training dataset, does stuff 2.1 doesn't. Better prompt adherence and mostly uncensored
  - *From: Lodis*

- **Wan vs LTXV**
  - LTXV is fast but generations are terrible compared to Wan
  - *From: Lodis*

- **5B model visual look**
  - Reminds of HY mixed with Wan, has that cellophane look like LTX
  - *From: Draken*

- **5B vs 14B models**
  - 5B is fast but doesn't have the knowledge that 14b has, reminds me of 2.1. Anything other than a human gets turned into a human
  - *From: Rainsmellsnice*

- **LightX2V vs Lightning loras**
  - LightX2V gives better, more predictable cinematic results despite taking more steps
  - *From: screwfunk*

- **FastWan vs regular models**
  - FastWan is faster and much worse quality, not worth it
  - *From: Kijai*

- **Wan 2.2 Plus (website) vs open models**
  - Wan 2.2 Plus on their site is infinitely superior and does 1080p without grid stepping artifacts
  - *From: aikitoria*

- **Wan 2.2 FLF vs other FLF models**
  - Wan 2.2 FLF is superior - better than Kling and other closed source models for FLF morphing
  - *From: thaakeno*

- **Lightning LoRA vs lightx2v at 3.0 strength**
  - Lightning LoRA not much different from using lightx2v at 3.0 strength
  - *From: Kijai*

- **T2V vs I2V motion quality**
  - T2V can have more motion than I2V, T2V works fine with 2.2 but I2V needs specific LoRA stacking
  - *From: Ada*

- **Q8 vs fp8 quantization**
  - Q8 is better quality but slower than fp8
  - *From: Kijai*

- **Lightning 2.2 vs original Lightning**
  - Lightning 2.2 is not nearly as good as the previous distill LoRA
  - *From: Kijai*

- **Wan 5B vs 1.3B quality**
  - 5B has nearly 4x parameters but is worse in many ways compared to 1.3B, possibly due to VAE overwhelming the model
  - *From: Draken*

- **WAN VAE vs Qwen-Image VAE**
  - Virtually identical - 99.98% compatibility with negligible visual differences
  - *From: fredbliss*

- **WAN 2.2 I2V vs WAN 2.1 I2V at 1080p**
  - 2.2 works much better, 2.1 died into noise at borders
  - *From: aikitoria*

- **bf16 vs GGUF Q8 and fp8_scaled quality**
  - bf16 is overkill unless going for absolute maximum quality, Q8 and fp8_scaled are good enough
  - *From: Kijai*

- **Old LightX2V LoRAs vs new lightning LoRAs**
  - Old LightX2V LoRAs work better on NH with CFG3 for 3-5 steps without being too slow
  - *From: IceAero*

- **Qwen image vs Wan 2.2 T2I**
  - Qwen image has superior prompt following and text rendering
  - *From: aikitoria*

- **Old vs new LightX LoRAs**
  - Results vary by seed - sometimes old performs better, sometimes new. New LoRAs can mess up outputs for some users
  - *From: piscesbody*

- **Wan 2.1 vs 2.2 First-Last-Frame**
  - Wan 2.2 FLF shows improvement over 2.1 wrapper implementation
  - *From: VRGameDevGirl84*

- **Lightning vs LightX2V LoRAs**
  - Many users prefer old LightX2V for both high and low, new Lightning can make results worse
  - *From: screwfunk*

- **WAN 2.2 vs Kling Master hands**
  - WAN 2.2 does much better job with hands even at lower resolution
  - *From: Persoon*

- **5B vs 2.1 VAE memory usage**
  - 5B VAE is 4x heavier (1.4GB vs 480mb) with better quality
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Kijai's prompt splitting vs EchoShot**
  - Kijai's method works better and more reliably, EchoShot often fails to trigger
  - *From: Kijai*

- **2.2 speed LoRAs vs old LightX2V**
  - New 2.2 speed LoRAs are not better or even as good as the old LightX2V
  - *From: Kijai*

- **Shift 8 vs Shift 1 with different schedulers**
  - With DMP++_SDE scheduler, results look almost identical despite opposite curves. With UniPC, shift 1 and 8 also look nearly identical
  - *From: Nekodificador*

- **20 frame vs 60 frame VACE generations**
  - Wan2.1 VACE degrades heavily in quality for style transfer when going from 20 to 60 frames
  - *From: Poppi*

- **2.2 vs 2.1 quality**
  - 2.2 14B is better at basically everything except VACE according to tests
  - *From: Josiah*

- **5B vs 14B models**
  - 5B requires more effort to get good results, 14B produces better quality with minimal effort
  - *From: DawnII*

- **Lightning LoRA vs full steps**
  - Can work without Lightning LoRA but need CFG 5+ and 20+ steps, making Lightning faster overall
  - *From: N0NSens*

- **GIMM vs RIFE for frame interpolation**
  - GIMM slightly better than RIFE but slower. Both don't match Topaz quality
  - *From: Kijai*

- **FastWan vs LightXv2 for I2V**
  - FastWan not better or faster than LightXv2 for I2V, makes results overly high contrast
  - *From: mdkb*

- **FP8 vs GGUF memory usage**
  - GGUF saves more RAM (stays 32-40G vs fp8_scaled hitting 63-64G), but FP8 faster if you have memory
  - *From: : Not Really Human :.*

- **e5m2 vs e4m3 FP8 formats**
  - e4m3 is 0.5% better for Wan, but only 40xx+ cards support compiling e4m3. e5m2 needed for 30xx cards
  - *From: phazei*

- **LightX2V 2.1 vs 2.2 Lightning**
  - 2.1 version consistently outperforms 2.2 Lightning LoRA
  - *From: shuzhi*

- **fp16 vs bf16 vs fp32 VAE decode**
  - Difference between fp16/bf16 and fp32 is tiny and not visible to eye, fp32 not worth the VRAM cost
  - *From: Kijai*

- **Wan 2.2 with/without LoRAs for I2V**
  - Massive difference - no LoRA produces poor results, combining lightx2v and 2.2 lightning gives much better output
  - *From: FL13*

- **New Lightning LoRA vs old LightX2V**
  - Old LightX2V can do darker scenes, new Lightning forces brightness but has better prompt adherence
  - *From: IceAero*

- **T2V 1.1 vs T2V 1.0 LoRA**
  - 1.1 is stronger and follows prompts better but sometimes fails on complex tasks
  - *From: Kijai*

- **6 steps vs 4 steps with new Lightning**
  - 6 steps feels better, 4 steps needs custom sigmas or scheduler that doesn't drop off
  - *From: Kijai*

- **WAN 2.2 Lightning vs LightX2V 2.1**
  - Some users prefer sticking with 2.1, results vary by use case
  - *From: NebSH*

- **Lightning 1.1 vs old Lightning LoRAs**
  - Old LightX2V preferred - new ones only slightly better for movement but destroy lighting capabilities
  - *From: Critorio*

- **Lightning 2.2 vs LightX2V 2.1**
  - Older version has more motion, lightning kills motion even more
  - *From: Daflon*

- **fp16 vs fp8 models**
  - Difference is noticeable but not huge, fp16 requires more offloading but better quality
  - *From: Kijai*

- **bf16 vs fp16**
  - bf16 can have quite significant difference, closer to fp32 than fp16
  - *From: Kijai*

- **Lightning 2.2 vs LightX2V**
  - LightX2V generally produces better quality results, Lightning appears more 'cursed' than Wan 2.1 lightx2v
  - *From: MysteryShack*

- **Lightning I2V vs original 2.1 LoRA**
  - Original 2.1 LoRA produces better motion and prompt adherence for some users
  - *From: WorldX*

- **LoraLoaderModelOnly vs WanVideo Lora Select Multi**
  - Both work well with minimal differences
  - *From: The Dude*

- **Different Lightning versions**
  - Lightning 1.1 seems worse than the old 2.1 x2v version
  - *From: MysteryShack*

- **Native ComfyUI vs WanVideo Wrapper performance**
  - Native consistently 2 times faster than wrapper for same workflow
  - *From: pagan*

- **fp8_fast vs fp16 performance**
  - fp8_fast maybe 30% faster than fp16 and only ~10% faster than fp16_fast, but with quality hit
  - *From: Kijai*

- **Lightning LoRAs on 2.2 vs 2.1**
  - Loading lightning feels like loading a 2.1 wan lora - more strength makes it look more like 2.1
  - *From: Draken*

- **Native vs Wrapper speed**
  - Native is 2x faster (5s vs 10s on 5090)
  - *From: pagan*

- **WAN 2.2 distilled vs normal steps**
  - 4 steps CFG 1 distilled looks 200x better than 20 steps CFG 3.5
  - *From: Draken*

- **FP8 vs FP16 quality**
  - FP8 scaled changes output quality, was very bad in 2.1, seems better in 2.2 but still affects results
  - *From: Kijai*

- **I2V lightning vs T2V lightning**
  - I2V lightning gives really similar results to T2V lightning at boosted amounts, could be T2V lightning boosted by x2
  - *From: Draken*

- **Fun Control vs VACE control**
  - Fun has always been more lenient but not quite as good as UniAnimate
  - *From: DawnII*

- **2.2 Fun vs base model quality**
  - Quality is probably not as good as base model, same was true for 2.1 fun models
  - *From: DawnII*

- **bf16 vs fp16_fast**
  - bf16 not faster than fp16_fast, but they only released bf16 weights. With fp8 scaled it doesn't matter
  - *From: Kijai*

- **Wan2.2 lightning LoRAs vs LightX LoRAs**
  - Kijai's lightning LoRAs not well trained and have style bias, recommends sticking with LightX or using a mix
  - *From: Kijai*

- **Fun models vs original models**
  - Fun models consistently worse quality than originals across all releases - lack compute and dataset to match original
  - *From: aikitoria*

- **Veo3 vs other video generators**
  - Veo3 with audio still king but much more expensive. Seedance rates best in user voting. Performance varies by use case
  - *From: Draken*

- **Sapiens vs OpenPose/DWPose**
  - Sapiens is better but more complex, much better results for pose detection
  - *From: fredbliss*

- **WAN 2.2 PRO vs Open Source**
  - Local/OS version preferred - PRO looks like sepia and lens flare slapped in post process
  - *From: DawnII*

- **Fun 2.2 high + base low+unianimate vs other combinations**
  - Mixing fun high and base low+unianimate gives higher fidelity
  - *From: DawnII*

- **GGUF vs fp8 scaled Wan 2.2**
  - GGUF produces cleaner results, especially with LoRAs due to different application methods
  - *From: Draken*

- **Qwen Lightning vs Wan Lightning LoRAs**
  - Qwen Lightning doesn't ruin style like Wan version, looks almost exactly the same as full Qwen image
  - *From: Kijai*

- **PUSA vs VACE for extension**
  - PUSA has no color shifting like VACE, but VACE has advantages with control/ref. Killer combination would be using both together
  - *From: Hashu*

- **Wan 2.2 5B vs 14B performance**
  - 5B: 22 minutes for 1080x1920, significantly faster than 14B's 1 hour for comparable results
  - *From: QuintForms*

- **RIFE vs GIMM interpolation**
  - RIFE better for sword action, GIMM warps background more but creative interpolators become noisy when confused
  - *From: Kijai*

- **Lightning LoRA vs LightX2V LoRA**
  - New lightning LoRA gives more natural walking, LightX2V causes slipping feet and unwanted behaviors when used with Wan 2.2
  - *From: Alpha-Neo*

- **SeedVR2 GGUF vs regular versions**
  - GGUF versions produce blurry and weird results, regular versions work better
  - *From: Gill Bastar*

- **Topaz vs ComfyUI upscaling**
  - ComfyUI with 1.5x upscaler + RIFE interpolation claimed to be better than Topaz for speed, quality comparison inconclusive
  - *From: Alpha-Neo*

- **Wan 2.2 vs Grok Imagine**
  - Wan 2.2 is miles better than Grok Imagine, which is described as 'a joke' and '100x better'
  - *From: thaakeno*

- **Fun low noise vs base Wan 2.2 low noise**
  - Base Wan 2.2 has much better detail on low noise, Fun low doesn't finish properly
  - *From: DawnII*

- **DPM vs Euler sampler speed**
  - DPM is twice as slow as Euler per step
  - *From: Karo*

- **SeedVR2 preference**
  - Still prefer SeedVR2 the most despite infinite VRAM requirements
  - *From: Karo*

- **Wan 2.1 vs 2.2 Lightning LoRA quality**
  - 2.1 lightx2v is amazing, 2.2 Lightning has something very wrong - too much style bias
  - *From: Kijai*

- **5B vs 14B model capabilities**
  - 5B can do 1080p but 14B can't, 5B gives solid video in 40 seconds on 3090
  - *From: QuintForms*

- **Skyreels vs base Wan**
  - Skyreels offers better human motion and portraits, 24fps vs 16fps
  - *From: DawnII*

- **FastWan vs LightX2V for speed**
  - FastWan may be better than lightx2v for some cases
  - *From: Kiwv*

- **cfg 1.0 vs higher cfg**
  - cfg other than 1.0 is slower because model runs twice per step
  - *From: Kijai*

- **Block swap speed impact varies by system**
  - Minimal impact on high-end systems (~0.1s per block) but significant impact on lower-end systems
  - *From: Kijai*

- **2.1 + 2.2 merges vs pure 2.2**
  - These merges are more 2.1 than 2.2, wouldn't even call them 2.2
  - *From: Kijai*

- **GGUF vs fp8 on 24GB VRAM**
  - No real reason to use GGUF other than Q8 on 24GB VRAM/64GB RAM, fp8_scaled preferred for speed
  - *From: Kijai*

- **FP8 vs GGUF inference speed**
  - FP8 has faster inference than GGUF
  - *From: Juampab12*

- **480p vs 720p I2V models for coherence**
  - 480p i2vs (including Sky Reels) were better with coherence than 720p models
  - *From: JohnDopamine*

- **GGUF Q6 vs FP8**
  - FP8 would be faster than Q6 and better quality even with slight offloading
  - *From: Kijai*

- **GGUF vs standard models**
  - GGUF about 20% slower due to dequant operation, but allows larger models to fit in memory
  - *From: Kijai*

- **T2V vs I2V quality with Lightning LoRA**
  - The difference of quality between T2V and I2V both having light lora is miles apart
  - *From: Hevi*

- **Fun Control vs VACE**
  - Fun control superior for getting correct control but inferior in quality. Underrated once VACE came out
  - *From: Hashu*

- **Wan 2.1 vs 2.2 for V2V**
  - Still use Wan 2.1 V2V workflow because 2.2 doesn't compare as of yet
  - *From: Josiah*

- **GGUF vs native ComfyUI for 4070ti super**
  - Native ComfyUI workflow faster than GGUF, but needs 64GB RAM
  - *From: pewpewpew*

- **Stand-In vs Phantom**
  - Similar to Phantom but just 300MB LoRA instead of full model
  - *From: Kijai*

- **Wan 2.1 vs 2.2 for emotions**
  - Wan 2.1 emotions were always uncanny and something was off, 2.2 provides better facial expressions
  - *From: gokuvonlange*

- **Native vs Wrapper for Wan 2.2**
  - Wrapper runs much better with low VRAM/RAM, saves 3GB VRAM and several GB RAM, faster generations
  - *From: Jonathan*

- **Lightning vs LightX2V LoRAs**
  - Lightning pushes things into stylized results more often than LightX2V
  - *From: garbus*

- **Q8 vs fp16 quality**
  - Q8 is very close to fp16 with much better efficiency, differences are minimal
  - *From: Kijai*

- **Multitalk vs FantasyTalk**
  - Multitalk is better, FantasyTalk came out before multitalk and was quickly forgotten
  - *From: DawnII*

- **Wan 2.1 vs 2.2 for stable subjects**
  - If subject stays in frame without dynamic movement, 2.2 doesn't offer much over 2.1
  - *From: Kijai*

- **fp8 scaled vs Q8**
  - fp8 scaled is preferred because it's very close quality and much faster
  - *From: Kijai*

- **LightX2V vs CausVid v2**
  - LightX2V is superior to CausVid v2 in most cases, CausVid can be forgotten about except for edge cases
  - *From: Kijai*

- **Wan 2.2 HN vs LN for motion**
  - High Noise model better for motion, Low Noise better for controls and detail refinement
  - *From: Ablejones*

- **I2V vs T2V for face likeness**
  - Much easier time keeping likeness with i2v in 2.2 than 2.1, but distills will skew results
  - *From: DawnII*

- **StandIn vs VACE reference for likeness**
  - VACE reference works better than StandIn for identity preservation
  - *From: hablaba*

- **Multitalk with Wan 2.1 t2v VACE vs i2v with Phantom for speed**
  - Wan 2.1 t2v with VACE much faster - 10 mins vs 40 mins for similar quality
  - *From: mdkb*

- **Lightning vs LightX2V LoRAs**
  - Lightning is for Wan 2.2, LightX2V is for Wan 2.1. Lightning is faster but may have lower quality
  - *From: Kagi*

- **New Wan22-Lightning LoRAs vs LightX2V**
  - New Lightning LoRAs are fast but not as good quality as LightX2V
  - *From: xwsswww*

- **Fun 2.2 vs VACE 2.1 for v2v**
  - Fun 2.2 works better than VACE 2.1, first v2v that properly places objects like skateboard trucks
  - *From: Drommer-Kille*

- **MAGREF vs Phantom**
  - MAGREF is better for character subject consistency, works as reference-to-video instead of start-frame-to-video
  - *From: gokuvonlange*

- **fp8 vs GGUF Q8**
  - Q8 has better quality but fp8 with fast mode is 30-40% faster on 4090/5090, and allows LoRA merging
  - *From: Kijai*

- **720p vs 1080p generation time**
  - 720p takes 85s, 1080p takes 15 minutes - 4x resolution but 10x longer time due to RAM spillover
  - *From: Drommer-Kille*

- **Stand-in MultiTalk vs regular MultiTalk**
  - Not quite as good lipsync quality as regular MultiTalk
  - *From: Kijai*

- **Wan 2.1 vs 2.2 character rotation**
  - 2.1 causes body parts to mix during rotation like nightmare, 2.2 fixes this with normal rotation
  - *From: Lodis*

- **Wan 2.2 Lightning LoRAs vs LightXV 2.1 LoRAs**
  - 2.2 Lightning faster with 4 steps but destroys motion quality, 2.1 LightXV better motion
  - *From: Lodis*

- **Stand-in vs Phantom for subject consistency**
  - Phantom is better overall but Stand-in has benefit of being LoRA for other workflows
  - *From: Juampab12*

- **Phantom vs MagRef capabilities**
  - Phantom can do pixel perfect character replacement including clothing, MagRef better for I2V likeness
  - *From: Piblarg*

- **MultiTalk compatibility**
  - Works well with Wan 2.1, not as well with 2.2, would need model release from devs for 2.2
  - *From: Kijai*

- **Wan 2.1 14B vs 2.2 speed**
  - 14B 2.1 is much faster than 2.2
  - *From: Drommer-Kille*

- **VACE 2.1 vs 2.2**
  - VACE 2.1 is better even than 2.2
  - *From: Kijai*

- **Fun 2.1 vs Fun 2.2**
  - Fun 2.2 seems lot better than 2.1 Fun
  - *From: Kijai*

- **Reference image vs start image in trajectory control**
  - Start image works, reference image doesn't work for trajectory control
  - *From: Kijai*

- **Different LightX2V ranks**
  - Rank 128 gives better prompt adherence than rank 256, rank 16 worked best for specific scenes
  - *From: xwsswww*

- **Q6 vs Q8 gguf quantization**
  - Q8 seems to prompt faster than Q6
  - *From: xwsswww*

- **Using distill model directly vs LoRAs**
  - Running original distill model directly is stronger than using extracted LoRAs
  - *From: Kijai*

- **Lightning LoRA vs LightX2V for Wan 2.2**
  - The team says Lightning is worse than using the old LightX2V
  - *From: Juan Gea*

- **FP8 vs BF16 text encoder**
  - BF16 is better, not much reason to not use it since text encoder is unloaded anyway
  - *From: Kijai*

- **Compiled vs uncompiled memory usage**
  - Compiled evens out VRAM peaks significantly, uncompiled shows mountain-like RoPE peaks
  - *From: Kijai*

- **Wrapper vs Native block swapping**
  - Native ComfyUI has super granular automatic offloading that's superior to manual block swap
  - *From: Kijai*

- **Wan 2.2 vs Kling speed**
  - Wan 2.2: 10s video in 196s, faster than Kling
  - *From: Drommer-Kille*

- **Wan 2.2 Fun-InP vs base model**
  - Fun-InP has smooth transitions but loses creativity, feels more like interpolation. Base model better except for transition smoothness
  - *From: dir2050*

- **Phantom vs MagRef for likeness**
  - Sometimes MagRef nails it better (five guys holding beers), but recent tests show Phantom better for likeness
  - *From: mdkb*

- **Lightning lora vs lightx2v for NSFW content**
  - Lightning lora censors and generates blocking objects, lightx2v maintains capability
  - *From: MysteryShack*

- **Lightning lora vs base generation quality**
  - Lightning ruins generations with more static scenes and altered coloring
  - *From: crinklypaper*

- **Context options Wan 2.2 vs AnimateDiff**
  - AnimateDiff was much smoother for context transitions, Wan 2.2 restarts from first frame
  - *From: xwsswww*

- **WanFM vs normal Wan 2.2 FFLF**
  - WanFM won in one test case but benefit unclear since 2.2 already does similar processing internally
  - *From: Kijai*

- **fp16 on-the-fly quantization vs pre-quantized models**
  - fp16 with on-the-fly quant has fewer issues overall, downside is larger storage space
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Latent extraction vs decode/encode for video extension**
  - 
  - *From: Kijai*

- **WanWrapper vs Native workflows on RTX 3060**
  - WanWrapper ksampler runs much slower compared to native workflow
  - *From: Abx*

- **MultiTalk vs expected sonic-level quality**
  - MultiTalk still kinda sucks compared to expected quality levels
  - *From: MysteryShack*

- **Phantom vs MagRef for character consistency**
  - Phantom is t2v ref image consistent and pretty good, MagRef is i2v equivalent but never quite tops Phantom
  - *From: mdkb*

- **FantasyPortrait vs MultiTalk for lip-sync**
  - FantasyPortrait not great at lipsync but good at transferring head pose and emotion, MultiTalk better for lipsync
  - *From: Kijai*

- **VACE vs Redux for inpainting**
  - VACE works better than Redux
  - *From: Nekodificador*

- **WAN 2.2 vs 2.1 speed perception**
  - 2.2 outputs often seem sped up compared to 2.1 at same fps
  - *From: Fawks*

- **T2V + Phantom vs I2V for dynamics**
  - Much more dynamic with Phantom vs I2V, but lipsync not as good
  - *From: Kijai*

- **Wrapper vs Native for VACE single image**
  - Only works with wrapper, native has problems
  - *From: Nekodificador*

- **GGUF vs FP8 scaled versions**
  - FP8 scaled is faster, GGUF is smaller for VRAM but slower due to decompression overhead
  - *From: . Not Really Human .*

- **RTX 5090 vs RTX 6000 Pro**
  - Pro 6000 much faster when models fit in VRAM (300% speed boost), 5090 only 20% slower when using block swap properly
  - *From: WorldX*

- **FP32 vs FP16 vs BF16 text encoders**
  - Mixed weights FP32&FP16 best for intricate details, BF16 close behind
  - *From: Benjimon*

- **Wan 2.1 vs 2.2 for Fantasy Portrait**
  - User prefers 2.1 over 2.2 for Fantasy Portrait
  - *From: VRGameDevGirl84(RTX 5090)*

- **Mixed weights model vs other variants**
  - Best results achieved with mixed weights model from maybleMyers
  - *From: Benjimon*

- **fp8 e5m2 vs fp8 e4m3fn for 30xx cards**
  - fp8 e5m2 works with 30xx cards, fp8 e4m3fn doesn't work with 30xx cards, need 40xx or above
  - *From: mdkb*

- **MAGREF vs standard I2V models**
  - MAGREF is reference model not first frame model, works much better with context windows
  - *From: Kijai*

- **GGUF Q8 vs FP8 speed**
  - FP8 faster even without fp8 matmul, but GGUF sometimes appears faster in wrapper due to memory issues
  - *From: Kijai*

- **GGUF Q8 vs FP8 quality**
  - Q8 way better quality than plain fp8, slightly better than fp8 scaled
  - *From: Kijai*

- **GGUF Q8 vs FP8 VRAM usage**
  - Q8 uses more VRAM than fp8 - T2V ~14GB fp8 vs 15.5GB Q8
  - *From: Kijai*

- **LightX 1.1 vs other versions for I2V**
  - Better hands with lighting 1.1 on specific LoRA
  - *From: Kenk*

- **UniAnimate vs MTV Crafter weights**
  - UniAnimate is just better, especially when used with MAGREF
  - *From: Kijai*

- **FantasyPortrait + Multitalk vs other lipsync**
  - Best lipsync combination currently, brings quality from '1920s silent movie period to 1960s bad acting period'
  - *From: mdkb*

- **Dev branch vs main branch performance**
  - Dev branch showing slower performance for some AMD/ZLUDA users, opposite of expected improvements
  - *From: patientx*

- **Depth control vs straight input video**
  - Straight input video as control can work just as well as depth preprocessing
  - *From: VRGameDevGirl84(RTX 5090)*

- **MultiTalk vs InfiniteTalk**
  - InfiniteTalk allows much longer videos (1000 vs 250 frames) and better results
  - *From: NC17z*

- **Chinese AI models vs American companies**
  - China is winning with free open source video models while American companies lag behind
  - *From: Lodis*

- **Wan 2.1 vs AnimateDiff**
  - Some users get very bad results with Wan 2.1 and prefer going back to AnimateDiff
  - *From: xwsswww*

- **InfiniteTalk vs MultiTalk degradation**
  - InfiniteTalk doesn't degrade over long generations, MultiTalk becomes mushy mess after ~15 seconds
  - *From: Kijai*

- **Qwen Image Edit vs Kontext**
  - Initial tests show Qwen makes things plastic looking, needs experimentation
  - *From: Lodis*

- **F5-TTS language support**
  - Only handles 2 languages well, French doesn't work, has catastrophic forgetting issue
  - *From: MysteryShack*

- **MagRef vs Phantom for identity**
  - MagRef works better for identity preservation than Phantom with VACE
  - *From: mdkb*

- **Uni3C vs v2v with denoise**
  - Uni3C less controlled than v2v with 0.65 denoise, ~25% success rate
  - *From: Dream Making*

- **DMP SDE vs Res Multistep schedulers**
  - DMP SDE shows less noise in previews, Res Multistep creates very noisy previews but good final output
  - *From: Kijai*

- **FP8 vs GGUF Q8 quality**
  - FP8 produces significantly worse quality than GGUF Q8, no speed difference on 3090
  - *From: iShootGood*

- **MAGREF with vs without clip embeds**
  - Without clip embeds provides stronger reference, with clip embeds more stable
  - *From: Kijai*

- **Q8 vs fp8 on RTX 3090**
  - Q8 is better choice for 3090, especially with compile - better quality than e5m2
  - *From: Kijai*

- **InfiniteTalk vs MultiTalk**
  - MultiTalk has more even transitions when using same context windows and overlap
  - *From: DawnII*

- **e5m2 vs e4m3fn quantization**
  - e4m3fn is better quality, e5m2 not worth the quality loss except for 3000 series with torch.compile
  - *From: Kijai*

- **FantasyTalk vs MultiTalk vs InfiniteTalk**
  - FantasyTalk was redundant when MultiTalk released, InfiniteTalk is like MultiTalk but better. FantasyPortrait is still relevant as it's not audio driven
  - *From: Kijai*

- **With vs without LightX2V LoRA**
  - Without LightX2V it's very slow but much better quality - 1min 30sec clip takes about 5 hours
  - *From: seitanism*

- **InfiniteTalk vs MultiTalk for V2V**
  - InfiniteTalk seems better, MultiTalk couldn't do the same V2V results
  - *From: Draken*

- **Motion frame 9 vs 25**
  - 9 works fine and is faster (15:35 vs 20:33 execution time), 9 is default for new model while 25 was default for multitalk
  - *From: Kijai*

- **ComfyUI vs full 9GB InfiniteTalk**
  - Using ComfyUI version changes face drastically compared to full version
  - *From: MysteryShack*

- **Single vs Multi talk models**
  - Single changes faces, Multi doesn't change faces as much
  - *From: MysteryShack*

- **With vs without LightX2V LoRA**
  - With LightX2V LoRA you get very static faces, without LoRA and more steps more movement happens
  - *From: seitanism*

- **High CFG vs Low CFG on Wan 2.2**
  - Lower CFG produces less dynamic but cleaner results, high CFG causes wonkiness
  - *From: NC17z*

- **Original vs upscaled video quality**
  - Upscaling tidies up artifacts but removes expression and emotion, making it look bland and plastic
  - *From: seitanism*

- **Fantasy Portrait vs Fantasy Talk**
  - Fantasy Portrait captures more emotion than Fantasy Talk
  - *From: ManglerFTW*

- **Image upscaling vs latent upscaling**
  - Image upscaling works better according to Kijai
  - *From: daking999*

- **Qwen Edit vs Kontext**
  - Qwen has better prompt adherence but worse image quality. Qwen easily loses details that Kontext preserves
  - *From: blake37 and Drommer-Kille*

- **InfiniteTalk vs MultiTalk generation speed**
  - InfiniteTalk takes significantly longer to generate than MultiTalk
  - *From: T2 (RTX6000Pro)*

- **FusionX performance with InfiniteTalk**
  - FusionX is not faster in any way with InfiniteTalk
  - *From: NC17z*

- **MultiTalk vs InfiniteTalk**
  - MultiTalk doesn't do much for animating anything other than head, mouth and some body movements. InfiniteTalk does better job moving camera and other things, but produces more questionable output.
  - *From: T2 (RTX6000Pro)*

- **InfiniteTalk vs MultiTalk for long videos**
  - InfiniteTalk is amazing for stability even after 1 minute with no degradation, never worked as well with other methods for 1-3 minute generations. Unclear if this is mainly because of MagRef or InfiniteTalk or both together.
  - *From: seitanism*

- **Light2XV vs new 1.1 speed LoRAs**
  - Light2XV from Wan 2.1 performs better on Wan 2.2
  - *From: NebSH*

- **GGUF Q8 vs FP8 scaled**
  - Q8 better quality, FP8 has benefit of fp8 matmuls on supporting hardware
  - *From: Kijai*

- **InfiniteTalk vs MultiTalk for long videos**
  - InfiniteTalk keeps quality better even with super long videos, more stable
  - *From: Juan Gea*

- **Wan 2.1 vs 2.2**
  - 2.2 is better, faster, allows more control with less effort overall, more prompt work though
  - *From: Josiah*

- **GGUF scaled_fast vs Q8 quant mode**
  - scaled_fast is a lot faster than Q8, otherwise really close, GGUF never allows merging LoRAs
  - *From: Kijai*

- **Start step 5/7 vs 2/4**
  - Higher steps (5/7) cause stutter repeat mode, 2/4 steps work better, needs high enough sigmas
  - *From: Kijai*

- **VACE alone vs VACE + other methods**
  - VACE alone can be very effective for inpainting existing subjects, better than expected
  - *From: Dream Making*

- **Fake VACE 2.2 models vs WAN 2.2 T2V with 2.1 VACE**
  - Fake VACE 2.2 models work even worse than using WAN 2.2 T2V models with 2.1 VACE module
  - *From: seitanism*

- **InfiniteTalk extension vs VACE extension**
  - VACE extension is smoother than InfiniteTalk, but InfiniteTalk preserves given frames better
  - *From: DawnII*

- **T2V vs I2V for pull-focus and camera pans**
  - T2V often better than I2V because proper pull-focus is hard with starting image and pan to right person impossible with I2V
  - *From: Drommer-Kille*

- **Control splines vs OpenPose**
  - Control splines provide more information - openpose limited to pose only while splines handle camera movement and other objects
  - *From: Blink*

- **Infinitetalk on different models**
  - Can't use infinitetalk on high model effectively, gets good prompt adherence but quality suffers, need to vid2vid with wan2.1
  - *From: MysteryShack*

- **Wan VACE vs Qwen Edit**
  - Visual comparison shared showing different results
  - *From: N0NSens*

- **Wan 2.2 vs 2.1 for complex shots**
  - 2.2 can handle shots that 2.1 typically fails at
  - *From: Drommer-Kille*

- **AnimateDiff vs Wan frame counts**
  - AnimateDiff was 16 frames, Wan variants use 81-121 frames causing longer render times
  - *From: xwsswww*

- **LTXV vs Wan quality**
  - LTXV with lora was very good, much higher temporal compression than Wan, about 100x faster but Wan still has better overall quality
  - *From: NebSH*

- **Full Turbo model vs adaptive rank lora vs rank 64 lora**
  - No huge differences between them, adaptive pretty close to full model, rank 64 is fine too
  - *From: Kijai*

- **GGUF Q8 vs fp8 speed**
  - GGUF Q8 is almost as fast as fp8 and better quality, fp8 is way faster on 4000+ series than Q8
  - *From: Kijai*

- **Native VAE vs Wan VAE decode speed**
  - Native VAE is slightly faster
  - *From: Kijai*

- **Fun InP vs I2V FLF**
  - I2V FLF is better even with no prompt, Fun InP is like a simple transition
  - *From: hicho*

- **Wan VAE vs Qwen VAE for 4K generation**
  - Qwen VAE produces more natural results with better small patch alignment
  - *From: Instability01*

- **Context windows T2V vs I2V extension**
  - Better to extend I2V from last frame than using context windows - context is slower and lower quality
  - *From: Kenk*

- **20 steps vs LightX + 6 steps quality**
  - Quality with 20 steps is still worse than with LightX and 6 steps, adds noise and artifacts
  - *From: Drommer-Kille*

- **InfiniteTalk vs MultiTalk speed**
  - InfiniteTalk is not slower than MultiTalk, MultiTalk is mostly redundant now
  - *From: Kijai*

- **Lightning LoRA vs LightX2V**
  - Lightning LoRA makes everything brighter and more saturated, prefer LightX2V
  - *From: Kijai*

- **Full Turbo model vs normal model + LoRA**
  - LoRA is fine, full model is slightly stronger
  - *From: Kijai*

- **Wan 2.2 vs 2.1 for lip sync**
  - 2.1 works better for multitalk/infinitetalk, 2.2 recreates mouth well but has color issues
  - *From: Kenk*

- **MelBandRoFormer vs demucs**
  - MelBandRoFormer performs better in some cases for vocal separation
  - *From: Kijai*

- **Wrapper vs Native with LoRAs**
  - Wrapper+CFG reads prompts better, Native preserves LoRA look better
  - *From: Drommer-Kille*

- **WAN 2.1 I2V vs Runway**
  - Getting better results with WAN 2.1 I2V than Runway for music video creation
  - *From: VRGameDevGirl84(RTX 5090)*

- **WAN 2.2 i2v Low noise vs MagRef with Uni3c**
  - WAN 2.2 i2v Low noise model gave better results with Uni3c than MagRef, though not perfect
  - *From: mdkb*

- **Phantom model quality at different resolutions**
  - Phantom makes great quality at 832x480, but quality degrades when using MagRef with Uni3c at 960x540
  - *From: mdkb*

- **Context windows vs other extension methods**
  - Context is better than any released tech for extending wan, but requires extra compute time
  - *From: Draken*

- **InfiniteTalk vs MultiTalk**
  - InfiniteTalk model 2x larger and 1.5x slower, but miles better with its own sampling loop
  - *From: N0NSens*

- **Lightning models vs LightX2V**
  - Lightning lora is fast but with limited movements and prompt adherence compared to lightx2v for I2V
  - *From: xwsswww*

- **Nunchaku vs Speed LoRAs**
  - Nunchaku 2-3x faster while distill lora is 12x faster, but nunchaku takes less VRAM
  - *From: Kijai*

- **Lightning vs LightX2V distillation models**
  - Using Lightning on high noise, LightX2V on low noise, both at 0.8 weight
  - *From: CJ*

- **VACE vs Fun models**
  - VACE is still better than Fun models, even old VACE GGUF 8 model compared to Fun
  - *From: Gill Bastar*

- **LoRA loader vs Power LoRA stacker**
  - No difference in output or loading times, just aesthetic preference. Core nodes preferred for sharing workflows
  - *From: Kijai*

- **Wan 2.2 vs 2.1 Lightning LoRAs**
  - 2.2 Lightning LoRAs make quality look like 2.1 and aren't as good as LightX2V LoRA in 2.1
  - *From: piscesbody*

- **MagRef + InfiniteTalk vs other methods**
  - Works 100 times better than anything else for keeping likeness and quality with basically no degradation
  - *From: seitanism*

- **Context windows vs InfiniteTalk**
  - Context windows don't work well with I2V and are much slower, InfiniteTalk is better
  - *From: Kijai*

- **Dev version vs main version performance**
  - Dev version saves up to 30GB RAM with 2.2 workflows but may have slightly slower loading times
  - *From: Kijai*

- **Using both high and low samplers vs only low sampler**
  - Using only low sampler looks better, avoids elongated proportions from high sampler
  - *From: Kenk*

- **2.2 Lightning vs FusionX LoRA quality**
  - Wan 2.1 FusionX LoRA was much better quality than lightning
  - *From: BecauseReasons*

- **InfiniteTalk vs MultiTalk for mimicking**
  - InfiniteTalk makes better mimic but has color issues
  - *From: N0NSens*

- **3060 vs higher end cards for AI video**
  - 3060 is best value card, can do a lot for <$400 and replaceable without concern
  - *From: mdkb*

- **Wan 2.2 vs other models for gender role reversal**
  - No model can do woman lifting man properly, all models fine with man lifting woman
  - *From: seitanism*

- **Wan 2.2 S2V vs other models**
  - Single model unlike mixture of experts, only has 16 input channels (T2V), demo videos only look as good as wan 2.1 multitalk
  - *From: MysteryShack*

- **InfiniteTalk vs MultiTalk for sync**
  - 2.2 InfiniteTalk sync is 'kinda meh' compared to MultiTalk
  - *From: N0NSens*

- **InfiniteTalk vs Wan S2V**
  - InfiniteTalk appears better for lip sync quality
  - *From: DawnII*

- **S2V vs InfiniteTalk**
  - InfiniteTalk is definitely better quality, S2V only positive is image doesn't degrade as fast
  - *From: ArtOfficial*

- **S2V vs MultiTalk**
  - Comparison shared showing S2V vs MultiTalk results at same small resolution
  - *From: patientx*

- **InfiniteTalk vs S2V**
  - InfiniteTalk is superior for lip sync, S2V has weird mouth movement and feels off at 16fps
  - *From: ˗ˏˋ⚡ˎˊ-*

- **MultiTalk vs InfiniteTalk**
  - MultiTalk preferred when InfiniteTalk makes weird noise at head of shot with certain models
  - *From: T2 (RTX6000Pro)*

- **480p GGUF vs aniwan vs aniwan + Pusa**
  - Comparison of InfiniteTalk dynamic tests showing different model performance
  - *From: Дмитрий Марков*

- **MultiTalk/InfiniteTalk vs S2V with Wan 2.2**
  - after my latest tests - I dont see any reason to use multi/infinite with 2.2. You got worse motion with worse quality and longer gen. So it doesn't worth it
  - *From: N0NSens*

- **Veo 3 I2V vs other models**
  - I tried veo3 I2V, it is crap in terms of keeping resemblence. t2v is awesome, but not i2v
  - *From: Hevi*

- **InfiniteTalk vs S2V quality**
  - so far infinitetalk really looks better
  - *From: seitanism*

- **Wan 2.1 vs 2.2 capabilities**
  - i switched to 2.2 the first day when i realized it is way more capable than 2.1
  - *From: Lodis*

- **S2V vs InfiniteTalk**
  - S2V has better teeth handling, framepack instead of context windows, better lipsync, twice as fast inference, but quality degrades over time and less natural movement
  - *From: Kijai, piscesbody, Impactframes.*

- **LightX 2.1 vs Lightning LoRAs**
  - LightX 2.1 LoRAs give better results than Lightning LoRAs when used with Wan 2.2
  - *From: Lodis*

- **Wrapper vs Native quality differences**
  - Native produces much better T2I results than wrapper even with same settings. For video generation, differences are less pronounced
  - *From: hablaba*

- **Framepack vs Context Windows**
  - Framepack allows infinite generation but has quality degradation over time. Context window overlap is not good for lipsync
  - *From: Kijai*

- **HunyuanVideo-Foley vs MMAudio**
  - Better than MMAudio but MMAudio is still considered king. Not worse than Eleven Labs
  - *From: Draken, ˗ˏˋ⚡ˎˊ-, Juampab12*

- **S2V vs MultiTalk lip sync quality**
  - MultiTalk has smoother motion at 25fps, S2V has stop motion issues at 16fps
  - *From: hicho*

- **Sapiens vs DWPose for pose control**
  - Sapiens with filtered bones works better, avoids headphone artifacts
  - *From: ˗ˏˋ⚡ˎˊ-*

- **HunyuanVideo-Foley vs MMAudio**
  - Doesn't seem much better than MMAudio, not worth implementing
  - *From: DawnII*

- **Framepack vs context windows for S2V**
  - Framepack has no burning but worse lipsync due to overlap, context windows have burning but better lipsync
  - *From: Kijai*

- **S2V vs Infinite Talk/MultiTalk for lip sync**
  - S2V is pretty stiff compared to MAGREF + Multi or InfiniteTalk for lip sync quality
  - *From: Kijai*

- **GGUF vs fp8 quantization quality**
  - GGUF offers better quality over fp8, making it worth the complexity to support
  - *From: Kijai*

- **S2V model T2V performance vs other models**
  - S2V disappointing for T2V, opposed to motions like walking, video extensions don't follow prompts
  - *From: flo1331*

- **Infinite Talk vs S2V**
  - User finds S2V is trash compared to Infinite Talk for their use case
  - *From: asd*

- **HunyuanVideo-Foley vs mmaudio**
  - Prompt following is better but not enough to make it usable, mmaudio still preferred
  - *From: DawnII*

- **MAGREF vs other I2V models**
  - MAGREF 14B fp8 scaled gives best results on RTX3090 setup with Infinite Talk
  - *From: NC17z*

- **2.2 T2V vs 2.1**
  - 2.2 T2V is almost identical to 2.1, but I2V is not - 2.2 I2V low noise doesn't stick to start image
  - *From: Kijai*

- **MAGREF vs regular I2V**
  - MAGREF works like phantom using image as reference, does better with context windows than normal I2V for longer videos
  - *From: blake37*

- **Context windows vs Framepack**
  - Context windows give better quality for long generations but lipsync isn't as good
  - *From: Kijai*

- **FP8 vs GGUF on RTX 3060**
  - FP8 usually works better in wrapper, GGUF in native, but depends on workflow
  - *From: mdkb*

- **MultiTalk vs InfiniteTalk**
  - InfiniteTalk produces better mouth movements but can make weird noise frames at head of shot
  - *From: T2 (RTX6000Pro)*

- **Context windows vs other extension methods**
  - Context windows have zero degradation but higher inference cost
  - *From: Kijai*

- **InfiniteTalk vs MultiTalk**
  - MultiTalk preferred for jumping less with uni3c controller and no noise on first frames
  - *From: T2 (RTX6000Pro)*

- **Phantom with vs without negative prompts**
  - Usually better without any negative prompt or minimal negatives
  - *From: Ablejones*

- **QwenEdit vs nano banana**
  - Nano banana is on another level, QwenEdit with LoRAs might get close
  - *From: Nekodificador*

- **MAGREF vs regular I2V**
  - MAGREF is slower but works better for longer contexts, though harder to go back from Wan 2.2 quality
  - *From: Charlie and blake37*

- **Wan 2.1 vs 2.2 with InfiniteTalk**
  - 2.1 works better with infinitetalk but doesn't keep face likeness well in I2V, 2.2 keeps face likeness very well but doesn't follow infinitetalk as well
  - *From: MysteryShack*

- **Wan 2.2 I2V vs Veo3**
  - Wan 2.2 I2V beats Veo3 with proper setup
  - *From: MysteryShack*

- **FP8 vs FP16 quality**
  - Weight precision plays smaller role than expected, FP8_scaled produces very similar results to FP16
  - *From: Kijai*

- **InfiniteTalk vs MultiTalk with context**
  - InfiniteTalk works better with context, MultiTalk has much more movement that struggles with context window
  - *From: N0NSens*

- **CineScale vs UltraWan**
  - CineScale is way better than UltraWan for upscaling
  - *From: DawnII*

- **Regular context window vs InfiniteTalk**
  - Regular context window works much worse than InfiniteTalk. InfiniteTalk is way faster than using context windows
  - *From: N0NSens/Kijai*

- **InfiniteTalk vs S2V**
  - Most people would say InfiniteTalk still. S2V has its benefits but not really direct upgrade
  - *From: Kijai*

- **Native S2V vs KJ's workflow**
  - S2V is mehh. Native implementation lets you use native tools
  - *From: Charlie/Ablejones*

- **LightX2V vs Lightning LoRAs**
  - BecauseReasons prefers Lightning for cleaner results, Juampab12 prefers LightX for better motion
  - *From: BecauseReasons, Juampab12*

- **InfiniteTalk vs S2V**
  - InfiniteTalk is better than S2V for lip-sync quality
  - *From: piscesbody*

- **FLF model vs I2V/VACE FLF**
  - FLF model sucks, better to use I2V or VACE FLF
  - *From: hicho*


## Tips & Best Practices

- **Use different LightX2V strengths for high/low noise models**
  - Context: Strength 3 on high noise, keep at 1 for low noise
  - *From: gokuvonlange*

- **First few steps of high noise model better without LightX**
  - Context: General consensus for better quality
  - *From: TK_999*

- **Use Euler sampler for second pass low noise**
  - Context: Better results with different samplers for each pass
  - *From: GOD_IS_A_LIE*

- **VACE works as a 2-step refiner**
  - Context: First pass with 2.1 almost done, VACE refines in 2 steps
  - *From: GOD_IS_A_LIE*

- **Use quantile adaptive lightxv2 lora for T2V**
  - Context: Works best out of all speed loras for text-to-video generation
  - *From: gokuvonlange*

- **Generate image first to preview before video processing**
  - Context: More efficient workflow to check if you like the scene before starting heavy processing
  - *From: aikitoria*

- **Use multiple input frames to preserve motion in VACE**
  - Context: When chaining I2V sections, using multiple input frames maintains better motion continuity
  - *From: seitanism*

- **Adjust VACE strength between 1-1.5 for background stability**
  - Context: Strength of 1 can cause weird background changes, increase to 1.5 to alleviate but watch for oversaturation
  - *From: seitanism*

- **Drop last 9 frames when splicing VACE videos**
  - Context: For smooth transitions when chaining videos, drop the last 9 frames of each clip except the final one
  - *From: seitanism*

- **Use Github Desktop for custom node management**
  - Context: Easier to test PRs, roll back versions, and handle updates
  - *From: Kijai*

- **Connect context options only to high noise sampler for better results**
  - Context: Uses more VRAM but avoids low noise sampler correcting window changes
  - *From: Cseti*

- **Keep high noise model without LoRAs for better prompt adherence**
  - Context: When wanting better prompt following, avoid lightx2v on high model and use higher CFG
  - *From: gokuvonlange*

- **Use different overlap values to prevent seam overlap**
  - Context: Can use different overlap so seams don't overlap in context windows
  - *From: Kijai*

- **Generate at lower resolution then upscale**
  - Context: Generate at 640x352 then scale to 1280x704 for better performance
  - *From: nacho.money*

- **Separate prompts with | for multi-scene context windows**
  - Context: Only works with wrapper encode node for changing prompts between context windows
  - *From: Kijai*

- **Use specific camera terminology for better results**
  - Context: 'Dolly in/out', 'tracking shot', 'orbiting', 'crane/vertical lift' work better than generic camera terms
  - *From: The Shadow (NYC)*

- **Use T2V lightx2v Lora for 14B text to video, not I2V**
  - Context: Prevents pixel/stipple artifacts in motion blur
  - *From: nacho.money*

- **Use quantile on low pass to speed up generation**
  - Context: When using CFG 3.5 technique
  - *From: The Shadow (NYC)*

- **Avoid mixing 2.1 loras with 2.2 for camera control**
  - Context: Camera control is problematic, stay away from mixing versions
  - *From: The Shadow (NYC)*

- **Run T5 on CPU if maxing out VRAM**
  - Context: Helps with VRAM limitations during generation
  - *From: hicho*

- **Use sage + fp16 for 20% speed boost**
  - Context: Performance optimization
  - *From: Jonathan*

- **Set keep alive=0 and use clean vram node with Ollama**
  - Context: When using OllamaGenerateAdvance node to avoid problems
  - *From: Simjedi*

- **Use CFG 3-3.5 on high pass without LoRAs for better quality**
  - Context: When not using speed LoRAs on high noise model
  - *From: The Shadow (NYC)*

- **LightX LoRA works better on low pass only**
  - Context: Use LightX on low pass, then CFG on high pass for good motion and prompt adherence
  - *From: VRGameDevGirl84(RTX 5090)*

- **T2V LoRAs work better even for I2V**
  - Context: General recommendation for LoRA selection
  - *From: The Shadow (NYC)*

- **Use at least first high noise step with CFG > 1**
  - Context: Most beneficial single improvement for prompt following and motion
  - *From: Ablejones*

- **Beta or beta57 schedulers better than bong_tangent**
  - Context: For two-stage model sampling, bong_tangent too symmetric
  - *From: Ablejones*

- **Use res_2m sampler for now over res_2s**
  - Context: Despite res_2s being preferred, res_2m recommended due to model swapping discrepancies
  - *From: Ablejones*

- **Use different boundary values based on step count**
  - Context: For 40 steps use boundary 15, for 20 steps use boundary 8
  - *From: aikitoria*

- **Negative prompt ignored at CFG=1**
  - Context: Use NAG for negative prompts at CFG 1 instead
  - *From: garbus*

- **Video2Video denoise strength guidelines**
  - Context: <0.3 to refine details, ~0.6 to edit objects, >0.8 for drastic changes. Don't change low noise denoise, only adjust high noise
  - *From: Ant*

- **Use block swap at 20 to manage VRAM during upscaling**
  - Context: When VRAM chokes during high-res processing
  - *From: thaakeno*

- **Generate at lower resolution first, then upscale**
  - Context: Model doesn't do good motion at high res, also faster
  - *From: Kijai*

- **Use 'camera man shadow' in negative prompt to avoid unwanted shadows**
  - Context: When model generates camera operator shadows
  - *From: thaakeno*

- **Interpolate to 25fps for MMaudio compatibility**
  - Context: When using MMaudio with 16fps Wan output
  - *From: thaakeno*

- **Try different CFG values if one doesn't work**
  - Context: When having trouble with prompt adherence
  - *From: Juampab12*

- **Use higher denoise steps on low noise for more detail**
  - Context: Better than upscaling for adding details
  - *From: shockgun*

- **Remove unused clip embeds to save RAM**
  - Context: For 2.2 models, clip embeds are only used in 2.1 I2V
  - *From: Kijai*

- **Use more steps and start later for less change in V2V**
  - Context: When doing V2V upscaling to preserve original content
  - *From: Kijai*

- **Don't use SDE/LCM samplers for less change**
  - Context: When doing V2V operations where you want to preserve the original
  - *From: Kijai*

- **Lower shift should be less change**
  - Context: Parameter adjustment for V2V operations
  - *From: Kijai*

- **Do interpolation after upscaling, not before**
  - Context: Interpolation is lighter process and should be the last step
  - *From: gokuvonlange*

- **Generate at 768 instead of 720 and crop after**
  - Context: To avoid artifacts when rendering non-standard resolutions
  - *From: Juan Gea*

- **Remove lightx2v lora on high noise, use CFG=5 on all timesteps of high noise**
  - Context: For T2I and T2V generations
  - *From: mamad8*

- **Use 3+5 steps configuration**
  - Context: Seems to end on proper sigma the best
  - *From: DawnII*

- **Use euler + beta for T2V/I2V, res_multistep + beta57 for T2I**
  - Context: Better results than default settings
  - *From: mamad8*

- **Use native implementation over wrapper for better results with specific configurations**
  - Context: Never had good results with wrapper using certain configs
  - *From: mamad8*

- **Use long detailed prompts with Wan**
  - Context: Wan likes long ass prompts, especially for transitions
  - *From: Juampab12*

- **Prompt for specific effects to avoid slideshow results**
  - Context: If you don't prompt for any effect with different images, it makes slideshow
  - *From: Kijai*

- **Use commas for powerful prompting control**
  - Context: Can describe sequence of events and specific moments between commas
  - *From: Cubey*

- **Pull video back into ComfyUI to recover workflow settings**
  - Context: When you forgot the settings used for a successful generation
  - *From: screwfunk*

- **Test with 4 steps first before increasing detail**
  - Context: Run quick test to verify movement is correct before committing to longer generations
  - *From: shockgun*

- **Don't try to be a drop-in replacement**
  - Context: Being drop-in replacement would prevent significant model improvements
  - *From: aikitoria*

- **Always backup LoRAs you like**
  - Context: Due to platform takedowns and availability issues
  - *From: Karo*

- **Use cfg on high noise side for proper motion with lightx2v**
  - Context: High side needs cfg for motion, can use lightx2v carefully or skip it on high noise
  - *From: Kijai*

- **Keep video generation to 81 frames or less**
  - Context: Above 81 frames causes significant quality degradation
  - *From: ✧ฅโ๑ↀᆺↀ ๑ใฅ✧PookieNumnums*

- **Use closeups for better action detail**
  - Context: More pixels per object allows model to understand and reproduce actions better
  - *From: Juan Gea*

- **Start with proper models and lightx2v LoRAs at strength 2**
  - Context: Quick start recommendation for wan 2.2
  - *From: Draken*

- **Use explicit action descriptions for complex behaviors**
  - Context: Instead of 'stealing ice cream' use 'taking the ice cream into its paws. The panda holds the ice cream away from the woman and starts eating it'
  - *From: garbus*

- **Keep CFG at 3.5 for first pass in multi-sampler workflows**
  - Context: In workflows with multiple ksamplers, CFG 1 in second and third samplers doesn't affect negative prompt effectiveness
  - *From: 3DBicio*

- **Use different seeds for high and low noise samplers**
  - Context: When using multitalk, set high sampler to specific seed and low sampler to seed 0
  - *From: nacho.money*

- **Avoid pumping distill steps too high**
  - Context: Like most distilled models, too many steps causes overcooking
  - *From: Draken*

- **Reset multistep sampling when switching models**
  - Context: Add euler step when switching to prevent artifacts from multistep samplers using previous model's latents
  - *From: Ablejones*

- **Use high quality prompt prefix**
  - Context: Add 'high-quality photorealistic video, dawn time, soft lighting, top lighting, balanced composition' at beginning improves quality infinitely
  - *From: Alisson Pereira*

- **Use LoRA scheduling for motion control**
  - Context: For motion based loras you want it to dropoff, use timestep scheduling instead of multiple samplers
  - *From: Juampab12*

- **Don't merge LoRAs with scaled fp8 models**
  - Context: In wrapper they work best if you don't merge the loras into scaled models
  - *From: Kijai*

- **Adding last frame helps model significantly**
  - Context: For undertrained models, adding the last frame helps the model sooo much
  - *From: mamad8*

- **Use Claude for prompt generation**
  - Context: When manual prompting fails multiple times, Claude-generated detailed prompts often work on first try
  - *From: Juampab12*

- **Don't use shift for single frame generation**
  - Context: When doing 1 frame, higher shift does not increase quality
  - *From: VRGameDevGirl84(RTX 5090)*

- **Use dedicated endpoints for different model types**
  - Context: Don't switch between I2V and T2V on same endpoint - make separate endpoints so Runpod can optimize flashboot
  - *From: gokuvonlange*

- **Use different step configurations for T2V vs I2V**
  - Context: T2V needs more high noise steps (25/15), I2V needs more low noise steps (15/25)
  - *From: aikitoria*

- **Don't use compressed schedule on high noise steps**
  - Context: Must perform all HN steps normally, otherwise output will be poor
  - *From: Ablejones*

- **Safe approach is no LightX on high noise, LightX on low noise only**
  - Context: Low noise model responds well to LightX, high noise should be left normal
  - *From: Ablejones*

- **Use lower rank LoRAs to reduce memory impact**
  - Context: 32 rank should be fine instead of 64, and it's included in block swap calculations
  - *From: Kijai*

- **Keep prompts short when using VACE to give more room for the rest**
  - Context: When using VACE control system
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Prompt for literally what's inside the mask, not how it's interacting with the outside**
  - Context: When doing VACE inpainting to avoid unwanted transformations
  - *From: Nekodificador*

- **For LoRA training on Wan 2.2: motion/big concepts = high noise, details/person/style = low noise**
  - Context: When deciding which expert to train for dual LoRA approach
  - *From: Juampab12*

- **You can get 80% results by training only one LoRA depending on the task**
  - Context: If lazy about dual LoRA training for 2.2
  - *From: Juampab12*

- **Use different LoRA strengths for high vs low noise**
  - Context: Testing shows 2.25 strength high, 1.75 strength low works better than 1.0 on both
  - *From: Juampab12*

- **Start with one non-LoRA step for better tone setting**
  - Context: 1 step with cfg=3.5 and no LoRA, then remaining steps with cfg=1 and LoRAs for better lighting
  - *From: IceAero*

- **Use minimum 3+3 steps for good results**
  - Context: 2+2 steps is not enough, 3+3 is fine minimum, 4+4 is much better
  - *From: Kijai/Juampab12*

- **Use mixed LoRA approach for best results**
  - Context: Old LightX2V 2.1 on high noise, new Lightning 2.2 on low noise
  - *From: Doctor Shotgun*

- **Add AccVid LoRA for more accurate results**
  - Context: When using Lightning LoRAs, adding AccVid improves output quality
  - *From: piscesbody*

- **Use lower strength values on initial generation steps**
  - Context: 0.4-0.6 strength on first steps looks more natural than 1.0
  - *From: PATATAJEC*

- **Try CFG 3.5 on first step, then CFG 1.0 for remaining steps**
  - Context: When using Lightning LoRAs for better control
  - *From: IceAero*

- **Use block swapping for higher resolutions**
  - Context: 30 blocks out with 5B model allows 3072 resolution on 24GB VRAM
  - *From: Juan Gea*

- **Don't use Lightning LoRA on High Noise model**
  - Context: Lightning LoRA for high noise model isn't great, degrades output quality
  - *From: gokuvonlange*

- **Use lower strength with Lightning LoRA**
  - Context: Lightning LoRA works better at lower strengths like 0.5 instead of 1.0
  - *From: various users*

- **Frame rate affects generation feel**
  - Context: Sometimes generation works better at 24fps vs 16fps for timing, though it doesn't affect actual inference
  - *From: Juan Gea*

- **Don't use any lora on high noise model**
  - Context: It destroys motion and prompt following. Use 10 steps without lora for high model, then 10 steps with lora on low model
  - *From: Ada*

- **Use iterative prompting method**
  - Context: Each attempt trying to fix one specific thing by prompting more carefully based on what doesn't work on previous attempt
  - *From: Ablejones*

- **Start with no lora or wan2.1 loras first**
  - Context: Getting it to understand the prompt on first step or two is key before applying new loras
  - *From: Ablejones*

- **Use detailed, fluff text in prompts**
  - Context: The more instructions you write the better it works, it really likes fluff text because dataset captions are probably long text
  - *From: aikitoria*

- **6 steps minimum for good quality**
  - Context: Less than 6 seems to produce errors or bad gens, 6 steps is consistently always good as minimum
  - *From: Lodis*

- **Use different step distributions**
  - Context: Give more steps to low than high, e.g. 4 high + 6 low for 10 total steps
  - *From: screwfunk*

- **Check denoised output to see lora effects**
  - Context: Look at preview or decode denoised output to compare with/without lora
  - *From: Kijai*

- **Be careful not to ruin motion with high lora strength**
  - Context: When boosting lora strength on high model
  - *From: Kijai*

- **Avoid Lightning loras for I2V**
  - Context: Should be avoided for I2V workflows
  - *From: Kijai*

- **Character loras work better on low model only**
  - Context: Taking character loras off high and only applying to low gave decent results since they can stifle movement
  - *From: screwfunk*

- **Use blockswapping for upscaling longer videos**
  - Context: When VRAM is limited, use blockswapping at 20 blocks to enable upscaling
  - *From: thaakeno*

- **Keep prompts simple for better character consistency**
  - Context: Complex multi-part prompts can hurt character consistency across scenes
  - *From: kendrick*

- **Drag good output back into ComfyUI to recover settings**
  - Context: When workflow gets broken, use a previous good generation to restore all settings
  - *From: screwfunk*

- **More steps help with consistency**
  - Context: Higher step counts improve temporal consistency in generations
  - *From: Kijai*

- **Use higher start steps to avoid style killing**
  - Context: When using LoRAs or style preservation
  - *From: thaakeno*

- **Balance VACE strength or schedule for different timesteps**
  - Context: Using 2 full strength VACEs isn't generally good
  - *From: Kijai*

- **Use lightx2v 2.1 at higher strength on high noise model**
  - Context: Better than Lightning 2.2, low noise is basically 2.1
  - *From: Kijai*

- **Add 'The subjects appearance/hairstyle remains the same' to prompts**
  - Context: When using scene cutting technique for better subject preservation
  - *From: Jonathan*

- **Use exact same prompt for upscaling to avoid changes**
  - Context: When upscaling with WAN 2.2, keep step count and prompt identical to original generation
  - *From: Gill Bastar*

- **Use CFG for best motion quality**
  - Context: For WAN 2.2, CFG produces better motion than lightning LoRAs
  - *From: Kijai*

- **CFG 1 with 3.0 strength LightX2V works better for resemblance**
  - Context: Character resemblance stays better with CFG 1 + LightX2V rather than higher CFG values
  - *From: FancyJustice*

- **Reference subjects at beginning of prompt for scene transitions**
  - Context: Start prompt with subject description, then use 'the scene cuts to' for maintaining resemblance
  - *From: Jonathan*

- **Use Qwen2.5-VL 72B for WAN prompt optimization**
  - Context: Same family of models makes it ideal for optimizing prompts for WAN generation
  - *From: fredbliss*

- **Use different schedulers for high and low samplers**
  - Context: Can improve results when using multiple samplers
  - *From: SonidosEnArmonía*

- **Start simple with workflows**
  - Context: When having issues, stick to simpler workflows rather than complex multi-node setups
  - *From: SonidosEnArmonía*

- **Focus on getting motion right first, then upscale**
  - Context: Even at low res, get the motion you want and upscale that specific result
  - *From: Fill*

- **Match or mix seeds between HP and LP samplers**
  - Context: Experiment with different seed strategies for high pass and low pass
  - *From: The Shadow (NYC)*

- **Use Beta scheduler instead of Beta57 with Euler**
  - Context: Beta scheduler works much better than Beta57 for certain styles
  - *From: The Shadow (NYC)*

- **Use lightning LoRA at 0.7 strength with low CFG for high noise**
  - Context: When using CFG + LoRA mix for 5 second generations
  - *From: Kijai*

- **Blur depth maps to reduce control strength**
  - Context: Alternative to lowering strength parameter for depth control
  - *From: Draken*

- **Use separate VACE nodes for each control type**
  - Context: When using multiple controls like depth and pose
  - *From: SonidosEnArmonía*

- **Prompt 'in a middle of' gesture/jump to make dynamic first frames**
  - Context: For creating more dynamic starting frames
  - *From: Blink*

- **Use | character to separate prompts for scene changes**
  - Context: Alternative to EchoShot that works more reliably
  - *From: Kijai*

- **Use float schedules for VACE strength and CFG**
  - Context: More control over generation process
  - *From: Nekodificador*

- **For T2I, shift must be 1**
  - Context: When using certain workflows to avoid issues
  - *From: N0NSens*

- **Use double reference with white background**
  - Context: Can help improve reference following in VACE
  - *From: Nekodificador*

- **Refresh browser to show generation preview in SamplerCustomAdvanced**
  - Context: Preview sometimes doesn't show up until next generation
  - *From: Kijai*

- **Use detailed prompting with frame-by-frame descriptions**
  - Context: For complex camera movements and character actions
  - *From: Ablejones*

- **Describe lots of action in prompts**
  - Context: Don't just use simple prompts like 'girl exercising' - need detailed action descriptions
  - *From: Cubey*

- **Use CFG 1 for T2V, higher CFG for I2V motion**
  - Context: T2V works well at CFG 1, I2V needs higher CFG for better motion but creates tradeoff with likeness
  - *From: Josiah*

- **Higher CFG equals more motion**
  - Context: When you need more movement in generations
  - *From: Josiah*

- **Don't use bong_tangent with low step counts**
  - Context: Bong tangent scheduler needs 40+ steps to work properly, especially with HN+LN models
  - *From: Ablejones*

- **Use non-SDE samplers for less variation step-to-step**
  - Context: When experiencing unwanted changes between generation steps
  - *From: Ablejones*

- **Don't use speed LoRAs when testing style LoRAs**
  - Context: Speed LoRAs have too much style influence and change the model's output significantly
  - *From: crinklypaper*

- **For V2V upscaling, prompt is somewhat irrelevant**
  - Context: Content already exists, model can figure out minor fixes. Basic scene-setting prompt works as well as detailed ones
  - *From: mdkb*

- **Use LightX 2.1 LoRAs as they work fantastic and don't affect motion**
  - Context: For Wan 2.2 generation
  - *From: Lodis*

- **Enable Memory Context Restore in BIOS for faster boots with high RAM**
  - Context: When using 128GB+ RAM configurations
  - *From: phazei*

- **Use VACE control strength 1:1 instead of 3 and 1.5**
  - Context: Produces better results with VACE module
  - *From: Lodis*

- **Don't convert between fp8 formats**
  - Context: Converting e4 to e5 loses quality on both sides, avoid e4m2 conversion
  - *From: Kijai*

- **WAN is trained on 81 frames**
  - Context: Going off this length won't work as well, model expects 81 frame videos
  - *From: Draken*

- **Add noise setting only affects results when LoRAs are used**
  - Context: In FlF2V workflows, the add noise setting has no effect without LoRAs but creates interesting effects with them
  - *From: piscesbody*

- **Use strength 0.9 instead of 1.0 for better results**
  - Context: With new Lightning LoRAs for less artifacts
  - *From: Kijai*

- **Describe initial scene properly for I2V with new Lightning**
  - Context: Prompt matters a lot with 3+3 steps, need basic scene description like 'man in black suit in brightly lit room'
  - *From: Hoernchen*

- **Use 'Hard cut transition' prompting for scene changes**
  - Context: For teleporting characters to new scenes, describe characters first, then hard cut transition, then scene
  - *From: Juampab12*

- **Use character identity preservation prompts**
  - Context: Add phrases like 'maintaining same facial features', 'keeping same identity', or 'exact same person'
  - *From: FancyJustice*

- **Use gray (127,127,127) for first frame in certain workflows**
  - Context: When working with specific generation setups
  - *From: artemonary*

- **Lower LoRA strength to avoid issues**
  - Context: Try 0.75 or 0.5 strength when experiencing problems
  - *From: ボグダンおじさん*

- **For camera prompting, structure prompt differently**
  - Context: Use format like 'Sunny, Outdoor, [action]. The camera [movement], [lens type]' instead of starting with camera movement
  - *From: HeadOfOliver*

- **Character likeness is better when faces are cropped closer**
  - Context: Doesn't do well with likeness when characters are far from camera
  - *From: FancyJustice*

- **Keep original image stationary until scene changes**
  - Context: Whatever the character looks like right before scene change gets transferred
  - *From: FancyJustice*

- **Use prompts like 'and after a brief flash' to improve prompt following**
  - Context: When Wan isn't following prompts properly, narrative language can help
  - *From: Hoernchen*

- **Merge LoRA setting saves VRAM and speeds up subsequent runs**
  - Context: Slower first time but faster for next runs with same LoRA
  - *From: pagan*

- **Use quantized models for high resolution generation**
  - Context: Q5_K_M quantized version helps with VRAM usage for large resolutions
  - *From: : Not Really Human :*

- **Consider stepped CFG for complex LoRA setups**
  - Context: 2cfg step 1 lora 0, 1cfg lora 1 step 2,3 on 6 step 3/3
  - *From: CaptHook*

- **Use Kijai's defaults for best results**
  - Context: User spent 12 hours testing and found Kijai's defaults consistently produced best results
  - *From: CaptHook*

- **Use Lightning LoRAs at strength 1 only**
  - Context: Higher strengths make output look more like 2.1 instead of 2.2
  - *From: Ablejones*

- **Use VACE with lower strength for image guidance without fixed first frame**
  - Context: When you want image as guide but not as starting frame for I2V
  - *From: Ablejones*

- **Use audio scale 3 and audio cfg 3 with vid2vid**
  - Context: Works well with 0.65 denoise for video-to-video workflows
  - *From: samhodge*

- **Separate vocals properly for better MultiTalk results**
  - Context: Use Spleeter or better vocal separation tools instead of basic separation
  - *From: Kijai*

- **Use First-Frame-Last-Frame technique with VLM automation**
  - Context: For batch processing multiple images automatically without manual intervention
  - *From: R.*

- **Eye the optimal split point from previews**
  - Context: Instead of calculating complex optimal schedules, visually determine when to switch between high/low noise models
  - *From: Kijai*

- **Higher audio_cfg above 1 is slower but more accurate**
  - Context: For MultiTalk lip sync, values above 1 sample multiple times for better quality
  - *From: MilesCorban*

- **Use denoise < 1.0 for video-to-video MultiTalk**
  - Context: Enables proper v2v functionality in MultiTalk workflows
  - *From: Kijai*

- **Use qwen2.5-vl generated prompts for better results**
  - Context: Wan was captioned with qwen2.5-vl, so prompts generated from it work better with lower shift values
  - *From: fredbliss*

- **Higher shift = let model run against training curves**
  - Context: Use higher shift when you want autopilot mode, lower shift for more control with solid prompting
  - *From: fredbliss*

- **Set LoRA strength as float list for different steps**
  - Context: Even if high noise is 5-6 steps out of 8 total, you need 8 values in the list
  - *From: MysteryShack*

- **Use start step directly instead of denoise percentage**
  - Context: Clearer than denoise percentage, especially for low step counts
  - *From: Kijai*

- **Don't want slow motion? First step better not have ANY kind of lora**
  - Context: Universal rule for all distill loras to avoid motion artifacts
  - *From: MysteryShack*

- **Use cached Qwen node to save memory**
  - Context: Node deletes models from memory after running and can cache prompts to disk for reuse
  - *From: Kijai*

- **Merge LoRAs when using FP8 scaled + fast mode**
  - Context: Unmerged LoRAs not possible with FP8 as LoRA application requires upcasting
  - *From: Kijai*

- **Check sigma values in logs to determine high/low split**
  - Context: Sigmas appear in logs when workflow runs, count steps from comma positions to determine proper split point
  - *From: phazei*

- **Use Joy Caption for better prompting**
  - Context: Extra options work really well for video generation prompting
  - *From: screwfunk*

- **Don't use radial attention on early steps**
  - Context: It's disastrous especially on early steps of the high noise model, ruins video coherence
  - *From: Kijai*

- **Use confidence threshold of 0.5 for Sapiens keypoints**
  - Context: Remove anything under 0.5 confidence to avoid bad detection points
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Remove triangle and clavicule from VACE pose input**
  - Context: When using Sapiens with VACE, remove the triangle in middle and clavicule for compatibility
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Use I2V lightning LoRAs with strength less than 1**
  - Context: Regular use less than 1 strength to avoid camera shake issues
  - *From: IceAero*

- **Prompt text preprocessing matters for WAN**
  - *From: fredbliss*

- **Use specific camera movement prompts**
  - Context: For car following shots, try 'first-person perspective', 'camera follows the car side by side', or 'dynamic tracking shot following a [car model] closely'
  - *From: Hashu*

- **Backup pip freeze and whole venv**
  - Context: 30s of compression saves hours of fixing when things break
  - *From: Hoernchen*

- **Check DDR5 RAM compatibility carefully**
  - Context: DDR5 requires specific motherboard compatibility for both size and speed, unlike DDR4
  - *From: Canin17*

- **Use local LLM for action-rich prompts**
  - Context: When getting slow motion at higher frame counts, ask LLM to help create prompts with enough action
  - *From: Hashu*

- **Don't use creative upscaling for likeness retention**
  - Context: When trying to maintain character likeness during upscaling
  - *From: Drommer-Kille*

- **Use CFG for fast motion generation**
  - Context: CFG is key for generating really fast motion, can also mix with high distill LoRA strengths
  - *From: Kijai*

- **High lightning LoRA at 2.5 for natural walking**
  - Context: For natural paced or slightly slow walks, keep low at 1 and avoid going above 2.5 on high to prevent artifacts
  - *From: Alpha-Neo*

- **Use negative prompts for unwanted elements**
  - Context: Put unwanted elements like cars in negative prompt instead of trying to prompt them away
  - *From: aikitoria*

- **3-2 pulldown for 16fps to 24fps conversion**
  - Context: Interpolate 16fps by 3x to 48fps, then strip every other frame to get 24fps for sync with mmaudio
  - *From: nacho.money*

- **Use higher LoRA strength on high noise model for Wan 2.1 LoRAs**
  - Context: When using Wan 2.1 LoRAs with Wan 2.2
  - *From: Kijai*

- **Use 2.0-2.5 strength for high noise model**
  - Context: LoRA strength settings
  - *From: DaxRedding*

- **Temporal mask is opposite to VACE**
  - Context: Using temporal masks with Fun InP
  - *From: Kijai*

- **Give Fun 2.2 enough freedom for better motion**
  - Context: Balancing motion and detail quality
  - *From: Kijai*

- **Add stationary dots to prevent unwanted camera movement**
  - Context: Controlling camera stability in generations
  - *From: ingi // SYSTMS*

- **Use big swap file and --disable-smart-memory for high resolution generation**
  - Context: When running 1600x900x81 frames on lower VRAM GPUs
  - *From: mdkb*

- **Don't use Fun 2.2 for low noise final step**
  - Context: Use 3rd sampler at end without Fun for better quality finish
  - *From: Kijai*

- **Mix images with videos when training character LoRAs**
  - Context: Training only on images kills motion in final model
  - *From: MilesCorban*

- **Use v2v with higher denoise than 0.79 for more changes**
  - Context: 0.79 is tipping point - lower keeps structure, higher changes based on prompt
  - *From: mdkb*

- **Use procexp64 to monitor VRAM usage per node**
  - Context: Free Microsoft tool for monitoring GPU load and memory commit
  - *From: mdkb*

- **Use Lightning + LightX2V LoRA combination**
  - Context: Lightning LoRAs at strength 1.0, then LightX2V at 0.2-0.5 strength to clear up blurry results when stacking multiple LoRAs
  - *From: screwfunk*

- **Use bigger model for prompt generation instead of Qwen2.5**
  - Context: Let Claude or similar make prompts, then use FL Prompt selector from ComfyUI_Fill-Nodes
  - *From: Janosch Simon*

- **Use cfg + lightx2v scheduled for best results**
  - Context: Kijai's preferred setup, sometimes disable cfg for better results
  - *From: Kijai*

- **More than 1 cfg step often needed**
  - Context: Motion can break with only single cfg step
  - *From: Kijai*

- **Decode, upscale, encode instead of latent upscale**
  - Context: Latent upscale is terrible quality
  - *From: Kijai*

- **Check LLM output for unwanted additions**
  - Context: Sometimes LLM adds 'here is my response, are you happy with it' even when told to just output the prompt
  - *From: pagan*

- **Use separate block swaps for high and low noise models**
  - Context: Makes sense for upscaling workflows when models are different sizes
  - *From: Kijai*

- **For video2video without lightning, bypass LoRA and use more steps**
  - Context: Put high noise sampler's CFG to 3.5, expect 4-5x slower
  - *From: Hevi*

- **Use tight crop for better facial similarity**
  - Context: When providing face reference in VACE
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Consider upscaling 720p instead of generating high-res directly**
  - Context: Saves time especially when needing many attempts, 720p to 1080p takes about 500 seconds
  - *From: Hevi*

- **Use normal map control with blur adjustment for 3D renders**
  - Context: For V2V from 3D renders, use normal map control and blur to adjust generation adherence while preserving shapes and movement
  - *From: Blink*

- **Mix control video with straight normal color to adjust strength**
  - Context: Mix control video with normal color (128, 128, 255) to prevent bleeding into generation
  - *From: Blink*

- **Use gradual blending for seamless transitions between control clips**
  - Context: Create natural transitions by letting control go off for some frames
  - *From: Blink*

- **Use Wan 5B for upscaling instead of SeedVR**
  - Context: Do V2V with denoise 0.35-0.5 after simple Lanczos resize, or use I2V with 5B to guide upscale
  - *From: Juan Gea*

- **Wan 2.2 Low Noise can fix wobbling before upscaling**
  - Context: Run video through Wan 2.2 Low Noise with 0.2-0.3 denoise before upscaling with SeedVR2
  - *From: AmirKerr*

- **Use face detection with crop and stitch for face consistency**
  - Context: Mask face, crop to 1024x1024, do V2V to improve face, then stitch back for broken background faces
  - *From: Juan Gea*

- **SeedVR needs high batch number for stable images**
  - Context: Higher batch sizes prevent instability in SeedVR upscaling
  - *From: shockgun*

- **Use face target and crop then rembg for best Stand-in results**
  - Context: When preparing reference images for Stand-in LoRA
  - *From: Kijai*

- **Match generation dimensions with reference image size**
  - Context: For optimal Stand-in LoRA performance
  - *From: Kijai*

- **Video following camera actions depends more on motion parameters than prompting**
  - Context: Need high quality high-noise steps rather than better prompts
  - *From: Instability01*

- **Use variable LoRA strengths and CFGs for better results**
  - Context: For improved video generation quality
  - *From: Instability01*

- **Best temp fix for identity issues is a real 2.2 distill LoRA**
  - Context: Fixes identity issues by virtue of fewer steps
  - *From: Instability01*

- **Use 'Fast shot, flying into...' instead of 'The camera flies' to avoid generating actual cameras or crew**
  - Context: When creating camera movement prompts
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Lower LightX2V to 0.6 and increase steps for less overcooking**
  - Context: When using speed LoRAs
  - *From: Hevi*

- **Use 'extreme slowmotion' or 'Close-up to mid-shot, ultra slow motion, cinematic shot' for slow motion effects**
  - Context: When wanting slow motion in Wan 2.2
  - *From: Drommen-Kille*

- **Stay above Q6 quantization for good results**
  - Context: Weight precision doesn't seem major as long as above Q6
  - *From: Kijai*

- **Use --reserve-vram argument if getting OOM with partial loads**
  - Context: When native doesn't estimate VRAM need correctly
  - *From: Kijai*

- **Use unsampling after HN model steps before LN model**
  - Context: When combining HN and LN models, doing 1-2 steps of unsampling after HN keeps motion but gives more freedom to LN model with controls
  - *From: Ablejones*

- **Use higher resolution for better face consistency**
  - Context: When having face consistency issues after 1 second in I2V generations
  - *From: N0NSens*

- **For best I2V results, use full model instead of distills**
  - Context: Distillation models will skew results for face likeness preservation
  - *From: DawnII*

- **Reduce VACE strength when combining with other controls**
  - Context: When using VACE with other control methods, lower strength may be needed to avoid conflicts
  - *From: Hashu*

- **Use white background for mask parts to keep, can draw directly on load image node**
  - Context: When creating masks for workflows
  - *From: Kijai*

- **For Stand-In, use only 'man' or 'woman' in prompts without extra appearance descriptions**
  - Context: When you don't want to alter facial features
  - *From: mdkb*

- **Use high-resolution frontal face images for best Stand-In results**
  - Context: Input image recommendations for Stand-In
  - *From: mdkb*

- **24fps helps with Stand-In quality**
  - Context: Video generation settings
  - *From: BobbyD4AI*

- **Describe the whole image with i2v as part of the prompt then the action**
  - Context: Better results with I2V generations
  - *From: crinklypaper*

- **Use AIO instead of official controlnet for better performance**
  - Context: When using Canny and other controlnet duties
  - *From: Drommer-Kille*

- **Always boot ComfyUI before starting generation**
  - Context: To avoid having to restart mid-generation
  - *From: Drommer-Kille*

- **Use 1.25x latent upscale instead of 2x**
  - Context: 2x latent upscale usually generates problems with weird rims around objects
  - *From: Drommer-Kille*

- **Maximize reference resolution by cropping properly**
  - Context: Don't leave too much white space around the reference image as it limits resolution
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Use MAGREF when you don't want model to latch onto input image too hard**
  - Context: For context window generations where you want reference behavior rather than exact first frame matching
  - *From: Kijai*

- **Enable fp8 fast mode for significant speed gains**
  - Context: Works fine with 2.2 models and can be 30-40% faster than GGUF
  - *From: Kijai*

- **Use character name in prompt for better consistency**
  - Context: Give character description a name, then write the name doing something for Wan 2.2 to understand better
  - *From: xwsswww*

- **Use 'fixed shot, static camera' to prevent camera movement**
  - Context: When using LoRAs that cause unwanted camera movement
  - *From: Lodis*

- **Adding 'character stays in place' works better than just 'fixed shot'**
  - Context: For character rotation LoRAs to prevent unwanted movement
  - *From: Mngbg*

- **Use inverted canny maps with reduced strength**
  - Context: Black lines on white background, strength 1.0 instead of 1.5 for better canny control
  - *From: xwsswww*

- **Higher CFG good for fast movement generation**
  - Context: CFG 3.5 vs 1 shows dramatic difference in motion speed, but may cause artifacts
  - *From: Mngbg*

- **Use 0.38 denoise for x2 latent upscale**
  - Context: Specific setting that works fine for upscaling
  - *From: Valle*

- **Don't blur the mask for VACE, only blur final composition**
  - Context: When doing VACE inpainting to avoid artifacts
  - *From: Kijai*

- **Use reference image and canny input as separate VACE streams**
  - Context: To control camera motion/depth and reference strength separately
  - *From: Josiah*

- **Let automated memory management do its thing, don't use VRAM clear nodes**
  - Context: VRAM clear nodes are more harm than good
  - *From: Kijai*

- **Use --reserve-vram argument instead of multigpu node**
  - Context: Multigpu node doesn't do anything useful
  - *From: Kijai*

- **Use WanImageToVideo node for I2V models**
  - Context: Required to add proper mask, can't use I2V without it
  - *From: Kijai*

- **Scale down Fantasy Portrait strength when using adult face to drive kids**
  - Context: Adult face driving kids gets too weird without scaling
  - *From: Guey.KhalaMari*

- **Use Cached node for best RAM management**
  - Context: Should have zero impact on performance while saving RAM
  - *From: Kijai*

- **Increase distill LoRA strength to help with leftover noise/snow artifacts**
  - Context: When using distillation LoRAs and experiencing noise issues
  - *From: Kijai*

- **Images in ComfyUI should always be RGB, never RGBA**
  - Context: VAEs never support RGBA, the mask is the A channel
  - *From: Kijai*

- **Don't use Uni3c for context with FantasyPortrait**
  - Context: FP doesn't need it and Uni3c ruins more of the motion
  - *From: Kijai*

- **Use async offloading for minimal inference speed hit**
  - Context: When working with memory management
  - *From: Kijai*

- **Use full steps without loras to reduce noisy pattern in Wan 2.2 Fun**
  - Context: When getting noisy patterns in Fun variant
  - *From: DawnII*

- **Run base 2.2 low noise to address noise issues**
  - Context: Alternative to running full steps without loras
  - *From: DawnII*

- **Use separate VACE embeds for different strengths**
  - Context: When needing individual control over controlnet and reference strengths
  - *From: Nekodificador*

- **Set power limit to 500W instead of 600W**
  - Context: For managing GPU power consumption during generation
  - *From: Kijai*

- **Use comfyui-videohelpersuite node 'Select images' with image set to -1 to extract last frame**
  - Context: When needing to extract the last frame from VAE Decode for video workflows
  - *From: mdkb*

- **Quality of reference image is crucial for VACE**
  - Context: Better reference images lead to dramatically improved results, sometimes looking like lora quality
  - *From: Nekodificador*

- **Use CauseVid at 0.8 strength for maintaining likeness**
  - Context: When working with 2.1 VACE workflows for better identity preservation
  - *From: Josiah*

- **Use lazy switches instead of bypass/muting for more reliable workflows**
  - Context: When building complex switching workflows that need to work with API
  - *From: Kijai*

- **Don't cast e4m3fn model to e5m2**
  - Context: It will be worse than using either format properly
  - *From: Kijai*

- **Use reference images with white background for VACE**
  - Context: Position the object approximately where you want it to appear in output
  - *From: Ablejones*

- **Use virtual environments for experimental nodes**
  - Context: Prevents conflicts when installing nodes with complex dependencies like GGUF converters
  - *From: screwfunk*

- **Extract last frame and use WanVideo Blender for extension**
  - Context: For video continuation without contrast issues, use overlap of 1 frame
  - *From: xwsswww*

- **Use flowmatch_pusa scheduler with PUSA**
  - Context: When using PUSA LoRA for proper functionality
  - *From: JohnDopamine*

- **Use CFG with WanFM for proper transitions**
  - Context: When using WanFM sampling method
  - *From: Kijai*

- **Set audio scale to 3 for MultiTalk with MagRef**
  - Context: For v2v lip-sync with maintained face consistency
  - *From: mdkb*

- **Use LCM on high noise model for prompt adherence**
  - Context: When having trouble getting Wan2.2 to follow prompts properly
  - *From: MysteryShack*

- **Output at each stage for reliability**
  - Context: Due to random particle/snow blips in low noise mode
  - *From: MysteryShack*

- **Use SDPA instead of SageATTN for InFrame with fp16**
  - Context: When getting poor likeness results with InFrame on fp16 models
  - *From: hablaba*

- **For VACE inpainting, alignment of objects/subjects between images is crucial**
  - Context: When using First-Frame-Last-Frame functionality
  - *From: hicho*

- **Use extract last frame approach for better context continuity**
  - Context: When working with context windows
  - *From: xwsswww*

- **Try 5 frames for single image VACE when 1 frame fails**
  - Context: Solves weird artifacts like hands appearing in wrong places
  - *From: mdkb*

- **For MAGREF, you can give different images to windows that don't include start frame and pad them to reduce sticking**
  - Context: Special case for MAGREF with context windows
  - *From: Kijai*

- **Remove negative prompts to avoid skull artifacts in early steps**
  - Context: When seeing consistent skull shapes at first diffusion step
  - *From: SonidosEnArmonía*

- **Use adapter_scale around 0.7 to reduce mouth over-animation**
  - Context: When Fantasy Portrait generates too extreme mouth movements
  - *From: VRGameDevGirl84(RTX 5090)*

- **For LoRA training use 15 images + 15 videos for high noise, 30 images for low noise**
  - Context: Character LoRA training best practices
  - *From: el marzocco*

- **Don't use CLIP vision node with Fantasy Portrait first/last frame workflow**
  - Context: Makes generation super fast when using extracted frames
  - *From: VRGameDevGirl84(RTX 5090)*

- **Use high quality driving video with head taking most of screen**
  - Context: For better Fantasy Portrait results - good lighting, clear mouth visibility
  - *From: seitanism*

- **Use repository at github.com/Wan-Video/Wan2.2 to get full quality**
  - Context: For best results instead of other implementations
  - *From: Benjimon*

- **Refresh ComfyUI with CTRL+R after installing new models**
  - Context: When VACE models don't show up in model select node
  - *From: Ryzen*

- **Remove negative prompts for more diverse first steps**
  - Context: Negative prompts can cause skull diffusing in first step
  - *From: SonidosEnArmonía*

- **Add gray frames to end of batch to satisfy Wan requirements**
  - Context: Use get image batch range node to chop additional frames off if needed
  - *From: Flipping Sigmas*

- **Fix input video framing to remove padding and frame closer to source**
  - Context: Helps with context window stability and character consistency
  - *From: smithyIAN*

- **Use Set LoRA nodes instead of connecting to model loader**
  - Context: Avoids reloading whole model when changing LoRAs
  - *From: Kijai*

- **Use cached encode to help with VRAM on 3090**
  - Context: Helps memory but caches prompts
  - *From: Josiah*

- **Use wildcards for context windows to avoid repetitive output**
  - Context: Splits prompts so each window has own prompt
  - *From: Kijai*

- **First step of high noise model should have no LoRA for T2V**
  - Context: Prevents slow motion problem, I2V doesn't have this issue
  - *From: MysteryShack*

- **Use longer prompts with motion cues and cinematic elements**
  - Context: For more motion and speed in generations
  - *From: Josiah*

- **Can halve block swap amount when using context windows**
  - Context: Don't need as much block swap with context windows
  - *From: Kijai*

- **For skyreels lora looping issues, boost LoRA strength**
  - Context: When using skyreels lora on 2.2 and getting looping effects
  - *From: Kijai*

- **Use first step with CFG then rest without for better motion**
  - Context: Wan 2.2 I2V workflow optimization
  - *From: Kijai*

- **Convert 30fps video to 16fps using select_every_nth to 2**
  - Context: Making control videos compatible with Wan 2.2
  - *From: artemonary*

- **Model can do most things but some actions need incredibly specific prompts**
  - Context: Getting difficult actions like striking to work
  - *From: Ablejones*

- **Use Claude for prompt iteration and refinement**
  - Context: Scientific approach to prompt engineering
  - *From: Ablejones*

- **Use first frame of input video to create ref image with Flux**
  - Context: For consistent style transfer when you want the ref image to match the structure
  - *From: VRGameDevGirl84(RTX 5090)*

- **Use 25fps as sweet spot for MultiTalk, even 24fps can cause slurring**
  - Context: For lip sync quality
  - *From: mdkb*

- **Set audio scale to 2.5 for better MultiTalk performance**
  - Context: When other settings aren't working well
  - *From: mdkb*

- **Stick to 81 or 121 frames for talking models**
  - Context: Models were trained on these frame counts and get weird with other lengths
  - *From: NC17z*

- **Use MAGREF model to maintain source image likeness**
  - Context: For better adherence to reference image in i2v workflows
  - *From: mdkb*

- **Use MultiTalk + FantasyPortrait together**
  - Context: FantasyPortrait uses face landmark tracking, MultiTalk keeps lipsync on point
  - *From: mdkb*

- **Use pleasant adult voices for better MultiTalk results**
  - Context: Unique/out-of-distribution voices may not work as well
  - *From: MysteryShack*

- **Edit audio spacing in Audacity before lip sync**
  - Context: Fine-tune pauses and timing for better results
  - *From: MysteryShack*

- **Use empty mask input for proper resize**
  - Context: Add empty mask to inputs for proper image/mask size matching
  - *From: Kijai*

- **Watch frame rate settings in Video In node**
  - Context: 25fps setting can cause longer generation times than expected
  - *From: mdkb*

- **Don't update ComfyUI frequently to avoid breaking workflows**
  - Context: Custom nodes often break with updates
  - *From: Kijai*

- **Use 25fps for audio embeddings regardless of output fps**
  - Context: MultiTalk is trained at 25fps, change only the output fps for sync
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Audio can provide more than lip sync**
  - Context: Audio also influences hand movements and overall motion
  - *From: Dream Making*

- **Color match not necessary with new model**
  - Context: The colormatch doesn't seem that necessary with this new model
  - *From: Kijai*

- **Every LoRA added with GGUF increases memory use and slows it down**
  - Context: When comparing to merged loras
  - *From: Kijai*

- **Use disk cache in WanVideo Text Encoder**
  - Context: Saves prompt to disk so same prompt next time doesn't need encoding, saves time
  - *From: Kijai*

- **Don't touch frame_window_size setting**
  - Context: Leave at default 81, motion_frame is the overlap that can be adjusted
  - *From: Kijai*

- **Lower LoRA strength instead of increasing steps**
  - Context: Usually better to lower the Lora strength with distill models
  - *From: Kijai*

- **Use either T2V or I2V LightX2V LoRA**
  - Context: Both work interchangeably for I2V/MagRef model
  - *From: Kijai*

- **Use GitHub Desktop for keeping up with development work**
  - Context: Simple to roll back to commits and update, better than ComfyUI Manager for fast-moving repos
  - *From: Kijai*

- **Use MagRef model without clip embeds**
  - Context: MagRef model doesn't require clip embeds connection unlike other models
  - *From: DawnII*

- **Be careful with LoRAs on high noise side**
  - Context: Low noise side can use LoRAs freely, high noise side needs careful application to not ruin motion - best to use CFG and no lora or weak lora with CFG
  - *From: Kijai*

- **Use masks for targeted lip-sync**
  - Context: Good luck with MultiTalk using VACE and masking faces, regenerating just the face area
  - *From: Tango Adorbo*

- **Audio scale strength above 1 creates exaggeration**
  - Context: Tried strength of 2 and it looked too exaggerated
  - *From: seitanism*

- **Don't touch frame window size parameter**
  - Context: Frame window is how many frames processed at once, leave it default
  - *From: Kijai*

- **LoRA rank above 64 hits diminishing returns**
  - Context: Higher ranks are bigger memory hit when using unmerged LoRAs, especially with GGUF
  - *From: Kijai*

- **Use Linux distro with bundled nvidia drivers**
  - Context: Something with nvidia drivers bundled is best to get started as manual driver install is usually huge pain
  - *From: Kijai*

- **Use 2 steps with multiple speed LoRAs for fast testing**
  - Context: Using Lightx, Pusa, Accvid, and FastWan LoRAs together for 2-step generation in 319 seconds
  - *From: VRGameDevGirl84*

- **Don't change the 81 frame default**
  - Context: The 81 frame setting shouldn't be changed, base model does best at 81
  - *From: Kijai*

- **Audio scale shouldn't be too high**
  - Context: Audio scale of 2 is too high and can have detrimental effects, audio cfg scale of 3-5 is fine
  - *From: Kijai, seitanism*

- **Need extra frames for complete audio sync**
  - Context: Need additional 28 frames beyond audio length to avoid vocal sync failure before end of video
  - *From: NC17z*

- **Standard CFG for Wan is 3-6**
  - Context: For Wan models, use CFG between 3-6 range
  - *From: Ryzen*

- **Keep prompts simple for lip sync models**
  - Context: Use basic prompts like 'Woman Talking' rather than detailed descriptions
  - *From: NC17z*

- **Use external vocal separation tools instead of ComfyUI nodes**
  - Context: Better results for lip sync when using dedicated audio separation software
  - *From: NC17z*

- **Consider first pass with low steps for speed**
  - Context: Use 1 step or low steps for initial video creation, then refine in upscaling pass
  - *From: NC17z*

- **Multiple swap blocks mainly useful as OOM safeguard**
  - Context: Especially when generating at higher resolutions, doesn't significantly impact speed
  - *From: . Not Really Human :.*

- **Use InfiniteTalk for videos longer than 3-5 seconds, MultiTalk/Fantasy Talker for shorter clips**
  - Context: When doing lip sync work
  - *From: NC17z*

- **Use --disable-smart-memory instead of --cache-none**
  - Context: For memory management - means less reloading with about same OOM reduction
  - *From: mdkb*

- **Create webcam video of yourself lip-syncing for better control**
  - Context: Use 480x480 webcam capture of your lip-sync as reference for more accurate results
  - *From: NC17z*

- **Use SetNode and GetNode or Anything Everywhere nodes for workflow organization**
  - Context: For managing complex workflows
  - *From: MysteryShack*

- **Use vid2vid with partial denoise to fix timing issues**
  - Context: Take InfiniteTalk result and run it through vid2vid upscale with MultiTalk, then do two runs - vid2vid with partial denoise (0.65) can fix sins with timing
  - *From: samhodge*

- **Combine InfiniteTalk with vid2vid for better results**
  - Context: Take the infinite talking for the whole video, then run vid2vid with same audio with 0.65 denoise to fix the spazzy motion on the InfiniteTalk output
  - *From: samhodge*

- **I2V may not work well for Qwen->Wan bridge, but T2V with noise samples can**
  - Context: When bridging Qwen image to Wan video, T2V as input samples of noise works much better than I2V approach
  - *From: fredbliss*

- **Use CFG 8 for more dramatic results**
  - Context: When working with image to video generation
  - *From: fredbliss*

- **Crop head, process with InfiniteTalk, then paste back to original**
  - Context: For better lip-sync results with minimal background changes
  - *From: Kijai*

- **Use silent audio to generate longer scenes without dialog**
  - Context: InfiniteTalk can work with silence audio for extended generations
  - *From: mamad8*

- **Keep models in cache by having unused generation nodes in workflow**
  - Context: To prevent slow model reloading when switching between tools
  - *From: mamad8*

- **Use 'R' keyboard shortcut for refresh node definitions**
  - Context: Alternative to finding refresh button in ComfyUI
  - *From: Kijai*

- **Set Manager version to 'nightly' for WanVideoWrapper**
  - Context: Required for latest features and updates
  - *From: Kijai*

- **Use 'git pull' for updating nodes**
  - Context: Best way to update WanVideoWrapper from command line
  - *From: Kijai*

- **For multiple LoRAs, keep recommended strengths**
  - Context: If lora author recommends 0.7 strength, leave at 0.7 even with multiple LoRAs
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Fun Control is very flexible with inputs**
  - Context: Can input RGB or random masks and it will follow
  - *From: Hashu*

- **Use select images node with '0:yourframecount' to trim extra frames**
  - Context: Removes extra frames appended at end of InfiniteTalk generation
  - *From: ArtOfficial*

- **Use audio scale of 2.5 for better lip movement in MultiTalk**
  - Context: Otherwise lips don't move much
  - *From: mdkb*

- **Mix MultiTalk and InfiniteTalk for best results**
  - Context: When doing lip sync work
  - *From: mdkb*

- **Use 3 Sampler method with Wan-Lighting for more motion**
  - Context: Definitely makes a difference in bringing in more motion
  - *From: ArtOfficial*

- **For Wan 2.2 training, split samples by 10 or 20 steps and use low vram mode**
  - Context: Trains at normal speed but quality results not yet achieved
  - *From: Drommer-Kille*

- **Interpolate Wan output to 30fps for better viewing experience**
  - Context: Raw output feels like it skips frames
  - *From: ArtOfficial*

- **Fill masked area with grey (0.5/128) and provide same area as mask for VACE**
  - Context: When using VACE inpainting
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Use very dim grey values (1,2,3) for segmentation masks**
  - Context: For MultiTalk masking different speakers
  - *From: samhodge*

- **Connect negative prompt to NAG input when using cfg 1.0**
  - Context: Since normal negative doesn't work with cfg 1, this acts like having a negative
  - *From: Juan Gea*

- **Add denoised->decode->video between every sampler for debugging**
  - Context: To see where generation breaks down and how settings affect different stages
  - *From: Instability01*

- **Use 1x res_2s high step, 2x res_2s low steps with LTX 4-5 on high, 1 on low**
  - Context: For maximum motion while retaining original image
  - *From: Instability01*

- **Use LoRA training with popular celebrities for better consistency**
  - Context: When creating character-consistent videos, train LoRA with recognizable celebrities since models know them well and data is available
  - *From: Nekodificador*

- **Focus on fewer shots with better quality rather than full scenes**
  - Context: Better to do half a scene with quality shots than full scene with mediocre results
  - *From: Nekodificador*

- **Use prompt separation/echoshot formatting for jump cuts**
  - Context: Better success getting jump cuts and hard transitions in WAN 2.2 I2V
  - *From: DawnII*

- **Chain WanVideo LoRA select nodes using prev_lora input**
  - Context: When adding multiple LoRAs to workflow
  - *From: seitanism*

- **Test LoRA strength between 0.5 and 1.7**
  - Context: For WAN 2.2 with LoRAs, experiment with different strengths in this range
  - *From: seitanism*

- **Use start frame to guide masked generation**
  - Context: When using differential diffusion, start frame helps avoid random generation
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Manually adjust mask proportions for better results**
  - Context: When using VACE with character replacement, manually adjusting masks in editing software makes huge difference
  - *From: Nekodificador*

- **Lock runtime environment for reproducible results**
  - Context: Don't update until you have time to debug, version your runtime with data and workflow
  - *From: samhodge*

- **Use simplified Chinese for prompts**
  - Context: When wanting to try Chinese prompts in Wan 2.2, use simplified Chinese in DeepL
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Higher CFG for 5B without acceleration**
  - Context: For 5B model without accelerators, use CFG 3.5 or 5
  - *From: Juan Gea*

- **Use dpm++_sde with lightx2v loras**
  - Context: Usually gets better results with lightx2v loras especially
  - *From: Kijai*

- **Loras make huge difference for single image gen**
  - Context: When doing single image generation with Wan
  - *From: Kijai*

- **Use tiled VAE for 4K resolution generation**
  - Context: Required when generating at 4K resolution
  - *From: Kijai*

- **Lower VACE strength to 0.5 for inpainting and rely on text prompt**
  - Context: Works best in some inpainting cases, can also add end frame to video with black mask
  - *From: SonidosEnArmonía*

- **Use LightX2V LoRA for better I2V results**
  - Context: Produces better results than Lightning LoRAs for I2V generation
  - *From: A.I.Warper*

- **Film grain not really needed for I2V**
  - Context: Based on testing, film grain doesn't add significant value to I2V workflows
  - *From: Kenk*

- **Don't use CFG on low noise at all**
  - Context: Keep low noise at cfg 1.0 and use lightx2v or lightning at 1.0
  - *From: Kijai*

- **Steps that use CFG should have LoRA disabled or at low strength**
  - Context: When using CFG scheduling on high noise
  - *From: Kijai*

- **Use scheduled CFG and LoRA strength together**
  - Context: Better than using 3-4 samplers
  - *From: Kijai*

- **Use prefetch_blocks and use_non_blocking for 2x speed**
  - Context: Block swap optimization settings
  - *From: matatrata*

- **Don't use multitalk node for short clips**
  - Context: For clips around 5s or less, use normal I2V node
  - *From: Kijai*

- **Don't mess with window_size in multitalk**
  - Context: Causes interpolation artifacting at transition points
  - *From: DawnII*

- **Load models without LoRAs when using CFG**
  - Context: When using 3-4 samplers with Wan 2.2
  - *From: DawnII*

- **Use latent insertion trick for better results**
  - Context: Add input image as extra latent to avoid start being noise
  - *From: Kijai*

- **Use PUSA LoRA to preserve original colors**
  - Context: When doing VACE inpainting to maintain reference image colors, though it has big memory impact with GGUF
  - *From: SonidosEnArmonía*

- **Work with minimal LoRAs or tweak strengths**
  - Context: LoRAs can change reference too much, better to use lightx2v and PUSA only if wanting to preserve colors
  - *From: SonidosEnArmonía*

- **Provide more pose images than needed for UniAnimate**
  - *From: Kijai*

- **Use TAESD preview and CFG/LoRA scheduling**
  - Context: For previewing single step results and being able to cancel if generation looks bad
  - *From: Kijai*

- **Use prefetch_block and non-blocking memory transfer together**
  - Context: For optimal block swapping performance
  - *From: Kijai*

- **Don't use TeaCache with LightX2V**
  - Context: It's either one or the other, not both
  - *From: Kijai*

- **Use GGUF instead of plain fp8**
  - Context: Unless using --fast flag, should use GGUF. For --fast use scaled fp8
  - *From: Kijai*

- **Set prefetch blocks to 1**
  - Context: One was enough and more didn't make a difference
  - *From: Kijai*

- **Use global seed for testing LoRAs effectively**
  - Context: When testing LoRAs, global seed helps with consistency
  - *From: CJ*

- **Separate control inputs in VACE**
  - Context: Don't combine pose/depth/lineart into single control - use separate VACE control inputs
  - *From: Ablejones*

- **Use --cache-none for memory help**
  - Context: Can help with memory issues but models reload every time if you have slow drive
  - *From: garbus*

- **Wrapper + block swap + virtual memory for 16GB systems**
  - Context: Combination can help run larger models on limited RAM systems
  - *From: hicho*

- **Balance memory with blocks_to_swap parameter**
  - Context: Key to running bigger models - balance VRAM and RAM usage with blocks_to_swap number
  - *From: Kijai*

- **Default to core nodes when sharing workflows**
  - Context: Less that can go wrong, fewer dependencies to keep updated
  - *From: Kijai*

- **Use single prompt for context options to maintain consistent motion**
  - Context: When generating long videos with context windows
  - *From: Drommer-Kille*

- **Set frame_window_size to 121 when using Skyreels**
  - Context: Skyreels 720p can handle 121 frames vs normal I2V's 81 frames
  - *From: Kijai*

- **Use CFG 3.5 in high sampler and lightning lora in low sampler**
  - Context: To get same prompt following as wrapper but with native image quality
  - *From: Drommer-Kille*

- **White pixels that completely surround your subject are important for VACE**
  - Context: When creating reference images for character replacement
  - *From: Ablejones*

- **Don't add Lightning LoRA to high noise model in 2.2**
  - Context: Prevents high dynamic results and reduces model effectiveness
  - *From: MysteryShack*

- **Don't use torch.compile with 14B model**
  - Context: On smaller models it reduces VRAM use, but on 14B it just slows it down
  - *From: Kijai*

- **Use depth control only for better backgrounds, avoid aggressive canny**
  - Context: Canny can create unwanted background artifacts
  - *From: hicho*

- **For single frame VACE, use 8 steps instead of 4**
  - Context: 4 steps is not enough for single frame generation
  - *From: hicho*

- **Mask the image area when using crop&stitch for overlays**
  - Context: More effective than relying on Wan's natural overlay handling
  - *From: Valle*

- **Trigger words in LoRAs can cause unwanted text/brand generation**
  - Context: Model interprets trigger words as brand names to render
  - *From: Kenk*

- **Use image with mouth slightly open for better InfiniteTalk generation**
  - Context: Helps lip sync generation significantly
  - *From: 3DBicio*

- **Don't use both pose and canny together in VACE**
  - Context: Creates canny imaging of stick skeleton which isn't needed
  - *From: mdkb*

- **Use NAG to remove something specific rather than generic negative prompting**
  - Context: NAG works best for targeted removal
  - *From: Kijai*

- **Increase NAG alpha and/or scale if effect is too weak**
  - Context: Default NAG settings can be adjusted for stronger effect
  - *From: Kijai*

- **Use cached text encoder node directly with NAG for RAM issues**
  - Context: Connect text embeds to text embeds and negative embeds to nag embeds
  - *From: Kijai*

- **Mix controlnets and chain VACE together for eye line correction**
  - Context: Use different strengths on dwpose, depth, ref image encoders
  - *From: JalenBrunson*

- **Use Set/Get nodes instead of Anything Everywhere**
  - Context: Anything Everywhere is buggy and confusing, set/get is more reliable
  - *From: Gateway {Dreaming Computers}*

- **For video upscaling challenges**
  - Context: Video upscaling is very difficult and ruins character consistency
  - *From: Dream Making*

- **Removing WanVideo Long I2V Multi node for speed**
  - Context: Can speed up inference for short 3-5 second videos, but node is necessary for proper InfiniteTalk function
  - *From: Mancho*

- **Use fp16 instead of bf16 for better results**
  - Context: Reference in VACE works better with fp16, and can help with VRAM issues
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Use wan.video for testing - it's much faster (3-5 minutes)**
  - Context: Don't use gradio for testing
  - *From: ZeusZeus*

- **Don't use both beta sigmas and beta scheduler**
  - Context: Applies beta sigma conversion twice
  - *From: Kijai*

- **Use 0.6/0.6 for alpha/beta values**
  - Context: Default recommended values for scheduling
  - *From: Ablejones*

- **Can offload everything to reduce VRAM usage**
  - Context: For the heavier S2V model
  - *From: Kijai*

- **Try 6 or 8 steps instead of 4 for better results**
  - Context: 4-step LoRAs aren't locked to 4 steps, very low in general
  - *From: JohnDopamine*

- **Best not to mix LoRA loader with setLoRAs**
  - Context: When using LoRAs in workflows
  - *From: Kijai*

- **Use muting instead of bypassing nodes for get/set issues**
  - Context: When ComfyUI 'fixed' get/set node behavior
  - *From: phazei*

- **Minimize custom nodes for better stability**
  - Context: Too many custom nodes create dependency conflicts and workflow sharing issues
  - *From: phazei*

- **Use --use-quad-cross-attention instead of --use-sage-attention**
  - Context: For AMD users, safer to start ComfyUI this way then use Kijai's sage attention node
  - *From: patientx*

- **Use separate block swap settings for high and low samplers**
  - Context: When using Fun 2.2 workflow with memory constraints
  - *From: scf*

- **Lower overlap on low sampler for speed**
  - Context: 16 overlap fine for low, up to 48 may be needed for high noise for better blending
  - *From: Kijai*

- **Don't use single sampler for longer generations**
  - Context: Not supposed to use single sampler for extended video generation
  - *From: Kijai*

- **Use two-pass workflow for animation + lipsync**
  - Context: You can do that in two pass, quite slow but it works: 1st pass T2V/VACE, 2nd pass I2V/InfiniteTalk/FantasyPortrait
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Use FantasyPortrait + InfiniteTalk together for better lipsync**
  - Context: I mean you can already use FantasyPortrait + InfiniteTalk together in the wrapper to get really good lipsync
  - *From: Kijai*

- **Aim for 95% VRAM usage for optimal performance**
  - Context: yeah that can be more optimal, something like 95% used is generally safe
  - *From: Kijai*

- **Stay under 832 resolution to avoid slowdowns**
  - Context: I found out at least in my case going over 832 makes everything extra slow
  - *From: patientx*

- **Use lightx2v I2V instead of T2V in some cases**
  - Context: i was using lightx2v i2v.. as kijai said, this is a mix of all existing techs
  - *From: Kenk*

- **Use DPM++ SDE Beta sampler in wrapper to match native Euler Beta results**
  - Context: When trying to match wrapper results to native
  - *From: Draken*

- **Use merged LoRAs in wrapper for better compatibility**
  - Context: When custom LoRAs aren't working properly
  - *From: Kijai, mamad8*

- **Unmerged LoRAs use more VRAM**
  - Context: When managing VRAM resources
  - *From: Kenk*

- **Use multiple VACE encoders instead of image blend to reduce skeleton artifacts**
  - Context: When working with pose control
  - *From: JalenBrunson*

- **Disable LightX LoRAs if experiencing color degradation in long videos**
  - Context: For InfiniteTalk videos longer than 1 minute
  - *From: boorayjenkins*

- **Filter side bones when using Sapiens for pose control**
  - Context: To avoid headphone and clavicle artifacts in VACE
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Use only first step with pose condition multiplied by 0.5**
  - Context: To reduce teeth artifacts and improve pose control
  - *From: Kijai*

- **Composite original unmasked area back over video after generation**
  - Context: For V2V with masked areas to preserve unedited regions
  - *From: ArtOfficial*

- **Keep LoRA strength much lower when using LightX2V**
  - Context: Use LightX2V at 0.3 strength for better results
  - *From: gordo*

- **Prompt 'she opens her mouth as she sings' for better S2V results**
  - Context: To improve lip sync quality in speech-to-video generation
  - *From: hicho*

- **Use PUSA for maintaining image likeness across context windows**
  - Context: Better preservation of reference images in I2V workflows
  - *From: DawnII*

- **Use 1.5 lightx2v strength instead of 1.0 for better results**
  - Context: 1.0 lightx2v doesn't work properly due to being too different from base model
  - *From: Kijai*

- **Feed same input image into extra latent via VAE Encode for character consistency**
  - Context: When using FFLF method for maintaining character details
  - *From: DawnII*

- **Use 10-15 seconds of audio for voice cloning with Chatterbox**
  - Context: For best voice cloning results with TTS systems
  - *From: Juampab12*

- **Convert audio to video first, then link audio input for frame calculation**
  - Context: To automatically calculate needed frames based on audio input for S2V
  - *From: hicho*

- **Use Linux for much better memory efficiency**
  - Context: 64GB RAM on Linux vs 128GB on Windows for same performance level
  - *From: Kijai*

- **Use default Kijai workflow with magref model for best Infinite Talk results**
  - Context: When using Infinite Talk for lip sync
  - *From: asd*

- **Use QwenVL with system prompt and video input to generate mmaudio prompts**
  - Context: When needing to prompt audio events at specific times in video
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Provide more overlap frames for video continuation**
  - Context: When using Fun or VACE for continuation - with only 1 frame it doesn't have enough info
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Use uni3c for camera control**
  - Context: Can record camera movements with iPhone and apply to AI generations
  - *From: T2 (RTX6000Pro)*

- **Always use offload_device for model loading**
  - Context: Should always be offload_device really to avoid memory issues
  - *From: Kijai*

- **Use larger overlap for context windows with lots of movement**
  - Context: Can happen with lots of movement or if camera moves, larger overlap can help
  - *From: Kijai*

- **Balance Framepack settings carefully**
  - Context: Need to find balance that gives enough motion but doesn't burn the image, too many steps can be bad especially with lightx2v
  - *From: Kijai*

- **Keep shift low with Framepack**
  - Context: Shift should be pretty low when using Framepack
  - *From: Kijai*

- **Use LCM sampler with Framepack**
  - Context: Some samplers destroy Framepack quickly, LCM seemed better
  - *From: Kijai*

- **Save workflow images at 1:1 scale**
  - Context: Click image twice to get 1:1 view then save or it won't pick up the JSON file
  - *From: T2 (RTX6000Pro)*

- **Generate audio first then load vs running with each video gen**
  - Context: Better to make the audio first then load it vs running it with each video generation
  - *From: JohnDopamine*

- **Use NAG instead of CFG for better concept avoidance**
  - Context: Especially useful with LightX distillations and specific unwanted elements
  - *From: Nekodificador*

- **Boost LoRA strength for mouth movement in S2V**
  - Context: Similar to 2.2 high noise requirements
  - *From: Kijai*

- **Use stride on high noise side only with 2.2**
  - Context: Makes things jittery but blends windows better, low noise can fix it
  - *From: Kijai*

- **For VACE inpainting, fill RGB areas with 128,128,128 gray**
  - Context: When using alpha masks for inpainting
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Use FantasyPortrait on first step only at lower strength**
  - Context: When combining with S2V for less strict control
  - *From: Kijai*

- **Don't use speedup tricks with Wan 2.2**
  - Context: Any speedup tricks kill all the quality in 2.2
  - *From: MysteryShack*

- **Use full CFG with Wan 2.2**
  - Context: CFG to 1 for too many steps kills prompt adherence
  - *From: MysteryShack*

- **Use CineScale LoRA at 0.7 strength**
  - Context: Full strength causes artifacting, 0.7 avoids this
  - *From: DawnII*

- **Higher denoise (0.6-0.7) works with CineScale**
  - Context: Unlike UltraWan which artifacts at higher denoise
  - *From: DawnII*

- **Use | symbol in WanWrapper for prompt batches**
  - Context: WanWrapper uses the | symbol to make a prompt batch that can be used to the content window
  - *From: Dita*

- **Generate start image and use that instead of pure T2V**
  - Context: When wanting long generations with character consistency
  - *From: Kijai*

- **Different techniques for different shots in complex projects**
  - Context: Some shots work just out the box with VACE+DWPose and inpainting, others require reference frames or depth with schedule strength
  - *From: Nekodificador*

- **3 prompts with more frames can be faster than 4 prompts with fewer frames**
  - Context: 3 prompts x 81 frames (14:36) was faster than 4 prompts x 65 frames (18:05) due to overlap processing
  - *From: Dever*

- **Right click image and open in browser to download with metadata**
  - Context: When ComfyUI workflow metadata isn't preserved in direct download
  - *From: Juampab12*

- **Google parts of model name to find download links**
  - Context: When looking for specific model downloads
  - *From: 𝕯𝖗. 𝕸𝖆𝖈𝖆𝖇𝖗𝖊 ☠*


## News & Updates

- **Wan 2.1 LoRA trainer extension found**
  - ComfyUI extension for training Wan 2.1 LoRAs discovered
  - *From: Ryzen*

- **Deforum Wan integration being explored**
  - Huemin looking into using Wan as image model for Deforum animations
  - *From: NebSH*

- **WAN 2.2 VACE test version available**
  - Test version of VACE for WAN 2.2 released on HuggingFace
  - *From: avataraim*

- **SageAttention3 early access available**
  - Early access version available but quality is poor, public release not yet available
  - *From: Kijai*

- **Text encoder caching improvements**
  - New node completely unloads T5 after use, leaves nothing in VRAM or RAM
  - *From: Kijai*

- **Bug fix for EchoShot disk cache**
  - Fixed bug where echoshot wouldn't activate if prompt was loaded from cache
  - *From: Kijai*

- **New T5 unload node released**
  - New node completely unloads T5 after use to save RAM, useful for high VRAM usage scenarios
  - *From: Kijai*

- **Context options support for prompt separation**
  - Can now separate prompts with | symbol for different scenes in context windows, only works with wrapper encode node
  - *From: Kijai*

- **NAG support added to text encoding**
  - New separate output for NAG (Negative Attention Guidance) support added to text encoding nodes
  - *From: Kijai*

- **Qwen3-coder 30B-a3b now available**
  - Latest version of the code generation model
  - *From: piscesbody*

- **Context windows now work with 5B model**
  - Kijai made it run with 5B
  - *From: Kijai*

- **New text encode node with NAG support**
  - Fixed disk cache issue
  - *From: Kijai*

- **First and last frame capability mentioned in recent update**
  - Functionality available in VACE and being developed for official release
  - *From: AJO*

- **ChatGPT custom GPT for Wan 2.2 prompts available**
  - Trained on official examples and formula document, can write T2V prompts or create prompts from images
  - *From: ✧ฅโ๑ↀᆺↀ ๑ใฅ✧PookieNumnums*

- **Test VACE model available for Wan 2.2**
  - Hugging Face repo with test version
  - *From: BondoMan*

- **Qwen 2.5 integrated into Wan wrapper**
  - Local prompt extension capability with zero memory usage after completion
  - *From: Kijai*

- **Wan 2.1 Audio-14B-720P branch mentioned**
  - Separate model for audio conditioning, lip-sync, talking head animation
  - *From: thaakeno*

- **Wan 2.2 mentioned but 2.1 version never seen**
  - They mentioned 2.1 months ago, now 2.2, but 2.1 never appeared
  - *From: Kijai*

- **ComfyUI native support for Wan 2.2 FLF2V**
  - Official ComfyUI blog announced native support
  - *From: BarleyFarmer*

- **WanImageToVideo node added for FLF support**
  - New node available in updated wrapper for first-last frame functionality
  - *From: Kijai*

- **VACE 2.2 anticipated release**
  - Community excited for VACE 2.2 release, expected soon
  - *From: pom*

- **Wan 2.3 predicted by end of 2025**
  - Speculation about next version timeline
  - *From: Ryzen*

- **FastWan for 5B model almost ready**
  - Speed optimization LoRA for 5B model development visible in GitHub commits
  - *From: Screeb*

- **First-Last-Frame support added to Wan 2.2 native**
  - FLF functionality now available in native ComfyUI, just needs latest update
  - *From: Rainsmellsnice*

- **Civitai LoRA takedowns affecting community**
  - Many LoRAs removed from Civitai, community looking for alternatives
  - *From: DaxRedding*

- **DFloat11 compression available for Wan2.2**
  - 32% size reduction while maintaining bit-identical outputs, allows 24GB GPU generation
  - *From: scf*

- **Phr00t released new Rapid AllInOne v2**
  - Claims more 2.2 features in v2, though still more 2.1 than 2.2
  - *From: hicho*

- **FastVideo 2.2 coming soon**
  - Next version of FastVideo LoRA in development
  - *From: Draken*

- **FPS1 LoRA released for experimental storyboarding**
  - Generates videos at 1 FPS instead of 16 FPS for creating longer scenes and storyboard frames
  - *From: mamad8*

- **LoRA timestep scheduling feature added**
  - Added to WanVideoWrapper, only works when unmerged, allows per-step control and curves
  - *From: Kijai*

- **GGUF compatibility fixed**
  - Should work with GGUF models now after latest update
  - *From: Kijai*

- **bf16 I2V models uploaded**
  - High and Low bf16 models available on HuggingFace
  - *From: Kijai*

- **AI-TOOLKIT supports Wan 2.2 5B training**
  - Very good official template available in RunPod
  - *From: Drommer-Kille*

- **New First-Last-Frame workflow available**
  - Can be found under workflow templates flf2v after updating ComfyUI
  - *From: Rainsmellsnice*

- **Wan 2.2 Lightning LoRAs released**
  - Official lightning LoRAs for Wan 2.2 released but had alpha value issues initially
  - *From: yi*

- **720P distilled I2V model released**
  - LightX2V Wan2.1-I2V-14B-720P-StepDistill-CfgDistill released
  - *From: DawnII*

- **Wan 2.2 Lightning empty repository created**
  - ModelTC/Wan2.2-Lightning repository created but initially empty
  - *From: yi*

- **New Wan 2.2 Lightning LoRAs released by Kijai**
  - Fixed versions that work at 1.0 strength instead of 0.125, available on HuggingFace
  - *From: Juampab12*

- **Fake 720p I2V LoRAs uploaded then removed**
  - 720p I2V LoRAs were uploaded but were actually just 480p versions adapted to model diffs
  - *From: screwfunk/Karo*

- **Qwen image model released**
  - New Qwen 20B T2I model dropped today from same company as Wan team
  - *From: TK_999/Ada*

- **Wan 2.2 Lightning LoRAs released**
  - New 4-step distillation LoRAs available for high and low noise passes
  - *From: Ant*

- **5B model first/last frame support added**
  - Kijai updated WanVideoWrapper to support first/last frame with 5B model
  - *From: Kijai*

- **FastWan2.2-TI2V-5B-FullAttn-Diffusers released**
  - New full attention version available on HuggingFace
  - *From: yi*

- **Lightning Distill LoRAs released for Wan 2.2**
  - LightX team released 4-step distill LoRA for 2.2 14B model
  - *From: DawnII*

- **FastWan 5B model converted to ComfyUI**
  - Kijai converted FastVideo team's distilled 5B model to ComfyUI format
  - *From: Kijai*

- **Wan 2.2 VACE expected in 1-2 months**
  - Official Wan 2.2 VACE system expected to release in 1-2 months
  - *From: hicho*

- **New image guide updated**
  - Alibaba updated their official image guide documentation
  - *From: hicho*

- **Grok Imagine coming to Premium subscribers**
  - All Premium subscribers should have access to Grok Imagine for super fast picture & video creation
  - *From: mdkb*

- **New Lightning lora commit**
  - New commit 7 mins ago with sekov1 version, removed alpha=8 so strength of 1
  - *From: Doctor Shotgun*

- **FastWan models released**
  - FastVideo released FastWan2.2-TI2V-5B and FastWan2.1-T2V-1.3B variants
  - *From: QANICS🕐*

- **Lightning lora updated with alpha keys**
  - Seko version added alpha keys so it can be used at 1.0 strength
  - *From: Kijai*

- **New rank64 lightning LoRAs released**
  - Functionally identical to Kijai's provided lightning LoRAs, confirmed through testing
  - *From: Kijai*

- **Lightning 2.2 LoRAs released but with issues**
  - New Lightning models uploaded but they don't work as well as previous versions and have timestep scheduling requirements
  - *From: Kijai*

- **LightX2V commit suggests 2.2 self-forcing distill**
  - GitHub commit matches naming scheme for 2.1 self-forcing distills, though config still uses 2.1
  - *From: JohnDopamine*

- **Context sliding workflow available**
  - Kijai shared context windowing workflow that samples model multiple times per step and blends results
  - *From: Kijai*

- **Torch compile support added to VAE decode**
  - Recent update allows torch compile for VAE operations but can cause issues if auto-connected
  - *From: Kijai*

- **Official context window support in development**
  - Kosinkadink started working on official context window support within ComfyUI in the context_windows branch
  - *From: Kosinkadink*

- **Wan 2.2 paper released**
  - Official paper for Wan 2.2 has been published
  - *From: Дмитрий Марков*

- **TensorRT optimization mentioned**
  - Real-time Wan generation being discussed with TensorRT
  - *From: Cubey*

- **Gen4-Aleph already on Runway's API**
  - Runway normally waits months before putting new tech on API
  - *From: Draken*

- **QwenImage latent support added to WAN wrapper**
  - Can now use QwenImage outputs directly in wrapper and decode with native if faster
  - *From: Kijai*

- **Google announcing Android vibecoding in realtime generative world**
  - Expected in 2-3 days according to speculation
  - *From: Nekodificador*

- **On-device inference getting serious investment**
  - Client mentioned increased investment in local AI inference
  - *From: fredbliss*

- **VACE 2.1 can be merged with Wan 2.2 models**
  - Community experimenting with merging VACE 2.1 components into 2.2 for reference following
  - *From: Kijai*

- **Juampab12 has updates coming soon**
  - Mentioned having new updates to share that are looking even better
  - *From: Juampab12*

- **Waver 12B model announced**
  - Claims to be open source, performs at Veo3 level, uses 32B text encoder, DiT architecture with flow matching
  - *From: yi*

- **Kijai uploaded fp8_e5m2 5B model**
  - New quantized version available on HuggingFace
  - *From: phazei*

- **ComfyUI frontend package 1.25.5 released**
  - Latest version works with updated VHS nodes
  - *From: Kijai*

- **New Lightning LoRA versions released**
  - T2V 1.1 and I2V versions available, with fixed alpha issues but not ComfyUI key compatibility
  - *From: Kijai*

- **Adaptive rank LoRA has highest rank at 256**
  - Available as the top-tier Lightning LoRA option
  - *From: Kijai*

- **Lightning 2.2 I2V LoRAs released**
  - New lightning LoRAs available for Wan 2.2, but causing various issues
  - *From: Multiple users*

- **MagCache officially supports Wan 2.2**
  - 1.5-2x speedup now available for Wan 2.2
  - *From: NebSH*

- **ATI motion transfer trajectories tool released**
  - New script for creating motion transfer trajectories from video
  - *From: Kijai*

- **Wan 2.2 Fun Control released**
  - New control model available at https://huggingface.co/alibaba-pai/Wan2.2-Fun-A14B-Control
  - *From: DawnII*

- **Context window support pull request submitted**
  - PR #9238 for ComfyUI to make it easier to experiment with context windows
  - *From: Kosinkadink*

- **New Lightning I2V LoRAs available**
  - Kijai converted versions available with different strength settings
  - *From: screwfunk*

- **Lightning LoRA versions updated**
  - Lightning 1.1 version released but may have quality issues compared to 1.0
  - *From: WorldX*

- **Wan 2.2 Fun Control and InP models released**
  - New models supporting control conditions (Canny, Depth, Pose, MLSD) and temporal inpainting, supporting up to 81 frames at multiple resolutions
  - *From: CJ*

- **Kijai released fp8 scaled versions of Fun models**
  - Available at 14.5GB instead of 28.6GB for better VRAM compatibility
  - *From: Kijai*

- **5B version of Fun models coming**
  - Based on code branch analysis, a 5B parameter version is expected
  - *From: DawnII*

- **SkyReels A3 demo revealed**
  - New model showing impressive singing and camera control capabilities, paper available on arXiv
  - *From: DawnII*

- **Wan Chattable Knowledge Base updated with 2.2 conversations**
  - NotebookLM knowledge base now includes Wan 2.2 discussion, accessible via provided link
  - *From: Nathan Shipley*

- **WAN wrapper nodes updated with fixes**
  - Fixed tensor size issues in Fun Control, removed unused clip vision connections
  - *From: Kijai*

- **Automatic CFG implementation added**
  - Added automatic CFG calculation per step based on cond/uncond ratio, following arxiv.org/abs/2508.03442
  - *From: Kijai*

- **Wan 2.2 Fun A14B Control models released**
  - New control models available on HuggingFace alibaba-pai repo
  - *From: Dannhauer80*

- **Possibility of 8-step Lightning model**
  - Discussion on GitHub about potential 8-step model development
  - *From: DawnII*

- **DiffSynth Studio commit supports arbitrary sequence length**
  - Recent commit adds support for variable length sequences
  - *From: fredbliss*

- **Kijai updated FP8 fast support**
  - Overhauled loader node, scaled + fast works with merged LoRAs, faster on 5090 than 4090
  - *From: Kijai*

- **Torch 2.8.0 now in stable release**
  - Kijai updated to torch 2.8.0 and latest triton, fp8_fast seems faster than before
  - *From: Kijai*

- **New FastWan2.2-TI2V-5B-FullAttn model released**
  - Available on HuggingFace in diffusers format
  - *From: SonidosEnArmonía*

- **FastWan LoRA extracted for 5B model**
  - Available in Kijai's repository
  - *From: Kijai*

- **Radial attention now supports WAN 2.2**
  - Updated attention code with 0 dense timesteps and decay factor of 1
  - *From: MysteryShack*

- **ComfyUI training nodes RFC in progress**
  - RFC discussion for generic training node implementation
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Qwen Image Lightning released**
  - 8-step distilled model for Qwen image generation, works with 4 steps too, doesn't ruin style like Wan version
  - *From: hicho*

- **VACE 2.2 developers working on update**
  - Kijai mentioned hearing that VACE developers are working on an update, though not confirmed officially
  - *From: JohnDopamine*

- **ComfyUI now in top CG academia/companies**
  - ComfyUI course at SIGGRAPH 2025 conference, showing mainstream academic adoption
  - *From: Christian Sandor*

- **New Fun 2.2 control model available**
  - 5B controlnet model with improved capabilities but lost reference input support
  - *From: Kijai*

- **PUSA fix pushed to repository**
  - Fix for something that was broken in previous commit
  - *From: Kijai*

- **DeepVerse world model released**
  - Sunday release of new world model, though lightweight with 4 FPS on A800
  - *From: DawnII*

- **FastWan 5B released**
  - Available for few days, works with controlnet
  - *From: Kijai*

- **Official Flash version announced**
  - Claims 12x faster than Wan 2.1, release imminent
  - *From: 青龍聖者@bdsqlsz*

- **5B controlnet support added**
  - Traditional depth controlnet now works with 5B model
  - *From: Kijai*

- **Skyreels LoRA extracted and available**
  - Can help break 121 frame loop limitation in 2.2
  - *From: Kijai*

- **Official Lightning LoRA announced**
  - Official one was announced today, maybe best to wait for that
  - *From: Kijai*

- **Wan 2.2 Fun A14B InP in training**
  - Model is currently in training phase
  - *From: yi*

- **Rapid AllInOne 2.2 v6 released**
  - v6 came today, merges both high/low models into one
  - *From: Drommer-Kille*

- **Prefetch option added to block swap**
  - New prefetch option available for block swap with debug option to confirm transfer speeds
  - *From: Kijai*

- **FAL now has Wan 2.2 14B LoRA trainer**
  - Available at https://fal.ai/models/fal-ai/wan-22-image-trainer
  - *From: Drommer-Kille*

- **New Stand-In identity control method released**
  - Lightweight plug-and-play identity control for video generation, 600MB LoRA
  - *From: s2k*

- **Block swap optimization implemented**
  - Recent changes make block swapping faster than before by a good margin
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Matrix Game 2.0 from Skyreels released**
  - Video + camera control model, feels like 'video model, half world model'
  - *From: JohnDopamine*

- **Stand-In LoRA released**
  - 600MB LoRA for face consistency, works like ID adapter, runs for one step using KV cache
  - *From: Kijai*

- **StableAvatar released from Microsoft Asia**
  - New lip-sync solution, appears to be trained on Fun model
  - *From: DawnII*

- **Fantasy Portrait weights available**
  - FantasyPortrait model weights now available on HuggingFace
  - *From: NebSH*

- **Multiple lip-sync releases in 48h**
  - Fantasy talking, StableAvatar, Pika new lipsync, and StandIn lora all released recently
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Stand-in LoRA now compatible with GGUF models**
  - Latest update fixed using GGUF models with Stand-in, allows SageAttention without errors
  - *From: garbus*

- **FFv1 support merged into VideoHelperSuite**
  - Allows lossless storage of picture collections as videos with workflow as mkv files
  - *From: thaakeno*

- **A3 (Skyworks) confirmed no plans to release in open source**
  - Contact with A3 team confirmed they won't open source the model
  - *From: NebSH*

- **LightX2V team acknowledged aesthetic issues in Wan 2.2 Lightning**
  - Team responded to feedback about aesthetic problems, may release 8-step version
  - *From: DawnII*

- **New Stand-In reference model released**
  - Subject replacement model for Wan video generation
  - *From: Purz*

- **Wan 2.2 Fun Camera model released**
  - Posted 8 hours ago, provides camera control capabilities for Wan 2.2
  - *From: Kijai*

- **Fun 2.2 GGUF quantizations available**
  - GGUF quantized versions of Fun 2.2 models are now available
  - *From: DawnII*

- **Better sing performance models to be released**
  - Pretrained models with improved singing/lip sync performance are planned for release
  - *From: NebSH*

- **Genie 3 local release expected next week**
  - Around Genie 2 level quality expected for local deployment
  - *From: Juampab12*

- **Three new features released: Fun 2.2 camera control, Stand-In reference LoRA for 2.1 14B, and FantasyPortrait face motion transfer**
  - Multiple new capabilities added to the ecosystem
  - *From: Kijai*

- **ComfyUI started implementing context windows natively for Wan**
  - Native ComfyUI support being developed
  - *From: Lodis*

- **Fun models now available in native ComfyUI in latest update**
  - Official ComfyUI integration
  - *From: Drommer-Kille*

- **Released Wan 14B 2.2 version of goldenboy retro anime style LoRA**
  - Includes detailed training process documentation
  - *From: crinklypaper*

- **Stand-in workflow updated and pushed to main**
  - Mostly working, attention masking for multiple people not added yet
  - *From: Kijai*

- **Fantasy Portrait updated with bug fixes**
  - Fixed variable naming error (z to x) and added progress bar for long encodes
  - *From: Kijai*

- **Fun 2.2 example workflow updated**
  - Fixed issues with 153 input frames causing overblown first frame
  - *From: Kijai*

- **Alibaba released camera control model for Wan 2.2**
  - Wan2.2-Fun-A14B-Control-Camera released recently, allows camera control via nodes instead of prompts
  - *From: Lodis*

- **GGUF versions available for Wan 2.2 Fun models**
  - QuantStack released GGUF versions, Fun INP works but Camera Control has issues
  - *From: Daflon*

- **WanVideoWrapper updated to fix dependency issues**
  - Kijai updated to catch exceptions and fix FantasyPortrait dependency problems
  - *From: Kijai*

- **Added bbox and landmark detection visualization to Fantasy Portrait**
  - New visualization features for 222 keypoints detection, less guesswork if it's working
  - *From: Kijai*

- **Added projection scaling controls for Fantasy Portrait**
  - Can now scale mouth, emotion, and adapter projections separately
  - *From: Kijai*

- **Fantasy Portrait branch not merged to main yet**
  - Need to switch branches to access Fantasy Portrait functionality
  - *From: A.I.Warper*

- **Added warning detection for fp8e4nv incompatibility with RTX 3090**
  - Will warn users about quantization compatibility issues
  - *From: Kijai*

- **New denoise method research paper released**
  - Arxiv paper on potentially faster video generation algorithms
  - *From: shockgun*

- **Wan 2.2 Flash teased by Alibaba**
  - Question about whether it will be open sourced
  - *From: Cseti*

- **Tencent dipping into Wan with ToonComposer**
  - New development in the Wan ecosystem
  - *From: DawnII*

- **Dino v3 announcement**
  - New version released
  - *From: LarpsAI*

- **i2v-Flash officially released**
  - Official release from Alibaba, appears to be paid only initially
  - *From: 642326806678077441*

- **Context windows now available in native Wan implementation**
  - Manual nodes available for testing, with hooks for ContextHandler
  - *From: Kosinkadink*

- **ToonComposer from Tencent using Wan model**
  - Professional implementation for keyframe animation, supports inbetween frames
  - *From: GOD_IS_A_LIE*

- **Flash-attn v2 wheels released for PyTorch 2.8**
  - Fixes compatibility issues that previously required uninstalling
  - *From: phazei*

- **StableAvatar finetuning and lora training codes released**
  - Released finetuning codes and lora training/finetuning codes for Wan2.1-Fun-V1.1-1.3B-InP, supports infinite-length videos at 480x832, 832x480, or 512x512 resolution
  - *From: NebSH*

- **WanFM inference optimization method discovered**
  - New method does start-to-end prediction, then end-to-start prediction and blends them together each step, but takes twice the sampling time
  - *From: Kijai*

- **Fantasy Portrait branch merged into main**
  - Main branch is now more recent, deleted the other branch to avoid confusion
  - *From: Kijai*

- **Nunchaku coming to Wan for 3+ months**
  - Expected to provide speed improvements similar to what they did for Flux
  - *From: Kijai*

- **New WanFM (Frame Morphing) sampling method released**
  - Model-agnostic bidirectional sampling method that samples forward and reverse on each step
  - *From: Kijai*

- **ComfyUI frontend changes affect bypassed nodes**
  - Recent updates now pass data through bypassed/muted nodes, breaking existing workflows
  - *From: phazei*

- **Fixed RoPE implementation for WanFM**
  - Kijai fixed the RoPE reverse issue that was causing jittery results on low noise side
  - *From: Kijai*

- **Fixed Fun-Control models for fp8 compatibility**
  - Updated models on HF repo to fix ref_conv layer issue with fp8 scaled models
  - *From: Kijai*

- **Phantom VACE fp16 full weights model released**
  - Piblarg shared full fp16 model for GGUF conversion
  - *From: Piblarg*

- **Matrix Game 2.0 interactive model based on Wan released**
  - Interactive model from Skywork based on Wan using self-forcing training technique, trained on GTA
  - *From: hicho*

- **Nunchaku team working on Wan quantization**
  - Nunchaku team indicated they are starting work on Wan model quantization
  - *From: aikitoria*

- **WanFM implementation added to main branch**
  - Though barely any difference vs using 2.2 normally, all examples can be done with plain 2.2
  - *From: Kijai*

- **Dev branch now uses less RAM when not merging LoRAs**
  - Potentially 20GB less RAM usage, model loader doesn't load when not merging
  - *From: Kijai*

- **14B VACE Phantom v2 GGUF models available**
  - Multiple sizes available on HuggingFace
  - *From: orabazes*

- **Phantom + MultiTalk combination fixed**
  - Now working with context windows
  - *From: Kijai*

- **Bidirectional sampling fix merged**
  - PR #9392 merged to fix OOM issues with bidirectional sampling
  - *From: Kosinkadink*

- **Topaz Starlight-Mini available**
  - New diffusion-based video upscaler, slow but high quality
  - *From: . Not Really Human .*

- **InfiniteTalk repository made public then privatized again**
  - Was available for 30 minutes before being pulled, repo duplicated at github.com/bmwas/InfiniteTalk but without weights
  - *From: JohnDopamine*

- **Kijai made fp8_scaled version of MAGREF available**
  - Both fp8_e4m3fn and fp8_e5m2 scaled versions released
  - *From: Kijai*

- **New video grid creation node added to KJNodes**
  - Uses VHS nodes and requires VHS to be installed to work
  - *From: Kijai*

- **InfiniteTalk release confirmed for tomorrow**
  - Will be compatible with existing MultiTalk workflows by changing model
  - *From: NebSH*

- **MTV Crafter hardcoded to 49 frames only**
  - Cannot work with 81 frames as previously thought
  - *From: Kijai*

- **CineTrans released for scene transitions**
  - 1.3B LoRA only model for scene transitions, does timesteps manipulation along with weights
  - *From: Kijai*

- **Qwen image edit model released**
  - Edit model is available but not supported in ComfyUI yet, missing components for usage
  - *From: Kijai*

- **Add Memory to Reserve node added**
  - New node in node-memory-reserve branch to reserve additional memory for models
  - *From: Kosinkadink*

- **InfiniteTalk released with ComfyUI support**
  - Same developers as MultiTalk, official repo and HuggingFace models available
  - *From: JohnDopamine*

- **VHS Load Video node updated with drag and drop functionality**
  - AustinMroz contributed the drag and drop feature
  - *From: JohnDopamine*

- **FastWan distillation available for 5B model**
  - Speed optimization for 5B model available in Kijai's repo
  - *From: TK_999*

- **InfiniteTalk released with ComfyUI support**
  - New lip sync model from MultiTalk authors, available in single and multi versions
  - *From: NebSH*

- **Qwen Image Edit ComfyUI implementation available**
  - New image editing model with ComfyUI wrapper released
  - *From: Lodis*

- **MeiGen-AI forked KJ's wrapper**
  - Created their own ComfyUI branch but conflicts with original wrapper
  - *From: Kijai*

- **InfiniteTalk models released**
  - Single and Multi person versions available in fp8_scaled format, updated MultiTalk with infinite generation capability
  - *From: Kijai*

- **MAGREF integration with InfiniteTalk**
  - MAGREF now works with InfiniteTalk for better character consistency
  - *From: Kijai*

- **Fixed merged LoRA issues with scaled models**
  - Updated code to support merged LoRAs with fp8_scaled models
  - *From: Kijai*

- **InfiniteTalk Q8 GGUF model released**
  - Took some trickery to convert but works - new Q8 GGUF version available
  - *From: Kijai*

- **MTVCrafter model mentions FusionX LoRA**
  - New model on HuggingFace mentions FusionX lora in documentation
  - *From: Dream Making*

- **Removed precision setting in multitalk loader**
  - Precision setting was redundant and has been removed
  - *From: Kijai*

- **InfiniteTalk Q4 and Q6 GGUF quantizations released**
  - Added Q4 and Q6 versions to HuggingFace repo
  - *From: Kijai*

- **Uni3c node updated for automatic video processing**
  - Modified uni3c node to work without manual latent input when using multitalk sampling
  - *From: Kijai*

- **ComfyUI UI changed refresh method**
  - Refresh nodes option moved from dropdown menu to 'R' shortkey
  - *From: CJ*

- **WanWrapper updated with multitalk improvements**
  - KJ updated wrapper this morning with improvements to multitalk functionality
  - *From: ArtOfficial*

- **LightX2V team acknowledges static face issue**
  - LightX2V developers acknowledge the issue with static faces and are working on proper distill LoRA
  - *From: Kijai*

- **TREAD technique for faster diffusion training**
  - Claims 37x speedup, implemented by feffy380, should make training Wan much faster
  - *From: Ada*

- **New TLBVFI interpolation method released**
  - ComfyUI implementation available, claims to be better than RIFE with latent space processing and 7 interpolated frames
  - *From: JohnDopamine*

- **Wan 2.2 Fun 5B Control released**
  - Hugging Face release of the control version
  - *From: DawnII*

- **KJ updated wrapper to automatically handle MultiTalk/InfiniteTalk video input**
  - Latest commit allows pulling and splicing from multitalk/infinitetalk input video automatically to replicate what meigen did in their fork
  - *From: DawnII*

- **Alibaba released whole suite of Fun models for 5B**
  - New Fun Control models released for the 5B Wan2.2 variant
  - *From: Kijai*

- **Added InfiniteTalk GGUF support**
  - Support for GGUF InfiniteTalk models was added to the nodes yesterday
  - *From: Kijai*

- **Added latent counter helper node for easier trimming**
  - New node added to make trimming latents easier in workflows
  - *From: Kijai*

- **Lumen model released**
  - 1.3B text-to-video model from Kunbyte, background replacement and relighting capabilities
  - *From: DawnII*

- **WanVideoWrapper updated with InfiniteTalk V2V support**
  - New streamlined workflow with faster sampling speeds
  - *From: Kijai*

- **Fun Control 5B model works with existing workflows**
  - Same workflow as 14B version, supports pose control
  - *From: Kijai*

- **GGUF VACE modules now supported**
  - Can load GGUF VACE modules, available on HuggingFace
  - *From: Kijai*

- **InfiniteTalk encode node added**
  - New node for InfiniteTalk workflow
  - *From: Kijai*

- **Auto-detection from filename for InfiniteTalk mode**
  - Mode automatically detected from file name
  - *From: Kijai*

- **Prompt travel feature added**
  - Can use prompts separated by | for different sections
  - *From: Kijai*

- **Preview Actual Frames output added**
  - New output added in latest push
  - *From: Kijai*

- **Kijai fixed differential diffusion in wrapper inpainting**
  - Was in wrong place for a year, now working properly with significant improvement
  - *From: Kijai*

- **PUSA developer training Wan2.2 version mentioned 2 weeks ago**
  - In process of training according to GitHub issue
  - *From: JohnDopamine*

- **Ostris released Wan2.2 orbit shot LoRA on HuggingFace**
  - Training took days even with 96GB VRAM in RunPod
  - *From: Drommer-Kille*

- **New Wan2.2-Fun-A14B-InP model released**
  - Supports temporal inpainting only, like first to last frame and in-between frames
  - *From: Zabo*

- **VACE inpainting differential diffusion code fixed**
  - Results improved significantly - before result was poor, now working much better
  - *From: Kijai*

- **Multiple VACE usage bug fixed**
  - Bug when using multiple VACEs in workflow has been resolved
  - *From: Kijai*

- **WanVideoWrapper updated with fixes**
  - Recent commits include fixes for various issues
  - *From: Kijai*

- **CineScale LoRA released for 4K upscaling**
  - 307MB LoRA files available on HuggingFace, uses cascading sampling approach
  - *From: MilesCorban*

- **Waver video model paper released by ByteDance**
  - Supports 10-second videos, 12B parameter model, but appears to be proprietary
  - *From: NebSH*

- **EasyCache and LazyCache implemented natively in ComfyUI**
  - New PR supports almost all models, LazyCache for cases where EasyCache performs poorly
  - *From: Kosinkadink*

- **Wan 2.2 5B Turbo model released**
  - Available in Kijai's HuggingFace repo, 4 steps, cfg 1.0, significant speed improvement
  - *From: Kijai*

- **Unofficial Wan 2.2 5B Turbo released**
  - Available at quanhaol/Wan2.2-TI2V-5B-Turbo on HuggingFace, beat the lightx2v lightning team to it
  - *From: DawnII*

- **Tiny VAE for 2.2 may be coming**
  - GitHub issue discussion about taehv implementation
  - *From: Prelifik*

- **CineScale LoRA released**
  - New LoRA for 4K video upscaling came out, available on GitHub
  - *From: Kijai*

- **ComfyUI masked conditioning fix merged**
  - Fix for masked conditioning issue with video latents merged 15 minutes ago
  - *From: Kosinkadink*

- **Sliders for Wan 2.1 & 2.2 coming next week**
  - Release expected for parameter sliders similar to baulab sliders
  - *From: phazei*

- **VACE 2.2 expected in July**
  - Release date mentioned for VACE 2.2 version
  - *From: JohnDopamine*

- **UniAnimate now works with unmerged LoRAs and GGUF**
  - Also works with Multi/InfiniteTalk long generation
  - *From: Kijai*

- **Added logging to CFG scheduler node**
  - Now displays the generated CFG list like image resize node
  - *From: Kijai*

- **GGUF Multi versions of InfiniteTalk uploaded**
  - Available at https://huggingface.co/Kijai/WanVideo_comfy_GGUF/tree/main/InfiniteTalk
  - *From: Kijai*

- **MelBandRoFormer vocal separation wrapped for ComfyUI**
  - New audio separation tool available
  - *From: Kijai*

- **PUSA LoRA for Wan 2.2 is being worked on**
  - In development for about 3 weeks
  - *From: hicho*

- **FantasyPortrait now works with multi/infinite talk loop**
  - Integration allows combining head movements with lip sync
  - *From: Kijai*

- **VAE cache memory leak fix in development**
  - Fix for InfiniteTalk VAE cache not clearing between windows
  - *From: Kijai*

- **Wan Nunchaku support coming**
  - Nunchaku confirmed successful backend migration, focusing on video models, expected end of August
  - *From: flo1331*

- **New WanVideoAddControlEmbeds node**
  - Alternative to previous control node that requires empty embeds input
  - *From: Kijai*

- **Added helper for LoRA strength scheduling**
  - New node for scheduling LoRA strength, useful for bypassing LoRA on certain steps
  - *From: Kijai*

- **VACE 2.2 is being worked on**
  - Confirmation that VACE 2.2 development is in progress
  - *From: Kijai*

- **Set/Get nodes may come to ComfyUI core**
  - Potential integration of set/get functionality into native ComfyUI
  - *From: Nekodificador/Kijai*

- **New cloth adapter + controlnet repo discovered**
  - Month or two old repo with dense pose controlnet and clothing replacement for Wan
  - *From: Kijai*

- **Fixed temporal mask casting error in image encoding**
  - Reduced memory usage by half in the process
  - *From: Kijai*

- **NYC meetup featuring WAN 2.2 presentation**
  - Community meetup with presentation focused on WAN 2.2 and community contributions
  - *From: The Shadow (NYC)*

- **Wan 2.2 S2V (Sound to Video) announced**
  - New capability coming soon, appears to be lip sync or audio-driven generation
  - *From: Abx*

- **New anime style LoRA for Wan 2.2 released**
  - Community creation with detailed writeup on the process
  - *From: crinklypaper*

- **Dev version of wrapper nodes released with refactored model loading**
  - Complete refactor of model loading system
  - *From: Kijai*

- **Wan 2.2 S2V (Speech to Video) model announced**
  - Similar to InfiniteTalk, also supports music-driven video, uses pose video reference and motion encoder similar to UniAnimate
  - *From: Kijai*

- **New Wan model info released but not live yet**
  - Uses Frame pack method, has causal self attention, pose control + audio control with frame pack sampling
  - *From: Kijai*

- **Wan 2.2 S2V model released**
  - Speech-to-video model, 14B and 5B variants available on HuggingFace, single model (not MoE)
  - *From: DawnII*

- **Kijai merged dev to main branch**
  - Merged due to maintenance overhead, model loading now always from disk, may break things but saves RAM
  - *From: Kijai*

- **New VAE only for 5B model**
  - There's a new VAE specifically for the 5B variant
  - *From: daking999*

- **Wan 2.2 S2V model released**
  - Speech-to-video model available on HuggingFace
  - *From: Impactframes*

- **ComfyUI native audio encoder nodes available**
  - New native nodes for audio encoding in ComfyUI
  - *From: Kijai*

- **ComfyUI NYC meetup hosting special Wan2.2 event**
  - Special event for Wan2.2 in New York area
  - *From: ericxtang*

- **S2V branch available for testing**
  - S2V functionality added to WanVideoWrapper, work in progress with audio generation and ref image support but no long generation method yet
  - *From: Kijai*

- **Major merge to main repository**
  - Pretty big update today, can roll back to version 1.3.1 if issues occur
  - *From: Kijai*

- **Nano Banana by Google available**
  - Google's Gemini-based image editing tool, free during preview, good for dataset creation
  - *From: DawnII*

- **ComfyUI native WAN S2V implementation released**
  - Work-in-progress native implementation available for testing, includes control video input
  - *From: comfy*

- **WAN S2V model ships as bf16 format**
  - The official S2V model uses bf16 compute dtype instead of fp16
  - *From: comfy*

- **New AniSora V3 model released**
  - https://huggingface.co/IndexTeam/Index-anisora/tree/main/V3
  - *From: DreamWeebs*

- **Lightning LoRAs for Wan 2.2 still in development**
  - new lightx loras are still a while away https://huggingface.co/lightx2v/Wan2.2-Lightning/discussions/30
  - *From: Karo*

- **ComfyUI fix for S2V audio conditioning**
  - reading this channel also made me realize I wasn't setting the negative audio to zero. now it is so it might work better
  - *From: comfy*

- **Wan team mentions ComfyUI on X**
  - On X Wan they mention Comfy. https://x.com/Alibaba_Wan/status/1956250711198765362
  - *From: Tony(5090)*

- **ComfyUI merged S2V support**
  - Official ComfyUI now has S2V nodes merged into main branch
  - *From: comfy*

- **HunyuanVideo-Foley released**
  - New audio generation model from Tencent for video, appears to be based on MMAudio
  - *From: JohnDopamine*

- **Waver 1.0 announced by Bytedance**
  - Was meant to be open source but they changed their minds
  - *From: Gill Bastar, Rainsmellsnice*

- **HunyuanVideo-Foley released**
  - New audio generation model from Tencent, uses 4-5 models (sigclip, vae, transformer, syncformer), similar performance to MMAudio
  - *From: Karo*

- **S2V branch updated with new workflow**
  - Updated S2V branch with framepack implementation and test workflow
  - *From: Kijai*

- **Unofficial VACE 2.2 merge available**
  - Hacked together merge of 14B VACE models, not official release
  - *From: DawnII*

- **Updated S2V model with smaller file size and better quality**
  - New S2V model is ~2GB smaller with audio injection layers in fp8 and pose conditioning fixed to not be in fp8
  - *From: Kijai*

- **S2V framepack working in both native ComfyUI and wrapper**
  - Framepack feature from S2V now implemented, but has its own weights so only works with S2V model
  - *From: Kijai*

- **Fixed overbaked first frame issue in native S2V workflow**
  - Updated native S2V workflow addresses the overblown first frame problem
  - *From: comfy*

- **GGUF offloading code added to S2V**
  - DawnII copied the GGUF offloading code from main branch to s2v branch, helps significantly with memory usage
  - *From: DawnII*

- **e5m2 GGUF version of S2V uploaded**
  - Kijai uploaded the e5m2 version to HuggingFace at Kijai/WanVideo_comfy_fp8_scaled/tree/main/S2V
  - *From: Kijai*

- **Recent changes to ComfyUI-WanVideoWrapper**
  - Fixes for model loading bugs with merged LoRAs and other memory-related improvements
  - *From: Kijai*

- **Block prefetch feature change rolled back**
  - A change to block prefetch feature caused issues on some systems and was rolled back
  - *From: Kijai*

- **Framepack technology activated in S2V**
  - Framepack technology from S2V technical report has been activated and is available
  - *From: Kijai*

- **ComfyUI has RAM usage improvements in latest stable**
  - For Windows users on PyTorch 2.8
  - *From: comfy*

- **New audio volume control node added to wrapper**
  - Multi and InfiniteTalk default to -23 lufs
  - *From: Kijai*

- **PyTorch 2.8 available with improved RAM usage**
  - New pytorch update helps with memory management, reduces swap file usage
  - *From: hicho and comfy*

- **Torch compile fix published**
  - Fixed version published that survives prompt being changed
  - *From: phazei*

- **CineScale already optimized for wrapper**
  - CineScale from Netflix has been available and working in wrapper for weeks
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Kijai joining comfy-org**
  - I'll be working for comfy-org, and at least initially allocate half of my time on that, technically they said they just want me to keep doing what I'm doing, but I do want to do more like native implementations
  - *From: Kijai*

- **S2V merged to main in wrapper**
  - Merged S2V to main in the wrapper and fixed bunch of bugs
  - *From: Kijai*

- **Pusa-Wan2.2-V1 model coming soon**
  - Found repo on HuggingFace but it was deleted, suggesting imminent release
  - *From: asd*

- **Native S2V nodes available**
  - Native S2V nodes are now in core ComfyUI
  - *From: ArtOfficial*


## Workflows & Use Cases

- **VACE 2.2 with openpose controlnet**
  - Use case: Style transfer and character animation with pose control
  - *From: GOD_IS_A_LIE*

- **2 sampler approach vs custom single node**
  - Use case: Comparing dual sampler workflow against custom combined sampler implementation
  - *From: VRGameDevGirl84(RTX 5090)*

- **VACE I2V chaining with T2V start**
  - Use case: Creating long videos with smooth transitions using 5 I2V sections fed from initial T2V
  - *From: seitanism*

- **Multi-scene generation with context windows**
  - Use case: Creating videos with multiple scenes using | separator in prompts
  - *From: thaakeno*

- **VACE upscaling with WAN 2.2**
  - Use case: Using WAN 2.1 VACE then upscaling with WAN 2.2 high noise at 2 steps by 1.5x factor
  - *From: GOD_IS_A_LIE*

- **Fast video preview with frame dropping**
  - Use case: Drop frames by 2-3, generate quickly, then interpolate and refine with high start step
  - *From: thaakeno*

- **Multi-scene generation with context windows**
  - Use case: 4 scenes in two context windows using | separator between prompts
  - *From: Cseti*

- **AMD ZLUDA setup for WAN**
  - Use case: Successfully running on AMD Radeon 8060S with 20 minute generation times for 1280x704 121 frames
  - *From: nacho.money*

- **Two-stage resolution workflow**
  - Use case: Generate at 640x352 then upscale to 1280x704 for better performance and quality balance
  - *From: nacho.money*

- **3-stage sampling for I2V**
  - Use case: Better quality I2V generation with 9 steps: 3H no Lora, 3H LightX2V@3, 3L@1
  - *From: BobbyD4AI*

- **Multi-resolution generation**
  - Use case: 2 high noise passes and then low noise pass to finish, from 3 different resolutions
  - *From: Kijai*

- **Character LoRA training**
  - Use case: 59min training with high noise model, tested at 18 steps high, 2 steps low
  - *From: Kenk*

- **Three sampler setup for quality**
  - Use case: No lora on first sampler with higher steps and high CFG, second pass high lora 3.0 and CFG 1, third sampler 1.0 lora and CFG 1
  - *From: Simjedi*

- **Four sampler setup**
  - Use case: 2/2/4/4 step distribution using kjsampler
  - *From: Simjedi*

- **Context window splitting with stride**
  - Use case: Splitting 5B context window to 2 samplers for smoothing
  - *From: Kijai*

- **Manual frame-based prompt scheduling**
  - Use case: Camera movement control by specifying actions at specific frame numbers in regular positive prompt
  - *From: Bleedy (Madham)*

- **Video encoding for V2V**
  - Use case: Load video, encode with VAE Encode node, send latent as input latent for video-to-video
  - *From: Ablejones*

- **Context window setup for long videos**
  - Use case: Use different context settings for high and low noise models to improve blending
  - *From: Kijai*

- **Multi-stage T2V generation with different resolutions**
  - Use case: Better motion at lower res, then upscale for final quality
  - *From: Kijai*

- **Generate 640x352 then scale to 1280x704**
  - Use case: For slower hardware, faster iteration on disappointing gens
  - *From: nacho.money*

- **V2V upscaling workflow for quality enhancement**
  - Use case: Upscaling 480p to 1080p while fixing details like LED lightbars
  - *From: thaakeno*

- **MMaudio integration with RIFE interpolation**
  - Use case: Generate 16fps, interpolate to 25fps for audio sync
  - *From: thaakeno*

- **High + Low + Low refinement**
  - Use case: Using high model, then low model twice with latent fan denoise 0.5, start step 0, end -1, step 6
  - *From: avataraim*

- **V2V upscaling with Wan 14B**
  - Use case: Upscaling videos while preserving content using high start step
  - *From: thaakeno*

- **FLF with native Wan 2.2 I2V**
  - Use case: Creating transitions between first and last frames
  - *From: Juampab12*

- **First-Last-Frame to Video (FLF2V)**
  - Use case: Creating videos with specific start and end frames, 10 second generations work well
  - *From: comfy*

- **T2I workflow based on Wan 2.2**
  - Use case: 1344x768 in 5sec, 2nd pass x2 upscaling to 2688x1536 in 4sec
  - *From: N0NSens*

- **Native first last image implementation**
  - Use case: Using ComfyUI native nodes for first/last frame conditioning
  - *From: Juampab12*

- **Three K-sampler setup**
  - Use case: Mix steps without LoRA and with LoRA for best of both worlds
  - *From: TK_999*

- **Video upscale and motion fix**
  - Use case: Feed video latent to high-noise model with start step control for upscaling/motion fixing
  - *From: thaakeno*

- **Parallel video generation**
  - Use case: Generate multiple videos simultaneously for efficiency
  - *From: Fill*

- **Combined MMAudio and Wan 2.2 workflow**
  - Use case: Single workflow for video generation with audio synthesis
  - *From: thaakeno*

- **Three sampler approach for Wan 2.2**
  - Use case: First step with no lightx and cfg, then lightx with 1 cfg for remaining steps
  - *From: Draken*

- **High resolution generation with latent upscale**
  - Use case: Run HIGH at lower res, then latent upscale for LOW noise processing
  - *From: Draken*

- **14B to 5B upscaling pipeline**
  - Use case: Decode 14B video, encode with VAE 2.2, feed to 5B with same starting frame and 0.3-0.5 denoise
  - *From: Juan Gea*

- **FPS1 storyboarding approach**
  - Use case: Generate videos at 1 FPS, then use other models to fill in-between frames for longer scenes
  - *From: mamad8*

- **Three-sampler approach with euler reset**
  - Use case: Add single euler step when switching to LN model to avoid multistep sampler artifacts
  - *From: Ablejones*

- **First frame last frame morphing**
  - Use case: Using FPS1 LoRA for temporal consistency in guided generation
  - *From: Fill*

- **Multi-stage generation with LoRA scheduling**
  - Use case: Use cfg for first steps without LoRA, then enable lightx2v for remaining steps
  - *From: Kijai*

- **Upscaling pipeline**
  - Use case: Generate 1600x960 with 14B, then upscale to 3072x1840 with 5B using block swap 30
  - *From: Juan Gea*

- **Hires fix approach with high/low models**
  - Use case: 4 steps each 0.5 denoise, 140sec gen time
  - *From: Daviejg*

- **Dockerized Wan 2.2 as serverless container**
  - Use case: Per-second billing with custom web UI dispatching jobs to H100 or 5090
  - *From: gokuvonlange*

- **Two-pass generation with LightX LoRA**
  - Use case: First pass normal generation, second pass with LightX at 0.5 strength for added detail
  - *From: VRGameDevGirl84(RTX 5090)*

- **High noise without LoRA, then low noise with LightX**
  - Use case: Better prompt comprehension while maintaining speed benefits
  - *From: Ablejones*

- **4 high noise steps with CFG, 3 scheduled steps, 6 low noise steps**
  - Use case: Sweet spot for quality vs speed with 2.2
  - *From: Ada*

- **3 samplers: high no LoRA, high with LoRA, low with LoRA**
  - Use case: When you can't use LoRA scheduling but need flexibility
  - *From: Kijai*

- **Dual LoRA training for Wan 2.2 with different timesteps**
  - Use case: Training both high and low noise experts with same dataset but different timestep ranges
  - *From: Kijai*

- **Using old 2.1 LoRAs on 2.2 low noise + training only high noise**
  - Use case: Easier migration path - use existing 2.1 LoRAs on low, only train new high noise LoRA
  - *From: crinklypaper*

- **Hybrid LoRA approach for T2V**
  - Use case: Use new lightning LoRA on high noise side only, old lightx2v or other LoRAs on low noise side for styling
  - *From: Kijai*

- **CFG staging for better lighting**
  - Use case: Start with 1 CFG 3.5 step without LoRA to set tone, then use CFG 1 with LoRAs for remaining steps
  - *From: IceAero*

- **Mixed LoRA generation workflow**
  - Use case: 4-step generation using old 2.1 LoRA on high noise, new Lightning on low noise
  - *From: Doctor Shotgun*

- **CFG scheduling with Lightning**
  - Use case: First step CFG 3.5 no LoRA, remaining steps CFG 1.0 with Lightning LoRA
  - *From: Ablejones*

- **Two-pass upscaling with 14B+5B**
  - Use case: Achieving higher resolutions like 3072x with limited VRAM
  - *From: Juan Gea*

- **Multi-pass Lightning setup**
  - Use case: Optimized quality with Lightning LoRAs
  - *From: Ablejones*

- **Prompt batching for variety**
  - Use case: Generating large variety of test content quickly
  - *From: Purz*

- **3-3-3 split with 2 different high models**
  - Use case: 3 steps at 3 cfg with no lora, then 3 steps with lora into low model to preserve original motion before using lora
  - *From: flo1331*

- **ClownsharkSampler setup to minimize model calls**
  - Use case: About 30 seconds longer than KSampler but results look more fully sampled, less noisy video
  - *From: Ablejones*

- **Mixed loras approach**
  - Use case: Using both lightx and lightning loras together on different parts
  - *From: SonidosEnArmonía*

- **Ada's I2V workflow**
  - Use case: I2V with complex prompts, 10 steps, all 1 cfg, follows complex prompts well
  - *From: Ada*

- **Lightning+Lightx+CausVid combination**
  - Use case: Combining multiple loras for enhanced results
  - *From: garbus*

- **Homebrew Veo3 workflow**
  - Use case: Using wan2.2, lightx2v 2.1, Multitalk and mmaudio for complete video generation
  - *From: nacho.money*

- **Context concatenation for long videos**
  - Use case: Extending video generations with character consistency maintained across scenes
  - *From: kendrick*

- **Upscaling with Wan 2.2 14B using blockswapping**
  - Use case: Upscaling videos from 480p to 1080p on 24GB VRAM systems
  - *From: thaakeno*

- **I2V with stacked LoRAs**
  - Use case: High quality I2V using phantom fusionx + pusa + lightx2v LoRAs for better prompt following and motion
  - *From: Ada*

- **Wan 2.1 + 2.2 hybrid pipeline**
  - Use case: Better I2V results by doing single frame Wan gen, then building frame sequence with prompt for FLF workflows
  - *From: Josiah*

- **Frame interpolation using Wan**
  - Use case: Generate first video at 16 FPS with 41 frames, add gray frames between each, then regenerate at 81 frames for 32 FPS
  - *From: mamad8*

- **Qwen-Image to WAN I2V pipeline**
  - Use case: Generate high quality first frame with Qwen-Image, then animate with WAN I2V
  - *From: fredbliss*

- **Scene transition with dual reference images**
  - Use case: Use 2 reference images at different aspect ratios for scene cuts while maintaining character likeness
  - *From: Jonathan*

- **FFLF (First Frame Last Frame) setup for WAN 2.2**
  - Use case: Creating video sequences with defined start and end frames
  - *From: AJO*

- **Batch video generation**
  - Use case: Generate 20 videos in 6 minutes (49 frames each) for finding the best result
  - *From: Fill*

- **Qwen image to Wan I2V pipeline**
  - Use case: Generate layout with Qwen image, then refine with Wan to add details
  - *From: aikitoria*

- **T2V with reference consistency**
  - Use case: Using specific prompting techniques to get almost 100% consistent results with reference
  - *From: Jonathan*

- **Side-by-side reference technique for character consistency**
  - Use case: Maintaining character appearance across different scenes
  - *From: Juampab12*

- **VACE inpainting for fixing video artifacts**
  - Use case: Fixing 45-frame segments with face artifacts using mask and video input
  - *From: Wembleycandy*

- **Prompt splitting for scene changes using | separator**
  - Use case: Creating videos with multiple distinct scenes or transitions
  - *From: Kijai*

- **VACE strength scheduling with floats**
  - Use case: Better control over style transfer and composition
  - *From: Nekodificador*

- **Context window upscaling for high-res videos**
  - Use case: Upscaling 10s videos with Wan 14B on limited VRAM
  - *From: thaakeno*

- **Keyframe-based generation for longer sequences**
  - Use case: Take first frame as new keyframe, regen 5s scene change, repeat
  - *From: Josiah*

- **Two-stage generation with save/load latent**
  - Use case: Managing VRAM limitations by splitting high noise and low noise generation
  - *From: Mngbg*

- **VACE + 2.2 HN merged workflow**
  - Use case: Getting reference following with 2.2 motion quality
  - *From: Kijai*

- **Flux Krea + Wan 2.2 pipeline**
  - Use case: Generate initial image with Flux Krea at 1920x1088, downscale to 1280x676 for Wan, upscale final video with Topaz
  - *From: .: Not Really Human :.*

- **Using replace image in Batch node for inbetween frames with VACE**
  - Use case: Adding interpolated frames between VACE generations
  - *From: xwsswww*

- **V2V upscaler workflow for fixing distant faces**
  - Use case: Push to 1600x900x81 resolution and fix faces at distance using low denoise settings
  - *From: mdkb*

- **Phantom+VACE merge for character consistency with controlnet**
  - Use case: Reliable character control coming off screen with openpose following
  - *From: Piblarg*

- **VACE character swapping with Wan 2.2**
  - Use case: Replacing characters in videos using reference images and SAM2 points editor
  - *From: mdkb*

- **FlF2V with add noise for dreamy effects**
  - Use case: Creating smooth morphing transitions between images with dreamy effects using LoRAs
  - *From: piscesbody*

- **USDU upscaling for video**
  - Use case: Upscaling from 1280x768 to 2560x1536, fixes hands and hair details but may have background seams
  - *From: Persoon*

- **Beta I2V workflow for scene teleportation**
  - Use case: Teleporting characters between different scenes while maintaining likeness
  - *From: Juampab12*

- **First-frame-last-frame morphing workflow**
  - Use case: Video extension with close first frame matching
  - *From: Gavmakes*

- **Pre-step dark scene generation**
  - Use case: Three methods: add 3rd sampler for single step, schedule LoRA strength to 0.0 at first step, or use CFG schedule
  - *From: IceAero*

- **162 frames in single workflow**
  - Use case: Testing long video generation capabilities
  - *From: Josiah*

- **VACE/Phantom merge**
  - Use case: Reliable identity preservation with control
  - *From: Piblarg*

- **MultiShot with scene changes while retaining likeness**
  - Use case: Generating videos with camera movement and character consistency
  - *From: Josiah*

- **Batch rendering workflow**
  - Use case: Multiple simultaneous generations for users with large memory pools
  - *From: HeadOfOliver*

- **High resolution I2V generation**
  - Use case: 1536x768 native generation using Wan 2.2 with Lightning LoRA and quantized models
  - *From: : Not Really Human :*

- **Motion control with Lightning LoRA**
  - Use case: Using different high/low LoRA strength ratios to control motion speed
  - *From: CaptHook*

- **Uneven split generation**
  - Use case: Running high model full steps while only distilling low noise model for efficiency
  - *From: MysteryShack*

- **First-frame-last-frame morphing with Fun InP**
  - Use case: Creating smooth transitions between two keyframes with temporal inpainting
  - *From: SonidosEnArmonía*

- **VACE/Phantom merge workflow**
  - Use case: Combining VACE control with Phantom consistency for better results
  - *From: Piblarg*

- **Long-form generation with context stacking**
  - Use case: Creating 257+ frame videos using 121,4,40 context settings
  - *From: samhodge*

- **Batch processing with VLM automation**
  - Use case: Processing multiple images (e.g., 20 images) automatically using Qwen2.5VL to minimize manual intervention
  - *From: R.*

- **Matrix scene character replacement**
  - Use case: Converting Neo shots to gorilla using WAN 2.1 + VACE inpainting with reference consistency
  - *From: Nekodificador*

- **Style mixing without LoRAs**
  - Use case: Achieving different styles using WAN 2.2 prompting alone
  - *From: R.*

- **High noise to low noise handoff using denoised samples**
  - Use case: Better stage transition control
  - *From: MysteryShack*

- **V2V using encoded samples in sample slot**
  - Use case: Video to video generation
  - *From: Kijai*

- **VACE single frame controlnet to video**
  - Use case: Generate video from single controlnet depth map with prompt following and reference image support
  - *From: Lodis*

- **Qwen2.5VL with Wan2.2 for automated prompting**
  - Use case: Automatic prompt generation from reference images with memory-efficient caching
  - *From: Kijai*

- **Chained VACE nodes for better control**
  - Use case: Use two WanVaceToVideo nodes with positive/negative continuing to next, only last outputs latent
  - *From: Atlas*

- **Sapiens 7-stage pipeline**
  - Use case: Comprehensive pose detection: Detect → Crop → Inference → Refine → Filter → Track → Draw
  - *From: fredbliss*

- **Fun Control with Sapiens pose**
  - Use case: Using Sapiens-generated poses with VACE control system for better pose-driven video generation
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Complete End-to-End pose detection pipeline**
  - Use case: Multi-person tracking with temporal smoothing: Detect → Track → Crop & Pad → Sapiens Inference → Refinement → Filter → Smooth → Draw
  - *From: fredbliss*

- **Video to Video with Wan 2.2**
  - Use case: Custom V2V workflow implementation
  - *From: VRGameDevGirl84*

- **PUSA extension workflow**
  - Use case: Using PUSA LoRA with T2V model and extra_latents for extension without color shifting
  - *From: Hashu*

- **Clip in native, rest in wrapper**
  - Use case: Hybrid approach for Wan 2.2 processing
  - *From: Drommer-Kille*

- **Blender + Vace then Wan 2.2 V2V**
  - Use case: Two-stage process for enhanced realism - first pass with Vace, second pass with Wan 2.2 for added realism
  - *From: Drommer-Kille*

- **MultiTalk + MMAudio sync workflow**
  - Use case: Process MultiTalk at 16fps, 3x interpolate to 48fps, strip every other frame to 24fps for MMAudio sync
  - *From: nacho.money*

- **Fun InP with temporal masks and VACE start/end image node**
  - Use case: Video extension with keyframe control
  - *From: Kijai*

- **Point editor with ctrl + left click**
  - Use case: Creating control regions for Fun control
  - *From: Kijai*

- **Phantom object reference workflow**
  - Use case: Object continuity across scenes
  - *From: Juampab12*

- **Multi-sampler setup for lighting LoRA**
  - Use case: Using lighting LoRA with uneven H/L split
  - *From: Karo*

- **Using Wan 2.2 low noise as upscaler**
  - Use case: Fix faces at distance, upscale while maintaining structure
  - *From: mdkb*

- **Sliding context workflow for 2.2**
  - Use case: 8 and 4 split with dpm++_sde sampler, cfg 1, shift set to 8
  - *From: kendrick*

- **VACE with controlnets for v2v**
  - Use case: Change v2v using reference image and controlnets to change structure
  - *From: mdkb*

- **Multiple sampler scheduling**
  - Use case: Using 3+ samplers for better control, similar to cfg scheduling
  - *From: Kijai*

- **High/Low model workflow with scheduling**
  - Use case: 1 step high/low (lightning) + 2 step (old loras) configuration
  - *From: Josiah*

- **FFLF with Wan 2.2 Fun Inpaint**
  - Use case: First-Frame-Last-Frame morphing workflow
  - *From: R.*

- **Decode-upscale-encode for higher resolution**
  - Use case: Upscaling generated videos
  - *From: Kijai*

- **Using WanImageToVideo encode for I2V**
  - Use case: Converting T2V workflow to I2V
  - *From: patientx*

- **VACE inpainting workflow**
  - Use case: Selective video editing with masking control
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Wan 5B upscaling pipeline**
  - Use case: Upscale 14B output by resizing then V2V with 5B at 0.35-0.5 denoise, can use I2V to guide with reference image
  - *From: Juan Gea*

- **Face cropping and stitching for background faces**
  - Use case: Fix mutating background faces by masking, cropping to 1024x1024, V2V improvement, then stitching back
  - *From: Juan Gea*

- **FFLF (First Frame Last Frame) with Wan 2.2**
  - Use case: Creating smooth video transitions, works well and is fast
  - *From: Charlie*

- **Extension using first few frames -> VAE Encode -> Empty Embeds -> Sampler**
  - Use case: Video extension technique
  - *From: daking999*

- **Stand-in with face cropping and rembg**
  - Use case: Character consistency in video generation
  - *From: Kijai*

- **Phantom + VACE + Wan2.2LN LoRA integration**
  - Use case: Combining multiple techniques for enhanced results
  - *From: Ablejones*

- **FFLF (First Frame Last Frame) for fast face swap**
  - Use case: Fast face replacement in videos
  - *From: Charlie*

- **Multitalk with context windows for long lip sync videos**
  - Use case: Creating extended lip-synced videos up to minutes long
  - *From: Kijai*

- **Skyreels v2 for 121 frame generation**
  - Use case: Extending video length beyond standard limits
  - *From: NebSH*

- **Fun Control trajectory example for complex camera movements**
  - Use case: Controlling camera trajectories in video generation
  - *From: Kijai*

- **HN + LN model combination with unsampling**
  - Use case: Get motion from HN model with a few steps, then use unsampling and continue with LN model for detailed control
  - *From: Ablejones*

- **Multitalk v2v with Wan 2.1 t2v VACE merge**
  - Use case: Fast video-to-video generation with lip sync, 832x480x121 @ 24fps in under 10 minutes
  - *From: mdkb*

- **Stand-In v2v with reference image using VACE**
  - Use case: Face replacement in existing videos, took 176 seconds on RTX 3060
  - *From: mdkb*

- **PersonMaskUltra workflow for better Stand-In quality**
  - Use case: Segments, crops and resizes reference image to fill 512px space for improved output quality
  - *From: BobbyD4AI*

- **Medieval movie scenes using Text2Image + character rotation + inpainting + Wan2.2 i2v**
  - Use case: Creating animated medieval scenes with consistent characters
  - *From: loopen44*

- **MAGREF + FantasyPortrait + Uni3C combination**
  - Use case: Character consistency with camera control and face forward positioning
  - *From: Kijai*

- **MultiTalk with locked camera then use as driver**
  - Use case: Creating driving video for stand-in without recording yourself
  - *From: Kijai*

- **Context window method for infinite generation**
  - Use case: Endless video generation with MAGREF reference latents
  - *From: Kijai*

- **Two sampler workflow with LightX2V**
  - Use case: First sampler without LightX2V, second sampler with 4 steps using LightX2V
  - *From: Danial*

- **FantasyPortrait + MultiTalk for lip sync**
  - Use case: Creating talking character videos with audio sync
  - *From: Kijai*

- **Depth + DW pose with Kontext for first frame and Wan 2.2**
  - Use case: Character animation with pose control
  - *From: Guus*

- **Stand-in with VACE for character replacement**
  - Use case: Character swapping in videos, though results can be hit or miss
  - *From: ArtOfficial*

- **Context windows for longer video generation**
  - Use case: Extending videos beyond normal length limits, achieved 23s generation
  - *From: Kijai*

- **T2V for first frame then I2V continuation**
  - Use case: Creating longer videos with consistent motion
  - *From: Daflon*

- **Last frame used as first frame for next video**
  - Use case: Creating 16+ second videos with Wan 2.2
  - *From: Daflon*

- **FFLF (First-Frame-Last-Frame) or Context for video extension**
  - Use case: Extending videos smoothly
  - *From: Josiah*

- **Using VACE with low noise only for better consistency**
  - Use case: More consistent results with reference image, though slower
  - *From: Sal TK FX*

- **Cascadour to Python script for 3D controlnet input into VACE**
  - Use case: Creating controlled 3D character animations
  - *From: mdkb*

- **FantasyPortrait + MultiTalk combination**
  - Use case: Audio-synced facial animation with better lip sync
  - *From: Guey.KhalaMari*

- **VACE + Phantom model integration**
  - Use case: Enhanced character consistency with style control
  - *From: Hashu*

- **Long video generation up to 873 frames**
  - Use case: Extended video sequences in single pass
  - *From: T2 (RTX6000Pro)*

- **Triple VACE embed setup**
  - Use case: Controlnet with low strength + Inpainting mask + Reference strength for precise control
  - *From: Nekodificador*

- **Phantom + VACE + Wan 2.2**
  - Use case: One-shot character consistency, though very slow
  - *From: gokuvonlange*

- **MultiTalk facial performance**
  - Use case: Improved facial performance in lip-sync applications
  - *From: T2 (RTX6000Pro)*

- **VACE reference and Canny controlnet split workflow**
  - Use case: Combining reference image preservation with motion control, though ref image quality issues remain
  - *From: mdkb*

- **Fantasy Portrait + MultiTalk combined workflow**
  - Use case: Combining talking head generation with lip sync, using MAGREF checkpoint and context windows
  - *From: A.I.Warper*

- **Downscaling + noise + SeedVR2 enhancement**
  - Use case: Adding textures and fine-grained details to bring images to life, works well with Wan generated images
  - *From: Shawneau 🍁 [CA]*

- **10 image Wan morphing manually**
  - Use case: Creating morphing sequences between multiple images
  - *From: Gateway {Dreaming Computers}*

- **QwenImage to Wan I2V bridge**
  - Use case: Using QwenImage latents as input for Wan I2V generation
  - *From: fredbliss*

- **Video extension using last frame extraction**
  - Use case: Extract last frame, run through I2V workflow again, stitch with WanVideo Blender with 1 frame overlap
  - *From: xwsswww*

- **Single image FFLF for looping**
  - Use case: Using same image as both first and last frame in Wan 2.2 FFLF for creating loops
  - *From: ezMan*

- **Two-pass system with high noise preview**
  - Use case: Team workflow where high noise generates motion preview first, then continues to low noise refinement if approved
  - *From: gokuvonlange*

- **MultiTalk with three character masking**
  - Use case: V2V lip-sync for multiple characters using separate masks and audio files (silent for non-speaking characters)
  - *From: mdkb*

- **Phantom with VACE module for character consistency**
  - Use case: Maintaining character likeness in T2V while adding VACE control capabilities
  - *From: mdkb*

- **Save and load latent for stateless processing**
  - Use case: Serverless workers where latents are saved as files for continuation across stateless sessions
  - *From: gokuvonlange*

- **VACE single image inpainting: 5 frames (1 with mask + 4 empty gray)**
  - Use case: Single image inpainting with VACE
  - *From: Nekodificador*

- **Phantom + MultiTalk + FantasyPortrait combination**
  - Use case: Dynamic talking head generation with context windows
  - *From: Kijai*

- **Qwen-image -> latent -> WAN 2.2 I2V bridge**
  - Use case: Direct latent transfer without VAE decode
  - *From: fredbliss*

- **Multiple FUN controls can be hooked up together**
  - Use case: Combining different control inputs
  - *From: Flipping Sigmas*

- **Qwen image to Wan latent passing**
  - Use case: Direct latent space manipulation between models for potential long video extension
  - *From: fredbliss*

- **Fantasy Portrait with first/last frame extraction**
  - Use case: Video-to-video conversion by extracting input video frames as start/end points
  - *From: VRGameDevGirl84(RTX 5090)*

- **Fantasy Portrait + MultiTalk combination**
  - Use case: Combining video-driven and audio-driven lip sync
  - *From: slmonker(5090D 32GB)*

- **MAGREF + Fantasy Portrait + MultiTalk for long stable videos**
  - Use case: Generate 520-700 frame stable videos with good lip sync using 81 context size, 32 overlap, 6 steps with lightx2v I2V lora
  - *From: Kijai*

- **Use Fun Control models for camera control with Blender paths**
  - Use case: Camera trajectory control using paths created in Blender
  - *From: Kijai*

- **Context window with wildcard prompts**
  - Use case: Long video generation without repetitive scenes
  - *From: Kijai*

- **I2V feedback loop for scene transitions**
  - Use case: Generate I2V, extract best frames, feed into next sequence for better continuity
  - *From: Josiah*

- **LightX2V with upscale and noise injection**
  - Use case: Better sharpness on T2V - extra low noise pass after latent upscale
  - *From: hablaba*

- **3-stage sampler approach for Wan 2.2**
  - Use case: Better motion quality in 2.2 by using CFG in early stages
  - *From: Kijai*

- **FantasyPortrait mixed with Multitalk for lipsync**
  - Use case: High quality talking head generation with lip sync
  - *From: mdkb*

- **Scene cuts using prompt structure**
  - Use case: Creating scene transitions within single generation using [scene 1][cut][scene 2] format
  - *From: NebSH*

- **Style transfer using Fun Control 2.2 with ref image and input video as control**
  - Use case: Converting videos to different artistic styles while maintaining motion
  - *From: VRGameDevGirl84(RTX 5090)*

- **Language replacement for commercial video**
  - Use case: Take English speaking video, use Spanish audio driving video with face landmarks to change mouth movements to match new language
  - *From: mdkb*

- **Long-form talking head generation with InfiniteTalk**
  - Use case: Creating videos up to 1000 frames with lip sync using static reference image and driving video
  - *From: NC17z*

- **MultiTalk + FantasyPortrait + Uni3C + UniAnimate**
  - Use case: Complete talking head generation with camera movement
  - *From: Gateway {Dreaming Computers}*

- **InfiniteTalk with context windows**
  - Use case: Long-form lip sync generation without degradation
  - *From: Kijai*

- **Using first/last frame for video targeting**
  - Use case: Put target video first frame in ref, control video for lip sync
  - *From: mdkb*

- **InfiniteTalk with MAGREF**
  - Use case: Audio-driven video generation with character consistency using image + audio input
  - *From: Kijai*

- **Audio sync setup**
  - Use case: Use VideoInfo to extract input FPS, feed to VideoCombine output, use 25fps for embeds
  - *From: ˗ˏˋ⚡ˎˊ-*

- **InfiniteTalk + FantasyPortrait + MagRef**
  - Use case: High quality lip sync with character consistency using I2V model
  - *From: SonidosEnArmonía*

- **Context windows instead of multitalk node for 2.2**
  - Use case: Running InfiniteTalk with Wan 2.2 by avoiding the multitalk node
  - *From: Kijai*

- **V2V with driving video for lip sync**
  - Use case: Video-to-video with InfiniteTalk using control video improves lip sync significantly
  - *From: SonidosEnArmonía*

- **InfiniteTalk V2V with uni3c integration**
  - Use case: Video-to-video lip sync that preserves original video motion through keyframing
  - *From: Kijai*

- **VACE with face masking for targeted lip sync**
  - Use case: Using MultiTalk with VACE and masks to regenerate only face area for lip sync
  - *From: Tango Adorbo*

- **Qwen image to Wan bridge**
  - Use case: Generate image with Qwen, then feed to high sampler to low sampler for video generation
  - *From: fredbliss*

- **Two-step Qwen to I2V process**
  - Use case: Generate image with Qwen in first workflow, then use second workflow to convert image to video
  - *From: 243049749014380544*

- **4-stage sampling with LoRA switching**
  - Use case: Wan 2.2 14B I2V at 1280x720 with Lightning 8 steps (2/2/2/2) - High first stage without LoRA, second with LoRA / Low first stage without LoRA, second with LoRA
  - *From: : Not Really Human :*

- **QwenImageWanBridge workflow**
  - Use case: Creating less broken messes with Qwen integration, needs experimentation with noise settings
  - *From: fredbliss*

- **LLM description workflow**
  - Use case: Using Qwen2.5 VL to describe image then reprompting T5 to get base image correct before feeding to Wan2.2 I2V
  - *From: Josiah*

- **Wan 2.2 upscaling workflow**
  - Use case: 720p to 1024p upscale in 15 minutes using low noise model
  - *From: VRGameDevGirl84(RTX 5090)*

- **Endless I2V workflow adaptation**
  - Use case: Modified POM's endless workflow to use I2V instead of VACE for continuous video generation
  - *From: VRGameDevGirl84(RTX 5090)*

- **InfiniteTalk with Fantasy Portrait v2v**
  - Use case: Swapped MultTalk model with Infinite model in Fantasy Portrait workflow for driving video
  - *From: NC17z*

- **Multi-pass video creation**
  - Use case: First pass with basic settings, second pass for upscaling and refinement
  - *From: NC17z*

- **V2V using InfiniteTalk with uni3c**
  - Use case: Feed video input to multitalk node, ensure on infinitetalk, connect uni3c without latent hooked up, then generate
  - *From: DawnII*

- **Video inpainting with VACE and segmentation**
  - Use case: Combining VACE inpainting with segmentation mask for object replacement in videos
  - *From: Drommer-Kille*

- **Camera motion using first and last frame**
  - Use case: Generate jib and parallax camera movements by creating first and last frames
  - *From: NC17z*

- **Qwen Image -> Wan Video T2V pipeline**
  - Use case: Creating video from Qwen-generated images with better alignment between image and video content
  - *From: fredbliss*

- **InfiniteTalk + vid2vid cleanup**
  - Use case: Generate long video with InfiniteTalk, then clean up motion issues with vid2vid at 0.65 denoise
  - *From: samhodge*

- **InfiniteTalk video-to-video lip sync**
  - Use case: Creating talking head videos from existing video + audio
  - *From: Kijai*

- **Qwen Image to Wan latent bridge**
  - Use case: Using image generation models to drive video generation
  - *From: fredbliss*

- **Video looping for long audio**
  - Use case: Extending short video clips to match longer audio duration
  - *From: NebSH*

- **Krita ComfyUI integration for inpainting**
  - Use case: Live painting workflow with exposed generation parameters
  - *From: Kijai*

- **InfiniteTalk vid2vid with padding**
  - Use case: Lip sync with video input, faster than other methods
  - *From: NC17z*

- **High noise first pass then InfiniteTalk second pass**
  - Use case: Start with HN model normally, end early and run rest with InfiniteTalk vid2vid style
  - *From: Josiah*

- **Multiple character masking for InfiniteTalk**
  - Use case: Splits each character's face to 16:9 B&W mask, first mask gets first audio
  - *From: mdkb*

- **Audio splitting by frame count and FPS**
  - Use case: For workflows with multiple samplers creating multiple videos
  - *From: VRGameDevGirl84(RTX 5090)*

- **Two stage Wan 2.2 workflow with denoised output saving**
  - Use case: High noise model to 50% signal noise, save denoised latents, then load in stage 2 with low noise model
  - *From: MysteryShack*

- **InfiniteTalk with multiple samplers loop**
  - Use case: Each sampler uses previous sampler's result as I2V input, like advanced 'continue from last frame'
  - *From: Kijai*

- **VACE with differential diffusion masking**
  - Use case: Can use latent masking alongside VACE for inpainting
  - *From: Kijai*

- **VACE inpainting with ControlNet fill**
  - Use case: Fill mask with corresponding ControlNet data, leave outside unprocessed to avoid artifacts
  - *From: Nekodificador*

- **2.2 I2V InfiniteTalk workflow shared**
  - Use case: Using InfiniteTalk with WAN 2.2 for video extension
  - *From: DawnII*

- **Celebrity LoRA training with Flux for keyframes, then VACE inpainting**
  - *From: Nekodificador*

- **Blender control splines for camera movement**
  - Use case: Creating videos with complex camera movements and object animations using grease pencil outlines, curves and spheres
  - *From: Blink*

- **Multitalk with masking integration**
  - Use case: Lip sync with selective area masking during generation
  - *From: Kijai*

- **4-stage Lightning sampling**
  - Use case: Stage 1 High without LoRa / Stage 2 High with LoRa / Stage 3 Low without LoRa / Stage 4 Low with LoRa for 8 steps total
  - *From: : Not Really Human :.*

- **VACE + Phantom combination for character consistency**
  - Use case: Maintaining character likeness across video generation
  - *From: Ablejones*

- **Two-stage sampling with Wan 2.2 high/low noise**
  - Use case: Splitting steps between high noise and low noise samplers
  - *From: ComfyCod3r*

- **Manual mask creation in DaVinci Fusion for VACE**
  - Use case: Better character replacement results with properly proportioned masks
  - *From: Nekodificador*

- **Cinescale upscaling**
  - Use case: 2x quality improvement with 1.5x upscale using two samplers with different settings and RoPE scaling
  - *From: Kijai*

- **Multi-sampler slowmo fighting**
  - Use case: Using three different samplers with varying acceleration loras and CFG settings to combat slow motion artifacts
  - *From: Juan Gea*

- **Static camera control with Uni3C**
  - Use case: Repeat image first, then encode to create static camera control for video generation
  - *From: Juan Gea*

- **MAGREF with context windows for long videos**
  - Use case: Creating longer video sequences while maintaining character consistency
  - *From: Kijai*

- **I2V extension from last frame for looping**
  - Use case: Creating smooth loops instead of using context windows
  - *From: Kenk*

- **VACE inpainting with end frame reference**
  - Use case: Controlled transformations like dissolving effects
  - *From: SonidosEnArmonía*

- **InfiniteTalk long generation**
  - Use case: Endless generation without context window drawbacks, no motion reduction or speed loss
  - *From: Kijai*

- **Manual chaining I2V samplers**
  - Use case: Alternative to InfiniteTalk node for more control with different prompts/settings per clip
  - *From: seitanism*

- **Multi-sampler setup for speed LoRAs with Wan 2.2**
  - Use case: Using speed LoRAs with high noise model
  - *From: ArtOfficial*

- **2/1 or 2/2 HN then full distill LN distribution**
  - Use case: Preferred sampler distribution for Wan 2.2
  - *From: DawnII*

- **3 sampler setup with 1 step full HN**
  - Use case: Making speed LoRAs work with Wan 2.2
  - *From: Karo*

- **Two-pass talking face swap**
  - Use case: First pass on Fantasy Portrait, then vid2vid InfiniteTalk for head movements and better lip sync
  - *From: SonidosEnArmonía*

- **FantasyPortrait + InfiniteTalk combination**
  - Use case: Using both models together with looping sampling for head pose and lip sync
  - *From: Kijai*

- **Chain samplers for early preview**
  - Use case: Using 4 samplers with 1 step each instead of 1 sampler with 4 steps to preview and stop early if needed
  - *From: scf*

- **T2V to I2V pipeline**
  - Use case: Save latent from T2V and move to I2V model, though it usually breaks movement dynamics
  - *From: Draken*

- **Context windows with looping**
  - Use case: Quality takes big hit and inference time x3 or more, but enables longer generations
  - *From: Kenk*

- **High/Low noise sampling with distillation**
  - Use case: Using Lightning on high noise, LightX2V on low noise at 0.8 weight each
  - *From: CJ*

- **FantasyPortrait + InfiniteTalk**
  - Use case: Face-synced talking head generation with audio
  - *From: Kijai*

- **VACE + InfiniteTalk face replacement**
  - Use case: Replacing actors in movie clips with character LoRAs and syncing audio
  - *From: JalenBrunson*

- **Multiple LoRAs for multi-clip projects**
  - Use case: 4 clips stitched together, different LoRA combinations for different segments
  - *From: Samy*

- **VACE character replacement using single frame I2V**
  - Use case: Identity swapping for film shots using Wan 2.2 Low Noise model with lightning and fastwan loras at 1280x720
  - *From: mdkb*

- **FantasyPortrait first, then InfiniteTalk vid2vid refinement**
  - Use case: Combining head movement projection with audio-reactive lip sync
  - *From: Kijai*

- **MagRef + InfiniteTalk for clip extension**
  - Use case: Maintaining likeness and quality with no degradation across extended clips
  - *From: seitanism*

- **Wan VACE I2I via controlnet depth for single amazing image**
  - Use case: Creating high-quality single images using video model with depth control
  - *From: Gateway {Dreaming Computers}*

- **Using differential diffusion for multiple LoRAs**
  - Use case: Apply different LoRAs to different spatial regions by doing second generation with differential diffusion
  - *From: mamad8*

- **mdkb's VACE restyling workflow in zip file**
  - Use case: For VACE restyling and decipher workflow setup
  - *From: mdkb*

- **Using Blender + OBS + Uni3c for camera motion**
  - Use case: 3D model dragged backward in Blender, captured with OBS, edited with Shotcut, controlnet into Uni3c
  - *From: mdkb*

- **FFLF (First Frame Last Frame) for video extension**
  - Use case: Creating longer videos based on latest frame using second samplers
  - *From: Kenk*

- **T2V workflow using removed image input nodes from i2v**
  - Use case: Messy but working T2V setup for 2.2 14b
  - *From: crinklypaper*

- **Using extra latent node with both samplers**
  - Use case: Prevents glitches at first several frames when using Wan 2.2
  - *From: N0NSens*

- **CFG Schedule with normal steps instead of 3 samplers**
  - Use case: Better prompt adherence and faster inference for T2V
  - *From: Mu5hr00m_oO*

- **Using ComfyUI native audio encoder nodes with S2V**
  - Use case: Audio processing for speech-to-video generation
  - *From: Kijai*

- **S2V workflow shared**
  - Use case: Speech-to-video generation testing
  - *From: slmonker*

- **TTS -> S2V pipeline suggestion**
  - Use case: Text-to-speech combined with speech-to-video for complete audio-visual generation
  - *From: daking999*

- **MultiTalk with MAGREF workflow**
  - Use case: Alternative to InfiniteTalk when noise issues occur
  - *From: T2 (RTX6000Pro)*

- **Vid2vid VACE workflow for expression matching**
  - Use case: Expression matching and lip-sync on video input with masking
  - *From: SonidosEnArmonía*

- **S2V with context windows for long videos**
  - Use case: Generating longer videos without degradation
  - *From: Kijai*

- **VACE + masking for background replacement**
  - Use case: Replacing backgrounds in existing videos
  - *From: Dream Making*

- **Multitalk + MagRef I2V with Uni3C camera control**
  - Use case: 48 second video generation with camera movement from concert video
  - *From: T2 (RTX6000Pro)*

- **S2V with context windows for long video generation**
  - Use case: Generating 601 frames at 960x640 in 13 minutes using audio + reference image guidance
  - *From: Kijai*

- **Infinite looping WAN workflow**
  - Use case: Takes 4 prompts to generate seamless looping video
  - *From: chancelor*

- **InfiniteTalk with VACE inpainting**
  - Use case: Combining lip-sync with pose control and inpainting
  - *From: SonidosEnArmonía*

- **S2V with pose control and audio**
  - Use case: Lip sync generation with facial pose guidance
  - *From: Kijai*

- **VACE inpainting with extra frames**
  - Use case: Video inpainting when frames not multiple of 4
  - *From: SonidosEnArmonía*

- **InfiniteTalk with I2V motion**
  - Use case: Lip sync with additional character motion and background animation
  - *From: fredbliss*

- **Video continuation using ImageToVideo Encode**
  - Use case: Endless video generation by stitching I2V segments
  - *From: seb bae*

- **S2V model for infinite video generation without audio**
  - Use case: Extending videos indefinitely using S2V's reference motion capability without requiring audio input
  - *From: comfy*

- **Using separate masks for multi-character Infinite Talk**
  - Use case: Control which faces get lip sync in videos with multiple characters using masks and separate audio tracks
  - *From: jjtjjt*

- **iPhone camera motion transfer**
  - Use case: Using iPhone videos to drive camera movements in AI generations through uni3c
  - *From: T2 (RTX6000Pro)*

- **2.2 HN -> S2V with context windows**
  - Use case: Combining high noise 2.2 with S2V using context windows
  - *From: DawnII*

- **Infinite Talk with MAGREF**
  - Use case: Best lip sync results on RTX3090 using Infinite Talk with MAGREF 14B fp8 scaled
  - *From: NC17z*

- **Long video generation with MAGREF**
  - Use case: Using reference image for long videos with better context window performance
  - *From: T2 (RTX6000Pro)*

- **InfiniteTalk with TTS integration**
  - Use case: Generate audio first with TTS then use for video generation rather than running TTS with each generation
  - *From: JohnDopamine*

- **VACE with spline editor for camera control**
  - Use case: Lock camera movement by keeping spline static on background
  - *From: DawnII*

- **Context windows for long generations**
  - Use case: Generate 3-4 minute videos 81 frames at a time passing previous 8 frames into context
  - *From: dipstik*

- **2.2 for T2I, QwenEdit for stills, 2.2 for I2V without lipsync, 2.1 with Multi/Infinit + uni3c for lipsync**
  - Use case: Complete video generation pipeline
  - *From: N0NSens*

- **Basic vid2vid then composite head/mouth to original**
  - Use case: Changing lips in existing video
  - *From: Kijai*

- **Context windows with stride on high noise side only**
  - Use case: Better window blending in 2.2 workflows
  - *From: Kijai*

- **High noise with overlap/stride then low noise without stride**
  - Use case: Context window generation with 2.2 - use 48 overlap and 10 stride for high noise, then different settings for low noise
  - *From: Kijai*

- **FantasyPortrait + S2V combination**
  - Use case: Combining pose control methods - FP on first step only with S2V
  - *From: Kijai*

- **Prompt travel with different prompts per context window**
  - Use case: Each prompt for ~81 frames in context windows
  - *From: Dever and Kijai*

- **CineScale upscaling with two samplers**
  - Use case: Latent upscale between two samplers for video upscaling
  - *From: DawnII*

- **InfiniteTalk long generation**
  - Use case: 2000 frames in 28 windows, at 832x480 with 4 steps, 12 mins
  - *From: Kijai*

- **S2V with driving video**
  - Use case: S2V seems to like having a driving video a lot more. 4 second wan2.2 t2v gen pose video, with 10 second s2v gen
  - *From: ArtOfficial*

- **VACE with between frames setup**
  - Use case: Connect to a VACE embed for first-last frame techniques
  - *From: Nekodificador*

- **3 KSampler workflows for Wan**
  - Use case: Better video generation results, user wants to add second image as last frame
  - *From: BecauseReasons*

- **First/Last Frame workflow using WanFirstLastFrameToVideo node**
  - Use case: Replaces WanImageToVideo for FLF generation
  - *From: Juampab12*

- **VACE first frame edit v2v**
  - Use case: Take video and new first frame to edit video with new first frame as reference
  - *From: Juampab12*


## Recommended Settings

- **LightX2V strength**: High noise: 3, Low noise: 1
  - Better quality and prompt adherence
  - *From: gokuvonlange*

- **Steps configuration with LightX**: High noise: 3 steps (no lightx) + 6 steps (with lightx), Low noise: 3 steps (with lightx)
  - Optimal balance of quality and speed
  - *From: TK_999*

- **CFG values**: High noise: CFG=5 (first steps), CFG=1 (later steps), Low noise: CFG=1
  - Better convergence
  - *From: TK_999*

- **Denoise for custom nodes**: 0.5-0.7
  - Produces dramatically different and better results
  - *From: VRGameDevGirl84(RTX 5090)*

- **VACE strength**: 1.0-1.5
  - 1.0 can cause background changes, 1.5 helps but may oversaturate
  - *From: seitanism*

- **Context windows frame count**: 81 frames per scene
  - For smooth scene transitions when using | separator
  - *From: avataraim*

- **Launch flag for memory issues**: --cache-none
  - Reduces RAM usage by disabling node caching
  - *From: Kijai*

- **RadialAttention block size**: 128
  - Image dimensions must be divisible by this value
  - *From: NebSH*

- **High/Low noise model split**: High: 6 steps (0-6, CFG 3), Low: 4 steps (6-10, CFG 1)
  - Good balance of quality and prompt adherence
  - *From: IceAero*

- **Alternative split for prompt adherence**: High: 20 steps (0-10, CFG 3.5), Low: 6 steps (3-6, CFG 1)
  - Better prompt following with high model getting more steps
  - *From: gokuvonlange*

- **Context window overlap**: 10 stride, 48 overlap on high noise
  - Successfully tested combination for window blending
  - *From: Kijai*

- **LightX2V strength for AMD**: Strength 1, CFG 1
  - Works well with 5 steps (3 high, 2 low) on AMD setup
  - *From: nacho.money*

- **Timestep split ratio**: 0.875 threshold
  - Original WAN training used 875 timestep split between high/low noise models
  - *From: Kijai*

- **CFG**: 3.5 for high pass, 1.5 for low pass
  - Better prompt adherence
  - *From: loopen44*

- **LightX2V LoRA strength**: 3 for high pass, 1 for low pass
  - Optimal balance
  - *From: loopen44*

- **Steps**: 5x5 steps for I2V
  - Good balance of quality and speed
  - *From: loopen44*

- **Context overlap**: Higher overlap blends better but slows generation
  - Quality vs speed tradeoff
  - *From: Kijai*

- **Sampler**: DDIM for faster generation
  - Half the time of DPMPP_SDE
  - *From: The Shadow (NYC)*

- **Steps for no LoRA**: 15 steps on high noise, 25 steps on low noise (40 total)
  - Official recommendation
  - *From: aikitoria*

- **CFG for no LoRA**: 3.0 to 3.5
  - For superior motion and prompt adherence without LoRAs
  - *From: mdkb*

- **LightX LoRA strength**: 0.5 on second pass
  - Better quality with 10 steps each pass
  - *From: VRGameDevGirl84(RTX 5090)*

- **Timestep boundary for model switching**: 0.875 (timestep 875)
  - Official code specification for high vs low noise model usage
  - *From: aikitoria*

- **Boundary value for 40 steps**: 15
  - Exactly correct for 40 steps/simple/shift 5
  - *From: aikitoria*

- **Boundary value for 20 steps**: 8
  - Proportionally correct for 20 step generation
  - *From: aikitoria*

- **LightX LoRA for T2V only**: 2 steps low model only, 1 CFG, unipc/beta
  - Faster inference for T2V
  - *From: Rainsmellsnice*

- **Context window overlap**: Lower values for low noise side
  - Doesn't need as much overlap, makes generation faster
  - *From: Kijai*

- **Context overlap**: 16 with 4 stride
  - Good balance vs 48 overlap which takes much longer
  - *From: thaakeno*

- **Shift parameter**: 3-5
  - Lower values give more creativity, around 3-5 works well
  - *From: thaakeno*

- **CFG for high/low noise split**: High: 3.5, Low: 1
  - Prevents washed out output when using lightx2v LoRAs
  - *From: BondoMan*

- **Steps for T2I quality**: 30 low noise, 20 high noise
  - Better sharpness and overall quality
  - *From: 🐝 bumblebee 🐝*

- **Block swap**: 20
  - Manages VRAM usage during intensive operations
  - *From: thaakeno*

- **Model quantization**: fp8_e5m2
  - Required for proper model loading instead of default
  - *From: topmass*

- **Steps for V2V upscale**: 12 steps with start at 9
  - Minimize changes while upscaling
  - *From: thaakeno*

- **CFG for 2.2 without LightX**: 3.5 CFG with 20 steps
  - Working parameters for 2.2 T2V
  - *From: N0NSens*

- **Sampler for 5B model**: flowmatch_pusa in wrapper, unipc in native
  - Different optimal samplers for different implementations
  - *From: daking999*

- **CFG**: 5 on high noise timesteps
  - Works well for T2I and T2V
  - *From: mamad8*

- **Steps configuration**: 3+5
  - Ends on proper sigma the best
  - *From: DawnII*

- **Sampler**: euler + beta for T2V/I2V, res_multistep + beta57 for T2I
  - Better results
  - *From: mamad8*

- **High noise CFG + SLG first step**: CFG + SLG first step, then 2 steps with CFG 1.0 and low side CFG 1.0
  - Kijai's working configuration
  - *From: Kijai*

- **H100 weight and compute dtype**: fp16 to use fp16 fast accum
  - Optimization for H100
  - *From: Kijai*

- **LightX LoRA strength**: High: 3.0, Low: 1.5
  - Gives great results in testing
  - *From: screwfunk*

- **CFG for high noise model**: 3.5
  - Improves character motion significantly
  - *From: Rainsmellsnice*

- **Steps distribution**: 8 steps total: 4 high, 4 low
  - Balanced approach for quality and speed
  - *From: screwfunk*

- **Blockswap for 4090**: Full 40 blocks possible
  - Takes advantage of available VRAM efficiently
  - *From: VK*

- **Start step for upscaling**: 8-9 out of 12 for pure upscale, 4 for motion fixes
  - Controls how much video changes during processing
  - *From: thaakeno*

- **Block swap for 14B model**: 20 blocks
  - Uses ~25GB VRAM for 81 frames at 1280x720 with 10 steps
  - *From: Kijai*

- **lightx2v maximum steps**: 6 steps or less
  - More than 6 steps ruins quality with lightx
  - *From: ComfyCod3r*

- **lightx2v strength**: 2.0
  - Recommended strength for both t2v and i2v variants
  - *From: Draken*

- **Character LoRA training**: min_t=0, max_t=1, 24 source images, 512px resolution
  - Fast convergence for likeness in 9 minutes
  - *From: Kenk*

- **5B upscaling denoise**: 0.3-0.5
  - Good balance for upscaling 14B output without artifacts
  - *From: Juan Gea*

- **Multitalk sync**: High seed: specific number, Low seed: 0, shift: 8
  - Closest to achieving audio sync
  - *From: nacho.money*

- **Distill LoRA steps**: 3/3 or 5/5 for i2v, 10/10 without LoRA
  - Better results than higher step counts which can overcook
  - *From: Karo*

- **Model switching sigma**: 0.875
  - Intended sigma value for high/low noise model transition
  - *From: Ablejones*

- **lightx2v LoRA strength**: 3.0+
  - Below 3.0 doesn't work properly, prompt only started working at 3.0
  - *From: Kijai*

- **distill LoRA strength**: 0.20
  - Works well with cfg 2, 10 steps, follows prompt very well
  - *From: hicho*

- **fusion LoRA i2v sweet spot**: 4.0
  - Found to be sweet spot for i2v with fusion lora
  - *From: topmass*

- **block swap for high resolution**: 30
  - Enables 3072x1840 generation with 5B model
  - *From: Juan Gea*

- **cfg for burning prevention**: 3.5
  - 2cfg was burning too much at higher values
  - *From: Kijai*

- **LoRA rank preference**: 64 or 128
  - 64 is fine, 128 can have subtle improvements, lower than 16 are awful
  - *From: Kijai*

- **shift**: 1
  - Produces perfectly sharp images for T2I generation
  - *From: aikitoria*

- **LoRA rank**: 64
  - Good balance - 256 is huge and doesn't add much, 8 too low
  - *From: VRGameDevGirl84(RTX 5090)*

- **LightX LoRA strength**: 0.5
  - Helps add details without overdoing it
  - *From: VRGameDevGirl84(RTX 5090)*

- **steps for two-pass**: 20 steps each pass
  - Works better than single 40-step pass for detail generation
  - *From: VRGameDevGirl84(RTX 5090)*

- **Shift value**: 1 for T2I, 12 for matching original code
  - Shift 1 works best for T2I workflows, shift 12 matches Alibaba's implementation
  - *From: aikitoria*

- **CFG without LightX**: 3.5 CFG for 20 steps high noise, then 6 steps low noise
  - Proven configuration that works well
  - *From: TK_999*

- **High/Low noise steps for T2V**: 25 steps high noise, 15 steps low noise
  - Matches official implementation boundary at 0.875
  - *From: aikitoria*

- **LoRA rank**: 32 instead of 64
  - Should be fine and reduces memory impact
  - *From: Kijai*

- **Wan 2.2 Lightning LoRA strength**: 0.125
  - Alpha 8, rank 64 = 0.125. Original had hardcoded alpha values
  - *From: Kijai*

- **Shift parameter for short step counts**: 8-9
  - Wan is linear and needs high shelf at start for short steps
  - *From: Simjedi*

- **Steps for Lightning LoRAs**: 4 steps
  - Works well with euler scheduler and 0.125 strength
  - *From: Kijai*

- **CFG for Wan 2.2 with Lightning**: High: 3.5, Low: 1.0
  - Recommended settings for high and low noise models
  - *From: Nemlet17*

- **LoRA strength for new lightning**: 1.0
  - Fixed versions work at normal strength unlike original 0.125 requirement
  - *From: Kijai*

- **Step distribution**: 3 high + 3 low minimum
  - 2+2 steps insufficient, 3+3 fine, 4+4 much better
  - *From: Kijai/Juampab12*

- **Sampler**: Euler
  - Official training uses Euler only
  - *From: Kijai*

- **Shift value**: 5
  - Used in official training setup
  - *From: Kijai*

- **CFG**: 1.0 for LoRA steps
  - Works best with lightning LoRAs, CFG 3.5 can oversaturate
  - *From: multiple users*

- **Lightning LoRA strength**: 1.0/1.0 for high/low noise
  - Default recommended settings
  - *From: Doctor Shotgun*

- **CFG for Lightning**: CFG 1.0
  - Designed for low CFG operation
  - *From: gokuvonlange*

- **Steps for Lightning**: 4 steps (2/2 split)
  - Official recommendation for 2.2 Lightning
  - *From: Doctor Shotgun*

- **Resolution for Lightning**: 1280x720
  - Works better than 480p, avoids slow motion artifacts
  - *From: Kijai*

- **Scheduler**: Euler
  - Works better than LCM for Lightning LoRAs
  - *From: piscesbody*

- **Lightning LoRA strength**: 1.0 for both High and Low noise
  - Recommended starting point for new Lightning LoRAs
  - *From: Purz*

- **CFG for Lightning LoRA**: CFG 1.0 with Lightning, CFG 3.5 without
  - Lightning LoRA is distilled to work at low CFG
  - *From: multiple users*

- **FastWan 5B steps**: 3-6 steps with CFG 1.0
  - Distilled model designed for low step count
  - *From: Kijai*

- **Block swapping for 5B**: 30 blocks out
  - Enables high resolution generation on 24GB VRAM
  - *From: Juan Gea*

- **Lightning lora strength for T2I**: CFG 1, strength 0.5, 15 steps high and low
  - Better results than 4 steps at 1 strength and better than without loras
  - *From: Shawneau 🍁 [CA]*

- **Fast 5B T2V generation time**: 10 second generation + 17 second decode
  - With compile optimization
  - *From: Kijai*

- **Full model I2V settings**: 20 steps, CFG 3.5, no distill or lightx2v lora
  - Really good prompt adherence but takes very long to generate
  - *From: gokuvonlange*

- **Minimum steps recommendation**: 6 steps total (3+3)
  - Less than 6 produces errors or bad gens
  - *From: Lodis*

- **Lightning lora scheduler**: Euler with shift=5, cfg=1.0
  - Official recommendation for NFE=4 not 8
  - *From: Kijai*

- **LightX2V 3+3 configuration**: 3 steps high + 3 steps low
  - Works fantastic with old lightx
  - *From: Lodis*

- **CRF encoding setting**: CRF 10 or 17
  - CRF 17 supposed to be visually lossless, CRF 10 for higher quality
  - *From: N0NSens*

- **MMAudio configuration**: Interpolation at 30 or 60fps, 5s config, 4-5 word prompts
  - Works better with interpolation and short prompts
  - *From: : Not Really Human :*

- **Lightning lora strength**: Lower strength with low cfg values
  - Works with low cfg if you lower strength
  - *From: Kijai*

- **sampler_name and scheduler for lightx LoRA**: euler beta
  - Recommended sampler for Wan 2.2 with lightx LoRA
  - *From: Dan*

- **blockswapping**: 20 blocks
  - Enables upscaling to 1080p on 24GB VRAM
  - *From: thaakeno*

- **I2V LoRA combination**: phantom fusionx + pusa + lightx2v
  - Provides better motion quality and prompt following than lightning LoRA alone
  - *From: Ada*

- **Lightning LoRA usage**: 4 steps total, 1 cfg
  - Optimal settings for the new lightning LoRA, though limited to simple prompts
  - *From: Ada*

- **CFG scheduling for native 2.2**: CFG 4-5 on first step only, revert to CFG 1 for remaining steps
  - Better stability with split sampling
  - *From: PizzaSlice*

- **Lightning 2.2 timestep schedule**: euler/simple with shift 5.0 and flowmatch_distill
  - Matches their specific timesteps for 4 steps
  - *From: Kijai*

- **Lightning LoRA strength**: 0.2-0.35
  - Prevents color burning and convergence issues
  - *From: 3DBicio*

- **LightX2V LoRA strength**: 2.0-3.0 strength with CFG 1
  - Better resemblance maintenance in I2V
  - *From: Jonathan*

- **WAN 2.2 Q4_K_S GGUF parameters**: 4 steps, CFG 1, LCM/simple scheduler, LightX2V 2.0 strength
  - Works well even on lower-end hardware
  - *From: Jonathan*

- **VAE tile sizes for 16GB VRAM**: 512x384 for tiles, 384 for stride
  - Cuts VAE decoding time in half compared to default 272x144
  - *From: patientx*

- **Qwen-Image precision**: fp8_e5m2
  - Avoids burnout errors that occur with fp8_e4m3fn
  - *From: fredbliss*

- **VRAM usage**: 14GB idle, 23GB during inference
  - Model loading/unloading based on VRAM constraints
  - *From: 642326806678077441*

- **Lightning LoRA strength**: Strength 1 for old LightX2V on high noise
  - Better motion results
  - *From: SonidosEnArmonía*

- **Steps configuration**: 4+4 steps for LightX2V
  - Commonly used configuration for good results
  - *From: .: Not Really Human :.*

- **Shift value**: Shift 8 in HN (High Noise)
  - Used in conjunction with CFG 1
  - *From: piscesbody*

- **CFG**: 2.0
  - Prevents blurry/foggy results with low contrast
  - *From: Kijai*

- **Shift**: 5.0
  - Better quality than 1.0 for general use, 0.5 for sharper images
  - *From: Kijai*

- **Lightning LoRA strength**: 0.7
  - Good compromise between speed and quality
  - *From: Kijai*

- **Frame count**: 81
  - Model cannot properly do 5 seconds at 24fps beyond this
  - *From: Kijai*

- **Context overlap**: More overlap needed
  - For better results with context windows
  - *From: Kijai*

- **CFG**: 1 for specific cases
  - Juan Gea was using CFG=8 which might cause burning with speed LoRAs
  - *From: Juan Gea*

- **Shift parameter**: 8 for I2V, 1 for T2I
  - Shift=1 breaks I2V completely but required for T2I
  - *From: N0NSens*

- **Scheduler**: DMP++_SDE with beta
  - Used in testing comparisons between shift values
  - *From: Nekodificador*

- **Generation time on 5090**: 1 min 30s for 5 second video
  - Performance benchmark
  - *From: Kijai*

- **CFG for motion control**: CFG 1 for T2V, higher for I2V
  - T2V works well at low CFG, I2V needs higher CFG for motion
  - *From: Josiah*

- **Lightning LoRA steps**: 4+4 steps or 3/3 steps
  - Fast generation with Lightning LoRAs
  - *From: .: Not Really Human :.*

- **Non-Lightning generation**: CFG 5+ and 20+ steps
  - When not using Lightning LoRAs, need higher CFG and steps
  - *From: N0NSens*

- **Frame limit for consistent motion**: Up to 109 frames for I2V, 81 frames recommended
  - Model trained on 81 frames, longer sequences may loop
  - *From: N0NSens*

- **LightX LoRA strengths for HIGH and LOW models**: HIGH (1.0, 1.0, 3.0) & LOW (3.0, 2.0, 1.0) at 6 total steps split at 3
  - Provides good balance of speed and quality
  - *From: : Not Really Human :.*

- **FastWan maximum strength**: 0.35 for video
  - Maximum recommended strength, image strength unknown
  - *From: 3DBicio*

- **V2V denoise level**: Below 0.5
  - For upscaling workflows where content already exists
  - *From: mdkb*

- **Blockswap value**: 40
  - More than 40 is useless for memory management
  - *From: : Not Really Human :.*

- **LightX2V high noise strength**: 2
  - Consistently outperforms 2.2 lightning version
  - *From: shuzhi*

- **VACE control strength**: 1:1
  - Better results than 3 and 1.5 ratios
  - *From: Lodis*

- **Add noise shift value**: 8-10
  - Higher values produce cleaner results with dreamy effects
  - *From: piscesbody*

- **CFG for Wan 2.2 Lightning**: 1.0
  - Official workflow uses cfg 1.0 so negative prompts aren't used
  - *From: Kijai*

- **Lightning LoRA strength**: 0.9 for high, varies for low
  - Better results than 1.0, less artifacts
  - *From: Kijai*

- **Steps for new Lightning**: 6 steps preferred over 4
  - 4 steps needs custom sigmas, 6 feels better
  - *From: Kijai*

- **Flowmatch_distill with shift**: 5.0 shift (same as custom euler sigmas)
  - Works well with 4 steps at 0.9 strength
  - *From: Kijai*

- **HN model with Lightning**: 3+3, 4+4, or 5+3 steps
  - Better than just 3+3, CFG optional on LN but helpful for certain elements
  - *From: IceAero*

- **Lightning LoRA strength**: 1 for both high and low
  - Recommended strength for new lightning LoRAs
  - *From: Critorio*

- **Old Lightning LoRA strength**: 3 (high) and 1 (low)
  - Previously working settings for older LoRAs
  - *From: Gill Bastar*

- **Shift parameter for LightX**: 6
  - Better results with LightX LoRAs
  - *From: Karo*

- **CFG scheduling**: Can define by step
  - Available in both wrapper and native
  - *From: Kijai*

- **Lightning I2V LoRA strengths**: 1.5/1 (high/low) for balanced motion
  - Provides goldilocks balance between slow and fast motion
  - *From: CaptHook*

- **Wan 2.2 optimal config**: fp8, 1024x576, 81fr, unipc, shift 8, cfg 1, 6 steps
  - Recommended working configuration
  - *From: CaptHook*

- **CFG for Wan 2.2**: CFG 1 on both samplers
  - Best results with Lightning LoRA, constant 1 recommended
  - *From: Cubey*

- **LightX2V adaptive rank LoRA**: 0.8 high side, 0.9 low side
  - Better motion control than Lightning
  - *From: MilesCorban*

- **Lightning LoRA strength**: 1.0
  - Higher values make output look like 2.1 instead of 2.2
  - *From: Ablejones*

- **Audio scale for MultiTalk**: 3.0
  - Helps maintain lip sync quality for longer durations
  - *From: samhodge*

- **Audio CFG**: 3.0
  - Works well with audio scale 3 for vid2vid workflows
  - *From: samhodge*

- **VRAM reservation**: --reserve-vram 2
  - Prevents tensor allocation errors in native ComfyUI with limited VRAM
  - *From: Kijai*

- **Control end_percent**: 0.5
  - Prevents errors when too low
  - *From: Kijai*

- **Audio_scale**: 3
  - Better MultiTalk lip sync performance
  - *From: SonidosEnArmonía*

- **Block swap**: 30 consistently
  - Prevents OOM when 20 fails, keep consistent across models
  - *From: Kijai*

- **Denoise**: < 1.0
  - Required for proper video-to-video MultiTalk functionality
  - *From: Kijai*

- **Switch DiT boundary**: 0.875
  - Default boundary for switching from high to low noise model
  - *From: fredbliss*

- **FlowMatchScheduler shift**: 5
  - Default shift value used in modelscope diffsynth
  - *From: fredbliss*

- **Lightning LoRA first step weight**: 0.0
  - Prevents slow-motion issues
  - *From: MysteryShack*

- **Fun Control steps**: 4 total steps recommended
  - Official i2v workflow uses 4 total steps
  - *From: Rainsmellsnice*

- **High/Low noise split**: 14 high / 6 low steps
  - Better detail preservation and motion quality than 11/9 split
  - *From: crinklypaper*

- **Shift value for sigma control**: Shift 8 for higher sigma values, shift 5 for middle split
  - Controls when high noise switches to low noise based on sigma threshold
  - *From: Kijai*

- **Resolution for VRAM efficiency**: 800x480 for testing, lower res for longer frames
  - Balance between quality and VRAM usage for extended generation
  - *From: VK (5080 128gb)*

- **Input dimensions**: Divisible by 16
  - Prevents tensor size mismatch errors
  - *From: Kijai*

- **Sapiens keypoint confidence threshold**: 0.5
  - Filters out bad detection points
  - *From: ˗ˏˋ⚡ˎˊ-*

- **I2V lightning LoRA strength**: Less than 1
  - Prevents camera shake issues
  - *From: XWAVE*

- **Radial attention dense timesteps**: 11
  - Standard setting for WAN 2.2, 0 timesteps looks too good to be true
  - *From: MysteryShack*

- **Frame count**: 77 frames instead of 81
  - Eliminates slow motion effect, better matches Wan 2.2's 16-frame architecture
  - *From: xwsswww*

- **LoRA strength for 2.1 LoRAs on 2.2**: 3.0 for high noise, 1.5 for low noise
  - Proper strength adjustment for cross-version compatibility
  - *From: Abyss*

- **RAM for Wan 2.2**: 96GB comfortable, 64GB minimum
  - 64GB can OOM after 3 generations with setting changes, 96GB is comfortable
  - *From: Rainsmellsnice*

- **Lightning LoRA strength**: High: 2.5, Low: 1.0
  - For natural walking pace without artifacts
  - *From: Alpha-Neo*

- **CFG for motion control**: CFG 3.5 on high, 0.5 with light LoRA
  - Finding sweet spot for decent quality with motion, keeping 0.9-1.0 on low
  - *From: Hevi*

- **Lightning LoRA 4-step**: 4 steps with lightning LoRA on Wan 2.2
  - For faster generation
  - *From: army*

- **Control strength for 5B controlnet**: 0.5
  - Good balance for first try results
  - *From: Kijai*

- **VACE encode strength**: 0.7
  - Standard setting for face swapping workflow
  - *From: Ruairi Robinson*

- **Lighting LoRA strength**: 0.9
  - Works well in multi-sampler setup
  - *From: Karo*

- **ComfyUI startup parameter**: --disable-smart-memory
  - Helps with OOM issues on 12GB VRAM with 32GB system RAM
  - *From: mdkb*

- **Denoise threshold for v2v**: 0.79
  - Tipping point - lower keeps structure, higher allows prompt-based changes
  - *From: mdkb*

- **v2v strength for good motion retention**: 0.85
  - Maintains motion while allowing character changes
  - *From: Benjimon*

- **Training frames for motion retention**: 77 frames
  - Helps avoid slow motion issues when training on images
  - *From: Juampab12*

- **cfg for speed**: 1.0
  - cfg other than 1.0 runs model twice per step, making it slower
  - *From: Kijai*

- **Lightning LoRA strength**: 1.0 each for high/low
  - Standard strength for Lightning LoRAs
  - *From: screwfunk*

- **LightX2V LoRA strength**: 0.2-0.5
  - Works as glue to bring LoRAs together, clears up blurry results
  - *From: screwfunk*

- **Skyreels LoRA strength**: 2.0 on high, 1.0 on low
  - Allows 121 frame generation
  - *From: Kijai*

- **CFG value with low steps**: 2.0
  - Can't use very high cfg with less steps
  - *From: Kijai*

- **Prefetch blocks**: 1
  - Single block enough to offset speed loss on most systems
  - *From: Kijai*

- **High model timestep range**: 0.875-1.0
  - Default range for high noise model
  - *From: Alisson Pereira*

- **Low model timestep range**: 0.0-0.875
  - Default range for low noise model
  - *From: Alisson Pereira*

- **Skyreels T2V LoRA strength**: high = [2,2.5,2.5] (float list), low = no use
  - For 121 frames 6 steps
  - *From: avataraim*

- **Old LightX2V LoRA strength**: 3 high/1 low
  - Better than newer versions for I2V
  - *From: N0NSens*

- **Steps distribution for 2.2**: Balance steps between low and high (e.g., 4 low 4 high for 8 total)
  - To respect scheduler's curve
  - *From: ˗ˏˋ⚡ˎˊ-*

- **LoRA scheduling**: Step 1: 2.0, Step 8: 1.2 with linear interpolation
  - Provides varying LoRA strength over denoising steps
  - *From: ˗ˏˋ⚡ˎˊ-*

- **MultiTalk denoise**: 0.7 minimum for lip movement
  - Lower values don't produce lip movement
  - *From: AmirKerr*

- **Video length for quality**: 81 frames maximum
  - Wan mostly trained on 5sec (81 frame) videos, quality goes downhill with longer sequences
  - *From: Hevi*

- **Wan 5B upscaling denoise**: 0.35 or 0.5
  - Good balance for V2V upscaling without over-processing
  - *From: Juan Gea*

- **SeedVR2 sampler/scheduler**: Heun/Beta or Euler/Beta with 4 steps
  - Good quality-speed balance, might go lower to 1.8 denoise
  - *From: AmirKerr*

- **LoRA extraction rank**: 64 usually sufficient, 128 can be better
  - 64 sufficient for most cases, 128 possibly not worth twice the size
  - *From: Kijai*

- **Reference image size for Stand-in**: 640x640 or higher (768x768, 1024x1024)
  - Better results than 512x512
  - *From: Kijai*

- **Stand-in LoRA strength and latent multiplier**: Variable based on needs
  - Has effect on output quality
  - *From: Kijai*

- **Context overlap frames**: Lower values
  - Higher overlap increases render time significantly
  - *From: xwsswww*

- **Skyreels LoRA weight**: 1.8 on high, 1.5 on low
  - Works well for 121 frame generation
  - *From: NebSH*

- **LightX2V LoRA strength**: 0.6 with increased steps
  - Reduces overcooking while maintaining speed benefits
  - *From: Hevi*

- **Block swap**: Enable for wrapper when using high resolution
  - Prevents OOM errors that native handles automatically
  - *From: Kijai*

- **Quantization disabled**: Leave disabled for pre-quantized models
  - Works as auto-select for already quantized models
  - *From: Kijai*

- **LightX2V steps and CFG**: 4 steps, CFG 1.0, LoRA strength 1.00
  - Standard settings for LightX2V acceleration
  - *From: Danial*

- **VACE with guidance frames**: 8 steps without acceleration LoRAs
  - Structure is already provided so needs fewer steps
  - *From: pom*

- **Multitalk v2v denoise**: 0.7
  - Used for video-to-video generation with Multitalk
  - *From: mdkb*

- **High noise CFG**: 3.5 for 10 steps (of 20) with no LoRA
  - Good quality balance
  - *From: gokuvonlange*

- **Low noise CFG**: 1 for 2 steps (of 4) with LoRA
  - Fast inference with LoRA
  - *From: gokuvonlange*

- **Width dimensions**: Use 832 instead of 840, follow divisible by 16 rule
  - Avoid broadcast dimension errors
  - *From: Kijai*

- **VACE strength for Stand-In v2v**: 0.2 (reduced from 1.0)
  - Balance between original video and reference influence
  - *From: mdkb*

- **Block swap**: 40 blocks for maximum memory efficiency
  - Reduces max allocated memory from 16GB to 11GB
  - *From: Kijai*

- **Prefetch blocks**: 0 for least memory use
  - Combined with non-blocking false gives lowest VRAM usage but slower speed
  - *From: Kijai*

- **Resolution for 720p generation**: 832x480
  - Works reliably, higher resolutions may cause OOM on some cards
  - *From: patientx*

- **LightX2V steps**: 4 steps in the sampler using the LoRA
  - LoRA was trained on 4 steps
  - *From: Danial*

- **Torch compile**: Disable with stand-in method
  - There's probably some issue with compile with the stand-in method
  - *From: Kijai*

- **Lightning LoRA strength**: 1.0 for both high and low
  - Instead of 3.0/1.0 to avoid motion destruction
  - *From: xwsswww*

- **Canny control strength**: 1.0
  - Reduced from 1.5 with inverted canny for better results
  - *From: xwsswww*

- **Block swap VRAM usage**: 23G
  - MultiTalk + Wan 2.2 with main model block swapped
  - *From: nacho.money*

- **CFG for motion control**: 3.5 vs 1
  - Higher CFG produces faster motion but may cause artifacts
  - *From: Mngbg*

- **Image resize divisibility**: 32
  - Required for proper model functioning
  - *From: mdkb*

- **Block swap for 81 frames at 720x720**: ~20 blocks
  - To fit in 24GB VRAM
  - *From: Kijai*

- **Fantasy Portrait block swap**: 40 or higher
  - Example was set for 57 frames, need more for 81 frames
  - *From: Kijai*

- **Context windows node**: Use defaults
  - Just drag from sampler node and use default settings
  - *From: A.I.Warper*

- **blocks_to_swap**: 20
  - Puts half the model on RAM and half to VRAM for 8GB VRAM users
  - *From: Kijai*

- **CFG**: 1
  - Only runs positive conditioning, higher values run both positive and negative
  - *From: DawnII*

- **reserve-vram**: 5
  - Helps prevent ComfyUI freezing with native nodes
  - *From: Kosinkadink*

- **fuse_method**: pyramid or linear
  - Values must be from allowed list, not numeric
  - *From: Drommer-Kille*

- **--reserve-vram**: 5
  - Prevents VRAM spillover to slow shared memory, dramatically improves speed
  - *From: Nekodificador*

- **cfg**: 1.0
  - Disables negative prompt pass for twice the speed
  - *From: Kosinkadink*

- **blocks**: 40
  - Optimal performance with sage attention 3
  - *From: cocktailprawn1212*

- **power limit**: 500W
  - Better stability vs default 600W with minimal performance impact
  - *From: Kijai*

- **Ref-image VACE strength**: 0.6–1.0 (start at 0.8)
  - If identity is drifting
  - *From: Josiah*

- **Ref-image VACE start/end percent**: start: 0.00, end: 0.25–0.40
  - Fade out after look is established
  - *From: Josiah*

- **Canny/motion VACE strength**: 0.5–0.8 (start ~0.7)
  - For motion control throughout clip
  - *From: Josiah*

- **Canny/motion VACE start/end percent**: start: 0.00, end: 1.00
  - Drive the whole clip
  - *From: Josiah*

- **Lightx2v lora strength**: 2-3 strength
  - Required strength for proper function with high noise pass
  - *From: Kijai*

- **Lightning lora strength**: 1.0 strength
  - Proper strength setting for lightning loras
  - *From: Kijai*

- **Fun Control high noise steps**: 4+4 instead of 2
  - Reduces ghosting issues in generated videos
  - *From: Kijai*

- **WanFM schedulers**: unipc works, lcm/dpm++_sde don't work
  - Compatibility with the bidirectional sampling method
  - *From: Kijai*

- **Video extension overlap**: 1 frame
  - For smooth blending when using WanVideo Blender node
  - *From: xwsswww*

- **Audio scale**: 3
  - Best results for MultiTalk with MagRef for lip-sync accuracy
  - *From: mdkb*

- **Denoise**: 0.50
  - Used with PUSA on native using image batch repeat
  - *From: hicho*

- **CFG for lightning LoRAs**: 2.0 first step, then 1.0
  - Lightning supposed to be CFG1 but works better if first step has higher CFG without lightning
  - *From: phazei*

- **Audio CFG**: high
  - Set high for MultiTalk, works on high noise model but most lipsync happens on low noise stage
  - *From: MysteryShack*

- **LightX2V rank**: 64
  - Used successfully with MagRef for 5 steps at 832x480x81 @ 24fps
  - *From: mdkb*

- **Context overlap**: 48
  - For better continuity with context windows
  - *From: Kijai*

- **VACE frames for single image**: 5 frames
  - First frame with change/mask, 4 empty gray frames
  - *From: Nekodificador*

- **Temporal frames calculation**: 81 frames = 21 latents
  - 4x VAE compression ratio
  - *From: Kijai*

- **FPS for WAN 2.2**: 12fps then RIFE doubling
  - Outputs appear sped up at 16fps compared to 2.1
  - *From: Fawks*

- **adapter_scale**: 0.7
  - Reduces over-animated mouth movements in Fantasy Portrait
  - *From: VRGameDevGirl84(RTX 5090)*

- **block_swap**: 40 blocks for 5090, 19-20 blocks for 1280x704
  - Enables higher resolution/longer videos by offloading to CPU RAM
  - *From: Ryzen*

- **steps**: 10 steps
  - Used for 3-minute 1280x720 81-frame generation
  - *From: Ryzen*

- **fuse_method**: linear or pyramid
  - Only accepted values for WanVideoContextOptions
  - *From: 𝕯𝖗. 𝕸𝖆𝖈𝖆𝖇𝖗𝖊 ☠*

- **high/low noise split**: 0.9 split (15 high, 25 low for 40 steps)
  - Original implementation timestep distribution
  - *From: Benjimon*

- **Training configuration**: 512 resolution for video, 768 and 1024 for images, 15 videos plus 2 datasets with 15 images each
  - Consumes 75GB RAM during training
  - *From: Ryzen*

- **Context window parameters**: 81 frame context size, 32 overlap, 6 steps
  - Reduces context drift and improves stability
  - *From: Kijai*

- **Lightning settings for less jiggling**: CFG=2 on HIGH, CFG=1 on LOW
  - Improves motion quality but takes more time
  - *From: Ashtar*

- **MMAudio fps requirement**: 25 fps
  - MMAudio expects 25fps input for proper audio generation
  - *From: Kijai*

- **Context overlap**: 32 or 48
  - Better consistency in long generations
  - *From: Josiah*

- **Divisible by**: 16 or 32
  - Prevents rounding errors in generation
  - *From: Kijai*

- **LightX2V T2V**: High pass: 0,3,3 strength, shift 8, 6 total steps split at 3
  - Decent quality at low step count
  - *From: hablaba*

- **LightX2V I2V**: High pass: 0,4,3,1,1, Low pass: 1 strength, 10 total steps
  - Good results for I2V
  - *From: hablaba*

- **CFG for LightX2V**: First high pass step CFG 2, all else CFG 1
  - Better quality balance
  - *From: hablaba*

- **Lightning LoRA strength**: 1.8/1.5 (high/low)
  - Prevents looping effects with skyreels lora
  - *From: NebSH*

- **Lightning LoRA application**: Second pass of high only then on low
  - Optimal application method for Lightning 6 steps
  - *From: . Not Really Human .*

- **Scene cut limit**: 2-3 scenes maximum
  - Best results, limited to 5 multishots in same prompt
  - *From: NebSH*

- **MultiTalk FPS**: 30
  - Better lip sync performance
  - *From: Charlie*

- **Audio CFG**: 2
  - Optimal audio control
  - *From: Charlie*

- **Audio scale**: 2.5
  - Better MultiTalk performance when other settings fail
  - *From: mdkb*

- **Denoise**: 0.7
  - When using add noise to samples true for talking models
  - *From: VRGameDevGirl84(RTX 5090)*

- **Add noise to samples**: true
  - Required for talking models to work properly
  - *From: VRGameDevGirl84(RTX 5090)*

- **LightX2V strength**: 0.8
  - Used for 6-step generation with good results
  - *From: Kijai*

- **DPM++/SDE sampler**: 6 steps
  - 17 minute generation time on 5090 with quality results
  - *From: Kijai*

- **MultiTalk CFG**: 3.0
  - Good baseline for lip sync quality
  - *From: samhodge*

- **MultiTalk scale**: 1.0 to 2.5
  - Depending on how enunciated you want the result
  - *From: samhodge*

- **Context windows**: 121,4,40
  - Good settings for identity preservation
  - *From: samhodge*

- **audio_scale**: 2.0
  - Provides better audio conditioning results
  - *From: Kijai*

- **fps for wav2vec embeds**: 25
  - MultiTalk trained at 25fps
  - *From: multiple users*

- **merge_loras**: disabled
  - Prevents noise issues with fp8_scaled models
  - *From: Kijai*

- **scheduler**: dmp++ sde over res_multistep
  - Less noisy previews, better quality
  - *From: Kijai*

- **InfiniteTalk steps with LightX2V**: 6-10 steps
  - Optimal for distill LoRA usage
  - *From: Kijai*

- **LoRA strength with LightX2V**: 0.8
  - Better to lower strength than increase steps
  - *From: Kijai*

- **Audio scale**: 1
  - Default setting works for most cases
  - *From: Kijai*

- **Blockswap for memory issues**: 20-40
  - Helps with OOM issues, start with 20 and increase if needed
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Frame window size**: 81
  - Should match normal generation frame count, don't change
  - *From: Kijai*

- **frame_window**: don't change default
  - Controls how many frames processed at once
  - *From: Kijai*

- **num_frames**: total desired frames
  - Sets the final video length
  - *From: Kijai*

- **VAE precision**: Wan2_1VAE_bf16.safettensors with bf16
  - Correct VAE and precision combination
  - *From: NC17z*

- **denoise for V2V**: 0.4
  - Used in V2V testing
  - *From: DawnII*

- **motion_frames for I2V**: 9
  - Matching their code implementation
  - *From: DawnII*

- **LoRA rank**: up to 64
  - Higher values hit diminishing returns and increase memory usage
  - *From: Kijai*

- **Motion frame**: 9
  - Default for new model, works fine and is faster than 25
  - *From: Kijai*

- **Audio CFG scale**: 3-5
  - Recommended range, makes generation take 3x time as it does 3 passes
  - *From: Kijai*

- **Frame window**: 81
  - Base model does best at 81 frames, shouldn't be changed
  - *From: Kijai*

- **LoRA strength**: 0.8
  - Lower strength helps with outfit variety when LoRA is overtrained
  - *From: Ryzen*

- **CFG**: 3
  - Allows negative prompts to work, CFG 1 doesn't use negatives
  - *From: Ryzen*

- **Wan 2.2 upscale parameters**: 4 steps, denoise 1.00, add noise to samples = true, start at step 2
  - For 720p to 1024p upscaling
  - *From: VRGameDevGirl84(RTX 5090)*

- **InfiniteTalk long generation**: 25 steps, shift 8, cfg 3.5, audio cfg 4.0
  - 2400 frames generation taking 2.5 hours
  - *From: seitanism*

- **Wan 2.2 scheduler**: euler beta
  - Works best according to user experience
  - *From: VRGameDevGirl84(RTX 5090)*

- **LightX2V LoRA usage**: 4 steps, 1 cfg
  - Produces less dynamic but cleaner results
  - *From: seitanism*

- **Audio CFG for lip sync**: 3-5
  - Works optimally for lip synchronization accuracy
  - *From: NC17z*

- **Manual sigmas for 4-step T2V**: [1.0000, 0.9375, 0.8750, 0.4375, 0.0000]
  - Linear scheduling gives better results than BetaSamplingScheduler
  - *From: phazei*

- **Runtime cache setting**: --cache-none
  - Prevents ComfyUI from tanking with high VRAM/DRAM usage
  - *From: samhodge*

- **InfiniteTalk long generation**: 2400 frames, 32 steps, no lora, 480x720x81, 9 motion frames, 3.5 cfg, 7 shift, 3.5 audio cfg scale, dpm++ sde, MAGREF+infinitetalk
  - Achieved stable 1+ minute generation with no visible degradation
  - *From: seitanism*

- **Vid2vid denoise for motion cleanup**: 0.65 denoise
  - Good balance for fixing spazzy motion from InfiniteTalk without losing quality
  - *From: samhodge*

- **Wan 2.2 FLF frame requirements**: Minimum 81 frames, maximum under 180 frames
  - Second input goes grey outside these bounds
  - *From: cyber jock*

- **InfiniteTalk V2V steps**: 4 total steps, start at 2
  - Optimal for video-to-video processing
  - *From: Kijai*

- **Light2XV LoRA strength**: 3 on high noise, 1 on low noise
  - Better performance than new speed LoRAs
  - *From: NebSH*

- **Motion frames for InfiniteTalk**: 35 motion frames
  - Reduces dead air frames at end of clips
  - *From: NC17z*

- **Audio scale adjustment**: Turn down audio scale
  - Mitigates prompt following issues in long generations
  - *From: DawnII*

- **fps**: 25
  - Model is really meant for 25fps
  - *From: Kijai*

- **motion_frames**: 9
  - Default overlap for smooth transitions between 81 frame windows
  - *From: seitanism*

- **start_step**: 2
  - For vid2vid, allows input video to establish before sampler takes over
  - *From: Kijai*

- **control_strength**: 0.0 to 0.1
  - Control can be overpowering, low strength works better
  - *From: Hashu*

- **Audio scale**: 2.5
  - Better lip movement in MultiTalk, otherwise lips don't move much
  - *From: mdkb*

- **High noise stage**: 2 steps without lora
  - First stage of native 2 ksampler setup
  - *From: Not Really Human*

- **Low noise stage**: 2 steps with lora
  - Second stage of native 2 ksampler setup
  - *From: Not Really Human*

- **Max frames in InfiniteTalk**: Adjustable beyond 1000
  - Default locks at 1000 but can be increased for longer audio
  - *From: JohnDopamine*

- **VACE mask fill**: Grey 0.5/128
  - Proper masking for inpainting
  - *From: ˗ˏˋ⚡ˎˊ-*

- **MultiTalk mask values**: Very dim grey (1,2,3)
  - For segmentation of different speakers
  - *From: samhodge*

- **Motion optimization**: LTX 4-5 on high noise, 1 on low noise, cfg=1
  - Maximum motion while retaining original image
  - *From: Instability01*

- **Audio scale for infinitetalk**: 1.5 default for vid2vid, 1.0 for i2v
  - Effect can be too weak in vid2vid
  - *From: Kijai*

- **CFG and shift for Fun 5B**: CFG 5, shift 5
  - Good results with flowmatch_pusa scheduler
  - *From: Blink*

- **LoRA strength for WAN 2.2**: 0.5 to 1.7
  - Range that works well, depends on LoRA epoch and quality
  - *From: seitanism*

- **Lightning sampling steps**: 8 steps (2/2/2/2)
  - 4-stage approach with different LoRA applications
  - *From: : Not Really Human :.*

- **CineScale RoPE scaling**: [1.0, 20.0, 20.0] for first sampler, [1.0, 25.0, 25.0] for second
  - Proper spatial frequency scaling for resolution upscaling
  - *From: Kijai*

- **Distill model parameters**: steps 4, cfg 1, shift 1
  - Proper settings for distilled models
  - *From: samhodge*

- **Wan 2.2 render performance**: 81 frames at 720p takes 82.76 seconds
  - Performance benchmark on fp8 scaled models
  - *From: Drommer-Kille*

- **5B Turbo parameters**: 4 steps, cfg 1.0, flowmatch_distill or dpm++_sde sampler
  - Optimized for the turbo model
  - *From: Kijai*

- **Cinescale workflow**: 50 steps first sampler, 50 steps second starting at step 15, bilinear upscale, RoPE scaling applied
  - Official implementation approach
  - *From: Kijai*

- **Linear 4 step sigmas with shift 5.0**: 0.9998, 0.9375, 0.8333, 0.6250, 0.0000
  - For custom sigma implementation
  - *From: Kijai*

- **Default frames for 5B**: 121 frames
  - Model default configuration
  - *From: Kijai*

- **CineScale LoRA strength**: 0.6
  - Used for 1.3b upscaling at 0.6 denoise
  - *From: DawnII*

- **Film grain LoRA rank**: Rank8
  - Works for style LoRAs and files are only 73mb
  - *From: Drommer-Kille*

- **VACE strength for inpainting**: 0.5
  - Strength of 1 tries to fix subject exactly on mask area, 0.5 is better for some cases
  - *From: SonidosEnArmonía*

- **WAN 2.2 5B Turbo wrapper**: 4 steps, cfg 1.0, flowmatch_distill scheduler
  - Proper turbo model settings
  - *From: Kijai*

- **WAN 2.2 5B Turbo native**: 5 steps, euler simple, cfg 1.0 or custom sigmas for 4 steps
  - 4 steps with normal schedule doesn't work well
  - *From: Kijai*

- **CFG split for 20 steps without LightX**: cfg 3.5, switch at 11 steps for dpm++sde, 2nd sampler 1 cfg
  - Proper dual sampler setup
  - *From: crinklypaper*

- **InfiniteTalk motion_frame**: overlap amount between clips
  - Controls frame overlap in continuous generation
  - *From: Kijai*

- **InfiniteTalk frame_window_size**: model input size
  - Defines model context window
  - *From: Kijai*

- **audio_scale**: 2.0
  - 3.0 causes issues, 2.0 works great
  - *From: Kenk*

- **frame rate for multitalk**: 25fps for fast movements, 16fps acceptable for slower content
  - Better motion handling
  - *From: Kenk*

- **euler/beta with 8 steps**: 8 steps
  - Produces superior quality with Wan 2.2 Low I2V
  - *From: gordo*

- **LoRA strength with CFG Schedule**: 2.0
  - Needed to make LoRAs work with CFG Schedule
  - *From: Drommer-Kille*

- **Phantom frame count**: 121 frames
  - Must be 121 frames else things go wrong, causes midgets at other frame counts
  - *From: mdkb*

- **Loop sampling overlap calculation**: 81 + 81 - 9 = 153 for exactly 2 windows
  - Must account for motion_frame overlap when calculating window frames
  - *From: Kijai*

- **Virtual VRAM**: 14 GB
  - Used religiously for native workflows to help with OOMs
  - *From: mdkb*

- **VRAM usage limit**: 95%
  - Above 95% on Windows causes severe slowdowns
  - *From: Kijai*

- **I2V shift threshold**: 0.9
  - Original default for I2V vs 0.875 for T2V
  - *From: Kijai*

- **Block swap amount**: 40 blocks
  - For 1280x720x121 frames on limited VRAM setups
  - *From: Dream Making*

- **Prefetch blocks**: 1
  - More didn't make a difference in testing
  - *From: Kijai*

- **CFG end percent**: 0.01
  - Applies CFG only to initial step
  - *From: DawnII*

- **Control latent strength**: 0
  - Keeps generation completely static
  - *From: DawnII*

- **Lightning/LightX2V weight**: 0.8
  - Good balance for both high and low noise
  - *From: CJ*

- **MultiTalk VRAM usage**: ~2.5GB more at Q8
  - Can be divided by block swap amount
  - *From: Kijai*

- **CFG schedule**: 3.5 in high sampler, 1 in low sampler
  - Maintains prompt following while preserving native image quality
  - *From: Drommer-Kille*

- **InfiniteTalk steps**: 4-6 steps with lightx2v lora
  - 6 is better than 4, more than 6 gives minimal improvements
  - *From: Kijai*

- **Frame window size for Skyreels**: 121
  - Skyreels 720p default supports 121 frames vs normal I2V's 81
  - *From: Kijai*

- **CFG**: 2
  - Used in successful T2V low noise examples
  - *From: Gateway {Dreaming Computers}*

- **Steps**: 8
  - Better for single frame VACE generation than 4 steps
  - *From: hicho*

- **Sigma split**: 0.875
  - Optimal sigma configuration mentioned
  - *From: JalenBrunson*

- **VACE strength**: 2
  - Setting used in successful generation
  - *From: hicho*

- **Wan 2.2 without Light2v LoRAs**: 6 steps total, split at middle, very first step using cfg
  - General recommendation from Kijai
  - *From: Kijai*

- **With Lightning LoRAs**: Don't go past 10 steps, 6 can be enough, split point in middle plus/minus 1 step
  - Optimal for distill loras
  - *From: Kijai*

- **High/Low noise split for 2.2**: 8 steps total, 4 on both sides instead of 3/17 split
  - More balanced than 3 high noise, 17 low noise
  - *From: Kijai*

- **lightx2v LoRA strength for T2V**: 1.5-2 on high, 1 on low
  - User experience for T2V, vs 3/1 for i2v
  - *From: Gentleman bunny*

- **DWPose resolution**: Ratchet up resolution in standard DWPose node
  - Higher resolution makes difference for eye line control
  - *From: JalenBrunson*

- **LoRA strength per step**: First step no lora, 2nd step strength 2, rest at 1
  - Allows using CFG on first step
  - *From: Kijai*

- **Video generation length for speed**: 5-7 seconds
  - Runs almost at same speed as real-time for I2V with InfiniteTalk
  - *From: Kenk*

- **Audio sample rate**: 16000
  - Required sample rate for audio processing in S2V model
  - *From: DawnII*

- **Steps for Wan 2.2 I2V**: 6-8 steps instead of 4
  - 4 steps too low, causes poor quality
  - *From: JohnDopamine*

- **Alpha/Beta values**: 0.6/0.6
  - Default recommended values
  - *From: Ablejones*

- **Shift value for troubleshooting**: 8 for both samplers
  - May help with blurry results
  - *From: screwfunk*

- **Input FPS**: 50 fps hardcoded
  - Built into the model architecture
  - *From: Kijai*

- **Output FPS**: 16 fps
  - Video saved at this rate
  - *From: Kijai*

- **Resolution formula for S2V**: (width÷16) × (height÷16) × frames ÷ 30 = whole number
  - Prevents einops errors
  - *From: patientx*

- **CFG Skimming with Lightning**: 4 steps (2+2)
  - Fast generation with LoRA on HIGH & LOW
  - *From: : Not Really Human :*

- **Resolution limitations for 24fps**: Only 368x384 works reliably
  - Higher resolutions may work but require more GPU power
  - *From: patientx*

- **Frame limits**: 105 frames maximum, 109 frames causes error
  - Model has frame count limitations
  - *From: N0NSens*

- **Small resolution settings**: 192x192 145 frames, 384x384 145 frames work
  - Lower resolutions are more stable for longer sequences
  - *From: patientx*

- **VACE strength reduction**: Reduce strength to remove openpose artifacts
  - Prevents control inputs from appearing in output
  - *From: xwsswww*

- **Steps with LightX2V**: 6 steps
  - worked better on that native example with the lightx2v lora and 6 steps
  - *From: Kijai*

- **CFG for S2V**: 3.5
  - Used in native workflow test
  - *From: Vérole*

- **Block swap for WanWrapper**: 20-30 blocks
  - I use block swap 20 with wan 2.2 workflows if I am targeting 832x480x81
  - *From: patientx*

- **Custom sigmas for 4-step Lightning**: [1.0, 0.75, 0.5, 0.25] with shift 5
  - 4 linear sigmas work better than normal schedulers
  - *From: Kijai*

- **CFG and Audio CFG scale**: 2.2 for both
  - Good balance for InfiniteTalk results
  - *From: Antey*

- **Steps for S2V**: 6 steps
  - Good quality, could potentially use less
  - *From: Kijai*

- **CFG for S2V**: 1
  - Works well with LightX2V at strength 1
  - *From: ingi // SYSTMS*

- **Lightning LoRA steps**: 4 steps with 4.5/3.5 CFG
  - Produces acceptable results
  - *From: Mu5hr00m_oO*

- **Audio scale and audio_cfg_scale**: 2.2
  - Improved InfiniteTalk results
  - *From: Antey*

- **LoRA strength for LightX2V**: 0.3
  - Much lower strength needed when combining with other LoRAs
  - *From: gordo*

- **Pose condition multiplier**: 0.5
  - Reduces teeth artifacts while maintaining pose control
  - *From: Kijai*

- **Steps for S2V**: 6 steps
  - Perfect results achievable with proper lora merge
  - *From: mamad8*

- **S2V generation steps**: 8 steps
  - Used with 3 CFG and 0.5 lora strength
  - *From: hicho*

- **LCM steps**: 5 steps
  - Fast inference with LCM sampler
  - *From: Kijai*

- **LightX2V LoRA strength for High/Low noise models**: 3.0 strength at high noise, 1.0 at low noise
  - Community consensus for best results with Wan 2.2 speed LoRAs
  - *From: N0NSens*

- **S2V model frame generation**: Can generate 35+ seconds of video
  - Model capable of long form generation, may degrade less with guiding images at every step
  - *From: comfy*

- **Training steps for character LoRAs**: 1k-3k steps
  - Sufficient for character training, 3000 steps max recommended on fal
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Context windows bucket length**: Set to frame length
  - For context windows method, just set bucket length to frame length and it works
  - *From: Kijai*

- **Steps for ultra HD renders**: 100+ steps
  - At 720p+ with high motion, noticeable improvements when using ultra high steps
  - *From: Neex*

- **model loader device**: offload_device
  - Prevents memory issues and OOM errors
  - *From: Kijai*

- **video encoder tiling**: enabled
  - Helps with VRAM requirements and prevents OOM
  - *From: T2 (RTX6000Pro)*

- **Uni3C strength**: 3 at high pass
  - Proper strength setting for Uni3C control
  - *From: N0NSens*

- **Framepack shift**: pretty low
  - Higher shift values can cause issues with Framepack
  - *From: Kijai*

- **ComfyUI launch flag**: --reserve-vram 5
  - Forces reservation of VRAM to prevent OOMing
  - *From: Juampab12*

- **CFG schedule**: cfg 5 first step, cfg 1 next 2 steps (high) with lightx 3 str, then 3 steps 2.5 lightx cfg1 (low)
  - Working FLF setup
  - *From: Juampab12*

- **Start step for vid2vid**: 2
  - To avoid trash frames at the beginning
  - *From: N0NSens*

- **Context window inference time**: 501 frames at 640x640 with 6 steps takes 5:56
  - Performance benchmark on 5090
  - *From: Kijai*

- **S2V pose strength**: Lower strength on first step only
  - Less strict control while still maintaining pose guidance
  - *From: Kijai*

- **FantasyPortrait steps**: First step only
  - Reduces character changes while maintaining projection benefits
  - *From: Kijai*

- **Context window overlap/stride**: 48 overlap, 10 stride
  - For high noise pass in 2.2 context generation
  - *From: Kijai*

- **I2V steps**: 30 steps 15/15, dmpp_sde/beta
  - Settings used for good I2V results
  - *From: ArtOfficial*

- **Memory allocator**: 0
  - Makes system give memory back to OS more aggressively
  - *From: comfy*

- **Lightx2v LoRA**: 8 steps, CFG 2.5 or 3.0, strength 1.0
  - Better results with native S2V
  - *From: Ablejones*

- **InfiniteTalk window size and overlap**: Window size and motion_frame controls overlap
  - Controls how much frames overlap in looping
  - *From: Kijai*

- **Frame limits for stability**: Max 81 frames stable without extension methods
  - Beyond that may cause memory issues
  - *From: Mu5hr00m_oO*


## Concepts Explained

- **MoE noise expert split**: Wan 2.2 uses separate High and Low noise expert models in MoE architecture
  - *From: general discussion*

- **Step distribution**: Steps split between models: 0-4 in first pass, 4-8 in second pass for 8 total steps
  - *From: GOD_IS_A_LIE*

- **Context windows in WAN**: Feature allowing multiple scenes in single generation using | separator between prompts
  - *From: avataraim*

- **VACE strength parameter**: Controls how strongly VACE modifies the video, affects background stability vs oversaturation
  - *From: seitanism*

- **PyTorch memory allocation behavior**: Keeps RAM allocated when moving models between RAM/VRAM, can't free it while objects exist
  - *From: Kijai*

- **RadialAttention token divisibility**: Not just resolution but final token count needs to be divisible by block size
  - *From: Kijai*

- **High/Low noise expert split**: WAN 2.2 uses MoE architecture with separate models for high noise (early steps) and low noise (refinement steps)
  - *From: ArtOfficial*

- **Context windows in video generation**: Method to generate longer videos by processing in overlapping segments without VRAM increase or quality degradation
  - *From: Kijai*

- **Blockswap**: Memory optimization technique, available in native workflows but not needed with sufficient VRAM
  - *From: IceAero*

- **LightX2V LoRA**: Distillation lora that makes the model work without using cfg and at lower step count, similar to high and low cfg
  - *From: Kijai*

- **Context windows with 5B**: Each step does multiple model predictions with different parts of latents and blends them together, using 81 or 121 frames context vs AnimateDiff's 16
  - *From: Kijai*

- **Block swapping**: Only reports what the weights use, rest of the processing uses additional VRAM
  - *From: Kijai*

- **5B timestep per frame**: Works like Pusa/DiffusionForcing - technically timestep per frame, practically works with single image input and first timestep zeroed
  - *From: Kijai*

- **Timesteps in noise scheduling**: Conventional way of splitting noise schedule into 1000 discrete steps, informs model how noisy image is at current step
  - *From: aikitoria*

- **High vs Low pass models**: Low Pass = Wan 2.1 (refined), High Pass = new Wan 2.2 architecture
  - *From: The Shadow (NYC)*

- **Sigma vs Timestep**: Timestep in Wan code is sigma scaled by 1000, different from ComfyUI where timesteps create evenly spaced values for sigmas
  - *From: aikitoria*

- **High/Low noise model split**: High noise model used when timestep above boundary, low noise for below boundary
  - *From: aikitoria*

- **Context window overlap**: How much each window overlaps with others, helps blending but makes generation slower due to more model predictions
  - *From: Kijai*

- **Stride in context windows**: 1 latent = 4 frames, so stride of 4 = disabled, goes frame by frame
  - *From: Kijai*

- **Pyramid vs Linear fuse**: Pyramid weights middle overlap frames more heavily, Linear does straight 50/50 blend
  - *From: thaakeno*

- **Start step in V2V**: Controls how much video changes - lower values change more, higher values stay closer to input
  - *From: thaakeno*

- **High noise vs low noise models**: 2.2 uses MoE with separate expert models for high and low noise processing
  - *From: BondoMan*

- **FLF (First Last Frame)**: Setting first and last frames and letting the model work out what's in between
  - *From: Juampab12*

- **VACE strength**: Controls all VACE functionality with no separation between different aspects
  - *From: Kijai*

- **First-Last-Frame to Video (FLF2V)**: Method of conditioning video generation with specific first and last frames
  - *From: Rainsmellsnice*

- **Grey frames in Wan 2.2**: Non-guiding frames are represented as grey, can be manually specified in input
  - *From: comfy*

- **High noise vs Low noise models**: Wan 2.2 has different models for different noise levels, with different capabilities
  - *From: Kijai*

- **High/Low noise model split**: High model handles motions, low model handles detail in 2.2 architecture
  - *From: screwfunk*

- **Blockswap**: Technique to use more blocks by swapping between VRAM and RAM
  - *From: Ryzen*

- **TCFG**: New experimental feature that fixes strobing issues while maintaining quality
  - *From: phazei*

- **Start/end steps in V2V**: Similar to changing denoise in classic video-to-video workflows
  - *From: Draken*

- **FFLF (First-Frame-Last-Frame)**: Feature that morphs between start and end images for video generation
  - *From: thaakeno*

- **fp8 matrix multiplication**: fp8 * fp8 = bad quality, but (fp8 -> fp16) * (fp8 -> fp16) = good quality
  - *From: Kijai*

- **Block swap**: One full block is ~700MB in fp16, swapping all blocks minimizes VRAM usage to just the active block
  - *From: Kijai*

- **Batch size in video generation**: Number of images processed per iteration - higher batch size leads to more temporally stable videos
  - *From: MiGrain*

- **FPS1 LoRA concept**: LoRA that generates videos at 1 frame per second instead of 16, used for storyboarding and creating longer scene structures
  - *From: mamad8*

- **Model switching sigma**: Sigma value of 0.875 where Wan team intended the transition between high and low noise models to occur
  - *From: Ablejones*

- **Multistep sampler artifacts**: Burning/artifacts that occur when multistep samplers use latents from different models in their calculations
  - *From: Ablejones*

- **LoRA timestep scheduling**: Feature that allows controlling LoRA strength per step, 0 skips applying it altogether on that step, enables curves and dropoff control
  - *From: Kijai*

- **Self-forcing training**: Training method that doesn't require a dataset, beauty of lightx2v approach, anyone with compute could do it
  - *From: Kijai*

- **Adaptive LoRA ranks**: Each layer rank calculated based on difference, some layers rank 500+ while less important ones lower
  - *From: Kijai*

- **shift**: Biases denoising steps - higher shift gives more steps to 'cook' before details are established, affects composition/movement/color. Shift 1 with simple scheduler removes exact same noise each step
  - *From: Ablejones*

- **flashboot**: Runpod feature where if worker is 'warm', generation starts instantly even from idle state
  - *From: gokuvonlange*

- **noise boundary**: Wan 2.2 has trained boundary between high noise and low noise models, but using shift 1 ignores this boundary yet produces better T2I results
  - *From: aikitoria*

- **High noise vs Low noise expert split**: Wan 2.2 uses MoE architecture where high noise expert handles composition/structure, low noise expert handles refinement. Different step ratios needed for T2V vs I2V.
  - *From: aikitoria*

- **Block swap calculation**: LoRA memory impact can be calculated by dividing LoRA size by block swap count
  - *From: Kijai*

- **MoE High/Low Noise Expert Split**: Wan 2.2's architecture splits processing between high noise (motion/big concepts) and low noise (details/style) experts
  - *From: Juampab12*

- **VACE Strength**: Controls how strictly the system applies reference/prompt to masked area - high strength (1.0) forces subject placement, lower gives more realistic freedom
  - *From: SonidosEnArmonía*

- **720P Distilled Model Formula**: 720P distilled model = 720P original model + (480P step distillation - 480P original model), not a native 720P model
  - *From: Dan*

- **High/Low noise expert split**: Wan 2.2 uses different models for high and low noise levels, allowing different LoRAs on each
  - *From: Kijai*

- **Sigma cutoff for I2V**: I2V has sigma cutoff at 875, affecting how steps are distributed between high/low noise models
  - *From: DawnII*

- **Lightning LoRA**: 4-step distillation LoRAs for faster generation, separate high and low noise versions
  - *From: gokuvonlange*

- **Mixed LoRA approach**: Using different LoRAs for high noise vs low noise passes to optimize quality
  - *From: Doctor Shotgun*

- **GGUF model sizing**: GGUF is just a storage format, higher size means higher quality packing, not more training data
  - *From: Kijai*

- **FastWan model**: Distilled version of Wan 5B that works at 3-6 steps without CFG, converted from FastVideo team's diffusers version
  - *From: Kijai*

- **Lightning vs LightX2V**: Lightning is new 4-step distill LoRA, LightX2V is older speed LoRA - they are different approaches
  - *From: DawnII*

- **Low noise model seeding**: Low noise model is fixed and not really seeded in typical sense, can be 0 fixed or same seed as high
  - *From: Lodis*

- **work_device_cpu**: Keeps as many large tensors on CPU (system RAM) as possible until needed for actual model inference
  - *From: Ablejones*

- **FLF (First-Frame-Last-Frame)**: Morphing technique that interpolates between a first and last frame to create video transitions
  - *From: thaakeno*

- **Blockswapping**: Memory management technique that swaps model blocks to reduce VRAM usage during inference
  - *From: screwfunk*

- **High/Low noise expert split**: Wan 2.2's MoE architecture separates processing between high and low noise regions
  - *From: context*

- **Scene cutting for subject preservation**: Technique using prompts like 'scene abruptly hard cuts to' to maintain subject resemblance across different contexts without specialized models
  - *From: Jonathan*

- **Split sampling 2.2**: Using separate high noise and low noise models in Wan 2.2 architecture for better generation quality
  - *From: Kijai*

- **Context windowing**: Samples the model multiple times per step and blends results, slows down generation but enables longer sequences
  - *From: Kijai*

- **Scene transition prompting**: Using phrases like 'the scene immediately and abruptly cuts to' to maintain character consistency across scene changes
  - *From: Jonathan*

- **VAE compatibility**: WAN and Qwen-Image use identical VAE architectures allowing cross-model latent space operations
  - *From: fredbliss*

- **High/Low Pass sampling**: Wan 2.2 uses separate high and low noise samplers that can be configured independently with different LoRAs and settings
  - *From: various*

- **Context windows**: Method for generating longer videos, but challenging with I2V models since they need image input in each window
  - *From: Kijai*

- **Quantile LoRA**: Alternative to numbered rank versions (64/128/256) with self-forcing behavior
  - *From: The Shadow (NYC)*

- **Self attention splitting**: Method to control scene transitions by splitting attention at specific steps, stronger split good for scene changes
  - *From: Kijai*

- **Patch embedding**: Critical layer in diffusion models that differs significantly between Wan 2.1 and 2.2, affecting VACE compatibility
  - *From: Kijai*

- **Context window**: Technique for processing high-resolution videos within VRAM limitations by processing in chunks
  - *From: thaakeno*

- **DisableNoise node**: Node that prevents adding new noise when continuing a generation, used instead of RandomNoise for save/load latent workflows
  - *From: Ablejones*

- **--cache-none flag**: ComfyUI flag that automatically clears memory after each node to manage RAM usage
  - *From: Kijai*

- **Block merging**: Technique to merge specific transformer blocks between models, with early blocks affecting composition and later blocks affecting style
  - *From: Kijai*

- **HN/LN models**: High Noise and Low Noise model variants in the two-stage generation process
  - *From: Kijai*

- **fp8 quantization conversion**: Converting between e4m3 and e5m2 formats loses quality on both sides, should be avoided
  - *From: Kijai*

- **Add noise in video generation**: Setting that adds noise to the process, only has effect when using LoRAs, changes results significantly
  - *From: Kijai*

- **VACE control strength ratios**: Settings that control how strongly VACE applies its effects, 1:1 ratio works better than 3:1.5
  - *From: Lodis*

- **Adaptive rank LoRA**: Highest rank Lightning LoRA variant at around rank 256, with FFN layers up to rank 319
  - *From: Kijai*

- **Lightning LoRA brightness forcing**: New Lightning LoRAs force daylight scenes due to dataset limitations, unlike older LightX2V versions
  - *From: Multiple users*

- **VACE architecture advantage**: VACE doesn't fine-tune base WAN - works as extra layers, allowing combination with other models like Phantom
  - *From: Piblarg*

- **Video token calculation**: For Wan 2.1/2.2 14B: width/16 * height/16 * (length+3)/4. For Wan 2.2 5B: width/32 * height/32 * (length+3)/4
  - *From: .: Not Really Human :.*

- **Block swapping impact**: Absolute hell for speed when using rented GPUs
  - *From: MysteryShack*

- **MoE (Mixture of Experts) in Wan 2.2**: High/low noise expert split architecture, though the use of MoE terminology may be a stretch
  - *From: TK_999*

- **Sigma boundary thresholds**: Set to not split in half, with boundary at 0.875 for T2V and 0.9 for I2V
  - *From: DawnII*

- **Merge LoRA function**: Merges LoRA with model before inference, slower first time but faster subsequent runs and saves VRAM
  - *From: pagan*

- **Temporal inpainting**: InP models can take any number of input frames and fill in empty frames between them, like start/end frame interpolation but more flexible
  - *From: Kijai*

- **52 channel input**: New Fun Control models use 52 input channels instead of standard 48, with unknown purpose for extra 4 channels
  - *From: Kijai*

- **Dual sampler setup**: 2.2 models require specific dual sampler configuration for high/low noise processing
  - *From: Kijai*

- **Signal to noise ratio threshold**: The boundary point at 0.5 SNR where model switches from high noise to low noise expert, occurs around step 875 in original implementation
  - *From: MysteryShack*

- **4n+1 frame format**: WAN automatically trims frame count to fit this mathematical requirement
  - *From: Nekodificador*

- **High/Low noise expert split**: WAN 2.2 uses different models for high sigma (high noise) and low sigma (low noise) denoising steps
  - *From: Kijai*

- **Modified sigma calculation**: modified_sigma = (shift * base_sigma) / (1 + (shift - 1) * base_sigma) - used to determine model switching point
  - *From: fredbliss*

- **Denoise parameter**: Sets start step to fraction of total steps, e.g., 4 * 0.4 = 1.6 rounded up to 2 steps
  - *From: Kijai*

- **50% Signal-to-Noise Ratio threshold**: Theoretical optimal point for switching between high and low noise models, but varies for distilled models
  - *From: MysteryShack*

- **Sigma threshold switching**: T2V uses 0.875 threshold, I2V uses 0.9 threshold to determine when to switch from high to low noise model based on noise levels in generation
  - *From: Kijai*

- **FP8 weight limitations**: PyTorch only supports FP8 matrix multiplication, not FP8+FP8 addition or multiplication, requiring upcasting for LoRA application
  - *From: Kijai*

- **UDP refinement**: Unbiased Data Processing refinement in Sapiens including distribution-aware coordinate decoding, sub-pixel accuracy using Gaussian blur and Taylor expansion
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Radial attention**: Sparse attention with mask specialized for video, requires tuning for which steps and blocks it's applied to
  - *From: Kijai*

- **Split-screen generation**: Prompting technique for creating synchronized dual perspective videos with detailed scene descriptions
  - *From: 🦙rishappi*

- **PUSA intended use**: Designed to cheaply convert Wan 14B T2V to I2V model using only $500 and 4000 videos. Works with T2V model + LoRA + extra_latents, not just slapping it with other LoRAs
  - *From: Kijai*

- **Context windows in Wan**: Background differs a lot between context windows because each window uses different seed. More overlap and stride can help consistency
  - *From: Kijai*

- **High/Low noise models in Wan 2.2**: High noise model brings very noisy image to slightly less noisy (basis for video), low noise model brings noisy image to proper end result. Two-stage process designed to work together
  - *From: izashin*

- **3-2 pulldown**: Video to film conversion technique: 3x interpolate source fps to higher fps, then strip out every other frame to reach target fps (e.g., 16fps -> 48fps -> 24fps)
  - *From: nacho.money*

- **VAE approximation**: vae_approx used for previews - approximates VAE giving rough view, pretty much instant so can be used for live previews
  - *From: Kijai*

- **Attention sink**: Phenomenon where models latch onto initial tokens/frames as a 'sink' for attention, similar to BOS tokens in LLMs. Could be key to enabling video extension
  - *From: fredbliss*

- **Temporal mask**: Mask used with Fun InP where black areas are generated and white areas are kept (opposite to VACE)
  - *From: Kijai*

- **Fun 2.2 control model**: 5B controlnet model that supports both I2V and T2V, can do temporal inpainting but lost reference input capability
  - *From: Kijai*

- **Fun 2.2 low noise limitation**: Cannot finish at good quality, better to use 3rd sampler without Fun at end
  - *From: Kijai*

- **Style bias in Lightning LoRA**: 2.2 Lightning makes everything bright and oversaturated, especially problematic for dark scenes
  - *From: Kijai*

- **MoE architecture difference**: 5B uses MoE with High/Low noise expert split, different capabilities than 14B
  - *From: community discussion*

- **Block swap**: System for swapping model blocks between GPU and CPU to manage VRAM usage, with transfer and compute time profiling
  - *From: Kijai*

- **High/Low model split**: MoE architecture splits processing between high noise (0.875-1.0 timesteps) and low noise (0.0-0.875 timesteps) expert models
  - *From: Alisson Pereira*

- **Prefetch**: Option to preload blocks for block swap to reduce transfer time impact
  - *From: Kijai*

- **FFLF**: First-Frame-Last-Frame morphing technique
  - *From: R.*

- **LoRA strength scheduling**: Varying LoRA strength over denoising steps, supports any node that outputs float list
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Split attention in Stand-In**: Uses rope split where LoRA is applied to selfattn q k v only
  - *From: Kijai*

- **Dequant operation**: Operation that slows down GGUF models by ~20%, has custom kernel for Linux only
  - *From: Kijai*

- **LoRA scheduling**: Varying LoRA strength over denoising steps with interpolation between values
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Differential diffusion**: Technique using masks for selective inpainting to control which areas get denoised
  - *From: Juan Gea*

- **Shared attention mechanism**: Stand-In's method of incorporating face reference without adding extra latents to the full sequence
  - *From: Kijai*

- **Block swap**: Memory optimization technique that swaps model blocks to manage VRAM usage
  - *From: patientx*

- **FFLF**: First Frame Last Frame - a morphing technique for video generation
  - *From: Charlie*

- **Stand-in LoRA**: A LoRA that allows using reference images for character consistency, similar to Phantom but with different training
  - *From: Kijai*

- **res_2s sampler**: Higher order method with smaller truncation error, does double the steps essentially
  - *From: Instability01*

- **TeaCache**: Method for skipping steps in model inference for speed optimization
  - *From: Kijai*

- **Block swapping**: Memory management technique that automatically moves model blocks between VRAM and RAM as needed
  - *From: Kijai*

- **Context windows**: Technique for extending video generation by overlapping and blending segments
  - *From: Kijai*

- **Uni3c**: Control method to lock camera position for stable extended generation
  - *From: Kijai*

- **FFLF**: First Frame Last Frame - technique for video morphing between start and end frames
  - *From: AR*

- **Wan v3 is Wan 1.3B (WanFun)**: Clarification that the v3 model refers to the 1.3B parameter WanFun model
  - *From: Kijai*

- **Fun Control patch embedding**: Uses 52 input channels combining noise (16) + image conditioning (16) + control (16) + mask (4)
  - *From: Kijai*

- **Wan 2.2 LN as LoRA**: The Low Noise model can be extracted as a LoRA and applied to other Wan 2.1 models to transfer improvements
  - *From: Ablejones*

- **kv_cache feature**: Performance optimization that applies model only once then caches and reuses k and v values on remaining steps, but may affect quality
  - *From: Kijai*

- **pdf in FantasyPortrait context**: Unclear face detection system, possibly 'point-detection'
  - *From: Kijai*

- **Stand-in**: New lip sync model similar to Live Portrait but as Wan adapter for 2.1 14B I2V
  - *From: Kijai*

- **Reference latent**: What is used as the first latent in each context window that doesn't include the actual first frame
  - *From: Kijai*

- **MAGREF**: I2V model for character subject consistency that works as reference-to-video instead of start-frame-to-video
  - *From: gokuvonlange*

- **fp8 scaled models**: Quantized models with specific scaling to minimize quality loss compared to standard fp8
  - *From: Kijai*

- **VSA model**: Some sort of sparse attention architecture, wouldn't work with regular workflows
  - *From: Kijai*

- **Context windows**: Method for generating longer videos beyond normal limits
  - *From: Kijai*

- **Block swap**: Memory management technique to fit large models in limited VRAM
  - *From: nacho.money*

- **Higher rank LoRA**: Closer to the original model it's extracted from, stronger but not always better
  - *From: Kijai*

- **FusionX model**: Wan 2.1 with 5-6 LoRAs baked in, then saved, then single LoRA extracted from that
  - *From: Kijai*

- **PD-FGC**: 222 keypoint face detection system used in Fantasy Portrait
  - *From: Kijai*

- **Block offloading**: Memory management technique that can sometimes cause allocation crashes
  - *From: Obsolete*

- **Block swap**: Manual memory management that reduces constant memory use underneath VRAM peaks
  - *From: Kijai*

- **NAG (Negative prompting)**: Method to have negative prompting when not using CFG, mostly when CFG is set to 1
  - *From: Kijai*

- **FLF (First-Last-Frame)**: Morphing technique where video transitions from first frame to last frame
  - *From: Kijai*

- **Graph breaks in torch.compile**: Points where compilation is interrupted and resumed, can cause memory issues
  - *From: Kijai*

- **Reserve VRAM**: Tells model loading code to assume it needs X GB more memory than estimated, preventing OOM or Windows shared memory spillover
  - *From: Kosinkadink*

- **NAG (Negative Augmented Generation)**: Allows negative conditioning at CFG 1.0 while maintaining speed benefits
  - *From: DawnII*

- **Block swapping**: Automatic VRAM management that moves model blocks between VRAM and RAM as needed
  - *From: Persoon*

- **VACE reference behavior**: Works more like FaceID V2 than a simple IPAdapter, requiring high quality reference images for best results
  - *From: Nekodificador*

- **Lightning lora censoring**: At high strengths, lightning loras generate objects to block body parts, possibly due to distillation differences from lightx2v
  - *From: MysteryShack*

- **WanFM method**: Does start-to-end prediction, then end-to-start prediction with reverse RoPE and blends them together each step
  - *From: Kijai*

- **WanFM (Frame Morphing)**: Sampling method that does forward and reverse passes on each step, reversing input and RoPE frequencies for reverse pass, then blending results
  - *From: Kijai*

- **First frame encoding difference**: VAE encodes first frame differently (partial latent) vs full latents, causing flash effect if you use full latents for continuation
  - *From: Kijai*

- **Block swap**: ComfyUI feature that uses disk space to handle memory overflow, but doesn't automatically clear after generation
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Self-forcing**: A training technique, not something you 'use' - the model is trained with self-forcing method
  - *From: Kijai*

- **WanFM sampling**: Method that does 2 model predictions per step, forwards and backwards, then blends those results
  - *From: Kijai*

- **Causal sampling**: Different from self-forcing, was used for first causvid and first self-forcing models, causes motion quality degradation when used with 21 latents instead of intended 3
  - *From: Kijai*

- **Context stride**: Controls frame movement to next batch in context windows - documented in AnimateDiff evolved
  - *From: Kijai*

- **I2V limitations with context windows**: I2V can't work well with context as video never finished and every window needs start image
  - *From: Kijai*

- **VACE control video behavior**: Never adds anything, only for replacing. VACE only adds reference image to latents
  - *From: Kijai*

- **Start to End Frame node usage**: Only for I2V models, adds frames to latents for 5B model
  - *From: Kijai*

- **CFG early step behavior**: Classifier-free guidance shows negative prompt content in early diffusion steps before converging to positive
  - *From: Kijai*

- **Block swap**: Technique to offload model blocks to CPU RAM to fit larger models/higher resolutions in limited VRAM
  - *From: Ryzen*

- **GGUF quantization overhead**: GGUF models are compressed and need decompression during inference, making them slower despite smaller size
  - *From: . Not Really Human .*

- **High/low noise expert split**: Wan 2.2 uses different model experts for different noise levels in the denoising process
  - *From: Benjimon*

- **Context windows for I2V models**: Each window is a separate model prediction on every step. I2V models requiring start images try to start from it for each window, but can't use last frame as it's never fully denoised
  - *From: Kijai*

- **VACE compatibility**: VACE is an addon for T2V models only, cannot work with I2V models unless retrained. Phantom works with VACE because it's a T2V model finetuned to use references
  - *From: Kijai*

- **Control signals for stability**: Anything that controls generation like VACE control, audio control, uni3c - plain text conditioning works very poorly for long stable generations
  - *From: Kijai*

- **Context frames vs total frames**: Memory usage based on context frames * width * height, not total output frames
  - *From: Kijai*

- **FP8 matmul vs emulated FP8**: True FP8 matmul only on supported cards, otherwise upcast to base precision
  - *From: Kijai*

- **GGUF dequantization**: GGUF has to be dequantized on the fly, adding extra calculations
  - *From: Kijai*

- **Diffusion forcing in Skyreels**: Method that batches images into latent instead of single one for better contextual understanding of motion
  - *From: sawlike*

- **Multi-stage sampling**: Using different CFG settings across sampling stages, typically CFG for early steps, no CFG for later steps
  - *From: Kijai*

- **Block swapping**: Memory management technique that only loads needed blocks directly and swaps the rest
  - *From: Kijai*

- **MoE (Mixture of Experts)**: Wan 2.2 architecture with High/Low noise expert split
  - *From: MysteryShack*

- **Context windows vs looping method**: Two different approaches - context windows samples in chunks, looping samples whole thing in loop
  - *From: Kijai*

- **Scaled models**: Modified precision versions that must be used consistently across main and extra models
  - *From: Kijai*

- **InfiniteTalk**: Updated MultiTalk model that allows infinite/endless generation with audio control, works as endless I2V
  - *From: Kijai*

- **MAGREF**: Reference system that provides more freedom and stability, works at 480p resolution
  - *From: Kijai*

- **Audio scale vs Audio CFG scale**: Audio scale multiplies conditioning in every case, audio_cfg_scale only works when main CFG is used
  - *From: Kijai*

- **Motion frame**: The overlap setting in multitalk processing, can be adjusted but best to leave at default
  - *From: Kijai*

- **Frame window size**: Similar to context window length, should be set to frame number you generate normally
  - *From: DawnII*

- **Multitalk node vs context windows**: Multitalk node is alternative to context windows for long video gen, not needed for 81 frames and under
  - *From: Kijai*

- **V2V keyframing approach**: Instead of true video-to-video, system takes keyframes every 72 frames and uses uni3c + audio to generate between them
  - *From: DawnII*

- **High/Low noise split**: Wan 2.2 MoE architecture separates high noise and low noise processing, with different LoRA compatibility
  - *From: Kijai*

- **Block swap**: Memory management technique that keeps data in RAM rather than writing to disk
  - *From: Kijai*

- **LoRA rank**: Amount of parameters per layer - higher rank means bigger effect but also higher memory usage
  - *From: Kijai*

- **Motion frame overlap**: Number of frames used from previous generation when it continues - window of 81 with overlap 25 means 81-25=56 new images per loop
  - *From: Kijai*

- **Audio start index**: Index showing where audio processing begins in frame sequence during generation
  - *From: seitanism*

- **NAG**: Negative prompt guidance system that helps when CFG=1 isn't using negative prompts
  - *From: mamad8*

- **Swap blocks**: Feature mainly useful as safeguard against OOM errors, especially at higher resolutions, may only take effect on new prompts
  - *From: . Not Really Human :.*

- **V2V with InfiniteTalk**: Not currently fully implemented, requires input sample length to equal frame_window_size
  - *From: MysteryShack*

- **Temporal mask for Fun**: Black frames are changed, white frames unchanged, opposite of VACE masking
  - *From: DawnII*

- **SceneCut support in InfiniteTalk**: Input video can contain multiple shots, convenient for remaking video with input audio while maintaining camera movement and scene layout
  - *From: NebSH*

- **V2V implementation in InfiniteTalk**: Chops up video every 72 frames and uses uni3c to bridge the gap, not true V2V
  - *From: DawnII*

- **InfiniteTalk first frame noise issue**: InfiniteTalk model cannot handle full noise like it encounters in non-loop sampling, causing noisy first frames. Fixed by encoding init image and injecting it to first latent on every step.
  - *From: Kijai*

- **Context windows in video generation**: Method for processing longer videos by breaking them into overlapping segments, useful with the new InfiniteTalk noise fix
  - *From: Kijai*

- **Motion frames in InfiniteTalk**: Frame window is fixed at 81, motion frames are overlap between windows. Formula: total_frames = (x * 81) - ((x-1) * motion_frames)
  - *From: DawnII*

- **Frame padding**: Video is padded to account for looping windows, causing lingering gibberish at end
  - *From: DawnII*

- **start_step in vid2vid**: First N steps considered already done, input video used instead, noise added based on what noise should be on those steps
  - *From: Kijai*

- **motion_frames**: Context window overlap, every batch of 81 frames uses 9 frames from last clip as first clip for smooth transition
  - *From: seitanism*

- **InfiniteTalk context windows**: Each window is 81 frames with overlap, sampling shows audio indices for each window
  - *From: Kijai*

- **Differential diffusion**: Mixes the init with the noise per step using mask as thresholds, so mask can be blurred and blends better than normal latent masking
  - *From: Kijai*

- **Temporal inpainting**: Inpainting that works on first to last frame and in-between frames, not spatial inpainting like VACE
  - *From: Kijai*

- **I2V chaining in loops**: Multiple samplers where each uses previous sampler's result as I2V input, requires finished denoised output
  - *From: Kijai*

- **NAG (Negative Attention Guidance)**: Applied to positive conditioning, not negative. With cfg 1.0, normal negative isn't used
  - *From: Kijai*

- **Mixed precision models**: 99% fp16 weights with fp32 bias, adds minimal size (~6mb) with barely noticeable quality difference
  - *From: Kijai*

- **MultiTalk masking**: Limits where each audio can affect result, not precise mouth targeting but broader area control
  - *From: Kijai*

- **Fun InP model**: Model for first-last frame temporal inpainting, confusing naming
  - *From: Blink*

- **Extra latent technique**: Adding latent to I2V changes the noise pattern, not intended way but can improve certain prompting scenarios
  - *From: Kijai*

- **Differential diffusion**: Code technique for inpainting that was incorrectly placed, now fixed for better masking results
  - *From: Kijai*

- **Differential diffusion**: Uses grayscale masks for blending, works poorly with low steps due to limited adjustment room
  - *From: Kijai*

- **RoPE frequency scaling**: Spatial base frequency scaling for resolution changes while temporal frequency stays at 1.0
  - *From: Kijai*

- **Context windows with prompt changes**: Prompts separated by | are spread evenly across context windows, last prompt used for remaining frames
  - *From: Kijai*

- **RoPE scaling**: A technique that can improve results even without cinescale, applied to both samplers in upscaling workflow
  - *From: Kijai*

- **Flowmatch_distill**: A sampler that's only really necessary for 4 steps, gets errors if you try more steps
  - *From: Kijai*

- **Set Lora node**: Sets loras after loading model so you don't have to reload the model, uses more VRAM but allows dynamic lora application
  - *From: Kijai*

- **MAGREF**: A model with I2V structure trained differently that allows context windows and character consistency
  - *From: Kijai*

- **Context windows with I2V models**: I2V models being start image models by nature makes them incompatible with context windows concept
  - *From: Kijai*

- **CUDA out of memory vs Allocation on device**: CUDA out of memory = RAM error, Allocation on device = VRAM error
  - *From: Kijai*

- **InfiniteTalk vs MultiTalk**: InfiniteTalk doesn't degrade when continuing from last frame, allows endless generation without context window drawbacks
  - *From: Kijai*

- **Block swap settings**: non_blocking increases RAM use but speeds transfers; prefetch_blocks moves blocks asynchronously from RAM to VRAM; block_swap_debug reports transfer times
  - *From: Kijai*

- **Torch compile caching**: Compile is cached per input - same resolution and frame count shouldn't re-compile
  - *From: Kijai*

- **CFG interpolation**: Start and end CFG being same disables interpolation, range outside start/end percent is put to 1.0
  - *From: Kijai*

- **first_sampler variable**: Used as an 'end_sampling_before_final_timestep' check, badly named leftover variable that skips slicing of timesteps
  - *From: Kijai*

- **latent insertion trick**: Adding input image as extra latent to avoid start being noise
  - *From: Kijai*

- **Loop sampling window overlap**: When using loop sampling with window size 81 and motion_frames 9, it creates overlap requiring more total frames than just the window size
  - *From: Kijai*

- **InfiniteTalk latent training**: InfiniteTalk is trained to expect the image in the latents, which is why first latent in normal I2V workflow is just noise
  - *From: Kijai*

- **Block swapping memory calculation**: Divide model size by 40 on 14B models, by 30 on 1.3B and 5B models to get per-block memory usage
  - *From: Kijai*

- **MoE High/Low noise expert split**: Wan 2.2 uses different experts for high and low noise, can hook different inputs to each
  - *From: Draken*

- **SNR threshold splitting**: New node splits steps based on sigma threshold (0.875) instead of manually selected step count
  - *From: Kijai*

- **Block swap memory management**: Balances memory use between VRAM and RAM using blocks_to_swap parameter to run larger models
  - *From: Kijai*

- **VACE keyframe interpolation**: Basic VACE feature that allows smooth transitions between keyframes, often overlooked
  - *From: Kijai*

- **Dense pose controlnet**: More detailed pose control compared to regular openpose, available in cloth adapter repos
  - *From: Kijai*

- **Fakevace**: Alternative VACE implementation that can work with extend nodes and InfiniteTalk
  - *From: JalenBrunson*

- **Frame window size in InfiniteTalk**: Size of a single generation when splitting process to multiple generations, with motion_frame as overlap between windows
  - *From: Kijai*

- **Fun InP vs Fun-Control channel requirements**: Fun InP = 36 channels like normal I2V, Fun-Control 2.2 = 52 channels (16+16+16+4)
  - *From: Kijai*

- **InfiniteTalk first latent expectation**: InfiniteTalk model is trained to expect the first latent to be an image, that's why it works for continuous I2V generation
  - *From: Kijai*

- **Crop&stitch**: Powerful technique for handling overlays and masked regions
  - *From: Valle*

- **Stand-in rope**: Feature implemented for ComfyUI compatibility, comfy version is better than original
  - *From: Kijai*

- **Frame pack method**: Sampling method used in new Wan S2V model with causal self attention
  - *From: Kijai*

- **Non-blocking in block swap**: Reserves more RAM but is faster, uses more CPU RAM for speed
  - *From: xwsswww*

- **Tea Cache compatibility**: Doesn't work with LoRA accelerators, causes pixelation issues
  - *From: .: Not Really Human :.*

- **Framepack**: Technology that allows video extension and potentially infinite generation, used in S2V model
  - *From: Kijai*

- **Context window size**: Frame window size that affects inference speed - larger windows make generation slower
  - *From: Mancho*

- **Beta sigma conversion**: A scheduling technique that can be applied in samplers, shouldn't be used twice
  - *From: Kijai*

- **Reference latent**: Used in S2V model exactly like Phantom model for consistency
  - *From: Kijai*

- **CFG Schedule**: Method to vary CFG values across sampling steps for better results
  - *From: Mu5hr00m_oO*

- **CFG Skimming**: CFG interpolation technique, same as advanced CFG interpolation
  - *From: DawnII*

- **Framepack extension technique**: Technique used for longer video generation beyond 5 seconds
  - *From: ArtOfficial*

- **Framepack**: Architecture used by WAN S2V for video generation, allows consistent VRAM usage regardless of frame count
  - *From: Kijai*

- **Context overlap**: Higher overlap means more model passes needed and slower generation, but better blending between windows
  - *From: Kijai*

- **Context windows**: Method for generating longer videos by processing in segments
  - *From: Kijai*

- **Block swap**: Manual VRAM management technique in WanWrapper for memory optimization
  - *From: Kijai*

- **Uni3C**: Component that provides camera control functionality
  - *From: T2 (RTX6000Pro)*

- **Framepack**: A technique that initializes motion in input latents to allow infinite generation, used by S2V model. Different from direct guidance, more like projection
  - *From: Kijai, MilesCorban*

- **Context windows vs Framepack**: Context windows use overlapping frames for continuity, while framepack uses motion initialization for infinite generation
  - *From: Kijai*

- **Merged vs Unmerged LoRAs**: Native always merges LoRAs, while wrapper can use them unmerged. GGUF is always unmerged. Behavior differs significantly between modes
  - *From: Kijai, Draken*

- **PUSA**: Serves as a way to expand t2v model capabilities for frame extension, I2V, extended generation. Helps maintain likeness across context windows due to how it attends images
  - *From: DawnII*

- **Framepack implementation**: One of three motioner methods in S2V, doesn't have context window burning issues but reduces lipsync quality due to overlap
  - *From: Kijai*

- **Pose condition layer**: Layer in S2V model that shouldn't be quantized to fp8 for proper functionality
  - *From: Kijai*

- **mmproj**: The visual component of VLM (Vision Language Models), not a text encoder
  - *From: DawnII*

- **Framepack**: Context sliding technique used by S2V model with its own weights, allows for extended video generation
  - *From: Kijai*

- **MAGREF**: I2V model trained to use the image more as a reference than as a start image, so it has lot more freedom to work with
  - *From: Kijai*

- **Framepack continuation method**: Method for video generation where bucket function determines frame handling - different from context windows approach
  - *From: Kijai*

- **MAGREF**: A full Wan I2V model that works like Phantom, using image as reference rather than direct I2V conversion
  - *From: blake37*

- **Framepack**: Technology from S2V that enables longer generation but quality degrades over time, requires careful balance of settings
  - *From: Kijai*

- **Context windows**: Method for generating longer videos by passing previous frames as context, better quality than Framepack but worse lipsync
  - *From: Kijai*

- **Beta scheduler differences**: ComfyUI and diffusers handle beta scheduling differently - diffusers applies shift first then beta, ComfyUI may do opposite
  - *From: Kijai*

- **Context windows vs extension**: Context windows do single generation in windows with no quality degradation, unlike extension methods
  - *From: Kijai*

- **Alpha channel handling**: Alpha isn't special to models, just extra channel with information. VAE strips alpha away
  - *From: Kijai*

- **CFG with empty conditioning**: Empty conditioning still runs model as if without prompt, then subtracts that result
  - *From: Ablejones*

- **Context window stride artifacts**: High noise output shows stride artifacts that get cleaned up in low noise pass
  - *From: Kijai*

- **MAGREF vs regular I2V for context**: MAGREF works with context windows while regular I2V works poorly due to training to reference first frame
  - *From: daking999*

- **Prompt travel**: Different prompts can be used for different segments of context windows, each covering ~81 frames
  - *From: Kijai*

- **InfiniteTalk looping**: The infinite talk node simply continues from last frame in a loop, expects the image encoded as first latent
  - *From: Kijai*

- **Context window stitching**: Different context prompts with new scenes, infinitetalk looping is better for this
  - *From: DawnII*

- **VACE embed technique**: Connect between frames setup to a VACE embed for advanced control
  - *From: Nekodificador*

- **VACE first frame edit**: VACE can take a video and a new first frame and edit the video using that new first frame as reference
  - *From: Juampab12*


## Resources & Links

- **Rapid Wan 2.2 All-in-One model** (model)
  - https://civitai.com/models/1824594/rapid-wan-22-all-in-one?modelVersionId=2064884
  - *From: hicho*

- **Wan2.2 ControlNet implementation** (repo)
  - https://github.com/TheDenk/wan2.2-controlnet
  - *From: A.I.Warper*

- **WAN 2.2 14B (GGUF) V2V workflow** (workflow)
  - https://huggingface.co/thaakeno46/ComfyUI-Workflows/blob/main/WAN%202.2%2014B%20(GGUF)%20V2V.json
  - *From: thaakeno*

- **Wan 2.1 LoRA trainer** (tool)
  - https://comfy.icu/extension/jaimitoes__ComfyUI_Wan2_1_lora_trainer
  - *From: Ryzen*

- **WSL2 ComfyUI setup guide** (tutorial)
  - https://www.youtube.com/watch?v=ZBgfRlzZ7cw
  - *From: seitanism*

- **Triton and SageAttention installer** (tool)
  - https://civitai.com/articles/12851/easy-installation-triton-and-sageattention
  - *From: Ruairi Robinson*

- **WAN 2.2 VACE test version** (model)
  - https://huggingface.co/lym00/Wan2.2_T2V_A14B_VACE-test/tree/main
  - *From: avataraim*

- **RadialAttention ComfyUI implementation** (repo)
  - https://github.com/woct0rdho/ComfyUI-RadialAttn
  - *From: Lumi*

- **Block Sparse SageAttention 2.0** (repo)
  - https://github.com/Radioheading/Block-Sparse-SageAttention-2.0
  - *From: Kijai*

- **SpargeAttn wheels** (repo)
  - https://github.com/woct0rdho/SpargeAttn/releases
  - *From: Kijai*

- **SageAttention3 early access** (model)
  - https://huggingface.co/jt-zhang/SageAttention3
  - *From: Kijai*

- **LightX2V LoRA comparison** (resource)
  - https://www.reddit.com/r/comfyui/comments/1meszym/21_lightx2v_lora_will_make_wan22_more_like_wan21/
  - *From: toyxyz*

- **Triton Windows build** (repo)
  - https://github.com/woct0rdho/triton-windows
  - *From: Kijai*

- **NSFW LoRA for WAN 2.2** (lora)
  - civitai.com/models/1476909
  - *From: crinklypaper*

- **WAN 2.2 ControlNet Depth v1** (model)
  - https://huggingface.co/TheDenk/wan2.2-ti2v-5b-controlnet-depth-v1
  - *From: orabazes*

- **Prompt generator tool** (tool)
  - https://dengeai.com/prompt-generator
  - *From: avataraim*

- **Official Alibaba source materials** (documentation)
  - *From: The Shadow (NYC)*

- **WAN camera prompting guide** (documentation)
  - https://alidocs.dingtalk.com/i/nodes/EpGBa2Lm8aZxe5myC99MelA2WgN7R35y
  - *From: crinklypaper*

- **HSD LoRA for high speed dynamic movement** (lora)
  - https://civitai.com/models/1698719/high-speed-dynamic
  - *From: Jonathan*

- **LLM prompt generation system guide** (workflow)
  - https://pastebin.com/raw/nFjbM7mJ
  - *From: Simjedi*

- **Ollama workflow for prompt generation** (workflow)
  - workflow shared in chat
  - *From: Simjedi*

- **Mobius looping/long video strategy** (repo)
  - https://github.com/YisuiTT/Mobius
  - *From: daking999*

- **Wan 2.2 official code repository** (repo)
  - https://github.com/Wan-Video/Wan2.2/tree/main/wan/configs
  - *From: aikitoria*

- **H1111 implementation for full quality** (repo)
  - https://github.com/maybleMyers/H1111/tree/wan2.2b
  - *From: Benjimon*

- **I2V workflow for 14B** (workflow)
  - *From: VRGameDevGirl84(RTX 5090)*

- **T2V workflow with auto-calculation** (workflow)
  - *From: VRGameDevGirl84(RTX 5090)*

- **Wan 2.2 Prompt Creator ChatGPT** (tool)
  - https://chatgpt.com/g/g-688805b301ec81918e3a5a45dbb8405b-wan2-2-prompt-creator
  - *From: ✧ฅโ๑ↀᆺↀ ๑ใฅ✧PookieNumnums*

- **VACE Test model for Wan 2.2** (model)
  - https://huggingface.co/lym00/Wan2.2_T2V_A14B_VACE-test/tree/main
  - *From: BondoMan*

- **Sage Attention installation guide** (tutorial)
  - https://www.youtube.com/watch?v=CgLL5aoEX-s
  - *From: xwsswww*

- **Wan 2.2 system prompt** (code)
  - https://github.com/Wan-Video/Wan2.2/blob/main/wan/utils/system_prompt.py
  - *From: Kijai*

- **MMaudio ComfyUI nodes** (tool)
  - *From: nacho.money*

- **Wan 2.2 i2v crush LoRA** (lora)
  - https://huggingface.co/ostris/wan22_5b_i2v_crush_it_lora
  - *From: thaakeno*

- **EchoShot model** (model)
  - https://huggingface.co/JonneyWang/EchoShot
  - *From: Juampab12*

- **MOSS-TTSD** (repo)
  - https://github.com/OpenMOSS/MOSS-TTSD
  - *From: EKvan*

- **Prompt generator tool** (tool)
  - https://prompt.dengeai.com/prompt-generator
  - *From: The Shadow (NYC)*

- **Wan 2.2 ComfyUI Repackaged** (model)
  - https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/tree/main/split_files/text_encoders
  - *From: Kijai*

- **Wan prompting guide** (guide)
  - https://alidocs.dingtalk.com/i/nodes/EpGBa2Lm8aZxe5myC99MelA2WgN7R35y
  - *From: Ada*

- **Wan 2.2 prompter with video input** (tool)
  - https://prompter.on.websim.com/
  - *From: thaakeno*

- **ComfyUI Wan 2.2 FLF2V blog post** (guide)
  - https://blog.comfy.org/p/wan22-flf2v-comfyui-native-support
  - *From: BarleyFarmer*

- **CondensedMovies dataset** (dataset)
  - https://github.com/m-bain/CondensedMovies
  - *From: mamad8*

- **RES4LYF custom node** (node)
  - https://github.com/ClownsharkBatwing/RES4LYF
  - *From: mamad8*

- **Wan2.2_T2V_A14B_VACE-test** (model)
  - https://huggingface.co/lym00/Wan2.2_T2V_A14B_VACE-test/tree/main
  - *From: Ashtar*

- **SageAttention installation scripts** (scripts)
  - https://huggingface.co/lym00/scripts/tree/main
  - *From: hicho*

- **UMT5 encoders** (model)
  - https://huggingface.co/city96/umt5-xxl-encoder-gguf/tree/main
  - *From: xwsswww*

- **Reddit discussion on Wan 2.2 settings** (guide)
  - https://www.reddit.com/r/StableDiffusion/comments/1mfzvl5/debate_best_wan_22_t2v_settings_steps_sampler_cfg/?share_id=Z4koU6SN5YPpZUm7SgVRk&utm_content=1&utm_medium=ios_app&utm_name=ioscss&utm_source=share&utm_term=10
  - *From: The Shadow (NYC)*

- **MMAudio + Wan 2.2 workflow** (workflow)
  - https://huggingface.co/thaakeno46/ComfyUI-Workflows/blob/main/Wan2.2-MMAudio_GGUF_T2V.json
  - *From: thaakeno*

- **FastVideo GitHub commit** (repo)
  - https://github.com/hao-ai-lab/FastVideo/commit/5f42748ed11bd1be9929d7b3de42691f6eac553a
  - *From: Screeb*

- **DFloat11 compressed Wan2.2** (model)
  - https://huggingface.co/DFloat11/Wan2.2-T2V-A14B-2-DF11
  - *From: hicho*

- **Phr00t Rapid AllInOne v2** (model)
  - https://huggingface.co/Phr00t/WAN2.2-14B-Rapid-AllInOne/tree/main/v2
  - *From: hicho*

- **Mixed precision weights** (model)
  - https://huggingface.co/maybleMyers/wan_files_for_h1111/tree/main
  - *From: Benjimon*

- **Official Wan 2.2 code** (repo)
  - https://github.com/Wan-Video/Wan2.2
  - *From: aikitoria*

- **FusionX ingredients and workflows** (workflow)
  - https://civitai.com/models/1736052/fusionxlightning-ingredientsworkflows
  - *From: Kenk*

- **FPS1 experimental LoRAs** (lora)
  - Wan22_I2V_FPS1_lownoise_s13000.safetensors: https://pixeldrain.com/u/eXypSibw, Wan22_I2V_FPS1_highnoise_s9000.safetensors: https://pixeldrain.com/u/ei2FRBkU
  - *From: mamad8*

- **Wan official prompt guide** (documentation)
  - https://alidocs.dingtalk.com/i/nodes/EpGBa2Lm8aZxe5myC99MelA2WgN7R35y
  - *From: crinklypaper*

- **ClownShark samplers** (sampler)
  - https://github.com/ClownsharkBatwing/RES4LYF/tree/main
  - *From: The Shadow (NYC)*

- **LightX2V I2V 14B distill LoRA** (lora)
  - https://huggingface.co/Kijai/WanVideo_comfy/blob/main/Lightx2v/lightx2v_I2V_14B_480p_cfg_step_distill_rank64_bf16.safetensors
  - *From: Ablejones*

- **Quantile adaptive T2V LoRA** (lora)
  - https://huggingface.co/Kijai/WanVideo_comfy/blob/main/Lightx2v/lightx2v_14B_T2V_cfg_step_distill_lora_adaptive_rank_quantile_0.15_bf16.safetensors
  - *From: The Shadow (NYC)*

- **bf16 I2V models** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/blob/main/Wan2_2-I2V-A14B-HIGH_bf16.safetensors
  - *From: Kijai*

- **bf16 I2V Low model** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/blob/main/Wan2_2-I2V-A14B-LOW_bf16.safetensors
  - *From: Kijai*

- **Self-Forcing Plus repo** (repo)
  - https://github.com/GoatWu/Self-Forcing-Plus
  - *From: Kijai*

- **h1111 gradio app** (tool)
  - https://github.com/maybleMyers/h1111
  - *From: Alisson Pereira*

- **A1111 WebUI** (tool)
  - https://github.com/AUTOMATIC1111/stable-diffusion-webui
  - *From: Rainsmellsnice*

- **Modal Labs examples repository** (repo)
  - https://github.com/modal-labs/modal-examples
  - *From: Karo*

- **Runpod ComfyUI worker template** (repo)
  - https://github.com/runpod-workers/worker-comfyui
  - *From: gokuvonlange*

- **Wan 2.2 config showing shift 12 for T2V** (repo)
  - https://github.com/Wan-Video/Wan2.2/blob/main/wan/configs/wan_t2v_A14B.py#L34
  - *From: aikitoria*

- **Video about noise scheduling** (educational)
  - https://www.youtube.com/watch?v=egn5dKPdlCk
  - *From: Ablejones*

- **First-Last-Frame ComfyUI node** (repo)
  - https://github.com/stduhpf/ComfyUI--Wan22FirstLastFrameToVideoLatent
  - *From: hicho*

- **Aether Crash Telephoto LoRA** (lora)
  - https://www.reddit.com/r/StableDiffusion/comments/1mf1wqp/lora_release_aether_crash_telephoto_crashzoom/
  - *From: NebSH*

- **T2I Civitai workflow** (workflow)
  - https://civitai.com/models/1834338?modelVersionId=2079614
  - *From: Juampab12*

- **Fixed Wan 2.2 Lightning LoRAs** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/tree/main/Wan22-Lightning
  - *From: Kijai*

- **Triton for Windows** (tool)
  - https://github.com/woct0rdho/triton-windows
  - *From: Kijai*

- **SageAttention for Windows** (tool)
  - https://github.com/woct0rdho/SageAttention
  - *From: Kijai*

- **Wan 2.2 Lightning Official Repo** (repo)
  - https://huggingface.co/lightx2v/Wan2.2-Lightning
  - *From: yi*

- **720P Distilled I2V Model** (model)
  - https://huggingface.co/lightx2v/Wan2.1-I2V-14B-720P-StepDistill-CfgDistill-Lightx2v/commits/main
  - *From: DawnII*

- **Kijai's Wan 2.2 Lightning LoRAs** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/tree/main/Wan22-Lightning
  - *From: Juampab12*

- **Lightx2v I2V 720P (fake)** (model)
  - https://huggingface.co/lightx2v/Wan2.1-I2V-14B-720P-StepDistill-CfgDistill-Lightx2v
  - *From: Doctor Shotgun*

- **Wan 2.2 Lightning LoRAs** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/tree/main/Wan22-Lightning
  - *From: Ant*

- **FastWan2.2-TI2V-5B-FullAttn-Diffusers** (model)
  - https://huggingface.co/FastVideo/FastWan2.2-TI2V-5B-FullAttn-Diffusers
  - *From: yi*

- **LightX2V Lightning repo** (repo)
  - https://huggingface.co/lightx2v/Wan2.2-Lightning
  - *From: Luis Clement*

- **Wan2.2 Lightning GitHub** (repo)
  - https://github.com/ModelTC/Wan2.2-Lightning/tree/fxy/distill
  - *From: Kijai*

- **Wan 2.2 Lightning LoRAs** (repo)
  - https://github.com/ModelTC/Wan2.2-Lightning
  - *From: hicho*

- **Lightning LoRA models** (model)
  - https://huggingface.co/lightx2v/Wan2.2-Lightning/tree/main/Wan2.2-T2V-A14B-4steps-lora-rank64-V1
  - *From: ˗ˏˋ⚡ˎˊ-*

- **FastWan 5B converted model** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/blob/main/FastWan/Wan2_2-TI2V-5B-FastWanFullAttn_bf16.safetensors
  - *From: Kijai*

- **Claude custom project for prompting** (tool)
  - *From: Juampab12*

- **Wan prompting guide** (tool)
  - https://prompter.on.websim.com
  - *From: gokuvonlange*

- **Alibaba image guide** (documentation)
  - https://alidocs.dingtalk.com/i/nodes/amweZ92PV6DbOdgzUZZe0YxN8xEKBD6p
  - *From: hicho*

- **ClownsharkSampler workflow** (workflow)
  - shared as PNG
  - *From: Ablejones*

- **Kijai's Lightning loras** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/tree/main/Wan22-Lightning
  - *From: Kijai*

- **MMAudio space** (tool)
  - https://huggingface.co/spaces/hkchengrex/MMAudio
  - *From: : Not Really Human :*

- **FastVideo FastWan models** (model)
  - https://huggingface.co/FastVideo/FastWan2.2-TI2V-5B-FullAttn-Diffusers
  - *From: s2k*

- **PSNbst Accelerator lora** (lora)
  - https://huggingface.co/PSNbst/Wan22-Accelerator-PAseer
  - *From: piscesbody*

- **Qwen Image VAE** (model)
  - https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI/resolve/main/split_files/vae/qwen_image_vae.safetensors
  - *From: Draken*

- **Wan 2.2 GGUF Upscaler 14B workflow** (workflow)
  - https://huggingface.co/thaakeno46/ComfyUI-Workflows/blob/main/WAN2.2_GGUF_UPSCALER_14B.json
  - *From: thaakeno*

- **Wan 2.2 GGUF V2V workflow** (workflow)
  - https://huggingface.co/thaakeno46/ComfyUI-Workflows/blob/main/Wan2.2_GGUF_V2V.json
  - *From: thaakeno*

- **Wan 2.2 GGUF FLF workflow** (workflow)
  - https://huggingface.co/thaakeno46/ComfyUI-Workflows/blob/main/WAN2.2_GGUF_FFLF.json
  - *From: thaakeno*

- **Wan22-Accelerator-PAseer** (model)
  - https://huggingface.co/PSNbst/Wan22-Accelerator-PAseer/tree/main
  - *From: N0NSens*

- **Qwen3 prompt enhancement node** (node)
  - *From: shockgun*

- **ComfyUI-AutomaticCFG** (tool)
  - https://github.com/Extraltodeus/ComfyUI-AutomaticCFG
  - *From: PizzaSlice*

- **WanVideo_comfy_fp8_scaled** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy_fp8_scaled
  - *From: Kijai*

- **Video prompter tool** (tool)
  - https://prompter.on.websim.com/
  - *From: thaakeno*

- **TheDenk 5B ControlNets** (model)
  - https://huggingface.co/TheDenk
  - *From: DawnII*

- **Pixelle-MCP ComfyUI server** (tool)
  - https://github.com/AIDC-AI/Pixelle-MCP
  - *From: AJO*

- **WAN 2.2 high noise 14B fp8_scaled model** (model)
  - https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/tree/main/split_files/diffusion_models
  - *From: hiroP*

- **Kijai's fp8_scaled model collection** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy_fp8_scaled
  - *From: Kijai*

- **ComfyUI file formatting documentation** (documentation)
  - https://comfyuidoc.com/Interface/SaveFileFormatting.html
  - *From: Kijai*

- **Caching node pack for text encoders** (tool)
  - https://github.com/alastor-666-1933/caching_to_not_waste
  - *From: patientx*

- **VRGameDevGirl84 workflows** (workflow)
  - *From: Gill Bastar*

- **Batch video generation node** (tool)
  - *From: Fill*

- **Wan 2.2 Lightning LoRAs** (lora)
  - https://huggingface.co/Kijai/WanVideo_comfy/tree/main/Wan22-Lightning
  - *From: avataraim*

- **LightX2V LoRAs** (lora)
  - https://huggingface.co/Kijai/WanVideo_comfy/tree/main/Lightx2v
  - *From: GalaxyTimeMachine (RTX4090)*

- **WAN 2.2 14B Arcane Jinx LoRA** (model)
  - https://huggingface.co/Cseti/wan2.2-14B-Arcane_Jinx-lora-v1
  - *From: Cseti*

- **SageAttention repository** (repo)
  - https://github.com/thu-ml/SageAttention
  - *From: Josiah*

- **Vibecoding examples collection** (tool)
  - https://ballad.microapp.me
  - *From: fredbliss*

- **Wan2.2_T2V_A14B_VACE-test checkpoint** (model)
  - https://huggingface.co/lym00/Wan2.2_T2V_A14B_VACE-test
  - *From: Piblarg*

- **Model merging tutorial** (tutorial)
  - https://discord.com/channels/1076117621407223829/1386453178240733235/1402513536068096063
  - *From: Ablejones*

- **YouTube video by NerdyRodent** (tutorial)
  - https://www.youtube.com/watch?v=MkAuWTLJp1s
  - *From: Draken*

- **spacepxl Wan 2.1 control LoRAs** (model)
  - https://huggingface.co/spacepxl/Wan2.1-control-loras
  - *From: ˗ˏˋ⚡ˎˊ-*

- **N0NSens T2I workflow** (workflow)
  - https://discord.com/channels/1076117621407223829/1401393279790088213
  - *From: N0NSens*

- **FakeVace2.2 experimental model** (model)
  - https://huggingface.co/CCP6/FakeVace2.2/tree/main
  - *From: JohnDopamine*

- **Reddit comparison post** (comparison)
  - https://www.reddit.com/r/StableDiffusion/comments/1mhosa2/update_qwenimage_vs_flux_1d_vs_krea_1d_vs_wan_22/
  - *From: Дмитрий Марков*

- **Spline-Path-Control** (repo)
  - https://github.com/WhatDreamsCost/Spline-Path-Control
  - *From: Jonathan*

- **ComfyUI-GIMM-VFI** (repo)
  - https://github.com/kijai/ComfyUI-GIMM-VFI
  - *From: Kijai*

- **ComfyUI-Rife-Tensorrt** (repo)
  - https://github.com/yuvraj108c/ComfyUI-Rife-Tensorrt
  - *From: aipmaster*

- **Wan2.2_T2V_A14B_VACE-test merge** (model)
  - https://huggingface.co/lym00/Wan2.2_T2V_A14B_VACE-test
  - *From: JalenBrunson*

- **ComfyUI-RadialAttn workflow** (workflow)
  - https://github.com/woct0rdho/ComfyUI-RadialAttn
  - *From: : Not Really Human :.*

- **WAN 2.1 Makoto Shinkai style with res_2s_bong_tangent sampler** (model)
  - https://civitai.com/models/1766551/wan21-your-name-makoto-shinkai-style
  - *From: Дмитрий Марков*

- **FakeVace2.2 for Wan 2.2** (model)
  - https://huggingface.co/CCP6/FakeVace2.2/tree/main
  - *From: Lodis*

- **Waver project page** (project)
  - http://www.waver.video/
  - *From: yi*

- **Waver GitHub repository** (repo)
  - https://github.com/FoundationVision/Waver?tab=readme-ov-file
  - *From: yi*

- **Dream LoRA for morphing** (lora)
  - https://civitai.com/models/1811141?modelVersionId=2049587
  - *From: piscesbody*

- **Video arena leaderboard** (benchmark)
  - https://artificialanalysis.ai/text-to-video/arena?tab=leaderboard
  - *From: yi*

- **Wan 2.2 Lightning discussion** (discussion)
  - https://huggingface.co/lightx2v/Wan2.2-Lightning/discussions/14
  - *From: Screeb*

- **New Lightning LoRAs** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/tree/main/Wan22-Lightning
  - *From: Kijai*

- **LoRA rank inspection** (repo)
  - https://huggingface.co/Kijai/WanVideo_comfy/tree/main/Lightx2v
  - *From: Kijai*

- **WanVideo I2I LoRA for similarity** (model)
  - https://civitai.com/models/1421989/wanvideo-i2i-480p-expression-changer-perspective-changer
  - *From: Juampab12*

- **Lightning team discussion** (repo)
  - https://huggingface.co/lightx2v/Wan2.2-Lightning/discussions/13
  - *From: DawnII*

- **Lightning 2.2 LoRAs** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/tree/main/Wan22-Lightning
  - *From: Josiah*

- **ATI Motion Transfer** (tool)
  - https://github.com/bytedance/ATI?tab=readme-ov-file#motion-transfer
  - *From: Kijai*

- **MagCache** (tool)
  - https://github.com/Zehong-Ma/MagCache
  - *From: NebSH*

- **fp8 scaled models comparison** (repo)
  - https://huggingface.co/Kijai/WanVideo_comfy_fp8_scaled
  - *From: Kijai*

- **Wan 2.2 Fun Control** (model)
  - https://huggingface.co/alibaba-pai/Wan2.2-Fun-A14B-Control
  - *From: DawnII*

- **Kijai Lightning LoRAs** (lora)
  - https://huggingface.co/Kijai/WanVideo_comfy/tree/main/Wan22-Lightning
  - *From: : Not Really Human :*

- **LightX2V adaptive rank LoRA** (lora)
  - https://huggingface.co/Kijai/WanVideo_comfy/blob/main/Lightx2v/lightx2v_14B_T2V_cfg_step_distill_lora_adaptive_rank_quantile_0.15_bf16.safetensors
  - *From: MilesCorban*

- **Lightning discussion thread** (discussion)
  - https://huggingface.co/lightx2v/Wan2.2-Lightning/discussions/13
  - *From: CaptHook*

- **Wan2.2-Fun-A14B-Control** (model)
  - https://huggingface.co/alibaba-pai/Wan2.2-Fun-A14B-Control
  - *From: CJ*

- **Wan2.2-Fun-A14B-InP** (model)
  - https://huggingface.co/alibaba-pai/Wan2.2-Fun-A14B-InP
  - *From: Kijai*

- **Kijai's fp8 scaled Fun models** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy_fp8_scaled/tree/main/Fun
  - *From: Kijai*

- **V2V workflows** (workflow)
  - https://huggingface.co/thaakeno46/ComfyUI-Workflows/tree/main
  - *From: SonidosEnArmonía*

- **Native Wan 2.2 14B FLF2V workflow** (workflow)
  - https://docs.comfy.org/tutorials/video/wan/wan2_2#wan2-2-14b-flf2v-workflow-example
  - *From: JohnDopamine*

- **SkyReels A3 demo** (repo)
  - https://github.com/SkyworkAI/skyreels-a3.github.io
  - *From: DawnII*

- **SkyReels paper** (paper)
  - https://arxiv.org/abs/2506.00830
  - *From: yi*

- **Wan Chattable Knowledge Base** (knowledge base)
  - https://notebooklm.google.com/notebook/a08901b9-0511-4926-bbf8-3c86a12dc306
  - *From: Nathan Shipley*

- **Sapiens pose detector CLI** (tool)
  - not provided
  - *From: fredbliss*

- **Automatic CFG paper** (research)
  - https://arxiv.org/abs/2508.03442
  - *From: Kijai*

- **Wan 2.1 Knowledge Base** (knowledge base)
  - https://nathanshipley.notion.site/Wan-2-1-Knowledge-Base-1d691e115364814fa9d4e27694e9468f
  - *From: DawnII*

- **Sapiens ComfyUI node pack** (node pack)
  - https://github.com/smthemex/ComfyUI_Sapiens
  - *From: NebSH*

- **Wan2.2-Lightning LoRA v1.1** (model)
  - https://huggingface.co/lightx2v/Wan2.2-Lightning/tree/main/Wan2.2-T2V-A14B-4steps-lora-rank64-Seko-V1.1
  - *From: hicho*

- **Wan2.2-Fun-A14B-Control** (model)
  - https://huggingface.co/alibaba-pai/Wan2.2-Fun-A14B-Control
  - *From: Dannhauer80*

- **8-step model discussion** (discussion)
  - https://github.com/ModelTC/Wan2.2-Lightning/discussions/4
  - *From: DawnII*

- **DiffSynth Studio FlowMatchScheduler** (repo)
  - https://github.com/modelscope/DiffSynth-Studio/blob/main/diffsynth/schedulers/flow_match.py
  - *From: fredbliss*

- **Scheduler explanation video** (educational)
  - https://m.youtube.com/watch?v=egn5dKPdlCk
  - *From: artemonary*

- **thaakeno ComfyUI Workflows** (workflow)
  - https://huggingface.co/thaakeno46/ComfyUI-Workflows/blob/main/WAN2.2_GGUF_I2V_LIGHTNING.json
  - *From: thaakeno*

- **Kijai Github Sponsor** (support)
  - https://github.com/sponsors/kijai#sponsors
  - *From: 🦙rishappi*

- **Joy Caption Beta** (tool)
  - https://huggingface.co/spaces/fancyfeast/joy-caption-beta-one
  - *From: screwfunk*

- **ComfyUI JoyCaption Node** (node)
  - https://github.com/1038lab/ComfyUI-JoyCaption/tree/main
  - *From: screwfunk*

- **Wan Knowledge Base** (documentation)
  - https://nathanshipley.notion.site/Wan-2-1-Knowledge-Base-1d691e115364814fa9d4e27694e9468f
  - *From: mdkb*

- **FastWan2.2-TI2V-5B model** (model)
  - https://huggingface.co/FastVideo/FastWan2.2-TI2V-5B-FullAttn-Diffusers
  - *From: SonidosEnArmonía*

- **Sapiens CLI implementation** (tool)
  - https://github.com/fblissjr/sapiens_cli
  - *From: fredbliss*

- **Google Vids** (tool)
  - https://workspace.google.com/products/vids/
  - *From: fredbliss*

- **ComfyUI pose interpolation** (node)
  - https://github.com/toyxyz/ComfyUI_pose_inter
  - *From: DawnII*

- **BFloat16 Sapiens model** (model)
  - https://huggingface.co/melmass/sapiens/blob/main/sapiens_1b_goliath_best_goliath_AP_639_bfloat16.pt2
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Sapiens 2B COCO model** (model)
  - https://huggingface.co/noahcao/sapiens-pose-coco/tree/main/sapiens_lite_host/torchscript/pose/checkpoints/sapiens_2b
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Co-tracker** (repo)
  - https://github.com/facebookresearch/co-tracker
  - *From: fredbliss*

- **DOT tracker** (repo)
  - https://github.com/16lemoing/dot
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Sapiens CLI** (tool)
  - https://github.com/fblissjr/sapiens_cli
  - *From: fredbliss*

- **Qwen Image Lightning** (model)
  - https://huggingface.co/lightx2v/Qwen-Image-Lightning/tree/main
  - *From: hicho*

- **WAN resources ChatGPT bot** (tool)
  - https://discord.com/channels/1076117621407223829/1400081347678306304/1400081347678306304
  - *From: Dorksense*

- **PUSA workflow example** (workflow)
  - https://discord.com/channels/1076117621407223829/1386453178240733235/1398123737257083032
  - *From: Hashu*

- **TLBVFI interpolation method** (repo)
  - https://github.com/ZonglinL/TLBVFI?tab=readme-ov-file
  - *From: Kijai*

- **Tiny VAE model for previews** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/blob/main/taew2_1.safetensors
  - *From: Kijai*

- **SeedVR2 setup video** (tutorial)
  - https://youtu.be/I0sl45GMqNg?si=fc0Xci7XNeG-nSQb
  - *From: nacho.money*

- **DLoRAL for frame interpolation** (repo)
  - https://github.com/yjsunnn/DLoRAL?tab=readme-ov-file
  - *From: Kijai*

- **ComfyUI LayerForge for cropping** (tool)
  - https://github.com/Azornes/Comfyui-LayerForge
  - *From: gordo*

- **FFmpeg frame rate changing guide** (documentation)
  - https://trac.ffmpeg.org/wiki/ChangingFrameRate
  - *From: Kijai*

- **Triton Windows installation** (repo)
  - https://github.com/woct0rdho/triton-windows
  - *From: Kijai*

- **SageAttention** (repo)
  - https://github.com/woct0rdho/SageAttention
  - *From: Kijai*

- **Sapiens CLI with multi-person tracking** (repo)
  - https://github.com/fblissjr/sapiens_cli/blob/main/cli/README.md
  - *From: fredbliss*

- **DeepVerse world model** (repo)
  - https://github.com/SOTAMak1r/DeepVerse
  - *From: DawnII*

- **Wan lighting workflow issue** (repo)
  - https://github.com/ModelTC/Wan2.2-Lightning/issues/3
  - *From: flo1331*

- **StreamingLLM paper** (repo)
  - https://github.com/mit-han-lab/streaming-llm
  - *From: fredbliss*

- **ComfyUI-TLBVFI** (repo)
  - https://github.com/BobRandomNumber/ComfyUI-TLBVFI
  - *From: phazei*

- **SeedVR2-7B model** (model)
  - https://huggingface.co/ByteDance-Seed/SeedVR2-7B/tree/main
  - *From: Karo*

- **FastWan 5B model** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/tree/main/FastWan
  - *From: Kijai*

- **Skyreels LoRA for 121 frame fix** (lora)
  - https://huggingface.co/Kijai/WanVideo_comfy/blob/main/Skyreels/Wan2_1_Skyreels-v2-I2V-720P_LoRA_rank_64_fp16.safetensors
  - *From: Kijai*

- **5B controlnet implementation** (repo)
  - https://github.com/TheDenk/wan2.2-controlnet
  - *From: Kijai*

- **Wan 2.2 GGUF V2V workflow** (workflow)
  - https://huggingface.co/thaakeno46/ComfyUI-Workflows/blob/main/Wan2.2_GGUF_V2V.json
  - *From: thaakeno*

- **mdkb's workflows** (workflow)
  - referenced on mdkb's website footprints and current projects pages
  - *From: mdkb*

- **Community knowledge notebook** (tool)
  - https://notebooklm.google.com/notebook/a08901b9-0511-4926-bbf8-3c86a12dc306
  - *From: JohnDopamine*

- **WAN 2.2 system prompt** (code)
  - In qwen subfolder in the wrapper
  - *From: Kijai*

- **Wan2.2-Fun-A14B-InP discussions** (discussion)
  - https://huggingface.co/alibaba-pai/Wan2.2-Fun-A14B-InP/discussions/1#6899d52a63714925142812f3
  - *From: yi*

- **ComfyUI-WanMoeKSampler** (repo)
  - https://github.com/stduhpf/ComfyUI-WanMoeKSampler/
  - *From: Tomber*

- **Rapid AllInOne 2.2** (model)
  - https://huggingface.co/Phr00t/WAN2.2-14B-Rapid-AllInOne
  - *From: Drommer-Kille*

- **Skyreels LoRA** (lora)
  - https://huggingface.co/Kijai/WanVideo_comfy/blob/main/Skyreels/Wan2_1_Skyreels-v2-I2V-720P_LoRA_rank_adaptive_quantile_0.20_fp16.safetensors
  - *From: Kijai*

- **Wan2_1_Skyreels-v2-T2V-720P_LoRA** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/blob/main/Skyreels/Wan2_1_Skyreels-v2-T2V-720P_LoRA_rank_64_fp16.safetensors
  - *From: Kijai*

- **Stand-In identity control** (model)
  - https://huggingface.co/BowenXue/Stand-In
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Matrix Game 2.0** (model)
  - https://huggingface.co/Skywork/Matrix-Game-2.0
  - *From: JohnDopamine*

- **Fantasy Portrait** (repo)
  - https://github.com/Fantasy-AMAP/fantasy-portrait
  - *From: Kijai*

- **Radial Attention workflow** (workflow)
  - https://github.com/woct0rdho/ComfyUI-RadialAttn/blob/main/example_workflows/radial_attn.json
  - *From: : Not Really Human :*

- **Stand-In LoRA** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/tree/main/Stand-In
  - *From: Kijai*

- **StableAvatar** (model)
  - https://huggingface.co/FrancisRing/StableAvatar
  - *From: DawnII*

- **Fantasy Portrait weights** (model)
  - https://huggingface.co/acvlab/FantasyPortrait/tree/main
  - *From: NebSH*

- **SeedVR2 ComfyUI nodes** (repo)
  - https://github.com/numz/ComfyUI-SeedVR2_VideoUpscaler
  - *From: 🦙rishappi*

- **SeedVR2 GGUF models** (model)
  - https://huggingface.co/cmeka/SeedVR2-GGUF/tree/main
  - *From: AmirKerr*

- **Wan2.2 T2V GGUF models** (model)
  - https://huggingface.co/QuantStack/Wan2.2-T2V-A14B-GGUF/tree/main
  - *From: Josiah*

- **NotebookLM model tracker** (tool)
  - https://notebooklm.google.com/notebook/a08901b9-0511-4926-bbf8-3c86a12dc306
  - *From: DawnII*

- **Vibe-coded kernel blog** (resource)
  - https://benanderson.work/blog/vibe-coded-kernel/
  - *From: 642326806678077441*

- **Wan 2.2 5B model** (model)
  - https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/blob/main/split_files/diffusion_models/wan2.2_ti2v_5B_fp16.safetensors
  - *From: Kijai*

- **Wan 2.2 VAE** (model)
  - https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/blob/main/split_files/vae/wan2.2_vae.safetensors
  - *From: humangirltotally*

- **FantasyPortrait for face driving** (model)
  - https://huggingface.co/acvlab/FantasyPortrait/tree/main
  - *From: DeeX*

- **Higgs Audio Voice Clone WebUI** (tool)
  - https://github.com/Saganaki22/higgs-audio-WebUI
  - *From: drbaph*

- **All-in-one Wan 2.2 workflow for AMD GPUs** (workflow)
  - comfyui-zluda fork github
  - *From: patientx*

- **Skyreels v2 LoRA** (lora)
  - https://huggingface.co/Kijai/WanVideo_comfy/blob/main/Skyreels/Wan2_1_Skyreels-v2-T2V-720P_LoRA_rank_64_fp16.safetensors
  - *From: NebSH*

- **Wan 2.1 Knowledge Base** (knowledge base)
  - https://nathanshipley.notion.site/Wan-2-1-Knowledge-Base-1d691e115364814fa9d4e27694e9468f
  - *From: DeepSeaCatz*

- **ComfyUI Wan 2.2 First Last Frame node** (custom node)
  - https://github.com/stduhpf/ComfyUI--Wan22FirstLastFrameToVideoLatent
  - *From: QANICS🕐*

- **Stand-In reference example workflow** (workflow)
  - https://github.com/kijai/ComfyUI-WanVideoWrapper/blob/main/example_workflows/wanvideo_Stand-In_reference_example_01.json
  - *From: ˗ˏˋ⚡ˎˊ-*

- **NotebookLM Discord Knowledge Base** (knowledge base)
  - https://notebooklm.google.com/notebook/a08901b9-0511-4926-bbf8-3c86a12dc306?pli=1
  - *From: JohnDopamine*

- **LightX2V LoRAs for Wan 2.1** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/tree/main/Lightx2v
  - *From: Danial*

- **Fun 2.2 GGUF quantizations** (model)
  - https://huggingface.co/QuantStack/Wan2.2-Fun-A14B-InP-GGUF
  - *From: DawnII*

- **EchoMimic ComfyUI node** (repo)
  - https://github.com/smthemex/ComfyUI_EchoMimic
  - *From: hicho*

- **ComfyUI GGUF quantization tools** (tool)
  - https://github.com/city96/ComfyUI-GGUF/tree/main/tools
  - *From: Ablejones*

- **Fun 2.2 Camera Control models** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy_fp8_scaled/blob/main/Fun/
  - *From: Kijai*

- **Stand-In Preprocessor** (repo)
  - https://github.com/WeChatCV/Stand-In_Preprocessor_ComfyUI
  - *From: orabazes*

- **NotebookLM with latest Wan info** (resource)
  - https://notebooklm.google.com/notebook/a08901b9-0511-4926-bbf8-3c86a12dc306
  - *From: Nathan Shipley*

- **MultiTalk workflow** (workflow)
  - https://github.com/kijai/ComfyUI-WanVideoWrapper/blob/main/example_workflows/wanvideo_multitalk_test_02.json
  - *From: ˗ˏˋ⚡ˎˊ-*

- **FantasyPortrait branch and models** (model)
  - https://github.com/kijai/ComfyUI-WanVideoWrapper/tree/fantasy_portrait and https://huggingface.co/Kijai/WanVideo_comfy/tree/main/FantasyPortrait
  - *From: Kijai*

- **ComfyUI blog post on Wan2.2 Fun InP support** (documentation)
  - https://blog.comfy.org/p/comfyui-wan22-fun-inp-support
  - *From: xwsswww*

- **mxToolkit with Slider2D node** (tool)
  - https://github.com/Smirnov75/ComfyUI-mxToolkit
  - *From: phazei*

- **LayerStyle node pack for masking** (tool)
  - https://github.com/chflame163/ComfyUI_LayerStyle
  - *From: corza*

- **Stand-In preprocessor ComfyUI** (tool)
  - https://github.com/WeChatCV/Stand-In_Preprocessor_ComfyUI
  - *From: mdkb*

- **Goldenboy retro anime style LoRA for Wan 14B 2.2** (lora)
  - https://civitai.com/models/1671285?modelVersionId=2112013
  - *From: crinklypaper*

- **Kijai's fp8 scaled models repository** (models)
  - https://huggingface.co/Kijai/WanVideo_comfy_fp8_scaled
  - *From: Kijai*

- **Kijai's main WanVideo repository** (models)
  - https://huggingface.co/Kijai/WanVideo_comfy
  - *From: screwfunk*

- **Comfy-Org repackaged models** (models)
  - https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/tree/main/split_files/diffusion_models
  - *From: Kijai*

- **MAGREF model** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/blob/main/Wan2_1-Wan-I2V-MAGREF-14B_fp8_e4m3fn.safetensors
  - *From: Kijai*

- **Stand-in reference example workflow** (workflow)
  - https://github.com/kijai/ComfyUI-WanVideoWrapper/blob/main/example_workflows/wanvideo_Stand-In_reference_example_01.json
  - *From: pewpewpew*

- **Wan2.2-Fun-A14B-Control-Camera** (model)
  - https://huggingface.co/alibaba-pai/Wan2.2-Fun-A14B-Control-Camera
  - *From: Lodis*

- **Stand-In LoRA** (model)
  - https://huggingface.co/BowenXue/Stand-In
  - *From: ArtOfficial*

- **GGUF Camera Control** (model)
  - https://huggingface.co/QuantStack/Wan2.2-Fun-A14B-Control-Camera-GGUF/tree/main
  - *From: Daflon*

- **VSA paper** (research)
  - https://arxiv.org/pdf/2525.13389
  - *From: Kijai*

- **Cat singing workflow** (workflow)
  - https://discord.com/channels/1076117621407223829/1403263501421776977/1405598984600551575
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Photopea** (tool)
  - *From: ˗ˏˋ⚡ˎˊ-*

- **New denoise algorithm paper** (research)
  - https://arxiv.org/pdf/2504.17033
  - *From: shockgun*

- **PD-FGC inference repository** (repo)
  - https://github.com/Dorniwang/PD-FGC-inference
  - *From: Kijai*

- **Fantasy Portrait repository** (repo)
  - https://github.com/Fantasy-AMAP/fantasy-portrait
  - *From: Kijai*

- **ONNX Runtime nightly install** (installation)
  - https://onnxruntime.ai/docs/install/#install-nightly-2
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Google MediaPipe face landmarks** (tool)
  - https://ai.google.dev/edge/mediapipe/solutions/vision/face_landmarker
  - *From: mdkb*

- **umt5-xxl-enc-bf16.safetensors** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/blob/main/umt5-xxl-enc-bf16.safetensors
  - *From: Kijai*

- **Qwen3-4B official models** (model)
  - https://huggingface.co/Qwen/Qwen3-4B
  - *From: ˗ˏˋ⚡ˎˊ-*

- **seed-vc for voice swapping** (tool)
  - https://github.com/Plachtaa/seed-vc
  - *From: LarpsAI*

- **janky_memory_patcher** (tool)
  - https://github.com/drozbay/janky_memory_patcher
  - *From: JohnDopamine*

- **Wan22_A14B_T2V_lora_extract_r64.safetensors** (lora)
  - https://huggingface.co/drozbay/Wan2.2_A14B_lora_extract/blob/main/Wan22_A14B_T2V_lora_extract_r64.safetensors
  - *From: gokuvonlange*

- **ToonComposer** (repo)
  - https://github.com/TencentARC/ToonComposer
  - *From: GOD_IS_A_LIE*

- **NAG paper** (research)
  - https://chendaryen.github.io/NAG.github.io/
  - *From: DawnII*

- **Janky Memory Patcher** (tool)
  - https://github.com/drozbay/janky_memory_patcher
  - *From: Ablejones*

- **Flash-attention prebuild wheels** (tool)
  - https://github.com/mjun0812/flash-attention-prebuild-wheels/releases/tag/v0.4.10
  - *From: phazei*

- **Intel shared GPU memory override** (news)
  - https://videocardz.com/newz/intel-adds-shared-gpu-memory-override-feature-for-core-ultra-systems-enables-larger-vram-for-ai
  - *From: hicho*

- **StableAvatar repository** (repo)
  - https://github.com/Francis-Rings/StableAvatar
  - *From: NebSH*

- **ComfyUI StableAvatar implementation** (repo)
  - https://github.com/smthemex/ComfyUI_StableAvatar
  - *From: NebSH*

- **WanFM repository** (repo)
  - https://github.com/ff2416/WanFM
  - *From: dir2050*

- **MAGREF Wan2.1 I2V 14B GGUF with workflow** (model)
  - https://huggingface.co/QuantStack/MAGREF_Wan2.1_I2V_14B-GGUF/tree/main
  - *From: mdkb*

- **Execution inversion demo for lazy switches** (repo)
  - https://github.com/BadCafeCode/execution-inversion-demo-comfyui
  - *From: Kijai*

- **SeedVR2 upscaling workflow discussion** (workflow)
  - https://www.reddit.com/r/StableDiffusion/comments/1mqnlnf/adding_textures_and_finegrained_details_with/
  - *From: Shawneau 🍁 [CA]*

- **Wan2_1-T2V-14B-Phantom_fp8_e5m2_scaled_KJ.safetensors** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy_fp8_scaled/blob/main/T2V/Wan2_1-T2V-14B-Phantom_fp8_e5m2_scaled_KJ.safetensors
  - *From: Kijai*

- **Wan22-FastMix** (model)
  - https://huggingface.co/Zuntan/Wan22-FastMix/tree/main
  - *From: l҈u҈c҈i҈f҈e҈r҈*

- **ComfyUI-QwenImageWanBridge** (repo)
  - https://github.com/fblissjr/ComfyUI-QwenImageWanBridge
  - *From: fredbliss*

- **WanFM** (repo)
  - https://github.com/ff2416/WanFM?tab=readme-ov-file
  - *From: Kijai*

- **AutoGGUF** (tool)
  - https://github.com/leafspark/AutoGGUF
  - *From: Tony(5090)*

- **ComfyUI-ModelQuantizer** (node)
  - https://github.com/lum3on/ComfyUI-ModelQuantizer
  - *From: orabazes*

- **SDMatte** (repo)
  - https://github.com/vivoCameraResearch/SDMatte
  - *From: DawnII*

- **First frame object lora** (lora)
  - https://civitai.com/models/1863941?modelVersionId=2109632
  - *From: Дмитрий Марков*

- **Phantom VACE fp16 model** (model)
  - https://huggingface.co/Inner-Reflections/Wan2.1_VACE_Phantom/blob/main/wan-14B_vace_phantom_v2_fp16.safetensors
  - *From: Piblarg*

- **Fixed Fun-Control models** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy_fp8_scaled/tree/main/Fun
  - *From: Kijai*

- **Matrix Game 2.0 interactive model** (model)
  - https://huggingface.co/Skywork/Matrix-Game-2.0/tree/main
  - *From: hicho*

- **Wan LoRA trainer node** (tool)
  - https://github.com/jaimitoes/ComfyUI_Wan2_1_lora_trainer
  - *From: shockgun*

- **QwenVL ComfyUI nodes** (node)
  - https://github.com/alexcong/ComfyUI_QwenVL
  - *From: MilesCorban*

- **AutoGGUF tool** (tool)
  - https://github.com/leafspark/AutoGGUF/releases/tag/v2.0.1
  - *From: Tony(5090)*

- **StableAvatar** (repo)
  - https://github.com/Francis-Rings/StableAvatar
  - *From: army*

- **14B VACE Phantom v2 GGUF models** (model)
  - https://huggingface.co/orabazes/wan-14B_vace_phantom_v2_GGUF
  - *From: orabazes*

- **Context Options documentation** (documentation)
  - https://github.com/Kosinkadink/ComfyUI-AnimateDiff-Evolved/tree/main/documentation/nodes#context-optionsstandard-static
  - *From: Kijai*

- **Qwen-Image to WAN Bridge** (repo)
  - https://github.com/fblissjr/ComfyUI-QwenImageWanBridge
  - *From: fredbliss*

- **Git rebase vs merge visualization** (documentation)
  - https://miro.medium.com/v2/1*cEXnJtDL2tGeoN3KoCJSIw.png
  - *From: scf*

- **Stand-In Preprocessor fix** (repo)
  - https://github.com/WeChatCV/Stand-In_Preprocessor_ComfyUI/issues/3#issuecomment-3193744986
  - *From: mdkb*

- **ComfyUI-TopazVideoAI node** (node)
  - https://github.com/sh570655308/ComfyUI-TopazVideoAI
  - *From: . Not Really Human .*

- **ComfyUI-MultiGPU for VRAM management** (node)
  - https://github.com/pollockjj/ComfyUI-MultiGPU
  - *From: Jonathan*

- **FP32 text encoder** (model)
  - https://huggingface.co/Nap/umt5-xxl-encoder-only-fp32-safetensors/tree/main
  - *From: Benjimon*

- **Topaz Astra app** (tool)
  - https://astra.app
  - *From: . Not Really Human .*

- **ComfyUI PR #9392** (repo)
  - https://github.com/comfyanonymous/ComfyUI/pull/9392
  - *From: Kosinkadink*

- **Wan 2.2 official repository** (repo)
  - https://github.com/Wan-Video/Wan2.2
  - *From: Benjimon*

- **Modified H1111 implementation for small GPU** (repo)
  - https://github.com/maybleMyers/H1111/tree/wan2.2b
  - *From: Benjimon*

- **Mixed weights model files** (model)
  - https://huggingface.co/maybleMyers/wan_files_for_h1111/tree/main
  - *From: Benjimon*

- **MAGREF fp8 scaled models** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy_fp8_scaled/blob/main/I2V/Wan2_1-I2V-14B-MAGREF_fp8_e4m3fn_scaled_KJ.safetensors
  - *From: Kijai*

- **ShotVL multimodal LLMs for cinematic understanding** (model)
  - https://huggingface.co/Vchitect/ShotVL-3B
  - *From: s2k*

- **InfiniteTalk duplicated repository** (repo)
  - https://github.com/bmwas/InfiniteTalk
  - *From: DawnII*

- **RealisMotion (works with Wan)** (repo)
  - https://github.com/JingyunLiang/RealisMotion
  - *From: JohnDopamine*

- **Wan prompt guide** (guide)
  - https://www.instasd.com/post/wan2-2-whats-new-and-how-to-write-killer-prompts
  - *From: Josiah*

- **Prompt generator examples** (tool)
  - https://dengeai.com/prompt-generator
  - *From: Josiah*

- **InfiniteTalk examples** (repo)
  - https://github.com/bmwas/InfiniteTalk/tree/main/examples
  - *From: NebSH*

- **Wan 2.2 merged models** (model)
  - https://huggingface.co/Phr00t/WAN2.2-14B-Rapid-AllInOne
  - *From: Gateway*

- **Kenk's workflow** (workflow)
  - https://civitai.com/models/1824027
  - *From: Kenk*

- **CineTrans** (model)
  - https://github.com/UknowSth/CineTrans
  - *From: Kijai*

- **MTV Crafter** (model)
  - https://dingyanb.github.io/MTVCrafter-/
  - *From: Kijai*

- **Lightning LoRA usage guide** (workflow)
  - https://huggingface.co/lightx2v/Wan2.2-Lightning/discussions/20
  - *From: . Not Really Human .*

- **Runpod tutorial featuring Kijai's work** (tutorial)
  - https://www.youtube.com/watch?v=w9wlVeEa610
  - *From: ˗ˏˋ⚡ˎˊ-*

- **InfiniteTalk HuggingFace** (model)
  - https://huggingface.co/MeiGen-AI/InfiniteTalk/tree/main
  - *From: JohnDopamine*

- **InfiniteTalk GitHub repo** (repo)
  - https://github.com/MeiGen-AI/InfiniteTalk
  - *From: JohnDopamine*

- **InfiniteTalk ComfyUI branch** (repo)
  - https://github.com/MeiGen-AI/InfiniteTalk/tree/comfyui
  - *From: JohnDopamine*

- **FastWan 5B distillation** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/tree/main/FastWan
  - *From: TK_999*

- **VRGameDevGirl84's Fun Control workflow** (workflow)
  - https://discord.com/channels/1076117621407223829/1373520070596231251
  - *From: VRGameDevGirl84(RTX 5090)*

- **InfiniteTalk models** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy_fp8_scaled/blob/main/InfiniteTalk/
  - *From: Kijai*

- **Qwen Image Edit workflow** (workflow)
  - https://www.reddit.com/r/StableDiffusion/comments/1mu8ccu/comfyorgqwenimageedit_comfyui_hugging_face/
  - *From: Lodis*

- **InfiniteTalk GitHub** (repo)
  - https://github.com/MeiGen-AI/InfiniteTalk
  - *From: NebSH*

- **HiggsAudio ComfyUI wrapper** (tool)
  - https://github.com/Yuan-ManX/ComfyUI-HiggsAudio/
  - *From: NebSH*

- **ResolutionMaster node** (tool)
  - https://www.reddit.com/r/comfyui/comments/1mtzfyx/resolutionmaster_a_new_node_for_precise/
  - *From: Gateway {Dreaming Computers}*

- **Wan2_1-InfiniTetalk models** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy_fp8_scaled
  - *From: Kijai*

- **Standard Wan models** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/tree/main
  - *From: Kijai*

- **InfiniteTalk issue discussion** (repo)
  - https://github.com/kijai/ComfyUI-WanVideoWrapper/issues/1069#issuecomment-3200088392
  - *From: Kijai*

- **InfiniteTalk Q8 GGUF** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy_GGUF/blob/main/InfiniteTalk/Wan2_1-InfiniteTalk_Single_Q8.gguf
  - *From: Kijai*

- **MagRef Q8 GGUF** (model)
  - https://huggingface.co/QuantStack/MAGREF_Wan2.1_I2V_14B-GGUF/blob/main/MAGREF_Wan2.1_I2V_14B-Q8_0.gguf
  - *From: seitanism*

- **MagRef Q6 GGUF** (model)
  - https://huggingface.co/QuantStack/MAGREF_Wan2.1_I2V_14B-GGUF/blob/main/MAGREF_Wan2.1_I2V_14B-Q6_K.gguf
  - *From: seitanism*

- **Wan2.1 I2V 480P GGUF models** (model)
  - https://huggingface.co/city96/Wan2.1-I2V-14B-480P-gguf/tree/main
  - *From: Kijai*

- **MTVCrafter model** (model)
  - https://huggingface.co/yanboding/MTVCrafter
  - *From: Dream Making*

- **InfiniteTalk GGUF Q4/Q6** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy_GGUF/tree/main/InfiniteTalk
  - *From: Kijai*

- **Speed LoRAs discussion** (guide)
  - https://www.reddit.com/r/StableDiffusion/comments/1mujk6a/psa_speed_up_loras_for_wan_22_kill_everything/
  - *From: Dream Making*

- **V2V examples** (examples)
  - https://drive.google.com/drive/folders/1lG4A-VhL1QtSueMTe7D06fsQwof6eK8F
  - *From: NebSH*

- **ComfyUI-QwenImageWanBridge** (repo)
  - https://github.com/fblissjr/ComfyUI-QwenImageWanBridge/
  - *From: fredbliss*

- **CineTrans** (repo)
  - https://github.com/UknowSth/CineTrans
  - *From: Josiah*

- **ComfyUI-WanMoeKSampler** (repo)
  - https://github.com/stduhpf/ComfyUI-WanMoeKSampler
  - *From: xwsswww*

- **Wan21_Uni3C_controlnet_fp16.safetensors** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/blob/main/Wan21_Uni3C_controlnet_fp16.safetensors
  - *From: Ubertummen*

- **TREAD diffusion training speedup** (repo)
  - https://github.com/feffy380/diffusion-pipe/tree/tread
  - *From: Ada*

- **TREAD paper** (paper)
  - https://arxiv.org/pdf/2501.04765
  - *From: Ada*

- **TLBVFI interpolation ComfyUI implementation** (repo)
  - https://github.com/BobRandomNumber/ComfyUI-TLBVFI
  - *From: JohnDopamine*

- **Kijai sponsor page** (sponsor)
  - https://github.com/sponsors/kijai
  - *From: seitanism*

- **ComfyUI educational stream** (video)
  - https://www.youtube.com/watch?v=TZIijn-tvoc
  - *From: Fill*

- **Ultimate Vocal Remover** (tool)
  - https://ultimatevocalremover.com/
  - *From: NC17z*

- **Wan 2.2 Fun 5B Control** (model)
  - https://huggingface.co/alibaba-pai/Wan2.2-Fun-5B-Control
  - *From: DawnII*

- **InfiniteTalk GitHub issue with tips** (repo)
  - https://github.com/MeiGen-AI/InfiniteTalk/issues/6#issuecomment-3204108512
  - *From: NebSH*

- **South Park Alias Wavefront tutorials** (tutorial)
  - https://www.youtube.com/playlist?list=PL8F5B91C31A4FEE17
  - *From: samhodge*

- **Wan2.2-Fun-5B-Control models** (model)
  - https://huggingface.co/alibaba-pai/Wan2.2-Fun-5B-Control
  - *From: Kijai*

- **WanVideo GGUF InfiniteTalk models** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy_GGUF/tree/main/InfiniteTalk
  - *From: Kijai*

- **LightX2V Wan2.2 Lightning LoRAs** (lora)
  - https://huggingface.co/lightx2v/Wan2.2-Lightning/tree/main/Wan2.2-T2V-A14B-4steps-lora-rank64-Seko-V1.1
  - *From: blird*

- **ComfyUI-QwenImageWanBridge** (repo)
  - https://github.com/fblissjr/ComfyUI-QwenImageWanBridge
  - *From: fredbliss*

- **Banodoco Wan Video Discussion KB** (knowledge_base)
  - https://notebooklm.google.com/notebook/a08901b9-0511-4926-bbf8-3c86a12dc306?pli=1
  - *From: 𝕯𝖗. 𝕸𝖆𝖈𝖆𝖇𝖗𝖊 ☠*

- **Qwen Image dataset for video prompts** (dataset)
  - https://www.modelscope.cn/datasets/DiffSynth-Studio/Qwen-Image-Self-Generated-Dataset
  - *From: fredbliss*

- **InfiniteTalk GGUF models** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy_GGUF/tree/main/InfiniteTalk
  - *From: Kijai*

- **Wan2.1-I2V-14B GGUF** (model)
  - https://huggingface.co/city96/Wan2.1-I2V-14B-480P-gguf/tree/main
  - *From: Kijai*

- **Lumen T2V model** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/blob/main/Fun/Lumen/Wan2_1_Lumen-T2V-1.3B-V1.0_bf16.safetensors
  - *From: Kijai*

- **Lumen GitHub repository** (repo)
  - https://github.com/Kunbyte-AI/Lumen/tree/main
  - *From: Kijai*

- **GGUF VACE modules** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy_GGUF/blob/main/VACE/Wan2_1-VACE_module_14B_Q8_0.gguf
  - *From: Kijai*

- **InfiniteTalk single character model** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/tree/main/InfiniteTalk
  - *From: Kijai*

- **MultiTalk weights** (model)
  - https://huggingface.co/MeiGen-AI/MeiGen-MultiTalk/blob/main/multitalk.safetensors
  - *From: samhodge*

- **InfiniteTalk workflow examples** (workflow)
  - *From: Kijai*

- **Ostris Wan2.2 orbit shot LoRA** (model)
  - https://huggingface.co/ostris/wan22_i2v_14b_orbit_shot_lora
  - *From: Drommer-Kille*

- **Wan2.2-Fun-A14B-InP model** (model)
  - https://huggingface.co/alibaba-pai/Wan2.2-Fun-A14B-InP
  - *From: Zabo*

- **PUSA-VidGen Wan2.2 version development** (repo)
  - https://github.com/Yaofang-Liu/Pusa-VidGen/issues/34
  - *From: JohnDopamine*

- **ComfyUI-for-Nuke integration** (tool)
  - https://github.com/vinavfx/ComfyUI-for-Nuke
  - *From: samhodge*

- **InfiniteTalk I2V example workflow** (workflow)
  - https://github.com/kijai/ComfyUI-WanVideoWrapper/blob/main/example_workflows/wanvideo_I2V_InfiniteTalk_example_01.json
  - *From: JohnDopamine*

- **InfiniteTalk V2V example workflow** (workflow)
  - https://github.com/kijai/ComfyUI-WanVideoWrapper/blob/main/example_workflows/wanvideo_InfiniteTalk_V2V_example_01.json
  - *From: JohnDopamine*

- **Qwen text enhancement for WanVideo** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/tree/main/Qwen
  - *From: ˗ˏˋ⚡ˎˊ-*

- **2.2 I2V InfiniteTalk workflow** (workflow)
  - https://discord.com/channels/1076117621407223829/1396263390296674324/1408070176095735890
  - *From: DawnII*

- **InfiniteTalk GGUF models** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy_GGUF/tree/main/InfiniteTalk
  - *From: DawnII*

- **ComfyUI QwenImage WanBridge** (tool)
  - https://github.com/fblissjr/ComfyUI-QwenImageWanBridge
  - *From: fredbliss*

- **Execution blocker for ComfyUI debugging** (tool)
  - https://github.com/BadCafeCode/execution-inversion-demo-comfyui/blob/d9eebfaa1a6a33067e8c9108ef093b48279c4cbb/flow_control.py#L133-L158
  - *From: ˗ˏˋ⚡ˎˊ-*

- **ComfyUI-QwenImageWanBridge** (repo)
  - https://github.com/fblissjr/ComfyUI-QwenImageWanBridge
  - *From: fredbliss*

- **WanVideo_comfy models** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy
  - *From: Josiah*

- **WanVideoWrapper workflows** (workflow)
  - https://github.com/kijai/ComfyUI-WanVideoWrapper/tree/main/example_workflows
  - *From: JohnDopamine*

- **PUSA VidGen update** (repo)
  - https://github.com/Yaofang-Liu/Pusa-VidGen/commit/4b664d213c5d6a0c141c5e7e8e8d3e9fb5391182
  - *From: JohnDopamine*

- **3-alpha-ultra model** (model)
  - https://huggingface.co/deca-ai/3-alpha-ultra
  - *From: Ada*

- **CineScale LoRA** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/tree/main/CineScale
  - *From: Kijai*

- **CineScale original repo** (repo)
  - https://github.com/Eyeline-Labs/CineScale
  - *From: s2k*

- **FreeScale predecessor** (repo)
  - https://github.com/ali-vilab/FreeScale
  - *From: JohnDopamine*

- **Blender OpenPose addons** (tool)
  - https://impactframes.gumroad.com/l/fxnyez and https://toyxyz.gumroad.com/l/ciojz
  - *From: xwsswww*

- **InfiniteTalk example workflow** (workflow)
  - https://github.com/kijai/ComfyUI-WanVideoWrapper/blob/main/example_workflows/wanvideo_InfiniteTalk_V2V_example_01.json
  - *From: samhodge*

- **Waver video project page** (model)
  - http://www.waver.video/
  - *From: NebSH*

- **Ultimate Vocal Remover 5** (tool)
  - *From: samhodge*

- **Wan 2.2 5B Turbo** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/tree/main/Wan22-Turbo
  - *From: Kijai*

- **Unofficial Wan 2.2 5B Turbo** (model)
  - https://huggingface.co/quanhaol/Wan2.2-TI2V-5B-Turbo
  - *From: DawnII*

- **Qwen text encoders** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/tree/main/Qwen
  - *From: Dita*

- **UniAnimate Lora** (lora)
  - https://huggingface.co/Kijai/WanVideo_comfy/blob/main/UniAnimate-Wan2.1-14B-Lora-12000-fp16.safetensors
  - *From: ˗ˏˋ⚡ˎˊ-*

- **LTXV Instagram examples** (example)
  - https://www.instagram.com/reel/DJUHfgso5yx/?utm_source=ig_web_copy_link&igsh=MzRlODBiNWFlZA==
  - *From: NebSH*

- **CineScale LoRA** (lora)
  - https://github.com/Eyeline-Labs/CineScale/tree/main
  - *From: Kijai*

- **MediaSyncer tool** (tool)
  - https://whatdreamscost.github.io/MediaSyncer/
  - *From: JohnDopamine*

- **Kenk's big workflow** (workflow)
  - https://civitai.com/models/1824027?modelVersionId=2137850
  - *From: Kenk*

- **Sliders project** (tool)
  - https://sliders.baulab.info/
  - *From: phazei*

- **360 degree rotation LoRA** (lora)
  - https://civitai.com/models/1346623/360-degree-rotation-microwave-rotation-wan21-i2v-lora
  - *From: xwsswww*

- **InfiniteTalk models** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/tree/main/InfiniteTalk
  - *From: seitanism*

- **DawnII's CausVid testing thread** (discussion)
  - https://discord.com/channels/1076117621407223829/1399888174519685224
  - *From: DawnII*

- **MelBandRoFormer ComfyUI wrapper** (repo)
  - https://github.com/kijai/ComfyUI-MelBandRoFormer
  - *From: Kijai*

- **InfiniteTalk GGUF models** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy_GGUF/tree/main/InfiniteTalk
  - *From: Kijai*

- **Kijai's Wan 2.2 scaled models** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy_fp8_scaled/tree/main
  - *From: Kenk*

- **Wan 2.2 5B Turbo FP8 E5M2** (model)
  - https://huggingface.co/patientxtr/wan22ti2v5bturbofp8e5m2
  - *From: patientx*

- **WAN-14B VACE Phantom v2 GGUF Q8** (model)
  - https://huggingface.co/orabazes/wan-14B_vace_phantom_v2_GGUF/blob/main/wan-14B_vace_phantom_v2_Q8.gguf
  - *From: xwsswww*

- **WAN-14B VACE Phantom v2 GGUF Q5_K_M** (model)
  - https://huggingface.co/orabazes/wan-14B_vace_phantom_v2_GGUF/blob/main/wan-14B_vace_phantom_v2_Q5_K_M.gguf
  - *From: orabazes*

- **ComfyUI-MultiGPU** (repo)
  - https://github.com/pollockjj/ComfyUI-MultiGPU
  - *From: Jonathan*

- **Mellon project** (repo)
  - https://github.com/cubiq/Mellon/
  - *From: Ablejones*

- **WanVideo GGUF repository** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy_GGUF/tree/main
  - *From: xwsswww*

- **MAGREF I2V model** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy_fp8_scaled/blob/main/I2V/Wan2_1-I2V-14B-MAGREF_fp8_e4m3fn_scaled_KJ.safetensors
  - *From: Kijai*

- **Fantasy Portrait + InfiniteTalk workflow** (workflow)
  - *From: Kijai*

- **Audio separation node** (node)
  - *From: Kenk*

- **HXHY-Realistic_Kontext_LoRA** (lora)
  - https://huggingface.co/AlekseyCalvin/HXHY-Realistic_Kontext_LoRA_byXiaolxl
  - *From: Akumetsu971*

- **Magic-TryOn repository** (repo)
  - github.com/vivoCameraResearch/Magic-TryOn
  - *From: Prelifik*

- **ComfyUI_WanVace-pipeline** (node pack)
  - https://github.com/tarkansarim/ComfyUI_WanVace-pipeline
  - *From: xwsswww*

- **MTVCrafter info page** (documentation)
  - https://dingyanb.github.io/MTVCrafter-/
  - *From: The Shadow (NYC)*

- **Tarkan Sarim LinkedIn demo** (demo)
  - https://www.linkedin.com/posts/tarkan-sarim-a069347_comfyui-ugcPost-7365141303698886656-LuOF
  - *From: NebSH*

- **VACE methods knowledge base** (documentation)
  - https://nathanshipley.notion.site/Wan-2-1-Knowledge-Base-1d691e115364814fa9d4e27694e9468f#1d691e11536481f380e4cbf7fa105c05
  - *From: mdkb*

- **Video-to-audio-through-text alternative** (repo)
  - https://github.com/DragonLiu1995/video-to-audio-through-text
  - *From: sneha1743*

- **WanMoeKSampler for automating H/L sampler split** (tool)
  - https://github.com/stduhpf/ComfyUI-WanMoeKSampler
  - *From: BobbyD4AI*

- **Magic-TryOn repository** (repo)
  - https://github.com/vivoCameraResearch/Magic-TryOn
  - *From: sneha1743*

- **New anime style LoRA for Wan 2.2** (lora)
  - https://discord.com/channels/1076117621407223829/1409548743425917041
  - *From: crinklypaper*

- **Wan 2.2 S2V announcement** (news)
  - https://x.com/Alibaba_Wan/status/1960012297059057935
  - *From: Abx*

- **Wan audio announcement** (news)
  - https://x.com/Alibaba_Wan/status/1959963989703880866
  - *From: Abx*

- **ComfyUI blog on masking and scheduling LoRA weights** (tutorial)
  - https://blog.comfy.org/p/masking-and-scheduling-lora-and-model-weights
  - *From: Draken*

- **Meetup presentation** (event)
  - https://lu.ma/62hfwf86
  - *From: The Shadow (NYC)*

- **wav2vec2 safetensors conversion** (model)
  - https://huggingface.co/Kijai/wav2vec2_safetensors/tree/main
  - *From: Kijai*

- **mdkb's VACE workflows zip** (workflow)
  - https://markdkberry.com/workflows/footprints/
  - *From: mdkb*

- **T2V 2.2 14b workflow on Civitai** (workflow)
  - https://civitai.com/models/1868641?modelVersionId=2147818
  - *From: crinklypaper*

- **ATI model and tracking points** (repo)
  - https://github.com/bytedance/ATI
  - *From: mdkb*

- **Mel-Band Roformer Vocal Model** (tool)
  - https://github.com/KimberleyJensen/Mel-Band-Roformer-Vocal-Model
  - *From: DawnII*

- **Wrapper example workflows** (workflow)
  - https://github.com/kijai/ComfyUI-WanVideoWrapper/tree/main/example_workflows
  - *From: Mu5hr00m_oO*

- **Wan 2.2 S2V 14B model** (model)
  - https://huggingface.co/Wan-AI/Wan2.2-S2V-14B
  - *From: DawnII*

- **Wan S2V demo page** (demo)
  - https://humanaigc.github.io/wan-s2v-webpage/
  - *From: Screeb*

- **HuggingFace demo space** (demo)
  - https://huggingface.co/spaces/Wan-AI/Wan2.2-S2V
  - *From: ZeusZeus (RTX 4090)*

- **Fixed HotReloadHack** (tool)
  - https://github.com/kijai/ComfyUI-HotReloadHack
  - *From: Kijai*

- **Wan 2.2 S2V model** (model)
  - https://huggingface.co/Wan-AI/Wan2.2-S2V-14B
  - *From: Impactframes*

- **Wan S2V demo space** (demo)
  - https://huggingface.co/spaces/Wan-AI/Wan2.2-S2V
  - *From: NebSH*

- **WanVideo S2V models** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy_fp8_scaled/tree/main/S2V
  - *From: DawnII*

- **CFG Skimming branch** (repo)
  - https://github.com/Mu5hr00moO/ComfyUI-WanVideoWrapper/tree/CFG_Skimming
  - *From: Mu5hr00m_oO*

- **NYC ComfyUI meetup** (event)
  - https://luma.com/62hfwf86
  - *From: ericxtang*

- **S2V wav2vec2 model** (model)
  - https://huggingface.co/Wan-AI/Wan2.2-S2V-14B/blob/main/wav2vec2-large-xlsr-53-english/model.safetensors
  - *From: slmonker*

- **ComfyUI Windows Portable** (tool)
  - https://github.com/YanWenKun/ComfyUI-Windows-Portable
  - *From: Kenk*

- **Skimmed CFG** (repo)
  - https://github.com/Extraltodeus/Skimmed_CFG
  - *From: MilesCorban*

- **KokoroTTS ComfyUI node** (node)
  - https://github.com/benjiyaya/ComfyUI-KokoroTTS
  - *From: daking999*

- **Nano Banana** (tool)
  - https://aistudio.google.com/apps/bundled/past_forward?showPreview=true&showAssistant=true
  - *From: asd*

- **Wan S2V paper** (paper)
  - https://humanaigc.github.io/wan-s2v-webpage/content/wan-s2v.pdf
  - *From: MilesCorban*

- **Kijai VACE models** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy_GGUF/tree/main/VACE
  - *From: xwsswww*

- **ComfyUI native S2V PR** (repo)
  - https://github.com/comfyanonymous/ComfyUI/pull/9568
  - *From: comfy*

- **Audio Duration Node documentation** (tool)
  - https://comfyai.run/documentation/AudioDurationNode
  - *From: samhodge*

- **S2V workflow example** (workflow)
  - https://github.com/user-attachments/files/22001431/sound_to_video_wan_example.json
  - *From: Kijai*

- **AniSora V3 model** (model)
  - https://huggingface.co/IndexTeam/Index-anisora/tree/main/V3
  - *From: DreamWeebs*

- **WanVideo ComfyUI fp8 scaled models** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy_fp8_scaled/tree/main/I2V/AniSora
  - *From: Kijai*

- **Background replacement workflow** (workflow)
  - https://discord.com/channels/1076117621407223829/1376383134303784970/1376383134303784970
  - *From: Dream Making*

- **ElevenLabs video to sound generator** (tool)
  - https://videotosfx.elevenlabs.io/
  - *From: Ablejones*

- **S2V branch pull request** (repo)
  - https://github.com/kijai/ComfyUI-WanVideoWrapper/pull/1122
  - *From: Mu5hr00m_oO*

- **Wan 2.2 full safetensor models** (model)
  - https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/tree/main/split_files/diffusion_models
  - *From: ingi // SYSTMS*

- **HunyuanVideo-Foley** (model)
  - https://huggingface.co/tencent/HunyuanVideo-Foley
  - *From: JohnDopamine*

- **HunyuanVideo-Foley GitHub** (repo)
  - https://github.com/Tencent-Hunyuan/HunyuanVideo-Foley
  - *From: JohnDopamine*

- **Ultimate Vocal Remover** (tool)
  - https://ultimatevocalremover.com/
  - *From: NC17z*

- **MelBandRoFormer for ComfyUI** (repo)
  - https://github.com/kijai/ComfyUI-MelBandRoFormer
  - *From: Kenk*

- **SAM2 video masking node** (repo)
  - https://github.com/kijai/ComfyUI-segment-anything-2
  - *From: JalenBrunson*

- **CFG Skimming workflow** (workflow)
  - https://drive.google.com/file/d/1aHVLpLlzJ4805L5IwCmKabb5COxX2ZPo/view?usp=sharing
  - *From: Mu5hr00m_oO*

- **Skimmed CFG documentation** (documentation)
  - https://deepwiki.com/Extraltodeus/Skimmed_CFG
  - *From: Mu5hr00m_oO*

- **ComfyUI-Sapiens pose detection** (repo)
  - https://github.com/smthemex/ComfyUI_Sapiens
  - *From: Impactframes.*

- **ComfyUI-Rife-Tensorrt** (repo)
  - https://github.com/yuvraj108c/ComfyUI-Rife-Tensorrt
  - *From: Mu5hr00m_oO*

- **HunyuanVideo-Foley** (repo)
  - https://github.com/Tencent-Hunyuan/HunyuanVideo-Foley
  - *From: Karo*

- **HunyuanVideo-Foley demo** (tool)
  - https://szczesnys.github.io/hunyuanvideo-foley/
  - *From: pom*

- **QwenImageWanBridge research nodes** (repo)
  - https://github.com/fblissjr/ComfyUI-QwenImageWanBridge/tree/main/nodes/research
  - *From: fredbliss*

- **PUSA-VidGen update** (repo)
  - https://github.com/Yaofang-Liu/Pusa-VidGen/commit/4b664d213c5d6a0c141c5e7e8e8d3e9fb5391182
  - *From: DawnII*

- **Krea realtime video** (tool)
  - https://www.krea.ai/blog/announcing-realtime-video
  - *From: Nekodificador*

- **Unofficial VACE 2.2 merge** (model)
  - https://huggingface.co/lym00/Wan2.2_T2V_A14B_VACE-test/tree/main
  - *From: screwfunk*

- **ComfyUI-VibeVoice wrapper** (repo)
  - https://github.com/wildminder/ComfyUI-VibeVoice
  - *From: DawnII*

- **ComfyUI-Chatterbox for voice cloning** (repo)
  - https://github.com/wildminder/ComfyUI-Chatterbox
  - *From: N0NSens*

- **Higgs Audio TTS model** (model)
  - https://github.com/boson-ai/higgs-audio
  - *From: Juampab12*

- **MiniMax-bmo removal node** (repo)
  - https://github.com/casterpollux/MiniMax-bmo
  - *From: JohnDopamine*

- **Native S2V test workflow (35 second generation)** (workflow)
  - *From: comfy*

- **Updated native S2V workflow with first frame fix** (workflow)
  - *From: comfy*

- **Qwen2.5-VL-7B-Instruct-GGUF models** (model)
  - https://huggingface.co/unsloth/Qwen2.5-VL-7B-Instruct-GGUF/tree/main
  - *From: xwsswww*

- **Fixed S2V workflow for color mismatch** (workflow)
  - https://discord.com/channels/1076117621407223829/1342763350815277067/1410771695022637187
  - *From: ˗ˏˋ⚡ˎˊ-*

- **S2V model checkpoint** (model)
  - https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/blob/main/split_files/diffusion_models/wan2.2_s2v_14B_bf16.safetensors
  - *From: ˗ˏˋ⚡ˎˊ-*

- **diffusion-pipe-TREAD** (tool)
  - https://github.com/Ada123-a/diffusion-pipe-TREAD
  - *From: ˗ˏˋ⚡ˎˊ-*

- **HunyuanVideo-Foley wrapper** (tool)
  - https://github.com/if-ai/ComfyUI_HunyuanVideoFoley
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Kijai example workflows** (workflow)
  - https://github.com/kijai/ComfyUI-WanVideoWrapper/tree/main/example_workflows
  - *From: JohnDopamine*

- **LoRA scheduling article** (resource)
  - https://blog.comfy.org/p/masking-and-scheduling-lora-and-model-weights
  - *From: ˗ˏˋ⚡ˎˊ-*

- **CineScale super-resolution** (model)
  - https://github.com/Eyeline-Labs/CineScale/
  - *From: JohnDopamine*

- **ComfyUI-WanVideoWrapper commits** (repo)
  - https://github.com/kijai/ComfyUI-WanVideoWrapper/commits/main/
  - *From: JohnDopamine*

- **ComfyUI-VibeVoice** (repo)
  - https://github.com/wildminder/ComfyUI-VibeVoice
  - *From: JohnDopamine*

- **MAGREF model** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/blob/main/Wan2_1-Wan-I2V-MAGREF-14B_fp8_e4m3fn.safetensors
  - *From: Mancho*

- **Scaled MAGREF model** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy_fp8_scaled/blob/main/I2V/Wan2_1-I2V-14B-MAGREF_fp8_e4m3fn_scaled_KJ.safetensors
  - *From: Mancho*

- **Wan 2.2 LoRAs** (model)
  - https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/tree/main/split_files/loras
  - *From: Ashtar*

- **ComfyUI HunyuanFoley** (repo)
  - https://github.com/aistudynow/Comfyui-HunyuanFoley
  - *From: 𝕯𝖗. 𝕸𝖆𝖈𝖆𝖇𝖗𝖊 ☠*

- **ComfyUI HunyuanVideoFoley** (repo)
  - https://github.com/if-ai/ComfyUI_HunyuanVideoFoley
  - *From: 𝕯𝖗. 𝕸𝖆𝖈𝖆𝖇𝖗𝖊 ☠*

- **ComfyUI Custom Sigma Editor** (tool)
  - https://github.com/JoeNavark/comfyui_custom_sigma_editor
  - *From: Nekodificador*

- **ComfyUI HunyuanVideo Foley** (repo)
  - https://github.com/if-ai/ComfyUI_HunyuanVideoFoley
  - *From: Ablejones*

- **SageAttention releases** (repo)
  - https://github.com/woct0rdho/SageAttention/releases
  - *From: Ablejones*

- **ComfyUI-AnimateDiff-Evolved context documentation** (documentation)
  - https://github.com/Kosinkadink/ComfyUI-AnimateDiff-Evolved/tree/main/documentation/nodes#context-options-and-view-options
  - *From: Mu5hr00m_oO*

- **ComfyUI portable build with PyTorch 2.8** (tool)
  - https://huggingface.co/Nakamotosatoshi/ComfyUI_0.3.55
  - *From: hicho*

- **FrameUtilitys custom nodes** (tool)
  - https://github.com/lum3on/ComfyUI-FrameUtilitys
  - *From: SonidosEnArmonía*

- **CineScale implementation** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/tree/main/CineScale
  - *From: ˗ˏˋ⚡ˎˊ-*

- **WAN workflows collection** (workflow)
  - https://github.com/bluespork
  - *From: hicho*

- **MAGREF project page** (model)
  - https://magref-video.github.io/
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Lightx2v I2V LoRA** (model)
  - https://huggingface.co/lightx2v/Wan2.1-I2V-14B-480P-StepDistill-CfgDistill-Lightx2v
  - *From: Ablejones*

- **ComfyUI API nodes for nano banana** (workflow)
  - https://blog.comfy.org/p/nano-banana-via-comfyui-api-nodes
  - *From: DawnII*

- **Reddit workflow for Wan 2.2** (workflow)
  - https://www.reddit.com/r/StableDiffusion/comments/1mxu5tq/wan_22_text2video_with_ultimate_sd_upscaler_the/
  - *From: chrisd0073*

- **CineScale workflows** (workflow)
  - https://civitai.com/models/1893519/cinescalewan22-highlow-noise-three-shot-intelligent-prompt-word-to-video-high-detail-workflow-v1
  - *From: BecauseReasons*

- **Qwen2.5-7B-Instruct GGUF** (model)
  - huggingface.co/bartowski/Qwen2.5-7B-Instruct-GGUF
  - *From: Prelifik*

- **Wan prompting documentation** (documentation)
  - https://www.instasd.com/post/wan2-2-whats-new-and-how-to-write-killer-prompts
  - *From: 𝕯𝖗. 𝕸𝖆𝖈𝖆𝖇𝖗𝖊 ☠*

- **Wan camera moves and controls documentation** (documentation)
  - https://alidocs.dingtalk.com/i/nodes/EpGBa2Lm8aZxe5myC99MelA2WgN7R35y
  - *From: 𝕯𝖗. 𝕸𝖆𝖈𝖆𝖇𝖗𝖊 ☠*

- **VACE examples workflow** (workflow)
  - https://github.com/kijai/ComfyUI-WanVideoWrapper/blob/main/example_workflows/wanvideo_1_3B_VACE_examples_03.json
  - *From: Juampab12*

- **Chinese wav2vec2 model** (model)
  - https://huggingface.co/jonatasgrosman/wav2vec2-large-xlsr-53-chinese-zh-cn/tree/main
  - *From: piscesbody*


## Known Limitations

- **24fps generations often sped up**
  - Videos at 24fps randomly correct speed or feel sped up, not consistent
  - *From: Ruairi Robinson*

- **Poor timestamping control**
  - Wan 2.2 not good with simple timestamping like 'this appears at 3s mark' unlike Veo
  - *From: Drommer-Kille*

- **Cannot control light colors effectively**
  - Impossible to control light colors for specific cinematography like Blade Runner style
  - *From: GOD_IS_A_LIE*

- **Character LoRA applies to all faces**
  - Person LoRAs apply to every character's face in generation, difficult to limit to specific characters
  - *From: Ruairi Robinson*

- **WAN 2.2 generation times still too long**
  - 15+ minute runs make it less practical than closed models despite better quality
  - *From: Drommer-Kille*

- **SageAttention3 poor quality**
  - Early access version has terrible quality, needs step/block restrictions to be usable
  - *From: Kijai*

- **RadialAttention strict resolution requirements**
  - Only works with resolutions where token count is divisible by block size
  - *From: Kijai*

- **VACE 2.1 with 2.2 not perfect**
  - Using 2.1 VACE with 2.2 models doesn't work perfectly, waiting for 2.2 VACE release
  - *From: seitanism*

- **bf16 required for original T5 implementation**
  - Original WAN T5 code doesn't work properly in fp16, requires bf16 or ComfyUI bridge
  - *From: Kijai*

- **Camera prompt adherence poor in I2V**
  - Even with detailed prompts, CFG 3.5, and various tricks, camera movement prompts don't work well in I2V mode
  - *From: Juan Gea*

- **Male genitalia generation issues**
  - WAN 2.2 struggles with male genitalia generation, often creates fingers instead. Training LoRAs for this is difficult
  - *From: Kenk*

- **Context options don't work well with I2V**
  - Context window functionality designed primarily for T2V, limited effectiveness in I2V workflows
  - *From: Kijai*

- **Motion varies significantly with resolution**
  - Higher resolutions like 576x1024 produce slow-motion effects, while 480x720 has more natural motion
  - *From: shockgun*

- **Camera control ignores prompts**
  - Even on their website, camera movements like 'camera overpassing a runner' don't work reliably
  - *From: Juan Gea*

- **5B model has inferior motion quality**
  - Motion is far from 2.2 A14B quality, generates weird motion or bad faces
  - *From: Lodis*

- **Loop args don't work well with newer models**
  - Only worked on 1.3B model, didn't blend well with 2.2
  - *From: Kijai*

- **Context generation can have scene jumps**
  - Sometimes overlap is not enough to blend and you get huge jumps
  - *From: Kijai*

- **Color correction node oversaturates**
  - Often 'corrects' otherwise ok input to be oversaturated
  - *From: lostintranslation*

- **No LightX2V I2V LoRA for 14B at 720p**
  - Only 480p version available, but works with 480p
  - *From: Lodis*

- **Context overlap technique has limits**
  - Won't work well with I2V, has limits when used with pure T2V without control
  - *From: Kijai*

- **Current LoRAs pull 2.2 back to 2.1 quality**
  - Need proper 2.2 LoRAs to fully unlock 2.2 capabilities
  - *From: The Shadow (NYC)*

- **50/50 step split may not be optimal**
  - Should probably be more like 25% high noise, 75% low noise
  - *From: ArtOfficial*

- **Context windows don't work well with I2V**
  - Due to strong image conditioning, causes video to replay after frame count
  - *From: Kijai*

- **VACE 2.1 poor performance on high noise model**
  - Works fine on low noise model but terrible results on high noise model
  - *From: Kijai*

- **GGUF quantized models poor quality**
  - Only FP8 or FP16 models work well, quantized models don't work good
  - *From: avataraim*

- **Sage Attention limited benefits on older GPUs**
  - Cards lower than RTX 3000 series won't see much improvement
  - *From: xwsswww*

- **5B model doesn't work well with existing LoRAs**
  - LightX and other 14B LoRAs incompatible due to size differences
  - *From: WorldX*

- **Context windows don't maintain action coherence for long videos**
  - Guy running will change pace, action differs, background changes over 15 seconds
  - *From: Juan Gea*

- **Model doesn't handle 24fps well**
  - Causes burnt frames, better to generate at 16fps and interpolate
  - *From: thaakeno*

- **9:16 aspect ratio produces weird character motions**
  - Walking characters do weird motions in vertical format, works better in higher ratios
  - *From: scf*

- **5B model very slow on 3090**
  - 7 minutes for generation on RTX 3090
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Phantom not compatible with 2.2 high noise model**
  - Seems fully incompatible when tested
  - *From: Kijai*

- **5B model extension doesn't work well**
  - Tested extension with 5B model, results not good
  - *From: Kijai*

- **5B first to last frame by giving last latent doesn't work**
  - Attempted FLF approach failed with 5B model
  - *From: Kijai*

- **Character LoRAs from 2.1 don't trigger properly in 2.2**
  - LoRAs that work in 2.1 fail to trigger in 2.2 I2V
  - *From: screwfunk*

- **2.2 T2V produces noisy/fuzzy results in wrapper**
  - Multiple users report poor quality compared to 2.1
  - *From: AffenBrot*

- **VACE 2.2 high noise model has limited compatibility**
  - Some modalities don't work at all, some work weakly. Not worth using over 2.1 VACE
  - *From: Kijai*

- **Middle frame transitions rarely produce proper motions**
  - While it works technically, proper motions between images are rare
  - *From: Kijai*

- **Depth control with VACE 2.2 not very effective**
  - Depth does something but results are not very great
  - *From: Kijai*

- **2.2 not drop-in replacement for 2.1**
  - LoRAs and workflows from 2.1 don't directly work with 2.2
  - *From: Karo*

- **5B model quality issues**
  - Generally pretty garbage quality compared to 14B model
  - *From: Screeb*

- **Camera motion keywords ignored**
  - Model tends to ignore camera movement prompts in some workflows
  - *From: Rainsmellsnice*

- **LoRA masking not supported for Wan**
  - Advanced masking techniques for selective training not available yet
  - *From: Ryzen*

- **Quality degradation above 81 frames**
  - Anything above 81 frames starts to really suffer in quality
  - *From: ✧ฅโ๑ↀᆺↀ ๑ใฅ✧PookieNumnums*

- **Motion quality suffers at higher resolutions**
  - Higher resolution causes motion to suffer, may need more steps or different params
  - *From: Kijai*

- **fp8 can hallucinate incorrect objects**
  - fp8 precision can change subject matter completely (divers becoming seaweed)
  - *From: hicho*

- **High noise layer difficult to work with**
  - Messing with the high layer is problematic even with 3 sampler approach
  - *From: Karo*

- **Model struggles with object state changes**
  - Difficult to show actions like stealing ice cream - tends to maintain original object states
  - *From: Kijai*

- **Multitalk doesn't work well with Wan 2.2**
  - Audio sync issues, works better with 2.1
  - *From: Kijai*

- **First frame last frame doesn't work with 5B model**
  - Only available for 14B model currently
  - *From: Kijai*

- **Frames over 81 cause weird twisting artifacts**
  - Generation quality degrades significantly beyond 81 frames
  - *From: Kijai*

- **Wan doesn't handle destruction/gore well**
  - Struggles with realistic blood/flesh texturing and destruction concepts
  - *From: DevouredBeef*

- **lightx2v doesn't work properly with high noise model**
  - Requires using cfg for first steps, fine balance needed between cfg and LoRA strength
  - *From: Kijai*

- **Hard limit is VRAM for frame count**
  - Without guidance, generation just loops after 81 frames
  - *From: Kijai*

- **LoRA extraction only works against training model**
  - Can't extract from one model and apply to another effectively
  - *From: Kijai*

- **Caching doesn't work with distillations**
  - Most don't use easycache because it doesn't really work with the distillations
  - *From: Kijai*

- **lightx2v adds same 1girl face in 2.2**
  - Tends to add the same face, making model more 2.1-like
  - *From: RRR*

- **Wan 2.2 doesn't like violence**
  - Model tends to ignore violent actions in prompts like hitting
  - *From: mamad8*

- **High shift values can cause distortions**
  - Increasing shift too much makes it harder for video to find coherent path, leading to distortions or garbled mess
  - *From: gokuvonlange*

- **2.1 LoRAs don't work optimally with 2.2**
  - Require higher strength settings which harms model quality, but necessary unless using more steps
  - *From: Juampab12*

- **Camera controls lost with LoRA usage**
  - Excellent at character motion but camera controls except zoom are gone when using LoRA
  - *From: Rainsmellsnice*

- **Native nodes don't support wrapper scheduling features**
  - String to float conversion and advanced scheduling only work with wrapper nodes
  - *From: Kijai*

- **Wan 2.2 5B model has poor motion quality**
  - Motion doesn't come close to what high noise expert can achieve despite good image quality
  - *From: Kijai*

- **VACE character consistency requires LoRA**
  - Nearly impossible to get character consistency without a character LoRA
  - *From: Nekodificador*

- **Multitalk not compatible with 720p models**
  - Multitalk works with 480p but generates noise with 720p models
  - *From: Juan Gea*

- **Enhance-a-video bad for high noise model**
  - In experience it's bad for the high noise, but somewhat useful for the low noise
  - *From: Kijai*

- **New lightning LoRAs only work for T2V**
  - I2V compatibility is broken - no motion, poor prompt adherence. I2V-specific LoRAs not released yet
  - *From: Kijai/DawnII*

- **Reduced dynamic range in 2.2**
  - Wan 2.2 Lightning has significantly reduced dynamic performance compared to 2.1 version
  - *From: wange1002*

- **Struggles with dark/moody scenes**
  - New lightning LoRAs produce overly bright results, lose cinematic/moody tones
  - *From: gokuvonlange*

- **Guide image support buggy in 2.2**
  - Guide images have issues especially in I2V mode
  - *From: TK_999/NebSH*

- **New Lightning LoRA high noise pass produces poor results**
  - Weird camera fade effects, poor prompt adherence compared to old LoRAs
  - *From: Doctor Shotgun*

- **Lightning LoRAs lack text embedding layers**
  - Missing important layers that affect LightX2V performance
  - *From: Kijai*

- **480p resolution produces slow motion and artifacts**
  - Lower resolutions don't work well with Lightning LoRAs
  - *From: Kijai*

- **5B model behaves differently from 14B models**
  - Not interchangeable, 5B handles first/last frame differently
  - *From: seitanism*

- **Lightning LoRA breaks complex camera movements**
  - Lightning LoRA on high noise model causes issues with complex camera movements and motion quality
  - *From: SonidosEnArmonía*

- **Camera fade out issue with 2.2 LoRA**
  - 2.2 LoRA causes unwanted camera fade out effects that weren't present in Pisces
  - *From: Doctor Shotgun*

- **Lightning LoRA has strong bias**
  - Lightning LoRA has way too big bias, doesn't handle lower strengths well like LightX2V could
  - *From: Kijai*

- **Split screen with 'cut' keyword**
  - Using the word 'cut' in prompts causes unwanted split-screen effects
  - *From: IceAero*

- **New lightning loras destroy motion and prompt following**
  - Particularly bad prompt adherence when using high+low, drops half the prompt even with 2 CFG
  - *From: flo1331*

- **Fast 5B model has poor prompt following**
  - About zero prompt following, quality degraded
  - *From: N0NSens*

- **VAE decode time is very slow**
  - 60 seconds to generate, 80 seconds to decode. Decoding longer than generating
  - *From: Kijai*

- **2.2 new loras currently only work for T2V**
  - The new ones for 2.2 are T2V only, 2.1 ones kind of work for I2V
  - *From: Immac*

- **Lightning lora changes faces and brightness**
  - Makes videos brighter than wanted and changes faces
  - *From: screwfunk*

- **Lightning lora bad at cfg distillation**
  - Seems pretty bad at cfg distillation, doesn't work well with very low cfg
  - *From: Kijai*

- **5B model turns everything into humans**
  - Anything other than a human gets turned into a human
  - *From: Rainsmellsnice*

- **Context windows work poorly with I2V**
  - Sliding context doesn't work well with I2V workflows
  - *From: Kijai*

- **VAE grid stepping artifacts**
  - When characters with hair move, VAE creates weird grid stepping because it cannot render motion smoothly
  - *From: aikitoria*

- **Lightning LoRA fails on complex prompts**
  - Works fine for simple prompts but falls apart on complex scenarios that base Wan 2.2 handles
  - *From: Kijai*

- **Character LoRAs tend to stifle motion**
  - Character LoRAs reduce motion quality, creating a trade-off between character consistency and animation
  - *From: screwfunk*

- **Going through doors is difficult**
  - The model struggles with generating characters moving through doorways
  - *From: kendrick*

- **Masking with WanVideo Encode didn't work**
  - User reported that masking rendered from Blender didn't function properly with WanVideo Encode
  - *From: xwsswww*

- **No true 2.2 VACE support**
  - Most VACE modes either are super weak or don't work at all with the high noise model
  - *From: Kijai*

- **Frame interpolation doesn't work well with Wan**
  - Attempted frame interpolation using all frames to double FPS but results weren't great
  - *From: Kijai*

- **Lightning kills motion significantly**
  - Lightning LoRAs reduce motion so much that lower strength + CFG feels better, quickly reaching point where lightx2v is better
  - *From: Kijai*

- **WAN 2.2 lightning LoRAs are not great**
  - Current lightning LoRAs for 2.2 don't work as well as older LightX2V LoRAs
  - *From: Kijai*

- **Hard to avoid offloading with 2.2 14B model**
  - Model is too large to fit entirely in VRAM on most consumer cards
  - *From: Kijai*

- **Context windowing slows generation significantly**
  - Multiple sampling per step creates unavoidable slowdown for longer sequences
  - *From: Kijai*

- **[CUT] prompt doesn't work reliably**
  - Sometimes just displays text [CUT] on screen instead of creating scene transitions
  - *From: FancyJustice*

- **Wan 2.2 heavily biased toward realism**
  - Very difficult to get stylized art - wasn't trained on stylized art at all
  - *From: Fill*

- **Context windows don't work well with I2V**
  - I2V models need image input in each window, causing snapping or full T2V behavior
  - *From: Kijai*

- **90+ frames causes looping and quality degradation**
  - Generating more than 81 frames generally works poorly with visual quality issues
  - *From: Kijai*

- **Bong_tangent scheduler not good for low steps**
  - Not recommended for <20 steps, especially not for Wan 2.2. Beta is best for <10 steps
  - *From: Ablejones*

- **Cannot properly generate 5 seconds at 24fps beyond 81 frames**
  - Model has difficulty with longer generations
  - *From: Kijai*

- **5B model has issues at large resolutions like 1920x1080**
  - Hallucinates more than Kontext/Krea at large resolutions
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Character consistency not perfect without training**
  - Even with reference techniques, character retention is imperfect
  - *From: Juampab12*

- **VACE doesn't work properly with Wan 2.2**
  - Due to different patch_embedding architecture in high noise model
  - *From: Kijai*

- **Wan2.1 VACE quality degrades significantly for longer generations**
  - Style transfer quality drops heavily when going from 20 to 60 frames
  - *From: Poppi*

- **2.2 speed LoRAs performance**
  - Not better than old LightX2V, can cause bleached/burned appearance
  - *From: Kijai*

- **EchoShot implementation unreliable**
  - Often doesn't trigger, panda prompt won't work with their method
  - *From: Kijai*

- **VACE blocks don't work with 2.2 HN model**
  - Need to merge 2.1 patch embedding and block 0 to get reference following
  - *From: Kijai*

- **Camera prompting difficult with I2V**
  - Camera movement prompting is challenging to control with image-to-video
  - *From: N0NSens*

- **Motion loops back after 81 frames**
  - Model trained on 81 frames, longer sequences may repeat or undo previous actions
  - *From: Hoernchen*

- **Poor performance at higher resolutions without proper settings**
  - Higher resolutions like 1280x720 need increased CFG and steps
  - *From: Mngbg*

- **5B model requires more effort**
  - 5B model needs more careful prompting and parameter tuning compared to 14B
  - *From: DawnII*

- **Speed LoRAs significantly change model style**
  - Lightning and LightX have colossal effect on image style, LightX makes everything anime-like
  - *From: Дмитрий Марков*

- **2.1 LoRAs cause poor temporal continuity on 2.2**
  - Jerky frames and strange generations when using 2.1 trained LoRAs on 2.2 models
  - *From: mamad8*

- **FP8 requires newer GPU architecture**
  - 3000 series lacks native fp8 support, needs at least 4000 series. A5000 is compute 8.6 but needs 8.9
  - *From: Lodis*

- **Wan 2.2 Lightning LoRA quality**
  - Performs worse than 2.1 LightX2V, limited to specific 4-step setup usecase
  - *From: Kijai*

- **Frame count affects style consistency**
  - Different frame counts produce different styles - fewer frames tend toward comic/anime, more frames toward realism
  - *From: Дмитрий Марков*

- **USDU upscaling background seams**
  - While it fixes hands and hair details, it creates seams in backgrounds that need more tile blending
  - *From: Persoon*

- **Add noise LoRA only works in Low Noise model**
  - LoRA effects only appear in LN model, not in HN model
  - *From: piscesbody*

- **Lightning LoRAs cannot generate dark/night scenes**
  - Force daylight scenes, break on dark prompts, likely due to dataset limitations
  - *From: Kijai*

- **New LoRAs have compatibility issues with GGUF quants**
  - Don't work as well with quantized models, need more steps
  - *From: Josiah*

- **Scene teleportation inconsistency**
  - Characters sometimes only appear on one side of scene, requires specific prompting techniques
  - *From: FancyJustice*

- **New I2V LoRA redraws first frame more than old T2V version**
  - Less preservation of input image compared to using T2V LoRA for I2V
  - *From: N0NSens*

- **Lightning LoRAs completely destroy lighting capabilities**
  - No dark scenes, always full bright, can't make scenes with dim lights
  - *From: Critorio*

- **Small context windows in MultiTalk don't work**
  - With small windows like 25 frames, can't create many new frames per iteration and may not finish
  - *From: Kijai*

- **MultiTalk quality degradation with too many windows**
  - Image quality degrades based on number of windows, not video length
  - *From: Kijai*

- **RadialAttention changes input image in I2V**
  - Strays too far from source image making it useless for I2V
  - *From: N0NSens*

- **Going over 81 frames affects prompt adherence and motion**
  - Longer videos may have reduced prompt following and motion quality
  - *From: MysteryShack*

- **Lightning LoRA prompt adherence issues**
  - Low noise model affects prompt adherence, doesn't work well with complex or weird prompts
  - *From: MysteryShack*

- **Latent composite masked doesn't support video**
  - Only works for images, not video latents
  - *From: xwsswww*

- **Lightning quality issues with v1.1**
  - Lightning 1.1 version appears to have worse quality than previous versions
  - *From: MysteryShack*

- **Fun Control model size**
  - Very large file size making disk space management difficult
  - *From: xwsswww*

- **Fun Control limited to 4 seconds maximum**
  - Unlike VACE which can go longer with sufficient VRAM
  - *From: Draken*

- **Lightning LoRAs force bright daytime aesthetic**
  - Cannot easily achieve dark or night scenes even with strong negative prompting
  - *From: Ablejones*

- **VAE cannot be chunked without seams**
  - Temporal VAE must process full sequence, causing memory issues with long videos
  - *From: Kijai*

- **MultiTalk trained with Chinese wav2vec**
  - Other wav2vec models don't work - they don't sync to audio at all
  - *From: Kijai*

- **MultiTalk lip sync timing issues**
  - Tends to be off-sync for first 2 seconds and last 2 seconds of clips, works well in middle portion
  - *From: hiroP*

- **Reference image quality in WAN 2.2**
  - Reference does not work very well, start image works better
  - *From: DawnII*

- **FP8 quality degradation**
  - FP8 scaling still changes output quality compared to FP16
  - *From: Kijai*

- **VACE control breakdown with long videos**
  - Using VACE first frame with long control video starts breaking down after 100 frames
  - *From: TheSwoosh*

- **Lightning LoRA can't handle black colors properly**
  - This lora can't even do black, changes model aesthetics unlike previous distilled models
  - *From: Kijai*

- **2-step processing through 14B network insufficient**
  - 2 steps through a giant 14B network seems pointless, not enough processing power
  - *From: Draken*

- **Fun Control quality not as good as base model**
  - Quality degrades compared to normal text to video, gets better with fewer high noise steps but never matches base quality
  - *From: Canin17*

- **Lightning LoRA doesn't work well with CFG > 1**
  - Actively detrimental when CFG is higher than 1
  - *From: Canin17*

- **Wan2.2 lightning LoRAs have style bias**
  - Not well trained and introduce unwanted style changes, better to use LightX LoRAs or mix
  - *From: Kijai*

- **I2V sometimes doesn't follow reference image**
  - May only pick up color scheme or specific elements like smoke, inconsistent adherence to reference
  - *From: VK (5080 128gb)*

- **Fun models consistently lower quality**
  - Lack compute and dataset resources to match original model quality across all releases
  - *From: aikitoria*

- **FP8 memory leak with LoRA changes**
  - Changing LoRAs or porq strength causes 3x VRAM usage increase on subsequent runs without block swap
  - *From: Kijai*

- **Radial attention ruins motion quality**
  - Changes movement for worse, especially problematic on early steps and low step counts
  - *From: N0NSens*

- **Sapiens pose consistency issues**
  - No time consistency, won't handle complex shots with frame drops properly
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Q3 quantized models have poor quality**
  - T2V generations are quite 'artistic' with low quantization
  - *From: Drommer-Kille*

- **Meta's BF16 Sapiens incompatible with modern PyTorch**
  - Shouldn't work for PyTorch > 2.0
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Fire/explosion quality in Wan 2.2**
  - Fire is one thing Wan 2.2 doesn't do particularly well, and 2.1 LoRAs haven't helped much
  - *From: JohnDopamine*

- **VACE color shifting**
  - VACE introduces color shifting issues, especially problematic for temporal inpainting with lightx2v generated videos
  - *From: daking999*

- **Masks don't work properly in Wan 2.2**
  - Masks in WanVideo Encode act more like control net or attention masks rather than true masks for i2v/t2v
  - *From: xwsswww*

- **Wan 2.2 wrapper doesn't fully follow input or change style**
  - V2V with wrapper has limitations compared to Vace for style changes
  - *From: Drommer-Kille*

- **16fps is problematic for film production**
  - 16fps is not a multiple of standard fps rates, creates issues for professional film work requiring 24fps
  - *From: Drommer-Kille*

- **Interpolation fails on fast action**
  - All interpolation methods struggle with kinetic fast-paced action, sword fights, liquid splashing - missing subframe motion information
  - *From: Ruairi Robinson*

- **Wan 2.2 cannot mix 5B and 14B models**
  - Different latent spaces prevent using 5B for first pass and 14B for second pass
  - *From: Kijai*

- **SeedVR2 extremely slow**
  - Can upscale 1080p to 4K but takes couple of days to process
  - *From: Drommer-Kille*

- **Cars keep appearing despite negative prompts**
  - Persistent issue where cars appear in generated videos regardless of prompting strategy
  - *From: Drommer-Kille*

- **Fun 2.2 control model lost reference input**
  - The new Fun 2.2 control model no longer supports reference inputs that worked with Fun 1.1
  - *From: Kijai*

- **Fun 2.2 refuses to work beyond 81 frames**
  - Model won't generate any movement when trying more than 81 frames
  - *From: Kijai*

- **Fun low noise model quality issues**
  - Fun low noise doesn't finish properly, could be LoRA compatibility issue
  - *From: Kijai*

- **Wan doesn't understand object physics**
  - Example: doesn't understand when skateboard is upside down
  - *From: Drommer-Kille*

- **Point editor lacks relative scaling**
  - Editor shows images at original size, sucks on large images due to no relative scaling
  - *From: Kijai*

- **2.2 Lightning LoRA has severe style bias**
  - Makes everything bright and oversaturated, especially bad for dark scenes, changes clothing inappropriately
  - *From: Kijai*

- **14B model cannot do 1080p while 5B can**
  - Counterintuitive limitation of larger model
  - *From: QuintForms*

- **121 frame looping issue in 2.2**
  - Without Skyreels LoRA, subjects won't leave frame properly in longer generations
  - *From: Kijai*

- **Fun 2.2 cannot finish at good quality**
  - Needs additional sampler without Fun at end for proper quality
  - *From: Kijai*

- **14B 2.2 is not 24fps like 5B**
  - Easily seen when trying I2V for 121 frames
  - *From: Kijai*

- **MultiTalk resolution limit**
  - Can't use 1280x720, only works at lower resolutions like 832x480 on 5090
  - *From: NebSH*

- **2.2 I2V loops at 121 frames**
  - Model tends to loop content at 121 frame length
  - *From: Kijai*

- **Skyreels LoRA may affect 2.2 motion quality**
  - Probably has negative effect on the 2.2 motion, but still better than plain 2.2 on 121 frames
  - *From: Kijai*

- **Karras/exponential doesn't work with flowmatch**
  - It's just opposite of what it should be with flowmatch models
  - *From: Kijai*

- **Latent upscale quality**
  - Latent upscale is terrible quality
  - *From: Kijai*

- **No native VACE for Wan 2.2**
  - Have to wait for official VACE for Wan 2.2
  - *From: AmirKerr*

- **Skyreels LoRA breaks looping in T2V**
  - Requires increased strength but disrupts 121 frame loop functionality
  - *From: Kijai*

- **LightX2V LoRA changes faces in I2V**
  - Tends to change the face of the subject when used with Wan 2.2
  - *From: RRR*

- **Upscaling without training is poor quality**
  - Always gonna be terrible without training model for it
  - *From: Kijai*

- **Higher resolutions cause slow motion**
  - At higher resolutions there is less motion or slow motion effects
  - *From: SonidosEnArmonía*

- **GGUF models don't work with batch size > 1**
  - Problem with GGUF is batch size limitation, works with batch 1 but takes longer for videos
  - *From: Alisson Pereira*

- **Wan 2.2 doesn't have VACE equivalent**
  - No official VACE release for 2.2, only experimental workflows with merged models and hacks
  - *From: Josiah*

- **Background faces mutate due to insufficient resolution**
  - Model doesn't have enough pixel space for stable results in backgrounds, needs 1152p+ resolution
  - *From: Juan Gea*

- **SeedVR adds inter-frame flicker**
  - SeedVR upscaling introduces temporal inconsistency, needs better temporal addon
  - *From: HeadOfOliver*

- **Torch compile first run takes more VRAM on Windows**
  - Weird issue with compile in Windows - first run uses more VRAM, doesn't happen in Linux
  - *From: Kijai*

- **ComfyUI LoRA extraction doesn't do 5D tensors**
  - Probably only extracts patch embed, not full model differences
  - *From: Kijai*

- **Stand-in LoRA has limited effect on Wan 2.2 high noise**
  - Doesn't work well with high noise settings in 2.2
  - *From: Kijai*

- **Stand-in not working well with whole body references**
  - Examples show whole body but couldn't get it to work in practice
  - *From: Kijai*

- **Motion vs likeness trade-off**
  - More motion results in less likeness and vice versa
  - *From: Instability01*

- **Less motion at higher resolutions**
  - Above 900x900 tends to produce less motion in videos
  - *From: Instability01*

- **Stand-in causing videos to match reference too closely in last frame**
  - Not very versatile/flexible, tends to revert to reference appearance
  - *From: Juampab12*

- **Stand-in model doesn't work with Wan 2.2 LOW**
  - Compatibility issue specifically with the LOW noise model in 2.2
  - *From: Hevi*

- **Wan 2.2 5B has artifacts in video output**
  - Quality issues reported with the 5B model
  - *From: army*

- **LightX2V has aesthetic issues**
  - Team acknowledged aesthetic problems with current Lightning LoRA
  - *From: DawnII*

- **Multitalk incredibly slow for full potential usage**
  - Performance limitation prevents full utilization of multitalk capabilities
  - *From: Kijai*

- **Context windows can cause ghosting and instability**
  - Without proper camera control, context windows produce poor blending
  - *From: Juan Gea*

- **LightX2V motion issues with Wan 2.2**
  - Current LightX2V distillation has acknowledged motion problems with Wan 2.2, team working on better solution
  - *From: Kijai*

- **Wan 2.2 Fun Control lacks reference image support**
  - Unlike Fun 2.1 v1.1, the 2.2 version doesn't support reference images in the wrapper
  - *From: Kijai*

- **Particle simulations don't work well**
  - AI ignores particles in simulations, even with full model unlikely to change
  - *From: Gill Bastar*

- **Combining StandIn and VACE reference breaks generation**
  - Using both controls together with same reference causes issues
  - *From: Hashu*

- **StandIn gets worse at higher resolutions**
  - Performance degrades when increasing resolution beyond certain point
  - *From: Hashu*

- **FantasyPortrait struggles with anime eyes and extreme driving videos**
  - Model has difficulty with certain art styles and extreme facial expressions
  - *From: Kijai*

- **Stand-In works better with single person prompts**
  - Multiple people in prompts causes confusion and reduces likeness quality
  - *From: mdkb*

- **Wan 2.2 struggles with complex camera movements on certain images**
  - Model unable to handle specific camera movement requests like circular tracking shots for some image types
  - *From: 伊熙尔杜的克星*

- **VACE can't do lip sync, only expressions**
  - VACE can handle expressions and pose control but not lip synchronization
  - *From: mdkb*

- **fp8 scaled Fun 2.2 control models don't work for reference**
  - The ref_conv layer in fp8 causes silent failures for reference functionality
  - *From: Kijai*

- **Context windows work poorly with start image**
  - Context windows work better with reference image than start image for I2V
  - *From: Kijai*

- **GGUF doesn't allow LoRA merging**
  - Must use LoRAs unmerged which uses more VRAM and slows down generation
  - *From: Kijai*

- **720p cannot generate small faces properly**
  - Higher resolution needed for detailed facial features
  - *From: Drommer-Kille*

- **Stand-in attention masking may be very slow with SageAttention**
  - SageAttention doesn't support attention masking used by stand-in
  - *From: Kijai*

- **Fun InP sliding timestep window doesn't work with released 5B weights**
  - Theory is correct but implementation doesn't work in practice with current weights
  - *From: Kijai*

- **MultiTalk doesn't work well with Wan 2.2**
  - Works well with 2.1 but compatibility issues with 2.2
  - *From: Kijai*

- **MultiTalk requires more than 8GB VRAM**
  - Cannot run on 8GB VRAM systems
  - *From: xwsswww*

- **Wan 2.2 Lightning LoRAs destroy motion quality**
  - Barely any motion despite being faster with 4 steps
  - *From: Lodis*

- **Fun Control Camera GGUF has compatibility issues**
  - Tensor type mismatches and gradient errors
  - *From: Kijai*

- **2.1 LoRAs on 2.2 cause camera movement**
  - Results work but camera may move away from intended position
  - *From: Mngbg*

- **Wan 2.2 High noise tends towards slow motion**
  - At 81 frames sometimes produces slow motion effects
  - *From: Ablejones*

- **Fun 2.2 trajectory control doesn't work with reference input**
  - Only works when using start image input
  - *From: Kijai*

- **More than 81 frames usually causes color fading**
  - Light color fading occurs after a few frames in longer generations
  - *From: Kijai*

- **Fun InP model extension makes first half too static**
  - When placing image in middle of video, first half remains almost static
  - *From: Kijai*

- **Fun Control model reference only in Control model**
  - Reference input not available in InP or Control-Camera models
  - *From: Kijai*

- **RTX 3090 cannot use native 2.2 reliably**
  - User literally cannot use native 2.2 on RTX 3090, wrapper crashes but can work
  - *From: ˗ˏˋ⚡ˎˊ-*

- **fp8e4nv not supported on RTX 3090 architecture**
  - Must use e5m2 quantization instead for torch.compile compatibility
  - *From: Kijai*

- **WanVideoSampler extremely slow without block swap**
  - Saturates VRAM fully and uses shared VRAM which barely runs
  - *From: Kijai*

- **VACE + Phantom model integration issues**
  - Can completely mess up the image, suspect both VACE and Phantom being baked in causes handling differences
  - *From: Nekodificador*

- **Native nodes cause frequent recompilation**
  - Recompiles even when just changing prompt, not optimal performance
  - *From: Kijai*

- **MMaudio limited to 5-8 second videos**
  - Not suitable for talking people, mainly for sound effects
  - *From: . Not Really Human .*

- **700px limit for Wan 2.2 with block swap**
  - 1000px takes very long time on WanVideo Sampler
  - *From: xwsswww*

- **Wan 2.2 transitions happen too late in video**
  - Changes occur closer to end rather than smooth transitions throughout duration
  - *From: dir2050*

- **Color shifting when saving videos**
  - Videos don't preserve true colors when saved, affects both native nodes and video suite
  - *From: SonidosEnArmonía*

- **Noisy pattern in Wan 2.2 Fun variant**
  - Persistent noise even with full steps, may require base 2.2 low noise instead
  - *From: 𝕯𝖗. 𝕸𝖆𝖈𝖆𝖇𝖗𝖊 ☠*

- **Context windows implementation still early**
  - Manual nodes only, may have errors with longer sequences
  - *From: Lodis*

- **VACE modules don't work with GGUF files**
  - Cannot use VACE with Phantom GGUF, no way to include it in workflow as VACE modules don't work with GGUF files
  - *From: mdkb*

- **Context transitions not smooth in Wan 2.2**
  - Flow between context slots always restarts from first frame, unlike AnimateDiff which was smooth
  - *From: xwsswww*

- **Lightning lora prompt adherence poor**
  - Lightning lora doesn't listen to directional prompts like 'turns head right, then left' while lightx2v technically works
  - *From: MysteryShack*

- **Fantasy Portrait stuttering with open mouth**
  - Fantasy Portrait creates involuntary movements and stuttering when source mouth stays open for extended periods
  - *From: smithyIAN - 4080ti Super 16gig*

- **WanFM requires end frame**
  - The whole point of Frame Morphing is to morph from start to end frame, can't work with just start frame
  - *From: Kijai*

- **VACE and Phantom don't support GGUF**
  - Can't plug non-GGUF VACE module into Phantom GGUF model
  - *From: mdkb*

- **Latent extraction for video continuation doesn't work**
  - First frame encoding is handled differently, causes flash effect when using full latents
  - *From: Kijai*

- **Endless generation has poor motion quality**
  - While it can go endlessly, motion quality degrades significantly, making it impractical
  - *From: Kijai*

- **Wan 2.2 lacks dynamics with single image input**
  - When using same image as first and last frame, output may lack dynamics compared to 2.1
  - *From: ezMan*

- **MultiTalk quality degrades over longer generations**
  - Quality starts degrading before 1000 frames, 1000 frame limit exists for quality reasons
  - *From: seitanism*

- **Phantom difficult to use with other models**
  - Combining Phantom with VACE can cause character consistency issues, nasty flashes and artifacts because VACE's referencing might override Phantom's
  - *From: mdkb*

- **Fighting scenes don't work well in Wan**
  - Wan avoids actual fist connections in fighting sequences
  - *From: mdkb*

- **Can't combine Phantom and MultiTalk embeds**
  - Each has their own embeds node feeding into same image_embeds input, no clear way to combine them
  - *From: seitanism*

- **Wan2.2 random particle/snow blips in low noise mode**
  - Weird particle or snow blips happen randomly in low noise mode, making it unreliable
  - *From: MysteryShack*

- **VACE single image doesn't work with native nodes**
  - Only works with wrapper implementation
  - *From: Nekodificador*

- **Context windows don't work well with I2V models**
  - Every window needs start image, causing consistency issues
  - *From: Kijai*

- **VACE control doesn't follow well for single image**
  - Doesn't follow control effectively with just one image
  - *From: Kijai*

- **Fast motions don't work well with last frame context approach**
  - Jank between moving into next batch
  - *From: xwsswww*

- **People appear too wide/thin at 720p and other resolutions**
  - Possibly caused by 2.1 LoRAs not adapting properly to 2.2
  - *From: Fawks*

- **Fantasy Portrait doesn't support video input natively**
  - Only accepts image input, requires workaround with frame extraction for video-to-video
  - *From: VRGameDevGirl84(RTX 5090)*

- **Fantasy Portrait arms don't move**
  - Only face/mouth animation, arms remain static unless positioned in end frame
  - *From: Drommer-Kille*

- **Video LoRA training struggles with outfit variations**
  - Video-only datasets insufficient for outfit diversity, needs mixed image/video training data
  - *From: Ryzen*

- **Wan 2.2 tends to over-generate talking people**
  - Model bias toward generating people with open mouths/talking poses
  - *From: Lodis*

- **VACE cannot work with I2V models**
  - VACE is specifically an addon for T2V models and cannot be used with I2V models unless someone retrains the whole system
  - *From: Kijai*

- **High noise extraction from 2.2 not reliable**
  - People have tried to extract 2.2 as a LoRA but results are mixed at best, no reliable way to incorporate high noise yet
  - *From: DawnII*

- **AI video clips are 8-bit and fail Netflix QA**
  - 8-bit AI clips cannot pass automatic QA process for Netflix, faking 10-bit by adding noise may still result in rejection
  - *From: Drommer-Kille*

- **Context window creates fade in/out at 5 seconds**
  - With static_standard and 6 steps, creates fade effect combining two separate clips rather than following first clip
  - *From: Lodis*

- **No Wan 2.2 MAGREF model exists yet**
  - Only 2.1 MAGREF available, workflows showing 2.2 contain typos
  - *From: Kijai*

- **MTV Crafter hardcoded to 49 frames**
  - Cannot generate 81 frame outputs
  - *From: Kijai*

- **Context window degrades over time**
  - Current method degrades with longer generations, InfiniteTalk should fix this
  - *From: Kijai*

- **Scene cuts difficult to achieve**
  - Hard to maintain causal consistency between separate generations
  - *From: Ablejones*

- **T2V tends to be repetitive without wildcards**
  - Single prompt produces repetitive output in long context
  - *From: Kijai*

- **Wan 2.2 avoids striking/combat actions**
  - Model has restrictions with prompting for striking, likely a T5 issue, needs very specific prompts
  - *From: Ablejones*

- **MTV Crafter limited to 49 frames**
  - Training limitation prevents longer generations, examples don't exceed 49 frames
  - *From: Kijai*

- **Fun Control 14B can't do hard poses**
  - Model struggles with difficult pose requirements
  - *From: Kijai*

- **I2V plain generation generally just loops**
  - Without proper techniques, I2V tends to produce looping content
  - *From: Kijai*

- **Wan 2.2 I2V doesn't support inbetween frames**
  - Can only use first and last frames, not intermediate keyframes
  - *From: xwsswww*

- **Fun Control models are 30GB**
  - Too large for some users to download and use
  - *From: mdkb*

- **VACE for 5B model not available yet**
  - Only base 5B model available, which has quality issues
  - *From: Lodis*

- **InfiniteTalk video-to-video not properly implemented yet**
  - Glitchy results when trying v2v, needs proper developer implementation
  - *From: JohnDopamine*

- **InfiniteTalk fork conflicts with main wrapper**
  - Cannot install both MeiGen-AI fork and KJ's wrapper simultaneously
  - *From: Kijai*

- **F5-TTS language limitations**
  - Only handles 2 languages well, French doesn't work, has catastrophic forgetting
  - *From: MysteryShack*

- **Qwen Image Edit makes things plastic looking**
  - Initial tests show plastic appearance, may need sampler experimentation
  - *From: Lodis*

- **VACE with multiple people identity issues**
  - Difficulty maintaining likeness of 3 people simultaneously
  - *From: mdkb*

- **Hand hallucinations in InfiniteTalk**
  - Model tends to generate incorrect hand movements and positions
  - *From: Kijai*

- **Green screen effect with MAGREF**
  - Characters do not blend well with background when using MAGREF
  - *From: Hevi*

- **Transition artifacts in high motion**
  - InfiniteTalk transition between windows becomes apparent with more motion
  - *From: DawnII*

- **Image degradation over time**
  - Progressive blurriness and quality loss in longer generations
  - *From: multiple users*

- **8GB VRAM insufficient for most InfiniteTalk workflows**
  - 3070 8GB struggles even with Q6 model and blockswap, needs very low resolution and RAM
  - *From: seitanism*

- **Extra frames generated beyond audio length**
  - InfiniteTalk generates extra frames causing sync issues when audio is shorter than video
  - *From: BobbyD4AI*

- **Lip movement continues after audio ends**
  - Model continues lip movement during silence periods at end of audio clips
  - *From: Tony(5090)*

- **Q8 I2V model compatibility issues**
  - Some Q8 I2V models not compatible, getting 'blocks.0.cross_attn.ip_adapter_single_stream_k_proj.weight' errors
  - *From: ˗ˏˋ⚡ˎˊ-*

- **InfiniteTalk V2V is not true V2V**
  - Uses keyframing every 72 frames rather than processing full video continuously
  - *From: DawnII*

- **No proper distill for Wan 2.2 yet**
  - Speed LoRAs like LightX2V work but no proper distilled version available
  - *From: Kijai*

- **VACE doesn't follow text prompts well**
  - Better to grab motion with I2V workflow rather than relying on VACE text prompts
  - *From: Piblarg*

- **Context options don't work well with InfiniteTalk**
  - User couldn't make context work properly, always produced strange results
  - *From: mamad8*

- **Speed LoRAs kill quality on high noise side**
  - Low noise side can use them freely, but high noise side needs careful application to avoid ruining motion
  - *From: Kijai*

- **No prompt word scheduling support**
  - Cannot change prompts every N frames like some users want
  - *From: 1081570872994824212*

- **InfiniteTalk not officially supported on Wan 2.2**
  - It's very much made for 2.1, you can brute force whatever but it's not officially supported
  - *From: Kijai*

- **No CLIP vision model works with Wan 2.2**
  - When asked about CLIP vision compatibility with Wan 2.2, response was 'None for 2.2'
  - *From: Kijai*

- **Model not meant for 5 second videos**
  - The whole model and multitalk node are not designed for short 5 second videos
  - *From: Kijai*

- **LightX2V LoRA causes static faces**
  - Using LightX2V LoRA results in very static faces with limited movement
  - *From: seitanism*

- **InfiniteTalk doesn't support start and end images**
  - Designed for continuous generation with context windows, not short clips with defined endpoints
  - *From: seitanism*

- **InfiniteTalk V2V not fully implemented**
  - Current code branch doesn't handle start/end frames or proper v2v functionality
  - *From: MysteryShack*

- **Wan models not good for long detailed prompts**
  - Designed for simple prompts, not for complex detailed descriptions
  - *From: NC17z*

- **Upscaling reduces expression and emotion**
  - Multiple denoising passes with low model loses expressions and magic of high model
  - *From: mamad8*

- **FusionX LoRA issues with long videos**
  - Exacerbates color shift over 1 minute and reduces ID preservation in videos
  - *From: NC17z*

- **I2V color shifts beyond 1 minute**
  - Color shifts become more pronounced in I2V generation beyond 1 minute
  - *From: NC17z*

- **InfiniteTalk speed**
  - Takes significantly longer to render compared to MultiTalk, especially for 30-second 480x480 clips
  - *From: NC17z*

- **Qwen Edit detail loss**
  - Easily loses details from source image that Kontext rarely loses
  - *From: Drommer-Kille*

- **5B model VAE is slow despite fast generation**
  - The 5B model generates quickly but VAE processing remains slow, converting to fp8 won't help much as VAE weights aren't large
  - *From: hicho*

- **Wan latents don't like when you cut the first frame off**
  - Trimming first frames from Wan latents can cause issues, making skip latent parameter less useful than expected
  - *From: Kijai*

- **V2V as noise not implemented in InfiniteTalk loop**
  - Video-to-video with noise/denoise functionality is not implemented in the loop method and wouldn't obey denoise settings anyway
  - *From: Kijai*

- **GGUF and non-GGUF models cannot be mixed**
  - Must use matching format for InfiniteTalk and base Wan models
  - *From: Kijai*

- **Background changes too much without masking in InfiniteTalk**
  - Need to crop head and paste back for clean results
  - *From: Kijai*

- **Lumen is text-conditioned only**
  - 1.3B model only currently available
  - *From: Kijai*

- **InfiniteTalk doesn't work properly with Wan 2.2**
  - Not trained for 2.2, functional but not optimal
  - *From: DawnII*

- **GGUF models don't allow merging LoRAs**
  - Cannot merge LoRAs when using GGUF quantized models
  - *From: Kijai*

- **Wan doesn't work well with every different frame count**
  - Model input size changes affect performance
  - *From: Kijai*

- **Vid2vid denoises whole video**
  - Unlike approaches like latentsync, entire video gets denoised causing background changes
  - *From: DawnII*

- **Majority of samplers are cursed for InfiniteTalk**
  - Many samplers don't work well with InfiniteTalk
  - *From: MysteryShack*

- **Fun-InP model is temporal inpainting only**
  - Not spatial inpainting like VACE, only works on first to last frame transitions
  - *From: Kijai*

- **Differential diffusion works poorly for low frame counts**
  - Reason unclear but consistent issue with low frame count videos
  - *From: Kijai*

- **Can't do proper I2V chaining with noisy input**
  - Must finish previous window sampling before using as input for next I2V window
  - *From: Kijai*

- **Normal map control in VACE causes color bleeding**
  - Makes normal map control unusable due to heavy color bleeding into other areas
  - *From: Blink*

- **Context windows work poorly with I2V**
  - Each window uses input image as starting point, works better with MAGREF as reference
  - *From: Mattis*

- **VACE doesn't handle blurred masks properly**
  - Only diff diff part would work with blurred masks, binary masks recommended
  - *From: Kijai*

- **Cannot separate reference and control scheduling in single VACE encode**
  - Not possible to schedule reference differently from control in single encode
  - *From: Kijai*

- **VACE better for inpainting existing subjects than adding new ones**
  - Works well where subject already exists, not good for adding subjects where they don't exist
  - *From: Dream Making*

- **InfiniteTalk looping doesn't work with T2V**
  - The model works with T2V but the looping sampling method does not
  - *From: Kijai*

- **Fantasy Portrait fails when no face detected**
  - Skips frames without detected faces, can cause processing to fail entirely
  - *From: fredbliss*

- **Infinitetalk doesn't work well on high noise model**
  - Gets good prompt adherence but quality suffers significantly
  - *From: MysteryShack*

- **I2V can't do proper pull-focus or pan to person**
  - Starting with image makes these camera techniques very difficult
  - *From: Drommer-Kille*

- **WAN 2.1 LoRAs compatibility with WAN 2.2 variable**
  - Most work on low noise, high noise can be variable and may need strength adjustment
  - *From: DawnII*

- **Lightning LoRA is censored**
  - Provides better prompt adherence but censors content and reduces character consistency
  - *From: MysteryShack*

- **Large workflow metadata can crash Windows Explorer**
  - Workflows over 200KB+ metadata can cause system crashes when viewing files
  - *From: Ashtar*

- **CineScale requires high VRAM for 4K generation**
  - Runs at full 4K resolution without tiling, not practical for consumer GPUs
  - *From: Kijai*

- **Models work worse outside intended frame count**
  - Phantom designed for 121 frames, performance degrades significantly at lower frame counts
  - *From: Kijai*

- **UniAnimate incompatible with GGUF models**
  - UniAnimate LoRA won't work with GGUF format models
  - *From: Kijai*

- **High resolution generation causes artifacts**
  - At 1080p and above, models produce extra heads and elongated limbs similar to SD1.5 issues
  - *From: ingi // SYSTMS*

- **Changing reference images per frame not easily possible**
  - Would require splitting attention in code, no current setup available for frame-wise reference changes
  - *From: Kijai*

- **T2V rough with 5B turbo**
  - Text-to-video generation is rough with the 5B turbo model, I2V works better
  - *From: Kijai*

- **GGUF can't merge loras**
  - More loras you add, more overhead since GGUF can't merge loras unlike other formats
  - *From: Kijai*

- **Cinescale VAE has no temporal coherency**
  - Can't use it for more than 1 frame as it has no temporal coherency
  - *From: Kijai*

- **Context windows don't work properly with Wan 2.2**
  - Context windows not intended to work on 2.2 model at least for now
  - *From: Mngbg*

- **Film grain node can't process 800+ frame videos**
  - Throws OOM errors when trying to process very long videos
  - *From: Kenk*

- **Bidirectional sampling causes OOM even on high-end GPUs**
  - Always runs into OOM errors even at low resolutions on RTX 5090
  - *From: Roman_S*

- **Wan 2.2 has ping pong effect after 81 frames**
  - Video tries to revert back toward original input image after 81 frames
  - *From: JohnDopamine*

- **LightX2V LoRA doesn't work properly at 4K**
  - LoRA has limitations when used at 4K resolution
  - *From: Instability01*

- **WAN 2.2 5B Turbo T2V poor performance**
  - Couldn't get much quality out of the Turbo 5B T2V model
  - *From: Kijai*

- **Lightning LoRA works poorly on high noise model**
  - Works fine on low noise though
  - *From: Kijai*

- **Context windows make 2.2 unusable for some**
  - Almost 3x the rendering time, described as 'like rendering 2 videos at the same time'
  - *From: DawnII*

- **Speed LoRAs incompatible with high noise model**
  - LightX2V and other speedup loras don't work with high noise unless specifically trained for it
  - *From: MysteryShack*

- **Color degradation with Wan 2.2**
  - Washed out colors compared to 2.1, especially noticeable in multitalk workflows
  - *From: Kenk*

- **Wan lacks good image editing capabilities**
  - Insanely good as T2I model but not as good for image editing
  - *From: Dream Making*

- **FantasyPortrait doesn't combine well with InfiniteTalk**
  - Head movements and expressions not being copied properly
  - *From: SonidosEnArmonía*

- **Loop sampling not meant for short videos**
  - Loop sampling method not meant for 81 frame or less generations, same as context windows
  - *From: Kijai*

- **InfiniteTalk doesn't work well with smaller faces**
  - InfiniteTalk alone doesn't always produce best results when face is smaller in frame
  - *From: T2 (RTX6000Pro)*

- **VACE + Phantom overwhelming lower VRAM**
  - VACE introduces too much work for Phantom workflow on 3060, runs like a dog and keels over even with reduced character count
  - *From: mdkb*

- **Context windows don't work with I2V**
  - Only works with T2V generations
  - *From: Kijai*

- **Face detection failures**
  - Fantasy face detector sometimes fails even on seemingly fine images, dependent on underlying face detector
  - *From: Kijai*

- **Color degradation with InfiniteTalk**
  - Colors get washed out when using InfiniteTalk, especially on both high and low samplers
  - *From: N0NSens*

- **African language lip sync not working**
  - Certain languages don't work well with the lip sync models
  - *From: Kenk*

- **16GB RAM insufficient for Wan 2.1 14B**
  - Even with Q4 GGUF, system freezes due to RAM limitations
  - *From: Akumetsu971/Kijai*

- **InfiniteTalk context windows don't work with extensions**
  - Context windows non-functional when using with extend nodes
  - *From: JalenBrunson*

- **InfiniteTalk coherence degrades toward end**
  - Loses coherence near end of extended generations
  - *From: JalenBrunson*

- **LoRA training limitations**
  - Text encoder training not happening, so CLIP output likely does nothing
  - *From: Kijai*

- **VACE underutilized**
  - Many users not taking full advantage of VACE capabilities
  - *From: Nekodificador*

- **VACE struggles with position/angle changes from reference image**
  - Cannot handle replacing characters if reference image is at different angle than target position
  - *From: mdkb*

- **Lightning 2.2 LoRAs don't work well on high noise model**
  - Can't achieve high dynamic results when adding lightning lora to high noise model
  - *From: piscesbody*

- **InfiniteTalk needs new model to work properly with 2.2**
  - Can sort of work already but has very weak effect on the high noise model
  - *From: Kijai*

- **VACE temporal extension causes facial features drift**
  - Faces change and grow makeup in porn-ish overdone way even without porn loras
  - *From: lostintranslation*

- **2.2 Lightning LoRAs don't work well yet**
  - Still a harder problem to solve, took months for 2.1 distill LoRAs
  - *From: Kijai*

- **Infinite Talk causes gradual video degradation in I2V mode**
  - Quality degrades over time, possibly due to the LoRA
  - *From: Дмитрий Марков*

- **Wan 2.2 commercial overlay prompting not available in open source**
  - Text overlay removal and instructions only work in commercial version
  - *From: Дмитрий Марков*

- **VACE 2.1 has ghosting effects and control input mixing with output**
  - Sometimes control input mixed with output result, inconsistent quality
  - *From: Lodis*

- **Lipsync with VACE has drift problems**
  - Can almost nail it but doesn't quite work perfectly, similar issue with fakevace
  - *From: mdkb*

- **Gender role reversal impossible**
  - No AI model can generate woman lifting man, all default to man lifting woman instead
  - *From: seitanism*

- **2.2 + infinite context causes memory issues**
  - Won't work in general with any 2 sampler setup, causes OOM
  - *From: Kijai*

- **New S2V model likely incompatible with other components**
  - Little chance for compatibility with other stuff due to frame pack method
  - *From: Kijai*

- **T2V quality inconsistent with current distill LoRAs**
  - Can get good outputs then next prompt is crap, balance between motion/speed/quality difficult
  - *From: Kijai*

- **Wan 2.2 I2V cannot generate lightning**
  - If there's no lightning in the original image, you can't get lightning to appear in wan 2.2 i2v
  - *From: MysteryShack*

- **S2V model produces static results**
  - Tests show just static dolls talking, does little motion on its own
  - *From: ZeusZeus (RTX 4090)*

- **WanFM has VRAM requirements**
  - Causes OOM even on A100 80GB in some configurations
  - *From: Yan*

- **Color shift in long generations**
  - 28-second examples show slight color shift over time (gets more cyan)
  - *From: Screeb*

- **Wan.video refuses to generate without human detected in input**
  - For S2V, requires human detection in input image
  - *From: Juampab12*

- **S2V model heavier on VRAM than 2.2 A14B**
  - Requires more VRAM despite being newer
  - *From: Kijai*

- **Hardcoded FPS values causing confusion**
  - Input fps locked to 50, unclear why this value was chosen
  - *From: Kijai*

- **S2V focused on human speech only**
  - Model's clear intent is humans talking, not general environmental sounds
  - *From: MilesCorban*

- **S2V no long generation method yet**
  - Can do audio gen and ref image but missing long video generation capability
  - *From: Kijai*

- **S2V lower quality than InfiniteTalk**
  - Current S2V implementation produces worse results than InfiniteTalk
  - *From: ArtOfficial*

- **S2V resolution constraints**
  - Specific formula required for resolutions to work, many combinations fail with einops errors
  - *From: patientx*

- **S2V mouth movement looks weird**
  - Mouth generally looks off with S2V and 16fps output feels unnatural
  - *From: Kijai*

- **VACE+Phantom model compatibility**
  - Combined VACE+Phantom GGUF model doesn't work well with WanVideoWrapper or isn't compatible with WAN 2.2
  - *From: xwsswww*

- **S2V framepack implementation incomplete**
  - Framepack implementation is beyond current capabilities and not fully working
  - *From: Kijai*

- **Model has strict resolution auto-selection**
  - The code has strict automatic resolution selection that limits flexibility
  - *From: Kijai*

- **Model has degradation in long generation**
  - these methods always have some degradation when it's constantly encoded and decoded
  - *From: Kijai*

- **S2V has distortions at start**
  - distortions on start are caused by static img to vid, it's because of the extension method, in the original code they just drop the first frames
  - *From: Kijai*

- **Context windows with Fun Control causes errors**
  - When scaling back the end percent below .5, it throws errors. With just 81 frames its fine
  - *From: Guey.KhalaMari*

- **Tongue never moves in lipsync models**
  - One thing I notice with all these lip-sync model is that the tongue never moves. lol Makes it look wierder when you study it
  - *From: Guey.KhalaMari*

- **Start-end frame morphing issues**
  - the video stays the same up until the last frame where it changes to the end image
  - *From: Dream Making*

- **S2V doesn't blink naturally**
  - Character doesn't blink during speech generation
  - *From: Kijai*

- **S2V quality degrades over long videos**
  - Quality bakes and degrades significantly over 800 frames, becoming very bad
  - *From: Kijai*

- **Context window overlap bad for lipsync**
  - The overlap in context windows negatively affects lip synchronization quality
  - *From: Kijai*

- **S2V movement less natural than InfiniteTalk**
  - Character movement appears more stiff and less natural compared to InfiniteTalk
  - *From: Rainsmellsnice, Impactframes.*

- **InfiniteTalk color degradation after 1 minute**
  - Starts falling apart at 1 minute, becomes very weird by 2 minutes
  - *From: boorayjenkins*

- **Custom LoRAs need 33+ frames in wrapper but only 5 in native**
  - LoRAs trained on 5 frames don't work with small frame counts in wrapper
  - *From: mamad8*

- **S2V has stop motion/lagging issues**
  - 16fps output creates choppy motion compared to 25fps MultiTalk
  - *From: hicho*

- **VACE color shift issues**
  - Color Match helps but doesn't solve extreme cases, training seepage affects functionality
  - *From: pom*

- **S2V code feels unfinished**
  - Includes lots of unused code, messy implementation compared to other Wan models
  - *From: Kijai*

- **Context windows reduce lipsync quality with framepack**
  - Overlap in framepack method degrades lip sync accuracy
  - *From: Kijai*

- **HunyuanVideo-Foley not significantly better than MMAudio**
  - Similar quality, uses 4-5 models making it complex to implement properly
  - *From: Kijai*

- **PUSA limited diversity**
  - Only finetuned on 4000 videos so diversity is probably limited
  - *From: fredbliss*

- **S2V model poor at T2V generation and motion**
  - Model opposed to motions like walking, video extensions don't follow prompts, speed LoRAs cause blur
  - *From: flo1331*

- **Control signals only work with Fun-Control model**
  - Cannot use control inputs like Canny, Depth, Pose with regular 1.3B or other base models
  - *From: N0NSens*

- **ComfyUI inefficient with long videos**
  - Stores all frames in RAM simultaneously in fp32, making 4K video handling nearly impossible
  - *From: Kijai*

- **S2V model limited motion compared to other lip sync methods**
  - S2V produces stiffer results compared to MAGREF + Multi or InfiniteTalk for lip sync
  - *From: Kijai*

- **Framepack only works with S2V model**
  - Cannot apply framepack context sliding to Wan 2.1/2.2 models as it has its own specific weights
  - *From: Kijai*

- **Action LoRAs don't work with S2V**
  - Motion/action loras won't work with S2V, only style and character loras work
  - *From: Kenk*

- **Infinite Talk works badly on high noise model**
  - Infinite talk works very badly on the high noise model, but works fine on low noise - more like vid2vid
  - *From: Kijai*

- **Index out of bounds error over 100 steps**
  - Getting 'index out of bounds' error when using over 100 steps with Wan and VACE
  - *From: Neex*

- **uni3c affects whole generation**
  - uni3c has effect on whole thing and not only the camera, also kills some motion sometimes
  - *From: N0NSens*

- **uni3c only works with I2V**
  - uni3c doesn't work with T2V, only with I2V for camera control
  - *From: hicho*

- **Framepack degrades over longer generations**
  - Goes bad the longer it goes, need weak settings or careful balance
  - *From: Kijai*

- **Context windows have worse lipsync**
  - Better quality for long gens but lipsync isn't as good as Framepack
  - *From: Kijai*

- **Uni3C only works with I2V**
  - Cannot be used with VACE workflows, only I2V
  - *From: DawnII*

- **AccVid LoRA causes artifacts**
  - Creates overlap artifacts in InfiniteTalk outputs
  - *From: VRGameDevGirl84(RTX 5090)*

- **InfiniteTalk creates noise frames**
  - Makes weird noise frames at head of shot despite better mouth movements
  - *From: T2 (RTX6000Pro)*

- **Context windows ghosting with movement**
  - Can have ghosting transitions with lots of movement or camera movement
  - *From: slmonker(5090D 32GB)*

- **VACE doesn't continue movement**
  - Quality is also really bad for video continuation
  - *From: Drommer-Kille*

- **Context windows increase inference time significantly**
  - All overlap areas have extra computational cost
  - *From: Kijai*

- **S2V severely impacted by distillations**
  - Changes significantly from original with distilled models
  - *From: Ablejones*

- **VACE masks only support binary**
  - Cannot use blurred masks
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Context windows don't work with bridge**
  - Would need a node to combine embeds for bridge compatibility
  - *From: Kijai*

- **I2V works poorly with context windows**
  - Due to training to always reference first frame at beginning of each window
  - *From: Kijai*

- **FantasyPortrait doesn't follow iris well**
  - FP projection doesn't track eye movements accurately
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Wan 2.2 denoises input images**
  - I2V removes grain/noise from input images, trained on high quality material only
  - *From: Lodis*

- **Speed optimizations break Wan 2.2 quality**
  - Any speedup tricks completely destroy quality in 2.2
  - *From: MysteryShack*

- **InfiniteTalk doesn't work with long gen loop**
  - For T2V, InfiniteTalk works for short gens, maybe with context windows for long gens, but doesn't work with the long gen loop
  - *From: Kijai*

- **Beyond 45-81 frames causes quality degradation**
  - When increasing frame number beyond 45 frames, results get really bad with blurred smoke-like diffusion. Max 81 is stable without extension methods
  - *From: ByArlooo/Mu5hr00m_oO*

- **ComfyUI native Latent nodes not compatible with video latents**
  - Most of the ComfyUI native Latent modification nodes are not compatible with video latents, like Crop latent wasn't working because it wasn't considering the frames dimension
  - *From: Ablejones*

- **Context window issues with dynamic camera movements**
  - Context windows work really bad with camera moves. When camera movements are too dynamic, it gets confused when pose isn't long enough
  - *From: Kijai/ArtOfficial*

- **InfiniteTalk affects rest of video beyond face**
  - Need automated way to mask just face/lower face back in, currently labor intensive in After Effects
  - *From: Geoff*

- **Save Image With Alpha might not work with animated sequences**
  - Kijai notes it might not work at all for PNG sequences with alpha channel
  - *From: Kijai*


## Hardware Requirements

- **RAM usage for training**
  - 81GB RAM used for HiDream training batch size 8 at 1024p
  - *From: tarn59*

- **Generation performance**
  - 121 frames 512x512 with LightX2V in 30s, uses 70% RAM caching both High and Low noise models
  - *From: tarn59*

- **VRAM for different model sizes**
  - Q6 quantized models work well at 720x480, takes 2 minutes to generate with 16GB VRAM
  - *From: 1013738790742925343*

- **Memory consumption scaling**
  - User experiencing 27GB->29GB->32GB RAM usage progression leading to system freeze
  - *From: homem desgraca*

- **Storage space for models**
  - User filled 2TB drive in a week with WAN-related models and training
  - *From: Drommer-Kille*

- **VRAM for upscaling**
  - RTX 5090 can handle 1.5x upscaling for 77 frames, 2x possible for 16 frames
  - *From: GOD_IS_A_LIE*

- **Memory management with --cache-none**
  - Using --cache-none flag reduces RAM usage significantly but requires reloading models
  - *From: Kijai*

- **bf16 support for T5**
  - AMD RX 6800 falls back to fp32 when bf16 not supported, making T5 very slow
  - *From: patientx*

- **VRAM for context windows**
  - Context windows don't increase VRAM usage - that's the main benefit of the feature
  - *From: Kijai*

- **AMD ZLUDA performance**
  - AMD Radeon 8060S can run 1280x704 121 frames in 20 minutes with proper setup
  - *From: nacho.money*

- **RTX 5090 native vs wrapper**
  - Native workflows much slower than wrapper on RTX 5090 - 20+ minutes vs 400 seconds for same output
  - *From: IceAero*

- **RAM management options**
  - Can use --cache-none launch option to disable all caching and free RAM completely between model switches
  - *From: Kijai*

- **VRAM for 5B model**
  - RTX 5070 Ti with 128GB RAM can handle I2V at 2.5 minutes for 5x5 steps
  - *From: loopen44*

- **Virtual memory for crashes**
  - Should set virtual memory higher than 64GB unless you have more than 64GB RAM
  - *From: Ablejones*

- **14B model VRAM**
  - Works on systems, maxes out 5090 without headroom during ksampler
  - *From: hicho*

- **L40S performance**
  - 445 seconds for 832x480 generation
  - *From: AJO*

- **5090 performance benchmarks**
  - 30 mins for 5 seconds native 14B at 1280x703, 2-3 mins with wrapper+LightX
  - *From: AJO*

- **4080 12GB performance**
  - 2 minutes max for 5 second videos
  - *From: Lodis*

- **RAM configuration**
  - Z790 boards support up to 256GB DDR5, but speed drops with more RAM. 4x64GB may drop to 5600-5200MHz from rated 6400MHz
  - *From: AJO*

- **RTX 3060 12GB performance**
  - 15 minutes for T2V generation, 9 minutes when models already loaded
  - *From: Abx*

- **Memory management for low VRAM**
  - 32GB swap files, --disable-smart-memory and --cache-none flags help prevent OOM
  - *From: mdkb*

- **AMD 8060S performance**
  - 20 minutes for 7 second video at 640x352, with 64GB dedicated + 32GB shared GPU memory
  - *From: nacho.money*

- **Sage Attention GPU compatibility**
  - Version 2++ requires RTX 30XX and above, minimal benefit on RTX 20XX series
  - *From: mdkb*

- **VRAM management for upscaling**
  - Need block swap at 20 for high-res processing to avoid choking VRAM
  - *From: thaakeno*

- **5B model performance on 3090**
  - Takes 7 minutes for generation, quite slow compared to other models
  - *From: ˗ˏˋ⚡ˎˊ-*

- **30 second generation time**
  - Kijai managing 30-35 second generations, likely on high-end hardware
  - *From: Kijai*

- **H100 performance**
  - 1x H100 can run 25 step generation, SeedVR2 7B brutal even on H100 for 720 to 1080 upscaling with max batch size around 40
  - *From: topmass*

- **3090 VRAM limits**
  - Max resolution 960x656 for 49 frames without blockswap/gguf on 3090
  - *From: daking999*

- **5090 training limitations**
  - Using 320 resolution for low model due to 5090 VRAM constraints
  - *From: mamad8*

- **VRAM for native 1920x1088, 81 frames**
  - 52GB VRAM, 400 seconds render time on RTX 6000 Pro
  - *From: Fill*

- **System RAM usage**
  - Up to 96GB system RAM used with certain configurations, 60GB typical with Wan
  - *From: Fill*

- **Sage attention performance**
  - 2 minutes for full video at 960x720, 5 minutes at 1280x720
  - *From: Ryzen*

- **H100 optimization**
  - Use auto mode for sage attention, fp16 dtype for fast accumulation
  - *From: Kijai*

- **RAM for Wan 2.2**
  - User upgraded to 128GB RAM due to OOM issues, average use around 98GB with full 40 block swap
  - *From: VK*

- **RTX 4090 capabilities**
  - Can run 14B with blockswap, 1920x1080 generation takes 8 minutes
  - *From: Ryzen*

- **AM5 motherboard RAM compatibility**
  - AM5 doesn't like 4 sticks of RAM very much, may need specific configurations
  - *From: phazei*

- **Performance scaling**
  - 640x480 to 704x1280 (3x pixels) took 4x time instead of expected 3x
  - *From: phazei*

- **14B model VRAM usage**
  - 20 block swap uses max 24.916 GB VRAM for 81 frames at 1280x720
  - *From: Kijai*

- **fp16 on 6GB VRAM**
  - 6GB VRAM + 64GB RAM requires increasing virtual memory to avoid disconnection
  - *From: hicho*

- **B200 performance**
  - 25 minutes generation time on B200, slower than expected due to model chunks
  - *From: aikitoria*

- **VRAM for character LoRA training**
  - L40S getting OOM errors, specific requirements unclear
  - *From: Santoshyandhe*

- **Maximum resolution tested**
  - 2560x1536 for 81 frames using 5B model upscaling
  - *From: Juan Gea*

- **3072x1840 resolution achievable**
  - Using 5B model with block swap 30, 30 steps, 16 iterations, 53 seconds per iteration
  - *From: Juan Gea*

- **1280x780 generation time**
  - 1 min 26s on 5090
  - *From: Kijai*

- **Training compute estimate**
  - About $10k run for 14B model training, $20k for both high/low models
  - *From: aikitoria*

- **h1111 generation time**
  - 1 hour with 4090 for generation
  - *From: Benjimon*

- **KJ wrapper performance improvement**
  - Times went down from 125s to 80s for 5s 512x512 gen, using 6 steps vs 4 steps
  - *From: Rainsmellsnice*

- **Cold boot time on Modal**
  - 20 seconds cold boot into UI
  - *From: Karo*

- **Model loading time on network volume**
  - Network volume causes 1-2 minutes billing just for loading model into memory
  - *From: gokuvonlange*

- **RAM usage with LoRA scheduling**
  - 64GB starting to look like minimum rather than comfortable amount. Memory usage varies: 27 blocks with merge, 33-35 without merge
  - *From: Rainsmellsnice*

- **Ampere card compatibility**
  - 3090s and other Ampere cards need e5 fp8 weights or they freak out
  - *From: samhodge*

- **5090 performance with Lightning**
  - 1280x720x81, 4/4 euler, new loras, 262 seconds generation time
  - *From: IceAero*

- **5B model VRAM for reasonable times**
  - Card doesn't have enough VRAM for reasonable generation times with 5B model
  - *From: QANICS🕐*

- **VAE decode performance with 5.5B model**
  - VAE decode takes very long time with the 5.5B model due to large VAE file size
  - *From: cocktailprawn1212*

- **Generation time**
  - 4-step generation in 36.92 seconds, 14 minute gen time for 720x1280
  - *From: TK_999*

- **VRAM usage**
  - 11GB for T5 text encoder when not using cached embeds
  - *From: Doctor Shotgun*

- **FastWan 5B VRAM usage**
  - Can generate 121 frames at 1280x704 in ~34 seconds total (14s sampling + 20s decode)
  - *From: Kijai*

- **High resolution with 5B model**
  - 24GB VRAM with 30 blocks out enables 3072 resolution generation
  - *From: Juan Gea*

- **RTX 5090 performance**
  - Used for multi-prompt iteration batching and fast generation testing
  - *From: Purz*

- **Fast 5B VRAM usage**
  - 6 steps on 1280x704x121 frames uses max 13.043 GB allocated memory, 13.875 GB reserved
  - *From: N0NSens*

- **3060 12GB can run high res**
  - 832x480 done in 8 mins, 1600x960 possible but challenging on 3060 12GB with 32GB system RAM
  - *From: mdkb*

- **3090 performance**
  - 1600x960 resolution takes 10 minutes on 3090 with 64GB RAM
  - *From: SonidosEnArmonía*

- **Compilation time impact**
  - Compiling VAE took almost 2 mins, transformer blocks about 10 seconds first run
  - *From: Kijai*

- **VRAM usage**
  - 720p takes 40 mins, Q5 models give 2GB VRAM headroom vs Q6
  - *From: mdkb*

- **Generation speed**
  - 832x832x81 frames in 4:32 on optimized setup
  - *From: Ada*

- **4090 performance**
  - 337 frames with 8 steps takes ~10 mins on 4090
  - *From: Kijai*

- **FastWan performance**
  - 9 second generation but 20 second decode time
  - *From: Kijai*

- **Upscaling to 1080p VRAM usage**
  - Uses 23.5GB VRAM when upscaling to 1080p with Wan 2.2 14B on L4 GPU
  - *From: thaakeno*

- **Context generation speed**
  - 337 frames generated in 10 minutes on 4090 with lightx2v LoRA
  - *From: kendrick*

- **5B model on 5080**
  - I2V generation time varies significantly based on settings and complexity
  - *From: lomerio*

- **3090 torchcompile compatibility**
  - fp8_e4m3fn hangs on 3090s due to inductor issue, need to use e5 instead
  - *From: Kijai*

- **Storage consumption**
  - ComfyUI folder reached 700GB in 7 days, filled entire 2TB drive
  - *From: Drommer-Kille*

- **24GB VRAM for WAN 2.2 fp8**
  - Can fit 81 frames at 480p without block swap on RTX 4090
  - *From: BobbyD4AI*

- **16GB VRAM VAE optimization**
  - Using 512x384 tile sizes cuts VAE decode time in half on 16GB cards
  - *From: patientx*

- **Torch compile increases disk usage**
  - Compiled models cache to disk but size is negligible compared to model loading time savings
  - *From: Kijai*

- **VRAM for 5B model**
  - Different VRAM requirements due to different latent space compared to other Wan models
  - *From: Kijai*

- **24GB VRAM sufficient for batch generation**
  - Can run batch video generation with 24GB VRAM
  - *From: Gill Bastar*

- **12GB 3060 performance**
  - Can upscale to 1600x900x81 frames in 27 minutes, improvement over previous 49 frame limit
  - *From: mdkb*

- **RTX 4090 VRAM for WAN 2.2 5B**
  - Can run 1280x720 locally, but struggles with higher resolutions
  - *From: Persoon*

- **Mac M4 compatibility issues with 5B**
  - Even with 128GB RAM, OOMs on VAE due to fp32 requirements
  - *From: wwlee.*

- **RTX 3090 confirmed working**
  - With SageAttention, WAN 2.2 Q8 GGUF confirmed working
  - *From: Josiah*

- **VRAM for context window upscaling**
  - High-res 10s video upscaling with Wan 14B requires context windows and is very slow
  - *From: thaakeno*

- **VRAM for extended generations**
  - Can do more than 81 frames with prompt splitting if you have the VRAM
  - *From: Kijai*

- **5090 generation time**
  - 1 min 30s for 5 second video on RTX 5090
  - *From: Kijai*

- **VRAM for VAE precision**
  - FP32 VAE uses twice the memory of FP16, rent 80GB GPU for testing
  - *From: Kijai*

- **High resolution generation**
  - 16GB VRAM can handle 1344x768 at 5 seconds
  - *From: N0NSens*

- **Rife TensorRT performance**
  - 5 seconds for 720p 16->32 frame conversion on RTX 4090, 2 seconds to process 10 seconds of video
  - *From: aipmaster*

- **1600x900x81 generation on 3060 12GB**
  - Achieved with fp8_e5m2, 32GB system RAM, swap file on SSD, --disable-smart-memory. Takes 27 minutes
  - *From: mdkb*

- **1280x614px generation on 4060TI 16GB**
  - 350 seconds render time with 64GB RAM
  - *From: : Not Really Human :.*

- **Memory usage with 128GB RAM**
  - Usually 56% used when generating, upgrade from 64GB for comfort
  - *From: phazei*

- **RAM speed limitations with 4 sticks**
  - Can't use max speed with 4 sticks, had to choose between faster 64GB or regular 128GB
  - *From: kendrick*

- **3000 series GPU compilation**
  - 3000 series NVIDIA GPUs can't use torch.compile with e4m3fn weights
  - *From: Kijai*

- **4K upscaling VRAM**
  - Even with blockswap on 40, 4K upscaling took more than 50GB VRAM
  - *From: thaakeno*

- **RTX 5090 upgrade consideration**
  - User considering 4-5k upgrade from 3090 to 5090 for better performance
  - *From: ˗ˏˋ⚡ˎˊ-*

- **RTX PRO 6000 performance**
  - 1280x720, 81 frames took 2 minutes
  - *From: HeadOfOliver*

- **5090 rental performance**
  - 1024x576 takes 10 minutes, 20 minutes estimated for 1280x720 81 frames due to block swapping
  - *From: MysteryShack*

- **H200 capability**
  - Can do 500 frames at 960x544 without context
  - *From: ˗ˏˋ⚡ˎˊ-*

- **fp16 vs fp8 VRAM usage**
  - fp16 requires more offloading, fp8 is faster due to less offloading needed
  - *From: Kijai*

- **High resolution I2V**
  - 1280x1400p achievable with fp16 and block swap 40
  - *From: xwsswww*

- **High resolution generation**
  - 1536x768 generation completed in 11 minutes using quantized Q5_K_M model
  - *From: : Not Really Human :*

- **Phantom workflow resource usage**
  - Very resource intensive according to user testing
  - *From: samhodge*

- **VRAM optimization**
  - Merge LoRA setting saves VRAM, quantized models help with large resolutions
  - *From: pagan*

- **Fun Control model VRAM**
  - Original model needs 28.6GB, fp8 scaled version needs 14.5GB
  - *From: Kijai*

- **3090 compatibility**
  - Can run fp8 scaled Fun models at 14.5GB
  - *From: Rainsmellsnice*

- **Model switching speed**
  - High to low model switching takes 15-25 seconds with 12GB VRAM and 24GB system RAM
  - *From: PizzaSlice*

- **AMD optimization**
  - 96GB VRAM AMD card can remove block transfer and force unload for better utilization
  - *From: nacho.money*

- **RAM usage for WAN 2.2 Fun**
  - Can reach 60-80GB RAM usage, T5 removal saves 10-20GB
  - *From: Gonzo*

- **VRAM for WAN 2.2 Fun**
  - RTX 3090 gets OOM at 720x480 81 frames with FP8 e5m2 scaled
  - *From: Josiah*

- **Performance on RTX 5090**
  - Native: 5 seconds, Wrapper: 10 seconds for same generation
  - *From: pagan*

- **4K upscaling with Wan 2.2 14B**
  - NOT recommended - causes system overload and overheating
  - *From: thaakeno*

- **VRAM for 600 frame generation**
  - Would need 96GB VRAM for extended frame generation at good quality
  - *From: VK (5080 128gb)*

- **5090 vs 4090 performance**
  - FP8_fast significantly faster on RTX 5090 than RTX 4090 percentually
  - *From: Kijai*

- **sageattn compatibility**
  - sageattn_qk_int8_pv_fp16_triton only option working with cuda128+torch2.8.0, other options cause bfloat16 errors
  - *From: trax*

- **Sapiens processing speed**
  - 5 minutes for 192 frame video on RTX 4090, can achieve 57.2 FPS average with optimizations
  - *From: fredbliss*

- **BFloat16 GPU compatibility**
  - Works best with Ampere+ GPUs (RTX 3090, A100) for 50% memory reduction
  - *From: fredbliss*

- **Sapiens batch processing**
  - Can handle 48 bboxes in parallel, batch processing crucial for multi-person scenarios
  - *From: ˗ˏˋ⚡ˎˊ-*

- **VRAM for Wan 2.2**
  - Can run on RTX 2080 with 8GB VRAM, but requires 64GB system RAM. RTX 6000 Pro can run everything native
  - *From: xwsswww*

- **RAM requirements**
  - 32GB RAM is very low for Wan 2.2, 64GB minimum recommended, 96GB comfortable for frequent generation
  - *From: Rainsmellsnice*

- **High resolution processing**
  - 1920x1080 v2v took over an hour on step 0 with 100GB RAM usage, while 1280x720 took 15 minutes
  - *From: Drommer-Kille*

- **SeedVR2 VRAM scaling**
  - RTX 4090: 720x720 to 960x960 max, RTX 3090 with 64GB RAM: 720p->1080p uses 98% VRAM
  - *From: Gill Bastar*

- **Wan 2.2 5B performance**
  - 22 minutes for 1080x1920 on RTX 4090, ~20 seconds VAE decoding for 1280x704 121 frames
  - *From: QuintForms*

- **Topaz VRAM usage**
  - Heaviest model uses maybe 16GB VRAM, uses 20-30% GPU on 5090, can run on 4GB VRAM cards
  - *From: Drommer-Kille*

- **RAM for fp8 vs GGUF models**
  - 64+ GB RAM can use fp8 with offloading, 32GB or less should use GGUF quantized models
  - *From: Kijai*

- **RTX 3060 12GB setup**
  - Can run fp8_e5m2 Wan 2.2 14B with workflow tweaks, --disable-smart-memory, and large swap file on SSD. Slower but works for upscaling to 900p
  - *From: mdkb*

- **SeedVR2 VRAM usage**
  - Takes 'infinite VRAM' - model is 33GB, causes high VRAM requirements
  - *From: Karo*

- **fp16 model with 32GB VRAM**
  - Can handle 81 frames at 720p, which is maximum official support
  - *From: Shawneau 🍁 [CA]*

- **3060 GPU capability**
  - Can achieve 1600x900x81 frames in 27 minutes with proper optimization
  - *From: mdkb*

- **3090 performance with 5B**
  - Gives solid video in 40 seconds
  - *From: Kiwv*

- **Storage issues with frequent model releases**
  - New models coming out every other day causing storage problems
  - *From: Kijai*

- **3090 torch compile**
  - Need fp8e5m2 models for torch compile, fp8e4nv not supported
  - *From: Josiah*

- **SageAttention compatibility**
  - 2000 series can't use sage2, 3000 series can use SageAttention regardless of model precision
  - *From: Kijai*

- **5090 VRAM usage**
  - WAN fp8 fits nicely on 5090 without block swap needed
  - *From: pagan*

- **A100 recommendations**
  - Don't need GGUF on A100 40GB, use fp8 models
  - *From: Juampab12*

- **Block swap memory impact**
  - Prefetch uses additional VRAM about the size of single block
  - *From: Kijai*

- **Rapid AllInOne efficiency**
  - Can do 121 frames at 720p without OOM
  - *From: Drommer-Kille*

- **VRAM for high resolution I2V**
  - Full HD (1920x1080) I2V likely not possible with 24GB, may need GGUF Q3 with heavy offloading
  - *From: Hevi*

- **Compute capability for FP8**
  - A5000 with compute 8.6 cannot do 14B FP8, needs higher compute capability
  - *From: Slavrix*

- **5B model performance**
  - 5B model supports 1024x1024 at 24 FPS and is very fast
  - *From: Gill Bastar*

- **Native ComfyUI needs 64GB RAM**
  - For non-GGUF models on 4070ti super, native workflow faster but requires 64GB RAM vs 32GB for GGUF
  - *From: pewpewpew*

- **SeedVR extremely VRAM hungry**
  - Even 32GB VRAM struggles with SeedVR, need GGUF models and offloading
  - *From: Gill Bastar*

- **GGUF Q8 works on 3090**
  - Can run GGUF Q8 on 3090, Q6 recommended for 32GB VRAM
  - *From: Hevi*

- **Block swap performance impact**
  - Each block computed individually, block swap adds transfer time on top of compute
  - *From: patientx*

- **VRAM savings with wrapper vs native**
  - Wrapper saves 3GB VRAM and several GB RAM compared to native implementation
  - *From: Jonathan*

- **Reference image processing**
  - Larger reference images may use more VRAM but not confirmed since it's single image
  - *From: Kijai*

- **VRAM management**
  - Native implementation uses ~88% of 24GB VRAM for 720p 121 I2V, wrapper needs block swapping
  - *From: Hevi*

- **4090 capability**
  - Can run minute-long multitalk generations and Q8 models effectively
  - *From: Kijai*

- **RAM usage concern**
  - RAM usage more concerning than VRAM when using offloading with fp16
  - *From: Kijai*

- **Multitalk performance**
  - 6 minutes for 1 person on 3060 with 832x480x121 frames at 24fps
  - *From: mdkb*

- **GPU compatibility for fp8_e4m3fn**
  - GPUs prior to 4000 series don't work with fp8_e4m3fn with torch compile, need to use fp8_e5m2
  - *From: Kijai*

- **Fun models storage**
  - Each Fun model is 30GB (15GB x2 for high/low noise variants)
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Stand-In v2v processing time**
  - 176 seconds on RTX 3060 for video processing
  - *From: mdkb*

- **Torch 2.9 compatibility issues**
  - Flash attention and custom nodes break with PyTorch 2.9, uninstalling flash attention recommended
  - *From: pagan*

- **Stand-in workflow VRAM usage**
  - 16GB VRAM easily enough with proper block swap settings
  - *From: Kijai*

- **Memory usage for 81 frames at 832x480**
  - Max 16.362GB with 15 blocks swapped, 11.657GB with 40 blocks swapped
  - *From: Kijai*

- **Memory usage with optimizations**
  - 7.136GB max allocated with chunked_rope enabled
  - *From: Kijai*

- **RTX 3090 generation speed**
  - Minimum 80s/it for 720p, varies significantly with resolution
  - *From: MiGrain*

- **RAM requirements for Wan 2.2**
  - 32GB RAM causes swapping issues, 64GB recommended for smooth operation
  - *From: Zueuk*

- **VRAM for MultiTalk**
  - Needs more than 8GB VRAM, fits in 23G with block swap
  - *From: nacho.money*

- **Dual GPU setup**
  - 2x 5090 available on RunPod for $1.75/hour
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Storage needs**
  - 15GB per Wan 2.2 model file, 4 models = 60GB disk space
  - *From: xwsswww*

- **Heat generation**
  - Hot spot behind PC reaches 93F/34C during generation, cable burning reported
  - *From: garbus*

- **VRAM for 81 frames at 720x720**
  - Needs ~20 block swap to fit in 24GB, max allocated 18.914GB
  - *From: Kijai*

- **RAM usage for Wan 2.2**
  - Hitting 80GB reserved with 128GB RAM on 2.2 workflow
  - *From: Kijai*

- **RAM usage can exceed 100GB**
  - Workflows can take up to 100GB+ RAM with paging
  - *From: Obsolete*

- **RTX 3090 quantization compatibility**
  - Must use fp8e5m2 instead of fp8e4nv for torch.compile
  - *From: Kijai*

- **Disk space for memory allocation**
  - Need 10% disk space available for proper memory allocation
  - *From: ˗ˏˋ⚡ˎˊ-*

- **8GB VRAM challenges**
  - Tough to work with, requires block swap around 20 for basic functionality
  - *From: Kijai*

- **CUDA Compute Capability 8.6 limitations**
  - Torch.compile with fp8_e4m3fn not supported, need to use fp8_e5m2, GGUF or higher precision
  - *From: ˗ˏˋ⚡ˎˊ-*

- **873 frames generation possible**
  - Successfully generated on single GPU but with noticeable artifacts
  - *From: T2 (RTX6000Pro)*

- **64GB RAM + 16GB VRAM can still run out**
  - RAM issues after second sampler finishes even with 64GB RAM
  - *From: 3Dmindscaper2000*

- **VRAM management critical for Windows users**
  - Windows CUDA does slow swap to shared memory instead of OOM, reserve-vram flag essential
  - *From: Kosinkadink*

- **13GB shared RAM usage observed**
  - 5090 user seeing significant shared memory usage during generation
  - *From: Kosinkadink*

- **AMD Ryzen 9 9900X achieves 40 it/s**
  - For FantasyPortrait node running on CPU
  - *From: Kijai*

- **Power consumption varies significantly**
  - 4090: 10-20W variance, 5090: 80W variance during generation
  - *From: IceAero*

- **720p 5 second clip on 4090**
  - Takes about 2 minutes for 1044x788 resolution on RTX 4090
  - *From: GalaxyTimeMachine (RTX4090)*

- **3060 VRAM limitations**
  - 3060 requires reduction from 720p to 832x480 resolution and various optimizations like distorch loading to avoid OOM
  - *From: mdkb*

- **3060 cards can't run e4m3fn models**
  - Need GGUF versions or fp16 with on-the-fly quantization for 3060 compatibility
  - *From: mdkb*

- **Phantom fp16 is 30GB**
  - Too large for on-the-fly quantization on 3060 cards
  - *From: mdkb*

- **GGUF conversion needs CUDA toolkit**
  - Requires nvcc and full CUDA toolkit installation for llama.cpp compilation
  - *From: orabazes*

- **VRAM usage with PUSA**
  - PUSA sampling uses more VRAM regardless of model format or merging
  - *From: Kijai*

- **RTX 3060 optimization**
  - Needs --disable-smart-memory flag, 32GB static swap file, offload everything possible to RAM. OOMs first run but works second time
  - *From: mdkb*

- **Model loading memory management**
  - Set second model loader to offload_device instead of main_device to prevent OOM, though main_device is faster
  - *From: phazei*

- **5090 VRAM limitations**
  - Not enough VRAM for MagRef + MultiTalk combination even on 5090 when renting
  - *From: MysteryShack*

- **RAM usage reduction in dev branch**
  - 20GB less RAM when not merging LoRAs
  - *From: Kijai*

- **VRAM optimization**
  - Workflow that was OOMing now uses GPU to fullest capacity
  - *From: ˗ˏˋ⚡ˎˊ-*

- **RTX 5090 VRAM limits**
  - Can handle up to 1280x720 97 frames, anything above causes OOM
  - *From: WorldX*

- **Block swap performance**
  - 3-minute generation time for 1280x720 81 frames with full FP16 model using block swap
  - *From: Ryzen*

- **RTX 6000 Pro performance**
  - 300% faster than RTX 5090 when models fit in VRAM, 48GB capacity vs 32GB
  - *From: WorldX*

- **8GB VRAM compatibility**
  - GGUF versions work on 8GB cards, FP8 scaled versions may cause OOM
  - *From: xwsswww*

- **Full model size too large for 32GB VRAM**
  - Original combined model pieces would exceed 32GB VRAM capacity
  - *From: Tony(5090)*

- **Training memory usage**
  - 75GB RAM consumed while training with 15 videos plus 2 datasets with 15 images each at 512/768/1024 resolutions
  - *From: Ryzen*

- **fp8 variants for different GPU generations**
  - fp8 e5m2 works with 30xx cards, fp8 e4m3fn requires 40xx cards or above
  - *From: mdkb*

- **Depth Crafter VRAM usage**
  - Consumes significant VRAM, causes OOM on 24GB VRAM with 125 frame videos
  - *From: Gill Bastar*

- **3090 FP8 support**
  - No real FP8 support on 3090, uses emulated FP8
  - *From: Josiah*

- **Context window VRAM**
  - Memory usage = context frames * width * height, need sufficient RAM for frame count after decode
  - *From: Kijai*

- **Training speed**
  - RTX card doing 1.5s/it for video training, 7000-10000 steps taking ~4 hours
  - *From: Ryzen*

- **System memory usage**
  - Image concat multi uses almost 120GB system memory
  - *From: Gateway*

- **VRAM usage optimization**
  - Dev branch uses different block swapping method with no init, loads only needed blocks directly
  - *From: Kijai*

- **Memory reservation capability**
  - New node allows reserving additional memory beyond model estimates
  - *From: Kosinkadink*

- **Performance variance on AMD/ZLUDA**
  - Dev branch showing slower performance (31-33 sec/it vs expected improvements) on Windows AMD systems
  - *From: patientx*

- **RTX 5090 performance**
  - 1024x576 video took 18 minutes for 873 frames
  - *From: T2 (RTX6000Pro)*

- **RTX 3090 performance**
  - 16 seconds at 480x480 took 18:34, 33 frames took 32 minutes, can do up to 1000 frames
  - *From: NC17z*

- **RTX 3060 performance**
  - 500 frames took 35 minutes
  - *From: mdkb*

- **Fun Control VRAM needs**
  - FP32/FP16 mixed model should use 30GB dedicated VRAM and 40GB total VRAM
  - *From: seitanism*

- **InfiniteTalk VRAM usage**
  - Same VRAM as MultiTalk despite larger model size due to looping method
  - *From: Kijai*

- **5090 generation time**
  - 17 minutes for 6-step generation with LightX2V
  - *From: Kijai*

- **3060 capabilities**
  - Can generate 8 seconds reasonably, 20 seconds in less reasonable time
  - *From: mdkb*

- **VRAM for InfiniteTalk**
  - 3060 struggles with InfiniteTalk, works better on higher end GPUs
  - *From: mdkb*

- **FP8 performance on 3090**
  - No speed difference between FP8 and GGUF Q8 on RTX 3090
  - *From: iShootGood*

- **RTX 3090 memory limits**
  - Q8 GGUF works better than fp8 for 3090, e5m2 not worth quality loss
  - *From: Kijai*

- **InfiniteTalk + FantasyPortrait VRAM**
  - Requires significant VRAM - grows model by 4GB, 24GB VRAM + 128GB RAM still getting OOM
  - *From: Kijai*

- **RTX 3070 8GB limitations**
  - Need Q6 model with blockswap, low resolution, and sufficient RAM to work
  - *From: Kijai*

- **4090/5090 fp8 performance**
  - Fp8 is faster on 4090 and 5090, but Q8 still better quality
  - *From: Kijai*

- **GPU compatibility for torch.compile**
  - Need RTX 4000 series or higher for fp8_e4m3fn weights, RTX 3090 users should use e5m2 or GGUF Q8
  - *From: Kijai*

- **Storage needs**
  - Users reporting need for 4TB+ NVMe storage for ComfyUI models, model storage growing rapidly
  - *From: 𝕯𝖗. 𝕸𝖆𝖈𝖆𝖇𝖗𝖊 ☠*

- **HDD vs SSD performance**
  - WAN takes forever to load on HDD, SSD strongly recommended
  - *From: Draken*

- **Network speed for NAS**
  - 1GB network not sufficient for NAS model storage, need 2.5G or 10G fiber
  - *From: piscesbody*

- **VRAM for Wan 2.2 14B**
  - Possible to run on 16GB VRAM using KJ's wrapper with proper optimization
  - *From: : Not Really Human :*

- **Generation time scaling**
  - Using audio CFG makes generation take 3x the time due to 3 passes (positive, negative, audio)
  - *From: Kijai*

- **Long generation times for quality**
  - 1 minute 36 second song with 25 steps takes approximately 2 hours 30 minutes on 5090
  - *From: seitanism*

- **Long generation times**
  - 2400 frames took 2.5 hours, 720p to 1024p upscale took 15 minutes
  - *From: seitanism*

- **VRAM issues with mixed precision model**
  - Wan 2.2 fp32/fp16 mixed stuck at 22GB VRAM usage with poor performance
  - *From: seitanism*

- **OOM with low noise upscale**
  - Wan 2.2 low noise upscale causes OOM on RTX 5090
  - *From: VRGameDevGirl84(RTX 5090)*

- **VRAM usage with cache-none**
  - 48GB VRAM, 128GB DRAM, 2GB swap - ComfyUI stable all day with --cache-none
  - *From: samhodge*

- **SeedVR2 VRAM requirements**
  - Not viable for 24GB cards, constantly runs out of VRAM
  - *From: 646594572499025921*

- **InfiniteTalk generation time**
  - 2400 frames at 480x720 with MagRef+InfiniteTalk executed in 6 hours 12 minutes
  - *From: seitanism*

- **InfiniteTalk GGUF model performance**
  - Q4 quality seems fine, Q8 very close to fp16 quality with fast dequant
  - *From: Kijai*

- **Fantasy Portrait Face Detector**
  - Should process 850 frames in few seconds on GPU with proper onnxruntime-gpu setup
  - *From: Kijai*

- **VRAM for 3000 frames**
  - Question about whether VAE decode will run out of VRAM at end with max 3000 frames
  - *From: Yae*

- **Wan 2.2 14B training VRAM**
  - 5 days to train LoRA with 5090, can use 32GB with split samples and low VRAM mode
  - *From: Drommer-Kille*

- **RunPod L40S performance**
  - Good performance for generation tasks, used for quick turnaround testing
  - *From: Santoshyandhe*

- **RTX 3090 limitations**
  - 17 minutes for single generation when Torch Compile not connected, can struggle with newer workflows
  - *From: NC17z*

- **Storage costs on RunPod**
  - $7 for 100GB storage per month, considered expensive
  - *From: Santoshyandhe*

- **RTX A6000 48GB performance**
  - 997 frames at 720p takes about 40 minutes, using e5m2 quantization on Ampere architecture
  - *From: samhodge*

- **Precision considerations for different architectures**
  - Ampere RTX A6000 (2020) uses e5m2, Ada (2022) and Blackwell (2025) support better precisions
  - *From: samhodge*

- **WAN 2.2 on 5090**
  - Can run fp32/fp16 mixed model with 20 blocks swapped, hardly need for Pro 6000 except training
  - *From: seitanism*

- **FP16 WAN 2.2 VRAM usage**
  - Uses 15GB VRAM but runs extremely slow, similar issues to 1% fp32/99% fp16 model
  - *From: seitanism*

- **CineScale VRAM needs**
  - Requires same VRAM as running at target resolution normally, tested at 1632x2880 on 96GB VRAM
  - *From: Kijai*

- **Wan 2.2 performance**
  - 81 frames at 720p renders in 82.76 seconds on fp8 scaled models
  - *From: Drommer-Kille*

- **VRAM for 10s video at 24fps**
  - Would need VRAM for 242 frames at some point in pipeline, at full offloading barely any difference to Wan 14B
  - *From: Kijai*

- **5070TI insufficient for 83 frame video with sound**
  - Takes ages to load, need to increase block swap and use TE on CPU
  - *From: hicho*

- **Torch compile compatibility**
  - Works on 3000 series and up, E5 compiles on 3000, E4 on 4000/5000 series
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Turbo model performance**
  - 9s to sample, 24s to decode for 5B turbo model
  - *From: Kijai*

- **RTX 6000 performance**
  - 1280x1280, 30 seconds rendered in 45 minutes
  - *From: Fill*

- **High VRAM for CineScale 4K**
  - Speculation that 8xA100 needed for proper 4K generation
  - *From: scf*

- **Tiled VAE required for 4K**
  - Must use tiled VAE when generating at 4K resolution
  - *From: Kijai*

- **3090 torch compile compatibility**
  - Works with GGUF or fp8_e5m2, no reason to disable compile on 3090
  - *From: Kijai*

- **Block swap usually needed on 3090**
  - Amount depends on resolution, compile reduces the need by reducing peak VRAM
  - *From: Kijai*

- **VAE decoding performance**
  - Default res takes ~20 seconds on 4090 while generation is 9 seconds
  - *From: Kijai*

- **InfiniteTalk speed benchmark**
  - ~10 minutes for 600 frames on 4090 without compile (640x640, 7 steps)
  - *From: Kijai*

- **FP8 E5M2 model for older hardware**
  - Converted for AMD and Nvidia 3000 series users to use with torch.compile
  - *From: patientx*

- **Processing time improvements**
  - 5B turbo model: 6 minutes with fp16, 4 minutes with e5m2 + torch.compile, down to 57sec sampling with unipc+beta
  - *From: patientx*

- **InfiniteTalk VRAM usage**
  - 12GB VRAM may be too low for InfiniteTalk, especially with VAE cache leak causing 2-3GB extra usage from 2nd window
  - *From: SonidosEnArmonía*

- **FP8 scaled_fast optimal for RTX 50 series**
  - FP8 scaled_fast mode is best for speed and slightly lower memory use than GGUF Q8, 16GB VRAM should be enough with 64GB RAM
  - *From: Kijai*

- **PUSA LoRA memory impact**
  - PUSA LoRA is huge and has pretty big memory impact when used with GGUF or as unmerged LoRA
  - *From: Kijai*

- **VRAM management**
  - Keep below 95% VRAM on Windows to avoid shared memory slowdowns. 25GB max allocated on 5090 for 696 frames at 832x512
  - *From: Kijai*

- **Block swapping stats**
  - Block transfer times around 0.0003s, compute time 1.3s, to_cpu transfer 0.2743s per block
  - *From: Draken*

- **Speed comparison**
  - 3 minutes for 5 seconds at 1200x600 on RTX 3090 with Wan 2.2 + Lightning
  - *From: Ashtar*

- **RAM for Wan 2.1**
  - 16GB RAM insufficient for 14B model, 64GB recommended
  - *From: Akumetsu971/SonidosEnArmonía*

- **InfiniteTalk VRAM on 5090**
  - Max allocated 28.411GB, max reserved 29.938GB for 297 frames at 960x640
  - *From: Kijai*

- **MultiTalk additional VRAM**
  - ~2.5GB more at Q8, divisible by block swap amount
  - *From: Kijai*

- **Block swap rendering time**
  - 7515 seconds for rendering with 17712.77MB total transformer block memory
  - *From: SwampMonster*

- **VRAM usage for image encoding**
  - 1536x1536 is pretty much the limit with 24GB VRAM without tiling
  - *From: Kijai*

- **Performance difference between model formats**
  - GGUF takes ~10 seconds to load, fp8 takes ~2 seconds
  - *From: Kijai*

- **3060 12GB performance**
  - Can run VACE identity swap at 1280x720 with 1 frame in about 3 minutes
  - *From: mdkb*

- **VRAM usage with LightX2V**
  - 81 frames at 832x480 with 6 steps: max 11.910 GB allocated, 12.750 GB reserved
  - *From: Kijai*

- **RAM savings with dev version**
  - Saves up to 30GB RAM with 2.2 workflows
  - *From: Kijai*

- **Paging file needed even with large RAM**
  - Even with 128GB RAM, need paging file to prevent crashes when going 1MB over
  - *From: Ablejones*

- **RAM for video work**
  - 64GB seems like minimum, considering 128GB for high level work
  - *From: Lodis*

- **VRAM for video generation**
  - 8GB VRAM not enough for video work, 3060 good value at <$400
  - *From: Lodis*

- **CPU recommendation**
  - 9950x good combo with 5090
  - *From: Lodis*

- **3060 performance**
  - 8 mins for 81 frames at 832x480 resolution
  - *From: mdkb*

- **Color Match node performance**
  - Takes all day on large/long videos, needs GPU acceleration
  - *From: 감자*

- **VRAM usage optimization**
  - Using iGPU for display saves 4% GPU VRAM, 2.2 14B fp16 peaks at 64% vs previous 90%+ usage
  - *From: Drommer-Kille*

- **Model loading from disk**
  - New loading method reserves much less RAM but may be slower on some setups
  - *From: Kijai*

- **Inference speed**
  - 11x slower than real-time (12 second video takes 60 seconds to generate)
  - *From: Mancho*

- **VRAM usage**
  - S2V model is heavier on VRAM than Wan 2.2 A14B but easier on RAM
  - *From: Kijai*

- **PyTorch version**
  - Need PyTorch 2.7+ for proper functionality, 2.3.1 causes issues
  - *From: patientx*

- **VRAM for attention operations**
  - 512×512: ~1GB base, 1024×1024: ~4GB, 2048×2048: ~16GB (calculated with 3x modifier)
  - *From: Mu5hr00m_oO*

- **Block swap and torch compile compatibility**
  - Cannot use compile torch and blockswap together currently with S2V
  - *From: slmonker*

- **Frame count vs VRAM**
  - 1000 frames uses same VRAM as 81 frames due to context window architecture
  - *From: Kijai*

- **Memory issues with latest wrapper**
  - Latest WanVideoWrapper version shows unusual VRAM spikes and instability
  - *From: Kenk*

- **GPU requirements for fp8_e5m2_fast**
  - you need 4000+ series GPU to use the _fast mode
  - *From: Kijai*

- **VRAM optimization target**
  - 95% VRAM usage is generally safe for optimal performance
  - *From: Kijai*

- **Processing speed benchmark**
  - 48 seconds video took 58 minutes processing, so a little over a minute a second generation times
  - *From: T2 (RTX6000Pro)*

- **Resolution performance impact**
  - going over 832 makes everything extra slow
  - *From: patientx*

- **S2V generation speed**
  - RTX 4090: 13 minutes for 601 frames at 960x640 with 6 steps
  - *From: Kijai*

- **InfiniteTalk generation time**
  - RTX 3090 24GB + 32GB RAM: 15-18 minutes for 17 seconds at 832x592
  - *From: Antey*

- **S2V long video generation**
  - 1000 frames at 720p in 25 minutes
  - *From: ingi // SYSTMS*

- **A5000 performance issues**
  - First sampler pass took 24 hours for 501 frames, indicating severe performance problems
  - *From: Slavrix*

- **VACE GGUF Q4_K_S**
  - OOM issues reported with 48GB VRAM on 119 frames 1280x720
  - *From: AmirKerr*

- **S2V fp8 model**
  - 2GB smaller after fixing pose condition layer, audio injection layers work fine in fp8
  - *From: Kijai*

- **HunyuanVideo-Foley VRAM usage**
  - No reason for it to use that much VRAM according to analysis
  - *From: Kijai*

- **Blackwell GPU requirements**
  - PyTorch 2.8 + CUDA 12.8 minimum requirement for Blackwell series GPUs
  - *From: Kijai*

- **RTX 6000 Pro performance for T2V**
  - About 200 seconds for 720x1280x81 frames T2V generation, 64GB DDR4 RAM becomes bottleneck
  - *From: dg1860*

- **Linux vs Windows memory efficiency**
  - 64GB RAM on Linux equivalent to 128GB on Windows for same performance, much more memory efficient
  - *From: Kijai*

- **H100 capability for long generation**
  - Can generate 47 second videos on H100, though VRAM/RAM usage not specified
  - *From: ˗ˏˋ⚡ˎˊ-*

- **S2V VRAM usage**
  - S2V is a hefty beast even at q4k_m quantization, GGUF offloading helps significantly
  - *From: DawnII*

- **Memory leak in Framepack**
  - Before fix: Max allocated memory: 15.313 GB, Max reserved memory: 22.531 GB - 7GB wasted due to accumulation
  - *From: Kijai*

- **RTX3090 performance**
  - 50 minutes generation time for Infinite Talk with MAGREF 14B fp8 on RTX3090
  - *From: NC17z*

- **VACE encoding VRAM**
  - Peaks at 15GB VRAM for 85 frames at 1280x720 with 6 steps
  - *From: Kijai*

- **Long video generation**
  - Successfully generated 1600 frames on RTX6000Pro
  - *From: T2 (RTX6000Pro)*

- **128GB RAM with 3090**
  - Still experienced crashes at 500 frames until using offload_device
  - *From: 𝕯𝖗. 𝕸𝖆𝖈𝖆𝖇𝖗𝖊 ☠*

- **RTX 3060 model choice**
  - FP8 usually works better in wrapper, GGUF in native workflows
  - *From: mdkb*

- **Context windows performance**
  - 501 frames at 640x640, 6 steps: 5:56 on RTX 5090, max 12.775GB VRAM
  - *From: Kijai*

- **Memory management**
  - PyTorch reserves RAM even after moving objects, Windows reserves 20GB before runs
  - *From: Kijai*

- **Python 3.13 benefits**
  - No obvious performance benefits noticed yet
  - *From: Ablejones*

- **VRAM for upscaling workflow**
  - Regular 14B high/low noise models cause VRAM issues even on RTX 5090, Q8 models recommended
  - *From: WorldX and Gill Bastar*

- **RAM usage improvement**
  - 64GB RAM users can avoid swap files with new pytorch 2.8 update
  - *From: hicho*

- **CineScale VRAM**
  - V2V VRAM requirements not higher due to being a LoRA
  - *From: DawnII*

- **14B model requirements**
  - 14b requires 8xh100, probably for 4k
  - *From: [˗ˏˋ⚡ˎˊ-]*

- **InfiniteTalk generation speed**
  - 2000 frames in 28 windows, at 832x480 with 4 steps, 12 mins
  - *From: Kijai*

- **L40s performance**
  - Generated video on l40s which took around 20 minutes for Bollywood movie dialogue
  - *From: Santoshyandhe*

- **Increased VRAM usage in recent versions**
  - Need to increase blockswaps from 20 to 26 for 480x720 resolution, OOM issues even with 96GB VRAM
  - *From: .: Not Really Human :., HeadOfOliver*


## Community Creations

- **VACE 2.2 workflow with openpose** (workflow)
  - Working VACE implementation using openpose controlnet
  - *From: GOD_IS_A_LIE*

- **Custom combined sampler node** (node)
  - Single node combining high and low noise sampling with denoise control
  - *From: VRGameDevGirl84(RTX 5090)*

- **T5 unload node** (node)
  - Completely unloads T5 after use, leaves nothing in VRAM or RAM
  - *From: Kijai*

- **Latest frame grabber node** (node)
  - Grabs the latest last frame from a directory for chaining workflows
  - *From: Flipping Sigmas*

- **VACE multi-scene chaining workflow** (workflow)
  - Complex workflow with T2V start feeding into 5 I2V sections with frame interpolation
  - *From: seitanism*

- **WAN 2.2 upscaling workflow** (workflow)
  - Uses WAN 2.1 VACE then WAN 2.2 high noise for upscaling
  - *From: GOD_IS_A_LIE*

- **T5 Memory Unload Node** (node)
  - Completely unloads T5 encoder after use to save RAM
  - *From: Kijai*

- **NAG Text Encoding Node** (node)
  - Separate text encoding node with NAG (Negative Attention Guidance) support
  - *From: Kijai*

- **CustomGPT for WAN prompting** (tool)
  - GPT trained on official Alibaba materials for generating cinematic prompts
  - *From: The Shadow (NYC)*

- **WanVideoWrapper** (node)
  - Kijai's ComfyUI wrapper for Wan models with context windows support
  - *From: Kijai*

- **LLM prompt generation system** (workflow)
  - System guide for LLM to create prompts for T2I generation with negative prompts
  - *From: Simjedi*

- **Character LoRA** (lora)
  - Trained on specific face for 59 minutes with high noise model
  - *From: Kenk*

- **WanVideoWrapper** (node)
  - Kijai's ComfyUI wrapper for Wan models
  - *From: Multiple users*

- **Blockswap node** (node)
  - Saves VRAM by offloading to CPU
  - *From: Ryzen*

- **Automatic context frame calculator** (workflow)
  - Automatically calculates context frames and num_frames based on number of '|' separators in prompt
  - *From: avataraim*

- **Ollama prompt preprocessing workflow** (workflow)
  - Uses Ollama nodes to process prompts and images, returns English and Chinese prompts using multimodal models
  - *From: Juan Gea*

- **Qwen 2.5 integration** (node)
  - Local prompt extension with zero memory usage after completion
  - *From: Kijai*

- **V2V upscaling workflow** (workflow)
  - Upscales 480p to 1080p while fixing specific details
  - *From: thaakeno*

- **MMaudio + RIFE workflow** (workflow)
  - Integrates audio generation with frame interpolation for sync
  - *From: thaakeno*

- **Custom VFI batching node** (node)
  - VFI node with batch_size 40 for faster interpolation (4 seconds vs 15-20s)
  - *From: gokuvonlange*

- **14B I2V movie training experiment** (training)
  - Training 14B I2V on 3500 movie extracts at FPS=1, 5-81 frames at 192 resolution for high model, 5-21 frames at 320 for low model
  - *From: mamad8*

- **Animorphs-type transformation lora** (lora)
  - Early 250 step checkpoint for transformation effects on 2.2 5B i2v
  - *From: orabazes*

- **Background training loras** (lora)
  - City centre backgrounds and background removal techniques
  - *From: Ryzen*

- **Middle frame implementation** (workflow)
  - Modified WanFirstLastImageToVideo code for middle frame conditioning
  - *From: Juampab12*

- **Video upscale + motion fix workflow** (workflow)
  - Takes video latent and feeds to high-noise model with start step control
  - *From: thaakeno*

- **MMAudio integration workflow** (workflow)
  - Combined video generation and audio synthesis in single workflow
  - *From: thaakeno*

- **FPS=1 I2V training approach** (training method)
  - Training LoRA on slideshow-type video for sequential scene generation
  - *From: mamad8*

- **WanVideoWrapper** (node)
  - ComfyUI wrapper for Wan models
  - *From: Kijai*

- **FPS1 LoRA** (lora)
  - Custom LoRA for specific frame rate control, showing promising results
  - *From: mamad8*

- **FPS1 experimental LoRA** (lora)
  - Generates videos at 1 FPS instead of 16 for storyboarding and longer scene creation
  - *From: mamad8*

- **Character transformation LoRA** (lora)
  - Nick Cage transforming into elephant, trained at 3000 steps
  - *From: orabazes*

- **LoRA timestep scheduling** (feature)
  - Allows per-step LoRA strength control with curves and dropoff
  - *From: Kijai*

- **Context window workflow** (workflow)
  - Wan 2.2 with context window implementation
  - *From: thaakeno*

- **Multi-sampler approach** (workflow)
  - 3 ksamplers: 1 step 3.5cfg, 2 steps cfg1 ltrx 3.0, final cfg1 ltrx 0.7
  - *From: 3DBicio*

- **Custom dockerized Wan 2.2 serverless setup** (workflow)
  - Complete Docker container with ComfyUI, pytorch, models, sage attention for serverless deployment
  - *From: gokuvonlange*

- **Custom web UI for job dispatching** (tool)
  - Vibe-coded web UI that dispatches jobs to H100 or 5090 workers
  - *From: gokuvonlange*

- **Judy Hopps LoRA** (lora)
  - T2V A14B LoRA for Wan 2.2
  - *From: MisterMango*

- **Enhanced workflow with LoRA scheduling** (workflow)
  - Integration of Kijai workflow LoRA improvements
  - *From: au*

- **Fixed Wan 2.2 Lightning LoRAs** (lora)
  - Corrected alpha values and converted to fp16 from original fp32 LoRAs
  - *From: Kijai*

- **Multiple rank extractions of 720p distill I2V** (lora)
  - Extracted rank 32, 64, and 128 versions of the 720p distilled I2V model
  - *From: Kijai*

- **Kijai's fixed Wan 2.2 Lightning LoRAs** (lora)
  - Fixed versions of official LoRAs that work at 1.0 strength with proper ComfyUI key naming
  - *From: Kijai*

- **Judy Hopps LoRA for Wan 2.2** (lora)
  - Improved character LoRA for Judy Hopps, upcoming release on Civitai
  - *From: MisterMango*

- **Aether punch face impact LoRA** (lora)
  - LoRA for Wan 2.2 5B I2V creating punch impact effects
  - *From: Juampab12*

- **Claude prompting system** (tool)
  - Custom Claude project with Wan prompting guide for generating structured prompts
  - *From: Juampab12*

- **WanVideoWrapper** (node)
  - Kijai's wrapper with optimized VRAM management and compile optimizations
  - *From: Kijai*

- **ClownsharkSampler** (sampler)
  - Alternative sampler that produces more fully sampled, less noisy results
  - *From: Ablejones*

- **Qwen3 prompt enhancement node** (node)
  - Node that can take image or video to generate prompts, no auth key required
  - *From: shockgun*

- **WanVideoWrapper improvements** (node)
  - Ongoing updates and fixes to the ComfyUI wrapper for Wan models
  - *From: Kijai*

- **CFG scheduling node for native 2.2** (node)
  - Node that handles CFG lists for first step only CFG application in native workflows
  - *From: Kijai*

- **Video prompter with API integration** (tool)
  - Tool for generating video descriptions from uploaded videos using API
  - *From: thaakeno*

- **Image difference analysis CLI tool** (tool)
  - Python CLI for comparing VAE outputs with statistical analysis and amplified difference visualization
  - *From: fredbliss*

- **WanVideo context windowing workflow** (workflow)
  - Advanced workflow for generating longer sequences using context sliding technique
  - *From: Kijai*

- **Video batch splitter** (node)
  - Splits batch videos out for individual selection and downstream processing
  - *From: Fill*

- **Video picker node (planned)** (node)
  - Select which video from batch to send downstream for upscaling
  - *From: Fill*

- **WAN 2.2 14B Arcane Jinx LoRA** (lora)
  - High and low noise LoRA for character consistency
  - *From: Cseti*

- **Collage side-by-side webapp** (tool)
  - Vibecoded webapp for creating side-by-side character references
  - *From: Juampab12*

- **VACE module separation node** (node)
  - Saves disk space by storing VACE in separate file, similar to wrapper functionality
  - *From: Kijai*

- **Subgraph workflow organization** (workflow)
  - Clean single node containing entire workflow, like Blender groups
  - *From: Nekodificador*

- **FakeVace2.2** (model)
  - Experimental attempt to recreate VACE 2.2 functionality
  - *From: JohnDopamine*

- **Latent injection nodes** (node)
  - Experimental nodes for latent encoder/injector with activation patching for better text-to-latent embedding
  - *From: fredbliss*

- **VACE strength control node for Phantom embeds** (node)
  - Allows setting VACE strength of phantom embeds, can work with insane values like 1000
  - *From: Ablejones*

- **Phantom+VACE merge model** (model)
  - Months of work to find good vace/phantom mix for character consistency and control
  - *From: Piblarg*

- **FlF2V dreamy morphing workflow** (workflow)
  - Workflow using add noise setting with LoRAs to create smooth dreamy transitions
  - *From: piscesbody*

- **VACE character swap workflow** (workflow)
  - Method for swapping characters using VACE module with Wan 2.2 and reference images
  - *From: mdkb*

- **Scene teleportation I2V workflow** (workflow)
  - Beta workflow for teleporting characters between scenes with likeness preservation
  - *From: Juampab12*

- **WanVideo I2I Expression/Perspective LoRA** (lora)
  - Helps maintain character similarity during scene changes and perspective shifts
  - *From: Juampab12*

- **VACE/Phantom merge** (workflow)
  - Merging VACE and Phantom for identity preservation with control
  - *From: Piblarg*

- **Native VACE node** (node)
  - Native ComfyUI node that works similar to loading VACE as a module
  - *From: Kijai*

- **Custom LoRA training approach** (workflow)
  - Different training for high/low noise - removed static videos from high noise, used different resolutions and frame counts
  - *From: Cseti*

- **RadialAttn implementation** (tool)
  - Works at 768x768 resolution, tested up to 81 frames
  - *From: Дмитрий Марков*

- **VACE/Phantom merge workflow** (workflow)
  - Combines VACE control with Phantom consistency
  - *From: Piblarg*

- **Gemini frame calculator** (tool)
  - Automatically calculates optimal frame counts for different resolutions
  - *From: GalaxyTimeMachine (RTX4090)*

- **Sapiens pose detector (full version)** (tool)
  - Two-stage pose detection and drawing using full Sapiens model with torchscript, not lite version
  - *From: fredbliss*

- **WAN 2.2 + VACE merge** (model)
  - Block merge combining WAN 2.2 with VACE capabilities
  - *From: R.*

- **Sapiens pose detector** (tool)
  - Updated pose detector with --max-people setting and input video removal
  - *From: fredbliss*

- **Visual scheduler node concept** (node)
  - Proposed node to set schedules visually with sigma curve display for better understanding
  - *From: Kijai*

- **VACE advanced nodes** (node)
  - Advanced VACE nodes on GitHub for enhanced control capabilities
  - *From: Lodis*

- **Phantom merge with VACE** (workflow)
  - Combined VACE and phantom merge workflow for character consistency
  - *From: Lodis*

- **WanVideo VACE Start to End Frame node** (node)
  - Kijai's node for single frame to video conversion with controlnet input
  - *From: Lodis*

- **Sapiens wheels** (tool)
  - Pre-compiled wheels for easier Sapiens installation
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Sapiens flexible pipeline** (tool)
  - Comprehensive pipeline supporting multiple model formats, trackers, and optimization strategies with performance presets
  - *From: fredbliss*

- **Sapiens ComfyUI node** (node)
  - ComfyUI integration for Sapiens pose detection with batch processing and memory optimization
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Sapiens CLI multi-person tracking** (tool)
  - Complete pose detection pipeline with multi-person tracking, camera movement handling, and temporal smoothing
  - *From: fredbliss*

- **2.2 VACE hybrid merge** (workflow)
  - Method to merge some early blocks + patch embed from 2.1 into 2.2 to increase VACE effect on high noise side
  - *From: JohnDopamine*

- **Select Every Nth Frame node** (node)
  - Drops every nth frame, useful for 3-2 pulldown conversion from interpolated footage
  - *From: Kijai*

- **Get Images From Batch Indexed node** (node)
  - Used for stripping out specific frames for fps conversion workflows
  - *From: Kijai*

- **Custom sword fight LoRA** (lora)
  - LoRA trained on sword fights at 24fps, makes fighting look like 90s movie style
  - *From: Ruairi Robinson*

- **Enhanced drag crop node** (node)
  - Added rectangle crop and magic image loading features to ComfyUI-Olm-DragCrop
  - *From: Hoernchen*

- **Sapiens multi-person tracking** (tool)
  - CLI tool for tracking 10+ people with pose estimation, segmentation, and 300+ human features
  - *From: fredbliss*

- **Enhanced WanVideoWrapper schedulers** (node)
  - Branch with additional schedulers and fancy looping node with dynamic prompt controls
  - *From: Hoernchen*

- **Skyreels LoRA extraction** (lora)
  - Extracted from Skyreels model to help break 121 frame loop in 2.2
  - *From: Kijai*

- **5B controlnet implementation** (node)
  - Traditional depth controlnet working with 5B model
  - *From: TheDenk*

- **WanVideo wrapper updates** (node)
  - Continuous updates to wrapper with new model support
  - *From: Kijai*

- **Sigma visualization nodes** (node)
  - Custom nodes for visualizing sigma splits with Fixed Fraction, Sigma Threshold, and SNR options
  - *From: Alisson Pereira*

- **ComfyUI-WanMoeKSampler** (node)
  - KSampler modification for Wan 2.2 MoE
  - *From: Tomber*

- **Block swap prefetch optimization** (optimization)
  - Added prefetch option to improve block swap transfer speeds
  - *From: Kijai*

- **Skyreels LoRA extraction** (lora)
  - Extracted Skyreels LoRA for 121-frame generation capability
  - *From: Kijai*

- **Skyreels LoRA conversions** (lora)
  - Converted old Skyreels I2V LoRA to work with T2V, breaks looping but enables longer generation
  - *From: Kijai*

- **Stand-In ComfyUI implementation** (node)
  - ComfyUI wrapper for Stand-In LoRA face consistency system
  - *From: Kijai*

- **VACE inpainting workflow** (workflow)
  - Workflow using Impact pack for face masking with VACE inpainting
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Modified SeedVR GGUF nodes** (node)
  - Alisson Pereira created modified version for GGUF compatibility
  - *From: Gill Bastar*

- **All-in-one Wan 2.2 workflow for ZLUDA** (workflow)
  - Specially targeting AMD GPU users with ZLUDA or TheRock torch
  - *From: patientx*

- **WanVideoWrapper** (custom node)
  - ComfyUI wrapper for Wan video models with example workflows
  - *From: Kijai*

- **Skyreels v2 LoRA** (lora)
  - Speed LoRA that enables 121 frame generation for Wan
  - *From: Kijai*

- **ComfyUI Wan 2.2 FFLF node** (custom node)
  - First Frame Last Frame implementation for Wan 2.2 5B
  - *From: stduhpf*

- **LoRA extraction workflow** (workflow)
  - Method to extract LoRA from Wan 2.2 LN using Wan 2.1 as base model
  - *From: Ablejones*

- **Fun Control workflow** (workflow)
  - Clean workflow for Fun Control bullet time style generations
  - *From: T2 (RTX6000Pro)*

- **Enhanced Stand-In workflow** (workflow)
  - Uses PersonMaskUltra node to segment, crop and resize reference images for better quality output
  - *From: BobbyD4AI*

- **Stand-In v2v workflow** (workflow)
  - Enables video-to-video with reference image using VACE integration
  - *From: mdkb*

- **Stand-in workflow with face cropping** (workflow)
  - Uses MediaPipe and InspyreNet instead of official YOLO preprocessor, no additional packages needed beyond Essentials and controlnet-aux
  - *From: Kijai*

- **Fantasy Portrait integration** (feature)
  - Face consistency system that works with MAGREF and other models for portrait generation
  - *From: Kijai*

- **Context window workflow for long generation** (workflow)
  - Method for generating 177+ frame videos using context windows with MAGREF
  - *From: Kijai*

- **WanVideoWrapper** (node)
  - Kijai's wrapper implementation with different workflow approach
  - *From: Juan Gea*

- **Fantasy Portrait visualization** (node)
  - Added bbox and landmark detection visualization with 222 keypoints
  - *From: Kijai*

- **VACE RAM reduction node** (node)
  - Node for reduced RAM usage in wrapper workflows
  - *From: Kijai*

- **Python script for Cascadour 3D scenes** (workflow)
  - Claude-generated Python script to create 3D controlnet input from Cascadour
  - *From: mdkb*

- **Cached text encoder node** (node)
  - Fully unloads text encoder model after encoding, doesn't even leave it in RAM
  - *From: Kijai*

- **WanVideo AddStandInLatent node** (node)
  - New node for debugging, connected to video combine
  - *From: Kijai*

- **NAG node for Wan** (node)
  - Wan-specific node for negative prompting when not using CFG
  - *From: Kijai*

- **Janky Memory Patcher** (node)
  - Overrides memory manager estimation, allows customizable VRAM buffer
  - *From: Ablejones*

- **Advanced VACE control node** (node)
  - Allows separate reference and control strength in single node
  - *From: Ablejones*

- **Experimental Phantom+VACE strength control** (node)
  - Controls VACE strength values for phantom embed latents
  - *From: Ablejones*

- **Lazy switches for workflow switching** (workflow technique)
  - More reliable switches that don't need bypass/muting and work with API
  - *From: Kijai*

- **VACE + Phantom merge workflow** (workflow)
  - Combined 1.3B VACE + Phantom workflow for style from prompt generation
  - *From: Kijai*

- **WanVaceAdvanced nodes** (node)
  - Includes latent extraction node for video continuation experiments
  - *From: Ablejones*

- **WanFM implementation** (node)
  - Frame Morphing sampling method for bidirectional generation
  - *From: Kijai*

- **Phantom VACE merge** (model)
  - Community member Piblarg created and shared fp16 full weights version of Phantom VACE merge for GGUF conversion
  - *From: Piblarg*

- **Wan LoRA trainer** (node)
  - ComfyUI node for training LoRAs on Wan models
  - *From: shockgun*

- **Qwen-Image to WAN Bridge** (node)
  - Direct latent bridge from Qwen-image to WAN 2.2 without VAE decode
  - *From: fredbliss*

- **Fantasy Portrait first/last frame workflow** (workflow)
  - Hack to enable video-to-video by extracting input video frames as start/end points
  - *From: VRGameDevGirl84(RTX 5090)*

- **Modified frame extraction nodes** (node)
  - Custom nodes for grabbing first and last frames from video input
  - *From: VRGameDevGirl84(RTX 5090)*

- **Gray frame padding node** (node)
  - Adds gray frames to end of batch to satisfy Wan requirements, use with get image batch range to chop additional frames
  - *From: Flipping Sigmas*

- **Video grid creation node** (node)
  - Creates video grids from folder of videos, added to KJNodes, requires VHS nodes
  - *From: Kijai*

- **Model loader refactor in wrapper** (tool)
  - Better handling for unmerged LoRAs, loads at sampler directly to blockswap for faster start and less RAM usage
  - *From: Kijai*

- **MTV Crafter motion adapter extraction** (tool)
  - Extracted motion adapter from MTV Crafter model for use with MAGREF
  - *From: Kijai*

- **Add Memory to Reserve node** (node)
  - Node to reserve additional memory for models beyond estimated requirements
  - *From: Kosinkadink*

- **Layer extraction tool for PUSA** (tool)
  - Claude-coded tool for loading/injecting layer extractions with CLI script
  - *From: JohnDopamine*

- **Modified InfiniteTalk workflow** (workflow)
  - Replaced MultiTalk with InfiniteTalk in existing Fantasy Portrait workflow for longer video generation
  - *From: NC17z*

- **Fun Control multi-input workflow** (workflow)
  - Workflow with multiple control options including Flux generation, face landmarks, and various control inputs
  - *From: VRGameDevGirl84(RTX 5090)*

- **WanMoeKSampler** (node)
  - Custom sampler for photo restoration experiments
  - *From: cocktailprawn1212*

- **HiggsAudio ComfyUI Wrapper** (wrapper)
  - Alternative TTS wrapper with potential venv conflicts
  - *From: NebSH*

- **MTVcrafter integration** (workflow)
  - Available in dev branch with test workflow
  - *From: Kijai*

- **Dev branch updates** (tool)
  - Includes InfiniteTalk support and improved memory handling
  - *From: Kijai*

- **Modified uni3c node** (node)
  - Automatically processes video input without manual latent connection when using multitalk sampling
  - *From: Kijai*

- **Qwen to Wan bridge workflow** (workflow)
  - Integration between Qwen image generation and Wan video generation
  - *From: fredbliss*

- **Automatic InfiniteTalk workflow** (workflow)
  - Modified Kijai's test v2v infinite talk workflow to run fully automatically
  - *From: slmonker(5090D 32GB)*

- **Tutorial video for InfiniteTalk** (tutorial)
  - Recording tutorial video for automatic InfiniteTalk workflow
  - *From: slmonker(5090D 32GB)*

- **Mask attention for Fantasy Portrait** (modification)
  - Hacky implementation of mask attention inside Fantasy Portrait extension
  - *From: ManglerFTW*

- **Endless I2V workflow** (workflow)
  - Modified POM's endless workflow to use I2V instead of VACE
  - *From: VRGameDevGirl84(RTX 5090)*

- **InfiniteTalk context method implementation** (workflow)
  - Working temporal mask implementation for Fun model
  - *From: DawnII*

- **ComfyUI-QwenImageWanBridge** (tool)
  - Bridge for connecting Qwen image generation to Wan video generation with T2V method
  - *From: fredbliss*

- **WanVideoWrapper InfiniteTalk V2V** (node)
  - Updated wrapper with streamlined workflow and faster sampling for video-to-video lip sync
  - *From: Kijai*

- **Qwen Image to Wan latent bridge** (workflow)
  - Custom workflow for passing Qwen image latents directly to Wan generation
  - *From: fredbliss*

- **Audio splitting custom node** (node)
  - Splits audio based on frame count and FPS for workflows with multiple samplers
  - *From: VRGameDevGirl84(RTX 5090)*

- **Multiple character masking setup** (workflow)
  - Splits each character's face to 16:9 B&W mask for multi-character InfiniteTalk
  - *From: mdkb*

- **Multiple people support for Fantasy Portrait** (node)
  - Pull request to add support for multiple people in Fantasy Portrait node
  - *From: ManglerFTW*

- **TeaCache node** (node)
  - Caching node that caused user difficulties but provides memory optimization
  - *From: Akumetsu971*

- **ComfyUI QwenImageWanBridge** (tool)
  - Bridge for using Qwen image processing with WAN, supports LoRAs and image editing
  - *From: fredbliss*

- **ComfyUI-QwenImageWanBridge** (tool)
  - Nodes to convert Qwen image latents to WAN video, includes normalization and conversion nodes
  - *From: fredbliss*

- **First person WAN 2.2 i2v LoRA** (lora)
  - Trained for first person perspective, works in both i2v and t2v
  - *From: Drommer-Kille*

- **Blender control spline system** (workflow)
  - Using grease pencil outlines, curves and spheres for complex camera and object movement control
  - *From: Blink*

- **EasyCache/LazyCache ComfyUI implementation** (node)
  - Native ComfyUI caching system supporting almost all models with configurable thresholds
  - *From: Kosinkadink*

- **CineScale integration** (node)
  - RoPE frequency scaling support for resolution upscaling in WanVideoWrapper
  - *From: Kijai*

- **Film grain LoRA** (lora)
  - Real film grain LoRA in training, Rank8, 73mb files
  - *From: Drommer-Kille*

- **WanVideoWrapper** (node)
  - Kijai's ComfyUI implementation for Wan models
  - *From: Kijai*

- **CineScale LoRA quantized versions** (lora)
  - Kosinkadink quantized CineScale models for ComfyUI
  - *From: Tony(5090)*

- **MelBandRoFormer wrapper** (node)
  - Vocal separation model wrapper for ComfyUI
  - *From: Kijai*

- **Wan 2.2 FP8 E5M2 conversion** (model)
  - Converted 5B turbo model for older hardware compatibility
  - *From: patientx*

- **Debug pass-through node** (node)
  - Outputs console info about image data, tensors, memory usage, and media properties for debugging
  - *From: Gateway {Dreaming Computers}*

- **Uni3c workflow adaptation** (workflow)
  - Adapted Benji Future Thinkers workflow for Uni3c with controlnet support
  - *From: mdkb*

- **Deepthroat LoRA** (lora)
  - Custom LoRA trained by community member, well received
  - *From: Kenk*

- **Audio separation workflow** (workflow)
  - Extracts audio from every song, even from videos using voice isolation model
  - *From: Kenk*

- **WanVideoAddControlEmbeds node** (node)
  - Alternative control node for Fun Control system
  - *From: Kijai*

- **WanVacePhantomDualV2** (node)
  - Handles dual control inputs for VACE
  - *From: Ablejones*

- **Helper node for mask operations** (node)
  - Originally for Fun InP, works for VACE by inverting mask
  - *From: Kijai*

- **ComfyUI_WanVace-pipeline** (node pack)
  - Timeline tools and workflow management for Wan/VACE
  - *From: tarkansarim*

- **Fakevace implementation** (workflow)
  - Alternative VACE that works with extend nodes
  - *From: 771193439399444490*

- **New anime style LoRA for Wan 2.2** (lora)
  - Community-created LoRA with detailed process writeup
  - *From: crinklypaper*

- **WanVideoWrapper dev version** (node)
  - Refactored model loading system for ComfyUI
  - *From: Kijai*

- **wav2vec2 safetensors conversion** (model conversion)
  - Converted wav2vec2 to safetensors with fp16 version for easier setup
  - *From: Kijai*

- **VACE workflow zip package** (workflow)
  - Contains two VACE workflows including one for restyling
  - *From: mdkb*

- **Kenk's Wan LoRAs** (lora)
  - Civitai Wan LoRA creator, fantastic work according to user feedback
  - *From: Kenk*

- **CFG Skimming implementation** (workflow)
  - Alternative to 3-sampler setup with better prompt adherence
  - *From: Mu5hr00m_oO*

- **WanVideo Scheduler Selector** (node)
  - Custom node for better scheduler control
  - *From: Mu5hr00m_oO*

- **Cached CLIP encoding for KJNodes** (node)
  - Performance improvement for CLIP encoding
  - *From: Mu5hr00m_oO*

- **CFG Skimming experiment** (technique)
  - Lightning 4 steps generation with LoRA on HIGH & LOW noise
  - *From: : Not Really Human :*

- **Class extraction script** (tool)
  - Python script to split nodes.py into individual classes for LLM analysis of bugs
  - *From: MysteryShack*

- **Character/pose sheet workflow** (workflow)
  - done in a past with flux/sdxl/cn. now with wan. char/anything sheet
  - *From: N0NSens*

- **WanVideoWrapper native implementation** (node)
  - Native ComfyUI implementation providing raw model controls
  - *From: comfy*

- **CFG Skimming port to WanVideoWrapper** (node)
  - Port of CFG skimming technique to reduce burn-in effects
  - *From: Mu5hr00m_oO*

- **All additional quant sizes for S2V** (model)
  - Complete set of quantized model sizes uploaded
  - *From: orabazes*

- **Custom Sapiens pose implementation** (node)
  - Improved pose detection with filtering for VACE, better than existing Sapiens node
  - *From: ˗ˏˋ⚡ˎˊ-*

- **S2V pose input node** (node)
  - New pose_input node available in S2V branch
  - *From: Kijai*

- **PUSA flowmatch sampler** (node)
  - Sampler that expands timesteps for PUSA functionality
  - *From: DawnII*

- **Iron Maiden Eddie tribute video** (workflow)
  - AI reimagined tribute using Wan 2.1 to animate iconic album covers and bring Eddie to life
  - *From: Gateway {Dreaming Computers}*

- **fp8 Tensor subclassing for memory efficiency** (tool)
  - Custom torch.Tensor subclass to store frames in fp8 and convert on-the-fly for operations, enabling 1000+ 4K frames in ComfyUI
  - *From: ˗ˏˋ⚡ˎˊ-*

- **diffusion-pipe-TREAD** (tool)
  - Fork from Adamanthy that makes training faster than standard diffusion-pipe
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Context window upscaler workflow** (workflow)
  - Uses new core context windows to lower VRAM needs for upscaling
  - *From: ArtOfficial*

- **Sigma visualization node** (node)
  - Custom node to visualize sigma curves and timing information
  - *From: Mu5hr00m_oO (5080 + 64)*

- **Custom VACE strength per frame** (custom node)
  - Allows setting different VACE strengths for each latent frame
  - *From: Ablejones*

- **WanVaceAdvanced** (custom node)
  - Advanced VACE implementation with per-frame strength control
  - *From: Ablejones*

- **Torch compile fix** (tool)
  - Fix for torch compile surviving prompt changes by padding embeddings
  - *From: phazei*

- **Context window workflow** (workflow)
  - High noise + low noise two-pass system with different overlap/stride settings
  - *From: Kijai*

- **Matrix recreation project** (workflow)
  - 55 shots total Matrix scene recreation using gorilla character replacement, using VACE, DWPose, depth control, and various techniques per shot
  - *From: Nekodificador*

- **Face refining workflow** (workflow)
  - Experimenting with face refining for better lip movement when the face is relatively small in the video
  - *From: Ablejones*

- **WanFirstLastFrameToVideo** (node)
  - Custom node that replaces WanImageToVideo for first/last frame video generation
  - *From: Juampab12*
