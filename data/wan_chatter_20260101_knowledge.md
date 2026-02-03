# Wan Chatter Knowledge Base
*Extracted from Discord discussions: 2026-01-01 to 2026-02-01*


## Technical Discoveries

- **Merging LoRA with fp8 model workflow**
  - Load model => load lora (like normal workflow) => save model - much easier than expected
  - *From: pagan*

- **SVI Pro difference augmentation for longer videos**
  - Can generate coherent videos up to 241 frames without running back by using scheduled difference augmentation on frames beyond typical 81 frames
  - *From: Ablejones*

- **SVI memory efficiency improvement**
  - Setting length to 65fps instead of 81 for each clip makes generation super fast and uses less VRAM
  - *From: Elvaxorn*

- **VAE decode yellowing fix**
  - Wan's VAE requires large/full temporal window - switch from tiled VAE decode to normal VAE decode to prevent yellowing/banding
  - *From: ucren*

- **1022 LoRA training base**
  - The wan2.2_i2v_A14b_low_noise_lora_rank64_lightx2v_4step_1022.safetensors was actually trained on wan 2.1 model, causing 170 key mismatch
  - *From: Benjimon*

- **SageAttention speedup increases with generation size**
  - User confirmed that SageAttention2 provides better performance improvements on larger generation sizes
  - *From: Lumifel*

- **RTX 5090 performance baseline established**
  - 49 minutes for 15 videos (81 frames each, 720x1280, 6 steps) - approximately 3 minutes per video
  - *From: 42hub*

- **SVI Pro has slowmotion tendency by design**
  - SVI by nature is biased towards less motion because of the anchor frame - it's always trying to get back to the anchor frame for consistency
  - *From: Ablejones*

- **Text encoder replacements can change model behavior without retraining**
  - Changing text encoders CAN make different behaviors even if model doesn't understand new tokens - retrained Qwen3 models work as replacements for same size models
  - *From: Scruffy*

- **MLP layers are sensitive to quantization in some models**
  - With LongCat, doing MLP in fp8 ruined quality completely. Wan 2.1 had crazy quality hit with fp8 matmuls on MLP but largest speed increase. Wan 2.2 seems fine with it
  - *From: Kijai*

- **VAE precision bug returns on PyTorch 2.11.0**
  - Cannot decode 640x640x81, affects both wrapper and native implementations
  - *From: Gleb Tretyak*

- **fp32 VAE decoding uses less memory than bf16 when conv3d bug is active**
  - fp32 is 2x memory use but the bug causes 3x, so fp32 is actually better
  - *From: Kijai*

- **Flash attention works on ROCm and Windows now**
  - Does small compiling with triton at first use, memory usage is lower, works with wan wrapper when flash-attention is selected
  - *From: patientx*

- **LongVie2 provides depth controlnet for I2V models**
  - Only depth controlnet available for I2V models, uses depth/spatracker tracks controlnet and can continue from 8 frames
  - *From: Kijai*

- **SVI 2.0 Pro uses anchor latent to mitigate degradation**
  - The degradation was never about encode-decode process, it's natural with these models, anchor latent in SVI mitigates this
  - *From: Kijai*

- **MoE ksampler ensures proper timestep split**
  - Makes sure time step split between high and low model is exactly 0.875 (standard), especially important for LoRAs limited to those timesteps
  - *From: ingi // SYSTMS*

- **CLIP Vision Tiling improves image-to-video accuracy**
  - Breaking images into tiles allows CLIP vision to see more detail since it's capped at 256x256. Setting to 2 tiles sees 512x512 (2 tiles = 2x2 tiles essentially)
  - *From: ingi // SYSTMS*

- **WanAnimate face detection is more stable than LivePortrait's facecropper**
  - LivePortrait's facecropper has trouble stabilizing head rotation and scale causing artifacts. WanAnimate's face detection is far more stable and produces less jittery results when used as driving video
  - *From: David Snow*

- **LTX-2 works as fast Wan upscaler**
  - 1080p Wan upscale tests using LTX-2 take just over a minute each using v2v workflow. Need to reduce lora strength as it adds too much detail
  - *From: David Snow*

- **Wan 2.2 low-noise model can run standalone**
  - You can use lownoise 2.2 model only if you cant fit both high and low in ram. Works better than 2.1 but real difference is using both models. 2.1 is very similar to 2.2 low
  - *From: Blink*

- **Sage made huge improvement for LTX-2, torch compilation didn't notice much difference**
  - SageAttention provided significant performance boost while torch compilation had minimal impact
  - *From: psylent_gamer*

- **FP8 numbers are discrete sets, not continuous like traditional floats**
  - Only 256 numbers with big range split into bands, mantissa determines granularity between bands
  - *From: phazei*

- **Pytorch uses caching system to avoid expensive GPU driver allocations**
  - Pytorch maintains cache of memory allocated from CUDA driver and sub-allocates from this cache to avoid constant driver-level allocations
  - *From: mallardgazellegoosewildcat2*

- **Skip final model call can reduce inference time by 20% for low-step generations**
  - For 4-step generations, skipping final model call saves 20% time with practically no quality loss
  - *From: Ablejones*

- **VRGameDevGirl84 created a beat-locked auto video editor**
  - Gradio app that automatically edits multi-camera video footage to music by analyzing rhythm, energy, and structure. Uses stems to decide shots and locks cuts to musical beats.
  - *From: VRGameDevGirl84(RTX 5090)*

- **Mocha only uses single mask that propagates automatically**
  - Mocha uses a single frame mask and propagates it automatically to the whole video, not a multi-frame mask
  - *From: Kijai*

- **Can't run HuMo and SCAIL simultaneously**
  - You can run HuMo as a second pass but not at the same time in the same latent with SCAIL
  - *From: Dream Making*

- **VACE only works with T2V models**
  - VACE cannot be used with I2V models like SVI
  - *From: Kijai*

- **SVI anchor frame should be first frame for coherent generation**
  - The anchor latent should be the first frame to get a coherent image, not the last frame
  - *From: pagan*

- **SVI Pro 2.2 can work as a LoRA with strength values 0.7/0.5**
  - User tested SVI weight at 0.7 and 0.5 with good results for video extension
  - *From: Dream Making*

- **ComfyUI now has asynchronous weight offloading**
  - ComfyUI offloads unused weights to RAM and juggles active weights between VRAM/RAM asynchronously, so if step compute time is long like with video models, weight moving may not slow it down
  - *From: Kijai*

- **Wan 2.2 FP16 can run on 16GB VRAM despite 53GB model size**
  - Due to ComfyUI's asynchronous offloading system that manages weights between VRAM and RAM
  - *From: SantaHunter*

- **Face similarity should be part of loss function when training LoRAs**
  - Would improve face preservation in LoRA training, described as 'crazy that people don't do that'
  - *From: mallardgazellegoosewildcat2*

- **Embedding training on Wan 1.3B can transfer to other Wan versions**
  - Since Wan uses same text encoder for all versions, embeddings trained on 1.3B with small images could transfer to larger models
  - *From: spacepxl*

- **Block swap can improve speed even with smaller quants**
  - User reported 10% speed improvement using block swap with q4/q3 models, even when GPU has enough VRAM
  - *From: patientx*

- **Wrapper version 1.4.0 changed T2V outputs**
  - After version 1.4.0, T2V generates different outputs with better prompt adherence and more detailed results, but lightx LoRAs may need rebalancing
  - *From: garbus*

- **NAG memory optimizations implemented**
  - NAG node updated with optional inplace memory saving optimizations that reduce VRAM usage significantly but may slightly change output
  - *From: Kijai*

- **StoryMem RoPE implementation was incomplete**
  - Original StoryMem repo was missing RoPE offset implementation in code despite mentioning it in paper, recently fixed in latest commit
  - *From: Kijai*

- **WanVideo Apply NAG is not supported with Wan 2.1**
  - Removing WanVideo Apply NAG made workflow work with Wan 2.1, though it works fine with Wan 2.2
  - *From: Juan Gea*

- **Wan distilled loras work best with shift=5**
  - They were trained with shift=5, and in general shift depends on resolution - higher resolution needs higher shift due to relationship between resolution, noise level, and signal to noise ratio
  - *From: spacepxl*

- **SVI 2.0 Pro can continue from latent directly without decode/encode**
  - This is one of its main features and preserves more detail than saving to disk and reloading
  - *From: Kijai*

- **Every diffusion/flow model can be img2img or vid2vid with inpainting and masks**
  - This is a result of how the models work mathematically, but requires correct code tools/nodes to take advantage
  - *From: mallardgazellegoosewildcat2*

- **SCAIL has 3D pose data**
  - Unlike VACE which was possible before, SCAIL provides better pose control with 3D data
  - *From: Juampab12*

- **VHS Load Video (FFmpeg) avoids color shift**
  - VHS normal loader uses opencv and causes pink/magenta color drift, while FFmpeg version maintains accurate colors like native
  - *From: CaptHook*

- **Self-refine-video technique implemented for Wan models**
  - Uses restart sampling with uncertainty masking to improve video quality, requires 50% more compute time but produces better results
  - *From: Kijai*

- **Color shift issue identified in VHS video loading nodes**
  - VHS Load Video and Native Load Video produce color drift when loading videos, only VHS FFmpeg Load Video preserves correct colors
  - *From: lostintranslation*

- **SageAttn provides ~90% quality with 2x speedup**
  - Using SageAttn attention mechanism gives substantial speedup with minimal quality loss, especially when combined with distill LoRAs
  - *From: Kijai*

- **New UniVerse-1-Base model released**
  - Ovi-style model trained on Wan 2.1 1.3B, uses ace-step instead of mmaudio, but appears undertrained
  - *From: yi*

- **SkyReels V3 R2V model looks identical to T2V model with no new layers**
  - The R2V architecture appears to be the same as standard T2V models
  - *From: Kijai*

- **SkyReels V3 R2V model supports 4 reference images maximum**
  - Model pads with empty slots for unused reference images, max is 4
  - *From: Kijai*

- **SkyReels V3 default frame count is 121 for R2V**
  - Formula is num_frames = duration * 24 + 1, default 121 frames for R2V
  - *From: Kijai*

- **SkyReels V3 model appears to be distilled**
  - Model behavior suggests it's a distilled version, explains performance differences
  - *From: Kijai*

- **MOVA is essentially Wan 2.2 A14B with audio, not 32B**
  - Uses two models like Wan 2.2, fully runnable on consumer GPUs, basically Ovi scaled to Wan 2.2
  - *From: yi*

- **SkyReels V3 consists of 4 different models**
  - Includes talking avatar, shot model for extending with new shots, extend model, and multitalk weights
  - *From: Kijai*

- **MOVA supports multi-shot and has better character consistency**
  - Model has better VAE, sound, Apache license, smaller text encoder
  - *From: yi*

- **Double distillation can cause excessive CFG-like effects**
  - Loading LightX2V on top of already distilled model creates artifacts
  - *From: mallardgazellegoosewildcat2*

- **Self-Refine is available in testing branch for WanVideoWrapper**
  - Kijai has self-refine for wrapper in early testing stages on separate branch, see self-refine-video branch
  - *From: izashin*

- **MOVA requires significant VRAM**
  - Eats ~55 GB VRAM for 94 frames 720p with memory option 'cpu' and 'bfloat16'. 72 GB VRAM / 45 GB RAM for 193 frames
  - *From: Stef*

- **MOVA performs scene cuts spontaneously**
  - MOVA made scene cuts without prompting them in the generation
  - *From: Stef*

- **Skyreels Extend model is based on Wan 2.1 720p**
  - Compared tensors and it's almost same as the base 720p model with some distill lora added, very similar to lightx2v
  - *From: Kijai*

- **TalkingAvatar is 95% multitalk code**
  - Whole model code is multitalk but they don't credit it anywhere
  - *From: Kijai*

- **NVFP4 conversion of Wan 2.2 i2v high reduces model size from 28GB to 7.8GB in 45 seconds**
  - Conversion completed on 5090, but models are very lossy - proper NVFP4 models need calibration
  - *From: topmass*

- **NVFP4 models provide 30% faster generation after load**
  - 4-step LoRA NVFP4 working fine with 81 frames at 24fps
  - *From: topmass*

- **MOVA is only 1-2 seconds slower per iteration compared to Wan 2.2 a14b**
  - Performance tested over in different channel
  - *From: yi*

- **Audio models are much smaller than video models**
  - Audio to video cross-attention slows it down a bit but audio itself is fast
  - *From: Kijai*


## Troubleshooting & Solutions

- **Problem:** VAE decode causing yellowing/banding in videos
  - **Solution:** Switch from tiled VAE decode to normal VAE decode - wan's VAE requires large/full temporal window
  - *From: ucren*

- **Problem:** SVI causing yellowing after first frame
  - **Solution:** Issue is with zero frame scaling in VAE - SVI uses real zero frames for I2V conditioning and ComfyUI scales them after concat
  - *From: Kijai*

- **Problem:** 170 key mismatch with 1022 low noise LoRA
  - **Solution:** LoRA was trained on wan2.1 model, not wan2.2 - use appropriate base model
  - *From: Benjimon*

- **Problem:** ComfyUI memory crashes with SVI workflow
  - **Solution:** There are clear models and execution cache options under File/Edit menu, also memory leak issues with model loader
  - *From: Tony(5090)*

- **Problem:** Random fences and gates appearing in generations
  - **Solution:** Usually caused by pushing LoRA too hard or excess noise - reduce LoRA strength or noise levels
  - *From: David Snow*

- **Problem:** SageAttention compiled from source crashes ComfyUI
  - **Solution:** SDPA works as alternative
  - *From: Lumifel*

- **Problem:** Custom SVI node changing faces even without SVI enabled
  - **Solution:** Use native ComfyUI nodes instead of custom 'vibecoded' nodes - native works perfectly
  - *From: RRR*

- **Problem:** LoRA key not loaded errors with SVI Pro
  - **Solution:** Ignore the errors - they're from 2.1 LoRA layers not present in 2.2, but rest of LoRA applies fine
  - *From: Kijai*

- **Problem:** Device mismatch error with prev_samples in SVI Pro
  - **Solution:** Use 'denoised' output from Clownshark sampler nodes instead of regular 'output' - it's on correct device
  - *From: Ablejones*

- **Problem:** RTX 5090 power connector burning/melting
  - **Solution:** Don't use cable that came in box, get third party braided cable set, ensure proper PSU like Corsair RME series
  - *From: ingi // SYSTMS*

- **Problem:** SVI Pro nodes showing as red/missing
  - **Solution:** Switch to nightly build for Kijai nodes or manually pull master branch from custom_nodes/comfyui-kjnodes
  - *From: ucren*

- **Problem:** Original SVI LoRAs don't work in native workflows
  - **Solution:** Use converted LoRAs from Kijai's repo specifically made for native ComfyUI
  - *From: Kijai*

- **Problem:** ComfyUI backend freezes when opening workflows
  - **Solution:** Open two windows (not tabs), use one to close and reopen so the working one doesn't change
  - *From: Kenk*

- **Problem:** Flickering in S2V generation
  - **Solution:** Was caused by bug that didn't pick up the base image
  - *From: Kenk*

- **Problem:** SVI original LoRAs not working
  - **Solution:** Use SVI LoRAs from Kijai's HuggingFace instead of original ones
  - *From: Zueuk*

- **Problem:** Previews in subgraphs showing static images
  - **Solution:** Update video helper suite nodes and enable animated previews in options, use Latent2rgb
  - *From: Kijai*

- **Problem:** PyTorch 2.11.0 causing OOM on VAE decoding
  - **Solution:** Update CUDNN or return to stable PyTorch version, use fp32 VAE as workaround
  - *From: Gleb Tretyak*

- **Problem:** Invalid buffer size error with SamplerCustomAdvanced
  - **Solution:** No specific solution provided, user seeking help
  - *From: buggz*

- **Problem:** Getting stretched human-like forms with chibi characters in Wan Animate
  - **Solution:** Greatly expand the mask size (200+ pixels makes massive difference), position reference in same spot as pose video
  - *From: David Snow*

- **Problem:** 5090 power connector issues
  - **Solution:** Triple check cable is seated fully, avoid force bending, slight undervolting or power limiting to 500W, limit reconnections to ~20 times
  - *From: Kijai*

- **Problem:** SVI 2.2 Pro making black videos in landscape but not portrait
  - **Solution:** No definitive solution provided, one user mentioned prompt weights with SVI causing issues
  - *From: mdkb*

- **Problem:** ComfyUI-Kitchen error after updating
  - **Solution:** Run 'ComfyUI_Main\python_embeded\python.exe -m pip install -U comfy-kitchen' on portable installs
  - *From: The Shadow (NYC)*

- **Problem:** Color shift between windows in WanAnimate long generations
  - **Solution:** No solution provided, acknowledged as known issue
  - *From: Guey.KhalaMari*

- **Problem:** Slow motion issues with SVI
  - **Solution:** Try higher CFG for faster motion, use smoothwan model, try different lightx loras like old MOE distill lora, use 3 sampler setup where first sampler runs without lightx and higher CFG
  - *From: craftogrammer / 42hub*

- **Problem:** SageAttention stopped working with ImportError about required packages
  - **Solution:** Use Triton and Sage versions from woct0rdho on Windows
  - *From: 42hub*

- **Problem:** Color match node failing with infinite 'Reconnecting'
  - **Solution:** Try disabling multithread option in the color match node
  - *From: Kijai*

- **Problem:** SCAIL only working with CUDA 12.8 but user has CUDA 13
  - **Solution:** Upgrade onnxruntime-gpu to nightly version for CUDA 13.x support
  - *From: LukeG89*

- **Problem:** Context windows erroring on last step with clownshark samplers
  - **Solution:** Use extra_option 'skip_final_model_call'
  - *From: Ablejones*

- **Problem:** Memory fragmentation in pytorch cache causing OOM
  - **Solution:** Pytorch cache becomes fragmented after long runs with diverse tensor sizes, limiting ability to find contiguous blocks
  - *From: mallardgazellegoosewildcat2*

- **Problem:** ComfyUI Manager installing wrong version of WanVideoWrapper
  - **Solution:** Manual installation from fresh zip instead of using manager
  - *From: N0NSens*

- **Problem:** Mocha workflow failing with tensor size mismatch
  - **Solution:** Mask should be only on first frame, not multi-frame
  - *From: Dream Making*

- **Problem:** SageAttention CUDA error on RTX 6000 Pro
  - **Solution:** Need to compile SageAttention 2.2 for sm_120 or find pre-compiled .whl
  - *From: harrisonwells*

- **Problem:** Torch compile stopped working after ComfyUI update
  - **Solution:** Torch compile might be broken since recent ComfyUI update
  - *From: pagan*

- **Problem:** InfiniteTalk workflow error with more than 4 steps
  - **Solution:** Change scheduler to dpm++_sde or lcm
  - *From: Kijai*

- **Problem:** ComfyUI memory issues with current version causing lockups
  - **Solution:** Revert to ComfyUI version v0.8.2 from Jan 7 to fix VRAM overshoot issues
  - *From: chancelor*

- **Problem:** Color burn-in and detail shift in longer SVI generations
  - **Solution:** Use Color Match node, though it only partially helps. HPS and MPS reward LoRAs break generation flow with SVI
  - *From: blake37*

- **Problem:** SCAIL and HuMo can't work in same workflow
  - **Solution:** Run HuMo as second pass in V2V mode with 0.5 or 0.8 denoise after SCAIL
  - *From: Dream Making*

- **Problem:** Tensor mismatch errors with Wan 2.2 Fun VACE
  - **Solution:** Check model/VAE/encoder compatibility and ensure frame/resolution count matches
  - *From: psylent_gamer*

- **Problem:** Normal maps bleeding into output with WAN2.1 VACE after 81 frames
  - **Solution:** Issue occurs when exceeding 81 frames in single batch at 720p
  - *From: BEE*

- **Problem:** ComfyUI caught in reloading loop after tab refresh
  - **Solution:** Bug in recent frontend version, should be resolved in latest version or try going backwards
  - *From: Kijai*

- **Problem:** Black output with higher prefetch counts in block swap
  - **Solution:** Keep prefetch at 1, higher values cause NaN tensors which appear faster but don't actually work
  - *From: Kijai*

- **Problem:** Long loading times for transformer parameters
  - **Solution:** Update ComfyUI, remove conflicting nodes like 'infinitetalk' fork, disable pinned memory if needed
  - *From: Kijai*

- **Problem:** Segmentation fault on 5090 with WanVideoWrapper
  - **Solution:** Try without block swap node and torch compile node
  - *From: Kijai*

- **Problem:** Dimension mismatch error
  - **Solution:** Ensure same size in samplers and image_embeds, dim 3 should be height
  - *From: Kijai*

- **Problem:** Native multitalk not finding model
  - **Solution:** Place model in 'model_patches' folder, not diffusion_models
  - *From: Kijai*

- **Problem:** WanVideo Apply NAG causing issues with Wan 2.1
  - **Solution:** Remove/disable WanVideo Apply NAG when using Wan 2.1
  - *From: Juan Gea*

- **Problem:** Lost previews on sampler v2 nodes and VHS nodes
  - **Solution:** Download missing taew2.2 file (needed for 5B model), change UI framerate settings, refresh browser multiple times
  - *From: lostintranslation*

- **Problem:** Color drift when loading videos with VHS
  - **Solution:** Use VHS Load Video (FFmpeg) instead of regular VHS loader to avoid pink/magenta color shift
  - *From: CaptHook*

- **Problem:** RuntimeError with SCAIL: shape invalid for input
  - **Solution:** Ensure dimensions are multiples of 32
  - *From: ingi // SYSTMS*

- **Problem:** Frame misalignment in SVI extension reassembly
  - **Solution:** Set correct frame overlap - use 5 frames for one latent (4 per latent +1 bonus), not 4 frames
  - *From: lostintranslation*

- **Problem:** Extremely slow T5 text encoder loading (85s vs few seconds)
  - **Solution:** Check for RAM paging issues, though root cause unclear - normal load should be few seconds
  - *From: Kijai*

- **Problem:** Color drift when loading videos for extension workflows
  - **Solution:** Use VHS FFmpeg Load Video node instead of regular VHS Load Video or Native Load Video nodes
  - *From: Austin Mroz*

- **Problem:** SCAIL execution order issues with Video Combine
  - **Solution:** Use dummy connections or node ID ordering to ensure proper execution sequence
  - *From: Kijai*

- **Problem:** SCAIL OOM issues with context windows
  - **Solution:** Use only 1 prefetch and adjust block swap settings, disable context windows for shorter videos
  - *From: Kijai*

- **Problem:** Transformers v5 breaking Florence2
  - **Solution:** Downgrade to Transformers 4.57.3
  - *From: JohnDopamine*

- **Problem:** Merged LoRA models causing errors
  - **Solution:** Re-merge LoRAs using ComfyUI nodes to fix compatibility issues
  - *From: patientx*

- **Problem:** WanSelfAttention.normalized_attention_guidance() takes 3-4 arguments but 8 given
  - **Solution:** Disable WanVideo Apply NAG node
  - *From: Nao48*

- **Problem:** SkyReels V3 R2V won't work as-is with KeyError 'blocks.0.self_attn.k.weight'
  - **Solution:** Model uses diffusers keys, needs conversion
  - *From: JohnDopamine*

- **Problem:** Clip loader breaking with mat1 and mat2 error
  - **Solution:** Uninstall and reinstall transformers==4.48.0 tokenizers==0.21.0
  - *From: Faust-SiN*

- **Problem:** Negative prompts not working with distill LoRAs at CFG=1
  - **Solution:** Add NAG to workflow or use delayed negative prompting method
  - *From: JohnDopamine*

- **Problem:** ComfyUI merge issues with SkyReels - 'Linear' object has no attribute 'weight_scale'
  - **Solution:** Unknown fix mentioned but not provided
  - *From: Piblarg*

- **Problem:** SVI math for frame overlap causing misalignment
  - **Solution:** Use default 5 frames, formula should be 4 * latents + 1
  - *From: Kijai*

- **Problem:** Easy Use pack prevents sampler preview from showing
  - **Solution:** Enable 'model preview thumbnails' setting in Easy Use to fix the preview
  - *From: lostintranslation*

- **Problem:** Slow LoRA loading from disk
  - **Solution:** Update safetensors pip package to fix slow loading issues
  - *From: Kijai*

- **Problem:** Cannot merge VACE with Skyreels model
  - **Solution:** It's because it's scaled fp8 model, can't really merge it that simply
  - *From: Kijai*

- **Problem:** Ghosting effect in SVI Pro generations
  - **Solution:** Use smootherstep_blend instead of linear for overlapping to reduce artifacts
  - *From: Kenk*

- **Problem:** MOVA OOM even with 96GB VRAM
  - **Solution:** Select 'cpu' in offload mode instead of 'none' to avoid OOM
  - *From: Stef*

- **Problem:** NVFP4 conversion requires both models loaded using around 20GB VRAM
  - **Solution:** After load, generations are about 30% faster despite initial VRAM usage
  - *From: topmass*


## Model Comparisons

- **SVI Pro 2.0 vs regular workflows**
  - Truly amazing, can generate each clip separately for preview before merging, much more efficient workflow
  - *From: Elvaxorn*

- **Different LightX2V LoRAs**
  - wan2.2_i2v_A14b_high_noise_lightx2v_4step_1030.safetensors and wan2.2_i2v_A14b_low_noise_lightx2v_4step.safetensors full models are the best at 6 steps with euler
  - *From: Benjimon*

- **VACE 2.1 vs 2.2 Fun VACE**
  - VACE 2.1 still beats 2.2 Fun VACE for multi-frame interpolation
  - *From: Kijai*

- **I2V vs T2V for prompt adherence**
  - T2V model better understands prompts and can be used to reprocess I2V videos with Res4lyf to improve quality and prompt comprehension
  - *From: Xor*

- **Native vs WanVideoWrapper for SVI 2.2 Pro**
  - User found wrapper works better after native runs were wonky
  - *From: JohnDopamine*

- **HY-Motion full vs LITE model**
  - Full model is more consistent but slower, LITE model is faster and offers more variety with same prompt
  - *From: tarn59*

- **Open source vs Gemini for video understanding**
  - Open models are very substantially weaker than Gemini, but with finetuning on local video LLM you can beat Gemini on narrow tasks
  - *From: mallardgazellegoosewildcat2*

- **Vast vs RunPod performance**
  - RunPod much faster - 5 seconds per image vs 60 seconds on Vast instance
  - *From: Kevin "Literally Who?" Abanto*

- **SVI vs InfiniteTalk for endless generation**
  - InfiniteTalk seems to actually be infinite over minutes, SVI can be too if you don't diverge from anchor frame too much
  - *From: Kijai*

- **Holocine vs SVI**
  - Holocine not worth it anymore with SVI available
  - *From: NebSH*

- **LTX-2 vs other models**
  - 19B parameters, should fit in 24GB, comes with 4-8 step distilled models
  - *From: ZeusZeus (RTX 4090)*

- **Wan 2.1 vs 2.2 low-noise only**
  - 2.2 low performs better than 2.1, swapping models doesn't break workflows, surprisingly compatible
  - *From: Godhand*

- **LTX-2 vs Wan 2.2**
  - LTX-2 nowhere close to replacing Wan for I2V, Wan still king for many things especially pose fidelity and lipsync. Nothing touches WanAnimate and SCAIL for pose fidelity
  - *From: taoofai / cyncratic*

- **Stock GGUF with 1030 lora vs wan remix checkpoint**
  - Checkpoint merges add more motion but mess with likeness
  - *From: MarkDalias*

- **With tile vs without tile CLIP vision**
  - Tile can cause problems in some cases, without tile sometimes produces better results with more accurate likeness
  - *From: David Snow*

- **WAN 2.2 vs LTX-2 for T2V**
  - WAN understands human anatomy way better, LTX does weird stuff and 'bollywoods everything'
  - *From: b̶̈́͠o̶̗̅n̶̽̒k̵̽̿*

- **WAN vs Stepfun**
  - Switched to WAN because it got so much extra stuff added
  - *From: mallardgazellegoosewildcat2*

- **SVI vs VACE for continuations**
  - SVI way better than VACE but suffers from color/brightness shift and degradation. VACE has color shift issues
  - *From: Juan Gea*

- **Different video models for best results**
  - Best might be Cosmos but only for robot and car videos
  - *From: mallardgazellegoosewildcat2*

- **LTX-2 with WAN Low feels like WAN 2.6**
  - Combining LTX-2 with WAN low produces results that feel like an unreleased WAN 2.6
  - *From: hicho*

- **LTX2V vs Wan models**
  - User found LTX2V compelling enough to stop using Wan models recently
  - *From: hicho*

- **NVFP4 vs regular quantization**
  - NVFP4 quality is between Q4 and Q6 gguf, size between Q3 and Q4, but 8x faster. Currently doesn't support ControlNet or LoRAs
  - *From: CaptHook*

- **SVDQuant vs regular quantization**
  - SVDQuant is superior but requires careful calibration, which is the hard part preventing Wan implementation
  - *From: mallardgazellegoosewildcat2*

- **Wan 2.6 vs LTX-2**
  - LTX-2 is better in almost all aspects except Wan 2.6's cameo feature (reference video to video) which is pretty cool
  - *From: ZeusZeus (RTX 4090)*

- **Wan quality vs LTX2 quality**
  - Wan has better visual quality than LTX2, LTX2 wins on speed and audio support but Wan is better base model overall
  - *From: Piblarg*

- **FP16 vs FP8 speed with Wan 2.2**
  - No speed difference noticed between FP8 and FP16, only switching between High and Low model takes longer
  - *From: SantaHunter*

- **Wan ecosystem vs LTX2**
  - Wan has more tools and modalities but lacks native audio and long duration. LTX2 faster, smaller, longer videos but licensing issues prevent broad adoption
  - *From: Kijai*

- **Wrapper vs Native for Wan Animate**
  - Animate quality in wrapper is 5x better than native
  - *From: asd*

- **LTX2 vs Wan 2.5**
  - LTX2 is faster, smaller, higher quality, longer videos - Wan really lost
  - *From: ZeusZeus*

- **VHS loaders vs Native video loading**
  - Native is faster (19s vs 32s for VHS regular vs 55s for VHS FFmpeg) and has no color drift. VHS FFmpeg is most color accurate but slowest
  - *From: lostintranslation*

- **SCAIL vs VACE for pose control**
  - SCAIL is superior with 3D pose data vs VACE's basic pose control
  - *From: Juampab12*

- **SVI vs VACE quality**
  - SVI has much less quality loss and color drift than VACE, but both still exist to some degree
  - *From: lostintranslation*

- **SCAIL vs LTX2 for pose copying**
  - LTX2 better for facial consistency, SCAIL better for pose accuracy
  - *From: Kevin "Literally Who?" Abanto*

- **Klein 9B vs Nanobanana Pro for background replacement**
  - NBP significantly ahead for relighting and subject preservation
  - *From: blake37*

- **Magi vs Wan 2.2 vs Stepvideo**
  - Stepvideo and Magi ranked first, Wan 2.2 considered king of local generation due to hardware requirements
  - *From: mallardgazellegoosewildcat2*

- **Self-refine on vs off**
  - Clear improvement in video quality with self-refine, especially for motion consistency
  - *From: TK_999*

- **SkyReels V3 vs InfiniteTalk**
  - SkyReels V3 does some things differently but unclear if superior to LongCat Avatar
  - *From: Kijai*

- **MOVA vs LTX2**
  - MOVA examples are much worse quality, limited to 8 seconds vs LTX2's 30+ seconds
  - *From: Kijai*

- **MOVA vs Ovi**
  - MOVA looks sharper than Ovi, better sound, but Ovi has better visual quality overall
  - *From: mallardgazellegoosewildcat2*

- **Wan 2.1 vs 2.2 motion**
  - 2.1 far from 2.2 quality with motion
  - *From: Kijai*

- **LTX2 vs other models for long video**
  - LTX2 absolutely on its own level for long video generation, can do 30s+ with same context
  - *From: Kijai*

- **MOVA vs Wan 2.2 speed**
  - MOVA is about 1-2 seconds slower per iteration compared to Wan2.2
  - *From: yi*

- **Wan 2.5/2.6 vs 2.2**
  - Quality of wan 2.5/2.6 is a downgrade from 2.2 in many ways due to shortcuts for speed
  - *From: Ruairi Robinson*

- **Wan 2.5 vs 2.6**
  - 2.6 is bad but 2.5 is way better in quality, dialogue, motion, prompt understanding
  - *From: asd*

- **MOVA guitar vs stock wan + mmaudio**
  - Stock wan + mmaudio is better than MOVA for music generation
  - *From: Benjimon*

- **Low quality InfiniteTalk vs other lip-sync methods**
  - Even low quality InfiniteTalk workflow beat the example shown
  - *From: Krikross*

- **MOVA vs Wan 2.2 a14b performance**
  - MOVA only about 1-2 seconds slower per iteration
  - *From: yi*

- **HuMo vs other methods for long generations**
  - HuMo can't natively do long generations
  - *From: Kijai*


## Tips & Best Practices

- **Use old 480 rank64 LoRA instead of 1022 for low model**
  - Context: 1022 LoRA not good with low model, old one much better
  - *From: Elvaxorn*

- **Use 1030 LoRA for better motion than 1022**
  - Context: For high noise model generations
  - *From: Elvaxorn*

- **Stride input frames to help with movement and speed**
  - Context: Taking 1 frame every 15 from PNG sequence gives completely different, faster output
  - *From: Kenk*

- **Use VACE for multi-keyframe interpolation instead of SVI**
  - Context: SVI/2.2 isn't trained for multi-keyframe injection, VACE works better for that use case
  - *From: Kijai*

- **Decode and re-encode latents for SVI anchor changes**
  - Context: Last latent is actually 4 frames, not 1 - need to decode with VAE and re-encode to get single anchor frame
  - *From: Ablejones*

- **Always start with native ComfyUI, then WanWrapper if not available**
  - Context: Avoid vibecoded custom nodes - most new features are quickly available in native or Kijai implementations
  - *From: ucren*

- **Use distill LoRA strength at 1.5 on high pass to counter slow-mo effect**
  - Context: When using SVI Pro and experiencing slowmotion issues
  - *From: gilfoyle*

- **Prompt aggressively to break away from anchor frame in SVI**
  - Context: Lazy prompting will keep SVI stuck to anchor image due to its consistency mechanism
  - *From: Ablejones*

- **Find front-facing character view as anchor latent for T2V with SVI**
  - Context: When doing T2V generations involving character appearance before SVI extension
  - *From: slmonker(5090D 32GB)*

- **Can regenerate anchor midway in long sequences**
  - Context: For 10x 5s segments, you can do another anchor when you know something will change in the scene
  - *From: pagan*

- **Use two VACE encode nodes with different strengths for separate control**
  - Context: One with control net and other with reference at different strengths when you want reference image to matter more than control video or vice versa
  - *From: Piblarg*

- **Use --cache-none to automatically release model and node cache**
  - Context: When switching between workflows to prevent freezing
  - *From: LukeG89*

- **For non-standard characters, greatly expand the mask**
  - Context: 20, 60, 100, 200 pixel masks show massive improvement with chibi characters
  - *From: David Snow*

- **Position reference in same spot as pose video**
  - Context: Helps with character consistency in Wan Animate
  - *From: David Snow*

- **Use SCAIL to scale poses to match target proportions**
  - Context: When working with non-standard character proportions
  - *From: ucren*

- **Padding to 300 + feet in frame helps A LOT**
  - Context: For better character consistency
  - *From: Kav*

- **Modifying input video is more important than everything else**
  - Context: After extensive testing with Wan models
  - *From: Kav*

- **Limit node pack count for better performance**
  - Context: Running 120+ node packs causes slowest startup in the universe
  - *From: Kijai*

- **Undervolt 5090 to 500W from 550W for safety**
  - Context: Prevents power connector issues and overheating
  - *From: Kijai*

- **Don't use model merges for purposes other than what they're made for**
  - Context: Quality degrades, especially with AIO models
  - *From: Kijai*

- **Use large masks with WanAnimate**
  - Context: WanAnimate seems to prefer really large masks for better results
  - *From: David Snow*

- **Add motion descriptions in prompts**
  - Context: For avoiding slow motion in SVI, describe the motion in the prompt
  - *From: cyncratic*

- **Use 3 sampler setup for better motion**
  - Context: First sampler without lightx and higher CFG, takes more time but improves motion
  - *From: 42hub*

- **Generate at higher resolution for better results**
  - Context: General observation that reasonably higher resolution yields better results
  - *From: 42hub*

- **Try SGM-uniform scheduler for better motion**
  - Context: User found motion improved when switching from euler/simple to sgm-uniform
  - *From: cocktailprawn1212*

- **Can mix WAN high motion with LTX-2 at 0.3 denoise for better results**
  - Context: Using LTX-2 for v2v processing of WAN output
  - *From: hicho*

- **Use only WAN 2.2 low for upscaling with 2-3 steps**
  - Context: Upscaling workflow, balance between frames per batch and resolution
  - *From: Janosch Simon*

- **Can upscale better in ComfyUI than any current paid upscaling service**
  - Context: Using iterative captioned tiled upscale with Flux
  - *From: mallardgazellegoosewildcat2*

- **Use res4lyf samplers with specific extra_options for efficiency**
  - Context: default_dtype=float32, multistep_initial_sampler=euler, skip_final_model_call
  - *From: Ablejones*

- **LN is basically 2.1, HN is where the 2.2 magic is at**
  - Context: Understanding WAN 2.2 model variants
  - *From: mdkb*

- **Keep entire SVI system step count under 10 steps**
  - Context: When using multi-sampler SVI setup with high and low noise
  - *From: Canin17*

- **Use portrait crop of first I2V frame as SVI anchor**
  - Context: SVI works best with closeup portraits for anchor frames
  - *From: ucren*

- **Disable hands in SCAIL for better quality**
  - Context: When getting poor motion quality with hands flying away
  - *From: Kijai*

- **Use reverse image batch node for progressive character entry**
  - Context: When character only partially visible in initial frames
  - *From: David Snow*

- **Use anchor frame changes and vary SVI weight/denoising for experimental effects**
  - Context: When doing video extensions with SVI Pro
  - *From: Dream Making*

- **Some LoRAs can go to 2.0 strength but it gets very spicy**
  - Context: General LoRA usage advice
  - *From: mallardgazellegoosewildcat2*

- **Use higher order and/or multi-step samplers with momentum to use fewer steps**
  - Context: For speeding up generation, moving from Euler to DPM allows using fewer steps
  - *From: mallardgazellegoosewildcat2*

- **Train embeddings on Wan 1.3B with small images for speed, then transfer to larger models**
  - Context: Since all Wan versions use same text encoder
  - *From: spacepxl*

- **Use character LoRA even with Wan Animate for likeness preservation**
  - Context: Wan Animate still needs character LoRA in testing
  - *From: Dream Making*

- **Use 24fps for SVI-Pro2.2 output**
  - Context: Works well in most cases for video generation
  - *From: JohnDopamine*

- **Full CFG always helps inpainting**
  - Context: Even with empty negatives, but requires full steps (40)
  - *From: mallardgazellegoosewildcat2*

- **Don't use face points with steadydancer**
  - Context: Steadydancer doesn't have face control capability
  - *From: Kijai*

- **Use higher distill lora strengths and proper CFG with 2.2**
  - Context: Better than painter-like hacks for getting motion
  - *From: Kijai*

- **Use shift=5 with Wan distilled loras**
  - Context: They were specifically trained with this value
  - *From: spacepxl*

- **Save latents instead of video files for SVI extension**
  - Context: When you want to preserve maximum detail between extensions and continue workflows later
  - *From: Kijai*

- **Duplicate first frame several times to fix refine pass garbage frames**
  - Context: Add duplicated frames at beginning, then trim after decoding to avoid garbage first frames in Wan refine pass
  - *From: N0NSens*

- **Use cfg on first step, no cfg on later steps method**
  - Context: Still valid and recommended approach for sampling
  - *From: Kijai*

- **Use VHS Load Video (FFmpeg) for color accuracy**
  - Context: When you need to avoid color drift that occurs with regular VHS loader
  - *From: CaptHook*

- **Use restart sampling with many steps**
  - Context: Start with 1000+ steps when experimenting with restart sampling for best results
  - *From: mallardgazellegoosewildcat2*

- **Prompt character details when using SCAIL**
  - Context: Important to describe style and character details when character is turning or moving
  - *From: Kijai*

- **Use augment_empty_frames with self-refine**
  - Context: Combine experimental augment_empty_frames feature with self-refine for more controlled motion
  - *From: JohnDopamine*

- **Save only necessary frames for SVI extensions**
  - Context: For video extension workflows, only encode the last few frames needed rather than entire long videos
  - *From: mallardgazellegoosewildcat2*

- **Use white padding for SkyReels V3 reference images**
  - Context: When using reference images with the model
  - *From: Kijai*

- **Self-refine sampling works better with more steps**
  - Context: Because restarts add more noise than SDE samplers
  - *From: mallardgazellegoosewildcat2*

- **Highly recommend upscaling pass for LTX2**
  - Context: Due to very compressive VAE in spatial dimensions
  - *From: yi*

- **Use delayed negative prompting for first third of steps**
  - Context: Have blank negative for first portion of generation steps
  - *From: mallardgazellegoosewildcat2*

- **SVI is not trained to continue from more than one latent**
  - Context: Can have issues when trying to extend beyond default parameters
  - *From: Kijai*

- **Use DWOpenpose instead of depth for VACE face work**
  - Context: When doing subject transfer in videos, DWOpenpose will be closer to reference image than depth maps
  - *From: Stef*

- **Don't use DA 3 for VACE**
  - Context: For VACE workflows, DA 3 made things worse than with DA 2 vitg
  - *From: Stef*

- **Test MOVA properly with correct settings**
  - Context: Use 121 frames 24fps for proper testing since Hunyuanvideo foley doesn't support framerate other than 24fps
  - *From: yi*

- **Use ComfyUI bridge node for FP8 text encoding**
  - Context: When wrapper text encoder doesn't support FP8 scaled, use the comfy native text encoding with bridge node
  - *From: Kijai*

- **Just converting to NVFP4 is very lossy - proper NVFP4 models need calibration**
  - Context: When using NVFP4 conversion tools
  - *From: Kijai*

- **You could use InfiniteTalk or MultiTalk with SVI for better results**
  - Context: When doing audio-driven video generation
  - *From: Kijai*


## News & Updates

- **ComfyUI frontend updated to v1.37.1**
  - Preview bridge mask editor fixed for crop/masking workflows
  - *From: ucren*

- **New 1217 LightX2V LoRA released**
  - Decent for low noise model
  - *From: Elvaxorn*

- **New omnivcus has newly trained VACE for 2.2**
  - Haven't been tested yet but available
  - *From: Kijai*

- **HY-Motion-1.0 released by Benji**
  - Can do climbing obstacles, fighting, crawling, playing instruments, climbing stairs/ladders. Adjustable runtime 1-12 seconds. Could pair well with Wan Animate
  - *From: tarn59*

- **Thesby Qwen3VL models got deleted**
  - User looking for backup of deleted models
  - *From: Gleb Tretyak*

- **LTX-2 released**
  - 19B parameters, dev and distilled models (4-8 steps), joint audio-video training, ComfyUI support ready
  - *From: ZeusZeus (RTX 4090)*

- **LongVie2 added to Kijai's main branch**
  - Depth controlnet for I2V models, can continue from 8 frames
  - *From: Kijai*

- **NVIDIA bringing back RTX 3060 in Q1 2026**
  - To tackle memory shortages
  - *From: Tachyon*

- **Flash attention now working on ROCm and Windows**
  - Previously wasn't available for these platforms
  - *From: patientx*

- **LTX-2 released**
  - New open source video model with audio support, 20 second generations, available on HuggingFace
  - *From: Ada*

- **ComfyUI-Kitchen added for fp8/fp4 support**
  - New addition to help with fp8 and fp4 model support
  - *From: Tachyon*

- **DreamID-V released by ByteDance**
  - New video generation model from ByteDance released on GitHub
  - *From: AshmoTV*

- **HummingbirdXT - WAN 2.2 5B distill released by AMD**
  - Lightweight VAE decoder that can substitute for WAN-2.2-5B VAE with reduced computational cost
  - *From: yi*

- **VerseCrafter - world model based on WAN released by TencentARC**
  - New world model architecture built on WAN foundation
  - *From: yi*

- **SoulX FlashTalk announced**
  - New lip-sync/talking head technology
  - *From: DawnII*

- **WAN team mentioned releasing lighter version 'for the community to use'**
  - Suggests 20B-25B parameter model similar to WAN 2.2 coming
  - *From: yi*

- **Wan 2.2 NVFP4 quantized models released**
  - GitMylo released NVFP4 versions but quality may be degraded
  - *From: Ada*

- **UniPic3 CM models released by Skywork**
  - Two distillation methods available: consistency model and DMD distillation
  - *From: mallardgazellegoosewildcat2*

- **Adobe bought Invoke**
  - Invoke has gone full Adobe according to user
  - *From: mallardgazellegoosewildcat2*

- **ComfyUI now supports asynchronous weight offloading**
  - Allows better memory management by moving weights between VRAM/RAM asynchronously
  - *From: Kijai*

- **New V-RGBX inverse rendering tool works in ComfyUI**
  - RGB to albedo/normals etc, works with no code changes needed in ComfyUI
  - *From: spacepxl*

- **FlashVSR fork with bug fixes released**
  - Fixes dropped frames, misaligned output, memory leaks, adds 1.1 support and frame chunking
  - *From: lostintranslation*

- **InfiniteTalk merged into native ComfyUI**
  - Commit 16b9aabd52c3b81b365fbf562bbcc4528111ef6b merged into Comfy-Org/ComfyUI
  - *From: Kijai*

- **VACE tailored nodes released**
  - RGnodes released for VACE and other video/mask needs
  - *From: rryyaann*

- **OmniVideo2-A14B released**
  - New model from Fudan-FUXI available on HuggingFace
  - *From: yi*

- **StoryMem repo updated with RoPE fixes**
  - Recent commit added missing RoPE offset implementation
  - *From: JohnDopamine*

- **SVI 2.0 Pro available for Wan 2.2**
  - Extension system now works with Wan 2.2 architecture at github.com/vita-epfl/Stable-Video-Infinity/tree/svi_wan22
  - *From: lostintranslation*

- **Native InfiniteTalk Extension Workflow released**
  - Supports custom audio or TTS, posted to WAN resources
  - *From: Elvaxorn*

- **Memory optimization improvements for high res InfiniteTalk**
  - New optimizations save 1GB+ VRAM for 720p+ generations
  - *From: Kijai*

- **Self-refine-video implementation available**
  - Early testing branch available on ComfyUI-WanVideoWrapper repository
  - *From: Kijai*

- **SkyReels V3 announced**
  - New R2V, A2V, V2V models based on Wan architecture with multishot video extension
  - *From: yi*

- **Color shift issue officially acknowledged**
  - VHS developer confirmed the color space conversion issues and provided technical explanation
  - *From: Austin Mroz*

- **OmniTransfer model announced**
  - New model from lead HuMo developer, similar to OmniInsert but improved version
  - *From: JohnDopamine*

- **SkyReels V3 R2V model released**
  - New reference-to-video model based on Wan 2.1 with 24fps capability
  - *From: yi*

- **MOVA (OpenMOSS) released with Apache 2.0 license**
  - 32B parameter video-audio model, actually Wan 2.2 A14B + audio, Apache licensed
  - *From: mallardgazellegoosewildcat2*

- **Self-refine video sampling branch available for testing**
  - New sampling method in development branch of WanVideoWrapper
  - *From: JohnDopamine*

- **NVIDIA FastGen research repo released**
  - Distillation training stuff featuring Wan, ~2 days old
  - *From: JohnDopamine*

- **MOVA ComfyUI implementation available**
  - Custom node available at HM-RunningHub/ComfyUI_RH_MOVA repo
  - *From: Lodis*

- **Modulo support added to KJNodes calculator**
  - Added modulo operation support to calculator node
  - *From: Kijai*

- **Boolean output added to KJNodes calculator**
  - Calculator node now has boolean output for comparison operations
  - *From: Kijai*

- **Wan 2.6 has video reference capability**
  - Can upload a reference video of a person then do new videos of that person, no training at all
  - *From: Ruairi Robinson*

- **MOVA team roadmap includes API and HF space**
  - They are making an API and HF space along with diffusers implementation
  - *From: yi*

- **SVI 2.0 Pro branch doesn't have training code available**
  - Team states 'We currently have no plans to open-source the training code' - only original 2.1 SVI has training code
  - *From: Persoon*


## Workflows & Use Cases

- **SVI Pro 2.0 + Longlook motion scale + RCM 2.2 + upscale/interpolation**
  - Use case: Budget VEO3 alternative at 832x480 (65 fps per clip)
  - *From: Elvaxorn*

- **Face-only second pass generation**
  - Use case: Generate face separately then comp back in to improve facial animations when face is too small in frame
  - *From: David Snow*

- **PNG frame encoding method for SVI**
  - Use case: Less stressful on RAM for long video interpolation - save frames as PNG then encode back to latent
  - *From: Kenk*

- **SVI Pro with multiple segments using prev_samples**
  - Use case: Extended video generation with consistent character across segments
  - *From: BarleyFarmer*

- **T2V to SVI Pro extension workflow**
  - Use case: Starting with T2V generation then extending with SVI Pro, though seamless transition is challenging
  - *From: seitanism*

- **HuMo + SVI workflow with anchor swapping**
  - Use case: Audio-driven video with ability to change anchor for different sections, supports outfit changes
  - *From: JohnDopamine*

- **Model alternating steps workflow**
  - Use case: Alternate single steps between Wan Animate and SCAIL models for combined benefits
  - *From: mallardgazellegoosewildcat2*

- **SVI 2.0 Pro with video extension**
  - Use case: Extending existing videos by encoding original and feeding as prev latents with anchor frame
  - *From: 42hub*

- **WanVideoBlender for smooth transitions**
  - Use case: Feed two videos with overlap frames (1 usually works) to create smooth transitions
  - *From: Tachyon*

- **Progressive SVI generation**
  - Use case: 25 segments of 69 latent frames with different prompts per segment for long videos
  - *From: TK_999*

- **LongVie2 with depth control**
  - Use case: I2V generation with depth controlnet, can extend from original video's first frame
  - *From: Kijai*

- **Using LTX-2 as Wan upscaler**
  - Use case: Fast 1080p upscaling of Wan videos in about a minute using v2v detailer workflow
  - *From: David Snow*

- **WanAnimate face detection for LivePortrait**
  - Use case: Use WanAnimate's more stable face detection as driving video for LivePortrait to reduce jitter
  - *From: David Snow*

- **SCAIL with Context Windows**
  - Use case: Can go beyond normal frame count limits for long generations, works best on plain backgrounds
  - *From: 42hub*

- **LTX-2 to WAN 2.2 low v2v with audio transfer**
  - Use case: Getting audio capabilities in WAN by using LTX-2 first then processing with WAN
  - *From: hicho*

- **Batch upscaler using WAN 2.2 low with 1.3-1.5x upscale**
  - Use case: Standalone batch processing for long videos with balance between frames and resolution
  - *From: Ivoxx*

- **Stitching I2Vs with VACE and upscaling with SeedVR2**
  - Use case: Long video generation by combining multiple I2V segments and fixing seams
  - *From: pom*

- **Using Phantom with multiple character references**
  - Use case: Multi-character video generation following specific rules
  - *From: mdkb*

- **Multi-sampler SVI setup with CFG shifting**
  - Use case: Using first 2 steps with CFG for structure, then distill LoRA for finishing
  - *From: Canin17*

- **Wan refine pass after LTX generation**
  - Use case: Using Wan as refinement step to improve LTX output quality
  - *From: N0NSens*

- **Beat-locked video editing with stems**
  - Use case: Automatic multi-camera editing synced to music using audio stem analysis
  - *From: VRGameDevGirl84(RTX 5090)*

- **3-step character replacement process: I2V → SCAIL → HuMo V2V**
  - Use case: Multi-shot sequences where character starts turned around then reveals target face
  - *From: Dream Making*

- **Use VACE with Qwen edit for face application before T2V**
  - Use case: Applying reference face to video generation
  - *From: Dream Making*

- **SVI Pro for long generations instead of context windows**
  - Use case: Faster long video generation with per-segment prompting control
  - *From: blake37*

- **Multi-sampler SVI Pro setup**
  - Use case: Video extension with custom schedulers like bong_tangent
  - *From: garbus*

- **NAG with SVI for prompt adherence**
  - Use case: Making model follow complex prompts like sprouting wings and flying
  - *From: JohnDopamine*

- **StoryMem for memory-enhanced generation**
  - Use case: Using memory images with temporal positioning
  - *From: Kijai*

- **SVI Pro extension workflow**
  - Use case: Extending videos while preserving quality and minimizing color drift
  - *From: Kijai*

- **First frame duplication for refine pass**
  - Use case: Avoiding garbage frames at start of Wan refine operations by duplicating first frame multiple times
  - *From: N0NSens*

- **SCAIL pose control**
  - Use case: Advanced pose control with 3D pose data for video generation
  - *From: Juampab12*

- **VACE method for video extension**
  - Use case: Using VACE with Steerable Motion node for better video extensions
  - *From: JohnDopamine*

- **Multiple video extension without saving**
  - Use case: Producing extensions to existing videos using SVI while minimizing disk I/O
  - *From: lostintranslation*

- **Self-refine with regular and distill models**
  - Use case: Improving video quality through restart sampling, works better with full models than distills
  - *From: Kijai*

- **SkyReels V3 R2V with Phantom node**
  - Use case: Reference-to-video generation using existing Phantom workflows
  - *From: Kijai*

- **VACE FFLF combined with InfiniteTalk**
  - Use case: Video extension using first-frame-last-frame with infinite talk
  - *From: Elvaxorn*

- **Two-step workflow for video extension**
  - Use case: Generate initial video, then use video-to-video infinite talk for extension
  - *From: asd*

- **SVI Pro 2.0 color-preserving workflow**
  - Use case: For SVI where color shift is almost imperceptible
  - *From: Stef*

- **Multiple reference images for SVI**
  - Use case: Passing multiple reference images like a 3D scene from different angles for better background understanding
  - *From: lostintranslation*

- **Background change with VACE**
  - Use case: Change background while keeping same subject/face using reference image with new background and original video for control
  - *From: Albert*

- **A2V (Audio to Video) has its own workflow, R2V (Reference to Video) can be used in Phantom workflow**
  - Use case: Audio-driven and reference-driven video generation
  - *From: Kijai*

- **NVFP4 conversion workflow using ComfyUI_Kitchen_nvfp4_Converter**
  - Use case: Reducing VRAM usage for Wan models
  - *From: topmass*


## Recommended Settings

- **diff_augment_scale parameter**: 1.6 default, but adjust per video
  - Too high causes scene changes, needs tuning based on content
  - *From: Ablejones*

- **SVI Pro video length**: 65 frames instead of 81
  - Makes generation super fast and uses less VRAM
  - *From: Elvaxorn*

- **Motion latent count for SVI**: Minimum 4 frames (goes in increments of 4)
  - Last latent contains 4 frames, need 5 minimum as first frame is different
  - *From: Kijai*

- **LightX2V steps**: 6 steps with euler sampler
  - Best performance for the recommended LoRA models
  - *From: Benjimon*

- **RTX 5090 power limit**: 90% max power
  - User running at this setting since March to help prevent power connector issues
  - *From: AJO*

- **SVI Pro motion_latent_count**: 2 motion latents
  - Better results than 0 or 1 motion latents for T2V to SVI transitions
  - *From: seitanism*

- **MoE timestep split**: 0.875
  - Standard training split between high and low models, important for LoRA compatibility
  - *From: ingi // SYSTMS*

- **SVI overlap frames**: 1
  - Usually works for smooth transitions in WanVideoBlender
  - *From: Tachyon*

- **5090 power limit**: 500W
  - Safer than full 550W, prevents power connector issues
  - *From: Kijai*

- **Mask expansion for chibi characters**: 200+ pixels
  - Makes massive difference for non-standard character proportions
  - *From: David Snow*

- **LightX2V steps**: 4-5 steps
  - Best balance of time vs quality, takes 2ish minutes per gen at 1280x720
  - *From: Akshvodae | Joe*

- **CLIP Vision tiles**: 2 tiles for 512x512 effective resolution
  - CLIP vision capped at 256x256, tiling allows seeing more detail
  - *From: ingi // SYSTMS*

- **VACE steps**: 6 steps better than 4 or 8
  - User found better results at 6 steps, 8 was too much
  - *From: Blink*

- **SVI sampler setup**: i2v 1030 high, i2v 1022 low, 2 steps high, 4 steps low (6 total)
  - Specific configuration for better motion
  - *From: MarkDalias*

- **LightX LoRA strengths**: Variable values shown in workflow image
  - Helps with motion control
  - *From: patientx*

- **WAN 2.2 low upscaling**: 0.3 denoise with 2-3 steps
  - Balance between quality and speed for upscaling
  - *From: Ivoxx*

- **LTX-2 v2v processing**: 0.3 denoise
  - Good balance for video-to-video processing
  - *From: hicho*

- **res4lyf extra_options**: skip_final_model_call, default_dtype=float32
  - Reduces memory usage and inference time
  - *From: Ablejones*

- **SVI 2.0 Pro LoRA strength**: 60% or lower
  - Helps combat stifled motion issues
  - *From: DevouredBeef*

- **SCAIL frame picking**: Every 2 frames
  - Depends on input video motion speed
  - *From: Kijai*

- **Numpy version**: 1.26.4 or 1.26.0
  - Avoids breaking LTX and SeedVR2 nodes
  - *From: Kijai*

- **SVI weight**: 0.7 or 0.5
  - Good results for video extension, can test higher values
  - *From: Dream Making*

- **Block swap prefetch**: 1
  - Higher values cause black output due to NaN tensors
  - *From: Kijai*

- **HuMo denoise for second pass**: 0.5 or 0.8
  - When using HuMo as V2V second pass after SCAIL
  - *From: Dream Making*

- **CFG Schedule**: Only use CFG on first step
  - Trick to get more movement with lightx2v distill loras
  - *From: Kijai*

- **Steps for undistilled models**: 40 steps (36 also fine)
  - Black Forest Lab's recommended number
  - *From: mallardgazellegoosewildcat2*

- **SVI split point sigma**: 0.9 for I2V, 0.875 for T2V
  - Optimal split points based on sigma values
  - *From: Kijai*

- **NAG parameters**: Scale: 12, tau: 4.0, alpha: 0.4
  - Effective for prompt adherence
  - *From: JohnDopamine*

- **StoryMem RoPE offset**: 5 (default)
  - Frame indices spread by factor of 5
  - *From: Kijai*

- **shift**: 5
  - Wan distilled loras were trained with this value
  - *From: spacepxl*

- **frame overlap for SVI**: 5 frames for one latent
  - Correct formula is 4 frames per latent +1, not just 4 frames
  - *From: lostintranslation*

- **fps for SVI**: 24fps
  - Works well with SVI2.2-Pro though not officially recommended
  - *From: JohnDopamine*

- **SCAIL block swap**: ~30 blocks for 720p
  - Optimal VRAM usage for 4090, uses under 20GB
  - *From: Kijai*

- **Self-refine step increase**: 50% more steps
  - Default implementation increases model calls by 50% for quality improvement
  - *From: Kijai*

- **SageAttn as default**: Enable SageAttn auto mode
  - Provides 2x speedup with ~90% quality retention
  - *From: Kijai*

- **SCAIL prefetch**: 1 prefetch only
  - Prevents OOM issues when using context windows
  - *From: Kijai*

- **SkyReels V3 steps with LightX2V**: 6 steps
  - Demonstrated working configuration
  - *From: Kijai*

- **Default SkyReels V3 frames**: 81 frames in code, 121 for R2V
  - Based on duration * 24 + 1 formula
  - *From: Kijai*

- **SVI frame overlap**: 4 * latents + 1
  - Proper mathematical formula for frame alignment
  - *From: Kijai*

- **MOVA memory settings**: cpu offload mode, bfloat16
  - To avoid OOM with high VRAM usage
  - *From: Stef*

- **MOVA recommended resolution**: 352*640 for standard, 1280*720 for 720p model
  - Official recommended resolutions
  - *From: yi*

- **motion_latent_count for SVIPro**: 0 for 1st sampler, 1 for 2nd sampler
  - To properly continue from previous latent with 5 frame overlap
  - *From: Kijai*

- **Self-refine certain_percentage default**: .999
  - Default setting seems oddly high, worth experimenting with
  - *From: JohnDopamine*

- **Steps for lip-sync generation**: 4 steps
  - Default setting used in examples
  - *From: Kijai*

- **NVFP4 generation test**: 700x400 px, 81 frames, 24fps
  - Test configuration for NVFP4 model
  - *From: topmass*


## Concepts Explained

- **SVI (Stable Video Infinity)**: Helps with video continuation for keeping consistency, uses last latent from previous generation to continue
  - *From: TK_999*

- **Difference augmentation**: Mechanism that forces I2V generated frames to move further from initial input frame, useful for nudging I2V output in controllable manner
  - *From: Ablejones*

- **Motion latent count**: In SVI, refers to number of frames used for continuation - last latent contains 4 frames, first frame is separate reference
  - *From: Kijai*

- **Structural repulsion boost**: Vague marketing term used by custom node creators - likely refers to painter method but unclear what it actually does
  - *From: RRR*

- **SVI anchor mechanism**: SVI is biased towards less motion because it's always trying to get back to the anchor frame for consistency - this is how it maintains character consistency
  - *From: Ablejones*

- **Mixed precision quantization**: ComfyUI mixed format includes info for each layer with settings like activation precision and whether it can use fp8 matmuls. Needs dict in model or quant keys
  - *From: Kijai*

- **SVI anchor latent**: Method to mitigate quality degradation in extended video generation by providing reference point
  - *From: Kijai*

- **MoE timestep split**: Division between high and low noise experts in MoE architecture at 0.875 threshold
  - *From: ingi // SYSTMS*

- **Conv3d memory bug**: PyTorch issue affecting VAE decoding, related to CUDNN version, causes 3x memory usage
  - *From: Kijai*

- **AIO model**: All-in-one model, refers to 2.1 model with multiple LoRAs baked in
  - *From: Kijai*

- **CLIP Vision tiling**: Breaking images into tiles so CLIP vision can see more detail since it's normally capped at 256x256 resolution
  - *From: ingi // SYSTMS*

- **Native vs Wrapper workflows**: Native refers to workflows built around KSampler from ComfyUI native, wrapper refers to workflows built around WanVideo Sampler from Kijai's repo
  - *From: 42hub*

- **High/Low noise models in Wan 2.2**: Wan 2.2 uses MoE architecture with separate high and low noise expert models, high model sets motion while low handles detail
  - *From: 42hub*

- **VACE vs LoRA**: VACE is not a LoRA but 'extra model layers' that plug into model loader differently than LoRAs
  - *From: 42hub*

- **Pytorch memory fragmentation**: Cache becomes fragmented after long runs with diverse tensor sizes, making it hard to find contiguous blocks for new large tensors
  - *From: mallardgazellegoosewildcat2*

- **Skip final model call**: Mathematical denoise by interpolation instead of extra model call, similar to how ComfyUI handles previews
  - *From: Ablejones*

- **PyTorch memory fragmentation**: PyTorch cache pool can have free memory but be unable to allocate due to fragmentation. Blocks need to be contiguous, free, and in same segment to merge.
  - *From: mallardgazellegoosewildcat2*

- **SVI anchor frame concept**: Anchor frame is what you want the likeness anchored to throughout the video sequence, should remain consistent across segments
  - *From: 42hub*

- **SCAIL structure**: I2V model with 20 input channels, pose conditioning temporally concatenated at half resolution
  - *From: Kijai*

- **Asynchronous weight offloading**: ComfyUI feature that moves unused model weights to RAM while keeping active weights in VRAM, done asynchronously so it doesn't slow down generation if compute time is long
  - *From: Kijai*

- **SVI Pro 2.2**: LoRA for Wan 2.2 that enables longer I2V generations by chaining segments together using frames from previous generation plus original reference image
  - *From: blake37*

- **Prompt adapters vs LoRAs**: Prompt adapters tend to be better for things requiring subtlety like character and style, and are lighter weight than LoRAs
  - *From: pom*

- **RoPE shift/offset**: Temporal positioning method where frame indices are spread by factor of 5, e.g. 3 memory images get -15, -10, -5 positions
  - *From: Kijai*

- **Motion latent count**: Number of latents used by SVI node, typically last latent which represents 4 frames
  - *From: Kijai*

- **Sigma to step conversion**: Automatically sets split point based on sigma values instead of manual step selection
  - *From: Kijai*

- **SVI anchor system**: Uses anchor frames to prevent continuous drift - may drift initially but then stabilizes rather than continuing to degrade
  - *From: Ablejones*

- **Wan frame formula**: Wan accepts frames according to formula 1 + 4 × n, where first frame is reference and then 4 frames per latent
  - *From: JohnDopamine*

- **Resolution-dependent shift**: Higher resolution increases signal at given noise level, so you increase shift to increase noise level for equivalent SNR
  - *From: spacepxl*

- **Self-refine-video**: Technique using restart sampling with uncertainty masking to iteratively improve video generation quality
  - *From: mallardgazellegoosewildcat2*

- **Uncertainty mask**: Masks areas that didn't change from previous restart in self-refine process, though naming is somewhat loose
  - *From: mallardgazellegoosewildcat2*

- **RES sampler**: Higher-order explicit Runge Kutta with exponential integrator, actually a bug fix of DPM sampler
  - *From: mallardgazellegoosewildcat2*

- **Restart sampling**: Sampling technique that adds more noise than SDE, can be combined with SDE for both small per-step noise and big restart noise
  - *From: mallardgazellegoosewildcat2*

- **Self-refine video sampling**: Uses restart sampling with noise injection, can take you off known trajectory but SDE noise helps get back on track
  - *From: mallardgazellegoosewildcat2*

- **Double distillation effects**: Loading distillation LoRA on already distilled model causes excessive sharpening and artifacts
  - *From: mallardgazellegoosewildcat2*

- **Temporal VAE compression**: 8x temporal compression makes fast motion difficult for diffusion model, especially human body movement
  - *From: spacepxl*

- **Reference concatenation**: SkyReels concatenates reference images after noise, not before like VACE
  - *From: Kijai*

- **Self-Refine**: Similar to restart sampler, implemented for video generation improvement
  - *From: mallardgazellegoosewildcat2*

- **Skyreels Extend generation process**: First generate a single clip, then extract keyframes with logic based on total length (limited to 200 seconds)
  - *From: Kijai*

- **Bypassed nodes behavior**: Returns the value of first input from first output, matches output to input
  - *From: Kijai*

- **Attention mechanism**: Magic that connects different modalities - 'you just connect up different modalities with some attn and magically it works'
  - *From: mallardgazellegoosewildcat2*

- **Neural network performance**: Mostly down to cache misses, requires CUDA kernel analysis for proper performance analysis
  - *From: mallardgazellegoosewildcat2*


## Resources & Links

- **New 1217 LightX2V LoRA** (model)
  - https://huggingface.co/lightx2v/Wan2.2-Distill-Loras/blob/main/wan2.2_t2v_A14b_low_noise_lora_rank64_lightx2v_4step_1217.safetensors
  - *From: Elvaxorn*

- **Best LightX2V full models** (model)
  - https://huggingface.co/lightx2v/Wan2.2-Distill-Models/tree/main
  - *From: Benjimon*

- **ComfyUI StoryMem implementation** (repo)
  - https://github.com/anveshane/Comfyui_StoryMem
  - *From: TK_999*

- **H1111 story branch with UltraVico** (repo)
  - https://github.com/maybleMyers/H1111/tree/story
  - *From: Benjimon*

- **StereoPilot for 2D to 3D** (model)
  - https://huggingface.co/KlingTeam/StereoPilot
  - *From: DawnII*

- **SVI Pro native workflow by Kijai** (workflow)
  - https://discord.com/channels/1076117621407223829/1342763350815277067/1454805653599031358
  - *From: LukeG89*

- **SVI_v2_PRO LoRAs for native ComfyUI** (lora)
  - https://huggingface.co/Kijai/WanVideo_comfy/blob/main/LoRAs/Stable-Video-Infinity/v2.0/
  - *From: LukeG89*

- **HuMo + SVI workflow resource thread** (workflow)
  - https://discord.com/channels/1076117621407223829/1455601193660452995
  - *From: JohnDopamine*

- **HY-Motion-1.0 Hugging Face space** (model)
  - https://huggingface.co/spaces/tencent/HY-Motion-1.0
  - *From: tarn59*

- **Wan 2.2 fp8 mixed precision models** (model)
  - https://huggingface.co/silveroxides/Wan_2.2-fp8_scaled_hybrid/tree/main
  - *From: Lumifel*

- **Video understanding LLMs collection** (repo)
  - https://github.com/yunlong10/Awesome-LLMs-for-Video-Understanding
  - *From: buggz*

- **WanSoundTrajectory node for audio-reactive movement** (node)
  - https://github.com/drozbay/ComfyUI-WanSoundTrajectory
  - *From: Dream Making*

- **SVI v2.0 Pro LoRAs** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy/tree/main/LoRAs/Stable-Video-Infinity/v2.0
  - *From: Juan Gea*

- **WanVideoBlender node** (tool)
  - https://github.com/banodoco/steerable-motion
  - *From: Tachyon*

- **Wan community timeline** (resource)
  - https://wanx-troopers.github.io/timeline.html
  - *From: 42hub*

- **SVI workflows collection** (workflow)
  - https://wanx-troopers.github.io/svi.html#svi-20-pro
  - *From: 42hub*

- **LTX-2 model** (model)
  - https://huggingface.co/Lightricks/LTX-2
  - *From: ZeusZeus (RTX 4090)*

- **LTX-2 repository** (repo)
  - https://github.com/Lightricks/LTX-2
  - *From: ZeusZeus (RTX 4090)*

- **ComfyUI LTX-2 support** (repo)
  - https://github.com/comfyanonymous/ComfyUI/pull/11632
  - *From: LukeG89*

- **42hub's Wan resource site** (resource)
  - https://wanx-troopers.github.io/
  - *From: 42hub*

- **Timeline of Wan developments** (resource)
  - https://wanx-troopers.github.io/timeline.html
  - *From: 42hub*

- **LightX LoRA information** (resource)
  - https://wanx-troopers.github.io/loras/part-01.html
  - *From: 42hub*

- **LTX-2 models** (model)
  - https://huggingface.co/Lightricks/LTX-2/tree/main
  - *From: Ada*

- **ComfyUI-LTXVideo nodes** (tool)
  - https://github.com/Lightricks/ComfyUI-LTXVideo
  - *From: David Snow*

- **SCAIL AudioReactive** (tool)
  - https://github.com/ckinpdx/ComfyUI-SCAIL-AudioReactive
  - *From: AJO*

- **Wan 2.2 VACE models** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy_fp8_scaled/tree/main/VACE
  - *From: Blink*

- **DreamID-V support for WAN** (repo)
  - https://github.com/HM-RunningHub/ComfyUI_RH_DreamID-V
  - *From: NebSH*

- **LongCat Avatar GGUF models** (model)
  - https://huggingface.co/vantagewithai/LongCat-Video-Avatar-ComfyUI-GGUF/tree/main
  - *From: mdkb*

- **UniVideo - video editing model** (repo)
  - https://github.com/KlingTeam/UniVideo
  - *From: asd*

- **HummingbirdXT model** (model)
  - https://huggingface.co/amd/HummingbirdXT
  - *From: yi*

- **VerseCrafter model** (model)
  - https://huggingface.co/TencentARC/VerseCrafter
  - *From: yi*

- **WAN 2.2 GGUF Storyboard** (repo)
  - https://github.com/chrishill197724-gif/ComfyUI-Wan22-GGUF-Storyboard
  - *From: hicho*

- **CRT-Nodes for looping** (repo)
  - https://github.com/PGCRT/CRT-Nodes
  - *From: hudson223*

- **Wan 2.2 FFLF workflow** (workflow)
  - https://civitai.com/models/2074404?modelVersionId=2365252
  - *From: Canin17*

- **DreamID-V implementation** (repo)
  - https://github.com/bytedance/DreamID-V
  - *From: berserk4501*

- **UniPic3 CM models** (model)
  - https://huggingface.co/Skywork/Unipic3_cm
  - *From: 🦙rishappi*

- **Wan 2.2 NVFP4 models** (model)
  - https://huggingface.co/GitMylo/Wan_2.2_nvfp4/tree/main
  - *From: Ada*

- **VACE transition control node** (node)
  - https://old.reddit.com/r/comfyui/comments/1l93f7w/my_weird_custom_node_for_vace/
  - *From: JohnDopamine*

- **V-RGBX inverse rendering** (repo)
  - https://github.com/Aleafy/V-RGBX
  - *From: spacepxl*

- **InsertAnywhere** (repo)
  - https://github.com/myyzzzoooo/InsertAnywhere
  - *From: JohnDopamine*

- **ReCo model** (repo)
  - https://github.com/HiDream-ai/ReCo
  - *From: JohnDopamine*

- **Wan timeline resource** (resource)
  - https://wanx-troopers.github.io/timeline.html
  - *From: 42hub*

- **FlashVSR stable fork** (repo)
  - https://github.com/naxci1/ComfyUI-FlashVSR_Stable
  - *From: lostintranslation*

- **OmniTransfer (Wan 2.1 based)** (repo)
  - https://github.com/PangzeCheung/OmniTransfer
  - *From: JohnDopamine*

- **SVI notes** (resource)
  - https://wanx-troopers.github.io/svi.html
  - *From: 42hub*

- **Huggingface prompt tuning docs** (resource)
  - https://huggingface.co/docs/peft/en/package_reference/prompt_tuning
  - *From: mallardgazellegoosewildcat2*

- **ComfyUI-RGnodes** (repo)
  - https://github.com/rgamevfx/ComfyUI-RGnodes
  - *From: rryyaann*

- **OmniVideo2-A14B** (model)
  - https://huggingface.co/Fudan-FUXI/OmniVideo2-A14B
  - *From: yi*

- **StoryMem repo** (repo)
  - https://github.com/Kevin-thu/StoryMem
  - *From: JohnDopamine*

- **CamCloneMaster** (repo)
  - https://github.com/KlingTeam/CamCloneMaster
  - *From: sebi*

- **SVI 2.0 Pro for Wan 2.2** (repo)
  - https://github.com/vita-epfl/Stable-Video-Infinity/tree/svi_wan22
  - *From: lostintranslation*

- **SCAIL pose control** (model)
  - https://raw.githubusercontent.com/zai-org/SCAIL/refs/heads/master/resources/community2.gif
  - *From: lostintranslation*

- **FlashVSR upscaler** (repo)
  - https://github.com/naxci1/ComfyUI-FlashVSR_Stable
  - *From: lostintranslation*

- **DITTO style transfer** (repo)
  - https://github.com/EzioBy/Ditto
  - *From: JohnDopamine*

- **Wan 2.2 nvfp4 version** (model)
  - https://huggingface.co/GitMylo/Wan_2.2_nvfp4/tree/main
  - *From: dj47*

- **Quantization conversion tool** (tool)
  - https://github.com/silveroxides/convert_to_quant
  - *From: Shubhooooo*

- **Image batcher for VACE** (tool)
  - https://huggingface.co/Stkzzzz222/remixXL/blob/main/image_batcher_by_indexz.py
  - *From: Dream Making*

- **Self-refine-video implementation** (repo)
  - https://github.com/kijai/ComfyUI-WanVideoWrapper/tree/self-refine-video
  - *From: Kijai*

- **Self-refine-video original paper** (repo)
  - https://github.com/agwmon/self-refine-video
  - *From: Juampab12*

- **VHS color shift issue report** (issue)
  - https://github.com/Kosinkadink/ComfyUI-VideoHelperSuite/issues/529
  - *From: CaptHook*

- **UniVerse-1-Base model** (model)
  - https://huggingface.co/dorni/UniVerse-1-Base
  - *From: yi*

- **SkyReels V3** (repo)
  - https://github.com/SkyworkAI/SkyReels-V3
  - *From: yi*

- **Ace-Step v1.5 update** (repo)
  - https://github.com/ace-step/ace-step-v1.5.github.io
  - *From: JohnDopamine*

- **SkyReels V3 converted model** (model)
  - https://huggingface.co/Kijai/WanVideo_comfy_fp8_scaled/blob/main/SkyReelsV3/Wan21_SkyReels-V3-R2V_fp8_scaled_mixed.safetensors
  - *From: Kijai*

- **SkyReels V3 HuggingFace Space** (demo)
  - https://huggingface.co/spaces/Skywork/SkyReels-V3
  - *From: yi*

- **Self-refine video branch** (repo)
  - https://github.com/kijai/ComfyUI-WanVideoWrapper/tree/self-refine-video
  - *From: JohnDopamine*

- **NVIDIA FastGen research** (repo)
  - https://github.com/NVlabs/FastGen
  - *From: JohnDopamine*

- **MOVA OpenMOSS models** (model)
  - https://huggingface.co/OpenMOSS-Team/MOVA-720p/tree/main
  - *From: slmonker(5090D 32GB)*

- **SkyReels V3 GitHub** (repo)
  - https://github.com/SkyworkAI/SkyReels-V3
  - *From: Prelifik*

- **MOVA ComfyUI implementation** (repo)
  - https://github.com/HM-RunningHub/ComfyUI_RH_MOVA
  - *From: Lodis*

- **Self-refine video branch** (repo)
  - https://github.com/kijai/ComfyUI-WanVideoWrapper/tree/self-refine-video
  - *From: izashin*

- **MOVA Twitter announcement** (announcement)
  - https://x.com/cheng_qinyuan/status/2017118768040989157?s=20
  - *From: yi*

- **SetGet resolver script** (tool)
  - https://github.com/yujianvip/ComfyUI-SetGet-Resolver
  - *From: JohnDopamine*

- **HQ Image Save nodes** (node)
  - https://github.com/spacepxl/ComfyUI-HQ-Image-Save
  - *From: chrisd0073*

- **CoCoTools IO nodes** (node)
  - https://github.com/Conor-Collins/ComfyUI-CoCoTools_IO
  - *From: chrisd0073*

- **ComfyUI_Kitchen_nvfp4_Converter** (tool)
  - https://github.com/tritant/ComfyUI_Kitchen_nvfp4_Converter
  - *From: topmass*

- **YouTube video showing Wan 2.2** (demo)
  - https://youtu.be/AUcYJczWXT4?t=446
  - *From: hicho*


## Known Limitations

- **SVI/2.2 not good for multi-keyframe injection**
  - Not trained for keyframe interpolation like VACE, works worse than VACE for that use case
  - *From: Kijai*

- **StoryMem only works for 2 shots**
  - Shows glitches between sections even with many steps, not suitable for longer sequences
  - *From: Benjimon*

- **I2V prompt adherence issues**
  - Still far from true prompt adherence, often just rolling dice on each generation
  - *From: David Snow*

- **SteadyDancer has no face control**
  - Cannot work with face images from pose and face detection nodes
  - *From: Kijai*

- **SVI Pro tends toward slowmotion**
  - By design due to anchor frame mechanism - requires aggressive prompting to break away from anchor
  - *From: Ablejones*

- **SVI reverts character changes like outfit/hair color**
  - Due to anchor frame consistency mechanism pulling back to original appearance
  - *From: Zabo*

- **T2V to SVI Pro transition issues**
  - Difficult to get seamless transition between T2V video and first SVI Pro I2V - always some weird change in first few frames
  - *From: seitanism*

- **HuMo compatibility with Wan 2.2**
  - HuMo is trained on Wan 2.1 so workflows using Wan 2.2 HN stage are never completely perfect but work 'well enough'
  - *From: Ablejones*

- **Video models don't quantize well compared to LLMs**
  - Video diffusion models have quality issues with quantization while LLMs are happy in 4 bit
  - *From: mallardgazellegoosewildcat2*

- **SVI Pro only works with I2V models**
  - Cannot be used with T2V models, not compatible with VACE
  - *From: Kijai*

- **Video quality degrades over time with merged models**
  - More noticeable with base + many LoRAs, degradation compounds with extensions
  - *From: LukeG89*

- **SVI still has some degradation and color shifts**
  - After chaining many clips, despite improvements
  - *From: seitanism*

- **LongVie2 hit and miss when start image isn't exact**
  - Works better when using original video's first frame as start image
  - *From: Kijai*

- **5090 power connector rated for only ~20 reconnections**
  - Terrible design, should avoid frequent disconnecting
  - *From: Kijai*

- **PyTorch 2.11.0 has stability issues**
  - Nightly build causes various problems including VAE decoding OOM
  - *From: Kijai*

- **Wan 2.2 high+low requires significant RAM**
  - Needs 64GB RAM, 32GB is not enough for both models
  - *From: Blink*

- **Wan slow motion issues**
  - SVI can produce slow motion results intermittently, various factors affect this including LoRA choice
  - *From: cocktailprawn1212*

- **SCAIL memory intensive**
  - NLF processor in SCAIL is memory intensive
  - *From: Guey.KhalaMari*

- **Relight LoRA causes identity drift**
  - Using relight LoRA in WanAnimate causes identity drift issues
  - *From: harrisonwells*

- **LTX-2 bad at fast movements and small details**
  - LTX struggles with fast movements and fine details compared to Wan
  - *From: Zueuk*

- **SVI has no controlnet or prompt control**
  - Makes it too random for planned video shots compared to VACE
  - *From: mdkb*

- **VACE only takes one reference**
  - Cannot handle multiple references directly, people experiment with compound images
  - *From: 42hub*

- **SVI flickering issues with end frames**
  - Weird flickering artifacts when using end frames, different kind of bad when negative prompting flicker
  - *From: pom*

- **LongCat Avatar can't use WAN LoRAs**
  - No compatibility with existing WAN LoRA ecosystem
  - *From: mdkb*

- **Wan 2.2 Vi Pro can't do proper end frame generation**
  - Someone used different anchor claiming it's last frame but it's not really last frame generation
  - *From: Kijai*

- **NVFP4 doesn't support ControlNet or LoRAs yet**
  - Technology is currently half-baked according to user experience
  - *From: CaptHook*

- **Mocha doubles model input making it very slow**
  - Mocha is extremely slow, taking about 1 hour for 81 frames
  - *From: Kijai*

- **SCAIL hand detection isn't great**
  - Hand detection alignment often screws up, especially on closeups
  - *From: Kijai*

- **SVI Pro has color drift issues in longer generations**
  - Common issue with color shifting over time, Color Match node only partially helps
  - *From: blake37*

- **HPS and MPS reward LoRAs break SVI generation flow**
  - Can't use these LoRAs together with SVI Pro
  - *From: blake37*

- **SCAIL and HuMo can't work in same workflow**
  - Need to run as separate passes
  - *From: Dream Making*

- **Current open source video models limited to non-HD 5 second videos with simple motion**
  - Questioning what you can actually 'do' with current capabilities
  - *From: mallardgazellegoosewildcat2*

- **Normal maps not officially supported by VACE**
  - Not a trained VACE modality, though it somewhat works in practice
  - *From: Kijai*

- **V-RGBX doesn't know what to do with sky, eyes/pupils**
  - Generalization issues with certain scene elements, needs more AOVs like reflection/refraction
  - *From: spacepxl*

- **LTX2 licensing restrictions**
  - Can't commercialize if competing with LTX company, revenue share required for paid licenses
  - *From: mallardgazellegoosewildcat2*

- **Wan missing native audio and length**
  - Only has Ovi for audio, no native long duration support
  - *From: Kijai*

- **SVI 2 Pro motion issues**
  - Stilted motion and reduced prompt adherence, loses SVI benefits below 60% strength
  - *From: DevouredBeef*

- **StoryMem high lora strength**
  - Boosting StoryMem lora strength produces demon-like artifacts
  - *From: Kijai*

- **SVI still has color drift and quality loss**
  - Much better than VACE but both issues still exist, especially with extreme actions like faces going out of view
  - *From: lostintranslation*

- **SVI only receives last X frames plus anchor**
  - No awareness of objects or details that appeared earlier in sequence but not visible in recent frames
  - *From: Kijai*

- **SCAIL masked operations not officially supported**
  - No official masked SCAIL nodes exist currently, though theoretically possible
  - *From: mallardgazellegoosewildcat2*

- **KJNodes GetNode can't work in subgraphs**
  - Variables are scoped to each canvas instance rather than global, preventing subgraph use
  - *From: Kijai*

- **Self-refine doesn't work well with distill models**
  - Motion is defined too early in distill models for self-refine to be as effective
  - *From: Kijai*

- **Self-refine incompatible with er_sde sampler**
  - Cannot use self-refine technique with er_sde sampling method
  - *From: TK_999*

- **SCAIL slow with context windows**
  - Context windows make SCAIL generation very slow, better to disable for shorter videos
  - *From: Kijai*

- **UniVerse-1-Base undertrained**
  - Results show the model appears to be undertrained despite being 28GB
  - *From: yi*

- **Magi model installation complexity**
  - Requires special attention mechanism and is difficult to install, though not strictly necessary
  - *From: Lodis*

- **SkyReels V3 based on older Wan 2.1**
  - Not as good as Wan 2.2 for motion quality
  - *From: Kijai*

- **MOVA limited to 8 seconds**
  - Much shorter than LTX2's 30+ second capability
  - *From: Kijai*

- **MOVA demo clips are poor quality**
  - Examples shown are significantly worse than competing models
  - *From: Kijai*

- **SVI is fragile due to training method**
  - Trained using noise from specific generation setup, not very flexible
  - *From: mallardgazellegoosewildcat2*

- **VAE compression issues for distant subjects**
  - Very compressive VAE in spatial dimensions makes distant faces/objects require upscaling
  - *From: mallardgazellegoosewildcat2*

- **MOVA requires reference image**
  - Inference script requires --ref_path argument, may not support native T2V
  - *From: Shubhooooo*

- **MOVA doesn't support fp8 quantization**
  - Code doesn't do fp8, uses bf16 on everything
  - *From: yi*

- **MOVA installation complexity**
  - Need weird dependencies that can conflict with protobuf, more complex than usual custom nodes
  - *From: Stef*

- **Skyreels Extend has fps issues**
  - Movement is jerky/unnatural, lipsync feels off despite using 25fps
  - *From: Kijai*

- **VACE with depth maps poor for facial features**
  - Depth map doesn't have enough info for eye and mouth movement transfer
  - *From: Albert*

- **Scaled fp8 models can't be merged simply**
  - Cannot merge VACE with Skyreels due to fp8 scaling
  - *From: Kijai*

- **HuMo can't natively do long generations**
  - Need to combine with other methods like InfiniteTalk or MultiTalk with SVI
  - *From: Kijai*

- **NVFP4 conversion is very lossy without calibration**
  - Simple conversion results in quality loss
  - *From: Kijai*

- **SVI 2.0 Pro branch lacks proper documentation for Wan 2.2 training**
  - Not well documented for training on Wan 2.2 instead of 2.1
  - *From: Persoon*


## Hardware Requirements

- **SVI workflow memory usage**
  - Memory blows up after second extension during VAE decode, crashes after 3 hours of testing
  - *From: TK_999*

- **RAM management on RunPod**
  - 76GB RAM gets frozen, need to restart pod frequently due to memory leaks
  - *From: Dannhauer80*

- **RTX 5090 performance**
  - 49 minutes for 15 videos (81 frames, 720x1280, 6 steps) with 123GB RAM and AMD Ryzen 9 9950X
  - *From: Kevin "Literally Who?" Abanto*

- **RTX 5090 power connector issues**
  - 16-pin connector problems causing melting/burning. Power consumption ridiculously high. Issues across brands (Gigabyte, ASUS, MSI)
  - *From: slmonker(5090D 32GB)*

- **PSU recommendation for RTX 5090**
  - Corsair RME series recommended over Great Wall 1250W 80plus gold which had issues
  - *From: Charlie*

- **32GB RAM insufficient for Wan 2.2**
  - Not enough to run Wan 2.2 properly
  - *From: Zueuk*

- **LTX-2 fits in 24GB VRAM**
  - 19B parameter model should fit in 24GB with offloading
  - *From: ZeusZeus (RTX 4090)*

- **5090 temperature management**
  - Regularly hits 85C, undervolting recommended for better performance
  - *From: cyncratic*

- **Vast vs RunPod performance**
  - RunPod: 5 seconds per image, Vast: 60 seconds per image with Wan
  - *From: Kevin "Literally Who?" Abanto*

- **RAM for video models**
  - At least 64GB recommended, some users have 128GB. 32GB minimum for hobby use with GGUFs. One user reported 60GB usage during 1080p LTX generation
  - *From: Juampab12 / patientx / David Snow*

- **Wan 2.2 high+low VRAM**
  - Requires significant VRAM to run both models, can use low-noise only if limited
  - *From: Blink*

- **Linux vs Windows VRAM handling**
  - Windows has unified shared memory for temporary VRAM spikes, Linux is strict and causes instant OOM. WSL2 provides native Linux speed with Windows shared VRAM benefits
  - *From: craftogrammer*

- **WAN 2.2 with model splitting**
  - 896x512 2-stage I2V+A at 25 FPS 30 sec took 18 min 40 sec without touching swap file
  - *From: psylent_gamer*

- **32GB RAM for casual use**
  - Might survive on 32GB if just playing around, not for serious work
  - *From: Juampab12*

- **LongCat Avatar VRAM usage**
  - 30 minutes generation time on RTX 3060 for 93 frames at 832x480 with 12 steps
  - *From: mdkb*

- **RAM usage for multiple models**
  - User reported 244GB/250GB RAM usage with Flux2, Wan2.2 models, VACE, SVI 2.0 Pro and LoRAs loaded
  - *From: seitanism*

- **Mocha performance**
  - Mocha is 50% slower than base model due to doubling model input
  - *From: Kijai*

- **SCAIL performance**
  - SCAIL is about 50% slower because it halves pose image resolution
  - *From: Kijai*

- **Wan 2.2 FP16 VRAM usage**
  - Can run on 16GB VRAM despite 53GB model size due to ComfyUI's weight offloading
  - *From: SantaHunter*

- **VRAM requirements depend on model and system**
  - Can't simply add VRAM and RAM together, depends on specific model and system configuration
  - *From: Kijai*

- **Block swap speed improvements**
  - 10% speed improvement reported even with q4/q3 models when using block swap
  - *From: patientx*

- **MultiTalk memory usage**
  - VRAM usage significantly reduced through mask chunking optimizations
  - *From: Kijai*

- **NAG memory optimization**
  - NAG will not increase memory use at all with new optimizations
  - *From: Kijai*

- **PyTorch 2.10**
  - Works fine but no major performance improvements, some users experience OOM errors
  - *From: topmass*

- **VRAM optimization for InfiniteTalk**
  - New optimizations save 1GB+ VRAM for 720p 81 frames, needs high resolution to be effective
  - *From: Kijai*

- **Disk speed for T5 encoder**
  - Should load 11GB umt5-xxl-enc-bf16.safetensors in few seconds on good SSD like Samsung 990 Pro, not 85 seconds
  - *From: Kijai*

- **SCAIL VRAM usage**
  - Uses more VRAM than regular Wan, ~20GB for 720p with 30 block swap on 4090
  - *From: Kijai*

- **12GB VRAM limitations**
  - Difficult to run newer models like Stepvideo and Magi due to 30+ billion parameters
  - *From: mallardgazellegoosewildcat2*

- **Self-refine performance impact**
  - Increases generation time by 50% due to additional model calls
  - *From: Kijai*

- **MOVA VRAM usage**
  - 55GB VRAM for 94 frames 720p, 72GB VRAM for 193 frames, 45GB RAM
  - *From: Stef*

- **MOVA generation time**
  - 1h15 gen time for 8 sec 720p video, 5 hours for longer generations
  - *From: Stef*

- **NVFP4 models initial VRAM usage**
  - Around 20GB VRAM when both models loaded, but faster generation after load
  - *From: topmass*

- **NVFP4 conversion speed**
  - 45 seconds conversion time on RTX 5090
  - *From: topmass*

- **Audio model performance**
  - Acestep 1.5 requires about 4-10 seconds for 4 min generation
  - *From: yi*


## Community Creations

- **WanEx I2VDifferenceAugmentation** (node)
  - Renamed node for difference augmentation in longer videos, applies augmentation per frame with scheduling
  - *From: Ablejones*

- **SVI Pro 2.0 workflow with multiple optimizations** (workflow)
  - Combines SVI Pro + Longlook motion scale + RCM 2.2 + upscale/interpolation for budget VEO3 alternative
  - *From: Elvaxorn*

- **Fast Film Grain Node OOM fix** (workflow)
  - Use Rebatch Images node before (240 or lower) and after (max value) Fast Film grain node to prevent OOMs
  - *From: Elvaxorn*

- **WanVideoBlender node fork** (node)
  - Fork of existing node used for making PR
  - *From: Ablejones*

- **SVI v2 Pro wrapper workflow** (workflow)
  - Example workflow for using SVI v2 Pro with the wrapper
  - *From: Juan Gea*

- **42hub's Wan resource website** (resource)
  - Comprehensive collection of Wan information, timelines, and LoRA recommendations
  - *From: 42hub*

- **ComfyUI-Kitchen** (tool)
  - Addition to ComfyUI to help with fp8 and fp4 support
  - *From: Tachyon*

- **Generation Timer with bold numbers** (node)
  - Shows generation time in bold format, more useful than checking terminal
  - *From: Elvaxorn*

- **Batch upscaler workflow for WAN 2.2 low** (workflow)
  - Standalone batch processing for long videos with frame/resolution balance
  - *From: Ivoxx*

- **Beat-locked auto video editor** (tool)
  - Gradio app for automatic multi-camera editing synced to music using stem analysis
  - *From: VRGameDevGirl84(RTX 5090)*

- **Unlimited length video nodes** (node)
  - Nodes for chunk-based unlimited length video generation with re-do capability
  - *From: VRGameDevGirl84(RTX 5090)*

- **Prompt splitter node** (node)
  - Node that splits prompts and uses them on each run
  - *From: VRGameDevGirl84(RTX 5090)*

- **Face similarity ranking tool** (tool)
  - Tool to rank/sort/rename faces for similarity comparison using deepface, helpful for dataset preparation
  - *From: JohnDopamine*

- **First Middle Last Frame workflow** (workflow)
  - Workflow that handles multiple frame inputs including middle frames for music video creation
  - *From: VRGameDevGirl84(RTX 5090)*

- **Image sequence overwrite node** (node)
  - Node being developed to overwrite image sequences in same directory
  - *From: VRGameDevGirl84(RTX 5090)*

- **RGnodes** (nodes)
  - VACE tailored nodes that also work for other video/mask needs
  - *From: rryyaann*

- **StoryMem RoPE implementation** (code)
  - Proper RoPE offset implementation for StoryMem functionality
  - *From: Kijai*

- **Memory optimization for attention blocks** (optimization)
  - Reduces VRAM usage for high resolution InfiniteTalk workflows by 1GB+
  - *From: Kijai*

- **Combined upscale and downscale node** (node)
  - Combines upscale model with lanczos downscaling to save RAM by avoiding intermediate caching
  - *From: Kijai*

- **Auto-connected node insertion** (workflow tool)
  - Right-click context menu to add commonly used nodes like GetNode with automatic connections
  - *From: Kijai*

- **WanVideoWrapper self-refine branch** (node)
  - Implementation of self-refine-video technique for Wan models in ComfyUI
  - *From: Kijai*

- **Color correction workflow solution** (workflow)
  - Workflow using color correct nodes to compensate for VHS color drift issues
  - *From: CaptHook*

- **SkyReels V3 ComfyUI conversion** (model)
  - Converted SkyReels V3 R2V model for ComfyUI compatibility
  - *From: Kijai*

- **Diffusers to ComfyUI conversion script** (tool)
  - Custom script to convert diffusers format models, can strip quantization
  - *From: Kijai*

- **Long sequence generator workflow** (workflow)
  - Very long sequence generator with image batch joining for multiple premade chunks
  - *From: lostintranslation*
