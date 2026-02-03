# Wan Chatter Knowledge Base
*Extracted from Discord discussions: 2025-09-01 to 2025-10-01*


## Technical Discoveries

- **PUSA 2.2 works with VACE when using reference image or control signal**
  - PUSA can be combined with VACE for enhanced control capabilities
  - *From: Kijai*

- **PUSA makes T2V model act like I2V with ability to extend videos, start/end frame**
  - Main purpose is to cheaply add I2V capabilities to T2V models
  - *From: Kijai*

- **WAN 2.1 was trained with only 4k videos and ~$500 worth of compute**
  - Extremely cost-effective training approach
  - *From: Kijai*

- **Detailed prompts work better with WAN 2.1**
  - More detailed prompts produce better output quality, especially for camera movements
  - *From: Akumetsu971*

- **Including CFG gives motion with Wan 2.2**
  - CFG is needed for proper motion generation with Wan 2.2
  - *From: asd*

- **LightX2V LoRA works better at strength 3.0**
  - Using LightX2V at 3.0 strength without CFG produces good results
  - *From: Kijai*

- **Number of steps clearly influences speed of final output**
  - Step count affects the motion speed in generated videos
  - *From: 𝕯𝖗. 𝕸𝖆𝖈𝖆𝖇𝖗𝖊 ☠*

- **Pusa LoRA can be resized to 1/4 original size**
  - Resized from rank 512 (4.7GB) to average rank 98 (1GB) with minimal quality loss
  - *From: Kijai*

- **Resized Pusa LoRAs work fine unmerged**
  - The resized versions can be used without merging and may actually be stronger
  - *From: Kijai*

- **Best generation was with resized, unmerged Pusa LoRA**
  - Resized unmerged LoRAs produced superior results
  - *From: Kijai*

- **V2V degrades quality compared to I2V**
  - V2V actually degrades quality according to multiple users' observations
  - *From: VRGameDevGirl84(RTX 5090)*

- **Pusa LoRA minimum strength requirement**
  - Pusa LoRA needs minimum strength of 1.4 to work properly, which is the original default
  - *From: Kijai*

- **Degradation proportional to frame count**
  - Evidence shows degradation is proportional to number of frames generated
  - *From: dipstik*

- **Triton cache clearing fixes memory issues**
  - Clearing triton caches fixed inconsistent VRAM usage that was jumping between 20GB and 14GB
  - *From: Kijai*

- **Wan latent space structure**
  - Wan latent space has 4 images packed into one latent
  - *From: Kijai*

- **LTX Tiled VAE Decoder works with WAN 2.2 VAE**
  - Using LTX's tiled VAE decoder with WAN 2.2 VAE runs 5 times faster than usual decoder, with no apparent quality loss. Also helps 5B VAE load completely on GPU when it normally wouldn't
  - *From: l҈u҈c҈i҈f҈e҈r҈*

- **Pusa dataset uses Qwen-style prompting**
  - The Pusa training dataset prompts look like average qwen style prompting and need to be moderately descriptive
  - *From: TK_999*

- **Context windows with multiple frames reduces extension artifacts**
  - Using last 13 frames as context instead of single frame helps maintain consistency when extending videos, though some color grading inconsistencies remain
  - *From: 𝕯𝖗. 𝕸𝖆𝖈𝖆𝖇𝖗𝖊 ☠*

- **ChatGPT can help improve WAN prompting**
  - Taking example prompts and having ChatGPT modify your prompt according to the example format improves instruction following, especially for camera movement
  - *From: Gill Bastar*

- **GGUF Q8 better than fp8_e5m2 for quality**
  - GGUF Q8 is slightly slower but better quality than fp8_e5m2, unless using lots of big LoRAs which can't be merged with GGUF
  - *From: Kijai*

- **Rolling back to version 1.3.1 fixed generation issues**
  - User experienced washed out images, no movement, extra people, and wrong composition with newer version
  - *From: screwfunk*

- **Model loading behavior changed significantly**
  - Kijai changed model loading to use lazy loading with safetensors, keeps state_dict weights as references on meta device, moves to appropriate device only during sampling, saves 20-30GB RAM with 2.2 workflows
  - *From: Kijai*

- **Unmerged LoRA loading is now handled by sampler**
  - Loading is done on the sampler now, based on blockswap settings directly, making it smarter
  - *From: Kijai*

- **Context windows work with Wan 2.2 I2V but with limitations**
  - Can generate videos but sometimes tries to go back to start image between contexts, inconsistent results
  - *From: xwsswww*

- **Multiple image I2V implementation working**
  - Can use multiple input images with context windows, first image is main image, others are 'extra' images used like multiple prompts
  - *From: Kijai*

- **Pusa can work with context windows on T2V model**
  - Using Pusa with T2V 2.2 model gives strength comparable to I2V 2.2 and even more, allowing start from any frame and several key frames
  - *From: Mngbg*

- **Higher strength keeps more of input image**
  - Higher the strength, more it keeps the input image
  - *From: Kijai*

- **Context window stride causes jittery effect**
  - Stride causes jittery effect, more on high noise side and it can be less on low noise
  - *From: Kijai*

- **Pusa uses vector timesteps instead of single timestep**
  - Instead of one global timestep controlling noise across entire video, Pusa uses vector of timesteps—one for each frame. This allows each frame to evolve independently during diffusion process, enabling fine-grained control over motion and timing
  - *From: Dever*

- **Block swapping saves VRAM by loading blocks sequentially**
  - 14B model has 40 blocks, you swap 20 and it saves half the model's size in VRAM
  - *From: Kijai*

- **TAESD preview shows higher quality than latent2rgb**
  - Quality is on another level compared to latent2rgb, but TAESD shows all 81 frames while latent2rgb shows 21 frames as it's just latents
  - *From: Kijai*

- **Pusa can work with I2V models with specific setup**
  - To use Pusa with I2V would mean using the lora, inserting image to first latent AND adding the 20 extra channels I2V model needs
  - *From: Kijai*

- **Wan 2.2 I2V maintains small faces better than other models**
  - For i2v got best results with Wan 2.2 1920x1080 than any AI model. It was the only that kept small faces good. All closed models failed that
  - *From: Drommer-Kille*

- **Context windows technique is temporal tiling, not extension**
  - Context windows refers to original technique used with animatediff, which is temporal tiling in frame dimension, not extension like infinitetalk
  - *From: Kijai*

- **Pusa extension with noise ramping shows improved results**
  - Adding noise on every step with multipliers like 0.2,0.4,0.4,0.4 or 0.0,0.1,0.2,0.3 seems better than original pusa pipeline
  - *From: Kijai*

- **Using more than 1 noisy step with Pusa helps keep original colors better**
  - Pusa model performs better color preservation when using multiple noisy steps instead of just one
  - *From: Kijai*

- **Context windows with basic T2V and Pusa LoRA generates more coherent long videos**
  - Using context windows with just Pusa LoRA (no input images, no special scheduler, just dpm_sde++ and basic T2V) seems to generate more coherent 337 frame videos
  - *From: mamad8*

- **Wan 2.2 14B I2V works well with start and end image without needing Fun models**
  - Base I2V model handles first-frame-last-frame well, no need for specialized Fun models
  - *From: mamad8*

- **Xformers causes slow model loading times from HD**
  - Uninstalling xformers and using only pytorch attention makes models load faster
  - *From: MysteryShack*

- **InfiniteTalk can handle extremely long generations with minimal VRAM impact**
  - Max frame count doesn't affect VRAM use, only RAM use as finished frames are kept in memory. Can do 5500+ frames on 32GB VRAM + 64GB RAM easily. VRAM use determined by window size and resolution only.
  - *From: Kijai*

- **Audio CFG setting doesn't make significant difference**
  - Testing with audio CFG at 2.0 vs 1.0 showed minimal difference in InfiniteTalk results
  - *From: samhodge*

- **Fun Control models require enabling specific option**
  - When using Fun Control models and getting tensor size errors, enable 'fun_or_fl2v_model' option in WanVideo ImageToVideo Encode node
  - *From: Juan Gea*

- **5B model variants give very different quality**
  - Both the fast and turbo variants of the 5B model prefer different settings and give very different quality with same settings
  - *From: Dita*

- **Multiple prompts can be used with InfiniteTalk**
  - Can give more prompts by separating them with | symbol, and prompts get applied to each context window
  - *From: Kijai*

- **Wan 2.2 handles reflections well**
  - Observed good reflection rendering in mirror scenes
  - *From: Lodis*

- **Wan 2.2 still has finger quality issues**
  - Back to having finger problems like earlier versions
  - *From: Drommer-Kille*

- **GGUF 8.0 uses only 20GB VRAM at 848x480**
  - Can scale up to 1280x720 without issues, factor of 2.26415
  - *From: samhodge*

- **Native block swap reduces VRAM usage significantly**
  - From 5GB to 2.6GB VRAM usage
  - *From: hicho*

- **Overlap of 9 frames works well for video extension**
  - Recommended overlap setting for seamless video extension
  - *From: Dr. Macabre*

- **VACE can handle multiple subjects on same reference image**
  - Cut and paste subjects onto single canvas with white background, dimensions must match control video
  - *From: Kijai*

- **Pusa shows promising motion continuity**
  - Better than last-frame methods for maintaining camera motion direction
  - *From: Kijai*

- **Chinese prompts work better than translated English versions**
  - Chinese prompt generation produces higher quality results than their English translations
  - *From: hicho*

- **CFG 1 makes negative prompts useless**
  - With CFG set to 1, negative prompts are completely ignored
  - *From: Lodis*

- **Wan 2.2 Lightning v1.1 LoRA produces cartoon style**
  - The newer Lightning LoRA gives cartoon-like results instead of realistic ones
  - *From: Santodan*

- **V2V with denoise 0.60 fixes motion issues**
  - Video-to-video with 0.60 denoise helps when denoise 1 produces no motion
  - *From: hicho*

- **GGUF models are faster than FP8**
  - GGUF versions run 1 minute faster than FP8 versions
  - *From: patientx*

- **Disabling tiles decode fixes flickering in upscaling**
  - Flickering in upscaled video output can be resolved by disabling tiles decode
  - *From: FL13*

- **Three sampler setup for Wan 2.2 I2V improves dynamics**
  - Using 3 ksamplers: first without lora, second with LightX 2.1 lora for better dynamics and no slow motion, third with 2.2 lora. Total 6 steps (2/2/2)
  - *From: .: Not Really Human :.*

- **Higher rank LoRAs (256) introduce more animation than lower ranks**
  - Rank 256 LoRAs produce better movement, character looks down, clothes have better animation, more dynamic than low rank LoRAs
  - *From: 𝕯𝖗. 𝕸𝖆𝖈𝖆𝖇𝖗𝖊 ☠*

- **Magic-Wan-Image mixed model performs well with low steps**
  - Merged Wan 2.2 high & low into single model, tested with clownshark sampler at 4 steps
  - *From: patientx*

- **Pusa model works best for Wan 2.2**
  - Can be combined with VACE but requires experimentation
  - *From: pom*

- **SlowMotion issue in Wan 2.2 related to video length**
  - At 7 seconds getting slowmo, at 4 seconds speed is better, possibly related to 4 frames per 1 latent
  - *From: Kenk*

- **Using CFG is extremely important for Wan 2.2 motion**
  - People use 3 or more samplers to set some steps to use CFG, but using CFG does the work
  - *From: Kijai*

- **LightX2V floating CFG can cause ghosting in i2v**
  - Mixes some parts of both models at the end
  - *From: Kenk*

- **2 steps without lora helps bring in more WAN 2.2 natural motion**
  - Can mix CFG with lower strength Lora as alternative
  - *From: BecauseReasons*

- **Low resolution i2v has far better movement than higher resolution**
  - Upscaling low res latents and feeding to low sampler led to pixelated output
  - *From: flo1331*

- **RAAG settings useful on high side or two pass sampling**
  - Testing with CFG 8 and tcfg on with light_v1.1, RAAG at 10, no burning or oversaturation
  - *From: Dita*

- **Lora merge option only obeys the last one's merge setting**
  - All loras need merge enabled individually for order independence
  - *From: Hoernchen*

- **Wan 2.2 was trained at 960x960 resolution for both T2V and I2V**
  - Training resolution confirmed as 960x960 pixels
  - *From: Mak*

- **Wan 2.2 models naturally loop around frame 109**
  - Model has tendency to loop after 109 frames
  - *From: N0NSens*

- **5B model gives more motion than 14B in some cases**
  - Charlie claims 5B understands prompts better and gives better results for certain use cases, particularly I2V
  - *From: Charlie*

- **Fun Control high noise with regular Wan low noise works well**
  - Using Fun Control model as high noise and regular Wan as low noise gives better quality, don't necessarily need control on low noise side
  - *From: Kijai*

- **Wan prompt generator node helps with motion in T2V and I2V without LLM**
  - Using manual prompts from JSON files in the wan prompt generator significantly improves motion
  - *From: hicho*

- **Linear sigma split works well for low step counts**
  - For 6 steps or under, manual sigma selection works best: 1.0000, 0.9375, 0.8750, 0.4375, 0.0000
  - *From: phazei*

- **Power consumption for Wan is lower than image generation**
  - 5080 uses ~200w for Wan video vs 350w for Flux image generation, 5090 uses ~226w at 720p
  - *From: VK (5080 128gb)*

- **VACE can be used as a detailer with SEGS**
  - Using control input video as original with 0.5 strength and ~0.5 denoise for upscaling and detailing
  - *From: Ablejones*

- **Wan 2.2 can handle extended generation through latent saving/loading in chunks**
  - VK demonstrated successfully decoding saved latents in segments (0-10, 10-20, 20-30 frames) with smooth blending between chunks
  - *From: VK (5080 128gb)*

- **MultiTalk produces better results than InfiniteTalk for face generation**
  - Multiple users reported MultiTalk gives better quality without the 'exploding confetti' first frames that InfiniteTalk produces
  - *From: mdkb*

- **Reward LoRAs work with Wan 2.2 and add detail enhancement**
  - Testing shows 1.0 strength gives best results, adds details like scaffolding, improved drum detail, electric cords
  - *From: crinklypaper*

- **Inserting reference frames in middle of video helps maintain character consistency**
  - VK found that inserting 8 reference frames in the middle of generation helps keep form of reference image
  - *From: VK (5080 128gb)*

- **VHS Combine causes OOM issues with long videos**
  - VHS Combine consumes excessive RAM when processing 1000+ frames, causing out-of-memory errors. Same workflow works fine with Save Image node instead
  - *From: samhodge*

- **Wan 2.2 reward LoRAs work with base models too**
  - MPS and HPS reward LoRAs trained on Fun models still have effect on other Wan 2.2 models including normal and Pusa
  - *From: Kijai*

- **InfiniteTalk doesn't decode latents during processing**
  - InfiniteTalk passes images through without actual decoding, only decodes frame_window_size at once, not the full batch
  - *From: Kijai*

- **Reward LoRAs don't work well with Pusa**
  - Testing showed reward LoRAs produce suboptimal results when combined with Pusa workflows
  - *From: Lodis*

- **Wan 2.2 boundary switching mechanism**
  - Uses boundary parameter to switch between high/low noise models. For i2v: boundary = 0.900 (switches after step 22 at 40 total steps). For t2v: boundary = 0.875 (switches after step 12)
  - *From: A.I.Warper*

- **Wan 2.2 behaves like FL2V model**
  - 2.2 acts like fl2v model in that it's trained to handle last frame encoding differently
  - *From: Kijai*

- **Radial attention speed vs quality trade-off**
  - Block size 128 is faster than 256/512. First step and first block are critical for quality. Always has quality hit but speed benefit useful for testing
  - *From: Kijai*

- **Wan 2.2 supports middle frame interpolation**
  - 2.2 fun InP can do middle frame interpolation better than previous versions, though still struggles with blending
  - *From: Kijai*

- **Wan 2.2 doesn't perform good motion for short ranges**
  - Initial testing shows limited motion capability for short duration generations
  - *From: Kijai*

- **HPS LoRA tends to redraw and add unwanted elements in I2V**
  - HPS decided to redraw monster face and adds artifacts on fur and feathers
  - *From: N0NSens*

- **MPS LoRA seems to work better for I2V without unwanted artifacts**
  - User reports MPS gives good results compared to HPS artifacts
  - *From: SonidosEnArmonía*

- **Resolution affects motion quality - higher resolution prevents slow motion**
  - 832x480 produced slow motion, but 960x544 and higher gave real-time motion
  - *From: N0NSens*

- **Uni3C can work with T2V by padding with zeros**
  - Simple solution to get Uni3C working with T2V despite shape mismatches
  - *From: Kijai*

- **VACE already works with A14B low noise model**
  - People want VACE for A14B 2.2 high noise model specifically
  - *From: Kijai*

- **Infinite Talk + silent audio + unianimate creates endless pose generation**
  - Combining these allows continuous pose-driven video without audio
  - *From: Kijai*

- **LoRA strength affects likeness vs plastic skin appearance**
  - More shift gives more likeness but more plastic-like skin texture
  - *From: scf*

- **LoRAs work better when merged directly into model node vs using setLoras**
  - Better likeness achieved by setting LoRA into model input with merge option activated
  - *From: mamad8*

- **VACE can't be used with SEGS detailer directly but works with core nodes**
  - Core nodes work for latent inpainting with Wan models, but Impact Pack SEGS detailer has compatibility issues
  - *From: Dita*

- **Radial attention provides significant speed improvements in InfiniteTalk workflows**
  - Nearly 2 minute gain per 81 frame batch speed-up when using radial attention with InfiniteTalk+FantasyPortrait
  - *From: mdkb*

- **HuMo model released - 17B parameters based on Wan 14B with audio layers**
  - It's basically wan 14b + audio layers, trained on 97-frame videos at 25 FPS, could work as drop-in replacement for Phantom without audio
  - *From: yi*

- **LightX2V LoRA at higher strengths creates overexaggerated facial expressions**
  - Using LightX lora to 1.2 or 1.5 with fast wan creates crazy facial movement and overexaggeration
  - *From: VRGameDevGirl84(RTX 5090)*

- **5B model can train LoRAs very fast on 11GB VRAM**
  - Can train on fairly large dataset and high resolution with 5B model using default DP settings on 11GB VRAM
  - *From: crinklypaper*

- **Block swap can be increased from default 20 to 40 for better memory management**
  - Default is set to 20 but can go up to 40
  - *From: Kijai*

- **Torch compile reduces memory use significantly when available**
  - Disabled by default but reduces memory use quite a bit if you can use it
  - *From: Kijai*

- **GGUF versions use half the RAM of fp16**
  - Q8 GGUF uses half the memory compared to fp16
  - *From: Kijai*

- **HuMo uses I2V structure unlike Phantom**
  - Instead of putting refs in noise latent, you put them in I2V channel as last frames
  - *From: Kijai*

- **Fast mode quality impact varies by model version**
  - Not bad at all in 2.2, but terrible in 2.1
  - *From: Kijai*

- **bf16 performs better than fp16 in Wan video model loader**
  - bf16 latents with too few steps already contain a fully formed face while fp16 is more of a cloud with a nose
  - *From: Hoernchen*

- **e5m2 works better for 2.2 than it does for 2.1**
  - Significant difference in prompt adherence, e5m2 being better than e4m3
  - *From: Kijai*

- **Disabling LightX2V LoRA can improve InfiniteTalk likeness**
  - Removing LightX LoRA improves quality and likeness but may require different CFG/steps
  - *From: BecauseReasons*

- **FastWan T2V at strength 1.0 performs better than LightX2V I2V LoRA**
  - Better than using LightX2V i2v lora in InfiniteTalk with FantasyPortrait, maintains speed boost with less consistency changes
  - *From: mdkb*

- **25fps works better for lipsync than 24fps**
  - User found that lipsync drifted at 24fps but was spot on at 25fps
  - *From: mdkb*

- **Wan 2.2 Fun VACE modules released**
  - New VACE modules for Wan 2.2 from Fun team (Alibaba PAI), includes high and low noise variants
  - *From: JohnDopamine*

- **Fun VACE works out of the box**
  - The new Fun VACE model works without requiring new implementation in wrapper
  - *From: Kijai*

- **Multiple reference images work with concatenation**
  - Can concatenate multiple reference images into one image for better control
  - *From: Kijai*

- **Frame extension and outpainting work with Fun VACE**
  - Temporal inpainting and outpainting functionality confirmed working
  - *From: Kijai*

- **Video continuations work better with Fun VACE 2.2**
  - User reported better results for FFLF (First Frame Last Frame) with Fun VACE compared to regular Fun InP
  - *From: Cseti*

- **Control + start/end frame combination possible**
  - Can mix control images with start/end frames in VACE input using mask to mark specific frames
  - *From: Kijai*

- **Wan 2.2 VACE works on high noise which previous VACE couldn't do**
  - VACE 2.2 can handle high noise side in addition to low noise, expanding functionality
  - *From: Kijai*

- **VACE 2.2 has better reference adherence and detail than 2.1**
  - Image quality and detail preservation improved in new version
  - *From: ingi // SYSTMS*

- **VACE 2.2 shows reduced color shifting issues compared to 2.1**
  - Multiple users report better color consistency in extended generations
  - *From: Daflon*

- **HuMo works better than Phantom even without audio functionality**
  - Character consistency improved over previous models
  - *From: Kijai*

- **Parallel inference exists in Alibaba's repository code**
  - Code analysis shows parallel processing capabilities
  - *From: HeadOfOliver*

- **VACE 2.2 uses black background with white lines for line art/canny work**
  - Different from previous versions that used white background
  - *From: Rishi Pandey*

- **Higher resolution reduces color shifting in VACE**
  - Tests showed less color degradation at higher resolutions
  - *From: Hashu*

- **GGUF models have compatibility issues with Wan wrapper**
  - Some GGUF models show different shapes/model detection issues causing stride errors, while native ComfyUI works fine
  - *From: xwsswww*

- **HuMo audio issue fixed**
  - Fixed single GPU code for parallel attention which wasn't accounting for shorter audio sequence length
  - *From: Kijai*

- **Context windows work in HuMo but cause drastic shifts**
  - Only 16 overlap tested, creates significant changes between segments
  - *From: Kijai*

- **VACE 2.2 color amplifies green during processing**
  - Color degradation occurs through multiple workflow passes, particularly green amplification
  - *From: mdkb*

- **New VACE has masking improvements but edge bleeding issues**
  - High noise model works great with masking, but expanded masks create grey alpha edges
  - *From: yo9o*

- **uni3c stabilizes the context windows**
  - Using uni3c helps with context window stability in WAN video generation
  - *From: Kijai*

- **HuMo works as T2V too without reference images**
  - HuMo can function as text-to-video by using fully black pixels and mask in the I2V channel
  - *From: Kijai*

- **HuMo + InfiniteTalk combination works**
  - Proof of concept showing HuMo can work with InfiniteTalk using silent audio for 3 context windows, maintaining I2V functionality
  - *From: Kijai*

- **32 overlap gives better results**
  - Using 32 overlap in context windows produces improved video quality
  - *From: Kijai*

- **VACE 2.2 works with context windows**
  - Context windows are functional with VACE 2.2 but slow things down exponentially
  - *From: cyncratic*

- **fp8 scaled from fp32 slightly better than from fp16/bf16**
  - Quantization quality is improved when done from fp32 source rather than fp16 or bf16
  - *From: Kijai*

- **LoRA strength varies by type for Wan 2.2 High Noise models**
  - Mechanical LoRAs like lightx2v and Pusa use strength higher than 1.0, while style and normal LoRAs use under 1.0 strength
  - *From: Canin17*

- **Whip pan camera prompting works reliably in I2V**
  - Camera prompting generally has problems in I2V, but 'whip pan' seems to work consistently for quick camera movements
  - *From: N0NSens*

- **First frame improves VACE results when it matches controlnet**
  - First frame always makes things better if it matches the first frame of your control
  - *From: Kijai*

- **Default Chinese negative prompt blocks anime style**
  - Default negative prompt contains 'artwork, style, painting' which blocks anime/cartoon styles - these should be removed when doing anime
  - *From: Kijai*

- **640x960 performs better than 720x1280 for context windows**
  - 640x960 works better than 720x1280 and is much faster - 20 sec clip took 15 min vs 25 min for 720
  - *From: aidiffuser*

- **Installing xformers made VAE decode 3x faster**
  - User reported significant speed improvement in VAE decoding after installing xformers
  - *From: Stad*

- **Radial attention provides significant speed boost**
  - Test showed 170.37 seconds with radial attention vs 316.06 seconds without it, plus requires resolution change from 1024x512 to 1024x576
  - *From: VRGameDevGirl84(RTX 5090)*

- **Pusa improves face quality even when used outside intended workflow**
  - Adding Pusa LoRA alongside LightX improved face quality, though this may be due to affecting weights rather than intended Pusa functionality
  - *From: Gleb Tretyak*

- **Phantom does likeness very well**
  - User noted that Phantom model performs well for character likeness
  - *From: xwsswww*

- **LightX craps out S2V quality**
  - Testing showed LightX significantly degrades S2V (speech-to-video) output quality and kills movement
  - *From: burgstall*

- **VACE 2.2 Fun supports proper multi-controlnet blends**
  - Depth + normal + lineart controlnets can now be properly blended, especially useful with style transfer
  - *From: yo9o*

- **Native VACE implementation is much faster than wrapper**
  - 17s/it for 50 frames at 1430x1080 in native vs 38s/it in wrapper
  - *From: yo9o*

- **UNIPC sampler helps with smoke/floating artifacts**
  - Changing sampler to UNIPC reduced unwanted floating elements in generations
  - *From: Flipping Sigmas*

- **Gray (0.5 or 127 RGB) is the neutral value for VACE control frames**
  - Gray is considered neutral/empty for inpainting, not black or white
  - *From: Kijai*

- **Workaround for dots problem with open pose in VACE 2.2**
  - Disable face detection in open pose, use result with infinite talk for v2v with face but no dots
  - *From: 𝕯𝖗. 𝕸𝖆𝖈𝖆𝖇𝖗𝖊 ☠*

- **Stand-in and Unianimate LoRAs add new layers to models**
  - These are special cases that modify model architecture, not just weights like normal LoRAs
  - *From: Kijai*

- **Combining VACE 2.2 with Phantom gives better results**
  - Using VACE 2.2 for high noise and Phantom for low noise produces superior output
  - *From: Ablejones*

- **HuMo 1.7B works with CausVid LoRA (bidirect)**
  - The HuMo 1.7B model is compatible with the bidirectional CausVid LoRA for improved performance
  - *From: Kijai*

- **HuMo 1.7B architecture details**
  - HuMo 1.7B is 1.3B Wan + audio proj + audio crossttn layers, behaves like Phantom by having reference at end of noise, unlike bigger HuMo which is I2V model with refs in I2V extra channels
  - *From: Kijai*

- **Florence integration with Wan**
  - Florence can be used to enhance prompts for Wan generation, with comparison showing similar results at high denoise 0.6
  - *From: N0NSens*

- **Speed LoRAs work with HuMo**
  - LightX, FastWan, and Pusa LoRAs are compatible with HuMo model for faster generation
  - *From: VRGameDevGirl84(RTX 5090)*

- **Better Infinite Talk results with specific settings**
  - Wan2.1_14B_FP8 with sageattention, Audio Scale 1.40, Audio CFG 1.50, KSampler 4 steps, CFG 1.50, Shift 5, dpm++_sde produces improved results
  - *From: NC17z*

- **Shift modifies the sigma curve**
  - Higher shift can add more detail but also unwanted elements, lower steps can benefit from higher shift
  - *From: Kijai*

- **Using shift for likeness/consistency**
  - Shift adds more detail/changes which wouldn't be best for maintaining likeness/consistency especially for i2v and vid2vid with VACE or Phantom
  - *From: xwsswww*

- **Humo 1.7B VRAM usage**
  - Humo 1.7b stays under 7gb VRAM usage for 480x832x205 frames (besides VAE decoding stage)
  - *From: patientx*

- **Humo character consistency**
  - Humo does a great job at keeping character consistency when using a photo as reference
  - *From: VRGameDevGirl84(RTX 5090)*

- **WAN output enhancement with SDXL AnimateDiff**
  - Running WAN output through SDXL animatediff at low denoise can improve WAN smudging
  - *From: VK (5080 128gb)*

- **Lora loading behavior change**
  - When using unmerged Loras, system never loads anything, just applies them on the fly - this is couple of months old functionality
  - *From: Kijai*

- **Per-step lora strength control**
  - When using unmerged loras, you can input a list of floats corresponding to each step as the lora strength
  - *From: Kijai*

- **ComfyUI memory management improvement**
  - Comfy appears to have fixed wan model ram memory management, doesn't go past 60gb now with 3 samplers, previously would max RAM to 90+ and crash WSL2
  - *From: pagan*

- **VACE 2.2 has better results with CFG compared to CFG 1**
  - Much better quality when using CFG instead of CFG 1
  - *From: Kijai*

- **Wan 2.1 still superior for faces compared to 2.2**
  - 2.1 rules for faces, better facial performance than 2.2
  - *From: chrisd0073*

- **VACE 2.2 has hidden relight feature**
  - Better results than 2.1, will relight foreground to match background when replacing BG with grey area if input mask not used
  - *From: chrisd0073*

- **ComfyUI commit e42682b provides major improvement**
  - Major improvement at least on native, commit focuses on memory optimization
  - *From: pagan*

- **Torch.compile provides 20-30% speed improvement and less VRAM usage**
  - Makes code more efficient, usually ends up using less VRAM and executes 20-30% faster
  - *From: Kijai*

- **Merge LoRAs helps with memory management**
  - When merge loras on for wan 2.2, can generate 129 frames without context options, but with it off same frames cause OOM
  - *From: Bleedy (Madham)*

- **Radial attention provides speed improvement**
  - About 10 minutes faster generation but uses slightly more RAM and VRAM
  - *From: Charlie*

- **Wan 2.2 handles vertical video format very well**
  - Model can handle vertical aspect ratios nicely, better than expected
  - *From: mallardgazellegoosewildcat*

- **Video models work best with cinematic-style input images**
  - Images that look like movie stills with aspect ratio, black bars, anamorphic lens and cinematic color grading match training data best since they trained on half of hollywood
  - *From: mallardgazellegoosewildcat*

- **Wan 2.2 quality improvement over 2.1**
  - 2.2 is quite a lot better than 2.1, getting closer to stepvideo/magi levels with only subtle warping
  - *From: mallardgazellegoosewildcat*

- **Wan 2.2 low noise model is nearly identical to Wan 2.1**
  - The high noise model is what makes 2.2 good, not the low noise. Testing 2.2 low noise T2V vs 2.1 T2V produces almost identical results
  - *From: Kijai*

- **VACE ref uses position too strongly**
  - When using VACE references, the positioning control can be overly rigid
  - *From: Kijai*

- **Blockswap transfers are very fast on some systems**
  - User reported transfer times of 0.0002s, compute times of ~0.27s, and to_cpu times of ~0.0008s with DDR4 RAM
  - *From: lostintranslation*

- **Optimal block count for 81 frames is around 30**
  - 30 blocks swapped pegs VRAM at 95% and seems to be the fastest option, only a few seconds faster than other counts
  - *From: lostintranslation*

- **HPS 2.1 reward LoRA was causing anime-style slop look in VACE outputs**
  - Disabling HPS 2.1 significantly improved cartoon style output and character consistency
  - *From: Gleb Tretyak*

- **Wan 2.2 VACE works better with blurred masks compared to 2.1**
  - In 2.1, blurred masks always broke, but 2.2 handles them better for complex shots
  - *From: chrisd0073*

- **Using CFG scheduling causes first step to go through all blocks twice**
  - This is normal behavior when CFG is used for the first step
  - *From: Kijai*

- **Lucy Edit model is built on Wan 5B**
  - DecartAI's Lucy Edit model uses Wan 5B as foundation but quality reflects 5B limitations
  - *From: HeadOfOliver*

- **Wan 2.2 Animate model released**
  - 14B parameter model for character animation, 78 frames (77+1 reference), two modes: image animation or subject replacement into reference video
  - *From: DawnII*

- **Wan-animate trained for 78 frame chunks**
  - Can go longer but in 78 frame chunks
  - *From: DawnII*

- **Face control uses raw facial image as driving input**
  - Avoids manually defined facial signals, uses skeletal information to locate and crop facial region, spatially compresses facial image into 1D latent to reduce identity-specific information
  - *From: DawnII*

- **Wan-animate encoder takes limb delta into account**
  - Their encoder actually takes into account limb delta between the reference and subject
  - *From: DawnII*

- **Mask format is different for Wan-animate**
  - Made a node to transform mask to that style, it does not work with normal mask
  - *From: Kijai*

- **Wan-animate is based on same structure as 2.1 I2V**
  - Same structure as 2.1 I2V, clip embeds and all, they call it 2.2 but honestly it's same structure
  - *From: Kijai*

- **Rank 256 LoRA shows significant quality improvement**
  - Character is stiff and looks straight on rank 32, on 256 he's looking down, clothes move better, everything is more alive
  - *From: 𝕯𝖗. 𝕸𝖆𝖈𝖆𝖇𝖗𝖊 ☠*

- **Frame window size and num_frames must be equal when using context options**
  - This is IMPORTANT for proper operation
  - *From: Kijai*

- **Default frame_window_size is 77 because refs are added to latents making that 81 for the model**
  - Original method degrades over time
  - *From: Kijai*

- **Wan Animate is closer to 2.1 architecture**
  - Lora 2.2 are not compatible with wan animate
  - *From: Kijai*

- **Reference frames are included and later cut, similar to VACE**
  - This explains why input frames become +4 during sampling
  - *From: Kijai*

- **Relighting LoRA .safetensors version doesn't work, but .ckpt version works**
  - Keys are identical when converted but still different behavior
  - *From: Kijai*

- **LightX2V can and should be used at 1.5 strength or higher**
  - Testing shows it works well at elevated strengths
  - *From: Kijai*

- **Wan 2.2 Animate has 2 new model inputs: face pixels and pose latents**
  - The model uses vitpose for pose detection and takes face crops at hardcoded 512x512 resolution
  - *From: Kijai*

- **Face detection failure causes major issues**
  - Model absolutely sucks when face is not detected, often happens when input frame count doesn't follow the Wan 4+1 frame rule
  - *From: Kijai*

- **Window size is constant at 77 frames**
  - Uses 77 + 77 + 77 windowing, can't do partial windows. If you have frames between 77 and 154, you'll always get 154 frames output
  - *From: Kijai*

- **Frame count must follow specific rules**
  - For windowing to work properly, total frames should be 161 (not 162) due to the +1 rule. 81 window with 162 total causes tensor size mismatch errors
  - *From: ˗ˏˋ⚡ˎˊ-*

- **14B model significantly outperforms 5B**
  - 14B approaches stepfun/magi level quality at half the size, has excellent 3D awareness and handles foreground objects well. 5B model destroys sharpness and has poor quality
  - *From: mallardgazellegoosewildcat*

- **Motion encoder and face components cannot be quantized**
  - GGUF conversion fails because motion encoder and face processing parts must remain unquantized
  - *From: Kijai*

- **Frame window size affects generation success**
  - 161 frames with window 77 gives error, but with window 81 works. 171 frames with window 81 errors. Seems if it goes beyond two windows, errors occur
  - *From: theUnlikely*

- **WanAnimate masking breaks without face images**
  - Masking simply breaks if there's no face images given - workaround is to pass empty image for every frame when doing masking without face
  - *From: Kijai*

- **bf16 gives better quality than fp8**
  - bf16 720p looks better than fp8, though not much better but indeed better
  - *From: slmonker(5090D 32GB)*

- **Longer frame videos improve quality**
  - Changed input video from 16fps to 29.97fps (close to 89 frames) and is way better - this model needs more room
  - *From: Nekodificador*

- **LightX at 10 total steps causes snow artifacts**
  - Bumped lightx from 8 total to 10 total and got snow. Before it wasn't a case. Maybe 10 is too much
  - *From: Gleb Tretyak*

- **Model can do more than 81 frames pretty well**
  - Seems the model also can do more than 81 frames pretty well just as it is
  - *From: Kijai*

- **WanAnimate pupil/gaze direction doesn't track properly by default**
  - Setting face strength to zero fixes the eye gaze problem, suggesting it's something in the face processing
  - *From: A.I.Warper*

- **WanAnimate uses no CFG by default**
  - Default settings are 20 steps, cfg 1.0, shift 5.0. Model might be CFG disabled.
  - *From: Kijai*

- **WanAnimate default prompt is just Chinese text**
  - The prompt is literally just `视频中的人在做动作` (person in video doing actions)
  - *From: Kijai*

- **Face pixels set to -1 for uncond in WanAnimate code**
  - In their code they set face pixels to -1 for unconditional generation
  - *From: Kijai*

- **2.1 LoRAs work with WanAnimate**
  - WanAnimate is based on 2.1 i2v, so 2.1 loras do have an effect
  - *From: Piblarg*

- **First step with CFG gives better likeness in WanAnimate**
  - Using CFG on first step improves character likeness as expected
  - *From: Kijai*

- **Pose input accepts depth maps mixed in**
  - Really cool for backward facing scenes that pose gets wrong otherwise
  - *From: Clément*

- **Model performs poorly with frame counts under 81**
  - Some may work, but most not well, so it's safer to do the full count and clip
  - *From: Kijai*

- **CFG distillation can improve final quality**
  - Found as far back as animatediff/lcm stuff, though not completely sure why
  - *From: Piblarg*

- **Empty prompting works fine for wan animate**
  - Prompting can break the references pretty badly if not aligned
  - *From: Piblarg*

- **HUMO works as regular i2v model**
  - Found randomly while experimenting and swapping models
  - *From: ▲*

- **WanAnimate preprocessing has many more features in original code**
  - Original code does quite a bit more than workflow does, includes option to use Flux Kontext to repose reference, pose retargeting/scaling etc
  - *From: Kijai*

- **Frame count should be multiples of 77 to avoid memory errors**
  - Reference adds extra latent making model process one latent larger, so with 77 it processes 81 in reality
  - *From: Kijai*

- **WanAnimate embeds node uses ~5GB VRAM for 81 frames**
  - Memory improved in recent updates, not even passing 10GB VRAM used with 81 megapixel frames
  - *From: Kijai*

- **Snow artifacts are related to sigma schedule**
  - If the high noise model starts doing work at lower sigma values (below 0.85), it hands off noisy particle-like stuff to the low noise model, which interprets it as snow
  - *From: Instability01*

- **Text embeddings are cached per prompt**
  - Each cache file name is a hash of the prompt, helps save time on encoding
  - *From: Kijai*

- **Dimensions must be divisible by 16**
  - Width * height * frames divisible by 16 for resolution compatibility
  - *From: Kijai*

- **Mask block size affects black square artifacts**
  - Increasing mask block size and expanding the mask prevents black artifacts if mask is too close to subject
  - *From: xwsswww*

- **First frame flash fixed in single window mode**
  - Fixed issue where flash occurred without bg_images when doing single window
  - *From: Kijai*

- **Lucy Edit recently updated and improved**
  - Repository updated 1 hour ago, quality got better and less blurry
  - *From: Stad*

- **patientx created GGUF quantizations (q3, q4, q6, fp8_e5m2) of WanAnimate model**
  - Testing shows q4 provides good balance of quality vs memory usage
  - *From: patientx*

- **piscesbody created modified WanAnimate masking using Qwen2.5VL for tagging**
  - 155 frames completed in 30 seconds sampling time, claims better results than Florence2
  - *From: piscesbody*

- **Phantom + VACE 2.2 combination can work**
  - Used Phantom fp8_e5m2 model with VACE 2.2 Low Noise module in FFLF workflow
  - *From: mdkb*

- **SkyReels can achieve 24fps with 121 frames using FFLF**
  - Alternative method for longer duration videos without VACE
  - *From: mdkb*

- **res_multistep + bong_tanget samplers add more movement to Wan 2.2**
  - Tested with fast movement clips
  - *From: Drommer-Kille*

- **Removing background and mask makes WanAnimate work as stronger VACE/Fun controlnet**
  - When bg image and mask are removed, the animation becomes a stronger controlnet
  - *From: slmonker(5090D 32GB)*

- **All image inputs must be divisible by 16 for WanAnimate to work with long videos**
  - If dimensions aren't divisible by 16, you can only run videos with exactly 77 frames
  - *From: BestWind*

- **WanAnimate uses hardcoded input resolutions**
  - VitPose ONNX model has hardcoded input res of 256x192, face model input is 512x512, causing warped crops
  - *From: Kijai*

- **Face adapter blocks moved to main blocks for VRAM reduction**
  - WanAnimate face adapter blocks are now part of main blocks (every 5th block, total of 8) and included in block swap
  - *From: Kijai*

- **Native torch RMSNorm is 9x faster when available**
  - Updated code uses native torch RMSNorm in nightly builds, RMS norm itself is 9x faster but not a major bottleneck
  - *From: Kijai*

- **WAN 2.2 Animate has 'jiggle physics' effects on scantily clad characters in dancing videos**
  - Noticed during testing with dancing video generations
  - *From: patientx*

- **Face strength setting affects mask quality significantly**
  - Face strength needs to be 1.0 or it screws the mask
  - *From: Kijai*

- **Color matching can cause terrible results on long video generations**
  - Setting to 'Disabled' works better for long videos
  - *From: CaptHook*

- **Window size calculation affects render times significantly**
  - For 113 frames, changing window size from 81 to 57 reduced render time from 11 min to 7 min
  - *From: CaptHook*

- **Higher resolution improves likeness, accurate motion and consistency**
  - WanAnimate works well with higher resolution, same with VACE and Phantom models
  - *From: xwsswww*

- **Wan 2.2 low is a finetuned version of 2.1**
  - Either 2.1 or 2.2 LoRAs work fine with Animate since base layers are the same for likenesses
  - *From: xiver2114*

- **Wan Animate is wan2.1 i2v so wan2.1 t2v will work as well**
  - Base layers compatibility between model versions
  - *From: xiver2114*

- **10 seconds video generation capability confirmed**
  - New model will support 10 second video generation
  - *From: 青龍聖者@bdsqlsz*

- **Frame window size doesn't need to encode all frames at once**
  - Can use frame window size of 77 instead of 113 frames to reduce VRAM usage
  - *From: Kijai*

- **Frame count shouldn't make huge difference in VRAM use on VAE, but resolution does**
  - VAE VRAM usage is more dependent on resolution than frame count
  - *From: Kijai*

- **Video resolution must be divisible by 8**
  - 270p doesn't work, but 272p works fine for video generation
  - *From: traxxas25*

- **Wan 2.1 T2V LoRAs work with Wan 2.2 Animate**
  - Cross-compatibility confirmed between model versions
  - *From: scf*

- **WanAnimatePreprocess node can auto-detect faces and poses**
  - Automatically gets face from pose detection, provides points for SAM2 without manual editing
  - *From: Kijai*

- **Animal pose works with WanAnimatePreprocess**
  - Successfully tested with animal poses and background replacement
  - *From: Hashu*

- **Context windows prevent burn but cause background shifts**
  - Trade-off between temporal consistency and background stability
  - *From: Kijai*

- **BF16 uses much more RAM than FP8**
  - User switched from bf16 to fp8 and saw significant RAM reduction
  - *From: slmonker(5090D 32GB)*

- **Wan Animate works better with single reference images**
  - Multiple reference images (4) cause issues like extra arms, single image works fine
  - *From: Kijai*

- **Context windows create brightness changes when shifting**
  - Sudden brightness changes occur when shifting frame windows in context generation
  - *From: WhimsicalZ*

- **LoRAs work better with stylized mode**
  - The reward loras (MPS/HPS) perform better when using stylized mode
  - *From: Kijai*

- **VACE masking issues have specific causes**
  - Too small mask blocks, not using face images, or face strength < 1.0 cause masking artifacts in output
  - *From: Kijai*

- **Wan Animate uses Flux preprocessing for pose mode**
  - In pose-only mode vs replace mode, Wan Animate preprocesses reference with Flux Kontext to extract pose information
  - *From: ˗ˏˋ⚡ˎˊ-*

- **FastWan + LightX allows 2-step generation**
  - Using FastWan and LightX LoRAs together enables good quality video generation in just 2 steps
  - *From: VRGameDevGirl84(RTX 5090)*

- **24fps works better than 16fps for Wan Animate**
  - Traditional 16fps causes issues, switching to 24fps gives much better results
  - *From: NC17z*

- **Wan 2.2 model is uncensored and follows prompts well**
  - Model follows prompts nicely and follows image identity better than previous versions
  - *From: Lodis*

- **Virtual try-on works well with new qwen edit model**
  - Virtual try-on works fucking awesome on the new qwen edit model
  - *From: Lodis*

- **3 image inputs work but quality degrades**
  - Technically works with 3 image inputs, but quality starts to degrade a bit, maybe two images is ideal combo
  - *From: Lodis*

- **Wan 2.2 works with only 4 steps**
  - Did first tests using only 4 steps with good results for both realistic and anime style
  - *From: Lodis*

- **New face image capture works very well for fast-moving faces**
  - The new face image capture seems to work very well. You notice the difference with faces that move around the frame fast
  - *From: mightynice*

- **Animate model does lip sync better than VACE 2.1**
  - Animate does lip sync better than vace 2.1, does some tests and does ok
  - *From: 🦙rishappi*

- **WAN 2.1 base works with bbox for non-human subjects**
  - 2.1 base plus with bbox only works for tracking non-human subjects, while original WanAnimate code/demo doesn't do non-humans
  - *From: Kijai*

- **SAM 2.1 better than earlier versions**
  - SAM 2.1 is better than previous versions for masking
  - *From: Kijai*

- **WAN 2.5 has audio/video sync capabilities**
  - One-pass A/V sync: Wan 2.5 creates a fully synchronized video (audio/voiceover + lip-sync) from a single, well-structured prompt
  - *From: 🦙rishappi*

- **RamTorch works with WAN models**
  - Successfully got RamTorch working with wan models for memory optimization
  - *From: Benjimon*

- **Wan animate preprocessor has flux kontext step that makes ref and first frame match**
  - The preprocessing includes a kontext step using Flux to align the reference image with the first frame of video
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Wan animate does sampling twice (2x20 steps)**
  - The inference process involves two rounds of 20-step sampling
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Wan 2.2 matched Veo 3 performance for user**
  - User reports Wan 2.2 matched Veo 3 results a decent percentage of the time during testing
  - *From: mallardgazellegoosewildcat*

- **Wan 2.5 can generate multiple people speaking different languages**
  - Can prompt people to speak in any language (EN, PT, JP) and have multiple languages in one scene
  - *From: ZeusZeus (RTX 4090)*

- **Wan 2.5 has built-in native audio generation**
  - Audio is prompted directly without audio input, quality comparable to Veo 3
  - *From: ZeusZeus (RTX 4090)*

- **Wan 2.5 supports timed actions in prompts**
  - You can specify actions at specific time intervals - eg: 0s–2s: The girl holds a lipstick and applies it to her lips. 2s–5s: The girl puts down the lipstick
  - *From: 🦙rishappi*

- **Wan 2.5 has comprehensive prompt formula**
  - Prompt = Subject + Scene + Movement + Sound Description (Human Voice / Sound Effects / Background Music)
  - *From: 🦙rishappi*

- **Higher LoRA rank improves results**
  - LoRA rank 64 is better than 32 for complex captions and motion tracking. 64 helps with motion but can lead to overfitting, 32 can lead to underfitting
  - *From: Ryzen*

- **Detailed captions help LoRA diversity**
  - With detailed captions in dataset, LoRA generates different people instead of same face
  - *From: Ryzen*

- **Video models may beat image models for text-to-image**
  - Video models have way better understanding of the world than image models
  - *From: Screeb*

- **Wan 2.5 VAE has artifacts**
  - VAE artifacts present, suggesting it could be smaller than expected and using more compressive VAE to get more motion in
  - *From: mallardgazellegoosewildcat*

- **Wan 2.5 pricing structure**
  - $0.5 for 720p, $1.5 for 1080p 10 seconds
  - *From: 𝕯𝖗. 𝕸𝖆𝖈𝖆𝖇𝖗𝖊 ☠*

- **Wan 2.5 audio input limitation**
  - Only allows 5s audio input, not the full 10s (maybe pro only feature)
  - *From: Juampab12*

- **Wan 2.5 supports depth control**
  - New depth support capabilities discovered in Wan 2.5
  - *From: hicho*

- **Wan 2.5 has more powerful prompt control than 2.2**
  - 2.5 offers more powerful prompt control, and when running img2vid, it is easier to generate videos that deviate significantly from the original image
  - *From: toyxyz*

- **Wan 2.5 uses MoT architecture instead of MoE**
  - Mixture of Transformers rather than Mixture of Experts architecture
  - *From: 🦙rishappi*

- **2.2 FUN VACE can create very long videos with frame overlap**
  - You can do a 3 hour long one shot with 2.2 FUN Vace using 5-20 frame overlap with padding
  - *From: seitanism*

- **Hand animation LoRA works well when retrained for 2.2**
  - Hand animation LoRA retrained for 2.2 works pretty well, though without reference image it tends to snap back every 81 frames
  - *From: ingi // SYSTMS*

- **WanAnimate supports temporal reference for extensions**
  - Similar to InfiniteTalk, it's trained to use temporal reference allowing for automatic extensions using 2 extensions
  - *From: Kijai*

- **WanAnimate works better at 12fps than 24fps for pose-driven videos**
  - Had some pose issues with 24fps
  - *From: Kijai*

- **Multiple face references for WanAnimate cause errors**
  - Last attempt at multiple references resulted in errors, not sure if they're supported
  - *From: Dever*

- **Wan 2.5 lipsync is more natural than alternatives**
  - Much more natural looking than InfiniteTalk or WanAnimate
  - *From: orabazes*

- **Back shot reference images help with character turn-arounds**
  - Using a back shot reference actually helped achieve better turn-around results in pose-driven generation
  - *From: Gigi8*

- **Wan 2.5 supports both audio generation and audio input**
  - You can have the model generate audio or provide audio to drive the generation
  - *From: DawnII*

- **WanVideo Animate embeds accepts ref_images input, might work with multiple images**
  - The input shows 'ref_images' but tooltip says 'Image', unclear what happens with 2 separate images
  - *From: fearnworks*

- **Can train Wan 2.2 LoRAs with images only**
  - Training on images can transfer some learning to video but may harm movement, decreases resource cost significantly
  - *From: fearnworks*

- **Fun VACE 2.2 keeps up with faster motion better than VACE 2.1**
  - Main benefit of 2.2 Fun VACE is handling much faster motion
  - *From: Kijai*

- **Texture swimming is fundamentally a VAE compression issue**
  - VAE compression unable to produce temporally-stable high frequency details, particularly noticeable with high-frequency details like dinosaur skin
  - *From: Screeb*

- **Wan 2.2 low noise LoRAs sometimes work with Wan 2.1**
  - Made things saturated and detailed in a weird way when tried with t2v 2.1 distill
  - *From: hicho*

- **TaylorSeer-Lite provides significant speedup for Wan 2.2**
  - 3.05x speedup - 386s vs 1176s for 81 frames generation on RTX 5090, nearly zero VRAM increase
  - *From: scf*

- **Wavespeed Wan 2.5 fast is better quality than regular Wan 2.5 for i2v**
  - Also uncensored, possibly uses distillation or sliding window kernel
  - *From: ZeusZeus (RTX 4090)*

- **Modern distillation methods often produce higher quality than original models**
  - Distillation is essentially an additional training run with opportunity to improve on parent model priors
  - *From: mallardgazellegoosewildcat*

- **Wan 2.5 architecture upgrade explained**
  - Named 2.5 after 2.2 because of major architecture upgrade - called Mixture of Transformers (MoT) instead of MoE
  - *From: toyxyz*

- **QwenImage + Wan2.2 creates effective anime generation**
  - Combination produces high quality anime videos with low fail rate
  - *From: Drommer-Kille*

- **Wan2.2 has high anime training bias**
  - After 360 anime i2v clips, fail rate is only 20%, mostly trained with anime content
  - *From: Drommer-Kille*

- **Lynx is an addon module system**
  - Uses additional modules on top of existing Wan 2.1, main weights unchanged, includes IP adapter and ref adapter
  - *From: Kijai*

- **Block swap works well with video models due to long operations**
  - Offloading can be done asynchronously during long video operations
  - *From: Kijai*

- **Uni3c works on T2V models despite expectations**
  - Initially thought it couldn't work on T2V for architectural reasons, but testing proved it works perfectly
  - *From: Kijai*

- **VACE checks every frame of video individually, twice during processing**
  - This explains performance characteristics
  - *From: Kijai*

- **Lynx uses double encoder architecture**
  - Has both a VAE encoder and a face model encoder, plus frozen DiT blocks to get per-block embeddings
  - *From: mallardgazellegoosewildcat*

- **VACE reference adds 4 frames/single latent to start of batch**
  - This is why you see +4 frames to total at inference, can be trimmed after sampling
  - *From: DawnII*

- **WanAnimate maintains 1:1 frame count**
  - 121 frames in produces 121 frames out at 77 frame windows
  - *From: A.I.Warper*

- **VACE 2.2 main advantage is with motion handling**
  - Better at fast motion and background objects motion which was lacking in 2.1
  - *From: Izaan*

- **Cloud GPUs now over 100x cheaper than local per token**
  - When using libraries like Dynamo over enough GPUs
  - *From: mallardgazellegoosewildcat*

- **New Wan 2.2 Lightning LoRA released with enhanced camera control and motion dynamics**
  - 250928 version with improved motion dynamics, designed to work with Euler scheduler, 4 steps, shift=5, cfg=1
  - *From: yi*

- **Flowmatch_distill scheduler works better with new Lightning LoRAs than Euler**
  - Kijai showed significantly better results using flowmatch_distill schedule instead of regular Euler
  - *From: Kijai*

- **Custom timesteps for flowmatch_distill equivalent**
  - Euler/simple 4 steps with custom timesteps 999.7998, 937.5000, 833.3333, 625.0000 or linear 999, 750, 500, 250 with shift 5
  - *From: Kijai*

- **Lightning LoRA rank differences between high and low noise**
  - Low noise LoRA is rank 64 while high noise LoRA is rank 128, questioning if only high part was retrained
  - *From: Kijai*

- **T2V Lightning LoRAs work on I2V but with motion inconsistency**
  - T2V LoRAs trained on top of T2V will work for I2V but effect is always better if natively trained on the model being used
  - *From: yi*

- **New Lightning 2509 lora performs much worse as lora compared to the full model**
  - High rank (256-512) required to extract properly from dyno model, lora at rank 128 gives significantly different results
  - *From: Kijai*

- **Dyno full model changes text embed layers in addition to attention and ffn linear layers**
  - Usually doesn't affect distillation but can change results, explaining why extraction is difficult
  - *From: Kijai*

- **Lightning loras have style baked in, unlike lightx2v**
  - Same issue as AccVid and FastWan distillations, lightx2v doesn't have this problem
  - *From: Kijai*

- **LYNX uses extremely low resolution for IP adapter**
  - IP adapter uses 112x112 resolution, reference uses 256x256, fails completely on anime
  - *From: Kijai*

- **Timestep embeddings can be extracted separately to improve lora performance**
  - Extracted time_embeddings component (~360mb) can be loaded through extra_models to better match full model results
  - *From: JohnDopamine*

- **GGUF conversion possible for Wan models**
  - Can convert Wan models to GGUF format using comfyui-gguf node pack tools with llama-quantize.exe
  - *From: patientx*

- **WanAnimate trained with blocky masks**
  - The model is specifically trained to only handle blocky masks, can also work with square masks
  - *From: Kijai*

- **Context windows improve longer video generation**
  - Context windows help prevent color shifting and quality degradation in longer videos
  - *From: U̷r̷a̷b̷e̷w̷e̷*

- **Frame window size affects face consistency**
  - Going over 77 frames causes loss of face consistency despite using same seed, faces become different each time
  - *From: mdkb*

- **Context options are not compatible with WanAnim looping**
  - Error occurs when trying to use context options with WanAnim looping since it creates video in a loop
  - *From: mdkb*

- **Setting num_frames and frame_window_size equal disables looping**
  - Having frame window equal or larger than max frames disables the looping mechanism
  - *From: Kijai*

- **Wan 2.2 Palingenesis model shows better results for certain styles**
  - Comparison showed Palingenesis (on low) performed better than Dyno model (on high) for Silent Hill style generation
  - *From: patientx*

- **Uni3C works with Wan 2.2 but with limitations**
  - Works with higher strength, doesn't error with 2.2 specifically, but effect is weaker than with 2.1
  - *From: Kijai*

- **Wan Alpha generates transparent videos**
  - New Wan-Alpha model can generate videos with alpha channels for transparency effects
  - *From: Gleb Tretyak*

- **Using same image as end frame in I2V creates interesting effects**
  - When using the same image as both start and end frame in I2V workflow
  - *From: Kijai*

- **Camera render from Blender works well with Uni3C**
  - Simple Blender viewport render (no cycles/eevee) with strength 4.0 on high noise only produces spot-on animation
  - *From: xwsswww*

- **DC-AE compression technology significantly reduces inference latency**
  - The accelerated models achieve up to 14.8× lower inference latency than their base counterparts without compromising quality, and further enable 2160×3840 video generation on a single GPU
  - *From: scf*

- **DC-Gen T2I model adapted to DC-AE is available**
  - It's their T2I DC-Gen model Flux Krea adapted to DC-AE
  - *From: yi*

- **FLUX plastic skin issue comes from specific sampler choice**
  - That comes mainly with Euler sampler that all cloud services seem to use. Gradient Estimation+linear_quadratic or bong_tanget generates very different look and can get very gritty with same lora
  - *From: Drommer-Kille*

- **Wan 2.5 is 24fps**
  - wan 2.5 is 24fps btw
  - *From: hicho*

- **Wan 2.5 might be around 20-30B parameters**
  - More like 20B - 30B would be my guess
  - *From: yi*

- **Kandinsky 5.0 uses HYV VAE, qwen2.5 vl for text and fully new DiT**
  - Finally no T5 encoder, allows tuning the text encoder
  - *From: yi*

- **Kandinsky 5.0 is 2B model with larger model coming**
  - Current 2B version, larger 'Kandinsky Pro' model planned
  - *From: yi*

- **GGUF LoRA application is stronger than merged LoRAs**
  - Applied on the fly can use precision of LoRA weights vs merged
  - *From: Kijai*


## Troubleshooting & Solutions

- **Problem:** OOM errors on RTX PRO 6000 with 96GB VRAM on previously working workflows
  - **Solution:** Native WAN uses 53GB VRAM vs wrapper which was failing, suggesting wrapper memory issue
  - *From: HeadOfOliver*

- **Problem:** nag_context not supported with split_cross_attn_ffn error when using InfiniteTalk with split prompts
  - **Solution:** Can't use nag with split prompting (|) currently - need to choose one or the other
  - *From: Kijai*

- **Problem:** PUSA LoRAs causing system memory crashes on 64GB RAM
  - **Solution:** Merge the LoRAs instead of loading separately, as they're too big otherwise (8GB more to load)
  - *From: Kijai*

- **Problem:** flowmatch_pusa scheduler doesn't work for split sampling
  - **Solution:** Use add noise instead, scheduler zeros sigma too early when generation isn't done
  - *From: Kijai*

- **Problem:** InfiniteTalk extra talking frames after audio ends
  - **Solution:** Either cut frames to exact audio length or add silence to end of audio for natural fade
  - *From: Kijai*

- **Problem:** FP8 LoRAs causing errors
  - **Solution:** Convert FP8 LoRAs by merging them or use bf16 versions
  - *From: Kijai*

- **Problem:** End latent functionality not working properly
  - **Solution:** Use ugly workaround - encode image duplicated 5x then pick last latent for full latent
  - *From: Kijai*

- **Problem:** Slow motion in Wan 2.2 generations
  - **Solution:** Use CFG and proper LoRA strengths to fix motion issues
  - *From: WorldX*

- **Problem:** High RAM usage in ComfyUI
  - **Solution:** Create swap file on NVME drive to help flush cache quicker
  - *From: dg1860*

- **Problem:** OOM errors with InfiniteTalk at higher resolutions
  - **Solution:** Lower frame count or use blockswap settings to manage VRAM
  - *From: Ubertummen*

- **Problem:** Widget to String node showing wrong values
  - **Solution:** Use primitive node instead of float constant as it modifies widget directly
  - *From: Kijai*

- **Problem:** Unexpected jumps at video start
  - **Solution:** Use proper latent trimming and blending instead of concatenation
  - *From: dipstik*

- **Problem:** Inconsistent VRAM usage on Windows with Triton
  - **Solution:** Clear triton caches at C:\Users\<username>\AppData\Local\Temp\torchinductor_<username>\triton\ and C:\Users\<username>\.triton
  - *From: Kijai*

- **Problem:** Random OOM errors after PyTorch/Triton updates
  - **Solution:** Update to latest nightly PyTorch and clear all triton caches
  - *From: Kijai*

- **Problem:** Pusa generating completely different content from reference
  - **Solution:** Set Pusa LoRA strength to minimum 1.4, avoid duplicating start frame
  - *From: Kijai*

- **Problem:** torch.OutOfMemoryError with 'Allocation on device'
  - **Solution:** This indicates VRAM issue, not RAM. High-vram flag only useful when you have more VRAM than RAM
  - *From: Kijai*

- **Problem:** GPU disconnection and PC freezing during generation
  - **Solution:** Could be thermal throttling - check GPU temperatures and replace thermal pads if needed. One user fixed crashing 3090 by replacing thermal pads
  - *From: Ashtar*

- **Problem:** Cannot access free variable 's2v_pose' error
  - **Solution:** Update WanVideoWrapper nodes - this was a bug that has been fixed
  - *From: Kijai*

- **Problem:** WAN 2.2 VAE not loading completely on GPU
  - **Solution:** Use LTX Tiled VAE Decoder which allows complete loading and faster processing
  - *From: l҈u҈c҈i҈f҈e҈r҈*

- **Problem:** 64GB RAM maxing out making ComfyUI unusable
  - **Solution:** Create page file on NVME drive instead of SATA and clear triton caches - massive speed improvement
  - *From: dg1860*

- **Problem:** System hard crashes with CPU and Disk Cache together
  - **Solution:** Change to GPU processing and disable disk cache
  - *From: blake37*

- **Problem:** Video encoding too slow
  - **Solution:** Change WanVideo Encode from CPU to GPU processing for much faster encoding
  - *From: Dever*

- **Problem:** WanVideoSampler 'dtype' KeyError
  - **Solution:** Try using e4 scaled quant model or e5 versions depending on GPU
  - *From: crinklypaper*

- **Problem:** Weird generation outputs - washed out, no movement, extra people
  - **Solution:** Roll back to version 1.3.1
  - *From: screwfunk*

- **Problem:** P2 state messes up generation in Windows
  - **Solution:** Disable P2 state in Nvidia Profile Inspector
  - *From: Kenk*

- **Problem:** VSH combine takes 2 minutes when multiple ComfyUI windows open
  - **Solution:** Close all other ComfyUI tabs in Chrome, sometimes need to close all and reopen fresh tab
  - *From: Kenk*

- **Problem:** System crashes and hangs
  - **Solution:** Generate video, wait few minutes before generating next, avoid queuing
  - *From: Drommer-Kille*

- **Problem:** OOM issues after first generation run
  - **Solution:** Set model loaders to offload_device instead of main_device
  - *From: HeadOfOliver*

- **Problem:** 36 vs 16 channel mismatch error
  - **Solution:** Use correct model type - use I2V node for I2V models, T2V node for T2V models
  - *From: Kijai*

- **Problem:** Broken unmerged LoRAs
  - **Solution:** Update to latest version after Kijai's sleep-deprived commit fix
  - *From: Kijai*

- **Problem:** UniAnimate pose KeyError: 'dtype'
  - **Solution:** Kijai investigating but needs more info on models used
  - *From: Gigi8*

- **Problem:** GPU crashes and 'GPU is lost' error
  - **Solution:** Check power connectors, may be hardware issue with PSU or connections
  - *From: Drommer-Kille*

- **Problem:** Channel mismatch error when using Pusa with I2V
  - **Solution:** Wan 2.2 I2V + Pusa doesn't work on current main, it works on commit 56e3366c26e610a12e7216f49e745f5a7b4929b4
  - *From: Dever*

- **Problem:** Context window indices error with Pusa
  - **Solution:** Try different window size / overlap / stride - it's sensitive to frame counts
  - *From: Kijai*

- **Problem:** Wrong VAE causing channel errors
  - **Solution:** Make sure using correct VAE - 2.2 vae fp16
  - *From: Kijai*

- **Problem:** Don't use I2V node with multi-image context
  - **Solution:** Don't use the I2V node if you are using multi-image context
  - *From: Kijai*

- **Problem:** 1080p not supported dimension
  - **Solution:** 1080 exactly is not supported dimension in VAE because it doesn't divide by 16
  - *From: Kijai*

- **Problem:** TAESD preview not working in native workflows
  - **Solution:** Warning about 'models/vae_approx/None' - TAESD technically slows down generation but only milliseconds per step, not noticeable on low step workflows
  - *From: Kijai*

- **Problem:** Sage attention not available
  - **Solution:** Use SDPA as alternative, and disconnect compile_args if you don't have Triton
  - *From: Kijai*

- **Problem:** VRAM usage close to max causing GPU performance issues
  - **Solution:** Increase block swap to avoid GPU not working correctly when VRAM usage is very close to max like 23.4 on 24GB
  - *From: Ashtar*

- **Problem:** IndexError with Pusa extend workflow
  - **Solution:** Update the String to Float List so that it matches the number of latents - 13 frames by default
  - *From: mamad8*

- **Problem:** Pusa last noise multiply not working in V2V + LF workflow
  - **Solution:** Need to provide noise multipliers per extra latent added, not per whole list. For 13 start frames + 1 end frame, provide 5 multipliers in order of injection, not by index
  - *From: Kijai*

- **Problem:** Characters' mouths keep moving after audio ends in InfiniteTalk
  - **Solution:** Add silence to your audio. The looping method requires each window to be same size, so it pads with reflected audio which keeps them talking
  - *From: Kijai*

- **Problem:** Flickering and garbled motion when using 28 steps without LightX
  - **Solution:** Remove the CFG schedule node entirely when not using LightX. CFG scheduling is only for LightX (sets CFG 3.5 on first step only), should be on all steps for normal use
  - *From: mamad8*

- **Problem:** Video cuts between context windows leading to different scenes
  - **Solution:** 1. Provide prompts with common context that follow each other well (use | to separate prompts). 2. Use stride of 10 for high noise and stride of 4 for low noise, both with overlap of 48 and pyramid as fuse_method
  - *From: mamad8*

- **Problem:** Model outputting degraded results after several generations
  - **Solution:** Restart ComfyUI. Issue may occur when using both LoRAs on model node of wrapper + LoRAs on setLoras node simultaneously
  - *From: mamad8*

- **Problem:** Out of memory errors with long multitalk generations
  - **Solution:** Switch to InfiniteTalk which has been giving better results and better memory management
  - *From: blake37*

- **Problem:** Color/contrast shift in Fun Control low noise pass
  - **Solution:** Issue appears in both first and second sampler passes, workflow configuration may need adjustment
  - *From: Nathan Shipley*

- **Problem:** CUDA 13 compatibility issues
  - **Solution:** Remove CUDA 13 toolkit and driver, restart, then install driver only then CUDA 12.8 toolkit only and restart
  - *From: hicho*

- **Problem:** Tensor size error with Fun Control models
  - **Solution:** Enable 'fun_or_fl2v_model' option in WanVideo ImageToVideo Encode node
  - *From: Juan Gea*

- **Problem:** Both characters talking simultaneously in InfiniteTalk multi-character setup
  - **Solution:** Need to plug in masks - InfiniteTalk needs a mask for each audio, so if you give it audio_1 and audio_2, the mask input needs to be a batch of 2 masks
  - *From: Kijai*

- **Problem:** Video quality degradation with consecutive I2V runs using last frame
  - **Solution:** No real solution available yet, each generation causes some quality degradation in sharpness, color and contrast
  - *From: Kenk*

- **Problem:** Blurry first frame in I2V
  - **Solution:** Issue was resolved after updating the wrapper
  - *From: hicho*

- **Problem:** Triton compatibility issues with Python 3.13
  - **Solution:** Download triton-windows zip and unzip into python_embedded folder, adds files to include folder and libs folder
  - *From: Urabere*

- **Problem:** Large VRAM usage after switching from high to low model
  - **Solution:** Drop execution cache to clear 11-15GB VRAM occupation
  - *From: jeffcookio*

- **Problem:** Blurry I2V output returning
  - **Solution:** Issue acknowledged as recurring problem, no specific solution provided
  - *From: hicho*

- **Problem:** 161 frames I2V animation loops at some point
  - **Solution:** Hitting context window limit, need to manage context windows properly
  - *From: jeffcookio*

- **Problem:** Tensor alignment shape errors when combining InfiniteTalk with Pusa
  - **Solution:** No solution found, user not in mood to reverse engineer
  - *From: MysteryShack*

- **Problem:** Blurry outputs after ComfyUI update
  - **Solution:** Update wrapper via git clone and check sampler connections
  - *From: hicho*

- **Problem:** Cartoon style output instead of realistic
  - **Solution:** Switch from Wan22-Lightning to older Lightx2v LoRAs and add hyperrealistic prompts
  - *From: Lodis*

- **Problem:** StringFromList error
  - **Solution:** Use correct CLIP model: umt5_xxl_fp8_e4m3fn_scaled.safetensors instead of umt5-xxl-enc-fp8_e4m3fn.safetensors
  - *From: Ashtar*

- **Problem:** UltimateSDUpscaler only outputs first frame
  - **Solution:** Update UltimateSDUpscaler nodes to latest version
  - *From: DennisM*

- **Problem:** Node parameters getting accidentally changed
  - **Solution:** Check for detached connections and mouse-over accidents that change values
  - *From: hicho*

- **Problem:** Canvas won't move over sigma split graphs
  - **Solution:** Z-index issue with graph overlay preventing mouse interaction
  - *From: Kenk*

- **Problem:** No fp8 version for multi-speaker models causes VRAM issues
  - **Solution:** Use blockswap 40 on 5090, though it puts VRAM usage in 31GB danger zone
  - *From: blake37*

- **Problem:** ComfyUI --fast flag causing OOM with WanVideo ImageToVideo Encode node
  - **Solution:** Run without --fast flag to fix OOM issue
  - *From: Kenk*

- **Problem:** S2V model not responding to camera movement and walking prompts
  - **Solution:** Model may be trained primarily on portrait talking heads, try using multitalk for better prompt adherence
  - *From: nacho.money*

- **Problem:** Music interfering with S2V lipsync
  - **Solution:** Separate voice from music before feeding to S2V model
  - *From: Miku*

- **Problem:** Context extension with I2V returns to starting image
  - **Solution:** No clear solution provided, acknowledged as ongoing issue
  - *From: flo1331*

- **Problem:** VAE encode darkening effect in infinite talk
  - **Solution:** Issue occurs when not re-encoding between windows, faster but causes darkening
  - *From: Kijai*

- **Problem:** Unmerged loras not working with fp8 e5 scaled models
  - **Solution:** Enable merge_loras option makes scaled models work with loras
  - *From: Hoernchen*

- **Problem:** --fast argument causing VAE encode issues
  - **Solution:** Use specific fast options like --fast fp16_accumulation instead of general --fast
  - *From: Kijai*

- **Problem:** Resize node divisible by 2 instead of 16 causing tensor mismatch
  - **Solution:** Set resize node to divisible by 16
  - *From: Poppi*

- **Problem:** T2V model giving channels error with I2V workflow
  - **Solution:** Make sure using correct T2V model, not I2V model
  - *From: Kijai*

- **Problem:** Broken nodes issue after ComfyUI update
  - **Solution:** Revert WanWrapper to commit from August 23rd
  - *From: HeadOfOliver*

- **Problem:** Comfy interface not responding after using symlinks
  - **Solution:** Move models back to original folder, avoid using too many symlinks
  - *From: BecauseReasons*

- **Problem:** VACE not leaving unmasked regions alone
  - **Solution:** Issue with chaining samplers, context options in wrapper don't follow masked areas as well as native VACE
  - *From: the_darkwatarus_museum*

- **Problem:** Infinite Talk not working after updates
  - **Solution:** Check model hash, reinstall ComfyUI, Triton, and SAGE attention. Python 3.13.6, PyTorch 2.8.0, CUDA 12.9
  - *From: kendrick*

- **Problem:** Tensor mismatch errors with mixed model types
  - **Solution:** Model mismatch - ensure GGUF and FP8 models aren't mixed improperly
  - *From: Charlie*

- **Problem:** Preview Animation node broken
  - **Solution:** Use SaveVideo or SaveWEBM nodes instead, Preview Animation has been broken for a while
  - *From: Kijai*

- **Problem:** Symlinks being removed after ComfyUI updates
  - **Solution:** Use extra_model_paths.yaml file instead of symlinks
  - *From: Ablejones*

- **Problem:** OOM errors when generating long videos (2000+ frames)
  - **Solution:** Use save latents approach to decode in chunks, or use Kijai's infinite talk workflow with long I2V node that does decoding within the loop
  - *From: samhodge*

- **Problem:** InfiniteTalk producing 'exploding confetti' in first frames
  - **Solution:** Switch to MultiTalk which doesn't have this issue
  - *From: mdkb*

- **Problem:** Wan VAE issues when using tiled_decode in ultimate SD upscaler
  - **Solution:** Turn off tiled_decode in ultimate SD upscaler node, though quality will be lower
  - *From: FL13*

- **Problem:** VACE 2.2 not maintaining character identity properly
  - **Solution:** User reported using Wan 2.2 LN model with VACE gives better results for character consistency
  - *From: mdkb*

- **Problem:** VHS Combine OOM with long videos
  - **Solution:** Replace VHS Combine with Save Image node to avoid memory issues, then combine video in post-processing
  - *From: samhodge*

- **Problem:** InfiniteTalk first latent noise issue
  - **Solution:** Use WAN Image to Video Encode First Latent node to provide proper first image in latents
  - *From: Kijai*

- **Problem:** Green noise in Fun Inpaint fp8
  - **Solution:** Issue appears to be related to fp8 e4m3fn scaled high noise, may need to check noise shift settings
  - *From: Hevi*

- **Problem:** Color shift in InfiniteTalk
  - **Solution:** Added color shift correction option to InfiniteTalk sampling node
  - *From: Kijai*

- **Problem:** Color shifting with start+end images in wrapper
  - **Solution:** Enable the fun_or_fl2v_model switch in wrapper settings
  - *From: Kijai*

- **Problem:** Triton compilation errors
  - **Solution:** Clear triton cache folders: %USERPROFILE%\.triton\cache and C:\Users\[username]\AppData\Local\Temp\torchinductor_[...]
  - *From: Mu5hr00m_oO (5080 + 64)*

- **Problem:** Fake tensor errors after wrapper update
  - **Solution:** Check for input size mismatches with the model requirements
  - *From: ingi // SYSTMS*

- **Problem:** Noise pattern artifacts in generations
  - **Solution:** Use lightx2v LoRAs to avoid noise patterns, or check if using openpose with fun models
  - *From: gordo*

- **Problem:** Color match node throwing RuntimeError about empty TensorList
  - **Solution:** One of the inputs (image_ref or image_target) is empty, check if group node is bypassed
  - *From: Akumetsu971*

- **Problem:** Getting stick figures in pose detection
  - **Solution:** Disable detect_body in both dwpose_estimator nodes or set blend factor to 0.1 or 0.05
  - *From: Akumetsu971*

- **Problem:** Max frames less than context window frames causing mismatch
  - **Solution:** User error - ensure max frames setting is not less than context window frames
  - *From: T2 (RTX6000Pro)*

- **Problem:** USDU upscaler crashes with 81 frames on 3060
  - **Solution:** Run workflow twice at 65 frames each, then combine in video editor with slight overlap
  - *From: mdkb*

- **Problem:** Radial attention block size errors with resolutions
  - **Solution:** Must use resolutions divisible by block size (64 or 128), sometimes requires ComfyUI restart after first crash
  - *From: .: Not Really Human :.*

- **Problem:** High RAM usage (92GB) in ComfyUI
  - **Solution:** Use --disable-smart-memory --cache-none arguments to limit RAM usage to 30-40GB
  - *From: .: Not Really Human :.*

- **Problem:** Cannot copy out of meta tensor error in WanVideoSampler
  - **Solution:** Use torch.nn.Module.to_empty() instead of torch.nn.Module.to() when moving from meta to different device
  - *From: 𝕯𝖗. 𝕸𝖆𝖈𝖆𝖇𝖗𝖊 ☠*

- **Problem:** Context windows + Fun 2.2 control causing complete ComfyUI crashes
  - **Solution:** Index out of bounds error in CUDA kernel, no solution provided
  - *From: DawnII*

- **Problem:** vace_scale KeyError when using VACE
  - **Solution:** Need to load VACE model properly, the error occurs when VACE isn't loaded
  - *From: Dream Making*

- **Problem:** Size mismatch errors with radial attention
  - **Solution:** Update WanVideoWrapper nodes via git clone instead of ComfyUI manager, and use correct VAE - only 5B model uses 2.2 VAE
  - *From: Kijai*

- **Problem:** Wan 2.2 5B model gives minimal motion with I2V
  - **Solution:** Use T2V instead of I2V for better motion results, or try 50 steps without turbo wan
  - *From: crinklypaper*

- **Problem:** Differential diffusion makes output worse
  - **Solution:** Set noise mask feather to 0 to disable differential diffusion
  - *From: Dita*

- **Problem:** Character quality loss with face turning in long videos
  - **Solution:** Using VACE to swap character back in strips out lipsync, creating a trade-off issue
  - *From: mdkb*

- **Problem:** InfiniteTalk changing face completely
  - **Solution:** Don't use FusionX, use normal I2V model instead
  - *From: Kijai*

- **Problem:** Could not find TAEW model file error
  - **Solution:** File was corrupted, needed to redownload
  - *From: scf*

- **Problem:** Load LoRA with merge taking 5 minutes at 3it/s
  - **Solution:** Should not take more than some seconds, something is broken
  - *From: Kijai*

- **Problem:** HuMo audio not working
  - **Solution:** Audio code may be unfinished, requires whisper-large-v3 model and has unusual input structure
  - *From: Kijai*

- **Problem:** Workflow corrupting itself
  - **Solution:** Recreate workflow in new file, original may be corrupted
  - *From: Dream Making*

- **Problem:** Infinite Talk speed issues with LoRAs
  - **Solution:** Speed-up loras not only slow it down but mess with consistency, but you need to increase steps and cfg if you disable them
  - *From: mdkb*

- **Problem:** VACE workflows stopped working for face swapping
  - **Solution:** Swapped out Wan 2.2 and VACE bf16 module for Phantom and VACE GGUF and it worked again
  - *From: mdkb*

- **Problem:** LightX2V models cause VACE issues
  - **Solution:** Have to use older models instead of LightX2V for better VACE performance
  - *From: JohnDopamine*

- **Problem:** Cannot extract last latents for video extension
  - **Solution:** Must decode to images and use I2V workflow due to temporally packed latent space
  - *From: Kijai*

- **Problem:** HuMo original code has multiple basic errors
  - **Solution:** Code has missing required arguments and can't work as released
  - *From: Kijai*

- **Problem:** Masking v2v workflow issues
  - **Solution:** Some users report masking not working with Fun VACE, but others confirm it works fine
  - *From: dg1860*

- **Problem:** Blue and broken images in Wan generations
  - **Solution:** Downgrade numpy to version <2.0, check boot log for dependency conflicts
  - *From: mdkb*

- **Problem:** VACE 2.2 giving model mismatch error
  - **Solution:** Use VAE 2.1 with VACE 2.2, not VAE 2.2 (which is for 5B model)
  - *From: Cseti*

- **Problem:** HuMo audio issues on single GPU
  - **Solution:** Audio crossattn function needs fixing for single GPU setups, works on multi-GPU
  - *From: Kijai*

- **Problem:** GGUF Low noise model loading error with different shapes
  - **Solution:** Use city96 script instead of quantstack models, shapes differ between implementations
  - *From: Kijai*

- **Problem:** Audio scale artifacts in InfiniteTalk above 1.0
  - **Solution:** Keep audio_scale at 1.0 to avoid color flashes and image degradation
  - *From: blake37*

- **Problem:** ComfyUI crash with torch compile
  - **Solution:** Disable WanVideo Torch Compile Settings
  - *From: «☼spacemathapocalypse☼»*

- **Problem:** VACE start/end frame node crashes with control frames only
  - **Solution:** Don't pass only control frames, use with reference images or other inputs
  - *From: Kijai*

- **Problem:** Canny control not working properly
  - **Solution:** Use invert image node with Canny for VACE, needs black lines and white background
  - *From: mdkb*

- **Problem:** CUDA error on 5090 with Triton/SageAttention
  - **Solution:** Install SageAttention from woct0rdho releases instead of pip
  - *From: xiver2114*

- **Problem:** Diffusion Model Loader error in latest ComfyUI
  - **Solution:** Disable non-blocking in block swap settings
  - *From: Kijai*

- **Problem:** HuMo crashes with block swap
  - **Solution:** Disable torch compile if using it
  - *From: Kijai*

- **Problem:** Mask bleeds gray edges with expanded masks
  - **Solution:** Replace with SAM2 for better masking results
  - *From: scf*

- **Problem:** GGUF stride error with Wan 2.2 models
  - **Solution:** Update gguf to 0.17.1 and diffusers to 0.35.0.dev0
  - *From: Kijai*

- **Problem:** Poor VACE quality with default settings
  - **Solution:** Change sampler from uni_pc beta to dpmpp sde gpu beta57 for major quality improvement
  - *From: Gleb Tretyak*

- **Problem:** WhisperModelLoader error with KeyError: 'audio_encoders'
  - **Solution:** Update ComfyUI - audio_encoders folder was added in S2V update
  - *From: Kijai*

- **Problem:** HumoEmbed node error about start/stop percentage after branch switch
  - **Solution:** Delete __pycache__ folder in wrapper directory
  - *From: JohnDopamine*

- **Problem:** ValueError: range() arg 3 must not be zero in tiled encoding
  - **Solution:** Fixed in code update
  - *From: Kijai*

- **Problem:** Context options not working with cfg float list
  - **Solution:** Fixed cfg schedule issue in latest update
  - *From: Kijai*

- **Problem:** Misty effect and white dots on faces with VACE 2.2 + controlnets
  - **Solution:** Disable face aspect of pose controlnet as workaround
  - *From: mdkb*

- **Problem:** Video/mouth sync issues
  - **Solution:** Use 25 fps and proper resolution (832x480 or mentioned alternatives)
  - *From: Kijai*

- **Problem:** OOM on VAE decode at high resolution
  - **Solution:** Save latents using save latent node and enable tiled decode
  - *From: VK (5080 128gb)*

- **Problem:** PUSA noise node error with constant values
  - **Solution:** Use Create Schedule Float List node - the noise node requires a list input
  - *From: Kijai*

- **Problem:** bf16 VACE modules don't work with fp8 Wan models
  - **Solution:** Use matching precision - fp8 VACE modules with fp8 Wan models to avoid half-baked results
  - *From: mdkb*

- **Problem:** Pose dots bleeding through on face
  - **Solution:** Issue occurs with bf16 module + fp8 main model combo, works better with matching precisions
  - *From: mdkb*

- **Problem:** ComfyUI crashes with VACE workflows
  - **Solution:** Check ComfyUI logs in user folder, may be related to torch.compile issues
  - *From: Kijai*

- **Problem:** HuMo context windows tensor size error
  - **Solution:** Update Kijai nodes to latest version via git pull
  - *From: xwsswww*

- **Problem:** HuMo OOMs frequently with default context window
  - **Solution:** Use 30 frames instead of default 81 frames for context windows, tried with block swap of 30
  - *From: xwsswww*

- **Problem:** Video cuts between context windows with HuMo
  - **Solution:** Issue occurred when using 30 frames per context with 97 total frames - may need higher frame count per context
  - *From: xwsswww*

- **Problem:** InfiniteTalk first frame appears noisy
  - **Solution:** InfiniteTalk expects first latent to always be unnoised, provide proper unnoised first frame
  - *From: Kijai*

- **Problem:** Old xformers version causing problems
  - **Solution:** Uninstall old xformers rather than upgrading - having old version installed causes problems, not having it doesn't
  - *From: Kijai*

- **Problem:** SageAttention error with transformer_options
  - **Solution:** Update KJNodes to latest nightly version - bug was fixed recently due to ComfyUI update changing attention code
  - *From: Kijai*

- **Problem:** USDU flickering in middle of video
  - **Solution:** Change temporal_frames from default 64 to 84 to fix flickering issue
  - *From: FL13*

- **Problem:** First second exposure change with low denoise
  - **Solution:** Turn off tiled_decode to fix exposure change issue
  - *From: FL13*

- **Problem:** Sharded model files not loading in ComfyUI
  - **Solution:** Use combined models instead of sharded versions, available on HuggingFace
  - *From: Kijai*

- **Problem:** q_lora missing error with standard Wan loader
  - **Solution:** Must use stand-in LoRA in model loader when using text/image embeddings
  - *From: Kijai*

- **Problem:** Empty start image causing AttributeError in VACE Start To End Frame
  - **Solution:** Node updated to handle passthrough when only control images provided
  - *From: Kijai*

- **Problem:** RTX 3090 CUDA memory errors
  - **Solution:** Switch from --highvram to --normalvram launch argument
  - *From: herpderpleton*

- **Problem:** SAGE attention causing black images on some GPUs
  - **Solution:** Disable SAGE attention via command line
  - *From: Kijai*

- **Problem:** Block swap causing infinite first step
  - **Solution:** Adjust block swap values, requires significant RAM with fp16
  - *From: Gleb Tretyak*

- **Problem:** Torch 2.8.0 on Windows causing VRAM allocation issues
  - **Solution:** First run uses more VRAM when using torch compile
  - *From: Kijai*

- **Problem:** CUDA device error with torch compile and PyTorch 2.8.0
  - **Solution:** Either downgrade to PyTorch 2.7.1 or upgrade to 2.9 nightly, and clear triton cache after updating
  - *From: Kijai*

- **Problem:** Block swap error: Expected all tensors to be on same device
  - **Solution:** Block swap node for native is pointless and not needed - it's automatic. Better to use --reserve-vram launch parameter
  - *From: Kijai*

- **Problem:** Multiple speakers not working in InfiniteTalk
  - **Solution:** Need one mask for each audio in batch, not just one mask total
  - *From: Kijai*

- **Problem:** ComfyUI silent crash on startup with WanVideoWrapper
  - **Solution:** Problem was sageattention package causing crash on import - uninstall sageattention to fix
  - *From: Gleb Tretyak*

- **Problem:** WanVideoWrapper sampler not showing previews after update
  - **Solution:** Update VHS nodes - this fixes the preview issue
  - *From: Dream Making*

- **Problem:** First 24 frames garbled/noisy when upscaling
  - **Solution:** Lower shift parameter to 3-5, or check if clip is longer than 5 seconds
  - *From: FL13*

- **Problem:** VACE Fun 2.2 not good at spatial inpainting with masks
  - **Solution:** Use Wan 2.2 low with VACE 2.1 for better spatial inpainting results
  - *From: hablaba*

- **Problem:** Pusa scheduler causing VRAM overflow
  - **Solution:** Don't use Pusa scheduler outside its intended purpose (I2V with T2V model or extension). It uses significantly more memory and is detrimental when used incorrectly
  - *From: Kijai*

- **Problem:** Wrong model channels error
  - **Solution:** Error 'expected input[1, 16, 21, 72, 72] to have 36 channels, but got 16 channels' means using I2V model (36 channels) with T2V workflow (16 channels). Switch to correct model type
  - *From: Kijai*

- **Problem:** ComfyUI copy-paste not working
  - **Solution:** Update ComfyUI Easy Use to fix copy-paste issues with noodles/connections
  - *From: VRGameDevGirl84(RTX 5090)*

- **Problem:** Infinite Talk prompt changing not working
  - **Solution:** Restart ComfyUI when prompt changes aren't taking effect in Infinite Talk workflows
  - *From: slmonker(5090D 32GB)*

- **Problem:** Video degradation in Infinite Talk
  - **Solution:** Update wrapper nodes - issue was fixed yesterday
  - *From: Kijai*

- **Problem:** WanVideo Encode Latent Batch node producing blurry results in masked area with Fun Vace 2.2
  - **Solution:** Nothing about that is compatible, the method is for I2V models, which VACE is not
  - *From: Kijai*

- **Problem:** Can't use VACE 2.1 after updating wanwrapper, getting 'Wan22' from 'comfy.latent_formats' error
  - **Solution:** That's very old ComfyUI as it doesn't have the Wan 2.2 VAE code available, need to update ComfyUI
  - *From: Kijai*

- **Problem:** CombineVideosV2 node not showing up despite installation
  - **Solution:** Need to install kornila and change function called bool to boolean in nodes.py
  - *From: asd*

- **Problem:** Humo 1.7 not working with torch.compile
  - **Solution:** Disable torch.compile, model is 1.3B so needs different loras
  - *From: Kijai*

- **Problem:** Context windows causing repetition of init image with 2.2
  - **Solution:** Using context windows with I2V workflows is generally a really dumb idea with 2.2
  - *From: Koba*

- **Problem:** Error when trying more than 101 frame count with context options
  - **Solution:** RuntimeError: Trying to create tensor with negative dimension -14: [16, -14, 72, 128] - needs investigation
  - *From: VRGameDevGirl84(RTX 5090)*

- **Problem:** Ghosting in 2.2 i2v workflow
  - **Solution:** Wrong step start/stop for both samplers (should be 0/3 3/-1 or 1000), wrong strength for high noise (high lightx needs more strength with 2.2, 2.5-3.0)
  - *From: Hoernchen*

- **Problem:** VACE producing garbage output
  - **Solution:** Don't misplugged High in Low and Low in High - this produces garbage
  - *From: Gleb Tretyak*

- **Problem:** fp8_e4 compatibility issues on 30xx series
  - **Solution:** Need to find the fp8_e5 version of the same file if you're on 30xx series
  - *From: ArtOfficial*

- **Problem:** Blue screen of death during generation
  - **Solution:** Add clear VRAM before show any node
  - *From: VRGameDevGirl84(RTX 5090)*

- **Problem:** HuMO only works with 1280x720 resolution
  - **Solution:** Cannot use other resolutions like 480, causes 'Sizes of tensors must match' error
  - *From: amli*

- **Problem:** Torch 2.8.0 has compilation issues on Windows
  - **Solution:** Avoid torch 2.8.0 on Windows, use 2.9 nightly and clear all triton caches
  - *From: Kijai*

- **Problem:** Radial attention requires image size divisible by block size
  - **Solution:** For 1280x720, use 1280x768 instead or adjust block size to 64
  - *From: mdkb*

- **Problem:** Second sampler doing 0 steps error
  - **Solution:** Check sampler step configuration
  - *From: Kijai*

- **Problem:** VACE strength above 1.0 darkens output
  - **Solution:** Reduce VACE strength to 0.7-1.0 to reduce contrast issues
  - *From: xwsswww*

- **Problem:** Callback_latent error in latest wrapper
  - **Solution:** Update wrapper from GitHub
  - *From: Kijai*

- **Problem:** Wan causing PC crashes and BSOD
  - **Solution:** Use --disable-smart-memory switch, disable sage attention, or set power limit with nvidia-smi -pl <watts>. Issue may be CPU memory controller or mem temp hitting 110C
  - *From: mdkb, Kijai*

- **Problem:** Double ghost effect in i2v generations
  - **Solution:** Check VACE controlnets positioning vs ref image - VACE adds ghosts to compensate when controlnets are out of position
  - *From: mdkb*

- **Problem:** InfiniteTalk generating more frames than expected
  - **Solution:** Frame window size should be set to values the model handles well like 81 frames, not total frame count. It can't do partial windows so rounds up
  - *From: Kijai*

- **Problem:** Changing number of frames in vid2vid changes content
  - **Solution:** This is normal behavior - video models learn different things at different resolutions/frame counts, similar to 2D models at different resolutions
  - *From: mallardgazellegoosewildcat*

- **Problem:** Text encoder node taking much longer than before (3-4 minutes vs very fast)
  - **Solution:** Issue seems environmental, possibly related to ComfyUI changes around a week prior
  - *From: JalenBrunson*

- **Problem:** Model loading taking longer than before
  - **Solution:** Unresolved issue, user suspects environment conflict
  - *From: JalenBrunson*

- **Problem:** GGUF model error with wrapper: Input type (torch.cuda.HalfTensor) and weight type (torch.cuda.ByteTensor) mismatch
  - **Solution:** GGUF models work fine on native ComfyUI nodes but have issues with wrapper
  - *From: Izaan*

- **Problem:** Over-animated motion even at CFG 1.5
  - **Solution:** Go even lower with CFG - use tiny fractions if needed
  - *From: Kijai*

- **Problem:** Sigma to Step node error: start_step must be less than end_step
  - **Solution:** Issue occurs when increasing start step because end step sigma is always smaller value
  - *From: Hashu*

- **Problem:** 'Header too large' error with Want5TextEncoderNode
  - **Solution:** Usually indicates corrupted model file
  - *From: Kijai*

- **Problem:** VACE darkening unmasked areas in output video
  - **Solution:** User planning to use Blender to create rotoscoped mask for better control
  - *From: xwsswww*

- **Problem:** Models taking forever to load on Linux
  - **Solution:** Check vm.swappiness setting - should be 0, not default 60. Virtual memory causes HD I/O overload
  - *From: MysteryShack*

- **Problem:** Character LoRAs bleeding into each other
  - **Solution:** Remove reward LoRAs (MPS, HPS) when using controlnets as they add unwanted elements
  - *From: mdkb*

- **Problem:** CFG 1 overexposes videos and ignores dim light prompting
  - **Solution:** Setting CFG to 3.5 in Hi-Sampler fixes that
  - *From: Drommer-Kille*

- **Problem:** Wan crashing PC
  - **Solution:** Setting GPU wattage limit to 400W fixed the crashing problem
  - *From: Drommer-Kille*

- **Problem:** Huggingface upload failures
  - **Solution:** Upload is slow and has failed 3 times, xet upload 5 times faster at least
  - *From: Kijai*

- **Problem:** Normal masks don't work with Wan-animate
  - **Solution:** Made a node to transform mask to that style
  - *From: Kijai*

- **Problem:** FaceMaskFromPoseKeypoints - len() of unsized object error
  - **Solution:** Probably failed detection on some frame, dwpose node isn't very robust
  - *From: Kijai*

- **Problem:** TypeError: len() of unsized object
  - **Solution:** It's the dwpose detection failing on certain videos
  - *From: Kijai*

- **Problem:** einops.EinopsError with tensor shape mismatch
  - **Solution:** Make sure frame_window_size and input frames are at exact same count
  - *From: Kijai*

- **Problem:** Videos with distracting camera motions cause dwpose to fail
  - **Solution:** Use videos with simpler, less dynamic camera movement
  - *From: rishappi*

- **Problem:** DWPose detection failures
  - **Solution:** Mat Anything works as decent alternative to DWPose, Sapiens also works fine
  - *From: JohnDopamine*

- **Problem:** SAM2 model version causing issues
  - **Solution:** Check the model you have set for SAM2 model - older/smaller models can cause problems
  - *From: JohnDopamine*

- **Problem:** RuntimeError: Sizes of tensors must match except in dimension 0
  - **Solution:** Make sure total frames follow the 4+1 rule. Use 161 total frames instead of 162, or match window size exactly to avoid windowing
  - *From: Kijai*

- **Problem:** Block swap causing device errors (CPU/CUDA mismatch)
  - **Solution:** Lower block swap value - 25 works for 1024x576x97, 30-35 can cause issues. Turn off non-blocking if needed
  - *From: slmonker(5090D 32GB)*

- **Problem:** OOM on decode at high resolutions
  - **Solution:** Use tiled decode for high resolution outputs
  - *From: slmonker(5090D 32GB)*

- **Problem:** Input video size errors
  - **Solution:** Ensure input video matches context options frame count exactly (e.g., 77fr context = 77fr input video)
  - *From: Martin_H*

- **Problem:** GGUF conversion errors with motion encoder
  - **Solution:** Motion encoder cannot be quantized - exclude it from GGUF conversion process
  - *From: Kijai*

- **Problem:** Text encoder being slow
  - **Solution:** Was set to CPU mode - change to GPU for instant results
  - *From: Nekodificador*

- **Problem:** Hang at 33% on runpod
  - **Solution:** CUDA version mismatch - fix with: pip install --index-url https://download.pytorch.org/whl/cu128 torch torchvision torchaudio
  - *From: JalenBrunson*

- **Problem:** Padding tensor size mismatch error
  - **Solution:** Fixed offload bug related to blocks vs face_blocks naming
  - *From: Kijai*

- **Problem:** Black artifacts when not using pose/face
  - **Solution:** Set pose and face strength to 1 - the blocking occurs when they are both not 1
  - *From: Instability01*

- **Problem:** Missing nodes error
  - **Solution:** Go into manager and select nightly even if it's selected - it won't pull unless you click it
  - *From: particle9*

- **Problem:** Short clips need special settings
  - **Solution:** 
  - *From: Kijai*

- **Problem:** WanAnimate crashes when returning 1000+ frames
  - **Solution:** It's a RAM issue, not VRAM. The model had VRAM to spare but crashed when returning the frames to system memory
  - *From: Kijai*

- **Problem:** For short clips, need to set frame window size equal to num_frames
  - **Solution:** Set the frame window size equal to num_frames for short clips
  - *From: Kijai*

- **Problem:** Model invents stuff at the end if loaded frame count isn't a multiple of window size
  - **Solution:** This is by design from original code - extra frames are meant to be trimmed
  - *From: A.I.Warper*

- **Problem:** Grid blocks/artifacts appearing in generations
  - **Solution:** Try using resolution divisible by 64, boost the resolution settings
  - *From: Quality_Control*

- **Problem:** Background mask sticking around
  - **Solution:** Remove the 'get background image' node from the workflow
  - *From: Clément*

- **Problem:** Face not tracking properly
  - **Solution:** Take care about cropping - if the face is not centered well it doesn't work for eyes
  - *From: Kijai*

- **Problem:** Points editor requiring two executions
  - **Solution:** Connect width/height to points editor, start gen to get first frame, stop it, set points, then run again. Or save first frame in target resolution and copy paste to points editor node
  - *From: Kijai*

- **Problem:** All animate outputs coming out CFG burnt even at CFG 1
  - **Solution:** Use 1cfg+lightx, other options like 50 steps don't seem to work
  - *From: Gleb Tretyak*

- **Problem:** Tensor size mismatch error in WanAnimate
  - **Solution:** Happens if you use less than 77 input frames
  - *From: StableVibrations*

- **Problem:** Error about resolution and frame count
  - **Solution:** Resolution needs to be divisible by 16 or frame count related
  - *From: Kijai*

- **Problem:** ComfyUI-MelBandRoFormer nodes import failed
  - **Solution:** Run pip install numpy<2.0 - ecosystem still needs <2.0
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Problem:** VACE first latent trimming broken
  - **Solution:** Should be fixed now, accidentally broke VACE first latent trimming
  - *From: Kijai*

- **Problem:** OOM on RTX 5090 with 1280x720 81 frames
  - **Solution:** Try text encoder on cpu + comfy chunk, or lower resolution
  - *From: hicho*

- **Problem:** Snow particles with NAG+LightX on WAN 2.2
  - **Solution:** Make sure no high step occurs after sigmas of around 0.9, red line should be at 0.9 ish or higher
  - *From: Instability01*

- **Problem:** Black mask shapes in output video
  - **Solution:** Check for no person found in mask, mask block sizes, and too low strength value on pose or face strength
  - *From: The Dude*

- **Problem:** Black square artifacts in masks
  - **Solution:** Use face strength of 1.0 and provide black frames for face input
  - *From: Kijai*

- **Problem:** Model failure with VACE 2.1 inpainting
  - **Solution:** Use matching VACE fp8 module for the model instead of mixing model types
  - *From: mdkb*

- **Problem:** RuntimeError with tensor size mismatch
  - **Solution:** Use resolutions where width * height * frames is divisible by 16
  - *From: Kijai*

- **Problem:** Corrupt output with T5 cache
  - **Solution:** Delete cache files when switching between quantized/unquantized encoding
  - *From: Kijai*

- **Problem:** Black squares with imperfect mask boxes
  - **Solution:** Works with near-black colors up to (30,30,30), doesn't have to be pure black (0,0,0)
  - *From: Dever*

- **Problem:** OOM errors with WanAnimate on 12GB VRAM
  - **Solution:** Use blockswap node, lighter text encoder (6GB instead of 11GB), lower resolutions first
  - *From: harriet_h*

- **Problem:** RAM saturating with high block swap settings
  - **Solution:** Start with lower block swap numbers (16 should be enough with 32GB RAM), don't set too high
  - *From: buttercup5108*

- **Problem:** Wan2.2 produces garbled output without LightX
  - **Solution:** LightX with 6 steps works better than no LightX with 40 steps
  - *From: Ruairi Robinson*

- **Problem:** 50 recommended steps destroy everything in Wan2.2
  - **Solution:** Use fewer steps, 50 steps causes issues
  - *From: Gleb Tretyak*

- **Problem:** Character faces too small/far away don't work well
  - **Solution:** Need super zoomed in reference video, consider two passes of cropping or remove face video from animate embeds
  - *From: ArtOfficial*

- **Problem:** Rigid masking issues with wan-animate
  - **Solution:** Can use grow and blur options, or precise masks with VACE
  - *From: DawnII*

- **Problem:** SageAttention and Triton required for isolated environments
  - **Solution:** pip install triton-windows, find sage whl file
  - *From: buttercup5108*

- **Problem:** CUDA out of memory error with 81 frames 512x512
  - **Solution:** Switch WanVideo block swap from 35 to 25
  - *From: 435512773737447446*

- **Problem:** First frame saturation/burn-in effect
  - **Solution:** Update to latest version - first latent was wrong and got burned
  - *From: Kijai*

- **Problem:** Video extends beyond original framecount
  - **Solution:** Make frame window size equal to total frames for short clips, or ensure frame window is larger than num_frames
  - *From: Kijai*

- **Problem:** Size mismatch errors with long videos
  - **Solution:** Ensure ref image and ref video are same size and dimensions divisible by 16
  - *From: ingi // SYSTMS*

- **Problem:** Can't detect face error
  - **Solution:** Use human reference for pose video even if using non-human (like dog) as ref image
  - *From: slmonker(5090D 32GB)*

- **Problem:** Color changes during video after second frame using Kijai workflow
  - **Solution:** Use color matching with MVGD option, though it darkens the image
  - *From: Kevin "Literally Who?" Abanto*

- **Problem:** Can't get rid of mask in video generation
  - **Solution:** Use much bigger block sizes (should look like Minecraft) and reduce grow mask to -1
  - *From: Kijai*

- **Problem:** Gray background when removing background input
  - **Solution:** Remove both background input and character mask, keep only pose, face, and reference image
  - *From: ArtOfficial*

- **Problem:** ONNX not using GPU properly
  - **Solution:** Uninstall onnxruntime, then install onnxruntime-gpu and onnx
  - *From: ArtOfficial*

- **Problem:** Face blocks ended up as fp8 causing quality hit
  - **Solution:** Reverted face blocks back from fp8 to maintain quality
  - *From: Kijai*

- **Problem:** OOM issues with WAN 2.2 Animate
  - **Solution:** More block swap needed, especially at end of each window during decode-encode process
  - *From: Kijai*

- **Problem:** OOM error at 113 frames @ 720p with 12GB VRAM
  - **Solution:** Use frame window size of 77 or enable VAE tiling, or reduce to 640p
  - *From: Kijai*

- **Problem:** Black screen when using Framepack with fp16
  - **Solution:** Use bf16 base_precision instead, fp16 doesn't work properly with certain models
  - *From: Kijai*

- **Problem:** Point Editor image not updating
  - **Solution:** Right click to 'clear image' first, then run workflow
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Problem:** VAE taking too long and maxing out VRAM
  - **Solution:** Set VAE precision to fp16 instead of fp32, enable VAE tiling
  - *From: Kijai*

- **Problem:** WanVideoSampler tensor size mismatch error
  - **Solution:** Use resolution divisible by 8 (e.g., 272 instead of 270)
  - *From: traxxas25*

- **Problem:** Missing group icons in ComfyUI corner
  - **Solution:** Enable 'Show fast toggles' in Rgthree settings
  - *From: SonidosEnArmonía*

- **Problem:** Wan Animate OOM on A100 42GB VRAM with 77 frames
  - **Solution:** 
  - *From: gpbhupinder*

- **Problem:** Face crop detection error in WanAnimatePreprocess
  - **Solution:** Check if face is detected in input, put detection models in comfyui/models/detection
  - *From: patientx*

- **Problem:** Pose/bone is bigger than mask in WanAnimatePreprocess
  - **Solution:** Set padding to 0, avoid using reference image with masking
  - *From: Kijai*

- **Problem:** High noise introduces noisy motion in 2.2 PUSA extension
  - **Solution:** Try cfg skimming schedule or reduce cfg of first few steps
  - *From: DawnII*

- **Problem:** Background appears gray when no background_video connected
  - **Solution:** Use bg_images input
  - *From: Kijai*

- **Problem:** Tensor dimension error with negative values
  - **Solution:** Update WanVideoWrapper - progress is being made on fixing this
  - *From: Hazzani*

- **Problem:** OOM crashes during second generation
  - **Solution:** Set VAE from f32 to f16 to reduce VRAM usage
  - *From: Dkamacho*

- **Problem:** Context range() arg 3 must not be zero error
  - **Solution:** Reduce overlap or increase frames - overlap cannot be greater than context frames
  - *From: DawnII*

- **Problem:** SAM2 keeping VRAM after completion
  - **Solution:** Fixed in latest update - was keeping ~200-300MB VRAM unnecessarily
  - *From: Kijai*

- **Problem:** Face_images_in variable error when disabled
  - **Solution:** Update to latest wrapper version - code now creates zeros automatically when face isn't used
  - *From: Kijai*

- **Problem:** PoseAndFaceDetection OpenCV size error
  - **Solution:** Issue connected to FPS - use 30fps video with forced rate 16 instead of true 16fps video
  - *From: HeadOfOliver*

- **Problem:** Wan 2.2 5B using same VRAM as 14B
  - **Solution:** Try Q4 or Q5 quantized models for 12GB VRAM instead of full precision
  - *From: el marzocco*

- **Problem:** ONNX preprocessing running slowly
  - **Solution:** Install onnxruntime-gpu for NVIDIA GPUs, uninstall normal onnxruntime - should be really fast on CUDA
  - *From: Kijai*

- **Problem:** OpenCV error with WanAnimatePreprocess node
  - **Solution:** Error occurs when face is not in full view (side profile), need to use crop by mask
  - *From: xwsswww*

- **Problem:** ComfyUI UI freezing when navigating to top of workflow
  - **Solution:** Update ComfyUI frontend using 'pip install -U comfyui-frontend-package' command
  - *From: Kijai*

- **Problem:** Points Editor causing workflow freeze
  - **Solution:** Use newer workflow without points editor, issue may be with older ComfyUI frontend versions
  - *From: Kijai*

- **Problem:** LoRAs get bypassed when blockswapping kicks in
  - **Solution:** When model is loaded partially, loras disappear completely including lightning loras
  - *From: Persoon*

- **Problem:** Segment-anything-2 second run error
  - **Solution:** TypeError: 'NoneType' object is not subscriptable - suspect cache was released, had to restart ComfyUI
  - *From: piscesbody*

- **Problem:** Self-forcing 10s model won't load in ComfyUI
  - **Solution:** Model has ema model structure, need to extract 'generator_ema' key using conversion script provided
  - *From: Kijai*

- **Problem:** Undetected face on some frames causes preprocessing failure
  - **Solution:** Original code had no fallback when something is not detected, it just fails
  - *From: Kijai*

- **Problem:** Black screen issues with model precision mismatch
  - **Solution:** Don't use bf16 dtypes when main model is fp16, probably sageattention causing issue
  - *From: Kijai*

- **Problem:** SAM masking fails on non-humans
  - **Solution:** Use other SAM models, 2.1 is better, or try bbox only approach
  - *From: Kijai*

- **Problem:** Blockify mask creating interference
  - **Solution:** Run mask cleanup before the block node or do erode (negative grow mask) first before dilate
  - *From: Kijai*

- **Problem:** Fun VACE module compatibility with precision
  - **Solution:** Use bf16 model when module is bf16, even though you lose fp16 fast performance
  - *From: Kijai*

- **Problem:** OOM on 367 frames 1280x720 with 4090/64GB RAM
  - **Solution:** Failure occurred at Image concatenate node rather than during diffusion
  - *From: Jas*

- **Problem:** CUDA out of memory error on 4090
  - **Solution:** Set use_non_blocking to false in WANVideo Block Swap node
  - *From: wouter*

- **Problem:** VACE module won't load after update
  - **Solution:** Update PyTorch to 2.10 nightly or switch rms norm back to default
  - *From: MysteryShack*

- **Problem:** WanVideoSampler error: expected input to have 36 channels but got 16
  - **Solution:** Check model compatibility and VAE selection
  - *From: Josiah*

- **Problem:** Pose detection not working properly
  - **Solution:** Change from yolo_l.onnx to yolo10m.onnx
  - *From: Léon*

- **Problem:** Pose estimator sticks appearing outside canvas
  - **Solution:** Update nodes and adjust padding option
  - *From: Kijai*

- **Problem:** Hand detection issues after update
  - **Solution:** Set hand stick width to 1
  - *From: Léon*

- **Problem:** Tensor mismatch error in WanAnimateToVideo
  - **Solution:** Adjust continue_motion_max_frames parameter
  - *From: Danial*

- **Problem:** Color smudging during motion in Wan output
  - **Solution:** Running wan output through SDXL on low denoise can fix it a bit
  - *From: VK (5080 128gb)*

- **Problem:** Context options causing character/face to get brighter
  - **Solution:** Use context window options, set frame_window_size equal to total frames
  - *From: Gateway {Dreaming Computers}*

- **Problem:** Need to handle 154 frames with context options
  - **Solution:** Set frame_window_size = 154 and context_frames = 77, remember 4n+1 rule, set load video path format to wan
  - *From: DawnII*

- **Problem:** Copy paste not working in ComfyUI
  - **Solution:** Chrome related issue - works in Firefox. Was working until recent update
  - *From: 𝕯𝖗. 𝕸𝖆𝖈𝖆𝖇𝖗𝖊 ☠*

- **Problem:** Cannot view latent file contents
  - **Solution:** Use the latent preview node to see frames and resolution
  - *From: VK (5080 128gb)*

- **Problem:** Hand animation LoRA snaps back every 81 frames
  - **Solution:** Use reference image to prevent snapping back
  - *From: Koba*

- **Problem:** Wan 2.5 generation failed with 'No inspiration found'
  - **Solution:** Try changing the description after waiting in queue
  - *From: seitanism*

- **Problem:** Tensor mismatch errors in longer duration workflows
  - **Solution:** Make sure resolutions are multiples of 16
  - *From: Rainsmellsnice*

- **Problem:** Pose retargeting not working
  - **Solution:** Use Flux kontext or other edit model to repose your driving video character and reference character first, then detect pose and retarget bones. Works best when poses match
  - *From: Kijai*

- **Problem:** Blocking/mask artifacts with block size 48
  - **Solution:** Use the new preprocess nodes from ComfyUI-WanAnimatePreprocess
  - *From: stas*

- **Problem:** Bottom of objects getting wonky in generations
  - **Solution:** Disable the relighting lora - it's meant to make things realistic including shading and 3D effects
  - *From: Rainsmellsnice*

- **Problem:** Texture chattering/swimming in detailed areas
  - **Solution:** Use bf16 instead of fp8, highest resolution possible, avoid high-frequency details in reference images
  - *From: Juampab12*

- **Problem:** Background plate degradation with VACE
  - **Solution:** Use mask from inpainting to recomp on original footage if needed, or composite on original background with good alpha mask
  - *From: Neex*

- **Problem:** Wrong LoRA effects when captioning too detailed
  - **Solution:** Caption simply - use 'hood is up' instead of 'her hood is up, and her face is partially shrouded by shadow'
  - *From: crinklypaper*

- **Problem:** Uncaptioned elements appearing in all outputs
  - **Solution:** Caption everything you want to control, forgot to caption studded belt and it appeared on many people randomly
  - *From: crinklypaper*

- **Problem:** Blocky/line artifacts in video generation
  - **Solution:** Use fp16 instead of scaled models, increase steps to 20-25, avoid using 6-step LoRA for quality
  - *From: Tonon*

- **Problem:** ComfyUI API moderation blocking content that works on official Wan site
  - **Solution:** Use other services like Higgsfield which may have different restrictions
  - *From: Drommer-Kille*

- **Problem:** ComfyUI Wan API extremely slow (10-30min vs 3min on official site)
  - **Solution:** Use official Wan site instead, ComfyUI locks for 5-15min per generation
  - *From: Drommer-Kille*

- **Problem:** Performance drop and VRAM issues with new WanVideoWrapper version
  - **Solution:** Keep load device on offload_device, don't use main_device. Model loading moved to sampler
  - *From: Kijai*

- **Problem:** Encoding takes ages with new ComfyUI version
  - **Solution:** Don't use --fast flag or specify optimizations like --fast fp16_accumulation. Autotune feature causes encode issues
  - *From: Kijai*

- **Problem:** Dark/vignetted frames at end of generations
  - **Solution:** Try generating only 81 frames instead of 97 at once, most wan models don't behave well above 81 frames
  - *From: seitanism*

- **Problem:** Audio node sample rate max incorrectly shows 2048
  - **Solution:** Don't change the default value, it gets resampled to what model needs anyway (16k)
  - *From: Kijai*

- **Problem:** WanAnimate depth input turns video green
  - **Solution:** Use blend method similar to VACE, but needs strict depth training to be reliable
  - *From: Nathan Shipley*

- **Problem:** Native context options cause tensor size mismatch with VACE
  - **Solution:** Doesn't work with VACE/I2V currently, needs edits for different conditioning dimensions
  - *From: Kosinkadink*

- **Problem:** Training LoRA on 3090 with OOM
  - **Solution:** Set blockswap to max and work backwards, slowly decrease resolution, train on 512 resolution
  - *From: crinklypaper*

- **Problem:** VACE ref image showing as extra frames
  - **Solution:** Recent change where ref image appears as starting 4 frames, 81 frames becomes 85
  - *From: hablaba*

- **Problem:** AudioCraft/Foley install breaking ComfyUI nodes
  - **Solution:** Use phazei's HunyuanVideo-Foley implementation instead, or restore protobuf to version 5.29.4
  - *From: Gleb Tretyak*

- **Problem:** VACE mask leaking into output
  - **Solution:** Use grow mask with negative expansion to shrink mask slightly inside the depth map
  - *From: HeadOfOliver*

- **Problem:** WanAnimate flipping vertical videos to horizontal in masking
  - **Solution:** Use FFMPEG command: ffmpeg -i name.mp4 -vf "scale=1080:1920" -c:a copy name_fixed.mp4
  - *From: BecauseReasons*

- **Problem:** Uni3c not working with WanVideo Long I2V Multi/InfiniteTalk
  - **Solution:** Issue related to context windows clashing, need to ask Kijai for solution
  - *From: mdkb*

- **Problem:** Slow initial model loading times
  - **Solution:** 65-80 seconds is normal for native with dual 5090s, single 5090 loads faster at ~44 seconds
  - *From: Baku*

- **Problem:** LoRA key not loaded errors with new Lightning LoRA on native ComfyUI
  - **Solution:** Use Kijai's converted versions with proper key naming (diffusion_model. prefix added) or wait for official re-upload with native compatibility
  - *From: Kijai*

- **Problem:** Wan VACE background replacement when not wanted
  - **Solution:** Unplug mask and bg image connections from the node
  - *From: Charlie*

- **Problem:** New Lightning LoRA acting oddly with Fun VACE model
  - **Solution:** Use flowmatch_distill scheduler instead of Euler for better results
  - *From: Kijai*

- **Problem:** Lightning LoRA still changes style too much
  - **Solution:** Main issue remains unresolved - prompting night scene still produces day scene
  - *From: Kijai*

- **Problem:** T2V Lightning LoRA degrades color when used on I2V
  - **Solution:** No solution provided, confirmed limitation
  - *From: Lodis*

- **Problem:** InfiniteTalk works with regular I2V node but not with Long I2V Multi/InfiniteTalk node
  - **Solution:** Use WanVideo ImageToVideo Encode node instead of the Long I2V Multi/InfiniteTalk node
  - *From: Vérole*

- **Problem:** New Lightning lora gives overexposed/lighting issues on low noise
  - **Solution:** Continue using lightx2v for low noise instead of new lightning lora
  - *From: Kijai*

- **Problem:** WanAnimate not following prompts with speedup loras
  - **Solution:** Use cfg and avoid first step 0 lora trick for better prompt adherence
  - *From: MysteryShack*

- **Problem:** Dark/night scenes not rendering properly with new Lightning
  - **Solution:** 
  - *From: Kijai*

- **Problem:** Red/oompa loompa face coloring
  - **Solution:** Remove relight lora and reduce lightx2v strength from 1.2 to 1.0
  - *From: mdkb*

- **Problem:** InfiniteTalk stuck at 80%
  - **Solution:** Check if it's in importing/vae encoding phase before actual generation - high GPU/CPU usage indicates it's still working
  - *From: patientx*

- **Problem:** SAM2 points editor ignoring boundary markers
  - **Solution:** Use Sam 2.1 heira large model, reduce expand to 2 instead of 10, bypass blocky node, and plug in negative coordinates
  - *From: mdkb*

- **Problem:** Torch 2.8 causing OOM issues
  - **Solution:** Revert to stable setup: torch 2.7.1, triton_windows-3.3.1.post19, sageattention-2.2.0, flash_attn-2.7.4.post1
  - *From: Cubey*

- **Problem:** WanAnimate changing clothes instead of just face
  - **Solution:** Use face detector node instead of SAM2, or ensure mask covers whole person as model prefers larger masks
  - *From: Draken*

- **Problem:** Camera zoom not working with i2v
  - **Solution:** Try 'camera dollies in' prompt, give it a specific thing to zoom to, move zoom description closer to start of prompt
  - *From: Draken*

- **Problem:** WanAnim looping error with context options
  - **Solution:** Don't use context options with WanAnim looping, or set frame window size equal to total frames
  - *From: Kijai*

- **Problem:** Mask issues over 81 frames
  - **Solution:** Check frame window settings and ensure proper configuration
  - *From: Charlie*

- **Problem:** Uni3C list index out of range error
  - **Solution:** Check that input video resolution matches generation resolution, ensure proper sizing
  - *From: Kijai*

- **Problem:** Uni3C can't handle modified timesteps
  - **Solution:** Don't use uni3c controlnet with samplers that use modified timesteps like dpm++_sde
  - *From: Kijai*

- **Problem:** Character likeness degrades over 77 frames
  - **Solution:** Use static camera instead of moving camera for better character consistency
  - *From: mdkb*

- **Problem:** OOM issues with newer versions
  - **Solution:** Downgrade to CUDA 12.8 with PyTorch 2.7.1 instead of 12.9 + 2.8.0
  - *From: Gleb Tretyak*

- **Problem:** Characters always have open mouths in Wan 2.2
  - **Solution:** Use livewallpaper lora or anime sex face lora at low strength, or use neutral face control with WanAnimate
  - *From: CFSStudios*

- **Problem:** Wan 2.5 API flagging innocent pirate ship images as IP infringement
  - **Solution:** The issue was specifically with pirate ship imagery - using a different image (building) worked fine. Suggested workaround is to use Qwen image edit to modify the image until it's accepted
  - *From: D-EFFECTS, Instability01*

- **Problem:** Getting bad results with Wan 2.2 VACE
  - **Solution:** Multiple users reporting reverting to 2.1 due to poor results with 2.2 fun/VACE
  - *From: Abx, Gleb Tretyak*

- **Problem:** Cars going backward in Wan generations
  - **Solution:** Try to add Pusa, it sometimes helps with that. It confuses the front and back on some models (car models)
  - *From: Zabo, Tonon*

- **Problem:** VACE mask leaking during inpainting
  - **Solution:** Extending the mask for mask input of vace encode fixed leaking. Inpainting mask is let's say a box 100x100, but the mask input is mask 105x105
  - *From: scf*

- **Problem:** Using fp16 models with native workflow gives weird results
  - **Solution:** Native workflow uses fp8, getting weird results with fp16 models using it
  - *From: yuvraj*

- **Problem:** Wan 2.2 inpainting showing dark black edges and white outlines on mask boundaries
  - **Solution:** Try using only the low sampler instead of both high and low samplers, set steps start 0 end 5
  - *From: SonidosEnArmonía*

- **Problem:** VACE uni3c not respecting ref/first frame image
  - **Solution:** No solution provided in discussion
  - *From: TheSwoosh*

- **Problem:** Wan 2.2 inpainting mask edge artifacts
  - **Solution:** Use white color for inpainting in control video, watch mask expand settings (example used 14)
  - *From: SonidosEnArmonía*


## Model Comparisons

- **WAN wrapper vs native memory usage**
  - Native uses 53GB VRAM vs wrapper which was causing OOM on same hardware
  - *From: HeadOfOliver*

- **InfiniteTalk vs WanS2V for lip-sync**
  - User prefers InfiniteTalk, but WanS2V easier to experiment with in ComfyUI
  - *From: Ablejones*

- **Wan 2.2 Pusa vs regular I2V**
  - Better adherence to prompt, movement, and image quality with Pusa
  - *From: . Not Really Human :.*

- **LightX2V vs waiting 15 minutes with Wan 2.1 T2V**
  - Regular T2V produces better results than speed LoRA
  - *From: Ghost*

- **Pusa with vs without comparison**
  - No visible difference observed in side-by-side test
  - *From: Dever*

- **I2V vs V2V quality**
  - I2V gives better quality than V2V
  - *From: ReDiff*

- **V2V vs I2V processing**
  - V2V basically wraps I2V, doesn't do actual multi-frame sampling
  - *From: mccoxmaul*

- **GGUF Q8 vs fp8_e5m2**
  - GGUF Q8 slightly slower but better quality, unless using lots of big LoRAs
  - *From: Kijai*

- **Context windows in WAN 2.2 vs 2.1**
  - WAN 2.2 context windows much better - 2.1 had warps and fuzz at transitions half the time, 2.2 only has overt warps 1 in 10 times
  - *From: blake37*

- **LTX Tiled VAE vs normal VAE decoder**
  - LTX version 5x faster with no apparent quality loss
  - *From: l҈u҈c҈i҈f҈e҈r҈*

- **NVME vs SATA for page file**
  - NVME page file provides massive speed improvement over SATA
  - *From: dg1860*

- **CausVid vs LightX2V**
  - CausVid is worse, was never intended for normal sampling, LightX2V at lower strength gives similar effects
  - *From: Kijai*

- **Multiple ComfyUI windows vs single window**
  - Multiple windows cause VSH combine to take 2 minutes, single window works better
  - *From: Kenk*

- **Pusa vs regular T2V**
  - Pusa on T2V 2.2 model gives strength comparable to I2V 2.2 and even more
  - *From: Mngbg*

- **Context with vs without end frames**
  - Start/End frame generation had better control - model anchored to end frame better, but continuation isn't great
  - *From: Dever*

- **Foley vs MMAudio**
  - Both have pros/cons, Foley doesn't need golden fps to be 25, works with 60fps, but tends to add background music too often
  - *From: . Not Really Human .*

- **Wrapper vs native workflows**
  - Wrapper has support for more models like infinite talk, native can't use tiny vae
  - *From: Kijai*

- **Wrapper vs native prompt adherence**
  - Wrapper workflow has much more prompt adherence compared to native, it actually listens to prompt
  - *From: ComfyCod3r*

- **Audio CFG impact on generation time**
  - CFG doubles the time and audio CFG triples
  - *From: Kijai*

- **Fun models vs Wan 2.2 14B I2V for first-frame-last-frame**
  - Wan 2.2 14B I2V works better than Fun models for temporal inpainting. Fun models are based on T2V and not as good as Wan team's work
  - *From: mamad8*

- **WanGP vs ComfyUI memory optimization**
  - WanGP under Windows/Pinokio only uses 9GB out of 16GB VRAM even on high VRAM setting, not as optimized as ComfyUI
  - *From: . Not Really Human .*

- **Native vs Wrapper for extended generations**
  - Native is slower with worse picture quality. Wrapper produces better results for multi-context generations
  - *From: N0NSens*

- **InfiniteTalk vs S2V (Wan 2.2)**
  - InfiniteTalk is more flexible than S2V and works at 25fps while S2V is 16fps. InfiniteTalk works poorly on 2.2 A14B model.
  - *From: Kijai*

- **InfiniteTalk vs MultiTalk**
  - InfiniteTalk has been giving better results than MultiTalk for long generations
  - *From: blake37*

- **CFG 1 vs CFG 3.5**
  - CFG 3.5 produces significantly better results than CFG 1, not even a competition
  - *From: Drommer-Kille*

- **InfiniteTalk vs S2V quality**
  - InfiniteTalk is better than S2V in opinion
  - *From: Juampab12*

- **5B model fast vs turbo variants**
  - Fast variant causes more changes to foreground and doesn't hold original image as well as turbo, however turbo causes color shifting and wobble camera more frequently
  - *From: Dita*

- **FusionX LoRA vs Light LoRAs for Wan 2.1**
  - FusionX much better quality but slower
  - *From: BecauseReasons*

- **Native vs Wrapper VRAM optimization**
  - Native can be optimized to match wrapper with proper settings (low VRAM, block swap)
  - *From: hicho*

- **V2V vs I2V for long generations**
  - V2V good for 40 seconds easily, I2V struggles beyond 10 seconds
  - *From: samhodge*

- **Pusa vs last-frame method for continuity**
  - Pusa better for motion continuity, last-frame method has jarring seams
  - *From: Kijai*

- **InfiniteTalk vs other seamless techniques**
  - InfiniteTalk first to seem almost seamless using last-frame technique
  - *From: Kijai*

- **Lightx2v vs Wan22-Lightning**
  - Older Lightx2v LoRAs (rank32/256) produce better quality than newer Lightning LoRAs
  - *From: Lodis*

- **Self forcing DMD vs other speed LoRAs**
  - Self forcing DMD is very good for 1.3B model, better than CausVid
  - *From: Zabo*

- **I2V native vs T2V pusa wrapper**
  - Visual comparison shows different results, choice depends on use case
  - *From: FL13*

- **InfiniteTalk vs MultiTalk**
  - InfiniteTalk is way better and makes MultiTalk almost redundant
  - *From: Kijai*

- **GGUF vs FP8 models**
  - GGUF models are faster (1 minute improvement) with comparable quality
  - *From: patientx*

- **Multi vs Infinite Talk**
  - Multi gives much more motion than Infinite
  - *From: N0NSens*

- **Audio Foley vs MMAudio**
  - MMAudio for little stuff, Foley for more complex scenes. Both have flaws like adding background music
  - *From: .: Not Really Human :.*

- **GGUF vs FP8 speed**
  - GGUF loads faster but steps are slower due to compression. About 1.5 sec slower per step
  - *From: hicho*

- **3 samplers vs 2 samplers for T2V**
  - 2 samplers works best for T2V according to testing
  - *From: DennisM*

- **InfiniteTalk vs Wav2Lip**
  - InfiniteTalk much more advanced, works with just image input
  - *From: TimHannan*

- **VibeVoice vs Chatterbox**
  - VibeVoice is 10x better, Chatterbox is not SOTA
  - *From: Juampab12*

- **Wan 2.2 vs 2.1 for lip sync**
  - Don't need InfiniteTalk with 2.2, 2.2 handles movement better
  - *From: N0NSens*

- **MagRef vs basic i2v model**
  - MagRef adds too much to character when using with Infinite
  - *From: Charlie*

- **5B vs 14B model motion capability**
  - 5B can provide more motion than 14B in vanilla I2V generation, understands prompts better for certain use cases
  - *From: Charlie*

- **Fun Control vs regular Wan 2.2 character consistency**
  - InfiniteTalk maintains better character consistency than FunControl, which alters character face and skin color significantly
  - *From: Cleo*

- **Power consumption: Wan vs Flux**
  - Wan uses significantly less power (200-226w) compared to Flux image generation (350w)
  - *From: VK (5080 128gb)*

- **MultiTalk vs InfiniteTalk**
  - MultiTalk wins - better quality, no confetti artifacts, similar completion time
  - *From: mdkb*

- **Wan 2.2 vs 2.1 for character identity**
  - Wan 2.2 keeps character identity much better, especially as low noise model in InfiniteTalk
  - *From: MysteryShack*

- **Fantasy Portrait + MultiTalk vs InfiniteTalk + Fantasy Portrait**
  - MT+FP produces stronger results with better facial landmarks and eye movement capture
  - *From: mdkb*

- **MultiTalk vs InfiniteTalk**
  - MultiTalk more compatible with other models as it doesn't modify first latent result, InfiniteTalk only works with I2V models but has better motion
  - *From: Kijai*

- **720x1280 vs 480x832**
  - 720x1280 better at keeping face consistent, 480x832 always messes up faces somehow
  - *From: vuuw*

- **Native vs Wrapper color handling**
  - Native handles start+end frame encoding better by default, wrapper needs fun_or_fl2v_model switch enabled
  - *From: lemuet*

- **Wan 2.2 Low model vs other upscaling**
  - 2.2 Low model + UltimateSD Upscaler produces better detail improvement than other techniques
  - *From: Juan Gea*

- **Wan 2.1 vs Wan 2.2 for Infinite Talk**
  - Attached comparison videos showing difference with same seed and settings
  - *From: Izaan*

- **HPS vs MPS LoRAs for I2V**
  - MPS performs better without artifacts, HPS adds unwanted details and redraws faces
  - *From: N0NSens*

- **Native vs Wrapper LoRA handling**
  - Native produces better results, wrapper requires different settings
  - *From: scf*

- **setLoras vs direct model merge for LoRAs**
  - Direct model merge gives better likeness than setLoras method
  - *From: mamad8*

- **5B vs 14B model**
  - 5B generates in 20 seconds (excluding vae) but is not a good replacement for 14B quality-wise
  - *From: crinklypaper*

- **Radial vs Sage attention**
  - Radial provides speed gains but messes with detail and mutes character emotion in infinitetalk
  - *From: blake37*

- **Fun 2.2 control vs core method for inpainting**
  - Fun control works but transformation only happens at the end, core method is smoother
  - *From: Dream Making*

- **HuMo vs Phantom**
  - Seems same as phantom so far, quite a bit better based on comparison page
  - *From: Kijai*

- **Fun Control vs Regular model vs USD upscaler**
  - USD is the worst and slowest
  - *From: N0NSens*

- **e5m2 vs e4m3 for Wan 2.2**
  - e5m2 significantly better for prompt adherence
  - *From: Hoernchen*

- **InfiniteTalk vs other lip-sync solutions**
  - Open source that's it, but it's def not the best
  - *From: JohnDopamine*

- **Fun VACE FFLF vs Fun InP vs regular FFLF**
  - Fun VACE FFLF works better than both Fun InP and regular FFLF
  - *From: Cseti*

- **Fun VACE vs 2.1 VACE for video continuations**
  - Fun VACE works much better for continuations, 2.1 VACE reference didn't work with 2.2 high noise
  - *From: seitanism*

- **Control video results 2.2 vs 2.1**
  - Results are way worse than 2.1 even with no loras
  - *From: ArtOfficial*

- **VACE 2.2 vs 2.1 for extension**
  - 2.2 works better for video extension with less color degradation
  - *From: Daflon*

- **HuMo vs Phantom**
  - HuMo is better than Phantom even without audio functionality working
  - *From: Kijai*

- **VACE 2.2 lighting integration vs 2.1**
  - 2.2 doesn't integrate environment lighting as well as 2.1 but has better reference adherence
  - *From: ingi // SYSTMS*

- **Old VACE vs New VACE 2.2**
  - 2.2 has better understanding of objects (kittens), but movement might be less realistic
  - *From: Zuko*

- **SageAttention vs default attention**
  - SageAttention patch being deprecated due to new native attention selection in ComfyUI
  - *From: Kijai*

- **Torch versions**
  - Avoid 2.8.0 due to compile issues, 2.7.1 good, 2.9 nightly seems fine
  - *From: Kijai*

- **HuMo vs InfiniteTalk**
  - HuMo has better lipsync and more natural results than InfiniteTalk/S2V, but lacks endless generation mode
  - *From: NebSH*

- **Q8 vs Q4 quantization**
  - Q8 gives more details compared to Q4
  - *From: xwsswww*

- **HuMo vs InfiniteTalk lip sync**
  - HuMo has better lip sync quality but both have limitations - HuMo limited to ~97 frames, InfiniteTalk better for longer content
  - *From: Rävlik*

- **fp8 vs bf16 for Wan models**
  - Full models (bf16) always best quality, but fp8 scaled good for prototyping or OOM issues
  - *From: ArtOfficial*

- **Wrapper vs native ComfyUI implementations**
  - fp8 in wrapper superior to GGUF, can push models further and do more
  - *From: mdkb*

- **VACE 2.1 vs 2.2 for tight control**
  - Not much difference for control + ref, 2.2 harder to work with due to lack of proper distill lora
  - *From: Kijai*

- **With vs without radial attention**
  - 170.37s vs 316.06s - radial attention nearly 2x faster, second also performs better at consistency and lipsync
  - *From: VRGameDevGirl84(RTX 5090)*

- **RTX 3090 vs RTX 5090 for Wan inference**
  - 205s vs 557s on same workflow - 5090 is significantly faster, about 2.7x speed improvement
  - *From: 𝕯𝖗. 𝕸𝖆𝖈𝖆𝖇𝖗𝖊 ☠*

- **LightX with vs without S2V**
  - LightX totally degrades S2V output quality and kills movement compared to without
  - *From: burgstall*

- **VACE 2.2 Fun vs VACE 2.1**
  - 2.2 has better quality but worse reference handling, no color shift between contexts is improved
  - *From: Piblarg*

- **Phantom vs VACE references**
  - Phantom references are on another level, true subject to video capability
  - *From: Ablejones*

- **Native vs Wrapper VACE performance**
  - Native gives much faster s/it performance than wrapper implementation
  - *From: yo9o*

- **RTX 5090 FE vs MSI Vanguard**
  - MSI Vanguard much quieter but more expensive, FE is slimmer but louder
  - *From: Hoernchen*

- **AMD 7900xtx vs RTX 5090**
  - 5090 chosen for 32GB VRAM over 24GB, despite AMD having shitty support
  - *From: Hoernchen*

- **VACE 2.2 Fun vs VACE 2.1 for inpainting**
  - VACE 2.1 better for spatial inpainting with masks, VACE Fun better for high motion inpainting and complex movement
  - *From: hablaba*

- **Multiple VACE embeds 2.2 Fun vs 2.1**
  - Multiple VACE embeds don't work as well in 2.2 Fun, mixing models in high/low gives better results
  - *From: JalenBrunson*

- **fp8 model quality ranking**
  - fp16 > bf16 > fp8_scaled > fp8_e4m3fn for quality
  - *From: Tony(5090)*

- **HuMo vs Infinite Talk motion**
  - HuMo has more motion and is much faster than Infinite Talk, but HuMo has 'stiff head' problem
  - *From: VRGameDevGirl84(RTX 5090)*

- **Resolution impact on speed**
  - 960x640 took 533 seconds vs 768x512 took 133 seconds with lightning LoRAs
  - *From: herpderpleton*

- **Context windows vs AnimateDiff**
  - Context windows hasn't worked as well as Animatediff for user, but animatediff didn't have I2V and worked terribly with T2V, only worked ok with controlnets
  - *From: xwsswww*

- **Humo fp16 vs fp8 vs q4km gguf**
  - Significant visual quality difference between fp16 and fp8, fp16 result is great
  - *From: patientx*

- **Wan 2.2 vs 2.1 for background handling**
  - Wan 2.2 is holding up better than 2.1 on BG but it fails characters
  - *From: chrisd0073*

- **LightX2V with 2.2**
  - LightX2V is not trained for 2.2 so it works poorly and CFG is just lot better
  - *From: Kijai*

- **Wan 2.1 vs 2.2 for faces**
  - 2.1 still superior for facial performance
  - *From: chrisd0073*

- **VACE 2.1 vs 2.2**
  - 2.2 has degradations compared to 2.1 in some workflows but has hidden relight feature
  - *From: Vérole*

- **With vs without torch.compile**
  - Massive difference without compile, but not useful if already using compile as it's already optimized
  - *From: Kijai*

- **bf16 vs fp16**
  - bf16 is safer due to larger range with less risk of overflow/underflow, fp16 will be less noisy. Can run fp16 with underflow/overflow detection to test if bf16 is needed
  - *From: mallardgazellegoosewildcat*

- **Wan 2.2 vs other models**
  - Getting closer to stepvideo/magi levels, definitely better than Wan 2.1
  - *From: mallardgazellegoosewildcat*

- **FastWan vs LightX2V for character consistency**
  - FastWan doesn't change character consistency as much as lightx2v, which is why it was used instead for magref infinite talk
  - *From: mdkb*

- **CausVid vs other speed LoRAs**
  - CausVid needs more steps but doesn't affect character consistency as much
  - *From: Piblarg*

- **VACE vs ControlNet training costs**
  - VACE is much cheaper than ControlNet - Flux ControlNet attempts cost $40k according to open model initiative
  - *From: mallardgazellegoosewildcat*

- **Phantom vs VACE for character consistency**
  - One user's reference was amazing at character consistency but failed to follow control video, while LightX 4/4 trashed character consistency but followed control video well
  - *From: Gleb Tretyak*

- **Wan 2.2 + VACE 2.2 fun in dual model mode**
  - Better than previous setup, faster and can hit higher resolutions
  - *From: mdkb*

- **5090 vs H100 performance**
  - Depends on batch size - if H100 can use its VRAM it edges out, but 5090 has fp4 advantage
  - *From: mallardgazellegoosewildcat*

- **T5 11GB vs Q6 quantized version**
  - Results look exactly the same, Q6 slightly faster (16 mins vs 19 mins) and uses less memory (95GB vs 105GB peak)
  - *From: mdkb*

- **Topaz vs Cosmos 4K upscaler**
  - Cosmos upscaler is better in some ways, Topaz results can be 'squiffy'
  - *From: mallardgazellegoosewildcat*

- **Phantom vs VACE for likeness**
  - Phantom is more powerful for likeness but VACE 2.2 has improvements over 2.1
  - *From: xwsswww*

- **Phantom+VACE vs other methods**
  - Best combination currently despite darkening unmasked areas issue
  - *From: xwsswww*

- **Wan-animate vs Runway Act 2**
  - It's basically Runway's act 2 but better than Runway according to comparisons on GitHub page
  - *From: VRGameDevGirl84(RTX 5090)*

- **2.1 lightx2v vs 2.2 version for wan 2.2**
  - Better luck with the 2.1 lightx2v than with the 2.2 version
  - *From: nacho.money*

- **Rank 32 vs Rank 256 LoRA**
  - Rank 256 is way better, solves major problems and gives more realistic motion
  - *From: Ruairi Robinson*

- **CFG 1 vs CFG 3.5**
  - Speed difference is 25 seconds (60s to 85s), but CFG 3.5 fixes overexposure
  - *From: Drommer-Kille*

- **Wan Animate vs VACE**
  - Surpasses VACE in terms of benchmarks
  - *From: Lodis*

- **Wan Animate vs standard V2V models**
  - People-focused models do longer videos than standard v2v models
  - *From: Drommer-Kille*

- **Context vs non-context processing**
  - Without context is much faster (161 frames), context better only for really long gens to avoid degradation
  - *From: NebSH*

- **Animate VRAM usage vs Wan 2.2**
  - Animate is more VRAM hungry - can do 864x1344 with wan2.2 but get OOM with animate
  - *From: scf*

- **Wan 14B vs 5B models**
  - 14B blows 5B out of the water - much better quality, sharpness, and 3D awareness. 5B destroys sharpness
  - *From: mallardgazellegoosewildcat*

- **Wan vs VACE for control**
  - Wan animate controls too much, which makes it not better than VACE for some use cases
  - *From: shockgun*

- **LCM vs dpmpp_sde scheduler**
  - LCM might be a bit better for animated characters
  - *From: DawnII*

- **Chatterbox vs VibevoIce**
  - Chatterbox > vibevoice according to user preference
  - *From: 🦙rishappi*

- **WanAnimate vs VACE quality**
  - WanAnimate generates good results in third attempt without parameter tweaking, unlike VACE 2.1 which required much tweaking
  - *From: Nekodificador*

- **4-step LoRA vs full workflow**
  - 4step lora produces much cleaner output than the full, slower workflow
  - *From: 314273375717425152*

- **bf16 vs fp8 quality**
  - bf16 is better than fp8, though not much better but indeed better
  - *From: slmonker(5090D 32GB)*

- **Face quantized vs non-quantized**
  - q3km (face non quantized) vs q2km (face quantized) showed minimal difference in quality
  - *From: patientx*

- **WanAnimate vs other models for vid2vid**
  - WanAnimate is clearly best for vid2vid
  - *From: Kijai*

- **HuMo vs InfiniteTalk for audio**
  - HuMo is great but doesn't support proper long gens, InfiniteTalk still feels best for audio in practice
  - *From: Kijai*

- **Q2 vs Q3 quantization quality**
  - Q3 has higher detail and has loras merged instead of added on generation, but Q2 looks same for size reduction
  - *From: patientx*

- **WanAnimate vs website results**
  - Website version tracks pupils perfectly while local version doesn't
  - *From: A.I.Warper*

- **20 steps vs 50 steps for Wan VACE 2.2**
  - 20 steps too little for VACE 2.2, normal is 50 steps
  - *From: Kijai*

- **Phantom vs WanAnimate likeness**
  - Phantom is overall 1:1 better likeness, WanAnimate similar but not exactly 1:1 especially for fine details
  - *From: Piblarg*

- **VACE with character Lora vs other methods**
  - Plain VACE with character Lora works better, other ref details like specific clothes don't bleed into generation
  - *From: hablaba*

- **WAN website vs local**
  - The difference between website wan animate and local is huge, at least with example workflow
  - *From: Juampab12*

- **Lucy Edit 5B vs 14B**
  - Only 5B model is open-source, 14B model is behind their api and charges
  - *From: ArtOfficial*

- **GGUF quantization levels q2k vs q3 vs q4**
  - Q4 has highest detail, q3 is close, q2k noticeably worse. Q3-Q4 difference is less than q2-q3 difference
  - *From: The Punisher*

- **Wan Animate vs VACE+Phantom**
  - VACE+Phantom still considered best overall, better likeness than Wan Animate
  - *From: xwsswww*

- **Wrapper vs Native workflows**
  - Wrapper has better prompt adherence and looping, native has better gaze control
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Wan Animate vs Phantom+VACE+PUSA**
  - Wan Animate surpassed the massive workflow with far less tweaking required
  - *From: DawnII*

- **GGUF quantization levels (q2-q3-q4 vs q6-fp8_e5m2-bf16)**
  - q4 provides good balance, higher precision shows better quality
  - *From: patientx*

- **LightX 6 steps vs no LightX 40 steps**
  - LightX with 6 steps produces better results
  - *From: Ruairi Robinson*

- **Phantom vs WanAnimate for likeness**
  - Quality_Control disagrees that Phantom is better than WanAnimate for accuracy
  - *From: Quality_Control*

- **Qwen2.5VL vs Florence2 for masking**
  - Qwen2.5VL should get better results than Florence2
  - *From: piscesbody*

- **AMD vs NVIDIA performance**
  - AMD works differently, requires different block swap settings
  - *From: patientx*

- **GGUF q4km (10.7gb) vs q8 (18gb) vs fp8_e5m2 (17.1gb) vs bf16 (32.1gb)**
  - Quality comparison shown
  - *From: patientx*

- **DWPose vs VitPose-H**
  - VitPose-H is what WanAnimate uses, though quality difference shown
  - *From: Kijai*

- **UniAnimate DWPose node vs regular**
  - UniAnimate version cleaned up moves that other estimator couldn't handle, but uses same model with tunable parameters
  - *From: T2 (RTX6000Pro)*

- **ONNX vs torch scripts for pose processing**
  - Torch scripts are faster - 1m28sec vs 3 minutes for ONNX on CPU
  - *From: patientx*

- **Euler scheduler vs DPM++ for WAN Animate**
  - Euler scheduler preferred - less jiggly and better contrast
  - *From: CaptHook*

- **Sage vs flash attention performance**
  - Sage can be 100% faster than flash attention on consumer GPUs
  - *From: Kijai*

- **Q6 vs fp8 model quality**
  - Q6 model preferred as fp8 model was slightly blocky
  - *From: CaptHook*

- **Native workflow vs wrapper for Animate**
  - Native workflow worked better, wrapper had OOM issues and was slower
  - *From: traxxas25*

- **Q_K_M vs fp8_Scaled models**
  - No much difference in quality, fp8 is slower
  - *From: Léon*

- **Wan platform vs ComfyUI implementation**
  - Better results on wan.video site, ComfyUI missing pose retargeting
  - *From: chrisd0073*

- **PUSA vs VACE for extensions**
  - PUSA is more difficult to use, color drifts like VACE, motion is different kind of bad. VACE has quality issues but 'worked'
  - *From: lostintranslation*

- **Wan Animate with vs without preprocessor**
  - New preprocessor nodes give cleaner 1:1 transfer and better eyes compared to standard workflow
  - *From: VRGameDevGirl84(RTX 5090)*

- **VACE vs PUSA for ID consistency**
  - VACE still gets better ID consistency, but stylized works really well with PUSA
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Wan 2.2 vs Wan 2.1 VACE**
  - New qwen edit model is an improvement for sure and very awesome
  - *From: Lodis*

- **Wan 2.2 vs Veo 3**
  - Wan 2.2 is already better than Veo 3 if you combine the different models
  - *From: ZeusZeus (RTX 4090)*

- **VACE 2.1 vs Animate for face consistency**
  - VACE 2.1 actually seems better at all kinda shots for keeping same face
  - *From: 🦙rishappi*

- **VACE 2.1 vs Animate for wide shots**
  - VACE (2.1) is better at that from my tests for wide shots
  - *From: ˗ˏˋ⚡ˎˊ-*

- **WAN 2.5 vs VEO 3**
  - I2V looks better than VEO 3, T2V not convinced yet. Audio quality behind VEO 3 with 'jzzzzzzz' noise
  - *From: DawnII*

- **WAN 2.5 vs WAN 2.2**
  - WAN 2.5 worse than Wan2.2 5B on arena, looks like more of a 5B continuation than 2.1/2.2 continuation
  - *From: yi*

- **WAN vs StepVideo**
  - StepVideo has much stronger benchmark scores than wan/hunyuan according to arxiv papers
  - *From: mallardgazellegoosewildcat*

- **Wan 2.5 vs Wan 2.2**
  - Wan 2.5 gives better results but adds complexity, time, and RAM requirements
  - *From: Draken*

- **Wan 2.5 audio vs other open source models**
  - Infinitely better sound than any open source video model
  - *From: seitanism*

- **SAM 2.1 vs SAM 2.0**
  - SAM 2.1 is lot better than 2.0
  - *From: Kijai*

- **Wan Animate vs Live Portrait with glasses**
  - Wan Animate works with glasses while Live Portrait makes eyes messy
  - *From: VRGameDevGirl84(RTX 5090)*

- **SOTA video generation stack**
  - Wan animate + V2V infinite talk at 50% denoise is current SOTA
  - *From: ArtOfficial*

- **SOTA alternative**
  - Wan 2.5 with fsdp and some ram torch
  - *From: Benjimon*

- **Audio quality**
  - Wan 2.5 audio seems like mmaudio quality
  - *From: JohnDopamine*

- **Wan 2.5 pricing**
  - 50 cents a video, similar to Veo3 cost
  - *From: VK (5080 128gb)*

- **Wan 2.2 vs Wan 5B speed**
  - 5B was same speed as 14b with lightx
  - *From: VK (5080 128gb)*

- **Wan 2.5 vs previous versions**
  - Prompt adherence and video quality is on another level
  - *From: Zabo*

- **Wan 2.5 vs InfiniteTalk/HuMo**
  - Wan 2.5 audio input lipsync is worse than infinitetalk/humo
  - *From: Juampab12*

- **Wan 2.5 vs previous versions**
  - Only about 20% better for pure video gen, but has new features
  - *From: yi*

- **Waver 1.0 vs Wan 2.5**
  - Waver 1.0 closed source 12B model is still far better for pure video generation
  - *From: yi*

- **StepVideo and Magi vs Wan 2.5**
  - StepVideo and Magi are both better than Wan 2.5, probably similar size
  - *From: mallardgazellegoosewildcat*

- **VACE 2.1 vs Wan 2.5**
  - ID preservation is better in VACE 2.1
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Wan 2.2 vs Wan 2.5**
  - Wan 2.2 better than Wan 2.5 according to one user, while another says smoothness is similar but 2.5 has more powerful prompt control
  - *From: Abx/toyxyz*

- **HunyuanV vs Wan**
  - HunyuanV has better VAE than Wan and is already 24fps, dataset more suited to some users' style
  - *From: mallardgazellegoosewildcat/JohnDopamine*

- **2.2 FUN VACE vs other methods**
  - 2.2 FUN VACE is the best available, much better than framepack or diffusion forcing
  - *From: seitanism*

- **StepVideo vs Wan 2.5**
  - StepVideo looks better than Wan 2.5 and can be run today with blockswapping
  - *From: mallardgazellegoosewildcat*

- **Wan 2.2 vs Veo3 quality**
  - Wan 2.2 can sometimes match Veo3 quality
  - *From: mallardgazellegoosewildcat*

- **LTX vs Wan competition**
  - Don't think LTX can compete with Wan, only maybe Hunyuan with their upcoming video model
  - *From: Lodis*

- **Current vs past AI video generation**
  - Two years ago we were excited for Cogvideox 2B model, showing how far things have come
  - *From: VK*

- **Wan 2.1 vs 2.2**
  - 2.2 better for general looks, 2.1 has more control options. 2.2 works best for complex detail needs, 2.1 better for complex motions
  - *From: Tonon*

- **VACE 2.1 vs Fun VACE 2.2**
  - VACE 2.1 generally better regarded, Fun VACE 2.2 better for fast motion and maintaining likeness
  - *From: Kijai*

- **fp8 vs bf16**
  - bf16 provides better quality, reduces texture chatter, fp16 math better than bf16 if no overflows but bf16 prevents overflows
  - *From: Juampab12*

- **RTX 3090 vs 5070ti for video**
  - Similar speed for video generation, 3090 has older tensor cores but Int8 support, 5070ti not worth upgrading to
  - *From: mallardgazellegoosewildcat*

- **Distilled models vs original models**
  - Good distills tend to be higher quality than original if using modern methods, but with reduced diversity
  - *From: mallardgazellegoosewildcat*

- **Wan2.2 vs AnimateDiff**
  - WanAnimate takes things to whole new level compared to AnimateDiff
  - *From: T2 (RTX6000Pro)*

- **Seedream 4 vs other models**
  - Seedream 4 is best on fal platform, crushes nano banana in image editing
  - *From: ZeusZeus (RTX 4090)*

- **Wan 2.5 vs Veo3**
  - Wan 2.5 costs less per generation than Veo3 but lacks really good audio
  - *From: Gateway {Dreaming Computers}*

- **I2V vs T2V for creative work**
  - T2V might overtake I2V because you can prompt short stories for unique visuals vs limited single scene in I2V
  - *From: Rainsmellsnice*

- **T2V vs I2V preferences**
  - T2V with good reference more interesting than I2V, T2V with LoRAs is ideal
  - *From: Ablejones*

- **HailuoV2 vs Veo 3 for sword fights**
  - HailuoV2 beats Veo 3 with ease, Veo 3 behaves like video game with repetitive swings
  - *From: Xodroc*

- **Kling vs Veo 3**
  - Kling also robustly beats Veo 3 sometimes
  - *From: mallardgazellegoosewildcat*

- **VACE 2.2 vs 2.1**
  - Main advantage is better motion handling, especially fast motion and background objects
  - *From: Izaan*

- **New Lightning LoRA vs previous v1.1**
  - More motion but still overly bright, 4 steps better than 6 steps
  - *From: Kijai*

- **Wan 2.5 vs Veo3 fast**
  - Veo3 still hard to beat for some things but Wan 2.5 getting closer, though Veo3 not cheap
  - *From: Gateway*

- **New Lightning LoRA vs old lightx2v for 2.1**
  - Initial lightx2v is near perfect for 2.1, new ones highly fine-tuned for 2.2
  - *From: Kijai*

- **lightx2v vs new Lightning 2509 on low noise**
  - lightx2v still better, new lightning has exposure issues but better details
  - *From: Kijai*

- **LYNX vs Phantom performance**
  - LYNX uses 3 cfg passes like Phantom, HuMo 1.7B uses 4 passes
  - *From: Kijai*

- **Lightning lora vs dyno full model**
  - Full model performs drastically better, lora extraction problematic
  - *From: Kijai*

- **Pusa vs other models for anime**
  - Very different look with more muted colors, not necessarily bad but different style
  - *From: Drommer-Kille*

- **Lightning loras vs lightx2v**
  - lightx2v provides better movement and realism than lightning loras
  - *From: xwsswww*

- **Enemyx vs wildminder VibeVoice**
  - Enemyx version produces fewer weird artifact noises
  - *From: mdkb*

- **MagRef vs Phantom for character swapping**
  - MagRef better for character swapping - successfully swapped 5 people in video, better than Phantom for that use case
  - *From: mdkb*

- **Palingenesis vs Dyno model**
  - Palingenesis on low setting outperformed Dyno on high for Silent Hill style
  - *From: patientx*

- **Q8 GGUF vs fp8_scaled**
  - User reports Q8 runs more smoothly, but both produced poor quality on lower-end hardware
  - *From: Gill Bastar*

- **Wan 2.2 vs 2.1 for realism**
  - Wan 2.2 is easily better than basic Flux for realism
  - *From: Drommer-Kille*

- **VACE 2.1 vs FunVace 2.2 and Animate**
  - For reference preservation, VACE 2.1 beats FunVace 2.2 and Animate
  - *From: ˗ˏˋ⚡ˎˊ-*

- **LongLive performance**
  - Very fast (2 minutes on 1 H100) but quality concerns
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Wan 2.1 14B vs 1.3B**
  - wan 2.1 14b is almost identical as 1.3b according to scoring results
  - *From: mamad8*

- **Sora 2 vs current open source models**
  - the quality is nuts nothing i even close
  - *From: Janosch Simon*

- **Hunyuan 3D vs Tripo for image to 3D**
  - Last time i checked it was worse than OS version of Tripo
  - *From: Drommer-Kille*

- **Kandinsky 5.0 T2V vs Wan models**
  - It outperforms larger Wan models (5B and 14B) and offers the best understanding of Russian concepts in the open-source ecosystem
  - *From: Zabo*

- **Merged vs GGUF LoRAs**
  - GGUF applied on the fly is usually stronger, merge adds more likeness in experience
  - *From: Kijai/scf*

- **Kandinsky 3 was competitive with other image models**
  - Was really good, had pixel-space upscale model
  - *From: mallardgazellegoosewildcat*


## Tips & Best Practices

- **Use arc shot prompts for camera movement in WAN**
  - Context: For achieving specific camera movements through text prompts
  - *From: DennisM*

- **Mention camera motion several different ways throughout the prompt when using speed LoRAs**
  - Context: Speed LoRAs affect motion, so repetition helps ensure camera movement is followed
  - *From: DennisM*

- **Mask out face and denoise with 0.6 or 0.7 for lip-sync**
  - Context: For better lip-sync results, raw latent noise mask looks messy
  - *From: Ablejones*

- **Right-click save videos only when getting useful results**
  - Context: Keeps output folder clean instead of saving everything automatically
  - *From: Kijai*

- **Match audio and video length beforehand using ffmpeg**
  - Context: For InfiniteTalk, sync audio with video streams to handle silence properly
  - *From: Geoff*

- **Duplicate your image and use it for more than 1 frame with I2V**
  - Context: When using image-to-video generation
  - *From: Kijai*

- **Boost LoRA strength with 2.1 Pusa to get more of your init image**
  - Context: When you want stronger adherence to input image
  - *From: Kijai*

- **Don't add noise on the 2nd sampler in 3-sampler workflows**
  - Context: When using multiple KSamplers
  - *From: Kijai*

- **Enable CFG on first sampler when using 3 samplers with LoRA disabled**
  - Context: To jump start motion in first few steps
  - *From: Kijai*

- **Use box masks instead of precise masks for better results**
  - Context: When character moves in video, precise masks can be off
  - *From: Kijai*

- **Higher LoRA strength = more adherence to image but cost of motion/dynamics**
  - Context: Balancing image fidelity vs motion
  - *From: DawnII*

- **Use GPT to generate detailed prompts**
  - Context: For lip-sync and character animation, give image to GPT with simple instruction like 'she is singing' to generate detailed prompts
  - *From: VRGameDevGirl84(RTX 5090)*

- **Stick to standard resolutions for quality**
  - Context: Non-standard resolutions impact quality but not performance - use 832x480, 1280x720, 960x720
  - *From: .: Not Really Human :.*

- **Use high CFG on high noise for wacky results**
  - Context: For experimental/creative outputs with Pusa
  - *From: Kijai*

- **Use ChatGPT to modify prompts according to example prompts**
  - Context: When WAN isn't following instructions well, especially for camera movement
  - *From: Gill Bastar*

- **Use 9 or 13 frames minimum for context extension**
  - Context: For practical video extension using context frames
  - *From: Kijai*

- **Lower high LoRA strength for better motion control**
  - Context: User found 0.5 for high and 1 for low worked better than higher values
  - *From: Dever*

- **Use ColorMatch node for consistency between segments**
  - Context: When extending videos to maintain color grading consistency
  - *From: Juampab12*

- **Keep character in frame for I2V context windows**
  - Context: I2V with context windows only works when character stays in frame, otherwise snaps back to init image
  - *From: Kijai*

- **Use upscale node x2 when reinjecting last frame**
  - Context: Helps when extending videos using frame reinjection method
  - *From: 𝕯𝖗. 𝕸𝖆𝖈𝖆𝖇𝖗𝖊 ☠*

- **Use LightX2V at lower strength instead of always 1.0**
  - Context: Slower generation but potentially better quality
  - *From: Kijai*

- **Always post before mounting PC inside case**
  - Context: Hardware troubleshooting
  - *From: Kenk*

- **Never skim on motherboard or PSU**
  - Context: Hardware reliability
  - *From: Kijai*

- **Close ComfyUI tab and open new one for stability**
  - Context: When experiencing generation issues
  - *From: Kenk*

- **Check SMART values for HDD issues**
  - Context: When PSU problems affect storage
  - *From: Dream Making*

- **Use 3 KSampler setup for better motion**
  - Context: Running first 2 steps without lightx/lightning seems to really improve motion drastically
  - *From: BecauseReasons*

- **Stay around 720p for best quality**
  - Context: Better to stay around 720p rather than going to 1920x1080 directly
  - *From: Kijai*

- **Avoid VRAM going past 95%**
  - Context: Monitor VRAM use and balance it out, avoid it going past 95% to avoid huge speed loss from running out of VRAM
  - *From: Kijai*

- **Use 2-3 GB VRAM reserve if multitasking**
  - Context: 2-3 usually enough if you use PC while generating and have monitor plugged to same GPU
  - *From: Kijai*

- **Hoard models while you can**
  - Context: Due to potential legal crackdowns making distribution more fragmented
  - *From: Phr00t*

- **Use TAESD preview for better quality previews**
  - Context: Enable animated previews in Video Helper Suite options and use TAESD for much better preview quality
  - *From: JohnDopamine*

- **Don't tag users repeatedly for general questions**
  - Context: Only tag for important bugs, new releases, or when the person will specifically benefit
  - *From: Kijai*

- **Use audio cfg higher than 1 for aggressive content**
  - Context: Play with audio cfg cause it's aggressive, need it higher than 1 to get character to be more aggressive, max around 6
  - *From: Charlie*

- **Don't use bong_tangent or beta57 schedulers for less than 10 total steps**
  - Context: Both schedulers were designed with 20-40 steps in mind
  - *From: Ablejones*

- **Use res_2s_ode sampler for more stability**
  - Context: Version that doesn't add SDE noise and is more stable than regular res_2s
  - *From: Ablejones*

- **Prompt for shoes/feet to get full body shots**
  - Context: Old SDXL trick that works with Wan for generating full body views
  - *From: DennisM*

- **Use 'wide shot' for full body compositions**
  - Context: Wan tends to favor top torso, wide shot helps get full body
  - *From: DennisM*

- **Save LoRA checkpoints every 200 steps to avoid overfitting**
  - Context: Makes it easier to find the sweet spot before overfitting occurs
  - *From: Ryzen*

- **Don't use NAG with CFG > 1**
  - Context: Negative prompt will have really high and sometimes unwanted/uncontrollable impact
  - *From: mamad8*

- **Use Kijai's weights for compatibility**
  - Context: Even if other versions exist, prob best to use the ones Kijai has for compatibility in case there is a difference
  - *From: JohnDopamine*

- **Use 2 samplers with different CFG values**
  - Context: Use CFG 3.5 in high noise sampler and CFG 1 in low noise sampler, with no lora in high sampler and 4-step lora in low noise sampler
  - *From: Drommer-Kille*

- **Create mask shape x2 into Mask Batch Multi for multi-character**
  - Context: For multi-character InfiniteTalk setups
  - *From: samhodge*

- **Use last frame as start_image and original face as end_image for character consistency**
  - Context: When character has turned away from camera, use this technique with I2V to get intermediary frames where face is visible
  - *From: gordo*

- **Use Uni3C camera control with static video for still camera**
  - Context: To prevent camera slowly zooming in Wan 2.2 generations
  - *From: Juampab12*

- **Don't see much point past 720p with these models**
  - Context: Rather than generating at higher resolution in one go, better to upscale afterward if needed
  - *From: Kijai*

- **Use 'then' and 'while' for sequential prompting**
  - Context: For targeting specific timing in generations, commas separate actions
  - *From: Cubey*

- **Use random seed for multi-sampling workflows**
  - Context: When doing several samplings to avoid burning generation with same seed
  - *From: Kibito*

- **For face replacement, use VACE with 2.1**
  - Context: Recommended approach for face replacement workflows
  - *From: N0NSens*

- **Balance new noise carefully with Pusa**
  - Context: Difficulty is balancing continuity vs accuracy when using Pusa
  - *From: Kijai*

- **Manually cut and paste subjects to single canvas for best VACE results**
  - Context: Better than simple concatenation for multi-subject reference images
  - *From: Kijai*

- **Use overlap of 4-12 frames for video extension**
  - Context: Practical range is 6-8 frames at 24/30fps, adjust for motion complexity
  - *From: Akumetsu971*

- **Use scientific method for troubleshooting**
  - Context: Make hypothesis and null hypothesis, try to disprove null hypothesis systematically
  - *From: samhodge*

- **Match tool versions by release date**
  - Context: Don't mix January 2024 tools with August 2025 tools - they won't work together
  - *From: samhodge*

- **Motion is high noise, detail is low noise**
  - Context: Understanding the dual noise expert architecture in Wan 2.2
  - *From: Charlie*

- **Use VACE for fight scene replication**
  - Context: For Matrix-style action sequences
  - *From: Charlie*

- **Drop resolution to 480 then upscale**
  - Context: When context windows crash due to RAM limits
  - *From: cyncratic*

- **Use block swapping for higher resolutions**
  - Context: To fit higher resolutions in VRAM
  - *From: N0NSens*

- **Use LightX 2.1 lora at strength 3 for 2.2 high, then LightX 2.2 lora for low noise version**
  - Context: For better results with 6 total steps
  - *From: Zabo*

- **Higher rank LoRAs can be heavy with GGUF, may get similar improvement by increasing LoRA strength**
  - Context: When using unmerged LoRAs with GGUF models
  - *From: Kijai*

- **Use 4 frame batch to prevent shifting/changing initial frame with PUSA**
  - Context: Improves consistency in video generation
  - *From: 𝕯𝖗. 𝕸𝖆𝖈𝖆𝖇𝖗𝖊 ☠*

- **Use shorter prompts with InfiniteTalk**
  - Context: Long prompts get confused
  - *From: Charlie*

- **Add silence at end of audio to stop lip movement**
  - Context: InfiniteTalk will keep moving lips without silence
  - *From: Kijai*

- **Schedule lora strength to 0 for first steps**
  - Context: Example: 0,3,3 strength schedule instead of using extra ksampler
  - *From: hablaba*

- **Use basic prompts for InfiniteTalk**
  - Context: Don't do long elaborate prompts
  - *From: Charlie*

- **Test on 250 frames for InfiniteTalk**
  - Context: Good starting length
  - *From: Charlie*

- **Use PNG format for workflow sharing**
  - Context: Only format Discord won't erase metadata from
  - *From: Dita*

- **Use looping LoRA at 0.25-0.5 strength**
  - Context: When trying to achieve natural looping around 101f or 121f
  - *From: The Shadow (NYC)*

- **Don't try to target magic sigma values**
  - Context: High/low split should be determined by sigma scheduling, not fixed values
  - *From: Kijai*

- **Use 4-6 steps with linear split for best results**
  - Context: Manually pick sigmas for low step generation
  - *From: phazei*

- **Use upscaling tools after generation for better video quality**
  - Context: To achieve smooth, high-quality results seen on social media
  - *From: Charlie*

- **Hide imperfections like hands behind back**
  - Context: Creative positioning to work around model limitations
  - *From: MysteryShack*

- **Clean input folder regularly**
  - Context: ComfyUI can choke if input folder gets filled with thousands of images
  - *From: JohnDopamine*

- **For best InfiniteTalk workflow: create your video first, then process with InfiniteTalk as V2V**
  - Context: When doing complex video generation with multiple steps
  - *From: MysteryShack*

- **Use overlap of 8 instead of 40 for faster processing**
  - Context: When using context options in long video generation
  - *From: mdkb*

- **Don't try higher steps with certain workflows - gives worse results**
  - Context: When using MultiTalk workflows
  - *From: Flipping Sigmas*

- **Use at least 1024x1024 input then upscale**
  - Context: When using tiled_decode for quality vs flickering tradeoff
  - *From: Gill Bastar*

- **Set MPS on high and HPS on low with 1:1 ratio**
  - Context: For better fast motion results with reward LoRAs
  - *From: Lodis*

- **Lower Pusa strength to follow prompt more but output may become incoherent**
  - Context: When using Pusa extension with movement
  - *From: FL13*

- **Moving from 480p to 720p is best fix for faces**
  - Context: Better than trying to fix faces with upscalers
  - *From: vuuw*

- **Use low denoise for upscaling to preserve original content**
  - Context: When using t2v models for upscaling, use denoise 0.1-0.79, with 0.1 for polish and higher values for more changes
  - *From: mdkb*

- **Increase padding and mask blur for 4K upscaling**
  - Context: For 4K upscaling to reduce seams, use padding at 128 and mask blur at 32
  - *From: FL13*

- **Use simple positive prompts for upscaling**
  - Context: For upscaling, just use 'high quality, 4k, realistic lighting' instead of original generation prompt
  - *From: FL13*

- **Use higher resolutions (960x544+) to avoid slow motion**
  - Context: When generating videos, lower resolutions like 832x480 tend to produce slow motion
  - *From: N0NSens*

- **Set empty embeds to 1 frame and enable LoRA merge for better results**
  - Context: When using wrapper, this produces more native-like image quality
  - *From: scf*

- **Use 0.08 denoise on USDU upscaler workflows**
  - Context: For splitting long videos into segments for processing on lower VRAM cards
  - *From: mdkb*

- **Connect preview images node to inputs to debug empty tensor issues**
  - Context: When troubleshooting color match or similar nodes
  - *From: Akumetsu971*

- **Use silent audio with infinite talk for pose generation without speech**
  - Context: Allows character animation without talking when no vocals needed
  - *From: Kijai*

- **Use sageattn with infinite for better performance**
  - Context: When using infinite talk, sageattn is recommended or it's slower
  - *From: Kijai*

- **Set motion_frame to 9 for infinite talk**
  - Context: When using infinite talk, don't need colormatch and motion_frame should be 9
  - *From: Kijai*

- **Use depth mask for best inpainting results**
  - Context: When doing inpainting with base model, depth mask gives best results
  - *From: Dita*

- **Play with less steps on high noise side for Wan 2.2**
  - Context: You can do less steps on high noise side, leaving it noisier for better results
  - *From: Kijai*

- **Use feathered mask before SEGS to avoid differential diffusion issues**
  - Context: Feather the mask before putting into SEGS if you want feathered mask but not differential diffusion
  - *From: Ablejones*

- **Use fp8 in fast mode to get most out of RTX 5090**
  - Context: For optimal performance on high-end hardware
  - *From: Kijai*

- **Sage Attention increases speed a lot at 720p but won't reduce memory use**
  - Context: Already enabled in model loader
  - *From: Kijai*

- **For better VACE reference respect, don't just plug image into both input frames AND ref images**
  - Context: When wanting ref image to be more respected in VACE
  - *From: Kijai*

- **Use 3-2 pulldown technique to sync different frame rates**
  - Context: To sync 16fps Wan 2.2 with 24fps models like InfiniteTalk or mmaudio
  - *From: nacho.money*

- **Use 'r' hotkey to refresh models/loras without restarting ComfyUI**
  - Context: When adding new models or loras
  - *From: scf*

- **Remove background and composite yourself for better results**
  - Context: When using multiple reference images
  - *From: Kijai*

- **Use lower rank lora to avoid memory issues when running unmerged**
  - Context: When having VRAM problems with loras
  - *From: Kijai*

- **Can use unmerged loras at high noise and merged at low noise**
  - Context: Managing VRAM usage with loras
  - *From: N0NSens*

- **Power limit GPU to 280W for minimal performance hit**
  - Context: Managing heat and power consumption
  - *From: daking999*

- **Never install requirements.txt directly to avoid dependency conflicts**
  - Context: 90% of dependency versions aren't hard requirements
  - *From: Kijai*

- **Use same venv for over a year by manually managing dependencies**
  - Context: Avoids most installation issues
  - *From: Kijai*

- **Use GitHub Desktop for switching branches and trying PRs**
  - Context: Simplifies git operations for testing
  - *From: Kijai*

- **Test VACE without speed loras first to understand base capabilities**
  - Context: Isolate VACE performance from lora effects
  - *From: mdkb*

- **Use SAM 2 with points editor or Florence 2 for automatic masking**
  - Context: For masking moving targets in video
  - *From: mdkb*

- **Match GGUF setups with fp8_e5m2 wrapper setups as fallback**
  - Context: If one doesn't work smoothly, try the other
  - *From: mdkb*

- **Use detailed prompts and 1:1 input images, resize to 1024x512, set frames to 121**
  - Context: For better VACE results
  - *From: drbaph*

- **Connect images and masks outputs to VACE encode node**
  - Context: Masks indicate start/end frames or areas not to edit
  - *From: Piblarg*

- **Use CFG 6+ with reward LoRAs for better quality**
  - Context: Higher CFG needed when using distillation LoRAs vs original 3-pass CFG
  - *From: Kijai*

- **Boosting lightx2v strength makes characters more expressive/angrier**
  - Context: Balancing emotion intensity in HuMo generations
  - *From: Kijai*

- **Describe the background precisely in prompts**
  - Context: Helps with HuMo quality and prevents gray/blurry backgrounds
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Use normalize node for audio**
  - Context: Helps prevent overexposed/plasticky look in HuMo generations
  - *From: Kijai*

- **Round masks rather than complex shapes**
  - Context: Sometimes works better than detailed masking, prevents giant people artifacts
  - *From: mdkb*

- **Remove style-blocking terms from negative prompt for anime**
  - Context: When doing anime/cartoon styles, remove 'artwork, style, painting' from default Chinese negative prompt
  - *From: Kijai*

- **Use both High and Low Noise models for richer results**
  - Context: Dual model setup pushes further than single model workflows despite VRAM constraints
  - *From: mdkb*

- **Leave out MPS and HPS initially for testing**
  - Context: When troubleshooting VACE 2.2, remove MPS and HPS loras first to isolate issues
  - *From: Kijai*

- **Match precision between VACE modules and main models**
  - Context: Use same precision (fp8/bf16) for both VACE and Wan models to avoid compatibility issues
  - *From: mdkb*

- **Use defaults for context options, raise overlap if blending isn't good enough**
  - Context: When configuring context windows for video generation
  - *From: Kijai*

- **Gotta prompt them all when using multiple reference images**
  - Context: HuMo ignores even single reference if you prompt for something else
  - *From: Kijai*

- **Use reference image as start frame as part of the prompt**
  - Context: To get better reference image adherence in generation
  - *From: xwsswww*

- **Audio scale 1.2-1.4 for perfect lipsync with fast rap**
  - Context: When using InfiniteTalk with rap music
  - *From: Charlie*

- **25fps is necessary with InfiniteTalk**
  - Context: Lower framerates like 24fps can cause drift in InfiniteTalk workflow
  - *From: mdkb*

- **Switch audio to add not para for series audio processing**
  - Context: When using multiple audio inputs in InfiniteTalk
  - *From: mdkb*

- **Remove background from reference images for VACE**
  - Context: Helps with better subject isolation, VACE paper shows references on white backgrounds
  - *From: Flipping Sigmas*

- **Don't use long prompts with InfiniteTalk**
  - Context: AI gets confused and forgets about singing, focus on simple actions like 'aggressively rapping with hand gestures'
  - *From: Charlie*

- **Use unsampling steps before switching to Phantom**
  - Context: Best results when mixing 2.2 and Phantom models
  - *From: Ablejones*

- **Set fans to 50% at idle for better GPU longevity**
  - Context: Prevents GPU from getting hot when load is applied
  - *From: Charlie*

- **Use specific prompting for camera movements**
  - Context: Include 'shaky handheld camera' or 'camera dollies' in prompts for desired camera effects
  - *From: Charlie*

- **Clear triton cache after PyTorch updates**
  - Context: When updating PyTorch versions, especially with torch compile issues
  - *From: Kijai*

- **Use --disable-smart-memory for native VRAM management**
  - Context: When getting OOM errors with native ComfyUI nodes
  - *From: Kijai*

- **Lower denoise and modify prompt to avoid tiling artifacts**
  - Context: When upscaling with Wan - use quality/style prompts rather than detailed subject descriptions
  - *From: softboi*

- **Use fp8_scaled over fp8_e4m3fn**
  - Context: For Wan models, fp8_scaled performs better than regular fp8_e4m3fn variants
  - *From: Kijai*

- **Increase CFG and steps for better likeness in FunVace**
  - Context: When not getting good likeness results with FunVace 2.2
  - *From: xwsswww*

- **Use pipe delimiter for multiple prompts in wrapper**
  - Context: When using wrapper text encoder node, separate multiple prompts with | for different generation windows
  - *From: Kijai*

- **Radial attention speeds up Infinite Talk**
  - Context: Radial attention saves about 1 minute off every 7 minutes in InfiniteTalk workflows
  - *From: mdkb*

- **Use fisheye lens for music video genre**
  - Context: When creating rap/music videos
  - *From: Charlie*

- **Use hybrid approach for lora/cfg scheduling**
  - Context: First step or two using cfg and no lora, then rest of the steps with lora at high strength and no cfg on the high noise side
  - *From: Kijai*

- **Update audio scale to 2.5 for better mouth movements in Humo**
  - Context: When using Humo for lip sync
  - *From: VRGameDevGirl84(RTX 5090)*

- **Use Suno and download stems for audio generation**
  - Context: Use just lyrics in the first url and the full song on the other one
  - *From: VRGameDevGirl84(RTX 5090)*

- **Don't use enhancer loras on 2.2 or be careful**
  - Context: They work on the low noise but careful cause they can add flux face and butt chin
  - *From: VRGameDevGirl84(RTX 5090)*

- **Start with CFG around 3.0**
  - Context: If it doesn't burn it or create wacky motion you can go higher
  - *From: Kijai*

- **Use concept loras on low noise for 2.2**
  - Context: When using concept loras with 2.2
  - *From: VRGameDevGirl84(RTX 5090)*

- **Use filename in negative prompt for ordered generation**
  - Context: When using CFG 1 and negative prompt does nothing, use filename to ensure segments generate in order
  - *From: VRGameDevGirl84(RTX 5090)*

- **Set torch.compile dynamic to None instead of False**
  - Context: Makes it dynamic only when needed, more efficient than dynamic=True
  - *From: Kijai*

- **For HuMO, use audio scale 2.5 for better mouth movement**
  - Context: Helps get mouth moving more during lip sync
  - *From: VRGameDevGirl84(RTX 5090)*

- **Use quadratic scheduler with seeds3**
  - Context: Usually 1+2 or 1+3 steps for better results
  - *From: buttercup5108*

- **Test with higher frame counts for better torch.compile results**
  - Context: 10 frames too low, 25 frames better for testing
  - *From: buttercup5108*

- **Use LightX in later steps for better motion control**
  - Context: When using 3 samplers with lighti2x
  - *From: Piblarg*

- **Stack multiple reference images for better character consistency**
  - Context: Use closeup face shots as additional refs, can feed batches to reference input
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Keep frame window size at values model handles well**
  - Context: Use 81 frames for InfiniteTalk instead of total frame count
  - *From: Kijai*

- **Don't go above 95% VRAM utilization**
  - Context: To avoid major slowdowns during generation
  - *From: Kijai*

- **Never use decoded frames directly from inpainting**
  - Context: Always composite the result on the original image, use feathered mask for proper blending
  - *From: Kijai*

- **Use phantom ref with VACE for better results**
  - Context: When doing character work with single subjects
  - *From: Kijai*

- **Better align prompts with control video**
  - Context: Don't prompt for dancing if control video isn't dancing, don't prompt for multiple characters if control only has one
  - *From: AshmoTV*

- **Save to PNG batch instead of video combine**
  - Context: Video combine shifts saturation according to some tests
  - *From: SonidosEnArmonía*

- **Blur masks for complex shots with fast motion**
  - Context: VACE 2.2 works better with blurred masks, need to find correct size and blur for each shot
  - *From: chrisd0073*

- **Use VACE strength 1.0 for VACE 2.2**
  - Context: Higher strength was needed for older merged phantom models but not for 2.2
  - *From: Gleb Tretyak*

- **Avoid reward LoRAs for consistency**
  - Context: When wanting character consistency and fewer issues, skip MPS and HPS LoRAs
  - *From: xwsswww*

- **Consider seed quality for character likeness**
  - Context: Bad seeds can affect likeness results in VACE
  - *From: xwsswww*

- **Use 2.1 lightx2v LoRA instead of 2.2 version**
  - Context: For Wan 2.2 workflows
  - *From: nacho.money*

- **Use rank 256 LoRA for better quality**
  - Context: Significant improvement in character movement and realism
  - *From: 𝕯𝖗. 𝕸𝖆𝖈𝖆𝖇𝖗𝖊 ☠*

- **Undervolting for gaming is not the same as for generative AI**
  - Context: Had crashes with stable diffusion when applying similar undervoltage method
  - *From: 𝕯𝖗. 𝕸𝖆𝖈𝖆𝖇𝖗𝖊 ☠*

- **Can use T2V lightx LoRA on I2V version**
  - Context: Still works and sometimes makes better results than using the I2V lightx 480p version
  - *From: Lodis*

- **Don't expect great results with low steps + lora etc, probably need to tune it a lot**
  - Context: When using LoRAs with Wan Animate
  - *From: Kijai*

- **Try not using context windows, it's better in everything but really long gens probably**
  - Context: For most use cases
  - *From: Kijai*

- **Better not use pose images - pose images will get the video getting really bad**
  - Context: When generating with Wan Animate
  - *From: slmonker(5090D 32GB)*

- **The model is pretty sensitive to prompts**
  - Context: When using Wan Animate
  - *From: Kijai*

- **Works only with 832x480, issues with 480X832**
  - Context: Resolution compatibility for segmentation
  - *From: Dr. Macabre*

- **Use videos with less distracting camera motions for better dwpose detection**
  - Context: When pose detection fails
  - *From: rishappi*

- **Use pose and ref inputs only for good results**
  - Context: When not using face detection, pose + reference works well
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Match reference image aspect ratio to output**
  - Context: For multiple reference images, use side-by-side for 16:9 output, top-bottom for 9:16
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Use edge extend or proper padding instead of white/black backgrounds**
  - Context: White or black backgrounds can leak into the generation
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Reduce LoRA strengths for better prompt following**
  - Context: Prompt following can be heavily affected by LoRAs, use just enough strength for the effect to work
  - *From: Lodis*

- **Disable SAM model in workflow to save memory**
  - Context: SAM model was left enabled in example workflow but not needed
  - *From: Kijai*

- **Use relight LoRA for much better character blending**
  - Context: Makes character integration much better
  - *From: Kijai*

- **When adding steps to LightX workflow, reduce LoRA strength accordingly**
  - Context: If you add steps instead of default 4, need to adjust strength
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Set frame window same as input frames for best results**
  - Context: For basic generation without looping
  - *From: slmonker(5090D 32GB)*

- **Use context options instead of frame_window**
  - Context: Set frame window = num frames and use context for better control
  - *From: Kijai*

- **LightX doesn't do well at full strength above 7 steps**
  - Context: Keep steps at 4-6 for best quality
  - *From: DawnII*

- **CFG scheduling helps with likeness**
  - Context: For better character resemblance
  - *From: DawnII*

- **Use Euler scheduler for better results**
  - Context: When using WanAnimate workflow
  - *From: T2*

- **Don't use background frames, use Seedream to stylize first frame instead**
  - Context: When having mask issues
  - *From: A.I.Warper*

- **Use image blend set to screen for combining depth and pose**
  - Context: When mixing pose and depth inputs
  - *From: A.I.Warper*

- **Give something to the face input, using black frames**
  - Context: When doing masking examples
  - *From: Kijai*

- **Use context windows instead of full frame generation**
  - Context: Alternative to generating full count and clipping
  - *From: Kijai*

- **CFG scheduling gives better results**
  - Context: Even though default is CFG 1.0
  - *From: DawnII*

- **Don't fall for the sunk cost fallacy**
  - Context: When considering whether to install tools
  - *From: Juampab12*

- **Use quadratic dpm_2 scheduler**
  - Context: When experiencing CFG burn issues
  - *From: buttercup5108*

- **Always nuke the KJ video nodes folder on big updates**
  - Context: It never auto updates well, only reliable solution
  - *From: Quality_Control*

- **Use 40 minimum steps without distillation, CFG around 3.5**
  - Context: When not using lightning/relight lora
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Turn on force offload if you run out of VRAM after first window**
  - Context: To give room for the VAE, or if decoding is super slow
  - *From: Kijai*

- **Remove mask and bg images to only animate character and keep background**
  - Context: In WanAnimate workflow
  - *From: xiver2114*

- **With NAG you have to dial in the alpha and tau values until it's affecting stuff but not killing quality**
  - Context: Using NAG sampler
  - *From: hudson223*

- **Use closeup reference images for better results**
  - Context: When trying to increase reference image powers in VACE
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Generate reference image using first frame as ControlNet**
  - Context: Having ref image close to start frame gives best looking results
  - *From: hudson223*

- **Position reference image correctly for the shot**
  - Context: Prevents getting prompt results instead of reference image likeness
  - *From: mdkb*

- **Use obvious negative prompts with NAG and increase value until artifacts disappear**
  - Context: For configuring NAG sampler effectively
  - *From: hudson223*

- **Use OG 2.1 'v2' LoRA rank64/128 for LightX2V**
  - Context: When working with VACE to avoid compatibility issues
  - *From: JohnDopamine*

- **Start with smaller block swap numbers first**
  - Context: When setting up blockswap for memory management
  - *From: Lodis*

- **LightX is designed for low steps, no need for 8+ steps**
  - Context: When using LightX LoRA
  - *From: patientx*

- **Talk to Qwen like an LLM with detailed instructions**
  - Context: For better masking: 'select the whole archer including head hair and both hands and arms also the arm seen on the right that has tattoo'
  - *From: Drommer-Kille*

- **Ensure character has sufficient pixels**
  - Context: Use full body shots rather than portraits for better results
  - *From: slmonker(5090D 32GB)*

- **Pose driving works better than character replacement for face consistency**
  - Context: Character replacement more prone to CFG burning
  - *From: slmonker(5090D 32GB)*

- **Lower pose_strength when character uses ref video character size**
  - Context: When output character matches reference video size instead of desired size
  - *From: slmonker(5090D 32GB)*

- **Use crop instead of pad in resize node to keep whole ref image including background**
  - Context: When wanting to preserve entire reference image
  - *From: slmonker(5090D 32GB)*

- **Don't mask both characters at the same time**
  - Context: When working with multiple characters in one scene
  - *From: Klinter*

- **Use VHS load video frame offset to start from specific frame**
  - Context: When target character doesn't appear in first frame
  - *From: Klinter*

- **Remove background input to use ref image as background for style transfer**
  - Context: When wanting motion transfer instead of person replacement
  - *From: ArtOfficial*

- **Calculate window size properly for long videos**
  - Context: Don't want last window generating 81 frames if only few frames left over
  - *From: CaptHook*

- **Use reference image background instead of control video background**
  - Context: Remove background input from animate embeds
  - *From: ArtOfficial*

- **Input something to face input even when not using face**
  - Context: Like EmptyImage node to avoid issues
  - *From: Kijai*

- **Train T2V LoRAs for person likeness, not I2V**
  - Context: T2V LoRAs work fine with WAN 2.2 models for character consistency
  - *From: JohnDopamine*

- **Use cfg for first step even with LightX2V LoRA**
  - Context: Helps with style control, won't mess up LoRA if not too high cfg
  - *From: Kijai*

- **Use negative prompts targeting specific things you don't want**
  - Context: Works better than listing random negative words with NAG node
  - *From: Kijai*

- **Remove 'artwork' and 'painting' from negative prompt for illustrated content**
  - Context: When working with cartoon/anime styles
  - *From: Kijai*

- **Set virtual memory to 60GB if you have storage**
  - Context: Helps with memory management for larger models
  - *From: hicho*

- **Use frame window size of 57 or 61 for 113 frames**
  - Context: Close to two windows for optimal processing
  - *From: Kijai*

- **Keep source fps when doing controlled generation**
  - Context: For VACE/Wan Animate where motion is directed by inputs
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Set blockswap to 40 for 389 frames at 720x1280 on 64GB RAM system**
  - Context: For managing memory usage with long sequences
  - *From: Kijai*

- **Don't use reference image with masking in WanAnimatePreprocess**
  - Context: Reference is meant for retargeting pose to different body shapes
  - *From: Kijai*

- **Set padding to 0 to avoid alignment issues**
  - Context: When not using reference mode in WanAnimatePreprocess
  - *From: Kijai*

- **Use tiled_vae option in WanVideo Animate Embeds for higher frame limits**
  - Context: Can push beyond normal memory limitations
  - *From: harriet_h*

- **Use CFG 3,3,3 on first steps with PUSA**
  - Context: When using PUSA, start with CFG 3 then skim down if it burns
  - *From: DawnII*

- **Don't use distill with PUSA on 2.2**
  - Context: When using PUSA on Wan 2.2, skip distill and run CFG on at least first 3 steps
  - *From: DawnII*

- **Adjust PUSA LoRA strength per generation**
  - Context: Increase strength for more likeness, can also mitigate motion issues but may lose prompt following
  - *From: DawnII*

- **Use standard resolutions for better results**
  - Context: Stick to 832x490, 1024x576, or 1280x720 instead of non-standard resolutions
  - *From: Dkamacho*

- **Set reward LoRAs to maximum 0.5 strength**
  - Context: Default for MPS/HPS reward loras is 0.5, don't exceed this value
  - *From: Kijai*

- **Use stride=1 and disable for Wan models**
  - Context: Stride doesn't work well with Wan due to latent structure, set to 1 or 4=disabled
  - *From: Kijai*

- **Mask everything you want to replace in Wan Animate**
  - Context: Include hair, face, and body in the mask for proper replacement
  - *From: xiver2114*

- **Use high-definition video clips to avoid preprocessing troubles**
  - Context: A good high-definition video clip can save you a lot of trouble in pre-processing
  - *From: piscesbody*

- **Lower face strength for better results**
  - Context: When doing character replacement, try lowering the face strength
  - *From: Léon*

- **Don't use retarget_image by default**
  - Context: People kept using it by default when it should not be used if you don't want to retarget
  - *From: Kijai*

- **Two images is ideal for multi-image input**
  - Context: Quality starts to degrade with 3 images, maybe two images is ideal combo
  - *From: Lodis*

- **Use photographic LoRAs to push away anime/cartoon style**
  - Context: When wanting realistic outputs with Flux or SD, use 4 photographic loras at once
  - *From: mallardgazellegoosewildcat*

- **720p upscaling might be better than native 1080p**
  - Context: More cost effective than generating directly at 1080p
  - *From: mallardgazellegoosewildcat*

- **Prompt adherence improved**
  - Context: Better understanding of prompts like 'shot on a phone, amateur style'
  - *From: Mak*

- **Higher shift improves video layout and motion at cost of details**
  - Context: Shift borrows from detail steps to give to layout/motion steps
  - *From: mallardgazellegoosewildcat*

- **More steps reduce need for high shift values**
  - Context: High step counts eliminate the trade-off between layout and details
  - *From: mallardgazellegoosewildcat*

- **Use T-pose character for best Wan Animate results**
  - Context: Model is designed to work with T-pose due to Flux kontext preprocessing
  - *From: Kijai*

- **Bbox detection is sufficient in most cases with SAM2.1**
  - Context: When using SAM2.1 model for pose detection
  - *From: Kijai*

- **Use rank 64 LoRA for complex captions and motion tracking**
  - Context: When training LoRAs with detailed captions or need better motion
  - *From: Ryzen*

- **Slow train LoRAs to avoid overfitting**
  - Context: 7000 steps on 50 images with complex captions
  - *From: Ryzen*

- **Use detailed captions for dataset diversity**
  - Context: To generate different people instead of same face in LoRA
  - *From: Ryzen*

- **Don't forget to set load video path format to 'wan' to avoid errors**
  - Context: When using wan animate
  - *From: Gateway {Dreaming Computers}*

- **Portrait videos are much more visible than landscape in posts**
  - Context: For competitions and social media visibility
  - *From: AJO*

- **Make sure to load all frames (e.g., 154 frames) or the remaining frames will be random**
  - Context: When processing longer videos
  - *From: VK (5080 128gb)*

- **For LoRA training on high/low model architectures**
  - Context: Train it the way you plan to use it in inference - for most people this means train BOTH high and low together, switching point is up to you
  - *From: mallardgazellegoosewildcat*

- **Fast testing approach**
  - Context: Best videos can come from fast testing with just 3 steps
  - *From: hicho*

- **Use Kijai's preprocessor for better results**
  - Context: Kijai's preprocessor gives better results than the old masking nodes in native implementation
  - *From: 𝕯𝖗. 𝕸𝖆𝖈𝖆𝖇𝖗𝖊 ☠*

- **Use 10 frame overlap for video transitions**
  - Context: When creating long sequences with VACE, though n/4+1 value might be more correct
  - *From: JohnDopamine*

- **Character LoRA definitely helps with consistency**
  - Context: When doing long form video generation
  - *From: JohnDopamine*

- **Use LLM on the fly for prompting each segment**
  - Context: Base prompts on final frame of prior segment plus previous prompt for better continuity
  - *From: JohnDopamine*

- **For style mixing LoRAs, include examples of 2D mixed with different styles and call it out in captions**
  - Context: So the model understands the mix
  - *From: ingi // SYSTMS*

- **Use VACE extend with first 10 frames from previous generation**
  - Context: For creating longer sequences
  - *From: Daviejg*

- **Try disabling face pose part while leaving body**
  - Context: When having issues with character turn-arounds
  - *From: VK*

- **Match poses between retarget and reference for best results**
  - Context: Often doesn't work at all if poses don't match
  - *From: Kijai*

- **Use enlarged feathered masks and track extra 'bits' onto mask for different car shapes**
  - Context: When replacing cars with different profiles (roof racks, etc.)
  - *From: Ruairi Robinson*

- **Art direct shots to avoid texture swimming weakness**
  - Context: When dealing with high-frequency detail issues
  - *From: Neex*

- **Quality over quantity for LoRA datasets**
  - Context: Small diverse dataset better than large poor quality one
  - *From: crinklypaper*

- **Use AE roto brush for masking - very fast and reliable**
  - Context: More reliable than automated solutions in ComfyUI for masking
  - *From: Ruairi Robinson*

- **Caption what you want to control vs not control**
  - Context: For style LoRAs, caption everything except the style so it gets applied automatically
  - *From: crinklypaper*

- **Delay TaylorSeer by a few initial steps**
  - Context: When using TaylorSeer-Lite for better results
  - *From: Zuko*

- **Don't merge multiple LoRAs, train from scratch instead**
  - Context: Better practice is to train a third LoRA from scratch that combines functionality with one combined loss
  - *From: mallardgazellegoosewildcat*

- **Use different LoRA weights per step and per block when merging**
  - Context: If you must merge existing LoRAs, use reward model as verifier with gradient descent
  - *From: mallardgazellegoosewildcat*

- **Use Florence for auto-captioning images for Wan animate**
  - Context: Works well for prompting animate despite expectations
  - *From: Drommer-Kille*

- **Delay caching for a few steps on both models when using LightX2V**
  - Context: When seeing quality degradation with speed LoRAs
  - *From: Zuko*

- **Use Uni3C instead of trying to match camera with WanAnimate**
  - Context: For reference animate mode camera matching
  - *From: DawnII*

- **Feather in depth on corners for camera matching**
  - Context: When using VACE for camera work
  - *From: Nathan Shipley*

- **Get a wan account for daily free video**
  - Context: Use gmail account, check in daily for 1 free video render
  - *From: Gateway {Dreaming Computers}*

- **Use masking to control multiple people speaking with InfiniteTalk**
  - Context: Edit audio clips with silence at beginning/end for each speaker
  - *From: mdkb*

- **Disconnect masks and bg frames to use reference image background instead of driving video**
  - Context: When using WanAnimate wrapper
  - *From: DawnII*

- **Use incomplete mask to add foreground elements in VACE**
  - Context: Complete mask prevents adding foreground elements
  - *From: Izaan*

- **Never do prompt engineering as human**
  - Context: Use black box optimization, Bayesian inference and evolutionary/genetic methods instead
  - *From: mallardgazellegoosewildcat*

- **Power limit GPUs for efficiency**
  - Context: 5090 gets 90% speed with half power, 70% power gives 95-98% speed when memory bound
  - *From: The Punisher*

- **Use 5 steps instead of 4 for new Lightning LoRA**
  - Context: 4 steps not enough, 6 seems overcooked
  - *From: Draken*

- **Use total 4 steps split in middle for Lightning LoRA**
  - Context: 2 steps high + 2 steps low, not 4+4
  - *From: Kijai*

- **Remove character background for Wan VACE 2.2 like VACE 2.1**
  - Context: For reference images in VACE workflow
  - *From: Kijai*

- **Use String to Float node for custom timesteps**
  - Context: Instead of interpolate steps, input: 0.999, 0.937, 0.833, 0.625
  - *From: Kijai*

- **Lightning LoRA strength 1:1 should work according to Reddit**
  - Context: For proper LoRA application
  - *From: Lodis*

- **Use dyno full model instead of lora for high noise**
  - Context: Better performance than extracted lora version
  - *From: Kijai*

- **Crop tighter to character for better face likeness in WanAnimate**
  - Context: Face needs to be bigger in frame and prompted for
  - *From: Kijai*

- **Use MAGREF with InfiniteTalk for more freedom**
  - Context: When InfiniteTalk changes likeness too much
  - *From: Kijai*

- **Stylize first frame with qwen-edit then use InfiniteTalk**
  - Context: Alternative workflow for better results
  - *From: Kijai*

- **Use uncomfortably close face reference for lip sync**
  - Context: For WanAnimate lip sync - 'you want to smell their digital breath'
  - *From: U̷r̷a̷b̷e̷w̷e̷*

- **Put 'geisha' in negative prompt to prevent Asian transformation**
  - Context: When characters are incorrectly turning Asian in WanAnimate
  - *From: mdkb*

- **Use frame window size 77 for short videos, 81 for long videos**
  - Context: WanAnimate frame window configuration
  - *From: Charlie*

- **Set num_frames and frame_window_size equal when using context options**
  - Context: WanAnimate with context windows - disables looping and uses context options normally
  - *From: Kijai*

- **Know when to say 'good enough'**
  - Context: Avoid spending a week seeking perfection - sometimes need to accept results and move on
  - *From: mdkb*

- **Connect get frame count to frame window size for non-looping workflows**
  - Context: When not using WanAnim looping
  - *From: Kijai*

- **Match input image pose to video pose for better I2V results**
  - Context: Including camera distance and body parts filmed - the less AI has to interpret, the better
  - *From: Gill Bastar*

- **Use prompting for motion with Uni3C in 2.2**
  - Context: With 2.2, prompting helps as Uni3C effect is weaker than with 2.1
  - *From: Kijai*

- **Use 'arc shot' in prompts for camera movement**
  - Context: When wanting camera motion effects
  - *From: Abx*

- **Apply Uni3C only to high noise model, not low noise**
  - Context: For dual model setups with Wan 2.2
  - *From: xwsswww*

- **Focus on Time + Energy vs Quality approach**
  - Context: To avoid getting lost in endless tweaking and rabbit holes
  - *From: mdkb*

- **Consider servers over local if possible**
  - Context: For better performance, though working with low VRAM can be fun challenge
  - *From: mdkb*

- **For camera rotation prompts, mention specific parts like tail to force full rotation**
  - Context: there is a tendancy for pixels to want to stay the same, and typically a full rotation wants the last frame to look like the first frame. So a rotation can be cut short, because the only way it can end on the face is by turning around and reversing / not doing the rotation at all. Mentioning the tail really forces it to do the full rotation
  - *From: Instability01*

- **Use fantasy portrait model with reduced mouth and emo scale for better lip sync**
  - Context: using the fantasy portrait model with infinite talk, and reducing the mouth scale and emo scale from face detector to 0.01 results in less exaggerated lip sync
  - *From: Dorksense*

- **Use wavespeed.ai to avoid content filters**
  - Context: Wavespeed's got the weights and they don't put any filters
  - *From: ZeusZeus (RTX 4090)*

- **For VACE inpainting masks, use true gray for vace2.1**
  - Context: true gray for vace2.1, no idea for fun vace
  - *From: Gleb Tretyak*

- **For Wan 2.2 LoRA use 1 for high noise and 0.5 for low**
  - Context: Testing custom LoRA
  - *From: Ryzen*

- **12GB VRAM is blockswap territory for Wan**
  - Context: Running Wan on consumer hardware
  - *From: mallardgazellegoosewildcat*

- **Can add actual noise mask to the latent for inpainting**
  - Context: Troubleshooting inpainting issues
  - *From: Ablejones*


## News & Updates

- **PUSA 2.2 officially released**
  - Available at huggingface.co/RaphaelLiu/Pusa-Wan2.2-V1
  - *From: Zabo*

- **Alibaba Wan mentioned community video work**
  - Official Wan account shared community-created video on Twitter
  - *From: ByArlooo*

- **Wan 2.2 S2V 14B model released**
  - New speech-to-video model available on HuggingFace
  - *From: Monero*

- **Resized Pusa LoRAs released**
  - High and Low noise versions resized to rank 98, available on Kijai's HuggingFace
  - *From: Kijai*

- **Wrapper updated to support latest features**
  - Needs update as of specific time to use new functionality
  - *From: Kijai*

- **VibeVoice Large 7B model uploaded**
  - Might be good for multi-speaker scenes with InfiniteTalk
  - *From: orabazes*

- **Kijai updated WanVideoWrapper for Pusa 2.2**
  - Update allows I2V node to grab from start image when flowmatch_pusa scheduler is used
  - *From: Kijai*

- **Wan 2.3 announcement on Reddit**
  - New version announced but based on several months old articles, timeline unclear
  - *From: scf*

- **S2V nodes renamed and moved to main branch**
  - WanVideo S2V Sampler node renamed to include pose support and framepack mode. S2V branch no longer needed
  - *From: Kijai*

- **LoRA resize node added to KJNodes**
  - Can reduce LoRA size by half with only 5% effect loss, Pusa 2.2 works fine even at quarter size
  - *From: Kijai*

- **Kijai made a bad commit that broke unmerged LoRAs completely**
  - Fixed within 2 hours, users need to update again if they updated during that window
  - *From: Kijai*

- **Model loading system completely redesigned**
  - Now uses lazy loading with safetensors to save 20-30GB RAM
  - *From: Kijai*

- **Multiple image I2V support added**
  - Can now use batch of images for context windows with I2V
  - *From: Kijai*

- **AudioStory weights dropped**
  - New model from TencentARC for audio-driven content, might work well with InfiniteTalk
  - *From: JohnDopamine*

- **New multi-image context window support**
  - Latest WanVideoWrapper allows setting individual start frames for each context and an end image
  - *From: Dever*

- **Pusa LoRA available for Wan 2.2**
  - Wan22_PusaV1 works only in wrapper at the moment, needs custom sampling method
  - *From: Mngbg*

- **ComfyUI implements ByteDance USO**
  - ComfyUI finally implemented the bytedance USO functionality
  - *From: Lodis*

- **Microsoft released VibeVoice and it's in ComfyUI**
  - Voice cloning tool available in ComfyUI with good quality results from 8 second samples
  - *From: ✧ฅโ๑ↀᆺↀ ๑ใฅ✧PookieNumnums*

- **VibeVoice project discontinued**
  - Microsoft discontinued VibeVoice TTS project, though inference code in ComfyUI still works
  - *From: xiver2114*

- **Block swap implementation for native ComfyUI**
  - Someone created ComfyUI-wanBlockswap for native implementation
  - *From: xwsswww*

- **New models appearing on Wan website**
  - Website updated with new models for both I2V and T2V, suggesting new models coming soon
  - *From: hicho*

- **Chatterbox Multilingual released**
  - Supports 23 languages including Arabic, Danish, German, Greek, English, Spanish, Finnish, French, Hebrew, Hindi, Italian, Japanese, Korean, Malay, Dutch, Norwegian, Polish, Portuguese, Russian, Swedish, Swahili, Turkish, Chinese. MIT Licensed.
  - *From: patientx*

- **VibeVoice repository taken down**
  - GitHub repository is now 404, likely deleted for making voice cloning too accessible
  - *From: multiple users*

- **Fun Control 2.2 A14B already does a lot of what VACE does**
  - New capabilities in Fun Control reducing need for separate VACE 2.2
  - *From: Kijai*

- **Nano Banana available for free in Gemini and Adobe Firefly**
  - Adobe admits others do better AI, also allowing VEO in Adobe apps
  - *From: Drommer-Kille*

- **Kijai working on native InfiniteTalk**
  - Already working but needs optimization for long generation
  - *From: Kijai*

- **VACE module moved to extramodel**
  - Same input can be used for other tools like MTV_crafter, old workflows still work
  - *From: Kijai*

- **Pusa noise system works on 2.1**
  - Confirmed compatibility with Wan 2.1 models
  - *From: Kijai*

- **InfiniteTalk update makes MultiTalk redundant**
  - Latest InfiniteTalk improvements supersede MultiTalk functionality
  - *From: Kijai*

- **Alibaba working on their own framepack version called 'streamer'**
  - Will allow longer videos, mentioned in Reddit article
  - *From: Lodis*

- **Chatterbox TTS updated with multilingual support**
  - Now covers 23 languages out of the box
  - *From: U̷r̷a̷b̷e̷w̷e̷*

- **Kijai pushed InfiniteTalk update for padding with silence**
  - Characters won't keep speaking after audio ends, includes empty embed loading
  - *From: Kijai*

- **New node added to generate videos where character keeps mouth shut**
  - Uses empty embed for silent video generation
  - *From: Kijai*

- **Kijai updated InfiniteTalk frame iteration logic**
  - If frame number ≤ frame_window_size, does 1 iteration instead of forcing 2
  - *From: Kijai*

- **InfiniteTalk auto-downloads required .pt files**
  - No manual download needed, files are automatically downloaded
  - *From: Kijai*

- **New kinestasis concept LoRA released for Wan 2.2**
  - Available on HuggingFace by Cseti
  - *From: hicho*

- **Low-VRAM workflow pack released**
  - Complete pack for generating long videos with VACE, works for 30-60 seconds
  - *From: Akumetsu971*

- **Wan 2.2 Fun Reward LoRAs released**
  - New reward LoRAs available on HuggingFace for detail enhancement
  - *From: yi*

- **Reward LoRAs should not mix 2.1 components with 2.2 generations**
  - Official note warns against using 2.1 components in 2.2 generations to avoid negative effects
  - *From: Lodis*

- **New Lightning version in development**
  - New lightning version has few weeks ETA according to HuggingFace discussion
  - *From: crinklypaper*

- **Wan 2.2 Fun Reward LoRAs released**
  - MPS and HPS reward LoRAs now available for Wan 2.2 on HuggingFace
  - *From: Mu5hr00m_oO*

- **Resized reward LoRAs available**
  - Kijai created resized versions of reward LoRAs that are 10x smaller with rank reduction
  - *From: Kijai*

- **UniVerse-1 audio model released**
  - 1.3B audio model from Dorniwang, 28GB model size, uses Wan 1.3B for video part
  - *From: Kijai*

- **MoeSampler native node available**
  - Native ComfyUI sampler that uses same boundary values as wrapper (0.875 for t2v, 0.900 for i2v)
  - *From: : Not Really Human :.*

- **Performance issues after ComfyUI updates**
  - Users reporting OOM issues and speed decreases after recent ComfyUI updates
  - *From: xwsswww*

- **HuMo model announced by Phantom team**
  - Human-Centric Video Generation via Collaborative Multi-Modal Conditioning, weights to be released before January 15th
  - *From: ZeusZeus (RTX 4090)*

- **Native Infinite Talk implementation in progress for ComfyUI core**
  - Kijai working on adding to main ComfyUI, currently in branch on his fork
  - *From: Kijai*

- **Uni3C updates pushed for wrapper**
  - Now works with T2V and VACE, automatically interpolates input to generation frame count
  - *From: Kijai*

- **HuMo models released by ByteDance**
  - 17B parameter model based on Wan 14B with audio layers, trained on 97-frame videos at 25 FPS
  - *From: yi*

- **SEGS detailer working with VACE+Phantom**
  - Working on separate fork of Impact-Pack, nearly ready to submit PR but needs more testing
  - *From: Ablejones*

- **Wan 2.2 tile controlnet available**
  - TheDenk released wan2.2-ti2v-5b-controlnet-tile-v1 for potential upscaling use
  - *From: Hevi*

- **HuMo weights released**
  - 70GB safetensors, fp32, video + audio natively, Apache license
  - *From: ZeusZeus (RTX 4090)*

- **Kijai working on HuMo branch**
  - Code was released, weights just came out, input masks still need to be added
  - *From: Kijai*

- **sync.so launching on ComfyUI through API this week**
  - They build their own models
  - *From: 320091681187954689*

- **Hunyuan-image distilled got released with GGUF versions**
  - Targets 8 step generation, fully NSFW capable
  - *From: patientx*

- **SeedVR2 ComfyUI implementation now has blockswap node and better memory management**
  - VAE tiling and way better memory management, nowhere as memory heavy as it used to be
  - *From: Adrien Toupet*

- **Wan 2.2 Fun VACE modules released**
  - Alibaba PAI team released VACE modules for Wan 2.2, includes high and low noise variants
  - *From: JohnDopamine*

- **Kijai released multiple format versions of Fun VACE**
  - Released bf16, fp8 (e4m3fn and e5m2), and GGUF (Q4_K_M and Q8_0) versions
  - *From: Kijai*

- **HuMo original code doesn't work**
  - Original HuMo repository code has basic errors preventing execution, audio functionality doesn't work
  - *From: Kijai*

- **VACE 2.2 released by Fun team**
  - New VACE version with high noise support and improved quality
  - *From: multiple users*

- **Reward LoRAs now available**
  - Open sourced reward LoRAs for quality improvement
  - *From: Dream Making*

- **HuMo provisional ComfyUI support added**
  - Audio-reactive character model now testable in ComfyUI
  - *From: Alisson Pereira*

- **HuMo model now working with proper audio sync**
  - Fixed parallel attention issues, available on WanVideoWrapper branch
  - *From: Kijai*

- **FP8 scaled HuMo uploaded**
  - Available at huggingface.co/Kijai/WanVideo_comfy_fp8_scaled/tree/main/HuMo
  - *From: Kijai*

- **Whisper encoder optimized**
  - Removed unused decoder layers from whisper model
  - *From: Kijai*

- **SageAttention patch being deprecated**
  - ComfyUI now has native attention selection, patch will be removed or adapted
  - *From: Kijai*

- **HuMo audio support implemented**
  - Kijai got HuMo working with audio functionality
  - *From: JohnDopamine*

- **Workflow breaking update pushed**
  - Update changes model loading to use extra_model instead of separate inputs
  - *From: Kijai*

- **Tiled VAE encoding added for HuMo**
  - Added tiled VAE encoding option for HuMo embeds
  - *From: Kijai*

- **Context windows + cfg issue fixed**
  - Fixed compatibility between context windows and cfg scheduling
  - *From: Kijai*

- **Fun team released VACE version for Wan 2.2**
  - Works pretty good, drop-in replacement for existing workflows
  - *From: Kijai*

- **HuMo model released**
  - New model from Phantom team - basically Phantom with optional audio input built in
  - *From: Kijai*

- **New Wan2.2 mega AIO model released**
  - Includes VACE, T2V/I2V, First-Last, all in 1 model with 1 sampler at cfg/4 steps
  - *From: Phr00t*

- **GGUF versions of VACE 2.2 now available**
  - Q4 and Q5 variants released on HuggingFace
  - *From: The Shadow (NYC)*

- **Waver 1.0 announced as new SOTA video model**
  - 12B parameters, outperforms Veo3, but will not be open source
  - *From: yi*

- **New grain LoRA in development for Wan 2.1**
  - Early version showing progress, needs more training
  - *From: Drommer-Kille*

- **Job Manager UI tool created for workflow organization**
  - Creates job names, numbered shots, subfolders, custom ComfyUI batch files
  - *From: T2 (RTX6000Pro)*

- **HuMo 1.7B weights released**
  - New model weights available on HuggingFace
  - *From: DawnII*

- **PyTorch deprecating torchaudio, replacing with torchcodec**
  - ComfyUI moving to use pyav for audio handling
  - *From: Kijai*

- **Rumors of Wan 2.5 and two new SOTA models coming soon**
  - One model comparable to Nano, plus video model and HunYuan image upgrade
  - *From: Juampab12*

- **Long generation model coming next month**
  - A longer generation model for HuMo/Wan will be released next month
  - *From: Kijai*

- **VACE-like model releasing this weekend**
  - A model similar to VACE will be released over the weekend, name cannot be revealed yet
  - *From: 青龍聖者@bdsqlsz*

- **HuMo 1.7B support added**
  - Support for HuMo 1.7B model has been added to WanVideo wrapper
  - *From: Kijai*

- **Torch 2.10 released**
  - torch-2.10.0.dev20250910+cu128 is now available, replacing 2.9
  - *From: Ashtar*

- **New LanPaint workflow supports Wan 2.2**
  - LanPaint from scraed supports Wan 2.2 for inpainting
  - *From: asd*

- **Kijai submitted PR to ComfyUI core for basic audio nodes**
  - PR #9908 for basic audio functionality in core ComfyUI
  - *From: Kijai*

- **PyTorch 2.10 now in nightly**
  - New version available with potential improvements
  - *From: Kijai*

- **B300 GPUs now available at CoreWeave**
  - General release expected soon
  - *From: mallardgazellegoosewildcat*

- **New Wan Animated (formerly VACE) announced**
  - Uses vitpose + LIA, includes faceadapt+bodyadapt+relight, best animation character control replacement effect especially for complex actions. 14B model, may be around 64GB size
  - *From: 青龍聖者@bdsqlsz*

- **China blocks Nvidia Pro 6000D chip sales**
  - Only stopping purchase of specially designed Pro 6000D chips, not all Nvidia chips. Pro 6000D is weaker than 5090 and can't be clustered with NVLink
  - *From: 青龍聖者@bdsqlsz*

- **Wan 2.5 mentioned in development**
  - VACE devs skipping 2.2 suggests possible return to single model/sampler architecture
  - *From: mallardgazellegoosewildcat*

- **VRGameDevGirl84 updated node to take audio input**
  - Will publish updated version that day
  - *From: VRGameDevGirl84*

- **Video Helper Suite updated with video previews on subgraphs**
  - Recent update provides video preview functionality
  - *From: JohnDopamine*

- **Wan 2.5 announcement speculation**
  - Community discussing potential Wan 2.5 release with hopes for 24fps and longer videos
  - *From: hicho*

- **DecartAI released Lucy Edit model**
  - Open source video editing model based on Wan 5B, free non-commercial license
  - *From: hicho*

- **Wan Animate model mentioned**
  - Reference to Wan Animate being provided to Kijai, but details unclear
  - *From: AIGambino*

- **Wan 2.2 Animate model released**
  - 14B parameter model available on Hugging Face, includes relighting LoRA
  - *From: slmonker(5090D 32GB)*

- **Wan 2.5 expected next week**
  - There will be a conference in Hangzhou next week, expected that wan2.5 will be released at the conference
  - *From: slmonker(5090D 32GB)*

- **Live launch event on January 24th**
  - Invited to attend their live launch event, will post pictures on Twitter
  - *From: 青龍聖者@bdsqlsz*

- **ComfyUI native implementation pushed**
  - Comfy pushed initial native WanAnimate implementation and wrapper version
  - *From: Kijai*

- **Wan 2.5 announced for release on the 24th (next week)**
  - One week after Wan Animate release
  - *From: slmonker(5090D 32GB)*

- **Kijai updated example workflow with I2V LoRA and relight LoRA**
  - Also fixed ref resize issue where width/height inputs weren't connected properly
  - *From: Kijai*

- **Wan site updated**
  - Official Wan website received updates
  - *From: hicho*

- **Kijai added frame count checks in latest commit**
  - Should resolve some tensor size mismatch issues
  - *From: Kijai*

- **WanAnimate GGUF conversion available**
  - Q3_K_M and Q2_K versions uploaded for testing
  - *From: The Punisher*

- **Fixed offload bug in latest version**
  - Issue with blocks vs face_blocks naming resolved
  - *From: Kijai*

- **WanAnimate appears to be based on 2.1 but labeled as 2.2**
  - Despite being labeled 2.2, it's actually built on Wan 2.1
  - *From: ˗ˏˋ⚡ˎˊ-*

- **New quantized versions available**
  - Q2, Q3, Q4_0 versions of WanAnimate uploaded to HuggingFace
  - *From: The Punisher*

- **Self-Forcing model released**
  - Real-time streaming video generation on single RTX 4090
  - *From: DawnII*

- **Point tracker custom node released**
  - Great for tracking and creating custom masks
  - *From: traxxas25*

- **Mask management added in native ComfyUI**
  - New functionality available
  - *From: Vérole*

- **WAN team said on Reddit not to use wan 2.2 loras**
  - May not work properly
  - *From: chrisd0073*

- **Lucy Edit recently updated with local nodes**
  - Not a production tool but pretty novel for experimentation
  - *From: ArtOfficial*

- **Lucy Edit repository updated with quality improvements**
  - Update happened 1 hour ago, results are better and less blurry than before
  - *From: Stad*

- **Fixed first frame flash in single window mode**
  - Bug that occurred without bg_images has been resolved
  - *From: Kijai*

- **Possible Wan 2.5 teased**
  - 青龍聖者@bdsqlsz posted cryptic tweet suggesting upcoming release but can't reveal details
  - *From: 青龍聖者@bdsqlsz*

- **WanAnimate face adapter blocks moved to main blocks**
  - Now included in block swap for VRAM reduction
  - *From: Kijai*

- **Native torch RMSNorm support added**
  - Available in nightly builds, provides 9x speed improvement for RMS norm
  - *From: Kijai*

- **First frame saturation issue fixed**
  - Fixed in recent update within past 24 hours
  - *From: Kijai*

- **Fixed small desync/color shift between windows**
  - Code was changed from early access version causing the issue
  - *From: Kijai*

- **Reverted face blocks from fp8 due to quality hit**
  - Face blocks accidentally ended up as fp8 in recent updates
  - *From: Kijai*

- **Pose retargeting feature in development**
  - Will be separate node for native workflows, needs work on temporal stability
  - *From: Kijai*

- **Wan 2.5 release scheduled for January 24th, 10:00 AM China Time**
  - Live stream announcement with new model having many more features than imagined
  - *From: 青龍聖者@bdsqlsz*

- **Kijai now works part-time for comfy-org**
  - Getting paid for model implementations and utility work
  - *From: Kijai*

- **Lucy edit support added to wrapper**
  - Added in latest update, took only 1 minute of work
  - *From: Kijai*

- **New WanAnimatePreprocess repository available**
  - For impatient users who want to test
  - *From: Kijai*

- **Lynx model announcement from ByteDance**
  - Face-driven video generation with VAE encoder and Q-former adapter, code and model coming soon
  - *From: Shubhooooo*

- **Qwen Image Edit 2509 released**
  - New version with multi-image support and ControlNet capabilities
  - *From: Dever*

- **Wan 2.5 expected within 2 days**
  - 10 seconds, 1080p support anticipated
  - *From: multiple users*

- **Hunyuan 3.0 80B model coming this week**
  - Positioned as 'nano banana killer'
  - *From: slmonker(5090D 32GB)*

- **OmniInsert project announced by Phantom team**
  - Subject insertion for videos, no code/model yet
  - *From: JohnDopamine*

- **WanVideoWrapper updated with face image improvements**
  - Latest version creates zeros automatically when face images not used, saves memory for long generations
  - *From: Kijai*

- **New Wan Animate Preprocess nodes available**
  - Manual install from GitHub provides cleaner face transfer and better eye quality
  - *From: A.I.Warper*

- **Qwen Image Edit 2509 FP8 version released**
  - FP8 quantized version now available on HuggingFace
  - *From: Lodis*

- **ComfyUI native development progress**
  - ComfyUI making progress on native implementation with recent commits
  - *From: Lodis*

- **Wan 2.5 preview announced**
  - Wan 2.5 preview will be released, but may be API-only initially before open source release
  - *From: yi*

- **Major update from 2.1 to 2.2**
  - It's mainly because there's too much content in this update. It's not like a small update from 2.1 to 2.2, but rather a major update
  - *From: 青龍聖者@bdsqlsz*

- **Wan 2.5 will be multisensory**
  - Official announcements suggest Wan 2.5 will have multisensory capabilities
  - *From: yi*

- **Open source version still planned**
  - Developers said that because of an important meeting, the preview version was released in advance, and the subsequent official version will still be open source
  - *From: Yan*

- **New preprocessor nodes available**
  - ComfyUI-WanAnimatePreprocess nodes for facial capture and pose capture
  - *From: chancelor*

- **WAN 2.5 preview released on WaveSpeed**
  - Available on wavespeed.ai at $0.25-$1.50 per video depending on resolution, 10 second videos, 480p/720p/1080p options
  - *From: yi*

- **WAN 2.5 livestream announcement**
  - Release stream scheduled, ComfyUI team will be there as partners
  - *From: fearnworks*

- **ComfyUI adding WAN 2.5 API nodes**
  - GitHub PR shows ComfyUI adding API nodes for WAN 2.5, no local model support initially
  - *From: Juan Gea*

- **WAN 3.0 coming in January**
  - WAN 3.0 expected in January according to community discussion
  - *From: NebSH*

- **Wan 2.5 announced with 10s generation and 1080p**
  - Conference presentation scheduled, multiple language sessions
  - *From: Multiple users*

- **Wan 3.0 scheduled for October release**
  - Timeline confirmed by insider
  - *From: 青龍聖者@bdsqlsz*

- **ComfyUI native support for Wan2.2 Animate and Qwen-Edit 2509**
  - Official blog post released
  - *From: Léon*

- **New dedicated Wan+ComfyUI channel created**
  - Channel for ComfyUI-related Wan discussions and updates
  - *From: Kijai*

- **Wan 2.5 briefly leaked on wavespeed.ai then removed**
  - Access removed due to timezone confusion/early release
  - *From: ZeusZeus (RTX 4090)*

- **Wan 2.5 preview announced**
  - 1080p, 10 seconds, 24fps, audio support, T2V and I2V separate models, timed action prompts, multilingual audio support
  - *From: multiple users*

- **Wan 2.5 open source status unclear**
  - Team discussing whether to open source behind doors during livestream delay
  - *From: 🦙rishappi*

- **Wan 2.5 available on wavespeed**
  - Already up for testing on wavespeed platform
  - *From: Ruairi Robinson*

- **Wan 2.5-Preview officially launched**
  - API-only initially, features native multimodal architecture, A/V synchronization, 1080p HD 10s videos, cinematic quality, RLHF implementation
  - *From: 🦙rishappi*

- **Wan 2.5 currently API-only on platforms like wavespeed and fal**
  - Preview model based on feedback, full version may be released later
  - *From: 🦙rishappi*

- **World model on Alibaba's roadmap**
  - Future development towards AGI
  - *From: 青龍聖者@bdsqlsz*

- **Wan 2.5 features announced**
  - 1080p, 24fps, 10 seconds, API first, hopefully open source November, audio support, editing support, timestamps prompting support
  - *From: Lodis*

- **Wan 2.5 available for API testing**
  - Available on create.wan.video for testing via API
  - *From: Tonon*

- **Waver removed open source mentions**
  - They removed mention of being open source after being asked about it on their discord
  - *From: yi*

- **Wan 2.5 released as API/preview version only**
  - Available through APIs and wan.video website, 1080p 10 second videos at 24fps
  - *From: multiple users*

- **Wan team confirms 2.5 will be open sourced**
  - Team member in WeChat said they will release documentation, training details, and inference code when final version releases
  - *From: kerokero/ZeusZeus*

- **No schedule for open model yet**
  - Confirmed there is no schedule for the open model release
  - *From: toyxyz*

- **Qwen released more models this week**
  - New Qwen releases including Qwen 3 VL coming with 3B and 7B variants
  - *From: mallardgazellegoosewildcat/hicho*

- **New Qwen image edit requires ComfyUI update**
  - Latest Qwen image edit model needs ComfyUI update to work
  - *From: buttercup5108*

- **Anisora 3.2 released**
  - New version is 110GB, fp8 version available. Anime finetune of Wan model
  - *From: asd*

- **Wan 2.5 features 1080p, 10 seconds, with sound**
  - Available through API, includes T2I and image editing capabilities
  - *From: multiple users*

- **Native ComfyUI workflow updated**
  - They updated the native workflow today
  - *From: hicho*

- **Suno V5 released**
  - Pro and Premiere plan only, can remix entire songs, has all music styles
  - *From: VRGameDevGirl84*

- **Wan 2.5 preview released but closed source**
  - Hardware specs will only be revealed with official release. Team considering options for open source weights
  - *From: toyxyz*

- **ComfyUI integrated Wan 2.2 animate in native nodes**
  - Native implementation now available
  - *From: 32Bit_Badman*

- **TaylorSeer-Lite support added for Wan 2.1/2.2**
  - Available through ComfyUI-TaylorSeer node
  - *From: Zuko*

- **Lynx model released by ByteDance**
  - Character consistency model based on Wan 2.1 with IP adapter and ref adapter modules
  - *From: CMM0000*

- **Wan 2.5 preview collecting feedback**
  - Full release will have open training + inference code, weights may be released but not decided, requires significantly more VRAM for 1080p 10 second videos
  - *From: Izaan*

- **ComfyUI memory leak fixes**
  - End of memory leaks in ComfyUI according to recent update
  - *From: The Shadow (NYC)*

- **Triton-windows 3.4 build with fp8 support**
  - Supposedly allows 3090 to torch compile fp8_e4m3
  - *From: phazei*

- **Wan 2.2 coming according to Nunchaku developers**
  - Mentioned during development discussion
  - *From: Tony(5090)*

- **Lynx added to Fal for testing**
  - Available for experimentation
  - *From: mallardgazellegoosewildcat*

- **Humo team working on extension-capable version**
  - Built specifically for doing extensions
  - *From: Ablejones*

- **WAN 2.5 architecture hinted as 'Mixture of Transformers'**
  - Dev on stream suggested it might be based on specific arxiv paper
  - *From: yi*

- **Unreal Engine 5.7 preview released with nanite foliage**
  - Could integrate well with Wan Animate
  - *From: xwsswww*

- **Wan 2.2 Lightning LoRA v2.0 (250928) released with enhanced camera control and motion dynamics**
  - lightx2v team actively working on further improvements, more updates coming
  - *From: yi*

- **LightX2V team re-uploaded files with native ComfyUI compatibility**
  - Files now work for both workflows after key naming changes
  - *From: Screeb*

- **Hunyuan Image v3 released**
  - 160GB model size, 80B parameters with 13B active, autoregressive architecture
  - *From: JohnDopamine*

- **Wan 2.5 currently API only, might be open sourced later**
  - Team said they might open source on full release to cover training costs with API revenue first
  - *From: multiple*

- **New Lightning 2509 lora released for high and low noise**
  - Full dyno model also available, performs better than lora version
  - *From: FL13*

- **Raylight multi-GPU inference tool released**
  - Splits inference across multiple GPUs for performance gains
  - *From: Faust-SiN*

- **LongLive-1.3B model released**
  - Wan1.3B tuned like self forcing, claimed to be faster and better than self forcing. Sustains 20.7 FPS on H100, supports up to 240-second videos
  - *From: yi*

- **Wan2.2XX Palingenesis finetune on Reddit**
  - New finetune getting hype with 50+ stars on HuggingFace in 2 days, but minimal difference reported in initial testing
  - *From: JohnDopamine*

- **Wan Alpha released for transparent video generation**
  - New model from WeChatCV that generates videos with alpha channels
  - *From: JohnDopamine*

- **Self-Forcing Plus now supports Wan 2.2**
  - Training code available from LightX2V team, no LoRA yet
  - *From: yi*

- **AI Toolkit trainer on HuggingFace free for one week**
  - Can train ALL supported models including Wan 2.2 14B
  - *From: Drommer-Kille*

- **Wan 2.5 available in MCP playground**
  - Made by Alibaba team that creates ComfyUI-copilot
  - *From: AJO*

- **WanAnimate available via Replicate API**
  - Very cheap pricing: 333 seconds for $1
  - *From: Draken*

- **Sora 2 released with major improvements**
  - iOS only, US only, invite only initially. Has cameo feature for cloning people from video references. ChatGPT Pro users get access to Sora 2 Pro model
  - *From: Juampab12*

- **DC-VideoGen paper and project announced**
  - Wan2.1 14B adapted to DC-AE with significant speed improvements
  - *From: yi*

- **Kandinsky 5.0 T2V Lite released**
  - 2B model that outperforms larger Wan models according to claims
  - *From: yi*

- **ComfyUI added API support for Wan 2.5**
  - New API nodes for Wan 2.5 appearing in ComfyUI
  - *From: Ryzen*

- **Kandinsky 5.0 released with ComfyUI nodes**
  - 2B model available with GitHub repo and workflow, larger model coming
  - *From: Draken/yi*

- **Sora 2 access available but very limited**
  - Sharing in OpenAI Discord but need to be very quick (3-4 seconds)
  - *From: mamad8*


## Workflows & Use Cases

- **Using ChatGPT to create camera movement prompts based on WAN 2.1 prompt guide**
  - Use case: Generating specific camera movements like arc shots
  - *From: Akumetsu971*

- **PUSA + InfiniteTalk combination**
  - Use case: Enhanced lip-sync with improved quality
  - *From: NebSH*

- **3 KSampler approach for better motion**
  - Use case: First sampler with CFG but no LoRA, then add LoRAs in subsequent samplers
  - *From: BecauseReasons*

- **Video-driven lipsync with webcam**
  - Use case: Record yourself lipsyncing to create facial movement reference for better results
  - *From: NC17z*

- **Chaining multiple videos for longer output**
  - Use case: Generate 3 shorter videos and combine into one long video to use less VRAM
  - *From: WorldX*

- **First-frame-last-frame with Pusa**
  - Use case: 161 frames animation using context
  - *From: Dever*

- **Infinite Talk + MagRef workflow**
  - Use case: Lip-sync video generation with character consistency
  - *From: VRGameDevGirl84(RTX 5090)*

- **Last frame continuation workflow**
  - Use case: Creating longer videos by using last frame of previous generation as start frame for next
  - *From: Kenk*

- **Multi-prompt context window workflow for long videos**
  - Use case: Generating 10+ second videos using multiple prompts with context windows
  - *From: Dever*

- **Frame reinjection with context for extension**
  - Use case: Extending videos by feeding last 13 frames as context to next generation
  - *From: 𝕯𝖗. 𝕸𝖆𝖈𝖆𝖇𝖗𝖊 ☠*

- **FLF (First Frame Last Frame) for music videos**
  - Use case: Creating music videos with start and end frame control
  - *From: VRGameDevGirl84(RTX 5090)*

- **Context window with multiple prompts using | separator**
  - Use case: T2V and I2V with different prompts per window
  - *From: Kijai*

- **Panda context workflow adapted for Wan 2.2 I2V**
  - Use case: I2V generation with context windows
  - *From: Ashtar*

- **Multi I2V with batch images**
  - Use case: Using multiple input images with context windows
  - *From: Kijai*

- **Multi-image context I2V**
  - Use case: Generate windows of 81 frames with overlap, each one can have a start image and a prompt
  - *From: Dever*

- **3 KSampler setup for motion enhancement**
  - Use case: Running first 2 steps without lightx/lightning to improve motion with subsequent steps using speed LoRAs
  - *From: BecauseReasons*

- **Context windows for longer video generation**
  - Use case: Generating longer videos using temporal tiling technique, works with overlap frames
  - *From: Kijai*

- **Pusa extension for T2V**
  - Use case: Video extension using Pusa with noise ramping for better motion continuation
  - *From: Kijai*

- **FLF2V for transitions**
  - Use case: First-to-last frame transitions, works well with underwater transitions at 121 frames
  - *From: Drommer-Kille*

- **Extended video generation using context windows**
  - Use case: Creating 30+ second videos by chaining multiple context windows with proper prompt transitions
  - *From: N0NSens*

- **V2V adaptation for long generation**
  - Use case: Adapting workflows for video-to-video generation of 30+ seconds, though quality needs adjustment
  - *From: Akumetsu971*

- **WanVace with start frame for environment replacement**
  - Use case: Environment replacement and performance change using VACE with start frame conditioning
  - *From: Fleembus*

- **Multi-character InfiniteTalk setup**
  - Use case: Two characters having a conversation with proper masking
  - *From: samhodge*

- **Extension method with Pusa 2.2 using subgraphs**
  - Use case: Chaining Pusa 2.2 Extend workflow with subgraphs for longer generations
  - *From: JohnDopamine*

- **Context/stride approach for I2V extensions**
  - Use case: Extending I2V generations beyond 5 seconds with reasonable transitions
  - *From: blake37*

- **Benji's extension method reworked for wrapper**
  - Use case: Extended video generation with some modifications for the wrapper
  - *From: N0NSens*

- **Using Nano Banana to fix garbled text from Wan 2.2**
  - Use case: Post-processing to convert garbled text into readable poems or content
  - *From: Drommer-Kille*

- **Docker-based Whisper for speaker diarization**
  - Use case: Transcribe chats and split into speaker segments with SRT timecodes
  - *From: samhodge*

- **CGI vid2vid for controlled generation**
  - Use case: Using Unreal previs as scaffold for character-consistent photographed footage
  - *From: samhodge*

- **Convert I2V to T2V**
  - Use case: Replace image encoding with empty latent and change models
  - *From: SonidosEnArmonía*

- **Video upscaling with SD**
  - Use case: 4K upscaling in 14 minutes on RTX 5090, includes flickering fix
  - *From: FL13*

- **Context windows with different input images**
  - Use case: Different input image per sequence for longer videos
  - *From: Ashtar*

- **V2V VACE long video workflow**
  - Use case: Creating long videos with V2V VACE, though takes hours to generate
  - *From: Akumetsu971*

- **Tiled upscale with SEGS detailer for video enhancement**
  - Use case: Cleaning up video quality, sampling only masked parts to prevent LoRA bleeding
  - *From: Ablejones*

- **Three sampler I2V setup**
  - Use case: Better dynamics in I2V generation using sequential samplers with different LoRAs
  - *From: .: Not Really Human :.*

- **Combining Wan 2.2 with VACE**
  - Use case: Style control with latest model
  - *From: pom*

- **4 second video generation to avoid slowmo**
  - Use case: Getting proper speed motion in Wan 2.2
  - *From: Kenk*

- **Multi-window lip sync generation**
  - Use case: Long form video with 375 frames (125x3) using Multitalk
  - *From: N0NSens*

- **HDRI dome creation for Unreal**
  - Use case: Outpainting with VACE and Layer Forge node
  - *From: yukass*

- **Automated music video creation**
  - Use case: Custom node for exact scene timing with InfiniteTalk
  - *From: VRGameDevGirl84(RTX 5090)*

- **Dynamic InfiniteTalk scene workflow**
  - Use case: Creating multiple scenes with different durations automatically, like endless travel but for InfiniteTalk
  - *From: VRGameDevGirl84(RTX 5090)*

- **Three sampler workflow for wild results**
  - Use case: Creating complex transformation effects like person turning into tornado
  - *From: T2 (RTX6000Pro)*

- **Low-VRAM VACE workflow**
  - Use case: Generating 30-60 second videos on limited VRAM setups
  - *From: Akumetsu971*

- **VACE with SEGS detailer**
  - Use case: Upscaling and detailing videos using tiling and subject separation
  - *From: Ablejones*

- **Save latents in chunks then decode separately**
  - Use case: Generating very long videos (2000+ frames) without OOM
  - *From: VK (5080 128gb)*

- **Insert reference frames in middle of video generation**
  - Use case: Maintaining character consistency across long sequences
  - *From: VK (5080 128gb)*

- **Separate driving video for motion control**
  - Use case: Adding custom motion from external sources like SketchUp screen grabs
  - *From: Flipping Sigmas*

- **Save intermediate InfiniteTalk results to disk**
  - Use case: Avoiding waiting hours when intermediate results exist and allowing continuation
  - *From: Kijai*

- **Two-pass sampling with sigma scheduling**
  - Use case: Improved quality using high/low pass approach with custom sigma inputs
  - *From: The Shadow (NYC)*

- **VACE with ControlNet enhancements**
  - Use case: Adding DWpose and other ControlNet inputs to enhance VACE features
  - *From: yukass*

- **4-stage Wan 2.2 i2v process**
  - Use case: Improved video generation with reduced corruptions using 1+1 then 1+2 staging
  - *From: patientx*

- **T2V model upscaling with USDU**
  - Use case: Use Wan 2.2 low model with UltimateSD Upscaler for detail enhancement at denoise 0.3
  - *From: Juan Gea*

- **VACE upscaling workflow**
  - Use case: Alternative upscaling using Wan 2.1 VACE, works up to 2K resolution
  - *From: FL13*

- **USDU video upscaling on 3060**
  - Use case: Upscaling 65 frame videos in ~20 minutes, splitting longer videos into segments
  - *From: mdkb*

- **Wan 2.2 with Infinite Talk**
  - Use case: Lip-sync generation using low noise model with specific LoRA combinations
  - *From: Izaan*

- **Infinite Talk + silent audio + unianimate**
  - Use case: Endless pose generation without speech, faster than context windows
  - *From: Kijai*

- **VACE reference + Uni3C**
  - Use case: Camera movement control with character consistency
  - *From: Kijai*

- **Infinite Talk + uni3c camera control + unianimate_poses**
  - Use case: Video to video with camera motion and pose control from driving video
  - *From: T2 (RTX6000Pro)*

- **USDU video upscaler for 1080p**
  - Use case: 24fps 1080p 121 frames upscales in 30 mins using t2v denoise polish/fix trick
  - *From: mdkb*

- **InfiniteTalk + FantasyPortrait with radial attention**
  - Use case: Speed optimized workflow with significant performance gains
  - *From: mdkb*

- **Using VACE for dance replication**
  - Use case: Copy dances from reference video to new character
  - *From: Kevin "Literally Who?" Abanto*

- **Context windows with HuMo**
  - Use case: Attempting continuous generation with reference copying
  - *From: Kijai*

- **VACE Start End Image + ControlVideo + Uni3C**
  - Use case: Complex control setup, though control video negates uni3c effect
  - *From: Dream Making*

- **Video continuation using multiple samplers**
  - Use case: Creating longer videos by chaining 61 frame + 41 frame + 41 frame generations
  - *From: Cseti*

- **Multi-reference image concatenation**
  - Use case: Using multiple reference images by concatenating them into single image
  - *From: Kijai*

- **Video extension with VACE 2.2**
  - Use case: Create 195 frame videos by extending 81 frames with last 16 frames, then looping
  - *From: Daflon*

- **Two reference images with VACE 2.2**
  - Use case: Use multiple image references for better character consistency
  - *From: Kijai*

- **VACE 2.2 with masking for character replacement**
  - Use case: Swap characters in videos while maintaining scene consistency
  - *From: multiple users*

- **SAM2 masking + VACE generation**
  - Use case: Better object masking for video generation with grow mask and blur
  - *From: Zuko*

- **FFLF with VACE 2.2 + WAN 2.2 LN**
  - Use case: First-frame-last-frame morphing, though has mist/distillation issues
  - *From: mdkb*

- **HuMo with audio length auto-detection**
  - Use case: Set num_frames to -1 for automatic audio length matching
  - *From: Kijai*

- **HuMo reference image made optional**
  - Use case: Text-to-video generation without image input
  - *From: Kijai*

- **Multiple controls with VACE**
  - Use case: Complex control over video generation, though hard to use and VRAM intensive
  - *From: Lumifel*

- **V2V with VACE using depthmap/pose**
  - Use case: Video style transfer while maintaining structure
  - *From: mdkb*

- **VACE 2.2 with context windows for long generation**
  - Use case: 177 frames with maintained quality and reference accuracy
  - *From: Kijai*

- **HuMo with InfiniteTalk sampling mashup**
  - Use case: Using silent audio for infinite generation and HuMo for the rest
  - *From: Kijai*

- **InfiniteTalk via vid2vid for existing video lip sync**
  - Use case: Lip syncing existing videos, requires masking for final production quality
  - *From: Kijai*

- **For loop node for extending video segments**
  - Use case: Iterate over control video and extend from segment to segment for longer generations
  - *From: Gleb Tretyak*

- **Start with HuMo and extend with InfiniteTalk**
  - Use case: Combining different models but ends up being more InfiniteTalk-like than HuMo
  - *From: Kijai*

- **Using VACE masking with original footage overlay**
  - Use case: Generate background with Wan at lower resolution, overlay original crispy face and cloth texture on top
  - *From: Izaan*

- **Multi-controlnet with VACE 2.2**
  - Use case: Style transfer using depth, normal, and lineart controls combined
  - *From: yo9o*

- **VACE + Phantom hybrid approach**
  - Use case: Use VACE 2.2 for high noise, switch to Phantom for final steps
  - *From: Ablejones*

- **Background character insertion**
  - Use case: Create ref frame with person using Flux, use VACE to diffuse into video, fine-tune with reference images
  - *From: Dream Making*

- **V2V with face using open pose workaround**
  - Use case: Disable face detection in open pose, use with infinite talk to avoid dots problem
  - *From: 𝕯𝖗. 𝕸𝖆𝖈𝖆𝖇𝖗𝖊 ☠*

- **High noise with wrapper (Uni3C) + low noise with native + third denoise step at 0.5**
  - Use case: Multi-step generation combining wrapper and native capabilities
  - *From: mamad8*

- **Tiled sampling workflow for Wan upscaling**
  - Use case: Upscaling with tile-based approach to reduce artifacts
  - *From: FL13*

- **Endless HuMo video generation**
  - Use case: Creating long-form videos with different scenes and prompts, can create full minute videos in about 16 minutes
  - *From: VRGameDevGirl84(RTX 5090)*

- **Infinite Talk without context options**
  - Use case: Use silent audio or no people for infinite length video generation without context window limitations
  - *From: mdkb*

- **Loop-based prompt switching**
  - Use case: Using index numbers from loops to choose different prompts for different sections of video
  - *From: JalenBrunson*

- **Infinite Talk workflows for lip sync**
  - Use case: Dialogue generation, tweaked for long talking/singing videos
  - *From: mdkb*

- **Video to video with HUMO**
  - Use case: First test of video to video with HUMO worked, could potentially work with controlnets and masks
  - *From: VRGameDevGirl84(RTX 5090)*

- **Segmenting control video into chunks for any length video with Wan2.2 VACE**
  - Use case: Making unlimited length videos by splitting into chunks with overlap
  - *From: Gleb Tretyak*

- **HuMO endless video generation**
  - Use case: Creating lip sync videos longer than 97 frame limit by splitting into groups
  - *From: VRGameDevGirl84(RTX 5090)*

- **VACE with grey mask background**
  - Use case: Control video foreground with grey mask background, don't plug mask to get relight feature
  - *From: chrisd0073*

- **Video to video HuMO without reference image**
  - Use case: Adding lip sync to existing video using empty image as reference
  - *From: VRGameDevGirl84(RTX 5090)*

- **Using FastWan with MagRef InfiniteTalk**
  - Use case: Maintaining character consistency in long video generation while speeding up inference
  - *From: mdkb*

- **Stacking multiple reference images in VACE**
  - Use case: Improving character consistency by providing multiple angle references
  - *From: ˗ˏˋ⚡ˎˊ-*

- **VACE with ControlNet for First-Frame-Last-Frame morphing**
  - Use case: Converting long videos (150+ frames) while maintaining consistency between segments
  - *From: buttercup5108*

- **Dual model mode: Wan 2.2 + VACE 2.2 fun**
  - Use case: Faster generation that can hit higher resolutions
  - *From: mdkb*

- **Using multiple reference images with VACE**
  - Use case: Stitching references like with Qwen edit for better control
  - *From: Gleb Tretyak*

- **Automated prompt generation with Humo + Gemini LLM**
  - Use case: Takes reference image and transcribed lyrics to auto-generate 16 different prompts instead of manual copy-paste from ChatGPT
  - *From: VRGameDevGirl84(RTX 5090)*

- **Character training on Replicate**
  - Use case: Upload 50 images, get character LoRA in 30 mins for ~$0.50 on H100
  - *From: Ruairi Robinson*

- **VACE 2.2 with SEG Anything Ultra V2**
  - Use case: Character swapping using segmentation and reference images, easier than previous SAM2 method
  - *From: mdkb*

- **Humo workflow for character animation**
  - Use case: Upload image and song, creates character animation automatically
  - *From: VRGameDevGirl84(RTX 5090)*

- **Use InfiniteTalk silence node for long video**
  - Use case: Replace InfiniteTalk/Multitalk long video encoder node to make long videos
  - *From: slmonker(5090D 32GB)*

- **Replacement mode is just animate with a mask**
  - Use case: Subject replacement in videos
  - *From: Kijai*

- **Can use similar loop as infinitetalk for long generation**
  - Use case: Extended video generation
  - *From: Kijai*

- **Simple MattAnyone group saved as Node Template**
  - Use case: Alternative to DWPose detection
  - *From: JohnDopamine*

- **Use Wan 2.2 Animate with pose and reference only**
  - Use case: Character animation without face detection complexity
  - *From: Atlas*

- **Multiple reference images by combining in single image**
  - Use case: Using both close-up and full body reference shots
  - *From: 🦙rishappi*

- **SDXL Lightning for input images + Wan 5B I2V at 580p**
  - Use case: Cost-effective video generation pipeline
  - *From: mallardgazellegoosewildcat*

- **WanAnimate with relight LoRA**
  - Use case: Better character blending and lighting consistency
  - *From: Kijai*

- **WanAnimate without background masking**
  - Use case: Simple character animation by deleting masking components
  - *From: A.I.Warper*

- **Short clip generation**
  - Use case: Set frame window = num frames to disable looping for short clips
  - *From: Kijai*

- **Using WanAnimate without reference image**
  - Use case: Character swapping - every character converts to the reference one
  - *From: Piblarg*

- **Combining pose and depth maps**
  - Use case: Better handling of backward facing scenes that pose gets wrong
  - *From: Clément*

- **Face-only animation with mask**
  - Use case: Isolating animation to just facial features
  - *From: T2*

- **Low denoise phantom pass after Lucy Edit**
  - Use case: To nudge likeness closer while maintaining quality
  - *From: ArtOfficial*

- **Using 2 ksamplers advanced with start_at_step end_at_step**
  - Use case: Attempting to splice latents together
  - *From: buttercup5108*

- **Fun Reward at 1.0 strength during first phase, then 0.5 on 2nd and 3rd phase**
  - Use case: Better quality results
  - *From: pom*

- **Auto slowest speed best quality setup for Wan 2.2 VACE**
  - Use case: Segment and extend workflow for long video generation
  - *From: Gleb Tretyak*

- **Using points editor with SAM2 for character tracking**
  - Use case: Character swaps with VACE, use red dots for mask edges and green dots for mask area
  - *From: mdkb*

- **Windows of 121 frames for looping**
  - Use case: Akin to InfiniteTalk looping, works with wrapper but becomes deep fried by 3rd window
  - *From: ˗ˏˋ⚡ˎˊ-*

- **FFLF using Phantom model with VACE 2.2 module**
  - Use case: First-Frame-Last-Frame morphing with mixed model versions
  - *From: mdkb*

- **Modified WanAnimate with Qwen2.5VL masking**
  - Use case: Faster and smarter masking process, 155 frames in 30 seconds
  - *From: piscesbody*

- **Native WanAnimate with custom utility nodes**
  - Use case: Using LatestVideoFinalFrame node for auto-running and video combination
  - *From: Flipping Sigmas*

- **Remove bg image and mask for stronger controlnet effect**
  - Use case: Getting stronger animation control without replacement
  - *From: slmonker(5090D 32GB)*

- **Multiple character replacement by running one by one with different masks**
  - Use case: Animating multiple characters in same scene
  - *From: Klinter*

- **Use frame offset in VHS to start from character appearance**
  - Use case: When target character doesn't appear in first frame
  - *From: Klinter*

- **Use samples from WanVideoWrapper for video2video refinement**
  - Use case: Character consistency across generations using existing video as input
  - *From: Kijai*

- **Remove background and character mask for reference image background**
  - Use case: When you want reference image background instead of control video background
  - *From: ArtOfficial*

- **T2V and I2V training in same run**
  - Use case: Training LoRAs that work for both text-to-video and image-to-video
  - *From: JohnDopamine*

- **Using frozen frames from video cuts with Infinite Talk**
  - Use case: Audio-driven lip sync with reference frames from movie clips
  - *From: NC17z*

- **First-Frame-Last-Frame morphing with FramePackWrapper**
  - Use case: Video extension and frame interpolation
  - *From: Léon*

- **Wan 2.2 Animate for 12GB VRAM**
  - Use case: Low VRAM video generation, 113 frames @ 640p in under 10min
  - *From: harriet_h*

- **Using WanAnimatePreprocess to replace manual pose/face detection**
  - Use case: Simplifies workflow by removing points editor and manual detection nodes
  - *From: Kijai*

- **PUSA extension workflow**
  - Use case: Extending videos but requires per-generation tuning of LoRA strengths and CFG
  - *From: DawnII*

- **Context windows for long videos**
  - Use case: Generate 393 frames at 720x1280 using frame windows with overlap
  - *From: Kijai*

- **Perfect loop creation**
  - Use case: Generate video with i2v -> feed last frame to FLF model with original as final frame
  - *From: Danial*

- **Dual model VACE + Wan 2.2**
  - Use case: Character swapping using i2v mask with VACE module, works on 3060 RTX with optimization
  - *From: mdkb*

- **Object replacement using masking**
  - Use case: Replace objects in videos like bikes with horses while keeping person
  - *From: hicho*

- **Character replacement with pose control**
  - Use case: Replace characters while maintaining original pose and movement
  - *From: Léon*

- **Virtual try-on workflow**
  - Use case: Testing clothing and appearance changes on people in videos
  - *From: Lodis*

- **Mask cleanup for object tracking**
  - Use case: Clean up blockify mask interference by running mask cleanup before block node
  - *From: Kijai*

- **Regional Adaptive Sampling for WAN**
  - Use case: KV Cache technique for accelerating diffusion transformer inference, experimental WAN support
  - *From: JohnDopamine*

- **Long video generation using batch processing**
  - Use case: Generating 161+ frame videos by splitting into batches
  - *From: mdkb*

- **Multi-modal character animation with MagRef + InfiniteTalk**
  - Use case: Combining image-to-video with audio-driven facial animation
  - *From: samhodge*

- **Character consistency with pose transfer**
  - Use case: Making stick figures adapt to different character proportions
  - *From: harriet_h*

- **Latest KJ workflow with ViT node**
  - Use case: Preprocessing for Wan generation
  - *From: justinj*

- **Context window setup for longer videos**
  - Use case: Processing 154+ frame videos with proper context handling
  - *From: Gateway {Dreaming Computers}*

- **FUN VACE with frame padding for long videos**
  - Use case: Creating hours-long continuous video sequences using 5-20 frame overlap with grey padding
  - *From: seitanism*

- **LLM-driven sequential video generation**
  - Use case: Using LLMs to generate prompts for each segment based on final frame of prior segment
  - *From: JohnDopamine*

- **Wan 2.5 integration with n8n**
  - Use case: API workflow integration for automated video generation
  - *From: Gateway {Dreaming Computers}*

- **V2V to 1080p then VACE extension and interpolation**
  - Use case: Creating Wan 2.5 equivalent at home
  - *From: FL13*

- **WanAnimate single gen with pose, face and mask**
  - Use case: Character animations and turn-arounds
  - *From: Kijai*

- **Multiple samplers chained for extensions**
  - Use case: Creating longer sequences in native ComfyUI without wrapper
  - *From: Kijai*

- **VFX compositing with VACE for 3D character integration**
  - Use case: Track shot, add 3D asset, create infill mask, use DepthAnything, reference image, process with Wan 2.1 + VACE
  - *From: Neex*

- **Car replacement with automatic masking**
  - Use case: Automatic masking segmentation and LoRA model insert for replacing cars in videos
  - *From: Tonon*

- **Video LoRA training with mixed content**
  - Use case: Mix of images and videos, more images than videos as easier to prepare, caption specific motions
  - *From: crinklypaper*

- **Batch I2V using VHS load images from folder with increment nodes**
  - Use case: Processing multiple images to videos automatically
  - *From: Draken*

- **Use official Wan site for prompt enhancement and tags, copy to ComfyUI**
  - Use case: Better prompting experience and avoiding API limitations
  - *From: hicho*

- **QwenImage to Wan2.2 pipeline**
  - Use case: Generating anime videos with high success rate
  - *From: Drommer-Kille*

- **Uni3C with WanAnimate**
  - Use case: Better camera control in character animation
  - *From: DawnII*

- **MultiGPU node usage**
  - Use case: Running VACE with limited VRAM, works on wrapper too
  - *From: SonidosEnArmonía*

- **Multi-stage VACE pipeline for lipsync**
  - Use case: First VACE with FLF and camera movement, then V2V with Infinite for lipsync, finally another VACE FLF
  - *From: yukass*

- **Batch interpolation for clips**
  - Use case: Minimal workflow for processing multiple clips
  - *From: Drommer-Kille*

- **VACE 2.2 with only low model**
  - Use case: Works fine without needing high+low dual samplers
  - *From: lemuet*

- **Separate character passes for multiple people**
  - Use case: Do each person in their own WanAnimate pass for multi-character scenes
  - *From: 42hub*

- **Use WanVideo ImageToVideo Encode node instead of Long I2V Multi/InfiniteTalk for InfiniteTalk**
  - Use case: When InfiniteTalk fails with the multi-node setup
  - *From: Vérole*

- **Remove mask and background image connections to prevent background replacement**
  - Use case: When you want to keep original image background in Wan Animate
  - *From: Charlie*

- **Use dyno full model for high noise + lightx2v lora for low noise**
  - Use case: Best current setup for Wan 2.2 generation
  - *From: Kijai*

- **3KSampler node giving website-quality results**
  - Use case: Matching official website output quality
  - *From: Ansel*

- **GGUF conversion process**
  - Use case: Converting Wan models to quantized GGUF format
  - *From: patientx*

- **Context windows for longer videos**
  - Use case: Preventing color shift and degradation in extended video generation
  - *From: U̷r̷a̷b̷e̷w̷e̷*

- **VACE and Phantom in FFLF with controlnets**
  - Use case: Good quality video generation workflow
  - *From: mdkb*

- **Blender camera animation with Uni3C**
  - Use case: Simple viewport render from Blender for camera motion, use strength 4.0 on high noise only
  - *From: xwsswww*

- **Pusa workflow modifications**
  - Use case: Adapted Pusa workflow without actual LoRAs, works with dpm++_sde
  - *From: Dever*

- **Wan 2.2 Fun VACE inpainting using only low sampler**
  - Use case: Video inpainting without mask edge artifacts
  - *From: SonidosEnArmonía*

- **Modified 2.2 inpaint workflow from native ComfyUI**
  - Use case: Inpainting with two model version setup
  - *From: Ablejones*


## Recommended Settings

- **PUSA LoRA strength**: High: 1.5, Low: 1.4
  - Recommended settings from official implementation
  - *From: ˗ˏˋ⚡ˎˊ-*

- **CFG scale with LightX2V**: 1.0
  - For 4-step acceleration
  - *From: NebSH*

- **Denoise strength for lip-sync**: 0.6 or 0.7
  - Works better than raw latent noise mask
  - *From: Ablejones*

- **CFG for PUSA**: 1.5 to 2.0 for good results, no CFG also works
  - Lower CFG prevents burning/overexposure
  - *From: Kijai*

- **LightX2V LoRA strength**: 2.0 or 3.0
  - Much better results than 1.0 with 2.2 high noise
  - *From: Kijai*

- **Step configuration**: 10 split by 4 and 20 split by 12
  - For different motion speeds in output
  - *From: 𝕯𝖗. 𝕸𝖆𝖈𝖆𝖇𝖗𝖊 ☠*

- **Frame window and motion overlap**: Default 81 - 9 = 72 new frames each iteration
  - Each window is frame_window_size minus motion_frame
  - *From: Kijai*

- **Resized Pusa LoRA strength**: 1.4-1.5
  - Recommended alpha values from official documentation
  - *From: Hippotes*

- **Pusa LoRA strength**: 1.4 minimum
  - Original default that ensures proper functionality
  - *From: Kijai*

- **Wan default FPS**: 16 fps
  - Fixed framerate for Wan model
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Frame calculation**: seconds × 16 + 1 extra frame
  - Wan samples in batches of 4, adds extra frames
  - *From: Kenk*

- **LightX2V LoRA strength**: 0.5 for high, 1 for low
  - Better motion control compared to higher values
  - *From: Dever*

- **Context extension frames**: 9 or 13 frames minimum
  - Practical minimum for effective context-based extension
  - *From: Kijai*

- **Block swap for context workflows**: 20 blocks
  - Worked for 4080 16GB VRAM + 96GB RAM setup
  - *From: Dever*

- **Video framerate for 10 second output**: 16 fps
  - 161 frames at 16fps = 10 seconds, original workflow used 24fps
  - *From: Dever*

- **Pusa LoRA resize**: Quarter size
  - Works fine even at 25% of original 512 rank size
  - *From: Kijai*

- **main_device option**: Will be removed/ignored
  - Now redundant with new model loading system
  - *From: Kijai*

- **offload_device**: Use instead of main_device
  - Prevents OOM issues with new loading system
  - *From: HeadOfOliver*

- **LightX2V strength**: Lower than 1.0
  - Can improve quality, requires more steps/CFG
  - *From: Kijai*

- **PCIe lane**: Gen4 instead of Gen5
  - Rumored to prevent GPU crashes, though didn't help for this user
  - *From: Drommer-Kille*

- **Pusa LoRA strength**: 1.5 and 1.4
  - Optimal strength values for Pusa LoRA
  - *From: Mngbg*

- **CFG for Pusa**: >1
  - For Pusa it is desirable to use cfg>1
  - *From: Mngbg*

- **High/Low noise overlap**: 48/24
  - Reduced high overlap from 48 to 24 for better context blending
  - *From: Dever*

- **Block swapping**: 20 blocks for 14B model
  - Saves half the model's size in VRAM
  - *From: Kijai*

- **VRAM reserve**: 2-3 GB
  - Enough if using PC while generating with monitor on same GPU
  - *From: Kijai*

- **Wan 2.1 LoRA strength with 2.2 models**: 3.0 for high noise model, lower strength for low noise model
  - LoRAs not made for 2.2 high noise model need higher strength, low noise is almost same as 2.1
  - *From: Kijai*

- **Pusa block swap for higher resolutions**: Increase from 10 to 30 block swap for 752x976 resolution
  - Pusa is heavy and requires more block swap for higher resolutions
  - *From: Ashtar*

- **Context window values for 10-20 second videos**: Standard context values work, no need to change for different durations
  - Context settings don't need adjustment for 10s, 15s, or 20s generations
  - *From: Ashtar*

- **InfiniteTalk generation time**: 40 mins on 5090 for 5500 frames using 4 steps
  - Using only 4 steps with LightX2V LoRA for speed optimization
  - *From: Kijai*

- **CFG for non-LightX workflows**: 3.5 for both low and high noise
  - Base model requires higher CFG when not using lightning models
  - *From: mamad8*

- **Steps without LightX**: 20 total steps (10+10 split)
  - Sufficient for good quality with I2V model
  - *From: mamad8*

- **Context window stride settings**: Stride 10 for high noise, stride 4 for low noise, overlap 48, pyramid fuse_method
  - Prevents cuts between context windows
  - *From: mamad8*

- **Pusa noise multipliers**: Per extra latent added, not whole list
  - System expects multipliers for injected latents only
  - *From: Kijai*

- **Audio CFG**: 1.0
  - Audio CFG at 2.0 vs 1.0 showed minimal difference
  - *From: samhodge*

- **High noise sampler CFG**: 3.5
  - Much better results than CFG 1
  - *From: Drommer-Kille*

- **Low noise sampler CFG**: 1.0
  - Used with 4-step Lightning LoRA
  - *From: Drommer-Kille*

- **Context window overlap**: 65 frames overlap in 121 frame context
  - Blends well for extended generations
  - *From: samhodge*

- **Resolution for A6000**: 832x480
  - Takes little over an hour for 250 frames
  - *From: samhodge*

- **VRAM requirement for 720p 81 frames**: 37GB
  - GPU memory usage with 40 context window
  - *From: samhodge*

- **Best samplers for 5B model**: euler_a/lcm + simple, sgm or beta
  - Work best with both fast and turbo variants
  - *From: Dita*

- **VRAM optimization**: Use low VRAM mode and native block swap
  - Reduces usage from 5GB to 2.6GB
  - *From: hicho*

- **Video extension overlap**: 9 frames
  - Works great for seamless extension
  - *From: Dr. Macabre*

- **Resolution scaling**: 848x480 base, scale to 1280x720
  - Stays within 24GB VRAM limits with upscaling
  - *From: samhodge*

- **Lightx2v LoRA strength**: High: 3, Low: 1.5
  - Better quality than Lightning LoRAs
  - *From: Lodis*

- **Lightning LoRA strength**: 0.125
  - Recommended by Kijai for newer Lightning LoRAs
  - *From: Santodan*

- **DPM++ samplers with beta schedulers**: Around 6 steps
  - Higher quality output
  - *From: Lodis*

- **V2V denoise**: 0.60
  - Fixes motion issues when denoise 1 produces no motion
  - *From: hicho*

- **24GB VRAM resolution**: 1024x576x109 frames with 16/64 context
  - Using block swapping
  - *From: N0NSens*

- **Sampler choice for 2.2**: dpm+sde
  - Better than euler (causes ghosting) and unipc
  - *From: N0NSens*

- **Blockswap**: 40
  - For 5090 with multi-speaker models, manages VRAM usage
  - *From: blake37*

- **Resolution for multi-speaker**: 768x1024
  - Used with blockswap 40 setup
  - *From: blake37*

- **LoRA rank**: 256
  - Provides better animation and dynamics than lower ranks
  - *From: 𝕯𝖗. 𝕸𝖆𝖈𝖆𝖇𝖗𝖊 ☠*

- **Sampler steps distribution**: 2/2/2 (6 total)
  - For three sampler workflow with different LoRAs
  - *From: .: Not Really Human :.*

- **Video length for Wan 2.2**: 4 seconds
  - Avoids slowmotion issues that occur at 7 seconds
  - *From: Kenk*

- **Split ratio for i2v**: 0.9
  - Proper denoising split for image to video
  - *From: Dita*

- **Split ratio for t2v**: 0.875
  - Proper denoising split for text to video
  - *From: Dita*

- **LightX2V lora strength**: 2.0
  - Works alone but order matters with other loras
  - *From: Hoernchen*

- **Lora rank for character work**: 128
  - Good balance for character consistency
  - *From: Charlie*

- **InfiniteTalk window size**: 81 frames minimum
  - Loop node works in window sizes, under 81 wouldn't use loop node
  - *From: Kijai*

- **Shift value for MagRef GGUF**: 6
  - Example workflow had shift at 11 which seems excessive, 6 works without problems
  - *From: mdkb*

- **VACE control strength**: 0.5
  - For detailing lower quality videos with denoise ~0.5
  - *From: Ablejones*

- **Manual sigma values for 6 steps**: 1.0000, 0.9375, 0.8750, 0.4375, 0.0000
  - Linear split works best for low step counts
  - *From: phazei*

- **InfiniteTalk frames for longer videos**: 249 frames
  - To generate videos longer than 5 seconds, increase from default 149 frames
  - *From: Santoshyandhe*

- **Reward LoRA strength**: 1.0
  - Best balance of detail enhancement without artifacts
  - *From: crinklypaper*

- **Context overlap**: 8
  - Faster processing than default 40 while maintaining quality
  - *From: mdkb*

- **tiled_decode in SD upscaler**: off
  - Prevents VAE issues with Wan models
  - *From: FL13*

- **Reward LoRA strength**: 0.4 instead of 0.5
  - 0.5 was too strong
  - *From: Kijai*

- **InfiniteTalk window processing**: Every window same size regardless of input frames
  - How the system is designed to work
  - *From: Kijai*

- **Steps for max quality without speed LoRAs**: 40-50 steps total (20/20 or 25/25)
  - For maximum quality I2V generation
  - *From: . Not Really Human .*

- **H100 generation time**: 3 minutes for 81 frames at 720p
  - With lightx2v and 3 ksampler setup
  - *From: vuuw*

- **Radial attention block_size**: 128
  - Faster than 256/512, only supported sizes are 64/128
  - *From: Kijai*

- **MPS/HPS LoRA strength**: 0.5
  - Default recommended strength for reward LoRAs
  - *From: Kijai*

- **Skyreels LoRA strength**: 2.0
  - Helps prevent looping in longer generations
  - *From: Zabo*

- **Upscaling denoise**: 0.2-0.3
  - Low denoise preserves original content while improving details
  - *From: FL13*

- **LoRA strength for Light2X**: 0.5
  - Better results than default strength
  - *From: dipstik*

- **DWPose detect_body**: disabled or blend factor 0.1-0.05
  - Prevents stick figure artifacts
  - *From: Akumetsu971*

- **USDU denoise**: 0.08
  - Works well for combining video segments
  - *From: mdkb*

- **Empty embeds frames**: 1
  - Improves image quality in wrapper
  - *From: scf*

- **Shift parameter for LoRAs**: 8 for likeness, 1 for image quality
  - Balance between character likeness and plastic skin appearance
  - *From: mamad8*

- **MPS weight for Wan 2.2**: 0.5
  - Initially suggested value that works well
  - *From: mdkb*

- **Steps for 5B model**: 50 steps without turbo wan
  - Best results from 5B, but at that point might as well use 14B
  - *From: crinklypaper*

- **LightX LoRA strength**: 1.2-1.5
  - Creates extra movement and overexaggerated facial expressions
  - *From: VRGameDevGirl84(RTX 5090)*

- **Radial attention resolution threshold**: Not useful at 480p, clearly beneficial at 720p
  - Resolution and sequence length both count as dimensions for radial benefit
  - *From: Kijai*

- **Block swap**: Up to 40
  - Better memory management than default 20
  - *From: Kijai*

- **HuMo default specs**: 25 fps, 97 frames
  - Based on 2.1 architecture
  - *From: Kijai*

- **Subject LoRA training**: Rank 64, 12-16 face images, 700-1000 steps, Low Lora 0.5 strength for High steps, 1.0 for Low steps
  - Should converge in about an hour on 4090
  - *From: mccoxmaul*

- **FPS for lipsync**: 25fps
  - Prevents lipsync drift that occurs at 24fps
  - *From: mdkb*

- **LightX2V lora strength for I2V**: 5.6 and 2.0
  - Works well for I2V applications
  - *From: patientx*

- **GPU power limit**: 280W (80% for 3090)
  - Minimal performance hit while managing heat
  - *From: daking999*

- **audio_scale**: 1.0
  - Higher values cause color artifacts and image degradation
  - *From: blake37*

- **VAE version**: 2.1
  - VACE 2.2 requires VAE 2.1, not 2.2 (which is for 5B model)
  - *From: Cseti*

- **numpy version**: <2.0
  - Prevents blue/broken image artifacts
  - *From: mdkb*

- **LoRA strength**: 0.5 for both reward LoRAs
  - Better quality balance
  - *From: xiver2114*

- **CFG**: 6+
  - Needed with reward LoRAs due to distillation vs original 3-pass CFG
  - *From: Kijai*

- **Sampler**: dpmpp sde gpu beta57
  - Massive quality improvement over uni_pc beta
  - *From: Gleb Tretyak*

- **HuMo FPS**: 25
  - Proper frame rate for HuMo generation
  - *From: Kijai*

- **Steps**: 30 without speedup LoRAs
  - Good balance for VACE 2.2 generation
  - *From: Zuko*

- **fps**: 25
  - Required for proper HuMo sync
  - *From: Kijai*

- **num_frames**: -1
  - Uses audio length automatically
  - *From: Kijai*

- **context frames**: 16
  - Default context window setting that works well
  - *From: cyncratic*

- **steps**: 4
  - Can achieve good results with just 4 steps
  - *From: Kijai*

- **max frame length**: 129
  - Maximum frames supported by HuMo at 25fps (~5 seconds)
  - *From: Kijai*

- **HuMo steps**: 4 steps minimum with lightx2v
  - Can work with only 4 steps when using lightx2v lora
  - *From: Kijai*

- **HuMo frame limit**: 97 frames at 25 fps
  - Official limit - generating longer may degrade performance
  - *From: Kijai*

- **Context window resolution**: 640x960
  - Better performance and faster than 720x1280 for long generations
  - *From: aidiffuser*

- **Context window frames**: 30 frames minimum for HuMo
  - Lower than 65 frames not tested, 30 works but may cause cuts between windows
  - *From: Kijai*

- **Block swap**: 30
  - Used with 30 frame context windows for HuMo
  - *From: xwsswww*

- **Audio scale**: 1.4
  - For perfect lipsync with fast rap music
  - *From: Charlie*

- **Steps with radial attention**: 7 steps
  - Used in successful 1280x768 1375 frames generation
  - *From: Charlie*

- **USDU temporal_frames**: 84
  - Fixes flickering in middle of video (default 64 causes issues)
  - *From: FL13*

- **USDU denoise**: 0.2
  - For smoothing/adding detail to existing video
  - *From: ingi // SYSTMS*

- **VACE control frames**: Gray (0.5 or 127 RGB)
  - Neutral/empty value for inpainting
  - *From: Kijai*

- **Launch arguments for RTX 3090**: --normalvram instead of --highvram
  - Prevents CUDA memory allocation errors
  - *From: herpderpleton*

- **GPU fan control**: 50% at idle
  - Prevents thermal spikes when load is applied
  - *From: Charlie*

- **HuMo minimum frames**: 5 frames minimum
  - Model limitation for generation
  - *From: Kijai*

- **VACE 2.2 generation**: 832x480 to 1280x720
  - Recommended resolution range for good results
  - *From: Ablejones*

- **Triton cache paths**: C:\Users\<username>\AppData\Local\Temp\torchinductor_<username>\triton and C:\Users\<username>\.triton
  - Clear these after PyTorch updates to fix compilation issues
  - *From: Kijai*

- **Frame rate for 5B model**: 24 fps instead of 16 fps
  - 5B model uses different frame rate than other variants
  - *From: FL13*

- **HuMo generation parameters**: 97 frames at 25 fps, 2 steps with speed LoRAs
  - Model limitation for current version
  - *From: Kijai*

- **Best sampler for lightx2v**: dpm++_sde
  - Works best with lightx2v LoRA
  - *From: Kijai*

- **Best sampler without lightx2v**: unipc
  - Usually works best without speed LoRAs
  - *From: Kijai*

- **VRAM usage optimization**: Keep VRAM below 95%, reduce block count if not at 95%
  - Optimal memory management for block swap
  - *From: Kijai*

- **Humo 1.7B with CausVid**: 4-8 steps, 480x832, CFG 5, euler-beta
  - Works efficiently under 7GB VRAM
  - *From: patientx*

- **LightX2V strength for 2.2 high noise**: 2.5-3.0
  - Higher strength needed with 2.2 compared to 2.1
  - *From: Hoernchen*

- **Step distribution for 2.2**: 0/3 3/-1 or 1000
  - Proper step start/stop for both samplers
  - *From: Hoernchen*

- **Audio scale for better mouth movements**: 2.5
  - Improves mouth movements in Humo
  - *From: VRGameDevGirl84(RTX 5090)*

- **CFG for first step**: Around 3.0
  - Good starting point, can go higher if no burning or wacky motion
  - *From: Kijai*

- **VACE blocks**: 8 VACE blocks instead of 5
  - For character swapping workflows
  - *From: Kijai*

- **HuMO block swap**: 30 blocks
  - Bigger model needs more block swap than normal model for same resolution/frame count
  - *From: amli*

- **CFG schedule**: 0,0,3,3,3,3,3,3 for 8-steps
  - Better results with CFG scheduling
  - *From: patientx*

- **VACE strength**: 1.35 or reduce to 0.7-1.0
  - Higher values cause contrast issues, lower values reduce contrast
  - *From: buttercup5108*

- **Radial attention resolution**: 1280x768 instead of 1280x720
  - Image size must be divisible by block size (128)
  - *From: Charlie*

- **HuMO max frames**: 97 frames maximum
  - Model limit, crashes beyond this
  - *From: VRGameDevGirl84(RTX 5090)*

- **Frame window size for InfiniteTalk**: 81 frames
  - Value the model handles well, avoids rounding up issues
  - *From: Kijai*

- **Power limit for stability**: nvidia-smi -pl <watts> (e.g. 400W)
  - Prevents crashes from excessive power draw
  - *From: Kijai*

- **prefetch_block**: 1
  - With prefetch enabled, move from CPU to GPU shouldn't take any time
  - *From: Kijai*

- **use_non_blocking**: enabled
  - Faster but uses more memory
  - *From: lostintranslation*

- **Block swap count**: 30 for 81 frames
  - Optimal performance hitting 95% VRAM utilization
  - *From: lostintranslation*

- **CFG for over-animation**: Below 1.5, use fractions
  - To reduce excessive motion
  - *From: Kijai*

- **CFG for Wan**: 3.5 at 20 steps for first high pass
  - User reported good results with these settings
  - *From: mccoxmaul*

- **Motion LoRA strength**: 1.6
  - User found their LoRA doesn't work at 1.0 but starts showing at 1.6
  - *From: Ryzen*

- **VACE strength for 2.2**: 1.5
  - Helps follow DWPose control
  - *From: xwsswww*

- **vm.swappiness**: 0
  - Prevents virtual memory from slowing down model loading on Linux
  - *From: MysteryShack*

- **CFG scale**: 3.5
  - Fixes overexposure issues with dim light prompting
  - *From: Drommer-Kille*

- **GPU wattage limit**: 400W
  - Prevents Wan from crashing PC
  - *From: Drommer-Kille*

- **LoRA strength**: HN str 3, LN str 1
  - Common configuration across workflows
  - *From: mdkb*

- **Default FPS**: 30
  - Code default based on control
  - *From: DawnII*

- **frame_window_size**: 81 (default)
  - Refs are added to latents making 81 for the model
  - *From: Kijai*

- **pose_strength**: 0.1
  - Lower values for better control
  - *From: Kijai*

- **face_strength**: adjustable setting
  - Might help when face encoder struggles with non-faces
  - *From: Kijai*

- **lightx2v strength**: 1.5 or higher
  - Can and should be higher than default
  - *From: Kijai*

- **Block swap**: 25 for 1024x576x97, avoid 30-40
  - Higher values cause device mismatch errors
  - *From: slmonker(5090D 32GB)*

- **Frame window size**: 77 (constant)
  - Model uses fixed windowing, can't do partial windows
  - *From: Kijai*

- **Total frames for windowing**: 161 (not 162)
  - Must follow 4+1 rule to avoid tensor size mismatches
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Face crop resolution**: 512x512 (hardcoded)
  - Face processing is fixed at this resolution
  - *From: Kijai*

- **LightX LoRA strength**: 1.0
  - Standard strength for 6 steps
  - *From: slmonker(5090D 32GB)*

- **Steps for LightX**: 6 steps
  - As set by Kijai, works well
  - *From: slmonker(5090D 32GB)*

- **CFG for WanAnimate**: 1
  - Default non-LoRA CFG
  - *From: xiver2114*

- **Pose and face strength**: 1
  - Prevents black artifacts
  - *From: Instability01*

- **Block size for masking**: 32 pixels
  - Used in Kijai example workflow
  - *From: scf*

- **Block swap prefetch**: 15 and 1 prefetch
  - Reduces generation time from 120 sec/it to 54 sec/it
  - *From: patientx*

- **Default WanAnimate parameters**: 20 steps, cfg 1.0, shift 5.0
  - Official default settings
  - *From: Kijai*

- **Window size for long generations**: 121 frames
  - Works fine if you have the VRAM to hold it
  - *From: A.I.Warper*

- **Face strength**: 0
  - Fixes eye gaze tracking problems
  - *From: A.I.Warper*

- **Steps for Wan VACE 2.2**: 50
  - 20 steps too little, 50 is normal
  - *From: Kijai*

- **Resolution divisibility**: 64
  - Helps avoid grid block artifacts
  - *From: Quality_Control*

- **CFG**: 1
  - With lightx to avoid CFG burn
  - *From: Gleb Tretyak*

- **Scheduler/Sampler**: unipc/beta
  - Used in wrapper
  - *From: Gleb Tretyak*

- **Frame count**: 77
  - Multiples of 77 avoid memory errors, reference adds extra latent
  - *From: xiver2114*

- **Model sampling**: 2 or 1
  - To improve quality
  - *From: Rainsmellsnice*

- **Steps**: 40 minimum
  - Without distillation
  - *From: ˗ˏˋ⚡ˎˊ-*

- **CFG**: 3.5ish
  - Good balance, 6 might be too high
  - *From: ˗ˏˋ⚡ˎˊ-*

- **NAG strength**: 3/5
  - Used in best setup for Wan 2.2 Fun VACE
  - *From: Gleb Tretyak*

- **LightX LoRA weight**: 1/1
  - Part of best setup configuration
  - *From: Gleb Tretyak*

- **Face strength**: 1.0
  - Required to fix black square artifacts in masks
  - *From: Kijai*

- **Mask block size**: 32 (default)
  - Good default value for preventing mask artifacts
  - *From: Dever*

- **Steps with lightning LoRA**: 10 steps
  - 10 steps with LightX and NAG produce better results than 50 steps
  - *From: Gleb Tretyak*

- **CFG**: Start at 3, then adjust. Try 6 for VACE 2/1
  - No number set in stone, depends on scenario
  - *From: DawnII*

- **Steps for Wan2.2**: 50 steps with uni pc beta
  - Recommended setting, though 50 destroys some outputs
  - *From: Gleb Tretyak*

- **Block swap minimum**: 25 minimum for 12GB VRAM, 16 for better systems
  - Memory management
  - *From: patientx*

- **LoRA weights**: lightxv2 @ 1.2 strength, relight @ 1.0 strength
  - Tested configuration for GGUF comparisons
  - *From: patientx*

- **Resolution**: 832×1536 for high quality results
  - Higher resolution greatly improves results
  - *From: 1236961470231609364*

- **WanVideo block swap**: 25 instead of 35
  - Prevents CUDA out of memory errors
  - *From: 435512773737447446*

- **Frame window size**: Equal to total frames for short clips
  - Prevents video extending beyond original framecount
  - *From: Kijai*

- **Prefetch**: 0 for full block swap
  - Loads 2 blocks minimum for full swap
  - *From: Kijai*

- **Dynamic in torch compile**: True for Blackwell cards
  - Speeds up processing from ~500s to ~300s after first intensive run
  - *From: Canin17*

- **VAE precision**: fp16 or bf16
  - Halves VRAM use and drastically reduces gen time
  - *From: Kijai*

- **Block swap for 12GB VRAM**: 40 blocks with 1 prefetch
  - Should work easily with torch compile
  - *From: Kijai*

- **Window size calculation**: Total frames / 2 for optimal performance
  - Avoids inefficient partial windows
  - *From: CaptHook*

- **Face strength for masking**: 1.0
  - Lower values screw up the mask quality
  - *From: Kijai*

- **Relight LoRA strength**: 2.0 for heavy lighting changes
  - Integrates lighting of driving video with reference image
  - *From: HeadOfOliver*

- **Pose and face strength for higher resolution**: Pose 0.6, Face 0.8
  - Works better at higher resolutions
  - *From: buttercup5108*

- **Frame window size**: 77 instead of 113
  - Reduces VRAM usage without quality loss
  - *From: Kijai*

- **VAE precision**: fp16
  - Prevents maxing out VRAM, fp32 uses too much memory
  - *From: Kijai*

- **Block swap**: 25 or 40 with prefetch 0
  - Allows 6GB VRAM usage, reduces memory impact
  - *From: Kijai*

- **Video resolution**: Divisible by 8
  - Required for proper tensor operations
  - *From: traxxas25*

- **Force Rate in Video Loader**: 16 frames
  - Standard setting for Wan models
  - *From: Léon*

- **blockswap**: 40
  - For 389 frames at 720x1280 with 64GB RAM
  - *From: Kijai*

- **blockswap**: 35
  - User setting for 720p 81 frames with 128GB RAM
  - *From: slmonker(5090D 32GB)*

- **character LoRA strength**: 1.0
  - For character consistency in T2V mode
  - *From: el marzocco*

- **padding**: 0
  - Avoid alignment issues when not using reference mode
  - *From: Kijai*

- **CFG schedule for PUSA**: 3,3,3 on first steps
  - Prevents burning while maintaining quality
  - *From: DawnII*

- **Context frames for Wan Animate**: 77 or 81 frames
  - Works best around these values, quality degrades with more frames
  - *From: Kijai*

- **Block swap setting**: 40 for 8GB cards
  - Enables higher resolution on lower VRAM
  - *From: xwsswww*

- **VAE precision**: f16 instead of f32
  - Reduces VRAM usage significantly for long generations
  - *From: Dkamacho*

- **Face strength**: 1.0 or higher
  - Values below 1.0 cause masking artifacts in VACE
  - *From: Kijai*

- **Reward LoRA strength**: 0.5 maximum
  - Default value, don't exceed for MPS/HPS loras
  - *From: Kijai*

- **Steps**: 4
  - Good results achieved with only 4 steps for both realistic and anime style
  - *From: Lodis*

- **Face strength**: Lower values
  - Better results when lowered for character replacement
  - *From: Léon*

- **Precision matching**: Use consistent dtypes - fp16 model with fp16 modules
  - Prevents black screen issues
  - *From: Kijai*

- **WAN 2.5 pricing**: 480p: $0.05/s, 720p: $0.10/s, 1080p: $0.15/s
  - Official pricing structure
  - *From: Hippotes*

- **Shift parameter**: Above 10 for 16-20 steps
  - Higher shift improves layout and motion
  - *From: BecauseReasons*

- **Steps for SDE samplers**: 200+ steps
  - Allows very low or zero shift values
  - *From: mallardgazellegoosewildcat*

- **refert_num parameter**: Overlap frames for temporal guidance
  - Controls how many frames are used for temporal guidance
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Hand stick width**: 1
  - Fixes hand detection issues
  - *From: Léon*

- **LoRA training steps**: 7000 steps on 50 images
  - For complex captioned datasets without overfitting
  - *From: Ryzen*

- **LoRA rank**: 64
  - Better for complex captions and motion tracking compared to 32
  - *From: Ryzen*

- **Infinite talk denoise**: 50%
  - For SOTA V2V results when combined with wan animate
  - *From: ArtOfficial*

- **frame_window_size**: Equal to total frames when using context options
  - Proper context handling for longer videos
  - *From: DawnII*

- **context_frames**: 77
  - Standard context frame size for wan animate
  - *From: xiver2114*

- **fal pricing**: 50 cents per video
  - Indicates compute requirements
  - *From: VK (5080 128gb)*

- **Fast testing parameters**: 3 steps
  - Can produce good results quickly for testing
  - *From: hicho*

- **Frame overlap for VACE**: 10 frames or n/4+1
  - Better transitions in long form video
  - *From: JohnDopamine*

- **Frame generation**: 209 frames in 3 windows at 1280x720 with 6 steps
  - For extended sequences
  - *From: Kijai*

- **Frame rate**: 12fps instead of 24fps
  - Better results for pose-driven content
  - *From: Kijai*

- **Wan 2.1 video training VRAM**: RTX Pro 6000 recommended
  - Frequently spikes up to 89/92 GB when training with 5s 16fps video
  - *From: fearnworks*

- **Steps for quality without LoRA**: 40-60 steps
  - Quality gain can be quite insane on 2.1
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Steps with distill LoRA**: 20-25 steps
  - Usually 20 is enough, 25 if you can for better quality
  - *From: Tonon*

- **Wan generation resolution**: 1536x864 or 1280x720
  - Higher resolution helps with texture swimming issues
  - *From: Neex*

- **TaylorSeer first_enhance**: 5
  - For optimal performance with delayed start
  - *From: Zuko*

- **Max frames for Wan models**: 81 frames
  - Models don't behave well above this limit
  - *From: seitanism*

- **ComfyUI --fast flag**: avoid or use specific optimizations
  - Causes encoding issues, use --fast fp16_accumulation instead
  - *From: Kijai*

- **WanVideoWrapper load device**: offload_device
  - Avoid VRAM issues with newer versions
  - *From: Kijai*

- **Qwen Image steps**: 25 steps (with 8step lora available)
  - Good quality balance
  - *From: Drommer-Kille*

- **Training resolution**: 512 resolution with automatic ratio picking
  - Better performance and compatibility
  - *From: crinklypaper*

- **Blockswap setting**: Set to max and work backwards
  - Avoid OOM errors during training
  - *From: crinklypaper*

- **VACE Fun 2.2**: 8-steps
  - Achieved excellent results with good motion following
  - *From: Izaan*

- **WanAnimate frame windows**: 77 frames
  - Successfully processes 121 frame videos
  - *From: A.I.Warper*

- **Protobuf version**: 5.29.4
  - Fixes compatibility issues after AudioCraft install
  - *From: Gleb Tretyak*

- **Lightning LoRA scheduler**: Euler scheduler, 4 steps, shift=5, cfg=1
  - Official recommended settings from lightx2v team
  - *From: aipmaster*

- **Custom timesteps for flowmatch_distill equivalent**: 999.7998, 937.5000, 833.3333, 625.0000 or 0.999, 0.937, 0.833, 0.625
  - Better results than regular Euler scheduler
  - *From: Kijai*

- **Lightning LoRA step distribution**: Total 4 steps split in middle (2 high + 2 low)
  - Proper way to use 4-step Lightning LoRA
  - *From: Kijai*

- **Alternative step count for new Lightning**: 5 steps total
  - 4 steps not enough, 6 seems overcooked
  - *From: Draken*

- **Dyno model precision**: bf16
  - According to official ComfyUI example
  - *From: Kijai*

- **Lightning lora strength**: 1.0-1.2
  - Testing different strengths with fp8/fp16
  - *From: Kijai*

- **Rank for proper extraction**: 512
  - At rank 512 starts to match motion of full model
  - *From: Kijai*

- **lightx2v strength**: 1.0
  - Reduces red face issues when removing relight lora
  - *From: mdkb*

- **dyno model steps**: 4 steps total - 2 high, 2 low
  - Distilled model configuration with low noise using lora
  - *From: Ansel*

- **expand value for SAM2**: 2 instead of 10
  - Better targeting when using Sam 2.1 heira large model
  - *From: mdkb*

- **frame_window_size for context**: Equal to num_frames
  - Disables looping when using context options
  - *From: Kijai*

- **uni3c strength with 2.2**: 3.0
  - Higher strength needed for camera control to work with 2.2 models
  - *From: Kijai*

- **Frame window size**: Equal to or larger than num_frames
  - Disables looping when equal or larger
  - *From: Kijai*

- **WanAnimate embed frames**: 121 instead of 77
  - Solves context options compatibility error
  - *From: mdkb*

- **Context window size**: 81 preferred over 77
  - Better performance when not using looping
  - *From: Kijai*

- **Uni3C strength for 2.2**: 0.8 to 1.5 on high model
  - Optimal range for Wan 2.2, higher strengths show poor effect
  - *From: Instability01*

- **Uni3C with 2.1**: Strength 4.0 on high noise only
  - Works well for camera animation from Blender
  - *From: xwsswww*

- **WanAnimate steps**: 30 steps, cfg 3, shift 5
  - Used in working examples
  - *From: Gleb Tretyak*

- **Rotation video frame rate**: 10 fps in video loader node for 77 frame generation
  - the bust only did like a 270 degree rotation within 81 frames at 16 fps. I think I set it to like 10 fps in the video loader node and did a 77 frame generation, because then there was a full rotation
  - *From: Instability01*

- **Mouth scale and emo scale for face detector**: 0.01
  - results in less exaggerated lip sync when using fantasy portrait model with infinite talk
  - *From: Dorksense*

- **Mask expand**: 14
  - Used in working inpainting workflow
  - *From: SonidosEnArmonía*

- **Low sampler steps**: start 0, end 5, total 5
  - For inpainting when motion already exists in mask
  - *From: SonidosEnArmonía*


## Concepts Explained

- **PUSA**: 菩萨 (Thousand-Hand Guanyin) - uses many timestep variables to achieve numerous video generation capabilities, adds I2V features to T2V models
  - *From: pagan*

- **noise_multipliers**: Controls timestep scaling and input image noise level, 0.2 is used in PUSA implementation
  - *From: ˗ˏˋ⚡ˎˊ-*

- **cond_position**: Where to insert reference frames, can be multiple positions from 0 to 20
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Pusa LoRA purpose**: Allows T2V model to do I2V - you don't need to remember to switch models
  - *From: Mu5hr00m_oO*

- **LoRA resizing**: Process to reduce LoRA file size while retaining most effectiveness, using dynamic averaging
  - *From: Kijai*

- **Frame windows in long generation**: Each window processes frame_window_size minus motion_frame worth of new frames with overlap
  - *From: Kijai*

- **Disk cache benefit**: Saves memory and speeds up repeated use of same prompts, especially useful when restarting frequently
  - *From: Kijai*

- **Pusa**: High-rank LoRA (4GB) that acts as functional model, integrates LightX2V for faster inference without slow motion
  - *From: JohnDopamine*

- **Latent trimming vs merging**: Merging latents is really concatenation, proper blending requires trimming to avoid jumpy transitions
  - *From: dipstik*

- **Context windows in WAN**: Method to split generation into overlapping windows, blends results at each step. Allows generating more frames by keeping model seeing only ~81 frames. Not an extension method - generates whole video in one go
  - *From: Kijai*

- **LoRA rank and size relationship**: LoRA can be up to original model size - it's a matrix telling model how to change weights. Bigger tasks need more matrix. Pusa is rank 512 hence 4.7GB size
  - *From: Juampab12*

- **Lazy loading with safetensors**: Keeps state_dict weights as references on meta device, only moves to appropriate device during sampling, saves RAM
  - *From: Kijai*

- **Context window prompting**: Use | separator for different prompts per window, if runs out of prompts keeps using last one
  - *From: Kijai*

- **Block swap**: System for managing model loading based on VRAM availability
  - *From: Kijai*

- **Pusa vector timesteps**: Instead of one global timestep controlling noise across entire video, uses vector of timesteps—one for each frame, allowing independent frame evolution
  - *From: Dever*

- **Context window stride**: Stride enabled on high noise can help blending but causes jittery effect
  - *From: Kijai*

- **Block swapping**: Method to save VRAM by loading model blocks sequentially rather than all at once
  - *From: Kijai*

- **Context windows**: Temporal tiling technique from AnimateDiff, not extension - like tiled sampler does an image but in frame dimension
  - *From: Kijai*

- **Block swap**: Memory management technique to handle large models by swapping model blocks in and out of VRAM
  - *From: Kijai*

- **TAESD**: Tiny AutoEncoder for preview that provides much higher quality previews than latent2rgb
  - *From: Kijai*

- **Pusa noise multipliers**: You provide multipliers per extra latent you add, not for the whole video list. For example, 13 start frames + 1 end frame requires 5 multipliers given in injection order
  - *From: Kijai*

- **Wan latent structure**: First frame is 1 latent, then 4 frames per latent after that. So 4xN + 1 frames total structure
  - *From: mamad8*

- **Context window prompt structure**: Use | to separate prompts for different context windows. Number of prompts should match number of context windows (e.g., 337 frames = 4 prompts separated by 3 |)
  - *From: mamad8*

- **Context windows calculation**: ceil(frame_count/(frame_window_size - motion_frame)). For 81 frame window, 600 frames at 16fps, motion_frame of 9: ceil(600/(81-9)) = 9 context windows
  - *From: queeg501*

- **InfiniteTalk multi-character masking**: Static masks that map where each audio can affect the video. If you give audio_1 and audio_2, mask input needs batch of 2 masks
  - *From: Kijai*

- **Fun Control embed strength**: Can multiply the latent strength to adjust control weight, similar to ControlNet weight control
  - *From: Kijai*

- **Speaker diarization**: Process of splitting audio track into separate speakers using speech-to-text with SRT timecodes
  - *From: samhodge*

- **Context window limit**: Maximum frame length before video generation starts looping or degrading
  - *From: jeffcookio*

- **Pusa noise balancing**: Technique of balancing new noise addition for continuity vs accuracy in video extension
  - *From: Kijai*

- **Block swapping**: X amount of blocks on GPU, rest on CPU, moves next block from CPU to GPU during processing, then back to CPU. Native offloading is more precise, working by parameters rather than whole blocks
  - *From: Kijai*

- **SEGS with VACE**: Tools for detailing, inpainting, replacing that can work with video models, biggest challenge is seamless integration with non-traditional controlnets like VACE
  - *From: Ablejones*

- **4 frames per 1 latent**: Temporal relationship in Wan 2.2 affecting slowmotion behavior
  - *From: Kenk*

- **VAE latent packing**: VAE spreads data to 16 channels, doesn't directly correspond to frames as it's temporal/spatial
  - *From: Kijai*

- **Merge loras behavior**: All loras added together additively, but merge option only obeys last one's setting
  - *From: Kijai*

- **Empty embed for silence**: Pre-encoded silence that can be loaded as .pt file for padding audio
  - *From: Kijai*

- **High/Low Noise Preview**: High Noise Preview can be used to quickly check generation before Low Noise sampling is done
  - *From: BobbyD4AI*

- **LoRA merging**: Merge_lora option is meant for non-gguf models to merge loras before use, likely for memory optimization
  - *From: mdkb*

- **Flowmatch_pusa scheduler**: Uses more VRAM than normal schedulers because it activates per-frame timesteps functionality
  - *From: Kijai*

- **HPS vs MPS**: HPS improves prompt adherence, MPS improves general quality
  - *From: Kijai*

- **High vs Low shift in Wan 2.2**: Higher shift handles composition/prompt adherence, lower shift emphasizes finer detail and realism
  - *From: MysteryShack*

- **Frame window size**: InfiniteTalk only decodes the frame_window_size at once, not the whole batch
  - *From: Kijai*

- **Boundary parameter**: Corresponds to timesteps/sigmas that determine when MoE model switches from high noise to low noise expert
  - *From: A.I.Warper*

- **Spatial vs Full Frame inpainting**: Spatial inpaint uses masks like image editing, full frame inpaint replaces entire frames (like interpolation)
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Fun_or_fl2v_model switch**: Setting that changes how last frame is encoded, necessary for models trained to handle end frames differently
  - *From: Kijai*

- **VACE 2.2 high noise model**: What users specifically want - VACE that works with the A14B 2.2 high noise model, as current VACE works with low noise
  - *From: Kijai*

- **HPS LoRA behavior**: HPS wants to draw/add details, can redraw faces and add artifacts especially on fur and feathers
  - *From: N0NSens*

- **Uni3C with T2V**: Works by padding with zeros to handle shape mismatches between control input and generation
  - *From: Kijai*

- **vace_scale**: Parameter required when using VACE that causes KeyError if VACE model isn't properly loaded
  - *From: Dream Making*

- **Differential diffusion**: Feature that can make output worse, can be disabled by setting noise mask feather to 0
  - *From: Dita*

- **Radial attention**: Attention mechanism that benefits on large input sequences, considering both frame length and resolution as dimensions
  - *From: Kijai*

- **3-2 pulldown**: Frame conversion technique where you take 16fps, frame interpolate x3, then remove every other frame to achieve 24fps for syncing
  - *From: nacho.money*

- **HuMo structure**: Uses I2V structure unlike Phantom - refs go in I2V channel as last frames instead of noise latent
  - *From: Kijai*

- **Zero VAE latents**: Pre-encoded empty latents that lock you to specific latent resolution, used in HuMo
  - *From: Kijai*

- **Temporally packed latent space**: Latent space where first latent is single image encoded alone, subsequent latents contain 4 images each, making direct latent cutting impossible
  - *From: Kijai*

- **Fun team**: Side team from Alibaba that creates models for more flexibility - first Fun model was for cog-videox to add multi-resolution support
  - *From: Kijai*

- **VACE input masking**: Can mark specific frames in VACE input with mask to keep them as guidance while leaving other frames for control images
  - *From: Kijai*

- **Fun VACE**: VACE 2.2 created by Fun team at Alibaba, not related to Fun Control or InP models
  - *From: Kijai*

- **VACE modules**: VACE blocks separated from full model, used with T2V model to create complete VACE functionality
  - *From: Kijai*

- **High/Low noise expert split**: VACE 2.2 can work on both high and low noise sides, expanding from 2.1's low-noise-only capability
  - *From: Kijai*

- **Context windows in HuMo**: Allows longer generations but creates drastic shifts between segments due to high freedom
  - *From: Kijai*

- **Parallel attention monkeypatch**: HuMo uses parallel attention that modifies normal attention, cross attention, and model forward functions
  - *From: Kijai*

- **VACE masking**: Masks in VACE indicate start/end frames or areas that shouldn't be edited during generation
  - *From: Piblarg*

- **Context windows**: Technique that allows generating longer videos by processing in overlapping segments
  - *From: Kijai*

- **I2V channel masking**: Using fully black pixels and mask in I2V channel to achieve T2V functionality
  - *From: Kijai*

- **HuMo reference encoding**: I2V input is encoded as black frames + references at the end
  - *From: Kijai*

- **Latents**: The encoded representations that get decoded into images - can be saved and loaded separately to manage memory
  - *From: VK (5080 128gb)*

- **Extra model input**: Generic input in VACE nodes that can accept any model type, replacing specific model inputs
  - *From: mdkb*

- **Pusa scheduler vs regular Pusa LoRA**: When using flowmatch_pusa scheduler, higher Pusa LoRA weight = higher adherence to input but less motion allowed. Without the specific scheduler, it just affects weights
  - *From: Kijai*

- **Uni3c vs Unianimate**: Uni3c is more about camera movement, Unianimate is more about people movement
  - *From: mdkb*

- **Stand-in LoRA architecture**: Special LoRAs that add new layers to models rather than just modifying weights, must be added to model loader
  - *From: Kijai*

- **Block swap**: Memory management technique that works with any precision but requires significant RAM with fp16
  - *From: Kijai*

- **VACE reference vs control**: Reference is single frame for subject, control accepts videos for guidance
  - *From: Dream Making*

- **High/Low noise expert split**: MoE architecture in Wan 2.2 that separates processing for different noise levels
  - *From: context*

- **Allocation on device error**: Refers to VRAM out of memory, not system RAM
  - *From: Kijai*

- **Context schedule metrics**: Context options uses latent as metric - 4 frames = 1 latent, so 21 frames means 105-126 actual frames
  - *From: xwsswww*

- **Pusa scheduler purpose**: Pusa should be considered as its own model, only meant for I2V with T2V model or extension work
  - *From: Kijai*

- **Sigma curve modification**: Shift modifies the sigma curve, which can be visualized using the scheduler node
  - *From: Kijai*

- **Unmerged Loras**: System never loads anything when using unmerged Loras, just applies them on the fly, allowing for per-step strength control
  - *From: Kijai*

- **Context windows with I2V**: Method splits the steps into substeps that do the whole video in windows, it's not an extension technique
  - *From: Kijai*

- **Flux face**: Same face unnatural look and possibly butt chin that can be caused by enhancer loras
  - *From: VRGameDevGirl84(RTX 5090)*

- **Sigma in denoising**: Input used during denoising step, higher sigma makes model treat image as more noisy and apply bigger adjustments
  - *From: 42hub*

- **Shift parameter**: Makes sigmas output bulge up in WanVideoScheduler chart, affects noise scheduling
  - *From: 42hub*

- **Torch.compile dynamic modes**: True=always dynamic, False=never dynamic, None=dynamic only when needed (most efficient)
  - *From: Kijai*

- **Frame window in video generation**: The amount of frames processed by the model at once, not batch processing but frame dimension processing in windows. Different from context windows
  - *From: Kijai*

- **Video DiT frame count sensitivity**: Video DITs hate when frame counts change - model learns different things at different frame counts, would need different RoPE formula to handle variable counts
  - *From: mallardgazellegoosewildcat*

- **InfiniteTalk extension method**: Not context-based, just continues from last frame using I2V loop
  - *From: Kijai*

- **Block swapping**: Memory management technique that swaps model blocks between GPU and CPU, with debug logs showing transfer times
  - *From: Kijai*

- **ClownSampler substeps**: Runs a second sampler every step - if main has 5 steps and substep has 5, you get 25 total substeps per step, making it 2500% slower than euler but following model closer
  - *From: mallardgazellegoosewildcat*

- **Noise types in ClownSampler**: Violet noise for details, brown noise for layout, pyramid for balance, uniform makes image more complex, simplex puts weird grid
  - *From: mallardgazellegoosewildcat*

- **HPS 2.1**: Reward LoRA that can improve quality but may cause unwanted anime-style appearance
  - *From: Gleb Tretyak*

- **Gaussian Splats vs NeRFs**: Splats are thousands of times faster (RTX 3060 for city scale vs 32 H100s for NeRFs) but not differentiable like NeRFs
  - *From: mallardgazellegoosewildcat*

- **Face Control in Wan-animate**: Uses raw facial image as driving input instead of facial landmarks, spatially compresses facial image into 1D latent to reduce identity-specific information
  - *From: DawnII*

- **Relighting LoRA**: Auxiliary LoRA to enhance environmental integration during character replacement, might be game changer
  - *From: slmonker(5090D 32GB)*

- **Limb delta**: The encoder takes into account limb delta between the reference and subject
  - *From: DawnII*

- **Pose reprojection**: Feature not implemented in ComfyUI version, needed for direct comparison to official demos with very different proportions
  - *From: Kijai*

- **Reference frame inclusion**: Reference is included during processing and later cut, similar to VACE workflow
  - *From: Kijai*

- **4+1 frame rule**: Wan-specific frame count requirement that must be followed for proper windowing and to avoid tensor size errors
  - *From: Kijai*

- **Window size constant**: Wan uses fixed 77-frame windows in sequence (77+77+77), cannot process partial windows
  - *From: Kijai*

- **Non-blocking block swap**: Increases RAM usage (not VRAM) but provides faster performance
  - *From: Kijai*

- **Frame window**: Controls how many frames are processed together - must match total frames for short clips to work
  - *From: Kijai*

- **Points Editor**: Red 0 is background (negative), green 0 is face (positive), 1 for body if you want body
  - *From: 𝕯𝖗. 𝕸𝖆𝖈𝖆𝖇𝖗𝖊 ☠*

- **Context windows**: Better alternative to frame_window for control
  - *From: Nao48*

- **Block swap**: Memory optimization technique that reduces VRAM usage with minimal latency impact
  - *From: Kijai*

- **Window size padding**: Model rounds to nearest multiple of window size (like 77 frames), generating extra frames that need to be trimmed
  - *From: Clément*

- **Face pixels uncond**: In WanAnimate code, face pixels are set to -1 for unconditional generation
  - *From: Kijai*

- **CFG disabled model**: WanAnimate might be a CFG disabled model since they don't use CFG in defaults
  - *From: Kijai*

- **CFG distillation**: Can improve final quality of things, found in animatediff/lcm
  - *From: Piblarg*

- **Sunk cost fallacy**: Don't continue investing in something just because you've already invested
  - *From: Juampab12*

- **Frame window size**: In wrapper needs to be set to same number as frame count to avoid extra frames
  - *From: Kijai*

- **High/Low noise expert split**: MoE architecture where high steps create particles that low noise model turns into things like bits of paper
  - *From: Instability01*

- **Sigma schedule**: Tells you how much noise your current state has during generation, affects when high/low noise models hand off work
  - *From: Instability01*

- **Text embed caching**: Saves encoded text embeddings to disk with filename as hash of prompt, prevents re-encoding same prompts
  - *From: Kijai*

- **50% SNR split**: Important timing for when to split steps in Wan 2.2, different from Wan 2.1 step counting
  - *From: DawnII*

- **Block swap**: Memory management technique that allows running larger models by swapping data between VRAM and RAM
  - *From: multiple users*

- **CFG burning**: Artifacts that occur in character replacement scenarios, less common in pose-driven videos
  - *From: slmonker(5090D 32GB)*

- **FFLF**: First-Frame-Last-Frame morphing technique for video generation
  - *From: mdkb*

- **Replace vs Animate mode**: Replace mode does character replacement, animate mode does motion transfer to your image without replacement
  - *From: VLRevolution*

- **Context windows**: Allows processing longer videos by dividing into chunks, but not available in native WanAnimate
  - *From: ArtOfficial*

- **Pose retargeting**: Feature for adapting poses to different character scales (like chibi), currently missing from implementation
  - *From: Kijai*

- **VAE**: Variational autoencoder - encodes images to latent space
  - *From: Kijai*

- **Block swap**: Memory management technique that doesn't affect quality, only memory/speed
  - *From: Kijai*

- **Color matching**: Feature to maintain color consistency between video frames
  - *From: Kijai*

- **Frame Window Size**: Number of frames processed at once, can be less than total frame count to reduce VRAM usage
  - *From: Kijai*

- **Pose retargeting**: Rescaling skeleton limb by limb based on T-pose differences between characters
  - *From: Instability01*

- **VAE tiling**: Technique to reduce VRAM usage during VAE encoding/decoding
  - *From: Kijai*

- **replacement mode pose**: Feature in WanAnimatePreprocess for retargeting poses, still unfinished
  - *From: Kijai*

- **Q-former adapter**: Component in Lynx model that works with VAE encoder for face processing
  - *From: mallardgazellegoosewildcat*

- **Context overlap**: Number of frames shared between each context window for smooth transitions, cannot exceed context frame count
  - *From: xiver2114*

- **PUSA training method**: Point was never to be SOTA but to demonstrate a low-cost training method for extensions
  - *From: DawnII*

- **Stride in context windows**: Spread out overlap method, works poorly with Wan due to latent structure having 4 images per latent
  - *From: Kijai*

- **Retarget_image**: Target to scale the bones to, previously called reference image, should not be used by default if you don't want to retarget
  - *From: Kijai*

- **EMA model**: Exponential Moving Average model - some .pt models contain both generator and generator_ema, with ema usually being better
  - *From: Kijai*

- **Double pass**: Inference code does two passes but with 1 model, double pass = 2.2 otherwise 2.1
  - *From: Juampab12*

- **Joint probability distribution for audio/video**: Unified probability measure space to train diffusion model over both video and audio modalities
  - *From: mallardgazellegoosewildcat*

- **Blockify mask**: Makes even single pixel into a block, can cause interference in tracking
  - *From: Kijai*

- **Shift in rectified flow models**: Borrows steps from detail refinement to give to layout/motion generation at high resolutions
  - *From: mallardgazellegoosewildcat*

- **Flux Kontext**: Preprocessing step that aligns reference image with first video frame, works like image editing
  - *From: Kijai*

- **refert_num**: Parameter controlling overlap frames for temporal guidance in video generation
  - *From: Kijai*

- **MoE architecture with High/Low noise expert split**: Wan 2.2 uses mixture of experts with separate experts for different noise levels
  - *From: Context*

- **Color smudging**: During fast motion or any motion there is color smudging that happens, more apparent in anime and when using greenscreen
  - *From: VK (5080 128gb)*

- **Wan 2.5 audio prompting**: Human Voice = 'Dialogue content spoken by character' + Emotion + Intonation + Speech speed + Tone + Accent. Sound Effects = Sound source material + Action + Ambient sound. Background Music = Background scene/setting + Style
  - *From: 🦙rishappi*

- **4n+1 rule**: Frame count rule that needs to be followed for proper video processing
  - *From: DawnII*

- **Native Multimodal Architecture**: Unified framework for both understanding and generation, supporting text, images, video, and audio input/output
  - *From: 🦙rishappi*

- **RLHF**: Reinforcement Learning from Human Feedback - continuously aligns with human preferences, enhancing image quality and video dynamics
  - *From: 🦙rishappi*

- **High and low noise expert training**: For MoE architectures like Wan 2.2, there's debate on how to train both high and low models - some train full timestep, some train both together
  - *From: crinklypaper*

- **Continuously differentiable**: Required for AI work to have gradients - Gaussian Splatting lacks this property
  - *From: mallardgazellegoosewildcat*

- **MoT (Mixture of Transformers)**: Architecture used in Wan 2.5 instead of MoE (Mixture of Experts)
  - *From: 🦙rishappi*

- **Frame padding technique**: Using 5-20 frames of previous clip and padding rest with grey for seamless transitions
  - *From: seitanism*

- **Temporal reference**: Training technique that allows models like WanAnimate and InfiniteTalk to use reference from previous frames for extensions
  - *From: Kijai*

- **VACE extend**: Using the first 10 frames from previous generation as input for the next generation to create longer sequences
  - *From: Daviejg*

- **Speed LoRAs**: LoRAs that allow running at just 4 steps, several available for wan 2.1 family, smaller choice for 2.2 with more issues
  - *From: 42hub*

- **High/Low noise distill**: 2.2 lacks proper distill making it harder to use, need to play with cfg and lora strengths
  - *From: Kijai*

- **VACE gray mask technique**: Using middle RGB gray to define inpainted areas, unclear if required for vace-fun 2.2
  - *From: Neex*

- **Mixture of Transformers (MoT)**: Architecture upgrade in Wan 2.5, evolution from MoE architecture in 2.2
  - *From: 🦙rishappi*

- **TaylorSeer-Lite**: Caching mechanism that provides lossless speedup, benefits higher step counts but won't stack with low step distillation
  - *From: mallardgazellegoosewildcat*

- **Block swap**: More granular offloading that works asynchronously with video models during long operations
  - *From: Kijai*

- **Addon modules**: Additional layers added on top of existing model without modifying base weights, unlike LoRAs
  - *From: Kijai*

- **MoE architecture**: Mixture of Experts with High/Low noise expert split in Wan 2.2
  - *From: system*

- **Resampler in Lynx**: Does the encoding, not a full VAE - used for face model path while second path uses VAE dense features
  - *From: Kijai*

- **Reference tokens in Lynx**: Spatial details captured across all layers using frozen copy of base model with noise level 0
  - *From: mallardgazellegoosewildcat*

- **VACE reference processing**: Adds latent to beginning of batch, that's why you see +4 frames to total
  - *From: DawnII*

- **250928 naming convention**: Stands for September 2025 (2509 = September 2025)
  - *From: Abyss*

- **LoRA rank differences**: Low noise LoRA is rank 64, high noise is rank 128 - possibly indicates only high part was retrained
  - *From: Kijai*

- **flowmatch_distill scheduler**: Custom scheduler that works better with Lightning LoRAs than standard Euler, limited to 4 steps max
  - *From: Kijai*

- **Dyno**: Name for latest Lightning model release (previous was 'seko'), not a lora type
  - *From: Kijai*

- **Adaptive lora extraction**: Calculates importance of each layer separately, not just one rank
  - *From: Kijai*

- **Frame window size**: Controls how video is processed in blocks - 77 for short videos, 81 for long videos, or equal to total frames when using context options
  - *From: multiple users*

- **Context windows**: Feature that helps prevent color shifting and quality degradation in longer video generation by managing how frames are processed
  - *From: U̷r̷a̷b̷e̷w̷e̷*

- **Blocky masks**: WanAnimate is specifically trained to work with blocky segmentation masks rather than precise edge detection
  - *From: Kijai*

- **Context windows vs looping**: Context windows encode all frames first (memory intensive), looping only encodes frame window size at once
  - *From: Kijai*

- **Uni3C limitations with 2.2**: Low noise side can't use Uni3C at 3.0 strength, and overall effect is weaker than 2.1
  - *From: Kijai*

- **Alpha channel video generation**: Wan-Alpha generates videos with transparency, like adding RGBA instead of RGB (33% processing increase)
  - *From: mccoxmaul*

- **DC-AE**: A compression technology that achieves up to 14.8× lower inference latency than base models without compromising quality
  - *From: scf*

- **Wan Alpha**: Generates alpha channel for transparency effects, decoded with alpha VAE for background removal or compositing
  - *From: Kijai*

- **Cameo (Sora 2)**: Feature that clones people from video references, takes a video clip as input like a micro-insta-lora
  - *From: Draken*

- **Blockswapping**: Memory management technique requiring CUDA kernel for optimal performance
  - *From: mallardgazellegoosewildcat*

- **Fun VACE**: Kijai extracted the VACE layers, adding them back to T2V models equals full size VACE model
  - *From: Ablejones*


## Resources & Links

- **WAN 2.1 Prompt Guide** (guide)
  - https://www.comfyonline.app/blog/wan2-1-prompt-guide
  - *From: Akumetsu971*

- **Official WAN camera movement documentation** (documentation)
  - https://alidocs.dingtalk.com/i/nodes/EpGBa2Lm8aZxe5myC99MelA2WgN7R35y
  - *From: DennisM*

- **PUSA 2.2 models** (model)
  - https://huggingface.co/RaphaelLiu/Pusa-Wan2.2-V1
  - *From: Zabo*

- **Audio encoder for S2V** (model)
  - https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/tree/main/split_files/audio_encoders
  - *From: yi*

- **Topaz Labs video upscaling** (tool)
  - https://www.topazlabs.com/tools/video-upscale
  - *From: Akumetsu971*

- **PUSA project page** (documentation)
  - https://yaofang-liu.github.io/Pusa_Web/
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Resized Pusa LoRAs** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/blob/main/Pusa/
  - *From: Kijai*

- **Wan 2.2 S2V 14B** (model)
  - https://huggingface.co/Wan-AI/Wan2.2-S2V-14B
  - *From: Monero*

- **RunPod template for Wan 2.2** (tool)
  - https://get.runpod.io/wan-template
  - *From: FL13*

- **ComfyUI Hot Reload fork** (tool)
  - https://github.com/kijai/ComfyUI-HotReloadHack
  - *From: Kijai*

- **Caching node pack** (tool)
  - https://github.com/alastor-666-1933/caching_to_not_waste
  - *From: patientx*

- **VibeVoice Large 7B** (model)
  - https://huggingface.co/microsoft/VibeVoice-Large
  - *From: orabazes*

- **Pusa 2.2 documentation** (model)
  - https://huggingface.co/RaphaelLiu/Pusa-Wan2.2-V1
  - *From: .: Not Really Human :.*

- **ComfyUI flow control demo** (repo)
  - https://github.com/BadCafeCode/execution-inversion-demo-comfyui/blob/main/flow_control.py
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Windows triton cache clearing script** (tool)
  - *From: Ablejones*

- **High Set Reveal LoRA** (lora)
  - https://civitai.com/models/1885597/wan22-i2v-high-set-reveal?modelVersionId=2134314
  - *From: Lodis*

- **Pusa V1 training dataset prompts** (dataset)
  - https://huggingface.co/datasets/RaphaelLiu/PusaV1_training/raw/main/metadata.csv
  - *From: TK_999*

- **FLF workflow for music videos** (workflow)
  - *From: VRGameDevGirl84(RTX 5090)*

- **Kijai's fp8 scaled models** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy_fp8_scaled
  - *From: Kijai*

- **Hidden's ComfyUI fork for packaging workflows** (repo)
  - https://github.com/hiddenswitch/ComfyUI
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Wan2_2-I2V-A14B-HIGH_bf16.safetensors** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/blob/main/Wan2_2-I2V-A14B-HIGH_bf16.safetensors
  - *From: HeadOfOliver*

- **Wan 2.2 I2V Context Window workflow JSON** (workflow)
  - *From: Ashtar*

- **AudioStory** (repo)
  - https://github.com/TencentARC/AudioStory/
  - *From: JohnDopamine*

- **T2V panda context workflow** (workflow)
  - *From: Kijai*

- **WanVideoWrapper multi-image context workflow** (workflow)
  - *From: Dever*

- **3 KSampler motion enhancement workflows** (workflow)
  - https://civitai.com/models/1853617
  - *From: BecauseReasons*

- **Wan 2.2 continuous generation subgraphs** (workflow)
  - https://civitai.com/models/1866565/wan22-continuous-generation-subgraphs
  - *From: mccoxmaul*

- **Wan cinematic prompting guide** (guide)
  - https://alidocs.dingtalk.com/i/nodes/EpGBa2Lm8aZxe5myC99MelA2WgN7R35y
  - *From: Lodis*

- **WanVideoWrapper commit for Pusa I2V** (repo)
  - https://github.com/kijai/ComfyUI-WanVideoWrapper/commit/56e3366c26e610a12e7216f49e745f5a7b4929b4
  - *From: Dever*

- **HunyuanVideo-Foley models** (model)
  - https://huggingface.co/tencent/HunyuanVideo-Foley/tree/main
  - *From: . Not Really Human .*

- **Triton/SageAttention for Blackwell** (repo)
  - https://github.com/woct0rdho
  - *From: Kijai*

- **3 KSampler discussion thread** (discussion)
  - https://huggingface.co/lightx2v/Wan2.2-Lightning/discussions/20
  - *From: BecauseReasons*

- **LightX2V LoRA for I2V** (lora)
  - https://huggingface.co/Kijai/WanVideo_comfy/resolve/main/Lightx2v/lightx2v_I2V_14B_480p_cfg_step_distill_rank64_bf16.safetensors
  - *From: Ashtar*

- **MiniMax Remover** (model)
  - https://huggingface.co/spaces/zibojia/MiniMax-Remover
  - *From: Juampab12*

- **AnimateDiff Context Options documentation** (documentation)
  - https://github.com/Kosinkadink/ComfyUI-AnimateDiff-Evolved/tree/main/documentation/nodes#context-options-and-view-options
  - *From: Mu5hr00m_oO*

- **ComfyUI-wanBlockswap** (repo)
  - https://github.com/orssorbit/ComfyUI-wanBlockswap
  - *From: xwsswww*

- **Kijai's example workflows** (workflow)
  - https://github.com/kijai/ComfyUI-WanVideoWrapper/tree/main/example_workflows
  - *From: JohnDopamine*

- **WanGP alternative UI** (tool)
  - not provided
  - *From: hicho*

- **ComfyUI-VibeVoice nodes** (node)
  - wildminder/ComfyUI-VibeVoice
  - *From: samhodge*

- **InfiniteTalk single model** (model)
  - https://huggingface.co/MeiGen-AI/InfiniteTalk/resolve/main/comfyui/infinitetalk_single.safetensors
  - *From: samhodge*

- **InfiniteTalk multi model** (model)
  - https://huggingface.co/MeiGen-AI/InfiniteTalk/resolve/main/comfyui/infinitetalk_multi.safetensors
  - *From: samhodge*

- **Kijai's InfiniteTalk models** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/tree/main/InfiniteTalk
  - *From: JohnDopamine*

- **InfiniteTalk example workflow** (workflow)
  - https://github.com/kijai/ComfyUI-WanVideoWrapper/blob/main/example_workflows/wanvideo_I2V_InfiniteTalk_example_02.json
  - *From: JohnDopamine*

- **Wan 2.2 Fun Control models fp16** (model)
  - https://huggingface.co/alibaba-pai/Wan2.2-Fun-A14B-Control
  - *From: Juan Gea*

- **ComfyUI GGUF conversion tools** (tool)
  - https://github.com/city96/ComfyUI-GGUF/tree/main/tools
  - *From: Kijai*

- **Cache-DiT optimization** (repo)
  - https://github.com/vipshop/cache-dit
  - *From: hicho*

- **Benji's extension workflow video** (workflow)
  - https://www.youtube.com/watch?v=YZTvL8C_xz4&ab_channel=Benji%E2%80%99sAIPlayground
  - *From: BobbyD4AI*

- **UVR5 (Ultimate Vocal Remover)** (tool)
  - https://github.com/Anjok07/ultimatevocalremovergui
  - *From: Urabere*

- **ComfyUI-UVR5 node** (node)
  - https://github.com/AIFSH/ComfyUI-UVR5
  - *From: Urabere*

- **Music Source Separation Training** (repo)
  - https://github.com/ZFTurbo/Music-Source-Separation-Training
  - *From: Lodis*

- **Whisper WebUI Docker** (tool)
  - https://github.com/jhj0517/Whisper-WebUI
  - *From: samhodge*

- **Triton Windows fix** (fix)
  - https://github.com/woct0rdho/triton-windows/releases/download/v3.0.0-windows.post1/python_3.13.2_include_libs.zip
  - *From: Urabere*

- **InfiniteTalk GGUF models** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy_GGUF/tree/main/InfiniteTalk
  - *From: samhodge*

- **Nano Banana on HuggingFace** (tool)
  - https://huggingface.co/spaces/multimodalart/nano-banana
  - *From: JohnDopamine*

- **Wan prompt generator node** (node)
  - https://github.com/ZB678232321/ComfyUI-wan-prompt-generator
  - *From: hicho*

- **Lightx2v LoRAs** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/tree/main/Lightx2v
  - *From: Lodis*

- **InfiniteTalk models** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/tree/main/InfiniteTalk
  - *From: Dever*

- **CineScale upscaling code** (repo)
  - https://github.com/Eyeline-Labs/CineScale/blob/main/cinescale_t2v1.3b.py
  - *From: Cseti*

- **TiM paper - new generative tech** (research)
  - https://arxiv.org/abs/2509.04394
  - *From: ZeusZeus (RTX 4090)*

- **ERTACache auto rectifying method** (repo)
  - https://github.com/bytedance/ERTACache
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Magic-Wan-Image merged model** (model)
  - https://civitai.com/models/1927692?modelVersionId=2184505
  - *From: patientx*

- **VibeVoice-7B model** (model)
  - https://modelscope.cn/models/microsoft/VibeVoice-7B/files
  - *From: .: Not Really Human :.*

- **WanMoeKSampler experimental node** (node)
  - https://github.com/stduhpf/ComfyUI-WanMoeKSampler
  - *From: Lodis*

- **HunyuanVideo-Foley** (tool)
  - https://github.com/Tencent-Hunyuan/HunyuanVideo-Foley
  - *From: nacho.money*

- **ComfyUI-wanBlockswap** (node)
  - https://github.com/orssorbit/ComfyUI-wanBlockswap
  - *From: hicho*

- **Nathan's Wan 2.1 Knowledge Base** (knowledge base)
  - https://nathanshipley.notion.site/Wan-2-1-Knowledge-Base-1d691e115364814fa9d4e27694e9468f
  - *From: The Shadow (NYC)*

- **Chattable Wan knowledge base** (AI chat interface)
  - https://notebooklm.google.com/notebook/a08901b9-0511-4926-bbf8-3c86a12dc306
  - *From: The Shadow (NYC)*

- **Live Wallpaper Style LoRA** (lora)
  - https://civitai.com/models/1264662/live-wallpaper-style
  - *From: The Shadow (NYC)*

- **Tile SEGS for video fork** (repo)
  - https://github.com/drozbay/ComfyUI-Impact-Pack
  - *From: Ablejones*

- **Chatterbox TTS** (model)
  - https://share.google/IZKasnU5J4LPzoEYB
  - *From: VRGameDevGirl84(RTX 5090)*

- **ComfyUI WanVideoWrapper bug fix** (repo)
  - https://github.com/kijai/ComfyUI-WanVideoWrapper/commit/c538cd4c8a4b4c9314fb82f9907a6f9ba2dd9acd
  - *From: Kijai*

- **Wan prompt generator node** (tool)
  - https://github.com/ZB678232321/ComfyUI-wan-prompt-generator
  - *From: hicho*

- **Kinestasis concept LoRA for Wan 2.2** (lora)
  - https://huggingface.co/Cseti/wan2.2-14B-Kinestasis_concept-lora-v1
  - *From: hicho*

- **Detail Daemon for ComfyUI** (tool)
  - https://github.com/Jonseed/ComfyUI-Detail-Daemon
  - *From: Gateway {Dreaming Computers}*

- **Quick Connections plugin** (tool)
  - https://github.com/niknah/quick-connections
  - *From: cyncratic*

- **LightBulb brightness control** (tool)
  - https://github.com/Tyrrrz/LightBulb
  - *From: phazei*

- **Nathan Shipley searchable documentation** (documentation)
  - *From: mdkb*

- **Qwen 2.5 VL for video analysis** (model)
  - https://ollama.com/library/qwen2.5vl
  - *From: BobbyD4AI*

- **Wan 2.2 Fun Reward LoRAs** (model)
  - https://huggingface.co/alibaba-pai/Wan2.2-Fun-Reward-LoRAs
  - *From: yi*

- **Magix nodes** (repo)
  - https://github.com/XmYx/magix-nodes
  - *From: samhodge*

- **Comfy Latent Nodes** (repo)
  - https://github.com/Velour-Fog/comfy-latent-nodes
  - *From: VK (5080 128gb)*

- **Resized Wan 2.2 Fun Reward LoRAs** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/tree/main/Wan22_FunReward
  - *From: Kijai*

- **Wan 2.2 Fun Reward LoRAs** (model)
  - https://huggingface.co/alibaba-pai/Wan2.2-Fun-Reward-LoRAs
  - *From: Mu5hr00m_oO*

- **Lightning development discussion** (repo)
  - https://huggingface.co/lightx2v/Wan2.2-Lightning/discussions/26
  - *From: crinklypaper*

- **FLUX HPS implementations** (model)
  - https://huggingface.co/CodeGoat24/FLUX.1-dev-PrefGRPO/tree/main
  - *From: yi*

- **Live Wallpaper Style LoRA** (lora)
  - https://civitai.com/models/1264662/live-wallpaper-style
  - *From: The Shadow (NYC)*

- **Lightx2v I2V 14B distilled model** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/blob/main/Lightx2v/lightx2v_I2V_14B_480p_cfg_step_distill_rank64_bf16.safetensors
  - *From: DennisM*

- **UniVerse-1 Base Model** (model)
  - https://huggingface.co/dorni/UniVerse-1-Base/tree/main
  - *From: yi*

- **UniVerse-1 GitHub repo** (repo)
  - https://github.com/Dorniwang/UniVerse-1-code/
  - *From: Kijai*

- **InfiniteTalk workflow** (workflow)
  - workflow shared as PNG
  - *From: VRGameDevGirl84(RTX 5090)*

- **HuMo repository** (repo)
  - https://github.com/Phantom-video/HuMo
  - *From: ZeusZeus (RTX 4090)*

- **Kijai's ComfyUI fork with multitalk** (repo)
  - https://github.com/kijai/ComfyUI/tree/multitalk
  - *From: Kijai*

- **Silent audio repository** (repo)
  - https://github.com/anars/blank-audio
  - *From: Dever*

- **USDU upscaler workflow Reddit post** (workflow)
  - https://www.reddit.com/r/StableDiffusion/comments/1nctdy8/wan_22_ultimate_sd_upscaler_working_on_12gb_32gb/
  - *From: Abx*

- **HuMo models** (model)
  - https://huggingface.co/bytedance-research/HuMo/tree/main
  - *From: yi*

- **Wan22-Lightning i2v models** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/tree/main/Wan22-Lightning
  - *From: hicho*

- **Crinklypaper's LoRAs** (model)
  - https://civitai.com/user/tazmannner379
  - *From: crinklypaper*

- **Wan 2.2 tile controlnet** (model)
  - https://huggingface.co/TheDenk/wan2.2-ti2v-5b-controlnet-tile-v1
  - *From: Hevi*

- **Whisper-large-v3 model** (model)
  - https://huggingface.co/openai/whisper-large-v3/blob/main/model.safetensors
  - *From: Kijai*

- **HuMo weights** (model)
  - https://huggingface.co/bytedance-research/HuMo/tree/main
  - *From: ZeusZeus (RTX 4090)*

- **HuMo project page** (documentation)
  - https://phantom-video.github.io/HuMo/
  - *From: SonidosEnArmonía*

- **VACE knowledge base** (documentation)
  - https://nathanshipley.notion.site/Wan-2-1-Knowledge-Base-1d691e115364814fa9d4e27694e9468f#1d691e11536481f380e4cbf7fa105c05
  - *From: mdkb*

- **VACE tutorial video** (tutorial)
  - https://www.youtube.com/watch?v=ZE9kxEut7lo
  - *From: mdkb*

- **Kijai HuMo branch** (repo)
  - https://github.com/kijai/ComfyUI-WanVideoWrapper/tree/humo
  - *From: Ablejones*

- **Wan2.2-VACE-Fun-A14B original model** (model)
  - https://huggingface.co/alibaba-pai/Wan2.2-VACE-Fun-A14B
  - *From: JohnDopamine*

- **Kijai Fun VACE modules bf16** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/blob/main/Fun/VACE/Wan2_2_Fun_VACE_module_A14B_HIGH_bf16.safetensors
  - *From: Kijai*

- **Kijai Fun VACE fp8 e4m3fn modules** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy_fp8_scaled/blob/main/VACE/
  - *From: Kijai*

- **Kijai Fun VACE fp8 e5m2 modules** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy_fp8_scaled/blob/main/VACE/
  - *From: Kijai*

- **Kijai Fun VACE GGUF modules** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy_GGUF/blob/main/VACE/
  - *From: Kijai*

- **HuMo GGUF models** (model)
  - https://huggingface.co/VeryAladeen/Wan2_1-HuMo_17B-GGUF
  - *From: DawnII*

- **VACE 2.2 fp8 models** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy_fp8_scaled/tree/main/VACE
  - *From: Dever*

- **VACE 2.2 modules** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/tree/main/Fun/VACE
  - *From: Dever*

- **Reward LoRAs** (model)
  - https://www.reddit.com/r/StableDiffusion/comments/1nf05fe/we_open_sourced_the_vace_model_and_reward_loras/
  - *From: Dream Making*

- **HuMo GGUF** (model)
  - https://huggingface.co/Alissonerdx/HuMo-GGUF
  - *From: Alisson Pereira*

- **Wan knowledge base** (resource)
  - https://nathanshipley.notion.site/Wan-2-1-Knowledge-Base-1d691e115364814fa9d4e27694e9468f
  - *From: JohnDopamine*

- **WanVideoWrapper example workflows** (workflow)
  - https://github.com/kijai/ComfyUI-WanVideoWrapper/tree/main/example_workflows
  - *From: JohnDopamine*

- **QuantStack Wan 2.2 GGUF** (model)
  - https://huggingface.co/QuantStack/Wan2.2-T2V-A14B-GGUF
  - *From: xiver2114*

- **Kijai HuMo FP8 scaled** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy_fp8_scaled/tree/main/HuMo
  - *From: Kijai*

- **Optimized Whisper encoder** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/blob/main/HuMo/whisper_large_v3_encoder_fp16.safetensors
  - *From: Kijai*

- **HuMo GGUF Q5KM** (model)
  - https://huggingface.co/VeryAladeen/Wan2_1-HuMo_17B-GGUF/tree/main
  - *From: U̷r̷a̷b̷e̷w̷e̷*

- **Alisson's HuMo GGUF** (model)
  - https://huggingface.co/Alissonerdx/Wan2.1-HuMo-GGUF
  - *From: Alisson Pereira*

- **SageAttention fix** (tool)
  - https://github.com/woct0rdho/SageAttention/releases
  - *From: xiver2114*

- **Rope face swap tool** (tool)
  - https://github.com/Hillobar/Rope
  - *From: drbaph*

- **IndexTTS2 voice cloning** (tool)
  - https://github.com/snicolast/ComfyUI-IndexTTS2
  - *From: U̷r̷a̷b̷e̷w̷e̷*

- **Audio samples website** (resource)
  - https://www.myinstants.com/en/categories/television/
  - *From: Alisson Pereira*

- **Movie sounds sites** (resource)
  - https://movie-sounds.org/ and https://clip.cafe/
  - *From: U̷r̷a̷b̷e̷w̷e̷*

- **VACE 2.2 Fun model** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/tree/main/Fun/VACE
  - *From: The Shadow (NYC)*

- **HuMo GGUF models** (model)
  - https://huggingface.co/VeryAladeen/Wan2_1-HuMo_17B-GGUF/tree/main
  - *From: softboi*

- **HuMo scaled versions** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy_fp8_scaled/tree/main/HuMo
  - *From: ArtOfficial*

- **VACE workflow template** (workflow)
  - Not provided
  - *From: Vérole*

- **Original fp32 models** (model)
  - https://huggingface.co/alibaba-pai/Wan2.2-VACE-Fun-A14B/tree/main
  - *From: ˗ˏˋ⚡ˎˊ-*

- **VACE 2.2 fp8 scaled models** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy_fp8_scaled/tree/main/VACE
  - *From: FL13*

- **Discord conversation about latents and WAN** (resource)
  - https://discord.com/channels/1076117621407223829/1342763350815277067/1414435146937139271
  - *From: VK (5080 128gb)*

- **Wan 2.2 Fun VACE control example workflow** (workflow)
  - https://github.com/kijai/ComfyUI-WanVideoWrapper/blob/main/example_workflows/wanvideo_Fun_2_2_control_example_03.json
  - *From: burgstall*

- **Lipsync workflow with masking** (workflow)
  - https://markdkberry.com/workflows/research/#lipsync
  - *From: mdkb*

- **VACE extend workflows collection** (workflow collection)
  - https://discord.com/channels/1076117621407223829/1386453178240733235
  - *From: JohnDopamine*

- **Triton for Windows** (repo)
  - https://github.com/woct0rdho/triton-windows
  - *From: Kijai*

- **SageAttention for Windows** (repo)
  - https://github.com/woct0rdho/SageAttention
  - *From: Kijai*

- **Audio enhancement Python tool** (tool)
  - https://discord.com/channels/1076117621407223829/1224639978601185280/1417131491091157093
  - *From: U̷r̷a̷b̷e̷w̷e̷*

- **Wan2.2 Combined Models** (model)
  - https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/tree/main/split_files/diffusion_models
  - *From: Kijai*

- **Wan2.2 GGUF Models** (model)
  - https://huggingface.co/QuantStack/Wan2.2-VACE-Fun-A14B-GGUF/tree/main
  - *From: The Shadow (NYC)*

- **Wan2.2 Mega AIO Model** (model)
  - https://huggingface.co/Phr00t/WAN2.2-14B-Rapid-AllInOne
  - *From: Phr00t*

- **Multi-controlnet workflow** (workflow)
  - *From: yo9o*

- **AMD SDPA bug report** (repo)
  - https://github.com/ROCm/TheRock/issues/1315
  - *From: Hoernchen*

- **Waver 1.0 announcement** (model)
  - http://www.waver.video/
  - *From: Tonon*

- **PyTorch 2.9 nightly installation command** (install command)
  - pip3 install -U --pre torch torchvision --index-url https://download.pytorch.org/whl/nightly/cu129
  - *From: Kijai*

- **SageAttention GitHub repo** (repo)
  - https://github.com/woct0rdho/SageAttention
  - *From: Kijai*

- **Triton Windows GitHub repo** (repo)
  - https://github.com/woct0rdho/triton-windows
  - *From: Kijai*

- **HuMo 1.7B model weights** (model)
  - https://huggingface.co/bytedance-research/HuMo/commits/main
  - *From: DawnII*

- **Compiled SageAttention wheel for torch 2.9** (wheel file)
  - https://private-user-images.githubusercontent.com/54047/437063550-ecf01218-77fb-49c7-96bf-55e582111954.png
  - *From: Kijai*

- **HuMo 1.7B fp16 model** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/blob/main/HuMo/Wan2_1-HuMo-1_7B_fp16.safetensors
  - *From: Kijai*

- **Kijai's fp8_scaled models** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy_fp8_scaled
  - *From: Kijai*

- **VRGameDevGirl custom nodes** (repo)
  - https://github.com/vrgamegirl19/comfyui-vrgamedevgirl/tree/main
  - *From: VRGameDevGirl84(RTX 5090)*

- **Endless video workflow analysis** (workflow)
  - https://markdkberry.com/workflows/footprints/
  - *From: mdkb*

- **Infinite Talk workflows** (workflow)
  - https://markdkberry.com/workflows/research/
  - *From: mdkb*

- **LanPaint** (repo)
  - https://github.com/scraed/LanPaint
  - *From: asd*

- **Wan 2.2 VACE User Guide** (guide)
  - https://nathanshipley.notion.site/Guide-VACE-with-Wan-2-2-in-ComfyUI-27191e115364802186aacc04c00d71f3
  - *From: Nathan Shipley*

- **res4lyf node pack** (node pack)
  - *From: Kijai*

- **ComfyUI memory fix commit** (repo)
  - https://github.com/comfyanonymous/ComfyUI/commit/e42682b24ef033a93001ba27cc5c5aa461a61d8d
  - *From: JohnDopamine*

- **HuMO models** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy_fp8_scaled/tree/main/HuMo
  - *From: Kijai*

- **Triton Windows installation** (repo)
  - https://github.com/woct0rdho/triton-windows
  - *From: Kijai*

- **ComfyUI audio nodes PR** (repo)
  - https://github.com/comfyanonymous/ComfyUI/pull/9908
  - *From: 42hub*

- **VACE masking workflow** (workflow)
  - https://www.reddit.com/r/StableDiffusion/comments/1nheba5/wan_22_funvace_masking/
  - *From: chrisd0073*

- **Shift explanation chart** (resource)
  - https://www.reddit.com/media?url=https%3A%2F%2Fpreview.redd.it%2Fwan-2-2-misconception-the-best-high-low-split-is-unknown-v0-npzjhjy70gnf1.png%3Fwidth%3D1318%26auto%3Dwebp%26s%3Dfc12beb669978952365ec2dcafd1310356b3c3be
  - *From: 42hub*

- **1 minute silence audio** (resource)
  - https://bigsoundbank.com/one-minute-of-silence-s0917.html
  - *From: xwsswww*

- **FastWan LoRA rank 128** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/resolve/main/FastWan/FastWan_T2V_14B_480p_lora_rank_128_bf16.safetensors?download=true
  - *From: mdkb*

- **CineScale 4K upscaler** (tool)
  - https://eyeline-labs.github.io/CineScale/
  - *From: Kijai*

- **OCR Chrome Extension** (tool)
  - https://chromewebstore.google.com/detail/ocr-image-reader/bhbhjjkcoghibhibegcmbomkbakkpdbo
  - *From: Quality_Control*

- **WAN 2.2 Mega Merge** (model)
  - https://huggingface.co/Phr00t/WAN2.2-14B-Rapid-AllInOne/tree/main/Mega-v1
  - *From: Alisson Pereira*

- **Wan2.2-Fun-A14B-InP model** (model)
  - https://huggingface.co/alibaba-pai/Wan2.2-Fun-A14B-InP
  - *From: buttercup5108*

- **RES4LYF sampler repository** (repo)
  - https://github.com/ClownsharkBatwing/RES4LYF
  - *From: Ethan*

- **Pexels test video** (resource)
  - https://www.pexels.com/video/a-4x4-vehicle-speeding-on-a-dirt-road-during-a-competition-15604814/
  - *From: Kijai*

- **FFLF workflow with ControlNets** (workflow)
  - mdkb profile research page
  - *From: mdkb*

- **Cosmos Transfer1 7B 4K Upscaler** (model)
  - https://huggingface.co/nvidia/Cosmos-Transfer1-7B-4KUpscaler
  - *From: mallardgazellegoosewildcat*

- **Replicate Wan LoRA Trainer** (tool)
  - https://replicate.com/ostris/wan-lora-trainer/train
  - *From: Ruairi Robinson*

- **Lucy Edit Dev model** (model)
  - https://huggingface.co/decart-ai/Lucy-Edit-Dev
  - *From: hicho*

- **ModelHunter tool** (tool)
  - https://tr1dae.github.io/ModelHunter/
  - *From: Quality_Control*

- **Krita Wan VACE tutorial** (workflow)
  - https://www.reddit.com/r/StableDiffusion/comments/1nkm091/krita_wan_vace_animation_keyframe_inbetweening/
  - *From: xwsswww*

- **Wan 2.2 Animate model** (model)
  - https://huggingface.co/Wan-AI/Wan2.2-Animate-14B
  - *From: slmonker(5090D 32GB)*

- **Wan 2.2 Animate Playground** (demo)
  - https://huggingface.co/spaces/Wan-AI/Wan2.2-Animate
  - *From: slmonker(5090D 32GB)*

- **Wan-animate project page** (documentation)
  - https://humanaigc.github.io/wan-animate/
  - *From: DawnII*

- **Humo workflow** (workflow)
  - https://discord.com/channels/1076117621407223829/1417710283945672764
  - *From: VRGameDevGirl84(RTX 5090)*

- **ComfyUI repackaged model** (model)
  - https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/blob/main/split_files/diffusion_models/wan2.2_animate_14B_bf16.safetensors
  - *From: piscesbody*

- **Wan animate user guide** (documentation)
  - https://github.com/Wan-Video/Wan2.2/blob/a64d5b25af052a24e8e1bc23aa7af3ee130b1d84/wan/modules/animate/preprocess/UserGuider.md
  - *From: Mads Hagbarth Damsbo*

- **RamTorch for memory optimization** (tool)
  - https://github.com/lodestone-rock/RamTorch
  - *From: Blink*

- **Wan 2.2 Animate 14B models** (model)
  - https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/blob/main/split_files/diffusion_models/wan2.2_animate_14B_bf16.safetensors
  - *From: Kijai*

- **Wan 2.2 Animate GGUF Q8_0** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy_GGUF/blob/main/Wan22Animate/Wan2_2_Animate_14B_Q8_0.gguf
  - *From: Kijai*

- **Wan 2.2 Animate FP8 E4M3FN** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy_fp8_scaled/blob/main/Wan22Animate/Wan2_2-Animate-14B_fp8_e4m3fn_scaled_KJ.safetensors
  - *From: Kijai*

- **Wan 2.2 Animate FP8 E5M2** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy_fp8_scaled/blob/main/Wan22Animate/Wan2_2-Animate-14B_fp8_e5m2_scaled_KJ.safetensors
  - *From: Kijai*

- **Original Wan Animate examples** (repo)
  - https://github.com/Wan-Video/Wan2.2/tree/main/examples/wan_animate
  - *From: Kijai*

- **Relighting LoRA** (lora)
  - https://huggingface.co/Wan-AI/Wan2.2-Animate-14B/tree/main/relighting_lora
  - *From: JohnDopamine*

- **Working Relighting LoRA FP16** (lora)
  - https://huggingface.co/Kijai/WanVideo_comfy/blob/main/WanAnimate_relight_lora_fp16.safetensors
  - *From: Kijai*

- **Wan 2.2 Animate 14B model** (model)
  - https://huggingface.co/Wan-AI/Wan2.2-Animate-14B
  - *From: Ada*

- **Wan Animate project page** (documentation)
  - https://humanaigc.github.io/wan-animate/
  - *From: Ada*

- **Reddit best practices collection** (guide)
  - https://www.reddit.com/r/StableDiffusion/comments/1n0n362/collecting_best_practices_for_wan_22_i2v_workflow/
  - *From: pom*

- **Sapiens pose detector** (model)
  - https://huggingface.co/facebook/sapiens-pose-bbox-detector
  - *From: ˗ˏˋ⚡ˎˊ-*

- **ComfyUI Sapiens integration** (node)
  - https://github.com/smthemex/ComfyUI_Sapiens
  - *From: ˗ˏˋ⚡ˎˊ-*

- **WanAnimate example workflow** (workflow)
  - https://github.com/kijai/ComfyUI-WanVideoWrapper/blob/main/example_workflows/wanvideo_WanAnimate_example_01.json
  - *From: DennisM*

- **WanAnimate models** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy_fp8_scaled/tree/main/Wan22Animate
  - *From: Dever*

- **WanAnimate GGUF quantized** (model)
  - https://huggingface.co/wsbagnsv1/Wan2.2-Animate-14B-GGUF
  - *From: The Punisher*

- **CLIP Vision model** (model)
  - https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/blob/main/split_files/clip_vision/clip_vision_h.safetensors
  - *From: Shubhooooo*

- **Native ComfyUI implementation** (workflow)
  - *From: hicho*

- **Point Tracker Custom Node** (tool)
  - https://github.com/tnil25/ComfyUI-TJNodes/tree/master
  - *From: traxxas25*

- **ComfyUI-Gaze** (tool)
  - https://github.com/Malu05/ComfyUI-Gaze/tree/main
  - *From: A.I.Warper*

- **Wan 2.2 Animate GGUF** (model)
  - https://huggingface.co/wsbagnsv1/Wan2.2-Animate-14B-GGUF
  - *From: The Punisher*

- **Self-Forcing model** (model)
  - https://huggingface.co/gdhe17/Self-Forcing/commit/7266b489f4cd3c4ad533611478a0d80cd1d2f1c5
  - *From: DawnII*

- **WanAnimate paper** (paper)
  - https://arxiv.org/pdf/2509.14055
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Lucy Edit ComfyUI** (repo)
  - https://github.com/DecartAI/Lucy-Edit-ComfyUI/tree/main?tab=readme-ov-file
  - *From: ArtOfficial*

- **Kijai's animate workflows** (workflow)
  - https://github.com/kijai/ComfyUI-WanVideoWrapper/tree/main/example_workflows
  - *From: Shubhooooo*

- **ComfyUI-Florence2** (repo)
  - https://github.com/kijai/ComfyUI-Florence2
  - *From: JohnDopamine*

- **Radial Length Helper node** (tool)
  - https://github.com/Hud224/Radial_Length_Helper/tree/main
  - *From: hudson223*

- **Moondream3 discussion** (model)
  - https://huggingface.co/moondream/moondream3-preview/discussions/1
  - *From: JohnDopamine*

- **NAG sampler documentation** (repo)
  - https://github.com/ChenDarYen/ComfyUI-NAG?tab=readme-ov-file#key-inputs
  - *From: hudson223*

- **Rally car drifting test video** (video)
  - https://www.pexels.com/video/a-4x4-vehicle-speeding-on-a-dirt-road-during-a-competition-15604814/
  - *From: Kijai*

- **Animation frame rate conversion workflow** (workflow)
  - https://www.reddit.com/r/StableDiffusion/comments/1nhhe1j/convert_animation_to_on_threes_subject_only/
  - *From: hudson223*

- **WanVaceAdvanced workflows** (repo)
  - https://github.com/drozbay/ComfyUI-WanVaceAdvanced
  - *From: xwsswww*

- **Phantom workflow examples** (workflow)
  - https://discord.com/channels/1076117621407223829/1403263501421776977
  - *From: xwsswww*

- **Modified Qwen2.5VL object detection** (repo)
  - https://github.com/piscesbody/Comfyui_Object_Detect_QWen_VL.git
  - *From: piscesbody*

- **WanAnimate relight LoRA** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/blob/main/WanAnimate_relight_lora_fp16.safetensors
  - *From: TK_999*

- **Modified Wan2.2 repo with RAM torch support** (repo)
  - https://github.com/maybleMyers/Wan2.2
  - *From: Benjimon*

- **AutoFrameWindowCalculator custom node** (node)
  - https://github.com/eddyhhlure1Eddy/auto_wan2.2animate_freamtowindow_server
  - *From: slmonker(5090D 32GB)*

- **FaceAnalysis node pack** (node)
  - https://github.com/cubiq/ComfyUI_FaceAnalysis
  - *From: piscesbody*

- **Native WanAnimate workflow** (workflow)
  - https://discord.com/channels/1076117621407223829/1342763350815277067/1418876590955429909
  - *From: Tony(5090)*

- **Sobol sequence for quasi monte carlo seeding** (reference)
  - https://en.m.wikipedia.org/wiki/Sobol_sequence
  - *From: mallardgazellegoosewildcat*

- **Color-matcher library** (repo)
  - https://github.com/hahnec/color-matcher
  - *From: Kijai*

- **Wan2GP for GPU-poor users** (repo)
  - https://github.com/deepbeepmeep/Wan2GP
  - *From: JohnDopamine*

- **Qwen models for prompt enhancement** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/tree/main/Qwen
  - *From: Kijai*

- **WanAnimatePreprocess** (repo)
  - https://github.com/kijai/ComfyUI-WanAnimatePreprocess
  - *From: Kijai*

- **Wan2.2-Animate-14B-GGUF** (workflow)
  - https://huggingface.co/QuantStack/Wan2.2-Animate-14B-GGUF/blob/main/example_workflow/wan%20animate%20native.json
  - *From: buttercup5108*

- **Wan2.2-Animate-14B** (model)
  - https://huggingface.co/Wan-AI/Wan2.2-Animate-14B
  - *From: Shubhooooo*

- **ComfyUI_pose_inter** (tool)
  - https://github.com/toyxyz/ComfyUI_pose_inter
  - *From: ˗ˏˋ⚡ˎˊ-*

- **ComfyUI-UniAnimate-W** (tool)
  - https://github.com/Isi-dev/ComfyUI-UniAnimate-W?tab=readme-ov-file#animate-x
  - *From: ˗ˏˋ⚡ˎˊ-*

- **ComfyUI-FramePackWrapper** (tool)
  - https://github.com/kijai/ComfyUI-FramePackWrapper
  - *From: Léon*

- **Wan platform** (tool)
  - https://wan.video/
  - *From: chrisd0073*

- **Wan fp8 safetensors** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy_fp8_scaled/tree/main/Wan22Animate
  - *From: Shubhooooo*

- **Lynx project page** (project)
  - https://byteaigc.github.io/Lynx/
  - *From: Shubhooooo*

- **Wan 2.2 Animate Workflow for 12GB VRAM** (workflow)
  - https://civitai.com/models/1980698?modelVersionId=2242118
  - *From: harriet_h*

- **Qwen Image Edit 2509** (model)
  - https://huggingface.co/Qwen/Qwen-Image-Edit-2509
  - *From: Dever*

- **Qwen Image Edit 2509 HuggingFace Space** (demo)
  - https://huggingface.co/spaces/Qwen/Qwen-Image-Edit-2509
  - *From: slmonker(5090D 32GB)*

- **Qwen Image Edit 2509 GGUF** (model)
  - https://huggingface.co/QuantStack/Qwen-Image-Edit-2509-GGUF
  - *From: buttercup5108*

- **OmniInsert project** (project)
  - https://phantom-video.github.io/OmniInsert/
  - *From: JohnDopamine*

- **WanAnimatePreprocess** (repo)
  - https://github.com/kijai/ComfyUI-WanAnimatePreprocess
  - *From: Mak*

- **Wan Animate Preprocess nodes** (repo)
  - https://github.com/kijai/ComfyUI-WanAnimatePreprocess
  - *From: A.I.Warper*

- **FastWan LoRA** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/resolve/main/FastWan/FastWan_T2V_14B_480p_lora_rank_64_bf16.safetensors
  - *From: VRGameDevGirl84(RTX 5090)*

- **Qwen Image Edit 2509 FP8** (model)
  - https://huggingface.co/orabazes/Qwen_Image_Edit_2509_FP8/tree/main
  - *From: Lodis*

- **AnimateDiff Context Options documentation** (documentation)
  - https://github.com/Kosinkadink/ComfyUI-AnimateDiff-Evolved/tree/main/documentation/nodes#context-optionsstandard-uniform
  - *From: Kijai*

- **Wan2GP for low VRAM** (tool)
  - https://github.com/deepbeepmeep/Wan2GP
  - *From: xiver2114*

- **Wan2.2 Animate 14B model** (model)
  - https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/blob/main/split_files/diffusion_models/wan2.2_animate_14B_bf16.safetensors
  - *From: AR*

- **Wan2.2-VACE-Fun-A14B** (model)
  - https://huggingface.co/alibaba-pai/Wan2.2-VACE-Fun-A14B
  - *From: Lodis*

- **OmniInsert by Phantom** (repo)
  - https://github.com/Phantom-video/OmniInsert
  - *From: JohnDopamine*

- **Self-Forcing model update** (model)
  - https://huggingface.co/gdhe17/Self-Forcing/commit/2f8b779212da279d212c22a509b66ad6552f350e
  - *From: DawnII*

- **Wan 2.5 livestream** (livestream)
  - https://x.com/i/broadcasts/1rmGPvwXRkZxN
  - *From: yi*

- **WAN 2.5 on WaveSpeed** (model)
  - https://wavespeed.ai/models/alibaba/wan-2.5/text-to-video
  - *From: yi*

- **RamTorch for WAN** (tool)
  - https://github.com/lodestone-rock/RamTorch/tree/main/ramtorch
  - *From: Benjimon*

- **ComfyUI WAN 2.5 API PR** (repo)
  - https://github.com/comfyanonymous/ComfyUI/pull/9996
  - *From: Juan Gea*

- **Regional Adaptive Sampling** (tool)
  - https://github.com/Slickytail/ComfyUI-RegionalAdaptiveSampling/commit/0ed435ba0b281006d20eccb5eb7172e497cae824
  - *From: JohnDopamine*

- **WanAnimatePreprocess node pack** (repo)
  - https://github.com/kijai/ComfyUI-WanAnimatePreprocess
  - *From: Kijai*

- **VitPose models for ComfyUI** (model)
  - https://huggingface.co/Kijai/vitpose_comfy/tree/main/onnx
  - *From: Kijai*

- **ComfyUI API nodes for Wan** (repo)
  - https://github.com/comfyanonymous/ComfyUI/blob/master/comfy_api_nodes/nodes_wan.py
  - *From: ZeusZeus (RTX 4090)*

- **Wan 2.5 livestream** (livestream)
  - https://www.youtube.com/live/hyRFWDEX_EA?si=mtc7an2dIKtwC0Xz
  - *From: Cseti*

- **Official ComfyUI blog post** (blog)
  - https://blog.comfy.org/p/wan22-animate-and-qwen-image-edit-2509
  - *From: Léon*

- **Wan 2.5 livestream** (livestream)
  - https://www.youtube.com/watch?v=hyRFWDEX_EA
  - *From: Léon*

- **Bilibili livestream** (livestream)
  - https://live.bilibili.com/31811590
  - *From: psilo*

- **Latest KJ workflow** (workflow)
  - https://discord.com/channels/1076117621407223829/1420053619541283000/1420114433287651359
  - *From: justinj*

- **ComfyUI commit** (repo)
  - https://github.com/comfyanonymous/ComfyUI/commit/e8087907995497c6971ee64bd5fa02cb49c1eda6
  - *From: JohnDopamine*

- **Wan 2.5 available on wan.video** (api)
  - wan.video
  - *From: slmonker(5090D 32GB)*

- **Wan2.2 Competition results** (competition)
  - https://tensor.art/blackboard/wan22-campaign?tab=post1
  - *From: AJO*

- **Alibaba Wan Twitter announcement** (announcement)
  - https://x.com/Alibaba_Wan/status/1970697244740591917
  - *From: metahades*

- **Wan 2.5 API testing** (api)
  - https://create.wan.video/generate/video/image-to-video?model=wan2.5
  - *From: Tonon*

- **Alibaba Cloud Wan 2.5 model details** (model)
  - https://bailian.console.alibabacloud.com/?tab=model#/model-market/detail/wan2.5-i2v-preview
  - *From: Lodis*

- **Wan Car Dream video example** (example)
  - https://youtu.be/rHoHqUlqcl4?si=gmDlUMoGa4pxEIve
  - *From: Nekodificador*

- **Chinese livestream** (video)
  - https://www.youtube.com/watch?v=hyRFWDEX_EA
  - *From: Zabo*

- **StepVideo FP8 implementation** (repo)
  - https://github.com/modelscope/DiffSynth-Studio/blob/main/examples/stepvideo/stepvideo_text_to_video_quantized.py
  - *From: mallardgazellegoosewildcat*

- **Wan 2.5 free website** (tool)
  - https://zaodian.quark.cn/
  - *From: kerokero*

- **Wan 2.5 pricing** (tool)
  - https://create.wan.video/pricing?whereToMemberShip=upgrade
  - *From: hicho*

- **OmniInsert by Phantom team** (repo)
  - https://github.com/Phantom-video/OmniInsert
  - *From: JohnDopamine*

- **Lynx project** (repo)
  - https://byteaigc.github.io/Lynx/
  - *From: JohnDopamine*

- **Tom & Jerry long video paper** (research)
  - https://arxiv.org/abs/2504.05298
  - *From: JohnDopamine*

- **Test-time training for video** (research)
  - https://test-time-training.github.io/video-dit/
  - *From: johannezz*

- **ComfyUI-WanAnimatePreprocess** (repo)
  - https://github.com/kijai/ComfyUI-WanAnimatePreprocess
  - *From: Kijai*

- **Wan2.2-I2V-A14B-4steps-lora-rank64-Seko-V1** (model)
  - https://huggingface.co/lightx2v/Wan2.2-Lightning/tree/main/Wan2.2-I2V-A14B-4steps-lora-rank64-Seko-V1
  - *From: hicho*

- **AI Video Leaderboard** (tool)
  - https://artificialanalysis.ai/text-to-video/arena?tab=leaderboard-image
  - *From: Lodis*

- **AI toolkit for Wan 2.2 LoRA training** (tool)
  - *From: fearnworks*

- **Wan2.2-Fun-A14B-Control** (model)
  - https://huggingface.co/alibaba-pai/Wan2.2-Fun-A14B-Control
  - *From: buttercup5108*

- **Wan2.2-Animate-14B-GGUF** (model)
  - https://huggingface.co/QuantStack/Wan2.2-Animate-14B-GGUF/tree/main
  - *From: 32Bit_Badman*

- **Character LoRAs** (model)
  - https://civitai.com/user/tazmannner379
  - *From: crinklypaper*

- **Training channel** (resource)
  - <#1344309523187368046>
  - *From: fearnworks*

- **ComfyUI-TaylorSeer** (node)
  - https://github.com/philipy1219/ComfyUI-TaylorSeer
  - *From: Zuko*

- **MagiAttention kernel** (tool)
  - https://github.com/SandAI-org/MagiAttention
  - *From: mallardgazellegoosewildcat*

- **OmniInsert research** (repo)
  - https://phantom-video.github.io/OmniInsert/
  - *From: hicho*

- **Wan relight LoRA** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/tree/main/LoRAs/Wan22_relight
  - *From: piscesbody*

- **Wan21_PusaV1_LoRA_14B_rank512_bf16.safetensors** (lora)
  - https://huggingface.co/Kijai/WanVideo_comfy/blob/main/Pusa/Wan21_PusaV1_LoRA_14B_rank512_bf16.safetensors
  - *From: mccoxmaul*

- **clip_vision_h.safetensors** (model)
  - https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/blob/main/split_files/clip_vision/clip_vision_h.safetensors
  - *From: Kijai*

- **Lynx model** (model)
  - https://huggingface.co/ByteDance/lynx
  - *From: CMM0000*

- **DJZ-Nodes** (node_pack)
  - https://github.com/MushroomFleet/DJZ-Nodes/tree/main
  - *From: The Shadow (NYC)*

- **ComfyUI_Fill-Nodes** (node_pack)
  - https://github.com/filliptm/ComfyUI_Fill-Nodes?tab=readme-ov-file#image-nodes
  - *From: JohnDopamine*

- **ComfyUI-WarperNodes** (node_pack)
  - https://github.com/AIWarper/ComfyUI-WarperNodes
  - *From: A.I.Warper*

- **Phazei's HunyuanVideo-Foley node** (node)
  - https://github.com/phazei/ComfyUI-HunyuanVideo-Foley
  - *From: theUnlikely*

- **ComfyUI Portrait Master for outfit generation** (node)
  - https://github.com/florestefano1975/comfyui-portrait-master
  - *From: Tachyon*

- **Sparse-VideoGen** (repo)
  - https://github.com/svg-project/Sparse-VideoGen
  - *From: hicho*

- **Searge nodes for local LLM prompting** (node)
  - *From: mccoxmaul*

- **Wan 2.2 Lightning LoRA v2.0 (250928)** (model)
  - https://huggingface.co/lightx2v/Wan2.2-Lightning
  - *From: yi*

- **Kijai's converted Lightning LoRAs with ComfyUI compatible keys** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/blob/main/LoRAs/Wan22-Lightning/
  - *From: Kijai*

- **ByteDance Lynx model** (model)
  - https://huggingface.co/ByteDance/lynx
  - *From: Daflon*

- **Hunyuan Image v3** (model)
  - https://x.com/tencenthunyuan/status/1972126886102004139
  - *From: Siraj*

- **Wan2.2-Lightning dyno full model** (model)
  - https://huggingface.co/lightx2v/Wan2.2-Lightning/tree/main/Wan2.2-T2V-A14B-4steps-250928-dyno
  - *From: JohnDopamine*

- **New Lightning 2509 loras** (lora)
  - https://huggingface.co/lightx2v/Wan2.2-Lightning/tree/main/Wan2.2-T2V-A14B-4steps-lora-250928
  - *From: Kijai*

- **Raylight multi-GPU tool** (tool)
  - https://github.com/komikndr/raylight
  - *From: Faust-SiN*

- **3KSampler node** (node)
  - https://github.com/VraethrDalkr/ComfyUI-TripleKSampler
  - *From: Ansel*

- **Kijai's fp8 scaled dyno model** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy_fp8_scaled/blob/main/T2V/Wan2_2-T2V-A14B-HIGH_4_steps-250928-dyno-lightx2v_fp8_e4m3fn_scaled_KJ.safetensors
  - *From: Kijai*

- **360 degree rotation LoRA for Wan 2.2 i2v** (lora)
  - https://civitai.com/models/1346623/360-degree-rotation-microwave-rotation-wan21-i2v-lora
  - *From: xwsswww*

- **VibeVoice ComfyUI (Enemyx version)** (repo)
  - https://github.com/Enemyx-net/VibeVoice-ComfyUI
  - *From: U̷r̷a̷b̷e̷w̷e̷*

- **VibeVoice ComfyUI (Wildminder version)** (repo)
  - https://github.com/wildminder/ComfyUI-VibeVoice
  - *From: JohnDopamine*

- **LongLive-1.3B model** (model)
  - https://huggingface.co/Efficient-Large-Model/LongLive-1.3B
  - *From: yi*

- **VibeVoice finetuning** (repo)
  - https://github.com/voicepowered-ai/VibeVoice-finetuning
  - *From: MysteryShack*

- **VibeVoice Merge LoRA tool** (tool)
  - https://github.com/Many0therFunctions/VibeVoice-Merge-Lora-To-Checkpoint/
  - *From: MysteryShack*

- **Wan Alpha model** (model)
  - https://github.com/WeChatCV/Wan-Alpha
  - *From: JohnDopamine*

- **Self-Forcing Plus Wan 2.2 support** (repo)
  - https://github.com/GoatWu/Self-Forcing-Plus/tree/wan22
  - *From: yi*

- **AI Toolkit trainer** (tool)
  - https://huggingface.co/spaces/multimodalart/ai-toolkit
  - *From: Drommer-Kille*

- **WanAnimate API on Replicate** (api)
  - https://replicate.com/wan-video/wan-2.2-animate-animation
  - *From: Draken*

- **Wan prompting guide** (guide)
  - https://alidocs.dingtalk.com/i/nodes/EpGBa2Lm8aZxe5myC99MelA2WgN7R35y
  - *From: Abx*

- **Uni3C tutorial video** (tutorial)
  - https://youtu.be/0cw2N3W7nKo?si=KB5Mz-karWuD4sxT&t=740
  - *From: mdkb*

- **Rolling Forcing research** (research)
  - https://kunhao-liu.github.io/Rolling_Forcing_Webpage/
  - *From: yi*

- **DC-VideoGen project** (repo)
  - https://github.com/dc-ai-projects/DC-VideoGen
  - *From: yi*

- **DC-AE examples** (documentation)
  - https://github.com/dc-ai-projects/DC-Gen/blob/main/projects/DC-AE-1.5.md
  - *From: yi*

- **DC Transfer models** (model)
  - https://huggingface.co/guyuchao/DC_Transfer/tree/main
  - *From: yi*

- **LongLive real-time video generation** (repo)
  - https://github.com/NVlabs/LongLive
  - *From: Izaan*

- **ReCamMaster camera trajectory control** (repo)
  - https://github.com/KwaiVGI/ReCamMaster?tab=readme-ov-file#-awesome-related-works
  - *From: AmirKerr*

- **ComfyUI DDD 2D to 3D stereoscopic conversion** (workflow)
  - https://civitai.com/models/1988265/comfyui-ddd-2d-to-3d-stereoscopic-conversion-and-3d-stereoscopic-generation?modelVersionId=2250722
  - *From: Geoff*

- **Kandinsky 5.0 T2V Lite** (model)
  - https://huggingface.co/collections/ai-forever/kandinsky-50-t2v-lite-68d71892d2cc9b02177e5ae5
  - *From: yi*

- **Wan alpha tempo workflow** (workflow)
  - https://github.com/mr-lab/tempo/blob/master/ComfyUI_00031_.webp?raw=true
  - *From: mrassets*

- **Kandinsky 5.0 ComfyUI implementation** (repo)
  - https://github.com/ai-forever/Kandinsky-5/tree/main/comfyui
  - *From: Draken*

- **Kandinsky 5.0 demos** (demo)
  - https://x.com/wildmindai/status/1973075746038956115
  - *From: yi*

- **Wan 2.2 inpainting workflow** (workflow)
  - *From: SonidosEnArmonía*

- **Wan 2.2 Fun VACE inpainting workflow with test video** (workflow)
  - *From: Ablejones*


## Known Limitations

- **WAN 2.2 speed LoRAs cause slow motion issues**
  - Known issue affecting motion quality, even LightX2V team has concerns
  - *From: hicho*

- **PUSA doesn't work with I2V models**
  - Channel mismatch error when trying to use PUSA LoRAs on I2V base models
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Context windows introduce motion discontinuity**
  - No image quality degradation but motion continuation issues, introduces new elements between windows
  - *From: Kijai*

- **Can't use nag with split prompting in WAN 2.2**
  - Technical limitation preventing simultaneous use of both features
  - *From: Kijai*

- **Pusa keeps returning to init image with I2V**
  - Makes it not work well with I2V workflows
  - *From: Kijai*

- **End latent functionality issues**
  - Something is off when using end latent, can't handle single latent properly
  - *From: Kijai*

- **Context increases VRAM significantly**
  - 161 frame animation not feasible due to memory requirements
  - *From: 𝕯𝖗. 𝕸𝖆𝖈𝖆𝖇𝖗𝖊 ☠*

- **InfiniteTalk lacks context beyond individual windows**
  - No anticipation or preparation for singing after silence unless it fits perfectly in window
  - *From: Kijai*

- **Multitalk struggles with unclear audio**
  - If audio track is unclear, mouth movement may not work properly
  - *From: T2*

- **Static masks problematic with moving characters**
  - When character moves, static precise masks become misaligned
  - *From: Kijai*

- **Pusa interprets prompts in its own way**
  - May generate different actions than prompted (e.g., man walking instead of camera movement)
  - *From: Gill Bastar*

- **Wan 2.2 + Infinite Talk combination**
  - Not great quality when used together
  - *From: Kijai*

- **Context windows with reference frames**
  - Won't work properly since it works with ref in the latents
  - *From: Kijai*

- **Video extension causes detail deterioration**
  - Visible loss of details even on 81 frames, gets worse after multiple generations. Both FLF and simple frame reinjection have this issue
  - *From: 𝕯𝖗. 𝕸𝖆𝖈𝖆𝖇𝖗𝖊 ☠*

- **Color grading inconsistency in extensions**
  - First frame sometimes doesn't match color grading of frame it came from when extending videos
  - *From: 𝕯𝖗. 𝕸𝖆𝖈𝖆𝖇𝖗𝖊 ☠*

- **I2V context windows require character in frame**
  - Only works when character stays in frame, otherwise always tries to snap back to init image on each window
  - *From: Kijai*

- **WAN 2.2 max 5 seconds, 5B model max 10 seconds**
  - Standard generation limits for the models
  - *From: army*

- **GGUF gets heavier with every LoRA**
  - LoRAs can't be merged with GGUF format, so memory usage increases with each LoRA added
  - *From: Kijai*

- **Context windows with I2V inconsistent**
  - Sometimes tries to go back to start image between contexts, works 'once in a full moon'
  - *From: xwsswww*

- **Action delay in I2V generations**
  - 1 second delay before action starts, reducing effective action time from 5 to 4 seconds
  - *From: Lodis*

- **Censorship for biomedical horror content**
  - Cannot generate cables connecting to human arms, struggles with sci-fi biomedical content
  - *From: Dream Making*

- **CausVid not suitable for normal sampling**
  - Only intended for 3 latents worth of frames at once
  - *From: Kijai*

- **Sage attention diminishes results**
  - Impacts motion and overall quality
  - *From: TK_999*

- **Pusa doesn't work with I2V node currently**
  - There's no multi image setup for 5B model, it's just reusing the same image for now
  - *From: Kijai*

- **Context windows don't give nice results in some cases**
  - Context options don't always produce good results, depends on what you're doing
  - *From: Lodis*

- **Phantom and context windows seem confused**
  - Using phantom with context windows produces confusing results
  - *From: Kijai*

- **Foley adds background music too often**
  - Foley tends to add background music even when prompted with 'no music'
  - *From: . Not Really Human .*

- **Wan maximum native resolution is 720p**
  - Higher resolutions like 1920x1080 work but not natively, takes much longer to generate and may have quality issues
  - *From: Juampab12*

- **I2V with context windows has limited camera movement**
  - Can sort of work if subject never leaves frame or camera doesn't move much, as each window needs its own start image
  - *From: Kijai*

- **MultiTalk deteriorates over time**
  - MultiTalk was flawed and deteriorates the longer it goes, unlike InfiniteTalk which was trained to handle extension
  - *From: Kijai*

- **Wan 2.2 I2V adds too much motion for close ups**
  - I2V for close ups is weird, adds too much motion
  - *From: Dream Making*

- **Pusa not good at ending on multiple frames**
  - First-frame-last-frame doesn't work well with Pusa currently
  - *From: Kijai*

- **Wan VAE first frame being different**
  - The first frame encoding is different from subsequent frames, causing issues
  - *From: Kijai*

- **I2V model doesn't work well with T2V LoRAs**
  - T2V style LoRAs don't play nice with I2V models
  - *From: TheSwoosh*

- **WanGP memory optimization under Windows**
  - Only uses 9GB out of 16GB VRAM even on high settings, no Sage2+ support on Windows/Pinokio
  - *From: . Not Really Human .*

- **Higher resolution causes slower motion**
  - When raising resolution, motion becomes slower. 640x480 has fine motion but 720x1280 becomes slow motion
  - *From: DennisM*

- **InfiniteTalk works poorly on Wan 2.2 A14B model**
  - Better compatibility with other model versions
  - *From: Kijai*

- **Video quality degradation with consecutive I2V runs**
  - Each generation using last frame causes cumulative quality loss in sharpness, color and contrast
  - *From: Kenk*

- **High resolution outputs often distorted**
  - At resolutions like 1792x896x81, outputs aren't very good with subtle but clearly wrong distortions, especially with people
  - *From: IceAero*

- **Context swap transitions can be problematic**
  - Occasionally get bad context swap transitions, though minority of generations with current recommended settings
  - *From: blake37*

- **Motion limitations with image context**
  - Placing an image compromises motion in the video, getting much less motion than with static camera video
  - *From: Juampab12*

- **Wan 2.2 not good with text generation**
  - Produces garbled text that needs post-processing
  - *From: Drommer-Kille*

- **I2V struggles with long generations**
  - Cannot get much further than 10 seconds, degrades quality and changes face/clothes
  - *From: samhodge*

- **Last-frame extension methods have jarring seams**
  - Visible seams when extending video using last frame as first frame
  - *From: Kijai*

- **VACE reference image dimension constraints**
  - Reference image dimensions must match control video dimensions
  - *From: Kijai*

- **Models struggle with environmental consistency**
  - Roads and backgrounds change unexpectedly during generation
  - *From: Lodis*

- **Wan 2.2 doesn't follow prompts well with LightX and CFG 1**
  - Prompt adherence issues when using these settings together
  - *From: N0NSens*

- **Long generation methods unstable with Wan 2.2**
  - Too much motion makes InfiniteTalk unstable, better to use 2.1
  - *From: Kijai*

- **Context windows crash with RAM limits**
  - Need to reduce resolution or use tiled VAE decode
  - *From: hablaba*

- **S2V model limited to portrait talking heads**
  - Doesn't respond well to camera movement or character walking prompts, seems specifically trained for stationary talking head content
  - *From: nacho.money*

- **No framepack support for Wan 2.2**
  - Framepack may not work as well as expected with Wan, team working on their own 'streamer' solution
  - *From: flo1331*

- **Context extension issues with I2V**
  - Separate segments always return to starting image resulting in poor generations
  - *From: flo1331*

- **Radial sage has quality issues**
  - Has to be limited to certain steps and/or blocks to be acceptable, speed benefit only at larger resolutions
  - *From: Kijai*

- **Fantasy Portrait only supports Wan 2.1**
  - No confirmed update to support 2.2 yet
  - *From: Poppi*

- **InfiniteTalk works with low noise in 2.2**
  - Barely any effect on high noise model
  - *From: Kijai*

- **Can't use latents directly between samplers**
  - Have to do decode/encode again due to VAE latent structure
  - *From: Kijai*

- **Long character movement issues with multi/infinitetalk**
  - Camera must be static and character won't move for long generations
  - *From: N0NSens*

- **5B model poor at frame changes**
  - Cannot keep subject face well when subject moves from near to far
  - *From: army*

- **Wan struggles with strobing/flashing lights**
  - Model seems clueless about nightclub-style strobing effects
  - *From: Hippotes*

- **Model fights against non-trained content**
  - Models want to do what they were trained on, everything else is fighting the model to do differently
  - *From: mdkb*

- **Low step generation rarely good beyond midpoint**
  - With low steps, quality degrades significantly after the middle of the sequence
  - *From: Kijai*

- **Character consistency issues with Fun Control**
  - Fun Control severely changes character face and skin color compared to reference
  - *From: Cleo*

- **Wan 2.2 lacks extra features and forced to run high noise at full steps**
  - Takes 5-8 minutes on RTX 5090, making it not quite production ready
  - *From: MysteryShack*

- **Wan 2.2 I2V isn't great for changing backgrounds and scenes**
  - Cannot effectively change backgrounds and scenes compared to other methods
  - *From: MysteryShack*

- **Frame limit exists for long generations due to system RAM constraints**
  - 1750 frames OK, 3000 frames causes OOM even with 128GB RAM
  - *From: samhodge*

- **InfiniteTalk only works with I2V models**
  - Cannot be used with other model types due to how it modifies the first latent result
  - *From: Kijai*

- **Reward LoRAs don't work well with Pusa**
  - Combination produces suboptimal results in testing
  - *From: Lodis*

- **VHS Combine memory inefficiency**
  - Cannot handle 1000+ frames without excessive RAM usage leading to OOM
  - *From: samhodge*

- **No native Pusa implementation**
  - Currently no native ComfyUI implementation of Pusa, only wrapper version available
  - *From: Kijai*

- **Middle frame interpolation struggles**
  - 2.2 fun InP does middle frames better than previous versions but still has blending issues
  - *From: Kijai*

- **UniVerse-1 quality concerns**
  - Looking at examples, may not be worth implementation effort due to quality issues
  - *From: Kijai*

- **Radial attention always has quality hit**
  - Speed benefit comes at cost of quality, best used for testing then disabled for final runs
  - *From: Kijai*

- **4K upscaling seam issues**
  - Upscaling to 4K can produce visible seams and weird behaviors, requires higher padding/blur settings
  - *From: Juan Gea*

- **Wan 2.2 poor motion for short ranges**
  - Doesn't seem capable of good motion for short duration generations
  - *From: Kijai*

- **HPS LoRA adds unwanted artifacts in I2V**
  - Particularly bad on fur and feathers, tends to redraw faces incorrectly
  - *From: 𝕯𝖗. 𝕸𝖆𝖈𝖆𝖇𝖗𝖊 ☠*

- **Radial attention strict resolution requirements**
  - Must use resolutions divisible by block size (64 or 128), crashes with invalid sizes
  - *From: Izaan*

- **USDU upscaler VRAM limitations**
  - 3060 can handle 65 frames in ~20 minutes, but 81 frames takes 2.5 hours
  - *From: mdkb*

- **Native Infinite Talk doesn't work with VACE yet**
  - Currently only works with I2V, VACE integration not implemented
  - *From: Kijai*

- **HuMo model limited to 97 frames**
  - Trained on 97-frame videos at 25 FPS, generating longer may degrade performance until new checkpoint released
  - *From: Zabo*

- **Wan 2.2 5B poor motion with I2V**
  - Can't get simple camera pull/zoom out with 30 steps and 3.5 CFG, works better with T2V
  - *From: Hevi*

- **VACE and lipsync trade-off**
  - Using VACE to swap character back strips out the lipsync
  - *From: mdkb*

- **Radial attention quality trade-off**
  - Provides speed gains but messes with detail and mutes character emotion
  - *From: blake37*

- **20s InfiniteTalk at 720p requires more than 24GB VRAM**
  - Even with available techniques, this length and resolution exceeds 24GB capacity
  - *From: BecauseReasons*

- **HuMo has no continuous generation**
  - What's the point without continuous generation, though could work with context windows
  - *From: Kijai*

- **HuMo audio currently not working**
  - Could be unfinished audio code, may not work with lightx2v
  - *From: Kijai*

- **InfiniteTalk doesn't handle angles well**
  - Performance degrades significantly with non-frontal angles
  - *From: BecauseReasons*

- **HuMo locked to specific resolutions**
  - Code works with only 2 different resolutions due to pre-encoded empty latents
  - *From: Kijai*

- **3 second limit in HuMo**
  - Though seems it can do 129 frames too
  - *From: Kijai*

- **Cannot use GGUF models with native ComfyUI loaders for modules**
  - GGUF modules don't have a loader in native ComfyUI currently
  - *From: Kijai*

- **GGUF loras cannot be merged**
  - With City's ComfyUI-GGUF nodes, loras are always used unmerged
  - *From: Kijai*

- **HuMo code doesn't work**
  - Original HuMo repository has basic errors preventing execution, audio functionality broken
  - *From: Kijai*

- **Video extension through latent cutting not possible**
  - Due to temporally packed latent space, must decode and re-encode for extensions
  - *From: Kijai*

- **Control video results worse than 2.1**
  - Even with no loras, control video results are significantly worse than VACE 2.1
  - *From: ArtOfficial*

- **VACE 2.2 doesn't integrate environment lighting as well as 2.1**
  - Generates into masked shape without full lighting integration
  - *From: ingi // SYSTMS*

- **VACE only works with T2V models (16 input channels)**
  - Cannot be used with I2V models, needs T2V architecture
  - *From: Kijai*

- **HuMo audio functionality doesn't work on single GPU**
  - Audio crossattn function has issues on single GPU setups
  - *From: Kijai*

- **Color shifting still occurs with video extension**
  - Both 2.1 and 2.2 show color degradation issues in extensions
  - *From: N0NSens*

- **HuMo cannot be combined with VACE**
  - Different conditioning systems prevent simultaneous use
  - *From: Kijai*

- **HuMo has issues with non-trained resolutions**
  - Works best with resolutions it was trained on
  - *From: Kijai*

- **VACE expanded masks create grey alpha edges**
  - Masking expansion causes color bleeding artifacts
  - *From: yo9o*

- **HuMo emotion prompts don't control character movement**
  - Can control emotions but physical actions like tai chi or running are not retained
  - *From: piscesbody*

- **GGUF models have compatibility issues with wrapper**
  - Some GGUF models cause stride errors in wrapper but work in native
  - *From: JmySff*

- **HuMo context windows don't work as well as InfiniteTalk**
  - Context windows work somewhat but not nearly as well as endless infinite talk mode
  - *From: Kijai*

- **HuMo lacks endless generation mode**
  - Currently limited usecase due to missing endless generation capability
  - *From: Kijai*

- **Profile shots impossible with HuMo**
  - Reference image always steers generation back to facing camera
  - *From: ˗ˏˋ⚡ˎˊ-*

- **WAN stubborn about full human body**
  - Always aims for whole human body, cyborgs or complex robots barely possible
  - *From: Hoernchen*

- **Context windows cause background artifacts**
  - Always an issue with context windows causing strange backgrounds
  - *From: Kijai*

- **HuMo degrades beyond 97 frames**
  - Model trained for 97 frames at 25 fps, longer generations may degrade performance
  - *From: Kijai*

- **VACE 2.2 lacks proper distill lora for high noise**
  - Makes it harder to work with - requires 3 samplers or scheduling cfg/lora strengths
  - *From: Kijai*

- **Context windows cause visible shifts between windows**
  - Background and small details like blood on lip disappearing between context windows
  - *From: Kijai*

- **VACE adds random elements with reference-only input**
  - VACE with only reference image likes adding random things to motion
  - *From: Lumifel*

- **HuMo is very sensitive to context options settings**
  - Spits out errors based on context options settings, seems too sensitive to random numbers entered
  - *From: xwsswww*

- **Multiple reference images not working well with HuMo**
  - Trying to pass more than one reference image results in it being ignored or only using first image
  - *From: Alisson Pereira*

- **Unianimate creates stiff movement**
  - Even at 0.1 strength, Unianimate creates stiff Terminator-like head movement when using Blender-generated pose data
  - *From: mdkb*

- **LightX severely impacts S2V quality**
  - LightX pixelates output and kills movement in speech-to-video workflows
  - *From: The Coin Hunter*

- **VACE 2.2 Fun worse at reference handling than 2.1**
  - Multiple references contaminate the video, not as good for face/body swaps
  - *From: Ablejones*

- **Concatenated reference images don't work properly**
  - Just places references in positions/sizes they appear, doesn't enable dynamic interaction
  - *From: Ablejones*

- **Context windows don't work well with Wan 2.2 I2V**
  - Prompt scheduling not available, '|' separator doesn't work reliably
  - *From: Phr00t*

- **HuMo + InfiniteTalk results aren't great**
  - Starts with HuMo then extends with InfiniteTalk, quality suffers
  - *From: Kijai*

- **Wan models poor at spatial understanding**
  - Bad understanding of spatial space, size etc, affects T5 and UMT5 text encoder models
  - *From: Zabo*

- **HuMo 1.7B runs 4 model passes per step**
  - Makes it very slow to use compared to other models
  - *From: Kijai*

- **VACE 2.2 Fun not as good for clothing/face swaps with pose control**
  - Different applications than VACE 2.1 - better for high motion inpainting
  - *From: ArtOfficial*

- **Tiling artifacts when upscaling with detailed prompts**
  - New objects appear out of nowhere, model fantasizes when it doesn't understand
  - *From: N0NSens*

- **HuMo short generation length**
  - Current HuMo can only do short clips - 97 frames at 25 fps, not many seconds
  - *From: Kijai*

- **HuMo stiff head problem**
  - HuMo tends to produce videos with very immovable/stiff heads compared to Infinite Talk
  - *From: mdkb*

- **Context windows repetition**
  - Context windows cause repetition of initial image every 81 frames
  - *From: Koba*

- **Florence only works for images**
  - Florence node only works for image enhancement, not video
  - *From: FL13*

- **WanVideo Encode Latent Batch not compatible with VACE**
  - The method is for I2V models, which VACE is not
  - *From: Kijai*

- **Context windows causing issues with 2.2**
  - Generally a really dumb idea with I2V workflows in 2.2, causes repetition of init image
  - *From: Koba*

- **Humo 1.7 wrapper doesn't recognize gguf**
  - Wrapper didn't recognise the humo 1.7 gguf with error 'patch_embedding.weight'
  - *From: patientx*

- **GGUF models very slow**
  - Wan2.1 GGUF Q5 720P model took 1 hour 4 minutes for 240 frames with 4 steps, despite better quality
  - *From: NC17z*

- **LightX2V poor performance with 2.2**
  - LightX2V is not trained for 2.2 so it works poorly
  - *From: Kijai*

- **Context windows overflow on long sequences**
  - Context windows overflow on encode decode with 3000 input frames
  - *From: Gleb Tretyak*

- **HuMO 97 frame limit**
  - Model crashes beyond 97 frames
  - *From: VRGameDevGirl84(RTX 5090)*

- **HuMO resolution restriction**
  - Only works with 1280x720, other resolutions cause tensor size mismatch errors
  - *From: amli*

- **VACE 2.2 degradation in some workflows**
  - Some workflows show quality degradation compared to 2.1
  - *From: Vérole*

- **Radial attention resolution requirements**
  - Only supports image sizes divisible by block size, 1280x720 not supported with 128 block size
  - *From: mdkb*

- **Context window issues with HuMO**
  - Entering 97 for context_frames produces worse output than not using it at all
  - *From: patientx*

- **Video models have poor geometry understanding**
  - Get confused with spatial relationships, which is why MagVideo and Nvidia Gen3c now have explicit physics training
  - *From: mallardgazellegoosewildcat*

- **Side profile generation issues**
  - Side profiles seem to need control to force them, models struggle with character turning around
  - *From: Kijai*

- **InfiniteTalk can't do partial windows**
  - Always rounds up frame count, can't sample single frames
  - *From: Kijai*

- **Merged models lose control and quality**
  - Merge processes between different models can destroy motion and quality
  - *From: Alisson Pereira*

- **GGUF models don't work with wrapper**
  - Work fine with native ComfyUI nodes but cause tensor type mismatch errors with WanVideoWrapper
  - *From: Izaan*

- **ClownShark sampler not compatible with wrapper**
  - Only works with native ComfyUI implementation
  - *From: JohnDopamine*

- **VACE struggles with style consistency**
  - User couldn't achieve desired cartoon style, kept getting anime instead despite negative prompts
  - *From: Gleb Tretyak*

- **Character consistency vs motion following trade-off**
  - Good character consistency tends to fail at following control video, while good motion following destroys character consistency
  - *From: Gleb Tretyak*

- **Character LoRA bleeding between characters**
  - Makes it difficult to maintain distinct characters in multi-character scenes
  - *From: Ruairi Robinson*

- **Phantom/MagRef lose consistency on face turns**
  - While LoRA allows character rotation, instant methods fail with perspective changes
  - *From: mdkb*

- **VACE darkens unmasked areas**
  - Phantom+VACE combination causes darkening in areas that should remain unchanged
  - *From: xwsswwx*

- **Lucy Edit trained on 5B model**
  - Quality reflects limitations of smaller 5B base model
  - *From: HeadOfOliver*

- **Only one character at a time**
  - Looks like only one character at a time though
  - *From: Piblarg*

- **Humo loves making characters backlit**
  - Having tough time prompting direct light with consistent results
  - *From: Quality_Control*

- **No speedup on high noise for VACE 2.2**
  - Need even MORE steps with nearly no speedup for VACE 2.2
  - *From: MysteryShack*

- **LightX2v kills motion blur**
  - Big issue with lightX2v - it kills motion blur
  - *From: Ruairi Robinson*

- **All inputs technically optional but purpose of model is clearly people**
  - Model designed specifically for human animation
  - *From: Kijai*

- **Original method degrades over time**
  - Context method better for very long generations
  - *From: Kijai*

- **Face encoder wants to do faces**
  - Struggles with non-face subjects, changes arms and legs too
  - *From: Kijai*

- **Can't do longer than 5s v2v easily**
  - User asking about extended video lengths
  - *From: Drommer-Kille*

- **DWPose detection is old tech from 2023 and not very robust**
  - Fails on many frames causing poor results
  - *From: Lodis*

- **Side effect of higher CFG can be extra unwanted people and messing up the prompt**
  - CFG settings need careful tuning
  - *From: Drommer-Kille*

- **VACE padding uses white, Wan Animate uses black**
  - Different padding behavior between models can affect results
  - *From: Kijai*

- **Fixed 77-frame window size**
  - Cannot process partial windows, always outputs multiples of 77 frames
  - *From: Kijai*

- **Motion encoder cannot be quantized**
  - GGUF conversion fails on motion and face processing components
  - *From: Kijai*

- **5B VAE destroys sharpness**
  - Significant quality degradation compared to 14B model
  - *From: mallardgazellegoosewildcat*

- **Unreliable generation sometimes**
  - May need to run multiple seeds to get good results
  - *From: mallardgazellegoosewildcat*

- **Masking fails without face images**
  - WanAnimate masking breaks if no face images are provided
  - *From: Kijai*

- **Frame window restrictions**
  - Errors occur when going beyond two windows - 161 frames works with window 81 but 171 frames with same window fails
  - *From: theUnlikely*

- **Motion exaggeration at high frame counts**
  - Higher frame counts cause motion to become overexaggerated idle wobble
  - *From: lostintranslation*

- **Lower resolutions possible but poor quality**
  - Lower resolutions work but don't work very well
  - *From: patientx*

- **Model struggles with non-human subjects**
  - Didn't work well with hippo - model is human centric after all
  - *From: Kijai*

- **Point tracker doesn't work on servers**
  - Only works locally, won't work on Runpod/Vast.ai type servers
  - *From: traxxas25*

- **Pupil/gaze direction tracking doesn't work properly**
  - Pupils don't track correctly, seems to be related to face processing
  - *From: A.I.Warper*

- **Model conditioned on single person only**
  - Can't handle multiple characters in scene
  - *From: Piblarg*

- **Frame count restrictions**
  - Performs poorly with frame counts under 81
  - *From: Kijai*

- **TeaCache not effective with low steps**
  - More counterproductive than helpful with distilled/lightning models using low steps
  - *From: The Punisher*

- **WanAnimate likeness not exactly 1:1**
  - Better with realistic people, less so with anything outside of that, fine details especially affected
  - *From: Piblarg*

- **Lucy Edit doesn't understand many prompts**
  - Can't do much complex stuff, doesn't support reference images
  - *From: ArtOfficial*

- **Face cropping bad in example workflow**
  - Depends on input, might need to pad it, doesn't work well with side profile faces
  - *From: Kijai*

- **LightX2V stiffens motion in out of distribution stuff**
  - Settings that worked for stylised/animated stuff created noisy messes for realism
  - *From: pom*

- **WanAnimate best for humans currently**
  - No luck with non-human characters in this implementation
  - *From: Mazrael.Shib*

- **Wan Animate struggles with cartoon/non-human characters**
  - Duck character (Duckman) has issues, model expects human-like characters
  - *From: buttercup5108*

- **Poor likeness compared to Phantom**
  - Wan Animate has issues with character likeness, especially from different angles
  - *From: xwsswww*

- **Quality degrades with long generations**
  - Quality tends to get worse and worse in extended segments
  - *From: Gleb Tretyak*

- **Fragile reference frame handling**
  - Wan Animate is more fragile than VACE regarding reference frame, especially without background
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Lucy Edit quality still poor**
  - Even with recent improvements, quality is still far from perfect and unusable for many cases
  - *From: BecauseReasons*

- **WanAnimate has rigid masking compared to VACE**
  - Less flexible masking options, need to grow and blur or use precise masks
  - *From: DawnII*

- **Model struggles with faces that are too small/far away**
  - Needs super zoomed in reference video for face performance to work properly
  - *From: ArtOfficial*

- **Character replacement more prone to CFG burning than pose driving**
  - Pose-driven videos generally don't burn, character replacement often does
  - *From: slmonker(5090D 32GB)*

- **Native ComfyUI implementation may not work with SageAttention yet**
  - Sage command line flag causes issues
  - *From: ArtOfficial*

- **30xx series GPUs don't get efficient fp8 memory usage**
  - fp8 not native on 30xx series
  - *From: Lodis*

- **Cannot choose frame in Points Editor**
  - Points Editor automatically selects first frame, cannot manually select different frame for mask detection
  - *From: Kijai*

- **Context windows not available in native**
  - Native WanAnimate doesn't have context windows, must use frame overlap or multiple sampling blocks
  - *From: ArtOfficial*

- **Pose retargeting missing**
  - Won't work well if reference character is smaller or cartoonish without pose retargeting
  - *From: Kijai*

- **Face detection requires human poses**
  - Using non-human reference images requires human pose videos to work properly
  - *From: slmonker(5090D 32GB)*

- **Pose retargeting lacks temporal stability**
  - Not temporally stable at all, needs smoothing
  - *From: Kijai*

- **No temporal pose processor available**
  - Sapiens doesn't have temporal processing capabilities
  - *From: Kijai*

- **VACE module seems to be ignored in some workflows**
  - Even with strength of 1, it just uses prompt instead of VACE input
  - *From: Gleb Tretyak*

- **OOM at 1280x704 resolution**
  - Even with blockswap 40, same as VACE limitations
  - *From: CaptHook*

- **720p generation requires significant VRAM**
  - 12GB VRAM can't handle 113 frames @ 720p without tiling
  - *From: harriet_h*

- **Relight LoRA pulls towards realism**
  - Makes it difficult to maintain illustrated/cartoon styles
  - *From: Kijai*

- **ComfyUI implementation missing pose retargeting**
  - Unlike the official Wan platform which has this feature
  - *From: Kijai*

- **Hunyuan and Flux models only work properly with bf16**
  - fp16 causes issues with these model types
  - *From: Kijai*

- **Lucy Edit only available as 5B model**
  - No 14B model available yet
  - *From: Lodis*

- **WanAnimatePreprocess replacement mode is unfinished**
  - Pose retargeting feature still work in progress
  - *From: Kijai*

- **Can't use reference image with masking in WanAnimatePreprocess**
  - Reference is only for retargeting mode
  - *From: Kijai*

- **High noise model in 2.2 PUSA introduces noisy motion**
  - Quality degrades in extension scenarios
  - *From: DawnII*

- **Qwen Edit Nunchaku version is censored**
  - Compared to fp8 and bf16 versions
  - *From: MysteryShack*

- **PUSA requires per-generation tuning**
  - Every input/prompt combination needs manual adjustment of LoRA strength and CFG settings
  - *From: lostintranslation*

- **Context windows below 30 frames produce poor results**
  - Very low context window sizes take forever and don't end up looking good
  - *From: Kijai*

- **Wan Animate generates different people between context windows**
  - ID consistency fails when using context windows with lower frame counts
  - *From: xwsswww*

- **Wan models loop only at 161 frames**
  - Natural looping occurs at 161 frames but quality degrades significantly before that point
  - *From: xiver2114*

- **ControlNet stuff not working properly**
  - Controlnet stuff is kinda working, but not really following the exact mapping
  - *From: Lodis*

- **Face consistency issues in wide shots**
  - Unless it's medium or closeup shots, keeping same face kinda fails
  - *From: 🦙rishappi*

- **Quality degradation with multiple images**
  - Quality starts to degrade with 3 image inputs, two images seems ideal
  - *From: Lodis*

- **Self-forcing models only 1.3B**
  - Those self forcing models are 1.3B, they never did 14B
  - *From: Kijai*

- **Side profile face tracking doesn't work**
  - Pose detection fails on full side profile faces where other side isn't in view
  - *From: xwsswww*

- **WAN 2.5 audio quality issues**
  - Audio has 'jzzzzzzz' noise, quality behind VEO 3
  - *From: MysteryShack*

- **I2V not compatible with VACE**
  - I2V model doesn't work with VACE fun control
  - *From: Gleb Tretyak*

- **WAN 2.5 may not be open source initially**
  - Reports suggest it may remain closed source, unlike previous WAN models
  - *From: BecauseReasons*

- **Wan 2.5 audio VAE has poor quality**
  - Audio fidelity is bad based on examples shown
  - *From: MysteryShack*

- **Wan Animate often extends limbs improperly**
  - Pose transfer frequently creates unrealistic limb extensions
  - *From: Kijai*

- **Wan Animate only works with human detection**
  - Limited to human pose detection, no support for other control inputs
  - *From: 青龍聖者@bdsqlsz*

- **MagRef is I2V while VACE is T2V**
  - Cannot directly combine MagRef with VACE due to different input requirements
  - *From: ArtOfficial*

- **Model availability uncertain**
  - Wan 2.5 shown as preview only, release date and open source status unclear
  - *From: multiple users*

- **Color smudging during motion**
  - Happens during fast motion, more apparent in anime and greenscreen usage
  - *From: VK (5080 128gb)*

- **Text integration not perfect**
  - Text appears clear but not perfectly integrated, a bit wonky on cards like it was Photoshopped on
  - *From: Screeb*

- **Wan 2.5 only available via API**
  - No local weights available currently, only accessible through platforms like wavespeed and fal
  - *From: Zabo*

- **VEO3 heavily censored**
  - 80% rejection rate, blocks magic, transformations, alien plasma blasters, requires ID verification
  - *From: MysteryShack*

- **Audio generation easily triggers mute**
  - Even SFW content gets muted frequently, no refund on failed generation credits
  - *From: crinklypaper*

- **Wan 2.5 lipsync quality**
  - Audio input lipsync is worse than existing solutions like InfiniteTalk/HuMo
  - *From: Juampab12*

- **Wan 2.5 VAE artifacts**
  - Model shows VAE artifacts, suggesting quality compromises
  - *From: mallardgazellegoosewildcat*

- **StepVideo GPU requirements**
  - Not something you can run on consumer GPUs
  - *From: Kijai*

- **AI 3D model quality**
  - AI for 3d mesh generation and texturing exists but quality is poor, especially topology
  - *From: Lodis*

- **Wan 2.5 model is much heavier than previous versions**
  - Confirmed by Wan team member during presentation, making it challenging for consumer GPUs
  - *From: ZeusZeus*

- **Wan 2.5 queue times very long**
  - Users reporting 1.5-2.5 hour wait times for free generation
  - *From: DawnII/seitanism*

- **VACE 2.2 cannot do first-to-last frame consistently**
  - User reports issues with first to last frame functionality
  - *From: Gleb Tretyak*

- **Pruning models limited to 50% maximum**
  - Even 50% pruning results in big quality drop
  - *From: mallardgazellegoosewildcat*

- **WanAnimate doesn't work well with anime styles**
  - Based on experiences, Animate doesn't work too well with anime content
  - *From: harriet_h*

- **Anisora 3.2 struggles with non-human subjects**
  - Having trouble animating a cartoon pony, seems really meant for humans
  - *From: Rainsmellsnice*

- **Pose retargeting fails without matching poses**
  - Often doesn't work at all if retarget poses don't match reference poses
  - *From: Kijai*

- **Wan 2.2 harder to use without proper distill**
  - Have to play with cfg and lora strengths since no 2.2 high noise distill lora without downsides
  - *From: Kijai*

- **Different text effects between VACE versions**
  - Can't get same text effects with vace 2.2 as with 1.1 and masking
  - *From: VK (5080 128gb)*

- **Phantom ignores mask and degrades image**
  - Blackens image and contrast fails, VAE decoding affects entire image regardless of masking
  - *From: mdkb*

- **VACE 2.1 respects reference image positioning too much**
  - Tends to respect positioning of reference image in frame too much, though can be advantage in some use cases
  - *From: 42hub*

- **Wan API heavily restricted and slow through third-party services**
  - ComfyUI API 10-30min vs 3min on official site, moderation blocks content that works elsewhere
  - *From: Drommer-Kille*

- **Distilled models have reduced diversity**
  - Quality may be higher but output variety suffers compared to original models
  - *From: ~dvs~*

- **Wan models perform poorly above 81 frames**
  - Recommended to stay at or below 81 frames for stable generation
  - *From: seitanism*

- **WanAnimate depth input issues**
  - Turns video green, seems to expect pose data rather than depth
  - *From: Nathan Shipley*

- **Lynx unlikely to work with WanAnimate**
  - Animate is I2V while Lynx is T2V focused, generally doesn't work in reverse
  - *From: Kijai*

- **VACE doesn't work on I2V models**
  - Cannot force VACE to work on I2V even when attempted
  - *From: Kijai*

- **Plastic face quality in WanAnimate**
  - High quality ref images tend to lose facial details, faces appear plastic
  - *From: Gateway {Dreaming Computers}*

- **Lynx relies on insightface with non-commercial license**
  - Uses buffalo_l model which has licensing restrictions
  - *From: Kijai*

- **Lynx no new long generation method**
  - Just T2V with better identity reference, usefulness depends on control method compatibility
  - *From: Kijai*

- **VACE not good with lipsync**
  - Strips out lipsync when used on already lipsynced content
  - *From: mdkb*

- **WanAnimate retains human head when converting to non-human**
  - Always keeps human head even when trying anthropomorphic animals/creatures
  - *From: A.I.Warper*

- **Humo q8 GGUF not getting likeness**
  - Using Kijai's example workflow but no character resemblance
  - *From: xwsswww*

- **Lightning LoRA still changes style too much**
  - Prompting night scenes still produces day scenes, overly bright output
  - *From: Kijai*

- **T2V Lightning LoRAs cause motion inconsistency when used on I2V**
  - Works but results not optimal compared to native I2V training
  - *From: yi*

- **New Lightning LoRA degrades color on I2V**
  - Color degradation observed when using T2V LoRA on I2V workflow
  - *From: Lodis*

- **Lightning LoRA still crap at I2V**
  - Kijai confirmed new Lightning LoRA still has issues with I2V
  - *From: Kijai*

- **InfiniteTalk doesn't work with Long I2V Multi node**
  - Works with regular ImageToVideo Encode but fails with multi-node setup
  - *From: Vérole*

- **LYNX fails completely on anime content**
  - IP adapter resolution too low at 112x112, doesn't include hair or beard details
  - *From: Kijai*

- **WanAnimate doesn't preserve background from reference image**
  - Uses reference for character only, not as start image like I2V
  - *From: Kijai*

- **Lightning loras don't work well in ComfyUI**
  - According to developers, hence the dyno full model release
  - *From: MysteryShack*

- **New Lightning has baked-in style issues**
  - Same problem as other distillations like AccVid and FastWan
  - *From: Kijai*

- **Wan 2.2 doesn't lip sync well with WanAnimate**
  - Lip sync quality is poor compared to InfiniteTalk, even with good face reference videos
  - *From: reallybigname*

- **Camera zoom difficult with Wan 2.2 i2v**
  - Camera zoom prompts not working reliably with lightx2v i2v 480p lora
  - *From: xwsswww*

- **Face consistency degrades over 77 frames**
  - Loss of face consistency when video exceeds 77 frames, faces become different each time despite same seed
  - *From: mdkb*

- **SAM2 not great for face-only targeting**
  - SAM2 struggles with precise face detection, face detector nodes work better for face-only tasks
  - *From: Draken*

- **Sage Attention 3 has quality hit with Wan**
  - Significant quality degradation makes it not worth using with Wan models
  - *From: Kijai*

- **WanAnimate character consistency degrades over 77 frames**
  - Person doesn't look like reference image anymore in longer videos
  - *From: mdkb*

- **Uni3C effect much weaker with Wan 2.2**
  - Even at 4.0 strength the effect is pretty poor with 2.2 compared to 2.1
  - *From: Kijai*

- **Uni3C low noise incompatibility**
  - Low noise side can't use Uni3C at 3.0 strength
  - *From: Kijai*

- **Characters always speak in Wan 2.2**
  - Even with closed mouth input and prompts, characters tend to have open mouths or speaking animation
  - *From: Gigi8*

- **Camera motion with character performance mismatch**
  - Using orbit camera motion on front-facing character keeps character front-facing while background moves
  - *From: A.I.Warper*

- **Uni3C greater effect on background**
  - Has more impact on background than intended subject
  - *From: Kijai*

- **Wan 2.2 VACE producing poor results**
  - Multiple users reporting bad results with 2.2 fun vace, reverting to 2.1
  - *From: Abx, Gleb Tretyak*

- **Flux LoRA mixing issues**
  - if you try and mix more than a couple of loras in flux you get scenes from that 1990s brian yuzna horror movie SOCIETY. you can train a character and it looks good standing there but then have them driving a motorbike lora then say you want to add a style lora , then you want add any other thing and it melts to shit
  - *From: Ruairi Robinson*

- **Wan Alpha not working as expected**
  - Tests show it's removing the alpha channel rather than properly generating transparency effects
  - *From: U̷r̷a̷b̷e̷w̷e̷*

- **Wan 2.5 API very sensitive to content filtering**
  - Flags even innocent AI-generated images of pirate ships as IP infringement
  - *From: D-EFFECTS*

- **Kandinsky 5.0 requires H100 or A100 for researchers**
  - Though 2B model should run on consumer GPUs
  - *From: Gleb Tretyak/Draken*

- **No 2.2 version of native inpaint workflow available**
  - Need to modify existing workflows for two model version
  - *From: Ablejones*

- **Optimal blockswapping requires CUDA kernel not yet available**
  - For memory and cache management with comms overlapping
  - *From: mallardgazellegoosewildcat*


## Hardware Requirements

- **PUSA LoRAs memory usage**
  - Nearly 5GB per LoRA, requires merging for systems with 64GB RAM to avoid crashes
  - *From: screwfunk*

- **WAN S2V on 8GB VRAM**
  - Possible with Q4 quantization or lower, 640x81 frames recommended for RTX 3070
  - *From: hicho*

- **VRAM for InfiniteTalk**
  - RTX 4090 (24GB) can do about 1024x500, higher resolutions cause OOM
  - *From: Ubertummen*

- **RAM usage increase in ComfyUI**
  - Recent updates causing high system RAM usage making PC unusable
  - *From: dg1860*

- **NVME swap file solution**
  - Creating swap file on NVME drive helps with RAM cache flushing
  - *From: dg1860*

- **VRAM usage inconsistency**
  - First run uses 19.6GB, second run drops to 14.1GB on Windows with Triton compile
  - *From: Kijai*

- **Infinite Talk frame limits on 12GB VRAM**
  - 4070 12GB gets OOM when trying context options for frame generation
  - *From: dipstik*

- **--highvram flag effectiveness**
  - Only useful when you have more VRAM than RAM. 48GB VRAM + 50GB RAM difference too little. For WAN 14B, high-vram would need 80GB+
  - *From: Kijai*

- **A6000 48GB performance**
  - 161 frames generated in 12 minutes. Torch compile can add 20-30% speed boost on top of sage attention
  - *From: Ashtar*

- **4080 16GB + 96GB RAM performance**
  - Context window workflow takes 14-18 minutes, requires 20 block swap
  - *From: Dever*

- **3090 thermal management**
  - Can crash at 86°C, custom fan curve and thermal pad replacement solved crashing issues
  - *From: Ashtar*

- **Performance optimization impact**
  - Sage attention can provide 100% speed boost at higher resolutions, torch compile adds 20-30% more plus reduced VRAM usage
  - *From: Kijai*

- **Two unquantized models**
  - Already 64GB VRAM requirement
  - *From: Kijai*

- **VRAM usage with bf16 on RTX 5090**
  - Can run but tight on memory
  - *From: Kijai*

- **Example workflow uses ~65GB VRAM**
  - Normal usage range 55-65GB VRAM
  - *From: HeadOfOliver*

- **1600W PSU**
  - User has very good 1600W PSU but still experiencing crashes
  - *From: Drommer-Kille*

- **128GB DDR5 with MSI motherboard**
  - Good boot times even with large RAM configuration
  - *From: Kijai*

- **VRAM management**
  - 14B model needs careful block swapping - 20 blocks saves half VRAM, 40 blocks slower but uses less VRAM
  - *From: Kijai*

- **VRAM threshold**
  - Avoid VRAM going past 95% to prevent huge speed loss
  - *From: Kijai*

- **Generation times**
  - 40 seconds video takes 40 minutes on RTX 6000 Pro at 1024x1024 full quality
  - *From: ingi // SYSTMS*

- **Context generation performance**
  - 480x832 I2V with Pusa and context: 420 seconds (vs 353 seconds without Pusa)
  - *From: Ashtar*

- **Generation speeds with different settings**
  - 720p 5 second video takes 6 minutes, 15 mins at 768x768 with fp16_fast, 1 minute per second for InfiniteTalk standard
  - *From: ComfyCod3r*

- **InfiniteTalk performance**
  - 1 minute long generation in 9 minutes on good GPU, 40 mins on 5090 for 5500 frames with 4 steps
  - *From: Charlie*

- **MultiGPU native workflow performance**
  - 1280x720 generation took 416.11 seconds with AIO and MultiGPU nodes with blockswap
  - *From: : Not Really Human :*

- **VRAM optimization in wrapper**
  - 2060 can do 70 frames at 720x480 with recent optimizations
  - *From: hicho*

- **InfiniteTalk long generation VRAM**
  - Can do 5500+ frames on 32GB VRAM + 64GB RAM easily, VRAM use determined by window size and resolution only
  - *From: Kijai*

- **720p 81 frames 40 context window**
  - Requires 37GB VRAM
  - *From: samhodge*

- **1080p generation on 5090**
  - Can do 1080p with full block swap but is slow, around 5 minutes
  - *From: hicho*

- **1792x896x81 frames**
  - Can run reliably on high-end hardware but output quality suffers
  - *From: IceAero*

- **Basic model with LoRAs**
  - 304x304x33 frames fits into 16GB VRAM without CLIP, 3x faster than using system RAM
  - *From: patientx*

- **RAM for Wan 2.2**
  - 96+GB RAM recommended, 64GB not enough, 32GB will be harsh with constant swapping
  - *From: Ada*

- **VRAM for Wan 2.2**
  - 16GB VRAM just enough with quant, 20GB for GGUF 8.0 at 848x480, 36GB for 1280x720
  - *From: Ada, samhodge*

- **System RAM for video output**
  - 36GB RAM needed for 1737 frames at RGB 24bit 1280x720
  - *From: samhodge*

- **Low-end testing**
  - RTX 2060 can handle 1024x700, 33 frames
  - *From: hicho*

- **RTX 5090 upscaling performance**
  - 14 minutes to upscale to 4K
  - *From: FL13*

- **24GB VRAM limits**
  - 512x512 at 99.9% usage, 640x640 causes OOM
  - *From: Foxbite*

- **24GB with block swapping**
  - Can do 1024x576x109 frames with 16/64 context
  - *From: N0NSens*

- **6GB VRAM with wrapper**
  - Can do 720x480x81 frames with 2GB difference in VRAM usage
  - *From: hicho*

- **VRAM usage with blockswap**
  - 5090 with blockswap 40 uses around 31GB VRAM, considered danger zone
  - *From: blake37*

- **2060 6GB VRAM capabilities**
  - Can do 512x512 33 frames without blockswap, 720x512 81 frames with full blockswap
  - *From: hicho*

- **RAM requirements for native workflow**
  - 32GB RAM may cause issues with 2 fp8 models, needs at least 64GB for optimal performance
  - *From: hicho*

- **4060ti 16G performance**
  - Works at 480x832 resolution
  - *From: .: Not Really Human :.*

- **16GB VRAM generation time**
  - 5-7min per window at low res, can be faster with block tuning
  - *From: N0NSens*

- **Recommended resolution for 3000 series**
  - 832x480 good balance for older cards
  - *From: The Shadow (NYC)*

- **VRAM optimization**
  - 720p video possible with 16G VRAM using swap block in wrapper
  - *From: army*

- **Power consumption**
  - 5080: ~200w for Wan video vs 350w for Flux images, 5090: ~226w at 720p generation
  - *From: VK (5080 128gb)*

- **VRAM for VACE long videos**
  - 30 seconds achievable on low-VRAM setups, 60 seconds harder with multiple OOM crashes
  - *From: Akumetsu971*

- **High-end setup for unquantized models**
  - Using full 14B models without quantization requires strong GPU
  - *From: Cleo*

- **System RAM for long videos**
  - 1750 frames OK with 128GB RAM, 3000 frames causes OOM. 68GB system RAM used for 3500 frames, jumping to 105GB during processing
  - *From: samhodge*

- **VRAM usage during generation**
  - Charlie did 2300 frames at 720p. 12GB VRAM usage reported for 3500 frame generation
  - *From: Charlie*

- **Processing time scaling**
  - Beyond 150 frames I2V slows to 500s/it, taking 10x longer than 130 frames
  - *From: BecauseReasons*

- **RAM usage with Wan 2.2**
  - Using 88GB out of 96GB system RAM for 1280x720 81 frame generation on RTX 5090 is normal in Windows
  - *From: Kijai*

- **VHS memory limits**
  - VHS Combine OOMs with 10GB RAM limit at 1000 frames, works fine at 600 frames
  - *From: samhodge*

- **H100 performance**
  - 3 minutes for 81 frames at 720x1280 with lightx2v
  - *From: vuuw*

- **Upscaling performance on different resolutions**
  - 1280x720 took 2:40, 1536x864 took 28:09 on unspecified hardware for low model upscaling
  - *From: N0NSens*

- **InfiniteTalk rendering speed**
  - 39-41 frames takes ~10 minutes on 4090
  - *From: humangirltotally*

- **VACE upscaling speed**
  - 81 frames took 4-5 minutes with 5090
  - *From: FL13*

- **4-stage i2v timing**
  - 320x480 20 sec video in ~9 minutes, used to take 20-30 minutes
  - *From: patientx*

- **RAM usage scaling**
  - Windows shows 90GB+ usage but Linux needs only 64GB for same workloads, 128GB recommended for Windows
  - *From: Kijai*

- **USDU upscaling on RTX 3060**
  - 65 frames take ~20 minutes, 81 frames take 2.5 hours
  - *From: mdkb*

- **128GB RAM benefits**
  - Less stuttery performance, helps with multiple models and multitasking, but may have DDR5 compatibility issues
  - *From: GalaxyTimeMachine (RTX4090)*

- **ComfyUI RAM usage**
  - Can use 92GB+ system RAM on high-end systems, --disable-smart-memory --cache-none reduces to 30-40GB
  - *From: WorldX*

- **5B LoRA training VRAM**
  - Can train on 11GB VRAM with fairly large dataset and high resolution using default DP settings
  - *From: crinklypaper*

- **14B LoRA training on 3090**
  - Can train 14B LoRAs on 3090 even without blockswap, getting 2.5 samples/sec on large dataset
  - *From: crinklypaper*

- **USDU video upscaling**
  - 24fps 1080p 121 frames upscales in 30 mins on potato hardware
  - *From: mdkb*

- **5B model inference**
  - Much faster than 14B except for VAE decoding part, makes 1080p possible with 3090 without blockswap
  - *From: Hevi*

- **HuMo VRAM needs**
  - 70GB safetensors model, will need quantization for consumer GPUs
  - *From: ZeusZeus (RTX 4090)*

- **InfiniteTalk on 24GB vs 128GB**
  - If you can't do 20s IT on 24GB, you probably won't do it on 128GB. Can do 20s on 12GB with long wait time
  - *From: mdkb*

- **RTX 5090 performance**
  - Much more fun with Wan, bottleneck becomes SSD space, commit charge on Windows becomes RAM bottleneck
  - *From: Hoernchen*

- **VRAM advantage of GGUF Q4**
  - Q4 GGUF provides decent quality while leaving extra VRAM for higher resolution
  - *From: Hevi*

- **GGUF loading speed**
  - GGUF models load into VRAM quicker than fp8 versions
  - *From: Hevi*

- **HuMo RAM usage**
  - Original HuMo code requires 128GB RAM and won't start on 24GB VRAM
  - *From: Kijai*

- **VRAM usage with VACE**
  - 6GB VACE + 14GB Wan 2.2 can run on 3060 12GB VRAM with 32GB system RAM
  - *From: mdkb*

- **PyTorch version**
  - PyTorch 2.9 nightly recommended for Windows, 2.8 has torch.compile issues
  - *From: Kijai*

- **Python version**
  - Python 3.12 recommended
  - *From: Kijai*

- **Dependencies**
  - SageAttention 2.2.0, Triton 3.4, numpy <2.0
  - *From: Kijai*

- **VRAM monitoring recommended**
  - Use monitoring tools to prevent memory leaks that can crash instances
  - *From: mdkb*

- **5090 Blackwell compatibility issues**
  - Requires specific Triton compilation or precompiled wheels for proper operation
  - *From: Atlas*

- **Dependencies**
  - gguf 0.17.1, diffusers 0.35.0.dev0 needed for proper GGUF support
  - *From: Kijai*

- **InfiniteTalk memory**
  - RAM limit only for processing, not GPU VRAM dependent
  - *From: Kijai*

- **Long generation times**
  - 5 minute video takes approximately 10 hours on RTX 3090
  - *From: burgstall*

- **4 second video generation**
  - Takes 15 minutes to generate 4-second video
  - *From: Alisson Pereira*

- **4K upscaling RAM needs**
  - Around 50GB RAM needed to upscale to 4K, 2K is manageable but 4K unrealistic for most setups
  - *From: Hevi*

- **bf16 VACE VRAM usage**
  - Takes around 40GB VRAM for bf16 models, fp8 much more manageable
  - *From: Zabo*

- **RTX 3060 12GB performance**
  - Can run Q4 GGUF models but with minimal character movement and blurry lip sync
  - *From: The Coin Hunter*

- **Minimum context frames for HuMo**
  - Haven't tried under 65 frames, 30 frames works but may cause issues. Default 81 is too high for some GPUs
  - *From: Kijai*

- **Block swap memory calculation**
  - If you swap 30 blocks, 1GB LoRA ends up using 250MB more VRAM. With 40 block swap, becomes ~25MB
  - *From: Kijai*

- **RTX 3080 Ti capabilities**
  - 16GB VRAM / 64GB RAM can handle 540p Wan video generation locally
  - *From: Izaan*

- **Dual GPU setup power draw**
  - 5090 + 3090 setup pulling 550W + 350W simultaneously when running video and images at same time
  - *From: 𝕯𝖗. 𝕸𝖆𝖈𝖆𝖇𝖗𝖊 ☠*

- **RTX 3090 with 24GB considered low VRAM**
  - 24GB far from high-vram with these models
  - *From: Kijai*

- **Block swap with fp16 requires significant RAM**
  - Memory bottleneck when using fp16 precision with block swap
  - *From: Kijai*

- **Dual RTX 5090 setup needs 1KW PSU**
  - Successfully running two 5090s on 1000W power supply
  - *From: Hoernchen*

- **RTX 3060 can achieve 720p in one run**
  - Using fp8_e5m2 models with block swap enabled 720p generation
  - *From: mdkb*

- **Performance: 314.32it/s on RTX 5090**
  - Speed varies but can achieve over 300 iterations per second
  - *From: 𝕯𝖗. 𝕸𝖆𝖈𝖆𝖇𝖗𝖊 ☠*

- **VRAM usage with RTX 4070 Ti SUPER**
  - 16376 MB total VRAM, 64705 MB total RAM reported working with various models
  - *From: Gleb Tretyak*

- **RTX Pro 6000 performance**
  - Similar speed to 5090, costs just over $1/hour to rent, efficient inference speed
  - *From: Ruairi Robinson*

- **RTX 3090 FP8 compatibility**
  - RTX 3090 doesn't support fp8_e4m3fn, need e5 variants instead
  - *From: ˗ˏˋ⚡ˎˊ-*

- **HuMo VRAM usage**
  - 97 frames at 1280x720 with 6 steps uses max 7.270 GB allocated, 7.469 GB reserved
  - *From: Kijai*

- **Pusa memory impact**
  - Pusa scheduler uses significantly more VRAM - can cause OOM when used incorrectly
  - *From: Kijai*

- **Humo 1.7B VRAM**
  - Stays under 7GB VRAM for 480x832x205 frames (besides VAE decoding)
  - *From: patientx*

- **Humo fp16 model**
  - Only 3GB for fp16 version
  - *From: patientx*

- **WSL2 performance**
  - ComfyUI on WSL is good, was faster with RTX 5090, memory management improved
  - *From: pagan*

- **Torch.compile needs Triton**
  - Requires Triton installation which is not easy to setup
  - *From: Kijai*

- **First torch.compile run slower**
  - First run at any given input size slower as it compiles, subsequent runs get full benefit
  - *From: Kijai*

- **B200 GPU limited optimization**
  - Almost nothing available for B200 optimization, have to do everything by hand
  - *From: mallardgazellegoosewildcat*

- **Memory optimization trade-off**
  - Sacrificed performance on super-beefy cards with lots of VRAM in favor of lower overall VRAM usage
  - *From: 42hub*

- **Wan 14B at fp32 memory usage**
  - Would be over 100GB, considered insanity and much slower
  - *From: Kijai, samurzl*

- **Memory temperature monitoring**
  - 3080 mem temp can hit 110C easily without triggering full fan speed since fans are set on core temp only
  - *From: Kijai*

- **RAM usage independent of resolution**
  - RAM use is about model size, resolution won't affect it
  - *From: Kijai*

- **48GB VRAM considerations**
  - User will choose large enough models if memory doesn't overflow, estimates new model around 64GB
  - *From: piscesbody*

- **VRAM utilization**
  - Aim for 95% utilization for best performance, don't exceed to avoid slowdowns
  - *From: Kijai*

- **RAM for blockswap**
  - DDR4 with 128GB performs well, 4 sticks in dual channel configuration shows fast transfer times
  - *From: lostintranslation*

- **GPU comparison**
  - H100 vs 5090 depends on batch size and VRAM usage, 5090 has fp4 advantage
  - *From: mallardgazellegoosewildcat*

- **Wan character training time**
  - 1.3B model: 4 hours on user's setup, 14B would take much longer
  - *From: mdkb*

- **T5 memory usage**
  - 11GB T5 peaks at 105GB memory, Q6 quantized peaks at 95GB
  - *From: mdkb*

- **Gaussian Splats performance**
  - Can run city-scale on RTX 3060, while NeRFs need 32 H100s
  - *From: mallardgazellegoosewildcat*

- **Model size**
  - 35GB for the full model
  - *From: MysteryShack*

- **Rank 256 LoRA VRAM**
  - Takes more VRAM to load the 256 obviously
  - *From: 𝕯𝖗. 𝕸𝖆𝖈𝖆𝖇𝖗𝖊 ☠*

- **Speed difference with CFG settings**
  - Speed difference with CFG 1 vs 3.5 is 25 seconds (60s to 85s)
  - *From: Drommer-Kille*

- **VRAM usage**
  - More VRAM hungry than standard Wan 2.2 - OOM on 864x1344 where Wan 2.2 works
  - *From: scf*

- **ZeroGPU backend**
  - H200 with 141GB VRAM used in HuggingFace spaces
  - *From: Juampab12*

- **VRAM for 720p generation**
  - Takes significant resources, requires memory management
  - *From: 𝕯𝖗. 𝕸𝖆𝖈𝖆𝖇𝖗𝖊 ☠*

- **Block swap limits**
  - RTX 4090 can handle ~25 block swap for 1024x576x97, higher values cause errors
  - *From: slmonker(5090D 32GB)*

- **RAM usage for non-blocking**
  - Non-blocking block swap increases RAM usage but improves speed
  - *From: Kijai*

- **241 frames generation**
  - Successfully generated with 40 blocks on sufficient hardware
  - *From: NebSH*

- **VRAM usage for 121 frames**
  - 54985MiB / 97887MiB for 121 frames generation
  - *From: A.I.Warper*

- **VRAM usage for 1080p**
  - 78697MiB / 97887MiB trying 1080p
  - *From: A.I.Warper*

- **Block swap performance**
  - Without block swap: 120 sec/it (400x400, 77 frames), with block swap 15 and 1 prefetch: 54 sec/it
  - *From: patientx*

- **GGUF file sizes**
  - Q3_K_M version is 9.17GB, Q2_K is about 2/3 the size
  - *From: patientx*

- **VRAM for 121 frames full HD**
  - 78GB VRAM for 1080p 121 frames generation
  - *From: A.I.Warper*

- **RAM bottleneck for long generations**
  - System RAM runs out when returning 1000+ frames, not VRAM issue
  - *From: Kijai*

- **3090 compatibility**
  - Can run 16GB model on 3090 with 32GB system RAM
  - *From: Clément*

- **4070ti 12GB**
  - Getting OOM on 4070ti 12GB with Q4_K_M
  - *From: Gigi8*

- **4070ti super performance**
  - 33 second video in 20 minutes at 512x512
  - *From: Léon*

- **RTX 4070Ti 12GB + 32GB RAM**
  - 45min for 81 frames 960x528 with Q4_K_S
  - *From: Gigi8*

- **8GB RTX 3070**
  - OOM using Q4 GGUF on wan animate
  - *From: 668957627945975809*

- **RTX 5090**
  - Memory error with 81 frames at 1280x720, can do 385 frames at 720x1280 with block swap
  - *From: Ruairi Robinson*

- **8GB card**
  - Wan Animate takes 1 hour for 608x512 vid using Q8 GGUF
  - *From: xwsswww*

- **VRAM for Wan Animate**
  - Maxes out 6GB VRAM even on 13 frames, runs on 12GB but is heavy
  - *From: hicho*

- **GPU compatibility for quantization**
  - Newer than RTX 3000 series use e4m3fn, RTX 3000 and below or AMD use e5m2
  - *From: patientx*

- **WanAnimate memory usage**
  - 12GB VRAM with 32GB RAM needs 25+ block swap, 16GB VRAM works with 20 block swap
  - *From: patientx*

- **AMD GPU performance**
  - RX 6800 16GB works well, different block swap requirements than NVIDIA
  - *From: patientx*

- **High-end performance**
  - 576x1024, 144 frames took 6 minutes on 5090-class hardware
  - *From: Thom293*

- **RAM requirements**
  - SAM-2 preprocessing with ramtorch takes 128GB RAM but works on 30GB VRAM
  - *From: Benjimon*

- **VRAM usage after optimization**
  - 720x720x81 frames uses ~6GB VRAM with full block swap after recent updates
  - *From: Kijai*

- **Blackwell card optimization**
  - Dynamic torch compile reduces processing from ~500s to ~300s after initial intensive run
  - *From: Canin17*

- **12GB VRAM workflow**
  - Organized workflow optimized for 12GB VRAM / 32GB RAM
  - *From: harriet_h*

- **VRAM for 720x720, 81 frames, 6 steps**
  - Max allocated: 5.143 GB, Max reserved: 6.531 GB with fp8_scaled and 40 blocks swapped
  - *From: Kijai*

- **Generation time**
  - 1024x576 81 frames ~5min (1 min per second of video) on RTX 4080 16GB
  - *From: CaptHook*

- **VAE encoding time improvement**
  - 600px video at 24 mins on 8GB GPU with fp16 VAE
  - *From: xwsswww*

- **12GB VRAM can generate 113 frames @ 480p**
  - Maximum resolution without OOM for this VRAM level
  - *From: harriet_h*

- **12GB VRAM can do 640p with proper settings**
  - Using frame window size optimization and VAE tiling
  - *From: harriet_h*

- **6GB VRAM possible with block swap**
  - Using block swap settings allows very low VRAM usage
  - *From: Kijai*

- **Samsung 990 Pro SSD for fast model loading**
  - 3 second model loading from disk, not huge difference from 870
  - *From: Kijai*

- **24GB VRAM gets maxed out during VAE decode**
  - 24217/24576 VRAM usage during WanVideo Decode process
  - *From: Ashtar*

- **VRAM**
  - A100 42GB still OOMs with 77 frames using fp8 scaled
  - *From: gpbhupinder*

- **System RAM**
  - 389 frames at 720x1280 runs on 64GB RAM with blockswap 40
  - *From: Kijai*

- **System RAM**
  - User with 128GB RAM running out with 720p 81 frames when using bf16
  - *From: slmonker(5090D 32GB)*

- **Performance**
  - 117 frames at 480x848 completed in 4:19 on RTX 5080 16GB with 32GB RAM
  - *From: eraxor_*

- **VRAM for 393 frames at 720x1280**
  - Max 25.603 GB VRAM, 27GB reserved on RTX 5090 with 4 steps, 14 minutes generation time
  - *From: Kijai*

- **8GB VRAM performance**
  - 720p generation in 24 minutes with 30 frame context windows using block swap 40
  - *From: xwsswww*

- **6GB VRAM capability**
  - Can run Wan 14B with Q3 quantization, full block swap, and optimized wrapper nodes
  - *From: hicho*

- **12GB VRAM recommendations**
  - Q4 uses 8GB, Q5 recommended for 12GB cards with 64GB system RAM
  - *From: el marzocco*

- **RTX 3060 with 32GB RAM**
  - Can run 720p with dual model workflows, 19GB total model files, requires workflow optimization
  - *From: mdkb*

- **OOM at 367 frames**
  - 4090 with 64GB RAM hits OOM at 367 frames 1280x720, failure at image concatenate node
  - *From: Jas*

- **WAN 2.5 local inference**
  - 10s 24fps 1080p unlikely to run locally on consumer hardware
  - *From: Lumifel*

- **PyTorch 2.10 nightly for rms_norm_function**
  - Required for latest VACE module functionality
  - *From: Kijai*

- **VitPose models not heavy for inference**
  - Even largest models work fine on 16GB VRAM
  - *From: Kijai*

- **1080p generation time**
  - About 12 hours for 10 seconds on a 5090, wouldn't get full quality due to decoding limitations without tiling
  - *From: Benjimon*

- **720p generation**
  - Takes a bit of time on 3090 for 720p generation
  - *From: Rainsmellsnice*

- **720p at 24fps**
  - Will be hard to fit 10s even at 720p 24fps
  - *From: Lumifel*

- **Wan 2.2 generation capability**
  - Can generate with 12GB VRAM and 32GB system RAM
  - *From: Lodis*

- **Local generation constraints**
  - CPU only users limited to SD 1.5 1-step generations
  - *From: mallardgazellegoosewildcat*

- **13B models fit on RTX 5090**
  - HunyuanVideo 13B already fits on 5090
  - *From: mallardgazellegoosewildcat*

- **Video models don't need more than 30B parameters**
  - Waver 1.0 is 12B and performs at Veo3 level, scaling beyond 30B is considered useless
  - *From: yi*

- **VRAM for WanAnimate generation**
  - Max allocated memory: 26.077 GB, Max reserved: 27.656 GB for 209 frames
  - *From: Kijai*

- **GPU for style mixing example**
  - Used RTX 4090 when creating the 2D/3D style mix example
  - *From: ingi // SYSTMS*

- **Video LoRA training VRAM**
  - RTX Pro 6000 needed for 5s 16fps video training, spikes to 89/92 GB
  - *From: fearnworks*

- **RTX 3090 performance**
  - 720p 97 frames 17 steps takes 45 minutes for 7 second clip at 14fps, maxes out 24GB VRAM
  - *From: Splicer*

- **Cloud training costs**
  - Around $2 for training LoRA depending on parameters, Vast.ai about 30% cheaper than Runpod
  - *From: Hevi*

- **TaylorSeer-Lite VRAM usage**
  - Nearly zero VRAM increase, 3.05x speedup on RTX 5090 for 81 frames
  - *From: scf*

- **WanVideoWrapper VRAM management**
  - 96GB VRAM user experienced issues with newer versions requiring offload_device setting
  - *From: yo9o*

- **MagiAttention GPU compatibility**
  - Recommended for Hopper architecture GPUs (H100/H800), not necessary for non-Hopper GPUs
  - *From: mallardgazellegoosewildcat*

- **Lynx full model VRAM**
  - Around 18-19GB VRAM in fp8, 4GB larger than base model
  - *From: Kijai*

- **Wan 2.5 VRAM requirements**
  - Significantly more VRAM needed for 1080p 10 second videos, final requirements unknown
  - *From: Izaan*

- **Qwen Image generation time**
  - About 40 seconds with RTX 5090
  - *From: Drommer-Kille*

- **FILM VFI interpolation speed**
  - 80 seconds to interpolate 49 frames at 1024x768 resolution
  - *From: mamad8*

- **WAN 2.2 model loading**
  - Single 5090: ~44 seconds, dual 5090: 65-80 seconds with 128GB RAM and 990 NVME
  - *From: Baku*

- **Dual 5090 power consumption**
  - Requires separate 1600W PSU for GPUs plus 600W for rest of system, can trip 15amp breakers
  - *From: Baku*

- **GPU heat generation**
  - Room temperature increases 5 degrees with 4090+5090 running, like a sauna
  - *From: Thom293*

- **RAM for model swapping**
  - 768GB RAM eliminates OOM when swapping WAN 2.2 models
  - *From: Doctor Shotgun*

- **Hunyuan Image v3 memory requirements**
  - 160GB model size, 80B params with 13B active, needs 768GB RAM and 96GB VRAM according to one user's speculation
  - *From: Doctor Shotgun*

- **InfiniteTalk 20 hour run showed degradation after 4 minutes**
  - 6+ minutes of speech total, gradual degradation starts at 4min mark
  - *From: burgstall*

- **Rank 256 lora is 2.5GB**
  - High memory cost for proper extraction
  - *From: Kijai*

- **H100 performance comparison**
  - H100 delivers 756 tflops fp16 vs 5090's 209 tflops. LongLive achieves 20.7 FPS on H100, 24.8 FPS with FP8 quantization
  - *From: Benjimon*

- **Sage Attention 3**
  - Requires 50 Blackwell GPUs (5xxx series cards)
  - *From: toyxyz*

- **720p generation on 3060**
  - Struggling to achieve 720p on RTX 3060, needs to use tiled embeds and lower settings
  - *From: mdkb*

- **VRAM for WanAnimate**
  - Difficulty achieving 720p, craps out around 600p taking >40 mins on lower VRAM cards
  - *From: mdkb*

- **High-end hardware for new models**
  - 5K series cards recommended at minimum for working with new models properly
  - *From: Gleb Tretyak*

- **4090 specs for WanAnimate**
  - 4090 with 80GB RAM using Q8 GGUF model runs more smoothly
  - *From: Gill Bastar*

- **LongLive real-time requirements**
  - Needs 4xH100 for the real-time part
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Memory issues with longer videos**
  - 30 blocks swapped on low sampler process causes OOM
  - *From: Kenk*

- **Real-time performance with Wan 1.3B**
  - 0.65x real-time speed on 1 H100
  - *From: ˗ˏˋ⚡ˎˊ-*

- **Large memory usage for big resolution/frame count**
  - Running into OOMs with large resolution, large frame count things, especially when using big kernel lanczos during upscaling
  - *From: stenandrimpy*

- **Wan 2.2 VRAM**
  - Can run on iGPU technically, needs 2-3GB VRAM in theory for a block and latents
  - *From: Juampab12/Draken*

- **12GB VRAM**
  - Considered blockswap territory for Wan, 16GB also workable
  - *From: mallardgazellegoosewildcat*


## Community Creations

- **Custom dark theme with red elements** (theme)
  - Extreme dark theme for users with photophobia, though readability questioned
  - *From: l҈u҈c҈i҈f҈e҈r҈*

- **LoRA Resize Node** (node)
  - Node to resize LoRAs with dynamic averaging to reduce file size
  - *From: Kijai*

- **Enhanced caching node pack** (node)
  - Modified node pack for easier prompt/condition saving and loading with naming system
  - *From: patientx*

- **Video chaining workflow** (workflow)
  - Generates and chains several videos to create one long video
  - *From: WorldX*

- **Infinite Talk + MagRef workflow** (workflow)
  - Combines lip-sync with character consistency for video generation
  - *From: VRGameDevGirl84(RTX 5090)*

- **Batch cache clearing script** (tool)
  - Windows batch script to clear triton and torchinductor caches
  - *From: Ablejones*

- **LoRA Resize Node** (node)
  - Added to KJNodes, can reduce LoRA size by half with only 5% effect loss
  - *From: Kijai*

- **Multi-prompt extension workflow** (workflow)
  - Workflow for extending videos using context windows and multiple prompts
  - *From: Dever*

- **Video to PNG batch processor** (workflow)
  - System to run multiple jobs then combine PNGs into long video with toggle activation
  - *From: Kenk*

- **Modified panda workflow for Wan 2.2 I2V** (workflow)
  - Context window workflow adapted from T2V panda example
  - *From: Ashtar*

- **Multiple image I2V implementation** (feature)
  - Support for batch images in context windows
  - *From: Kijai*

- **Wan 2.2 rapid AIO and chroma AIO** (model)
  - All-in-one models created for Wan 2.2
  - *From: Phr00t*

- **Multi-image context workflow** (workflow)
  - Allows setting individual start frames for each context window and end image
  - *From: Dever*

- **Music video using Wan 2.2** (video)
  - Full-length music video created using Wan 2.2 with various techniques
  - *From: VRGameDevGirl84(RTX 5090)*

- **Custom LoRA for keyframes** (lora)
  - Experimental LoRA to generate key frames for much longer generations than 5 seconds, still in development with quality issues
  - *From: mamad8*

- **Pusa extension node** (node)
  - Node for extending T2V videos using Pusa with configurable noise multipliers
  - *From: Kijai*

- **Per-block control visualization** (workflow)
  - Experimental setup showing latent after each block for learning and fine-grained control
  - *From: Kijai*

- **Block strength node concept** (node)
  - A block strength node for the model itself like model merge nodes, but not necessarily to blend models together
  - *From: ingi // SYSTMS*

- **Sigma graphs visualization** (tool)
  - Visual representation of sigma values during generation process
  - *From: Kijai*

- **Asian ethnicity LoRA** (lora)
  - LoRA trained on Asian subjects, though discussion suggests base model may be sufficient
  - *From: Ryzen*

- **Extension workflow rework** (workflow)
  - Reworked Benji's extension method for the wrapper with modifications
  - *From: N0NSens*

- **Multi-stage workflow with merged LoRAs** (workflow)
  - Converting models with LoRAs merged into GGUF format for better VRAM efficiency
  - *From: patientx*

- **Magref workflow** (workflow)
  - Cleaner implementation than wrapper examples, works straight out of the box
  - *From: Dr. Macabre*

- **Something to String node** (node)
  - Replacement for missing Int To String node, can convert int to string
  - *From: Kijai*

- **Chinese prompt generator translation** (node)
  - English translation of Chinese prompt generator node interface
  - *From: hicho*

- **Video upscaling workflow** (workflow)
  - 4K upscaling with flickering fix using subgraphs
  - *From: FL13*

- **Context window workflow** (workflow)
  - Different input images per sequence for longer videos
  - *From: Ashtar*

- **Music video with InfiniteTalk** (video)
  - YouTube music video created using Wan models with InfiniteTalk for lip sync
  - *From: VRGameDevGirl84(RTX 5090)*

- **Tiled SEGS detailer workflow** (workflow)
  - Modified Impact-Pack for video compatibility with SEGS detailer nodes
  - *From: Ablejones*

- **Three sampler I2V workflow** (workflow)
  - Custom workflow using 3 ksamplers with different LoRAs for improved dynamics
  - *From: .: Not Really Human :.*

- **Automated music video custom node** (node)
  - Automates exact scene timing with padding for InfiniteTalk workflows
  - *From: VRGameDevGirl84(RTX 5090)*

- **Silent embed loading system** (tool)
  - Pre-encoded silence for padding InfiniteTalk audio
  - *From: Kijai*

- **Tile SEGS for video** (node)
  - Video segmentation currently in fork, PR planned when ready
  - *From: Ablejones*

- **Dynamic InfiniteTalk scene node** (node)
  - Allows multiple scenes with automatic duration handling, creates dynamic outputs like endless travel
  - *From: VRGameDevGirl84(RTX 5090)*

- **English translation of Wan prompt generator** (node)
  - Translated Chinese prompt generator to English for better accessibility
  - *From: asd*

- **Low-VRAM workflow pack** (workflow)
  - Complete pack for generating Wan2.1 videos and Flux images with limited VRAM
  - *From: Akumetsu971*

- **VACE SEGS detailer integration** (workflow)
  - Integration of VACE with SEGS detailer for video upscaling and enhancement
  - *From: Ablejones*

- **Magix nodes** (nodes)
  - Custom nodes for video processing and extension workflows
  - *From: samhodge*

- **VACE + Wan 2.2 merge** (model)
  - Custom merge of VACE with Wan 2.2 for extended video generation
  - *From: JohnDopamine*

- **WAN String Select LoRA** (node)
  - Node that allows selecting LoRA based on string with partial match support
  - *From: Kijai*

- **Color shift correction for InfiniteTalk** (node)
  - Added option to InfiniteTalk sampling to correct color shifting issues
  - *From: Kijai*

- **Image Batch Repeat Interleaved** (node)
  - Node for inserting images/frames into batch with intervals, useful for VACE interpolation
  - *From: Kijai*

- **Wan 2.2 upscaler workflow** (workflow)
  - Standalone upscaler using 2.2 low model with UltimateSD Upscaler, faster than original implementations
  - *From: FL13*

- **VACE upscaling workflow** (workflow)
  - Alternative upscaler using Wan 2.1 VACE for up to 2K resolution
  - *From: FL13*

- **Native Infinite Talk implementation** (node)
  - ComfyUI core integration for continuous lip-sync generation, faster than context windows
  - *From: Kijai*

- **Uni3C wrapper updates** (node)
  - Enhanced to work with T2V and VACE, auto-interpolates input to match generation frame count
  - *From: Kijai*

- **USDU upscaler workflow for 3060** (workflow)
  - Video upscaling solution for lower VRAM cards using segment processing
  - *From: mdkb*

- **SEGS detailer fork for VACE+Phantom** (tool)
  - Modified Impact-Pack fork that works with VACE and Phantom, nearly ready for PR
  - *From: Ablejones*

- **USDU video upscaler workflow** (workflow)
  - Non-upscaling USDU node workflow using 1080p pre-upscaled video for t2v denoise polish
  - *From: mdkb*

- **WanVideoWrapper HuMo branch** (node)
  - ComfyUI implementation of HuMo model with new node structure
  - *From: Kijai*

- **SeedVR2 blockswap node** (node)
  - Better memory management for SeedVR2 upscaling
  - *From: Adrien Toupet*

- **Fun VACE module conversions** (model)
  - Kijai converted original Fun VACE to multiple formats: bf16, fp8, GGUF with various quantization levels
  - *From: Kijai*

- **Endless time travel workflow adaptation** (workflow)
  - Modified existing endless time travel workflow to work with Wan 2.2 Fun VACE
  - *From: Cseti*

- **HuMo ComfyUI support** (node)
  - Provisional support for HuMo audio-reactive model in ComfyUI
  - *From: Alisson Pereira*

- **VACE 2.2 GGUF conversion** (model)
  - GGUF versions of VACE 2.2 for easier loading
  - *From: Kijai*

- **Custom LLM for Wan support** (tool)
  - LLM trained on wan_chatter channel discussions for technical support
  - *From: JohnDopamine*

- **HuMo GGUF quantizations** (model)
  - Community-created GGUF versions of HuMo with selective layer quantization
  - *From: Alisson Pereira*

- **SAM2 video segmentation workflow** (workflow)
  - Points editor node with SAM2 for better video object masking
  - *From: Zuko*

- **VACE upscale workflow** (workflow)
  - Upscale from 1024x576 to 2880x1616 with excellent results
  - *From: T2 (RTX6000Pro)*

- **Load Images from Path node** (node)
  - Loads folder of images as image batch for video processing
  - *From: Kijai*

- **Context window frame saving** (feature)
  - Can now save individual frames from each context loop to folder
  - *From: Kijai*

- **VACE 2.2 workflow template** (workflow)
  - Essential workflow template for VACE 2.2 with KJ's loaders, 3 samplers, reference image and ControlNet
  - *From: Vérole*

- **WanVideoVACEStartToEndFrame node** (node)
  - Node for start/end frame processing in VACE workflows, requires start or end frame input
  - *From: Kijai*

- **Context window + Uni3C workflow** (workflow)
  - Combined workflow for long generation with better motion than InfiniteTalk
  - *From: Kijai*

- **After Effects inpainting script** (tool)
  - LLM coded AE script for creating inpainting movable regions inside compositions to do inpaint on faces or persons at full resolution
  - *From: SonidosEnArmonía*

- **Grain LoRA for Wan 2.1** (lora)
  - Film grain effect LoRA in development, needs more training
  - *From: Drommer-Kille*

- **Job Manager UI** (tool)
  - Creates organized project structure with numbered shots and custom ComfyUI batch files
  - *From: T2 (RTX6000Pro)*

- **Wan2.2 Mega AIO** (model)
  - Combined model with VACE/WAN 2.2/SkyReels/FunReward/umt5/vae in single checkpoint
  - *From: Phr00t*

- **Tiled sampling workflow for Wan wrapper** (workflow)
  - Workflow to achieve upscaling with tile-based approach using Wan wrapper
  - *From: FL13*

- **Endless HuMo workflow** (workflow)
  - Custom nodes and workflow for creating long-form HuMo videos with scene switching and audio synchronization
  - *From: VRGameDevGirl84(RTX 5090)*

- **Custom audio splitting nodes** (node)
  - Nodes that split audio and combine videos for multi-scene generation
  - *From: VRGameDevGirl84(RTX 5090)*

- **Wan 2.2 VACE User Guide** (guide)
  - Guide created from stream content using Gemini to make 1 hour video skimmable
  - *From: Nathan Shipley*

- **Video chunking workflow** (workflow)
  - Segmenting control video into chunks for unlimited length with Wan2.2 VACE
  - *From: Gleb Tretyak*

- **HuMO endless workflow** (workflow)
  - Splits long videos into groups to bypass 97 frame limit for lip sync
  - *From: VRGameDevGirl84(RTX 5090)*

- **Video and audio splitter nodes** (node)
  - Splits up video and audio for processing workflows
  - *From: VRGameDevGirl84(RTX 5090)*

- **Radial attention auto-setter** (node)
  - Custom node to auto set nearest valid token values for length and resolution in radial attention
  - *From: hudson223*

- **Seconds to string converter** (node)
  - Node for converting seconds to string format
  - *From: Dita*

- **WAN 2.2 Mega Merge** (model)
  - All-in-one version combining low model + VAE + CLIP with VACE for T2V, I2V, and FFLF capabilities
  - *From: Phr00t*

- **WAN fill color node** (node)
  - Creates solid color images, can use decimals
  - *From: Kijai*

- **Cached text encoder replacement** (node)
  - Zero memory impact text encoder that removes whole model when done
  - *From: Kijai*

- **Insert empty frames nodes** (node)
  - Multiple nodes for inserting empty frames, including ones that put empty frames in between existing frames
  - *From: Kijai*

- **ModelHunter** (tool)
  - Web tool for inspecting JSON workflow files and generating Google search links for missing models
  - *From: Quality_Control*

- **Automated Humo workflow** (workflow)
  - Integration of Gemini LLM with Humo for automatic prompt generation from reference images and lyrics
  - *From: VRGameDevGirl84(RTX 5090)*

- **Mask transformation node** (node)
  - Node to transform mask to Wan-animate style since normal masks don't work
  - *From: Kijai*

- **WanAnimate ComfyUI wrapper** (node)
  - Initial native WanAnimate implementation and wrapper for ComfyUI
  - *From: Kijai*

- **FP8 repackaged model** (model)
  - ComfyUI repackaged version in FP8 format
  - *From: Cubey*

- **MattAnyone Node Template** (workflow)
  - Alternative to DWPose for pose detection
  - *From: JohnDopamine*

- **WanVideoWrapper** (node)
  - ComfyUI implementation of Wan video models with windowing support
  - *From: Kijai*

- **VHS preset for frame counting** (workflow)
  - Preset that helps with proper frame count calculation for Wan models
  - *From: ˗ˏˋ⚡ˎˊ-*

- **WanAnimate GGUF conversion script** (tool)
  - Scripts for converting WanAnimate to GGUF format with motion and face blocks excluded
  - *From: Kijai*

- **Linear Quadratic Scheduler** (node)
  - Custom scheduler with inflection_percent and threshold_noise parameters for low step count control
  - *From: Ablejones*

- **Point Tracker Custom Node** (tool)
  - Custom node for tracking points and creating masks in ComfyUI
  - *From: traxxas25*

- **WanAnimate GGUF quantizations** (model)
  - Q2, Q3, Q4_0 quantized versions of WanAnimate 14B
  - *From: The Punisher*

- **Radial Length Helper** (node)
  - Auto snaps resolution and length to nearest valid values, gives list of valid lengths
  - *From: hudson223*

- **WanAnimate native workflow** (workflow)
  - Native ComfyUI implementation workflow
  - *From: Vérole*

- **Resolution helper node** (node)
  - Helps calculate valid resolutions where width * height * frames is divisible by 16
  - *From: patientx*

- **Parameter sweep for NAG** (workflow)
  - Demonstrated NAG sampler parameter effects and artifacts
  - *From: Kijai*

- **GGUF quantized WanAnimate models** (model)
  - q3, q4, q6, fp8_e5m2 quantizations for memory efficiency
  - *From: patientx*

- **Modified Qwen2.5VL masking node** (node)
  - Faster and smarter masking with automatic model unloading
  - *From: piscesbody*

- **LatestVideoFinalFrame custom node** (node)
  - Extracts final frame from previously exported video for auto-running workflows
  - *From: Flipping Sigmas*

- **Custom utility node for number counting** (node)
  - Alternative to was nodes number counter for workflow continuity
  - *From: Flipping Sigmas*

- **Quasi monte carlo seed management** (node)
  - Seed bank node that generates multiple seeds efficiently using quasi monte carlo exploration
  - *From: mallardgazellegoosewildcat*

- **Optimized WanAnimate workflow** (workflow)
  - Organized workflow optimized for 12GB VRAM / 32GB RAM with purple color coding
  - *From: harriet_h*

- **WanVideoWrapper** (node)
  - Kijai's ComfyUI wrapper for WAN video models
  - *From: Kijai*

- **Block swap prefetch optimization** (feature)
  - Makes block swapping only 0.01 per block longer
  - *From: Draken*

- **WanAnimatePreprocess** (tool)
  - Preprocessing tool for Wan Animate workflows
  - *From: Kijai*

- **Lucy Edit support in wrapper** (node)
  - Added support for Lucy Edit model in existing wrapper
  - *From: Kijai*

- **WanAnimatePreprocess** (node)
  - Automated pose and face detection preprocessing for Wan Animate
  - *From: Kijai*

- **Wan 2.2 Animate Workflow for 12GB VRAM** (workflow)
  - Optimized workflow for low VRAM cards, generates 113 frames @ 640p in under 10min
  - *From: harriet_h*

- **WanVideoWrapper** (node)
  - Optimized wrapper for Wan models with memory improvements and context window support
  - *From: Kijai*

- **Wan Animate Preprocess nodes** (node)
  - Preprocessing nodes for cleaner face transfer and better eye quality in Wan Animate
  - *From: Kijai*

- **FastWan LoRA** (lora)
  - Enables 2-step generation when combined with LightX LoRA
  - *From: Kijai*

- **ComfyUI-WanAnimatePreprocess** (node)
  - Preprocessor nodes for facial capture and pose capture
  - *From: Kijai*

- **Python script for .pt to safetensors conversion** (script)
  - Converts self-forcing .pt models to safetensors format by extracting generator_ema
  - *From: Kijai*

- **WanVideoWrapper update** (node)
  - Kijai working on wrapper support for new WAN models
  - *From: seitanism*

- **Regional Adaptive Sampling WAN support** (tool)
  - Experimental WAN support added for inference acceleration
  - *From: JohnDopamine*

- **WanAnimatePreprocess** (node)
  - Pose detection and drawing nodes for Wan Animate with improved hand detection
  - *From: Kijai*

- **Draw ViT Pose Node** (node)
  - Separate detection and drawing nodes for pose preprocessing
  - *From: Kijai*

- **Successful LoRA training** (lora)
  - 7000 steps on 50 detailed captioned images using rank 64, generates different people instead of same face
  - *From: Ryzen*

- **Hand animation LoRA for 2.2** (lora)
  - Hand animation LoRA retrained for Wan 2.2, works well but needs reference image to prevent snapping back every 81 frames
  - *From: ingi // SYSTMS*

- **WanAnimatePreprocess nodes** (node)
  - Better preprocessing for WanAnimate, way better than current preproc
  - *From: Kijai*

- **Rescale nodes for DWPose** (node)
  - Could potentially improve pose retargeting cases, though compatibility with vitpose unclear
  - *From: Nekodificador*

- **Causvid v2** (lora)
  - Speed LoRA used with wan 2.1 + VACE
  - *From: Neex*

- **LightX2V** (lora)
  - Amazing speed LoRA for 2.1
  - *From: Kijai*

- **Phantom/MagRef merge** (workflow)
  - VACE/phantom merge workflow
  - *From: Piblarg*

- **WanVideoWrapper** (node)
  - Kijai's ComfyUI implementation for Wan models
  - *From: system*

- **MultiGPU node** (node)
  - Allows running VACE with limited VRAM, works with wrapper
  - *From: SonidosEnArmonía*

- **Image Randomizer node** (node)
  - Updated to support videos for batch processing directories
  - *From: JohnDopamine*

- **Humo extension support pull request** (code contribution)
  - Added extension capability to Humo for native ComfyUI, under review
  - *From: Ablejones*

- **VACE production pipeline guide** (tutorial)
  - Detailed YouTube guide for using VACE in commercial projects with embroidery/fabric details
  - *From: Izaan*

- **Kijai's Lightning LoRA conversion** (lora)
  - Converted Lightning LoRAs with proper ComfyUI key naming (diffusion_model. prefix) and fp16 format
  - *From: Kijai*

- **Custom LoRA key conversion script** (tool)
  - Script to convert LoRA key naming schemes for compatibility
  - *From: Screeb*

- **Kijai's fp8 scaled dyno model** (model)
  - fp8 quantized version of dyno model with improved naming convention
  - *From: Kijai*

- **JohnDopamine's timestep embeddings extraction** (model component)
  - 360mb safetensors file containing time_embeddings to improve lora performance
  - *From: JohnDopamine*

- **Flash attention wheel** (tool)
  - Custom built flash_attn-2.7.4.post1 wheel for torch 2.8 compatibility (took 6 hours to build on Windows)
  - *From: TK_999*

- **Livewallpaper LoRA** (lora)
  - Completely removes mouth jabbering but heavily affects general motion
  - *From: CFSStudios*

- **Anime Sex Face LoRA** (lora)
  - Helps reduce mouth jabbering with less effect on motion than livewallpaper LoRA
  - *From: CFSStudios*

- **Palingenesis Model** (model)
  - Wan 2.2 variant that shows improved results for certain styles
  - *From: Gill Bastar*

- **Wan alpha workflow using 2.2 t2v** (workflow)
  - Workflow for generating alpha channel videos
  - *From: mrassets*
